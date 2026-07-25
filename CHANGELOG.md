# Changelog — MAT (Pro Wrestling Database)

## 2026-07-25
- Project kickoff. Wrote master brief (`PROJECT.md`): vision, IA/sitemap, SEO+GEO strategy, China market plan, membership funnel, tech stack.
- Ran 4 parallel research agents → datasets in `/data/` (41 wrestlers + 160+ relationship edges, 30 rated matches, 15 storylines, full design/SEO/GEO/China reference).
- Built single-file design system (`css/site.css`) — dark "arena" theme, mobile-first, all components (cards, rating meters, tale-of-the-tape, mega-nav, embeds/facade, tiers, forms).
- Built `js/main.js` — mobile nav, mega-panel toggles, facade video loader (YouTube+Bilibili), roster search/filter, waitlist form (in-memory, no browser storage).
- Built front page (`index.html`) with full mega-nav, hero featured match, five-star club, icons, relationship teaser, waitlist capture, GEO answer + FAQ.
- Built flagship templates: match page (Undertaker vs HBK WM25), wrestler page (The Undertaker), membership funnel (`membership/`).
- Dispatched builder-agent fleet for the remaining wrestler/match/rivalry/relationship/promotion/China pages, indexes, markdown mirrors, and SEO infra.
