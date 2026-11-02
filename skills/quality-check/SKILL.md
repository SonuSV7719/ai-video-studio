---
name: quality-check
description: Mandatory pre-delivery verification suite. Validates visual safety zones, audio LUFS, text accuracy, and asset licensing before client review.
---

# quality-check

Execute this verification suite before EVERY client delivery. Any detected flaw must be repaired prior to presenting the render.

## 1. Frame Extraction & Visual Inspection
- Execute test render to `out/<video_name>.mp4`.
- Extract still sample frames using FFmpeg:
  - Start frame (`t = 1.0s`)
  - Midpoint frame (`t = duration / 2`)
  - End frame (`t = duration - 1.0s`)
  - Every major kinetic text / B-roll transition point
- **Visual Checklist**:
  - [ ] Are captions strictly within the middle third?
  - [ ] Is text kept outside top 150px and bottom 250px safe zones?
  - [ ] Zero text truncation or horizontal overflow beyond canvas edges.
  - [ ] Zero black frames, frozen video renders, or flash glitches.
  - [ ] Spelling, capitalization, and grammar verified against source facts.

## 2. Audio & Loudness Verification
- Run FFmpeg `ebur128` filter to measure master output audio:
  - [ ] Integrated loudness is approximately **-14 LUFS** (±1.0 LUFS tolerance).
  - [ ] True peak does not exceed **-1.0 dBFS** (zero digital clipping).
  - [ ] Background music is cleanly ducked under spoken dialogue.

## 3. Legal & Manifest Verification
- [ ] Every included music and SFX file has a corresponding row in `assets/audio-index.json`.
- [ ] `credits.txt` exists and lists full attribution text for any attribution-required assets.

## 4. Delivery Format
Always provide the director with the detailed checklist table, measured metrics, and extracted frame preview paths. Never respond with a simple "done".
