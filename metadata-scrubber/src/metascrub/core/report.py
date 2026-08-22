"""
Report generation.

Responsibilities:
- Take raw metadata dicts (from readers/*) and turn them into a human-readable
  summary — this is the "oh shit, my photo has my house's GPS location" moment,
  so wording matters more than in a typical dev tool.
- Support at least two output modes:
    - CLI table (rich or plain print) for `metascrub scan`
    - Optional JSON/HTML export for `--export report.html` (future flag)
- Aggregate stats across a batch run: "X of Y files contained sensitive metadata"

Suggested shape for a per-file result (adjust as needed once readers exist):

    {
        "file": "IMG_0001.jpg",
        "type": "image",
        "findings": {
            "gps": {"lat": -6.xxxx, "lon": 106.xxxx},
            "device": "iPhone 13 Pro",
            "software": "iOS 17.4",
            "timestamp": "2026-03-01T10:22:00",
        },
        "risk_level": "high",  # e.g. high if GPS present, medium if device/author, low if none
    }
"""


def build_report(results: list[dict]) -> str:
    """Turn a list of per-file finding dicts into a printable CLI report."""
    # TODO: group by risk_level, print sensitive fields clearly
    raise NotImplementedError


def summarize_batch(results: list[dict]) -> dict:
    """Return aggregate stats: total files, files with GPS, files with author info, etc."""
    # TODO
    raise NotImplementedError
