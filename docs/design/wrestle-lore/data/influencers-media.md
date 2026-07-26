# Wrestle Lore — Influencers & Media Roster (page-ready dataset)

Researcher deliverable for the new "Media & Creators" tab. Covers real wrestling
interviewers, podcasters, YouTubers, and journalists. Every row carries a source note and a
confidence flag. Rule followed: no invented facts, quotes, or stats; anything unconfirmed is
flagged `VERIFY`. Builds on section 6 of `00-content-data-research.md` and goes deeper.

- Date of research: 2026-07-26
- Confidence legend: `HIGH` = multiple/authoritative sources agree; `MED` = single reputable source or subject to change; `VERIFY` = confirm before publishing.

---

## Route pattern

- New pages live at **`/media/{slug}/`** (recommended over `/influencers/{slug}/` — "media" reads
  cleaner and covers journalists, not just influencers).
- Tab label: **"Media & Creators"**.
- Index/hub page at `/media/` listing the roster grouped by format (Long-form interview, News &
  insider, Podcast/radio, Video/YouTube).
- None of these pages exist yet. Every personality below is a GAP (see Gap List).

## Separation rule: MEDIA vs ACTIVE WRESTLER

This tab is for people whose primary job is covering wrestling, not performing it. Three cases to
keep straight for the build team:

1. **Pure media** (interviewers, journalists, hosts) — belong here, do not appear on the athlete grid.
2. **Active wrestlers** the user or fans might mention as "media" (e.g. **Sami Zayn**) stay on the
   **athlete grid at `/wrestlers/{slug}/`**, not here.
3. **Wrestler/booker-turned-media** (e.g. **Bully Ray**, **Jim Cornette**) have a dual identity.
   Give them a `/media/` page for their broadcast work and cross-link to any existing
   `/wrestlers/` page. Tag them `dual-role` so they are not double-counted as pure media.

---

## Table A — Pure media personalities (primary roster)

| Name | Slug suggestion | Who they are (one line) | Platform / show | Feature? | Confidence | Source |
|---|---|---|---|---|---|---|
| **Chris Van Vliet** | `chris-van-vliet` | Emmy-winning host who runs the top long-form wrestler-interview show in the space | "Insight with Chris Van Vliet" (podcast + two YouTube channels, ~2M subs); joined Cumulus Podcast Network Nov 6, 2025 | **YES — hero** | HIGH | Barchart/Cumulus release 2025-11-06; en.wikipedia.org/wiki/Chris_Van_Vliet |
| **Ariel Helwani** | `ariel-helwani` | Combat-sports journalist who interviews wrestling's biggest names alongside his MMA work | "The MMA Hour" and "The Ariel Helwani Show" (Yahoo Sports) | YES | HIGH | podcasts.apple.com/us/podcast/the-ariel-helwani-show; sports.yahoo.com/videos/shows/ariel-helwani-show |
| **Sean Ross Sapp** | `sean-ross-sapp` | Part-owner and lead reporter at Fightful; a primary backstage-news breaker | Fightful (fightful.com), Fightful Select | YES | HIGH | fightful.com/personalities/sean-ross-sapp; linkedin.com/in/sean-ross-sapp |
| **Dave Meltzer** | `dave-meltzer` | Veteran journalist behind the Wrestling Observer Newsletter; his star-rating scale is the industry standard | Wrestling Observer Newsletter (f4wonline.com), Wrestling Observer Radio | YES | HIGH | en.wikipedia.org/wiki/List_of_professional_wrestling_matches_rated_5_or_more_stars_by_Dave_Meltzer; f4wonline.com |
| **Renee Paquette** | `renee-paquette` | Broadcaster and interviewer; former WWE backstage host, now an AEW on-air personality | "The Sessions with Renee Paquette" (reportedly on hiatus); AEW broadcasts | YES | MED (podcast status VERIFY) | wrestlinginc.com/1277319 (hiatus); podcasts.apple.com/us/podcast/the-sessions-with-rene-paquette |
| **Denise Salcedo** | `denise-salcedo` | Independent wrestling interviewer and YouTuber known for candid sit-downs | "Instinct Culture" (YouTube + podcast) | YES | HIGH | youtube.com/denisesalcedo; podscan.fm/podcasts/instinct-culture-by-denise-salcedo |
| **Conrad Thompson** | `conrad-thompson` | Podcast producer-host who turned wrestler retrospectives into a network; runs the Starrcast convention | "Something to Wrestle with Bruce Prichard", "83 Weeks with Eric Bischoff", "Grilling JR"; Starrcast | YES | HIGH | en.wikipedia.org/wiki/Conrad_Thompson; espn.com/wwe/story/_/id/24514346 |
| **Peter Rosenberg** | `peter-rosenberg` | Hot 97 radio host and longtime WWE media contributor | "Cheap Heat with Peter Rosenberg" (podcast) | YES | HIGH | shows.acast.com/cheap-heat-with-peter-rosenberg |
| **Dave LaGreca** | `dave-lagreca` | Daily wrestling talk-radio host; anchors the genre's flagship call-in show | "Busted Open" (SiriusXM) | YES | HIGH | podcasts.apple.com/us/podcast/busted-open; cagesideseats.com/wwe/462282 |
| **Wade Keller** | `wade-keller` | Founder and editor of PWTorch; one of the longest-running wrestling journalists | Pro Wrestling Torch (pwtorch.com), "Wade Keller Pro Wrestling Podcast" | MED (feature optional) | MED | pwtorch.com (widely reported) — VERIFY current title |
| **Sam Roberts** | `sam-roberts` | Radio personality and wrestling host; interviews and panel work | "Notsam Wrestling" (podcast) | MED (feature optional) | MED | podcasts.apple.com (widely reported) — VERIFY current platform |

## Table B — Dual-role: wrestler/booker-turned-media (cross-link, do not double-count)

| Name | Media slug | Wrestling page (existing?) | Media role | Confidence | Source |
|---|---|---|---|---|---|
| **Bully Ray** (Mark LoMonaco) | `bully-ray` (media) | `/wrestlers/bully-ray/` ✓ exists | Co-host of "Busted Open" (SiriusXM) with Dave LaGreca | HIGH | listennotes.com/podcasts/busted-open; cagesideseats.com/wwe/462282 |
| **Jim Cornette** | `jim-cornette` | none (no wrestler page) | Former manager/booker; hosts "Jim Cornette's Drive-Thru" and "The Jim Cornette Experience" | HIGH | podbean.com/.../Jim-Cornette's-Drive-Thru; podtail.com/en/podcast/jim-cornette-s-drive-thru |

## Table C — Outlets / channels (brand tiles, not individual people)

| Outlet | Slug suggestion | What it is | Feature? | Confidence | Source |
|---|---|---|---|---|---|
| **Fightful** | `fightful` | News site + Fightful Select insider tier (Sean Ross Sapp) | YES | HIGH | fightful.com/about |
| **WrestleTalk** | `wrestletalk` | UK-based YouTube news/opinion channel | MED | MED | wrestletalk.com/videos; wwe-youtubers.fandom.com/wiki/WrestleTalk |
| **PWTorch (Pro Wrestling Torch)** | `pwtorch` | Wade Keller's news/analysis outlet + podcast network | MED | MED | pwtorch.com |
| **Wrestling Observer** | `wrestling-observer` | Meltzer's newsletter + radio (f4wonline.com) | YES | HIGH | f4wonline.com |

Note on WrestleTalk: former on-air figure **Adam Blampied** has a public 2017 controversy
(he apologized for "manipulating" women — BBC). Feature the **channel/brand**, not Blampied
personally, and do not build a personality page for him. Source: bbc.co.uk news-entertainment-arts-41764308.

---

## Cross-links to existing `/wrestlers/` slugs

Use these on each media page's "notable interviews / connections" strip. All targets confirmed to
exist in the current roster of 89 profiles.

- **Chris Van Vliet** interview subjects with pages: `/wrestlers/the-rock/`, `/wrestlers/john-cena/`,
  `/wrestlers/batista/` (Dave Bautista), `/wrestlers/chris-jericho/`, `/wrestlers/becky-lynch/`,
  `/wrestlers/cody-rhodes/`. Source: Cumulus release guest list.
- **Renee Paquette** — married to `/wrestlers/jon-moxley/`; AEW connection. (Relationship widely
  reported; confidence HIGH.)
- **Conrad Thompson** shows built around `/wrestlers/ric-flair/` (Grilling JR / Flair content),
  `/wrestlers/hulk-hogan/` era, `/wrestlers/eric-bischoff/`... note Bischoff has **no** wrestler page
  (HOF gap) — cross-link only once built.
- **Bully Ray** — self cross-link `/wrestlers/bully-ray/`.
- **Dave Meltzer** — pairs naturally with the existing matches/star-ratings pages under `/matches/`
  (his scale is already the review network's rating basis).

---

## Gap List — media entities with NO page yet (all new)

Every row above is a gap. Build priority order:

1. **`/media/` hub page** — required so the new tab has a landing route.
2. **Chris Van Vliet** `/media/chris-van-vliet/` — the hero; build first (HIGH, most decorated).
3. **Ariel Helwani, Sean Ross Sapp, Dave Meltzer, Conrad Thompson** — highest-authority tier.
4. **Denise Salcedo, Peter Rosenberg, Dave LaGreca, Renee Paquette** — strong second tier.
5. **Bully Ray (media page)** + link to existing `/wrestlers/bully-ray/`; **Jim Cornette** `/media/jim-cornette/`.
6. **Wade Keller, Sam Roberts** — optional third tier (VERIFY current roles first).
7. **Outlet tiles**: Fightful, Wrestling Observer, PWTorch, WrestleTalk.

Adjacent gaps this dataset surfaces (not media, but referenced): **Eric Bischoff** and **Bruce
Prichard** have no `/wrestlers/` pages yet — needed before Conrad Thompson's show cross-links resolve.

---

## Surprising verified fact

**WWE launched an official 24/7 "WWE Radio" channel on SiriusXM on July 23, 2026**, folding live
Premium Live Event coverage and existing wrestling podcasts (including Busted Open) onto the platform
— reshaping where wrestling media distributes audio. This is three days before this research date and
directly affects the Dave LaGreca / Bully Ray "Busted Open" entries.
Source: corporate.wwe.com/about/news/2026/07-23-2026; siriusxm.com/blog/wwe-radio; wrestlinginc.com/2221847. Confidence HIGH.

---

## Anti-AI copy note for the build phase

One-liners above use specific nouns (show names, networks, roles), no decorative arrows, no
em-dash separators, no banned cliche words. Keep that standard in the page bios. Do not state
Renee Paquette's podcast is "active" — it is reportedly on hiatus (flag or omit). Do not attribute
quotes to any personality without a linked source.

## Consolidated source list

- Chris Van Vliet / Cumulus: https://www.barchart.com/story/news/35963222/chris-van-vliet-joins-cumulus-podcast-network
- Chris Van Vliet (bio): https://en.wikipedia.org/wiki/Chris_Van_Vliet
- Ariel Helwani Show: https://podcasts.apple.com/us/podcast/the-ariel-helwani-show/id1724284031
- Sean Ross Sapp / Fightful: https://www.fightful.com/personalities/sean-ross-sapp/
- Dave Meltzer star ratings: https://en.wikipedia.org/wiki/List_of_professional_wrestling_matches_rated_5_or_more_stars_by_Dave_Meltzer
- Renee Paquette / The Sessions hiatus: https://www.wrestlinginc.com/1277319/aew-personality-renee-paquettes-podcast-the-sessions-reportedly-on-hiatus/
- Denise Salcedo / Instinct Culture: https://www.youtube.com/denisesalcedo
- Conrad Thompson / Starrcast: https://www.espn.com/wwe/story/_/id/24514346 ; https://en.wikipedia.org/wiki/Conrad_Thompson
- Peter Rosenberg / Cheap Heat: https://shows.acast.com/cheap-heat-with-peter-rosenberg
- Busted Open (LaGreca / Bully Ray): https://www.listennotes.com/podcasts/busted-open-siriusxm-Dc1mQdqbgBW/
- Jim Cornette's Drive-Thru: https://www.podbean.com/podcast-detail/nx4ji-4d358/Jim-Cornette%E2%80%99s-Drive-Thru-Podcast
- Fightful (about): https://www.fightful.com/about/
- WWE Radio on SiriusXM: https://corporate.wwe.com/about/news/2026/07-23-2026 ; https://www.siriusxm.com/blog/wwe-radio
- WrestleTalk: https://wrestletalk.com/videos/
