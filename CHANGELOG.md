## 2026-07-26 (Polish + performance sprint)
- H7 Self-hosted fonts: added 7 Latin-subset woff2 (Anton 400, Oswald/Inter 400/600/700, 140KB total) under /fonts/; @font-face + metric-matched fallback faces (size-adjust/ascent-override computed from the real fonts vs Arial) to zero swap CLS. apply_shell.py now strips all Google Fonts preconnect+stylesheet links site-wide and preloads only Anton (the display/LCP font). Verified: 0 third-party font requests, all 7 served locally, Anton/Inter/Oswald all load.
- Q3 Shipped /404.html: full shell + ⌘K search + 8 popular-route tiles; noindex,follow. Stamped by apply_shell (targets() now includes standalone 404.html).
- A11y batch: solid loss badge deepened #e05263->#c23a4a (white contrast 3.8->5.25, AA); 16px form controls <=640px (stops iOS auto-zoom); >=44px touch targets on coarse pointers; forced-colors block so gradient-clipped headlines don't vanish in Windows high-contrast. (focus-visible ring + dim-text lift already present from prior pass.)
- Verified: CSS parses (699 rules), 404 + title/faction/tag-team render at 1366px, no horizontal overflow at 375px, link check unchanged (16 pre-existing legacy-wrestler gaps, zero new).

## 2026-07-26 (Phase 2 — new content types: Titles, Factions, Tag Teams)
- Built 30 new pages via a 4-agent build wave: Titles hub + 11 championship lineages (WWE/World/IC/US/Women's/Tag + WCW/ECW/IWGP/AEW/TNA), Factions hub + 8 stables (nWo, DX, Four Horsemen, Shield, Bloodline, Judgment Day, Bullet Club, Evolution), Tag Teams hub + 8 teams (Hardys, Dudleyz, E&C, New Day, Usos, Hart Foundation, Young Bucks, LOD).
- All reuse existing CSS components (ev-hero/champ-panel/champ-row/grid-cards/faq-block/related-links); zero invented CSS. Every page: title ≤60 ending " | Wrestle Lore", meta 140-160, valid double-quoted JSON-LD (BreadcrumbList everywhere, ItemList on hubs, FAQPage on detail pages), correct canonical, no em-dashes. Cross-links only to existing pages (zero new 404s).
- Wired the three hubs into the mega-nav "More" dropdown (new "Titles & Teams" column); re-stamped shell across 225 pages (fonts/nav/palette/footer). Regenerated sitemap.xml (198 -> 225 URLs) and js/search-index.js (177 -> 207 entries). Render-verified titles/factions/tag-team pages at 1366px.
- Data honesty preserved: reign/champion facts flagged VERIFY (Ripley interim title, IWGP 2026 reactivation, Bloodline/Judgment Day current status) phrased "as reported," not asserted.

## 2026-07-26 (Wrestle Lore revamp — multi-agent)
- Renamed MAT -> Wrestle Lore across the site; unified canonical domain to matwrestling.com; sitemap 119 -> 198 URLs.
- Ran 30-agent design orchestration (3 workflows): 13 design/brief/tech-lead docs + 7 vision + 10 data docs in docs/design/wrestle-lore/. Master brief resolves 5 cross-spec conflicts; content manifest maps ~211 new pages.
- Phase 0: single-source 7-tab shell (build/apply_shell.py) stamped across ~195 pages; killed 3 forked navs + dead /titles//search/ links.
- Phase 1 (9-agent build): NJPW + AEW, Hall of Fame (AJ Styles headlines 2026 class), current/legends/women hubs, Media + Chris Van Vliet, AJ Styles showcase, 18 champion profiles. Full 7-tab nav lit up.
- Critique wave (8 agents) -> 56-item POLISH-BACKLOG.md. Verified + fixed its P0: 98 wrestler profiles were unstyled (athlete-hero/content-grid/etc. had no CSS) -> added full profile stylesheet.
- UX: faceted filter bar (js/facets.js) on hubs; promotion-tinted cards; engagement layer (js/engage.js) = sticky left scroll-spy rail + "Keep going" bottom rail + Discover floater (Did-you-know facts, Stumble), all reading each page's own links.
- Fixes: rail overlap at 1366/1440 (now >=1600 only); fonts missing on 93 pages (injected); Stone Cold restored to nav Featured; homepage reveal failsafe + real stats (7 promotions / 107 wrestlers); removed fabricated "12,840 waitlist" + AggregateRating counts on 30 match pages (-> honest first-party rating); rebuilt /wrestlers/ roster 41 -> 107 with A-Z filter.

# Changelog — MAT (Pro Wrestling Database)

## 2026-07-26
- Wrestler batches 8–10: upgraded 14 pages to gold-standard 5-feature template (fixed a `wl-strip-wrap` regression across 5 build scripts), then added 20 new profiles (Attitude/Golden Era legends + Kane/Owen Hart/British Bulldog/Edge/Razor Ramon upgrades). 89 wrestler profiles total, all gold-standard.
- Launched **Events** content type: 5 PPV edition pages with real sourced 2026 results (Royal Rumble, Elimination Chamber, WrestleMania 42, Backlash, Night of Champions) + 5 brand hub pages + `/events/` index. Corrected an initial assumption mid-plan — WWE Premium Live Events stream on **ESPN** in the US from 2026 (new deal), not Netflix; Netflix carries the international live feed + US archive. Every event page's watch panel links both correctly. Added `Premium Live Events` column to the homepage's existing Matches mega-nav dropdown (no new top-level tab, per the site's nav rule). New CSS components: `event-hero`, `watch-panel`, `match-card-list`, `event-card`.
- Flagged, not yet resolved: the site has two canonical domains in use — `matwrestling.com` (README + homepage/promotions/matches templates + sitemap.xml, 791 refs) vs `matdb.io` (all 89 wrestler pages, 400 refs). New Events pages use `matwrestling.com` to match the sitemap and majority of flagship templates. Needs a single reconciliation pass across the wrestler pages.

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
