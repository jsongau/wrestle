# Session Summary — 2026-07-25 · MAT Wrestling Database (v1)

## Objective
Build a portfolio artifact to help Jay win the **WWE / TKO — Manager, Membership Growth** role (R0008155). Reframed the "ultimate wrestling fan site" as a **membership-growth engine**: an SEO/GEO/China-driven acquisition surface → engagement loop → waitlist capture → tiered paid membership → lifecycle retention. This maps the build directly to the job's core responsibilities.

## What was built
A crawlable, mobile-first static site ("MAT — Match · Athlete · Timeline"), Sherdog-style, covering WWE/WCW/ECW/TNA/NXT (1997–present).

- **104 HTML pages, 173 files total.**
- 41 wrestler profiles · 30 rated match pages · 15 rivalry pages · relationships web · rankings · 5 promotion hubs + index · about + methodology.
- Membership funnel: tiers page, waitlist capture (email/SMS), growth-strategy one-pager mapped to the job.
- China edition: `/zh/` home + membership (Simplified Chinese, Bilibili embeds, WeChat/QR funnel) + `/china/` strategy page.
- SEO/GEO infra: `robots.txt` (allows AI crawlers), `sitemap.xml` (103 URLs, hreflang), `llms.txt`, schema.org JSON-LD on every page (Person, SportsEvent, Review+AggregateRating, BreadcrumbList, FAQPage, Organization), answer-first content + FAQs.
- Markdown mirror in `/content/` (GEO corpus).
- Single-file design system `css/site.css` + vanilla `js/main.js` (no framework, no build, no browser storage).

## Architecture decisions (and rejected alternatives)
- **Static hand-authored HTML over a framework/SSG.** Chosen for maximum crawlability, zero build friction, instant deploy to Vercel/GH Pages, and durability. Rejected Next.js/Astro: unnecessary complexity for a content site; JS-rendered nav hurts crawlability.
- **Root-absolute asset paths (`/css/…`).** Correct for a deployed web root; note they don't resolve via `file://` (must serve over HTTP to preview locally).
- **Slug manifest before parallel build.** Locked canonical slugs so 9 parallel builder-agents produced link-consistent pages. Result: 0 broken internal links across 104 pages.
- **Video via facade → official search.** We don't have verified YouTube/Bilibili IDs, so embeds open the official search instead of risking wrong/broken iframes. Verified IDs drop straight into the same component.

## Verification
- 0 broken internal links (104 pages checked).
- 0 invalid JSON-LD blocks (all parse).
- Every page links CSS + JS; screenshots rendered over HTTP (desktop + mobile + China) confirm styling and responsiveness.

## Known follow-ups / next steps
1. **Backend (the real job muscle):** stand up the waitlist capture for real — Supabase table (email, sms, promotion, source, ts) + an API route + double opt-in. Wire the form's mock console event to it. This is the highest-leverage next task.
2. Drop in **verified video IDs** (YouTube for global, Bilibili for `/zh/`).
3. Add **real images** (wrestler/match art) + OG images; currently initials placeholders + referenced `/assets/*` paths.
4. Add `/promotions/` to `sitemap.xml`.
5. Analytics + event tracking (funnel readout page is mocked; wire to real events).
6. Deploy: confirm GitHub repo + Vercel project + git remote before any push.

## Stack / conventions (for future sessions)
- Static HTML + one CSS file (`css/site.css`, design tokens) + one JS file (`js/main.js`). No framework, no build, no browser storage.
- One live repo (this folder). Cloud is the authoritative git; device folder mirrors it. Preview iterations go to Downloads as `-v2/-v3`, never into the repo.
- Base URL for canonical/OG: `https://matwrestling.com` (placeholder — swap for the real domain at deploy).
- Research datasets live in `/data/`; markdown mirror in `/content/`.
