#!/usr/bin/env python3
"""Lore Feed generator — the newsroom of Wrestle Lore.
ONE source (DISPATCHES) emits, all in sync:
  /lore-feed/                    -> hub: current-week editorial front page + browse-by-week index
  /lore-feed/<YYYY-MM-DD>/       -> one SEO/GEO page per Monday-week (recap + dispatches + schema)
  components/meganav.html        -> the site-wide ticker's .rt-item markup = the rolling last-7-days items
  css/site.css                   -> the .lf-* editorial styles (idempotent block)
  sitemap.xml                    -> +weekly URLs
Then run `python3 build/apply_shell.py` to stamp the ticker across all pages.
To add news: append ONE dict to DISPATCHES, rerun this, then apply_shell.py.
Weekly PAGES bucket Monday..Sunday; the TICKER is a rolling 7-day window from build day.
ROOT overridable: WL_ROOT=/path python3 build/build_lorefeed.py ; date via WL_TODAY=YYYY-MM-DD.
Also emits self-contained previews to /tmp for review (WL_PREVIEW_DIR).
"""
import os, re, datetime, html as _html

ROOT = os.environ.get("WL_ROOT", "/root/wwe")
BASE = "https://wrestlelore.com"
TODAY = datetime.date.fromisoformat(os.environ["WL_TODAY"]) if os.environ.get("WL_TODAY") else datetime.date.today()
PREVIEW_DIR = os.environ.get("WL_PREVIEW_DIR", "/tmp/lf-preview")

def esc(s): return _html.escape(str(s), quote=True)

# ------------------------------------------------------------------ DATA
# cat: title|event|signing|departure|return|business|media|roster|retirement|passing
# promo: wwe|nxt|aew|tna|njpw|tko|industry   official: True=promotion-confirmed, False=trade report
DISPATCHES = [
  dict(date="2026-07-28", promo="nxt", cat="return", official=False, who="Grayson Waller",
       hl="Grayson Waller crashes NXT, calls his shot at Tony D'Angelo",
       dek="A surprise return promo put the whole men's roster on notice and the NXT Championship squarely in his sights.",
       src="Sports Illustrated", url="https://www.si.com/fannation/wrestling/wwe/grayson-waller-drops-pipebomb-promo-on-austin-theory-new-day-others-in-nxt-return"),
  dict(date="2026-07-28", promo="nxt", cat="signing", official=False, who="Cruz Montana",
       hl="Mike Santana lands in NXT under a new name, Cruz Montana",
       dek="The former TNA and AEW standout arrives in WWE developmental with a ring name honoring his late father.",
       src="Fightful", url="https://www.fightful.com/podcasts/cruz-montana-fka-mike-santana-arrives-in-wwe-nxt-7-28-26-full-show-review-highlights/"),
  dict(date="2026-07-27", promo="wwe", cat="title", official=True, who="Raquel Rodriguez",
       hl="Raquel Rodriguez pins Sol Ruca for the Women's Intercontinental Title",
       dek="Her first singles championship in WWE comes on the SummerSlam go-home Raw.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/07/27/wwe-raw-7-27-results-raquel-rodriguez-wins-womens-intercontinental-title-roman-reigns-and-seth-rollins-face-off-on-summerslam-go-home-show/"),
  dict(date="2026-07-27", promo="tko", cat="business", official=True, who="Club WWE",
       hl="WWE opens the doors on Club WWE, a paid membership tier",
       dek="A 99-dollar-a-year program bundling a match-used welcome kit, exclusive merch, early ticket access and a premium library, live July 31.",
       src="WWE.com", url="https://corporate.wwe.com/about/news/2026/07-27-2026"),
  dict(date="2026-07-26", promo="aew", cat="event", official=True, who="Kenny Omega", lead=True, mono="Redemption",
       hl="Omega survives Redemption, then lights the fuse on All In",
       dek="Kenny Omega turned back The Jet, Kevin Knight, to keep the AEW World Championship, then turned on the man he now meets in London: Will Ospreay, fresh off walking out on the Death Riders the same night.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-redemption-results-july-26-2026"),
  dict(date="2026-07-26", promo="aew", cat="title", official=True, who="Willow Nightingale",
       hl="Willow Nightingale dethrones Thekla for the Women's World Title",
       dek="A career-defining win at Redemption sets up a marquee defense against Mercedes Mone at All In: London.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-redemption-results-july-26-2026"),
  dict(date="2026-07-26", promo="aew", cat="title", official=True, who="Maya World",
       hl="Maya World takes the TBS Championship from Hikaru Shida",
       dek="One of four title switches on a stacked Redemption card.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-redemption-results-july-26-2026"),
  dict(date="2026-07-26", promo="aew", cat="title", official=True, who="Andrade",
       hl="Andrade beats Mark Davis for the AEW National Championship",
       dek="Gold to show for the split from the Don Callis Family weeks earlier.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-redemption-results-july-26-2026"),
  dict(date="2026-07-25", promo="wwe", cat="roster", official=True, who="Cody Rhodes",
       hl="Cody Rhodes and CM Punk come face to face on SmackDown",
       dek="The SummerSlam card sharpens as champion and challenger share the ring.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-07-24"),
  dict(date="2026-07-25", promo="wwe", cat="roster", official=True, who="Gunther",
       hl="The Ring General leaves Nick Aldis laid out on SmackDown",
       dek="A contract signing turns physical, escalating Gunther's path into SummerSlam.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-07-24"),
  dict(date="2026-07-23", promo="tko", cat="media", official=True, who="WWE Radio",
       hl="WWE Radio goes 24/7 on SiriusXM channel 156",
       dek="Live premium-event coverage plus podcasts from Cody Rhodes, The Undertaker and Stephanie McMahon.",
       src="WWE.com", url="https://corporate.wwe.com/about/news/2026/07-23-2026"),
  dict(date="2026-07-23", promo="wwe", cat="business", official=True, who="Mattel",
       hl="Mattel and WWE bring Lucha Libre AAA to the toy aisle",
       dek="A multi-year global licensing deal puts an AAA figure line on shelves in fall 2027.",
       src="WWE.com", url="https://corporate.wwe.com/about/news/2026/07-23-2026-0"),
  dict(date="2026-07-23", promo="wwe", cat="business", official=False, who="Free agency",
       hl="A wave of released WWE names clears its non-competes",
       dek="Kofi Kingston, Sheamus, Xavier Woods, Zelina Vega and the Motor City Machine Guns are reported free to sign elsewhere.",
       src="Fightful", url="https://www.fightful.com/wrestling/former-wwe-superstars-officially-free-agents-after-90-day-non-competes-expire/"),
  dict(date="2026-07-20", promo="wwe", cat="return", official=False, who="Nikki Bella",
       hl="Nikki Bella says she has cleared testing at the Performance Center",
       dek="The update points toward an in-ring return following April ankle surgery.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/07/20/nikki-bella-provides-update-on-injury-says-she-visited-pc-recently-to-get-cleared/"),
  dict(date="2026-07-18", promo="wwe", cat="title", official=True, who="Fatal Influence",
       hl="Fatal Influence take the Women's Tag Titles at Saturday Night's Main Event",
       dek="Fallon Henley and Lainey Reid beat Paige and Brie Bella, with Jacy Jayne lending a hand.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/07/18/fatal-influence-wins-wwe-womens-tag-team-championships-at-saturday-nights-main-event/"),
  dict(date="2026-07-16", promo="industry", cat="passing", official=False, who="Siva Afi", memoriam=True,
       hl="Siva Superfly Afi, 1949 to 2026",
       dek="The Samoan veteran of the 1980s WWF, later a working stuntman, has died at 77.",
       src="F4WOnline", url="https://www.f4wonline.com/news/wwe/siva-afi-passes-away-at-77/"),
  dict(date="2026-07-14", promo="wwe", cat="media", official=True, who="ReelShort",
       hl="WWE and ReelShort greenlight a vertical microdrama series",
       dek="A live-action series starring Drew McIntyre, Jacob Fatu and Joe Hendry is set for early fall 2026.",
       src="WWE.com", url="https://corporate.wwe.com/about/news/2026/07-14-2026"),
  dict(date="2026-07-13", promo="wwe", cat="event", official=True, who="Roman Reigns",
       hl="Roman Reigns vs Seth Rollins is official for SummerSlam",
       dek="The World Heavyweight Title clash headlines two nights at U.S. Bank Stadium in Minneapolis.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-07-13/roman-reigns-and-seth-rollins"),
  dict(date="2026-07-08", promo="aew", cat="signing", official=True, who="Jack Perry",
       hl="Jack Perry re-signs with AEW",
       dek="A Dynamite: Beach Break vignette confirms one of the Four Pillars is staying put.",
       src="Wrestling Headlines", url="https://wrestlingheadlines.com/aew-news-jack-perry-re-signs-with-aew-new-title-matches-set-big-match-added-to-aew-redemption-more/"),
  dict(date="2026-07-08", promo="tna", cat="signing", official=False, who="Rich Swann",
       hl="Former World Champion Rich Swann re-ups with TNA",
       dek="A new deal keeps the eight-year mainstay in the fold ahead of Lockdown in Chicago.",
       src="Pro Wrestling Dot Net", url="https://prowrestling.net/site/2026/07/08/tna-re-signs-a-former-world-champion/"),
  dict(date="2026-07-08", promo="tko", cat="business", official=True, who="TKO",
       hl="TKO will report second-quarter results on August 3",
       dek="Numbers land after market close, with an investor call to follow at 5 p.m. ET.",
       src="TKO Group Holdings", url="https://investor.tkogrp.com/news/news-details/2026/TKO-to-Announce-Second-Quarter-2026-Results/default.aspx"),
  dict(date="2026-07-06", promo="wwe", cat="title", official=True, who="CM Punk",
       hl="CM Punk returns and takes the Undisputed WWE Title from Sami Zayn",
       dek="A surprise Raw main event flips the top of the card heading toward SummerSlam.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-07-06"),
  dict(date="2026-07-06", promo="wwe", cat="title", official=True, who="The Vision",
       hl="Bron Breakker and Austin Theory capture the World Tag Team Titles",
       dek="The Vision beat The Street Profits on Raw with a timely assist from Maxxine Dupri.",
       src="F4WOnline", url="https://www.f4wonline.com/news/wwe/the-vision-win-world-tag-team-titles-on-wwe-raw-after-surprise-outside-help/"),
  dict(date="2026-07-06", promo="aew", cat="departure", official=False, who="Jake Roberts",
       hl="Jake The Snake Roberts announces his AEW departure",
       dek="The Hall of Famer confirms the end of a run that began alongside Lance Archer in 2020.",
       src="Fightful", url="https://www.fightful.com/wrestling/jake-the-snake-roberts-announces-aew-departure/"),
  dict(date="2026-07-05", promo="wwe", cat="departure", official=False, who="Sheamus",
       hl="Sheamus is reported to be leaving WWE",
       dek="The Celtic Warrior declined a restructured extension, with his profile moved to alumni.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/07/05/report-sheamus-to-exit-wwe-after-rejecting-restructured-contract-extension/"),
  dict(date="2026-07-04", promo="njpw", cat="retirement", official=True, who="Tomoaki Honma",
       hl="Tomoaki Honma sets his retirement after 29 years",
       dek="Citing neck issues, the NJPW veteran plans a farewell match in 2027.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/07/04/njpws-tomoaki-honma-announces-he-is-to-retire/"),
  dict(date="2026-06-28", promo="tna", cat="title", official=False, who="Nic Nemeth",
       hl="Nic Nemeth wins the TNA World Title at Slammiversary",
       dek="The Call Your Shot trophy delivers a second TNA World Championship over Mike Santana in Boston.",
       src="Sports Illustrated", url="https://www.si.com/fannation/wrestling/tna/tna-slammiversary-results-new-world-champions-crowned-former-wwe-star-debuts"),
  dict(date="2026-06-28", promo="tna", cat="title", official=False, who="Xia Brookside",
       hl="Xia Brookside is the new TNA Knockouts World Champion",
       dek="A Slammiversary win over Lei Ying Lee crowns a new Knockouts titleholder.",
       src="Wrestling Headlines", url="https://wrestlingheadlines.com/another-title-change-takes-place-at-tna-slammiversary-2026/"),
  dict(date="2026-06-28", promo="tna", cat="signing", official=False, who="Uhaa Nation",
       hl="Apollo Crews arrives in TNA as Uhaa Nation",
       dek="The former WWE star debuts under his independent name after his contract expired.",
       src="Sports Illustrated", url="https://www.si.com/fannation/wrestling/tna/tna-slammiversary-results-new-world-champions-crowned-former-wwe-star-debuts"),
  dict(date="2026-06-28", promo="aew", cat="event", official=True, who="Owen Hart Cup",
       hl="Ospreay and Mone win the Owen Hart Cups at Forbidden Door",
       dek="Will Ospreay beat Swerve Strickland and Mercedes Mone downed Maya World in the tournament finals.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-x-njpw-forbidden-door-results-june-28-2026"),
  dict(date="2026-06-28", promo="njpw", cat="event", official=True, who="Shota Umino",
       hl="Shota Umino turns back PAC to keep the IWGP Global Title",
       dek="A Forbidden Door defense holds the line for the champion.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-x-njpw-forbidden-door-results-june-28-2026"),
  dict(date="2026-06-28", promo="aew", cat="return", official=True, who="Jay White",
       hl="Jay White makes a surprise Forbidden Door return",
       dek="He aids Adam Copeland and Christian Cage as the tag champions retain.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-x-njpw-forbidden-door-results-june-28-2026"),
  dict(date="2026-06-28", promo="nxt", cat="title", official=True, who="Kendal Grey",
       hl="Kendal Grey wins the NXT Women's Title at Great American Bash",
       dek="A main-event victory over Lola Vice crowns a new NXT Women's Champion.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/06/28/nxt-the-great-american-bash-2026-results-kendal-grey-wins-womens-title-tony-dangelo-zaria-and-myles-borne-retain/"),
  dict(date="2026-06-09", promo="nxt", cat="title", official=True, who="Zaria",
       hl="Zaria captures the NXT Women's North American Title",
       dek="A win over Tatum Paxley puts new gold around her waist.",
       src="F4WOnline", url="https://www.f4wonline.com/news/nxt/zaria-wins-wwe-nxt-womens-north-american-championship/"),
  dict(date="2026-06-08", promo="tko", cat="business", official=False, who="TKO",
       hl="A shareholder suit over the WWE-Endeavor merger settles before trial",
       dek="A Delaware settlement is reached days before a scheduled trial; terms were not disclosed.",
       src="ESPN", url="https://www.espn.com/wwe/story/_/id/49002375/mcmahon-secures-deal-suit-seeking-misconduct-documents"),
]

# ------------------------------------------------------------------ MAPS
CAT = {  # cat -> (label, css-accent-var)
  "title":("Title Change","--c-gold-bright"), "event":("Event","--c-red-bright"),
  "signing":("Signing","--c-win"), "departure":("Departure","--c-red"),
  "return":("Return","--c-focus"), "business":("Business","#b7c1d0"),
  "media":("Media","--c-media"), "roster":("Roster","--c-gold"),
  "retirement":("Retirement","#b7c1d0"), "passing":("In Memoriam","#9aa3ad"),
}
PROMO = {  # promo -> (label, css-color-var for spine/sq, dark-text?)
  "wwe":("WWE","--c-wwe",False), "nxt":("NXT","--c-nxt",True), "aew":("AEW","--c-aew",False),
  "tna":("TNA","--c-tna",False), "njpw":("NJPW","--c-njpw",False),
  "tko":("Business","--c-mens",False), "industry":("Industry","--c-mens",False),
}
MON = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
MONL = ["January","February","March","April","May","June","July","August","September","October","November","December"]

def d2date(s): return datetime.date.fromisoformat(s)
def monday(dt): return dt - datetime.timedelta(days=dt.weekday())
def wk_id(dt): return monday(dt).isoformat()
def wk_label(mon): return "Week of %s %d, %d" % (MONL[mon.month-1], mon.day, mon.year)
def short(dt): return "%s %d" % (MON[dt.month-1], dt.day)
def wk_range(mon):
    sun = mon + datetime.timedelta(days=6)
    if mon.month == sun.month:
        return "%s %d–%d, %d" % (MON[mon.month-1], mon.day, sun.day, mon.year)
    return "%s %d – %s %d, %d" % (MON[mon.month-1], mon.day, MON[sun.month-1], sun.day, sun.year)

for d in DISPATCHES:
    d["_dt"] = d2date(d["date"]); d["_wk"] = wk_id(d["_dt"])
DISPATCHES.sort(key=lambda d: d["_dt"], reverse=True)

# group into weeks (desc)
WEEKS = []  # list of (mon_date, [items])
_seen = {}
for d in DISPATCHES:
    _seen.setdefault(d["_wk"], []).append(d)
for wid in sorted(_seen.keys(), reverse=True):
    WEEKS.append((d2date(wid), _seen[wid]))

# ------------------------------------------------------------------ CARD RENDER
def card(d, lead=False):
    plabel, pvar, pdark = PROMO[d["promo"]]
    clabel, cvar = CAT[d["cat"]]
    tag = ('<span class="lf-tag lf-tag--official">Official</span>' if d["official"]
           else '<span class="lf-tag">Report</span>')
    memoriam = d.get("memoriam")
    kicker = ('<span class="lf-cat">%s</span>%s%s' %
              (esc(clabel),
               "" if memoriam else '<span class="lf-promo">%s</span>' % esc(plabel),
               tag))
    cls = "lf-item" + (" is-lead" if lead else "") + (" is-memoriam" if memoriam else "")
    pc_val = "var(%s)" % pvar
    kc_val = "var(%s)" % cvar if cvar.startswith("--") else cvar
    inner = ('<div class="lf-kicker">%s</div>'
             '<h3 class="lf-hl">%s</h3><p class="lf-dek">%s</p>'
             '<div class="lf-foot"><span class="lf-when" data-date="%s">%s</span><span class="lf-src">%s</span></div>'
             % (kicker, esc(d["hl"]), esc(d["dek"]), d["date"], short(d["_dt"]), esc(d["src"])))
    # A lead card is a 2-column grid (copy | art); the copy MUST be one wrapper element
    # so the art can be the single second child. Non-lead cards are single-column.
    if lead:
        inner = '<div class="lf-lead__copy">%s</div>' % inner
    return (
      '<article class="%s" data-date="%s" data-promo="%s" data-cat="%s" data-official="%d" '
      'data-headline="%s" style="--pc:%s;--kc:%s">'
      '<a class="lf-item__link" href="%s" target="_blank" rel="noopener">%s</a></article>'
      % (cls, d["date"], d["promo"], d["cat"], 1 if d["official"] else 0, esc(d["hl"]),
         pc_val, kc_val, esc(d["url"]), inner))

_LEAD_CAT = {"title":8,"event":7,"signing":5,"return":4,"departure":4,"business":3,"media":2,"roster":3,"retirement":2,"passing":0}
def _lead_score(d):
    return (100 if d.get("lead") else 0) + (10 if d["official"] else 0) + _LEAD_CAT.get(d["cat"], 1)

def feed_block(items):
    """Lead = biggest story (explicit flag > official title/event > newest); river = the rest, date-sorted."""
    cands = [d for d in items if not d.get("memoriam")] or items
    lead = max(cands, key=lambda d: (_lead_score(d), d["_dt"])) if cands else None
    out = []
    if lead:
        plabel, pvar, pdark = PROMO[lead["promo"]]
        art = ('<div class="lf-lead__art" style="--pc:var(%s)" data-mono="%s">'
               '<span class="lf-lead__badge">The Main Event</span></div>'
               % (pvar, esc(lead.get("mono", plabel))))
        # lead card: wrap copy + art
        c = card(lead, lead=True)
        c = c.replace('</a></article>', art + '</a></article>')
        out.append('<div class="lf-lead">%s</div>' % c)
    river = [d for d in items if d is not lead]
    if river:
        out.append('<div class="lf-river">%s</div>' % "".join(card(d) for d in river))
    return "\n".join(out)

# ------------------------------------------------------------------ WEEK RECAP (real, entity-rich copy)
def recap(items, mon):
    def by(c): return [d for d in items if d["cat"] == c]
    titles, sign, dep = by("title"), by("signing"), by("departure")
    events, biz = by("event"), by("business") + by("media")
    ret, pas, rost, retire = by("return"), by("passing"), by("roster"), by("retirement")
    n = len(items)
    parts = ["The week of %s logged %d dispatch%s across professional wrestling." %
             (wk_range(mon), n, "" if n == 1 else "es")]
    if titles:
        names = "; ".join(t["hl"] for t in titles[:6])
        parts.append("Championships moved: %s." % names)
    if sign:
        parts.append("On the roster front: %s." % "; ".join(s["hl"] for s in sign[:4]))
    if dep or retire:
        parts.append("Departures and farewells: %s." % "; ".join(x["hl"] for x in (dep + retire)[:4]))
    if biz:
        parts.append("Off screen, the business desk tracked: %s." % "; ".join(b["hl"] for b in biz[:4]))
    if events and not titles:
        parts.append("In the ring: %s." % "; ".join(e["hl"] for e in events[:3]))
    return " ".join(parts)

# ------------------------------------------------------------------ SHELL
def shell(title, desc, canonical, main, extra_head=""):
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
      '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
      '<title>%s</title>\n<meta name="description" content="%s">\n<link rel="canonical" href="%s">\n'
      '<meta name="robots" content="index,follow">\n'
      '<meta property="og:type" content="website">\n<meta property="og:title" content="%s">\n'
      '<meta property="og:description" content="%s">\n<meta property="og:url" content="%s">\n'
      '<meta property="og:site_name" content="Wrestle Lore">\n%s'
      '<link rel="stylesheet" href="/css/site.css">\n</head>\n<body>\n'
      '<header class="site-header nav7"></header>\n<main id="main">\n%s\n</main>\n'
      '<footer class="site-footer site-footer--fat"></footer>\n'
      '<script src="/js/media.js" defer></script>\n%s\n</body>\n</html>\n'
      % (esc(title), esc(desc), canonical, esc(title), esc(desc), canonical, extra_head, main, FEED_JS_TAG))

# masthead + control desk (shared by hub + week pages)
def masthead(kicker, big, dateline, edition, standfirst):
    return ('<header class="lf-mast">'
      '<div class="lf-mast__rule"><span>Wrestle Lore</span>'
      '<span class="mid">Results · Title Changes · Signings · The Business</span>'
      '<span>%s</span></div><hr class="lf-hairline">'
      '<h1 class="lf-logo"><span class="the">%s</span>%s</h1><hr class="lf-hairline">'
      '<div class="lf-mast__foot"><span class="lf-dateline">%s</span>'
      '<span class="lf-standfirst">%s</span><span class="lf-editions">%s</span></div></header>'
      % (esc(edition), esc(kicker), esc(big), esc(dateline), esc(standfirst), esc(edition)))

def desk():
    promos = [("all","All",""),("wwe","WWE","--c-wwe"),("nxt","NXT","--c-nxt"),("aew","AEW","--c-aew"),
              ("tna","TNA","--c-tna"),("njpw","NJPW","--c-njpw"),("tko","Business","--c-mens")]
    cats = [("all","All"),("title","Title Changes"),("event","Events"),("signing","Signings"),
            ("departure","Departures"),("return","Returns"),("business","Business"),("roster","Roster")]
    pc = "".join('<button class="lf-chip" data-val="%s" aria-pressed="%s"%s>%s%s</button>'
                 % (v,"true" if v=="all" else "false",
                    (' style="--chip:var(%s)"'%c) if c else "",
                    ('<span class="lf-chip__dot"></span>' if c else ""), esc(l)) for v,l,c in promos)
    cc = "".join('<button class="lf-chip" data-val="%s" aria-pressed="%s">%s</button>'
                 % (v,"true" if v=="all" else "false", esc(l)) for v,l in cats)
    return ('<div class="lf-desk"><div class="lf-desk__row">'
      '<label class="lf-search"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>'
      '<input id="lf-q" type="search" placeholder="Search this feed — a name, a title, a promotion" aria-label="Search" autocomplete="off"></label></div>'
      '<div class="lf-desk__row" style="margin-top:10px"><span class="lf-chiplabel">Promotion</span>'
      '<div class="lf-chiprow" data-facet="promo" style="width:auto;flex:1">%s</div></div>'
      '<div class="lf-desk__row" style="margin-top:8px"><span class="lf-chiplabel">Desk</span>'
      '<div class="lf-chiprow" data-facet="cat" style="width:auto;flex:1">%s</div></div></div>'
      '<p class="lf-count" id="lf-count"></p>' % (pc, cc))

COLOPHON = ('<p class="lf-colophon"><b>The Lore Feed</b> is the newsroom of Wrestle Lore. '
  'Dispatches are filed by hand from named outlets and carry an <b>Official</b> stamp when confirmed by a promotion, '
  'or <b>Report</b> when sourced from the trade press. Each week Monday through Sunday keeps its own page. '
  'Wrestle Lore is an independent, fan-made project and is not affiliated with WWE, TKO Group Holdings, AEW, TNA or NJPW.</p>')

# ------------------------------------------------------------------ WEEK SWITCHER
def week_switcher(current_mon):
    months = [m for m, _ in WEEKS]
    idx = months.index(current_mon) if current_mon in months else -1
    newer = months[idx-1] if idx > 0 else None
    older = months[idx+1] if 0 <= idx < len(months)-1 else None
    def navbtn(mon, label):
        if mon:
            return '<a class="lf-wb__nav" href="/lore-feed/%s/">%s</a>' % (mon.isoformat(), label)
        return '<span class="lf-wb__nav is-off">%s</span>' % label
    chips = []
    for mon, _ in WEEKS:
        cur = (mon == current_mon)
        chips.append('<a class="lf-wb__wk%s" href="/lore-feed/%s/"%s>%s</a>'
                     % (" is-cur" if cur else "", mon.isoformat(),
                        ' aria-current="page"' if cur else "", short(mon)))
    return ('<nav class="lf-weekbar" aria-label="Switch week">%s'
            '<div class="lf-wb__track">%s</div>%s</nav>'
            % (navbtn(newer, "Newer week"), "".join(chips), navbtn(older, "Older week")))

# ------------------------------------------------------------------ WEEK PAGE
def week_page(mon, items, older_mon, newer_mon):
    wid = mon.isoformat()
    label = wk_label(mon)
    title = "%s — WWE, AEW, TNA & NXT News | Wrestle Lore" % label
    desc = ("%s in professional wrestling: every title change, signing, result and business story across WWE, AEW, TNA, NXT and NJPW, dated and sourced." % label)
    canonical = "%s/lore-feed/%s/" % (BASE, wid)
    nav = []
    if newer_mon: nav.append('<a class="link-more" href="/lore-feed/%s/">Newer week</a>' % newer_mon.isoformat())
    nav.append('<a class="link-more" href="/lore-feed/">All weeks</a>')
    if older_mon: nav.append('<a class="link-more" href="/lore-feed/%s/">Older week</a>' % older_mon.isoformat())
    # JSON-LD: CollectionPage + ItemList + BreadcrumbList
    li = []
    for i, d in enumerate(items, 1):
        li.append('{"@type":"ListItem","position":%d,"name":"%s","url":"%s"}' % (i, esc(d["hl"]).replace('"','\\"'), esc(d["url"])))
    jsonld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage",'
      '"name":"%s","description":"%s","url":"%s","isPartOf":{"@type":"WebSite","name":"Wrestle Lore","url":"%s/"},'
      '"mainEntity":{"@type":"ItemList","numberOfItems":%d,"itemListElement":[%s]}}</script>\n'
      '<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
      '{"@type":"ListItem","position":1,"name":"Home","item":"%s/"},'
      '{"@type":"ListItem","position":2,"name":"Lore Feed","item":"%s/lore-feed/"},'
      '{"@type":"ListItem","position":3,"name":"%s","item":"%s"}]}</script>\n'
      % (esc(label), esc(desc), canonical, BASE, len(items), ",".join(li),
         BASE, BASE, esc(label), canonical))
    main = ('<div class="lf-wrap lf-wrap--week">'
      '<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li>'
      '<li><a href="/lore-feed/">Lore Feed</a></li><li aria-current="page">%s</li></ol></nav>'
      '%s'
      '%s%s'
      '<p class="lf-recap">%s</p>'
      '%s'
      '<div class="lf-weeknav">%s</div>%s</div>'
      % (esc(label), week_switcher(mon),
         masthead("The Week in Wrestling", label.replace("Week of ","Week of "), wk_range(mon),
                  "%d filed" % len(items), "Every result, title change, signing and passing, dated and sourced."),
         desk(), esc(recap(items, mon)), feed_block(items), " ".join(nav), COLOPHON))
    return shell(title, desc, canonical, main, extra_head=jsonld)

# ------------------------------------------------------------------ HUB PAGE
def week_index_card(mon, items):
    label = wk_label(mon)
    top = next((d for d in items if d.get("lead")), items[0])
    tallies = {}
    for d in items: tallies[d["cat"]] = tallies.get(d["cat"], 0) + 1
    chips = "".join('<span class="lf-wi__chip">%d %s</span>' % (n, CAT[c][0]) for c, n in
                    sorted(tallies.items(), key=lambda kv: -kv[1])[:3])
    return ('<a class="lf-wi" href="/lore-feed/%s/">'
      '<span class="lf-wi__k">%s</span><span class="lf-wi__n">%d dispatches</span>'
      '<span class="lf-wi__hl">%s</span><span class="lf-wi__chips">%s</span></a>'
      % (mon.isoformat(), esc(label), len(items), esc(top["hl"]), chips))

def hub_page(weeks):
    cur_mon, cur_items = weeks[0]
    title = "The Lore Feed — WWE, AEW, TNA & NXT News, Week by Week | Wrestle Lore"
    desc = ("The newsroom of Wrestle Lore: every title change, signing, result and business story across WWE, AEW, TNA, NXT and NJPW, filed weekly and archived by the week.")
    canonical = "%s/lore-feed/" % BASE
    dateline = "%s, %s %d, %d" % (["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][TODAY.weekday()],
                                  MONL[TODAY.month-1], TODAY.day, TODAY.year)
    li = []
    for i, (mon, items) in enumerate(weeks, 1):
        li.append('{"@type":"ListItem","position":%d,"name":"%s","url":"%s/lore-feed/%s/"}' %
                   (i, wk_label(mon), BASE, mon.isoformat()))
    jsonld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage",'
      '"name":"The Lore Feed","description":"%s","url":"%s","isPartOf":{"@type":"WebSite","name":"Wrestle Lore","url":"%s/"},'
      '"mainEntity":{"@type":"ItemList","name":"Weekly editions","numberOfItems":%d,"itemListElement":[%s]}}</script>\n'
      '<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
      '{"@type":"ListItem","position":1,"name":"Home","item":"%s/"},'
      '{"@type":"ListItem","position":2,"name":"Lore Feed","item":"%s"}]}</script>\n'
      % (esc(desc), canonical, BASE, len(weeks), ",".join(li), BASE, canonical))
    index = "".join(week_index_card(mon, items) for mon, items in weeks)
    main = ('<div class="lf-wrap">'
      '%s%s%s'
      '<div class="lf-dept"><span class="kk">// Front Page</span><h2>This Week</h2><span class="ln"></span>'
      '<a class="lf-dept__more" href="/lore-feed/%s/">Full week page</a></div>'
      '%s'
      '<div class="lf-dept"><span class="kk">// The Vault</span><h2>Browse by Week</h2><span class="ln"></span></div>'
      '<div class="lf-weekindex">%s</div>'
      '%s</div>'
      % (masthead("The Weekly", "Lore Feed", dateline, "Vol. I",
                  "Every result, title change, signing and passing across professional wrestling. Reported, dated, and filed."),
         desk(), week_switcher(cur_mon), cur_mon.isoformat(), feed_block(cur_items), index, COLOPHON))
    return shell(title, desc, canonical, main, extra_head=jsonld)

# ------------------------------------------------------------------ TICKER (rolling 7 days) -> meganav.html
def ticker_items(days=7, cap=8):
    cutoff = TODAY - datetime.timedelta(days=days)
    within = [d for d in DISPATCHES if d["_dt"] >= cutoff][:cap]
    if not within:  # never leave the ticker empty; fall back to newest
        within = DISPATCHES[:cap]
    return within

def ticker_markup():
    items = ticker_items()
    def sq(d):
        _, pvar, _ = PROMO[d["promo"]]
        return pvar
    lives = []
    for i, d in enumerate(items):
        lives.append('<a class="rt-item%s" href="%s" target="_blank" rel="noopener">'
          '<span class="rt-sq" style="background:var(%s)"></span>'
          '<span class="rt-name">%s</span><span class="rt-txt">%s</span>'
          '<span class="rt-t rf-time" datetime="%sT12:00:00Z">%s</span></a>'
          % (" is-on" if i == 0 else "", esc(d["url"]), sq(d), esc(d["who"]), esc(d["hl"]),
             d["date"], short(d["_dt"])))
    dots = "".join('<span class="rt-dot%s"></span>' % (" is-on" if i == 0 else "") for i in range(len(items)))
    live_svg = ('<span class="rt-live"><svg class="rt-live-mk" width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">'
      '<circle cx="16" cy="16" r="9.5" fill="none" stroke="#21e06a" stroke-width="0.9" opacity=".25"/>'
      '<circle cx="16" cy="16" r="4.4" fill="#21e06a"><animate attributeName="r" values="4.2;5.2;4.2" dur="2s" repeatCount="indefinite"/>'
      '<animate attributeName="opacity" values="1;.6;1" dur="2s" repeatCount="indefinite"/></circle>'
      '<circle cx="16" cy="16" r="2.1" fill="#8dffb9"/></svg></span>')
    return ('<div class="ticker7 rt" aria-label="Live wrestling headlines">\n'
      '  <div class="rt-tag">%sLIVE</div>\n'
      '  <div class="rt-stage">%s</div>\n'
      '  <div class="rt-dots" aria-hidden="true">%s</div>\n'
      '  <a class="rt-more" href="/lore-feed/">Lore Feed</a>\n'
      '</div>' % (live_svg, "".join(lives), dots))

def patch_meganav():
    p = os.path.join(ROOT, "components", "meganav.html")
    if not os.path.exists(p):
        print("!! meganav.html not found, skipping ticker patch"); return
    src = open(p, encoding="utf-8").read()
    new = ticker_markup()
    patched = re.sub(r'<div class="ticker7 rt".*?Lore Feed</a>\s*</div>', new, src, count=1, flags=re.S)
    if patched != src:
        open(p, "w", encoding="utf-8").write(patched)
        print("ticker patched into components/meganav.html (%d items, rolling 7d from %s)" % (len(ticker_items()), TODAY))
    else:
        print("!! ticker pattern not matched — check meganav.html")

# ------------------------------------------------------------------ CSS injection
def inject_css():
    p = os.path.join(ROOT, "css", "site.css")
    css = open(p, encoding="utf-8").read()
    block = "/* LOREFEED:START */\n" + LF_CSS + "\n/* LOREFEED:END */"
    if "/* LOREFEED:START */" in css:
        css = re.sub(r"/\* LOREFEED:START \*/.*?/\* LOREFEED:END \*/", block, css, flags=re.S)
    else:
        css = css.rstrip() + "\n\n" + block + "\n"
    open(p, "w", encoding="utf-8").write(css)
    print("css/site.css: LOREFEED block written")

# ------------------------------------------------------------------ sitemap
def update_sitemap():
    p = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(p): return
    xml = open(p, encoding="utf-8").read()
    urls = ["/lore-feed/"] + ["/lore-feed/%s/" % mon.isoformat() for mon, _ in WEEKS]
    add = ""
    for u in urls:
        loc = BASE + u
        if loc not in xml:
            add += '  <url><loc>%s</loc><changefreq>weekly</changefreq></url>\n' % loc
    if add:
        xml = xml.replace("</urlset>", add + "</urlset>")
        open(p, "w", encoding="utf-8").write(xml)
        print("sitemap +%d urls" % add.count("<url>"))

def write(path, htmlstr):
    full = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(htmlstr)

# ------------------------------------------------------------------ PREVIEW (self-contained)
def preview(path, htmlstr, style):
    os.makedirs(PREVIEW_DIR, exist_ok=True)
    h = htmlstr
    h = h.replace('<link rel="stylesheet" href="/css/site.css">', style)
    h = h.replace('<script src="/js/media.js" defer></script>', "")
    h = h.replace('<header class="site-header nav7"></header>',
                  '<header class="site-header nav7">%s<div class="pv-bar"><b>WRESTLE LORE</b><span>preview — brand fonts load from production</span></div></header>' % ticker_markup())
    h = h.replace('<footer class="site-footer site-footer--fat"></footer>', '')
    open(os.path.join(PREVIEW_DIR, path), "w", encoding="utf-8").write(h)

# ------------------------------------------------------------------ CSS + JS payloads
_here = os.path.dirname(os.path.abspath(__file__))
LF_CSS = open(os.path.join(_here, "lorefeed.css"), encoding="utf-8").read() if os.path.exists(os.path.join(_here, "lorefeed.css")) else ""
FEED_JS = open(os.path.join(_here, "lorefeed.js"), encoding="utf-8").read() if os.path.exists(os.path.join(_here, "lorefeed.js")) else ""
FEED_JS_TAG = "<script>%s</script>" % FEED_JS if FEED_JS else ""

PREVIEW_FONTS = """
@font-face{font-family:"Anton";font-display:swap;src:url("https://wrestlelore.com/fonts/anton-latin-400-normal.woff2") format("woff2");}
@font-face{font-family:"Oswald";font-weight:400;font-display:swap;src:url("https://wrestlelore.com/fonts/oswald-latin-400-normal.woff2") format("woff2");}
@font-face{font-family:"Oswald";font-weight:600;font-display:swap;src:url("https://wrestlelore.com/fonts/oswald-latin-600-normal.woff2") format("woff2");}
@font-face{font-family:"Oswald";font-weight:700;font-display:swap;src:url("https://wrestlelore.com/fonts/oswald-latin-700-normal.woff2") format("woff2");}
@font-face{font-family:"Inter";font-weight:400;font-display:swap;src:url("https://wrestlelore.com/fonts/inter-latin-400-normal.woff2") format("woff2");}
@font-face{font-family:"Inter";font-weight:600;font-display:swap;src:url("https://wrestlelore.com/fonts/inter-latin-600-normal.woff2") format("woff2");}
@font-face{font-family:"JetBrains Mono";font-weight:400;font-display:swap;src:url("https://wrestlelore.com/fonts/jetbrains-mono-latin-400-normal.woff2") format("woff2");}
"""
PREVIEW_TOKENS = """
:root{--c-bg:#0a0b0d;--c-bg-elev-1:#121418;--c-bg-elev-2:#1a1d23;--c-bg-elev-3:#23272f;
--c-line:#2b3038;--c-line-strong:#3a414c;--c-text:#e8eaed;--c-text-muted:#a2a9b4;--c-text-dim:#6b727d;
--c-gold:#d4af37;--c-gold-bright:#f2cc4b;--c-gold-dim:#8c7420;--c-red:#e11d2a;--c-red-bright:#ff3b48;
--c-win:#2fbf71;--c-focus:#5aa9ff;--c-media:#a855f7;--c-mens:#8593a6;
--c-wwe:#c8102e;--c-nxt:#f5c518;--c-tna:#1e73be;--c-njpw:#d81f26;--c-aew:#c8a24a;--line:#2b3038;--redb:#ff3b48;
--font-display:"Anton","Arial Narrow",sans-serif;--font-cond:"Oswald","Arial Narrow",sans-serif;
--font-body:"Inter",system-ui,Arial,sans-serif;--font-sans:var(--font-body);--font-mono:"JetBrains Mono",ui-monospace,Menlo,monospace;}
*{box-sizing:border-box;}
body{margin:0;background:var(--c-bg);color:var(--c-text);font-family:var(--font-body);font-size:16px;line-height:1.5;
background-image:radial-gradient(1200px 500px at 50% -8%,rgba(212,175,55,.05),transparent 60%);}
a{color:inherit;text-decoration:none;}::selection{background:var(--c-gold);color:#000;}
"""
TICKER_CSS = """
.ticker7{background:#000;border-bottom:1px solid var(--c-line);display:flex;align-items:stretch;height:38px;font-size:13px;}
.ticker7.rt{border-bottom:1px solid var(--c-line);}
.rt-tag{flex:0 0 auto;display:flex;align-items:center;gap:.55em;padding:0 16px;height:100%;font-family:var(--font-mono);font-size:10.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--c-text-muted);border-right:1px solid var(--c-line);white-space:nowrap;}
.rt-live{display:inline-flex;align-items:center;justify-content:center;width:16px;height:16px;flex:0 0 auto;}
.rt-live-mk{display:block;filter:drop-shadow(0 0 3px rgba(33,224,106,.85));}
.rt-stage{position:relative;flex:1;min-width:0;height:100%;}
.rt-item{position:absolute;inset:0;display:flex;align-items:center;gap:.75em;padding:0 22px;opacity:0;transition:opacity .6s ease;pointer-events:none;white-space:nowrap;}
.rt-item.is-on{opacity:1;pointer-events:auto;}
.rt-sq{width:7px;height:7px;border-radius:1px;flex:0 0 auto;}
.rt-name{font-family:var(--font-cond);text-transform:uppercase;letter-spacing:.06em;font-size:14px;color:var(--c-text);flex:0 0 auto;}
.rt-item:hover .rt-name{color:var(--c-gold-bright);}
.rt-txt{font-family:var(--font-body);font-size:13px;color:var(--c-text-muted);overflow:hidden;text-overflow:ellipsis;}
.rt-t{font-family:var(--font-mono);font-size:11px;color:var(--c-text-dim);margin-left:auto;flex:0 0 auto;padding-left:1em;letter-spacing:.03em;text-transform:uppercase;}
.rt-dots{flex:0 0 auto;display:flex;align-items:center;gap:5px;padding:0 15px;height:100%;border-left:1px solid var(--c-line);}
.rt-dot{width:5px;height:5px;border-radius:99px;background:var(--c-line-strong);}
.rt-dot.is-on{background:var(--c-gold);}
.rt-more{flex:0 0 auto;display:flex;align-items:center;height:100%;padding:0 16px;border-left:1px solid var(--c-line);font-family:var(--font-mono);font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--c-gold);white-space:nowrap;}
"""

def build_preview_style():
    return "<style>\n" + PREVIEW_FONTS + PREVIEW_TOKENS + TICKER_CSS + LF_CSS + "\n</style>"

# a tiny preview rotator so the ticker cycles in the standalone previews (prod uses js/nav.js)
PREVIEW_TICKER_JS = """<script>(function(){var s=document.querySelector('.rt-stage');if(!s)return;var it=[].slice.call(s.querySelectorAll('.rt-item')),d=[].slice.call(document.querySelectorAll('.rt-dot')),i=0;setInterval(function(){it[i].classList.remove('is-on');if(d[i])d[i].classList.remove('is-on');i=(i+1)%it.length;it[i].classList.add('is-on');if(d[i])d[i].classList.add('is-on');},3200);})();</script>"""

# ------------------------------------------------------------------ MAIN
if __name__ == "__main__":
    if not LF_CSS:
        raise SystemExit("build/lorefeed.css missing — write it first")
    # 1) real repo artifacts
    inject_css()
    for i, (mon, items) in enumerate(WEEKS):
        newer = WEEKS[i-1][0] if i > 0 else None
        older = WEEKS[i+1][0] if i < len(WEEKS)-1 else None
        write("/lore-feed/%s/index.html" % mon.isoformat(), week_page(mon, items, older, newer))
    write("/lore-feed/index.html", hub_page(WEEKS))
    patch_meganav()
    update_sitemap()
    # 2) self-contained previews (for review only; not committed)
    style = build_preview_style()
    cur_mon, cur_items = WEEKS[0]
    older = WEEKS[1][0] if len(WEEKS) > 1 else None
    preview("lore-feed-hub-preview.html", hub_page(WEEKS).replace(FEED_JS_TAG, FEED_JS_TAG + PREVIEW_TICKER_JS), style)
    preview("lore-feed-week-preview.html",
            week_page(cur_mon, cur_items, older, None).replace(FEED_JS_TAG, FEED_JS_TAG + PREVIEW_TICKER_JS), style)
    print("previews -> %s" % PREVIEW_DIR)
    print("weeks: %d  dispatches: %d  ticker(7d): %d" % (len(WEEKS), len(DISPATCHES), len(ticker_items())))
    print("done. now run: python3 build/apply_shell.py")
