# Visual Stylesheet: Bairan Surreal Multiplane Motion Collage

**Song**: Bairan (by Banjaare)  
**Audio Source**: `raw_footage/bairan_audio.mp3` (Duration: `02:30.39` | 150.4s | 3,610 frames @ 24fps)  
**Reference Video**: `reference/bairan_reference.mp4` (Official Bairan Mixed-Media Music Video)  
**Style Architecture**: **Surrealistic Multiplane Paper Collage & Motion Graphics** (`paper-popup` + `kino-montage` + `archive-lighttable`)

---

## 1. Canvas & Motion System Specifications

| Metric | Specification | Technical Rationale |
| :--- | :--- | :--- |
| **Resolution** | `1920 x 1080` (16:9 Landscape Master) | Cinematic widescreen canvas |
| **Framerate** | `24.000 fps` Constant Frame Rate (CFR) | Organic filmic stop-motion/motion graphic cadence |
| **Motion Model** | Multiplane 2.5D Layered Parallax | Depth layers (Foreground Cutouts → Midground Action → Background Texture) |
| **Shadow Model** | Physical Cast Drop Shadows | `filter: drop-shadow(12px 18px 24px rgba(0,0,0,0.55))` |
| **Heartbeat Dynamics** | Double-Thump Systolic Pulse | `scale(t) = 1.0 + 0.14 * (sin(t * freq)^12 + 0.5 * sin(t * freq + 0.3)^12)` |
| **Transition System** | Torn Paper Wipes & Eye Pupil Portal Zooms | Seamless surrealist thematic bridges between scenes |

---

## 2. Color Palette Tokens

```
┌────────────────────────────────────────────────────────────────────────┐
│                        BAIRAN COLOR TOKENS                             │
├───────────────┬───────────┬────────────────────────────────────────────┤
│ ruby-heart    │ #C9182B   │ Anatomical ruby crystal heart, emotional   │
│               │           │ pulse, romantic bloodline energy           │
├───────────────┼───────────┼────────────────────────────────────────────┤
│ gold-foil     │ #E8C172   │ 3D extruded title "बैरण", payal anklets,   │
│               │           │ glowing Hindi typography text              │
├───────────────┼───────────┼────────────────────────────────────────────┤
│ deep-ocean    │ #142236   │ Tempestuous sea, night sky, silhouette base│
├───────────────┼───────────┼────────────────────────────────────────────┤
│ alta-red      │ #D82626   │ Traditional bridal feet dye, passion       │
├───────────────┼───────────┼────────────────────────────────────────────┤
│ paper-torn    │ #F7F3E9   │ Cream cardboard cutout edges & polaroids   │
├───────────────┼───────────┼────────────────────────────────────────────┤
│ tear-violet   │ #8A5CF6   │ Luminous magical particle tears & cosmos   │
└───────────────┴───────────┴────────────────────────────────────────────┤
```

---

## 3. Typography & Kinetic Lyrics Specification

- **Primary 3D Extruded Title**:
  - `Rozha One` / `Noto Serif Devanagari` (Weight: 900, extruded depth `+8px`, golden-leaf gradient `#FDE68A` -> `#D97706`, dark amber drop shadow).
- **Secondary Urdu Script Title**:
  - `Noto Naskh Arabic` / `Gulzar` ("بیرن", floating underneath cloud).
- **Kinetic Lyrics Hierarchy**:
  - Font: `Nirmala UI Bold` / `Cinzel Decorative`
  - Style: Golden illuminated text with 2px dark brown outline (`rgba(30,15,5,0.85)`), pop-in on vocal attack, glowing ember shimmer.
  - Safe Margins: 120px from bottom edge (90% action safe zone).

---

## 4. Layer Architecture & Motion Graphics Grammar

```
Layer 4 [HUD / Typography]     : Golden Devanagari lyrics + Urdu script + Title cards
Layer 3 [Foreground Cutouts]   : Crying girl profile, boy sleeping, wavy hair borders
Layer 2 [Dynamic Action / Hero]: Pulsing Ruby Heart, Polaroid photo slides, Eye Portal
Layer 1 [Midground Landscape]  : Torn paper ocean, rolling sunset hills, balcony pillars
Layer 0 [Background Sky]       : Drifting cloud volume, starry Milky Way, stormy waves
```

---

## 5. Visual Hooks & Easing Curves

1. **3-Second Hook Gate**: Opening frame features curly hair framing silhouetted borders, parting like a theatrical curtain to reveal the golden cloud title.
2. **Beat-Synchronized Motion**:
   - Dholak / Kick Drops: Radial camera shake (`intensity: 4px`, decay `0.15s`).
   - Ruby Heart: Exponential spring scale thump synchronized to the 92 BPM rhythm.
   - Eye Portal: Exponential crash zoom (`ease: expo.inOut`, `scale: 1.0 -> 8.5`) diving into the iris.
