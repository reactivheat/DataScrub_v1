# Test fixtures

Small sample files used by the test suite, with **fake, self-injected**
metadata only — never real personal photos or documents.

Suggested fixtures to add as you build:
- `sample_with_gps.jpg` — JPG with a fake GPS EXIF tag set via `piexif`
- `sample_no_metadata.jpg` — clean JPG for negative-case tests
- `sample_with_author.pdf` — PDF with a fake `/Author` set via `pypdf`
- `sample_with_author.docx` — DOCX with fake `core_properties.author`

You can generate these with a small one-off script — don't commit real data.
