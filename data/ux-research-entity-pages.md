# Entity & Content-Page UX Research — Profile, Match & Rivalry Pages

**Prepared:** 2026-07-25
**Scope:** UX for MAT's *content/detail* pages — the wrestler **profile** (`.profile` / `.facts` / `.tale` of the tape), the **match-review** page (`.ratingbox` / `.tale` / `.rate` / `table.data`), and the **rivalry** page (`.related-links`, `.timeline`, head-to-head). Goal: maximize scannability, credibility, session depth, and time-on-page while staying crawlable/GEO-citable on the existing dark theme.
**Method:** Nielsen Norman Group, Baymard Institute, Smashing Magazine, plus teardown of leading entity/detail pages (Sherdog & Tapology fighter pages, IMDb title pages, Wikipedia infoboxes, Letterboxd film pages, ESPN player pages).

> How to read this: each section gives the **Principle**, the **Source**, and a concrete **Apply to MAT** note referencing the real templates/classes already in the codebase (`/root/wwe/wrestlers/*/index.html`, `/root/wwe/matches/*/index.html`, `/root/wwe/css/site.css`).

---

## 0. Executive summary — the 8 highest-impact upgrades

1. **Add a ratings-distribution bar + real review count** to `.ratingbox`. Right now the match page shows a single "4.5 MAT RATING" number; a bare average hides polarization and reads as thinner social proof than a distribution + count. This is the single biggest credibility lever. (Baymard, Smashing)
2. **Stack the three rating "voices" explicitly** — MAT editorial ★, community average, and the historical critic (Meltzer/Cagematch already in `table.data`) — labeled and visually distinct. Reference/aggregate parity is what Letterboxd/IMDb/Tapology do. (Smashing)
3. **Fix mobile data tables.** `table.data` has `min-width:480px` inside a horizontally-scrolling `.table-wrap` — on a phone the "tale of the tape" gets cut off with no scroll affordance. Add a visible scroll cue or switch key/value tables to a stacked no-scroll layout. (NN/G)
4. **Front-load headings and links with information-bearing first two words** so the F-pattern scan works; several `<h2>`s ("Career", "The Story") and card links are fine, but "Related" and generic anchors leak scan value. (NN/G)
5. **Turn `.tale` into a true head-to-head** on rivalry/match pages — parallel stat rows (titles, signature win, era, MAT score) between the two names, not just Winner/Defeated chips. (NN/G comparison tables)
6. **Persist and grow the `.related-links` block into a segmented "keep exploring" rail** (Rivalries / Same era / Same promotion / Watch next) — related-entity depth is the primary time-on-page and session-depth driver for reference sites. (NN/G, internal-linking research)
7. **Make the video façade earn the fold.** The `.facade` click-to-YouTube pattern is good for performance; add a duration/"official upload" cue and keep it top-left of the content column where the F-scan lands. (NN/G, dark-theme legibility)
8. **Protect density on the dark theme** — the `#0a0b0d` base with `--c-bg-elev-1/2` tiers is correct; enforce elevation-by-surface (not shadow), desaturated gold/red accents, and generous line-height on long prose so the profile bios stay readable. (Smashing, Toptal)

---

## 1. Profile / detail-page layout & hierarchy (the "tale of the tape" fold)

**Principle.** The best entity pages resolve the user's question *above the fold* with a fixed, predictable anatomy: **identity block** (name, photo, one-line "who is this"), **at-a-glance facts** (the infobox / tale of the tape), and **primary metric** (rating/record). Wikipedia's right-rail infobox, IMDb's title header (poster + rating + metadata row), Sherdog/Tapology fighter headers (photo + record + physical stats grid), and ESPN player headers all put the scannable key-value facts adjacent to the identity, before any long-form prose. Users who arrive from search have a specific question ("real name?", "who won?", "how long was the reign?") and abandon if the fold doesn't answer it. Front-load the answer; most users don't scroll far.

**Source.** NN/G, *F-Shaped Pattern* & *Writing for the Web / inverted pyramid* (front-load the most important points in the first two paragraphs); Baymard product-page anatomy; above-the-fold engagement research ([omniconvert](https://www.omniconvert.com/blog/above-the-fold-design/), [theedigital](https://www.theedigital.com/blog/fold-still-matters)).

**Apply to MAT.**
- The wrestler `.profile` grid (`280px 1fr` at ≥720px) already nails the identity-left / facts-right anatomy, and the `.answer` block ("Roman Reigns … is the 'Tribal Chief' whose record 1,316-day reign…") is a textbook inverted-pyramid lead — **keep it, it's a strength and doubles as the GEO/answer-engine snippet.**
- `.facts` (2-col dashed-underline key/value grid) is the wrestler infobox. **Standardize the field order across every profile** (Real name → From → Debut → Promotions → Height/Weight → Signature/Finishers → Titles count) so returning users learn where to look — consistency is what makes an infobox scannable. Add **Height/Weight** (currently missing on Reigns) since physical stats are the literal "tale of the tape" fans expect from fighter pages.
- On the **match page**, the fold splits prose-left / facts-right (`.grid-2`). The right `aside` stacks `.ratingbox` → `.tale` → `table.data` (tale of the tape) → `.rate`. That is the correct priority order (verdict → who → details → your input). **Move nothing; deepen the `.ratingbox` (see §3).**
- Add a compact **`.facts`-style at-a-glance strip to rivalry pages** too (Span, # of matches, Peak PPV, Blow-off, MAT era) — rivalry pages currently jump from `.answer` straight to `.timeline` with no infobox.

---

## 2. Scannability — headings, chunking, tables, the F-pattern

**Principle.** Unformatted prose forces the efficiency-driven **F-pattern**: a strong top scan, a weaker second scan, then a vertical run down the left edge — most words go unread. Combat it by (a) front-loading headings and links with the **information-bearing first two words** ("if users see only the first 2 words, they should still get the gist"), (b) chunking into short sections with descriptive `<h2>`/`<h3>`, (c) bolding key phrases, (d) using bullets and key/value tables instead of paragraphs for facts, and (e) grouping related content with borders/background. Reduce word count; every removed sentence lowers scanning burden.

**Source.** NN/G, *F-Shaped Pattern for Reading Web Content* ([nngroup](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/)); *How People Read Online* ([W&M Swem](https://guides.libraries.wm.edu/writing-for-web/how-we-read-online)).

**Apply to MAT.**
- Headings are mostly good ("Career", "Signature Matches", "Rivalries", "The Story"). **Rename generic ones:** the final `<h2>Related</h2>` → "Explore next" or "More on The Bloodline"; "FAQ" is fine (users hunt for it). Lead each `<h2>` with the payload word.
- **Kill generic link text.** The `.related-links` anchors are already descriptive ("The Bloodline saga", "Cody Rhodes (WrestleMania 39 & 40)") — good. But card links like "vs Cody Rhodes — WrestleMania 40" are strong; keep that pattern everywhere and avoid bare "Browse the match archive"/"more".
- The `.answer` block (gold left-border, tinted background, bold gold lead sentence) is exactly the "group + emphasize" technique — it's your F-pattern anchor. **Ensure every profile, match, and rivalry page opens with one.**
- **Chunk long bios.** Reigns' Career section is two dense paragraphs; that's acceptable, but for longer profiles break into `<h3>` sub-beats ("The Shield", "The Tribal Chief era", "The Cody blow-off") so the left-edge vertical scan hits meaningful labels.
- Keep the `.faq` `<details>` blocks — collapsible Q&A is both a scannability aid and a FAQPage-schema/GEO asset (already implemented well).

---

## 3. Ratings & reviews UX (aggregate vs editorial vs community)

**Principle.** A single average number is the weakest form of rating UX. Best practice pairs **decimal average + review count + a clickable distribution bar chart**, because a "4.5 from 242 ratings" masks whether scores are consistently good or polarized (1★/5★). Baymard: show a *graphical* breakdown, keep it expanded by default, make bars act as filters (radio-style, mutually exclusive), and *hide* the distribution only when there are ≤5 reviews. Volume reassures more than a perfect score — users prefer 4.5 from 12 ratings over 5.0 from 2. Distinguish **editorial** (a named critic verdict) from **aggregate/community** (crowd) — leading media/entity sites show both side by side (IMDb rating vs Metascore; Letterboxd average + histogram; Tapology community pick % + tale-of-the-tape). For **input**, use a large, reversed-order star radio set with clear hover/checked states and a low-friction save.

**Source.** Baymard, *Ratings Distribution Summary — 5 requirements* ([baymard](https://baymard.com/blog/user-ratings-distribution-summary)); Smashing, *Product Reviews & Ratings UX* ([smashingmagazine](https://www.smashingmagazine.com/2023/01/product-reviews-ratings-ux/)); Smart Interface Design Patterns ([smart-interface-design-patterns](https://smart-interface-design-patterns.com/articles/reviews-and-ratings-ux/)).

**Apply to MAT.**
- **Upgrade `.ratingbox`.** Today: `.ratingbox__big` = "4.5 / MAT RATING" + a static `.rating` stars row + a one-line editorial caption. Add, directly beneath:
  - **Community average + count**: e.g. "Fans: 4.6 ★ · 7,840 ratings" (you already carry `aggregateRating ratingCount:7840, reviewCount:402` in the Review JSON-LD — surface it visibly, not only in schema).
  - **A 5→1 distribution bar chart** using existing tokens (`--c-gold` fill on `--c-bg-elev-2` track). Make each bar a filter link to that star's reviews. Expand by default; suppress when reviewCount ≤ 5.
- **Separate the three voices clearly:** (1) **MAT editorial** = the big number + prose verdict (this is your differentiator — a named, opinionated review, like a Meltzer/critic); (2) **Community** = average + distribution; (3) **Historical critics** = the Meltzer ★★★★½ and Cagematch ~8.8 rows already in `table.data`. Label them so users don't conflate MAT's score with the crowd's. This "editorial + aggregate + reference" triad is exactly how the strongest entity pages earn trust.
- **The `.rate` input is well built** (reversed radio set, gold hover/checked, focus-visible outline, accessible labels/legend). Two fixes: (a) it's gated behind "Join free to save your rating" — allow an *optimistic* click that shows the star fill immediately, then prompt to save (reduces input friction, lifts participation); (b) after rating, show "You rated 4★ · community 4.6★" to close the loop and reinforce contribution.
- On **wrestler profiles**, the signature-match cards use `.rating{--rating:x}` stars — good at-a-glance quality signal. Consider a small "MAT avg across N rated matches" stat in `.facts` to give each wrestler an aggregate quality fingerprint (a Letterboxd-style "average rating" for their body of work).

---

## 4. Data-table UX — desktop & mobile

**Principle.** Build the desktop table first, then adapt. Desktop: left-aligned text, right/decimal-aligned numbers, row hover, sticky header on long tables, zebra or divider lines, sortable columns for multi-row data. Mobile is where tables break: NN/G says keep true *comparison* tables tabular (users need to compare across columns) with a **pinned first column (row headers)** and a **visible horizontal-scroll cue** (arrows/cut-off edge, not dots) — but for simple **key/value** tables, collapse to a stacked list so nothing is clipped and no scroll is needed. Never force device rotation. Pre-filter or let users choose columns when data is wide.

**Source.** NN/G, *Mobile Tables: Comparisons and Other Data Tables* ([nngroup](https://www.nngroup.com/articles/mobile-tables/)); *Fit Big Tables on Small Screens*.

**Apply to MAT.**
- **Current risk:** `table.data{min-width:480px}` inside `.table-wrap{overflow-x:auto}`. The "Championships" and "tale of the tape" tables are **key/value (2-col) tables**, not comparisons — on a ~360px phone they force horizontal scroll for no reason and the right column ("Record 1,316-day reign") can be clipped with no visible affordance.
  - **Fix A (recommended for key/value tables):** at `max-width:520px`, drop `min-width` and render each `<tr>` as a stacked block — `th` label on its own line (uppercase dim, you already style it), `td` value below. Zero scroll, zero clipping. Use a `.data--kv` modifier so you don't affect true comparison tables.
  - **Fix B (for genuine comparison/head-to-head tables — see §6):** keep tabular, **pin the first column** (`position:sticky; left:0`) and add a visible right-edge fade + "→ scroll" cue so users know more columns exist.
- **Desktop polish:** `table.data` already has hover (`tr:hover`), gold caption, uppercase condensed `thead`, and link styling — solid. Add **right-alignment for numeric columns** (ratings, days, years) and make **rankings/championship-history tables sortable** (they're the ones with many rows where sort matters; the tale-of-the-tape does not need sort).
- **Captions are present** (`<caption>The tale of the tape</caption>`) — keep them; they aid both scanning and screen readers.

---

## 5. Cross-linking & "related entities" — the session-depth engine

**Principle.** For a reference/database site, **related-entity links are the primary driver of pages/session and time-on-site.** IMDb ("More like this", cast → filmographies), Letterboxd (related films, member reviews, lists), Wikipedia (dense inline + "See also"), and Sherdog (fight history rows each linking to the opponent) all keep users hopping between entities. Best practice: contextual in-body links (highest engagement), plus a curated end-of-page module that is **segmented and labeled** (not one undifferentiated blob), with descriptive anchors, and ideally a "watch/read next" hook. Every entity should link to its neighbors along multiple axes (opponent, era, promotion, stable, rivalry).

**Source.** NN/G on links carrying information scent; internal-linking + engagement guidance ([thegray.company](https://thegray.company/blog/internal-linking), [siteimprove](https://www.siteimprove.com/blog/internal-linking-strategy-for-seo/)).

**Apply to MAT.**
- The `.related-links` block (auto-fit card grid, gold hover) is the right component and appears on both profiles and match pages — **strong foundation.** Upgrades:
  - **Segment it.** Instead of one "Related" grid of 7 mixed links, split into labeled rows: **"Rivalries"**, **"Same era"**, **"Same promotion / stable"**, **"Watch next (rated matches)"**. Segmented related modules get more clicks than a flat list because each answers a different intent.
  - **Reciprocate links.** Reigns → Cody Rhodes must be matched by Cody → Reigns; each match page links both competitors' profiles (already done on Rock vs Austin — good) and each profile links its signature matches (also done). Audit that every edge is bidirectional.
  - **Inline links are your best asset** — the Reigns bio already links Shield/Bloodline/Cody/Rock/Rollins/Moxley inline. Keep prose link density high (Wikipedia model); inline links out-convert footer modules for depth.
  - **`.rel` relationship cards** (family/Shield-brother) in the aside are a great differentiator — the "relationship map" cross-link (`/relationships/`) is a session-depth magnet unique to wrestling. Surface a mini version on every profile.
  - Add a **"Next in this rivalry / next match on this card"** link at the bottom of match pages (sequential navigation) — turns single-match visits into card binges.

---

## 6. Comparison / head-to-head UX

**Principle.** Comparison is a distinct pattern: put the two entities in **parallel columns with aligned attribute rows**, so the eye compares *down* each attribute. Tale-of-the-tape (boxing/MMA/UFC) is the canonical form — name + photo at top of each column, then Height, Reach, Record, etc. row-by-row, with the winner/edge highlighted per row. Keep it tabular even on mobile (comparison is the one case where you don't collapse), with the attribute labels pinned. Highlight the differentiator, not everything.

**Source.** NN/G *Mobile Tables* (comparison tables stay tabular; pin labels); UFC tale-of-the-tape convention ([theplayoffs](https://theplayoffs.news/en/ufc-316-vicente-luque-vs-kevin-holland-head-to-head-comparison-tale-of-the-tape/)).

**Apply to MAT.**
- The match `.tale` today is `1fr auto 1fr` = Name/Winner-chip · **VS** · Name/Loss-chip. That's a *result* banner, not a comparison. **Extend it into a true tale of the tape:** below the VS row, add aligned attribute rows spanning both columns — e.g. **World titles**, **MAT avg match rating**, **Signature win**, **Era/peak**, **Height/Weight** — with a subtle per-row "edge" highlight (the `--c-win` green you already have). Keep the dramatic red "VS" divider (`.tale .vs` in `--c-red`) — it's on-brand.
- Give **rivalry pages a head-to-head scoreboard**: matches won H2H, PPV buys/era, MAT-rated classics count, blow-off result. This is the rivalry page's "tale of the tape" and a highly shareable, screenshot-friendly unit.
- Consider a lightweight **"Compare any two wrestlers"** tool feeding the same parallel-column component — a proven engagement/time-on-page feature on sports/fighter databases (Tapology, ESPN).
- Mobile: this comparison table is the case to **keep tabular** (don't stack) — pin the center attribute labels, let the two value columns sit either side.

---

## 7. Media / video placement

**Principle.** For a page whose hero content is a match, video is the emotional payload — but performance and layout discipline matter. Place the primary media **top-left of the main content column** where the F-scan lands, above the long-form story. Use a lightweight **click-to-play façade** (poster + play button) rather than an eager iframe to protect LCP, and give it a clear affordance (play glyph, duration, source label) so users trust the click. Don't let autoplaying/heavy embeds push the key facts below the fold.

**Source.** NN/G above-the-fold + interaction-cost; dark-theme legibility for overlay controls ([smashingmagazine](https://www.smashingmagazine.com/2025/04/inclusive-dark-mode-designing-accessible-dark-themes/)).

**Apply to MAT.**
- The match page's `.hero__card > .embed > .facade` pattern is **excellent** — `aspect-ratio:16/9`, `preconnect` to `i.ytimg.com` / `youtube-nocookie.com`, black poster with `.facade__ph`/`.facade__btn`/`.facade__label`, and it opens the official WWE/YouTube search. Keep this; it's performant and rights-safe.
- **Enhancements:** (a) add a **duration/date chip** and a "Full match · official upload" label so the click promises something specific (raises play rate); (b) ensure the play button meets the 3:1 non-text contrast on `#000` (the red `--c-red-bright` hover is fine; confirm the resting state); (c) once verified embed IDs exist (the note says YouTube & Bilibili IDs "drop straight into this player"), swap the search-open for a true in-place `<iframe>` on click so users never leave the page — that directly protects time-on-page.
- On **wrestler profiles**, the `.profile__photo` is a text initials placeholder (`REIGNS`). When real imagery lands, keep it in the 280px identity column; don't let a large hero image shove `.facts` below the fold on mobile (stack photo → answer → facts, which the current single-column collapse already does).

---

## 8. Content density vs whitespace on the dark theme

**Principle.** Dark themes reduce eye strain and suit media/entertainment brands but demand discipline: **avoid pure black** (#000) for large surfaces — use very dark gray; **avoid pure white** body text — use off-white to cut halation; convey **elevation with progressively lighter surfaces**, not heavy shadows (shadows barely read on dark); **desaturate accent colors** so they don't vibrate; keep **4.5:1** text contrast (3:1 for large/non-text UI); and give long-form prose **generous line-height and measure** because dense light text on dark fatigues faster. Density should come from clear grouping and spacing tiers, not from cramming.

**Source.** Smashing, *Inclusive Dark Mode* ([smashingmagazine](https://www.smashingmagazine.com/2025/04/inclusive-dark-mode-designing-accessible-dark-themes/)); Toptal, *Principles of Dark UI* ([toptal](https://www.toptal.com/designers/ui/dark-ui-design)); Onething ([onething.design](https://www.onething.design/post/best-practices-for-dark-mode-ui-design)).

**Apply to MAT.**
- The token system already follows best practice: base `--c-bg:#0a0b0d` (near-black, not pure), a **3-tier elevation scale** `--c-bg-elev-1:#121418 / -2:#1a1d23 / -3:#23272f` (elevation-by-surface — correct), off-white text `--c-text:#e8eaed` with muted/dim tiers, and **desaturated** gold/red (`--c-gold:#d4af37`, `--c-red:#e11d2a`) with `-tint` low-alpha fills for `.answer`/chips. `color-scheme:dark` is declared. **This is a well-built dark system — protect it.**
- **Verify contrast** of `--c-text-dim:#6b727d` on `--c-bg` for anything load-bearing — dim gray on near-black can dip under 4.5:1; keep it for decorative/label text only (it's used for `.facts b` uppercase labels and captions, which is acceptable, but not for body copy).
- **Body prose:** `--lh-body:1.6` is good; ensure the long bio paragraphs use it and cap measure (~`--wrap-narrow:760px`, already used on FAQ) so lines don't run too wide against the dark field.
- **Density control:** the spacing scale (`--sp-1…8`) plus card borders (`--c-line`) do the grouping work shadows can't. Lean on the elevation tiers to separate `.ratingbox`/`.tale`/`table.data`/`.notice` in the aside stack — each already sits on `--c-bg-elev-1` with a border, which reads cleanly. Avoid adding drop shadows for separation.
- The **film-grain overlay** (`.grain`, opacity .05, overlay blend) and gold/red glows are on-brand atmosphere; keep opacity low so they never cost text contrast, and they're already correctly behind `pointer-events:none`.

---

## 9. Engagement & time-on-page patterns

**Principle.** Time-on-page and session depth on content sites are driven by: (1) answering the entry question instantly (reduces bounce), then (2) offering an obvious *next* action — related entities, "watch next", sequential navigation; (3) interactive units (rate, compare, expand FAQ, filter reviews) that invite a click and a return; (4) chunked, scannable long-form that rewards scrolling; and (5) social-proof/contribution loops (rate → see how your rating compares) that create reasons to log in and come back.

**Source.** NN/G interaction-cost & scannability; above-the-fold engagement ([nudgenow](https://www.nudgenow.com/blogs/understanding-above-the-fold-best-practices)); reviews-participation loops (Smashing).

**Apply to MAT.**
- **Interactive hooks already present:** `.rate` star input, `<details>` FAQ, video façade, `.related-links`. **Add:** the ratings distribution filter (§3), the compare tool (§6), and sequential "next match/next in rivalry" links (§5). Each is a fresh reason to stay or click deeper.
- **Contribution loop:** let the `.rate` click render instantly + show the community delta, then invite the free join to *save* it — this converts passive readers into logged-in returners without gating the content (protects both engagement and GEO crawlability).
- **Don't gate content behind JS or a wall.** The pages are static HTML with content in the DOM (schema, prose, tables all server-rendered) — this is what keeps them crawlable *and* fast (low LCP → lower bounce). Preserve that; keep any rating/compare interactivity progressive-enhancement only (the site already gates reveal animations behind `.js` so content shows without JS — apply the same principle to new features).
- **Every page should end with momentum**, not a dead stop: the segmented `.related-links` + a single membership CTA is the right closer. Avoid multiple competing CTAs at the bottom.

---

## 10. Component-level checklist (map to existing classes)

| Component | Class | Status | Highest-impact change |
|---|---|---|---|
| Identity + lead answer | `.profile`, `.answer` | Strong | Standardize `.facts` field order; add Height/Weight |
| Infobox | `.facts` | Good | Consistent fields; consider "MAT avg rating" stat |
| Rating verdict | `.ratingbox` | **Thin** | Add community avg + review count + distribution bars |
| Editorial vs aggregate vs critic | `.ratingbox` + `table.data` rows | Present but unlabeled | Label the 3 voices distinctly |
| Head-to-head | `.tale` | Result banner only | Add aligned attribute rows (true tale of the tape) |
| Data tables | `table.data` / `.table-wrap` | Desktop good, **mobile clips** | Stack key/value on mobile; pin col + scroll cue on comparisons |
| Rating input | `.rate` | Well built | Optimistic click; show community delta; loosen gate |
| Related entities | `.related-links` | Good foundation | Segment + label; reciprocate; add "watch/next" |
| Relationship cards | `.rel` | Differentiator | Surface mini map on every profile |
| Video | `.hero__card`/`.embed`/`.facade` | Excellent | Duration/label chip; in-place iframe on verified IDs |
| FAQ | `.faq` `<details>` | Excellent | Keep (scannability + GEO) |
| Dark theme tokens | `:root` vars | Well built | Guard dim-text contrast; elevation not shadow |

---

## Sources

- NN/G — [F-Shaped Pattern for Reading Web Content](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/)
- NN/G — [Mobile Tables: Comparisons and Other Data Tables](https://www.nngroup.com/articles/mobile-tables/)
- NN/G — [Mobile & Tablet Usability reports](https://www.nngroup.com/reports/topic/mobile-and-tablet-design/)
- Baymard — [Ratings Distribution Summary: 5 Requirements](https://baymard.com/blog/user-ratings-distribution-summary)
- Baymard — [UX Best Practice Guidelines](https://baymard.com/product/ux-best-practice-guidelines)
- Smashing Magazine — [Product Reviews & Ratings UX](https://www.smashingmagazine.com/2023/01/product-reviews-ratings-ux/)
- Smashing Magazine — [Inclusive Dark Mode: Designing Accessible Dark Themes](https://www.smashingmagazine.com/2025/04/inclusive-dark-mode-designing-accessible-dark-themes/)
- Smart Interface Design Patterns — [Reviews & Ratings UX](https://smart-interface-design-patterns.com/articles/reviews-and-ratings-ux/)
- Toptal — [Principles of Dark UI Design](https://www.toptal.com/designers/ui/dark-ui-design)
- Onething — [Best Practices for Dark Mode UI Design](https://www.onething.design/post/best-practices-for-dark-mode-ui-design)
- The Gray Company — [Internal Linking for SEO, UX & Conversion](https://thegray.company/blog/internal-linking)
- Siteimprove — [Internal Linking Strategy](https://www.siteimprove.com/blog/internal-linking-strategy-for-seo/)
- W&M Swem Library — [How People Read Online](https://guides.libraries.wm.edu/writing-for-web/how-we-read-online)
- Omniconvert — [Above the Fold in Web Design](https://www.omniconvert.com/blog/above-the-fold-design/)
- thePlayoffs — [UFC Tale of the Tape / Head-to-Head example](https://theplayoffs.news/en/ufc-316-vicente-luque-vs-kevin-holland-head-to-head-comparison-tale-of-the-tape/)
- Reference entity pages studied: Sherdog & Tapology fighter pages, IMDb title pages, Wikipedia infoboxes, Letterboxd film pages, ESPN player pages.
