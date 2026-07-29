# Rankings — every-match video + randomized hero (2026-07-29)

## What changed
- **Video coverage 21 → 32 of 36 matches.** Sourced 11 new OFFICIAL YouTube embeds (WWE / WWE Vault / WWE NXT), each re-verified via the YouTube oEmbed endpoint (author_name must be a rights-holder channel AND title must match). IDs recorded in project memory (`rankings_video_ids`).
- **Hero is now a random draw of ANY video match.** `build_hero` pool changed from `tier == "five-star"` to *every match with `video.id` and not `no_hero`*. All eligible ship as hero slides; non-first ship `display:none` (no thumb prefetch). `rankings.js` (and the preview's compact script) Fisher-Yates the slides on each load and reveal a random `data-hero-show` (=6) — refresh → different spotlight. Per-slide badges now reflect the real rating (`rating_badge` + `tier_label`), not a hardcoded 5★.
- **Cache-bust bug fixed.** `apply_shell.py::_ver()` hashed only 4 files, so `rankings.js` edits shipped under a stale `?v=`. Now hashes ALL css+js (repo-relative path + bytes, sorted) — any asset change bumps the token.

## Decisions
- **Benoit stays in the grid, never in the hero** (`no_hero:true`). User directive; enforced by the hero pool filter + the nav-ladder swap in build_rankings.py.
- **4 matches keep poster cards — no official embed exists.** Both Benoit matches (WWE scrub), Sting vs Hogan Starrcade '97 (official copy is wwe.com-only, YouTube upload delisted), Terry Funk vs Sabu (ECW barbed-wire, too graphic for WWE to post). We never embed fan re-uploads ("official source so we don't get in trouble").

## Traps discovered
- **`media.js` binds the click to `.yt__link`, not the `.yt` div.** Synthetic `.yt`-div clicks don't open the theater; real users click the anchor (which fills the facade) so it works. Test the anchor.
- **i.ytimg.com is unreachable from the cloud sandbox** — headless screenshots show black thumbnails even though the markup is correct; they load on the user's machine.
- **Deploy divergence:** origin advanced (Triple H dossier: profile.css/js, meganav, media.js, site.css) while we worked. Safe path = reset to origin, overlay our 4 untouched source files, hand-merge the site.css tail (both sides appended at EOF), then **regenerate** all pages from origin's components. Verified the deploy diff reverts nothing parallel (267 pages = `?v=` only).

## Exact next steps
1. **Match pages for the 8 newest matches** (6 HHH/HBK + 2 Benoit) — `/matches/{slug}/` currently 404 from the "Full breakdown" links. Build `build_match_media.py` to emit the real `.yt` embed + VideoObject + streaming link-out.
2. **Join Insider Supabase waitlist** — the top backend task; `/rankings/` is now the highest-watch-time surface to funnel from.
