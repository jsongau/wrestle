# 02 — Hero (Broadcast)

## Purpose
Hook the wrestling fan in under 5 seconds, state exactly what MAT is and who it's for, and
present the first (above-the-fold) CTA — the single highest-leverage element on the page.
The hero is where "no photography" is won: drama is built from **light + oversized type +
grain**, then given one angled cut for fight-poster momentum.

## Layout & structure
- `.hero-bb` — full-bleed section, `min-height:clamp(600px,90vh,940px)`, `display:grid`
  vertically centered, with a **diagonal bottom clip**
  (`clip-path:polygon(0 0,100% 0,100% calc(100% - 4vw),0 100%)`); the next section pulls up
  `margin-top:-2vw` to tuck into the notch.
- `.hero-bb__inner` (inside `.wrap`): single column on mobile → two columns at `≥860px`
  (`1.15fr .85fr`): copy left, a live database "proof" card right.
- **Mobile:** headline → lede → CTA cluster stacked, CTA above the fold; the proof card
  drops below the CTAs. Keep the angle shallow so it never clips text.
- Layered background (back→front): `.hero-bb__bg` (two radial spotlights + conic stage
  sweep) → `.hero-bb__grain` → `.hero-bb::after` vignette → content.

## Components & CSS classes
- `.hero-bb`, `.hero-bb__bg` (`aria-hidden`), `.hero-bb__grain` (`aria-hidden`),
  `.hero-bb__inner`.
- `.hero-bb__title` (Anton, `clamp(3rem,7.5vw+.5rem,8rem)`, `line-height:.9`) with
  `.accent` (gold-foil clipped line) and optional `.stroke` (outline "shout" line).
- `.hero-bb__lede` (Inter, `--fs-500`, muted, ≤52ch).
- `.eyebrow` for the kicker.
- CTA cluster: `.cluster` with `.btn.btn--gold.btn--lg` (primary) + `.btn.btn--ghost.btn--lg`
  (secondary). Micro-trust line under the cluster (`.form-note` / `.muted`).
- Proof card: reuse `.hero__card` / `.hero__card-body` (or a `.tile`) showing a real
  wrestler/match record — interactive real content beats a stock image and proves depth.

## Content
- **Eyebrow:** `THE ULTIMATE PRO-WRESTLING DATABASE`
- **H1 (`.hero-bb__title`):**
  `EVERY RIVALRY.` / `EVERY MATCH.` / `<span class="accent">EVERY LEGEND.</span>`
- **Lede:** `Four decades of storylines, five-star matches, and the feuds that defined an
  era — indexed, ranked, and remembered.`
- **Primary CTA:** `Explore the Roster` → `/wrestlers/` (gold) — or, in waitlist mode,
  `Get early access` (see section 09 for the conversion-primary variant).
- **Secondary CTA:** `Join MAT Insider` → `/membership/` (ghost).
- **Micro-trust cue:** `Free to browse. No card required. · 12,000+ fans on the list.`
- **Proof card:** a real "Tale of the Tape" or top-rated match snippet (name, rating,
  promotion chip) linking into the database.

## Interactions & motion
- **Mesh drift:** `.hero-bb__bg` animates `background-position` via `@keyframes heroDrift`
  (26s, `ease-in-out`, alternate) — GPU-cheap, `background-position` only. Disabled under
  reduced motion.
- **Pointer parallax:** a tiny rAF-throttled listener writes `--px/--py` custom props to
  `.hero-bb__bg` (which has `transition:transform .4s` + `scale(1.06)` to avoid edge gaps).
  Bails at init under reduced motion or non-fine pointers.
- **Scroll reveal:** eyebrow/title/lede/CTA can carry `[data-reveal]` with `--i` stagger for
  a broadcast "build-on" (optional; keep the hero mostly instant for LCP).
- **CTA shine:** `.btn--gold::after` sweep on hover (auto-off under reduced motion).

## Accessibility
- Exactly one `<h1>` on the page lives here; keep the `<br>`-split lines inside a single
  `<h1>` (use `&nbsp;` to avoid awkward mid-phrase breaks).
- All background layers `aria-hidden="true"`.
- CTAs are the first tab stops after the nav; visible focus rings; secondary CTA is a real
  link for SEO visitors (the low-friction escape hatch).
- Contrast: white/`--c-text` copy sits over the vignette-darkened center (≥55% transparent
  radius keeps the middle dark enough); gold `.accent` line is decorative-large so its
  contrast is fine.

## SEO/GEO notes
- The H1 carries the primary entity/keyword ("pro-wrestling database") for search + GEO.
- Hero copy is static HTML (LCP text). Preload Anton so the title paints fast.
- The proof card links to real internal pages, seeding topical depth from the top of the DOM.
