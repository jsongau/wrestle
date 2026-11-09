# Wrestler dossier waves (Mike's ledger)

Goal (Jay, 2026-11-09): every wrestler on John Cena's format, a sourced data/<slug>.md behind each page, pages crawlable to each other, and a custom animated key-art SVG per wrestler.

Bar: /wrestlers/john-cena/ (~11,700 words, 12 sections). About two thirds of that is a 2,326-row match ledger from data/john-cena-matches.csv. A wave matches Cena's STRUCTURE and per-section depth with verified facts. Row count follows what can be sourced, never padding.

Team: Mike (webmaster, builds + crawl graph + repo), Ross (one per wrestler: data/<slug>.md + build/wldata/<snake>.py), Mary (assets/art/<slug>.svg + measured QA). Definitions in .claude/agents/.

Pipeline per wrestler: Ross .md (sourced) > wldata module > Mary SVG > Mike build_dossier.py + apply_shell.py > crosslinks + search index + sitemap + roster > verify (verify(), JSON-LD, render 1440/390, 0 console errors, 0 broken links) > preview to Jay > commit on approval > push on "deploy".

Census 2026-11-09 (words on page): 63 dossier pages (55 generated, 3.3k–5.4k words; 8 hand-authored), 27 old variant A (490–1,090), 9 variant B (186–998), 9 variant X. Only 4 have data/<slug>.md (john-cena, triple-h, aj-styles, cm-punk).

| Wave | Wrestlers | Status |
|---|---|---|
| 0 | stacy-keibler (new page) | LIVE 2026-11-09 (b355a4c) |
| 1 | r-truth, austin-theory, nic-nemeth, trick-williams, yota-tsuji, matt-hardy (thinnest current roster) | LIVE 2026-11-09 (b355a4c) |
| 2 | british-bulldog, owen-hart, razor-ramon, booker-t, the-hurricane, ricky-steamboat | queued |
| 3 | jake-roberts, arn-anderson, vader, yokozuna, rick-rude, brian-pillman, kevin-nash | queued |
| 4 | lex-luger, big-show, chyna, mr-perfect, bam-bam-bigelow, dusty-rhodes, roddy-piper | queued |
| 5 | andre-the-giant, natalya, goldust, christopher-daniels, bobby-lashley, christian, savio-vega | queued |
| 6 | diamond-dallas-page, bully-ray, sycho-sid, ted-dibiase, shinsuke-nakamura, diesel | queued |
| 7 | the-rock, triple-h (hand-authored, thin for their stature) + .md backfill for aj-styles, cm-punk | queued |
| 8–15 | .md fact files + record-depth pass for the 55 generated dossiers, 7 per wave, current roster first | queued |

Needs a decision from Jay (not queued):
- Persona alias pages (the-ringmaster, stunning-steve-austin, mean-mark-callous, the-american-badass): should be 301 redirects into the main profile's Personas section, not separate dossiers. Duplicate thin pages dilute ranking.
- chris-benoit: existing policy stands (see memory benoit policy); no upgrade.
- vince-mcmahon: factual-only treatment needs Jay's sign-off before an upgrade.
- Cena-scale ledgers: depth past ~100 rows per wrestler needs a match database (one matches table keyed by wrestler), not hand-typed rows in 108 Python modules.

## Log
- 2026-11-09: Waves 0–1 fanned out (7 Ross + 1 Mary). Generator gained DATA["art"] (inlines assets/art/<slug>.svg; missing file falls back to the placeholder). css/dossier.css gained the .portrait--art rules.
- 2026-11-09: Waves 0-1 built in the working tree (uncommitted). 7 dossiers: rows 47/36/38/47/39/27/61, every page 11-12 sections, 0 console errors at 1440/390, all JSON-LD parses. Stacy linked from lita + trish-stratus (Invasion 2001 record row), women/, wrestlers/ roster, search index (with aliases), sitemap.
- Theme band: removed the decorative &rarr; from listen links (writing-style rule; generator-wide).
- Trap: build/build_roster.py is STALE. It regenerates /wrestlers/ from scratch and deletes the current design (1,161 lines). Do not run it; add roster cards by patch.

## Fix queue found by this wave (verified, not yet done)
- SITEWIDE 404s from components/meganav.html on all 566 pages: /titles/nxt-championship/, /tag-teams/ftr/, /tag-teams/the-steiner-brothers/.
- 13 generated pages link a /data/<slug>.md that does not exist: asuka bayley becky-lynch bianca-belair cody-rhodes gunther lita mercedes-mone randy-orton rhea-ripley roman-reigns seth-rollins trish-stratus. Fixed for real by the .md backfill waves.
- Stale facts (per Ross research, verify before editing): /titles/ lists Breakker & Theory as World Tag champs (lost Crown Jewel Nov 7 2026); /titles/tna-world-championship/ says Nic Nemeth is champion (Leon Slater since Bound for Glory Oct 11 2026); build/wldata/jeff_hardy.py misses the Jun 28 2026 Slammiversary tag win, the Aug 23 Lockdown loss and the syX reveal, and counts 3 TNA tag reigns instead of 5; /promotions/njpw/ should say Tsuji's second IWGP reign.
- Crosslink backlog: ~60 sentence-level links into the 7 new dossiers from existing pages (list kept by Mike; old-template pages get theirs in their own wave).
- Generator gaps: slot 5 is factions OR before (Trick Williams lost football or Trick Melo, one of them); "Before WWE" heading is hard-coded even for NJPW; no CMLL promo chip; prose fields escape HTML so career/rivalry text cannot carry links except rivalry cards with slug=.
- Art: matt-hardy crack motif reads as a spider web; one more pass.
- 2026-11-09 (batch 2): nav 404s fixed by building the 3 missing pages (/titles/nxt-championship/, /tag-teams/ftr/, /tag-teams/the-steiner-brothers/). Nav Titles panel was ~3 months stale (7 belts + featured file + world feeds): all corrected from data/champions.md, the new single source of truth for current champions. 6 title pages + titles hub + edge dossier corrected. Jeff Hardy dossier refreshed (21 to 49 rows, TNA tag reigns 3 to 5, syX reveal). Generator auto-links every opponent, rivalry card and first prose mention of any wrestler / tag team / title with a live page; build/link_opponents.py does the same for hand-authored record tables; build/link_mentions.py for one-off prose links on hand pages. Body-content wrestler links sitewide: 2,653 to 4,342. Sitemap gained 15 missing URLs.

## Champion maintenance rule
- data/champions.md is the source of truth. When a title changes: update it first, then components/meganav.html (belt plate name + data-start + featured file + world feeds), the title page, titles/index.html, then apply_shell.py. Title pages carry hand-written "As of" dates that go stale.

## Pre-existing broken links (not introduced; backlog)
- 13 generated dossiers link a missing /data/<slug>.md (fixed by .md backfill waves).
- Old-template pages link legend pages that do not exist: barry-windham, demolition, big-boss-man, ultimate-warrior, honky-tonk-man, bob-backlund, big-john-studd, smokin-gunns, hart-foundation (should be /tag-teams/the-hart-foundation/), dos-hombres, shane-mcmahon, io-shirai (should be iyo-sky), dustin-rhodes.
- events/index.html filter links to 15 missing /events/<promo>/ and /promotions/{nwa,roh,aaa}/ hubs.
- rankings/ + matches/ link 6 match pages that were never built (hbk-vs-razor x2, hbk-vs-mankind, triple-h x3).
- Lore Feed ticker in the shell still leads with the Nov 6 Crown Jewel preview; refresh with build_lorefeed.py when the week of Nov 9 is added.
