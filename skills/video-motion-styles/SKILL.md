---
name: video-motion-styles
description: Complete taxonomy and technical implementation specifications for the world's premier motion graphics styles (Editorial Documentary, Swiss Kinetic Typography, Silicon Valley Tech Minimalist, Acid Brutalist, Analog Film).
---

# Video Motion Graphics Creation Styles

Use this skill whenever choosing, directing, or styling motion graphics compositions to ensure they look crafted by world-class human designers (Ordinary Folk, Pentagram, Buck, Apple, Vox) and avoid generic "AI-generated" looks.

---

## 1. Style Archetypes & Technical Recipes

### Style A: The High-End Editorial Documentary (Vox / Johnny Harris / Polymatter)
- **Vibe**: Investigative journalism, intellectual depth, tactile archival credibility.
- **Palette**: Deep charcoal `#121212`, warm raw paper `#f4f1ea`, highlighter yellow `#ffd000` or marker red `#e63946`, muted graphite lines `rgba(244,241,234,0.14)`.
- **Typography**: 
  - Display: Elegant editorial serif (`Instrument Serif` or `Playfair Display`) paired with condensed bold sans (`Barlow Condensed` or `Oswald`).
  - Metadata: Strict monospaced timestamps, coordinates, and source citations (`JetBrains Mono`, `letterSpacing: 0.15em`, `textTransform: uppercase`).
- **Tactile Texture**:
  - Procedural film grain overlay (`<Grain opacity={0.08} />`).
  - Authentic marker highlight animation (`width: 0% → 100%` behind key phrases).
  - 2.5D parallax photo cutouts sliding against subtle topographic gridlines.
- **Sound Design**: Real paper rustle, mechanical camera shutters, typewriter clacks, subtle low-frequency atmospheric hums.

---

### Style B: Swiss Kinetic Typography & Asymmetric Modernism (Pentagram / Bauhaus)
- **Vibe**: Bold, authoritative, graphic-design-first, uncompromisingly clean.
- **Palette**: High-contrast black `#080808` & bone white `#ffffff`, with a single explosive accent (Safety Orange `#ff5c00` or International Klein Blue `#002fa7`).
- **Typography**:
  - Clean grotesque sans (`Inter`, `Helvetica Neue`, `Neue Haas Grotesk`) at extreme hierarchy scale differences (e.g., 140px title with 14px uppercase label).
  - Tight negative tracking (`letterSpacing: -0.03em`) on display headlines.
- **Motion Dynamics**:
  - Masked word reveals: Words slide up from beneath an `overflow: hidden` bounding box with a 4° rotational tilt (`<Mask k={p} tilt={4}>`).
  - Rigid typographic grid with hairline borders (`1px solid rgba(255,255,255,0.15)`).
  - Staggered word pops aligned precisely to beat drops.

---

### Style C: Silicon Valley Tech Minimalism (Apple / Stripe / Linear / Vercel)
- **Vibe**: Hyper-refined, frictionless, precision-engineered, ultra-modern SaaS/Hardware.
- **Palette**: Obsidian `#0c0d0e`, Slate `#1e2023`, Frosted White borders `rgba(255, 255, 255, 0.10)`, Electric Cyan `#00f0ff` or Emerald `#10b981`.
- **Visual Primitives**:
  - Glassmorphic card containers with gradient border lighting (`backdropFilter: blur(24px)`).
  - Drifting dot matrix background with feathered radial vignette (`<Background />`).
  - Micro-metric badges (e.g. `[ REAL-TIME • 30 FPS • NATIVE ]`).
- **Spring Physics**:
  - Heavy, calm settles (`damping: 18, stiffness: 140, mass: 0.8`).
  - Knobs and toggles snapping into place (`damping: 12, stiffness: 200`).
- **Sound Design**: Tactile glass taps, subtle UI frequency clicks, low-end sub drops on scene reveals.

---

### Style D: Acid Brutalist & Cyberpunk FUI (Future Interfaces)
- **Vibe**: Raw, high-energy, digital-native, technical.
- **Palette**: Pitch black `#000000`, Acid Lime `#d4ff00`, Hazard Yellow `#ffea00`, Glitch Magenta `#ff0055`.
- **Visual Primitives**:
  - Wireframe bounding boxes, crosshair markers (`+ + +`), technical corner brackets.
  - High-velocity typographic cuts, quick 1-frame strobe flash on impact beats.
  - Subtle chromatic aberration and scanline filters on transitions.

---

## 2. The "Anti-AI Look" Enforcement Protocol
To ensure compositions NEVER look like cheap automated AI generator output:

| AI-Generated Cliche (BANNED) | Human Motion Director Standard (ENFORCED) |
| :--- | :--- |
| Generic purple/blue radial blobs in center | Multi-layered background: drifting dot grid + feathered gradient + real procedural film grain |
| Floating centered yellow pill buttons | Editorial typography hierarchy with monospaced metadata headers and rule lines |
| Uniform, identical bouncy springs on every element | Purposeful physics: heavy panels settle slow (`d:18, s:120`), text snaps quick (`d:10, s:220`) |
| Unmotivated crossfade / generic camera whip | Object continuity: persistent elements morph or travel across scene boundaries |
| Chaotic visual noise with 5 colors | Strict 3-token palette: Background, Primary Text, Single Semantic Accent Color |
| Cheap drop shadows | Diffused ambient glow driven by element state (`boxShadow: 0 20px 40px rgba(0,0,0,0.5)`) |
