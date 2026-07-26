# Wrestle Lore — Future Roadmap & New Pages

Head-of-product synthesis of the six futurist specs (`vision/A` through `vision/F`) into one ranked
plan. Every proposed new page and feature is scored, de-duplicated across specs, grouped into NOW /
NEXT / LATER waves, and given a concrete route, a one-line pitch, its cross-links, and a backend flag.

- Date: 2026-07-26
- Grounding: `00-content-data-research.md`, `01-inspiration-research.md`, and `vision/A..F`.
- Source specs merged here: A (new content types), B (interactive tools), C (data graph and
  discovery), D (community and gamification), E (GEO and the AI answer engine), F (growth and
  monetization).
- Standing constraints: static HTML, no build step at request time, one `css/site.css`, vanilla JS,
  no browser storage, root-absolute crawlable links, every page pre-rendered at author time.
- Fact rule: no invented reigns, records, ratings, dates, or business terms. Every data-heavy or
  business-heavy item carries a `VERIFY` flag on the specific facts to confirm before publishing.
- Existing routes to link into: `/wrestlers/` (89), `/matches/` (30 rated), `/rivalries/` (15),
  `/promotions/{wwe,wcw,ecw,tna,nxt}/`, `/events/` (5 PLE editions + 5 brand hubs), `/moments/` (4),
  `/rankings/`, `/relationships/`, `/membership/` and `/membership/growth-strategy/`. The site header
  already advertises `/titles/`, which is unbuilt.

---

## Scoring model

- **Impact (1 to 5):** a blend of search demand, engagement or retention, and revenue. 5 means it
  moves all three or dominates one lever the hiring manager reports on.
- **Effort (1 to 5):** build cost on the current static no-build stack. 1 is trivial from front-matter
  already authored. 5 needs a backend service, live data, or a legal-rights clearance.
- **Priority = Impact minus (Effort minus 1).** Higher ships sooner. Ties broken by whether the item
  is a foundation other items depend on, closes an advertised gap, or earns revenue on day one.
- **Wave:** NOW ships on the static stack first and unlocks the rest. NEXT is still static but needs
  more curation, more data, or depends on a NOW item. LATER needs a backend, live data, or rights.

The one dependency almost everything reads is a single build-time data file. B calls it
`entities.json`, C extends it to `graph.json` (typed, weighted, sourced edges). It is one static
artifact next to `js/search-index.js`, emitted by the existing Python builders. Ship it first; it is
the trunk the tools, the graph views, the rails, and the GEO exports all read.

---

## The single ranked master table

Ordered by Priority. Backend column: `No` ships static today, `Later` is a static v1 with a
backend-only v2, `Backend` needs a service for any version.

| # | New page / feature | Route | Wave | Impact | Effort | Backend | One-line pitch | Key cross-links |
|---|---|---|---|---|---|---|---|---|
| 1 | Data trunk: entities + graph | `/data/entities.json`, `/data/graph.json` | NOW | 5 | 2 | No | One static file of typed, sourced, weighted relationships that every tool, map, rail, and GEO export reads. | Feeds every route below; consumed by `/lab/`, `/map/`, `/rankings/`, all profiles. |
| 2 | Championship title lineages | `/titles/`, `/titles/{belt}/` | NOW | 5 | 2 | No | The reign table for every belt, the exact shape answer engines lift, closing the gap the nav already promises. | `/wrestlers/`, `/events/`, `/matches/`, `/promotions/`. |
| 3 | Graph-typed rabbit-hole rails | every entity page (no new route) | NOW | 5 | 2 | No | A required "Keep going" block auto-built from the graph so no page dead-ends, the retention and internal-link backbone at once. | Dense outbound to `/wrestlers/`, `/matches/`, `/rivalries/`, `/factions/`, `/promotions/`. |
| 4 | Move and finisher index | `/moves/`, `/moves/{slug}/` | NOW | 5 | 2 | No | "What is an RKO" is enormous and unowned; a definitional primitive linked from the finisher line on all 89 profiles. | `/wrestlers/` (finisher line), `/matches/` (match-deciding move). |
| 5 | Head-to-head compare and versus | `/compare/`, `/compare/{a}-vs-{b}/`, `/versus/{a}-vs-{b}/` | NOW | 5 | 2 | No | Tale-of-the-tape stats plus the win-loss record, the single most citable answer format, state in the URL to share. | `/wrestlers/`, `/rivalries/`, `/matches/`, `/events/`. |
| 6 | Markdown mirror + llms files | `*.md` twins, `/llms.txt`, `/llms-full.txt` | NOW | 5 | 2 | No | A clean `.md` twin of every page plus a corpus map, the format LLM retrieval ingests cleanest, near-free from existing dicts. | `<link rel=alternate>` on every page; `.md` Related lists walk the graph. VERIFY: rename from "MAT" and lock the domain first. |
| 7 | Streaming affiliate + watch hub | `/watch/`, `/watch/{promotion}/` | NOW | 5 | 2 | Later | Wrap the live "where to watch" badges into tracked links and a hub that ranks for "how to watch WWE PLEs," revenue at peak intent. | `/promotions/`, `/events/` watch cards, `/membership/`. VERIFY affiliate terms per partner. Backend only for a `/go/` redirect. |
| 8 | Six Degrees of Wrestling | `/lab/connect/`, `/connect/{a}-to-{b}/` | NOW | 4 | 2 | No | Client-side shortest-path between any two wrestlers, trivia-shaped pages ("How is IYO SKY connected to Ric Flair") that read as answer-engine bait. | Every hop links a profile; every edge links its `/matches/` or `/rivalries/` receipt. |
| 9 | This Day in Wrestling | `/this-day/`, `/this-day/{mm-dd}/` | NOW | 4 | 2 | No | 366 dated pages plus a tiny JS redirect to today, a daily return habit from anniversary facts already held. | `/wrestlers/`, `/matches/`, `/events/`, `/moments/`. VERIFY every anniversary date. |
| 10 | Guess the Wrestler daily game | `/play/guess/`, `/play/guess/archive/` | NOW | 4 | 2 | No | A date-seeded Wordle-style puzzle with a shareable spoiler-free grid, the strongest return-visit loop and a soft membership trigger. | Reveal links the answer profile; `?mode=wcw` variants; `/membership/`. |
| 11 | Best-of answer pages | `/best/{topic}/` | NOW | 4 | 2 | No | Ranked "best five-star / 2026 / WrestleMania / women's matches" pages with ItemList schema built to win the AI Overview. | `/matches/`, `/leaderboards/`, `/eras/`. Label rating source editorial vs cited. |
| 12 | Faction and stable database | `/factions/`, `/factions/{slug}/` | NOW | 4 | 2 | No | Bloodline, nWo, Four Horsemen, Bullet Club member histories, completionist search that ties NJPW into the roster. | `/wrestlers/`, `/rivalries/`, `/matches/`. VERIFY rosters and dates. |
| 13 | Eras and year timeline | `/eras/{slug}/`, `/timeline/{year}/` | NEXT | 4 | 2 | No | The Attitude Era and its siblings as browse destinations, the spine that makes the poster wall navigable by feel. | `/wrestlers/` (era badge), `/matches/`, `/rivalries/`, `/promotions/`. VERIFY era boundary years. |
| 14 | Cross-promotion crossover map | `/crossover/`, `/crossover/{a}-to-{b}/` | NEXT | 4 | 2 | No | "Which wrestlers went from WCW to WWE" and NJPW-to-WWE flow pages, huge evergreen demand with no strong answer online. | `/wrestlers/`, `/promotions/`; features AJ Styles across TNA, NJPW, WWE. VERIFY every jump. |
| 15 | Glossary + what-is / who-is | `/glossary/{term}/`, `/what-is/{term}/`, `/who-is/{slug}/` | NEXT | 4 | 1 | No | Kayfabe, heel, shoot, and short factual question pages, pure People-also-ask and voice-answer capture with DefinedTerm schema. | Examples link real `/wrestlers/`, `/matches/`, `/rivalries/`, `/moments/`. |
| 16 | Records and leaderboards | `/records/{metric}/`, `/leaderboards/` | NEXT | 4 | 2 | Later | Numbered "longest reigns / most titles / highest rated" lists, the most link-earned format, editorial now and re-sortable on real votes later. | Every row links its entity; `/promotions/`, `/eras/`, `/rankings/`. Backend only to re-sort on user votes. |
| 17 | Ask the Database hub | `/ask/`, `/ask/{slug}/` | NEXT | 4 | 2 | Later | A pre-rendered map of every question the site answers with a client-side filter, the feel of querying a database with zero backend. | `/best/`, `/compare/`, `/what-is/`, entity hubs. Backend only for v2 live retrieval. |
| 18 | Fantasy booking studio | `/booker/`, `/booker/{slug}/` | NEXT | 4 | 3 | Later | Build and share a full fantasy card as a URL, the most-loved fan pastime turned into a viral backlink engine. | `/wrestlers/`, `/matches/` (stipulation examples), `/events/`, `/compare/`. Backend for save, upvote, community board. |
| 19 | Dataset schema + data catalog | `/data/`, sharpen `sameAs` and SportsOrganization | NEXT | 4 | 2 | No | Declare the whole site a citable Dataset and resolve every wrestler to Wikidata, the trust signal answer engines weight. | `/methodology/`, entity pages. VERIFY every external `sameAs` URL. |
| 20 | Event-surge lifecycle template | `/events/{event}/preview/`, `/live/`, `/results/` | NEXT | 4 | 3 | Later | A reusable pre-show, live, and recap arc that captures the PLE demand spike and stacks affiliate clicks on membership conversion. | `/watch/{promotion}/`, participant profiles, `/rivalries/`, `/membership/`. Backend for email capture and prediction grading. |
| 21 | Scoped relationship network map | `/map/`, `/map/{promotion}/`, `/map/faction/{slug}/` | NEXT | 4 | 4 | No | An explorable force-directed relationship view no wrestling database has, with a pre-rendered SVG and `<noscript>` list for crawlability. | Every node links its page; `/promotions/`, `/relationships/`; profile mini-maps. Whole-graph physics is the only heavier optional lift. |
| 22 | Curated collections | `/collections/`, `/collections/{slug}/` | NEXT | 3 | 2 | Later | Finite themed checklists (Five-Star Club, every Bloodline match) that deliver the Letterboxd completionist pull with no login. | `/matches/`, `/wrestlers/`, `/promotions/`, `/eras/`. Backend for personal progress and badges. |
| 23 | Lore Number | `/connect/lore-number/`, chip on every profile | NEXT | 3 | 2 | No | A Kevin-Bacon anchor stat ("Ric Flair number: 2") on 89 profiles, a novel quotable claim that earns citations. | Chip links the shortest path; `/rankings/`, the map. VERIFY the most-central anchor against the computed graph. |
| 24 | Tag-team database | `/tag-teams/{slug}/` | NEXT | 3 | 2 | No | Member histories and reigns for the Hardys, Usos, New Day, giving the tag-war rivalries a proper home. | `/wrestlers/`, tag `/titles/`, `/matches/`. VERIFY reigns and membership. |
| 25 | Career timeline explorer | `/lab/timeline/`, embedded on profiles | NEXT | 3 | 3 | No | A scrubbable per-career timeline plus an era slider across the whole roster, a nostalgia magnet that lifts time on page. | Dots link `/matches/`, `/events/`; era hubs. Progressive enhancement over static facts. |
| 26 | Bracket and prediction maker | `/play/bracket/{event}/` | NEXT | 3 | 3 | Later | Fill a Rumble or tournament bracket, share it, then get graded when real results land, a two-visit loop tied to the live calendar. | `/events/{edition}/`, participants, `/compare/`. Backend only for a cross-user leaderboard. |
| 27 | HEAT trending hub | `/heat/`, `/heat/most-connected/` | NEXT | 3 | 2 | No | An honest, labeled blend of a weekly editorial list, graph centrality, and recently-added, with a novel "bridge wrestler" ranking. | Badges on tiles; `/rankings/`, entity pages. Backend only for genuine live popularity. |
| 28 | Family dynasty trees | `/dynasties/{slug}/` | NEXT | 3 | 2 | No | The Hart, Anoa'i, Flair, Rhodes, Guerrero trees as crawlable CSS nested lists, high-dwell shareable curiosity. | Every node links a `/wrestlers/`; `/relationships/`. VERIFY exact relations. |
| 29 | Hot-take poll showcase | `/polls/`, `/polls/{slug}/` | NEXT | 3 | 2 | Later | Debate pages arguing both sides from cited data, dwell-time bait now and a live vote later. | Two `/wrestlers/`, top `/matches/`, `/compare/`, `/leaderboards/`. Backend for live voting. |
| 30 | Badge catalog | `/badges/` | NEXT | 3 | 1 | Later | Publish the full earn-it catalog (Five-Star Scout, Nitro Completionist, Head Booker) as an aspirational sign-up promise. | `/membership/`, `/booker/`, `/collections/`, `/leaderboards/`. Backend to award. |
| 31 | Star-rating sim + pairwise ranker | `/rate/{match}/`, `/lab/my-top-ten/` | NEXT | 3 | 2 | Later | Rate a match and compare to the editorial figure, or build a personal Top 10 in the URL, participation without moderation cost. | `/matches/`, `/leaderboards/`. Backend only for aggregate community ratings. |
| 32 | No-login next-up personalization | "Because you looked at X" rail (no new route) | NEXT | 3 | 3 | No | A Netflix-style rail computed from a `?from=` session trail, no cookie, no storage, degrades to the static rails. | Graph neighbors of the just-viewed node. Honest limit: no cross-session memory without a backend. |
| 33 | Venue and arena pages | `/venues/{slug}/` | NEXT | 2 | 2 | No | MSG, Tokyo Dome, and a geographic axis on the events catalog, ties NJPW in through Wrestle Kingdom. | `/events/`, `/matches/`, `/moments/`. VERIFY attendance and gate figures. |
| 34 | Debut and retirement tracker | `/timeline/debuts/`, `/timeline/retirements/` | NEXT | 2 | 2 | No | "Who is retiring in 2026" news-driven pages, timely but strictly factual. | `/wrestlers/`, `/events/`. VERIFY: AJ Styles retirement is single-source; Cena is a tour, not a completed retirement. |
| 35 | Creator profiles and lists | `/creators/{slug}/`, `/lists/{creator}/`, `/creators/embed/` | NEXT | 3 | 2 | Later | The canonical who-interviewed-whom index plus co-branded lists and embeddable widgets, turning creators into a backlink network. | `/wrestlers/`, `/collections/`. VERIFY affiliation and image rights. Backend for `?ref` attribution. |
| 36 | Entrance theme archive | `/themes/{slug}/` | NEXT | 2 | 2 | No | Theme, composer, and a link out to official audio (never hosted), deepening the sensory side of profiles. | `/wrestlers/`, `/moments/`. VERIFY composer and rights; link-out only. |
| 37 | Promo and mic-work archive | `/promos/{slug}/` | NEXT | 2 | 2 | No | Austin 3:16 and the pipebomb as quote-anchored pages, spoken-word incidents that complement `/moments/`. | Speaker profile, `/events/`, `/rivalries/`. Link, do not duplicate, the existing pipebomb rivalry. |
| 38 | User ratings and reviews | `/matches/*`, `/reviews/{slug}/`, `/u/{username}/` | LATER | 5 | 5 | Backend | Real 1-to-5 stars and micro-reviews turn the editorial AggregateRating into legitimate UGC data, the top GEO and account-creation lever. | `/matches/`, `/u/`, `/leaderboards/`. Supabase: ratings, reviews, RLS, cron write-back to static JSON. |
| 39 | Membership depth ladder | `/insider/`, `/vault/`, `/insider/rewind/` | LATER | 4 | 5 | Backend | A free-account Insider layer and a gated stats Vault that gate the tail of tables, never the citable head, so SEO stays intact. | `/membership/`, tools in B, stats blocks. Supabase auth plus Stripe; share vision D's one backend. |
| 40 | Community fantasy cards | `/booker/community/`, `/booker/community/{id}/` | LATER | 3 | 5 | Backend | Save, publish, and upvote fan cards, converting a one-off share into a returning-creator UGC farm. | `/wrestlers/`, `/booker/`, `/leaderboards/`, `/badges/`. Supabase: cards, votes, write-back. |
| 41 | Live polls + reviewer board | `/polls/*`, `/leaderboards/reviewers/` | LATER | 3 | 5 | Backend | Real one-vote-per-day polling and a top-reviewer ranking, pure status mechanics that reward showing up. | `/compare/`, `/leaderboards/`, `/u/`. Supabase: poll votes, materialized reviewer view. |
| 42 | Personal collections + badges | `/u/{username}/`, progress on `/collections/{slug}/` | LATER | 3 | 5 | Backend | Trackable "12 of 18" collections, a watchlist, and awarded badges, the completionist payoff storage blocked until now. | `/collections/`, `/badges/`, entity pages. Supabase: watchlist, progress, user_badges. |
| 43 | Data and API licensing | `/data/licensing/`, `/api/v1/` | LATER | 4 | 5 | Backend | B2B licensing of the ratings, lineage, and graph dataset, the highest revenue-per-customer line, static JSON export now and a keyed API later. | `/data/`, `/methodology/`. Static `entities.json` export is the zero-backend v1. VERIFY all license terms with a human. |
| 44 | Ask the Database live retrieval | `/ask/` v2 | LATER | 3 | 5 | Backend | A natural-language box that runs retrieval over the site's own verified data, retrieval-only so it never fabricates. | Same surface as item 17. Serverless or edge function; the static v1 captures most of the GEO value. |
| 45 | Drops and print shop | `/drops/`, `/shop/` | LATER | 3 | 5 | Backend | Time-boxed member drops and print-on-demand posters from the poster-wall art, revenue and return-visit urgency. | `/membership/`, wrestler and match pages. Hard gate: name-and-likeness rights must clear first. Print-on-demand partner backend. |

---

## The five eye-opening flagship ideas

These differentiate Wrestle Lore most and read strongest to a WWE / TKO membership-growth manager.
Each is on the static stack (one has an optional heavier tier), and each proves a distinct instinct:
graph thinking, data visualization, habit design, AI-era distribution, and lifecycle growth.

1. **Six Degrees of Wrestling** (`/lab/connect/` + pre-rendered `/connect/{a}-to-{b}/`). Client-side
   shortest-path over the relationship graph. No competitor (Cagematch, Sherdog) has it. It turns the
   internal-link graph into a game, and trivia-shaped pages like "How is IYO SKY connected to Ric
   Flair" are prime answer-engine bait. Pure static.

2. **The interactive relationship network map** (`/map/`, `/map/{promotion}/`,
   `/map/faction/{slug}/`, plus a "Their web" mini-map on every profile). An explorable force-directed
   view of who faced, feuded, allied, and crossed over with whom. It makes the abstract network
   concrete for a hiring manager in one screenshot. Scoped subgraphs ship in vanilla JS with a
   pre-rendered SVG and `<noscript>` fallback for full crawlability; whole-graph physics is the only
   optional heavier lift.

3. **Guess the Wrestler daily game** (`/play/guess/`). A date-seeded Wordle-style puzzle with a
   clue ladder and a shareable spoiler-free result grid, no storage and no backend. It is the
   strongest daily return-visit loop on the site and a soft conversion into `/membership/`, which is
   the exact retention-to-signup behavior the role is hired to grow.

4. **The Markdown Mirror and Ask the Database** (`*.md` twins, `/llms-full.txt`, `/ask/`). A clean
   `.md` twin of every page, a concatenated corpus file, and a question-map hub built so ChatGPT,
   Perplexity, Gemini, and Claude quote Wrestle Lore by name. Near-free from the dicts the Python
   builders already hold, and a durable AI-citation advantage while competitors ship HTML only. The
   `/ask/` v1 is pure static; only its live-retrieval v2 needs a backend.

5. **The event-surge lifecycle campaign template** (`/events/{event}/preview/`, `/live/`,
   `/results/`). One reusable arc that captures the predictable PLE demand spike, stacks affiliate
   clicks at peak intent on top of membership conversion, and closes with a re-rate recap. It is the
   clearest on-the-job proof of a membership-growth manager's core skill: a repeatable, measurable,
   event-triggered funnel. Static today; email capture and prediction grading are the only backend.

---

## Build sequence

**NOW wave, in order:** ship the data trunk (item 1) first because everything reads it. Then title
lineages (2, closes the advertised nav gap), the graph-typed rails (3, the retention and internal-link
backbone), and the move index (4, the cheapest large-search win the base specs miss). Land compare and
versus (5) and the Markdown mirror plus `llms` files (6) for the SEO and GEO base, the streaming
affiliate hub (7) for revenue on day one, then Six Degrees (8), This Day (9), and Guess the Wrestler
(10) for differentiation and the daily habit, and best-of pages (11) and factions (12) to round out
the answer surface. Every page in every wave ends with the mandatory graph-typed "Keep going" block.

**NEXT wave:** the browse spine (eras, crossover map, glossary), the discovery layer (records,
ask hub, dataset schema, network map, Lore Number, HEAT), the creation tools (booker, timeline,
bracket, ranker), and the growth scaffolding (event-surge template, collections, badge catalog,
creator program) that goes live the moment the backend arrives.

**LATER wave:** the one shared Supabase backend lights up the UGC economy (ratings and reviews,
community cards, live polls, personal collections and badges) and the membership depth ladder, then
the data and API licensing product and the rights-gated drops and shop. User ratings and reviews is
the single highest-leverage LATER item because it converts the existing editorial AggregateRating into
legitimate data and is the lowest-friction reason to create an account.

## Cross-spec de-duplication notes

- `entities.json` (B), `graph.json` (C), and the `/data/entities.json` export (E and F) are one
  artifact, merged into item 1.
- `/compare/` (B), `/versus/` (A), and the comparison answer pages (E) are one product surface with a
  tool view and a pre-rendered answer view, merged into item 5.
- Book the Card (B) and the Fantasy Booking Studio (D) are one builder, merged into item 18.
- Watch-along hubs (D) and the streaming affiliate hub (F) are one `/watch/` system, merged into
  item 7, with the affiliate wrap as the revenue layer.
- Editorial leaderboards (D) and records (A) are one ranked-list system, merged into item 16.
- Six Degrees tool (B) and its crawlable path pages (C) are one product, merged into item 8.
- The `/data/` catalog appears in E (Dataset schema) and F (licensing); the static catalog is item 19,
  the commercial and API layer is item 43.

## Consolidated verification queue

- Reign dates and lengths, title-change events, and reign counts before any `/titles/` page ships.
- Faction, tag-team, and dynasty rosters and dates; family relations are easy to get wrong.
- Every `crossed`, `family`, and `mentored` graph edge needs an evidence URL or a `VERIFY` flag.
- The most-central node before naming the Lore Number anchor (Ric Flair is the hypothesis, not fact).
- Head-to-head records, title counts, and every external `sameAs` URL.
- Rename from "MAT" and the final production domain before `llms.txt` and the Markdown mirror ship.
- Affiliate program availability and terms per partner (ESPN, Netflix, HBO Max, NJPW World, TNA+,
  Amazon Associates).
- 2026 event calendar and dates before building preview pages (owned by the base workflow).
- AJ Styles retirement (single-source) and John Cena status (tour, not completed) before any tracker.
- Name-and-likeness rights before any merchandise, print, or paid collectible.
- Data-license terms (personal, commercial, AI-training) with a human before the licensing page.

## Anti-AI copy standard

Specific nouns (GTS, Wrestle Kingdom, Tokyo Dome, ESPN, Netflix, entry number 30), no decorative
arrows in prose, no em-dash separators, none of the banned cliche vocabulary. Every fantasy output is
labeled fantasy, every derived metric is labeled editorial, every rating is labeled editorial or
cited, and every unverified fact carries a `VERIFY` flag until sourced.
