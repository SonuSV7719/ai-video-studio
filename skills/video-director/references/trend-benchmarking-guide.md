# Trend Benchmarking & Viral Reference Deconstruction Guide

When producing content that must match the retention and visual aesthetic of viral Instagram Reels, YouTube Shorts, or TikTok videos, follow this rigorous reverse-engineering workflow.

---

## The Philosophy: Do Not Copy, Deconstruct DNA

Never blindly copy a competitor's exact content. Instead, deconstruct their **structural video mechanics**:
1. **Pacing DNA**: Cut velocity, Average Shot Length (ASL), and hook rhythm.
2. **Visual DNA**: Color palette, background luminance, typographic hierarchy, and visual density.
3. **Audio DNA**: Integrated speech loudness, dynamic range (LRA), and Foley timing.
4. **Retention DNA**: Pattern interrupt frequency and placement of behind-the-head graphic elements.

---

## 🛠️ Step-by-Step Benchmarking Pipeline

### 1. Ingest & Automated Deconstruction
Run the studio's automated trend benchmarker on any public URL or downloaded clip:

```bash
# Analyze a YouTube Short or Instagram Reel
python tools/trend_benchmarker.py "https://www.youtube.com/shorts/EXAMPLE_ID" --out-dir reference/trending/benchmark_01

# Or analyze a local reference MP4
python tools/trend_benchmarker.py reference/benchmarks/competitor_reel.mp4 --out-dir reference/trending/benchmark_01
```

### 2. Inspecting the Generated Artifacts

The tool produces four critical outputs in `reference/trending/<slug>/`:

```
reference/trending/benchmark_01/
├── frames/                      # High-res stills sampled at hook timestamps (0.5s, 1.5s, 3.0s...)
├── meta.json                    # Video metadata, creator info, view counts, tags
├── style_benchmark.json         # Raw metrics: ASL, cuts, LUFS, dominant colors
└── benchmark_report.md          # Comprehensive executive reverse-engineering report
```

### 3. Evaluating Pacing & Cut Velocity (ASL)

Open `benchmark_report.md` and check the **Average Shot Length (ASL)**:

| ASL Range | Category | Editing Strategy to Deploy |
| :--- | :--- | :--- |
| **0.8s – 1.4s** | Hyper-Retention | Jump-cut on every breath. Use punch-ins (`1.15x` -> `1.35x` digital zooms). Insert B-roll or kinetic text over every 3rd word. |
| **1.5s – 2.4s** | Tech / Creator Reel | Clean talking-head with behind-the-head text drops (`backdrop-word`) every 2 seconds. Translucent UI cards (`liquid-glass-graph`) for statistics. |
| **2.5s – 4.0s** | Explainer / Narrative | Deliberate framing. Cut on action. Use split-screens (`broll-split`) and highlighter callouts (`article-highlights`). |
| **4.0s+** | Thought Leadership | Cinematic, uninterrupted camera takes. Elevate with atmospheric sound design and lighting drops (`spotlight`). |

### 4. Hook Mechanics (0.0s – 3.0s)
Inspect the generated frames in `frames/`:
- **Frame 0 (0.5s)**: What is visible on screen in the first half-second?
  - Is there a giant bold text keyword behind the speaker?
  - Is there an unusual visual prop or striking contrast?
- **Frame 1 (1.5s)**: Does the shot punch in or does a graphic pop up?
- **Rule of Thumb**: If the reference has `≥ 1 cut` in the first 3 seconds, replicate that exact transition timing in your `storyboard.md`.

### 5. Color Palette Extraction
`style_benchmark.json` extracts the top 5 dominant colors. Incorporate them directly into your project's `stylesheet.md`:

```markdown
## Color Tokens (Benchmarked from Reference)
- Primary Background: `#0E0E12` (Deep Charcoal)
- Text Color: `#FFFFFF` (Pure Crisp White)
- Primary Accent: `#FF3B30` (Electric Coral Red)
- Secondary Accent: `#007AFF` (Tech Blue)
- Muted Grey: `#8E8E93` (HUD / Subtitles)
```

### 6. Video Effects Mapping
Match the visual cues observed in the benchmark frames to the corresponding 51 built-in video effects:

| What You See in the Reference Reel | Corresponding Video Effect in Studio |
| :--- | :--- |
| Giant serif/bold word drops behind the speaker | `backdrop-word` (`--text "KEYWORD"`) |
| Camera smoothly tracks the speaker's face with corner brackets | `locked-on` (`--opt zoom=1.35`) |
| Lights dim dramatically while speaker stays illuminated | `spotlight` (`--text "THE TRUTH"`) |
| Screenshots / reels circling 3D around speaker's head | `orbit` (`--images reference/takes/`) |
| Translucent glass card displaying a climbing graph | `liquid-glass-graph` (`--text "+350%"`) |
| iPhone settings toggles flipping on sequentially | `apple-toggles` |
| Floating frosted glass cards & Claude pill | `glass-widgets` |
| Fast punch-in on an emphatic word | `lean-in` (`--opt zoom=1.45`) |
| Handwritten red crayon underline | `crayon-write` (`--text "MISTAKE"`) |

---

## 📋 Pre-Production Checklist Before Rendering

- [ ] Has the reference been downloaded and benchmarked via `trend_benchmarker.py`?
- [ ] Have the measured ASL and hook cuts been transferred to `storyboard.md`?
- [ ] Has `stylesheet.md` adopted the benchmarked color tokens and typography?
- [ ] Has an interactive preview deck been generated with `generate_interactive_storyboard.py`?
- [ ] Has the user signed off on the storyboard and stylesheet?
