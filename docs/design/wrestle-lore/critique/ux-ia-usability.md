# UX / IA / Usability Critique — Wrestle Lore

Senior UX/IA adversarial review. Scope: navigation, findability, cognitive load, information scent,
breadcrumbs, empty/zero/error states, and the drill path (tab → hub → profile). No praise. Every item
cites a real file/selector, gives the fix, states buildability on a static no-build crawlable site, and
names a researched source pattern.

Files reviewed: `/root/wwe/index.html`, `/root/wwe/css/site.css`, `/root/wwe/js/nav.js`,
`/root/wwe/js/main.js`, `/root/wwe/js/enhance.js` (grep), `/root/wwe/wrestlers/index.html`,
`/root/wwe/matches/index.html`, `/root/wwe/events/index.html`,
`/root/wwe/moments/mankind-hell-in-a-cell-fall-1998/index.html`, `/root/wwe/wrestlers/kane/index.html`,
and the site tree (`/root/wwe/*`). Cross-checked against the team's own spec
`docs/design/wrestle-lore/03-mega-nav.md`.

---

## TL;DR — the three that matter most

1. **The shipped nav contradicts your own spec and orphans every Phase 1 hub.** The bar is 5 tabs;
   `/hall-of-fame/`, `/current/`, `/legends/`, `/women/`, `/media/` exist on disk but are reachable
   from no primary-nav link on any core page. New content is invisible to humans navigating.
2. **The flagship findability feature (Cmd-K) is stale and can't find the new content.** The search
   index holds 0 of the new hubs and 89 of 94 wrestler profiles. Combined with a roster index frozen
   at 41 cards, roughly 53 profiles are reachable only by chance body links.
3. **Dead-ends everywhere at the bottom of the funnel.** No 404 page, no zero-result state on the
   roster/match filters, and the gold-standard profile (Kane) has no on-page breadcrumb. When a user
   or crawler goes off the happy path, the site stops helping.

---

## A. NAVIGATION & INFORMATION SCENT

### A1. Nav ships 5 tabs; the spec says 7; Phase 1 hubs are orphaned  [CRITICAL]
- **Problem.** `index.html:51-106` (and the identical block stamped into `wrestlers/index.html:100`,
  `matches/index.html`, `events/index.html:30`, `moments/.../index.html:34`, `wrestlers/kane/index.html:26`)
  ships the bar as **Wrestlers · Matches · Events · Promotions · More**. Your own
  `03-mega-nav.md:20-24` mandates **Wrestlers · Matches · Events · Promotions · Hall of Fame · Media ·
  More**. Meanwhile the directories `/hall-of-fame/`, `/current/`, `/legends/`, `/women/`, `/media/`
  all exist (confirmed via `ls`). There is no link to any of them in the header on the pages reviewed.
  A user cannot navigate to the Hall of Fame or the Women's hub at all; those pages are islands.
- **Fix.** Bring the shipped shell up to the 7-tab spec, or (better, given the meganav-guard constraint
  of a fixed bar) keep 5 tabs and route the new hubs into existing dropdown panels: put Hall of Fame,
  Legends, Current, Women under the **Wrestlers** panel as a "By Status / By Division" column; put
  Media under **More**. Re-stamp the one nav partial across all ~170 pages. Because the nav is copy-
  pasted inline (not a JS include), this is a single find/replace build step — but it also means the
  nav is *already* drifting page to page, which is the root risk (see A5).
- **Buildable?** Yes. Static HTML edit + re-stamp. No backend.
- **Source pattern.** Transfermarkt promotes high-value entity classes (competitions, clubs) to
  first-class landing pages and surfaces them in a stable global bar rather than burying them;
  see their own writeup of "new navigation tools and landing pages"
  (https://www.transfermarkt.co.uk/new-navigation-tools-and-landing-pages-coming-to-transfermarkt/view/news/438576).

### A2. The "More" tab is a mislabeled grab-bag with a lying link target  [HIGH]
- **Problem.** `index.html:97` — `<a class="nav__link" href="/rankings/" ...>More</a>`. The tab is
  labeled "More" but its click target is `/rankings/`, an unrelated destination. Inside it, Rivalries,
  Relationships, and Moments (three of your most *addictive* content types) sit two levels deep under a
  label with zero information scent. "More" tells a user nothing; Nielsen's scent research says a link
  must predict its destination.
- **Fix.** Kill "More." Surface Rivalries + Relationships + Moments under a scented label such as
  **"The Web"** (you already brand it that way on the home bento, `index.html:229`) or **"Connections"**,
  and give the tab an honest index landing (`/relationships/` or a new `/explore/`). Move Rankings to
  live inside the **Matches** panel next to "Top-Rated (5★)" where it belongs.
- **Buildable?** Yes. HTML only.
- **Source pattern.** Letterboxd never uses a "More" catch-all; every nav node names its content
  (Films, Lists, Members, Journal). https://letterboxd.com/

### A3. No "you are here" state anywhere in the nav  [HIGH]
- **Problem.** On `events/index.html` the "Events" tab has no active styling and no `aria-current`.
  Same on every hub. `css/site.css:112-115` styles `.nav__link` hover/focus only. A user three clicks
  deep has no persistent signal of which section they are in.
- **Fix.** Add `aria-current="page"` (or a `data-section` body attribute matched to a tab) and a CSS
  rule, e.g. `.nav__link[aria-current="page"]{color:var(--c-gold-bright);box-shadow:inset 0 -2px 0
  var(--c-gold);}`. The stamp step can set the attribute per section.
- **Buildable?** Yes. One CSS rule + a per-section attribute in the stamp.
- **Source pattern.** IMDb and Transfermarkt both keep the active primary section persistently
  highlighted; it is the cheapest orientation cue in catalog UX.

### A4. Mobile: you cannot reach a hub landing from its own tab  [HIGH]
- **Problem.** `js/main.js:22-34`: on `max-width:900px` the parent `.nav__link` click is
  `preventDefault()`-ed to toggle the panel. So on phones, tapping "Wrestlers" only expands the
  submenu; you reach `/wrestlers/` only via the "All Wrestlers" sublink. "More" has **no** "All"
  sublink, so mobile users can reach no landing for it at all (compounds A2). This is a known
  disclosure-vs-navigation conflict.
- **Fix.** Either (a) make the first row of every expanded mobile panel an explicit "View all
  [Section]" link, or (b) use the two-tap pattern: first tap opens, a visible caret is the toggle and
  the label itself navigates. Ensure every panel has an index escape link.
- **Buildable?** Yes. HTML (add the "View all" rows) + small JS tweak.
- **Source pattern.** NN/g mobile subnavigation guidance: always give the parent category its own
  reachable landing, don't let the accordion swallow it
  (https://www.nngroup.com/articles/mobile-subnavigation/).

### A5. The nav is copy-pasted inline into every page and is already drifting  [HIGH / systemic]
- **Problem.** The full 60-line `<header>` block is duplicated verbatim in every HTML file. That is why
  A1 happened: the spec moved, the pages didn't. With ~170 pages this guarantees divergence
  (Kane's profile even uses a *different* body layout system, see B1).
- **Fix.** On a no-build site you can't include partials server-side, but you can (a) keep a single
  canonical `nav.html` partial in the repo and a stamping script as the *only* way nav changes ship
  (looks like `build/` exists — enforce it), and (b) add a CI/grep check that every page's nav hash
  matches the canonical. Do not hand-edit nav in page files.
- **Buildable?** Yes. Build-time stamp + a diff check. No runtime backend.

### A6. Events panel mixes instances and categories with no labeling logic  [MEDIUM]
- **Problem.** `index.html:76-87`: the Events mega has "Recent" (specific dated shows, e.g.
  WrestleMania 42) beside "Brands" (evergreen series hubs, e.g. WrestleMania) with a third unlabeled
  column (`<h3>&nbsp;</h3>`) mixing "All Events" with more brand hubs. A user can't tell that
  `/events/wrestlemania-42-2026/` (an instance) and `/events/wrestlemania/` (the series) are different
  page types. Empty `&nbsp;` headings (also at `:58`, `:84`, `:93`) are a scent vacuum.
- **Fix.** Two clearly-titled columns only: "Latest shows" (instances) and "Series & specials" (hubs),
  each header filled. Add a one-line descriptor under the series links so instance-vs-series is obvious.
- **Buildable?** Yes. HTML.
- **Source pattern.** Transfermarkt separates a competition's current season page from its all-time
  landing page with distinct labels and breadcrumbs; the instance/series distinction is never implicit.

---

## B. THE DRILL PATH & BREADCRUMBS

### B1. The gold-standard profile has no on-page breadcrumb (but ships breadcrumb schema)  [CRITICAL]
- **Problem.** `wrestlers/kane/index.html:13-17` emits a full `BreadcrumbList` JSON-LD (Home →
  Wrestlers → Kane), but the rendered page has **no** `.crumbs` element. It jumps straight from the
  global nav into `<header class="athlete-hero">` (`:96`). Index pages and the moments page *do* render
  crumbs (`wrestlers/index.html:173`, `moments/.../index.html:107`). So the deepest, most-linked node
  in the drill path is the one place a user loses their trail. Worse: `athlete-hero`, `content-grid`,
  `stat-card`, `record-table` are classes **not present in `site.css`** (grep: 0 hits) — the profile
  template forked off the design system entirely, which is how it lost the crumb.
- **Fix.** Add the visible breadcrumb to the profile template to match the schema:
  `<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a
  href="/wrestlers/">Wrestlers</a></li><li aria-current="page">Kane</li></ol></nav>`, placed above the
  hero. Then reconcile the forked profile CSS back into `site.css`.
- **Buildable?** Yes. HTML + fold the orphan classes into the shared stylesheet.
- **Source pattern.** IMDb and Letterboxd both render a visible breadcrumb/parent link on every title
  and person page; the on-page trail and the structured-data trail must agree.

### B2. Profiles are drill-path dead-ends: sibling entities are unlinked text  [CRITICAL for stickiness]
- **Problem.** On Kane (`wrestlers/kane/index.html`): "Signature Matches" (`:176-180`) are plain
  prose, not links to `/matches/...` pages that exist. The "Career Timeline" and "Personas" name
  events and partners with no links. The record table (`:193-198`) links **opponents** but not the
  **events** (e.g. "King of the Ring 1998" is text, though `/events/` exists) and not the stipulation
  or the match page. There is no link from Kane to the rivalries or relationships he belongs to, and no
  "next/previous wrestler" or "more like this." A user who lands on a profile from search has almost
  nowhere addictive to go next except the global nav.
- **Fix.** Make every entity mention a link: opponent → profile (done), event → event page, signature
  match → match page, faction/partner → relationship page. Add two rails to the profile template:
  **"Rivalries featuring Kane"** and **"More monsters / Related wrestlers"** (seed by shared promotion
  + era tags you already store in `data-tags`). This is the single biggest lever on session depth.
- **Buildable?** Yes. All target pages exist; this is internal linking + one related-rail component
  (`.related-links` already exists in `site.css:369`).
- **Source pattern.** Sherdog fighter pages link every cell of the fight-history table — opponent,
  event, and method — so any row is a launch point (https://www.sherdog.com/). Letterboxd's "Similar
  Films" and IMDb's "More like this" carousel are the canonical related-rail patterns for keeping a
  session alive.

### B3. You have a sticky entity-subnav component built and unused  [HIGH — free win]
- **Problem.** `css/site.css:538-543` defines `.subnav-page` — a sticky, horizontally-scrolling tab
  strip (Oswald, uppercase, pill tabs) clearly intended for per-entity section jumps. No reviewed page
  uses it. Kane's long profile (Bio, Championships, Personas, Timeline, FAQ, Signature, Record) has no
  in-page jump nav, so on mobile it is a very long scroll with no wayfinding.
- **Fix.** Add `.subnav-page` to the profile template with anchor links to each `<h2>` section
  (Overview · Titles · Timeline · Matches · FAQ). It sticks under the header (the CSS already sets
  `top:60px`). Same component fits match and event pages.
- **Buildable?** Yes. The CSS exists; add the markup + `id`s on sections.
- **Source pattern.** Transfermarkt's per-player tab strip (Profile / Stats / Transfers /
  Achievements) is the model; on long single pages Letterboxd uses the same sticky in-page tabbing.

### B4. Redundant doors: Matches vs Rankings vs "Top-Rated (5★)"  [MEDIUM]
- **Problem.** `index.html:70-71` puts "All Matches" and "Top-Rated (5★) → /rankings/" side by side;
  the "More" panel *also* lists "Rankings" (`:103`); the matches index answer copy links to a `#by-era`
  browse. Three overlapping entry points to "good matches" with unclear boundaries. Cognitive load with
  no payoff — users can't predict what's behind each.
- **Fix.** Define one clear model: **Matches** = the full filterable archive; **Rankings** = curated
  ranked lists (Top 100, best per year). State the difference in one line on each index. Remove the
  duplicate "Rankings" from the More panel once Matches owns it.
- **Buildable?** Yes. HTML + copy.

---

## C. FINDABILITY & SEARCH

### C1. Cmd-K search index is stale and misses the new content  [CRITICAL]
- **Problem.** `js/search-index.js` contains 153 entries: 89 Wrestler, 30 Match, 15 Rivalry, 10 Event,
  5 Promotion, 4 Moment — and **0** entries for `/hall-of-fame/`, `/current/`, `/legends/`, `/women/`,
  `/media/` (grep confirmed). There are 94 wrestler directories on disk, so 5 profiles aren't even in
  search. The command palette (`js/nav.js`) is the marquee "most searchable site" feature, and it can't
  surface the newest, highest-intent pages (champions, women's division, HOF).
- **Fix.** Regenerate `search-index.js` from the filesystem as part of the build (one script that walks
  `/wrestlers/`, `/matches/`, `/events/`, `/hall-of-fame/`, etc. and emits the array). Add `k` kinds for
  the new hubs. Make regeneration a required build step so the index can never drift again.
- **Buildable?** Yes. Static JSON-in-JS generated at build; no runtime backend.
- **Source pattern.** Letterboxd's global search returns every entity type (films, people, lists,
  members) from one box; parity requires the index to cover every content type you ship.

### C2. Roster index appears frozen at 41 while 94 profiles exist  [CRITICAL]
- **Problem.** `wrestlers/index.html:183` states "profiles 41 of the most important wrestlers" and
  `:191` hardcodes `<span id="roster-count">41</span>`; the home stat bar says "41+" (`index.html:163`).
  Filesystem shows 94 wrestler dirs. If the A-Z grid renders 41 cards, ~53 profiles are browse-orphaned
  (reachable only by internal body links or a search that itself misses 5 of them, per C1). Three
  different numbers (41 / 89 / 94) for the same thing also erodes the "definitive database" trust claim.
- **Fix.** Regenerate the roster grid + count from the filesystem in the same build step as C1. Show a
  live "N of 94" that updates as filters apply (the counter wiring already exists in `main.js:84`).
  Reconcile the home stat bar to the true number.
- **Buildable?** Yes. Build-time generation of the card list.

### C3. Zero-result filter state is a blank dead-end  [HIGH]
- **Problem.** `js/main.js:71-85` (`apply()`) toggles `.hide` on cards and writes the count, but when
  `shown === 0` it does nothing else: the grid is empty, the label reads "0 wrestlers shown," and there
  is no message, no "clear filters," no fallback. Same for the matches index. There is a `.cmdk__empty`
  state for the palette (`site.css:904`) but nothing for the on-page filters.
- **Fix.** In `apply()`, when `shown === 0`, inject an empty-state block: a line ("No wrestlers match
  'X' in WCW.") plus a "Clear filters" button that resets the query and promo. Add a `.list-empty`
  style. Announce it via `aria-live="polite"` on the count region so screen-reader users hear it.
- **Buildable?** Yes. ~15 lines JS + one CSS rule.
- **Source pattern.** Letterboxd and IMDb list filters always render an explicit "no results / adjust
  your filters" state with a reset affordance rather than a silent empty grid.

### C4. No 404 page  [CRITICAL for a crawlable site]
- **Problem.** `ls` confirms no `404.html`. On a static host, any typo, moved/renamed slug, or stale
  external link serves the host's default error page with no nav, no search, no way back. For a site
  whose entire pitch is crawlability and long-tail SEO, this is the worst dead-end.
- **Fix.** Ship `/404.html` with the full shell (nav + Cmd-K), an honest message, a search prompt, and
  rails to the top hubs and five-star matches. Configure the host (Netlify/Cloudflare/`_redirects` or
  equivalent) to serve it. Also add redirects for any renamed slugs (the Kevin Steen "redirect" task
  implies slugs are already changing).
- **Buildable?** Yes. One static page + host config. No backend.
- **Source pattern.** IMDb and Letterboxd 404s keep the global nav + search and offer popular
  destinations so a wrong URL becomes a new session instead of an exit.

### C5. Filter buttons are unstyled; filter bar sits inside the grid  [MEDIUM]
- **Problem.** `wrestlers/index.html:196-201` and `matches/index.html:189-194` use `class="fbtn"` for
  the promotion filters, but `.fbtn` has **0** definitions in `site.css` (grep). They render as raw
  browser buttons — inconsistent with the polished `.rt-filters button` pills used elsewhere
  (`site.css:552-557`). The filter bar is also placed *inside* `#roster` as `grid-column:1/-1`, so it's
  a grid child rather than a proper toolbar, which is fragile and semantically odd.
- **Fix.** Either rename `fbtn` to the existing styled `rt-filters` pattern or add a `.fbtn` rule
  mirroring it (including `[aria-pressed="true"]`/`is-active` gold state). Move the filter bar out of
  the grid into a sibling `.rt-filters` toolbar above it. Add `aria-pressed` to the toggle buttons.
- **Buildable?** Yes. CSS + small markup move.

### C6. Search discoverability is invisible on touch; palette has no browse fallback  [MEDIUM]
- **Problem.** The search affordance is a `⌘K` pill (`index.html:108-110`) — meaningless and
  unpressable-looking on phones (no keyboard). The palette opens empty-ish (first 8 index items,
  `nav.js:39`) with no categories, no "popular," and its empty state (`nav.js:50`) offers no "browse
  all wrestlers" escape link.
- **Fix.** On mobile show a plain magnifier button that opens the same palette. Seed the empty palette
  with labeled groups ("Jump to: Wrestlers · Matches · Events") and, in the no-results state, add a
  "Browse all wrestlers" link. Consider scoping (type a kind prefix) for the power users you're courting.
- **Buildable?** Yes. JS + HTML in the existing palette.
- **Source pattern.** Letterboxd's search seeds recent/popular and groups results by type; the empty
  state always offers a browse path. https://letterboxd.com/

---

## D. ERROR / EDGE / CONSISTENCY

### D1. Facade video error handling is a new-tab hop, not an inline state  [MEDIUM]
- **Problem.** On the home hero (`index.html:144-149`) the featured video facade `onclick` opens a
  YouTube *search* in a new tab instead of playing — inconsistent with the real facade→iframe swap used
  on the moments page (`main.js:37-56`). If a region blocks the embed, the moments page relies on a
  buried text link (`moments/.../index.html:132`); there's no inline "unavailable in your region" state.
- **Fix.** Use the real `data-provider`/`data-id` facade on the home hero too. Add an inline fallback
  message on embed error (China note is good but should be a visible state, not fine print).
- **Buildable?** Yes. HTML + a small `onerror`/timeout handler in `main.js`.

### D2. Breadcrumb/heading `text-wrap:balance` + em-dash separators fight the copy standard  [LOW/IA-adjacent]
- **Problem.** Breadcrumbs and metadata lean on ` · ` and `—` separators (e.g.
  `events/index.html:130` "June 27, 2026 · Riyadh"; card meta throughout). Your own copy standard bans
  em-dash separators and decorative punctuation. This is IA-adjacent because separators carry hierarchy
  meaning inconsistently (sometimes date·place, sometimes promo·nickname).
- **Fix.** Standardize record metadata order and separator (a thin middot is fine if consistent; drop
  em-dashes as separators). Document the meta grammar so every card reads the same.
- **Buildable?** Yes. Copy + template.

### D3. `main.js` `[data-filter]` selector collides with record-table filters  [MEDIUM — verify]
- **Problem.** `main.js:64` binds every `[data-filter]` element as if it were a search *input* with a
  `data-filter-target`. Kane's record filters (`wrestlers/kane/index.html:184-190`) use
  `data-filter="ppv"` on `<button>`s for a different purpose, and `enhance.js` separately binds
  `button[data-filter]` (grep). Two scripts claiming the same attribute is a latent bug: the roster
  input and the record buttons share a selector namespace.
- **Fix.** Namespace them: use `data-list-filter` for the search input and `data-record-cat` for record
  buttons so no handler double-binds. Verify Kane's PPV/TV/Tag/Title filter actually works today (it
  depends on which script wins).
- **Buildable?** Yes. Attribute rename across templates.

---

## E. PRIORITIZED BUILD BACKLOG

| # | Item | Sev | Effort | Backend? |
|---|------|-----|--------|----------|
| 1 | Ship `/404.html` with shell + search + rails (C4) | Critical | S | No (host cfg) |
| 2 | Regenerate `search-index.js` + roster grid from FS at build (C1, C2) | Critical | M | No |
| 3 | Surface Phase 1 hubs in nav; kill "More" mislabel (A1, A2) | Critical | M | No |
| 4 | Add breadcrumb to profile template; refold forked CSS (B1) | Critical | M | No |
| 5 | Zero-result empty state + clear-filters + aria-live (C3) | High | S | No |
| 6 | Related rails + link every entity mention on profiles (B2) | High | M | No |
| 7 | `aria-current` active nav state (A3) | High | S | No |
| 8 | Sticky in-page `.subnav-page` on long profiles (B3) | High | S | No |
| 9 | Mobile "View all [Section]" escape links (A4) | High | S | No |
| 10 | Single canonical nav partial + drift check (A5) | High | M | No (build) |
| 11 | Style `.fbtn` / move filter bar out of grid (C5) | Med | S | No |
| 12 | De-duplicate Matches/Rankings model + labels (B4) | Med | S | No |
| 13 | Namespace `data-filter` collision (D3) | Med | S | No |
| 14 | Home hero real facade + inline embed error state (D1) | Med | S | No |
| 15 | Events panel instance-vs-series labeling (A6) | Med | S | No |

Nothing on this list needs a backend. The two structural risks — a hand-copied nav and a hand-authored
search index/roster — are both solved by moving them into the existing `build/` step so they can never
drift from the content on disk again.

---

## Sources researched
- Transfermarkt, "New navigation tools and landing pages" — first-class entity landing pages + stable
  global nav: https://www.transfermarkt.co.uk/new-navigation-tools-and-landing-pages-coming-to-transfermarkt/view/news/438576
- Nielsen Norman Group, "Mobile Subnavigation" — parent categories must stay reachable:
  https://www.nngroup.com/articles/mobile-subnavigation/
- Letterboxd — entity-as-facet linking, typed global search, "Similar Films" rails, explicit empty
  states: https://letterboxd.com/
- Sherdog — every fight-history cell (opponent/event/method) is a launch point: https://www.sherdog.com/
- IMDb — persistent breadcrumb/parent link + "More like this" recommendation carousel on every title.
