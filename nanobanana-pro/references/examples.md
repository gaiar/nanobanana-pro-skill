# Curated Nano Banana Pro Examples

Best-performing prompts from Twitter and prompt engineering communities.

## Table of Contents

1. [Luxury Lifestyle Shot](#example-1-luxury-lifestyle-shot)
2. [Candid Morning Scene](#example-2-candid-morning-scene)
3. [Street Style with Car](#example-3-street-style-with-car)
4. [Balcony Night Scene](#example-4-balcony-night-scene)
5. [Elevator Mirror Selfie](#example-5-elevator-mirror-selfie)
6. [Product Branding Storyboard Grid](#example-6-product-branding-storyboard-grid)

---

## Example 1: Luxury Lifestyle Shot

**Concept**: Woman in luxury bathroom setting

**Key techniques**: Identity locking, environment detail, fabric physics

```
Using my photo as a strict and non-negotiable reference, preserve 100% of my facial identity — exact facial features, proportions, bone structure, skin texture, and natural expression. Do not alter, beautify, idealize, or stylize the face in any way. The face must remain fully authentic, realistic, and unchanged.

Create a hyper-realistic medium shot of a young woman sitting casually on a marble bathroom vanity countertop in a luxury interior. The image must follow real photographic logic, anatomy, and lighting behavior, avoiding any CGI or artificial look.

Subject & Pose:
The woman sits naturally on the edge of the vanity, relaxed and confident. Her posture is realistic, with natural weight distribution. Her legs are crossed casually at the ankles or resting in a relaxed position. One hand gently runs through her hair, while the other rests naturally on her thigh. She smiles warmly and looks directly into the camera, creating an intimate, candid connection.

Outfit & Styling:
She wears a short satin slip dress with thin spaghetti straps and a softly gathered bust. The fabric behaves realistically: visible sheen from light, natural folds and tension, accurate drape and gravity. A delicate pendant necklace completes the look. Makeup is minimal and editorial — natural skin texture, soft blush, subtle lip shine, no heavy contouring.

Environment:
A refined luxury bathroom interior: beige, speckled stone or ceramic tile walls, white and grey marble vanity countertop, dark wood cabinetry beneath. A large rectangular mirror with a wooden frame is positioned directly behind her, reflecting her back and a wooden door, adding depth and realism to the composition.

Foreground Props:
On the marble countertop in the foreground: a dark luxury perfume bottle with metallic accents, makeup brushes, an open lipstick, small skincare jars. To her right sits a white vessel sink. All objects are realistically scaled, naturally placed, and softly integrated into the scene.

Lighting & Atmosphere:
Warm, cinematic side lighting enters from the right, mimicking golden-hour sunlight. Distinct striped shadows (venetian blind / gobo effect) fall across her legs and the lower cabinetry. Light behaves naturally: soft highlights, gentle falloff, realistic contrast. The mood is intimate, cozy, and sun-drenched.

Camera & Photography Style:
Lifestyle and fashion editorial photography. Eye-level to slightly low camera angle. 50–85mm portrait lens look. Shallow depth of field with soft background separation. 35mm film aesthetic with subtle grain. Kodak Portra 400–style color grading: warm skin tones, gentle contrast, organic texture. Natural light only, no flash.

Overall Mood:
Intimate luxury, candid elegance, modern femininity. A private, cinematic moment captured with the realism and softness of analog film photography.

Negative Prompt:
altered face, different identity, idealized beauty, flawless skin, plastic or waxy texture, CGI, digital art, illustration, artificial lighting, broken anatomy, distorted hands, harsh shadows, overprocessed skin, cartoon style
```

---

## Example 2: Candid Morning Scene

**Concept**: Authentic lazy morning lifestyle

**Key techniques**: Imperfection details, natural light, lived-in environment

```json
{
  "subject_core": {
    "demographics": "24 years old, female, mixed French-Vietnamese heritage, pale skin with visible pores, scatterings of freckles across the nose bridge, and natural redness/flush on cheeks",
    "body_type": "5'5\", slight slouch, average build, soft shoulders, visible collarbones",
    "facial_features": "Wide expressive brown eyes, distinct cupid's bow, slightly crooked front tooth visible when smiling, soft jawline",
    "hair": "Jet black, messy 'bedhead' texture, chin-length bob with unruly bangs falling into eyes, frizzy halo from humidity"
  },

  "subject_styling": {
    "makeup_grooming": "Completely bare face, no makeup, chapped lips, faint dark circles under eyes, visible sleep crease on left cheek",
    "expression": "Mid-laugh, unguarded and genuine, eyes crinkled shut, mouth open in a sudden burst of amusement, highly candid",
    "pose_action": "Sitting cross-legged on a floor cushion, hunching forward slightly while trying to balance a plate of toast on one knee, one hand brushing hair out of face"
  },

  "wardrobe": {
    "top": "Oversized, heather grey hoodie, vintage and pilled fabric, coffee stain on the cuff, drawstrings uneven",
    "bottom": "Faded navy blue biker shorts, cotton stretch material",
    "footwear": "Barefoot, high detail on skin texture",
    "accessories": "Simple thin gold chain necklace, hair tie on wrist"
  },

  "environment_context": {
    "location": "Sun-drenched messy living room corner, apartment setting",
    "background_elements": "Stack of unread books, a dying houseplant, dust motes dancing in light beams, textured rug",
    "time_context": "Late Sunday morning, bright harsh sunlight streaming through blinds casting striped shadows, cozy atmosphere"
  },

  "cinematography_and_tech": {
    "lighting": "Natural window light, side-lit, high contrast (chiaroscuro), warm golden temperature, blown-out highlights in background",
    "camera_gear": "Fujifilm X100V, 23mm fixed lens, classic chrome simulation",
    "framing": "Eye-level, medium close-up, slightly off-center composition, snapshot aesthetic",
    "visual_fidelity": "High ISO noise/grain, sharp focus on eyes/teeth but soft background, believable texture rendering",
    "color_grading": "Desaturated greens, warm skin tones, filmic look, slightly lifted blacks to mimic printed photo"
  },

  "aspect_ratio": "4:5"
}
```

---

## Example 3: Street Style with Car

**Concept**: Influencer selfie with luxury car

**Key techniques**: Color story, main character energy, prop integration

```json
{
  "subject": {
    "description": "Young woman taking selfie next to chrome pink BMW i8, casual main character energy",
    "setting_rules": "street scene, luxury car, urban modern backdrop",
    "age": "early 20s",

    "expression": {
      "eyes": "focused on phone screen, taking selfie, casual confidence",
      "mouth": "relaxed, soft, natural",
      "brows": "relaxed, effortless",
      "overall": "unbothered, 'just casually next to a pink supercar' energy"
    },

    "hair": {
      "color": "platinum blonde",
      "style": "loose, flowing from under cap",
      "details": "messy-pretty, some pieces falling forward, effortless waves",
      "length": "medium-long, past shoulders"
    },

    "body": {
      "frame": "petite, slim, toned",
      "waist": "tiny, fully exposed midriff",
      "legs": "toned, athletic, fully visible",
      "stance": "casual lean against car, weight shifted"
    },

    "pose": {
      "position": "standing next to driver door of car, leaning slightly against it",
      "upper_body": {
        "action": "one arm UP holding phone for selfie",
        "phone_angle": "high, classic selfie position",
        "other_arm": "relaxed at side"
      },
      "lower_body": {
        "stance": "one leg straight, one slightly crossed or bent",
        "weight": "casual lean, hip near car",
        "energy": "relaxed but aware of angles"
      }
    }
  },

  "clothing": {
    "top": {
      "type": "ultra cropped baby tee",
      "color": "bright YELLOW, sunshine yellow",
      "graphic": "small star or cute graphic on chest",
      "fit": {
        "length": "EXTREME crop - ends just below chest, full stomach exposed",
        "tightness": "fitted, hugging curves",
        "sleeves": "short sleeves, casual"
      }
    },
    "bottom": {
      "type": "ultra mini athletic shorts",
      "color": "WHITE, clean bright white",
      "fit": {
        "style": "tight fitted athletic shorts",
        "length": "very short, upper thigh",
        "waist": "high-waisted, sits at natural waist"
      },
      "material": "stretchy athletic fabric, smooth"
    },
    "shoes": {
      "type": "white sneakers",
      "style": "clean, casual, athletic vibe"
    }
  },

  "accessories": {
    "headwear": {
      "type": "baseball cap",
      "color": "BLACK",
      "style": "worn forward, classic"
    },
    "headphones": {
      "type": "over-ear headphones",
      "color": "WHITE",
      "position": "around neck, not on ears"
    }
  },

  "the_car": {
    "make": "BMW i8",
    "wrap": "CHROME PINK / rose gold mirror finish",
    "effect": {
      "reflection": "mirror chrome reflecting everything around",
      "color": "pink/rose gold, flashy, attention-grabbing"
    },
    "presence": "the car is a CO-STAR, not just background"
  },

  "environment": {
    "location": "modern urban area, upscale shopping district",
    "ground": "cobblestone or nice pavement",
    "backdrop": {
      "buildings": "modern glass buildings, upscale retail",
      "vibe": "wealthy area, nice neighborhood"
    },
    "time": "daytime, good natural light"
  },

  "color_story": {
    "her": {
      "top": "bright YELLOW",
      "shorts": "clean WHITE",
      "cap": "BLACK",
      "headphones": "WHITE",
      "hair": "platinum BLONDE"
    },
    "car": "chrome PINK / rose gold",
    "overall": "yellow + white + pink chrome = eye-catching, vibrant, instagram-perfect"
  },

  "vibe": {
    "energy": "casual luxury, 'this is just my tuesday'",
    "mood": "unbothered, main character, casual flex",
    "contrast": "sporty casual outfit + absurd luxury car"
  }
}
```

---

## Example 4: Balcony Night Scene

**Concept**: Wine on balcony, late night, intimate selfie

**Key techniques**: Narrative-driven, tiredness without losing appeal, city backdrop

**Critical elements**:
- Camera POV: "We ARE her phone"
- Tired but alive expression
- Wine as storytelling prop
- City lights as backdrop
- The "struggle" to get face + background in frame

```
FACE:
- Big innocent doe eyes, heavy, tired, it's late
- But still that GLOW underneath
- The doe eyes at 70% power
- Wine-tired contentment
- Still looking at camera with THAT look

BODY:
- Petite frame, slim upper body
- Natural curves, small waist
- Soft, feminine proportions

SKIN:
- Pale white, fair porcelain
- Smooth, healthy, natural texture

HAIR:
- Platinum blonde, icy white-blonde
- Messy, end of day, been running hands through it
- Some tucked behind ear, some falling across face

THE POSE:
Camera Reality: We ARE her phone. She's sunk into balcony chair/couch. Phone held OUT to side at angle. Trying to get her face AND the city in frame. The struggle is real, the result is PERFECT. Night city behind her.

Setting: Apartment balcony, night, city lights, wine, her, alone with her phone.

THE WINE - THE PROP:
- Red wine, half empty
- Big wine glass, the proper kind
- Held loosely in one hand
- Wine says "relaxed", "loose", "honest hours"
- She's in THAT headspace - warm, open, soft

THE TOP - YELLOW KNIT CARDIGAN:
- Soft knit cardigan, warm yellow/mustard/golden color
- Chunky or medium knit, buttons down front
- Unbuttoned, hanging OPEN, not closed
- Shows what's under (maybe tiny bralette, maybe nothing)
- The warmth of the color against cool night

THE BALCONY DETAILS:
- Normal apartment balcony, not huge, not fancy but AESTHETIC
- String lights maybe draped, or just city lights doing the work
- Small outdoor couch or deep chair she's SUNK into
- Some plants in corner, maybe a candle burned low
- Wine bottle on small table, more than half gone

THE CITY BACKDROP:
- City lights sprawling behind
- Building lights, street lights, life
- The warm glow of urban night

LIGHTING & ATMOSPHERE:
Warm string lights or city glow. Soft, intimate. Late night energy. The kind of lighting that makes everything look romantic.

PHOTOGRAPHY STYLE:
Phone camera selfie aesthetic. Natural, intimate, real. The kind of photo that feels private even if she posts it.

VIBE:
- Balcony hours, wine time
- Alone but not lonely
- Tired but ALIVE
- The late night that feels like a secret
- Soft, warm, intimate
- The photo that feels private even if she posts it
```

---

## Example 5: Elevator Mirror Selfie

**Concept**: Stylish elevator selfie with layered outfit

**Key techniques**: Specific location atmosphere, outfit layering, narrative backstory

```json
{
  "scene": {
    "type": "elevator_mirror_selfie",
    "location": "apartment_elevator",
    "time": "daytime",
    "lighting": "warm_elevator_light",
    "atmosphere": "intimate_between_floors"
  },

  "camera": {
    "pov": "we_are_the_phone",
    "type": "mirror_selfie",
    "angle": "chest_level_slightly_angled",
    "framing": "full_body_in_mirror",
    "phone_visible": true
  },

  "subject": {
    "pose": {
      "stance": "facing_mirror_hips_angled",
      "weight": "on_one_leg_hip_soft_curve_out",
      "energy": "relaxed_effortless_not_aggressive",
      "arms": {
        "right": "holding_phone_for_selfie",
        "left": "carrying_jacket_draped_over_forearm"
      }
    },
    "expression": {
      "eyes": {
        "style": "soft_doe_eyes_through_lowered_lashes",
        "energy": "knowing_not_sleepy",
        "contact": "looking_at_camera_direct",
        "message": "i_see_you_looking"
      },
      "cheeks": {
        "color": "soft_pink_flush",
        "reason": "just_came_in_from_cold",
        "texture": "healthy_rosy_alive"
      },
      "lips": {
        "position": "soft_part_slightly_open",
        "color": "pink_glossy",
        "energy": "about_to_say_something"
      }
    },
    "hair": {
      "color": "platinum_blonde_icy_white",
      "style": "long_loose_slightly_wavy",
      "placement": "falling_from_under_cap_over_shoulders"
    }
  },

  "outfit": {
    "hat": {
      "type": "baseball_cap",
      "color": "forest_green_or_olive",
      "wear_style": "forward_classic",
      "effect": "shadows_forehead_intensifies_eyes"
    },
    "top": {
      "type": "cropped_long_sleeve",
      "fabric": "ribbed_knit_thin_fitted",
      "color": "black",
      "fit": "tight_every_curve_traced",
      "length": "cropped_above_belly_button"
    },
    "skirt": {
      "type": "pleated_tennis_skirt",
      "color": "crisp_white",
      "fit": "high_waisted",
      "length": "short_upper_thigh",
      "detail": "gap_of_bare_skin_between_crop_and_skirt"
    },
    "stockings": {
      "type": "fishnet_thigh_highs",
      "color": "black",
      "pattern": "small_diamond_delicate",
      "top": "thin_lace_band",
      "thigh_gap": "1-2_inches_bare_skin_between_skirt_and_lace"
    },
    "jacket": {
      "type": "leather_or_olive_khaki",
      "status": "draped_over_forearm_not_worn",
      "purpose": "adds_context_story_texture"
    }
  },

  "accessories": {
    "bag": {
      "type": "small_crossbody",
      "material": "black_leather",
      "position": "strap_diagonal_across_chest"
    },
    "earrings": "small_silver_hoops",
    "necklace": "thin_silver_chain_tiny_pendant"
  },

  "color_story": {
    "primary": ["forest_green_cap", "black_top", "white_skirt", "black_fishnet"],
    "accents": ["platinum_blonde", "pale_skin", "pink_flush"],
    "contrast": "green_vs_blonde, white_vs_black, pure_vs_sin"
  },

  "narrative": {
    "context": "girl_in_transit_between_places",
    "backstory": "just_came_from_outside_flushed_cheeks_jacket",
    "action": "caught_herself_in_mirror_liked_what_she_saw",
    "intention": "stopped_to_take_this_for_someone"
  },

  "vibe": {
    "core": "soft_invitation_knowing_effortless",
    "contrast": "sporty_cap_vs_fishnet_sin, casual_vs_calculated",
    "energy": "she_knows_you_know"
  }
}
```

---

## Example 6: Product Branding Storyboard Grid

**Concept**: 3x3 grid mockup presentation for product branding portfolio

**Key techniques**: Multi-panel composition, consistent product identity across frames, editorial designer aesthetic, varied camera angles within a cohesive series

**Usage**: Requires a reference product image via `--image` flag. The model preserves the product's packaging, branding, materials, colors and proportions across all nine panels.

```
Create ONE final image.

A clean 3×3 [ratio] storyboard grid with nine equal [ratio] sized panels on [4:5] ratio.

Use the reference image as the base product reference. Keep the same product, packaging design, branding, materials, colors, proportions and overall identity across all nine panels exactly as the reference. The product must remain clearly recognizable in every frame. The label, logo and proportions must stay exactly the same.

This storyboard is a high-end designer mockup presentation for a branding portfolio. The focus is on form, composition, materiality and visual rhythm rather than realism or lifestyle narrative. The overall look should feel curated, editorial and design-driven.

FRAME 1:
Front-facing hero shot of the product in a clean studio setup. Neutral background, balanced composition, calm and confident presentation of the product.

FRAME 2:
Close-up shot with the focus centered on the middle of the product. Focusing on surface texture, materials and print details.

FRAME 3:
Shows the reference product placed in an environment that naturally fits the brand and product category. Studio setting inspired by the product design elements and colours.

FRAME 4:
Product shown in use or interaction on a neutral studio background. Hands and interaction elements are minimal and restrained, the look matches the style of the package.

FRAME 5:
Isometric composition showing multiple products arranged in a precise geometric order from the top isometric angle. All products are placed at the same isometric top angle, evenly spaced, clean, structured and graphic.

FRAME 6:
Product levitating slightly tilted on a neutral background that matches the reference image color palette. Floating position is angled and intentional, the product is floating naturally in space.

FRAME 7:
is an extreme close-up focusing on a specific detail of the label, edge, texture or material behavior.

FRAME 8:
The product in an unexpected yet aesthetically strong setting that feels bold, editorial and visually striking.
Unexpected but highly stylized setting. Studio-based, and designer-driven. Bold composition that elevates the brand.

FRAME 9:
Wide composition showing the product in use, placed within a refined designer setup. Clean props, controlled styling, cohesive with the rest of the series.

CAMERA & STYLE:
Ultra high-quality studio imagery with a real camera look. Different camera angles and framings across frames. Controlled depth of field, precise lighting, accurate materials and reflections. Lighting logic, color palette, mood and visual language must remain consistent across all nine panels as one cohesive series.

OUTPUT:
A clean 3×3 grid with no borders, no text, no captions and no watermarks.
```

**Notes**:
- Replace `[ratio]` in the first line with the desired panel aspect ratio (e.g., `1:1`, `4:5`, `3:4`)
- The outer grid ratio is fixed at `4:5` — this works well for Instagram and portfolio presentations
- Always pass the product reference image via `--image` flag
- This is a natural language prompt — JSON format is not needed because the structure comes from the frame-by-frame directives
- The prompt is designed to be used as-is with minimal customization — just swap the ratio placeholder

---

## Prompt Engineering Patterns From These Examples

### Pattern 1: The Identity Lock Opening
Always start with explicit face preservation when using reference photos.

### Pattern 2: The "We ARE the Camera" Perspective
Define POV explicitly for selfies and first-person shots.

### Pattern 3: Fabric Physics
Always describe how fabric interacts with light and gravity.

### Pattern 4: The Narrative Hook
Include story context—why is this photo being taken?

### Pattern 5: Color Story Coordination
List all colors explicitly and describe their harmony.

### Pattern 6: Imperfection Details
Add realistic imperfections: sleep creases, chapped lips, coffee stains, frizzy hair.

### Pattern 7: The Negative Prompt Shield
Always include negative prompts to prevent common AI artifacts.

### Pattern 8: The Multi-Panel Grid
For storyboard/grid compositions, describe each frame individually with specific camera angle, framing, and purpose. Include a global "CAMERA & STYLE" section to enforce visual consistency across all panels. Specify the output format explicitly ("clean 3x3 grid, no borders, no text").
