# Wrestle Lore — Mega-Nav Specification (Direction B evolved)

Buildable spec for the final Wrestle Lore mega-navigation. It evolves the chosen "Editorial Poster
Wall" (Direction B) into a wider, more colorful, more separated instrument that satisfies every revamp
requirement. Every clickable in this document maps to a real page under `/root/wwe/`; targets that do
not yet exist are marked `GAP (build)` and collected in section 9 so no link ships as a 404.

- Author: mega-nav designer. Date: 2026-07-26.
- Source of facts: `00-content-data-research.md` and `01-inspiration-research.md` in this folder. No
  facts are invented here. Streaming, Hall of Fame, and roster facts carry the same confidence flags
  as the research docs. Copy rules: no decorative arrows in CTAs, no em-dash sentence separators, no
  marketing-cliché banned words, specific nouns.
- Base aesthetic kept: dark arena theme, Anton display, Oswald condensed UI, Inter body, gold hairline
  top-rule on every panel, CSS-only duotone poster tiles with monograms and scanlines (no images).

---

## 1. Key decisions (read first)

1. **The bar grows from 5 tabs to 7 tabs plus search.** Final bar, left to right:
   **Wrestlers · Matches · Events · Promotions · Hall of Fame · Media · More**, then a right-pinned
   `⌘K` search pill. Promotions, Hall of Fame, and Media are promoted to top level to carry the new
   requirements (brands/streaming, HOF showcase, influencers). Moments moves into the More panel as a
   full poster row (it holds only four items) and keeps its own index page.
2. **Color does more work.** Six promotion accents (WWE/WCW/ECW/TNA/NXT plus the new **NJPW**) plus
   six non-promotion category tokens (Current, Legend, Women's, Men's, Hall of Fame, Media, Era).
   Shape encodes the axis so color is never ambiguous (section 3).
3. **Wrestlers separate on four axes inside one panel:** status (Current vs Legend), division
   (Women's vs Men's), promotion (six chips including NJPW), and era. AJ Styles is the lead feature
   tile.
4. **Promotions is a dedicated tab of brand cards** that each show positioning plus a "Where to watch"
   chip row (verified streaming homes), and add NJPW as the sixth promotion.
5. **Every panel is present in raw HTML at load.** JavaScript only toggles visibility. This keeps the
   nav fully crawlable and gives search engines and answer engines the internal-link graph.

---

## 2. Tab architecture and responsive behavior

### 2.1 The bar
- Sticky header, `background:rgba(10,11,13,.9)` with `backdrop-filter:blur(12px)`, `1px` bottom line.
  Min height 70px. Max content width `--wrap` (1200px), 24px side padding.
- Brand lockup at far left: Anton wordmark **Wrestle Lore** with a boxed monogram tile `WL`
  (`36px`, gold-bright text `#f2cc4b`, `1px` border `--c-gold-dim`, `--r-md`). Links to `/`.
- Seven tab links in Oswald 15px, uppercase, `letter-spacing:.1em`, 24px vertical padding. Each tab is
  a real `<a>` to its index page and also opens a panel on hover/focus.
- A flexible spacer pushes the search pill to the right: rounded pill, magnifier glyph, label "Search",
  `kbd` showing `⌘K`. Opens the existing command palette.

### 2.2 Tab set and what each opens

| # | Tab label | Tab link (index) | Panel type | Exists? |
|---|---|---|---|---|
| 1 | Wrestlers | `/wrestlers/` | Four-axis poster panel | index EXISTS |
| 2 | Matches | `/matches/` | Poster + rating chips | index EXISTS |
| 3 | Events | `/events/` | Poster + brand/year/promotion chips | index EXISTS |
| 4 | Promotions | `/promotions/` | Brand-card grid with streaming chips | index EXISTS |
| 5 | Hall of Fame | `/hall-of-fame/` | Hero + classes + two-time club | hub GAP (build) |
| 6 | Media | `/media/` | Hero + creator grid | hub GAP (build) |
| 7 | More | `/rankings/` | Moments row + utility links | index EXISTS |

### 2.3 Responsive
- **>=1080px:** full bar, hover-to-open dropdown panels, poster grids at four to six columns.
- **840–1079px:** tab labels stay; panels drop to three columns; brand cards to two columns.
- **<840px:** collapse to a hamburger drawer. The seven tabs become a vertical accordion (each tab a
  toggle button that expands its panel inline). Poster rows scroll horizontally inside each expanded
  section. Search pill becomes a full-width row at the top of the drawer.
- Panels never exceed viewport height; long panels scroll inside themselves (`max-height:80vh;
  overflow:auto`).

---

## 3. Color and badge system

### 3.1 Tokens (add the new ones to `css/site.css`)

Existing promotion accents (keep):
```
--c-wwe:#c8102e;  --c-wcw:#e2b13c;  --c-ecw:#b0b0b0;  --c-tna:#1e73be;  --c-nxt:#f5c518;
```
Add:
```
--c-njpw:#d21c1c;            /* NJPW red — VERIFY against official NJPW branding before lock */
--c-current:var(--c-red);    /* status: active 2026            (#e11d2a) */
--c-legend:var(--c-gold);    /* status: retired/historic       (#d4af37) */
--c-women:#d6409f;           /* division: women's — magenta, unused elsewhere */
--c-men:#5b6b82;             /* division: men's — steel, low-chroma so it never competes */
--c-hof:#6b46c1;             /* hall of fame — royal purple, paired with gold */
--c-media:#1fb6c4;           /* media & creators — broadcast teal */
--c-era:#9a7b3f;             /* era — single bronze family, tinted by lightness per era */
```
Each color also gets a `-tint` (rgba at .12) for badge fills, matching the existing
`--c-gold-tint` / `--c-red-tint` pattern.

NJPW differentiation from WWE red: NJPW tiles use a **black field with a white top hairline** and the
`NJ` monogram, while WWE uses its accent gradient with the gold hairline. Same-family reds never sit
adjacent because promotion order in every rail is WWE, WCW, ECW, TNA, NXT, NJPW (NJPW last).

### 3.2 Shape encodes the axis (color is never ambiguous)

| Badge | Shape / CSS | Encodes | Values and colors |
|---|---|---|---|
| **Status pill** | fully rounded `--r-pill`, tinted fill + colored border | Current vs Legend | Current = red, Legend = gold |
| **Division chip** | `--r-md` (8px) soft rectangle | Women's vs Men's / tag / faction | Women's = magenta, Men's = steel |
| **Era tag** | `--r-sm` (4px), uppercase, `letter-spacing:.08em` | era band | bronze family, label carries the year range |
| **Promotion rule** | 3px left border on rows, gradient art on tiles | home promotion | six promotion accents |
| **Section token** | panel top-rule + headline underline | which tab you are in | gold default; HOF = purple; Media = teal |

Result: a poster tile can show a red *pill* (Current), a magenta *chip* (Women's), and a WWE-red
*gradient* at once and read cleanly, because pill vs chip vs field are distinct shapes.

---

## 4. Component specs

### 4.1 Panel shell (all tabs)
- `position:absolute; top:100%; left:0;` spanning the wrap; `background:#0c0d10`;
  `border:1px solid --c-line`; `border-top:2px solid` the section token (gold, or purple for HOF, or
  teal for Media); `box-shadow:0 40px 90px rgba(0,0,0,.65)`; 30px padding; `min-width:720px`.
- Header: `.phead` Anton uppercase ~1.6rem headline, `.psub` Oswald uppercase kicker 11px.
- Open animation: fade plus 8px rise, 200ms, `--ease`. Disabled under reduced motion.

### 4.2 Poster tile (the core unit, evolved)
- `.poster` wraps `.art` (the graphic) + `.cap` (name/sub).
- **People/media art:** aspect 3/4. **Event/brand art:** aspect 16/10 landscape.
- Art background is a **two-stop duotone** carrying more color than the old single accent:
  `linear-gradient(155deg, var(--promo), color-mix(in oklab, var(--status) 22%, transparent), #0b0c0f 74%)`.
- Scanline overlay via `::after` repeating-linear-gradient at 3% white (kept from Direction B).
- Anton monogram initials centered, `rgba(255,255,255,.92)`.
- **Overlays (new):** top-left status **pill** (Current/Legend), bottom-right promotion **tag**.
- **Hover reveal (CSS only):** a one-line fact strip rises over the lower art (rating, era, or one
  signature fact). On touch, that fact sits under the tile in `.cap`.
- Hover motion: `translateY(-4px)`, border shifts to the tile accent. Reduced motion keeps only the
  border change.

### 4.3 Brand / streaming card (Promotions tab)
- Header band in the promotion accent with the monogram tile and promotion name.
- One positioning line (specific nouns, no clichés).
- **"Where to watch" chip row:** small text chips (never logos, to avoid trademark image issues), each
  labeling platform plus region, for example `Raw · Netflix`, `PLEs · ESPN (US)`, `PLEs · Netflix (intl)`.
- Footer links: "Events" and "Top wrestlers" for that promotion.

### 4.4 Category chip rail
- Horizontal wrap of `.plink` pills, Oswald uppercase 12px. Promotion chips tint to their accent on
  hover; status/division/era chips tint to their token. Used for the faceted browse axes.

### 4.5 Hall of Fame class card
- Landscape tile: class year in Anton, headline inductee name, co-inductees as a small caption. Links
  to the headline inductee's existing profile where one exists, otherwise to the HOF hub class anchor.

### 4.6 Media creator card
- Portrait tile, teal token. Name, one-line role (interviewer, podcaster, journalist). Links to a
  `/media/{slug}/` page. All media pages are GAP until built (section 9).

### 4.7 Command palette (`⌘K`)
- Unchanged behavior from the existing build: overlay, fuzzy search over the generated index, keyboard
  driven. Rename any "MAT" strings to "Wrestle Lore". Opens on `⌘K`, `Ctrl-K`, or `/`.

---

## 5. Panel-by-panel content

### 5.1 Wrestlers panel (four axes)
- **Headline:** "Wrestlers" / kicker "89 profiles across six promotions".
- **Featured poster row (6 tiles, all EXIST):**
  1. **AJ Styles** (lead feature) `/wrestlers/aj-styles/` — TNA + NJPW + WWE duotone. Copy: "The
     Phenomenal One. TNA franchise player, Bullet Club founder, former IWGP Heavyweight Champion, and
     multi-time WWE Champion." Do NOT state he retired (retirement is `VERIFY`, single-source).
  2. Roman Reigns `/wrestlers/roman-reigns/`
  3. Cody Rhodes `/wrestlers/cody-rhodes/`
  4. Rhea Ripley `/wrestlers/rhea-ripley/` (Women's pill)
  5. Becky Lynch `/wrestlers/becky-lynch/` (Women's pill)
  6. The Undertaker `/wrestlers/the-undertaker/` (Legend pill)
- **Status chips:** Current `/wrestlers/current/` `GAP`; Legends `/wrestlers/legends/` `GAP`.
- **Division chips:** Women `/wrestlers/women/` `GAP`; Men `/wrestlers/men/` `GAP`.
- **By promotion chips:** WWE `/promotions/wwe/`, WCW `/promotions/wcw/`, ECW `/promotions/ecw/`,
  TNA `/promotions/tna/`, NXT `/promotions/nxt/`, NJPW `/promotions/njpw/` `GAP`.
- **By era chips:** Golden Era, New Generation, Attitude Era, Ruthless Aggression, PG Era, Modern —
  each `/wrestlers/era/{slug}/` `GAP`.
- **See all:** "All wrestlers A to Z" `/wrestlers/` EXISTS.
- Sami Zayn stays here (`/wrestlers/sami-zayn/`), never in Media.

### 5.2 Matches panel
- **Headline:** "Matches" / kicker "Every rated bout".
- **Poster row (EXIST):** Undertaker vs HBK at WrestleMania 25 `/matches/undertaker-vs-hbk-wm25/`;
  CM Punk vs Cena at Money in the Bank 2011 `/matches/cm-punk-vs-cena-mitb-2011/`; plus two more
  editor picks from `/matches/`. (Confirm exact slugs against `/matches/` at build.)
- **Chips:** All matches `/matches/`; Five-star club `/rankings/` EXISTS; by promotion chips reuse the
  six promotion links above.

### 5.3 Events panel (separation by series, year, promotion)
- **Headline:** "Premium Live Events" / kicker "Results and where to watch".
- **Recent PLE poster row (EXIST), each with a streaming tag "ESPN (US) / Netflix (intl)":**
  WrestleMania 42 `/events/wrestlemania-42-2026/`; Royal Rumble 2026 `/events/royal-rumble-2026/`;
  Elimination Chamber 2026 `/events/elimination-chamber-2026/`; Backlash 2026 `/events/backlash-2026/`;
  Night of Champions 2026 `/events/night-of-champions-2026/`.
- **By series chips (EXIST):** WrestleMania `/events/wrestlemania/`, Royal Rumble
  `/events/royal-rumble/`, Elimination Chamber `/events/elimination-chamber/`, Night of Champions
  `/events/night-of-champions/`, Backlash `/events/backlash/`.
- **By year chip:** 2026 `/events/2026/` `GAP` (interim target `/events/`).
- **By promotion chips:** WWE `/promotions/wwe/` EXISTS; WCW/ECW/TNA/NJPW event hubs `GAP`.
- **See all:** All events `/events/` EXISTS.

### 5.4 Promotions panel (brand cards + streaming)
Six brand cards. Streaming facts from `00-content-data-research.md`. Chips are text, region-labeled.

| Card | Link | "Where to watch" chips | Confidence |
|---|---|---|---|
| **WWE** | `/promotions/wwe/` | `Raw · Netflix` · `SmackDown · USA Network` · `NXT · The CW` · `PLEs · ESPN (US)` · `PLEs · Netflix (intl)` | HIGH |
| **NXT** | `/promotions/nxt/` | `The CW (US)` · `Netflix (archive, intl)` | HIGH |
| **NJPW** | `/promotions/njpw/` `GAP` | `NJPW World` · `TrillerTV` | HIGH (accent color VERIFY) |
| **TNA** | `/promotions/tna/` | `AMC & AMC+ (live)` · `TNA+ (streaming)` · `Prime Video (library)` | HIGH |
| **WCW** | `/promotions/wcw/` | `WWE archive · Netflix` | MED / VERIFY US home |
| **ECW** | `/promotions/ecw/` | `WWE archive · Netflix` | MED / VERIFY US home |
- Each card footer: "Events" and "Top wrestlers" for that promotion (both resolve to the promotion
  page section for now).
- NJPW card cross-links **AJ Styles** `/wrestlers/aj-styles/`, **Shinsuke Nakamura**
  `/wrestlers/shinsuke-nakamura/`, **Jon Moxley** `/wrestlers/jon-moxley/`, **Finn Balor**
  `/wrestlers/finn-balor/` (all EXIST) as the Bullet Club / IWGP tie-ins.

### 5.5 Hall of Fame panel
- Section token switches to purple (`--c-hof`) with a gold hairline.
- **Most-decorated hero tile:** **Ric Flair** `/wrestlers/ric-flair/`, badge "2x HOF". Copy:
  "Two-time inductee. Inducted solo in 2008 and again in 2012 with the Four Horsemen." (HIGH)
- **Two-Time Club chip row (status HIGH; do not print solo years, they are VERIFY):**
  Shawn Michaels `/wrestlers/shawn-michaels/`, Booker T `/wrestlers/booker-t/`,
  Scott Hall `/wrestlers/razor-ramon/`, Kevin Nash `/wrestlers/kevin-nash/`,
  Hulk Hogan `/wrestlers/hulk-hogan/`.
- **Last 5 classes poster row:**
  - 2025 Triple H `/wrestlers/triple-h/` (co: Lex Luger `/wrestlers/lex-luger/`) EXISTS
  - 2024 Paul Heyman `/hall-of-fame/#class-2024` `GAP` (no inductee page yet)
  - 2023 Rey Mysterio `/wrestlers/rey-mysterio/` EXISTS (co: Great Muta `GAP`)
  - 2022 The Undertaker `/wrestlers/the-undertaker/` (co: Vader `/wrestlers/vader/`) EXISTS
  - 2021 Kane `/wrestlers/kane/` EXISTS
- **See all classes:** `/hall-of-fame/` `GAP (build)`.

### 5.6 Media panel
- Section token teal (`--c-media`).
- **Hero:** **Chris Van Vliet** `/media/chris-van-vliet/` `GAP`. Copy: "Emmy-winning host of the
  Insight interview show." (person HIGH; page GAP)
- **Proposed creator grid (all GAP, each `VERIFY` affiliation before publishing):** Renee Paquette,
  Peter Rosenberg, Ariel Helwani, Sean Ross Sapp, Denise Salcedo, Dave Meltzer / Wade Keller.
  Targets `/media/{slug}/`.
- **Handoff note printed nowhere on the tab but recorded here:** Sami Zayn is an active wrestler and
  belongs on the Wrestlers grid, not here.
- This tab ships only after `/media/` and at least `/media/chris-van-vliet/` exist (section 9). Until
  then, hide the tab rather than link to a 404.

### 5.7 More panel
- **Moments poster row (EXIST):** Mankind's Hell in a Cell fall
  `/moments/mankind-hell-in-a-cell-fall-1998/`; Triple H tears his quad
  `/moments/triple-h-tears-his-quad-2001/`; Kane's debut `/moments/kane-debut-badd-blood-1997/`;
  Steve Austin breaks his neck `/moments/steve-austin-broken-neck-1997/`. "All moments" `/moments/`.
- **Utility chips (EXIST):** Rivalries `/rivalries/`, Relationships `/relationships/`, Rankings
  `/rankings/`, Methodology `/methodology/`, About `/about/`, 中文 `/zh/`.

---

## 6. Interaction layers

### 6.1 Hover and click
- Mouse enter opens the panel; mouse leave closes after a 180ms delay (prevents flicker crossing the
  gap). Clicking a tab toggles its panel and closes any other open panel. Clicking the tab label a
  second time, or clicking outside, closes it. (Same pattern the existing preview JS already uses.)

### 6.2 Keyboard and ARIA
- Each tab link carries `aria-haspopup="true"` and `aria-expanded` reflecting open state; the panel has
  a matching `id` referenced by `aria-controls`.
- `Tab` moves across the seven tab links and the search pill.
- `Enter` or `Space` on a focused tab opens its panel and moves focus to the first link inside.
- `ArrowDown` from a tab opens and enters the panel; `ArrowUp`/`ArrowDown` and `ArrowLeft`/`ArrowRight`
  move a roving `tabindex` across the poster grid and chip rails.
- `Escape` closes the open panel and returns focus to its tab.
- `⌘K`, `Ctrl-K`, and `/` open the command palette from anywhere.
- Focus-visible ring uses `--c-focus` (#5aa9ff), 2px outline, on tabs, tiles, and chips.

### 6.3 Mobile drawer
- Hamburger toggles a full-height drawer. Tabs become accordion toggles (`aria-expanded` on each).
  Only one section open at a time. Poster rows scroll horizontally with momentum; chips wrap.

### 6.4 Reduced motion
- Under `prefers-reduced-motion: reduce`, disable panel rise, tile lift, and hover-reveal transitions.
  Keep instant opacity changes and border-color feedback.

### 6.5 Crawlability (hard constraint)
- All panel markup, including every `<a>` in section 7, is rendered in the initial HTML. JavaScript
  only adds/removes an `open` class. With JS disabled, tabs are plain links to their index pages and
  every panel link remains in the DOM and reachable. No link target is injected by script.

---

## 7. Master clickable to link-target table

Legend: **E** = page exists today. **G** = GAP, build before this link ships (section 9).

| Tab | Clickable label | Target | State |
|---|---|---|---|
| Brand | Wrestle Lore (wordmark) | `/` | E |
| Wrestlers | Wrestlers (tab) | `/wrestlers/` | E |
| Wrestlers | AJ Styles (feature) | `/wrestlers/aj-styles/` | E |
| Wrestlers | Roman Reigns | `/wrestlers/roman-reigns/` | E |
| Wrestlers | Cody Rhodes | `/wrestlers/cody-rhodes/` | E |
| Wrestlers | Rhea Ripley | `/wrestlers/rhea-ripley/` | E |
| Wrestlers | Becky Lynch | `/wrestlers/becky-lynch/` | E |
| Wrestlers | The Undertaker | `/wrestlers/the-undertaker/` | E |
| Wrestlers | Current (status) | `/wrestlers/current/` | G |
| Wrestlers | Legends (status) | `/wrestlers/legends/` | G |
| Wrestlers | Women (division) | `/wrestlers/women/` | G |
| Wrestlers | Men (division) | `/wrestlers/men/` | G |
| Wrestlers | WWE | `/promotions/wwe/` | E |
| Wrestlers | WCW | `/promotions/wcw/` | E |
| Wrestlers | ECW | `/promotions/ecw/` | E |
| Wrestlers | TNA | `/promotions/tna/` | E |
| Wrestlers | NXT | `/promotions/nxt/` | E |
| Wrestlers | NJPW | `/promotions/njpw/` | G |
| Wrestlers | Golden Era | `/wrestlers/era/golden-era/` | G |
| Wrestlers | New Generation | `/wrestlers/era/new-generation/` | G |
| Wrestlers | Attitude Era | `/wrestlers/era/attitude-era/` | G |
| Wrestlers | Ruthless Aggression | `/wrestlers/era/ruthless-aggression/` | G |
| Wrestlers | PG Era | `/wrestlers/era/pg-era/` | G |
| Wrestlers | Modern | `/wrestlers/era/modern/` | G |
| Wrestlers | All wrestlers A to Z | `/wrestlers/` | E |
| Matches | Matches (tab) | `/matches/` | E |
| Matches | Undertaker vs HBK (WM25) | `/matches/undertaker-vs-hbk-wm25/` | E (verify slug) |
| Matches | CM Punk vs Cena (MITB '11) | `/matches/cm-punk-vs-cena-mitb-2011/` | E (verify slug) |
| Matches | All matches | `/matches/` | E |
| Matches | Five-star club | `/rankings/` | E |
| Events | Events (tab) | `/events/` | E |
| Events | WrestleMania 42 | `/events/wrestlemania-42-2026/` | E |
| Events | Royal Rumble 2026 | `/events/royal-rumble-2026/` | E |
| Events | Elimination Chamber 2026 | `/events/elimination-chamber-2026/` | E |
| Events | Backlash 2026 | `/events/backlash-2026/` | E |
| Events | Night of Champions 2026 | `/events/night-of-champions-2026/` | E |
| Events | WrestleMania (series) | `/events/wrestlemania/` | E |
| Events | Royal Rumble (series) | `/events/royal-rumble/` | E |
| Events | Elimination Chamber (series) | `/events/elimination-chamber/` | E |
| Events | Night of Champions (series) | `/events/night-of-champions/` | E |
| Events | Backlash (series) | `/events/backlash/` | E |
| Events | 2026 (year) | `/events/2026/` | G (interim `/events/`) |
| Events | All events | `/events/` | E |
| Promotions | Promotions (tab) | `/promotions/` | E |
| Promotions | WWE card | `/promotions/wwe/` | E |
| Promotions | NXT card | `/promotions/nxt/` | E |
| Promotions | NJPW card | `/promotions/njpw/` | G |
| Promotions | TNA card | `/promotions/tna/` | E |
| Promotions | WCW card | `/promotions/wcw/` | E |
| Promotions | ECW card | `/promotions/ecw/` | E |
| Promotions | NJPW tie: Shinsuke Nakamura | `/wrestlers/shinsuke-nakamura/` | E |
| Promotions | NJPW tie: Jon Moxley | `/wrestlers/jon-moxley/` | E |
| Promotions | NJPW tie: Finn Balor | `/wrestlers/finn-balor/` | E |
| Hall of Fame | Hall of Fame (tab) | `/hall-of-fame/` | G |
| Hall of Fame | Ric Flair (most-decorated) | `/wrestlers/ric-flair/` | E |
| Hall of Fame | Shawn Michaels (2x club) | `/wrestlers/shawn-michaels/` | E |
| Hall of Fame | Booker T (2x club) | `/wrestlers/booker-t/` | E |
| Hall of Fame | Scott Hall (2x club) | `/wrestlers/razor-ramon/` | E |
| Hall of Fame | Kevin Nash (2x club) | `/wrestlers/kevin-nash/` | E |
| Hall of Fame | Hulk Hogan (2x club) | `/wrestlers/hulk-hogan/` | E |
| Hall of Fame | 2025 class: Triple H | `/wrestlers/triple-h/` | E |
| Hall of Fame | 2025 co: Lex Luger | `/wrestlers/lex-luger/` | E |
| Hall of Fame | 2024 class: Paul Heyman | `/hall-of-fame/#class-2024` | G |
| Hall of Fame | 2023 class: Rey Mysterio | `/wrestlers/rey-mysterio/` | E |
| Hall of Fame | 2022 class: The Undertaker | `/wrestlers/the-undertaker/` | E |
| Hall of Fame | 2022 co: Vader | `/wrestlers/vader/` | E |
| Hall of Fame | 2021 class: Kane | `/wrestlers/kane/` | E |
| Hall of Fame | See all classes | `/hall-of-fame/` | G |
| Media | Media (tab) | `/media/` | G |
| Media | Chris Van Vliet (hero) | `/media/chris-van-vliet/` | G |
| Media | Renee Paquette | `/media/renee-paquette/` | G (VERIFY) |
| Media | Peter Rosenberg | `/media/peter-rosenberg/` | G (VERIFY) |
| Media | Ariel Helwani | `/media/ariel-helwani/` | G (VERIFY) |
| Media | Sean Ross Sapp | `/media/sean-ross-sapp/` | G (VERIFY) |
| Media | Denise Salcedo | `/media/denise-salcedo/` | G (VERIFY) |
| Media | Dave Meltzer | `/media/dave-meltzer/` | G (VERIFY) |
| More | More (tab) | `/rankings/` | E |
| More | Mankind Hell in a Cell fall | `/moments/mankind-hell-in-a-cell-fall-1998/` | E |
| More | Triple H tears his quad | `/moments/triple-h-tears-his-quad-2001/` | E |
| More | Kane's debut | `/moments/kane-debut-badd-blood-1997/` | E |
| More | Steve Austin breaks his neck | `/moments/steve-austin-broken-neck-1997/` | E |
| More | All moments | `/moments/` | E |
| More | Rivalries | `/rivalries/` | E |
| More | Relationships | `/relationships/` | E |
| More | Rankings | `/rankings/` | E |
| More | Methodology | `/methodology/` | E |
| More | About | `/about/` | E |
| More | 中文 | `/zh/` | E |
| Search | Search (⌘K) | opens command palette | E |

---

## 8. SEO / GEO notes for the nav

- Wrap the header nav in `SiteNavigationElement` JSON-LD listing the seven top targets, so answer
  engines read the site's shape from the nav itself.
- The panels are the internal-link backbone: every hub links down to spokes and every promotion,
  status, division, and era chip is a crawlable hub link. This is the same graph the "Keep going"
  blocks use on content pages (see `01-inspiration-research.md`, patterns 1 and 6).
- Each GAP hub, when built, ships `ItemList` JSON-LD plus an answer-first summary and a short FAQ, so
  the new facet pages are citable.

---

## 9. Companion pages to build before the nav is fully live

Ships-now links (state **E** in section 7) cover the majority of the nav today. To light up every
chip and satisfy requirements 2, 5, 6, and 7, build these companion pages (grouped by wave):

**Wave 1 (required to satisfy the named requirements):**
- `/promotions/njpw/` — NJPW brand + streaming card page (req 5). VERIFY accent `#d21c1c`.
- `/wrestlers/current/`, `/wrestlers/legends/`, `/wrestlers/women/`, `/wrestlers/men/` — status and
  division hubs (req 2).
- `/hall-of-fame/` hub with class anchors including `#class-2024` (req 6).
- `/media/` hub plus `/media/chris-van-vliet/` (req 7; needed before the Media tab ships).

**Wave 2 (fills remaining chips):**
- `/wrestlers/era/{golden-era,new-generation,attitude-era,ruthless-aggression,pg-era,modern}/`.
- `/events/2026/` year hub; WCW/ECW/TNA/NJPW event hubs.
- Remaining media pages (Paquette, Rosenberg, Helwani, Sapp, Salcedo, Meltzer) — each `VERIFY`.
- HOF inductee profiles missing pages (Paul Heyman, Great Muta, and other headliners in the research
  gap list).

Interim rule: any chip whose target is still GAP is either hidden or points to the nearest existing
index (Media tab hidden entirely; the 2026 year chip points to `/events/`) so nothing ships as a 404.

---

## 10. Copy and verification flags

- Rename every "MAT" string in the header, palette, titles, and `og:site_name` to **Wrestle Lore**.
- Do not state AJ Styles has retired (single-source `VERIFY`). Feature him as the TNA to NJPW to WWE
  journey instead.
- Do not print solo induction years for the Two-Time Club chips (years are `VERIFY`); the two-time
  status is HIGH and safe to show.
- Verify the NJPW brand red and the WCW/ECW streaming US home before lock.
- Verify each proposed media personality's current affiliation before their page and chip publish.
- Copy style: plain CTAs ("See all", "All events"), no decorative arrows, no em-dash separators, no
  banned marketing words, specific nouns throughout.
