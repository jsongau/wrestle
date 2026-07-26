# Wrestle Lore — Content Showcase Modules (spec 09)

Buildable spec for the four data-driven showcase modules of the Direction-B revamp:
(a) Promotion **brand cards** with "where to watch" streaming chips, (b) the **Hall of Fame** module
(last 5 classes + Ric Flair as most-decorated), (c) the **AJ Styles hero feature** (TNA -> NJPW ->
WWE arc), and (d) the **Media & Creators** tab roster.

- Author: content showcase designer. Date: 2026-07-26.
- Facts source: `00-content-data-research.md` and `01-inspiration-research.md` in this folder. No facts
  invented here. Every streaming/HOF/roster fact carries the research doc's confidence flag. Anything
  `VERIFY` must be confirmed before publish and, where a claim is unproven (AJ Styles retirement),
  the copy must not assert it.
- Base aesthetic kept from Direction B: dark arena theme, Anton display, Oswald condensed UI, Inter
  body, gold hairline top-rule on module headers, CSS-only duotone poster tiles with monograms and
  scanlines (no images yet). Reuses existing CSS components: `.tile`, `.card`, `.grid-3`, `.chip`,
  `.answer`, `.faq`, `.poster`, `.crumbs`.
- Copy rules enforced: no decorative arrows in CTAs, no em-dash sentence separators, no marketing
  cliches, specific nouns, no fabricated quotes or stats.
- Aligns with `03-mega-nav.md`: the bar carries **Promotions**, **Hall of Fame**, and **Media** as
  top-level tabs; this doc specs what lives on those hubs and the reusable modules that also embed on
  the homepage and relevant profile pages.

---

## 0. New CSS tokens this spec requires

Add to `css/site.css` `:root` (shared with the mega-nav spec so tokens are defined once):

```css
--c-njpw:#d21c1c;   /* NJPW red — VERIFY vs official NJPW branding before lock */
--c-aew:#c9a227;    /* AEW gold on black field — VERIFY; differentiate from WCW/NXT via black card + double rule */
--c-hof:#6b46c1;    /* Hall of Fame — royal purple, always paired with gold */
--c-media:#1fb6c4;  /* Media & Creators — broadcast teal */
--c-njpw-tint:rgba(210,28,28,.12);
--c-hof-tint:rgba(107,70,193,.14);
--c-media-tint:rgba(31,182,196,.12);
```

Two new chip variants (streaming chip is intentionally text, never a platform logo, to avoid
trademark-image issues; label US vs Intl explicitly):

```css
.chip--njpw{color:#fff;background:var(--c-njpw);border-color:var(--c-njpw);}
.chip--hof{color:#fff;background:var(--c-hof);border-color:var(--c-hof);}
.chip--media{color:#04252a;background:var(--c-media);border-color:var(--c-media);}
.chip--stream{color:var(--c-text);background:var(--c-bg-elev-2);border-color:var(--c-line-strong);
  font-family:var(--font-cond);letter-spacing:.02em;text-transform:none;}
.chip--stream b{color:var(--c-gold-bright);font-weight:700;} /* platform name */
.chip--verify{color:var(--c-gold-bright);background:transparent;border-color:var(--c-gold-dim);
  border-style:dashed;} /* renders as "VERIFY" pill in authoring/staging; strip or confirm before publish */
```

Badge shape rule (carried from A3/inspiration): **pill = status/promotion**, **stream-chip = where
to watch**, **flat text kicker = era/date**. Color alone never disambiguates; shape + color together do.

---

## MODULE A — Promotion brand cards ("Where to watch")

### A.1 Purpose and placement
A grid of brand cards that (1) positions each promotion in one factual line, (2) shows where each one
streams via a "Where to watch" chip row, and (3) links to the promotion hub, its top wrestlers, and
its events. Lives on `/promotions/` (replaces the current flat `.card` grid in
`promotions/index.html`), embeds as a 3-across rail on the homepage, and each card's streaming row is
reused verbatim on the individual promotion page and on that promotion's event cards.

Order on the grid: **active first** (WWE, AEW, NJPW, TNA, NXT), then a **Legacy** subsection
(WCW, ECW) under its own gold-hairline `.section-head` labeled "Legacy promotions".

### A.2 Card anatomy (component: `.brand-card`)
A taller variant of `.card`. Top to bottom:

1. **Accent header bar** (6px) in the promotion accent color; the whole card gets a
   `border-top:3px solid var(--c-{promo})`.
2. **Monogram + wordmark row**: CSS monogram tile (reuse `.tile__mono` treatment, ~3.5rem Anton
   initial in the accent color at low opacity) beside the full promotion name (Anton) and a one-line
   promotion chip (`.chip--{promo}`).
3. **Positioning line** (Inter, `--c-text-muted`, one sentence, specific nouns).
4. **"Where to watch" block**: eyebrow label `WHERE TO WATCH`, then a wrapped row of `.chip--stream`
   pills. Each pill shows the platform in bold plus a region/role qualifier, e.g.
   `<b>Netflix</b> Raw`, `<b>ESPN</b> PLEs · US`, `<b>NJPW World</b> all events`.
5. **Footer link row**: three text links — "Promotion hub", "Top wrestlers", "Events" — pointing at
   real anchors (see link table). Any target that is a GAP renders as a disabled state, never a live 404.

Whole card is not a single `<a>` (it holds multiple links); the header/monogram links to the hub, the
footer links to sub-targets.

### A.3 Exact content per card (verbatim, from research §1; confidence in brackets)

**WWE** (accent `--c-wwe` #c8102e, monogram "W")
- Positioning: "The industry leader. Raw, SmackDown, NXT and the Premium Live Events." [HIGH]
- Where to watch chips: `Netflix — Raw` [HIGH] · `USA Network — SmackDown` [HIGH] ·
  `The CW — NXT` [HIGH] · `ESPN — PLEs (US)` [HIGH] · `Netflix — PLEs (Intl)` [HIGH]
- Streaming sentence (used on hub): "Raw streams on Netflix. SmackDown airs on USA Network. Premium
  Live Events run on ESPN in the US and Netflix internationally."

**AEW** (accent `--c-aew` #c9a227 on black field, monogram "A") — **hub GAP (build `/promotions/aew/`)**
- Positioning: "All Elite Wrestling. Dynamite, Collision and the modern PPV calendar." [HIGH]
- Where to watch chips: `TBS — Dynamite` [HIGH] · `TNT — Collision` [HIGH] · `HBO Max — both` [HIGH] ·
  `AEW Plus on TrillerTV — Intl` [HIGH] · `PPVs on HBO Max / TrillerTV` [MED]
- Streaming sentence: "Dynamite on TBS, Collision on TNT, both on HBO Max. International fans use AEW
  Plus on TrillerTV."

**NJPW** (accent `--c-njpw` #d21c1c on near-black, monogram "N") — **hub GAP (build `/promotions/njpw/`)**
- Positioning: "New Japan Pro-Wrestling. Founded 1972, the largest promotion in Japan, home of the
  Tokyo Dome's Wrestle Kingdom." [HIGH]
- Where to watch chips: `NJPW World — all events` [HIGH] · `TrillerTV` [HIGH] ·
  `TV Asahi — Japan` [HIGH] · `Wrestle Kingdom, Jan 4` [HIGH]
- Streaming sentence: "Watch on NJPW World, the promotion's own subscription, plus TrillerTV."
- Note: NJPW red accent flagged `VERIFY` against official branding.

**TNA** (accent `--c-tna` #1e73be, monogram "T") — hub EXISTS `/promotions/tna/`
- Positioning: "TNA Wrestling. Thursday Night iMPACT and the X-Division." [HIGH]
- Where to watch chips: `AMC — iMPACT live` [HIGH] · `AMC+ — streaming` [HIGH] · `TNA+ — full library`
  [HIGH] · `Library seasons on Prime Video` [HIGH]
- Streaming sentence: "Thursday Night iMPACT on AMC and AMC+, with TNA+ for the full library. Older
  iMPACT seasons are listed on Prime Video."
- Directly answers the user's "is TNA on Amazon?" question in the card body copy.

**NXT** (accent `--c-nxt` #f5c518, monogram "X") — hub EXISTS `/promotions/nxt/`
- Positioning: "WWE NXT. The developmental brand and its TakeOver-era classics." [HIGH]
- Where to watch chips: `The CW — NXT (US)` [HIGH] · `Netflix — archives` [HIGH]

**Legacy — WCW** (accent `--c-wcw` #e2b13c, monogram "W") — hub EXISTS `/promotions/wcw/`
- Positioning: "World Championship Wrestling. Folded 2001. The nWo and 83 weeks atop the Monday Night
  Wars." [HIGH]
- Where to watch chips: `Library owned by WWE` [HIGH] · `Archive on Netflix` [MED / VERIFY US home]

**Legacy — ECW** (accent `--c-ecw` #b0b0b0, monogram "E") — hub EXISTS `/promotions/ecw/`
- Positioning: "Extreme Championship Wrestling. Folded 2001. The hardcore revolution." [HIGH]
- Where to watch chips: `Library owned by WWE` [HIGH] · `Archive on Netflix` [MED / VERIFY]

### A.4 Interaction layers
- Rest: accent border-top, muted body. Hover: `translateY(-2px)`, border brightens to accent color
  at 40%, monogram opacity rises (reuse `.card:hover` + `.tile:hover .tile__mono`). Legacy cards get a
  desaturated field (grayscale 20%) that clears on hover, signaling "archive".
- Stream chips are non-interactive labels; footer links are the interactive targets.
- Motion respects `prefers-reduced-motion` (existing base rule).

---

## MODULE B — Hall of Fame showcase

### B.1 Purpose and placement
The HOF hub `/hall-of-fame/` (**GAP, build**) and a condensed embed on the homepage. Structure follows
the leaderboard/collection pattern (B3): an answer-first summary, a **most-decorated hero**, a
**Two-Time Club** strip, and a **Last 5 Classes** timeline. Every inductee with a real page links to it;
inductees without pages render as non-link text tiles (labeled, never dead links) and are collected in
the GAP list.

### B.2 Answer-first + FAQ (GEO)
Lead with `.answer`: "The WWE Hall of Fame's most-decorated member is Ric Flair, a two-time inductee.
He entered in 2008 on his own and again in 2012 as a member of the Four Horsemen." [HIGH]
Add a `.faq` with, at minimum: "How many times is Ric Flair in the WWE Hall of Fame?" and "Who was
the most recent Hall of Fame headliner?" (answer: Triple H, 2025 [HIGH]). Ship `ItemList` +
`BreadcrumbList` JSON-LD; each class row is an `ItemList` entry.

### B.3 Most-decorated hero (component: `.poster` featured variant, HOF purple + gold)
- Full-width `.poster` with `--c-hof` gradient field, gold gradient-border, monogram "F".
- Content: eyebrow "MOST-DECORATED INDUCTEE", Anton headline "Ric Flair", stat line
  "Two-time WWE Hall of Famer" and two dated chips: `.chip--hof 2008 · Solo` and
  `.chip--hof 2012 · Four Horsemen`. [HIGH]
- CTA text link (no arrow): "Read the Ric Flair profile" -> `/wrestlers/ric-flair/` (EXISTS).

### B.4 Two-Time Club strip (component: horizontal `.tile` rail)
Five poster tiles, gold badge "2x HOF", each linking to its existing page. Solo-year labels are
`MED / VERIFY`; render the year in a `.chip--verify` state until confirmed, but the two-time status
itself is `HIGH` and prints plainly.

| Tile | Two inductions (VERIFY solo years) | Link target | Exists |
|---|---|---|---|
| Shawn Michaels | 2011 solo + 2019 DX | `/wrestlers/shawn-michaels/` | Yes |
| Booker T | 2013 solo + 2019 Harlem Heat | `/wrestlers/booker-t/` | Yes |
| Scott Hall (Razor Ramon) | 2014 solo + 2020 nWo | `/wrestlers/razor-ramon/` | Yes |
| Kevin Nash | 2015 solo + 2020 nWo | `/wrestlers/kevin-nash/` | Yes |
| Hulk Hogan | 2005 solo + 2020 nWo | `/wrestlers/hulk-hogan/` | Yes |

### B.5 Last 5 Classes timeline (component: five `.tile--gold` class cards in a rail)
Each class card: kicker = class year, `.tile__name` = headline inductee, sub-line = notable
co-inductees (text only). Headline inductee links to their page when it exists; co-inductees link only
if a page exists, otherwise plain text.

| Class | Headline (link) | Co-inductees shown (link if page exists) | Exists / GAP |
|---|---|---|---|
| 2025 | Triple H -> `/wrestlers/triple-h/` | Lex Luger -> `/wrestlers/lex-luger/`; Michelle McCool (GAP); The Natural Disasters (GAP) | Triple H, Lex Luger EXIST |
| 2024 | Paul Heyman (GAP, build `/wrestlers/paul-heyman/`) | Bull Nakano (GAP); U.S. Express (GAP); Muhammad Ali, celebrity (GAP); Barry Windham (GAP) | headliner GAP |
| 2023 | Rey Mysterio -> `/wrestlers/rey-mysterio/` | The Great Muta (GAP); Stacy Keibler (GAP); Andy Kaufman, celebrity (GAP) | Rey Mysterio EXISTS |
| 2022 | The Undertaker -> `/wrestlers/the-undertaker/` | Vader -> `/wrestlers/vader/`; Queen Sharmell (GAP); The Steiner Brothers (GAP) | Undertaker, Vader EXIST |
| 2021 | Kane -> `/wrestlers/kane/` | Eric Bischoff (GAP); Rob Van Dam (GAP); Molly Holly (GAP); The Great Khali (GAP) | Kane EXISTS |

All class/inductee facts [HIGH] from research §2. GAP pages to build listed in the consolidated GAP
list (§F). A class card whose headline is a GAP renders the name in plain text with a small "profile
coming" note, so the timeline is complete without shipping a 404.

---

## MODULE C — AJ Styles hero feature

### C.1 Purpose and placement
A three-promotion "journey" hero that (1) headlines the new NJPW push, (2) links TNA, NJPW and WWE
hubs from one unit, and (3) drives to the existing AJ Styles profile. Lives at the top of
`/promotions/njpw/` (when built), embeds on the homepage as a featured `.poster`, and cross-embeds on
`/promotions/tna/` and `/promotions/wwe/`. Profile already exists: `/wrestlers/aj-styles/` (EXISTS).

### C.2 Layout (component: `.poster` gradient-border feature + a 3-node arc rail)
- Left: full-height `.poster` field, monogram "AJ", eyebrow "THE PHENOMENAL ONE", Anton headline
  "AJ Styles", one-line positioning: "One of a small group of wrestlers to headline TNA, NJPW and
  WWE." [HIGH]
- Right: a **journey arc** of three linked nodes, each a compact `.card` with promotion chip + one
  factual line (no decorative arrows between nodes; use a plain hairline connector or numbered 1/2/3):

  1. `.chip--tna` **TNA** — "Longtime franchise player and multi-time World Champion." [HIGH]
     -> `/promotions/tna/` (EXISTS)
  2. `.chip--njpw` **NJPW** — "Original Bullet Club leader and IWGP Heavyweight Champion." [HIGH]
     -> `/promotions/njpw/` (GAP, build)
  3. `.chip--wwe` **WWE** — "Debuted at the 2016 Royal Rumble; multi-time WWE Champion." [HIGH]
     -> `/promotions/wwe/` (EXISTS)

- Signature-moves line (text): "Styles Clash. Phenomenal Forearm. Calf Crusher." [HIGH]
- Primary CTA text link: "Read the AJ Styles profile" -> `/wrestlers/aj-styles/` (EXISTS).
- Related tiles rail beneath (Bullet Club / NJPW ties, all existing): Shinsuke Nakamura
  (`/wrestlers/shinsuke-nakamura/`), Finn Balor (`/wrestlers/finn-balor/`), Jon Moxley
  (`/wrestlers/jon-moxley/`). Kenny Omega and Will Ospreay are GAP; omit until built.

### C.3 Career-status rule (critical)
The reported retirement at Royal Rumble 2026 is **single-source (`VERIFY`)**. The feature must **not**
state he retired. Ship the arc in present/career-summary tense. Only if confirmed, add a dated
"Career retrospective" ribbon; until then no retirement language, no past-tense "was". This is a hard
gate, not a preference.

---

## MODULE D — Media & Creators tab

### D.1 Purpose and placement
The `/media/` hub (**GAP, build**) presenting wrestling media personalities: interviewers,
podcasters, journalists. Accent `--c-media` teal so the whole tab reads as a distinct category on
sight. Structure: answer-first summary, one confirmed **hero**, then a **proposed roster grid** where
every unconfirmed entry carries a visible `VERIFY` state and links out only where a real, citable page
exists.

### D.2 Routing note the build team must honor
**Sami Zayn is an active wrestler, not media.** The user mentioned him; he stays on the athlete grid
at `/wrestlers/sami-zayn/` (EXISTS) and must NOT appear on this tab. If a cross-link is wanted, it is a
one-line "See also" pointer on the media hub to his wrestler profile, nothing more.

### D.3 Hero (component: `.poster`, media teal, monogram "CVV")
- **Chris Van Vliet** [HIGH]. Eyebrow "MEDIA & CREATORS", headline "Chris Van Vliet", one-line:
  "Emmy-winning host of the INSIGHT long-form interview show." [HIGH]
- CTA text link: "Media profile" -> `/media/chris-van-vliet/` (GAP, build). No fabricated quotes on
  the card; only the sourced descriptor.

### D.4 Proposed roster grid (all pages GAP; all MED/VERIFY except hero)
Render each as a `.tile` with `.chip--media` and, until each affiliation is confirmed, a
`.chip--verify` "VERIFY" pill. Links go live only when a page is built.

| Name | One-liner (from research §6) | Confidence | Link target (all GAP) |
|---|---|---|---|
| Chris Van Vliet | Emmy-winning INSIGHT interviewer (HERO) | HIGH | `/media/chris-van-vliet/` |
| Renee Paquette | Broadcaster/interviewer; host of "The Sessions" | MED / VERIFY | `/media/renee-paquette/` |
| Peter Rosenberg | Radio host and wrestling media personality | MED / VERIFY | `/media/peter-rosenberg/` |
| Ariel Helwani | Combat-sports journalist who covers wrestling | MED / VERIFY | `/media/ariel-helwani/` |
| Sean Ross Sapp | Fightful wrestling news reporter | MED / VERIFY | `/media/sean-ross-sapp/` |
| Denise Salcedo | Wrestling interviewer and YouTuber | MED / VERIFY | `/media/denise-salcedo/` |
| Dave Meltzer | Wrestling Observer; the star-rating source | MED / VERIFY | `/media/dave-meltzer/` |
| Wade Keller | PWTorch veteran journalist | MED / VERIFY | `/media/wade-keller/` |

Meltzer's tile should note he is the origin of the star-rating culture Wrestle Lore's match ratings
build on, linking to `/methodology/` (EXISTS) as a bonus internal link.

---

## E. Cross-cutting: mandatory "Keep going" block + JSON-LD

Every module-bearing hub (`/promotions/`, `/hall-of-fame/`, `/media/`, `/promotions/njpw/`) ends with
the mandatory **"Keep going" block** (4-6 contextual links, the #1 retention + internal-link lever
from inspiration §B2). Suggested per hub:
- Promotions hub: Matches, Events, Hall of Fame, Wrestlers by promotion.
- HOF hub: Ric Flair profile, Legends wrestler filter, Rankings, Two-Time Club members.
- NJPW hub: AJ Styles, Finn Balor, Shinsuke Nakamura, Jon Moxley, Promotions hub.
- Media hub: Methodology (ratings), Matches, Chris Van Vliet, Sami Zayn wrestler profile.

JSON-LD per module: `SportsOrganization` for each brand card, `ItemList` for HOF classes and the media
roster, `Person`/`ProfilePage` for the AJ Styles and Ric Flair heroes, `BreadcrumbList` on every hub,
plus the `.answer`/`FAQPage` blocks for GEO citation.

---

## F. Master clickable -> link-target table (every link in these modules)

`EXISTS` = live page under `/root/wwe/`. `GAP` = must be built before this link ships; render as
non-link/disabled until then so nothing 404s.

| # | Module | Clickable label | Link target | Status |
|---|---|---|---|---|
| 1 | A | WWE brand card (hub/monogram) | `/promotions/wwe/` | EXISTS |
| 2 | A | WWE "Top wrestlers" | `/wrestlers/` (WWE filter) | EXISTS |
| 3 | A | WWE "Events" | `/events/` | EXISTS |
| 4 | A | AEW brand card (hub) | `/promotions/aew/` | GAP |
| 5 | A | NJPW brand card (hub) | `/promotions/njpw/` | GAP |
| 6 | A | TNA brand card (hub) | `/promotions/tna/` | EXISTS |
| 7 | A | TNA "Top wrestlers" (AJ Styles, Samoa Joe, Christopher Daniels) | `/wrestlers/aj-styles/`, `/wrestlers/samoa-joe/`, `/wrestlers/christopher-daniels/` | EXISTS |
| 8 | A | NXT brand card (hub) | `/promotions/nxt/` | EXISTS |
| 9 | A | WCW brand card (hub) | `/promotions/wcw/` | EXISTS |
| 10 | A | ECW brand card (hub) | `/promotions/ecw/` | EXISTS |
| 11 | B | Most-decorated hero: Ric Flair | `/wrestlers/ric-flair/` | EXISTS |
| 12 | B | Two-Time Club: Shawn Michaels | `/wrestlers/shawn-michaels/` | EXISTS |
| 13 | B | Two-Time Club: Booker T | `/wrestlers/booker-t/` | EXISTS |
| 14 | B | Two-Time Club: Scott Hall (Razor Ramon) | `/wrestlers/razor-ramon/` | EXISTS |
| 15 | B | Two-Time Club: Kevin Nash | `/wrestlers/kevin-nash/` | EXISTS |
| 16 | B | Two-Time Club: Hulk Hogan | `/wrestlers/hulk-hogan/` | EXISTS |
| 17 | B | 2025 class: Triple H | `/wrestlers/triple-h/` | EXISTS |
| 18 | B | 2025 class: Lex Luger | `/wrestlers/lex-luger/` | EXISTS |
| 19 | B | 2024 class: Paul Heyman | `/wrestlers/paul-heyman/` | GAP |
| 20 | B | 2023 class: Rey Mysterio | `/wrestlers/rey-mysterio/` | EXISTS |
| 21 | B | 2023 class: The Great Muta | `/wrestlers/the-great-muta/` | GAP |
| 22 | B | 2022 class: The Undertaker | `/wrestlers/the-undertaker/` | EXISTS |
| 23 | B | 2022 class: Vader | `/wrestlers/vader/` | EXISTS |
| 24 | B | 2021 class: Kane | `/wrestlers/kane/` | EXISTS |
| 25 | B | 2021 class: Eric Bischoff | `/wrestlers/eric-bischoff/` | GAP |
| 26 | B | 2021 class: Rob Van Dam | `/wrestlers/rob-van-dam/` | GAP |
| 27 | B | HOF hub itself | `/hall-of-fame/` | GAP |
| 28 | C | AJ Styles hero -> profile | `/wrestlers/aj-styles/` | EXISTS |
| 29 | C | Arc node 1: TNA | `/promotions/tna/` | EXISTS |
| 30 | C | Arc node 2: NJPW | `/promotions/njpw/` | GAP |
| 31 | C | Arc node 3: WWE | `/promotions/wwe/` | EXISTS |
| 32 | C | Related: Shinsuke Nakamura | `/wrestlers/shinsuke-nakamura/` | EXISTS |
| 33 | C | Related: Finn Balor | `/wrestlers/finn-balor/` | EXISTS |
| 34 | C | Related: Jon Moxley | `/wrestlers/jon-moxley/` | EXISTS |
| 35 | C | Related: Kenny Omega | `/wrestlers/kenny-omega/` | GAP |
| 36 | C | Related: Will Ospreay | `/wrestlers/will-ospreay/` | GAP |
| 37 | D | Media hub itself | `/media/` | GAP |
| 38 | D | Hero: Chris Van Vliet | `/media/chris-van-vliet/` | GAP |
| 39 | D | Roster: Renee Paquette | `/media/renee-paquette/` | GAP |
| 40 | D | Roster: Peter Rosenberg | `/media/peter-rosenberg/` | GAP |
| 41 | D | Roster: Ariel Helwani | `/media/ariel-helwani/` | GAP |
| 42 | D | Roster: Sean Ross Sapp | `/media/sean-ross-sapp/` | GAP |
| 43 | D | Roster: Denise Salcedo | `/media/denise-salcedo/` | GAP |
| 44 | D | Roster: Dave Meltzer | `/media/dave-meltzer/` | GAP |
| 45 | D | Roster: Wade Keller | `/media/wade-keller/` | GAP |
| 46 | D | Meltzer tile -> ratings method | `/methodology/` | EXISTS |
| 47 | D | "See also" Sami Zayn (wrestler, not media) | `/wrestlers/sami-zayn/` | EXISTS |

### GAP pages to build so these modules ship without 404s
Hubs: `/promotions/aew/`, `/promotions/njpw/`, `/hall-of-fame/`, `/media/`.
Wrestler/inductee pages: paul-heyman, the-great-muta, eric-bischoff, rob-van-dam (and, for fuller HOF
coverage, michelle-mccool, molly-holly, barry-windham); kenny-omega, will-ospreay (NJPW ties).
Media pages: chris-van-vliet (priority, hero) plus any roster name promoted from proposed to live.

---

## G. Build order recommendation
1. Add CSS tokens + chip variants (§0). 2. Rebuild `/promotions/` with brand cards (Module A) using
existing hubs; ship AEW/NJPW cards in disabled state. 3. Build `/promotions/njpw/` + AJ Styles hero
(Modules C). 4. Build `/hall-of-fame/` (Module B, all headliner links live except GAP names).
5. Build `/media/` with Chris Van Vliet live and the rest as proposed VERIFY tiles (Module D).
6. Confirm every `VERIFY` fact and flip states before publish.
