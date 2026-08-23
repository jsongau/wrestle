#!/usr/bin/env python3
"""patch_sig_links.py - apply the Signature-Matches link + hover-preview component
to the HAND-AUTHORED dossier pages (cm-punk, john-cena), which predate
build/build_dossier.py and so are never regenerated.

It shares one implementation with the generator: every card is parsed back out of
the markup into the same {rating,event,opponent,stip} dict the data modules use,
then re-emitted through build_dossier.sig_card(). So a hand page and a generated
page can never drift, and both obey the same hard rule - a card is only ever
linked to a path that exists on disk. Cards with no breakdown page stay inert
<div>s; no stubs are invented to make the section look complete.

Idempotent. Re-run after adding any page under /matches/ and the cards that now
have a target light up on their own.

Run:  WL_ROOT="$PWD" python3 build/patch_sig_links.py [slug ...]
"""
import importlib.util, os, re, sys

ROOT = os.environ.get("WL_ROOT", os.getcwd())
os.environ.setdefault("WL_ROOT", ROOT)
_s = importlib.util.spec_from_file_location(
    "build_dossier", os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_dossier.py"))
bd = importlib.util.module_from_spec(_s); _s.loader.exec_module(bd)

HAND = ["cm-punk", "john-cena", "aj-styles"]
# Anchored on the card's full shape rather than on "first matching close tag":
# a .sig2-card contains a nested <div class="sig2-top">, so a lazy (.*?)</\1>
# would stop at that inner </div> and silently skip every non-link card.
CARD = re.compile(r'<(a|div) class="sig2-card[^"]*"[^>]*>'
                  r'(<div class="sig2-top">.*?<p class="sig2-stip">.*?</p>)</\1>', re.S)
SCRIPT = '<script src="/js/sig-preview.js" defer></script>'

def field(inner, cls, tag="p"):
    m = re.search(r'<%s class="%s"[^>]*>(.*?)</%s>' % (tag, cls, tag), inner, re.S)
    return m.group(1).strip() if m else ""

def parse(inner):
    """Recover the card's data from its own markup - the inverse of sig_card()."""
    return dict(
        rating=field(inner, "sig2-rate", "span"),
        event=bd._sig_text(field(inner, "sig2-ev", "h3")),
        opponent=re.sub(r"^vs\s+", "", bd._sig_text(field(inner, "sig2-opp"))),
        stip=bd._sig_text(field(inner, "sig2-stip")),
    )

def subject(h, slug):
    m = re.search(r"<title>([^:<|]+)", h)
    return (m.group(1).strip() if m else slug.replace("-", " ").title())

def patch(slug):
    p = os.path.join(ROOT, "wrestlers", slug, "index.html")
    if not os.path.isfile(p): return None
    h = open(p, encoding="utf-8").read()
    i = h.find('id="signature"')
    if i == -1: return None
    j = h.index("</section>", i)
    head, sec, tail = h[:i], h[i:j], h[j:]
    name = subject(h, slug)
    seen = []

    def sub(m):
        c = parse(m.group(2))
        if not c["event"]:
            return m.group(0)
        out = bd.sig_card(name, c)
        # ADDITIVE ONLY. This edits HTML it does not own, and a checkout may hold
        # only a subset of /matches/. An existing href whose page is absent HERE
        # is kept verbatim (it just gets no baked panel) rather than being torn
        # out -- otherwise running this on a partial tree would delete good links.
        if "sig2-card--link" not in out:
            was = re.search(r'<a class="sig2-card sig2-card--link" href="([^"]+)"', m.group(0))
            if was:
                seen.append((c, was)); return m.group(0)
        seen.append((c, re.search(r'href="([^"]+)"', out)))
        return out

    sec2 = CARD.sub(sub, sec)
    h2 = head + sec2 + tail
    if "/js/sig-preview.js" not in h2:
        h2 = h2.replace("</body>", SCRIPT + "\n</body>", 1)
    if h2 != h:
        open(p, "w", encoding="utf-8").write(h2)
    return [(c, m.group(1) if m else None) for c, m in seen]

def main(argv):
    for slug in (argv or HAND):
        rows = patch(slug)
        if rows is None:
            print("  %-14s no #signature section" % slug); continue
        n = len([r for r in rows if r[1]])
        print("  %-14s %d/%d cards linked" % (slug, n, len(rows)))
        for c, u in rows:
            print("      %-28s vs %-18s %s" % (c["event"][:28], c["opponent"][:18], u or "-- no page --"))
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
