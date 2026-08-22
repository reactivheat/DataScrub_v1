"""
Office document metadata reader — planned for v0.2, scaffolded now so the
interface is consistent from day one.

Formats: DOCX (python-docx), XLSX (openpyxl)

Key fields (core_properties in both libraries):
- author, last_modified_by, created, modified, company, title, comments

Note: DOCX/XLSX are zip archives under the hood — core_properties comes
from docProps/core.xml. If python-docx/openpyxl ever fall short, that XML
can always be read directly as a fallback.
"""

from pathlib import Path

from .base import BaseReader


class OfficeReader(BaseReader):
    SUPPORTED_EXT = {".docx", ".xlsx"}

    def supports(self, path: Path) -> bool:
        return path.suffix.lower() in self.SUPPORTED_EXT

    def read(self, path: Path) -> dict:
        # TODO:
        # if .docx -> python_docx.Document(path).core_properties
        # if .xlsx -> openpyxl.load_workbook(path).properties
        # map author / last_modified_by / company / created / modified -> findings dict
        raise NotImplementedError
