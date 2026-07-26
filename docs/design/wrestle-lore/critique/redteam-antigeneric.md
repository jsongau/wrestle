# Red-Team Critique: "Wrestle Lore" reads AI-generated, and here's the proof

Adversarial review. No praise. Every claim is tied to a file/selector and a fix that ships on a
static, no-build, crawlable site. Copy rewrites obey the house standard (no decorative arrows, no
em-dash separators, no cliché banned words). Researched patterns are named with source and rationale.

Reviewed: `/index.html`, `/css/site.css`, `/wrestlers/kane/index.html` (the stated "gold standard"),
`/events/index.html`, `/moments/mankind-hell-in-a-cell-fall-1998/index.html`, `/js/nav.js`, `/js/main.js`,
plus greps across `/wrestlers/` (107 files) and `/matches/` (30 files).

---

## VERDICT

The homepage is a competent template. The moment you click into the actual database — the wrestler
profiles, which are 90% of the URLs and the whole reason the site exists — it falls apart. The
"gold-standard" Kane profile and 97 other wrestler pages are wired to a CSS vocabulary that **does not
exist in the stylesheet**, so they render as near-unstyled documents. On top of that, the 30 match
pages ship a **fabricated `AggregateRating` (9,640 ratings, 431 reviews) on a site that has zero users
and a pre-launch waitlist**. Those two facts alone would sink this in front of a WWE/TKO hiring panel:
the first says "we never opened the pages we're proudest of," the second says "we invent our own social
proof." The generic feel is real, but it is the *third* most important problem, not the first.

---

## PART A — THE KILL SHOTS (broken + trust-destroying; fix before anything cosmetic)

### A1. The "gold-standard" profile — and 97 others — are unstyled. The design system and the templates speak different languages.
**Evidence.** `/wrestlers/kane/index.html` loads only `/css/site.css` (line 9) and contains no inline
`<style>`. Its markup uses `athlete-hero`, `hero-inner`, `hero-sub`, `hero-desc`, `content-grid`,
`bio-col`, `stats-col`, `stat-card`, `stat-big`, `stat-num`, `stat-label`, `record-table`,
`record-filter`, `rf-btn`, `res-cell`, `res-badge`, `persona-card`, `sig-section`, `sig-grid`,
`sig-match`, `tl-year`, `faq-block`, `champ-row`, `cr-title`, `cr-reign`, `cr-note`, `mb-label`,
`mb-pct`, `wl-strip-wrap`. **A grep of `site.css` for every one of those returns zero matches.** The
stylesheet instead defines a *different* profile vocabulary: `.profile`, `.profile__photo`, `.facts`,
`table.record`, `.rt-filters`, `.rec-stat`, `.champ-rows > div` + `.k`, `.timeline` + `<time>`, `.faq`
+ `.faq__body`, `.persona`, `.mb-head`.
- Scope: `athlete-hero` appears in **98 wrestler files**; the real `.profile`/`.facts` classes appear in
  only **9** (the older alter-ego pages: `mean-mark-callous`, `stunning-steve-austin`,
  `the-american-badass`, `stone-cold-steve-austin`, `the-ringmaster`, plus `ricky-steamboat`,
  `vince-mcmahon`, `booker-t`, `chris-benoit`). So there are **two template generations**, and the newer
  bulk one — the one used for Kane, The Undertaker, Roman Reigns, AJ Styles, Ric Flair, John Cena, Cody
  Rhodes, every featured star linked from the mega-nav — is the broken one.
- Consequence: the two-column `content-grid` never becomes a grid (falls to block flow), `stat-card`
  panels have no background/border, `persona-card` and `sig-match` have no card treatment, and the
  finish-method bars are invisible: `.mb-fill` is set to `width:0` and only expands via
  `.is-in .mb-fill{width:var(--w)}` (site.css line 630-631), but Kane's bars sit in `.method-bars` with
  no `[data-reveal]`/`.is-in` ancestor, so they stay at 0%. The page is dark text-on-dark boxes with no
  hierarchy.
**Fix.** Pick ONE vocabulary and make the templates and CSS agree. Cheapest correct path: regenerate the
98 pages from the builder scripts (`build_wrestlers_7*.py`) using the classes that already exist in
`site.css` (`.profile`, `.facts`, `table.record`, `.rec-stat`, `.champ-rows`, `.timeline`, `.faq`,
`.persona`, `.mb-head`). Do NOT hand-add 30 aliasing rules to the CSS — that hides the divergence and
doubles the maintenance surface. Add a build-time assertion: after generating, grep each page for any
`class="..."` token not present in `site.css` and fail the build.
**Buildable?** Yes, pure static — it is a generator + CSS reconciliation, no backend.

### A2. Fabricated `AggregateRating` on all 30 match pages. This is the E-E-A-T landmine.
**Evidence.** `/matches/undertaker-vs-hbk-wm25/index.html` lines 40-48 ship a `Review` whose
`author` is the `Organization` "Wrestle Lore Editorial" and which embeds
`"aggregateRating":{"ratingValue":"4.9","ratingCount":"9640","reviewCount":"431"}`. Grep confirms the
same block on **all 30 match files**. The site's own Organization schema says `"foundingDate":"2026"`
(`/index.html` line 30) and the homepage asks people to *join a waitlist* — there is no logged-in user
base that could have produced 9,640 ratings. This is invented social proof.
- Three separate problems stacked: (1) the numbers are fabricated; (2) Google's structured-data policy
  disallows self-serving `AggregateRating` markup the site controls and can penalize/ignore it —
  exactly the "unverifiable claims" a red-team looks for; (3) it is internally inconsistent: the
  editorial `reviewRating` is 5.0 while the "aggregate" is 4.9, and `aggregateRating` is nested inside
  a single `Review` (schema-wrong; it belongs on the `itemReviewed`).
**Fix.** Delete `aggregateRating` from every match page now. Keep the single editorial `Review` but give
it a *named human* author (see B1), not a faceless Organization. Only reintroduce an aggregate when real
member votes exist, and when you do, render the count on-page from the same source of truth. Until then,
lead with the honest, defensible number you *can* cite: Meltzer's star rating and Cagematch's community
average — see the dual-score pattern in D2.
**Buildable?** Yes — a find/replace across 30 files plus a builder change.

### A3. Every "watch" button lies about what it does, and the JS that would make it true is dead.
**Evidence.** The homepage hero facade (`/index.html` lines 160-165) and every match facade
(`/matches/.../index.html` lines 182-190) use `onclick="window.open('https://www.youtube.com/results?
search_query=...')"` — they open a **YouTube search results page**, not a video. Yet the copy directly
under the WM25 player reads: *"Verified embed IDs (YouTube & Bilibili for China) drop straight into this
player."* (match file line 190). That is false. Meanwhile `main.js` lines 37-56 implement a real
click-to-load embed that reads `data-provider`/`data-id`/`data-bvid` — **no facade on any reviewed page
sets those attributes**, so that handler never fires. You shipped the honest mechanism and then bypassed
it with a search link plus a claim that the honest mechanism is running.
**Fix.** Either (a) populate `data-provider="youtube" data-id="…"` on each facade and delete the
`onclick`, letting `main.js` do the verified embed it was built for, or (b) if rights are unresolved,
change the button to a plain "Search on YouTube" outbound link and delete the "verified embed IDs" copy.
Do not claim a capability you disabled.
**Buildable?** Yes — the code already exists; wire the data attributes.

### A4. The record filter buttons on every profile are decorative — they filter nothing.
**Evidence.** Kane's match record (lines 200-206) renders `<div class="record-filter"
data-record-filter>` with `<button class="rf-btn" data-filter="ppv">` etc. `main.js` only binds to
`document.querySelectorAll('[data-filter]')` where the element is expected to be an **input** whose value
is read (`normalize(input.value)`, line 72) and whose rows are `[data-search]` items. The buttons are
`button` elements with `data-filter` used as a *category name*, targeting `[data-cats]` rows — a
contract that no code implements. Clicking "PPV/TV/Tag/Title" does nothing. (`.rf-btn` also has no CSS —
see A1.)
**Fix.** Add a small handler keyed on `[data-record-filter] .rf-btn[data-filter]` that toggles
`.record-row` visibility by matching the button's `data-filter` token against each row's `data-cats`,
updates `aria-pressed`, and shows a live count. ~20 lines, no deps.
**Buildable?** Yes — vanilla JS, matches the existing no-storage constraint.

---

## PART B — THE "AI-GENERATED / NO POINT OF VIEW" TELLS (why it feels generic)

### B1. There is no human anywhere. Faceless "Editorial" is the single biggest authority gap.
**Evidence.** Reviews are authored by `{"@type":"Organization","name":"Wrestle Lore Editorial"}`
(match file line 43). No byline, no author page, no credentials, no "who decides the rating." The
methodology is asserted in FAQ ("editorial score informed by critical consensus") but no person stands
behind it.
**Why it matters / research.** Every elite, trusted wrestling/sports outlet is built on *named humans*:
Dave Meltzer IS the Wrestling Observer; Defector's whole pitch is worker-owned, strongly bylined writers
with distinct voices ([Defector](https://defector.com/), [Albert Burneko on Defector's rise](https://medialyter.substack.com/p/albert-burneko-on-the-rise-of-defector)).
Google's E-E-A-T rewards identifiable expertise. A faceless org rating matches is the textbook
AI-slop signal.
**Fix.** Create 1-3 real reviewer identities with `/about/`-linked author pages (name, photo, one-line
wrestling bona fides, their all-time top five). Put a byline + date + "why I scored it this" note on
every match review. Change the schema `author` to `{"@type":"Person","name":"…","url":"/team/…/"}`.
**Buildable?** Yes — static author pages + a byline partial.

### B2. Safe, voiceless, cliché copy. The site describes wrestling instead of having an opinion about it.
**Evidence (with the house copy standard applied).** Section headings are interchangeable hype:
"The matches that defined an era" (index 214), "The legends who built it" (230), "Everything is
connected" (245), "Don't just watch. Remember." (291). The answer box (208) is a Wikipedia-neutral
definition. None of it says anything only a wrestling fan would say.
- The site also **violates its own copy rule**: em-dash-as-separator is everywhere, e.g. hero lede
  "modern professional wrestling — WWE, WCW, ECW, TNA and NXT, from the 1997 Monday Night Wars to today"
  (index 150) and the answer callout (208). If the standard bans it, the flagship page must obey it.
**Fix — replace descriptions with verdicts.** Give each rail a stance and a reason, no em-dash, no arrows:
  - Five-Star rail H2: "The 30 matches we'll die on a hill for" (was "The matches that defined an era").
  - Icons rail H2: "The 12 who actually moved the needle" (was "The legends who built it").
  - Relationships H2: "Wrestling is one family tree. We drew it." (was "Everything is connected").
  - Answer box, opinionated + still GEO-clean: "Wrestle Lore ranks and reviews modern pro wrestling from
    1997 on. We take a side on every match, we show our math, and we map how every wrestler connects to
    the next." (removes the em-dash and the neutral tone).
**Buildable?** Yes — copy edits.

### B3. Uniform spacing and one-note motion — the "stamped by a machine" rhythm.
**Evidence.** Every section is `.section{padding-block:var(--sp-8)}` (site.css 84), every content block
carries `data-reveal` with the identical `translateY(24px)/.7s` transition (site.css 394-395). Scrolling
the homepage is the same beat seven times. Real editorial pages vary density: a punchy stat strip, then a
dense table, then a full-bleed quote.
**Fix.** Introduce 2-3 rhythm variants: a full-bleed dark "pull-quote" band (a famous JR/Meltzer line),
a dense data section with tighter `--sp-6` padding, and stagger reveals with a small
`transition-delay` per child (`--i`). Vary, don't uniformly apply.
**Buildable?** Yes — CSS + a data attribute.

### B4. Monogram placeholders instead of faces = the clearest "it's a demo" signal.
**Evidence.** Every tile and profile uses a duotone gradient with one giant letter (`.tile__mono`,
`.profile__photo .pmono`, site.css 483-486, 650-651). 107 wrestler pages, zero photographs. Cagematch,
WWE.com and Letterboxd are *poster/photo-first*; the visual identity of a wrestler IS the product.
**Fix.** Even without licensed press photos, ship real silhouettes/entrance-pose PNGs or a consistent
illustrated set; at minimum add a single hero image per top-50 wrestler. Flag: licensing must be
resolved (official press kits, Creative Commons, or commissioned art) — this is a rights task, not just
a code task.
**Buildable?** Static hosting is fine; **flag** image rights as the blocker.

### B5. Numbers that don't add up — small trust papercuts that read as auto-generated.
**Evidence.** Stats bar says "41+ Wrestlers" (index 179) while the project actually has ~89-107 wrestler
pages; "12,840 fans on the waitlist" (index 270) is a hard-coded fabricated figure with no source;
the Organization `sameAs` Bilibili link is an empty stub `https://space.bilibili.com/` (index 30).
Fabricated round-ish numbers next to real ones is an AI tell and a trust leak.
**Fix.** Make the counters reflect reality (generate the count at build time from the file system), drop
the fake waitlist number until it's real ("Be an early member" beats a made-up 12,840), and either fill
or remove the empty social URLs.
**Buildable?** Yes — build-time counts; copy edit.

---

## PART C — ACCESSIBILITY / STRUCTURE / PERF (quieter, still disqualifying at senior level)

### C1. Mega-nav `aria-expanded` never updates on desktop. Screen readers are told the panel is closed while it's open.
**Evidence.** `.nav__link` carries a static `aria-expanded="false"` (index 52+). On desktop the panel
opens via CSS `:hover`/`:focus-within` (site.css 122); `main.js` only flips `aria-expanded` on the
`max-width:900px` branch (lines 24-33). So keyboard/AT users on desktop get a permanently "collapsed"
announcement.
**Fix.** On focus-within/hover for pointer users, sync `aria-expanded`; better, make the top items real
disclosure buttons with JS-driven state at all widths.

### C2. Nav markup (~80 lines) is duplicated inline into every one of ~170 pages.
**Evidence.** The identical header/`cmdk`/footer block is pasted into `/index.html`, `/wrestlers/kane/`,
`/matches/…`, `/events/`, `/moments/…` — verbatim. Any nav change is a 170-file edit, which is exactly
how A1's divergence happened and how the next one will. (This is inherent to no-build static, but it is
currently unmanaged.)
**Fix.** Keep it static but generate the shell from one partial in the build scripts, and have the build
verify all pages carry byte-identical shell markup. This is also your guardrail against the
mega-nav ever silently growing past its fixed tab budget.

### C3. Render-blocking font payload + always-on hero animation.
**Evidence.** Every page loads Anton + Oswald (4 weights) + Inter (4 weights) from Google Fonts as a
render-blocking `<link>` (index 27). The hero runs a 26s infinite `conic-gradient` animation
(`heroDrift`, site.css 426-427) that repaints continuously above the fold.
**Fix.** Self-host and subset the fonts (`font-display:swap` already present), drop unused weights, and
`preload` only the two used in the hero. Consider pausing `heroDrift` once scrolled out of view.

---

## PART D — STEAL THIS: specific, sourced patterns that make it feel human and authoritative

Each is buildable on a static, crawlable site.

### D1. Letterboxd "Four Favorites" + one-line reviews → give every reviewer and every wrestler a POV surface.
**Source & why.** Letterboxd's most-copied feature is the **Top Four** on every profile: an instant
identity marker and conversation starter, plus its culture of **funny one-line reviews** that are
shareable and human ([ScreenHub](https://www.screenhub.com.au/news/features/the-letterboxd-phenomenon-why-film-lovers-love-this-app-2659530/)).
**Steal.** (1) On each author page (B1), a "Four Favorites" match poster row. (2) On each match page, a
pull-quote "the one-line verdict" above the long review (e.g. "Two men in their forties out-wrestled the
entire card and the calendar."). (3) Curator **Lists** ("Matches that broke kayfabe," "Five-star debuts")
as static pages — pure internal-linking gold for crawlability.
**Buildable?** Fully static.

### D2. Rotten Tomatoes / Metacritic dual score → replace the fake aggregate with an honest two-source verdict.
**Source & why.** RT/Metacritic earn trust by showing **critic vs audience** as two separate,
sourced numbers. It is the antidote to A2: you already *have* two legitimate external numbers.
**Steal.** A `.verdict` component per match showing three labeled figures: "Wrestle Lore 5.0 (our call,
bylined)", "Meltzer ★★★★¾", "Cagematch 9.6/10 (community)". You already display these in the tale-of-the-tape
table (WM25 lines 220-221) — promote them into a designed, honest scorebar and drop `aggregateRating`.
**Buildable?** Static; cite/link the external sources for E-E-A-T.

### D3. Cagematch rating center → distribution + vote count, shown only when real.
**Source & why.** [Cagematch](https://www.cagematch.net/?id=111) is the genre standard: every match
shows a **community average out of 10 and the number of votes**, plus a comments center. The vote count
is the credibility — the opposite of an invented 9,640.
**Steal (phased).** Ship the *empty state* now: a real 5-star input (already styled, `.rate`) with "Be
the first to rate this — join free." When you have a backend/edge function for votes, render the true
average and a small distribution bar. **Flag:** live community voting needs a backend (e.g. a form
POST to an edge function / serverless store); the display layer is static.

### D4. Pitchfork decimal score + "Best New" badge → a signature verdict object.
**Source & why.** Pitchfork's authority comes from a single decisive number (8.7) and a coveted badge.
It signals "we take a side."
**Steal.** A reusable "5-Star Club" badge (you already gesture at it, index 255) applied consistently,
and a bold numeric verdict at the very top of each match page above the fold, with the reviewer's name.
**Buildable?** Static CSS component.

### D5. Defector/Wrestling Observer named-voice model → the trust engine, not a widget.
**Source & why.** [Defector](https://defector.com/) proves an audience will pay for *people with
opinions and names*, not neutral aggregation. Meltzer's star ratings carry weight because Meltzer's name
is on them.
**Steal.** Bylines + author pages (B1), a short "How we rate" manifesto on `/methodology/` written in
first person with a real signature, and an editorial voice guide so section copy stops sounding
interchangeable (B2).
**Buildable?** Fully static.

---

## PRIORITIZED PUNCH LIST
1. **A1** — reconcile the 98 broken profile pages with the design system (regenerate; add a class-audit build gate). *Highest impact; it's the whole database.*
2. **A2** — strip fabricated `AggregateRating` from 30 match pages; replace with D2 honest dual score. *Trust landmine.*
3. **B1 + D5** — put real named humans and bylines on every rating. *Kills the AI-slop feel; builds E-E-A-T.*
4. **A3, A4** — make the watch buttons and record filters real, or stop claiming they work.
5. **B2, B5** — opinionated copy, obey the em-dash rule, fix the counts.
6. **B4** — resolve image rights and ship faces. **C1-C3, D1/D3/D4** — polish and stickiness.
