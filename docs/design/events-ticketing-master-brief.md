# Master Brief — "Events & Tickets" multi-agent build

**Project:** Wrestle Lore (internal MAT) · WWE/TKO Manager-of-Membership-Growth portfolio piece.
**This brief orchestrates a multi-agent build** of the `/events/` "Upcoming & Tickets" surface + the homepage "Next Event" module, per the two design specs and the research brief in this folder.
**Author gate:** this is the plan to approve **before** building (the build touches a database, adds an API/serverless call, and spans multiple pages — so per the owner's standing rule, plan first). Nothing here deploys until the owner confirms repo + Vercel project + git remote.

---

## 0. Locked decisions (from 2026-07-27 sign-off)

1. **Data = hybrid.** Baked `data/events.json` → build script → static crawlable HTML (authority), **plus** a live "find WWE near me" layer via the free **Ticketmaster Discovery API** (delight), degrading gracefully to the baked list.
2. **Scope = WWE-first, extensible.** Real data + narrative are WWE; the data model carries a `promotion` field so AEW/TNA/NJPW slot in later with no rework.
3. **Primary CTA = owned-channel capture, framed as the Club WWE funnel.** "Notify me when WWE comes to my city" + presale alerts → email/SMS → a segmented list that mirrors and demonstrates the Club WWE membership funnel (WWE's real $99/yr product, launched this week).

---

## 1. Architecture overview (data flow)

```
                    ┌──────────────────────────────────────────┐
 SOURCE OF TRUTH    │  data/events.json   (curated, sourced)    │
                    └───────────────┬──────────────────────────┘
                                    │  build_events_upcoming.py  (+ build_next_event.py)
                                    ▼
 BAKED / CRAWLABLE   /events/ hub · /events/{slug}/ attend pages · homepage next-event block
   (static HTML)     road-timeline · attend-map · price-row (sourced "as of" figures)
                                    │
 LIVE ENHANCEMENT    js/events-nearby.js ──► /api/tm-search (serverless key-proxy)
   (progressive)                                  └──► Ticketmaster Discovery API (keyword=WWE + city/geo)
                                    │                        returns name/date/venue/url → link OUT (affiliate)
                                    ▼
 OWNED CAPTURE        capture forms ──► /api/signup (serverless) ──► Supabase `signup` table
   (the product)         (double opt-in, RLS insert-only)         └──► analytics intent events (no PII)
                                    ▼
 SEGMENTATION         geography × event-interest × intent × channel  →  funnel-readout page (KPIs)
```

Two serverless functions (Vercel Functions or Supabase Edge Functions — pick one runtime, the repo already has Supabase MCP connected but unused): `tm-search` (hides the TM API key, attaches affiliate params, caches within TM limits) and `signup` (validates + writes the capture, triggers double opt-in email). The static site stays static; these are the only backend surface.

---

## 2. Backend-first: schema & API (build/approve before any UI)

### 2.1 `signup` table (Supabase Postgres)
```sql
create table public.signup (
  id                uuid primary key default gen_random_uuid(),
  created_at        timestamptz not null default now(),
  email             text not null,
  phone             text,
  channel_pref      text[] not null default '{email}',      -- email|sms
  home_market       text,                                   -- "Minneapolis, MN"
  home_geo          text,                                   -- geohash (optional)
  radius_pref       int  default 75,                        -- miles
  brand_interest    text[] default '{}',                    -- raw|smackdown|nxt|ple|houseshow
  followed_talent   text[] default '{}',                    -- wrestler slugs
  promotion         text  default 'wwe',                    -- extensibility
  event_id          text,                                   -- nullable, for event-scoped opt-ins
  intent            text not null,                          -- notify_city|presale|reminder|waitlist|price_watch|rsvp_going|rsvp_watch
  attend_intent     text default 'unknown',                 -- going|watching|unknown
  budget_band       text,
  target_price      numeric,                                -- for price_watch
  source            text,                                   -- module id
  utm               jsonb,
  consent_marketing boolean not null default false,
  consent_ts        timestamptz,
  double_optin_confirmed_at timestamptz,
  optin_token       uuid default gen_random_uuid()
);
alter table public.signup enable row level security;
-- Insert-only from the anon key; NO select/update/delete to anon. Reads happen server-side (service role) only.
create policy "anon insert only" on public.signup for insert to anon with check (true);
```
- **Double opt-in:** `signup` inserts unconfirmed; the `signup` function emails a confirm link (`?token=optin_token`) → a confirm function stamps `double_optin_confirmed_at`. Only confirmed rows are marketable (CAN-SPAM / good hygiene, and the honest bar the site holds).
- **Anti-abuse:** honeypot field, per-IP rate limit in the function, email format + MX sanity check, no PII in client analytics.
- **Segmentation views** (service-role, for the readout page): counts by `home_market`, by `brand_interest`, by `intent`, waitlist volume by event, `attend` vs `watch`. These *are* the CRM segments the WWE JD names.
- Follow `jay-core-skills:ship-safely` (never commit keys), `jay-domain-skills:privacy-first-analytics`, and the Supabase advisor/`get_advisors` security pass before wiring.

### 2.2 `events.json` schema (curated source of truth)
```json
{
  "updated": "2026-07-27",
  "events": [
    {
      "slug": "summerslam-2026",
      "promotion": "wwe",
      "name": "SummerSlam 2026",
      "brand": "ple",
      "status": "upcoming",                  // upcoming|past  (flips template)
      "start_date": "2026-08-01",
      "end_date": "2026-08-02",
      "nights": 2,
      "venue": "U.S. Bank Stadium",
      "city": "Minneapolis", "region": "MN", "country": "US",
      "geo": {"lat": 44.9736, "lng": -93.2575},
      "onsale": {"status": "on_sale", "public_onsale": "2026-05-01", "presales": [
        {"type": "credit_card", "partner": "Chase Freedom", "starts": "2026-04-29"},
        {"type": "registration", "url": "https://www.wwe.com/…", "starts": "2026-04-30"}
      ]},
      "sellers": {
        "primary": {"name": "Ticketmaster", "url": "https://www.ticketmaster.com/…", "affiliate": true},
        "premium": {"name": "On Location", "url": "https://onlocationexp.com/wwe/…", "official": true},
        "resale":  [{"name":"StubHub","url":"…"},{"name":"SeatGeek","url":"…"},{"name":"TickPick","url":"…"}]
      },
      "price": {"from": null, "currency": "USD", "as_of": null, "source": null, "verify": true},
      "broadcast": {"us": "ESPN", "intl": "Netflix"},
      "answer_first": "WWE's next Premium Live Event is SummerSlam, Aug 1–2, 2026 at U.S. Bank Stadium in Minneapolis…",
      "sources": ["https://en.wikipedia.org/wiki/SummerSlam_(2026)", "https://corporate.wwe.com/about/news/2026/04-15-2026"]
    }
  ]
}
```
- **`price.from` stays `null` unless a sourced current figure exists** → the builder omits price + `offers.price` when null (no fabricated numbers; honors the site rule). `verify:true` forces a build-time re-check.
- `status:past` events reuse the existing results template (`build_events_11.py`) — one URL, lifecycle-aware.

---

## 3. File plan (what gets created / edited)

**New**
- `data/events.json` — curated upcoming (+ merge existing past editions' metadata over time).
- `build_events_upcoming.py` — bakes hub "Upcoming" zone, per-event attend pages, `road-timeline`, `attend-map`, `price-row` (marker-injection pattern).
- `build_next_event.py` (or a function in the above) — bakes homepage Parts 1 + 3 between `<!-- NEXT-EVENT:START/END -->`.
- `js/events-nearby.js` — live city search (calls `/api/tm-search`), graceful fallback.
- `js/events-capture.js` — capture forms (posts `/api/signup`), states, no browser storage.
- `api/tm-search.*` and `api/signup.*` (+ `api/optin-confirm.*`) — serverless functions.
- `/events/tickets/index.html` — optional SEO landing ("Find WWE tickets near you"), city-first.

**Edited (additive, non-breaking)**
- `events/index.html` — add the "Upcoming & Tickets" zone above the existing archive; add markers.
- `index.html` — add the homepage next-event markers + block.
- `css/site.css` — new namespaced components: `attend-map`, `priority-pass`, `presale-capture`, `road-timeline`, `price-row`, `notify-city`, `countdown`, `.hv3-next`.
- Events mega-panel (in `components/meganav.html`) — add "Upcoming & Tickets" link (edit the component, re-stamp via `apply_shell.py`; never hand-edit stamped pages).
- `sitemap.xml`, `js/search-index.js`, `/content/*.md` mirror, `llms.txt`, `robots.txt` (allow crawl), `CHANGELOG.md`.

**Never:** commit API keys; hand-edit baked marker blocks or shell-stamped headers; put version-numbered files in the repo (previews go to Downloads as `-v2/-v3`). Per `jay-domain-skills:edit-source-not-output`.

---

## 4. Build waves & agent roster

Run in waves; within a wave, agents are parallel; waves gate on the prior wave's verification. Keep each agent's scope tight and hand it the two design specs + the research brief.

**Wave 0 — Data & schema (must finish first; blocks all)**
- **Agent D0 (Data curator):** author `data/events.json` from the research brief §7; every event fully sourced; `price.from=null` unless sourced; `verify:true` where noted. Re-check dates/on-sale live at build time.
- **Agent D1 (Backend/schema):** stand up the `signup` table + RLS + double-opt-in + the three serverless functions (stubbed responses ok until keys). Run `get_advisors` security pass. **Deliver the schema for owner approval before writing UI** (backend-first rule).

**Wave 1 — Static build (baked authority)**
- **Agent B1 (Events hub + pages):** `build_events_upcoming.py` → hub "Upcoming" zone, per-event attend pages, `attend-map`, `road-timeline`, `price-row`. Lifecycle flag; reuse existing components; new CSS namespaced.
- **Agent B2 (Homepage module):** `build_next_event.py` → homepage Parts 1 + 3; markers; `.hv3-next`.

**Wave 2 — Interactive layers**
- **Agent I1 (Live search):** `js/events-nearby.js` + `/api/tm-search`; keyword=WWE + city/geo; affiliate-wrapped `url`; quota/caching/privacy compliance; graceful fallback.
- **Agent I2 (Capture):** `js/events-capture.js` + wire `/api/signup`; all module capture points; double opt-in UX; analytics intent events; no browser storage.

**Wave 3 — Quality passes (parallel)**
- **Agent Q1 (Copy):** invoke **`my-writing-style`** + **`jay-core-skills:kill-ai-tells`** + **`jay-domain-skills:conversion-first-copy`** + **`calm-conversion`**; voice every visible string + empty/loading/success/error states; run the writing self-check.
- **Agent Q2 (SEO/GEO/schema):** **`jay-domain-skills:structured-data-jsonld`** + **`crawlable-by-design`** + **`programmatic-seo-geo`**; `Event`/`SportsEvent`+`offers`, `BreadcrumbList`, `FAQPage`, `ItemList`; sitemap/search-index/content-mirror/llms.txt; internal-link mesh; canonical + lifecycle URL stability (`stable-urls-and-redirects`).
- **Agent Q3 (A11y/responsive):** the site's `responsive-accessibility-review` + `jay-domain-skills:accessible-by-default`; 360px, AA contrast, focus, reduced-motion, color-independent status, forms.

**Wave 4 — Verification (gate to done)**
- **Agent V1 (Fact/compliance):** re-verify every date/venue/price against sources; enforce no-fabrication, `[VERIFY]` resolved or omitted, FTC affiliate disclosure adjacent, all-in pricing, TM API terms; the site's `source-verification` + `production-page-audit`.
- **Agent V2 (Technical):** link check (0 broken), JSON-LD validation (0 invalid), render screenshots (1366 + 390), no-JS render, countdown correctness, capture round-trip to Supabase (test row), analytics events firing. Use Playwright (already in the toolchain).

Dependencies: D0,D1 → B1,B2 → I1,I2 → Q1,Q2,Q3 → V1,V2. (A prudent orchestration is a pipeline so each event/page flows to the next stage as it's ready, with V1/V2 as the final barrier.)

---

## 5. Truthfulness & compliance gates (every agent honors)

1. **No fabricated numbers** — prices are dynamic; publish sourced "from $X, as of [date]" or omit. (The site already deleted fabricated waitlist/rating figures; don't reintroduce them.)
2. **Resolve or omit `[VERIFY]`** — prices, On Location tiers, Club WWE mechanics, Crown Jewel 2026, Royal Rumble 2027, WM43 venue, Discovery rps, any Amex/Capital One WWE presale claim.
3. **"We don't sell tickets"** — fan-guide framing; link official/authorized sellers; not affiliated with WWE/TKO.
4. **FTC** — affiliate disclosure adjacent to ticket links; all-in pricing if a price shows.
5. **Never distribute presale codes** — guide fans to register with the official seller.
6. **Keys never in the repo**; TM terms (redirect to TM, limited caching, 24h takedown, privacy disclosure) respected.

---

## 6. Definition of done (checklist)

- [ ] `/events/` hub shows Upcoming zone + preserved Results archive; nav link added via component (no new tab).
- [ ] Per-event attend pages render; lifecycle flag flips upcoming↔past on one canonical URL.
- [ ] Homepage next-event block + city search live; both render with JS off.
- [ ] Live city search returns WWE events by city/ZIP, links out (affiliate), falls back gracefully.
- [ ] Capture writes one clean segmented row (double opt-in); test row verified in Supabase; analytics intent events fire; no PII in analytics.
- [ ] JSON-LD valid on every template; sitemap/search-index/llms.txt/content-mirror updated; 0 broken internal links.
- [ ] Every price sourced + dated or omitted; FTC disclosure present; all-in pricing where shown.
- [ ] 360px clean, AA contrast, reduced-motion safe; LCP < 2.5s, CLS ~0.
- [ ] Copy passed `my-writing-style` + `kill-ai-tells` self-check; no dark patterns.
- [ ] Screenshots (desktop + mobile + no-JS) attached as proof; `CHANGELOG.md` + a dated session summary written.

---

## 7. Monetization notes (revenue lever)

- Outbound ticket links are **affiliate-ready**: join **Impact** (Ticketmaster, Vivid, SeatGeek, StubHub Intl), **Partnerize** (StubHub US), **CJ** (TickPick — 4%/45-day), **FlexOffers** (Gametime). Wrap outbound `url`s server-side in `/api/tm-search` and in the baked links. **Confirm live rates in each dashboard; never hard-code.** FTC disclosure is mandatory and adjacent.
- On Location (TKO-owned) — no public affiliate program found; link it anyway as the **official** premium funnel and the strongest employer-aligned trust signal.
- The real monetization thesis for the portfolio is not affiliate pennies — it's proving you can **build the owned-channel engine that converts fans to paid membership** (Club WWE at $99/yr × a fraction of a huge waitlist). Say that in the interview.

---

## 8. Out of scope (follow-ups)

- SMS sending infra (Twilio/ESP) — schema + opt-in are built; wiring a real sender is a later wave.
- Full lifecycle-email templates (welcome, presale drip, on-sale reminder, sold-out→waitlist, win-back by market) — draft in `/membership/lifecycle/` next.
- Real affiliate account approvals (need a live domain + content footprint first).
- AEW/TNA/NJPW event data (model already supports `promotion`; populate later).
- WrestleMania 43 (Riyadh, 2027) dedicated pre-capture hub — high-value; spin up once travel packages are announced.

---

## 9. The interview pitch (why this exists)

> "WWE just launched Club WWE — a $99/yr membership with a growing waitlist. I built the owned-channel funnel to convert fans into members, running live on real wrestling content. The events page turns every ticket-buying intent — notify-my-city, presale alerts, sold-out waitlists — into a segmented email/SMS contact (geography × event-interest × attend-intent), the exact CRM segmentation the role calls for. Tickets link out to Ticketmaster and to On Location — your own TKO hospitality arm — while I keep the fan relationship. Here's the data model, the lifecycle, the A/B backlog, and the weekly funnel readout."

That paragraph is the job. This build makes it demonstrably true.
