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
# full creator names + show display names for the media-page one-card-per-show grid
CREATOR = {"WWE":"WWE","NXT":"WWE","AEW":"All Elite Wrestling","TNA":"TNA Wrestling","NJPW":"New Japan Pro-Wrestling","TKO":"WWE"}
SHOWNAME = {"Raw":"WWE Raw","NXT":"WWE NXT","Dynamite":"AEW Dynamite","iMPACT":"TNA iMPACT","SmackDown":"WWE SmackDown","Collision":"AEW Collision"}
SHOWORDER = ["Raw","NXT","Dynamite","iMPACT","SmackDown","Collision"]

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
  {"week":"2026-07-27","label":"Week of July 27, 2026","start":datetime.date(2026,7,27),"promos":{
     "WWE":[("mjkfX_uZUvk","2026-07-27","Raw · Full show highlights"),("--hLGjImq-0","2026-07-27","Raw · Top 10 moments"),("saKRhf4w5TE","2026-07-27","Raw · Reigns and Rollins faceoff"),("JbIeCIKWGyc","2026-07-27","Raw · Women's Intercontinental Title"),("-3a1GBuAXRc","2026-07-27","Raw · Bloodline six-man brawl")],
     "NXT":[("uue21lg-9ek","2026-07-28","NXT · Full show highlights"),("fjDZCSmQ--8","2026-07-28","NXT · North American Title"),("oEbR8Ycp5d0","2026-07-28","NXT · Lizzy Rain vs. Izzi Dame"),("N4VYaqhr8Ts","2026-07-28","NXT · Cruz Montana confrontation")]
  }},
  {"week":"2026-07-20","label":"Week of July 20, 2026","start":datetime.date(2026,7,20),"promos":{
     "WWE":[("4e_UUsgGk7I","2026-07-20","Raw · Full show highlights"),("PUvTijJM7jY","2026-07-20","Raw · Top 10 moments"),("RxI4yvWIuRU","2026-07-24","SmackDown · Full show highlights"),("yIvKS9Aub3M","2026-07-24","SmackDown · Top 10 moments")],
     "AEW":[("XFgrft96kQc","2026-07-22","Dynamite · TNT Championship"),("lKanl86PGZ8","2026-07-22","Dynamite · Women's Tag Title"),("p5ryAl5rFvI","2026-07-22","Dynamite · Tag team main event"),("C0FSDMJAHf0","2026-07-25","Collision · Main event scene")],
     "TNA":[("am_jSHkhRXM","2026-07-23","iMPACT · World Title main event"),("ciYpd4ysD8s","2026-07-23","iMPACT · Fallout"),("EbaTy6LvQ-4","2026-07-23","iMPACT · TV Title tournament")],
     "NXT":[("gt46FaNa18E","2026-07-21","NXT · Full show highlights"),("cB_XQGhra-c","2026-07-21","NXT · Title Street Fight"),("nFUnfdu326Q","2026-07-21","NXT · A new arrival"),("6BPO4g8oFFM","2026-07-21","NXT · Grudge match")]
  }},
  {"week":"2026-07-13","label":"Week of July 13, 2026","start":datetime.date(2026,7,13),"promos":{
     "WWE":[("F5MaGPEgNpk","2026-07-13","Raw · Full show highlights"),("HoY5Q2MEulU","2026-07-13","Raw · Top 10 moments"),("to3cS-GFBhw","2026-07-13","Raw · Evans vs. Dragon Lee gauntlet"),("f0fhFVG0S6Q","2026-07-17","SmackDown · Full show highlights"),("o1H6NTSLkTM","2026-07-17","SmackDown · Top 10 moments"),("X7QbBu7nc7M","2026-07-17","SmackDown · Four-way chaos")],
     "AEW":[("-RBTRrsa8wI","2026-07-15","Dynamite · Tag team match"),("H1UiQT5SewE","2026-07-15","Dynamite · Women's tag match"),("VgH9wRLzDis","2026-07-15","Dynamite · Fletcher vs. Komander title"),("N_d-5kFe_zE","2026-07-15","Dynamite · Main event"),("La3j1kfw60o","2026-07-15","Dynamite · Title celebration"),("aTgsJgs0kfw","2026-07-18","Collision · Singles match"),("WJ_-lFglkW4","2026-07-18","Collision · Backstage"),("1zqI39P6P1Y","2026-07-18","Collision · Ospreay vs. Brooks"),("-JwJ4m7-AtI","2026-07-18","Collision · Shida vs. Aminata title"),("llqGQlMwWf4","2026-07-18","Collision · Perry vs. Wayne")],
     "TNA":[("MufGdGZQ7DA","2026-07-16","iMPACT · X-Division Championship"),("ptlVuM7K09E","2026-07-16","iMPACT · TV Title tournament"),("xFyXTGKBLqg","2026-07-16","iMPACT · In-ring segment"),("qp8XCs-MHRI","2026-07-16","iMPACT · Backstage"),("wBcD3SJX7iY","2026-07-16","iMPACT · Heavyweight collision")],
     "NXT":[("0drmI0Tx5pA","2026-07-14","NXT · Full show highlights"),("D7XrmRr-TtU","2026-07-14","NXT · Top 10 moments"),("XRkOtmOderI","2026-07-14","NXT · Triple threat match"),("xbzzpgJG6RM","2026-07-14","NXT · Tag Team Championship")]
  }},
  {"week":"2026-07-06","label":"Week of July 6, 2026","start":datetime.date(2026,7,6),"promos":{
     "WWE":[("WLLhAIBGYes","2026-07-06","Raw · Full show highlights"),("CaO9NYMtf0Q","2026-07-06","Raw · Top 10 moments"),("oEC0G3EbTPA","2026-07-06","Raw · Punk def. Zayn for the title"),("CmYUhl_Sj40","2026-07-10","SmackDown · Full show highlights"),("7l1LecGUU0c","2026-07-10","SmackDown · Top 10 moments"),("9ByuFejfsOk","2026-07-10","SmackDown · Keys vs. Jimmy Uso")],
     "AEW":[("I3fnU7ZLh7Y","2026-07-08","Dynamite · Omega wins the AEW World Title"),("3G4Tjv9qkNw","2026-07-08","Dynamite · Fletcher vs. Takeshita"),("jffQcqkJETM","2026-07-08","Dynamite · Jericho vs. Ciampa"),("3m0YvB2Xmek","2026-07-11","Collision · Bailey vs. Davis title"),("XOM3ayF4hf8","2026-07-11","Collision · Moxley declares war")],
     "TNA":[("4uG-F-ldUc8","2026-07-09","iMPACT · Top 10 moments"),("rZzXdXzLIWo","2026-07-09","iMPACT · Lee vs. Brookside No DQ title"),("QgihHvX9b-E","2026-07-09","iMPACT · The Hardys defend the tag titles")],
     "NXT":[("_zoiUOqb3ug","2026-07-07","NXT · Full show highlights"),("N0nMHWH2SMQ","2026-07-07","NXT · Top 10 moments"),("nGp1OpcS8ao","2026-07-07","NXT · Armstrong runs wild")]
  }},
  {"week":"2026-06-29","label":"Week of June 29, 2026","start":datetime.date(2026,6,29),"promos":{
     "WWE":[("0uv4vcBggO0","2026-06-29","Raw · Full show highlights"),("azBRmfL4IqY","2026-06-29","Raw · Top 10 moments"),("REtZ4GF6hKQ","2026-06-29","Raw · Gable def. McDonagh"),("FTYASRcqDG0","2026-07-03","SmackDown · Full show highlights"),("IRhvYdhOgTM","2026-07-03","SmackDown · Top 10 moments"),("S5mZshIt-c0","2026-07-03","SmackDown · Cargill's team def. Flair's team")],
     "AEW":[("EPPJTMFjfuY","2026-07-01","Dynamite · The Switchblade era is back on"),("UgccIioF5F0","2026-07-01","Dynamite · Omega's deal with the Devil")],
     "TNA":[("FZe78ZgBjjE","2026-07-02","iMPACT · Top 10 moments"),("CLed_zO9WOc","2026-07-02","iMPACT · The future of TNA stands up")],
     "NXT":[("y8gsHGlD3EQ","2026-06-30","NXT · Full show highlights"),("ABk_DDRL244","2026-06-30","NXT · Top 10 moments"),("nYqlQZUcOqs","2026-06-30","NXT · The Kendal Grey era begins")]
  }},
  {"week":"2026-06-22","label":"Week of June 22, 2026","start":datetime.date(2026,6,22),"promos":{
     "WWE":[("mVj8KxC3ffE","2026-06-22","Raw · Full show highlights"),("M8pFl0QxCLE","2026-06-22","Raw · Top 10 moments"),("IK9fM1pVEpM","2026-06-22","Raw · Solo spikes Jimmy Uso"),("7Q6-eVp3fcc","2026-06-26","SmackDown · Full show highlights"),("FGVsRRFMV7I","2026-06-26","SmackDown · Top 10 moments"),("JLHDVfEv_3U","2026-06-26","SmackDown · Ricky Saints blasts Trick Williams")],
     "AEW":[("ZIQMzoD54eI","2026-06-24","Dynamite · Ospreay vs. ELP"),("ZT1rp-fqre4","2026-06-24","Dynamite · Omega vs. Zack Sabre Jr."),("jOPxaNjXNSE","2026-06-24","Dynamite · Briscoe stands tall vs. MJF"),("FZeg7sp6qgk","2026-06-27","Collision · The Conglomeration vs. The Opps"),("RbKHWzwmofA","2026-06-27","Collision · The Jet vs. Dezmond Xavier TNT Title")],
     "TNA":[("mCFOjYKvy2Q","2026-06-25","iMPACT · The Hardys before Slammiversary"),("YbR2GWTWpJM","2026-06-25","iMPACT · Ultimate X preview")],
     "NXT":[("FJ0qhyEUFJU","2026-06-23","NXT · Full show highlights"),("9Wu3BfrxNdM","2026-06-23","NXT · Top 10 moments"),("FckBMYW3klE","2026-06-23","NXT · Naraku's fireball")]
  }},
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
    active = [p for p in ORDER if wk["promos"].get(p)]  # skip promotions with no aired shows this week
    for i, promo in enumerate(active):
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

def media_thisweek_grid(wk):
    # One card per SHOW (the full-show highlight = first clip per show), in schedule
    # order, skipping shows that haven't aired. Matches the media page's .vgrid.tw-grid.
    byshow = {}
    for promo in ORDER:
        for (y,d,l) in wk["promos"].get(promo, []):
            show = l.split("·")[0].strip()
            if show not in byshow:
                byshow[show] = (promo,y,d,l)
    ordered = [s for s in SHOWORDER if s in byshow] + [s for s in byshow if s not in SHOWORDER]
    cards = []
    for show in ordered:
        promo,y,d,l = byshow[show]
        desc = l.split("·",1)[1].strip() if "·" in l else "Highlights"
        cre = CREATOR.get(promo,"WWE")
        href = page_url(promo,d,l)
        title = "%s, %s" % (SHOWNAME.get(show, show), pretty(d))
        cards.append(
          '<article class="vcard" data-wl-item>'
          '<div class="yt" data-yt-id="%s" data-yt-title="%s" data-yt-creator="%s" data-yt-page="%s">'
          '<a class="yt__link" href="%s">%s</a></div>'
          '<div class="vcard__body"><span class="telemetry"><b>%s</b></span>'
          '<h3 class="vcard__title">%s</h3>'
          '<div class="vcard__meta"><span class="vcard__creator">%s</span><span class="dot">&#8226;</span><span>%s</span></div>'
          '</div></article>'
          % (y, esc(title), esc(cre), href, href, esc(title), dayshort(d),
             esc(SHOWNAME.get(show, show)), esc(cre), esc(desc)))
    return '<div class="vgrid tw-grid">\n    %s\n  </div>' % "\n    ".join(cards)

def gallery_week_switcher(current_week):
    # Reuses the lore-feed .lf-weekbar styles (already in css/site.css) for consistent
    # week-to-week nav. Newer/Older + a chip per gallery week, current highlighted.
    idx = next((i for i,w in enumerate(WEEKS) if w["week"]==current_week), -1)
    newer = WEEKS[idx-1] if idx>0 else None
    older = WEEKS[idx+1] if 0<=idx<len(WEEKS)-1 else None
    def navbtn(w,label):
        if w: return '<a class="lf-wb__nav" href="/gallery/%s/">%s</a>' % (w["week"],label)
        return '<span class="lf-wb__nav is-off">%s</span>' % label
    chips = []
    for w in WEEKS:
        cur = (w["week"]==current_week)
        short = datetime.date.fromisoformat(w["week"]).strftime("%b %-d")
        chips.append('<a class="lf-wb__wk%s" href="/gallery/%s/"%s>%s</a>'
                     % (" is-cur" if cur else "", w["week"], ' aria-current="page"' if cur else "", short))
    return ('<nav class="lf-weekbar" aria-label="Switch week">%s'
            '<div class="lf-wb__track">%s</div>%s</nav>'
            % (navbtn(newer,"Newer week"), "".join(chips), navbtn(older,"Older week")))

def week_page(wk, older, newer):
    nav = []
    if newer: nav.append('<a class="link-more" href="/gallery/%s/">Newer week</a>' % newer["week"])
    nav.append('<a class="link-more" href="/gallery/">All weeks</a>')
    if older: nav.append('<a class="link-more" href="/gallery/%s/">Older week</a>' % older["week"])
    main = ('<section class="section thisweek" aria-label="%s">\n<div class="wrap">\n'
      '<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/gallery/">Viewing Gallery</a></li><li aria-current="page">%s</li></ol></nav>\n'
      '%s\n'
      '<div class="section-head"><div><p class="eyebrow">The Week · Catch Up</p><h2>%s</h2><hr class="rule-gold"></div><span class="tw-dateline">%s</span></div>\n'
      '<p class="tw-lede">Every show from this week in one place. Titles give nothing away and thumbnails blur until you hover, so you can catch up without getting spoiled. Pick a promotion, press play, and each clip opens with a link to where the full show streams.</p>\n'
      '%s\n<div class="cluster" style="gap:var(--sp-4);margin-top:var(--sp-5)">%s</div>\n</div>\n</section>'
      % (wk["label"],wk["label"],gallery_week_switcher(wk["week"]),wk["label"],wk["label"].upper(),week_widget(wk)," ".join(nav)))
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
    rel_html = "\n            ".join(rel)
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
  ("Is the wrestling recap spoiler-safe?",
   "Yes. Clip titles give nothing away, and a one-tap Spoilers control lets you hide thumbnails if you are catching up late, so you can pick a week and press play without results jumping out at you."),
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

# ---- media section sub-nav (section-scoped, generated; shell contract intact) ----
SUBNAV = [
  ("This Week",    "/gallery/",          "week"),
  ("Shows",        "/media/",            "/media/"),
  ("By Promotion", "/promotions/",       "/promotions/"),
  ("Moments",      "/moments/",          "/moments/"),
  ("Interviews",   "/media/interviews/", "/media/interviews/"),
]
def subnav(active):
    lis = "".join('<li><a href="%s"%s>%s</a></li>' % (h, ' aria-current="page"' if k==active else "", esc(l))
                  for (l, h, k) in SUBNAV)
    return ('<nav class="wl-subnav" aria-label="Media sections"><div class="wrap wl-subnav__inner">'
            '<span class="wl-subnav__tag">MEDIA // DESK</span><ul class="wl-subnav__list">%s</ul></div></nav>\n' % lis)

def latest_by_promo(weeks, promo, n=8):
    out = []
    for wk in weeks:
        for (y, d, l) in wk["promos"].get(promo, []):
            out.append((promo, y, d, l))
            if len(out) >= n: return out
    return out

def gv_rail(title, kk, clips, more_href=None, more_label=None):
    if not clips: return ""
    cards = "".join(facade_card(p, y, d, l) for (p, y, d, l) in clips)
    more = ('<a class="gv-more" href="%s">%s</a>' % (more_href, esc(more_label))) if more_href else ""
    return ('<section class="gv-sec" aria-label="%s"><div class="gv-sec__head"><div>'
            '<span class="gv-sec__kk">%s</span><h2>%s</h2></div>%s</div>'
            '<ul class="tw-rail">%s</ul></section>\n' % (esc(title), esc(kk), esc(title), more, cards))

def gv_hero(wk):
    first = None
    for p in ORDER:
        if wk["promos"].get(p):
            y, d, l = wk["promos"][p][0]; first = (p, y, d, l); break
    if not first: return ""
    p, y, d, l = first
    show = l.split("·")[0].strip()
    net, _ = shownet(l)
    href = page_url(p, d, l)
    desc = l.split("·", 1)[1].strip() if "·" in l else "Highlights"
    return ('<section class="gv-hero">'
      '<div class="yt gv-hero__art" data-yt-id="%s" data-yt-title="%s" data-yt-creator="%s" data-yt-page="%s">'
      '<a class="yt__link" href="%s">%s</a><span class="gv-hero__tag">Just aired // %s</span></div>'
      '<div class="gv-hero__meta"><span class="gv-sec__kk">Featured this week</span>'
      '<h2 class="gv-hero__h">%s</h2><p class="gv-hero__sub">%s · %s · %s</p>'
      '<a class="gv-hero__cta" href="%s">Press play to watch here, spoiler-safe</a></div></section>\n'
      % (y, esc(vtitle(p, l, d)), esc(CREATOR.get(p, "WWE")), href, href, esc(l), dayshort(d),
         esc(SHOWNAME.get(show, show)), esc(desc), esc(net), dayshort(d), href))

def hub_page(weeks):
    wk0 = weeks[0]
    # New this week (WEEKS[0], all aired promos)
    ntw = [(p, y, d, l) for p in ORDER for (y, d, l) in wk0["promos"].get(p, [])]
    new_row = gv_rail("New this week", "Just aired // %s" % wk0["label"], ntw)
    # Per-promotion latest rails (cross-week) so WWE, AEW, TNA and NXT always show
    promo_rows = ""
    for p in ORDER:
        promo_rows += gv_rail("%s highlights" % p, "Catch up // %s" % p,
                              latest_by_promo(weeks, p, 8), "/gallery/%s/" % wk0["week"], "See the week")
    # Browse-by-week index
    cards = []
    for i, wk in enumerate(weeks):
        badge = '<span class="gwk-badge">Latest</span>' if i==0 else ""
        n = sum(len(v) for v in wk["promos"].values())
        cards.append('<a class="gwk" href="/gallery/%s/">%s<span class="gwk-date">%s</span><span class="gwk-meta">%d clips</span></a>' % (wk["week"], badge, wk["label"], n))
    faq_html = "".join('<div class="gfaq__item"><h3>%s</h3><p>%s</p></div>' % (esc(q), esc(a)) for q, a in FAQS)
    main = (subnav("week")
      + '<section class="section" aria-label="This Week in Wrestling">\n<div class="wrap">\n'
      '<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li aria-current="page">This Week in Wrestling</li></ol></nav>\n'
      '<div class="gv-mast"><p class="eyebrow">Weekly recap · Updated nightly</p><h1>This Week in Wrestling</h1>'
      '<p class="gv-mast__sub">Every WWE, AEW, TNA and NXT show in one place. Spoiler-safe highlights, what aired each night, and where to stream it.</p></div>\n'
      + gv_hero(wk0) + new_row + promo_rows
      + '<section class="gv-sec" id="schedule" aria-label="Weekly TV schedule"><div class="gv-sec__head"><div>'
        '<span class="gv-sec__kk">When to tune in</span><h2>The wrestling week</h2></div></div>'
      + LEGEND + calendar_html(weeks) + '</section>\n'
      + '<section class="gv-sec" id="archive" aria-label="Browse by week"><div class="gv-sec__head"><div>'
        '<span class="gv-sec__kk">The vault</span><h2>Browse by week</h2></div></div>'
        '<div class="gwk-list">%s</div></section>\n' % "".join(cards)
      + '<div class="gfaq"><h2>Wrestling recap FAQ</h2>%s</div>\n' % faq_html
      + '</div>\n</section>')
    title = "This Week in Wrestling: WWE, AEW, TNA and NXT Recaps and Highlights | Wrestle Lore"
    desc = ("Your weekly wrestling recap hub. Spoiler-safe highlights for WWE Raw, SmackDown and NXT, AEW Dynamite and Collision, and TNA iMPACT, plus what aired each night and where to stream every show.")
    hero_id = ntw[0][1] if ntw else "mjkfX_uZUvk"
    og = {"image": "https://i.ytimg.com/vi/%s/hqdefault.jpg" % hero_id}
    return shell(title, desc, "%s/gallery/" % BASE, main, extra_head=hub_jsonld(weeks), og=og)

def shell(title, desc, canonical, main, extra_head="", og=None):
    if og:
        extra_head += (
          '<meta property="og:type" content="website"><meta property="og:site_name" content="Wrestle Lore">'
          '<meta property="og:title" content="%s"><meta property="og:description" content="%s">'
          '<meta property="og:url" content="%s"><meta property="og:image" content="%s">'
          '<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="%s">'
          '<meta name="twitter:image" content="%s">'
          '<meta name="robots" content="index,follow,max-image-preview:large,max-video-preview:-1">'
          % (esc(title), esc(desc), canonical, og["image"], esc(title), og["image"]))
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n'
      '<title>%s</title>\n<meta name="description" content="%s">\n<link rel="canonical" href="%s">\n%s<link rel="stylesheet" href="/css/site.css">\n</head>\n<body>\n'
      '<header class="site-header nav7"></header>\n<main id="main">\n%s\n</main>\n<footer class="site-footer site-footer--fat"></footer>\n'
      '<script src="/js/media.js" defer></script>\n</body>\n</html>\n' % (esc(title),esc(desc),canonical,extra_head,main))

def write(path, html):
    full = os.path.join(ROOT, path.lstrip("/")); os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full,"w",encoding="utf-8").write(html)

def patch_thisweek_file(path):
    # Single source of truth: ANY page carrying <!-- TW:START --> ... <!-- TW:END -->
    # markers gets its This-Week block regenerated from WEEKS[0]. Marker style:
    #   <!-- TW:START -->        -> homepage master-detail widget (week_widget)
    #   <!-- TW:START:grid -->   -> media one-card-per-show grid (media_thisweek_grid)
    # so the homepage, the media page, and the gallery all draw from the one WEEKS list.
    if not os.path.exists(path): return
    html = open(path,encoding="utf-8").read(); orig = html
    wk = WEEKS[0]
    def repl(m):
        raw = m.group(1) or ""
        if "grid" in raw:
            tag, inner = "<!-- TW:START:grid -->", media_thisweek_grid(wk)
        else:
            tag = "<!-- TW:START (generated from build/build_gallery.py WEEKS[0] — do not hand-edit) -->"
            inner = week_widget(wk)
        return "%s\n      %s\n      <!-- TW:END -->" % (tag, inner)
    html = re.sub(r"<!-- TW:START(:grid| [^>]*)? -->.*?<!-- TW:END -->", repl, html, flags=re.S)
    html = re.sub(r'<span class="tw-dateline">[^<]*</span>',
                  '<span class="tw-dateline">%s</span>' % wk["label"], html)
    if html != orig:
        open(path,"w",encoding="utf-8").write(html)
        print("regenerated This-Week block(s) from WEEKS[0] (%s) in %s" % (wk["week"], os.path.basename(path)))

def patch_homepage():
    # Patch every site page that hosts a This-Week block from the single WEEKS source.
    for rel in ("index.html", "media/index.html"):
        patch_thisweek_file(os.path.join(ROOT, rel))

def update_sitemap():
    p = os.path.join(ROOT,"sitemap.xml"); xml = open(p,encoding="utf-8").read()
    urls = ["/gallery/"] + ["/gallery/%s/" % wk["week"] for wk in WEEKS] + [info["url"] for info in INDEX.values()]
    add = ""
    for u in urls:
        loc = BASE + u
        if loc not in xml: add += '  <url><loc>%s</loc><changefreq>weekly</changefreq></url>\n' % loc
    if add:
        xml = xml.replace("</urlset>", add + "</urlset>"); open(p,"w",encoding="utf-8").write(xml); print("sitemap +%d urls" % add.count("<url>"))

# ==================== V2 APP PAGES (hub + per-week static SEO pages) ====================
APP_TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gallery_app.html")

def weeks_json():
    data=[]
    for i,w in enumerate(WEEKS):
        data.append({"week":w["week"],"label":w["label"],"start":w["week"],"live":(i==0),
                     "promos":{p:[list(c) for c in w["promos"][p]] for p in ORDER if w["promos"].get(p)}})
    return json.dumps(data, ensure_ascii=False)

def wk_span(wk):
    a=datetime.date.fromisoformat(wk["week"]); b=a+datetime.timedelta(days=6)
    if a.month==b.month: return "%s %d to %d, %d" % (a.strftime("%B"), a.day, b.day, a.year)
    return "%s %d to %s %d, %d" % (a.strftime("%B"), a.day, b.strftime("%B"), b.day, b.year)

def app_jsonld(wk, canonical, is_hub):
    vids=[]
    pos=1
    for p in ORDER:
        for (y,d,l) in wk["promos"].get(p,[]):
            show=l.split("\u00b7")[0].strip() if "\u00b7" in l else l.split("·")[0].strip()
            vids.append({"@type":"ListItem","position":pos,"item":{"@type":"VideoObject",
              "name":vtitle(p,l,d),"description":"Official %s highlight from %s." % (SHOWNAME.get(show,show), pretty(d)),
              "thumbnailUrl":"https://i.ytimg.com/vi/%s/hqdefault.jpg" % y,"uploadDate":d,
              "embedUrl":"https://www.youtube-nocookie.com/embed/%s" % y,
              "contentUrl":"https://www.youtube.com/watch?v=%s" % y,
              "publisher":{"@type":"Organization","name":"Wrestle Lore","url":BASE+"/"}}}); pos+=1
    name = "This Week in Wrestling" if is_hub else "Wrestling recaps, %s" % wk_span(wk)
    coll={"@context":"https://schema.org","@type":"CollectionPage","name":name,"url":canonical,
          "description":"Spoiler-safe WWE, AEW, TNA and NXT highlights for %s." % wk["label"],
          "mainEntity":{"@type":"ItemList","numberOfItems":len(vids),"itemListElement":vids}}
    crumbs={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Home","item":BASE+"/"},
      {"@type":"ListItem","position":2,"name":"This Week in Wrestling","item":BASE+"/gallery/"}]}
    if not is_hub:
        crumbs["itemListElement"].append({"@type":"ListItem","position":3,"name":wk["label"],"item":canonical})
    aired=sorted({(l.split("·")[0].strip(), d) for p in ORDER for (y,d,l) in wk["promos"].get(p,[])}, key=lambda t:t[1])
    faq=[{"@type":"Question","name":"What wrestling highlights are in the %s recap?" % wk["label"].lower(),
          "acceptedAnswer":{"@type":"Answer","text":"Official highlights from %s, all embedded from each promotion's official channel." % (", ".join("%s (%s)" % (SHOWNAME.get(s,s), pretty(d)) for s,d in aired) or "the week's shows")}},
         {"@type":"Question","name":"Where can I stream WWE, AEW, TNA and NXT this week?",
          "acceptedAnswer":{"@type":"Answer","text":"WWE Raw streams on Netflix, SmackDown on Peacock, NXT airs on The CW, AEW Dynamite and Collision stream on HBO Max, and TNA iMPACT streams on AMC+."}}]
    faqpage={"@context":"https://schema.org","@type":"FAQPage","mainEntity":faq}
    return "".join('<script type="application/ld+json">%s</script>' % json.dumps(x, ensure_ascii=False) for x in (coll,crumbs,faqpage))

def app_head_extra(wk, i, canonical, is_hub, title, desc):
    hero=None
    for p in ORDER:
        if wk["promos"].get(p): hero=wk["promos"][p][0][0]; break
    img="https://i.ytimg.com/vi/%s/hqdefault.jpg" % (hero or "mjkfX_uZUvk")
    h=('<link rel="canonical" href="%s">'
       '<meta property="og:type" content="website"><meta property="og:site_name" content="Wrestle Lore">'
       '<meta property="og:title" content="%s"><meta property="og:description" content="%s">'
       '<meta property="og:url" content="%s"><meta property="og:image" content="%s">'
       '<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="%s"><meta name="twitter:image" content="%s">'
       '<meta name="robots" content="index,follow,max-image-preview:large,max-video-preview:-1">'
       % (canonical, esc(title), esc(desc), canonical, img, esc(title), img))
    if i>0: h+='<link rel="prev" href="%s/gallery/%s/">' % (BASE, WEEKS[i-1]["week"])
    if i+1<len(WEEKS): h+='<link rel="next" href="%s/gallery/%s/">' % (BASE, WEEKS[i+1]["week"])
    return h+app_jsonld(wk, canonical, is_hub)+"\n"

def app_backbone(wk, i, is_hub):
    # Crawlable server-rendered content; the client app replaces it on load.
    h1 = "This Week in Wrestling" if is_hub else "This Week in Wrestling: %s" % wk_span(wk)
    aired=[]
    for p in ORDER:
        for (y,d,l) in wk["promos"].get(p,[]):
            show=l.split("·")[0].strip(); aired.append((d,show,p,y,l))
    aired.sort()
    shows_seen=[]
    for d,show,p,y,l in aired:
        if (show,d) not in shows_seen: shows_seen.append((show,d))
    intro=("Every WWE, AEW, TNA and NXT show from %s in one place: official, spoiler-safe highlights, what aired each night, and where to stream it. "
           % wk["label"].lower())
    if shows_seen:
        intro+="This week so far: "+", ".join("%s on %s" % (SHOWNAME.get(s,s), pretty(d)) for s,d in shows_seen)+"."
    out=['<div class="gv-mast"><p class="eyebrow">Weekly recap · Updated nightly</p><h1>%s</h1><p class="gv-mast__sub">%s</p></div>' % (esc(h1), esc(intro))]
    cur=None
    for d,show,p,y,l in aired:
        if (show,d)!=cur:
            if cur: out.append("</ul></section>")
            net,_=shownet(l)
            out.append('<section class="gv-sec"><h2>%s, %s</h2><p class="telemetry" style="font-size:10px">STREAMS ON %s</p><ul class="tw-rail">' % (esc(SHOWNAME.get(show,show)), pretty(d), esc(net.upper())))
            cur=(show,d)
        out.append(facade_card(p,y,d,l))
    if cur: out.append("</ul></section>")
    links=['<a href="/gallery/%s/">%s</a>' % (w["week"], w["label"]) for w in WEEKS]
    out.append('<nav class="gv-sec" aria-label="All recap weeks"><h2>Browse every week</h2><p>%s</p><p><a href="/lore-feed/%s/">Read the written news recap for this week</a></p></nav>' % (" · ".join(links), wk["week"]))
    return "\n".join(out)

def app_page(i, is_hub):
    wk=WEEKS[i]
    canonical = BASE+"/gallery/" if is_hub else "%s/gallery/%s/" % (BASE, wk["week"])
    if is_hub:
        title="This Week in Wrestling: WWE, AEW, TNA and NXT Recaps and Highlights | Wrestle Lore"
        desc=("Your weekly wrestling recap hub. Spoiler-safe official highlights for WWE Raw, SmackDown and NXT, AEW Dynamite and Collision, and TNA iMPACT, plus what airs each night and where to stream it.")
        crumb="This Week"
    else:
        title="WWE, AEW, TNA and NXT Recaps: %s | Wrestle Lore" % wk["label"]
        desc=("Spoiler-safe wrestling recap for %s: official highlights from Raw, NXT, Dynamite, iMPACT, SmackDown and Collision as they air, with streaming homes for every show." % wk["label"].lower())
        crumb=wk["label"]
    t=open(APP_TEMPLATE_PATH,encoding="utf-8").read()
    t=t.replace("{{TITLE}}",esc(title)).replace("{{DESC}}",esc(desc)).replace("{{CRUMB}}",esc(crumb))
    t=t.replace("{{HEAD_EXTRA}}",app_head_extra(wk,i,canonical,is_hub,title,desc))
    t=t.replace("{{SUBNAV}}",subnav("week"))
    t=t.replace("{{WEEKS_JSON}}",weeks_json())
    t=t.replace("{{INIT_WEEK}}",str(i))
    t=t.replace("{{BACKBONE}}",app_backbone(wk,i,is_hub))
    return t
# ==================== END V2 APP PAGES ====================

if __name__ == "__main__":
    nv = 0
    for wk in WEEKS:
        for promo in ORDER:
            for (y,d,l) in wk["promos"].get(promo, []):
                write("/media/w/%s/index.html" % slug(promo,d,l), video_page(promo,y,d,l,wk)); nv += 1
    for i, wk in enumerate(WEEKS):
        newer = WEEKS[i-1] if i>0 else None; older = WEEKS[i+1] if i+1<len(WEEKS) else None
        write("/gallery/%s/index.html" % wk["week"], app_page(i, False))
    write("/gallery/index.html", app_page(0, True))
    patch_homepage(); update_sitemap()
    print("done: %d video pages + %d week pages + hub (ROOT=%s)" % (nv, len(WEEKS), ROOT))
