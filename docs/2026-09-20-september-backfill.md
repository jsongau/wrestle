# 2026-09-20 — The September backfill

Three weeks of Lore Feed + Gallery filled in one session after the site sat
unattended Sep 2–19. Written for the next session (human or AI) that has to
do this again.

## What changed and why

- `build/fill_week_0831.py` — filled Sep 2–6 into the already-open week of
  Aug 31 (19 dispatches, 8 videos). EXTENDS the existing gallery week literal
  in place via two in-list anchors instead of prepending a duplicate week.
- `build/add_week_0907.py` — week of Sep 7 complete (20 dispatches, 7 videos).
- `build/add_week_0914.py` — week of Sep 14 through Sep 20 (17 dispatches,
  9 videos, first official-channel RAF video the gallery has carried).
- `build/build_gallery.py` — SHOWNET gained "Sunday Night's Main Event"
  (Peacock) and "All In" (HBO Max); SNME added to SHOWNAME + SHOWORDER.
  Before this, both shows silently mislabeled as Netflix (`shownet()`
  defaults instead of failing — trap documented below).
- Generators re-run: gallery (246 video pages, 13 week pages), lorefeed
  (205 dispatches, 14 weeks, home rail 7, ticker 8), search index
  (550 entries, curated aliases intact), patch_next_event (self-advanced to
  Worlds Collide Sep 26 — zero edits, eventsdata.py's date filter worked),
  apply_shell (549 pages, 0 NOHDR/NOFTR).

## Decisions made (and rejected)

- **Reigns RETAINED over Penta 9/14** — two written sources (PWTorch, PW.net,
  spear at 22:25). REJECTED: YouTube ID FkxdfCo5QyQ, titled as Penta winning
  the title; oEmbed resolves it to fan channel "NagraPidi". The title claim
  is false. oEmbed author check is the gate that caught it — keep using it.
- **Zayn beat Punk on the 9/11 SmackDown** (Arena CDMX, WWE.com's own
  headline, 67-day reign ends). One W3 agent asserted the win happened at
  SNME Sep 13 — hallucinated date, overridden by the primary source.
- **Vaquer over Morgan, Chile live event, 9/12** (POST) — added at assembly,
  outside every agent lane, because it completes the arc the 9/7 Raw row
  opens (Morgan retains on TV, loses the belt off TV five nights later).
- **RAF 13 dated Sep 18**, not the briefed Sep 19 — Fightful, Wikipedia and
  Yahoo all say Friday Sep 18, Watsco Center; MiddleEasy's 9/19 is
  publish-date drift. Snyder RETAINED at RAF Moscow (USA Wrestling +
  Wikipedia) against FloWrestling's "claims title" phrasing.
- **Andy Williams passing dated Sep 6**, collapse described without
  asserting a day (Wrestling Inc's copy is internally inconsistent).
  The AEW tribute show (9/12) is its own dispatch in the 0907 week.
- **home=True budgets:** fill added ZERO home rows (the 0831 opener already
  carried the 5-cap); 0907 and 0914 each carry exactly 5, with agent-flagged
  rows (Ospreay eliminator, Kelani Jordan, Mason Rook) demoted at assembly.
  The home rail takes the newest 7 site-wide, so old-week flags are dead
  weight anyway.
- **Conflicts printed as conflicts** per site policy: Andrade's finisher
  name (Destination Madrid vs The Message), MCMG's opponents (Lethal Swirl
  vs The Swirl). Sep 11 SmackDown undercard verified but not filed — the
  feed is a digest, not a results page.
- **No ratings invented:** Raw 9/14 and NXT 9/15 numbers did not exist as of
  Sep 20 (Nielsen September methodology change delayed reporting).

## Traps discovered

- `shownet()` DEFAULTS to Netflix for any unknown show label — a caption
  starting with an unmapped show name mislabels silently. When adding a
  special (SNME, All In, a PLE), add it to SHOWNET **before** the week
  script runs, and grep the built week page for the expected network.
- Agents return `htags` as Python lists about a third of the time; the rail
  expects space-separated strings. Convert at assembly, and drop htags
  entirely from rows demoted out of home=True.
- The gallery fill-vs-open distinction matters: a second `{"week":"2026-08-31"...}`
  literal would have rendered a duplicate week. Extending in place via
  unique in-list caption anchors (with count checks) is the pattern.
- Stale .git lock files (index.lock, packed-refs.lock, refs/**) accumulate
  because the bridge cannot delete; mv them into `_to_delete/` before any
  commit. A commit can SUCCEED after printing a HEAD.lock error — always
  `git log -1` before retrying.

## Exact next steps

1. Push (user's own Terminal: `cd /Users/kytlegacy/wrestle` then
   `git push origin main`) — only when Jay says push.
2. Backlog, unchanged: RAF 12 results still stale in build_raf.py;
   /events/tickets/ still sells SummerSlam; CM Punk dossier now stale
   (lost the title 9/11, says champion); ~61 wrestlers on old format;
   Supabase waitlist.
3. Sep 26 is a double: AEW All Out AND WWE Worlds Collide, same night.
   Next weekly update should open the week of Sep 21 with both.
