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
    "pulse":     ("Right Now",             None),
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
    if a.get("pulse"):
        s.append("pulse")
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

# --------------------------------------------------- hero fight-metrics tabs
def _clip_words(s, n=120):
    """Truncate an HTML-entity string to ~n visible chars at a word boundary.
    Splitting on spaces can never bisect an entity (entities contain no
    spaces); visible length is measured on the unescaped text."""
    import html as _h
    if len(_h.unescape(s)) <= n:
        return s
    out, used = [], 0
    for w in s.split(" "):
        wlen = len(_h.unescape(w)) + (1 if out else 0)
        if used + wlen > n:
            break
        out.append(w); used += wlen
    return " ".join(out).rstrip(".,;:") + "&hellip;"

def _fm_world_titles(a):
    """World-title count: the hstat that mentions world titles, else the
    identity bar's world_titles, else counted from the JSON-LD award list."""
    for h in a["hstats"]:
        if "world" in h["label"].lower():
            return str(h["value"])
    if a.get("world_titles"):
        return str(a["world_titles"])
    return str(len([w for w in a["ld"]["award"] if "world champion" in w.lower()]))

def fm_metrics(a):
    """METRICS panel body: cm-punk's hand-built .fm-* vocabulary, generated
    from the same data the record section is built from."""
    rec = a["record"]; rows = rec["rows"]
    total = rec.get("total") or len(rows)
    cd = len([r for r in rows if r.get("landmark")])
    wt = _fm_world_titles(a)
    # fourth digit: the biggest remaining hero stat (punk's slot holds "434
    # day title reign" - the headline number that is neither a bout count nor
    # the world-title tally)
    def _num(v):
        m = re.search(r"\d+", str(v))
        return int(m.group(0)) if m else -1
    extra = max((h for h in a["hstats"] if "world" not in h["label"].lower()),
                key=lambda h: _num(h["value"]))
    digits = (
        '<div class="fm-digits" role="list" aria-label="Career numbers">'
        '<div class="fm-d" role="listitem"><b>%d</b><span>Documented bouts</span></div>'
        '<div class="fm-d" role="listitem"><b>%d</b><span>Career-defining</span></div>'
        '<div class="fm-d" role="listitem"><b>%s</b><span>World titles</span></div>'
        '<div class="fm-d" role="listitem"><b>%s</b><span>%s</span></div></div>'
        % (total, cd, wt, extra["value"], esc(extra["label"])))
    ring = ('<div class="fm-wl rec2-wl-veiled" id="fm-wl">'
        '<svg class="rec2-donut" viewBox="0 0 120 120" role="img" aria-hidden="true" '
        'aria-label="Career win rate across the full book">'
        '<circle class="dn-bg" cx="60" cy="60" r="44"></circle>'
        '<circle class="dn-seg" id="fm-w" cx="60" cy="60" r="44"></circle>'
        '<circle class="dn-seg" id="fm-l" cx="60" cy="60" r="44"></circle>'
        '<circle class="dn-seg" id="fm-d" cx="60" cy="60" r="44"></circle>'
        '<circle class="dn-seg" id="fm-n" cx="60" cy="60" r="44"></circle>'
        '<text class="dn-pct" id="fm-pct" x="60" y="58" text-anchor="middle">0%</text>'
        '<text class="dn-cap" x="60" y="74" text-anchor="middle">WIN RATE</text></svg>\n'
        '<p class="rec2-wl-side fm-wl-rec" aria-hidden="true"><b id="fm-rec">0-0</b>'
        '<span>W&ndash;L &middot; full book</span></p>\n'
        '<div class="rec2-wl-veil"><p>Kayfabe protected</p>'
        '<button class="rec2-wl-unveil" type="button" '
        'aria-label="Turn spoilers on to reveal the win rate">Spoilers</button></div></div>')
    # ledger: current billing, world titles, bout count, billed-from
    chip = ""
    now_txt = "%s %s" % (a.get("now_label", ""), a.get("now_bold", ""))
    if "champion" in now_txt.lower():
        chip = '<span class="fm-chip">Champion</span>'
    billed = ""
    for t in a["tape"]:
        if t["label"].lower().startswith("billed"):
            billed = t["value"]; break
    if billed and a.get("weight_lb"):
        billed += " &middot; %s lb" % a["weight_lb"]
    ledger = ('<div class="fm-ledger"><div class="fm-lg-h"><span>Record</span>%s</div>'
        '<dl class="fm-lg">'
        '<div><dt>Now</dt><dd>%s</dd></div>'
        '<div><dt>World titles</dt><dd>%s</dd></div>'
        '<div><dt>In the books</dt><dd>%d bouts</dd></div>'
        '%s</dl></div>'
        % (chip, esc(a["now_bold"]), wt, total,
           ('<div><dt>Billed</dt><dd>%s</dd></div>' % billed) if billed else ""))
    # bouts-by-promotion bars from real row counts
    order = rec.get("promo_order") or []
    for r in rows:
        if r["promo"] not in order: order.append(r["promo"])
    counts = [(k, len([r for r in rows if r["promo"] == k])) for k in order]
    counts = [(k, n) for k, n in counts if n]
    mx = max(n for _, n in counts)
    bars = "".join(
        '<div class="fm-bar" data-fm-promo="%s"><span class="l">%s</span>'
        '<span class="t"><i style="width:%s%%"></i></span><b class="n">%d</b>'
        '<span class="p">%d%%</span></div>'
        % (esc(k), esc(rec.get("promo_labels", {}).get(k, k)),
           ("%.1f" % (100.0 * n / mx)).rstrip("0").rstrip("."), n,
           round(100.0 * n / total))
        for k, n in counts)
    return ('<div class="fm">%s<div class="fm-mid">%s%s</div>'
        '<div class="fm-bars" aria-label="Bouts by promotion">'
        '<div class="fm-bars-h">Bouts by promotion</div>%s</div></div>\n'
        '<p class="ledger-note"><b>Curated ledger</b> &middot; documented highlights '
        '&middot; some bouts are not listed</p>'
        % (digits, ring, ledger, bars))

def fm_feed(a):
    """FEED panel body: empty live mount + compact fallback cards built from
    the 3 newest pulse cards. The fallback ships visible (no-JS safe);
    js/herotabs.js hides it only while a live widget attempt is pending."""
    p = a["pulse"]; handle = p["handle"]
    minis = []
    for c in p["cards"][:3]:
        head = ('<div class="fm-mini-top"><span class="fm-mini-av">%s</span>'
                '<span class="fm-mini-who"><b>%s</b><span>@%s</span></span>'
                '<span class="fm-mini-date">%s</span></div>'
                % (esc(a.get("mono", "")), esc(a["name"]), esc(handle), c["date"]))
        link = ('<a class="fm-mini-src" href="%s" target="_blank" rel="noopener">'
                'View on X &rarr;</a>' % esc(c["x_url"])) if c.get("x_url") else ""
        minis.append('<article class="fm-mini">%s<p class="fm-mini-q">%s</p>%s</article>'
                     % (head, _clip_words(c["quote"]), link))
    foot = ('<div class="fm-feed-foot"><a href="#pulse">All posts &rarr;</a>'
            '<a href="https://x.com/%s" target="_blank" rel="noopener">@%s on X</a></div>'
            % (esc(handle), esc(handle)))
    return ('<div class="fm-feed" data-x-handle="%s">'
            '<div class="fm-feed-body">'
            '<div class="fm-feed-live" aria-live="polite"></div>'
            '<div class="fm-feed-fallback">%s%s</div>'
            '</div></div>' % (esc(handle), "".join(minis), foot))

def fm_figure(a):
    """Tabbed portrait figure - FIGHT METRICS / LIVE FEED - for subjects with
    a live X pulse. data-fm-generated tells js/herotabs.js to wire the ring
    (the hand-built cm-punk page wires its own and ships without the flag).
    Default tab is FEED because the subject has a live X account."""
    return ('<figure class="portrait" aria-label="%s fight metrics and live feed" '
      'data-fm-tabs data-fm-generated data-default-tab="feed">\n'
      '      <span class="vlabel">%s</span>\n'
      '      <div class="fm-tabbar" role="tablist" aria-label="Roster card views">'
      '<button class="fm-tab" id="fmTabMetrics" type="button" role="tab" data-tab="metrics" '
      'aria-selected="false" aria-controls="fmPanelMetrics" tabindex="-1">Metrics</button>'
      '<button class="fm-tab" id="fmTabFeed" type="button" role="tab" data-tab="feed" '
      'aria-selected="true" aria-controls="fmPanelFeed">Feed</button></div>\n'
      '      <div class="fm-panel" id="fmPanelMetrics" role="tabpanel" aria-labelledby="fmTabMetrics" hidden>%s</div>\n'
      '      <div class="fm-panel" id="fmPanelFeed" role="tabpanel" aria-labelledby="fmTabFeed">%s</div>\n'
      '      <figcaption class="cap"><span class="r">Roster File &middot; %s</span><span class="n">%s</span>'
      '</figcaption>\n    </figure>'
      % (esc(a["name"]), a["vlabel"], fm_metrics(a), fm_feed(a),
         esc(a["epithet"]), esc(a["realname"])))

def hero(a):
    _h1t, _h1s = hero_name(a["name"])
    hs = "".join(
        '<div class="hstat"><b><span class="num" data-count="%s">%s</span>%s</b><span>%s</span></div>'
        % (h["value"], h["value"], '<span class="x">&times;</span>' if h.get("x") else "", esc(h["label"]))
        for h in a["hstats"])
    if a.get("pulse") and a["pulse"].get("handle"):
        fig = fm_figure(a)
    else:
        fig = ('<figure class="portrait" aria-label="%s key art">\n      <span class="slot">PHOTO SLOT</span>\n'
      '      <span class="vlabel">%s</span>\n'
      '      <svg class="crown" viewBox="0 0 64 54" aria-hidden="true"><path d="%s"/></svg>\n'
      '      <span class="mono" aria-hidden="true">%s</span>\n'
      '      <figcaption class="cap"><span class="r">Roster File &middot; %s</span><span class="n">%s</span>'
      '</figcaption>\n    </figure>'
      % (esc(a["name"]), a["vlabel"], CROWN, esc(a["mono"]),
         esc(a["epithet"]), esc(a["realname"])))
    return ('<header class="hero" id="top"><div class="wrap">\n    <div>\n'
      '      <div class="hero-kick">%s</div>\n'
      '      <h1%s><span class="the">%s</span>%s</h1>\n'
      '      <p class="hero-tag">%s</p>\n'
      '      <div class="hero-now"><span>%s</span><b>%s</b>%s</div>\n'
      '      <div class="hero-stats">%s</div>\n'
      '      <div class="hero-cta-row">\n'
      '        <button class="discover" type="button" data-scroll="#record">Explore the full record%s</button>\n'
      '        <a class="ghost-link" href="#career">%s</a>\n      </div>\n    </div>\n'
      '    %s\n  </div></header>'
      % (a["hero_kick"], _h1s, esc(a["epithet"]), _h1t, a["hero_tag"],
         a.get("now_label", "NOW"), esc(a["now_bold"]), a["now_tail"], hs, CHEV,
         esc(a["ghost_link"]), fig))

# ------------------------------------------------ THE WALK-OUT (optional)
# An entrance-theme strip between the hero and .layout: the overture before the
# dossier. OPTIONAL and data-driven, like slot10 - a subject with no DATA["theme"]
# emits nothing at all (no band, no stylesheet cost beyond the shared css, no
# js/theme-song.js tag). Shape:
#
#   DATA["theme"] = {
#     "kicker":   "Entrance theme",                  # left of the dateline
#     "since":    "Raw &middot; July 25, 2011",      # optional dateline
#     "track":    "Cult of Personality",
#     "artist":   "Living Colour",
#     "meta":     "Vivid &middot; 1988 &middot; 4:54",
#     "note":     "<b>...</b> one paragraph of HTML",
#     "cue":      {"quote": "...", "src": "..."},    # optional crowd-pop line
#     "spotify_id": "5e3YOg6fIkP0wD5TyxcHOH",        # optional; no id = links only
#     "links":    [{"svc": "Spotify", "sub": "Full track", "href": "..."}, ...],
#     "lineage":  [{"date": "2005", "title": "...", "who": "AFI &middot; ROH",
#                   "now": False}, ...],
#     "foot":     "sourcing line, may contain <a>",  # optional
#   }
#
# Two rules the markup depends on and verify() enforces:
#   1. `links` is REQUIRED and must be non-empty, because it IS the fallback and
#      the fallback is the only thing a blocked visitor ever sees.
#   2. the listen row ships UNHIDDEN. js/theme-song.js hides it only while a
#      live embed attempt is in flight (see that file's header).
def theme_band(a):
    t = a.get("theme")
    if not t:
        return ""
    head = esc(t.get("kicker", "Entrance theme"))
    if t.get("since"):
        head += " <i>&middot;</i> %s" % t["since"]
    cue = ""
    if t.get("cue"):
        cue = ('<blockquote class="wo-cue"><p>&ldquo;%s&rdquo;</p><cite>%s</cite></blockquote>'
               % (t["cue"]["quote"], t["cue"]["src"]))
    links = "".join(
        '<li><a href="%s" target="_blank" rel="noopener" aria-label="%s">'
        '<span class="wo-svc">%s</span><span class="wo-sub">%s</span>'
        '<span class="wo-go" aria-hidden="true">&rarr;</span></a></li>'
        % (esc(l["href"]),
           esc("%s by %s on %s (opens in a new tab)" % (t["track"], t["artist"], l["svc"])),
           esc(l["svc"]), esc(l["sub"]))
        for l in t["links"])
    lin = "".join(
        '<li%s><span class="wo-d">%s%s</span><span><b>%s</b>'
        '<span class="wo-w">%s</span></span></li>'
        % (' class="is-now"' if e.get("now") else "", esc(e["date"]),
           '<span class="wo-now">Now</span>' if e.get("now") else "",
           esc(e["title"]), e["who"])
        for e in t.get("lineage", []))
    lineage = ('<div class="wo-line"><p class="wo-lbl">Theme lineage</p>'
               '<ol class="wo-lin">%s</ol></div>' % lin) if lin else ""
    # cue + sourcing share one full-width strip; without either there is no strip
    foot = ('<p class="wo-foot">%s</p>' % t["foot"]) if t.get("foot") else ""
    under = ('    <div class="wo-under">%s%s</div>\n' % (cue, foot)) if (cue or foot) else ""
    # The embed is wired only when an id is present; without one the strip is
    # still complete - the listen row is the player.
    embed = ""
    if t.get("spotify_id"):
        embed = (' data-walkout data-embed="https://open.spotify.com/embed/track/%s"'
                 ' data-embed-title="%s"'
                 % (esc(t["spotify_id"]),
                    esc("Spotify player: %s by %s" % (t["track"], t["artist"]))))
    return ('<section class="walkout reveal" id="walkout" aria-labelledby="wo-h"%s>\n'
      '  <div class="walkout-in">\n'
      '    <div class="wo-rule"><span class="wo-rule-k">The walk-out</span>'
      '<span class="wo-rule-line" aria-hidden="true"></span>'
      '<span class="wo-rule-src">%s</span></div>\n'
      '    <div class="wo-grid">\n'
      '      <div class="wo-lede">\n'
      '        <p class="wo-kick">%s</p>\n'
      '        <h2 class="wo-track" id="wo-h">%s</h2>\n'
      '        <p class="wo-by">%s<span class="wo-meta">%s</span></p>\n'
      '        <p class="wo-note">%s</p>\n      </div>\n'
      '      <div class="wo-play"><p class="wo-lbl">Hear it</p>\n'
      '        <div class="wo-stage">\n'
      '          <span class="wo-wait" aria-hidden="true">Cueing the record</span>\n'
      '          <div class="wo-live" hidden></div>\n'
      '          <ul class="wo-listen">%s</ul>\n'
      '        </div>\n      </div>\n'
      '      %s\n    </div>\n%s  </div>\n</section>'
      % (embed, t.get("source_label", "Player &middot; Spotify"),
         head, esc(t["track"]), esc(t["artist"]), t.get("meta", ""), t.get("note", ""),
         links, lineage, under))

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
      '<b id="rec2-shown">%d</b> of %d matches shown</p>'
      '<p class="ledger-note"><b>Curated ledger</b> &middot; documented highlights &middot; '
      'some bouts are not listed</p></section>'
      % (cd, full_label, total, "".join(fbtns), tbtns, WL_DONUT, REC_THEAD,
         "".join(match_row(r) for r in rows), cd, total))

# ---------------------------------------------------------------- signature links + hover preview
# Signature cards link to /matches/<slug>/ breakdown pages and carry baked preview
# data (data-sp-*) that js/sig-preview.js renders on hover/focus. Two hard rules:
#
#   1. NEVER emit an href we have not stat'd on disk. Only ~a third of the signature
#      cards across the roster have a breakdown page written yet; a card with no page
#      stays an inert <div>. A thin stub would be worse than an honest non-link.
#   2. The preview is baked at build time (no fetch on hover), and it must not spoil.
#      Match pages hide the result behind .wl-spoiler-block on purpose, so the hook is
#      read from the ratingbox critic line and the spoiler paragraph is never touched.

_SIG_STOP = {"the", "and", "vs", "for", "with", "his", "her", "one", "two", "night",
             "match", "title", "championship", "world", "classic", "min", "minute"}

_SIG_ABBR = {
    "money-in-the-bank": "mitb", "wrestlemania": "wm", "survivor-series": "ss",
    "royal-rumble": "rumble", "night-of-champions": "noc", "hell-in-a-cell": "hiac",
    "elimination-chamber": "chamber", "over-the-limit": "otl", "extreme-rules": "er",
    "money-in-the-bank-ladder-match": "mitb",
}

def _sig_slugify(s):
    s = _html.unescape(str(s or ""))
    s = re.sub(r"[‘’'`]", "", s)
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def _sig_people(s):
    """Split an opponent field into individual wrestlers ('Sheamus & Drew McIntyre')."""
    parts = re.split(r"\s*(?:&amp;|&|,|/| and )\s*", _html.unescape(str(s or "")))
    return [p.strip() for p in parts if p.strip()]

def _sig_aliases(name):
    """Slug forms a real filename might use for one person: full, surname, last two."""
    s = _sig_slugify(name)
    out = {s}
    p = [x for x in s.split("-") if x]
    if len(p) > 1:
        out.add(p[-1]); out.add("-".join(p[-2:]))
    return {a for a in out if len(a) >= 3}

def _sig_year(*fields):
    for f in fields:
        m = re.search(r"\b(?:19|20)\d{2}\b", _html.unescape(str(f or "")))
        if m: return m.group(0)
    return None

def _sig_tokens(*fields):
    out = []
    for f in fields:
        for t in _sig_slugify(f).split("-"):
            if len(t) >= 3 and t not in _SIG_STOP and not t.isdigit():
                out.append(t)
    return out

def _sig_event_keys(event):
    """Slug fragments an event might appear as: full slug, known abbreviation,
    the promotion/first token, and the slug with a trailing year stripped."""
    ev = _sig_slugify(event)
    ev_noyear = re.sub(r"-?(?:19|20)\d{2}$", "", ev).strip("-")
    keys = [ev, ev_noyear]
    for full, ab in _SIG_ABBR.items():
        if ev_noyear.startswith(full): keys.append(ab)
    head = ev_noyear.split("-")[0] if ev_noyear else ""
    if head and len(head) >= 2: keys.append(head)
    keys.append(re.sub(r"[^a-z0-9]", "", "".join(w[0] for w in ev_noyear.split("-") if w))[:5])
    seen, out = set(), []
    for k in keys:
        if k and k not in seen: seen.add(k); out.append(k)
    return out

SIG_WARN = []

_SIG_DIRS = None
def _sig_match_dirs():
    """Every /matches/<slug>/ that actually has an index.html. Read from disk, never
    hardcoded: a breakdown page added to the repo lights its card up on the next build."""
    global _SIG_DIRS
    if _SIG_DIRS is None:
        d = os.path.join(ROOT, "matches")
        _SIG_DIRS = sorted(
            x for x in (os.listdir(d) if os.path.isdir(d) else [])
            if os.path.isfile(os.path.join(d, x, "index.html")))
    return _SIG_DIRS

def _sig_exists(url):
    """True if a site-absolute URL maps to a real index.html under ROOT."""
    if not url or not url.startswith("/") or "//" in url[1:]: return False
    p = os.path.join(ROOT, url.strip("/").replace("/", os.sep), "index.html")
    return os.path.isfile(p)

def _sig_has(slug, alias):
    return re.search(r"(?:^|-)%s(?:-|$)" % re.escape(alias), slug) is not None

def resolve_sig_url(subject, card):
    """Best /matches/ page for one signature card, or None. Two passes, both of which
    only ever return a path that exists on disk:
      1. construct candidate slugs (both name orders x event/abbrev x year) and stat them;
      2. failing that, scan the real directory listing for a slug naming BOTH wrestlers,
         scored on year + event tokens, and take it only if the winner is unambiguous."""
    if card.get("url"):
        # An AUTHORED url is the owner's assertion and is emitted verbatim. A checkout
        # may hold only a subset of the site (this is how the sandbox is shaped), so
        # deleting the link because the page is absent HERE would silently break a
        # link that is fine in production. Warn loudly instead; verify() exempts
        # authored urls from the must-resolve rule and holds derived ones to it.
        if not _sig_exists(card["url"]):
            SIG_WARN.append("%s / %s -> authored url %s has no index.html in this checkout"
                            % (subject, card.get("event"), card["url"]))
        return card["url"]
    subj = _sig_aliases(subject)
    people = [_sig_aliases(p) for p in _sig_people(card.get("opponent"))]
    if not subj or not people: return None
    year = _sig_year(card.get("event"), card.get("stip"))
    evkeys = _sig_event_keys(card.get("event"))

    # --- pass 1: constructed candidates
    tails = []
    for ev in evkeys + [""]:
        for y in ([year, ""] if year else [""]):
            t = "-".join(x for x in (ev, y) if x)
            if t not in tails: tails.append(t)
    for opp in people:
        for a in sorted(subj, key=len, reverse=True):
            for b in sorted(opp, key=len, reverse=True):
                for x, y in ((a, b), (b, a)):
                    for tail in tails:
                        cand = "-".join(p for p in ("%s-vs-%s" % (x, y), tail) if p)
                        if os.path.isfile(os.path.join(ROOT, "matches", cand, "index.html")):
                            return "/matches/%s/" % cand

    # --- pass 2: scored scan of what is actually on disk
    toks = set(_sig_tokens(card.get("event"), card.get("stip"))) | set(evkeys)
    namet = {t for al in list(subj) + [a for o in people for a in o] for t in al.split("-")}
    best = []
    for slug in _sig_match_dirs():
        if not any(_sig_has(slug, a) for a in subj): continue
        if not any(any(_sig_has(slug, a) for a in opp) for opp in people): continue
        dy = _sig_year(slug)
        if year and dy and dy != year: continue
        # The slug's event portion is whatever is left after the two names, "vs" and the
        # year. If it names an event and none of the card's event keys appear in it, this
        # is a DIFFERENT bout between the same two wrestlers -- do not link it.
        rest = "".join(t for t in slug.split("-")
                       if t not in namet and t != "vs" and t != dy)
        if rest and not any(k and k in rest for k in evkeys): continue
        score = (3 if (year and dy == year) else 0) + sum(1 for t in toks if _sig_has(slug, t))
        best.append((score, slug))
    if not best: return None
    best.sort(key=lambda x: (-x[0], x[1]))
    if len(best) > 1 and best[0][0] == best[1][0]:
        return None          # ambiguous (a trilogy, say) -> stay honest, stay unlinked
    return "/matches/%s/" % best[0][1]

_SIG_PV_CACHE = {}
_SIG_MONTHS = ("January|February|March|April|May|June|July|August|September|"
               "October|November|December")

def _sig_text(s):
    return re.sub(r"\s+", " ", _html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()

def sig_preview(url):
    """Read the real target page and lift the five preview fields. Build time only —
    the hover panel never touches the network. Returns {} when the page is not a
    match breakdown (e.g. a card that points at a wrestler dossier) so the card
    still links but simply carries no panel."""
    if url in _SIG_PV_CACHE: return _SIG_PV_CACHE[url]
    out = {}
    p = os.path.join(ROOT, url.strip("/").replace("/", os.sep), "index.html")
    try:
        h = open(p, encoding="utf-8").read()
    except OSError:
        _SIG_PV_CACHE[url] = out; return out
    m = re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S)
    out["title"] = _sig_text(m.group(1)) if m else ""
    m = re.search(r'<p class="hero__lead"[^>]*>(.*?)</p>', h, re.S)
    lead = _sig_text(m.group(1)) if m else ""
    if lead:
        dm = re.search(r"\b(?:%s)\s+\d{1,2},\s+\d{4}\b" % _SIG_MONTHS, lead)
        out["date"] = dm.group(0) if dm else ""
        out["where"] = lead.rsplit("·", 1)[1].strip() if "·" in lead else ""
        head = lead.split("—")[0].strip()
        out["event"] = head if head and head != lead else (lead if not out["date"] else "")
    m = re.search(r'class="ratingbox__big"[^>]*>\s*([0-9](?:\.[0-9]+)?)', h)
    out["rate"] = m.group(1) if m else ""
    m = re.search(r'class="rating__stars"[^>]*>(.*?)</span>', h, re.S)
    out["stars"] = _sig_text(m.group(1)) if m else ""
    # The hook is the ratingbox critic line. The lede proper lives inside
    # .wl-spoiler-block and states the result — baking it would spoil the page.
    i = h.find('class="ratingbox"')
    if i != -1:
        m = re.search(r'<p class="muted"[^>]*>(.*?)</p>', h[i:i + 3000], re.S)
        if m: out["hook"] = _sig_text(m.group(1))
    if not out.get("hook"):
        body = re.sub(r'<div class="wl-spoiler-block".*?</div>', " ", h, flags=re.S)
        j = body.find("<h2>The Story</h2>")
        if j != -1:
            m = re.search(r"<p>(.*?)</p>", body[j:j + 4000], re.S)
            if m:
                t = _sig_text(m.group(1))
                s = re.split(r"(?<=[.!?])\s+", t)
                out["hook"] = _clip_words(esc(s[0] if s else t), 150) if t else ""
                out["hook"] = _html.unescape(out["hook"])
    out = {k: v for k, v in out.items() if v}
    # A card may legitimately point somewhere that is not a match breakdown (a
    # dossier, say). No rating + title means no panel — the card still links.
    if not (out.get("rate") and out.get("title")): out = {}
    _SIG_PV_CACHE[url] = out
    return out

def sig_card(subject, c):
    """One signature card: <a> with baked preview data when a real page backs it,
    inert <div> when nothing does."""
    # A rating can legitimately be non-numeric: the research rule is "never
    # invent a star rating", so a match with no verifiable Observer grade
    # arrives as "&mdash;". int(float(...)) crashed on the first such module
    # (batista). An unrated match renders its dash and no star row - honest
    # data must not be a build error.
    try:
        stars = "★" * int(float(c["rating"]))
    except (TypeError, ValueError):
        stars = ""
    star_html = '<span class="sig2-stars">%s</span>' % stars if stars else ""
    inner = ('<div class="sig2-top"><span class="sig2-rate">%s</span>%s</div>'
             '<h3 class="sig2-ev">%s</h3><p class="sig2-opp">vs %s</p><p class="sig2-stip">%s</p>'
             % (c["rating"], star_html, esc(c["event"]), esc(c["opponent"]), esc(c["stip"])))
    url = resolve_sig_url(subject, c)
    if not url:
        return '<div class="sig2-card">%s</div>' % inner
    pv = sig_preview(url)
    at = "".join(' data-sp-%s="%s"' % (k, esc(pv[k]))
                 for k in ("title", "date", "where", "event", "rate", "stars", "hook")
                 if pv.get(k))
    return '<a class="sig2-card sig2-card--link" href="%s"%s>%s</a>' % (esc(url), at, inner)

def sec_signature(n, a):
    cards = a["signature"]
    reel = len(cards) >= 8
    out = [sig_card(a["name"], c) for c in cards]
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
    """Overview paragraphs, on classes instead of inline styles.

    * Every paragraph is <p class="ov-p">; css/dossier.css ("PROSE & SPREAD")
      owns the measure, the fluid size and the spacing. No inline styles, no
      !important fighting.
    * a["correction"] — an int index into a["overview"] — marks the paragraph
      that corrects a widely repeated error about the subject. It is wrapped
      in the framed <aside class="corr"> ("Setting one thing straight") and
      splits into two print columns at >=1600px.
    * MARGIN PULL-FACTS are authored inline in the overview strings:
          <span class="pull" aria-hidden="true">
            <span class="pull-fig">650</span>
            <span class="pull-cap">days as champion &mdash; ...</span></span>
      pull-fig--sm for words/dates; pull--q + pull-quote for a quote pull.
      A pull must DUPLICATE a fact already present in the running text — it is
      aria-hidden and display:none below 1600px, so it must be able to vanish
      without losing information. Facts only. Never author a pull inside the
      correction paragraph: the .corr frame clears the pull band.
    """
    corr = a.get("correction")
    ps = []
    for i, p in enumerate(a["overview"]):
        para = '<p class="ov-p">%s</p>' % p
        if corr is not None and i == corr:
            para = ('<aside class="corr"><h3 class="corr-kick">Setting one thing straight</h3>'
                    '%s</aside>' % para)
        ps.append(para)
    return sec_h(n, "overview") + "".join(ps) + "</section>"

def sec_pulse(n, a):
    """Optional 'Right Now' social pulse. Cards are curated, press-verified posts -
    never fabricated, never given invented engagement counts. A card with x_url gets
    X-embed chrome (avatar monogram, name/handle, X glyph, View on X); platform
    cards get a chip instead. cm-punk's hand-authored section defined the vocabulary."""
    p = a["pulse"]
    cards = []
    for c in p["cards"]:
        cls = "pulse-card" + (" pulse-featured" if c.get("wide") else "") + (" pulse-card--x" if c.get("x_url") else "")
        if c.get("x_url"):
            top = ('<div class="pulse-xhead"><span class="pulse-av">%s</span>'
                   '<span class="pulse-who"><b>%s</b><span>@%s</span></span>'
                   '<span class="pulse-xglyph" aria-hidden="true">&#120143;</span></div>'
                   % (esc(a.get("mono","")), esc(a["name"]), esc(p["handle"])))
        else:
            top = ('<div class="pulse-top"><span class="pulse-chip">%s</span>'
                   '<span class="pulse-date">%s</span></div>' % (esc(c.get("chip","")), c["date"]))
        body = '<p class="pulse-quote">%s</p>' % c["quote"]
        if c.get("why"): body += '<p class="pulse-why">%s</p>' % c["why"]
        links = ""
        if c.get("x_url"):
            links += ('<span class="pulse-date">%s</span><a class="pulse-src" href="%s" target="_blank" '
                      'rel="noopener">View on X &rarr;</a>' % (c["date"], esc(c["x_url"])))
        if c.get("src_url"):
            links += ('<a class="pulse-src" href="%s" target="_blank" rel="noopener">via %s &rarr;</a>'
                      % (esc(c["src_url"]), esc(c["src"])))
        cards.append('<article class="%s">%s%s<div class="pulse-links">%s</div></article>'
                     % (cls, top, body, links))
    foot = ('<p class="pulse-foot">%s</p>' % p["foot"]) if p.get("foot") else ""
    h = sec_h(n, "pulse")
    h = h.replace("<h2>%s</h2>" % SEC_META["pulse"][0], "<h2>Right Now</h2>")
    return h + lead(p["lead"]) + '<div class="pulse-grid">%s</div>%s</section>' % ("".join(cards), foot)

BUILDERS = {"overview": sec_overview, "record": sec_record, "signature": sec_signature, "pulse": sec_pulse,
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
    # Wording: count + noun ("10 SOURCE NOTES"), so the control answers "what
    # is this?" at a glance. The title keeps the full fraction; rail.js keeps
    # the full-sentence accessible name.
    cred = ('<p class="tt-cred" title="%d of %d entries carry a source note">'
            '<span class="tt-n">%d</span><span class="tt-lbl">source notes</span></p>'
            % (sourced, total, sourced)) if total else ""
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
    band = theme_band(a)
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
      '<!-- ===== THE WALK-OUT (entrance theme) ===== -->\n%s'
      '<div class="layout"><main class="profile-main">\n    %s\n  </main>%s</div>\n'
      '<footer class="site-footer site-footer--fat" data-wl-shell></footer>\n'
      '<script>%s</script>\n'
      '<script src="/js/main.js?v=%s"></script>\n'
      '<script src="/js/search-index.js?v=%s" defer></script>\n'
      '<script src="/js/nav.js?v=%s" defer></script>\n'
      '<script src="/js/engage.js?v=%s" defer></script>\n'
      '<script src="/js/profile.js?v=%s" defer></script>\n'
      '<script src="/js/rail.js?v=%s"></script>\n'
      '<script src="/js/herotabs.js?v=%s" defer></script>\n'
      '<script src="/js/sig-preview.js?v=%s" defer></script>\n'
      '%s<script>%s</script>\n</body>\n</html>\n'
      % (esc(title), esc(a["meta_desc"]), u, esc(a["name"]), esc(a["epithet"]), esc(a["og_desc"]), u,
         BASE, esc(a["name"]), BASE, esc(a["name"]), esc(a["epithet"]), esc(a["tw_desc"]),
         ASSET_V, jsonld(a, secs), ASSET_V, ASSET_V,
         subnav(a, secs), idn(a), hero(a), (band + "\n") if band else "",
         "\n    ".join(body_secs), rail(a),
         FACT_JS, ASSET_V, ASSET_V, ASSET_V, ASSET_V, ASSET_V, ASSET_V, ASSET_V, ASSET_V,
         ('<script src="/js/theme-song.js?v=%s" defer></script>\n' % ASSET_V) if band else "",
         tail))

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
    corr = a.get("correction")
    if corr is not None:
        if not isinstance(corr, int) or not (0 <= corr < len(a["overview"])):
            errs.append("correction=%r is not a valid overview index" % (corr,))
        elif re.search(r'<span class="pull(?: pull--q)?"', a["overview"][corr]):
            errs.append("a .pull is authored inside the correction paragraph (the .corr frame clears the band)")
    for i, p in enumerate(a["overview"]):
        n_pull = len(re.findall(r'<span class="pull(?: pull--q)?"', p))
        if n_pull != p.count('aria-hidden="true"><span class="pull-'):
            errs.append("overview[%d]: malformed .pull markup (needs aria-hidden + pull-fig/pull-quote child)" % i)
        if n_pull != p.count('class="pull-cap"') + p.count('class="pull-quote"'):
            errs.append("overview[%d]: a .pull is missing its pull-cap/pull-quote" % i)
    t = a.get("theme")
    if t is not None:
        for k in ("track", "artist", "note"):
            if not t.get(k): errs.append("theme is missing %s" % k)
        # the listen row IS the fallback; a theme with no links has no fallback
        if not t.get("links"): errs.append("theme has no links -> the fallback would be empty")
        for l in t.get("links", []):
            for k in ("svc", "sub", "href"):
                if not l.get(k): errs.append("theme link missing %s" % k)
            if not str(l.get("href", "")).startswith("https://"):
                errs.append("theme link href is not https: %r" % l.get("href"))
        for e in t.get("lineage", []):
            for k in ("date", "title", "who"):
                if not e.get(k): errs.append("theme lineage entry missing %s" % k)
        if len([e for e in t.get("lineage", []) if e.get("now")]) > 1:
            errs.append("theme lineage flags more than one entry as now")
        sid = t.get("spotify_id")
        # a guessed id is worse than no player at all: Spotify base-62 ids are 22 chars
        if sid is not None and not re.fullmatch(r"[A-Za-z0-9]{22}", str(sid)):
            errs.append("theme spotify_id %r is not a 22-char Spotify track id" % sid)
        if t.get("cue") and not (t["cue"].get("quote") and t["cue"].get("src")):
            errs.append("theme cue needs both quote and src")
        if '<ul class="wo-listen">' in htmlstr and 'class="wo-listen" hidden' in htmlstr:
            errs.append("the walk-out fallback ships hidden (it must be visible without JS)")
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', htmlstr, re.S):
        try: json.loads(m)
        except Exception as e: errs.append("invalid JSON-LD: %s" % e)
    authored = {c["url"] for c in a.get("signature", []) if c.get("url")}
    for href in re.findall(r'<a class="sig2-card sig2-card--link" href="([^"]+)"', htmlstr):
        href = _html.unescape(href)
        # Derived links must resolve. Authored ones are the owner's call (see
        # resolve_sig_url) and only earn a WARN, so a partial checkout still builds.
        if href not in authored and not _sig_exists(href):
            errs.append("signature card links %s which has no index.html on disk" % href)
    for card in re.findall(r'<a class="sig2-card sig2-card--link"[^>]*>', htmlstr):
        if "data-sp-" in card and not ('data-sp-title="' in card and 'data-sp-rate="' in card):
            errs.append("signature preview data is half-baked (needs title + rate)")
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
    for w in SIG_WARN: print("  WARN signature: %s" % w)
    print("done: %d dossier pages  ROOT=%s" % (n, ROOT))
    print("now run: python3 build/apply_shell.py")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
