# Session summary — Events & Tickets planning (2026-07-27)

**Type:** research + architecture planning. **No code shipped** (by design — this session produces the plan to approve before building).

## What was produced
- `data/research-wwe-ticketing.md` — sourced research brief (WWE ticketing ecosystem, presales, On Location/TKO, secondary market + affiliate, Discovery API, real 2026–27 calendar, niche UX modules, compliance guardrails).
- `docs/design/events-ticketing-page.md` — full design spec for the `/events/` upcoming + ticketing surface (anatomy, 12 modules, hybrid data, CRM capture, design-system fit, SEO/GEO, copy, analytics).
- `docs/design/homepage-next-event-module.md` — the front-page "Next Event + search your city" block.
- `docs/design/events-ticketing-master-brief.md` — the multi-agent build plan (schema, file plan, 5 build waves, skill invocations, verification gates, interview pitch).

## Decisions locked (owner sign-off, 2026-07-27)
1. **Hybrid data** — baked `events.json` → build script → static crawlable HTML, PLUS a live "find WWE near me" layer via the free Ticketmaster Discovery API. *Rejected:* baked-only (loses real city search), live-API-first (kills the site's SEO/GEO crawlability thesis).
2. **WWE-first, extensible** — real data/narrative are WWE; `promotion` field lets AEW/TNA/NJPW slot in later. *Rejected:* all-promotions-now (4x data upkeep, dilutes the WWE-job story).
3. **Primary CTA = owned-channel capture, framed as the Club WWE funnel.** *Rejected:* outbound-clicks-first (leaves the membership-growth demonstration — the whole point — on the table).

## Key discoveries / traps
- **Club WWE launched this week** ($99/yr, includes early ticket access) — almost certainly the "new digital membership product + growing waitlist" in the job posting. Reframes the whole site as the funnel that feeds it. Exact ticket-access mechanics still [VERIFY].
- **On Location = wholly-owned TKO subsidiary** (same parent as WWE, acq. Feb 28 2025) — linking it = pointing fans at the employer's own premium funnel. Strongest trust/tie-in.
- **"Amex/AXS/credit-card" resolved:** WWE's recent presale partner was **Chase Freedom** (passcode = phone # on card), not Amex; **AXS** is AEG's ticketing platform, not a credit card.
- **Ticketmaster is NOT universal** — channel varies by market (US = Ticketmaster/On Location; Saudi = webook; Australia = Ticketek; Europe = local TM). The per-market "how to attend" map is the page's most honest, defensible utility.
- **Discovery API** is free but you may **not monetize the API itself** (route purchases via affiliate) and the **key must be proxied server-side** (never in the static repo). Redirect-to-TM + limited caching + privacy disclosure required.
- **Dynamic pricing** → never hard-code a price; sourced "from $X, as of [date]" or omit. FTC: affiliate disclosure adjacent + all-in pricing.

## Exact next steps
1. Owner approves the master brief.
2. **Wave 0 (backend-first): author `data/events.json` + stand up the Supabase `signup` table** (RLS insert-only, double opt-in) + the `tm-search`/`signup` serverless functions. This is the next hard backend task — offered to take it.
3. Waves 1→4 per the master brief (static build → interactive → quality passes → verify).

## Stack / approach notes (for future sessions)
- Static hand-authored HTML + `build_*.py` marker-injection (same pattern as `build_events_11.py`, `build_ring_feed.py`) for the baked layer; `js/events-nearby.js` + serverless key-proxy for the live layer; Supabase for capture (MCP already connected, previously unused). Reuse existing components (`ev-hero`, `event-grid`, `ev-tile`, `meta-chips`, `faq-block`); new CSS namespaced + additive. Edit components/build sources, never baked/stamped output.

## CHANGELOG line to append
`- Events & Tickets: research + build plan. 4 planning docs (research brief, page spec, homepage-module spec, multi-agent master brief). Locked hybrid data (baked events.json + live Ticketmaster Discovery API), WWE-first/extensible, owned-channel capture framed as the new Club WWE funnel. Backend-first next: events.json + Supabase signup table.`
