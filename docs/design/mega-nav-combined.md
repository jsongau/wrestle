# MAT Mega-Nav — CONTROL ROOM (Concept 2 + 3 combined) · CHOSEN DIRECTION

Jay's pick: merge **Concept 2 (Production Truck / broadcast HUD)** with **Concept 3 (Gold Standard / ⌘K search)**.
Preview: `MAT-meganav-combined-control-room.html`.

## What it is
A broadcast "control room" aesthetic with a real global-search command palette.

- **Broadcast HUD (from C2):** live five-star ratings ticker across the top; monospace telemetry labels (JetBrains Mono); corner-bracket frames on the hero and mega tiles; red "● LIVE / ON AIR" accents; stat readouts.
- **Bento command-board mega (from C2):** hovering/click "Wrestlers" opens a mixed-span panel — a featured-athlete tile (record + brackets), a promotion switcher grid (WWE/WCW/ECW/TNA/NXT + A–Z), a roster stat cell, and a trending cell. Replaces flat link columns with a "control board."
- **⌘K command palette (from C3):** the header carries a search pill; ⌘K (or click) opens a categorized results overlay (Wrestlers / Matches / Rivalries) with duotone icons + ratings. Solves MAT's #1 UX gap (no global search).
- **Shared style:** black + gold `#d4af37` + red `#e11d2a`, Anton display, Oswald UI, Inter body, film grain, subtle mesh + grid background.

## Interaction & a11y
- Mega: hover-intent on desktop, click-toggle on touch; Esc closes; column headers are links.
- Palette: ⌘K / click to open, Esc / scrim-click to close, focus moves to input on open (in the real build: native `<dialog>` for free focus-trap + focus-return, arrow-key navigation, in-memory `MAT_INDEX`, no browser storage).
- Ticker + all motion respect `prefers-reduced-motion`.

## Rollout plan (for the real build — pending Jay's go)
1. Fold the HUD + ⌘K into `css/site.css` (new `.hud-*`, `.mega-board`, `.cmdk` classes; additive) and a new `js/cmdk.js` (palette + in-memory search index of all 41 wrestlers + 30 matches + rivalries).
2. Update the shared header markup across all 104 pages (ticker optional per page; search pill everywhere) — scripted find/replace since the header block is identical.
3. Keep the v2 Broadcast Bold hero/tiles; layer the HUD framing on the homepage.
4. Verify: 0 broken links, keyboard nav, reduced-motion, mobile; screenshot proof; commit.
