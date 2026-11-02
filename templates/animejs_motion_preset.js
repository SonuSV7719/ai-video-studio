/**
 * Anime.js Motion Graphics Preset for AI Video Studio
 * Provides reusable animations: Staggered text, pop-up spring cards, SVG path draw, pulse
 * Docs: https://animejs.com/
 */

import anime from 'animejs';

export const MotionPresets = {
  // Staggered character reveal
  revealText: (selector, staggerMs = 35) => {
    return anime({
      targets: `${selector} .char`,
      translateY: ['1.2em', 0],
      opacity: [0, 1],
      duration: 650,
      delay: anime.stagger(staggerMs, { from: 'first' }),
      easing: 'easeOutExpo',
    });
  },

  // Spring card pop-up with slight tilt
  popUpCard: (selector, delayMs = 0) => {
    return anime({
      targets: selector,
      scale: [0.75, 1.0],
      translateY: [60, 0],
      rotateZ: [-6, 0],
      opacity: [0, 1],
      duration: 850,
      delay: delayMs,
      easing: 'spring(1, 90, 14, 0)',
    });
  },

  // Rhythmic heartbeat double-thump
  heartPulse: (selector) => {
    const tl = anime.timeline({ loop: true });
    tl.add({ targets: selector, scale: 1.18, duration: 120, easing: 'easeOutQuad' })
      .add({ targets: selector, scale: 1.0, duration: 130, easing: 'easeInQuad' })
      .add({ targets: selector, scale: 1.10, duration: 100, easing: 'easeOutQuad' })
      .add({ targets: selector, scale: 1.0, duration: 290, easing: 'easeInQuad' });
    return tl;
  },

  // SVG Line draw
  drawStroke: (selector, duration = 1500) => {
    return anime({
      targets: selector,
      strokeDashoffset: [anime.setDashoffset, 0],
      easing: 'easeInOutCubic',
      duration: duration,
    });
  }
};
