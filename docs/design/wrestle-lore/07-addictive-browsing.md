# Wrestle Lore — Addictive Browsing & Retention System

Engagement/retention-designer deliverable for the Direction-B "Editorial Poster Wall" revamp. This
spec designs the layer that turns a database into a rabbit hole: mandatory next-links, themed related
rails, a no-storage "because you viewed" surface, honest trending, gamified collection/completion
cues, and dwell-time hooks. Every mechanic here is also an internal-linking move, so retention and
SEO/GEO are the same work (pattern C in `01-inspiration-research.md`).

- Date: 2026-07-26. Author: engagement/retention design.
- Builds on and does not re-derive: `00-content-data-research.md` (facts, slugs, gaps),
  `01-inspiration-research.md` (patterns B1–B7, C), `04-subnav-taxonomy.md` (axes, tags, facet hubs,
  color/badge tokens), `05-search-discovery.md` (⌘K). Facts are the research docs' source of truth;
  anything unverified is flagged `VERIFY`.
- Hard constraints honored: static, no build step, **fully crawlable** (every rail item and next-link
  is a raw `<a href>`, never JS-rendered), **no browser storage** (no localStorage/sessionStorage/
  cookies; in-memory + `document.referrer` + URL hash only), root-absolute paths, one stylesheet
  (`css/site.css`), vanilla JS. Anti-AI copy standard: no decorative arrows in CTAs, no em-dash
  sentence separators, no banned marketing words, specific nouns.

## 0. Ownership boundary (what this doc owns vs. its neighbors)

- `04-subnav-taxonomy.md` owns the **filter bar, facet hubs, badges, and axis color tokens**. This
  doc **consumes** those tokens and adds only engagement-specific ones (§6).
- `05-search-discovery.md` owns **⌘K search**. This doc adds the **zero-result and idle-search
  fallbacks** that feed browsing (§4.6), nothing else in search.
- This doc owns the **post-content engagement stack**: the Keep-going block, related rails, the
  referrer rail, trending, collection/completion cues, the session trail, and dwell hooks — plus the
  **front-matter fields** that generate them (§8) and the **clickable → target table** (§10).

---

## 1. The retention model (five loops, ranked by leverage)

1. **Never dead-end (the spine).** Every page ends in a mandatory "Keep going" block of 4–6
   contextual next-links. This is the #1 retention lever and the backbone of the internal-link graph.
2. **Rail-stacking (the discovery unit).** Above Keep-going, each entity page carries 1–3 themed
   horizontal rails ("More from WCW", "Same rivalry", "Rematch"), each a small finishable promise
   that invites the next click.
3. **Sideways continuity (no-storage personalization).** A "Because you came from …" rail derived
   from `document.referrer` (not storage) keeps the thread when a user arrives from another entity,
   and an in-memory **session trail** shows the path taken this visit.
4. **Curiosity + completion (gamified, content-derived).** Trending rails, ranked leaderboards, and
   collection/completion meters computed from the **database** (not user history), so the
   completionist pull works with zero login and zero storage.
5. **Dwell hooks (time-on-page).** Expandable Lore, CSS hover previews, pull-facts, and a scroll
   progress rail lengthen each stop so the next rail is reached, not bounced past.

Every loop resolves to more `<a href>` edges between canonical pages. Same hub-spoke links serve the
crawler and the rabbit-holer (pattern C1).

---

## 2. Universal page skeleton (where engagement sits)

Below the entity's own content, every entity page (`wrestler`, `match`, `event`, `moment`,
`rivalry`, `promotion`, `hof-class`, `media`) ends with a fixed engagement stack, in this order:

```
… entity content (bio / result / card / prose) …
[ FAQ block ]                         (SEO/GEO; owned by content, kept here for order)
[ RAIL 1 — primary related ]          themed, entity-type recipe §5, .rail
[ RAIL 2 — secondary related ]        (optional; only if the recipe fills it)
[ BECAUSE-YOU-CAME-FROM strip ]       JS-injected from referrer; hidden if empty (§4.3)
[ COLLECTION / COMPLETION panel ]     entity-type recipe §5 (wrestler trophy case, rivalry meter)
[ KEEP GOING block ]                  mandatory, 4–6 typed next-links (§4.1) — always last content
[ SESSION TRAIL ]                     JS-injected "Your path this visit"; hidden if <2 hops (§4.4)
[ site footer ]
```

Rules: the **Keep-going block is mandatory and always the last content section**; rails are additive
above it. Referrer strip and session trail are progressive enhancement — they render only when JS +
data exist and are **never** the only path to a page (crawlers still get the static rails + Keep
going). Order is fixed site-wide so returning users learn where "what's next" lives (pattern B7
restraint).

---

## 3. The horizontal rail (core component)

One reusable rail, used for every themed row. Extends the existing `.grid-spot` + `.tile` poster
system (already in `css/site.css`) with a scroll-snap track so it reads as a finishable row on
mobile and a wrapped grid on desktop.

### 3.1 Markup (crawlable: every item is an `<a>`)

```html
<section class="section--tight rail-sec" data-reveal aria-labelledby="rail-wcw">
  <div class="wrap">
    <div class="section-head">
      <div><p class="eyebrow">More from WCW</p>
           <h2 id="rail-wcw">The WCW shelf</h2><hr class="rule-gold"></div>
      <a class="link-more" href="/promotions/wcw/">All WCW</a>
    </div>
    <ul class="rail" role="list">
      <li><a class="tile tile--gold" href="/wrestlers/sting/" data-seed="212">
        <span class="tile__media"><span class="tile__mono">S</span><span class="tile__spot"></span></span>
        <span class="chip chip--wcw tile__badge">WCW</span>
        <span class="tile__body"><span class="tile__kicker">WCW · New Gen</span>
          <span class="tile__name">Sting</span></span></a></li>
      <!-- 5–10 more items -->
    </ul>
  </div>
</section>
```

### 3.2 CSS to add to `css/site.css`

```css
.rail{list-style:none;margin:0;padding:0 0 var(--sp-2);display:flex;gap:var(--sp-4);
  overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;
  scrollbar-width:thin;scrollbar-color:var(--c-line-strong) transparent;}
.rail>li{flex:0 0 clamp(150px,42vw,200px);scroll-snap-align:start;}
.rail>li>.tile{height:100%;}
@media (min-width:64rem){                 /* desktop: wrap into a dense grid, no scroll */
  .rail{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));overflow:visible;}
}
.rail::-webkit-scrollbar{height:8px;}
.rail::-webkit-scrollbar-thumb{background:var(--c-line-strong);border-radius:99px;}
.rail-sec+.rail-sec{padding-top:0;}       /* stack rails tight, Netflix-style */
.rail-sec .link-more{white-space:nowrap;} /* "All WCW" never wraps */
```

- **Item budget:** 6–12 per rail. Fewer than 4 valid items = drop the rail (an empty rail reads as
  broken). More than 12 = the last tile becomes a "See all N →text-only" `.tile--more` linking the
  source hub, so the rail promises completion.
- **Reduced motion / no-JS:** the rail is pure CSS scroll + links; nothing depends on JS. Honors the
  existing `prefers-reduced-motion` block (no new animation).

---

## 4. Engagement components

### 4.1 Keep-going block (mandatory, the spine)

Replaces the current ad-hoc `<h2>Related</h2>` + `.related-links` with a **typed, slotted** block so
every page reliably points sideways, backward, and forward. 4–6 links, each labeled by relation type.

```html
<nav class="keepgoing" aria-label="Keep going">
  <p class="eyebrow">Keep going</p>
  <ul class="keepgoing__list">
    <li class="kg kg--rematch"><a href="/matches/bret-hart-vs-austin-wm13/">
        <span class="kg__rel">The prequel</span>
        <span class="kg__t">Bret Hart vs Austin, WrestleMania 13</span></a></li>
    <li class="kg kg--person"><a href="/wrestlers/the-rock/">
        <span class="kg__rel">Wrestler</span><span class="kg__t">The Rock</span></a></li>
    <li class="kg kg--rivalry"><a href="/rivalries/rock-vs-austin/">
        <span class="kg__rel">The rivalry</span><span class="kg__t">Rock vs Austin</span></a></li>
    <li class="kg kg--event"><a href="/events/wrestlemania/">
        <span class="kg__rel">The event series</span><span class="kg__t">WrestleMania</span></a></li>
    <li class="kg kg--rank"><a href="/rankings/">
        <span class="kg__rel">Leaderboard</span><span class="kg__t">The Five-Star Club</span></a></li>
  </ul>
</nav>
```

Slot recipe per entity type (fill 4–6; skip a slot only if no valid target exists):

| Slot | Relation | Source field |
|---|---|---|
| 1 | **Sideways peer** (same promo/era/division) | `related[]` or generated from shared tags |
| 2 | **A named person** on the page | `people[]` / participants |
| 3 | **The connecting story** (rivalry/faction) | `rivalries[]` |
| 4 | **Up a level** (event series / promotion / era hub) | `parentSeries` / `promo[0]` |
| 5 | **A leaderboard or collection** | fixed per type (`/rankings/`, `/hall-of-fame/`) |
| 6 | **The rematch / next chapter** (matches, events) | `rematchOf` / `nextEdition` |

CSS:

```css
.keepgoing{border-top:1px solid var(--c-line);margin-top:var(--sp-7);padding-top:var(--sp-5);}
.keepgoing__list{list-style:none;margin:var(--sp-3) 0 0;padding:0;display:grid;gap:var(--sp-2);
  grid-template-columns:repeat(auto-fit,minmax(min(240px,100%),1fr));}
.kg a{display:grid;gap:.15em;padding:var(--sp-3) var(--sp-4);background:var(--c-bg-elev-1);
  border:1px solid var(--c-line);border-left:3px solid var(--c-line-strong);border-radius:var(--r-md);
  text-decoration:none;color:var(--c-text);transition:border-color var(--dur) var(--ease);}
.kg a:hover{border-color:var(--c-line-strong);border-left-color:var(--kg-accent,var(--c-gold));}
.kg__rel{font-family:var(--font-cond);text-transform:uppercase;letter-spacing:.06em;
  font-size:var(--fs-300);color:var(--c-text-dim);}
.kg__t{font-family:var(--font-cond);font-size:var(--fs-500);text-transform:uppercase;letter-spacing:.01em;}
/* the left rule is colored by relation type so the block parses in one second */
.kg--rematch{--kg-accent:var(--c-red);} .kg--person{--kg-accent:var(--c-gold);}
.kg--rivalry{--kg-accent:var(--c-red-bright);} .kg--event{--kg-accent:var(--c-focus);}
.kg--rank{--kg-accent:var(--c-gold-bright);}
```

No CTA verbs, no arrows — the relation label is the affordance (anti-AI copy standard). Every
Keep-going link is a plain `<a>`, so it is the crawler's primary deep-path and the reader's next hop
at once.

### 4.2 Themed related rails (per §3, content per §5)

Generated at author time from front-matter. Each rail's eyebrow states the exact relation ("Same
rivalry", "5-star matches", "Also from 2001") so the promise is specific, not "You might like".

### 4.3 "Because you came from …" strip (no-storage personalization)

The honest, storage-free version of Netflix's "Because you watched". On load, JS reads
`document.referrer`; if it is a same-origin entity page, it injects one strip that (a) offers a clear
return link and (b) shows a short rail related to **that** referrer entity, pulled from a small
JSON map (`/data/graph.json`, generated at build from front-matter — already the same relatedness the
static rails use).

- **Input:** `document.referrer` only (a read, not storage). No cookies, no localStorage.
- **Behavior:** parse referrer path → look up its node in `graph.json` → render "Because you came
  from **Rock vs Austin**" + 4 tiles of that node's `related[]` (minus the current page).
- **Fallback / privacy:** if referrer is empty, cross-origin, or the same page, **render nothing**
  (the section stays `hidden`). No layout shift beyond the reveal; container reserves no space.
- **Crawlable:** this strip is JS-only by design and never a sole path — every target it could show
  is already reachable via the static rails and Keep-going, so crawlers lose nothing.

```html
<section class="section--tight came-from" hidden data-camefrom
         data-map="/data/graph.json" aria-label="Because you came from another page">
  <div class="wrap"><div class="section-head">
    <div><p class="eyebrow">Because you came from</p>
      <h2 data-cf-title></h2><hr class="rule-gold"></div>
    <a class="link-more" data-cf-back href="#">Back to it</a></div>
    <ul class="rail" data-cf-rail role="list"></ul>
  </div>
</section>
```

### 4.4 Session trail ("Your path this visit")

An in-memory multi-hop breadcrumb of the current visit, with **no storage**. The trail is carried in
the **URL hash** across hops (`#from=rock-vs-austin,the-rock`), read into memory on load, and never
written to disk. It shows where the user has been this session and lets them jump back.

- On a Keep-going / rail click, JS appends the current page's slug to a `from` list and writes it to
  the destination link's hash before navigation (`history` untouched on the source page).
- On load, JS reads `location.hash` `from=` into an in-memory array, renders the trail, then
  `history.replaceState`s the hash away so it never pollutes Back or the shareable URL. Canonical is
  unaffected (hash is non-indexable; already the rule in `04` §2).
- Hidden until ≥2 hops. Capped at 6 (drops oldest) to bound URL length.
- Honest framing: it is "your path this visit", not a saved history. When the tab is closed it is
  gone, because nothing is stored — state this in the label's `title`.

```html
<nav class="trail" hidden data-trail aria-label="Your path this visit">
  <span class="trail__lead">Your path this visit</span>
  <ol class="trail__list"><!-- JS fills: Home › Rock vs Austin › The Rock › (here) --></ol>
</nav>
```

### 4.5 Trending / "This week in Wrestle Lore" (honest, editorial)

A homepage + hub rail of hand-picked items, ranked, with **no fake live counters** (anti-cliché
standard). Two truthful signals only:

- **Trending** = an editorially ordered list set by hand in one file (`/data/trending.md` front-
  matter → rendered into the homepage rail at author time). Order implies popularity; no numbers
  invented.
- **Recently added** = real, from build metadata (page `mtime` / a `dateAdded` field). This is
  factual and safe to label "Added this week".

Optional per-tile flags, both honest: `.flag--rising` (gold, editorial "climbing") and
`.flag--new` (red, from real build date). Rendered as the existing `.tile` with a corner flag; reuse
`.tile__badge` slot. Trending rail uses the standard `.rail`.

### 4.6 Search-to-browse fallbacks (feeds ⌘K into rails)

Owned jointly with `05`: when ⌘K returns **zero results**, show a "Nothing for '{q}'. Start here"
panel of 4 evergreen hubs (Legends, Women, Hall of Fame, Trending) — never a dead end. When the
palette opens with **no query**, seed it with the current Trending list so the empty state is a
browse surface, not a blank box. (Implementation lives in `05`; this is the retention requirement.)

### 4.7 Collection / completion cues (gamified, content-derived, no user state)

Completion is computed from the **database**, not the user — so the completionist pull works with no
login and no storage. Two forms:

- **Wrestler "Trophy Case".** A shelf of accolade badges on the profile: title reigns, 5-star
  matches catalogued, HOF status, faction memberships — filled (gold) when present, dim when not.
  Reuses `.chip`/`.mark--hof` tokens from `04` §3. It reframes the existing champ/record data as a
  collectible set and links each filled badge to the proof (a match, the HOF hub, a faction page).
- **Set-completion meter.** On a rivalry/series/promotion hub: "6 of 6 matches catalogued", "You've
  reached the end of WCW events". A simple filled bar (reuse `.mb-track`/`.mb-fill` from the method
  bars). It measures **catalogue** completeness (honest) and gives the "did I see them all?" pull
  (pattern B5). Never implies the user's own progress.

```html
<div class="collect">
  <p class="eyebrow">Career collection</p>
  <ul class="collect__case">
    <li><a class="chip chip--gold" href="/matches/styles-vs-daniels-vs-joe-unbreakable-2005/">5★ match</a></li>
    <li><a class="chip mark--hof" href="/hall-of-fame/">Hall of Fame</a></li>
    <li><span class="chip chip--dim" aria-disabled="true">World title: none</span></li>
  </ul>
</div>
```

```css
.chip--dim{color:var(--c-text-dim);background:transparent;border-color:var(--c-line);}
.collect__case{list-style:none;display:flex;flex-wrap:wrap;gap:.5rem;padding:0;margin-top:var(--sp-2);}
```

### 4.8 Dwell-time hooks (time-on-page, all CSS/native)

- **Expandable Lore** (`<details class="lore">`): origin stories, gimmick histories, kayfabe-vs-real
  notes collapsed by default. Opening one is a free micro-interaction that keeps the user on-page and
  leans into the "Lore" brand. Native `<details>`, no JS.
- **CSS hover preview on tiles** (pattern B6): on `.tile:hover` reveal a compact overlay (rating +
  promo + one signature fact) via the existing `.tile__spot`; on mobile the fact sits under the tile.
  No JS, stays crawlable.
- **Pull-facts** ("Did you know"): a styled `.pullfact` aside seeded from a verified `facts[]`
  front-matter field. Only verified facts; anything flagged `VERIFY` is omitted, not shown.
- **Scroll progress rail:** a 2px top bar tied to scroll depth (existing enhance.js reveal
  infrastructure; add a `requestAnimationFrame` scroll handler, no storage). Signals "there's more
  below", pulling the reader toward the rails at the bottom.

---

## 5. Per-entity rail recipes (what each page gets)

Each recipe lists the rails (in order), their source field, and the Keep-going slots. Rails render
only when they have ≥4 valid items; otherwise the relation folds into Keep-going.

| Entity | Rail 1 | Rail 2 | Collection panel | Keep-going emphasis |
|---|---|---|---|---|
| **Wrestler** `/wrestlers/{slug}/` | "Signature matches" (from `matches[]`) | "Rivals & allies" (from `rivalries[]`+`allies[]`) | Trophy Case (§4.7) | peer wrestler, a rivalry, a promotion hub, a facet hub (Legends/Women), a leaderboard |
| **Match** `/matches/{slug}/` | "Both wrestlers" (participants) | "Same rivalry" or "Also from {year}" | 5★ badge + "rated" | the rematch (`rematchOf`), the rivalry, the event, `/rankings/` |
| **Event edition** `/events/{series}-{year}/` | "On this card" (matches) | "This series" (other editions) | streaming badge + "N matches rated" | the series hub, the year hub `/events/2026/`, a headline wrestler, `/events/` |
| **Event series** `/events/{series}/` | "Editions" (year list) | "Best matches from {series}" | set meter "N editions" | year hub, another series, promotions, `/events/` |
| **Moment** `/moments/{slug}/` | "The people involved" | "More moments" (type-matched) | — | the wrestler, the match/event it happened at, `/moments/`, a rivalry |
| **Rivalry** `/rivalries/{slug}/` | "The matches" (bouts) | "Both wrestlers" | **set meter** "6 of 6 matches" | each wrestler, the promotion, `/rivalries/`, `/relationships/` |
| **Promotion** `/promotions/{slug}/` | "Top wrestlers" (roster) | "Events" / "Where to watch" (streaming chips §00) | roster count meter | another promotion, a facet hub, `/promotions/`, an event series |
| **HOF class** `/hall-of-fame/{year}/` | "This class" (inductees) | "Other classes" | class-completion note | most-decorated (Ric Flair), `/hall-of-fame/`, an inductee, Two-Time Club |
| **Media** `/media/{slug}/` | "More creators" | "Wrestlers they've interviewed" (only where pages exist) | — | `/media/`, a wrestler, a promotion, Trending |

Sourcing note: all rail contents come from the **front-matter fields in §8**; the build script emits
static `<a>` tiles. Nothing is invented at runtime. Where a target page is a gap (per `00`/`04`), the
tile renders **non-linked** with a "profile in progress" note (never a 404) — the same rule `04` §5.3
uses for HOF.

---

## 6. Color rules (engagement layer)

Reuse all axis tokens from `04-subnav-taxonomy.md` §3 (promotion accents, `--c-status-current` red,
`--c-status-legend` gold, `--c-women` magenta, `--c-njpw`, `--c-aew`, `--c-hof`). Add only these
engagement tokens to `:root`:

```css
--c-trend:var(--c-red);            /* trending / heat = red flame            */
--c-rising:var(--c-gold-bright);   /* editorial "climbing"                   */
--c-new:var(--c-red-bright);       /* "added this week" (real build date)    */
--c-came-from:var(--c-focus);      /* referrer strip accent = cool blue      */
```

Rules that keep the wall legible (pattern B7 restraint):

1. **Rails inherit the page's hub accent.** On a hub with a body class (`hub--legend`, etc., from
   `04` §3.4), the rail eyebrow rule and `link-more` use that accent, so a related rail feels native
   to the page it sits on. On entity pages the default is gold.
2. **Relation type colors the Keep-going left-rule only** (§4.1) — one small colored edge per card,
   never a full fill, so five relation types coexist without noise.
3. **Trending/heat is the only place red-as-flame appears**, so "hot" reads instantly and is never
   confused with the CURRENT-status red pill (different shape: flame flag vs. status pill).
4. **The referrer strip uses `--c-came-from` blue** to signal "off your main path / a sidebar
   suggestion", matching the media/press-box blue from `04` so blue always means "meta layer".
5. **Collection: filled = gold, empty = `--c-text-dim` on transparent.** The gap between a lit and an
   unlit badge is the completionist tension; no third color needed.

Max **one** engagement accent visible per section besides the entity's own promotion chips.

---

## 7. Interaction layers

- **Default (no JS / crawler):** static rails, Keep-going, collection panel, and expandable Lore all
  render as raw HTML `<a>`/`<details>`. Every next-hop is reachable. Referrer strip and session trail
  are simply absent. This is the crawlable, guaranteed floor.
- **Hover (desktop):** tile lift + `.tile__spot` preview (existing); Keep-going card lights its
  relation-colored left rule; `link-more` underlines. No layout shift.
- **Scroll:** `data-reveal` fade-rise on rails as they enter (existing IntersectionObserver in
  `enhance.js`); 2px scroll-progress bar advances (§4.8).
- **On load with JS:** parse `document.referrer` → maybe show came-from strip (§4.3); parse
  `#from=` → maybe show session trail (§4.4), then `replaceState` the hash away.
- **On next-hop click (JS):** append current slug to the destination's `#from=` before navigation so
  the trail survives one hop without storage.
- **Reduced motion:** all reveals/progress collapse to instant via the existing
  `prefers-reduced-motion` block; scroll-progress bar still updates position (no transition).
- **Mobile:** rails become horizontal scroll-snap tracks (§3.2); Keep-going grid collapses to one
  column; came-from strip shows 2 tiles instead of 4; trail truncates with a leading "…".
- **Keyboard:** rails are a `role="list"` of links (native tab order); scroll-snap does not trap
  focus; `link-more` is reachable first so keyboard users get "see all" before scanning tiles.

---

## 8. Data model — front-matter fields that generate the engagement layer

Add these optional fields to each entity's `.md` front-matter. The build script reads them to emit
rails, Keep-going, the trophy case, and `/data/graph.json` (which powers the referrer strip). All are
plain slug lists; the script resolves slug → title/accent, and renders any unresolved slug as a
non-link "in progress" tile.

```yaml
# common to all entities
related:    [slug, slug, ...]   # sideways peers (same promo/era/division). Fills Rail 1 + KG slot 1.
people:     [slug, ...]         # named wrestlers/creators on the page. KG slot 2.
rivalries:  [slug, ...]         # connecting stories/factions. Rail 2 + KG slot 3.
facts:      ["verified fact", ...]  # pull-facts (§4.8). VERIFY-flagged facts excluded.
# wrestler
matches:    [slug, ...]         # signature matches → Rail 1
allies:     [slug, ...]         # → "Rivals & allies" rail
accolades:  {five_star: [match-slug], hof: true|"2x", titles: [name], factions: [slug]}  # Trophy Case
# match
participants: [slug, slug]      # → "Both wrestlers"
event:      slug                # → the event edition
rematchOf:  slug|null           # → KG "the rematch" slot 6
# event edition
series:     slug                # parent series → KG slot 4
year:       2026                # → year hub
card:       [match-slug, ...]   # → "On this card"
# event series
editions:   [slug, ...]         # → "Editions" rail + set meter
# rivalry
bouts:      [match-slug, ...]   # → "The matches" rail + "N of N" set meter
# promotion
roster:     [slug, ...]; events:[slug, ...]; streaming:[{label, region}]  # §00 facts, verbatim
```

Single source of truth: `related[]` also feeds the graph node used by the referrer strip, so
authoring one field powers three surfaces (static rail, Keep-going, came-from). `/data/graph.json` is
a build artifact, not hand-authored.

---

## 9. JavaScript spec (append to `js/main.js` / `js/enhance.js`; ~70 lines, no deps, no storage)

1. **Referrer strip** (`enhance.js`): on DOMContentLoaded, if `document.referrer` is same-origin and
   its path is a known entity, `fetch('/data/graph.json')` (cached by HTTP only), look up the node,
   render up to 4 `related` tiles minus the current slug, un-`hidden` the section, set the back link.
   Empty/cross-origin referrer → leave `hidden`. One `fetch`, no storage.
2. **Session trail** (`main.js`): read `location.hash` `from=` into an in-memory array; if length ≥2,
   render `.trail__list` and un-`hidden`; then `history.replaceState(null,'',location.pathname)` to
   drop the hash. Bind a delegated click handler on `.keepgoing a, .rail a` that, before navigation,
   appends the current page slug to a `from` list (cap 6) and rewrites the clicked link's `href` hash.
3. **Scroll progress** (`enhance.js`): one `rAF`-throttled scroll listener sets `--scroll` on a
   `.progress` bar; no storage, respects reduced motion.
4. **Trending / recently-added**: fully static (built from `/data/trending.md` and build `mtime`); no
   runtime JS needed.

All three degrade to nothing without JS; none read or write any Web Storage or cookie (constraint
honored). Reuse the existing IntersectionObserver for rail reveals — do not add a second observer.

---

## 10. Master clickable → link-target table

Only targets that **exist today** are "live"; gaps are marked and must render as non-link "in
progress" tiles (never a 404), per `00`/`04`. Slugs verified against the live `/wrestlers/`,
`/matches/`, `/rivalries/`, `/events/`, `/moments/`, `/promotions/` directories.

### 10.1 Keep-going block — worked example: match `Rock vs Austin, WM X-Seven`

| Slot | Label | Target | Status |
|---|---|---|---|
| Rematch/prequel | "The prequel" | `/matches/bret-hart-vs-austin-wm13/` | live |
| Person | "Wrestler" | `/wrestlers/the-rock/` | live |
| Person | "Wrestler" | `/wrestlers/stone-cold-steve-austin/` | live |
| Rivalry | "The rivalry" | `/rivalries/rock-vs-austin/` | live |
| Event series | "The event series" | `/events/wrestlemania/` | live |
| Leaderboard | "The Five-Star Club" | `/rankings/` | live |

### 10.2 Wrestler rails + Keep-going — worked example: `AJ Styles` (the NJPW showcase, req 5)

| Control | Rail / slot | Target | Status |
|---|---|---|---|
| Styles vs Daniels vs Joe | Signature matches | `/matches/styles-vs-daniels-vs-joe-unbreakable-2005/` | live |
| Shinsuke Nakamura | Rivals & allies | `/wrestlers/shinsuke-nakamura/` | live |
| Finn Bálor (Prince Devitt) | Rivals & allies / Bullet Club | `/wrestlers/finn-balor/` | live |
| Jon Moxley | Rivals & allies | `/wrestlers/jon-moxley/` | live |
| NJPW | Keep-going: promotion | `/promotions/njpw/` | **GAP — REQUIRED (build)** |
| Bullet Club | Keep-going: faction | `/relationships/#factions` or faction page | GAP (faction page) |
| Trophy Case: IWGP title | collection badge | `/promotions/njpw/` | GAP target |
| Trophy Case: 5★ (Unbreakable) | collection badge | `/matches/styles-vs-daniels-vs-joe-unbreakable-2005/` | live |

### 10.3 Trending rail (homepage) — proposed launch set (all live)

| Tile | Target | Flag |
|---|---|---|
| WrestleMania 42 (2026) | `/events/wrestlemania-42-2026/` | new (real date) |
| Ric Flair — most-decorated HOF | `/wrestlers/ric-flair/` | rising (editorial) |
| Rock vs Austin, WM X-Seven | `/matches/rock-vs-austin-wm-x-seven-2001/` | — |
| The Bloodline | `/rivalries/the-bloodline/` | rising (editorial) |
| Hall of Fame | `/hall-of-fame/` | **GAP — REQUIRED** |
| AJ Styles | `/wrestlers/aj-styles/` | — |

### 10.4 Collection / leaderboard destinations (fixed)

| Cue | Target | Status |
|---|---|---|
| "The Five-Star Club" (from any 5★ match/trophy) | `/rankings/` | live |
| "Hall of Fame" (from HOF trophy badge) | `/hall-of-fame/` | GAP — REQUIRED |
| "The web / everything connected" (rivalry set meter) | `/relationships/` | live |
| Legends facet (Keep-going sideways) | `/wrestlers/legends/` | GAP (per `04`) |
| Women's facet (Keep-going sideways) | `/wrestlers/women/` | GAP (per `04`) |

### 10.5 Referrer strip & session trail (JS-injected)

| Element | Target logic | Status |
|---|---|---|
| Came-from title/back link | `document.referrer` path (same-origin only) | live (JS) |
| Came-from tiles | `graph.json[referrerSlug].related[]` | needs `/data/graph.json` build artifact |
| Trail hops | `#from=` slug list → each `/…/{slug}/` | live (JS); all targets are canonical pages |

---

## 11. Gaps, dependencies, and VERIFY flags

- **Build (REQUIRED for engagement layer):** append §3/§4 CSS classes and §6 tokens to `css/site.css`;
  add the referrer-strip + session-trail + scroll-progress JS (§9); generate `/data/graph.json` from
  front-matter; author `/data/trending.md`; add the §8 front-matter fields to entity `.md` files and
  re-run the build scripts so every page emits its rails + Keep-going block.
- **Depends on other owners:** the facet hubs (`/wrestlers/legends/`, `/women/`, `/current/`),
  `/promotions/njpw/`, `/hall-of-fame/`, `/media/`, `/events/2026/` are `04`'s builds; this doc's
  rails/Keep-going **link into** them and must render their tiles non-linked until they exist. Brand
  rename to "Wrestle Lore" and mega-nav propagation are the nav owner's task.
- **Data dependency:** the Trophy Case's title-reign badges need reign data; champ rows already exist
  on some profiles (e.g. AJ Styles) but not uniformly. Ship the case with the badges that have data;
  do not fabricate reigns for profiles lacking them.
- **VERIFY (do not print until confirmed, per `00`):** AJ Styles 2026 retirement (keep him CURRENT,
  no retrospective framing); NJPW/AEW brand hex; two-time HOF solo years; media-roster affiliations
  beyond Chris Van Vliet; WCW/ECW archive US streaming home. Any `VERIFY` fact is **excluded** from
  pull-facts and rail copy until cleared.
- **Honesty rule (anti-cliché standard):** trending is editorial-ordered with no invented counts;
  "recently added" uses real build dates only; completion meters measure the **catalogue**, never a
  user's history; no "X people viewing now" style fake signals anywhere.
