# Wrestle Lore — POLISH & HARDEN BACKLOG

Head-of-design + engineering-triage synthesis of all seven critiques in
`docs/design/wrestle-lore/critique/` (ux-ia-usability, visual-design-polish, a11y-inclusive,
perf-cwv, mobile-responsive, engagement-retention, redteam-antigeneric).

One prioritized list. Every row scored **IMPACT x EFFORT on a static, no-build, crawlable site**,
grouped QUICK-WINS / HIGH-VALUE / LATER, with the cited file, the concrete change, and whether it
needs a backend. Scoring key below. Nothing here needs a server you host except three explicitly
flagged items (community rating aggregation, ESP double-opt-in, all optional Tier-2 work).

**Ground-truth re-verified against the repo (2026-07-26), and it is worse than the critiques assumed:**
- **107** wrestler directories on disk. Homepage stat says **"41+"** (`index.html:179`), roster index
  says **41** (`wrestlers/index.html:207`), search index holds ~89, brief says 89. Four different
  numbers for one thing.
- **98** wrestler pages use `class="athlete-hero"`; `site.css` has **0** matching rules. The flagship
  page type renders as unstyled browser-default HTML.
- **198** total pages. **93** ship no design fonts at all. **0** pages preload anything. No `404.html`.
- `js/search-index.js` contains **0** entries for `/hall-of-fame/ /current/ /legends/ /women/ /media/`.
- Fabricated: `AggregateRating` (9,640 ratings) on 30 match pages; "12,840 fans" waitlist
  (`index.html:270`), on a pre-launch site with no users.

### Scoring key
- **Impact**: H = moves perceived quality / searchability / retention hard; M = noticeable; L = polish.
- **Effort** (static site): S = < half a day / CSS-or-markup; M = build-script or JS module + re-stamp;
  L = asset sourcing or new subsystem.
- **Score** = Impact/Effort priority (P0 do-first … P3 later).
- **Backend?**: No = ships static/no-build/crawlable. "Flag" = optional Tier-2 needs a datastore/ESP;
  the shipped version is static.

---

## QUICK-WINS (high or medium impact, S effort — ship this week)

| ID | Item | Cited file(s) | Concrete change | Impact | Effort | Score | Backend? |
|----|------|---------------|-----------------|--------|--------|-------|----------|
| Q1 | Delete fabricated `AggregateRating` on all 30 match pages | `matches/*/index.html` (redteam #2) | Remove the invented 9,640-rating / 4.9 block; replace with an honest dual score (Meltzer star rating + Cagematch, both cited) per Rotten Tomatoes critic/audience split | H | S | P0 | No |
| Q2 | Kill fake "12,840 fans" + wrong "41+" stat | `index.html:270`, `index.html:179` | Remove the invented waitlist count (honest copy, no number); wire stat-bar counts to build-generated real totals (107 wrestlers, 30 matches…) | H | S | P0 | No |
| Q3 | Ship `/404.html` | none (missing) (ux C4) | Full shell + Cmd-K + search prompt + rails to top hubs and 5-star matches; add host 404 config (`_redirects`/Netlify/CF) | H | S | P0 | No (host cfg) |
| Q4 | Zero-result empty state + clear-filters + `aria-live` | `js/main.js:71-85` (ux C3, a11y A10) | On `shown===0` inject "No wrestlers match X in WCW" + reset button; announce count via `aria-live="polite"` | M | S | P1 | No |
| Q5 | `aria-current` active-nav state | `css/site.css:112`, all shells (ux A3) | Per-section body/`data-section` attr in the stamp + one CSS rule for the active tab | M | S | P1 | No |
| Q6 | Style `.fbtn` + move filter bar out of grid + `aria-pressed` | `wrestlers/index.html:196`, `matches/index.html:189` (ux C5, a11y A10) | `.fbtn` has 0 CSS rules; alias to `.rt-filters` pattern incl. active state; lift bar to a sibling toolbar; add `aria-pressed` | M | S | P1 | No |
| Q7 | Namespace the `data-filter` collision | `js/main.js:64`, `js/enhance.js` (ux D3) | Rename search input to `data-list-filter`, record buttons to `data-record-cat` so two scripts stop double-binding one attribute | M | S | P1 | No |
| Q8 | Contrast fixes (two hard AA fails) | `css/site.css:562` `.res-l`, `:612` `--c-text-dim` (a11y A5) | Loss badge white-on-#e05263 = 3.8:1 → dark-on-red or deepen to #c23a4a; raise dim token to ~#9199a6 or forbid on elev-2/3 | M | S | P1 | No |
| Q9 | Input focus ring (WCAG 2.4.11) | `css/site.css:332` (a11y A6) | Replace 1px border recolor with `:focus-visible{outline:2px solid var(--c-focus);outline-offset:2px}` | M | S | P1 | No |
| Q10 | `forced-colors` media block | `css/site.css` (none exists) (a11y A7, visual H4) | Add `@media (forced-colors:active)` so gradient-clipped headlines (`.hero-bb__title .accent`, `.ev-hero h1`, `.rec-stat .n`) don't render invisible | M | S | P1 | No |
| Q11 | 16px mobile inputs (stop iOS auto-zoom on the funnel field) | `css/site.css:331` (mobile M6) | `@media(max-width:640px){.input,select,textarea{font-size:16px}}` — waitlist email currently ~15px | M | S | P1 | No |
| Q12 | Hero `svh` instead of `vh` | `css/site.css:418` (mobile M7) | `min-height:clamp(480px,80svh,940px)` so the hero stops jumping/over-tall with mobile toolbars and the marquee peeks above the fold | M | S | P1 | No |
| Q13 | Touch targets ≥44px at coarse pointer | `css/site.css:542,554,873,894` (mobile M5, a11y A11) | `@media(pointer:coarse)` min-height on `.subnav-page a`, `.rt-filters button`, `.rf-btn`, `.nav__search`, `.cmdk__row`, footer links | M | S | P2 | No |
| Q14 | Waitlist success as live status + focus move | `index.html:256`, `js/main.js:120` (a11y A8) | `role="status" aria-live="polite"` on `.form-success` + move focus to it (the exact conversion moment is currently silent to AT) | M | S | P1 | No |
| Q15 | Home hero real facade + honest label | `index.html:144-149` (perf F12, ux D1, a11y A15, redteam #3) | Swap inline `onclick` YouTube-search for the real `.facade[data-provider]` inline-play used elsewhere; stop claiming "verified embeds" while opening a search | M | S | P1 | No |
| Q16 | `heroDrift` + header blur perf | `css/site.css:420-427,97` (perf F6, F7) | Animate `transform` not `background-position` (or drop); layer-promote sticky header, blur 10→6px, move `is-stuck` shadow off the blurred layer, add `@supports` solid fallback | M | S | P1 | No |
| Q17 | Marquee read twice by AT | `index.html:170-188` (a11y A9) | `aria-hidden="true"` on the duplicated ticker set (the linked 5-star rail below is the real one) | L | S | P2 | No |
| Q18 | Events panel instance-vs-series labels + empty `&nbsp;` headings | `index.html:58,76-93` (ux A6, a11y A14) | Two titled columns ("Latest shows" / "Series & specials"); fill or `sr-only` the empty `<h3>&nbsp;</h3>` headings | M | S | P2 | No |
| Q19 | Drop `optimizeLegibility` + 500 font weights | `css/site.css:69`, font request (perf F10, F12) | Remove global `text-rendering:optimizeLegibility`; drop Oswald/Inter 500 (unused) from the self-host set | L | S | P2 | No |
| Q20 | Rating "out of 5" for AT + new-tab cues | `index.html:152,202`, `moments/...:132` (a11y A13, A15) | `sr-only` "out of 5 stars" on ratings; "(opens in new tab)" on `target=_blank` links | L | S | P2 | No |
| Q21 | Tile press + wire-or-delete spotlight + stagger + hover:none | `css/site.css:394-398,477`, `js/main.js` (visual M2) | `.tile__spot` is dead CSS (no JS sets `--mx/--my`) — wire a 6-line pointermove or delete; add `:active` press; stagger reveal; `@media(hover:none)` resting state | M | S | P2 | No |
| Q22 | `.tale` / `.facts` reflow + full-width hero CTAs + cmdk height | `css/site.css:235,279,418`, `index.html:136` (mobile M8,M11,M12,M10) | `.tale`→1col ≤520px; `.facts`→1col ≤420px; hero `.btn` full-width ≤520px; `.cmdk__results max-height:min(52vh,50dvh)` | M | S | P2 | No |
| Q23 | Copy hygiene sweep (own copy standard) | card meta, `events/index.html:130` etc. (ux D2, engagement, redteam #3) | Remove em-dash separators, decorative arrows, banned cliche words; fix and document one meta grammar (date · place order) | M | S | P1 | No |

---

## HIGH-VALUE (high impact, M/L effort — the spine of the polish sprint)

| ID | Item | Cited file(s) | Concrete change | Impact | Effort | Score | Backend? |
|----|------|---------------|-----------------|--------|--------|-------|----------|
| **H1** | **Re-stamp all 107 wrestler profiles onto the canonical shell + real DS classes** | `wrestlers/kane/index.html` + 97 more; `css/site.css` (ALL SEVEN critiques) | The #1 fix. Re-point the profile build script to the vocabulary `site.css` actually styles (`.profile`,`.facts`,`.champ-panel`,`table.record`+`.rt-filters`,`.timeline`,`.faq`,`.tabs`). One change fixes: unstyled flagship (98 pages), missing breadcrumb, dropped skip link, duplicate banner, dead record filter, no fonts, un-deferred `main.js`, missing `enhance.js` (invisible method bars), 6-col table horizontal page-overflow at 360px, `<th>` without `scope`, color-only win/loss sparkline | H | M | **P0** | No |
| **H2** | **Build-time class-coverage guard + one head/footer/nav partial + drift check** | `build/`, all shells (ux A5, visual C1, perf F4) | ~30-line script greps every emitted `class` token against selectors in `site.css` and fails the build on any 0-match class (would have caught H1 before 98 pages shipped). Collapse the hand-copied `<head>`/nav/footer to one stamped partial + a hash/diff check so nav can never drift again | H | M | **P0** | No |
| **H3** | **Regenerate `search-index.js` + roster grid + all counts from the filesystem** | `js/search-index.js`, `wrestlers/index.html:207`, `index.html:179` (ux C1,C2; engagement F10) | Build step walks `/wrestlers/ /matches/ /events/ /hall-of-fame/ /current/ /legends/ /women/ /media/` and emits the search array (with kinds for new hubs), the full 107-card roster grid, and every stat count. Kills stale search, the frozen-41 roster, and the number contradictions in one generator | H | M | **P0** | No |
| H4 | Surface Phase 1 hubs in nav; kill mislabeled "More" | `index.html:51-106` (ux A1,A2) | HOF/Legends/Current/Women exist on disk but link from no primary nav. Route them into the Wrestlers panel (By Status / By Division), Media into a renamed final tab; "More" tab currently points to `/rankings/` — give it an honest scented label ("The Web"/"Connections") and real landing | H | M | P0 | No |
| H5 | Fat footer (stamped on all 198 pages) | `index.html:283` + every page (engagement F7) | Replace the 3-link footer (About · Methodology · Insider) with columns: Popular Wrestlers, Five-Star Matches, Event Series, Promotions, Hubs, plus newsletter field. Highest ROI-per-effort: one shell edit lands on every page as a crawl + rabbit-hole layer | H | M | P0 | No |
| H6 | Keep-going block + related rails + link every proper noun on entity templates | `wrestlers/kane/index.html` end; `moments/...:140`; `matches/...` (engagement F1,F8,F11; ux B2) | Flagship ends at a table then footer with zero forward links. Append the `07-addictive-browsing` stack: signature-match rail, rivals/allies rail, trophy case, Keep-going block, prev/next pager. Make every named event/faction/match a real `<a>`. Swap ad-hoc `.related-links` for the typed `.keepgoing`. Biggest lever on session depth + crawl edges | H | M | P0 | No |
| H7 | Self-host fonts + preload Anton + size-adjust fallbacks | `index.html:25-27`, `css/site.css:436` (perf F1,F2,F3) | Self-host 5-6 woff2; delete all Google Fonts `<link>`/`preconnect` (2 blocking third-party origins on 105 pages); preload only Anton; add `size-adjust`/`ascent-override` fallback `@font-face` for Anton + Oswald to zero the swap CLS. ~0.4-0.8s LCP win | H | M | P0 | No |
| H8 | ⌘K accessible combobox | `js/nav.js`, shell (a11y A1,A12; ux C6; mobile M2) | APG combobox contract: `role="combobox"` + `aria-controls`/`aria-activedescendant`/`aria-selected`, focus trap, focus-return to trigger, Escape from overlay not just input, `inert` background, `aria-live` result count. Seed empty state with recently-viewed + curated hubs; zero-result redirects instead of dead-ends | H | M | P1 | No |
| H9 | Mega-nav link + disclosure split | `index.html:52+`, `js/main.js:22-34` (a11y A2,A3; mobile M4; ux A4) | Fixes three bugs at once: desktop `aria-expanded` is hardcoded false and lies; mobile taps on hub labels `preventDefault` so `/wrestlers/` is unreachable; tablets (hover:none, 768-1024px) can't open panels at all. Keep label a real link, add a separate 44px chevron button that owns `aria-expanded`+`aria-controls`; add Escape-to-close; gate tap-toggle on `(hover:none)` | H | M | P1 | No |
| H10 | Finish the mobile nav drawer | `js/main.js:11-19` (mobile M3) | Half-built: no scroll-lock, no scrim, no tap-outside/Escape/close-on-link, no focus management (ironically ⌘K locks the body but the drawer doesn't). Add all five; reuse ⌘K's existing lock code | H | S | P1 | No |
| H11 | Persistent mobile search icon + ✕ close in ⌘K | `index.html:108`, `js/nav.js` (mobile M2) | Flagship search is 2 taps deep inside the collapsed drawer with no persistent icon, and once open has only keyboard-only dismiss (no ✕, keyboard covers the backdrop). Pull the trigger out of the drawer as an always-visible ≤900px icon; add a 44px ✕; `inputmode="search"` | H | S | P1 | No |
| H12 | Adopt `localStorage` functional-memory module | `js/main.js` (self-imposed "no storage") (engagement F4) | Lift the self-imposed no-storage rule (client-only, crawl-safe, no cookie banner for functional storage). One `js/memory.js`: recently-viewed, watchlist, seen-checkmarks, visit streak. Unlocks the rating loop and daily return; keep the crawlable `<a>` layer untouched underneath | H | M | P1 | No |
| H13 | Working rate-first loop | `matches/cm-punk-vs-cena-mitb-2011/index.html:209` (engagement F3) | `fieldset.rate` has no JS handler and is wall-gated. Tier 1 (static): stars respond, persist to localStorage, show "you rated / how you compare", client-side `/my-ratings/`; account prompt becomes "sync across devices". Tier 2 (aggregated community score) is the one true backend dep — flag, ship Tier 1 now | H | M | P1 | Flag (Tier 2) |
| H14 | Contextual email capture on every entity page | `index.html:250` only; deep pages have none (engagement F2) | Organic traffic lands on Kane/moments/matches, which have no field. Add one contextual capture module above the footer on every entity page, reusing `form[data-waitlist]` with a per-type `data-source`. Prod needs an ESP form endpoint (a form `action`, not a server you host) | H | M | P1 | Flag (ESP) |
| H15 | Spend the color system (promotion/category tokens) | `css/site.css:15-37`, `index.html` (visual H3; redteam #1) | Homepage is monochrome-gold; red wasted; `--c-wwe/--c-womens/--c-hof/--c-media` never appear. Set a hierarchy of meaning: gold = quality/rating only, red = live/CTA, promotion accent = provenance (chip + 2px tile top-border). Give women/HOF/media hubs their token identity. Verify `--c-njpw/--c-aew` hex (marked VERIFY) | H | M | P1 | No |
| H16 | Named reviewers + author pages + first-person voice; wire dead embed/filter code | match/profile bylines (redteam #3) | Replace faceless "Wrestle Lore Editorial" and interchangeable cliche headings ("Everything is connected", "The legends who built it") with named reviewers, author pages, opinionated first-person methodology (Defector/Meltzer authority, Letterboxd verdict line). Wire the already-built embed + record-filter code | H | M | P1 | No |
| H17 | On This Day + countdown to next PLE | `index.html` marquee (engagement F5) | Two date-driven static modules: build-generated `/data/onthisday.json` keyed MM-DD rendered against `new Date()`; countdown band to the next dated event. Fresh daily, share-bait, deep-page link farm, zero backend | H | M | P1 | No |
| H18 | Real / duotone portrait cards | `css/site.css:474-496` (visual M1) | A 107-card roster of single-faded-letter tiles is 107 near-identical rectangles. Ship duotone-treated silhouette PNGs (`mix-blend-mode` over the gradient) + bottom scrim; until assets land, constrain `--seed` to 6 curated non-muddy angles + monogram. Asset-sourcing effort, not an engineering blocker | H | L | P2 | No |

---

## LATER (medium/low impact, or larger effort for the payoff — after the sprint)

| ID | Item | Cited file(s) | Concrete change | Impact | Effort | Score | Backend? |
|----|------|---------------|-----------------|--------|--------|-------|----------|
| L1 | Vertical rhythm system (componentize inline spacing) | `index.html` throughout (visual H1) | Move scattered inline `style="margin/padding/font-size"` into component classes; add `.section--tight/--feature` rhythm variance + flow spacing. (Correct tokens + no components is a template tell) | M | M | P2 | No |
| L2 | Type discipline rule | `css/site.css:39-45,436` (visual H2) | One rule: Anton = hero + H2 + entity H1; Oswald = UI/labels/table headers; Inter = body only. Pull `--fs-600` down so H2/H3 separate on mobile; apply Anton negative tracking to all display headings | M | S | P2 | No |
| L3 | Sticky in-page `.subnav-page` on long profiles | `css/site.css:538` (unused) (ux B3) | Component is built and used nowhere; add anchor tabs (Overview · Titles · Timeline · Matches · FAQ) to profile + match + event templates | M | S | P2 | No |
| L4 | De-duplicate Matches vs Rankings vs "Top-Rated" | `index.html:70,103` (ux B4) | One model: Matches = full filterable archive; Rankings = curated ranked lists. State the difference once on each index; drop the duplicate Rankings link | M | S | P2 | No |
| L5 | ⌘K empty/zero states as browse launchpad | `js/nav.js:39,50` (engagement F6) | (Ships with H8/H12) empty = recently-viewed + curated hubs; zero = "try these" evergreen hubs, never a blank box | M | S | P2 | No |
| L6 | Prev/next pager within each collection | entity templates (engagement F8) | Build script emits neighbor links (alpha/chronological/by-rating) per page; two `<a>` at the top of the Keep-going block | M | S | P2 | No |
| L7 | True bento for "The Web" | `index.html:230`, `css/site.css:531` (visual M5) | The connection section is the flattest grid on the page. Build a real varied-cell bento (tall hero + medium + stat cells + wide CTA) — also the best portfolio screenshot | M | M | P2 | No |
| L8 | Elevation ladder + grain that reads | `css/site.css:52,388` (visual M3,M4) | Define elev-0..3 carried by surface tint + `--edge-light` top-highlight (not just shadow on near-black); one grain owner per stacking context, soft-light blend, ~.09-.12 opacity | M | S | P3 | No |
| L9 | `content-visibility:auto` on below-fold blocks | long pages (perf F8) | `content-visibility:auto;contain-intrinsic-size:auto 600px` on record/sig/media/bento/faq sections (not hero); reserve size to avoid CLS | M | S | P3 | No |
| L10 | Lazy-load `search-index.js` on first ⌘K | `index.html:291`, `js/nav.js` (perf F5) | Inject the ~3KB index on first palette-open instead of every page load | L | S | P3 | No |
| L11 | Hover link previews (desktop) | prose links (engagement F9) | Small card on hover of internal entity links from `/data/graph.json`; degrades to nothing on touch. Honors reduced-motion/fine-pointer gates | M | M | P3 | No |
| L12 | Auto-hide sub-nav/header on scroll (mobile) | `css/site.css:99,538`, `js/enhance.js:122` (mobile M9) | Two sticky layers eat ~16% of a phone screen; extend the existing scroll handler to hide-on-down / show-on-up | M | S | P3 | No |
| L13 | Vary section-header motif + motion timing | `index.html:198+`, `css/site.css:54,401` (visual L3,L4,L5) | Unify on the stronger `.sec-h` left-bar over the repeated `.rule-gold`; split micro (120-160ms) vs macro (500-700ms) durations; collapse mobile mega columns | L | S | P3 | No |
| L14 | Marquee swipe-default + facade region fallback | `css/site.css:464`, `moments/...:126` (mobile M13, ux D1) | Make the ticker a swipeable scroller on `(hover:none)`; add an inline "unavailable in your region" embed-error state instead of buried fine print | L | S | P3 | No |
| L15 | `nav__spacer` CSS-only + associate mega `<h3>` | `index.html:107` (a11y A14) | Make the layout spacer CSS-only so the nav `<ul>` holds only real items | L | S | P3 | No |

---

## TOP 10 changes that most raise perceived quality + searchability

1. **H1 — Re-stamp all 107 profiles onto the real design system.** The single most important page type
   currently renders as unstyled HTML on 98 pages. Every other quality claim is void until this ships.
   Cited by all seven critiques.
2. **H3 — Regenerate search index + roster grid + counts from the filesystem.** Makes the "most
   searchable site" claim true: new hubs + all 107 profiles become findable, and the number
   contradictions disappear.
3. **H2 — Build-time class-coverage guard + single stamped partial.** Prevents H1/H3/nav-drift from ever
   recurring; this is the engineering root cause fix, not a patch.
4. **H5 — Fat footer on all 198 pages.** Cheapest crawl-depth + internal-linking + rabbit-hole win;
   one edit, sitewide.
5. **H6 — Keep-going block + related rails + link every proper noun.** Turns dead-end profiles into a
   link graph — the biggest lever on both session depth and crawlable edges.
6. **H4 — Surface Phase 1 hubs in nav.** HOF/Legends/Current/Women are on disk but reachable by no human;
   findability is zero until they're in the nav.
7. **H7 — Self-host fonts + preload + size-adjust fallback.** The whole perceived-speed story rides on
   fonts; removes two blocking third-party origins and ~0.4-0.8s of LCP plus the hero swap-CLS.
8. **Q3 — 404 page.** On a crawlability-first site, every bad/renamed slug currently exits the site.
9. **H15 — Spend the color system tribally.** Promotion-color wayfinding is the visual edge over
   Cagematch and the fix for the generic monochrome-gold "luxury template" read.
10. **H8 + H11 — Accessible, mobile-reachable ⌘K.** The flagship feature is currently broken for
    keyboard/AT users and buried 2 taps deep with no dismiss on phones.

## The 5 "make it not look AI-generated" fixes

1. **Delete every fabricated number (Q1, Q2).** The `AggregateRating` (9,640 ratings / 4.9) on 30 match
   pages, "12,840 fans" waitlist, and "41+" vs the real 107 are the #1 AI/portfolio tell — invented,
   self-serving, internally inconsistent, and Google penalizes the markup.
2. **Give it a human (H16).** Replace faceless "Wrestle Lore Editorial" bylines and interchangeable
   cliche headings ("Everything is connected", "The legends who built it") with named reviewers, author
   pages, and opinionated first-person methodology.
3. **Copy hygiene (Q23).** Remove em-dash separators, decorative arrows, and banned cliche words per the
   site's own copy standard; enforce one documented meta grammar.
4. **Break template uniformity (L1, L2, Q21, L13).** Componentize the scattered inline spacing tokens
   (correct tokens with no components is the classic generated tell), vary section rhythm, stagger the
   single reveal gesture, and vary the repeated `.rule-gold` motif.
5. **Spend the design system instead of defaulting it (H15, H18).** Tribal promotion color + real
   duotone portraits replace monochrome gold and 107 identical faded-letter tiles — the difference
   between a designed database and a template.

---

## Backend-flagged items (everything else ships static / no-build / crawlable)
- **H13 Tier 2** — community-aggregated ratings ("4.8 from 2,314 fans") needs a datastore. Ship the
  localStorage Tier 1 now.
- **H14 production** — real double-opt-in + founding-member badge needs an ESP form endpoint (a form
  `action`, not a server you host).

The two structural risks — a hand-copied nav/head and a hand-authored search index/roster/counts — are
both solved by moving them into the existing `build/` step (H2, H3) so they can never drift from the
content on disk again.
