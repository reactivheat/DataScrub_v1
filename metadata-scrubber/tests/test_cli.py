"""
Tests for cli.py.

Use Click's CliRunner to invoke commands without spawning a real subprocess.

Example:

    from click.testing import CliRunner
    from metascrub.cli import main

    def test_scan_command_runs():
        runner = CliRunner()
        result = runner.invoke(main, ["scan", "tests/fixtures/sample_with_gps.jpg"])
        assert result.exit_code == 0
        assert "GPS" in result.output
"""
