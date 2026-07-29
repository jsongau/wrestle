#!/usr/bin/env python3
"""Viewing Gallery generator.
Emits, from the WEEKS data:
  /media/w/<slug>/index.html   -> one crawlable page per video (autoplay player + VideoObject schema)
  /gallery/<YYYY-MM-DD>/        -> one week's master-detail gallery (cards LINK to the video pages)
  /gallery/                     -> archive hub: full weekly TV schedule calendar + SEO copy + FAQ
Also: patches the homepage This-Week widget facades to link to the video pages,
and injects all new URLs into sitemap.xml. Run then `python3 build/apply_shell.py`.
To add a week: append a dict to WEEKS and re-run. Pages carry universal-shell stubs.
ROOT overridable: WL_ROOT=/path/to/repo python3 build/build_gallery.py
Networks verified 2026-07-28 — see data/research-weekly-schedule.md (do not "fix" back):
  Raw=Netflix · SmackDown=USA/Peacock · NXT=The CW · AEW=TBS/TNT+HBO Max · TNA=AMC/AMC+.
"""
import os, re, calendar, datetime, json

ROOT = os.environ.get("WL_ROOT", "/root/wwe")
BASE = "https://wrestlelore.com"

# ---- streaming homes, PER SHOW (US, verified 2026-07-28) ----
NETFLIX = "https://www.netflix.com/tudum/articles/how-to-watch-wwe-on-netflix"
PEACOCK = "https://www.peacocktv.com/sports/wwe"
CWAPP   = "https://www.cwtv.com/shows/wwe-nxt/"
HBOMAX  = "https://www.hbomax.com/aew"
AMCPLUS = "https://www.amcplus.com"
SHOWNET = {  # show -> (streaming label, url)
  "Raw": ("Netflix", NETFLIX), "SmackDown": ("Peacock", PEACOCK), "NXT": ("The CW", CWAPP),
  "Dynamite": ("HBO Max", HBOMAX), "Collision": ("HBO Max", HBOMAX), "iMPACT": ("AMC+", AMCPLUS),
}
def shownet(label):
    return SHOWNET.get(label.split("·")[0].strip(), ("Netflix", NETFLIX))

SHOWS  = {"WWE": "Raw & SmackDown", "AEW": "Dynamite & Collision", "TNA": "iMPACT", "NXT": "NXT"}
TABNET = {"WWE": "Raw · Netflix — SmackDown · USA/Peacock", "AEW": "TBS/TNT · HBO Max",
          "TNA": "iMPACT · AMC & AMC+", "NXT": "NXT · The CW"}
WATCHLINKS = {
  "WWE": ('<a class="tw-net" href="%s" target="_blank" rel="noopener">Raw on Netflix</a>'
          '<a class="tw-net" href="%s" target="_blank" rel="noopener">SmackDown on Peacock</a>' % (NETFLIX, PEACOCK)),
  "AEW": '<a class="tw-net" href="%s" target="_blank" rel="noopener">AEW on TBS/TNT · stream on HBO Max</a>' % HBOMAX,
  "TNA": '<a class="tw-net" href="%s" target="_blank" rel="noopener">iMPACT on AMC · stream on AMC+</a>' % AMCPLUS,
  "NXT": '<a class="tw-net" href="%s" target="_blank" rel="noopener">NXT live on The CW</a>' % CWAPP,
}
ORDER = ["WWE", "AEW", "TNA", "NXT"]

# ---- the recurring weekly TV grid (Mon=0..Sun=6) + dated specials ----
SCHEDULE = {
  0: [("WWE", "Raw", "Netflix")],
  1: [("WWE", "NXT", "The CW")],
  2: [("AEW", "Dynamite", "TBS · HBO Max")],
  3: [("TNA", "iMPACT", "AMC · AMC+")],
  4: [("WWE", "SmackDown", "USA · Peacock")],
  5: [("AEW", "Collision", "TNT · HBO Max")],
  6: [],
}
SPECIALS = {  # date -> (company, event, note)  — PLEs/specials on their REAL dates
  datetime.date(2026, 7, 18): ("WWE", "Saturday Night's Main Event", "MSG · NBC · Peacock"),
  datetime.date(2026, 7, 26): ("AEW", "Redemption", "Montreal · HBO Max · PPV"),
}
CHIPCLS = {"Raw": "wwe", "SmackDown": "wwe", "NXT": "nxt", "Dynamite": "aew", "Collision": "aew", "iMPACT": "tna"}

WEEKS = [
  {"week":"2026-07-20","label":"Week of July 20, 2026","start":datetime.date(2026,7,20),"promos":{
     "WWE":[("4e_UUsgGk7I","2026-07-20","Raw · Full show highlights"),("PUvTijJM7jY","2026-07-20","Raw · Top 10 moments"),
            ("RxI4yvWIuRU","2026-07-24","SmackDown · Full show highlights"),("yIvKS9Aub3M","2026-07-24","SmackDown · Top 10 moments")],
     "AEW":[("XFgrft96kQc","2026-07-22","Dynamite · TNT Championship"),("lKanl86PGZ8","2026-07-22","Dynamite · Women's Tag Title"),
            ("p5ryAl5rFvI","2026-07-22","Dynamite · Tag team main event"),("C0FSDMJAHf0","2026-07-25","Collision · Main event scene")],
     "TNA":[("am_jSHkhRXM","2026-07-23","iMPACT · World Title main event"),("ciYpd4ysD8s","2026-07-23","iMPACT · Fallout"),
            ("EbaTy6LvQ-4","2026-07-23","iMPACT · TV Title tournament")],
     "NXT":[("gt46FaNa18E","2026-07-21","NXT · Full show highlights"),("cB_XQGhra-c","2026-07-21","NXT · Title Street Fight"),
            ("nFUnfdu326Q","2026-07-21","NXT · A new arrival"),("6BPO4g8oFFM","2026-07-21","NXT · Grudge match")]}},
  {"week":"2026-07-13","label":"Week of July 13, 2026","start":datetime.date(2026,7,13),"promos":{
     "WWE":[("F5MaGPEgNpk","2026-07-13","Raw · Full show highlights"),("HoY5Q2MEulU","2026-07-13","Raw · Top 10 moments"),
            ("f0fhFVG0S6Q","2026-07-17","SmackDown · Full show highlights"),("o1H6NTSLkTM","2026-07-17","SmackDown · Top 10 moments")],
     "AEW":[("-RBTRrsa8wI","2026-07-15","Dynamite · Tag team match"),("H1UiQT5SewE","2026-07-15","Dynamite · Women's tag match"),
            ("aTgsJgs0kfw","2026-07-18","Collision · Singles match"),("WJ_-lFglkW4","2026-07-18","Collision · Backstage")],
     "TNA":[("MufGdGZQ7DA","2026-07-16","iMPACT · X-Division Championship"),("ptlVuM7K09E","2026-07-16","iMPACT · TV Title tournament"),
            ("xFyXTGKBLqg","2026-07-16","iMPACT · In-ring segment"),("qp8XCs-MHRI","2026-07-16","iMPACT · Backstage")],
     "NXT":[("0drmI0Tx5pA","2026-07-14","NXT · Full show highlights"),("D7XrmRr-TtU","2026-07-14","NXT · Top 10 moments"),
            ("XRkOtmOderI","2026-07-14","NXT · Triple threat match"),("xbzzpgJG6RM","2026-07-14","NXT · Tag Team Championship")]}},
]

def esc(s): return s.replace("&","&amp;").replace('"',"&quot;").replace("<","&lt;")
def slugify(s):
    s = s.lower().replace("·"," ").replace("&","and")
    s = re.sub(r"[^a-z0-9]+","-",s).strip("-")
    return re.sub(r"-+","-",s)
def pretty(dstr): return datetime.date.fromisoformat(dstr).strftime("%B %-d, %Y")
def dayshort(dstr): return datetime.date.fromisoformat(dstr).strftime("%a · %b %-d").upper()

def slug(promo, date, label): return slugify("%s %s %s" % (promo, label, date))
def page_url(promo, date, label): return "/media/w/%s/" % slug(promo, date, label)
def vtitle(promo, label, date): return "%s %s, %s" % (promo, label.replace(" · ", ", "), pretty(date))

# ---- index for related lookups ----
INDEX = {}  # yid -> dict
for wk in WEEKS:
    for promo in ORDER:
        for (yid, date, label) in wk["promos"].get(promo, []):
            INDEX[yid] = {"promo":promo,"date":date,"label":label,"week":wk["week"],"weeklabel":wk["label"],
                          "slug":slug(promo,date,label),"url":page_url(promo,date,label)}

def facade_card(promo, yid, date, label):
    net, url = shownet(label)
    ttl = vtitle(promo, label, date)
    href = page_url(promo, date, label)
    return ('<li><article class="vcard"><div class="yt" data-yt-id="%s" data-yt-title="%s" data-yt-creator="%s" data-yt-service="%s" data-yt-service-url="%s" data-yt-page="%s">'
            '<a class="yt__link" href="%s">%s</a></div>'
            '<div class="vcard__body"><span class="telemetry"><b>%s</b></span><h3 class="vcard__title">%s</h3></div></article></li>'
            % (yid, esc(ttl), promo, esc(net), url, href, href, esc(label), dayshort(date), esc(label)))

def week_widget(wk):
    tabs, panels = [], []
    for i, promo in enumerate(ORDER):
        sel = "true" if i==0 else "false"; ti = "" if i==0 else ' tabindex="-1"'
        tabs.append('<button class="tw-item" type="button" role="tab" id="tw-tab-%s" aria-controls="tw-panel-%s" aria-selected="%s"%s><span class="tw-item__name">%s</span><span class="tw-item__net">%s</span></button>'
                    % (promo.lower(),promo.lower(),sel,ti,promo,esc(TABNET[promo])))
        hidden = "" if i==0 else " hidden"
        cards = "\n              ".join(facade_card(promo,y,d,l) for (y,d,l) in wk["promos"][promo])
        panels.append('<div class="tw-panel" role="tabpanel" id="tw-panel-%s" aria-labelledby="tw-tab-%s"%s>'
          '<div class="tw-panel__head"><span class="telemetry"><b>%s · %s</b></span>'
          '<span class="tw-nets">%s</span></div>'
          '<ul class="tw-rail">\n              %s\n            </ul></div>'
          % (promo.lower(),promo.lower(),hidden,wk["label"].upper(),promo,WATCHLINKS[promo],cards))
    return '<div class="tw-layout"><div class="tw-list" data-wl-tabs role="tablist" aria-label="Choose a promotion">%s</div><div class="tw-detail">%s</div></div>' % ("".join(tabs),"".join(panels))

def week_page(wk, older, newer):
    nav = []
    if newer: nav.append('<a class="link-more" href="/gallery/%s/">Newer week</a>' % newer["week"])
    nav.append('<a class="link-more" href="/gallery/">All weeks</a>')
    if older: nav.append('<a class="link-more" href="/gallery/%s/">Older week</a>' % older["week"])
    main = ('<section class="section thisweek" aria-label="%s">\n<div class="wrap">\n'
      '<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/gallery/">Viewing Gallery</a></li><li aria-current="page">%s</li></ol></nav>\n'
      '<div class="section-head"><div><p class="eyebrow">The Week · Catch Up</p><h2>%s</h2><hr class="rule-gold"></div><span class="tw-dateline">%s</span></div>\n'
      '<p class="tw-lede">Every show from this week in one place. Titles give nothing away and thumbnails blur until you hover, so you can catch up without getting spoiled. Pick a promotion, press play, and each clip opens with a link to where the full show streams.</p>\n'
      '%s\n<div class="cluster" style="gap:var(--sp-4);margin-top:var(--sp-5)">%s</div>\n</div>\n</section>'
      % (wk["label"],wk["label"],wk["label"],wk["label"].upper(),week_widget(wk)," ".join(nav)))
    return shell(vtitle_week(wk), "Catch up on %s: WWE, AEW, TNA and NXT highlights in one spoiler-safe viewing gallery, with links to where each show streams." % wk["label"],
                 "%s/gallery/%s/" % (BASE,wk["week"]), main)

def vtitle_week(wk): return "%s — Viewing Gallery | Wrestle Lore" % wk["label"]

def video_page(promo, yid, date, label, wk):
    net, url = shownet(label)
    title = vtitle(promo, label, date)
    desc = "Catch up on %s from %s. Watch the highlight in the Wrestle Lore viewing gallery, with a link to stream the full show on %s." % (title, pretty(date), net)
    canonical = "%s%s" % (BASE, page_url(promo,date,label))
    rel = []
    for p in ORDER:
        for (y,d,l) in wk["promos"].get(p,[]):
            if y != yid: rel.append(facade_card(p,y,d,l))
    rel_html = "\n            ".join(rel[:8])
    jsonld = (
      '<script type="application/ld+json">{"@context":"https://schema.org","@type":"VideoObject",'
      '"name":"%s","description":"%s","thumbnailUrl":"https://i.ytimg.com/vi/%s/hqdefault.jpg",'
      '"uploadDate":"%s","embedUrl":"https://www.youtube-nocookie.com/embed/%s",'
      '"contentUrl":"https://www.youtube.com/watch?v=%s","publisher":{"@type":"Organization","name":"Wrestle Lore","url":"%s/"}}</script>\n'
      '<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
      '{"@type":"ListItem","position":1,"name":"Home","item":"%s/"},'
      '{"@type":"ListItem","position":2,"name":"Viewing Gallery","item":"%s/gallery/"},'
      '{"@type":"ListItem","position":3,"name":"%s","item":"%s/gallery/%s/"},'
      '{"@type":"ListItem","position":4,"name":"%s","item":"%s"}]}</script>'
      % (esc(title),esc(desc),yid,date,yid,yid,BASE,BASE,BASE,esc(wk["label"]),BASE,wk["week"],esc(title),canonical)
    )
    main = ('<section class="section thisweek wl-vpage" aria-label="%s">\n<div class="wrap">\n'
      '<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/gallery/">Viewing Gallery</a></li>'
      '<li><a href="/gallery/%s/">%s</a></li><li aria-current="page">%s</li></ol></nav>\n'
      '<div class="wl-vp-brand"><span class="wl-modal__mark">WL</span><span class="wl-modal__gallery"><a href="/gallery/">Wrestle Lore <b>Viewing Gallery</b></a></span>'
      '<span class="wl-modal__note">Clip embedded from the official channel. Watch the full show on its home network.</span></div>\n'
      '<div class="wl-pageplay"><div class="wl-modal__frame"><div class="wl-velvet"><div class="wl-modal__stage" data-yt-page-player data-yt-id="%s"></div></div></div></div>\n'
      '<div class="wl-vp-bar"><div><p class="eyebrow">%s · %s</p><h1 class="wl-vp-title">%s</h1></div>'
      '<div class="wl-vp-links"><a class="tw-net" href="%s" target="_blank" rel="noopener">Full show on %s</a>'
      '<a class="tw-net" href="https://www.youtube.com/watch?v=%s" target="_blank" rel="noopener">Watch on YouTube</a>'
      '<button class="wl-modal__share" type="button" data-share-url="%s"><svg class="wl-share-ico" viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path fill="currentColor" d="M18 16.08a2.9 2.9 0 0 0-2.05.86l-6.9-4.02a3 3 0 0 0 0-1.84l6.83-3.98A3 3 0 1 0 15 5a3 3 0 0 0 .06.6L8.24 9.58a3 3 0 1 0 0 4.84l6.88 4.02A3 3 0 1 0 18 16.08z"/></svg><span>Share</span></button></div></div>\n'
      '<p class="wl-vp-ctx">%s A neutral, spoiler-safe highlight from %s. Full show streams on %s.</p>\n'
      '<div class="sec-h" style="margin-top:var(--sp-6)"><h2>More from %s</h2><a class="link-more" href="/gallery/%s/">See the full week</a></div>\n'
      '<ul class="tw-rail">\n            %s\n</ul>\n</div>\n</section>'
      % (title, wk["week"], esc(wk["label"]), esc(title), yid, promo, SHOWS[promo], esc(title), url, net, yid, esc(canonical),
         esc(title+"."), pretty(date), net, esc(wk["label"]), wk["week"], rel_html))
    return shell("%s | Wrestle Lore Viewing Gallery" % title, desc, canonical, main, extra_head=jsonld)

# ---- THE SCHEDULE CALENDAR (cal3) ----
def cal_chip(co, name, note, special=False):
    if special:
        return ('<span class="cal3-chip cal3-chip--sp"><b class="cal3-co">%s</b><span class="cal3-nm">%s</span><small>%s</small></span>'
                % (esc(co), esc(name), esc(note)))
    cls = CHIPCLS.get(name, "wwe")
    return ('<span class="cal3-chip cal3-chip--%s"><b class="cal3-co">%s</b><span class="cal3-nm">%s</span><small>%s</small></span>'
            % (cls, esc(co), esc(name), esc(note)))

def calendar_html(weeks):
    wbm = {}
    for wk in weeks:
        for i in range(7): wbm[wk["start"]+datetime.timedelta(days=i)] = wk["week"]
    first = weeks[0]["start"]
    mo_name = first.strftime("%B"); mo_year = first.strftime("%Y")
    heads = "".join('<span class="cal3-h">%s</span>' % d for d in ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
    cells = []
    for d in calendar.Calendar(firstweekday=0).itermonthdates(first.year, first.month):
        if d.month != first.month:
            cells.append('<span class="cal3-cell cal3-cell--empty" aria-hidden="true"></span>'); continue
        chips = "".join(cal_chip("WWE" if co=="WWE" else co, show, note) for (co, show, note) in SCHEDULE[d.weekday()])
        if d in SPECIALS:
            sco, sname, snote = SPECIALS[d]
            chips += cal_chip(sco, sname, snote, special=True)
        head = ('<span class="cal3-d"><b>%d</b><small>%s</small></span>' % (d.day, d.strftime("%a")))
        w = wbm.get(d)
        if w:
            cells.append('<a class="cal3-cell cal3-cell--live" href="/gallery/%s/" aria-label="%s %d: open the catch-up gallery">%s%s'
                         '<span class="cal3-tag">▸ CATCH UP</span></a>' % (w, mo_name, d.day, head, chips))
        else:
            cells.append('<div class="cal3-cell">%s%s</div>' % (head, chips))
    nclips = sum(len(v) for wk in weeks for v in wk["promos"].values())
    return ('<div class="cal3" role="region" aria-label="%s %s wrestling TV schedule">'
      '<div class="cal3__top"><span class="cal3__mo">%s <b>%s</b></span>'
      '<span class="cal3__hint">Gold nights link to a spoiler-safe catch-up gallery</span></div>'
      '<div class="cal3-head">%s</div><div class="cal3-grid">%s</div>'
      '<div class="cal3__foot"><span>Weekly TV grid recurs every week · specials sit on their real dates</span>'
      '<span><b>%d weeks</b> ready to catch up · %d clips</span></div></div>'
      % (mo_name, mo_year, mo_name, mo_year, heads, "".join(cells), len(weeks), nclips))

LEGEND = ('<div class="lg3row" role="list" aria-label="Calendar key">'
  '<span class="lg3" role="listitem"><i class="lg3__d" style="background:var(--c-wwe,#c8102e)"></i>WWE · Raw / SmackDown</span>'
  '<span class="lg3" role="listitem"><i class="lg3__d" style="background:var(--c-nxt,#f5c518)"></i>WWE NXT</span>'
  '<span class="lg3" role="listitem"><i class="lg3__d" style="background:var(--c-aew,#c8a24a)"></i>AEW · Dynamite / Collision</span>'
  '<span class="lg3" role="listitem"><i class="lg3__d" style="background:var(--c-tna,#1e73be)"></i>TNA · iMPACT</span>'
  '<span class="lg3" role="listitem"><i class="lg3__d lg3__d--sp"></i>Premium Live Event</span>'
  '<span class="lg3 lg3--gold" role="listitem"><i class="lg3__d lg3__d--gold"></i>Catch-up gallery available</span></div>')

FAQS = [
  ("What wrestling airs each week?",
   "Every week: WWE Raw on Monday (Netflix), WWE NXT on Tuesday (The CW), AEW Dynamite on Wednesday (TBS, streaming on HBO Max), TNA iMPACT on Thursday (AMC and AMC+), WWE SmackDown on Friday (USA Network, streaming on Peacock) and AEW Collision on Saturday (TNT, streaming on HBO Max). Premium Live Events land on top of the weekly grid."),
  ("Where can I stream WWE, AEW, TNA and NXT?",
   "WWE Raw streams on Netflix. SmackDown airs on USA Network and streams on Peacock. NXT airs on The CW. AEW Dynamite and Collision air on TBS and TNT and stream on HBO Max. TNA iMPACT airs on AMC and streams on AMC+. Every clip in the gallery links out to the show's official home."),
  ("Is the Viewing Gallery spoiler-safe?",
   "Yes. Clip titles give nothing away and thumbnails stay blurred until you hover, so you can pick a week and press play without results jumping out at you."),
]

def hub_jsonld(weeks):
    items = [{"@type":"ListItem","position":i+1,"name":wk["label"],
              "url":"%s/gallery/%s/" % (BASE, wk["week"])} for i, wk in enumerate(weeks)]
    coll = {"@context":"https://schema.org","@type":"CollectionPage",
      "name":"Wrestle Lore Viewing Gallery","url":"%s/gallery/" % BASE,
      "description":"The weekly wrestling TV calendar and spoiler-safe catch-up galleries for WWE, AEW, TNA and NXT.",
      "mainEntity":{"@type":"ItemList","itemListElement":items}}
    faq = {"@context":"https://schema.org","@type":"FAQPage",
      "mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQS]}
    crumbs = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Home","item":"%s/" % BASE},
      {"@type":"ListItem","position":2,"name":"Viewing Gallery","item":"%s/gallery/" % BASE}]}
    return "".join('<script type="application/ld+json">%s</script>\n' % json.dumps(x, ensure_ascii=False) for x in (coll, faq, crumbs))

def hub_page(weeks):
    cards = []
    for i, wk in enumerate(weeks):
        badge = '<span class="gwk-badge">Latest</span>' if i==0 else ""
        n = sum(len(v) for v in wk["promos"].values())
        cards.append('<a class="gwk" href="/gallery/%s/">%s<span class="gwk-date">%s</span><span class="gwk-meta">WWE · AEW · TNA · NXT — %d clips</span></a>' % (wk["week"],badge,wk["label"],n))
    faq_html = "".join('<div class="gfaq__item"><h3>%s</h3><p>%s</p></div>' % (esc(q), esc(a)) for q, a in FAQS)
    main = ('<section class="section" aria-label="Viewing Gallery archive">\n<div class="wrap">\n'
      '<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li aria-current="page">Viewing Gallery</li></ol></nav>\n'
      '<div class="section-head"><div><p class="eyebrow">The Archive · Updated Weekly</p><h2>This Week in Wrestling</h2><hr class="rule-gold"></div></div>\n'
      '<p class="tw-lede">Six shows a week, four promotions, one place to catch up. <b>WWE Raw</b> opens Monday on Netflix, <b>NXT</b> runs Tuesday on The CW, <b>AEW Dynamite</b> hits Wednesday, <b>TNA iMPACT</b> lands Thursday on AMC, <b>SmackDown</b> closes the work week Friday on USA, and <b>AEW Collision</b> rounds out Saturday. The calendar maps every night so you can see what aired and where to stream it, then jump into a spoiler-safe highlight gallery for any week that has gone gold.</p>\n'
      '%s\n%s\n'
      '<p class="sub-h telemetry" style="margin-top:var(--sp-6)"><b>JUMP INTO A WEEK</b></p>\n'
      '<div class="gwk-list">%s</div>\n'
      '<div class="gfaq"><h2>Catch up, spoiler-safe</h2>%s</div>\n'
      '</div>\n</section>' % (LEGEND, calendar_html(weeks), "".join(cards), faq_html))
    return shell("Wrestling Viewing Gallery — Weekly WWE, AEW, TNA & NXT Recaps | Wrestle Lore",
                 "The weekly wrestling TV calendar and spoiler-safe catch-up galleries: WWE, AEW, TNA and NXT — what airs each night, where to stream it, and every week's highlights.",
                 "%s/gallery/" % BASE, main, extra_head=hub_jsonld(weeks))

def shell(title, desc, canonical, main, extra_head=""):
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n'
      '<title>%s</title>\n<meta name="description" content="%s">\n<link rel="canonical" href="%s">\n%s<link rel="stylesheet" href="/css/site.css">\n</head>\n<body>\n'
      '<header class="site-header nav7"></header>\n<main id="main">\n%s\n</main>\n<footer class="site-footer site-footer--fat"></footer>\n'
      '<script src="/js/media.js" defer></script>\n</body>\n</html>\n' % (esc(title),esc(desc),canonical,extra_head,main))

def write(path, html):
    full = os.path.join(ROOT, path.lstrip("/")); os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full,"w",encoding="utf-8").write(html)

def patch_homepage():
    p = os.path.join(ROOT,"index.html"); html = open(p,encoding="utf-8").read(); orig = html
    for yid, info in INDEX.items():
        if info["week"] != WEEKS[0]["week"]: continue
        u = info["url"]
        if 'data-yt-id="%s"' % yid in html and 'data-yt-page' not in html.split('data-yt-id="%s"'%yid,1)[1][:120]:
            html = html.replace('data-yt-id="%s"' % yid, 'data-yt-id="%s" data-yt-page="%s"' % (yid,u), 1)
        html = html.replace('href="https://www.youtube.com/watch?v=%s"' % yid, 'href="%s"' % u)
    if html != orig: open(p,"w",encoding="utf-8").write(html); print("patched homepage facades")

def update_sitemap():
    p = os.path.join(ROOT,"sitemap.xml"); xml = open(p,encoding="utf-8").read()
    urls = ["/gallery/"] + ["/gallery/%s/" % wk["week"] for wk in WEEKS] + [info["url"] for info in INDEX.values()]
    add = ""
    for u in urls:
        loc = BASE + u
        if loc not in xml: add += '  <url><loc>%s</loc><changefreq>weekly</changefreq></url>\n' % loc
    if add:
        xml = xml.replace("</urlset>", add + "</urlset>"); open(p,"w",encoding="utf-8").write(xml); print("sitemap +%d urls" % add.count("<url>"))

if __name__ == "__main__":
    nv = 0
    for wk in WEEKS:
        for promo in ORDER:
            for (y,d,l) in wk["promos"][promo]:
                write("/media/w/%s/index.html" % slug(promo,d,l), video_page(promo,y,d,l,wk)); nv += 1
    for i, wk in enumerate(WEEKS):
        newer = WEEKS[i-1] if i>0 else None; older = WEEKS[i+1] if i+1<len(WEEKS) else None
        write("/gallery/%s/index.html" % wk["week"], week_page(wk, older, newer))
    write("/gallery/index.html", hub_page(WEEKS))
    patch_homepage(); update_sitemap()
    print("done: %d video pages + %d week pages + hub (ROOT=%s)" % (nv, len(WEEKS), ROOT))
