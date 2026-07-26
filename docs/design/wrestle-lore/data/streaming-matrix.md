# Wrestle Lore — Streaming Matrix (Where To Watch)

Where-to-watch analyst deliverable. Powers the brand "where to watch" badges and a dedicated
watch hub. Every row carries a source note and a confidence flag. Rule followed: no fabricated
facts, quotes, or stats; every platform claim is tied to a dated source; anything that could
shift is flagged.

- Date of research: 2026-07-26
- Confidence legend: `HIGH` = multiple authoritative sources agree; `MED` = single reputable source or subject to change; `VERIFY` = confirm before publishing.
- Scope: US as the primary market. International noted where it differs.

---

## Route pattern for new pages

- Watch hub landing: `/watch/`
- Per-promotion watch page: `/watch/{promotion}/` (e.g. `/watch/wwe/`, `/watch/aew/`, `/watch/njpw/`, `/watch/tna/`, `/watch/wcw/`, `/watch/ecw/`)
- Badge component (no standalone page): a small "where to watch" chip rendered on each `/promotions/{slug}/` hub and on each `/events/{slug}/` card. Data source = the matrix table below.
- Slug rule: reuse existing promotion slugs so badges and watch pages line up with `/promotions/wwe/`, `/promotions/wcw/`, `/promotions/ecw/`, `/promotions/tna/`, `/promotions/nxt/`, and the planned `/promotions/njpw/`.

---

## 1. Master streaming matrix (US, current)

| Brand / show | Weekly TV (US) | Live PLE / PPV (US) | Streaming / archive (US) | International note | Confidence | Source |
|---|---|---|---|---|---|---|
| **WWE Raw** | Netflix, Mondays 8/7c (exclusive since Jan 6 2025) | n/a | Netflix (episode replays) | Netflix in most non-US markets | HIGH | wwe.com/article/how-to-watch |
| **WWE SmackDown** | USA Network, Fridays 8/7c | n/a | Past episodes on Netflix | Netflix internationally | HIGH | wwe.com/article/how-to-watch |
| **WWE NXT** | The CW, Tuesdays 8/7c | n/a | The CW app; archives on Netflix | Netflix internationally | HIGH | wwe.com/article/how-to-watch |
| **WWE Premium Live Events** (WrestleMania, Royal Rumble, SummerSlam, Survivor Series, and monthly PLEs) | n/a | **ESPN app (ESPN DTC), the exclusive US home. First WWE PLE on ESPN was Wrestlepalooza, Sept 20 2025** | Same PLE plays live and on-demand inside the ESPN app; older PLE library on Netflix | Netflix carries PLEs in most non-US markets | HIGH | wwe.com PLE-on-ESPN announcement; ESPN.com upcoming-WWE-events |
| **AEW Dynamite** | TBS, Wednesdays 8-10 ET | n/a | HBO Max (simulcast plus replays) | AEW Plus on TrillerTV | HIGH | hbomax.com/aew |
| **AEW Collision** | TNT, Saturdays 8-10 ET | n/a | HBO Max | AEW Plus on TrillerTV | HIGH | hbomax.com/aew |
| **AEW PPVs** (Revolution, Double or Nothing, All In, All Out, Full Gear) | n/a | **HBO Max streams every AEW PPV live, starting with All Out on Sept 20 2025** | HBO Max on-demand after air | AEW Plus on TrillerTV internationally | HIGH | allelitewrestling.com HBO Max PPV announcement; Yahoo Sports AEW PPV guide |
| **NJPW (New Japan)** | No US linear TV | Big cards sold as PPV through NJPW World and TrillerTV | **NJPW World** (the promotion's own subscription, njpwworld.com) plus **NJPW on TrillerTV / TrillerTV+** | NJPW World is global; TV Asahi airs it in Japan | HIGH | f4wonline.com NJPW US guide; trillertv.com NJPW channel; njpwworld.com |
| **TNA Wrestling** (Thursday Night iMPACT) | **AMC, Thursdays 9-11 ET, debuted Jan 15 2026** (moved from AXS TV) | TNA PPVs via TNA+ and traditional PPV | **AMC+ (simulcast); TNA+ (tnaplus.com, the full library); older iMPACT seasons on Amazon Prime Video** | AMC carried on Prime Video and Apple TV channels in some regions | HIGH | amcnetworks.com press release; thesportster.com AMC how-to-watch; primevideo.com TNA iMPACT listings |
| **WCW (legacy, folded 2001)** | Defunct | n/a | **Not on any streaming service as of mid-2026.** WWE owns the library; a YouTube "Vault" style channel for WCW/ECW has been reported but is unconfirmed | Same gap internationally | MED / VERIFY | thesportster.com WWE Peacock-to-Netflix archive update (Fightful report) |
| **ECW (legacy, folded 2001)** | Defunct | n/a | **Not on any streaming service as of mid-2026.** Same status as WCW; reported YouTube Vault channel unconfirmed | Same gap internationally | MED / VERIFY | thesportster.com archive update |

---

## 2. Direct answer to the user: "Is TNA on Amazon?"

Yes, but only the back catalog, not the live show.

- **Live current TNA (2026):** Thursday Night iMPACT airs on **AMC** (Thursdays 9-11 ET, debuted Jan 15 2026) and simulcasts on **AMC+**. This moved from AXS TV. Confidence HIGH.
- **Full TNA library and PPVs:** the promotion's own subscription, **TNA+**. Confidence HIGH.
- **Amazon Prime Video:** carries **older iMPACT seasons as on-demand catalog** (Season 25 and Season 26 both list on Prime Video). This is library content, not the live AMC broadcast. Confidence HIGH.

Recommended badge copy for the TNA card:
> Thursday Night iMPACT on AMC and AMC+. Full library on TNA+. Older iMPACT seasons stream on Prime Video.

Do not claim the live weekly show streams on Amazon. It does not.

---

## 3. Surprising verified fact (correction to base research)

The base research doc (`00-content-data-research.md`, rows for WCW/ECW) guessed the legacy WCW and
ECW archives were "migrating to Netflix." That is not what happened. After the WWE library left
Peacock (Peacock era ended Jan 1 2026) and WWE PLEs moved to Netflix, the **WCW, ECW, WCCW, and
other territory archives went dark on every streaming service** and are not available anywhere as of
mid-2026. A YouTube "Vault" channel carrying WCW and ECW has been reported by Fightful but is
unconfirmed by WWE, Netflix, or Peacock.

Build implication: the WCW and ECW "where to watch" badges must say the archive is currently
offline, not point fans to Netflix. This protects the portfolio from shipping a wrong fact.

---

## 4. Ready-to-drop badge copy (anti-AI standard, no banned words)

Each string is short enough for a card chip and names specific platforms.

- **WWE Raw:** `Raw streams on Netflix, Mondays 8/7c.`
- **WWE SmackDown:** `SmackDown airs on USA Network, Fridays 8/7c.`
- **WWE NXT:** `NXT airs on The CW, Tuesdays 8/7c.`
- **WWE PLEs:** `Premium Live Events stream on the ESPN app in the US. Netflix carries them internationally.`
- **AEW:** `Dynamite on TBS, Collision on TNT, both on HBO Max. Every AEW PPV streams live on HBO Max.`
- **NJPW:** `Watch on NJPW World, the promotion's own subscription, plus NJPW on TrillerTV.`
- **TNA:** `Thursday Night iMPACT on AMC and AMC+. Full library on TNA+. Older seasons on Prime Video.`
- **WCW:** `The WCW library is off streaming for now. WWE owns the tapes; no service carries them as of 2026.`
- **ECW:** `The ECW library is off streaming for now. Same status as the WCW archive.`

Banned-word check: no "seamless", "elevate", "unlock", "game-changer", "dive", "ultimate destination".
No decorative arrows, no em-dash separators. Every line names a real platform.

---

## 5. Pricing reference (for an optional detail row, not the badge)

| Service | US price (mid-2026) | Confidence | Source |
|---|---|---|---|
| ESPN app (ESPN DTC, unlimited tier) | $29.99 / month | MED / VERIFY exact tier | WWE/ESPN deal coverage (si.com, heavy.com, kgw.com) |
| AMC+ | $6.99 / month ad-supported; $9.99 / month premium | HIGH | thesportster.com AMC how-to-watch |
| Netflix | standard consumer tiers (not wrestling-specific) | HIGH | general |
| HBO Max | standard consumer tiers | HIGH | general |
| NJPW World | subscription via njpwworld.com | MED / VERIFY current USD price | njpwworld.com help/subscription |
| TNA+ | subscription via tnaplus.com | MED / VERIFY current USD price | TNA deal coverage |

Note: prices move. Keep pricing off the badge and in a footnote or a `/watch/{promotion}/` detail
block so a price change never breaks a card. Flag both subscription prices `VERIFY` before printing.

---

## 6. Cross-links to existing pages

The watch pages and badges should link to roster and promotion pages that already exist.

- **WWE badge / `/watch/wwe/`** to `/promotions/wwe/`, plus current stars: `/wrestlers/cody-rhodes/`, `/wrestlers/roman-reigns/`, `/wrestlers/gunther/`, `/wrestlers/rhea-ripley/`, `/wrestlers/cm-punk/`.
- **AEW badge / `/watch/aew/`**: no `/promotions/aew/` page yet (gap). Cross-link roster with AEW ties: `/wrestlers/jon-moxley/`, `/wrestlers/chris-jericho/`, `/wrestlers/mercedes-mone/`.
- **NJPW badge / `/watch/njpw/`**: `/promotions/njpw/` is a planned gap. Cross-link `/wrestlers/aj-styles/`, `/wrestlers/shinsuke-nakamura/`, `/wrestlers/jon-moxley/`, `/wrestlers/finn-balor/`.
- **TNA badge / `/watch/tna/`**: `/promotions/tna/`, plus `/wrestlers/aj-styles/`, `/wrestlers/samoa-joe/`, `/wrestlers/christopher-daniels/`, `/wrestlers/bully-ray/`.
- **WCW badge / `/watch/wcw/`**: `/promotions/wcw/`, plus `/wrestlers/sting/`, `/wrestlers/ric-flair/`, `/wrestlers/hulk-hogan/`, `/wrestlers/goldberg/`, `/wrestlers/diamond-dallas-page/`.
- **ECW badge / `/watch/ecw/`**: `/promotions/ecw/`, plus `/wrestlers/rob-van-dam/` (gap, no page), `/wrestlers/bully-ray/`, `/wrestlers/rey-mysterio/`, `/wrestlers/chris-jericho/`.

---

## 7. Gap list (entities without a page that this dataset touches)

Build or stub these so watch-page clickables do not 404:

1. **`/watch/` hub landing page** — required, does not exist.
2. **Per-promotion watch pages** `/watch/wwe/`, `/watch/aew/`, `/watch/njpw/`, `/watch/tna/`, `/watch/wcw/`, `/watch/ecw/` — all new.
3. **`/promotions/aew/`** — AEW has no promotion page yet, so the AEW badge and watch page have no hub to link to. Biggest structural gap for the streaming matrix.
4. **`/promotions/njpw/`** — planned in base research, still a gap; the NJPW watch page and badge need it.
5. **`/watch/` badge component** — the reusable chip that reads this matrix and renders on `/promotions/` and `/events/` cards. No component exists.
6. **Rob Van Dam wrestler page** — referenced as an ECW cross-link, no page (`/wrestlers/rob-van-dam/`).

---

## 8. Source notes

| Claim | Source | Confidence |
|---|---|---|
| WWE Raw on Netflix, SmackDown on USA, NXT on The CW | wwe.com/article/how-to-watch | HIGH |
| WWE PLEs exclusive to ESPN app in US; first PLE on ESPN was Wrestlepalooza Sept 20 2025 | wwe.com PLE-on-ESPN announcement; espn.com upcoming-WWE-events | HIGH |
| ESPN DTC unlimited tier around $29.99/month | si.com, heavy.com, kgw.com WWE/ESPN deal coverage | MED (verify exact tier) |
| AEW Dynamite on TBS, Collision on TNT, both simulcast on HBO Max | hbomax.com/aew | HIGH |
| HBO Max streams every AEW PPV live, from All Out Sept 20 2025 | allelitewrestling.com HBO Max PPV announcement; Yahoo Sports | HIGH |
| NJPW via NJPW World and TrillerTV in the US | f4wonline.com NJPW US guide; trillertv.com; njpwworld.com | HIGH |
| TNA iMPACT on AMC Thursdays 9-11 ET from Jan 15 2026, simulcast AMC+, moved from AXS TV | amcnetworks.com press release; thesportster.com; hollywoodreporter.com | HIGH |
| Older TNA iMPACT seasons on Amazon Prime Video (S25, S26) | primevideo.com TNA iMPACT listings | HIGH |
| WCW/ECW archives not on any streaming service as of mid-2026; YouTube Vault reported, unconfirmed | thesportster.com WWE Peacock-to-Netflix archive update (Fightful) | MED / VERIFY |

### Full URLs
- WWE how to watch: https://www.wwe.com/article/how-to-watch
- WWE PLEs debut on ESPN (Wrestlepalooza Sept 20): https://www.wwe.com/article/wwe-premium-live-events-to-debut-on-espn-platforms-in-the-u-s-beginning-sept-20-with-first
- ESPN upcoming WWE events: https://www.espn.com/wwe/story/_/id/46294371/upcoming-wwe-events-espn-dates-s-how-watch
- HBO Max AEW: https://www.hbomax.com/aew
- HBO Max AEW PPV announcement: https://www.allelitewrestling.com/post/hbo-max-to-stream-live-all-elite-wrestling-pay-per-view-events
- F4W NJPW US guide: https://www.f4wonline.com/event-guides/how-can-i-watch-njpw-us-full-guide-new-fans/
- TrillerTV NJPW channel: https://www.trillertv.com/channel/new-japan-pro-wrestling/
- AMC/TNA press release: https://www.amcnetworks.com/press-releases/amc-networks-tna-wrestling-announce-agreement-to-bring-tnas-flagship-weekly-tv-show-to-amc-thursday-night-impact/
- TNA AMC how to watch: https://www.thesportster.com/tna-amc-debut-how-to-watch/
- TNA iMPACT on Prime Video: https://www.primevideo.com/detail/0JUDFWRZQVXA7XUGHXAN08F1NQ
- WCW/ECW archive status: https://www.thesportster.com/wwe-peacock-netflix-archive-update/
