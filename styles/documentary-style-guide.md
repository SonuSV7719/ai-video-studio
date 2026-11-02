# The Documentary Style Guide — the router

Documentary is not one craft. It is a family of **editing styles**, each with its
own grammar, structure, ethics and signature techniques. This file maps them so
you pick the right skill before you cut. Every style below is a full skill under
`skills/<name>/SKILL.md`.

**How to choose:** ask what the *material is* and what the *argument needs*.

- If the truth lives in **behaviour you filmed** → observational.
- If it lives in a **person's words** → interview-led.
- If it lives in the **archive** → archival.
- If it lives in a **place or a number** → explainer / map-led.
- If it lives in **memory or feeling** → animation / essay.
- If the event was **never filmed** → reconstruction / docudrama.

---

## A · The theory — Bill Nichols' six modes
The academic canon (dominants, not boxes; most films blend several). Use it to
name the register a film is working in.

| Mode | What it does | Signature |
|---|---|---|
| **Poetic** | mood, tone, aesthetics over argument | associative/impressionistic editing |
| **Expository** | voice-of-God narration argues a thesis | images as evidence, didactic |
| **Observational** | fly-on-the-wall / Direct Cinema / cinéma vérité | no narration, no interviews, long takes |
| **Participatory** | filmmaker enters the story and engages the subject | filmmaker on camera, acknowledged presence |
| **Reflexive** | self-conscious about the form | exposes its own construction |
| **Performative** | subjective, personal, emotive | the filmmaker's lived experience is the text |

## B · The craft-level editing approaches (how the cut is built)
| Approach | The move |
|---|---|
| **Evidentiary** | images serve as proof for commentary |
| **Verité** | observational scenes from raw behaviour: microbeats, body language, amalgam scenes |
| **Montage** | media/thematic montage; compression or argument by juxtaposition |
| **Radio-cut / audio-first** | cut the interview as an audio-only arc, then cover |
| **Additive (assembly)** | start blank, add shots; logic-driven, montage-heavy |
| **Subtractive (excision)** | string rushes out, chip away; immersive, compartmentalised |

## C · The style skills (this pack)

### Explainer family — meaning carried by graphics and place
| Skill | Style | Use when |
|---|---|---|
| `vox-explainer` | narration-driven flat-design motion graphics, highlighter, 12fps stutter, animated maps | "explain the news", concepts, culture/science |
| `geo-explainer-maps` | map-led geo storytelling, camera moves across vector maps, route draw-ons | geopolitics, borders, history-through-place |
| `archival-essay-doc` | argumentative montage, bold statistic typography, photo zoom-and-pan | social-issue/historical argument films |
| `ken-burns-archival` | stills-in-motion, slow pan/zoom, sepia, letter narration | history built from photographs |

### Journalistic family — meaning carried by evidence
| Skill | Style | Use when |
|---|---|---|
| `investigative-doc` | evidence-led reconstruction, documents/data on screen, multicam sync | accountability, public-interest, Frontline/ProPublica register |
| `true-crime-doc` | thriller structure, hook episode, ticking clock, low-res surveillance | true-crime features and docuseries |
| `bodycam-evidence-doc` | raw institutional footage, no VO, meet the materials where they are | the footage itself is the story |
| `immersive-field-doc` | embedded first-person reportage, handheld, access-led | field reporting, conflict, subcultures |

### Cinematic family — meaning carried by character and polish
| Skill | Style | Use when |
|---|---|---|
| `netflix-docuseries` | streaming house style, Slow Media, episodic cliffhangers, character-led | personality docs, premium non-fiction series |
| `nature-wildlife-doc` | blue-chip natural history, awe-led, character-framed animals | wildlife, ecosystems, conservation |
| `op-docs-short` | short prestige documentary, form-forward, one focused story, <20 min | opinion docs, festival shorts |
| `documentary-film` (existing) | general observational/interview-led documentary | the default documentary craft |

### Form-forward family — meaning carried by form itself
| Skill | Style | Use when |
|---|---|---|
| `animated-documentary` | rotoscope / illustrated, animation as a storytelling tool | no footage exists, or the truth is internal |
| `docudrama-reenactment` | dramatized reconstruction, testimony + acted scenes, labelled | the event was never filmed |
| `essay-film` | first-person inquiry, lateral montage, motif recurrence | personal essays, meditative non-fiction |

---

## D · The style selector (a quick decision tree)

1. **Is there footage of the event?**
   - Yes, behaviour → `documentary-film` (observational) or `immersive-field-doc`.
   - Yes, evidence → `investigative-doc`, `true-crime-doc`, `bodycam-evidence-doc`.
   - Yes, character/life → `netflix-docuseries` or `op-docs-short`.
   - Yes, wildlife → `nature-wildlife-doc`.
   - No, only stills → `ken-burns-archival`.
   - No, only archive film → `archival-essay-doc`.
   - No, only testimony/memory → `animated-documentary`, `docudrama-reenactment`, `essay-film`.
2. **What carries the meaning?**
   - A graphic/argument → `vox-explainer`, `archival-essay-doc`.
   - A place → `geo-explainer-maps`.
   - A number/data → `investigative-doc`, `vox-explainer`.
3. **What is the platform?**
   - Long-form streaming → `netflix-docuseries`.
   - Short digital → `op-docs-short`, `vox-explainer`.

## E · Ethics that hold across every documentary skill (non-negotiable)
- **No fabricated quotes, statistics or attributions** — verify against source.
- **Label every recreation, animation and composite.** Where a style's ethics
  require a label (re-enactment, composite animal, actors used), the label is
  mandatory.
- **Never manufacture a confession** (true crime) and **never distort meaning**
  when combining footage (nature).
- **Consent and dignity** — do not retraumatise; protect sources.
- **The audience contract** — people should never feel tricked. With clarity,
  you earn the freedom to take big creative leaps.

## F · The craft features still apply
Every documentary skill carries the **MANDATORY FEATURE USE-CASES** (the modern
standard) and the **Visual Narration Layer** — but tuned to the style: restrained
in observational and essay work, full-strength in explainers and reels. The style
governs **how** the features look, never **whether** they are used where the
concept needs them.
