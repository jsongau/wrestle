# Wrestle Lore — SEO, GEO, Performance & Portfolio Positioning (Spec 12)

Owner: Senior engineer / tech lead #2 (SEO, GEO, performance, job-application positioning).
Date: 2026-07-26. Reads and depends on `10-MASTER-BRIEF.md`; does not override its decisions.
Scope: make Wrestle Lore the most *findable* wrestling site (classic SEO + AI answer-engine citation)
and the most *legible portfolio proof* for the WWE/TKO Membership-Growth role. This spec governs the
technical-SEO, structured-data, internal-link-graph, crawl, GEO, Core-Web-Vitals, and measurement
layers. It is additive to the visual/IA/copy specs and inherits every hard constraint (static, no build
step, crawlable raw `<a>`, one stylesheet, vanilla JS, no browser storage, no fabricated facts).

The organizing idea from the brief holds here: the retention graph, the internal-link graph, and the
funnel are one structure. SEO and GEO are that same `<a>` graph pointed at crawlers and answer engines.

---

## 0. Ground-truth audit (verified against `/root/wwe/` on 2026-07-26)

Before any new work, six existing defects will silently cap ranking. These are P0 because they affect
pages already live and are cheap to fix in Phase 0.

| # | Defect | Evidence | Impact | Fix |
|---|---|---|---|---|
| A0 | **Canonical domain mismatch.** Page `<link rel=canonical>` points to `matdb.io`; `sitemap.xml`, `robots.txt`, `llms.txt` use `matwrestling.com`. | `wrestlers/aj-styles/` canonical = `https://matdb.io/...`; sitemap loc = `https://matwrestling.com/...`. | Split signals; Google may index neither cleanly, dilutes every link. **Nothing else matters until one canonical host is chosen.** | Pick ONE production host (recommend `wrestlelore.com`, `VERIFY` availability). Global find/replace across all 169 pages + sitemap + robots + llms + JSON-LD `url`/`item`. |
| A1 | **Invalid JSON-LD (single-quoted keys/values).** FAQ `name` fields use `'...'` not `"..."`. | `wrestlers/aj-styles/`: `"name":'When did AJ Styles debut in WWE?'`. | Invalid JSON. Google/Perplexity/Bing silently drop the whole `@graph` node. FAQ + Person rich results lost site-wide. | Regenerate all JSON-LD through a serializer (Python `json.dumps`), never string templates. Validate every page in Phase 4. |
| A2 | **Fabricated `AggregateRating`.** 30 match pages carry `ratingCount:"9640"`, `reviewCount:"431"` etc. | `matches/undertaker-vs-hbk-wm25/`. | Directly violates the no-fabricated-stats constraint AND is a Google structured-data spam trigger (self-serving invented review counts). Manual-action risk. | **Remove `AggregateRating` entirely.** Keep a single first-party `Review`/`Rating` (the site's own star rating, `author` = Wrestle Lore) which is legitimate. See §2.3. |
| A3 | **Stale flat nav on sub-pages** links `/titles/` and `/search/`. | `wrestlers/aj-styles/` header. | If those paths 404, every one of 89+ profiles emits broken internal links; wastes crawl budget, drops PageRank into a hole. | Phase-0 nav propagation (brief step 3) already replaces this. Confirm zero links to non-existent `/titles/` `/search/`. |
| A4 | **Sitemap is incomplete.** 119 `<loc>` entries vs 169 HTML pages. | `grep -c` sitemap = 119; page count = 169. | ~50 pages (many wrestler profiles) are uncrawled/deprioritized. | Regenerate sitemap from the filesystem (§4.1) so count == live indexable pages exactly, every build. |
| A5 | **Only 2 of 4 moments carry `VideoObject`.** | `kane-debut...` and `mankind...` have it; `steve-austin-broken-neck-1997`, `triple-h-tears-his-quad-2001` do not. | Missed video rich-result eligibility and GEO video citations on the exact pages built to earn them. | Add `VideoObject` to all 4 (§2.4). |

Additional standing gaps (not defects, but ranking ceiling): render-blocking Google Fonts stylesheet on
all 106 checked pages; no OG/Twitter image (pure-CSS art means no shareable thumbnail); no
`ImageObject`/OG for social; `llms.txt` still says "MAT" and omits Promotions/HOF/Media/NJPW.

---

## 1. Technical-SEO foundation (per-page contract)

Every page ships this `<head>` contract. Codify it as a single template partial in the Python
generators so it cannot drift.

**Required, every page:**
- `<title>` — pattern per type (§1.1), <= 60 chars, primary entity first, brand suffix `| Wrestle Lore`.
- `<meta name="description">` — 140–160 chars, specific nouns, no banned marketing words, one concrete
  hook (a real stat/date), no truncation mid-word.
- `<link rel="canonical">` — self-referential, absolute, single production host, trailing slash, lower-case.
- `<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">`
  — `max-snippet:-1` and `max-video-preview:-1` explicitly authorize full snippets + video previews,
  which raises AI-answer citation eligibility.
- Open Graph: `og:title og:description og:type og:url og:site_name og:image og:image:alt og:locale`
  (+ `og:locale:alternate` for `zh_CN` on bilingual pages).
- Twitter: `twitter:card=summary_large_image twitter:title twitter:description twitter:image`.
- `hreflang` reciprocal pair (`en` <-> `zh-Hans` + `x-default`) on every page that has a `/zh/` twin;
  self-referential `hreflang` where no twin exists.
- Fonts: preconnect to `fonts.gstatic.com` (crossorigin) — see §5.

**Filter/hub crawl rules (from brief §2.1, restated for SEO):**
- Tier-1 hubs (`/wrestlers/current/`, `/legends/`, `/women/`, per-promotion, `/hall-of-fame/`, `/media/`,
  `/events/2026/`, series hubs) are canonical, indexable, in sitemap, carry `ItemList` (§2.5).
- Combined/Tier-2 state lives only in `location.hash` — inherently non-indexable, no action needed.
- `?q=` search results: `robots.txt` already disallows `/*?q=`; also emit `<meta robots="noindex,follow">`
  on any query-reflected view and `rel=canonical` to the clean index. Add `Disallow: /*#` is unneeded
  (fragments aren't crawled) — do NOT block hashes.
- The Media tab: while `/media/` is unbuilt, the tab is *hidden* (brief D1/§9), never a soft-404. No
  `noindex` placeholder page — absence, not a thin page.

### 1.1 Title & description patterns per type

| Type | Title pattern | Description hook |
|---|---|---|
| Wrestler | `{Name} — Career Record, Matches & Rivalries \| Wrestle Lore` | debut year + top promotion + one signature match, real. |
| Match | `{A} vs {B}, {Event} {Year} — {stars}-Star Match Review \| Wrestle Lore` | result + why-rated line, no invented crowd counts. |
| Event edition | `{Event} {Year} — Full Results, Card & Ratings \| Wrestle Lore` | date + venue + headline result. |
| Series hub | `{Series} — Every Edition, Results & Ratings \| Wrestle Lore` | count of editions catalogued. |
| Promotion | `{Promotion} — Roster, Events & Where to Watch \| Wrestle Lore` | 2026 streaming home (the answer-first hook). |
| Hall of Fame | `WWE Hall of Fame — Inductees, Classes & Records \| Wrestle Lore` | last class + Ric Flair 2x line. |
| Media | `Wrestling Media & Creators — Interviews & Analysts \| Wrestle Lore` | Chris Van Vliet + what the hub covers. |
| Facet hub | `{Facet} Wrestlers — {N} Profiles \| Wrestle Lore` | real N, the axis definition. |
| Moment | `{Moment} — What Happened & Video \| Wrestle Lore` | date + the incident in one clause. |

Titles are generated, never hand-typed, so the `| Wrestle Lore` suffix and length budget are enforced.

---

## 2. Structured data (JSON-LD) — the GEO backbone

Structured data is the single highest-leverage GEO tactic: answer engines lift entities and their
relations straight from `@graph`. Rule: **one `@graph` per page**, machine-serialized, every entity given
a stable `@id` (the canonical URL + fragment) so nodes cross-reference instead of duplicating. Cross-page
`@id` reuse (a wrestler's `@id` identical on their profile and inside a match's `competitor`) is what lets
an answer engine assemble the knowledge graph.

### 2.1 Site-wide nodes (on home, referenced by `@id` elsewhere)
- `Organization` `@id=/#org` — `name:"Wrestle Lore"`, `url`, `logo` (`ImageObject`), `sameAs` [social,
  `VERIFY` which exist], `foundingDate`. Reference from every page's publisher slot.
- `WebSite` `@id=/#website` — `SearchAction` `target:/wrestlers/?q={search_term_string}` (matches the
  real ⌘K/search route), `inLanguage:["en","zh-Hans"]`.

### 2.2 Per-type primary node

| Page | Primary `@type` | Key properties (real data only) |
|---|---|---|
| Wrestler | `Person` | `name, alternateName (ring names), birthDate, birthPlace, nationality, jobTitle, url, @id, sameAs (VERIFY), memberOf (Organization per promotion)`. NO fabricated `award` unless HOF/title is sourced. |
| Match | `Review` of `SportsEvent` | see §2.3. |
| Event edition | `SportsEvent` | `name, startDate, location (Place+PostalAddress, real venue), organizer (Organization @id), subEvent[] (each match as SportsEvent), offers` only if a real watch link. |
| Series hub | `ItemList` of editions | §2.5. |
| Promotion | `Organization` + `FAQPage` | `name, foundingDate, url, sameAs`; FAQ carries the streaming answer (§3). |
| Hall of Fame | `ItemList` (inductees) + `FAQPage` | Flair-2x + last-5-classes Q&A. |
| Media hub | `ItemList` (creators) | each item `Person` with `jobTitle:"Interviewer"` etc., `VERIFY` affiliations. |
| Moment | `VideoObject` | §2.4. |
| Facet hub | `CollectionPage` + `ItemList` | §2.5. |
| Rivalry | `SportsEvent` series or `CreativeWork` | link `about` -> the two `Person` `@id`s. |

### 2.3 Match reviews — fix the fabrication (A2)

Remove `AggregateRating` everywhere. Ship instead one legitimate first-party review:

```json
{"@type":"Review","@id":"{url}#review",
 "itemReviewed":{"@type":"SportsEvent","@id":"{url}#event","name":"{A} vs {B}, {Event} {Year}"},
 "author":{"@type":"Organization","@id":"/#org"},
 "reviewRating":{"@type":"Rating","ratingValue":"5","bestRating":"5","worstRating":"1"},
 "reviewBody":"{the real editorial review text}"}
```

This is honest (the star rating IS Wrestle Lore's own editorial rating, sourced from the methodology
page), it is Google-compliant (a single self-authored review, not invented aggregate counts), and it
still earns the review star treatment. Link the `Rating` origin to `/methodology/` in visible copy.

### 2.4 Video — the GEO multiplier for `/moments/`

Add `VideoObject` to all 4 moments (fix A5). Video is disproportionately cited by AI answer engines and
eligible for Google video rich results. Each needs: `name, description, thumbnailUrl (VERIFY a real
frame exists or omit), uploadDate, contentUrl OR embedUrl, duration (ISO 8601)`. If we do not host video
and only embed, use `embedUrl` and never invent a `duration`. Flag `VERIFY` any moment lacking a real
hosted/embedded video source; do not fabricate `contentUrl`.

### 2.5 Lists — every hub is an `ItemList`

Facet hubs, series hubs, HOF, media, rankings, and the home five-star rail carry `ItemList` with
`ItemListElement` -> `ListItem{position,url,name}` using each item's canonical `@id`. This is what makes a
hub answer "who are the current WWE women's wrestlers" as a ranked, linkable set. `numberOfItems` must
equal the real card count (ties to the honest-counts rule).

### 2.6 Breadcrumbs
Keep `BreadcrumbList` on every deep page (already present). Update the trail for new hierarchy:
`Home > Wrestlers > Legends > {Name}` where a facet hub is the true parent, `Home > Promotions > NJPW`,
`Home > Hall of Fame > {Class}`. Breadcrumbs both render the visible trail and feed the sitelink treatment.

---

## 3. GEO / AI-answer-engine citation strategy

GEO = being the source an LLM answer *quotes and links*. Tactics, in priority order:

1. **Answer-first blocks (the single biggest lever).** Every hub and showcase leads with a 40–60 word
   direct-answer paragraph in a `.answer-first` block, phrased as the answer to the page's head question,
   before any narrative. Answer engines extract the first self-contained factual paragraph. Home FAQ
   already plans four; extend the pattern to: promotion pages ("Where can I watch {promo} in 2026?"),
   HOF ("How many times is Ric Flair in the WWE Hall of Fame?" -> two), AJ Styles ("Which promotions has
   AJ Styles wrestled for?"), TNA ("Is TNA on Amazon?" -> library on Prime Video, live on AMC/AMC+, §8).
2. **`FAQPage` schema on every answer block** (already 164 pages). Each Q is a citable atom. Keep answers
   factual, dated, and self-contained (no "as mentioned above").
3. **Definitional clarity + entity consistency.** Use the exact same entity name string everywhere
   ("New Japan Pro-Wrestling (NJPW)" on first mention per page). Consistent naming raises entity
   confidence in the knowledge graph.
4. **`llms.txt` rebuild** (currently stale/MAT). Rewrite to: new brand, one-line site definition, the six
   promotions incl. NJPW, and a curated link list to the highest-value hubs (facet hubs, HOF, Media,
   promotions, methodology). `llms.txt` is the concierge for AI crawlers; keep it a hand-curated map of
   *canonical* pages, not everything.
5. **`robots.txt` already welcomes the AI crawlers** (GPTBot, OAI-SearchBot, PerplexityBot,
   Google-Extended, ClaudeBot, Bytespider) — good. Add `CCBot` (Common Crawl, feeds many models) and keep
   the `Sitemap:` line pointed at the ONE canonical host (fix A0 here too).
6. **Comparison & list content ranks in AI answers.** The rankings page, five-star club, "Two-Time Club",
   and streaming-comparison tables are exactly the shape answer engines lift. Format them as real HTML
   `<table>`/`<ol>` with captions, not just visual tiles, so they parse cleanly.
7. **Freshness signals for GEO.** Real `dateModified` in JSON-LD + visible "Updated {date}" where content
   genuinely changed; do not touch dates on unchanged pages (honesty + avoids freshness-spam pattern).
8. **Cite our own sources.** Methodology page names Wrestling Observer / Cagematch consensus; link to it
   from every rating. A site that shows its sources is more citable and matches the no-fabrication stance.

Measurement of GEO success (§7): track referrals from `chatgpt.com`, `perplexity.ai`, `gemini.google.com`,
`copilot.microsoft.com` in analytics, and periodically prompt those engines with the target questions to
see if Wrestle Lore is cited.

---

## 4. Crawl architecture, sitemap, internal-link graph

### 4.1 Sitemap (regenerate from filesystem, fix A4)
- Single script walks `/` for every `index.html`, emits `<loc>` for its directory URL. Count MUST equal
  indexable page count (exclude any `noindex`). Fail the build if a page exists but is missing, or a
  `<loc>` points to a non-existent dir (mirror the WL_INDEX link-existence check).
- `lastmod` from real git/file mtime, not "today".
- Keep the `xhtml:link` hreflang alternates for the `/zh/` pairs (already present on home).
- If page count crosses growth, split into a sitemap index (`sitemap.xml` -> `sitemap-wrestlers.xml`,
  `-events.xml`, etc.). At 169 not required yet; design the generator to shard at >1,000.
- No image sitemap needed while art is pure CSS (no indexable images). Revisit if real photos land
  (rights `VERIFY` — do not add wrestler photos without licensing).

### 4.2 Internal-link graph (the shared SEO/retention asset)
The brief's mandatory "Keep-going" block + themed rails on every entity page ARE the internal-link
structure. SEO requirements layered on top:
- **Every page reachable within 3 clicks of home** via raw `<a>` (hub -> spoke). The 7-tab nav + facet
  hubs guarantee this; verify with a crawl (§4.3).
- **Contextual descriptive anchor text**, never "click here"/"read more". Anchor = the target entity's
  name or the relation ("Rey Mysterio", "their WrestleMania 22 match"). This is a GEO signal too.
- **Bidirectional linking**: if match A links wrestler B, B's profile links match A (rails already do
  this from front-matter). No orphan entities.
- **Hub pages distribute authority**: facet hubs and promotion hubs link deep into the roster; the home
  links every hub. Flat, wide graph beats deep chains.
- **`/data/graph.json`** (brief §6) doubles as the link-graph source of truth; a QA step asserts every
  node has >= 2 inbound and >= 2 outbound links (no orphans, no dead ends), matching the "never
  dead-ends" retention rule.

### 4.3 Crawl QA (Phase 4 gate)
- Local crawler (wget/`linkchecker` or a Python `requests` walk over the static tree) asserting **zero
  404s** across all internal `<a href>` — this is the same fail-on-404 check the WL_INDEX build runs;
  run it against rendered HTML too.
- Assert every sitemap URL returns 200 and is self-canonical.
- Assert no page links to `/titles/` or `/search/` (A3 regression guard).
- Assert one host only appears in canonical/OG/JSON-LD (A0 regression guard).
- Orphan report from `graph.json`.

---

## 5. Core Web Vitals & performance

The site is static, no-build, one CSS file, vanilla JS, no images — an excellent CWV starting point. The
only real risks are fonts and CSS weight. Targets: LCP < 2.0s, INP < 200ms, CLS < 0.05, all at p75.

1. **Fonts (biggest lever).** Currently a render-blocking `fonts.googleapis.com/css2` stylesheet on every
   page.
   - Add `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>` (the stylesheet already
     preconnects to `fonts.googleapis.com`; the actual font files come from `gstatic`).
   - `display=swap` is already in the URL — keep it (prevents invisible-text FOIT; small CLS handled
     next).
   - **Recommend self-hosting** the three families (Anton, Oswald 400/600, Inter 400/500/600) as `woff2`
     under `/assets/fonts/` with `@font-face` + `font-display:swap` + `size-adjust`/`ascent-override` to
     kill the swap CLS. Removes a third-party connection and a render-blocking request — the single
     biggest LCP win available. `VERIFY` each font's license permits self-hosting (all three are OFL —
     yes, permitted).
   - Subset to Latin (+ Latin-ext) for en pages; the `/zh/` pages need a CJK face — do NOT ship a full
     CJK webfont (megabytes); use `font-display:swap` with system CJK stack fallback and `VERIFY` a
     subset approach for zh.
2. **CSS.** `site.css` is 68KB (uncompressed) and growing with §3 tokens/components. Keep it one file
   (HTTP/2, and the constraint). Ensure the server sends it gzip/brotli + a long `Cache-Control` +
   fingerprint the filename on change (`site.[hash].css`) so caching is aggressive without staleness.
   Inline the critical above-the-fold CSS in `<head>` only if LCP testing shows the external CSS is the
   blocker; otherwise the single cached file is fine.
3. **JS.** 4 small vanilla files (~28KB total). Load nav/search/enhance with `defer`. The ⌘K index
   (`search-index.js`) is 11KB and will grow to 89+ entries — keep it a separate deferred file, loaded
   only when the palette first opens (dynamic `import()` or lazy `<script>` injection) so it never blocks
   first paint. No framework, no hydration — INP is essentially free; just avoid long tasks in the
   filter-bar handler (debounce, operate on pre-parsed data attributes).
4. **CLS.** Reserve space for the poster tiles (aspect-ratio boxes, already CSS gradients so no image
   reflow). The font self-host + `size-adjust` removes the last CLS source. No layout-shifting
   ad/emb/ late-injected content.
5. **LCP element.** On home it is the hero H1 (Anton) — self-hosting Anton + preloading only the hero
   weight makes the LCP text paint immediately. Consider `<link rel="preload" as="font">` for the single
   hero font file only (over-preloading hurts).
6. **No render-blocking third parties.** No analytics that block (use a lightweight, async, cookieless
   analytic — §7 — respecting the no-storage constraint).
7. **HTTP headers (document for whoever hosts):** brotli, immutable long-cache on hashed assets,
   `Cache-Control: public, max-age=3600, stale-while-revalidate` on HTML, HTTP/2+, HSTS. These are host
   config, flagged for the deploy owner.

Verification: Lighthouse CI (mobile preset) on home + one of each template as a Phase-4 gate; PageSpeed
Insights field data once live.

---

## 6. Priced-in: how this all sequences with the brief's phases

SEO/GEO/perf work maps onto the brief's Phase 0–4 rather than adding a parallel track:

- **Phase 0 (system + rename):** fix A0 (one host), A1 (JSON-LD serializer), A2 (drop AggregateRating),
  A3 (nav), rebuild `llms.txt` + `robots.txt` host line, establish the `<head>` template partial (§1),
  self-host fonts (§5.1). These unblock everything and stop active bleeding.
- **Phase 1 (required pages):** each new hub/showcase ships with its §2 schema, §1.1 title/desc,
  answer-first block (§3), and `ItemList` from day one — never retrofit SEO.
- **Phase 2 (home + engagement + search):** wire `graph.json` orphan/inbound checks (§4.2); home carries
  Organization/WebSite/FAQPage/ItemList; ⌘K index deferred-loaded (§5.3).
- **Phase 3 (depth):** each new profile/hub enters sitemap + graph automatically via the generators.
- **Phase 4 (verify + ship):** crawl QA (§4.3), JSON-LD validation, Lighthouse gate, sitemap==pagecount
  assertion, GEO answer-question spot check. This IS the brief's Phase-4 gate, extended.

---

## 7. Measurement — what to instrument (and why it doubles as the portfolio proof)

Two audiences read the metrics: search/AI engines (covered above) and the WWE hiring manager (below).
Instrument, respecting the no-browser-storage constraint, with a **cookieless, no-localStorage** analytic
(e.g. server-log analysis, or a privacy-analytic in cookieless mode). Do not add tracking that writes
storage — it would violate the constraint and undercut the "we respect the reader" funnel thesis.

Funnel + growth metrics to capture (the Membership-Growth vocabulary, applied honestly):
- **Acquisition:** organic sessions by landing hub; AI-referral sessions (chatgpt/perplexity/gemini
  referrers) as a named channel — this is the GEO scoreboard.
- **Activation / engagement:** pages per session, rail click-through rate, Keep-going block CTR, scroll
  depth to the conversion layer, search (⌘K) usage rate. These prove the "rabbit hole" works.
- **Conversion:** membership-intent clicks by layer L0–L5 and by source hub; which intent moment converts
  best (the brief's "timing over volume" thesis). Since capture is real, measure real submit rate; do NOT
  invent a rate (kills the fabricated 38% permanently).
- **Retention proxy (no accounts yet):** returning-visitor rate via referrer + campaign, session-trail
  depth distribution.
- **SEO health:** indexed page count, hub rankings for target queries, rich-result coverage
  (Search Console), CWV field pass rate.

---

## 8. Streaming / verifiable facts this spec depends on (flag, do not invent)

The GEO answer-first blocks are only as good as their facts. Carry these from brief §8 / research 00 and
keep `VERIFY` until confirmed at publish; the answer-first paragraphs and FAQ schema must match exactly:
WWE (Raw=Netflix, SmackDown=USA Network, NXT=The CW, PLEs=ESPN US / Netflix intl); NJPW (NJPW World +
TrillerTV + TV Asahi Japan); **TNA (live AMC/AMC+, streaming TNA+, library Prime Video — the literal
answer to "is TNA on Amazon?")**; WCW/ECW (WWE archive on Netflix, US host `VERIFY`); AEW (TBS/TNT/HBO Max
+ AEW Plus, Wave 2). NJPW brand hex and AEW hex `VERIFY`. AJ Styles: no retirement claim. Two-Time Club
solo years `VERIFY` before printing. None of these ship as bare fact until cleared.

---

## 9. Portfolio positioning — what to show a WWE/TKO Membership-Growth hiring manager

The site is the artifact; this section says what to *point at* so a non-engineer manager reads it as
membership-growth competence, not just a fan site.

1. **A one-page "Growth case study" at `/about/` or a linked `/case-study/`** (crawlable, part of the
   site, not a PDF): the thesis (catalog depth -> retention -> intent-timed conversion), the funnel
   diagram L0–L5, and the honesty stance (why we removed fabricated stats — a growth leader who ships
   trustworthy numbers). This directly mirrors the JD: full-funnel ownership, lifecycle, honest
   instrumentation.
2. **Show the funnel, named in their language.** Label the conversion layers with membership-growth terms
   (acquisition -> activation -> conversion -> retention) so the manager maps it to their own funnel
   instantly. The "no loud nav CTA, convert on intent" decision is the headline growth insight — call it
   out explicitly.
3. **Show the SEO/GEO strategy as demand-gen.** A short section: "How people find Wrestle Lore" — organic
   search + AI answer engines as an owned acquisition channel. WWE's membership push lives on discovery;
   demonstrating GEO fluency (getting cited by ChatGPT/Perplexity) is a differentiated, current skill.
4. **Show measurement.** A lightweight, real metrics panel (or a mock clearly labeled "illustrative"
   using the §7 metric *names* with placeholder values marked as such — never present fake numbers as
   real). The competence shown is *what you'd measure and why*, per layer.
5. **Event-tied lifecycle.** Point at the L5 watch-along CTA on PPV pages + `/events/2026/` as proof of
   event-driven membership spikes — exactly WWE's PLE-night monetization rhythm.
6. **Internationalization foresight.** The `/zh/` edition + China GTM doc shows membership-growth thinking
   beyond the US market (WWE/TKO is global). Keep it truthful and flag the China-specific `VERIFY`s.
7. **Craft signals a manager notices without reading code:** fast load (send them a PageSpeed score),
   zero broken links, consistent design system, honest data. "This person ships polished, trustworthy
   product" is the meta-message.

Guardrail: every portfolio claim about traffic/conversion must be real or explicitly labeled
illustrative. A Membership-Growth candidate caught showing invented KPIs fails the exact competency being
tested. This is why A2 (fabricated AggregateRating) and the 38%/12,840 stats must go in Phase 0.

---

## 10. Acceptance checklist (Phase-4 gate, this spec's slice)

- [ ] One canonical host across all canonical/OG/JSON-LD/sitemap/robots/llms (A0).
- [ ] Every JSON-LD block valid JSON, machine-serialized, validates in Rich Results Test (A1).
- [ ] Zero `AggregateRating`; every match has one first-party `Review`/`Rating` (A2).
- [ ] Zero internal 404s; no links to `/titles/` `/search/`; every sitemap URL 200 + self-canonical (A3, §4.3).
- [ ] `sitemap.xml` count == indexable page count; real `lastmod` (A4, §4.1).
- [ ] All 4 moments carry valid `VideoObject` (A5).
- [ ] `<head>` contract present on all pages (title <=60, desc 140–160, canonical, robots, OG, Twitter, hreflang).
- [ ] Every Tier-1 hub carries `ItemList` with real `numberOfItems`; answer-first block present on hubs/showcases.
- [ ] `llms.txt` + `robots.txt` rebuilt (new brand, NJPW/HOF/Media, CCBot, one host).
- [ ] Fonts self-hosted (or preconnected) with `swap` + CLS override; Lighthouse mobile: LCP<2.0 INP<200 CLS<0.05.
- [ ] ⌘K index deferred-loaded; JS `defer`; no render-blocking third parties.
- [ ] No browser storage written (devtools Application tab) — analytics cookieless.
- [ ] Portfolio: `/case-study/` (or `/about/` section) live; no unlabeled fabricated KPI anywhere.
```
