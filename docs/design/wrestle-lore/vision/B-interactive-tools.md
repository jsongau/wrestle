# Wrestle Lore — Vision Spec B: Interactive Tools

Role: interactive-tools designer. Mission: client-side, no-backend pages that create addictive replay
value, stay fully crawlable, and travel as shareable links. Everything here runs on the existing
stack (static HTML, one `css/site.css`, vanilla JS, no browser storage). State lives in the **URL query
string**, which doubles as the share mechanism and the crawl surface. No fabricated facts; fields that
need sourcing are flagged `VERIFY`.

Grounded in `/root/wwe/docs/design/wrestle-lore/00-content-data-research.md` and `01-inspiration-research.md`.
Existing routes referenced: `/wrestlers/{slug}/` (89), `/matches/{slug}/` (30 rated), `/rivalries/` (15),
`/promotions/{wwe,wcw,ecw,tna,nxt}/`, `/events/` (5 PPV editions + 5 hubs), `/moments/` (4).

---

## 0. The one shared dependency: `entities.json` (build once, feed every tool)

Every tool below reads a single static data file, generated at author time from the same front-matter
that already builds the pages. This is not a backend — it is one more static asset next to
`js/search-index.js`, which today already ships `{t,u,k}` (title, url, kind) for 89+ objects.

Ship `/data/entities.json` extending that index with per-wrestler fields the tools need:

```
{ "slug":"cm-punk", "name":"CM Punk", "url":"/wrestlers/cm-punk/",
  "status":"current", "gender":"male", "promotions":["wwe"], "era":"modern",
  "debutYear":1999, "finisher":"GTS", "signatureMatches":["/matches/cm-punk-vs-cena-mitb-2011/"],
  "rivalries":["/rivalries/punk-vs-cena/"], "factions":["the-shield-adjacent"],
  "titlesCount":2, "peakRating":4.75, "loreScore":88 }
```

Rules that keep it honest and buildable:
- Only emit fields already authored in `.md` front-matter. `debutYear`, `finisher`, `titlesCount` are
  factual and citable. `loreScore`/`peakRating` are **editorial/derived** and must be labeled as such
  on-screen, never presented as an official stat. `VERIFY` height/weight/debut before locking.
- One file, gzipped it is small (< 60 KB for ~120 entities). Loaded once, cached, powers all tools.
- The build step for this is trivial: the existing `build_wrestlers_*.py` scripts already parse the
  front-matter; add one emitter that writes `entities.json`. No framework, no bundler.

Crawlability pattern used by every tool (the important part):
1. **App shell** at `/lab/...` or `/play/...` — a single static HTML page that reads URL params and
   hydrates from `entities.json`. This is the interactive surface.
2. **Pre-rendered gallery** — a curated set of the highest-demand permutations rendered as real static
   HTML pages (e.g. `/compare/cm-punk-vs-john-cena/`) with full copy, JSON-LD, and internal links.
   Crawlers and AI answer engines index these; the shell handles the long tail via params.
3. Every shell and gallery page ends in the mandatory "Keep going" links block (retention + SEO).

---

## 1. HEAD-TO-HEAD COMPARATOR — `/compare/` + `/compare/{a}-vs-{b}/`

**What it does.** Side-by-side "tale of the tape" for any two wrestlers: debut year, promotions,
championships count, signature match (with its Wrestle Lore rating), era, finisher, and the derived
Lore Score as a labeled editorial metric. Pick two from a search field; the page rebuilds instantly.

**Data it needs.** `entities.json` only. Zero new facts beyond what profiles already carry.

**Crawlable / shareable.** State is `?a=cm-punk&b=stone-cold`, so any comparison is a copy-paste link.
Pre-render the ~150 most-searched pairs as static `/compare/{a}-vs-{b}/` pages (rivals, era-mates,
GOAT debates: Austin vs Rock, Flair vs Sting, Rhea vs Charlotte). Each carries `ItemList` +
`ComparisonPage`-style JSON-LD and answers the literal query "[A] vs [B] stats". This is pure GEO fuel:
"who has more titles, X or Y" is a question AI engines love to cite a clean table for.

**Engagement hook.** Debate settling. Every comparison invites the next ("okay now Punk vs Bryan"),
and each row links to the deeper page (championship count links to that wrestler's title history).

**Why it wins.** Highest SEO demand of any tool (vs-queries are enormous), lowest build cost, no
`VERIFY` risk if it only surfaces authored fields. Ship this first.

**Cross-links.** Into `/wrestlers/{a}` and `/wrestlers/{b}`, the shared `/rivalries/{slug}/` if one
exists, and any `/matches/` they both appear in.

**Backend flag.** None.

---

## 2. DREAM-MATCH BOOKER — `/lab/dream-match/` + gallery `/dream-match/{a}-vs-{b}/`

**What it does.** Pick two (or a 2v2 / triple threat) wrestlers who never met, and the tool books a
fantasy result: a **deterministic** outcome derived from encoded stats (era-adjusted Lore Score,
division, finisher clash), a generated finish line ("[Winner] reverses into the [finisher] at 18:42"),
and a "how the crowd reacts" read. Same inputs always produce the same booking, so a shared link shows
your friend exactly what you saw.

**Data it needs.** `entities.json` (stats + finisher). The booking logic is a small pure function of
those fields plus a seed from the two slugs. **No RNG that drifts** — determinism is what makes it
shareable and what stops it from feeling like a slot machine.

**Crawlable / shareable.** `?a=&b=&stip=` in the URL. Pre-render a "Dream Match Hall" gallery of ~60
marquee never-happened bouts (Austin vs Punk, Andre vs Lesnar, Rhea vs Chyna, Flair vs Gunther) as
static pages, each with an editorial paragraph explicitly framed as **fantasy booking, not a real
result** (anti-misinformation; important for a WWE hiring manager reading this).

**Engagement hook.** The "what if" is the oldest addiction in wrestling fandom. Restipulation
(cage, Iron Man, Rumble entry number) re-rolls the booking and multiplies replays.

**Why it wins.** Uniquely wrestling, screenshot-native (people post their booking), and it demonstrates
product taste to a TKO manager: fan fantasy converted into a shareable object.

**Cross-links.** Winner/loser profiles, their real signature matches, the promotion hubs, and the
Comparator (a "see the real stats" button).

**Backend flag.** None. (A future "most-booked dream matches" leaderboard would need a backend to
count — flagged, not required for v1.)

---

## 3. GUESS THE WRESTLER — daily game — `/play/guess/`

**What it does.** A Wordle-style daily puzzle. One wrestler per day; the player gets progressive clues
(era, then promotion, then debut decade, then finisher, then a silhouette or duotone-blurred poster)
and guesses via the same typeahead the ⌘K search uses. Guess in fewer clues, better score. A shareable
spoiler-free result grid ("Wrestle Lore Guess #204 — 3 clues") for social.

**Data it needs.** `entities.json` for clues and the answer set; the existing poster art for the
silhouette reveal (CSS filter, no new assets).

**Crawlable / shareable.** The daily answer is chosen by a **date-seeded index into a shuffled slug
list** — no storage, no backend, no clock cheating that matters (everyone on 2026-07-26 gets the same
puzzle because the seed is the date). The result string is copy-paste, Wordle-style. The page itself is
one static route; an archive of past-day recap pages (`/play/guess/archive/`) is crawlable content.

**Engagement hook.** The single strongest **return-visit** mechanic on the site: a new puzzle every
day gives a reason to come back daily, which is exactly the membership-growth behavior the funnel wants.
Streak framing works even without storage ("come back tomorrow for #205").

**Why it wins.** Daily habit loop + viral share grid + a soft conversion moment ("save your streak —
join Wrestle Lore" links into `/membership/`). This is the flagship replay-value play.

**Cross-links.** The reveal card links to the answer's profile; a "play the deep cut" mode filters to
LEGENDS or a single promotion, each a linkable variant (`?mode=wcw`).

**Backend flag.** None for the core game. Cross-device streaks / global stats would need a backend
(flagged; not needed for launch — keep streaks honest and local-feel via the date seed).

---

## 4. SIX DEGREES OF WRESTLING — `/lab/connect/` + gallery `/connect/{a}-to-{b}/`

**What it does.** Enter two wrestlers; the tool finds the shortest chain linking them through shared
matches, rivalries, factions, and promotions ("Austin → shared Survivor Series team → Bret Hart →
faced → Owen Hart"). A breadth-first search over the relationship graph, client-side.

**Data it needs.** `entities.json` edges (rivalries, factions, co-participants in `/matches/`). The
data already exists across the 30 matches, 15 rivalries, and faction tags; this tool just traverses it.

**Crawlable / shareable.** `?from=&to=` state; pre-render a gallery of surprising connections
("How is IYO SKY connected to Ric Flair?") as static pages — these are irresistible AI-answer-engine
and long-tail targets because they read like trivia questions with a sourced answer.

**Engagement hook.** Pure rabbit hole. Every node in the chain is a click into a deeper page, so the
tool literally generates guided deep sessions — the B2 "next-links" lever as a game.

**Why it wins.** No competitor (Cagematch, Sherdog) has this. It is the most "future of wrestling
databases" idea here and it turns the internal-link graph into a playable feature.

**Cross-links.** Every node links to its profile; every edge links to the match/rivalry that proves it
(receipts, not vibes).

**Backend flag.** None. Graph is small enough for instant client-side BFS.

---

## 5. CAREER TIMELINE EXPLORER — `/lab/timeline/` + embedded on each profile

**What it does.** A horizontal, scrubbable timeline of a wrestler's career: debut, promotion moves,
title wins, signature matches (each a rated dot), Hall of Fame induction. Filter the master mode to
"show me everyone active in 2001" and it becomes an era slider across the whole roster.

**Data it needs.** `entities.json` dated events per wrestler (debut, title years, match dates). Match
dates already exist on `/matches/` pages; title/debut years are mostly authored but `VERIFY` any not
already on the profile.

**Crawlable / shareable.** Per-wrestler timeline renders inside the existing profile page (progressive
enhancement — the facts are in static HTML, JS just makes them scrubbable), so it is crawlable by
default. The master era-slider shell uses `?year=2001`; pre-render decade hubs (`/timeline/attitude-era/`,
`/timeline/2020s/`) as static SEO pages.

**Engagement hook.** "Who was on the roster the year I started watching" is a nostalgia magnet, and the
era hubs are prime browse lanes feeding the poster wall.

**Why it wins.** Doubles as content (era pages rank) and as a profile enrichment that lifts time-on-page.

**Cross-links.** Timeline dots link to matches/events; era hubs link to every wrestler active that year
and to the matching `/events/` editions.

**Backend flag.** None.

---

## 6. BOOK THE CARD — fantasy PPV builder — `/lab/book-the-card/`

**What it does.** Build a full fantasy pay-per-view: pick a venue/event skin (WrestleMania, Rumble),
add matches from the roster, set the order and stipulations, name your main event. Output is a
share-ready match card poster in the Broadcast Bold style.

**Data it needs.** `entities.json` for the roster picker; the existing `/events/` hubs for skins.

**Crawlable / shareable.** The whole card encodes into the URL (compact param scheme:
`?m1=a~b&m2=c~d~e&main=1`). A shared link reconstructs the exact card — no storage, no backend. Ship a
"Featured Fantasy Cards" gallery of editorial dream PPVs as static pages.

**Engagement hook.** Creation + identity. People share the card they built; each shared link is an
inbound acquisition path. Long session time (building beats browsing).

**Why it wins.** It is the single most "I made this" artifact on the site — the kind of UGC-feeling
output that spreads on wrestling social without needing a UGC backend.

**Cross-links.** Every slotted wrestler links to their profile and to the Dream-Match Booker to
"simulate" that slot; the event skin links to the real `/events/` hub.

**Backend flag.** Saving/publishing a card to a public gallery would need a backend. The URL-encoded
share covers v1 fully; only a persistent public "top cards" board needs storage (flagged, deferred).

---

## 7. BRACKET & PREDICTION MAKER — `/play/bracket/{event}/`

**What it does.** For tournament-shaped events (Royal Rumble entry predictor, King/Queen of the Ring
bracket, a "who wins the title" PLE predictor), fill a bracket or make picks; the tool renders your
completed bracket as a shareable image-style layout. When real results are authored on the `/events/`
page, a **results overlay** grades your picks.

**Data it needs.** `entities.json` roster + the real card/results already authored on the 2026
`/events/` editions (Royal Rumble, WrestleMania 42, etc.).

**Crawlable / shareable.** Picks encode in the URL; the bracket shell is one static page per event.
Pre-Rumble, the page is a prediction toy; post-event it becomes a "how the bracket actually went" recap
that stays as evergreen crawlable content.

**Engagement hook.** Prediction before a PLE, grading after — a two-visit loop tied to the real
wrestling calendar, which naturally times traffic spikes to WWE's actual schedule.

**Why it wins.** Ties the site's replay value to the live product cadence the hiring manager cares
about, and the pre/post structure gives every event two content lives.

**Cross-links.** Into the specific `/events/{edition}/`, participant profiles, and the Comparator.

**Backend flag.** Client-side grading against authored results = no backend. A live leaderboard of
whose bracket scored best across all users = backend (flagged, deferred).

---

## 8. STAR-RATING SIMULATOR + PAIRWISE RANKER — `/rate/{match}/` and `/lab/my-top-ten/`

**What it does.** Two linked pieces:
- **Rate-along** on any `/matches/` page: drag a 5-star slider, then reveal how your rating compares to
  the Wrestle Lore editorial rating and (where cited) the community/Meltzer figure. No storage — your
  rating lives only in the session and in a shareable `?stars=4.5` link.
- **Pairwise ranker** `/lab/my-top-ten/`: the tool shows two matches ("which was better?"); repeated
  choices build your personal Top 10, encoded in the URL to share and compare.

**Data it needs.** `entities.json` / match ratings already authored.

**Crawlable / shareable.** Rate-along is progressive enhancement on existing crawlable match pages.
The ranker's result Top 10 is a shareable URL; a curated "Wrestle Lore Top 10 Matches" stays static
and crawlable with `ItemList` JSON-LD.

**Engagement hook.** Opinion + comparison ("I rated it higher than the site did") is inherently
shareable and argument-starting.

**Why it wins.** Turns passive ratings into participation without the moderation and spam cost of open
voting. Matches Cagematch's rating spine but keeps v1 backendless.

**Backend flag.** Persistent aggregate community ratings require a backend + anti-abuse (flagged,
deferred). V1 = compare-to-editorial only, which needs nothing.

---

## Priority & buildability ranking

| Tool | Build cost | SEO/GEO | Replay | Backend for v1 |
|---|---|---|---|---|
| Comparator (#1) | Low | Very high | Med | None |
| Guess the Wrestler (#3) | Med | Med | Very high | None |
| Six Degrees (#4) | Med | High | High | None |
| Dream-Match Booker (#2) | Med | Med | High | None |
| Timeline (#5) | Med | High | Med | None |
| Book the Card (#6) | High | Med | High | None (share); backend only for public gallery |
| Bracket (#7) | Med | Med | High (calendar-timed) | None (share/grade); backend for leaderboard |
| Rating sim / ranker (#8) | Low | Med | Med | None; backend only for aggregate votes |

Two nav homes: `/lab/` (build/explore tools) and `/play/` (games), each a crawlable hub that ends in
the mandatory "Keep going" block. Route all of these through existing dropdowns per the mega-nav
contract — do not widen the top bar.

## Anti-AI copy standard applied
Specific nouns (GTS, Wrestle Kingdom, entry number 30), no decorative arrows in prose, no em-dash
separators, no "unleash/dive into/game-changer" filler. Every fantasy output is labeled fantasy; every
derived metric is labeled editorial; every unverified field carries `VERIFY`.
