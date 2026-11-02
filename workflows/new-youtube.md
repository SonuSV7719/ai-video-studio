# /new-youtube Workflow

**Description**: Intake and production pipeline for 16:9 landscape YouTube long-form videos with chapter markers, lower thirds, end-screen card, .srt subtitle export, and thumbnail frame capture.

---

## Workflow Steps

1. **Intake & Planning**:
   - Ask for: Topic, raw footage files, outline/PDD, target runtime, chapter milestones.
   - Establish storyboard: 5-second hook, chapter breaks, demonstration blocks, 20-second outro.
2. **Audio-Driven Editorial**:
   - Transcribe narration using `whisper-cli.exe`.
   - Trim silences and map out chapter timestamps.
   - Export synchronized `.srt` subtitle file to `out/<title>.srt`.
3. **Landscape Motion Graphics**:
   - Configure Remotion composition with `YouTubeComp` (1920×1080, 30 fps).
   - Render chapter lower-third banners during scene transitions.
   - Design 20-second interactive end-screen card with placeholder boxes for cards/subscribe.
4. **Master Audio Mix**:
   - Query `assets/audio-index.json` for cinematic/tech music bed.
   - Smooth ducking (18–22 dB) beneath speaker speech.
   - Master to integrated -14 LUFS (true peak ≤ -1.0 dBFS).
5. **Quality Check & Full Release Package**:
   - Render video: `out/<title>.mp4`.
   - Extract uncompressed 1920x1080 thumbnail frame: `out/<title>_thumb.png`.
   - Generate `out/<title>_credits.txt` with full attribution.
   - Verify with `/quality-check` and report results.
