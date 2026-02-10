"""Vertex AI client for Gemini image generation."""

from __future__ import annotations

import os
import subprocess

from google import genai
from google.genai import types

DEFAULT_MODEL = "gemini-3-pro-image-preview"
DEFAULT_LOCATION = "us-central1"

# Preview models that require the 'global' location on Vertex AI
GLOBAL_LOCATION_MODELS = {"gemini-3-pro-image-preview"}

# All available image generation models (Vertex AI)
AVAILABLE_MODELS = [
    "gemini-2.5-flash-image",
    "gemini-3-pro-image-preview",
    "imagen-4.0-generate-001",
    "imagen-4.0-fast-generate-001",
    "imagen-4.0-ultra-generate-001",
]

VALID_ASPECT_RATIOS = [
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

VALID_IMAGE_SIZES = ["1K", "2K", "4K"]


def _resolve_project() -> str:
    """Resolve GCP project from env var or gcloud config."""
    project = os.environ.get("GOOGLE_CLOUD_PROJECT")
    if project:
        return project

    try:
        result = subprocess.run(
            ["gcloud", "config", "get-value", "project"],
            capture_output=True,
            text=True,
            check=True,
        )
        project = result.stdout.strip()
        if project and project != "(unset)":
            return project
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    raise RuntimeError(
        "Cannot resolve GCP project. Set GOOGLE_CLOUD_PROJECT or run 'gcloud init'."
    )


def location_for_model(model: str) -> str:
    """Return the correct Vertex AI location for a given model."""
    if model in GLOBAL_LOCATION_MODELS:
        return "global"
    return DEFAULT_LOCATION


def create_client(
    project: str | None = None,
    location: str = DEFAULT_LOCATION,
) -> genai.Client:
    """Create a Vertex AI GenAI client using Application Default Credentials."""
    resolved_project = project or _resolve_project()
    return genai.Client(
        vertexai=True,
        project=resolved_project,
        location=location,
    )


def generate_image(
    client: genai.Client,
    prompt: str,
    model: str = DEFAULT_MODEL,
    aspect_ratio: str = "1:1",
    image_size: str = "2K",
) -> types.GenerateContentResponse:
    """Generate an image using Gemini's generateContent API.

    Return the full response containing image and optional text parts.
    """
    if aspect_ratio not in VALID_ASPECT_RATIOS:
        raise ValueError(
            f"Invalid aspect_ratio '{aspect_ratio}'. "
            f"Must be one of: {', '.join(VALID_ASPECT_RATIOS)}"
        )
    if image_size not in VALID_IMAGE_SIZES:
        raise ValueError(
            f"Invalid image_size '{image_size}'. "
            f"Must be one of: {', '.join(VALID_IMAGE_SIZES)}"
        )

    config = types.GenerateContentConfig(
        response_modalities=["IMAGE", "TEXT"],
        image_config=types.ImageConfig(
            aspect_ratio=aspect_ratio,
            image_size=image_size,
        ),
    )

    return client.models.generate_content(
        model=model,
        contents=prompt,
        config=config,
    )
