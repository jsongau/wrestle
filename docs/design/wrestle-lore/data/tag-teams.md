# Wrestle Lore — Tag Teams Dataset

Page-ready, verified dataset for the new Tag Teams section. The build phase turns each entry below
into a page at the route pattern `/tag-teams/{slug}/`. Every card links members to existing
`/wrestlers/{slug}/` pages where they exist; members without a profile are collected in the Gap List
so no clickable 404s.

- Researcher role: Tag Teams
- Date of research: 2026-07-26
- Rule followed: no invented facts, quotes, or stats. Anything time-sensitive or single-source is flagged.
- Confidence legend: `HIGH` = multiple authoritative sources agree; `MED` = single reputable source or subject to change; `VERIFY` = confirm before publishing.
- Copy standard: specific nouns, no decorative arrows, no em-dash separators, no filler adjectives.

## Route pattern

- Section index: `/tag-teams/`
- Team page: `/tag-teams/{slug}/`
- Each member name on a team page links to `/wrestlers/{member-slug}/` when that page exists.
- Reverse cross-link: each existing wrestler page should gain a "Tag Teams" strip linking to `/tag-teams/{slug}/`.
- Disambiguation note: two slugs (`hart-foundation`, `legion-of-doom`) also appear in the Factions
  dataset at `/factions/{slug}/`. The tag-team page covers the wrestling duo; the faction page covers
  the larger stable version. Cross-link the two, do not merge them. Recommend the tag-team route keep
  `hart-foundation` and `legion-of-doom` and have the faction page point to it.

---

## Master index table

| Team | Slug | Members | Promotion(s) | Era (active) | Confidence | Existing member pages |
|---|---|---|---|---|---|---|
| The Hardy Boyz | `hardy-boyz` | Matt Hardy, Jeff Hardy | WWF/WWE, TNA/IMPACT, ROH, AEW | 1998-present (on/off) | HIGH | matt-hardy, jeff-hardy |
| The Dudley Boyz | `dudley-boyz` | Bubba Ray Dudley, D-Von Dudley | ECW, WWF/WWE, TNA, NJPW | 1996-2016 (on/off) | HIGH | bully-ray |
| Edge and Christian | `edge-and-christian` | Edge, Christian | WWF/WWE | 1998-2001 | HIGH | edge, christian |
| The New Day | `the-new-day` | Kofi Kingston, Xavier Woods, Big E | WWE | 2014-2025 | HIGH | (none) |
| The Usos | `the-usos` | Jimmy Uso, Jey Uso | WWE | 2010-2024 (as a full-time team) | HIGH | (none) |
| The Hart Foundation | `hart-foundation` | Bret Hart, Jim "The Anvil" Neidhart | WWF | 1985-1991 | HIGH | bret-hart |
| Legion of Doom (Road Warriors) | `legion-of-doom` | Road Warrior Hawk, Road Warrior Animal | AWA, NWA/WCW, WWF | 1983-2003 (across runs) | HIGH | (none) |
| The Young Bucks | `young-bucks` | Matt Jackson, Nick Jackson | ROH, NJPW, PWG, AEW | 2004-present | HIGH | (none) |
| The Brothers of Destruction | `brothers-of-destruction` | The Undertaker, Kane | WWF/WWE | 1997-2020 (on/off) | HIGH | the-undertaker, kane |
| The Steiner Brothers | `steiner-brothers` | Rick Steiner, Scott Steiner | NWA/WCW, WWF, NJPW | 1989-2000s (on/off) | HIGH | (none) |
| The British Bulldogs | `british-bulldogs` | Davey Boy Smith, Dynamite Kid | WWF, Stampede, NJPW | 1984-1988 | HIGH | british-bulldog |
| Demolition | `demolition` | Ax, Smash (later Crush) | WWF | 1987-1991 | HIGH | (none) |
| The Rockers | `the-rockers` | Shawn Michaels, Marty Jannetty | AWA, WWF | 1985-1992 | HIGH | shawn-michaels |
| The Rock 'n' Sock Connection | `rock-n-sock-connection` | The Rock, Mankind (Mick Foley) | WWF | 1999 | HIGH | the-rock, mick-foley |
| The Outsiders | `the-outsiders` | Scott Hall, Kevin Nash | WCW | 1996-1999 | HIGH | razor-ramon, kevin-nash |
| The Brain Busters | `brain-busters` | Arn Anderson, Tully Blanchard | NWA, WWF | 1988-1989 | HIGH | arn-anderson |
| FTR | `ftr` | Cash Wheeler, Dax Harwood | WWE (as The Revival), AEW, NJPW, ROH | 2014-present | HIGH | (none) |
| The Bloodline (Usos-era tag) | see `/factions/the-bloodline/` | Jimmy Uso, Jey Uso, Solo Sikoa | WWE | 2020-present | HIGH (as faction) | (none) |

Cross-reference: faction-scale groups (The Bloodline, The Judgment Day, nWo) live in
`data/factions-stables.md` at `/factions/{slug}/`. This dataset covers two-man tag teams. The Usos
appear in both, tagged as a duo here and as part of the Bloodline stable there.

---

## 1. The Hardy Boyz — `/tag-teams/hardy-boyz/`

| Field | Detail |
|---|---|
| Members | Matt Hardy (`matt-hardy`), Jeff Hardy (`jeff-hardy`) |
| Promotions | WWF/WWE, TNA/IMPACT, Ring of Honor, AEW |
| Era | Debuted as a regular WWF team in 1998; multiple reunions through the 2010s and 2020s |
| Titles | Multi-time WWF/WWE World Tag Team and WWE Tag Team Champions; also held tag gold in TNA and ROH |
| Signature match | The ladder and TLC (Tables, Ladders and Chairs) matches against Edge and Christian and the Dudley Boyz. The three teams built the TLC concept together |
| Signature moves | Poetry in Motion; the Swanton Bomb (Jeff) off ladders and cages |
| Why it mattered | Real-life brothers who turned high-risk ladder spots into a main-event draw and helped define the Attitude Era tag division |
| Confidence | HIGH on team status, TLC legacy, brother relationship. MED on exact championship totals across every promotion (VERIFY final counts before printing numbers) |
| Cross-links | Rivalry with Edge and Christian and the Dudley Boyz; both members have solo pages |

Source notes: WWE.com Hardy Boyz profile and video library; Bleacher Report "Top 5 Hardy Boyz PPV
Matches"; Last Word on Pro Wrestling "20 Years Ago" TLC retrospective.

---

## 2. The Dudley Boyz — `/tag-teams/dudley-boyz/`

| Field | Detail |
|---|---|
| Members | Bubba Ray Dudley (`bully-ray`), D-Von Dudley (no page) |
| Promotions | ECW, WWF/WWE, TNA (as Team 3D), NJPW |
| Era | ECW breakout 1996-1999; WWF/WWE run 1999-2005; TNA/IMPACT as Team 3D 2005-2014; WWE return 2015-2016 |
| Titles | Most-decorated tag team in WWE/WWF, WCW and ECW combined by championship count; multi-time WWE World Tag Team Champions; ECW Tag Team Champions; TNA/NWA Tag Team Champions |
| Signature moves | The 3D (Dudley Death Drop); "Get the tables" and the powerbomb through the table |
| Why it mattered | Carried the ECW hardcore tag style into the mainstream and completed the three-team TLC trilogy with the Hardyz and Edge and Christian |
| Confidence | HIGH on team, ECW origin, TLC role. MED on exact combined title count (VERIFY the "most decorated" claim's specific number) |
| Cross-links | Bubba Ray solo page as `bully-ray`; D-Von is a Gap-List entry |

Source notes: WWE.com Dudley Boyz profile; ECW history records; WWE SummerSlam 2000 TLC video listing.

---

## 3. Edge and Christian — `/tag-teams/edge-and-christian/`

| Field | Detail |
|---|---|
| Members | Edge (`edge`), Christian (`christian`) |
| Promotion | WWF/WWE |
| Era | Regular team 1998-2001, before both became singles main-eventers |
| Titles | Multi-time WWF World Tag Team Champions; won the first-ever Tag Team Ladder and TLC bouts |
| Signature spots | The five-second pose; the con-chair-to; ladder-match specialists |
| Why it mattered | The comedic-heel foil in the Attitude Era tag trilogy; both men went on to WWE and Hall of Fame singles careers |
| Confidence | HIGH on team and TLC legacy. MED on exact tag-title reign count |
| Cross-links | Rivalry with Hardy Boyz and Dudley Boyz; both members have solo pages; Christian and Edge are real-life best friends since childhood |

Source notes: WWE.com video "Edge and Christian vs Hardy Boyz vs Dudley Boyz TLC SummerSlam 2000";
TJR Wrestling WrestleMania 17 review.

---

## 4. The New Day — `/tag-teams/the-new-day/`

| Field | Detail |
|---|---|
| Members | Kofi Kingston, Xavier Woods, Big E (all no page) |
| Promotion | WWE |
| Era | Debuted November 2014; ran as a trio through the 2010s and early 2020s |
| Titles | Record-tying multi-time WWE/Raw/SmackDown Tag Team Champions; held tag gold eleven times as a group across the three men (four of those as the Kingston and Woods duo per Fox Sports) |
| Reign record | Once held the longest single reign in WWE Tag Team Championship history (483 days, 2016-2017) before the Usos passed it |
| **Verified 2026 development** | Kingston and Woods were **released by WWE on May 3, 2026** and moved to the alumni section. Big E had already stopped in-ring competition after a 2022 neck injury. The full-time New Day run is over. Frame as a retrospective, do not present them as an active WWE act |
| Why it mattered | Turned positivity, unicorn horns and the Booty-O's gimmick into one of the most merchandised acts of the 2010s; Kingston's 2019 WrestleMania 35 WWE Championship win ("KofiMania") grew out of the group |
| Confidence | HIGH on the group, the reign record and the May 3, 2026 release. MED on the exact all-time title count (VERIFY the number before printing) |
| Cross-links | All three members are Gap-List entries; also referenced in `data/factions-stables.md` (`the-new-day`) |

Source notes: Fox News/Fox Sports "Legendary WWE tag team duo departs company" (May 2026);
Yahoo Sports "New Day's Kofi Kingston and Xavier Woods split from WWE" (May 2026); Wikipedia "The New
Day (professional wrestling)"; WWE.com. Confidence HIGH on the departure (multiple outlets, same date).

---

## 5. The Usos — `/tag-teams/the-usos/`

| Field | Detail |
|---|---|
| Members | Jimmy Uso, Jey Uso (both no page) |
| Promotion | WWE |
| Era | Main-roster debut 2010; anchored the SmackDown and Raw tag divisions through 2023 |
| Titles | Multi-time WWE/Raw/SmackDown Tag Team Champions; first Undisputed WWE Tag Team Champions after unifying the SmackDown and Raw titles in 2022 |
| **Reign record** | Longest reigning tag team champions in WWE history at **622 days** (July 18, 2021 to April 1, 2023, WrestleMania 39 Night 1), surpassing the New Day's record |
| Family | Sons of Rikishi; part of the Anoa'i family; cousins of Roman Reigns; core of The Bloodline |
| Why it mattered | The most decorated modern WWE tag team; Jey Uso's 2023-2025 Bloodline split fueled a breakout singles run |
| Confidence | HIGH on team, 622-day record and Bloodline ties. Both members work heavily as singles acts as of 2026, so "active full-time team" is MED/VERIFY |
| Cross-links | Both are Gap-List entries; The Bloodline lives at `/factions/the-bloodline/` with `roman-reigns` and `sami-zayn` pages |

Source notes: Fightful "The Usos officially become longest-reigning WWE Tag Team Champions" and "first
tag team to surpass 600-day reign"; SEScoops; Bleacher Report; Wikipedia "The Usos" and "Jimmy Uso".
The 622-day figure is widely reported (HIGH).

---

## 6. The Hart Foundation — `/tag-teams/hart-foundation/`

| Field | Detail |
|---|---|
| Members | Bret "Hitman" Hart (`bret-hart`), Jim "The Anvil" Neidhart (no page); managed by Jimmy Hart |
| Promotion | WWF |
| Era | Team run 1985-1991 |
| Titles | Two-time WWF World Tag Team Champions (1987, 1990) |
| Signature move | The Hart Attack (Neidhart backbreaker into a Bret clothesline) |
| Why it mattered | The launchpad for Bret Hart's singles run to five WWF Championships; a technical-plus-power template many teams copied |
| Confidence | HIGH |
| Disambiguation | The larger 1997 stable (Bret, Owen Hart, British Bulldog, Jim Neidhart, Brian Pillman) is the FACTION at `/factions/hart-foundation/`. This tag-team page is the original Bret-and-Anvil duo. Cross-link the two |

Source notes: WWE.com Hart Foundation profile; WWF title histories; Wikipedia "The Hart Foundation".

---

## 7. Legion of Doom (The Road Warriors) — `/tag-teams/legion-of-doom/`

| Field | Detail |
|---|---|
| Members | Road Warrior Hawk, Road Warrior Animal (both no page); managed by Paul Ellering |
| Promotions | AWA, NWA/Jim Crockett/WCW, WWF, NJPW, AJPW |
| Era | Formed 1983; runs across the AWA, NWA/WCW and WWF into the late 1990s; WWF reunion 2003 |
| Titles | Held tag gold in the AWA, NWA and WWF; the first team to hold the AWA, NWA and WWF World Tag Team Championships. Won the 1988 NWA Jim Crockett Sr. Memorial Cup |
| Signature move | The Doomsday Device |
| Why it mattered | The face-paint-and-spikes power template that influenced almost every hoss tag team that followed; genuine cross-promotional draws |
| Confidence | HIGH on team and the AWA/NWA/WWF triple-crown claim. MED on exact reign dates |
| Disambiguation | Also referenced in `data/factions-stables.md` as `legion-of-doom`. Keep one canonical tag-team page and cross-link |

Source notes: WWE.com Road Warriors/Legion of Doom profile; NWA and AWA title histories; Wikipedia
"The Road Warriors".

---

## 8. The Young Bucks — `/tag-teams/young-bucks/`

| Field | Detail |
|---|---|
| Members | Matt Jackson, Nick Jackson (real-life brothers Massie; both no page) |
| Promotions | Pro Wrestling Guerrilla (PWG), Ring of Honor, NJPW, AEW; also AEW Executive Vice Presidents |
| Era | 2004-present; central to the independent and NJPW booms of the 2010s |
| Titles | Multi-time AEW World Tag Team Champions; multi-time IWGP Junior Heavyweight Tag Team Champions in NJPW; multi-time ROH and PWG Tag Team Champions |
| Signature moves | The Meltzer Driver; superkick parties; the BTE Trigger |
| Why it mattered | Merchandise and "Being The Elite" YouTube pioneers whose independent-scene draw helped launch All Elite Wrestling in 2019 |
| Confidence | HIGH on team, AEW EVP role and multi-promotion titles. MED on exact reign counts (VERIFY totals before printing numbers) |
| Cross-links | AEW-tied; label alongside other AEW/NJPW acts on the site (Jon Moxley `jon-moxley`, Cody Rhodes `cody-rhodes` early AEW) |

Source notes: AEW World Tag Team Championship history (allelitewrestling.com); Wikipedia "AEW World
Tag Team Championship" and "IWGP Junior Heavyweight Tag Team Championship"; Pro Wrestling Fandom
profiles for Matt and Nick Jackson.

---

## 9. The Brothers of Destruction — `/tag-teams/brothers-of-destruction/`

| Field | Detail |
|---|---|
| Members | The Undertaker (`the-undertaker`), Kane (`kane`) |
| Promotion | WWF/WWE |
| Era | On-and-off team 1997-2020 (kayfabe brothers; feuded as often as they teamed) |
| Titles | WWF/WWE World Tag Team Champions and WCW Tag Team Champions (during the 2001 unification era) |
| Signature moves | The double chokeslam; the Tombstone and the chokeslam in tandem |
| Why it mattered | Two monster singles stars whose occasional alliance was always a marquee draw; both are singular WWE icons |
| Confidence | HIGH on team and both careers. MED on exact tag reign count |
| Cross-links | Both members have solo pages; Kane and Undertaker also appear in `/factions/the-corporation/` cross-references |

Source notes: WWE.com profiles for The Undertaker and Kane; WWF/WCW title histories.

---

## 10. The Steiner Brothers — `/tag-teams/steiner-brothers/`

| Field | Detail |
|---|---|
| Members | Rick Steiner, Scott Steiner (real-life brothers; both no page) |
| Promotions | NWA/WCW, WWF, NJPW, ECW, AJPW |
| Era | Formed 1989; dominant into the mid-1990s |
| Titles | Multi-time NWA/WCW World Tag Team Champions; WWF World Tag Team Champions; IWGP Tag Team Champions in NJPW |
| Signature moves | The Steiner Bulldog; the Frankensteiner (Scott); belly-to-belly suplexes |
| Why it mattered | Amateur-wrestling power team credited as one of the greatest tag teams of the 1990s; Scott later became a WCW World Heavyweight Champion |
| Confidence | HIGH on team and greatest-of-era standing. MED on exact reign totals |
| Cross-links | Inducted into the WWE Hall of Fame (2022 class, per the base research HOF table) |

Source notes: WWE.com; NWA/WCW and NJPW title histories; base research 00-content-data-research.md HOF
section (Steiner Brothers, 2022 class).

---

## 11. Additional verified teams (compact cards)

| Team | Slug | Members (existing page in bold) | Promotion(s) | Era | Titles / note | Confidence |
|---|---|---|---|---|---|---|
| The British Bulldogs | `british-bulldogs` | **british-bulldog** (Davey Boy Smith), Dynamite Kid | WWF, Stampede, NJPW | 1984-1988 | WWF World Tag Team Champions (WrestleMania 2, 1986) | HIGH |
| Demolition | `demolition` | Ax, Smash (later Crush) | WWF | 1987-1991 | Three-time WWF Tag Team Champions; long 1988-1989 reign of roughly 478 days | HIGH (team), MED (exact days) |
| The Rockers | `the-rockers` | **shawn-michaels**, Marty Jannetty | AWA, WWF | 1985-1992 | High-flying team; Michaels' 1992 singles turn (the barbershop window) launched HBK | HIGH |
| The Rock 'n' Sock Connection | `rock-n-sock-connection` | **the-rock**, **mick-foley** (Mankind) | WWF | 1999 | Multi-time WWF Tag Team Champions; the "This Is Your Life" segment drew a huge 1999 rating | HIGH |
| The Outsiders | `the-outsiders` | **razor-ramon** (Scott Hall), **kevin-nash** | WCW | 1996-1999 | Multi-time WCW World Tag Team Champions; the nWo's founding muscle | HIGH |
| The Brain Busters | `brain-busters` | **arn-anderson**, Tully Blanchard | NWA, WWF | 1988-1989 | WWF World Tag Team Champions (1989); part of the Four Horsemen lineage | HIGH |
| FTR | `ftr` | Cash Wheeler, Dax Harwood | WWE (as The Revival), AEW, NJPW, ROH | 2014-present | AEW, IWGP, ROH and NWA tag champions; modern throwback team | HIGH |

Source notes: WWE.com and promotion title histories for each; Wikipedia team entries. Exact reign
counts flagged MED where a specific number would be printed.

---

## Gap List — teams and members WITHOUT a page yet

Build or stub these so the section's clickables resolve. Ranked by priority.

### High priority (marquee teams, no member pages at all)
- **The New Day** members: **Kofi Kingston**, **Xavier Woods**, **Big E**. Kofi is a former WWE
  Champion (WrestleMania 35) and Woods a former King of the Ring; all three warrant solo profiles.
  Timely hook: the May 3, 2026 WWE release.
- **The Usos** members: **Jimmy Uso**, **Jey Uso**. Jey is a breakout singles star and Bloodline
  centerpiece; both are top-tier gaps.
- **The Young Bucks**: **Matt Jackson**, **Nick Jackson**. AEW EVPs and modern-era icons.
- **The Steiner Brothers**: **Rick Steiner**, **Scott Steiner** (2022 WWE Hall of Fame class).

### Medium priority (one member has a page, partner does not)
- **D-Von Dudley** (partner of `bully-ray`).
- **Jim "The Anvil" Neidhart** (partner of `bret-hart`).
- **Marty Jannetty** (partner of `shawn-michaels`).
- **Tully Blanchard** (partner of `arn-anderson`; Four Horsemen tie-in).
- **Dynamite Kid** (partner of `british-bulldog`).

### Lower priority (historic teams, both members missing)
- **Legion of Doom / Road Warriors**: **Road Warrior Hawk**, **Road Warrior Animal**.
- **Demolition**: **Ax**, **Smash**.
- **FTR**: **Cash Wheeler**, **Dax Harwood**.

### Page-shell gaps
- The section index `/tag-teams/` does not exist yet. Build it.
- Reverse "Tag Teams" cross-link strips do not exist on wrestler pages yet. Add to: `matt-hardy`,
  `jeff-hardy`, `edge`, `christian`, `bret-hart`, `bully-ray`, `shawn-michaels`, `the-rock`,
  `mick-foley`, `razor-ramon`, `kevin-nash`, `arn-anderson`, `british-bulldog`, `the-undertaker`,
  `kane`.

---

## Consolidated source list

- The Usos records: https://www.fightful.com/wrestling/usos-officially-become-longest-reigning-tag-team-champions/ ; https://www.fightful.com/wrestling/usos-become-first-tag-team-history-surpass-600-day-reign-wwe-tag-team-champions/ ; https://www.sescoops.com/news/the-usos-officially-break-wwe-record/ ; https://en.wikipedia.org/wiki/The_Usos
- The New Day departure (May 2026): https://www.foxnews.com/sports/legendary-wwe-tag-team-duo-departs-company-latest-wave-cuts ; https://sports.yahoo.com/wrestling/breaking-news/article/new-days-kofi-kingston-and-xavier-woods-split-from-wwe-amid-reported-contract-dispute-154432048.html ; https://en.wikipedia.org/wiki/The_New_Day_(professional_wrestling)
- TLC trilogy (Hardyz, Dudleyz, Edge and Christian): https://www.wwe.com/videos/edge-christian-vs-the-hardy-boyz-vs-the-dudley-boyz-wwe-tag-team-championship-tlc-match-summerslam-2000 ; https://lastwordonsports.com/prowrestling/2020/04/02/20-years-ago-edge-christian-hardyz-dudleyz-change-tag-team-history/amp
- Young Bucks titles: https://www.allelitewrestling.com/aew-world-tag-team-championship-history ; https://en.wikipedia.org/wiki/AEW_World_Tag_Team_Championship ; https://en.wikipedia.org/wiki/IWGP_Junior_Heavyweight_Tag_Team_Championship
- Base research (HOF, taxonomy, promotions): /root/wwe/docs/design/wrestle-lore/00-content-data-research.md
- Companion datasets: data/factions-stables.md ; data/titles-lineages.md
