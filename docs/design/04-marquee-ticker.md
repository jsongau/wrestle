# 04 — Marquee Ticker (five-star match ratings)

## Purpose
A broadcast lower-third "scores ticker" that scrolls recent five-star match ratings. It does
three jobs: reinforces that the database is *deep and current*, adds kinetic broadcast energy
between the static hero/stats and the content rails, and teases real match entities as
internal links.

## Layout & structure
- Full-bleed `.marquee` strip, `overflow:hidden`, hairline border top+bottom, with an
  **edge-fade mask** (`mask:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent)`)
  so items dissolve at both ends instead of hard-clipping (the premium tell).
- `.marquee__track` is `width:max-content`, a horizontal flex row, animated `translateX`.
- **Seamless loop:** duplicate the item set inside the track (or two tracks) and translate by
  `-50%` so the seam is invisible; the clone set is `aria-hidden`.
- Height is compact (`padding-block:--sp-3`); sits directly under the stats bar.

## Components & CSS classes
- `.marquee` (clip + mask + `--c-bg-elev-1` background).
- `.marquee__track` (`animation:marquee 42s linear infinite`; pauses on `.marquee:hover`).
- `.marquee__item` (Oswald, uppercase, `.04em`) with `<b>` for the rating and `.dot`
  (red separator).
- `@keyframes marquee{to{transform:translateX(-50%)}}`.

## Content
Format per item: `Match name` · `★ rating` (gold `<b>`), separated by a red `.dot` (`•`).
Example set (repeat/duplicate for the loop):

- `Bret Hart vs Stone Cold — WM13` **★4.75** •
- `Undertaker vs Shawn Michaels — WM25` **★4.90** •
- `Punk vs Cena — MITB '11` **★4.75** •
- `Okada vs Omega — Dominion` **★5.00** •
- `Flair vs Steamboat — Chi-Town` **★4.85** •
- `Austin vs Hart — WM13` **★5.00** •
- `Rollins vs Punk` **★4.50** •
- `Ripley vs Belair` **★4.25** •

Optional leading label chip (Oswald): `LATEST RATINGS`.

## Interactions & motion
- **Scroll:** pure CSS `translateX` (compositor-only). `--speed`/duration ~42s reads calm and
  premium — set speed by content length, not viewport width.
- **Pause on hover** so users can read/click an item (`animation-play-state:paused`).
- **Reduced motion:** `.marquee__track{animation:none;overflow-x:auto}` — the strip becomes
  natively scrollable and the duplicate is hidden, so no content is lost.

## Accessibility
- Container: `<div class="marquee" role="marquee" aria-label="Latest five-star match
  ratings">`.
- The **duplicate/clone track is `aria-hidden="true"`** so screen readers read the list once.
- If items are links, they remain focusable; hover-pause is matched by focus (keyboard users
  can tab through without the strip scrolling out from under them — consider pausing on
  `:focus-within`).
- Ratings use a real `★` glyph plus the numeric value in text (not color-only).

## SEO/GEO notes
- Each item can be a real `<a href>` to the match page — lightweight internal links to
  high-value "five-star match" entities.
- Keep the primary (non-clone) set in server-rendered HTML.
