"""UVI - A Python project template using uv for dependency management."""

from __future__ import annotations
from pathlib import Path
import tomli


def get_version() -> str:
    """Retrieve the project version from pyproject.toml."""
    pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
    with open(pyproject_path, "rb") as f:
        pyproject_data = tomli.load(f)
    return pyproject_data["project"]["version"]


__version__ = get_version()
