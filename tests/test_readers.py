"""
Tests for readers/*.

Plan:
- Put small sample files (with known, fake metadata you inject yourself)
  in tests/fixtures/ — e.g. a JPG with a fake GPS tag you set with piexif,
  a PDF with a fake /Author set with pypdf.
- Never use real personal photos/documents as fixtures.
- Assert that reader.read(fixture) returns the exact fake values you injected.

Example (once ImageReader is implemented):

    def test_image_reader_extracts_gps():
        reader = ImageReader()
        result = reader.read(Path("tests/fixtures/sample_with_gps.jpg"))
        assert result["findings"]["gps"]["lat"] == pytest.approx(-6.2, abs=0.01)
"""
