# 01 — Header & Mega Nav

## Purpose
Orientation + an always-available conversion path. The header keeps the primary action
("Join") reachable at any scroll depth (a persistent CTA is worth roughly +27% on
scroll-heavy pages) while giving fans fast routes into the database (Wrestlers · Matches ·
Storylines). It sets the broadcast tone in the first 60px: Anton wordmark, gold mark, a
red Join button.

## Layout & structure
- Sticky top bar, `min-height:60px`, full-bleed with a `.wrap`-width `.nav` inside.
- Row order (desktop): **brand (left) · mega-nav menu · `.nav__spacer` · secondary "Browse
  free" (ghost) · primary "Join" CTA (red)**.
- **Breakpoints:**
  - `≥901px` — horizontal `.nav__menu` with hover/focus mega panels; `.nav__toggle` hidden.
  - `≤900px` — menu collapses to a fixed full-width drawer (`transform:translateY(-120%)` →
    `.is-open`); mega panels render stacked/static inside the drawer; **the Join CTA stays
    visible in the bar** (do not hide it behind the hamburger).
- Mobile companion: a **bottom sticky CTA bar** ("Join the waitlist →") appears after the
  user scrolls past the hero (see Interactions).

## Components & CSS classes
- `.site-header` — sticky, blurred `color-mix` background; `.is-stuck` adds shadow +
  stronger border after scroll.
- `.nav`, `.nav__spacer`, `.nav__toggle` (44×44 hamburger).
- `.brand` (Anton, `1.5rem`, uppercase) + `.brand__mark` (gold metallic square, skewed
  glyph) + `.brand__mark span`.
- `.nav__menu` / `.nav__item` / `.nav__link` (`aria-expanded` gets a `▾`).
- `.mega` / `.mega--wide` (2- or 3-col panel) / `.mega__col h3` / `.mega__link` (`b` + `small`).
- `.nav__cta` — the red gradient Join button (Oswald, uppercase, `--glow-red`).
- Add `.btn.btn--ghost` (or reuse `.link-more`) for the low-friction "Browse free".

## Content
- **Brand:** `MAT` (mark = stylized "M"/belt glyph in `.brand__mark span`).
- **Top-level nav:** `Wrestlers` · `Matches` · `Storylines` · `Rankings` · `Membership`.
- **Mega panel — Wrestlers** (`.mega--wide`): columns "By Promotion" (WWE, WCW, ECW, TNA,
  NXT), "By Era" (Golden, Attitude, Ruthless Aggression, PG, Modern), "Browse" (A–Z index,
  Champions, Hall of Fame) — each `.mega__link` with `<b>Label</b><small>one-line hint</small>`.
- **Mega panel — Matches:** "Five-Star Classics", "By Match Type", "This Week in History",
  "Recently Added".
- **Secondary CTA:** `Browse free` (ghost).
- **Primary CTA:** `Join` (`.nav__cta`). Mobile bottom bar: `Join the waitlist →`.

## Interactions & motion
- **Sticky shadow:** a 1px sentinel above the header + `IntersectionObserver` toggles
  `.site-header.is-stuck` when the top scrolls out of view (no scroll listener). Transitions
  border-color/box-shadow only.
- **Mega panels:** open on `:hover` and `:focus-within` (CSS `opacity/visibility/transform`),
  and on click via `.mega.is-open` (JS toggles `aria-expanded` for keyboard/touch).
- **Mobile drawer:** `.nav__toggle` toggles `.nav__menu.is-open`; each parent toggles its
  child `.mega.is-open`.
- **Bottom sticky CTA (mobile):** an `IntersectionObserver` on a hero sentinel adds/removes a
  `.hide` class on the bar so it appears only past the hero.
- Reduced motion: all handled by the global reset; panel show/hide still works (opacity snap).

## Accessibility
- `<header>` contains `<nav aria-label="Primary">`.
- `.nav__toggle` has `aria-expanded` + `aria-controls="primary-menu"` and an
  `aria-label="Menu"`.
- Mega triggers are real `<button>`/`<a aria-haspopup="true" aria-expanded>`; panels are
  keyboard-reachable (`:focus-within` opens them) and `Esc` closes.
- Skip link (`.skip-link`) targets `#main`.
- Tap targets ≥44px; visible focus ring on every link/button.

## SEO/GEO notes
- Nav links are real crawlable `<a href>` hubs — primary internal-linking surface into the
  database; keep them in server-rendered HTML.
- Brand wordmark wrapped so the accessible name is "MAT — The Ultimate Pro Wrestling Database"
  (aria-label on the brand link) to reinforce the Organization entity.
