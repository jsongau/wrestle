# MAT — Mega-Nav + Style Concepts (3 prototypes)

Research basis: `data/research-meganav.md` (NN/g, Baymard, W3C ARIA APG, Adrian Roselli) +
`data/research-cool-styles.md` (Awwwards/Godly trends). Three distinct, clickable previews
were built so Jay can choose a direction. All share: black + gold `#d4af37` + red `#e11d2a`,
Anton/Oswald/Inter, no framework, no browser storage, reduced-motion + keyboard aware.

Each concept pairs a **mega-nav archetype** with a **visual style package**.

---

## Concept 1 — "MAIN EVENT" · Cinematic Broadcast + full-width columned mega
- **Archetype:** full-width columned mega panel with featured duotone cards (highest-ROI, closest to current markup).
- **Style:** dark cinematic — lit-arena mesh, film grain, poster-scale Anton type, frosted-glass panel.
- **Mega content (Wrestlers):** column 1 *By Promotion* (WWE/WCW/ECW/TNA/NXT with accent dots), column 2 *Featured* legends as mini duotone cards, column 3 *Top Matches*, column 4 a gold promo card ("Join MAT Insider").
- **Feel:** theatrical, premium, safe. The natural evolution of the current homepage.
- **Best if:** you want maximum "wow" with the least risk and a fast path to shipping.

## Concept 2 — "PRODUCTION TRUCK" · Broadcast HUD + bento command-board mega
- **Archetype:** bento mega panel (mixed-span tiles) + a live results ticker.
- **Style:** sports-broadcast HUD — corner-bracket frames, monospace telemetry labels, "LIVE" tag, stat readouts, brutalist accents.
- **Mega content:** a big featured-match tile, a promotion switcher grid, a "trending" tile, a stat block — like a broadcast control board.
- **Feel:** the most *ownable* and "database-authoritative" — looks like a broadcast graphics package.
- **Best if:** you want MAT to feel like a data/broadcast product nobody else looks like.

## Concept 3 — "GOLD STANDARD" · Editorial Command Board + ⌘K search-first nav
- **Archetype:** command-palette overlay (⌘K), search-first — also closes MAT's missing global-search gap.
- **Style:** modern editorial — soft mesh + grain, calmer oversized headline, spotlight-reactive bento.
- **Nav:** a prominent search pill ("Search wrestlers, matches… ⌘K") that opens a categorized results palette; lighter top bar.
- **Feel:** the most balanced, accessible, conversion-friendly, and "modern-tech" (Linear/Vercel energy).
- **Best if:** you want power-user speed + search + a refined, grown-up look.

---

### How to read the previews
Open each `MAT-meganav-*.html` on double-click. Each shows the header with its mega-nav **open**
so you can see the design immediately; hover/click the nav items (or press ⌘K / click search in Concept 3)
to interact. Pick one (or mix — e.g. Concept 1 look with Concept 3's ⌘K search) and I'll build it out for real across the site.
