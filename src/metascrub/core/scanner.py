"""
File discovery.

Responsibilities:
- Given a path (file or folder), yield the list of files to process
- Respect --recursive flag
- Filter by supported extensions (delegate to utils.file_types)
- Skip files that are too large / unreadable, and report why (don't crash silently)
"""

from pathlib import Path


def discover_files(path: str, recursive: bool = False) -> list[Path]:
    """
    Return a list of Path objects to be processed.

    TODO:
    - if path is a single file -> return [Path(path)] if supported
    - if path is a folder -> glob("*") or rglob("*") depending on `recursive`
    - filter using utils.file_types.is_supported(path)
    """
    raise NotImplementedError
