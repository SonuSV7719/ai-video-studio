# Editorial Precision & Animation Physics Standards

This reference details the core technical laws for senior video editors, motion designers, and audio engineers operating within `ai-video-studio`.

---

## 1. Editorial Rules of Assembly

### Rule 1.1: Cutting on Action
- When transitioning between talking head and B-roll or wide to close-up, place the cut precisely **during** a physical movement (a head tilt, a hand gesture, or an eyelid blink).
- Cutting on action hides the visual disruption and registers in the human brain as continuous motion.

### Rule 1.2: The Eye-Trace Law
- Viewers naturally fixate on the most contrastive or moving element (usually the speaker's eyes or a highlighted word).
- When cutting from Scene A to Scene B, align the incoming focal point with the outgoing focal point. Never force the viewer's eyes to snap across opposite screen quadrants without a guiding graphic motion.

### Rule 1.3: Jump-Cut Audio Smoothing & Dead Air Elimination
- Use `tools/analyze_silence.py` to identify micro-pauses greater than 250ms in spoken dialogue.
- When splicing dialogue takes together, apply a **2-frame (10ms) crossfade** on the audio track. Splicing raw audio without a crossfade produces audible DC offset clicks.

### Rule 1.4: Broadcast Dialogue Leveling
- Always normalize dialogue tracks via FFmpeg's dynamic audio normalizer:
  ```bash
  ffmpeg -i raw_take.wav -af "dynaudnorm=f=150:g=15:p=0.95:m=10.0" -ar 48000 leveled_take.wav
  ```
- Target broadcast loudness standard: **-14 LUFS** for online social video, **-16 LUFS** for documentary/YouTube. Maximum True Peak must not exceed **-1.0 dBFS**.

---

## 2. Motion Graphics & Physics Animation Rules

### Rule 2.1: Natural Spring Physics over Linear Easing
Linear animation (`t = frame / total`) looks artificial and robotic. Professional motion graphics use damped harmonic oscillation:

* **Anime.js Spring Formulation**:
  ```javascript
  anime({
    targets: '.ui-card',
    translateY: [-60, 0],
    opacity: [0, 1],
    easing: 'spring(1, 90, 14, 0)', // mass: 1, stiffness: 90, damping: 14, velocity: 0
  });
  ```
* **GSAP Physics Elastic Formulation**:
  ```javascript
  gsap.from('.metric-badge', {
    scale: 0.6,
    opacity: 0,
    duration: 0.8,
    ease: 'elastic.out(1, 0.4)'
  });
  ```

### Rule 2.2: Staggered Micro-Delays
Never animate multiple sibling elements simultaneously:
- **Letters in a Title**: 25ms to 40ms stagger per character (`delay: anime.stagger(30)`).
- **Cards in a Grid**: 60ms to 90ms stagger per card (`delay: anime.stagger(80)`).
- **Lines in a List / Code Block**: 120ms to 180ms stagger per line.

### Rule 2.3: SVG Stroke Drawing (Handwriting & Diagram Architecture)
When rendering flowcharts, architecture lines, or signatures:
```javascript
anime({
  targets: 'path.connection-line',
  strokeDashoffset: [anime.setDashoffset, 0],
  easing: 'easeInOutCubic',
  duration: 1200,
  delay: anime.stagger(200)
});
```

---

## 3. Remotion Architectural Rules

### Rule 3.1: Sequence Local Clock Law
Inside Remotion's `<Sequence from={T}>`, child components evaluate `useCurrentFrame()` **relative to T**.

```tsx
// ❌ WRONG: Double-offset bug that causes frozen playback
<Sequence from={60} durationInFrames={90}>
  <OffthreadVideo src={clip} startFrom={60} />
</Sequence>

// ✅ CORRECT: Evaluated locally within the sequence boundary
<Sequence from={60} durationInFrames={90}>
  <OffthreadVideo src={clip} />
</Sequence>
```

### Rule 3.2: Exact Framerate Locking (CFR)
- Vertical iPhone footage is recorded in Variable Frame Rate (VFR) by default.
- Always transcode raw camera footage to Constant Frame Rate (CFR) before loading into Remotion or OpenCV pipelines:
  ```bash
  ffmpeg -i raw_take.mov -r 30 -g 30 -tune fastdecode -c:v libx264 -crf 18 -pix_fmt yuv420p raw_footage/take_cfr30.mp4
  ```

---

## 4. Sound Design & Audio Sync Standards

### Rule 4.1: The 1-Frame Transient Rule
- A sound effect (whoosh, pop, impact, hit) must hit its maximum energy peak **1 frame before** or **exactly on** the visual cut.
- If audio arrives 2 frames after visual impact, human psychoacoustics perceive the video as "laggy" or desynchronized.

### Rule 4.2: Dialogue Ducking Architecture
- Never let background music or sound effects compete in the 1 kHz – 4 kHz speech clarity band.
- Whenever speech is active, duck background music by **-16 dB to -18 dB** with an attack time of **150ms** and a decay/release of **400ms**.
