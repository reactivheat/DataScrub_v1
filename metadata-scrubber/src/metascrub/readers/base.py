"""
Abstract interface all metadata readers must implement.

Why an abstract base: cli.py and core/scanner.py should never need to know
whether a file is a JPG or a DOCX — they just call `.read(path)` and get a
consistent dict back. This is what lets you add new file types later
(HEIC, video EXIF, etc.) without touching the CLI or report code.
"""

from abc import ABC, abstractmethod
from pathlib import Path


class BaseReader(ABC):
    """Every reader takes a file path and returns a findings dict (see core/report.py shape)."""

    @abstractmethod
    def supports(self, path: Path) -> bool:
        """Return True if this reader can handle the given file (by extension/magic bytes)."""
        raise NotImplementedError

    @abstractmethod
    def read(self, path: Path) -> dict:
        """Extract metadata and return it as a findings dict."""
        raise NotImplementedError
