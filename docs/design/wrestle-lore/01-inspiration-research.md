# Wrestle Lore — Design & Product Inspiration Research

Scope: patterns to steal for a static, no-build, fully crawlable pro-wrestling database + review
network. Two lenses: (a) sports/entertainment DATABASE + review sites, (b) ADDICTIVE browsing and
discovery. Every pattern below is annotated for how it lands on a static site with no login, no
browser storage, and root-absolute HTML links.

Date: 2026-07-26. Author: design/product inspiration researcher.

---

## Part A — Database + review sites: how they tame huge catalogs

### A1. Cagematch (the direct competitor to beat)
- **Faceted entity model.** Every noun is its own browsable index with its own filters: Wrestlers,
  Matches, Events, Promotions, plus statistics views on each. A match is a first-class object with a
  rating, not just a row on a wrestler page. Wrestle Lore already has this shape (wrestlers/matches/
  events/rivalries/moments) — lean into it and make each index page a real landing page, not a list.
- **Rating as the spine.** A 0–10 user rating and a "workrate" star culture is the reason people
  visit. It drives leaderboards ("highest-rated matches of 2026"), comparison, and repeat visits.
  Buildable static version: pre-render leaderboards (Top matches, Top by promotion, Top by year) as
  static pages from the .md front-matter you already author. No live voting needed for v1; show
  editorial + cited community ratings and flag which is which.
- **Statistics views.** Cagematch exposes "Statistics" tabs (win/loss, most matches, rating
  distributions). A static site can pre-compute these at author time and ship them as HTML tables —
  they are catnip for deep sessions and for SEO long-tail ("[wrestler] win loss record").
- **Separation of layers.** Cagematch cleanly splits transactional data (match records/stats),
  social validation (ratings/reviews), and discussion (forums). Adopt the first two; skip forums.
- Source: 24-7.is Cagematch review; cagematch.net ratings + statistics pages.

### A2. Letterboxd (the aesthetic + review-network model)
- **The catalog IS the identity.** Poster-grid density with a single strong accent color; the poster
  does the visual work, chrome stays minimal. Maps perfectly onto Direction-B poster-wall tiles.
- **Every object has a canonical page + rich cross-links.** Film -> cast -> each person -> their
  films. This "rabbit hole" internal linking is the retention engine. For Wrestle Lore: match ->
  both wrestlers -> their rivalries -> the event -> the promotion -> that promotion's other events.
  Never dead-end a page; every page needs 6-12 outbound links to sibling entities.
- **Lists as content.** User/editorial lists ("Best of 2026", "Every Iron Man Match") are cheap to
  author, extremely shareable, and rank well. Ship curated static lists as a content type.
- **Stats/"Year in review" as a hook.** Letterboxd's yearly wrapped-style stat pages drive a
  seasonal traffic spike. Static analog: a "2026 in wrestling" recap hub, pre-rendered.
- **Four-star culture + micro-reviews.** Short, punchy reviews beat long essays for scannability.
- Sources: Letterboxd UX case studies (Medium); "Why Letterboxd is the only social media worth
  using" (Substack); Letterboxd statistics 2026.

### A3. Transfermarkt / Tapology / Sherdog (dense sports data, made scannable)
- **Badges and color are load-bearing, not decorative.** Nationality flags, position tags, status
  dots (active/retired/injured), value chips. A user parses a row in under a second because color +
  icon encode category before they read text. Wrestle Lore should encode: promotion (already have
  accent colors), status (CURRENT vs LEGEND), division (MALE/FEMALE/tag/etc), era, and
  championship-held via consistent badge shapes.
- **One color system, applied everywhere.** Transfermarkt reuses the same club/nation color tokens
  across tables, profiles, and headers so the whole site reads as one instrument. Wrestle Lore
  already has promotion accents (WWE #c8102e, WCW #e2b13c, ECW #b0b0b0, TNA #1e73be, NXT #f5c518) —
  ADD NJPW (propose a red/black: NJPW #d21c1c on ink, or #c60c30) and add non-promotion category
  colors for the new axes (e.g. LEGENDS = gold #d4af37, CURRENT = red #e11d2a, WOMEN'S division =
  a distinct hue not yet used, e.g. magenta/violet, so it reads instantly).
- **Comparison and "market value"-style single hero metric.** One headline number per profile
  (Transfermarkt = market value) anchors the page. For a wrestler: a single "Lore Score" or
  "Peak rating" hero stat (clearly labeled as editorial/derived, not fabricated).
- **Sortable, filterable index tables + faceted browse rails.** The huge catalog is navigable via
  filter pills (the user already wants MORE categories). Static version: pre-render one page per
  facet combination you care about (e.g. /wrestlers/women/, /wrestlers/legends/, /wrestlers/njpw/)
  AND provide client-side filter pills on the master index for the rest.

### A4. IMDb (breadth + trending)
- **"Most popular / trending this week" module** on the homepage creates a reason to return. Static
  analog: an editorially-updated "Trending" rail (hand-set weekly) — honest, no fake live counters.
- **Known-for / top-credits** surfacing on person pages = the 3-5 things that matter, above the full
  list. For a wrestler: signature matches + top rivalries above the full match history.

---

## Part B — Addictive browsing & discovery patterns

### B1. Horizontal rails / rows (the core discovery unit)
- Netflix's entire model is stacked, themed horizontal rails ("Because you watched", "Top 10",
  "Trending"). Each rail is a small, finishable promise that invites the next. For a static site the
  rails are hand-authored or generated per page: "More from WCW", "Same rivalry", "Same era",
  "5-star matches", "If you liked this match". No personalization engine required — relatedness is
  encoded in the .md front-matter (promotion, era, participants, tags) and rendered at build time.
- Keep rails horizontally scrollable on mobile, wrapped grid on desktop.
- Source: Fleekbiz "How Netflix's UX encourages binge-watching".

### B2. "Next" / rabbit-hole linking (the deepest lever)
- The single biggest driver of deep sessions is that every page ends by pointing at 3-6 obvious next
  clicks. Netflix autoplays next; Letterboxd links every entity. Static version: a mandatory
  "Keep going" block at the bottom of EVERY page with contextual next steps (next event in the
  series, the rematch, the other wrestler, the rivalry hub). This is the #1 pattern to adopt.

### B3. Top 10 / leaderboards / ranked lists
- Ranking triggers curiosity ("who's #1?") and completionism ("did I see all 10?"). Pre-render
  ranked static pages: Top 10 matches of 2026, Top 10 by promotion, Most-decorated, Hall of Fame
  classes. Ranked = shareable = link bait = SEO.

### B4. Trending / recency signals
- A visible "what's hot now" surface pulls repeat visits. Do it honestly: editorial "This week in
  Wrestle Lore" set by hand, plus "Recently added" (real, from build metadata). Avoid fake live
  view counts (anti-AI/anti-cliché standard).

### B5. Progress + collection psychology (no-login version)
- Netflix "Continue watching" and Letterboxd "films watched" reward completion. Without login/
  storage, reproduce the *feeling* via visible catalog scale ("89 profiles, 30 rated matches") and
  completeness cues on hubs ("You've reached the end of WCW events"). Curated "collections" the user
  can mentally check off (a rivalry's full match list, a wrestler's title reigns) give the same pull.

### B6. Hover / tap preview enrichment
- Netflix hover-preview reduces click cost and increases browsing velocity. Static analog: on
  poster-tile hover, reveal a compact overlay (rating, promotion, era, one signature fact) via CSS
  only — no JS, works crawlable. On mobile the fact sits under the tile.

### B7. Premium feel = restraint + motion discipline
- What reads "premium": one accent per context, generous negative space, big confident type
  (Anton/Oswald already do this), duotone imagery, and *subtle* motion (fade/rise on scroll, gentle
  hover lift). Avoid decorative arrows, avoid busy gradients competing with content. The scanline/
  duotone poster treatment you have is on-trend; keep it consistent so the whole wall reads as one
  system.

---

## Part C — Searchability: SEO + GEO (AI answer-engine citation)

- **Hub-and-spoke architecture.** Each category index is a hub that links to all spokes and every
  spoke links back to the hub and to siblings. This is both the rabbit-hole retention engine (B2)
  AND the internal-linking structure search engines and LLMs reward. Same work, two payoffs.
- **Structured data (schema.org) on every page.** Ship JSON-LD: `Person`/`ProfilePage` for
  wrestlers, `Event` for PPVs (with `startDate`, `location`, `performer`), `VideoObject` for
  moments, `BreadcrumbList` on every page, `ItemList` on leaderboards/hubs, `Review`/`AggregateRating`
  on rated matches, `Organization`/`SportsOrganization` for promotions. This is the highest-leverage
  GEO move: it makes facts machine-extractable and citable by AI answer engines.
- **Answer-first content blocks.** For GEO, lead each page with a tight, factual summary paragraph
  and a short FAQ (`FAQPage` schema) answering the literal questions people ask ("Where can I watch
  WWE PLEs?", "How many times is Ric Flair in the WWE Hall of Fame?"). AI engines lift these.
- **Descriptive, stable, human-readable URLs** (already done: /wrestlers/{slug}/). Keep them.
- **One canonical page per entity**, breadcrumb everywhere, and an XML sitemap + curated internal
  "related" links so crawlers reach deep pages in few hops.
- Sources: memorable.design internal-linking 2026; seotuners schema for AEO/GEO; digidop structured
  data 2026.

---

## Part D — Applying it to the new requirements

### D1. More colors / more separation / more categories (req 1,2,3)
- Add category color tokens beyond promotion accents: CURRENT (red), LEGEND (gold), WOMEN'S division
  (new distinct hue), plus era bands. Use badge SHAPE to distinguish axis (pill = status, chip =
  division, tag = era) so color + shape together never ambiguous.
- Wrestler separation: build faceted hub pages — /wrestlers/current/, /wrestlers/legends/,
  /wrestlers/women/, /wrestlers/men/, and per-promotion + per-era rails on the master index. Surface
  MANY more wrestlers via dense poster grids (Letterboxd density).
- Events: separate hubs by promotion, by year, by brand; a year timeline is a strong hub + SEO page.

### D2. Brand cards with streaming info (req 4) — VERIFIED FACTS (flag anything shifting)
Where each promotion streams as of mid-2026 (confirm at build; TV rights move fast):
- **WWE Raw:** Netflix, globally (all tiers). [verified — multiple sources]
- **WWE SmackDown (US):** USA Network (cable); replays on Peacock. [verified]
- **WWE NXT (US):** The CW. [verified]
- **WWE Premium Live Events:** US on **ESPN** (the ESPN DTC app / ESPN Unlimited) in 2026;
  **Netflix internationally**. NOTE: one source still lists US PLEs on Peacock — the ESPN move is the
  2026 arrangement and matches the project brief; VERIFY the exact US home before publishing.
- **AEW (Dynamite/Collision):** TBS/TNT cable; streaming on **HBO Max**. PPVs on HBO Max (~$40 for
  subscribers), plus Triller / PPV.com / YouTube (~$50). [verified]
- **NJPW (New Japan):** **NJPW World** subscription, ~$9.99/mo, with English commentary on Wrestle
  Kingdom, G1 Climax, etc. [verified] — this is the streaming home to show on the new NJPW card.
- **TNA:** US on AXS TV / AMC (cable) + **TNA+** subscription (~$9.99/mo); post-air clips on YouTube.
  [verified — note AXS vs AMC cable carrier varies by source; VERIFY]
- **ROH:** **HonorClub** (~$9.99/mo). [verified]
- **AAA:** now WWE-affiliated; airs on FOX (LatAm) + free on WWE/AAA YouTube. [verified — evolving]
- **CMLL:** CMLL YouTube (Spanish), Triller (~$10, English), Televisa (Mexico). [verified]
Design: each brand card = promotion accent header + monogram + "Where to watch" row of small
platform chips (Netflix / ESPN / HBO Max / NJPW World / TNA+ / The CW), a one-line positioning fact,
and links to that promotion's events + top wrestlers. Chips are text, not logos (avoids trademark
image issues); label US vs Intl explicitly.

### D3. NJPW + AJ Styles (req 5)
- Add NJPW as a 6th promotion with its own accent (propose #c60c30 red on near-black, distinct from
  WWE #c8102e — differentiate by pairing NJPW with a black field + white rule, WWE with its own).
  VERIFY: NJPW brand red before locking. Showcase AJ Styles prominently — he is a genuine NJPW-to-WWE
  crossover (former IWGP Heavyweight Champion, Bullet Club founder), so he links both promotion hubs.
  FLAG: confirm AJ Styles' current 2026 status/roster before publishing bio claims.

### D4. Hall of Fame (req 6)
- HOF hub = ranked/collection content (B3). Show last 5 induction classes as a horizontal timeline
  of class cards, each linking to inductee profiles; feature "most-decorated inductee" hero =
  **Ric Flair, two-time WWE Hall of Famer** (2008 solo, 2012 with the Four Horsemen). VERIFY exact
  years and the 5 most recent classes/inductees before publishing — do not fabricate class rosters.

### D5. Influencers / Media tab (req 7)
- Treat as "Wrestling Media & Creators": interviewers, podcasters, journalists, and personalities.
  Proposed roster to research/verify: **Chris Van Vliet** (interviewer, INSIGHT podcast) as the
  flagship; plus figures like Ariel Helwani, the Wrestling Observer / Dave Meltzer, Sam Roberts,
  Denise Salcedo, and creator-side personalities. On "Sami Zayn": he is an active WWE wrestler, not a
  media personality — recommend featuring him under wrestlers and only cross-listing in media if he
  has a notable media project; FLAG for user decision. Each media card links out only where a real,
  citable page exists; no fabricated quotes.

### D6. Rename to "Wrestle Lore" (req 8)
- Global rename in nav, titles, meta, JSON-LD `name`/`WebSite`, footer, and the ⌘K palette. Update
  Open Graph site_name. Keep the tone; "Lore" invites the deep-dive/rabbit-hole framing (lean into it
  with a "Lore" content type: origin stories, gimmick histories, kayfabe-vs-real notes).

---

## Part E — The shortlist (highest-leverage, ranked)

1. **"Keep going" next-links block on every page** (B2) — the single biggest retention lever, and it
   doubles as the internal-linking SEO/GEO backbone. Mandatory, 4-6 contextual links per page.
2. **Themed horizontal rails everywhere** (B1) — "More from WCW", "Same rivalry", "5-star matches",
   generated from front-matter. Turns every page into a discovery surface.
3. **Ranked leaderboards + collections as static pages** (B3/A1) — Top matches, HOF classes,
   most-decorated, best-of-year. Shareable, SEO-strong, completionist pull.
4. **Badge + color system carrying real meaning** (A3) — status/division/era/promotion encoded by
   color AND shape, applied site-wide, so a 12-year-old parses a tile in one second.
5. **JSON-LD on every entity + answer-first summary/FAQ blocks** (Part C) — makes facts citable by
   AI answer engines and wins long-tail search; same hub-spoke links serve retention and crawlers.
6. **Faceted hub pages for the new axes** (D1) — pre-rendered /current, /legends, /women, per-year,
   per-promotion (incl. new NJPW) hubs, each a dense poster wall that ends in a rail and a
   "keep going" block.

---

## Sources
- 24-7.is — In-Depth Review of Cagematch.net's Wrestling Database
- cagematch.net — Ratings System + Matches Statistics pages
- Letterboxd UX case studies (Medium, davisdesigninteractive / raquelcarmona); amywild.substack.com
- Fleekbiz — How Netflix's UI/UX Encourages Binge-Watching
- Levitation — Design Psychology 2025: The Science Behind Addictive UX
- memorable.design — Internal Linking Strategy 2026; seotuners.com — Schema for AEO/GEO;
  digidop.com — Structured data for SEO and GEO 2026
- WrestleIndex — Where to Watch Wrestling in 2026; scorpiondeathtalk.substack — How to Watch Pro
  Wrestling 2026; ESPN/Netflix/HBO Max/NJPW World streaming pages (streaming facts, verify at build)
