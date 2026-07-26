# Wrestle Lore — Vision Spec F: Growth & Monetization

Role: growth and monetization futurist. This spec turns the database into a membership-growth engine
and a set of revenue lines that a WWE / TKO manager, Membership Growth, would recognize as their own
day job. It sits on top of, and cross-links into, the existing pages and the sibling vision specs.

- Written: 2026-07-26
- Scope: revenue + membership only. The community/UGC funnel and badges are owned by
  `vision/D-community-gamification.md`; the interactive tools are owned by `vision/B-interactive-tools.md`;
  the data graph is owned by `vision/C-data-graph-discovery.md`. This spec references them, it does not
  re-specify them.
- What already exists to build on: `/membership/` (Fan $0, Insider $0 free-to-join, Ringside $6/mo),
  `/membership/growth-strategy/` (funnel, lifecycle, weekly readout), and real outbound "where to watch"
  links on every event page (`.watch2__card`, ESPN + Netflix). Those three are the seeds for everything below.
- Confidence: `HIGH` = ships today on the static stack; `BACKEND` = needs a service (flagged inline);
  `VERIFY` = a business/legal fact to confirm before publishing (affiliate terms, partner deals).

---

## 0. The one-line pitch to the hiring manager

Wrestle Lore is a membership funnel disguised as the best wrestling database on the web. Free crawlable
content wins the search and AI-citation top of funnel, the "where to watch" badges convert intent to
streaming partners at the exact moment a fan decides to watch, and the Insider tier turns repeat rabbit-hole
sessions into a logged-in relationship. Every idea below is scored on the five levers a growth manager
reports on: acquisition, retention, engagement, trust, revenue.

Five revenue lines, ranked by how fast they ship and how clearly they prove the job:

1. Streaming affiliate on the "where to watch" badges (ships today, zero backend).
2. Insider / Ringside membership with gated depth (partly live, clear upgrade path).
3. Event-surge lifecycle campaigns around PLEs (ships today as static, email needs a service).
4. Creator and influencer partnerships routed through the media tab (ships today, revenue when signed).
5. Data and API licensing of the ratings + lineage + graph dataset (backend, highest ceiling).

---

## 1. Streaming affiliate layer — the "where to watch" badge becomes a revenue channel

The badges already exist and already link out. Right now they are plain hrefs to `espn.com/wwe/` and
Netflix. Turning them into a tracked affiliate surface is the single highest-leverage revenue move on the
site because it monetizes the moment of highest intent, the second a fan decides to watch, without asking
for money or a login.

- New hub: `/watch/` — a master "where to watch wrestling in 2026" page. One row per promotion, each with
  the platform chips from `00-content-data-research.md` section 1 (Netflix, ESPN, USA Network, The CW,
  HBO Max, NJPW World, TNA+, AMC, Prime Video), US vs International labeled. This is a top-tier SEO page:
  "where to watch [promotion]" and "how to watch WWE PLEs" are high, recurring, commercial-intent queries.
- New spokes: `/watch/wwe/`, `/watch/aew/`, `/watch/njpw/`, `/watch/tna/`, one per promotion, each the
  canonical answer page for that promotion's viewing options.
- Existing surfaces to upgrade: the `.watch2__card` block on all five 2026 event pages
  (`/events/wrestlemania-42-2026/`, `/events/royal-rumble-2026/`, `/events/backlash-2026/`,
  `/events/elimination-chamber-2026/`, `/events/night-of-champions-2026/`) and the promotion pages under
  `/promotions/`. Every existing badge gets the affiliate wrap and a `rel="sponsored nofollow"` attribute.

Why it wins:
- Revenue: affiliate and partner-referral commissions on subscriptions and PPV buys, captured at peak
  intent. This is the cleanest recurring revenue on a static site.
- Acquisition and trust: an honest, well-sourced "where to watch" answer is exactly what search engines
  and AI answer engines cite, which pulls free traffic that funnels into membership.
- It proves the job: it is literally a partner-monetization channel tied to the streaming rights map
  (ESPN, Netflix) that the WWE/TKO business now runs on.

Buildability: `HIGH` for the pages and the affiliate links (static hrefs, a per-partner tracking
parameter appended to the URL). Click-through and conversion measurement is `BACKEND` (a redirect
endpoint like `/go/{partner}/` or a partner dashboard); until then, use each partner's own affiliate
dashboard, no first-party service required. `VERIFY`: which partners run affiliate programs and their
terms (Amazon Associates covers Prime Video library seasons; ESPN, Netflix, HBO Max, NJPW World, TNA+
programs must be confirmed, some route through networks like Impact or CJ).

Cross-links: `/watch/` links to each `/promotions/{slug}/` and its top events; every event page's watch
card links to `/watch/{promotion}/`; `/watch/` is a natural footer link site-wide.

Anti-AI copy sample (badge): "Every WWE Premium Live Event streams live on ESPN in the US, and on Netflix
everywhere else. Raw is on Netflix. SmackDown airs Fridays on USA Network."

---

## 2. Membership architecture — from three tiers to a depth ladder

The tiers exist; the job is to give each tier a concrete reason to climb, and to gate depth rather than
gate the crawlable core (gating the core would kill the SEO/GEO engine that feeds the funnel). The rule:
everything a crawler and an AI answer engine should cite stays free and public; the paid value is depth,
speed, personalization, and status.

Proposed ladder (evolves the live `/membership/` page):

- Fan, $0, no account: the full crawlable database, forever. This is the acquisition and citation layer.
- Insider, $0, free account: the value is a saved identity across the no-login tools. Watchlist,
  saved dream-match cards (`vision/B`), personal ratings and reviews (`vision/D`), the weekly Rewind email,
  and Insider-only leaderboards. Route: `/insider/`. The account is the growth asset; the email is the
  retention channel.
- Ringside, $6/mo (already priced): ad-free, early access to new tools, the premium archive, watch-along
  hubs, member drops, and a Ringside badge on their reviews. Route stays `/membership/`.
- New top tier, Card Sub or Historian, ~$12/mo (`VERIFY` price against willingness to pay): everything in
  Ringside plus the full statistics vault, downloadable data exports, and an ad-free API key for personal
  use. Route: `/membership/#historian`. This tier is where the data-licensing product (section 5) meets
  the consumer.

New gated-depth surfaces (the carrot):
- `/vault/` — the premium statistics and archive layer. Free users see the top of every stats table and a
  clear "the full breakdown is in the Vault" line; members see the whole thing. Gating a table's tail, not
  its head, keeps the page crawlable and citable while creating a real upgrade reason.
- `/insider/rewind/` — the archive of the weekly Rewind newsletter, member-visible, each issue also a
  standalone SEO page (a back-issue archive ranks and re-sells the newsletter).

Why it wins:
- Retention and revenue: a free account is the highest-value conversion on the site because it turns an
  anonymous rabbit-hole session into a re-marketable relationship, which is the entire premise of a
  membership-growth role.
- Trust: never paywalling the facts keeps the citation engine intact, so paid conversion never cannibalizes
  free acquisition.

Buildability: the tier pages, copy, and the "top of table free, tail gated" pattern are `HIGH` as static
markup. Actual auth, saved state, gated rendering, and billing are `BACKEND` (Supabase auth + Stripe, the
same Supabase phase 2 that `vision/D` already scopes; share that one backend, do not stand up a second).

Cross-links: `/vault/` links from every stats block; `/insider/` links from the tools in `vision/B`;
`/membership/growth-strategy/` should reference this ladder as the funnel's product spine.

---

## 3. Event-surge lifecycle campaigns — monetize the PLE calendar

Wrestling traffic is spiky and predictable. A PLE weekend is a demand surge you can see coming a month
out. A membership-growth manager's core skill is running a lifecycle campaign against a known event, so
this section is the clearest on-the-job proof in the spec.

New per-event surge surfaces (built once, reused every event via the same template):
- `/events/{event}/preview/` — the pre-show hub: card, predictions widget (`vision/B` bracket/prediction
  tool), and the "where to watch" affiliate card (section 1) placed at the top when intent peaks. This page
  captures the search surge for "[event] card" and "[event] start time" and converts it two ways: an
  affiliate click to the stream, or an email capture to get the results recap.
- `/events/{event}/live/` — a lightweight live hub during the show (static, hand-updated or a simple
  results feed), the single URL fans keep open. High return-visit frequency during the window.
- `/events/{event}/results/` — the morning-after recap and re-rate, the retention payoff, and an SEO
  evergreen ("who won at [event]"). The existing 2026 event results pages already do this; formalize it as
  the campaign's closing step.

The campaign arc, mapped to the levers:
1. T-minus 3 weeks: preview page goes live, prediction tool opens, "get the recap" email capture opens
   (acquisition).
2. Event weekend: watch card and affiliate links at the top of the preview and live hub (revenue, at peak
   intent).
3. Show night: live hub keeps fans returning (engagement).
4. Morning after: results + re-rate email fires to everyone who predicted, with a Ringside upsell for the
   full ratings breakdown (retention + revenue).

Why it wins: it is a repeatable, measurable, event-triggered funnel, exactly the lifecycle-campaign work
the role is scored on, and it stacks affiliate revenue on top of membership conversion in the same window.

Buildability: all three page types are `HIGH` as static templates (the results type already exists). The
email capture, the scheduled sends, and the prediction-to-recap loop are `BACKEND` (an email service plus
the shared Supabase). `VERIFY`: which events are on the 2026 calendar and their real dates before building
preview pages (the base workflow owns the event facts).

Cross-links: each event's three-page arc links to `/watch/{promotion}/`, to the participating wrestler
profiles, to the rivalry hub, and to `/rankings/`; the recap links to `/membership/` for the upsell.

---

## 4. Creator and influencer partnerships — the media tab as a growth channel

The Media & Creators tab (`00-content-data-research.md` section 6, Chris Van Vliet as flagship) should be
built as an acquisition channel, not just a roster. A wrestling creator with an audience is a distribution
partner; the site gives them a reason to link back, and the backlink and the referred audience are the
payment.

New surfaces:
- `/creators/{slug}/` — a profile per media personality (Chris Van Vliet confirmed; others `VERIFY`), with
  their interview subjects cross-linked to those wrestlers' profiles. This makes the site the canonical
  index of who-interviewed-whom, which the creators themselves want to link to.
- `/lists/{creator-slug}/` — co-branded curated lists ("Chris Van Vliet's 10 favorite interviews", each
  entry linking to the wrestler and the match). A creator promoting their own list on their channel sends
  their audience straight into the rabbit hole. Lists are cheap to author (`vision/A` and `vision/D` both
  treat curated lists as a content type) and highly shareable.
- `/creators/embed/` — a documented set of embeddable static widgets (a rating badge, a "match of the
  night" card, a wrestler stat chip) that creators drop into their own sites and video descriptions. Every
  embed is a branded backlink and a referral path. Static, crawlable, and it turns partners into a free
  distribution network.
- A referral parameter (`?ref={creator}`) on shared links, so a creator's traffic and the memberships it
  drives are attributable. Attribution is what makes a partnership renewable.

Why it wins:
- Acquisition: creator backlinks and audience referrals are the cheapest high-quality traffic in wrestling
  media, and they compound SEO authority.
- Revenue and the job: an influencer/creator partner program with attribution and co-branded content is a
  named growth channel a WWE manager would run; building it here proves the skill directly.

Buildability: profile pages, lists, and embeds are `HIGH` (static HTML, the embed is a small self-contained
snippet). Referral attribution and any revenue-share payout are `BACKEND` (the `?ref` tag can be logged
via the same redirect endpoint as section 1). `VERIFY`: every creator's current affiliation and any
image/name usage rights before publishing; do not fabricate quotes.

Cross-links: `/creators/{slug}/` links to each wrestler they cover and back to `/wrestlers/`; `/lists/`
sits in the same list system as `vision/D`'s collections; embeds link home to the canonical entity page.

---

## 5. Data and API licensing — sell the structured asset

The site's real moat is the structured dataset: match ratings, title lineages, the relationship graph
(`vision/C`), and clean schema.org markup on every page. That dataset is exactly what other wrestling
media, fantasy apps, and AI answer engines need and cannot easily assemble. Licensing it is the highest
ceiling revenue line, and the GEO work already underway builds the asset for free.

New surfaces:
- `/data/` — a public, human-readable data catalog: what entities exist, what fields, update cadence,
  and a plain-language license summary. This page alone is a strong trust and authority signal.
- `/data/licensing/` — the commercial page: tiers for personal (free API key), commercial, and bulk/AI
  training use, with a contact/apply flow. `VERIFY` all pricing and license terms with a human before
  publishing.
- `/api/v1/` — a read API over the dataset. `BACKEND` (Supabase edge functions or a static JSON export
  served from `/data/entities.json`, the same `entities.json` that `vision/B` and `vision/C` already
  require; a static JSON dump is the zero-backend v1, a keyed API is v2).
- A downloadable dataset export gated behind the top membership tier (section 2), which is the consumer
  on-ramp to the licensing product.

Why it wins:
- Revenue: B2B licensing has the highest revenue-per-customer and does not depend on consumer traffic
  volume.
- Trust and GEO: publishing a clean, documented, citable dataset is the strongest possible signal to AI
  answer engines, which increases free citations, which increases the top of funnel. The same asset serves
  three goals: licensing revenue, AI citations, and the internal graph that powers retention.

Buildability: `/data/` and `/data/licensing/` are `HIGH` static pages. A static `entities.json` export is
`HIGH`. A keyed, metered API is `BACKEND`. Bulk/AI-training licensing is a `VERIFY` legal question first,
a product second.

Cross-links: `/data/` links from the footer and from `/methodology/` (the ratings source-of-truth page
already exists); the API docs link to the entity pages the data describes.

---

## 6. Drops and collectibles — sell the aesthetic

The poster-wall design is already a product. The duotone/scanline treatment on wrestler tiles is the exact
look that sells as a print, and a "drop" mechanic (limited, time-boxed) creates the return-visit urgency
that `01-inspiration-research.md` section B4 calls for, honestly, without fake counters.

New surfaces:
- `/drops/` — a hub for time-boxed member offers: a print of the month, a numbered digital collectible
  card for a signature match, an early-access tool. Ties to the Ringside tier's "member drops" benefit that
  the live `/membership/` page already promises.
- `/shop/` — print-on-demand posters and cards generated from the existing tile artwork.
  `BACKEND` via a print-on-demand partner (Printful/Gelato-style); the storefront page is static, the
  fulfillment is the partner's. `VERIFY`: every wrestler's name and likeness rights before selling any
  merchandise; this is a hard legal gate, flag it loudly.

Why it wins: revenue and retention (drops give members a recurring reason to return), and it extends the
brand's premium feel into a physical object. Lowest priority because the likeness-rights gate is real.

Buildability: hub and storefront pages `HIGH`; fulfillment `BACKEND` (partner); the whole line is `VERIFY`
on rights.

Cross-links: `/drops/` from `/membership/`; each drop links to the wrestler or match it celebrates.

---

## 7. Measurement — the weekly readout every idea reports into

Extend the existing `/membership/growth-strategy/` weekly readout so each revenue line above has a metric,
because a growth manager is hired to report numbers, not features:

- Streaming affiliate: clicks per platform, conversion, commission (from partner dashboards + the `/go/`
  redirect once built).
- Membership: free-account signups, Ringside conversion, churn, revenue per member.
- Event campaigns: preview-page traffic, email captures, affiliate clicks in the window, post-event
  upsell conversion.
- Creators: referred sessions and memberships by `?ref`, backlinks earned.
- Data/API: API keys issued, licensing inquiries, export downloads.

Buildability: the readout page is `HIGH` (static, hand-updated from dashboards). Automated dashboards are
`BACKEND`.

---

## Ranked build order (leverage vs effort)

1. Streaming affiliate wrap on existing badges + `/watch/` hub. Ships today, revenue today, feeds SEO.
2. Event-surge campaign template (`/events/{event}/preview|live|results`). Static now, proves the job.
3. Free-account Insider layer + `/vault/` gated-depth pattern. Static carrot now, backend later.
4. Creator program: `/creators/`, `/lists/{creator}/`, embeds, `?ref`. Static now, revenue when signed.
5. `/data/` + static `entities.json` export, then `/data/licensing/`. Highest ceiling, backend to scale.
6. `/drops/` + `/shop/`. Last, gated on likeness rights.

## Verification queue (business/legal, confirm before publishing)

- Affiliate program availability and terms for ESPN, Netflix, HBO Max, NJPW World, TNA+, Amazon Associates.
- Membership pricing for the proposed Historian tier.
- 2026 event calendar and dates for preview pages (owned by the base workflow).
- Every creator's current affiliation and name/image usage rights; no fabricated quotes.
- Name-and-likeness rights before any merchandise or paid collectible.
- Data license terms (personal / commercial / AI-training) with a human before the licensing page ships.

## Anti-AI copy standard applied

All sample copy above uses specific nouns (ESPN, Netflix, USA Network, NJPW World), no decorative arrows,
no em-dash separators, and none of the banned cliche words. Every "where to watch" and pricing claim
carries a source or a `VERIFY` flag rather than an invented number.
