import os
import sys
import tempfile
from pathlib import Path
from typing import Iterable

import PyInstaller.__main__

DEFAULT_EXCLUDE_MODULES = (
    "IPython",
    "jedi",
    "fastapi",
    "watchfiles",
    "uvicorn",
    "fastapi",
)


def compile_executable_for_onprem(
    *,
    module_name: str,
    connector_root_dir: Path,
    exclude_modules: Iterable[str],
    sdk_root: Path,
    compile_directory: Path | None = None,
) -> None:
    connector_main_path = connector_root_dir / module_name / "main.py"
    if not os.path.isfile(connector_main_path):
        raise RuntimeError(f"No entrypoint found for {module_name} at {connector_main_path}")
    compile_directory = compile_directory or Path(tempfile.mkdtemp())

    print(f"Compiling executable for {module_name} in {compile_directory}", file=sys.stderr)
    PyInstaller.__main__.run(
        [
            str(connector_main_path.absolute()),
            "--clean",
            f"--paths={sdk_root.absolute()}",
            "-y",
            f"--distpath={compile_directory / 'dist'}",
            f"--workpath={compile_directory / 'work'}",
            f"--specpath={compile_directory / 'spec'}",
            "--log-level=ERROR",
            *[f"--exclude-module={module}" for module in exclude_modules],
        ]
    )
    print("Compiled to:", file=sys.stderr)
    print(compile_directory / "dist" / "main" / "main")
