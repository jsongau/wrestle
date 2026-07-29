# 2026-07-29 — Sparkle engine recovery, mobile h-scroll fix, Lore Feed page + nav row

## What changed and why
- css/site.css: recovered 20 lines of wglyph "sparkle engine" CSS verbatim from commit 32c951f
  (base .wglyph, wg-rot/wg-tw/wg-radar/wg-breathe/wg-gleam keyframes, --lore gem, --live radar,
  hover glows). The footer-redesign commit d653a5b had committed a stale stylesheet and swept
  this block, so the Lore Feed gem rendered as an unstyled dot and no sparkle spun anywhere.
- Mobile horizontal scroll (was 27px @360 / 65px @320 on every page): root cause was the footer
  brand block — .ftr-brand__tag white-space:nowrap and a non-shrinking 2.4rem brand word. Fixed
  in place (tag wraps, word uses clamp(1.55rem,7.4vw,2.4rem), brand min-width:0, logo 60px under
  480px) plus html{overflow-x:clip} as a site-wide guard. Verified 0px overflow at 320/360/390 on
  home, lore-feed, membership, profile, title, event — measured with the guard lifted, so the
  layout truly fits.
- /ring-feed/ renamed to /lore-feed/ (slug now matches the brand; the old slug was never live so
  no redirect needed). Homepage "view all" link and page canonical updated. Page is the existing
  homepage feed module (markup + its inline CSS) on the standard shell.
- components/meganav.html: Lore Feed featured as a full-width live row at the top of the Media
  dropdown — gem glyph, "Live · The Wire", red CTA "Open the feed" — matching the Events
  dropdown's Live Events banner pattern. .mfeed row needs grid-column:1/-1 because the studio
  panel is a CSS grid (first attempt landed in one cell and overflowed).

## Traps for future sessions
- NEVER trust grep presence checks for CSS blocks: hover rules referencing .wg-spin made the base
  animation look present when the keyframes were gone. Compare against the source commit line set.
- Concurrent sessions still collide on css/site.css. Recover swept blocks verbatim from git,
  append-only; a parallel Undertaker session was active during this work (its untracked pages and
  CHANGELOG lines ride along harmlessly).
- The Lore Feed items are hardcoded in index.html AND lore-feed/index.html with frozen "1d ago"
  labels. Two copies until the feed gets a data layer. Decision pending: hand-curated vs
  auto-recent (data/feed.json + shared renderer).

## Next steps
- Surprise Me trivia restore from approved v3_2 (drop harvestFacts, curated facts back).
- data/events.json single source for the ticket floater + Events banner + tickets page.
- Feed data layer if the user opts into auto-recency.
