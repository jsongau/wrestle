# Weekly gallery page SEO/GEO contract

Every week is a page: `/gallery/<YYYY-MM-DD>/` (Monday key). It must exist from Monday 12 AM ET (the Monday scheduled task opens it) and compound all week as the nightly 2 AM ET scan embeds each show's verified clips. This file is the distilled contract; the full agent spec lives in `docs/2026-07-30-gallery-redesign-build-spec.md`.

## The compounding loop
Monday: page opens near-empty but indexable (upcoming-schedule scaffold, this-week copy, JSON-LD shell). Each night: new clips append to `WEEKS`, the rebuild regenerates the page, content and ItemList grow, lastmod bumps in sitemap.xml. By Sunday the page is the definitive recap of that week. Never delete a week; the archive is the moat.

## Per-week head (emitted by build_gallery.py, all derived from WEEKS)
- Title: `WWE, AEW, TNA and NXT Recaps: Week of <Month D, YYYY> | Wrestle Lore` (no em-dash separators anywhere; recap + highlights keywords; unique per week).
- Meta description: unique per week; name the shows and dates that aired and the streaming homes; spoiler-safe (no results in metadata).
- H1 (real server-rendered H1, not JS): `This Week in Wrestling: <Month D> to <Month D, YYYY>`.
- Canonical `https://wrestlelore.com/gallery/<week>/`; `link rel=prev/next` to newer/older weeks.
- OG/Twitter: og:image = the week's marquee clip hqdefault thumb; robots `index,follow,max-image-preview:large,max-video-preview:-1`.

## JSON-LD @graph per week
- CollectionPage (the week) + BreadcrumbList (Home > This Week in Wrestling > Week of ...).
- ItemList of VideoObject, one per clip: name, description, thumbnailUrl `https://i.ytimg.com/vi/<id>/hqdefault.jpg`, uploadDate (clip air date), embedUrl `https://www.youtube-nocookie.com/embed/<id>`, contentUrl `https://www.youtube.com/watch?v=<id>`, publisher Wrestle Lore. Grows nightly.
- FAQPage: 3 to 5 questions derived from the actual week ("What happened on WWE Raw on <date>?", "Where can I watch <show> highlights this week?", "When is <next PLE>?"). Answers stay spoiler-light and factual.

## On-page copy blocks (crawlable, server-rendered)
- Recap intro paragraph naming every show that aired with dates and networks (unique per week; grows as shows air).
- Per-show H2s in schedule order (`WWE Raw, <Month D>` etc), each followed by its clips.
- "Still to air" scaffold for un-aired days early in the week (targets "when is <show> on this week" and prevents thin-page feel).
- Tune-in data: every show name + night + streaming home appears in text, not just chips (Raw Mon Netflix, NXT Tue The CW, Dynamite Wed HBO Max, iMPACT Thu AMC+, SmackDown Fri Peacock, Collision Sat HBO Max; PLEs on real dates).

## Internal links (topical authority)
Each week page links: prev/next week, the /gallery/ hub, the matching lore-feed week `/lore-feed/<week>/`, promotion hubs, and event pages for any PLE that week. Wrestler names in deks link to their profile pages when they exist. The hub, homepage widget, and media page all draw from the same WEEKS source, so links never drift.

## Slug and naming
Hub stays `/gallery/` (canonical, already indexed); the recap intent is won via title/H1/schema/copy. An exact-match slug migration (301) is a deliberate separate step, never a silent rename.

## Editorial bar (non-negotiable)
Only oEmbed-verified official-channel videos (WWE, WWE NXT, All Elite Wrestling, TNA Wrestling, New Japan Pro-Wrestling, WWE Vault). Verify via `https://www.youtube.com/oembed?url=...&format=json`; keep only official author_name; NEVER invent an ID. Spoiler-safe labels ("Show · descriptor"). No arrow glyphs, no em-dash sentence separators, no AI-tell copy.

## Growth levers already scheduled
- Daily 2 AM ET: scan + verify + append + rebuild + notify (trigger `Wrestle Lore — Daily Gallery Video Scan`).
- Monday 12 AM ET: open the new week page (trigger `Wrestle Lore — Monday SEO Week Page`).
Both notify-and-approve; Jay deploys. Early-week indexing matters: deploy Monday's page promptly.
