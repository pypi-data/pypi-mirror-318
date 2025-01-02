from __future__ import annotations

import os
import sys

from cookiecutter.main import cookiecutter


def main() -> None:
    """Create a new Python project using the uvi template."""
    try:
        # When installed as a package, use the local template
        if os.path.exists(os.path.join(os.path.dirname(__file__), "..", "cookiecutter.json")):
            template = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        # When used directly via cookiecutter, use the GitHub repo
        else:
            template = "https://github.com/shaneholloman/uvi.git"

        # Run cookiecutter with the template
        cookiecutter(
            template,
            no_input=False,  # Enable interactive prompts
            overwrite_if_exists=False,  # Don't overwrite existing projects
        )
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
