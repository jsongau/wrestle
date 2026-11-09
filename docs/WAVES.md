# Wrestler dossier waves (Mike's ledger)

Goal (Jay, 2026-11-09): every wrestler on John Cena's format, a sourced data/<slug>.md behind each page, pages crawlable to each other, and a custom animated key-art SVG per wrestler.

Bar: /wrestlers/john-cena/ (~11,700 words, 12 sections). About two thirds of that is a 2,326-row match ledger from data/john-cena-matches.csv. A wave matches Cena's STRUCTURE and per-section depth with verified facts. Row count follows what can be sourced, never padding.

Team: Mike (webmaster, builds + crawl graph + repo), Ross (one per wrestler: data/<slug>.md + build/wldata/<snake>.py), Mary (assets/art/<slug>.svg + measured QA). Definitions in .claude/agents/.

Pipeline per wrestler: Ross .md (sourced) > wldata module > Mary SVG > Mike build_dossier.py + apply_shell.py > crosslinks + search index + sitemap + roster > verify (verify(), JSON-LD, render 1440/390, 0 console errors, 0 broken links) > preview to Jay > commit on approval > push on "deploy".

Census 2026-11-09 (words on page): 63 dossier pages (55 generated, 3.3k–5.4k words; 8 hand-authored), 27 old variant A (490–1,090), 9 variant B (186–998), 9 variant X. Only 4 have data/<slug>.md (john-cena, triple-h, aj-styles, cm-punk).

| Wave | Wrestlers | Status |
|---|---|---|
| 0 | stacy-keibler (new page) | built + verified 2026-11-09, awaiting Jay approval |
| 1 | r-truth, austin-theory, nic-nemeth, trick-williams, yota-tsuji, matt-hardy (thinnest current roster) | built + verified 2026-11-09, awaiting Jay approval |
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
