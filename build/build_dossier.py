#!/usr/bin/env python3
"""build_dossier.py - generate /wrestlers/<slug>/ pages on the v2 dossier template.

The dossier template (cm-punk, john-cena) was hand-authored HTML: ~230KB per page
carrying a 36KB page-local <style> block duplicated verbatim on every copy. This
generator emits the same markup from data, and links css/dossier.css instead of
inlining it, so N pages cost one cached stylesheet rather than N x 36KB.

Structure derived from a verbatim dissection of the three v2 pages. The rules that
are easy to get wrong, and are enforced here:

  1. Section numbers are a CONTINUOUS ORDINAL over emitted sections, not fixed slot
     numbers. aj-styles omits slot 10 and its reference/faq renumber to 10/11.
  2. Slot 5 is polymorphic: factions | before. Slot 10 is optional AND polymorphic:
     mma | feats | omitted, with different bodies.
  3. The subnav lists only 9 sections. signature, slot-10 and reference are ALWAYS
     omitted from it even when present on the page.
  4. data-cfull / data-clm on every filter button are computed from real rows, and
     the career-defining count must agree in three separate places.
  5. FAQ HTML and FAQPage JSON-LD must match 1:1 in count and order. JSON-LD answers
     use the full name (they are context-free); HTML answers may use pronouns.

Run:  WL_ROOT="$PWD" python3 build/build_dossier.py [slug ...]
Then: python3 build/apply_shell.py
"""

import datetime, html as _html, json, os, re, sys

ROOT = os.environ.get("WL_ROOT", os.getcwd())
BASE = "https://wrestlelore.com"
# Placeholder only. apply_shell.py hashes css/ + js/ and rewrites every ?v= across
# the site, so this value is always overwritten on the next shell pass. Do not treat
# it as the live asset version.
ASSET_V = "122a6b76"
TODAY = datetime.date.today()

def esc(s):
    return _html.escape(str(s), quote=True) if s is not None else ""

def nb(s):
    """Non-breaking spaces, as the template uses in .idn-name and the crumb."""
    return str(s).replace(" ", "&nbsp;")

def hero_name(name):
    """The hero h1, sized so it never clips.

    The hand-authored template joins the name with &nbsp; and relies on
    clamp(64px,10vw,154px). That works for "CM Punk" and breaks for almost
    everything longer: "ROMAN REIGNS" renders 797px wide in a 722px column at
    1440. Two fixes, both needed:

      1. A multi-word name keeps a real space so it can wrap to two lines.
      2. The max font-size is capped from the LONGEST WORD, because a single
         long word ("CHRISTOPHER", "HENDRICKSON") cannot wrap at all.

    Anton advances roughly 0.55em per uppercase glyph; 700px is the hero
    column at the 1440 breakpoint. Names short enough to fit keep the
    template's own 154px ceiling, so cm-punk-length names are unchanged.
    """
    words = str(name).split()
    longest = max(len(w) for w in words)
    cap = min(154, int(700 / (longest * 0.55)))
    txt = nb(name) if (len(words) == 1 or len(name) <= 9) else esc(name)
    style = "" if cap >= 154 else ' style="font-size:clamp(56px,10vw,%dpx)"' % cap
    return txt, style

# ---------------------------------------------------------------- constants
X_SVG = ("M18.9 2H22l-7.6 8.7L23.3 22h-6.9l-5.4-7-6.2 7H1.7l8.1-9.3L1 2h7.1l4.9 6.4L18.9 2Zm-2.4 18h1.9"
         "L7.6 3.9H5.6L16.5 20Z")
IG_SVG = ("M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.3 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3"
          ".1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.3 1.8-.4 2.2a3.8 3.8 0 0 1-.9 1.4 3.8 3.8 0 0 1-1.4.9c-.4.2"
          "-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.3-2.2-.4a3.8 3.8 0 0 1-1.4-.9 3.8 3.8"
          " 0 0 1-.9-1.4c-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.3-1.8.4-2.2.2-.6.5"
          "-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2Zm0 3.6A6.2 6.2 0 1 0 12 18.2"
          " 6.2 6.2 0 0 0 12 5.8Zm0 10.2A4 4 0 1 1 12 8a4 4 0 0 1 0 8Zm6.4-10.5a1.44 1.44 0 1 1-1.44-1.44"
          " 1.44 1.44 0 0 1 1.44 1.44Z")
CROWN = "M6 46 L2 14 L18 26 L32 6 L46 26 L62 14 L58 46 Z"
CHEV = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">'
        '<path d="m6 9 6 6 6-6"/></svg>')

# Two behaviour scripts the template carries inline. They live in the repo, not in
# /tmp, so this generator keeps working in a fresh checkout. tail-script.template.js
# is the 14.5KB record-ledger IIFE with its only two subject-specific values replaced
# by {PROMO_LABEL_JSON} and {TOTAL_MATCHES}; the footer-fact script is a constant.
_ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dossier_assets")

def _load(name):
    p = os.path.join(_ASSETS, name)
    if not os.path.exists(p):
        raise SystemExit("missing build asset: %s\n"
                         "Extract it from an existing dossier page's inline <script>." % p)
    return open(p, encoding="utf-8").read()

TAIL_TPL = _load("tail-script.template.js")
FACT_JS  = _load("footer-fact-script.constant.js")
for _ph in ("{PROMO_LABEL_JSON}", "{TOTAL_MATCHES}"):
    assert _ph in TAIL_TPL, "tail-script.template.js is missing placeholder %s" % _ph

# Section id -> (h2 text, subnav label or None when never listed)
SEC_META = {
    "overview":  ("Overview",              "Overview"),
    "record":    ("The Record",            "Record"),
    "signature": ("Signature Matches",     None),
    "titles":    ("Championships",         "Titles"),
    "factions":  ("Factions",              "Factions"),
    "before":    ("Before WWE",            "Before WWE"),
    "personas":  ("Personas",              "Personas"),
    "career":    ("Career Timeline",       "Career"),
    "rivalries": ("Rivalries",             "Rivalries"),
    "media":     ("Media &amp; Gaming",    "Media"),
    "mma":       ("MMA Record &mdash; UFC", None),
    "feats":     ("Records &amp; Feats",   None),
    "reference": ("Official &amp; Reference", None),
    "faq":       ("Frequently Asked",      "FAQ"),
}

def sections_for(a):
    """Ordered list of section ids this subject actually emits."""
    s = ["overview", "record"]
    # A subject with no rated matches gets no Signature section rather than an
    # empty grid. Randy Orton has no star rating in any source consulted.
    if a.get("signature"):
        s.append("signature")
    s.append("titles")
    s.append(a["slot5"]["id"])
    s += ["personas", "career", "rivalries", "media"]
    if a.get("slot10"):
        s.append(a["slot10"]["id"])
    s += ["reference", "faq"]
    return s

# ------------------------------------------------------------------ pieces
def sec_h(n, sid):
    return ('<section class="sec reveal" id="%s"><div class="sec-h"><span class="n">%02d</span>'
            '<h2>%s</h2></div>' % (sid, n, SEC_META[sid][0]))

def lead(t):
    return '<p class="sec-lead">%s</p>' % t if t else ""

def tiles(rows):
    return '<div class="rec2-stats">%s</div>' % "".join(
        '<div class="rec2-stat"><b>%s</b><span>%s</span></div>' % (v, esc(l)) for v, l in rows)

def subnav(a, secs):
    items = []
    for sid in secs:
        label = SEC_META[sid][1]
        if label:
            items.append('<li><a href="#%s">%s</a></li>' % (sid, label))
    return ('<nav class="subnav" aria-label="Profile sections"><ul>%s</ul>\n'
            '  <span class="subnav-ind" aria-hidden="true"></span>\n</nav>' % "".join(items))

def idn(a):
    soc = ""
    if a.get("x_url"):
        soc += ('<a href="%s" target="_blank" rel="noopener" aria-label="X">'
                '<svg viewBox="0 0 24 24" style="fill:currentColor"><path d="%s"/></svg></a>'
                % (esc(a["x_url"]), X_SVG))
    if a.get("ig_url"):
        soc += ('<a href="%s" target="_blank" rel="noopener" aria-label="Instagram">'
                '<svg viewBox="0 0 24 24" style="fill:currentColor"><path d="%s"/></svg></a>'
                % (esc(a["ig_url"]), IG_SVG))
    sp = "".join(
        '<a class="sp-item%s" href="%s" target="_blank" rel="noopener"><span class="sp-ic">%s</span>'
        '<span class="sp-txt"><b>%s</b><span>%s</span></span><span class="sp-tag">%s</span></a>'
        % (" sp-charity" if it.get("charity") else "", esc(it["href"]), esc(it["ic"]),
           esc(it["title"]), esc(it["sub"]), esc(it["tag"]))
        for it in a["sp_items"])
    vit = ["%s&nbsp;%s" % (a.get("debut_label", "EST."), a["debut_year"])]
    if a.get("height_imp"): vit.append(a["height_imp"])
    if a.get("weight_lb"):  vit.append("%s&nbsp;LB" % a["weight_lb"])
    if a.get("world_titles"): vit.append("%s&times;&nbsp;WORLD" % a["world_titles"])
    vit.append("<b>&#10216;&nbsp;%s&nbsp;&#10217;</b>" % nb(a["vitals_tagline"].upper()))
    return ('<div class="idn" id="idn"><div class="idn-in">\n'
      '  <nav class="idn-crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">&rsaquo;</span>'
      '<a href="/wrestlers/">Superstars</a><span class="sep">&rsaquo;</span><span class="cur">%s</span></nav>\n'
      '  <div class="idn-plate"><span class="idn-eye">%s</span><b class="idn-name">%s</b>'
      '<span class="idn-dia">&#9670;</span>\n'
      '   <span class="idn-vitals">%s</span>\n   <span class="idn-sep"></span>\n'
      '   <div class="idn-soc">%s</div>\n'
      '   <div class="idn-supwrap"><button class="idn-support js-idn" aria-expanded="false">Support '
      '<span class="chev">&#8964;</span></button>\n'
      '    <div class="idn-panel" id="idnPanel"><div class="sp-head"><span class="sp-k">Follow %s</span>'
      '<span class="sp-note">%s</span></div>\n%s\n    </div></div>\n'
      '  </div><div class="idn-rightspace" aria-hidden="true"></div>\n</div></div>'
      % (nb(esc(a["name"])), esc(a["epithet"]), nb(esc(a["name"]).upper()),
         " <i>&middot;</i> ".join(vit), soc, esc(a["name"]), a.get("support_note", "Merch &middot; Games &middot; Watch"), sp))

def hero(a):
    _h1t, _h1s = hero_name(a["name"])
    hs = "".join(
        '<div class="hstat"><b><span class="num" data-count="%s">%s</span>%s</b><span>%s</span></div>'
        % (h["value"], h["value"], '<span class="x">&times;</span>' if h.get("x") else "", esc(h["label"]))
        for h in a["hstats"])
    return ('<header class="hero" id="top"><div class="wrap">\n    <div>\n'
      '      <div class="hero-kick">%s</div>\n'
      '      <h1%s><span class="the">%s</span>%s</h1>\n'
      '      <p class="hero-tag">%s</p>\n'
      '      <div class="hero-now"><span>%s</span><b>%s</b>%s</div>\n'
      '      <div class="hero-stats">%s</div>\n'
      '      <div class="hero-cta-row">\n'
      '        <button class="discover" type="button" data-scroll="#record">Explore the full record%s</button>\n'
      '        <a class="ghost-link" href="#career">%s</a>\n      </div>\n    </div>\n'
      '    <figure class="portrait" aria-label="%s key art">\n      <span class="slot">PHOTO SLOT</span>\n'
      '      <span class="vlabel">%s</span>\n'
      '      <svg class="crown" viewBox="0 0 64 54" aria-hidden="true"><path d="%s"/></svg>\n'
      '      <span class="mono" aria-hidden="true">%s</span>\n'
      '      <figcaption class="cap"><span class="r">Roster File &middot; %s</span><span class="n">%s</span>'
      '</figcaption>\n    </figure>\n  </div></header>'
      % (a["hero_kick"], _h1s, esc(a["epithet"]), _h1t, a["hero_tag"],
         a.get("now_label", "NOW"), esc(a["now_bold"]), a["now_tail"], hs, CHEV,
         esc(a["ghost_link"]), esc(a["name"]), a["vlabel"], CROWN, esc(a["mono"]),
         esc(a["epithet"]), esc(a["realname"])))

WL_DONUT = ('<div class="rec2-wl rec2-wl-veiled" id="rec2-wl"><svg class="rec2-donut" viewBox="0 0 120 120" '
  'role="img" aria-hidden="true" aria-label="Win and loss share for the card shown">'
  '<circle class="dn-bg" cx="60" cy="60" r="44"></circle><circle class="dn-seg" id="dn-w" cx="60" cy="60" r="44"></circle>'
  '<circle class="dn-seg" id="dn-l" cx="60" cy="60" r="44"></circle><circle class="dn-seg" id="dn-d" cx="60" cy="60" r="44"></circle>'
  '<circle class="dn-seg" id="dn-n" cx="60" cy="60" r="44"></circle>'
  '<text class="dn-pct" id="dn-pct" x="60" y="58" text-anchor="middle">0%</text>'
  '<text class="dn-cap" x="60" y="74" text-anchor="middle">WIN RATE</text></svg>\n'
  '<div class="rec2-wl-side" aria-hidden="true"><p class="rec2-wl-rec"><b id="wl-rec">0-0</b></p>'
  '<ul class="rec2-wl-legend"><li><i class="lg lg-w"></i>Wins <b id="wl-w">0</b></li>'
  '<li><i class="lg lg-l"></i>Losses <b id="wl-l">0</b></li>'
  '<li><i class="lg lg-d"></i>Draws <b id="wl-d">0</b></li>'
  '<li><i class="lg lg-n"></i>No contests <b id="wl-n">0</b></li></ul></div>\n'
  '<div class="rec2-wl-veil"><p>The book is kayfabe protected</p>'
  '<button class="rec2-wl-unveil" type="button">Turn spoilers on</button></div></div>')

REC_THEAD = ('<div class="rec2-scroll"><table class="rec2-table"><thead><tr>'
  '<th class="rec2-sort" data-skey="res" aria-sort="none" title="Sort wins first">Res</th>'
  '<th class="rec2-sort" data-skey="date" aria-sort="none" title="Sort by date">Date</th>'
  '<th class="rec2-sort" data-skey="promo" aria-sort="none" title="Sort by promotion">Promo</th>'
  '<th class="rec2-sort" data-skey="event" aria-sort="none" title="Sort by event">Event</th>'
  '<th class="rec2-sort" data-skey="opp" aria-sort="none" title="Sort by opponent">Opponent(s)</th>'
  '<th class="rec2-sort" data-skey="stip" aria-sort="none" title="Sort by stipulation">Stipulation</th>'
  '<th class="rec2-sort" data-skey="title" aria-sort="none" title="Sort by title">Title</th>'
  '</tr></thead><tbody id="rec2-body">')

RW = {"W": "rw-w", "L": "rw-l", "D": "rw-d", "NC": "rw-n"}

def match_row(r):
    attrs = ['class="rec2-row"', 'data-result="%s"' % r["result"]]
    if r.get("landmark"): attrs.append('data-landmark="1"')
    attrs.append('data-promo="%s"' % r["promo"])
    if r.get("type"):     attrs.append('data-type="%s"' % r["type"])
    attrs.append('data-sort="%s"' % r["date"].replace("-", ""))
    opp = r["opponent"] if r.get("opponent_html") else esc(r["opponent"])
    return ('<tr %s><td><span class="rw %s">%s</span></td><td class="dim rec2-date">%s</td>'
            '<td><span class="pchip pchip-%s">%s</span></td><td class="rec2-ev">%s</td>'
            '<td class="rec2-opp">%s</td><td class="dim rec2-stip">%s</td>'
            '<td class="dim rec2-title">%s</td></tr>'
            % (" ".join(attrs), RW[r["result"]], r["result"], r["date"],
               r["promo"].lower(), r["promo"], esc(r["event"]), opp,
               esc(r.get("stip", "Singles")), esc(r["title"]) if r.get("title") else "&mdash;"))

def sec_record(n, a):
    rec = a["record"]; rows = rec["rows"]
    total = rec.get("total") or len(rows)
    cd = len([r for r in rows if r.get("landmark")])
    keys = []
    for r in rows:
        if r["promo"] not in keys: keys.append(r["promo"])
    order = rec.get("promo_order") or keys
    fbtns = ['<button class="rec2-fbtn on" data-f="all" data-cfull="%d" data-clm="%d">All <span>%d</span></button>'
             % (total, cd, cd)]
    for k in order:
        kr = [r for r in rows if r["promo"] == k]
        klm = len([r for r in kr if r.get("landmark")])
        fbtns.append('<button class="rec2-fbtn" data-f="%s" data-cfull="%d" data-clm="%d">%s <span>%d</span></button>'
                     % (k.lower(), len(kr), klm, rec.get("promo_labels", {}).get(k, k), klm))
    tagr = [r for r in rows if r.get("type") == "tag"]
    taglm = len([r for r in tagr if r.get("landmark")])
    tbtns = ('<button class="rec2-fbtn on" data-ft="all" title="Show all match types">All types</button>'
             '<button class="rec2-fbtn" data-ft="tag" data-cfull="%d" data-clm="%d">Tag / multi <span>%d</span></button>'
             % (len(tagr), taglm, taglm))
    full_label = rec.get("full_label", "Full record")
    return (sec_h(n, "record") + tiles(rec["stats"]) + lead(rec["lead"]) +
      '<div class="rec2-ctrl">\n<div class="rec2-scope" role="radiogroup" aria-label="Record scope" id="rec2-scope">'
      '<button class="rec2-scopebtn on" role="radio" aria-checked="true" data-scope="cf">Career-defining <span>%d</span></button>'
      '<button class="rec2-scopebtn" role="radio" aria-checked="false" data-scope="all">%s <span>%d</span></button></div>'
      '<button class="spl" id="splTgl" type="button" aria-pressed="false" title="Show every win and loss">'
      '<span class="spl-lbl">Spoilers off</span><span class="spl-track"><span class="spl-knob"></span></span></button>\n</div>'
      '<div class="rec2-filters" role="tablist" id="rec2-promo-filters">%s</div>'
      '<div class="rec2-filters" role="group" id="rec2-type-filters" style="margin-top:-4px">%s</div>'
      '%s%s%s'
      '<tr id="rec2-empty" class="rec2-empty" hidden><td colspan="7">No career-defining bouts match this filter. '
      '<a data-see-all role="button" tabindex="0">See them in the full record</a></td></tr>'
      '</tbody></table></div>\n'
      '<p class="rec2-count" id="rec2-count" aria-live="polite" aria-atomic="true">'
      '<b id="rec2-shown">%d</b> of %d matches shown</p></section>'
      % (cd, full_label, total, "".join(fbtns), tbtns, WL_DONUT, REC_THEAD,
         "".join(match_row(r) for r in rows), cd, total))

def sec_signature(n, a):
    cards = a["signature"]
    reel = len(cards) >= 8
    out = []
    for c in cards:
        stars = "★" * int(float(c["rating"]))
        inner = ('<div class="sig2-top"><span class="sig2-rate">%s</span><span class="sig2-stars">%s</span></div>'
                 '<h3 class="sig2-ev">%s</h3><p class="sig2-opp">vs %s</p><p class="sig2-stip">%s</p>'
                 % (c["rating"], stars, esc(c["event"]), esc(c["opponent"]), esc(c["stip"])))
        if c.get("url"):
            out.append('<a class="sig2-card sig2-card--link" href="%s">%s</a>' % (esc(c["url"]), inner))
        else:
            out.append('<div class="sig2-card">%s</div>' % inner)
    ld = a.get("signature_lead") or ("The nights that made %s, by acclaim (Meltzer / Cagematch, as reported)."
                                     % a["epithet"])
    if reel: ld += " Scroll for all %s." % a.get("signature_count_word", "eight")
    return (sec_h(n, "signature") + lead(ld) +
            '<div class="sig2-grid%s">%s</div></section>' % (" sig2-reel" if reel else "", "".join(out)))

def sec_titles(n, a):
    t = a["titles"]
    rows = "".join(
        '<div class="ch-row"><span class="ch-ic">%s</span><div class="ch-body"><h3 class="ch-name">%s</h3>'
        '<p class="ch-sub">%s</p></div><div class="ch-cnt"><b>%s</b><span>REIGNS</span></div></div>'
        % (r["ic"], esc(r["name"]), r["sub"], r["count"]) for r in t["rows"])
    return sec_h(n, "titles") + tiles(t["stats"]) + lead(t["lead"]) + '<div class="ch-list">%s</div></section>' % rows

def sec_slot5(n, a):
    s = a["slot5"]
    cards = "".join(
        '<article class="fac-card"><span class="fac-era">%s</span><h3 class="fac-name">%s</h3>'
        '<p class="fac-mem">%s</p><p class="fac-desc">%s</p></article>'
        % (c["era"], esc(c["name"]), esc(c["members"]), esc(c["desc"])) for c in s["cards"])
    return sec_h(n, s["id"]) + lead(s["lead"]) + '<div class="fac-grid">%s</div></section>' % cards

def sec_personas(n, a):
    p = a["personas"]
    cards = "".join(
        '<article class="per-card"><span class="per-mono">%s</span><span class="per-era">%s</span>'
        '<h3 class="per-name">%s</h3><p class="per-desc">%s</p></article>'
        % (esc(c["mono"]), c["era"], esc(c["name"]), esc(c["desc"])) for c in p["cards"])
    return sec_h(n, "personas") + lead(p["lead"]) + '<div class="per-row">%s</div></section>' % cards

def sec_career(n, a):
    c = a["career"]
    rows = "".join(
        '<div class="arch-row"><span class="arch-yr">%s</span><div class="arch-body">'
        '<h3 class="arch-title">%s</h3><p class="arch-desc">%s</p></div></div>'
        % (r["year"], esc(r["title"]), esc(r["desc"])) for r in c["rows"])
    return sec_h(n, "career") + lead(c["lead"]) + '<div class="arch-line">%s</div></section>' % rows

def sec_rivalries(n, a):
    r = a["rivalries"]
    cards = "".join(
        '<article class="fac-card"><h3 class="fac-name">%s</h3><p class="fac-desc">%s</p></article>'
        % (('<a href="/wrestlers/%s/">%s</a>' % (c["slug"], esc(c["name"]))) if c.get("slug") else esc(c["name"]),
           esc(c["desc"])) for c in r["cards"])
    return sec_h(n, "rivalries") + lead(r["lead"]) + '<div class="fac-grid">%s</div></section>' % cards

def sec_media(n, a):
    m = a["media"]
    rows = "".join(
        '<article class="pod-row"><span class="pod-when">%s</span><div class="pod-body">'
        '<h3 class="pod-title">%s</h3><p class="pod-desc">%s</p></div><span class="pod-kind">%s</span></article>'
        % (r["when"], esc(r["title"]), esc(r["desc"]), esc(r["kind"])) for r in m["rows"])
    h = sec_h(n, "media")
    if m.get("h2"): h = h.replace("<h2>%s</h2>" % SEC_META["media"][0], "<h2>%s</h2>" % m["h2"])
    return h + lead(m["lead"]) + '<div class="pod-list">%s</div></section>' % rows

def sec_slot10(n, a):
    s = a["slot10"]
    if s["id"] == "feats":
        rows = "".join(
            '<div class="ch-row"><span class="ch-ic">&#9733;</span><div class="ch-body">'
            '<h3 class="ch-name">%s</h3><p class="ch-sub">%s</p></div></div>'
            % (esc(r["name"]), esc(r["sub"])) for r in s["rows"])
        out = sec_h(n, "feats") + lead(s["lead"]) + tiles(s["stats"]) + '<div class="ch-list">%s</div>' % rows
        if s.get("footnote"):
            out += ('<p class="sec-lead" style="margin-top:14px;font-size:13px;opacity:.7">%s</p>' % esc(s["footnote"]))
        return out + "</section>"
    rows = "".join(
        '<tr class="rec2-row"><td><span class="rw %s">%s</span></td><td class="dim rec2-date">%s</td>'
        '<td class="rec2-ev">%s</td><td class="rec2-opp">%s</td><td class="dim rec2-stip">%s</td>'
        '<td class="dim rec2-title">%s</td></tr>'
        % (RW[r["result"]], r["result"], r["date"], esc(r["event"]), esc(r["opponent"]),
           esc(r["method"]), esc(r.get("notes", ""))) for r in s["rows"])
    gym = "".join(
        '<article class="fac-card"><span class="fac-era">%s</span><h3 class="fac-name">%s</h3>'
        '<p class="fac-mem">%s</p><p class="fac-desc">%s</p></article>'
        % (c["era"], esc(c["name"]), esc(c["members"]), esc(c["desc"])) for c in s.get("cards", []))
    return (sec_h(n, "mma") + lead(s["lead"]) + tiles(s["stats"]) +
            ('<div class="fac-grid">%s</div>' % gym if gym else "") +
            '<div class="rec2-scroll"><table class="rec2-table"><thead><tr><th>Res</th><th>Date</th>'
            '<th>Event</th><th>Opponent</th><th>Method</th><th>Notes</th></tr></thead><tbody>%s'
            '</tbody></table></div></section>' % rows)

def sec_reference(n, a):
    items = "".join(
        '<a class="ref2-item" href="%s" target="_blank" rel="noopener">'
        '<span class="ref2-k">%s</span><span class="ref2-v">%s</span></a>'
        % (esc(r["href"]), esc(r["k"]), esc(r["v"])) for r in a["reference"])
    return sec_h(n, "reference") + lead("Follow, connect and verify.") + '<div class="ref2-grid">%s</div></section>' % items

def sec_faq(n, a):
    items = "".join(
        '<details class="faq2-item"><summary class="faq2-q">%s<span class="faq2-ic"></span></summary>'
        '<p class="faq2-a">%s</p></details>' % (f["q"], f["a"]) for f in a["faq"])
    return sec_h(n, "faq") + '<div class="faq2-list">%s</div></section>' % items

def sec_overview(n, a):
    ps = []
    for i, p in enumerate(a["overview"]):
        mt = "" if i == 0 else ";margin-top:14px"
        ps.append('<p style="font-family:\'Inter\',sans-serif;color:rgba(244,245,247,.82);font-size:16px;'
                  'line-height:1.7;max-width:72ch%s">%s</p>' % (mt, p))
    return sec_h(n, "overview") + "".join(ps) + "</section>"

BUILDERS = {"overview": sec_overview, "record": sec_record, "signature": sec_signature,
            "titles": sec_titles, "factions": sec_slot5, "before": sec_slot5,
            "personas": sec_personas, "career": sec_career, "rivalries": sec_rivalries,
            "media": sec_media, "mma": sec_slot10, "feats": sec_slot10,
            "reference": sec_reference, "faq": sec_faq}

# Tale of the Tape. A row whose fact carries a `sub` provenance note becomes a
# native <details> whose <summary> IS the fact line, so the note can fold away
# at zero vertical cost and the sticky rail's bottom stays reachable
# (css/dossier.css "TALE OF THE TAPE", js/rail.js). A row with no `sub` has
# nothing to disclose and keeps the plain form. The whitespace-normalised
# rendered text of the card is unchanged by the transform: the value and the
# note were already on separate lines, because `.tott dd .cm` is display:block.
ROW_SRC = ('<div class="row row--src"><dt>%s</dt><dd>'
           '<details class="tsrc"><summary class="tsrc-v">'
           '<span class="tsrc-p">%s</span><span class="tsrc-ic" aria-hidden="true"></span>'
           '</summary><span class="cm tsrc-n">%s</span></details></dd></div>')
ROW_PLAIN = '<div class="row"><dt>%s</dt><dd>%s</dd></div>'

def rail(a):
    tape = a["tape"]
    rows = "".join(
        (ROW_SRC % (esc(r["label"]), r["value"], r["sub"])) if r.get("sub")
        else (ROW_PLAIN % (esc(r["label"]), r["value"]))
        for r in tape)
    sourced, total = sum(1 for r in tape if r.get("sub")), len(tape)
    # The credibility line the site is positioned on. It used to sit in the card
    # footer and cost 34px; on the title's baseline it costs nothing and it
    # survives folding, which is the state it matters most in.
    cred = ('<p class="tt-cred" title="%d of %d entries carry a source note">'
            '<span class="tt-n">%d/%d</span><span class="tt-lbl">sourced</span></p>'
            % (sourced, total, sourced, total)) if total else ""
    return ('<aside class="rail" aria-label="Quick facts">'
            '<section class="card tott" data-tape aria-labelledby="tott-h">'
            '<div class="tt-head"><h2 id="tott-h" class="kick">Tale of the Tape</h2>%s</div>'
            '<dl id="tott-dl">%s</dl></section></aside>' % (cred, rows))

# ------------------------------------------------------------------ JSON-LD
def jsonld(a, secs):
    u = "%s/wrestlers/%s/" % (BASE, a["slug"])
    person = {"@type": "Person", "@id": u + "#person", "name": a["name"],
              "alternateName": a["ld"]["alternateName"], "jobTitle": "Professional wrestler",
              "hasOccupation": {"@type": "Occupation", "name": "Professional wrestler"},
              "birthDate": a["born_iso"],
              "birthPlace": {"@type": "Place", "name": a["bornplace"]},
              "nationality": {"@type": "Country", "name": a["nationality"]}}
    if a.get("alumni"):
        person["alumniOf"] = {"@type": "CollegeOrUniversity", "name": a["alumni"]}
    if a.get("height_cm"):
        person["height"] = {"@type": "QuantitativeValue", "value": a["height_cm"], "unitCode": "CMT"}
    if a.get("weight_kg"):
        person["weight"] = {"@type": "QuantitativeValue", "value": a["weight_kg"], "unitCode": "KGM"}
    person.update({"award": a["ld"]["award"], "knowsAbout": a["ld"]["knowsAbout"],
                   "description": a["ld"]["description"], "sameAs": a["ld"]["sameAs"], "url": u})
    graph = [person,
      {"@type": "WebPage", "@id": u + "#webpage", "url": u,
       "name": "%s: %s" % (a["name"], a["epithet"]),
       "about": {"@id": u + "#person"},
       "isPartOf": {"@type": "WebSite", "name": "Wrestle Lore", "url": BASE + "/"},
       "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["#overview", ".faq2-a"]},
       "primaryImageOfPage": BASE + "/assets/wrestle-lore-logo.png"},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Superstars", "item": BASE + "/wrestlers/"},
        {"@type": "ListItem", "position": 3, "name": a["name"], "item": u}]},
      {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": f["q_ld"],
         "acceptedAnswer": {"@type": "Answer", "text": f["a_ld"]}} for f in a["faq"]]}]
    # json.dumps guarantees valid JSON. The hand-authored pages used single-quoted
    # strings inside FAQPage, which made the whole block unparseable on 60 pages.
    return ('<script type="application/ld+json">%s</script>'
            % json.dumps({"@context": "https://schema.org", "@graph": graph},
                         ensure_ascii=False, separators=(",", ":")))

# ------------------------------------------------------------------ page
def page(a):
    secs = sections_for(a)
    u = "%s/wrestlers/%s/" % (BASE, a["slug"])
    body_secs = []
    for i, sid in enumerate(secs, 1):
        body_secs.append(BUILDERS[sid](i, a))
    covered = [SEC_META[s][0].replace("&amp;", "and") for s in secs
               if s in ("titles", "factions", "before", "mma", "feats", "career", "rivalries")]
    title = "%s: %s, %s | Wrestle Lore" % (a["name"], a["epithet"], a["hook"])
    rec = a["record"]
    promo_label = {k.lower(): rec.get("promo_labels", {}).get(k, k)
                   for k in (rec.get("promo_order") or sorted({r["promo"] for r in rec["rows"]}))}
    tail = (TAIL_TPL.replace("{PROMO_LABEL_JSON}", json.dumps(promo_label, separators=(",", ":")))
                    .replace("{TOTAL_MATCHES}", str(rec.get("total") or len(rec["rows"]))))
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
      '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
      '<title>%s</title>\n<meta name="description" content="%s">\n'
      '<link rel="canonical" href="%s">\n'
      '<meta property="og:type" content="profile">\n<meta property="og:site_name" content="Wrestle Lore">\n'
      '<meta property="og:title" content="%s: %s">\n<meta property="og:description" content="%s">\n'
      '<meta property="og:url" content="%s">\n'
      '<meta name="twitter:card" content="summary_large_image">'
      '<meta property="og:image" content="%s/assets/wrestle-lore-logo.png">'
      '<meta property="og:image:alt" content="%s on Wrestle Lore">'
      '<meta name="twitter:image" content="%s/assets/wrestle-lore-logo.png">'
      '<meta name="twitter:title" content="%s: %s">'
      '<meta name="twitter:description" content="%s">\n'
      '<link rel="preload" href="/fonts/anton-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>\n'
      '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
      '<link rel="icon" href="/favicon.ico" sizes="any">\n'
      '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n'
      '<link rel="manifest" href="/site.webmanifest">\n'
      '<meta name="theme-color" content="#0b0c10">\n'
      '<link rel="stylesheet" href="/css/site.css?v=%s">\n%s\n'
      '<link rel="stylesheet" href="/css/profile.css?v=%s">\n'
      '<link rel="stylesheet" href="/css/dossier.css?v=%s">\n'
      '</head>\n<body>\n<header class="site-header nav7"></header>\n'
      '<div class="wl-dossier bar-glass" id="main">\n'
      '<!-- ===== STICKY SUB-NAV ===== -->\n%s\n'
      '<!-- ===== STICKY IDENTITY / SOCIAL BAR ===== -->\n%s\n%s\n'
      '<div class="layout"><main class="profile-main">\n    %s\n  </main>%s</div>\n'
      '<footer class="site-footer site-footer--fat" data-wl-shell></footer>\n'
      '<script>%s</script>\n'
      '<script src="/js/main.js?v=%s"></script>\n'
      '<script src="/js/search-index.js?v=%s" defer></script>\n'
      '<script src="/js/nav.js?v=%s" defer></script>\n'
      '<script src="/js/engage.js?v=%s" defer></script>\n'
      '<script src="/js/profile.js?v=%s" defer></script>\n'
      '<script src="/js/rail.js?v=%s"></script>\n'
      '<script>%s</script>\n</body>\n</html>\n'
      % (esc(title), esc(a["meta_desc"]), u, esc(a["name"]), esc(a["epithet"]), esc(a["og_desc"]), u,
         BASE, esc(a["name"]), BASE, esc(a["name"]), esc(a["epithet"]), esc(a["tw_desc"]),
         ASSET_V, jsonld(a, secs), ASSET_V, ASSET_V,
         subnav(a, secs), idn(a), hero(a), "\n    ".join(body_secs), rail(a),
         FACT_JS, ASSET_V, ASSET_V, ASSET_V, ASSET_V, ASSET_V, ASSET_V, tail))

# ------------------------------------------------------------------ driver
def load_all():
    import importlib.util
    out = {}
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wldata")
    for f in sorted(os.listdir(d)):
        if not f.endswith(".py") or f.startswith("_"): continue
        spec = importlib.util.spec_from_file_location(f[:-3], os.path.join(d, f))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        out[m.DATA["slug"]] = m.DATA
    return out

def verify(a, htmlstr):
    """Fail loudly rather than shipping a page with contradictory counts."""
    errs = []
    rec = a["record"]; rows = rec["rows"]
    total = rec.get("total") or len(rows)
    cd = len([r for r in rows if r.get("landmark")])
    if cd == 0: errs.append("no rows flagged landmark -> career-defining scope would be empty")
    if total < len(rows): errs.append("record.total %d < %d actual rows" % (total, len(rows)))
    for f in a["faq"]:
        for k in ("q", "a", "q_ld", "a_ld"):
            if not f.get(k): errs.append("faq entry missing %s" % k)
    if len(a["hstats"]) != 4: errs.append("hstats must be exactly 4, got %d" % len(a["hstats"]))
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', htmlstr, re.S):
        try: json.loads(m)
        except Exception as e: errs.append("invalid JSON-LD: %s" % e)
    shown = re.search(r'<b id="rec2-shown">(\d+)</b> of (\d+)', htmlstr)
    if shown and (int(shown.group(1)) != cd or int(shown.group(2)) != total):
        errs.append("rec2-count disagrees with row data")
    return errs

def main(argv):
    data = load_all()
    want = argv or sorted(data)
    n = 0
    for slug in want:
        if slug not in data:
            print("  no data module for %s" % slug); continue
        a = data[slug]
        h = page(a)
        errs = verify(a, h)
        if errs:
            print("  %-20s FAILED: %s" % (slug, "; ".join(errs))); continue
        p = os.path.join(ROOT, "wrestlers", slug, "index.html")
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, "w", encoding="utf-8").write(h)
        secs = sections_for(a)
        print("  %-20s %6.0f KB  %2d sections  %3d matches" %
              (slug, len(h) / 1024, len(secs), len(a["record"]["rows"])))
        n += 1
    print("done: %d dossier pages  ROOT=%s" % (n, ROOT))
    print("now run: python3 build/apply_shell.py")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
