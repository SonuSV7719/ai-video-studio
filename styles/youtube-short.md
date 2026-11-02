# Platform Style Guide: YouTube Short

## 1. Technical Canvas
- **Resolution**: `1080 × 1920` (9:16 Vertical)
- **Frame Rate**: `30 fps`
- **Duration Constraint**: Strictly under **60 seconds** (recommended 30–50s for peak algorithm looping)
- **Video Codec**: H.264 (MP4 container, yuv420p, high profile)
- **Audio Codec**: AAC, 48 kHz, stereo, 256 kbps

## 2. Safe Margins & UI Protection
- **Top Zone (0px – 150px)**: YouTube Shorts search and camera header.
- **Bottom Zone (1670px – 1920px, bottom ~250px)**: Channel avatar, subscribe pill, sound wave, title overlay.
- **Right Edge Buffer (approx 120px from right in bottom half)**: Reserved for Like, Dislike, Comments, Share stack.
- **Captions Placement**: Middle third (`y ≈ 700px – 1250px`), centered horizontally.

## 3. Pacing & Motion Direction
- **Hook Strategy**: First frame visual impact. Question or provocative insight in frame 0–30.
- **Pacing**: Fast cut rate; punch-in scale shifts (1.0x to 1.15x) on key emphasis nouns/verbs.
- **Graphic Overlays**: Third-party demos must display a discreet, high-contrast `"Source: ..."` tag anchored at safe top-left (`x: 60px, y: 180px`).
- **Loop Seamlessness**: Plan the final 1.5 seconds to seamlessly loop back into the first sentence whenever feasible.

## 4. Audio Engineering Standards
- **Master Loudness**: **-14 LUFS** (true peak ≤ -1.0 dBFS).
- **Music Ducking**: Music bed ducked **18 to 22 dB** beneath voice with clean attack and release.
- **Asset Compliance**: 100% free assets verified in `assets/audio-index.json`. Include attribution credit in upload description.
