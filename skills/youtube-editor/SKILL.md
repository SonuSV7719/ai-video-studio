---
name: youtube-editor
description: Master editing pipeline for 16:9 YouTube long-form videos with chapters, lower thirds, srt subtitles, and thumbnail capture.
---

# youtube-editor

Use this skill when constructing landscape (16:9) YouTube videos following `styles/youtube-long.md`.

## 1. Editorial Structure
1. **The 5-Second Cold Open**: Deliver a dynamic teaser or central thesis before any channel branding.
2. **Pacing & Energy**: Alternate between talking-head, screen-capture, graphical diagrams, and animated typography to sustain engagement.
3. **Chapter Segmentation**:
   - Construct modular narrative blocks (e.g., Intro, Overview, Technical Deep-Dive, Results, Conclusion).
   - Insert animated Lower Third badges on chapter transitions (`y ≈ 850px`).
4. **End-Screen Card**: Design a dedicated 20-second tail layout with visual bounding boxes for recommended videos and subscribe avatars.

## 2. Mandatory Output Package
Always export the complete YouTube release bundle:
- Master video: `out/<project_name>.mp4` (1080p or 4K, -14 LUFS, H.264/AAC)
- Subtitles: `out/<project_name>.srt` (Whisper-extracted timestamps)
- Thumbnail: `out/<project_name>_thumb.png` (High-res uncompressed PNG frame)
- Video Description: `out/<project_name>_desc.txt` (Timestamps + Attribution credits)
