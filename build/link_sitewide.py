#!/usr/bin/env python3
"""link_sitewide.py - run wl_links.link_page() over every HAND-AUTHORED page.

Generated families are skipped here because their generators call link_page()
themselves (editing their output would be erased on the next run):
  wrestlers/<slug>/ with a build/wldata module (build_dossier.py), lore-feed/
  (build_lorefeed.py), gallery/ and media/w/ (build_gallery.py), promotions/raf/
  (build_raf.py), the build/facdata factions (build_factions.py), rankings/ and the
  /matches/ hub (build_rankings*.py). Idempotent.

    WL_ROOT="$PWD" python3 build/link_sitewide.py
Then: python3 build/apply_shell.py
"""
import glob, os, sys
ROOT = os.environ.get("WL_ROOT", os.getcwd())
sys.path.insert(0, os.path.join(ROOT, "build"))
import wl_links

SKIP_PREFIX = ("zh/", "china/", "content/", "docs/", "assets/", "_", "archive/",
               "lore-feed/", "gallery/", "media/", "promotions/raf/", "rankings/",
               "membership/")  # conversion pages keep exits minimal
SKIP_EXACT = {"index.html", "404.html", "matches/index.html"}
gen_wrestlers = {os.path.splitext(f)[0].replace("_", "-") for f in os.listdir(os.path.join(ROOT, "build", "wldata"))
                 if f.endswith(".py") and not f.startswith("_")}
gen_factions = {os.path.splitext(f)[0] for f in os.listdir(os.path.join(ROOT, "build", "facdata")) if f.endswith(".py")}

total = changed = 0
for p in sorted(glob.glob(os.path.join(ROOT, "**", "index.html"), recursive=True)):
    rel = os.path.relpath(p, ROOT)
    if rel in SKIP_EXACT or rel.startswith(SKIP_PREFIX):
        continue
    parts = rel.split("/")
    if parts[0] == "wrestlers" and len(parts) == 3 and parts[1] in gen_wrestlers:
        continue
    if parts[0] == "factions" and len(parts) == 3 and parts[1] in gen_factions:
        continue
    s = open(p, encoding="utf-8").read()
    s2 = wl_links.link_page(s, rel)
    total += 1
    if s2 != s:
        open(p, "w", encoding="utf-8").write(s2)
        changed += 1
print("hand-authored pages scanned: %d, gained links: %d" % (total, changed))
