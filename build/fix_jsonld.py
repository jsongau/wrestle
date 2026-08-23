#!/usr/bin/env python3
r"""fix_jsonld.py - repair invalid JSON-LD across the roster, and report what is left.

THE BUG THIS FIXES
------------------
60 of 108 /wrestlers/ pages shipped a structured-data block that is not valid JSON.
The FAQPage nodes were hand-written with SINGLE-quoted string values:

    {"@type":"Question","name":'Why did WALTER become Gunther?', ...}

JSON has no single-quoted strings. A parser rejects the whole <script> block at the
first one, so Google discarded not just the FAQ but the Person, WebPage and
BreadcrumbList nodes sharing that block. Sixty pages were emitting zero usable
structured data while looking completely fine in a browser.

There are TWO defect classes, and 13 pages carry both:

  A. single-quoted string values, as above;
  B. single-quoted values that themselves CONTAIN an apostrophe:

        "text":'Glenn Thomas Jacobs. He was elected Knox County's mayor in 2018.'

     A naive [^']* scan stops at the inner apostrophe and produces garbage, which
     is why a first version of this script repaired only 47 of the 60 pages.

The disambiguation: in this corpus a single-quoted value always ends with an
apostrophe followed by a JSON structural character - , } or ] - while an
apostrophe INSIDE the prose never is. So the scanner accepts an inner apostrophe
and only treats one as terminal when a structural character follows it.

  C. a trailing comma before a closing bracket - "}},]} - which JSON also rejects.

Each defect was found by repairing the previous one and re-parsing what was left,
rather than by assuming the first cause was the only cause.

Verified before writing: no affected value contains a double quote, so re-quoting
through json.dumps is lossless. Every page is re-parsed after the rewrite and the
script refuses to save a file it cannot validate.

Idempotent: a page whose blocks already parse is left untouched.

    WL_ROOT="$PWD" python3 build/fix_jsonld.py [--dry-run] [glob ...]
"""

import glob as _glob, json, os, re, sys

ROOT = os.environ.get("WL_ROOT", os.getcwd())
BLOCK = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.S)
KEYS = "name|text|description|headline|alternateName"
# An inner apostrophe is kept; only an apostrophe followed by , } or ] closes the value.
SQ = re.compile(r'("(?:%s)"\s*:\s*)\'((?:[^\']|\'(?!\s*[,}\]]))*)\'(?=\s*[,}\]])' % KEYS)

TRAILING = re.compile(r',(\s*[}\]])')

def repair(block):
    """Re-quote single-quoted values and drop trailing commas. Returns (text, n)."""
    n = [0]
    def sub(m):
        n[0] += 1
        return m.group(1) + json.dumps(m.group(2), ensure_ascii=False)
    out = SQ.sub(sub, block)
    out, k = TRAILING.subn(r'\1', out)
    return out, n[0] + k

def process(path, dry=False):
    h = open(path, encoding="utf-8").read()
    bad_before = fixed = still_bad = 0
    out = []
    last = 0
    for m in BLOCK.finditer(h):
        body = m.group(2)
        try:
            json.loads(body)
            continue                      # already valid, leave it exactly as-is
        except Exception:
            bad_before += 1
        new, n = repair(body)
        try:
            json.loads(new)
        except Exception:
            still_bad += 1                # could not repair; do NOT touch it
            continue
        fixed += 1
        out.append((m.start(2), m.end(2), new))
    if out and not dry:
        buf = []
        for s, e, new in out:
            buf.append(h[last:s]); buf.append(new); last = e
        buf.append(h[last:])
        h2 = "".join(buf)
        # never save a file whose blocks do not all parse
        for m in BLOCK.finditer(h2):
            json.loads(m.group(2))
        open(path, "w", encoding="utf-8").write(h2)
    return bad_before, fixed, still_bad

def main(argv):
    dry = "--dry-run" in argv
    pats = [a for a in argv if not a.startswith("--")] or ["wrestlers/*/index.html"]
    files = []
    for p in pats:
        files += sorted(_glob.glob(os.path.join(ROOT, p)))
    tb = tf = ts = tp = 0
    unfixable = []
    for f in files:
        b, fx, sb = process(f, dry)
        if b: tp += 1
        tb += b; tf += fx; ts += sb
        if sb: unfixable.append(os.path.relpath(f, ROOT))
    print("scanned %d files" % len(files))
    print("pages with invalid JSON-LD : %d" % tp)
    print("blocks repaired            : %d%s" % (tf, "  (dry run, nothing written)" if dry else ""))
    print("blocks still unparseable   : %d" % ts)
    for u in unfixable:
        print("   NEEDS MANUAL FIX:", u)
    return 1 if ts else 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
