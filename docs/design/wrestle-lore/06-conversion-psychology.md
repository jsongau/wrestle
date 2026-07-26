# Wrestle Lore — Conversion Psychology & Membership Funnel Spec

Role: conversion psychology strategist. Goal: design the membership and lead funnel for Wrestle Lore
**without a loud nav CTA** (the user removed "Join MAT Insider" from the bar), using real behavioral
principles, tied to a static, no-build, fully crawlable, no-browser-storage site. Every feature below is
mapped to a funnel job (acquisition, engagement, capture, conversion, retention, trust, revenue) and to
a link target that already exists or is flagged `GAP`. No fabricated facts, quotes, or stats; illustrative
placeholders are flagged `VERIFY`.

- Date: 2026-07-26
- Builds on: `00-content-data-research.md`, `01-inspiration-research.md`, `02-homepage-architecture.md`, existing `/membership/` page, `css/site.css` tokens, `js/main.js` (in-memory only).
- Copy standard: no decorative arrows in CTAs, no em-dash sentence separators, no cliche marketing words, specific nouns.

---

## 0. Core thesis: the funnel IS the internal-link graph

Wrestle Lore's retention engine (the "Keep going" block, themed rails, hub-and-spoke linking from
`01-inspiration-research.md`) and its conversion funnel are the **same structure viewed twice**. Deep
sessions are the leading indicator of signup; the rabbit hole that serves SEO/GEO also serves conversion.
So the funnel does not fight the browsing experience or interrupt it with a loud bar CTA. It rides the
existing discovery surfaces and escalates the ask only as measured intent rises.

Intent ladder (each rung is a real surface defined below):
1. Anonymous reader lands on an entity page from search or an AI answer engine (acquisition).
2. Reader follows rails and "Keep going" links (engagement, session depth).
3. Reader hits a piece of gated premium value or a soft inline nudge (capture opportunity).
4. Reader gives an email to become a free Insider (capture, micro-commitment).
5. Insider gets recurring value and event-tied pushes, then upgrades to paid Ringside (conversion, revenue).
6. Member renews via drops, watch-alongs, and completion loops (retention).

---

## 1. The no-loud-nav-CTA decision (reconciliation)

The header keeps five content tabs plus `⌘K` search and **no red "Join" pill**. This supersedes the
header CTA still shown in `02-homepage-architecture.md` (rows 13/14 of its clickable table) and the loud
`.nav__cta` red pill in `css/site.css`. Rationale and where the ask moves instead:

- A persistent loud CTA in the bar is low-trust and low-yield on a database site; it reads as "product,"
  not "reference," and depresses the very session depth that predicts signup. Removing it raises perceived
  editorial credibility (trust) with near-zero capture cost, because capture moves to higher-intent moments.
- Membership stays reachable for crawlers and humans through a **quiet text link "Insider" inside the
  "More" dropdown**, the ambient **footer join line**, and the in-content moments in Section 3. All are
  raw-HTML `<a href="/membership/">`, so crawlability is preserved.
- Net effect: fewer, better-timed asks. The bar signals "trusted catalog"; conversion happens where
  interest is already demonstrated.

CSS change: retire `.nav__cta` from the bar (keep the class for reuse on in-content bands). Nav ends at
the `⌘K` search trigger.

---

## 2. Principles applied (and the ethical guardrails)

| Principle | How Wrestle Lore uses it | Guardrail (ethical / anti-cliche) |
|---|---|---|
| **Reciprocity** | The entire crawlable database, full wrestler profiles, and the visible editorial star rating are free and ungated. The ask comes only after value is delivered. | The core facts and ratings stay in raw HTML (SEO value + genuine gift). We never blur the fact a crawler needs. |
| **Curiosity gap / Zeigarnik** | Gated surfaces are the *secondary* layers a fan wants next: the classic-match archive, deep-dive breakdowns, "rate and save your own," the Sunday Rewind. | We tease real, existing value, not vaporware. Locked items name exactly what is inside. |
| **Commitment / consistency** | Micro-commitment first: one tap to pick a favorite promotion pre-segments and shrinks the form. A small yes precedes the email yes. | Optional, never blocks reading. No pre-checked consent. |
| **IKEA effect / endowment** | "Save your own star ratings" makes the member a co-author; saved ratings raise switching cost and return visits. | Requires an account by design; we say so plainly. |
| **Social proof** | Real catalog scale (169 pages, 89 profiles, 30 rated matches), cited community and editorial ratings labeled as which is which, and a methodology page. | No fake live counters, no invented member counts. See `VERIFY` items in Section 8. |
| **Authority / trust** | Visible methodology, source citations, the "not affiliated" disclaimer, honest pricing note. | Trust copy stays muted, never salesy. |
| **Loss aversion** | Founding-member framing and event-tied windows use scarcity that is *real* (a launch cohort that will actually close), not a fake ticking clock. | If a scarcity claim can't be honored, it is cut. Flagged `VERIFY`. |
| **Peak-end / completion** | Hubs end with "You've reached the end of WCW events" and collection checklists; the end of a satisfying session is exactly where the softest ask sits. | The ask is a single line, not a wall. |

---

## 3. Conversion moments (the interaction layers)

Six layers, escalating with intent. Each names its component, trigger, copy, color rule, and funnel job.
No layer blocks reading; none uses browser storage except in-memory within a single pageview.

### Layer 0 — Ambient (every page, lowest intensity)
- **Footer join line** (`.footer-join`, new): one muted sentence with a gold text link. Copy: "Wrestle
  Lore is free to read. Insiders also get the classic-match archive and the Sunday Rewind. Join free."
  Link "Join free" → `/membership/`.
- **"Keep going" block** (`.keep-going`, mandatory, from `02`): 4 to 6 contextual next links. Pure
  retention/SEO; not a sales ask, but it is what makes Layers 2 and 4 land because it deepens the session.
- Color: muted text, single gold link. No band, no box. Job: acquisition-to-engagement handoff, trust.

### Layer 1 — Inline value nudge (entity pages, contextual)
- **Component** `.join-inline` (new; visually a lighter `.answer`: `var(--c-gold-tint)` fill, 3px gold
  left rule, one line of text plus one link). Appears **once** per long entity page, after the primary
  content and before the rail, only where it is contextually true.
- Examples (copy is specific to the page, no arrows, no em-dash):
  - On a rated match page: "This match is one of 30 we star-rate in full. Insiders open the classic-match
    archive and can save their own ratings. Join free." → `/membership/`.
  - On a wrestler page with title history: "Track every reign and save your own verdicts as an Insider.
    Join free." → `/membership/`.
- Color: gold tint (premium, not alarm). Job: capture, curiosity gap, reciprocity payoff.

### Layer 2 — End-of-rail endcap (discovery surfaces)
- **Component** `.rail-endcap` (new): the final tile in a themed horizontal rail is a soft join card
  sized like a poster tile, so it reads as part of the wall, not an interruption. Copy: "Save this rail.
  Insiders get the full archive and weekly picks. Join free." → `/membership/`.
- Frequency rule: at most one endcap per page, only on the primary rail, never on the "Keep going" block.
- Color: gold hairline on `--c-bg-elev-1`; no red. Job: capture at the moment of demonstrated browsing
  velocity (the strongest static proxy for intent).

### Layer 3 — Gated premium value (the reciprocity gate, done ethically)
- **What is gated:** the classic-match archive index behind `/membership/`, deep-dive breakdown bodies,
  "rate and save your own," and the Sunday Rewind. **What is never gated:** every current entity page,
  the visible editorial star rating, and all facts a crawler or AI answer engine needs. This protects SEO
  and keeps the free gift genuine (no cloaking, no blurred facts).
- **Component** `.unlock` (new): an archive or deep-dive teaser card showing the real title, one factual
  line, and a lock chip. Copy: "Open the classic-match archive. Free with Insider." → `/membership/`.
  It shows what is inside; it does not hide a fact that already exists elsewhere on the site.
- Color: gold lock chip, gold link. Job: capture + conversion, curiosity gap, reciprocity.

### Layer 4 — Exit-intent (high-intent pages only, in-memory)
- **Component** `.exit-modal` (new `<dialog>`): triggers on desktop pointer-leave toward the tab bar and,
  on mobile, on a fast upward scroll past 70% of a long page. Copy: "Before you go: the 5-star match
  archive and the Sunday Rewind are free with Insider. Join free." Primary link → `/membership/`; a plain
  "No thanks" closes it.
- **Storage constraint (real):** the site uses no browser storage (`js/main.js` is in-memory only), so a
  dismissal cannot persist across pages or sessions. To avoid nagging, restrict this modal to a **small
  allowlist of high-intent pages** (the membership page's own related content, the top-rated-matches
  leaderboard, and the Hall of Fame hub), fire **once per pageview** via an in-memory flag, and never on
  first paint. This is the ethical version: it appears where interest is already high and cannot follow a
  user around. Flagged as a deliberate constraint, not a defect.
- Color: gold primary link, muted dismiss. Job: capture recovery, loss aversion (kept honest).

### Layer 5 — Event-tied, time-bound capture (the only place red is allowed)
- **Component** `.watchalong-cta` (new; red accent, `--c-live`): on PPV/PLE event pages, a band offering
  a live watch-along and a results push for that specific dated event. Copy on `royal-rumble-2026`:
  "Rumble night is live. Insiders get the watch-along and instant results. Join free." → `/membership/`.
- Scarcity is real here because the event has a real date; the urgency is not manufactured. After the
  event date passes, the band swaps to evergreen: "Get next event's watch-along. Join free."
- Color: red left rule + red link (time-bound urgency). This is the single context where red signals
  "now"; everywhere else membership is gold. Job: conversion + retention, ethical scarcity.

### Layer 6 — The membership page itself (`/membership/`, the dedicated close)
- Keep the existing structure: hero, three tiers (`.tiers`), the waitlist capture (`.waitlist-cta`), the
  six-stage funnel explainer, and the FAQ. Refinements in Section 5.

---

## 4. Color and shape rules for conversion surfaces

One rule keeps CTAs unambiguous across a site that already uses six promotion accents for content:

- **Gold** = membership, premium, and value (aspirational). Default for every join affordance.
- **Red** = live, dated, time-bound only (Layer 5 event watch-alongs, live badges). Never on evergreen
  join asks. This is why the nav pill (evergreen, red) was wrong and is removed.
- **Muted text** = trust, legal, disclaimers, and the ambient footer line.
- **Promotion accents** (WWE #c8102e, WCW #e2b13c, ECW #b0b0b0, TNA #1e73be, NXT #f5c518, NJPW `VERIFY`
  red) = content classification only, never a CTA fill. This prevents a join button from ever colliding
  in meaning with a promotion badge.
- **Shape:** join asks are pill links or gold-tint bands; content badges are chips/tags. Color plus shape
  together means a user never confuses "buy" with "browse."

Reuse existing tokens only: `--c-gold`, `--c-gold-bright`, `--c-gold-tint`, `--shadow-gold`, `--c-red`,
`--c-live`, `--c-text-muted`. New components add no new colors.

---

## 5. Membership page refinements (`/membership/`)

Keep the tiers and lifecycle explainer; fix trust and copy problems.

- **Rename** all "MAT" to "Wrestle Lore" (title, meta, OG, JSON-LD `name`, body copy). Current page still
  says "MAT Insider" and "wrestlelore.com" canonical. `GAP` until renamed.
- **Replace fabricated stats.** The waitlist band currently shows "12,840 on the waitlist" and "38%
  waitlist-to-member" and "4 lifecycle emails" as if real. Replace social proof with **real catalog
  scale** the site can stand behind: "89 wrestler profiles. 30 matches rated in full. 15 rivalries
  mapped." Keep the funnel-target numbers only inside the growth-strategy page, clearly labeled "target,"
  not on the capture form. Flagged `VERIFY` (see Section 8).
- **Micro-commitment first.** Keep the "favorite promotion" selector but present it as the first, lowest
  friction step (one tap) that pre-segments the lifecycle, then reveal the email field. Add NJPW to the
  promotion options (currently WWE/WCW/ECW/TNA/NXT). Commitment principle; also improves segmentation the
  role would report on.
- **Tier copy** stays: Fan $0, Insider $0 (free to join, email capture, "most popular"), Ringside $6/mo.
  Keep the honest "Pricing shown is illustrative for this prototype" disclaimer in the footer.
- **CTA copy** with no arrows: "Join free," "Go Ringside," "Browse free." Remove the "Full growth
  strategy →" arrow; use "Read the full growth strategy" as a text link.
- **FAQ + FAQPage JSON-LD:** rename to Wrestle Lore; keep "Is it free?" and "Can I cancel?"; add "What do
  Insiders get that readers don't?" answered with the real gated list (archive, save-your-ratings, Rewind).

---

## 6. Funnel job mapping (every feature to a growth outcome)

| Surface / feature | Acquisition | Engagement | Capture | Conversion | Retention | Trust | Revenue |
|---|---|---|---|---|---|---|---|
| Crawlable entity pages + JSON-LD + answer-first blocks | ● | ● | | | | ● | |
| "Keep going" block + themed rails (Layer 0/2) | ● | ● | ○ | | ● | | |
| Footer join line (Layer 0) | | | ○ | | | ● | |
| Inline value nudge `.join-inline` (Layer 1) | | ○ | ● | ○ | | | |
| Rail endcap `.rail-endcap` (Layer 2) | | ○ | ● | | | | |
| Gated archive / deep-dives `.unlock` (Layer 3) | | | ● | ● | ● | | ○ |
| Exit-intent modal (Layer 4, allowlist) | | | ● | ○ | | | |
| Event watch-along `.watchalong-cta` (Layer 5) | | ○ | ● | ● | ● | | ● |
| Membership page tiers + waitlist (Layer 6) | | | ● | ● | | ● | ● |
| Save-your-own ratings (IKEA/endowment) | | ● | | ○ | ● | | |
| Sunday Rewind newsletter | | | | ○ | ● | | ○ |
| Ringside drops + watch-alongs | | | | | ● | | ● |
| Methodology + citations + disclaimer | | | | | | ● | |

● primary job, ○ secondary.

---

## 7. Table of every conversion clickable → link target

Every join/capture clickable across the site, its component, copy (anti-cliche, no arrows), target, funnel
stage, and status. Content rails and "Keep going" links are specified in `02-homepage-architecture.md`;
this table is the **conversion** clickables only.

| # | Surface / component | Copy | Target | Funnel stage | Status |
|---|---|---|---|---|---|
| 1 | Nav "More" dropdown, quiet text item | Insider | `/membership/` | Capture | real (link exists) |
| 2 | Footer join line `.footer-join` (all pages) | Join free | `/membership/` | Capture | real |
| 3 | Inline nudge `.join-inline` (match pages) | Join free | `/membership/` | Capture | real |
| 4 | Inline nudge `.join-inline` (wrestler pages) | Join free | `/membership/` | Capture | real |
| 5 | Rail endcap `.rail-endcap` (primary rail) | Join free | `/membership/` | Capture | real |
| 6 | Gated archive teaser `.unlock` | Open the classic-match archive. Free with Insider | `/membership/` | Capture / Conversion | archive index `GAP` |
| 7 | Gated deep-dive teaser `.unlock` | Read the full breakdown. Free with Insider | `/membership/` | Capture | deep-dive pages `GAP` |
| 8 | Exit-intent modal primary (allowlist pages) | Join free | `/membership/` | Capture | real |
| 9 | Exit-intent modal dismiss | No thanks | (closes dialog) | none | real |
| 10 | Event watch-along band `.watchalong-cta` | Join free | `/membership/` | Conversion / Retention | real |
| 11 | Membership hero primary | Join free | `#join` (waitlist anchor) | Capture | real |
| 12 | Tier: Fan | Browse free | `/` | Acquisition | real |
| 13 | Tier: Insider (featured) | Join free | `#join` | Capture | real |
| 14 | Tier: Ringside | Go Ringside | `#join` | Revenue | real |
| 15 | Waitlist form submit `.waitlist-cta` | Join the waitlist | `data-waitlist` handler (mock) | Capture | real (mock) |
| 16 | Funnel explainer link | Read the full growth strategy | `/membership/growth-strategy/` | Trust | real |
| 17 | FAQ answer, China data | 中文 page | `/zh/` | Trust | real |
| 18 | Methodology reference (from `.join-inline` trust line) | How we rate matches | `/methodology/` | Trust | real (exists) |
| 19 | Leaderboard endcap (top-matches page) | Join free | `/membership/` | Capture | `/rankings/` exists; per-list `GAP` |
| 20 | Hall of Fame hub inline nudge | Join free | `/membership/` | Capture | `/hall-of-fame/` `GAP` |

Destinations that must exist so no conversion clickable 404s: `/membership/` (exists, needs rename),
`/membership/growth-strategy/` (exists), `/methodology/` (exists), `/zh/` (exists), `/rankings/` (exists).
`GAP`: the gated **classic-match archive index**, **deep-dive breakdown** pages, the **Hall of Fame hub**,
and per-list **leaderboard** pages. Until built, Layer 3 links point to `/membership/` (the tier list
already describes the archive), so nothing dead-ends.

---

## 8. VERIFY / do-not-fabricate flags

- `12,840 on the waitlist`, `38% waitlist-to-member`, `4 lifecycle emails` on the current membership
  waitlist band are **fabricated placeholders**. Replace with real catalog scale (89 profiles, 30 rated
  matches, 15 rivalries) for social proof; keep target metrics only in the growth-strategy page labeled
  "target." `VERIFY` before publish.
- `Founding-member badge` and any "first N members" scarcity: only publish if the launch program will
  actually honor it. Frame as illustrative for the prototype (matches existing footer disclaimer). `VERIFY`.
- `Ringside $6/month` pricing: illustrative; keep the existing "Pricing shown is illustrative for this
  prototype" disclaimer. `VERIFY` before any real launch.
- NJPW accent red for any promotion badge near a CTA: confirm the brand red before locking (`00` §4).
- No invented quotes from Chris Van Vliet or any media personality on capture surfaces.

---

## 9. Why this demonstrates membership-growth skill for the WWE / TKO application

- **Full-funnel ownership, not just a signup form.** The spec maps acquisition (crawlable + GEO), through
  engagement (session depth as the leading indicator), capture, free-to-paid conversion, and retention
  (event-tied drops and watch-alongs), which is exactly the WWE Manager, Membership Growth remit across a
  network like WWE's own PLE and streaming lifecycle.
- **Timing over volume.** Removing the loud nav CTA and escalating the ask by measured intent is the
  judgment a growth owner is hired for: it trades a vanity impression for higher-quality, better-timed
  capture, and it protects the reference-site trust that drives the traffic in the first place.
- **Event-tied lifecycle.** Layer 5 mirrors how WWE monetizes a live calendar (Royal Rumble, WrestleMania,
  SummerSlam): capture and retain around real dated moments, then convert to recurring access. Honest
  scarcity anchored to a real event date is the ethical, on-brand version.
- **Measurable and honest.** The funnel is instrumented in the growth-strategy page (waitlist growth, CTR,
  LP conversion, paid conversion, retention), and every social-proof number is real or flagged, which is
  the trust posture a membership brand and a serious hiring panel both require.

---

## 10. Build checklist (for the implementer)

1. Remove `.nav__cta` red pill from the bar in every page template; add a quiet "Insider" text link inside
   the "More" dropdown.
2. Add CSS components: `.footer-join`, `.join-inline`, `.rail-endcap`, `.unlock`, `.exit-modal`,
   `.watchalong-cta` (all use existing tokens; gold for evergreen, red only for `.watchalong-cta`).
3. Add an in-memory exit-intent handler to `js/main.js`, gated to the allowlist of high-intent pages,
   once per pageview, no storage.
4. Rename `/membership/` to Wrestle Lore; replace fabricated stats with real catalog scale; add NJPW to
   the promotion selector; strip arrows from CTA copy; add the third FAQ entry and mirror it in JSON-LD.
5. Place one `.join-inline` per long entity page, one `.rail-endcap` on the primary rail, the footer join
   line site-wide, and `.watchalong-cta` on PPV event pages.
6. Point all Layer 3 `.unlock` links to `/membership/` until the archive/deep-dive/HOF/leaderboard `GAP`
   pages exist, so nothing 404s.
