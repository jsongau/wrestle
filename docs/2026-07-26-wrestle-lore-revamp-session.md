# Session summary — 2026-07-26 · Wrestle Lore revamp

## What this session did
Rebranded MAT → **Wrestle Lore** and executed a multi-agent redesign + build. Site is now
**198 pages**, single design system, one canonical domain.

## Major decisions
- **7-tab mega-nav** (Wrestlers · Matches · Events · Promotions · Hall of Fame · Media · More + ⌘K),
  single-source, stamped site-wide via `build/apply_shell.py`. No loud Join CTA in the bar (conversion
  moved to in-content moments). Color encodes category, shape encodes axis (brief §0 D1–D5).
- **Domain unified** to `wrestlelore.com` (was split matdb.io / matwrestling). `MAT` → `Wrestle Lore`
  via word-boundary rename (safe vs "MATCH"/"format").
- **New content**: NJPW + AEW promotions, Hall of Fame (hub + 2026/2025 classes; AJ Styles headlines
  2026), /current//legends//women/ hubs, Media + Chris Van Vliet, AJ Styles showcase, 18 champion profiles.
- **Engagement layer** (`js/engage.js`): sticky left scroll-spy rail, "Keep going" bottom rail, Discover
  floater (Did-you-know + Stumble) — all read each page's own cross-links, no per-page data, no storage.

## Traps discovered (and fixed)
1. **98 wrestler profiles were unstyled** — `athlete-hero`/`content-grid`/`bio-col`/`stats-col`/`record-table`
   had zero CSS. Only the-undertaker (bespoke) looked right, which hid it. Fixed with one profile stylesheet.
2. **Fonts missing on 93 pages** — batch templates omitted the Google Fonts link → system-font fallback.
3. **Sticky left rail overlapped content** at 1366/1440px — I only tested wide. Now renders ≥1600px only.
4. **Fabricated data** — "12,840 waitlist" and `AggregateRating` (9,640 ratings) on 30 match pages.
   Removed; matches now carry an honest first-party editorial `Review`.
5. **Stale roster** — `/wrestlers/` listed 41 while 107 exist. Rebuilt from filesystem with A–Z filter.
6. **Count drift** — "41+ / 41 / 89 / 107" across pages; homepage stats now real (7 promotions / 107 wrestlers).
7. `MAT` inside `MATCH`/`format` — avoided by word-boundary rename.
8. **`</body>` in a CSS comment** broke the preview inliner (replace hit the wrong occurrence) — use `rfind`.

## Key files
- `build/apply_shell.py` — single-source nav/footer/palette stamper (run after any page batch).
- `build/build_roster.py` — regenerates `/wrestlers/` from the filesystem.
- `js/facets.js` — faceted filter bar; `js/engage.js` — engagement layer; `js/nav.js` — ⌘K palette.
- `docs/design/wrestle-lore/` — 30 design/vision/data docs + `10-MASTER-BRIEF.md` + `critique/POLISH-BACKLOG.md` (56 items).

## Exact next steps (from POLISH-BACKLOG.md, ranked)
1. **Self-host + subset fonts** — biggest LCP win (currently render-blocking Google Fonts).
2. **404 page** + surface it; confirm search-index includes the new hubs.
3. **Keep-going rails on non-profile pages** (events/matches) for the full internal-link loop.
4. **16 legacy content cross-links** to unbuilt wrestlers (barry-windham, big-boss-man, ultimate-warrior…) —
   build those profiles (data drafted in `docs/design/wrestle-lore/data/`).
5. **Titles lineage pages** `/titles/{belt}/` — closes the route the header historically advertised.
6. **Supabase waitlist backend** — the still-unbuilt funnel data layer (approved direction; needs project pick).

## Stack / conventions (for future sessions)
Static, no build step, crawlable (nav links in raw HTML). One `css/site.css`. Vanilla JS, no browser storage.
Broadcast Bold: Anton (display) / Oswald (UI) / Inter (body); gold #d4af37 + red #e11d2a + promotion accents.
Preview = self-contained `.html` with CSS/JS inlined (never PNG-as-preview). Commit ≠ deploy; confirm
GitHub repo + Vercel project + show remote before any push. No git remote configured yet.

---

## Phase 2 addendum — new content types (Titles / Factions / Tag Teams)

**Built:** 30 new pages via a 4-agent build wave (titles-core, titles-world, factions, tag-teams).
- **Titles**: hub + 11 lineages (`/titles/{belt}/`) — current holder + notable reigns using `champ-panel`/`champ-row`.
- **Factions**: hub + 8 stables (`/factions/{name}/`) — lede + member card grids with promotion-tagged monograms.
- **Tag Teams**: hub + 8 teams (`/tag-teams/{name}/`) — same pattern, FAQPage on each.

**Architecture decisions:**
- **Reused-only CSS.** Agents were constrained to existing components (`ev-hero`, `champ-panel`, `grid-cards`,
  `faq-block`, `related-links`). Zero new CSS — this is why the 30 pages inherited the styled look for free and
  avoided repeating the "98 unstyled profiles" trap.
- **Placeholder shell pattern.** New pages ship with empty `<header class="site-header"></header>` /
  `<footer class="site-footer"></footer>`; `build/apply_shell.py` stamps the real nav/palette/footer. This keeps
  the nav single-source: the build agents never hand-copy nav markup that could drift.
- **Nav wiring.** Added a "Titles & Teams" column to the "More" mega-panel (`apply_shell.py` NAV constant),
  widened to `mega--wide`. One edit, stamped to all 225 pages.
- **Zero-404 discipline.** Cross-links only to existing pages; unbuilt names render as plain text, hub tiles for
  unbuilt lineages are non-links with name-only ItemList entries. Link check: 0 new broken links (16 pre-existing
  legacy gaps remain, all from `/wrestlers/` pages — POLISH-BACKLOG #4).

**Consolidation ran:** `apply_shell.py` (225 pages) → sitemap 198→225 URLs → search-index 177→207 entries →
link check → 1366px render-verify (titles hub, lineage, faction, tag-team all clean) → commit `746a694`.

**Next backend task (offered):** the still-unbuilt **waitlist/membership data layer** (Supabase) — the one piece
that turns this from a browsable archive into a growth funnel with captured leads. Everything else is content depth.
