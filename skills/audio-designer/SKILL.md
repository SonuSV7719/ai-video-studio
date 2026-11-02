---
name: audio-designer
description: Sound design, beat-syncing, music ducking, and -14 LUFS audio mastering engine.
---

# audio-designer

Use this skill whenever selecting, editing, synchronizing, or mastering audio tracks and sound effects.

## 1. Track Selection & Beat-Grid Synchronization
- **Strict Index Policy**: Choose music ONLY from `assets/audio-index.json` matched by desired `mood`, `BPM`, and duration. Never introduce audio files not logged in the index.
- **Beat Grid Alignment**: Calculate frame timing from the track's BPM (`frames_per_beat = (60 / BPM) * fps`). Snap visual cuts, punch-in zooms, and title reveals precisely onto beat grid divisions.
- **Transitions & Fades**: Standard fade-in of 0.5s and fade-out of 1.0s on music beds.

## 2. Dynamic Voice Ducking
- When narration or dialogue is active, smoothly duck the background music by **18 to 22 dB** (reducing music gain to approx 0.08–0.12).
- Apply smooth 200ms easing curves on ducking attack and release to prevent pumping artifacts.

## 3. SFX Placement Rules
- Keep SFX **sparse, clean, and subtle**:
  - `whoosh`: Under fast transitions, whips, and card slides.
  - `hit`: On bold kinetic text punches and impactful title arrivals.
  - `ui`: Tactile clicks/pops on interface icons, pills, and toggles.
  - `riser`: Building suspense into major reveals.
- **Density Limit**: Never exceed approximately 1 SFX per 2 seconds. Never allow SFX frequencies to mask spoken dialogue.

## 4. Mastering & Legal Compliance
- Render master mix to integrated **-14 LUFS** (true peak ≤ -1.0 dBFS).
- For every track marked `attribution_required: true`, append the required credit text into `out/credits.txt`.
