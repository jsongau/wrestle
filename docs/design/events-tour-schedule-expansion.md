# Build Spec — Tour & Schedule Expansion + the Interactive Year Tour Map

**Status:** design/build spec, pending a multi-agent build. Extends the live `/events/tickets/` page.
**Companions:** `data/research-wwe-ticketing.md`, `docs/design/events-ticketing-page.md`, `-conversion-ux.md`, `-master-brief.md`, `homepage-next-event-module.md`.
**Last researched:** 2026-07-28. Dynamic facts (schedules, on-sale dates) are pulled live at build/runtime — this spec fixes the *system*, not a frozen calendar.

---

## 0. TL;DR

Grow `/events/tickets/` from "the big Premium Live Events" into **the full live-wrestling calendar** — WWE's weekly grind (Raw, SmackDown, NXT, house shows) plus the other promotions that ride the same ticketing rails (AEW, TNA, then NJPW/ROH/MLW). Anchor it with a **cool, interactive year-long tour map** that both a *local* ("tell me the day they announce a date in my city") and a *road-tripping superfan* ("show me the whole tour snaking across the country so I can plan around it") will bookmark. Every date links **out** to the seller; every "notify me" and "follow the tour" is an **owned-channel capture** stamped with geography — the exact national geo × interest CRM the WWE Membership-Growth role is about.

---

## 1. Why this exists (two audiences, one funnel)

- **The local.** 90% of fans never travel for wrestling — they wait for it to come to *them*. WWE runs Raw/SmackDown/house shows through ~100+ US markets a year, but a fan in Boise has no idea when the caravan is near. "**Notify me the day WWE announces a date within 75 miles of [my city]**" is the single highest-intent, highest-frequency owned-channel capture on the whole site (Bandsintown's entire business is this). It fires far more often than the ~14 PLEs/year.
- **The traveler.** A real segment plans trips *around* the tour — WrestleMania week, a SummerSlam weekend, or "which shows are on my July drive from Chicago to Denver." Serve them a **route/trip view** and a "follow the tour" subscription, and you capture the highest-LTV, highest-affinity fans on the site (and the ones most likely to buy On Location travel packages).
- **The job.** This is geographic CRM at national scale: segment by `home_market`, `radius`, `promotion_interest`, `travel_intent`. A live map that captures a segmented email in every metro in America is the artifact that makes "Manager, Membership Growth" undeniable.

---

## 2. Scope — promotions & show types (tiered, extensible)

The data model carries a `promotion` and `show_type` field so this scales without rework (the existing events model already reserved `promotion`).

**Promotions (by tier — build T1+T2 first):**

| Tier | Promotion | Ticketmaster attraction | Also on | Touring model |
|---|---|---|---|---|
| **T1** | **WWE** | `807358` | (AXS at AEG venues; webook Saudi; Ticketek AU) | Raw (Mon), SmackDown (Fri), NXT (Tue, mostly Orlando PC), house shows (weekends), PLEs. Named seasonal tours. |
| **T2** | **AEW** (Dynamite & Collision, PPVs) | `3168538` | AXS (`1106925`) | Dynamite (Wed) + Collision (Sat), frequently combined 2-day tapings touring cities; PPVs. |
| **T2** | **TNA** | `1008830` | AXS (`1100545`) | Weekly tapings + PPVs; TNA published a full 2026 live-events schedule. |
| **T3** (extensible, `[VERIFY]` per event) | NJPW (US/Strong), ROH, MLW, GCW, indies | varies | AXS / venue box office / promotion sites | Sporadic US dates; populate later. |

**Show types (`show_type`):** `ple` (Premium Live Event / PPV) · `tv` (Raw/SmackDown/Dynamite/etc. broadcast taping) · `house` (non-televised live event) · `special` (SNME, Worlds Collide, King/Queen of the Ring, festival). Each renders with a distinct pin size/weight on the map and a distinct badge.

**Brand sub-filter (WWE):** `raw` · `smackdown` · `nxt` · `house` · `ple`.

---

## 3. Research findings (sourced 2026-07-28)

- **WWE weekly TV tours city-to-city** and bundles dates into named seasonal tours — e.g., the **"2026 Road to WrestleMania Tour"** and the **"2026 Summer Tour"** — announced in batches (10–11 dates at a time), with venues co-announcing. Great editorial framing: the year has *chapters* (tour legs), not just isolated dates. ([WWE — Road to WrestleMania Tour dates](https://www.wwe.com/article/wwe-announces-11-new-dates-for-raw-and-smackdown-as-part-of-2026-road-to-wrestlemania-tour) · [WWE — Summer Tour dates](https://www.wwe.com/article/wwe-announces-10-new-live-event-dates-as-part-of-2026-summer-tour))
- **House shows are back** (non-TV live events touring, family-priced) — a whole additional layer of dates in secondary markets. ([SI — house shows comeback + pricing](https://www.si.com/fannation/wrestling/wwe/update-on-wwe-house-shows-making-a-comeback-and-ticket-pricing))
- **All three majors sell on Ticketmaster** by attraction ID (WWE `807358`, AEW `3168538`, TNA `1008830`), and **AEW + TNA also list on AXS.** This is the key: **the Ticketmaster Discovery API keyed by attraction ID returns a promotion's entire upcoming slate** — date, venue name, city/state, lat-long, on-sale, and the ticket URL — which is exactly the feed the map needs. ([WWE on TM](https://www.ticketmaster.com/wwe-tickets/artist/807358) · [AEW on TM](https://www.ticketmaster.com/aew-dynamite-collision-tickets/artist/3168538) · [TNA on TM](https://www.ticketmaster.com/tna-wrestling-tickets/artist/1008830) · [AEW on AXS](https://www.axs.com/teams/1106925/aew-tickets) · [TNA on AXS](https://www.axs.com/teams/1100545/tna-wrestling-tickets) · [TNA full 2026 schedule](https://tnawrestling.com/news/tna-wrestling-releases-its-full-2026-live-events-schedule))
- **On-sale cadence** (from the prior research brief): weekly-TV/house dates run a presale (often Thursday) → public on-sale (often Friday) 10am local; PLEs run credit-card/registration presales days ahead. Announce-to-on-sale lead time is usually 1–4 weeks — the window the notify-by-city alert lives in.
- **Weekly-TV broadcast homes** (unchanged): Raw → Netflix, SmackDown → USA, NXT → The CW; PLEs → ESPN (US) / Netflix (intl). Broadcast home does not change how the *taping ticket* is bought.

**Sources:** WWE.com tour announcements, SI, Ticketmaster + AXS attraction pages, tnawrestling.com — full list in §14.

---

## 4. THE STAR FEATURE — the interactive year tour map ("The Road")

A dark, arena-lit **map of the whole touring year** you can scrub, filter, and personalize. This is the bookmark-worthy, screenshot-worthy centerpiece.

### 4.1 Core concept
A stylized US map (with an international toggle) where every date on the calendar is a **glowing pin**, color-coded by promotion and sized by show type. A **timeline scrubber** runs the year; pressing **play** animates the tour *traveling* — pins light up in date order and a thin route line threads city to city, so you literally watch the caravan cross the country month by month. That "press play and watch the tour move" moment is the delight; everything else is utility hung off it.

### 4.2 Views (one dataset, four lenses)
1. **Map** (default, desktop) — pins on the US map; scrub/play the year; hover/tap a pin → event card.
2. **Route / Trip** (the traveler view) — pick a date range and/or two cities (a corridor); the map highlights shows that fall in that window/along that route; "**3 shows on your Jul 10–17 window**"; add-to-trip + calendar export. This is the road-tripper's planner.
3. **Near me** — "Set your city" drops a home pin + radius ring; the list re-sorts to nearest-first; "**Next show near you: Raw · 42 mi · Sep 14**." Empty → notify-me capture.
4. **Calendar / list** (accessibility + crawlable + no-JS default) — the same dates as a filterable, chronological list grouped by month and tour leg. This is the baked, indexable representation the map enhances.

### 4.3 Filters & framing
- **Promotion:** WWE · AEW · TNA (+ T3 when populated). Multi-select, color-legended.
- **Show type:** PLE · TV · House · Special (toggle chips).
- **WWE brand:** Raw · SmackDown · NXT.
- **Month** scrubber + **tour-leg chapters** ("Road to WrestleMania Tour," "Summer Tour") as labeled segments on the timeline — editorial storytelling over raw dates.
- **Region:** US · International layer (Saudi / UK / Europe / Australia) for the global follower.

### 4.4 Pin → event card (the conversion moment)
Tap/hover a pin: date · venue · city · promotion + show badge · on-sale status pill · **Get tickets** (out, affiliate-wrapped) · **Notify me** (capture, city pre-filled) · for premium-eligible dates, **Official ringside · On Location**. Same honesty rails as the main page (no fabricated prices; presale = "reminder"; affiliate disclosure adjacent).

### 4.5 States (design every one)
Default (baked year) · loading (skeleton map + list) · filtered · **empty region → notify-me** · hover/focus pin · play/scrub · reduced-motion (no travel animation; static pins + list) · error/API-down (fall back to baked list, keep captures) · no-JS (the calendar/list is the page).

### 4.6 The "cool" bar (luxury-editorial, not a gimmick)
Apply `jay-domain-skills:luxury-editorial-design`: dark near-black canvas, championship-gold WWE pins, restrained motion, a thin gold route line, tasteful glow, editorial month labels — a broadcast **telemetry** feel (the site's "Control Room" language), not a rainbow Google-My-Maps. Restraint is the premium signal. Every animation is `prefers-reduced-motion`-gated and never gates content visibility (the v2 reveal-bug lesson: motion adds, never hides).

---

## 5. Data model

### 5.1 Extend the event record (`data/events.json` → generalize to `data/schedule.json`)
```json
{
  "slug": "raw-2026-09-14-boston",
  "promotion": "wwe",            // wwe | aew | tna | njpw | ...
  "show_type": "tv",             // ple | tv | house | special
  "brand": "raw",                // raw | smackdown | nxt | dynamite | collision | null
  "name": "Monday Night Raw",
  "tour_leg": "2026 Road to WrestleMania Tour",   // editorial chapter (nullable)
  "date": "2026-09-14", "time_local": "19:30",
  "venue": "TD Garden", "city": "Boston", "region": "MA", "country": "US",
  "geo": {"lat": 42.3662, "lng": -71.0621},
  "onsale": {"status": "on_sale", "public_onsale": "2026-08-01", "presales": [...]},
  "sellers": {"primary": {"name":"Ticketmaster","url":"...","affiliate":true},
              "premium": {"name":"On Location","url":"...","official":true}},
  "tm_attraction": "807358", "tm_event_id": "...",
  "price": {"from": null, "verify": true},
  "source": "discovery_api", "as_of": "2026-07-28", "sources": ["..."]
}
```
- **PLEs keep their richer record** (the existing events); TV/house dates are lighter, mostly Discovery-API-sourced.
- `tour_leg` powers the timeline chapters and per-tour pages.
- **Never fabricate a date or price** — every row traces to the Discovery API (or an official announcement) with `as_of`.

### 5.2 The feed (hybrid, per the locked pattern)
- **Baked snapshot** (crawlable, no-JS, SEO): a nightly job hits the Discovery API per attraction ID, writes `data/schedule.json`, and a build script bakes the calendar/list + city pages + the map's default dataset into static HTML.
- **Live layer:** the map/near-me/route views call the Discovery API through the existing server-side proxy (`/api/tm-search`, extended to `/api/tm-tour?attraction=807358&geoPoint=…`) for freshness; degrade to the baked snapshot on failure.

---

## 6. Information architecture & routing

Per `jay-domain-skills:nav-budget-guard` (route into Events, never widen the top bar) and `programmatic-seo-geo` (the long-tail is the prize):

```
/events/tickets/            existing page — add the tour map + "this week" strip near the top
/events/tour/               THE tour map hub (all promotions, the full year, all four views)
/events/tour/wwe/           per-promotion tour pages (wwe / aew / tna)
/events/schedule/           the flat, filterable calendar/list (map's crawlable twin)
/events/in/{city-slug}/     ★ programmatic CITY pages — "WWE & wrestling in Boston: 2026 schedule & tickets"
```

**The city pages are the SEO engine.** "wrestling in [city]", "WWE tickets [city]", "when is WWE in [city]" is enormous, high-intent, recurring long-tail. One template × every touring metro = hundreds of crawlable pages, each: the city's upcoming dates (all promotions), the venue(s), how to buy, a `notify-me-[city]` capture, and a `SportsEvent`/`ItemList` schema block. This is exactly the programmatic-SEO play the site is built for — and each page is a geo-segmented capture funnel. (Guard against thin pages: only generate a city page when it has ≥1 real upcoming or recent date; otherwise it 404s or redirects to `/events/tour/`.)

---

## 7. Locals + travelers — the capture & retention features

All write to the existing `signup` table (one record, progressive profiling); all honor the corrected conversion/UX spec (email-first, one primary ask per surface, no phantom access).

- **Notify me when [promotion] is near [city]** — the flagship. `home_market` + `radius` + `promotion_interest[]` + `show_type_interest`. Fires when a new date lands in the subscriber's radius (the highest-frequency, highest-intent trigger on the site).
- **Follow the tour** — subscribe to a whole tour leg's updates ("Road to WrestleMania Tour"); a season-long nurture, the retention centerpiece.
- **Trip planner / route mode** — "shows on my [dates] in [region]"; add-to-trip; **export the whole trip to calendar (.ics)**; distant-city planning flags `travel_intent` → On Location / hospitality nurture.
- **Set your home city** — one stored `home_market` (URL-param-carried per the no-storage rule) personalizes every surface; enables geo-triggered sends without re-asking.
- **"This week in wrestling" strip** — a compact, always-fresh row on `/events/tickets/` and the homepage module: the next 3–5 dates anywhere, "and near you: …".
- **Follow a promotion / brand** — Raw-only vs SmackDown vs AEW segmentation.

---

## 8. Tech & design-system fit

- **Map rendering:** a **custom stylized SVG US map** (state paths + an equirectangular/Albers projection helper to place lat-long pins) is preferred over a tiled map lib — no API key, fast, fully on-brand (dark arena look), crawler-friendlier, and it makes the "play the tour" route animation trivial to draw as an SVG path. An international view uses a simple world SVG. (If a true pan/zoom slippy map is ever wanted, MapLibre GL with a dark style is the fallback — but gate panning to two-finger on mobile and never let it trap page scroll.)
- **Perf/CLS:** reserve the map's aspect-ratio; the baked list paints first; the map + live layer lazy-load (facade). Target the site's LCP < 2.5s / CLS ~0.
- **A11y (`jay-domain-skills:accessible-by-default`):** the calendar/list is the semantic source of truth — every pin has a keyboard-focusable, labeled list twin; `aria` on the map region; color never the only signal (promotion = color **+** legend label + pin shape); the play animation is reduced-motion-gated; full no-JS render.
- **Design system:** reuse the `.tix`-scoped tokens/components from the shipped page; new components (`tourmap`, `tour-timeline`, `route-panel`, `city-strip`) namespaced + additive; JetBrains-Mono telemetry labels; gold reserved.

---

## 9. SEO / GEO

- **City pages** (§6) = the long-tail engine; one H1/page, answer-first ("WWE's next date in Boston is Monday Night Raw on Sept 14, 2026 at TD Garden…"), `SportsEvent` + `ItemList` + `BreadcrumbList` + `FAQPage` schema, dense internal links (city ↔ promotion tour ↔ venue ↔ nearby cities), added to `sitemap.xml` + `llms.txt` + the markdown mirror. Per `programmatic-seo-geo` + `structured-data-jsonld` + `crawlable-by-design`.
- **URL stability** (`stable-urls-and-redirects`): city slugs are canonical and permanent; a metro with no current dates redirects to `/events/tour/`, never 404-churns.
- **Freshness signal:** the nightly rebake gives Google constantly-updated dates — a strong recurring-crawl signal.

---

## 10. Backend / data pipeline

- **`/api/tm-tour`** (extends `tm-search`): server-side Discovery API proxy, key hidden, per-attraction queries (`attractionId=807358`, date-range, optional `geoPoint`+`radius`), affiliate-wrapped URLs, cached within TM terms.
- **Nightly refresh:** a scheduled job (Vercel Cron / GitHub Action) pulls all attraction IDs → writes `data/schedule.json` → runs the build script → commits/deploys (or writes to a store the baked pages read). Respects TM caching/takedown terms.
- **Notify-by-city trigger:** on refresh, diff new dates against `signup` rows; queue geo-matched alerts (ties directly into the Supabase `signup` table + confirm-email sender already specced in the master brief). This is where the tour data and the membership funnel finally close the loop.

---

## 11. Honesty & compliance (every agent honors)

Never fabricate a date, venue, or price. Live/`as_of`-dated data only; `[VERIFY]` anything not from the API or an official announcement. Affiliate disclosure adjacent to ticket links; all-in or labeled pricing if shown; presale = "reminder," never a code. Respect Ticketmaster API terms (redirect to seller, limited caching, 24h takedown, privacy disclosure, no reselling access). Cross-promotion accuracy: don't imply WWE endorses the site (fan guide), and don't misattribute AEW/TNA dates.

---

## 12. Monetization & moat

- **Affiliate across all promotions** (Impact/Partnerize/CJ/FlexOffers) — more promotions × more dates = more qualified outbound clicks.
- **The moat** (`jay-domain-skills:moat-and-flywheel`): a live, national, multi-promotion tour map + a geo-segmented notify list is a **data + utility moat** — the more subscribers per metro, the better the "demand map," the more valuable the alerts, the stickier the site. No single promotion's own site does cross-promotion "wrestling near me."
- **The pitch:** "I built the owned-channel engine that turns every one of ~100 US markets into a segmented list, and alerts each fan the day the tour hits their town. Here's the map, the schema, and the trigger."

---

## 13. Multi-agent build plan (waves)

Build T1+T2 (WWE/AEW/TNA); T3 later. Suggested roster:

- **Wave 0 — Data & backend:** author the extended `schedule.json` schema; build `/api/tm-tour` + the nightly refresh; extend the Supabase `signup` schema for `promotion_interest`/`show_type_interest` + the geo-match trigger.
- **Wave 1 — The map widget:** the SVG US map + projection, pins, timeline scrubber + play animation, filters, the four views (Map/Route/Near-me/List), event cards. (Highest craft — pair with `luxury-editorial-design` + `accessible-by-default`.)
- **Wave 2 — City pages + schedule page:** the programmatic `/events/in/{city}/` template + `/events/schedule/` + per-promotion `/events/tour/{promo}/`; schema; sitemap/llms/markdown mirror.
- **Wave 3 — Capture & retention:** notify-by-city, follow-the-tour, trip planner + .ics, set-home-city; wire to `signup`.
- **Wave 4 — Copy pass** (`my-writing-style` + `kill-ai-tells` + `conversion-first-copy`) and **SEO pass** (`programmatic-seo-geo` + `structured-data-jsonld`).
- **Wave 5 — Verify:** Playwright renders (map + no-JS list + mobile), link check, JSON-LD validate, fact/freshness audit (`source-verification`), a11y (`responsive-accessibility-review`).

---

## 14. Open decisions for sign-off (before the build)

1. **Map tech:** custom SVG US map (recommended — on-brand, no key, animatable) vs a tiled map lib (MapLibre). 
2. **Promotion scope at launch:** WWE-only first, or WWE+AEW+TNA together (recommended — the cross-promotion "wrestling near me" is the differentiator).
3. **City-page threshold:** min dates to generate a city page (recommended: ≥1 upcoming within ~120 days, else redirect).
4. **Refresh cadence & host:** nightly Vercel Cron vs GitHub Action; commit-to-repo vs a data store.
5. **International:** include the global layer at launch or US-first.

---

## Sources
- WWE tours: wwe.com/article/wwe-announces-11-new-dates-for-raw-and-smackdown-as-part-of-2026-road-to-wrestlemania-tour · wwe.com/article/wwe-announces-10-new-live-event-dates-as-part-of-2026-summer-tour · americanarenas.com/sports/wwe/schedule · itnwwe.com/wrestling/wwe-live-events-schedule-calender
- House shows: si.com/fannation/wrestling/wwe/update-on-wwe-house-shows-making-a-comeback-and-ticket-pricing
- Ticketmaster attractions: ticketmaster.com/wwe-tickets/artist/807358 · ticketmaster.com/aew-dynamite-collision-tickets/artist/3168538 · ticketmaster.com/tna-wrestling-tickets/artist/1008830
- AXS: axs.com/teams/1106925/aew-tickets · axs.com/teams/1100545/tna-wrestling-tickets
- TNA schedule: tnawrestling.com/news/tna-wrestling-releases-its-full-2026-live-events-schedule · pwmania.com/tna-wrestling-announces-full-2026-live-events-schedule
- Discovery API mechanics + prior ticketing facts: see `data/research-wwe-ticketing.md`
