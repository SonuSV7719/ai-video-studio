---
name: video-verification
description: Use when verifying, auditing, and self-correcting rendered video outputs, animations, or reels — teaches the agent to dynamically inspect visual and audio quality, generate frame contact sheets, diagnose defects (margins, occlusion, contrast, sync), and write custom fix code on demand without hardcoding.
---

# 🔍 Video Verification: Autonomous Self-QA & Dynamic Healing Skill

Operate as an exacting **Broadcast Quality Control (QC) Inspector and Lead Technical Director**.

Your prime directive: **NEVER present a video or claim a render is complete without autonomously inspecting the output first.** You must generate visual frame evidence, dynamically evaluate the video against the project's creative requirements, diagnose any visual or auditory defects, write custom fix code on demand, and re-verify until the output is flawless.

---

## 🚫 The Anti-Pattern: Hardcoded Scripts vs Dynamic Reasoning

* **The Wrong Way**: Relying on rigid, hardcoded scripts with static regex or hardcoded thresholds that break across different aspect ratios, styles, and musical tempos.
* **The Agentic Way**: **Reason dynamically from the project's actual requirements (`storyboard.md` and `stylesheet.md`).** Write lightweight, on-demand verification and repair scripts tailored specifically to the project at hand.

---

## 🧭 The 4-Step Autonomous Verification Loop

```
┌────────────────────────────────────────────────────────────────────────┐
│                   THE SELF-VERIFICATION & HEALING LOOP                 │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Sample Keyframes    Extract contact sheets & keyframes at cuts      │
│ 2. Dynamic Inspection  Inspect safe zones, face occlusion, contrast    │
│ 3. Diagnose & Fix Code Generate custom repair code on demand           │
│ 4. Re-Verify & Deliver Confirm fix with new frame proof & report       │
└────────────────────────────────────────────────────────────────────────┘
```

---

## Step 1: Generate Visual Proof (On-Demand Frame Extraction)

Immediately after any video render, write a quick, dynamic Python snippet or FFmpeg call to extract:
1. **Scene Keyframe Stills**: Exactly at the midpoint or peak moment of each storyboard scene.
2. **Master Contact Sheet Grid**: A single composite image (e.g. 2x3 or 3x3) showing the entire visual arc at a glance.

```python
# Dynamic snippet pattern: extract key scene timestamps from storyboard
import subprocess, os
from PIL import Image

timestamps = [2.0, 6.5, 11.5, 16.5, 22.0, 27.5] # Tailored to the project's scenes
stills = []
for idx, t in enumerate(timestamps):
    out = f"export/qc_scene_{idx+1}.jpg"
    subprocess.run(f'ffmpeg -y -ss {t} -i export/master.mp4 -frames:v 1 -q:v 2 "{out}"', shell=True)
    stills.append(out)

# Dynamically assemble into a contact sheet grid
# (Arrange into rows and columns based on the number of scenes)
```

---

## Step 2: Dynamic Multi-Domain Inspection Checklist

Evaluate the extracted frames and media streams against these 5 domain audits:

### 1. Social Safe Margin Compliance (9:16 Vertical or 16:9 Landscape)
* **The Check**: Are critical text elements, headlines, or face cutouts dangerously close to platform UI overlays?
  - Vertical 9:16: Check top `180px` (profile name, audio pill) and bottom `370px` (caption container, like/comment icons).
* **Self-Critique Question**: *"Will a TikTok or Instagram overlay cover this subtitle or metric badge?"*

### 2. Layering & Occlusion (Behind-The-Head & Cutouts)
* **The Check**: When using 51 video effects (`backdrop-word`, `orbit`, `spotlight`), is text properly occluded *behind* the subject's head, or did segmentation glitch and draw text over the speaker's eyes/nose?
* **Self-Critique Question**: *"Is the speaker's face 100% natural and clean, with typography sitting convincingly in 3D space behind them?"*

### 3. Typographic Contrast & Readability (WCAG AAA)
* **The Check**: Does the lyric text or caption pill have sufficient luminance contrast against the moving background?
* **Self-Critique Question**: *"Can this text be read in 0.5 seconds on a small phone screen in bright sunlight?"*

### 4. Audio Loudness & Dynamic Ceiling (EBU R128)
* **The Check**: Run a quick programmatic `ebur128` check using `ffprobe`/`ffmpeg`.
  - Integrated Loudness: Target `-14.0 LUFS` to `-16.0 LUFS`.
  - True Peak Ceiling: Must NOT exceed `-1.0 dBFS` (avoids DAC inter-sample distortion upon mobile playback).
* **Self-Critique Question**: *"Is speech clear and level across scenes, or does a music drop cause digital clipping?"*

### 5. Motion Continuity & Freeze Bugs
* **The Check**: Scan for accidental frozen frames (such as Remotion's `<OffthreadVideo startFrom={T}>` double-offset bug where video freezes at clip end).
* **Self-Critique Question**: *"Does the motion stay active and organic across every transition, with zero dropped frames or black flashes?"*

---

## Step 3: Dynamic Self-Healing (On-Demand Code Generation)

If ANY defect is detected, **do not wait for the user to report it.** Diagnose the root cause and generate a targeted, custom script to fix it:

### Scenario A: Audio True-Peak or Clipping Detected
* **Dynamic Action**: Generate an on-demand FFmpeg filter script applying an inter-sample peak limiter (`alimiter=limit=-1.0dB:level=false`) and re-stream copy the video track without re-rendering:
  ```bash
  ffmpeg -i master.mp4 -c:v copy -af "alimiter=limit=-1.0dB:level=false" -c:a aac -b:a 192k fixed_master.mp4
  ```

### Scenario B: Text Colliding with Bottom Platform UI
* **Dynamic Action**: In the render script or Remotion composition, adjust the Y-coordinate of the subtitle container (e.g. shift from `Y = HEIGHT * 0.85` up to `Y = HEIGHT * 0.74`).

### Scenario C: Behind-The-Head Mask Bleed Over Hair/Face
* **Dynamic Action**: Adjust the MediaPipe alpha threshold or feathering kernel (e.g. increase Gaussian blur from `(7, 7)` to `(15, 15)` and apply slight dilation to expand the person mask over flyaway hair).

### Scenario D: Video Playback Freezing at Clip End (Remotion Clock Bug)
* **Dynamic Action**: Check `<Sequence from={T}>` and remove child `startFrom={T}` attributes to restore local sequence time.

---

## Step 4: Re-Verify and Deliver with Evidence

1. Re-render the affected section or master.
2. Re-extract keyframe stills and confirm the defect is gone.
3. Present the user with:
   - The master video link.
   - The embedded contact sheet image.
   - An honest inspection summary of what was audited and any auto-corrections applied.

---

## 📚 Supporting References
- [references/verification-rubrics.md](references/verification-rubrics.md) — Exact audit criteria for talking-head reels, explainers, and music videos.
- [references/dynamic-self-healing-recipes.md](references/dynamic-self-healing-recipes.md) — Dynamic code patterns for repairing audio, masks, easings, and margins on the fly.
