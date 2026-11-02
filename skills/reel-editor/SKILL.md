---
name: reel-editor
description: Professional vertical short-form editing engine for Instagram Reels, YouTube Shorts, and TikTok.
---

# reel-editor

Use this skill whenever crafting high-retention 9:16 short-form video content from talking-head clips, screencasts, or product announcements.

## 1. Audio-First Editing Pipeline
1. **Transcription & Boundary Detection**:
   - Run `whisper.cpp` (`whisper-cli.exe -m ggml-base.bin -f <audio_16k.wav> --output-json`) to produce millisecond word timestamps.
   - Detect speech pauses and dead air (>0.4s). Slice timeline strictly at speech boundaries.
   - Strip filler words ("um", "uh", "like", dead pauses) for crisp, relentless forward momentum.
2. **Visual Pacing & Punch-In Zooms**:
   - Insert punch-in scale transitions (1.12x–1.18x) on major emphasis keywords or topic transitions every 2–3 seconds.
   - Overlay B-roll / demo footage directly above relevant spoken nouns.
   - Tag demo overlays with `"Source: <Author>"` in the safe upper corner (`y: 180px`).
3. **Word-by-Word Kinetic Captions**:
   - Position captions strictly in the **middle third** (`y ≈ 700px – 1250px`).
   - Use high-contrast color pills (e.g., yellow `#facc15` or cyan `#38bdf8` text on dark semi-transparent backing).
   - Word pop-in driven by Remotion spring physics (`damping: 10, stiffness: 200`).
4. **Motion Directives**:
   - Zero linear motion: All scale, position, and opacity changes must use cubic-bezier easing or damped springs.
   - Maintain uniform typography and brand color palettes throughout the composition.
   - Keep on-screen text concise (1 to 4 words per beat).
