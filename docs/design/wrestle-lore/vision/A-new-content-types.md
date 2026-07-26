# Wrestle Lore — Vision Spec A: New Content Types

Content-type architect deliverable. This proposes the highest-value NEW page types beyond the four
that already exist (wrestler, match, event, moment). Each entry gives a concrete route, why it ranks
or engages or earns, how it builds on a static no-build crawlable site, and how it wires into pages
that already exist.

- Date: 2026-07-26
- Grounding read: `00-content-data-research.md`, `01-inspiration-research.md`
- Existing routes to cross-link: `/wrestlers/` (89), `/matches/` (30 rated), `/events/` (5 PLE
  editions + 5 brand hubs), `/rivalries/` (15), `/promotions/` (wwe, wcw, ecw, tna, nxt),
  `/moments/` (4). The site header ALREADY links `/titles/` — that route is expected and unbuilt.
- Standing constraints honored: static HTML, no build step at request time, one `css/site.css`,
  vanilla JS, no browser storage, root-absolute links, every page pre-rendered at author time.
- Fact rule: no invented reigns, dates, or gates. Every data-heavy tier below carries a `VERIFY`
  flag on the specific facts that must be confirmed against a cited source before publishing.

---

## How these are ranked

Score = search demand x buildability on the current static stack. "Buildability" rewards page
types that render from the same front-matter you already author for wrestlers, matches, and events,
and penalizes anything that needs a server, a database, or live data. The full ranked table is at
the end. The detailed specs run in ranked order.

---

## Tier 1 — Build these first (high demand, pure static)

### 1. Championship Title Lineage pages
- **Route:** `/titles/` (hub) and `/titles/{belt}/` per lineage.
  Examples: `/titles/wwe-championship/`, `/titles/world-heavyweight-championship/`,
  `/titles/universal-championship/`, `/titles/wwe-womens-championship/`,
  `/titles/intercontinental-championship/`, `/titles/wcw-world-heavyweight-championship/`,
  `/titles/ecw-world-championship/`, `/titles/tna-world-championship/`,
  `/titles/nxt-championship/`, `/titles/iwgp-world-heavyweight-championship/`.
- **Why it wins:** "wwe championship history" and "intercontinental champions list" are evergreen,
  high-volume queries with weak, ad-heavy incumbents. A clean chronological reign table is the exact
  shape an AI answer engine lifts, so it wins both classic search and citation. The header already
  promises `/titles/`, so this closes a live gap rather than inventing scope.
- **Buildability:** Pure static. Each lineage is a table of reigns (champion, won-from, date, event,
  reign length, notes). Ship `ItemList` plus `BreadcrumbList` JSON-LD. `VERIFY`: every reign date and
  length against a cited lineage source before publishing; do not estimate reign lengths.
- **Cross-links:** Each reign row links to `/wrestlers/{slug}/`; each title-change row links to the
  `/events/{slug}/` where it happened and the `/matches/{slug}/` if that match is rated; the belt's
  home promotion links to `/promotions/{slug}/`. Wrestler pages gain a "Title reigns" block that
  links back up to the lineage. This single type creates dozens of new internal links across the
  existing 89 profiles.

### 2. Era and Timeline pages
- **Route:** `/eras/` (hub) and `/eras/{slug}/`.
  Examples: `/eras/golden-era/`, `/eras/new-generation/`, `/eras/attitude-era/`,
  `/eras/ruthless-aggression/`, `/eras/pg-era/`, `/eras/modern-era/`, plus the year timeline
  `/timeline/{year}/` (e.g. `/timeline/2001/`, `/timeline/2026/`).
- **Why it wins:** "attitude era" alone is a standing high-volume term with strong browse intent, and
  the era frame is how casual fans actually organize wrestling in their heads. The taxonomy research
  already defines six eras, so this page type turns an internal tag into a destination. Year-timeline
  pages capture "[year] in wrestling" recap traffic and give a seasonal spike hook.
- **Buildability:** Pure static. An era page is a curated hub: defining wrestlers, defining matches,
  defining rivalries, the promotions that mattered, and a one-screen "what changed" summary. Renders
  from the era tag already proposed in the taxonomy. `VERIFY`: era boundary years before printing
  them as hard dates.
- **Cross-links:** Feeds from and back to `/wrestlers/` (era tag), `/matches/`, `/rivalries/`, and
  `/promotions/`. Every wrestler and match page gains an era badge that links to its era hub. This is
  the browse spine that makes the poster wall feel navigable by feel, not just by name.

### 3. Faction and Stable database
- **Route:** `/factions/` (hub) and `/factions/{slug}/`.
  Examples: `/factions/the-bloodline/`, `/factions/nwo/`, `/factions/four-horsemen/`,
  `/factions/d-generation-x/`, `/factions/the-shield/`, `/factions/bullet-club/`,
  `/factions/evolution/`, `/factions/the-nexus/`, `/factions/the-hart-foundation/`.
- **Why it wins:** Faction searches ("nwo members", "the shield members", "bloodline explained")
  carry both curiosity and completionist intent, which is the deep-session driver from the inspiration
  research. Forty existing wrestler pages already mention factions, so the demand and the source
  material are both present. The Bloodline and Bullet Club also tie the new NJPW promotion into the
  existing roster.
- **Buildability:** Pure static. A faction page lists members with join and exit notes, the group's
  signature matches and rivalries, and a short origin. Ship `Organization` plus `ItemList` JSON-LD.
  `VERIFY`: exact membership rosters and dates for each faction.
- **Cross-links:** Members link to `/wrestlers/{slug}/`; the group's feuds link to `/rivalries/`
  (nWo Invasion, Shield Rise and Betrayal, the Bloodline already exist as rivalries); signature bouts
  link to `/matches/`. Each member's wrestler page gains a "Factions" block linking back. This type
  converts the existing rivalry pages from one-off feuds into a connected group history.

### 4. Move and Finisher index
- **Route:** `/moves/` (hub) and `/moves/{slug}/`.
  Examples: `/moves/rko/`, `/moves/tombstone-piledriver/`, `/moves/stone-cold-stunner/`,
  `/moves/sweet-chin-music/`, `/moves/619/`, `/moves/styles-clash/`, `/moves/spear/`,
  `/moves/pedigree/`, `/moves/f5/`, `/moves/sharpshooter/`.
- **Why it wins:** This is the boldest cheap win. "what is an rko", "how to do a suplex",
  "list of wrestling moves" are enormous, always-on queries that no wrestling database owns cleanly,
  and they are exactly the definitional questions AI answer engines cite. A move page is a factual
  primitive: the base specs would not surface it, yet it is the most extractable content on the site.
- **Buildability:** Pure static and trivially so. Each page is a definition, the mechanics in plain
  language, who innovated it, its notable users, and the matches where it decided a bout. Ship
  `DefinedTerm` plus `FAQPage` JSON-LD to maximize citation. No media hosting required; link out to
  clips. `VERIFY`: innovator attributions, which are frequently disputed, so cite and hedge.
- **Cross-links:** "Notable users" link to `/wrestlers/{slug}/`; "decided this match" links to
  `/matches/{slug}/`. Every wrestler page's existing finisher line becomes a link into `/moves/`.
  This one type creates a dense new link layer from a field already present on all 89 profiles.

### 5. Head-to-head Versus pages
- **Route:** `/versus/{a}-vs-{b}/` with a stable alphabetical slug order.
  Examples: `/versus/john-cena-vs-randy-orton/`, `/versus/the-rock-vs-stone-cold-steve-austin/`,
  `/versus/undertaker-vs-triple-h/`, `/versus/hulk-hogan-vs-ric-flair/`.
- **Why it wins:** This is programmatic SEO at scale. "cena vs orton record", "who won more X or Y",
  and "[wrestler] vs [wrestler] history" are a bottomless long-tail, and the head-to-head record is
  the single most citable answer format an AI engine can quote. Curate the pairs that already share a
  rivalry or multiple rated matches, so every page is grounded in real data rather than generated
  filler.
- **Buildability:** Pure static, generated from the match front-matter you already author. Seed with
  the pairs that appear in `/rivalries/` and in the 30 rated matches, then widen. Ship a compact
  record table plus `FAQPage` JSON-LD ("Who has the better record?"). Guardrail: only publish a pair
  when at least two documented meetings exist, so no page is thin. `VERIFY`: win-loss tallies against
  match records; label editorial verdicts as opinion.
- **Cross-links:** Both combatants link to `/wrestlers/`; each listed meeting links to `/matches/`
  and `/events/`; the pair's feud links to `/rivalries/`. Wrestler pages gain a "Rivalries and
  head-to-heads" rail feeding these pages. This is the highest-ceiling type for raw search volume.

### 6. This Day in Wrestling
- **Route:** `/this-day/` (today redirect target) and `/this-day/{mm-dd}/` for all 366 dates.
  Examples: `/this-day/03-30/` (a WrestleMania date), `/this-day/01-24/`.
- **Why it wins:** This is the return-habit engine. A dated daily page gives fans a reason to come
  back every morning, and 366 evergreen pages each rank for "on this day wrestling [date]" plus every
  anniversary that falls on it. It manufactures recurring traffic from content you already hold: debut
  dates, title changes, and famous matches.
- **Buildability:** Static with one honest caveat. Pre-render all 366 pages from dated facts in your
  front-matter. Today's date can be resolved two ways without a backend: a tiny vanilla-JS redirect
  from `/this-day/` to the correct `{mm-dd}` page, while every `{mm-dd}` page is a real crawlable URL
  that stands alone. No storage, no server. `VERIFY`: every anniversary fact carries a cited date.
- **Cross-links:** Each entry links to the `/wrestlers/`, `/matches/`, `/events/`, or `/moments/`
  page it references. The homepage can surface today's card as an editorial "Trending" analog that is
  genuinely fresh without any live counter.

---

## Tier 2 — High value, still static, slightly more data work

### 7. Tag-Team database
- **Route:** `/tag-teams/` and `/tag-teams/{slug}/`.
  Examples: `/tag-teams/the-hardy-boyz/`, `/tag-teams/the-dudley-boyz/`, `/tag-teams/harlem-heat/`,
  `/tag-teams/the-steiner-brothers/`, `/tag-teams/diy/`, `/tag-teams/the-usos/`,
  `/tag-teams/the-new-day/`.
- **Why it wins:** Tag division history is under-served by the big incumbents and carries steady
  search ("tag team champions list", "best tag teams ever"). It also gives the existing TLC and tag
  war rivalry pages a proper home. The tag title lineage from type 1 slots directly into these pages.
- **Buildability:** Pure static. Members, title reigns, signature matches, and a short run history.
  Ship `SportsTeam` or `Organization` plus `ItemList` JSON-LD. `VERIFY`: reign dates and membership.
- **Cross-links:** Members link to `/wrestlers/`; reigns link to the tag `/titles/` lineage;
  signature bouts link to `/matches/` (TLC 2 at WrestleMania X-Seven already exists) and the
  `tlc-tag-wars` rivalry.

### 8. Family Dynasty trees
- **Route:** `/dynasties/` and `/dynasties/{slug}/`.
  Examples: `/dynasties/the-hart-family/`, `/dynasties/the-anoai-family/`,
  `/dynasties/the-flair-family/`, `/dynasties/the-rhodes-family/`,
  `/dynasties/the-guerrero-family/`.
- **Why it wins:** "anoai family tree" and "wrestling families" are strong curiosity queries with
  high dwell time, and a family tree is inherently shareable. The existing roster is dense with these
  bloodlines (Bret and Owen Hart, Roman Reigns and Rey Mysterio's extended ties, Ric and Charlotte
  Flair, Dusty and Cody Rhodes, Eddie and Chavo Guerrero), so the material is already on the site.
- **Buildability:** Static. Render the tree as a semantic nested list styled with CSS, not an image,
  so it stays crawlable and accessible. `VERIFY`: exact relations, which are easy to get wrong.
- **Cross-links:** Every node links to a `/wrestlers/` page where one exists, or is flagged as a gap.
  This ties into the existing `/relationships/` section and gives it structure.

### 9. Wrestling Glossary and Lore terms
- **Route:** `/glossary/` and `/glossary/{term}/`.
  Examples: `/glossary/kayfabe/`, `/glossary/heel/`, `/glossary/babyface/`, `/glossary/botch/`,
  `/glossary/work/`, `/glossary/shoot/`, `/glossary/jobber/`, `/glossary/heat/`, `/glossary/spot/`.
- **Why it wins:** Definitional queries ("what is kayfabe", "heel vs face meaning") are pure AI-answer
  bait and rank fast because they are short, factual, and self-contained. Owning the vocabulary makes
  Wrestle Lore the source an answer engine quotes when it explains the sport, which is the GEO play
  the inspiration research prioritized. It also delivers on the "Lore" in the site name.
- **Buildability:** Trivially static. Each term is one tight definition plus a real example that links
  into the catalog. Ship `DefinedTerm` and a site-wide `DefinedTermSet`.
- **Cross-links:** Every example links to a real `/wrestlers/`, `/matches/`, `/moments/`, or
  `/rivalries/` page (for example, "shoot" links to the Montreal Screwjob rivalry). Glossary terms
  can be auto-linked on first use across other pages.

### 10. Venue and Arena pages
- **Route:** `/venues/` and `/venues/{slug}/`.
  Examples: `/venues/madison-square-garden/`, `/venues/allstate-arena/`,
  `/venues/mercedes-benz-superdome/`, `/venues/tokyo-dome/`.
- **Why it wins:** Venue pages capture "wrestlemania venues" and "[arena] wrestling events" searches
  and give the events catalog a geographic axis. Tokyo Dome ties the new NJPW promotion in through
  Wrestle Kingdom.
- **Buildability:** Static, and a natural home for the attendance and gate data below. Ship `Place`
  plus `ItemList` of events held there. `VERIFY`: every attendance and gate figure with a source;
  these are the most-often-fabricated numbers in wrestling, so cite each one.
- **Cross-links:** Each venue lists its `/events/` and the notable `/matches/` and `/moments/` that
  happened there.

### 11. Records and Leaderboards
- **Route:** `/records/` and `/records/{metric}/`.
  Examples: `/records/longest-title-reigns/`, `/records/most-championships/`,
  `/records/most-wrestlemania-matches/`, `/records/highest-rated-matches/`,
  `/records/largest-attendance/`.
- **Why it wins:** Ranked lists trigger the "who is number one" curiosity and the completionist pull
  from the inspiration research, and they are the most link-worthy, most-cited format on the web.
  These leaderboards are assembled from data the title, match, and venue types already hold, so they
  are almost free once those exist.
- **Buildability:** Static, pre-computed at author time from front-matter. Ship `ItemList` JSON-LD.
  `VERIFY`: every ranked figure against its source; label the star-rating source explicitly.
- **Cross-links:** Every ranked row links back to the entity page it measures. This absorbs and
  extends the existing `/rankings/` section.

### 12. Debut and Retirement tracker
- **Route:** `/timeline/debuts/`, `/timeline/retirements/`, and per-year `/timeline/{year}/`.
- **Why it wins:** "who is retiring in 2026" and "wrestlers who debuted in [year]" are recurring,
  news-driven queries. With John Cena's retirement tour and the AJ Styles retirement flag from the
  research, this type is timely, but it must stay strictly factual.
- **Buildability:** Static, generated from debut and retirement dates in wrestler front-matter.
  `VERIFY`: the AJ Styles retirement is single-source in the research and must not be stated as fact
  until confirmed; John Cena's status is a "retirement tour" flag, not a completed retirement.
- **Cross-links:** Each entry links to a `/wrestlers/` page and, where applicable, the `/events/` of
  the debut or farewell match.

---

## Tier 3 — Worth it, but data or media caveats

### 13. Entrance Theme archive
- **Route:** `/themes/` and `/themes/{slug}/` (for example `/themes/real-american/`,
  `/themes/my-time-is-now/`).
- **Why it wins:** Entrance music is a beloved, high-search topic ("wwe theme songs"). It deepens the
  sensory side of the profiles.
- **Buildability caveat:** Do not host audio. Static pages can carry the title, composer, the
  wrestler it belongs to, and a link out to an official clip. Treat audio as a link-out, not an asset.
  `VERIFY`: composer and licensing details; music rights are a real trap, so link only to official
  sources.
- **Cross-links:** Each theme links to its `/wrestlers/` page and the `/moments/` where the entrance
  itself was the story.

### 14. Promo and Mic-Work archive
- **Route:** `/promos/` and `/promos/{slug}/` (for example `/promos/austin-316/`,
  `/promos/pipebomb/`, `/promos/cutting-edge/`).
- **Why it wins:** Iconic promos are searched by quote and drive strong engagement. Austin 3:16 and
  the CM Punk pipebomb are canonical.
- **Buildability caveat:** Static text pages built around the verified quote and context, with a
  link out to video rather than an embed you host. Overlaps `/moments/`; keep promos as spoken-word
  incidents and moments as physical-incident pages, and cross-link the two. `VERIFY`: exact quote
  wording and date. The pipebomb already exists as `/rivalries/cm-punk-pipebomb/`, so link, do not
  duplicate.
- **Cross-links:** Each promo links to the speaker's `/wrestlers/` page, the `/events/` it aired on,
  and any related `/rivalries/`.

---

## Backend-flagged (do not attempt on the static stack without a service)

These are attractive but violate the no-build, no-storage, no-server constraint. Flagged so nobody
tries to fake them:

- **Live current-champions board that auto-updates.** A `/titles/current/` page is fine as a
  hand-set static snapshot, but any auto-refresh needs a backend or a scheduled rebuild. Ship the
  static snapshot; schedule an editorial refresh instead.
- **User ratings, reviews, and voting.** The whole review-network dream implies accounts and a
  database. For v1, publish editorial and cited community ratings and label which is which, exactly as
  the inspiration research recommends. Real voting is a backend project.
- **Personalized "continue browsing" or watch history.** Impossible without storage or login. Use
  the pre-rendered "Keep going" related-links block instead, which achieves the same retention effect
  crawlably.
- **Live attendance and gate feeds.** Static tables with cited figures only; no live data.

---

## Ranked master table (search demand x buildability)

| Rank | New type | Route | Demand | Buildability | Backend? |
|---|---|---|---|---|---|
| 1 | Title lineage | `/titles/{belt}/` | Very high | Pure static | No |
| 2 | Eras and timeline | `/eras/{slug}/`, `/timeline/{year}/` | Very high | Pure static | No |
| 3 | Factions and stables | `/factions/{slug}/` | High | Pure static | No |
| 4 | Move and finisher index | `/moves/{slug}/` | Very high | Pure static | No |
| 5 | Head-to-head versus | `/versus/{a}-vs-{b}/` | Very high (long-tail) | Static, curated pairs | No |
| 6 | This day in wrestling | `/this-day/{mm-dd}/` | High, recurring | Static + tiny JS redirect | No |
| 7 | Tag-team database | `/tag-teams/{slug}/` | Medium-high | Pure static | No |
| 8 | Family dynasties | `/dynasties/{slug}/` | Medium-high | Static (CSS tree) | No |
| 9 | Glossary and lore terms | `/glossary/{term}/` | High (AI-answer) | Trivially static | No |
| 10 | Venues and arenas | `/venues/{slug}/` | Medium | Static | No |
| 11 | Records and leaderboards | `/records/{metric}/` | High | Static, pre-computed | No |
| 12 | Debut and retirement tracker | `/timeline/debuts/` | Medium, timely | Static | No |
| 13 | Entrance themes | `/themes/{slug}/` | Medium | Static, link-out audio | No (no hosting) |
| 14 | Promo and mic-work archive | `/promos/{slug}/` | Medium | Static, link-out video | No |

## Build sequence recommendation

Ship types 1, 4, and 6 first. Title lineage closes a gap the nav already advertises, the move index
is the cheapest large-search win the base specs miss, and This Day in Wrestling installs the daily
return habit. Types 2, 3, and 5 follow to complete the browse spine and the long-tail engine. Every
page in every type must end with the mandatory "Keep going" related-links block, because that block
is simultaneously the retention lever and the internal-linking structure that search and AI engines
reward.
