# Wrestle Lore — Visual / Brand Design Critique + Enhancement Spec

Role: Senior visual/brand designer. Adversarial review. No praise.
Scope reviewed: `/index.html`, `/css/site.css` (all 909 lines), `/wrestlers/kane/index.html`, `/events/index.html`, `/moments/mankind-hell-in-a-cell-fall-1998/index.html`, `/js/nav.js`, `/js/main.js`. Cross-checked 88 wrestler pages.
Date: 2026-07-26.

---

## VERDICT UP FRONT

The homepage is the only page that looks designed. It is genuinely good — the Broadcast Bold hero, glass stats bar, marquee, duotone tiles and gradient-edge poster are 2024-2025-competent. But the moment you leave the homepage the illusion collapses, and it collapses hardest on the single most important page type on the entire site: **the wrestler profile.** The "gold-standard" Kane page renders as **near-unstyled browser-default HTML** because its entire template was written against a class vocabulary that does not exist in `site.css`. That is not a polish problem. That is a broken flagship. Everything else in this document is secondary to that.

Second-order problem: the design system is **two design systems fighting**. There is the original `.card / .profile / table.record / .rt-filters` vocabulary (lines 175-573) and the newer `.tile / .ev-hero / .sec-h / .me-card` Broadcast Bold vocabulary (lines 374-908). Pages pick from both bags at random, and the flagship page picks from a *third* bag that isn't in the file at all. The result reads as three different websites wearing the same header.

---

## CRITICAL — fix before anything else

### C1. The wrestler profile template is unstyled. 88 pages. (`wrestlers/kane/index.html`, all `wrestlers/*`)

**Problem.** `wrestlers/kane/index.html` uses `.athlete-hero`, `.hero-inner`, `.hero-sub`, `.hero-desc`, `.content-grid`, `.bio-col`, `.stats-col`, `.stat-card`, `.stat-big`, `.stat-num`, `.champ-row / .cr-title / .cr-reign / .cr-note`, `.persona-card`, `.sig-section / .sig-grid / .sig-match`, `.record-section`, `.record-filter / .rf-btn`, `.record-table`, `.res-cell / .res-badge`, `.timeline .tl-year`, `.mb-label / .mb-pct`. I grepped the entire `css/` directory (one file, `site.css`): **zero** of these selectors exist. `site.css` instead defines a *different* profile system — `.profile`, `.profile__photo`, `.facts`, `.champ-panel / .champ-rows .k`, `table.record`, `.rt-filters button`, `.res / .res-w / .res-l`, `.persona`, `.timeline time` — that the Kane page never uses. So the page falls through to UA defaults: white-on-dark Inter at default weight, a default `<table>` with thin gray borders and no zebra, default `<button>` chrome for the filters, default `<details>` triangles for the FAQ, an `<h1>` in Inter (not Anton), and `.athlete-hero` with no background, no type treatment, no spacing. This is stamped across **88 wrestler files** (confirmed via grep for `class="athlete-hero"`).

Additional consequence: the record filter buttons (`.rf-btn`, `data-filter="ppv"`) are also **dead functionally** — `main.js` (lines 64-98) wires `[data-filter]` as a text *input* against `[data-search]` rows; Kane's markup has neither, so clicking a filter does nothing. Unstyled *and* inert.

**Fix.** Two valid paths; pick one and enforce it repo-wide:
- (A) Re-stamp all 88 profiles onto the vocabulary `site.css` already styles (`.profile`, `.facts`, `.champ-panel`, `table.record` + `.rt-filters`, `.persona`, `.tabs`). Cheapest if the build script that generated Kane can be re-pointed.
- (B) Add the missing selectors to `site.css`. Faster to hotfix, but you are then maintaining a third vocabulary — do this only as a stopgap.

Either way, add a **build-time guard**: a script that greps every emitted HTML file's `class="..."` tokens against the set of selectors defined in `site.css` and fails the build on any class with zero matching rule. This is the single highest-value thing you can build; it would have caught this before 88 pages shipped.

**Buildability.** Fully static. Path A is a template edit + re-run. The guard is ~30 lines of Python/node over the existing files, no backend.

**Source reference.** Letterboxd's film page is the exact analog of your wrestler page (entity + stats sidebar + rating + records) and it is *ruthlessly consistent* — every film uses one card/stat/rating component set. That consistency is why it feels premium despite being data-dense (see the Pratt IXD teardown of Letterboxd's design system, https://ixd.prattsi.org/2025/05/letterboxd-disassembled-creating-a-design-system-for-movie-review-site-letterboxd/). Your problem is not taste, it is that the flagship isn't wired to the system at all.

### C2. FAQ markup is inconsistent and half of it is unstyled (`wrestlers/kane/index.html:140`, `moments/...:146`)

**Problem.** `site.css` styles `.faq details` (line 298). The moments page uses `class="faq faq-block"` — styled correctly. The Kane page uses `class="faq-block"` **without** `.faq` — so its `<details>` render as raw UA disclosure widgets (default triangle, no border, no padding, no `+/–` affordance from line 302). Same content type, two renderings, one broken.

**Fix.** Standardize on `class="faq"` (drop the meaningless `.faq-block`) in the profile template, or add `.faq-block` as an alias in `site.css`. Prefer the former.

**Buildability.** Static, one template token.

---

## HIGH — hierarchy, rhythm, type, color

### H1. There is no page-level vertical rhythm system; spacing is ad-hoc inline styles (`index.html` throughout)

**Problem.** The homepage leans on inline `style="margin-top:var(--sp-7)"`, `style="padding:var(--sp-6)"`, `style="font-size:var(--fs-600)"`, `style="align-self:center"` (lines 141, 170, 231-233, 243, 275). Tokens are used, so values are consistent, but the *placement* is scattered across markup instead of living in classes. This is the classic AI-generated tell: correct tokens, no componentization. It makes the rhythm impossible to tune globally and guarantees drift as pages multiply. Section padding is a single `--sp-8` clamp on every `.section` (line 84) — so a dense 6-tile rail and a one-line CTA band get identical breathing room, which flattens the pacing. Premium editorial sites vary section rhythm deliberately (tight cluster, then a big exhale before a feature).

**Fix.** (1) Kill inline spacing/size styles; move each into a component class (`.bento__lead`, `.cta-band h2`, etc.). (2) Introduce a rhythm scale on sections: `.section--tight` (already exists, unused on home), `.section` (default), `.section--feature` (larger `padding-block`, e.g. `--sp-8` top / `--sp-7` bottom asymmetry) so the eye gets a cadence rather than a metronome. (3) Add `:where(.section) > .wrap > * + *` flow spacing so intra-section rhythm isn't hand-placed.

**Buildability.** Pure CSS + markup cleanup, no JS.

**Source reference.** Vercel and Linear marketing pages use asymmetric section padding (more space above a feature than below it) to create "chapters." See the 2026 bento/rhythm guidance in SaaSFrame's practical guide (https://www.saasframe.io/blog/designing-bento-grids-that-actually-work-a-2026-practical-guide) — the takeaway relevant here is *rhythm variance*, not uniform gaps.

### H2. Type scale is technically fine but the display font is under-used and the mid-scale is muddy (`site.css:39-45, 70-71, 436`)

**Problem.** You license three faces (Anton display, Oswald condensed, Inter body) but Anton (`--font-display`) appears almost nowhere outside the hero title and a few stat numbers. Section headings (`h2`) render in Oswald (`.section-head h2`, line 93), tile names in Oswald, event names in Anton (`.ev-tile__name`, line 856) — so the "voice" of a heading changes page to page with no rule. Meanwhile the numeric scale has a gap: `--fs-600` (1.35-1.8rem) to `--fs-700` (1.65-2.55rem) overlap heavily at small viewports, so `h2` and `h3` are nearly the same size on mobile, collapsing hierarchy exactly where screen space is tightest.

**Fix.** (1) Write a one-line rule: **Anton = hero + section H2 + entity H1** (the "broadcast" moments); **Oswald = UI labels, kickers, table headers, chips, meta**; **Inter = body + long-form only.** Apply it in `site.css` component rules, not per page. (2) Pull `--fs-600` down slightly (`clamp(1.25rem,1.1rem+.6vw,1.6rem)`) so H2/H3 separate on mobile. (3) Anton needs negative tracking at large sizes (you do this on `.hero-bb__title` at `-.005em`, line 437) — apply the same to all Anton headings; Anton set at `0` tracking looks like default poster clip-art.

**Buildability.** Pure CSS token + rule edits.

**Source reference.** The Ringer and Athletic lead with one heavy display face used *only* for the top of the hierarchy and everything else drops to a workhorse sans — that discipline is what stops a 3-font system from looking like a font sampler.

### H3. Gold is doing every job; the red is nearly wasted; category colors never appear (`site.css:15-37, index.html`)

**Problem.** Look at the homepage: eyebrows are gold, `rule-gold` is gold, `link-more` is gold, stat numbers are gold, buttons are gold, tile kickers are gold, ratings are gold, the answer callout is gold, the CTA border is gold. Red shows up on one marquee dot and the video play button. You defined a rich token set — promotion accents (`--c-wwe`, `--c-wcw`, `--c-tna`…), category tokens (`--c-womens`, `--c-hof`, `--c-media`, era colors) — and the homepage uses essentially none of them. The effect is monochrome-gold, which reads as "one accent applied everywhere," i.e. generic luxury-template. Wrestling's whole visual language is *tribal color* (nWo black/white, DX green, Bloodline, brand reds/blues). You have the tokens and you're not spending them.

**Fix.** (1) Establish a color *hierarchy of meaning*, not decoration: gold = rating/quality/premium only; red = live/urgent/CTA-action; promotion accent = provenance (chip + a 2px top-border on the tile). (2) On the "Five-Star Classics" and "Icons" rails, let each tile carry a faint promotion-tinted top edge (`border-top:2px solid var(--c-wwe)` etc.) so the grid reads as *multi-promotion* at a glance instead of uniform gold. (3) Introduce the women's/HOF/media accents on their respective hubs so those sections have identity. Gold should feel *earned* (a 5-star match, a HOFer), not ambient.

**Buildability.** Pure CSS; tokens already exist. Note `--c-njpw`/`--c-aew` are marked `VERIFY hex` in `site.css:24-25` — verify before shipping NJPW/AEW accents.

**Source reference.** Sofascore and ESPN use league/team color as a *wayfinding* signal (you always know which competition you're in). Letterboxd, by contrast, is deliberately monochrome because film has no team colors — you have team colors and are throwing the advantage away.

### H4. The gold gradient-text + gold-on-dark is a contrast liability (`site.css:439-441, 624-626, 776-778`)

**Problem.** `-webkit-background-clip:text` gold gradients (hero accent, `.rec-stat .n`, event `h1`) look great on desktop but the darkest stop (`--c-gold-dim #8c7420`) against `#0a0b0d` on thin Anton strokes is borderline for AA, and the gradient's bottom third dips below it. Also `color:transparent` clipped text is invisible to some high-contrast / forced-colors modes and prints blank. `--c-text-dim` was lifted to `#828a96` (line 612, good) but gold gradient text got no such audit.

**Fix.** (1) Add `@media (forced-colors: active){ .hero-bb__title .accent,.ev-hero h1,.rec-stat .n{ -webkit-text-fill-color:currentColor; color:CanvasText; background:none; } }`. (2) Raise the dark stop of display gradients to `--c-gold` (not `--c-gold-dim`) so the whole glyph clears AA. (3) For any gold text under `--fs-500`, use solid `--c-gold-bright`, never the gradient.

**Buildability.** Pure CSS.

**Source reference.** Standard WCAG forced-colors handling; Apple's bento marketing pages keep gradient text strictly at display sizes and never in the AA-critical mid-scale.

---

## MEDIUM — card/tile craft, depth, motion

### M1. Tiles have no image and lean on a letter-mono crutch that will look identical across dozens of cards (`site.css:474-496`, `index.html:202-224`)

**Problem.** The duotone tile is the nicest component you built, but its "art" is a single giant faded letter (`.tile__mono`, line 483) plus a diagonal `--seed` gradient. On a 6-tile rail it's charming; on a 40-wrestler roster grid it becomes forty near-identical dark rectangles distinguished only by a letter and a hue angle. That is the definition of "flat and generic at scale," and it's the experience a WWE hiring manager will click into first (the roster). The `--seed` angle trick also produces some genuinely muddy near-brown gradients at certain values (e.g. seeds around 40-90 on the red base).

**Fix.** (1) Ship real cutout portraits. Even without a photo budget, a **duotone-treated silhouette PNG** per wrestler (gold/black or promotion-color/black) transforms the grid — this is buildable statically as a per-wrestler `<img>` with `mix-blend-mode:luminosity` over the gradient. (2) Until photos exist, replace the single letter with a **two-line monogram + promotion glyph** and constrain `--seed` to a curated set of 6 hand-picked angles that never go muddy, rather than arbitrary 0-360. (3) Add a subtle bottom-to-top scrim (`linear-gradient(0deg,#000 0%,transparent 45%)`) behind `.tile__body` so text always has a legibility floor once real images land.

**Buildability.** Static. Duotone via CSS `mix-blend-mode` + a single-color silhouette; no build step. Portraits are an asset-sourcing task, flagged — not an engineering blocker.

**Source reference.** Letterboxd poster grids and The Ringer's ranked-list cards prove image-forward cards are the addictive unit; Cagematch (your data competitor) is *pure table* and looks like a 2009 database — beating it on card craft is your entire visual edge, so don't ship letter-only tiles at scale.

### M2. Hover is the only interaction state; there's no press, no focus polish on tiles, and reveal is the only motion (`site.css:394-398, 477, 490`)

**Problem.** Tiles do `translateY(-4px)` + shadow on hover (line 477) and a cursor-follow spotlight (`.tile__spot`, requires JS to set `--mx/--my` — is that wired? `main.js` has no mousemove handler, so **the spotlight never activates**; it's dead CSS). There is no `:active` press state anywhere, no tile focus-visible treatment beyond the global outline, and the only entrance motion is the single `data-reveal` fade-up used on nearly every block, so the whole page animates with one identical gesture. Uniform motion reads as templated.

**Fix.** (1) Either wire `.tile__spot` (a 6-line pointermove handler setting `--mx/--my` in %) or delete it — dead premium features are worse than none. (2) Add `.tile:active{transform:translateY(-1px) scale(.995);}` for tactile press. (3) Vary reveal: stagger rail children with `transition-delay:calc(var(--i)*60ms)` so a grid cascades instead of popping as one block (set `--i` inline per tile or via `:nth-child`). (4) Add `@media (hover:none)` fallbacks so touch users get the resting state, not stuck hover.

**Buildability.** Static CSS + ~6 lines JS for the spotlight (optional). All motion already gated behind `prefers-reduced-motion` (line 61) — keep that.

**Source reference.** Linear's card hover (lift + inner highlight + cursor-aware sheen) and the "premium bento interactions" catalog (https://superfiles.in/interactive-bento-grid-guide.php) — the pattern to steal is *cursor-tracked light on the card surface* plus a distinct press state, which you already half-built and left unwired.

### M3. Depth is a single flat shadow language; no elevation ladder (`site.css:52-53, 382-384`)

**Problem.** You have `--shadow-1`, `--shadow-2`, `--shadow-gold`, `--glow-gold`, `--glow-red`, `--edge-light` — but they're applied inconsistently and there's no rule for *what elevation means*. The glass stats bar, the mega panel, the featured poster and a plain card can all end up with `--shadow-2`, so nothing feels definitively "closer." Dark UIs need elevation carried by **surface lightness + inner top highlight**, not just drop shadow (shadows barely read on `#0a0b0d`).

**Fix.** Define an explicit ladder: elev-0 = page; elev-1 = `--c-bg-elev-1` + `--edge-light`; elev-2 = `--c-bg-elev-2` + `--edge-light` + `--shadow-1`; elev-3 (modals/mega/cmdk) = `--c-bg-elev-2` + `--shadow-2` + brighter hairline border. Apply `--edge-light` (inner top highlight) to *every* raised surface — it's the cheapest, most convincing dark-mode depth cue and you're only using it in a few places.

**Buildability.** Pure CSS token discipline.

**Source reference.** Material 3 and Vercel's dark theme both carry elevation primarily through surface tint + top inner-highlight on dark backgrounds; drop shadow is secondary. Your `--edge-light` is exactly this — spend it everywhere.

### M4. Grain and duotone are present but timid, and the grain double-stacks (`site.css:388-391, 429-431, 481-482`)

**Problem.** You have three separate grain/hatch systems: global `.grain` (line 389, opacity .05), hero `.hero-bb__grain` (line 429, opacity .07), and tile scanlines (line 481). On the homepage the global grain overlays the hero grain — two noise layers stacked, which at 60px scroll can shimmer/moire on some displays, and `mix-blend-mode:overlay` over near-black does almost nothing visible (overlay of mid-gray noise on `#0a0b0d` barely lifts). So you pay the render cost of grain and get almost none of the texture benefit. Duotone is only on tiles, not on heroes or section seams where it would sell the "broadcast" feel most.

**Fix.** (1) Pick one grain owner per stacking context: keep hero grain in the hero, suppress global `.grain` inside `.hero-bb`. (2) Switch grain blend to `soft-light` or bump opacity to ~.09-.12 and use a lighter noise fill so it actually reads on black. (3) Extend duotone treatment to the profile hero background (once C1 is fixed) and to `.seam` transitions for a consistent film-broadcast texture.

**Buildability.** Pure CSS.

**Source reference.** Grain/duotone is called out as a live 2026 trend (Studio Meyer, https://studiomeyer.io/en/blog/webdesign-trends-2026); the craft note is that on true-black UIs you must raise grain opacity and use soft-light or it's invisible — a common failure this site currently has.

### M5. Bento is only used once and doesn't earn the name (`index.html:230-234`, `site.css:531-533`)

**Problem.** The one `.bento` (Relationships) is a 1-wide + 2-square row — a fine 3-up, but it's not a *bento* (varied cell sizes/aspect ratios creating rhythm). `.bento>.is-wide{grid-column:span 2}` is the only size variant. For a site whose whole pitch is "everything is connected," the connection section is the flattest grid on the page.

**Fix.** Build a real bento for the relationships/"The Web" module: one tall hero cell (the Anoa'i dynasty, image-led), two medium, three small stat cells (counts of factions/couples/families), one wide "explore the map" CTA cell — varied `grid-row`/`grid-column` spans with a defined mobile collapse. This is also your best homepage screenshot for a portfolio.

**Buildability.** Pure CSS Grid with explicit `grid-template-areas` and a `@media` collapse; no JS.

**Source reference.** Apple product bento and the 2026 bento examples roundup (https://mockuuups.studio/blog/post/best-bento-grid-design-examples/) — the working principle is *deliberate cell-size variance tied to content importance*, which your single span-2 doesn't do.

---

## LOW — polish, consistency, credibility

### L1. Homepage stat numbers contradict the actual database (`index.html:163`)
Hero stats say "41+ Wrestlers" but the repo has ~88 wrestler profiles (grep count) and the brief cites 89. Under-selling your own scale on the hero, and it's a credibility tell if a reviewer counts. Update the `data-count` values and keep them build-generated, not hand-typed. Pure static fix.

### L2. Two facade video patterns coexist (`index.html:144-149` inline `onclick` vs `moments/...:126` `data-provider`)
The homepage hero uses an inline `onclick` that opens a YouTube *search*, while every other page uses the clean `.facade[data-provider]` click-to-load handled by `main.js:37-56`. The hero should use the real facade so the featured match actually plays inline like the rest of the site. Consistency + it's the marquee interaction on the page.

### L3. `.rule-gold` under every section head is a repetitive motif (`index.html:198,214,229,264`, `site.css:401`)
The 120px gold underline appears under every H2 identically. Fine once, monotonous four times in a scroll. Vary it: some sections could use the `.sec-h` left-bar treatment (line 804, already built and nicer) instead. Right now the events page (`.sec-h`) looks more considered than the homepage (`.rule-gold`) — unify on the stronger one.

### L4. `--dur:180ms` global with one easing curve makes all motion feel the same (`site.css:54`)
Every transition uses `var(--dur) var(--ease)`. Distinguish micro (hover 120-160ms) from macro (reveal 500-700ms, already 0.7s) and give overlays/mega a slightly different curve. Small, but uniform timing is part of why non-hero pages feel flat.

### L5. Mobile mega-nav dumps all panels open as static lists (`site.css:140-144`)
On mobile the `.mega` becomes a static left-bordered list under each tab. With Wrestlers (3 cols) + Events (3 cols) that's a very long accordion. Verify the sub-panel toggle (`main.js:22-34`) collapses them by default (it sets `.is-open`), and consider not rendering the "Featured wrestlers" column on mobile — it's the least useful and longest. UX-adjacent but affects perceived polish on the device most reviewers will use first.

---

## PRIORITY ORDER (build this order)
1. **C1** — restyle/re-stamp the 88 wrestler profiles + add the class-coverage build guard. Nothing else matters until the flagship page looks designed.
2. **C2, H3, H1** — FAQ consistency; spend the color tokens (promotion accents on tiles); kill inline spacing into components.
3. **M1, M5** — real/duotone portraits + a true bento; these are the two biggest "premium vs template" levers and your best portfolio screenshots.
4. **H2, H4, M2, M3, M4** — type discipline, contrast/forced-colors, wire-or-delete the spotlight + press states, elevation ladder, grain that's actually visible.
5. **L1-L5** — credibility and consistency cleanup.

Sources consulted: [Letterboxd design-system teardown (Pratt IXD)](https://ixd.prattsi.org/2025/05/letterboxd-disassembled-creating-a-design-system-for-movie-review-site-letterboxd/), [Designing bento grids that work — SaaSFrame](https://www.saasframe.io/blog/designing-bento-grids-that-actually-work-a-2026-practical-guide), [Best bento grid examples 2026 — Mockuuups](https://mockuuups.studio/blog/post/best-bento-grid-design-examples/), [Premium bento interactions 2026 — Superfiles](https://superfiles.in/interactive-bento-grid-guide.php), [Web design trends 2026 — Studio Meyer](https://studiomeyer.io/en/blog/webdesign-trends-2026).
