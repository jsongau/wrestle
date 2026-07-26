# Wrestle Lore — Factions & Stables Dataset

Page-ready, verified dataset for the new Factions section. Build phase turns each entry below into a
page at the route pattern `/factions/{slug}/`. Every faction card links members to existing
`/wrestlers/{slug}/` pages where they exist; missing members are collected in the Gap List (section
at the end) so no clickable 404s.

- Researcher role: Factions
- Date of research: 2026-07-26
- Rule followed: no invented facts, quotes, or stats. Anything time-sensitive or single-source is flagged.
- Confidence legend: `HIGH` = multiple authoritative sources agree; `MED` = single reputable source or subject to change; `VERIFY` = confirm before publishing.
- Copy standard: specific nouns, no decorative arrows, no em-dash separators, no filler adjectives.

## Route pattern

- Section index: `/factions/`
- Faction page: `/factions/{slug}/`
- Each member name on a faction page links to `/wrestlers/{member-slug}/` when that page exists.
- Reverse cross-link: each existing wrestler page should gain a "Factions" strip linking back to `/factions/{slug}/`.

---

## Master index table

| Faction | Slug | Promotion(s) | Era (active) | Confidence | Existing member pages |
|---|---|---|---|---|---|
| nWo (New World Order) | `nwo` | WCW, later WWF/WWE | 1996-2001; 2002 WWE revival | HIGH | hulk-hogan, kevin-nash, razor-ramon, big-show, randy-savage, mr-perfect, sting, ted-dibiase |
| D-Generation X | `d-generation-x` | WWF/WWE | 1997-2000; 2006 reunion | HIGH | shawn-michaels, triple-h, chyna |
| Four Horsemen | `four-horsemen` | NWA / Jim Crockett, WCW | 1985-1999 (multiple versions) | HIGH | ric-flair, arn-anderson, lex-luger, sting, brian-pillman, chris-benoit, mr-perfect |
| The Shield | `the-shield` | WWE | 2012-2014; 2017-2018 reunions | HIGH | roman-reigns, seth-rollins, jon-moxley |
| The Bloodline | `the-bloodline` | WWE | 2020-present | HIGH (history), MED (2026 lineup) | roman-reigns, sami-zayn |
| The Judgment Day | `judgment-day` | WWE | 2022-present | HIGH (history), MED (2026 lineup) | edge, damian-priest, finn-balor, rhea-ripley, liv-morgan |
| Bullet Club | `bullet-club` | NJPW (also ROH, IMPACT) | 2013-present | HIGH | finn-balor, aj-styles, cody-rhodes |
| Evolution | `evolution` | WWE | 2003-2005; 2014 reunion | HIGH | triple-h, ric-flair, randy-orton, batista |
| The Wyatt Family | `wyatt-family` | WWE | 2013-2017 | HIGH | daniel-bryan |
| The New Day | `the-new-day` | WWE | 2014-present | HIGH | (none) |
| The Nexus | `the-nexus` | WWE | 2010-2011 | HIGH | cm-punk, daniel-bryan, john-cena |
| The Hart Foundation | `hart-foundation` | WWF | 1985-1991 (team); 1997 (stable) | HIGH | bret-hart, owen-hart, british-bulldog, brian-pillman |
| The Corporation | `the-corporation` | WWF | 1998-1999 | HIGH | vince-mcmahon, the-rock, big-show, kane |
| Legion of Doom (Road Warriors) | `legion-of-doom` | AWA, NWA/WCW, WWF | 1983-2003 (across runs) | HIGH | (none) |

---

## 1. nWo (New World Order) — `/factions/nwo/`

| Field | Detail |
|---|---|
| Promotion | WCW (1996-2001); revived in WWF/WWE (2002) |
| Formed | July 7, 1996, Bash at the Beach. Hulk Hogan turned heel and joined Scott Hall and Kevin Nash |
| Founding three | Hulk Hogan (`hulk-hogan`), Scott Hall (`razor-ramon`, his WWE persona), Kevin Nash (`kevin-nash`) |
| Key later members with pages | The Giant / Big Show (`big-show`), Randy Savage (`randy-savage`), Curt Hennig (`mr-perfect`), Sting (`sting`, nWo Wolfpac), financial backer Ted DiBiase (`ted-dibiase`) |
| Why it mattered | The angle blurred the line between show and reality by presenting Hall and Nash as an outside invasion of WCW. It pushed Nitro past Raw for 83 straight weeks in the Monday Night War and reshaped how factions are booked |
| Confidence | HIGH (formation date, founding three). MED on exact join dates of secondary members |

Source notes: WWE video "Hulk Hogan forms The nWo" (wwe.com); Wikipedia "New World Order (professional
wrestling)"; Wrestling Inc. Bash at the Beach 1996 recap.

---

## 2. D-Generation X — `/factions/d-generation-x/`

| Field | Detail |
|---|---|
| Promotion | WWF/WWE |
| Formed | 1997 (Shawn Michaels and Triple H, with Chyna and Rick Rude) |
| Members with pages | Shawn Michaels (`shawn-michaels`), Triple H (`triple-h`), Chyna (`chyna`) |
| Members without pages | X-Pac / Sean Waltman, Road Dogg / Jesse James, Billy Gunn (The New Age Outlaws), Rick Rude |
| Why it mattered | DX was the on-screen voice of the Attitude Era's rebellious tone. The "crotch chop" and the 1998 invasion of a WCW event drove merchandise and TV segments. Shawn Michaels was inducted into the WWE Hall of Fame as a DX member in 2019 |
| Confidence | HIGH |

Source notes: Wikipedia "D-Generation X"; wwe.com superstar page; base research file section 2 (2019 HOF DX class).

---

## 3. Four Horsemen — `/factions/four-horsemen/`

| Field | Detail |
|---|---|
| Promotion | NWA / Jim Crockett Promotions, later WCW |
| Formed | 1985-1986. Original lineup: Ric Flair, Arn Anderson, Ole Anderson, Tully Blanchard, manager J.J. Dillon |
| Members with pages | Ric Flair (`ric-flair`), Arn Anderson (`arn-anderson`), Lex Luger (`lex-luger`), Sting (`sting`), Brian Pillman (`brian-pillman`), Chris Benoit (`chris-benoit`), Curt Hennig (`mr-perfect`) |
| Members without pages | Ole Anderson, Tully Blanchard, Barry Windham, Dean Malenko, Steve "Mongo" McMichael, manager J.J. Dillon |
| Why it mattered | The template for the modern wrestling stable. Four men who controlled the NWA World and tag titles, with Flair as the centerpiece. The group was inducted into the WWE Hall of Fame in 2012, which counted as Flair's second induction |
| Confidence | HIGH on core members. MED on which exact version a given member belonged to (the lineup changed several times) |

Source notes: Wikipedia "The Four Horsemen (professional wrestling)"; Online World of Wrestling profile;
base research file section 2 (2012 HOF induction, Flair two-time).

---

## 4. The Shield — `/factions/the-shield/`

| Field | Detail |
|---|---|
| Promotion | WWE |
| Formed | November 18, 2012, Survivor Series. Disbanded June 2014; reunited 2017-2018 |
| Members (all three have pages) | Roman Reigns (`roman-reigns`), Seth Rollins (`seth-rollins`), Dean Ambrose (`jon-moxley`, his current ring name) |
| Why it mattered | Three developmental talents debuted as a unit and each went on to hold the WWE or Universal Championship. Their matched tactical gear and entrance through the crowd became a signature. The breakup match set up years of main-event programs |
| Confidence | HIGH |

Note for build: Dean Ambrose is the same performer as Jon Moxley. The Shield page should label him
"Dean Ambrose" for the era and link to `/wrestlers/jon-moxley/`.

Source notes: Sports Illustrated 2022 Shield formation retrospective; Simple English Wikipedia "The Shield";
ESPN WWE profile.

---

## 5. The Bloodline — `/factions/the-bloodline/`

| Field | Detail |
|---|---|
| Promotion | WWE |
| Formed | 2020 (Roman Reigns aligned with Paul Heyman and the Usos). Evolved through several splits by 2026 |
| Members with pages | Roman Reigns (`roman-reigns`), Sami Zayn (`sami-zayn`, honorary "Uce" member 2022-2023) |
| Members without pages | Jey Uso, Jimmy Uso (The Usos), Solo Sikoa, Jacob Fatu, Paul Heyman (manager / "Wiseman"), Tama Tonga, Tonga Loa |
| Why it mattered | The longest and most decorated modern WWE story. Roman Reigns held the Universal Championship past 1,300 days behind the "Tribal Chief" and "acknowledge me" narrative. The Anoa'i family real-life ties gave the angle weight, and the 2022-2023 Sami Zayn arc drew some of the era's loudest crowd reactions |
| Confidence | HIGH on history. MED / VERIFY on the exact 2026 active lineup, which was shifting through mid-2026 (Solo Sikoa's group versus a Roman Reigns reunion) |

Source notes: Bleacher Report Crown Jewel Bloodline recap; PWTorch 2026-06-05; itrwrestling.com bio;
Last Word on Sports 2026-06-24 (Solo Sikoa status). Flag the live 2026 roster `VERIFY` at publish time.

---

## 6. The Judgment Day — `/factions/judgment-day/`

| Field | Detail |
|---|---|
| Promotion | WWE |
| Formed | April 2022. Founder Edge, with Damian Priest and Rhea Ripley; Finn Balor and Dominik Mysterio added, Edge later ousted |
| Members with pages | Edge (`edge`), Damian Priest (`damian-priest`), Finn Balor (`finn-balor`), Rhea Ripley (`rhea-ripley`), Liv Morgan (`liv-morgan`, joined 2024) |
| Members without pages | Dominik Mysterio, JD McDonagh, Carlito, Raquel Rodriguez |
| Why it mattered | The dominant WWE faction of 2023-2025, holding World, tag, and women's titles at once. Rhea Ripley became the group's breakout draw, and the "Mami" and Dominik pairing became a top merchandise line |
| Confidence | HIGH on history. MED on the 2026 status; reporting through 2026 pointed to the group winding down |

Source notes: Wikipedia "The Judgment Day"; thesportster.com Judgment Day member roles; khelnow.com departures
recap. Flag the 2026 active/disbanded status `VERIFY`.

---

## 7. Bullet Club — `/factions/bullet-club/`

| Field | Detail |
|---|---|
| Promotion | New Japan Pro-Wrestling (also ROH, IMPACT) |
| Formed | May 2013. Founder Prince Devitt (Finn Balor) |
| Members with pages | Finn Balor (`finn-balor`, as Prince Devitt, founder), AJ Styles (`aj-styles`, second leader), Cody Rhodes (`cody-rhodes`, member 2016-2018) |
| Members without pages | Kenny Omega, The Young Bucks (Matt and Nick Jackson), Karl Anderson, Luke Gallows, Bad Luck Fale, Tama Tonga, Jay White, Adam Cole |
| Why it mattered | The most exported wrestling brand of the 2010s. The "Too Sweet" hand sign and the merchandise line crossed over to the United States and helped establish New Japan's Western audience. Alumni went on to lead WWE (Balor, Styles, Cody, Cole) and to co-found AEW (Omega, Young Bucks) |
| Confidence | HIGH |

Note for build: this is the strongest cross-promotion faction and directly supports the planned NJPW
promotion page (see base research file section 4).

Source notes: Sports Illustrated 2023 Bullet Club anniversary feature; IMPACT Wiki roster; thesportster.com
Bullet Club leaders history.

---

## 8. Evolution — `/factions/evolution/`

| Field | Detail |
|---|---|
| Promotion | WWE |
| Formed | 2003. Disbanded 2005; one-night reunion 2014 |
| Members (all four have pages) | Triple H (`triple-h`), Ric Flair (`ric-flair`), Randy Orton (`randy-orton`), Batista (`batista`) |
| Why it mattered | A four-man stable built as a timeline of the business: Flair the past, Triple H the present, Orton and Batista the future. Both younger members left as World Champions and top singles draws, which validated the "future" framing |
| Confidence | HIGH |

Cross-link value: every member already has a page, so this is a fully linkable card and a good launch
example for the section.

Source notes: Wikipedia "Evolution (professional wrestling)"; wwe.com "The theory of Evolution";
thesportster.com Evolution history.

---

## 9. The Wyatt Family — `/factions/wyatt-family/`

| Field | Detail |
|---|---|
| Promotion | WWE |
| Formed | Main roster debut July 2013 |
| Members with pages | Daniel Bryan (`daniel-bryan`, storyline member 2014) |
| Members without pages | Bray Wyatt (leader), Luke Harper, Erick Rowan, Braun Strowman |
| Why it mattered | A horror-styled cult act led by Bray Wyatt, with the lantern entrance and "Follow the buzzards" tagline. It launched Braun Strowman and set up Wyatt's later "Fiend" character. Note that Bray Wyatt (Windham Rotunda) died in 2023, which the page should handle with a factual, respectful note |
| Confidence | HIGH |

Sensitivity note: verify current wording on Bray Wyatt's passing before publishing; keep to a plain
factual sentence, no speculation.

Source notes: Wikipedia "The Wyatt Family"; ESPN WWE profile; wwe.com playlist. Confirm the death-notice
wording `VERIFY`.

---

## 10. The New Day — `/factions/the-new-day/`

| Field | Detail |
|---|---|
| Promotion | WWE |
| Formed | Debuted November 2014 |
| Members (none have pages yet) | Kofi Kingston, Big E, Xavier Woods |
| Why it mattered | Held the Raw Tag Team Championship for 483 days, the longest tag title reign in WWE history. Kofi Kingston's 2019 WrestleMania WWE Championship win ("KofiMania") grew out of the group. The trombone ("Francesca") and pancake gimmick made them a top merchandise act |
| Confidence | HIGH on the 483-day record (widely cited). VERIFY the exact reign dates before printing them |

Gap note: this is the highest-value faction with zero linkable members. All three warrant wrestler pages.

Source notes: Wikipedia "The New Day (professional wrestling)"; ScreenRant New Day history; ESPN profile.

---

## 11. The Nexus — `/factions/the-nexus/`

| Field | Detail |
|---|---|
| Promotion | WWE |
| Formed | June 7, 2010. Wade Barrett led the debut season of NXT rookies in an attack on Raw |
| Members with pages | CM Punk (`cm-punk`, led the later New Nexus), Daniel Bryan (`daniel-bryan`, original member), John Cena (`john-cena`, forced member during the 2010 storyline) |
| Members without pages | Wade Barrett (leader), David Otunga, Justin Gabriel, Heath Slater, Michael Tarver, Skip Sheffield (Ryback), Darren Young |
| Why it mattered | One of WWE's most talked-about invasion angles. The debut segment, where the rookies destroyed the ringside area, was a genuine shock. The booking is also a common case study in how a hot faction can lose momentum quickly |
| Confidence | HIGH on formation and debut. MED on the full membership list across the group's phases |

Source notes: Online World of Wrestling Nexus profile; Simple English Wikipedia "Nexus"; sportskeeda New
Nexus (CM Punk) history.

---

## 12. The Hart Foundation — `/factions/hart-foundation/`

| Field | Detail |
|---|---|
| Promotion | WWF |
| Two forms | Tag team (Bret Hart and Jim Neidhart, 1985-1991); five-man stable (1997) |
| 1997 stable members with pages | Bret Hart (`bret-hart`), Owen Hart (`owen-hart`), British Bulldog (`british-bulldog`), Brian Pillman (`brian-pillman`) |
| Members without pages | Jim "The Anvil" Neidhart |
| Why it mattered | The 1997 stable ran a pro-Canada, anti-USA angle that split crowds by geography: cheered in Canada, booed in the United States. It peaked at In Your House: Canadian Stampede in Calgary and set up the Montreal Screwjob later that year |
| Confidence | HIGH |

Note for build: the page should distinguish the original 1980s tag team from the 1997 five-man stable.

Source notes: Online World of Wrestling Hart Foundation (2) profile; thesportster.com Hart Foundation facts;
prowrestling.fandom "The (New) Hart Foundation".

---

## 13. The Corporation — `/factions/the-corporation/`

| Field | Detail |
|---|---|
| Promotion | WWF |
| Formed | 1998-1999. Led by Vince McMahon and Shane McMahon |
| Members with pages | Vince McMahon (`vince-mcmahon`), The Rock (`the-rock`, "Corporate Champion"), Big Show (`big-show`), Kane (`kane`) |
| Members without pages | Shane McMahon, Big Boss Man, Ken Shamrock, Test, Triple H (joined late), the Mean Street Posse |
| Why it mattered | The authority-figure stable that Steve Austin fought against in the Attitude Era, the "boss versus employee" story that defined WWF's late-1990s ratings peak. The group later merged with the Undertaker's Ministry of Darkness to form the Corporate Ministry |
| Confidence | HIGH on core structure. MED on the full rotating roster and exact dates |

Source notes: Wikipedia "The Corporation (professional wrestling)"; Online World of Wrestling Corporation
profile; Wikipedia "Corporate Ministry". Flag the full member list `VERIFY`.

---

## 14. Legion of Doom (Road Warriors) — `/factions/legion-of-doom/`

| Field | Detail |
|---|---|
| Promotion | AWA, NWA/WCW, WWF (across multiple runs) |
| Active | 1983 through the early 2000s across territories |
| Members (none have pages yet) | Hawk, Animal, manager Paul Ellering |
| Why it mattered | Named the greatest tag team of all time in WWE's own retrospective. The face paint, spiked shoulder pads, and power offense made them a template for tag team presentation. They won tag titles in the AWA, NWA, and WWF |
| Confidence | HIGH on the "greatest tag team" framing (WWE and Yahoo Sports). VERIFY the specific title-reign counts before printing them |

Source notes: WWE.com Road Warriors page; Yahoo Sports "greatest WWE tag team of all time"; FanBuzz Road
Warriors feature.

---

## Gap List — members and managers WITHOUT a `/wrestlers/` page

Build these to make every faction card fully linkable. Ordered by how many marquee factions they unlock.

### Highest priority (unlock multiple factions or a whole card)

| Name | Unlocks / role | Faction(s) | Priority |
|---|---|---|---|
| Kenny Omega | Bullet Club leader, later AEW founder | Bullet Club | HIGH |
| The Young Bucks (Matt and Nick Jackson) | Bullet Club core, AEW founders | Bullet Club | HIGH |
| Bray Wyatt | Faction leader; whole card has 1 linkable member | Wyatt Family | HIGH |
| Kofi Kingston | New Day has zero linkable members | The New Day | HIGH |
| Big E | New Day | The New Day | HIGH |
| Xavier Woods | New Day | The New Day | HIGH |
| The Usos (Jey Uso, Jimmy Uso) | Bloodline core | The Bloodline | HIGH |
| Solo Sikoa | Bloodline 2026 lead | The Bloodline | HIGH |
| Paul Heyman | Bloodline "Wiseman"; also Nexus/ECW ties | The Bloodline | HIGH |
| Wade Barrett | Nexus leader | The Nexus | HIGH |
| Hawk and Animal (Road Warriors) | LOD has zero linkable members | Legion of Doom | HIGH |
| Dominik Mysterio | Judgment Day breakout | Judgment Day | HIGH |

### Secondary priority (round out a card)

| Name | Role | Faction(s) |
|---|---|---|
| X-Pac (Sean Waltman) | DX, nWo | D-Generation X, nWo |
| Road Dogg (Jesse James) | DX / New Age Outlaws | D-Generation X |
| Billy Gunn | DX / New Age Outlaws | D-Generation X |
| Tully Blanchard | Original Horseman | Four Horsemen |
| Barry Windham | Horseman; also a 2024 HOF gap in base research | Four Horsemen |
| Ole Anderson | Original Horseman | Four Horsemen |
| Dean Malenko | Horseman | Four Horsemen |
| Steve "Mongo" McMichael | Horseman | Four Horsemen |
| J.J. Dillon | Horsemen manager | Four Horsemen |
| Luke Harper | Wyatt Family | Wyatt Family |
| Erick Rowan | Wyatt Family | Wyatt Family |
| Braun Strowman | Wyatt Family breakout | Wyatt Family |
| Jacob Fatu | Bloodline 2025-2026 | The Bloodline |
| Tama Tonga | Bloodline and Bullet Club | The Bloodline, Bullet Club |
| JD McDonagh | Judgment Day | Judgment Day |
| Carlito | Judgment Day | Judgment Day |
| Jim "The Anvil" Neidhart | Hart Foundation co-founder | Hart Foundation |
| Shane McMahon | Corporation | The Corporation |
| Big Boss Man | Corporation | The Corporation |
| Ken Shamrock | Corporation | The Corporation |
| Karl Anderson, Luke Gallows, Bad Luck Fale, Jay White, Adam Cole | Bullet Club alumni | Bullet Club |
| David Otunga, Justin Gabriel, Heath Slater, Michael Tarver, Skip Sheffield (Ryback), Darren Young | Nexus rookies | The Nexus |
| Eric Bischoff | nWo authority figure (also a 2021 HOF gap) | nWo |

Note on personas already covered: Scott Hall links via `razor-ramon`; Diesel links via `kevin-nash`
(and the `diesel` persona page). Dean Ambrose links via `jon-moxley`.

---

## Notes for the build phase

- Launch-ready cards (every member links today): Evolution, The Shield.
- Near-ready (one or two gaps): Four Horsemen, D-Generation X, Judgment Day, Hart Foundation, The Corporation.
- Content-first opportunity (biggest gaps): The New Day and Legion of Doom have zero linkable members; building those wrestler pages plus the faction page together gives the most new internal links.
- Time-sensitive: The Bloodline and Judgment Day 2026 lineups are moving. Keep those two faction pages' "current status" line behind a `VERIFY` check at publish and set a review reminder.

## Consolidated source list

- nWo: https://www.wwe.com/videos/hulk-hogan-forms-the-nwo-with-scott-hall-and-kevin-nash-wcw-bash-at-the-beach-1996 ; https://en.wikipedia.org/wiki/New_World_Order_(professional_wrestling)
- DX: https://en.wikipedia.org/wiki/D-Generation_X ; https://www.wwe.com/superstars/d-generation-x
- Four Horsemen: https://en.wikipedia.org/wiki/The_Four_Horsemen_(professional_wrestling) ; https://www.onlineworldofwrestling.com/profile/four-horsemen/
- The Shield: https://www.si.com/wrestling/2022/11/16/roman-reigns-seth-rollins-dean-ambrose-the-shield-wwe-history
- The Bloodline: https://bleacherreport.com/articles/10141369-roman-reigns-jey-uso-jimmy-lose-to-the-bloodline-in-historic-wwe-crown-jewel-match ; https://itrwrestling.com/bio/the-bloodline/ ; https://lastwordonsports.com/prowrestling/2026/06/24/why-the-next-move-of-solo-sikoa-is-very-important/
- Judgment Day: https://en.wikipedia.org/wiki/The_Judgment_Day ; https://www.thesportster.com/wwe-judgment-day-every-member-role-group-ripley-dominik-balor-priest-edge/
- Bullet Club: https://www.si.com/wrestling/2023/05/03/njpw-bullet-club-anniversary-kenny-omega-finn-balor ; https://impact.fandom.com/wiki/Bullet_Club
- Evolution: https://en.wikipedia.org/wiki/Evolution_(professional_wrestling) ; https://www.wwe.com/classics/the-theory-of-evolution
- Wyatt Family: https://en.wikipedia.org/wiki/The_Wyatt_Family ; https://www.espn.com/wwe/story/_/id/18207147/wwe-profile-page-wyatt-family
- New Day: https://en.wikipedia.org/wiki/The_New_Day_(professional_wrestling) ; https://screenrant.com/new-day-complete-history-timeline-explained/
- Nexus: https://www.onlineworldofwrestling.com/profile/nexus/ ; https://simple.wikipedia.org/wiki/Nexus_(professional_wrestling)
- Hart Foundation: https://www.onlineworldofwrestling.com/profile/hart-foundation-2/ ; https://www.thesportster.com/wwe-hart-foundation-members-title-reigns-manager-facts-trivia/
- Corporation: https://en.wikipedia.org/wiki/The_Corporation_(professional_wrestling) ; https://en.wikipedia.org/wiki/Corporate_Ministry
- Legion of Doom: https://www.wwe.com/superstars/road-warriors ; https://sports.yahoo.com/articles/iconic-80s-powerhouse-duo-road-090000233.html
