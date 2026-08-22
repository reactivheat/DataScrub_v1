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
        dms: A tuple of (degrees, minutes, seconds) as floats or ints.
        ref: Hemisphere reference string ('N', 'S', 'E', or 'W').

    Returns:
        A signed decimal degree float. Negative for 'S' and 'W' hemispheres.
    """
    degrees, minutes, seconds = dms
    decimal = degrees + minutes / 60 + seconds / 3600
    if ref in ("S", "W"):
        decimal = -decimal
    return decimal
