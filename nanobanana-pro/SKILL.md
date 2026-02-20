---
name: nanobanana-pro
description: |
  Expert Prompt Engineer and Image Generator for Nano Banana Pro. Transforms simple concepts into highly detailed, structured prompts and generates images via Google Vertex AI. Use when users want to: (1) Generate AI images end-to-end (concept → prompt → image), (2) Create detailed image prompts from simple concepts, (3) Build structured JSON prompts for photorealistic results, (4) Develop identity-locked prompts preserving facial features, (5) Apply cinematic/film photography aesthetics to AI images.
---

# Nano Banana Pro — Prompt Engineer & Image Generator

Transform simple concepts into detailed, structured prompts optimized for Nano Banana Pro's reasoning engine, then generate images via Vertex AI.

## Setup Verification (run before first use)

Before the prompt workflow, verify the environment is ready. Run these checks silently — only stop and remediate if a check fails. See `references/setup-guide.md` for detailed remediation steps.

### 1. Python environment

```bash
# Check uv is installed
uv --version

# Check project exists and sync dependencies (creates .venv if missing, installs all deps)
cd ~/Developer/nanobanana-pro-skill && uv sync
```

If `uv` is missing: `brew install uv`. If the project directory is missing: inform the user and stop.

### 2. Google Cloud

```bash
# Check gcloud is installed and project is set
gcloud config get-value project
```

If gcloud is missing: `brew install google-cloud-sdk`.
If project is `(unset)`: prompt the user to run `gcloud init` or `gcloud config set project <PROJECT_ID>`.

```bash
# Check Application Default Credentials are configured
gcloud auth application-default print-access-token 2>/dev/null | head -c 20
```

If ADC fails: prompt the user to run `gcloud auth application-default login` (opens browser for OAuth — requires interactive user action, cannot be automated).

Once all checks pass, proceed to the workflow. Skip verification on subsequent runs in the same session.

## Core Formula

Every effective prompt follows this structure:

```
Scene/Environment + Subject + Style + Lighting + Technical Constraints + Negative Prompts
```

## Quick Start: The 6-Component Structure

1. **Subject** - Specific and clear ("young woman with freckles" not "woman")
2. **Action** - What they're doing ("smiling while holding coffee")
3. **Environment** - Setting with depth ("sun-drenched messy living room corner")
4. **Art Style** - Visual approach ("lifestyle editorial photography")
5. **Lighting** - Source, direction, temperature ("warm golden-hour sunlight, side-lit")
6. **Technical Details** - Camera, lens, film stock ("50-85mm portrait lens, Kodak Portra 400")

## Prompt Formats

Two formats available — the user chooses which one during the workflow (step 2).

### Natural Language Format (Quick)

Layered prose covering the 6 components. Fast to read and edit. Works well for most requests.

```
A [subject with specific details], [action/pose], in [environment with atmosphere].
[Lighting description]. Shot on [camera/lens], [film stock aesthetic].
[Color grading]. [Mood/vibe].
```

### JSON-Structured Format (Maximum Control)

Every detail in a machine-readable schema. Produces more consistent, reproducible results but takes longer to build. Choose the schema that fits the subject from `references/prompt-schemas.md`:

| Schema | Best for |
|--------|----------|
| Full Photorealistic | Maximum detail, any subject |
| Lifestyle/Editorial | Candid natural shots |
| Mirror Selfie | Reflective/selfie compositions |
| Art Director | Professional concept-to-prompt |

Fill every field — no placeholders, no `[brackets]`. Convert the user's concept into concrete values for each key.

## Key Techniques

### 1. Semantic Fields (Director's Notes)

Beyond technical parameters, use abstract concepts as "director's notes":

**Mood terms**: `fragile and intimate`, `decadent exhaustion`, `severe elegance`, `quiet anxiety`, `melancholic`

**Narrative terms**: `clandestine meeting`, `ignoring the camera`, `performance anxiety`

**Cultural codes**: `Wong Kar-wai aesthetic`, `Ophelia trope`, `silent wealth`, `voyeuristic`

These words affect results as strongly as technical terms. See `references/semantic-fields.md` for complete vocabulary.

### 2. Identity Locking (Face Preservation)

```
Using the uploaded photo as a strict and non-negotiable reference, preserve 100% of facial identity — exact facial features, proportions, bone structure, skin texture, and natural expression. Do not alter, beautify, idealize, or stylize the face in any way.
```

### 3. Camera Perspective Statements

Define the viewer's position explicitly:
- "We ARE the phone" (selfie perspective)
- "Camera is at eye-level"
- "Shot from slightly below, looking up"

### 4. Fabric & Material Behavior

Describe how materials interact with physics:
- "visible sheen from light, natural folds and tension, accurate drape and gravity"
- "fabric behaves realistically: soft highlights, gentle falloff"

### 5. Cinematic Language

Use real photography terms:
- **Film stocks**: "Kodak Portra 400", "Fujifilm Pro 400H", "Cinestill 800T"
- **Lens specs**: "50-85mm portrait lens", "35mm fixed lens"
- **Color grading**: "warm skin tones, gentle contrast, lifted blacks"

### 6. Negative Prompts

Always include to prevent common issues:
```
altered face, different identity, idealized beauty, flawless skin, plastic or waxy texture, CGI, digital art, illustration, artificial lighting, broken anatomy, distorted hands, harsh shadows, overprocessed skin, cartoon style
```

### 7. Defeating the AI Look

Four principles to break through the uncanny valley and produce images that don't look generated:

1. **Break symmetry** — Off-center framing, awkward crops, tilted angles, facial asymmetry
2. **Real skin, not porcelain** — Visible pores, redness, blemishes, peach fuzz, dark circles
3. **Kill saturation and sheen** — Muted palettes, no HDR glow, matte skin, faded film tones
4. **Add grain and artifacts** — Film grain, chromatic aberration, vignetting, slight focus misses

Apply all four together for maximum effect. See `references/techniques.md` § "Defeating the AI Look" for full directive vocabulary and a ready-to-use prompt fragment.

### 8. Physical Medium Authenticity (Critical)

**The model defaults to clean, polished output regardless of requested style.** You must actively fight this for every image that depicts a physical medium (prints, paintings, film photography, hand-drawn art, etc.).

#### The Principle

Describe the **physical process** that creates imperfections — not just the effects. Causal language ("ink fails to transfer because hand-pressing pressure is uneven") produces far more authentic results than effect language ("add some imperfections").

#### Three Rules

1. **Imperfections FIRST, subject SECOND** — The model weights prompt elements by position and text volume. If authenticity is critical, make it the leading instruction with the most text, not a sub-field buried in a schema. Start the prompt with the medium and its physical characteristics before describing what the image depicts.

2. **Describe the physical process, not just the result** — For every imperfection, explain HOW it arises in the real physical process:
   - Print: "ink fails to transfer in spots due to uneven hand-pressing pressure"
   - Watercolor: "pigment pools at edges where wet paint settles as paper dries"
   - Oil painting: "thick impasto ridges where the palette knife dragged through wet paint"
   - Film photo: "focus slightly missed because the photographer shifted mid-click"

3. **Explicitly negate the clean default** — The model will revert to digital perfection unless told not to. Always include explicit negations: "NOT clean, NOT digital, NOT polished, NOT crisp, NOT perfect."

#### When to Use ALL CAPS Emphasis

Use CAPS for qualities the model consistently underweights:
- Physical imperfections and texture
- Color restrictions (e.g., "ONLY black and pink, NO other colors")
- Qualities that contradict the model's clean default

#### Format Choice for Textured/Physical Media

For images that require heavy physical authenticity (prints, paintings, analog media), **prefer natural language prose over JSON**. JSON's structured format implicitly signals "organized, precise, clean" and the model follows that signal. Natural language with emphasis markers allows you to weight imperfections more heavily.

When the user requests JSON format for physical media, use a **hybrid approach**: place the medium authenticity requirements as a leading natural language block, then follow with the JSON schema for composition details.

See `references/techniques.md` § "Physical Medium Authenticity" for medium-specific imperfection vocabularies and ready-to-use prompt fragments.

## Image Editing

Edit existing images by passing one or more reference images alongside a text prompt. The Gemini model accepts PIL Image objects as multimodal input, so you can apply transformations like "remove the background", "add a hat", or "apply watercolor style".

### CLI Examples

```bash
# Edit a local image
uv run python -m nanobanana_pro.generate "Remove the background" \
  --image ~/Pictures/photo.png --no-open

# Edit an image from a URL
uv run python -m nanobanana_pro.generate "Make it look like a painting" \
  --image https://example.com/photo.jpg --no-open

# Multiple input images (e.g., style transfer)
uv run python -m nanobanana_pro.generate "Combine these into one scene" \
  --image ~/Pictures/a.png --image ~/Pictures/b.png --no-open
```

The `--image` flag is repeatable. Supported formats: `.jpg`, `.jpeg`, `.png`, `.webp`, `.gif`. Both local paths and HTTP(S) URLs are accepted.

## Workflow

1. **Clarify concept** — Ask user for subject, setting, mood, reference style, and whether they have reference images to edit
2. **Choose prompt format** — Ask the user which format they prefer:
   - Use AskUserQuestion with:
     - Question: "Which prompt format do you want?"
     - Header: "Format"
     - Options:
       - "Natural language (Recommended)" — Human-readable prose, faster to produce
       - "JSON structured" — Machine-readable schema with maximum detail, takes longer but more precise
3. **Build the prompt** — Depends on the format chosen:

   **If Natural Language:**
   - Build layers: Subject core → Action → Environment → Lighting → Camera/lens → Color story
   - Add narrative context ("she's been on the balcony for hours")
   - Append negative prompts
   - Verify all 6 components from the Core Formula are present
   - Output: a single block of descriptive prose

   **If JSON Structured:**
   - Read `references/prompt-schemas.md` to select the right schema for this concept
   - Fill every field with concrete values derived from the user's concept — no placeholders, no `[brackets]`
   - Apply semantic fields (mood, narrative, cultural codes) to `vibe`/`narrative` keys
   - Set `cinematography_and_tech` / `photography` values using real camera gear, film stocks, and lighting
   - Add negative prompts as a top-level `"negative_prompts"` string
   - Output: the complete JSON object

4. **Authenticity pass** — Before presenting, review the prompt for physical medium authenticity:
   - Does the concept involve a physical medium (print, painting, film, handmade art)? If yes:
     - Verify imperfections are described with **causal language** (how they arise physically)
     - Verify imperfections have **prominent placement** (leading position, significant text weight)
     - Verify explicit **negation of clean defaults** is present ("NOT clean, NOT digital...")
     - If using JSON format, ensure a natural language authenticity block leads the prompt
   - Does the concept involve photography? If yes:
     - Verify the "Defeating the AI Look" checklist is applied (asymmetry, skin texture, desaturation, grain)
   - For ALL concepts: ensure the prompt describes what the image should NOT look like, not just what it should

5. **Present prompt** — Show the final prompt to the user, then ask what to do next:
   - Use AskUserQuestion with:
     - Question: "What would you like to do with this prompt?"
     - Header: "Action"
     - Options:
       - "Generate image (Recommended)" — Run Vertex AI generation
       - "Copy to clipboard" — Copy prompt text via pbcopy
       - "Edit first" — Let user revise before generating
6. **Generate image** — If user chose "Generate image":
   a. Ask for generation options using AskUserQuestion:
      - Question: "Which aspect ratio?"
      - Header: "Ratio"
      - Options: "1:1 (square)", "4:3 (landscape)", "3:4 (portrait)", "16:9 (widescreen)"
   b. Write prompt to temp file and run:
      ```bash
      cd ~/Developer/nanobanana-pro-skill && \
      uv run python -m nanobanana_pro.generate --prompt-file /tmp/nanoprompt.txt \
        --aspect-ratio "<chosen_ratio>" --image-size "2K"
      ```
      If the user provided reference images in step 1, append `--image <path_or_url>` for each:
      ```bash
      cd ~/Developer/nanobanana-pro-skill && \
      uv run python -m nanobanana_pro.generate --prompt-file /tmp/nanoprompt.txt \
        --aspect-ratio "<chosen_ratio>" --image-size "2K" \
        --image "/path/to/reference.png"
      ```
   c. Report the saved file path and confirm image opened in Preview.app
7. **Copy to clipboard** — If user chose "Copy to clipboard":
   - Copy the exact prompt text to clipboard via `echo '...' | pbcopy`
   - Confirm it was copied

## Generation Options

| Option | Values | Default | Notes |
|--------|--------|---------|-------|
| Aspect ratio | 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9 | 1:1 | Match to intended platform |
| Image size | 1K, 2K, 4K | 2K | Higher = slower but sharper |
| Model | See model list below | gemini-3-pro-image-preview | Override with --model flag |

### Available Models

| Model | Type | Notes |
|-------|------|-------|
| `gemini-3-pro-image-preview` | Gemini (preview) | **Default.** Highest quality. Auto-uses `global` location |
| `gemini-2.5-flash-image` | Gemini (stable) | Fast, reliable fallback |
| `imagen-4.0-generate-001` | Imagen 4 | Via Imagen API |
| `imagen-4.0-fast-generate-001` | Imagen 4 Fast | Lower latency |
| `imagen-4.0-ultra-generate-001` | Imagen 4 Ultra | Highest quality Imagen |

See `references/vertex-ai-api.md` for full API details, rate limits, and error handling.

## Reference Files

- **Setup guide**: See `references/setup-guide.md` for uv, gcloud, and Vertex AI setup/troubleshooting
- **Prompt schemas**: See `references/prompt-schemas.md` for JSON structures
- **Curated examples**: See `references/examples.md` for Twitter-sourced prompts
- **Advanced techniques**: See `references/techniques.md` for spatial anchors, color stories, narrative elements
- **Semantic fields**: See `references/semantic-fields.md` for mood, narrative, and cultural code vocabulary
- **Vertex AI API**: See `references/vertex-ai-api.md` for model capabilities, resolutions, rate limits
