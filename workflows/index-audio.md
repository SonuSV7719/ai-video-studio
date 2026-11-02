# /index-audio Workflow

**Description**: Scans the `assets/audio-inbox/` staging folder, validates commercial licenses against `AUDIO_LICENSES.csv`, measures audio metrics (BPM, duration, LUFS), categorizes mood, routes files into library folders, and compiles `assets/audio-index.json`.

---

## Workflow Steps

1. **Scan Execution**:
   - Run the audio indexing script:
     ```bash
     python tools/index_audio.py
     ```
2. **Analysis Performed**:
   - Verifies license entry in `assets/AUDIO_LICENSES.csv`.
   - Rejects any file missing a license row, with `commercial_ok = n`, or with `NC`/`ND` tags.
   - Measures exact duration and integrated LUFS via FFmpeg `ebur128`.
   - Computes BPM tempo and suggests category (`music/<mood>` or `sfx/<type>`).
3. **Library Ingestion**:
   - Moves accepted audio files into `assets/music/` or `assets/sfx/`.
   - Updates `assets/audio-index.json` with structured metadata.
4. **Report**:
   - Reports all accepted files and categorizations.
   - Summarizes any rejected/skipped files with clear explanation of why they were rejected.
