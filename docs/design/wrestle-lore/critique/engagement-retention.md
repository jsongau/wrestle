# Wrestle Lore — Engagement / Retention / Conversion Critique

Adversarial review by the engagement/retention + conversion critic. Scope: the addictive-browsing
loop (keep-going hooks, rabbit-hole links, dead-ends), and the membership funnel now that the loud
hero CTA is being de-emphasized. Every finding cites a real file/selector, states the fix, confirms
buildability on a static no-build crawlable site (backend needs are flagged), and ties to a funnel
metric: **acquisition / retention / engagement / trust / revenue**. Copy standard: no decorative
arrows, no em-dash separators, no cliche banned words.

Files reviewed live: `/index.html`, `/wrestlers/kane/index.html`, `/events/index.html`,
`/moments/mankind-hell-in-a-cell-fall-1998/index.html`, `/matches/cm-punk-vs-cena-mitb-2011/index.html`,
`/js/main.js`, `/js/enhance.js`, `/js/nav.js`. Spec reviewed: `07-addictive-browsing.md`,
`vision/D-community-gamification.md`.

---

## The one-sentence verdict

You wrote a genuinely excellent retention spec (`07-addictive-browsing.md`) and then shipped a site
that ignores almost all of it. The document describes a rabbit hole; the live pages are a set of
cul-de-sacs. **The single most damaging fact in this review: your own "gold-standard" profile,
`/wrestlers/kane/index.html`, ends with a match-record table and then the footer. Zero forward
links. No related wrestlers, no rivalry, no next profile, no email capture.** A reader who lands
there from Google has exactly one designed action left: leave.

That is the whole problem in one page. The rest of this document is severity-ranked.

---

## FINDING 1 — The flagship profile is a dead-end (highest impact)

**Problem.** `/wrestlers/kane/index.html` is the template every other profile is cloned from. Its
final three sections are `.sig-section` (Signature Matches, prose only, no links), `.record-section`
(a `.record-table` where only opponent names link), and then `<footer class="site-footer">`. After
the last table row (line ~199) there is nothing: no "Keep going" block, no related rail, no
"Fans also viewed", no trophy case, no next/previous wrestler, no newsletter capture. The richest
internal-link opportunity on the entire site is spent on a footer with three links.

Contrast: `07-addictive-browsing.md` §2 mandates a fixed engagement stack on every entity page
(Rail 1, Rail 2, Because-you-came-from, Collection panel, **Keep-going block as the last content
section**, Session trail). None of it is on Kane. The spec is not the site.

Also note the profile links are lopsided: the bio prose links Undertaker / Shawn Michaels / Daniel
Bryan (good), but the Championships, Personas, and Timeline blocks are pure text. "Team Hell No",
"The Authority", "King of the Ring 1998", "WrestleMania XIV" are all named and none are links, even
though event and rivalry pages exist. Every un-linked proper noun is a leaked click and a lost
crawl edge.

**Fix.** Ship the `07` engagement stack, starting with the mandatory Keep-going block. Concretely,
append to the profile template, in this order, before the footer:

1. A **"Signature matches" rail** (`.rail` from `07` §3) — turn the prose `.sig-match` cards into
   linked tiles to the actual match pages.
2. A **"Rivals and allies" rail** — Undertaker, Daniel Bryan, Triple H, X-Pac, etc., as tiles.
3. A **Trophy Case** (`07` §4.7) built from the champ/record data already on the page: title
   reigns, 5-star matches catalogued, HOF status, faction memberships. Filled badges link to proof.
4. A **Keep-going block** (`07` §4.1) as the last content: one peer wrestler, one rivalry, one
   promotion hub, one facet hub, one leaderboard (`/rankings/`), plus next/previous wrestler.

Also link every proper noun: event names in `.record-table` link to `/events/{slug}/`; faction
names link to the relationships/faction hub.

**Buildability.** Fully static. These are `<a href>` tiles emitted by the same Python build script
that stamps the profile. The `07` spec already defines the front-matter fields (`related[]`,
`matches[]`, `rivalries[]`, `accolades{}`) and the CSS (`.rail`, `.keepgoing`, `.collect`). No
backend. This is a build-script edit plus a CSS append, applied across ~89 profiles.

**Source.** IMDb's title pages end with a "More like this" / "Fans also liked" rail and a full cast
grid; the entire product is built so no page is terminal
(https://help.imdb.com/article/imdb/discover-watch/recommended-for-you-faqs/GPZ2RSPB3CPVL86Z). The
knowledge-graph write-up shows they treat every entity as a node with typed edges to keep users
hopping (https://aws.amazon.com/blogs/machine-learning/part-1-power-recommendation-and-search-using-an-imdb-knowledge-graph/).
Steal the pattern: no entity page without an outbound entity rail.

**Metric.** Retention (pages/session, bounce) is the primary lever; engagement and SEO/crawl depth
follow because every added link is a crawl edge. This is the #1 fix on the site.

---

## FINDING 2 — Terminal pages have no email capture; the funnel is a single point of failure

**Problem.** The only lead-capture surface on a content journey is the homepage waitlist
(`/index.html` `form[data-waitlist][data-source="home_hero"]`, line ~250) and the `/membership/`
page. Every deep-landing page — Kane, the Mankind moment, the CM Punk match, the events index — has
**no email field at all.** Search and social traffic lands on those deep pages, not the homepage. So
the funnel's only mouth is on the one page most organic visitors never see. That is a structural
leak, not a copy problem.

The moment page (`/moments/.../index.html`) ends at FAQ then footer. The events index
(`/events/index.html`) ends at the "Event Brands" grid then footer. Neither offers a reason or a
box to join.

**Fix.** Add one contextual capture module to the bottom of every entity page, above the footer and
below the Keep-going block. Not the generic "Join the front row" — make it match the page:

- On a profile: "Get the Rewind: one email a week, the best match from a wrestler like Kane, and the
  story behind it." (single email field, reuses `form[data-waitlist]`, new `data-source="profile"`).
- On a moment/match: "We break down one classic like this every week." with the same field.

Keep it one field and one button; the existing `main.js` `form[data-waitlist]` handler already
renders the `.form-success` state, so wiring is free.

**Buildability.** Static. Reuses the existing form component and the mock in-memory handler in
`main.js` (lines ~120-137). Production needs a real POST target (Klaviyo/Buttondown/ConvertKit form
endpoint) — that is a form `action`, not a backend you host, so it stays no-build. Flag: real
double-opt-in and the "founding-member badge" need an ESP account.

**Source.** Newsletter-first media (The Athletic, Morning Brew) place capture at the end of every
article, contextualized to the content just read, not only on the homepage. The principle: capture
where attention peaks, which is the bottom of the thing they came to read.

**Metric.** Acquisition and revenue directly. Moving capture onto the ~150 deep pages multiplies the
funnel's surface area by roughly the ratio of deep-landing to homepage-landing traffic (typically
5:1 or worse for a content DB).

---

## FINDING 3 — The rating loop, the single strongest mechanic a review site has, is broken and gated

**Problem.** On `/matches/cm-punk-vs-cena-mitb-2011/index.html` the "Rate this match" widget
(`fieldset.rate`, lines ~209-217) is five radio inputs with **no JavaScript handler anywhere** —
`main.js` and `enhance.js` bind nothing to `.rate` or `input[name="stars"]`. Clicking a star does
nothing visible, and the only affordance is "Join free to save your rating". So the highest-intent
micro-action on the site (a fan wanting to log an opinion) produces zero feedback and is immediately
wall-gated. On the profile pages there is no rating entry point at all.

This is the opposite of the proven model. Letterboxd's entire retention engine is the frictionless
log/rate/review loop: you can tap a star before you are asked to do anything, and the act of rating
is what builds the habit and the personal library that brings you back
(https://loyaltyrewardco.com/letterboxd-does-personalisation-drive-loyalty/). Wrestle Lore has the
review-network positioning ("most ADDICTIVE... review network") and none of the loop.

**Fix (two tiers).**

- **Tier 1, no backend:** make the star widget actually respond. On click, fill the stars, persist
  the value in `localStorage` (see Finding 4), and immediately show "You rated this 5. The Wrestle
  Lore rating is 5.0. See how your ratings compare." with a link to a personal `/my-ratings/` page
  that is generated client-side from localStorage. No login required to rate. The membership prompt
  becomes "Create a free account to sync these across devices", which is a real benefit, not a wall.
- **Tier 2, backend:** aggregate community ratings and show "4.8 from 2,314 fans" — this is the only
  part that needs a datastore. Flag it clearly; ship Tier 1 now.

**Buildability.** Tier 1 is pure client JS plus localStorage, fully static and crawlable (crawlers
ignore local state; the editorial 5.0 stays in the HTML). Tier 2 needs a serverless endpoint
(Supabase/Cloudflare KV) and is the one genuine backend dependency in this document.

**Source.** Letterboxd (rate-first, account-later, personal diary as the retention hook)
(https://letterboxd.com/about/faq/). The lesson: never gate the first rating; the rating IS the
onboarding.

**Metric.** Engagement then retention then revenue. The saved-ratings library is the reason a
first-time visitor returns, and "sync across devices" is a genuine, non-annoying upgrade prompt.

---

## FINDING 4 — The self-imposed "no browser storage" rule quietly kills the best returning-visitor mechanics

**Problem.** `main.js` header comment: "No localStorage/sessionStorage/cookies (in-memory only)."
`07-addictive-browsing.md` §1 doubles down and engineers heroic workarounds (referrer parsing, a
`#from=` URL-hash session trail, catalogue-completion instead of user-completion). Respect for the
ingenuity, but this is a self-inflicted wound. localStorage is client-side only, requires no
backend, does not break crawlability (crawlers never execute the personalization), and under GDPR a
functional-only local store with a one-line notice needs no cookie banner. By banning it you throw
away every mechanic that actually drags people back:

- Recently viewed / "Continue where you left off"
- A personal watchlist ("matches to watch")
- Seen/watched checkmarks on match tiles (the completionist itch)
- Saved ratings (Finding 3)
- A visit streak / "you've explored 3 days in a row"

The referrer + URL-hash trail in `07` §4.3-4.4 is clever but strictly weaker: it survives one hop,
dies on refresh, and pollutes URLs. It is a workaround for a constraint you chose.

**Fix.** Adopt `localStorage` for a defined tier of "functional memory" features. Keep the crawlable
static layer exactly as `07` designs it (rails and Keep-going stay raw `<a>`), and layer localStorage
personalization on top as progressive enhancement:

1. **Recently viewed rail** — on each entity page, push `{slug,title,type}` to a capped
   localStorage array; render a "Pick up where you left off" rail on the homepage and a compact one
   in the ⌘K empty state (Finding 6). ~30 lines of JS.
2. **Watchlist** — a bookmark toggle on match/event tiles; a `/watchlist/` page rendered from
   localStorage.
3. **Seen checkmarks** — a tap on a match tile marks it seen; show "You've seen 12 of 30 five-star
   classics" as an honest personal completion meter (the `07` §4.7 catalogue meter becomes a real
   personal meter).

**Buildability.** 100% static, no backend, no build step. One small `js/memory.js` module. Add a
short functional-storage note to the footer/privacy page. This is the highest-leverage architectural
change available to a static site.

**Source.** Duolingo's streak is the canonical case: it works on loss aversion — people return to
avoid breaking a run they can see (https://www.justanotherpm.com/blog/the-psychology-behind-duolingos-streak-feature,
https://apptitude.io/blog/how-duolingos-streak-mechanic-actually-works/). A streak needs persistence.
No storage, no streak, no daily return.

**Metric.** Retention above all (D1/D7 return rate). This unlocks Findings 3, 5, and 6.

---

## FINDING 5 — There is no daily hook. A wrestling database is sitting on the best "On This Day" content on the web and not using it

**Problem.** Nothing on the site gives a reason to come back *today* specifically. The homepage
`.marquee` (`/index.html` lines ~170-188) is seven hardcoded 5-star matches, literally duplicated in
the markup for the loop. It never changes. The `.stats-bar` counts up once and sits. There is no
"Match of the Day", no "On This Day in Wrestling", no countdown to the next event. For a dataset
that is entirely dated events, this is a glaring miss.

**Fix.** Add two date-driven, fully static modules:

1. **"On This Day in Wrestling"** homepage rail. A build-generated `/data/onthisday.json` keyed by
   MM-DD (King of the Ring June 28 1998, WrestleMania dates, debuts, title changes). A ~15-line JS
   snippet reads `new Date()`, pulls today's entries, and renders linked tiles. Different every day,
   zero backend. This is a returning-visitor magnet and a link farm into deep pages at once.
2. **Countdown to the next Premium Live Event.** You already list dated future events
   (`/events/index.html`: Night of Champions 2026, etc.). A countdown band ("Next: SummerSlam,
   14 days") is trivial JS date math against a static date and is a proven wrestling-fan hook.

Also replace the fake static marquee with the honest editorial "Trending / This week" rail that
`07` §4.5 already specifies (hand-ordered, no invented counters).

**Buildability.** Fully static. `onthisday.json` is a build artifact; the render is client JS reading
the local clock. No backend. The countdown is pure JS.

**Source.** Baseball-Reference and the broader sports-history genre run daily "On This Day" as a
core engagement loop precisely because it is inexhaustible and inherently fresh
(https://en.wikipedia.org/wiki/Baseball_Reference, https://allsportshistory.com/category/on-this-day-in-sports-history/).
Wrestling's dated-event corpus is tailor-made for it.

**Metric.** Retention (daily return) and acquisition (the "On This Day" module is share-bait and a
recurring social/newsletter unit).

---

## FINDING 6 — The ⌘K empty state and zero-result state are wasted browse surfaces

**Problem.** In `js/nav.js`, `render('')` with no query does `idx.slice(0, 8)` — it shows the first
eight items in index order (line ~39). That is arbitrary, not useful. And on zero results it prints
"No matches for '…'" and stops (line ~50), a hard dead-end inside the one tool built for discovery.

**Fix.** Two changes in `nav.js`, both trivial:

- **Empty state = browse surface.** With no query, seed the palette with Recently Viewed (from
  localStorage, Finding 4) plus a fixed "Start here" set (Trending, Legends, Women, Hall of Fame,
  Five-Star Club). This is exactly `07` §4.6, still unbuilt.
- **Zero-result = redirect, never a dead-end.** Replace the empty message with "Nothing for '{q}'.
  Try these" and the same four evergreen hubs.

**Buildability.** Static, ~15 lines in `nav.js`. No backend.

**Source.** Algolia/DocSearch-style command palettes and the `07` §4.6 spec both treat the empty
palette as a curated browse launchpad, never a blank box. The rule: a search box that can return
nothing is a leak; give it a floor of evergreen destinations.

**Metric.** Engagement and retention (search is a high-intent surface; a dead search is a lost
session).

---

## FINDING 7 — The footer is three links; it should be the site's crawl-and-rabbit-hole floor

**Problem.** Every page ends with `<footer class="site-footer">` containing exactly
`About · Methodology · Insider` (see `/index.html` line ~283, identical on Kane, events, moment).
On a 198-page database this is a wasted, sitewide, always-present slab of real estate. A fat footer
is the cheapest rabbit-hole and crawl-depth win available, and it appears on every single page for
free.

**Fix.** Replace with a fat footer: columns for Popular Wrestlers (8-10 top profiles), Five-Star
Matches, Event Series, Promotions, Hubs (Legends/Women/HOF), plus the newsletter field (Finding 2)
and the existing legal links. This turns the one guaranteed element on every page into a
distribution and internal-linking engine.

**Buildability.** Static, stamped by the shell that already stamps the current footer across ~170
pages. No backend. One shell edit propagates everywhere.

**Source.** IMDb, Wikipedia, and every large content DB use a dense footer as a permanent
navigation and crawl layer. It is the highest-ROI-per-effort change in this document because it
ships once and lands on all 198 pages.

**Metric.** Retention (extra hops), SEO (crawl depth and internal PageRank flow), acquisition
(footer newsletter field).

---

## FINDING 8 — No sequential "next / previous" within any collection

**Problem.** Nothing lets a reader walk a set. On a match page there is no "next 5-star classic". On
a profile, no "next wrestler". On an event, no "next event chronologically". The `07` Keep-going
recipe mentions "the rematch / next chapter" but the live pages have none of it. Sequential browsing
is one of the strongest low-effort continuation hooks (the "keep pressing next" reflex).

**Fix.** Add a prev/next pager to entity templates: previous/next wrestler (alphabetical or by
popularity), previous/next event (chronological), previous/next 5-star match (by rating rank). Two
linked `<a>` at the top of the Keep-going block.

**Buildability.** Static. The build script knows the full ordered list of each type, so it can emit
the two neighbor links per page at build time. No backend.

**Source.** Letterboxd, Genius, and album/film databases all offer chronological or ranked prev/next
to enable "just one more" traversal. The mechanic is cheap and habit-forming.

**Metric.** Retention (pages/session), engagement.

---

## FINDING 9 — Link previews on hover would turn dense prose into a rabbit hole

**Problem.** Profiles and moments are link-rich in prose (Kane's bio, the Mankind moment body), but
each link is a blind commitment: click and leave the page you are reading, or do not click. There is
no way to peek. Wikipedia found this was the exact friction that stopped people from going deeper,
and shipped hover page previews specifically to increase link-following without full navigation
(https://diff.wikimedia.org/2018/04/18/how-we-designed-page-previews-for-wikipedia/).

**Fix.** On desktop hover of any internal entity link, show a small card: name, promotion chip, one
verified fact, rating if a match. Data comes from the same `/data/graph.json` the `07` referrer
strip already needs. On mobile it degrades to nothing (tap navigates as normal).

**Buildability.** Static. One JS module plus the graph JSON build artifact. No backend. Honors
reduced-motion and fine-pointer gates already established in `enhance.js`.

**Source.** Wikipedia Page Previews, built explicitly to reduce rabbit-hole friction and keep
readers moving through the link graph
(https://wikimediafoundation.org/news/2018/04/18/how-we-designed-page-previews-for-wikipedia/).

**Metric.** Engagement (link CTR, dwell) and retention.

---

## FINDING 10 — Fabricated social proof and mismatched stats are a trust liability

**Problem.** Two honesty problems undercut the trust that a database brand depends on:

1. The waitlist note (`/index.html` line ~254) states "Join **12,840** fans on the waitlist" as a
   hardcoded number on a portfolio site with no waitlist. That is invented social proof. For a
   project whose pitch is a *credible* database, a fake counter is a self-own the moment anyone
   scrutinizes it.
2. The `.stats-bar` says "41+ Wrestlers" (line ~163) while the project state claims 89 profiles.
   The homepage undersells its own catalogue and the numbers do not agree with reality.

`07` §11 explicitly bans invented counts ("no invented counts... no 'X people viewing now' style
fake signals"). The homepage violates the site's own honesty rule.

**Fix.** Replace the fabricated waitlist count with either a real number once one exists, or honest
copy with no number ("Join the Rewind. One email a week."). Correct the stats-bar counts to the
true catalogue size and wire them to build-generated counts so they never drift again.

**Buildability.** Static. The build script counts files per directory and injects the real numbers
into `data-count`. This also future-proofs the stats bar as content grows.

**Source.** `07-addictive-browsing.md` §4.5 and §11 (the honest-trending / no-invented-counts rule)
— the site's own spec is the authority here.

**Metric.** Trust (and by extension conversion; fake proof that gets noticed poisons the actual
ask). For a job-portfolio piece aimed at a membership-growth role, shipping fabricated growth
numbers is the worst possible tell.

---

## FINDING 11 — The moment/match "Related" block is an ad-hoc list, not the typed spine the spec designed

**Problem.** The moment page uses `<h2>Related</h2>` + `.related-links` with only the two wrestlers
in it (`/moments/.../index.html` lines ~140-143). The CM Punk match uses the same generic
`<h2>Related</h2>` + `.related-links`. These are the "current ad-hoc" blocks `07` §4.1 explicitly
says to *replace* with the typed, slotted Keep-going block. So even the pages that have *something*
are running the version the spec deprecated: no forward/backward/sideways typing, no rivalry, no
event, no "more moments", no leaderboard. A moment page about the most famous bump in history does
not link to the match it happened in, the event, other Hell in a Cell moments, or `/moments/`.

**Fix.** Swap every `.related-links` block for the `07` §4.1 `.keepgoing` component with typed slots
filled from front-matter, and add the "More moments" rail (`07` §5 moment recipe). Ensure the moment
links to its parent match/event and to `/moments/`.

**Buildability.** Static. Build-script template swap plus CSS already specified in `07` §4.1. No
backend.

**Source.** `07-addictive-browsing.md` §4.1 (your own deprecation of exactly this pattern).

**Metric.** Retention, crawl depth.

---

## Priority order (build sequence)

1. **Fat footer (Finding 7)** — one shell edit, lands on all 198 pages, immediate crawl + hop win.
2. **Keep-going block + rails on the profile template (Finding 1)** — kills the flagship dead-end;
   propagates to ~89 profiles via the build script.
3. **Adopt localStorage (Finding 4)** — unlocks 3, 5, 6; ~one small JS module.
4. **Contextual email capture on all entity pages (Finding 2)** — fixes the single-point-of-failure
   funnel.
5. **Working rate loop (Finding 3)** + **On This Day / countdown (Finding 5)** — the return hooks.
6. **⌘K empty/zero states (6), prev-next pager (8), hover previews (9), typed Related (11)** — the
   polish layer.
7. **Fix fabricated stats (Finding 10)** — do this before any external eyes; it is a five-minute
   trust fix.

The throughline: you already designed the retention system in `07-addictive-browsing.md`. The gap is
not vision, it is that the build scripts stamped the pre-spec templates. Almost every fix above is
"run the spec through the build script", plus one architectural decision (allow localStorage) that
the spec talked itself out of.

---

## Backend-flagged items (everything else is static/no-build)

- Community-aggregated ratings ("4.8 from 2,314 fans"), Finding 3 Tier 2 — needs a datastore.
- Real double-opt-in email + founding-member badge issuance, Finding 2 — needs an ESP form endpoint
  (still no server you host).

Everything else in this document ships on the static, no-build, fully crawlable site as it stands.

---

### Sources

- IMDb recommendations / knowledge-graph node model: https://help.imdb.com/article/imdb/discover-watch/recommended-for-you-faqs/GPZ2RSPB3CPVL86Z ; https://aws.amazon.com/blogs/machine-learning/part-1-power-recommendation-and-search-using-an-imdb-knowledge-graph/
- Letterboxd rate-first loop / personalization drives loyalty: https://letterboxd.com/about/faq/ ; https://loyaltyrewardco.com/letterboxd-does-personalisation-drive-loyalty/
- Wikipedia page previews (rabbit-hole friction): https://diff.wikimedia.org/2018/04/18/how-we-designed-page-previews-for-wikipedia/ ; https://wikimediafoundation.org/news/2018/04/18/how-we-designed-page-previews-for-wikipedia/
- Duolingo streak / loss aversion: https://www.justanotherpm.com/blog/the-psychology-behind-duolingos-streak-feature ; https://apptitude.io/blog/how-duolingos-streak-mechanic-actually-works/
- "On This Day" sports-history daily hook: https://en.wikipedia.org/wiki/Baseball_Reference ; https://allsportshistory.com/category/on-this-day-in-sports-history/
