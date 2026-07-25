# MAT — The Ultimate Pro Wrestling Database & Fan Network
### Master Project Brief · v1.0 · 2026-07-25

> Working title: **MAT** ("Match · Athlete · Timeline"). A crawlable, interlinked
> wrestling encyclopedia + review site — *Sherdog/Tapology for pro wrestling* —
> engineered from the ground up as a **membership-growth engine**.

---

## 0. Why this exists (the real objective)

This project is Jay's portfolio artifact for the **WWE / TKO — Manager, Membership Growth**
role (R0008155, LA, $93.75K–$125K). That job is **not** a design job. Its core is:

> "Convert a broad fan audience and a large, growing waitlist into a paid membership base"
> via owned channels (email, SMS, web, app, landing pages), lifecycle campaigns, A/B testing,
> funnel analytics, and cross-functional coordination.

So MAT is not "just a fan site." It is a **working demonstration of membership growth thinking**:
an acquisition surface (SEO/GEO-driven traffic) → engagement loop (ratings, interlinking) →
waitlist capture → tiered paid membership → lifecycle retention. Every feature is justified by
one of: **acquisition, retention, engagement, trust, revenue, or operational efficiency.**

**The pitch to WWE:** "You have 1B+ households and a waitlist. Here is the owned-channel
funnel I'd build to convert them — and here's a live prototype running on real wrestling content,
optimized for Google, AI answer engines, and the China market."

---

## 1. Positioning

- **Category:** definitive pro-wrestling database + match-review network (1997 → present).
- **Coverage:** WWE (WWF/E), WCW, ECW, TNA/Impact, NXT — the modern era from the 1997
  Monday Night Wars onward.
- **Model:** Sherdog's fighter/event/rating architecture, applied to wrestling, with a
  Cagematch-style rating layer and a Wikipedia-grade internal-link graph.
- **Differentiator:** *the relationship graph.* Every wrestler links to rivals, tag partners,
  trainers, real-life spouses/family, and the matches that define them. This density is what
  makes the site addictive to fans AND highly crawlable/citable by search + AI engines.

---

## 2. Information architecture (sitemap)

```
/                         Home — featured match, trending, membership CTA
/wrestlers/               Roster index (filter by promotion/era/division)
  /wrestlers/{slug}/      Profile: bio, titles, finishers, feuds, matches, relationships
/matches/                 Match index (sortable by our rating)
  /matches/{slug}/        Match page: our rating, embedded video, story, participants
/rivalries/               Storyline/feud index
  /rivalries/{slug}/      Feud page: timeline, matches, wrestlers
/relationships/           Real-life relationship web (romances, families, friends, heat)
/promotions/              WWE / WCW / ECW / TNA / NXT hub pages
/membership/              Insider membership tiers + join
/waitlist/                Waitlist capture (top of funnel)
/rankings/                Our all-time match & wrestler rankings
/china/  (/zh/)           Simplified-Chinese entry + China distribution
/about/  /methodology/    How we rate (trust/E-E-A-T signal)
sitemap.xml  robots.txt   Crawl infrastructure
```

**Rule:** the mega-nav is a fixed instrument. New content routes into existing dropdowns/hubs,
never widens the top bar. Depth via hubs, not more tabs.

---

## 3. Design system

- **Aesthetic:** dark "arena" theme — near-black canvas, championship gold (#D4AF37) accent,
  blood-red (#C8102E) for live/hot, chrome/steel neutrals. High contrast, editorial.
- **Mobile-first:** every layout designed at 360px first, enhanced up. Tap targets ≥44px.
- **Components:** wrestler card, match card w/ star-rating meter, rating gauge, nav mega-panel,
  relationship chips, timeline, embed wrapper (16:9 responsive), waitlist form, tier cards.
- **Perf:** system-font stack, CSS-only where possible, lazy-loaded iframes (facade pattern),
  no framework, no browser storage. Target LCP < 2.5s on 4G, CLS ~0.
- **A11y:** semantic HTML5 landmarks, alt text, focus states, prefers-reduced-motion, WCAG AA.

---

## 4. SEO strategy (Google/Bing)

- Semantic HTML5 + one H1/page, logical heading order.
- **Structured data (JSON-LD):** `Person` (wrestlers), `SportsEvent` (matches),
  `Review`/`AggregateRating` (our ratings), `BreadcrumbList`, `FAQPage`, `Organization`.
- Clean, keyworded, human-readable URLs (`/matches/hbk-vs-undertaker-wm25/`).
- Dense internal linking (the relationship graph = a natural link mesh).
- `sitemap.xml`, `robots.txt`, canonical tags, OG/Twitter cards, descriptive meta.
- Fast + mobile = Core Web Vitals green. Freshness via a changelog/updates feed.

## 5. GEO strategy (Generative Engine Optimization — ChatGPT/Perplexity/Gemini/AI Overviews)

GEO = being the source AI answer engines cite. Tactics baked in:

- **Answer-first content:** each page opens with a crisp, quotable factual summary
  (the "extractable answer" an LLM lifts).
- **FAQ blocks with `FAQPage` schema** on every major page — direct Q→A pairs.
- **Statistical density & specificity:** dates, results, ratings, named entities — LLMs
  favor concrete, citable facts over fluff.
- **Clear entity definitions** ("X is a...") so models bind facts to entities.
- **Markdown mirror** of every page (`/content/*.md`) — clean, chunk-friendly text.
- **llms.txt** at root pointing crawlers to the markdown corpus.
- Consistent, authoritative tone + a `/methodology/` page = trust/authority signal.

## 6. China market strategy (growth wedge)

WWE has repeatedly targeted China (largest untapped fan market). MAT models the entry:

- **Distribution:** WWE/wrestling clips live on **Bilibili, Douyin (TikTok CN), Weibo,
  Youku, WeChat Channels** — not YouTube (blocked). China pages embed/link Youku/Bilibili,
  not YouTube.
- **Localization:** `/zh/` Simplified-Chinese entry; Chinese ring names (e.g. 送葬者 = Undertaker,
  "巨石"强森 = The Rock); hreflang tags; culturally-tuned hero content.
- **Acquisition:** WeChat Mini-Program / Official Account funnel concept; QR-code-first
  capture (China UX norm); Xiaohongshu (RED) content strategy for younger fans.
- **Membership fit:** map the tiered membership to China payment rails (WeChat Pay / Alipay)
  and to how Chinese fans already pay for fandom (super-chats, digital collectibles).
- **Compliance note:** flag ICP-license + data-localization realities honestly (shows maturity).

---

## 7. Membership funnel (the job-winning core)

```
TRAFFIC (SEO+GEO+China)  →  ENGAGEMENT (ratings, graph)  →  WAITLIST  →  PAID TIERS  →  RETENTION
```

- **Top of funnel:** free crawlable content pulls organic + AI-referral traffic.
- **Capture:** waitlist form (email/SMS), exit-intent + inline CTAs, "notify me" on gated ratings.
- **Tiers (concept):** Free → **Insider** ($ / mo: full ratings, no ads, newsletters) →
  **Ringside** ($$: premium archive, watch-along, community, drops).
- **Conversion levers:** gated premium star-ratings + archive, member-only rankings,
  benefit-drop calendar, event-tied pushes.
- **Lifecycle:** welcome series, onboarding, win-back, renewal, event surge campaigns
  (mocked as email/SMS templates in `/membership/lifecycle/`).
- **Measurement:** a funnel-metrics readout page (waitlist growth, email CTR, LP conversion,
  checkout completion, paid conversion, retention) — mirrors the job's weekly-readout duty.
- **A/B testing:** documented test plan (subject lines, CTAs, offers, LP variants).

---

## 8. Tech stack & conventions

- **Static site:** hand-authored HTML5 + one CSS design system + vanilla JS. No build step
  required to view; deployable to Vercel/GitHub Pages. Simple, durable, fast, crawlable.
- **Content-as-markdown:** every page mirrored in `/content/*.md` (portability + GEO).
- **No browser storage** (localStorage/sessionStorage) — in-memory only.
- **Repo hygiene:** ONE live repo (this folder). No dated/versioned files committed.
  Preview iterations delivered to Downloads as `-v2/-v3`. `CHANGELOG.md` updated per work day.
  Session summaries in `/docs/`.
- **Deploy:** nothing pushed until Jay confirms GitHub repo + Vercel project + git remote.

---

## 9. Success metrics

- **Site:** Core Web Vitals green; 100% internal-link integrity; valid schema on all templates.
- **Growth model (illustrative KPIs the funnel is built to move):** organic sessions,
  AI-referral sessions, waitlist signups, waitlist→paid conversion %, email CTR, LP conversion,
  monthly retention, ARPU.
- **Job outcome:** a portfolio piece that lets Jay walk into the WWE interview and say
  "I already built your funnel — here's the data model, the lifecycle, and the China play."

---

## 10. Build order (this session)

1. Master brief (this file) ✔  2. Design system (CSS/JS)  3. Front page + mega nav
4. Content pages (wrestlers/matches/rivalries/relationships) 5. Membership funnel
6. SEO/GEO infra + China entry 7. Markdown mirror 8. Verify + commit + session summary.

*Agents run research in parallel while templates are built. Progress committed to the live repo periodically.*
