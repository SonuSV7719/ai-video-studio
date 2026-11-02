# Visual Stylesheet: Bairan Animated Music Video

**Song**: Bairan (by Banjaare)  
**Audio Source**: `raw_footage/bairan_audio.mp3` (Duration: `02:30.39` | 150.4s | 3,610 frames @ 24fps)  
**Reference Video**: `reference/bairan_reference.mp4` (Animated Love Story)  
**Style Benchmark**: Romantic Anime / Cel Watercolor Aesthetic (`cel-anime-80s` + `watercolor` from `lemo-opuscar`)

---

## 1. Canvas & Technical Metrics
| Metric | Setting | Specification |
| :--- | :--- | :--- |
| **Resolution** | `1920 x 1080` (16:9 Landscape) / `1080 x 1920` (9:16 Vertical Cut) | High-definition cinematic widescreen |
| **Framerate** | `24.000 fps` | Filmic 24fps CFR cadence matching traditional animation |
| **Color Space** | `BT.709` / `sRGB` | Warm golden hour & twilight mood |
| **Render Engine** | Remotion / Lemo-Opuscar HTML5 Canvas & SVG Layer Compositor | Procedural animated art + Remotion timeline |
| **Audio Standard** | Mastered to `-14 LUFS` | Broadcast pop standard, acoustic rhythm with balanced vocals |

---

## 2. Color Palette Tokens (Warm Sunset & Twilight Romance)

| Token Name | Hex Code | Visual Application & Description |
| :--- | :--- | :--- |
| **`bg-twilight`** | `#1C1924` | Night sky, deep shadow base, silhouette backgrounds |
| **`sky-sunset`** | `#E57357` | Warm terracotta orange sky gradient during golden hour |
| **`dusk-rose`** | `#D47A8A` | Soft blush pink cloud highlights and romantic lighting |
| **`gold-lantern`**| `#FFC857` | Warm glowing lanterns, street lamps, and window bokeh |
| **`earth-warm`** | `#4A3528` | Wood, cobblestone paths, earthy clothing tones |
| **`text-lyric`** | `#FFFDF9` | Soft warm cream for on-screen kinetic lyrics |
| **`accent-teal`** | `#4E878C` | Distant hills, water reflections, foliage contrast |

---

## 3. Typography & Lyric Styling
- **Primary Title**: `Cinzel Decorative` or `Playfair Display Bold` (Weight: 700, tracking `+0.08em`, letterspaced, elegant serif).
- **Subtitles & Kinetic Lyrics**: `Outfit SemiBold` / `Inter` (Weight: 600, sentence case, subtle outer glow `rgba(0,0,0,0.5)`, backdrop pill blur on complex backgrounds).
- **Hindi Script Glyphs (Devanagari)**: `Noto Serif Devanagari` / `Rozha One` for poetic Hindi typography inserts ("बैरण").

---

## 4. Motion Grammar & Easing Curves
- **Camera Grammar**:
  - Slow panoramic drifts (`0.5% - 1.2% scale drift` over 4–6s).
  - Gentle rack focus (defocusing foreground autumn leaves to reveal characters).
  - Parallax depth: 3 visual layers (Foreground silhouettes → Midground characters → Background sky/mountains).
- **Animation Easing**:
  - Character micro-gestures: Remotion `spring({ damping: 18, stiffness: 80, mass: 0.8 })`
  - Particle floats (fireflies, cherry blossom petals, dust motes): Perlin noise wind vector with GSAP drift.
- **Shot Cadence**: 4.0s to 7.0s per shot, synchronized to musical chord shifts and lyrical pauses.
