# Content-to-Tool & Stack Decision Matrix

This matrix governs how the autonomous Video Director selects, configures, and sequences tools across the `ai-video-studio` engine based on the subject matter, target platform, and narrative objective.

---

## 1. Talking-Head Reel / Founder Short (Vertical 9:16)
* **Goal**: High-authority thought leadership, SaaS announcement, personal branding.
* **Target Platforms**: Instagram Reels, YouTube Shorts, TikTok, LinkedIn Video.
* **Average Shot Length (ASL)**: `1.4s - 2.2s`.
* **Visual Treatment**:
  - Raw camera footage rendered with 0% synthetic blur and Mobius broadcast tone-mapping (`render_pure_aroll.py`).
  - Face tracking & person segmentation (`skills/video-effects`).
* **51 Viral Video Effects**:
  - `0-3s Hook`: `spotlight` (ambient dim with glowing headline behind head) or `locked-on` (dynamic face tracking).
  - `3-15s Body`: `backdrop-word` (massive serif/bold keyword dropping behind head), `lean-in` on punchlines.
  - `15-30s Proof`: `liquid-glass-graph` (floating translucent charts) or `apple-toggles` (iPhone toggles flipping on).
* **Kinetic Captions**: Apple-Clean or Vox-Highlighter from `styles/caption-styles.md` (1-3 words visible, active word highlighted in `#FFE600`).
* **Audio Stack**:
  - Voice: FFmpeg `dynaudnorm=f=150:g=15:p=0.95:m=10.0` (broadcast constant -14 LUFS).
  - Sound Effects: Earshot UI pops, crisp whooshes, riser hit at hook transition.
  - Music Bed: Muted lo-fi hip-hop or tech beat ducked at `-18 dB`.

---

## 2. DevTool, CLI & Terminal Demo (Vertical 9:16 or Horizontal 16:9)
* **Goal**: Developer agent launch, SDK tutorial, open-source tool showcase.
* **Target Platforms**: X / Twitter, YouTube, ProductHunt, GitHub Readme.
* **Average Shot Length (ASL)**: `2.0s - 3.5s`.
* **Visual Treatment**:
  - Lemo-Opuscar style: `dark-keynote` or `living-screencast`.
  - Monospace typography (JetBrains Mono / Space Mono).
  - Terminal windows with glowing borders, simulated typing cursors, and telemetry HUD indicators.
* **Motion Graphics & Animation**:
  - Anime.js SVG path drawing for architecture boxes and arrows (`anime.setDashoffset`).
  - Staggered code syntax reveals (`delay: anime.stagger(40)`).
* **51 Viral Video Effects**:
  - `shortcut-rain` (keyboard keys cascading in background).
  - `glass-widgets` (frosted glass metric pills floating around the screencast).
  - `checklist` (terminal-like task list ticking green).
* **Audio Stack**:
  - Voice: Clean, uncompressed narration or VoiceStudio cloned voice.
  - SFX: Mechanical keyboard key clicks (Cherry MX blue/brown), soft subtle hum/drone.

---

## 3. Deep-Dive Essay & Vox-Style Documentary (Horizontal 16:9)
* **Goal**: Analytical breakdown, market history, technical investigation.
* **Target Platforms**: YouTube Long-Form.
* **Average Shot Length (ASL)**: `3.0s - 5.0s`.
* **Visual Treatment**:
  - Lemo-Opuscar style: `swiss-motion`, `blueprint`, `risograph`, or `visual-investigation`.
  - Archival document treatments with paper grain textures downloaded via `openverse_search.py`.
* **Motion Graphics & Animation**:
  - Kinetic text highlighters (`skills/article-highlights`).
  - Animated 2.5D map zooms and document camera rotations.
* **51 Viral Video Effects**:
  - `pause-point` (freeze frame with hand-drawn marker arrow).
  - `huge-strike` (giant serif word crossed out with bold marker).
  - `broll-split` (split screen showing archival footage on top and animated data on bottom).
* **Audio Stack**:
  - Full multi-track cinematic score: Orchestral tension beds, tempo changes on act turns.
  - Sound design: Paper shuffles, archival camera shutter clicks, low orchestral braams.

---

## 4. SaaS Product Metrics & Revenue Showcase (Vertical 9:16)
* **Goal**: Share growth metrics, investor updates, ARR milestones.
* **Average Shot Length (ASL)**: `1.2s - 1.8s` (Rapid retention).
* **Visual Treatment**:
  - High-contrast dark mode canvas (`#0A0A0C`) with neon metric accents (`#00F0FF`, `#00FF66`).
  - Translucent liquid glass cards with real-time blur reflection.
* **Motion Graphics & Animation**:
  - GSAP / Anime.js animated number tickers counting up from `0` to `$1.2M`.
  - Spring-loaded bar graphs and curved sparklines drawing from left to right.
* **51 Viral Video Effects**:
  - `liquid-glass-graph` (floating graph under speaker's chin).
  - `phone-fan` (array of mobile screens fanning out like playing cards).
  - `select-resize` (blue UI bounding box grabbing and expanding the metric).
* **Audio Stack**:
  - Sound design: Ticking counter clicker synced to numbers, cash register chime or sub-bass thud at milestone reveal.

---

## 5. Creative Promo & Music Video (Vertical 9:16 or Horizontal 16:9)
* **Goal**: Music release, creative brand anthem, hype teaser.
* **Average Shot Length (ASL)**: `0.8s - 1.5s` (Synchronized to musical beat transients).
* **Visual Treatment**:
  - Lemo-Opuscar styles: `cel-anime-80s`, `woodcut`, `watercolor`, or `surreal-multiplane-collage`.
  - Prompt Motion (236 crazy prompt recipes from `reference/PROMPT_MOTION_INDEX.md`).
* **Motion Graphics & Animation**:
  - Anime.js physics springs with rhythmic pulsing (`spring(1, 90, 14, 0)`).
  - Multi-layer visual collage where foreground and background move at contrasting speeds.
* **51 Viral Video Effects**:
  - `dot-reveal` (shot builds itself out of glowing particles).
  - `rabbit-hole` (infinite recursive frame tunnel).
  - `carousel-spin` (3D revolving carousel).
* **Audio Stack**:
  - Master music track analyzed for onset beats and transients.
  - Cuts, flash frames, and camera punches locked to kick drum and snare hits.
