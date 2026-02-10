"""Utility functions for file naming, sanitization, and macOS integration."""

from __future__ import annotations

import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

OUTPUT_DIR = Path.home() / "Pictures" / "nanobanana-pro"

MAX_SLUG_LENGTH = 60


def sanitize_slug(text: str) -> str:
    """Convert text to a filesystem-safe slug.

    Lowercase, replace non-alphanumeric with hyphens, collapse runs, trim.
    """
    slug = text.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    if len(slug) > MAX_SLUG_LENGTH:
        slug = slug[:MAX_SLUG_LENGTH].rstrip("-")
    return slug


def generate_filename(prompt: str, extension: str = "png") -> str:
    """Generate a timestamped filename from a prompt.

    Format: 20260210_143022_a-sunset-over-mountains.png
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    slug = sanitize_slug(prompt)
    if not slug:
        slug = "image"
    return f"{timestamp}_{slug}.{extension}"


def ensure_output_dir() -> Path:
    """Create the output directory if it doesn't exist and return its path."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return OUTPUT_DIR


def open_image(path: Path) -> None:
    """Open an image file in macOS Preview.app."""
    if sys.platform != "darwin":
        print(f"Image saved to: {path}")
        return
    subprocess.run(["open", str(path)], check=False)
