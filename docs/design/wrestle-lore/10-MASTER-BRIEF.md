# Wrestle Lore — MASTER BRIEF (authoritative synthesis of specs 00–09)

Lead design-director deliverable. This is the single source of truth for the Wrestle Lore revamp. It
reconciles the eight design specs and two research docs in this folder, resolves every conflict
between them with a named decision, and hands the build team one IA, one color system, one set of
component/link mappings, one gap list, and one phased build order.

- Date: 2026-07-26. Supersedes conflicting instructions in specs 02–09 where a **DECISION** below says
  so; on any point not overridden here, the originating spec remains the detailed source.
- Ground truth verified against `/root/wwe/` on 2026-07-26: **89** wrestler dirs, **30** matches,
  **15** rivalries, **5** promotions (wwe, wcw, ecw, tna, nxt — **no njpw**), **10** events (5 PPV
  editions + 5 series hubs), **4** moments; the `/wrestlers/` index still renders **41** of 89 cards;
  the search global is still `MAT_SEARCH_INDEX`; the brand string "MAT" still appears in page headers.
- Hard constraints (non-negotiable, from PROJECT): static, no build step, fully crawlable (every nav
  and section link is a raw `<a href>`, never JS-rendered), one stylesheet `css/site.css`, vanilla JS,
  **no browser storage** (in-memory + `document.referrer` + URL hash only), root-absolute asset paths,
  no fabricated facts/quotes/stats (flag `VERIFY`), anti-AI copy standard (no decorative arrows in
  CTAs, no em-dash sentence separators, no banned marketing words, specific nouns).

---

## 0. Conflicts resolved (read this first — these are director decisions)

The specs disagree on five points. These decisions are binding; everything downstream follows them.

| # | Conflict | Specs in tension | **DECISION** |
|---|---|---|---|
| D1 | **Top-tab count.** 02 keeps the 5-tab bar (Wrestlers/Matches/Events/Moments/More); 03 grows to 7 tabs; 04 routes HOF+Media into "More" to protect a fixed bar. | 02 vs 03 vs 04 | **Ship the 7-tab bar from spec 03: Wrestlers · Matches · Events · Promotions · Hall of Fame · Media · More, plus a right-pinned ⌘K pill.** Requirement 7 explicitly asks for a Media *tab* and reqs 4/6 make Promotions and Hall of Fame first-class showcases. Moments folds into the **More** panel (only 4 items) and keeps its own `/moments/` index. The bar is then a **fixed 7-tab instrument** — do not add an 8th; new content routes into an existing panel or a hub sub-menu. This supersedes spec 02 §1.1 and spec 04 §9's "route into More" recommendation. |
| D2 | **Nav CTA.** 02 puts a red "Join Wrestle Lore" pill in the bar; 06 retires it. | 02 vs 06 | **Follow spec 06: no loud nav CTA.** The bar ends at the ⌘K pill. Membership moves to a quiet "Insider" text item in the **More** panel, an ambient footer join line, and the in-content conversion layers (§7). This supersedes spec 02 clickable rows 13/14 and the `.nav__cta` red pill in `css/site.css`. Rationale: a reference/catalog site converts better on higher-intent moments than on a persistent bar ask. |
| D3 | **NJPW accent hex.** Proposed as #c1272d (02, 05), #d21c1c (03, 09), #c8102e (04 — collides with WWE), #d81f26 (08). All `VERIFY`. | 02/03/04/05/08/09 | **Canonical `--c-njpw:#d81f26` (spec 08, the visual-systems authority; carries the WCAG math).** Reject #c8102e outright (identical to WWE). The hex stays `VERIFY` against official NJPW branding; **differentiation from WWE/site-red is by pairing, not hue** — NJPW tiles carry a unique white rising-sun overlay + 1px white top rule (spec 08 §2.3). |
| D4 | **Media accent = teal or purple.** 02/03/05/09 say teal (#1fb6c4 / #2dd4bf); 08 says purple #a855f7; 04 uses focus-blue. | 08 vs rest | **Canonical `--c-media:#a855f7` (purple), per spec 08.** Teal and focus-blue both sit in the same hue family as TNA blue (#1e73be), the focus ring (#5aa9ff), and the "came-from" blue, which breaks the one-second parse on a wall. Purple is cleanly distinct. This supersedes the teal value in 02/03/05/09; the token name `--c-media` is unchanged, so only the value moves. |
| D5 | **Hall of Fame accent = purple or gold.** 03/05/09 say royal purple #6b46c1; 08 says warmer gold #e8b923. | 08 vs rest | **Canonical `--c-hof:#e8b923` (warm gold), per spec 08.** HOF's badge shape is a **gold plaque** (`.badge-hof`), semantically "immortal/prestige"; gold is the natural read and keeps purple reserved solely for Media (avoids two purples). This supersedes the purple HOF value in 03/05/09. HOF sections theme with `.theme-hof` (gold), paired with the existing `--c-gold` for hairlines. |

Two consequences of D4+D5 worth stating plainly: **purple = Media only; gold family = Legend + Hall of
Fame** (disambiguated by shape — Legend is a gold hairline pill, HOF is a gold plaque). This is the
spec-08 "color family may repeat because shape encodes the axis" rule, applied at the system level.

---

## 1. Vision

Wrestle Lore is the most searchable, most cross-linked pro-wrestling database and review network on the
web, and a working membership-growth funnel — built as a portfolio artifact for a WWE/TKO Manager,
Membership Growth application. It wins on three fronts at once, because they are the same structure seen
three ways:

1. **Catalog depth as the pitch.** A dense, colorful "Editorial Poster Wall" (Direction B) where every
   tile parses in one second: color encodes category, shape encodes the axis. The wall itself proves the
   catalog is huge, organized, and alive.
2. **A rabbit hole that never dead-ends.** Every page ends in a mandatory "Keep going" block and carries
   themed related rails, so a visit becomes a deep session. The same hub-and-spoke `<a>` graph that
   drives retention is the internal-linking backbone for SEO and the citation surface for AI answer
   engines (GEO).
3. **A funnel that rides intent, not interruption.** No loud nav CTA. Membership is captured at
   demonstrated-intent moments (deep sessions, end-of-rail, event nights), gating only secondary value
   and never a crawlable fact.

Editorial standard: no invented facts, quotes, or stats; every uncertain claim ships `VERIFY` or not at
all. "Lore" invites the deep-dive framing — origin stories, gimmick histories, kayfabe-vs-real notes as
a first-class content flavor.

---

## 2. Final IA / sitemap and category taxonomy

### 2.1 Top-level sitemap (canonical directories)

```
/                                  home (poster wall, 12 blocks §5)
/wrestlers/                        master A–Z (rebuild 41 → 89 cards, faceted bar)
/wrestlers/current/                status=current            [GAP build — Wave 1]
/wrestlers/legends/                status=legend             [GAP build — Wave 1]
/wrestlers/women/                  gender=women              [GAP build — Wave 1]
/wrestlers/men/                    gender=men (client hash fallback; page optional — Wave 3)
/wrestlers/eras/                   era hub index             [GAP build — Wave 2]
/wrestlers/eras/{attitude-era,modern,...}/   era spokes      [GAP — Wave 2, Attitude+Modern first]
/wrestlers/{slug}/                 89 profiles (exist)
/matches/                          master (exist) + light facet bar
/matches/{slug}/                   30 rated matches (exist)
/events/                           master (exist) + series/year/promotion facets
/events/2026/                      year hub                  [GAP build — Wave 2]
/events/{series}/                  5 series hubs exist; add summerslam, survivor-series [GAP — Wave 3]
/events/{series}-{year}/           5 PPV editions (exist)
/promotions/                       brand-card hub (rebuild flat grid → brand cards)
/promotions/{wwe,wcw,ecw,tna,nxt}/ exist (add in-page Roster/Events/Streaming/History anchors)
/promotions/njpw/                  NJPW brand + streaming    [GAP build — Wave 1, REQUIRED req 5]
/promotions/aew/                   AEW brand (cross-link)    [GAP build — Wave 2, recommended]
/hall-of-fame/                     HOF hub                   [GAP build — Wave 1, REQUIRED req 6]
/hall-of-fame/{2021..2025}/        per-class pages (optional Tier-2 — Wave 3)
/media/                            Media & Creators hub      [GAP build — Wave 1, REQUIRED req 7]
/media/{slug}/                     creator pages             [GAP — Wave 1 hero, rest Wave 2]
/rivalries/  /relationships/  /rankings/  /moments/  /methodology/  /membership/  /about/  /zh/   (exist)
```

**URL rules (spec 04 §2, binding):** directories are the canonical indexable surface; combined/Tier-2
filter state lives in `location.hash` (shareable, non-indexable, no storage); `?q=` is search-only and
canonicalizes to the index; **no `?promo=` query facets** (they create thin duplicates); one canonical
page per entity — rosters live on `/promotions/{slug}/`, never `/wrestlers/{promo}/`.

### 2.2 The six-axis wrestler taxonomy (spec 04 §1, binding)

Every wrestler card carries `data-*` on six orthogonal axes; the same tags drive tile badges, filter
pills, and pre-rendered hubs. Tag assignment per slug comes from research doc 00 §5.

| Axis | Attribute | Values | Drives |
|---|---|---|---|
| A. Status | `data-status` | `current` \| `legend` | red/gold status pill; `/current/`, `/legends/` |
| B. Gender/Division | `data-gender` | `women` \| `men` | magenta women's marker; `/women/` |
| C. Promotion | `data-promo` | `wwe wcw ecw tna nxt njpw` (+ `aew nwa roh` search-only) | promotion accent; `/promotions/{slug}/` |
| D. Era | `data-era` | `golden new-gen attitude ruthless pg modern` | era tag (kicker text); era hubs |
| E. Division/role | `data-div` | `main-event womens tag cruiserweight faction` | division pill; faction cross-links |
| F. Accolade | `data-badge` | `hof hof-2x champion five-star` | gold plaque/diamond; HOF hub |

Exclusions (binding): persona/alias pages (`mean-mark-callous`, `the-american-badass`, `the-ringmaster`,
`stunning-steve-austin`, `diesel`, `razor-ramon`) are `data-alias="true"` — kept crawlable and in ⌘K, but
**off the poster walls**. `vince-mcmahon` is `data-role="executive"` — More panel / Personalities only,
never the athlete grid. **Sami Zayn is an active wrestler** — stays on the wrestler grid, never on Media.

**Hub tiers:** Tier-1 (own directory, canonical, `ItemList` JSON-LD, sitemap) for high-value facets
(current, legends, women, per-promotion, HOF, media, events-by-year, events-by-series). Tier-2
(client-only `<button>`, hash state) for everything below ~12 members (men, most eras, tag/cruiserweight/
faction, championship). The **Championship axis is blocked** until title-reign front-matter exists — do
not ship championship hubs/pills on fabricated data.

---

## 3. Color system and tokens (canonical — spec 08 as authority + D3/D4/D5)

Governing rule: **SHAPE encodes the axis, COLOR encodes the category**, on a 4-tier loudness order (one
dominant promotion accent per tile). Two categories may share a hue family because shape disambiguates.

### 3.1 Add to `:root` in `css/site.css` (additive only — no existing hex changes)

```css
/* NEW promotion accent (D3) */
--c-njpw:#d81f26;  --c-njpw-bright:#ff4a4f;  --c-njpw-tint:rgba(216,31,38,.14);  --c-njpw-sun:#fff; /* VERIFY hex */
--c-aew:#c8a24a;   /* RESERVED, text cross-links only until /promotions/aew/ ships; VERIFY */

/* status aliases */
--c-current:var(--c-red);   --c-current-bright:var(--c-red-bright);   --c-current-tint:var(--c-red-tint);
--c-legend:var(--c-gold);   --c-legend-bright:var(--c-gold-bright);   --c-legend-tint:var(--c-gold-tint);

/* division */
--c-womens:#e0409f; --c-womens-bright:#f26bbb; --c-womens-dim:#8f2464; --c-womens-tint:rgba(224,64,159,.14); /* D4-adjacent */
--c-mens:#8593a6;   --c-mens-tint:rgba(133,147,166,.12);

/* section themes (D4, D5) */
--c-hof:#e8b923;  --c-hof-bright:#ffd24a; --c-hof-deep:#7a5c12; --c-hof-tint:rgba(232,185,35,.14);  /* warm gold */
--c-media:#a855f7;--c-media-bright:#c084fc;--c-media-dim:#6b21a8; --c-media-tint:rgba(168,85,247,.14); /* purple */
--c-moment:var(--c-red-bright); --c-moment-tint:var(--c-red-tint);

/* era bands (muted, Tier 3) */
--c-era-golden:#c9a35b; --c-era-newgen:#9bb0c4; --c-era-attitude:#d0563f;
--c-era-ruthless:#7f8fa6; --c-era-pg:#6f9f8f; --c-era-modern:#b9c2cf;

/* themeable accent hook (defaults to gold, so existing rules render identically) */
--accent:var(--c-gold); --accent-bright:var(--c-gold-bright); --accent-dim:var(--c-gold-dim);
--accent-tint:var(--c-gold-tint); --accent-on:#000;

/* engagement tokens (spec 07) */
--c-trend:var(--c-red); --c-rising:var(--c-gold-bright); --c-new:var(--c-red-bright); --c-came-from:var(--c-focus);
```

### 3.2 Themeable accent scopes (spec 08 §4)

`[data-promo="wwe|wcw|ecw|tna|nxt|njpw"]` and `.theme-hof/.theme-moments/.theme-media/.theme-current/
.theme-legends/.theme-women` each remap `--accent*`. Refactor `.tile__media` gradient, `.tile:hover`
ring, `.tile__mono`, `.tile__spot`, `.tile__kicker`, `.section-head h2` underline, `.eyebrow`, rail
header rule, and `.btn--ghost:hover` to read `--accent`. One scope recolors a whole subtree.

### 3.3 Badge grammar (shape = axis; spec 08 §5)

Status = **pill** (current: red tint + pulsing dot; legend: gold hairline). Division = **squared chip**
(women's magenta; men's steel). Promotion = **color-bar tag** (3px left bar in accent). HOF = **gold
plaque** (`.badge-hof`, `--2x` variant for Ric Flair). Moment = **▸ play tag** (red). Era = **plain
condensed text** (muted band). Rating = **corner number** (existing). Streaming = **text chip**
(`.chip--stream`, never a logo). **Max two graphic badges per tile** (promotion chip top-left + one
right-corner marker in priority `hof-2x > hof > status > women`); era and secondary promotions live in
the kicker text.

### 3.4 WCAG AA (spec 08 §3, binding two rules)

1. Never set **body text** in `--c-red`, `--c-wwe`, `--c-tna`, or `--c-njpw` (all sub-4.5:1 on
   `--c-bg`); use the `-bright` variant for text or reserve those hexes for fills/large display.
2. Pair each solid chip fill with its documented text color: **dark text** on gold/wcw/nxt/womens/media/
   mens/hof; **white text** on wwe/tna/njpw. Focus ring stays `--c-focus #5aa9ff`. Every color-coded chip
   also carries a text label (color is never the only signal).

Ship a small on-site color **legend** (on hubs / `/about/`) teaching the grammar in one glance.

---

## 4. Mega-nav, sub-nav, and search build spec

### 4.1 Mega-nav (spec 03, with D1/D2)

Sticky bar, min-height 70px, `rgba(10,11,13,.9)` + blur, gold hairline bottom. Brand lockup far-left:
Anton "Wrestle Lore" + boxed `WL` monogram, links `/`. **Seven tab links** (Oswald 15px uppercase), each
a real `<a>` to its index that also opens a raw-HTML dropdown panel on hover/focus. Right-pinned ⌘K
search pill. **No Join pill (D2).** All panel markup ships in initial HTML; JS only toggles an `open`
class (crawlable; works JS-off). Panels: `<840px` collapse to a hamburger accordion drawer.

Panel contents (spec 03 §5): **Wrestlers** = four-axis panel (status/division/promotion/era chips) led by
an AJ Styles feature tile + 6 featured profiles; **Matches** = rated poster row + rating/promotion chips;
**Events** = recent PLE row with streaming tags + series/year/promotion chips; **Promotions** = six
brand cards with "Where to watch" chip rows; **Hall of Fame** (`.theme-hof` gold) = Ric Flair 2× hero +
Two-Time Club chip row + last-5-classes row; **Media** (`.theme-media` purple) = Chris Van Vliet hero +
proposed creator grid (ships only after `/media/` + Van Vliet exist; else the tab is hidden, never a
404); **More** = Moments poster row + Rivalries/Relationships/Rankings/Methodology/About/中文/**Insider**.

Wrap the header in `SiteNavigationElement` JSON-LD. Keyboard/ARIA per spec 03 §6: `aria-haspopup`/
`aria-expanded`/`aria-controls`, roving tabindex, Escape closes, `⌘K`/`Ctrl+K`/`/` open the palette.

### 4.2 Sub-nav: one faceted filter bar (spec 04 §4)

Reusable `.filterbar--faceted`, grouped by axis, used on every index. **A control that maps to a Tier-1
hub is an `<a href>`** (crawlable + no-JS navigates to the hub); JS intercepts on the master index to
filter in place and reflect non-default axes in `location.hash` (`replaceState`, no storage). **Tier-2
controls are `<button>`s.** Single-select within an axis, **AND** across axes, live count, and a
`.fb-empty` escape block with two nearest single-axis links so a zero-result filter never dead-ends.
Each Tier-1 hub recolors its `.fbtn.is-active` and eyebrow to its axis accent (`body.hub--legend`, etc.).
Promotion hubs get in-page anchor tabs: `#roster · #events · #streaming · #history`.

### 4.3 Search: header pill + ⌘K palette v2 (spec 05)

Two surfaces, one index. Header **search pill** (`<button data-cmdk-open aria-haspopup="dialog">`,
label + `⌘K` keycap; icon-only under 1080px). **Palette `#cmdk`** adds a type-scope tab row mirroring the
7 tabs (All/Wrestlers/Matches/Events/Promotions/Hall of Fame/Media/More) + a contextual facet-chip row
(promotion/status/division, Era behind `+`). Type scope and facets are independent axes that AND together,
so **blank query + NJPW + Current becomes faceted browse**. Empty state = discovery board (Trending
chips that *run* queries; Browse-by-category chips that *navigate*; Jump-to). **Recent is in-memory only**
(no storage; omitted on fresh load — documented so no one "fixes" it with localStorage). No-results state
offers "Did you mean" + browse chips + a `WL_GAP_HINTS` interim-hub link for known unbuilt terms.

**Index deliverable (spec 05 §7):** rename global `MAT_SEARCH_INDEX` → `WL_INDEX`; each entry gains
`t,u,ty,st,g,pr[],er[],cat[],a[],sub,b`. Generated at author time from `.md` front-matter with a
link-existence check that **fails the build on any 404**; `gap:true` pages are excluded from `WL_INDEX`
and held in `WL_GAP_HINTS`. Keep a one-release shim `window.MAT_SEARCH_INDEX = window.WL_INDEX;`.

---

## 5. Home page build spec (spec 02, with D1/D2 applied)

Twelve blocks, DOM order (hook → scale → people → events → brands → prestige → crossover → media →
trending → convert → answer/FAQ → keep going). Reuses existing Broadcast Bold components; background
alternates `--c-bg`/`--c-bg-elev-1` per section for separation.

1. **Hero** (`.hero-bb`): eyebrow "Pro wrestling, catalogued."; H1 EVERY RIVALRY / EVERY MATCH / EVERY
   LEGEND; lede naming WWE, WCW, ECW, TNA, NXT, and New Japan; CTAs gold "Join Wrestle Lore" → `/membership/`
   + ghost "Browse wrestlers" → `/wrestlers/`; right poster → `/matches/undertaker-vs-hbk-wm25/` (5.0).
2. **Scale bar + 5-star marquee:** true counts at build (6 promotions once NJPW ships, else 5; 89
   wrestlers, 30 rated matches, 15 rivalries). `VERIFY counts` = must equal real page counts.
3. **Wrestler discovery (centerpiece, req 2):** 5A four gateway lanes (Current red / Legends gold /
   Women magenta / Full Roster) → facet hubs; 5B a 16-tile poster grid across all axes + a client-side
   filter pill row (`All · Current · Legends · Women · WWE · WCW · ECW · TNA · NXT · NJPW`; pills are
   `<a>` to hubs with JS off). Tile hover reveals a `.tile__fact`.
4. **Events separation (req 3):** 6A latest-results rail (5 real 2026 editions, each with a streaming
   chip row); 6B "browse by series" (5 brand hubs); 6C facet strip (by promotion incl. NJPW, by year 2026,
   all events).
5. **Brand cards "Where to watch" (req 4):** six `.brand-card`s (WWE, NJPW, TNA, WCW, ECW, NXT), accent
   top-border, monogram, one positioning line, text streaming chips (US vs Intl labeled), links to the
   promotion + featured wrestlers. Do not render AEW/ROH/CMLL cards that would 404 (AEW arrives Wave 2).
6. **Hall of Fame rail (req 6, `.theme-hof`):** Ric Flair 2× most-decorated hero → `/wrestlers/ric-flair/`;
   last-5-classes timeline (2021–2025); Two-Time Club chip row (Michaels/Booker T/Razor Ramon/Nash/Hogan).
7. **AJ Styles + NJPW crossover (req 5, `.theme` NJPW):** three-node journey TNA → NJPW/Bullet Club → WWE,
   each node linking a promotion hub; secondary NJPW roster chips (Nakamura, Moxley, Finn Balor). **No
   retirement claim.**
8. **Media & Creators strip (req 7, `.theme-media` purple):** Chris Van Vliet hero + proposed grid, all
   `VERIFY`; links to `/media/` only until pages exist. Explicit note: Sami Zayn is not here.
9. **Trending rabbit-hole rails (req 9):** Five-Star Classics, Greatest Rivalries, Moments on video, the
   relationships bento. Honest recency only (editorial order + real build-date "added this week").
10. **Convert:** membership band renamed "Wrestle Lore Insider"; **replace the fabricated
    "12,840 waitlist / 38%" stats** with real catalog scale; add NJPW to the promotion selector.
11. **Answer-first + FAQ** (`FAQPage` JSON-LD): "What is Wrestle Lore?", "Where can I watch WWE PLEs?"
    (ESPN US / Netflix intl), "How many times is Ric Flair in the WWE Hall of Fame?" (two: 2008 solo,
    2012 Four Horsemen), "Which promotions?" (WWE/WCW/ECW/TNA/NXT/NJPW).
12. **Keep-going block** (mandatory) + final CTA band + footer (renamed, + HOF/Media/NJPW links).

Home JSON-LD: `Organization`, `WebSite` (+`SearchAction` → `/wrestlers/?q={query}`), `FAQPage`,
`ItemList` for the five-star rail. No fabricated `AggregateRating`.

---

## 6. Addictive-browsing layer (spec 07) — every entity page

Fixed engagement stack below entity content, in order: **FAQ → Rail 1 (primary related) → Rail 2
(optional) → "Because you came from…" strip (JS, referrer-only, hidden if empty) → Collection/Completion
panel → Keep-going block (mandatory, always last content) → Session trail (JS, hash-carried, hidden
<2 hops) → footer.** One reusable scroll-snap `.rail` (extends `.grid-spot`/`.tile`); rails render only
with ≥4 valid items, gaps render **non-linked** ("profile in progress"), never a 404. Keep-going = 4–6
typed relation links (sideways peer / person / rivalry / up-a-level / leaderboard / rematch), relation
type colors only the card's left rule. No-storage personalization: `document.referrer` (a read) against a
build-time `/data/graph.json`; session trail in `location.hash` then `replaceState`-ed away. Completion
is computed from the **database** (Trophy Case, "6 of 6 catalogued"), never the user. Trending is
editorial order + real build dates only — no invented counters. New front-matter fields (spec 07 §8:
`related, people, rivalries, matches, allies, accolades, participants, event, rematchOf, series, year,
card, editions, bouts, roster, streaming, facts`) generate rails, Keep-going, the Trophy Case, and
`graph.json`.

---

## 7. Conversion funnel (spec 06, binding with D2)

Six escalating layers keyed to intent, none blocking reading, none using storage beyond in-memory:
**L0** ambient (footer join line + Keep-going); **L1** `.join-inline` nudge once per long entity page;
**L2** `.rail-endcap` on the primary rail; **L3** `.unlock` gated *secondary* value (classic-match
archive, deep-dives, save-your-own-ratings, Sunday Rewind) — never gate a visible star rating or any
crawler-needed fact; **L4** in-memory exit-intent on a small high-intent allowlist only; **L5**
`.watchalong-cta` (the only place red = "now") on PPV event pages. **Color rule:** gold = evergreen
membership/premium; red = live/dated only; promotion accents never used as CTA fills. Membership page:
rename to Wrestle Lore, replace fabricated stats with real catalog scale, add NJPW to the selector, strip
CTA arrows, add "What do Insiders get?" FAQ. All L3 links fall back to `/membership/` until archive/
deep-dive/HOF/leaderboard pages exist. WWE-application relevance: full-funnel ownership, timing over
volume, event-tied lifecycle, and honest instrumentation.

---

## 8. Content showcases (specs 09 + 00)

- **Brand cards + streaming (req 4).** Verified 2026 homes (research 00 §1): **WWE** Raw=Netflix,
  SmackDown=USA Network, NXT=The CW, PLEs=ESPN (US)/Netflix (intl); **NJPW** NJPW World + TrillerTV +
  TV Asahi (Japan); **TNA** AMC & AMC+ (live) + TNA+ (streaming) + Prime Video (library) — this is the
  direct answer to "is TNA on Amazon?"; **WCW/ECW** WWE archive on Netflix (`VERIFY` exact US host);
  **NXT** The CW + Netflix archive; **AEW** (Wave-2 card) TBS/TNT/HBO Max + AEW Plus on TrillerTV. Chips
  are text, never logos; US vs Intl labeled.
- **Hall of Fame (req 6).** Answer-first + FAQ; Ric Flair 2× most-decorated hero (2008 solo, 2012 Four
  Horsemen, HIGH); Two-Time Club (Michaels, Booker T, Scott Hall/Razor Ramon, Kevin Nash, Hulk Hogan —
  status HIGH, **solo years `VERIFY`, do not print until confirmed**); Last-5-Classes 2021–2025 (Triple H
  ’25, Heyman ’24, Rey Mysterio ’23, Undertaker ’22, Kane ’21). Existing pages link; GAP inductees render
  as non-link tiles with "profile coming".
- **AJ Styles / NJPW (req 5).** Three-node journey hero linking all three promotion hubs + the existing
  profile. **Hard gate: the single-source Royal Rumble 2026 retirement must not be stated** — present/
  career-summary tense only, keep him `current`.
- **Media & Creators (req 7).** `/media/` purple hub: Chris Van Vliet confirmed hero (HIGH); proposed
  roster (Paquette, Rosenberg, Helwani, Sapp, Salcedo, Meltzer, Keller) all `VERIFY`, link out only when a
  page exists. **Sami Zayn stays a wrestler**, at most a "See also" pointer. Meltzer tile links
  `/methodology/` (star-rating origin).

---

## 9. Consolidated clickable → link mappings

Full per-surface tables live in each spec's clickable section (02 §15 home 98 rows; 03 §7 nav; 04 §8
sub-nav; 05 §13 search 54 rows; 06 §7 conversion 20 rows; 07 §10 engagement; 08 §10 + 09 §F showcases).
This brief does not re-transcribe them; it certifies they are consistent under the §0 decisions with two
adjustments: **(a) drop spec 02 rows 13/14 (nav Join pill) per D2**, replaced by the More-panel "Insider"
item + footer join line; **(b) the Media tab and its clickables ship only after `/media/` + Chris Van
Vliet exist**, else the tab is hidden. Every clickable resolves to a built page or a named non-404
interim fallback (facet chips → `/wrestlers/`; NJPW → `/promotions/`; HOF → `/rankings/`; L3 unlocks →
`/membership/`; GAP inductee/creator tiles → non-link "profile coming").

---

## 10. Facts to VERIFY, and the GAP build list

### 10.1 VERIFY before publish (do not state as fact until cleared)

- **NJPW brand red** exact hex (`--c-njpw:#d81f26` is the working value) and **AEW** hex.
- **AJ Styles Royal Rumble 2026 retirement** (single-source) — keep him `current`, no retrospective.
- **Two-Time Club solo-induction years** (Michaels/Booker T/Hall/Nash/Hogan) — two-time status is HIGH;
  years are MED, render in `.chip--verify` until confirmed.
- **WCW/ECW 2026 US archive host** (Netflix assumed, MED).
- **Media-roster affiliations** beyond Chris Van Vliet (all MED/VERIFY).
- **Homepage/scale counts** must equal real page counts at build.
- **Fabricated membership stats** (12,840 waitlist / 38% / 4 emails) — replace with real catalog scale.
- **Championship axis** — needs title-reign front-matter that does not exist; do not ship until authored.

### 10.2 GAP pages to build (nothing ships as a 404)

- **Promotions:** `/promotions/njpw/` (Wave 1, REQUIRED); `/promotions/aew/` (Wave 2).
- **Wrestler facet hubs:** `/wrestlers/current/`, `/legends/`, `/women/` (Wave 1); `/men/`, `/eras/` +
  `/eras/attitude-era/`, `/eras/modern/` (Wave 2).
- **Section hubs:** `/hall-of-fame/` (Wave 1, REQUIRED); `/media/` + `/media/chris-van-vliet/` (Wave 1,
  REQUIRED); `/events/2026/` (Wave 2); `/events/summerslam/`, `/events/survivor-series/` (Wave 3).
- **Missing profiles — HOF:** Paul Heyman, The Great Muta, Eric Bischoff, Rob Van Dam, Michelle McCool
  (Wave 2–3; until built, tiles are non-link).
- **Missing profiles — NJPW/Bullet Club:** Kenny Omega, Will Ospreay (Wave 2).
- **Media profiles:** Van Vliet (Wave 1 hero); Paquette/Rosenberg/Helwani/Sapp/Salcedo/Meltzer/Keller
  (Wave 2, each `VERIFY`).
- **Data/infra:** rebuild `/wrestlers/` index 41 → 89 with six-axis `data-*`; rename
  `MAT_SEARCH_INDEX` → `WL_INDEX` with the richer schema + link-existence check; generate
  `/data/graph.json` + `/data/trending.md`; append §3 tokens/components, `.rail`, `.keepgoing`,
  `.brandcard`, badge/chip classes, and conversion components to `css/site.css`.

---

## 11. Phased BUILD ORDER

**Phase 0 — System + rename (unblocks everything).**
1. Append all §3 tokens + `[data-promo]`/`.theme-*` scopes + badge/chip/tile/rail/keepgoing/brandcard/
   conversion CSS to `css/site.css` (additive; no existing hex changed). Retire `.nav__cta` from the bar.
2. Global rename "MAT" → "Wrestle Lore" (titles, meta, OG, nav brand, footer, JSON-LD `name`, ⌘K copy,
   membership page, canonical domain); `MAT_SEARCH_INDEX` → `WL_INDEX` (+ shim).
3. Propagate the 7-tab mega-nav (D1) + header search pill + footer to all 169 pages (kills the old flat
   nav still on sub-pages).

**Phase 1 — Required requirement pages (reqs 2,4,5,6,7).**
4. Rebuild `/wrestlers/` to 89 cards with six-axis `data-*` + faceted bar; extend `js/main.js` filter.
5. Build `/promotions/njpw/` + the AJ Styles crossover hero (reqs 5). Rebuild `/promotions/` as brand
   cards with streaming chips (req 4).
6. Build `/hall-of-fame/` (req 6) and the three wrestler facet hubs `/current/`, `/legends/`, `/women/`
   (req 2).
7. Build `/media/` + `/media/chris-van-vliet/` (req 7); only then un-hide the Media tab.

**Phase 2 — Home + engagement + search.**
8. Assemble the 12-block home page (§5). Wire the engagement stack (§6) + `/data/graph.json` +
   `/data/trending.md` across entity pages. Ship the ⌘K palette v2 + `WL_INDEX` + `WL_GAP_HINTS`.
9. Place conversion layers L0–L5 (§7); rebuild the membership page (rename, real stats, NJPW selector).

**Phase 3 — Depth + remaining chips.**
10. `/promotions/aew/`, `/events/2026/`, era hubs (Attitude, Modern), SummerSlam + Survivor Series series
    hubs; missing HOF + NJPW + media profiles (each `VERIFY` cleared before its chip links).

**Phase 4 — Verify + ship.**
11. Confirm every §10.1 VERIFY item or keep it flagged/omitted; run the link-existence check (zero 404s);
    verify scale counts; run the anti-AI copy pass; validate JSON-LD; check WCAG AA pairings; confirm no
    browser storage is written (devtools Application tab).

---

## 12. Cross-spec source map

Vision/patterns → 01; facts (streaming/HOF/AJ/NJPW/media/taxonomy/gaps) → 00; home → 02; mega-nav → 03;
sub-nav/taxonomy/URLs/breadcrumbs → 04; search/index schema → 05; conversion funnel → 06;
addictive-browsing/engagement → 07; color/badge/tile/brand-card system → 08; content showcase modules →
09. On any detail not overridden by §0 here, the originating spec governs.
