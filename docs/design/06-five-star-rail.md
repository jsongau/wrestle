# 06 — Five-Star Rail (duotone poster match tiles)

## Purpose
A rail of the greatest matches, rendered as duotone poster tiles. It proves database depth
with real, clickable, crawlable content and turns curiosity into "I need an account to keep
going." Doubles as an internal-linking hub for high-value "five-star match" entities.

## Layout & structure
- Standard editorial `.section-head` (eyebrow → H2 → `.rule-gold`; "All matches →" via
  `.link-more`), then a `.grid-spot` of `.tile`s.
- `.grid-spot` auto-fills `minmax(min(200px,100%),1fr)` → 4–6 across on desktop, 2 on small
  tablets, 1–2 on phones.
- Each tile is a **3:4 poster** (duotone media well) with a ghost monogram and a bottom
  body (kicker + match name). A rating badge sits bottom-right of the media.
- **Mobile:** grid collapses to 1–2 columns; consider horizontal scroll-snap for a
  Netflix-style rail (optional; keep tiles as real links either way).

## Components & CSS classes
- `.section-head`, `.eyebrow`, `.rule-gold`, `.link-more`.
- `.grid-spot` (the spotlight grid container — one delegated pointer listener drives all
  tiles).
- `.tile` (hover lift + gold-dim ring) with:
  - `.tile__media` (duotone gradient; angle driven by inline `--seed`; diagonal field-line
    texture via `::after`).
  - `.tile__mono` — Anton ghost letter/number, `aria-hidden`.
  - `.tile__spot` — the pointer-tracked gold radial glow (`--mx/--my`).
  - `.tile__body` → `.tile__kicker` + `.tile__name`.
  - `.tile__rating` — Anton gold rating chip, bottom-right of media.
  - `.tile__badge` — top-left status chip (e.g. `.chip--gold` "Classic").
- Use `.tile--gold` variant for the very top-rated (gold duotone instead of red) to signal
  status through color.

## Content
Section head: eyebrow `FIVE-STAR CLASSICS`, H2 `Matches that defined an era`.
Six tiles (seed the `--seed` per card for varied duotone angles):

| Monogram | Kicker | Name | Rating |
|---|---|---|---|
| `U` | WrestleMania 25 | Undertaker vs Michaels | ★4.90 |
| `A` | WrestleMania 13 | Austin vs Hart | ★5.00 |
| `O` | NJPW Dominion | Okada vs Omega | ★5.00 |
| `P` | Money in the Bank '11 | Punk vs Cena | ★4.75 |
| `F` | Chi-Town Rumble | Flair vs Steamboat | ★4.85 |
| `H` | Hell in a Cell '98 | Undertaker vs Foley | ★4.60 |

## Interactions & motion
- **Pointer spotlight:** one delegated `pointermove` listener on `.grid-spot` writes
  `--mx/--my` to the hovered `.tile` (rAF-throttled); `.tile__spot` fades in. Gated to
  fine-pointer devices.
- **Hover elevation:** `.tile:hover` lifts `translateY(-4px)`, warms border, and the
  `.tile__mono` shifts toward gold.
- **Scroll reveal + stagger:** tiles carry `[data-reveal]` with `style="--i:0…"` for a
  cascade (capped delay).
- Reduced motion: reveals show instantly; spotlight listener not attached; no lift.

## Accessibility
- Each `.tile` is a single `<a href>` to the match page; `.tile__mono`, `.tile__spot`, and
  the texture layer are `aria-hidden`.
- Rating badge includes text ("★4.90"), not color-only; expose `aria-label` on the tile
  linking name + rating ("Undertaker vs Michaels, rated 4.90").
- Focus ring visible; hover and `:focus-visible` produce the same affordance.
- Keep tile names as real text (Oswald), not baked into an image.

## SEO/GEO notes
- Real internal links build topical depth; wrap the rail as an `ItemList` (JSON-LD) with each
  match as an item for rich understanding + AI citation.
- Match names + ratings + event in text = citation-ready entity facts.
- Card text is server-rendered; any images lazy-load but text never depends on JS.
