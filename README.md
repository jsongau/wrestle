# MAT — The Ultimate Pro Wrestling Database
**Match · Athlete · Timeline** — a crawlable, mobile-first encyclopedia and review site for modern professional wrestling (WWE · WCW · ECW · TNA · NXT, 1997–present), engineered as a membership-growth engine.

> **Status:** v2 live in this repo · 105 HTML pages · 158 tracked files · 0 broken internal links · 0 invalid structured-data blocks.
> **Not yet deployed** — no git remote set. Nothing is pushed until the GitHub repo + Vercel project are confirmed.

---

## 1. Why this exists

MAT is a portfolio artifact built to win the **WWE / TKO — Manager, Membership Growth** role (R0008155, Los Angeles, $93,750–$125,000). That role is an *owned-channel growth* job: converting a broad fan audience and a growing waitlist into **paid members** via email/SMS/web funnels, lifecycle campaigns, A/B testing, CRM segmentation and weekly funnel readouts.

So MAT is deliberately more than a fan site. It is a **working demonstration of membership-growth thinking**: an SEO/GEO/China-driven acquisition surface → an engagement loop (ratings + a dense relationship graph) → waitlist capture → tiered paid membership → lifecycle retention. Every feature maps to one of: acquisition, retention, engagement, trust, revenue, or operational efficiency.

**The pitch:** "You have 1B+ households and a waitlist. Here is the owned-channel funnel I'd build to convert them — running live on real wrestling content, optimized for Google, AI answer engines, and the China market."

---

## 2. What it is (positioning)

The **Sherdog / Tapology of pro wrestling**: a definitive, interlinked database of the modern era with a Cagematch-style rating layer and a Wikipedia-grade internal-link graph. The differentiator is **the relationship web** — every wrestler links to rivals, tag partners, trainers, real-life spouses/family, and the matches that define them. That density is what makes the site addictive to fans *and* highly crawlable/citable by search + AI engines.

---

## 3. What's built (current inventory)

| Area | Live pages | Notes |
|---|---|---|
| Homepage | 1 | v2 "Broadcast Bold" redesign (Anton/Oswald/Inter, arena hero, film grain, duotone tiles, motion) |
| Wrestler profiles | 41 | Interlinked; Person + Breadcrumb + FAQ schema |
| Match reviews | 30 | MAT star rating, tale-of-the-tape, video, SportsEvent + Review schema |
| Rivalry pages | 15 | + rivalries index |
| Promotion hubs | 5 | WWE, WCW, ECW, TNA, NXT + index |
| Relationships / Rankings / Membership / About / Methodology | 5 | Real-life web, rankings, funnel, trust pages |
| China edition (`/zh/`, `/china/`) | 3 | Simplified Chinese, Bilibili embeds, WeChat/QR funnel |
| **Total** | **105 HTML pages** | 103-URL sitemap, robots.txt, llms.txt, `/content/` markdown mirror |

**Verification:** 0 broken internal links across all pages; 0 invalid JSON-LD; desktop + mobile + China renders confirmed via screenshots.

### Source datasets ready for the next page-generation wave (`/data/`)
Not yet built into pages — the fuel to roughly triple the site:
- **~86 wrestlers** (41 live + 45 in expansion), **~65 matches** (30 live + 35 expansion)
- **21 new rivalries + 17 factions**, **26 events/PPVs + 15 championship lineages**
- **67-term glossary** + **12 family-dynasty** profiles (SEO/GEO fuel)
All cited, deduped, and current through 2024–2026.

---

## 4. Architecture & tech stack

- **Static, hand-authored HTML** + one CSS design system (`css/site.css`) + vanilla JS (`js/main.js`, `js/enhance.js`). **No framework, no build step, no browser storage.**
- Chosen for maximum crawlability, zero build friction, instant deploy to Vercel/GitHub Pages, and durability. (Rejected Next.js/Astro: JS-rendered nav hurts crawlability and adds complexity a content site doesn't need.)
- Content mirrored as Markdown in `/content/` for portability + AI retrieval.
- Root-absolute asset paths (`/css/…`) — the site must be served over HTTP to preview correctly (double-clicking a page uses `file://` and won't load CSS). Self-contained `-v2` previews inline everything for double-click.
- Base URL placeholder: `https://wrestlelore.com` (swap for the real domain at deploy).

---

## 5. Design system

**v2 art direction: "Broadcast Bold"** (ESPN/UFC/DAZN energy). Type: **Anton** (display) + **Oswald** (condensed UI) + **Inter** (body). Black + championship-gold `#d4af37` + blood-red `#e11d2a`. Techniques: layered "arena spotlight" hero, data-URI film grain, duotone "fight-poster" tiles with monograms, gradient-border cards, pointer-tracked spotlight, metallic-gold shine buttons, marquee ratings ticker, glass stat bar, angled section seams, and scroll-reveal **gated behind a `.js` class so all content is visible without JavaScript** (progressive enhancement — protects SEO and reliability).

**Chosen navigation: "CONTROL ROOM"** (mega-nav concept 2 + 3 combined, preview approved) — a broadcast HUD (live ticker, corner-bracket frames, mono telemetry) with a bento command-board mega on every nav item, plus a **⌘K command-palette global search**. Spec: `docs/design/mega-nav-combined.md`. *Pending build-out across the site.*

Full per-section specs live in `docs/design/` (14 files). Design + UX research playbooks live in `data/` (`design-research-*.md`, `ux-research-*.md`, `research-meganav.md`, `research-cool-styles.md`).

---

## 6. SEO · GEO · China strategy

- **SEO:** semantic HTML5, one H1/page, clean slugs, dense internal linking, `sitemap.xml` (hreflang), `robots.txt`, canonical/OG/Twitter tags, Core-Web-Vitals-friendly (system-adjacent fonts, lazy facade video embeds). JSON-LD on every page: `Person`, `SportsEvent`, `Review`/`AggregateRating`, `BreadcrumbList`, `FAQPage`, `Organization`, `WebSite`.
- **GEO (Generative Engine Optimization):** answer-first paragraphs, visible FAQs + `FAQPage` schema, statistical density, `sameAs` entity linking, a Markdown mirror + `llms.txt`. `robots.txt` explicitly welcomes GPTBot, OAI-SearchBot, PerplexityBot, Google-Extended, ClaudeBot.
- **China:** Simplified-Chinese `/zh/` edition with `hreflang`; Bilibili/Youku embeds instead of (blocked) YouTube; WeChat Official-Account + Mini-Program + QR-first funnel concept; WeChat Pay/Alipay rails; honest ICP/PIPL localization notes. Strategy page at `/china/`.

---

## 7. Membership growth funnel (the job core)

```
TRAFFIC (SEO+GEO+China) → ENGAGEMENT (ratings, relationship graph) → WAITLIST → PAID TIERS → RETENTION
```

- **Tiers:** Free → **Insider** (free: full ratings, archive, newsletter) → **Ringside** ($6/mo: premium archive, watch-alongs, community, drops).
- **Capture:** waitlist form (email/SMS) segmented by favorite promotion + source; gated premium ratings/archive.
- **Lifecycle:** welcome → onboarding → win-back → renewal/event-surge (mocked; ready for a real ESP/CRM).
- **Measurement:** a funnel-readout concept mirroring the role's weekly reporting duty. `/membership/` + growth-strategy one-pager.

---

## 8. Repository structure

```
/index.html            Homepage (v2 Broadcast Bold)
/wrestlers/<slug>/      41 profile pages (+ index)
/matches/<slug>/        30 match reviews (+ index)
/rivalries/<slug>/      15 rivalry pages (+ index)
/promotions/<slug>/     WWE · WCW · ECW · TNA · NXT (+ index)
/relationships/  /rankings/  /membership/  /about/  /methodology/
/zh/  /china/           China edition + strategy
/css/site.css           Single-file design system
/js/main.js  /js/enhance.js   Behavior + motion (no storage)
/content/*.md           Markdown mirror (GEO corpus)
/data/*.md              Research + source datasets (20 files)
/docs/design/*.md       14 design/UX specs
/docs/*.md              Session summaries
robots.txt  sitemap.xml  llms.txt  PROJECT.md  CHANGELOG.md  README.md
```

---

## 9. Preview · run · deploy

**Preview locally** (serve over HTTP so `/css/` resolves):
```
python3 -m http.server 8080 --directory /Users/kytlegacy/Claude/Projects/WWE
```
Then open `http://localhost:8080`.

**Deploy:** not done. When ready, confirm the GitHub repo + Vercel project; the git remote will be shown before any push. `main` is the working branch.

---

## 10. Roadmap / next steps

1. **Build CONTROL ROOM nav** across all pages (HUD + ⌘K search + in-memory index) — then it ships on every new page.
2. **Page-generation wave** from `/data/` expansion sets (~150 new pages: +45 wrestlers, +35 matches, rivalries, factions, events, titles, glossary, families) → roughly triples the site.
3. **Membership backend** — real waitlist capture (Supabase table + insert-only RLS + double opt-in), wire the form.
4. Verified video IDs (YouTube global / Bilibili `/zh/`), real imagery + OG images.
5. Analytics + funnel event tracking; then deploy.

---

## 11. Credits & disclaimer

Fan-made educational project. **Not affiliated with, endorsed by, or sponsored by WWE, TKO Group Holdings, or any promotion.** All trademarks and match footage are property of their respective owners. Facts synthesized from public records (Wikipedia, Cagematch, official sources); no third-party text copied verbatim.
