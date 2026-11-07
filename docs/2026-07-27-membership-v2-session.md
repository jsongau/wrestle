# Session summary — Membership v2 rebuild

**Date:** 2026-07-27
**Scope:** Rebuild `/membership/` into an interactive signup surface; design the backend plan-first; model the Club WWE cross-sell.

## What changed and why
- Rebuilt the membership page from a static three-card brochure into a working signup surface: founder-rate lock-in, monthly/annual toggle, waitlist that doubles as message-board access, a tabbed perks explorer, a flair showcase, an honest Club WWE cross-sell, a growth-engine section, market proof, and an expanded FAQ. The old page did not actually let anyone lock a rate or capture intent; the job it is a portfolio for is exactly "convert a waitlist into a paid membership," so the page had to model that.
- Delivered as a **preview** (`membership-v2.html`, self-contained), not committed. Build method was a surgical replacement of only the page `<main>`, leaving header, footer, and design system untouched, so approval means a clean drop-in.

## Decisions made
- **Founder offer:** Ringside at **$4.99/mo locked for life** (planned $8.99 regular after launch). Implemented conceptually as Stripe grandfathering (pinned founder Price), not a coupon. Real 500-cohort cap in the DB.
- **WWE synergy:** a **tasteful, honest concept module**, clearly labeled "not a live offer," with a no-affiliation disclaimer. Chose honesty over a louder claim because brand-safety judgment is itself a job-win signal.
- **Backend:** **plan-first.** Nothing wired to Supabase. Schema, API, RLS, and lifecycle all specified in six build docs for approval before any build.

## Decisions rejected
- Rejected a headline-hero WWE cross-sell (over-implies a partnership).
- Rejected fake scarcity counters. Every number on the page is a real read or is labeled sample/modeled.
- Rejected inventing a founder price out of thin air; anchored $4.99 against real market prices (Fightful $5, Observer $14.99, Club WWE $99).

## Traps discovered
- **Club WWE is real** and launched 2026-07-31 at $99/yr. Verified across WWE corporate + five outlets before building on it.
- IntersectionObserver will not fire on a zero-width element (the progress-bar fill). Fixed by observing the parent bar.
- The cloud sandbox cannot reach wrestlelore.com, so the preview was made fully self-contained (inlined CSS + base64 fonts + logo) to render offline and screenshot faithfully.
- `site.css` puts an underline on all links, which conflicts with the my-writing-style "no underlined links" rule. Scoped off inside `main` for v2; a site-wide fix is offered.

## Proof
- Desktop + mobile screenshots; automated Playwright interaction test (pricing toggle, perks tabs, waitlist confirmation, counters) all pass.

## Exact next steps
1. Approve `01-BACKEND-SCHEMA-API.md` (the data model).
2. Build the first backend slice: `waitlist_signups` + `waitlist-join` edge function + `founder-progress` counter, wired to the v2 form and hero meter.
3. Then auth + Stripe founder lock, then the Locker Room board + flair, then lifecycle CRM.

## Stack noted for future sessions
Static HTML/CSS/JS front end (unchanged) + Supabase (Postgres/Auth/Storage/Edge/RLS) + Stripe (founder grandfather lock) + Resend/Twilio (email/SMS) + PostHog/GA4 (privacy-first analytics).
