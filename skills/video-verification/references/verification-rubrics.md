# Verification Rubrics for Video Archetypes

Use these dynamic criteria when evaluating extracted contact sheets and audio tracks across different project types.

---

## 1. Vertical Short-Form Reels / Shorts (9:16)
* **Visual Safe Margins**:
  - Top `180px` clear of essential titles (reserved for username, follow button, platform audio badge).
  - Bottom `370px` clear of key graphic cards and primary subtitles (reserved for platform caption box, creator handle, music credit, like/share button stack).
  - Right `110px` in the lower half clear of critical callouts (reserved for vertical action bar).
* **Face & Human Subject Inspection**:
  - The speaker's face must remain sharp, optical, and natural (strictly 0% synthetic matting blur or halo glow).
  - Behind-the-head typography must not overlap the speaker's eyes, nose, or mouth at any point during head movement.
* **Typographic Contrast**:
  - High-contrast text: Dark text on light background or pure white text with dark frosted glass pill (`background: rgba(20, 19, 25, 0.75)` with 24px backdrop-blur).
* **Audio Metrics**:
  - Integrated Loudness: `-14.0 LUFS` (+/- 1.0 LU).
  - True Peak: Maximum `-1.0 dBFS` (Zero clipping).

---

## 2. DevTool, CLI & Terminal Demos (16:9 or 9:16)
* **Code & Terminal Legibility**:
  - Code syntax font size must be at least `28px` on vertical reels, `22px` on horizontal 16:9.
  - No terminal cursor clipping at the boundary.
  - Highlighted line bounding box must have at least 8px padding around keywords.
* **Pacing & Keyframe Sync**:
  - Staggered typing speed: 30ms to 50ms per character.
  - UI popups must settle into position within 400ms using natural spring physics.

---

## 3. High-Energy Music Videos & Creative Prompts
* **Transient & Beat Lock**:
  - Visual cuts, camera zooms, and flash frames must fall within 1 frame (41ms at 24fps) of kick drum, snare hit, or vocal onset.
* **Layer Depth & Multiplane**:
  - Background, subject, and foreground text layers must demonstrate clear speed differentials (parallax).
  - Ember particles or dust motes must move smoothly without sudden teleportation.
