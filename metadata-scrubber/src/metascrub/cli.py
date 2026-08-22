"""
Command-line entrypoint.

Responsibilities:
- Parse CLI args/flags with Click
- Wire together: scanner -> readers -> report -> (optional) scrubbers
- Handle single-file mode and batch/folder mode

Planned commands:
    metascrub scan <path> [--recursive]
        -> read-only: extract & report metadata found, no files modified

    metascrub clean <path> [--output <dir>] [--recursive] [--dry-run]
        -> scrub metadata, write cleaned copies (never overwrite originals)

    metascrub scan <path> --visualize
        -> if GPS EXIF found in images, render a map preview (see visualize/map_preview.py)

Design notes:
- Keep this file thin. It should only handle argument parsing + orchestration.
- All real logic belongs in core/, readers/, scrubbers/, utils/.
- Exit codes: 0 = clean run, 1 = error, 2 = found sensitive metadata (useful for CI/scripting)
"""

import click


@click.group()
@click.version_option()
def main():
    """Offline metadata privacy scrubber — inspect and strip hidden metadata from files."""
    pass


@main.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--recursive", "-r", is_flag=True, help="Recurse into subfolders.")
@click.option("--visualize", is_flag=True, help="Render a map preview if GPS data is found.")
def scan(path, recursive, visualize):
    """Read-only scan: report what metadata is hiding in PATH (file or folder)."""
    # TODO: call core.scanner.discover_files(path, recursive)
    # TODO: for each file, pick the right reader via utils.file_types
    # TODO: pass results to core.report.build_report()
    raise NotImplementedError


@main.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--output", "-o", type=click.Path(), default="./cleaned", help="Output directory for cleaned files.")
@click.option("--recursive", "-r", is_flag=True, help="Recurse into subfolders.")
@click.option("--dry-run", is_flag=True, help="Show what would be scrubbed without writing files.")
def clean(path, output, recursive, dry_run):
    """Strip metadata from PATH (file or folder), writing cleaned copies to --output."""
    # TODO: never modify the original file in place
    # TODO: call core.scanner.discover_files -> scrubbers.* -> core.report
    raise NotImplementedError


if __name__ == "__main__":
    main()
