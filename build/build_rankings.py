#!/usr/bin/env python3
"""Rebuild /rankings/ into the Five-Star Club spoiler-reveal card hub.
Source of truth: data/matches.json. Reuses the .yt facade + media.js theater modal.
Swaps <main> in the existing page (keeps stamped shell/head), injects ItemList+FAQ schema,
loads media.js + rankings.js. Writes to OUT_ROOT. Run apply_shell.py after for cache-bust.
"""
import os, re, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_PAGE = os.path.join(ROOT, "rankings", "index.html")
DATA     = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "matches.json")
OUT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE     = "https://wrestlelore.com"

def esc(s): return html.escape(s or "", quote=True)

CHIPCLS = {"WWE":"chip--wwe","WWF":"chip--wwe","WCW":"chip--wcw","TNA":"chip--tna","NXT":"chip--nxt"}
POSTER_PC = {"WWE":"#7a1f24","WWF":"#7a1f24","WCW":"#243b6b","TNA":"#4a2668","NXT":"#6b5a12","ROH":"#5a1f1f","ECW":"#611a1a"}
# The program's official streaming home (verified 2026-07-28). Used for the watch-full-match link-out.
WWE_STREAM = ("Peacock", "https://www.peacocktv.com/sports/wwe")
STREAM = {"WWE":WWE_STREAM,"WWF":WWE_STREAM,"WCW":WWE_STREAM,"ECW":WWE_STREAM,"NXT":WWE_STREAM,
          "TNA":("TNA+","https://watch.tnawrestling.com/"), "ROH":("HonorClub","https://www.ringofhonor.com/")}
def stream_of(m): return STREAM.get(m.get("promotion") or "", (None, None))
CH_SHORT = {"Ring of Honor Wrestling": "ROH", "TNA Wrestling": "TNA", "WWE": "WWE"}

def rate_class(r):
    return "rank-rate--half" if r == 4.5 else ("rank-rate--four" if r <= 4 else "")

def stars_row(rating):
    return ('<span class="rating" style="--rating:%s"><span class="rating__stars" aria-hidden="true">'
            '&starf;&starf;&starf;&starf;&starf;</span></span>' % rating)

def yt_facade(m):
    v = m["video"]; slug = m["slug"]
    label = ", ".join(x for x in [m["title"], m.get("event") or ""] if x)
    svc, url = stream_of(m)
    svc_attr = (' data-yt-service="%s" data-yt-service-url="%s"' % (esc(svc), esc(url))) if svc else ""
    return ('<div class="yt" data-yt-id="%s" data-yt-title="%s" data-yt-creator="%s" data-yt-page="/matches/%s/"%s>'
            '<a class="yt__link" href="/matches/%s/">Play: %s (official %s upload)</a></div>'
            % (esc(v["id"]), esc(label), esc(v["channel"]), slug, svc_attr, slug, esc(m["title"]), esc(v["channel"])))

def poster(m):
    pc = POSTER_PC.get(m.get("promotion") or "", "#3a3f4a")
    mono = esc((m["title"] or "").replace(" vs ", " ✕ "))
    k = "%s · %s" % (esc(m.get("promotion") or ""), m.get("year") or "")
    return ('<a class="rank-poster" style="--pc:%s" href="/matches/%s/" aria-label="Open %s match page">'
            '<span class="rank-poster__k">%s</span><span class="rank-poster__mono">%s</span>'
            '<span class="rank-poster__watch">Open the breakdown</span></a>'
            % (pc, m["slug"], esc(m["title"]), k, mono))

def spoiler(m):
    # Winner + one-line result are REAL text (crawlable); CSS blurs until reveal.
    if m["winner"]:
        winner = esc(m["winner"])
        # trim "X def. Y ..." down to the consequence for the sub-line
        result = esc(m["result"] or "")
        sub = '<span class="spoiler__result">%s</span>' % result if result else ""
        inner = '<span class="spoiler__winner">%s</span>%s' % (winner, sub)
        cue = 'Reveal <b>winner</b>'
    else:
        # draws / angles (no single winner) — reveal the outcome
        inner = '<span class="spoiler__winner">%s</span>' % esc(m["result"] or "See result")
        cue = 'Reveal <b>result</b>'
    eye = ('<svg class="eye" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
           'aria-hidden="true"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/></svg>')
    return ('<div class="spoiler">'
            '<span class="spoiler__label">%s Who won?</span>'
            '<span class="spoiler__value">%s</span>'
            '<button class="spoiler__btn" type="button" aria-expanded="false" '
            'aria-label="Reveal the winner of %s">%s<span class="cue">%s</span></button>'
            '</div>'
            % ('<svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor" aria-hidden="true"><path d="M12 2 3 7v6c0 5 3.8 8.5 9 9 5.2-.5 9-4 9-9V7z"/></svg>',
               inner, esc(m["title"]), eye, cue))

def card(m, variant=""):
    v = m["video"]
    five = "rank-card--five" if m["tier"] == "five-star" else ""
    sm = "rank-card--sm" if variant == "sm" else ""
    cls = ("chip %s" % CHIPCLS.get(m.get("promotion") or "", "")).strip()
    media = yt_facade(m) if v["id"] else poster(m)
    ev = " · ".join([x for x in [m.get("event"), str(m.get("year") or "")] if x])
    src_bits = []
    if m.get("meltzer"): src_bits.append("Meltzer %s" % re.sub(r"\s*\(.*?\)", "", m["meltzer"]).replace("&starf;","").strip() or m["meltzer"])
    # simpler: use raw meltzer/cagematch numbers
    meltz = (m.get("meltzer") or "")
    cm = (m.get("cagematch") or "")
    src = " · ".join([x for x in [("Meltzer "+meltz) if meltz else "", ("Cagematch "+cm) if cm else ""] if x])
    svc, url = stream_of(m)
    if v["id"]:
        vt = "Full event" if v["type"] == "event" else ("Highlights" if v["type"] == "highlights" else "Full match")
        foot_right = ('<span class="rank-badge-vid"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
                      '<path d="M8 5v14l11-7z"/></svg>%s · %s</span>' % (vt, esc(CH_SHORT.get(v["channel"], v["channel"]))))
    elif svc:
        foot_right = ('<a class="rank-stream" href="%s" target="_blank" rel="noopener">Watch on %s</a>' % (esc(url), esc(svc)))
    else:
        foot_right = ""
    rr = rate_class(m["rating"])
    return (
      '<article class="rank-card %s %s" data-promo="%s" data-rating="%s" data-year="%s" data-name="%s">'
        % (five, sm, esc(m.get("promotion") or ""), m["rating"], m.get("year") or 0, esc(m["title"])) +
      '<span class="rank-rate %s">%s<small>&starf;</small></span>' % (rr, ("%.1f" % m["rating"]).rstrip("0").rstrip(".") if m["rating"] % 1 else "%.0f" % m["rating"]) +
      '<div class="rank-card__media">%s</div>' % media +
      '<div class="rank-card__body">' +
        '<div class="rank-card__meta"><span class="%s">%s</span>' % (cls, esc(m.get("promotion") or "")) +
        ('<span class="rank-era">%s</span>' % esc(re.sub(r"\s*/.*","",m["era"])) if m.get("era") else "") + '</div>' +
        '<h3 class="rank-card__title"><a href="/matches/%s/">%s</a></h3>' % (m["slug"], esc(m["title"])) +
        '<p class="rank-card__event">%s</p>' % esc(ev) +
        '<div class="rank-card__rating">%s<span class="rank-score">%s</span></div>' % (stars_row(m["rating"]), ("%.1f" % m["rating"])) +
        ('<p class="rank-src">%s</p>' % esc(src) if src else "") +
        spoiler(m) +
        '<div class="rank-card__foot"><a class="rank-go" href="/matches/%s/">Full breakdown</a>%s</div>' % (m["slug"], foot_right) +
      '</div>' +
      '</article>'
    )

def grid(matches, variant="", cls="rank-grid"):
    return '<div class="%s">%s</div>' % (cls, "\n".join(card(m, variant) for m in matches))

# ---------------- rotating hero spotlight ----------------
def hero_slide(m, idx, total):
    v = m["video"]
    if v["id"]:
        bg = "background-image:url(https://i.ytimg.com/vi/%s/hqdefault.jpg)" % v["id"]
    else:
        pc = POSTER_PC.get(m.get("promotion") or "", "#2a2f3a")
        bg = "background:radial-gradient(130%% 130%% at 72%% 8%%,%s 0%%,#0a0b0d 62%%)" % pc
    watch = ('<button class="rhero__watch" type="button" data-yt="%s"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>Watch the match</button>' % esc(v["id"])) if v["id"] else ""
    cls = ("chip %s" % CHIPCLS.get(m.get("promotion") or "", "")).strip()
    ev = " · ".join([x for x in [m.get("event"), str(m.get("year") or ""), (m.get("venue") or "").split(",")[0]] if x])
    era = ('<span class="rank-era">%s</span>' % esc(re.sub(r"\s*/.*", "", m["era"]))) if m.get("era") else ""
    eye = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/></svg>'
    return (
      '<li class="rhero__slide%s" role="group" aria-roledescription="slide" aria-label="%d of %d: %s">'
      '<div class="rhero__bg" style="%s"></div><div class="rhero__scrim"></div>'
      '<div class="rhero__content">'
        '<div class="rhero__badges"><span class="rhero__rank">5&#9733;</span><span class="rhero__tag">Five-Star Club</span>'
        '<span class="%s">%s</span>%s</div>'
        '<h2 class="rhero__title"><a href="/matches/%s/">%s</a></h2>'
        '<p class="rhero__meta">%s</p>'
        '<div class="rhero__rating">%s<span class="rank-score">%.1f</span><span class="rank-src">%s</span></div>'
        '<p class="rhero__hook">%s</p>'
        '<div class="rhero__cta">%s<a class="rhero__break" href="/matches/%s/">Full breakdown</a>'
        '<span class="rhero__safe">%sWinner hidden until you reveal it</span></div>'
      '</div></li>'
      % (" is-active" if idx == 0 else "", idx + 1, total, esc(m["title"]), bg,
         cls, esc(m.get("promotion") or ""), era,
         m["slug"], esc(m["title"]), esc(ev),
         stars_row(m["rating"]), m["rating"], esc(m.get("meltzer") or ""),
         esc(m.get("hook") or ""), watch, m["slug"], eye))

def rail_item(m, idx):
    ev = " · ".join([x for x in [m.get("event"), str(m.get("year") or "")] if x])
    return (
      '<li><button class="rrail%s" type="button" data-i="%d" aria-label="Show %s">'
      '<span class="rrail__no">&#9733;</span>'
      '<span class="rrail__body"><span class="rrail__nm">%s</span><span class="rrail__meta">%s</span></span>'
      '<span class="rrail__sc">%.1f</span></button></li>'
      % (" is-on" if idx == 0 else "", idx, esc(m["title"]), esc(m["title"]), esc(ev), m["rating"]))

def rate_card():
    return (
      '<a class="rhero__rate" href="/methodology/">'
      '<span class="rhero__rateh"><b>How we rate</b><span>5.0 max</span></span>'
      '<p>A five-star score that weighs Dave Meltzer&rsquo;s Wrestling Observer stars, the Cagematch community score, and how much the match still matters.</p>'
      '<span class="go">Read the method</span></a>')

def build_hero(data):
    spot = [m for m in data if m["tier"] == "five-star"][:6]
    n = len(spot)
    slides = "\n".join(hero_slide(m, i, n) for i, m in enumerate(spot))
    rail = "".join(rail_item(m, i) for i, m in enumerate(spot))
    return (
      '<section class="rank-hero" aria-label="Five-star match spotlight">'
      '<div class="rhero__main"><ul class="rhero__stage" aria-live="polite">%s</ul></div>'
      '<aside class="rhero__side">'
        '<div class="rhero__railhead"><span class="rhero__railttl">Five-star spotlight</span>'
        '<button class="rhero__pause" type="button" aria-label="Pause the rotation">&#10074;&#10074;</button></div>'
        '<ol class="rhero__rail">%s</ol>'
        '%s'
      '</aside>'
      '</section>' % (slides, rail, rate_card()))

def build_stats(data):
    five = sum(1 for m in data if m["tier"] == "five-star")
    vids = sum(1 for m in data if m["video"]["id"])
    promos = len(set(m["promotion"] for m in data if m["promotion"]))
    yrs = [m["year"] for m in data if m["year"]]
    span = "%d&ndash;%d" % (min(yrs), max(yrs))
    stats = [("%d" % five, "Perfect 5&#9733;"), ("%d" % len(data), "Ranked matches"),
             ("%d" % promos, "Promotions"), (span, "Era span"), ("%d" % vids, "Watchable now")]
    cells = "".join('<div class="rank-stat"><b>%s</b><span>%s</span></div>' % (a, b) for a, b in stats)
    return '<div class="rank-stats">%s</div>' % cells

def build_explorer(data):
    order = ["WWE", "WWF", "WCW", "ECW", "TNA", "NXT", "ROH", "AEW", "NJPW"]
    present = [p for p in order if any(m["promotion"] == p for m in data)]
    promo_chips = '<button class="rfil is-on" type="button" data-f="ALL">All</button>' + \
        "".join('<button class="rfil" type="button" data-f="%s">%s</button>' % (p, p) for p in present)
    rating_seg = ('<div class="rex-seg" data-ctl="rate" role="group" aria-label="Filter by rating">'
        '<button class="is-on" type="button" data-rate="ALL">All</button>'
        '<button type="button" data-rate="5">5&#9733;</button>'
        '<button type="button" data-rate="4.5">4&frac12;&#9733;</button>'
        '<button type="button" data-rate="4">4&#9733;</button></div>')
    sort_seg = ('<div class="rex-seg" data-ctl="sort" role="group" aria-label="Sort matches">'
        '<button class="is-on" type="button" data-sort="rating">Rating</button>'
        '<button type="button" data-sort="year-desc">Newest</button>'
        '<button type="button" data-sort="year-asc">Oldest</button>'
        '<button type="button" data-sort="name">A&ndash;Z</button></div>')
    controls = ('<div class="rex-controls">'
        '<div class="rex-group"><span class="rex-lbl">Rating</span>%s</div>'
        '<div class="rex-group"><span class="rex-lbl">Sort</span>%s</div>'
        '<span class="rex-spacer"></span><span class="rex-count"></span></div>'
        '<div class="rex-promos"><span class="rex-lbl">Promotion</span>%s</div>' % (rating_seg, sort_seg, promo_chips))
    cards_html = "\n".join(card(m) for m in data)
    return ('<div class="rank-explorer">%s<div class="rex-grid">%s</div>'
            '<p class="rex-empty" hidden>No matches for this filter.</p>'
            '<nav class="rex-pager" aria-label="Match pages"></nav></div>' % (controls, cards_html))

# ---------------- assemble body ----------------
def numword(n):
    w = {1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",
         10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen"}
    return w.get(n, str(n))

def build_body(data):
    five = [m for m in data if m["tier"] == "five-star"]
    near = [m for m in data if m["tier"] == "near-miss"]
    arch = [m for m in data if m["tier"] == "classic"]
    n_vid = sum(1 for m in data if m["video"]["id"])
    n5 = numword(len(five))

    disclose = ('<p class="rank-disclose">%d of these matches play right here in a spoiler-safe theater, embedded from <strong>official channels only</strong> (WWE and TNA Wrestling) through YouTube&rsquo;s privacy-enhanced player. Wrestle Lore hosts no footage. Each clip opens on <a href="https://www.youtube.com/@WWE" target="_blank" rel="noopener">YouTube</a> in a new tab, and the rights stay with the promotions.</p>' % n_vid)
    hero = (
      '<div class="wrap">'
      '<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li>Rankings</li></ol></nav>'
      '</div>'
      '<section class="section--tight"><div class="wrap">'
      '<span class="eyebrow">The Five-Star Club &middot; The Hub</span>'
      '<h1 style="font-family:var(--font-cond);text-transform:uppercase">The Wrestle Lore Five-Star Club</h1>'
      + build_hero(data)
      + '<p class="answer" style="margin-top:var(--sp-5)"><strong>The highest-rated pro wrestling matches of the modern era, in one place.</strong> ' + n5 + ' earn a perfect five stars. Alongside them sit the 4&frac12;&#9733; near misses and the rest of the rated archive. Every match links to its full breakdown, and <strong>every winner stays hidden until you reveal it</strong>, so you can browse without spoiling the matches you have not seen yet. '
      'The catalog spans <a href="/matches/undertaker-vs-hbk-wm25/">WWE, WCW, ECW, TNA, ROH and NXT</a>, scored against Meltzer and Cagematch consensus.</p>'
      '<div class="rank-controls">'
        '<span class="rank-controls__lede"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/></svg>Winners stay hidden until you reveal them.</span>'
        '<button class="reveal-all" type="button" aria-pressed="false"><svg class="reveal-all__eye" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/></svg><span class="reveal-all__txt">Reveal all winners</span></button>'
      '</div>'
      + disclose +
      '</div></section>'
    )

    explorer = (
      '<section class="section"><div class="wrap">'
      '<div class="section-head"><h2>Every rated match</h2><a class="btn btn--ghost" href="/matches/">All matches</a></div>'
      '<p class="muted" style="margin-top:calc(var(--sp-3)*-1)">Filter by star rating or promotion, sort by date or name, and page through the catalog. The star score is the rating. Nothing here is ranked best to worst: a five-star match is a five-star match, whether it lands on page one or page three. Reveal the winner on any card, or reveal the whole board at once.</p>'
      + build_explorer(data) +
      '</div></section>'
    )

    streak = (
      '<section class="section" style="background:var(--c-bg-elev-1);border-block:1px solid var(--c-line)"><div class="wrap wrap--narrow">'
      '<span class="eyebrow">Context</span><h2 style="font-family:var(--font-cond);text-transform:uppercase">The WrestleMania Streak</h2>'
      '<p class="muted" style="margin-top:var(--sp-3)">No storyline shapes this catalog more than <strong>The Undertaker&rsquo;s WrestleMania Streak</strong>. From 1991 onward, <a href="/wrestlers/the-undertaker/">The Undertaker</a> won every WrestleMania match he wrestled. His record reached <strong>21&ndash;0</strong> before <a href="/wrestlers/brock-lesnar/">Brock Lesnar</a> ended it at 21&ndash;1 at WrestleMania XXX in 2014. Several club and near-miss entries are Streak defences: the two with <a href="/wrestlers/shawn-michaels/">Shawn Michaels</a> at <a href="/matches/undertaker-vs-hbk-wm25/">WrestleMania XXV</a> and <a href="/matches/undertaker-vs-hbk-wm26-2010/">XXVI</a>, and the &ldquo;End of an Era&rdquo; Hell in a Cell with <a href="/wrestlers/triple-h/">Triple H</a> at <a href="/matches/undertaker-vs-triple-h-wm28-2012/">WrestleMania XXVIII</a>.</p>'
      '</div></section>'
    )

    faq = (
      '<section class="section"><div class="wrap wrap--narrow"><div class="section-head"><h2>Frequently Asked</h2></div><div class="faq">'
      '<details open><summary>What is the Wrestle Lore Five-Star Club?</summary><div class="faq__body">The roll call of every match that earns a perfect five-star Wrestle Lore rating. ' + n5 + ' matches make the club, across WWE, WCW, TNA, ROH and NXT. Alongside them sit the 4&frac12;&#9733; near misses and the rest of the rated archive. The rating blends Meltzer&rsquo;s <em>Wrestling Observer</em> stars, the Cagematch community score, and historical weight. All five-star matches are equal; the club is not ordered best to worst. <a href="/methodology/">See how we rate</a></div></details>'
      '<details><summary>What is the greatest wrestling match of the modern era?</summary><div class="faq__body">Wrestle Lore rates <a href="/matches/undertaker-vs-hbk-wm25/">The Undertaker vs Shawn Michaels at WrestleMania XXV (2009)</a> a full five stars, and it is regularly voted the greatest WrestleMania match ever, with a Cagematch score around 9.6. Other five-star classics include <a href="/matches/cm-punk-vs-cena-mitb-2011/">CM Punk vs John Cena</a> and <a href="/matches/samoa-joe-vs-cm-punk-roh-2004/">Samoa Joe vs CM Punk</a>. We rate matches by stars rather than ranking one five-star match above another.</div></details>'
      '<details><summary>Where can I watch these matches?</summary><div class="faq__body">Where an <strong>official full-match upload</strong> exists on a promotion&rsquo;s own YouTube channel (WWE or TNA Wrestling), it plays here in a spoiler-safe theater and opens on YouTube in a new tab. Wrestle Lore hosts no footage. The rest of the catalog streams on the promotions&rsquo; home platforms. We never embed unofficial re-uploads.</div></details>'
      '<details><summary>What was The Undertaker&rsquo;s WrestleMania Streak?</summary><div class="faq__body">The Undertaker won his first 21 WrestleMania matches, the run fans call The Streak. <a href="/wrestlers/brock-lesnar/">Brock Lesnar</a> ended it 21&ndash;1 at WrestleMania XXX in 2014. Several ranked entries are Streak defences: WM25 and WM26 against Shawn Michaels, and WM28 against Triple H.</div></details>'
      '<details><summary>Are the ratings ever updated?</summary><div class="faq__body">Yes. Wrestle Lore ratings reflect critical consensus as of mid-2026 and can change as historians re-evaluate matches. Insiders can also add their own ratings on each match page.</div></details>'
      '</div></div></section>'
    )

    related = (
      '<section class="section--tight"><div class="wrap"><div class="section-head"><h2>Related</h2></div>'
      '<nav class="related-links" aria-label="Related pages">'
      '<a href="/matches/">All star-rated matches</a>'
      '<a href="/moments/">Defining moments</a>'
      '<a href="/rivalries/">Legendary rivalries</a>'
      '<a href="/gallery/">Weekly viewing gallery</a>'
      '<a href="/methodology/">How we rate</a>'
      '</nav></div></section>'
    )

    return ('<main id="main">\n' + hero + explorer + streak + faq + related + '\n</main>')

# ---------------- schema ----------------
def build_schema(data):
    items = []
    for m in data:
        items.append('{"@type":"ListItem","position":%d,"url":"%s/matches/%s/","name":%s}'
                     % (m["rank"], BASE, m["slug"], json.dumps(m["title"])))
    itemlist = ('<script type="application/ld+json">'
      '{"@context":"https://schema.org","@type":"ItemList","name":"The Wrestle Lore Five-Star Club",'
      '"description":"A catalog of the highest-rated pro wrestling matches of the modern era, scored by stars rather than ranked.",'
      '"numberOfItems":%d,"itemListOrder":"https://schema.org/ItemListUnordered","itemListElement":[%s]}</script>'
      % (len(data), ",".join(items)))
    faq = ('<script type="application/ld+json">'
      '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
      '{"@type":"Question","name":"What is the Wrestle Lore Five-Star Club?","acceptedAnswer":{"@type":"Answer","text":"The roll call of every match earning a perfect five-star rating. Twelve matches make the club, across WWE, WCW, TNA, ROH and NXT, plus the 4.5-star near misses and a rated archive. The rating blends Dave Meltzer\'s Wrestling Observer stars, the Cagematch community score, and historical weight. All five-star matches are treated as equal rather than ranked against each other."}},'
      '{"@type":"Question","name":"What is the greatest wrestling match of the modern era?","acceptedAnswer":{"@type":"Answer","text":"Wrestle Lore rates The Undertaker vs Shawn Michaels at WrestleMania XXV (2009) a full five stars, and it is regularly voted the greatest WrestleMania match ever, with a Cagematch score around 9.6. Other five-star classics include CM Punk vs John Cena (Money in the Bank 2011) and Samoa Joe vs CM Punk (ROH 2004). We rate by stars rather than ranking one five-star match above another."}},'
      '{"@type":"Question","name":"Where can I watch these matches?","acceptedAnswer":{"@type":"Answer","text":"Where an official full-match upload exists on a promotion\'s own YouTube channel (WWE or TNA Wrestling), it plays in a spoiler-safe theater on the page and opens on YouTube in a new tab. Wrestle Lore hosts no footage and never embeds unofficial re-uploads. The rest of the catalog streams on the promotions\' home platforms."}},'
      '{"@type":"Question","name":"What was The Undertaker\'s WrestleMania Streak?","acceptedAnswer":{"@type":"Answer","text":"The Undertaker won his first 21 WrestleMania matches before Brock Lesnar ended it 21-1 at WrestleMania XXX in 2014. Several ranked entries are Streak defences against Shawn Michaels (WM25, WM26) and Triple H (WM28)."}},'
      '{"@type":"Question","name":"Are the ratings ever updated?","acceptedAnswer":{"@type":"Answer","text":"Yes. Wrestle Lore ratings reflect critical consensus as of mid-2026 and can be revised as historians re-evaluate matches. Insiders can add their own ratings on each match page."}}'
      ']}</script>')
    faq = faq.replace("Twelve matches make the club",
                      numword(sum(1 for m in data if m["tier"] == "five-star")) + " matches make the club")
    return itemlist + "\n" + faq

# ---------------- swap into page ----------------
def main():
    data = json.load(open(DATA, encoding="utf-8"))
    page = open(SRC_PAGE, encoding="utf-8").read()

    body = build_body(data)
    page = re.sub(r"<main id=\"main\">.*?</main>", lambda _: body, page, count=1, flags=re.S)

    # remove existing FAQPage ld+json, keep BreadcrumbList; inject fresh ItemList+FAQ
    page = re.sub(r'<script type="application/ld\+json">\s*\{"@context":"https://schema.org","@type":"FAQPage".*?</script>\s*', "", page, flags=re.S)
    page = page.replace("</head>", build_schema(data) + "\n</head>", 1)

    # Benoit is scrubbed from WWE history: swap him out of the nav five-star ladder too.
    # (The permanent fix is components/meganav.html + re-stamp; this keeps the preview clean.)
    page = re.sub(
        r'<a class="dk lrow" href="/matches/angle-vs-benoit-royal-rumble-2003/">.*?</a>',
        lambda _: ('<a class="dk lrow" href="/matches/bret-hart-vs-austin-wm13/">'
                   '<span class="rank">05</span>'
                   '<span class="lbody"><span class="klbl">WRESTLEMANIA 13 &middot; SUBMISSION &middot; \'97</span>'
                   '<span class="lnm">Bret Hart vs Austin</span></span>'
                   '<span class="meter7" aria-hidden="true"><span class="off">&starf;&starf;&starf;&starf;&starf;</span>'
                   '<span class="on">&starf;&starf;&starf;&starf;&starf;</span></span>'
                   '<span class="ltag">5.0</span></a>'),
        page, count=1, flags=re.S)

    # ensure media.js + rankings.js load
    if "/js/media.js" not in page:
        page = page.replace('<script src="/js/nav.js', '<script src="/js/media.js" defer></script>\n<script src="/js/rankings.js" defer></script>\n<script src="/js/nav.js', 1)

    # meta description refresh (hub framing)
    page = re.sub(r'<meta name="description" content="[^"]*">',
        '<meta name="description" content="The Wrestle Lore Five-Star Club: a browsable catalog of the highest-rated pro wrestling matches ever. Perfect five-star classics plus the 4.5-star near misses across WWE, WCW, ECW, TNA, ROH and NXT, with spoiler-safe winners and official match video. Filter by rating, sort, and watch.">',
        page, count=1)

    # writing-style safety sweep across the whole page (head + body + attributes):
    # no em dashes as separators, no decorative arrows. En-dash score/range entities are left intact.
    for a, b in ((" &mdash; ", ", "), ("&mdash;", ", "), (" — ", ", "), ("—", ", "),
                 (" &rarr;", ""), ("&rarr;", ""), (" →", ""), ("→", ""), ("➜", ""), ("↗", "")):
        page = page.replace(a, b)

    out = SRC_PAGE
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(page)
    print("wrote", out, "(%d bytes)" % len(page))
    print("cards:", len(data), "| with video:", sum(1 for m in data if m["video"]["id"]))

if __name__ == "__main__":
    main()
