---
name: video-storyboard
description: Generate an executive, interactive visual storyboard, shot list, voiceover script, and visual design stylesheet for developer-tool and product videos in a terminal-native, Claude Code-style aesthetic (dark UI, monospace type, calm pacing, interactive card previews). Use when the user asks for a storyboard, video plan, interactive story, demo video script, promo/explainer video, or "video like Claude Code".
argument-hint: "[generate|interactive|scaffold] [topic-or-brief]"
metadata:
  author: sonu
  version: "2.0.0"
---

# Video Storyboard (Terminal-Native & Interactive Product Storyboard)

Produce a complete, production-ready, **interactive visual storyboard** for a 30–90 second developer-tool or product video. The look is calm, confident, and terminal-first: the product doing real work is the hero, backed by a cinematic visual storyboard that stakeholders can interactively review and approve before any rendering begins.

---

## Core Rules & Production Gates

1. **Mandatory 3-Folder Architecture**:
   - `raw_footage/`: Raw screencasts, terminal sessions, camera A-roll, raw audio.
   - `reference/`: Reference benchmark videos, inspiration clips (via `yt-dlp`), competitor reels.
   - `export/`: Rendered storyboard assets, HTML interactive previews, final video masters.

2. **Pre-Production Review Gate (Storyboard & Stylesheet First)**:
   - NEVER jump straight into rendering a video without presenting the user with:
     - `stylesheet.md`: Colors, typography, safe margins, and easing curves.
     - `storyboard.md`: Scene-by-scene card layout with timings, visual layout, text overlays, and audio cues.
     - **Interactive Visual Storyboard**: A rich visual artifact (`storyboard_interactive.html` or markdown card carousel) containing concrete visual frame previews, color swatches, and timeline pacing.
   - Wait for explicit user confirmation or adjustments before rendering or writing video code.

3. **Natural Camera Clarity & Authentic UI (Strictly 0% Synthetic Blur)**:
   - For real camera takes, preserve 100% natural optical sharpness. Never apply synthetic oval background blur or blurry halo cutouts.
   - Terminal & UI mockups must be crisp, high-contrast, and monospaced with subtle 1px borders.

4. **Broadcast Audio Standards**:
   - Mastered to **-14 LUFS** (speech normalized via FFmpeg `dynaudnorm=f=150:g=15:p=0.95:m=10.0`).
   - Ambient lo-fi background bed ducked to **-22 LUFS** beneath voice with smooth exponential ramps.

---

## Step 1: Gather Inputs & Define Intent

Capture the 5 essential parameters (infer reasonable defaults if already provided; do not interrogate):
1. **Product / Feature Name**: Core value proposition in one sentence.
2. **Target Audience**: Devs, engineers, founders, or general tech enthusiasts.
3. **Format & Duration**: Default 45s (9:16 vertical Reels/Shorts, 16:9 landscape YouTube, or dual).
4. **Call to Action (CTA)**: One specific command (e.g. `npx tool@latest`), repo link, or website URL.
5. **Audio Treatment**: Captions + soft ambient music (default) or synchronized voiceover narration.

---

## Step 2: Narrative Arc Selection

Choose the high-retention 6-beat developer arc:

| Beat | Timeline Share | Purpose | Focus Element |
| :--- | :--- | :--- | :--- |
| **1. Hook** | 0% – 8% (0–4s) | Striking claim or developer pain point in one sentence | Stark typography / Terminal prompt |
| **2. Prompt** | 8% – 20% (4–9s) | Plain-English natural command typed into the CLI | Blinking cursor, 30 cps typing |
| **3. Work** | 20% – 60% (9–27s) | Autonomous execution: streamed progress, file diffs, passing checks | Monospace telemetry, progress bars |
| **4. Result** | 60% – 80% (27–36s) | Tangible finished output (live app, passing test suite, clean build) | Visual "wow" proof shot |
| **5. Proof** | 80% – 92% (36–41s) | Key metric: latency (<16ms), lines of code saved, or instant rerun | Benchmark card / Split-screen |
| **6. CTA** | 92% – 100% (41–45s) | Final brand logo, installation command, and action prompt | Minimalist brand card |

---

## Step 3: Visual Design Stylesheet (`stylesheet.md`)

**Mood**: Quiet, precise, terminal-native, editorial. Motion is purposeful; nothing bounces or flashes.

### Design Tokens
- **Background**: Near-black warm carbon `#1A1918` (or crisp dark slate `#0D0F12`).
- **Surface / Card**: `#242321` with `border: 1px solid rgba(255, 255, 255, 0.08)`.
- **Text Primary**: Soft bone white `#ECE9E1`.
- **Text Secondary**: Muted graphite `#9A968C`.
- **Accent Highlight**: Warm terracotta `#D97757` or Electric Cyan `#00E5FF` for cursor and active tokens.
- **Success & Status**: Sage green `#7FB069` (success), ruby `#E5484D` (error/alert).

### Typography
- **Monospace Code/Telemetry**: `JetBrains Mono`, `IBM Plex Mono`, or `SF Mono` (Weight: 500/600).
- **Titles & Captions**: Clean grotesk/sans (`Inter`, `SF Pro Display`, `Geist Sans`, Weight: 800/900).
- **Caption Badges**: Sentence case, maximum 3–7 words per line, placed in the action-safe vertical third.

### Motion Dynamics
- **Typing Engine**: Realistic typing cadence (25–40 chars/sec) with blinking block cursor (`_` or `▌`).
- **Stream Output**: Subtle vertical fade-rise (`translateY(8px) -> 0`, 160ms cubic-bezier).
- **Camera Moves**: Slow 3% push-in (`scale: 1.0 -> 1.03`), subtle parallax drift, hard cuts.

### Style Presets & Lemo-Opuscar Catalog
In addition to the default terminal aesthetic, you can pick any of the **66 production styles from Lemo-Opuscar** (`reference/repos/lemo-opuscar/styles/<slug>/STYLE.md`), including:
- `dark-keynote`: Carbon slate, glassmorphic code panels, warm terracotta highlights.
- `swiss-motion`: International typographic style, strict grid, high-contrast black/white.
- `hologram-hud`: Neon wireframe telemetry, cyan/amber glowing coordinates.
- `ascii-crt`: Phosphor green/amber terminal, scanline distortion, retro hacker aesthetic.
- `blueprint`: Architectural cyan drafting lines with technical annotations.
- `teardown`: Exploded 3D layer perspective and component disassembly.
See `reference/STYLE_ATLAS.md` for the complete 66-style directory.

---

## Step 4: Interactive Visual Storyboard Generation

To make the storyboard **interactive, visual, and professional**, generate both:
1. **Markdown Executive Storyboard (`storyboard.md`)** with Mermaid flows, scene tables, and slide carousels.
2. **Interactive Visual Preview Artifact (`storyboard_interactive.html`)** containing:
   - Interactive timeline scrubber with scene jump buttons.
   - Live visual card previews showing simulated terminal frames, UI layouts, and shot compositions.
   - Dynamic caption player showing synchronized text cues.
   - Color swatch inspector and technical asset checklist.

### Markdown Storyboard Structure
```markdown
# Executive Storyboard: [Product Name]
**Duration**: [XX] Seconds | **FPS**: 24 CFR | **Aspect Ratio**: [16:9 / 9:16]

## Narrative Timeline
[Mermaid flowchart showing beat sequence]

## Scene-by-Scene Cards
````carousel
```markdown
### Scene 1: [Scene Title] ([Start] - [End])
- **Shot Type**: [Terminal Centered / Split / PiP]
- **Visual Frame**: [Detailed layout description or ASCII Blueprint]
- **Terminal Input**: `> command entered`
- **Caption / VO**: "[Spoken dialogue or subtitle]"
- **Motion & Audio**: [Camera motion + SFX cue]
```
<!-- slide -->
...
````

## Master Production Table
| # | Time | Shot Type | Visual Layout | Terminal / UI Content | Caption / Voiceover | Audio & SFX |
|---|------|-----------|---------------|-----------------------|---------------------|-------------|
```

---

## Step 5: Quality Checklist Before Sign-Off

- [ ] **3-Folder Architecture Created**: `raw_footage/`, `reference/`, `export/` are verified.
- [ ] **Hook lands within first 3 seconds**: Immediately poses problem or striking claim.
- [ ] **Concrete Terminal Content**: Verbatim, authentic commands and directory paths (zero generic `foo`/`bar`).
- [ ] **Visually Verified Result**: Scene 4 showcases actual output, not just endless log scrolling.
- [ ] **One Clear CTA**: Exactly one URL or command given in final 4 seconds.
- [ ] **Readability With Sound Off**: Captions cover every narrative beat cleanly within safe zones.
- [ ] **User Review Gate**: Storyboard & Stylesheet presented to user for sign-off before code/renders.
