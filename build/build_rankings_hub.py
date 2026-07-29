#!/usr/bin/env python3
"""Rebuild /rankings/ into the Wrestle Lore Rankings HUB: a directory of ranked lists.
Flagship = the greatest matches ranked 1..N (data/matches.json `rank`, a real ordering).
Plus a directory of the other ranking categories (rivalries, events, promotions, wrestlers,
moments). Seeds the shell from the existing /rankings/index.html, swaps <main>, refreshes
head + schema. Run apply_shell.py after for the cache-bust stamp.
"""
import os, re, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(ROOT, "rankings", "index.html")
DATA = os.path.join(ROOT, "data", "matches.json")
BASE = "https://wrestlelore.com"
PAGE_URL = BASE + "/rankings/"

def esc(s): return html.escape(s or "", quote=True)
CHIPCLS = {"WWE":"chip--wwe","WWF":"chip--wwe","WCW":"chip--wcw","TNA":"chip--tna","NXT":"chip--nxt","ROH":"chip--roh","ECW":"chip--ecw"}

def stars_row(rating):
    return ('<span class="rating" style="--rating:%s"><span class="rating__stars" aria-hidden="true">'
            '&starf;&starf;&starf;&starf;&starf;</span></span>' % rating)

def ranked_row(m, i):
    cls = ("chip %s" % CHIPCLS.get(m.get("promotion") or "", "")).strip()
    ev = " · ".join([x for x in [m.get("event"), str(m.get("year") or "")] if x])
    med = " rkh-row--top" if i <= 3 else ""
    return (
      '<li class="rkh-row%s">'
      '<span class="rkh-no">%d</span>'
      '<span class="rkh-body">'
        '<a class="rkh-nm" href="/matches/%s/">%s</a>'
        '<span class="rkh-meta"><span class="%s">%s</span><span class="rkh-ev">%s</span></span>'
      '</span>'
      '<span class="rkh-rt">%s<b class="rkh-sc">%s</b></span>'
      '</li>'
      % (med, i, m["slug"], esc(m["title"]), cls, esc(m.get("promotion") or ""), esc(ev),
         stars_row(m["rating"]), ("%.1f" % m["rating"])))

# Directory of the other ranking categories (link to the live section indexes).
CATS = [
  ("Rivalries", "/rivalries/", "The feuds that defined eras, from Bret vs Austin to Punk vs Cena.",
   '<path d="M13 2 3 14h7l-1 8 10-12h-7z"/>'),
  ("Events", "/events/", "The greatest cards in history, across WWE, WCW, ECW, AEW and more.",
   '<path d="M3 9h18M3 9V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>'),
  ("Promotions", "/promotions/", "How the companies stack up, from WWE and WCW to NJPW and AEW.",
   '<path d="M3 21h18M5 21V7l7-4 7 4v14M9 21v-6h6v6"/>'),
  ("Wrestlers", "/wrestlers/", "The performers behind the classics, with full records and dossiers.",
   '<circle cx="12" cy="7" r="4"/><path d="M4 21v-2a6 6 0 0 1 16 0v2"/>'),
  ("Moments", "/moments/", "The single instants that changed the course of wrestling.",
   '<path d="M12 2v6m0 8v6m10-10h-6M8 12H2"/>'),
]
def cat_card(name, href, desc, icon):
    return ('<a class="rkh-cat" href="%s">'
            '<svg class="rkh-cat__ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true">%s</svg>'
            '<span class="rkh-cat__h">%s</span><span class="rkh-cat__d">%s</span>'
            '<span class="rkh-cat__go">Explore</span></a>' % (href, icon, esc(name), esc(desc)))

def build_main(data):
    ranked = sorted(data, key=lambda m: m["rank"])
    rows = "\n".join(ranked_row(m, m["rank"]) for m in ranked)
    top = ranked[0]
    n = len(data)
    n5 = sum(1 for m in data if m["tier"] == "five-star")
    cats = "".join(cat_card(*c) for c in CATS)

    hero = (
      '<div class="wrap">'
      '<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li>Rankings</li></ol></nav>'
      '</div>'
      '<section class="section--tight"><div class="wrap">'
      '<span class="eyebrow">The Rankings</span>'
      '<h1 style="font-family:var(--font-cond);text-transform:uppercase">The Wrestle Lore Rankings</h1>'
      '<p class="answer" style="margin-top:var(--sp-4)"><strong>Every ranking on Wrestle Lore, in one place.</strong> '
      'The greatest matches ranked one through %d, scored against Dave Meltzer&rsquo;s <em>Wrestling Observer</em> stars and the Cagematch community score, then weighed for how much each still matters. '
      'Rivalries, events, promotions, wrestlers and moments follow. Prefer to browse and watch instead of rank? The full, spoiler-safe <a href="/matches/">match archive lives here</a>.</p>'
      '</div></section>'
    ) % n

    matches = (
      '<section class="section"><div class="wrap">'
      '<div class="section-head"><h2>The Greatest Matches, Ranked</h2><a class="btn btn--ghost" href="/matches/">Browse &amp; watch all</a></div>'
      '<p class="muted" style="margin-top:calc(var(--sp-3)*-1)">Our number one is <a href="/matches/%s/">%s</a>. %d of these %d earn a perfect five stars. Ratings blend Meltzer, Cagematch and historical weight; open any match for the full breakdown and the video where it exists.</p>'
      '<ol class="rkh-list">%s</ol>'
      '</div></section>' % (top["slug"], esc(top["title"]), n5, n, rows)
    )

    directory = (
      '<section class="section" style="background:var(--c-bg-elev-1);border-block:1px solid var(--c-line)"><div class="wrap">'
      '<div class="section-head"><h2>More Rankings</h2></div>'
      '<p class="muted" style="margin-top:calc(var(--sp-3)*-1)">The match rankings are live now. These collections are ranked and expanded on an ongoing basis.</p>'
      '<div class="rkh-cats">%s</div>'
      '</div></section>' % cats
    )

    faq = (
      '<section class="section"><div class="wrap wrap--narrow"><div class="section-head"><h2>Frequently Asked</h2></div><div class="faq">'
      '<details open><summary>What is the greatest wrestling match of all time?</summary><div class="faq__body">Wrestle Lore ranks <a href="/matches/%s/">%s</a> its number one, a full five stars and regularly voted the greatest WrestleMania match ever. Ranks are set by Meltzer&rsquo;s <em>Wrestling Observer</em> stars, the Cagematch community score, and lasting importance.</div></details>'
      '<details><summary>How does Wrestle Lore rank matches?</summary><div class="faq__body">Each match carries a Wrestle Lore star rating that blends Dave Meltzer&rsquo;s stars, the Cagematch community score, and how much the match still matters. The ordering here reflects that combined score. <a href="/methodology/">See the full method</a>.</div></details>'
      '<details><summary>What else does Wrestle Lore rank?</summary><div class="faq__body">Beyond matches, Wrestle Lore covers <a href="/rivalries/">rivalries</a>, <a href="/events/">events</a>, <a href="/promotions/">promotions</a>, <a href="/wrestlers/">wrestlers</a> and <a href="/moments/">defining moments</a>. Ranked lists across those categories are added over time.</div></details>'
      '<details><summary>Where can I watch the ranked matches?</summary><div class="faq__body">Most of the top matches play right here in a spoiler-safe theater, embedded from official promotion channels, on the <a href="/matches/">match archive</a>. Wrestle Lore hosts no footage and never embeds unofficial re-uploads.</div></details>'
      '</div></div></section>' % (top["slug"], esc(top["title"]))
    )

    return '<main id="main">\n' + hero + matches + directory + faq + '\n</main>'

def build_schema(data):
    ranked = sorted(data, key=lambda m: m["rank"])
    items = ",".join('{"@type":"ListItem","position":%d,"url":"%s/matches/%s/","name":%s}'
                     % (m["rank"], BASE, m["slug"], json.dumps(m["title"])) for m in ranked)
    website = ('<script type="application/ld+json">'
      '{"@context":"https://schema.org","@type":"WebSite","name":"Wrestle Lore","url":"%s/"}</script>' % BASE)
    collection = ('<script type="application/ld+json">'
      '{"@context":"https://schema.org","@type":"CollectionPage","name":%s,"url":"%s","description":%s,'
      '"isPartOf":{"@type":"WebSite","name":"Wrestle Lore","url":"%s/"},'
      '"about":{"@type":"Thing","name":"Professional wrestling rankings"},'
      '"mainEntity":{"@type":"ItemList","name":"The Greatest Wrestling Matches, Ranked","numberOfItems":%d,"itemListOrder":"https://schema.org/ItemListOrderDescending"}}</script>'
      % (json.dumps("The Wrestle Lore Rankings"), PAGE_URL,
         json.dumps("Every Wrestle Lore ranking in one place: the greatest pro wrestling matches ranked, plus rivalries, events, promotions, wrestlers and moments."),
         BASE, len(data)))
    itemlist = ('<script type="application/ld+json">'
      '{"@context":"https://schema.org","@type":"ItemList","name":"The Greatest Wrestling Matches, Ranked",'
      '"description":"Pro wrestling matches ranked by Wrestle Lore, blending Meltzer and Cagematch consensus with historical weight.",'
      '"numberOfItems":%d,"itemListOrder":"https://schema.org/ItemListOrderDescending","itemListElement":[%s]}</script>'
      % (len(data), items))
    top = ranked[0]
    faq = ('<script type="application/ld+json">'
      '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
      '{"@type":"Question","name":"What is the greatest wrestling match of all time?","acceptedAnswer":{"@type":"Answer","text":%s}},'
      '{"@type":"Question","name":"How does Wrestle Lore rank matches?","acceptedAnswer":{"@type":"Answer","text":"Each match carries a Wrestle Lore star rating blending Dave Meltzer\'s Wrestling Observer stars, the Cagematch community score, and lasting importance. The ranking order reflects that combined score."}},'
      '{"@type":"Question","name":"What else does Wrestle Lore rank?","acceptedAnswer":{"@type":"Answer","text":"Beyond matches, Wrestle Lore covers rivalries, events, promotions, wrestlers and defining moments, with ranked lists across those categories added over time."}},'
      '{"@type":"Question","name":"Where can I watch the ranked matches?","acceptedAnswer":{"@type":"Answer","text":"Most top matches play in a spoiler-safe theater on the match archive, embedded from official promotion channels. Wrestle Lore hosts no footage and never embeds unofficial re-uploads."}}'
      ']}</script>'
      % json.dumps("Wrestle Lore ranks %s its number one, a full five stars and regularly voted the greatest WrestleMania match ever. Ranks are set by Meltzer stars, the Cagematch community score, and lasting importance." % top["title"]))
    breadcrumb = ('<script type="application/ld+json">'
      '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
      '{"@type":"ListItem","position":1,"name":"Home","item":"%s/"},'
      '{"@type":"ListItem","position":2,"name":"Rankings","item":"%s"}]}</script>' % (BASE, PAGE_URL))
    return website + "\n" + collection + "\n" + itemlist + "\n" + faq + "\n" + breadcrumb

def main():
    data = json.load(open(DATA, encoding="utf-8"))
    page = open(SRC, encoding="utf-8").read()

    page = re.sub(r"<main id=\"main\">.*?</main>", lambda _: build_main(data), page, count=1, flags=re.S)

    # strip existing hub-level schema then inject fresh (idempotent)
    page = re.sub(
        r'<script type="application/ld\+json">(?:(?!</script>).)*?'
        r'(?:"FAQPage"|"ItemList"|"BreadcrumbList"|"CollectionPage"|"WebSite")'
        r'(?:(?!</script>).)*?</script>\s*', "", page, flags=re.S)
    page = page.replace("</head>", build_schema(data) + "\n</head>", 1)

    TITLE = "Wrestling Rankings, The Greatest Matches Ranked | WWE, WCW, ECW, TNA, ROH, NXT | Wrestle Lore"
    DESC = ("The Wrestle Lore rankings hub: the greatest pro wrestling matches ranked one through %d by Meltzer and "
            "Cagematch consensus, plus ranked rivalries, events, promotions, wrestlers and moments across WWE, WCW, "
            "ECW, TNA, ROH and NXT." % len(data))
    KW = ("wrestling rankings, best wrestling matches ranked, greatest wrestling matches of all time, wrestling tier list, "
          "top wrestling rivalries, best wrestling events, WWE rankings, WCW, ECW, TNA, ROH, NXT, Meltzer ratings, Cagematch")
    page = re.sub(r'<title>[^<]*</title>', lambda _: '<title>%s</title>' % TITLE, page, count=1)
    page = re.sub(r'<meta name="description" content="[^"]*">', lambda _: '<meta name="description" content="%s">' % DESC, page, count=1)
    if 'name="keywords"' not in page:
        page = re.sub(r'(<meta name="description"[^>]*>)', lambda m: m.group(1) + '<meta name="keywords" content="%s">' % KW, page, count=1)
    page = re.sub(r'(<meta property="og:title" content=")[^"]*(">)', lambda m: m.group(1) + TITLE + m.group(2), page)
    page = re.sub(r'(<meta name="twitter:title" content=")[^"]*(">)', lambda m: m.group(1) + TITLE + m.group(2), page)
    page = re.sub(r'(<meta property="og:description" content=")[^"]*(">)', lambda m: m.group(1) + DESC + m.group(2), page)
    page = re.sub(r'(<meta name="twitter:description" content=")[^"]*(">)', lambda m: m.group(1) + DESC + m.group(2), page)

    # writing-style sweep (no em dashes as separators, no decorative arrows)
    for a, b in ((" &mdash; ", ", "), ("&mdash;", ", "), (" — ", ", "), ("—", ", "),
                 (" &rarr;", ""), ("&rarr;", ""), (" →", ""), ("→", ""), ("➜", ""), ("↗", "")):
        page = page.replace(a, b)

    open(SRC, "w", encoding="utf-8").write(page)
    print("wrote", SRC, "(%d bytes)" % len(page), "| ranked:", len(data))

if __name__ == "__main__":
    main()
