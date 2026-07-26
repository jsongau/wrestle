# Wrestle Lore — Bottom-Right Sticky Floater ("Discover") Spec

Role: Discovery / gamification designer. Scope: the third of three engagement rails, the
**bottom-right sticky floater**. Siblings (sticky left rail, sticky bottom rail) are specced
elsewhere; this doc owns only the floater and must not duplicate their jobs.

The left/bottom rails are *navigation you steer*. The floater is *discovery that comes to you*: a
compact, character-aware "Discover" element that keeps offering one more interesting thing to click
on a wrestler profile, without ever blocking the content or nagging. It is the site's serendipity
engine, the button you press when you did not know what to look at next.

Buildability contract (matches `/js/enhance.js` conventions): one vanilla-JS IIFE, no dependencies,
bails fully under `prefers-reduced-motion`, uses `matchMedia('(hover:hover) and (pointer:fine)')`
for hover niceties, no browser storage unless a line is explicitly flagged `[STORAGE]`, and no
network/backend unless flagged `[STATIC-JSON]` (a build-time static asset, still no server).
Crawlability is untouched because every destination the floater surfaces **already exists as a real
`<a href>` in the page body or in the shared nav**; the floater re-presents those edges, it never
becomes the only path to them.

Copy standard (inherited): no decorative arrows, no em-dash separators inside UI strings, no cliche
banned words. All microcopy below obeys it.

---

## 1. What to steal, and from whom

- **Material 3 FAB / Extended FAB.** The canonical bottom-right floating affordance: fixed to the
  content edge, 16px inset, one primary action, an optional label that expands on first paint then
  collapses to an icon. M3 is explicit that a FAB represents *the* single most useful forward action
  on a screen and must not compete with page CTAs. Steal: the shape, the inset, the collapse-to-icon
  economy, the single-action discipline.
  (https://m3.material.io/components/floating-action-button/guidelines,
  https://m3.material.io/components/extended-fab/guidelines)
- **StumbleUpon's "Stumble!" button.** One press, one serendipitous jump, near-zero decision cost.
  That single mechanic drove enormous session depth precisely because it removed the "what next"
  choice. Steal: the one-tap random jump as a first-class verb, and the feeling that pressing again
  is cheap. (https://en.wikipedia.org/wiki/StumbleUpon)
- **Wikipedia "Random article" + page previews + the wiki rabbit hole.** Wikipedia's own documented
  design goal is to let a reader hop node to node with minimal friction; page previews let you taste
  a destination before committing. Steal: preview-before-jump, and treating every entity as a node
  worth a random hop. (https://en.wikipedia.org/wiki/Wiki_rabbit_hole,
  https://diff.wikimedia.org/2018/04/18/how-we-designed-page-previews-for-wikipedia/)
- **Baseball-Reference "On This Day" / sports "this day in history".** A daily-changing hook tied to
  real dates gives a reason to return and a reason to click today specifically. Steal: date-anchored
  discovery as a return hook. (https://en.wikipedia.org/wiki/Baseball_Reference,
  https://allsportshistory.com/category/on-this-day-in-sports-history/)
- **IMDb "Fans also viewed" / knowledge-graph node model.** No entity page is terminal; every node
  has typed edges (rival, tag-teammate, same event). Steal: the floater's random jump should prefer
  *typed, character-relevant* neighbors over pure noise.
  (https://help.imdb.com/article/imdb/discover-watch/recommended-for-you-faqs/GPZ2RSPB3CPVL86Z)
- **Duolingo streak / loss-aversion micro-interaction.** A tiny, satisfying confirmation animation
  and a running count make a trivial action feel rewarding and repeatable. Steal: the reward beat
  after a rate/vote, and a lightweight session counter, without the shame mechanics.
  (https://www.justanotherpm.com/blog/the-psychology-behind-duolingos-streak-feature)

Anti-pattern to avoid, cited on purpose: FABs and floating widgets are the classic offenders for
obscuring content, hijacking attention, and reading as ad-chrome. The rules in section 6 exist to
dodge exactly that. (https://usersnap.com/blog/floating-action-button/)

---

## 2. Anatomy and resting state

Default (collapsed) is a single circular gold token, 56px, fixed bottom-right, 16px inset on
desktop, sitting **above** the sticky bottom rail (so it clears it, offset up by the bottom rail's
height plus 12px). Face: a small mark plus a one-word verb that hints the current mode. Resting
state is quiet: no motion, no pulse loop, gold ring at rest, slight lift on hover only when
`hover:hover` matches.

Tap / click expands it upward into a compact card, roughly 300px wide, 150 to 200px tall, anchored
to the same corner (grows up and left, never covers the corner it launched from). The card has:

- a one-line **mode label** and a small **mode dot-switcher** (3 to 4 dots) to cycle modes by hand,
- the **payload** (the did-you-know line, the neighbor preview, the rating control, the on-this-day
  line),
- one **primary link** (a real `<a href>` to an existing page),
- a **dismiss** affordance (close for this page) and a barely-there **"new one"** refresh.

Collapsed footprint is ~56px; expanded footprint never exceeds ~40 percent of a phone's width-safe
area and auto-collapses after an idle timeout. On viewports below 480px the floater docks as a
36px "pill tab" flush to the right edge, vertically centered-low, so it never overlaps the sticky
bottom rail's tap targets (mobile-responsive sibling doc governs the exact stack order).

---

## 3. The four modes

The floater ships with four rotating modes. It opens in whichever mode is most relevant to *this*
page and this reader, then a reader can dot-switch. Each mode is fully character-relevant and each
resolves to an existing internal link.

### Mode A — "Did you know" (default opener, lowest friction)
A single rotating factlet drawn from the current wrestler's own page data, ending in a real link.
- **Source:** page-local. Harvest from existing DOM: the `Finisher` and `Born` meta already in the
  profile head, the `Championships & Titles`, `Career Timeline`, and `Signature Matches` sections,
  and any proper-noun already linked in the bio (`/wrestlers/the-undertaker/`,
  `/rivalries/...`, `/events/...`). No new data needed for the fact text; the link target is an
  existing `<a href>` lifted from the body.
- **Payload example:** "Kane's first Hell in a Cell was against The Undertaker at Badd Blood 1997."
  followed by a primary link to that match or opponent page that already exists on the page.
- **Why it works:** it is a taste, not a wall of text (Wikipedia page-preview logic), and it seeds
  curiosity toward a link the reader had not scrolled to yet.

### Mode B — "Stumble the roster" (the StumbleUpon verb, the rabbit-hole core)
One tap jumps to a *character-relevant* neighbor, with a one-line preview shown first.
- **Source:** two tiers.
  - Tier 1 (zero deps): pick a random destination from the page's own harvested cross-links,
    weighted toward typed neighbors (rivals and tag partners first, then this wrestler's matches,
    then their events, then a peer wrestler). Everything here is already an `<a href>` in the body,
    so this is pure re-presentation.
  - Tier 2 `[STATIC-JSON]`: for a true across-site random hop beyond the current page's links, read
    a build-time `/data/roster.json` (slug, name, one-line hook, promotion accent). Static asset,
    no server, still crawlable because the same wrestlers are linked from `/wrestlers/` index.
- **Interaction:** first tap reveals the preview card (name, promotion accent, one hook line, small
  crest), so the reader chooses to commit, matching Wikipedia's preview-before-jump. A second tap on
  the primary link navigates. A "new one" reshuffles without navigating, which is the cheap,
  repeatable StumbleUpon gesture that builds depth.
- **Weighting rule:** never offer the page you are on; de-prioritize the last 3 shown this session
  (`[STORAGE]` optional, otherwise in-memory) so consecutive stumbles feel fresh.

### Mode C — "Rate this legend" (the micro-interaction, the return hook)
A one-tap rating of the current wrestler on a themed scale, with an instant reward beat.
- **Control:** a compact 5-star or themed 1-to-5 (a row of small championship-belt icons reads more
  on-brand than stars). One tap sets the rating, plays a short confirm animation (a belt "snap" or a
  gold flare), and shows a light session line such as "You have rated 3 legends today."
- **Storage:** the reader's own picks persist in-session in memory by default; persistence across
  visits is `[STORAGE]` (localStorage), which is exactly the one flag the engagement-retention
  critique argued the site should finally allow. **Community averages** ("4.8 from 2,314 fans") are
  `[BACKEND]` and out of scope for the static build; ship the personal loop now, leave a slot for
  the aggregate later.
- **Post-rate upsell to depth:** immediately after a rating, the card swaps to "Rated. Now rate a
  rival." and surfaces one rival link from the page. The reward beat plus a fresh target is the
  Duolingo loop, minus the shame.

### Mode D — "On this day" (the date-anchored daily hook)
Surfaces something in wrestling history matched to today's date, biased to the current wrestler when
possible.
- **Source:** `[STATIC-JSON]` a small `/data/on-this-day.json` keyed by MM-DD (debut, title win,
  classic match, each with an existing internal link). Compare against `new Date()` client-side;
  no server. When the current wrestler has an entry for today, lead with it ("On this day in 1997,
  Kane debuted at Badd Blood."); otherwise show the best site-wide entry for today.
- **Why it works:** it changes daily, which is the documented return-hook mechanic from
  sports "on this day" pages, and it gives a reason to click *today*.

---

## 4. Orchestration: which mode opens, and how rotation feels

Opening mode is chosen once per page load by a simple priority ladder, not randomly, so the floater
feels intentional:

1. If `on-this-day.json` has an entry matching today for this wrestler, open **Mode D**.
2. Else if the reader has not yet rated this wrestler this session, and they have scrolled past
   ~60 percent of the article (an existing IntersectionObserver sentinel can flag this), open
   **Mode C** (rate). Rating fits best after they have read.
3. Else open **Mode A** (did you know) as the safe, low-friction default.
4. **Mode B** (stumble) is always one dot-switch away and is the mode the "new one" button biases
   toward on repeat presses, because stumbling is the depth driver.

Rotation is manual-first: the dot-switcher and the "new one" refresh are the primary way to change
content. There is **no auto-cycling carousel** on a loop, which is the thing that makes floating
widgets feel like ads. The only automatic change is a single, slow, one-time content swap: if the
floater has sat collapsed and untouched for ~25 seconds, its collapsed label may swap its verb once
(for example from "Discover" to "Rate Kane") to hint a second mode exists, then it stays put. One
hint, not a loop.

---

## 5. How it drives rabbit-hole depth without being annoying

The depth mechanic is a chain, not a nag:

- Every mode ends in exactly one strong forward link, so pressing the floater always yields a next
  click, never a dead card. This is the direct counter to the flagship problem the
  engagement-retention critique named: the Kane profile currently dead-ends at the record table.
- **"New one" is cheaper than committing.** Reshuffling costs one tap and no navigation, so a
  restless reader keeps pulling the lever (StumbleUpon's core loop) and each pull is a fresh
  character-relevant target. Depth accumulates from voluntary, low-stakes presses.
- **Typed weighting keeps jumps relevant**, so the rabbit hole feels like following a story
  (rival to their classic match to the event it happened at) rather than random noise, which is the
  IMDb knowledge-graph lesson.
- **The rate loop hands off to a rival**, converting a terminal micro-action into a new node.
- **A tiny session tally** ("3 explored") gives a soft sense of momentum without a streak-shame
  punishment, borrowing the satisfying part of Duolingo and dropping the coercive part.

Depth is a byproduct of the reader wanting the next thing, which is the only durable kind.

---

## 6. Anti-annoyance rules (non-negotiable)

- **Never covers content.** The collapsed token is 56px in the corner; expansion grows up and left
  and auto-collapses on scroll and after ~12s idle. It sits above the sticky bottom rail, never on
  top of primary CTAs (M3's rule that a FAB must not compete with page actions).
- **Dismissible and it stays dismissed.** A close control collapses it for the page; a second close
  within the session hides it entirely for the session (in-memory; `[STORAGE]` to persist across
  visits). No re-popping.
- **No entrance pulse loop, no sound, no auto-open.** It never opens itself. Motion is a single
  short expand transition and the one reward beat on rating, all gated behind
  `prefers-reduced-motion: reduce` (under reduced motion it is a plain static card that changes
  content on click with zero animation).
- **No interstitials, no email capture, no ads.** This is discovery only; the funnel lives
  elsewhere.
- **Idle hint fires once.** The single verb-swap described in section 4 is the only unsolicited
  change, and it is one-shot.

---

## 7. Accessibility and crawlability

- The floater is a real `<button aria-expanded>` toggling a `role="dialog"`/`aria-label="Discover"`
  card; focus moves into the card on open and returns to the token on close; `Esc` collapses.
- Every payload link is a genuine `<a href>` to an existing page, keyboard reachable, so the floater
  adds zero crawl dependency: if JS never runs, nothing is lost because all destinations already
  live in the body and nav. The floater is progressive enhancement, injected after content paint.
- Rating control is a labeled radiogroup (belt icons have text labels), operable by arrow keys.
- Contrast: gold token on a dark scrim ring meets AA at the 56px size; do not rely on the gold
  alone to convey state, pair it with the label text.
- Live region: mode/content changes announce politely via `aria-live="polite"` on the payload node.

---

## 8. Build spec

- **File:** new `/js/discover.js`, one IIFE, loaded `defer` after `enhance.js`. Reuse the existing
  reduced-motion and fine-pointer guards verbatim.
- **Injection:** on `DOMContentLoaded`, build the DOM in JS and append to `<body>`; nothing is in
  the static HTML, so it cannot regress crawlability or layout.
- **Page reads (no backend):**
  - wrestler name and slug from `document.title` / the canonical URL,
  - `Finisher` and `Born` from the existing profile meta,
  - the section links via `document.querySelectorAll('main a[href^="/"]')`, bucketed by path prefix
    (`/rivalries/`, `/matches/`, `/events/`, `/wrestlers/`) for typed weighting.
- **Optional static data (flagged):** `[STATIC-JSON]` `/data/roster.json` and
  `/data/on-this-day.json`, fetched once, cached in memory, failing silently to page-local mode if
  absent. Build these in the same Python pipeline that stamps profiles.
- **CSS:** append a `.wl-discover` block to the shared stylesheet using existing tokens
  (`--gold #d4af37`, the red, promotion accent variables, Anton/Oswald/Inter). Positioning via
  `position:fixed; right:16px; bottom: calc(var(--bottomrail-h,0px) + 12px);` so it stacks with the
  sibling bottom rail.
- **State:** all in-memory by default; the only `[STORAGE]` keys are `wl.rated.<slug>` and
  `wl.discover.dismissed`, both optional and both degrade gracefully.
- **Perf:** zero third-party requests, no layout thrash on scroll (collapse via a class + CSS
  transition, not per-frame JS), well within the CWV budget the perf critique set.

## 9. Microcopy (copy-standard compliant)

- Collapsed verb: "Discover"
- Mode A: "Did you know" then a one-line fact and a link labeled by the destination name.
- Mode B: "Jump to a rival" or "Stumble the roster", refresh control labeled "Show another".
- Mode C: "Rate this legend", after: "Rated. Now rate a rival.", tally: "You explored 3 today."
- Mode D: "On this day", one line, one link.
- Dismiss: "Hide".

---

### Sources

- Material 3 FAB / Extended FAB guidelines: https://m3.material.io/components/floating-action-button/guidelines ; https://m3.material.io/components/extended-fab/guidelines
- StumbleUpon serendipity loop: https://en.wikipedia.org/wiki/StumbleUpon
- Wikipedia rabbit hole + page previews: https://en.wikipedia.org/wiki/Wiki_rabbit_hole ; https://diff.wikimedia.org/2018/04/18/how-we-designed-page-previews-for-wikipedia/
- Baseball-Reference / sports "on this day": https://en.wikipedia.org/wiki/Baseball_Reference ; https://allsportshistory.com/category/on-this-day-in-sports-history/
- IMDb "fans also viewed" knowledge-graph nodes: https://help.imdb.com/article/imdb/discover-watch/recommended-for-you-faqs/GPZ2RSPB3CPVL86Z
- Duolingo streak micro-interaction / loss aversion: https://www.justanotherpm.com/blog/the-psychology-behind-duolingos-streak-feature
- FAB anti-patterns (obscuring content, ad-chrome feel): https://usersnap.com/blog/floating-action-button/
