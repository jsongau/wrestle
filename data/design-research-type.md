# Arena — Premium Type & Visual System

Type + visual-system guidance for a dark, editorial, athletic pro-wrestling site.
Scope: static site. Global edition may use Google Fonts or self-hosted WOFF2. **China edition must not call Google Fonts** — use self-hosted subsets + a system-CJK fallback stack (details in §1.4).

Design north star: **broadcast-graphic energy meets editorial restraint.** Big condensed
display headers, generous negative space, one hero accent per view, gold as jewelry (not
paint), blood-red as the alarm you use sparingly.

Palette anchors: black canvas, gold `#d4af37`, blood-red `#c8102e`.

---

## Table of contents

1. [Font pairing](#1-font-pairing)
2. [Fluid type scale + heading treatments](#2-fluid-type-scale--heading-treatments)
3. [Color / gradient tokens](#3-color--gradient-tokens)
4. [Texture, noise & glassmorphism](#4-texture-noise--glassmorphism)
5. [Components: buttons, chips, badges, rating meters](#5-components-buttons-chips-badges-rating-meters)
6. [Sources](#6-sources)

---

## 1. Font pairing

### 1.0 Principle

A condensed athletic display face gives the "arena / fight-card" shout; a neutral,
high-x-height body sans keeps long copy calm and legible. **Contrast, don't compete:** pair
a *loud, narrow, all-caps* display with a *quiet, humanist, mixed-case* body. Typewolf's
real-world Bebas Neue samples confirm the pattern — condensed caps display sits over neutral
body faces (GT America, Montserrat, Tiempos Text). ([Typewolf](https://www.typewolf.com/bebas-neue))

Load **two families max** for performance. A third "numerals/label" face is optional and
should be a weight of the display, not a new family.

---

### 1.1 Pairing A — **Anton + Inter** (recommended)

The most "broadcast" option. Anton is a single ultra-heavy grotesque condensed weight —
reads like a title card / lower-third. Inter is the modern neutral workhorse for UI and body,
with a huge weight range, tabular figures, and excellent hinting on screens.

Why it wins for this brand: Anton's single 900-ish weight is *tiny to load* (one file), hits
hardest at large sizes, and never tempts you into using the display face for body. Inter
covers everything else (nav, tables, stat blocks, paragraphs) with one variable file.

**Google Fonts embed (global edition):**

```html
<!-- in <head>, before your CSS -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link
  href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700;800&display=swap"
  rel="stylesheet">
```

**Preload the hero display file** (Anton is used above the fold; preload only what paints first):

```html
<!-- Preload the actual woff2 Google serves for Anton (URL is stable per-family; grab from the css2 response) -->
<link rel="preload" as="font" type="font/woff2" crossorigin
  href="https://fonts.gstatic.com/s/anton/v25/1Ptgg87LROyAm3Kz-C8.woff2">
```

Weights to load: **Anton 400** (its only weight; render it big), **Inter 400/500/600/700**
(add 800 only if you need a heavy body callout). Skip 100–300 — they disappear on a black bg.

---

### 1.2 Pairing B — **Bebas Neue + Inter** (editorial / clean)

Bebas Neue is taller, tighter, and more "poster" than Anton — great for vertical fight-card
stacks and oversized names. It is **uppercase-only**, so it is display-only by design
(Typewolf notes this limits it to headlines). Pair again with Inter for body.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link
  href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;500;600;700&display=swap"
  rel="stylesheet">
```

Weights: **Bebas Neue 400** (single weight), **Inter 400/500/600/700**.
Because Bebas is thin-stroked, give it heavy tracking control and large sizes only
(see §2.3). Use it when you want *elegant* over *brutal*.

---

### 1.3 Pairing C — **Archivo Expanded / Oswald + Source Sans 3** (self-hosted, expressive)

For a system that wants width *and* weight variation, use a variable display grotesque:

- **Oswald** (variable 200–700, condensed) — flexible weights, superb for kickers,
  eyebrows, and multi-weight scoreboards.
- or **Archivo** + **Archivo Expanded** (variable) — lets you go *wide* for section
  dividers and *condensed* for stat rails from one superfamily; very editorial-magazine.

Body: **Source Sans 3** (or keep Inter). Source Sans reads slightly warmer than Inter for
long articles.

**Self-hosted `@font-face` (works for both global and China editions):**

```css
/* Display: Oswald variable */
@font-face {
  font-family: "Oswald";
  src: url("/fonts/oswald-var.woff2") format("woff2-variations");
  font-weight: 200 700;          /* variable range */
  font-style: normal;
  font-display: swap;            /* show fallback immediately, swap when ready */
  font-named-instance: "Bold";
}

/* Body: Inter variable (subset — Latin only) */
@font-face {
  font-family: "Inter";
  src: url("/fonts/inter-var-latin.woff2") format("woff2-variations");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+2000-206F, U+2074,
                 U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
```

---

### 1.4 China edition — CJK fallback (no Google Fonts)

Do **not** ship a multi-megabyte CJK webfont. Use the platform's high-quality system CJK
faces and only self-host the *Latin* display + body subsets.

```css
:root {
  /* Latin display + body are self-hosted woff2 subsets; CJK falls through to the OS */
  --font-display: "Anton", "Oswald", "PingFang SC", "Microsoft YaHei", "Hiragino Sans GB", sans-serif;
  --font-body: "Inter", "PingFang SC", "HarmonyOS Sans SC", "Microsoft YaHei",
               "Hiragino Sans GB", "Noto Sans CJK SC", sans-serif;
}
```

Notes for the China build:
- Self-host all Latin woff2 from your own origin / a China CDN. Never `preconnect` to
  `fonts.gstatic.com` (blocked/slow behind the GFW).
- `PingFang SC` covers iOS/macOS; `Microsoft YaHei` covers Windows; `HarmonyOS Sans SC` /
  `Noto Sans CJK SC` cover Android/Huawei/Linux.
- Because the display face never renders CJK glyphs, CJK headings automatically fall to
  `PingFang SC` bold — set `font-weight: 700` on CJK headings so they still read as titles.

---

### 1.5 Performance checklist (all editions)

- **`font-display: swap`** on every `@font-face` — text paints immediately in the fallback,
  then swaps. Avoids invisible-text (FOIT) on slow arena Wi-Fi. ([MDN / web.dev](https://web.dev/articles/font-display))
- **Preload only above-the-fold fonts** (the display face + body regular). Preloading
  everything hurts LCP.
- **Subset aggressively.** Latin-only subsets cut Inter/Oswald by 60–80%. Use
  `glyphhanger` or `fonttools pyftsubset` and the `unicode-range` above.
- **Prefer variable fonts** for body (one file = all weights) but a *static single-weight*
  file for Anton/Bebas (they only have one weight — no variable benefit).
- **Self-host for control** even on the global edition if you want to avoid the extra
  `fonts.gstatic.com` connection; Google Fonts is fine but adds one cross-origin hop.
- Set a **`size-adjust` / fallback face** to reduce layout shift (CLS) during swap:

```css
@font-face {
  font-family: "Inter-fallback";
  src: local("Arial");
  size-adjust: 107%;        /* tune so fallback metrics ≈ Inter, minimizing CLS */
  ascent-override: 90%;
  descent-override: 22%;
  line-gap-override: 0%;
}
:root { --font-body: "Inter", "Inter-fallback", system-ui, sans-serif; }
```

---

## 2. Fluid type scale + heading treatments

### 2.1 The scale (clamp-based, no media queries)

Built the Utopia way: define a **min viewport (360px)** and **max viewport (1240px)**, a
smaller ratio on mobile (~1.2 minor-third) and a bolder ratio on desktop (~1.28) so headings
grow *faster* than body as the screen widens. Reference these tokens everywhere instead of
hand-writing `clamp()` per element. ([Utopia](https://utopia.fyi/blog/utopian-typography-is-easy/))

```css
:root {
  /* --- Fluid type scale: clamp(MIN, PREFERRED, MAX) ---
     PREFERRED mixes a rem base + vw slope so it scales between 360–1240px viewports. */
  --step--1: clamp(0.83rem, 0.80rem + 0.15vw, 0.94rem);  /* fine print / captions   */
  --step-0:  clamp(1.00rem, 0.95rem + 0.25vw, 1.13rem);  /* body                     */
  --step-1:  clamp(1.20rem, 1.10rem + 0.50vw, 1.50rem);  /* lead / large body        */
  --step-2:  clamp(1.44rem, 1.25rem + 0.95vw, 2.00rem);  /* h4 / card titles         */
  --step-3:  clamp(1.73rem, 1.40rem + 1.60vw, 2.67rem);  /* h3 / section subhead      */
  --step-4:  clamp(2.07rem, 1.55rem + 2.60vw, 3.55rem);  /* h2                        */
  --step-5:  clamp(2.49rem, 1.65rem + 4.20vw, 4.74rem);  /* h1                        */
  --step-6:  clamp(2.99rem, 1.50rem + 7.40vw, 6.31rem);  /* hero / fight-card name    */
  --step-7:  clamp(3.58rem, 0.90rem + 13.4vw, 8.42rem);  /* poster / oversized        */

  /* Line-height + tracking tokens */
  --lh-tight: 0.92;   /* stacked display */
  --lh-snug:  1.05;   /* single-line headings */
  --lh-body:  1.6;    /* paragraphs */
  --track-display: -0.01em;  /* condensed caps: slight negative or 0 */
  --track-kicker:  0.22em;   /* wide-spaced eyebrows/labels */
}
```

### 2.2 Base element mapping

```css
html { -webkit-text-size-adjust: 100%; }
body {
  font-family: var(--font-body);
  font-size: var(--step-0);
  line-height: var(--lh-body);
  font-feature-settings: "cv11" 1, "ss01" 1; /* Inter: nicer 1, a, g (optional) */
  text-rendering: optimizeLegibility;
}

h1, h2, h3, .display {
  font-family: var(--font-display);
  line-height: var(--lh-snug);
  letter-spacing: var(--track-display);
  text-transform: uppercase;   /* Anton/Bebas are caps-forward */
  text-wrap: balance;          /* avoids orphan words in headlines */
}
h1 { font-size: var(--step-5); }
h2 { font-size: var(--step-4); }
h3 { font-size: var(--step-3); line-height: var(--lh-snug); }

.hero-name { font-size: var(--step-6); line-height: var(--lh-tight); }
.poster    { font-size: var(--step-7); line-height: 0.86; }

/* Eyebrow / kicker — the wide-tracked label above a headline */
.kicker {
  font-family: var(--font-body);
  font-size: var(--step--1);
  font-weight: 600;
  letter-spacing: var(--track-kicker);
  text-transform: uppercase;
  color: var(--gold);
}

p { max-width: 68ch; }  /* measure control for readability */
```

### 2.3 Heading treatments (copy-ready recipes)

**a) Gradient text (gold foil headline):**

```css
.text-gold-foil {
  background: var(--grad-gold-foil);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  -webkit-text-fill-color: transparent;
}
```

**b) Outline / stroke text (empty "ghost" numerals & words):**

```css
.text-outline {
  color: transparent;
  -webkit-text-stroke: 1.5px var(--gold);
  text-stroke: 1.5px var(--gold);
  paint-order: stroke fill;
}
/* Fallback for non-webkit engines */
@supports not (-webkit-text-stroke: 1px red) {
  .text-outline { color: var(--gold); }
}
```

**c) Oversized numerals (scoreboard / ranking):** load Inter's **tabular figures** so digits
align in columns, and use the poster step.

```css
.numeral-xl {
  font-family: var(--font-display);
  font-size: var(--step-7);
  line-height: 0.8;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
}
/* "Ghost rank" behind a card: huge outline numeral */
.rank-ghost {
  font-size: clamp(6rem, 18vw, 14rem);
  color: transparent;
  -webkit-text-stroke: 2px color-mix(in srgb, var(--gold) 35%, transparent);
  position: absolute; inset: auto -0.1em -0.15em auto; z-index: 0; pointer-events: none;
}
```

**d) Duotone / stroked hybrid headline (fill + red underglow):**

```css
.headline-arena {
  color: var(--paper);
  text-shadow:
    0 0 1px rgba(0,0,0,.4),
    0 0 24px color-mix(in srgb, var(--blood) 45%, transparent);
}
```

**e) Transforms & tracking rules of thumb:**
- Condensed caps display (Anton/Bebas): tracking `-0.01em` to `0` — they're already tight.
- All-caps *body-size* labels: **add** tracking `0.08–0.22em` (caps need air).
- Never letter-space lowercase body text.
- Use `text-wrap: balance` on headings, `text-wrap: pretty` on paragraphs.

---

## 3. Color / gradient tokens

Black canvas + gold jewelry + blood-red alarm. Includes layered gradients, glows, duotone,
and gradient borders. All copy-ready as custom properties.

```css
:root {
  /* --- Core brand --- */
  --gold:        #d4af37;
  --blood:       #c8102e;

  /* --- Neutrals (warm-black arena, not pure #000) --- */
  --ink-900:     #0a0a0b;   /* page background */
  --ink-850:     #101012;
  --ink-800:     #16161a;   /* raised surface */
  --ink-700:     #1e1e24;   /* card */
  --ink-600:     #2a2a32;   /* border / hairline base */
  --paper:       #f4f2ec;   /* off-white text (never pure #fff on black) */
  --paper-dim:   #b9b6ad;   /* secondary text */
  --paper-faint: #6f6c66;   /* tertiary / meta */

  /* --- Gold ramp (for depth, hover, foil) --- */
  --gold-100:    #f7ecc4;
  --gold-300:    #e8cf7a;
  --gold-500:    #d4af37;   /* = --gold */
  --gold-700:    #a9832a;
  --gold-900:    #6e531a;

  /* --- Blood ramp --- */
  --blood-100:   #ff6b7d;
  --blood-300:   #e83350;
  --blood-500:   #c8102e;   /* = --blood */
  --blood-700:   #8f0a20;
  --blood-900:   #560414;

  /* --- Alpha tokens (for glows/borders over dark) --- */
  --gold-a12:    color-mix(in srgb, var(--gold) 12%, transparent);
  --gold-a25:    color-mix(in srgb, var(--gold) 25%, transparent);
  --gold-a40:    color-mix(in srgb, var(--gold) 40%, transparent);
  --blood-a30:   color-mix(in srgb, var(--blood) 30%, transparent);
  --white-a06:   rgba(255,255,255,.06);
  --white-a10:   rgba(255,255,255,.10);

  /* =========================================================
     GRADIENTS
     ========================================================= */

  /* Gold foil — for headline text-clip & premium fills */
  --grad-gold-foil: linear-gradient(
    100deg,
    var(--gold-900) 0%,
    var(--gold-500) 22%,
    var(--gold-100) 42%,
    var(--gold-500) 58%,
    var(--gold-700) 78%,
    var(--gold-300) 100%
  );

  /* Blood → ink — hero wash / CTA */
  --grad-blood: linear-gradient(135deg, var(--blood-700) 0%, var(--blood-500) 55%, #7a0a1c 100%);

  /* Arena hero — layered radial spotlights + red rake over warm black */
  --grad-arena: 
    radial-gradient(120% 80% at 20% 0%, var(--gold-a12) 0%, transparent 45%),
    radial-gradient(90% 70% at 90% 10%, var(--blood-a30) 0%, transparent 40%),
    linear-gradient(180deg, var(--ink-850) 0%, var(--ink-900) 100%);

  /* Spotlight — single overhead cone for feature cards */
  --grad-spotlight: radial-gradient(140% 100% at 50% -10%,
    rgba(255,255,255,.10) 0%, transparent 42%);

  /* Duotone recipe — layer OVER a grayscale <img> via mix-blend */
  --duotone-shadow: var(--blood-900);
  --duotone-highlight: var(--gold-300);

  /* =========================================================
     GLOWS / SHADOWS
     ========================================================= */
  --glow-gold:  0 0 0 1px var(--gold-a25), 0 8px 30px -8px var(--gold-a40);
  --glow-blood: 0 0 0 1px var(--blood-a30), 0 10px 40px -10px color-mix(in srgb, var(--blood) 55%, transparent);
  --shadow-card: 0 1px 0 var(--white-a06) inset, 0 20px 50px -20px rgba(0,0,0,.8);
  --shadow-lift: 0 30px 60px -25px rgba(0,0,0,.9);
}
```

### 3.1 Gradient border (gold rim on dark card)

Uses the double-background / `border` transparent + `background-origin` trick so the border
itself is a gradient:

```css
.rim-gold {
  border: 1px solid transparent;
  border-radius: 14px;
  background:
    linear-gradient(var(--ink-700), var(--ink-700)) padding-box,
    var(--grad-gold-foil) border-box;
}
/* Animated conic sheen version (feature card) */
.rim-conic {
  position: relative; border-radius: 16px; background: var(--ink-700);
}
.rim-conic::before {
  content: ""; position: absolute; inset: 0; border-radius: inherit; padding: 1px;
  background: conic-gradient(from var(--a,0deg),
    var(--gold-900), var(--gold-300), var(--blood-500), var(--gold-500), var(--gold-900));
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor; mask-composite: exclude;
  animation: rim-spin 6s linear infinite;
}
@property --a { syntax: "<angle>"; inherits: false; initial-value: 0deg; }
@keyframes rim-spin { to { --a: 360deg; } }
@media (prefers-reduced-motion: reduce) { .rim-conic::before { animation: none; } }
```

### 3.2 Duotone image recipe

```css
.duotone { position: relative; isolation: isolate; }
.duotone img { width: 100%; display: block; filter: grayscale(1) contrast(1.15); }
.duotone::after {
  content: ""; position: absolute; inset: 0; mix-blend-mode: color;
  background: linear-gradient(180deg, var(--duotone-shadow), var(--duotone-highlight));
}
.duotone::before {  /* deepen shadows */
  content: ""; position: absolute; inset: 0; z-index: 1; mix-blend-mode: multiply;
  background: var(--duotone-shadow); opacity: .55;
}
```

### 3.3 Usage rules

- **Gold = jewelry.** Borders, single words, ratings, small fills. Large gold fills look
  cheap; prefer the foil gradient or a hairline rim.
- **Red = alarm.** Live badges, destructive actions, "vs", key CTAs. One red moment per view.
- Text is `--paper` (#f4f2ec), never pure white on black (harsh, halates).
- Keep body text off gradients; gradients are for display type and surfaces only.
- Check contrast: gold `#d4af37` on `#0a0a0b` ≈ 8.9:1 (AAA for large, AA for small).
  Blood `#c8102e` on black ≈ 4.0:1 — **large text / non-text only**; pair with `--paper` for body.

---

## 4. Texture, noise & glassmorphism

### 4.1 SVG grain overlay (data-URI, zero HTTP request)

`feTurbulence` `fractalNoise` produces film-grain over any surface. Higher `baseFrequency` =
finer grain; keep opacity low (≈3–8%) so it's felt, not seen. ([freeCodeCamp](https://www.freecodecamp.org/news/grainy-css-backgrounds-using-svg-filters/), [CSS-Tricks: Grainy Gradients](https://css-tricks.com/grainy-gradients/))

```css
/* Global grain layer — add once to <body> or a fixed overlay element */
.grain::after {
  content: "";
  position: fixed; inset: 0; z-index: 9999; pointer-events: none;
  opacity: .05;                 /* 0.03–0.08 sweet spot */
  mix-blend-mode: overlay;      /* or 'soft-light' for gentler grain */
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  background-size: 140px 140px; /* tile the small SVG for crisp, cheap grain */
}
@media (prefers-reduced-motion: reduce) { /* grain is static, no change needed */ }
```

Notes:
- `%23` = `#`, `%25` = `%` inside the data URI — required for it to parse.
- Tile a small (≈140px) noise square via `background-size` instead of one huge SVG — much
  cheaper to rasterize.
- `mix-blend-mode: overlay` keeps grain visible in both shadows and highlights; `soft-light`
  is subtler for premium restraint.

### 4.2 Grainy gradient (noise fused into the hero wash)

```css
.hero {
  position: relative; isolation: isolate;
  background: var(--grad-arena);
}
.hero::before {                 /* grain scoped to hero only */
  content: ""; position: absolute; inset: 0; z-index: -1; opacity: .07;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23g)'/%3E%3C/svg%3E");
}
```

### 4.3 Tasteful glassmorphism (stat rail / sticky nav / modal)

Restrained: low blur, hairline top highlight, faint tint. Avoid frosted-everything.

```css
.glass {
  background: linear-gradient(
      180deg, rgba(255,255,255,.06), rgba(255,255,255,.02));
  -webkit-backdrop-filter: blur(14px) saturate(140%);
  backdrop-filter: blur(14px) saturate(140%);
  border: 1px solid var(--white-a10);
  border-radius: 16px;
  box-shadow:
    0 1px 0 rgba(255,255,255,.12) inset,   /* top hairline sheen */
    0 20px 50px -20px rgba(0,0,0,.7);
}
/* Fallback where backdrop-filter is unsupported: solid tinted panel */
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .glass { background: color-mix(in srgb, var(--ink-800) 92%, transparent); }
}
```

Rules: use glass over *busy* backgrounds only (hero, imagery). Never stack glass on glass.
Keep blur ≤ 16px; higher looks smeary and costs GPU on scroll.

---

## 5. Components: buttons, chips, badges, rating meters

All lean on the tokens from §3. Copy-ready.

### 5.1 Buttons

```css
.btn {
  --btn-fg: var(--paper);
  display: inline-flex; align-items: center; gap: .55em;
  font-family: var(--font-body);
  font-weight: 700; font-size: var(--step--1);
  letter-spacing: .06em; text-transform: uppercase;
  padding: .85em 1.6em; border-radius: 10px; border: 1px solid transparent;
  color: var(--btn-fg); cursor: pointer; text-decoration: none;
  transition: transform .15s ease, box-shadow .2s ease, background-color .2s ease;
}
.btn:active { transform: translateY(1px); }
.btn:focus-visible { outline: 2px solid var(--gold-300); outline-offset: 3px; }

/* Primary — blood CTA */
.btn--primary {
  background: var(--grad-blood);
  box-shadow: var(--glow-blood);
}
.btn--primary:hover { box-shadow: var(--glow-blood), var(--shadow-lift); transform: translateY(-1px); }

/* Gold — premium secondary (gradient rim, ghost fill) */
.btn--gold {
  color: var(--gold-100);
  background: linear-gradient(var(--ink-800), var(--ink-800)) padding-box,
              var(--grad-gold-foil) border-box;
  border: 1px solid transparent;
}
.btn--gold:hover {
  color: #1a1408;
  background: var(--grad-gold-foil) padding-box, var(--grad-gold-foil) border-box;
}

/* Ghost — quiet tertiary */
.btn--ghost {
  background: transparent; border-color: var(--ink-600); color: var(--paper-dim);
}
.btn--ghost:hover { border-color: var(--gold-a40); color: var(--paper); }
```

### 5.2 Chips (filters / tags)

```css
.chip {
  display: inline-flex; align-items: center; gap: .4em;
  font-size: var(--step--1); font-weight: 600; letter-spacing: .04em;
  padding: .4em .85em; border-radius: 999px;
  background: var(--ink-700); color: var(--paper-dim);
  border: 1px solid var(--ink-600);
  transition: .18s ease;
}
.chip:hover { color: var(--paper); border-color: var(--gold-a40); }
.chip[aria-pressed="true"], .chip--active {
  color: #1a1408; background: var(--gold-300); border-color: var(--gold);
}
.chip--live { color: var(--blood-100); border-color: var(--blood-a30); }
.chip--live::before {
  content: ""; width: .5em; height: .5em; border-radius: 50%;
  background: var(--blood-500); box-shadow: 0 0 0 0 var(--blood-a30);
  animation: pulse 1.6s ease-out infinite;
}
@keyframes pulse { to { box-shadow: 0 0 0 .6em transparent; } }
@media (prefers-reduced-motion: reduce) { .chip--live::before { animation: none; } }
```

### 5.3 Badges (rank / championship / status)

```css
.badge {
  display: inline-flex; align-items: center; gap: .35em;
  font-family: var(--font-display); font-size: var(--step--1);
  letter-spacing: .04em; text-transform: uppercase;
  padding: .3em .7em; border-radius: 6px; line-height: 1;
}
.badge--champ {                      /* gold foil title belt */
  color: #1a1408; background: var(--grad-gold-foil);
  box-shadow: var(--glow-gold);
}
.badge--rank {                       /* outline gold */
  color: var(--gold-100); border: 1px solid var(--gold-a40); background: var(--gold-a12);
}
.badge--live {
  color: var(--paper); background: var(--blood-500); box-shadow: var(--glow-blood);
}
```

### 5.4 Rating meter (star power / stats bar)

A premium segmented + gradient-fill meter. Accessible via `role="meter"`.

```css
/* Gradient bar meter (0–100) */
.meter {
  --val: 72;                          /* set inline: style="--val:88" */
  height: 10px; border-radius: 999px; overflow: hidden;
  background: var(--ink-600);
  box-shadow: inset 0 1px 2px rgba(0,0,0,.6);
}
.meter > i {
  display: block; height: 100%;
  width: calc(var(--val) * 1%);
  background: linear-gradient(90deg, var(--blood-500), var(--gold-500), var(--gold-100));
  box-shadow: 0 0 12px var(--gold-a40);
  border-radius: inherit;
  transition: width .6s cubic-bezier(.2,.8,.2,1);
}
```

```html
<div class="meter" role="meter" aria-valuenow="88" aria-valuemin="0" aria-valuemax="100"
     style="--val:88"><i></i></div>
```

**Segmented "pip" rating (5-notch power score):**

```css
.pips { display: inline-flex; gap: 4px; }
.pips > span {
  width: 22px; height: 6px; border-radius: 2px;
  background: var(--ink-600);
}
.pips > span[data-on] {
  background: var(--grad-gold-foil);
  box-shadow: 0 0 8px var(--gold-a40);
}
```

```html
<div class="pips" role="img" aria-label="Power rating 4 of 5">
  <span data-on></span><span data-on></span><span data-on></span><span data-on></span><span></span>
</div>
```

---

## 6. Sources

- [Typewolf — Bebas Neue pairings & similar fonts](https://www.typewolf.com/bebas-neue)
- [Utopia — Fluid responsive typography with clamp()](https://utopia.fyi/blog/utopian-typography-is-easy/) · [Type scale calculator](https://utopia.fyi/type/calculator/)
- [freeCodeCamp — Grainy CSS backgrounds using SVG filters](https://www.freecodecamp.org/news/grainy-css-backgrounds-using-svg-filters/)
- [CSS-Tricks — Grainy Gradients](https://css-tricks.com/grainy-gradients/)
- [Codrops — SVG filter effects: creating texture with feTurbulence](https://tympanus.net/codrops/2019/02/19/svg-filter-effects-creating-texture-with-feturbulence/)
- [web.dev — font-display / eliminate render-blocking font behavior](https://web.dev/articles/font-display)
- [Pimp my Type — Font pairings for Inter](https://pimpmytype.com/inter-pairings/)
- [Elementor — 30 best font pairings for web design](https://elementor.com/blog/font-pairing/)
- [Made Good Designs — Best condensed fonts](https://madegooddesigns.com/best-condensed-fonts/)
- Google Fonts: [Anton](https://fonts.google.com/specimen/Anton) · [Bebas Neue](https://fonts.google.com/specimen/Bebas+Neue) · [Oswald](https://fonts.google.com/specimen/Oswald) · [Archivo](https://fonts.google.com/specimen/Archivo) · [Inter](https://fonts.google.com/specimen/Inter)

_Note: verify the exact preload woff2 URL for Anton against the live `css2` response — Google
rotates the version hash (`/s/anton/vNN/...`) periodically._
