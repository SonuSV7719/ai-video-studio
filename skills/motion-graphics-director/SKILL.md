---
name: motion-graphics-director
description: Master art direction, aesthetic evaluation, and code generation skill that enforces human agency-grade craft, eliminating all AI-generated looks.
---

# motion-graphics-director

Use this skill whenever generating, reviewing, or refactoring Remotion code, storyboards, and compositions to guarantee studio-grade visual taste.

## 1. Composition Architecture

### Always include the 4-layer stack in every Remotion scene:
1. **Layer 0 (Atmosphere)**: `<Background t={t} glow={glow} />` (drifting dots + ambient vignette + muted glow).
2. **Layer 1 (Texture)**: `<Grain frame={frame} opacity={0.08} />` (procedural `feTurbulence` grain reseeded on twos).
3. **Layer 2 (Graphic Grid)**: Hairline gridlines, technical crosshairs, source citation tags, and monospaced category pills.
4. **Layer 3 (Hero Content)**: High-contrast typography with `<Mask />` reveals, card mockups, and dynamic footage windows.

---

## 2. Typography Rules (The Editorial Difference)
- **Scale Contrast**:
  - Main statement: `fontSize: 72–110px`, `fontWeight: 800`, `letterSpacing: -0.03em`, `lineHeight: 1.05`.
  - Micro-metadata: `fontSize: 16–20px`, `fontFamily: F.mono`, `letterSpacing: 0.20em`, `textTransform: uppercase`.
- **Masking Over Bouncing**:
  - Instead of bouncing entire words into place like CapCut templates, use `<Mask k={progress} tilt={3}>` so words cleanly rise out of an invisible razor line.
- **Single Accent Rule**:
  - Highlight only ONE word or phrase per sequence in the semantic accent color (`C.accent`).

---

## 3. Kinetic Camera & Pacing
- **Eased Punch-in**: Zoom from `1.0` to `1.14` over 6 frames using `easePunch` or `spring({ damping: 14, stiffness: 180 })` on beat hits.
- **Reading Holds**: Keep text static for at least 1.0s after settling so viewers absorb the message without visual fatigue.
- **Never Dead-Still**: While text holds, background dots drift slowly (`t * 4px`) and grain shimmers, keeping the canvas organically alive.
