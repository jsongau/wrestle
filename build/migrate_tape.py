#!/usr/bin/env python3
"""ONE-TIME MIGRATION — hand-authored dossiers -> the folded Tale of the Tape.

The 8 generated dossiers get this markup from build_dossier.py's rail().  The
five hand-authored pages (cm-punk, john-cena, aj-styles, the-rock, triple-h)
have no data module, so their existing HTML is transformed in place, to exactly
the same shape:

    <div class="row"><dt>L</dt><dd>VALUE <span class="cm">NOTE</span></dd></div>
      ->
    <div class="row row--src"><dt>L</dt><dd><details class="tsrc">
       <summary class="tsrc-v"><span class="tsrc-p">VALUE</span>
       <span class="tsrc-ic" aria-hidden="true"></span></summary>
       <span class="cm tsrc-n">NOTE</span></details></dd></div>

A row with no <span class="cm"> has nothing to disclose and is left byte-for-byte
alone.  The card also gains `data-tape`, a `.tt-head` wrapper carrying the
credibility line, an id on the <dl>, and the /js/rail.js tag.

GUARANTEES
  * idempotent — a card already carrying `data-tape` is skipped, and running
    the script twice is a no-op (verified by re-hashing the file);
  * every row's text is preserved exactly — the value and the note are the same
    strings, only re-parented.  `.tott dd .cm` is display:block, so the value
    and the note were already on separate lines: the rendered text does not
    move either;
  * the number of <span class="cm"> notes is asserted equal before and after,
    per file.  A mismatch aborts before anything is written.

Usage:  WL_ROOT=/path/to/site python3 build/migrate_tape.py [--check] [slug ...]
        --check  report only, write nothing.
"""
import os, re, sys, hashlib

ROOT = os.environ.get("WL_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The pages with no wldata module. `the-rock` is listed because the dossier
# index still names it; it has no directory in this tree and is reported as
# absent rather than silently skipped.
HAND = ["cm-punk", "john-cena", "aj-styles", "the-rock", "triple-h"]

RAIL_RE  = re.compile(r'<aside class="rail"[^>]*>.*?</aside>', re.S)
CARD_RE  = re.compile(r'(<section class="card tott")(\s[^>]*)?(>)')
ROW_RE   = re.compile(r'<div class="row"(?P<attr>[^>]*)>(?P<dt><dt>.*?</dt>)<dd>(?P<dd>.*?)</dd></div>', re.S)
CM_RE    = re.compile(r'^(?P<val>.*?)\s*<span class="cm">(?P<sub>.*)</span>\s*$', re.S)
H2_RE    = re.compile(r'(?P<h2><h2 id="tott-h" class="kick">Tale of the Tape</h2>)')
DL_RE    = re.compile(r'<dl(?P<attr>[^>]*)>')
NOTE_RE  = re.compile(r'<span class="cm[ "]')
SCRIPT_RE = re.compile(r'<script src="/js/rail\.js(\?[^"]*)?"')
ANCHOR_RE = re.compile(r'(<script src="/js/profile\.js(?:\?[^"]*)?"[^>]*></script>)')
BODY_RE   = re.compile(r'</body>')

ROW_SRC = ('<div class="row row--src"%s>%s<dd>'
           '<details class="tsrc"><summary class="tsrc-v">'
           '<span class="tsrc-p">%s</span><span class="tsrc-ic" aria-hidden="true"></span>'
           '</summary><span class="cm tsrc-n">%s</span></details></dd></div>')


def transform_rail(rail_html):
    """Return (new_rail, n_rows, n_sourced) or (rail_html, ...) if already done."""
    if 'data-tape' in rail_html:
        return rail_html, None, None, True            # already migrated

    n_rows = [0]
    n_src = [0]

    def row(m):
        n_rows[0] += 1
        attr, dt, dd = m.group("attr"), m.group("dt"), m.group("dd")
        cm = CM_RE.match(dd)
        if not cm:
            return m.group(0)                          # nothing to disclose
        n_src[0] += 1
        return ROW_SRC % (attr, dt, cm.group("val"), cm.group("sub"))

    out = ROW_RE.sub(row, rail_html)

    # card gets data-tape so js/rail.js and the CSS state classes engage
    out = CARD_RE.sub(lambda m: m.group(1) + " data-tape" + (m.group(2) or "") + m.group(3), out, count=1)

    # <dl> gets the id the control's aria-controls points at
    def dl(m):
        return m.group(0) if 'id=' in m.group("attr") else '<dl id="tott-dl"%s>' % m.group("attr")
    out = DL_RE.sub(dl, out, count=1)

    # header wrapper + the credibility line, on the title's own baseline
    cred = ('<p class="tt-cred" title="%d of %d entries carry a source note">'
            '<span class="tt-n">%d/%d</span><span class="tt-lbl">sourced</span></p>'
            % (n_src[0], n_rows[0], n_src[0], n_rows[0])) if n_rows[0] else ""
    out = H2_RE.sub(lambda m: '<div class="tt-head">' + m.group("h2") + cred + '</div>', out, count=1)

    return out, n_rows[0], n_src[0], False


def add_script(html):
    if SCRIPT_RE.search(html):
        return html, False
    tag = '<script src="/js/rail.js"></script>'
    if ANCHOR_RE.search(html):
        return ANCHOR_RE.sub(lambda m: m.group(1) + "\n" + tag, html, count=1), True
    if BODY_RE.search(html):
        return BODY_RE.sub(tag + "\n</body>", html, count=1), True
    return html + "\n" + tag + "\n", True


def migrate(path, check=False):
    src = open(path, encoding="utf-8").read()
    notes_before = len(NOTE_RE.findall(src))
    rails = RAIL_RE.findall(src)
    if not rails:
        return "no .rail — nothing to migrate", False
    if len(rails) > 1:
        return "ABORT: %d .rail blocks, expected 1" % len(rails), False

    new_rail, n_rows, n_src, already = transform_rail(rails[0])
    out = src.replace(rails[0], new_rail, 1)
    out, added_script = add_script(out)

    notes_after = len(NOTE_RE.findall(out))
    if notes_after != notes_before:
        return "ABORT: source-note count changed %d -> %d" % (notes_before, notes_after), False

    changed = out != src
    if changed and not check:
        open(path, "w", encoding="utf-8").write(out)
    if already:
        msg = "already migrated%s" % ("; +rail.js" if added_script else "")
    else:
        msg = "%d rows, %d sourced (notes %d==%d)%s" % (
            n_rows, n_src, notes_before, notes_after, "; +rail.js" if added_script else "")
    return msg + ("" if changed else " [no change]"), changed


def main(argv):
    check = "--check" in argv
    slugs = [a for a in argv if not a.startswith("--")] or HAND
    rc = 0
    for slug in slugs:
        path = os.path.join(ROOT, "wrestlers", slug, "index.html")
        if not os.path.exists(path):
            print("  %-12s ABSENT — no page at wrestlers/%s/index.html" % (slug, slug))
            continue
        msg, changed = migrate(path, check)
        after = hashlib.md5(open(path, "rb").read()).hexdigest()
        if msg.startswith("ABORT"):
            rc = 1
        print("  %-12s %s" % (slug, msg))
        if not check:
            # idempotence, proved rather than asserted: a second pass must be a no-op
            m2, c2 = migrate(path, False)
            again = hashlib.md5(open(path, "rb").read()).hexdigest()
            if c2 or again != after:
                print("  %-12s ABORT: second pass was not a no-op (%s)" % (slug, m2)); rc = 1
            else:
                print("  %-12s idempotent (md5 %s stable over two passes)" % (slug, after[:10]))
    print("done. now run: python3 build/apply_shell.py")
    return rc


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
