# Design Spec — "Events & Tickets" (the /events/ upcoming + ticketing surface)

**Status:** design spec, pending build. **Owner decisions (locked 2026-07-27):** hybrid data (baked list + live Ticketmaster Discovery API); **WWE-first, extensible**; primary CTA = **owned-channel capture framed as the Club WWE funnel**.
**Companion docs:** `data/research-wwe-ticketing.md` (facts + sources), `docs/design/homepage-next-event-module.md` (the front-page hook), `docs/design/events-ticketing-master-brief.md` (the build plan).

---

## 1. The one-line thesis

> A fan-first guide to **attending** WWE live — every "buy" links **out** to the official/authorized seller (Ticketmaster / AXS / webook / Ticketek / **On Location**), and every moment of intent captures an **owned-channel identity** (email/SMS) stamped with a **CRM segment** (geography × event-interest × attend-intent). It is, deliberately, the exact **owned-channel funnel that converts fans into Club WWE members** — WWE's real $99/yr membership that launched this week.

Every module must justify itself by the site's six levers: **acquisition, engagement, retention, trust, revenue, operational efficiency.** If a module captures no owned identity and produces no segment, cut it.

---

## 2. Where it lives (IA + nav rule)

The site already has an `/events/` hub, but it is **backward-looking** (past PLE results: Royal Rumble 2026 → Night of Champions 2026, built by `build_events_11.py`). We are adding a **forward-looking** layer. **Do not widen the top nav** — `Events` is already a nav7 tab. Structure:

```
/events/                     Hub — SPLIT into two clearly-labelled zones:
                               ┌ "Upcoming & Tickets"  (NEW — this spec, sits on top)
                               └ "Results Archive"      (EXISTING — recent editions + brands)
/events/{slug}/              Event page — LIFECYCLE-AWARE:
                               • before the event → "How to attend / get tickets" (this spec)
                               • after the event  → flips to "Results" (existing template)
/events/tickets/             (optional) Standalone "Find WWE tickets near you" landing
                               for SEO — same modules, city-search first. Routes under /events/.
```

Reconciliation rule: the upcoming event page and the results page are **the same URL over time** — a build flag (`status: upcoming|past`) selects which template renders. SummerSlam 2026 renders "attend" today, "results" on Aug 3. This keeps one canonical URL per event (good for SEO, matches the existing slug pattern, no redirects).

Nav wiring: add an **"Upcoming & Tickets"** link inside the existing **Events mega-panel** (the nav7 "Events timeline" panel), not a new tab. Per `jay-domain-skills:nav-budget-guard`.

---

## 3. Page anatomy — /events/ hub, top to bottom

Mobile-first (360px), enhanced up. All content renders **without JS** (baked HTML); JS only *enhances* (live search, countdown, capture). Reuse existing components where noted.

**A. Next-Event hero** — reuse/extend `ev-hero`.
- The single next PLE (today: **SummerSlam · Aug 1–2 · U.S. Bank Stadium, Minneapolis**), with a **live countdown** (to event, and to next on-sale/presale milestone), `meta-chips` (date / venue / city), and a two-button row:
  - Primary (out): **"Get tickets"** → Ticketmaster (affiliate-wrapped).
  - Secondary (capture): **"Alert me for this event"** → email/SMS opt-in scoped to the event.
- Small third link: **"Premium & ringside"** → On Location (labelled "Official WWE hospitality").
- Answer-first sentence under the H1 (for GEO): *"WWE's next Premium Live Event is SummerSlam, Aug 1–2, 2026 at U.S. Bank Stadium in Minneapolis; tickets are on sale via Ticketmaster, with official ringside and travel packages through On Location."*

**B. "Find WWE near your city"** — the hybrid data star (see §5).
- City/ZIP field + radius. On submit: **live** Ticketmaster Discovery API results (cards → outbound `url`). If nothing near: flips to **"Notify me when WWE comes to [city]"** capture (never a dead end — the Bandsintown pattern).
- No-JS fallback: the field is a normal GET that lands on `/events/tickets/?city=…` rendering the **baked** upcoming list filtered by state/market.

**C. Upcoming events grid** — reuse `event-grid` + `ev-tile`.
- All confirmed upcoming events (baked from `data/events.json`), each tile: date · city · brand accent · on-sale status pill (`On sale` / `Presale Aug 6` / `Announced`). Tile → the event's "attend" page.
- A `facets.js`-powered filter bar (brand: Raw/SmackDown/NXT/PLE; region; month) — reuse the existing hub filter pattern.

**D. "How to attend" channel map** — new lightweight component `attend-map`.
- The highest-utility, most-defensible module: a compact matrix telling fans **which platform for which market** (US → Ticketmaster/On Location; Saudi → webook; Australia → Ticketek; Europe → local Ticketmaster). Each cell links out. This is pure fan service and 100% honest.

**E. On Location / Priority Pass row** — new `priority-pass` band (visually premium, gold).
- "Want ringside, hospitality, or travel? Go official." Explains On Location = the **official** WWE premium seller (and, in a subtle trust line, part of TKO — WWE's parent). Links `onlocationexp.com/wwe` and per-event slugs. Price framed as **"packages from $[X], as of [date]"** with source, never asserted flat. Capture: **"Notify me when WM43 (Riyadh) travel packages drop"** — the marquee 2027 pre-capture.

**F. Presale & alerts capture** — new `presale-capture` (the funnel core).
- "Never miss a presale." Teaches the honest levers (register on WWE.com; watch for the credit-card presale — recently Chase; Verified Fan is a lottery) and offers the site's value: **"We'll alert you the moment presale registration opens for your events."** SMS-first for time-sensitive codes (proves multi-channel for the portfolio). Segments by event + channel.

**G. "Road to WrestleMania" timeline** — new `road-timeline` (editorial + commerce).
- Horizontal season map (Rumble → Chamber → WrestleMania → Backlash → MITB → SummerSlam → Survivor Series), each node = city + on-sale status + CTAs. "Follow the Road" = a themed drip subscribe. Retention centerpiece; links each node out.

**H. Secondary-market / price-range row** — new `price-row` (link-out only).
- Per marquee event: "GA from $X · VIP from $Y (as of [date])" + a **value hint** ("prices soft right now" only when sourced) + **"Watch price"** capture (email when resale drops). Buttons compare StubHub / SeatGeek / TickPick / Ticketmaster resale (multi-affiliate). All-in pricing per FTC; disclosure adjacent.

**I. FAQ** — reuse `faq-block` + `FAQPage` schema.
- Answer-first Q→A: "When do SummerSlam tickets go on sale?" "Where do I buy WWE tickets in [country]?" "What is Club WWE and does it get me presale access?" "Is On Location official?" "Why are prices different on each site?" Feeds GEO/AI-answer citation.

**J. Footer disclosure** — reuse FT2 footer + a **compliance strip**: "Wrestle Lore is a fan guide and does not sell tickets. We link to official and authorized sellers. Some links are affiliate links — we may earn a commission at no extra cost to you. Not affiliated with or endorsed by WWE or TKO."

---

## 4. Module catalog (the "cool/niche" widgets — build-ready)

Curated from the 12 researched (full rationale in the research brief §6). For this page, build these; the homepage module doc covers the front-page subset. Each has: **out** = outbound target, **catch** = owned capture, **segment** = CRM payload.

1. **Notify-me-by-city** (hero of §B). out: none (pure capture) → later alerts link to TM. catch: email + optional SMS. segment: `home_market, radius_pref, brand_interest[], event_tier, source`.
2. **Presale-code alert** (§F). out: alert → TM presale. catch: SMS-first. segment: `presale_optin, event_id, channel_pref, intent=high`.
3. **On-sale / presale countdown + "remind me"** (§A, §G). out: on-sale → TM; VIP → On Location. catch: email/SMS + `.ics`. segment: `reminder_event_id, reminder_type`.
4. **Event calendar + add-to-calendar (.ics)** (§C). out: TM/On Location. catch: "save event" soft opt-in. segment: `saved_events[], filters_used`.
5. **Interactive tour map + "set your city" pin** (§B enhancement). out: pin → TM/On Location. catch: empty-map → notify-me. segment: `home_geo, viewed_markets[]` (distant browsing = travel intent → On Location nurture).
6. **"Set your city" personalization spine** — one stored `home_city` re-orders the page (nearest first). segment: canonical `home_market` (stitches anon→known on opt-in).
7. **Superstar Tracker** — follow a wrestler → alert when booked near you (second interest axis, richest affinity). out: alert → event on TM. segment: `followed_talent[]`.
8. **Road to WrestleMania timeline** (§G). segment: `roadmap_subscriber, wrestlemania_intent`.
9. **Sold-out / membership waitlist** (the flagship membership conversion) — when GA is gone or for member-early-access, "Buy" → **"Join the waitlist / priority access."** segment: `waitlist[event], member_prospect, sellout_demand`.
10. **Price-range + resale price-drop watch** (§H). out: StubHub/SeatGeek/TickPick. catch: watch-price. segment: `price_watch[event], target_price, budget_band`.
11. **Seat-map preview link-out** — "view from your seat" hand-off to TM/On Location; capture "notify me when good seats appear in [section]." segment: `section_pref, vip_curiosity`.
12. **"Going?" watch-vs-attend toggle** — "I'm going" / "Watching at home" + social-proof counts. segment: `attend_intent` vs `watch_intent` (two distinct lifecycle audiences: ticket/travel vs watch-party/merch/streaming).

Build priority for MVP: **1, 2, 3, 4, 9** (the pure capture + funnel core) → then **5, 7, 8, 10** → then **6, 11, 12**.

---

## 5. Data architecture (hybrid — the locked decision)

**Baked layer (canonical, crawlable — the SEO/GEO authority):**
- `data/events.json` = source of truth (schema in the master brief). A build script (`build_events_upcoming.py`, following the `build_*.py` + marker-injection pattern used by `build_events_11.py` and `build_ring_feed.py`) renders the hub grid, event "attend" pages, timeline, and channel map into **static HTML** between `<!-- EVENTS-UPCOMING:START/END -->` markers. Crawlers and AI answer engines see everything; zero JS required to read.
- Editing flow (matches Ring Feed rule): edit `events.json` → rerun the build script → never hand-edit the baked block.

**Live layer (progressive enhancement — the "wow" search):**
- `js/events-nearby.js` calls the **Ticketmaster Discovery API** (`keyword=WWE` + `city`/`postalCode`+`radius`/`geoPoint`) on user action only, renders result cards linking to the TM `url` (affiliate-wrapped). Fails **gracefully** → the baked filtered list. Respects quota (~5k/day), low rps, caching limits, and posts the required privacy line.
- API key: **not** committed to the repo. For a static site, proxy the key through a tiny serverless function (Vercel function or Supabase Edge Function) so it's never exposed client-side; the function also lets us cache within TM's limits and attach affiliate params server-side. (Detailed in the master brief.)

**Why hybrid (teach-the-owner note):** a purely live page would be invisible to Google/AI (killing the site's core thesis); a purely baked page can't do real "near me." Baked-for-authority + live-for-delight is the pattern behind most great event sites, and it degrades safely.

---

## 6. Owned-channel capture & CRM model (backend-first)

Per the standing rule (propose schema before UI). The capture is the product; the page is its surface. Minimal, privacy-respecting, in-memory on the client (no browser storage per site rule) → posted to a backend.

Core signup record (one row per opt-in; see master brief for full DDL):
```
signup {
  id, created_at,
  email (required), phone (nullable, for SMS),
  channel_pref: [email|sms],
  home_market (city/metro), home_geo (lat/long or geohash, optional), radius_pref,
  brand_interest: [raw|smackdown|nxt|ple|houseshow],
  followed_talent: [slug...],
  event_id (nullable — set for event-scoped opt-ins),
  intent: [notify_city|presale|reminder|waitlist|price_watch|rsvp_going|rsvp_watch],
  attend_intent: [going|watching|unknown],
  budget_band (nullable), source (module id), utm_* ,
  double_optin_confirmed_at (nullable),
  consent_marketing (bool), consent_ts
}
```
This one table produces the exact **geography × event-interest × intent × channel** segmentation the WWE JD names, and mirrors Club WWE's funnel. RLS insert-only, double opt-in, honeypot + rate-limit. Analytics events fire on every intent action for the funnel-readout page.

---

## 7. Design-system fit

- **Reuse:** `ev-hero`, `event-grid`, `ev-tile`, `meta-chips`/`meta-chip`, `watch2` (rename mental model to "attend"), `faq`/`faq-block`, `sec-h`, `crumbs`, `wrap`, nav7 mega, FT2 footer, `js/facets.js` (filters), `js/enhance.js` (reveal/countdown), `js/nav.js`. **No invented CSS where a component exists.**
- **New components (add to `css/site.css`, namespaced, self-contained):** `attend-map`, `priority-pass`, `presale-capture`, `road-timeline`, `price-row`, `notify-city`, `countdown`. Follow the existing additive, non-breaking convention.
- **Tokens:** `--c-bg #0a0b0d`, `--c-gold #d4af37` (premium/On Location), `--c-red #e11d2a` (live/on-sale/hot), promotion accents (`--c-wwe #c8102e`). Fonts: Anton (display), Oswald (UI/labels), Inter (body), JetBrains Mono (countdown/telemetry). Reuse the "Broadcast Bold" language (arena hero, duotone tiles, glass bar, angled seams).
- **Mobile-first & a11y (WCAG AA):** ≥44px tap targets; 16px form inputs (no iOS zoom); labelled inputs; visible focus; `prefers-reduced-motion` disables countdown flips/reveal; color never the only signal on status pills (icon/label too). Per `jay-domain-skills:accessible-by-default`.
- **Perf:** system-adjacent local fonts (already self-hosted); lazy-load the map/live-search JS (facade); baked HTML paints instantly; target LCP < 2.5s, CLS ~0.
- **Aesthetic bar:** per `jay-domain-skills:luxury-editorial-design` — this should read like DAZN/UFC/ESPN, not a coupon site. Restraint, type hierarchy, generous spacing; the gold On Location band is the one indulgent moment.

---

## 8. SEO / GEO

- **Schema (JSON-LD, double-quoted, validated):** `Event`/`SportsEvent` per event with `name, startDate, endDate, location (Place+PostalAddress), eventStatus, eventAttendanceMode, offers (url→seller, priceCurrency, availability, validFrom), performer, image`; `BreadcrumbList`; `FAQPage`; `ItemList` on the hub. Per `jay-domain-skills:structured-data-jsonld`. **Only emit `offers.price` when we have a sourced, current figure — else omit price, keep `url`+`availability`.**
- **Crawlability:** baked HTML, one H1/page, clean slugs (`/events/summerslam-2026/`), dense internal links to wrestler/match/rivalry pages (the site's mesh), breadcrumb, added to `sitemap.xml` + `search-index.js` + `/content/*.md` mirror + `llms.txt`. Per `jay-domain-skills:crawlable-by-design`.
- **Answer-first copy** on every event page (the extractable one-liner) + FAQ = AI-citation ready. Per `jay-domain-skills:programmatic-seo-geo`.
- **URL stability:** one canonical URL per event across its upcoming→past lifecycle; no slug changes. Per `jay-domain-skills:stable-urls-and-redirects`.

---

## 9. Copy direction

- Voice: **`my-writing-style`** + **`jay-core-skills:kill-ai-tells`** on every visible string (headings, CTAs, microcopy, empty/loading states, FAQ, schema descriptions, a11y labels). No em-dashes if that's the house rule; specific over generic.
- Conversion without dark patterns: **`jay-domain-skills:calm-conversion`** — real countdowns (to real on-sales) not fake urgency; "notify me" not "LIMITED SPOTS"; honest scarcity only.
- CTA ladder (example, to be voiced by the copy agent): primary "Get tickets" (out) · capture "Alert me when WWE's in [city]" · premium "Ringside & travel (official)."
- Trust/earned-authority: **`jay-domain-skills:earned-authority`** — the page states plainly it's a fan guide, links official sellers, and shows sourced "as of" dates; it never implies it *is* WWE.

---

## 10. Analytics & the funnel-readout tie-in

Fire a console/analytics intent event on every capture and every outbound click: `notify_city_submit`, `presale_optin`, `reminder_set`, `waitlist_join`, `price_watch`, `rsvp_going|watching`, `talent_follow`, `outbound_click{seller,event}`. These feed the site's existing **membership funnel-readout** concept (waitlist growth, email/SMS list growth, opt-in→member conversion, alert CTR to partner, per-segment outbound clicks) — the weekly-readout duty the WWE role names. Per `jay-domain-skills:privacy-first-analytics` (no PII in analytics payloads; email/phone stay in the backend, not the tag).

---

## 11. Success criteria (definition of done for the page)

- Renders fully **without JS**; live search + capture enhance on top.
- 0 broken internal links; valid JSON-LD on every template; sitemap/search-index/llms.txt updated.
- Every price figure sourced + `[VERIFY]`-checked at build; no fabricated numbers; FTC disclosure adjacent; all-in pricing where shown.
- Every capture writes one clean segmented record; every intent fires one analytics event.
- Mobile 360px clean, AA contrast, reduced-motion safe.
- One canonical URL per event; lifecycle flag switches template without redirects.
