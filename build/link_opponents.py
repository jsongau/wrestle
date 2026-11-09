#!/usr/bin/env python3
"""link_opponents.py - auto-link opponents in HAND-AUTHORED dossier record tables.

Generated dossiers get opponent links from build_dossier.autolink() at build time.
Hand-authored dossiers (john-cena, cm-punk, aj-styles, the-rock, triple-h) are not
generated, so their <td class="rec2-opp"> cells were plain text. This runs the same
autolink() over every such cell that has no markup yet. Idempotent: a cell that
already contains a tag is skipped, so re-running changes nothing.

    WL_ROOT="$PWD" python3 build/link_opponents.py
Then: python3 build/apply_shell.py
"""
import importlib.util, os, re

ROOT = os.environ.get("WL_ROOT", os.getcwd())
spec = importlib.util.spec_from_file_location("bd", os.path.join(ROOT, "build", "build_dossier.py"))
bd = importlib.util.module_from_spec(spec); spec.loader.exec_module(bd)

HAND = ["john-cena", "cm-punk", "aj-styles", "the-rock", "triple-h"]
CELL = re.compile(r'(<td class="rec2-opp">)([^<]*)(</td>)')

for slug in HAND:
    p = os.path.join(ROOT, "wrestlers", slug, "index.html")
    if not os.path.isfile(p):
        continue
    bd._SELF = slug
    s = open(p, encoding="utf-8").read()
    n = [0]
    def sub(m):
        out = bd.autolink(m.group(2))
        if out != m.group(2):
            n[0] += out.count("<a ")
        return m.group(1) + out + m.group(3)
    s2 = CELL.sub(sub, s)
    if s2 != s:
        open(p, "w", encoding="utf-8").write(s2)
    print("  %-12s +%d links" % (slug, n[0]))
