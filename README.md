<div align="center">

# 🎬 AI Video Studio

**The Programmatic, Agentic Video Production Engine & Style System**  
*Code-driven motion graphics, terminal-native product demos, cinematic reels, and broadcast audio mastering — 100% local, reproducible, and review-gated.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Node: >=20](https://img.shields.io/badge/Node.js-%3E%3D20-green.svg?style=flat-square)](https://nodejs.org/)
[![Python: >=3.11](https://img.shields.io/badge/Python-%3E%3D3.11-3776AB.svg?style=flat-square&logo=python&logoColor=white)](https://python.org/)
[![Remotion](https://img.shields.io/badge/Remotion-React%20Video-61DAFB.svg?style=flat-square)](https://remotion.dev)
[![HyperFrames](https://img.shields.io/badge/HyperFrames-v0.8.223-ff8a3d.svg?style=flat-square)](https://github.com/heygen-com/hyperframes)
[![VoiceStudio](https://img.shields.io/badge/VoiceStudio-Local%20TTS%20%26%20Clone-993f61.svg?style=flat-square)](https://voicestudio.sh/)

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

## 📂 Repository Structure

```
ai-video-studio/
├── skills/                          # Global AI Agent Skills
│   ├── video-storyboard/            # Terminal-native & product video storyboard skill
│   ├── video-storyboard-stylesheet/ # Reference video analysis & stylesheet generator
│   └── lemo-opuscar/                # 66 code-rendered film styles skill
├── tools/                           # Studio Automation Scripts
│   ├── generate_interactive_storyboard.py # Interactive HTML storyboard generator
│   └── ...
├── templates/                       # Production Templates
│   ├── storyboard_template.md       # Scene-by-scene storyboard specification
│   └── stylesheet_template.md       # Visual design system token specification
├── reference/                       # Style Catalogs & Research
│   └── STYLE_ATLAS.md               # Master reference index of styles & directing rules
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
