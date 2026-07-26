# Wrestle Lore — Content Manifest

Master build list for the content-operations phase. Consolidates all nine page-ready datasets in
`/root/wwe/docs/design/wrestle-lore/data/` into one buildable plan: every new page, its route, its
source dataset, its cross-links, its priority, and one consolidated gap list of wrestlers and
entities to add.

- Compiled: 2026-07-26
- Baseline verified against `/root/wwe/wrestlers/` (89 existing profiles, plus persona pages).
- Confidence legend: `HIGH` = multiple authoritative sources agree; `MED` = single source or moving; `VERIFY` = recheck on publish day.
- Copy standard for every page authored from this manifest: specific nouns, no decorative arrows, no em-dash separators, none of the banned cliche words.
- Source datasets (short codes used below): TL titles-lineages, FS factions-stables, TT tag-teams, NJ njpw-and-ajstyles, WD womens-division, CR current-roster-expansion, HOF hall-of-fame, IM influencers-media, SM streaming-matrix.

---

## 1. New-page count by type

| Type | Route family | New pages | Notes |
|---|---|---|---|
| Title lineages | `/titles/{slug}/` + `/titles/` | 14 | 13 title pages + 1 hub |
| Factions | `/factions/{slug}/` + `/factions/` | 15 | 14 faction pages + 1 hub |
| Tag teams | `/tag-teams/{slug}/` + `/tag-teams/` | 18 | 17 team pages + 1 hub |
| Hall of Fame | `/hall-of-fame/` + `/hall-of-fame/{year}/` | 6 | 1 hub + 5 class pages (2022-2026) |
| Media and Creators | `/media/{slug}/` + `/media/` | 18 | 1 hub + 13 people (11 pure + 2 dual-role) + 4 outlet tiles |
| Watch (where to watch) | `/watch/{promotion}/` + `/watch/` | 7 | 1 hub + 6 per-promotion pages; plus a reusable badge component (not a page) |
| Promotions | `/promotions/{slug}/` | 2 | njpw, aew (both new) |
| Showcase (optional) | `/showcases/{slug}/` | 1 | aj-styles retrospective (optional) |
| **Structural subtotal** | | **81** | hubs, section pages, and title/faction/tag/HOF/media/watch cards |
| Wrestler profiles | `/wrestlers/{slug}/` | ~130 | consolidated gap list, section 4 |
| **Grand total (new pages)** | | **~211** | |

---

## 2. Master build table — structural and section pages

Route, page title, source dataset, cross-link status, and build wave. Wrestler profiles are counted
separately in section 4.

### 2.1 Titles (source: TL) — route `/titles/{slug}/`

| Route | Page title | Cross-links ready today | Wave |
|---|---|---|---|
| `/titles/` | Championships hub (current-champions snapshot + grid) | mixed | NOW |
| `/titles/undisputed-wwe-championship/` | Undisputed WWE Championship | cm-punk, sami-zayn, roman-reigns, cody-rhodes | NOW |
| `/titles/world-heavyweight-championship/` | World Heavyweight Championship (WWE) | roman-reigns, seth-rollins, gunther | NOW |
| `/titles/intercontinental-championship/` | WWE Intercontinental Championship | gunther, randy-savage, ricky-steamboat, chris-jericho | NOW |
| `/titles/united-states-championship/` | WWE United States Championship | ric-flair, john-cena, lex-luger | NOW |
| `/titles/womens-world-championship/` | Women's World Championship (Raw) | liv-morgan, becky-lynch, rhea-ripley, bianca-belair | NOW |
| `/titles/wwe-womens-championship/` | WWE Women's Championship (SmackDown) | rhea-ripley, charlotte-flair, bayley | NOW |
| `/titles/wwe-tag-team-championship/` | WWE Tag Team Championship | damian-priest | NEXT |
| `/titles/world-tag-team-championship/` | World Tag Team Championship | (gap-heavy) | NEXT |
| `/titles/wcw-world-heavyweight-championship/` | WCW World Heavyweight Championship (retired) | booker-t, ric-flair, hulk-hogan, goldberg, sting | NEXT |
| `/titles/ecw-world-heavyweight-championship/` | ECW World Heavyweight Championship (retired) | bobby-lashley | LATER |
| `/titles/iwgp-heavyweight-championship/` | IWGP Heavyweight Championship (NJPW) | aj-styles, jon-moxley, finn-balor | NEXT |
| `/titles/aew-world-championship/` | AEW World Championship | chris-jericho, jon-moxley, cm-punk, samoa-joe | NEXT |
| `/titles/tna-world-championship/` | TNA World Championship | kurt-angle, aj-styles, samoa-joe, sting | NEXT |

VERIFY at publish: IWGP reign numbering (MED, confirm 87th-champion count with NJPW/Puroresu System);
the 2023-2026 World Heavyweight reign chain; SummerSlam 2026 interim WWE Women's Champion result.

### 2.2 Factions (source: FS) — route `/factions/{slug}/`

| Route | Page title | Readiness | Wave |
|---|---|---|---|
| `/factions/` | Factions and stables hub | mixed | NOW |
| `/factions/evolution/` | Evolution | fully linkable (triple-h, ric-flair, randy-orton, batista) | NOW |
| `/factions/the-shield/` | The Shield | fully linkable (roman-reigns, seth-rollins, jon-moxley) | NOW |
| `/factions/four-horsemen/` | Four Horsemen | near-ready | NOW |
| `/factions/d-generation-x/` | D-Generation X | near-ready | NOW |
| `/factions/nwo/` | nWo (New World Order) | near-ready | NOW |
| `/factions/judgment-day/` | The Judgment Day | near-ready (VERIFY 2026 lineup) | NEXT |
| `/factions/the-bloodline/` | The Bloodline | near-ready (VERIFY 2026 lineup) | NEXT |
| `/factions/hart-foundation/` | The Hart Foundation (stable) | near-ready | NEXT |
| `/factions/the-corporation/` | The Corporation | near-ready | NEXT |
| `/factions/bullet-club/` | Bullet Club | near-ready (finn-balor, aj-styles, cody-rhodes) | NEXT |
| `/factions/the-nexus/` | The Nexus | near-ready | LATER |
| `/factions/wyatt-family/` | The Wyatt Family | gap-heavy (VERIFY Bray Wyatt passing note) | LATER |
| `/factions/the-new-day/` | The New Day (stable) | zero linkable members | LATER |
| `/factions/legion-of-doom/` | Legion of Doom (stable) | zero linkable members | LATER |

### 2.3 Tag teams (source: TT) — route `/tag-teams/{slug}/`

| Route | Page title | Readiness | Wave |
|---|---|---|---|
| `/tag-teams/` | Tag teams hub | mixed | NOW |
| `/tag-teams/hardy-boyz/` | The Hardy Boyz | fully linkable | NOW |
| `/tag-teams/edge-and-christian/` | Edge and Christian | fully linkable | NOW |
| `/tag-teams/brothers-of-destruction/` | The Brothers of Destruction | fully linkable | NOW |
| `/tag-teams/rock-n-sock-connection/` | The Rock 'n' Sock Connection | fully linkable | NOW |
| `/tag-teams/the-outsiders/` | The Outsiders | fully linkable | NOW |
| `/tag-teams/brain-busters/` | The Brain Busters | one gap (tully-blanchard) | NEXT |
| `/tag-teams/dudley-boyz/` | The Dudley Boyz | one gap (d-von) | NEXT |
| `/tag-teams/hart-foundation/` | The Hart Foundation (duo) | one gap (neidhart) | NEXT |
| `/tag-teams/the-rockers/` | The Rockers | one gap (jannetty) | NEXT |
| `/tag-teams/british-bulldogs/` | The British Bulldogs | one gap (dynamite-kid) | NEXT |
| `/tag-teams/the-usos/` | The Usos | zero linkable members | NEXT |
| `/tag-teams/the-new-day/` | The New Day (duo/trio) | zero linkable members | LATER |
| `/tag-teams/young-bucks/` | The Young Bucks | zero linkable members | LATER |
| `/tag-teams/steiner-brothers/` | The Steiner Brothers | zero linkable members | LATER |
| `/tag-teams/legion-of-doom/` | Legion of Doom (duo) | zero linkable members | LATER |
| `/tag-teams/demolition/` | Demolition | zero linkable members | LATER |
| `/tag-teams/ftr/` | FTR | zero linkable members | LATER |

Overlap note: `hart-foundation`, `legion-of-doom`, and `the-new-day` exist in both FS and TT. Per the
TT disambiguation rule, keep the tag-team page as the two-man/duo act and the faction page as the
larger stable, and cross-link the two. Do not merge, do not double-count in totals (each pair is two
distinct pages by design).

### 2.4 Hall of Fame (source: HOF) — route `/hall-of-fame/`

| Route | Page title | Headliner cross-link | Wave |
|---|---|---|---|
| `/hall-of-fame/` | WWE Hall of Fame hub (most-decorated + two-time club) | ric-flair | NOW |
| `/hall-of-fame/2026/` | Class of 2026 | aj-styles | NOW |
| `/hall-of-fame/2025/` | Class of 2025 | triple-h | NOW |
| `/hall-of-fame/2024/` | Class of 2024 | (Paul Heyman, gap) | NEXT |
| `/hall-of-fame/2023/` | Class of 2023 | rey-mysterio | NEXT |
| `/hall-of-fame/2022/` | Class of 2022 | the-undertaker | NEXT |

Correction carried from HOF dataset: the true last-5 window is 2022-2026 (Class of 2026 inducted
Apr 17, 2026), not the base doc's 2021-2025. Do not print "Flair is the only two-time inductee."

### 2.5 Media and Creators (source: IM) — route `/media/{slug}/`

| Route | Page title | Tier | Wave |
|---|---|---|---|
| `/media/` | Media and Creators hub | required | NOW |
| `/media/chris-van-vliet/` | Chris Van Vliet | hero | NOW |
| `/media/ariel-helwani/` | Ariel Helwani | high-authority | NEXT |
| `/media/sean-ross-sapp/` | Sean Ross Sapp | high-authority | NEXT |
| `/media/dave-meltzer/` | Dave Meltzer | high-authority (links `/matches/` star ratings) | NEXT |
| `/media/conrad-thompson/` | Conrad Thompson | high-authority | NEXT |
| `/media/denise-salcedo/` | Denise Salcedo | second tier | NEXT |
| `/media/peter-rosenberg/` | Peter Rosenberg | second tier | LATER |
| `/media/dave-lagreca/` | Dave LaGreca | second tier | LATER |
| `/media/renee-paquette/` | Renee Paquette (links jon-moxley) | second tier (VERIFY podcast status) | LATER |
| `/media/bully-ray/` | Bully Ray (dual-role, links `/wrestlers/bully-ray/`) | dual-role | LATER |
| `/media/jim-cornette/` | Jim Cornette (dual-role) | dual-role | LATER |
| `/media/wade-keller/` | Wade Keller | optional (VERIFY role) | LATER |
| `/media/sam-roberts/` | Sam Roberts | optional (VERIFY role) | LATER |
| `/media/fightful/` | Fightful (outlet tile) | outlet | NEXT |
| `/media/wrestling-observer/` | Wrestling Observer (outlet tile) | outlet | NEXT |
| `/media/pwtorch/` | PWTorch (outlet tile) | outlet | LATER |
| `/media/wrestletalk/` | WrestleTalk (outlet tile) | outlet | LATER |

Feature the WrestleTalk brand, not Adam Blampied (2017 controversy). Do not call Renee Paquette's
"The Sessions" active. Eric Bischoff and Bruce Prichard need wrestler pages before Conrad Thompson's
show cross-links resolve (tracked in section 4).

### 2.6 Watch and Promotions (source: SM, NJ) — routes `/watch/{promotion}/`, `/promotions/{slug}/`

| Route | Page title | Wave |
|---|---|---|
| `/promotions/njpw/` | New Japan Pro-Wrestling (promotion overview) | NOW |
| `/promotions/aew/` | All Elite Wrestling (promotion overview) | NOW |
| `/watch/` | Where to watch hub | NEXT |
| `/watch/wwe/` | Where to watch WWE | NEXT |
| `/watch/aew/` | Where to watch AEW | NEXT |
| `/watch/njpw/` | Where to watch NJPW | NEXT |
| `/watch/tna/` | Where to watch TNA | NEXT |
| `/watch/wcw/` | Where to watch WCW (archive offline) | LATER |
| `/watch/ecw/` | Where to watch ECW (archive offline) | LATER |
| `/showcases/aj-styles/` | AJ Styles retrospective (optional) | LATER |

Plus a reusable "where to watch" badge component (renders on `/promotions/` and `/events/` cards; not
a page). WCW/ECW archive status is MED/VERIFY: the badges must say the library is offline, not point to
Netflix. `/promotions/aew/` is the biggest structural gap for the streaming matrix. AJ Styles is
CONFIRMED retired (lost to Gunther, Royal Rumble Jan 31, 2026), but do not print "retired" on any
title page until that flag is cleared per TL.

---

## 3. Reverse cross-link work on existing wrestler pages (not new pages, but build tasks)

Existing profiles gain "Factions", "Tag Teams", and "Titles" strips that link into the new sections.
Priority targets already carrying multiple new links: roman-reigns, seth-rollins, jon-moxley,
triple-h, ric-flair, shawn-michaels, edge, christian, the-rock, bret-hart, the-undertaker, kane,
matt-hardy, jeff-hardy, bully-ray, razor-ramon, kevin-nash, arn-anderson, cm-punk, sami-zayn,
rey-mysterio, aj-styles, finn-balor, cody-rhodes, gunther, rhea-ripley, liv-morgan, charlotte-flair.

---

## 4. Consolidated gap list — wrestler profiles to build (`/wrestlers/{slug}/`)

Deduplicated across all datasets. Grouped by build wave. Slug = kebab of ring name unless noted.

### 4.1 WAVE NOW — current champions and marquee current stars (highest demand x readiness)

These kill the most 404s from the current-champions snapshot, the title pages, and live storylines.

`penta` (IC champ), `trick-williams` (US/TNA champ), `r-truth` (tag champ), `bron-breakker` (tag champ),
`austin-theory` (tag champ), `yota-tsuji` (IWGP champ, MED numbering), `kenny-omega` (AEW champ),
`nic-nemeth` (TNA champ), `tiffany-stratton` (women's champ), `jade-cargill`, `jey-uso`, `jacob-fatu`
(US champ), `solo-sikoa`, `kazuchika-okada` (AEW Unified champ), `will-ospreay`, `mjf`, `oba-femi`
(NXT champ), `dominik-mysterio`. (18)

### 4.2 WAVE NEXT — top current stars, faction/tag marquee, key legends

Current/recent: `jimmy-uso`, `rey-fenix`, `swerve-strickland`, `hangman-page`, `toni-storm`
(VERIFY absence), `jay-white`, `tetsuya-naito`, `hiroshi-tanahashi` (retired Jan 2026).
Faction and tag marquee (unlock zero-linkable cards): `kofi-kingston`, `big-e`, `xavier-woods`
(New Day), `matt-jackson`, `nick-jackson` (Young Bucks), `bray-wyatt` (VERIFY passing note),
`paul-heyman`, `wade-barrett`, `road-warrior-hawk`, `road-warrior-animal`, `rick-steiner`,
`scott-steiner` (2022 HOF), `braun-strowman`, `tama-tonga`, `adam-cole`, `karl-anderson`,
`luke-gallows`.
Women current depth: `roxanne-perez`, `alexa-bliss`, `chelsea-green`, `nia-jax`, `kairi-sane`.
Legends women (anchor the Legends lane): `fabulous-moolah` (contested-legacy caveat), `bull-nakano`
(2024 HOF), `sable`, `beth-phoenix`, `mickie-james`, `aj-lee`. (~40)

### 4.3 WAVE LATER — depth, legacy, and HOF completion

Legacy men and global: `rob-van-dam`, `rhyno`, `the-sandman`, `tommy-dreamer`, `taz`, `shane-douglas`
(ECW); `kota-ibushi`, `zack-sabre-jr` (NJPW); `bruno-sammartino`, `honky-tonk-man`, `harley-race` (WWE history).
Legends women: `gail-kim`, `awesome-kong`, `sensational-sherri`, `wendi-richter`, `alundra-blayze`,
`mae-young`, `molly-holly`, `victoria`, `ivory`, `jacqueline`, `jazz`, `aja-kong`, `manami-toyota`.
Women current depth 2: `raquel-rodriguez`, `lyra-valkyria`, `dakota-kai`, `zelina-vega`
(plus optional undercard: `tegan-nox`, `michin`, `piper-niven`, `b-fab`, `isla-dawn`, `maxxine-dupri`,
`jakara-jackson`, `jaida-parker`).
Faction/tag secondary members: `d-von-dudley`, `marty-jannetty`, `dynamite-kid`, `jim-neidhart`,
`tully-blanchard`, `ax`, `smash`, `cash-wheeler`, `dax-harwood`, `paul-ellering`, `x-pac`,
`road-dogg`, `billy-gunn`, `barry-windham`, `ole-anderson`, `dean-malenko`, `steve-mcmichael`,
`jj-dillon`, `luke-harper`, `erick-rowan`, `shane-mcmahon`, `big-boss-man`, `ken-shamrock`,
`bad-luck-fale`, `jd-mcdonagh`, `carlito`, `eric-bischoff`, `bruce-prichard`, `david-otunga`,
`justin-gabriel`, `heath-slater`, `michael-tarver`, `ryback`, `darren-young`.
HOF-only inductee tiles (may be non-roster; build as needed to resolve HOF links):
`stephanie-mcmahon`, `the-great-muta`, `michelle-mccool`, `stacy-keibler`, `queen-sharmell`,
`bad-news-brown`, `shad-gaspard`, `thunderbolt-patterson`, `lia-maivia`, `mike-rotunda`,
`earthquake`, `typhoon`. Celebrity tiles (HOF only, not wrestlers): `dennis-rodman`, `muhammad-ali`,
`andy-kaufman`. (~75)

Approximate consolidated total: ~130 new wrestler profiles (plus ~11 optional undercard/depth and
3 HOF celebrity tiles). Existing 89 profiles already resolve for the launch-ready cards in Wave NOW.

---

## 5. Build waves at a glance

| Wave | What ships | Why |
|---|---|---|
| NOW | `/titles/` hub + 6 core WWE title pages; `/factions/` hub + Evolution, The Shield, Four Horsemen, DX, nWo; `/tag-teams/` hub + 5 fully-linkable duos; `/hall-of-fame/` hub + 2026 and 2025 classes; `/media/` hub + Chris Van Vliet; `/promotions/njpw/` and `/promotions/aew/`; ~18 current-champion wrestler profiles | High demand and high readiness. Current-champions snapshot goes live, launch-ready faction/tag/HOF cards need few or no new profiles. |
| NEXT | Remaining titles (tag, world, legacy, global); Bloodline, Judgment Day, Bullet Club, Corporation, Hart Foundation; near-ready tag teams and the zero-linkable marquee teams (Usos, New Day, Young Bucks); HOF 2022-2024; high-authority media + outlet tiles; `/watch/` hub + 4 active-promotion watch pages; ~40 wrestler profiles | Strong demand, needs the Wave NOW member profiles first to remove 404s. |
| LATER | ECW title, Wyatt Family, New Day and Legion of Doom faction/tag pages; second-tier and dual-role media; WCW/ECW watch pages; AJ Styles showcase; ~75 legacy, depth, and HOF-completion wrestler profiles | Lower live demand or heavy profile dependencies; content-first work that deepens the archive. |

---

## 6. Cross-dataset flags for the build phase

- Title pictures move weekly. Every "current champion" claim (TL, CR, WD) is MED/VERIFY; recheck on publish day against wwe.com and allelitewrestling.com.
- IWGP reactivation and Yota Tsuji reign numbering: MED, single-source. Confirm before printing reign counts.
- The Bloodline and Judgment Day 2026 lineups are shifting: VERIFY the "current status" line at publish and set a review reminder.
- Bray Wyatt (Windham Rotunda) died in 2023: keep to one plain factual sentence, VERIFY wording.
- Kofi Kingston and Xavier Woods released May 3, 2026: frame The New Day as a retrospective, not an active act.
- Fabulous Moolah: present the record and the documented criticism, not a one-sided tribute.
- WCW/ECW archives are offline as of mid-2026: badges must not point to Netflix.
- AJ Styles retirement is CONFIRMED, but the "retired" flag stays off title pages until TL clears it.
- Slug collisions handled: Sasha Banks routes through `mercedes-mone`; Dean Ambrose and Diesel route through `jon-moxley` and `kevin-nash`/`diesel`; `hart-foundation`, `legion-of-doom`, and `the-new-day` are intentional dual pages (faction + tag).
