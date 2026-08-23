#!/usr/bin/env python3
"""ONE-TIME MIGRATION — hand-authored dossiers -> the merged PROSE & SPREAD pass.

The 8 generated dossiers get this markup from build_dossier.py (sec_overview /
rail()).  The five hand-authored pages (cm-punk, john-cena, aj-styles,
the-rock, triple-h) have no data module, so their existing HTML is transformed
in place:

  1. The Tale-of-the-Tape credibility control is reworded from the cryptic
     fraction ("10/14 SOURCED") to count + noun ("10 SOURCE NOTES") — the same
     wording build_dossier.py now emits.  The title attribute keeps the full
     fraction sentence; js/rail.js keeps the full-sentence accessible name.

  2. 2-3 aria-hidden margin pull-facts (.pull spans, css/dossier.css
     "PROSE & SPREAD" section 7) are inserted at exact text anchors.  Every
     pull DUPLICATES a fact already present in the page's own overview text,
     so hiding it below 1600px loses nothing.  Facts only — nothing invented.

  3. The correction callout (aside.corr) is NOT added to any of these pages:
     none of the four present hand-authored overviews contains a correction
     paragraph (checked by reading them), and none is fabricated.  A future
     hand-authored page that gains one can be added to CORR below using the
     same wrap-the-existing-<p> approach as proto B's patch.py.

GUARANTEES (modelled on migrate_tape.py)
  * idempotent — a page already carrying .pull markup gets no second set, a
    reworded control is not re-reworded, and the second pass is proved to be
    a byte-for-byte no-op per run;
  * every anchor must occur exactly once or the page is aborted un-written;
  * no .orig backups are written — the transform is additive and re-runnable.

Usage:  WL_ROOT=/path/to/site python3 build/migrate_prose.py [--check] [slug ...]
        --check  report only, write nothing.
"""
import os, re, sys, hashlib

ROOT = os.environ.get("WL_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# `the-rock` is listed because the dossier index still names it; it has no
# directory in this tree and is reported as absent rather than silently skipped.
HAND = ["cm-punk", "john-cena", "aj-styles", "the-rock", "triple-h"]

CRED_RE = re.compile(r'<span class="tt-n">(\d+)/(\d+)</span><span class="tt-lbl">sourced</span>')
CRED_NEW = '<span class="tt-n">\\1</span><span class="tt-lbl">source notes</span>'
CRED_DONE_RE = re.compile(r'<span class="tt-lbl">source notes</span>')


def pull(fig, cap, small=False):
    cls = "pull-fig pull-fig--sm" if small else "pull-fig"
    return ('<span class="pull" aria-hidden="true">'
            '<span class="%s">%s</span>'
            '<span class="pull-cap">%s</span></span>' % (cls, fig, cap))

# slug -> list of (anchor, html inserted immediately BEFORE the anchor).
# Each fact is present verbatim in the page's own overview prose.
PULLS = {
    "cm-punk": [
        ("He arrived in WWE in 2006 and spent",
         pull("JUNE&nbsp;27, 2011", "the &ldquo;pipe bomb&rdquo; &mdash; the most-watched "
              "WWE promo of the YouTube era", small=True)),
        ("The reign that followed ran <b>434 days</b>",
         pull("434", "days as WWE Champion &mdash; the longest reign of the modern era")),
        ("Punk walked out of WWE the night after",
         pull("12", "world championships held across ROH, ECW, WWE and AEW")),
    ],
    "john-cena": [
        ("Across a <b>26-year career</b> he carried",
         pull("17", "world championships &mdash; the WWE record, sealed at WrestleMania 41")),
        ("His peak was defined by extraordinary longevity",
         pull("380", "days holding the WWE Championship &mdash; a modern-era mark")),
        ("In 2025 Cena ran a year-long farewell tour",
         pull("650+", "Make-A-Wish wishes granted &mdash; the record")),
    ],
    "aj-styles": [
        ("He is, by acclaim, one of the greatest in-ring performers",
         pull("1ST", "NWA-TNA&rsquo;s first-ever Triple Crown and Grand Slam Champion")),
        ("A 2014 move to <b>New Japan</b> reinvented him",
         pull("371", "days in his second WWE Championship reign")),
    ],
    "triple-h": [
        ("he trained under",
         pull("14", "world championships won across the WWF/WWE and World Heavyweight lineages")),
        ("His cerebral, methodical style was the perfect foil",
         pull("7", "WrestleMania main events")),
        ("In 2022 he replaced Vince McMahon",
         pull("2022", "replaced Vince McMahon as Chief Content Officer; opened WWE&rsquo;s "
              "Netflix era in January 2025", small=True)),
    ],
}

# No hand-authored page currently carries a correction paragraph; see module
# docstring.  Format if one appears: slug -> anchor inside the <p> to wrap.
CORR = {}
CORR_KICK = '<h3 class="corr-kick">Setting one thing straight</h3>'


def migrate(path, slug, check=False):
    src = open(path, encoding="utf-8").read()
    out = src
    msgs = []

    # 1. tt-cred reword ------------------------------------------------------
    if CRED_DONE_RE.search(out):
        msgs.append("cred already reworded")
    else:
        n = len(CRED_RE.findall(out))
        if n != 1:
            return "ABORT: tt-cred fraction found %d times, expected 1" % n, False
        out = CRED_RE.sub(CRED_NEW, out, count=1)
        msgs.append("cred reworded")

    # 2. margin pulls --------------------------------------------------------
    if 'class="pull"' in out:
        msgs.append("pulls already present (%d)" % out.count('class="pull"'))
    else:
        for anchor, ins in PULLS.get(slug, []):
            if out.count(anchor) != 1:
                return "ABORT: pull anchor found %d times: %r" % (out.count(anchor), anchor[:50]), False
            out = out.replace(anchor, ins + anchor, 1)
        msgs.append("%d pulls inserted" % len(PULLS.get(slug, [])))

    # 3. correction callout --------------------------------------------------
    if slug in CORR and 'class="corr"' not in out:
        a = CORR[slug]
        if out.count(a) != 1:
            return "ABORT: corr anchor found %d times" % out.count(a), False
        i = out.find(a)
        p_open = out.rfind("<p ", 0, i)
        p_close = out.find("</p>", i) + len("</p>")
        out = (out[:p_open] + '<aside class="corr">' + CORR_KICK
               + out[p_open:p_close] + "</aside>" + out[p_close:])
        msgs.append("corr wrapped")

    changed = out != src
    if changed and not check:
        open(path, "w", encoding="utf-8").write(out)
    return "; ".join(msgs) + ("" if changed else " [no change]"), changed


def main(argv):
    check = "--check" in argv
    slugs = [a for a in argv if not a.startswith("--")] or HAND
    rc = 0
    for slug in slugs:
        path = os.path.join(ROOT, "wrestlers", slug, "index.html")
        if not os.path.exists(path):
            print("  %-12s ABSENT — no page at wrestlers/%s/index.html" % (slug, slug))
            continue
        msg, changed = migrate(path, slug, check)
        if msg.startswith("ABORT"):
            rc = 1
        print("  %-12s %s" % (slug, msg))
        if not check and not msg.startswith("ABORT"):
            # idempotence, proved rather than asserted
            before = hashlib.md5(open(path, "rb").read()).hexdigest()
            m2, c2 = migrate(path, slug, False)
            after = hashlib.md5(open(path, "rb").read()).hexdigest()
            if c2 or after != before:
                print("  %-12s ABORT: second pass was not a no-op (%s)" % (slug, m2)); rc = 1
            else:
                print("  %-12s idempotent (md5 %s stable over two passes)" % (slug, before[:10]))
    print("done. now run: python3 build/apply_shell.py")
    return rc


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
