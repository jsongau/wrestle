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
