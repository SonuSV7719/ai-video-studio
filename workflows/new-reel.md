# /new-reel Workflow

**Description**: Interactive intake and automated production pipeline for 9:16 vertical short-form reels (Instagram Reels, YouTube Shorts, TikTok).

---

## Workflow Steps

1. **Intake & Briefing**:
   - Request from the director:
     - Topic / core message
     - Raw talking-head video/audio clip(s)
     - Demo / B-roll footage (if applicable)
     - Desired target length (typically 20–45s) and tone (tech, upbeat, dramatic)
2. **Audio Transcription & Cut Planning**:
   - Extract audio track to 16 kHz WAV:
     `ffmpeg -i <clip> -ar 16000 -ac 1 -c:a pcm_s16le <audio_16k>.wav`
   - Run Whisper (`whisper-cli.exe`) to generate word timestamps.
   - Remove dead air, silence gaps, and verbal filler words.
3. **Motion Graphics & Caption Generation**:
   - Configure Remotion composition with `ReelComp` (1080×1920, 30 fps).
   - Place animated captions in the middle third (`y: 700px–1250px`).
   - Add punch-in zooms (1.15x) on key emphasis terms.
   - Insert B-roll demo clips with `"Source: <Author>"` lower third tags.
4. **Sound Design & Ducking**:
   - Select tech/upbeat track from `assets/audio-index.json`.
   - Align cuts to BPM beat grid.
   - Apply 18–22 dB ducking under dialogue.
   - Add subtle whoosh on transitions and click on text pops.
5. **Quality Check & Delivery**:
   - Render to `out/<reel_name>.mp4`.
   - Run `/quality-check` checklist (safe zones, -14 LUFS, licensing, no typos).
   - Extract sample frames at start, middle, and end.
   - Generate `out/<reel_name>_captions_hashtags.txt`.
   - Present checklist, sample frames, and final MP4 path to director.
