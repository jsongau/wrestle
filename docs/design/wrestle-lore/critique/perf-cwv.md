# Wrestle Lore — Performance / Core Web Vitals Critique + Enhancement Spec

Role: adversarial senior Performance/CWV critic. Scope: font loading, LCP, CLS, INP/JS
execution, payload. Every item cites a real file/selector, gives a buildable fix for a
static, no-build, crawlable site, and a source reference. No praise.

Files inspected: `/index.html`, `/css/site.css` (909 lines, 68 KB / ~14 KB gzip),
`/js/main.js`, `/js/enhance.js`, `/js/nav.js`, `/js/search-index.js`, `/wrestlers/kane/index.html`,
`/events/index.html`, `/moments/mankind-hell-in-a-cell-fall-1998/index.html`.
Measured across the site with grep over all 191 `index.html` files.

---

## THE HEADLINE PROBLEM: the site has no measurement and no font strategy

There is not a single self-hosted byte on this site. No images (`find` for jpg/png/webp/
avif/woff2 returns **zero files** — every "photo" is a CSS gradient + initial letter), no
fonts, nothing. That is good for payload but it means **the entire perceived-performance
story rides on three render-blocking Google Fonts families**, and that story is currently
told inconsistently across the site. Worse, the build is provably inconsistent page-to-page,
which means your CWV field data will be noisy garbage the moment you turn on real-user
monitoring. Hard counts from the repo:

| Symptom | Count (of 191 pages) |
|---|---|
| Pages that load the Google Fonts stylesheet | 99 |
| Pages that DO NOT load the design fonts at all (silent system-font fallback) | **93** |
| Pages loading `main.js` render-blocking (no `defer`) | **99** |
| Pages loading `main.js` with `defer` | 76 |
| Pages loading `enhance.js` (the motion/count-up/reveal layer) | 30 |
| Pages that `preload` the stylesheet or any font | **0** |

The "gold-standard profile" `/wrestlers/kane/index.html` is in the wrong bucket on all three:
it loads **no Google Fonts link at all** (renders in system fonts — Anton/Oswald/Inter never
arrive), it loads `main.js` **without `defer`**, and it **omits `enhance.js`** entirely. So
the flagship template does not even render in the brand typeface, and its animated method
bars are dead (see F11). This is the single most important thing to fix because it invalidates
everything else: you cannot optimize what you have not standardized.

---

## PRIORITIZED FINDINGS (highest impact first)

### F1 — Google Fonts is render-blocking on a third-party origin and gates your LCP. SELF-HOST. [CRITICAL]
**Problem.** `/index.html` lines 25-27 (and 99 other pages):
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Oswald:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```
This is a **render-blocking request to a third origin** (`fonts.googleapis.com`) that itself
triggers a **second** blocking hop to `fonts.gstatic.com` for the actual woff2 files. Even with
`preconnect`, that is a DNS+TLS+request chain on the critical path before your first paint, and
it is requesting **three families with nine total weight instances** (Anton, Oswald ×4, Inter
×4). Your LCP element is text painted in these fonts (see F3), so this chain is your LCP
critical path.

**Fix (buildable, no build step).** Download and self-host. Concretely:
1. Fetch the four woff2 files that `css2?...` currently serves (Anton regular; Oswald 400/600/700
   — you can drop 500, it is barely used; Inter 400/600/700 — drop 500). That is ~7 files max,
   realistically 5-6 after dropping the 500 weights.
2. Drop them in `/assets/fonts/` and add `@font-face` blocks to the top of `site.css` (or a tiny
   `fonts.css` loaded first). Point `--font-display`/`--font-cond`/`--font-sans` at them.
3. Delete both `preconnect`s and the `<link href="fonts.googleapis.com...">` from **all** pages.
This collapses two third-party origins to your own origin, removes two render-blocking external
requests, and lets you `preload` the exact files you need (F2). corewebvitals.io documents this
as a direct CWV win; DebugBear measured a single-font LCP improvement of **1.82s → 1.24s** just
from removing the discovery/handshake delay.
**Source:** https://www.corewebvitals.io/pagespeed/self-host-google-fonts and
https://www.debugbear.com/blog/preload-web-fonts

### F2 — Nothing is preloaded; the LCP font is discovered late. Preload ONLY the hero display font. [CRITICAL]
**Problem.** Zero pages preload anything (`rel="preload"` count = 0). Once self-hosted (F1),
the browser still will not discover the hero font until it has downloaded and parsed `site.css`
(68 KB) and matched `.hero-bb__title{font-family:var(--font-display)}` at line 436. That is a
late discovery for the element that IS your LCP.

**Fix.** After self-hosting, add exactly one preload for the display font (Anton) in `<head>`,
above the stylesheet:
```html
<link rel="preload" href="/assets/fonts/anton-latin-400.woff2" as="font" type="font/woff2" crossorigin>
```
Preload **only** the above-the-fold display face — not Oswald or Inter — because over-preloading
competes for bandwidth with the stylesheet itself. DebugBear: "Any important fonts used above the
fold should be preloaded... only the most important requests should be preloaded." On interior
pages (Kane, events, moments) the LCP is an `<h1>` also in Anton, so the same single preload
applies site-wide — put it in the shared `<head>` partial.
**Source:** https://web.dev/articles/preload-critical-assets and
https://www.debugbear.com/blog/preload-web-fonts

### F3 — LCP is text in Anton with `display=swap` → guaranteed CLS + late LCP from a metric-mismatched swap. Add a size-adjusted fallback. [CRITICAL, CLS+LCP]
**Problem.** The LCP element on the homepage is `.hero-bb__title` (`/index.html` line 133,
"EVERY RIVALRY / EVERY MATCH / EVERY LEGEND"), styled `font-size:clamp(3rem,7.5vw+.5rem,8rem)`
in Anton (`site.css` line 436-438). With `display=swap`, the browser paints the title in the
**fallback** font first, then re-paints in Anton when it arrives. Anton is an ultra-condensed,
tall display face; the system/`Inter` fallback has completely different advance widths and
cap-height. When the swap fires, three lines of a clamped 8rem headline reflow → a large,
above-the-fold **layout shift** that lands squarely in your CLS window, plus the "real" LCP
candidate paints late. This is the classic swap-CLS trap.

**Fix (buildable).** Define a size-adjusted fallback `@font-face` so the fallback occupies the
*same box* as Anton, eliminating the swap shift (this is exactly what Next.js `next/font` and
the Fontaine tool automate — you are just doing it by hand once):
```css
@font-face{
  font-family:"Anton Fallback";
  src:local("Arial Narrow"),local("Impact");
  size-adjust:105%;        /* tune with Fontaine / Malte Ubl's calculator */
  ascent-override:90%; descent-override:22%; line-gap-override:0%;
}
:root{ --font-display:"Anton","Anton Fallback","Arial Narrow",sans-serif; }
```
Keep `display=swap` (or `optional`) — with a matched fallback the swap is now visually seamless
and CLS stays ~0. Do the same one-line trick for Oswald (condensed UI) since it is used on
every `.tile__name`, `.eyebrow`, nav, etc. Inter can stay `swap` against system-ui (metrics are
close). Metric values from Malte Ubl's "high performance web font loading" write-up.
**Source:** https://www.industrialempathy.com/posts/high-performance-web-font-loading/ and
https://vercel.com/academy/nextjs-foundations/fonts-with-next-font (documents next/font's
automatic size-adjust fallback rationale)

### F4 — Standardize the `<head>` and script tags across all 191 pages. [CRITICAL, correctness+CWV consistency]
**Problem.** 93 pages have no font link, 99 load `main.js` blocking, only 30 load `enhance.js`.
Two different `<head>` templates are in the wild (compare `/index.html` line 27 which has fonts,
vs `/wrestlers/kane/index.html` line 9 which does not). Field CWV will be bimodal and
un-actionable.

**Fix.** One shared head/footer partial, stamped by the same generator that produced the pages.
Every page ships: (a) the single font preload (F2), (b) self-hosted `@font-face`, (c) `site.css`,
(d) scripts with `defer`. There is no reason for `main.js` to ever be render/parse-blocking —
add `defer` everywhere (it is at end-of-`<body>` on Kane so parse impact is small, but `defer`
also guarantees ordered, non-blocking execution and future-proofs against someone moving it into
`<head>`). Ship `enhance.js` only on pages that actually use `[data-reveal]`/`[data-count]`/
`.mb-fill`/record tables — but Kane uses `.mb-fill` and does NOT ship it (F11), so the current
split is wrong, not lean.

### F5 — `search-index.js` (11 KB / 2.9 KB gz) loads on EVERY page but is only needed on ⌘K open. Lazy-load it. [HIGH, INP/payload]
**Problem.** `/index.html` line 291 and every page loads `/js/search-index.js` (`defer`), which
declares `window.MAT_SEARCH_INDEX`. `nav.js` (line 4) reads it at load. But the palette is only
ever shown after the user presses ⌘K / `/` or clicks the search button. So on 100% of page loads
you pay to download + parse the full index that ~5% of sessions will use, on the critical
resource list.

**Fix (buildable).** Load the index on first intent. Keep `nav.js` tiny; when `open()` is first
called (`nav.js` line 11), inject `<script src="/js/search-index.js">` and build results in its
`onload`. Or use `<link rel="prefetch" href="/js/search-index.js">` (idle-time, non-blocking)
plus a lazy `import()`-style injection on interaction. Net effect: one fewer render-adjacent
request and ~3 KB less parse on every single navigation.
**Source:** https://web.dev/learn/performance/optimize-resource-loading (defer non-critical JS;
load on interaction)

### F6 — `heroDrift` animates `background-position` infinitely = continuous main-thread repaint. [HIGH, INP/CPU/battery]
**Problem.** `site.css` lines 420-427: `.hero-bb__bg` runs `animation:heroDrift 26s ease-in-out
infinite alternate` where the keyframes (line 427) animate **`background-position`** across a
`180%/200%` sized multi-radial-gradient over the full hero (min-height up to 940px).
`background-position` is **not** a compositor-only property — every frame repaints a huge gradient
layer on the main thread, forever, even when idle. That is a standing INP/scroll tax and a
laptop-fan/mobile-battery drain for a subtle effect most users will not notice.

**Fix.** Either (a) drop the animation and keep the static conic/radial gradient (it looks
identical for the first 2s anyway), or (b) if you want motion, animate a **`transform`** on the
`::before`/`.hero-bb__bg` layer (translate/scale a slightly oversized gradient), which the
compositor handles off-main-thread. You already do the correct thing on `.marquee__track` (line
463, `transform:translateX`) — apply the same discipline here. Respect the existing
`prefers-reduced-motion` guard (line 428) either way.
**Source:** https://web.dev/articles/optimize-lcp and general CWV guidance — animate only
`transform`/`opacity`.

### F7 — Persistent `backdrop-filter: blur()` on the sticky header (and glass/subnav/cmdk) repaints on every scroll. [MEDIUM-HIGH, INP/scroll]
**Problem.** `.site-header` (line 97-98) is `position:sticky` with `backdrop-filter:blur(10px)`
and is on screen for the whole session. `enhance.js` (line 125) toggles `.is-stuck` on scroll,
which changes `box-shadow`/`border-color` on that same blurred layer. `backdrop-filter` forces
the browser to sample and blur everything behind the element; doing that on a sticky bar during
scroll is a well-documented scroll-jank source (VitePress hit exactly this). Additional blur
layers: `.glass` stats-bar (line 447), `.subnav-page` (line 538), `.cmdk` overlay (line 883).

**Fix.** (a) Reduce header blur radius (10px → 6px) and, more importantly, ensure the header is
promoted to its own layer with `will-change:transform` or `transform:translateZ(0)` so the blur
result can be cached between identical frames. (b) The `is-stuck` scroll listener is throttled
by nature (only toggles a class) — fine — but avoid changing properties that invalidate the
blur cache; animate `box-shadow` via an inserted non-blurred `::after` sibling instead of on the
blurred element. (c) Provide a `@supports not (backdrop-filter:blur(2px))` solid-bg fallback for
the header like you already do for `.glass` (line 450) — currently the header has none, so
unsupported browsers get a semi-transparent unreadable bar.
**Source:** https://github.com/vuejs/vitepress/issues/1049 (blurred navbar scroll perf) and
https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter

### F8 — Long profile/event pages have no `content-visibility`; the browser lays out everything up front. [MEDIUM, rendering cost]
**Problem.** Pages like Kane render a bio, championship panel, personas, a 10-item timeline,
signature-match grid, and a full match-record table — all in the initial layout/paint pass even
though most is far below the fold. On the bigger event and roster pages this is a measurable
first-render cost.

**Fix (buildable, one line).** Add to below-the-fold section blocks:
```css
.record-section, .sig-section, .media-rail, .bento, .faq { content-visibility:auto; contain-intrinsic-size:auto 600px; }
```
Browser skips layout/paint for off-screen sections until they scroll near the viewport;
`contain-intrinsic-size` reserves space so it does **not** introduce CLS or break the scrollbar.
Do **not** apply it to the hero or first section. Guard the intrinsic size so anchored links
(`[id]{scroll-margin-top:112px}`, line 614) still resolve.
**Source:** https://web.dev/learn/performance/optimize-resource-loading and
https://developer.mozilla.org/en-US/docs/Web/CSS/content-visibility

### F9 — 68 KB single render-blocking stylesheet, no critical-CSS inlining. [MEDIUM, FCP/LCP]
**Problem.** `site.css` is 68 KB (14 KB gzip), a **single render-blocking** stylesheet on every
page, and it is loaded (on the 99 font pages) *after* the render-blocking Google Fonts link, so
first paint waits on both. 14 KB gzip is not huge, but it is 100% blocking and contains styles
for record tables, tiers, media rails, QR blocks, etc. that most pages never use.

**Fix (buildable).** Two options, pick one:
- **Cheap:** inline the ~2-3 KB of critical shell CSS (tokens, header/nav, hero, stats-bar,
  buttons) in a `<style>` in `<head>`, then load `site.css` with the standard
  `rel="preload" as="style" onload="this.rel='stylesheet'"` async pattern + `<noscript>`
  fallback (keeps it crawlable and progressive).
- **Structural:** split `site.css` into `core.css` (tokens+shell+home) always loaded, and
  `record.css`/`events.css`/`profile.css` loaded only by the templates that need them.
Given "no build step," the async-load-with-inlined-critical approach is the lowest-effort win.
Once fonts are self-hosted (F1), first paint depends only on your own origin + this file.
**Source:** https://web.dev/articles/optimize-lcp (eliminate render-blocking resources) and
https://web.dev/learn/performance/optimize-resource-loading

### F10 — `text-rendering:optimizeLegibility` globally on `<body>`. [LOW-MEDIUM, rendering]
**Problem.** `site.css` line 69: `text-rendering:optimizeLegibility` on `body`. This forces
kerning/ligature computation for **all** text on the page and is a known cause of slow first
paint on text-heavy pages (and this is a text-only site). It rarely produces a visible
improvement over the default.

**Fix.** Remove it; let it default to `auto`. Keep `-webkit-font-smoothing:antialiased`.
**Source:** https://web.dev/articles/optimize-lcp (avoid unnecessary main-thread text work);
long-standing guidance from the CSS performance community.

### F11 — Kane's animated method bars are dead because `enhance.js` is missing (perf-adjacent correctness). [MEDIUM, but flag it]
**Problem.** `.mb-fill{width:0}` and `.is-in .mb-fill{width:var(--w)}` (`site.css` lines 630-632)
depend on `enhance.js` adding `.is-in`. `/wrestlers/kane/index.html` does **not** load
`enhance.js` (line 207-209) and its method bars (lines 167-170) are not inside a `[data-reveal]`
wrapper, so `.is-in` is never applied → the bars render at **width 0 (invisible)**. This is
downstream of the F4 template inconsistency. Either ship `enhance.js` on profile pages, or add a
no-JS fallback: `.mb-fill{width:var(--w)}` as the base and only reset to 0 under `.js`
(mirroring the `.js [data-reveal]` pattern at line 394) so bars are correct without JS and
animate with it.

### F12 — Minor payload/wins worth batching in. [LOW]
- **Drop the 500 weights** from Oswald and Inter in the font request/self-host set (`css2?...`
  requests `wght@400;500;600;700` for both) — grep shows the design system uses 400/600/700;
  500 is dead weight (two fewer font files).
- **Two SVG grain data-URLs** run `feTurbulence` filters (`site.css` line 390 `.grain`, line 430
  `.hero-bb__grain`). `feTurbulence` is a comparatively expensive filter to rasterize; they are
  static so cost is one-time, but on the hero it rasterizes a full-viewport layer. Acceptable,
  but if INP audits flag it, pre-bake the noise to a small tiling PNG (still one static asset,
  cheaper to composite).
- **`min-height:100dvh` on `body`** (line 69) is fine, but combined with the `100dvh` hero and
  `-webkit-fill-available` quirks on iOS, verify no address-bar-driven resize shift; reserve
  hero height with the `clamp()` (already done, line 418 — good, keep it).
- **Facade pattern is correct — keep it.** `/index.html` lines 144-149 use a `<button>` facade
  that opens YouTube in a new tab (zero iframe), and `main.js` lines 37-56 lazily inject a
  `youtube-nocookie` iframe only on click with `loading="lazy"`. This is best-practice; do NOT
  regress it into an always-embedded iframe. (Noted as the one thing already done right.)

---

## PRIORITIZED ACTION LIST (do in this order)

1. **F4 + F1:** Standardize one `<head>`/footer partial; self-host the 5-6 woff2 files; delete
   all Google Fonts `<link>`/`preconnect`. (Fixes 93 broken pages + removes 2 blocking origins.)
2. **F2 + F3:** Preload only Anton; add size-adjusted `@font-face` fallbacks for Anton + Oswald.
   (Kills swap-CLS on the hero + interior H1s and pulls LCP in.)
3. **F5:** Lazy-load `search-index.js` on first ⌘K/`/`/click. (−3 KB parse every navigation.)
4. **F6 + F7:** Convert `heroDrift` to a `transform` animation (or drop it); layer-promote the
   sticky header, cut blur to 6px, move `is-stuck` shadow off the blurred element, add a
   `@supports` solid fallback. (Removes standing repaint + scroll jank.)
5. **F9:** Inline critical shell CSS + async-load `site.css`. (Faster FCP/LCP.)
6. **F8 + F10 + F11 + F12:** `content-visibility:auto` on below-fold blocks; drop
   `optimizeLegibility`; fix method-bar no-JS fallback; drop 500 weights.

**Expected impact (order-of-magnitude, static site, throttled mobile):**
- LCP: self-host + preload + size-adjust fallback typically pulls text LCP in by **0.4-0.8s**
  (DebugBear's single-font case = 0.58s) and removes the third-party handshake variance.
- CLS: size-adjusted fallbacks take the hero swap shift from a visible reflow to **~0**.
- INP/scroll: killing the infinite `background-position` repaint (F6) + taming header blur (F7)
  removes the two standing main-thread costs; most impactful on low-end Android.
- Payload/parse: −2 font weights, −3 KB index per nav, async CSS — modest but free.

---

## SOURCES
- Self-hosting Google Fonts for CWV — https://www.corewebvitals.io/pagespeed/self-host-google-fonts
- Preloading web fonts (LCP numbers, above-the-fold only) — https://www.debugbear.com/blog/preload-web-fonts
- High-performance web font loading / size-adjust fallbacks — https://www.industrialempathy.com/posts/high-performance-web-font-loading/
- next/font automatic size-adjust rationale — https://vercel.com/academy/nextjs-foundations/fonts-with-next-font
- Preload critical assets — https://web.dev/articles/preload-critical-assets
- Optimize resource loading (defer JS, async CSS) — https://web.dev/learn/performance/optimize-resource-loading
- Optimize LCP — https://web.dev/articles/optimize-lcp
- backdrop-filter scroll-perf issue — https://github.com/vuejs/vitepress/issues/1049
- backdrop-filter / content-visibility — https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter , https://developer.mozilla.org/en-US/docs/Web/CSS/content-visibility
