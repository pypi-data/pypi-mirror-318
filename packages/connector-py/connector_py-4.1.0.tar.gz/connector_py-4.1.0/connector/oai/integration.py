"""Utility class to manage connector implementation.

:py:class:`Integration` provides a single point to register Integration
capabilities.

By instantiating the :py:class:`Integration` you simply create a basic
integration without any real implementation. To actually implement any
capability, you have to define (async) function outside the class and
register them to the integration instance by decorating the
implementation with ``@integration.register_capability(name)``.

Capability function has to:
    * accept only one argument
    * return scalar response

The :py:class:`Integration` is as much type-hinted as possible and also
does several checks to ensure that the implementation "is correct".
Incorrect implementation should raise an error during application start
(fail fast).

What is checked (at application start):
    * capability name is known (defined in ``StandardCapabilityName`` enum)
    * the types of accepted argument and returned value matches the
    capability interface
"""

import inspect
import json
import logging
import typing as t
from dataclasses import asdict, dataclass

from pydantic import BaseModel, ValidationError

from connector.generated import (
    AppCategory,
    AuthCredential,
    BasicCredential,
    CapabilitySchema,
    EntitlementType,
    Error,
    ErrorCode,
    ErrorResponse,
    Info,
    InfoResponse,
    JWTCredential,
    OAuthClientCredential,
    OAuthCredential,
    ResourceType,
    StandardCapabilityName,
    TokenCredential,
)
from connector.oai.capability import (
    CapabilityCallableProto,
    capability_requires_auth,
    generate_capability_schema,
    get_capability_annotations,
    validate_capability,
)
from connector.oai.errors import ErrorMap, handle_exception
from connector.oai.modules.base_module import BaseIntegrationModule
from connector.oai.modules.oauth_module import OAuthModule
from connector.oai.modules.oauth_module_types import OAuthSettings

AuthSetting: t.TypeAlias = t.Union[
    t.Type[OAuthCredential],
    t.Type[OAuthClientCredential],
    t.Type[BasicCredential],
    t.Type[TokenCredential],
    t.Type[JWTCredential],
]

logger = logging.getLogger(__name__)


class IntegrationError(Exception):
    """Base class for exceptions raised by Integration."""


class DuplicateCapabilityError(IntegrationError):
    """Raised when registering the same capability repeatedly."""

    def __init__(self, capability_name: StandardCapabilityName) -> None:
        super().__init__(f"{capability_name} already registered")


class InvalidAppIdError(IntegrationError):
    """Raised when app_id is not valid.

    Most probably, empty or containing only whitespaces.
    """


@dataclass
class DescriptionData:
    user_friendly_name: str
    categories: list[AppCategory]
    description: str | None = None
    logo_url: str | None = None


@dataclass
class CapabilityMetadata:
    display_name: str | None = None
    description: str | None = None


class EmptySettings(BaseModel):
    pass


class Integration:
    app_id: str
    settings_model: t.Type[BaseModel]

    def __init__(
        self,
        *,
        app_id: str,
        version: str,
        exception_handlers: ErrorMap,
        auth: AuthSetting,
        description_data: DescriptionData,
        handle_errors: bool = True,
        resource_types: list[ResourceType] | None = None,
        entitlement_types: list[EntitlementType] | None = None,
        settings_model: t.Type[BaseModel] | None = None,
        oauth_settings: OAuthSettings | None = None,
    ):
        self.app_id = app_id.strip()
        self.version = version
        self.auth = auth
        self.exception_handlers = exception_handlers
        self.handle_errors = handle_errors
        self.description_data = description_data
        self.resource_types = resource_types or []
        self.entitlement_types = entitlement_types or []
        self.settings_model = settings_model or EmptySettings
        self.oauth_settings = oauth_settings

        if len(self.app_id) == 0:
            raise InvalidAppIdError

        self.capabilities: dict[str, CapabilityCallableProto[t.Any]] = {}
        self.capability_display_name: dict[str, str | None] = {}
        self.capability_description: dict[str, str | None] = {}
        self.modules: list[BaseIntegrationModule] = []

        if self.oauth_settings:
            self.add_module(OAuthModule())

    def add_module(self, module: BaseIntegrationModule):
        self.modules.append(module)
        module.register(self)

    def register_capability(
        self,
        name: StandardCapabilityName,
        display_name: str | None = None,
        description: str | None = None,
    ) -> t.Callable[
        [CapabilityCallableProto[t.Any]],
        CapabilityCallableProto[t.Any],
    ]:
        """Add implementation of specified capability.

        This function is expected to be used as a decorator for a
        capability implementation.

        Display name is an optional text to display for the integration capability,
        in place of the default behavior with is to use the capability name.

        Description is an optional 1-2 sentence description of any unusual behaviors
        of the capability, rendered for the end user.

        Raises
        ------
        RuntimeError:
            When capability is registered more that once.
        """
        if name.value in self.capabilities:
            raise DuplicateCapabilityError(name)

        def decorator(
            func: CapabilityCallableProto[t.Any],
        ) -> CapabilityCallableProto[t.Any]:
            validate_capability(name, func)
            self.capabilities[name.value] = func
            self.capability_display_name[name.value] = display_name
            self.capability_description[name.value] = description
            return func

        return decorator

    def register_capabilities(
        self,
        capabilities: dict[
            StandardCapabilityName,
            CapabilityCallableProto[t.Any]
            | tuple[CapabilityCallableProto[t.Any], CapabilityMetadata],
        ],
    ):
        """
        Register a dictionary of capabilities.

        This is a convenience method to register multiple capabilities at once.
        You can pass a tuple of (capability, metadata) to register a capability, along with any
        configuration specific to that capability, such as display_name, description, etc

        eg.
        ```
        integration.register_capabilities({
            StandardCapabilityName.VALIDATE_CREDENTIALS: (
                validate_credentials, CapabilityMetadata(description="Test")
            ),
            StandardCapabilityName.LIST_ACCOUNTS: list_accounts,
        })
        ```
        """
        for name, capability in capabilities.items():
            if isinstance(capability, tuple):
                func, metadata = capability
                self.register_capability(name, **asdict(metadata))(func)
            else:
                self.register_capability(name)(capability)

    async def dispatch(self, name: StandardCapabilityName, request_string: str) -> str:
        """Call implemented capability, returning the result.

        Raises
        ------
        NotImplementedError:
            When capability is not implemented (or registered)
        """
        try:
            capability = self.capabilities[name.value]
        except KeyError:
            if self.handle_errors:
                return ErrorResponse(
                    is_error=True,
                    error=Error(
                        message=f"Capability '{name.value}' is not implemented.",
                        error_code=ErrorCode.NOT_IMPLEMENTED,
                        app_id=self.app_id,
                    ),
                ).model_dump_json()
            raise NotImplementedError from None

        json_object = json.loads(request_string)
        if json_object and "auth" in json_object:
            try:
                auth_credential = AuthCredential.model_validate(json_object["auth"])
            except ValidationError:
                return ErrorResponse(
                    is_error=True,
                    error=Error(
                        message="Malformed auth in request",
                        error_code=ErrorCode.BAD_REQUEST,
                        app_id=self.app_id,
                    ),
                ).model_dump_json()
            missing = "Nothing"
            if self.auth == BasicCredential:
                if not auth_credential.basic:
                    missing = "basic"
            elif self.auth == OAuthCredential:
                if not auth_credential.oauth:
                    missing = "oauth"
            if missing != "Nothing":
                return ErrorResponse(
                    is_error=True,
                    error=Error(
                        message=f"Missing '{missing}' auth in request",
                        error_code=ErrorCode.BAD_REQUEST,
                        app_id=self.app_id,
                    ),
                ).model_dump_json()
        elif capability_requires_auth(name):
            return ErrorResponse(
                is_error=True,
                error=Error(
                    message="Missing auth in request",
                    error_code=ErrorCode.BAD_REQUEST,
                    app_id=self.app_id,
                ),
            ).model_dump_json()

        request_annotation, _ = get_capability_annotations(capability)
        try:
            request = request_annotation.model_validate(json_object)
        except ValidationError as e:
            return ErrorResponse(
                is_error=True,
                error=Error(
                    message=f"Invalid request - {repr(e.errors())}",
                    error_code=ErrorCode.BAD_REQUEST,
                    app_id=self.app_id,
                ),
            ).model_dump_json()

        # Parse and validate the connector settings before dispatching
        if self.settings_model == EmptySettings:
            pass
        elif request.settings is None and self.handle_errors:
            return ErrorResponse(
                is_error=True,
                error=Error(
                    message=f"No settings passed on request: {self.app_id} requires {self.settings_model.__name__}",
                    error_code=ErrorCode.BAD_REQUEST,
                    app_id=self.app_id,
                ),
            ).model_dump_json()
        else:
            try:
                self.settings_model.model_validate(request.settings)
            except ValidationError:
                return ErrorResponse(
                    is_error=True,
                    error=Error(
                        message="Invalid settings passed on request",
                        error_code=ErrorCode.BAD_REQUEST,
                        app_id=self.app_id,
                    ),
                ).model_dump_json()

        try:
            if inspect.iscoroutinefunction(capability):
                response = await capability(request)
            else:
                response = t.cast(
                    BaseModel,
                    capability(request),
                )

            return response.model_dump_json()
        except Exception as e:
            return handle_exception(
                self.exception_handlers, e, capability, self.app_id
            ).model_dump_json()

    def info(self) -> InfoResponse:
        """Provide information about implemented capabilities.

        Json schema describing implemented capabilities and their
        interface is returned. The authentication schema is also
        included.
        """
        capability_names = sorted(self.capabilities.keys())
        capability_schema: dict[str, CapabilitySchema] = {}
        for capability_name in capability_names:
            command_types = generate_capability_schema(
                capability_name, self.capabilities[capability_name]
            )

            display_name: str | None = capability_name.replace("_", " ").title()
            if (
                capability_name in self.capability_display_name
                and self.capability_display_name[capability_name] is not None
                and isinstance(self.capability_display_name[capability_name], str)
            ):
                display_name = self.capability_display_name[capability_name]

            description = None
            if (
                capability_name in self.capability_description
                and self.capability_description[capability_name] is not None
                and isinstance(self.capability_description[capability_name], str)
            ):
                description = self.capability_description[capability_name]

            capability_schema[capability_name] = CapabilitySchema(
                argument=command_types.argument,
                output=command_types.output,
                display_name=display_name,
                description=description,
            )

        oauth_scopes = None
        if self.oauth_settings:
            oauth_scopes = {
                capability.value: scope
                for capability, scope in self.oauth_settings.scopes.items()
                if scope is not None
            }

        return InfoResponse(
            response=Info(
                app_id=self.app_id,
                version=self.version,
                capabilities=capability_names,
                capability_schema=capability_schema,
                logo_url=self.description_data.logo_url,
                user_friendly_name=self.description_data.user_friendly_name,
                description=self.description_data.description,
                categories=self.description_data.categories,
                resource_types=self.resource_types,
                entitlement_types=self.entitlement_types,
                request_settings_schema=self.settings_model.model_json_schema(),
                authentication_schema=self.auth.model_json_schema(),
                oauth_scopes=oauth_scopes,
            )
        )
