# 03 — Stats Bar (glass social-proof strip)

## Purpose
Immediately answer "is this legit / is anyone here?" right after the hero's promise. A slim
glass strip of hard, specific counts reduces first-impression risk before we ask for
anything, and the numbers double as citation-worthy GEO stats.

## Layout & structure
- `.stats-bar` is a `.glass` panel that **overlaps the hero's bottom edge**
  (`margin:-3rem auto 0`, `position:relative`, `z-index:3`) so it floats over the angled cut
  — the textbook use of glassmorphism (a floating element over content/color).
- Width `min(100% - 2rem, --wrap)`, centered.
- **Grid:** 2 columns on mobile → 5 columns at `≥720px`
  (`grid-template-columns:repeat(5,1fr)`), centered text.
- Each cell = big Anton number + Oswald uppercase label.

## Components & CSS classes
- `.glass` (blur + saturate, hairline border, `--edge-light`, `@supports` solid fallback).
- `.stats-bar` (the grid + overlap positioning).
- `.stats-bar .s-num` (Anton, `--fs-800`, `--c-gold-bright`).
- `.stats-bar .s-lbl` (muted, uppercase, `.1em` tracking, `--fs-300`).
- Number spans carry `data-countup` attributes for the count-up animation (see 00 §6 and
  the motion research count-up module).

## Content
Five stats (real, specific, dated where possible):

| Number | Label |
|---|---|
| `41` | Legends indexed |
| `30` | Five-star classics |
| `15` | Defining rivalries |
| `4.87★` | Top match rating |
| `12,000+` | Fans on the waitlist |

Optional caption for GEO (visually `.dim`, `--fs-300`): `Database current as of 2026.`

## Interactions & motion
- **Count-up on scroll:** each `.s-num` uses `data-countup="<final>"` (+ optional
  `data-decimals`, `data-suffix`). An `IntersectionObserver` (threshold ~0.6) fires a
  `requestAnimationFrame` + `easeOutExpo` tween once, then unobserves. Uses
  `Intl.NumberFormat` for locale-correct separators.
- **Reduced motion:** the final value is written instantly — never a stuck "0".
- Subtle reveal: the whole bar can carry `[data-reveal]`.
- No hover behavior (it's a proof strip, not interactive).

## Accessibility
- Wrap in a labelled region: `<section aria-label="MAT by the numbers">` (it's proof, not a
  heading-worthy section).
- Each stat is a small group: number + label read together (`<div><b class="s-num">…</b>
  <span class="s-lbl">…</span></div>`); the label provides the accessible meaning.
- Count-up writes to `textContent` (screen readers announce the final value on focus/read,
  not every tick — keep the container out of an `aria-live` region).
- Contrast: gold numbers on the dark glass panel ≥ AA.

## SEO/GEO notes
- State the *number + unit + year in one sentence* somewhere adjacent ("30 five-star matches
  indexed as of 2026") — RAG/AI engines lift exactly this format for citations.
- Keep the final numbers in server-rendered HTML (the `0` placeholder is only a JS starting
  value; render the real number as the fallback text so non-JS/crawlers see truth).
