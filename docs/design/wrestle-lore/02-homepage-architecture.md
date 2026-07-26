# Wrestle Lore — Homepage Architecture & Build Spec

Senior homepage/product-designer deliverable. This is the full, buildable spec for the **Wrestle Lore**
home page: every section top to bottom, its purpose, the exact content it showcases, the interaction
layers, the color rules, and a table of every clickable and where it links. It builds on
`00-content-data-research.md` (facts) and `01-inspiration-research.md` (patterns). No invented facts —
anything unverified is flagged `VERIFY` inline and links are routed only to pages that already exist,
with gaps called out.

- Date: 2026-07-26
- Rename: the site is **Wrestle Lore** (was "MAT"). Brand mark monogram `WL`. Every `<title>`, meta,
  nav brand, footer, OG `site_name`, and JSON-LD `name` uses "Wrestle Lore". See §12.
- Reuses the existing single stylesheet `css/site.css` (Broadcast Bold). New tokens/components this
  page needs are specified in §2 and must be added to `css/site.css` before build.
- Crawl rule: **every nav and section link is a real `<a href>` in raw HTML**, not JS-rendered. JS only
  enhances (reveal, hover, marquee, ⌘K). The page is fully functional with JS off.

---

## 0. Page goals (why this page exists)

1. Prove the catalog is huge, colorful, and organized (req 1, 2, 3) — the wall itself is the pitch.
2. Give three obvious first clicks in the first two screens (hero CTA, a wrestler tile, a category lane).
3. Never dead-end: the page is a stack of rails, each a finishable promise that points at the next
   (inspiration §B1/B2). Bottom of page = a "Keep going" block, same as every interior page.
4. Be citable: answer-first paragraph + FAQ + JSON-LD so AI answer engines lift facts (inspiration §C).
5. Funnel to membership without begging: two CTA moments (hero + mid-page band), honest copy.

Section order is deliberate: **hook → scale → discover people → discover events → understand promotions
→ prestige (HOF) → the crossover story (AJ/NJPW) → the media layer → trending rabbit holes → convert →
answer/FAQ → keep going → footer.** Rationale: identity first, then the two biggest catalogs (people,
events), then context (brands), then the emotional/prestige hooks that make people stay.

---

## 1. Global frame (header, palette wall, footer)

### 1.1 Mega-nav (unchanged structure, renamed + 2 new tabs' content)
Keep the existing 5-tab poster-wall mega-nav (`Wrestlers / Matches / Events / Moments / More`) plus
`⌘K` search and the `Join` CTA. Two new destinations are added **inside existing dropdowns**, not as new
top-level tabs (keeps the bar to the fixed instrument):
- Under **Wrestlers** mega panel add a fourth column "By Status / Division": links to
  `/wrestlers/current/`, `/wrestlers/legends/`, `/wrestlers/women/` `GAP` (see §13), plus
  `/promotions/njpw/` `GAP`.
- Under **More** mega panel add: `Hall of Fame` → `/hall-of-fame/` `GAP`, `Media & Creators` →
  `/media/` `GAP`.
- Rename brand: `WL Wrestle Lore`. CTA button copy: `Join Wrestle Lore` → `/membership/`.

The header/nav CSS and JS already exist; only the link list and brand text change. Sticky, 56px tall,
translucent on scroll (existing behavior).

### 1.2 Palette wall — the whole home page is the "poster wall"
Every section uses the same tile/rail system so the page reads as one instrument (inspiration §A2/A3).
Background alternates `--c-bg` and `--c-bg-elev-1` between sections (existing `.seam` pattern) for
visual separation without new chrome.

### 1.3 Footer (renamed, +2 columns of new hubs)
Existing 4-column footer; update brand to Wrestle Lore, add "Hall of Fame", "Media & Creators", and
"NJPW" links to the relevant columns. Keep the fan-made disclaimer verbatim.

---

## 2. Color & badge rules (extends existing tokens)

The current tokens (`--c-wwe #c8102e`, `--c-wcw #e2b13c`, `--c-ecw #b0b0b0`, `--c-tna #1e73be`,
`--c-nxt #f5c518`, gold `#d4af37`, red `#e11d2a`) stay. **Add these tokens to `:root` in
`css/site.css`:**

```css
/* new promotion accent */
--c-njpw:#c1272d;                 /* NJPW crimson on near-black field; VERIFY vs official NJPW branding */
/* category axis accents (non-promotion) */
--c-current:#e11d2a;              /* CURRENT status = live red (reuses brand red) */
--c-legend:#d4af37;              /* LEGEND status = gold (reuses brand gold) */
--c-women:#d6398a;               /* Women's division = magenta-rose (new, unused hue) */
--c-media:#2dd4bf;               /* Media & Creators = teal (new, unused hue) */
--c-njpw-tint:rgba(193,39,45,.14);
--c-women-tint:rgba(214,57,138,.14);
--c-media-tint:rgba(45,212,191,.14);
```

**Badge system carries meaning by COLOR + SHAPE (inspiration §A3, §D1). One axis = one shape:**

| Axis | Shape (class) | Colors | Reads as |
|---|---|---|---|
| Promotion | pill `chip chip--{wwe,wcw,ecw,tna,nxt,njpw}` | promotion accents | where they wrestle(d) |
| Status | pill `chip chip--current` / `chip chip--legend` | red / gold | active 2026 vs historic |
| Division | pill `chip chip--women` | magenta | women's division |
| HOF | pill `chip chip--gold` (existing) with "HOF" text | gold | Hall of Famer |
| Media | pill `chip chip--media` | teal | interviewer/creator, not a wrestler |
| Rating | corner number `tile__rating` (existing) | gold | match star score |

Add the matching chip classes to CSS (mirror the existing `.chip--wwe` block):
```css
.chip--njpw{color:#fff;background:var(--c-njpw);border-color:var(--c-njpw);}
.chip--current{color:#fff;background:var(--c-red);border-color:var(--c-red-bright);}
.chip--legend{color:var(--c-gold-bright);background:var(--c-gold-tint);border-color:var(--c-gold-dim);}
.chip--women{color:#fff;background:var(--c-women);border-color:var(--c-women);}
.chip--media{color:#04201d;background:var(--c-media);border-color:var(--c-media);}
```
Tile-media gradient variants (mirror existing `.tile--gold .tile__media`): add `.tile--njpw`,
`.tile--women`, `.tile--media` swapping the `color-mix` base color to the axis token so a lane of tiles
reads its category at a glance.

**Rule of one accent per context:** a tile shows at most 2 chips (one promotion + one status/division),
never a rainbow. Section headers use one accent hairline (`.rule-gold`, or an equivalent
`.rule-njpw` / `.rule-women` for the themed sections).

---

## 3. HERO (screen 1)

**Purpose:** identity + one-line pitch + first click. Reuses `.hero-bb`.

**Layout desktop (≥860px):** existing 2-col grid `1.15fr .85fr`. Left = copy stack; right = a featured
"poster" card (the current Undertaker vs HBK WM25 facade is fine and links to a real match).
**Layout 360px:** single column, poster card stacks under the copy; title clamps via `--fs-900`.

**Content:**
- Eyebrow: `Pro wrestling, catalogued.` (replaces "Match · Athlete · Timeline").
- H1 (Anton, existing `.hero-bb__title`): `EVERY RIVALRY.` / `EVERY MATCH.` / `<span class="accent">EVERY LEGEND.</span>` — keep; it already tests well and needs no fact.
- Lede (rewrite for new scope, no em-dash separators, no banned words):
  `The searchable database of pro wrestling. Deep profiles, star-rated matches, brand guides with where to watch, a Hall of Fame, and the rivalries that tie it all together. WWE, WCW, ECW, TNA, NXT, and now New Japan.`
- CTAs (`.cluster`): primary gold `Join Wrestle Lore` → `/membership/`; ghost `Browse wrestlers` → `/wrestlers/`.
- Right poster: featured 5.0 match facade → links `/matches/undertaker-vs-hbk-wm25/` (real, 5.0).

**Interaction layers:**
- `.hero-bb__bg` parallax on pointer move (existing `--px/--py`), disabled under `prefers-reduced-motion`.
- `data-reveal` fade/rise on the copy stack and the poster (existing IntersectionObserver in enhance.js).
- Poster facade: click opens the match page (not a fake video), honest label.

---

## 4. SCALE BAR + FIVE-STAR MARQUEE (screen 1–2 seam)

**Purpose:** prove catalog size (completion psychology, inspiration §B5) and tease the rating spine.

**Stats bar** (`.glass.stats-bar`, existing). Update numbers to the true current counts at build time
(do not overstate — count real pages): `6 Promotions` (WWE/WCW/ECW/TNA/NXT/NJPW once NJPW ships; until
then show `5` + label note), `89 Wrestlers`, `30 Rated Matches`, `15 Rivalries`, `29 Years Covered`.
`VERIFY counts at build` — the `data-count` values must equal actual page counts.

**Marquee** (`.marquee`, existing): the 5.0 club ticker. Every item text-only, each duplicated for the
seamless loop. Pauses on hover; becomes a plain scroll under reduced-motion (existing). Items link
nowhere (decorative ticker); the "All rankings" link lives in the next section head. Keep current 7
five-star entries (all map to real match pages).

---

## 5. WRESTLER DISCOVERY BLOCK — "Current vs Legends, Women vs Men" (the centerpiece, req 2)

**Purpose:** the biggest, most colorful separation surface. Two stacked pieces: (A) four big category
lanes, (B) a dense poster grid of many wrestlers with filter pills.

### 5A. Category lanes (bento of 4 "gateway" tiles)
Reuse `.bento`; four wide gateway tiles, each themed by its axis token, each a real hub link.

| Lane | Tile theme class | Chip | Links to | Note |
|---|---|---|---|---|
| Current Stars | `tile--current` (red) | `chip--current` | `/wrestlers/current/` | `GAP §13` → until built, link `/wrestlers/` |
| Legends | `tile--gold` (existing) | `chip--legend` | `/wrestlers/legends/` | `GAP §13` → fallback `/wrestlers/` |
| Women's Division | `tile--women` (magenta) | `chip--women` | `/wrestlers/women/` | `GAP §13` → fallback `/wrestlers/` |
| The Full Roster | neutral | count chip "89" | `/wrestlers/` | exists |

Each gateway tile shows the axis name (Anton), a one-line description, and a small "count" (e.g.
"~30 active", "~50 legends", "13 in the women's division" — `VERIFY counts`). Copy uses specific
nouns, no clichés.

**Layout desktop:** 4-up row (or 2×2). **360px:** single column stack; each tile min-height 132px so
the gradient reads.

### 5B. "The Roster" poster grid + filter pills
Reuse `.grid-spot` + `.tile`. Show **16 wrestler tiles** spanning every axis so the wall looks deep and
colorful. Above it, a **filter pill row** (client-side, progressive-enhancement; with JS off the pills
are plain links to the facet hubs / `/wrestlers/`).

Pills (buttons, `aria-pressed`): `All · Current · Legends · Women · WWE · WCW · ECW · TNA · NXT · NJPW`.
JS filters the visible tiles by `data-status`, `data-division`, `data-promotion` attributes on each
`.tile`. No storage; state is in-memory only. With JS off, each pill is an `<a>` to its hub (or
`/wrestlers/` for gaps).

**16 tiles (all real pages), balanced across axes and colors:**

| # | Tile | Chips | data-attrs | Links to |
|---|---|---|---|---|
| 1 | Roman Reigns | WWE · Current | current, male, wwe | `/wrestlers/roman-reigns/` |
| 2 | Cody Rhodes | WWE · Current | current, male, wwe | `/wrestlers/cody-rhodes/` |
| 3 | Rhea Ripley | WWE · Women | current, women, wwe | `/wrestlers/rhea-ripley/` |
| 4 | Bianca Belair | WWE · Women | current, women, wwe | `/wrestlers/bianca-belair/` |
| 5 | Gunther | WWE · Current | current, male, wwe | `/wrestlers/gunther/` |
| 6 | CM Punk | WWE · Current | current, male, wwe | `/wrestlers/cm-punk/` |
| 7 | Becky Lynch | WWE · Women | current, women, wwe | `/wrestlers/becky-lynch/` |
| 8 | Stone Cold Steve Austin | WWE · Legend | legend, male, wwe | `/wrestlers/stone-cold-steve-austin/` |
| 9 | The Undertaker | WWE · Legend | legend, male, wwe | `/wrestlers/the-undertaker/` |
| 10 | Sting | WCW · Legend | legend, male, wcw | `/wrestlers/sting/` |
| 11 | Ric Flair | WCW · Legend | legend, male, wcw | `/wrestlers/ric-flair/` |
| 12 | Trish Stratus | WWE · Women · Legend | legend, women, wwe | `/wrestlers/trish-stratus/` |
| 13 | AJ Styles | TNA · NJPW | legend?, male, tna | `/wrestlers/aj-styles/` (status VERIFY, see §9) |
| 14 | Shinsuke Nakamura | NJPW · Current | current, male, njpw | `/wrestlers/shinsuke-nakamura/` |
| 15 | Jon Moxley | NJPW · Current | current, male, njpw | `/wrestlers/jon-moxley/` |
| 16 | Rey Mysterio | WWE · Legend · HOF | legend, male, wwe | `/wrestlers/rey-mysterio/` |

Section head "See all 89" link → `/wrestlers/`. `--seed` values vary per tile (existing gradient-angle
trick) so no two adjacent gradients match.

**Interaction layers:**
- Hover: `.tile` lift + `.tile__spot` cursor-follow glow (existing) + `.tile__mono` warms to gold.
- Hover/tap enrichment (inspiration §B6): on hover a compact overlay fades in over `.tile__media`
  showing one signature fact + promotion + status (CSS-only; on mobile the fact sits under the tile).
  Add `.tile__fact` element, hidden by default, revealed on `:hover`/`:focus-within`.
- Filter pills: click toggles `aria-pressed`, JS adds `hidden` to non-matching tiles with a 120ms
  fade; count in each pill (`.cnt`) shows how many match. Reduced-motion: instant.

---

## 6. EVENTS / PPV SEPARATION (req 3)

**Purpose:** make the event catalog browsable three ways: by recency, by series/brand, by year. Reuse
`.ev-tile` (+`.ev-tile--red`) for editions and `.tile` for series hubs.

### 6A. "Latest results" rail (horizontal, real 2026 editions)
5 `.ev-tile` cards, each with a **streaming badge** row (small chips: `ESPN (US)` `Netflix (intl)` per
§7 facts) and result kicker. Horizontal scroll-snap on mobile, wrapped grid desktop.

| Event tile | Kicker (real result) | Streaming chips | Links to |
|---|---|---|---|
| WrestleMania 42 (2026) | Rhodes & Reigns win titles | ESPN (US) · Netflix (intl) | `/events/wrestlemania-42-2026/` |
| Night of Champions 2026 | Sami Zayn wins the WWE Title | ESPN (US) · Netflix (intl) | `/events/night-of-champions-2026/` |
| Backlash 2026 | Reigns retains; Cena classic | ESPN (US) · Netflix (intl) | `/events/backlash-2026/` |
| Royal Rumble 2026 | (use real result from page) | ESPN (US) · Netflix (intl) | `/events/royal-rumble-2026/` |
| Elimination Chamber 2026 | (use real result from page) | ESPN (US) · Netflix (intl) | `/events/elimination-chamber-2026/` |

### 6B. "Browse by series" (brand hubs)
5 `.tile` gateway cards → the brand hubs (each aggregates all editions = the by-year archive spine).

| Tile | Links to |
|---|---|
| WrestleMania | `/events/wrestlemania/` |
| Royal Rumble | `/events/royal-rumble/` |
| Elimination Chamber | `/events/elimination-chamber/` |
| Night of Champions | `/events/night-of-champions/` |
| Backlash | `/events/backlash/` |

### 6C. Facet strip (text links, SEO + browse)
A one-line pill strip: `By promotion:` WWE `/promotions/wwe/` · WCW `/promotions/wcw/` · ECW
`/promotions/ecw/` · TNA `/promotions/tna/` · NJPW `/promotions/njpw/` `GAP` · NXT `/promotions/nxt/` ·
`All events` `/events/` · `By year: 2026` `/events/` (multi-year archive is a `GAP`, structure noted in
research §7). Section head "All events" → `/events/`.

**Layout 360px:** 6A rail = horizontal scroll-snap (one-and-a-peek card width ~78vw); 6B = 2-col grid;
6C wraps. Desktop: 6A = 5-up (or 3-up + scroll), 6B = 5-up row.

---

## 7. BRAND CARDS — "Where to watch" (req 4)

**Purpose:** the streaming answer engine bait. One card per promotion; each = accent header + monogram +
"Where to watch" chip row + one positioning fact + links to that promotion's page and top wrestlers.
Chips are **text, not logos** (avoids trademark image issues). Label US vs Intl explicitly. All
streaming facts from research §1 (HIGH confidence unless flagged).

Component: new `.brand-card` (build from `.tile` base + accent top-border by promotion token). Grid:
desktop 3-up (2 rows), 360px single column.

| Brand card | Accent | Where-to-watch chips | One-line fact (verified) | Card links |
|---|---|---|---|---|
| **WWE** | `--c-wwe` | Raw: Netflix · SmackDown: USA Network · NXT: The CW · PLEs: ESPN (US) / Netflix (intl) | "Raw streams on Netflix. SmackDown airs on USA Network. Premium Live Events run on ESPN in the US and Netflix internationally." | `/promotions/wwe/` · featured: `/wrestlers/roman-reigns/`, `/wrestlers/cody-rhodes/` |
| **NJPW** `NEW` | `--c-njpw` | NJPW World · TrillerTV · TV Asahi (Japan) | "Watch on NJPW World, the promotion's own subscription, plus TrillerTV. Flagship: Wrestle Kingdom at the Tokyo Dome." | `/promotions/njpw/` `GAP §13` · featured: `/wrestlers/aj-styles/`, `/wrestlers/shinsuke-nakamura/` |
| **TNA** | `--c-tna` | AMC · AMC+ · TNA+ · library on Prime Video | "Thursday Night iMPACT airs on AMC and AMC+, with TNA+ for the full library. Older seasons sit on Prime Video." | `/promotions/tna/` · featured: `/wrestlers/aj-styles/`, `/wrestlers/samoa-joe/` |
| **WCW** | `--c-wcw` | Library on WWE's streaming archive (Netflix) `VERIFY US host` | "WCW folded in 2001. WWE owns the tape library, now on its streaming archive." | `/promotions/wcw/` · featured: `/wrestlers/sting/`, `/wrestlers/goldberg/` |
| **ECW** | `--c-ecw` | Library on WWE's streaming archive (Netflix) `VERIFY US host` | "ECW folded in 2001. Its library lives in WWE's archive." | `/promotions/ecw/` · featured: `/wrestlers/mick-foley/`, `/wrestlers/rob-van-dam/` `GAP` → use `/wrestlers/bully-ray/` |
| **NXT** | `--c-nxt` | The CW · archives on Netflix | "WWE's developmental brand airs Tuesdays on The CW." | `/promotions/nxt/` · featured: `/wrestlers/gunther/`, `/wrestlers/cody-rhodes/` |

Note: AEW/ROH/CMLL are NOT promotions on this site yet (no pages) — do **not** add cards that would 404.
Research §1 has their facts if/when pages are built.

**Interaction layers:** card hover lift; chip row is non-interactive text (or each chip could be an
`<abbr>` with a title tooltip naming the platform in full). Accent top-border (3px) uses the promotion
token so the six cards form a color spectrum across the section.

---

## 8. HALL OF FAME RAIL (req 6)

**Purpose:** prestige + completionism (ranked/collection content, inspiration §B3). Two pieces: the
most-decorated hero, then the last-5-classes timeline, then the two-time club strip.

Section theme accent: gold (`.rule-gold`). Section head eyebrow `WWE Hall of Fame`, H2 "The immortals",
"Full Hall of Fame" link → `/hall-of-fame/` `GAP §13`.

### 8A. Most-decorated hero (Ric Flair)
Wide `.tile is-wide` (or `.brand-card` gold variant), `chip--gold` "2× HOF".
Copy (verified, research §2): "**Ric Flair** is a two-time WWE Hall of Famer, inducted in 2008 as an
individual and again in 2012 with the Four Horsemen." Link → `/wrestlers/ric-flair/`.

### 8B. Last 5 classes timeline (horizontal)
5 class cards (`.tile`), newest first, each linking to the headline inductee's real page.

| Class | Headline inductee tile | Links to | Co-inductees noted (link if page exists) |
|---|---|---|---|
| 2025 | Triple H | `/wrestlers/triple-h/` | Lex Luger `/wrestlers/lex-luger/`; Michelle McCool `GAP` |
| 2024 | Paul Heyman | `/hall-of-fame/#2024` `GAP` (no Heyman page) | — |
| 2023 | Rey Mysterio | `/wrestlers/rey-mysterio/` | The Great Muta `GAP` |
| 2022 | The Undertaker | `/wrestlers/the-undertaker/` | Vader `/wrestlers/vader/` |
| 2021 | Kane | `/wrestlers/kane/` | Rob Van Dam `GAP`; Eric Bischoff `GAP` |

For 2024 (Heyman has no page), the tile links to the HOF hub anchor `GAP`; until the hub exists, link
`/wrestlers/` is a poor fallback — prefer building the Heyman page or the hub first (§13). Do not 404.

### 8C. Two-Time Club strip (text/chip row, all real pages)
Small pill links, gold: Shawn Michaels `/wrestlers/shawn-michaels/`, Booker T `/wrestlers/booker-t/`,
Scott Hall (Razor Ramon) `/wrestlers/razor-ramon/`, Kevin Nash `/wrestlers/kevin-nash/`, Hulk Hogan
`/wrestlers/hulk-hogan/`. Caption: "Elite two-time inductees" with a small `VERIFY` note that exact solo
years are being confirmed (research §2 flags Hall/Booker/Michaels solo years as MED).

**Layout 360px:** 8A full-width; 8B horizontal scroll-snap; 8C wraps. Desktop: 8A wide tile spanning
2 cols beside a short intro, 8B 5-up row, 8C inline pill row.

---

## 9. AJ STYLES + NJPW CROSSOVER SHOWCASE (req 5)

**Purpose:** the signature "one wrestler, three promotions" story that also justifies adding NJPW.
Full-bleed feature band, NJPW crimson accent (`.rule-njpw`), distinct from the rest of the page.

**Layout desktop:** 2-col — left a large AJ Styles feature tile (`.tile--njpw`, mono "A", `chip--tna` +
`chip--njpw`), right a 3-step journey list (TNA → NJPW/Bullet Club → WWE) with a link per step. **360px:**
feature tile on top, journey list below.

**Content (verified, research §3; do NOT state retirement):**
- Hero line: "AJ Styles, The Phenomenal One." Link → `/wrestlers/aj-styles/`.
- Journey steps (each a link):
  1. "TNA franchise player and multi-time World Champion." → `/promotions/tna/`
  2. "Leader of the original Bullet Club and IWGP Heavyweight Champion in New Japan." →
     `/promotions/njpw/` `GAP §13`
  3. "Multi-time WWE Champion since his 2016 Royal Rumble debut." → `/promotions/wwe/`
- `VERIFY` banner (internal note, not shown as fact): "AJ Styles reported to retire at Royal Rumble
  2026 is single-source — do not publish as fact." If unconfirmed at build, omit any retirement copy.
- Secondary NJPW roster chips (real pages): Shinsuke Nakamura `/wrestlers/shinsuke-nakamura/`, Jon
  Moxley `/wrestlers/jon-moxley/`, Finn Balor (original Bullet Club "Prince Devitt")
  `/wrestlers/finn-balor/`. "Explore New Japan" CTA → `/promotions/njpw/` `GAP`.

**Interaction:** the journey list items reveal on scroll in sequence (staggered `data-reveal`);
hover on the feature tile runs the spotlight glow tinted NJPW crimson (override `--spot-color`).

---

## 10. MEDIA & CREATORS STRIP (req 7)

**Purpose:** surface the media layer as its own colored lane (teal, `.tile--media`, `chip--media`).
Hero + proposed grid. **Every card here is a `GAP`** (no media pages exist yet); until built, cards link
to the media hub `/media/` `GAP` or an external citable source, never a fake internal page.

Section head eyebrow `Media & Creators`, H2 "The people who tell the story", link → `/media/` `GAP §13`.

**Content (research §6):**
- **Hero: Chris Van Vliet** (HIGH). Copy: "Emmy-winning host of the INSIGHT interview show, the premier
  long-form wrestler interview." Link → `/media/chris-van-vliet/` `GAP` (build first) or external
  citable link as interim.
- Proposed grid (all `VERIFY` current affiliation, research §6): Renee Paquette, Peter Rosenberg,
  Ariel Helwani, Sean Ross Sapp (Fightful), Denise Salcedo, Dave Meltzer (Wrestling Observer, the
  star-rating source). Each tile carries a small `VERIFY` flag until built; link → its `/media/{slug}/`
  `GAP`.
- **Explicit routing note for the build team:** the user mentioned "Sami Zayn" for this tab. Sami Zayn
  is an **active wrestler**, not media — he stays on the athlete grid (`/wrestlers/sami-zayn/`) and must
  **not** appear here. This is called out so his mention is routed correctly.

**Layout 360px:** hero tile full-width, then 2-col grid. Desktop: hero wide tile + 3-up proposed grid.

---

## 11. TRENDING / RABBIT-HOLE RAILS (req 9, retention)

**Purpose:** the discovery engine — stacked themed rails, each a finishable promise (inspiration
§B1/B3/B4). Honest recency: an editorial "This week" set by hand, plus a real "Recently added". No fake
live counters.

### 11A. Five-Star Classics rail (keep existing)
`.grid-spot` of 6 five-star match tiles → real match pages (existing block, unchanged). Head link →
`/rankings/`.

| Tile | Links to |
|---|---|
| Undertaker vs Michaels (WM25) | `/matches/undertaker-vs-hbk-wm25/` |
| CM Punk vs Cena (MITB '11) | `/matches/cm-punk-vs-cena-mitb-2011/` |
| Styles vs Daniels vs Joe (TNA '05) | `/matches/styles-vs-daniels-vs-joe-unbreakable-2005/` |
| Gargano vs Ciampa (NOLA '18) | `/matches/gargano-vs-ciampa-takeover-new-orleans-2018/` |
| Angle vs Benoit (RR '03) | `/matches/angle-vs-benoit-royal-rumble-2003/` |
| Rey vs Eddie (Havoc '97) | `/matches/rey-mysterio-vs-eddie-guerrero-halloween-havoc-1997/` |

### 11B. "Greatest rivalries" rail
6 `.tile` → real rivalry pages: Austin vs McMahon `/rivalries/austin-vs-mcmahon/`, Rock vs Austin
`/rivalries/rock-vs-austin/`, Bret vs HBK (Montreal) `/rivalries/bret-vs-hbk-montreal/`, The Bloodline
`/rivalries/the-bloodline/`, Sting vs Flair `/rivalries/sting-vs-flair/`, Undertaker vs Kane
`/rivalries/undertaker-vs-kane/`. Head link → `/rivalries/`.

### 11C. "Moments on video" rail
4 `.tile` → real moment pages: Mankind's Hell in a Cell fall
`/moments/mankind-hell-in-a-cell-fall-1998/`, Kane's debut `/moments/kane-debut-badd-blood-1997/`,
Austin's broken neck `/moments/steve-austin-broken-neck-1997/`, Triple H tears his quad
`/moments/triple-h-tears-his-quad-2001/`. Head link → `/moments/`.

### 11D. "The web" bento (keep existing relationships block)
3 tiles → `/relationships/#families`, `/relationships/#couples`, `/relationships/#factions`. Head link →
`/relationships/`.

**Interaction:** all rails horizontal scroll-snap on mobile, wrapped `.grid-spot` desktop; tiles reuse
hover lift + spot glow + mono-warm. `data-reveal` staggers tiles in.

---

## 12. CONVERT + ANSWER + FAQ + KEEP GOING (screens near bottom)

### 12A. Membership band (keep existing `.waitlist-cta`)
Rename to Wrestle Lore Insider. Copy: "Full star ratings, the classic-match archive, the weekly Rewind
newsletter, and member-only rankings. Free to start." Email field + `Get early access`. Form posts to
existing waitlist handler. `VERIFY`/soften the "12,840 fans" count — use a real number or remove it
(anti-cliché standard; do not fabricate). CTA → `/membership/`.

### 12B. Answer-first block (GEO, keep existing `.answer`)
Rewrite: "**Wrestle Lore is a searchable database of pro wrestling.** It catalogs wrestlers, star-rates
the most important matches, guides you to where every promotion streams, and maps the rivalries across
WWE, WCW, ECW, TNA, NXT, and New Japan." Move this HIGHER (just under the hero) for GEO if testing shows
lift; keep a copy near FAQ. One instance only in final DOM to avoid duplicate-content.

### 12C. FAQ (`.faq` + `FAQPage` JSON-LD) — rewrite for new scope
Questions (answer-first, verified): "What is Wrestle Lore?", "Where can I watch WWE Premium Live
Events?" (answer: ESPN in the US, Netflix internationally — research §1), "How many times is Ric Flair in
the WWE Hall of Fame?" (answer: two — 2008 solo, 2012 with the Four Horsemen — research §2), "Which
promotions does Wrestle Lore cover?" (WWE, WCW, ECW, TNA, NXT, NJPW). Mirror each in the JSON-LD.

### 12D. "Keep going" block (mandatory, inspiration §B2)
The retention/SEO backbone. 6 contextual links, same component every interior page uses:
`/wrestlers/current/` `GAP`→`/wrestlers/`, `/hall-of-fame/` `GAP`, `/promotions/njpw/` `GAP`,
`/rankings/`, `/events/`, `/rivalries/`. Never dead-end.

### 12E. Final CTA band (keep existing)
"Don't just watch. Remember." → `/membership/`.

---

## 13. GAP LIST — pages this homepage links to that do NOT exist yet

The homepage must not 404. Each gap below needs either (a) the page built, or (b) an interim fallback
link specified above. Priority order for build:

1. `/promotions/njpw/` — linked from §5B, §6C, §7, §9, §12D. **Highest priority** (brand card + AJ
   showcase both point here). Interim fallback: none good; build this first.
2. `/hall-of-fame/` — linked from §1.1, §8, §12D. Build the hub; enables the 2024 Heyman tile.
3. `/wrestlers/current/`, `/wrestlers/legends/`, `/wrestlers/women/` — linked from §5A, §5B pills,
   §12D. Interim fallback: `/wrestlers/` (works, less precise). Build as faceted poster-wall hubs.
4. `/media/` + `/media/chris-van-vliet/` (and proposed media slugs) — linked from §1.1, §10. Interim:
   link the hub only; do not link unbuilt personality pages.
5. Missing person pages referenced: Rob Van Dam (§7 ECW, §8B) → interim use another real ECW/2021 name;
   Michelle McCool, The Great Muta, Paul Heyman, Eric Bischoff (§8) → route to HOF hub anchors, not
   `/wrestlers/`.

Until a gap is built, use the interim fallback named in its section. Track in the build ticket.

---

## 14. Responsive summary (360px vs desktop)

| Section | 360px | Desktop (≥960px) |
|---|---|---|
| Hero | 1 col, poster under copy | 2 col 1.15/.85 |
| Stats bar | 2×3 grid | 5-up (6 once NJPW) |
| Marquee | scroll | animated loop |
| 5A lanes | 1 col stack | 4-up or 2×2 |
| 5B roster grid | 2-col tiles, pills wrap/scroll | 4–5-up, pill row inline |
| 6A results | h-scroll snap (78vw cards) | 5-up |
| 6B series | 2-col | 5-up |
| Brand cards | 1 col | 3-up ×2 rows |
| HOF | hero full-width, classes h-scroll | wide hero + 5-up row |
| AJ/NJPW | stacked | 2-col |
| Media | hero + 2-col | wide hero + 3-up |
| Rails 11A–D | h-scroll snap | wrapped grid |
| Convert/FAQ/keep-going | 1 col | narrow wrap centered |

All horizontal rails: `scroll-snap-type:x mandatory` + `-webkit-overflow-scrolling:touch`; tiles
`scroll-snap-align:start`. Reduced-motion disables reveal, parallax, marquee animation, and filter
fades.

---

## 15. Master clickable → link-target table (every link on the page)

| # | Section | Clickable label | Target | Status |
|---|---|---|---|---|
| 1 | Header | Wrestle Lore (brand) | `/` | real |
| 2 | Header | Wrestlers | `/wrestlers/` | real |
| 3 | Header | Matches | `/matches/` | real |
| 4 | Header | Events | `/events/` | real |
| 5 | Header | Moments | `/moments/` | real |
| 6 | Header | More | `/rankings/` | real |
| 7 | Header dd | Current Stars | `/wrestlers/current/` | GAP→`/wrestlers/` |
| 8 | Header dd | Legends | `/wrestlers/legends/` | GAP→`/wrestlers/` |
| 9 | Header dd | Women's Division | `/wrestlers/women/` | GAP→`/wrestlers/` |
| 10 | Header dd | Hall of Fame | `/hall-of-fame/` | GAP |
| 11 | Header dd | Media & Creators | `/media/` | GAP |
| 12 | Header dd | NJPW | `/promotions/njpw/` | GAP |
| 13 | Header | Join Wrestle Lore | `/membership/` | real |
| 14 | Hero | Join Wrestle Lore | `/membership/` | real |
| 15 | Hero | Browse wrestlers | `/wrestlers/` | real |
| 16 | Hero | Featured match poster | `/matches/undertaker-vs-hbk-wm25/` | real |
| 17 | 5A | Current Stars lane | `/wrestlers/current/` | GAP→`/wrestlers/` |
| 18 | 5A | Legends lane | `/wrestlers/legends/` | GAP→`/wrestlers/` |
| 19 | 5A | Women's Division lane | `/wrestlers/women/` | GAP→`/wrestlers/` |
| 20 | 5A | Full Roster lane | `/wrestlers/` | real |
| 21 | 5B | Roman Reigns | `/wrestlers/roman-reigns/` | real |
| 22 | 5B | Cody Rhodes | `/wrestlers/cody-rhodes/` | real |
| 23 | 5B | Rhea Ripley | `/wrestlers/rhea-ripley/` | real |
| 24 | 5B | Bianca Belair | `/wrestlers/bianca-belair/` | real |
| 25 | 5B | Gunther | `/wrestlers/gunther/` | real |
| 26 | 5B | CM Punk | `/wrestlers/cm-punk/` | real |
| 27 | 5B | Becky Lynch | `/wrestlers/becky-lynch/` | real |
| 28 | 5B | Stone Cold Steve Austin | `/wrestlers/stone-cold-steve-austin/` | real |
| 29 | 5B | The Undertaker | `/wrestlers/the-undertaker/` | real |
| 30 | 5B | Sting | `/wrestlers/sting/` | real |
| 31 | 5B | Ric Flair | `/wrestlers/ric-flair/` | real |
| 32 | 5B | Trish Stratus | `/wrestlers/trish-stratus/` | real |
| 33 | 5B | AJ Styles | `/wrestlers/aj-styles/` | real |
| 34 | 5B | Shinsuke Nakamura | `/wrestlers/shinsuke-nakamura/` | real |
| 35 | 5B | Jon Moxley | `/wrestlers/jon-moxley/` | real |
| 36 | 5B | Rey Mysterio | `/wrestlers/rey-mysterio/` | real |
| 37 | 5B | See all 89 | `/wrestlers/` | real |
| 38 | 6A | WrestleMania 42 (2026) | `/events/wrestlemania-42-2026/` | real |
| 39 | 6A | Night of Champions 2026 | `/events/night-of-champions-2026/` | real |
| 40 | 6A | Backlash 2026 | `/events/backlash-2026/` | real |
| 41 | 6A | Royal Rumble 2026 | `/events/royal-rumble-2026/` | real |
| 42 | 6A | Elimination Chamber 2026 | `/events/elimination-chamber-2026/` | real |
| 43 | 6B | WrestleMania (series) | `/events/wrestlemania/` | real |
| 44 | 6B | Royal Rumble (series) | `/events/royal-rumble/` | real |
| 45 | 6B | Elimination Chamber (series) | `/events/elimination-chamber/` | real |
| 46 | 6B | Night of Champions (series) | `/events/night-of-champions/` | real |
| 47 | 6B | Backlash (series) | `/events/backlash/` | real |
| 48 | 6C | WWE (facet) | `/promotions/wwe/` | real |
| 49 | 6C | WCW (facet) | `/promotions/wcw/` | real |
| 50 | 6C | ECW (facet) | `/promotions/ecw/` | real |
| 51 | 6C | TNA (facet) | `/promotions/tna/` | real |
| 52 | 6C | NJPW (facet) | `/promotions/njpw/` | GAP |
| 53 | 6C | NXT (facet) | `/promotions/nxt/` | real |
| 54 | 6C | All events | `/events/` | real |
| 55 | 7 | WWE brand card | `/promotions/wwe/` | real |
| 56 | 7 | NJPW brand card | `/promotions/njpw/` | GAP |
| 57 | 7 | TNA brand card | `/promotions/tna/` | real |
| 58 | 7 | WCW brand card | `/promotions/wcw/` | real |
| 59 | 7 | ECW brand card | `/promotions/ecw/` | real |
| 60 | 7 | NXT brand card | `/promotions/nxt/` | real |
| 61 | 7 | (card features) Roman/Cody/AJ/Nakamura/Samoa Joe/Sting/Goldenberg/Foley/Gunther | respective `/wrestlers/*/` | real (RVD is GAP) |
| 62 | 8A | Ric Flair (most-decorated) | `/wrestlers/ric-flair/` | real |
| 63 | 8B | Triple H (2025) | `/wrestlers/triple-h/` | real |
| 64 | 8B | Lex Luger (2025 co) | `/wrestlers/lex-luger/` | real |
| 65 | 8B | Paul Heyman (2024) | `/hall-of-fame/#2024` | GAP |
| 66 | 8B | Rey Mysterio (2023) | `/wrestlers/rey-mysterio/` | real |
| 67 | 8B | The Undertaker (2022) | `/wrestlers/the-undertaker/` | real |
| 68 | 8B | Vader (2022 co) | `/wrestlers/vader/` | real |
| 69 | 8B | Kane (2021) | `/wrestlers/kane/` | real |
| 70 | 8C | Shawn Michaels | `/wrestlers/shawn-michaels/` | real |
| 71 | 8C | Booker T | `/wrestlers/booker-t/` | real |
| 72 | 8C | Scott Hall (Razor Ramon) | `/wrestlers/razor-ramon/` | real |
| 73 | 8C | Kevin Nash | `/wrestlers/kevin-nash/` | real |
| 74 | 8C | Hulk Hogan | `/wrestlers/hulk-hogan/` | real |
| 75 | 8 | Full Hall of Fame | `/hall-of-fame/` | GAP |
| 76 | 9 | AJ Styles (hero) | `/wrestlers/aj-styles/` | real |
| 77 | 9 | Step 1 TNA | `/promotions/tna/` | real |
| 78 | 9 | Step 2 NJPW/Bullet Club | `/promotions/njpw/` | GAP |
| 79 | 9 | Step 3 WWE | `/promotions/wwe/` | real |
| 80 | 9 | Shinsuke Nakamura | `/wrestlers/shinsuke-nakamura/` | real |
| 81 | 9 | Jon Moxley | `/wrestlers/jon-moxley/` | real |
| 82 | 9 | Finn Balor | `/wrestlers/finn-balor/` | real |
| 83 | 9 | Explore New Japan | `/promotions/njpw/` | GAP |
| 84 | 10 | Chris Van Vliet (hero) | `/media/chris-van-vliet/` | GAP |
| 85 | 10 | Media grid (Paquette, Rosenberg, Helwani, Sapp, Salcedo, Meltzer) | `/media/{slug}/` | GAP |
| 86 | 10 | All media | `/media/` | GAP |
| 87 | 11A | 6 five-star matches | `/matches/*/` (per §11A) | real |
| 88 | 11A | All rankings | `/rankings/` | real |
| 89 | 11B | 6 rivalries | `/rivalries/*/` (per §11B) | real |
| 90 | 11B | All rivalries | `/rivalries/` | real |
| 91 | 11C | 4 moments | `/moments/*/` (per §11C) | real |
| 92 | 11C | All moments | `/moments/` | real |
| 93 | 11D | Families/Couples/Factions | `/relationships/#…` | real |
| 94 | 11D | Explore the map | `/relationships/` | real |
| 95 | 12A | Get early access | `/membership/` | real |
| 96 | 12D | Keep-going: current/HOF/NJPW/rankings/events/rivalries | per §12D | mixed (3 GAP) |
| 97 | 12E | Join Wrestle Lore (final) | `/membership/` | real |
| 98 | Footer | Database/Promotions/HOF/Media/中文/About/Methodology links | respective paths | real (+GAP HOF/Media/NJPW) |

---

## 16. JSON-LD on the homepage (GEO)

Update the three existing blocks and add one: `Organization` (name "Wrestle Lore"), `WebSite` (with
`SearchAction` → `/wrestlers/?q={query}`), `FAQPage` (the §12C questions), and add `ItemList` for the
Five-Star rail (each item = match page URL + name). All `name`/`url` use the Wrestle Lore identity and
final production domain. Do not fabricate `AggregateRating` values.

---

## 17. Build order for this page

1. Add tokens + chip/tile variants to `css/site.css` (§2), plus `.brand-card` and `.tile__fact`.
2. Rename all strings to Wrestle Lore (§12, header, footer, meta, JSON-LD).
3. Build the highest-priority gap pages that this homepage links to (`/promotions/njpw/`,
   `/hall-of-fame/`, the three wrestler facet hubs, `/media/`) or wire the named interim fallbacks so
   nothing 404s.
4. Assemble sections in DOM order §3→§12, reusing existing components; add the filter-pill JS
   (progressive enhancement) and the tile hover-fact.
5. Verify every link in §15 resolves; verify counts in §4; run the anti-AI copy pass on all new strings.
