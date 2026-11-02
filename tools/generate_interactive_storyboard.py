import os
import sys
import json

def generate_interactive_html(title, scenes, stylesheet, output_path):
    scenes_json = json.dumps(scenes, indent=2)
    stylesheet_json = json.dumps(stylesheet, indent=2)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Interactive Storyboard & Stylesheet</title>
  <style>
    :root {{
      --bg: #141312;
      --card-bg: #1c1b19;
      --card-border: rgba(255, 255, 255, 0.08);
      --text: #ECE9E1;
      --text-muted: #9A968C;
      --accent: #D97757;
      --accent-cyan: #00E5FF;
      --success: #7FB069;
      --font-mono: 'JetBrains Mono', 'Fira Code', 'IBM Plex Mono', monospace;
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg);
      color: var(--text);
      font-family: var(--font-sans);
      line-height: 1.5;
      padding: 32px 24px;
      min-height: 100vh;
    }}
    .container {{
      max-width: 1280px;
      margin: 0 auto;
    }}
    header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 1px solid var(--card-border);
      padding-bottom: 24px;
      margin-bottom: 32px;
      flex-wrap: wrap;
      gap: 16px;
    }}
    .badge {{
      display: inline-block;
      padding: 4px 10px;
      font-size: 11px;
      font-family: var(--font-mono);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-radius: 4px;
      background: rgba(217, 119, 87, 0.15);
      color: var(--accent);
      border: 1px solid rgba(217, 119, 87, 0.3);
      margin-bottom: 8px;
    }}
    h1 {{
      font-size: 28px;
      font-weight: 800;
      letter-spacing: -0.02em;
      margin-bottom: 6px;
    }}
    .subtitle {{
      color: var(--text-muted);
      font-size: 14px;
    }}
    .deck-stats {{
      display: flex;
      gap: 20px;
      font-family: var(--font-mono);
      font-size: 13px;
    }}
    .stat-box {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      padding: 10px 16px;
      border-radius: 6px;
      text-align: right;
    }}
    .stat-label {{ color: var(--text-muted); font-size: 11px; text-transform: uppercase; }}
    .stat-val {{ font-weight: 700; color: var(--text); }}

    /* Layout */
    .main-grid {{
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 28px;
      margin-bottom: 36px;
    }}
    @media (max-width: 960px) {{
      .main-grid {{ grid-template-columns: 1fr; }}
    }}

    /* Viewport / Frame Mockup */
    .viewport-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 20px;
      position: sticky;
      top: 24px;
    }}
    .viewport-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
    }}
    .window-dots {{
      display: flex;
      gap: 6px;
    }}
    .dot {{
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #333;
    }}
    .dot.red {{ background: #e5484d; }}
    .dot.yellow {{ background: #f5a623; }}
    .dot.green {{ background: #7fb069; }}
    .frame-title {{
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--text-muted);
    }}
    .canvas-preview {{
      width: 100%;
      height: 480px;
      background: #0d0f12;
      border-radius: 6px;
      border: 1px solid rgba(255, 255, 255, 0.05);
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 24px;
    }}
    .canvas-hud-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .hud-tag {{
      background: rgba(0, 229, 255, 0.12);
      color: var(--accent-cyan);
      border: 1px solid rgba(0, 229, 255, 0.3);
      padding: 3px 8px;
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 600;
    }}
    .hud-fps {{
      font-family: var(--font-mono);
      font-size: 11px;
      color: rgba(255, 255, 255, 0.4);
    }}
    .canvas-terminal-mock {{
      background: rgba(18, 20, 24, 0.92);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 6px;
      padding: 16px;
      font-family: var(--font-mono);
      font-size: 13px;
      color: var(--text);
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.6);
      margin: auto 0;
    }}
    .canvas-caption-bar {{
      background: rgba(10, 12, 16, 0.85);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 10px 16px;
      border-radius: 6px;
      text-align: center;
      font-weight: 700;
      font-size: 15px;
      letter-spacing: -0.01em;
    }}
    .highlight-word {{
      color: var(--accent-cyan);
    }}

    /* Scene Navigation */
    .scene-navigator {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .scene-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 8px;
      padding: 16px;
      cursor: pointer;
      transition: all 0.2s ease;
      position: relative;
    }}
    .scene-card:hover {{
      border-color: rgba(255, 255, 255, 0.2);
      transform: translateX(3px);
    }}
    .scene-card.active {{
      border-color: var(--accent);
      background: #252320;
    }}
    .scene-card.active::before {{
      content: '';
      position: absolute;
      left: 0;
      top: 0;
      bottom: 0;
      width: 4px;
      background: var(--accent);
      border-radius: 8px 0 0 8px;
    }}
    .scene-meta {{
      display: flex;
      justify-content: space-between;
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--text-muted);
      margin-bottom: 6px;
    }}
    .scene-name {{
      font-size: 15px;
      font-weight: 700;
      margin-bottom: 6px;
    }}
    .scene-vo {{
      font-size: 13px;
      color: #ccc;
      font-style: italic;
      margin-bottom: 8px;
    }}
    .scene-tags {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .tag {{
      font-family: var(--font-mono);
      font-size: 10px;
      background: rgba(255, 255, 255, 0.05);
      padding: 2px 6px;
      border-radius: 3px;
      color: #aaa;
    }}

    /* Stylesheet section */
    .stylesheet-section {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 24px;
      margin-top: 32px;
    }}
    .palette-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
      gap: 16px;
      margin-top: 16px;
    }}
    .palette-card {{
      border: 1px solid var(--card-border);
      border-radius: 6px;
      overflow: hidden;
      background: #141312;
    }}
    .color-swatch {{
      height: 48px;
      width: 100%;
    }}
    .color-info {{
      padding: 8px;
      font-family: var(--font-mono);
      font-size: 11px;
    }}
    .color-name {{ font-weight: 600; color: #fff; margin-bottom: 2px; }}
    .color-hex {{ color: var(--text-muted); }}

    /* Timeline Bar */
    .timeline-scrubber {{
      display: flex;
      height: 12px;
      background: #242220;
      border-radius: 4px;
      overflow: hidden;
      margin-top: 24px;
      margin-bottom: 16px;
      cursor: pointer;
    }}
    .timeline-segment {{
      height: 100%;
      border-right: 1px solid #141312;
      transition: background 0.2s ease;
    }}
    .timeline-segment:hover {{
      opacity: 0.8;
    }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div>
        <div class="badge">Visual Storyboard & Stylesheet Deck</div>
        <h1>{title}</h1>
        <p class="subtitle">Terminal-native, high-retention video design specification (Pre-Production Review)</p>
      </div>
      <div class="deck-stats">
        <div class="stat-box">
          <div class="stat-label">Total Duration</div>
          <div class="stat-val" id="totalDuration">42.1s (1011f)</div>
        </div>
        <div class="stat-box">
          <div class="stat-label">Framerate</div>
          <div class="stat-val">24.000 CFR</div>
        </div>
        <div class="stat-box">
          <div class="stat-label">Review Status</div>
          <div class="stat-val" style="color: var(--success);">READY FOR REVIEW</div>
        </div>
      </div>
    </header>

    <!-- Timeline Scrubber -->
    <div class="timeline-scrubber" id="timelineBar"></div>

    <!-- Main Workspace Grid -->
    <div class="main-grid">
      <!-- Live Preview Canvas -->
      <div class="viewport-card">
        <div class="viewport-header">
          <div class="window-dots">
            <span class="dot red"></span>
            <span class="dot yellow"></span>
            <span class="dot green"></span>
          </div>
          <div class="frame-title" id="frameTitle">SCENE 1 • THE HOOK</div>
          <div class="hud-tag" id="hudShotType">FULLSCREEN A-ROLL</div>
        </div>

        <div class="canvas-preview" id="canvasPreview">
          <div class="canvas-hud-top">
            <span class="hud-tag" id="hudBadge">BREAKING AI</span>
            <span class="hud-fps" id="hudTimecode">00:00.00 – 00:03.29</span>
          </div>

          <div class="canvas-terminal-mock" id="canvasTerminal">
            <span style="color: var(--accent);">></span> <span id="canvasCommand">python -m genie.engine --interactive</span>
            <div id="canvasOutput" style="color: #9A968C; font-size: 12px; margin-top: 8px;">
              [init] Neural world model initialized (24 fps)<br>
              [stream] Ready for real-time steering...
            </div>
          </div>

          <div class="canvas-caption-bar" id="canvasCaption">
            "Google just dropped something completely insane."
          </div>
        </div>

        <div style="margin-top: 16px; display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 11px; color: var(--text-muted);">
          <span id="canvasMotion">Camera: 1.08x punch-in on frame 24</span>
          <span id="canvasAudio">Audio: Sub-bass boom + SFX whoosh</span>
        </div>
      </div>

      <!-- Scene Navigator List -->
      <div class="scene-navigator" id="sceneList"></div>
    </div>

    <!-- Stylesheet & Color Tokens -->
    <div class="stylesheet-section">
      <div class="badge" style="background: rgba(0,229,255,0.1); color: var(--accent-cyan); border-color: rgba(0,229,255,0.3);">
        Visual Design Stylesheet Tokens
      </div>
      <h3 style="margin-top: 8px; font-weight: 800;">Brand Color Palette & Layout Specs</h3>
      <div class="palette-grid" id="paletteGrid"></div>
    </div>
  </div>

  <script>
    const scenes = {scenes_json};
    const stylesheet = {stylesheet_json};
    let activeIndex = 0;

    function renderScenes() {{
      const listEl = document.getElementById('sceneList');
      const timelineEl = document.getElementById('timelineBar');
      listEl.innerHTML = '';
      timelineEl.innerHTML = '';

      scenes.forEach((scene, index) => {{
        // Timeline segment
        const seg = document.createElement('div');
        seg.className = 'timeline-segment';
        seg.style.width = scene.share + '%';
        seg.style.background = index === activeIndex ? 'var(--accent)' : 'rgba(255, 255, 255, 0.15)';
        seg.title = `Scene ${{index + 1}}: ${{scene.title}}`;
        seg.onclick = () => selectScene(index);
        timelineEl.appendChild(seg);

        // Card
        const card = document.createElement('div');
        card.className = 'scene-card' + (index === activeIndex ? ' active' : '');
        card.onclick = () => selectScene(index);
        card.innerHTML = `
          <div class="scene-meta">
            <span>SCENE ${{index + 1}} • ${{scene.timecode}}</span>
            <span>${{scene.duration}}</span>
          </div>
          <div class="scene-name">${{scene.title}}</div>
          <div class="scene-vo">"${{scene.vo}}"</div>
          <div class="scene-tags">
            <span class="tag">${{scene.shotType}}</span>
            <span class="tag">${{scene.motion}}</span>
          </div>
        `;
        listEl.appendChild(card);
      }});
    }}

    function selectScene(index) {{
      activeIndex = index;
      const s = scenes[index];

      document.getElementById('frameTitle').innerText = `SCENE ${{index + 1}} • ${{s.title.toUpperCase()}}`;
      document.getElementById('hudShotType').innerText = s.shotType.toUpperCase();
      document.getElementById('hudBadge').innerText = s.badge || 'TELEMETRY';
      document.getElementById('hudTimecode').innerText = s.timecode;
      document.getElementById('canvasCommand').innerText = s.command || 'engine --run';
      document.getElementById('canvasOutput').innerHTML = s.terminalOutput || '[streaming tokens...]';
      document.getElementById('canvasCaption').innerHTML = s.caption || s.vo;
      document.getElementById('canvasMotion').innerText = `Motion: ${{s.motion}}`;
      document.getElementById('canvasAudio').innerText = `Audio: ${{s.audio}}`;

      renderScenes();
    }}

    function renderPalette() {{
      const pGrid = document.getElementById('paletteGrid');
      pGrid.innerHTML = '';
      stylesheet.colors.forEach(col => {{
        const card = document.createElement('div');
        card.className = 'palette-card';
        card.innerHTML = `
          <div class="color-swatch" style="background: ${{col.hex}};"></div>
          <div class="color-info">
            <div class="color-name">${{col.name}}</div>
            <div class="color-hex">${{col.hex}}</div>
          </div>
        `;
        pGrid.appendChild(card);
      }});
    }}

    // Keydown listeners for arrow key scene navigation
    window.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {{
        selectScene((activeIndex + 1) % scenes.length);
      }} else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {{
        selectScene((activeIndex - 1 + scenes.length) % scenes.length);
      }}
    }});

    renderScenes();
    renderPalette();
  </script>
</body>
</html>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Interactive storyboard written to: {output_path}")

if __name__ == "__main__":
    sample_scenes = [
        {
            "title": "The Hook",
            "timecode": "00:00.00 – 00:03.29",
            "duration": "3.3s (79f)",
            "share": 8,
            "shotType": "Crisp Presenter A-Roll",
            "badge": "BREAKING AI",
            "command": "python -m genie.engine --version",
            "terminalOutput": "Google DeepMind Genie 4 (Build 2026.11)<br>Status: Autonomous World Engine Loaded",
            "vo": "Google just dropped something completely insane, and almost nobody noticed.",
            "caption": "Google just dropped something completely <span class='highlight-word'>INSANE</span>.",
            "motion": "Subtle 1.08x punch-in on frame 24",
            "audio": "Deep sub-boom + riser"
        },
        {
            "title": "The Proof / Dragon Flight Demo",
            "timecode": "00:03.29 – 00:09.50",
            "duration": "6.2s (149f)",
            "share": 15,
            "shotType": "B-Roll + Presenter 280px PiP",
            "badge": "REAL-TIME WORLD MODEL",
            "command": "genie stream --render --prompt 'ancient dragon over volcanic canyon'",
            "terminalOutput": "[stream] Latency: 14.2ms | Resolution: 4K 60FPS<br>[physics] Continuous terrain collision active",
            "vo": "This is Genie 4. Not a pre-rendered CGI clip — this entire 3D world is generated in real-time.",
            "caption": "Not a pre-rendered CGI clip — this entire world is <span class='highlight-word'>GENERATED IN REAL-TIME</span>.",
            "motion": "Fast push-in on terrain geometry",
            "audio": "Dragon wing swoosh + telemetry chirp"
        },
        {
            "title": "Continuous Physics Simulation",
            "timecode": "00:09.50 – 00:15.00",
            "duration": "5.5s (132f)",
            "share": 14,
            "shotType": "Split Detail / Collision",
            "badge": "ZERO GLITCH PHYSICS",
            "command": "inspect --physics --track-collisions",
            "terminalOutput": "Raytracing light bounces: 12 bounces / frame<br>Momentum vectors: 100% physically coherent",
            "vo": "It doesn't just draw frames — it simulates real physical momentum, lighting, and camera collisions.",
            "caption": "It simulates real <span class='highlight-word'>PHYSICAL MOMENTUM</span> and lighting.",
            "motion": "Slow drift with light flare sweep",
            "audio": "Impact pulse + synth sweep"
        },
        {
            "title": "Steerable Interactive Controller",
            "timecode": "00:15.00 – 00:22.00",
            "duration": "7.0s (168f)",
            "share": 17,
            "shotType": "Controller Mockup + Gameplay",
            "badge": "< 16ms LATENCY",
            "command": "connect --input 'DualSense Wireless' --stream",
            "terminalOutput": "Input registered: LeftStick (+0.84, -0.12)<br>Camera orientation updated in 12ms",
            "vo": "You can literally pick up a controller and steer through an infinite universe that didn't exist a second ago.",
            "caption": "Steer through an <span class='highlight-word'>INFINITE UNIVERSE</span> with a controller.",
            "motion": "Dynamic camera turn matching controller stick",
            "audio": "Haptic click + electronic riser"
        },
        {
            "title": "Architectural Leap (10x Efficiency)",
            "timecode": "00:22.00 – 00:29.50",
            "duration": "7.5s (180f)",
            "share": 18,
            "shotType": "Presenter + Glass UI Card",
            "badge": "NEURAL WEIGHTS VS MESHES",
            "command": "benchmark --compare genie3 genie4",
            "terminalOutput": "Genie 3: 180ms latency | 12 GB VRAM<br>Genie 4: 14ms latency | 2.4 GB VRAM (10x faster)",
            "vo": "Traditional game engines took decades to build. DeepMind just replaced geometry meshes with pure neural weights.",
            "caption": "Replaced geometry meshes with <span class='highlight-word'>PURE NEURAL WEIGHTS</span>.",
            "motion": "Glass card slides in from right",
            "audio": "Glass slide + digital ping"
        },
        {
            "title": "Infinite Multi-World Montage",
            "timecode": "00:29.50 – 00:36.00",
            "duration": "6.5s (156f)",
            "share": 15,
            "shotType": "Rapid Multi-Genre Cut",
            "badge": "END OF STATIC ASSETS",
            "command": "generate --montage --themes 'cyberpunk, jungle, orbit'",
            "terminalOutput": "Cut 1: Neo-Tokyo neon street [rendered]<br>Cut 2: Bioluminescent canopy [rendered]<br>Cut 3: Orbital station [rendered]",
            "vo": "Imagine game worlds with infinite procedurally authored storylines that react directly to your voice.",
            "caption": "Infinite procedurally authored storylines that react to your <span class='highlight-word'>VOICE</span>.",
            "motion": "Triple 1.5s hard cuts with speed ramp",
            "audio": "Triple staccato riser hits"
        },
        {
            "title": "Outro & Call To Action",
            "timecode": "00:36.00 – 00:42.12",
            "duration": "6.1s (147f)",
            "share": 14,
            "shotType": "Fullscreen A-Roll + Branded Endcard",
            "badge": "FOLLOW FOR NEXT DROP",
            "command": "echo 'Follow @ai_insider for daily breakthrough breakdowns'",
            "terminalOutput": "Subscribed to AI Insider telemetry feed.",
            "vo": "Drop a comment if you think neural engines will replace Unreal Engine, and follow for what comes next.",
            "caption": "Drop a comment and <span class='highlight-word'>FOLLOW</span> for what comes next.",
            "motion": "Logo badge pop with smooth fade",
            "audio": "Branded chime + volume fade"
        }
    ]

    sample_stylesheet = {
        "colors": [
            {"name": "Background Carbon", "hex": "#141312"},
            {"name": "Surface Card", "hex": "#1C1B19"},
            {"name": "Text Primary", "hex": "#ECE9E1"},
            {"name": "Text Muted", "hex": "#9A968C"},
            {"name": "Accent Coral", "hex": "#D97757"},
            {"name": "Accent Cyan", "hex": "#00E5FF"},
            {"name": "Success Green", "hex": "#7FB069"}
        ]
    }

    out_file = sys.argv[1] if len(sys.argv) > 1 else "storyboard_interactive.html"
    generate_interactive_html("Google Genie 4 AI Cinematic Reel", sample_scenes, sample_stylesheet, out_file)
