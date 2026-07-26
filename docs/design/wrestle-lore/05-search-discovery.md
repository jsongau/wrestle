# Wrestle Lore — Search & Discovery Spec (Search bar + ⌘K Command Palette v2)

Role: Search/discovery designer. This spec defines the header search pill, the ⌘K command palette v2
(scoped search, trending, recent, keyboard model, empty states), the search-index data shape, and how
search reinforces addictive browsing. It builds on the verified research in `00-content-data-research.md`
and `01-inspiration-research.md`, and stays consistent with the mega-nav (`03-mega-nav.md`) and homepage
(`02-homepage-architecture.md`) specs.

- Date: 2026-07-26
- Constraints honored: static, no build step, fully crawlable (nav links live in raw HTML, search is an
  enhancement layer only), **no browser storage** (no localStorage/sessionStorage/cookies), no fabricated
  facts, anti-AI copy standard (no decorative arrows in CTAs, no em-dash sentence separators, specific nouns).
- Current implementation to replace/extend: `js/search-index.js` (flat `{t,u,k}` array) and `js/nav.js`
  (the `#cmdk` overlay handler). Index global is renamed from `MAT_SEARCH_INDEX` to `WL_INDEX`.

Confidence legend: `HIGH` multiple sources / already built; `GAP` target page not built yet (has fallback);
`VERIFY` fact must be confirmed before publish.

---

## 1. Goals and the one non-negotiable

The search surface is not a utility bolted onto the corner. It is the fastest rabbit-hole entrance on the
site, and the highest-leverage discovery unit for people who arrive knowing a name (SEO landing traffic).
Three goals, ranked:

1. **Get a known-item seeker to the right page in under three keystrokes.** Type "flair", first result is
   Ric Flair, Enter lands the profile. This is the majority case and must feel instant.
2. **Turn a vague browser into a deep session.** When the box is empty or the query is thin, the palette is
   a discovery board: trending queries, browse-by-category facets, and jump-to hubs. Every empty state
   points at 6 to 10 obvious next clicks. Search never dead-ends, same rule as pages (`01` Part B2).
3. **Reinforce the taxonomy.** Scopes and facet chips are the same axes the poster wall uses (type, promotion,
   status, gender, era). Searching teaches the browse structure, and browsing teaches the search scopes.

The non-negotiable: **search is a progressive enhancement, never the only path to a page.** Every entity is
reachable through raw-HTML nav and hub links for crawlers and no-JS users. If `nav.js` fails to load, the
site is still fully navigable. The palette adds speed, not access.

---

## 2. Two surfaces, one index

| Surface | Where | Trigger | Purpose |
|---|---|---|---|
| **Header search pill** | Right-pinned in the sticky mega-nav bar, every page | Click / tap, or focus | Always-visible entry point; on desktop it is a real affordance that opens the palette, on mobile it is an icon button |
| **⌘K command palette** | Full-screen-dimmed centered overlay (`#cmdk`) | `⌘K` / `Ctrl+K`, `/`, click the pill, or any `[data-cmdk-open]` | The actual search + discovery board |

Both read one file, `js/search-index.js` (global `WL_INDEX`), plus a tiny curated `WL_DISCOVERY` block
(trending + browse links) defined inline in `nav.js`. No second network request; the index ships as a static
JS file the same way it does today.

### 2.1 Header search pill (the resting state)

- Desktop (>= 1080px): a pill button, Oswald 13px uppercase, label `Search`, a leading magnifier glyph, and a
  right-aligned keycap hint `⌘K` (render `Ctrl K` on non-Mac via a one-line UA check; if detection is skipped,
  default to `⌘K`). Height 36px, `border:1px solid var(--c-line-strong)`, `border-radius:var(--r-pill)`,
  background `var(--c-bg-elev-2)`, muted text. On hover the border shifts to `var(--c-gold-dim)` and the glyph
  to gold. Width ~200px so it reads as a search field, not a toolbar icon.
- 840 to 1079px: collapse to a 40px square icon button (magnifier only), keeps `aria-label="Search Wrestle Lore"`.
- < 840px: the icon button sits next to the hamburger; opening the palette is the mobile search experience
  (no separate search screen needed).
- Markup is a `<button type="button" data-cmdk-open aria-haspopup="dialog" aria-controls="cmdk">`. It is a
  button, not an input, so there is no accidental form submit and no duplicate focusable field.

### 2.2 The palette shell (`#cmdk`)

Reuse the existing `#cmdk` overlay id and class root `cmdk__*` so current pages keep working; extend markup.
Anatomy top to bottom:

```
┌──────────────────────────────────────────────── overlay (dim, blur) ┐
│  ┌───────────────────────────── panel (max 640px, centered, top 12vh) ┐ │
│  │ [🔎] [ input .cmdk__input                    ] [Esc]               │ │  ← search row
│  │ ─────────────────────────────────────────────────────────────────  │ │  ← gold hairline
│  │ [All][Wrestlers][Matches][Events][Promotions][HOF][Media][More]    │ │  ← scope tabs (type)
│  │ [WWE][WCW][ECW][TNA][NJPW][NXT] · [Current][Legend][Women][Men]    │ │  ← facet chip row (contextual)
│  │ ─────────────────────────────────────────────────────────────────  │ │
│  │  RESULTS list  .cmdk__results  (role=listbox)                       │ │
│  │   • grouped by type when scope = All                                │ │
│  │   • flat ranked list when a scope is active                         │ │
│  │  ── or ── EMPTY STATE (trending + browse) when query is blank       │ │
│  │  ── or ── NO-RESULTS panel (suggestions) when query has 0 hits      │ │
│  │ ─────────────────────────────────────────────────────────────────  │ │
│  │  footer: [↑↓ navigate] [↵ open] [tab switch scope] [esc close]      │ │  ← key legend
│  └────────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────┘
```

- Panel: `background:#0c0d10; border:1px solid var(--c-line-strong); border-top:2px solid var(--c-gold);
  border-radius:var(--r-lg); box-shadow:0 40px 90px rgba(0,0,0,.65); width:min(640px,92vw); margin:12vh auto 0.`
- The top rule is the "section token" (gold), same language as the mega-nav panels.
- Overlay: `background:rgba(6,7,9,.72); backdrop-filter:blur(6px);` click-outside closes.
- Search row: 56px tall, magnifier glyph left (gold when input focused), input fills, a small `Esc` chip right
  that also closes on click (touch users have no keyboard).

---

## 3. Scoped search: type scope + facet filter (two independent axes)

Scoping is the core v2 upgrade. Two independent filters combine with the text query.

### 3.1 Type scope (the tab row) — mirrors the 7-tab nav

`All` (default) · `Wrestlers` · `Matches` · `Events` · `Promotions` · `Hall of Fame` · `Media` · `More`.

- `All`: results grouped by type, each group capped at 5 with a `See all N wrestlers` group footer that sets
  the scope to that type (does not navigate). Group order: Wrestlers, Matches, Events, Promotions, Hall of
  Fame, Media, Rivalries, Moments, Pages.
- A single active scope: flat ranked list, cap 40, only that `type`.
- `Hall of Fame` scope draws from `type:"hof"` entries (classes + inductee records) and from wrestlers tagged
  `hof:true`. `Media` scope draws from `type:"media"`. Both are `GAP` until those pages exist; if the scope is
  active and its source pages are not built, show the built subset plus a single build-in-progress note that
  links to the interim hub (see §9 fallbacks). Never show a scope tab that would produce only 404 links.
- Scope tabs are Oswald 12px uppercase pills. Active tab: filled with the section token color (gold default,
  purple `--c-hof` for Hall of Fame, teal `--c-media` for Media). Inactive: `var(--c-text-muted)` on
  `var(--c-bg-elev-2)`.

### 3.2 Facet filter (the chip row) — the browse axes

A second row of chips filters within results by category, independent of the type scope. Chips are additive
within an axis (OR inside promotion, OR inside status) and intersect across axes (AND between promotion and
status), matching how faceted hubs read.

Axes and chips:

- **Promotion:** WWE · WCW · ECW · TNA · NJPW · NXT. Chip color = promotion accent (`chip--wwe` etc, already
  in CSS; add `chip--njpw`).
- **Status:** Current · Legend. `chip--current` (red), `chip--legend` (gold).
- **Division:** Women · Men. `chip--women` (magenta), `chip--men` (steel).
- **Era** (progressive disclosure, hidden behind a `+ Era` chip to avoid clutter): Golden 80s · New Gen ·
  Attitude · Ruthless Aggression · PG / Reality · Modern. Bronze `--c-era` family.

Facet visibility is contextual to the active type scope so the row never shows a meaningless filter:

| Type scope | Facets shown |
|---|---|
| All | Promotion + Status + Division (Era behind `+`) |
| Wrestlers | Promotion + Status + Division + Era |
| Matches | Promotion + Era |
| Events | Promotion + Year (2026 now; year chips are the by-year archive spine) |
| Promotions | none (six items, no facet needed) |
| Hall of Fame | Status implied; show Class-year chips (2021 to 2025) + Two-Time filter |
| Media | none for v1 (small roster) |
| More | none |

- A facet chip toggles on click and on `Space` when focused. Active chip is filled with its token color;
  inactive is outline in the token color at low chroma.
- Active facets render as a compact summary in the input placeholder area ("Wrestlers · NJPW · Current") so the
  user always sees the active constraint, and a single `Clear` text button resets all facets (not the query).
- Facets apply to the empty state too: choosing `NJPW` with a blank query shows the NJPW roster and the NJPW
  brand card as a curated result set, which is a discovery move, not just a filter.

### 3.3 Scope-by-prefix (power-user shorthand, optional layer)

Typing a known token followed by a space sets the scope, e.g. `w: ` (wrestlers), `m: ` (matches), `e: `
(events), `p: ` (promotions), `hof: `, `media: `. The prefix is consumed, the scope tab activates, and the
remaining text is the query. This is discoverable via a one-line hint in the empty state and is purely additive
over clicking the tabs. Keep it simple; do not overload with boolean operators.

---

## 4. Empty state: the discovery board (blank query)

This is where "addictive" is engineered. When the input is empty and no facet is set, the results area shows a
curated board, not nothing. Four stacked blocks, each a finishable rail (`01` B1/B3/B4):

1. **Recent (this visit only).** See §5 for the no-storage model. Rendered only if there is at least one
   in-memory recent item; otherwise this block is omitted (no empty shell).
2. **Trending searches.** 6 to 8 curated query chips maintained by hand in `WL_DISCOVERY.trending`. Clicking one
   fills the input and runs the search (it does not navigate), so the user sees ranked results and can keep
   drilling. Honest and editorial, no fake live counters (`01` B4). Proposed seed set below (all resolve to
   built pages; `VERIFY` any before publish):
   - `Ric Flair` · `WrestleMania 42` · `nWo` · `AJ Styles` · `Bloodline` · `Hell in a Cell` · `Royal Rumble` ·
     `Women's Division`
3. **Browse by category.** A grid of jump-to links (these DO navigate) that double as the taxonomy tour and the
   internal-linking backbone. Each is a colored chip using its axis token. Full targets in the §8 table.
   - Status: Current Stars, Legends. Division: Women's Division. Promotion: WWE, WCW, ECW, TNA, NJPW, NXT.
     Prestige: Hall of Fame. Crossover: Media & Creators. Rankings: Top Matches.
4. **Jump to** (static quick links): Wrestlers index, Matches index, Events, Rivalries, Moments, Promotions,
   Rankings, Membership. Small Oswald links, muted, gold on hover.

Copy note: block headers are plain nouns ("Trending", "Browse by category", "Jump to"). No exclamation, no
marketing adjectives, no arrows in the labels.

---

## 5. Recent searches under the no-storage constraint (design decision)

The constraint bans all browser storage, and the site is multi-page static, so each navigation reloads the
scripts and wipes any in-memory state. Therefore:

- **Recent is in-memory only, scoped to the current page's palette lifetime.** A module-level array in `nav.js`
  records the last 5 chosen results (or run queries) while the user opens and closes the palette on the same
  page. It resets to empty on every full page load. This is deliberate and honest: it helps within a single
  browsing burst (open palette, pick, reopen, refine) without pretending to persist history.
- **We do not fake cross-session history.** If the Recent array is empty (fresh page load), the block is simply
  not rendered, and the durable value lives in Trending + Browse-by-category, which are curated and always
  present. This keeps the empty state useful without storage.
- No cookies, no URL-param history, no fingerprinting. Documented here so a later engineer does not "fix" the
  missing persistence by reaching for localStorage and breaking the constraint.

---

## 6. No-results state (query with zero hits)

Never a bare "No matches". Show:

- Line 1: `No pages match "<query>".` (the query echoed, HTML-escaped).
- **Did you mean** row: up to 3 fuzzy suggestions computed by a cheap edit-distance / token-overlap pass over
  index titles and `aliases` (see §7). Clicking replaces the query. This catches "undertakr", "hbk", "hunter".
- **Try a category** row: the same Browse-by-category chips from the empty state, so a dead query still opens
  the rabbit hole.
- A single muted line: `Some pages are still being built.` shown only when the query matched a known `GAP` term
  (e.g. "Kenny Omega", "Chris Van Vliet") that is present as an alias pointing at an interim hub. In that case
  offer the interim hub link instead of a 404 (see §9).

Aliases carry most of the recall load, so the no-results state should be rare. That is the point: fund recall in
the index, not in an apology screen.

---

## 7. Search index data shape (the deliverable that unblocks build)

Replace the flat `{t,u,k}` objects with a richer, still-compact record. Keep keys short (this file ships to
every page). One array, one global `WL_INDEX`, generated from the page inventory by a small Python pass at
author time (same generation pattern as the existing `build_*` scripts).

### 7.1 Record schema

```js
// window.WL_INDEX = [ Entry, ... ]
// Entry:
{
  "t":  "Ric Flair",                 // title (display)               required
  "u":  "/wrestlers/ric-flair/",     // canonical url                 required
  "ty": "wrestler",                  // type (see enum)               required
  "st": "legend",                    // status: "current"|"legend"|"" (people only)
  "g":  "m",                         // gender: "m"|"f"|""            (people only)
  "pr": ["wwe","wcw","nwa","njpw"],  // promotion tags (accent axis)  0..n
  "er": ["golden","attitude"],       // era tags                      0..n
  "cat":["main-event","faction:four-horsemen","hof:2x"], // free category tags 0..n
  "a":  ["nature boy","naitch","16 time champion"],      // aliases / search-only synonyms
  "sub":"2x WWE Hall of Famer",      // one-line subtitle shown under the result title
  "b":  95                           // boost 0..100 (editorial prominence for tie-break/empty-state)
}
```

Field notes:
- `ty` enum: `wrestler` · `match` · `event` · `event-series` · `promotion` · `rivalry` · `moment` · `hof` ·
  `media` · `ranking` · `page`. (`event-series` = the brand hubs like `/events/royal-rumble/`; `event` = a dated
  edition like `/events/royal-rumble-2026/`. Distinguishing them lets the Events scope offer year facets.)
- `st`, `g` only populated for `wrestler` (and `media` where meaningful); empty string otherwise so the object
  stays small.
- `pr` uses the promotion token slugs that map 1:1 to accent tokens: `wwe wcw ecw tna nxt njpw` (plus
  `nwa aew roh` as needed for cross-tags; only `wwe wcw ecw tna nxt njpw` drive chip colors, others are
  search-only). Multi-promotion is expected and desirable (Sting = `["wcw","tna","wwe","nwa"]`).
- `cat` is the catch-all for browse lanes not covered by the fixed axes: divisions (`women`, `tag-team`,
  `cruiserweight`), factions (`faction:nwo`, `faction:bullet-club`, `faction:the-shield`), and HOF flags
  (`hof:2008`, `hof:2x`). Namespacing with `:` keeps them parseable.
- `a` (aliases) is the recall engine: nicknames ("The Phenomenal One"), initials ("hbk", "ddp"), gimmick names
  ("Prince Devitt" for Finn Balor), and common misspellings you choose to seed. Aliases are searched but not
  displayed as the title.
- `b` (boost) drives tie-breaking and the empty-state "Browse by category" ordering (highest-boost members of a
  facet lead). Editorial, derived, clearly not a fabricated stat, never shown as a number to users.

### 7.2 Generation rules (author-time Python)

- Source of truth is the existing per-entity `.md` front-matter already used by `build_*` scripts. Add the axis
  fields (`status`, `gender`, `promotions`, `eras`, `categories`, `aliases`, `subtitle`, `boost`) to
  front-matter; the generator emits `WL_INDEX`. Where front-matter is missing an axis, emit empty, do not guess.
- Persona/alias PAGES that are the same human (e.g. `mean-mark-callous`, `the-ringmaster`,
  `stunning-steve-austin`, `diesel`, `razor-ramon`) get `ty:"wrestler"` but a low `b` and an `a` cross-ref to
  the canonical, OR are folded in as aliases on the canonical entry to avoid duplicate-person clutter. Decision:
  keep them as their own low-boost entries (they are real pages that should be findable) and add the canonical
  name to their `a` so "Kevin Nash" also surfaces "Diesel".
- `vince-mcmahon` gets `ty:"page"` / category `personality`, kept out of the Wrestlers scope default ranking
  (it appears under More / a personality filter), per `00` §5.
- Every generated `u` must resolve to a built page at publish time. The generator runs a link-existence check
  and fails loudly on any `u` that 404s, except entries explicitly marked `gap:true` which are excluded from the
  shipped index and instead added to the alias-to-interim-hub map (see §9). This guarantees no result row 404s.

### 7.3 Size / performance

- ~169 pages, expect ~200 to 260 entries with aliases. At these key lengths the minified file is well under
  60KB, acceptable as a blocking-free `defer` script. No lazy loading needed. If it later crosses ~150KB, split
  into `wl-index-core.js` (people/promotions/HOF, loaded on every page) and a lazy `wl-index-deep.js` (matches/
  moments/rivalries) fetched on first palette open. Not required for v1.

---

## 8. Ranking / scoring model (extends current `score()`)

Keep the current tiered scoring and add alias + boost + facet awareness. For a query `q` (lowercased, trimmed)
against entry `it`:

1. Exact title match: 100. Title starts-with `q`: 85. Alias exact: 80. Alias starts-with: 70.
2. Any title token starts-with `q`: 60. Title contains `q`: 50. Alias contains `q`: 40. Subtitle/category
   contains: 25.
3. Multi-word query: split on space, require every term to match somewhere (title/alias/sub/cat) with AND;
   sum per-term best tier, then average, so "aj styles njpw" ranks the AJ Styles page even though "njpw" is a
   `pr` tag not in the title.
4. Add `+ (b/100)*8` boost so, on ties, prominent entries win (Ric Flair over a low-boost persona page).
5. Type-scope and facet filters are applied as a hard pre-filter before scoring (an entry that fails the active
   facet is dropped, not down-ranked).
6. Empty query: order by `b` desc within each group (this is what makes the grouped empty/`All` view show the
   marquee names first).

Cap: 40 results per scope, 5 per group in `All`. Debounce input handling at 60ms (typeahead feel, no jank).

---

## 9. GAP handling and interim fallbacks (no 404 from search, ever)

The mega-nav and homepage specs mark these targets as `GAP`. Search must not surface a raw link to an unbuilt
page. Rules:

| Target | State | Search behavior until built |
|---|---|---|
| `/promotions/njpw/` | GAP (high priority) | If built, index normally. If not yet built, the `NJPW` browse chip and any "njpw" query route to `/promotions/` with a note; NJPW-tied wrestlers (AJ Styles, Nakamura, Moxley, Finn Balor) still surface normally |
| `/wrestlers/current/`, `/legends/`, `/women/`, `/men/` | GAP | Browse chips point to these; until built, fall back to `/wrestlers/` (the master index carries client-side facet pills). Alias map redirects the query to the fallback |
| `/hall-of-fame/` and inductee-less classes | GAP | HOF scope + browse chip point to `/hall-of-fame/` once built; interim fallback `/rankings/`. Class anchors (`#2024`) only emitted after the hub exists |
| `/media/`, `/media/chris-van-vliet/` | GAP | Media scope + chip hidden until `/media/` and at least the Van Vliet page exist (mega-nav §5.6 rule). No teal chip that 404s |
| Kenny Omega, Will Ospreay, Paul Heyman, Great Muta, Bischoff, RVD, McCool | GAP (no page) | Held in an `aliases-to-hub` map, NOT in `WL_INDEX`. A query hits the no-results "still being built" line and offers the nearest built hub (e.g. Kenny Omega -> `/promotions/njpw/` or `/promotions/aew` fallback `/promotions/`) |

The `gap:true` entries live in a separate `WL_GAP_HINTS` object in `nav.js` (query-term -> interim url + short
label). This keeps the shipped `WL_INDEX` 404-free while still catching high-intent queries for content that is
promised but not yet built.

---

## 10. Keyboard and interaction model (full)

Global (document-level, from `nav.js`):
- `⌘K` / `Ctrl+K`: open palette (prevent default browser behavior). Works from anywhere except inside an input.
- `/`: open palette, only when focus is not in an input/textarea/select (current behavior, keep).
- These bind once; guard against double-binding if `nav.js` loads twice.

Inside the palette:
- Typing: filters live (60ms debounce).
- `ArrowDown` / `ArrowUp`: move active row; wraps; `scrollIntoView({block:"nearest"})`. Active row is visually
  highlighted and set `aria-selected="true"`.
- `Enter`: navigate to active row's `u`. If a Trending chip / group footer is active (a "run query" action, not
  a link), Enter runs that action instead of navigating.
- `Tab` / `Shift+Tab`: cycle the type-scope tabs (does not leave the palette). This makes scoping keyboard-first.
  `Shift+Tab` on the first scope returns focus to the input.
- `Alt+1..8`: jump directly to scope N (All=1 ... More=8). Power-user shortcut, listed in the footer legend on
  hover only, not shouted.
- `Space` on a focused facet chip toggles it; facet chips are in the tab order after the scope tabs.
- `Backspace` on an empty input with active facets removes the last facet (email-recipient-chip pattern).
- `Escape`: if facets or a scope are active, first `Escape` clears them back to `All`/no-facet; second `Escape`
  closes. If nothing is active, `Escape` closes. (Two-stage escape prevents accidental loss of a typed query.)
- Mouse/touch: click row navigates; click chip toggles; click scope switches; click `Esc` chip or outside
  closes.

Accessibility:
- Overlay `role="dialog" aria-modal="true" aria-label="Search Wrestle Lore"`. Input
  `role="combobox" aria-expanded aria-controls="cmdk-results" aria-activedescendant="<active row id>"`.
- Results `role="listbox" id="cmdk-results"`; rows `role="option"` with stable ids `cmdk-opt-<i>`.
- Focus trap inside the panel while open; on close, return focus to the element that opened it (the pill).
- `prefers-reduced-motion`: skip the panel rise/fade, show/hide instantly. Respect it for chip transitions too.
- Every color-coded chip also carries a text label, so color is never the only signal (WCAG 1.4.1).
- Touch targets >= 44px for chips and rows on the mobile layout.

---

## 11. Result row anatomy and color rules

Row (`.cmdk__row`, `role=option`), left to right:
- **Type badge** (`.cmdk__kind`): Oswald 10px uppercase, colored by the section token of its type, not the
  promotion. `wrestler` gold-neutral, `match` red, `event`/`event-series` gold, `promotion` its own accent,
  `hof` purple `--c-hof`, `media` teal `--c-media`, `rivalry`/`moment` muted. Fixed 84px column so titles align.
- **Title** (`.cmdk__title`): Inter/`--font-sans` 15px, `--c-text`, matched substring wrapped in `<mark>`
  (gold underline highlight, not a yellow block).
- **Subtitle** (`.cmdk__sub`): the entry `sub`, `--c-text-muted` 12px, single line, ellipsis.
- **Facet dots** (right): up to 3 tiny 8px dots colored by the entry's promotion tokens, plus a status pip
  (red current / gold legend) and a magenta pip for women's-division entries. This is the one-second parse
  (`01` A3): a user sees "gold pip = legend, blue dot = TNA" before reading. Dots are decorative; the row's
  accessible name is the title + type + subtitle, dots are `aria-hidden`.

Color rules (single source, all tokens already defined in `css/site.css` per homepage spec §):
- Section tokens: default gold `--c-gold`; HOF `--c-hof` (#6b46c1 per mega-nav) ; Media `--c-media` (#2dd4bf).
- Promotion accents: `--c-wwe #c8102e` · `--c-wcw #e2b13c` · `--c-ecw #b0b0b0` · `--c-tna #1e73be` ·
  `--c-nxt #f5c518` · `--c-njpw #c1272d` (VERIFY vs official NJPW branding before lock).
- Status/division tokens: `--c-current #e11d2a` · `--c-legend #d4af37` · `--c-women #d6398a` · `--c-men` steel.
- Active scope tab and the palette top rule take the active scope's section token, so entering the Hall of Fame
  scope turns the palette purple and Media turns it teal. This is the same "color does more work" rule the
  mega-nav uses, applied to search.
- One accent per context: a row shows its type badge color OR promotion dots, never a rainbow. The scanline/
  duotone poster treatment is not used inside the palette (kept lightweight and fast).

---

## 12. How search reinforces addictive browsing (the loop)

- **Every result row is a rabbit-hole entrance**, and every destination page ends in a "Keep going" block, so
  search -> page -> 6 more links is the core loop (`01` B2). Search seeds the loop; pages sustain it.
- **Trending chips run queries, not navigations**, so a curious click lands the user in a ranked result set
  they can keep filtering, which is stickier than dumping them on one page.
- **Browse-by-category chips are the taxonomy tour.** They teach the axes (promotion/status/division) that the
  poster wall and the facet chips share, so the search UI and the browse UI reinforce one mental model.
- **Facets turn search into faceted browse.** Blank query + `NJPW` + `Current` is a curated poster set, which is
  the same value a `/wrestlers/current/` hub gives, reachable in two keystrokes from any page.
- **GEO payoff:** the index's alias + category coverage is also the answer-engine surface. The same
  `subtitle`/`aliases` that boost recall are the phrasings people ask AI engines ("who is the Nature Boy", "2x
  WWE Hall of Famer"), and the JSON-LD on the destination pages (`01` Part C) makes the landing citable. Search
  recall and GEO citability are funded by the same field.

---

## 13. Table of every clickable in the search surfaces -> link target

Result rows are dynamic (their `u` comes from `WL_INDEX`, guaranteed non-404 by §7.2). The table below covers
the FIXED chrome clickables (header pill, scope tabs, facet chips, empty-state discovery, footer, no-results),
which are the load-bearing internal links. `run` = fills input and runs a query (no navigation). `nav` =
navigates. Fallbacks apply while a target is `GAP`.

| # | Surface | Clickable label | Action | Target (or fallback) | State |
|---|---|---|---|---|---|
| 1 | Header bar | Search pill / icon | open palette | `#cmdk` (dialog) | HIGH |
| 2 | Palette | Esc chip | close | — | HIGH |
| 3 | Scope tab | All | set scope | (filter only) | HIGH |
| 4 | Scope tab | Wrestlers | set scope + facets | (filter) / index `/wrestlers/` on "see all" | HIGH |
| 5 | Scope tab | Matches | set scope | (filter) / `/matches/` on "see all" | HIGH |
| 6 | Scope tab | Events | set scope | (filter) / `/events/` on "see all" | HIGH |
| 7 | Scope tab | Promotions | set scope | (filter) / `/promotions/` on "see all" | HIGH |
| 8 | Scope tab | Hall of Fame | set scope | (filter) / `/hall-of-fame/` on "see all" | GAP -> `/rankings/` |
| 9 | Scope tab | Media | set scope | (filter) / `/media/` on "see all" | GAP -> hidden until built |
| 10 | Scope tab | More | set scope | (filter over `ty:page`/rivalry/moment) | HIGH |
| 11 | Facet chip | WWE | toggle facet | filter `pr:wwe` | HIGH |
| 12 | Facet chip | WCW | toggle facet | filter `pr:wcw` | HIGH |
| 13 | Facet chip | ECW | toggle facet | filter `pr:ecw` | HIGH |
| 14 | Facet chip | TNA | toggle facet | filter `pr:tna` | HIGH |
| 15 | Facet chip | NJPW | toggle facet | filter `pr:njpw` | HIGH (roster tagged; hub GAP) |
| 16 | Facet chip | NXT | toggle facet | filter `pr:nxt` | HIGH |
| 17 | Facet chip | Current | toggle facet | filter `st:current` | HIGH |
| 18 | Facet chip | Legend | toggle facet | filter `st:legend` | HIGH |
| 19 | Facet chip | Women | toggle facet | filter `g:f` | HIGH |
| 20 | Facet chip | Men | toggle facet | filter `g:m` | HIGH |
| 21 | Facet chip | + Era (Golden/New Gen/Attitude/Ruthless/PG/Modern) | toggle facet | filter `er:*` | HIGH |
| 22 | Facet row | Clear | reset facets | (keeps query) | HIGH |
| 23 | Empty: Trending | Ric Flair | run | query "Ric Flair" -> row `/wrestlers/ric-flair/` | HIGH |
| 24 | Empty: Trending | WrestleMania 42 | run | -> `/events/wrestlemania-42-2026/` | HIGH |
| 25 | Empty: Trending | nWo | run | -> `/matches/nwo-formation-bash-at-the-beach-1996/` + `/rivalries/nwo-invasion/` | HIGH |
| 26 | Empty: Trending | AJ Styles | run | -> `/wrestlers/aj-styles/` | HIGH |
| 27 | Empty: Trending | Bloodline | run | -> `/rivalries/the-bloodline/` | HIGH |
| 28 | Empty: Trending | Hell in a Cell | run | -> HIAC moments/matches set | HIGH |
| 29 | Empty: Trending | Royal Rumble | run | -> `/events/royal-rumble/` + 2026 | HIGH |
| 30 | Empty: Trending | Women's Division | run | scope Wrestlers + facet `g:f` | HIGH |
| 31 | Empty: Browse | Current Stars | nav | `/wrestlers/current/` | GAP -> `/wrestlers/` |
| 32 | Empty: Browse | Legends | nav | `/wrestlers/legends/` | GAP -> `/wrestlers/` |
| 33 | Empty: Browse | Women's Division | nav | `/wrestlers/women/` | GAP -> `/wrestlers/` |
| 34 | Empty: Browse | WWE | nav | `/promotions/wwe/` | HIGH |
| 35 | Empty: Browse | WCW | nav | `/promotions/wcw/` | HIGH |
| 36 | Empty: Browse | ECW | nav | `/promotions/ecw/` | HIGH |
| 37 | Empty: Browse | TNA | nav | `/promotions/tna/` | HIGH |
| 38 | Empty: Browse | NJPW | nav | `/promotions/njpw/` | GAP -> `/promotions/` |
| 39 | Empty: Browse | NXT | nav | `/promotions/nxt/` | HIGH |
| 40 | Empty: Browse | Hall of Fame | nav | `/hall-of-fame/` | GAP -> `/rankings/` |
| 41 | Empty: Browse | Media & Creators | nav | `/media/` | GAP -> hidden |
| 42 | Empty: Browse | Top Matches | nav | `/rankings/` | HIGH |
| 43 | Empty: Jump to | Wrestlers | nav | `/wrestlers/` | HIGH |
| 44 | Empty: Jump to | Matches | nav | `/matches/` | HIGH |
| 45 | Empty: Jump to | Events | nav | `/events/` | HIGH |
| 46 | Empty: Jump to | Rivalries | nav | `/rivalries/` | HIGH |
| 47 | Empty: Jump to | Moments | nav | `/moments/` | HIGH |
| 48 | Empty: Jump to | Promotions | nav | `/promotions/` | HIGH |
| 49 | Empty: Jump to | Rankings | nav | `/rankings/` | HIGH |
| 50 | Empty: Jump to | Membership | nav | `/membership/` | HIGH |
| 51 | No-results | Did you mean <suggestion> | run | replaces query | HIGH |
| 52 | No-results | (Browse chips, same as 31-42) | nav | as above | mixed |
| 53 | No-results | still-being-built hub link | nav | interim hub from `WL_GAP_HINTS` | GAP-aware |
| 54 | Group footer (All scope) | See all N <type> | set scope | (switches scope to that type) | HIGH |

Recent block rows (when present, in-memory only) navigate to the stored `u`, same as result rows; not tabulated
because they are dynamic.

---

## 14. Build notes and file changes

- `js/search-index.js`: regenerate with the §7 schema; rename global `MAT_SEARCH_INDEX` -> `WL_INDEX`. Add the
  Python generator step to the existing `build_*` pipeline (reads front-matter, runs the §7.2 link-existence
  check, emits minified JS). Keep a back-compat shim line `window.MAT_SEARCH_INDEX = window.WL_INDEX;` for one
  release if any page still references the old name, then remove.
- `js/nav.js`: extend the `#cmdk` handler with scope tabs, facet chips, empty-state board, no-results panel,
  alias-aware scoring, `WL_DISCOVERY` (trending + browse) and `WL_GAP_HINTS` constants, and the §10 keyboard
  model. Guard against double-init. Keep zero dependencies and zero storage.
- `css/site.css`: add `chip--njpw`, `chip--current`, `chip--legend`, `chip--women`, `chip--media` (most already
  specced in homepage §), plus `cmdk__scope`, `cmdk__facets`, `cmdk__sub`, `cmdk__dots`, `cmdk__group`,
  `cmdk__empty-board`, `cmdk__noresults`. Reduced-motion and 44px touch rules included.
- Rename: all palette copy, the pill `aria-label`, and the dialog `aria-label` say "Wrestle Lore" (req 8).
- Every `#cmdk` markup block already present on the 169 pages needs the new inner rows; since there is no build
  step for HTML, add the scope/facet/footer markup to the shared header partial used by the `build_*` scripts
  and regenerate, or inject the extra rows from `nav.js` at runtime (progressive enhancement) so old static
  pages upgrade without a full re-render. Prefer runtime injection for the palette internals (keeps HTML small,
  guarantees consistency); keep only the outer `#cmdk` shell + `.cmdk__input`/`.cmdk__results` in static HTML.

## 15. Acceptance checklist

1. `⌘K`, `Ctrl+K`, `/`, and the pill all open the palette; `Esc` closes; focus returns to the pill.
2. Typing "flair" makes Ric Flair the first row; Enter navigates to `/wrestlers/ric-flair/`.
3. "hbk" (alias) surfaces Shawn Michaels; "the phenomenal one" surfaces AJ Styles.
4. Scope tabs filter by type; `Tab` cycles them; `Alt+1..8` jumps.
5. Facet chips filter (WWE + Current shows only current WWE wrestlers); `Clear` resets; two-stage `Escape`.
6. Blank query shows Trending + Browse + Jump to; no Recent block on fresh load; no storage written (verify in
   devtools Application tab: nothing set).
7. Every fixed clickable in §13 resolves to a built page or its documented fallback; zero 404s from search.
8. No result row links to a `GAP` page; GAP-intent queries hit the no-results hub hint.
9. Reduced-motion honored; all chips have text labels; listbox/combobox ARIA present; 44px touch targets.
10. Media scope/chip is hidden until `/media/` + Van Vliet exist; NJPW roster searchable even while the hub is a
    fallback.

---

## Sources
Builds on `00-content-data-research.md` (streaming, HOF, NJPW, media, taxonomy, gap list) and
`01-inspiration-research.md` (Cagematch faceted model, Letterboxd rabbit-hole linking, Transfermarkt badge/
color system, Netflix rails, keep-going blocks, JSON-LD/GEO). Token values reconciled with `02-homepage-
architecture.md` §(color tokens) and `03-mega-nav.md` §3-4. No new external facts introduced; any
promotion-color or roster fact carried here retains its upstream `VERIFY` flag.
