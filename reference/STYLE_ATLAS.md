# Master Video Styles & Reference Atlas

A unified reference catalog and technical index compiled from the top open-source programmatic video and AI animation repositories:
- `awesome-claude-5-5-videos` (AthemeRoy)
- `awesome-opus5-5-videos` (yihui-dev)
- `ClaudeAnimationBase` (JohnHeibel)
- `PDoomVideo` (JohnHeibel)
- `pdoom-video` (mexicat)
- `lemo-opuscar` (lemomo-ai)
- `mg-styles-15` (Vincentwei1021)
- `prompt-motion` (prompt-motion.com)

---

## 1. The Reference Repositories & Catalogs

| Repository / Source | Focus & Strengths | Key Assets & Frameworks |
| :--- | :--- | :--- |
| **`awesome-claude-5-5-videos`** | 424 curated video cases across Opus/Sonnet/Haiku. Deep analysis of 11 content domains and 13 production styles. | Domain-style heatmaps, 9-frame sampling atlas, dark vs. light palette studies, production cost metrics. |
| **`awesome-opus5-5-videos`** | Curated catalog of high-impact AI animated shorts, developer workflows, and creative prompt matrices. | Prompt-to-video case studies, multi-model production pipelines, chapter & caption architectures. |
| **`ClaudeAnimationBase`** | Hand-painted 2D cartoon animation engine with p5.brush and character emotion rigging. | `ANIMATION_GUIDE.md`: 31 character emotions, 5 key views, 12fps linework boiling, "model the viewer" timing principles. |
| **`PDoomVideo` & `pdoom-video`** | Complete source code and storyboard for the viral "I'm Upping My P(doom)" animated music video. | `STORYBOARD.md`: Escalation arc (tiny monitor to planet-sized AI), motivated transitions, stage sets vs cards, props over text overlays. |
| **`lemo-opuscar`** | **66 production-ready video styles** with complete design invariants, palettes, typefaces, and native motion moves. | `DIRECTOR.md`, `MY-STYLES.md`, `TECHNIQUE.md`, style frame generators, and 66 individual style definition files (`STYLE.md`). |
| **`mg-styles-15`** | 15 code-driven motion graphics archetypes with runnable HTML/CSS/Canvas/Three.js demos. | Flat vector, line art, isometric, 3D render, cel-boil, collage, liquid, morph, kinetic typography, HUD telemetry. |
| **`prompt-motion.com`** | **236 curated crazy motion graphics prompts & video showcases** across kinetic type, 3D UI, and physics. | [`PROMPT_MOTION_INDEX.md`](PROMPT_MOTION_INDEX.md), [`prompt_motion_cards.json`](prompt_motion_cards.json), searchable prompts and video previews. |

---

## 2. Core Animation & Directing Invariants

### A. The "Model the Viewer" Timing Principle (from `ClaudeAnimationBase`)
* **Every visual cue is a "Read"**: For every moment, ask what the viewer needs to understand and how long it takes them to register it.
* **One Read at a Time**: Never overlap two competing visual surprises. Sequence cause and reaction.
* **Fast Actions, Slow Meanings**: Quick movement (120–200ms) to travel, followed by a held rest (400–800ms) to allow the meaning to land.
* **Lead the Eye**: Move the camera or use an accent light to direct attention *before* the action occurs.

### B. "Sets, Not Cards" & Motivated Transitions (from `PDoomVideo`)
* **Continuity Over Fragmentation**: Instead of cutting between arbitrary disconnected graphics cards, build unified spatial "sets" (the lab, the terminal desk, the stage) and animate the camera through them.
* **Motivated Cuts**: Every transition must be carried by motion:
  - Brush wipes across natural strokes
  - Physical impact / camera shake on heavy beats
  - Zooms through monitors, eye pupils, or doorways
  - Action follow-through across camera cuts

### C. Show, Don't Write (Anti-Text Clutter Rule)
* Models chronically over-rely on labels and text overlays.
* If a character is confused, show sweat drops and eye darts — do not put a floating sign saying "I am confused".
* Preserve typography for primary headlines, kinetic speech reinforcement, and monospace code.

---

## 3. The 66 Production Styles Catalog (`lemo-opuscar`)

| Style Category | Selected Styles | Best For | Typical Palette & Aesthetic |
| :--- | :--- | :--- | :--- |
| **Developer & Tech** | `dark-keynote`, `ascii-crt`, `hologram-hud`, `circuit-board`, `living-screencast`, `teardown`, `desktop-flythrough` | CLI tools, developer agents, SaaS demos, SDK launch videos | Deep carbon (`#141312`), bone white (`#ECE9E1`), terracotta (`#D97757`), electric cyan (`#00E5FF`). |
| **Editorial & Design** | `swiss-motion`, `silkscreen-poster`, `risograph`, `art-deco`, `blueprint`, `visual-investigation` | Brand stories, technical essays, journalism, architectural breakdowns | High contrast, bold grotesque typography, grid-locked layouts, textured paper grain. |
| **Data & Scientific** | `dataviz`, `iso-infographic`, `satellite-briefing`, `lidar-survey`, `data-physical`, `microscope` | Benchmarks, AI token efficiency, financial charts, infrastructure | Clean axes, isometric projection, neon telemetry, monospaced coordinate badges. |
| **Hand-Drawn & Organic** | `cel-anime-80s`, `watercolor`, `woodcut`, `crayon-book`, `ink-wash`, `paper-popup`, `whiteboard` | Metaphors, emotional storytelling, accessible explainers | 12fps line boil, p5.brush watercolour textures, soft pastel washes, paper edges. |
| **Pop & Entertainment** | `pixel-rpg`, `rubber-hose`, `game-show`, `scifi-toon`, `silent-film`, `papercut-red` | Viral TikTok/Reels, music videos, culture commentary | High saturation, beat-synced pops, dramatic cartoon takes. |

---

## 4. The 15 Motion Graphics Presets (`mg-styles-15`)

1. **`01-flat-vector`**: Clean 2D geometric shapes, bold flat color blocks, frictionless sliding.
2. **`02-line-art`**: Continuous stroke drawing with path length animation (`stroke-dashoffset`).
3. **`03-isometric`**: 30-degree orthographic projection of layered cards, grids, and systems.
4. **`04-3d-render`**: Three.js / WebGL hardware-accelerated volumetric lighting and spatial rotation.
5. **`05-cel-boil`**: Hand-drawn frame wobble reseeded at 12fps for human warmth.
6. **`06-collage`**: Cut-out paper, textured photography fragments, stop-motion cadence.
7. **`07-liquid`**: Viscous SVG metaball fluid dynamics and organic shape merging.
8. **`08-morph`**: Continuous vector shape morphing between distinct semantic icons.
9. **`09-kinetic-type`**: Word-by-word staggered scaling, letter spacing expansion, knock-out alpha text.
10. **`10-hud-ui`**: High-tech sci-fi telemetry, crosshairs, radial meters, live coordinate counters.
11. **`11-glassmorphism`**: Layered frosted glass panels (`backdrop-filter: blur(16px)`), specular border sheen.
12. **`12-paper-unfold`**: 3D origami folding and origami shadow casting.
13. **`13-particle-field`**: Floating point clouds, neural weight connection lines, attractor physics.
14. **`14-split-screen-grid`**: Dynamic 2x2 and 3x3 multi-camera reactive responsive layouts.
15. **`15-dark-terminal`**: Terminal-first monospace command typing, ANSI color syntax, live log streams.

---

## 5. Standard Project Usage Reference

Whenever planning or executing a video:
1. **Choose Style Base**: Reference any of the 66 styles from `lemo-opuscar/styles/<slug>` or 15 MG presets from `mg-styles-15/demos/<preset>`.
2. **Review Reference Implementations**:
   - For character / 2D animation: inspect `reference/repos/ClaudeAnimationBase/src/`
   - For viral music / narrative escalation: inspect `reference/repos/PDoomVideo/STORYBOARD.md`
   - For developer tool / terminal: inspect `reference/repos/mg-styles-15/demos/15-dark-terminal/` and `lemo-opuscar/styles/dark-keynote/`
3. **Execute Pre-Production Gate**: Create `storyboard.md`, `stylesheet.md`, and `storyboard_interactive.html` with explicit palette and timing references before rendering.
