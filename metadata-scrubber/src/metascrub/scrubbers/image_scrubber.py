"""
Image metadata scrubber.

Approach: re-save the image via Pillow WITHOUT passing the exif kwarg —
this is the simplest reliable way to drop EXIF entirely. Alternative for
JPEG-only, faster on large batches: piexif.remove(src, dest).

Watch out for:
- PNG text chunks (tEXt/iTXt) aren't touched by "drop exif" — need explicit
  chunk stripping via Pillow's PngImagePlugin
- Re-saving changes file size / recompresses JPEG — decide whether to
  preserve original quality setting (img.save(..., quality=95))
"""

from pathlib import Path

from .base import BaseScrubber


class ImageScrubber(BaseScrubber):
    SUPPORTED_EXT = {".jpg", ".jpeg", ".png"}

    def supports(self, path: Path) -> bool:
        return path.suffix.lower() in self.SUPPORTED_EXT

    def scrub(self, src: Path, dest: Path) -> dict:
        # TODO:
        # img = Image.open(src)
        # data = list(img.getdata())
        # clean_img = Image.new(img.mode, img.size)
        # clean_img.putdata(data)
        # clean_img.save(dest)  # no exif kwarg = no EXIF written
        # return summary of what was stripped (reuse ImageReader.read(src) findings for the "before")
        raise NotImplementedError
