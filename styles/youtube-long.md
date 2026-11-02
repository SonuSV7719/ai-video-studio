# Platform Style Guide: YouTube Long-Form

## 1. Technical Canvas
- **Resolution**: `1920 × 1080` (16:9 Landscape Full HD / Master 4K upscale capable)
- **Frame Rate**: `30 fps` (or 60 fps for ultra-smooth UI demos)
- **Video Codec**: H.264 / H.265 (MP4 container, yuv420p)
- **Audio Codec**: AAC, 48 kHz, stereo, 320 kbps

## 2. Structure & Editing Architecture
- **Hook (0:00 – 0:05)**: Deliver the core value thesis or visual teaser within the first 5 seconds before brand intros.
- **Chapter Markers**: Structured into clear thematic segments with on-screen lower third chapter cues and corresponding YouTube timestamp descriptions.
- **Lower Thirds**: Subtle, modern graphic bars introducing speakers, chapters, and topics (`y ≈ 850px – 980px`, left-aligned).
- **End-Screen Card**: Dedicated **20-second outro** section at the tail with visual placeholders for related video elements and subscribe button.

## 3. Deliverables Package
Every long-form YouTube export must produce:
1. `out/<project_name>.mp4`: Master video.
2. `out/<project_name>.srt`: Synchronized subtitle file exported from speech transcript.
3. `out/<project_name>_thumb.png`: High-resolution (1920x1080) still frame extracted for thumbnail design.
4. `out/<project_name>_credits.txt`: Full attribution text block for video description.

## 4. Audio Engineering Standards
- **Master Loudness**: Strict **-14 LUFS** integrated.
- **True Peak**: ≤ **-1.0 dBFS**.
- **Speech Clarity**: High-pass filtered at 80 Hz, vocal presence boost at 2.5–4 kHz.
- **Music Ducking**: Smooth sidechain compression ducking music bed **18 to 22 dB** beneath narration.
- **Attribution**: Full attribution metadata logged in `credits.txt` ready to paste into YouTube description.
