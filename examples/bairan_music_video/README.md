# Case Study: Bairan Surreal Multiplane Motion Collage

This directory contains the production-grade implementation of **Bairan**, a 2.5-minute animated music video produced entirely with **AI Video Studio** following the strict studio directives.

---

## 🎬 Project Overview

- **Song**: Bairan (by Banjaare)
- **Audio Length**: `02:30.38` (150.38s | 3,609 frames @ 24.000 fps CFR)
- **Format**: 1080p Full HD Widescreen (`1920x1080`)
- **Aesthetic**: Surreal Multiplane Motion Collage (`paper-popup` + `kino-montage` + `archive-lighttable`)

---

## 📁 Files Included

| File | Purpose |
| :--- | :--- |
| [`storyboard.md`](storyboard.md) | Scene-by-scene card breakdown with timings, camera movements, text overlays, and audio cues |
| [`stylesheet.md`](stylesheet.md) | Visual design tokens, color palette (`#C9182B`, `#E8C172`, `#142236`), typography, and motion easing specs |
| [`render_bairan_motion_collage.py`](render_bairan_motion_collage.py) | Complete Python + OpenCV + FFmpeg rendering engine with procedural particle physics, spring polaroids, and 92 BPM heartbeat pulse |

---

## 🌟 Key Motion Graphics Techniques Demonstrated

1. **Parting Curtains & 3D Cloud Title (Scene 1)**:
   - Curved hair borders that smoothly part outward on spring curves as opening guitar chords play.
   - 3D extruded golden Devanagari and Urdu calligraphy on a drifting cloud.

2. **Multiplane Polaroid Physics (Scene 2)**:
   - Polaroid cutout of bridal feet with red Alta dye and golden payal anklets sliding into frame with realistic 3D paper drop shadows (`filter: drop-shadow(12px 18px 24px rgba(0,0,0,0.55))`).
   - Floating violet magical tear dust motes (`#8A5CF6`) rising from the subject's cheek.

3. **Beat-Synchronized Heartbeat Dynamics (Scene 3)**:
   - 3D anatomical ruby crystal heart animated with an authentic double-thump systolic bounce equation:
     $$\text{pulse}(t) = \max(0, \sin(t \cdot \omega))^{14} + 0.45 \cdot \max(0, \sin(t \cdot \omega + 0.35))^{12}$$
   - Concentric crimson energy ripples expanding outward on downbeats.

4. **Exponential Macro Eye Portal Crash Zoom (Scene 4)**:
   - Macro human eye where camera exponentially dives straight into the pupil (`scale: 1.0 -> 7.5x`), revealing a torn-paper stormy ocean horizon within the iris.

5. **Illuminated Devanagari Hindi Kinetic Lyrics**:
   - Two-pass text compositing: dark amber drop shadow outline + golden-leaf metallic fill synchronized to the vocal phrases.

---

## 🚀 How to Run

```bash
# 1. Place bairan_audio.mp3 into raw_footage/
# 2. Execute the master renderer
python render_bairan_motion_collage.py

# 3. Inspect generated contact sheets
python ../../tools/contact_sheet.py export/bairan_music_video_master.mp4 --out export/
```
