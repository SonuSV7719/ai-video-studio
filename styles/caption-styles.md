# The Caption Style Library

Five named, ready caption styles. A build **declares one** (or, at most, two used
deliberately) and holds it. Every style below gives the full style sheet, the
motion, the timing, the alpha notes, and when to use it. The Text Law still
holds: on-screen text maps the visual; a plain SRT is only an optional sidecar.

**Universal rules for every style:** word-level timing (±100 ms) · ≤2 lines ·
≤17 characters/second · minimum cue ~0.84 s · inside the text-safe zone · eased
motion (never linear) · one accent keyword per line · contrast ≥ 4.5:1.

---

## 1 · Apple-Clean
The default house caption. Quiet, premium, never in the way.
- **Font** SF Pro / Inter · **weight** 400–500 · **size** body ramp (17px-equivalent
  at 1080p, scaled to the frame) · **tracking** −0.374px · **leading** 1.4 ·
  **case** Sentence case.
- **Fill** #1d1d1f on light, #f5f5f7 on dark · **box** none · **stroke** none.
- **Accent** the single blue (#0071e3) on one keyword, underline or colour only.
- **Motion** fade + rise 8–12px, 250 ms in / 220 ms out, ease-out.
- **Alpha** solid text, no background.
- **Use when:** brand, product, corporate, education, any premium piece.

## 2 · Vox-Highlighter
Editorial, informational. The type is part of the argument.
- **Font** condensed sans (bold) · **size** large, line with the narration ·
  **tracking** tight · **case** Sentence case or ALL-CAPS for a shout.
- **Fill** near-black on a muted ground · **accent** the highlighter (yellow
  #FFE14D) or a red circle.
- **Motion** word-by-word reveal, anchor repositioning before each word; the
  **highlighter swipe lands on the stressed word**; stepwise lower-third reveal.
- **Alpha** solid; the highlighter is a shape behind the text.
- **Use when:** explainers, "explain the news", concept and culture videos.

## 3 · Sticker-Pop
Loud, social, retention-driven. Captions as stickers.
- **Font** rounded/heavy sans · **weight** 700–900 · **size** large · **case**
  ALL-CAPS · **tracking** slightly tight.
- **Fill** white · **stroke** 4–8px dark outline · **box** a rounded colour chip
  or a transparent sticker · **accent** one saturated colour per line.
- **Motion** per-word scale pop (0.85 → 1.0, overshoot 1.06) on the beat; slight
  rotation ±2° for energy.
- **Alpha** delivered as **transparent PNG stickers** (no background) so the chip
  shape and outline sit over the picture; clean premultiplied edge.
- **Use when:** Reels/Shorts/TikTok, DTC ads, hype, gaming.

## 4 · Outline-Alpha
Cinematic overlay text. Never a box; the picture stays visible through the type.
- **Font** clean sans or a display face · **weight** 500–700 · **size** large.
- **Fill** none (knock-out) or a very low-opacity white · **stroke** 2–3px white
  or accent · **box** none.
- **Motion** slow fade + rise, or a mask/wipe reveal; restrained.
- **Alpha** **outline-only text as PNG with alpha** (or an alpha clip), so the
  scene shows through the letters. For **text-behind-subject**, place this layer
  UNDER the subject's alpha matte (matte from chroma key or an AI matte) so the
  subject stands in front of the words.
- **Use when:** brand films, trailers, cinematic pieces, titles over footage.

## 5 · Karaoke-Word
Sung-along, music and speech-sync. The word lights up as it is said.
- **Font** clean sans, medium weight · **case** Sentence case · **size** medium.
- **Fill** dim (40–60% opacity) base; the **active word** at full brightness in
  the accent colour · **box** none or a subtle capsule.
- **Motion** the active word fills/scale-pops **on its exact word onset**; the
  rest dim; a small bounce at line end.
- **Alpha** solid, or transparent PNG if a capsule/sticker shape is used.
- **Use when:** music videos, lyric videos, podcasts, spoken-word, karaoke.

---

## Choosing a style (quick map)
| Build | Style |
|---|---|
| Brand, product, corporate, education, premium | **Apple-Clean** |
| Explainer, news, concept, culture | **Vox-Highlighter** |
| Reels/Shorts/TikTok, DTC ads, hype | **Sticker-Pop** |
| Brand film, trailer, cinematic, titles | **Outline-Alpha** |
| Music, lyrics, podcast, spoken-word | **Karaoke-Word** |

## Where these go in the build
1. **CONCEPT.md** — declare the chosen style and paste its style sheet into the
   caption style sheet field.
2. **ASSETS-PROMPT.md** — request any transparent caption PNGs / alpha clips
   (styles 3 and 4) under **transparent images (category 2)**, and the caption
   engine / font kit under **code components (category 6)**.
3. **Build** — apply the style consistently; time every caption from the
   word-level transcription JSON.
4. **QA** — the `edit-qa-validator` skill checks the style sheet, the timing and
   the alpha edges.
