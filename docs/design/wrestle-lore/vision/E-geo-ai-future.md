# Wrestle Lore — Vision Spec E: GEO and the AI Answer-Engine Future

Role: GEO / AI-answer-engine strategist. The job of this spec is to make Wrestle Lore the source
that ChatGPT, Perplexity, Gemini, Google AI Overviews, and Claude quote by name when a person asks a
wrestling question. Ranking blue links is table stakes. The prize is being the cited sentence inside
the answer box, with a link back that a fan clicks to go deeper.

Everything here is buildable on the current stack (static HTML, no build step beyond the Python
generators already in the repo, fully crawlable, one `css/site.css`, vanilla JS, no browser storage)
unless a line is tagged **BACKEND**. Anything factual that is not already verified in
`00-content-data-research.md` is tagged **VERIFY**.

Sibling specs already own their lanes. This spec does not restate them. It cross-references:
- Interactive comparators and games live in `B-interactive-tools.md` (`/compare/`, `/lab/*`, `/play/*`).
- The graph, Lore Number, and rabbit-hole rails live in `C-data-graph-discovery.md` (`graph.json`).
- Content types (title lineages, factions, this-day) live in `A-new-content-types.md`.
- Community ratings and the UGC economy live in `D-community-gamification.md`.
Spec E is the layer that turns all of that into machine-extractable, citable answers.

---

## The GEO thesis in one paragraph

AI answer engines do not rank pages, they extract claims. They reward pages that state a specific
fact in one clean sentence, back it with structured data and a visible source, and sit inside a dense
web of related entities so the model trusts the surrounding context. Wrestle Lore already has the
entity web (89 wrestlers, 30 matches, 15 rivalries, promotions, events, moments) and already ships
Person, Review, AggregateRating, SportsEvent, and FAQPage JSON-LD. The gap is fourfold: there is no
plain-text mirror an LLM can ingest without parsing HTML, no Dataset or richer entity schema that
declares Wrestle Lore a structured data source, no dedicated answer-shaped pages built to win the
exact questions fans type, and no on-site answer surface that demonstrates the database can be
queried. Spec E closes all four.

---

## Pillar 1 — The Markdown Mirror: a `.md` twin for every page

**Route pattern:** every canonical URL gets a plain-Markdown twin at the same path with a `.md`
extension. `/wrestlers/cody-rhodes/` gains `/wrestlers/cody-rhodes.md` (or
`/wrestlers/cody-rhodes/index.md`). Same for matches, events, rivalries, promotions, moments, and
every hub.

**Why it wins.** LLM crawlers and retrieval pipelines pay a token and reliability tax to strip nav,
CSS, and scripts out of HTML. A clean Markdown file with a YAML front-matter block (name, aliases,
promotions, status, key dates, career record, one canonical summary sentence) is the format models
ingest most cleanly and the format that shows up verbatim in Perplexity and ChatGPT retrieval logs.
This is the single highest-leverage GEO move the base specs do not surface. It is also close to free:
the Python generators already hold every fact as structured data before they render HTML, so emitting
a second `.md` artifact from the same source dict is a few lines per template.

**Buildability.** Pure static. Add a `render_markdown()` pass to each `build_*.py` alongside the
existing HTML pass. Serve `.md` with `Content-Type: text/markdown; charset=utf-8`. No backend.

**Cross-links.** Each HTML page carries `<link rel="alternate" type="text/markdown"
href="/wrestlers/cody-rhodes.md">` in `<head>`, and each `.md` file ends with a `Related` list of
sibling `.md` URLs so a crawler walks the whole graph in Markdown without ever touching HTML. The
`robots.txt` already exists; add an explicit allow for `.md` and reference the mirror in `llms.txt`.

**VERIFY:** confirm the production host serves arbitrary `.md` with the correct MIME type. If the CDN
forces `text/plain`, that still works for ingestion.

---

## Pillar 2 — `llms.txt` and `llms-full.txt`, rebuilt

The current `/llms.txt` is stale. It still names the site "MAT," points at `matwrestling.com`, and
lists five sections. It needs to become a real map to the whole database in the format LLMs read.

**Routes:**
- `/llms.txt` — the curated index. Rename to Wrestle Lore, fix the domain, and expand from five links
  to a sectioned map: Wrestlers, Matches, Rivalries, Promotions, Events, Moments, plus the new
  answer hubs from Pillar 3 and the Ask surface from Pillar 5. Every link points at the `.md` twin,
  not the HTML.
- `/llms-full.txt` — **new.** A single concatenated Markdown document containing the summary block of
  every entity on the site, generated at build time. This is the "hand the model the whole book"
  file that Perplexity and Claude retrieval favor for small-to-mid corpora. At roughly 250 entities
  with a 60-to-100 word summary each, this is a comfortable single file.

**Why it wins.** `llms.txt` is becoming the `robots.txt` of the answer-engine era. Being early and
thorough with a clean, correctly-branded map is a durable citation advantage while competitors like
Cagematch still ship HTML-only.

**Buildability.** Pure static, generated by one script that walks the entity dicts. No backend.

**VERIFY:** the rename to Wrestle Lore and the final production domain must be locked before this
ships, or the file will teach models the wrong name. Flag to the base rename workflow (Requirement 8).

---

## Pillar 3 — Answer Pages: pages built to be the featured snippet

These are new page types whose entire job is to win a specific query and get lifted into an AI answer
or a Google featured snippet. Each opens with a 40-to-60 word direct answer in a bordered
"answer block," then supports it with a table, then the deep content, then FAQ schema. Answer first,
evidence second, rabbit hole third.

### 3a. "Best of" and superlative pages — `/best/{topic}/`
Concrete routes, each targeting a real search:
- `/best/five-star-matches/` (every match rated near the ceiling, ranked, with the rating source
  labeled editorial vs cited)
- `/best/matches-2026/`
- `/best/wrestlemania-matches/`
- `/best/womens-matches/`
- `/best/wcw-matches/`

**Why it wins.** "Best [X] matches" is one of the highest-volume evergreen wrestling query families
and the exact shape AI Overviews answer with a ranked list. Ship these as real ranked pages with
`ItemList` schema so the model can lift the ordering, not just the prose. Pairs with the leaderboards
in `D-community-gamification.md`, but those are engagement surfaces; these are query-targeted answer
surfaces with schema tuned for extraction.

### 3b. Comparison answer pages — `/compare/{a}-vs-{b}/`
The interactive comparator in `B-interactive-tools.md` owns the tool. Spec E's contribution is that
each generated comparison must be a **crawlable, answer-shaped static page**, not only a JS view. It
opens with a one-sentence verdict-style summary ("Cody Rhodes and Roman Reigns have met at multiple
WrestleManias; here is the head-to-head record and title history"), a comparison table, then FAQ
schema answering "who has more championships," "who won their WrestleMania match," and similar. This
is the format that wins "X vs Y" queries, which are pure snippet bait.
**VERIFY:** every head-to-head result stated as fact.

### 3c. Definition and "who/what/when" pages — `/what-is/{term}/` and `/who-is/{slug}/`
Short, single-question pages for the literal questions fans and models ask:
- `/what-is/a-five-star-match/`
- `/what-is/kayfabe/`
- `/what-is/the-bloodline/`
- `/who-is/the-most-decorated-wwe-hall-of-famer/` (answer: Ric Flair, two-time inductee, per
  `00-content-data-research.md`)

**Why it wins.** These map one-to-one to the "People also ask" boxes and to short factual prompts.
They are cheap to author, they cross-link into the deep pages, and the glossary overlaps the Lore
terms in `A-new-content-types.md` so the work is shared. Each carries `DefinedTerm` or `FAQPage`
schema.

### 3d. Ranked list hubs — `/rankings/` expansion
The `/rankings/` directory already exists. Extend it with query-shaped ranked pages that each answer
a superlative question with `ItemList` schema and a visible methodology link, so an AI engine citing
the ranking also inherits the credibility of the stated method.

**Buildability of Pillar 3.** All static, all generated from existing front-matter. No backend.

---

## Pillar 4 — Structured-data futures: declare Wrestle Lore a dataset

The site ships good per-page schema already. The next tier makes the whole site legible to machines
as a *database*, not a collection of pages.

### 4a. `Dataset` and `DataCatalog` schema — `/data/`
A new `/data/` hub that describes each entity collection as a `Dataset` (name, description, license,
`distribution` pointing at the `.md` mirror and any JSON export), wrapped in a `DataCatalog`. This is
the schema Google Dataset Search and research-grade retrieval look for, and almost no wrestling site
ships it. It signals "this is a structured, citable source," which is exactly the trust signal answer
engines weight.

### 4b. Sharpen per-type schema
- Wrestlers: keep `Person`, add `sameAs` arrays pointing at Wikipedia, Wikidata, and official
  promotion profiles for every wrestler. `sameAs` is how a model resolves "the Cody Rhodes on
  Wrestle Lore" to the canonical entity in its knowledge graph, which is what earns the citation.
  **VERIFY** each external URL.
- Matches: the `Review` and `AggregateRating` are live; add `SportsEvent` context and `about` links
  so the match resolves to its event and its participants as entities.
- Promotions: upgrade `Organization` to `SportsOrganization` with `foundingDate`, `sport`, and
  `subOrganization` for brands (Raw, SmackDown, NXT).
- Add `speakable` schema hints on the answer block of Pillar 3 pages so voice assistants can read the
  summary aloud verbatim.

### 4c. A machine-readable entity export — `/data/entities.json`
`B-interactive-tools.md` already needs an `entities.json` and `C` needs a `graph.json`. Spec E's ask
is to also publish them at a stable `/data/` path, documented in `llms.txt` and wrapped by the
`Dataset` schema above, so external tools and models can pull the whole corpus in one request. One
build artifact, three consumers (tools, graph, GEO).

**Buildability of Pillar 4.** Static JSON and JSON-LD, generated from the same dicts. No backend.

---

## Pillar 5 — "Ask the Database": the on-site answer surface

**Route:** `/ask/` with pre-rendered answer pages at `/ask/{question-slug}/`.

**The buildable v1 (no backend).** `/ask/` is a static page listing the questions the database can
answer, grouped by entity type, each linking to a pre-rendered `/ask/{slug}/` answer page. Those
answer pages ARE the Pillar 3 answer pages under a question-phrased URL. A vanilla-JS filter box on
`/ask/` lets a visitor type and narrow the visible question list (client-side match against the
static index, no storage, fully crawlable because every answer already has its own URL). This gives
fans the feel of querying a database and gives crawlers a hub that maps every question the site
answers to a citable page. It is honest: nothing is generated live, every answer is a real authored
page with a source.

**The v2 (BACKEND).** A genuine natural-language "ask" box that runs retrieval over
`/data/entities.json` and returns a cited answer. This needs a serverless function or an edge worker
(the deferred Supabase and Vercel tooling in this environment could host it). Keep it retrieval-only
over the site's own verified data so it never fabricates. Flag clearly: this is the one backend
feature in Spec E, and the static v1 captures most of the GEO value without it.

**Why it wins.** An `/ask/` hub is a concentrated map of answerable questions, which is precisely
what an answer engine wants to find and cite. It also reads to a WWE hiring manager as a product
vision, not a page dump. And the v1 requires zero new infrastructure.

**Cross-links.** `/ask/` links into `/best/`, `/compare/`, `/what-is/`, and every entity hub. Every
entity page gets an "Ask about {name}" link pointing at the relevant `/ask/{slug}/` cluster.

---

## Pillar 6 — Citation hygiene: make the facts safe to quote

Answer engines drop sources they cannot trust. Three cheap moves raise trust:
1. **Visible sourcing on every fact-dense page.** A "Sources" block with real links, matching the
   confidence-flag discipline already used in the research docs. Cited, not decorative.
2. **`dateModified` on every page and in JSON-LD.** Freshness is a ranking and citation signal.
   The build already knows the timestamp.
3. **Editorial-vs-community labeling on ratings.** Where a rating is editorial or drawn from
   Observer/Cagematch consensus, say so in the visible text and in the `Review` `author` field. A
   model that can attribute the rating will quote it; one that cannot will skip it.

**Buildability.** Pure static, mostly template additions. No backend.

---

## Ranked build order (highest GEO leverage first)

| # | Move | Route(s) | Backend? | Why first |
|---|------|----------|----------|-----------|
| 1 | Markdown mirror | `*.md` twins | No | Biggest ingestion win, near-free from existing dicts |
| 2 | Rebuild `llms.txt` + `llms-full.txt` | `/llms.txt`, `/llms-full.txt` | No | Fixes stale branding, maps the corpus for LLMs |
| 3 | "Best of" answer pages | `/best/{topic}/` | No | Highest-volume evergreen queries, ItemList snippet bait |
| 4 | `/ask/` hub v1 | `/ask/`, `/ask/{slug}/` | No | Concentrated citable question map, product story |
| 5 | Comparison answer pages | `/compare/{a}-vs-{b}/` | No | "X vs Y" snippet family, reuses B's comparator data |
| 6 | Dataset schema + `/data/` | `/data/`, `/data/entities.json` | No | Declares the site a structured source |
| 7 | `what-is` / `who-is` + `sameAs` | `/what-is/{term}/`, `/who-is/{slug}/` | No | People-also-ask capture, entity resolution |
| 8 | `/ask/` v2 live retrieval | `/ask/` | **BACKEND** | Product ceiling, not needed for GEO value |

---

## Anti-AI copy standard (enforced on every surface above)

Answer blocks lead with a specific noun and a number, never a throat-clear. No decorative arrows, no
em-dash separators, none of the banned cliche vocabulary. Every superlative ("best," "most
decorated") is backed by a visible criterion and a source link. Ratings are labeled editorial or
cited. Nothing states a head-to-head result, a title count, or a date that is not verified, and every
unverified claim carries a VERIFY flag until sourced. The voice stays plain and factual, because that
is exactly the register an answer engine lifts cleanly.
