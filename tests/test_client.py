"""Tests for nanobanana_pro.client."""

from __future__ import annotations

import os
from unittest.mock import MagicMock, patch

import pytest

from nanobanana_pro.client import (
    VALID_ASPECT_RATIOS,
    VALID_IMAGE_SIZES,
    _resolve_project,
    create_client,
    generate_image,
)


class TestResolveProject:
    def test_from_env_var(self) -> None:
        with patch.dict(os.environ, {"GOOGLE_CLOUD_PROJECT": "my-project"}):
            assert _resolve_project() == "my-project"

    @patch.dict(os.environ, {}, clear=True)
    @patch("subprocess.run")
    def test_from_gcloud(self, mock_run: MagicMock) -> None:
        mock_run.return_value = MagicMock(stdout="gcloud-project\n", returncode=0)
        # Remove GOOGLE_CLOUD_PROJECT if present
        os.environ.pop("GOOGLE_CLOUD_PROJECT", None)
        assert _resolve_project() == "gcloud-project"

    @patch.dict(os.environ, {}, clear=True)
    @patch("subprocess.run")
    def test_gcloud_unset(self, mock_run: MagicMock) -> None:
        mock_run.return_value = MagicMock(stdout="(unset)\n", returncode=0)
        os.environ.pop("GOOGLE_CLOUD_PROJECT", None)
        with pytest.raises(RuntimeError, match="Cannot resolve GCP project"):
            _resolve_project()

    @patch.dict(os.environ, {}, clear=True)
    @patch("subprocess.run", side_effect=FileNotFoundError)
    def test_gcloud_not_installed(self, mock_run: MagicMock) -> None:
        os.environ.pop("GOOGLE_CLOUD_PROJECT", None)
        with pytest.raises(RuntimeError, match="Cannot resolve GCP project"):
            _resolve_project()


class TestCreateClient:
    @patch("nanobanana_pro.client.genai.Client")
    def test_with_explicit_project(self, mock_client_cls: MagicMock) -> None:
        create_client(project="explicit-project")
        mock_client_cls.assert_called_once_with(
            vertexai=True,
            project="explicit-project",
            location="us-central1",
        )

    @patch("nanobanana_pro.client.genai.Client")
    @patch("nanobanana_pro.client._resolve_project", return_value="resolved-project")
    def test_resolves_project(
        self, mock_resolve: MagicMock, mock_client_cls: MagicMock
    ) -> None:
        create_client()
        mock_client_cls.assert_called_once_with(
            vertexai=True,
            project="resolved-project",
            location="us-central1",
        )


class TestGenerateImage:
    def test_invalid_aspect_ratio(self) -> None:
        client = MagicMock()
        with pytest.raises(ValueError, match="Invalid aspect_ratio"):
            generate_image(client, "test", aspect_ratio="7:3")

    def test_invalid_image_size(self) -> None:
        client = MagicMock()
        with pytest.raises(ValueError, match="Invalid image_size"):
            generate_image(client, "test", image_size="8K")

    def test_calls_generate_content(self) -> None:
        client = MagicMock()
        generate_image(client, "A red apple", aspect_ratio="1:1", image_size="1K")
        client.models.generate_content.assert_called_once()
        call_kwargs = client.models.generate_content.call_args
        assert call_kwargs.kwargs["model"] == "gemini-3-pro-image-preview"
        assert call_kwargs.kwargs["contents"] == "A red apple"

    def test_valid_aspect_ratios(self) -> None:
        expected = [
            "1:1",
            "2:3",
            "3:2",
            "3:4",
            "4:3",
            "4:5",
            "5:4",
            "9:16",
            "16:9",
            "21:9",
        ]
        assert VALID_ASPECT_RATIOS == expected

    def test_valid_image_sizes(self) -> None:
        assert VALID_IMAGE_SIZES == ["1K", "2K", "4K"]
