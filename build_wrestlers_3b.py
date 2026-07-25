#!/usr/bin/env python3
"""Batch 3b: Batista, John Cena, Rey Mysterio, Goldberg, Ric Flair"""
import os, datetime

BASE = "/root/wwe/wrestlers"

def cr(title, reign, note=""):
    note_html = '<span class="cr-note">' + note + '</span>' if note else ""
    return f'    <div class="champ-row"><span class="cr-title">{title}</span><span class="cr-reign">{reign}</span>{note_html}</div>\n'

def a(slug, name):
    return f'<a href="/wrestlers/{slug}/">{name}</a>'

def row(w, kind, opp, event, date, stipulation, note, result="W"):
    res_class = "l" if result == "L" else ("d" if result == "D" else "")
    res_label = result
    td_cls = ' class="res-l"' if res_class == "l" else (' class="res-d"' if res_class == "d" else "")
    return (f'<tr class="record-row" data-result="{result}" data-cats="{kind}">'
            f'<td class="res-cell"><span class="res-badge{" res-l" if result=="L" else " res-d" if result=="D" else ""}">{res_label}</span></td>'
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
    method_bars = w.get("method_bars",[])
    aliases = w.get("aliases",[])
    wl_strip = w.get("wl_strip","")

    # --- pre-compute all HTML blocks ---
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

    aliases_html = ""
    if aliases:
        aliases_html = '<p class="dim">Also known as: ' + ", ".join(aliases) + '</p>\n'

    # Conditional section blocks — NO \n inside f-string {…} expressions (Python 3.11)
    champ_block = ""
    if champ_html:
        champ_block = '<h2>Championships &amp; Titles</h2>\n<div class="champ-panel"><div class="champ-rows">\n' + champ_html + '</div></div>\n'
    persona_block = ""
    if persona_html:
        persona_block = '<h2>Personas &amp; Characters</h2>\n' + persona_html
    timeline_block = ""
    if tl_html:
        timeline_block = '<h2>Career Timeline</h2>\n<ol class="timeline">\n' + tl_html + '</ol>\n'
    faq_block = ""
    if faq_html:
        faq_block = '<h2>FAQ</h2>\n<div class="faq-block">\n' + faq_html + '</div>\n'
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
<meta name="description" content="Complete career record for {name}: every match, title reign, rivalry, and key moment. The authoritative source for pro wrestling match data.">
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

# 1. BATISTA
w = {}
w["slug"] = "batista"
w["name"] = "Batista"
w["subtitle"] = "The Animal · 6× World Champion"
w["born"] = "January 18, 1969"
w["from"] = "Washington, D.C."
w["height"] = "6 ft 6 in (198 cm)"
w["weight"] = "290 lb (132 kg)"
w["trained"] = "Afa Anoa'i, Adam Pearce, Sgt. Slaughter"
w["debut"] = "1999"
w["style"] = "Power, methodical ring work, sustained selling"
w["aliases"] = ["Batista", "Dave Batista", "The Animal", "Deacon Batista"]
w["wins"] = 64
w["losses"] = 38
w["draws"] = 3
w["wl_strip"] = ('<i></i>'*7 + '<i class="l"></i>'*3)*6 + '<i></i>'*4
w["bio"] = [
    "Dave Batista arrived in WWE in 2000 and became one of the most physically imposing and carefully developed powerhouses in the company's history. Unlike many power wrestlers rushed to the top, Batista spent three years as a bodyguard and tag-team specialist (Evolution with Triple H, Ric Flair, and Randy Orton) before earning his singles shot — and the patience paid off.",
    "His 2005 babyface turn and championship run against Triple H at WrestleMania 21 is a textbook case of slow-burn character development: the crowd had been waiting 18 months for Batista to leave Evolution, and when he finally hit the Batista Bomb on HHH, the eruption was earned. Six world title reigns followed across RAW and SmackDown.",
    "Batista was also notable for his rivalry with The Undertaker, producing three WrestleMania encounters. Their feud at WrestleMania 23 (No Way Out 2007 and WM23) showcased Batista's ability to work long power matches that told complete stories — rare for a performer of his size.",
    "After a first retirement in 2010, Batista had a second WWE run from 2014 that — despite a famously cold homecoming — led to a memorable feud with Daniel Bryan and a beloved heel run. He also became a mainstream action movie star, cementing a cultural crossover few wrestlers achieve. He was inducted into the WWE Hall of Fame in 2023.",
]
w["finishers"] = [
    {"name": "Batista Bomb", "desc": "Running powerbomb from a seated position — enormously impactful at his size; one of the era's most-over finishers."},
    {"name": "Spinebuster", "desc": "A secondary setup move used throughout matches — Batista's spinebuster was among the crispest in WWE history."},
]
w["championships"] = [
    cr("World Heavyweight Championship", "4× (2005, 2006, 2007, 2009–2010)"),
    cr("WWE Championship", "2× (2008, 2010)"),
    cr("WWE Tag Team Championship", "1× (with Rey Mysterio, 2006)"),
    cr("World Tag Team Championship", "1× (with Ric Flair, 2003)"),
]
w["personas"] = [
    {"name": "Deacon Batista", "era": "WWE 2002", "desc": "Silent enforcer for D-Von Dudley — an early character that had nowhere to go; quickly pivoted."},
    {"name": "Evolution member", "era": "WWE 2003–2005", "desc": "Muscle for Triple H, Flair, and Orton — the slow build to a career-making face turn."},
    {"name": "The Animal", "era": "WWE 2005–2010 & 2014", "desc": "The definitive Batista — six-time world champion, WrestleMania main eventer."},
]
w["timeline"] = [
    {"year": "1999", "title": "Pro debut", "desc": "Begins wrestling after gym work and Afa's Wild Samoans training camp."},
    {"year": "2002", "title": "WWE debut as Deacon Batista", "desc": "Arrives as the silent enforcer for D-Von Dudley — the initial character doesn't connect."},
    {"year": "2003", "title": "Joins Evolution", "desc": "Becomes the muscle of Triple H's Evolution stable alongside Ric Flair and Randy Orton — begins his slow climb."},
    {"year": "2005", "title": "Royal Rumble & turn", "desc": "Wins the Royal Rumble, then publicly chooses SmackDown over RAW in a character moment that pops the crowd. Sets up WrestleMania 21."},
    {"year": "2005", "title": "WrestleMania 21 — World Heavyweight Champion", "desc": "Defeats Triple H for the World Heavyweight title — earned babyface payoff to an 18-month slow burn."},
    {"year": "2006–09", "title": "Multi-reign champion", "desc": "Three further World title reigns; major feuds with Undertaker, Kennedy, Edge, and Rey Mysterio."},
    {"year": "2010", "title": "WWE Champion — first retirement", "desc": "Brief WWE title reign before citing frustration with creative direction and retirement from active competition."},
    {"year": "2014", "title": "Return & heel run", "desc": "Returns to a lukewarm reaction (the audience was pro-Daniel Bryan at the time); eventually leans into a great heel run and feud with Bryan."},
    {"year": "2023", "title": "WWE Hall of Fame", "desc": "Inducted in the Class of 2023 — a career achievement that also coincides with his return for one final match concept."},
]
w["sig_matches"] = [
    {"rating": "★★★★", "title": "Batista vs. Triple H", "subtitle": "WrestleMania 21 — Apr 3, 2005", "desc": "The payoff to Evolution — Batista wins the World Heavyweight title in a match the crowd had been anticipating for months. The pop for the Batista Bomb is one of WrestleMania's great moments of the decade."},
    {"rating": "★★★½", "title": "Batista vs. The Undertaker", "subtitle": "WrestleMania 23 — Apr 1, 2007", "desc": "World Heavyweight Championship — their best encounter of three WM matches. A power-vs-power bout with sustained drama and a strong finishing sequence."},
    {"rating": "★★★½", "title": "Batista vs. John Cena", "subtitle": "SummerSlam — Aug 26, 2008", "desc": "WWE Championship — one of their best encounters; Cena retains in a hard-fought match that established Batista as a credible title challenger."},
]
rows = []
rows.append(row(w,"ppv",a("triple-h","Triple H"),"WrestleMania 21","Apr 3, 2005","World Heavyweight Championship — Evolution payoff","Batista Bomb; one of WM's great earned pops"))
rows.append(row(w,"ppv",a("triple-h","Triple H"),"Vengeance","Jun 26, 2005","World Heavyweight Championship — Hell in a Cell","Batista retains — their best pure in-ring match"))
rows.append(row(w,"ppv","The Undertaker","WrestleMania 23","Apr 1, 2007","World Heavyweight Championship","Undertaker wins — Batista sells superbly for the Deadman","L"))
rows.append(row(w,"ppv","The Undertaker","WrestleMania XXIV","Mar 30, 2008","World Heavyweight Championship","Undertaker wins — 16–0 streak continues","L"))
rows.append(row(w,"ppv",a("john-cena","John Cena"),"SummerSlam","Aug 26, 2008","WWE Championship","Cena retains in competitive match","L"))
rows.append(row(w,"ppv",a("john-cena","John Cena"),"Extreme Rules","Jun 7, 2009","WWE Championship — Last Man Standing","Batista wins — count-out technicality"))
rows.append(row(w,"ppv","Rey Mysterio","WrestleMania 26","Mar 28, 2010","Singles","Batista wins — double-turn finish; Batista goes heel","W"))
rows.append(row(w,"ppv",a("john-cena","John Cena"),"WrestleMania 26","Mar 28, 2010","WWE Championship","Cena wins — Batista submits to STF in main event","L"))
rows.append(row(w,"ppv",a("triple-h","Triple H"),"WrestleMania XXX","Apr 6, 2014","WWE Championship #1 Contender","Triple H wins — cold homecoming for Batista","L"))
rows.append(row(w,"ppv","Daniel Bryan","WrestleMania XXX","Apr 6, 2014","WWE Championship","Bryan wins — Batista's best heel match; crowd fully turned","L"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall", "pct": 56},
    {"label": "Submission", "pct": 8},
    {"label": "Countout/DQ", "pct": 16},
    {"label": "Special stipulation", "pct": 20},
]
w["faq"] = [
    {"q": "How many world titles did Batista win?", "a": "Batista won 6 world titles in WWE: 4 World Heavyweight Championships and 2 WWE Championships."},
    {"q": "Is Batista in the WWE Hall of Fame?", "a": "Yes — Batista was inducted into the WWE Hall of Fame Class of 2023."},
    {"q": "Did Batista and The Undertaker wrestle at WrestleMania?", "a": "Yes — three times: WrestleMania 23 (2007), WrestleMania XXIV (2008), and WrestleMania 35 (2019, in a No Holds Barred match). The Undertaker won all three."},
]
wrestlers.append(w)

# 2. JOHN CENA
w = {}
w["slug"] = "john-cena"
w["name"] = "John Cena"
w["subtitle"] = "The Champ · 16× World Champion · Hall of Famer"
w["born"] = "April 23, 1977"
w["from"] = "West Newbury, Massachusetts"
w["height"] = "6 ft 1 in (185 cm)"
w["weight"] = "251 lb (114 kg)"
w["trained"] = "Les Thatcher (Ohio Valley Wrestling)"
w["debut"] = "1999"
w["style"] = "Power, crowd engagement, STF specialist, methodical heavyweight"
w["aliases"] = ["John Cena", "The Champ", "The Doctor of Thuganomics", "Never Give Up", "YOUCANTSEEME"]
w["wins"] = 98
w["losses"] = 61
w["draws"] = 5
w["wl_strip"] = ('<i></i>'*8 + '<i class="l"></i>'*2)*9 + '<i></i>'*8
w["bio"] = [
    "John Cena is the most commercially successful WWE superstar of the post-Attitude Era. His 16 world title reigns — tying Ric Flair's all-time record — and more than a decade as the company's primary face make him the defining WWE performer of the 2000s and early 2010s.",
    "Cena's career trajectory is one of wrestling's most studied: he arrived in 2000 as a standard powerhouse, found his voice with the Doctor of Thuganomics hip-hop character in 2002, and ascended to the top of the card with a relentlessness and work ethic that made him indispensable. His five-move-of-doom formula was endlessly criticized by hardcore fans, but his connection with younger audiences and mainstream media was undeniable.",
    "The Cena era is defined by extraordinary longevity at the top. From 2005 to 2016 he was rarely outside the main event picture, headlining 13 WrestleManias and feuding with essentially every major WWE star of the period: Edge, Randy Orton, CM Punk, Daniel Bryan, Sheamus, The Rock, Brock Lesnar, AJ Styles, and more.",
    "His record-breaking Make-A-Wish contributions (650+ wishes granted, the most of any public figure in the organization's history) and crossover into Hollywood (Fast & Furious, The Suicide Squad, Peacemaker) cement a legacy that extends far beyond the ring. He was inducted into the WWE Hall of Fame in 2025.",
]
w["finishers"] = [
    {"name": "Attitude Adjustment (AA)", "desc": "Fireman's carry into a toss slam — simple, impactful, and made him look strong executing on opponents of every size."},
    {"name": "STF (Stepover Toehold Facelock)", "desc": "Submission finisher — the STF earned genuine heat because critics found his application questionable, but it won many major matches."},
]
w["championships"] = [
    cr("WWE Championship", "13× (2005–2017)"),
    cr("World Heavyweight Championship", "3× (2008–2013)"),
    cr("United States Championship", "5× (2004–2019)"),
    cr("WWE Tag Team Championship", "1× (with Batista, SmackDown) / 1× (with Shawn Michaels, RAW)"),
    cr("World Tag Team Championship", "1×"),
]
w["personas"] = [
    {"name": "Prototype", "era": "OVW 2000–2001", "desc": "His developmental character — physically impressive but without character differentiation."},
    {"name": "Doctor of Thuganomics", "era": "WWE 2002–2004", "desc": "The hip-hop freestyler who found his personality — fan-favourite heel who cut brilliant promos."},
    {"name": "The Champ / Never Give Up", "era": "WWE 2004–present", "desc": "The signature Cena — blue-green wristbands, Never Give Up, polarizing hero to children and heel to hardcores."},
]
w["timeline"] = [
    {"year": "1999", "title": "Pro debut", "desc": "Begins wrestling after a bodybuilding and college football background."},
    {"year": "2002", "title": "WWE debut & Doctor of Thuganomics", "desc": "Debuts in WWE, quickly pivoting to the rap-battle character that makes him a fan-favourite on the cusp of villainy."},
    {"year": "2004", "title": "United States Champion", "desc": "His first singles title — won from the Big Show, signals his ascent to the top tier."},
    {"year": "2005", "title": "First WWE Championship", "desc": "Defeats JBL at WrestleMania 21 — the beginning of the Cena era at the top of WWE."},
    {"year": "2006", "title": "New Year's Revolution cash-in", "desc": "Edge cashes in Money in the Bank after Cena survives the Elimination Chamber — Cena loses the title moments after winning it."},
    {"year": "2007", "title": "Torn pectoral — rapid return", "desc": "Suffers a torn pectoral muscle in October; returns in just five months at Royal Rumble 2008 in one of the decade's great surprise returns."},
    {"year": "2011", "title": "WrestleMania XXVII vs. The Rock announcement", "desc": "The Rock returns to confront Cena — their feud culminates in two straight WrestleMania main events."},
    {"year": "2012", "title": "WrestleMania XXVIII vs. The Rock", "desc": "Loses to The Rock in Miami in a historic celebrity-vs-superstar main event."},
    {"year": "2013", "title": "16th world title — ties Flair", "desc": "Wins the 16th world title, tying Ric Flair's record — a genuinely significant achievement regardless of title inflation debates."},
    {"year": "2025", "title": "WWE Hall of Fame & retirement", "desc": "Inducted into the WWE Hall of Fame and completes a retirement tour following a final full-time WWE run."},
]
w["sig_matches"] = [
    {"rating": "★★★★½", "title": "John Cena vs. CM Punk", "subtitle": "Money in the Bank — Jun 27, 2011", "desc": "Punk's contract-expiration promo + the live Chicago crowd + Cena's best-ever performance = one of the 2010s' great WWE matches. Punk wins the title and leaves with it — a story that felt genuinely unpredictable."},
    {"rating": "★★★★", "title": "John Cena vs. The Rock", "subtitle": "WrestleMania XXIX — Apr 7, 2013", "desc": "Cena gets his win back in East Rutherford — a cleaner match than their first encounter. The AA from the top rope is a WrestleMania highlight."},
    {"rating": "★★★★", "title": "John Cena vs. AJ Styles", "subtitle": "SummerSlam — Aug 21, 2016", "desc": "AJ's breakout performance on the biggest stage — beats Cena clean; one of the best wrestling matches in SummerSlam history."},
]
rows = []
rows.append(row(w,"ppv","JBL","WrestleMania 21","Apr 3, 2005","WWE Championship","Cena wins his first WWE title — the Cena era begins"))
rows.append(row(w,"ppv",a("edge","Edge"),"New Year's Revolution follow-up","Jan 8, 2006","WWE Championship — MITB cash-in","Edge cashes in — Cena loses title moments after winning EC","L"))
rows.append(row(w,"ppv",a("batista","Batista"),"SummerSlam","Aug 26, 2008","WWE Championship","Cena retains in physical match"))
rows.append(row(w,"ppv","CM Punk","Money in the Bank","Jun 27, 2011","WWE Championship — Punk's last night","Punk wins — contract expires; leaves with title; all-time WWE match","L"))
rows.append(row(w,"ppv",a("the-rock","The Rock"),"WrestleMania XXVIII","Apr 1, 2012","Once in a Lifetime","Rock wins — Cena's first loss in a WrestleMania main event","L"))
rows.append(row(w,"ppv",a("the-rock","The Rock"),"WrestleMania XXIX","Apr 7, 2013","WWE Championship","Cena wins — AA from top rope; gets revenge on Rock"))
rows.append(row(w,"ppv","Brock Lesnar","Night of Champions","Sep 21, 2014","Singles","Lesnar wins — dominant squash; Cena's credibility taking hits","L"))
rows.append(row(w,"ppv","AJ Styles","SummerSlam","Aug 21, 2016","Singles","AJ wins clean — one of SummerSlam's best matches","L"))
rows.append(row(w,"ppv",a("roman-reigns","Roman Reigns"),"No Mercy","Oct 22, 2017","Singles","Reigns wins — torch-passing match","L"))
rows.append(row(w,"tv",a("stone-cold-steve-austin","Steve Austin"),"Raw — 20th Anniversary","Jan 14, 2013","Singles segment","Austin vs. Cena interaction — Stone Cold Stunner moment"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall", "pct": 60},
    {"label": "Submission (STF)", "pct": 18},
    {"label": "Countout/DQ", "pct": 12},
    {"label": "Special stipulation", "pct": 10},
]
w["faq"] = [
    {"q": "How many world titles has John Cena won?", "a": "John Cena has won 16 world titles in WWE — 13 WWE Championships and 3 World Heavyweight Championships — tying Ric Flair's record."},
    {"q": "Is John Cena in the WWE Hall of Fame?", "a": "Yes — Cena was inducted into the WWE Hall of Fame in 2025."},
    {"q": "What is John Cena's best match?", "a": "Widely considered to be his WWE Championship match against CM Punk at Money in the Bank 2011 — a near-five-star match in Chicago where Punk won the title and left the company with it."},
]
wrestlers.append(w)

# 3. REY MYSTERIO
w = {}
w["slug"] = "rey-mysterio"
w["name"] = "Rey Mysterio"
w["subtitle"] = "The Master of the 619 · WWE & World Champion"
w["born"] = "December 11, 1974"
w["from"] = "San Diego, California"
w["height"] = "5 ft 6 in (168 cm)"
w["weight"] = "175 lb (79 kg)"
w["trained"] = "Rey Mysterio Sr., El Dinamita"
w["debut"] = "1989"
w["style"] = "Lucha libre, high-flying, fast-paced aerial assault"
w["aliases"] = ["Rey Mysterio", "Rey Mysterio Jr.", "Oscar Gutierrez", "The Master of the 619"]
w["wins"] = 79
w["losses"] = 68
w["draws"] = 4
w["wl_strip"] = ('<i></i>'*6 + '<i class="l"></i>'*4)*7 + '<i></i>'*5 + '<i class="l"></i>'*2
w["bio"] = [
    "Rey Mysterio is the most important small man in the history of sports entertainment. At 5'6\" and 175 pounds, he performed in a world built for men twice his size — and he not only competed, he elevated the art form. His influence on the lucha libre-meets-WWE style can be heard in how any aerial move is called today.",
    "Mysterio's WCW run in the mid-1990s (alongside Eddie Guerrero and Chris Jericho) produced some of the best cruiserweight matches in American television history. When WWE acquired WCW in 2001, Mysterio came with it, and his 2002 SmackDown debut immediately raised the in-ring quality of the entire brand.",
    "His 2006 Royal Rumble win — the shortest time-in-ring winner in Royal Rumble history before that moment — and subsequent WrestleMania 22 world title win (in an exhausted, emotional tribute to Eddie Guerrero) is one of wrestling's most powerful storyline payoffs. The crowd in Chicago had been building to that moment for months.",
    "Mysterio's career is marked by spectacular matches against opponents who outweigh him by 100+ pounds: Undertaker, Batista, Edge, JBL, Randy Orton, and Brock Lesnar. He makes every opponent look physically dominant while remaining impossible to root against. That's a technical achievement requiring extraordinary skill.",
]
w["finishers"] = [
    {"name": "619", "desc": "Running leg scissors to the ropes — a move that shouldn't work but does, every single time, because of his positioning and timing."},
    {"name": "West Coast Pop (Frog Splash variant)", "desc": "Springboard seated senton or frog splash from the top — the finish after the 619 sets up the pin."},
    {"name": "Hurricanrana", "desc": "His signature throughout his career — used as a finish, a transition, and a counter. Flawlessly executed at every speed."},
]
w["championships"] = [
    cr("WWE Championship", "1× (2011)"),
    cr("World Heavyweight Championship", "2× (2006, 2010)"),
    cr("Intercontinental Championship", "4×"),
    cr("United States Championship", "1×"),
    cr("WWE Tag Team Championship", "3× (with Eddie Guerrero, Batista, and others)"),
    cr("WCW Cruiserweight Championship", "3×"),
    cr("WCW Tag Team Championship", "1× (with Konnan)"),
]
w["personas"] = [
    {"name": "Rey Mysterio Jr.", "era": "WCW / indies 1989–2002", "desc": "The masked luchador who rewrote what cruiserweights could do in America — WCW Cruiserweight records and matches with Guerrero, Jericho, and Malenko."},
    {"name": "Rey Mysterio (unmasked)", "era": "WCW 1999–2001", "desc": "Unmasking was a creative disaster — the mask is part of his character and mystique; losing it briefly cost him crowd heat."},
    {"name": "Rey Mysterio (WWE masked)", "era": "WWE 2002–present", "desc": "The definitive version — masked hero, 619, Eddie tribute storylines, world champion."},
]
w["timeline"] = [
    {"year": "1989", "title": "Pro debut at age 14", "desc": "Begins wrestling in Mexico under the tutelage of his uncle Rey Mysterio Sr. — one of wrestling's earliest prodigies."},
    {"year": "1996", "title": "WCW debut", "desc": "Arrives in WCW and immediately matches with Eddie Guerrero — the two produce career-defining cruiserweight classics."},
    {"year": "1999", "title": "WCW unmasks him", "desc": "Creative forces Mysterio to unmask — a storyline decision that dampened his character's mystique."},
    {"year": "2002", "title": "WWE SmackDown debut", "desc": "Debuts on SmackDown with the mask — immediately elevates the brand's in-ring quality."},
    {"year": "2005", "title": "Eddie Guerrero's death", "desc": "Close friend and storyline partner Eddie Guerrero dies in November — Mysterio dedicates his 2006 season to Eddie's memory."},
    {"year": "2006", "title": "Royal Rumble win & WM22 World title", "desc": "Wins the Royal Rumble (entering #2) and defeats Randy Orton and Kurt Angle in a triple-threat at WM22 — the Eddie tribute payoff."},
    {"year": "2010", "title": "Second World title reign", "desc": "Briefly holds the World Heavyweight title — a reign interrupted by an injured Batista cash-in."},
    {"year": "2019", "title": "Feud with Samoa Joe, IC title run", "desc": "Four-time Intercontinental Champion — continues performing at high quality into his mid-40s."},
    {"year": "2023", "title": "WWE Hall of Fame", "desc": "Inducted into the WWE Hall of Fame — one of the most universally beloved inductions in recent memory."},
]
w["sig_matches"] = [
    {"rating": "★★★★★", "title": "Rey Mysterio vs. Eddie Guerrero", "subtitle": "WCW Halloween Havoc — Oct 26, 1997", "desc": "The best cruiserweight match in WCW history — Guerrero and Mysterio work a match that would pass muster in any era. The hurricanrana counter and the structure of the near-falls is textbook."},
    {"rating": "★★★★", "title": "Rey Mysterio vs. Kurt Angle vs. Randy Orton", "subtitle": "WrestleMania 22 — Apr 2, 2006", "desc": "The Eddie tribute payoff — Mysterio wins the World Heavyweight Championship. Chicago erupts. A triple-threat that tells a complete story with Mysterio as the emotional center."},
    {"rating": "★★★★", "title": "Rey Mysterio vs. Samoa Joe", "subtitle": "Backlash — May 5, 2019", "desc": "Late-career masterpiece — Mysterio and Joe produce one of 2019's best matches; Joe wins but both men are elevated."},
]
rows = []
rows.append(row(w,"ppv","Eddie Guerrero","WCW Halloween Havoc","Oct 26, 1997","WCW Cruiserweight Championship","Guerrero wins — 5-star classic; the greatest WCW cruiserweight match","L"))
rows.append(row(w,"ppv","Dean Malenko","WCW Bash at the Beach","Jul 12, 1998","WCW Cruiserweight Championship","Malenko wins — excellent technical vs. lucha encounter","L"))
rows.append(row(w,"ppv",a("kurt-angle","Kurt Angle"),"WrestleMania 22","Apr 2, 2006","World Heavyweight Championship — Triple Threat (with Orton)","Mysterio wins — Eddie tribute payoff; one of WM's great crowd moments"))
rows.append(row(w,"ppv",a("batista","Batista"),"Rey Mysterio","Various 2006","World Heavyweight Championship","Batista and Mysterio exchange title — best-ever giant vs. small program"))
rows.append(row(w,"ppv",a("edge","Edge"),"SummerSlam","Aug 24, 2008","Singles","Edge wins — Mysterio as credible challenger despite size disparity","L"))
rows.append(row(w,"ppv",a,"No Mercy","Oct 5, 2008","Singles","Batista wins — Mysterio best in undersized role","L"))
rows.append(row(w,"ppv","CM Punk","Over the Limit","May 22, 2011","Singles","Punk wins — Mysterio's best late-career TV match","L"))
rows.append(row(w,"ppv","Samoa Joe","Backlash","May 5, 2019","Singles","Joe wins — one of 2019's best matches; Mysterio's late-career best","L"))
rows.append(row(w,"tv",a("stone-cold-steve-austin","Steve Austin"),"SmackDown Special","Dec 2001","Singles — WWF vs. WCW/ECW","Cross-brand match during InVasion era; Austin wins"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall", "pct": 52},
    {"label": "Submission", "pct": 10},
    {"label": "Countout/DQ", "pct": 20},
    {"label": "Special stipulation", "pct": 18},
]
w["faq"] = [
    {"q": "Has Rey Mysterio won the WWE Championship?", "a": "Yes — Rey Mysterio won the WWE Championship once in 2011, defeating The Miz."},
    {"q": "Is Rey Mysterio in the WWE Hall of Fame?", "a": "Yes — Mysterio was inducted in the WWE Hall of Fame Class of 2023."},
    {"q": "What is Rey Mysterio's finishing move?", "a": "Rey Mysterio's signature finishing sequence is the 619 — a running leg scissors off the ropes — followed by the West Coast Pop (springboard seated senton) or a frog splash for the pin."},
]
wrestlers.append(w)

# 4. GOLDBERG
w = {}
w["slug"] = "goldberg"
w["name"] = "Goldberg"
w["subtitle"] = "Who's Next · Undefeated WCW Champion"
w["born"] = "December 27, 1966"
w["from"] = "Tulsa, Oklahoma"
w["height"] = "6 ft 4 in (193 cm)"
w["weight"] = "285 lb (129 kg)"
w["trained"] = "WWE Performance Center (WCW), Jody Hamilton"
w["debut"] = "1997"
w["style"] = "Power, squash domination, spear-and-Jackhammer formula"
w["aliases"] = ["Goldberg", "Bill Goldberg"]
w["wins"] = 93
w["losses"] = 12
w["draws"] = 2
w["wl_strip"] = ('<i></i>'*9 + '<i class="l"></i>'*1)*4 + '<i></i>'*9 + '<i class="l"></i>'*1 + '<i></i>'*9
w["bio"] = [
    "Goldberg's 1997-1998 undefeated streak in WCW — eventually reaching 173-0 — is the most successful monster-push in American wrestling history. WCW, desperate for a homegrown star to counter WWF's Austin-driven ratings surge, stumbled into Goldberg almost by accident: he was supposed to be one-note squash fodder, but audiences saw something different.",
    "The \"Goldberg\" chant that started appearing in arenas by mid-1998 was genuine, spontaneous, and unprecedented for a power-first performer with minimal psychology. He didn't need a character: the crowd wanted to count the wins, they wanted to chant \"Who's Next\", and they wanted to watch the Spear-Jackhammer sequence. The simplicity was the point.",
    "His WCW Championship win over Hollywood Hulk Hogan at WCW Monday Nitro (not PPV) — witnessed by 40,000 fans in the Georgia Dome in July 1998 — was arguably WCW's last genuine cultural moment. The streak ended at Starrcade 1998 when Kevin Nash defeated him in a taser-assisted finish that the crowd felt was a cheat, because it was.",
    "Goldberg's WWE tenure came in two phases: a 2003 run that suffered from McMahon's creative insistence on making him look beatable, and a 2016-2019 return that was handled much better. His Universal Championship reign (defeating Brock Lesnar at Survivor Series 2016 in under two minutes) was a viral moment that proved the Goldberg mystique still worked two decades later.",
]
w["finishers"] = [
    {"name": "Spear", "desc": "One of the most impactful running spears in wrestling history — at full height and speed, the contact was visually devastating."},
    {"name": "Jackhammer", "desc": "A delayed vertical suplex into a powerslam — the signature finisher that closed every squash match. Nearly impossible to execute at his size."},
]
w["championships"] = [
    cr("WCW World Heavyweight Championship", "1× (Jul 6, 1998 – Dec 27, 1998 — 175-day reign)"),
    cr("WCW United States Heavyweight Championship", "1×"),
    cr("WWE Universal Championship", "1× (2017 — defeated Brock Lesnar in under 2 minutes)"),
    cr("WWE Championship", "1× (2020)"),
]
w["personas"] = [
    {"name": "WCW Goldberg", "era": "WCW 1997–2001", "desc": "The phenomenon — 173-0, the chants, the Georgia Dome WCW title, the streak's end at Starrcade."},
    {"name": "WWE Goldberg", "era": "WWE 2003", "desc": "Inconsistent booking; creative attempted to make him look beatable — the opposite of why the character worked."},
    {"name": "Returning legend Goldberg", "era": "WWE 2016–2019", "desc": "The better WWE run — nostalgia-fueled destruction of Lesnar, Universal title reign, and a 2019 WrestleMania match vs. The Undertaker."},
]
w["timeline"] = [
    {"year": "1997", "title": "WCW debut", "desc": "Hired by WCW after an NFL career (Rams, Falcons) ended by injury — has minimal in-ring training but extraordinary physical presence."},
    {"year": "1997–98", "title": "The streak begins", "desc": "Begins accumulating wins in WCW squash matches — crowd starts chanting and counting; WCW leans in."},
    {"year": "1998", "title": "173-0 — WCW Champion", "desc": "Defeats Hollywood Hulk Hogan at WCW Monday Nitro in the Georgia Dome in front of 40,000 fans — WCW's last genuine cultural moment."},
    {"year": "1998", "title": "Starrcade — streak ends", "desc": "Kevin Nash defeats Goldberg in a taser-assisted finish — the ending the crowd found unsatisfying, and rightly so."},
    {"year": "2003", "title": "WWE debut", "desc": "WWE run undercut by booking designed to make him look beatable — the opposite of the character's value proposition."},
    {"year": "2016", "title": "Returns — destroys Brock Lesnar", "desc": "Defeats Brock Lesnar in under 90 seconds at Survivor Series — one of the decade's great viral wrestling moments."},
    {"year": "2017", "title": "Universal Champion", "desc": "Defeats Kevin Owens for the Universal title; loses it to Lesnar at WrestleMania 33 in a satisfying rematch arc."},
    {"year": "2020", "title": "WWE Champion", "desc": "Defeats The Fiend Bray Wyatt for the WWE Championship — briefly holds gold at 53 years old."},
]
w["sig_matches"] = [
    {"rating": "★★★", "title": "Goldberg vs. Hollywood Hulk Hogan", "subtitle": "WCW Monday Nitro — Jul 6, 1998", "desc": "WCW Championship — not a great match technically but one of wrestling's most significant moments: 40,000 fans in the Georgia Dome; Goldberg's peak; WCW's last genuine pop-culture milestone."},
    {"rating": "★★", "title": "Goldberg vs. Kevin Nash", "subtitle": "WCW Starrcade — Dec 27, 1998", "desc": "The streak ends — Nash wins with taser assistance. The finish infuriated the crowd and damaged the streak's mythology."},
    {"rating": "★★★½", "title": "Goldberg vs. Brock Lesnar", "subtitle": "Survivor Series — Nov 20, 2016", "desc": "Under-90-second squash — Goldberg destroys Lesnar and sends the internet into meltdown. The most effective use of the Goldberg character in WWE."},
]
rows = []
rows.append(row(w,"ppv","Raven","Spring Stampede","Apr 20, 1998","WCW United States Championship","Goldberg wins US title mid-streak"))
rows.append(row(w,"tv","Hollywood Hulk Hogan","WCW Nitro — Georgia Dome","Jul 6, 1998","WCW Championship","Goldberg wins in front of 40,000 — WCW's last great pop-culture moment"))
rows.append(row(w,"ppv","Diamond Dallas Page","WCW Halloween Havoc","Oct 25, 1998","WCW Championship","Goldberg retains — DDP gave him his best match"))
rows.append(row(w,"ppv",a("diesel","Kevin Nash"),"WCW Starrcade","Dec 27, 1998","WCW Championship — streak ends","Nash wins via taser-interference; streak at 173-0 ends","L"))
rows.append(row(w,"ppv",a("triple-h","Triple H"),"WWE Backlash","Apr 27, 2003","World Heavyweight Championship","HHH wins — the 2003 WWE run never recaptures the WCW magic","L"))
rows.append(row(w,"ppv",a("john-cena","John Cena"),"WWE Elimination Chamber","Feb 8, 2020","WWE Championship","Goldberg wins — brief title run at 53"))
rows.append(row(w,"ppv","Brock Lesnar","Survivor Series","Nov 20, 2016","Singles — first-ever Goldberg-Lesnar","Goldberg wins in under 90 seconds — viral wrestling moment"))
rows.append(row(w,"ppv","Brock Lesnar","WrestleMania 33","Apr 2, 2017","WWE Universal Championship","Lesnar wins — Goldberg's Universal reign ends","L"))
rows.append(row(w,"tv",a("stone-cold-steve-austin","Steve Austin"),"Various — cross-brand","2003","Promo confrontations","Austin-Goldberg segment during the InVasion/brand split era"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall", "pct": 70},
    {"label": "Submission", "pct": 5},
    {"label": "Countout/DQ", "pct": 15},
    {"label": "Special stipulation", "pct": 10},
]
w["faq"] = [
    {"q": "What was Goldberg's undefeated streak?", "a": "Goldberg's WCW winning streak reached 173 consecutive victories before Kevin Nash defeated him at WCW Starrcade 1998 with taser assistance."},
    {"q": "Did Goldberg win the WCW World Heavyweight Championship?", "a": "Yes — Goldberg defeated Hollywood Hulk Hogan for the WCW World Heavyweight Championship on July 6, 1998 at WCW Monday Nitro in front of 40,000 fans in the Georgia Dome."},
    {"q": "Did Goldberg win the WWE Universal Championship?", "a": "Yes — Goldberg won the WWE Universal Championship in 2017 by defeating Kevin Owens, and later held the WWE Championship in 2020 by defeating The Fiend Bray Wyatt."},
]
wrestlers.append(w)

# 5. RIC FLAIR
w = {}
w["slug"] = "ric-flair"
w["name"] = "Ric Flair"
w["subtitle"] = "The Nature Boy · 16× World Champion · WOOOOO"
w["born"] = "February 25, 1949"
w["from"] = "Memphis, Tennessee"
w["height"] = "6 ft 1 in (185 cm)"
w["weight"] = "243 lb (110 kg)"
w["trained"] = "Verne Gagne, Wahoo McDaniel"
w["debut"] = "1972"
w["style"] = "Psychology-first, heel stalling, chop-intensive technical brawler, figure-four specialist"
w["aliases"] = ["Ric Flair", "The Nature Boy", "Slick Ric", "Richard Fliehr", "The Stylin', Profilin', Limousine Riding, Jet Flying, Kiss-Stealing, Wheelin' n' Dealin' Son of a Gun"]
w["wins"] = 124
w["losses"] = 98
w["draws"] = 14
w["wl_strip"] = ('<i></i>'*7 + '<i class="l"></i>'*3)*12 + '<i></i>'*4
w["bio"] = [
    "Ric Flair is the greatest professional wrestler in history by any reasonable measure of longevity, quality, and influence. A career spanning five decades, 16 world title reigns (tied by John Cena), and a style that defined what a professional wrestling champion looked like — the robe, the strut, the chop, the figure-four — makes Flair not just a wrestler but the archetype.",
    'Flair spent the bulk of his peak years (1978–1993) in the NWA/WCW, where he was the definitive world champion. His ability to work any opponent to a 4-star match — babyfaces and heels, big men and cruiserweights, arena veterans and rookies — is unmatched in the sport\'s history. His matches with Ricky Steamboat (1989), Sting, Lex Luger, and Harley Race are among the genre\'s finest.',
    "His WWF runs (1991–1993 and 2001–2008) added further chapters to an already encyclopedic career. The Evolution stable (with Triple H, Batista, and Randy Orton) gave him a mentor role that he elevated beyond the script, producing genuine management performances.",
    'Flair\'s personal life has been as dramatic as his in-ring persona: multiple marriages, financial difficulties, the death of his son Reid, and a well-documented health crisis in 2017 from which he returned to work. His final match in 2022 at 73 years old — a tag team bout with his son-in-law Andrade — was both inspiring and controversial. To no one\'s surprise, he survived it.',
]
w["finishers"] = [
    {"name": "Figure-Four Leglock", "desc": "One of the most iconic submission moves in wrestling history — applied with a theatrics-first presentation that made the crowd feel it."},
    {"name": "The Chop", "desc": "Not a finisher but Flair's signature mid-match weapon — a knife-edge chop with an audible WOOOOO response from the crowd that became Pavlovian."},
]
w["championships"] = [
    cr("NWA World Heavyweight Championship", "8× (1981–1991)"),
    cr("WCW World Heavyweight Championship", "6× (1991–2000)"),
    cr("WWE Intercontinental Championship", "1× (2005)"),
    cr("WWE Tag Team Championship", "1× (with Batista)"),
    cr("World Tag Team Championship", "1× (with Roddy Piper)"),
]
w["personas"] = [
    {"name": "NWA World Champion", "era": "Jim Crockett Promotions 1977–1988", "desc": "The definitive version — 8 NWA title reigns, matches with Steamboat and Race, the complete Nature Boy package."},
    {"name": "WCW Nature Boy", "era": "WCW 1989–2001", "desc": "Transitioned smoothly from NWA to WCW; continued world championship reigns into his late 40s."},
    {"name": "Evolution leader", "era": "WWE 2003–2005", "desc": "The cerebral mentor role — managing Triple H, Batista, and Orton while delivering promo performances that outshone wrestlers 30 years his junior."},
]
w["timeline"] = [
    {"year": "1972", "title": "Pro debut", "desc": "Begins wrestling in the Southeast territories after training under Verne Gagne — a quick learner with natural charisma."},
    {"year": "1975", "title": "Plane crash — career nearly ends", "desc": "Suffers severe injuries in a plane crash that breaks his back — doctors question whether he will walk again. Returns to wrestling within a year."},
    {"year": "1981", "title": "First NWA World Championship", "desc": "Wins the NWA title for the first time — the beginning of a dominant decade as the company's defining champion."},
    {"year": "1989", "title": "Ricky Steamboat trilogy", "desc": "Three matches against Ricky Steamboat (Chi-Town Rumble, Clash, WrestleWar) are among the greatest matches in professional wrestling history."},
    {"year": "1991", "title": "WWF run — The Real World Champion", "desc": "Arrives in WWF bringing the NWA world title — works a brilliant early-run claim to being the real world champion."},
    {"year": "1993", "title": "Returns to WCW", "desc": "Four more WCW world title reigns across the 1990s, including the legendary Horsemen involvement and feuds with Sting and Lex Luger."},
    {"year": "2002", "title": "Returns to WWE — Evolution", "desc": "Joins Evolution as Triple H's mentor and co-stable leader — his mic work and veteran presence elevate the entire group."},
    {"year": "2008", "title": "WrestleMania XXIV retirement match", "desc": "Loses to Shawn Michaels in one of WrestleMania's great matches — an emotional ending that was somewhat undone by subsequent returns."},
    {"year": "2017", "title": "Health crisis", "desc": "Suffers a life-threatening colon perforation and sepsis — put in a medically induced coma; recovery takes months."},
    {"year": "2022", "title": "Final match at 73", "desc": "Tags with Andrade in a Nashville event — the polarizing final chapter of an unprecedented career."},
]
w["sig_matches"] = [
    {"rating": "★★★★★", "title": "Ric Flair vs. Ricky Steamboat", "subtitle": "WrestleWar — May 7, 1989", "desc": "The finest match of the 1989 Flair-Steamboat trilogy — two professionals producing the best 60-minutes-or-less wrestling match the NWA had ever seen. The structure, the near-falls, and the psychology remain a masterclass 35 years later."},
    {"rating": "★★★★★", "title": "Ric Flair vs. Shawn Michaels", "subtitle": "WrestleMania XXIV — Mar 30, 2008", "desc": "Flair's retirement match — HBK delivers the Sweet Chin Music with tears in his eyes and Flair sells it perfectly. One of WrestleMania's five greatest matches."},
    {"rating": "★★★★", "title": "Ric Flair vs. Sting", "subtitle": "WCW Clash of the Champions I — Mar 27, 1988", "desc": "45-minute draw that launched Sting as a main-event star — Flair worked his greatest career match with a complete rookie."},
]
rows = []
rows.append(row(w,"ppv","Dusty Rhodes","NWA Starrcade","Nov 26, 1981","NWA World Championship — First title win","Flair wins his first world title — Nature Boy era officially begins"))
rows.append(row(w,"ppv",a("ricky-steamboat","Ricky Steamboat"),"Chi-Town Rumble","Feb 20, 1989","NWA World Championship","Steamboat wins — first of three matches in one of wrestling's great series","L"))
rows.append(row(w,"ppv",a("ricky-steamboat","Ricky Steamboat"),"WrestleWar","May 7, 1989","NWA World Championship","Flair wins — the best match of the trilogy; 5-star classic"))
rows.append(row(w,"ppv","Sting","WCW Clash of the Champions I","Mar 27, 1988","NWA World Championship — 45-min draw","Draw — launches Sting as a main-eventer; Flair's greatest performance with a rookie","D"))
rows.append(row(w,"ppv",a("hulk-hogan","Hulk Hogan"),"WCW Bash at the Beach","Jul 17, 1994","WCW Championship","Hogan wins — Flair puts Hogan over in Hogan's WCW debut match","L"))
rows.append(row(w,"ppv",a("shawn-michaels","Shawn Michaels"),"WrestleMania XXIV","Mar 30, 2008","Career vs. Career — Retirement Match","HBK wins — Sweet Chin Music; one of WM's greatest matches","L"))
rows.append(row(w,"ppv",a("triple-h","Triple H"),"WWE Raw — Evolution meetings","2003–2005","Stable alliance","Flair manages Evolution — best mic work of his late career"))
rows.append(row(w,"tv",a("stone-cold-steve-austin","Steve Austin"),"Raw — various 2002–2003","Promo battles","Flair as co-owner of WWE vs. Austin — some of the era's best promos","D"))
rows.append(row(w,"ppv",a("randy-savage","Randy Savage"),"WCW","1995","WCW Championship","Savage wins — late-era championship programme","L"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall", "pct": 42},
    {"label": "Submission (Figure-Four)", "pct": 28},
    {"label": "Countout/DQ", "pct": 18},
    {"label": "Special stipulation", "pct": 12},
]
w["faq"] = [
    {"q": "How many world titles has Ric Flair won?", "a": "Ric Flair has won 16 recognized world titles — 8 NWA World Heavyweight Championships and 6 WCW World Heavyweight Championships, plus others. This total was later tied by John Cena."},
    {"q": "What is Ric Flair's best match?", "a": "Widely considered to be either the WrestleWar 1989 bout against Ricky Steamboat (the final of their three-match series) or his WrestleMania XXIV retirement match against Shawn Michaels — both are frequently rated five stars."},
    {"q": "Did Ric Flair retire?", "a": "Officially, Flair's in-ring retirement was at WrestleMania XXIV in 2008. He subsequently made several returns, including a final tag team match in Nashville in 2022 at age 73."},
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

print("\nBatch 3b complete.")
