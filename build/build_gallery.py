#!/usr/bin/env python3
"""Viewing Gallery archive generator.
Reads WEEKS data and emits:
  /gallery/index.html                 -> archive hub with a month calendar + week cards
  /gallery/<YYYY-MM-DD>/index.html     -> one week's master-detail gallery (per promotion, 4 clips)
Pages carry the universal-shell stubs (<header class="site-header nav7"></header>,
<footer class="site-footer site-footer--fat"></footer>) so build/apply_shell.py
stamps the real nav/footer/palette afterwards. Add a new dict to WEEKS each Monday.
"""
import os, calendar, datetime

ROOT = "/root/wwe"
NETFLIX = "https://www.netflix.com/tudum/articles/how-to-watch-wwe-on-netflix"
HBOMAX  = "https://www.hbomax.com/aew"
AMC     = "https://www.primevideo.com/detail/0JUDFWRZQVXA7XUGHXAN08F1NQ"

NET = {
  "WWE": ("Netflix", NETFLIX), "NXT": ("Netflix", NETFLIX),
  "AEW": ("HBO Max", HBOMAX),  "TNA": ("AMC+ (Prime Video)", AMC),
}
PROMO_SHOWS = {"WWE":"Raw & SmackDown","AEW":"Dynamite & Collision","TNA":"iMPACT","NXT":"NXT"}

WEEKS = [
  {"week":"2026-07-20","label":"Week of July 20, 2026","start":datetime.date(2026,7,20),
   "promos":{
     "WWE":[("4e_UUsgGk7I","2026-07-20","Raw · Full show highlights"),
            ("PUvTijJM7jY","2026-07-20","Raw · Top 10 moments"),
            ("RxI4yvWIuRU","2026-07-24","SmackDown · Full show highlights"),
            ("yIvKS9Aub3M","2026-07-24","SmackDown · Top 10 moments")],
     "AEW":[("XFgrft96kQc","2026-07-22","Dynamite · TNT Championship"),
            ("lKanl86PGZ8","2026-07-22","Dynamite · Women's Tag Title"),
            ("p5ryAl5rFvI","2026-07-22","Dynamite · Tag team main event"),
            ("C0FSDMJAHf0","2026-07-25","Collision · Main event scene")],
     "TNA":[("am_jSHkhRXM","2026-07-23","iMPACT · World Title main event"),
            ("ciYpd4ysD8s","2026-07-23","iMPACT · Fallout"),
            ("EbaTy6LvQ-4","2026-07-23","iMPACT · TV Title tournament")],
     "NXT":[("gt46FaNa18E","2026-07-21","NXT · Full show highlights"),
            ("cB_XQGhra-c","2026-07-21","NXT · Title Street Fight"),
            ("nFUnfdu326Q","2026-07-21","NXT · A new arrival"),
            ("6BPO4g8oFFM","2026-07-21","NXT · Grudge match")],
   }},
  {"week":"2026-07-13","label":"Week of July 13, 2026","start":datetime.date(2026,7,13),
   "promos":{
     "WWE":[("F5MaGPEgNpk","2026-07-13","Raw · Full show highlights"),
            ("HoY5Q2MEulU","2026-07-13","Raw · Top 10 moments"),
            ("f0fhFVG0S6Q","2026-07-17","SmackDown · Full show highlights"),
            ("o1H6NTSLkTM","2026-07-17","SmackDown · Top 10 moments")],
     "AEW":[("-RBTRrsa8wI","2026-07-15","Dynamite · Tag team match"),
            ("H1UiQT5SewE","2026-07-15","Dynamite · Women's tag match"),
            ("aTgsJgs0kfw","2026-07-18","Collision · Singles match"),
            ("WJ_-lFglkW4","2026-07-18","Collision · Backstage")],
     "TNA":[("MufGdGZQ7DA","2026-07-16","iMPACT · X-Division Championship"),
            ("ptlVuM7K09E","2026-07-16","iMPACT · TV Title tournament"),
            ("xFyXTGKBLqg","2026-07-16","iMPACT · In-ring segment"),
            ("qp8XCs-MHRI","2026-07-16","iMPACT · Backstage")],
     "NXT":[("0drmI0Tx5pA","2026-07-14","NXT · Full show highlights"),
            ("D7XrmRr-TtU","2026-07-14","NXT · Top 10 moments"),
            ("XRkOtmOderI","2026-07-14","NXT · Triple threat match"),
            ("xbzzpgJG6RM","2026-07-14","NXT · Tag Team Championship")],
   }},
]

def esc(s): return s.replace("&","&amp;").replace('"',"&quot;")
def daylabel(dstr):
    d = datetime.date.fromisoformat(dstr)
    return d.strftime("%a · %b %-d").upper()

def card(promo, vid):
    yid, date, label = vid
    net, url = NET[promo]
    title = f"{promo} {label.split(chr(183))[-1].strip()}, {datetime.date.fromisoformat(date).strftime('%B %-d, %Y')}"
    return (
      '<li><article class="vcard"><div class="yt" data-yt-id="%s" data-yt-title="%s" data-yt-creator="%s" data-yt-service="%s" data-yt-service-url="%s">'
      '<a class="yt__link" href="https://www.youtube.com/watch?v=%s">%s</a></div>'
      '<div class="vcard__body"><span class="telemetry"><b>%s</b></span><h3 class="vcard__title">%s</h3></div></article></li>'
      % (yid, esc(title), promo, esc(net), url, yid, esc(label), daylabel(date), esc(label))
    )

def week_widget(wk):
    order = ["WWE","AEW","TNA","NXT"]
    tabs = []
    panels = []
    for i, promo in enumerate(order):
        net, url = NET[promo]
        sel = "true" if i==0 else "false"
        ti = "" if i==0 else ' tabindex="-1"'
        tabs.append('<button class="tw-item" type="button" role="tab" id="tw-tab-%s" aria-controls="tw-panel-%s" aria-selected="%s"%s><span class="tw-item__name">%s</span><span class="tw-item__net">%s · %s</span></button>'
                    % (promo.lower(), promo.lower(), sel, ti, promo, PROMO_SHOWS[promo], net))
        hidden = "" if i==0 else " hidden"
        cards = "\n              ".join(card(promo, v) for v in wk["promos"][promo])
        panels.append(
          '<div class="tw-panel" role="tabpanel" id="tw-panel-%s" aria-labelledby="tw-tab-%s"%s>'
          '<div class="tw-panel__head"><span class="telemetry"><b>%s · %s</b></span>'
          '<a class="tw-net" href="%s" target="_blank" rel="noopener">Watch %s on %s</a></div>'
          '<ul class="tw-rail">\n              %s\n            </ul></div>'
          % (promo.lower(), promo.lower(), hidden, wk["label"].upper(), promo, url, promo, net, cards))
    return ('<div class="tw-layout"><div class="tw-list" data-wl-tabs role="tablist" aria-label="Choose a promotion">%s</div>'
            '<div class="tw-detail">%s</div></div>' % ("".join(tabs), "".join(panels)))

def week_page(wk, prev_wk, next_wk):
    nav = []
    if next_wk: nav.append('<a class="link-more" href="/gallery/%s/">Newer week</a>' % next_wk["week"])
    nav.append('<a class="link-more" href="/gallery/">All weeks</a>')
    if prev_wk: nav.append('<a class="link-more" href="/gallery/%s/">Older week</a>' % prev_wk["week"])
    main = (
      '<section class="section thisweek" aria-label="%s">\n<div class="wrap">\n'
      '<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li>'
      '<li><a href="/gallery/">Viewing Gallery</a></li><li aria-current="page">%s</li></ol></nav>\n'
      '<div class="section-head"><div><p class="eyebrow">The Week · Catch Up</p><h2>%s</h2><hr class="rule-gold"></div>'
      '<span class="tw-dateline">%s</span></div>\n'
      '<p class="tw-lede">Every show from this week in one place. Titles give nothing away and thumbnails blur until you hover, so you can catch up without getting spoiled. Pick a promotion, press play, and each clip opens with a link to where the full show streams.</p>\n'
      '%s\n<div class="cluster" style="gap:var(--sp-4);margin-top:var(--sp-5)">%s</div>\n</div>\n</section>'
      % (wk["label"], wk["label"], wk["label"], wk["label"].upper(), week_widget(wk), " ".join(nav))
    )
    title = "%s — Viewing Gallery | Wrestle Lore" % wk["label"]
    desc = "Catch up on %s: WWE, AEW, TNA and NXT highlights in one spoiler-safe viewing gallery, with links to where each show streams." % wk["label"]
    canonical = "https://wrestlelore.com/gallery/%s/" % wk["week"]
    return shell(title, desc, canonical, main)

def calendar_html(weeks):
    # month calendar for July 2026; days in a gallery week link to that week page
    week_by_monday = {}
    for wk in weeks:
        mon = wk["start"]
        for i in range(7):
            week_by_monday[(mon + datetime.timedelta(days=i))] = wk["week"]
    cal = calendar.Calendar(firstweekday=0)  # Monday first
    heads = "".join('<span class="cal-h">%s</span>' % d for d in ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
    cells = []
    for d in cal.itermonthdates(2026, 7):
        if d.month != 7:
            cells.append('<span class="cal-x"></span>'); continue
        wkid = week_by_monday.get(d)
        if wkid:
            cells.append('<a class="cal-d cal-d--on" href="/gallery/%s/">%d</a>' % (wkid, d.day))
        else:
            cells.append('<span class="cal-d">%d</span>' % d.day)
    return '<div class="cal"><div class="cal-grid cal-grid--head">%s</div><div class="cal-grid">%s</div><p class="cal-key">Gold dates have a viewing gallery. Pick a week to catch up.</p></div>' % (heads, "".join(cells))

def hub_page(weeks):
    cards = []
    for i, wk in enumerate(weeks):
        tag = "Latest" if i==0 else ""
        badge = ('<span class="gwk-badge">%s</span>' % tag) if tag else ""
        # count videos
        n = sum(len(v) for v in wk["promos"].values())
        cards.append(
          '<a class="gwk" href="/gallery/%s/">%s<span class="gwk-date">%s</span>'
          '<span class="gwk-meta">WWE · AEW · TNA · NXT — %d clips</span></a>'
          % (wk["week"], badge, wk["label"], n))
    main = (
      '<section class="section" aria-label="Viewing Gallery archive">\n<div class="wrap">\n'
      '<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li aria-current="page">Viewing Gallery</li></ol></nav>\n'
      '<div class="section-head"><div><p class="eyebrow">The Archive</p><h2>Viewing Gallery</h2><hr class="rule-gold"></div></div>\n'
      '<p class="tw-lede">Every week we round up WWE, AEW, TNA and NXT into one spoiler-safe gallery, then archive it here. New shows land through the week, so last week fills out while the new week begins. Pick a week on the calendar or from the list below.</p>\n'
      '%s\n<div class="gwk-list">%s</div>\n</div>\n</section>'
      % (calendar_html(weeks), "".join(cards))
    )
    return shell("Viewing Gallery — Weekly Wrestling Catch-Up Archive | Wrestle Lore",
                 "Browse the Wrestle Lore Viewing Gallery archive: weekly WWE, AEW, TNA and NXT highlights, spoiler-safe, with a calendar to jump to any week.",
                 "https://wrestlelore.com/gallery/", main)

def shell(title, desc, canonical, main):
    return (
      '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
      '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
      '<title>%s</title>\n<meta name="description" content="%s">\n'
      '<link rel="canonical" href="%s">\n<link rel="stylesheet" href="/css/site.css">\n</head>\n<body>\n'
      '<header class="site-header nav7"></header>\n<main id="main">\n%s\n</main>\n'
      '<footer class="site-footer site-footer--fat"></footer>\n'
      '<script src="/js/media.js" defer></script>\n</body>\n</html>\n'
      % (esc(title), esc(desc), canonical, main)
    )

def write(path, html):
    full = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(html)
    print("wrote", path)

if __name__ == "__main__":
    for i, wk in enumerate(WEEKS):
        nxt = WEEKS[i-1] if i>0 else None
        prv = WEEKS[i+1] if i+1 < len(WEEKS) else None
        write("/gallery/%s/index.html" % wk["week"], week_page(wk, prv, nxt))
    write("/gallery/index.html", hub_page(WEEKS))
    print("done:", len(WEEKS), "week pages + hub")
