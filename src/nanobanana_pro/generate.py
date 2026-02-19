"""CLI entry point: prompt -> Vertex AI -> saved image."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from nanobanana_pro.client import (
    DEFAULT_MODEL,
    VALID_ASPECT_RATIOS,
    VALID_IMAGE_SIZES,
    create_client,
    generate_image,
    location_for_model,
)
from nanobanana_pro.image_input import load_images
from nanobanana_pro.utils import (
    ensure_output_dir,
    generate_filename,
    open_image,
)


def _read_prompt(args: argparse.Namespace) -> str:
    """Read prompt from args, file, or stdin."""
    if args.prompt:
        return str(args.prompt)

    if args.prompt_file:
        path = Path(args.prompt_file)
        if not path.exists():
            print(f"Error: prompt file not found: {path}", file=sys.stderr)
            sys.exit(1)
        return path.read_text().strip()

    if not sys.stdin.isatty():
        return sys.stdin.read().strip()

    print(
        "Error: provide a prompt via argument, --prompt-file, or stdin.",
        file=sys.stderr,
    )
    sys.exit(1)


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser."""
    parser = argparse.ArgumentParser(
        prog="nanobanana-pro",
        description="Generate images via Vertex AI (Gemini 3 Pro Image)",
    )
    parser.add_argument(
        "prompt",
        nargs="?",
        default=None,
        help="Text prompt for image generation",
    )
    parser.add_argument(
        "--prompt-file",
        type=str,
        default=None,
        help="Path to a file containing the prompt",
    )
    parser.add_argument(
        "--aspect-ratio",
        type=str,
        default="1:1",
        choices=VALID_ASPECT_RATIOS,
        help="Image aspect ratio (default: 1:1)",
    )
    parser.add_argument(
        "--image-size",
        type=str,
        default="2K",
        choices=VALID_IMAGE_SIZES,
        help="Image resolution (default: 2K)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=DEFAULT_MODEL,
        help=f"Model name (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--project",
        type=str,
        default=None,
        help="GCP project ID (default: from env or gcloud config)",
    )
    parser.add_argument(
        "--image",
        action="append",
        dest="images",
        default=None,
        help="Input image (local path or URL) for editing. Repeatable.",
    )
    parser.add_argument(
        "--no-open",
        action="store_true",
        help="Don't open the image in Preview.app after saving",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    """Run the image generation pipeline."""
    parser = build_parser()
    args = parser.parse_args(argv)

    prompt = _read_prompt(args)
    if not prompt:
        print("Error: prompt is empty.", file=sys.stderr)
        sys.exit(1)

    # Load input images when provided (for editing workflows)
    loaded_images = None
    if args.images:
        try:
            loaded_images = load_images(args.images)
        except (FileNotFoundError, ValueError, RuntimeError) as exc:
            print(f"Error loading image: {exc}", file=sys.stderr)
            sys.exit(1)
        print(f"Editing image with prompt: {prompt[:80]}...")
    else:
        print(f"Generating image for: {prompt[:80]}...")

    location = location_for_model(args.model)
    client = create_client(project=args.project, location=location)
    response = generate_image(
        client=client,
        prompt=prompt,
        model=args.model,
        aspect_ratio=args.aspect_ratio,
        image_size=args.image_size,
        images=loaded_images,
    )

    image_saved = False
    output_dir = ensure_output_dir()
    saved_path: Path | None = None

    if not response.parts:
        print("Error: empty response from model.", file=sys.stderr)
        sys.exit(1)

    for part in response.parts:
        if part.inline_data is not None:
            image = part.as_image()
            if image is None:
                continue
            filename = generate_filename(prompt)
            saved_path = output_dir / filename
            image.save(str(saved_path))
            print(f"Image saved: {saved_path}")
            image_saved = True
            break
        elif part.text is not None:
            print(f"Model response: {part.text}")

    if not image_saved:
        print("Error: no image was returned by the model.", file=sys.stderr)
        sys.exit(1)

    if saved_path and not args.no_open:
        open_image(saved_path)


if __name__ == "__main__":
    main()
