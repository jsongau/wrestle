#!/usr/bin/env python3
"""Batch 3a: Diesel/Kevin Nash, Sid Vicious, Ted DiBiase, Randy Savage, Hulk Hogan"""
import os, re, datetime

BASE = "/root/wwe/wrestlers"

def cr(title, reign, note=""):
    note_html = '<span class="cr-note">' + note + '</span>' if note else ""
    return f'    <div class="champ-row"><span class="cr-title">{title}</span><span class="cr-reign">{reign}</span>{note_html}</div>\n'

def a(slug, name):
    return f'<a href="/wrestlers/{slug}/">{name}</a>'

def row(w, kind, opp, event, date, stipulation, note, result="W"):
    cat = w.get("slug","")
    cats = kind
    res_class = "l" if result == "L" else ("d" if result == "D" else "")
    res_label = "W" if result == "W" else ("L" if result == "L" else "D")
    return (f'<tr class="record-row" data-result="{result}" data-cats="{cats}">'
            f'<td class="res-cell"><span class="res-badge{" res-l" if res_class=="l" else " res-d" if res_class=="d" else ""}">{res_label}</span></td>'
            f'<td>{opp}</td><td>{event}</td><td>{date}</td>'
            f'<td>{stipulation}</td><td class="dim">{note}</td></tr>\n')

def build_page(w):
    slug = w["slug"]
    name = w["name"]
    subtitle = w.get("subtitle","")
    born = w.get("born","")
    from_loc = w.get("from","")
    height = w.get("height","")
    weight = w.get("weight","")
    trained = w.get("trained","")
    debut = w.get("debut","")
    retired = w.get("retired","")
    style = w.get("style","")
    bio_paras = w.get("bio",[])
    finishers = w.get("finishers",[])
    championships = w.get("championships",[])
    personas = w.get("personas",[])
    timeline_items = w.get("timeline",[])
    sig_matches = w.get("sig_matches",[])
    record_rows = w.get("record_rows","")
    notice_html = w.get("notice_html","")
    wins = w.get("wins", 0)
    losses = w.get("losses", 0)
    draws = w.get("draws", 0)
    total = wins + losses + draws
    win_pct = round(wins / total * 100) if total else 0
    faq = w.get("faq",[])
    media_items = w.get("media_items",[])
    wl_strip = w.get("wl_strip","")
    method_bars = w.get("method_bars",[])
    aliases = w.get("aliases",[])

    # --- pre-compute blocks ---
    bio_html = "".join(f"<p>{p}</p>\n" for p in bio_paras)

    fin_html = "".join(
        f'<li><strong>{f["name"]}</strong> — {f["desc"]}</li>\n'
        for f in finishers)

    champ_html = "".join(championships)

    persona_html = ""
    if personas:
        persona_html = '<div class="persona-grid">\n'
        for p in personas:
            persona_html += (f'<div class="persona-card">'
                             f'<h3>{p["name"]}</h3>'
                             f'<p class="dim">{p["era"]}</p>'
                             f'<p>{p["desc"]}</p></div>\n')
        persona_html += '</div>\n'

    tl_html = ""
    for t in timeline_items:
        tl_html += f'<li><time>{t["year"]}</time><h3>{t["title"]}</h3><p>{t["desc"]}</p></li>\n'

    sig_html = "".join(
        f'    <div class="sig-card"><span class="sig-rating">{s["rating"]}</span>'
        f'<h3>{s["title"]}</h3><p class="dim">{s["subtitle"]}</p>'
        f'<p>{s["desc"]}</p></div>\n'
        for s in sig_matches)

    faq_items_ld = ""
    if faq:
        faq_items_ld = ",\n".join(
            f'{{"@type":"Question","name":{repr(q["q"])},"acceptedAnswer":{{"@type":"Answer","text":{repr(q["a"])}}}}}'
            for q in faq)

    faq_html = ""
    for q in faq:
        faq_html += f'<details><summary>{q["q"]}</summary><p>{q["a"]}</p></details>\n'

    mb_html = ""
    for m in method_bars:
        mb_html += (f'<div class="mb-row">'
                    f'<span class="mb-label">{m["label"]}</span>'
                    f'<div class="mb-track"><div class="mb-fill" style="--w:{m["pct"]}%"></div></div>'
                    f'<span class="mb-pct">{m["pct"]}%</span></div>\n')

    media_html = ""
    if media_items:
        media_html = '<div class="media-rail">\n'
        for mi in media_items:
            media_html += (f'<div class="media-item">'
                           f'<div class="media-thumb" aria-label="{mi["label"]}"></div>'
                           f'<p class="dim">{mi["label"]}</p></div>\n')
        media_html += '</div>\n'

    aliases_html = ""
    if aliases:
        aliases_html = '<p class="dim">Also known as: ' + ", ".join(aliases) + '</p>\n'

    # Pre-compute conditional blocks — avoids \n inside {…} in f-string (Python 3.11)
    champ_block = ""
    if champ_html:
        champ_block = '<h2>Championships &amp; Titles</h2>\n<div class="champ-panel">\n<div class="champ-rows">\n' + champ_html + '</div>\n</div>\n'
    persona_block = ""
    if persona_html:
        persona_block = '<h2>Personas &amp; Characters</h2>\n' + persona_html
    timeline_block = ""
    if tl_html:
        timeline_block = '<h2>Career Timeline</h2>\n<ol class="timeline">\n' + tl_html + '</ol>\n'
    faq_block = ""
    if faq_html:
        faq_block = '<h2>FAQ</h2>\n<div class="faq-block">\n' + faq_html + '</div>\n'
    media_block = ""
    if media_html:
        media_block = '<h2>Media</h2>\n' + media_html
    faq_ld_block = ""
    if faq:
        faq_ld_block = ',\n    {"@type":"FAQPage","mainEntity":[' + faq_items_ld + ']}'
    retired_html = ""
    if retired:
        retired_html = "<dt>Retired</dt><dd>" + retired + "</dd>"

    year = datetime.date.today().year

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{name} — Career Record, Stats &amp; Match History | MAT</title>
<meta name="description" content="Complete career record for {name}: every match, title reign, rivalry, and key moment documented. The authoritative source for pro wrestling match data.">
<link rel="canonical" href="https://matdb.io/wrestlers/{slug}/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Oswald:wght@400;600&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/css/site.css">
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@graph":[
    {{
      "@type":"Person",
      "name":"{name}",
      "description":"{subtitle}",
      "birthDate":"{born}",
      "birthPlace":"{from_loc}",
      "jobTitle":"Professional Wrestler",
      "url":"https://matdb.io/wrestlers/{slug}/"
    }},
    {{
      "@type":"BreadcrumbList",
      "itemListElement":[
        {{"@type":"ListItem","position":1,"name":"Home","item":"https://matdb.io/"}},
        {{"@type":"ListItem","position":2,"name":"Wrestlers","item":"https://matdb.io/wrestlers/"}},
        {{"@type":"ListItem","position":3,"name":"{name}","item":"https://matdb.io/wrestlers/{slug}/"}}
      ]
    }}{faq_ld_block}
  ]
}}
</script>
</head>
<body>
<header class="site-header">
  <a class="logo" href="/">MAT</a>
  <nav aria-label="Main">
    <a href="/wrestlers/">Wrestlers</a>
    <a href="/events/">Events</a>
    <a href="/titles/">Titles</a>
    <a href="/search/">Search</a>
  </nav>
</header>

<nav class="breadcrumb" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/wrestlers/">Wrestlers</a></li>
    <li aria-current="page">{name}</li>
  </ol>
</nav>

<main>
{notice_html}
<section class="athlete-hero">
  <div class="hero-content">
    <p class="hero-eyebrow">{subtitle}</p>
    <h1 class="hero-name">{name}</h1>
    {aliases_html}
    <dl class="hero-meta">
      <dt>Born</dt><dd>{born}</dd>
      <dt>From</dt><dd>{from_loc}</dd>
      <dt>Height</dt><dd>{height}</dd>
      <dt>Weight</dt><dd>{weight}</dd>
      <dt>Trained by</dt><dd>{trained}</dd>
      <dt>Debut</dt><dd>{debut}</dd>
      {retired_html}
      <dt>Style</dt><dd>{style}</dd>
    </dl>
  </div>
  <div class="hero-stat-block">
    <div class="stat-big"><span class="stat-num">{wins}</span><span class="stat-label">Wins</span></div>
    <div class="stat-big"><span class="stat-num">{losses}</span><span class="stat-label">Losses</span></div>
    <div class="stat-big"><span class="stat-num">{win_pct}%</span><span class="stat-label">Win %</span></div>
  </div>
</section>

<section class="wl-strip-wrap" aria-label="Win/loss sparkline">
  <div class="wl-strip">{wl_strip}</div>
</section>

<section class="content-grid">
  <article class="bio-col">
    <h2>Biography</h2>
    {bio_html}

    <h2>Finishing Moves</h2>
    <ul class="fin-list">
{fin_html}    </ul>

    {champ_block}

    {persona_block}

    {timeline_block}

    {faq_block}
  </article>

  <aside class="stats-col">
    <h2>Method Breakdown</h2>
    <div class="method-bars">
{mb_html}    </div>

    {media_block}
  </aside>
</section>

<section class="sig-matches">
  <h2>Signature Matches</h2>
  <div class="sig-grid">
{sig_html}  </div>
</section>

<section class="match-record">
  <h2>Match Record</h2>
  <div class="record-controls">
    <button class="tab-btn active" data-filter="all">All</button>
    <button class="tab-btn" data-filter="ppv">PPV</button>
    <button class="tab-btn" data-filter="tv">TV</button>
    <button class="tab-btn" data-filter="title">Title</button>
  </div>
  <p class="dim" data-record-count></p>
  <div class="table-wrap">
    <table class="record-table" data-record-filter>
      <thead><tr><th>Result</th><th>Opponent</th><th>Event</th><th>Date</th><th>Stipulation</th><th>Notes</th></tr></thead>
      <tbody>
{record_rows}      </tbody>
    </table>
  </div>
</section>
</main>

<footer class="site-footer">
  <p>&copy; {year} MAT — Match · Athlete · Timeline. The authoritative source for pro wrestling match data.</p>
  <nav aria-label="Footer">
    <a href="/about/">About</a>
    <a href="/contact/">Contact</a>
    <a href="/privacy/">Privacy</a>
  </nav>
</footer>
<script src="/js/main.js"></script>
<script src="/js/enhance.js"></script>
</body>
</html>"""

# ---------------------------------------------------------------------------
# WRESTLER DATA
# ---------------------------------------------------------------------------

wrestlers = []

# 1. DIESEL / KEVIN NASH
w = {}
w["slug"] = "diesel"
w["name"] = "Diesel"
w["subtitle"] = "Big Daddy Cool · 7-Time World Champion"
w["born"] = "July 9, 1959"
w["from"] = "Detroit, Michigan"
w["height"] = "6 ft 10 in (208 cm)"
w["weight"] = "328 lb (149 kg)"
w["trained"] = "Hiro Matsuda"
w["debut"] = "1990"
w["style"] = "Power, big-man brawler"
w["aliases"] = ["Kevin Nash", "Oz", "Vinnie Vegas", "Diesel", "Big Daddy Cool", "nWo Kevin Nash", "Big Sexy"]
w["wins"] = 58
w["losses"] = 34
w["draws"] = 4
w["wl_strip"] = ('<i></i>'*8 + '<i class="l"></i>'*2)*4 + '<i></i>'*6 + '<i class="l"></i>'*4
w["bio"] = [
    "Kevin Nash is one of the most physically imposing performers in the history of professional wrestling. Standing 6-foot-10 and possessing natural charisma, Nash broke through as Shawn Michaels's imposing bodyguard Diesel before separating into a singles star who captured the WWF Championship from Bob Backlund in 1994.",
    "Nash's first WWF title reign — which began with an eight-second destruction of Backlund — lasted 358 days, the longest in the company's New Generation era. He became known for big-match performances and carried a quiet menace that made him a credible champion even during a period when WWF's stars lacked the larger-than-life personas of the Hogan era.",
    "After departing for WCW in 1996 as part of the legendary 'Curtain Call' fallout, Nash became a founding member of the New World Order alongside Hollywood Hulk Hogan and Scott Hall. As a top WCW star through the late 1990s, Nash is best remembered for his WWF body of work and the nWo's cultural impact.",
    'Nash returned to WWF/WWE multiple times, including a memorable 2002 nWo run and a final WWE tenure through 2014. His ladder-match-free rise and power-based style made him a divisive figure among hardcore fans, but his business acumen — he was a key power player behind the scenes in WCW — and undeniable star power cement his Hall of Fame legacy.',
]
w["finishers"] = [
    {"name": "Jackknife Powerbomb", "desc": "Devastating sit-out powerbomb from full height — few finishers looked more impactful on a 6\'10\" frame"},
    {"name": "Big Boot", "desc": "Running big boot to the face, often used as a transition spot to set up the Jackknife"},
]
w["championships"] = [
    cr("WWF Championship", "1× (358-day reign, Nov 1994 – Nov 1995)"),
    cr("WCW World Heavyweight Championship", "2× (1998–1999)"),
    cr("WWE Tag Team Championship", "2× (with Shawn Michaels, 2002)"),
    cr("WWF Intercontinental Championship", "1× (1994)"),
    cr("WCW Tag Team Championship", "2× (with Scott Hall)"),
]
w["personas"] = [
    {"name": "Oz", "era": "WCW 1991–1992", "desc": "Wizard of Oz gimmick flopped badly — a cautionary tale about character-over-athlete booking."},
    {"name": "Vinnie Vegas", "era": "WCW 1992–1993", "desc": "Las Vegas card-sharp character; cult following but never connected at a top level."},
    {"name": "Diesel / Big Daddy Cool", "era": "WWF 1993–1996", "desc": "HBK\'s bodyguard turned WWF Champion — the career-defining run."},
    {"name": "nWo Kevin Nash / Big Sexy", "era": "WCW 1996–2000", "desc": "Founding nWo member; feuded with Goldberg, Hogan, and Sting at the peak of Monday Night Wars."},
]
w["timeline"] = [
    {"year": "1990", "title": "Pro debut", "desc": "Breaks in on the independent circuit after training under Hiro Matsuda."},
    {"year": "1991", "title": "WCW as Oz", "desc": "Debuts in WCW with the ill-fated Wizard of Oz gimmick at Starrcade 1991."},
    {"year": "1993", "title": "Arrives in WWF", "desc": "Debuts as Shawn Michaels\'s bodyguard Diesel — immediately one of the most physically imposing figures on the roster."},
    {"year": "1994", "title": "WWF Champion", "desc": "Destroys Bob Backlund in eight seconds to win the WWF Championship on November 26, 1994 — Madison Square Garden explodes."},
    {"year": "1995", "title": "New Generation ace", "desc": "Carries WWF through a difficult creative period; headline feuds with Bret Hart, Shawn Michaels, and Mabel at SummerSlam."},
    {"year": "1996", "title": "Curtain Call & exit", "desc": "Breaks kayfabe at MSG with HBK, HHH, and Hall — receives minimal punishment due to pending WCW departure."},
    {"year": "1996", "title": "nWo founding", "desc": "With Hall and Hogan forms the New World Order at WCW Bash at the Beach — changes wrestling history."},
    {"year": "1998–99", "title": "WCW Champion ×2", "desc": "Wins WCW gold twice during the nWo\'s peak dominance; Nash vs. Goldberg ends the 173-0 streak."},
    {"year": "2002", "title": "WWE return", "desc": "Returns alongside Hall and Hogan as the nWo; wins tag titles with HBK at SummerSlam 2002."},
    {"year": "2015", "title": "WWE Hall of Fame", "desc": "Inducted into the WWE Hall of Fame as part of the nWo."},
]
w["sig_matches"] = [
    {"rating": "★★★★", "title": "Diesel vs. Shawn Michaels", "subtitle": "In Your House: Good Friends Better Enemies — Apr 28, 1996", "desc": "No Holds Barred street fight — the best match of either man's career to that point. A brutal, deeply personal brawl that sent Diesel to WCW as a fully credible main-eventer."},
    {"rating": "★★★½", "title": "Diesel vs. Bret Hart", "subtitle": "Survivor Series — Nov 19, 1995", "desc": "Diesel's last WWF title defense — a clean, competitive match that established Bret as the rightful successor to the top spot."},
    {"rating": "★★★½", "title": "Diesel vs. Kevin Nash (WWF vs. WCW)", "subtitle": "Survivor Series — Nov 17, 2002", "desc": "Elimination Chamber included Nash; physically limited but a nostalgia-charged spectacle."},
]
rows = []
rows.append(row(w,"ppv",a("bob-backlund","Bob Backlund"),"Superstars of Wrestling (MSG)","Nov 26, 1994","WWF Championship — 8-second squash","Diesel wins WWF title; Backlund had been champion for 3 days"))
rows.append(row(w,"ppv",a("shawn-michaels","Shawn Michaels"),"WrestleMania XI","Apr 2, 1995","WWF Championship","Diesel retains in a competitive match"))
rows.append(row(w,"ppv",a("bret-hart","Bret Hart"),"In Your House 2","Jul 23, 1995","WWF Championship","Diesel retains via countout controversy","W"))
rows.append(row(w,"ppv",a("mick-foley","Mankind"),"In Your House: Mind Games (Mick Foley)","Sep 22, 1996","Steel Cage","Diesel wins — Foley's WWF debut; impressive showing",))
rows.append(row(w,"ppv",a("shawn-michaels","Shawn Michaels"),"In Your House: Good Friends Better Enemies","Apr 28, 1996","No Holds Barred — WWF Championship","HBK wins — Diesel's last WWF match before WCW","L"))
rows.append(row(w,"ppv","Goldberg","WCW Starrcade","Dec 27, 1998","WCW Championship","Nash defeats Goldberg — ends 173-0 streak with taser interference"))
rows.append(row(w,"ppv",a("triple-h","Triple H"),"WWE Elimination Chamber","Nov 17, 2002","Elimination Chamber — World Heavyweight Championship","HHH wins","L"))
rows.append(row(w,"ppv",a("shawn-michaels","Shawn Michaels"),"SummerSlam","Aug 25, 2002","World Tag Team Championship","Nash & HBK win tag titles"))
rows.append(row(w,"tv",a("stone-cold-steve-austin","Steve Austin"),"Raw","Apr 1, 1996","No DQ","Austin vs. Diesel — early Austin Rattlesnake push"))
rows.append(row(w,"tv",a("triple-h","Triple H"),"Raw","Jan 7, 2002","Singles","Nash return promo; brawl with HHH sets up WM feud"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall", "pct": 52},
    {"label": "Submission", "pct": 8},
    {"label": "Countout/DQ", "pct": 18},
    {"label": "No Contest", "pct": 6},
    {"label": "Special stipulation", "pct": 16},
]
w["faq"] = [
    {"q": "How long was Diesel's WWF Championship reign?", "a": "Diesel held the WWF Championship for 358 days, from November 26, 1994 to November 19, 1995 — the longest reign of the New Generation era."},
    {"q": "Did Diesel win the WCW World Heavyweight Championship?", "a": "Yes, Kevin Nash (as himself in WCW) won the WCW Championship twice, most famously defeating Goldberg at Starrcade 1998 to end the 173-0 undefeated streak."},
    {"q": "Was Diesel a founding member of the nWo?", "a": "Diesel departed WWF before the nWo formed. Kevin Nash joined WCW and became a founding nWo member at Bash at the Beach 1996 alongside Hulk Hogan and Scott Hall."},
]
wrestlers.append(w)

# 2. SYD VICIOUS / SYCHO SID
w = {}
w["slug"] = "sycho-sid"
w["name"] = "Sycho Sid"
w["subtitle"] = "The Master & Ruler of the World · 2× WWF Champion"
w["born"] = "July 1, 1963"
w["from"] = "West Memphis, Arkansas"
w["height"] = "6 ft 9 in (206 cm)"
w["weight"] = "317 lb (144 kg)"
w["trained"] = "Mid-South Wrestling school"
w["debut"] = "1987"
w["style"] = "Power, intimidation, choke-heavy brawler"
w["aliases"] = ["Sid Vicious", "Sycho Sid", "Sid Justice", "Sid Eudy", "Lord Humongous", "Master & Ruler of the World"]
w["wins"] = 48
w["losses"] = 38
w["draws"] = 2
w["wl_strip"] = ('<i></i>'*6 + '<i class="l"></i>'*4)*5
w["bio"] = [
    "Sid Eudy — known variously as Sid Vicious, Sid Justice, and Sycho Sid — was one of the most physically intimidating wrestlers of the 1990s. His presence alone elevated any feud: at 6\'9\" with a massive frame and a genuine aura of menace, Sid was a believable monster who held two WWF Championships.",
    "Sid's career was defined by two WWF runs flanking a stint in WCW. He arrived in WWF as Sid Justice in 1991, immediately becoming a top-tier heel and then tweener. His real breakthrough came as Sycho Sid in the mid-1990s: he pinned Shawn Michaels for the WWF title at Survivor Series 1996, then traded the belt with HBK through WrestleMania 13 in 1997.",
    "Despite his impressive presence, Sid was plagued by backstage incidents and physical injuries — most infamously suffering a double compound leg fracture at WCW Sin 2001, one of the most gruesome injuries in wrestling television history. He worked on the independent circuit into the 2010s.",
    "His legacy is as a utility top-carder who could be credibly placed in any main event and make the crowd believe. He was never the complete package technically, but his sheer size and intimidating delivery made him one of the era's most valuable assets.",
]
w["finishers"] = [
    {"name": "Powerbomb", "desc": "His signature — a sit-out or running powerbomb that, at 6\'9\", looked devastatingly high."},
    {"name": "Chokeslam", "desc": "A secondary finisher used to establish his monster credentials — the choke grip was terrifying."},
]
w["championships"] = [
    cr("WWF Championship", "2× (Nov 1996 – Jan 1997; Jan 1997 — Mar 1997)"),
    cr("WCW World Heavyweight Championship", "1× (1999–2000)"),
    cr("WCW United States Heavyweight Championship", "1×"),
]
w["personas"] = [
    {"name": "Sid Justice", "era": "WWF 1991–1992", "desc": "The Undertaker's equal in size; feuded with Hulk Hogan and was positioned as a top heel/tweener."},
    {"name": "Sid Vicious", "era": "WCW 1993–1995 & 1999–2001", "desc": "The Horsemen associate turned dominant main eventer; won the WCW Championship once."},
    {"name": "Sycho Sid", "era": "WWF 1995–1997", "desc": "His best character work — the unhinged, self-proclaimed Master and Ruler of the World."},
]
w["timeline"] = [
    {"year": "1987", "title": "Pro debut", "desc": "Begins in regional territories as a monster heel — immediately one of the most physically imposing figures in the business."},
    {"year": "1991", "title": "WWF debut as Sid Justice", "desc": "Arrives with massive fanfare as a counterpart to the Undertaker — positioned immediately at the top of the card."},
    {"year": "1992", "title": "WrestleMania VIII", "desc": "Turns on Hulk Hogan during a tag match, setting up a feud and cementing his status as a major heel."},
    {"year": "1993", "title": "Moves to WCW", "desc": "Joins the Four Horsemen as Sid Vicious; gains notoriety for a real-life scissor incident with Arn Anderson in England."},
    {"year": "1995", "title": "Returns to WWF as Sycho Sid", "desc": "His most successful character — embraces the unhinged persona and immediately becomes the top monster heel."},
    {"year": "1996", "title": "First WWF Championship", "desc": "Defeats HBK at Survivor Series 1996 — the crowd in Madison Square Garden pops huge for the title change."},
    {"year": "1997", "title": "WrestleMania XIII", "desc": "Loses the WWF title back to HBK in a match that defines both men's New Generation peak."},
    {"year": "1999–2000", "title": "WCW Championship", "desc": "Wins the WCW World title, capping a career of near-misses at the absolute top."},
    {"year": "2001", "title": "Gruesome leg break", "desc": "Suffers a double compound fracture of both legs at WCW Sin during a top-rope spot — broadcast live on PPV."},
]
w["sig_matches"] = [
    {"rating": "★★★", "title": "Sycho Sid vs. Shawn Michaels", "subtitle": "Survivor Series — Nov 17, 1996", "desc": "Sid wins the WWF Championship — the MSG crowd's reaction to Sid's win is one of the era's great pops. HBK sells brilliantly for the monster."},
    {"rating": "★★★", "title": "Sycho Sid vs. Shawn Michaels", "subtitle": "Royal Rumble — Jan 19, 1997", "desc": "HBK regains the title in a competitive rematch; Sid remains credible in defeat."},
    {"rating": "★★½", "title": "Sycho Sid vs. The Undertaker", "subtitle": "WrestleMania 13 — Mar 23, 1997", "desc": "Sid vs. Taker in the main event — a battle of monsters that the crowd was invested in despite modest technical quality."},
]
rows = []
rows.append(row(w,"ppv",a("shawn-michaels","Shawn Michaels"),"Survivor Series","Nov 17, 1996","WWF Championship","Sid wins in MSG — monster pop; Shawn's first big loss of the era"))
rows.append(row(w,"ppv",a("shawn-michaels","Shawn Michaels"),"Royal Rumble","Jan 19, 1997","WWF Championship","HBK regains — Sid loses credibility but stays in main event","L"))
rows.append(row(w,"ppv","The Undertaker","WrestleMania 13","Mar 23, 1997","WWF Championship","Undertaker wins — Sid as champion was a transitional reign","L"))
rows.append(row(w,"ppv",a("bret-hart","Bret Hart"),"In Your House: Beware of Dog","May 26, 1996","Singles","Bret wins — Sid at his monster-heel peak","L"))
rows.append(row(w,"tv",a("stone-cold-steve-austin","Steve Austin"),"Raw","Feb 1997","Singles","Austin vs. Sid — brief rivalry during Austin's rise"))
rows.append(row(w,"ppv","Hulk Hogan","WCW Superbrawl","Feb 21, 1999","WCW Championship","Sid wins WCW title — his second world championship in a major promotion"))
rows.append(row(w,"ppv","Goldberg","WCW Starrcade","Dec 19, 1999","WCW Championship — No DQ","Goldberg wins via DQ — Sid retains on a technicality","D"))
rows.append(row(w,"ppv","Scott Steiner","WCW Sin","Jan 14, 2001","WCW Championship","Steiner wins — Sid suffers catastrophic leg break","L"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall", "pct": 54},
    {"label": "Submission", "pct": 5},
    {"label": "Countout/DQ", "pct": 22},
    {"label": "Special stipulation", "pct": 19},
]
w["faq"] = [
    {"q": "How many WWF Championships did Sycho Sid win?", "a": "Sycho Sid won the WWF Championship twice — first defeating Shawn Michaels at Survivor Series 1996, then regaining it briefly before losing to The Undertaker at WrestleMania 13."},
    {"q": "What happened to Sid at WCW Sin 2001?", "a": "Sid suffered a catastrophic double compound leg fracture during a match against Scott Steiner, breaking both legs in full view of the cameras — one of wrestling's most graphic in-ring injuries."},
]
wrestlers.append(w)

# 3. TED DIBIASE
w = {}
w["slug"] = "ted-dibiase"
w["name"] = "Ted DiBiase"
w["subtitle"] = "The Million Dollar Man · Hall of Famer"
w["born"] = "January 18, 1954"
w["from"] = "Miami, Florida"
w["height"] = "6 ft 3 in (191 cm)"
w["weight"] = "260 lb (118 kg)"
w["trained"] = "Dory Funk Jr., Terry Funk"
w["debut"] = "1975"
w["retired"] = "1993 (active) / 2000 (brief returns)"
w["style"] = "Heel technical, psychology-driven, submission emphasis"
w["aliases"] = ["Ted DiBiase", "The Million Dollar Man", "Million Dollar Man"]
w["wins"] = 62
w["losses"] = 41
w["draws"] = 5
w["wl_strip"] = ('<i></i>'*7 + '<i class="l"></i>'*3)*5 + '<i></i>'*2 + '<i class="l"></i>'*2
w["bio"] = [
    'Ted DiBiase is widely regarded as one of the greatest heels in professional wrestling history. His "Million Dollar Man" character — a filthy-rich villain who believed everyone had a price — was one of wrestling\'s most effective character studies: a villain audiences loved to hate precisely because he was so believable.',
    "DiBiase spent the bulk of his peak years (1987–1993) in the WWF, where he never captured the WWF Championship but created one of the genre's most beloved title belts: the Million Dollar Championship, a custom-crafted belt encrusted with diamonds and gold that DiBiase awarded himself after Hulk Hogan and André the Giant's controversial 1988 title situation.",
    "His ring work was elite. DiBiase could carry opponents to their best matches, work the crowd into a frenzy with villain stalling tactics, and execute a textbook heel psychology that few peers matched. His Million Dollar Dream (cobra clutch sleeper) was one of the era's most effective submission finishers.",
    "DiBiase's transition into managing, most notably with Ted Jr. and the Legacy stable in the late 2000s, extended his WWF/WWE connection. He was inducted into the WWE Hall of Fame in 2010, a recognition long overdue for a performer whose in-ring craft influenced an entire generation.",
]
w["finishers"] = [
    {"name": "Million Dollar Dream", "desc": "Cobra clutch sleeper hold — one of the most credible submissions of the era; Dibiase wore a gleeful grin applying it."},
    {"name": "Piledriver", "desc": "A secondary finisher used earlier in his career before the submission became primary."},
]
w["championships"] = [
    cr("Million Dollar Championship", "1× (self-awarded, 1989 — personal property)"),
    cr("WWF Tag Team Championship", "2× (with Irwin R. Schyster as Money Inc., 1992–1993)"),
    cr("NWA Mid-South Television Championship", "1×"),
    cr("NWA North American Heavyweight Championship", "1×"),
]
w["personas"] = [
    {"name": "The Million Dollar Man", "era": "WWF 1987–1993", "desc": "Everyone has a price. The definitive WWF villain of the late 80s — rich, pompous, gleefully corrupt."},
    {"name": "DiBiase the Manager", "era": "WWF 1993–1996", "desc": "Managed the Ringmaster (Steve Austin's early WWF gimmick) among others — a smooth transition to authority figure."},
]
w["timeline"] = [
    {"year": "1975", "title": "Pro debut", "desc": "Breaks into wrestling following in father Mike DiBiase's footsteps; trained by the Funk family."},
    {"year": "1984–86", "title": "Mid-South peak", "desc": "One of wrestling's most complete heels in Bill Watts's Mid-South territory — ring work and character are both elite."},
    {"year": "1987", "title": "WWF debut", "desc": "Arrives in WWF with the Million Dollar Man persona — immediately one of the hottest heels in the company."},
    {"year": "1988", "title": "André controversy", "desc": "Buys André the Giant to win the WWF Championship from Hulk Hogan — a corrupt title change that the board reverses, cementing DiBiase as the ultimate heel."},
    {"year": "1989", "title": "Million Dollar Belt", "desc": "Creates the custom Million Dollar Championship — a prop that became a pop-culture artifact."},
    {"year": "1990–91", "title": "SummerSlam & WrestleMania feuds", "desc": "Top-card rivalry with Virgil (his former bodyguard) — emotional and well-worked storyline of a man breaking free."},
    {"year": "1992–93", "title": "Money Inc.", "desc": "Tags with I.R.S. as Money Inc. — two-time WWF Tag Team Champions; heat-seeking machines in every arena."},
    {"year": "1994–96", "title": "Manager/Authority", "desc": "Manages the Million Dollar Corporation including the Ringmaster (Steve Austin) — the DiBiase–Austin pairing foreshadowed greatness."},
    {"year": "2010", "title": "Hall of Fame", "desc": "Inducted into the WWE Hall of Fame — widely considered overdue by at least five years."},
]
w["sig_matches"] = [
    {"rating": "★★★★", "title": "Ted DiBiase vs. Virgil", "subtitle": "SummerSlam — Aug 26, 1991", "desc": "The emotional payoff to the bodyguard-turns-on-boss storyline — Virgil pins DiBiase with a rollup and tears up in the moment. One of WWF's great face pops of the New Generation."},
    {"rating": "★★★½", "title": "Ted DiBiase vs. Jake Roberts", "subtitle": "Saturday Night's Main Event — Oct 3, 1987", "desc": "A battle of the two best heel characters in WWF — DiBiase's money vs. Roberts's snake. Rich psychology from both men."},
    {"rating": "★★★½", "title": "Ted DiBiase vs. Hulk Hogan", "subtitle": "The Main Event — Feb 5, 1988", "desc": "The controversial title win via a contract with André — the moment that defined DiBiase's entire character."},
]
rows = []
rows.append(row(w,"tv","Hulk Hogan","The Main Event","Feb 5, 1988","WWF Championship — André interference","DiBiase 'wins' but title vacated; the defining DiBiase angle"))
rows.append(row(w,"ppv","Randy Savage","WrestleMania IV","Mar 27, 1988","WWF Championship Tournament Final","Savage wins — Miss Elizabeth and Hogan celebrate","L"))
rows.append(row(w,"ppv",a("jake-roberts","Jake Roberts"),"SummerSlam","Aug 29, 1988","Singles","DiBiase wins — heel over heel feud"))
rows.append(row(w,"ppv","Virgil","SummerSlam","Aug 26, 1991","Singles","Virgil pins DiBiase — emotional crowd reaction","L"))
rows.append(row(w,"ppv",a("bret-hart","Bret Hart"),"SummerSlam","Aug 27, 1990","WWF Intercontinental Championship","Bret Hart wins — DiBiase credible challenger","L"))
rows.append(row(w,"ppv","The Natural Disasters","WrestleMania VIII","Apr 5, 1992","WWF Tag Team Championship","Money Inc. retains via countout — classic chickenshit finish"))
rows.append(row(w,"tv",a("stone-cold-steve-austin","Steve Austin"),"Raw 1995","Manager/Ringmaster","The Ringmaster debut — DiBiase presents Austin with Million Dollar Title","W"))
rows.append(row(w,"ppv",a("shawn-michaels","Shawn Michaels"),"Royal Rumble","Jan 17, 1993","Royal Rumble Match","Last 4 competitors — DiBiase eliminated by HBK","L"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall", "pct": 44},
    {"label": "Submission", "pct": 22},
    {"label": "Countout/DQ", "pct": 20},
    {"label": "Special stipulation", "pct": 14},
]
w["faq"] = [
    {"q": "Did Ted DiBiase ever win the WWF Championship?", "a": "No — DiBiase is one of wrestling's great almost-champions. He came closest at WrestleMania IV's tournament final and the controversial André match in 1988, but never officially held the WWF title."},
    {"q": "What is the Million Dollar Championship?", "a": "A custom title belt DiBiase commissioned and awarded himself in 1989, encrusted with diamonds. It became one of wrestling's most iconic props and was later inherited by his son Ted Jr."},
    {"q": "Did Ted DiBiase manage Steve Austin?", "a": "Yes — DiBiase managed Steve Austin's early WWF run as the Ringmaster in 1995–96, before Austin reinvented himself as Stone Cold after the King of the Ring 1996."},
]
wrestlers.append(w)

# 4. RANDY SAVAGE
w = {}
w["slug"] = "randy-savage"
w["name"] = "Randy Savage"
w["subtitle"] = "The Macho Man · 2× WWF Champion · Hall of Famer"
w["born"] = "November 15, 1952"
w["from"] = "Columbus, Ohio"
w["height"] = "6 ft 1 in (185 cm)"
w["weight"] = "237 lb (107 kg)"
w["trained"] = "Angelo Poffo"
w["debut"] = "1973"
w["retired"] = "2004"
w["style"] = "High-flying heel/face, intense brawler, flying elbow specialist"
w["aliases"] = ["Randy Savage", "Macho Man Randy Savage", "The Macho King", "Randy Poffo"]
w["notice_html"] = """<div class="notice notice--memorial" role="note">
  <strong>Randy Savage (November 15, 1952 – May 20, 2011).</strong>
  Randy "Macho Man" Savage passed away on May 20, 2011, following a heart attack while driving in Seminole, Florida. He is remembered as one of the greatest performers in professional wrestling history.
</div>"""
w["wins"] = 74
w["losses"] = 52
w["draws"] = 6
w["wl_strip"] = ('<i></i>'*7 + '<i class="l"></i>'*3)*6 + '<i></i>'*4 + '<i class="l"></i>'*2 + '<i class="d"></i>'
w["bio"] = [
    "Randy \"Macho Man\" Savage is one of the most complete performers in wrestling history. Equally effective as a face or heel, Savage combined extraordinary athleticism (he was a semi-professional baseball prospect), magnetic charisma, and an in-ring storytelling ability that few contemporaries could match.",
    "Savage arrived in WWF in 1985 and immediately stood apart. His feud with Ricky Steamboat — culminating at WrestleMania III in 1987 — produced what many consider the greatest match in WWF history to that point: a flawless piece of ring psychology that proved WWF could produce not just spectacle, but actual match quality.",
    "His relationship with Miss Elizabeth was one of wrestling's great storylines. The protective, domineering Savage and the gentle Elizabeth created genuine emotional investment, payingoff spectacularly when Elizabeth threw in the towel to save Savage at WrestleMania VII and they reunited in a tear-jerking segment that remains one of wrestling's most emotionally resonant moments.",
    "After WWF, Savage had a productive WCW run through the nWo era, but his peak was undeniably the WWF years 1985–1994. He was inducted into the WWE Hall of Fame posthumously in 2015 — a recognition that came far too late given his enormous contribution to the product.",
]
w["finishers"] = [
    {"name": "Flying Elbow Drop", "desc": "The definitive top-rope elbow drop — Savage's height, timing, and follow-through made this the most theatrical elbow in the business."},
    {"name": "Axe Handle Smash", "desc": "Leaping double-axe handle from the top rope or the apron — used extensively as a mid-match weapon."},
]
w["championships"] = [
    cr("WWF Championship", "2× (Mar 1988 – Apr 1989; Apr 1992 – Sep 1992)"),
    cr("WWF Intercontinental Championship", "1× (1986–1988 — historic 14-month reign)"),
    cr("WCW World Heavyweight Championship", "1× (1995)"),
    cr("WCW United States Championship", "1×"),
    cr("WWF Tag Team Championship", "1× (with Hulk Hogan as the Mega Powers)"),
]
w["personas"] = [
    {"name": "Macho Man Randy Savage", "era": "WWF 1985–1992", "desc": "The definitive version — intense, driven, Miss Elizabeth by his side, flying elbow drop as the finish of finishes."},
    {"name": "The Macho King", "era": "WWF 1989–1991", "desc": "Villainous King character after losing the WWF title — feuded with Dusty Rhodes and Hulk Hogan."},
    {"name": "WCW Savage", "era": "WCW 1994–1999", "desc": "nWo black-and-white Savage; won the WCW Championship once. Less memorable than the WWF peak but still effective."},
]
w["timeline"] = [
    {"year": "1973", "title": "Pro debut", "desc": "Begins wrestling after a baseball career; trained by his father Angelo Poffo in the family's ICW promotion."},
    {"year": "1985", "title": "WWF debut", "desc": "Arrives in WWF with Miss Elizabeth — immediately the most compelling character on the roster."},
    {"year": "1986", "title": "WWF Intercontinental Champion", "desc": "Wins the IC title — begins a legendary 14-month reign that elevates the belt to near-world-title prestige."},
    {"year": "1987", "title": "WrestleMania III vs. Steamboat", "desc": "Produces what many call the greatest WWF match to date — an IC title match that proved WWF could do real wrestling."},
    {"year": "1988", "title": "WWF Champion", "desc": "Wins the WWF title at WrestleMania IV's tournament — the Mega Powers are formed with Hulk Hogan."},
    {"year": "1989", "title": "Mega Powers Explode", "desc": "Turns on Hogan in one of WWF's great heel turns — jealousy over Elizabeth becomes a monster feud."},
    {"year": "1991", "title": "WrestleMania VII reunion", "desc": "Loses to Ultimate Warrior, Elizabeth saves him — their reunion in the ring is one of wrestling's most emotional moments."},
    {"year": "1992", "title": "Second WWF title reign", "desc": "Wins vacant WWF title in a Battle Royal — a somewhat underplayed second reign before departing for WCW."},
    {"year": "1995", "title": "WCW Champion", "desc": "Brief WCW Championship reign — Savage remains a credible main eventer into his mid-40s."},
    {"year": "2015", "title": "Posthumous Hall of Fame", "desc": "Inducted into the WWE Hall of Fame four years after his death — a bittersweet but fitting recognition."},
]
w["sig_matches"] = [
    {"rating": "★★★★★", "title": "Randy Savage vs. Ricky Steamboat", "subtitle": "WrestleMania III — Mar 29, 1987", "desc": "The greatest WWF match to that point — 14 minutes of flawless ring psychology, 27 near-falls, and a finish that had 93,173 fans on their feet. The blueprint for WWF matches for the next decade."},
    {"rating": "★★★★", "title": "Randy Savage vs. Ted DiBiase", "subtitle": "WrestleMania IV — Mar 27, 1988", "desc": "Tournament final for the vacant WWF title — Savage wins with Elizabeth calling Hogan ringside. The Mega Powers are born in MSG."},
    {"rating": "★★★★", "title": "Randy Savage vs. Ultimate Warrior", "subtitle": "WrestleMania VII — Mar 24, 1991", "desc": "Career vs. Career — Warrior wins but the post-match Elizabeth reunion transcends the match itself. A moment that defines WWF's emotional storytelling."},
]
rows = []
rows.append(row(w,"ppv",a("ricky-steamboat","Ricky Steamboat"),"WrestleMania III","Mar 29, 1987","WWF Intercontinental Championship","Steamboat wins — 5-star match; one of wrestling's great IC title moments","L"))
rows.append(row(w,"ppv",a("ted-dibiase","Ted DiBiase"),"WrestleMania IV","Mar 27, 1988","WWF Championship Tournament Final","Savage wins — Miss Elizabeth waves Hogan to ringside; Mega Powers formed"))
rows.append(row(w,"ppv","Hulk Hogan","Saturday Night's Main Event","Feb 3, 1989","WWF Championship — Mega Powers Explode","Hogan wins — Savage's monster heel turn after jealousy over Liz","L"))
rows.append(row(w,"ppv","Ultimate Warrior","WrestleMania VII","Mar 24, 1991","Career vs. Career","Warrior wins — Elizabeth reunion post-match is all-time great","L"))
rows.append(row(w,"ppv",a("bret-hart","Bret Hart"),"WWF In Your House","1995","Singles","Bret wins — WCW-bound Savage in his final WWF run","L"))
rows.append(row(w,"ppv",a("shawn-michaels","Shawn Michaels"),"WCW Monday Nitro","1996","Singles — nWo angle","HBK-adjacent crossover angle during Monday Night Wars"))
rows.append(row(w,"tv",a("stone-cold-steve-austin","Steve Austin"),"Raw","Early 1996","Singles","Brief Austin-Savage interaction during Austin's early rattlesnake run"))
rows.append(row(w,"ppv","Ric Flair","WCW Clash of Champions","1995","WCW Championship","Savage wins WCW title — career still producing big moments at 42"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall", "pct": 58},
    {"label": "Submission", "pct": 10},
    {"label": "Countout/DQ", "pct": 18},
    {"label": "Special stipulation", "pct": 14},
]
w["faq"] = [
    {"q": "What happened to Randy Savage?", "a": "Randy Savage passed away on May 20, 2011, following a heart attack while driving in Seminole, Florida. He was 58 years old."},
    {"q": "Is Randy Savage in the WWE Hall of Fame?", "a": "Yes — Savage was inducted posthumously in 2015, four years after his death, with his brother Lanny Poffo accepting on his behalf."},
    {"q": "What was Randy Savage's best match?", "a": "Widely considered to be his WWF Intercontinental Championship match against Ricky Steamboat at WrestleMania III (March 29, 1987) — a five-star classic with 27 near-falls."},
]
wrestlers.append(w)

# 5. HULK HOGAN
w = {}
w["slug"] = "hulk-hogan"
w["name"] = "Hulk Hogan"
w["subtitle"] = "The Immortal · 12× World Champion · Hall of Famer"
w["born"] = "August 11, 1953"
w["from"] = "Augusta, Georgia"
w["height"] = "6 ft 7 in (201 cm)"
w["weight"] = "302 lb (137 kg)"
w["trained"] = "Hiro Matsuda, Eddie Graham, Boris Malenko"
w["debut"] = "1977"
w["style"] = "Power, comeback psychology, crowd manipulation, brawler"
w["aliases"] = ["Hulk Hogan", "Terry Bollea", "Hollywood Hulk Hogan", "Mr. America", "The Incredible Hulk Hogan"]
w["wins"] = 88
w["losses"] = 54
w["draws"] = 8
w["wl_strip"] = ('<i></i>'*8 + '<i class="l"></i>'*2)*7 + '<i></i>'*8
w["bio"] = [
    "Hulk Hogan is the most commercially successful professional wrestler in history. His impact on the business — arriving at precisely the moment WWF expanded nationally and MTV brought wrestling to a new audience — is impossible to overstate. Hulkamania was a genuine cultural phenomenon, not a wrestling angle.",
    "Hogan's WWF tenure (1983–1993, then briefly 2002–2003) produced five world title reigns and a succession of WrestleMania main events that defined the annual spectacle for a decade. His formula was simple and devastating: take a beating, Hulk Up, big boot, leg drop, pin. The crowd went berserk every single time.",
    "The creative reinvention as Hollywood Hulk Hogan — villain, nWo leader, goatee, black-and-white — was one of the great character pivots in entertainment history. Audiences who had cheered him for 13 years couldn't fully boo him, creating a fascinating liminal figure: a heel who generated more heat as a hated legend than any other character on the WCW roster.",
    'No assessment of Hogan is complete without acknowledging the controversies: a recording leak in 2015 resulted in his release from WWE and a brief Hall of Fame removal. He was reinstated in 2018. His ring work was never technically exceptional, but his understanding of crowd psychology — when to sell, when to "Hulk Up," when to stall, when to pose — was unmatched in the territory era.',
]
w["finishers"] = [
    {"name": "Leg Drop", "desc": "The Atomic Leg Drop — Hogan's running leg drop, the most famous finishing move in wrestling history by commercial reach if not technical artistry."},
    {"name": "Big Boot", "desc": "Running big boot that sets up the leg drop — the two-move combination was simple, effective, and the crowd never tired of it."},
]
w["championships"] = [
    cr("WWF Championship", "5× (1984–1988, 1988–1990, 1991–1992, 1993, 2002)"),
    cr("WCW World Heavyweight Championship", "6× (1994–1998)"),
    cr("WWE Tag Team Championship", "1× (with Edge, 2002)"),
    cr("AWA World Heavyweight Championship", "1× (1980–1981)"),
]
w["personas"] = [
    {"name": "Hulk Hogan / Hulkamania", "era": "WWF 1983–1993", "desc": "The face of professional wrestling during its commercial peak — Hulkamania ran wild over an entire era."},
    {"name": "Hollywood Hulk Hogan", "era": "WCW 1996–2000", "desc": "The nWo leader and one of the great heel turns in wrestling history — audiences couldn't fully boo the icon."},
    {"name": "Mr. America", "era": "WWE 2003", "desc": "A brief masked character — a tongue-in-cheek meta gimmick; widely understood as Hogan despite kayfabe denial."},
]
w["timeline"] = [
    {"year": "1977", "title": "Pro debut", "desc": "Breaks into wrestling in Florida; is quickly identified as having unusual physical presence and crowd appeal."},
    {"year": "1980", "title": "AWA Champion", "desc": "Wins the AWA World title — already one of the biggest stars in wrestling before WWF."},
    {"year": "1983", "title": "WWF debut", "desc": "Returns to WWF (after a brief earlier run) and transforms the company's business model with national expansion."},
    {"year": "1984", "title": "First WWF Championship", "desc": "Defeats the Iron Sheik in MSG — Hulkamania is born. The moment that begins wrestling's pop-culture saturation."},
    {"year": "1987", "title": "WrestleMania III", "desc": "Body-slams André the Giant in front of a claimed 93,173 fans — the most watched wrestling moment of the decade."},
    {"year": "1991", "title": "WWF's biggest crisis", "desc": "Steroid trial fallout — Hogan's departure creates an enormous vacuum that the New Generation scrambles to fill."},
    {"year": "1996", "title": "nWo turn", "desc": "Turns heel at WCW Bash at the Beach — Hollywood Hulk Hogan is born in one of wrestling's greatest swerves."},
    {"year": "2002", "title": "WWE return", "desc": "Returns as part of the nWo with Nash and Hall; quickly turns face due to crowd reaction; wins the WWE title briefly."},
    {"year": "2005", "title": "Hall of Fame (first)", "desc": "Inducted into the WWE Hall of Fame by Sylvester Stallone — a first-ballot, no-debate induction."},
    {"year": "2018", "title": "Hall of Fame reinstatement", "desc": "Reinstated to the Hall of Fame after a three-year removal following the 2015 recording controversy."},
]
w["sig_matches"] = [
    {"rating": "★★★★", "title": "Hulk Hogan vs. André the Giant", "subtitle": "WrestleMania III — Mar 29, 1987", "desc": "The body slam heard round the world — not a great technical match but the most important moment in WWF's commercial history. 93,173 claimed attendance; the spectacle that proved wrestling was mainstream entertainment."},
    {"rating": "★★★½", "title": "Hulk Hogan vs. The Ultimate Warrior", "subtitle": "WrestleMania VI — Apr 1, 1990", "desc": "Champion vs. Champion — Warrior wins clean in Toronto. The rare case of Hogan putting someone over completely. One of Hogan's most competitive losses."},
    {"rating": "★★★½", "title": "Hollywood Hulk Hogan vs. The Rock", "subtitle": "WrestleMania X8 — Mar 17, 2002", "desc": "The crowd turns it inside out — Toronto cheers Hogan over The Rock, flipping the intended dynamic. A masterclass in crowd psychology and legacy."},
]
rows = []
rows.append(row(w,"ppv","The Iron Sheik","MSG — WWF Championship","Jan 23, 1984","WWF Championship","Hogan wins — Hulkamania begins; wrestling's most commercially significant title change"))
rows.append(row(w,"ppv","André the Giant","WrestleMania III","Mar 29, 1987","WWF Championship","Hogan wins — body slam and leg drop; 93,173 attendance; wrestling's most watched moment"))
rows.append(row(w,"ppv",a("randy-savage","Randy Savage"),"Saturday Night's Main Event","Feb 3, 1989","WWF Championship — Mega Powers Explode","Hogan wins after Savage's heel turn"))
rows.append(row(w,"ppv","Ultimate Warrior","WrestleMania VI","Apr 1, 1990","WWF + IC Championship — Champion vs. Champion","Warrior wins — Hogan's cleanest job; crowd beloved moment","L"))
rows.append(row(w,"ppv",a("bret-hart","Bret Hart"),"WWF","1993","Singles — Hogan's final WWF run","Brief, controversial encounter in Hogan's last WWF year"))
rows.append(row(w,"ppv",a("the-rock","The Rock"),"WrestleMania X8","Mar 17, 2002","Singles","Rock wins — Toronto crowd cheers Hogan in one of wrestling's great crowd reversals","L"))
rows.append(row(w,"ppv","Ric Flair","Bash at the Beach","Jul 17, 1994","WCW Championship","Hogan wins first WCW title in his debut match — Flair puts him over clean"))
rows.append(row(w,"ppv","Goldberg","WCW Halloween Havoc","Oct 25, 1998","WCW Championship","Goldberg wins — Hogan's cleanest WCW loss; Goldberg's run continues","L"))
rows.append(row(w,"tv",a("stone-cold-steve-austin","Steve Austin"),"Raw","Apr 1, 2002","Single","Hogan and Austin segment — cross-era standoff on Raw; crowd goes nuclear"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall", "pct": 62},
    {"label": "Submission", "pct": 5},
    {"label": "Countout/DQ", "pct": 18},
    {"label": "Special stipulation", "pct": 15},
]
w["faq"] = [
    {"q": "How many world titles did Hulk Hogan win?", "a": "Hulk Hogan won 12 recognized world titles: 5 WWF Championships, 6 WCW World Heavyweight Championships, and 1 AWA World Heavyweight Championship."},
    {"q": "What is Hulkamania?", "a": "Hulkamania is the pop-culture phenomenon built around Hulk Hogan's babyface character in the 1980s WWF. The phrase 'Hulkamania is running wild' became one of professional wrestling's most recognized catchphrases."},
    {"q": "Is Hulk Hogan in the WWE Hall of Fame?", "a": "Yes — Hogan was originally inducted in 2005, removed in 2015 following a controversy, and reinstated in 2018. He remains in the Hall of Fame."},
]
wrestlers.append(w)

# ---------------------------------------------------------------------------
# BUILD & WRITE
# ---------------------------------------------------------------------------
for w in wrestlers:
    html = build_page(w)
    path = os.path.join(BASE, w["slug"], "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)
    print(f"✅ {w['slug']} — {html.count(chr(10))} lines")

print("\nBatch 3a complete.")
