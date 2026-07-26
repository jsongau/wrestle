# Wrestle Lore — Sticky Engagement Rails (Left Rail + Bottom Rail)

Sticky-rails UX spec for the wrestler PROFILE page (flagship, e.g. `/wrestlers/kane/`). Covers two of
the three engagement surfaces: (1) the **STICKY LEFT RAIL** (in-page jump-nav + scroll-spy + quick
actions) and (2) the **STICKY BOTTOM RAIL** ("Keep going" horizontal rail of related wrestlers /
rivals / events). The BOTTOM-RIGHT FLOATER is a sibling surface owned by another role and is only
referenced here for stacking/z-index coordination (§7).

- Date: 2026-07-26. Author: sticky-rails UX design.
- Consumes, does not re-derive: `07-addictive-browsing.md` (the post-content engagement stack,
  `.rail` component, Keep-going block, no-storage rules), `04-subnav-taxonomy.md` (axis color
  tokens, promotion accents), `08-visual-color-system.md` (Broadcast Bold: Anton/Oswald/Inter, gold
  `#d4af37` + red, per-promotion accents), `05-search-discovery.md` (⌘K).

## 0. Hard constraints (inherited, non-negotiable)

- **Static, no build.** All markup for the rails is either already in the page body (links) or
  injected at runtime by one shared script (`js/enhance.js`, already loaded on every page).
- **Crawlability is untouched.** Every destination link the rails point to **already exists as a raw
  `<a href>` in the page body** (bio prose, championships list, "Rivals", "Same promotion", Keep-going
  block). The rails are a *re-presentation* of existing links, not the only path to them. If JS never
  runs, the crawler and a no-JS user still reach every target through the body copy. The rails add
  **zero** new canonical edges that don't also exist in-body.
- **No browser storage** (no localStorage/sessionStorage/cookies) except the one dismissal flag in
  §5.6, which is explicitly `FLAGGED` and degrades safely if absent (in-memory only by default).
- Root-absolute paths, one stylesheet (`css/site.css`), vanilla JS, `data-wl-*` hooks.
- Anti-AI copy standard: no decorative arrows in labels, no em-dash sentence separators, no banned
  marketing words, specific wrestling nouns ("Rivals", "Signature matches", not "Explore more").

## 1. Why these two surfaces (division of labor)

- The **left rail is orientation**: it answers "where am I in this page and what else can I do right
  now" without scrolling back to the top. It is a *within-page* instrument (jump-nav + spy) plus a
  small set of *leave-this-page* escape hatches (random, rivals, same promotion).
- The **bottom rail is momentum**: it answers "what do I click next" the instant a user reaches the
  end of a section, pulling from the page's own cross-links so every profile becomes a rabbit hole.
- Together they bracket the reading column: vertical wayfinding on the left, horizontal "next" along
  the bottom. Neither overlaps the body content on desktop; both collapse to non-intrusive forms on
  mobile (§ each).

---

# 2. STICKY LEFT RAIL

## 2.1 What it contains (top to bottom)

1. **Section jump-nav** — one link per `<h2>` on the page. On a wrestler profile the live sections
   are: Biography, Championships & Titles, Personas & Characters, Career Timeline, Signature Matches,
   FAQ, Match Record (plus injected engagement sections: Related rails, Keep going). Order mirrors
   document order exactly.
2. **Scroll-spy active state** — the link for the section currently in view is highlighted (gold left
   border + bold Oswald label). Exactly one active at a time.
3. **Quick actions** (3–4, visually separated by a hairline divider):
   - **Random wrestler** — links to `/wrestlers/` with a JS-upgraded click that jumps to a random
     roster slug (see §2.6); the raw href is the roster index so it works with no JS and is crawlable.
   - **Rivals** — anchors to the in-page "Rivals / Signature rivalries" content (`#rivals`), or if the
     bottom rail is present, opens/scrolls it. Falls back to `/rivalries/`.
   - **Same promotion** — links to the wrestler's primary promotion hub (e.g. `/promotions/wwe/`),
     read from the page's own promotion badge/front-matter mirror.
   - **Back to top** — appears only after the user scrolls past the first viewport.

## 2.2 Exact behavior

- **Derivation, not authoring.** The shared script queries `main h2` in document order. For each, it
  ensures an `id` (slugified from the heading text if the author didn't set one, e.g. "Championships &
  Titles" -> `championships-titles`), then builds `<li><a href="#id">Label</a></li>`. This means the
  rail needs zero per-page maintenance and can never drift from the actual sections.
- **Scroll-spy** uses a single `IntersectionObserver` with `rootMargin: "-45% 0px -50% 0px"` so a
  section becomes "active" when its heading crosses roughly the vertical middle of the viewport. The
  observer toggles `aria-current="true"` + `.is-active` on the matching rail link. A short guard
  suppresses spy updates for ~600ms after a click-to-scroll so the clicked target wins immediately
  (the classic scroll-spy "fights the click" bug called out in the Bootstrap/sticky-navbar writeups).
- **Smooth scroll** on jump-nav click via CSS `scroll-behavior: smooth` on `:root`, gated by
  `@media (prefers-reduced-motion: no-preference)`. `scroll-margin-top` on every `h2`/section equals
  the site header height so the heading is not hidden under the sticky top bar after a jump.
- **Reveal timing.** The rail is present in DOM but visually hidden until the user scrolls past the
  hero (first ~1 viewport), then fades in (150ms). Rationale: at the very top the jump-nav is
  redundant with the visible hero, and revealing on first scroll matches the NN/g "partially
  persistent" guidance (only show sticky chrome when it earns its space).

## 2.3 Markup (injected into `<main>` as first child, or authored inline)

```html
<aside class="wl-lrail" data-wl-lrail aria-label="On this page" hidden>
  <nav class="wl-lrail__nav" aria-label="Sections on this page">
    <p class="wl-lrail__eyebrow">On this page</p>
    <ol class="wl-lrail__list" role="list">
      <li><a href="#biography">Biography</a></li>
      <li><a href="#championships-titles">Championships</a></li>
      <li><a href="#personas-characters">Personas</a></li>
      <li><a href="#career-timeline">Career timeline</a></li>
      <li><a href="#signature-matches">Signature matches</a></li>
      <li><a href="#match-record">Match record</a></li>
    </ol>
  </nav>
  <hr class="wl-lrail__rule" aria-hidden="true">
  <nav class="wl-lrail__actions" aria-label="Quick actions">
    <a class="wl-lrail__act" href="/wrestlers/" data-wl-random>Random wrestler</a>
    <a class="wl-lrail__act" href="#rivals" data-wl-rivals>Rivals</a>
    <a class="wl-lrail__act" href="/promotions/wwe/" data-wl-samepromo>Same promotion</a>
    <button class="wl-lrail__act wl-lrail__top" type="button" data-wl-top hidden>Back to top</button>
  </nav>
</aside>
```

Notes: `hidden` is removed by JS on first scroll (no-JS users get it immediately since the CSS
fallback in §2.4 unhides it when JS is absent via a `.no-js` body class the site already sets/clears).
Quick-action anchors have real crawlable hrefs; `data-wl-*` only *upgrades* behavior.

## 2.4 CSS approach

- **Positioning:** `position: sticky; top: calc(var(--wl-header-h) + 1rem)` inside a
  CSS-grid-defined left column. The profile `<main>` becomes
  `grid-template-columns: minmax(0, 15rem) minmax(0, 1fr)` at `>=1100px`; the rail lives in column 1,
  content in column 2. `align-self: start` so sticky works. Max-height `calc(100vh - header - 2rem)`
  with `overflow-y: auto; overscroll-behavior: contain` for very long section lists.
- **Active state:** `.wl-lrail__list a` gets a transparent 3px left border; `.is-active` sets the
  border to gold `#d4af37`, Oswald 600, and `color: var(--wl-ink)`. One accent, no fill, so it reads
  as a broadcast lower-third tick rather than a highlighted chip.
- **Progressive-enhancement CSS-only spy (optional, layered):** where supported, add
  `scroll-target-group: auto` on the list and style `a:target-current` identically to `.is-active`.
  This is additive only — the IntersectionObserver remains the source of truth for `aria-current`
  because Chrome does not yet emit `aria-current` for `:target-current` (Soueidan, §6 ref).
- **No layout shift:** the grid column is reserved at the breakpoint whether or not the rail has
  faded in, so revealing it never reflows the article.

## 2.5 Accessibility

- Wrapper is `<aside aria-label="On this page">`; the two link groups are `<nav>` with distinct
  `aria-label`s so a screen-reader rotor lists "Sections on this page" and "Quick actions" separately.
- Active link carries `aria-current="true"` (set/removed by the observer), the standard SR signal for
  "current location within a set." Never rely on color alone — the bold weight + left tick are
  redundant non-color cues.
- Fully keyboard operable: it is just links + one button, in DOM order right after `<main>` opens, so
  Tab order is logical. "Back to top" is a real `<button>`, not a styled div.
- Respects `prefers-reduced-motion`: smooth scroll and fade-in are disabled, jumps are instant.
- A visually-hidden "Skip section navigation" link precedes the rail so keyboard users can bypass the
  ~8 links to reach body content, mirroring the site skip-link pattern.

## 2.6 Quick actions detail

- **Random wrestler:** `data-wl-random` handler picks a slug from an in-memory list the site already
  ships for ⌘K (`js/search-index.js`), excludes the current slug, and sets `location.href`. No storage.
  If the index has not loaded, the raw href (`/wrestlers/`) still fires. Copy is "Random wrestler", not
  "Surprise me".
- **Same promotion:** the promotion hub URL is read from the page's existing promotion badge link (the
  profile already renders a promotion chip that links to `/promotions/<slug>/`), so the action can
  never point somewhere the body does not already link.
- **Rivals:** primary behavior scrolls to the in-page rivals content or the bottom rail's rivals
  group; if neither exists on a given page, the href degrades to `/rivalries/`.

## 2.7 Mobile behavior (`<1100px`)

- The vertical rail is **not** rendered as a sticky sidebar (no room, and it would fight the reading
  column). Instead the same jump-nav collapses into a **horizontal sticky "chapter strip"** directly
  under the site header: a single-row, horizontally scrollable `<nav>` of the section links, snap-
  scrolling (`scroll-snap-type: x proximity`), with the active chip auto-scrolled into view
  (`scrollIntoView({inline: 'center'})`) by the same observer. Same markup, restyled by media query.
- Quick actions on mobile move into the bottom rail's utility row (§5.7) to avoid two competing sticky
  strips. Only one horizontal sticky strip is visible at the top on mobile.
- Height budget: the chapter strip is a single 44px row (meets the NN/g >=1cm tap-target rule), so the
  content-to-chrome ratio stays generous.

## 2.8 Three cited references (left rail)

1. **MDN Web Docs / Stripe API reference left sidebar** — the canonical "in-page nav that tracks
   scroll position" pattern: a persistent left column of section links whose active item follows the
   heading currently in the viewport. Steal: reserved grid column so the rail never overlaps prose;
   one subtle active tick, not a filled chip.
2. **Ryan Mulligan, "Scrollspy Navigation Web Component"** (ryanmulligan.dev/blog/scrollspy-nav) and
   **Bram.us, "Smooth Scrolling Sticky ScrollSpy Navigation"** — the exact IntersectionObserver +
   `rootMargin` middle-of-viewport technique and the click-vs-spy guard we adopt in §2.2. Steal: the
   `-45%/-50%` rootMargin and the post-click suppression window.
3. **Sara Soueidan, "Redefining Scrollspy with CSS (No JS Needed)"** (newsletter 2025-08-18) —
   `scroll-target-group` + `:target-current`. Steal: layer it as progressive enhancement, but keep JS
   authoritative for `aria-current` because Chrome 140+ does not yet expose it to assistive tech.

---

# 3. STICKY BOTTOM RAIL — "Keep going"

## 3.1 Concept

A slim, horizontally scrolling "Keep going" tray pinned to the bottom of the viewport that surfaces
the profile's **own** most valuable cross-links as tappable poster-cards: top rivals, same-promotion
peers, and key events/matches the wrestler appears in. It is the *momentum* surface — it turns "I
finished reading" into "one more click" without the user scrolling to the footer. It is a compressed,
always-reachable mirror of the in-body Related rails + Keep-going block from `07-addictive-browsing`.

## 3.2 What it contains and how items are chosen (from the page's own links)

The script builds the tray by scraping links **already in the DOM**, in this priority order, deduped,
capped at 8–10 cards:

1. **Rivals** — `<a href="/wrestlers/…">` that appear inside the Signature Matches / rivalry prose,
   ranked by in-page frequency (on `/wrestlers/kane/`, The Undertaker appears 5x -> first card).
2. **Same promotion** — the promotion hub link + a few roster peers linked in body.
3. **Key events / matches** — `/events/…` and `/matches/…` links found in Signature Matches / Career
   Timeline.
4. **Keep-going overflow** — any remaining typed links from the injected Keep-going block.

Each card is labeled by type ("Rival", "WWE", "Event 1997") using the existing axis color tokens, so
the tray is scannable, not a gray link soup. Because every card's href is an in-body link, the tray
adds no new crawl edges and needs no data file.

## 3.3 Exact behavior (scroll-aware)

- **Hidden at top, revealed on intent.** The rail stays off-screen (translated 100% down) until the
  user has scrolled past ~60% of the article OR has been idle-reading for a beat, then slides up
  (250–300ms, matching NN/g's 300–400ms sticky-reveal range). Rationale: don't cover content while the
  user is still in the bio; offer "what's next" only once they're deep enough to want it.
- **Auto-hide near the footer.** When the in-body Keep-going block / footer enters the viewport, the
  rail slides back down and stays hidden — the full-size version is now on screen, so the compressed
  tray would be redundant and would cover it. Uses one IntersectionObserver on the footer sentinel.
- **Direction-aware (optional).** On fast upward scroll it may hide to return screen space, re-showing
  when the user settles, same debounce/threshold discipline as the header pattern (>a few px).
- **Never autoplaying, never modal.** No timers that navigate, no overlay that traps focus. It is a
  strip of links the user may ignore forever.

## 3.4 Markup (injected before `</body>`, links mirror in-body anchors)

```html
<aside class="wl-brail" data-wl-brail aria-label="Keep going" data-state="hidden">
  <div class="wl-brail__bar">
    <p class="wl-brail__title">Keep going</p>
    <ul class="wl-brail__track" role="list">
      <li class="wl-brail__card" data-axis="rival">
        <a href="/wrestlers/the-undertaker/">
          <span class="wl-brail__kicker">Rival</span>
          <span class="wl-brail__name">The Undertaker</span>
        </a>
      </li>
      <li class="wl-brail__card" data-axis="promotion">
        <a href="/promotions/wwe/">
          <span class="wl-brail__kicker">WWE</span>
          <span class="wl-brail__name">Same promotion</span>
        </a>
      </li>
      <li class="wl-brail__card" data-axis="event">
        <a href="/events/badd-blood-1997/">
          <span class="wl-brail__kicker">Event 1997</span>
          <span class="wl-brail__name">Badd Blood: In Your House</span>
        </a>
      </li>
      <!-- up to 8–10 cards -->
    </ul>
    <button class="wl-brail__close" type="button" data-wl-brail-close
            aria-label="Dismiss keep going bar">Dismiss</button>
  </div>
</aside>
```

## 3.5 CSS approach

- `position: fixed; left/right: 0; bottom: 0; z-index: var(--z-brail)` (below the header's sticky
  layer and below the bottom-right floater, see §7). Transform-based show/hide:
  `transform: translateY(100%)` when `data-state="hidden"`, `translateY(0)` when `"shown"`, with a
  `transition: transform .28s ease` gated on `prefers-reduced-motion`.
- The track is `display: flex; overflow-x: auto; scroll-snap-type: x proximity; gap: .75rem`; each
  card `scroll-snap-align: start`, fixed width (~13rem desktop, ~68vw mobile so the next card peeks —
  the standard "there's more" affordance from horizontal media rails).
- Cards reuse the poster `.tile` visual language at reduced height; `data-axis` maps to the promotion/
  relationship accent tokens for the left border + kicker color. Opaque background
  (`--wl-surface-2`), never translucent, per NN/g contrast guidance.
- Bar height is one card row (~92px desktop, ~76px mobile) so it never eats more than a sliver of the
  viewport. A top hairline + slight upward shadow separates it from content.

## 3.6 Accessibility

- Wrapper `<aside aria-label="Keep going">`; it is a set of links plus one dismiss `<button>`.
- **Focus-safe reveal:** showing/hiding is CSS transform only; the element stays in the DOM and in tab
  order, so it does not steal or trap focus. If a keyboard user Tabs into a card while the bar is
  hidden, the bar reveals (`:focus-within` also sets the shown transform) so focus is never on an
  off-screen control.
- Horizontal track is keyboard-scrollable because each card is a focusable link; `scroll-padding` on
  the track keeps the focused card fully visible.
- Dismiss is a labeled real button; on activation focus returns to the last body element the user was
  reading (or the footer Keep-going block) rather than being dropped.
- Cards convey type via the `.wl-brail__kicker` text ("Rival", "WWE"), not color alone.
- `role="list"` retained despite `display:flex` (Safari drops list semantics off flex `<ul>`).

## 3.7 Mobile behavior

- Same fixed bottom tray, full width, one row, `~68vw` cards with peek. This is the *primary* form —
  bottom rails are a native-feeling mobile pattern (thumb-reachable).
- The left-rail quick actions (§2.7) are appended as a compact utility row *inside* the bottom rail's
  header line on mobile ("Random" · "Rivals" · "Promotion") so there is exactly one bottom surface,
  not two.
- Respect the iOS/Android home-indicator inset: `padding-bottom: env(safe-area-inset-bottom)`.
- Coordinates with the bottom-right floater (§7): the floater sits above the rail; when the rail is
  shown on mobile the floater nudges up by the rail height so they never overlap.

## 3.8 Dismissibility (with the single storage flag)

- The **Dismiss** button hides the rail for the rest of the session (in-memory) by default — zero
  storage, fully spec-compliant.
- `FLAGGED, opt-in`: if the project later allows one cookie/localStorage key, persist
  `wl-brail-dismissed=1` so a user who closed it does not see it again for N days. This is the *only*
  storage this spec would ever request, it is isolated behind a feature flag, and absence of storage
  simply reverts to per-session dismissal. This mirrors the standard dismissible bottom-bar / cookie-
  bar convention.

## 3.9 Three cited references (bottom rail)

1. **Wikipedia / MediaWiki "Related pages"** (Reading/Web) — the end-of-article set of ~3 related
   entries chosen from the article's own link graph. Steal: derive "what's next" from the page's
   existing links (no editorial data file), type-labeled, capped small. We extend it from a static
   footer block to a scroll-aware sticky tray.
2. **YouTube "Up next" / Netflix "More like this" horizontal shelves** — the peeking-card,
   snap-scroll horizontal rail that signals "there is more to the right" and makes the next click one
   tap. Steal: fixed card width with next-card peek, scroll-snap, kicker + title, thumb-reachable at
   the bottom on mobile. (We deliberately drop autoplay — links only, no forced navigation.)
3. **Nielsen Norman Group, "Sticky Headers: 5 Ways to Make Them Better"** — reveal on scroll intent
   (300–400ms), opaque not translucent, keep chrome small, cost/benefit before pinning. Steal: the
   reveal-timing, contrast, and height-budget rules applied to a bottom (rather than top) sticky.

---

# 4. Shared script & injection (both rails)

- One entry in `js/enhance.js` runs on `DOMContentLoaded`, guards on
  `document.querySelector('main h2')` (profile pages), and:
  1. slugifies/ensures `h2` ids, builds the left rail, wires the IntersectionObserver spy + click
     guard + smooth-scroll offset;
  2. scrapes in-body cross-links, ranks them (§3.2), builds the bottom rail, wires the reveal/hide
     observers and dismiss.
- Idempotent (checks for `[data-wl-lrail]` / `[data-wl-brail]` before injecting) so re-running or SSR-
  authored markup is not duplicated.
- Total added weight target: < 4KB JS, < 3KB CSS (in the single `css/site.css`). No dependencies.
- Feature-detects `IntersectionObserver`; if absent, both rails simply render as static (left rail =
  plain jump links, bottom rail = static tray shown once past 60% via a scroll listener fallback).

# 5. Z-index / stacking contract (coordination with sibling surfaces)

From highest to lowest: site header sticky bar > ⌘K dialog (modal) > bottom-right floater >
**bottom rail** > **left rail** > content. Define as tokens in `css/site.css`
(`--z-header`, `--z-cmdk`, `--z-floater`, `--z-brail`, `--z-lrail`) so the three engagement surfaces
never fight. On mobile, only one top sticky strip (left-rail chapter strip) and one bottom surface
(bottom rail, with floater docked above it) are visible at once.

# 6. Open questions / handoffs

- Confirm the bottom-right floater's mobile dock height with its owner so §3.7 nudge math is exact.
- Confirm whether the promotion accent for "Same promotion" should follow the *primary* promotion or
  the most-linked one when a wrestler spans WWE/WCW/TNA/NJPW.
- Decide if the §3.8 storage flag is approved for launch or deferred (default: per-session, no storage).
