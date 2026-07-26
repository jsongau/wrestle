# Wrestle Lore — Vision Spec D: Community & Gamification

Role: community and gamification futurist. Mission: turn a read-only database into a review network
and a game. The engagement loop wrestling fans crave is not "look things up," it is "rate it, argue
about it, book the card yourself, and get credit for knowing more than the next fan." This spec lays
out the UGC and game layer, splits it cleanly into what ships on the current static stack versus what
needs a backend, and sequences it so the site delivers real value long before a database exists.

- Date: 2026-07-26
- Grounding read: `00-content-data-research.md`, `01-inspiration-research.md`, sibling specs
  `vision/A-new-content-types.md` and `vision/B-interactive-tools.md`.
- Existing routes to wire into: `/wrestlers/` (89), `/matches/` (30 rated), `/rivalries/` (15),
  `/promotions/{wwe,wcw,ecw,tna,nxt}/`, `/events/` (5 PLE editions + 5 brand hubs), `/moments/` (4),
  `/rankings/`, `/membership/` and `/membership/growth-strategy/`.
- Standing constraints honored in Phase 0: static HTML, no build step at request time, one
  `css/site.css`, vanilla JS, no browser storage, root-absolute links, every page pre-rendered.
- The one hard rule that shapes everything: **no browser storage**. That means nothing personal can
  persist client-side. Anything a user "owns" (their ratings, their saved cards, their badges) needs a
  backend. So Phase 0 gamification is built entirely from **URL state** and **editorial/cited data**,
  and personal ownership arrives with Supabase in Phase 2.
- Fact rule: no invented ratings, vote counts, or reign data. Every seeded number carries a `VERIFY`
  flag and is labeled editorial until real user data replaces it.

---

## The sequencing thesis

Three phases. The site is fully useful and addictive at the end of Phase 0 with zero backend. Phase 1
is an optional, still-static bridge. Phase 2 lights up the true UGC economy on Supabase and becomes the
membership-growth engine the WWE role is hiring for.

- **Phase 0 (static now, no backend):** the game layer runs on URL state and cited/editorial data.
  Fantasy booking, watch-along hubs, editorial leaderboards, curated collections, and poll *showcase*
  pages all ship today. They travel as links, they are crawlable, they seed demand.
- **Phase 1 (static bridge):** pre-render the highest-demand permutations (top dream cards, top poll
  debates) as real pages so crawlers and AI answer engines index them. Still no backend. This is where
  the shareable galleries get their SEO teeth.
- **Phase 2 (Supabase backend):** accounts, real user star-ratings and written reviews, saved and
  upvoted fantasy cards, live polls, personal collections, badges, and reviewer leaderboards. A cron
  job writes community aggregates back into static JSON snapshots so pages stay fast and crawlable.
  This phase is the funnel: free to read, account to rate, membership to collect.

The trick that keeps Phase 2 honest with the site's crawlable-first DNA is the **hybrid write-back**:
user data lives in Postgres, but a scheduled edge function rolls it up and rewrites the static
aggregate files (rating averages, leaderboard order, poll totals). Pages render those snapshots as
plain HTML. The database powers the loop; the static snapshot keeps the SEO and speed.

---

## PHASE 0 — Static now, no backend

### 1. Fantasy Booking Studio — `/booker/`

**Route:** `/booker/` (hub and interactive builder) plus `/booker/{slug}/` for pre-rendered dream
cards (Phase 1 galleries, e.g. `/booker/attitude-era-dream-card/`, `/booker/bloodline-vs-nwo/`).

**What it does.** The single most-loved wrestling-fan pastime is booking the show yourself. Pick a
venue and an event name, then build a full card of 4 to 7 matches by choosing wrestlers from the roster,
setting a stipulation (Steel Cage, Iron Man, Hell in a Cell, Ladder), and picking a winner. The card
renders as a poster-style match sheet. State lives entirely in the URL query string, so the finished
card is a copy-paste share link and a crawl surface at the same time.

**Why it wins.** Fantasy booking is the highest-intent, highest-replay behavior in the fandom and it is
inherently viral: every card a fan builds is a link they want to send to argue with friends. That is a
backlink and a social-share engine with zero paid distribution. It also has near-infinite long-tail
SEO ("dream match [A] vs [B]") that the comparator in Spec B does not cover because this is
*card-level*, not pair-level.

**Buildability.** Static now. One vanilla-JS builder reads `/data/entities.json` (the shared asset
defined in Spec B), no framework. State encodes as `?e=Dream+Slam&m1=cm-punk:stone-cold:iron-man&
m2=rhea-ripley:charlotte-flair:cage&win1=cm-punk`. Phase 1 pre-renders a curated gallery of the
best cards as real HTML with JSON-LD `ItemList` and full copy. **Backend flag:** *saving* a card to a
profile, *upvoting* other fans' cards, and a community card leaderboard are Phase 2 (needs Supabase).

**Cross-links.** Every wrestler slot links to `/wrestlers/{slug}/`; a chosen stipulation links to the
matching real example under `/matches/`; the "inspired by" footer links to relevant `/rivalries/` and
`/events/` pages. The builder cross-promotes Spec B's `/compare/` for any two-name matchup.

---

### 2. Watch-Along Hubs — `/watch/`

**Route:** `/watch/` (hub) plus `/watch/{event-slug}/` per upcoming or recent card, e.g.
`/watch/summerslam-2026/`, `/watch/wrestle-kingdom-2026/`.

**What it does.** A live-event companion. Each hub answers "what is on, when, and where do I watch it,"
using the verified streaming facts already researched (Raw on Netflix, WWE PLEs on ESPN in the US and
Netflix internationally, AEW on HBO Max, NJPW on NJPW World, TNA on AMC and TNA+). Below the
how-to-watch block sits the printable match card and a prompt to rate each match after it happens. A
"start time in your timezone" line is computed client-side from a single UTC value, no backend.

**Why it wins.** "How to watch [event]" is recurring, high-volume, deadline-driven search that spikes
on event weeks, and the incumbents are ad-choked aggregators. Owning it captures fresh traffic on a
schedule and it is the natural home for the streaming badges. It also feeds the membership funnel: the
watch hub is where a fan who just watched a five-star match is most primed to rate it and sign up.

**Buildability.** Pure static. The streaming rows are the same platform chips the brand cards use.
`VERIFY` every card, date, and platform at publish because TV rights move fast. **Backend flag:** a
live "rate as you watch" widget and a live watch-party chat are Phase 2; Phase 0 shows the card and a
"rate it after" prompt that deep-links to the match page.

**Cross-links.** Links to the `/events/{slug}/` results page, to each `/promotions/{slug}/` for the
streaming context, to `/matches/` for any already-rated bout on the card, and to `/membership/` with a
"never miss a card" pitch.

---

### 3. Editorial Leaderboards — `/leaderboards/`

**Route:** `/leaderboards/` (hub) plus faceted pages: `/leaderboards/matches-2026/`,
`/leaderboards/matches-all-time/`, `/leaderboards/matches/wwe/`, `/leaderboards/matches/wcw/`,
`/leaderboards/rivalries/`, `/leaderboards/upsets/`.

**What it does.** Ranked, numbered lists of the highest-rated matches by year, promotion, and category.
Phase 0 ranks by the site's editorial rating plus cited community consensus (Cagematch, Meltzer),
clearly labeled as such. The number and the rank are the hook: "who is number one" and "did I see all
ten" are the two most reliable curiosity triggers in the medium.

**Why it wins.** Ranked lists are the most shareable and most link-earning content type on any database
site, and they are pure completionist bait for deep sessions. They also give AI answer engines a clean
`ItemList` to lift. This is the same ranked-content lever Spec A names, framed here as the seat the
*community* leaderboard will take over in Phase 2 with real votes.

**Buildability.** Pure static, rendered from match front-matter. **Backend flag:** the seeded ranks are
editorial today; in Phase 2 the same pages re-sort by real user aggregate ratings via the write-back
snapshot, and a `/leaderboards/reviewers/` page ranks top human reviewers (needs accounts).

**Cross-links.** Every entry links to its `/matches/{slug}/`; category headers link to the relevant
`/promotions/`, `/eras/` (Spec A), and `/rankings/` pages.

---

### 4. Curated Collections — `/collections/`

**Route:** `/collections/` (hub) plus `/collections/{slug}/`, e.g. `/collections/five-star-club/`,
`/collections/every-bloodline-match/`, `/collections/wcw-nitro-classics/`,
`/collections/wrestlemania-main-events/`.

**What it does.** Themed checklists a fan mentally ticks off. Each collection is a hand-authored set of
matches or wrestlers around one idea, rendered as a poster grid with a completeness cue ("18 matches,
you have reached the end of the set"). This reproduces the Letterboxd "films watched" pull without any
login, because the *feeling* of a finite, checkable set is the reward.

**Why it wins.** Collections are cheap to author, extremely shareable, and rank for browse-intent
queries. They are also the scaffolding for Phase 2 personal collections: the same slugs become
trackable once accounts exist, so a fan can mark a set complete and earn a badge.

**Buildability.** Pure static. **Backend flag:** *personal* progress ("you have watched 12 of 18") and
the badge for completing a set are Phase 2, because no-browser-storage means completion cannot persist
client-side.

**Cross-links.** Each item links to its entity page; collection footers link to the parent
`/promotions/`, `/eras/`, and `/rivalries/` hubs.

---

### 5. Hot-Take Poll Showcase — `/polls/`

**Route:** `/polls/` (hub) plus `/polls/{slug}/`, e.g. `/polls/austin-or-rock/`,
`/polls/best-wrestlemania-main-event/`.

**What it does.** Each poll page frames a genuine debate with both sides argued from cited data (peak
ratings, title reigns, signature matches) and a clear question. Phase 0 ships the *debate page* and a
results snapshot, not live voting, because storing votes requires a backend and browser storage is off
the table.

**Why it wins.** Debate is the native language of the fandom and poll pages are dwell-time and
comment-bait magnets. Even as static debate pages they capture "[A] vs [B] who is better" search and
set up the Phase 2 payoff where the vote goes live.

**Buildability.** Static showcase now. **Interim option (flag):** a lightweight third-party poll embed
can add real voting before Supabase exists, at the cost of an external dependency and off-site data;
recommend skipping it and going straight to native voting in Phase 2 for data ownership. **Backend
flag:** native live voting, per-day one-vote limits, and result history are Phase 2.

**Cross-links.** Each side links to the two `/wrestlers/` profiles and their top `/matches/`; the
result links to the relevant `/leaderboards/` and `/compare/` pages.

---

### 6. Badge System — defined now, awarded later

**Route:** `/badges/` (the taxonomy and how-to-earn page, static now).

**What it does.** Publish the full badge catalog as a static reference page so the game's rules are
visible and aspirational before any badge can be earned. Badges fall into three honest families:
**Reviewer** (rated 10, 50, 250 matches; wrote your first review), **Historian** (completed a
collection; visited every promotion hub), and **Booker** (published a dream card; a card of yours hit
the community leaderboard). Naming uses specific wrestling nouns, not generic points: "Five-Star
Scout," "Nitro Completionist," "Head Booker."

**Why it wins.** A visible badge catalog is a promise that pulls sign-ups the moment accounts exist. It
also tells the WWE hiring manager exactly what the retention loop is before a line of backend runs.

**Buildability.** The catalog page is static. **Backend flag:** *earning and displaying* badges needs
accounts, so awards are Phase 2. Ship the catalog in Phase 0 as a "coming with accounts" showcase tied
to the membership pitch.

**Cross-links.** Links to `/membership/`, `/booker/`, `/collections/`, and `/leaderboards/`.

---

## PHASE 2 — The UGC economy on Supabase

This is where Wrestle Lore becomes a review network and the membership funnel closes. Everything below
needs a backend; the recommended stack is **Supabase** (Postgres, Auth, Row Level Security, Edge
Functions). The design principle is unchanged: the database powers the loop, a scheduled write-back
keeps the public pages static and crawlable.

### 7. User star-ratings and written reviews — the flagship

**Routes touched:** every `/matches/{slug}/` gains a "Rate this match" control and a reviews section;
new `/reviews/{match-slug}/` review-detail pages; `/u/{username}/` profile with a user's rating history.

**What it does.** Signed-in fans give a 1 to 5 star rating and an optional short written review on any
match (and, later, wrestlers and events). The site already ships `Review` and `AggregateRating` JSON-LD
on match pages, but those numbers are editorial today. Real user ratings turn that markup into
*legitimate* aggregate data, which is a large SEO and GEO upgrade because AI answer engines weight
genuine review counts. Micro-reviews (short, punchy, capped length) beat essays for scannability and
match the Letterboxd model in the research.

**Why it wins.** This is the retention spine the whole competitive set (Cagematch, Letterboxd) is built
on. It is also the single strongest reason to create an account, so it is the top of the membership
funnel. Genuine `AggregateRating` with a real `ratingCount` is the highest-leverage GEO move on the
site.

**Backend / Supabase.** Tables: `profiles`, `ratings(user_id, match_slug, stars, created_at)` with a
unique constraint on `(user_id, match_slug)`, `reviews(user_id, match_slug, body, created_at)`. RLS so
a user writes only their own rows and everyone reads aggregates. An Edge Function on a cron rolls up
per-match averages and counts into `/data/ratings.json`; the static match page renders that snapshot,
so the public page stays fast and crawlable while the live control posts to the API. **VERIFY:** cap
review length and run basic moderation before display.

**Cross-links.** Reviews link author to `/u/{username}/`; profiles link every rating back to its
`/matches/{slug}/`; high-rated matches float up the `/leaderboards/` that now re-sort on real data.

---

### 8. Community fantasy booking — saved and upvoted cards

**Routes:** `/booker/community/` (browse and sort fan cards), `/booker/community/{card-id}/` (a saved
card), `/u/{username}/` lists a user's published cards.

**What it does.** The Phase 0 builder gains "save to profile" and "publish." Other fans upvote cards,
and a community leaderboard ranks the best. This closes the loop the builder opened: creation, then
credit, then competition.

**Why it wins.** Save-and-upvote converts a one-off share into a returning-creator habit and a UGC
content farm that keeps producing crawlable pages for free. The community leaderboard is a status game
that drives the "Head Booker" badge and, through it, membership.

**Backend / Supabase.** Tables: `cards(id, user_id, event_name, created_at)`,
`card_matches(card_id, slot, wrestlers, stipulation, winner)`, `card_votes(card_id, user_id)` with a
unique constraint per user. Write-back snapshot renders the top community cards as static pages for SEO.

**Cross-links.** Card pages link to every `/wrestlers/` slot and to `/booker/` to remix; the leaderboard
links to `/leaderboards/` and `/badges/`.

---

### 9. Live polls and reviewer leaderboards

**Routes:** `/polls/{slug}/` gains live voting; `/leaderboards/reviewers/` ranks top human reviewers.

**What it does.** The Phase 0 debate pages start counting real votes with a one-vote-per-user-per-day
rule, and a reviewers leaderboard ranks fans by review count and helpfulness. Both are pure status
mechanics that reward showing up.

**Backend / Supabase.** `poll_votes(poll_slug, option, user_id, voted_on)` with a unique constraint on
`(poll_slug, user_id, voted_on)`; reviewer rank is a materialized view over `reviews` and a
`review_helpful` table. Cron write-back renders result snapshots and leaderboard order into static JSON.

**Cross-links.** Poll results link to `/compare/` and `/leaderboards/`; reviewer profiles link to
`/u/{username}/`.

---

### 10. Personal collections, watchlist, and badges

**Routes:** `/u/{username}/` (profile with badges, watchlist, completed collections), and per-user
progress overlaid on the static `/collections/{slug}/` pages.

**What it does.** The Phase 0 curated collections become trackable. A fan marks matches watched, sees
"12 of 18," saves a watchlist, and earns the badges from the Phase 0 catalog. This is the completionist
payoff that no-browser-storage made impossible until now.

**Backend / Supabase.** `watchlist(user_id, match_slug)`, `collection_progress(user_id, collection_slug,
match_slug)`, `user_badges(user_id, badge_slug, earned_at)`; badges awarded by triggers or a nightly
function. Public profile pages render from a cached snapshot.

**Cross-links.** Profiles link every tracked item to its entity page and every badge to `/badges/`.

---

## The membership funnel (why this maps to the WWE role)

Gamification is the growth mechanism, not decoration. The funnel is a clean three-tier ladder that the
`/membership/` pages already anticipate:

- **Anonymous (Phase 0 value):** read everything, build and share fantasy cards, use watch hubs, browse
  leaderboards and collections. The site is genuinely useful with zero friction, which is what earns the
  first visit and the first share.
- **Free account (Phase 2 hook):** rate matches, write reviews, save one fantasy card, start earning
  Reviewer badges. The trigger is a fan who just watched a five-star match on a watch hub and wants to
  register their take. Rating is the lowest-friction, highest-frequency reason to sign in.
- **Member (Phase 2 revenue):** unlimited saved cards, exclusive and early-access polls, profile
  customization, premium badges, and a place on the reviewer leaderboard. Status and collection are the
  paid pull, not a paywall on facts.

The measurable growth story a hiring manager wants: share links from `/booker/` and `/polls/` drive
top-of-funnel visits, watch hubs convert event-week traffic, rating is the account-creation trigger, and
badges plus leaderboards drive the account-to-member step. Every step is a named route with an
instrumented event.

---

## Anti-AI microcopy standard (applies to every surface above)

Specific nouns, no decorative arrows, no em-dash separators, no cliché filler. Sample control copy:

- Rate control: "Give it your stars." Not "Rate now to unlock more."
- Fantasy card share: "You booked Dream Slam. Send it to someone who will argue." Not "Share your
  amazing card!"
- Empty leaderboard state (Phase 0): "These ranks are our call plus cited consensus. Your votes take
  over when accounts arrive."
- Badge catalog: "Rate 250 matches to earn Five-Star Scout." Not "Collect points and level up."

---

## Ranked build order

Score = (share and SEO upside) x (buildability on the current static stack). Static-now items win the
top slots because they ship value before any backend.

| Rank | Feature | Route | Phase | Backend? |
|---|---|---|---|---|
| 1 | Fantasy Booking Studio | `/booker/` | 0 | No (save/upvote = Phase 2) |
| 2 | Watch-Along Hubs | `/watch/` | 0 | No |
| 3 | Editorial Leaderboards | `/leaderboards/` | 0 | No (re-sort on real votes = Phase 2) |
| 4 | Curated Collections | `/collections/` | 0 | No (personal progress = Phase 2) |
| 5 | Hot-Take Poll Showcase | `/polls/` | 0 | No (live voting = Phase 2) |
| 6 | Badge catalog | `/badges/` | 0 | No (awards = Phase 2) |
| 7 | User ratings + reviews | `/matches/*`, `/reviews/`, `/u/*` | 2 | Supabase |
| 8 | Community fantasy cards | `/booker/community/` | 2 | Supabase |
| 9 | Live polls + reviewer board | `/polls/*`, `/leaderboards/reviewers/` | 2 | Supabase |
| 10 | Personal collections + badges | `/u/*` | 2 | Supabase |

---

## Sources and verification notes

- Streaming facts for watch hubs: `00-content-data-research.md` section 1 (all carry existing
  confidence flags; re-`VERIFY` per event at publish).
- Rating and review-network patterns, leaderboard and collection psychology: `01-inspiration-research.md`
  Parts A and B (Cagematch, Letterboxd, IMDb).
- Shared `/data/entities.json` dependency and URL-state pattern: `vision/B-interactive-tools.md` section 0.
- `/eras/`, `/titles/`, and ranked-content leverage: `vision/A-new-content-types.md`.
- Every seeded rating, rank, or vote total in Phase 0 is editorial or cited and must be labeled as such
  on-screen until real user data replaces it in Phase 2.
