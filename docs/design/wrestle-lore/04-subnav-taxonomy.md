# Wrestle Lore — Sub-Navigation, Category Taxonomy & Faceted Browse Spec

Information-architect deliverable for the Direction-B "Editorial Poster Wall" revamp. This spec
defines the **category taxonomy**, the **secondary/sub navigation** under each top tab, the
**index-page filter bars**, **breadcrumb logic**, the **drill path** from tab to filtered list to
profile, and a **crawlable URL scheme**. It ends with a **clickable → link-target table** for every
new control.

- Date: 2026-07-26. Author: IA agent.
- Builds on: `00-content-data-research.md` (facts, tag lists, gaps) and `01-inspiration-research.md`
  (patterns). Facts are not re-derived here; the research docs are the source of truth for which
  wrestler carries which tag. Anything unverified is flagged `VERIFY`.
- Hard constraints honored: static, no build step, **fully crawlable** (every facet is reachable by
  a raw `<a href>`, never JS-only), no browser storage, root-absolute paths, one stylesheet, vanilla
  JS. Anti-AI copy standard (no decorative arrows in CTAs, no em-dash sentence separators, no banned
  marketing words, specific nouns).

Two facts about the current build that this spec must correct:
1. `/wrestlers/index.html` renders **41** cards but the roster directory holds **89** slugs. The
   index must be regenerated to render all 89 with the new multi-axis `data-*` attributes below.
2. Sub-pages (`/wrestlers/`, `/promotions/`) still carry the **old flat nav** (Wrestlers/Matches/
   Rivalries/Relationships/Rankings/中文/Join) and the **old "MAT" brand**, while the homepage uses
   the new mega-nav. The mega-nav + brand rename to "Wrestle Lore" must be propagated site-wide
   (nav owner's task; noted here because sub-nav lives under those tabs).

---

## 1. The taxonomy model

Every wrestler entity carries tags on **six axes**. Axes are orthogonal; a wrestler holds one or
more values per axis. Tags are the single source that powers (a) tile badges, (b) filter pills, and
(c) pre-rendered facet hubs. Tag assignment per slug comes from `00-content-data-research.md`
sections 5 and 2–4; the index-build script applies them.

| Axis | Key | Values (controlled vocabulary) | Cardinality | Drives |
|---|---|---|---|---|
| **A. Status** | `data-status` | `current`, `legend` | one | red/gold status pill; `/wrestlers/current/`, `/wrestlers/legends/` |
| **B. Gender/Division** | `data-gender` | `women`, `men` | one | women's magenta marker; `/wrestlers/women/` |
| **C. Promotion** | `data-promo` | `wwe wcw ecw tna nxt njpw aew` (space-list, multi) | one+ | promotion accent chip; `/promotions/{slug}/` |
| **D. Era** | `data-era` | `golden` `new-gen` `attitude` `ruthless` `pg` `modern` | one+ | era tag (kicker text); era hubs (Tier 2) |
| **E. Division/role** | `data-div` | `main-event` `womens` `tag` `cruiserweight` `faction` | one+ | division pill (client filter); division hubs (Tier 2) |
| **F. Accolade** | `data-badge` | `hof` `hof-2x` `champion` `five-star` | zero+ | gold diamond marker; Hall of Fame hub |

Non-wrestler entities also get a single-token `data-kind`: `wrestler`, `event`, `moment`, `match`,
`rivalry`, `promotion`, `media`, `hof-class`. This mirrors the existing `search-index.js` `k` field.

**Persona/alias pages** (`mean-mark-callous`, `the-american-badass`, `the-ringmaster`,
`stunning-steve-austin`, `diesel`, `razor-ramon`) are cross-links, **not roster tiles** — exclude
from the poster walls (`data-alias="true"`), keep them crawlable and in ⌘K.
`vince-mcmahon` is `data-kind="wrestler" data-role="executive"` — surface only in the More panel /
Personalities lane, never on the athlete grid.

### 1.1 Hub tiers (what gets a pre-rendered page vs. a client-only pill)

The crawl budget and duplicate-content risk mean not every facet combination becomes a page. Two
tiers:

- **Tier 1 — pre-rendered crawlable hub (own directory, own canonical, in sitemap):** high
  search/GEO value or explicitly requested. Filter control is an `<a href>`.
- **Tier 2 — client-only pill (no page yet):** filter control is a `<button>`; state lives in the
  URL hash for sharing. Promote to Tier 1 later by rendering the page and swapping the control to an
  `<a>`.

| Facet | Tier | URL |
|---|---|---|
| All wrestlers A–Z | 1 | `/wrestlers/` |
| Current | 1 | `/wrestlers/current/` |
| Legends | 1 | `/wrestlers/legends/` |
| Women's division | 1 | `/wrestlers/women/` |
| Per promotion (roster) | 1 (reuse) | `/promotions/{wwe\|wcw\|ecw\|tna\|nxt\|njpw\|aew}/` |
| Hall of Fame | 1 | `/hall-of-fame/` |
| Media & Creators | 1 | `/media/` |
| Events by year | 1 | `/events/2026/` |
| Events by series | 1 (reuse+extend) | `/events/{wrestlemania\|royal-rumble\|…}/` |
| Men | 2 | hash `#gender=men` (a "men" hub would duplicate the master; skip) |
| Era (Attitude, Modern, …) | 2→1 | `/wrestlers/eras/{era}/` (build Attitude + Modern first) |
| Division (tag, cruiserweight, faction) | 2 | hash; factions cross-link `/relationships/#factions` |
| Championship / title reigns | 2 | data-dependent; needs title front-matter that does not exist yet — **VERIFY data before building** |

Rule of thumb: an axis **value** earns a Tier-1 page when it has ≥12 members and answers a real
search query ("women wrestlers", "attitude era wrestlers", "WWE Hall of Fame classes"). Below that,
keep it a client pill.

---

## 2. Crawlable URL / parameter scheme

The crux of "stay crawlable": **directories are the canonical, indexable surface; the hash is a
convenience layer.**

1. **Facet = directory.** Every Tier-1 facet is a real folder with `index.html`, a self-referential
   `<link rel="canonical">`, `BreadcrumbList` + `ItemList` JSON-LD, and a sitemap entry. Crawlers
   and no-JS users get the full filtered set as raw HTML links.
2. **Combined/Tier-2 state = URL hash.** On the master index the filter bar reflects the active set
   in `location.hash`, e.g. `/wrestlers/#promo=wcw&status=legend&era=attitude`. The hash is
   shareable, needs no storage, and is **not** a separate indexable URL. The master index canonicals
   to `/wrestlers/` regardless of hash.
3. **Query `?q=` stays for search only.** `search-index.js` and the `WebSite` `SearchAction`
   already target `/wrestlers/?q={query}`; keep that. `?q=` pre-fills the text filter; it does not
   create indexable variants (canonical still `/wrestlers/`).
4. **No query-string facets.** Do **not** ship `?promo=wcw` style links — they create thin,
   near-duplicate indexable pages. Facets are either a directory (Tier 1) or a hash (Tier 2).
5. **One canonical per entity.** A wrestler lives only at `/wrestlers/{slug}/`. Facet hubs *list*
   them; they never re-host the profile. Promotion rosters live at `/promotions/{slug}/` — do **not**
   create `/wrestlers/{promo}/` (avoids two URLs for one roster).

Full Tier-1 directory map to build:

```
/wrestlers/                     master A–Z (89), client filter bar
/wrestlers/current/             status=current
/wrestlers/legends/             status=legend
/wrestlers/women/               gender=women
/wrestlers/eras/                era hub index (Tier 2 spokes below)
/wrestlers/eras/attitude-era/   era=attitude   (build first)
/wrestlers/eras/modern/         era=modern     (build first)
/promotions/                    promotion hub index
/promotions/{wwe|wcw|ecw|tna|nxt}/   exist
/promotions/njpw/               GAP — REQUIRED (req 5)
/promotions/aew/                GAP — recommended (req names AEW)
/hall-of-fame/                  GAP — REQUIRED (req 6)
/hall-of-fame/{2021..2025}/     GAP — one page per class (Tier 2, optional)
/media/                         GAP — REQUIRED (req 7)
/media/{slug}/                  GAP — one page per creator
/events/                        master
/events/2026/                   GAP — year hub (req 3)
/events/{series}/               exist for 5 WWE series; add summerslam, survivor-series (GAP)
```

---

## 3. Color + badge system (additive to `css/site.css`)

Requirement 1 asks for MORE colors and MORE visual separation. Achieve it with **new tokens** and a
**shape-encodes-axis** rule so a tile parses in one second (pattern A3/D1).

### 3.1 New design tokens (append to `:root`)

```css
/* new promotion accents */
--c-njpw:#c8102e;            /* VERIFY vs official NJPW red; render on a BLACK field with a white
                                hairline so it never reads as WWE red — differentiate by field,
                                not hue (per 01-inspiration D3). */
--c-aew:#c79a3b;             /* VERIFY; AEW is black+gold. Pair with black field + square-cut badge
                                so it never reads as WCW gold #e2b13c. */
--c-njpw-field:#0a0a0b; --c-aew-field:#0b0b0c;

/* non-promotion axis colors */
--c-status-current:var(--c-red);     /* CURRENT = red (active now)     */
--c-status-legend:var(--c-gold);     /* LEGEND  = gold (canonized)     */
--c-women:#c33c9a;                    /* women's division — magenta, unused elsewhere */
--c-women-tint:rgba(195,60,154,.14);
--c-hof:var(--c-gold);                /* Hall of Fame = gold diamond    */
```

### 3.2 Shape encodes the axis (so color is never ambiguous)

| Axis | Shape | Class | Where |
|---|---|---|---|
| Promotion | filled **pill** | `.chip .chip--{promo}` (existing) | tile top-left |
| Status | outline **pill + dot** | `.status .status--current` / `.status--legend` (new) | tile top-right |
| Women's division | filled **oval marker** in magenta | `.mark--women` (new) | tile top-right, below status |
| Era | **square-cut hairline tag** | `.tag--era` (new) | tile kicker line (text) |
| Accolade (HOF/champion/5★) | gold **diamond/star marker** | `.mark--hof`, `.mark--5star` (existing rating) | tile top-right |

New CSS to add:

```css
.chip--njpw{color:#fff;background:var(--c-njpw);border-color:#fff;box-shadow:inset 0 0 0 1px #000;}
.chip--aew{color:var(--c-aew);background:var(--c-aew-field);border-color:var(--c-aew);border-radius:var(--r-sm);} /* square-cut */
.status{display:inline-flex;align-items:center;gap:.35em;padding:.15em .55em;border-radius:var(--r-pill);
  font-family:var(--font-cond);text-transform:uppercase;letter-spacing:.05em;font-size:var(--fs-300);
  border:1px solid currentColor;background:transparent;}
.status::before{content:"";width:.5em;height:.5em;border-radius:50%;background:currentColor;}
.status--current{color:var(--c-status-current);}
.status--legend{color:var(--c-status-legend);}
.mark--women{color:#fff;background:var(--c-women);border-color:var(--c-women);}   /* uses .chip base */
.mark--hof{color:#000;background:var(--c-gold);border-color:var(--c-gold);}       /* uses .chip base */
.tag--era{font-family:var(--font-cond);text-transform:uppercase;letter-spacing:.06em;
  font-size:var(--fs-300);color:var(--c-text-dim);}
```

### 3.3 Tile badge budget

Max **two** graphic badges per tile: **promotion chip** (top-left) + **one** right-corner marker in
priority order `hof-2x > hof > status(current/legend) > women`. Era and secondary promotions live in
the kicker text (`.tile__kicker`) to avoid clutter. This keeps the wall dense but legible.

### 3.4 Per-hub accent recolor (the "more separation" lever)

Each Tier-1 hub recolors its eyebrow, section rule, and active-pill to its axis color, so the four
walls feel distinct: `/current/` = red, `/legends/` = gold, `/women/` = magenta, `/promotions/{x}/`
= that promotion accent, `/hall-of-fame/` = gold, `/media/` = a cool neutral (`--c-focus` blue) to
signal "off-canvas / press box." Set once per page via a body class, e.g. `body.hub--legend`, that
remaps `--c-accent` used by `.eyebrow`, `.rule-gold`, and `.fbtn.is-active`.

---

## 4. Sub-nav component: the faceted filter bar

One reusable component, used on every index. Extends the existing `.filterbar`/`.fbtn` pattern
(already on `/wrestlers/`) from single-axis to multi-axis.

### 4.1 Structure and the crawlable trick

- The bar is grouped by axis. Each group has a label and a row of controls.
- **A control that maps to a Tier-1 hub is an `<a href>`** (crawlable + no-JS fallback). When JS is
  present and the user is already on the master index, JS intercepts the click and filters in place,
  updating the hash; otherwise the link just navigates to the hub.
- **A control that is Tier-2 (no page) is a `<button>`** that only filters client-side.
- Within an axis, selection is **single-select** (radio-like, with an "All" reset). **Across** axes,
  logic is **AND** (promotion=WCW AND status=legend narrows to WCW legends).
- A live count (`<span data-filter-count>`) and the existing text `<input data-filter>` remain.

HTML pattern (master `/wrestlers/`):

```html
<div class="filterbar filterbar--faceted" id="roster" data-facets>
  <div class="fb-group" data-axis="status">
    <span class="fb-label">Status</span>
    <a class="fbtn is-active" data-status="all" href="/wrestlers/">All</a>
    <a class="fbtn" data-status="current" href="/wrestlers/current/">Current</a>
    <a class="fbtn" data-status="legend"  href="/wrestlers/legends/">Legends</a>
  </div>
  <div class="fb-group" data-axis="gender">
    <span class="fb-label">Division</span>
    <a class="fbtn" data-gender="all" href="/wrestlers/">All</a>
    <a class="fbtn" data-gender="women" href="/wrestlers/women/">Women</a>
    <button class="fbtn" data-gender="men" type="button">Men</button>
  </div>
  <div class="fb-group" data-axis="promo">
    <span class="fb-label">Promotion</span>
    <button class="fbtn is-active" data-promo="all" type="button">All</button>
    <a class="fbtn" data-promo="wwe"  href="/promotions/wwe/">WWE</a>
    <a class="fbtn" data-promo="wcw"  href="/promotions/wcw/">WCW</a>
    <a class="fbtn" data-promo="ecw"  href="/promotions/ecw/">ECW</a>
    <a class="fbtn" data-promo="tna"  href="/promotions/tna/">TNA</a>
    <a class="fbtn" data-promo="nxt"  href="/promotions/nxt/">NXT</a>
    <a class="fbtn" data-promo="njpw" href="/promotions/njpw/">NJPW</a>
    <a class="fbtn" data-promo="aew"  href="/promotions/aew/">AEW</a>
  </div>
  <div class="fb-group" data-axis="era">
    <span class="fb-label">Era</span>
    <button class="fbtn is-active" data-era="all" type="button">All</button>
    <a class="fbtn" data-era="attitude" href="/wrestlers/eras/attitude-era/">Attitude</a>
    <a class="fbtn" data-era="modern"   href="/wrestlers/eras/modern/">Modern</a>
    <button class="fbtn" data-era="golden"   type="button">Golden</button>
    <button class="fbtn" data-era="new-gen"  type="button">New Gen</button>
    <button class="fbtn" data-era="ruthless" type="button">Ruthless Aggression</button>
    <button class="fbtn" data-era="pg"       type="button">PG / Reality</button>
  </div>
</div>
```

Each card carries the axes as data-attributes (extends the current `data-promo`/`data-tags`):

```html
<article class="card" data-search
  data-name="Sting" data-status="legend" data-gender="men"
  data-promo="wcw tna wwe" data-era="new-gen attitude ruthless modern"
  data-div="main-event faction" data-badge=""
  data-tags="the icon the stinger the crow scorpion death lock franchise of wcw">
  <span class="chip chip--wcw card__tag">WCW</span>
  <span class="status status--legend card__status">Legend</span>
  …
</article>
```

### 4.2 Filter JS (extend `js/main.js`, ~40 lines, no deps, no storage)

- Read all `.fb-group[data-axis]`; maintain `state = {status:'all',gender:'all',promo:'all',era:'all',div:'all'}`.
- On control activate: set that axis, toggle `.is-active` within the group, re-run `apply()`.
- `apply()`: a card is visible iff for every axis where `state[axis]!=='all'`, the card's
  `data-{axis}` token list contains the value AND (text filter matches `data-name`+`data-tags`).
  Show/hide with a class; update `data-filter-count`.
- Reflect non-default axes in `location.hash` (`history.replaceState`, so Back is not polluted).
- On load, parse `location.hash` (and `?q=`) and pre-apply. No `localStorage`, no cookies.
- `<a>` controls: `e.preventDefault()` only when `document` is the master index and JS is active;
  else allow navigation to the hub. This guarantees the crawlable/no-JS path.
- Empty state: if zero cards match, show a `.fb-empty` block with the two nearest single-axis links
  (e.g. "No WCW women in the set. See all Women or all WCW.") — never a dead end (pattern B2).

### 4.3 Filter-bar CSS additions

```css
.filterbar--faceted{display:grid;gap:var(--sp-3);}
.fb-group{display:flex;flex-wrap:wrap;gap:.5rem;align-items:center;}
.fb-label{font-family:var(--font-cond);text-transform:uppercase;letter-spacing:.08em;
  font-size:var(--fs-300);color:var(--c-text-dim);min-width:6.5em;}
.fb-empty{grid-column:1/-1;padding:var(--sp-5);border:1px dashed var(--c-line-strong);
  border-radius:var(--r-lg);color:var(--c-text-muted);}
a.fbtn{text-decoration:none;}                 /* facet anchors read as buttons, not links */
```

---

## 5. Per-index sub-nav specs

### 5.1 `/wrestlers/` (master) and its facet hubs
- **Master:** full faceted bar (4.1), all 89 cards, count, text search. Dropdown ("Wrestlers" tab
  mega panel) mirrors the axes (see §7 table). Ends in FAQ + "Keep going" rail (Legends, Women,
  Hall of Fame, a promotion).
- **`/current/`, `/legends/`, `/women/`, `/eras/{era}/`:** same component, but the hub's own axis
  pill is pre-selected and rendered `is-active`; the page ships **only** the matching cards as raw
  HTML (so it is a real crawlable set, not a JS-filtered master). Remaining axes stay as live pills
  to narrow further (e.g. on `/legends/`, the promotion group still filters). Per-hub accent recolor
  per §3.4. Each hub: answer-first paragraph, `ItemList` JSON-LD, "Keep going" rail to sibling hubs.

### 5.2 `/promotions/` and `/promotions/{slug}/`
- **Promotions index sub-nav:** a filter/segment bar with `Active` vs `Defunct` and `US` vs `Japan`
  segments, plus the 7 promotion chips. Cards become **brand cards** (req 4) carrying a "Where to
  watch" chip row (text chips, not logos): e.g. WWE → `Netflix` `USA Network` `The CW` `ESPN (US)`
  `Netflix (intl)`; NJPW → `NJPW World` `TrillerTV`; TNA → `AMC` `AMC+` `TNA+` `Prime (library)`;
  AEW → `TBS` `TNT` `HBO Max` `AEW Plus (intl)`. Streaming facts and exact copy come verbatim from
  `00-content-data-research.md` §1; anything it flags stays `VERIFY`.
- **Each promotion hub sub-nav:** in-page anchor tabs `Roster` · `Events` · `Streaming` · `History`
  (`<a href="#roster">` etc., crawlable jump-links). Roster section reuses the faceted bar scoped to
  that promotion (status + era only; promotion is fixed).

### 5.3 `/hall-of-fame/` (new)
- **Sub-nav segments:** `Most-Decorated` · `Two-Time Club` · `By Class (2025 → 2021)` · `Inductees A–Z`.
- **Layout:** hero panel = **Ric Flair, two-time inductee** (gold, `mark--hof` diamond, links
  `/wrestlers/ric-flair/`); "Two-Time Club" strip (Michaels, Booker T, Razor Ramon, Kevin Nash,
  Hulk Hogan — all existing pages); "Last 5 Classes" rail (2021–2025) with headline-inductee tiles
  linking to existing pages, and non-page inductees rendered as **non-link tiles with a "profile
  coming" note** (never a 404). Class years/rosters and the two-time years come from research §2;
  `VERIFY`-flagged years must not be printed until confirmed.

### 5.4 `/media/` (new — "Media & Creators", req 7)
- **Sub-nav segments:** `Interviewers` · `Podcasters` · `Journalists` · `Creators`.
- **Hero:** Chris Van Vliet (confirmed `HIGH`), links `/media/chris-van-vliet/`. Grid of the
  proposed roster (Renee Paquette, Rosenberg, Helwani, Sapp, Salcedo, Keller/Meltzer) each rendered
  with a `VERIFY` state until affiliation is confirmed; a media card links out only when its page
  exists. **Sami Zayn does NOT appear here** — he is an active wrestler; a small explainer line
  routes his mention to `/wrestlers/sami-zayn/`. Accent = `--c-focus` blue to separate the press box
  from the athlete walls.

### 5.5 `/events/` and event facet hubs (req 3)
- **Events index sub-nav (three toggles):**
  - **By series:** `WrestleMania` `Royal Rumble` `SummerSlam` `Survivor Series` `Elimination Chamber`
    `Night of Champions` `Backlash` → each links its series hub (5 exist; SummerSlam + Survivor
    Series are gaps).
  - **By year:** `2026` → `/events/2026/` (build). Structure supports `2025`, `2024`… later.
  - **By promotion:** `WWE` `NJPW` `TNA` `AEW` (client pills now; only WWE has event pages, others
    are gaps — pills that resolve to a promotion's events section).
  - A **Big Four** quick-filter (`Royal Rumble` `WrestleMania` `SummerSlam` `Survivor Series`).
- **Event card** carries a streaming badge ("ESPN (US) / Netflix (intl)" for WWE PLEs, per §1).
- **Event-edition breadcrumb** nests under its series (see §6).

### 5.6 `/matches/`, `/moments/`, `/rivalries/`
- Add a light faceted bar: Matches → `By promotion` + `By rating (5★ / 4.5★+)` + `By decade`;
  Moments → `By type (injury / debut / incident)`; Rivalries → `By era` + `By promotion`. All
  client-only (Tier 2) except promotion, which links the promotion hubs. Keeps the pattern uniform.

---

## 6. Breadcrumb logic

`BreadcrumbList` must be **stable and single-trail** for schema integrity, even though an entity
belongs to many facets. Rule: **one canonical parent per page**; cross-facet membership is shown via
tile chips and the "Keep going" rail, never in the breadcrumb.

| Page | Breadcrumb trail |
|---|---|
| `/wrestlers/` | Home / Wrestlers |
| `/wrestlers/current/` | Home / Wrestlers / Current |
| `/wrestlers/legends/` | Home / Wrestlers / Legends |
| `/wrestlers/women/` | Home / Wrestlers / Women's Division |
| `/wrestlers/eras/attitude-era/` | Home / Wrestlers / Eras / Attitude Era |
| `/wrestlers/{slug}/` | Home / Wrestlers / {Name} |
| `/promotions/` | Home / Promotions |
| `/promotions/{slug}/` | Home / Promotions / {Promo} |
| `/hall-of-fame/` | Home / Hall of Fame |
| `/hall-of-fame/2025/` | Home / Hall of Fame / 2025 Class |
| `/media/` | Home / Media & Creators |
| `/media/{slug}/` | Home / Media & Creators / {Name} |
| `/events/` | Home / Events |
| `/events/2026/` | Home / Events / 2026 |
| `/events/{series}/` | Home / Events / {Series} |
| `/events/{series}-{year}/` (edition) | Home / Events / {Series} / {Series} {Year} |

Notes: the wrestler **profile** parents to `Wrestlers` (not to a facet) so the trail never changes
when a wrestler gains a tag. The event **edition** parents to its **series** hub (two-level), which
is the one place a mid-level crumb is used, because the series hub genuinely exists and aids crawl
depth. Every breadcrumb ships as visible `<nav class="crumbs">` **and** matching `BreadcrumbList`
JSON-LD (both already present on existing pages — extend, don't replace).

---

## 7. Drill path: tab → filtered list → profile

Three worked paths (each ends in a profile and a rail, never a dead end — pattern B2):

**Path 1 — "Women's legends of WCW":**
Top tab **Wrestlers** (mega panel) → panel link **Legends** (`/wrestlers/legends/`) → on the hub,
click promotion pill **WCW** (narrows in place, hash `#promo=wcw`) → click a card, e.g.
**Chyna**/**Lita** → profile → "Keep going" rail offers *More Women's Legends*, *WCW roster*,
*Attitude Era*.

**Path 2 — "Where do I watch NJPW, and who's on it":**
Top tab **Wrestlers** → panel link **NJPW** (`/promotions/njpw/`) → promotion hub `Streaming`
jump-tab shows NJPW World / TrillerTV chips → `Roster` jump-tab → **AJ Styles** tile → profile
(TNA → NJPW/Bullet Club → WWE journey) → rail to *Bullet Club*, *Finn Bálor*, *Shinsuke Nakamura*.

**Path 3 — "Most-decorated Hall of Famer":**
Top tab **More** (mega panel) → **Hall of Fame** (`/hall-of-fame/`) → hero **Ric Flair (2×)** →
profile → rail to *Two-Time Club*, *2025 Class (Triple H)*, *Four Horsemen*.

Dropdown-panel contents (secondary nav under each tab) are enumerated in §8.

---

## 8. Master clickable → link-target table

Only targets that **exist today** are marked live; everything else is a **GAP** the design must
build (or render as a non-link "coming soon" tile so nothing 404s).

### 8.1 "Wrestlers" tab — mega panel (secondary nav)

| Control (label) | Target | Status |
|---|---|---|
| All Wrestlers A–Z | `/wrestlers/` | live (rebuild to 89) |
| Current | `/wrestlers/current/` | GAP (build) |
| Legends | `/wrestlers/legends/` | GAP (build) |
| Women's Division | `/wrestlers/women/` | GAP (build) |
| Attitude Era | `/wrestlers/eras/attitude-era/` | GAP (build, Tier 1) |
| Modern | `/wrestlers/eras/modern/` | GAP (build, Tier 1) |
| WWE / WWF | `/promotions/wwe/` | live |
| WCW | `/promotions/wcw/` | live |
| ECW | `/promotions/ecw/` | live |
| TNA / Impact | `/promotions/tna/` | live |
| NXT | `/promotions/nxt/` | live |
| NJPW | `/promotions/njpw/` | GAP — REQUIRED |
| AEW | `/promotions/aew/` | GAP — recommended |
| Featured: AJ Styles | `/wrestlers/aj-styles/` | live |
| Featured: Ric Flair | `/wrestlers/ric-flair/` | live |
| Featured: Roman Reigns | `/wrestlers/roman-reigns/` | live |
| Featured: Rhea Ripley | `/wrestlers/rhea-ripley/` | live |

### 8.2 `/wrestlers/` filter bar (§4.1 controls)

| Pill | Target (hub) | Control type | Status |
|---|---|---|---|
| Status: All | `/wrestlers/` | a | live |
| Status: Current | `/wrestlers/current/` | a | GAP |
| Status: Legends | `/wrestlers/legends/` | a | GAP |
| Division: Women | `/wrestlers/women/` | a | GAP |
| Division: Men | hash `#gender=men` | button | client-only |
| Promotion: WWE/WCW/ECW/TNA/NXT | `/promotions/{slug}/` | a | live |
| Promotion: NJPW | `/promotions/njpw/` | a | GAP |
| Promotion: AEW | `/promotions/aew/` | a | GAP |
| Era: Attitude / Modern | `/wrestlers/eras/{...}/` | a | GAP |
| Era: Golden / New Gen / Ruthless / PG | hash `#era={...}` | button | client-only |

### 8.3 "Events" tab panel + `/events/` sub-nav

| Control | Target | Status |
|---|---|---|
| All Events | `/events/` | live |
| 2026 | `/events/2026/` | GAP |
| WrestleMania | `/events/wrestlemania/` | live |
| Royal Rumble | `/events/royal-rumble/` | live |
| Elimination Chamber | `/events/elimination-chamber/` | live |
| Night of Champions | `/events/night-of-champions/` | live |
| Backlash | `/events/backlash/` | live |
| SummerSlam | `/events/summerslam/` | GAP |
| Survivor Series | `/events/survivor-series/` | GAP |
| Recent: WrestleMania 42 | `/events/wrestlemania-42-2026/` | live |
| Recent: Night of Champions 2026 | `/events/night-of-champions-2026/` | live |
| By promotion: NJPW / TNA / AEW | promotion events (hash/section) | GAP (only WWE has editions) |

### 8.4 "More" tab panel (routes the new hubs — see §9 nav note)

| Control | Target | Status |
|---|---|---|
| Hall of Fame | `/hall-of-fame/` | GAP — REQUIRED |
| Media & Creators | `/media/` | GAP — REQUIRED |
| Rivalries | `/rivalries/` | live |
| Relationships | `/relationships/` | live |
| Rankings | `/rankings/` | live |
| Promotions | `/promotions/` | live |
| Methodology | `/methodology/` | live |
| About | `/about/` | live |
| 中文 | `/zh/` | live |

### 8.5 `/hall-of-fame/` sub-nav + hero/strip

| Control | Target | Status |
|---|---|---|
| Most-Decorated (Ric Flair, 2×) | `/wrestlers/ric-flair/` | live |
| Two-Time: Shawn Michaels | `/wrestlers/shawn-michaels/` | live |
| Two-Time: Booker T | `/wrestlers/booker-t/` | live |
| Two-Time: Razor Ramon (Scott Hall) | `/wrestlers/razor-ramon/` | live |
| Two-Time: Kevin Nash | `/wrestlers/kevin-nash/` | live |
| Two-Time: Hulk Hogan | `/wrestlers/hulk-hogan/` | live |
| 2025 Class: Triple H | `/wrestlers/triple-h/` | live |
| 2025 Class: Lex Luger | `/wrestlers/lex-luger/` | live |
| 2024 Class: Paul Heyman | `/media/paul-heyman/` or `/wrestlers/paul-heyman/` | GAP |
| 2023 Class: Rey Mysterio | `/wrestlers/rey-mysterio/` | live |
| 2023 Class: The Great Muta | (page) | GAP |
| 2022 Class: The Undertaker | `/wrestlers/the-undertaker/` | live |
| 2022 Class: Vader | `/wrestlers/vader/` | live |
| 2021 Class: Kane | `/wrestlers/kane/` | live |
| 2021 Class: Eric Bischoff / RVD | (pages) | GAP |

### 8.6 `/media/` sub-nav + roster

| Control | Target | Status |
|---|---|---|
| Hero: Chris Van Vliet | `/media/chris-van-vliet/` | GAP — build first (HIGH) |
| Renee Paquette | `/media/renee-paquette/` | GAP + VERIFY |
| Peter Rosenberg | `/media/peter-rosenberg/` | GAP + VERIFY |
| Ariel Helwani | `/media/ariel-helwani/` | GAP + VERIFY |
| Sean Ross Sapp | `/media/sean-ross-sapp/` | GAP + VERIFY |
| Denise Salcedo | `/media/denise-salcedo/` | GAP + VERIFY |
| Dave Meltzer / Wade Keller | `/media/{slug}/` | GAP + VERIFY |
| (routing note) Sami Zayn | `/wrestlers/sami-zayn/` | live — NOT a media card |

### 8.7 `/promotions/{slug}/` in-page sub-nav (all slugs)

| Jump-tab | Anchor | Notes |
|---|---|---|
| Roster | `#roster` | faceted bar scoped to promotion |
| Events | `#events` | WWE live; NJPW/TNA/AEW gaps |
| Streaming | `#streaming` | "Where to watch" chips (§1 facts) |
| History | `#history` | prose |

---

## 9. Nav-bar note (top-tab count is the nav owner's call)

The chosen bar is **Wrestlers / Matches / Events / Moments / More + ⌘K + CTA**. Requirement 7 asks
for a Media/Influencers **tab**. To protect a fixed-width bar, this spec routes **Hall of Fame** and
**Media & Creators** into the **More** mega panel (§8.4) *and* gives each a first-class hub, a
homepage rail, and ⌘K entries — so they read as destinations without widening the bar. If the nav
owner prefers a literal 6th tab for **Media**, the sub-nav here is unchanged; only the panel's parent
moves. Recommendation: ship Media in **More** for launch, measure, and promote to a bar tab if it
earns the click. This mirrors the fixed-bar / work-the-sub-menu discipline used elsewhere in the
portfolio.

---

## 10. Interaction layers

- **Default:** all cards shown; each axis "All" active; count = total.
- **Hover (desktop):** tile lift + spotlight (existing `.tile:hover`); pill border → gold.
- **Active filter:** `.fbtn.is-active` uses the **hub accent** (§3.4), not always gold, so the bar
  echoes the wall's color.
- **Combined:** AND across axes; hash reflects non-default axes; count updates live.
- **Empty:** `.fb-empty` with two nearest single-axis escape links (never a dead end).
- **No-JS / crawler:** every Tier-1 pill is an `<a>` to a real page; the master shows all cards
  unfiltered; nothing depends on JS to be reachable.
- **Reduced motion:** honors existing `prefers-reduced-motion` block (no new animation introduced).
- **Mobile:** filter groups wrap; the bar becomes horizontally scrollable rows per axis; jump-tabs
  on promotion hubs become a sticky scrollable strip.

---

## 11. Gaps, dependencies, and VERIFY flags

- **Build (REQUIRED):** `/promotions/njpw/`, `/hall-of-fame/`, `/media/` (+ Chris Van Vliet),
  facet hubs `/wrestlers/current/`, `/legends/`, `/women/`; regenerate `/wrestlers/` to 89 cards
  with the new `data-*` schema; extend `js/main.js` filter (§4.2); append CSS tokens/classes (§3).
- **Build (recommended):** `/promotions/aew/`, `/events/2026/`, era hubs (Attitude, Modern),
  SummerSlam + Survivor Series series hubs.
- **Data dependency:** the **Championship** axis (F) needs title-reign front-matter that does not
  exist in the current `.md` data — **do not** ship championship hubs/pills until that data is
  authored and verified.
- **VERIFY (do not print until confirmed):** NJPW + AEW exact brand hex; AJ Styles 2026 retirement;
  media-roster affiliations beyond Chris Van Vliet; two-time HOF solo-induction years; WCW/ECW
  archive US streaming home. All per `00-content-data-research.md`.
- **Tag source of truth:** apply Axis A/B assignments from research §5; the ~13 women and the
  current/legend split are enumerated there. New batch slugs (asuka, bianca-belair, rhea-ripley,
  iyo-sky, liv-morgan, natalya, gunther, drew-mcintyre, damian-priest, la-knight, bobby-lashley,
  sheamus, and the added legends) map cleanly onto those lists; the build script assigns every one
  of the 89 slugs before render.
- **Cross-owner handoffs:** brand rename to "Wrestle Lore" and the mega-nav propagation to all
  sub-pages are the nav/rename owner's task; the streaming copy is the content owner's (§1); this
  spec consumes both.
