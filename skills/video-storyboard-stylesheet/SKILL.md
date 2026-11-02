---
name: video-storyboard-stylesheet
description: Analyze reference videos to produce a visual storyboard and design stylesheet (colors, typography, motion curves, layouts) for user review before video creation. Enforces the standard 3-folder architecture (raw_footage/, reference/, export/).
argument-hint: "[analyze|storyboard|stylesheet|init] [video-path-or-url]"
metadata:
  author: sonu
  version: "1.0.0"
---

# Video Reference to Storyboard & Stylesheet

Transform any reference video (file or URL) or creative brief into an executive **Storyboard** and **Visual Stylesheet** before writing code or rendering.

## Core Rules

1. **Mandatory 3-Folder Structure**: Every video project workspace MUST maintain:
   - `raw_footage/`: Original unedited camera recordings, A-roll takes, mic audio.
   - `reference/`: Reference reels, competitor videos, style benchmarks, downloaded clips.
   - `export/`: Final rendered video masters, revisions, and distribution files.
2. **Review Gate**: ALWAYS present the visual storyboard and stylesheet to the user for confirmation BEFORE writing Remotion/HyperFrames/GSAP code or rendering.
3. **No Artificial Blur**: Always preserve crisp, natural camera footage with broadcast tone mapping. Never inject artificial blurred masks or blurry halos unless explicitly requested by the user.
4. **Broadcast Audio Consistency**: Always normalize dialogue volume across takes using dynamic audio normalization (`dynaudnorm`).

---

## Workflow Steps

### Step 1: Project Initialization & Asset Staging
Initialize standard folders:
```powershell
mkdir raw_footage, reference, export -Force
```
If given a URL (YouTube, Instagram, TikTok, Twitter/X), download to `reference/` using `yt-dlp`:
```powershell
yt-dlp -f "bv*+ba/b" --merge-output-format mp4 -o "reference/%(title)s.%(ext)s" "<URL>"
```

### Step 2: Scene & Style Analysis (FFmpeg & HyperFrames)
1. **Scene Cut Detection**:
   Extract scene boundary keyframes and timestamps:
   ```powershell
   ffmpeg -i "reference/<ref_video>.mp4" -vf "select='gt(scene,0.3)',showinfo" -vsync vfr "reference/scenes/scene_%03d.jpg"
   ```
2. **Color Palette & Contrast Extraction**:
   Sample dominant color hex codes (background, primary text, accent highlight, borders).
3. **Pacing & Audio Cadence**:
   Measure shot lengths (e.g. 1.5s - 3.5s per cut for high-retention vertical reels).

---

### Step 3: Generate the Visual Stylesheet (`stylesheet.md`)
Create a comprehensive design system spec:
- **Canvas Specification**: Resolution (e.g., `1080x1920` 9:16 vertical), Framerate (`24.000 fps` cinematic CFR).
- **Safe Zones**: Top 150px (Instagram header / user profile), Bottom 350px (captions, audio title, description overlay).
- **Color Palette**:
  - `bg_dark`: `#0d0f12`
  - `accent_primary`: Electric Blue / Neon Lime / Cyberpunk Orange
  - `text_primary`: `#FFFFFF`
  - `text_secondary`: `#94A3B8`
- **Typography**:
  - Headline: Heavy Sans (e.g. `SF Pro Display`, `Inter`, `Montserrat` 800/900 weight, uppercase, tracking `-0.02em`).
  - Subtitle / Captions: High-contrast pill badge with drop shadow (`0 4px 20px rgba(0,0,0,0.6)`).
- **Motion & Easing Physics**:
  - GSAP / Remotion easing curves: `power3.out`, `back.out(1.7)`, spring tension/damping values.
  - Transition styles: Whip-pan, glitch flash, zoom snap, slide cut.

---

### Step 4: Generate the Executive Storyboard (`storyboard.md`)
Structure every scene with exact timing, visual intent, and audio cues:

| Scene # | Timecode / Duration | Visual Layout & Shot Type | On-Screen Graphic / Text | Voiceover / Dialogue | Sound Design & FX |
|---------|---------------------|---------------------------|--------------------------|----------------------|-------------------|
| **01** | `00:00 - 00:03` (72f) | Talking Head (Crisp A-roll, no blur) + Dynamic Headline Pill | `"THE NEW AI BREAKTHROUGH"` | `"Google just quietly dropped something insane."` | Sub-bass riser + Whoosh |
| **02** | `00:03 - 00:07` (96f) | Fullscreen B-roll Demo + Presenter PiP Badge (Bottom-Right) | Fast UI Feature Highlights | `"Notice how it handles continuous world physics..."` | Keyboard clicks + UI pop |
| ... | ... | ... | ... | ... | ... |

---

### Step 5: User Confirmation
Present the generated Storyboard and Stylesheet to the user. Await explicit approval or requested adjustments before proceeding to video generation.
