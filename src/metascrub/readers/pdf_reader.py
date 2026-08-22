"""
PDF metadata reader.

Library: pypdf

Key fields to extract (from reader.metadata / DocumentInformation dict):
- /Author, /Creator, /Producer, /CreationDate, /ModDate, /Title
- Also worth checking: embedded XMP metadata (can duplicate or add to the above)

Note: scanned/image-only PDFs still carry document info metadata even if
there's no extractable text — don't assume "no text = no metadata".
"""

from pathlib import Path

from .base import BaseReader


class PDFReader(BaseReader):
    SUPPORTED_EXT = {".pdf"}

    def supports(self, path: Path) -> bool:
        return path.suffix.lower() in self.SUPPORTED_EXT

    def read(self, path: Path) -> dict:
        # TODO:
        # 1. pypdf.PdfReader(str(path))
        # 2. reader.metadata -> map to Author/Creator/Producer/CreationDate/Title
        # 3. optionally check reader.xmp_metadata for extra fields
        # 4. return findings dict
        raise NotImplementedError
