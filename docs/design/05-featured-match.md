# 05 — Featured Match (gradient-border poster card)

## Purpose
"Show, don't tell." One editorial, asymmetric hero-match poster proves the database is deep
and *fun to explore*, and gives the paywall its context. It's the marquee "premium card"
moment — used **rarely** so the gradient border stays special.

## Layout & structure
- Breaks the uniform grid: one wide `.poster` inside a `.card--edge` gradient-border wrapper.
- `min-height:320px`, content bottom-aligned (`display:grid;align-items:end`), like a
  fight poster: oversized ghost monogram bleeding off the top-right, metadata bottom-left.
- **Layout options:**
  - Standalone full-width band (`.wrap`), or
  - The wide cell of a `.bento` grid (`.is-wide` = span 2) alongside smaller tiles.
- **Mobile:** full width, monogram scales down and stays clipped inside the card; meta stacks.

## Components & CSS classes
- `.card--edge` — the hairline gold→red gradient border via mask-composite; `::before`
  opacity `.55` → `1` on hover.
- `.poster` — red-tint radial + elevated surface; `align-items:end`.
- `.poster .tile__mono` — huge Anton ghost letters (`font-size:20rem`, bleeding
  `inset:auto -2.5rem -5rem auto`), `aria-hidden`.
- `.poster__meta` — the bottom-left content block (`z-index:2`).
- Inside meta: `.eyebrow`, an Anton match title, `.cluster` of chips
  (`.chip--wwe` etc. + `.chip--gold`), a `.ratingbox` (big gold rating), and a
  `.btn.btn--gold` "Read the breakdown".
- Optional `.chip--live` if it's a currently-trending pick.

## Content
- **Eyebrow:** `MATCH OF THE WEEK`
- **Title:** `THE UNDERTAKER vs SHAWN MICHAELS` (with a red `vs` in Oswald).
- **Sub-meta:** `WrestleMania 25 · March 2009 · Streak Match`
- **Chips:** `WWE` · `★ Classic` · `Streak`
- **Rating box:** `4.90` with `/ 5 · 2,100 ratings` small text.
- **Blurb (Inter, ≤2 lines):** `The night "Mr. WrestleMania" pushed the Deadman to his limit
  — a masterclass in near-fall storytelling.`
- **CTA:** `Read the breakdown →` (gold) linking to the match page.

## Interactions & motion
- **Gradient border warms** on hover/focus (`.card--edge:hover::before{opacity:1}`).
- Optional **pointer spotlight** by adding `.tile__spot` inside the poster (rAF writes
  `--mx/--my`), for a gold glow that tracks the cursor.
- Card lift: reuse `.card` hover elevation or a small `translateY`.
- `[data-reveal]` on entry.
- Reduced motion: border still warms (opacity, instant), no lift/spotlight motion.

## Accessibility
- The card is one primary link; make the title an `<a>` and use a stretched-link pattern
  (`.card__link::after` covers the card) so the whole poster is clickable while the accessible
  name is the title.
- Monogram is `aria-hidden`; the rating exposes `aria-label="Rated 4.90 out of 5"` on the
  `.ratingbox`.
- Chips convey meaning via text, not color alone.
- Sufficient contrast: `.poster__meta` sits over the darker bottom of the surface; add a
  subtle bottom scrim if a bright tint reduces legibility.

## SEO/GEO notes
- Mark up as part of the page's content with a real `<a href>` to the match entity.
- Consider `Review`/`AggregateRating` schema on the match's own page (not required on the
  homepage teaser).
- The blurb's first sentence is answer-first/definitional — good AI-liftable phrasing.
