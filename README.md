<div align="center">

# 🎬 AI Video Studio

**The Programmatic, Agentic Video Production Engine & Style System**  
*Code-driven motion graphics, terminal-native product demos, cinematic reels, and broadcast audio mastering — 100% local, reproducible, and review-gated.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Node: >=20](https://img.shields.io/badge/Node.js-%3E%3D20-green.svg?style=flat-square)](https://nodejs.org/)
[![Python: >=3.11](https://img.shields.io/badge/Python-%3E%3D3.11-3776AB.svg?style=flat-square&logo=python&logoColor=white)](https://python.org/)
[![Remotion](https://img.shields.io/badge/Remotion-React%20Video-61DAFB.svg?style=flat-square)](https://remotion.dev)
[![HyperFrames](https://img.shields.io/badge/HyperFrames-v0.8.223-ff8a3d.svg?style=flat-square)](https://github.com/heygen-com/hyperframes)
[![Anime.js](https://img.shields.io/badge/Anime.js-Motion%20Engine-F64F59.svg?style=flat-square)](https://animejs.com/)
[![VoiceStudio](https://img.shields.io/badge/VoiceStudio-Local%20TTS%20%26%20Clone-993f61.svg?style=flat-square)](https://voicestudio.sh/)
[![Earshot](https://img.shields.io/badge/Earshot-AI%20Audio%20Ears-8A2BE2.svg?style=flat-square)](https://github.com/Leonxlnx/earshot)
[![Openverse](https://img.shields.io/badge/Openverse-800M%2B%20CC%20Media-006699.svg?style=flat-square)](https://openverse.org)

[**Quick Start**](#-quick-start) • [**The 3 Golden Rules**](#-the-3-mandatory-golden-rules) • [**Interactive Storyboard**](#-interactive-visual-storyboard-engine) • [**66 Film Styles**](#-style-atlas--66-film-styles-catalog) • [**VoiceStudio**](#-local-ai-voice-cloning--dubbing-voicestudio)

</div>

---

## 🌟 What is AI Video Studio?

AI Video Studio is a production-grade framework that turns AI coding agents (Claude, Gemini, Antigravity, Cursor, Windsurf) into **Senior Motion Graphics Directors & Video Editors**.

Instead of hallucinating random cuts, messy timelines, or bad audio dips, AI Video Studio enforces **strict broadcast standards**, **disciplined folder architecture**, and a **mandatory pre-production review gate** so creators review and approve visual storyboards and design stylesheets *before* a single frame is rendered.

---

## 🛡️ The 3 Mandatory Golden Rules

Every video project managed by AI Video Studio strictly adheres to three non-negotiable directives:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        AI VIDEO STUDIO WORKFLOW                        │
├────────────────────┬───────────────────────────────────────────────────┤
│ 1. 3-Folder Setup  │ raw_footage/   reference/   export/               │
│ 2. Review Gate     │ stylesheet.md  storyboard.md  (Sign-Off Required) │
│ 3. Zero Blur       │ 100% Crisp Natural Optical Camera + Mobius Curve  │
│ 4. Loudness Standard│ dynaudnorm=f=150:g=15:p=0.95 (Constant -14 LUFS) │
└────────────────────┴───────────────────────────────────────────────────┘
```

1. **Mandatory 3-Folder Architecture**:
   - `raw_footage/`: Clean microphone WAVs, raw camera takes (`.MOV`/`.MP4`), original screencasts.
   - `reference/`: Benchmark reels, competitor videos, downloaded YouTube/TikTok clips (via `yt-dlp`).
   - `export/`: Interactive HTML storyboard decks, revision cuts, rendered final masters.
2. **Pre-Production Review Gate (Storyboard & Stylesheet First)**:
   - **NEVER** render a video without first presenting the user with:
     - `stylesheet.md`: Colors, typography, safe margins, and easing curves.
     - `storyboard.md`: Scene-by-scene card breakdown with timestamps, shot types, text overlays, and audio cues.
     - `storyboard_interactive.html`: A clickable, interactive visual deck.
   - Requires explicit human approval before video code or rendering commences.
3. **Natural Camera Clarity (Strictly 0% Synthetic Blur)**:
   - Real camera footage is rendered with 100% natural optical sharpness.
   - No synthetic oval background blur, AI matting blur, or halo cutouts.
   - Broadcast studio tone mapping applied via Mobius curve (`tonemap=mobius:param=0.3:npl=1000`).

---

## ⚡ Quick Start

### 1-Command Automated Installation

#### Windows (PowerShell)
```powershell
git clone https://github.com/SonuSV7719/ai-video-studio.git
cd ai-video-studio
.\setup.ps1
```

#### macOS / Linux
```bash
git clone https://github.com/SonuSV7719/ai-video-studio.git
cd ai-video-studio
chmod +x setup.sh
./setup.sh
```

---

## 🖥️ Interactive Visual Storyboard Engine

AI Video Studio includes an interactive browser-based visual storyboard generator:

```bash
python tools/generate_interactive_storyboard.py [output_path.html]
```

### Features:
* **Interactive Timeline Scrubber**: Clickable scene segments with duration percentages and frame counts.
* **Simulated Viewport Canvas**: Visual mockups with simulated terminal windows, blinking cursors, and telemetry HUD overlays.
* **Synchronized Captions**: Word-level kinetic subtitle previews with active keyword highlights.
* **Visual Color Swatches**: One-click hex copying for design tokens.

---

## 🎨 Style Atlas & 66 Film Styles Catalog

Integrated directly with **Lemo-Opuscar** and **MG-Styles-15**, the studio provides instant access to 66 production-ready film styles and 15 motion graphics archetypes:

| Category | Styles Included | Best For |
| :--- | :--- | :--- |
| **Developer & Tech** | `dark-keynote`, `ascii-crt`, `hologram-hud`, `living-screencast`, `teardown`, `desktop-flythrough` | CLI tools, developer agents, SaaS demos, SDK launch videos. |
| **Editorial & Design** | `swiss-motion`, `silkscreen-poster`, `risograph`, `art-deco`, `blueprint`, `visual-investigation` | Brand stories, technical essays, journalism, architectural breakdowns. |
| **Data & Scientific** | `dataviz`, `iso-infographic`, `satellite-briefing`, `lidar-survey`, `data-physical` | Benchmarks, AI token efficiency, financial charts, infrastructure. |
| **Organic & Cel Animation** | `cel-anime-80s`, `watercolor`, `woodcut`, `crayon-book`, `ink-wash`, `paper-popup` | Metaphors, emotional storytelling, accessible explainers. |
| **Motion Graphics (MG-15)**| `flat-vector`, `line-art`, `isometric`, `3d-render`, `cel-boil`, `liquid`, `morph`, `hud-ui` | High-energy kinetic explainer videos and social-first reels. |

*Full reference index available in [`reference/STYLE_ATLAS.md`](reference/STYLE_ATLAS.md).*

### 🚀 Prompt Motion: 236 Crazy AI Animation Prompts
Integrated catalog from [**Prompt Motion**](https://prompt-motion.com/) with 236 high-impact animation prompts, showreels, kinetic typography setups, and product UI animations. Browse the full index with video previews and prompt recipes in [`reference/PROMPT_MOTION_INDEX.md`](reference/PROMPT_MOTION_INDEX.md).

---

## ⚡ Kinetic Motion & Physics: Anime.js & GSAP

AI Video Studio integrates [**Anime.js**](https://animejs.com/) (`juliangarnier/anime`) and **GSAP** for declarative, code-driven animation:

* **SVG Path Drawing & Handwriting**: Smooth stroke reveals (`strokeDashoffset: [anime.setDashoffset, 0]`).
* **Staggered Kinetic Typography**: Letter-by-letter and word-by-word reveals using `delay: anime.stagger(35)`.
* **Physics & Springs**: Natural physical bounce curves using `easing: 'spring(1, 90, 14, 0)'`.
* **Beating Heartbeat & Pulsing Loops**: Seamless rhythmic timelines mapped to musical beats.
* **Recipes & Presets**: See [`skills/motion-graphics/references/animejs-recipes.md`](skills/motion-graphics/references/animejs-recipes.md) and [`templates/animejs_motion_preset.js`](templates/animejs_motion_preset.js).

---

## 🎙️ Local AI Voice Cloning & Dubbing (VoiceStudio)

For voice generation, voice cloning, and multi-language dubbing, AI Video Studio integrates with [**VoiceStudio**](https://voicestudio.sh/) (`debpalash/VoiceStudio`):

* **100% Local & Private**: No cloud subscriptions, runs entirely on your local machine.
* **646 Languages Supported**: Voice cloning from a 5-second clean reference sample.
* **Video Dubbing**: Translate and dub video tracks with automated timestamp synchronization.

### Install VoiceStudio:
```powershell
# Windows
irm https://voicestudio.sh/install.ps1 | iex

# macOS / Linux
curl -fsSL https://voicestudio.sh/install | sh
```

---

## 👂 Ears for Coding Agents: Earshot & Real-Sound

Integrated directly with [**Earshot**](https://github.com/Leonxlnx/earshot) (`Leonxlnx/earshot`), giving AI agents the ability to hear, analyze, time-align, and critique audio without hallucinating:

* **Auditory Reasoning**: What a file sounds like in words (`earshot describe`), whether it matches a text prompt (`earshot match`), and whether it's pro-recorded or code-synthesized (`earshot realness`).
* **Timeline Auditing**: Generates second-by-second listening transcripts aligned to video cuts (`earshot timeline --video input.mp4`).
* **Sound Synthesis (`earshot sfx` / `earshot forge`)**: 252+ procedural sound effects rendered directly in Python code (whooshes, UI pops, riser hits, clicks).
* **Skills Included**:
  - `skills/earshot/`: Instructions for agentic auditory reasoning and verification.
  - `skills/real-sound/`: Full production workflow for music editing, JSON sound design, license audits, and stem mastering.

---

## 🌐 Open Commons Media Search: Openverse

Integrated with [**Openverse**](https://openverse.org) ([WordPress/openverse](https://github.com/WordPress/openverse)) to search and ingest over 800M+ CC-licensed (Creative Commons / Public Domain) assets:

```bash
# Search and download free audio & music
python tools/openverse_search.py audio "acoustic guitar" --limit 5 --download raw_footage/audio/

# Search and download free textures & stock images
python tools/openverse_search.py images "vintage paper texture" --limit 5 --download reference/
```

* **Commercial & Modification Safe**: Automatically filters for CC0, PDM, and CC-BY compatible media.
* **Resilient Engine**: Queries Openverse REST API with fallback to Wikimedia Commons.

---

## 📂 Repository Structure

```
ai-video-studio/
├── skills/                          # 20 Specialized Video Production & Audio Agent Skills
│   ├── video-storyboard/            # Interactive visual storyboard & shot list generator
│   ├── video-storyboard-stylesheet/ # Reference video analyzer & stylesheet compiler
│   ├── lemo-opuscar/                # 66 code-rendered film styles engine
│   ├── earshot/                     # Ears for coding agents (describe, match, critique sound)
│   ├── real-sound/                  # Pro soundtrack engineering & licensed audio pipeline
│   ├── motion-graphics/             # Remotion & GSAP motion graphics builder
│   ├── motion-graphics-director/    # Creative direction & pacing rules
│   ├── cinematic-camera/            # Camera moves, lens distortion, lighting
│   ├── article-highlights/          # Kinetic highlighter & kinetic text animations
│   ├── asset-finder/                # Autonomous asset harvesting & validation
│   ├── audio-designer/              # SFX placement, ducking, broadcast mastering
│   ├── edit-qa-validator/           # Timeline QC, frame slips, aspect-ratio audits
│   ├── quality-check/               # Visual inspection & safe-margin tests
│   ├── reel-editor/                 # High-velocity 9:16 Shorts/Reels assembly
│   ├── short-form-retention/        # 3-second hook & retention curve optimization
│   ├── terminal-inserts/            # Monospace CLI & code demo window rendering
│   ├── video-motion-styles/         # Physics easings, springs, and velocity curves
│   ├── vox-explainer/               # Vox-style documentary graphics & maps
│   ├── youtube-editor/              # 16:9 narrative pacing & rhythm assembly
│   └── youtube-long-form-essay/     # Deep-dive essay video orchestration
├── styles/                          # Comprehensive Style Guides & Spec Sheets
│   ├── film-styles/                 # 66 complete style specs (STYLE.md + style.json)
│   ├── presets/                     # 8 platform presets (cinematic, shorts-reels, music-video...)
│   ├── caption-styles.md            # 5 caption styles (Apple-Clean, Vox-Highlighter, Sticker-Pop...)
│   ├── director-method.md           # Story structure & hook engineering
│   ├── documentary-style-guide.md   # Archival treatment, texture overlays
│   └── motion-ui-style-library.md   # Motion taxonomy & easing standards
├── tools/                           # Automated Python & Shell CLI Tools
│   ├── openverse_search.py          # Search & download 800M+ CC images, audio, & textures from Openverse
│   ├── generate_interactive_storyboard.py # Generates self-contained interactive HTML decks
│   ├── contact_sheet.py             # Generates 1 fps grids & filmstrip verification sheets
│   ├── qa_check.py                  # Audits timeline safe zones, LUFS audio & compliance
│   ├── index_audio.py               # EBU R128 loudness indexer & speech segmenter
│   ├── render_pure_aroll.py         # 0% synthetic blur studio tone mapper (Mobius curve)
│   ├── analyze_silence.py           # Detects speech pauses & dead air for jump-cuts
│   ├── extract_word_timings.py      # Word-level timestamp extractor for kinetic subtitles
│   ├── download_prompts.py          # Prompt Motion scraper & asset synchronizer
│   └── install_voicestudio.ps1      # 1-click installer for VoiceStudio
├── workflows/                       # Standard Operating Procedures & Runbooks
│   ├── new-reel.md                  # Complete 9:16 vertical reel creation pipeline
│   ├── new-youtube.md               # Complete 16:9 long-form video pipeline
│   ├── fix-edit.md                  # Rapid iteration & revision workflow
│   ├── index-audio.md               # Dialogue extraction & audio mastering workflow
│   └── status.md                    # Health check & asset readiness monitor
├── templates/                       # Production Templates
│   ├── storyboard_template.md       # Scene-by-scene storyboard specification
│   ├── stylesheet_template.md       # Visual design system token specification
│   └── animejs_motion_preset.js     # Reusable Anime.js motion presets (stagger, spring, SVG)
├── examples/                        # Real-World Production Case Studies
│   └── bairan_music_video/          # 2.5-min Surreal Multiplane Motion Collage (code, storyboard, stylesheet)
├── reference/                       # Style Catalogs & Research
│   ├── STYLE_ATLAS.md               # Master reference index of 66 film styles & directing rules
│   ├── PROMPT_MOTION_INDEX.md       # 236 Crazy AI Animation Prompts with video previews
│   └── prompt_motion_cards.json     # Machine-readable metadata for prompt-motion catalog
├── setup.ps1                        # 1-command Windows setup script
├── setup.sh                         # 1-command Linux/macOS setup script
├── LICENSE                          # MIT License
└── README.md                        # Documentation & quick-start guide
```

---

## 📜 Audio Mastering & Remotion Sequence Rules

### 1. Broadcast Dialogue Leveling (`dynaudnorm`)
Multi-take dialogue frequently suffers from variable mouth distance. Normalize all voice takes with FFmpeg:
```bash
ffmpeg -i input_take.wav -af "dynaudnorm=f=150:g=15:p=0.95:m=10.0" -ar 48000 output_take.wav
```

### 2. Remotion Sequence Local Clock Rule
Inside Remotion `<Sequence from={T}>`, child elements evaluate `useCurrentFrame()` relative to `T`.  
**Never** apply an additional `startFrom={T}` on child `<OffthreadVideo>`, which creates double-offset seeking and freezes video playback at the clip's end.

---

## 🤝 Contributing

Contributions, new styles, and additional motion components are welcome! Please open an issue or submit a pull request.

## 📄 License

MIT License © 2026 [SonuSV7719](https://github.com/SonuSV7719).
