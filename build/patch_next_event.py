#!/usr/bin/env python3
"""patch_next_event.py - stamp the next event from eventsdata.py into the pages.

    WL_ROOT="$PWD" python3 build/patch_next_event.py [--check]

--check reports what is stale and writes nothing; use it in CI or before a
deploy to find out that the homepage is lying before a visitor does.

HOW IT FINDS THE SPOTS. Not by line number - lines move. Each target is a
regex anchored on markup that is structural (a class name, an attribute) with
the volatile part as the capture group. Rerunning on already-patched output is
a no-op, which is what makes this safe to wire into the build.

WHAT IT DELIBERATELY DOES NOT DO. It does not touch /events/tickets/, which
carries a full page of SummerSlam sale copy plus a dead Survivor Series
presale countdown. That page needs prose rewritten, not strings swapped, and a
regex that tried would mangle it.
"""

import os, re, sys, importlib.util

ROOT = os.environ.get("WL_ROOT", os.getcwd())
HERE = os.path.dirname(os.path.abspath(__file__))

spec = importlib.util.spec_from_file_location("eventsdata", os.path.join(HERE, "eventsdata.py"))
ED = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ED)

CHECK = "--check" in sys.argv


def esc(s):
    """For HTML text nodes and double-quoted attributes."""
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def jsq(s):
    """For a value being dropped inside a JS SINGLE-quoted string literal.

    This is not paranoia, it is a bug that shipped in the first run of this
    script. The next event is "Sunday Night's Main Event". Two of the targets
    below sit inside `sub:'...'` and `vig.innerHTML='...'` - single-quoted JS -
    so the raw apostrophe closed the literal early and left `S MAIN EVENT...`
    as loose syntax. The homepage's whole production-truck module stopped
    parsing. HTML escaping does not help here; only backslash-escaping the
    quote does. Backslashes first, or you escape your own escapes.
    """
    return s.replace("\\", "\\\\").replace("'", "\\'")


def build_targets():
    n = ED.next_event()
    also = ED.also_on_sale()

    NAME = esc(n["name"])
    SHORT = esc(n["short"])
    WHEN = esc(n["when"])
    WHERE = esc(n["venue"] + ", " + n["city"])
    ROW = esc(n["row"])
    CITYSHORT = esc(n["cityshort"])
    VENUE_U = n["venue"].upper()
    CITY_U = n["cityshort"].upper()
    NAME_U = n["short"].upper()
    NIGHTS = "TWO NIGHTS" if n.get("nights", 1) > 1 else "ONE NIGHT"

    also_rows = "".join(
        '<a class="wev-a-row" href="%s" target="_blank" rel="noopener">'
        '<b>%s</b> %s, %s</a>' % (e["tickets"], esc(e["row"]), esc(e["short"]), esc(e["cityshort"]))
        for e in also
    )

    T = []

    # 1. The ticker strip. NOT index.html - components/meganav.html.
    #
    #    Patching index.html here "worked" and then silently un-worked: the
    #    strip lives in the shared nav component, and build/apply_shell.py
    #    stamps that component over the <header> of all 489 pages, restoring
    #    the stale copy on the very next build. Editing generated output is
    #    editing something the build is about to overwrite. It also means the
    #    dead SummerSlam line was on every page of the site, not just home.
    #
    #    ORDERING: this script must run BEFORE apply_shell.py, so the fresh
    #    component is what gets stamped.
    T.append((
        "components/meganav.html", "evlive name+date",
        re.compile(r'(<span class="evlive-nm">)(.*?)(</span>)'),
        r'\g<1>%s <b class="evlive-next">%s</b>\g<3>' % (SHORT, ROW),
    ))
    T.append((
        "components/meganav.html", "evlive venue line",
        re.compile(r'(<span class="evlive-meta">)(.*?)(</span>)'),
        r'\g<1>%s, %s &middot; %d more shows on sale\g<3>' % (esc(n["venue"]), CITYSHORT, len(also)),
    ))

    # 2. the CAM 3 strapline in the production-truck feed list
    #    `([^']*)` was wrong here: it stops at the first quote, and the value
    #    going IN contains one, so the tail of the old string survived and the
    #    new text was appended to it. Anchor on the real terminator - the
    #    closing quote followed by `},` - and match lazily.
    T.append((
        "index.html", "FEEDS events sub",
        re.compile(r"(\{id:'events',cam:'CAM 3',name:'Events',s:'2026 SEASON',href:'/events/',sub:')(.*?)('\},)"),
        lambda m: m.group(1) + jsq("%s // %s // %s" % (NAME_U, VENUE_U, CITY_U)) + m.group(3),
    ))

    # 3. The production-truck vignette: kicker, footer line and countdown
    #    target, present in BOTH index.html (an inline copy) and
    #    js/home-modules.js.
    #
    #    ONE regex spanning the whole block, not three anchors. The first
    #    draft matched the countdown on `var T=new Date('...')` alone, and
    #    --check caught it firing TWICE in index.html: the second hit was the
    #    Hall of Fame count-up clock at line 2574, ticking up from induction
    #    day. Patching that to the next PLE date would have silently broken an
    #    unrelated widget. An anchor has to be specific to the thing it means,
    #    and `new Date` is not - so the match now must BEGIN at this
    #    vignette's own kicker and run to its own timer.
    VIG = re.compile(
        r'(<span class="ptk-kl">NEXT STOP // )([^<]*)'      # 1 open, 2 kicker
        r'(</span>.*?<div class="ptk-under">)([^<]*)'        # 3 middle,  4 footer
        r"(</div>';\s*var T=new Date\(')([^']*)(')",        # 5 join, 6 date, 7 close
        re.S,
    )

    def vig_sub(m):
        # both of these land inside vig.innerHTML='...' - JS-escape, not HTML
        return (m.group(1) + jsq("%s // %s" % (NAME_U, n["row"].upper()))
                + m.group(3) + jsq("%s // %s // %s" % (VENUE_U, CITY_U, NIGHTS))
                + m.group(5) + n["start"] + m.group(7))

    for f in ("index.html", "js/home-modules.js"):
        T.append((f, "vignette kicker+footer+timer", VIG, vig_sub))

    # 5. the floating widget: tab label, name, countdown target, when, where,
    #    the ticket link, and the also-on-sale rows.
    T.append((
        "index.html", "widget tab label",
        re.compile(r'(<span class="wev-a-tab-lbl">)([^<]*)(</span>)'),
        r'\g<1>%s\g<3>' % SHORT,
    ))
    T.append((
        "index.html", "widget name",
        re.compile(r'(<h3 class="wev-a-name">)([^<]*)(</h3>)'),
        r'\g<1>%s\g<3>' % SHORT,
    ))
    T.append((
        "index.html", "widget timer aria-label",
        re.compile(r'(aria-label="Countdown to )([^"]*)(")'),
        r'\g<1>%s\g<3>' % SHORT,
    ))
    T.append((
        "index.html", "widget when",
        re.compile(r'(<p class="wev-a-when">)([^<]*)(</p>)'),
        r'\g<1>%s\g<3>' % WHEN,
    ))
    T.append((
        "index.html", "widget where",
        re.compile(r'(<p class="wev-a-where">)([^<]*)(</p>)'),
        r'\g<1>%s\g<3>' % WHERE,
    ))
    T.append((
        "index.html", "widget ticket link",
        re.compile(r'(<a class="wev-a-cta" href=")([^"]*)(")'),
        r'\g<1>%s\g<3>' % n["tickets"],
    ))
    T.append((
        "index.html", "widget also-on-sale rows",
        re.compile(r'(<p class="wev-a-also-k">Also on sale</p>)(.*?)(</div>)', re.S),
        lambda m: m.group(1) + also_rows + m.group(3),
    ))
    T.append((
        "index.html", "widget countdown target",
        re.compile(r"(var target=new Date\(')([^']*)('\)\.getTime\(\);)"),
        r"\g<1>%s\g<3>" % n["start"],
    ))

    return n, T


def main():
    n, targets = build_targets()
    files = {}
    changed_files = set()
    misses, hits, nochange = [], [], []

    for fname, label, rx, repl in targets:
        path = os.path.join(ROOT, fname)
        if fname not in files:
            if not os.path.exists(path):
                misses.append("%s :: %s (FILE MISSING)" % (fname, label))
                continue
            with open(path, encoding="utf-8") as fh:
                files[fname] = fh.read()
        before = files[fname]
        after, cnt = rx.subn(repl, before)
        if cnt == 0:
            misses.append("%s :: %s (NO MATCH)" % (fname, label))
        elif after == before:
            nochange.append("%s :: %s" % (fname, label))
        else:
            hits.append("%s :: %s (x%d)" % (fname, label, cnt))
            files[fname] = after
            changed_files.add(fname)

    print("next event: %s - %s - %s, %s" % (n["name"], n["when"], n["venue"], n["city"]))
    for h in hits:
        print("  UPDATED  ", h)
    for c in nochange:
        print("  current  ", c)
    for m in misses:
        print("  !! MISS  ", m)

    # A miss means the markup moved and this patcher silently stopped covering
    # a spot. That is exactly how the original six copies drifted, so it is a
    # hard failure, not a warning.
    if misses:
        raise SystemExit("\n%d target(s) did not match. Fix the anchors before shipping." % len(misses))

    if CHECK:
        print("\n--check: %d spot(s) stale, nothing written." % len(hits))
        raise SystemExit(1 if hits else 0)

    for fname in sorted(changed_files):
        with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as fh:
            fh.write(files[fname])
    print("\nwrote %d file(s): %s" % (len(changed_files), ", ".join(sorted(changed_files)) or "none"))


if __name__ == "__main__":
    main()
