# 2026-07-29 — Nav rename, Surprise Me (Lore Wrestler/Match), Explore hover-stub

## What changed
- **Mega nav:** "Superstars" → "Wrestlers" (label, aria-label, section comment in `components/meganav.html`); restamped onto all 268 pages via `build/apply_shell.py`.
- **Surprise Me floater (bottom-right, `.sm-ctrl` in `js/home-engage.js`):** removed "Random legend" and "Hall of Fame" rows; added **Lore Wrestler** (luchador-mask SVG `.ico-mask`, "Any of 108") → random `/wrestlers/*` page, and **Lore Match** (ring SVG `.ico-ring`, "Any of 30") → random `/matches/*` page. Kept the approved "Did you know / Undertaker 21-0" fact and the gold **Surprise me** button verbatim. Icons animate on hover (`sm-maskbob`, `sm-blink`, `sm-ringpulse`, `sm-ropebounce` in `css/site.css`).
- **Explore floater (bottom-left):** was always-open card; now a collapsed **ticket stub** (`.f2-explore` > `.f2-stub`, vertical "EXPLORE", gold edge + perforation notches, gleam sweep) that expands to the Vault Ticket match card on hover/focus (`.f2-explore:hover .f2-card`). Design A, per approval; yellow dot removed, label = "Explore". **Follow-up (same day):** stripped five-star branding from the EXPANDED card too — kicker is now "Explore" (was "Five-star match"), removed the star rating render and the sparkle glyph, and the reason drops "Rated X stars" (user: "just Explore").

## Decisions
- **Preserved the approved Surprise Me verbatim** (Undertaker fact + gold button); only the two rows were swapped. Ref: `preserve-approved-work` skill.
- **Rows are JS random-nav `<button>`s** (no crawlable href). SEO/GEO value lives in the DESTINATION pages (real indexed `/wrestlers/*`, `/matches/*`). Flagged the bigger play: dedicated crawlable "Lore Wrestler / Lore Match" hub landing pages if we want those as ranking concepts.
- **Mobile:** stub hidden `<=560px`; card shows directly (no hover on touch). Overflow verified 0px @320/360/390.

## Traps discovered
- **GNU sed** on the device Linux VM — use `sed -i` (NOT BSD `sed -i ''`).
- **Concurrent rankings session** left `build/build_rankings.py`, `js/rankings.js`, `rankings/index.html` modified — must be EXCLUDED from this commit (`git add -u` then `git reset` those three) so we don't cross sessions.
- **`.git/index.lock`** gets left behind when git refreshes the index through the device bridge (writes blocked) — `rm -f` it before committing.
- Cloud-mirror render showed harmless 404s for `oswald-600/700` weights (subset staged); production repo unaffected.

## Next steps
- Deploy this slice (see deploy block); rankings page nav lags until the rankings session commits its own restamp.
- SEO/GEO: decide whether "Lore Wrestler / Lore Match" become real hub landing pages.
- Backend: `data/events.json` single source for the ticket floater + Events banner + tickets page (kills frozen hardcoded dates).


## Round 2 (same day) — hover freshness + polish
- **Rotating facts:** replaced the single hardcoded Undertaker fact with a pool of **14 hand-curated** "Did you know" facts (`FACTS[]` in home-engage.js) that rotate with no immediate repeat on each `mouseenter`/`focusin` of the Surprise Me floater. Still curated, never auto-generated (per `preserve-approved-work`). User complaint that triggered it: "surprise me fact can't be the brock lesnar one each time."
- **Explore new-on-hover:** the Explore card advances to a fresh match/champion/hub on each hover/focus (`freshCard` on `.f2-explore` mouseenter + stub `focus`, not `focusin`, to avoid firing on the inner View/Next buttons).
- **Gleam refined:** dropped the diagonal white sheen (`@keyframes f2sweep`); replaced with a soft gold light that glides down the gold left edge (`.f2-stub__gleam` → `@keyframes f2edge`) — ticket-foil feel. User: "the glowing sheen on the explore looks ugly."
- **Back-to-top hidden on home:** `body[data-home] .wl-totop{display:none}` — the shared `media.js` back-to-top (`WL.backToTop`) collided with the Surprise Me floater bottom-right; it stays available on long content pages.


### Trap: never show raw counts in the UI
Do NOT display raw database/inventory counts in user-facing labels, subtext, badges, or pills (e.g. "Any of 108", "30 matches", "12 items"). They look cheap, they *undersell* small inventories (30 reads as thin), and they date the content the instant data changes. Use qualitative language or nothing. Fixed 2026-07-29: removed "Any of 108"/"Any of 30" from the Lore Wrestler/Lore Match rows. Codified as the `no-raw-counts` skill.


## Round 3 (same day) — Lore Feed ticker made universal (single-source)
The live-headline ticker (`.ticker7.rt`: LIVE tag, promotion-colored items, pager dots, Lore Feed link) was **home-only** — markup, `.rt-*` CSS, and rotation JS all lived in `index.html`, which is exactly why it never appeared on other pages. Made it universal and single-source:
- **Markup** moved into `components/meganav.html` inside the stamped `<header>`, so `build/apply_shell.py` stamps it on every page (idempotent). It now sits inside the sticky header = sticky on top of the nav, every page.
- **CSS** (`.rt`, `.rt-*`, `@keyframes rt-pulse`) lifted from index.html inline `<style>` into `css/site.css`.
- **Rotation JS** moved from index.html inline script into `js/nav.js` (loads `defer` everywhere), DOMContentLoaded-guarded.
- Removed the home-only markup + rotator from `index.html`; removed the wrong `lore-ticker` widget I built by mistake.
- Verified: ticker present + rotating (Moxley->Omega) on home, wrestler, title, event; 0 h-overflow @320/360/390; one ticker per page.
- Minor follow-up: `.rf-time` relative-time updater is still home-only, so non-home pages show the absolute date ("Jul 27") instead of "2d ago".
**Trap:** I asked the user which placement to use instead of just looking at the live main page, where the `.ticker7` widget already existed. Look at the running page before asking.


### LIVE mark → green "Orbit Signal" (chosen from 3 designs)
Replaced the red pulsing `.rt-live` dot with a custom green animated SVG. Offered 3 options (A Sonar Ping, B Broadcast EQ, C Orbit Signal); user chose **C**. It's a self-contained SMIL SVG: breathing core + bright center + two particles orbiting a faint ring, green (#21e06a / #8dffb9) with a drop-shadow glow. `.rt-live` restyled in site.css to a 16px flex container; removed the now-duplicated inline `.rt-*` CSS from index.html (it was shadowing the green styles). Verified green + animating (pixel mean-diff 6.2 across frames) in the universal ticker; 0 overflow.
