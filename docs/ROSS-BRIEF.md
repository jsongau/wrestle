# Ross brief: one wrestler, Cena-format dossier

Working copy: /home/claude/wl (a clone of Jay's repo). Work ONLY in this folder. No git commands. Never run build/apply_shell.py. Only touch: data/<slug>.md, build/wldata/<snake>.py, and the generated wrestlers/<slug>/index.html (the generator writes that).

Read first, in this order:
1. .claude/agents/ross.md (your role and rules)
2. CLAUDE.md sections 6 and 7
3. docs/2026-08-23-wrestler-dossier-generator.md (generator invariants and traps)
4. build/build_dossier.py (the schema: what keys DATA needs, sections_for(), verify())
5. build/wldata/trish_stratus.py and build/wldata/lita.py (complete worked examples, women's-division legends)
6. data/john-cena.md (the .md format) and data/triple-h.md
7. The wrestler's current page wrestlers/<slug>/index.html if it exists: harvest it, then VERIFY every harvested claim. Old pages contain errors.

Depth target: the John Cena page (wrestlers/john-cena/index.html) is the bar. Match its structure: every section the generator supports that the subject can honestly fill (overview, record, signature, titles, factions or before, personas, career, rivalries, media, feats, reference, faq), plus the walk-out theme band if the entrance theme is verifiable. Depth comes from REAL rows and REAL facts: as many verified record rows as you can source (title matches, PLE/PPV matches, TV milestones, debut, last match), 8+ FAQ entries, a full career timeline. Never pad. If a section cannot be filled honestly, omit it and say why in the module docstring.

Facts: web-search and fetch. Wikipedia is a starting point, not the only source; cross-check with WWE.com, Cagematch (may be blocked), ProFightDB, Fightful, PWInsider, Sports Illustrated, ESPN, official promotion pages. Current status as of 2026-11-09 must be searched, not recalled. Every claim in the .md carries a URL. Flag disputes with ⚑.

Links: link opponents, factions, events and titles only to pages that exist on disk (check with ls). List of wrestler slugs: ls wrestlers/.

Key art: set DATA["art"] = "<slug>" (Mary is drawing assets/art/<slug>.svg in parallel; the generator will inline it). Do not draw it yourself.

Copy style (binding): no em dashes used as sentence separators (write two sentences or use a comma; en dash in ranges like 2001–2006 is fine), no arrows in visible text, no banned words (seamless, empower, unlock, elevate, comprehensive, leverage, curated, journey, delve, testament, tapestry), plain American English, exact nouns, one idea per sentence.

Done means: WL_ROOT=/home/claude/wl python3 build/build_dossier.py <slug> prints the page line with no FAILED. (Ignore a missing-art notice if Mary has not finished yet.)

Report back (concise, under 400 words): sections emitted, record row count, FAQ count, source count, every ⚑ flag, anything you omitted and why, and a CROSSLINK list: existing pages (path) that should link to this wrestler, each with the sentence where the link belongs.
