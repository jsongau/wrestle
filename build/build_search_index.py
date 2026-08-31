#!/usr/bin/env python3
"""build_search_index.py - regenerate js/search-index.js from the site itself.

    WL_ROOT="$PWD" python3 build/build_search_index.py

Run BEFORE apply_shell.py, so the pages' ?v= cache-bust hashes pick up the
new file.

WHY THIS EXISTS. The command-palette index was a hand-maintained file that
nothing in the build regenerated - every generator wrote a <script src> tag
pointing at it and none of them wrote INTO it. It froze on Aug 4, 2026 at
209 entries while the site grew to 512 pages. The owner found out by
searching "tyr" for a profile that had been live for a week and getting
Drew McIntyre. If a page is worth building, it is worth being findable by
the person the site belongs to.

WHAT IS PRESERVED. The old index carried hand-curated aliases ("hhh" finds
Triple H, "brahma bull" finds The Rock) and hand-tuned display names. Those
cannot be derived from the pages, so this script KEEPS every existing entry
whose URL still resolves, verbatim, and only APPENDS what is missing. It
never rewrites a curated row. Deleting a page removes its row on the next
run.

ORDERING MATTERS. nav.js scores exact=100 / prefix=80 / substring=50 /
token-start=40 and ties keep array order, so within an equal score the
array decides what a person sees first. Curated entries stay first; new
sections follow by how likely a human is to be searching for them; the 218
video pages go dead last so a three-letter query surfaces Tyron Woodley,
not six weeks of Raw highlight clips.
"""

import html
import json
import os
import re

ROOT = os.environ.get("WL_ROOT", os.getcwd())
OUT = os.path.join(ROOT, "js", "search-index.js")

SKIP_DIRS = {"_to_delete", ".git", ".deploy_trash", ".wl_tmp5", "node_modules",
             "components", "build", "js", "css", "fonts", "assets", "docs"}

# url-prefix -> (kind chip, weight). Lower weight sorts earlier among ADDED rows.
# The kind chip text renders in the palette; wrestler/match/event/moment have
# styled chips in css and everything else falls back to the default chip look.
SECTIONS = [
    ("wrestlers/",               "Wrestler",   0),
    ("promotions/raf/athletes/", "Wrestler",   1),
    ("factions/",                "Faction",    2),
    ("tag-teams/",               "Tag Team",   3),
    ("titles/",                  "Title",      4),
    ("events/",                  "Event",      5),
    ("promotions/raf/raf-",      "Event",      6),
    ("matches/",                 "Match",      7),
    ("rivalries/",               "Rivalry",    8),
    ("moments/",                 "Moment",     9),
    ("promotions/",              "Promotion", 10),
    ("hall-of-fame/",            "Hall of Fame", 11),
    ("lore-feed/",               "Lore Feed", 12),
    ("gallery/",                 "Recap",     13),
    ("rankings/",                "Hub",       14),
    ("media/w/",                 "Video",     99),   # dead last, see docstring
    ("media/",                   "Media",     15),
    ("",                         "Page",      50),
]


def section_for(u):
    p = u.strip("/") + "/"
    for prefix, kind, weight in SECTIONS:
        if p.startswith(prefix):
            return kind, weight
    return "Page", 50


CRUMB = re.compile(r'aria-current="page"[^>]*>([^<]+)<')
TITLE = re.compile(r"<title>(.*?)</title>", re.S)


def clean(t):
    t = html.unescape(t).strip()
    t = re.sub(r"\s+", " ", t)
    return t


def page_name(path, url):
    """Best display name for a page, most-reliable source first."""
    try:
        with open(path, encoding="utf-8") as fh:
            s = fh.read(20000)  # name lives in <head>/breadcrumb; skip the rest
    except OSError:
        return None
    # 1. breadcrumb current-page text - already the human name. Validate hard:
    #    on one template the regex can land inside an inline <style> block, so
    #    anything that looks like CSS or runs long is rejected.
    m = CRUMB.search(s)
    if m:
        c = clean(m.group(1))
        if c and len(c) <= 80 and not re.search(r"[{};]|display:|\.[a-z-]+,", c):
            return c
    # 2. <title>, stripped of the site suffix, then cut at the first separator
    #    ("Tyron Woodley: RAF Record and Profile" -> "Tyron Woodley").
    m = TITLE.search(s)
    if m:
        t = clean(m.group(1))
        t = re.sub(r"\s*\|\s*Wrestle Lore.*$", "", t)
        for sep in (" — ", " – ", ": "):
            if sep in t:
                left = t.split(sep)[0].strip()
                # keep "CM Punk vs John Cena — Money in the Bank (2011)" whole:
                # a "vs" page's name IS both sides of the separator
                if " vs " in left.lower() and sep != ": ":
                    t = re.sub(r"\s*(Match Review|Review).*$", "", t).strip()
                else:
                    t = left
                break
        if t:
            return t
    return None


def live_pages():
    for r, dirs, files in os.walk(ROOT):
        rel = os.path.relpath(r, ROOT)
        # At the walk's root, relpath is "." - which the hidden-dir rule below
        # would match, pruning every subdirectory and ending the walk with
        # zero pages. First run did exactly that and emptied the index (the
        # run report - "kept 0, dropped 209" - made it obvious before it
        # shipped; that report exists for this reason).
        if rel == ".":
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
            continue
        top = rel.split(os.sep)[0]
        if top in SKIP_DIRS or top.startswith("."):
            dirs[:] = []
            continue
        if "index.html" in files:
            yield "/" + rel.replace(os.sep, "/") + "/"


def main():
    with open(OUT, encoding="utf-8") as fh:
        s = fh.read()
    existing = json.loads(s[s.index("["):s.rindex("]") + 1])

    live = set(live_pages())
    kept = [e for e in existing if e["u"] in live]
    dropped = [e["u"] for e in existing if e["u"] not in live]
    have = {e["u"] for e in kept}

    added = []
    for u in sorted(live - have):
        kind, weight = section_for(u)
        path = os.path.join(ROOT, u.strip("/"), "index.html")
        name = page_name(path, u)
        if not name:
            print("  !! no name derivable, skipped:", u)
            continue
        added.append({"t": name, "u": u, "k": kind, "_w": weight})

    added.sort(key=lambda e: (e.pop("_w"), e["t"]))
    out = kept + added

    payload = "window.MAT_SEARCH_INDEX=" + json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\n"
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(payload)

    print("kept %d curated entries (aliases intact), added %d, dropped %d dead"
          % (len(kept), len(added), len(dropped)))
    for d in dropped:
        print("  dropped (page gone):", d)
    print("total: %d entries for %d live pages -> %s" % (len(out), len(live), os.path.relpath(OUT, ROOT)))


if __name__ == "__main__":
    main()
