# Wrestle Lore — BUILD PLAN (engineering / tech-lead #1)

Concrete, buildable plan for the static, no-build, crawlable revamp. Companion to
`10-MASTER-BRIEF.md` (the product/design source of truth). This document owns *how* it gets built:
the shell-injection architecture, generator evolution, search-index generation, the 169-page rename,
the NJPW + new category pages, and Core Web Vitals. Written 2026-07-26, verified against `/root/wwe/`.

Author: senior engineer / tech lead #1. On any product/copy/color decision, the master brief and its
source specs govern; this plan does not re-open them.

---

## 0. Ground-truth engineering audit (what we are actually building on)

I read the tree, the generators, the CSS/JS, and a sample of every page type. The site is **not** the
clean "one stylesheet, single-source nav, generated pages" system the prose implies. It is a set of
independently-authored HTML files with **divergent shells**. The revamp's hardest problem is not the new
pages; it is unifying 169 inconsistent existing pages without a runtime build. Findings:

| # | Finding | Evidence | Consequence for the plan |
|---|---|---|---|
| A1 | **Nav is forked into 3+ variants.** Home = 5-tab mega (`nav__menu`, `mega__link`, `data-cmdk-open`). Wrestler pages = a stale 4-link bar `Wrestlers/Events/Titles/Search` with **`/titles/` and `/search/` that 404**, footer "© 2025 MAT". Match/promotion/event/rivalry pages = a third 5–6 `nav__link` variant. | `index.html` head vs `wrestlers/roman-reigns/index.html` (nav emitted at `build_wrestlers_10a.py:449`) vs `matches/…`, `promotions/wwe/…`. | A single-source nav injector is the spine of the whole revamp (Phase 0). Nothing else is safe until every page shares one shell. |
| A2 | **Two live canonical domains.** `matdb.io` on ~400 page references (wrestler pages), `wrestlelore.com` on ~852 (everything else). | `grep` of `<link rel=canonical>` / OG URLs across `*.html`. | The rename is not just "MAT → Wrestle Lore" text. It must **collapse two domains to one** canonical host in canonicals, OG, hreflang, JSON-LD `@id`/`url`, sitemap, robots. |
| A3 | **No shared template layer.** Each of the 20 `build_wrestlers_*.py` (a/b pairs, batches 1–10, 40–92 KB each) hardcodes head + nav + footer as inline f-strings. `build_events_11.py`, `build_moments_12.py` do the same with different markup. | 20 files each contain a full `<header class="site-header">`. | Editing nav by hand across generators = 20+ edits and still leaves hand-authored pages untouched. We need injection *decoupled from generation*. |
| A4 | **Existing pages mix hand-authored and generated.** Not every page can be re-emitted from a generator without losing hand edits, and several generators predate current content. | PROJECT note "hand-authored + Python-generated"; generator footers say 2025. | **Do not "just regenerate everything."** Retrofit existing pages in place; reserve generators for NEW pages and for pages we can prove are 100% generated. This is the single biggest trap. |
| A5 | **Search index is the old flat schema** `MAT_SEARCH_INDEX=[{t,u,k}]`, 169 entries, hand-consistent with pages by luck, not by check. `js/search-index.js` is committed but shows 0 lines in `wc` (single long line). | `js/search-index.js` head; `js/nav.js` reads `window.MAT_SEARCH_INDEX`. | Need a generator that (a) emits the rich `WL_INDEX` schema, (b) is derived from the pages/data so it cannot drift, (c) **fails on any link 404**. Keep the `MAT_SEARCH_INDEX` shim one release. |
| A6 | **`/wrestlers/` index renders 41 of 89.** Master brief confirms. Persona/alias/executive pages exist as real dirs (`mean-mark-callous`, `diesel`, `vince-mcmahon`, …) and are in the index today. | Brief §0; 90 dirs in `/wrestlers/`. | The 41→89 rebuild must apply the six-axis taxonomy AND the exclusion rules (aliases off-wall, in ⌘K). |
| A7 | **CSS is one 892-line file; JS is 4 small files** (`main.js` 143, `enhance.js` 129, `nav.js` 92 = the ⌘K palette, `search-index.js` data). No framework, no bundler. | `css/site.css`, `js/`. | Good. Additive-only CSS (brief §3) and progressive-enhancement JS keep CWV strong. Do not introduce a bundler. |

**Headline:** treat this as a **retrofit + finish-out**, not a greenfield build. Phase 0 exists to pay
down the shell/rename/domain debt so Phases 1–2 build on one consistent substrate.

---

## 1. Core architecture decision: the shell stitcher (single-source nav, no runtime build)

The constraint "static, no build step, crawlable (nav links in raw HTML)" and the reality "169 pages
with 3 forked navs, no shared template" are reconciled by **one author-time post-processor** that owns
the shared chrome. This is the keystone of the whole plan.

### 1.1 Mechanism — marker-delimited regions rewritten in place

Introduce `build/apply_shell.py` (idempotent, re-runnable) plus a `partials/` directory holding the
**single source** of each shared region:

```
partials/
  head-common.html     # charset, viewport, font <link>, /css/site.css, theme-color, the JS-class script
  nav.html             # the 7-tab mega-nav (D1), brand lockup "Wrestle Lore" + WL monogram, ⌘K pill (no Join pill, D2)
  cmdk.html            # the #cmdk palette dialog markup (v2: type-scope tabs + facet chips)
  footer.html          # renamed footer + HOF/Media/NJPW links + ambient "Insider" join line (D2/L0)
build/apply_shell.py   # stitches partials into every *.html between markers
build/wl_config.py     # single source of constants: DOMAIN, BRAND, tab list, promotion accents, VERIFY flags
```

Every page carries HTML comment markers; the stitcher replaces **only** the region between them, leaving
page-unique `<title>`, meta description, per-page JSON-LD, and `<main>` untouched:

```html
<!--WL:HEAD-->            ... single-source head-common ...      <!--/WL:HEAD-->
<!--WL:NAV-->             ... single-source 7-tab mega-nav ...   <!--/WL:NAV-->
<!--WL:CMDK-->            ... single-source ⌘K dialog ...        <!--/WL:CMDK-->
<!--WL:FOOTER-->          ... single-source footer ...           <!--/WL:FOOTER-->
```

Why this design:
- **Crawlable:** the stitched output is literal `<a href>` in the delivered `.html`. No JS rendering of
  nav. Works JS-off. Ships to any static host unchanged.
- **No runtime build:** stitching happens once at author time (like the generators already do). The
  deployed artifact is plain HTML. `apply_shell.py` is a maintenance tool, not a server.
- **Single source of truth:** nav/footer/head live in one file each. Change once, run `apply_shell.py`,
  all 169+ pages update. This is exactly the meganav-guard "fixed 7-tab instrument, edit the source not
  the page" discipline.
- **Idempotent + safe on hand-authored pages:** it edits only between markers, so hand-written `<main>`
  content is never at risk (answers trap A4). Pages missing markers are reported, not silently skipped.

### 1.2 One-time retrofit to install markers

The 169 existing pages do not have markers yet. `apply_shell.py --install` runs once in a mode that
finds each page's existing `<header …>…</header>` (and old footer, and the head region up to
`</head>`) by a small set of known-variant patterns (the 3 nav forks from A1), replaces each with the
marker pair + fresh partial, and writes a report of any page whose shell it could not confidently locate
(hand-fix those few). After install, all pages have markers and every later run is the fast marker path.

Guardrails: run under `git`, commit before install, diff the result. `apply_shell.py` never touches
anything outside markers, and prints a per-page before/after byte count so an accidental `<main>` deletion
is obvious in review.

### 1.3 Generators emit markers, not chrome

Retire the inline head/nav/footer f-strings in every generator; replace with the four marker pairs
(empty or with a `<!--WL:NAV-->` placeholder). Generators then only own `<title>`, per-page meta, per-page
JSON-LD, and `<main>`. `apply_shell.py` fills the chrome after generation. Net effect: **nav lives in
exactly one file** regardless of whether a page is generated or hand-authored.

---

## 2. Data architecture: front-matter → derived artifacts (single source for facets, search, graph)

Today the six-axis taxonomy, the search index, and the engagement graph would each drift independently.
Fix by making them all **derived from one per-entity data source**, checked at author time.

### 2.1 Per-entity front-matter

Each wrestler/match/event/etc. gets a small YAML/JSON front-matter record (either a sidecar
`*.meta.json` next to the page, or a central `data/entities/` set — recommend central for easy
whole-catalog scans). Fields per the taxonomy (brief §2.2) and engagement schema (brief §6):

```
slug, title, type, status, gender, promo[], era[], div[], badge[], alias, role,
related[], people[], rivalries[], matches[], allies[], accolades[], participants[],
event, rematchOf, series, year, streaming[], facts[]
```

Bootstrapping the 89 wrestlers: extract what exists from the pages (nickname/era already render), then
apply the tag map from research doc 00 §5. Budget this as real work (§6 effort), not a script freebie —
the axis tags are editorial.

### 2.2 Three derived build steps (all fail-closed)

```
build/gen_search_index.py   -> js/search-index.js   (window.WL_INDEX + WL_GAP_HINTS + MAT shim)
build/gen_graph.py          -> data/graph.json      (referrer + keep-going + trophy-case source)
build/gen_hubs.py           -> /wrestlers/{current,legends,women,...}/ card lists + ItemList JSON-LD
```

Each reads front-matter, and each runs the **link-existence check**: every `u` / related URL must resolve
to a real directory with an `index.html` on disk, or the step exits non-zero (brief §4.3, §10.2 "nothing
ships as a 404"). `gap:true` entities are excluded from `WL_INDEX` and pushed to `WL_GAP_HINTS`.

### 2.3 A single `build/build_all.py` orchestrator + `build/check_links.py`

One command runs generators → `apply_shell.py` → the three derived steps → link check → a report. This
is the "build" (author-time only). CI/pre-commit runs `check_links.py` (crawl every `<a href>` that is
site-internal, assert 200/exists) and a shell-consistency check (every page has all four markers, one
nav variant hash). Zero-404 is a gate, not a hope.

---

## 3. New pages: how each is built

All new pages are **generated** (data-driven) so they inherit markers and stay consistent. Card markup
is one shared Python helper `render_tile(entity)` (emits the badge grammar of brief §3.3) reused by
every hub, so a card looks identical on the home wall, a facet hub, and a nav panel.

| Page(s) | Builder | Source | Notes / traps |
|---|---|---|---|
| `/promotions/njpw/` (req 5) | new `build/gen_promotions.py` (also rebuilds the 5 existing promo pages to brand-card layout + `#roster/#events/#streaming/#history` anchors) | front-matter + streaming table (00 §1) | `--c-njpw:#d81f26` stays `VERIFY`; white rising-sun overlay + 1px top rule differentiate from WWE (D3). AJ Styles crossover hero here + on home. **No AJ retirement claim.** |
| `/promotions/` brand-card hub (req 4) | same generator | 6 brand cards (WWE/NJPW/TNA/WCW/ECW/NXT) | Text streaming chips only, US vs Intl labeled. **Do not render AEW card until `/promotions/aew/` exists** (else 404 from the card link). |
| `/wrestlers/` rebuild 41→89 (req 2) | `gen_hubs.py` + `render_tile` | front-matter, six axes | Apply exclusions: aliases off-wall/in-⌘K, `vince-mcmahon` executive-only, Sami Zayn stays a wrestler. Faceted bar: Tier-1 = `<a href>`, Tier-2 = `<button>`. |
| `/wrestlers/current/`, `/legends/`, `/women/` (req 2, Wave 1) | `gen_hubs.py` | filter front-matter by axis | Each is a real directory (Tier-1), `ItemList` JSON-LD, in sitemap, body class `hub--{axis}` recolors accent. |
| `/wrestlers/men/`, `/eras/*` (Wave 2) | `gen_hubs.py` | axis filter | `men` may be hash-only fallback if thin; eras Attitude+Modern first. |
| `/hall-of-fame/` (req 6, Wave 1) | new `build/gen_hof.py` | HOF data (00): Ric Flair 2×, last-5 classes 2021–25, Two-Time Club | `.theme-hof` gold. Two-Time solo years render in `.chip--verify` until confirmed; **do not print unverified years as fact**. GAP inductees = non-link tiles. |
| `/media/` + `/media/chris-van-vliet/` (req 7, Wave 1) | new `build/gen_media.py` | media roster (00 §, all `VERIFY` except CVV = HIGH) | `.theme-media` purple. **Media tab stays hidden until `/media/` + CVV page exist** (else the tab links a 404). Proposed roster tiles are non-link until each page ships. Explicit "Sami Zayn is a wrestler" note. |
| `/events/2026/` (Wave 2), `/events/summerslam/`, `/events/survivor-series/` (Wave 3) | extend `build_events_11.py` | existing event data | Add series/year/promotion facets to `/events/` master. |
| Missing profiles (HOF: Heyman, Muta, Bischoff, RVD, McCool; NJPW: Omega, Ospreay; media roster) | reuse wrestler generator path (see §4) | research | Each `VERIFY` cleared before its chip becomes a link. |
| Home page 12-block rebuild (§5 brief) | `build/gen_home.py` (replaces the hand-authored `index.html` body) | hubs + rails + FAQ | New JSON-LD: Organization, WebSite+SearchAction, FAQPage, ItemList (five-star rail). No fabricated AggregateRating. Replace the fake "12,840 / 38%" stats with real catalog counts. |

---

## 4. Evolving the Python generators (the 20-file problem)

The 20 `build_wrestlers_*.py` are a liability: duplicated shells, batch-numbered, 40–92 KB each. Two
moves, in order:

1. **Decouple chrome now (Phase 0, cheap, high value).** Replace every inline head/nav/footer f-string
   in all generators with the four markers. This alone kills the fork and lets `apply_shell.py` own the
   nav. It does **not** require rewriting the generators' data logic.

2. **Consolidate to one data-driven generator later (Phase 3, optional, higher risk).** Fold the 20
   batch scripts into a single `build/gen_wrestler.py` that loops the front-matter records and emits
   `<main>` from templates. Benefit: new profiles are a data edit, not a new 45 KB script. **Trap A4:**
   several existing wrestler pages contain hand edits; the consolidated generator must be validated to
   reproduce current `<main>` byte-for-byte on a sample before we let it overwrite, or it must be used
   **only for new profiles** and pages flagged fully-generated. Do not mass-regenerate the 89 to "clean
   up" — that risks silently reverting hand work. If parity can't be proven cheaply, keep the batch
   scripts frozen and only add `gen_wrestler.py` for net-new profiles.

`render_tile()` and the marker partials are shared by both old and new generators, so consistency does
not depend on the consolidation ever finishing.

---

## 5. The rename + domain unification (169 pages)

This is mechanical but has sharp edges. Do it as a scripted pass, `build/rename_to_wrestle_lore.py`,
reviewed as a single diff, **not** hand edits.

Ordered substitutions (specific, to avoid over-matching):
1. **Domain first (A2):** pick the canonical host once in `wl_config.py` (e.g. `wrestlelore.com` —
   `VERIFY` the actual registered domain before ship). Rewrite `matdb.io` → host and
   `wrestlelore.com` → host in `<link rel=canonical>`, `<link rel=alternate hreflang>`, OG `url`/
   `og:image`, twitter, JSON-LD `@id`/`url`/`sameAs`, `sitemap.xml`, `robots.txt`, `llms.txt`.
2. **Brand string:** `MAT — Pro Wrestling Database` / `MAT` brand lockup / footer "MAT Wrestling
   Database" → "Wrestle Lore". Be surgical: the token `MAT` also appears as the acronym in body copy and
   FAQ answers ("MAT (Match · Athlete · Timeline)…"); rewrite those to the new name/backronym, don't
   blind-replace the 3 letters (they occur inside words). Match on the known phrases, not `\bMAT\b` alone.
3. **JS global:** `MAT_SEARCH_INDEX` → `WL_INDEX` in `js/search-index.js`, `js/nav.js`, and any inline
   reference; add the one-release shim `window.MAT_SEARCH_INDEX = window.WL_INDEX;` at the tail of
   `search-index.js`.
4. **Copy landmines:** the ⌘K empty-state copy, the membership page name, the OG images (filenames may
   embed "mat"), the `assets/` filenames.

Because the shell (title suffix "| MAT", footer, nav brand) is being moved into partials in Phase 0, most
brand-string occurrences collapse to **one edit in `partials/`**; the rename script then only has to
handle the per-page `<title>`, per-page meta description, and per-page JSON-LD that live outside markers.
Sequence Phase-0 step 1 (install shell) *before* the rename so the rename surface shrinks from 169 pages
to (partials + per-page heads).

Post-rename gate: `grep` for residual `MAT`, `matdb.io`, `matwrestling`, `2025 MAT` returns only
intended hits (the shim, historical changelog). Add these to `check_links.py`'s assertions.

---

## 6. Phased build plan with effort estimates

Estimates are ideal engineering-days for one senior engineer; taxonomy tagging and copy are the real cost
centers, not the code. "Trap" = the thing most likely to blow the estimate.

### Phase 0 — Substrate: shell, rename, domain (unblocks everything). ~4–5 d
- 0.1 Build `partials/`, `build/wl_config.py`, `build/apply_shell.py` (marker path + `--install`). **1.5 d**
- 0.2 One-time `--install` retrofit on 169 pages; hand-fix the pages it can't auto-locate; commit + diff. **1 d**
  - *Trap:* the 3 nav forks (A1) plus any one-off pages mean the installer needs several match patterns;
    budget the long tail of "could not locate shell" pages.
- 0.3 Author the 7-tab mega-nav partial (D1), footer (D2), `cmdk.html` shell, head-common. **0.5 d**
- 0.4 `rename_to_wrestle_lore.py` + domain unification + `WL_INDEX` global + shim; review as one diff. **1 d**
  - *Trap:* the `MAT` acronym inside words / FAQ backronym; over-broad replace corrupts copy.
- 0.5 Append brief §3 tokens + `.theme-*`/`[data-promo]` scopes + badge/chip/rail/keepgoing/brandcard
  CSS to `css/site.css` (additive; retire `.nav__cta`). **0.5 d**

**Exit gate:** every page has 4 markers + identical nav hash; zero `/titles/`, `/search/` 404s; one
canonical host; brand = Wrestle Lore everywhere; CSS tokens present; site renders JS-off.

### Phase 1 — Required requirement pages (reqs 2,4,5,6,7). ~6–8 d
- 1.1 Front-matter for 89 wrestlers with six-axis tags + exclusions (A6). **2 d** *(editorial, the tax.)*
- 1.2 `render_tile()` + `gen_hubs.py`; rebuild `/wrestlers/` 41→89 + faceted bar; extend `js/main.js`
  filter (AND across axes, hash state, no storage). **1.5 d**
- 1.3 `/wrestlers/current/`, `/legends/`, `/women/` hubs (Tier-1, ItemList). **0.5 d**
- 1.4 `gen_promotions.py`: `/promotions/njpw/` + AJ crossover hero; rebuild `/promotions/` brand-card hub
  + 5 existing promo pages to anchored brand-card layout w/ streaming chips. **1.5 d**
  - *Trap:* streaming facts + NJPW hex are `VERIFY`; render `.chip--verify`, don't assert.
- 1.5 `gen_hof.py` → `/hall-of-fame/` (Ric Flair 2×, last-5, Two-Time Club w/ `VERIFY` years). **0.5 d**
- 1.6 `gen_media.py` → `/media/` + `/media/chris-van-vliet/`; only then un-hide the Media tab in the nav
  partial (until then the tab is absent, never a 404). **1 d**

**Exit gate:** all seven tabs resolve to real indexes; NJPW live; brand cards show streaming; HOF + 3
facet hubs + media hero live; link check green.

### Phase 2 — Home, engagement, search. ~5–6 d
- 2.1 `gen_home.py` 12-block home (§5); real scale counts; FAQPage/ItemList JSON-LD; kill fake stats. **1.5 d**
- 2.2 `gen_graph.py` → `data/graph.json`; wire the engagement stack (FAQ → rails → came-from → completion
  → keep-going → session trail) into entity templates via a shared `render_engagement()` helper. **2 d**
  - *Trap:* rails render only with ≥4 valid items; gaps render non-linked, never 404 — enforce in helper.
- 2.3 `gen_search_index.py` → `WL_INDEX` rich schema + `WL_GAP_HINTS`; upgrade `js/nav.js` to ⌘K v2
  (type-scope tabs + facet chips; blank+facets = browse; in-memory recents only). **1.5 d**
- 2.4 Conversion layers L0–L5 (§7); rebuild `/membership/` (rename, real stats, NJPW selector, no
  arrows, "What do Insiders get?" FAQ). **1 d**

**Exit gate:** home = 12 blocks; every entity page ends in keep-going; ⌘K v2 faceted; no storage written
(verify devtools Application tab); conversion layers present, none gate a crawlable fact.

### Phase 3 — Depth + remaining chips + generator consolidation. ~4–6 d
- `/promotions/aew/`, `/events/2026/`, era hubs (Attitude, Modern), SummerSlam + Survivor Series series
  hubs. **2 d**
- Missing profiles (HOF: Heyman/Muta/Bischoff/RVD/McCool; NJPW: Omega/Ospreay; media roster) — each
  `VERIFY` cleared before its chip links. **2 d** *(mostly research/copy)*
- Optional `gen_wrestler.py` consolidation (§4.2), only if byte-parity proven. **1–2 d, deferrable**

### Phase 4 — Verify + ship. ~2 d
- Clear/flag every §10.1 VERIFY item; run `check_links.py` (zero 404); confirm scale counts equal real
  page counts; anti-AI copy pass (covercapy standard: no decorative arrows, no em-dash separators, no
  banned words); validate all JSON-LD; check WCAG AA chip pairings; confirm no browser storage; Lighthouse
  CWV pass on home + a wrestler + an event page.

**Total: ~21–27 engineering-days.** Phase 0 is the long pole for *risk*, Phase 1 for *volume*.

---

## 7. Performance / Core Web Vitals plan

The static, no-framework, one-CSS-file architecture is already CWV-friendly. Protect it:

- **LCP:** hero is CSS-gradient + web-display font, no hero image to download — good. **Self-host the
  three fonts** (Anton/Oswald/Inter) under `/assets/fonts/` with `font-display:swap` and `preload` only
  the two above-the-fold weights, instead of the render-blocking Google Fonts `@import`/`<link>` used
  today (two `preconnect`s + a blocking stylesheet is the current LCP tax). Subset to Latin (+ the few
  glyphs used). This is the single biggest CWV win and belongs in Phase 0's head-common partial.
- **CLS:** reserve aspect-ratio boxes on every `.tile__media` and brand card (they're gradient tiles, so
  `aspect-ratio` is free and zero-shift). Nav is sticky, fixed height (70px) — no reflow. Any future real
  images get explicit width/height.
- **INP:** all JS is progressive-enhancement and event-delegated; keep it that way. ⌘K palette filters an
  in-memory array (89+ small entries) — fine. Facet filter uses `hidden`/class toggles, not DOM rebuilds.
  Do not add a framework or hydration.
- **Payload:** `css/site.css` (~one file) stays a single request; additive tokens add <2 KB. `WL_INDEX`
  grows from 169 to ~200 entries with a richer schema — keep it a static `.js` (cacheable), gzip ~ a few
  KB. Defer `js/search-index.js` and `js/nav.js` (`defer` attr); nav works without them (raw `<a>`).
- **Crawl/GEO budget:** the `<a>`-graph doubling as the internal-link graph means many links per page;
  keep nav panels in-DOM but visually collapsed (already the plan) so crawlers get them without JS. Ship
  `sitemap.xml` regenerated by `build_all.py`, `llms.txt` updated with the new sections, per-page JSON-LD.
- **Caching:** long-cache `/css/`, `/js/`, `/assets/` with content-hashed filenames if the host allows;
  HTML short-cache. No service worker (adds storage; brief forbids browser storage — a cache API is a gray
  area, skip it).

---

## 8. Risks & traps (ranked)

1. **Regenerating over hand-authored pages (A4).** Highest-impact data-loss risk. Mitigation: markers +
   `apply_shell.py` touch only chrome; never mass-regenerate `<main>`; consolidation gated on byte-parity.
2. **Shell installer mislocating a page's header/footer (0.2).** Mitigation: run under git, per-page
   byte-delta report, hand-fix the long tail, commit before/after separately.
3. **Rename over-matching the `MAT` acronym inside words/backronym.** Mitigation: phrase-based
   substitutions, not `\bMAT\b`; post-rename grep gate.
4. **Shipping a 404 from a card/tab/chip** (AEW card, Media tab, GAP inductee, facet chip). Mitigation:
   `check_links.py` fails the build; tabs/cards conditional on target existence in the generator.
5. **Asserting unverified facts** (NJPW hex, AJ retirement, Two-Time years, streaming hosts). Mitigation:
   `.chip--verify` + `VERIFY` registry in `wl_config.py`; nothing prints as fact until cleared.
6. **Two domains leaking post-rename** (mixed canonicals → SEO dilution). Mitigation: single host in
   config, grep gate, sitemap/robots regenerated from config.
7. **CSS regression from "additive-only" not being additive.** Mitigation: no existing hex changes;
   `--accent` defaults to gold so existing rules render identically; visual diff key pages.
8. **Nav growing past 7 tabs** under future pressure. Mitigation: enforce the fixed-7 instrument in the
   nav partial + a check that counts top-level `<a>` in `partials/nav.html`.

---

## 9. Ten-line summary + first three build steps

1. This is a **retrofit**, not greenfield: 169 pages carry 3 forked navs, a dead `/titles//search/` bar
   on wrestler pages, two live domains (`matdb.io` + `wrestlelore.com`), and 20 generators each
   hardcoding their own shell.
2. Keystone architecture: a **marker-based shell stitcher** (`build/apply_shell.py` + `partials/`) gives
   single-source nav/footer/head as raw crawlable HTML with no runtime build, safe on hand-authored pages.
3. Make facets, search, and the engagement graph **derive from per-entity front-matter**, with a
   link-existence check that fails the build on any 404.
4. New pages (NJPW, brand-card hub, HOF, facet hubs, media, home) are all **generated** and share one
   `render_tile()` so a card looks identical everywhere.
5. The rename is scripted (`rename_to_wrestle_lore.py`), collapses two domains to one canonical host, and
   is sequenced **after** shell-install so its surface shrinks from 169 pages to partials + per-page heads.
6. Consolidate the 20 wrestler generators only later, only for new profiles unless byte-parity is proven
   — never mass-regenerate over hand edits.
7. CWV: self-host + subset the fonts (biggest LCP win), reserve `aspect-ratio` on tiles for zero CLS, keep
   all JS deferred progressive-enhancement, no framework, single CSS file.
8. Phasing: **0** substrate (shell/rename/domain/tokens) → **1** required pages (NJPW, brand cards, HOF,
   facet hubs, media) → **2** home/engagement/search → **3** depth → **4** verify + zero-404 ship.
9. Effort ≈ **21–27 engineering-days**; taxonomy tagging (89 wrestlers) and copy are the real cost
   centers, not the code; top risks are data-loss from regeneration and the `MAT` acronym rename.
10. Everything ships behind two hard gates: **zero internal 404s** (`check_links.py`) and **nothing
    asserted as fact until its `VERIFY` flag clears**.

**Recommended first three build steps (do these in order):**
1. **Build `partials/` + `build/apply_shell.py` + `build/wl_config.py`; run `--install` across all 169
   pages** to replace every forked nav/footer with marker regions fed by one 7-tab mega-nav source
   (fixes A1/A3, kills the dead `/titles//search/` bar). Commit before and after; diff.
2. **Run `rename_to_wrestle_lore.py`: unify `matdb.io` + `wrestlelore.com` to one canonical host and
   `MAT` → Wrestle Lore** (brand, titles, OG, hreflang, JSON-LD, sitemap, robots, llms.txt), rename
   `MAT_SEARCH_INDEX` → `WL_INDEX` with a one-release shim; then grep-gate for residual `MAT`/old domains.
3. **Append the brief §3 color tokens + `.theme-*`/`[data-promo]` scopes + badge/chip/rail/keepgoing/
   brandcard CSS to `css/site.css` (additive, `--accent` defaults to gold), self-host + subset the three
   fonts in head-common, and stand up `build/check_links.py`** so every later step ships behind a
   zero-404 gate.
