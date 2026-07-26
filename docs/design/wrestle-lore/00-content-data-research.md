# Wrestle Lore — Content & Data Research Spec

Research analyst deliverable for the Direction-B poster-wall revamp. Every fact below carries a
source note and a confidence flag. Rule followed: no fabricated facts, quotes, or stats; anything
uncertain is flagged `VERIFY`. All internal links map to pages that already exist under
`/root/wwe/` unless listed in the Gap List.

- Date of research: 2026-07-26
- Confidence legend: `HIGH` = multiple/authoritative sources agree; `MED` = single reputable source or subject to change; `VERIFY` = must be confirmed before publishing.

---

## 1. Streaming & Broadcast Homes (Requirement 4)

Use this table to build the brand cards ("where each streams"). US + international columns.

| Promotion | Weekly TV (US) | PLE/PPV / Streaming (US) | International | Confidence | Source |
|---|---|---|---|---|---|
| **WWE Raw** | Netflix (Mondays 8/7c) — exclusive since Jan 2025 | Netflix | Netflix (most non-US regions) | HIGH | wwe.com/article/how-to-watch; Forbes 2026-01-14 |
| **WWE SmackDown** | USA Network (Fridays 8/7c) | Past episodes migrate to Netflix | Netflix | HIGH | wwe.com; Forbes 2026-01-14 |
| **WWE NXT** | The CW (Tuesdays 8/7c) | The CW / archives on Netflix | Netflix | HIGH | wwe.com; Forbes 2026-01-14 |
| **WWE Premium Live Events** (WrestleMania, Royal Rumble, SummerSlam, Survivor Series, etc.) | n/a | **ESPN app / ESPN DTC** — exclusive US home starting 2026 | Netflix (international) | HIGH | ESPN Press Room 2025-08; CNBC 2025-08-06; Forbes 2026-01-14 |
| **AEW Dynamite** | TBS (Wednesdays 8-10 ET) | HBO Max (simulcast + replays) | AEW Plus on TrillerTV | HIGH | HBO Max /aew; Forbes 2026-01-14 |
| **AEW Collision** | TNT (Saturdays 8-10 ET) | HBO Max | AEW Plus on TrillerTV | HIGH | tntdrama.com; HBO Max; Forbes |
| **AEW PPVs** | n/a | Traditional PPV, TrillerTV, Amazon, HBO Max | TrillerTV | MED | Forbes 2026-01-14 |
| **NJPW (New Japan)** | n/a (US) | **NJPW World** (own subscription, njpwworld.com); TrillerTV; some cards on YouTube/YouTube TV | NJPW World (global); TV Asahi in Japan | HIGH | njpwworld.com; F4W guide; TrillerTV |
| **TNA Wrestling** | **AMC** (Thursday Night iMPACT, Thu 9-11 ET, from Jan 15 2026) | AMC+; **TNA+** (own subscription); older iMPACT seasons on Amazon Prime Video | TNA+ + intl partners | HIGH | Yahoo Sports 2026 TNA deal; Media Play News; primevideo.com listings |
| **WCW (legacy)** | Defunct (folded 2001) | Library owned by WWE; available via WWE's streaming archive (historically Peacock US; migrating to Netflix) | Netflix | MED / VERIFY US home | WWE owns WCW library (well established); exact 2026 US archive host = VERIFY |
| **ECW (legacy)** | Defunct (folded 2001) | Library owned by WWE; same archive path as WCW | Netflix | MED / VERIFY | same as above |

### Answer to the user's direct question: "Is TNA on Amazon?"
Partially. TNA's **live/current 2026 home is AMC + AMC+**, plus its own **TNA+** subscription service.
Separately, **older TNA iMPACT! seasons are listed on Amazon Prime Video** (e.g. "TNA iMPACT! Season 26").
So: current weekly show = AMC/AMC+/TNA+, and Amazon carries back-catalog/library seasons, not the
live AMC broadcast. Confidence HIGH; recommend the brand card say "AMC & AMC+ (live), TNA+ (streaming),
library seasons on Prime Video."

### Card copy building blocks (no banned words, specific nouns)
- WWE: "Raw streams on Netflix. SmackDown airs on USA Network. Premium Live Events run on ESPN in the US and Netflix internationally."
- AEW: "Dynamite on TBS, Collision on TNT, both on HBO Max. International fans use AEW Plus on TrillerTV."
- NJPW: "Watch on NJPW World, the promotion's own subscription, plus TrillerTV."
- TNA: "Thursday Night iMPACT on AMC and AMC+, with TNA+ for the full library."

---

## 2. WWE Hall of Fame Showcase (Requirement 6)

### Last 5 induction classes (headline inductees)

| Class | Headline inductee(s) | Notable co-inductees | Existing page? | Confidence | Source |
|---|---|---|---|---|---|
| **2025** | **Triple H** | Lex Luger, Michelle McCool, The Natural Disasters | Triple H ✓ (`/wrestlers/triple-h/`), Lex Luger ✓ (`/wrestlers/lex-luger/`) | HIGH | wwe.com 2025 HOF recap; SI list |
| **2024** | **Paul Heyman** | Bull Nakano, U.S. Express, Muhammad Ali (celebrity), Thunderbolt Patterson, Lia Maivia | none of headliners | HIGH | SI list |
| **2023** | **Rey Mysterio** | The Great Muta, Andy Kaufman (celebrity), Stacy Keibler | Rey Mysterio ✓ (`/wrestlers/rey-mysterio/`) | HIGH | SI list |
| **2022** | **The Undertaker** | Vader, Queen Sharmell, The Steiner Brothers | Undertaker ✓ (`/wrestlers/the-undertaker/`), Vader ✓ (`/wrestlers/vader/`) | HIGH | SI list |
| **2021** | **Kane** | Molly Holly, Eric Bischoff, The Great Khali, Rob Van Dam | Kane ✓ (`/wrestlers/kane/`) | HIGH | SI list |

### Most-decorated inductee (multi-time inductions)
- **Ric Flair — two-time WWE Hall of Famer** (confirmed). Individual induction **2008**; second induction **2012 as a member of the Four Horsemen**. Page exists: `/wrestlers/ric-flair/`. Confidence HIGH (SI list flags "2nd time for Ric Flair" in 2012).
- Other confirmed multi-time inductees to note as "elite two-timers" club:
  - **Shawn Michaels** — 2011 (solo) + 2019 (D-Generation X). Page ✓ `/wrestlers/shawn-michaels/`.
  - **Booker T** — 2013 (solo) + 2019 (Harlem Heat). Page ✓ `/wrestlers/booker-t/`.
  - **Scott Hall** — 2014 (solo) + 2020 (nWo). Page ✓ as `/wrestlers/razor-ramon/` (his WWE persona).
  - **Kevin Nash** — 2015 (solo) + 2020 (nWo). Page ✓ as `/wrestlers/kevin-nash/` (also `/diesel/`).
  - **Hulk Hogan** — 2005 (solo) + 2020 (nWo). Page ✓ `/wrestlers/hulk-hogan/`.
  - **Barry Windham** — 2012 (Four Horsemen) + 2024 (U.S. Express). No page.
  - Note: exact solo-induction years for Hall/Booker/Michaels above are MED — VERIFY the specific years before printing them on the card. The two-time status itself is HIGH.

### Showcase design note
Feature **Ric Flair as the "most-decorated"** hero panel (2x HOF, gold accent), backed by a
"Two-Time Club" strip (Michaels, Booker T, Hall, Nash, Hogan) — all link to existing pages. Then a
"Last 5 Classes" row (2021-2025) with the headline inductee tile linking to existing pages where
available (Kane, Undertaker/Vader, Rey Mysterio, Triple H/Lex Luger).

---

## 3. AJ Styles Showcase (Requirement 5)

Existing page: `/wrestlers/aj-styles/` (already references NJPW x6, Bullet Club x4, TNA x18, "Phenomenal" x9).

| Fact | Detail | Confidence | Source |
|---|---|---|---|
| Nickname | "The Phenomenal One" | HIGH | multiple |
| TNA run | Longtime TNA franchise player; multi-time TNA/NWA World Champion; original "face" of TNA | HIGH | wrestlingprofiles; TNA history |
| NJPW run | Leader of the original **Bullet Club**; **IWGP Heavyweight Champion**; headlined Wrestle Kingdom | HIGH | NJPW records; wrestlingprofiles |
| WWE run | Debuted 2016 Royal Rumble; **multi-time WWE Champion** and US Champion; feuds with Cena, Nakamura, Reigns | HIGH | wwe.com; wrestlingprofiles |
| Signature | Styles Clash; Phenomenal Forearm; Calf Crusher | HIGH | multiple |
| **Career status** | **Reported to have retired at Royal Rumble 2026** | **VERIFY** (single-source: SEScoops headline) | sescoops.com/aj-styles-retiring |

Design note: AJ Styles is the perfect "three-promotion journey" hero (TNA -> NJPW/Bullet Club -> WWE),
which also justifies adding NJPW. If the retirement is confirmed, frame as a career-retrospective
showcase; until confirmed, do NOT state he retired. Flag `VERIFY` on the card.

---

## 4. Add NJPW as a Promotion (Requirement 5)

- `/promotions/njpw/` does **NOT** exist yet (current promotions: wwe, wcw, ecw, tna, nxt). **GAP — must be built.**
- Suggested brand accent color: NJPW crimson/red (distinct from WWE #c8102e). Propose **#c1272d** or a
  deep red-black; VERIFY brand palette against official NJPW branding before finalizing.
- Card facts: founded 1972; largest promotion in Japan; flagship event **Wrestle Kingdom** (Tokyo Dome, Jan 4);
  top title **IWGP World Heavyweight Championship**; streams on **NJPW World** + TrillerTV. Confidence HIGH.
- Cross-link to existing roster with NJPW ties: **AJ Styles** (Bullet Club), **Shinsuke Nakamura**
  (`/wrestlers/shinsuke-nakamura/`), **Jon Moxley** (`/wrestlers/jon-moxley/`, IWGP US champ history),
  **Finn Balor** (`/wrestlers/finn-balor/`, original Bullet Club leader "Prince Devitt"),
  **Kenny Omega** (no page — gap), **Will Ospreay** (no page — gap).

---

## 5. Wrestler Category Taxonomy (Requirements 1, 2)

Proposed multi-axis tag system. Each existing wrestler slug gets tags on all four axes so the poster
wall can filter and create many colored category tiles.

### Axis A — Status: CURRENT vs LEGEND
- **CURRENT (active 2026, ~30):** asuka, bayley, becky-lynch, bianca-belair, bobby-lashley,
  charlotte-flair, cm-punk, cody-rhodes, damian-priest, drew-mcintyre, finn-balor, gunther, iyo-sky,
  john-cena (retirement tour — flag), jon-moxley, kevin-owens, la-knight, liv-morgan, mercedes-mone,
  natalya, randy-orton, rey-mysterio, rhea-ripley, roman-reigns, sami-zayn, samoa-joe, seth-rollins,
  sheamus, shinsuke-nakamura. (aj-styles = CURRENT pending retirement VERIFY.)
- **LEGEND (retired/inactive/historic, ~50):** andre-the-giant, arn-anderson, bam-bam-bigelow,
  batista, big-show, booker-t, bret-hart, brian-pillman, british-bulldog, brock-lesnar, bully-ray,
  chris-benoit, chris-jericho, christian, christopher-daniels, chyna, daniel-bryan,
  diamond-dallas-page, diesel, dusty-rhodes, eddie-guerrero, edge, goldberg, goldust, hulk-hogan,
  jake-roberts, jeff-hardy, kane, kevin-nash, kurt-angle, lex-luger, lita, matt-hardy, mick-foley,
  mr-perfect, owen-hart, randy-savage, razor-ramon, ric-flair, rick-rude, ricky-steamboat,
  roddy-piper, savio-vega, shawn-michaels, sting, stone-cold-steve-austin, sycho-sid, ted-dibiase,
  the-rock, the-undertaker, triple-h, trish-stratus, vader, yokozuna.
- **PERSONA/ALIAS pages (do not double-count as people):** mean-mark-callous, the-american-badass,
  the-ringmaster, stunning-steve-austin (Austin/Undertaker gimmick pages); diesel + razor-ramon are
  WWE personas of Nash/Hall. Treat as redirects/cross-links, not roster tiles.
- **NON-WRESTLER:** vince-mcmahon (executive/authority) — surface under "More" or a Personalities lane, not the athlete grid.

### Axis B — Gender division: FEMALE vs MALE
- **FEMALE (13):** asuka, bayley, becky-lynch, bianca-belair, charlotte-flair, chyna, iyo-sky, lita,
  liv-morgan, mercedes-mone, natalya, rhea-ripley, trish-stratus.
- **MALE:** all other roster people.

### Axis C — Primary promotion (accent color drives the tile)
Tag each with home promotion(s) for colored grouping: WWE #c8102e, WCW #e2b13c, ECW #b0b0b0,
TNA #1e73be, NXT #f5c518, **NJPW (new) VERIFY red**. Many wrestlers carry 2+ (e.g. Sting = WCW+TNA+WWE;
AJ Styles = TNA+NJPW+WWE; Chris Jericho = WCW+ECW+WWE+AEW).

### Axis D — Division / Era (browse-y categories)
- **Eras:** Golden Era (80s), New Generation (early 90s), Attitude Era (late 90s), Ruthless
  Aggression (2000s), Reality/PG Era (2010s), Modern (2020s).
- **Divisions:** Heavyweight/Main Event, Women's Division, Tag Team, Cruiserweight/High-Flyer,
  Faction (Four Horsemen, nWo, DX, The Shield, Bloodline, Bullet Club).

This yields many colored, clickable category lanes (e.g. "Attitude Era", "Women's Legends",
"Bullet Club", "WCW Icons", "Current NXT") for the addictive browse goal (Requirement 9).

---

## 6. Influencers / Media Roster (Requirement 7)

Proposed tab = "Media & Creators" (wrestling media personalities, interviewers, podcasters, YouTubers).
Flag: these are MEDIA people, distinct from active wrestlers. None currently have pages (all GAP).

| Name | One-liner | Media or Wrestler? | Confidence | Source |
|---|---|---|---|---|
| **Chris Van Vliet** | Emmy-winning host of the "Insight" interview podcast/YouTube; premier long-form wrestler interviewer | MEDIA | HIGH | en.wikipedia.org/wiki/Chris_Van_Vliet; podcast.chrisvanvliet.com |
| **Sami Zayn** | **Active WWE wrestler** — the user mentioned him; he is a performer, not media. Keep on the athlete grid, not this tab. | WRESTLER (has page `/wrestlers/sami-zayn/`) | HIGH | wwe.com |
| **Renee Paquette** | Broadcaster/interviewer (ex-WWE, AEW); host of "The Sessions" podcast | MEDIA | MED / VERIFY current role | widely reported |
| **Peter Rosenberg** | Radio host and WWE/wrestling media personality | MEDIA | MED / VERIFY | widely reported |
| **Ariel Helwani** | Combat-sports journalist who covers wrestling; interviews top stars | MEDIA | MED / VERIFY | widely reported |
| **Sean Ross Sapp (Fightful)** | Wrestling news reporter/insider | MEDIA | MED / VERIFY | widely reported |
| **Denise Salcedo** | Wrestling interviewer/YouTuber | MEDIA | MED / VERIFY | widely reported |
| **Wade Keller / Dave Meltzer** | Veteran wrestling journalists (PWTorch / Wrestling Observer; Meltzer = the star-rating source) | MEDIA | MED / VERIFY | widely reported |

Design note: Populate the tab with **Chris Van Vliet as the hero** (confirmed HIGH) plus a proposed
grid of the MED entries, each carrying a `VERIFY` flag until each personality's current affiliation is
confirmed. Do NOT put Sami Zayn here — he is an active wrestler; explain that in the spec-to-design
handoff so the team routes the user's mention correctly.

---

## 7. PPV / Event Separation (Requirement 3)

Existing events: 5 PPV editions (backlash-2026, elimination-chamber-2026, night-of-champions-2026,
royal-rumble-2026, wrestlemania-42-2026) + 5 brand hubs (backlash, elimination-chamber,
night-of-champions, royal-rumble, wrestlemania). All under `/events/`.

Proposed separation facets for the poster wall:
- **By promotion:** WWE / WCW / ECW / TNA / NJPW (as pages get built).
- **By year:** 2026 hub now; structure for multi-year archive (e.g. `/events/royal-rumble/` = all editions).
- **By brand/series:** Big Four (Royal Rumble, WrestleMania, SummerSlam, Survivor Series) vs monthly PLEs.
- **Streaming badge on each event card:** WWE PLE = "ESPN (US) / Netflix (intl)" per section 1.

Gap: only WWE 2026 events exist; WCW/ECW/TNA/NJPW event pages are all gaps if the design wants
cross-promotion event separation.

---

## 8. Gap List — Requested entities WITHOUT a page yet

Build or stub these so the design's clickables don't 404:

- **NJPW promotion page** `/promotions/njpw/` — REQUIRED (Requirement 5).
- **Media & Creators pages:** Chris Van Vliet + any media roster chosen (all new).
- **HOF headliners missing pages:** Paul Heyman (2024), The Great Muta (2023), Eric Bischoff / Rob Van Dam / Molly Holly / The Great Khali (2021), Michelle McCool / The Natural Disasters (2025), Queen Sharmell / Steiner Brothers (2022), Bull Nakano / U.S. Express / Barry Windham (2024).
- **NJPW-tied stars missing pages:** Kenny Omega, Will Ospreay.
- **Note:** HOF classes with existing pages that CAN link now: Kane, Undertaker, Vader, Rey Mysterio, Triple H, Lex Luger, Ric Flair, Shawn Michaels, Booker T, Hulk Hogan, Razor Ramon (Scott Hall), Kevin Nash.

---

## 9. Site Rename (Requirement 8)
"MAT" -> **"Wrestle Lore"** across all pages, `<title>`, meta, nav brand, llms.txt, sitemap, JSON-LD
`name`, and social/OG tags. (Implementation task; flagged here so the content spec uses the new name.)

---

## Consolidated Source List
- WWE how-to-watch: https://www.wwe.com/article/how-to-watch
- Forbes 2026 TV deals: https://www.forbes.com/sites/brianmazique/2026/01/14/wwe-aew-and-tna-tv-deals-explained-how-to-watch-wrestling/
- ESPN Press Room (WWE PLE deal): https://espnpressroom.com/us/press-releases/2025/08/espn-wwe-reach-landmark-rights-agreement...
- CNBC ESPN/WWE deal: https://www.cnbc.com/2025/08/06/espn-wwe-five-year-deal-live-events.html
- Yahoo TNA TV deal (AMC, Jan 15 2026): https://sports.yahoo.com/articles/tna-wrestling-inks-major-tv-171938734.html
- Media Play News (AMC+ / TNA): https://www.mediaplaynews.com/new-amc-networks-deal-with-tna-wrestling-includes-streaming-on-amc-plus/
- TNA iMPACT! on Prime Video: https://www.primevideo.com/detail/0JUDFWRZQVXA7XUGHXAN08F1NQ
- HBO Max AEW: https://www.hbomax.com/aew
- NJPW World: https://www.njpwworld.com/ ; F4W how-to-watch NJPW: https://www.f4wonline.com/event-guides/how-can-i-watch-njpw-us-full-guide-new-fans/
- SI WWE HOF list: https://www.si.com/fannation/wrestling/wwe-hall-of-fame-list-and
- WWE 2025 HOF recap: https://www.wwe.com/shows/wwe-hall-of-fame/2025/article/recap
- Chris Van Vliet: https://en.wikipedia.org/wiki/Chris_Van_Vliet
- AJ Styles retirement (VERIFY): https://www.sescoops.com/aj-styles-retiring
