# 2026-08-22 - Lore Feed: weeks of Aug 3, Aug 10 and Aug 17

## What changed
The feed stopped at the week of Jul 27 (SummerSlam). Three weeks were missing. Added 45 dispatches to `DISPATCHES` in `build/build_lorefeed.py`, which emitted three new week pages, refreshed the hub, the site-wide ticker and the homepage rail from the same list.

- `/lore-feed/2026-08-03/` 16 dispatches. Lead: Page, Bandido and Brody King win the AEW World Trios Titles at Grand Slam Mexico. Also the NXT tag title change (Borne and Heights), Dory Funk Jr. in memoriam, TKO Q2 earnings, Royal Rumble 2027 to State Farm Stadium.
- `/lore-feed/2026-08-10/` 14 dispatches. Lead: The MFTs win the WWE Tag Team Titles. Also Jacy Jayne takes the Women's US Title, Oiwa wins G1 Climax 36, Tenzan retires.
- `/lore-feed/2026-08-17/` 15 dispatches. Lead: CM Punk retains as Sami Zayn turns on Kevin Owens. Also Solo Sikoa siding with LA Knight, Omega and Ospreay before All In, Dragunov leaving WWE.

## Sourcing rule applied
Every dispatch points at a page that was fetched and read. 21 distinct source URLs went through a second verification pass. One claim failed and was corrected: the Dragunov story does not support an April 17 last appearance, so the dek now cites the March 30 loss to Carmelo Hayes, which the page does support. Two candidate items were dropped for weak sourcing: a Kofi Kingston trademark story resting on a rumour roundup, and a "believed to be signed" Steven Borden note.

## Traps discovered
- **WWE.com SmackDown URLs**: the bare `https://www.wwe.com/shows/smackdown/<date>` often serves the PREVIEW, not results. Use the `/results` suffix for SmackDown. Raw and NXT serve results at the bare URL.
- **WL_ROOT is required.** `build/build_lorefeed.py` defaults `ROOT` to `/root/wwe` and dies with a PermissionError on this machine. Always run `WL_ROOT="$PWD" python3 build/build_lorefeed.py` from the repo root.
- **`htags` has a fixed vocabulary.** The homepage rail filter only knows matches, titles, rivalries and roster. A business or media dispatch marked `home=True` would land in the rail under a filter that does not exist, so business items are left out of the rail.

## Two generator fixes in the same pass
- The feed search placeholder used an em dash, which breaks the binding writing style. Now "Search this feed by name, title or promotion".
- `card()` printed the promotion chip even when it repeated the desk label, so `promo="tko"` plus `cat="business"` rendered "BUSINESS BUSINESS". The chip is now suppressed when the two labels match. Generic fix, applies to past and future weeks.

## Build gate
378 pages stamped, 0 NOHDR / 0 NOFTR. 378 files changed, 2199 insertions, 2010 deletions. Non-feed pages changed by exactly 5 lines each: the `?v=` cache-bust hash and the rolling ticker markup. No content loss.

## Next steps
1. The "Send me the Lore Feed" form on the homepage rail posts nowhere. Build the Supabase waitlist table and insert behind it. That is the next backend task.
2. Consider moving `DISPATCHES` out of the Python file into a JSON data file, so adding news does not mean editing code. Not needed while one person edits the feed.
3. Automate research: pull wwe.com and allelitewrestling.com recaps into a review queue so a week becomes an approval step instead of a research session.
4. Still open from 2026-08-03: the 6 AM PT nightly sync on the jsongaum account can re-clobber pages. It has not been confirmed disabled.
