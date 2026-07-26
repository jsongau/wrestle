# Wrestle Lore — NJPW Promotion + AJ Styles Dossier

Page-ready, verified datasets for the build phase. NJPW specialist deliverable. Goes deeper than
`00-content-data-research.md`. Every fact carries a source note and a confidence flag. No fabricated
facts, quotes, or stats; anything uncertain is flagged.

- Date of research: 2026-07-26
- Confidence legend: `HIGH` = multiple/authoritative sources agree; `MED` = single reputable source or subject to change; `VERIFY` = confirm before publishing.
- Route patterns:
  - Promotion overview page: **`/promotions/njpw/`** (new; sits beside wwe/wcw/ecw/tna/nxt).
  - New wrestler profiles: **`/wrestlers/{slug}/`** (matches existing convention).
  - AJ Styles flagship: enhance existing **`/wrestlers/aj-styles/`**; optional showcase route **`/showcases/aj-styles/`** for the three-promotion retrospective.
- Cross-link convention: names link to `/wrestlers/{slug}/` when a profile already exists; otherwise the slug is a GAP (see section 6).

---

## 1. NJPW Promotion Overview (`/promotions/njpw/`)

### Brand facts card

| Field | Value | Confidence | Source |
|---|---|---|---|
| Full name | New Japan Pro-Wrestling (NJPW) | HIGH | Wikipedia; njpw.fandom |
| Founded | 1972 by Antonio Inoki | HIGH | Wikipedia; Puroresu System |
| Home country | Japan (HQ Tokyo); largest promotion in Japan | HIGH | Wikipedia |
| Owner | Bushiroad (acquired NJPW in 2012) | HIGH | Wikipedia |
| Domestic TV | TV Asahi (Japan) | HIGH | Wikipedia |
| Flagship event | Wrestle Kingdom, held annually January 4 at the Tokyo Dome | HIGH | NJPW; Forbes 2026-01-04 |
| Signature tournaments | G1 Climax (summer), New Japan Cup (spring), Best of the Super Jr. | HIGH | NJPW records |
| Style tag | Strong style; "King of Sports" positioning | MED | widely reported |
| Suggested accent color | Deep NJPW red/black (propose `#c1272d`); VERIFY against official 2026 branding before locking | VERIFY | brand-palette check pending |

### Where NJPW streams NOW (verified 2026-07-26)

| Platform | What you get | Region | Confidence | Source |
|---|---|---|---|---|
| **NJPW World** (njpwworld.com) | The promotion's own subscription; live + full archive; apps on Roku, Apple TV, Android/Google Play | Global | HIGH | njpwworld.com; Roku/Google Play/App Store listings |
| **TrillerTV** (formerly FITE) | NJPW and "NJPW of America" live streams + library | US / intl | HIGH | trillertv.com/channel/new-japan-pro-wrestling; F4W guide |
| TV Asahi | Broadcast | Japan | HIGH | Wikipedia |

Card copy building block (no banned words, specific nouns): "Watch New Japan on NJPW World, the
promotion's own subscription with the full Tokyo Dome archive, or on TrillerTV in the US. In Japan it
airs on TV Asahi."

### IWGP title picture — reworked in January 2026 (feature this; it is genuinely surprising)

NJPW **reunified then re-split** its top title at Wrestle Kingdom 20 week. Yota Tsuji won the IWGP
World Heavyweight Championship from Konosuke Takeshita on Jan 4, 2026, then split the belt back into
its original parts and **restored the IWGP Heavyweight Championship**, which had been retired since
the 2021 Ibushi unification.

| Title | 2026 status | Current holder (as of research date) | Confidence | Source |
|---|---|---|---|---|
| **IWGP Heavyweight Championship** | **Reinstated Jan 6, 2026**; NJPW's restored top singles title, defended in Japan | **Yota Tsuji** (recognized as 87th champion) | HIGH | Fightful; 411Mania; Wrestling Inc. |
| IWGP World Heavyweight Championship | Retired / split back into components in Jan 2026 | n/a (last: Yota Tsuji, briefly) | HIGH | Fightful |
| IWGP Intercontinental Championship | Remains retired (folded in 2021) | n/a | HIGH | Fightful; Wikipedia |
| IWGP Global Heavyweight Championship | Active as a separate title for international/touring defenses | VERIFY current holder (Andrade El Idolo was a 2026 challenger) | MED | Wikipedia; AOL/AEW report |
| IWGP Junior Heavyweight Championship | Active (cruiserweight division) | VERIFY current holder | MED | NJPW records |
| IWGP Tag Team + Jr. Tag Championships | Active | VERIFY current holders | MED | NJPW records |

Note for build: if `/titles/` pages are built (see titles-lineages.md), the IWGP Heavyweight
Championship gets its own lineage page at `/titles/iwgp-heavyweight-championship/`. Reign numbers
past #87 are MED — confirm with NJPW/Puroresu System before printing counts.

Slug suggestion for the promotion page: `njpw` (`/promotions/njpw/`). Alt display name "New Japan
Pro-Wrestling."

---

## 2. Key Figures (cross-links + slug suggestions)

Verified current status. Several marquee names have LEFT NJPW — do not present them as current NJPW
roster; present them as NJPW legends / alumni with their current home noted.

| Wrestler | NJPW claim to fame | Status 2026 | Existing page? | Slug suggestion | Confidence | Source |
|---|---|---|---|---|---|---|
| **Kazuchika Okada** | "The Rainmaker"; multi-time IWGP Heavyweight Champion; face of NJPW 2010s | Left NJPW; **in AEW** (won AEW singles gold, e.g. Continental/International titles) | none (GAP) | `kazuchika-okada` | HIGH | Wikipedia; Sportskeeda; AEW results |
| **Hiroshi Tanahashi** | "The Ace" who rebuilt NJPW; multi-time IWGP Heavyweight Champion | **Retired from in-ring at Wrestle Kingdom 20, Jan 4, 2026** (Tokyo Dome); moved to an NJPW office/executive role | none (GAP) | `hiroshi-tanahashi` | HIGH | F4W; Forbes 2026-01-04; Slam Wrestling |
| **Tetsuya Naito** | Leader of Los Ingobernables de Japon (LIJ); multi-time IWGP/double champion | **Departed NJPW** (mutual non-renewal announced Apr 16, 2025, alongside BUSHI); underwent surgery | none (GAP) | `tetsuya-naito` | HIGH | Cageside Seats; F4W; Wrestling Inc. |
| **Jay White** | "Switchblade"; ex-Bullet Club leader; IWGP Heavyweight Champion | **In AEW** (returned at Forbidden Door, Jun 28, 2026) | none (GAP) | `jay-white` | HIGH | AEW results; Wrestling Inc. |
| **Will Ospreay** | Ex-IWGP World Heavyweight & United States Champion; NJPW-built junior-to-heavy star | **In AEW** (top-card; featured at Forbidden Door 2026) | none (GAP) | `will-ospreay` | HIGH | Yahoo Sports; AEW |
| **AJ Styles** | Second leader of the original Bullet Club; 2x IWGP Heavyweight Champion | Retired (WWE) Jan 31, 2026 — see dossier | **yes** `/wrestlers/aj-styles/` | (existing) | HIGH | see section 4 |
| **Finn Balor** (Prince Devitt) | **Founder / first leader of Bullet Club** (as "Prince Devitt") | Active WWE | **yes** `/wrestlers/finn-balor/` | (existing) | HIGH | Bullet Club history |
| **Shinsuke Nakamura** | Multi-time IWGP Heavyweight & Intercontinental Champion; "King of Strong Style" | Active WWE | **yes** `/wrestlers/shinsuke-nakamura/` | (existing) | HIGH | NJPW records |
| **Jon Moxley** | Former IWGP United States Champion (NJPW crossover run) | Active AEW | **yes** `/wrestlers/jon-moxley/` | (existing) | HIGH | NJPW/AEW records |
| **Kenny Omega** | Bullet Club leader after Styles; IWGP Heavyweight Champion; G1 winner | Active AEW (AEW World Champion, per titles-lineages.md) | none (GAP) | `kenny-omega` | HIGH | Bullet Club history; AEW |

### Bullet Club faction (feature block)

| Fact | Detail | Confidence | Source |
|---|---|---|---|
| Founded | 2013 in NJPW | HIGH | Wikipedia; Puroresu System |
| Founder / 1st leader | **Prince Devitt** (now Finn Balor) | HIGH | Bullet Club history |
| Leadership succession | Devitt then **AJ Styles** (2014), then **Kenny Omega** (turned on Styles Jan 2016), later Jay White, then **David Finlay** (recent leader) | HIGH | Wikipedia; Puroresu System; Monthly Puroresu |
| Legacy | Original faction whose "Too Sweet" spread across NJPW, WWE (Balor Club) and AEW (The Elite) | MED | widely reported |
| Cross-links available now | `/wrestlers/aj-styles/`, `/wrestlers/finn-balor/` | HIGH | site roster |

Correction note for build: some fan wikis call AJ Styles the "third" Bullet Club leader. Verified
succession is Devitt (founder) then Styles, making Styles the **second** leader. Use "second leader"
or, safest, "succeeded founder Prince Devitt as leader in 2014."

---

## 3. NJPW-to-Wrestle-Lore Cross-Link Map

For the poster wall / promotion card, these existing profiles carry NJPW ties and should link into
`/promotions/njpw/`:

- `/wrestlers/aj-styles/` — Bullet Club, 2x IWGP Heavyweight Champion
- `/wrestlers/finn-balor/` — Prince Devitt, Bullet Club founder
- `/wrestlers/shinsuke-nakamura/` — IWGP Heavyweight & IC Champion
- `/wrestlers/jon-moxley/` — IWGP United States Champion

---

## 4. AJ Styles Deep Dossier (flagship showcase)

Enhance `/wrestlers/aj-styles/`; optional retrospective at `/showcases/aj-styles/`. Frame as a
**three-promotion journey: TNA then NJPW/Bullet Club then WWE**, now a **confirmed career
retrospective** (he retired Jan 31, 2026).

### Identity

| Field | Value | Confidence | Source |
|---|---|---|---|
| Ring name | AJ Styles, "The Phenomenal One" | HIGH | multiple |
| Real name | Allen Neal Jones | HIGH | Wikipedia |
| Born | June 2, 1977, Jacksonville, North Carolina | HIGH | Wikipedia |
| Pro debut | 1998 | HIGH | wrestlingprofiles |
| In-ring retirement | Jan 31, 2026 (WWE Royal Rumble, lost retirement match to Gunther) | HIGH | CBS Sports; ESPN; WWE.com |
| Signatures | Styles Clash; Phenomenal Forearm; Calf Crusher | HIGH | multiple |

### TNA run (the foundation)

| Fact | Detail | Confidence | Source |
|---|---|---|---|
| Role | Original franchise player and "face" of TNA | HIGH | SI; TNA history |
| NWA World Heavyweight Championship | 3 reigns | MED | wrestlingprofiles |
| TNA World Heavyweight Championship | 2 reigns | MED | wrestlingprofiles |
| X Division Championship | 6 reigns; first-ever X Division Champion | HIGH | wrestlingprofiles |
| Milestone | First to complete both the TNA Triple Crown and Grand Slam | MED | wrestlingprofiles |

### NJPW / Bullet Club run (the transformation)

| Fact | Detail | Confidence | Source |
|---|---|---|---|
| Arrival | Revealed as new Bullet Club member at Invasion Attack, Apr 2014 | HIGH | Wikipedia |
| Leadership | Succeeded founder Prince Devitt (Finn Balor) as Bullet Club leader in 2014 | HIGH | Bullet Club history |
| IWGP Heavyweight title — 1st | Won May 3, 2014 (def. Kazuchika Okada); held ~163 days | HIGH | wrestlingprofiles; smarkoutmoment |
| IWGP Heavyweight title — 2nd | Won Feb 11, 2015 (def. Hiroshi Tanahashi); held ~144 days | HIGH | wrestlingprofiles |
| Impact | Headlined Wrestle Kingdom; his NJPW run "changed everything" for his career | HIGH | SI |

### WWE run (the peak)

| Fact | Detail | Confidence | Source |
|---|---|---|---|
| Debut | Jan 2016 Royal Rumble surprise entry | HIGH | Wikipedia; WWE |
| WWE Championship | 2 reigns — 1st won Sep 11, 2016 (def. Dean Ambrose, ~140 days); 2nd won Nov 7, 2017 (def. Jinder Mahal, ~371 days, one of the longest modern reigns) | HIGH | wrestlingprofiles; Wikipedia |
| United States Championship | Multiple reigns (2017, 2019) | MED | wrestlingprofiles |
| Intercontinental Championship | 1 reign (2020) | MED | wrestlingprofiles |
| Tag team gold | World Tag Team Championship (WWE) — count/dates conflict across sources (Wikipedia "twice"; wrestlingprofiles cites a reign with Dragon Lee, Oct 20, 2025) | VERIFY | Wikipedia vs wrestlingprofiles |
| Notable feuds | John Cena, Shinsuke Nakamura, Roman Reigns | HIGH | WWE |

### Retirement (confirmed — update the base research VERIFY flag)

The `00-content-data-research.md` flagged AJ Styles' retirement as `VERIFY` (single source). It is now
**CONFIRMED**: AJ Styles wrestled a **retirement match against Gunther at WWE Royal Rumble 2026 and
lost**, ending a 28-year career. Frame the flagship as a career retrospective; the "TNA to NJPW to
WWE, curtain call vs Gunther" arc is the showcase spine.

Cross-links inside the dossier: `/wrestlers/gunther/` (final opponent), `/wrestlers/finn-balor/`
(Bullet Club founder he succeeded), `/wrestlers/shinsuke-nakamura/` (WWE feud + NJPW peer),
`/wrestlers/roman-reigns/`, `/wrestlers/john-cena/`. GAP cross-links to build: `kazuchika-okada`
(first IWGP title win victim), `hiroshi-tanahashi` (second IWGP title win victim), `kenny-omega`
(Bullet Club successor).

---

## 5. Suggested new pages summary (route patterns)

| Page | Route | Priority |
|---|---|---|
| NJPW promotion overview | `/promotions/njpw/` | HIGH (required) |
| Kazuchika Okada profile | `/wrestlers/kazuchika-okada/` | HIGH |
| Hiroshi Tanahashi profile | `/wrestlers/hiroshi-tanahashi/` | HIGH |
| Will Ospreay profile | `/wrestlers/will-ospreay/` | HIGH |
| Kenny Omega profile | `/wrestlers/kenny-omega/` | HIGH |
| Jay White profile | `/wrestlers/jay-white/` | MED |
| Tetsuya Naito profile | `/wrestlers/tetsuya-naito/` | MED |
| Bullet Club faction page | `/rivalries/` or a factions hub (see factions-stables.md) | MED |
| IWGP Heavyweight title lineage | `/titles/iwgp-heavyweight-championship/` | MED |
| AJ Styles retrospective showcase | `/showcases/aj-styles/` (optional) | MED |

---

## 6. GAP LIST — NJPW names with NO page yet (build these)

Ranked by importance for an NJPW section that does not 404:

1. **Kazuchika Okada** (`kazuchika-okada`) — the biggest single gap; the defining NJPW star of the 2010s, now an AEW headliner. Must-build.
2. **Hiroshi Tanahashi** (`hiroshi-tanahashi`) — "The Ace"; just retired at Wrestle Kingdom 20 (Jan 2026), so a timely, high-traffic page.
3. **Will Ospreay** (`will-ospreay`) — NJPW-built, now an AEW top act; also fills an AEW gap.
4. **Kenny Omega** (`kenny-omega`) — Bullet Club leader, IWGP champ, AEW World Champion (also listed as a gap in base research and titles-lineages).
5. **Jay White** (`jay-white`) — ex-Bullet Club leader, IWGP champ, now AEW.
6. **Tetsuya Naito** (`tetsuya-naito`) — LIJ leader; departed NJPW in 2025.
7. **Yota Tsuji** (`yota-tsuji`) — current IWGP Heavyweight Champion; needed if the current-champion snapshot links out.

Already covered (no build needed): AJ Styles, Finn Balor, Shinsuke Nakamura, Jon Moxley.

---

## 7. Source list

- NJPW World: https://www.njpwworld.com/ — Roku/Google Play/App Store NJPW World app listings
- TrillerTV NJPW: https://www.trillertv.com/channel/new-japan-pro-wrestling/
- F4W "How can I watch NJPW in the US": https://www.f4wonline.com/event-guides/how-can-i-watch-njpw-us-full-guide-new-fans/
- NJPW (history/owner/founding): https://en.wikipedia.org/wiki/New_Japan_Pro-Wrestling
- IWGP Heavyweight reinstatement: https://www.fightful.com/wrestling/iwgp-heavyweight-championship-officially-reinstated/ ; https://411mania.com/wrestling/yota-tsuji-announces-official-reinstatement-iwgp-heavyweight-championship/ ; https://www.wrestlinginc.com/2069278/njpw-yota-tsuji-iwgp-heavyweight-championship-retires-prior-titles/
- Tanahashi retirement: https://www.f4wonline.com/news/new-japan/hiroshi-tanahashi-to-retire-reveals-date-of-final-match/ ; https://www.forbes.com/sites/alfredkonuwa/2026/01/04/njpw-wrestle-kingdom-20-jan-4-2026-results-and-winners-at-tanahashis-retirement/
- Naito departure: https://www.cagesideseats.com/2025/4/16/24409708/tetsuya-naito-exiting-new-japan-pro-wrestling-mutual-contract-bushi-lij ; https://www.f4wonline.com/news/new-japan/tetsuya-naito-njpw-mutally-agree-to-not-renew-contract/
- Okada in AEW: https://en.wikipedia.org/wiki/Kazuchika_Okada ; https://en.wikipedia.org/wiki/AEW_International_Championship
- Jay White / Ospreay AEW (Forbidden Door 2026): https://www.allelitewrestling.com/post/aew-x-njpw-forbidden-door-results-june-28-2026 ; https://sports.yahoo.com/wrestling/live/aew-forbidden-door-2026-live-results-updates-grades-analysis-for-tonights-ppv-063000582.html
- Bullet Club history / leaders: https://en.wikipedia.org/wiki/Bullet_Club ; https://puroresusystem.fandom.com/wiki/History_of_Bullet_Club
- AJ Styles: https://en.wikipedia.org/wiki/AJ_Styles ; https://wrestlingprofiles.com/wrestler/aj-styles/ ; https://www.si.com/fannation/wrestling/aj-styles-new-japan-wwe
- AJ Styles retirement (confirmed): https://www.cbssports.com/wwe/news/2026-wwe-royal-rumble-results-aj-styles-gunther-retirement-match/ ; https://www.espn.com/wwe/story/_/id/47791473/aj-styles-wwe-retirement-reaction-royal-rumble ; https://www.wwe.com/videos/aj-styles-bids-farewell-after-emotional-loss-to-gunther-royal-rumble-2026-highlights
