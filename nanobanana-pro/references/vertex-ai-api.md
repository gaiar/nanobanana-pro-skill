# Vertex AI Image Generation — API Reference

## Model

- **Default**: `gemini-3-pro-image-preview` (highest quality, auto-uses `global` location)
- **Fallback**: `gemini-2.5-flash-image` (fast, reliable)
- **API**: `generateContent` (via `google-genai` SDK, not the Imagen `predict` API)
- **Auth**: Application Default Credentials (ADC) via `gcloud auth application-default login`

## SDK Usage

```python
from google import genai
from google.genai import types

client = genai.Client(vertexai=True, project="PROJECT_ID", location="us-central1")

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents="A red apple on white background",
    config=types.GenerateContentConfig(
        response_modalities=["IMAGE", "TEXT"],
        image_config=types.ImageConfig(
            aspect_ratio="1:1",
            image_size="2K",
        ),
    ),
)

for part in response.parts:
    if part.inline_data is not None:
        image = part.as_image()
        image.save("output.png")
    elif part.text is not None:
        print(part.text)
```

## Image Editing (Multimodal Input)

Pass one or more PIL Image objects alongside a text prompt to edit existing images. The SDK serializes PIL objects automatically.

### SDK Usage

```python
from PIL import Image

# Load a reference image
ref = Image.open("photo.png")

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=[ref, "Remove the background and make it transparent"],
    config=types.GenerateContentConfig(
        response_modalities=["IMAGE", "TEXT"],
        image_config=types.ImageConfig(
            aspect_ratio="1:1",
            image_size="2K",
        ),
    ),
)
```

Multiple images can be passed for tasks like style transfer:

```python
style = Image.open("painting.jpg")
content = Image.open("photo.png")

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=[style, content, "Apply the style of the first image to the second"],
    config=config,
)
```

### CLI Usage

```bash
# Edit a local image
uv run python -m nanobanana_pro.generate "Remove the background" \
  --image ~/Pictures/photo.png

# Edit an image from a URL
uv run python -m nanobanana_pro.generate "Make it look like a painting" \
  --image https://example.com/photo.jpg

# Multiple input images
uv run python -m nanobanana_pro.generate "Combine these" \
  --image ~/Pictures/a.png --image ~/Pictures/b.png
```

## Aspect Ratios

| Ratio | Use Case |
|-------|----------|
| 1:1 | Square — social media profile, product shots |
| 2:3 | Portrait — phone wallpaper, Pinterest |
| 3:2 | Landscape — photo print, blog header |
| 3:4 | Portrait — Instagram portrait |
| 4:3 | Landscape — presentations, thumbnails |
| 4:5 | Portrait — Instagram feed |
| 5:4 | Landscape — large print |
| 9:16 | Tall portrait — stories, reels, TikTok |
| 16:9 | Widescreen — YouTube thumbnail, desktop wallpaper |
| 21:9 | Ultra-wide — cinematic banner |

## Image Sizes (Resolution)

| Size | Approximate Resolution | Use Case |
|------|----------------------|----------|
| 1K | ~1024px on long edge | Quick previews, drafts |
| 2K | ~2048px on long edge | General use, social media |
| 4K | ~4096px on long edge | Print, high-resolution display |

## Rate Limits

- **Requests per minute**: Varies by project quota (default ~10 RPM for preview models)
- **Tokens per minute**: Shared with text generation quota
- **Image generation**: May take 10-30 seconds per request
- **Preview model caveat**: Rate limits and availability may change

## Response Structure

The response contains a list of `parts`, each of which may be:
- **Image part**: `part.inline_data` is not None; use `part.as_image()` to get a PIL Image
- **Text part**: `part.text` contains model commentary or refusal reasons

The model may return text instead of (or alongside) an image if:
- The prompt violates safety policies
- The request is ambiguous
- The model adds a caption/description

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| `403 Permission Denied` | Vertex AI API not enabled or wrong project | `gcloud services enable aiplatform.googleapis.com` |
| `401 Unauthorized` | ADC not configured | `gcloud auth application-default login` |
| `429 Resource Exhausted` | Rate limit hit | Wait and retry, or request quota increase |
| `400 Bad Request` | Invalid aspect ratio or image size | Check valid values above |
| Empty response (no image) | Safety filter triggered | Revise prompt to avoid policy violations |

## CLI Tool

```bash
# Basic usage
uv run python -m nanobanana_pro.generate "A red apple on white background"

# With options
uv run python -m nanobanana_pro.generate "Cinematic sunset" \
  --aspect-ratio 16:9 --image-size 4K

# From file (used by the skill workflow)
uv run python -m nanobanana_pro.generate --prompt-file /tmp/nanoprompt.txt

# From stdin
echo "A mountain landscape" | uv run python -m nanobanana_pro.generate

# Without auto-opening the image
uv run python -m nanobanana_pro.generate "test" --no-open
```

Output directory: `~/Pictures/nanobanana-pro/`
Filename format: `YYYYMMDD_HHMMSS_slug-from-prompt.png`
