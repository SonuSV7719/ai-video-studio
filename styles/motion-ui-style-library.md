# Motion & UI/UX Style Library

The catalogue of **motion styles** and **UI/UX styles**. Use it in the **Style
Pass** (see the end): pick a motion style, a UI style and a caption style
deliberately before building. A style is a *routing word* — it decides material,
density, ornament and motion. Never say only "make it glassmorphic"; name the
style, the job, and the failure mode.

---

## PART A · Motion styles

### A1 · Motion types (the format)
Explainer · UI/UX animation · logo animation · title sequence · animated
infographic · social motion graphic · product animation · kinetic typography ·
isometric animation · abstract motion · 2D character animation · 3D motion design ·
mixed-media motion · data-visualisation motion · educational motion.

### A2 · Motion styles (the look)
| Style | The look |
|---|---|
| **Kinetic typography** | text is the animation — slides, stretches, breaks, reforms on the beat |
| **Isometric** | fixed-angle fake 3D from 2D shapes; clean, dynamic |
| **3D motion design** | modelled + animated, cinematic; product/architectural |
| **3D-2D hybrid** | flat UI with depth cues, fake parallax, 3D accents in a 2D layout |
| **Abstract** | tone over message; shapes and colour |
| **Minimal / bold minimalism** | clean space, heavy type, bright accent, restrained motion |
| **Maximalism** | dense, loud, layered, textured |
| **Editorial / type-led** | print grammar: big headlines, generous whitespace |
| **Liquid motion** | fluid morphing, stretchy transitions, seamless loops |
| **Liquid glass** | translucent, refractive, fluid depth (Apple's language) |
| **Deep glow** | intense blooms, layered neon, radiant gradients |
| **Cutout craft** | paper-cut, collage, scanned textures, handmade |
| **Analog / retro film** | grain, dust, scratches, frame jitter, warm fade, VHS/Super 8 |
| **Grunge street** | torn paper, paint, marker, ripped tape, jump edits |
| **Movie-title / cinematic** | film typography, slow moves, deep shadows, flares, grain |
| **Glitch 2.0** | precise, intentional digital distortion (not chaotic VHS) |
| **Retro-futurism** | 1950s–80s optimism + modern tech |
| **Y2K / vaporwave** | chrome, pixelation, lo-fi nostalgia, magenta/cyan |
| **Painterly 3D** | brush-like textures on 3D; warm, handcrafted |
| **Stop-motion-inspired CGI** | clay/puppet surfaces, miniature sets, "on twos" timing |
| **Mixed media** | 2D + 3D + photo + illustration + live action in one frame |
| **Expressive mascot** | odd/funny/cute character carried through |
| **Oddly satisfying** | soft-body, liquid flow, magnetic snap, looping machines |
| **Data-viz motion** | charts and maps that animate the number |
| **Coded / generative** | procedural systems, ASCII, reactive physics, shaders |

### A3 · Motion techniques
Morphing · mixing 2D+3D · thin lines · limited palette · grain · micro-animations ·
storytelling-through-motion · VR/AR animation · procedural/generative systems ·
state-machine interactive motion · node-based procedural · "on twos/threes"
(12/8 fps cadence).

### A4 · The 2026 signal
Authenticity over polish: grain, handmade imperfection, tactile textures in;
glossy over-produced perfection out. Plus AI-assisted production, real-time 3D,
brand-systemised motion, and short-form as the default.

---

## PART B · UI/UX styles

The catalogues run long (67 / 68 / 50+ / 41 styles). Grouped into families:

### B1 · Depth & surface (illusion)
Glassmorphism · dark glassmorphism · glassmorphism-lite · frosted acrylic
(Windows 11) · **liquid glass** (Apple) · glass + grain · glassmorphism v3
(dynamic tint) · neumorphism / soft UI · dark neumorphism · soft-UI pastel ·
claymorphism · clay + dark · modern skeuomorphism · skeuomorphism 2.0 ·
hyperrealism.

### B2 · Flat & structured
Flat design · flat 3.0 · Material Design · Material 3 / Material You · Fluent ·
Metro · Swiss / International type · Swiss modernism 2.0 · minimalism · bold /
expressive minimalism · monochrome · ultra-minimal whitespace · corporate clean ·
Notion-style · Stripe-style.

### B3 · Raw & experimental
Brutalism · neobrutalism · soft brutalism · anti-design · anti-polish/raw ·
deconstructed design · pixel-art UI · terminal / CLI · databending / corrupt ·
cyberpunk / neon · holographic / prismatic · ASCII art UI · Memphis · stained
glass · steampunk.

### B4 · Retro & nostalgia
Y2K / retro chrome · aqua · Windows Aero · vaporwave / synthwave · retro
futurism · retro vintage · magazine grid.

### B5 · Layout-led
Bento grid · glass + bento · progressive blur · anti-grid / organic layouts ·
aurora UI / gradient mesh · mesh gradient · conic gradient · grain + gradient ·
split screen · masonry flow · card stack · magazine grid.

### B6 · Nature & organic
Organic / handcrafted · watercolour · natural organic · biophilic · wabi-sabi ·
farmhouse / cottagecore.

### B7 · Spatial & futuristic
Spatial UI (visionOS) · 3D UI · mixed-reality / AR UI · AI-native UI · HUD /
sci-fi.

### B8 · Motion-first
Kinetic typography · parallax · glassmorphism-in-motion · particle · aurora ·
motion-driven.

### B9 · Industry / vendor languages
Apple HIG (Aqua → Liquid Glass) · Material 3 · Fluent (Microsoft) · Ant Design ·
shadcn/ui · macOS vibrancy · corporate Memphis · macOS/Windows-native.

---

## PART C · UI/UX trends & patterns (behaviour, 2026)
AI-native / conversational UI · agentic UX (intent-driven) · copilot UI (not
autopilot) · generative & adaptive interfaces · adaptive personalisation ·
multimodal interaction · graphical-first / direct manipulation · voice UI &
zero-UI · accessibility-first design · purposeful / functional motion ·
micro-interactions · dark mode as default · expressive oversized typography ·
fluid / variable typography · richer colour + subtle depth ("dopamine" palettes) ·
3D & immersive elements · experimental navigation · gamified design · data-driven
storytelling · design tokens · MX design (machine-experience) · calm interfaces ·
ethical / transparent design · responsible glassmorphism · bento grids.

---

## PART D · The Style Pass (run it while writing CONCEPT.md)

**No style is mandatory.** There is no house look you must use. Pick the style
that fits the brief, recommend it with your reasoning, and use it. The Apple
Standard is the pack's default *suggestion* for product/UI/corporate work — one
option among many, not a rule. Nothing is deprecated.

Before building, pick deliberately and record it in CONCEPT.md:

| Slot | Choose | Why |
|---|---|---|
| **Motion style** | one from Part A2 | sets the whole motion language |
| **UI style** | one from Part B (if a UI appears) | sets surfaces, depth, type |
| **Caption style** | one from `CAPTION-STYLES.md` | sets the text voice |
| **Colour / grade** | the look | sets tone |
| **Motion system** | easing curves, transition library, scene templates | keeps every video on-brand |

Rules:
- **One primary + one garnish.** Pick a dominant style and at most one accent.
- **Name the failure mode.** Every style has one (neumorphism fails contrast;
  glassmorphism fails text; brutalism fails hierarchy if careless).
- **Prove it before the build** — a style frame (a still at final quality) locks
  the look at the cheapest moment.
- The style governs **how** the mandatory features look, never **whether** they
  are used.
