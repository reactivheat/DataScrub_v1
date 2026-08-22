"""
PDF metadata scrubber.

Approach: pypdf.PdfWriter — copy all pages from the reader, then explicitly
overwrite /Info metadata with an empty dict via writer.add_metadata({}).
Also strip XMP metadata if present (writer.xmp_metadata = None where supported).
"""

from pathlib import Path

from .base import BaseScrubber


class PDFScrubber(BaseScrubber):
    SUPPORTED_EXT = {".pdf"}

    def supports(self, path: Path) -> bool:
        return path.suffix.lower() in self.SUPPORTED_EXT

    def scrub(self, src: Path, dest: Path) -> dict:
        # TODO:
        # reader = PdfReader(str(src))
        # writer = PdfWriter()
        # for page in reader.pages: writer.add_page(page)
        # writer.add_metadata({})  # wipes /Info dict
        # with open(dest, "wb") as f: writer.write(f)
        raise NotImplementedError
