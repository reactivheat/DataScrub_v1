"""
File type detection.

Extension-based is fine for v0.1 (fast, no deps). If it turns out to be
unreliable (renamed files, no extension), swap to magic-byte sniffing later
via `python-magic` — but that adds a system dependency (libmagic), so keep
it optional/deferred.
"""

from pathlib import Path

ALL_SUPPORTED_EXT = {
    ".jpg", ".jpeg", ".png",   # images
    ".pdf",                    # pdf
    ".docx", ".xlsx",          # office (v0.2)
}


def is_supported(path: Path) -> bool:
    return path.suffix.lower() in ALL_SUPPORTED_EXT


def get_file_category(path: Path) -> str:
    """Return 'image' | 'pdf' | 'office' | 'unknown' — used to pick the right reader/scrubber."""
    # TODO: map extension -> category string
    raise NotImplementedError
