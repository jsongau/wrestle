# Wrestle Lore — Mobile / Responsive Critique + Enhancement Spec

Role: adversarial mobile/responsive critic. Test viewport: **360px** (iPhone SE / low-end Android, the real-world floor), one-handed, iOS Safari + Chrome Android with dynamic toolbars.

Scope reviewed: `index.html`, `css/site.css` (full), `js/main.js`, `js/enhance.js`, `js/nav.js`, `wrestlers/kane/index.html` ("gold-standard" profile), `events/index.html`, `moments/mankind-hell-in-a-cell-fall-1998/index.html`.

Verdict up front: the design-system pages (home, events, moments) are *mostly* responsive because the grids use the `minmax(min(Xpx,100%),1fr)` idiom, which is genuinely good. But the mobile **navigation drawer is half-built** (no scroll lock, no scrim, no dismiss-on-tap-outside, no focus handling), the flagship **search is buried two taps deep and can barely be dismissed on a phone**, and the **"gold-standard" profile is not on the design system at all** — it renders as an unstyled raw table that horizontally overflows the entire page at 360px. For a project whose thesis is "the most SEARCHABLE, most ADDICTIVE wrestling site," the mobile funnel is the weakest surface in the build.

Everything below is buildable on a static, no-build, crawlable site. Two items flagged as needing a data/markup migration (not a backend).

---

## TIER 1 — Breaks or badly frustrates on a phone

### M1. The "gold-standard" profile is off-design-system and horizontally overflows the viewport
**Problem.** `wrestlers/kane/index.html` uses a class vocabulary that **does not exist in `css/site.css`**: `.athlete-hero`, `.hero-inner`, `.content-grid`, `.bio-col`, `.stats-col`, `.stat-card`, `.record-section`, `.record-table`, `.record-filter`, `.rf-btn`, `.sig-grid`, `.sig-match`, `.persona-card`, `.champ-row`/`.cr-title`/`.cr-reign`. I grepped `site.css` for all of them: **zero matches.** So apart from the shared header/footer/⌘K shell, the entire Kane page is unstyled default HTML. The design system already ships the correct components — `.profile` (grid `280px 1fr` ≥720px), `.facts`, `.table-wrap` + `table.record` (with `min-width:720px` **and** a `.record-mobile` card fallback at `max-width:760px`), `.rt-filters`, `.timeline`, `.faq` — and Kane uses none of them.
The mobile-fatal consequence is the match record. Kane's markup is a raw `<table class="record-table">` with **6 columns** (`R / Opponent / Event / Date / Stipulation / Note`) and **no `.table-wrap` overflow container and no `min-width`/card fallback** (`wrestlers/kane/index.html` lines 191–200). A 6-column table of long strings ("Won; Undertaker interference; one-day reign") cannot fit 360px; because it is not inside an `overflow-x:auto` box, the table widens the `<body>` itself, so the **whole page gets a horizontal scrollbar and pinch-zooms out** — the single worst mobile defect there is, and it is on the page held up as the template. If this format was cloned across the profile batch (the task list shows profiles built by `build_wrestlers_7*.py`), the bug is replicated site-wide.
**Fix.**
1. Re-template Kane (and any profile built in this format) onto the existing DS classes: `.profile`/`.profile__photo`/`.facts` for the header, `.champ-panel`/`.champ-rows` for titles, `.timeline` for the career list, `.faq` for FAQ, and the `.tabs` + `.record-scroll` (or `.record-desktop`/`.record-mobile`) record component that `enhance.js` already wires.
2. As an immediate hotfix even before re-templating, wrap every table in `<div class="table-wrap">…</div>` and give raw tables `min-width` so the scroll is trapped inside the box, never the page. Add a global guard so a stray wide element can never break layout again:
```css
html,body{overflow-x:clip;}                 /* page can never scroll sideways */
main :where(table){display:block;overflow-x:auto;-webkit-overflow-scrolling:touch;max-width:100%;}
```
3. Rename the record filter hooks to match `enhance.js` (it already handles `[data-record-filter]` + `button[data-filter]` with `aria-pressed`), or the filter buttons are dead on this page too.
**Buildability.** Static HTML/CSS only. Re-templating is a codegen change in the profile build scripts; `overflow-x:clip` is a one-line safety net. No backend.
**Source.** The `overflow-x:clip` on the root and the "wrap every table" rule are the canonical fixes in [Defensive CSS](https://defensivecss.dev/tip/input-zoom-safari/)'s scrolling-overflow tips; horizontal page-scroll from unconstrained tables is the textbook mobile-table failure that responsive-table patterns (contain-and-scroll, or reflow-to-cards) exist to solve.

### M2. Search — the flagship feature — is two taps deep on mobile and nearly impossible to dismiss
**Problem (discoverability).** The only search entry point is `<button class="nav__search" data-cmdk-open>` which lives *inside* `.nav__menu` (`index.html` lines 108–110). At ≤900px that whole `<ul>` is the collapsed drawer (`site.css` lines 134–138, `transform:translateY(-120%)`). So on a phone the path to search is: reach the top-left hamburger → open drawer → scroll past 5 hub items → tap "Search". The `⌘K` / `/` shortcuts in `nav.js` (lines 83–88) are keyboard-only and meaningless on touch. There is **no persistent search affordance in the mobile top bar** — for a site selling itself as "the most SEARCHABLE," search is the hardest thing to find on the smallest screen.
**Problem (dismissal).** Once open, the `.cmdk` overlay auto-focuses the input after 20ms (`nav.js` line 17), so the on-screen keyboard covers the lower ~half. Dismissal options are: `Esc` (no key on a phone) or tapping the backdrop *outside the box* (`nav.js` line 81, `e.target === overlay`) — but with the keyboard up, the only tappable backdrop is a thin strip, and the visible affordances are three keyboard-only hints (`↑↓ navigate · ↵ open · esc close`, `index.html` line 121) plus an "Esc" chip. **There is no tap ✕ close button.** A user who opens search and changes their mind is stuck poking at margins.
**Fix.**
1. Promote search to a **persistent icon button in the mobile bar**, always visible next to the hamburger (not inside the drawer). It already exists as a `<button>` — pull `.nav__item--search` out of `.nav__menu` in the shell partial, or add a second always-visible trigger for ≤900px and `display:none` it ≥901px.
2. Add a real close control to `.cmdk__head` (a 44px ✕ button calling `close()`), and swap the keyboard-only footer hints for touch-relevant text on small screens (or hide `.cmdk__foot` under `max-width:640px`).
3. Give the input `font-size:16px` at mobile widths (see M6) and add `enterkeyhint="search"` / `inputmode="search"` so the keyboard shows a "Search" return key.
**Buildability.** Pure markup/CSS + ~6 lines in `nav.js` for the ✕ handler. Crawlable (it's a button, content unaffected). No backend.
**Source.** Every reference command-palette implementation exposes a **click target in addition to** the shortcut precisely because shortcuts don't exist on touch — see the [Command Palette pattern (uxpatterns.dev)](https://uxpatterns.dev/patterns/advanced/command-palette) and [Algolia DocSearch](https://docsearch.algolia.com/), which render a tappable search button as the primary mobile entry and a full-screen modal with an explicit cancel/close control. A persistent search icon in the header is the norm on content apps (IMDb, Letterboxd) for exactly this reason.

### M3. The mobile nav drawer has no scroll lock, no scrim, and no way to dismiss except the toggle
**Problem.** `js/main.js` (lines 11–19) toggles `.nav__menu.is-open` and flips the icon — that's the entire drawer logic. Missing, all of which are baseline expectations on mobile:
- **No body scroll lock.** The page behind the open drawer still scrolls under your finger (ironically, `nav.js` *does* lock the body for ⌘K — the two overlays are inconsistent).
- **No backdrop/scrim.** `.nav__menu` is `position:fixed;inset:60px 0 auto 0` with height = content (`site.css` line 135), so it only covers the top slice of the screen; the rest of the page shows through undimmed, so it doesn't read as a modal layer and there's nothing to tap to dismiss.
- **No tap-outside-to-close, no Escape, no close-on-link-tap.** The only way to close is to find the small hamburger again at top-left. Tap a nav link and the drawer stays open behind the new page load on the next paint.
- **No focus management / focus trap.** Focus isn't moved into the drawer on open or restored on close; a screen-reader/keyboard user on mobile can tab into the page behind it.
**Fix.** In `main.js`, on open: add `document.body.style.overflow='hidden'`; render/insert a `.nav__scrim` element (fixed, semi-opaque) and close on scrim tap; add `keydown` Escape to close; move focus to the first link and restore to the toggle on close. Close the drawer automatically when a nav link is tapped. CSS for the scrim:
```css
.nav__scrim{position:fixed;inset:60px 0 0 0;background:rgba(6,7,9,.6);opacity:0;visibility:hidden;
  transition:opacity var(--dur) var(--ease),visibility var(--dur);z-index:90;}
.nav__scrim.is-open{opacity:1;visibility:visible;}
@media(min-width:901px){.nav__scrim{display:none;}}
```
Reuse the exact body-lock code already in `nav.js` so the two overlays behave the same.
**Buildability.** ~15 lines of vanilla JS + the CSS above. No backend; degrades fine without JS (drawer just stays a static list).
**Source.** Scroll-lock + scrim + dismiss-outside are the defining traits of the overlay/drawer pattern in [NN/g, "Basic Patterns for Mobile Navigation"](https://www.nngroup.com/articles/mobile-navigation-patterns/); the scroll-behind bug and its fix are documented in [Robin Weser, "Scroll Blocking Overlays"](https://weser.io/blog/scroll-blocking-overlays).

### M4. Tapping a hub label opens the submenu instead of navigating — and swallows the hub page
**Problem.** `main.js` (lines 22–34) intercepts clicks on `.nav__link[aria-haspopup]` at ≤900px and calls `e.preventDefault()` to toggle the mega panel. So on a phone, tapping "Wrestlers" / "Events" / "Promotions" **never goes to `/wrestlers/` etc.** — it only expands an accordion. Recovery exists (the panel contains an "All Wrestlers" / "All Events" link), but it's non-obvious, and the disclosure caret (`.nav__link[aria-expanded]::after{content:"▾";font-size:.7em}`, `site.css` line 115) is a tiny 0.7em glyph that doesn't read as "this is a toggle, not a link." Users expect the label to navigate and a separate caret to expand.
Secondary, touch tablets ≥901px: the mega panels are revealed **only** by `:hover`/`:focus-within` (`site.css` line 122), and the JS tap-toggle is gated to ≤900px. On an iPad in portrait (768–1024px) there's no hover, so the dropdowns are simply unreachable by tapping — you only ever get the hub landing page.
**Fix.**
- In the drawer, split the row into a **navigating label** + a **separate 44px disclosure toggle** (button with the caret). The label link goes to the hub; the toggle expands the panel. This is the standard mobile mega-menu accordion.
- Raise the breakpoint that enables the tap-to-open interception (or key it off `(hover:none)` instead of a px width) so touch tablets get tap-expandable panels too:
```js
if (window.matchMedia('(hover:none)').matches) { /* intercept + toggle */ }
```
**Buildability.** Markup change in the nav partial (one extra `<button>` per hub item) + swap the matchMedia query. No backend. Keeps every hub link crawlable (the label stays a real `<a href>`).
**Source.** Split label-vs-caret disclosure and `(hover:none)` gating are the mobile mega-menu recommendations in [NN/g, "Basic Patterns for Mobile Navigation"](https://www.nngroup.com/articles/mobile-navigation-patterns/); hover-only reveal on touch is the classic "dropdowns dead on tablets" anti-pattern.

---

## TIER 2 — Real friction, high ROI

### M5. Touch targets below the 44/48px floor across filters, sub-nav, ⌘K rows, and footer
**Problem.** Multiple interactive controls are ~28–38px tall — under both Apple's 44pt and Material/WCAG's 48px/24px guidance:
- `.subnav-page a` `padding:.4em .7em` (~28px) in a horizontal scroller (`site.css` line 542).
- `.rt-filters button` `padding:.4em .9em` (~30px) (`site.css` line 554); Kane's `.rf-btn` is fully unstyled = default tiny button.
- `.cmdk__row` `padding:.6em .7em` (~36–40px) — result rows you tap on a phone (`site.css` line 894).
- `.nav__search` `padding:.5em .8em` (~30px) (`site.css` line 873).
- Home + Kane footers are inline text links separated by "·" (`index.html` line 285) — tiny, crammed tap targets, and note this minimal footer is a *different component* from the DS `.footer-grid`, so mobile footer navigation is both inconsistent and hard to hit.
**Fix.** Establish a min tap size for interactive elements at coarse pointers:
```css
@media (pointer:coarse){
  .subnav-page a,.rt-filters button,.rf-btn,.nav__search,.cmdk__row,.related-links__a{min-height:44px;}
  .cmdk__row{padding-block:.85em;}
}
```
Add vertical padding rather than only height so the label stays centered. Rebuild the mobile footer on `.footer-grid` (stacked columns) so links become full-width rows.
**Buildability.** CSS-only for the sizing; footer is a markup swap to an existing component. No backend.
**Source.** 44×44pt is Apple HIG; 48×48dp is Material; WCAG 2.5.8 sets a 24px minimum with spacing — summarized with the "add padding, not just height" guidance in [LogRocket, "All accessible touch target sizes"](https://blog.logrocket.com/ux-design/all-accessible-touch-target-sizes/) and the [WCAG 2.5.8 implementation guide](https://www.allaccessible.org/blog/wcag-258-target-size-minimum-implementation-guide).

### M6. Conversion inputs are <16px → iOS Safari auto-zooms on focus (jank on the primary funnel field)
**Problem.** `.input` uses `font-size:var(--fs-400)` = `clamp(0.94rem,…,1.05rem)`; at the mobile floor that's **~15px** (`site.css` line 331). iOS Safari auto-zooms the page whenever a focused input's text is under 16px, then doesn't fully zoom back out — so focusing the **waitlist email field** (the top-of-funnel capture on the home page, `index.html` line 252) triggers a disorienting zoom on exactly the interaction the whole site is funneling toward. The `.cmdk__input` is safe (`fs-500` ≥18px), which makes the inconsistency easy to miss.
**Fix.**
```css
@media (max-width:640px){ .input,select,textarea{font-size:16px;} }
```
(Do not use `maximum-scale=1` / `user-scalable=no` to suppress it — that breaks pinch-zoom accessibility.)
**Buildability.** One CSS rule. No backend.
**Source.** [CSS-Tricks, "16px or larger text prevents iOS form zoom"](https://css-tricks.com/16px-or-larger-text-prevents-ios-form-zoom/) and [Defensive CSS, "Input zoom on iOS Safari"](https://defensivecss.dev/tip/input-zoom-safari/).

### M7. Hero uses `vh`, not `dvh` — it jumps and over-tall on mobile with dynamic toolbars
**Problem.** `.hero-bb{min-height:clamp(600px,90vh,940px)}` (`site.css` line 418). On mobile, `vh` is the *large* viewport (toolbar hidden), so a `90vh` hero is taller than what's actually visible and its height jumps when the URL bar shows/hides on scroll. A 600px floor also means the phone's first screen is almost entirely hero, pushing the stats bar, marquee, and five-star rail below a tall fold. The drawer already uses `100dvh` correctly (`site.css` line 136) — the hero should too.
**Fix.**
```css
.hero-bb{min-height:clamp(480px,80svh,940px);}   /* svh = small viewport; stable, no jump */
```
Lower the floor and the vh factor for phones so the marquee/rail peek above the fold and invite scroll.
**Buildability.** One line; `svh`/`dvh` are broadly supported in 2026 with the `clamp` px floor as fallback. No backend.
**Source.** Dynamic viewport units (`svh`/`lvh`/`dvh`) are the standard fix for the mobile "100vh is too tall / jumps" problem; consistent with the drawer's own use of `dvh` here.

### M8. `.tale` never reflows — three columns crushed at 360px
**Problem.** `.tale{grid-template-columns:1fr auto 1fr}` with no mobile breakpoint (`site.css` lines 235–239). On a Tale of the Tape at 360px, two wrestler names at `fs-600` plus a `fs-700` "VS" are forced into ~150px side columns — names wrap awkwardly or overflow their cell. Compare `.champ-rows`, which *does* collapse to one column at `max-width:560px` (`site.css` line 601); `.tale` should follow the same discipline.
**Fix.**
```css
@media (max-width:520px){
  .tale{grid-template-columns:1fr;}
  .tale .vs{justify-self:center;padding-block:var(--sp-2);}
}
```
**Buildability.** CSS-only. No backend.
**Source.** Matches the site's own established reflow pattern (`.champ-rows`, `.form__row`) and general responsive-table/comparison reflow guidance.

### M9. Two sticky layers eat ~16% of a phone screen; heavy persistent chrome
**Problem.** `.site-header` sticky `min-height:60px` (`site.css` line 99) + `.subnav-page` sticky `top:60px` (~40px, `site.css` line 538) = ~100px of permanent chrome on a ~640px-tall viewport. `[id]{scroll-margin-top:112px}` (line 614) confirms the stack. On record/profile pages that use the subnav, a sixth of the screen is always chrome.
**Fix.** On scroll-down, hide the sub-nav (or the header) and reveal on scroll-up — an auto-hiding header. `enhance.js` already listens to scroll for `.is-stuck` (lines 122–128); extend it to track scroll direction and toggle a `.is-hidden` transform on `.subnav-page` (translateY(-100%)) below a small threshold.
**Buildability.** ~10 lines added to the existing scroll handler + a CSS transition class. No backend.
**Source.** Auto-hide-on-scroll to reclaim vertical space is a well-established mobile pattern (Medium, Chrome Android's own toolbar); reduces persistent chrome without removing access.

---

## TIER 3 — Polish / smaller wins

- **M10. ⌘K results max-height vs keyboard.** `.cmdk__results{max-height:52vh}` (`site.css` line 893) plus `12vh` top padding plus the input can exceed the space above the on-screen keyboard; lower rows sit behind the keyboard. Use `max-height:min(52vh,50dvh)` and reduce top padding to `8vh` under `max-width:640px`. CSS-only.
- **M11. Hero CTAs aren't full-width taps.** In `.cluster`, `.btn` stays inline-flex, so "Join Wrestle Lore Insider — Free" (`index.html` line 136) is a left-aligned pill with a small hit area and can wrap its own label. Under `max-width:520px`, make hero/CTA-band buttons `width:100%` for big thumb targets. CSS-only.
- **M12. `.facts` stays 2-up on all widths.** `grid-template-columns:1fr 1fr` (`site.css` line 279) with no mobile collapse; long values (e.g., Kane's "Also known as" list) get very narrow columns at 360px. Collapse to 1 column under ~420px. (Also moot on Kane until M1 puts it on `.facts`.) CSS-only.
- **M13. Marquee is 42s and unpausable by touch.** `.marquee:hover` pause (`site.css` line 464) never fires on touch, so the ticker can't be stopped to read/tap an item on a phone; reduced-motion turns it into a manual `overflow-x:auto` scroller (good), so consider making the swipeable scroller the *default* on `(hover:none)`. CSS-only.
- **M14. Duplicate `id="cmdk"` risk.** Every page stamps the `.cmdk` dialog and the shell; fine as long as one per page, but the profile pages load `main.js` **non-deferred** (`kane` line 207) while DS pages use `defer`/order differs — keep script order/`defer` identical across the stamped shell so the mobile toggle and ⌘K bind consistently. Markup consistency, no backend.

---

## Priority order for the build
1. **M1** (unstyled profile + page-level horizontal overflow) — systemic, on the template.
2. **M2** (surface + make dismissable mobile search) — flagship feature, funnel-critical.
3. **M3** (finish the drawer: scroll-lock + scrim + dismiss + focus) — every session touches it.
4. **M6** (16px inputs) and **M4** (hub tap navigation) — cheap, high-frequency.
5. Remainder (M5, M7–M14) — CSS-only sweeps, batchable.

Every fix above ships as static HTML/CSS/vanilla-JS and preserves crawlability. No backend required for anything; M1 and the footer swap (M5) are the only items needing markup/codegen changes rather than pure CSS.

### Sources
- [NN/g — Basic Patterns for Mobile Navigation](https://www.nngroup.com/articles/mobile-navigation-patterns/)
- [Robin Weser — Scroll Blocking Overlays](https://weser.io/blog/scroll-blocking-overlays)
- [Command Palette pattern — uxpatterns.dev](https://uxpatterns.dev/patterns/advanced/command-palette)
- [Algolia DocSearch](https://docsearch.algolia.com/)
- [CSS-Tricks — 16px or larger text prevents iOS form zoom](https://css-tricks.com/16px-or-larger-text-prevents-ios-form-zoom/)
- [Defensive CSS — Input zoom on iOS Safari](https://defensivecss.dev/tip/input-zoom-safari/)
- [LogRocket — All accessible touch target sizes](https://blog.logrocket.com/ux-design/all-accessible-touch-target-sizes/)
- [WCAG 2.5.8 Target Size (Minimum) implementation guide](https://www.allaccessible.org/blog/wcag-258-target-size-minimum-implementation-guide)
- [Smashing Magazine — The Thumb Zone: Designing for Mobile Users](https://www.smashingmagazine.com/2016/09/the-thumb-zone-designing-for-mobile-users/)
