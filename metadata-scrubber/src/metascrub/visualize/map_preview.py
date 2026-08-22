"""
GPS map preview — this is the demo feature: show the user WHERE their photo
was taken before it gets scrubbed, so the risk actually lands emotionally
instead of just being an abstract lat/lon number in a report.

Library: folium (generates a self-contained HTML file with an embedded map,
works offline once tile images are cached — for a fully offline demo,
consider bundling a static map image fallback instead of live tiles).

Usage sketch:
    metascrub scan photo.jpg --visualize
    -> if GPS found, render map_<filename>.html and open it / print the path
"""

from pathlib import Path


def render_gps_preview(lat: float, lon: float, label: str, output_path: Path) -> Path:
    """
    Generate an HTML map centered on (lat, lon) with a marker, save to output_path.

    TODO:
    import folium
    m = folium.Map(location=[lat, lon], zoom_start=15)
    folium.Marker([lat, lon], popup=label).add_to(m)
    m.save(str(output_path))
    return output_path
    """
    raise NotImplementedError
