# Mega Nav Research & Direction — MAT (2026-07-26)

Research behind the graphic-heavy mega-nav redesign. Goal: make the nav a
signature surface that shows clear separation between content types
(Wrestlers, Matches, Events, Moments), reads as premium, and stays fast and
crawlable. `Join MAT Insider` and `中文` removed from the bar per direction.

## What the best mega navs do (sourced)

From Nielsen-Norman-adjacent UX guidance and 2025/2026 example roundups:

- **Visual grouping is the job.** Icons, thumbnails, and subtle background
  shifts divide sections so the eye parses categories instantly. Every visual
  must have navigational purpose, never decoration for its own sake.
- **Multi-column with microcopy.** Columns grouped by a logical hierarchy
  (here: by content type, then by promotion/brand/recency), each link carrying
  a one-line description for ambiguous labels.
- **Featured content earns the space.** The strongest menus surface a hero
  tile or editors' pick rather than treating the panel like a sitemap.
- **Color-coding by type** (ASOS, Wizz Air) speeds recognition. MAT already has
  promotion accents (WWE red, WCW gold, ECW steel, TNA blue, NXT yellow) plus
  gold for the brand and red for "hot" — we lean on those.
- **Restraint still reads premium** (Adidas, IBM prove text-only can win).
  Graphic-heavy works only with strong typographic hierarchy and calm spacing.
- **Interaction:** wide hover zones, a short close-delay so the menu does not
  snap shut on a stray cursor, subtle fade/slide (no performance-killing
  animation), and full keyboard + screen-reader support.

Sources: Design Shack "Mega Menus Revisited: UX Best Practices in 2025";
Creative Corner "13 Must-See Mega Menu Examples"; NN/g mega-menu guidance;
LogRocket mega-menu design examples.

## Constraints specific to MAT

- **No real images yet.** All "graphics" are built from CSS: duotone gradient
  poster tiles, monogram marks, promotion color chips, and inline SVG icons.
  This keeps previews self-contained and the live site fast (no image
  requests, no layout shift).
- **Crawlable.** Nav links stay in the raw HTML, not JS-rendered, so the
  internal-link graph stays visible to search and AI crawlers.
- **Fixed instrument.** Five primary tabs (Wrestlers, Matches, Events,
  Moments, More) plus a Search (⌘K) entry. New content routes into a dropdown,
  never widens the bar.

## Three directions delivered

1. **A — Broadcast Control Room.** ESPN/UFC broadcast-graphics language:
   corner brackets, mono telemetry labels, compact poster chips, gold/red
   accents. Dense, authoritative, "live data" feel.
2. **B — Editorial Poster Wall.** Streaming-service / magazine language: large
   duotone poster tiles with monograms, big Anton headlines, generous
   whitespace, gold hairlines. Cinematic and premium.
3. **C — Arena Spotlight.** Cinematic dark with radial glow: a list on the
   left and a large featured hero card on the right of each panel, promotion-
   colored glows. The most "AAA product" feel.

## Trade-off flagged

Removing `Join MAT Insider` from the bar removes the always-visible conversion
path, and MAT is a membership funnel. Recommendation: keep the loud CTA out of
the bar as requested, but re-home a lightweight join entry point (a hero CTA
and/or a slim right-aligned text link) so the funnel is not lost. Not added to
these previews; available on request.
