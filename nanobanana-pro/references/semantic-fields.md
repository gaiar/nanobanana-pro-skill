# Semantic Fields: Director's Notes for Nano Banana Pro

Nano Banana Pro interprets style not only through technical parameters (light/color) but through **semantic fields** — abstract concepts, mood, and implied narrative. These words function as "director's notes," determining micro-expressions, poses, and overall atmosphere.

## Table of Contents

1. [Emotional State & Mood](#emotional-state--mood)
2. [Hidden Narrative (Storytelling)](#hidden-narrative-storytelling)
3. [Cultural Codes & Archetypes (Vibe)](#cultural-codes--archetypes-vibe)
4. [Physical Sensations (Sensory)](#physical-sensations-sensory)
5. [How to Apply Semantic Fields](#how-to-apply-semantic-fields)

---

## Emotional State & Mood

Set the tone of the frame beyond simple "dark" or "light" descriptions.

| Semantic Term | Effect | Use Case |
|---------------|--------|----------|
| `fragile and intimate` | Tender poses, soft gazes | Urban environment portraits |
| `decadent exhaustion` | Luxury-weariness, "slumping" poses | Post-party, luxury settings |
| `severe elegance` | Cold, unapproachable aura, rigid poses | Leather outfits, high fashion |
| `quiet anxiety` | Nervous gestures (biting finger, staring into void) | Tension in luxury contexts |
| `melancholic` | "Sad romance" mood | Beach, water, solitary scenes |

### Example Applications

```
"Fragile and intimate" → subject naturally adopts gentle posture, softer gaze direction

"Decadent exhaustion" → specific fatigue-from-luxury pose, subject appears to slide down the table

"Severe elegance" → creates cold, unapproachable image, affects rigidity of leather-clad poses

"Quiet anxiety" → subject bites finger, stares into emptiness, tension in frame with luxury car

"Melancholic" → key word for creating "sad romance" at beach or in water
```

---

## Hidden Narrative (Storytelling)

Describe what happens "off-camera" or between characters.

| Semantic Term | Effect | Use Case |
|---------------|--------|----------|
| `clandestine meeting` | Danger, secrecy, averted gazes | Alley scenes, noir |
| `surveillance or departure` | Peeping effect, back-turned figures | Mystery, tension |
| `waiting for service that isn't coming` | Boredom, props like bell in hand | Luxury ennui |
| `ignoring the camera` | Paparazzi/documentary feel, no posing | Candid aesthetics |
| `performance anxiety` | Psychological drama context | Dressing room, backstage |

### Example Applications

```
"Clandestine meeting" → creates sense of danger and secrecy in alley, affects how characters (don't) look at each other

"Surveillance or departure" → explains why man stands with back turned watching woman, creates voyeuristic effect

"Waiting for service that isn't coming" → detail describing boredom with bell in hand

"Ignoring the camera" → creates paparazzi or documentary effect, removes "posing"

"Performance anxiety" → sets context for dressing room, transforms ordinary photo into psychological drama
```

---

## Cultural Codes & Archetypes (Vibe)

References to film genres or art that unpack into a complete set of visual rules.

| Semantic Term | Effect | Use Case |
|---------------|--------|----------|
| `Wong Kar-wai aesthetic` | Languid atmosphere, neon light, specific framing | Moody night scenes |
| `Ophelia trope` | "Girl in water" — passive pose, closed eyes, sleep/death feeling | Water, nature scenes |
| `silent wealth` | No loud logos, expensive textures (leather, velvet), restraint | Quiet luxury |
| `voyeuristic` | Shoot through obstacles (fence, window), peeping effect | Intimate surveillance |
| `sun-worship` | Ecstatic pose with head thrown back (not just "sunbathing") | Beach, outdoor |

### Example Applications

```
"Wong Kar-wai aesthetic" → immediately sets languid atmosphere, neon light, specific framing

"Ophelia trope" → code word for "girl in water," determines passive pose, closed eyes, sense of sleep/death

"Silent Wealth" → style excluding loud logos but requiring expensive textures (leather, velvet) and restraint

"Voyeuristic" → composition instruction: shoot through obstacles (fence, window), creating peeping effect

"Sun-worship" → describes ecstatic pose with head thrown back, not just "sunbathing"
```

---

## Physical Sensations (Sensory)

Tactile sensations that visualize through textures.

| Semantic Term | Effect | Use Case |
|---------------|--------|----------|
| `breathlessness` | Extreme facial proximity, sense of hearing each other's breath | Intimate couples |
| `attainable` | Interior feels cozy, realistic, not sterile-studio | Lifestyle shots |

### Example Applications

```
"Breathlessness" → describes extreme proximity of faces, where it seems characters hear each other's breath

"Attainable" → word for interiors that makes them cozy and realistic, not sterile-studio
```

---

## How to Apply Semantic Fields

### Integration Pattern

Add semantic terms to the `vibe` or `mood` sections of prompts:

```json
{
  "vibe": {
    "semantic_mood": "decadent exhaustion",
    "narrative_context": "waiting for service that isn't coming",
    "cultural_reference": "silent wealth",
    "sensory_quality": "attainable"
  }
}
```

### Natural Language Integration

```
A woman in a luxury hotel suite. The mood is decadent exhaustion —
she's been in this suite for three days, room service knows her order.
Silent wealth aesthetic: no logos, but you can tell the robe is cashmere.
The space feels attainable, lived-in, not a catalog shot.
```

### Key Principle

> Nano Banana Pro works as a **semantic engine**. A prompt is not a list of objects but a **director's task**. Words like "anxiety" or "voyeurism" affect the result as strongly as technical terms like "soft light."

### Combining Technical + Semantic

Strong prompts layer both:

```
Technical: "Side-lit, Kodak Portra 400, 85mm lens, shallow depth of field"
+
Semantic: "Quiet anxiety, ignoring the camera, fragile and intimate"
=
Result: Technically precise image with emotional depth
```
