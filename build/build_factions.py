#!/usr/bin/env python3
"""build_factions.py - generate /factions/<slug>/ pages from data modules.

Data lives in build/facdata/<slug>.py as a module-level DATA dict; the markup is
emitted from that data; verify() fails the build rather than shipping a page
that contradicts itself.

THE TEMPLATE
------------
Faction pages are SITE pages, not dossier pages. The house vocabulary for this
template is the one already shipping in /factions/the-shield/ and
/factions/the-bloodline/ - i.e. css/site.css, not the .wl-dossier world:

    .crumbs  .wrap  .ev-hero > .wrap.ev-hero__inner (with .ev-hero__brand)
    .ev-lede  .meta-chips > .meta-chip(.meta-chip--gold)
    .sec-h > h2
    .grid-cards > article.card
        span.chip.chip--wwe.card__tag
        a.card__media[aria-label] > span.card__initials      (linked member)
        span.card__media[aria-hidden] > span.card__initials  (unlinked member)
        div.card__body > h3.card__title > a.card__link
                       + p.card__meta
    .moment-body  .answer  .stats-strip  table.data  .timeline
    .champ-row/.cr-title/.cr-reign/.cr-note  .sig-grid > .sig-card
    .persona-grid > .persona-card  .faq > details > .faq__body  .rel/.rel__type
    .related-links > .related-links__a
    h1 form: The <span class="accent">Shield</span>

Every one of those classes already exists in css/site.css. The ONLY new CSS this
template needs is the richer timeline row (date + heading + paragraph), which
site.css's .timeline does not cover, plus a shrink modifier for six-character
card initials. Both live at the bottom of css/dossier.css under a banner and are
scoped to .wl-faction so nothing existing can move.

The rules that are easy to get wrong, and are enforced here:

  1. A section with no rows is dropped, not emitted empty. The Straight Edge
     Society held no championship, so it has no Championships section, and the
     prose says so instead. verify() asserts the emitted h2s are exactly the
     ones sections_for() asked for, in order.
  2. A member or moment links out ONLY when the target page exists on disk.
     There is no allowlist to fall out of date: link_for() stats the filesystem.
     A subject whose page does not exist renders as plain text - the site card
     vocabulary has a first-class shape for that (span.card__media[aria-hidden],
     plain h3.card__title), copied straight off the-bloodline. verify() re-reads
     the finished HTML and asserts that every internal href resolves.
  3. JSON-LD is emitted through json.dumps and never hand-written. Sixty pages
     on this site once shipped an unparseable FAQPage because the hand-authored
     markup used single-quoted strings.
  4. FAQ HTML and FAQPage JSON-LD must match 1:1 in count and order, and the
     Organization member[] must match the Members grid 1:1. verify() counts the
     rendered HTML, not the data, so a renderer bug cannot hide behind the data.
  5. Prose fields carry HTML entities (&mdash;, &ldquo;) on purpose, so they are
     emitted raw. verify() rejects a bare "<" or a bare "&" in any prose field
     so a stray character cannot break the document, and rejects any
     "&amp;middot;"-style double escape in the output.
  6. patch_factions_index() INSERTS into the real hub. It never rewrites it:
     it reads the existing article.card blocks, adds only the missing ones in
     the alphabetical slot they belong in, and re-runs are no-ops.

Run:  WL_ROOT="$PWD" python3 build/build_factions.py [slug ...]
Then: WL_ROOT="$PWD" python3 build/apply_shell.py
"""

import datetime, html as _html, json, os, re, sys

ROOT = os.environ.get("WL_ROOT", os.getcwd())
BASE = "https://wrestlelore.com"
# Placeholder only. apply_shell.py hashes css/ + js/ and rewrites every ?v=
# across the site, so this value is always overwritten on the next shell pass.
ASSET_V = "122a6b76"
TODAY = datetime.date.today()

# Collected during a run so main() can report what linked and what did not.
LINK_LOG = []


def esc(s):
    return _html.escape(str(s), quote=True) if s is not None else ""


def esc_a(s):
    """Escape for a double-quoted attribute or element text, leaving ' alone.

    html.escape(quote=True) turns every apostrophe into &#x27;, which is
    harmless but litters <title> and meta description - the two strings most
    likely to be read by a human in a search result or a browser tab.
    Double-quoted attributes only need & < > and ".
    """
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;")) if s is not None else ""


# ---------------------------------------------------------------- link safety
def page_exists(path):
    """True when /a/b/ resolves to <ROOT>/a/b/index.html on disk."""
    p = os.path.join(ROOT, path.strip("/"), "index.html")
    return os.path.isfile(p)


def link_for(kind, slug, label):
    """Anchor when the target page exists, escaped plain text when it does not.

    kind is "wrestlers" or "matches". Nothing is linked on faith: a slug that
    has no index.html on disk is logged and rendered as text, because a faction
    page full of 404s is worse than one full of plain names.
    """
    text = esc(label)
    if not slug:
        LINK_LOG.append((kind, None, label, "no-slug"))
        return text
    path = "/%s/%s/" % (kind, slug)
    if page_exists(path):
        LINK_LOG.append((kind, slug, label, "linked"))
        return '<a href="%s">%s</a>' % (path, text)
    LINK_LOG.append((kind, slug, label, "missing"))
    return text


def href_for(path):
    """The path when it resolves on disk, else None. Same policy as link_for."""
    if page_exists(path):
        LINK_LOG.append(("explore", path, path, "linked"))
        return path
    LINK_LOG.append(("explore", path, path, "missing"))
    return None


# ------------------------------------------------------------------ initials
# .card__initials is a single Anton/Oswald token sized at --fs-800 (up to
# 3.6rem). The shipped pages use 2-5 characters: SHLD, BLDL, ROMAN, JEY, PAUL.
# Six fits only at a smaller size, hence the --long modifier.
def initials_for(name):
    words = [w for w in re.split(r"[^A-Za-z0-9']+", str(name)) if w]
    if words and words[0].lower() == "the" and len(words) > 1:
        words = words[1:]
    if not words:
        return "WL"
    for cand in (words[-1], words[0]):
        if 2 <= len(cand) <= 6:
            return cand.upper()
    return words[-1][:6].upper()


def initials_html(name):
    tok = initials_for(name)
    cls = "card__initials card__initials--long" if len(tok) > 5 else "card__initials"
    return '<span class="%s">%s</span>' % (cls, esc(tok))


def acronym_for(name):
    """SES / NN / SCS - the hub's own card__initials style for a faction."""
    words = [w for w in re.split(r"[^A-Za-z0-9]+", str(name)) if w]
    if words and words[0].lower() == "the" and len(words) > 1:
        words = words[1:]
    return "".join(w[0] for w in words).upper()[:5] or "WL"


def chip_for(promotion):
    """The site's promotion chip. Gold is the house fallback: the shipped hub
    uses chip--gold for NJPW, so anything without a dedicated colour gets it."""
    key = str(promotion).strip().lower()
    known = {"wwe": "wwe", "wwf": "wwe", "wwf/wwe": "wwe", "wcw": "wcw",
             "ecw": "ecw", "tna": "tna", "nxt": "nxt", "njpw": "njpw"}
    return "chip chip--%s card__tag" % known.get(key, "gold")


# ------------------------------------------------------------------ sections
SEC_META = {
    "overview":  "Overview",
    "members":   "Members",
    "timeline":  "Timeline",
    "titles":    "Championships",
    "moments":   "Signature Moments",
    "legacy":    "Legacy",
    "faq":       "Frequently Asked",
    "sources":   "Sources",
}
SEC_ORDER = ["overview", "members", "timeline", "titles", "moments", "legacy", "faq", "sources"]


def sections_for(f):
    """Ordered ids this faction actually emits. A section with no rows is dropped."""
    out = []
    for sid in SEC_ORDER:
        if sid == "titles" and not f.get("titles"):
            continue          # the Straight Edge Society held nothing; say so in prose instead
        if sid == "moments" and not f.get("moments"):
            continue
        out.append(sid)
    return out


def sec_h(sid, count=None):
    """The site section header. Exactly the-shield's markup, plus the optional
    .count span css/site.css already styles."""
    c = '<span class="count">%s</span>' % esc(count) if count else ""
    return ('\n  <div class="sec-h" id="%s"><h2>%s</h2>%s</div>\n  '
            % (sid, SEC_META[sid], c))


def lead(t):
    return '<p class="muted">%s</p>\n  ' % t if t else ""


def note(t):
    return '\n  <p class="form-note">%s</p>' % t if t else ""


# ------------------------------------------------------------------ 01 overview
def sec_overview(f):
    """Answer-first paragraph in .answer, the rest in .moment-body, the numbers
    in .stats-strip and the sourced quick facts in the site's table.data."""
    body = "".join("<p>%s</p>" % p for p in f["overview"][1:])
    stats = "".join('<div><div class="stat-num">%s</div><div class="stat-lbl">%s</div></div>'
                    % (esc(v), esc(l)) for v, l in f["stats"])
    rows = []
    for r in f["tape"]:
        sub = '<br><span class="dim">%s</span>' % r["sub"] if r.get("sub") else ""
        rows.append("<tr><th>%s</th><td>%s%s</td></tr>" % (esc(r["label"]), r["value"], sub))
    return (sec_h("overview") + lead(f["overview_lead"]) +
            '<p class="answer">%s</p>\n  ' % f["overview"][0] +
            '<div class="moment-body">%s</div>\n  ' % body +
            '<div class="stats-strip">%s</div>\n  ' % stats +
            '<div class="table-wrap" style="margin-top:var(--sp-5)">'
            '<table class="data"><caption>Tale of the tape</caption>'
            '<tbody>%s</tbody></table></div>' % "".join(rows))


# -------------------------------------------------------------------- 02 members
def member_card(m, promo):
    """the-shield's card when the wrestler has a page, the-bloodline's
    aria-hidden variant when they do not. Same shape either way.

    promo is the faction's promotion: a member card carries the faction's chip,
    exactly as the shipped pages do (every Bloodline card reads "WWE").
    """
    name = esc(m["name"])
    ini = initials_html(m["name"])
    slug = m.get("slug")
    path = "/wrestlers/%s/" % slug if slug else None
    if path and page_exists(path):
        LINK_LOG.append(("wrestlers", slug, m["name"], "linked"))
        media = ('<a class="card__media" href="%s" aria-label="%s">%s</a>' % (path, name, ini))
        title = '<h3 class="card__title"><a class="card__link" href="%s">%s</a></h3>' % (path, name)
    else:
        LINK_LOG.append(("wrestlers", slug, m["name"], "missing" if slug else "no-slug"))
        media = '<span class="card__media" aria-hidden="true">%s</span>' % ini
        title = '<h3 class="card__title">%s</h3>' % name
    return ('<article class="card">\n'
            '      <span class="%s">%s</span>\n'
            '      %s\n'
            '      <div class="card__body">%s<p class="card__meta">%s</p></div>\n'
            '    </article>'
            % (chip_for(promo), esc(promo), media, title, m["role"]))


def sec_members(f):
    promo = promo_label(f)
    cards = "\n    ".join(member_card(m, promo) for m in f["members"])
    notes = "".join('<article class="sig-card"><h3>%s</h3>'
                    '<p class="card__meta">%s &middot; %s</p><p>%s</p></article>'
                    % (esc(m["name"]), m["dates"], m["role"], m["note"]) for m in f["members"])
    return (sec_h("members", "%d members" % len(f["members"])) + lead(f["members_lead"]) +
            '<div class="grid-cards">\n    %s\n  </div>\n  ' % cards +
            '<h3 class="night-h">Who they were</h3>\n  ' +
            '<div class="sig-grid">%s</div>' % notes +
            note(f.get("members_note")))


# ------------------------------------------------------------------- 03 timeline
def sec_timeline(f):
    rows = "".join('<li><span class="tl-year">%s</span>'
                   '<h3 class="tl-title">%s</h3><p class="tl-desc">%s</p></li>'
                   % (r["when"], r["title"], r["desc"]) for r in f["timeline"])
    return (sec_h("timeline", "%d beats" % len(f["timeline"])) + lead(f["timeline_lead"]) +
            '<ol class="timeline">%s</ol>' % rows)


# --------------------------------------------------------------- 04 championships
def sec_titles(f):
    rows = "".join('<div class="champ-row"><span class="cr-title">%s %s</span>'
                   '<span class="cr-reign">%s %s</span><span class="cr-note">%s</span></div>'
                   % (r.get("ic", "&#9733;"), r["name"], esc(r["count"]), esc(r["unit"]), r["sub"])
                   for r in f["titles"])
    return (sec_h("titles", "%d reigns" % len(f["titles"])) + lead(f["titles_lead"]) +
            '<div class="stat-card">%s</div>' % rows + note(f.get("titles_note")))


# ------------------------------------------------------------------- 05 moments
def sec_moments(f):
    rows = "".join('<article class="sig-card"><h3>%s</h3>'
                   '<p class="card__meta">%s &middot; %s</p><p>%s</p></article>'
                   % (link_for("matches", m.get("match_slug"), m["title"]),
                      esc(m["year"]), esc(m["kind"]), m["desc"]) for m in f["moments"])
    return (sec_h("moments", "%d moments" % len(f["moments"])) + lead(f["moments_lead"]) +
            '<div class="sig-grid">%s</div>' % rows)


# -------------------------------------------------------------------- 06 legacy
def sec_legacy(f):
    ps = "".join("<p>%s</p>" % p for p in f["legacy"])
    cards = "".join('<article class="persona-card"><h3>%s</h3>'
                    '<p class="card__meta">%s</p><p>%s</p></article>'
                    % (esc(c["name"]), c["era"], c["desc"]) for c in f["after"])
    return (sec_h("legacy") + lead(f["legacy_lead"]) +
            '<div class="moment-body">%s</div>\n  ' % ps +
            '<h3 class="night-h">Where they went</h3>\n  ' +
            '<div class="persona-grid">%s</div>' % cards)


# ----------------------------------------------------------------------- 07 faq
def sec_faq(f):
    items = "".join('<details><summary>%s</summary><div class="faq__body">%s</div></details>'
                    % (q["q"], q["a"]) for q in f["faq"])
    return (sec_h("faq", "%d questions" % len(f["faq"])) + lead(f.get("faq_lead", "")) +
            '<div class="faq">%s</div>' % items)


# ------------------------------------------------------------------- 08 sources
def sec_sources(f):
    items = "".join('<div class="rel"><span class="rel__type">%s</span>'
                    '<a href="%s" target="_blank" rel="noopener nofollow">%s</a></div>'
                    % (esc(s["k"]), esc(s["href"]), esc(s["v"])) for s in f["sources"])
    return (sec_h("sources", "%d sources" % len(f["sources"])) + lead(f["sources_lead"]) +
            '<div class="grid-3">%s</div>' % items + note(f.get("sources_note")))


BUILDERS = {"overview": sec_overview, "members": sec_members, "timeline": sec_timeline,
            "titles": sec_titles, "moments": sec_moments, "legacy": sec_legacy,
            "faq": sec_faq, "sources": sec_sources}


# ---------------------------------------------------------------------- hero
def hero(f):
    """Byte-for-byte the-shield's hero: .ev-hero > .wrap.ev-hero__inner, with the
    crumbs, the brand eyebrow, the accent h1 and the meta chips in that order."""
    chips = "\n      ".join('<span class="meta-chip%s">%s</span>'
                            % (" meta-chip--gold" if c.get("gold") else "", c["html"])
                            for c in f["chips"])
    return ('<section class="ev-hero">\n'
            '  <div class="wrap ev-hero__inner">\n'
            '    <nav class="crumbs" aria-label="Breadcrumb"><ol>'
            '<li><a href="/">Home</a></li>'
            '<li><a href="/factions/">Factions</a></li>'
            '<li aria-current="page">%s</li></ol></nav>\n'
            '    <span class="ev-hero__brand">%s</span>\n'
            '    <h1>%s <span class="accent">%s</span></h1>\n'
            '    <div class="meta-chips">\n      %s\n    </div>\n'
            '  </div>\n'
            '</section>'
            # brand carries entities (&middot;, &ndash;) so it is emitted raw and
            # policed by the prose hygiene check in verify(); esc() here would
            # double-escape it into a literal "&middot;" on the page.
            % (esc(f["name"]), f["brand"], esc(f["h1_a"]), esc(f["h1_b"]), chips))


# ------------------------------------------------------------------ explore more
def explore(f):
    """the-shield's Explore more: one .related-links row of .related-links__a
    pills. Only ever links to pages that exist on disk."""
    pills = []
    for it in f["explore"]:
        h = href_for(it["href"])
        if h:
            pills.append('<a class="related-links__a" href="%s">%s</a>' % (esc(h), esc(it["name"])))
    if not pills:
        return ""
    return (sec_h_plain("Explore more") +
            '<nav class="related-links" aria-label="Related pages">\n    %s\n  </nav>'
            % "".join(pills))


def sec_h_plain(label):
    return '\n  <div class="sec-h"><h2>%s</h2></div>\n  ' % label


# -------------------------------------------------------------------- JSON-LD
def jsonld(f):
    u = "%s/factions/%s/" % (BASE, f["slug"])
    members = []
    for m in f["members"]:
        person = {"@type": "Person", "name": m["name"]}
        if m.get("slug") and page_exists("/wrestlers/%s/" % m["slug"]):
            person["url"] = "%s/wrestlers/%s/" % (BASE, m["slug"])
        if m.get("sameAs"):
            person["sameAs"] = m["sameAs"]
        role = {"@type": "OrganizationRole", "roleName": m["ld_role"], "member": person}
        if m.get("start_iso"):
            role["startDate"] = m["start_iso"]
        if m.get("end_iso"):
            role["endDate"] = m["end_iso"]
        members.append(role)

    org = {"@type": "Organization", "@id": u + "#faction", "name": f["name"],
           "url": u, "description": f["ld_description"],
           "foundingDate": f["founded_iso"], "dissolutionDate": f["dissolved_iso"],
           "member": members,
           "parentOrganization": {"@type": "Organization", "name": f["promotion_full"]},
           "sameAs": [s["href"] for s in f["sources"]]}
    if f.get("alternate_names"):
        org["alternateName"] = f["alternate_names"]
    if f.get("founding_location"):
        org["foundingLocation"] = {"@type": "Place", "name": f["founding_location"]}
    if f.get("ld_knows"):
        org["knowsAbout"] = f["ld_knows"]

    graph = [org,
             {"@type": "WebPage", "@id": u + "#webpage", "url": u,
              "name": f["ld_page_name"], "about": {"@id": u + "#faction"},
              "isPartOf": {"@type": "WebSite", "name": "Wrestle Lore", "url": BASE + "/"},
              "speakable": {"@type": "SpeakableSpecification",
                            "cssSelector": [".answer", ".faq__body"]},
              "primaryImageOfPage": BASE + "/assets/wrestle-lore-logo.png"},
             {"@type": "BreadcrumbList", "itemListElement": [
                 {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
                 {"@type": "ListItem", "position": 2, "name": "Factions",
                  "item": BASE + "/factions/"},
                 {"@type": "ListItem", "position": 3, "name": f["name"], "item": u}]},
             {"@type": "FAQPage", "mainEntity": [
                 {"@type": "Question", "name": q["q_ld"],
                  "acceptedAnswer": {"@type": "Answer", "text": q["a_ld"]}} for q in f["faq"]]}]
    # json.dumps guarantees valid JSON. Never hand-write this block.
    return ('<script type="application/ld+json">%s</script>'
            % json.dumps({"@context": "https://schema.org", "@graph": graph},
                         ensure_ascii=False, separators=(",", ":")))


# ----------------------------------------------------------------------- page
def page(f):
    secs = sections_for(f)
    u = "%s/factions/%s/" % (BASE, f["slug"])
    body = "".join(BUILDERS[sid](f) for sid in secs) + explore(f)
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
            '<title>%s</title>\n<meta name="description" content="%s">\n'
            '<meta name="robots" content="index,follow,max-image-preview:large">\n'
            '<link rel="canonical" href="%s">\n'
            '<meta property="og:type" content="article">\n'
            '<meta property="og:site_name" content="Wrestle Lore">\n'
            '<meta property="og:title" content="%s">\n'
            '<meta property="og:description" content="%s">\n'
            '<meta property="og:url" content="%s">\n'
            '<meta property="og:image" content="%s/assets/wrestle-lore-logo.png">\n'
            '<meta property="og:image:alt" content="%s on Wrestle Lore">\n'
            '<meta name="twitter:card" content="summary_large_image">\n'
            '<meta name="twitter:title" content="%s">\n'
            '<meta name="twitter:description" content="%s">\n'
            '<meta name="twitter:image" content="%s/assets/wrestle-lore-logo.png">\n'
            '<link rel="preload" href="/fonts/anton-latin-400-normal.woff2" as="font" '
            'type="font/woff2" crossorigin>\n'
            '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
            '<link rel="icon" href="/favicon.ico" sizes="any">\n'
            '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n'
            '<link rel="manifest" href="/site.webmanifest">\n'
            '<meta name="theme-color" content="#0b0c10">\n'
            '<link rel="stylesheet" href="/css/site.css?v=%s">\n'
            '<link rel="stylesheet" href="/css/dossier.css?v=%s">\n%s\n'
            '</head>\n<body>\n'
            '<a class="skip-link" href="#main">Skip to content</a>\n'
            '<header class="site-header nav7"></header>\n'
            '<main id="main" class="wl-faction">\n'
            '%s\n\n'
            '<div class="wrap">%s\n</div>\n'
            '</main>\n'
            '<footer class="site-footer site-footer--fat" data-wl-shell></footer>\n'
            '<script src="/js/main.js?v=%s"></script>\n'
            '<script src="/js/search-index.js?v=%s" defer></script>\n'
            '<script src="/js/nav.js?v=%s" defer></script>\n'
            '</body>\n</html>\n'
            # esc_a, not esc: <title> and the meta strings are read by humans and
            # do not need apostrophes turned into &#x27;
            % (esc_a(f["title"]), esc_a(f["meta_desc"]), u,
               esc_a(f["og_title"]), esc_a(f["og_desc"]), u, BASE, esc_a(f["name"]),
               esc_a(f["og_title"]), esc_a(f["tw_desc"]), BASE,
               ASSET_V, ASSET_V, jsonld(f),
               hero(f), body,
               ASSET_V, ASSET_V, ASSET_V))


def promo_label(f):
    """The chip text for this faction's promotion: "WWE", "ROH", ... Taken from
    the front of the hero brand ("WWE &middot; 2009&ndash;2010") so it can never
    disagree with what the hero says."""
    return re.split(r"\s*&(?:middot|nbsp);\s*|\s+&", str(f["brand"]))[0].strip()


# --------------------------------------------------------------------- verify
PROSE_KEYS = ("brand", "lede", "overview_lead", "members_lead", "timeline_lead",
              "titles_lead", "moments_lead", "legacy_lead", "sources_lead")


def _prose_ok(s):
    """Prose carries entities on purpose. Reject a bare '<' or a bare '&'."""
    bad = []
    if re.search(r"<(?!/?(?:b|i|em|strong|a|span|br)\b)", s):
        bad.append("bare '<'")
    if re.search(r"&(?!(?:[a-zA-Z][a-zA-Z0-9]{1,9}|#\d{1,5}|#x[0-9a-fA-F]{1,5});)", s):
        bad.append("bare '&'")
    return bad


def verify(f, htmlstr):
    """Fail loudly rather than shipping a page that contradicts itself."""
    errs = []
    secs = sections_for(f)

    # 1. the emitted section headers are exactly the ones sections_for() asked
    #    for, in order, plus the unnumbered Explore more block at the end.
    got = re.findall(r'<div class="sec-h"(?: id="[a-z]+")?><h2>([^<]+)</h2>', htmlstr)
    want = [SEC_META[s] for s in secs] + ["Explore more"]
    if got != want:
        errs.append("section headers %r != expected %r" % (got, want))

    # 2. the template's own vocabulary is present, not the dossier's. A faction
    #    page that grows a .wl-dossier class or a .fac-card has drifted back.
    for banned in ("wl-dossier", "fac-card", "arch-line", "pod-list", "faq2-",
                   "ref2-", "class=\"rail\"", "subnav"):
        if banned in htmlstr:
            errs.append("dossier vocabulary leaked into a site-template page: %s" % banned)
    for need in ('class="ev-hero"', 'class="wrap ev-hero__inner"', 'class="ev-hero__brand"',
                 'class="crumbs"', 'class="meta-chips"', 'class="grid-cards"',
                 'class="card__body"', 'class="related-links"'):
        if need not in htmlstr:
            errs.append("template markup missing: %s" % need)

    # 3. every internal href resolves on disk (this runs BEFORE apply_shell.py
    #    stamps the shared meganav, so it measures only what this file authored)
    for href in sorted(set(re.findall(r'href="(/[^"#?]*)"', htmlstr))):
        if href.startswith(("/css/", "/js/", "/fonts/", "/assets/")):
            continue
        if href in ("/favicon.svg", "/favicon.ico", "/apple-touch-icon.png", "/site.webmanifest"):
            continue
        if href == "/":
            continue
        if not page_exists(href):
            errs.append("broken internal link: %s" % href)

    # 4. JSON-LD parses, and its counts agree with the RENDERED HTML (not with
    #    the data, so a renderer bug cannot hide behind a correct data module)
    html_members = htmlstr.count('<article class="card">')
    html_faq = htmlstr.count("<details><summary>")
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', htmlstr, re.S)
    if not blocks:
        errs.append("no JSON-LD on the page")
    for b in blocks:
        try:
            data = json.loads(b)
        except Exception as e:
            errs.append("invalid JSON-LD: %s" % e)
            continue
        types = {n.get("@type") for n in data.get("@graph", [])}
        for need in ("Organization", "BreadcrumbList", "FAQPage", "WebPage"):
            if need not in types:
                errs.append("JSON-LD graph is missing %s" % need)
        for node in data.get("@graph", []):
            if node.get("@type") == "FAQPage":
                if len(node["mainEntity"]) != html_faq:
                    errs.append("FAQPage has %d questions, the HTML renders %d"
                                % (len(node["mainEntity"]), html_faq))
                for i, q in enumerate(node["mainEntity"]):
                    if q["name"] != f["faq"][i]["q_ld"]:
                        errs.append("FAQPage question %d is out of order" % i)
            if node.get("@type") == "Organization":
                if len(node["member"]) != html_members:
                    errs.append("Organization member[] has %d, the Members grid renders %d"
                                % (len(node["member"]), html_members))
                for i, r in enumerate(node["member"]):
                    nm = r["member"]["name"]
                    if esc(nm) not in htmlstr:
                        errs.append("Organization member %r is not on the page" % nm)
                    if nm != f["members"][i]["name"]:
                        errs.append("Organization member %d is out of order" % i)
    if html_members != len(f["members"]):
        errs.append("Members grid renders %d cards, the data has %d"
                    % (html_members, len(f["members"])))
    if html_faq != len(f["faq"]):
        errs.append("FAQ renders %d items, the data has %d" % (html_faq, len(f["faq"])))

    # 5. FAQ / members / sources shape
    if len(f["faq"]) < 5:
        errs.append("only %d FAQ entries, the template wants 5+" % len(f["faq"]))
    for q in f["faq"]:
        for k in ("q", "a", "q_ld", "a_ld"):
            if not q.get(k):
                errs.append("faq entry missing %s" % k)
    if len(f["sources"]) < 4:
        errs.append("only %d sources, the template wants 4+" % len(f["sources"]))
    for s in f["sources"]:
        if not s["href"].startswith("https://"):
            errs.append("source is not an https URL: %s" % s["href"])
    if len(f["overview"]) < 3:
        errs.append("overview has %d paragraphs, wants 3-4" % len(f["overview"]))
    if not f["members"]:
        errs.append("no members")
    for m in f["members"]:
        for k in ("name", "role", "dates", "note", "ld_role"):
            if not m.get(k):
                errs.append("member %r missing %s" % (m.get("name"), k))

    # 6. dates that are claimed in two places must agree
    for iso, label in ((f["founded_iso"], "founded_iso"), (f["dissolved_iso"], "dissolved_iso")):
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", iso):
            errs.append("%s=%r is not an ISO date" % (label, iso))
    if f["founded_iso"] >= f["dissolved_iso"]:
        errs.append("founded_iso is not before dissolved_iso")

    # 7. prose hygiene
    for k in PROSE_KEYS:
        if f.get(k):
            for bad in _prose_ok(f[k]):
                errs.append("%s contains %s" % (k, bad))
    for i, p in enumerate(f["overview"] + f["legacy"]):
        for bad in _prose_ok(p):
            errs.append("prose paragraph %d contains %s" % (i, bad))

    # 8. double-escaped entities. Passing an entity-bearing field through esc()
    #    turns "&middot;" into "&amp;middot;", which renders as literal text.
    #    This caught the .ev-hero__brand line shipping "ROH &middot; 2003".
    for m in set(re.findall(r"&amp;(?:[a-zA-Z]{2,10}|#\d{1,5});", htmlstr)):
        errs.append("double-escaped entity in output: %s" % m)

    # 9. head requirements
    for need in ('rel="canonical"', 'name="description"', 'content="index,follow',
                 "<title>", '<header class="site-header nav7">'):
        if need not in htmlstr:
            errs.append("head/shell is missing %s" % need)
    return errs


# --------------------------------------------------------------------- driver
def load_all():
    import importlib.util
    out = {}
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "facdata")
    if not os.path.isdir(d):
        raise SystemExit("missing data directory: %s" % d)
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".py") or fn.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(fn[:-3], os.path.join(d, fn))
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        out[m.DATA["slug"]] = m.DATA
    return out


# --------------------------------------------------------------- crawl plumbing
def update_sitemap(slugs):
    """Same shape as build_raf.py's update_sitemap(): append only what is absent."""
    p = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(p):
        print("sitemap: no sitemap.xml at %s" % p)
        return
    xml = open(p, encoding="utf-8").read()
    urls = ["%s/factions/%s/" % (BASE, s) for s in slugs]
    urls.append("%s/factions/" % BASE)
    add = [u for u in urls if "<loc>%s</loc>" % u not in xml]
    if not add:
        print("sitemap: faction urls already present")
        return
    today = TODAY.isoformat()
    blk = "".join('<url><loc>%s</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq>'
                  '<priority>0.7</priority></url>\n' % (u, today) for u in add)
    xml = xml.replace("</urlset>", blk + "</urlset>")
    open(p, "w", encoding="utf-8").write(xml)
    print("sitemap +%d faction urls" % len(add))


def patch_cm_punk(data):
    """Turn the .fac-name headings in the CM Punk dossier's #factions block into links.

    The dossier generator writes that block as plain text. Rather than teach it
    about faction pages, this patches the emitted file in place and is
    idempotent: a heading that is already a link is left alone.
    """
    p = os.path.join(ROOT, "wrestlers", "cm-punk", "index.html")
    if not os.path.exists(p):
        print("cm-punk: no page to patch")
        return
    html = open(p, encoding="utf-8").read()
    by_name = {d["name"]: d["slug"] for d in data.values()}
    n = 0
    for name, slug in by_name.items():
        plain = '<h3 class="fac-name">%s</h3>' % name
        linked = '<h3 class="fac-name"><a href="/factions/%s/">%s</a></h3>' % (slug, name)
        if linked in html:
            continue
        if plain in html:
            html = html.replace(plain, linked, 1)
            n += 1
        else:
            print("  WARN cm-punk: no plain .fac-name heading for %r" % name)
    if n:
        open(p, "w", encoding="utf-8").write(html)
    print("cm-punk: %d faction headings linked (%d already linked)"
          % (n, len(by_name) - n))


# ------------------------------------------------------------------- the hub
# /factions/index.html is a REAL, hand-authored page with eight cards on it.
# This generator inserts into it and never rewrites it. The card below is the
# shape already in that file, copied exactly - four-space indent on <article>,
# six on its children, the media/body split on one line each.
HUB_CARD = ('    <article class="card">\n'
            '      <span class="%s">%s</span>\n'
            '      <a class="card__media" href="/factions/%s/" aria-label="%s">'
            '<span class="card__initials">%s</span></a>\n'
            '      <div class="card__body"><h3 class="card__title">'
            '<a class="card__link" href="/factions/%s/">%s</a></h3>'
            '<p class="card__meta">%s</p></div>\n'
            '    </article>\n')

NUMWORD = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
           "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
           "seventeen", "eighteen", "nineteen", "twenty"]


def _sortkey(title):
    """Alphabetical, ignoring a leading article, so "The Shield" files under S."""
    t = re.sub(r"^the\s+", "", str(title).strip().lower())
    return re.sub(r"[^a-z0-9 ]+", "", t)


def hub_card_for(f):
    name = esc(f["name"])
    # The shipped hub writes its card__meta as "WWE &middot; 2012-2014" - the
    # full years, plain hyphen. Rebuild it from the ISO dates so the new cards
    # read the same way as the eight already on the page.
    promo = promo_label(f)
    y0, y1 = f["founded_iso"][:4], f["dissolved_iso"][:4]
    era = "%s &middot; %s" % (promo, y0 if y0 == y1 else "%s-%s" % (y0, y1))
    return HUB_CARD % (chip_for(promo), esc(promo), f["slug"], name,
                       esc(acronym_for(f["name"])), f["slug"], name, era)


def patch_factions_index(data):
    """Insert the new faction cards into the real /factions/ hub, alphabetically.

    Non-destructive and idempotent:
      * the file is never rewritten from a template - if it is missing, this
        says so and stops, because inventing a hub over a real page is the
        failure mode that loses work;
      * a faction whose /factions/<slug>/ href is already in the file is
        skipped, so a second run adds nothing;
      * the existing <article class="card"> blocks are re-emitted byte-for-byte
        in their existing relative order; only new blocks are interleaved.
    """
    p = os.path.join(ROOT, "factions", "index.html")
    if not os.path.exists(p):
        print("  WARN factions hub: %s does not exist - not creating one" % p)
        return
    html = open(p, encoding="utf-8").read()
    orig = html

    m = re.search(r'<div class="grid-cards">\n(.*?)\n  </div>', html, re.S)
    if not m:
        print("  WARN factions hub: no .grid-cards block to insert into")
        return
    grid = m.group(1)
    blocks = re.findall(r'    <article class="card">\n.*?\n    </article>\n?', grid, re.S)
    if not blocks or "".join(blocks).strip() != grid.strip():
        print("  WARN factions hub: could not account for every card - leaving the hub alone")
        return

    def key_of(block):
        t = re.search(r'<a class="card__link" href="[^"]*">([^<]*)</a>', block)
        return _sortkey(t.group(1) if t else "")

    entries = [[key_of(b), b if b.endswith("\n") else b + "\n"] for b in blocks]
    added = []
    for f in sorted(data.values(), key=lambda x: _sortkey(x["name"])):
        if '/factions/%s/' % f["slug"] in html:
            continue
        card = hub_card_for(f)
        k = _sortkey(f["name"])
        pos = next((i for i, e in enumerate(entries) if e[0] > k), len(entries))
        entries.insert(pos, [k, card])
        added.append(f["slug"])

    if not added:
        print("factions hub: all %d cards already present, nothing inserted" % len(data))
        return

    new_grid = "".join(e[1] for e in entries).rstrip("\n")
    html = html[:m.start(1)] + new_grid + html[m.end(1):]

    # the hub's intro sentence counts the cards; keep it honest
    n = len(entries)
    word = NUMWORD[n] if n < len(NUMWORD) else str(n)
    html = re.sub(r'(These )(\w+)( factions shaped)', lambda mm: mm.group(1) + word + mm.group(3),
                  html, count=1)

    html = _sync_hub_itemlist(html, entries)

    if html != orig:
        open(p, "w", encoding="utf-8").write(html)
    print("factions hub: inserted %d cards (%s); %d cards on the page"
          % (len(added), ", ".join(added), n))


def _sync_hub_itemlist(html, entries):
    """Keep the hub's ItemList JSON-LD 1:1 with the cards actually on the page.

    Surgical on purpose: only the ItemList node is rebuilt, in the hand-authored
    block's own layout, so the diff is the three new entries and the count and
    nothing else. Every object still goes through json.dumps - none of it is
    hand-written - and the whole block is re-parsed afterwards, with the edit
    thrown away if it would not parse. Idempotent: a second run is a no-op.
    """
    m = re.search(r'(<script type="application/ld\+json">)(.*?)(</script>)', html, re.S)
    if not m:
        return html
    block = m.group(2)
    try:
        doc = json.loads(block)
    except Exception as e:
        print("  WARN factions hub: ItemList JSON-LD does not parse (%s) - left alone" % e)
        return html
    node = next((n for n in doc.get("@graph", []) if n.get("@type") == "ItemList"), None)
    if node is None:
        return html

    items = []
    for i, (_k, card) in enumerate(entries, 1):
        a = re.search(r'<a class="card__link" href="(/factions/[^"]*)">([^<]*)</a>', card)
        if not a:
            print("  WARN factions hub: a card has no card__link - ItemList left alone")
            return html
        items.append({"@type": "ListItem", "position": i,
                      "name": _html.unescape(a.group(2)), "url": BASE + a.group(1)})

    head = {k: v for k, v in node.items() if k not in ("numberOfItems", "itemListElement")}
    head["numberOfItems"] = len(items)
    rebuilt = (json.dumps(head, ensure_ascii=False, separators=(",", ":"))[:-1] +
               ',"itemListElement":[\n' +
               ",\n".join("      " + json.dumps(it, ensure_ascii=False, separators=(",", ":"))
                          for it in items) +
               "\n    ]}")

    old = re.search(r'\{"@type":"ItemList".*?\]\}', block, re.S)
    if not old:
        print("  WARN factions hub: could not locate the ItemList node text - left alone")
        return html
    new_block = block[:old.start()] + rebuilt + block[old.end():]
    try:
        if json.loads(new_block) != json.loads(json.dumps(
                {**doc, "@graph": [dict(n, **({"numberOfItems": len(items),
                                               "itemListElement": items}
                                              if n.get("@type") == "ItemList" else {}))
                                   for n in doc["@graph"]]})):
            print("  WARN factions hub: rebuilt ItemList is not equivalent - left alone")
            return html
    except Exception as e:
        print("  WARN factions hub: rebuilt JSON-LD would not parse (%s) - left alone" % e)
        return html
    return html[:m.start(2)] + new_block + html[m.end(2):]


def build_pass(data, want, quiet=False):
    """One generation pass. Returns the slugs that verified and were written."""
    written = []
    for slug in want:
        if slug not in data:
            print("  no data module for %s" % slug)
            continue
        f = data[slug]
        del LINK_LOG[:]
        h = page(f)
        errs = verify(f, h)
        if errs:
            print("  %-26s FAILED" % slug)
            for e in errs:
                print("      - %s" % e)
            continue
        p = os.path.join(ROOT, "factions", slug, "index.html")
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, "w", encoding="utf-8").write(h)
        written.append(slug)
        if quiet:
            continue
        secs = sections_for(f)
        linked = sum(1 for r in LINK_LOG if r[3] == "linked")
        plain = sum(1 for r in LINK_LOG if r[3] in ("missing", "no-slug"))
        print("  %-26s %6.0f KB  %d sections  %2d members  %2d timeline rows  "
              "links: %d resolved / %d plain"
              % (slug, len(h) / 1024, len(secs), len(f["members"]), len(f["timeline"]),
                 linked, plain))
        for kind, s, label, state in LINK_LOG:
            if state == "linked" and kind in ("wrestlers", "matches"):
                print("      linked -> /%s/%s/  (%s)" % (kind, s, label))
        for kind, s, label, state in LINK_LOG:
            if state == "missing":
                path = s if kind == "explore" else "/%s/%s/" % (kind, s)
                print("      plain text (no %s on disk): %s" % (path, label))
    return written


def main(argv):
    data = load_all()
    want = argv or sorted(data)

    # Two passes. Faction pages cross-link to each other, and href_for() only
    # links what is already on disk, so a single pass would leave the first
    # page's sibling links as plain text purely because of build order. The
    # first pass is silent; the reported numbers come from the settled second.
    if len(want) > 1:
        build_pass(data, want, quiet=True)
    written = build_pass(data, want)

    if written:
        update_sitemap(written)
        patch_cm_punk({k: v for k, v in data.items() if k in written})
        patch_factions_index({k: v for k, v in data.items() if k in written})
    print("done: %d faction pages  ROOT=%s" % (len(written), ROOT))
    print("now run: WL_ROOT=\"$PWD\" python3 build/apply_shell.py")
    return 0 if len(written) == len(want) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
