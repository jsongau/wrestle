# Wrestle Lore — Vision Spec C: Data Graph & Discovery

Role: data/graph and discovery futurist. This spec turns the whole catalog (89 wrestlers, 30 rated
matches, 15 rivalries, 5 promotions, events, moments) into one connected graph, then builds discovery
experiences on top of it. Every idea ships on the current stack: static HTML, no build step, one
`css/site.css`, vanilla JS, no browser storage, root-absolute crawlable links. Backend needs are
flagged explicitly and kept optional.

Ground rules honored: no fabricated facts (crossover and family edges carry a `VERIFY` flag until a
source is attached), no decorative arrows, no em-dash separators, no cliché filler, specific nouns.

Sibling specs: A (new content types) and B (interactive tools). B already proposes a Six Degrees
*tool* and a shared `entities.json`. This spec does not re-pitch that tool. It defines the graph
*data layer* underneath it, the *crawlable* pre-rendered pages it should also emit, and five graph
experiences the base specs do not surface: a cross-promotion crossover map, a scoped network map, an
honest HEAT signal, graph-typed rabbit-hole rails on every page, and no-login session personalization.

---

## 0. The foundation everything else stands on: `graph.json`

One static file, generated once at author time from the page front-matter that already exists, plus a
small hand-curated edge file for facts the front-matter does not carry (family, romance, mentor,
crossover). This is the same object B calls `entities.json`, extended with typed, weighted, sourced
edges. Build it, and ideas 1 through 6 all fall out of it.

Shape:

```
{ "nodes": [ { "id":"aj-styles", "name":"AJ Styles", "type":"wrestler",
              "promos":["tna","njpw","wwe"], "era":"modern", "status":"current",
              "heat": 0, "degree": 0 } ],
  "edges": [ { "a":"aj-styles", "b":"samoa-joe", "rel":"faced",
              "weight":3, "evidence":"/matches/styles-vs-daniels-vs-joe-unbreakable-2005/",
              "verify": false } ] }
```

Edge vocabulary (each rendered as a distinct rail label and a distinct badge color):
`faced` (shared a match), `feuded` (has a rivalry page), `allied` (same faction or tag team),
`family` (real blood or marriage), `mentored` (trainer or protege), `crossed` (moved between
promotions), `debuted-with`, `betrayed`. Weight = count of shared matches or storyline depth, so rails
and the map can rank the strongest links first.

- **Buildability:** pure static. A ~15KB to 60KB JSON, gzip-served, parsed once by any page that needs
  it. No backend. Derive `faced`/`feuded`/`allied` automatically from match, rivalry and relationship
  pages already written; hand-author `family`/`mentored`/`crossed` from `/data/storylines-relationships.md`
  and `/data/expansion-rivalries-factions.md`, each with an `evidence` URL or `VERIFY`.
- **Why it wins:** one artifact feeds the six-degrees tool (B), the network map (idea 3), the crossover
  map (idea 4), the HEAT score (idea 5), the rails (idea 6) and next-up (idea 7). Author the truth once.
- **Cross-links:** consumed by `/relationships/`, `/rankings/`, every `/wrestlers/{slug}/`, and B's `/lab/`.

---

## Idea 1. Six Degrees connector, and the crawlable path pages under it

Route (tool): `/connect/` hub plus the live picker B already specced at `/lab/connect/`.
Route (the new part): pre-rendered static pages `/connect/{a}-to-{b}/`, one per high-demand pairing.

The interactive picker is B's. The addition here is the SEO and GEO half: run breadth-first shortest
path over `graph.json` at author time and **pre-render the top pairings as real HTML pages**. Example:
`/connect/john-cena-to-cm-punk/`, `/connect/sting-to-roman-reigns/`, `/connect/aj-styles-to-the-rock/`.
Each page shows the shortest chain with every hop as a linked entity and the evidence match or faction
under it, then a "Try another pair" link into the live tool.

- **Why it wins:** "how are X and Y connected" is a real search and a natural AI-answer question. A
  static answer page with `ItemList` schema and named hops is exactly what answer engines cite, and it
  is a dense internal-linking node (six clickable entities per page). Generating 150 pairings from the
  most-connected nodes is a loop, not a content-writing job.
- **Buildability:** pure static. BFS in the generator; no client JS required for the pre-rendered pages
  (the live picker reuses B's code). Cap the gallery to curated marquee pairings so the URL space stays
  intentional and every page is genuinely interesting.
- **Anti-fabrication:** a path is only as true as its edges. If any hop rides a `VERIFY` edge, the page
  says so on that hop rather than asserting it.
- **Cross-links:** hops link to `/wrestlers/{slug}/`; evidence links to `/matches/` and `/rivalries/`;
  footer links to `/connect/` and the `/map/` view centered on either endpoint.

---

## Idea 2. The Lore Number: a Kevin-Bacon anchor for wrestling

Route: `/connect/lore-number/` plus a small "Lore Number: 2" chip on every `/wrestlers/{slug}/`.

Pick one deliberately central node (Ric Flair is the strongest candidate given his cross-era, cross-
promotion reach; confirm against the computed graph before locking) and compute every wrestler's degree
of separation from that anchor. Publish the distribution: how many wrestlers are one hop away, two hops,
the rare outliers at four-plus. The chip on each profile ("Ric Flair number: 2") is a curiosity hook
that begs a click into the path.

- **Why it wins:** it is a shareable, quotable stat that no other wrestling database publishes, which is
  precisely the kind of novel structured claim that earns AI citations and social pull. It also turns an
  abstract graph into a single friendly number on 89 pages.
- **Buildability:** pure static. One BFS from the anchor over `graph.json` at build; write the number
  into each profile and one ranked table page. No backend.
- **Cross-links:** the chip links to `/connect/ric-flair-to-{slug}/`; the hub links to `/rankings/` and
  the network map. Recompute whenever a wrestler is added.

---

## Idea 3. Scoped interactive network map

Routes: `/map/` (whole graph), `/map/{promotion}/` (for example `/map/wcw/`), `/map/faction/{slug}/`
(for example `/map/faction/the-shield/`, `/map/faction/nwo/`), plus an embedded mini-map panel on each
`/wrestlers/{slug}/` titled "Their web" showing that node and its immediate neighbors.

A force-directed node-link view rendered from `graph.json`. Node color encodes promotion (reuse the
existing accent tokens), node size encodes degree, edge color encodes relationship type. Click a node to
recenter; every node is also a plain link to its page.

- **Why it wins:** this is the single most "future of wrestling databases" surface in the whole project.
  Cagematch has tables; nobody has an explorable relationship map. It is a deep-session magnet (people
  drag and recenter for minutes) and it makes the abstract "network" concrete for a hiring manager in
  one screenshot.
- **Buildability:** the interactive layout is the heaviest lift in this spec. Vanilla JS force layout on
  canvas is feasible for the scoped views (a promotion or faction subgraph is dozens of nodes, not
  thousands); flag the whole-graph `/map/` for performance and cap or cluster it. **Crawlability guard:**
  ship a pre-rendered static SVG of each scoped map plus a plain linked node list inside `<noscript>`, so
  the page is fully crawlable and works with JS off. No backend; the canvas reads the static JSON.
  Rendering the whole-graph physics live is the only part that could justify a future service, and even
  that is optional. Flag: needs a lightweight force-layout routine (~150 lines) added to the JS bundle.
- **Cross-links:** every node links to its entity page; the scoped hubs link to `/promotions/{slug}/`
  and `/relationships/`; profile mini-maps link to the full `/map/{their-promotion}/`.

---

## Idea 4. Cross-promotion crossover map

Routes: `/crossover/` hub plus one directional page per lane:
`/crossover/wcw-to-wwe/`, `/crossover/ecw-to-wwe/`, `/crossover/tna-to-wwe/`, `/crossover/njpw-to-wwe/`,
`/crossover/wcw-to-tna/`, and the reverse lanes worth telling. A `/crossover/aew/` and `/crossover/njpw/`
lane covers modern talent movement once those hubs exist.

The signature graph story of pro wrestling is talent moving between companies: the WCW and ECW invasion
talent that landed in WWE, the TNA originals who became WWE headliners, the Bullet Club pipeline out of
NJPW. Each lane page is a flow view (a static Sankey-style column or a simple two-column ledger) listing
every wrestler who made that jump, with their run in each promotion and the match or event that marks
the crossover.

- **Why it wins:** enormous evergreen search demand ("wrestlers who went from WCW to WWE", "TNA
  wrestlers now in WWE", "NJPW to WWE") with almost no strong single-page answer online, which is a GEO
  opening. It is also the perfect frame for the newly added NJPW promotion and the AJ Styles showcase
  (TNA to NJPW to WWE is a three-lane story that this map is built to tell). Each lane is a dense hub
  linking a dozen-plus wrestler pages and both promotion hubs.
- **Buildability:** pure static, pre-rendered from the `crossed` edges in `graph.json`. A CSS-grid flow
  layout needs no JS. **Fact caution:** every crossover claim must carry a source; mark unconfirmed
  jumps `VERIFY` and do not publish a lane page until its roster is checked against
  `/data/expansion-wrestlers.md`. Do not invent movements.
- **Cross-links:** each name links to `/wrestlers/{slug}/`; column headers link to `/promotions/{a}/`
  and `/promotions/{b}/`; feature AJ Styles across the TNA, NJPW and WWE lanes and back-link to
  `/wrestlers/aj-styles/`; link the hub to `/relationships/` and the network map.

---

## Idea 5. HEAT: an honest trending signal (no fake counters)

Routes: `/heat/` leaderboard hub plus a small HEAT badge component reusable on any tile.

"What is hot right now" without lying about live traffic. HEAT is a labeled, honest blend of three
inputs, each of which the static site can actually know:
1. **Timely (editorial):** a hand-set weekly list of wrestlers, matches or rivalries tied to what aired
   on this week's shows. Honest because a human set it.
2. **Structural (computed):** graph centrality, that is degree and betweenness from `graph.json`. This
   surfaces the genuinely most-connected and the "bridge" figures who link otherwise separate clusters.
   Publish this as its own evergreen ranking, "Most Connected", so the page has value even in a quiet
   week.
3. **Recency (build metadata):** "Recently added" pulled from the generator, never a fabricated view
   count.

Keep the three inputs visibly labeled so nothing pretends to be live analytics.

- **Why it wins:** a reason to return weekly (the timely list) plus an evergreen ranking that ranks and
  gets cited (the centrality list). The "bridge wrestler" angle (who connects the most clusters) is a
  novel, quotable stat, the same citation lever as the Lore Number.
- **Buildability:** structural and recency parts are pure static (centrality is a short graph pass at
  build). The timely list is a manual weekly edit of one small data file. **Backend flag:** genuine
  real-time popularity (actual clicks, actual trends) would need an analytics service and a tiny
  read-only endpoint; that is explicitly out of scope for v1 and the honest static blend replaces it.
- **Cross-links:** HEAT badges sit on tiles across `/wrestlers/`, `/matches/`, `/rivalries/`; the hub
  links to `/rankings/`, `/heat/most-connected/`, and every ranked entity.

---

## Idea 6. Rabbit-hole rails on every page, powered by the graph

Route: no new route. A required "Keep going" block appended to the bottom of every entity page, and
graph-typed related rails higher up.

Inspiration spec B2 named the "keep going" block as the top retention lever. This makes it automatic and
typed instead of hand-written. From a page's node in `graph.json`, emit rails by edge type:
"Shared a ring with", "Same faction", "Ran the same promotion", "One degree away", "Crossed over from
the same company", ranked by edge weight. Every rail is four to six linked tiles. No page ever
dead-ends.

- **Why it wins:** it is simultaneously the retention engine (a contextual next click at every exit) and
  the internal-linking backbone that search and answer engines reward. Same graph pass, two payoffs.
  Typed labels ("Shared a ring with") read as specific human curation, not a generic "related" box.
- **Buildability:** pure static, generated at author time from `graph.json`. Zero client JS for the
  server-rendered rails. Enforce a floor (every page ships at least eight outbound entity links) as a
  build check so no profile is a dead end.
- **Cross-links:** by definition, dense outbound links into `/wrestlers/`, `/matches/`, `/rivalries/`,
  `/factions/` (spec A), `/promotions/`. Feeds and is fed by the crossover and network views.

---

## Idea 7. No-login, no-storage "Next Up" personalization

Routes: no new route. A "Because you just looked at {X}" rail and a live "Your trail" strip, injected
client-side into any page.

The hard constraint is no browser storage: no localStorage, no cookies. So personalization lives in two
honest, private places instead:
1. **In-memory session trail.** A JS array in the page's runtime, seeded from the referrer and from a
   `?from={slug}` param that internal links carry, then handed forward via the same param as the user
   clicks. This drives a "Because you just looked at AJ Styles, try these" rail computed from that node's
   graph neighbors, and a small "Your trail" breadcrumb of the current session's path.
2. **URL as memory.** Because the trail rides in the URL, a session is shareable and back-button safe,
   and it needs zero storage. It resets on a cold entry, which is the correct, private behavior.

- **Why it wins:** the Netflix "because you watched" pull, delivered with no account, no cookie banner,
  no privacy cost. It deepens sessions (each page adapts to where you just were) and, because the
  recommendations are graph edges, every suggestion is also a real internal link.
- **Buildability:** pure static plus a small vanilla JS enhancement (~60 lines) reading `?from=` and
  `document.referrer`, computing neighbors from `graph.json`. Degrades cleanly: with JS off, the page
  still shows the server-rendered graph rails from idea 6. **Honest limit to flag:** without storage,
  personalization does not persist across a reload or a new visit; true cross-session memory
  ("continue where you left off", a saved watchlist) would require storage or a backend, and that is a
  deliberate, stated non-goal for v1.
- **Cross-links:** the rail links to `graph.json` neighbors of the just-viewed node; the trail strip
  links back to each entity in the current session path.

---

## How the seven fit together

`graph.json` (idea 0) is the trunk. The six-degrees pages and Lore Number (1, 2) are shortest-path
reads of it. The network map and crossover map (3, 4) are two visual projections of it. HEAT (5) is a
ranking pass over it. The rails and next-up (6, 7) are per-page reads of it. Author the relationships
once, ship seven discovery surfaces, and every one of them thickens the internal-linking mesh that both
retention and search feed on.

## Build order (highest leverage first)

1. `graph.json` generator and the graph-typed rails on every page (ideas 0 and 6). Foundation plus the
   biggest retention and SEO lever, both pure static.
2. Crossover map (idea 4). Distinctive, high search demand, pure static, showcases NJPW and AJ Styles.
3. Six-degrees crawlable path pages and the Lore Number chip (ideas 1 and 2). Cheap loops over the graph,
   strong GEO citation targets.
4. HEAT hub with the "Most Connected" evergreen ranking (idea 5). Pure static; add the weekly timely
   edit as an ongoing habit.
5. Scoped network map (idea 3). Highest engagement payoff, heaviest JS; ship scoped SVG-fallback views
   first, whole-graph later.
6. No-login next-up (idea 7). A polish layer once the graph and rails exist.

## Verification queue (do not publish until sourced)

- Every `crossed`, `family`, `mentored` edge needs an evidence URL; default them to `VERIFY`.
- Confirm the most central node before naming the Lore Number anchor (Ric Flair is the hypothesis, not a
  fact, until the graph is computed).
- AJ Styles status and any crossover copy inherit the `VERIFY` flag already noted in the content research.
- NJPW crossover lanes depend on the NJPW promotion hub and roster being built first.
