# Ross brief: a title or tag-team page from a sibling template

Working copy: /home/claude/wl. Work ONLY on your one new folder plus your data/<slug>.md. No git. Never run build/apply_shell.py or any build script. Do not edit any other page.

1. Read .claude/agents/ross.md (rules) and CLAUDE.md sections 2 and 6.
2. Copy the named sibling page to the new path and rewrite its CONTENT for your subject: title, meta description, canonical, og/twitter tags, JSON-LD (every block must parse with json.loads), breadcrumb, hero, every section, FAQ (FAQ HTML and FAQPage JSON-LD 1:1 in count and order). Keep the sibling's markup, classes and section structure exactly; the shared header/footer between <header class="site-header nav7"> and its </header>, and the footer, stay untouched (Mike re-stamps them).
3. Every fact is web-verified as of 2026-11-09 and recorded with a source URL in data/<slug>.md (same format as data/john-cena.md: frontmatter, facts, ⚑ disputes, sources). Current champions/status must be searched, not recalled.
4. Links: only to pages that exist on disk (check with ls). Link every wrestler who has /wrestlers/<slug>/, every event page, every related title/tag-team page.
5. Copy style (binding): no em dashes as sentence separators, no arrows in visible text, no banned words (seamless, empower, unlock, elevate, comprehensive, leverage, curated, journey, delve, testament, tapestry). Plain American English.
6. Self-check before reporting: python3 - parse every ld+json block; every href="/..." resolves to a file or folder/index.html; no "&rarr;" or "→" in visible text; no leftover text about the sibling subject (grep the sibling's main names).

Report (under 300 words): sections, FAQ count, source count, ⚑ flags, current holder/status with date and source, and a CROSSLINK list (existing pages that should link to the new page, with the sentence).
