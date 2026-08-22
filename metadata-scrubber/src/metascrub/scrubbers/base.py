"""
Abstract interface all scrubbers must implement.

Golden rule for this whole module: NEVER modify the original file in place.
Always write to a new path (default: ./cleaned/<original_name>) and let the
user opt into overwrite explicitly later if they really want it.
"""

from abc import ABC, abstractmethod
from pathlib import Path


class BaseScrubber(ABC):
    @abstractmethod
    def supports(self, path: Path) -> bool:
        raise NotImplementedError

    @abstractmethod
    def scrub(self, src: Path, dest: Path) -> dict:
        """
        Write a metadata-stripped copy of `src` to `dest`.
        Return a dict summarizing what was removed (feeds into core/report.py).
        """
        raise NotImplementedError
