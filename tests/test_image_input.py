"""Tests for nanobanana_pro.image_input."""

from __future__ import annotations

from io import BytesIO
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from PIL import Image

from nanobanana_pro.image_input import (
    _is_url,
    _load_from_file,
    _load_from_url,
    load_image,
    load_images,
)

# ---------------------------------------------------------------------------
# _is_url
# ---------------------------------------------------------------------------


class TestIsUrl:
    def test_https(self) -> None:
        assert _is_url("https://example.com/photo.png") is True

    def test_http(self) -> None:
        assert _is_url("http://example.com/photo.png") is True

    def test_local_path(self) -> None:
        assert _is_url("/tmp/photo.png") is False

    def test_relative_path(self) -> None:
        assert _is_url("photo.png") is False

    def test_ftp(self) -> None:
        assert _is_url("ftp://example.com/photo.png") is False


# ---------------------------------------------------------------------------
# _load_from_file
# ---------------------------------------------------------------------------


class TestLoadFromFile:
    def test_valid_png(self, tmp_path: Path) -> None:
        img_path = tmp_path / "test.png"
        Image.new("RGB", (10, 10), color="red").save(str(img_path))
        result = _load_from_file(str(img_path))
        assert isinstance(result, Image.Image)
        assert result.size == (10, 10)

    def test_valid_jpg(self, tmp_path: Path) -> None:
        img_path = tmp_path / "test.jpg"
        Image.new("RGB", (10, 10), color="blue").save(str(img_path))
        result = _load_from_file(str(img_path))
        assert isinstance(result, Image.Image)

    def test_valid_webp(self, tmp_path: Path) -> None:
        img_path = tmp_path / "test.webp"
        Image.new("RGB", (10, 10), color="green").save(str(img_path))
        result = _load_from_file(str(img_path))
        assert isinstance(result, Image.Image)

    def test_missing_file(self) -> None:
        with pytest.raises(FileNotFoundError, match="Image file not found"):
            _load_from_file("/tmp/nonexistent_image_12345.png")

    def test_directory_path(self, tmp_path: Path) -> None:
        with pytest.raises(ValueError, match="Path is a directory"):
            _load_from_file(str(tmp_path))

    def test_unsupported_extension(self, tmp_path: Path) -> None:
        txt_path = tmp_path / "test.bmp"
        txt_path.write_text("not an image")
        with pytest.raises(ValueError, match="Unsupported image format"):
            _load_from_file(str(txt_path))

    def test_tilde_expansion(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        img_path = tmp_path / "test.png"
        Image.new("RGB", (10, 10)).save(str(img_path))
        monkeypatch.setenv("HOME", str(tmp_path))
        result = _load_from_file("~/test.png")
        assert isinstance(result, Image.Image)


# ---------------------------------------------------------------------------
# _load_from_url
# ---------------------------------------------------------------------------


def _make_png_bytes() -> bytes:
    """Create minimal valid PNG bytes."""
    buf = BytesIO()
    Image.new("RGB", (4, 4), color="red").save(buf, format="PNG")
    return buf.getvalue()


class TestLoadFromUrl:
    @patch("nanobanana_pro.image_input.urllib.request.urlopen")
    def test_success(self, mock_urlopen: MagicMock) -> None:
        ctx = MagicMock()
        ctx.__enter__ = MagicMock(return_value=ctx)
        ctx.__exit__ = MagicMock(return_value=False)
        ctx.read.return_value = _make_png_bytes()
        mock_urlopen.return_value = ctx

        result = _load_from_url("https://example.com/photo.png")
        assert isinstance(result, Image.Image)
        mock_urlopen.assert_called_once_with(
            "https://example.com/photo.png", timeout=30
        )

    @patch("nanobanana_pro.image_input.urllib.request.urlopen")
    def test_download_failure(self, mock_urlopen: MagicMock) -> None:
        mock_urlopen.side_effect = OSError("Connection refused")
        with pytest.raises(RuntimeError, match="Failed to download"):
            _load_from_url("https://example.com/broken.png")

    @patch("nanobanana_pro.image_input.urllib.request.urlopen")
    def test_invalid_image_data(self, mock_urlopen: MagicMock) -> None:
        ctx = MagicMock()
        ctx.__enter__ = MagicMock(return_value=ctx)
        ctx.__exit__ = MagicMock(return_value=False)
        ctx.read.return_value = b"not image data"
        mock_urlopen.return_value = ctx

        with pytest.raises(ValueError, match="not a valid image"):
            _load_from_url("https://example.com/bad.png")


# ---------------------------------------------------------------------------
# load_image (dispatch)
# ---------------------------------------------------------------------------


class TestLoadImage:
    @patch("nanobanana_pro.image_input._load_from_url")
    def test_dispatches_to_url(self, mock_url: MagicMock) -> None:
        mock_url.return_value = Image.new("RGB", (4, 4))
        load_image("https://example.com/photo.png")
        mock_url.assert_called_once_with("https://example.com/photo.png")

    @patch("nanobanana_pro.image_input._load_from_file")
    def test_dispatches_to_file(self, mock_file: MagicMock) -> None:
        mock_file.return_value = Image.new("RGB", (4, 4))
        load_image("/tmp/photo.png")
        mock_file.assert_called_once_with("/tmp/photo.png")


# ---------------------------------------------------------------------------
# load_images
# ---------------------------------------------------------------------------


class TestLoadImages:
    @patch("nanobanana_pro.image_input.load_image")
    def test_multiple(self, mock_load: MagicMock) -> None:
        img = Image.new("RGB", (4, 4))
        mock_load.return_value = img
        result = load_images(["/a.png", "https://b.com/c.png"])
        assert len(result) == 2
        assert mock_load.call_count == 2

    @patch("nanobanana_pro.image_input.load_image")
    def test_empty_list(self, mock_load: MagicMock) -> None:
        result = load_images([])
        assert result == []
        mock_load.assert_not_called()

    @patch("nanobanana_pro.image_input.load_image")
    def test_fail_fast(self, mock_load: MagicMock) -> None:
        mock_load.side_effect = FileNotFoundError("nope")
        with pytest.raises(FileNotFoundError):
            load_images(["/missing.png", "/also_missing.png"])
        # Only the first call should have been attempted
        assert mock_load.call_count == 1
