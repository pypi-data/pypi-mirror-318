# src/videoutil/cli.py
import click
from pathlib import Path
from . import generate as generate_module
from . import rename as rename_module
from . import combine as combine_module

@click.group()
def main():
    """Video utility tools for combining and managing video files."""
    pass

@main.command()
def rename():
    """Rename video pairs in a directory."""
    rename_module.rename_videos()

@main.command()
def generate():
    """Generate test video pairs."""
    generate_module.generate_videos()

@main.command()
def combine():
    """Combine video pairs in a directory."""
    combine_module.combine_videos()

if __name__ == '__main__':
    main()