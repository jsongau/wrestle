# 2026-08-03 — Gallery: Week of Aug 3, SummerSlam-led catch-up

## What shipped
New weekly gallery page `/gallery/2026-08-03/` ("Week of August 3, 2026"), led by SummerSlam
fallout, plus 8 per-clip `/media/w/` pages, refreshed homepage + `/media/` This-Week widgets,
and `sitemap.xml` (+9). Source of truth: a new `WEEKS[0]` dict in `build/build_gallery.py`.

## The 8 clips (all official WWE, oEmbed-verified; labels spoiler-safe)
Night 1 (Sat Aug 1): Saturday full show (fhccSekCjhc), Undisputed WWE Title Punk/Rhodes
(vppyXi3THwo), Hell in a Cell Femi/Lesnar (NWG1hYXMS0M), Gunther vs. Aldis (8f4oQURoi_w),
Women's tag Paige & Bellas (gVJFzfzQIvM).
Night 2 (Sun Aug 2): Sunday full show (-Iy_6T23ttg), World Heavyweight Reigns/Rollins
(MXIhmvodQXM), Intercontinental Penta/Gable (9MEIl3OR1DQ).

## Decisions
- **SummerSlam-led, not a pure TV week** (user choice): it's Monday, only tonight's Raw has aired,
  so the freshest marquee content is SummerSlam (Aug 1-2). Clips dated by their real night; the
  page's "Still to air this week" carries Raw/NXT/Dynamite/iMPACT/SmackDown/Collision.
- **Teach the app a new show type rather than fake the data** (open/closed principle): the client
  `weekShows()` whitelisted only the six weekly shows and silently dropped anything else. Added
  "SummerSlam" as a first-class show (whitelist + SHOWNET ESPN + showFull "WWE SummerSlam") and
  generalized the hardcoded partial-week lede.
- **ESPN, not Peacock**: WWE PLEs moved to ESPN's app for 2026 (see data/research-weekly-schedule.md).
  Corrected the server maps and a stale client PLE/SPECIALS "Peacock".
- **Focused deploy over full re-stamp**: running apply_shell re-stamped every page's `?v=` token
  (f9b1847b -> 6e85b695) because of a pre-existing `_ver` all-assets upgrade, not this change.
  Committed only the gallery/homepage/media/sitemap/scripts; reverted the ~350-page cosmetic churn.

## Traps found
- `gallery_app.html` `weekShows()` order array is a hardcoded show whitelist — non-listed shows vanish.
- ID discipline: YouTube `/feeds/` RSS is robots-blocked; oEmbed works. WebSearch `allowed_domains=["youtube.com"]`
  finds candidates; accept only `author_name` = WWE with a matching title. A "SummerSlam 2025 / WWE Deutschland"
  impostor was caught this way.
- device_bash cannot write `.git` (stale index.lock, Operation not permitted) — commits/pushes must run in the
  user's native Terminal. Cloud egress can't push either (proxy 403).
- Render sandbox can't reach i.ytimg.com, so preview thumbnails look black there; they load live.

## Next steps
- Fill this week's TV as it airs: Raw 8/3, NXT 8/4, Dynamite 8/5, iMPACT 8/6, SmackDown 8/7, Collision 8/8.
- Update the client `PLE` object (gallery_app.html ~line 491) off the now-past SummerSlam to the next PLE
  (AEW All In, Aug 30, Wembley) to relight the countdown.
- Backend: automate weekly clip ingestion from official channel uploads + oEmbed verify (kills the manual hunt).
- Separate cleanup: reconcile the site-wide `?v=` cache-bust drift in its own commit.
