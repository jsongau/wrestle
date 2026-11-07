# Design Spec — Homepage "Next Event + Search Your City" module

**Status:** design spec, pending build. **Scope:** one homepage block (`index.html`) that (a) showcases the **next upcoming WWE event** and (b) lets a fan **search events by their city** — the top-of-funnel hook that feeds the full `/events/` surface and the owned-channel/Club WWE funnel.
**Companion:** `docs/design/events-ticketing-page.md` (full page), `data/research-wwe-ticketing.md` (facts), master brief (build plan).

---

## 1. Purpose & why it earns a homepage slot

The homepage is the site's highest-traffic surface. A live "next event + find it near you" block converts anonymous visitors into **segmented owned-channel contacts** at the moment of peak intent, and routes them into `/events/`. It maps to the WWE role's core: **owned-channel acquisition + geo/interest segmentation.** It earns the slot because it moves **acquisition, engagement, and (via capture) retention** — not cosmetics.

Guardrail: this is **one block**, not a new tab (per `jay-domain-skills:nav-budget-guard`). It reuses the existing 12-block homepage system, nav7 header, and self-gated JS conventions from the v3 homepage build.

---

## 2. Placement

Slot it **high — directly beneath the hero / Ring Feed**, above the evergreen "five-star club / roster" blocks. Rationale: intent-to-attend is time-sensitive and news-like (belongs near the top with the Ring Feed), while encyclopedia content is evergreen (belongs below). Namespaced CSS (`.hv3` family) and self-gated JS as established; injected between `<!-- NEXT-EVENT:START -->` / `<!-- NEXT-EVENT:END -->` markers via the build script (same pattern as `build_ring_feed.py`), so `apply_shell.py` and the rest of the page are untouched.

---

## 3. Anatomy (three parts, mobile-first)

**Part 1 — Next-Event spotlight (baked, instant paint)**
- The single next PLE from `data/events.json` (today: **SummerSlam · Sat–Sun Aug 1–2, 2026 · U.S. Bank Stadium, Minneapolis**).
- Elements: brand/logo lockup, **live countdown** (JetBrains Mono; to event; and a smaller "next on-sale" clock when relevant), `meta-chips` (date · venue · city), on-sale status pill, and a button row:
  - Primary (out): **"Get tickets"** → Ticketmaster (affiliate-wrapped).
  - Secondary (capture): **"Alert me"** → email/SMS opt-in scoped to this event.
- Baked so it paints with zero JS and is crawlable; countdown is a JS enhancement that degrades to a static date.

**Part 2 — "Find WWE near your city" (hybrid)**
- One input (city or ZIP) + optional radius, one button: **"Find events near me."**
- On submit (JS present): calls the Discovery API layer (`js/events-nearby.js`) → renders up to ~5 result cards (name · date · venue · city) each linking **out** to the Ticketmaster `url`.
- **No results near you?** → the field morphs into the capture: **"No WWE dates near [city] yet — get notified when they announce one."** (email → `home_market` pre-filled). Never a dead end (Bandsintown pattern).
- **No-JS / SEO fallback:** the input is a real GET to `/events/tickets/?city=…`, which renders the **baked** upcoming list filtered by state/market. So the feature works, and is indexable, even without JS.

**Part 3 — Upcoming rail (baked)**
- A compact horizontal rail of the next 3–4 events (`ev-tile` mini variant), each → its `/events/{slug}/` attend page, ending in a **"All upcoming events →"** link to `/events/`.

---

## 4. Data source

- **Baked:** the build script reads `data/events.json`, picks `status:upcoming` sorted by date, and injects Part 1 (next event) + Part 3 (rail) as static HTML. Re-run on data change; never hand-edit the baked block.
- **Live:** Part 2's city search uses the same `js/events-nearby.js` + serverless key-proxy as the `/events/` page (built once, reused). Shares caching + affiliate wrapping. Graceful fallback to the baked filtered list.

---

## 5. Capture & CRM payload

The module writes the same `signup` record as the events page (single source of truth — see events-ticketing-page.md §6 and the master brief DDL). Homepage-specific defaults:
- `source = home_next_event` (spotlight "Alert me") or `home_city_search` (city notify-me).
- `home_market` (from the city field), `radius_pref`, `brand_interest` defaults to `[ple]` for the spotlight, inferred from search context otherwise, `event_id` set for the spotlight opt-in.
- `intent = notify_city | reminder`. Double opt-in, insert-only, honeypot + rate-limit, no browser storage.

This single block therefore seeds the geo × interest segmentation on the highest-traffic page — the cleanest possible top-of-funnel for the membership-growth story.

---

## 6. Design-system fit & states

- Reuse `ev-tile`, `meta-chip`, `countdown` (shared with the events page), `wrap`, section header pattern; new markup namespaced under `.hv3-next` and self-contained in `css/site.css` (additive). Match "Broadcast Bold": arena tones, gold for premium, red for live/on-sale.
- **States to design:** default (baked next event) · countdown ticking · search loading (skeleton) · search results · **no-results → capture** · capture success ("You're on the list — check your email to confirm") · error (API down → "Search is catching its breath; browse all upcoming events →"). Every state has copy (below) and a no-JS equivalent.
- **A11y/perf:** labelled input, ≥44px targets, 16px font (no iOS zoom), visible focus, `aria-live` on the results region, reduced-motion disables countdown flips; live JS lazy-loaded; baked parts paint first (protect LCP/CLS). Per `jay-domain-skills:accessible-by-default`.

---

## 7. Copy (voice: `my-writing-style` + `kill-ai-tells`; conversion via `calm-conversion`)

Direction only — the copy agent voices final strings and runs the self-check:
- Section label: something like **"Next stop"** / **"WWE near you"** (not "Upcoming Events Widget").
- Spotlight: real countdown + "Get tickets" / "Alert me" — no fake urgency.
- City search placeholder: "Your city or ZIP." Button: "Find events near me."
- No-results (the important one): honest + useful, e.g. "Nothing near [city] yet. We'll email you the day WWE books it." 
- Success: confirm the double opt-in step plainly.
Avoid: "Don't miss out!", countdown timers to nothing, "LIMITED SPOTS." Honesty converts better here and protects the recruiter-facing trust bar.

---

## 8. Analytics

Fire intent events: `home_nextevent_view`, `home_ticket_click{event}`, `home_alert_optin{event}`, `home_city_search{market}`, `home_city_notify{market}`. No PII in payloads (`jay-domain-skills:privacy-first-analytics`). Feeds the same funnel-readout as the events page so homepage vs page capture can be compared (an A/B/segmentation story for the interview).

---

## 9. Build notes

- Add build step (extend the upcoming-events build script or a small `build_next_event.py`) that injects Parts 1 + 3 between the homepage markers. Register the markers in the homepage; keep `index.html` out of `apply_shell.py`'s stamp exclusions as already configured.
- Reuse — do not fork — `js/events-nearby.js` and the `countdown` component from the events page. One implementation, two mount points.
- Verify: renders with JS off (baked next event + rail visible, city field is a working GET); countdown correct in America/Chicago and the viewer's locale; no horizontal scroll at 360px; 0 new broken links; homepage JSON-LD still valid.
