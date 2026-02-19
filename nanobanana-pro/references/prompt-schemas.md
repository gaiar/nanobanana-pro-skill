# Nano Banana Pro JSON Prompt Schemas

## Table of Contents

1. [Full Photorealistic Schema](#full-photorealistic-schema)
2. [Lifestyle/Editorial Schema](#lifestyleeditorial-schema)
3. [Mirror Selfie Schema](#mirror-selfie-schema)
4. [Art Director Schema](#art-director-schema)

---

## Full Photorealistic Schema

Maximum control for hyper-realistic images:

```json
{
  "subject": {
    "description": "[Short concept description]",
    "setting_rules": "[Scene constraints]",
    "age": "[Specific age or range]",

    "expression": {
      "eyes": "[Eye behavior and gaze]",
      "mouth": "[Lip position and mood]",
      "brows": "[Brow position]",
      "overall": "[Emotional energy]"
    },

    "hair": {
      "color": "[Specific color]",
      "style": "[How it's worn]",
      "details": "[Texture, movement]",
      "length": "[Specific length]"
    },

    "body": {
      "frame": "[Build description]",
      "waist": "[Waist description]",
      "legs": "[Leg description]",
      "stance": "[Weight distribution]"
    },

    "pose": {
      "position": "[Where in scene]",
      "upper_body": {
        "action": "[Arm positions]",
        "other_arm": "[Secondary arm]"
      },
      "lower_body": {
        "stance": "[Leg positions]",
        "weight": "[Weight distribution]",
        "energy": "[Movement quality]"
      },
      "overall": "[Pose vibe]"
    },

    "face": {
      "features": "[Specific facial features]",
      "makeup": "[Makeup level and style]",
      "expression": "[Micro-expression]"
    }
  },

  "clothing": {
    "top": {
      "type": "[Garment type]",
      "color": "[Specific color]",
      "graphic": "[Any prints/graphics]",
      "fit": {
        "length": "[Where it ends]",
        "tightness": "[How it fits]",
        "sleeves": "[Sleeve style]"
      },
      "effect": "[Visual result]"
    },
    "bottom": {
      "type": "[Garment type]",
      "color": "[Specific color]",
      "fit": {
        "style": "[Cut/style]",
        "length": "[Where it ends]",
        "waist": "[Waist position]",
        "effect": "[Visual result]"
      },
      "material": "[Fabric type]"
    },
    "shoes": {
      "type": "[Shoe type]",
      "style": "[Aesthetic]",
      "effect": "[Completes look how]"
    }
  },

  "accessories": {
    "headwear": {
      "type": "[Item type]",
      "color": "[Color]",
      "style": "[How worn]",
      "effect": "[Visual effect]"
    },
    "jewelry": {
      "earrings": "[Type and style]",
      "necklace": "[Type and style]",
      "rings": "[Type and style]"
    },
    "device": {
      "type": "[Phone/device]",
      "position": "[Where held]"
    }
  },

  "environment": {
    "location": "[Specific setting]",
    "ground": "[Surface type]",
    "backdrop": {
      "buildings": "[Background elements]",
      "elements": "[Additional details]",
      "vibe": "[Atmosphere]"
    },
    "time": "[Time of day]",
    "atmosphere": "[Overall mood]"
  },

  "photography": {
    "style": "[Photography genre]",
    "angle": "[Camera angle]",
    "quality": "[Technical quality]",
    "framing": "[Composition]",
    "lighting": "[Light quality]"
  },

  "color_story": {
    "subject_colors": "[List key colors on subject]",
    "environment_colors": "[List environment colors]",
    "overall": "[Color harmony description]"
  },

  "vibe": {
    "energy": "[Core energy]",
    "mood": "[Emotional tone]",
    "contrast": "[Visual/conceptual contrasts]",
    "story": "[Narrative element]"
  }
}
```

---

## Lifestyle/Editorial Schema

Optimized for natural, candid-looking shots:

```json
{
  "subject_core": {
    "demographics": "[Age, gender, ethnicity, skin texture details]",
    "body_type": "[Height, build, posture details]",
    "facial_features": "[Eye shape/color, nose, jawline, specific features]",
    "hair": "[Color, style, texture, movement]"
  },

  "subject_styling": {
    "makeup_grooming": "[Makeup style, skin finish, imperfections]",
    "expression": "[Micro-expression, mood, gaze direction]",
    "pose_action": "[Posture, hand placement, dynamic action]"
  },

  "wardrobe": {
    "top": "[Material, fit, color, texture, wear-and-tear]",
    "bottom": "[Type, fit, details]",
    "footwear": "[Style, condition]",
    "accessories": "[Jewelry, bags, distinct items]"
  },

  "environment_context": {
    "location": "[Specific setting with depth]",
    "background_elements": "[Objects, foliage, architecture]",
    "time_context": "[Time of day, weather, atmospheric particles]"
  },

  "cinematography_and_tech": {
    "lighting": "[Light source, direction, temperature, hardness/softness]",
    "camera_gear": "[Camera type, lens mm, film stock or sensor]",
    "framing": "[Shot scale, angle, composition rule]",
    "visual_fidelity": "[Grain, sharpness, depth of field, texture]",
    "color_grading": "[Palette, saturation, contrast style]"
  },

  "aspect_ratio": "[e.g., 16:9, 9:16, 4:5, 3:4]"
}
```

---

## Mirror Selfie Schema

Specialized for reflective/selfie compositions:

```json
{
  "scene": {
    "type": "[mirror_selfie, elevator_selfie, etc.]",
    "location": "[Specific location]",
    "time": "[Time of day]",
    "lighting": "[Light source]",
    "atmosphere": "[Mood]"
  },

  "camera": {
    "pov": "we_are_the_phone",
    "type": "[mirror_selfie, front_camera, etc.]",
    "angle": "[Camera angle]",
    "framing": "[Full body, half body, etc.]",
    "phone_visible": true
  },

  "subject": {
    "pose": {
      "stance": "[Body position]",
      "weight": "[Weight distribution]",
      "energy": "[Movement quality]",
      "arms": {
        "right": "[Right arm action]",
        "left": "[Left arm action]"
      }
    },
    "expression": {
      "eyes": {
        "style": "[Eye expression]",
        "energy": "[Eye mood]",
        "contact": "[Gaze direction]"
      },
      "cheeks": {
        "color": "[Cheek color/flush]",
        "texture": "[Skin quality]"
      },
      "lips": {
        "position": "[Lip position]",
        "color": "[Lip color]",
        "energy": "[Lip mood]"
      }
    },
    "hair": {
      "color": "[Hair color]",
      "style": "[Hair style]",
      "placement": "[Where hair falls]"
    }
  },

  "outfit": {
    "hat": {
      "type": "[Hat type]",
      "color": "[Color]",
      "wear_style": "[How worn]",
      "effect": "[Visual effect]"
    },
    "top": {
      "type": "[Top type]",
      "fabric": "[Material]",
      "color": "[Color]",
      "fit": "[How it fits]",
      "length": "[Where it ends]"
    },
    "bottom": {
      "type": "[Bottom type]",
      "color": "[Color]",
      "fit": "[How it fits]",
      "length": "[Where it ends]"
    },
    "legwear": {
      "type": "[Type if any]",
      "color": "[Color]",
      "detail": "[Pattern/texture]"
    }
  },

  "accessories": {
    "bag": {
      "type": "[Bag type]",
      "material": "[Material]",
      "position": "[Where positioned]"
    },
    "earrings": "[Type]",
    "necklace": "[Type]",
    "rings": "[Type]"
  },

  "color_story": {
    "primary": ["[List primary colors]"],
    "accents": ["[List accent colors]"],
    "contrast": "[Color contrast description]"
  },

  "narrative": {
    "context": "[Story context]",
    "backstory": "[What led to this moment]",
    "action": "[What's happening now]",
    "intention": "[Why taking this photo]"
  },

  "vibe": {
    "core": "[Core feeling]",
    "contrast": "[Visual/emotional contrast]",
    "energy": "[Energy level]"
  }
}
```

---

## Art Director Schema

For professional use—converts simple concepts to full prompts:

```json
{
  "subject_core": {
    "demographics": "[Age, gender, ethnicity, detailed skin texture]",
    "body_type": "[Height, build, weight, physical traits]",
    "facial_features": "[Eye shape/color, nose, jawline, specific features]",
    "hair": "[Color, style, texture, movement]"
  },

  "subject_styling": {
    "makeup_grooming": "[Makeup style, facial hair, skin finish, imperfections]",
    "expression": "[Micro-expression, mood, gaze direction]",
    "pose_action": "[Posture, hand placement, dynamic action]"
  },

  "wardrobe": {
    "top": "[Material, fit, color, texture, wear-and-tear]",
    "bottom": "[Type, fit, details]",
    "footwear": "[Style, condition]",
    "accessories": "[Jewelry, bags, tech, distinct items]"
  },

  "environment_context": {
    "location": "[Specific setting, depth]",
    "background_elements": "[Objects, people, foliage, architecture]",
    "time_context": "[Time of day, weather, season, atmospheric particles]"
  },

  "cinematography_and_tech": {
    "lighting": "[Light source, direction, temperature, hardness/softness]",
    "camera_gear": "[Camera type, lens mm, film stock or sensor type]",
    "framing": "[Shot scale, angle, composition rule]",
    "visual_fidelity": "[Grain, sharpness, depth of field, texture quality]",
    "color_grading": "[Palette, saturation, contrast style]"
  },

  "aspect_ratio": "[e.g., 16:9, 9:16, 1:1, 4:5, 3:4]"
}
```

---

## Quick Reference: Common Values

### Camera Gear
- `"Fujifilm X100V, 23mm fixed lens, classic chrome simulation"`
- `"Shot on iPhone 15 Pro, 24mm lens"`
- `"Canon EOS R5, 85mm f/1.4"`
- `"Disposable film camera"`

### Film Stocks / Color Grading
- `"Kodak Portra 400 - warm skin tones, gentle contrast"`
- `"Fujifilm Pro 400H - soft pastels, lifted shadows"`
- `"Cinestill 800T - tungsten, halation, cinema look"`
- `"VSCO A6 analog preset"`

### Lighting Types
- `"Natural window light, side-lit, high contrast"`
- `"Warm golden-hour sunlight from right"`
- `"Hard flash photography with starburst flare"`
- `"Soft diffused overcast light"`

### Visual Fidelity
- `"High ISO noise/grain, sharp focus on eyes"`
- `"Shallow depth of field with soft background separation"`
- `"35mm film aesthetic with subtle grain"`
- `"Motion blur on hands, sharp face"`
