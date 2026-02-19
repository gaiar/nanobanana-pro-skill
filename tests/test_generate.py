"""Tests for nanobanana_pro.generate."""

from __future__ import annotations

import argparse
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from PIL import Image

from nanobanana_pro.generate import _read_prompt, build_parser, main


class TestBuildParser:
    def test_defaults(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["test prompt"])
        assert args.prompt == "test prompt"
        assert args.aspect_ratio == "1:1"
        assert args.image_size == "2K"
        assert args.model == "gemini-3-pro-image-preview"
        assert args.no_open is False
        assert args.project is None
        assert args.images is None

    def test_all_flags(self) -> None:
        parser = build_parser()
        args = parser.parse_args(
            [
                "my prompt",
                "--aspect-ratio",
                "16:9",
                "--image-size",
                "4K",
                "--model",
                "custom-model",
                "--project",
                "my-project",
                "--no-open",
            ]
        )
        assert args.prompt == "my prompt"
        assert args.aspect_ratio == "16:9"
        assert args.image_size == "4K"
        assert args.model == "custom-model"
        assert args.project == "my-project"
        assert args.no_open is True

    def test_prompt_file(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--prompt-file", "/tmp/prompt.txt"])
        assert args.prompt_file == "/tmp/prompt.txt"
        assert args.prompt is None

    def test_single_image_flag(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["prompt", "--image", "/tmp/photo.png"])
        assert args.images == ["/tmp/photo.png"]

    def test_multiple_image_flags(self) -> None:
        parser = build_parser()
        args = parser.parse_args(
            [
                "prompt",
                "--image",
                "/tmp/a.png",
                "--image",
                "https://example.com/b.jpg",
            ]
        )
        assert args.images == ["/tmp/a.png", "https://example.com/b.jpg"]

    def test_no_image_flag(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["prompt"])
        assert args.images is None


class TestReadPrompt:
    def test_from_argument(self) -> None:
        args = argparse.Namespace(prompt="hello world", prompt_file=None)
        assert _read_prompt(args) == "hello world"

    def test_from_file(self, tmp_path: Path) -> None:
        prompt_file = tmp_path / "prompt.txt"
        prompt_file.write_text("file prompt content")
        args = argparse.Namespace(prompt=None, prompt_file=str(prompt_file))
        assert _read_prompt(args) == "file prompt content"

    def test_missing_file(self, tmp_path: Path) -> None:
        args = argparse.Namespace(
            prompt=None, prompt_file=str(tmp_path / "missing.txt")
        )
        with pytest.raises(SystemExit):
            _read_prompt(args)

    def test_no_input_tty(self) -> None:
        args = argparse.Namespace(prompt=None, prompt_file=None)
        with patch("sys.stdin") as mock_stdin:
            mock_stdin.isatty.return_value = True
            with pytest.raises(SystemExit):
                _read_prompt(args)


class TestMain:
    @patch("nanobanana_pro.generate.open_image")
    @patch("nanobanana_pro.generate.ensure_output_dir")
    @patch("nanobanana_pro.generate.generate_image")
    @patch("nanobanana_pro.generate.create_client")
    def test_successful_generation(
        self,
        mock_create: MagicMock,
        mock_generate: MagicMock,
        mock_output_dir: MagicMock,
        mock_open: MagicMock,
        tmp_path: Path,
    ) -> None:
        mock_output_dir.return_value = tmp_path

        # Mock response with image part
        mock_image = MagicMock()
        mock_part = MagicMock()
        mock_part.inline_data = b"fake_image_data"
        mock_part.as_image.return_value = mock_image
        mock_part.text = None
        mock_response = MagicMock()
        mock_response.parts = [mock_part]
        mock_generate.return_value = mock_response

        main(["A red apple", "--no-open"])

        mock_create.assert_called_once()
        mock_generate.assert_called_once()
        mock_image.save.assert_called_once()

    @patch("nanobanana_pro.generate.ensure_output_dir")
    @patch("nanobanana_pro.generate.generate_image")
    @patch("nanobanana_pro.generate.create_client")
    def test_no_image_returned(
        self,
        mock_create: MagicMock,
        mock_generate: MagicMock,
        mock_output_dir: MagicMock,
        tmp_path: Path,
    ) -> None:
        mock_output_dir.return_value = tmp_path

        # Mock response with text only, no image
        mock_part = MagicMock()
        mock_part.inline_data = None
        mock_part.text = "I cannot generate that image."
        mock_response = MagicMock()
        mock_response.parts = [mock_part]
        mock_generate.return_value = mock_response

        with pytest.raises(SystemExit):
            main(["A red apple", "--no-open"])

    @patch("nanobanana_pro.generate.open_image")
    @patch("nanobanana_pro.generate.ensure_output_dir")
    @patch("nanobanana_pro.generate.generate_image")
    @patch("nanobanana_pro.generate.create_client")
    @patch("nanobanana_pro.generate.load_images")
    def test_image_editing(
        self,
        mock_load_images: MagicMock,
        mock_create: MagicMock,
        mock_generate: MagicMock,
        mock_output_dir: MagicMock,
        mock_open: MagicMock,
        tmp_path: Path,
    ) -> None:
        mock_output_dir.return_value = tmp_path
        img = Image.new("RGB", (4, 4))
        mock_load_images.return_value = [img]

        mock_image = MagicMock()
        mock_part = MagicMock()
        mock_part.inline_data = b"fake"
        mock_part.as_image.return_value = mock_image
        mock_part.text = None
        mock_response = MagicMock()
        mock_response.parts = [mock_part]
        mock_generate.return_value = mock_response

        main(["Remove bg", "--image", "/tmp/photo.png", "--no-open"])

        mock_load_images.assert_called_once_with(["/tmp/photo.png"])
        mock_generate.assert_called_once()
        call_kwargs = mock_generate.call_args.kwargs
        assert call_kwargs["images"] == [img]

    @patch("nanobanana_pro.generate.load_images")
    def test_image_load_error_exits(self, mock_load: MagicMock) -> None:
        mock_load.side_effect = FileNotFoundError("not found")
        with pytest.raises(SystemExit):
            main(["Edit", "--image", "/missing.png", "--no-open"])

    def test_empty_prompt(self) -> None:
        with patch("sys.stdin") as mock_stdin:
            mock_stdin.isatty.return_value = True
            with pytest.raises(SystemExit):
                main([])
