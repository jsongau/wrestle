# Restructure: /matches/ becomes the hub, /rankings/ becomes a rankings directory (2026-07-29)

## What changed
- **/matches/ is now the comprehensive matches hub.** The rich video/rankings page (36 matches, random any-video spotlight hero, 32 official embeds, spoiler-safe cards) was ported verbatim from the interim /matches/viewing-gallery/ URL. Added: a text **search** (matches on wrestler, event, promotion, stipulation, era, AND the slug so fan nicknames like "hbk", "taker", "triple h" work) and hub-grade **SEO** (rated + watchable title/meta/keywords/OG; `CollectionPage` + `WebSite` + `BreadcrumbList` + `ItemList` + `FAQPage` schema). Replaces the old hand-authored index (which it matches and beats).
- **/matches/viewing-gallery/ deleted**, 301 → /matches/ via a new `vercel.json`.
- **/rankings/ rebuilt as a rankings hub** (`build/build_rankings_hub.py`): the 36 greatest matches ranked 1→36 from the real `rank` field (top 3 gold-flagged), plus a directory of ranked categories (Rivalries, Events, Promotions, Wrestlers, Moments → the live section indexes). Text-forward, deliberately distinct from the /matches/ video gallery. Own `CollectionPage` + ordered `ItemList` + `FAQPage` + `BreadcrumbList`.

## URL journey (for redirect hygiene)
/rankings/ (original hub) → /matches/viewing-gallery/ (interim) → **/matches/** (final hub). /rankings/ is now repurposed (NOT a redirect). Only /matches/viewing-gallery/ redirects.

## Decisions
- Rankings hub leads with the one category that has real ranking data (matches). Other categories link to their section indexes honestly ("ranked and expanded on an ongoing basis") rather than faking rankings without data.
- build_rankings.py `SRC_PAGE` now targets `matches/index.html`; `PAGE_URL`/`PAGE_PATH` derive from it, so canonical + schema + breadcrumb followed the move automatically. Breadcrumb is 2-level (Home > Matches) at /matches/.

## Traps discovered
- **Non-idempotent generator:** build_rankings.py reads its own output; the schema strip must remove EVERY type it re-injects (including `WebSite`), or blocks stack up on each rebuild. Fixed; verified stable across 3 rebuilds.
- **Nickname search:** titles use full names ("Shawn Michaels"), so "hbk" found nothing until the slug (which encodes nicknames) was added to the `data-search` haystack.
- **/rankings/ intro `%d`:** a hero string was built without applying `% n`; caught in the render screenshot.

## Next steps
- The 8 newest matches (6 HHH/HBK + 2 Benoit) still have no `/matches/{slug}/` page (404 on "Full breakdown"). Build `build_match_media.py`.
- Expand the rankings hub with real ranked lists for the other categories (needs rating data for rivalries/events/wrestlers).
- Backend: Join Insider Supabase waitlist.
