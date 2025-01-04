"""This module contains utility functions for the slimcontext parsers.

Copyright (c) 2024 Neil Schneider
"""

from pathlib import Path


def generate_context_header(file_path: Path, root_dir: Path | None = None) -> list[str]:
    """Generate the standard context header with a relative path (if possible).

    Returns:
        String - File break and path relative to project root.
    """
    try:
        relative_path = file_path.relative_to(root_dir) if root_dir else file_path.resolve()
    except ValueError:
        # If file_path is not under root_dir
        relative_path = file_path.resolve()

    return [
        '\n******',
        f'File: {relative_path}\n',
    ]
