# 07 — Icons / Roster Rail (duotone wrestler tiles)

## Purpose
Put faces (well, monograms) to the database. A rail of iconic wrestlers rendered as duotone
poster tiles gives fans an immediate, browsable entry point into the roster, proves breadth,
and seeds internal links to the highest-traffic wrestler pages. Mirrors the five-star rail's
treatment so the page reads as one system.

## Layout & structure
- Same pattern as section 06: `.section-head` (eyebrow → H2 → `.rule-gold` + "Full roster →")
  over a `.grid-spot` of `.tile`s.
- 3:4 poster tiles; gold-duotone (`.tile--gold`) for champions/legends, red-duotone (default
  `.tile`) for everyone else — status through color per the 90/8/2 rule.
- **Mobile:** 2-up grid or horizontal scroll-snap rail.
- Optional filter chip row above the grid (`.pill-row` of `.chip`s: All · WWE · WCW · ECW ·
  Legends) — visual only on the homepage; deep filtering lives on `/wrestlers/`.

## Components & CSS classes
- `.section-head`, `.eyebrow`, `.rule-gold`, `.link-more`.
- `.pill-row` + `.chip` (+ promotion variants) for the optional filter row.
- `.grid-spot` → `.tile` / `.tile--gold` with:
  - `.tile__media` (duotone, per-card `--seed`), `.tile__mono` (Anton initial, `aria-hidden`),
    `.tile__spot` (pointer glow).
  - `.tile__body` → `.tile__kicker` (the nickname/gimmick) + `.tile__name`.
  - `.tile__badge` — `.chip--gold` "Champion" / `.chip--wwe` etc. top-left.

## Content
Section head: eyebrow `THE ICONS`, H2 `Legends of the squared circle`.
Eight tiles (kicker = nickname; vary `--seed`):

| Init | Kicker | Name | Tile |
|---|---|---|---|
| `U` | The Phenom | The Undertaker | `.tile--gold` |
| `A` | The Rattlesnake | Stone Cold Steve Austin | `.tile--gold` |
| `H` | The Game | Triple H | default |
| `F` | The Nature Boy | Ric Flair | `.tile--gold` |
| `M` | The Heartbreak Kid | Shawn Michaels | default |
| `R` | The Tribal Chief | Roman Reigns | default |
| `B` | The EST | Bianca Belair | default |
| `P` | Best in the World | CM Punk | default |

## Interactions & motion
- **Pointer spotlight** via the delegated `.grid-spot` listener (rAF, fine-pointer only).
- **Hover elevation** (`.tile:hover`), monogram warms to gold.
- **Scroll reveal + stagger** with `[data-reveal]` + `--i`.
- Optional filter chips toggle `aria-pressed`; on the homepage they can smooth-scroll to
  `/wrestlers/?filter=` rather than filtering in place (keeps content crawlable).
- Reduced motion: reveals show instantly; no spotlight/lift motion.

## Accessibility
- Each tile is one `<a href>` to the wrestler page; decorative layers `aria-hidden`.
- Tile accessible name = ring name (+ optionally nickname): `aria-label="The Undertaker,
  The Phenom"`.
- Filter chips are real `<button aria-pressed>` with visible focus; color is never the only
  signal (label text present).
- Champion status conveyed by the badge text, not just the gold duotone.

## SEO/GEO notes
- Highest-value internal links on the page — point to canonical wrestler entity pages.
- Wrap as an `ItemList` (JSON-LD); ring names + nicknames in text are strong entity signals
  for search and AI citation.
- Nicknames ("The Phenom", "The Rattlesnake") are common query phrasings — keeping them as
  visible text helps GEO.
