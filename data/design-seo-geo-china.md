# Modern Mobile-First, Ultra-Crawlable Sports/Database Fan Site — Build Reference

A concrete, copy-pasteable reference for a Sherdog/Tapology/Cagematch-style dark "arena" fan/database site.
Stack constraints: **hand-written HTML + CSS + vanilla JS only. No framework. No build step. No browser storage** (no `localStorage`/`sessionStorage`/cookies for state).

Last compiled: 2026-07 · Verify vendor specifics (embed URLs, license rules) before shipping.

---

## Table of Contents

1. [Design System](#1-design-system)
2. [Mobile-First + Performance](#2-mobile-first--performance)
3. [SEO (structured data, robots, sitemap, meta)](#3-seo)
4. [GEO — Generative Engine Optimization](#4-geo--generative-engine-optimization)
5. [China Market](#5-china-market)

---

## 1. Design System

Dark "arena" theme: near-black canvas, gold accent (championship/belt), red hot-accent (live/finish), steel neutrals. All tokens are CSS custom properties so you can theme once and reuse everywhere. No build step required — this is plain CSS.

### 1.1 Design tokens (`:root`)

```css
/* ---- design-tokens.css ---- */
:root {
  color-scheme: dark;

  /* ===== PALETTE ===== */
  /* Canvas / surfaces — near-black graduating to steel */
  --c-bg:            #0a0b0d;   /* page canvas (near-black) */
  --c-bg-elev-1:     #121418;   /* cards, header */
  --c-bg-elev-2:     #1a1d23;   /* nested panels, hover */
  --c-bg-elev-3:     #23272f;   /* inputs, chips */
  --c-line:          #2b3038;   /* hairline borders */
  --c-line-strong:   #3a414c;

  /* Steel neutrals (text) */
  --c-text:          #e8eaed;   /* primary text */
  --c-text-muted:    #a2a9b4;   /* secondary */
  --c-text-dim:      #6b727d;   /* captions, meta */

  /* Gold accent — belts, ratings, primary highlight */
  --c-gold:          #d4af37;
  --c-gold-bright:   #f2cc4b;
  --c-gold-dim:      #8c7420;
  --c-gold-tint:     rgba(212,175,55,.12);

  /* Red hot-accent — live, finishes, danger, CTAs */
  --c-red:           #e11d2a;
  --c-red-bright:    #ff3b48;
  --c-red-dim:       #8f1219;
  --c-red-tint:      rgba(225,29,42,.12);

  /* Semantic status */
  --c-win:           #2fbf71;   /* win / verified */
  --c-loss:          #e05263;   /* loss */
  --c-draw:          #c8a44d;   /* draw / no-contest */
  --c-live:          var(--c-red-bright);
  --c-focus:         #5aa9ff;   /* focus ring (AA on dark) */

  /* ===== FLUID TYPE SCALE (clamp: min, preferred vw, max) =====
     Base ~16px mobile → ~18px desktop. Major-third-ish ramp. */
  --fs-300: clamp(0.78rem, 0.74rem + 0.20vw, 0.875rem); /* fine print */
  --fs-400: clamp(0.94rem, 0.90rem + 0.25vw, 1.05rem);  /* body */
  --fs-500: clamp(1.13rem, 1.05rem + 0.40vw, 1.35rem);  /* lead / h4 */
  --fs-600: clamp(1.35rem, 1.20rem + 0.75vw, 1.80rem);  /* h3 */
  --fs-700: clamp(1.65rem, 1.35rem + 1.50vw, 2.55rem);  /* h2 */
  --fs-800: clamp(2.05rem, 1.55rem + 2.60vw, 3.60rem);  /* h1 / hero */
  --fs-900: clamp(2.60rem, 1.80rem + 4.20vw, 5.00rem);  /* poster numerals */

  --lh-tight: 1.08;
  --lh-snug:  1.28;
  --lh-body:  1.6;

  /* ===== SPACING SCALE (4px base, fluid at the top) ===== */
  --sp-1: 0.25rem;  /* 4  */
  --sp-2: 0.5rem;   /* 8  */
  --sp-3: 0.75rem;  /* 12 */
  --sp-4: 1rem;     /* 16 */
  --sp-5: 1.5rem;   /* 24 */
  --sp-6: 2rem;     /* 32 */
  --sp-7: 3rem;     /* 48 */
  --sp-8: clamp(3rem, 2rem + 5vw, 6rem); /* section gap */

  /* ===== RADII / SHADOW / MOTION ===== */
  --r-sm: 4px;
  --r-md: 8px;
  --r-lg: 14px;
  --r-pill: 999px;

  --shadow-1: 0 1px 2px rgba(0,0,0,.4);
  --shadow-2: 0 4px 16px rgba(0,0,0,.5);
  --shadow-gold: 0 0 0 1px var(--c-gold-dim), 0 6px 24px rgba(212,175,55,.10);

  --ease: cubic-bezier(.2,.7,.2,1);
  --dur: 180ms;

  /* Layout */
  --wrap: 1200px;
  --wrap-narrow: 760px; /* article measure */

  /* ===== SYSTEM FONT STACK (zero webfont cost by default) ===== */
  --font-sans: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue",
               Arial, "Noto Sans", "Noto Sans SC", sans-serif,
               "Apple Color Emoji", "Segoe UI Emoji";
  --font-cond: "Oswald", "Bebas Neue", "Arial Narrow", var(--font-sans); /* poster/stat headings */
  --font-mono: ui-monospace, "SF Mono", "Cascadia Code", Menlo, Consolas, monospace;
}

/* Respect reduced motion globally */
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: .01ms !important; animation-iteration-count: 1 !important;
      transition-duration: .01ms !important; scroll-behavior: auto !important; }
}
```

> `"Noto Sans SC"` is included in the stack so Simplified-Chinese pages fall back gracefully without a webfont (see §5). The condensed stack (`--font-cond`) is what gives the "poster/tale-of-the-tape" sports look; only load Oswald if you accept the webfont cost (§2.6).

### 1.2 Reset + base

```css
/* ---- base.css ---- */
*, *::before, *::after { box-sizing: border-box; }
* { margin: 0; }
html { -webkit-text-size-adjust: 100%; scroll-behavior: smooth; }
body {
  background: var(--c-bg);
  color: var(--c-text);
  font-family: var(--font-sans);
  font-size: var(--fs-400);
  line-height: var(--lh-body);
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  min-height: 100dvh;
}
h1,h2,h3,h4 { line-height: var(--lh-tight); font-weight: 700; text-wrap: balance; }
h1 { font-size: var(--fs-800); }
h2 { font-size: var(--fs-700); }
h3 { font-size: var(--fs-600); }
p  { max-width: 68ch; text-wrap: pretty; }
a  { color: var(--c-gold-bright); text-decoration-color: color-mix(in srgb, var(--c-gold) 40%, transparent);
     text-underline-offset: 2px; }
a:hover { color: var(--c-gold); }
img, iframe, video { max-width: 100%; display: block; }
:focus-visible { outline: 2px solid var(--c-focus); outline-offset: 2px; border-radius: var(--r-sm); }

/* Poster/stat numerals */
.stat, .tale h3 { font-family: var(--font-cond); letter-spacing: .01em; text-transform: uppercase; }
```

### 1.3 Layout primitives

```css
.wrap   { width: min(100% - 2rem, var(--wrap)); margin-inline: auto; }
.wrap--narrow { width: min(100% - 2rem, var(--wrap-narrow)); margin-inline: auto; }
.section { padding-block: var(--sp-8); }
.stack > * + * { margin-top: var(--sp-4); }        /* vertical rhythm */
.cluster { display: flex; flex-wrap: wrap; gap: var(--sp-2); align-items: center; }
```

### 1.4 Card component (fighter/event/match card)

```css
/* ---- card.css ---- */
.card {
  background: var(--c-bg-elev-1);
  border: 1px solid var(--c-line);
  border-radius: var(--r-lg);
  overflow: clip;
  transition: border-color var(--dur) var(--ease), transform var(--dur) var(--ease);
  position: relative;
}
.card:hover { border-color: var(--c-line-strong); transform: translateY(-2px); }

/* Whole-card link (accessible): stretch the primary anchor over the card */
.card__link::after { content: ""; position: absolute; inset: 0; }
.card__media { aspect-ratio: 4 / 5; background: var(--c-bg-elev-2); }
.card__media img { width: 100%; height: 100%; object-fit: cover; }
.card__body { padding: var(--sp-4); }
.card__title { font-size: var(--fs-500); }
.card__meta  { color: var(--c-text-dim); font-size: var(--fs-300); }

/* Status chips */
.chip {
  display: inline-flex; align-items: center; gap: .4em;
  padding: .2em .6em; border-radius: var(--r-pill);
  font-size: var(--fs-300); font-weight: 600; line-height: 1;
  background: var(--c-bg-elev-3); color: var(--c-text-muted);
  border: 1px solid var(--c-line);
}
.chip--live { color:#fff; background: var(--c-red); border-color: var(--c-red-bright); }
.chip--live::before { content:""; width:.5em; height:.5em; border-radius:50%;
  background:#fff; box-shadow:0 0 0 0 rgba(255,255,255,.7); animation: pulse 1.4s infinite; }
.chip--gold  { color: var(--c-gold-bright); background: var(--c-gold-tint); border-color: var(--c-gold-dim); }
.chip--win   { color: var(--c-win); }
.chip--loss  { color: var(--c-loss); }
@keyframes pulse { 70%{box-shadow:0 0 0 6px rgba(255,255,255,0);} 100%{box-shadow:0 0 0 0 rgba(255,255,255,0);} }

/* Tale-of-the-tape / stat block */
.tale { display:grid; grid-template-columns: 1fr auto 1fr; gap: var(--sp-3);
        background: var(--c-bg-elev-1); border:1px solid var(--c-line);
        border-radius: var(--r-lg); padding: var(--sp-5); }
.tale .stat { font-family: var(--font-cond); font-size: var(--fs-700); color: var(--c-gold-bright); }
.tale .vs   { align-self:center; color: var(--c-red); font-family: var(--font-cond); font-size: var(--fs-600); }
```

### 1.5 Pure-CSS star-rating meter

Two variants. **(A) Static display** driven by a single CSS variable (no images, no JS, supports fractional stars via `background-clip: text`). **(B) Accessible interactive input** using native radios (works without JS; degrades fine with no storage).

**(A) Display-only fractional meter** — set `--rating` (0–5):

```html
<div class="rating" style="--rating: 4.3" role="img" aria-label="Rated 4.3 out of 5">
  <span class="rating__stars" aria-hidden="true">★★★★★</span>
</div>
```

```css
.rating { --rating: 0; display: inline-block; font-size: var(--fs-600); line-height: 1; }
.rating__stars {
  position: relative;
  display: inline-block;
  font-family: Times, serif;          /* consistent solid ★ glyph */
  letter-spacing: .1em;
  /* empty (background) stars = steel */
  color: var(--c-line-strong);
}
.rating__stars::before {
  content: "★★★★★";
  position: absolute; inset: 0; overflow: hidden;
  white-space: nowrap;
  /* fill width = rating/5, accounting for letter-spacing via ch is imperfect;
     use % of the 5-star box: */
  width: calc(var(--rating) / 5 * 100%);
  color: var(--c-gold-bright);
  -webkit-background-clip: initial;
}
```

> Tip: because `letter-spacing` widens the box, the cleanest fractional fill is to render the gold layer as a clipped copy sized by percentage (above). For pixel-perfect fills, use a fixed-width monospaced star or an inline SVG symbol.

**(B) Interactive 5-star radio input** (pure CSS hover/checked, no JS, no storage — submit via form):

```html
<fieldset class="rate">
  <legend>Rate this match</legend>
  <!-- reverse order so CSS sibling selector can light preceding stars -->
  <input type="radio" id="r5" name="stars" value="5"><label for="r5" aria-label="5 stars">★</label>
  <input type="radio" id="r4" name="stars" value="4"><label for="r4" aria-label="4 stars">★</label>
  <input type="radio" id="r3" name="stars" value="3"><label for="r3" aria-label="3 stars">★</label>
  <input type="radio" id="r2" name="stars" value="2"><label for="r2" aria-label="2 stars">★</label>
  <input type="radio" id="r1" name="stars" value="1"><label for="r1" aria-label="1 star">★</label>
</fieldset>
```

```css
.rate { border:0; padding:0; display:inline-flex; flex-direction: row-reverse; gap:.1em; font-size: var(--fs-600); }
.rate legend { font-size: var(--fs-300); color: var(--c-text-muted); margin-bottom: var(--sp-1); }
.rate input { position:absolute; opacity:0; width:0; }        /* visually hide, keep focusable */
.rate label { color: var(--c-line-strong); cursor:pointer; transition: color 120ms var(--ease); }
/* checked star + all AFTER it in DOM (which are visually to the LEFT via row-reverse) */
.rate input:checked ~ label { color: var(--c-gold); }
/* hover state overrides checked */
.rate:hover label { color: var(--c-line-strong); }
.rate label:hover, .rate label:hover ~ label { color: var(--c-gold-bright); }
.rate input:focus-visible + label { outline: 2px solid var(--c-focus); outline-offset:2px; }
```

**Aggregate rating meter (horizontal bar):**

```html
<div class="meter" style="--pct: 86" role="img" aria-label="Community score 86 out of 100">
  <span class="meter__fill"></span><b class="meter__num">8.6</b>
</div>
```
```css
.meter { position:relative; height:10px; background:var(--c-bg-elev-3); border-radius:var(--r-pill); overflow:hidden; }
.meter__fill { position:absolute; inset:0 auto 0 0; width:calc(var(--pct)*1%);
  background:linear-gradient(90deg,var(--c-red),var(--c-gold)); border-radius:inherit; }
.meter__num { position:absolute; right:.5em; top:-1.6em; font-family:var(--font-cond); color:var(--c-gold-bright); }
```

---

## 2. Mobile-First + Performance

### 2.1 Responsive card grid (auto-fit, no media queries needed)

```css
.grid-cards {
  display: grid;
  gap: var(--sp-4);
  /* fluid: as many ~180px+ columns as fit, they grow to fill */
  grid-template-columns: repeat(auto-fill, minmax(min(180px, 100%), 1fr));
}
/* Denser roster on wide screens */
@media (min-width: 90rem) {
  .grid-cards { grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); }
}
```

### 2.2 Container queries (component-level responsiveness)

Container queries let a card restyle based on *its own* width, not the viewport — ideal when the same card appears in a sidebar and a full-width grid.

```css
.card-ctx { container-type: inline-size; container-name: card; }

/* When the card's container is wide enough, go horizontal */
@container card (min-width: 380px) {
  .card { display: grid; grid-template-columns: 120px 1fr; align-items: stretch; }
  .card__media { aspect-ratio: 1 / 1; }
}
```
Container queries are baseline across all current evergreen browsers (2023+). Safe to use in 2025-2026.

### 2.3 Responsive 16:9 embed wrapper (modern + fallback)

```css
/* Modern browsers */
.embed { aspect-ratio: 16 / 9; width: 100%; background:#000; border-radius: var(--r-md); overflow: clip; }
.embed > iframe, .embed > .facade { width:100%; height:100%; border:0; display:block; }

/* Legacy fallback (very old browsers): padding-hack */
@supports not (aspect-ratio: 1) {
  .embed { position: relative; height: 0; padding-bottom: 56.25%; }
  .embed > * { position:absolute; inset:0; }
}
```

### 2.4 Facade "click-to-load" lazy embed (YouTube + Bilibili) — HTML/CSS/JS

The facade pattern ships a lightweight poster image + play button instead of the heavy third-party iframe (each YouTube iframe can pull ~1MB+ of JS). The real iframe is injected only on click. This is the single biggest perf win for embed-heavy fan pages and directly improves LCP/TBT. (Popularized by Paul Irish's `lite-youtube-embed`; this is a dependency-free, no-storage version.)

```html
<!-- YouTube facade -->
<div class="embed">
  <button class="facade" type="button"
          data-provider="youtube"
          data-id="dQw4w9WgXcQ"
          aria-label="Play video: Fight highlights">
    <img class="facade__poster"
         src="https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg"
         alt="" width="480" height="360" loading="lazy" decoding="async">
    <span class="facade__btn" aria-hidden="true">▶</span>
  </button>
</div>

<!-- Bilibili facade (for China / see §5). Provide your own poster image. -->
<div class="embed">
  <button class="facade" type="button"
          data-provider="bilibili"
          data-bvid="BV1Kx411q7Eg"
          aria-label="播放视频：比赛集锦">
    <img class="facade__poster" src="/img/posters/bili-BV1Kx411q7Eg.jpg"
         alt="" loading="lazy" decoding="async">
    <span class="facade__btn" aria-hidden="true">▶</span>
  </button>
</div>
```

```css
.facade { position: relative; width:100%; height:100%; padding:0; border:0; cursor:pointer;
          background:#000; display:block; }
.facade__poster { width:100%; height:100%; object-fit: cover; opacity:.85;
                  transition: opacity var(--dur) var(--ease); }
.facade:hover .facade__poster { opacity: 1; }
.facade__btn {
  position:absolute; inset:0; margin:auto; width:68px; height:48px;
  display:grid; place-content:center; font-size:24px; color:#fff;
  background: var(--c-red); border-radius: 14px; box-shadow: var(--shadow-2);
  transition: transform var(--dur) var(--ease), background var(--dur) var(--ease);
}
.facade:hover .facade__btn { transform: scale(1.06); background: var(--c-red-bright); }
```

```js
/* ---- facade.js : no dependencies, no storage ---- */
document.addEventListener('click', function (e) {
  const btn = e.target.closest('.facade');
  if (!btn) return;

  const p = btn.dataset.provider;
  let src;

  if (p === 'youtube') {
    // Use privacy-enhanced nocookie domain; autoplay on user gesture.
    src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(btn.dataset.id)
        + '?autoplay=1&rel=0&modestbranding=1';
  } else if (p === 'bilibili') {
    src = 'https://player.bilibili.com/player.html?bvid=' + encodeURIComponent(btn.dataset.bvid)
        + '&autoplay=1&high_quality=1&danmaku=0';
  } else {
    return;
  }

  const iframe = document.createElement('iframe');
  iframe.src = src;
  iframe.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen';
  iframe.setAttribute('allowfullscreen', '');
  iframe.setAttribute('title', btn.getAttribute('aria-label') || 'Embedded video');
  iframe.loading = 'lazy';
  iframe.referrerPolicy = 'strict-origin-when-cross-origin';

  btn.replaceWith(iframe); // .embed keeps the 16:9 box
});
```

> **Poster sources:** YouTube exposes `https://i.ytimg.com/vi/<ID>/hqdefault.jpg` (or `maxresdefault.jpg`). Bilibili has no stable public thumbnail CDN pattern, so store your own poster (also better for the Great Firewall — see §5). Preconnect to the embed origin only when a facade is present (§2.5).

### 2.5 Core Web Vitals (LCP / CLS / INP) checklist

**LCP (Largest Contentful Paint — target < 2.5s):**
- Mark the hero/LCP image and *do not* lazy-load it: `fetchpriority="high" loading="eager" decoding="async"`.
- Preload the LCP image and hero font:
  ```html
  <link rel="preload" as="image" href="/img/hero.avif" fetchpriority="high">
  ```
- Serve modern formats (AVIF → WebP → JPEG fallback via `<picture>`), width/quality-sized.
- `preconnect` to third-party embed/image origins used above the fold:
  ```html
  <link rel="preconnect" href="https://i.ytimg.com" crossorigin>
  <link rel="preconnect" href="https://www.youtube-nocookie.com" crossorigin>
  ```
- Inline critical CSS in `<head>`; defer the rest. With no build step, keep total CSS small (single file, HTTP/2) or inline it.

**CLS (Cumulative Layout Shift — target < 0.1):**
- Always set `width`/`height` (or `aspect-ratio`) on `img`, `iframe`, `video`, and ad/embed slots so the browser reserves space. The `.embed { aspect-ratio:16/9 }` box (§2.3) prevents embed shift.
- Reserve space for late content (fonts, banners). Use `font-display: swap` with a metrics-matched fallback to avoid text reflow.
- Never insert content above existing content after load.

**INP (Interaction to Next Paint — target < 200ms):**
- Keep JS tiny and event-delegated (see `facade.js` — one listener for all embeds).
- Avoid long tasks; break up any heavy JS with `requestIdleCallback`.
- Facade pattern removes third-party embed JS from initial load, cutting main-thread blocking.

**Responsive image template:**
```html
<picture>
  <source type="image/avif" srcset="/img/f/khabib-400.avif 400w, /img/f/khabib-800.avif 800w" sizes="(max-width:600px) 45vw, 200px">
  <source type="image/webp" srcset="/img/f/khabib-400.webp 400w, /img/f/khabib-800.webp 800w" sizes="(max-width:600px) 45vw, 200px">
  <img src="/img/f/khabib-400.jpg" width="400" height="500" alt="Khabib Nurmagomedov" loading="lazy" decoding="async">
</picture>
```

### 2.6 Font-loading strategy

Default: **use the system stack** (§1.1) → zero network cost, zero CLS, instant text. Only add a webfont for the condensed "poster" headings if the brand needs it. If you do:

```html
<!-- self-host to avoid third-party connection + FF blocking in China -->
<link rel="preload" href="/fonts/oswald-600.woff2" as="font" type="font/woff2" crossorigin>
```
```css
@font-face {
  font-family: "Oswald";
  src: url("/fonts/oswald-600.woff2") format("woff2");
  font-weight: 600;
  font-display: swap;             /* show fallback immediately, swap when ready */
  /* size-adjust minimizes the swap reflow (CLS) */
  size-adjust: 100%;
  ascent-override: 90%;
}
```
Rules: **self-host** woff2 (one weight per file), subset to Latin (+ Latin-Ext), `font-display: swap`, `preload` only the above-the-fold weight, and pick a fallback with similar metrics so the swap barely shifts. Never block render on fonts. For Chinese pages, do **not** webfont-load full CJK (megabytes) — rely on the `Noto Sans SC` / system CJK fallback in the stack.

---

## 3. SEO

Every code block below is ready to adapt. Put JSON-LD in `<script type="application/ld+json">` in `<head>` or end of `<body>`.

### 3.1 `<head>` meta template (canonical / OG / Twitter / hreflang)

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>Khabib Nurmagomedov — Record, Bio & Fight History | ArenaDB</title>
  <meta name="description" content="Complete Khabib Nurmagomedov profile: 29-0 MMA record, title history, fight-by-fight results, stats and video highlights.">
  <link rel="canonical" href="https://arenadb.com/fighter/khabib-nurmagomedov">

  <!-- hreflang: one line per locale + x-default. URLs must be absolute and reciprocal. -->
  <link rel="alternate" hreflang="en" href="https://arenadb.com/fighter/khabib-nurmagomedov">
  <link rel="alternate" hreflang="zh-Hans" href="https://arenadb.com/zh/fighter/khabib-nurmagomedov">
  <link rel="alternate" hreflang="x-default" href="https://arenadb.com/fighter/khabib-nurmagomedov">

  <!-- Open Graph -->
  <meta property="og:type" content="profile">
  <meta property="og:site_name" content="ArenaDB">
  <meta property="og:title" content="Khabib Nurmagomedov — Record, Bio & Fight History">
  <meta property="og:description" content="29-0 MMA record, title history, fight-by-fight results and highlights.">
  <meta property="og:url" content="https://arenadb.com/fighter/khabib-nurmagomedov">
  <meta property="og:image" content="https://arenadb.com/img/og/khabib.jpg"><!-- 1200x630 -->
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="en_US">
  <meta property="og:locale:alternate" content="zh_CN">

  <!-- Twitter/X -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Khabib Nurmagomedov — Record, Bio & Fight History">
  <meta name="twitter:description" content="29-0 MMA record, title history and highlights.">
  <meta name="twitter:image" content="https://arenadb.com/img/og/khabib.jpg">

  <meta name="theme-color" content="#0a0b0d">
</head>
```

> hreflang rules: absolute URLs, **reciprocal** (every alternate must point back), one `x-default`, use `zh-Hans`/`zh-Hant` (script) rather than only `zh-CN`/`zh-TW` when possible.

### 3.2 JSON-LD — Person (athlete profile)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://arenadb.com/fighter/khabib-nurmagomedov#person",
  "name": "Khabib Nurmagomedov",
  "alternateName": "The Eagle",
  "url": "https://arenadb.com/fighter/khabib-nurmagomedov",
  "image": "https://arenadb.com/img/f/khabib-800.jpg",
  "birthDate": "1988-09-20",
  "birthPlace": { "@type": "Place", "name": "Sildi, Dagestan, Russia" },
  "height": { "@type": "QuantitativeValue", "value": 178, "unitCode": "CMT" },
  "weight": { "@type": "QuantitativeValue", "value": 70.3, "unitCode": "KGM" },
  "nationality": { "@type": "Country", "name": "Russia" },
  "jobTitle": "Mixed Martial Artist",
  "athlete": { "@type": "SportsTeam", "name": "American Kickboxing Academy" },
  "sameAs": [
    "https://en.wikipedia.org/wiki/Khabib_Nurmagomedov",
    "https://www.wikidata.org/wiki/Q16205655",
    "https://www.instagram.com/khabib_nurmagomedov/"
  ]
}
</script>
```
> `sameAs` to Wikipedia + Wikidata is a strong **entity-clarity** signal (helps both classic SEO and GEO — see §4).

### 3.3 JSON-LD — SportsEvent (a fight card / bout)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SportsEvent",
  "@id": "https://arenadb.com/event/ufc-229#event",
  "name": "UFC 229: Khabib vs. McGregor",
  "sport": "Mixed Martial Arts",
  "startDate": "2018-10-06T22:00:00-07:00",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "location": {
    "@type": "Place",
    "name": "T-Mobile Arena",
    "address": { "@type": "PostalAddress", "addressLocality": "Las Vegas", "addressRegion": "NV", "addressCountry": "US" }
  },
  "competitor": [
    { "@type": "Person", "name": "Khabib Nurmagomedov", "@id": "https://arenadb.com/fighter/khabib-nurmagomedov#person" },
    { "@type": "Person", "name": "Conor McGregor", "@id": "https://arenadb.com/fighter/conor-mcgregor#person" }
  ],
  "organizer": { "@type": "Organization", "name": "Ultimate Fighting Championship", "url": "https://www.ufc.com" },
  "offers": {
    "@type": "Offer", "url": "https://arenadb.com/event/ufc-229",
    "availability": "https://schema.org/SoldOut", "price": "0", "priceCurrency": "USD"
  }
}
</script>
```

### 3.4 JSON-LD — Review + AggregateRating (match rating)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Review",
  "itemReviewed": {
    "@type": "SportsEvent",
    "name": "Khabib vs. McGregor (UFC 229 Main Event)",
    "@id": "https://arenadb.com/event/ufc-229#event"
  },
  "author": { "@type": "Person", "name": "Editorial Staff" },
  "datePublished": "2018-10-07",
  "reviewBody": "A masterclass in grappling control...",
  "reviewRating": { "@type": "Rating", "ratingValue": "4.5", "bestRating": "5", "worstRating": "1" },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.3",
    "bestRating": "5",
    "worstRating": "1",
    "ratingCount": "12840",
    "reviewCount": "512"
  }
}
</script>
```
> Google requires that rating stars in results reflect *genuine, on-page* user/editorial reviews — never fabricate `ratingCount`. `AggregateRating` can also be nested directly inside the reviewed item (Person/Product/Event) instead of inside a Review.

### 3.5 JSON-LD — BreadcrumbList

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://arenadb.com/" },
    { "@type": "ListItem", "position": 2, "name": "Fighters", "item": "https://arenadb.com/fighters" },
    { "@type": "ListItem", "position": 3, "name": "Khabib Nurmagomedov", "item": "https://arenadb.com/fighter/khabib-nurmagomedov" }
  ]
}
</script>
```

### 3.6 JSON-LD — FAQPage (also key for GEO, §4)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is Khabib Nurmagomedov's professional MMA record?",
      "acceptedAnswer": { "@type": "Answer",
        "text": "Khabib Nurmagomedov retired with a perfect 29-0 professional MMA record, including 8-0 in UFC title fights." }
    },
    {
      "@type": "Question",
      "name": "When did Khabib retire?",
      "acceptedAnswer": { "@type": "Answer",
        "text": "He announced his retirement on October 24, 2020, after defeating Justin Gaethje at UFC 254." }
    }
  ]
}
</script>
```
> The FAQ **question/answer text must be visibly present on the page**. Note: Google restricts FAQ *rich-result display* mostly to authoritative gov/health sites, but the markup still aids GEO and AI extraction — keep it.

### 3.7 JSON-LD — Organization (site identity; place once on homepage)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://arenadb.com/#org",
  "name": "ArenaDB",
  "url": "https://arenadb.com/",
  "logo": { "@type": "ImageObject", "url": "https://arenadb.com/img/logo-512.png", "width": 512, "height": 512 },
  "description": "The community-driven database of combat sports records, events and match ratings.",
  "foundingDate": "2024",
  "sameAs": [
    "https://twitter.com/arenadb",
    "https://www.youtube.com/@arenadb",
    "https://space.bilibili.com/xxxxxxxx"
  ]
}
</script>
```

### 3.8 `robots.txt` template

```text
# https://arenadb.com/robots.txt
User-agent: *
Allow: /
Disallow: /search
Disallow: /*?sort=
Disallow: /*?filter=
Disallow: /admin/

# Explicitly welcome AI crawlers you WANT to be cited by (GEO, §4).
# Remove any you wish to block instead.
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Bytespider
Allow: /

Sitemap: https://arenadb.com/sitemap.xml
```
> `GPTBot` = OpenAI training crawler; `OAI-SearchBot` = ChatGPT live search; `Google-Extended` = opt-in/out for Gemini/AI Overviews training; `PerplexityBot` = Perplexity; `ClaudeBot` = Anthropic; `Bytespider` = ByteDance (matters for China/Doubao). If you want AI citations, **allow** these.

### 3.9 `sitemap.xml` template (with hreflang + video)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml"
        xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">
  <url>
    <loc>https://arenadb.com/fighter/khabib-nurmagomedov</loc>
    <lastmod>2026-07-25</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <xhtml:link rel="alternate" hreflang="en" href="https://arenadb.com/fighter/khabib-nurmagomedov"/>
    <xhtml:link rel="alternate" hreflang="zh-Hans" href="https://arenadb.com/zh/fighter/khabib-nurmagomedov"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://arenadb.com/fighter/khabib-nurmagomedov"/>
    <video:video>
      <video:thumbnail_loc>https://arenadb.com/img/posters/khabib-hl.jpg</video:thumbnail_loc>
      <video:title>Khabib Nurmagomedov — Career Highlights</video:title>
      <video:description>Every UFC finish and takedown.</video:description>
      <video:player_loc>https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ</video:player_loc>
    </video:video>
  </url>
</urlset>
```
For large DBs, split into multiple sitemaps under a `sitemapindex` (≤ 50,000 URLs / ≤ 50MB uncompressed each).

### 3.10 Crawlability essentials (a "database" site lives or dies here)

- **Real `<a href>` links** for every entity — never JS-only navigation (you're framework-free, so this is natural; keep it that way).
- Clean, stable, human-readable slugs: `/fighter/khabib-nurmagomedov`, `/event/ufc-229`.
- Semantic HTML: one `<h1>`, real `<table>` for records/tale-of-the-tape, `<nav>`, `<main>`, `<article>`, breadcrumb `<nav aria-label="Breadcrumb">`.
- Internal linking: cross-link fighters ↔ events ↔ divisions ↔ rankings densely. Related-links block on every entity page.
- Pagination with `<a>` + descriptive text; avoid infinite scroll as the only path.
- Canonical every filter/sort permutation back to the base list (see robots `Disallow: /*?sort=`).

---

## 4. GEO — Generative Engine Optimization

Goal: get **cited/quoted** inside ChatGPT, Perplexity, Gemini, Claude, and Google AI Overviews. GEO complements SEO — the AI engines mostly retrieve from the live web (RAG) + their index, so crawlability (§3) is the price of entry; the tactics below raise your *citation* probability.

### 4.1 What the research actually shows (Princeton/IIT-Delhi "GEO" paper, Aggarwal et al.)

The foundational study introduced **GEO-BENCH** (10,000 queries across 8 domains) and measured visibility with *Position-Adjusted Word Count* + *Subjective Impression*. Tactics that raised source visibility in generated answers by up to **~40%** (and up to **115%** for lower-ranked pages):

| Tactic | Reported lift in AI visibility |
|---|---|
| **Cite Sources** (add credible citations) | ~30–40% (up to 115% for a page ranked ~5th) |
| **Add Quotations** (expert/primary quotes) | ~30–40% |
| **Add Statistics** (concrete numbers/data) | ~30–40% |
| **Fluency Optimization** (clear, well-written prose) | ~15–30% |
| **Authoritative/Technical tone** | ~10–20% |
| Keyword stuffing | **negative / no help** |

Key implication: **statistics + quotations + citations + fluent authoritative prose** is the winning combination. Keyword stuffing does not work for GEO. (Effectiveness is domain-dependent — stats win in Law/Gov/Opinion; quotes win in History/People & Society.) [Sources below]

### 4.2 Answer-first content structure (the #1 practical pattern)

Lead every page/section with a direct, self-contained answer, then expand. AI extractors lift the first 1–3 sentences after a question-style heading.

```html
<article class="wrap--narrow">
  <h1>What is Khabib Nurmagomedov's MMA record?</h1>

  <!-- ANSWER-FIRST: complete, quotable, contains the entity + the number -->
  <p class="answer"><strong>Khabib Nurmagomedov retired undefeated with a
  29–0 professional MMA record</strong>, going 13–0 in the UFC and 8–0 in
  UFC lightweight title fights before retiring on October 24, 2020.</p>

  <!-- THEN depth, stats, quotes, citations -->
  <h2>Record by finish type</h2>
  <table> ... </table>
</article>
```
Guidelines: put the answer in the **first ~40–60 words**; make headings **exact natural-language questions**; keep each answer a standalone chunk that makes sense out of context (see §4.5).

### 4.3 FAQ schema + visible FAQ

Ship a visible Q&A block **and** `FAQPage` JSON-LD (§3.6). Aim for 6+ real questions per major entity page phrased the way users ask AI ("who did Khabib beat for the title?", "is Khabib in the Hall of Fame?"). This is one of the highest-ROI GEO moves for a database site because your data *is* the answer.

### 4.4 Entity clarity

Make each entity unambiguous to the knowledge graph:
- `Person`/`Organization`/`SportsEvent` JSON-LD with stable `@id` URIs (§3).
- `sameAs` → **Wikipedia + Wikidata** + official socials. Wikidata linkage is the strongest disambiguation signal.
- Consistent naming, `alternateName` for nicknames ("The Eagle").
- Cross-link related entities internally so the model sees the graph structure.

### 4.5 Content chunking for retrieval (RAG)

RAG systems split pages into ~200–500-token chunks and embed each. Optimize so each chunk stands alone:
- One idea per section under a descriptive `<h2>/<h3>`.
- Repeat the subject noun instead of pronouns near section starts ("Khabib's title defenses…" not "His defenses…") so a lifted chunk keeps its subject.
- Use tables, definition lists, and short paragraphs — easy to parse and quote.
- Front-load the key fact in each chunk; don't bury the number in paragraph 3.
- Keep a canonical, single source-of-truth page per entity (avoid near-duplicate pages that dilute retrieval).

### 4.6 Statistics + citation density

Because "Add Statistics" and "Cite Sources" are top-ranked tactics, a stats DB has a natural GEO edge:
- Surface hard numbers inline as text (not only in images): records, finish rates, dates, attendance, purse.
- Cite primary/authoritative sources (official org results, Wikipedia) with visible outbound links.
- Add named authors + `datePublished`/`dateModified` and keep a visible "Last updated" — freshness is a citation signal.

### 4.7 `llms.txt` convention — template + honest status

`llms.txt` (proposed by Jeremy Howard / Answer.AT — Answer.AI, Sept 2024) is a root-level Markdown file that gives LLMs a curated map of your most important pages. **Honest status (2025-2026):** it is *not yet consumed by the major inference engines* — server-log analyses show OpenAI/Google crawlers generally don't request it, and Google's John Mueller has been publicly skeptical. Treat it as **low-cost, forward-looking hygiene**, not a ranking lever. Anthropic and many dev-tool sites publish one.

Place at `https://arenadb.com/llms.txt`:

```markdown
# ArenaDB

> ArenaDB is a community-driven database of combat-sports records, events, and
> match ratings, covering MMA, boxing and pro-wrestling with verified,
> source-cited statistics.

## Core databases
- [Fighter directory](https://arenadb.com/fighters): Every fighter profile with full record and bio.
- [Event archive](https://arenadb.com/events): Fight cards with results, ratings and video.
- [Rankings](https://arenadb.com/rankings): Current divisional and pound-for-pound rankings.

## Key reference pages
- [How ratings work](https://arenadb.com/about/ratings): Methodology for community match ratings.
- [Data sources & citations](https://arenadb.com/about/sources): Where our data comes from.

## Optional
- [About / Editorial standards](https://arenadb.com/about)
```
(Optionally also `llms-full.txt` with fuller Markdown content of key pages.)

### 4.8 Practical GEO checklist

- [ ] Answer-first paragraph under each question-style `<h1>/<h2>`
- [ ] 6+ visible FAQs + `FAQPage` JSON-LD per entity
- [ ] Hard statistics rendered as text, with visible citations to authoritative sources
- [ ] Person/Event/Org JSON-LD with `@id` + `sameAs` (Wikipedia/Wikidata)
- [ ] Self-contained retrieval chunks (subject-repeated, one idea per section)
- [ ] Named author + visible last-updated date
- [ ] AI crawlers allowed in `robots.txt` (§3.8)
- [ ] `llms.txt` published (low priority)
- [ ] Fast, crawlable, JS-free navigation (§2, §3.10)

**GEO sources:**
- Aggarwal et al., "GEO: Generative Engine Optimization" (arXiv:2311.09735) — <https://arxiv.org/pdf/2311.09735>
- "The Princeton GEO Paper in Plain English" (DerivateX) — <https://derivatex.agency/blog/princeton-geo-paper-plain-english/>
- Search Engine Land, GEO framework coverage — <https://searchengineland.com/generative-engine-optimization-framework-introduced-research-paper-435855>
- Wikipedia, "Generative engine optimization" — <https://en.wikipedia.org/wiki/Generative_engine_optimization>
- Enrich Labs GEO guide (2026) — <https://www.enrichlabs.ai/blog/generative-engine-optimization-geo-complete-guide-2026>
- "llms.txt — honest look at hype vs reality" (IdeaHills) — <https://ideahills.com/what-is-llms-txt-an-honest-look-at-hype-vs-reality-template/>
- Frase, "What is GEO? 2026 Guide" — <https://www.frase.io/blog/what-is-generative-engine-optimization-geo>

---

## 5. China Market

Honest reality first: **YouTube, Google, Facebook, Instagram, X, Twitch and Discord are blocked** by the Great Firewall (GFW). A Western-hosted site typically loads slowly (10–30s) or intermittently in mainland China. Reaching Chinese fans is less about porting your site and more about **publishing native content on Chinese platforms** and, if you want the site itself to be usable, dealing with hosting + ICP realities.

### 5.1 Platform map (where combat-sports fans actually are)

| Platform | What it is | Use it for |
|---|---|---|
| **Bilibili (哔哩哔哩)** | Long-form video + danmaku (bullet comments); young, fandom-heavy, "otaku"/subculture core | Your primary video home in China — highlights, breakdowns, docs. The YouTube substitute. Embeddable (§5.3). |
| **Douyin (抖音)** | China's TikTok; short vertical video, huge reach + commerce | Short clips, viral finishes, hooks driving to Bilibili/site. |
| **Weibo (微博)** | Twitter-like microblog; news, trending topics, celebrity | Real-time results, event hype, hashtags (#话题#), announcements. |
| **Youku (优酷)** | Alibaba's long-form video (more mainstream/older than Bilibili) | Alt video host / embeds (§5.3). |
| **WeChat (微信)** | Super-app: messaging + **Official Accounts** + **Mini-Programs** + **Channels (视频号)** + Pay | Retention, membership, payments, in-app content. See §5.4. |
| **Xiaohongshu / RED (小红书)** | Lifestyle discovery + search; text+photo "notes", increasingly a search engine | SEO-like discovery, listicles, athlete lifestyle, growing sports niche. |
| **Doubao / Kimi / Baidu** | Chinese AI + Baidu search (Google is blocked) | China-GEO: allow `Bytespider` (§3.8); Baidu SEO if hosting onshore. |

### 5.2 The realistic playbook for a Western fan site

1. **Content-first, not site-first.** Repurpose your best video/data into native Bilibili + Douyin + Weibo accounts. This needs **no ICP** and dodges the GFW entirely.
2. **Set up a WeChat Official Account** (see §5.4) as your owned CRM/retention channel.
3. **Only if you need the actual website fast in China:** get an ICP filing + onshore/hybrid CDN (see §5.5). Otherwise accept slow international access, or serve a lightweight `zh-Hans` version optimized to survive the GFW (no Google Fonts, no YouTube, no `googleapis.com`, no `gstatic`, self-hosted assets, Chinese video embeds only).
4. **QR-first everything** (§5.7).

### 5.3 Embedding Chinese video (YouTube is blocked → use Bilibili / Youku)

Use the **same facade pattern** from §2.4 — it already supports Bilibili. Raw responsive iframes:

**Bilibili:**
```html
<div class="embed">
  <iframe
    src="https://player.bilibili.com/player.html?bvid=BV1Kx411q7Eg&autoplay=0&high_quality=1&danmaku=0&as_wide=1"
    scrolling="no" frameborder="no" allowfullscreen="true"
    referrerpolicy="strict-origin-when-cross-origin"
    title="比赛集锦"></iframe>
</div>
```
- URL: `https://player.bilibili.com/player.html?bvid=<BVID>` (modern `bvid`; legacy used `aid`+`cid`). Params: `autoplay`, `high_quality=1`, `danmaku=0` (hide bullet comments), `as_wide=1` (widescreen), `page=1`.
- Get the `BVID` from the video URL `bilibili.com/video/BV1Kx411q7Eg`.
- Serve over **https**; the `.embed{aspect-ratio:16/9}` wrapper makes it responsive.

**Youku:**
```html
<div class="embed">
  <iframe src="https://player.youku.com/embed/XNjMxxxxxxx==" 
          frameborder="0" allowfullscreen
          title="优酷视频"></iframe>
</div>
```
- URL: `https://player.youku.com/embed/<VIDEO_ID>` (the `==`-style ID from the share/embed code). Youku also offers `https://player.youku.com/player.php/sid/<ID>/v.swf` legacy — avoid Flash; use `/embed/`.

> Prefer **self-hosted poster images** for the facade (Bilibili/Youku lack a stable public thumbnail URL pattern like YouTube's, and self-hosting is more GFW-robust).

### 5.4 WeChat: Official Accounts, Mini-Programs, Channels, Pay

WeChat is a walled super-app — content lives *inside* it, largely un-crawlable by outside search, so treat it as an owned channel, not SEO.

- **Official Account (公众号):**
  - *Subscription account (订阅号)* — best for media/publishers; can post ~daily; shows in the Subscriptions feed. Good default for a fan site.
  - *Service account (服务号)* — 4 posts/month but richer APIs, menus, and access to WeChat Pay; better if you want membership/payments.
  - Foreign entities *can* register (needs business verification; a China entity or a verification partner smooths it). Content is Simplified Chinese, article-style with images/video.
- **Mini-Program (小程序):** app-like experience inside WeChat (no install). Ideal for a lightweight "fighter database" / event schedule / ratings that runs *natively in China* without ICP-blocked website woes. Built with WXML/WXSS/JS (WeChat's own stack) — separate from your site, but you can mirror the same data. Supports WeChat Pay for memberships.
- **Channels / 视频号:** WeChat's native short-video feed, tightly integrated with Official Accounts, Moments sharing and livestreams. Cross-post your Douyin clips here; strong for social/viral spread within WeChat.
- **Payments — WeChat Pay & Alipay:** the two dominant rails; credit cards are rare. For memberships/donations:
  - **WeChat Pay** (via Service Account or Mini-Program) and **Alipay** are standard.
  - **Cross-border options exist for foreign merchants** (WeChat Pay/Alipay cross-border, or aggregators) but require a real merchant entity + KYC and settle in your currency. Both now also accept **international credit cards linked inside the apps** for inbound tourists, but locals expect native Pay.
  - **QR codes** are the universal payment + follow mechanism (§5.7).

### 5.5 ICP license + data-localization realities (honest)

- **ICP filing (ICP备案 / "beian")** vs **ICP commercial license (ICP证):**
  - *ICP filing* = required to legally **host a site on mainland-China servers** for informational (non-transactional) content. Provincial MIIT approval; needs a China business entity/legal presence.
  - *ICP commercial license* = additionally required if you sell/charge (e-commerce, paid membership, ads-as-service). Must have the filing first.
- **Hosting outside China → no ICP required**, but you're behind the GFW: slow, throttled, or intermittently blocked; **an ICP does not fix speed by itself** — it's a legal/hosting decision, not a performance switch.
- **To be both legal and fast in China you generally need:** a China entity (or a partner/agent), an ICP filing, and **onshore or "hybrid"/China-edge CDN** hosting (e.g., a China-accessible CDN with an ICP). Some providers offer ICP-less China acceleration in limited/grey ways — verify current legality before relying on it.
- **Data localization (PIPL / CSL / DSL):** China's Personal Information Protection Law requires personal data of China users to generally be **stored in China**, with cross-border transfer subject to security assessment/standard contract/consent. For a fan site: avoid collecting Chinese users' personal data on foreign servers; if you run accounts/payments in China, plan for in-China data storage and compliance. Since your stack uses **no browser storage and minimal PII**, you're already lower-risk — keep it that way for the China edition.
- **Practical honest take:** most Western fan sites should **not** chase ICP first. Win on-platform (Bilibili/Douyin/Weibo/WeChat) where the audience and the fast infra already are; pursue ICP + onshore hosting only when there's a real business case (paid membership at scale in China).

### 5.6 Simplified-Chinese localization + hreflang

- Serve a real `zh-Hans` (Simplified) edition at `/zh/...`; use `zh-Hant` if you also target Taiwan/HK.
- `<html lang="zh-Hans">`; reciprocal hreflang pairs + `x-default` (see §3.1 and §3.9).
- **Don't rely on Google Fonts / `googleapis.com` / `gstatic.com`** — they're blocked/slow in China. Use the system CJK stack (`Noto Sans SC` fallback is in `--font-sans`, §1.1); if you must webfont CJK, self-host a subset from a China CDN (full CJK webfonts are megabytes — avoid).
- Localize numerals/dates, names (provide `alternateName` in both scripts), and units. Professional human translation for combat-sports terminology; MT alone reads wrong to fans.
- For Baidu SEO (if hosting onshore): add Baidu-specific meta, submit to Baidu Search Console, and note Baidu weights on-page keywords and freshness more literally than Google.

### 5.7 QR-first UX norms

QR codes are the default bridge in China (follow an account, pay, open a Mini-Program, share a profile). Bake them into the UI:

```html
<div class="qr">
  <img src="/img/qr/wechat-oa.png" width="160" height="160"
       alt="扫码关注 ArenaDB 微信公众号" loading="lazy" decoding="async">
  <p class="card__meta">微信扫一扫，关注公众号</p>
</div>
```
```css
.qr { display:inline-grid; gap:var(--sp-2); justify-items:center; padding:var(--sp-4);
      background:var(--c-bg-elev-1); border:1px solid var(--c-line); border-radius:var(--r-lg); }
.qr img { background:#fff; padding:8px; border-radius:var(--r-md); } /* white quiet-zone for scan reliability */
```
Norms: put QR codes on every share point (follow OA, open Mini-Program, WeChat Pay, share fighter card). Keep a **white quiet-zone** around the code, ≥160px on screen, high contrast. Offer "长按识别二维码" (long-press to recognize) for in-app viewing where the camera isn't available.

**China sources:**
- Chinafy, "2025 guide to ICP licences in China" — <https://www.chinafy.com/blog/a-2025-guide-to-icp-licences-in-china-do-i-need-an-icp-license-for-my-website>
- Chinafy, "ICP License vs No ICP License" — <https://www.chinafy.com/blog/icp-license-vs-no-icp-license-do-you-need-one-for-your-website-to-work-in-china>
- MS Advisory, "ICP License in China (2026)" — <https://msadvisory.com/icp-license-china/>
- Nanjing Marketing Group, "Six Chinese Social Media Platforms" — <https://nanjingmarketinggroup.com/blog/six-chinese-social-media-platforms>
- BWB Agency, "What is Bilibili (2025)" — <https://bwb.agency/latest-news/what-is-bilibili-the-cultural-force-of-china-s-younger-generation-and-opportunities-for-brands-in-2025>
- Extrabux, "Top 13 Chinese Social Media Platforms 2025" — <https://www.extrabux.com/en/guide/8872844>
- Lei Mao, "Embed Bilibili Video" (iframe params) — <https://leimao.github.io/blog/Embed-Bilibili-Video/>
- Iframely, Youku/Bilibili embed references — <https://iframely.com/domains/youku> · <https://iframely.com/domains/bilibili>

---

### Appendix — file layout (no build step)

```
/index.html
/fighter/khabib-nurmagomedov/index.html
/zh/fighter/khabib-nurmagomedov/index.html
/css/design-tokens.css   /css/base.css   /css/components.css
/js/facade.js
/robots.txt   /sitemap.xml   /llms.txt
/img/...  /fonts/...
```
Load CSS as one bundle (concatenate the files) or inline critical tokens+base in `<head>` and link the rest. One `facade.js`, deferred:
```html
<link rel="stylesheet" href="/css/site.css">
<script src="/js/facade.js" defer></script>
```
