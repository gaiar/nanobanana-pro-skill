"""Load images from local files or URLs for editing workflows."""

from __future__ import annotations

import urllib.request
from io import BytesIO
from pathlib import Path

from PIL import Image

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}

_URL_TIMEOUT = 30


def _is_url(source: str) -> bool:
    """Check whether *source* looks like an HTTP(S) URL."""
    return source.startswith("http://") or source.startswith("https://")


def _load_from_file(path: str) -> Image.Image:
    """Open an image from a local file path.

    Raise ``FileNotFoundError`` for missing paths and ``ValueError`` for
    unsupported extensions or directories.
    """
    p = Path(path).expanduser().resolve()
    if not p.exists():
        raise FileNotFoundError(f"Image file not found: {path}")
    if p.is_dir():
        raise ValueError(f"Path is a directory, not a file: {path}")
    if p.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported image format '{p.suffix}'. "
            f"Supported: {', '.join(sorted(SUPPORTED_EXTENSIONS))}"
        )
    return Image.open(p).copy()


def _load_from_url(url: str) -> Image.Image:
    """Download an image from *url* and return a PIL Image."""
    try:
        with urllib.request.urlopen(url, timeout=_URL_TIMEOUT) as resp:  # noqa: S310
            data = resp.read()
    except Exception as exc:
        raise RuntimeError(f"Failed to download image from {url}: {exc}") from exc

    try:
        return Image.open(BytesIO(data)).copy()
    except Exception as exc:
        raise ValueError(
            f"Downloaded data from {url} is not a valid image: {exc}"
        ) from exc


def load_image(source: str) -> Image.Image:
    """Load a single image from a local path or URL."""
    if _is_url(source):
        return _load_from_url(source)
    return _load_from_file(source)


def load_images(sources: list[str]) -> list[Image.Image]:
    """Load multiple images. Fail fast on the first error."""
    return [load_image(s) for s in sources]
