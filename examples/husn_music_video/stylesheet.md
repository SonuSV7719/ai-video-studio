# Design Stylesheet — "Husn" (Anuv Jain) AI Kinetic Music Video
**Format**: 1080x1920 (9:16 Vertical Reel) | **Framerate**: 24.000 CFR | **Duration**: 30.0s  
**Director Style**: Zero-Timeline Multi-Layered Kinetic Collage (Claude / AI Music Video Aesthetic)

---

## 🎨 Color Palette & Visual Identity

Inspired by indie acoustic warmth, midnight nostalgia, and high-contrast editorial typography:

```css
:root {
  /* Canvas & Atmospheric Background */
  --bg-dark: #0B0B0E;              /* Deep obsidian night */
  --bg-warm-shadow: #141318;       /* Subtle warm vignette */
  --bg-card-glass: rgba(28, 27, 34, 0.72); /* Frosted liquid glass (blur 24px) */
  --glass-border: rgba(255, 255, 255, 0.12);

  /* Primary Typography */
  --text-primary: #F7F5EE;         /* Warm milk paper */
  --text-muted: #9E9AA6;           /* Distant haze */
  --text-dim: #54515E;             /* Subtle timestamp/metadata */

  /* Emotional Accent Sparks */
  --accent-coral: #FF4A3D;         /* Heartbreak / raw passion punch */
  --accent-amber: #F5A623;         /* Warm streetlamp glow / lyric highlight */
  --accent-cyan-ice: #00E5FF;      /* High-contrast UI bracket / face lock */
}
```

---

## 🔤 Typography Specification

1. **Massive Behind-The-Head Typographic Drops (`backdrop-word`)**:
   - Font: `Archivo Black` / `Anton` (Display Bold)
   - Size: `180px` – `240px` (Upper-case, track-tight -4px)
   - Color: Semi-translucent `--text-primary` (opacity `0.15` to `0.30`) or `--accent-coral`
   - Layer: Rendered behind singer's silhouette/head cutout using MediaPipe segmentation.

2. **Kinetic Subtitle & Lyric Highlight**:
   - Font: `Inter` / `Montserrat` (Medium 600)
   - Size: `38px` – `44px`
   - Inactive Word: `--text-muted` (`#9E9AA6`)
   - Active Word (Synced to vocal singing): Glowing `--accent-amber` (`#F5A623`) with pill backdrop

3. **Handwritten Marker & Sketch Accents (`crayon-write` / `scribble`)**:
   - Font / Vector: `Instrument Serif` / Hand-drawn SVG strokes
   - Stroke: `4px` rough crayon texture in `--accent-coral`

---

## 📐 Safe Zones & Layout Rules (9:16 Social Standards)

```
┌──────────────────────────────────────┐  Y = 0px
│ [TOP SAFE MARGIN: 180px]             │  (Avoid IG handle, battery, audio pill)
├──────────────────────────────────────┤  Y = 180px
│                                      │
│  GIANT BEHIND-THE-HEAD WORD (Layer 2)│
│                                      │
│      [ SINGER / SUBJECT ]            │
│      Face Tracking Box [ 1.35x ]     │  Center Safe Area (Y: 300px - 1400px)
│                                      │
│   FROSTED GLASS LYRIC PILL (Layer 4) │
│                                      │
├──────────────────────────────────────┤  Y = 1550px
│ [BOTTOM SAFE MARGIN: 370px]          │  (Avoid Caption box, like/share icons)
└──────────────────────────────────────┘  Y = 1920px
```

---

## ⚡ Motion & Physics Rules (Anime.js & GSAP)

1. **Spring Dynamics**:
   - Lyric pills & UI cards enter with dampened oscillation: `spring(1, 85, 13, 0)`.
   - Never use linear motion for cards.
2. **Kinetic Stagger**:
   - Poetic word reveal: `delay: anime.stagger(40)`.
3. **Transient Punch-Ins**:
   - Guitar downbeats trigger subtle `1.08x` digital camera punch-ins with immediate `300ms` exponential decay.
