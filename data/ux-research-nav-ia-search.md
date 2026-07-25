# Navigation, Information Architecture & Search/Findability — UX Research for MAT

**Prepared for:** MAT ("Match · Athlete · Timeline") — pro-wrestling database + membership-growth engine
**Scope:** mega-nav, IA/taxonomy for a large entity database, breadcrumbs, on-site search UX, faceted filtering & sorting, internal-linking / related content, pagination vs infinite scroll, and the findability failure modes to avoid.
**Method:** evidence-based synthesis from Nielsen Norman Group, Baymard Institute, Smashing Magazine, plus how leading database/reference sites (Sherdog, Tapology, IMDb, Wikipedia, Letterboxd, Cagematch) solve the same problems.
**Date:** 2026-07-25

---

## 0. Current MAT state (what this report is grounded in)

Read directly from the repo so every recommendation maps to real code and routes:

- **Mega-nav** (`index.html`, `header.site-header > nav.nav`): a fixed 7-item bar — **Wrestlers** (wide mega panel `.mega--wide`, 3 columns: By Promotion / All / Featured), **Matches** (mega panel: Explore / Editors' Picks), **Rivalries**, **Relationships**, **Rankings**, **中文**, and a **Join MAT Insider** CTA (`.nav__cta`). Panels open on hover; `aria-haspopup`/`aria-expanded` are present; mobile uses `.nav__toggle` (hamburger). PROJECT.md codifies the rule: *"the mega-nav is a fixed instrument… New content routes into existing dropdowns/hubs, never widens the top bar."*
- **Breadcrumbs** (`.crumbs` nav + `BreadcrumbList` JSON-LD): present on index/section pages, starts with Home, current page rendered as **plain text (not a link)** — already correct.
- **On-site "search"** (`js/main.js`): client-side live filter. An `input[data-filter]` filters `[data-search]` cards by `data-name` + `data-tags`; `[data-promo]` buttons filter by promotion; a `#roster-count` counter updates. **No global site search, no autocomplete, no zero-results/empty state, no sort control, no multi-facet combining, no URL state.**
- **Matches index** (`/matches/`): cards carry a `.rating` (MAT stars) and are ordered by era; the copy says "sortable by our rating" but **no sort control exists**.
- **Related content** (`.related-links`): flat, hand-curated anchor lists on match pages, wrestler pages (Rivalries + Related blocks), and section pages; wrestler profiles also use relationship `.chip`s.
- **Constraints** (PROJECT.md): static hand-authored HTML + one CSS system + vanilla JS, **no build step, no browser storage** (localStorage/sessionStorage forbidden — so persist UI state in the **URL**, not storage), mobile-first at 360px, tap targets ≥44px, WCAG AA, dark "arena" theme.
- **Scale:** ~40 wrestlers, 30 matches, plus rivalries/relationships/promotions — 100+ interlinked entity pages and growing.

The good news: MAT already follows several best practices (fixed nav discipline, breadcrumbs with schema, non-linked current crumb, mobile-first, URL-friendly slugs). The gaps are concentrated in **search depth, faceting/sorting, findability recovery, and systematizing related-content**.

---

## 1. Mega-nav: best practices & pitfalls

### 1.1 Group into scannable, labeled columns — never a wall of links
- **Principle:** A mega menu's advantage is that it shows structure. Break choices into distinct panels with clear subheadings; arrange items in **vertical columns** (people scan top-to-bottom), left-justified for scannability. Avoid content-free decorative images; only use imagery that illustrates an actual option.
- **Evidence:** NN/g, *Mega Menus Gone Wrong* — the top failures are "the organizing principle is difficult to discover," failing to group long lists, and adding visual fluff. ([nngroup.com](https://www.nngroup.com/articles/mega-menus-gone-wrong/))
- **Apply to MAT:** The **Wrestlers** panel already does this well (By Promotion / All / Featured columns with `<b>` label + `<small>` descriptor). Keep the pattern. When the roster grows, do **not** add a 4th column of raw names — add an **"By Division"** (Heavyweight / Tag / Women's / Cruiserweight) and **"By Era"** (Attitude / Ruthless Aggression / PG / Modern) grouping so the panel still expresses taxonomy, not inventory. The **Matches** panel is currently thin (2 columns); give it parallel structure: *Explore* (All, Top-rated 5★, By era, By promotion) and *Editors' Picks* — so both entity panels feel like the same instrument.

### 1.2 Do not grow the bar — route depth into panels/hubs
- **Principle:** Top-level nav items compete for attention; every added tab dilutes the rest and worsens mobile. Depth belongs inside panels and hub pages, not in more top-level tabs.
- **Evidence:** NN/g repeatedly finds overloaded top navigation harms findability; the recommended structure is a small stable top level with breadth expressed in the panel. Reinforced by MAT's own PROJECT.md rule.
- **Apply to MAT:** Enforce the 7-tab ceiling. Future sections (e.g. Promotions, Methodology, About, Waitlist) should surface **inside** the relevant mega panel or footer, or as a hub sub-menu — never as a new bar item. Consider whether **Relationships** and **Rivalries** should collapse under a single **"Storylines"** panel (with Rivalries / Relationships / Rankings columns) to free a slot and strengthen the "relationship graph" positioning — this is a taxonomy decision to validate with tree-testing (§2.5).

### 1.3 Intent-delay on hover; but treat click/touch as first-class
- **Principle:** Hover mega menus must tolerate diagonal mouse travel (an "intent" delay before closing) or they snap shut and frustrate users. On touch there is no hover, so the parent must be reachable AND the panel openable — a common pitfall is a hover-only panel whose parent link navigates away on the first tap, making children unreachable.
- **Evidence:** NN/g, *Mega Menus Gone Wrong* (timing/closing behavior) and *Mega Menus Work Well* body of work; touch-target guidance (≥1cm) from NN/g breadcrumb/mobile research. ([nngroup.com](https://www.nngroup.com/articles/mega-menus-gone-wrong/))
- **Apply to MAT:** Add a small close-delay (~150–300ms) to `.mega` hover so users can move into the panel. Because each parent (`/wrestlers/`, `/matches/`) is *also* a real destination, keep the current mobile pattern where the hamburger `.nav__toggle` expands panels via tap (don't rely on hover). Verify keyboard support: Tab into the parent, arrow/Tab through `.mega__link`s, `Esc` closes — wire `aria-expanded` to reflect actual open state (it's currently static in markup).

### 1.4 Accessibility of the panel
- **Principle:** Mega panels must be operable by keyboard and screen reader: focus order follows visual order, `Esc` closes and returns focus, state is announced.
- **Evidence:** W3C WAI-ARIA Authoring Practices (disclosure/menu patterns); NN/g accessibility guidance.
- **Apply to MAT:** The `aria-haspopup`/`aria-expanded` attributes exist but appear hardcoded. Toggle `aria-expanded` in JS on open/close for both desktop hover and mobile tap; ensure `.mega` is not `display:none` in a way that traps focus. This also protects the WCAG AA target in PROJECT.md §3.

### 1.5 Reference-site patterns worth stealing
- **IMDb / Letterboxd:** persistent **global search box in the header** is the primary wayfinding tool, not the mega menu — the menu is for browse, search is for find. **MAT lacks a global search entirely** (see §3). This is the single biggest nav gap.
- **Wikipedia:** minimal chrome, search-first, and dense in-body links carry navigation (see §6). Validates MAT's "relationship graph" thesis.
- **Sherdog/Tapology:** entity type is the top-level split (Fighters / Events / Organizations) — exactly MAT's Wrestlers / Matches / Rivalries split. Keep it.

---

## 2. Information architecture & taxonomy for a large entity database

### 2.1 Model the domain as entity types with consistent, parallel templates
- **Principle:** For reference/database sites, IA is driven by **entity types** and their relationships, not by marketing sections. Each type gets a consistent index → detail template so users learn one mental model and reuse it everywhere.
- **Evidence:** NN/g, *Information Architecture: Study Guide* (organize around users' mental models and content relationships). ([nngroup.com](https://www.nngroup.com/articles/ia-study-guide/)) Mirrors Sherdog's fighter/event/org model that MAT explicitly emulates.
- **Apply to MAT:** MAT's five entity types are sound: **Wrestler** (`/wrestlers/{slug}/`), **Match** (`/matches/{slug}/`), **Rivalry** (`/rivalries/{slug}/`), **Relationship** (`/relationships/`), **Promotion** (`/promotions/{slug}/`). Keep each `index` page as the "browse this type" hub and each detail page structurally identical within its type (already largely true). Document the template contract so new pages don't drift.

### 2.2 Give each entity multiple orthogonal facets (the taxonomy)
- **Principle:** A large entity set needs several independent classification axes so users can slice it their way. Don't force a single hierarchy onto content that is naturally multi-dimensional.
- **Evidence:** NN/g faceted-search research: faceted classification lets users combine independent attributes; single rigid trees fail large catalogs. ([nngroup.com](https://www.nngroup.com/reports/ecommerce-ux-search-including-faceted-search/))
- **Apply to MAT:** Formalize these facets as consistent `data-*` attributes on cards (extending the existing `data-promo` / `data-tags` convention) so both filtering (§5) and internal linking (§6) can use them:
  - **Wrestlers:** promotion(s) (`data-promo`, exists), era, division/weight class, alignment (face/heel), championship status, nationality, active/retired.
  - **Matches:** promotion, year/era, event, match type (Hell in a Cell, TLC, Ladder, Iron Man…), MAT rating (`--rating`, exists), title match (y/n).
  - **Rivalries:** promotion, era, participants.
  This is also the GEO/SEO win — these facets become citable, crawlable filtered listing pages.

### 2.3 Prefer flat + faceted over deep hierarchy
- **Principle:** Deep trees hurt findability (users get lost, "where am I / how do I get back"); a broad, shallow structure with faceted browse scales better for hundreds of items.
- **Evidence:** NN/g IA study guide and findability testing work favor broad-shallow for large content sets. ([nngroup.com](https://www.nngroup.com/articles/ia-study-guide/))
- **Apply to MAT:** Max depth is already sensible (`/type/{slug}/` = 2 levels). Resist creating `/wrestlers/wwe/attitude-era/heels/…` sub-trees; instead expose those slices as **filtered views of the flat index** (`/wrestlers/?promo=wwe&era=attitude`). Keep promotion hubs (`/promotions/wwe/`) as curated editorial landing pages, not as the only path to a wrestler.

### 2.4 Label with the user's vocabulary, not internal jargon
- **Principle:** Category labels must match users' words. Ambiguous labels are a top cause of "I couldn't find it even though it was there."
- **Evidence:** NN/g, *Low Findability and Discoverability* names unclear category names / poor classification as primary IA root causes. ([nngroup.com](https://www.nngroup.com/articles/navigation-ia-tests/))
- **Apply to MAT:** "Rivalries" vs "Feuds" vs "Storylines," and "Relationships" (real-life) vs "Rivalries" (on-screen) are exactly the kind of pair users conflate. Add a one-line descriptor under each in the mega panel and on the index hero ("Rivalries = on-screen feuds; Relationships = real-life connections") to disambiguate.

### 2.5 Validate the taxonomy with card sorting + tree testing
- **Principle:** Don't guess categories — test them. **Card sorting** (open/closed) surfaces users' mental models and whether your labels convey groupings; **tree testing** measures whether people can actually find things in your structure by browsing (task success, directness, first-click) before any UI is built.
- **Evidence:** NN/g, *Card Sorting vs. Tree Testing* and *Tree Testing* — card sorting builds/validates the IA, tree testing evaluates it cheaply and iteratively. ([nngroup.com](https://www.nngroup.com/articles/card-sorting-tree-testing-differences/), [nngroup.com](https://www.nngroup.com/articles/tree-testing/))
- **Apply to MAT:** Cheap validation before build-out: run a **closed card sort** ("which section would you look in for X?") on the Rivalries/Relationships/Rankings/Promotions labels, and a **tree test** of the proposed sitemap (5–8 tasks like "find the highest-rated Undertaker match," "find who trained CM Punk"). This is the highest-leverage, lowest-cost IA de-risking step and reads as senior UX rigor in the portfolio.

---

## 3. On-site search UX (the biggest current gap)

MAT currently has **no global search** — only per-index client-side filtering. For a 100+ page database this is the top findability failure mode (§8). Reference sites (IMDb, Letterboxd, Wikipedia, Sherdog) all lead with a persistent search box.

### 3.1 Provide a persistent, prominent global search box
- **Principle:** On database/reference sites, search is the primary find tool; it must be visible on every page (in the header), not buried behind an icon on desktop.
- **Evidence:** NN/g, *Low Findability* (search is one of the two ways users find things; when browse fails, search must catch them). ([nngroup.com](https://www.nngroup.com/articles/navigation-ia-tests/)) Baymard on-site search corpus. ([baymard.com](https://baymard.com/blog/collections/on-site-search))
- **Apply to MAT:** Add a search field to `.site-header` across all templates (icon-that-expands is acceptable on 360px mobile, but the input should be one tap away). MAT already declares a `SearchAction` in the WebSite JSON-LD pointing at `/wrestlers/?q={query}` — **generalize this to a real site-wide results page** `/search/?q=` covering all entity types, and update the schema target. Because there's no server and no build step, implement it as a **static JSON index** (`/search-index.json` listing every wrestler/match/rivalry with name, aliases/tags, type, url) loaded by vanilla JS — reuse the existing `data-name`/`data-tags` vocabulary as the corpus.

### 3.2 Autocomplete: ~10 suggestions, scoped, with matched text highlighted
- **Principle:** Keep the suggestion list manageable (~10 desktop, 4–8 mobile) to avoid choice paralysis; **highlight the predicted portion** of each suggestion; **visually distinguish** entity suggestions (a specific wrestler/match) from category-scope suggestions ("in Matches"); highlight the active row and support arrow-key + Enter navigation; give mobile rows generous spacing/hit areas to prevent mistaps; keep the dropdown visually clean (avoid noise).
- **Evidence:** Baymard, *9 UX Best Practice Design Patterns for Autocomplete Suggestions* (only 19% get it right): limit count, style category scope differently, highlight suggested text, highlight active suggestion + keyboard nav, adequate mobile spacing. ([baymard.com](https://baymard.com/blog/autocomplete-design))
- **Apply to MAT:** Autocomplete should return **entity results, not just query strings** — a wrestler thumbnail + name, a match with its star rating — so a user can jump straight to `/wrestlers/cm-punk/` from the dropdown. Group by type ("Wrestlers / Matches / Rivalries") with the type label styled distinctly. Bold the matched substring. Cap at 8–10. This turns search into a fast wayfinding tool AND an engagement driver (more entity clicks = more depth = closer to the waitlist CTA).

### 3.3 Search must tolerate aliases, nicknames, and typos
- **Principle:** Reference-domain search fails when it only matches the canonical title. Wrestlers have ring names, real names, and nicknames; users type any of them.
- **Evidence:** Baymard on-site search research: symptom/synonym/alias mismatch is a leading cause of false "no results." ([baymard.com](https://baymard.com/blog/collections/on-site-search))
- **Apply to MAT:** The `data-tags` fields are already rich alias corpora (e.g. "hbk the heartbreak kid the showstopper mr wrestlemania"). Index those tags in the search JSON so "HBK," "Deadman," "Tribal Chief," "送葬者" all resolve. Add light typo tolerance (substring + simple Levenshtein or a curated synonym map) so "undertaker"/"undertkaer" both work.

### 3.4 Let users search within the current context
- **Principle:** Users often want to "search within this category" rather than site-wide.
- **Evidence:** Baymard, *Allow Users to 'Search Within' Their Current Category* — 94% of sites don't, and users expect scoped search. ([baymard.com](https://baymard.com/blog/search-within-current-category))
- **Apply to MAT:** The existing per-index `[data-filter]` boxes already provide scoped search on `/wrestlers/` and `/matches/` — good. Make the placeholder explicit ("Search within wrestlers…") and, when a global search results page exists, offer a "Search all of MAT for '…'" escape hatch from the scoped box.

---

## 4. Findability failure modes to avoid — the "no results" / empty state

### 4.1 Never show a dead-end zero-results page
- **Principle:** A blank "no results" page is a top abandonment trigger. Recovery paths beat apologies: (1) related categories, (2) alternative/relaxed queries run behind the scenes with previews, (3) recommendations/recently viewed, (4) support/contact, (5) popular/bestseller content. Generic "check your spelling" tips alone are largely ignored.
- **Evidence:** Baymard, *5 Proven UX Strategies for "No Results" Pages* — ~50% of sites strand users; NN/g, *3 Guidelines for Search Engine "No Results" Pages*. ([baymard.com](https://baymard.com/blog/no-results-page), [nngroup.com](https://www.nngroup.com/articles/search-no-results-serp/))
- **Apply to MAT:** MAT's filter currently just hides all cards on no match → an invisible dead end. Add an explicit empty state to both the scoped filters and the future `/search/` page:
  - Message that restates the query ("No wrestlers match 'goldbrg'").
  - **Relaxed suggestions** ("Did you mean **Goldberg**?") using the alias/typo map.
  - **Fallbacks that keep them in-funnel:** featured wrestlers, Top-rated 5★ matches (`/rankings/`), Editors' Picks, and a link to browse all (`/wrestlers/`, `/matches/`).
  - A soft CTA ("Can't find a match? Join the MAT Insider waitlist and request it →" `/waitlist/`) — turns a failure into a capture, directly serving the membership-growth objective.

### 4.2 The specific failure modes MAT must guard against
- No global search (§3.1) → users who don't know the exact index page are stuck. **Highest priority.**
- Silent empty states (§4.1) → the filter hiding everything with no message.
- Alias blindness (§3.3) → "Deadman" returning nothing.
- Single-facet filtering (§5) → can't ask "5★ WWE matches from the Attitude Era."
- No sort control despite claiming sortability (§5.4) → expectation mismatch on `/matches/`.
- Related-links that are hand-curated and inconsistent (§6) → dead-ends at the bottom of detail pages.
- Filter/sort state lost on Back (§5.5, §7) → pogo-sticking users lose their place.
- Deep hero images pushing breadcrumbs/filters below the fold on mobile (§6.4).

---

## 5. Faceted filtering & sorting UX

### 5.1 Show result counts next to each filter value
- **Principle:** Displaying the count of matching items per option (e.g. "WCW (12)") is one of the single highest-impact filter improvements — it sets expectations and prevents zero-result selections.
- **Evidence:** Baymard, *Ecommerce Filter UI* — per-value counts described as one of the highest-impact filter upgrades. ([baymard.com](https://baymard.com/learn/ecommerce-filter-ui))
- **Apply to MAT:** Add counts to the `[data-promo]` buttons and any new facet controls ("WWE (28) · WCW (9) · ECW (5)…"). Trivial to compute client-side from the `data-promo` attributes already on cards.

### 5.2 Allow multi-select and combine facets (AND across types, OR within)
- **Principle:** Use checkboxes (multi-select), OR within a facet ("WWE or WCW"), AND across facets ("WWE AND Attitude Era AND 5★"). Radio-button single-select cripples large-catalog browse.
- **Evidence:** Baymard, *Ecommerce Filter UI* — multi-select with OR-within/AND-across is the expected logic. ([baymard.com](https://baymard.com/learn/ecommerce-filter-ui))
- **Apply to MAT:** Today `[data-promo]` is single-active-promo (`data-active-promo`). Upgrade the filter engine in `js/main.js` to combine multiple facets: promotion(s) + era + division for wrestlers; promotion(s) + era + match-type + min-rating for matches. Keep the free-text `[data-filter]` box as an additional AND term (already the case).

### 5.3 Display applied filters as removable chips, plus "Clear all"
- **Principle:** Show an overview of currently applied filters above the results, each individually removable, with a global clear. 42% of sites get applied-filter display wrong.
- **Evidence:** Baymard, *How to Design 'Applied Filters'* / *Filter UI*. ([baymard.com](https://baymard.com/learn/ecommerce-filter-ui))
- **Apply to MAT:** Reuse the existing `.chip` component as removable applied-filter chips above the roster/match grid (e.g. "WWE ✕  ·  5★ ✕  ·  Clear all"). Keep the `#roster-count` live count next to it ("Showing 14 of 40").

### 5.4 Separate SORT from FILTER, and actually provide it
- **Principle:** Sorting (reorder the same set) and filtering (reduce the set) are different tasks and need distinct controls. Common sorts: relevance, rating, date, A–Z.
- **Evidence:** NN/g ecommerce search & faceted-search report treats sort and filter as distinct control groups. ([nngroup.com](https://www.nngroup.com/reports/ecommerce-ux-search-including-faceted-search/))
- **Apply to MAT:** `/matches/` claims "sortable by our rating" but has no control. Add a `<select>` sort: **MAT rating (high→low)**, **Year (new→old / old→new)**, **A–Z**. For `/wrestlers/`: A–Z, promotion, era. Implement client-side (reorder DOM nodes) — no build step needed. This closes a live expectation gap on the matches index.

### 5.5 Desktop live-updates; mobile drawer with "Show N results"; persist in URL
- **Principle:** On desktop, update results instantly and keep filters persistently visible (left sidebar). On mobile, use a full-screen drawer/bottom-sheet with an explicit **"Show N results"** apply button. Reflect state in URL query params so Back and sharing work.
- **Evidence:** Baymard, *Ecommerce Filter UI* (real-time desktop, apply-button mobile, persist via URL). ([baymard.com](https://baymard.com/learn/ecommerce-filter-ui))
- **Apply to MAT:** Desktop: the current instant-filter behavior is right — add a sticky/persistent filter rail instead of the inline button row when the grid is long. Mobile: put filters behind a "Filters" button opening a sheet with a gold "Show N results" CTA (fits the arena theme, ≥44px tap target). **Crucially, encode state in the URL** (`/matches/?promo=wwe&min=5&sort=rating`) — this satisfies both the "persist on Back" rule AND MAT's no-browser-storage constraint (URL is the only allowed state store), and makes filtered views crawlable/citable for SEO/GEO.

---

## 6. Internal linking / "related content" UX (the depth & engagement engine)

This is MAT's stated differentiator ("the relationship graph") and its main lever for session depth → waitlist exposure. Systematize it.

### 6.1 Rich, contextual in-body links beat bottom-of-page link lists
- **Principle:** Contextual links placed within the narrative (Wikipedia-style) are followed far more than a generic "related" block, because they carry meaning at the point of interest. In-page/anchor links also aid orientation on long pages.
- **Evidence:** NN/g, *In-Page Links for Content Navigation*. ([nngroup.com](https://www.nngroup.com/articles/in-page-links-content-navigation/)) Wikipedia/IMDb "connections" model.
- **Apply to MAT:** Wrestler bios already do this well (inline links to `/wrestlers/samoa-joe/`, `/rivalries/cm-punk-pipebomb/`). Extend the pattern to every match story and rivalry timeline — link each named wrestler, event, and title on first mention. This is also the GEO play (dense entity binding for LLMs).

### 6.2 Make `.related-links` systematic and reciprocal, not hand-curated
- **Principle:** Related-content modules drive depth only when they are consistent, relevant, and bidirectional (A links to B *and* B links to A). Ad-hoc curation creates gaps and dead-ends and is unmaintainable at 100+ pages.
- **Evidence:** NN/g findability work (dead-ends and orphan pages are a discoverability failure); topical-cluster internal-linking practice. ([nngroup.com](https://www.nngroup.com/articles/navigation-ia-tests/))
- **Apply to MAT:** Drive `.related-links` from the facet data (§2.2) rather than by hand: on a match page, auto-surface *other matches sharing a participant*, *other matches from the same event/era*, *the rivalry this match belongs to*, and *both wrestlers' profiles*. On a wrestler page: *top-rated matches featuring them*, *their rivalries*, *their relationships*, *promotion hub*. Enforce **reciprocity** (a link-integrity check in CI — PROJECT.md already targets "100% internal-link integrity"). This removes dead-ends and multiplies crawlable link density.

### 6.3 Label related modules by relationship type
- **Principle:** "Related" is vague; typed modules ("Rivalries," "Wrestlers in this match," "More from the Attitude Era," "You may also like") set expectations and get more clicks.
- **Evidence:** NN/g content/navigation labeling guidance; matches the current wrestler-page pattern (separate "Rivalries" and "Related" blocks).
- **Apply to MAT:** Keep distinct, typed blocks rather than one generic list. Use the `.chip` component for people/entities and `.related-links` for cross-type navigation, so the relationship graph reads visually.

### 6.4 Keep the module above the fold-of-interest and don't bury orientation
- **Principle:** Related content and breadcrumbs lose value if pushed far down (esp. below large hero images on mobile).
- **Evidence:** Smashing, *Designing Effective Breadcrumbs* (hero images pushing wayfinding down cause abandonment). ([smashingmagazine.com](https://www.smashingmagazine.com/2022/04/breadcrumbs-ux-design/))
- **Apply to MAT:** On mobile match pages, ensure the embedded 16:9 video facade doesn't push the "Wrestlers in this match" links and next-match suggestions so far down they're never seen. Consider a compact "Up next / Related" strip nearer the top for long pages.

---

## 7. Pagination vs infinite scroll vs load-more

### 7.1 Match the pattern to task type and catalog size
- **Principle:** Infinite scroll suits **exploratory, homogeneous, goal-less** browsing (feeds). It hurts **goal-oriented** tasks: users can't refind items, lose scroll position on Back, can't reach the footer, and it degrades SEO and low-bandwidth performance. Pagination suits large catalogs and comparison; **Load-More buttons** are the balanced default for small-to-medium content and mobile.
- **Evidence:** NN/g, *Infinite Scrolling: When to Use It* and *Alternatives to Pagination on Product-Listing Pages* (Show-More often best: footer access, user control, mobile data, normalized by Google mobile). ([nngroup.com](https://www.nngroup.com/articles/infinite-scrolling-tips/), [nngroup.com](https://www.nngroup.com/articles/alternatives-pagination-listing-pages/))
- **Apply to MAT:** MAT's tasks are **goal-oriented reference lookups**, and it depends on the **footer** (disclaimer, membership links) and on **SEO/GEO crawlability** — three strikes against infinite scroll. At current scale (~40 wrestlers, ~30 matches) **render all cards on one page** (fastest, most crawlable, footer reachable) and let client-side filter/sort do the narrowing. When any index exceeds ~50–100 items, switch to a **"Load more" button** (or paginated views with real `?page=` URLs), never infinite scroll.

### 7.2 Always show progress and totals
- **Principle:** Whatever the pattern, show "Viewing X of Y" and remaining count.
- **Evidence:** NN/g, *Alternatives to Pagination* (Lululemon "Viewing 40 of 333"). ([nngroup.com](https://www.nngroup.com/articles/alternatives-pagination-listing-pages/))
- **Apply to MAT:** The `#roster-count` element already exists — render it as "Showing 14 of 40 wrestlers," and pair it with the applied-filter chips (§5.3).

### 7.3 Preserve position/state across Back (pogo-sticking)
- **Principle:** Users click into a detail page then Back; preserve their scroll position and applied filters/sort.
- **Evidence:** NN/g, *Alternatives to Pagination* (support pogo-sticking; preserve scroll). ([nngroup.com](https://www.nngroup.com/articles/alternatives-pagination-listing-pages/))
- **Apply to MAT:** Encode filter/sort in the URL (§5.5) so Back restores the exact filtered view. With no-storage constraint, URL params + native anchor scroll restoration are the mechanism.

---

## 8. Breadcrumbs (mostly right — tighten these)

MAT already: starts trails at Home, renders the current page as non-linked text, and emits `BreadcrumbList` JSON-LD. Keep all of that. Refinements:

### 8.1 Location-based (hierarchy), supplementary to nav, current page not a link
- **Principle:** Breadcrumbs show site hierarchy (not session history), supplement (never replace) primary nav, include the current page as **non-clickable** and visually distinct, and only link to real ancestor pages. For polyhierarchies pick one canonical path.
- **Evidence:** NN/g, *Breadcrumbs: 11 Design Guidelines*. ([nngroup.com](https://www.nngroup.com/articles/breadcrumbs/))
- **Apply to MAT:** Detail pages should show the full trail: `Home › Wrestlers › CM Punk` and `Home › Matches › CM Punk vs Cena — MITB 2011`. A match belongs to both a rivalry and two wrestlers (polyhierarchy) — pick **one canonical parent** for the crumb (its section index, e.g. Matches), and expose the other relationships via `.related-links`/breadcrumb-style sibling links, not the trail. Add `aria-current="page"` to the final crumb (`.crumbs` currently uses plain `<li>` text — good, just add the ARIA).

### 8.2 Place above the H1, visible without scrolling; don't bury under heroes
- **Principle:** Put breadcrumbs directly above the page title, visible without scrolling; avoid disabled-looking or ambiguous styling that draws rage clicks.
- **Evidence:** Smashing, *Designing Effective Breadcrumbs*; NN/g guideline set. ([smashingmagazine.com](https://www.smashingmagazine.com/2022/04/breadcrumbs-ux-design/), [nngroup.com](https://www.nngroup.com/articles/breadcrumbs/))
- **Apply to MAT:** Ensure `.crumbs` sits above the H1 on every detail template and above any hero image on mobile.

### 8.3 Mobile: single line, no wrap, adequate tap targets
- **Principle:** Don't let breadcrumbs wrap to multiple lines on mobile; truncate ancestors (accordion/ellipsis that expands) rather than hiding; keep tap targets ≥~1cm.
- **Evidence:** NN/g mobile breadcrumb guidelines; Smashing accordion-truncation pattern. ([nngroup.com](https://www.nngroup.com/articles/breadcrumbs/), [smashingmagazine.com](https://www.smashingmagazine.com/2022/04/breadcrumbs-ux-design/))
- **Apply to MAT:** For long match titles at 360px, truncate the trail (`Home › Matches › CM Punk vs Cena…`) with the current page ellipsized, and keep links ≥44px per PROJECT.md.

### 8.4 Skip breadcrumbs where hierarchy is flat
- **Principle:** Don't show breadcrumbs on top-level/flat pages where they add nothing.
- **Evidence:** NN/g guideline #7. ([nngroup.com](https://www.nngroup.com/articles/breadcrumbs/))
- **Apply to MAT:** Fine to omit on the home page; keep on all `index` and detail pages (2 levels deep) where they aid wayfinding.

---

## 9. Prioritized action list for MAT

**P0 — findability foundation (do first):**
1. **Global search** with a static JSON index + header search box on every template; point the existing `SearchAction` schema at a real `/search/` results page (§3.1).
2. **Autocomplete** returning typed entity results (wrestler/match/rivalry), ~10 items, matched-text highlighted, alias/nickname aware via `data-tags` (§3.2–3.3).
3. **Zero-results / empty state** on both filters and `/search/`: relaxed suggestions + fallbacks + waitlist capture CTA (§4).

**P1 — browse depth:**
4. **Multi-facet filtering** (promotion + era + division/rating) with per-value counts, applied-filter chips, "Showing X of Y," and **URL-encoded state** (§5.1–5.5).
5. **Sort control** on `/matches/` (rating, year, A–Z) and `/wrestlers/` — closes the "sortable" claim gap (§5.4).
6. **Systematize `.related-links`** from facet data, enforce reciprocity + link-integrity check (§6.2).

**P2 — polish & validation:**
7. Mega-nav: hover intent-delay, live `aria-expanded`, keyboard/`Esc` support; give Matches panel parallel structure (§1.3–1.4, §1.1).
8. Breadcrumb `aria-current`, mobile truncation, canonical-parent rule for matches (§8).
9. Keep single-page render now; add **Load-more** (not infinite scroll) only past ~50–100 items (§7).
10. **Card-sort + tree-test** the taxonomy/labels (Rivalries vs Relationships vs Storylines) before further build-out (§2.4–2.5).

---

## Sources

- Nielsen Norman Group — [Mega Menus Gone Wrong](https://www.nngroup.com/articles/mega-menus-gone-wrong/)
- Nielsen Norman Group — [Breadcrumbs: 11 Design Guidelines for Desktop and Mobile](https://www.nngroup.com/articles/breadcrumbs/)
- Nielsen Norman Group — [Low Findability and Discoverability: Four Testing Methods](https://www.nngroup.com/articles/navigation-ia-tests/)
- Nielsen Norman Group — [Information Architecture: Study Guide](https://www.nngroup.com/articles/ia-study-guide/)
- Nielsen Norman Group — [Card Sorting vs. Tree Testing](https://www.nngroup.com/articles/card-sorting-tree-testing-differences/) · [Tree Testing](https://www.nngroup.com/articles/tree-testing/)
- Nielsen Norman Group — [In-Page Links for Content Navigation](https://www.nngroup.com/articles/in-page-links-content-navigation/)
- Nielsen Norman Group — [Infinite Scrolling: When to Use It, When to Avoid It](https://www.nngroup.com/articles/infinite-scrolling-tips/) · [Alternatives to Pagination on Product-Listing Pages](https://www.nngroup.com/articles/alternatives-pagination-listing-pages/)
- Nielsen Norman Group — [3 Guidelines for Search Engine "No Results" Pages](https://www.nngroup.com/articles/search-no-results-serp/) · [Ecommerce Search UX incl. Faceted Search (report)](https://www.nngroup.com/reports/ecommerce-ux-search-including-faceted-search/)
- Baymard Institute — [9 UX Best Practice Design Patterns for Autocomplete Suggestions](https://baymard.com/blog/autocomplete-design)
- Baymard Institute — [5 Proven UX Strategies for "No Results" Pages](https://baymard.com/blog/no-results-page)
- Baymard Institute — [Ecommerce Filter UI Best Practices](https://baymard.com/learn/ecommerce-filter-ui) · [On-Site Search UX collection](https://baymard.com/blog/collections/on-site-search) · [Search Within Current Category](https://baymard.com/blog/search-within-current-category)
- Smashing Magazine — [Designing Effective Breadcrumbs Navigation](https://www.smashingmagazine.com/2022/04/breadcrumbs-ux-design/)
- W3C WAI-ARIA Authoring Practices (menu/disclosure patterns)
- Reference-site IA patterns observed: Sherdog, Tapology, IMDb, Wikipedia, Letterboxd, Cagematch (entity-type navigation, search-first wayfinding, dense in-body linking)
