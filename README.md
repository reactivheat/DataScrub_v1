# Metadata Scrubber

Offline CLI tool that inspects and strips hidden metadata — GPS location,
device info, author names, timestamps — from images, PDFs, and Office
documents. No API calls, no telemetry, everything runs locally.

> Status: 🚧 early scaffolding — architecture is in place, core logic is
> being built out. See [Roadmap](#roadmap) below.

## Why

Files carry more information than most people realize. A photo shared
online can leak the exact GPS coordinates of where it was taken. A PDF or
Word doc can leak your real name, your employer, or your device — even
after you've "anonymized" the visible content.

## Usage (planned interface)

```bash
# Read-only: see what metadata is hiding in a file or folder
metascrub scan photo.jpg
metascrub scan ./my_folder --recursive

# See a map of where a GPS-tagged photo was taken, before you scrub it
metascrub scan photo.jpg --visualize

# Strip metadata, write cleaned copies to ./cleaned/ (originals untouched)
metascrub clean photo.jpg
metascrub clean ./my_folder --recursive --output ./safe_to_share
```

## Supported formats

| Format | Read | Scrub |
|---|---|---|
| JPG / PNG (EXIF, GPS) | v0.1 | v0.1 |
| PDF | v0.1 | v0.1 |
| DOCX / XLSX | v0.2 | v0.2 |
| HEIC | v0.2 | v0.2 |

## Project structure

```
src/metascrub/
├── cli.py           # Click CLI entrypoint
├── core/             # scanning + report generation
├── readers/           # per-filetype metadata extraction
├── scrubbers/          # per-filetype metadata stripping
├── utils/              # shared helpers (GPS conversion, file type detection)
└── visualize/           # GPS map preview (folium)
```

## Install (dev mode)

```bash
git clone https://github.com/reactivheat/metadata-scrubber.git
cd metadata-scrubber
pip install -e ".[dev]"
```

## Roadmap

- **v0.1** — image (JPG/PNG) + PDF support, CLI scan/clean, text report
- **v0.2** — Office docs (DOCX/XLSX), batch folder scan, HEIC support
- **v0.3** — GPS map preview (`--visualize`), HTML report export

## Contributing

Not open for external contributions yet — building the core solo first.
Will open up once v0.1 is stable. Feel free to star/watch for updates.

## License

MIT
