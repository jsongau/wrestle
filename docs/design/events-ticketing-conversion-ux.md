# Conversion & UX Spec (v1) — Events & Tickets

**Status:** authoritative conversion/UX layer. **Supersedes** the conversion/UX portions of `events-ticketing-page.md` (§3–§4, §9–§10) and amends `events-ticketing-master-brief.md` (scope + definition of done) where noted in §2. Companion facts: `data/research-wwe-ticketing.md`.

**How this was produced:** a 5-lens agent panel — conversion-funnel architect (`calm-conversion` + `conversion-first-copy`), UX/interaction + visual (`accessible-by-default` + `luxury-editorial-design`), copywriter (`my-writing-style` + `kill-ai-tells`), retention (`gamification-retention-loops`), and an adversarial critic (`brutal-teardown`). The critic overturned several earlier assumptions; this doc integrates the corrections rather than averaging them. Where two lenses disagreed, the resolution and the loser are stated (§14).

---

## 1. Corrected strategic frame (three rules that govern everything)

1. **Capture identity before every outbound hand-off — but the list must stand on its own value.** We don't own the transaction, so each out-link leaks unless paired with a capture. The capture's promise is concrete and self-sufficient: *"never miss a presale or on-sale near you,"* not *"join a membership."*
2. **Club WWE is editorial we link OUT to, never the label on our own list.** On the page: "Here's WWE's official membership — join on WWE.com." In the portfolio/interview: "I built a working *model* of the funnel that would convert fans into Club WWE members." The page never implies a fan is enrolling in Club WWE, because we can't enroll them. This keeps the cleverest positioning without the brand/legal exposure.
3. **Honesty is the conversion strategy, because the audience includes a WWE recruiter.** No phantom access, no fabricated counts, no countdowns to nothing, no "code" we don't hand out, no resale scarcity we can't source. One fake element spotted by WWE brand/legal outweighs every CRO gain.

---

## 2. Corrections to the page spec & master brief (adopt these)

The panel changed the following from the earlier specs. Build agents follow this doc where it conflicts.

- **Kill "priority access" / "membership waitlist" language (was Module 9).** We cannot enroll anyone in a real queue. Reframe as an **inventory + price watch**: "Sold out? We'll tell you if resale drops or more seats release," plus a link out to Club WWE as WWE's official early-access route.
- **Transactional email sender moves INTO MVP scope** (was "out of scope" in master brief §8). Double opt-in *requires* a confirmation sender; without it, zero rows confirm and the entire list is unmarketable. MVP includes the confirm email + one real first-alert. SMS sending can stay deferred; email cannot.
- **One primary capture per page** (was up to ~10 competing asks). Everything else progressively profiles the *same* record. See §3.
- **Email-first, single field, everywhere. SMS demoted** to an optional progressive add for the presale case only (was "SMS-first"). See §14.
- **CTA hierarchy is lifecycle-aware / state-dependent** (was a fixed "Get tickets primary / Alert me secondary"). See §4.
- **Rename "presale-code alert" → "presale reminder."** Never promise a "code." See §6.2.
- **Lead the differentiated wedge; defer generic modules.** Signature = the attend-map + honest presale coaching + Follow-a-Superstar. Defer the seat-map preview, deal-score, and the multi-seller resale comparison shelf. See §5.
- **Resolve the no-browser-storage vs "set your city" contradiction** before building personalization. See §14.
- **Show a sourced price anchor on the buy CTA** using the Discovery API's live `priceRanges` (was: no price at all). See §14.
- **Handle empty / past / negative-countdown states** with a build-time guard. See §7.

---

## 3. Capture architecture — one primary ask, progressive profiling on one record

The old plan scattered ten email asks, each with its own verb (Alert / Notify / Watch / Follow / Track / Remind / Join / Save). When everything is a capture, nothing is the capture, and verb sprawl blocks a mental model.

**New model:**
- **One primary capture per page,** stated once, high, in plain language. On `/events/` and on each event page it's the presale/on-sale **reminder** scoped to context; on the homepage module it's **notify-me-by-city**.
- **Everything else enriches the same `signup` record** (progressive profiling): once we have an email, following a Superstar, setting a city, RSVPing, or watching a price **adds fields, never re-asks for email.** A returning known fan is recognized, not re-onboarded.
- **One standard capture verb** ("Get [X] reminders" / "Notify me") across the page. The **only** module allowed a distinct verb is **Follow** (a Superstar) — because its mental model genuinely differs (you're following a person, not an event).
- **Duplicate opt-in = success-with-enrichment,** never an error ("Added SummerSlam to your alerts").

This also fixes the schema over-ask: fields accrue over time on one row instead of being front-loaded into one giant form.

---

## 4. Lifecycle-aware CTA hierarchy (the core conversion lever)

The buy button leaks your highest-intent fan; the alert only catches the not-ready fan. Resolve by making the hierarchy depend on the event's on-sale state. Primary = visually dominant (bone fill); secondary = ghost; tertiary = text.

| Event state | Primary CTA | Secondary CTA | Tertiary |
|---|---|---|---|
| **On sale now** (e.g., SummerSlam) | **Get tickets** → Ticketmaster, with a live "from $X" anchor (§14) | **Watch the price** (capture) or **Remind me before the next on-sale** | Premium & ringside → On Location |
| **Announced, presale/on-sale upcoming** (e.g., Survivor Series) | **Get the presale reminder** (capture — the hero) | Get tickets when live → Ticketmaster (disabled/"opens Aug 7") | Premium → On Location |
| **Sold out** | **Watch for resale + released seats** (capture) | See resale reality → Ticketmaster/StubHub (labeled) | How Club WWE early access works → WWE.com |
| **Announced, no on-sale yet / marquee future** (e.g., WM43 Riyadh) | **Notify me when tickets/travel go live** (capture — the hero) | Follow the Road (season drip) | Official travel → On Location |

Rule: for the ~95% of visits where the fan can't or won't buy this second (event months out, not on sale, sold out, wrong city), **the capture is the hero and dominates.** Only "on sale now" gives the outbound button the primary slot — and even then it carries a price anchor and a co-adjacent capture reason.

---

## 5. The wedge — what leads, what's deferred

**Lead with the two things a generic "Bandsintown for wrestling" cannot copy:**

1. **The "How to attend" map + honest presale coaching.** Nobody maps WWE's fragmented global ticketing — US = Ticketmaster (+ AXS at AEG venues), Saudi = webook, Australia = Ticketek, Europe = local Ticketmaster, premium everywhere = On Location. This is pure, sourced fan service and the most citable, most trust-building surface on the site. It's the signature.
2. **Follow-a-Superstar + your city** ("Follow Cody + set Minneapolis → we'll tell you when he's near you"). The richest affinity axis, the most emotional opt-in reason, and the loop with the highest honest trigger frequency (a ~50-name roster is always generating real news). Both the retention lens and the critic independently ranked this the #1 thing to build — so it moves into MVP, not phase 2.

**Support with:** notify-me-by-city (acquisition breadth), the state-dependent next-event hero, the On Location band + WM43 pre-capture, RSVP going/watching (as a personal utility), and "Follow the Road" (the season retention spine).

**Defer (post-MVP):** seat-map preview link-out, SeatGeek-style deal-score, the multi-seller resale comparison shelf, and "set your city" persistence (blocked on the storage decision, §14). These are the most generic and lowest-trust; polishing them for launch dilutes the wedge.

---

## 6. Surviving capture flows (fields, progression, honesty)

Global: email-first single field → progressive optional phone (with explicit unchecked SMS consent) → double opt-in via transactional email. No browser storage of PII. Honeypot + rate limit. One-click unsubscribe + SMS STOP surfaced in the confirmation. Coarse IP city pre-fill (editable); precise geolocation only on explicit tap.

### 6.1 Notify-me-by-city (primary on homepage; the "no dead end")
Email (required) → `home_market` carried from the search field (never re-asked) → optional "also follow a Superstar?" (enriches, doesn't gate). Promise: *"We'll email you the day WWE books a date near [city], and again when presale and public on-sale open."* Also puts a capture on the **results** state, not just no-results: *"Not the show you wanted? Get alerts for Premium Live Events near [city]."* (Most metros return a weekly-TV taping, so the results path must capture too, and must not show a Tuesday NXT taping as a "match" to a PLE-seeker — filter by `event_tier`.)

### 6.2 Presale reminder (renamed; honest coaching)
Email (required) → optional phone for the time-critical go-live text (explicit why). Event pre-scoped from context. Promise: *"WWE's free presale runs on an email window that closes before the public on-sale. We tell you when and where to register, and which card unlocks it. We don't hand out codes, and nobody should."* First alert delivers exactly that, so expectation = reality. Never the word "code" in the promise.

### 6.3 Sold-out → resale + release watch (replaces "waitlist")
Email (required). Promise: *"Sold out? We'll alert you if verified resale drops or more seats release."* Plus editorial link-out: *"Want early access next time? That's what Club WWE ($99/yr) is for — here's how it works on WWE.com."* No queue language, no `member_prospect` implying we enroll anyone; keep an internal `sellout_demand` signal (demand data) without promising access.

### 6.4 Follow-a-Superstar (the wedge; distinct verb allowed)
One tap "Follow" on any wrestler/event card = the opt-in (writes `followed_talent[]`). If no email yet, the first follow asks once for email, then never again. Promise: *"We'll tell you when [name] is booked near you."*

### 6.5 RSVP going / watching (personal utility first)
One-tap toggle, zero fields, records an anonymous intent signal; asks for email only if the fan wants reminders. **No visible counts until real and non-trivial** (see §13). The going/watching *ratio* is the only inherently honest numeric surface (a proportion the page itself produces) — show it only past a threshold.

### 6.6 Price watch (single, not a 4-way shelf)
Email (required) → optional target price. Promise: *"We'll email you when verified resale drops"* (to your target or on the next real drop). Resale is de-emphasized and labeled; we lead primary + official, not a scalper comparison wall.

---

## 7. State matrix (design every state; "graceful" must be defined)

**Search (the live layer):**

| State | Behavior |
|---|---|
| Default | Input + baked upcoming rail visible; no auto geolocation prompt |
| Loading | Skeleton at exact card dims (no CLS), `aria-busy`, "Searching near [city]…", **3s timeout → fallback** |
| Results | ≤5 cards, each links out (affiliate) with live "from $X" price anchor; **capture offered on this state too** (§6.1) |
| No results | Region morphs to notify-me capture, city pre-filled; "Nearest date: [event] · [mi] — going to travel?" (routes distant intent → On Location) |
| Error / timeout / quota | Fall back to baked list instantly + keep capture; "Search isn't loading right now. See all upcoming events." Never a spinner to nowhere. **Cache by city+radius bucket; pre-warm top metros; serve baked instantly for common cities.** |
| No-JS | `<form method="get" action="/events/tickets/">` renders the baked filtered list |

**Capture:**

| State | Behavior |
|---|---|
| Success | Inline "You're on the list — check your email to confirm." (double opt-in stated) |
| Duplicate | Success-with-enrichment, never an error ("Added [event] to your alerts") |
| Error / network | "That didn't send — tap to retry," entered data preserved (needs the in-flight state exception, §14) |
| Invalid email | "That email doesn't look right. Check it and try again." |
| No-JS | Real HTML form POST → **server-rendered confirmation page** (capturing works without JS, the honest choice) |
| Confirmation bridge | Pending-confirmation page carries real value (the actual on-sale date + their market's platform), an "open Mail" affordance, and a 24h resend — so it isn't a dead wait |

**Countdown / event lifecycle:**

| State | Behavior |
|---|---|
| Real deadline pending | Countdown only to a real fan action: presale registration close, "code through tonight," public on-sale open (e.g., Survivor Series Aug 5 → 6 → 7). Every countdown answers "do this before zero." |
| On sale, no pending deadline | Show the **date, not a ticking clock** ("SummerSlam is August 1 and 2, 2026"). A clock counting down to event start once tickets are on sale is soft fake urgency — don't. |
| Reduced-motion / no-JS | Static date, value crossfade not slot-flip, seconds de-emphasized/omitted |
| Zero / underway | Clamp at zero → "Happening now" / "Just wrapped" |
| No upcoming event exists | Degrade to "Next event TBA — get notified" (an empty state that itself converts) + a **build-time guard that a future event is present** so the homepage hero never shows a past event with a negative clock |

---

## 8. Double opt-in + transactional sender (now MVP)

The confirmation email is not optional infrastructure — it's the thing that makes a row marketable. MVP wiring:
- Transactional sender for (a) the confirm email and (b) the first real alert. Report **confirmed vs unconfirmed separately** in the funnel readout or the metric lies (realistic confirm rate is ~40–70%).
- The first alert after confirmation carries **real value**, not a "welcome": the actual on-sale date and the fan's market platform. This proves the channel on message one.
- Consent is unchecked and explicit; SMS requires a separate "reply YES." This compliance literacy is itself part of the portfolio story.

---

## 9. Reconciled copy (surviving strings, style-checked)

Voiced with `my-writing-style` + `kill-ai-tells`; no em-dashes as separators, no arrows in labels, verb+object CTAs, no fabricated numbers, Club WWE as link-out. Corrected where the critic overturned the earlier copy.

**Next-event hero — on sale now (SummerSlam):**
- Eyebrow: `The next Premium Live Event`
- H1 (A/B): "SummerSlam lands in Minneapolis, August 1 and 2" / "Get in the building for SummerSlam"
- Answer-first: "WWE's next Premium Live Event is SummerSlam, on August 1 and 2, 2026, at U.S. Bank Stadium in Minneapolis. Tickets are on sale now through Ticketmaster. Ringside seats and travel come from On Location, WWE's official hospitality partner."
- Primary CTA (A/B): "Get SummerSlam tickets" / "See seats on Ticketmaster" — with live "from $X" anchor
- Secondary CTA (concrete, not "alert me"): "Watch SummerSlam prices"
- Tertiary: "See official ringside and travel"
- Countdown: static "SummerSlam is August 1 and 2, 2026" (on sale, no pending deadline → no ticking clock)

**Next-event hero — presale upcoming (Survivor Series):**
- Primary CTA: "Get the Survivor Series presale reminder"
- Honest, dated line: "Presale is August 6. Public on-sale is August 7. Register before August 6 for the earliest shot."
- Countdown target: presale open (a real deadline)

**Find WWE near your city:**
- Heading: "Find WWE near your city" · placeholder: "Your city or ZIP" · button: "Find events near me"
- No-results→capture: "No WWE dates near [city] yet. Leave your email and we'll tell you the day they book one." Button: "Notify me about [city]"
- Results→capture (new): "Not the show you wanted? Get alerts for Premium Live Events near [city]."

**Presale reminder block:**
- Heading: "Register for the presale before the window closes"
- Body: "WWE's free presale runs on an email window that closes before tickets go public. Miss the window, miss the presale. Pick your events and we'll tell you the day registration opens."
- Trust line: "We tell you when and where to register. We don't hand out presale codes, and nobody should."
- Button: "Get presale reminders" (email-first; SMS offered after)

**Sold-out → resale/release watch (reframed, no "waitlist"):**
- Heading: "Sold out? We'll watch it for you"
- Body: "When seats are gone, we'll alert you if verified resale drops or more seats release. Want early access next time? That's what Club WWE ($99 a year) is for — here's how it works on WWE.com."
- Button: "Watch this event"

**On Location band:**
- Heading: "Want ringside? Go through the official partner"
- Body: "On Location is WWE's official hospitality partner, and it shares WWE's parent company, TKO. Its WWE packages, WWE Priority Pass, bundle official tickets, front-row and club seats, pre-show hospitality, and Superstar meet-and-greets."
- Price line (only with a sourced figure, else omit): "SummerSlam packages start at ${from}, as of {as_of}."
- Button: "See On Location packages" · Trust: "On Location is the official seller. We're a fan guide that links to it, not a reseller."

**WM43 pre-capture:** "WrestleMania 43 is heading to Riyadh. In 2027, WrestleMania runs outside North America for the first time. Travel packages aren't on sale yet. We'll tell you the day they are." Button: "Notify me about WrestleMania 43 travel."

**Compliance:** affiliate line adjacent to buttons — "Some links here are affiliate links. If you buy through them, we may earn a commission. It never changes the price you pay." Footer — "Wrestle Lore is a fan guide. We don't sell tickets. We link to official and authorized sellers, including Ticketmaster, On Location, AXS, webook, and Ticketek. We're not affiliated with or endorsed by WWE or TKO."

FAQ (8 answer-first Q&As) and the full state-copy set are carried verbatim from the copywriter's deliverable (they passed the style self-check) with the "waitlist" answer reworded to the resale/release framing above.

---

## 10. Retention loops + lifecycle map (the engine)

The loop lives in the channel, not the page (static, no storage). Build the **lifecycle alert engine once**; every module is a trigger source + a segment.

**Four loops** (trigger → action → variable reward → investment): Follow-a-Superstar (identity anchor — honest, high-frequency triggers from the roster), Follow-the-Road (season spine — the calendar hands you ~monthly re-engagement), RSVP going/watching (forks the list into two lifecycle tracks), Notify-me-by-city (latent demand + a demand-forecast dataset).

**Lifecycle map** (condition on `signup` × `events.json`; SMS only for go-live/code-adjacent moments, email for the rest):
Just-Announced (email, geo/talent-targeted) → Presale-registration-opens (email + SMS for high-intent) → Presale-live (SMS: which card / how to register, never the code) → Public-on-sale (SMS go-live + email) → 1-week (email, forked: going→travel/On Location; watching→how-to-watch) → 1-day (SMS for going; email for watching) → Post-event (email recap → next Road stop) → Win-back-by-city (only on a *real* new event in the market). Stage 7 hands the fan back to stage 1 — a ring, not a funnel.

**Optional light points/streak/referral** — only if it pays out in what a fan guide can honestly deliver (earlier alert send-order, our own resale-watch priority, recognition) and clearly ladders *up into* Club WWE's real rewards (link out), never counterfeits them. Referral counts only after the invited fan confirms *and* takes one real action; anti-gaming safeguards mandatory. Build this last, after there's engagement data worth rewarding.

**Build first:** Follow-a-Superstar wired directly onto the lifecycle engine — highest retention because the affinity is identity-level (doesn't churn between events) and the roster supplies constant honest triggers.

---

## 11. Visual hierarchy + mobile interaction (premium, not coupon)

**Contrast rulings (measured on `#0a0b0d`), non-negotiable:** gold `#d4af37` ~9.4:1 (safe; reserve for premium/membership only); **red `#e11d2a` ~4.1:1 fails AA for normal text** — use only as large text, fills, borders, or icon+label; on-sale pill = red fill + **white** label + icon (~4.76:1, passes); body bone `#f4f1ea` ~15:1; meta gray floor `#8a8a8a` ~5.5:1, go no lighter.

**CTA color system (three distinct jobs):** primary = **solid bone fill + near-black label** (max contrast, wins the eye); secondary = **ghost** (1px bone-40% border, transparent, same width, immediately adjacent); tertiary = text link with the one gold underline. Status = red (fill+white+icon). Premium/membership = gold. Red and gold never become chrome for ordinary buttons.

**The one gold moment:** the On Location / Priority Pass band is the single indulgent surface. Gold appears nowhere else except the countdown's active hairline and the tertiary underline. Restraint is the premium signal.

**Editorial layout:** hairline dividers (1px ~12% bone) between modules, **no boxed drop-shadow cards**; oversized Anton section numbers "01–12" as left-margin marks; the upcoming grid features the next event larger, the rest smaller (varied rhythm, not three identical coupon tiles); whitespace 64→112px between modules; measure ≤66ch; duotone art-directed arena imagery, no clip-art, no emoji icons.

**Type scale (mobile→desktop via clamp):** hero name Anton 44→88 / 0.96; H2 Anton 26; body Inter **16** (never lower — iOS zoom) / 1.6; countdown JetBrains Mono 34 `tabular-nums`; eyebrow Oswald 12 upper +2. Spacing on an 8px base.

**Mobile @360 (the risky modules):**
- **Road-to-WrestleMania timeline → vertical stepper on mobile** (scroll-snap horizontal is a desktop enhancement only, always with a vertical fallback for keyboard/SR/no-JS). No auto-advance.
- **Attend-map → stacked list keyed to the fan's own market first** ("In the US? Ticketmaster + On Location"), never a multi-column table (360 overflow).
- **Tour map → facade** (baked schematic + tappable 44px pins → bottom sheet, never hover tooltip) with an adjacent baked market list; a real pan/zoom map only inside a full-screen modal, two-finger gesture, never one-finger (hijacks page scroll).
- **Price row → one "Compare prices" tap expands the seller list** (never 4 buttons crammed in a row); FTC line adjacent; all-in or labeled "from/base + fees, as of [date]."
- Reserve min-height on the results/capture region so the "field morphs into capture" swaps content **inside a fixed container** (no layout shift under the thumb). Extend reduced-motion handling to all injected transitions, not just the countdown.

**Focus ring (all interactives):** `box-shadow: 0 0 0 2px #0a0b0d, 0 0 0 4px #f4f1ea` — visible on dark, on gold, on bone. CLS ~0: reserve hero `aspect-ratio`, fixed-width countdown, exact skeleton dims, matched font fallback metrics.

---

## 12. A/B backlog (top 8, adjusted)

1. Concrete benefit vs generic verb: "Alert me" → "Get presale reminders" (opt-in rate).
2. Homepage order: next-event spotlight first vs city-search first (total capture rate; guardrail = ticket CTR).
3. Email-only vs email+phone shown together (submit rate; SMS share as secondary).
4. Future-moment framing: "Get notified" → "We'll email you the day WWE books [city], before the presale window closes" (no-results→capture conversion).
5. Coarse IP city pre-fill vs empty field (search submit rate; guardrail = wrong-city corrections).
6. Wedge test: lead with "Follow [Superstar] + your city" vs "notify me for this event" (opt-in rate + segment richness).
7. Sold-out reframe: honest resale/release watch vs any "priority" language (opt-in rate + a qualitative trust read).
8. Price anchor on buy CTA: no price vs live "from $X (via Ticketmaster)" (outbound CTR).

Each ships behind a real metric; none manipulate. Primary KPIs: confirmed opt-in rate, list growth, opt-in→engaged, alert CTR to partner, per-segment outbound clicks.

---

## 13. Analytics (honest measurement)

Fire one PII-free intent event per action (`notify_city`, `presale_optin`, `reminder_set`, `waitlist`→`resale_watch`, `price_watch`, `rsvp_going|watching`, `talent_follow`, `outbound_click{seller,event}`); fire `outbound_click` **before** unload. Keep email/phone out of analytics payloads (backend only). Report **confirmed vs unconfirmed opt-ins separately.** Social-proof counts render only above a real floor (round down, suppress small-N); the RSVP ratio is the one safe numeric surface. No seeded numbers — the site removed fabricated counts once; don't reintroduce them.

---

## 14. Resolved spec conflicts

- **SMS-first (funnel lens) vs email-first (critic).** Resolved: **email-first, single field, everywhere.** Phone appears only after email succeeds, only for the time-critical presale go-live, with an explicit why. Leading SMS on a site that says "we are not WWE" is a trust cliff and craters mobile completion. Data, not the portfolio narrative, decides whether SMS earns expansion.
- **No-browser-storage vs "set your city" persistence.** Resolved: carry `home_city` in the **URL query** as the fan navigates (works within the no-storage rule), and design the returning-known state (don't re-ask for a city we already have; suppress opt-in prompts for lists they're on). A single non-PII preference cookie is an acceptable, explicitly-documented exception if URL-carrying proves clumsy — but PII never goes in storage. Until resolved, "set your city" persistence stays deferred (§5).
- **Countdown everywhere vs honesty.** Resolved: countdowns only to **real fan deadlines**; neutral date otherwise; clamp at zero; empty state converts.
- **Price-less buy CTA (honesty) vs no anchor (conversion).** Resolved: use the Discovery API's live `priceRanges` — a sourced, real-time, FTC-compliant figure — as "from $X (via Ticketmaster)" on live cards; baked pages carry a dated "as of" range; omit only when truly unavailable.
- **Kitchen-sink modules vs a wedge.** Resolved: lead the attend-map + presale coaching + Follow-a-Superstar; defer generic clones (§5).

---

## 15. Build order (before you write UI)

1. **Detox the language** (cheap, existential): kill "priority access"/"membership waitlist"; demote Club WWE to link-out; rename "presale-code alert" → "presale reminder." Do this first — one brand/legal snag outweighs every CRO gain.
2. **Guarantee delivery:** transactional sender + first real alert into MVP; design the confirmation bridge; report confirmed vs unconfirmed.
3. **Rebuild capture around one lifecycle-aware primary ask** per page (§3–§4); email-first; progressive profiling on one record.
4. **Lead the wedge:** attend-map + presale coaching + Follow-a-Superstar; capture on search *results* too; defer the generic modules.
5. **Specify the hand-waved states** (§7): no-JS capture, duplicate/error, empty/past/negative countdown, API timeout+cache+peak-load, geolocation permission, storage-vs-personalization.

---

## 16. Definition of done (conversion/UX)

- One primary capture per page; every other action enriches the same record; duplicate = enrichment, not error.
- CTA hierarchy switches by on-sale state; on-sale-now carries a live sourced price anchor.
- Capturing works with JS off (real form POST → server-rendered confirmation); double opt-in has a working sender and a confirmation bridge; confirmed vs unconfirmed reported separately.
- No phantom access, no "code" promise, no fabricated counts, no countdown-to-nothing; affiliate disclosure adjacent; all-in or labeled pricing.
- Email-first; SMS only as a justified progressive add.
- Mobile 360: timeline vertical, attend-map stacked, maps tap-not-hover, price sellers behind one expand; AA contrast (red only as fill+white+icon or large); focus ring visible on every surface; CLS ~0; reduced-motion covers all injected transitions.
- Every capture writes one clean segment; every intent fires one PII-free event; the wedge (attend-map + presale coaching + Follow-a-Superstar) is what a fan remembers.
