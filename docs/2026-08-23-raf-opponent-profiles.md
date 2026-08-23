# RAF opponent profiles: eight new athlete files, and the RAF athlete set becomes a graph

**Date:** 2026-08-23
**Scope:** `build/build_raf.py`, `/promotions/raf/athletes/*`, `/promotions/raf/raf-13/`, `/promotions/raf/raf-14/`, `sitemap.xml`

---

## What changed

**Eight new athlete files**, one for every opponent Arman Tsarukyan has faced or is booked against in Real American Freestyle:

| Slug | Athlete | RAF record | Second record |
|---|---|---|---|
| `colby-covington` | Colby Covington | 4-0 | Selected UFC record, 8 bouts |
| `dillon-danis` | Dillon Danis | 0-2 | none |
| `tony-ferguson` | Tony Ferguson | 0-1 | Selected UFC record, 9 bouts |
| `urijah-faber` | Urijah Faber | 0-2 | none |
| `lance-palmer` | Lance Palmer | 1-3 | none |
| `georgio-poullas` | Georgio Poullas | 1-2 | none |
| `keelon-jimison` | Keelon Jimison | 1-3 | none |
| `kuat-khamitov` | Kuat Khamitov | 0-1 | Recent MMA record, 6 bouts |

**Two new event pages** so no announced booking dead-ends: `raf-13` (Sept 19, Watsco Center, Coral Gables) and `raf-14` (Oct 3, Fontainebleau Las Vegas). 13 events to 15; 142 bouts to 153.

---

## The generator change that made it possible

`athlete_page()` was written for exactly one athlete. It hardcoded a "UFC Record" section, read the RAF record out of `stats[2]`, and assumed every athlete had a DOB, a reach, a real name and a grappling paragraph. Eight of the nine new subjects break at least one of those.

Three changes fixed it without a rewrite:

1. **`alt_of(a)` normalises the second record.** Tsarukyan's key is `ufc` for historical reasons; the opponents use a generic `alt` with `alt_title` / `alt_lead`. One function returns one shape, and the section title, sub-nav label and JSON-LD `jobTitle` all derive from it. Athletes with no second record simply don't get the section.
2. **`secs_for(a)` builds the sub-nav from what the page actually has**, so section numbering (`01`..`06`) stays contiguous whether there are five sections or six. The old module-level `SECS` constant was a lie the moment a second athlete existed.
3. **`_pub()` guards every optional field.** Reach, height, DOB and real name are all omitted rather than printed as "Not published" or `None`. Jimison has no published DOB; Danis and Poullas have no published reach.

The RAF-record lead now reads `rafstats[0][0]`, not `stats[2][0]` — positional indexing into a display list was the fragile part, and it silently produced wrong copy rather than an error.

---

## Linkable and crawlable

`ATHLETE_BY_NAME` indexes all nine athletes, and `athlete_link()` resolves a name to its page while refusing to self-link. It is wired into four places:

- **`bout_row()`** — every athlete name in every event-card table across all 15 event pages
- **RAF record tables** — opponent column on every athlete page
- **Second-record tables** — opponent column (catches Tsarukyan appearing in Covington's UFC list, etc.)
- **Rivalry cards** — the `.fac-name` heading

Plus a rail block, **"Other RAF athlete files"**, linking the other eight from every profile, and the RAF hub's Athlete files grid listing all nine.

Measured result: every athlete page has **10 to 17 inbound internal links**, from event pages, the hub, and each other. Zero orphans. All nine in `sitemap.xml`, all with `Person` + `FAQPage` + `BreadcrumbList` JSON-LD (validated as parseable JSON), unique `<title>`, self-referential canonical, `index,follow`.

---

## Research corrections baked in

Four agents researched two athletes each. What they overturned:

- **Tony Ferguson's 2006 national title is NCWA, not NCAA.** Widely miscited.
- **Keelon Jimison's real RAF record is 1-3, not the 1-0-2 his own RAF athlete page shows.** RAF omits his RAF 02 loss to Cayden Henschel; FloWrestling and InterMat both carry it. The page states the discrepancy in the "Setting one thing straight" box rather than quietly picking a number.
- **Urijah Faber is 0-2 in RAF**, not 0-1 — he also lost to Henry Cejudo at RAF 06.
- **Kuat Khamitov's age**: RAF says 28; Sherdog, Tapology, ESPN, sports.ru and mma.express all publish 1988-02-22, which makes him 38. Published the database consensus. His MMA record is attributed to Sherdog explicitly because Tapology has him at 26-7-2.
- **Colby Covington is an RAF investor while competing in it.** Co-founder Chad Bronstein has said on the record that this buys no matchmaking control, and overruled Covington publicly on the Belal Muhammad booking. That is the correction box on his page.
- **Lance Palmer is RAF's Head of Talent Development** while competing.
- **Georgio Poullas's June 2026 aggravated-battery arrest was deliberately omitted** — unresolved case, low-profile individual, no bearing on his wrestling record.

## Data corrections to existing pages

- **RAF 11 main event score.** RAF's own recap and the large majority of press ran **5-3**; RAF's event-page scoreboard and USA Wrestling ran **5-2**. Yahoo's round-by-round shows 5-2 was the score at the end of period two. Filed as 5-3 with the discrepancy stated in the RAF 11 event note. Covington's points-for-and-against stat corrected 31-6 to 36-11.
- **The belt is a family, not one belt.** RAF's founding announcement: "RAF Crossover Championship... The inaugural Cruiserweight Crossover Championship." Standardised on **Cruiserweight Crossover Championship** (RAF 11, RAF 13) and **Middleweight Crossover Championship** (RAF 14). RAF itself uses both word orders.
- **RAF 06 Tsarukyan vs Poullas is filed as "decision, score disputed"** rather than a number. Four outlets published four scores: RAF 5-4, press consensus 5-3, MMA Mania 6-4, USA Wrestling 5-2. The event note says so.
- **RAF 06 Jimison vs Guida** now carries its 13-2 score.
- **RAF 12 card corrected**: the women's bout is Kennedy Blades vs **Diana Avsaragova** for the Women's Middleweight Championship, not a catchweight against Reese Larramendy. Burroughs–Brady and Nickal–McEnelly are catchweight. Wick–Nolf is for a **vacant** middleweight belt; Dvalishvili–Cejudo is for an **inaugural** crossover lightweight belt. Covington vs Muhammad was RAF 12's original main event and moved to RAF 13.
- **Covington's division**: RAF files him three ways — athlete page says catchweight, champions page says crossover cruiserweight, the RAF 11 bout was contested at cruiserweight. Stated plainly in his Background section rather than picking one silently.
- **Hub lede no longer hardcodes the event count.** It said "Thirteen events in" while the stat bar said 15. Now computed from `EVENTS`.

---

## Still open

- **RAF 12 was still in progress at build time** (Aug 22, 8pm ET). Results are not published; the page correctly shows the announced card with "Not yet wrestled". It needs a results pass. Two bouts were posted at time of research: Woodley def. Buckley 14-8, Ono def. Davino 4-0.
- **RAF 14's crossover middleweight belt lineage is unverified from RAF directly** — RAF's champions page does not list a crossover middleweight title. Sherdog and Jits Magazine describe Tsarukyan as defending champion. Treated as inaugural.
- **Six commits are still unpushed.** The GitHub token does not have repository access to `jsongau/wrestle`.

## Traps discovered

- **The `.reveal` class makes full-page screenshots look broken.** `profile.css` sets `opacity:0` on `.reveal` and `profile.js` adds `.in` on intersection. A Playwright `fullPage` screenshot only reveals what the 1000px viewport touched, so every section below the fold renders blank. Scroll the page and force `.in` before capturing, or you will spend an hour debugging CSS that is fine.
- **Missing web fonts fake an overflow bug.** With Anton absent the browser falls back to system-ui, which is roughly 30% wider, and the hero `h1` clips ("TSARUKYA"). With `fonts/anton-latin-400-normal.woff2` present the h1 fits exactly at every breakpoint. Always stage the fonts before judging type.
- **Injecting a `%` operator into an already-`%`-formatted concatenated string is a syntax error, not a runtime one.** The hub `main` string is one big literal formatted once at the end; new `%d` placeholders belong in the existing tuple.
