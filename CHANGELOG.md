## 2026-08-23 (RAF: eight opponent athlete files, RAF 13 and RAF 14, and the athlete set becomes a linked graph)
- **Eight new profiles** at `/promotions/raf/athletes/`: Colby Covington, Dillon Danis, Tony Ferguson, Urijah Faber, Lance Palmer, Georgio Poullas, Keelon Jimison, Kuat Khamitov. Every opponent Tsarukyan has faced or is booked against, on the same `/wrestlers/` profile template.
- **`athlete_page()` generalised.** `alt_of()` normalises the second combat record (Tsarukyan's `ufc` key, the opponents' generic `alt`), `secs_for()` builds the sub nav from the sections a page actually has so numbering stays contiguous, and `_pub()` omits unpublished DOB, reach, height and real name instead of printing `None`. The RAF record lead now reads `rafstats[0][0]` rather than indexing positionally into the display stats.
- **Linkable and crawlable.** `ATHLETE_BY_NAME` plus `athlete_link()` wired into `bout_row()` (every name in every event card across 15 events), both record tables, and the rivalry cards; a new "Other RAF athlete files" rail block links the other eight from every profile. Every athlete page now has 10 to 17 inbound internal links. Nine athletes in `sitemap.xml`, all with valid Person, FAQPage and BreadcrumbList JSON-LD, unique titles and self canonicals.
- **Two new event pages** so no announced booking dead-ends: `raf-13` (Sept 19, Watsco Center, Coral Gables) and `raf-14` (Oct 3, Fontainebleau Las Vegas). 13 events to 15, 142 bouts to 153.
- **RAF 11 score filed as 5-3, with the disagreement stated.** RAF's own recap and most press ran 5-3; RAF's event scoreboard and USA Wrestling ran 5-2, which Yahoo's round by round shows was the score after period two. Covington's points for and against corrected 31-6 to 36-11.
- **The crossover belt is a family, not one belt**: Cruiserweight Crossover Championship (RAF 11, RAF 13), Middleweight Crossover Championship (RAF 14). Standardised everywhere.
- **RAF 06 Tsarukyan vs. Poullas is now "decision, score disputed"** rather than a number: RAF published 5-4, press 5-3, MMA Mania 6-4, USA Wrestling 5-2. RAF 06 Jimison vs. Guida carries its 13-2 score.
- **RAF 12 card corrected**: Kennedy Blades defends the Women's Middleweight Championship against Diana Avsaragova, not a catchweight against Reese Larramendy. Burroughs-Brady and Nickal-McEnelly are catchweight. Wick-Nolf is for a vacant belt, Dvalishvili-Cejudo for an inaugural one. Covington vs. Muhammad moved off this card to RAF 13.
- **Research corrections**: Ferguson's 2006 title is NCWA not NCAA; Jimison is 1-3 in RAF, not the 1-0-2 his RAF page shows (it omits his RAF 02 loss); Faber is 0-2, not 0-1; Khamitov is 38 per five fight databases, not the 28 RAF lists. Covington competes in RAF as an investor and Palmer as its Head of Talent Development, both stated on the page.
- Hub lede no longer hardcodes the event count. Build gate: 485 pages stamped, 0 NOHDR / 0 NOFTR.

## 2026-08-23 (Tsarukyan page: real template classes, page-local CSS shipped like the profiles do)
- Agents dissected the cm-punk page. The profile template is THREE layers, not two: `site.css`, `profile.css` scoped under `.wl-dossier`, and a **36KB page-local `<style>` block** carrying components that exist in neither stylesheet.
- The athlete page now ships its own `<style>` block the same way, with the verbatim rules for `.sec-lead`, `.rec2-*` (stat tiles, scroll container, sticky-header table), `.rw`/`.rw-w`/`.rw-l` result badges, `.pchip` chips, `.faq2-*` accordion and `.fac-*` cards.
- Markup rewritten onto those classes: `rec2-scroll` + `rec2-table` for both record tables, `rw` badges instead of text, `pchip` for title and event tags, `faq2-item` instead of a bare `details`, `opp-link` for the event links. Verified full class parity against cm-punk, zero template classes missing.
- Notes for later: `.rw` and `.lg` collide by name with unrelated `.wl-dossier .rw` / `.record-legend .lg` rules in profile.css, which is why the profiles keep them page-local rather than in a shared sheet. Three chips used in cm-punk's markup (`pchip-aew`, `pchip-ecw`, `pchip-ind`) have no rule anywhere and render grey.

## 2026-08-23 (Arman Tsarukyan page rebuilt on the real profile template)
- **The athlete page now uses the `/wrestlers/` profile template**, not a RAF-styled approximation: sticky sub nav, the `.idn` identity bar with vitals and socials, the `.hero` block with kicker, NOW chip, stat row and portrait card, numbered `.sec` sections, and the Tale of the Tape rail. `profile.css` scopes roughly 432 rules under `.wl-dossier`, so that wrapper is the template, not decoration.
- `.rec2-stats` and `.rec2-stat` were page-local to cm-punk's inline `<style>` and existed in neither stylesheet. Moved into the idempotent RAF block in `css/site.css` so any future profile can use them.
- Fixes found by rendering: `&middot;` in the hero kicker was double escaped by `esc()`; and joining a two word name with `&nbsp;` overflowed the `h1`, which only works for a short name like CM Punk.
- Build gate: 475 pages stamped, 0 NOHDR / 0 NOFTR.

## 2026-08-23 (RAF: Arman Tsarukyan athlete file, RAF 09 card corrected)
- **New `/promotions/raf/athletes/arman-tsarukyan/`**: full RAF record (8 matches plus the announced RAF 14 booking) with every match linked to its event card, the complete 12 fight UFC record, bio, and the wrestling background stated honestly. Person + BreadcrumbList schema. Linked from a new "Athlete files" block on the RAF hub so it is not an orphan.
- **Placed under `/promotions/raf/athletes/`, not `/wrestlers/`.** Tsarukyan is an MMA fighter, not a pro wrestler; putting him in the wrestler namespace would pollute its A to Z, its counts and its search index.
- **Corrected the RAF 09 card**: it was missing the Tsarukyan vs. Keelon Jimison bout (tech fall 16-5). The athlete page would have claimed a RAF 09 win the RAF 09 page did not list. 141 bouts to 142.
- **Two research corrections baked into the page**: Tsarukyan and Makhachev have fought once, not twice (the UFC 311 rematch was booked and withdrawn from), and no world, European or national freestyle medal appears in any published record, so the page says Master of Sport rank and nothing more.
- `.rec2-*` classes are scoped under `.profile-main` and render unstyled elsewhere; the athlete page uses the RAF stat block instead. Build gate: 475 pages stamped, 0 NOHDR / 0 NOFTR.

## 2026-08-22 (Real American Freestyle: new /promotions/raf/ section, wired into the feed and gallery)
- **New generator `build/build_raf.py`** emits the RAF hub plus 13 event pages (RAF 01 to RAF 12 and RAF Georgia), 141 bouts with weight class, winner, method, score and title status, 42 oEmbed-verified official clips, SportsEvent / FAQPage / BreadcrumbList schema, sitemap +14. Third instance of the one-source generator pattern; no new abstractions.
- **Lore Feed**: `raf` added to the `PROMO` map plus 10 sourced dispatches, so RAF flows into the weekly feed, the site-wide ticker and the homepage rail from the same list as WWE and AEW.
- **Gallery + homepage This Week**: RAF is a fifth promotion tab, with clips in the three weeks that contain a RAF card (Jul 6, Jul 13, Aug 17). The tab only appears in weeks that have one, which the per-week `promos` dict handles for free.
- **Nav unchanged at the top level.** RAF went into the existing Promotions mega menu and the `/promotions/` directory instead.
- Traps: `js/media.js` owns `.yt[data-yt-id]` and replaces any custom facade with "NO SIGNAL"; the `.dk bcard` promotions grid lives in `components/meganav.html`, so editing `promotions/index.html` is reverted by apply_shell; `vtitle()` read "RAF RAF" when a promo's tab name equals its show name. All three fixed. Notes in `docs/2026-08-22-raf-integration.md`.
- Build gate: 474 pages stamped, 0 NOHDR / 0 NOFTR.

## 2026-08-22 (Viewing Gallery - August catch-up: Aug 3 filled in, Aug 10 and Aug 17 added)
- **74 official clips added** to `WEEKS` in `build/build_gallery.py`. The week of Aug 3 went from 8 SummerSlam clips and six "clips landing soon" slots to all 7 shows captured; new `/gallery/2026-08-10/` and `/gallery/2026-08-17/` cover both following weeks. 74 new `/media/w/` video pages with VideoObject schema, sitemap +74.
- **Every id oEmbed-verified** against the YouTube endpoint, accepted only on author_name of WWE, All Elite Wrestling or TNA Wrestling with a matching title and date. Labels kept spoiler-safe: stakes and participants, never results.
- **PLE countdown relit**: `gallery_app.html` still pointed at SummerSlam on Aug 1 and was one day from `pleInRange` hiding the band and emptying the "road to" rail. Repointed at AEW All In: London, Aug 30 at Wembley. SPECIALS gained Aug 30 All In and Sep 6 Sunday Night's Main Event in both the server and client copies.
- Build gate: 452 pages stamped, 0 NOHDR / 0 NOFTR. Notes in `docs/2026-08-22-lorefeed-august-catchup.md`.

## 2026-08-22 (Lore Feed - August catch-up: weeks of Aug 3, Aug 10, Aug 17)
- **Three missing weeks published.** 45 new dispatches appended to `DISPATCHES` in `build/build_lorefeed.py`: `/lore-feed/2026-08-03/` (16, lead = AEW World Trios change at Grand Slam Mexico), `/lore-feed/2026-08-10/` (14, lead = The MFTs win the WWE Tag Team Titles), `/lore-feed/2026-08-17/` (15, lead = CM Punk retains as Sami Zayn turns on Kevin Owens). Hub, rolling 7-day ticker and homepage rail all regenerate from the same list.
- **Every dispatch source-verified.** 21 distinct URLs fetched and read; one failed claim corrected (Dragunov's last appearance), two weakly-sourced items dropped. Official promotion recaps preferred (wwe.com, allelitewrestling.com, tnawrestling.com, corporate.wwe.com, TKO investor relations); trade press carries the Report stamp.
- **Generator fixes**: feed search placeholder no longer uses an em dash (binding writing style); `card()` suppresses the promotion chip when it duplicates the desk label, killing the "BUSINESS BUSINESS" kicker on `promo="tko"` dispatches. Both are generic and apply to every week.
- Build gate: 378 pages stamped, 0 NOHDR / 0 NOFTR; non-feed pages changed by 5 lines each (cache-bust + ticker), no content loss. Traps and next steps in `docs/2026-08-22-lorefeed-august-catchup.md`.

## 2026-08-03 (Lore Feed single-source: homepage rail wired to dispatches + SummerSlam)
- **The homepage "Lore Feed" rail is now generated by `build_lorefeed.py`, not hand-coded.** It was a static block in index.html that drifted from the /lore-feed/ page and nav ticker. Added `home=True` + `htags` flags on dispatches; the generator injects the featured items into `.hrl-list` (regex-scoped, idempotent) alongside the ticker. One dispatch list now feeds the /lore-feed/ page, the ticker, AND the homepage rail. Still curated (you flag which items are featured), so it can't drift.
- **SummerSlam 2026 published** (9 sourced dispatches, fold into the week of Jul 27). Rail + ticker lead with Reigns; week page carries the three title changes (Gable/IC, Corbin/US, Green/interim). Coexists with the same-day gallery "Week of Aug 3" This Week widget (df6f89f2), untouched.
- Rebased onto live df6f89f2. index.html change is 9 lines (rail + ticker + cache-bust), no content loss; apply_shell 364 pages, 0 NOHDR / 0 NOFTR.

## 2026-08-03 (Gallery — Week of Aug 3, SummerSlam-led catch-up)
- **New week `/gallery/2026-08-03/`** in `build/build_gallery.py` (WEEKS[0]), led by SummerSlam fallout: 8 official, oEmbed-verified WWE clips split by night — Aug 1: Punk/Rhodes (Undisputed), Gunther/Aldis, Paige & Bella Twins, Femi/Lesnar (Hell in a Cell), Saturday full show; Aug 2: Reigns/Rollins (World Heavyweight), Penta/Gable (IC), Sunday full show. Spoiler-safe labels; one crawlable `/media/w/` page per clip with VideoObject schema. "Still to air this week" lists Raw/NXT/Dynamite/iMPACT/SmackDown/Collision as the week fills in.
- **Taught the gallery app about Premium Live Events**: `gallery_app.html` `weekShows()` modeled only the six weekly shows, so a PLE ("SummerSlam") was silently dropped. Added it to the show whitelist, SHOWNET, showFull; generalized the hardcoded "Raw and NXT are in the books" lede to name whatever actually aired. Server: SHOWNET/SHOWNAME/SHOWORDER + SummerSlam, SPECIALS Aug 1/2.
- **Correct networking**: WWE PLEs stream on **ESPN** in 2026 (not Peacock) — fixed in both server maps and the client PLE/SPECIALS.
- Homepage + `/media/` This-Week widgets refresh to SummerSlam from WEEKS[0]; `sitemap.xml` +9 URLs. Gallery-scoped commit only — a pre-existing site-wide `?v=` cache-bust drift (from the `_ver` all-assets upgrade) was left for a separate reconcile.

## 2026-08-03 (Membership — restore after nightly-sync clobber)
- **Restored the Insiders page** (founder meter, community scorecard, faction gifting, selectable tiers, Ringside annual→signup) from b46343b onto current main. The 2026-08-01 Nightly sync had regenerated membership/index.html back to the old "Get in the ring" waitlist page from a stale source, silently reverting all of the 29 Jul membership work. Re-stamped against the current shell (header/footer byte-identical to live pages). ⚠️ The nightly generator's membership source must be updated or excluded, or it will clobber this again.

## 2026-07-29 (Lore Feed — newsroom generator + site-wide 7-day ticker)
- **New generator `build/build_lorefeed.py`**: one `DISPATCHES` list (35 dated, sourced dispatches across WWE/NXT/AEW/TNA/NJPW/TKO) emits, all in sync: the `/lore-feed/` editorial hub (lead + river + "Browse by Week" index), one SEO/GEO page per Monday-week at `/lore-feed/<YYYY-MM-DD>/` (7 weeks, each with recap prose + CollectionPage/ItemList/BreadcrumbList JSON-LD), and the site-wide rolling 7-day ticker in `components/meganav.html` (cap 8, newest first, crawlable HTML — stamps to every page). Replaces the old thin relative-time wire.
- **Editorial discipline**: every dispatch carries a visible Official (promotion-confirmed) vs Report (trade press) stamp; obituaries get an "In Memoriam" treatment; `_lead_score` picks the week's biggest story, not merely the newest. All marquee items spot-verified against reputable sources 2026-07-29.
- **Lead-alignment fix**: lead card copy is wrapped in `.lf-lead__copy` so the 2-column grid renders as copy | art instead of scattering headline/dek/footer/art across columns.
- **Week switcher**: new `.lf-weekbar` (Newer/Older + a chip per week, current in gold, horizontally scrollable, all real links) on the hub and every weekly page; sticky on weekly pages.
- **Also**: `.lf-*` styles appended to `css/site.css` (idempotent LOREFEED block, source `build/lorefeed.css`); feed JS source `build/lorefeed.js` inlined into pages; `sitemap.xml` +8 weekly URLs. Build gate: 280 pages stamped, 0 NOHDR / 0 NOFTR. A daily 6 AM PT scheduled task will append fresh news for approval once this ships.

## 2026-07-29 (Explore card — curated marquee rotation)
- **`js/home-engage.js`**: Replaced the auto-harvested Explore (`.f2-explore`) rotation with a hand-picked marquee set, killing scraped junk (Angle vs Benoit, three Gargano matches, the mangled "Board // Rated 30" hub title). Now rotates: Triple H, The Rock, The Undertaker, Stone Cold profiles; Undertaker vs Michaels (WM25), Rock vs Austin (WM X-Seven), Bret Hart vs Austin (WM13), Undertaker vs Triple H (WM28) matches; plus one live **Watch** card.
- **Watch card opens the theater modal**: the Watch entry reuses a real, build-maintained `.yt[data-yt-id]` video facade already on the page and clicks it, so it opens the shared media.js theater player (embedded YouTube) on the homepage and never goes stale. Falls back to `window.WL.openModal`, then to the video page.
- Every curated href verified to resolve on disk (8/8 pages exist); no invented facts in the copy. `renderCard` now swaps the CTA label to "Watch" and wires the modal for `kind:'watch'`.

## 2026-07-29 (Restructure: /matches/ becomes the hub, /rankings/ becomes a rankings directory)
- **/matches/ is now the matches hub**: the rich video/rankings page (36 matches, random spotlight hero, 32 official embeds, spoiler-safe cards) ported verbatim from /matches/viewing-gallery/, plus a text search (matches wrestler/event/promotion/slug, so "hbk"/"taker" work) and hub SEO (rated + watchable title/meta/keywords/OG; CollectionPage + WebSite + BreadcrumbList + ItemList + FAQ). Replaces the old hand-authored index.
- **/matches/viewing-gallery/ deleted**, 301 to /matches/ via new vercel.json.
- **/rankings/ rebuilt as a rankings hub** (build_rankings_hub.py): 36 greatest matches ranked 1 to 36 from real rank data (top 3 flagged) + a directory of ranked categories (rivalries, events, promotions, wrestlers, moments). Distinct from the /matches/ video gallery; own CollectionPage + ordered ItemList + FAQ + BreadcrumbList.
- Generator idempotency fix: schema strip now includes WebSite/CollectionPage. Files: build/build_rankings.py, build/build_rankings_hub.py (new), css/site.css, js/rankings.js, vercel.json (new). See docs/2026-07-29-matches-hub-rankings-restructure.md.

## 2026-07-29 (Rankings — every-match video + randomized hero)
- **Video coverage 21 to 32 of 36 matches**: added 11 official YouTube embeds (WWE / WWE Vault / WWE NXT), each oEmbed-verified (rights-holder channel + title match). Remaining 4 have no official upload (2 Benoit, Sting/Hogan Starrcade '97, Funk/Sabu ECW) and stay poster cards, no fan re-uploads.
- **Hero rebuilt as a random any-video spotlight**: `build_hero` pool = every match with a video and not `no_hero` (was five-star only); `rankings.js` shuffles and reveals a random 6 per load, so a refresh changes the spotlight. Per-slide badges reflect the real rating (5 / 4.5 / 4 star), not a hardcoded 5-star.
- **Cache-bust fix**: `apply_shell.py::_ver()` now hashes ALL css+js (was 4 files), so `rankings.js` and future JS edits never ship under a stale `?v=`.
- Benoit kept in the grid, excluded from hero (`no_hero`). Files: data/matches.json, build/build_rankings.py, build/apply_shell.py, js/rankings.js, css/site.css. See docs/2026-07-29-rankings-videos-random-hero.md.

## 2026-07-29 (Events hub — Phase 2 complete)
- **`events/index.html` rebuilt as multi-promotion hub**: Replaced the old WWE-only events page with a comprehensive, filterable hub covering WWE, AEW, WCW, ECW, TNA, NJPW, ROH, AAA, NWA, and Indies.
  - Title/meta: `Professional Wrestling Events — Complete History | Wrestle Lore`
  - JSON-LD @graph: BreadcrumbList + CollectionPage + FAQPage (8 GEO-targeted Q&A pairs)
  - Scoped `evhub-*` CSS block: promotion filter pills (11 options), featured flagship event cards (16 cards, `data-promo`), sub-series row grids (9 promotion sections, `data-promo-section`), promotion directory (9 cards), FAQ accordion
  - Filter JS injected: pill toggle + card/section hide/show (`evhub-hidden` class), keyboard-accessible (Enter/Space)
  - Promotion color coding: WWE red, AEW gold, WCW dark red, ECW silver, TNA orange, NJPW red, ROH dark red, AAA green, NWA blue, Indies purple
- **`sitemap.xml` updated**: Added 20 event series URLs with priority (hub at 0.9, flagship series at 0.8, supporting series at 0.7); updated existing `wrestlemania/` and `royal-rumble/` to `monthly` changefreq.
- **`llms.txt` updated**: Added full Events section (16 descriptive links covering all promotions and series pages) for AI crawler / LLM reference.
- **Phase 3 next**: Build individual event series pages in priority order: `events/wrestlemania/`, `events/royal-rumble/`, `events/summerslam/`, `events/survivor-series/`, `events/wcw/`, `events/wcw/starrcade/`, `events/aew/`, `events/aew/double-or-nothing/`, `events/njpw/`, `events/njpw/wrestle-kingdom/`, `events/ecw/`, `events/tna/`, `events/roh/`, `events/aaa/`.

## 2026-07-29 (Events data build — Phase 1 complete)
- **Established `data/events/` content database**: Scraped, sourced, and wrote 10 comprehensive `.md` dossiers covering every major promotion and event in professional wrestling history, plus a master build brief. All files committed to `/data/events/`.
  - `wwe-wrestlemania.md` — WM 1 (1985) through WM 41 (2025), every edition with date, venue, attendance, main event(s), notable matches
  - `wwe-big4-ppvs.md` — Royal Rumble (complete winners table 1988–2026), SummerSlam (1988–2026), Survivor Series (1987–2026) including Montreal Screwjob documentation
  - `wwe-ppv-catalog.md` — All non-Big-4 WWE PPVs: In Your House (27 editions), King of the Ring, No Mercy, Armageddon, Money in the Bank, Hell in a Cell, Elimination Chamber, PLE era (Crown Jewel, Clash at the Castle, Day 1, etc.)
  - `wwe-weekly-tv.md` — Monday Night Raw (Jan 1993–Netflix 2025), SmackDown (Aug 1999–present), NXT + TakeOver series
  - `wcw-events.md` — Starrcade complete table (1983–2000), Great American Bash, Halloween Havoc, SuperBrawl, Bash at the Beach (nWo formation 1996), WCW Nitro/Thunder, Greed (final WCW PPV)
  - `ecw-events.md` — All 21 ECW PPVs chronologically, ECW One Night Stand 2005/2006, ECW WWE brand
  - `aew-events.md` — Big Four (Double or Nothing/All Out/Revolution/Full Gear 2019–2026), All In Wembley, Forbidden Door, WrestleDream, Worlds End, Dynasty, Redemption, Dynamite/Rampage/Collision
  - `tna-impact-events.md` — Bound for Glory complete table (2005–2026, 22 editions), Slammiversary, Lockdown (2005–2014), Impact! era PPVs (Rebellion, Emergence, Over Drive)
  - `njpw-roh-events.md` — Wrestle Kingdom 6–20 (2007–2026), G1 Climax history + legendary matches (Okada vs. Omega 6-star), Dominion, ROH Final Battle/Best in the World/G1 Supercard/Supercard of Honor
  - `aaa-nwa-indie-events.md` — AAA TripleManía I–34 (1993–2026), NWA history + championship lineage (1948–present), PWG (Battle of Los Angeles), PROGRESS, wXw, STARDOM, GCW, EVOLVE, Dragon Gate, CHIKARA
- **`events-build-master-brief.md`**: 4-agent build plan with full URL architecture, hub page IA, UX brief, JSON-LD templates (EventSeries + FAQPage), GEO target phrases per event, sitemap additions, internal linking matrix, robots.txt/llms.txt additions, and 5-phase build roadmap.
- All disputed/estimated figures flagged `⚑` throughout. Sources: Wikipedia, WWE.com, cagematch.net, Wrestling Observer Newsletter, official promotion sites.
- **Phase 2 next**: Build `events/index.html` — comprehensive multi-promotion filterable hub replacing existing WWE-only file.

## 2026-07-28 (Triple H dossier — Integrate → production)
- **Events: shipped `/events/tour/` — "The Road" 2026 tour map** (interactive WWE/AEW/TNA map: scrub/play the caravan across the year, Near-me/Route/Calendar views; Smart Seat Finder with honest deep-links — Ticketmaster primary / SeatGeek resale; "where to sit" ring-sightline guide; On Location premium tier; pricing-trust + notify capture). Wired the native teaser `.card` into `/events/tickets/`, added Events mega-nav rowlinks to `/events/tour/` + `/events/tickets/` (fixes the orphaned tickets page), added both to `sitemap.xml`. `.road`-scoped self-contained CSS; universal shell via apply_shell.py; skip-link set to position:fixed; re-stamped 267 pages.
- Shipped `wrestlers/triple-h/index.html` as the reusable **dossier profile template**: sticky nav stack (mega → sub → id-bar with breadcrumbs, social, Support), gradient Anton hero + roster card, sticky Tale-of-the-Tape rail, tabbed win/loss record (ALL 15 / W 7 / L 8) with sortable Opponent/Event/Time columns, championships ledger, gimmick-era timeline (Terra Ryzing → Jean-Paul Lévesque → HHH → DX → Evolution → King of Kings → Authority → CCO), rivalries, Media & Recent Work (WWE: Unreal S2), fixed "Related superstars" bar, discreet 4.5/10 rating.
- New **scoped** `css/profile.css` (namespaced `.wl-dossier`; recursive audit = 0 leaks, re-audited vs current site.css so its global `.rail`/`.hero`/`.subnav` can't bleed) + `js/profile.js`, loaded only on this page. Head/nav/footer left **byte-identical** to the shell (only 5 intended edits). `site.css`/JS kept at `?v=0fbbcf2b`; `profile.css`/`js` are content-hash-versioned.
- Fixed the shell's **invalid FAQPage JSON-LD** (single quotes + trailing comma → now valid Person + BreadcrumbList + FAQPage; Person carries alternateName **"HHH"** + AggregateRating 4.5/10). Dropped ~190KB of duplicate base64 fonts (site.css already ships them).
- Added `data/triple-h.md` (sourced dossier) and `CLAUDE.md` §6 (keep `data/{slug}.md` updated whenever a wrestler is scraped). Full write-up: `docs/2026-07-28-triple-h-dossier-deploy-session.md`.

- Mini-nav redesigned as a centered nameplate: breadcrumbs moved to the far-left gutter and now scroll away (not sticky-locked); a museum-style vitals line that gracefully collapses on a slower expo-out condense; clearer white social buttons (the SVG paths had no fill and were rendering black); a 6-item Support dropdown (two books, King of Kings apparel, DX gear, Mattel figures, Connor's Cure charity) shown as cards; and the bottom-left match floater removed. profile.css/js re-hashed (v=ce824c1f / 817aa455); index assembled on-device.

## 2026-07-27 (Front page — mobile optimization)
- Fixed the This Week video cards jittering/"moving back and forth" on tap: the `.thisweek .yt__thumb` had a `transform:scale(1.06)` that reflowed the card on `:focus-within` (tap), and the rail used `scroll-snap-type:x mandatory` which snap-yanked it back on iOS. Removed the thumb transform, switched to `scroll-snap-type:x proximity` + `overscroll-behavior-x:contain`. Verified: rail scrollLeft no longer jumps on focus (40→40).
- Killed page-level horizontal scroll. Root cause: the `.tw-layout` grid/flex children lacked `min-width:0`, so the horizontal video rail expanded the page (mobile docW 604→390) instead of scrolling internally. Added `min-width:0` to the layout/detail/panel/rail/list, plus a scoped `#main{overflow-x:clip}` safety net (scoped to the content wrapper so nav dropdowns, which live outside #main, are untouched).
- Added a visible horizontal-scroll affordance: thin gold scrollbar on the video rail, mobile promotion-tabs row, and the ≤1024 nav directory tabs, plus a peeking next card. Sticky-hover guard (`@media (hover:none)`) stops touch taps from latching hover-zoom on `.yt/.tile/.vcard`.
- Shrunk the roster discovery tiles (`.grid-spot .tile`): were 1-up 3:4 posters on mobile (huge). Now 2-up with 1:1 media + smaller watermark on ≤560px; desktop min-column 200→158px (6-up, was 5-up) and aspect 3/4→4/5. Home-only classes, no other pages affected.
- De-duplicated the `.thisweek` styles (were copied both inline in index.html and in site.css); fixed both so the homepage widget and /gallery/ pages stay in sync.
- KNOWN pre-existing (not fixed here, flagged): the mega-nav dropdown panels anchor `left:0` even on right-side tabs, so wide panels (Media/Titles) overflow the right edge at ≤~1440 (desktop docW 1720) — a real desktop h-scroll source that needs a nav-positioning fix + preview.

## 2026-07-27 (Nav — full-bleed bar + "Masthead" wordmark)
- Mega-nav is now full bleed: removed the `.wrap` (max-width 1200px) wrapper from `components/meganav.html` so the bar spans 100vw edge-to-edge; `.nav7 .bar` gets `width:100%` + `padding-inline:clamp(16px,3vw,34px)` for the gutter. Belt still overflows the 62px bar (unchanged).
- New wordmark (Concept C, "Masthead"): belt logo → slim gold vertical divider → big Anton `WRESTLE` over a wide-tracked (.62em) gold Oswald `LORE` subline. Replaces the cramped `.bword--stack` (line-height .86). Real spacing between the two lines.
- Directory tabs restyled airier: Oswald 400 (was 600), letter-spacing .11em (was .06em), 14px (was 13.5). Verified with Playwright at 1440/1280/1152 (all 7 tabs + pill + CTA fit) and 1024 (existing overflow-scroll pattern engages). No console errors.

## 2026-07-27 (Viewing Gallery v3 — YouTube-style theater modal)
- Rebuilt the modal into a two-column layout: velvet-framed player on the left, a right rail with a streaming promo card + promotion tabs (All/WWE/AEW/TNA/NXT) + a scrollable "Keep watching" list. Fixes the top-clipping bug — box is now height-bounded (`max-height:100dvh - headroom`) with the 16/9 frame width-capped to available height, and the close button no longer gets clipped (box `overflow:visible`, extra headroom).
- Modal title is now an `<a>` to the video's own page. Share button copies the clean canonical page URL only (defensive whitespace strip); the earlier bug appended the title text after the slug.
- Autoplay-next: modal iframe gets `enablejsapi`+`origin` on http(s) and registers a YT.Player; on ENDED it advances to the next clip in the active promotion filter (wraps). file:// preview skips the API (avoids error 153) and just plays.
- Promotion normalization: homepage labels promotions with full names ("All Elite Wrestling") while gallery/video pages use short codes ("AEW"). Added `promoCode()` to fold any variant to one canonical code so tabs + autoplay-next behave identically on every page.
- Right-rail items are real `<a href>` to their pages (crawlable, cmd/middle-click opens the page) but left-click swaps the video in-modal (stay-on-site). Streaming card promotes the official platform (Netflix/HBO Max/AMC+) as goodwill. JS/CSS only — no page regen. Verified with Playwright at 1440x820, 1366x670, 390x780: layout, title link, clean share URL, TNA filter isolates 4 clips, close visible at all heights.

## 2026-07-27 (Universal shell — component system, site-wide)
- New `/components/` directory is now the single source of truth for the shell: `meganav.html` (the full nav7 header — 7 tabs + 7 bespoke mega panels + search pill + Join Insider), `footer.html` (the approved FT2 "Directory Grid" fat footer), `palette.html` (#cmdk). Golden rule documented in components/README.md + docs/UNIVERSAL-SHELL.md: edit components, never pages.
- Rewrote build/apply_shell.py as the UNIVERSAL SHELL STAMPER: reads the components at runtime (no more inline constants), home page no longer excluded (its .ticker7 strip sits outside `<header>` and survives). Stamped 226 pages, 0 NOHDR / 0 NOFTR, idempotent. Fixed the header regex to also match `class="site-header nav7"` so re-runs stay stable.
- The nav7 mega nav (Superstars roster dossier, Matches ladder+desk, Events timeline, Promotions grid, HOF Ring of Honor, Titles & Teams belt rack with live reign-day counters, Media studio) is now universal — every page gets the Superstars nav. js/nav.js needed zero changes (already gated on `.nav7`).
- FT2 fat footer CSS added to css/site.css under "UNIVERSAL FOOTER (FT2 directory grid)", self-contained under `.site-footer--fat` (6 -> 3 -> 2 -> 1 column collapse, reduced-motion safe, `p{max-width}` override for the provenance line). Legacy minimal `.site-footer` base kept for /zh/ + /china/.
- Verified with Playwright at 1366x900 + 390x844: wrestler/titles/events/home all render nav + FT2 footer, panels open on hover, ⌘K opens, reign counters live (DAY n), home ticker + floaters intact, no horizontal scroll, footer collapses to 1 col on mobile. Link check: all 125 component hrefs resolve; site-wide scan shows only the 16 pre-existing legacy-wrestler gaps, zero new breaks. Known pre-existing engage.js empty-selector console error on profile pages noted, unchanged.

## 2026-07-26 (Main page v3 — 12-block build + nav7 header, home only)
- Rebuilt index.html per master brief section 5: O-concept header (ticker, full-bleed bar, 7 bespoke mega panels, equal-strap belt rack with live reign-day counters + SVG live-wire champion reveals, AAA/Worlds Collide/El Grande Americano cells) + 12 content blocks with current real data and verified 2026 streaming homes. Home-only scope: CSS namespaced (.nav7/.hv3), self-gated JS, JetBrains Mono self-hosted, apply_shell.py excludes root index.html. Zero broken links, JSON-LD parses, clean console at 1366px.

## 2026-07-26 (Polish + performance sprint)
- H7 Self-hosted fonts: added 7 Latin-subset woff2 (Anton 400, Oswald/Inter 400/600/700, 140KB total) under /fonts/; @font-face + metric-matched fallback faces (size-adjust/ascent-override computed from the real fonts vs Arial) to zero swap CLS. apply_shell.py now strips all Google Fonts preconnect+stylesheet links site-wide and preloads only Anton (the display/LCP font). Verified: 0 third-party font requests, all 7 served locally, Anton/Inter/Oswald all load.
- Q3 Shipped /404.html: full shell + ⌘K search + 8 popular-route tiles; noindex,follow. Stamped by apply_shell (targets() now includes standalone 404.html).
- A11y batch: solid loss badge deepened #e05263->#c23a4a (white contrast 3.8->5.25, AA); 16px form controls <=640px (stops iOS auto-zoom); >=44px touch targets on coarse pointers; forced-colors block so gradient-clipped headlines don't vanish in Windows high-contrast. (focus-visible ring + dim-text lift already present from prior pass.)
- Verified: CSS parses (699 rules), 404 + title/faction/tag-team render at 1366px, no horizontal overflow at 375px, link check unchanged (16 pre-existing legacy-wrestler gaps, zero new).

## 2026-07-26 (Phase 2 — new content types: Titles, Factions, Tag Teams)
- Built 30 new pages via a 4-agent build wave: Titles hub + 11 championship lineages (WWE/World/IC/US/Women's/Tag + WCW/ECW/IWGP/AEW/TNA), Factions hub + 8 stables (nWo, DX, Four Horsemen, Shield, Bloodline, Judgment Day, Bullet Club, Evolution), Tag Teams hub + 8 teams (Hardys, Dudleyz, E&C, New Day, Usos, Hart Foundation, Young Bucks, LOD).
- All reuse existing CSS components (ev-hero/champ-panel/champ-row/grid-cards/faq-block/related-links); zero invented CSS. Every page: title ≤60 ending " | Wrestle Lore", meta 140-160, valid double-quoted JSON-LD (BreadcrumbList everywhere, ItemList on hubs, FAQPage on detail pages), correct canonical, no em-dashes. Cross-links only to existing pages (zero new 404s).
- Wired the three hubs into the mega-nav "More" dropdown (new "Titles & Teams" column); re-stamped shell across 225 pages (fonts/nav/palette/footer). Regenerated sitemap.xml (198 -> 225 URLs) and js/search-index.js (177 -> 207 entries). Render-verified titles/factions/tag-team pages at 1366px.
- Data honesty preserved: reign/champion facts flagged VERIFY (Ripley interim title, IWGP 2026 reactivation, Bloodline/Judgment Day current status) phrased "as reported," not asserted.

## 2026-07-26 (Wrestle Lore revamp — multi-agent)
- Renamed MAT -> Wrestle Lore across the site; unified canonical domain to wrestlelore.com; sitemap 119 -> 198 URLs.
- Ran 30-agent design orchestration (3 workflows): 13 design/brief/tech-lead docs + 7 vision + 10 data docs in docs/design/wrestle-lore/. Master brief resolves 5 cross-spec conflicts; content manifest maps ~211 new pages.
- Phase 0: single-source 7-tab shell (build/apply_shell.py) stamped across ~195 pages; killed 3 forked navs + dead /titles//search/ links.
- Phase 1 (9-agent build): NJPW + AEW, Hall of Fame (AJ Styles headlines 2026 class), current/legends/women hubs, Media + Chris Van Vliet, AJ Styles showcase, 18 champion profiles. Full 7-tab nav lit up.
- Critique wave (8 agents) -> 56-item POLISH-BACKLOG.md. Verified + fixed its P0: 98 wrestler profiles were unstyled (athlete-hero/content-grid/etc. had no CSS) -> added full profile stylesheet.
- UX: faceted filter bar (js/facets.js) on hubs; promotion-tinted cards; engagement layer (js/engage.js) = sticky left scroll-spy rail + "Keep going" bottom rail + Discover floater (Did-you-know facts, Stumble), all reading each page's own links.
- Fixes: rail overlap at 1366/1440 (now >=1600 only); fonts missing on 93 pages (injected); Stone Cold restored to nav Featured; homepage reveal failsafe + real stats (7 promotions / 107 wrestlers); removed fabricated "12,840 waitlist" + AggregateRating counts on 30 match pages (-> honest first-party rating); rebuilt /wrestlers/ roster 41 -> 107 with A-Z filter.

# Changelog — MAT (Pro Wrestling Database)

## 2026-07-26
- Wrestler batches 8–10: upgraded 14 pages to gold-standard 5-feature template (fixed a `wl-strip-wrap` regression across 5 build scripts), then added 20 new profiles (Attitude/Golden Era legends + Kane/Owen Hart/British Bulldog/Edge/Razor Ramon upgrades). 89 wrestler profiles total, all gold-standard.
- Launched **Events** content type: 5 PPV edition pages with real sourced 2026 results (Royal Rumble, Elimination Chamber, WrestleMania 42, Backlash, Night of Champions) + 5 brand hub pages + `/events/` index. Corrected an initial assumption mid-plan — WWE Premium Live Events stream on **ESPN** in the US from 2026 (new deal), not Netflix; Netflix carries the international live feed + US archive. Every event page's watch panel links both correctly. Added `Premium Live Events` column to the homepage's existing Matches mega-nav dropdown (no new top-level tab, per the site's nav rule). New CSS components: `event-hero`, `watch-panel`, `match-card-list`, `event-card`.
- Flagged, not yet resolved: the site has two canonical domains in use — `wrestlelore.com` (README + homepage/promotions/matches templates + sitemap.xml, 791 refs) vs `matdb.io` (all 89 wrestler pages, 400 refs). New Events pages use `wrestlelore.com` to match the sitemap and majority of flagship templates. Needs a single reconciliation pass across the wrestler pages.

## 2026-07-25
- Project kickoff. Wrote master brief (`PROJECT.md`): vision, IA/sitemap, SEO+GEO strategy, China market plan, membership funnel, tech stack.
- Ran 4 parallel research agents → datasets in `/data/` (41 wrestlers + 160+ relationship edges, 30 rated matches, 15 storylines, full design/SEO/GEO/China reference).
- Built single-file design system (`css/site.css`) — dark "arena" theme, mobile-first, all components (cards, rating meters, tale-of-the-tape, mega-nav, embeds/facade, tiers, forms).
- Built `js/main.js` — mobile nav, mega-panel toggles, facade video loader (YouTube+Bilibili), roster search/filter, waitlist form (in-memory, no browser storage).
- Built front page (`index.html`) with full mega-nav, hero featured match, five-star club, icons, relationship teaser, waitlist capture, GEO answer + FAQ.
- Built flagship templates: match page (Undertaker vs HBK WM25), wrestler page (The Undertaker), membership funnel (`membership/`).
- Dispatched builder-agent fleet for the remaining wrestler/match/rivalry/relationship/promotion/China pages, indexes, markdown mirrors, and SEO infra.
- Fleet delivered: 41 wrestler profiles, 30 match pages, 15 rivalries + index, wrestlers/matches/rankings/relationships indexes, 5 promotion hubs + index, about + methodology + growth-strategy, /zh/ + /zh/membership/ + /china/, robots.txt + sitemap.xml (103 URLs) + llms.txt, and /content/ markdown mirror.
- Verified: 104 HTML pages, 0 broken internal links, 0 invalid JSON-LD; rendered desktop + mobile + China screenshots as proof.
- Total: 173 files. Site is deploy-ready (pending real domain, verified video IDs, images, and a live waitlist backend).

## 2026-07-25 (v2 — Broadcast Bold homepage redesign)
- Ran 4 parallel design-research agents (visual, motion, typography, conversion) → playbooks in /data/design-research-*.md.
- Chose art direction: **Broadcast Bold** (ESPN/UFC/DAZN). Type system: Anton (display) + Oswald (condensed UI) + Inter (body).
- Wrote 12 per-section design specs in /docs/design/ (design-system + one per homepage section).
- Upgraded css/site.css (additive, non-breaking): layered "arena spotlight" hero, film-grain overlay, duotone poster tiles + monograms, gradient-border cards, pointer spotlight, metallic-gold shine buttons, marquee ticker, glass stat bar, angled seams, scroll-reveal (gated behind .js so content is visible without JS).
- Added js/enhance.js: scroll-reveal, count-up, hero parallax, card spotlight, sticky header — all reduced-motion + no-JS safe.
- Rebuilt index.html in Broadcast Bold; verified desktop + mobile renders (Google Fonts loaded). Delivered self-contained preview MAT-preview-home-v2.html.

## 2026-07-25 (design + content expansion)
- Design research (4 agents) + 12 per-section design specs (docs/design/) + 3 mega-nav concept previews; chosen direction: CONTROL ROOM (broadcast HUD + ⌘K command palette), spec in docs/design/mega-nav-combined.md.
- UX research (4 agents): nav/IA/search, mobile+a11y, conversion/membership, entity-page UX (data/ux-research-*.md).
- CONTENT EXPANSION (5 agents) in data/expansion-*.md — dedZuped vs existing, cited, 2024–2026-current:
  - +45 wrestlers (total ~86), +35 matches (total ~65), +21 rivalries & +17 factions, +26 events/PPVs & +15 title lineages, +67 glossary terms & +12 family dynasties.
- NOT yet built into pages — this is the source dataset for the next page-generation wave.

## 2026-07-25 (IGBBMN cross-pollination — Undertaker page finished)
- Reviewed the connected IGBBMN MMA project (Next.js). Adapted its best components to MAT's static stack: filterable fight-record table, win/loss result chips, method-breakdown bars, on-page sub-nav, championships panel, career timeline, pull-facts. **Dropped the betting/market module** per request.
- Added the "record system" to css/site.css (additive) + a record-filter to js/enhance.js (accessible, no storage).
- Compiled The Undertaker's verified curated match ledger (data/undertaker-record.md): 28 landmark matches, WrestleMania 25–2, Streak 21–0, 7 world titles, finish breakdown (18 Tombstones). Corrected two online sourcing errors (No Way Out 2006 was a LOSS; 3rd WHC came from CM Punk at HITC 2009).
- Rebuilt wrestlers/the-undertaker/ into the finished, gold-standard profile: record summary, filterable ledger (desktop table + mobile cards), finish bars, championships, timeline, signature matches, rivalries, relationships, FAQ. Now uses Broadcast Bold fonts. Filter verified (Losses → 5).

## 2026-07-25 (UX pass on Undertaker page — 3 UX-designer review agents)
- Ran 3 UX review panels (usability/a11y, visual, engagement/conversion) on the Undertaker page; implemented the high-impact set.
- Fixes: all 28 bouts now reachable on mobile (was 10); sr-only Win/Loss labels; [id]{scroll-margin-top} + sticky thead offset; --c-text-dim lifted for AA contrast; filter chips show per-filter counts; "Streak-ends" tag variant.
- Visual: duotone-monogram hero portrait (was flat initials); metal-gradient summary numbers; zebra + colored result rail on the table; finish bars animate on reveal; win/loss sparkline of the 28-bout arc; is-gold stat wash; "The Streak" sub-nav anchor.
- Engagement (static, no betting): "Rate the Deadman" 5-star widget (join-to-save), share-the-Streak button (Web Share API), Follow, and a "Guess the Legend" teaser → funnel; all fire console intent events for analytics.
- Workflow: delivering self-contained .html previews (not PNGs) going forward.

## 2026-07-25 (Undertaker deep build — tabs, alter egos, media)
- Added a tabbed record to the Undertaker page: **Landmark ledger (28) / WrestleMania (25–2, all 27) / PPV·PLE (curated ~30)**, each in its own scrollable area (inner scroll). Complete WM record + curated PPV record + Royal Rumble stats compiled & verified (data/undertaker-records-expanded.md).
- Created alter-ego profile pages (SEO-optimized, cross-linked, schema): **/wrestlers/mean-mark-callous/** (WCW 1989–90) and **/wrestlers/the-american-badass/** (biker era 2000–03). Added a "Personas" section + Person alternateName/sameAs linking them (data/undertaker-personas-media.md).
- Added **Documentaries & Shows** and **Podcasts** sections with sticky-label rails + TVSeries/PodcastSeries schema (The Last Ride, Biography A&E, Broken Skull Sessions, Escape the Undertaker, Six Feet Under, etc.).
- Tab + scroll UI added to css/site.css; tab keyboard/ARIA logic in js/enhance.js. Verified: 0 broken links, tabs switch, WM=27 rows, PPV=30 rows.
- 2026-07-29: Recovered the sparkle-engine CSS swept out by the footer redesign (lore gem, sale spin, live radar, hover glows) — fixes the Lore Feed gem rendering as a plain dot and the ticket floater sparkle not spinning. Fixed mobile horizontal scroll site-wide (footer brand nowrap + clamp, min-width 0, html overflow-x clip; verified 0px at 320/360/390 on six page types). Lore Feed is now a real page at /lore-feed/ (renamed from the dead /ring-feed/ slug) and featured as a live row with the gem glyph at the top of the Media dropdown.
- 2026-07-29 — Nav Superstars→Wrestlers; Surprise Me → Lore Wrestler/Lore Match (animated icons, approved Undertaker fact kept); Explore floater collapses to a hover-expand ticket stub and rebranded from five-star to Explore (kicker/stars/sparkle stripped); restamp.
- 2026-07-29 — Home floaters round 2: 14 rotating curated Did-You-Know facts + a fresh Explore card on every hover; Explore gleam refined to a gold edge-light; site back-to-top hidden on home; restamp.
- 2026-07-29 — Lore Feed ticker made universal: moved .ticker7 markup into the stamped nav, .rt CSS into site.css, rotator into nav.js; sticky on top of every page (was home-only); restamp.
- 2026-07-29 — Ticker LIVE mark: swapped the red pulsing dot for a custom green animated "Orbit Signal" SVG (chosen from 3); moved inline .rt CSS fully into site.css.
- 2026-07-29 — Match pages: winner hidden behind a tap-to-reveal VS card + blurred result/FAQ (spoiler-safe, full text stays in the DOM for SEO/GEO), and the video area now plays a real verified embed in the site's modal instead of linking out to a YouTube search. Rolled out to all 30 /matches/ pages (26 real embeds, 4 honest watch-elsewhere links) via a new idempotent build/build_match_kit.py + css/matchkit.css + js/matchkit.js (site.css untouched).
