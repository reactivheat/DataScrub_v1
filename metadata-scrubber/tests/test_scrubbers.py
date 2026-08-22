"""
Tests for scrubbers/*.

Plan:
- Round-trip test: read fixture -> scrub -> read the scrubbed output ->
  assert findings dict is now empty/None for the fields that matter.
- Assert original fixture file is untouched (hash before == hash after run).

Example (once ImageScrubber is implemented):

    def test_image_scrubber_removes_gps(tmp_path):
        reader = ImageReader()
        scrubber = ImageScrubber()
        src = Path("tests/fixtures/sample_with_gps.jpg")
        dest = tmp_path / "cleaned.jpg"

        scrubber.scrub(src, dest)
        result = reader.read(dest)

        assert "gps" not in result["findings"]
        assert src.stat().st_mtime == ORIGINAL_MTIME  # original untouched
"""
