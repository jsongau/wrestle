# 2026-08-22 - Real American Freestyle added to Wrestle Lore

## What RAF is
A freestyle wrestling league founded in 2025 by Chad Bronstein, Izzy Martinez, Eric Bischoff and Hulk Hogan. Real unscripted matches with real scores, presented with pro wrestling stagecraft. Hogan died in July 2025, seven weeks before the first card. Fox Nation carries every event exclusively, on subscription, not pay per view. Thirteen events staged: RAF 01 through RAF 12 plus RAF Georgia.

## What was built
New generator `build/build_raf.py`, the third instance of the pattern `build_lorefeed.py` and `build_gallery.py` already run. One `EVENTS` list emits everything.

- `/promotions/raf/` hub: what RAF is, all 13 championships with the three vacancies, every event, and an FAQ answering the questions a pro wrestling fan actually asks (is it scripted, how does freestyle scoring work, where do I watch).
- `/promotions/raf/<slug>/` for all 13 events, 141 bouts total, with weight class, both competitors, winner, method and score, and which title was on the line.
- 42 oEmbed-verified official YouTube clips embedded across the event pages.
- Schema: SportsOrganization + FAQPage on the hub, SportsEvent + BreadcrumbList + ItemList per event. Sitemap +14.

## Integration into existing surfaces
- **Lore Feed**: `raf` added to the `PROMO` map plus 10 sourced RAF dispatches. RAF now flows into the weekly feed, the site-wide ticker and the homepage rail from the same `DISPATCHES` list as WWE and AEW.
- **Gallery and the homepage This Week module**: RAF added as a fifth promotion tab. RAF clips land in the three weeks that contain a RAF card: week of Jul 6 (RAF Georgia), Jul 13 (RAF 11), Aug 17 (RAF 12). RAF is monthly, so the tab only appears in weeks that have a card, which the per-week `promos` dict handles automatically.
- **Nav**: the top level did NOT change. RAF was added inside the existing Promotions mega menu and to the `/promotions/` directory page.

## Sourcing
141 bouts came from USA Wrestling (themat.com), FloWrestling, InterMat and RAF's own event pages, cross-checked where sources disagreed. Every one of the 42 video ids was verified through the YouTube oEmbed endpoint and accepted only on an author_name of "Real American Freestyle Wrestling" or "Fox Nation".

Two candidate items were DROPPED for contradicting better-sourced facts: a reported Dake loss to Arsenii Dzhioev in February (RAF's own champions page and every event card contradict it) and a sanctions story about RAF Moscow resting on a single weak secondary source. RAF 12 runs tonight and is published as an announced card with no results.

## Traps discovered
- **`js/media.js` owns `.yt[data-yt-id]`.** A custom video facade gets silently replaced with a "NO SIGNAL" placeholder. Use the same `article.vcard > div.yt > a.yt__link` contract `build_gallery.facade_card` emits, or the theater player will not adopt the card.
- **The `.dk bcard` promotions grid lives in `components/meganav.html`, not in `promotions/index.html`.** It is stamped into every page's `<header>` by apply_shell.py. Editing the page directly appears to work and is silently reverted on the next apply_shell run. Never anchor a body edit on markup that turns out to be nav.
- **`vtitle()` in build_gallery.py prepends the promo to the show name**, which read "RAF RAF" when a promotion's tab name equals its show name. Fixed generically with a leading-token dedupe.
- Adding a sixth card to `/promotions/` broke the lede sentence that said "the five promotions". The generator now corrects that sentence in the same pass.

## Next steps
1. Publish RAF 12 results tomorrow. The card is already live with `result: None` on every bout, so it is a data edit, not a build.
2. RAF 13 (Sept 19, Miami) and RAF 14 (Oct 3, Las Vegas) are announced and can be added as upcoming.
3. Review gate: check in 30 days whether any RAF event page reaches page one for its own event name. Nobody in pro wrestling media currently ranks for RAF results, which was the whole thesis for building this.
4. No athlete directory was built. RAF's own site does that well and we link out to it.
