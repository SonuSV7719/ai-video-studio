# Platform Style Guide: Instagram Reel

## 1. Technical Canvas
- **Resolution**: `1080 × 1920` (9:16 Vertical)
- **Frame Rate**: `30 fps` (Strict constant frame rate)
- **Target Duration**: 15–45 seconds (high retention curve)
- **Video Codec**: H.264 (MP4 container, yuv420p, high profile)
- **Audio Codec**: AAC, 48 kHz, stereo, 256 kbps

## 2. Safe Margins & UI Protection
- **Top Zone (0px – 150px)**: Reserved for Instagram navigation, search, and system bars. Keep faces, headers, and text outside this area.
- **Bottom Zone (1670px – 1920px, bottom ~250px)**: Reserved for account handle, sound label, caption snippet, and like/comment/share icons. Never place subtitles, buttons, or legal credits here.
- **Side Margins**: Keep 48px padding on left and right for clean framing on narrow screens.
- **Captions Zone**: Strictly confined to the **middle third** (`y ≈ 700px – 1250px`).

## 3. Pacing & Motion Direction
- **The 1-Second Hook**: High-contrast graphic, bold text pop, or immediate spoken question within the first 30 frames.
- **Visual Rhythm**: A visual cut, camera punch-in (1.15x), B-roll overlay, or kinetic graphic pop every **2 to 3 seconds**.
- **Motion Character**: Eased curves only (`spring({ damping: 12, stiffness: 150 })` or cubic-bezier). No raw linear interpolation.
- **Captions**: Word-by-word animated highlights, bold sans-serif font (Inter/Montserrat/Poppins), high contrast backdrop pill.

## 4. Audio Engineering Standards
- **Master Target Loudness**: **-14 LUFS** integrated.
- **True Peak**: ≤ **-1.0 dBFS**.
- **Voiceover**: Dominant channel, compressed, crisp EQ.
- **Music Bed Ducking**: Automatically ducked **18 to 22 dB** beneath active speech with 200ms smooth ramp.
- **Sound Effects (SFX)**: Subtle whooshes on cuts, tactile clicks/pops on text entrances; never mask dialogue.
- **Licensing**: Only assets with verified commercial rows in `assets/audio-index.json`. Generate `credits.txt` for any attribution requirements.
