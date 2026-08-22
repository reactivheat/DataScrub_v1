"""
Office document scrubber — v0.2 scope, scaffolded now for interface consistency.

Approach: load core_properties via python-docx / openpyxl, overwrite each
field (author, last_modified_by, company, comments, etc.) with empty string
or None, then save to `dest`.
"""

from pathlib import Path

from .base import BaseScrubber


class OfficeScrubber(BaseScrubber):
    SUPPORTED_EXT = {".docx", ".xlsx"}

    def supports(self, path: Path) -> bool:
        return path.suffix.lower() in self.SUPPORTED_EXT

    def scrub(self, src: Path, dest: Path) -> dict:
        # TODO:
        # doc = Document(src) / load_workbook(src)
        # props = doc.core_properties
        # props.author = ""; props.last_modified_by = ""; props.company = ""; ...
        # doc.save(dest)
        raise NotImplementedError
