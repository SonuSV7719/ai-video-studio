---
name: lemo-opuscar
description: Direct and produce short films, animations, and motion graphics entirely in code using the 66 curated styles from the Lemo-Opuscar library (e.g. Dark Keynote, Swiss Motion, Hologram HUD, ASCII CRT, Blueprint, Teardown, Ukiyo-e, Cel Anime). Use when the user asks for a video, film, short, promo, explainer or animation in a named style, when planning video aesthetics, or when making a custom code-rendered film style.
argument-hint: "[style-name|list|make] [topic-or-brief]"
metadata:
  author: lemomo-ai
  version: "1.0.0"
---

# Lemo-Opuscar: 66 Code-Rendered Film Styles Library

The complete **Lemo-Opuscar** film style engine and directory. Every style is a complete, code-driven video pipeline that renders frames via headless Chrome/Canvas/Three.js and joins them with synthesized soundtracks and voiceover via local FFmpeg.

**Local Library Path**:  
`C:\Users\sonup\.gemini\antigravity\scratch\video-studio\reference\repos\lemo-opuscar`

---

## 1. Operating Rules & Pre-Production Gate

1. **Mandatory 3-Folder Structure**: Every project workspace MUST maintain:
   - `raw_footage/`: Raw screencasts, terminal sessions, camera takes, raw voice recordings.
   - `reference/`: Reference reels, competitor benchmarks, downloaded clips (via `yt-dlp`).
   - `export/`: Rendered storyboard assets, HTML interactive previews, final video masters.
2. **Review Gate**: ALWAYS present the visual storyboard and stylesheet to the user for confirmation BEFORE generating final render code or executing builds.
3. **Natural Camera Clarity (Strictly 0% Synthetic Blur)**: When blending real camera takes with motion graphics, preserve 100% crisp camera footage with broadcast tone mapping.
4. **Broadcast Audio Standards**: Master dialogue to **-14 to -16 LUFS** using FFmpeg `dynaudnorm`.

---

## 2. The 66 Production Styles Catalog

The 66 styles are located in `$LIB/styles/<slug>/` (each with its own `STYLE.md`, palette, typography, and native moves):

### A. Tech, Developer & Product Launch
- **`dark-keynote`**: Minimalist dark UI, deep carbon (`#141312`), bone white, warm terracotta/coral accents. Ideal for CLI tools, agents, and SDK releases.
- **`ascii-crt`**: Retro green/amber phosphor terminal, CRT scanlines, monospaced ASCII rendering.
- **`hologram-hud`**: Sci-fi telemetry, glowing vector wireframes, floating coordinate meters.
- **`living-screencast`**: Dynamic screen recordings with smooth camera zooms and cursor trails.
- **`teardown`**: Exploded-view 3D hardware and UI component disassembly.
- **`desktop-flythrough`**: Continuous 3D camera pan over developer desktop environments.
- **`circuit-board`**: Neon traces lighting up across dark silicon substrates.

### B. Editorial, Data & Infographics
- **`swiss-motion`**: Strict grid layouts, bold grotesque sans-serif typography, stark contrast.
- **`dataviz`**: Fluid animated charts, scatter plots, trend lines, and metrics.
- **`iso-infographic`**: 30-degree orthographic projection of layered cards, servers, and networks.
- **`satellite-briefing`**: High-altitude geospatial camera zooms with tactical overlays.
- **`visual-investigation`**: Documentary evidence framing, newspaper cutouts, highlighted documents.
- **`blueprint`**: Technical CAD architectural drafting with white line work on cyan/navy.

### C. Artistic, Narrative & Character
- **`cel-anime-80s`**: Retro hand-drawn anime aesthetic with soft grain and chromatic aberration.
- **`watercolor`**: Organic pigments bleeding on textured paper grain with 12fps line boil.
- **`ink-wash`**: East Asian sumi-e brush strokes with dynamic ink flow.
- **`paper-popup`**: 3D pop-up storybook with folding shadow physics.
- **`woodcut`**: Bold textured relief printing with high graphic contrast.
- **`risograph`**: Multilayer spot-color print aesthetic with misregistration textures.

---

## 3. Workflow: Producing a Film in a Style

### Step 1: Select or Recommend a Style
Inspect available styles or help the user pick based on their topic:
```powershell
Get-ChildItem "C:\Users\sonup\.gemini\antigravity\scratch\video-studio\reference\repos\lemo-opuscar\styles"
```
Read the style's specification:
```powershell
Get-Content "C:\Users\sonup\.gemini\antigravity\scratch\video-studio\reference\repos\lemo-opuscar\styles\<slug>\STYLE.md"
```

### Step 2: Generate Storyboard & Stylesheet Gate
Before writing code or rendering, extract the style's design invariants:
- **`stylesheet.md`**: Color tokens, typography, motion easing curves, safe zones.
- **`storyboard.md`**: Scene breakdown (2–4s per beat), shot layouts, graphic overlays, audio cues.
- **Interactive Storyboard**: Run `python tools/generate_interactive_storyboard.py` to create a clickable visual preview deck.

### Step 3: Present for Approval
Present the storyboard and stylesheet to the user. Await confirmation before compiling renders.
