"""
GPS coordinate helpers.

EXIF stores GPS as Degrees/Minutes/Seconds (DMS) tuples plus a ref
(N/S/E/W), not plain decimal — this converts to the decimal lat/lon that's
actually usable for a map preview.
"""


def dms_to_decimal(dms: tuple, ref: str) -> float:
    """
    Convert an EXIF GPS DMS tuple (degrees, minutes, seconds) + hemisphere
    ref ('N'/'S'/'E'/'W') into a signed decimal degree float.

    Args:
        dms: A tuple of (degrees, minutes, seconds).
        ref: Hemisphere reference ('N', 'S', 'E', or 'W').

    Returns:
        Signed decimal degree as a float.
    """
    degrees, minutes, seconds = dms
    decimal = degrees + minutes / 60 + seconds / 3600
    if ref in ("S", "W"):
        decimal = -decimal
    return decimal
