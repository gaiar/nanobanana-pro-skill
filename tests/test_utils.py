"""Tests for nanobanana_pro.utils."""

from __future__ import annotations

import re
from pathlib import Path
from unittest.mock import patch

from nanobanana_pro.utils import (
    OUTPUT_DIR,
    ensure_output_dir,
    generate_filename,
    open_image,
    sanitize_slug,
)


class TestSanitizeSlug:
    def test_basic(self) -> None:
        assert sanitize_slug("Hello World") == "hello-world"

    def test_special_characters(self) -> None:
        assert sanitize_slug("A sunset over mountains!") == "a-sunset-over-mountains"

    def test_collapses_hyphens(self) -> None:
        assert sanitize_slug("hello   ---   world") == "hello-world"

    def test_strips_leading_trailing(self) -> None:
        assert sanitize_slug("  --hello-- ") == "hello"

    def test_empty_string(self) -> None:
        assert sanitize_slug("") == ""

    def test_all_special_chars(self) -> None:
        assert sanitize_slug("!@#$%") == ""

    def test_truncation(self) -> None:
        long_text = "a" * 100
        result = sanitize_slug(long_text)
        assert len(result) <= 60

    def test_truncation_no_trailing_hyphen(self) -> None:
        text = "hello " * 20
        result = sanitize_slug(text)
        assert not result.endswith("-")
        assert len(result) <= 60


class TestGenerateFilename:
    def test_format(self) -> None:
        filename = generate_filename("A red apple")
        pattern = r"^\d{8}_\d{6}_a-red-apple\.png$"
        assert re.match(pattern, filename), f"'{filename}' doesn't match pattern"

    def test_custom_extension(self) -> None:
        filename = generate_filename("test", extension="jpg")
        assert filename.endswith(".jpg")

    def test_empty_prompt_fallback(self) -> None:
        filename = generate_filename("!@#$%")
        assert "image" in filename

    def test_contains_timestamp(self) -> None:
        filename = generate_filename("test")
        parts = filename.split("_")
        assert len(parts[0]) == 8  # date
        assert len(parts[1]) == 6  # time


class TestEnsureOutputDir:
    def test_creates_dir(self, tmp_path: Path) -> None:
        test_dir = tmp_path / "nanobanana-pro"
        with patch("nanobanana_pro.utils.OUTPUT_DIR", test_dir):
            result = ensure_output_dir()
            assert result == test_dir
            assert test_dir.exists()

    def test_existing_dir(self, tmp_path: Path) -> None:
        test_dir = tmp_path / "nanobanana-pro"
        test_dir.mkdir()
        with patch("nanobanana_pro.utils.OUTPUT_DIR", test_dir):
            result = ensure_output_dir()
            assert result == test_dir


class TestOpenImage:
    @patch("subprocess.run")
    def test_opens_on_darwin(self, mock_run: object) -> None:
        with patch("nanobanana_pro.utils.sys") as mock_sys:
            mock_sys.platform = "darwin"
            open_image(Path("/tmp/test.png"))

            assert mock_run.called  # type: ignore[union-attr]

    @patch("subprocess.run")
    @patch("builtins.print")
    def test_prints_on_linux(self, mock_print: object, mock_run: object) -> None:
        with patch("nanobanana_pro.utils.sys") as mock_sys:
            mock_sys.platform = "linux"
            open_image(Path("/tmp/test.png"))
            assert not mock_run.called  # type: ignore[union-attr]
            assert mock_print.called  # type: ignore[union-attr]


class TestOutputDir:
    def test_is_in_pictures(self) -> None:
        assert OUTPUT_DIR == Path.home() / "Pictures" / "nanobanana-pro"
