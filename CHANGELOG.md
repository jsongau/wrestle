# Changelog — MAT (Pro Wrestling Database)

## 2026-07-25
- Project kickoff. Wrote master brief (`PROJECT.md`): vision, IA/sitemap, SEO+GEO strategy, China market plan, membership funnel, tech stack.
- Ran 4 parallel research agents → datasets in `/data/` (41 wrestlers + 160+ relationship edges, 30 rated matches, 15 storylines, full design/SEO/GEO/China reference).
- Built single-file design system (`css/site.css`) — dark "arena" theme, mobile-first, all components (cards, rating meters, tale-of-the-tape, mega-nav, embeds/facade, tiers, forms).
- Built `js/main.js` — mobile nav, mega-panel toggles, facade video loader (YouTube+Bilibili), roster search/filter, waitlist form (in-memory, no browser storage).
- Built front page (`index.html`) with full mega-nav, hero featured match, five-star club, icons, relationship teaser, waitlist capture, GEO answer + FAQ.
- Built flagship templates: match page (Undertaker vs HBK WM25), wrestler page (The Undertaker), membership funnel (`membership/`).
- Dispatched builder-agent fleet for the remaining wrestler/match/rivalry/relationship/promotion/China pages, indexes, markdown mirrors, and SEO infra.
- Fleet delivered: 41 wrestler profiles, 30 match pages, 15 rivalries + index, wrestlers/matches/rankings/relationships indexes, 5 promotion hubs + index, about + methodology + growth-strategy, /zh/ + /zh/membership/ + /china/, robots.txt + sitemap.xml (103 URLs) + llms.txt, and /content/ markdown mirror.
- Verified: 104 HTML pages, 0 broken internal links, 0 invalid JSON-LD; rendered desktop + mobile + China screenshots as proof.
- Total: 173 files. Site is deploy-ready (pending real domain, verified video IDs, images, and a live waitlist backend).

## 2026-07-25 (v2 — Broadcast Bold homepage redesign)
- Ran 4 parallel design-research agents (visual, motion, typography, conversion) → playbooks in /data/design-research-*.md.
- Chose art direction: **Broadcast Bold** (ESPN/UFC/DAZN). Type system: Anton (display) + Oswald (condensed UI) + Inter (body).
- Wrote 12 per-section design specs in /docs/design/ (design-system + one per homepage section).
- Upgraded css/site.css (additive, non-breaking): layered "arena spotlight" hero, film-grain overlay, duotone poster tiles + monograms, gradient-border cards, pointer spotlight, metallic-gold shine buttons, marquee ticker, glass stat bar, angled seams, scroll-reveal (gated behind .js so content is visible without JS).
- Added js/enhance.js: scroll-reveal, count-up, hero parallax, card spotlight, sticky header — all reduced-motion + no-JS safe.
- Rebuilt index.html in Broadcast Bold; verified desktop + mobile renders (Google Fonts loaded). Delivered self-contained preview MAT-preview-home-v2.html.

## 2026-07-25 (design + content expansion)
- Design research (4 agents) + 12 per-section design specs (docs/design/) + 3 mega-nav concept previews; chosen direction: CONTROL ROOM (broadcast HUD + ⌘K command palette), spec in docs/design/mega-nav-combined.md.
- UX research (4 agents): nav/IA/search, mobile+a11y, conversion/membership, entity-page UX (data/ux-research-*.md).
- CONTENT EXPANSION (5 agents) in data/expansion-*.md — dedZuped vs existing, cited, 2024–2026-current:
  - +45 wrestlers (total ~86), +35 matches (total ~65), +21 rivalries & +17 factions, +26 events/PPVs & +15 title lineages, +67 glossary terms & +12 family dynasties.
- NOT yet built into pages — this is the source dataset for the next page-generation wave.

## 2026-07-25 (IGBBMN cross-pollination — Undertaker page finished)
- Reviewed the connected IGBBMN MMA project (Next.js). Adapted its best components to MAT's static stack: filterable fight-record table, win/loss result chips, method-breakdown bars, on-page sub-nav, championships panel, career timeline, pull-facts. **Dropped the betting/market module** per request.
- Added the "record system" to css/site.css (additive) + a record-filter to js/enhance.js (accessible, no storage).
- Compiled The Undertaker's verified curated match ledger (data/undertaker-record.md): 28 landmark matches, WrestleMania 25–2, Streak 21–0, 7 world titles, finish breakdown (18 Tombstones). Corrected two online sourcing errors (No Way Out 2006 was a LOSS; 3rd WHC came from CM Punk at HITC 2009).
- Rebuilt wrestlers/the-undertaker/ into the finished, gold-standard profile: record summary, filterable ledger (desktop table + mobile cards), finish bars, championships, timeline, signature matches, rivalries, relationships, FAQ. Now uses Broadcast Bold fonts. Filter verified (Losses → 5).

## 2026-07-25 (UX pass on Undertaker page — 3 UX-designer review agents)
- Ran 3 UX review panels (usability/a11y, visual, engagement/conversion) on the Undertaker page; implemented the high-impact set.
- Fixes: all 28 bouts now reachable on mobile (was 10); sr-only Win/Loss labels; [id]{scroll-margin-top} + sticky thead offset; --c-text-dim lifted for AA contrast; filter chips show per-filter counts; "Streak-ends" tag variant.
- Visual: duotone-monogram hero portrait (was flat initials); metal-gradient summary numbers; zebra + colored result rail on the table; finish bars animate on reveal; win/loss sparkline of the 28-bout arc; is-gold stat wash; "The Streak" sub-nav anchor.
- Engagement (static, no betting): "Rate the Deadman" 5-star widget (join-to-save), share-the-Streak button (Web Share API), Follow, and a "Guess the Legend" teaser → funnel; all fire console intent events for analytics.
- Workflow: delivering self-contained .html previews (not PNGs) going forward.

## 2026-07-25 (Undertaker deep build — tabs, alter egos, media)
- Added a tabbed record to the Undertaker page: **Landmark ledger (28) / WrestleMania (25–2, all 27) / PPV·PLE (curated ~30)**, each in its own scrollable area (inner scroll). Complete WM record + curated PPV record + Royal Rumble stats compiled & verified (data/undertaker-records-expanded.md).
- Created alter-ego profile pages (SEO-optimized, cross-linked, schema): **/wrestlers/mean-mark-callous/** (WCW 1989–90) and **/wrestlers/the-american-badass/** (biker era 2000–03). Added a "Personas" section + Person alternateName/sameAs linking them (data/undertaker-personas-media.md).
- Added **Documentaries & Shows** and **Podcasts** sections with sticky-label rails + TVSeries/PodcastSeries schema (The Last Ride, Biography A&E, Broken Skull Sessions, Escape the Undertaker, Six Feet Under, etc.).
- Tab + scroll UI added to css/site.css; tab keyboard/ARIA logic in js/enhance.js. Verified: 0 broken links, tabs switch, WM=27 rows, PPV=30 rows.
