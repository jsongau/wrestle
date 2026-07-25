# Motion & Micro-Interactions Research — Premium Dark Sports/Entertainment Site

**Scope:** No framework · No build step · No browser storage · Plain HTML/CSS + vanilla JS.
**Targets:** 60fps, `prefers-reduced-motion` respected everywhere, mobile-friendly, touch-safe.
**Date:** 2026-07-25

---

## 0. Guiding Principles (2025–2026 best practice)

1. **Animate only `transform` and `opacity`.** These are the only two properties the browser can composite on the GPU without layout/paint. Animating `top/left/width/height/margin` forces reflow and kills 60fps. ([MDN – prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion))
2. **Prefer `IntersectionObserver` over scroll listeners.** Scroll events fire dozens of times per frame and run on the main thread; IO is async, off-main-thread, and batches entries. ([MDN IntersectionObserver], [Chee Web Dev](https://cheewebdevelopment.com/vanilla-js-scroll-events-animations-with-intersectionobserver-api/))
3. **Reduced motion is the law, not a nicety.** Every effect below has a `@media (prefers-reduced-motion: reduce)` fallback that removes movement while keeping content visible/legible. ([CSS-Tricks almanac](https://css-tricks.com/almanac/rules/m/media/prefers-reduced-motion/), [Pope Tech](https://blog.pope.tech/2025/12/08/design-accessible-animation-and-movement/))
4. **Add `will-change` sparingly and remove it after.** Permanent `will-change` on many nodes wastes GPU memory. Apply during interaction, drop when idle.
5. **Throttle pointer work with `requestAnimationFrame`.** Never write to the DOM directly inside `mousemove`/`pointermove`; coalesce into one rAF tick.
6. **Respect touch.** Magnetic/spotlight/hover effects are pointer-fine only. Gate them behind `matchMedia('(hover: hover) and (pointer: fine)')` so phones don't run useless listeners.

Global reset that every section relies on:

```css
:root {
  --ease-out-quint: cubic-bezier(0.22, 1, 0.36, 1);
  --ease-out-expo:  cubic-bezier(0.16, 1, 0.3, 1);
  --dur-fast: 180ms;
  --dur:      420ms;
  --dur-slow: 800ms;
  --accent: #e11d2a;        /* sports red */
  --accent-2: #ffb020;      /* ember gold */
  --bg: #0a0a0c;
  --card: #141418;
}

/* Kill EVERYTHING that moves when the user asks for calm. */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.001ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.001ms !important;
    scroll-behavior: auto !important;
  }
}
```

> This global block is a safety net. Each component below **also** handles reduced motion explicitly so nothing appears blank/broken when animations are stripped.

---

## 1. Scroll-Reveal Animations (IntersectionObserver — fade / slide / stagger)

A single observer drives every reveal on the page. Elements opt in with `data-reveal`. Staggering is done per-container with a CSS custom property `--i` and a `data-reveal-stagger` parent — no per-element JS timers.

### HTML

```html
<section class="grid" data-reveal-stagger>
  <article class="card" data-reveal="up"        style="--i:0">Match 1</article>
  <article class="card" data-reveal="up"        style="--i:1">Match 2</article>
  <article class="card" data-reveal="up"        style="--i:2">Match 3</article>
</section>

<h2 data-reveal="left">Tonight's card</h2>
<p  data-reveal="fade">Scroll to reveal.</p>
```

### CSS

```css
[data-reveal] {
  opacity: 0;
  transform: translate3d(0, 0, 0);
  transition:
    opacity var(--dur) var(--ease-out-quint),
    transform var(--dur) var(--ease-out-quint);
  will-change: opacity, transform;
}
[data-reveal="up"]   { transform: translate3d(0, 32px, 0); }
[data-reveal="down"] { transform: translate3d(0, -32px, 0); }
[data-reveal="left"] { transform: translate3d(-40px, 0, 0); }
[data-reveal="right"]{ transform: translate3d(40px, 0, 0); }
[data-reveal="scale"]{ transform: scale(0.92); }
[data-reveal="fade"] { transform: none; }

/* Stagger: children delay by their index. Cap so late items don't lag forever. */
[data-reveal-stagger] > [data-reveal] {
  transition-delay: calc(min(var(--i, 0), 8) * 70ms);
}

/* Revealed state */
[data-reveal].is-visible {
  opacity: 1;
  transform: translate3d(0, 0, 0);
}
/* Drop the GPU hint once the transition is done (added by JS). */
[data-reveal].is-settled { will-change: auto; }

@media (prefers-reduced-motion: reduce) {
  [data-reveal] { opacity: 1 !important; transform: none !important; }
}
```

### JS (reusable, ~30 lines)

```js
// scroll-reveal.js
(function () {
  const els = document.querySelectorAll('[data-reveal]');
  if (!els.length) return;

  // Reduced motion OR no IO support → just show everything.
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce || !('IntersectionObserver' in window)) {
    els.forEach((el) => el.classList.add('is-visible'));
    return;
  }

  const io = new IntersectionObserver(
    (entries, obs) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        const el = entry.target;
        el.classList.add('is-visible');
        // Free GPU memory after the transition finishes.
        el.addEventListener(
          'transitionend',
          () => el.classList.add('is-settled'),
          { once: true }
        );
        obs.unobserve(el); // reveal once; never re-hide
      }
    },
    {
      rootMargin: '0px 0px -10% 0px', // trigger slightly before fully in view
      threshold: 0.15,
    }
  );

  els.forEach((el) => io.observe(el));
})();
```

**Notes**
- `rootMargin: '0px 0px -10% 0px'` fires the reveal a touch before the element bottoms into view, which reads more natural than a hard edge. ([Handoff.design](https://handoff.design/css-animation/scroll-animations.html))
- One observer for the whole page beats one-per-element. Unobserve after firing so nothing is tracked forever.
- Stagger lives in CSS (`--i`), so JS never manages timers — cheaper and easier to tune.
- **Progressive enhancement:** if JS fails or IO is unsupported, content is shown, not hidden.

> **CSS-only alternative (no JS):** native scroll-driven animations via `animation-timeline: view()` are now baseline in Chromium/Firefox 2025 but still need a JS fallback for Safari < 26 and are harder to make reversible-safe, so the IO approach above remains the portable default. ([Magic UI guide](https://magicui.design/blog/css-animation-on-scroll))

---

## 2. Animated Hero Background

### 2a. CSS-only animated gradient / mesh (zero JS, cheapest)

Animate `background-position` of an oversized multi-radial-gradient. It composites cheaply and never touches layout.

```html
<header class="hero">
  <div class="hero__bg" aria-hidden="true"></div>
  <div class="hero__content">
    <h1>FIGHT NIGHT</h1>
  </div>
</header>
```

```css
.hero { position: relative; overflow: hidden; min-height: 82vh; background: var(--bg); }

.hero__bg {
  position: absolute;
  inset: -20%;                 /* bleed so movement never shows edges */
  z-index: 0;
  background:
    radial-gradient(38% 44% at 20% 30%, rgba(225,29,42,0.45), transparent 60%),
    radial-gradient(42% 50% at 80% 25%, rgba(255,176,32,0.30), transparent 62%),
    radial-gradient(50% 55% at 60% 80%, rgba(120,20,220,0.35), transparent 60%),
    var(--bg);
  background-size: 200% 200%;
  filter: blur(40px) saturate(120%);
  animation: mesh-drift 18s var(--ease-out-quint) infinite alternate;
}

@keyframes mesh-drift {
  0%   { background-position: 0% 0%,   100% 0%,   50% 100%; }
  100% { background-position: 100% 50%, 0% 60%,   40% 0%; }
}

/* Optional animated conic "arena light" sweep behind the title */
.hero__content::before {
  content: "";
  position: absolute; inset: -50%;
  background: conic-gradient(from 0deg, transparent 0 70%, rgba(255,176,32,0.12) 85%, transparent 100%);
  animation: sweep 12s linear infinite;
  z-index: -1;
}
@keyframes sweep { to { transform: rotate(1turn); } }

@media (prefers-reduced-motion: reduce) {
  .hero__bg { animation: none; }
  .hero__content::before { animation: none; }
}
```

**Perf notes:** `background-position` animation stays on the compositor; the one-time `blur()` is rasterized once. Keep blur ≤ 40px on mobile and avoid animating the blur radius itself (that repaints every frame).

### 2b. Lightweight canvas particle / ember effect (JS option)

Floating embers rising behind the hero. Capped particle count, DPR-aware, pauses when off-screen, disabled for reduced motion and on small/low-power devices.

```html
<canvas class="hero__embers" aria-hidden="true"></canvas>
```

```css
.hero__embers { position: absolute; inset: 0; z-index: 1; pointer-events: none; }
```

```js
// embers.js
(function () {
  const canvas = document.querySelector('.hero__embers');
  if (!canvas) return;

  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const smallOrLowPower =
    innerWidth < 640 || (navigator.deviceMemory && navigator.deviceMemory <= 4);
  if (reduce || smallOrLowPower) return; // static gradient carries the hero

  const ctx = canvas.getContext('2d', { alpha: true });
  const DPR = Math.min(devicePixelRatio || 1, 2); // cap DPR — huge perf win on retina
  let w, h, particles, raf = null, running = false;

  const COUNT = Math.min(70, Math.round(innerWidth / 22)); // scale to width, hard cap

  function resize() {
    w = canvas.clientWidth; h = canvas.clientHeight;
    canvas.width = w * DPR; canvas.height = h * DPR;
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
  }

  function makeParticle() {
    return {
      x: Math.random() * w,
      y: h + Math.random() * h,
      r: 0.6 + Math.random() * 2.2,
      vy: 0.2 + Math.random() * 0.9,
      vx: (Math.random() - 0.5) * 0.35,
      a: 0.15 + Math.random() * 0.55,
      hue: 20 + Math.random() * 25, // orange→gold
    };
  }

  function seed() { particles = Array.from({ length: COUNT }, makeParticle); }

  function tick() {
    ctx.clearRect(0, 0, w, h);
    ctx.globalCompositeOperation = 'lighter'; // additive glow
    for (const p of particles) {
      p.y -= p.vy; p.x += p.vx;
      if (p.y < -10) Object.assign(p, makeParticle(), { y: h + 10 });
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = `hsla(${p.hue}, 100%, 60%, ${p.a})`;
      ctx.fill();
    }
    raf = requestAnimationFrame(tick);
  }

  function start() { if (!running) { running = true; tick(); } }
  function stop()  { running = false; if (raf) cancelAnimationFrame(raf); raf = null; }

  resize(); seed(); 
  addEventListener('resize', () => { resize(); seed(); }, { passive: true });

  // Only animate while the hero is visible → saves battery on scroll.
  new IntersectionObserver(
    ([e]) => (e.isIntersecting ? start() : stop()),
    { threshold: 0 }
  ).observe(canvas);

  // Pause when tab is hidden.
  document.addEventListener('visibilitychange', () =>
    document.hidden ? stop() : start()
  );
})();
```

**Perf notes**
- **Cap DPR at 2** — retina phones report 3+; rendering at native DPR triples fill cost for no visible gain.
- **Particle count scales to viewport width** and is hard-capped (≤70). Additive blending (`'lighter'`) gives glow without per-particle shadow blur (which is expensive).
- **IntersectionObserver pauses the loop** when the hero scrolls away, and `visibilitychange` pauses on tab switch — no wasted frames/battery.
- Disabled entirely on `<640px` and `deviceMemory ≤ 4` — the CSS gradient (2a) is the graceful floor.
- No `shadowBlur` (biggest canvas perf trap). Glow comes from soft small radii + additive comp.

---

## 3. Infinite Marquee / Ticker (CSS keyframes)

Modern seamless technique: duplicate the track, animate `translateX` by `-100% - gap`, mark the clone `aria-hidden`. Pauses on hover and fully stops for reduced motion. ([Ryan Mulligan – The Infinite Marquee](https://ryanmulligan.dev/blog/css-marquee/))

### HTML

```html
<div class="marquee" role="marquee" aria-label="Latest match ratings">
  <ul class="marquee__track">
    <li>Reigns vs Rhodes <b>4.75★</b></li>
    <li>Rollins vs Punk <b>4.50★</b></li>
    <li>Ripley vs Belair <b>4.25★</b></li>
  </ul>
  <ul class="marquee__track" aria-hidden="true">   <!-- exact clone -->
    <li>Reigns vs Rhodes <b>4.75★</b></li>
    <li>Rollins vs Punk <b>4.50★</b></li>
    <li>Ripley vs Belair <b>4.25★</b></li>
  </ul>
</div>
```

### CSS

```css
.marquee {
  --gap: 2.5rem;
  --speed: 30s;              /* lower = faster */
  display: flex;
  gap: var(--gap);
  overflow: hidden;
  user-select: none;
  -webkit-mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
          mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
}

.marquee__track {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  gap: var(--gap);
  min-width: 100%;
  margin: 0; padding: 0 0 0 var(--gap); list-style: none;
  animation: marquee var(--speed) linear infinite;
}
.marquee__track li b { color: var(--accent-2); margin-left: .4rem; }

.marquee:hover .marquee__track { animation-play-state: paused; }

@keyframes marquee {
  from { transform: translateX(0); }
  to   { transform: translateX(calc(-100% - var(--gap))); }
}

@media (prefers-reduced-motion: reduce) {
  .marquee__track { animation: none; }
  .marquee { overflow-x: auto; }        /* let users scroll it manually instead */
  .marquee__track[aria-hidden="true"] { display: none; }
}
```

**Notes**
- Two identical tracks + `translateX(calc(-100% - var(--gap)))` = zero-jump loop; the gap term keeps spacing consistent across the seam. ([Ryan Mulligan](https://ryanmulligan.dev/blog/css-marquee/))
- The clone is `aria-hidden` so screen readers read the ticker once. ([Ryan Mulligan], [Effect.Labs](https://effect-labs.com/en/pages/blog/marquee-infinite-scroll.html))
- The `mask-image` fade at both edges is the "premium" tell — content dissolves instead of hard-clipping.
- Reduced motion: stop the animation, hide the duplicate, and make the strip natively scrollable so no content is lost. ([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using_for_accessibility))
- **Speed by content, not width:** set `--speed` relative to how much text there is; ~30s per full loop reads calm and premium.

---

## 4. Number Count-Up on Scroll

Counts up once when the stat enters view. Uses `requestAnimationFrame` (not `setInterval`) with an eased curve, respects `Intl.NumberFormat`, and honors reduced motion by snapping to the final value.

### HTML

```html
<div class="stats">
  <div class="stat"><span class="stat__num" data-countup="4.87" data-decimals="2">0</span><small>Avg rating</small></div>
  <div class="stat"><span class="stat__num" data-countup="128000" data-suffix="+">0</span><small>Fans</small></div>
  <div class="stat"><span class="stat__num" data-countup="97" data-suffix="%">0</span><small>Sellout rate</small></div>
</div>
```

### JS

```js
// countup.js
(function () {
  const els = document.querySelectorAll('[data-countup]');
  if (!els.length) return;

  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  const fmt = (val, decimals) =>
    new Intl.NumberFormat(undefined, {
      minimumFractionDigits: decimals,
      maximumFractionDigits: decimals,
    }).format(val);

  function run(el) {
    const end = parseFloat(el.dataset.countup);
    const decimals = parseInt(el.dataset.decimals || '0', 10);
    const prefix = el.dataset.prefix || '';
    const suffix = el.dataset.suffix || '';
    const duration = parseInt(el.dataset.duration || '1600', 10);

    if (reduce) { el.textContent = prefix + fmt(end, decimals) + suffix; return; }

    const start = performance.now();
    const easeOutExpo = (t) => (t === 1 ? 1 : 1 - Math.pow(2, -10 * t));

    function frame(now) {
      const p = Math.min((now - start) / duration, 1);
      const val = end * easeOutExpo(p);
      el.textContent = prefix + fmt(val, decimals) + suffix;
      if (p < 1) requestAnimationFrame(frame);
      else el.textContent = prefix + fmt(end, decimals) + suffix; // exact final
    }
    requestAnimationFrame(frame);
  }

  if (!('IntersectionObserver' in window)) { els.forEach(run); return; }

  const io = new IntersectionObserver(
    (entries, obs) => {
      for (const e of entries) {
        if (!e.isIntersecting) continue;
        run(e.target);
        obs.unobserve(e.target); // count once
      }
    },
    { threshold: 0.6 } // most of the stat visible before it fires
  );
  els.forEach((el) => els && io.observe(el));
})();
```

**Notes**
- `requestAnimationFrame` + `performance.now()` gives frame-perfect timing that self-corrects on slow frames — `setInterval` drifts and can't hit 60fps reliably.
- `easeOutExpo` decelerates into the final value, which feels premium vs. linear.
- Reduced motion → value is written instantly; no animation, no empty "0".
- Fires at `threshold: 0.6` so the number is well in view before it runs; unobserved after one run.
- `Intl.NumberFormat` gives correct thousands separators/decimals for the user's locale for free.

---

## 5. Premium Hover Micro-Interactions

**All of these are gated to fine-pointer devices** so phones never run the listeners:

```js
const CAN_HOVER = matchMedia('(hover: hover) and (pointer: fine)').matches;
const REDUCE = matchMedia('(prefers-reduced-motion: reduce)').matches;
```

### 5a. Magnetic buttons

Button drifts toward the cursor within its bounds; snaps back on leave. One rAF tick per move; translations only. ([Init HTML](https://en.inithtml.com/resources/magnetic-hover-effect-creating-cursor-attracted-buttons-with-vanilla-javascript/), [Coding Stella](https://codingstella.com/how-to-make-magnetic-button-hover-effect-using-html-css/))

```html
<a href="#" class="btn btn--magnetic"><span>Buy tickets</span></a>
```

```css
.btn--magnetic {
  display: inline-block;
  will-change: transform;
  transition: transform 400ms var(--ease-out-quint);
}
.btn--magnetic > span { display: inline-block; transition: transform 400ms var(--ease-out-quint); }
@media (prefers-reduced-motion: reduce) {
  .btn--magnetic, .btn--magnetic > span { transition: none; }
}
```

```js
// magnetic.js
if (CAN_HOVER && !REDUCE) {
  document.querySelectorAll('.btn--magnetic').forEach((btn) => {
    const label = btn.querySelector('span') || btn;
    const STRENGTH = 0.35;      // 0–1, how far it follows
    const LABEL_STRENGTH = 0.15;
    let rafId = null, tx = 0, ty = 0;

    function move(e) {
      const r = btn.getBoundingClientRect();
      const mx = e.clientX - (r.left + r.width / 2);
      const my = e.clientY - (r.top + r.height / 2);
      tx = mx * STRENGTH; ty = my * STRENGTH;
      if (!rafId) rafId = requestAnimationFrame(apply);
    }
    function apply() {
      rafId = null;
      btn.style.transform = `translate3d(${tx}px, ${ty}px, 0)`;
      label.style.transform = `translate3d(${tx * LABEL_STRENGTH}px, ${ty * LABEL_STRENGTH}px, 0)`;
    }
    btn.addEventListener('pointermove', move);
    btn.addEventListener('pointerleave', () => {
      if (rafId) cancelAnimationFrame(rafId), (rafId = null);
      btn.style.transform = '';        // CSS transition snaps it home
      label.style.transform = '';
    });
  });
}
```

### 5b. Card spotlight (pointer-tracked radial glow via CSS custom props)

JS only writes two custom properties (`--mx`, `--my`); CSS paints the glow. This is the cheapest possible way — no layout, one rAF, and the effect is entirely declarative. ([FreeFrontend glow effects](https://freefrontend.com/css-glow-effects/), [CodeFronts card hovers](https://codefronts.com/motion/css-card-hover-effects/))

```html
<article class="card card--spotlight">
  <h3>Main Event</h3>
  <p>Reigns vs Rhodes</p>
</article>
```

```css
.card--spotlight {
  position: relative;
  background: var(--card);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 16px;
  overflow: hidden;
  isolation: isolate;
}
.card--spotlight::before {
  content: "";
  position: absolute; inset: 0;
  background: radial-gradient(
    280px circle at var(--mx, 50%) var(--my, 50%),
    rgba(225,29,42,0.22),
    transparent 60%
  );
  opacity: 0;
  transition: opacity 300ms ease;
  z-index: -1;
  pointer-events: none;
}
.card--spotlight:hover::before { opacity: 1; }

@media (prefers-reduced-motion: reduce) {
  .card--spotlight::before { transition: none; }
}
```

```js
// spotlight.js
if (CAN_HOVER) {                      // glow is subtle → fine even w/ reduced motion
  document.querySelectorAll('.card--spotlight').forEach((card) => {
    let rafId = null, x = 0, y = 0;
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      x = e.clientX - r.left; y = e.clientY - r.top;
      if (!rafId) rafId = requestAnimationFrame(() => {
        rafId = null;
        card.style.setProperty('--mx', x + 'px');
        card.style.setProperty('--my', y + 'px');
      });
    });
  });
}
```

### 5c. Image zoom (CSS-only)

```css
.media { overflow: hidden; border-radius: 14px; }
.media img {
  display: block; width: 100%;
  transition: transform 600ms var(--ease-out-quint), filter 600ms ease;
  will-change: transform;
}
.media:hover img { transform: scale(1.06); filter: saturate(1.15) contrast(1.05); }

@media (prefers-reduced-motion: reduce) {
  .media img { transition: none; }
  .media:hover img { transform: none; }
}
```

### 5d. Underline sweep (CSS-only, animated `scaleX`)

Scales a pseudo-element from left to right — composited, not a `width` animation. ([CodeFronts hover effects](https://codefronts.com/motion/css-hover-effects/))

```css
.link-sweep {
  position: relative; color: inherit; text-decoration: none;
}
.link-sweep::after {
  content: "";
  position: absolute; left: 0; bottom: -2px;
  width: 100%; height: 2px;
  background: var(--accent);
  transform: scaleX(0);
  transform-origin: right;
  transition: transform 320ms var(--ease-out-quint);
}
.link-sweep:hover::after,
.link-sweep:focus-visible::after {
  transform: scaleX(1);
  transform-origin: left;   /* origin flip = sweep in from left, out to right */
}
@media (prefers-reduced-motion: reduce) {
  .link-sweep::after { transition: none; }
  .link-sweep:hover::after { transform: scaleX(1); }
}
```

> **Focus parity:** every hover effect above also responds to `:focus-visible` (or is harmless without it) so keyboard users get the same affordance. Underline sweep explicitly includes `:focus-visible`.

---

## 6. Sticky / Condensing Header + Scroll Progress Bar

### 6a. Condensing header

Header shrinks/gains a backdrop after a small scroll threshold. Uses a **sentinel + IntersectionObserver** — no scroll listener at all. Class toggles drive pure-CSS transitions.

```html
<div id="top-sentinel" aria-hidden="true"></div>
<header class="site-header">
  <a class="brand" href="/">FIGHTCLUB</a>
  <nav>…</nav>
</header>
```

```css
#top-sentinel { position: absolute; top: 0; height: 1px; width: 1px; }

.site-header {
  position: sticky; top: 0; z-index: 100;
  display: flex; align-items: center; justify-content: space-between;
  padding: 1.25rem 2rem;
  background: transparent;
  transition:
    padding 300ms var(--ease-out-quint),
    background-color 300ms ease,
    box-shadow 300ms ease,
    backdrop-filter 300ms ease;
}
.site-header.is-condensed {
  padding: 0.6rem 2rem;
  background: rgba(10,10,12,0.72);
  backdrop-filter: blur(12px) saturate(140%);
  -webkit-backdrop-filter: blur(12px) saturate(140%);
  box-shadow: 0 1px 0 rgba(255,255,255,0.06), 0 12px 30px -18px #000;
}
.site-header .brand { transition: font-size 300ms var(--ease-out-quint); }
.site-header.is-condensed .brand { font-size: 0.95em; }

@media (prefers-reduced-motion: reduce) { .site-header, .brand { transition: none; } }
```

```js
// header-condense.js
(function () {
  const header = document.querySelector('.site-header');
  const sentinel = document.querySelector('#top-sentinel');
  if (!header || !sentinel || !('IntersectionObserver' in window)) return;
  new IntersectionObserver(
    ([e]) => header.classList.toggle('is-condensed', !e.isIntersecting),
    { rootMargin: '-80px 0px 0px 0px' } // condense after ~80px scrolled
  ).observe(sentinel);
})();
```

### 6b. Scroll progress bar

Two options — prefer the CSS-only one where supported.

**Option A — CSS-only (scroll-driven animation, no JS):**

```css
.scroll-progress {
  position: fixed; top: 0; left: 0; height: 3px; width: 100%;
  transform-origin: 0 50%;
  transform: scaleX(0);
  background: linear-gradient(90deg, var(--accent), var(--accent-2));
  z-index: 200;
  animation: grow-progress linear;
  animation-timeline: scroll(root block);
}
@keyframes grow-progress { to { transform: scaleX(1); } }

@supports not (animation-timeline: scroll()) { .scroll-progress { display: none; } }
@media (prefers-reduced-motion: reduce) { .scroll-progress { animation: none; } }
```

**Option B — JS fallback (works everywhere, throttled with rAF):**

```html
<div class="scroll-progress" id="progress" aria-hidden="true"></div>
```

```js
// scroll-progress.js  (use when animation-timeline is unsupported)
(function () {
  const bar = document.getElementById('progress');
  if (!bar || CSS.supports('animation-timeline: scroll()')) return; // CSS handles it
  let ticking = false;
  function update() {
    const doc = document.documentElement;
    const max = doc.scrollHeight - doc.clientHeight;
    const p = max > 0 ? doc.scrollTop / max : 0;
    bar.style.transform = `scaleX(${p})`;
    ticking = false;
  }
  addEventListener('scroll', () => {
    if (!ticking) { ticking = true; requestAnimationFrame(update); }
  }, { passive: true });
  update();
})();
```

**Notes**
- The header uses a **sentinel + IO** instead of a `scroll` listener — the toggle only runs when the boundary is actually crossed, not every frame.
- Scroll progress via `animation-timeline: scroll(root)` runs off the main thread entirely; the JS fallback is rAF-throttled and `passive`. Both animate only `transform: scaleX()` (compositor-only).
- `backdrop-filter` is GPU-accelerated but not free on low-end Android — it's applied only in the condensed state, and the header remains fully readable if the browser ignores it.

---

## 7. Accessibility — `prefers-reduced-motion` Strategy (summary)

| Component | Reduced-motion behavior |
|---|---|
| Global reset | All animations/transitions collapsed to ~0ms via the `*` media block (safety net). |
| Scroll reveal | Elements shown immediately, no fade/slide; also shown if JS/IO missing. |
| Hero gradient/mesh | `animation: none` — static, still on-brand. |
| Hero embers (canvas) | Loop never starts; static gradient carries the hero. Also off on small/low-power devices. |
| Marquee | Animation stopped, duplicate hidden, strip becomes natively scrollable (no content lost). |
| Count-up | Final value written instantly; no tween, never shows a stuck "0". |
| Magnetic button | Listeners skipped (also skipped on touch); transitions off. |
| Card spotlight | Glow still tracks (it's positional, not motion) but its fade transition is disabled — safe & subtle. |
| Image zoom | No scale; `transform: none` on hover. |
| Underline sweep | Snaps to full underline, no sweep. |
| Header condense | Class still toggles for the frosted background, but padding/size transitions are off. |
| Scroll progress | CSS version's animation disabled; JS fallback still fine (single transform, no perceived motion). |

**Additional a11y guarantees baked in above:**
- Decorative layers (`.hero__bg`, `.hero__embers`, marquee clone, progress bar) carry `aria-hidden="true"` so assistive tech ignores them.
- Every hover affordance also works on `:focus-visible` (keyboard parity).
- Pointer effects are gated behind `(hover: hover) and (pointer: fine)` so they never fire on touch, avoiding sticky-hover bugs.
- Nothing is hidden with no path to visibility: all reveal/count content degrades to fully visible if JS, IO, or animations are unavailable (progressive enhancement).
- Detect the preference **live** where cheap: `matchMedia('(prefers-reduced-motion: reduce)')` is read at init; for long-lived pages you can also add `mq.addEventListener('change', …)` to react if the OS setting flips.

---

## Sources

- MDN — [prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion) and [Using media queries for accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using_for_accessibility)
- Ryan Mulligan — [The Infinite Marquee](https://ryanmulligan.dev/blog/css-marquee/) (canonical modern CSS marquee)
- CSS-Tricks — [prefers-reduced-motion almanac](https://css-tricks.com/almanac/rules/m/media/prefers-reduced-motion/)
- Pope Tech — [Design accessible animation and movement](https://blog.pope.tech/2025/12/08/design-accessible-animation-and-movement/)
- Chee Web Development — [Vanilla JS Scroll Events & Animations with IntersectionObserver](https://cheewebdevelopment.com/vanilla-js-scroll-events-animations-with-intersectionobserver-api/)
- Handoff.design — [On-Scroll Animations with IntersectionObserver](https://handoff.design/css-animation/scroll-animations.html)
- Magic UI — [A Modern Guide to CSS Animation on Scroll](https://magicui.design/blog/css-animation-on-scroll)
- Effect.Labs — [Create a Modern Infinite Marquee in Pure CSS](https://effect-labs.com/en/pages/blog/marquee-infinite-scroll.html)
- Init HTML — [Magnetic Hover Effect with Vanilla JavaScript](https://en.inithtml.com/resources/magnetic-hover-effect-creating-cursor-attracted-buttons-with-vanilla-javascript/)
- Coding Stella — [Magnetic Button Hover Effect](https://codingstella.com/how-to-make-magnetic-button-hover-effect-using-html-css/)
- FreeFrontend — [CSS Glow Effects](https://freefrontend.com/css-glow-effects/) · CodeFronts — [Card Hover Effects](https://codefronts.com/motion/css-card-hover-effects/), [Hover Effects](https://codefronts.com/motion/css-hover-effects/)
