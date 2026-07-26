# Wrestle Lore — Women's Division Dataset

Page-ready, verified dataset for the female roster, split CURRENT vs LEGEND. The build phase turns
each entry into a profile at the existing route pattern `/wrestlers/{slug}/`, and the two status
groups feed the female + current/legend filter lanes on the poster wall.

- Researcher role: Women's division
- Date of research: 2026-07-26
- Rule followed: no invented facts, quotes, or stats. Every row carries a confidence flag; anything
  time-sensitive (active title holdings, in-storyline results) is flagged because it moves week to week.
- Confidence legend: `HIGH` = multiple authoritative sources agree; `MED` = single reputable source or
  subject to change; `VERIFY` = confirm the exact detail before it goes on a published card.
- Copy standard: specific nouns, no decorative arrows, no em-dash separators, no filler adjectives,
  none of the banned cliche words.

## Route pattern

- Section index: `/wrestlers/` (shared with men; the female tag drives the filtered view).
- Profile page: `/wrestlers/{slug}/` (identical to the existing men's profiles).
- Status axis: each profile is tagged `current` or `legend` so the wall can build a "Women's Current"
  lane and a "Women's Legends" lane. This mirrors Axis A + Axis B in `00-content-data-research.md`.
- Cross-links: rivalry pages under `/rivalries/{slug}/`, tag entries under `/tag-teams/{slug}/`
  (see `data/tag-teams.md`), title lineages under `/titles/{slug}/` (see `data/titles-lineages.md`).

---

## Section A — CURRENT female roster (active 2026)

### A1. Already has a profile page (10)

| Wrestler | Slug (existing) | Key facts (verified) | Confidence | Source |
|---|---|---|---|---|
| Rhea Ripley | `rhea-ripley` | "Mami" / "The Nightmare." Adelaide, Australia. WWE Women's Champion in 2026 after beating Jade Cargill at WrestleMania Sunday, retained vs Cargill at Clash in Italy. Former Women's World and Women's Tag Team Champion (with IYO SKY, Jan 2026). | HIGH bio; MED/VERIFY current title state | espn.com; wwe.com; foxnews.com |
| Bianca Belair | `bianca-belair` | "The EST of WWE." Former Raw and SmackDown Women's Champion; won 2021 Royal Rumble; ex-collegiate track and field athlete. | HIGH | wwe.com; wikipedia |
| Liv Morgan | `liv-morgan` | Women's World Champion in 2026 (Raw side); entered 2026 Queen of the Ring while champion; former Women's Tag Team Champion. New Jersey native, ex-Riott Squad. | HIGH bio; MED/VERIFY current reign | wwe.com; wrestlinginc.com |
| IYO SKY | `iyo-sky` | 2026 Queen of the Ring tournament winner; challenged Women's World Champion Liv Morgan at SummerSlam 2026. Japanese star (ex-Io Shirai, Stardom); former Women's and Women's Tag Team Champion. | HIGH bio; MED/VERIFY current storyline | wwe.com; aol.com |
| Becky Lynch | `becky-lynch` | "The Man." Headlined WrestleMania 35 main event; multi-time Raw/SmackDown Women's Champion; Irish. 2026 WWE status is the subject of backstage reporting. | HIGH bio; VERIFY 2026 status | slamwrestling.net; sescoops.com |
| Charlotte Flair | `charlotte-flair` | Daughter of Ric Flair (`/wrestlers/ric-flair/`); record multi-time women's world champion; active on-screen in 2026 (interfered in Cargill vs Stratton at Night of Champions). | HIGH | wwe.com; fightful.com |
| Asuka | `asuka` | "The Empress of Tomorrow." Japanese; held a record undefeated WWE streak; former Raw/SmackDown and NXT Women's Champion; ex-Kabuki Warriors with Kairi Sane. | HIGH | wwe.com; wikipedia |
| Bayley | `bayley` | Longest-reigning SmackDown Women's Champion; ex-Four Horsewomen of NXT; former Damage CTRL leader. | HIGH | wwe.com; wikipedia |
| Natalya | `natalya` | Hart family (niece of Bret Hart, `/wrestlers/bret-hart/`); former Divas and SmackDown Women's Champion; longest-tenured woman on the roster. | HIGH | wwe.com; wikipedia |
| Mercedes Mone | `mercedes-mone` | Formerly Sasha Banks in WWE; ex-Four Horsewomen; now a multi-belt "CEO" champion in TNA/NJPW/AEW. Note: page already covers the Sasha Banks era, so do not build a separate `sasha-banks` slug. | HIGH | wikipedia; itrwrestling |

### A2. GAP — active in 2026, NO profile page yet (build these)

| Wrestler | Suggested slug | Key facts (verified) | Confidence | Source |
|---|---|---|---|---|
| Tiffany Stratton | `tiffany-stratton` | "The Buff Barbie." Ex-gymnast. Former NXT Women's Champion; cashed in Money in the Bank (won 2024). Held the WWE Women's Championship roughly 302 days, then won the WWE Women's United States Championship in 2026. | HIGH bio; MED current title | fightful.com; wwe.com; fandomwire |
| Jade Cargill | `jade-cargill` | Inaugural AEW TBS Champion; carried a long undefeated run that ended at Double or Nothing 2023; jumped to WWE (debut Nov 2023). Held the WWE Women's Championship in 2026 before losing to Rhea Ripley at WrestleMania. | HIGH bio; MED current state | pwtorch.com; allelitewrestling.com; wwe.com |
| Roxanne Perez | `roxanne-perez` | "The Prodigy." Former NXT Women's Champion; called up and active on the main roster in 2026 (Queen of the Ring, tag matches with Liv Morgan). | HIGH bio; MED brand | wwe.com; smackdownhotel roster |
| Alexa Bliss | `alexa-bliss` | Multi-time Raw/SmackDown Women's Champion; ex-gymnast; competed in 2026 Queen of the Ring. Long WWE tenure with several character eras. | HIGH | wwe.com; wikipedia |
| Chelsea Green | `chelsea-green` | "The Hot Mess" / self-styled first WWE Women's United States Champion; active 2026 title contender; Canadian. | HIGH bio; VERIFY exact current title claim | sportskeeda; smackdownhotel roster |
| Nia Jax | `nia-jax` | "The Irresistible Force." Former WWE and Raw Women's Champion; won Money in the Bank; part of the Anoa'i family. | HIGH | wwe.com; wikipedia |
| Kairi Sane | `kairi-sane` | "The Pirate Princess." Japanese; former NXT Women's Champion; ex-Kabuki Warriors and Damage CTRL with Asuka and IYO SKY. | HIGH | wwe.com; wikipedia |
| Raquel Rodriguez | `raquel-rodriguez` | Former Women's Tag Team Champion; power wrestler; ex-NXT Women's Tag Champion. | HIGH | wwe.com; wikipedia |
| Lyra Valkyria | `lyra-valkyria` | Former NXT Women's Champion; inaugural WWE Women's Intercontinental Champion; Irish. | MED/VERIFY inaugural claim | wwe.com; smackdownhotel roster |
| Dakota Kai | `dakota-kai` | New Zealand; ex-Damage CTRL; former Women's Tag Team Champion. | HIGH | wwe.com; wikipedia |
| Zelina Vega | `zelina-vega` | Former Queen of the Ring winner and Women's Tag Team Champion; manager and in-ring competitor. | HIGH | wwe.com; wikipedia |
| Rhea-tier depth (build after the above): Tegan Nox, Michin (Mia Yim), B-Fab, Piper Niven, Isla Dawn, Maxxine Dupri, Jakara Jackson, Jaida Parker | slug = kebab of ring name | Active or recently active 2026 undercard and tag names surfacing in Raw/SmackDown match cards. | MED/VERIFY per name | smackdownhotel roster; wwe.com show pages |

---

## Section B — LEGEND female roster (retired / historic)

### B1. Already has a profile page (3)

| Wrestler | Slug (existing) | Key facts (verified) | Confidence | Source |
|---|---|---|---|---|
| Trish Stratus | `trish-stratus` | Seven-time WWE Women's Champion; 2013 WWE Hall of Fame; headlined a 2004 Raw main event; face of the early-2000s division. | HIGH | wwe.com; simple.wikipedia |
| Lita | `lita` | Four-time Women's Champion; high-flying pioneer; longtime Trish Stratus rival; 2014 WWE Hall of Fame; ex-Team Xtreme with the Hardys. | HIGH | wikipedia; wwe.com |
| Chyna | `chyna` | "The Ninth Wonder of the World." First woman in the Royal Rumble and King of the Ring; two-time Intercontinental Champion; ex-D-Generation X. | HIGH | wikipedia |

### B2. GAP — legends with NO profile page yet (build these)

| Wrestler | Suggested slug | Key facts (verified) | Confidence | Source |
|---|---|---|---|---|
| The Fabulous Moolah | `fabulous-moolah` | Record longest-recognized WWE Women's Championship run (decades across reigns, first won in the 1950s). Legacy is genuinely contested over her treatment of trainees, so copy must present both her record and the documented criticism, not a clean hagiography. | HIGH record; HIGH that legacy is disputed | wikipedia (1956-2010 title); lastwordonsports; thesportster |
| Bull Nakano | `bull-nakano` | Japanese legend (All Japan Women's / AJW); former WWF Women's Champion after beating Alundra Blayze; 2024 WWE Hall of Fame. Iconic hair and face paint; renowned brawls with Aja Kong. | HIGH | postwrestling; wwe.com; comicbook |
| Sable | `sable` | Attitude Era headline attraction; former WWF Women's Champion; landmark late-90s crossover star. | HIGH | wikipedia |
| Beth Phoenix | `beth-phoenix` | "The Glamazon." Multi-time Women's/Divas Champion; 2017 WWE Hall of Fame; power-wrestling standout. | HIGH | wikipedia; wwe.com |
| Mickie James | `mickie-james` | Multi-time WWE and Impact/TNA women's champion; ran the famous obsessed-fan storyline with Trish Stratus. | HIGH | wikipedia |
| AJ Lee | `aj-lee` | Record-setting Divas Champion (longest single Divas title reign); face of the "Divas Revolution" push. | HIGH | wikipedia |
| Sensational Sherri | `sensational-sherri` | Manager and champion; former WWF Women's Champion; 2006 WWE Hall of Fame; managed Randy Savage and Shawn Michaels. | HIGH | wikipedia |
| Wendi Richter | `wendi-richter` | "Rock 'n' Wrestling Connection" star of the 1980s; former WWF Women's Champion; 2010 WWE Hall of Fame. | HIGH | wikipedia |
| Gail Kim | `gail-kim` | WWE Women's Champion and record-setting Impact/TNA Knockouts Champion; TNA Hall of Fame; former Knockouts division cornerstone. | HIGH | wikipedia |
| Awesome Kong / Kharma | `awesome-kong` | Dominant TNA Knockouts Champion (as Awesome Kong) who also wrestled in WWE as Kharma; power/monster archetype. | HIGH | wikipedia |
| Ivory | `ivory` | Three-time WWF Women's Champion; ex-Right to Censor; 2018 WWE Hall of Fame (as part of a group). | MED/VERIFY HOF detail | wikipedia |
| Molly Holly | `molly-holly` | Two-time Women's Champion; 2021 WWE Hall of Fame; noted for her hardcore-era title work. | HIGH | wikipedia; SI HOF list |
| Victoria | `victoria` | Former WWE Women's Champion; hardcore-match innovator in the early-2000s division. | HIGH | wikipedia |
| Madusa / Alundra Blayze | `alundra-blayze` | WWF Women's Champion (as Alundra Blayze) and WCW/AWA star (as Madusa); 2015 WWE Hall of Fame; famous WCW title-toss angle. | HIGH | wikipedia |
| Mae Young | `mae-young` | Pioneer whose career spanned nine decades; 2008 WWE Hall of Fame; Attitude Era comedy and hardcore appearances. | HIGH | wikipedia |
| Jacqueline | `jacqueline` | Former WWF/WWE Women's Champion and Cruiserweight Champion; 2016 WWE Hall of Fame. | HIGH | wikipedia |
| Jazz | `jazz` | Former WWE Women's Champion; ECW alumna; hard-hitting early-2000s heel. | MED | wikipedia |
| Aja Kong | `aja-kong` | Japanese joshi legend (AJW); headline rival of Bull Nakano; touchstone for the puroresu women's style. | HIGH | wikipedia |
| Manami Toyota | `manami-toyota` | Widely cited joshi great (AJW); reference point for high-workrate women's matches. | MED (acclaim well documented; specific title lines VERIFY) | wikipedia |

---

## Gap List — priority build order

Biggest, highest-value gaps (build first because they are top-billed and already collide with
existing pages via rivalries and current storylines):

1. `tiffany-stratton` — reigning-caliber current headliner, no page. Highest priority.
2. `jade-cargill` — current headliner, AEW-to-WWE crossover, WrestleMania 2026 title match. Highest priority.
3. `fabulous-moolah` — the single most historically significant missing woman; anchors the Legends lane (with the documented-legacy caveat).
4. `bull-nakano` — 2024 Hall of Famer, only Japanese woman flagged in the base research; anchors an international-legends angle alongside `aja-kong` and `manami-toyota`.
5. `roxanne-perez`, `alexa-bliss`, `chelsea-green`, `nia-jax` — active main-roster names appearing in 2026 match cards, needed so event and rivalry links do not 404.
6. Legends depth: `sable`, `beth-phoenix`, `mickie-james`, `aj-lee`, `gail-kim`, `awesome-kong`.
7. Historic title-lineage names: `alundra-blayze`, `sensational-sherri`, `wendi-richter`, `mae-young`, `molly-holly`, `victoria`, `ivory`, `jacqueline`, `jazz`.

Count snapshot: 13 female profiles exist today (10 current + 3 legend). This dataset adds roughly
11 current gaps and 19 legend gaps, which would take the division to about 43 profiles and give the
current/legend filter real weight on both sides.

## Cross-link opportunities to existing pages

- Charlotte Flair links to her father Ric Flair (`/wrestlers/ric-flair/`).
- Natalya links to Bret Hart (`/wrestlers/bret-hart/`) and the Hart Foundation entries in `data/tag-teams.md`.
- Rivalry pages to seed under `/rivalries/`: Trish Stratus vs Lita; Rhea Ripley vs Jade Cargill (2026);
  Liv Morgan vs IYO SKY (2026); Bull Nakano vs Alundra Blayze; Bull Nakano vs Aja Kong.
- Tag entries for `data/tag-teams.md`: Kabuki Warriors (Asuka, Kairi Sane), Damage CTRL
  (Bayley, IYO SKY, Dakota Kai, Kairi Sane), Rhea Ripley and IYO SKY (2026 Women's Tag Champions).
- Title lineages for `data/titles-lineages.md`: WWE Women's Championship, Women's World Championship,
  WWE Women's United States Championship, WWE Women's Tag Team Championship, and the historic
  WWE Women's Championship (1956-2010, the Moolah/Blayze/Richter line).

## Source notes

- Current title states (Rhea Ripley, Liv Morgan, Tiffany Stratton, Jade Cargill) are drawn from 2026
  WWE.com show pages plus Fightful, ESPN, Forbes, Newsweek, and Fox coverage. These are in-storyline
  and shift week to week, so every "current champion" claim carries MED/VERIFY and should be
  re-checked at build time rather than hard-coded.
- Biographical and career-accolade facts (Hall of Fame years, historic reigns, finishers, family
  ties) are HIGH: confirmed on WWE.com and Wikipedia and consistent across the outlets above.
- No quotes are reproduced. No reign lengths beyond the ones directly reported (Stratton ~302 days as
  WWE Women's Champion; Moolah's decades-long recognized run) are stated as fact.
- Fabulous Moolah's legacy is deliberately framed as contested per Last Word on Pro Wrestling and
  The Sportster; do not publish a one-sided tribute.

### Consolidated source URLs
- https://en.wikipedia.org/wiki/Women%27s_World_Championship_(WWE)
- https://en.wikipedia.org/wiki/WWE_Women%27s_Championship
- https://en.wikipedia.org/wiki/WWE_Women%27s_Championship_(1956%E2%80%932010)
- https://www.fightful.com/wrestling/tiffany-stratton-passes-250-days-as-wwe-womens-champion/
- https://sports.yahoo.com/articles/tiffany-stratton-makes-history-wwe-013625439.html
- https://www.wwe.com/shows/wrestlemania/sunday-2026/cargill-vs-ripley-wrestlemania-sunday-2026
- https://www.foxnews.com/sports/rhea-ripley-curiously-gets-help-charlotte-flair-retain-womens-title-wwe-clash-italy
- https://www.wwe.com/shows/summerslam/2026/liv-morgan-vs-iyo-sky
- https://www.wrestlinginc.com/2184628/liv-morgan-wwe-queen-of-the-ring-2026-womens-world-title/
- https://www.pwtorch.com/site/2023/05/28/jade-cargill-undefeated-streak-ends-new-tbs-champion-crowned-at-double-or-nothing/
- https://www.postwrestling.com/2024/03/06/bull-nakano-joins-2024-wwe-hall-of-fame-class/
- https://lastwordonsports.com/prowrestling/2018/03/13/the-brutal-history-of-fabulous-moolah/
- https://www.thesmackdownhotel.com/roster/wwe/
