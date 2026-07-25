# MAT Content Corpus (Markdown Mirror / GEO)

This folder is the clean Markdown mirror of MAT's key pages — a chunk-friendly text corpus built for GEO (Generative Engine Optimization) and AI crawlability. Each file is a source-of-truth content document for one page or section of MAT (Match · Athlete · Timeline), written answer-first with descriptive headings, concrete facts and self-contained chunks so that search engines and AI answer engines (ChatGPT, Perplexity, Gemini, Google AI Overviews) can extract and cite MAT accurately.

## Why does this folder exist?

MAT's GEO strategy is to be the source AI answer engines cite. Part of that is mirroring every major page as clean Markdown here in /content/, and pointing crawlers to this corpus from llms.txt at the site root. These Markdown files are plain-text, low-noise versions of the HTML pages: same facts, no layout markup, optimized for chunking and quotation. Facts are synthesized from public records — dates, results, ratings and named entities — and are not copied verbatim from any source.

## What files are in this folder?

- home.md — the MAT front-page content: what MAT is, coverage stats, the featured match, the Five-Star Club, icons of the era, the relationship-web teaser, membership summary and FAQ. Mirrors /.
- membership.md — MAT Insider membership: the three tiers (Fan, Insider, Ringside), pricing, the six-stage acquisition-to-retention funnel, and the waitlist. Mirrors /membership/.
- wrestlers-index.md — a one-line-per-wrestler index of all 41 wrestlers (name, nickname, promotions, profile link path). Mirrors /wrestlers/.
- matches-index.md — a one-line-per-match index of all 30 rated matches (match, event/date, MAT rating, link path). Mirrors /matches/.
- rivalries-index.md — the 15 landmark rivalries with one-line summaries and link paths. Mirrors /rivalries/.
- relationships.md — the real-life relationship web: couples, families/bloodlines, factions and trainer lineages. Mirrors /relationships/.
- methodology.md — how MAT rates matches: the five-star scale, informed by Meltzer, Cagematch and historical significance. Mirrors /methodology/.
- china-strategy.md — the China go-to-market summary: distribution, localization, acquisition, payments and compliance. Mirrors /zh/ and the China strategy.
- README.md — this file, explaining the corpus and listing its contents.

## How should this corpus be used?

Treat each file as the canonical text for its page. All internal link paths use MAT's canonical slugs (for example, /wrestlers/the-undertaker/ and /matches/undertaker-vs-hbk-wm25/), so the corpus preserves MAT's internal link graph in plain text. When MAT's HTML pages change, update the matching Markdown file here to keep the mirror accurate.
