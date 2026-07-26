# Wrestle Lore — WWE Hall of Fame Dataset (page-ready)

Researcher deliverable for the `/hall-of-fame/` build. Every row carries a source note and a
confidence flag. Rule followed: no invented facts, quotes, or stats. Anything unconfirmed is marked
`VERIFY`.

- Date of research: 2026-07-26
- Confidence legend: `HIGH` = multiple authoritative sources agree; `MED` = single reputable source or detail subject to change; `VERIFY` = confirm before publishing.
- Anti-AI copy standard applied: no decorative arrows, no em-dash separators, specific nouns, no cliche banned words.

## TIMING CORRECTION (important for the build)

The base research doc (`00-content-data-research.md`, section 2) lists the last 5 classes as
**2021-2025**. That was correct when written. As of the current date (2026-07-26) the **Class of 2026
was already inducted on April 17, 2026** at Dolby Live at Park MGM, Las Vegas. So the true "last 5
induction classes" are now **2022, 2023, 2024, 2025, 2026**. This dataset uses the corrected window.
Confidence HIGH (WWE.com, ESPN, F4W, Wikipedia all confirm the 2026 ceremony).

---

## 1. Last 5 induction classes (2022-2026)

| Class | Ceremony date + venue | Headline inductee(s) | Notable co-inductees | Special-category | Confidence | Source |
|---|---|---|---|---|---|---|
| **2026** | Apr 17 2026, Dolby Live at Park MGM, Las Vegas | Stephanie McMahon, AJ Styles | Demolition (Ax and Smash) | Celebrity: Dennis Rodman. Legacy (posthumous): Sycho Sid, Bad News Brown. Immortal Moment: Hogan vs Andre, WrestleMania III | HIGH | WWE.com 2026 recap; F4W full list; Wikipedia WWE HOF (2026) |
| **2025** | WrestleMania 41 weekend, Las Vegas | Triple H | Lex Luger, Michelle McCool, The Natural Disasters (Earthquake and Typhoon) | n/a | HIGH | WWE.com 2025 recap; Wrestling Inc.; SI |
| **2024** | WrestleMania 40 weekend, Philadelphia | Paul Heyman | Bull Nakano, The U.S. Express (Barry Windham and Mike Rotunda), Thunderbolt Patterson, Lia Maivia | Celebrity: Muhammad Ali (posthumous) | HIGH | WWE.com class of 2024; Bleacher Report; SI |
| **2023** | WrestleMania 39 weekend, Los Angeles | Rey Mysterio | The Great Muta, Stacy Keibler | Celebrity: Andy Kaufman (posthumous) | HIGH | WWE.com class of 2023; Yahoo; F4W |
| **2022** | WrestleMania 38 weekend, Dallas | The Undertaker | Vader, The Steiner Brothers (Rick and Scott), Queen Sharmell | Warrior Award: Shad Gaspard (posthumous) | HIGH | WWE.com class of 2022; Bleacher Report; F4W |

Slug suggestion for each class page: `/hall-of-fame/{year}/` (e.g. `/hall-of-fame/2026/`).

---

## 2. Per-class inductees with cross-links to existing /wrestlers/ slugs

Legend: ✓ = page exists at `/wrestlers/{slug}/`; GAP = no page yet.

### Class of 2026
| Inductee | Category | Existing slug | Confidence |
|---|---|---|---|
| AJ Styles | Individual | `/wrestlers/aj-styles/` ✓ | HIGH |
| Sycho Sid (Sid Eudy) | Legacy (posthumous) | `/wrestlers/sycho-sid/` ✓ | HIGH |
| Hulk Hogan (via Immortal Moment) | Immortal Moment | `/wrestlers/hulk-hogan/` ✓ | HIGH |
| Andre the Giant (via Immortal Moment) | Immortal Moment | `/wrestlers/andre-the-giant/` ✓ | HIGH |
| Stephanie McMahon | Individual (authority) | GAP | HIGH |
| Dennis Rodman | Celebrity | GAP | HIGH |
| Demolition (Ax and Smash) | Tag team | GAP | HIGH |
| Bad News Brown (Allen Coage) | Legacy (posthumous) | GAP | HIGH |

### Class of 2025
| Inductee | Category | Existing slug | Confidence |
|---|---|---|---|
| Triple H | Individual | `/wrestlers/triple-h/` ✓ | HIGH |
| Lex Luger | Individual | `/wrestlers/lex-luger/` ✓ | HIGH |
| Michelle McCool | Individual | GAP | HIGH |
| The Natural Disasters (Earthquake and Typhoon) | Tag team | GAP | MED (member names re-verify) |

### Class of 2024
| Inductee | Category | Existing slug | Confidence |
|---|---|---|---|
| Paul Heyman | Individual | GAP | HIGH |
| Bull Nakano | Individual | GAP | HIGH |
| The U.S. Express (Barry Windham and Mike Rotunda) | Tag team | GAP | HIGH |
| Thunderbolt Patterson | Individual | GAP | MED |
| Lia Maivia | Individual (Legacy) | GAP | MED |
| Muhammad Ali | Celebrity (posthumous) | GAP | HIGH |

### Class of 2023
| Inductee | Category | Existing slug | Confidence |
|---|---|---|---|
| Rey Mysterio | Individual | `/wrestlers/rey-mysterio/` ✓ | HIGH |
| The Great Muta | Individual | GAP | HIGH |
| Stacy Keibler | Individual | GAP | HIGH |
| Andy Kaufman | Celebrity (posthumous) | GAP | HIGH |

### Class of 2022
| Inductee | Category | Existing slug | Confidence |
|---|---|---|---|
| The Undertaker | Individual | `/wrestlers/the-undertaker/` ✓ | HIGH |
| Vader | Individual | `/wrestlers/vader/` ✓ | HIGH |
| The Steiner Brothers (Rick and Scott) | Tag team | GAP | HIGH |
| Queen Sharmell | Individual | GAP | HIGH |
| Shad Gaspard | Warrior Award (posthumous) | GAP | HIGH |

---

## 3. Most-decorated inductee (multi-time inductions)

Question asked: confirm Ric Flair as two-time, note any others.

### Ric Flair — confirmed two-time
- **First induction 2008** (individual). **Second induction 2012 as a member of the Four Horsemen.** Page exists: `/wrestlers/ric-flair/`. Confidence HIGH (prowrestling.fandom, WWE profile, contemporaneous 2012 coverage).
- Historical note worth featuring: Ric Flair was the **first person to be inducted twice** and was billed as "the only two-time WWE Hall of Famer" for years, until the group inductions of 2019-2020 created a wave of second inductions. Confidence HIGH.

### The "two-time (or more) club" — full picture
| Person | Inductions | Existing slug | Confidence |
|---|---|---|---|
| **Hulk Hogan** | 2005 individual; 2020 (nWo); 2026 (Immortal Moment, Hogan vs Andre WM III) | `/wrestlers/hulk-hogan/` ✓ | HIGH that all three happened; MED whether the Immortal Moment counts as a personal "induction" |
| **Ric Flair** | 2008 individual; 2012 (Four Horsemen) | `/wrestlers/ric-flair/` ✓ | HIGH |
| **Shawn Michaels** | 2011 individual; 2019 (D-Generation X) | `/wrestlers/shawn-michaels/` ✓ | HIGH |
| **Triple H** | 2019 (D-Generation X); 2025 individual | `/wrestlers/triple-h/` ✓ | HIGH |
| **Booker T** | 2013 individual; 2019 (Harlem Heat) | `/wrestlers/booker-t/` ✓ | HIGH |
| **Scott Hall** | 2014 individual (as Razor Ramon); 2020 (nWo) | `/wrestlers/razor-ramon/` ✓ | HIGH |
| **Kevin Nash** | 2015 individual; 2020 (nWo) | `/wrestlers/kevin-nash/` ✓ (also `/wrestlers/diesel/`) | HIGH |
| **Andre the Giant** | 1993 (inaugural individual); 2026 (Immortal Moment) | `/wrestlers/andre-the-giant/` ✓ | HIGH the two happened; MED whether Immortal Moment counts |
| **Barry Windham** | 2012 (Four Horsemen); 2024 (U.S. Express) | GAP | MED |
| **X-Pac / Sean Waltman** | 2019 (D-Generation X); 2020 (nWo) | GAP | MED |

### Verdict for the hero panel
- **Ric Flair is the cleanest, safest "most-decorated" hero** for a two-time individual-plus-faction story, and the "first ever two-timer" line is a strong, verifiable hook. Recommend Flair as the hero panel.
- **Caveat to flag for design:** if you count the 2026 Immortal Moment as a personal induction, **Hulk Hogan reaches three** (2005, 2020, 2026), which technically makes Hogan the most-decorated by raw count. Because the "Immortal Moment" is a moment/match honor rather than a standard individual induction, treat this as a footnote, not the headline. Do NOT print "Flair is the only two-time inductee" (that stopped being true in 2019). Confidence on the count: HIGH; confidence on how to classify Immortal Moment: MED / editorial call.

---

## 4. Route pattern for the new pages

- **Index / hub:** `/hall-of-fame/` — landing page (hero, most-decorated panel, two-time club strip, last-5-classes row, link to full class archive).
- **Per-class pages:** `/hall-of-fame/{year}/` — one page per class, e.g. `/hall-of-fame/2026/`, `/hall-of-fame/2025/`, `/hall-of-fame/2024/`, `/hall-of-fame/2023/`, `/hall-of-fame/2022/`.
- Inductees who are wrestlers link out to their existing `/wrestlers/{slug}/` page; do not create duplicate profile pages under `/hall-of-fame/`.

---

## 5. Proposed /hall-of-fame/ index page structure

1. **Page header.** H1 "WWE Hall of Fame". One-sentence intro naming what the ceremony is (annual induction held on WrestleMania weekend since 1993, plus the 2026 move to Las Vegas). No banned words.
2. **Most-decorated hero panel.** Ric Flair, gold accent. Two-time badge, the two induction years (2008, 2012), the "first two-time inductee" line, link to `/wrestlers/ric-flair/`. Footnote tile: Hogan three-honor note.
3. **Two-Time Club strip.** Horizontal card row: Flair, Shawn Michaels, Triple H, Booker T, Scott Hall, Kevin Nash, Hulk Hogan. Each card links to its existing wrestler slug. Cards for GAP people (Barry Windham, X-Pac) shown as text-only until pages exist.
4. **Last 5 Classes row (2022-2026).** One tile per class, headline inductee as the face, year label, link to `/hall-of-fame/{year}/`. Tiles for headliners with pages link to the wrestler slug too (AJ Styles, Triple H, Rey Mysterio, Undertaker).
5. **Special categories explainer.** Short block defining Celebrity wing, Legacy wing, Warrior Award, Immortal Moment, with the most recent example of each (Dennis Rodman; Sycho Sid and Bad News Brown; Shad Gaspard; Hogan vs Andre WM III).
6. **Full class archive link.** Link out to per-year pages / future full 1993-2026 index.
7. **JSON-LD.** `ItemList` of classes; each class `Event` with inductee `Person` entries.

## 6. Per-class page mini structure (`/hall-of-fame/{year}/`)

1. **Class header.** H1 "WWE Hall of Fame Class of {year}", ceremony date and venue line.
2. **Headliner block.** Photo/name of the headline inductee, one-paragraph "why they were inducted" (facts only), link to wrestler slug if it exists.
3. **Inductee table.** Every inductee: name, category (Individual / Tag team / Celebrity / Legacy / Warrior Award / Immortal Moment), a one-line fact, cross-link to `/wrestlers/{slug}/` where a page exists.
4. **Prev / next class nav.** Link to `/hall-of-fame/{year-1}/` and `/hall-of-fame/{year+1}/`.
5. **JSON-LD.** `Event` with `subEvent` or `performer` list of inductee `Person` entries.

---

## 7. GAP LIST — inductees WITHOUT a page yet (build/stub so links do not 404)

Priority (headliners and prominent inductees first):
- **Stephanie McMahon** (2026 headliner) — highest-priority gap; on-screen authority, not currently in roster.
- **Paul Heyman** (2024 headliner) — high priority.
- **Dennis Rodman** (2026 celebrity) — high-profile crossover name.
- **Demolition (Ax and Smash)** (2026 tag team).
- **The Great Muta** (2023) — also a NJPW crossover tie-in for the planned `/promotions/njpw/` build.
- **Stacy Keibler** (2023).
- **Michelle McCool** (2025).
- **The Natural Disasters (Earthquake and Typhoon)** (2025 tag team).
- **The Steiner Brothers (Rick and Scott)** (2022 tag team).
- **Queen Sharmell** (2022).
- **Bull Nakano** (2024).
- **The U.S. Express (Barry Windham and Mike Rotunda)** (2024) — Barry Windham is also a two-time inductee (Four Horsemen 2012).
- **Bad News Brown (Allen Coage)** (2026 Legacy).
- **Shad Gaspard** (2022 Warrior Award).
- **Thunderbolt Patterson, Lia Maivia** (2024 Legacy).
- Celebrity/posthumous, lower build priority: **Muhammad Ali** (2024), **Andy Kaufman** (2023).
- Two-time-club GAP names: **X-Pac / Sean Waltman**.

Inductees that CAN link to existing pages right now (no gap): AJ Styles, Sycho Sid, Hulk Hogan, Andre the Giant, Triple H, Lex Luger, Rey Mysterio, The Undertaker, Vader, Ric Flair, Shawn Michaels, Booker T, Scott Hall (`/wrestlers/razor-ramon/`), Kevin Nash.

---

## 8. Source notes

- WWE.com Class of 2022: https://www.wwe.com/shows/wwe-hall-of-fame/class-of-2022
- WWE.com Class of 2023: https://www.wwe.com/shows/wwe-hall-of-fame/class-of-2023
- WWE.com Class of 2024: https://www.wwe.com/shows/wwe-hall-of-fame/class-of-2024
- WWE.com Class of 2025 recap: https://www.wwe.com/shows/wwe-hall-of-fame/2025/article/recap
- WWE.com Class of 2026: https://www.wwe.com/wwe-hall-of-fame-2026-04-17
- ESPN 2026 class: https://www.espn.com/wwe/story/_/id/48476972/meet-2026-wwe-hall-fame-class-aj-styles-stephanie-mcmahon-demolition-more
- F4W 2026 full list: https://www.f4wonline.com/event-guides/wwe-hall-of-fame-2026-inductees-full-list/
- Wikipedia WWE Hall of Fame (2026): https://en.wikipedia.org/wiki/WWE_Hall_of_Fame_(2026)
- Ric Flair two-time: https://prowrestling.fandom.com/wiki/Ric_Flair ; https://headlineplanet.com/home/2012/03/27/tna-hypes-ric-flairs-wwe-hall-of-fame-induction-addresses-controversy/
- Bleacher Report 2022 (Sharmell + full class): https://bleacherreport.com/articles/10029720
- Bleacher Report 2024 (US Express): https://bleacherreport.com/articles/10112184-the-us-express-named-to-2024-wwe-hall-of-fame-class-joins-paul-heyman-bull-nakano
