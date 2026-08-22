"""
Image metadata reader.

Target formats: JPG, PNG, HEIC (v0.2+)
Libraries: Pillow (general image handling) + piexif (raw EXIF dict access)

Key fields to extract:
- GPS (GPSInfo IFD) -> convert DMS to decimal via utils.gps.dms_to_decimal
- Device make/model (Make, Model tags)
- Software/OS used to edit (Software tag)
- Original timestamp (DateTimeOriginal)
- Owner/author if present (Artist, Copyright tags — rare but happens)

Note: PNG doesn't have EXIF by default but can carry tEXt/iTXt chunks
(often software name, sometimes more) — handle separately from JPEG EXIF.
"""

from pathlib import Path

from .base import BaseReader


class ImageReader(BaseReader):
    SUPPORTED_EXT = {".jpg", ".jpeg", ".png"}  # add .heic in v0.2

    def supports(self, path: Path) -> bool:
        return path.suffix.lower() in self.SUPPORTED_EXT

    def read(self, path: Path) -> dict:
        # TODO:
        # 1. open with Pillow: Image.open(path)
        # 2. get exif dict via img.getexif() or piexif.load(str(path))
        # 3. pull GPSInfo IFD, decode with utils.gps
        # 4. map raw EXIF tag IDs -> human-readable keys (Make, Model, Software, DateTimeOriginal)
        # 5. return findings dict matching the shape in core/report.py
        raise NotImplementedError
