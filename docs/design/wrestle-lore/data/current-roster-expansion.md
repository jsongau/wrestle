# Wrestle Lore — Current Roster Expansion Dataset

Active-roster research deliverable. Goal: make the "current" tier of Wrestle Lore feel complete by
adding top WWE and AEW stars who are active in 2026 but do not yet have a profile page. Every row
carries a source note and a confidence flag. No fabricated facts, quotes, or stats. Anything subject
to weekly change is flagged `VERIFY`.

- Date of research: 2026-07-26
- Confidence legend: `HIGH` = multiple/authoritative sources agree; `MED` = single reputable source or subject to change; `VERIFY` = confirm the exact belt/date before publishing (title pictures move week to week).
- Deduped against the existing 89 slugs under `/root/wwe/wrestlers/`. None of the 20 proposed slugs below collide with an existing slug.

---

## Route pattern for the new pages

- New profiles follow the existing convention exactly: `/wrestlers/{slug}/` (one directory per wrestler, `index.html` inside).
- No new route family is needed. These slot straight into the existing wrestler grid and inherit the CURRENT status tag from the taxonomy in `00-content-data-research.md` section 5 (Axis A).
- Faction cross-links point at existing faction/stable data in `data/factions-stables.md` (Bloodline, Lucha Bros, etc.) where present.

---

## Current title landscape (verified anchor facts, 2026-07-26)

These are the belts the proposed profiles hang off. Confirm the exact holder on the publish date; the
title scene changed several times in July 2026.

| Title | Holder (as researched) | Key dated fact | Confidence | Source |
|---|---|---|---|---|
| Undisputed WWE Championship | **CM Punk** (page exists) | CM Punk won it from Sami Zayn on Raw, 2026-07-06; Sami Zayn had won it at Night of Champions 2026 | HIGH | wwe.com Raw 2026-07-06; wwe.com NoC 2026 |
| WWE United States Championship | **Jacob Fatu** (contested vs LA Knight) | Fatu won the US Title at WrestleMania 2026, retained at Backlash; LA Knight program ongoing on Raw 2026-07-20 | MED / VERIFY exact holder | wwe.com Raw 2026-07-20; Fightful; Sportskeeda |
| WWE Women's Championship | **Tiffany Stratton** | Reported current WWE Women's Champion | MED / VERIFY | Sportskeeda; wwe.com |
| WWE Intercontinental Championship | **Penta** (contested) | Penta beat Dominik Mysterio for the IC Title on Raw, 2026-03-02; Rey Fenix chasing the belt | MED / VERIFY | wwe.com; 411Mania; YouTube Raw 2026-03-02 |
| NXT Championship | **Oba Femi** | Current NXT Champion; set for main-roster debut at Royal Rumble, 2026-01-31 | HIGH | Netflix Tudum; Sportskeeda; wwe.com |
| AEW World Championship | **Kenny Omega** (2nd reign) | Omega beat MJF at Beach Break 2026; Ospreay vs Omega set for All In 2026 | HIGH | allelitewrestling.com; Wrestling Inc.; TPWW |
| AEW Unified Championship | **Kazuchika Okada** | Retained at All Out 2026; record-setting reign | HIGH | Fightful; SI; allelitewrestling.com |

---

## Dataset A — WWE current stars without a page (GAP)

Target route: `/wrestlers/{slug}/`

| Name | Slug suggestion | Brand / role | Key verified facts | Cross-links (existing slugs) | Confidence | Source |
|---|---|---|---|---|---|---|
| Jey Uso | `jey-uso` | Raw main-eventer, top babyface | Returned to WWE mid-2026; chasing the Undisputed WWE Title held by Sami Zayn/CM Punk; former World Heavyweight Champion; twin of Jimmy Uso | `roman-reigns`, `sami-zayn`, `cm-punk`, `solo-sikoa`(new) | HIGH | wwe.com/superstars/jey-uso; Cageside Seats; Sportskeeda |
| Jacob Fatu | `jacob-fatu` | SmackDown, US Champion | Won WWE United States Championship at WrestleMania 2026, retained at Backlash; Bloodline "Samoan Werewolf"; program with LA Knight on Raw 2026-07-20 | `la-knight`, `solo-sikoa`(new), `roman-reigns` | HIGH | wwe.com/superstars/jacob-fatu; 411Mania; Fightful |
| Solo Sikoa | `solo-sikoa` | Bloodline leader | Leads his faction of the Bloodline; held a championship in 2026; brother of the Usos, cousin of Roman Reigns | `roman-reigns`, `jey-uso`(new), `jacob-fatu`(new) | HIGH | wwe.com/superstars/solo-sikoa; ITR Wrestling; wwe.com Raw 2026-07-20 |
| Bron Breakker | `bron-breakker` | Raw powerhouse | Multi-time Intercontinental Champion; central to Survivor Series: WarGames 2026 build; son of Rick Steiner, nephew of Scott Steiner | `seth-rollins`, `gunther` | HIGH | FOX Sports; Sportskeeda |
| Tiffany Stratton | `tiffany-stratton` | SmackDown, Women's Champion | Reported current WWE Women's Champion; defended vs Jade Cargill at Night of Champions 2026 | `charlotte-flair`, `jade-cargill`(new) | MED / VERIFY | Sportskeeda; wwe.com/superstars/tiffany-stratton |
| Jade Cargill | `jade-cargill` | SmackDown, top contender | Faced Tiffany Stratton at Night of Champions 2026; power athlete, former AEW TBS Champion | `bianca-belair`, `tiffany-stratton`(new) | HIGH | wwe.com NoC 2026; FOX Sports |
| Dominik Mysterio | `dominik-mysterio` | Raw heel | Former Intercontinental Champion; lost the IC Title to Penta on Raw 2026-03-02; son of Rey Mysterio | `rey-mysterio`, `penta`(new), `finn-balor` | HIGH | wwe.com/superstars/dominik-mysterio; Wikipedia IC title |
| Penta | `penta` | Raw, singles gold | Beat Dominik Mysterio for the Intercontinental Title on Raw 2026-03-02; half of the Lucha Brothers; brother of Rey Fenix | `rey-fenix`(new), `dominik-mysterio`(new) | HIGH | Fightful; Wrestling Attitude; YouTube Raw 2026-03-02 |
| Rey Fenix | `rey-fenix` | SmackDown, cruiserweight | Won the AAA World Cruiserweight Championship in 2026 (first WWE-era title); chasing Penta's IC Title; other half of the Lucha Brothers | `penta`(new) | MED / VERIFY | 411Mania; Wrestling Inc.; wwe.com/superstars/rey-fenix |
| Oba Femi | `oba-femi` | NXT to main roster | NXT Champion; main-roster debut at Royal Rumble 2026-01-31; beat Trick Williams in a Winner Take All match, 2025-09-23 | `trick-williams`(new) | HIGH | Netflix Tudum; wwe.com/superstars/oba-femi; F4W |
| Trick Williams | `trick-williams` | NXT / TNA crossover | TNA World Champion while on the NXT roster; faced Oba Femi in Winner Take All, 2025-09-23 | `oba-femi`(new) | HIGH | wwe.com 2025-09-23; F4W |

Secondary WWE add (build after the eleven above):

| Name | Slug suggestion | Note | Confidence | Source |
|---|---|---|---|---|
| Jimmy Uso | `jimmy-uso` | Twin of Jey Uso, longtime tag star; needed to complete the Usos/Bloodline cross-link web | HIGH | Wikipedia WWE Tag Team Championship; wwe.com |

---

## Dataset B — AEW current stars without a page (GAP)

Target route: `/wrestlers/{slug}/`

| Name | Slug suggestion | Role | Key verified facts | Cross-links (existing slugs) | Confidence | Source |
|---|---|---|---|---|---|---|
| Kenny Omega | `kenny-omega` | AEW World Champion | Two-time AEW World Champion; beat MJF at Beach Break 2026 for the second reign; defends vs Will Ospreay at All In 2026; original Bullet Club / NJPW pedigree | `jon-moxley`, `will-ospreay`(new), `aj-styles`, `finn-balor` | HIGH | Wrestling Inc.; allelitewrestling.com; TPWW; PWTorch |
| Will Ospreay | `will-ospreay` | AEW top star | Returned from neck surgery in 2026; won the Owen Hart Cup by beating Swerve Strickland; earned an AEW World Title shot vs Omega at All In; ex-NJPW IWGP champion | `kenny-omega`(new), `swerve-strickland`(new), `jon-moxley` | HIGH | Bleacher Report; F4W; Forbes; SI |
| Swerve Strickland | `swerve-strickland` | AEW former World Champ | First Black AEW World Champion; absent stretch in 2026 with a hinted return at AEW Redemption; lost Owen Hart Cup final to Ospreay | `will-ospreay`(new), `hangman-page`(new) | HIGH | Wrestling Inc.; F4W; WrestleZone |
| "Hangman" Adam Page | `hangman-page` | AEW main-eventer | Former AEW World Champion; returned to AEW in July 2026 after a four-month absence; on Collision 2026-07-11 said he would not challenge for the World Title and targeted other belts | `kenny-omega`(new), `swerve-strickland`(new) | HIGH | WrestleZone; allelitewrestling.com Collision 2026-07-11; eWrestlingNews |
| MJF | `mjf` | AEW top heel | Former AEW World Champion; won the title at Double or Nothing 2026, lost it to Kenny Omega at Beach Break 2026; "fighting through" injuries per 2026 reports | `kenny-omega`(new) | HIGH | Fightful; SI; ClutchPoints |
| Toni Storm | `toni-storm` | AEW women's icon | Multi-time AEW Women's World Champion ("Timeless" persona); reported out for the entirety of 2026 | `mercedes-mone`, `mariah-may`(not built) | MED / VERIFY reason for absence | Wrestling Inc.; SI; Augusta Free Press |
| Kazuchika Okada | `kazuchika-okada` | AEW Unified Champion | Holds the AEW Unified Championship; retained at All Out 2026; NJPW legend ("The Rainmaker") with a record-setting AEW reign; crossover with the NJPW promotion page | `jon-moxley`, `kenny-omega`(new) | HIGH | Fightful; SI; allelitewrestling.com |

---

## Cross-link opportunities into existing pages

Building these profiles unlocks links from pages that already exist:

- `roman-reigns` gains Bloodline links to `jey-uso`, `jacob-fatu`, `solo-sikoa`, `jimmy-uso`.
- `rey-mysterio` gains a father-son link to `dominik-mysterio`.
- `cm-punk` and `sami-zayn` gain title-feud links to `jey-uso` (Undisputed WWE Title chase).
- `la-knight` gains a US Title feud link to `jacob-fatu`.
- `jon-moxley` (ex-IWGP, ex-AEW World Champ) gains links to `kenny-omega`, `will-ospreay`, `kazuchika-okada`.
- `aj-styles` and `finn-balor` (Bullet Club history) gain a link to `kenny-omega` (original Bullet Club).
- `mercedes-mone` (AEW) gains a women's-division link to `toni-storm`.
- The pending NJPW promotion page (`/promotions/njpw/`, gap in `njpw-and-ajstyles.md`) should link to `kazuchika-okada`, `kenny-omega`, and `will-ospreay`.

---

## GAP LIST — build these (priority order)

Tier 1, current champions and main-eventers (build first, highest "current feels complete" impact):
1. `kenny-omega` (AEW World Champion)
2. `jey-uso` (Undisputed WWE Title chase, top babyface)
3. `jacob-fatu` (WWE US Champion)
4. `will-ospreay` (AEW World Title challenger, All In headliner)
5. `kazuchika-okada` (AEW Unified Champion, NJPW anchor)
6. `oba-femi` (NXT Champion crossing to main roster)
7. `tiffany-stratton` (WWE Women's Champion)

Tier 2, top stars and former World Champions:
8. `swerve-strickland`
9. `hangman-page`
10. `mjf`
11. `solo-sikoa`
12. `bron-breakker`
13. `jade-cargill`
14. `dominik-mysterio`
15. `toni-storm`

Tier 3, tag/luchador and completion pieces:
16. `penta`
17. `rey-fenix`
18. `trick-williams`
19. `jimmy-uso`

Slugs to keep an eye on for future waves (not built here, mentioned as cross-link targets): `mariah-may`, `jamie-hayter`, `adam-cole`, `orange-cassidy`, `ricochet`, `karrion-kross`, `chad-gable`, `roxanne-perez`, `giulia`.

---

## Anti-AI copy note for the build phase

When these profiles are authored, use specific nouns (the exact belt, the exact event, the exact date
from the tables above), avoid decorative arrows and em-dash separators, and skip cliche banned words.
Every dated claim in a profile should trace back to a source row here, with the `VERIFY` belts
re-checked against wwe.com or allelitewrestling.com on the publish date, since several 2026 title
reigns changed hands within a single week.

---

## Consolidated source list

- WWE Raw results 2026-07-06 (CM Punk wins Undisputed WWE Title): https://www.wwe.com/shows/raw/2026-07-06
- WWE Raw results 2026-07-20 (Bloodline, LA Knight, Solo Sikoa, Jacob Fatu): https://www.wwe.com/shows/raw/2026-07-20
- Jey Uso vs Sami Zayn / WWE Championship (Cageside Seats): https://www.cagesideseats.com/wwe/456169/jey-uso-sami-zayn-wwe-championship-smackdown
- Jacob Fatu status and 2026 plans (411Mania): https://411mania.com/wrestling/jacob-fatu-status-big-year-2026/
- Solo Sikoa champion in 2026 (ITR Wrestling): https://itrwrestling.com/news/solo-sikoa-champion-2026-win-wwe-smackdown/
- Every current WWE champion (WhatCulture): https://whatculture.com/wwe/every-current-wwe-champion-full-list-updates
- Current WWE champions list 2026-07-22 (The SmackDown Hotel): https://www.thesmackdownhotel.com/roster/current-champions/?promotion=wwe
- Tiffany Stratton vs Jade Cargill, Night of Champions 2026: https://www.wwe.com/shows/nightofchampions/2026/tiffany-stratton-vs-jade-cargill
- Penta wins IC Title from Dominik Mysterio, Raw 2026-03-02: https://www.youtube.com/watch?v=PqsOHd7makc
- Rey Fenix wins AAA World Cruiserweight Title (411Mania): https://411mania.com/wrestling/rey-fenix-urges-wwe-more-opportunities-sets-sights-penta-ic-title/
- Oba Femi main-roster debut at Royal Rumble (Netflix Tudum): https://www.netflix.com/tudum/articles/oba-fami-wwe-raw-superstar-bio
- Oba Femi vs Trick Williams Winner Take All 2025-09-23: https://www.wwe.com/shows/wwenxt/2025-09-23/femi-trick-winner-takes-all
- Kenny Omega beats MJF for AEW World Title (allelitewrestling.com): https://www.allelitewrestling.com/post/kenny-omega-beats-mjf-to-become-aew-world-champion-for-a-second-time
- Omega wins AEW World Title, Ospreay vs Omega set for All In (TPWW): https://www.tpww.net/2026/07/kenny-omega-wins-aew-world-title-at-aew-beach-break-2026-show-will-ospreay-vs-omega-for-aew-world-title-set-for-all-in-2026/
- Will Ospreay wins Owen Hart Cup over Swerve Strickland (Bleacher Report): https://bleacherreport.com/articles/25443029-will-ospreay-beats-swerve-strickland-win-owen-hart-cup-and-aew-world-title-shot-at-all-in
- Ospreay cleared after neck surgery (SI): https://www.si.com/fannation/wrestling/aew/will-ospreay-confirms-when-he-officially-got-cleared-for-aew-return
- Swerve Strickland absence, return hinted at Redemption (F4W): https://www.f4wonline.com/news/aew/swerve-strickland-return-aew-redemption-tony-khan/
- Hangman Adam Page returns, won't challenge for World Title, Collision 2026-07-11 (allelitewrestling.com): https://www.allelitewrestling.com/post/aew-collision-results-july-11-2026
- Hangman Page return announced after four-month absence (WrestleZone): https://www.wrestlezone.com/news/1651225-hangman-adam-pages-aew-return-announced-after-four-month-absence
- MJF wins AEW World Title at Double or Nothing 2026 (Fightful): https://www.fightful.com/wrestling/mjf/
- MJF status after World Title loss (SI): https://www.si.com/fannation/wrestling/update-on-mjf-aew-status-following-world-title-loss
- Toni Storm out for the entirety of 2026 (Wrestling Inc.): https://www.wrestlinginc.com/2128254/aew-toni-storm-miss-entirety-2026-injury/
- Kazuchika Okada retains AEW Unified Title at All Out (Fightful): https://www.fightful.com/wrestling/kazuchika-okada-aew-all-out/
- Okada breaks AEW championship record (SI): https://www.si.com/fannation/wrestling/aew/kazuchika-okada-breaks-major-aew-championship-record
