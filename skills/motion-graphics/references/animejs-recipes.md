# Anime.js Animation Recipes & Motion Patterns

Anime.js (`https://animejs.com/`) is a fast, multipurpose JavaScript animation engine ideal for procedural motion graphics, Remotion sequences, SVG path animations, and staggered kinetic typography.

---

## 1. Core Capabilities in AI Video Studio

| Animation Pattern | Anime.js Mechanism | Best Used For |
| :--- | :--- | :--- |
| **SVG Path Drawing** | `strokeDashoffset: [anime.setDashoffset, 0]` | Handwriting, animated line borders, signature flourishes |
| **Staggered Typography** | `delay: anime.stagger(40, { from: 'first' })` | Kinetic word-by-word and character-by-character reveals |
| **Elastic & Spring Physics** | `easing: 'spring(1, 80, 10, 0)'` | Pop-up cards, modal dialogs, playful badge drops |
| **SVG Morphing** | `d: [{ value: pathA }, { value: pathB }]` | Fluid organic shape transitions, morphing icons |
| **Timeline Orchestration** | `anime.timeline({ easing: 'easeOutExpo' })` | Multi-phase intro stings and scene transitions |

---

## 2. Production Code Recipes

### Recipe A: SVG Line Drawing & Handwriting Reveal
```javascript
import anime from 'animejs';

// Animate stroke outline of an SVG path or icon
anime({
  targets: '.svg-path-line',
  strokeDashoffset: [anime.setDashoffset, 0],
  easing: 'easeInOutSine',
  duration: 1500,
  delay: function(el, i) { return i * 250 },
  direction: 'alternate',
  loop: false
});
```

### Recipe B: Staggered Word / Character Kinetic Typography
```javascript
import anime from 'animejs';

// Wraps characters or words in <span> elements then staggers entry
anime.timeline({ loop: false })
  .add({
    targets: '.kinetic-text .letter',
    translateY: ["1.1em", 0],
    translateZ: 0,
    opacity: [0, 1],
    duration: 750,
    delay: anime.stagger(35, { from: 'center' }),
    easing: "easeOutExpo"
  });
```

### Recipe C: Multiplane Spring Bouncing Card
```javascript
import anime from 'animejs';

anime({
  targets: '.multiplane-card',
  scale: [0.85, 1.0],
  translateY: [40, 0],
  rotateZ: [-5, 0],
  opacity: [0, 1],
  duration: 900,
  easing: 'spring(1, 90, 12, 0)' // mass, stiffness, damping, initialVelocity
});
```

### Recipe D: Beat-Synchronized Heartbeat Pulse
```javascript
import anime from 'animejs';

// Double-thump systolic heartbeat on kick drums
const heartTimeline = anime.timeline({ loop: true, autoplay: true });
heartTimeline
  .add({
    targets: '.heart-icon',
    scale: 1.18,
    duration: 120,
    easing: 'easeOutQuad'
  })
  .add({
    targets: '.heart-icon',
    scale: 1.0,
    duration: 140,
    easing: 'easeInQuad'
  })
  .add({
    targets: '.heart-icon',
    scale: 1.10,
    duration: 100,
    easing: 'easeOutQuad'
  })
  .add({
    targets: '.heart-icon',
    scale: 1.0,
    duration: 290,
    easing: 'easeInQuad'
  });
```

---

## 3. Integration with Remotion & Canvas

Inside Remotion components, Anime.js can drive DOM element refs or pure JavaScript animation state on each frame or via standard React hooks:

```jsx
import React, { useEffect, useRef } from 'react';
import anime from 'animejs';

export const AnimatedHero = () => {
  const boxRef = useRef(null);

  useEffect(() => {
    anime({
      targets: boxRef.current,
      translateX: 250,
      rotate: '1turn',
      backgroundColor: '#FFC857',
      duration: 2000,
      easing: 'easeInOutQuad'
    });
  }, []);

  return <div ref={boxRef} className="hero-box" />;
};
```
