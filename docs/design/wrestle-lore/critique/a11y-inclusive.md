# Wrestle Lore — Accessibility Critique & Enhancement Spec (WCAG 2.2 AA)

Adversarial audit. Role: accessibility auditor. Scope reviewed as real files:
`index.html`, `css/site.css` (full, 909 lines), `js/nav.js` (⌘K palette), `js/main.js`,
`js/enhance.js`, `wrestlers/kane/index.html` (labelled "gold-standard"),
`events/index.html`, `moments/mankind-hell-in-a-cell-fall-1998/index.html`.

Verdict up front: the site is **better than average** on a few things people usually
botch — a real skip link on most pages, `prefers-reduced-motion` handling that is
genuinely thorough, no-JS content visibility gated behind `.js`, labelled icon buttons,
`:focus-visible` styling. But it ships **at least three keyboard/AT-blocking defects**
(the ⌘K palette, the desktop mega-nav's lying `aria-expanded`, and a completely
different "gold-standard" profile template that drops the skip link, doubles the banner
landmark, and loads a dead filter). Contrast has two hard fails hiding in the color
tokens. Below, every item cites the file/selector, gives buildable static fixes, and
names the pattern source I checked.

Contrast numbers below are computed WCAG relative-luminance ratios against the actual
hex tokens in `css/site.css`.

---

## P0 — Blocking defects (keyboard / screen-reader users cannot use the feature)

### A1. ⌘K command palette is not an accessible combobox: no focus trap, no focus return, dead `role="listbox"`
**Problem.** `js/nav.js` + the `#cmdk` markup (`index.html` lines 115–122, repeated on
every page). The dialog is `role="dialog" aria-modal="true"`, but:
- **No focus trap.** Nothing keeps Tab inside the dialog. Tab moves focus to the page
  behind it, which is still fully in the accessibility tree (only `body{overflow:hidden}`
  is set — background is not `inert`/`aria-hidden`). `aria-modal="true"` is a *promise*
  to AT that is being broken. (WCAG 2.4.3 Focus Order; 1.3.1.)
- **No focus restoration.** `close()` (nav.js line 19) never returns focus to the trigger
  (`.nav__search`). After Escape, focus is lost to `<body>`. (WCAG 2.4.3.)
- **Escape only works from the input.** The `keydown` Escape handler is bound to
  `input` (nav.js line 75). Click a result region, or Tab away, and Escape no longer
  closes it. (WCAG 2.1.2 — the reverse case: user is stranded.)
- **The result list is invisible to screen readers.** `<ul role="listbox">` with
  `<li role="option" class="is-active">` (nav.js line 54) but the input is a plain
  `type="text"`, **not** `role="combobox"`, has **no** `aria-controls`,
  **no** `aria-activedescendant`, and the active option has **no** `id` and
  **no** `aria-selected="true"` — only a `.is-active` class for visuals. Arrow keys
  move a highlight sighted users see and AT users get nothing. (WCAG 4.1.2 Name/Role/Value.)

**Fix (all static, no backend).** Convert to the APG *combobox with list autocomplete*
contract:
```html
<input class="cmdk__input" type="text" role="combobox"
       aria-expanded="false" aria-controls="cmdk-results"
       aria-activedescendant="" aria-autocomplete="list" aria-label="Search">
<ul class="cmdk__results" id="cmdk-results" role="listbox" aria-label="Search results"></ul>
```
In `nav.js`:
- Give each row `id="cmdk-opt-"+i`, and on `move()`/`render()` set
  `input.setAttribute('aria-activedescendant', activeId)` and
  `el.setAttribute('aria-selected', i===active)`. Toggle `aria-expanded` on the input
  when results are present.
- On `open()`: store `var opener = document.activeElement;`. On `close()`:
  `if (opener) opener.focus();`.
- Add a focus trap: on the overlay, `keydown` → if `Tab`, compute first/last focusable
  and wrap; move the Escape handler from `input` to the overlay/`document` (scoped to
  when `.is-open`).
- Set the rest of the page inert while open:
  `document.getElementById('main').inert = true;` (and header/footer), reverse on close.
  `inert` is baseline-supported; keep the `overflow:hidden` too.
**Buildability.** Pure JS/HTML edits to one shared file + the shell markup; no build step.
**Source.** [W3C APG — Editable Combobox with List Autocomplete](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/combobox-autocomplete-list/)
(defines `aria-activedescendant`/`aria-selected`/focus return); MDN
[`combobox` role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/combobox_role).

### A2. Desktop mega-nav reports `aria-expanded="false"` permanently — it is lying to AT
**Problem.** `index.html` lines 52/68/75/88/97 (and every shell copy): each
`.nav__link` has `aria-haspopup="true" aria-expanded="false"`. On desktop the panel opens
purely via CSS `:hover`/`:focus-within` (`site.css` line 122); `aria-expanded` is **only**
ever updated inside the mobile (`max-width:900px`) click branch of `main.js` (lines 22–34).
So on desktop a screen-reader user hears "Wrestlers, has popup, collapsed" and the state
never changes even though a panel is visibly open. There is also **no Escape-to-close** and
no way to dismiss the panel with the keyboard except tabbing entirely past it. (WCAG 4.1.2;
2.1.1 Keyboard.)

**Fix (static).** Treat each top item as a **link + disclosure** (Roselli/GOV.UK pattern),
not a fake menu:
- Keep the `.nav__link` as the real link to the hub, and add a *separate* small
  disclosure `<button aria-expanded="false" aria-controls="mega-wrestlers">▾</button>`
  that toggles the panel and owns the state. This also fixes the mobile problem in A3.
- Drive open state from `aria-expanded` (JS + CSS `[aria-expanded="true"] + .mega`)
  instead of `:hover`, or at minimum sync `aria-expanded` on `focusin`/`focusout`/`Escape`
  for the `.nav__item`. Add a `document` `keydown` for `Escape` that closes any open
  `.mega`, returns focus to its toggle.
- If you keep hover-open for pointer users, still update `aria-expanded` from JS on the
  `mouseenter`/`mouseleave` so the DOM state matches reality.
**Buildability.** Markup + `main.js`/`site.css` only.
**Source.** [Adrian Roselli — Link + Disclosure Widget Navigation](http://adrianroselli.com/2019/06/link-disclosure-widget-navigation.html);
[Level Access — Accessible mega menus](https://www.levelaccess.com/blog/challenges-mega-menus-standard-menus-make-accessible/).

### A3. On mobile, the top hub links are hijacked — and there is no `Escape`/`aria-controls`
**Problem.** `main.js` lines 22–34: at `≤900px`, clicking `.nav__link[aria-haspopup]`
calls `e.preventDefault()` and toggles the panel. Result: on a phone you **cannot reach
`/wrestlers/`, `/matches/`, `/events/` landing pages by tapping the top item** — only the
"All Wrestlers" child link inside the panel gets you there. The toggling link also has no
`aria-controls` pointing at its `.mega` (which has no `id`). (WCAG 2.1.1; 4.1.2; and a
plain content-reachability failure.)
**Fix.** Adopt the A2 split: link stays a link (navigates on tap), the adjacent chevron
`<button>` opens the submenu. Give each `.mega` an `id` and wire `aria-controls`.
**Buildability.** Markup + `main.js`.
**Source.** Same as A2 (the link-vs-disclosure split is exactly the fix for this).

### A4. The "gold-standard" Kane profile is a *different, undocumented template* that regresses core a11y
**Problem.** `wrestlers/kane/index.html` does **not** use the design system. It uses
classes that **do not exist in `site.css`** (`.athlete-hero`, `.hero-inner`,
`.content-grid`, `.bio-col`, `.stats-col`, `.stat-card`, `.record-table`, `.rf-btn`,
`.sig-grid`, `.persona-card`, `.faq-block`, `.tl-year`, `.mb-label`, `.res-badge`).
Concrete a11y regressions vs. the homepage/moments template:
1. **No skip link.** `index.html` and the moments page both start with
   `<a class="skip-link" href="#main">` — Kane does **not** (compare Kane line 22 `<body>`
   straight into `<header>`). Keyboard users must tab through the entire mega-nav on every
   profile — and profiles are ~89 of ~170 pages, i.e. the majority of the site. (WCAG 2.4.1
   Bypass Blocks — fail.)
2. **Duplicate `banner` landmark.** Kane has `<header class="site-header">` (line 23) **and**
   a second `<header class="athlete-hero">` (line 96) that is a direct child of `<body>`.
   Two `<header>`s scoped to `body` = two `banner` landmarks. AT landmark navigation now
   lists two "banner" regions. (WCAG 1.3.1.) Make the hero a `<section aria-labelledby>`.
3. **Dead filter control.** The record filter buttons (`.rf-btn`, lines 185–189) are wired
   to `enhance.js`'s `[data-record-filter]` handler — but **Kane never loads `enhance.js`**
   (scripts, lines 207–209: only `main.js`, `search-index.js`, `nav.js`). So the filter
   buttons do nothing: no `aria-pressed`, no visible pressed state (no `.rf-btn` CSS
   exists), no result count. A control that looks operable but isn't is a 4.1.2 + 2.1.1
   failure. Either load `enhance.js` or delete the buttons.
4. **Data table has no `scope`.** `.record-table` `<th>` cells (line 192) lack
   `scope="col"`; the win/loss `<th>R</th>` header is opaque. Add `scope="col"` to every
   header cell and give the table a `<caption>`. (WCAG 1.3.1.)
5. **Win/loss sparkline is color-only.** `.wl-strip` (line 104) renders results as empty
   `<i></i>` (win, green) vs `<i class="l"></i>` (loss, red) — the *only* differentiator is
   hue. The wrapping `aria-label="Win/loss sparkline"` doesn't expose the sequence, and
   red/green is the worst possible pairing for the most common color-vision deficiency.
   (WCAG 1.4.1 Use of Color; 1.1.1.) Add per-item `<i aria-hidden="true">` plus a
   visually-hidden textual summary ("Last 6: W L L L W W"), and add a shape/letter, not
   just color.
**Fix.** Re-stamp profiles from the *same shell* as `index.html`/`moments` (skip link +
single banner + full script set), or, faster: (a) prepend the skip link, (b) change
`athlete-hero` `<header>`→`<section>`, (c) add `enhance.js` to the script block, (d) add
`scope="col"` + `<caption>`, (e) give the sparkline text. All are string edits, no build.
**Buildability.** Template/markup edits; ideally fold profiles into the canonical shell so
this can't drift again (the whole site is "stamped" per the brief — stamp *one* correct
shell).
**Source.** [W3C — Bypass Blocks / skip link](https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks.html);
[MDN — one banner landmark per page](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header).

---

## P1 — Serious (measurable failures, degraded experience)

### A5. Two color tokens fail contrast; `--c-text-dim` has no headroom at 12–14px
**Problem (computed against the real tokens).**
- **Loss badge fails.** `.res-l{color:#fff;background:var(--c-loss)}` (`site.css` line 562)
  → white on `--c-loss #e05263` = **3.8:1**, below the 4.5 needed for the "W"/"L" letter
  badges (normal text). Also used for the round loss chips (`site.css` line 838 context).
- **Dim text is on the edge.** After the "lift dim text to ~AA" override
  (`site.css` line 612, `--c-text-dim:#828a96`): on `--c-bg #0a0b0d` = 5.65:1 (pass), but
  on `--c-bg-elev-2 #1a1d23` = **4.84:1** and on `--c-bg-elev-3 #23272f` = **4.30:1 (FAIL)**.
  `fs-300` clamps down to `0.78rem` (~12.5px) — this is *normal* text for WCAG, so 4.5 is
  required. Dim-on-elevated appears in `.watch-item h4`, `.meta-chip`-adjacent labels,
  `.scroll-hint`, table sub-text, `.tier li.no`, breadcrumb/footer. Many are right at or
  under the line.
**Fix.**
- Loss: darken the surface pairing — use `--c-loss` as an *outline/left-bar* with light
  text on the dark card (as `.res-list .res-w` already does for wins, line 838), or set the
  badge text to `#120406` on the red (dark-on-light) which clears 4.5 comfortably; or
  deepen to `--c-loss:#c23a4a` and keep white (≈4.8:1).
- Dim: raise the token to ~`#9199a6` (≈5.9:1 on elev-2, ≈5.3:1 on elev-3) or forbid
  `--c-text-dim` on `elev-2`/`elev-3` surfaces and use `--c-text-muted` there.
**Buildability.** Two token edits in `site.css`.
**Source.** [Make Things Accessible — WCAG 2.2 AA contrast](https://www.makethingsaccessible.com/guides/contrast-requirements-for-wcag-2-2-level-aa/)
(1.4.3 = 4.5:1 normal / 3:1 large).

### A6. Text inputs remove the focus outline and rely on a 1px border color change — fails 2.4.11
**Problem.** `.input:focus{border-color:var(--c-gold);outline:none}` (`site.css` line 332).
`:focus` (not `:focus-visible`) with higher specificity than the global
`:focus-visible{outline:2px…}` (line 76) means keyboard focus on the email/search inputs
shows **only** a 1px border recolor (`--c-line-strong #3a414c` → `--c-gold #d4af37`). WCAG
2.2 adds **2.4.11 Focus Appearance (AA)**: the indicator must be at least a 2px-thick
perimeter (or equivalent area) *and* ≥3:1 against both the focused and unfocused states. A
1px recolor fails the area minimum. (Also weak for 2.4.7.)
**Fix.** Keep the gold border but restore a real ring:
```css
.input:focus-visible{border-color:var(--c-gold);outline:2px solid var(--c-focus);outline-offset:2px;}
.input:focus:not(:focus-visible){border-color:var(--c-gold);} /* mouse: subtle */
```
**Buildability.** One CSS rule.
**Source.** [TestParty — meeting 2.4.11 Focus Appearance](https://testparty.ai/blog/wcag-focus-appearance-minimum);
[WebAIM — WCAG 2.2 overview](https://webaim.org/blog/wcag-2-2-overview-and-feedback/).

### A7. Gradient-clipped text disappears in Windows High Contrast / `forced-colors`
**Problem.** Multiple headline treatments use
`-webkit-background-clip:text;background-clip:text;color:transparent` — hero title accent
(`site.css` line 439), event `h1` (line 776), `.rec-stat .n` (line 624), `.ev-hero h1`.
In `forced-colors: active` the OS strips background images and forces text color; with
`color:transparent` the text can render **transparent = invisible**. The homepage `<h1>`
accent word "EVERY LEGEND" and every event/record headline can vanish. (WCAG 1.4.3/1.4.12;
forced-colors best practice.) There is **no** `@media (forced-colors: active)` block in the
909-line stylesheet at all.
**Fix.**
```css
@media (forced-colors: active){
  .hero-bb__title .accent,.ev-hero h1,.ev-hero h1 .accent,.rec-stat .n,.stats-bar .s-num{
    -webkit-text-fill-color:CanvasText;color:CanvasText;background:none;filter:none;}
  .btn,.chip,.meta-chip{border:1px solid;}         /* restore borders lost to forced colors */
  .card,.tile,.mega{border:1px solid CanvasText;}
}
```
**Buildability.** One additive media block.
**Source.** [Adrian Roselli — WHCM / forced-colors](http://adrianroselli.com/2021/02/whcm-and-system-colors.html);
[MDN — `forced-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors).

### A8. Waitlist success is a silent status change — screen-reader users get no confirmation
**Problem.** `main.js` lines 120–137: on submit, the form is hidden (`.hide`) and
`.form-success` gets `.is-visible` (`site.css` line 336, `display:none`→`block`). No
`aria-live`, no focus move. A screen-reader user submits and hears nothing; worse, focus is
now on a hidden `<button>` inside a `display:none` form. (WCAG 4.1.3 Status Messages, AA;
2.4.3.) This is the *membership funnel* — the exact conversion moment the brief cares about.
**Fix.** Add `role="status" aria-live="polite"` to `.form-success` (`index.html` line 256),
and after revealing it, move focus to it (`success.setAttribute('tabindex','-1');
success.focus();`).
**Buildability.** One attribute + two JS lines.
**Source.** [W3C — Status Messages (4.1.3)](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html).

### A9. Duplicated marquee content is read twice by AT
**Problem.** `index.html` lines 170–188: the five-star ticker duplicates all seven items
"for seamless loop" but the second set is **not** hidden from AT. A screen reader announces
14 items (7 repeated). The wrapper `aria-label` doesn't help. (WCAG 1.3.1 — redundant
content.) Also the whole marquee is presentational; its links... there are none, so it is
pure decoration that still gets read.
**Fix.** Mark the entire ticker `aria-hidden="true"` (it duplicates the "Five-Star
Classics" rail below it, which *is* linked and reachable), or at minimum put
`aria-hidden="true"` on the duplicate `.marquee__item` set.
**Buildability.** One attribute.
**Source.** [W3C — 1.3.1 Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html).

### A10. Record-filter buttons never expose pressed state as a status; no result announcement
**Problem.** `enhance.js` lines 89–95 toggle `aria-pressed` on the desktop record filter
(good), but the resulting count (`countEl`, line 87) is a bare number with no `aria-live`,
so filtering to "Wins (3)" is silent to AT. The homepage/promotion filters in `main.js`
(lines 64–98) update a counter (`counter.textContent = shown`) with **no `aria-pressed`
at all** on `[data-promo]` buttons and no live region. (WCAG 4.1.3; 4.1.2.)
**Fix.** Add `aria-pressed` to `[data-promo]` buttons (toggle in the `main.js` handler),
and wrap the visible count in `<span role="status" aria-live="polite">`.
**Buildability.** JS + markup.
**Source.** [W3C — Status Messages (4.1.3)](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html).

---

## P2 — Should fix (2.2-specific + polish)

### A11. Target sizes below 24×24 (WCAG 2.2 AA 2.5.8)
**Problem.** New in 2.2. Undersized/too-tightly-spaced targets:
- Breadcrumb links `.crumbs a` (`site.css` 758) — ~14px tall inline, gaps `.5em`.
- Footer inline links (`index.html` 285, `About · Methodology · Insider`) — tiny text,
  `·`-separated, spacing well under 24px.
- `.link-more` (site.css 403), `.subnav-page a` (`.4em .7em`, line 542), `.rt-filters
  button` (`.4em .9em`, line 553) — borderline ~24px tall.
Breadcrumb/inline-in-sentence links can use the 2.5.8 *inline exception*, but the footer
row and `.link-more`/subnav pills do not read as inline prose.
**Fix.** Give the footer nav `display:flex;gap:var(--sp-4)` and each link `padding:.5em`
(or `min-height:24px;display:inline-flex;align-items:center`). Bump `.subnav-page a` /
`.rt-filters button` vertical padding so computed height ≥24px.
**Buildability.** CSS only.
**Source.** [Vispero — new SC in WCAG 2.2 (2.5.8)](https://vispero.com/resources/new-success-criteria-in-wcag22/).

### A12. `role="listbox"` empty-state and no-JS: results container should be a live region
**Problem.** `nav.js` `render()` writes "No matches for …" into the listbox (line 50) but
nothing announces it, and while typing, the count of results changing is silent. For a
search UI this is the core feedback. (WCAG 4.1.3.)
**Fix.** Add `aria-live="polite"` to a small status node in `.cmdk__head` (e.g.
`<span class="sr-only" aria-live="polite">`) and write "N results"/"No matches" there on
each `render()`. Keep the listbox for `aria-activedescendant`.
**Buildability.** Markup + a line in `nav.js`.
**Source.** APG combobox (same as A1).

### A13. Ambiguous rating text for AT ("5.0" with no unit)
**Problem.** `.rating__stars` is `aria-hidden` (`index.html` line 152) and the visible
number is just `5.0` (`.rating__num`) / `.tile__rating` "5.0" (lines 202–207). A screen
reader reads "five point zero" with no context. (WCAG 1.1.1 / 1.3.1 clarity.)
**Fix.** Add a visually-hidden unit: `<span class="rating__num">5.0<span class="sr-only">
out of 5 stars</span></span>`, and give `.tile__rating` an `aria-label="Rated 5.0 out of
5"`. (`.sr-only` already exists, `site.css` line 613.)
**Buildability.** Markup.
**Source.** [W3C — 1.1.1 Non-text Content](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html).

### A14. `nav__spacer` uses `aria-hidden` on a focusable-sibling context; and mega `<h3>` are not associated
**Problem.** (a) `<li class="nav__spacer" aria-hidden="true">` (`index.html` line 107) is a
layout `<li>` inside the `<ul>` — harmless but it injects an `aria-hidden` list item into
the nav list; cleaner to make it CSS-only (`.nav__menu::before`/flex) so the list contains
only real items. (b) The mega panels use `<h3>` section headers (e.g. "By Promotion") and
some are `&nbsp;` placeholders (`index.html` lines 58, 84, 93) — an `<h3>` whose text is a
non-breaking space is an **empty heading** to AT. (WCAG 1.3.1; 2.4.6 Headings.)
**Fix.** Replace `&nbsp;` headings with real labels or drop the `<h3>` and use a
visually-hidden continuation, e.g. `<h3 class="sr-only">More promotions</h3>`.
**Buildability.** Markup.
**Source.** [W3C — 2.4.6 Headings and Labels](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html).

### A15. New-tab links don't warn; external links lack an accessible cue
**Problem.** `moments/…` line 132 and `events/index.html` 117 use
`target="_blank" rel="noopener"` (good `rel`) but no textual "(opens in new tab)" cue, and
the home hero facade `onclick=window.open(...)` (`index.html` 145) opens a *YouTube search
page* in a new tab from a control labelled "Watch …". (WCAG 3.2.5 / 2.4.4 link purpose.)
**Fix.** Append `<span class="sr-only"> (opens in new tab)</span>` to external/new-tab
links; relabel the hero facade to match what it does ("Search this match on YouTube").
**Buildability.** Markup.
**Source.** [W3C — 3.2.5 Change on Request](https://www.w3.org/WAI/WCAG22/Understanding/change-on-request.html).

---

## What is already good (keep it)
- **Reduced motion is thorough.** Global kill-switch (`site.css` 61–63) plus per-effect
  guards: hero drift (428), marquee (470), reveal (398), method bars (632), gold-button
  shine (519), and JS bail-outs in `enhance.js` (line 8) and count-up (line 18). This is
  above the norm — preserve it when adding features.
- **No-JS resilience.** `[data-reveal]` is gated behind `.js` (site.css 394) so content is
  visible without JavaScript; real anchor links back every ⌘K action.
- **Skip link + `scroll-margin-top`** on the canonical shell (site.css 78, 614).
- **Labelled icon controls** (`.nav__toggle`, `.nav__search`, `.facade` all have
  `aria-label`), and `aria-hidden` on decorative layers (hero bg/grain, `▶`, `▾`).
- **Tabs widget** in `enhance.js` (99–120) is a correct APG tab pattern (roving tabindex,
  arrow keys, `aria-selected`, `hidden` panels) — reuse this as the model for A1/A2.

---

## Priority build order
1. **A1** ⌘K combobox (focus trap + return + `aria-activedescendant`) — global, one file.
2. **A4** Re-stamp profiles on the canonical shell (skip link, single banner, load
   `enhance.js`, `scope`, sparkline text) — affects the ~89 profile pages, the majority.
3. **A2 / A3** Mega-nav link+disclosure split (fixes desktop lying state *and* mobile hub
   reachability in one change).
4. **A5 / A6 / A7** Token contrast fixes + input focus ring + `forced-colors` block —
   three small CSS edits, site-wide.
5. **A8 / A10 / A12** Live-region status messages (funnel + filters + search).
6. **A9 / A11 / A13 / A14 / A15** Markup polish.

All fixes are static-site compatible; none require a backend. The only cross-cutting
recommendation is to **collapse the profile template into the same shell** used by
`index.html`/`moments` so the A4-class regressions cannot silently reappear across 170 pages.
