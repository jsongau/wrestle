#!/usr/bin/env python3
"""Batch 4b: Seth Rollins, Dean Ambrose/Jon Moxley, AJ Styles, Kevin Owens, Savio Vega"""
import os, datetime

BASE = "/root/wwe/wrestlers"

def cr(title, reign, note=""):
    note_html = '<span class="cr-note">' + note + '</span>' if note else ""
    return f'    <div class="champ-row"><span class="cr-title">{title}</span><span class="cr-reign">{reign}</span>{note_html}</div>\n'

def a(slug, name):
    return f'<a href="/wrestlers/{slug}/">{name}</a>'

def row(w, kind, opp, event, date, stipulation, note, result="W"):
    return (f'<tr class="record-row" data-result="{result}" data-cats="{kind}">'
            f'<td class="res-cell"><span class="res-badge{" res-l" if result=="L" else " res-d" if result=="D" else ""}">{result}</span></td>'
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

    bio_html = "".join(f"<p>{p}</p>\n" for p in bio_paras)
    fin_html = "".join(f'<li><strong>{f["name"]}</strong> — {f["desc"]}</li>\n' for f in finishers)
    champ_html = "".join(championships)

    persona_html = ""
    if personas:
        persona_html = '<div class="persona-grid">\n'
        for p in personas:
            persona_html += (f'<div class="persona-card"><h3>{p["name"]}</h3>'
                             f'<p class="dim">{p["era"]}</p><p>{p["desc"]}</p></div>\n')
        persona_html += '</div>\n'

    tl_html = "".join(f'<li><time>{t["year"]}</time><h3>{t["title"]}</h3><p>{t["desc"]}</p></li>\n' for t in timeline_items)

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

    faq_html = "".join(f'<details><summary>{q["q"]}</summary><p>{q["a"]}</p></details>\n' for q in faq)

    mb_html = "".join(
        f'<div class="mb-row"><span class="mb-label">{m["label"]}</span>'
        f'<div class="mb-track"><div class="mb-fill" style="--w:{m["pct"]}%"></div></div>'
        f'<span class="mb-pct">{m["pct"]}%</span></div>\n'
        for m in method_bars)

    aliases_html = ""
    if aliases:
        aliases_html = '<p class="dim">Also known as: ' + ", ".join(aliases) + '</p>\n'

    champ_block = ""
    if champ_html:
        champ_block = '<h2>Championships &amp; Titles</h2>\n<div class="champ-panel"><div class="champ-rows">\n' + champ_html + '</div></div>\n'
    persona_block = ('<h2>Personas &amp; Characters</h2>\n' + persona_html) if persona_html else ""
    timeline_block = ('<h2>Career Timeline</h2>\n<ol class="timeline">\n' + tl_html + '</ol>\n') if tl_html else ""
    faq_block = ('<h2>FAQ</h2>\n<div class="faq-block">\n' + faq_html + '</div>\n') if faq_html else ""
    faq_ld_block = (',\n    {"@type":"FAQPage","mainEntity":[' + faq_items_ld + ']}') if faq else ""
    retired_html = ("<dt>Retired</dt><dd>" + retired + "</dd>") if retired else ""

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
    {{"@type":"Person","name":"{name}","description":"{subtitle}","birthDate":"{born}","birthPlace":"{from_loc}","jobTitle":"Professional Wrestler","url":"https://matdb.io/wrestlers/{slug}/"}},
    {{"@type":"BreadcrumbList","itemListElement":[
      {{"@type":"ListItem","position":1,"name":"Home","item":"https://matdb.io/"}},
      {{"@type":"ListItem","position":2,"name":"Wrestlers","item":"https://matdb.io/wrestlers/"}},
      {{"@type":"ListItem","position":3,"name":"{name}","item":"https://matdb.io/wrestlers/{slug}/"}}
    ]}}{faq_ld_block}
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
  <nav aria-label="Footer"><a href="/about/">About</a> <a href="/contact/">Contact</a> <a href="/privacy/">Privacy</a></nav>
</footer>
<script src="/js/main.js"></script>
<script src="/js/enhance.js"></script>
</body>
</html>"""

# ---------------------------------------------------------------------------
wrestlers = []

# 1. SETH ROLLINS
w = {}
w["slug"] = "seth-rollins"
w["name"] = "Seth Rollins"
w["subtitle"] = "The Visionary · Monday Night Messiah · 3× World Champion"
w["born"] = "May 28, 1986"
w["from"] = "Davenport, Iowa"
w["height"] = "6 ft 1 in (185 cm)"
w["weight"] = "217 lb (98 kg)"
w["trained"] = "AIWF Midwest (Larry Zbyszko school), Ring of Honor"
w["debut"] = "2005"
w["style"] = "High-flying technical, Phoenix Splash, methodical storytelling, best-in-show quality"
w["aliases"] = ["Seth Rollins", "Colby Lopez", "Tyler Black", "The Architect", "The Visionary", "Monday Night Messiah", "The Revolutionary"]
w["wins"] = 81
w["losses"] = 58
w["draws"] = 3
w["wl_strip"] = ('<i></i>'*7 + '<i class="l"></i>'*3)*7 + '<i></i>'*7
w["bio"] = [
    "Seth Rollins is the best complete professional wrestler on the WWE roster over the last decade. When the conversation turns to who can have a five-star match with anyone, Rollins's name appears first. His combination of aerial athleticism (Phoenix Splash, Frog Splash, Curb Stomp) and technical wrestling intelligence places him in the company of AJ Styles as WWE's most reliable in-ring asset.",
    "Rollins's career has three clear phases: the Ring of Honor era as Tyler Black (ROH World Champion, some of that era's finest matches), the Shield era (the cerebral architect of the dominant faction), and his extraordinary solo run that began the moment he cashed in Money in the Bank on Brock Lesnar to steal WrestleMania 31's main event.",
    "The WM31 cash-in — interrupting a Lesnar vs. Reigns main event the crowd had mixed feelings about, pivoting the entire night in under five minutes — is the best in-the-moment wrestling booking decision in recent memory. Rollins becomes the champion, the crowd erupts, and the event ends on an unexpected high note that nobody in the building predicted.",
    "As a heel character (The Architect, Monday Night Messiah, The Visionary), Rollins's promo ability and character work are as impressive as his in-ring output. His feud with Cody Rhodes that culminated at WrestleMania XL produced one of the most complete wrestling feuds of the decade.",
]
w["finishers"] = [
    {"name": "Curb Stomp (Pedigree Stomp)", "desc": "Running double-foot stomp to a kneeling opponent — one of wrestling's most visually distinctive finishers; briefly banned due to injury concerns then reinstated."},
    {"name": "Phoenix Splash", "desc": "720-degree corkscrew moonsault from the top rope — used less frequently now but one of the most athletic moves in wrestling when executed."},
]
w["championships"] = [
    cr("WWE World Heavyweight Championship", "2× (2023 — current era)"),
    cr("WWE Championship", "1× (2015 — cashed in at WM31)"),
    cr("WWE Universal Championship", "1× (2019)"),
    cr("ROH World Championship", "1× (as Tyler Black, 2010)"),
    cr("WWE Intercontinental Championship", "3×"),
    cr("WWE United States Championship", "1×"),
    cr("WWE Tag Team Championship", "4× (with Roman Reigns, John Cena, and others)"),
]
w["personas"] = [
    {"name": "Tyler Black", "era": "ROH 2007–2010", "desc": "The Ring of Honor era — extraordinary matches with Bryan Danielson, Austin Aries, and others; ROH World Champion."},
    {"name": "The Shield architect", "era": "WWE 2012–2014", "desc": "The cerebral one who holds the Shield together and is most clearly going to succeed in singles."},
    {"name": "The Architect / Visionary / Messiah", "era": "WWE 2014–present", "desc": "Multiple character iterations, all effective — Rollins's versatility as a performer allows total reinvention."},
]
w["timeline"] = [
    {"year": "2005", "title": "Pro debut", "desc": "Begins wrestling in Iowa and the Midwest independent circuit as Colby Lopez."},
    {"year": "2010", "title": "ROH World Champion as Tyler Black", "desc": "Wins the ROH World Championship — one of the most complete indie performers of his generation."},
    {"year": "2012", "title": "WWE debut as The Shield", "desc": "Arrives alongside Reigns and Ambrose at Survivor Series — The Shield is immediately the most compelling act in WWE."},
    {"year": "2014", "title": "Shield betrayal", "desc": "Turns on The Shield in June 2014 to join Evolution — the chair shot heard round the world; starts his best singles character work."},
    {"year": "2015", "title": "WrestleMania 31 MITB cash-in", "desc": "Interrupts Lesnar vs. Reigns to cash in MITB — wins WWE title; the crowd reaction is the highlight of WM31."},
    {"year": "2017", "title": "Knee injury — extended absence", "desc": "Torn knee ligaments sideline him — returns stronger with refined character work."},
    {"year": "2019", "title": "Universal Champion — vs. Becky Lynch", "desc": "His most sustained top-level run — feuds with Rollins and others while holding the Universal title."},
    {"year": "2023–24", "title": "World Heavyweight Champion — Cody feud", "desc": "The Rollins-Rhodes feud is one of WWE's best in years — culminates in WM XL Night 1 in an instant-classic match."},
]
w["sig_matches"] = [
    {"rating": "★★★★★", "title": "Seth Rollins vs. Cody Rhodes", "subtitle": "WrestleMania XL Night 1 — Apr 6, 2024", "desc": "World Heavyweight Championship — one of WrestleMania's all-time great matches. Rollins and Rhodes work a 45-minute epic with multiple near-falls that brought the Philadelphia crowd to their feet repeatedly. Rollins's best-ever performance."},
    {"rating": "★★★★½", "title": "Seth Rollins vs. John Cena", "subtitle": "Royal Rumble — Jan 25, 2015", "desc": "WWE Championship — Rollins's best title defense; works Cena to the best singles performance Cena had in 2015; the ladder of near-falls is beautifully constructed."},
    {"rating": "★★★★½", "title": "Seth Rollins vs. Shawn Michaels", "subtitle": "Monday Night Raw — Oct 27, 2014", "desc": "A surprise TV match that produced one of the best Raw matches in years — HBK comes out of retirement briefly; Rollins keeps up with the greatest of all time."},
]
rows = []
rows.append(row(w,"ppv",a("brock-lesnar","Brock Lesnar"),"WrestleMania 31 — MITB","Mar 29, 2015","WWE Championship — MITB cash-in during Lesnar vs. Reigns","Rollins wins — the best in-match cash-in in MITB history"))
rows.append(row(w,"ppv",a("john-cena","John Cena"),"Royal Rumble","Jan 25, 2015","WWE Championship","Rollins retains — their best singles match; a forgotten gem","W"))
rows.append(row(w,"ppv",a("randy-orton","Randy Orton"),"WrestleMania 31","Mar 29, 2015","Singles (before cash-in)","Orton RKO outta nowhere — one of wrestling's all-time spots","L"))
rows.append(row(w,"ppv",a("roman-reigns","Roman Reigns"),"Money in the Bank","Jun 19, 2016","WWE Championship","Reigns wins — Rollins' injury storyline picks up","L"))
rows.append(row(w,"ppv",a("cm-punk","CM Punk"),"WrestleMania XL Night 1","Apr 6, 2024","World Heavyweight Championship vs. Cody Rhodes","Rhodes wins in 45-min epic — instant-classic WM match","L"))
rows.append(row(w,"ppv","AJ Styles","Royal Rumble","Jan 28, 2017","Singles","AJ wins — AJ's best performance of the year","L"))
rows.append(row(w,"ppv",a("brock-lesnar","Brock Lesnar"),"SummerSlam","Aug 11, 2019","Universal Championship","Rollins retains via DQ — one of 2019's most physical matches","W"))
rows.append(row(w,"tv",a("stone-cold-steve-austin","Steve Austin"),"Raw 20th Anniversary era","2013","Shield-era interaction","The Shield prevents Austin from opening Raw segment; crowd heat"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall", "pct": 52},
    {"label": "Submission", "pct": 12},
    {"label": "Curb Stomp (KO)", "pct": 18},
    {"label": "Countout/DQ", "pct": 10},
    {"label": "Special stipulation", "pct": 8},
]
w["faq"] = [
    {"q": "Who is Seth Rollins's finishing move?", "a": "Seth Rollins's primary finishing move is the Curb Stomp — a running double-foot stomp to a kneeling opponent's head. He also uses the Phoenix Splash (a 720-degree corkscrew moonsault) in key matches."},
    {"q": "Did Seth Rollins really cash in Money in the Bank at WrestleMania?", "a": "Yes — Seth Rollins cashed in his Money in the Bank contract during the Brock Lesnar vs. Roman Reigns main event of WrestleMania 31, winning the WWE Championship in one of the great in-event surprise moments in WrestleMania history."},
]
wrestlers.append(w)

# 2. JON MOXLEY (Dean Ambrose)
w = {}
w["slug"] = "jon-moxley"
w["name"] = "Jon Moxley"
w["subtitle"] = "Dean Ambrose · AEW World Champion · The Purveyor of Violence"
w["born"] = "December 7, 1985"
w["from"] = "Cincinnati, Ohio"
w["height"] = "6 ft 4 in (193 cm)"
w["weight"] = "234 lb (106 kg)"
w["trained"] = "Les Thatcher (Cincinnati), HWA"
w["debut"] = "2004"
w["style"] = "Brawler, death-match specialist, psychological storytelling, technical ground game"
w["aliases"] = ["Jon Moxley", "Dean Ambrose", "Jonathan Good", "The Lunatic Fringe", "The Unstable", "Purveyor of Violence"]
w["wins"] = 83
w["losses"] = 48
w["draws"] = 4
w["wl_strip"] = ('<i></i>'*8 + '<i class="l"></i>'*2)*7 + '<i></i>'*9
w["bio"] = [
    "Jon Moxley is one of professional wrestling's most complete performers and its most interesting story. His WWE career as Dean Ambrose — characterized by an intensity and looseness that felt genuinely unpredictable — never fully captured what the live crowds sensed the character could be. His AEW career as Jon Moxley, freed from creative constraints, revealed a performer operating at the top of the profession.",
    "The Shield era (2012–2014) gave Ambrose the platform his raw talent demanded: alongside Seth Rollins and Roman Reigns, he was the most volatile and watchable member of wrestling's most compelling faction. His singles work after the Shield disbanded — particularly the brutal match with Seth Rollins at Hell in a Cell 2014 and his WWE Championship reigns — demonstrated a performer capable of carrying a company.",
    "His 2019 departure from WWE and immediate debut in AEW as Jon Moxley (a name he had used throughout his pre-WWE indie career) was one of the more significant free-agency decisions in wrestling history. It confirmed that a performer who had chafed under creative restrictions could, when given freedom, produce work that justified every instinct critics had suspected.",
    "Three AEW World Championship reigns, multiple acclaimed death-match performances, and a sustained run as one of the most reliable main-event draws in pro wrestling establish Moxley as a top-five performer of his generation. His work in New Japan, GCW, and AEW alongside WWE colleagues-turned-competitors represents the most productive creative freedom wrestling has seen.",
]
w["finishers"] = [
    {"name": "Paradigm Shift (Dirty Deeds)", "desc": "Double underhook DDT — one of the most consistently protected finishers in wrestling; rarely kicked out of and always impactful."},
    {"name": "Bulldog Choke", "desc": "His submission finish — the rear naked choke applied from a bulldog position; a legitimate submission with a grappling credibility."},
]
w["championships"] = [
    cr("AEW World Championship", "3× (2019, 2022, 2023)"),
    cr("IWGP United States Championship", "1×"),
    cr("WWE Championship", "1× (2016)"),
    cr("WWE Intercontinental Championship", "2×"),
    cr("WWE United States Championship", "1×"),
    cr("GCW World Championship", "1×"),
]
w["personas"] = [
    {"name": "Dean Ambrose / The Lunatic Fringe", "era": "WWE 2012–2019", "desc": "The loose cannon of The Shield and then the unpredictable solo performer — never fully channelled by WWE creative."},
    {"name": "Jon Moxley", "era": "AEW / indie 2019–present", "desc": "The complete realization — Moxley freed from creative constraints became one of the industry's finest performers."},
]
w["timeline"] = [
    {"year": "2004", "title": "Pro debut in Cincinnati", "desc": "Begins wrestling in the Heartland Wrestling Association — immediately distinguishable by intensity and natural character."},
    {"year": "2011", "title": "WWE developmental", "desc": "Signs with WWE and begins in FCW developmental — arrives on the main roster as part of The Shield."},
    {"year": "2012", "title": "The Shield debut", "desc": "Arrives at Survivor Series alongside Rollins and Reigns — the most compelling debut since The Nexus."},
    {"year": "2014", "title": "Shield disbands — Hell in a Cell vs. Rollins", "desc": "His Shield-era solo peak — the Hell in a Cell match with Rollins at HIAC 2014 is the best cell match since Austin-Undertaker."},
    {"year": "2016", "title": "WWE Champion", "desc": "Wins the WWE Championship in a money-in-the-bank cash-in style at Money in the Bank — his first world title."},
    {"year": "2018", "title": "Short-lived heel turn, creative frustrations", "desc": "Brief heel run as a doctor character that failed to connect — his frustration with WWE creative becomes public."},
    {"year": "2019", "title": "AEW debut at Double or Nothing", "desc": "Debuts in AEW at the inaugural Double or Nothing event — one of wrestling's great surprise appearances."},
    {"year": "2019–23", "title": "Three AEW World titles", "desc": "Becomes the face of AEW alongside Chris Jericho — three reigns that establish the company's championship prestige."},
]
w["sig_matches"] = [
    {"rating": "★★★★½", "title": "Dean Ambrose vs. Seth Rollins", "subtitle": "Hell in a Cell — Oct 26, 2014", "desc": "The betrayal made personal inside the Cell — Ambrose and Rollins in a brutal, emotionally resonant cell match that was the best Cell match in a decade."},
    {"rating": "★★★★", "title": "Jon Moxley vs. Kenny Omega", "subtitle": "AEW Double or Nothing — May 23, 2020", "desc": "Unsanctioned street fight — a brutal, intense brawl that made Moxley the face of AEW's main-event ambitions. Both men bled; the crowd was invested throughout."},
    {"rating": "★★★★", "title": "Jon Moxley vs. Bryan Danielson", "subtitle": "AEW — 2021", "desc": "A series of matches that produced the best in-ring work of both careers — Moxley and Danielson as peers in technical violence is the match-up AEW needed."},
]
rows = []
rows.append(row(w,"ppv",a("seth-rollins","Seth Rollins"),"Hell in a Cell","Oct 26, 2014","Hell in a Cell — Rollins betrayal payoff","One of the best Cell matches in a decade; Ambrose loses but the match is his"))
rows.append(row(w,"ppv",a("brock-lesnar","Brock Lesnar"),"WrestleMania 32","Apr 3, 2016","Singles — No Holds Barred","Lesnar wins — Ambrose's best WM showing; chainsaw props and all","L"))
rows.append(row(w,"ppv","The Miz","Money in the Bank","Jun 19, 2016","WWE Championship","Ambrose wins — his first and only WWE world title"))
rows.append(row(w,"ppv","Kenny Omega","AEW Double or Nothing","May 23, 2020","Unsanctioned Street Fight","Moxley wins — AEW's best match to that date"))
rows.append(row(w,"ppv","Chris Jericho","AEW Revolution","Feb 29, 2020","AEW World Championship","Moxley wins his second AEW title — Jericho match is their best"))
rows.append(row(w,"ppv","Bryan Danielson","AEW","2021","Series of matches","Danielson vs. Moxley — AEW's best sustained programme of 2021","D"))
rows.append(row(w,"tv",a("stone-cold-steve-austin","Steve Austin"),"Raw — Ambrose era","2016","Promo segment","Austin promo appearance; Ambrose closest modern equivalent to Austin's lunatic energy"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall", "pct": 48},
    {"label": "Submission (Bulldog Choke)", "pct": 22},
    {"label": "Countout/DQ", "pct": 14},
    {"label": "Special stipulation", "pct": 16},
]
w["faq"] = [
    {"q": "What is the difference between Dean Ambrose and Jon Moxley?", "a": "Dean Ambrose was Jon Moxley's ring name in WWE (2012-2019). When he left WWE in 2019, he reverted to Jon Moxley — the name he used throughout his pre-WWE independent career. The two names refer to the same performer."},
    {"q": "How many world titles has Jon Moxley won?", "a": "Jon Moxley has won 3 AEW World Championships, 1 WWE Championship, 1 IWGP United States Championship, and 1 GCW World Championship — making him a multi-time world champion across multiple major promotions."},
]
wrestlers.append(w)

# 3. AJ STYLES
w = {}
w["slug"] = "aj-styles"
w["name"] = "AJ Styles"
w["subtitle"] = "The Phenomenal One · WWE Champion · TNA Legend"
w["born"] = "June 2, 1977"
w["from"] = "Gainesville, Georgia"
w["height"] = "5 ft 11 in (180 cm)"
w["weight"] = "218 lb (99 kg)"
w["trained"] = "Rick Michaels, WCW Power Plant graduates"
w["debut"] = "1998"
w["style"] = "Phenomenal — aerial, technical, Calf Crusher specialist, Styles Clash and Phenomenal Forearm"
w["aliases"] = ["AJ Styles", "Allen Jones", "The Phenomenal One", "The Face That Runs the Place"]
w["wins"] = 86
w["losses"] = 64
w["draws"] = 5
w["wl_strip"] = ('<i></i>'*7 + '<i class="l"></i>'*3)*8 + '<i></i>'*2
w["bio"] = [
    "AJ Styles is one of the two or three most technically gifted performers in professional wrestling history. A career spanning nearly three decades and every major promotion on earth — WWE, TNA/IMPACT, ROH, NJPW, and dozens of independent promotions — has produced an essentially matchless body of work.",
    "Styles built his reputation in TNA/IMPACT Wrestling (2002–2014), where as a founding performer he became synonymous with the company's in-ring quality. His feuds with Christopher Daniels and Samoa Joe in TNA produced matches that belonged alongside anything WWE produced in the same period — a fact that made his WWE arrival in 2016 all the more anticipated.",
    "The Royal Rumble 2016 debut — in at number 3, to a thunderous reception from a crowd that was not supposed to be able to cheer him — announced that WWE had acquired the best wrestler not under contract. His subsequent feuds with John Cena (including a three-match series that is among the best of either man's career), Roman Reigns, and Samoa Joe established him as a legitimate world-class main-eventer in WWE's top promotion.",
    "At 47, Styles continues to produce match-quality that rivals performers 20 years his junior. The longevity speaks to an exceptional physical intelligence: he has adapted his style over the decades, adding heel technical psychology to the aerial work of his youth, and remains one of the safest workers in the business for his opponents.",
]
w["finishers"] = [
    {"name": "Styles Clash", "desc": "A face-down piledriver variant — the most distinctive setup in wrestling and a finish that immediately pops any crowd who recognizes what's coming."},
    {"name": "Phenomenal Forearm", "desc": "A springboard forearm from the ring apron to a standing opponent — Styles's signature big match finish; athletically incredible at any age."},
    {"name": "Calf Crusher", "desc": "A modified knee-compression submission — used as a secondary finish and an effective match-story device."},
]
w["championships"] = [
    cr("WWE Championship", "2× (2016–2017, 2018–2019)"),
    cr("United States Championship", "3×"),
    cr("Intercontinental Championship", "2×"),
    cr("TNA World Heavyweight Championship", "5×"),
    cr("IWGP Heavyweight Championship", "1× (New Japan, 2014)"),
    cr("ROH World Championship", "1×"),
    cr("NWA World Heavyweight Championship", "1×"),
]
w["personas"] = [
    {"name": "TNA AJ Styles", "era": "TNA 2002–2014", "desc": "The foundation — six world titles in TNA, extraordinary in-ring reputation, the best American wrestler not in WWE."},
    {"name": "Bullet Club AJ Styles", "era": "NJPW 2014–2016", "desc": "The NJPW run that polished the heel character — leading Bullet Club made Styles a global star before the WWE debut."},
    {"name": "The Phenomenal One (WWE)", "era": "WWE 2016–present", "desc": "The culmination — world-class performer finally on the world's largest stage; two WWE Championship reigns."},
]
w["timeline"] = [
    {"year": "1998", "title": "Pro debut", "desc": "Begins wrestling in Georgia and the Southeast independent circuit."},
    {"year": "2002", "title": "TNA/IMPACT co-founder", "desc": "Joins TNA as a founding performer — immediately one of the best wrestlers in America."},
    {"year": "2005", "title": "Styles vs. Daniels vs. Samoa Joe", "desc": "The Ultimate X and Unbreakable triple threat match — one of wrestling's all-time great triple threats; TNA's finest moment."},
    {"year": "2014", "title": "New Japan and Bullet Club", "desc": "Joins NJPW and becomes the leader of Bullet Club — wins the IWGP Heavyweight title; global reputation solidifies."},
    {"year": "2016", "title": "WWE debut — Royal Rumble", "desc": "Enters the Royal Rumble at number 3 to one of wrestling's great unannounced surprise reactions."},
    {"year": "2016", "title": "First WWE Championship", "desc": "Defeats Dean Ambrose for the WWE Championship on SmackDown — SmackDown is immediately reestablished as a flagship product."},
    {"year": "2016", "title": "Feud with John Cena — 3-match series", "desc": "SummerSlam, No Mercy, and Royal Rumble — one of the great trilogy feuds in WWE."},
    {"year": "2018", "title": "Second WWE title reign", "desc": "Second WWE title reign — longer, more sustained; feuds with Samoa Joe, Cesaro, and Daniel Bryan."},
    {"year": "2023–24", "title": "US title and current era", "desc": "Continues performing at elite level into his late 40s — one of the sport's great career longevity stories."},
]
w["sig_matches"] = [
    {"rating": "★★★★★", "title": "AJ Styles vs. Christopher Daniels vs. Samoa Joe", "subtitle": "TNA Unbreakable — Sep 11, 2005", "desc": "The greatest triple threat match in wrestling history — flawless structure, zero dead time, and three performers at their absolute peak. Styles pins Daniels while Joe slumps outside; the crowd comes apart."},
    {"rating": "★★★★½", "title": "AJ Styles vs. John Cena", "subtitle": "SummerSlam — Aug 21, 2016", "desc": "Styles's WWE breakthrough performance — defeats Cena clean in what many considered the best SummerSlam match in over a decade. The crowd's investment throughout proved the move to WWE was the right call."},
    {"rating": "★★★★½", "title": "AJ Styles vs. Samoa Joe", "subtitle": "WWE Championship — TakeOver-era matches, 2018", "desc": "Their best WWE encounter — a series of matches that recalled the TNA magic; the Calf Crusher vs. the Kokina Clutch as a submission war is compelling storytelling."},
]
rows = []
rows.append(row(w,"ppv","Christopher Daniels","TNA Unbreakable (Triple Threat)","Sep 11, 2005","TNA World Championship","Styles wins in the greatest triple threat match in wrestling history"))
rows.append(row(w,"ppv","Dean Ambrose","SmackDown 900","Sep 11, 2016","WWE Championship — SmackDown live","Styles wins his first WWE title on SmackDown's milestone show"))
rows.append(row(w,"ppv",a("john-cena","John Cena"),"SummerSlam","Aug 21, 2016","Singles","Styles wins clean — best SummerSlam match in over a decade; Styles WWE breakthrough"))
rows.append(row(w,"ppv","Samoa Joe","WWE Championship","2018","WWE Championship — series","Styles and Joe exchange suplexes and submissions — one of WWE's best feuds of 2018"))
rows.append(row(w,"ppv",a("roman-reigns","Roman Reigns"),"WrestleMania 33","Apr 2, 2017","Singles","Reigns wins — their best singles match; Styles makes Reigns look legitimate","L"))
rows.append(row(w,"ppv",a("brock-lesnar","Brock Lesnar"),"Survivor Series","Nov 19, 2017","WWE vs. Universal Brand","Lesnar wins in a match that exceeded all expectations","L"))
rows.append(row(w,"ppv","Shinsuke Nakamura","WrestleMania 34","Apr 8, 2018","WWE Championship","Styles retains — their best of multiple encounters at WM34","W"))
rows.append(row(w,"tv",a("stone-cold-steve-austin","Steve Austin"),"Stone Cold Podcast","2017","Podcast interview","Austin interviews Styles on the Network — best-in-world conversation"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall", "pct": 50},
    {"label": "Submission (Calf Crusher)", "pct": 20},
    {"label": "Styles Clash / Forearm", "pct": 16},
    {"label": "Countout/DQ", "pct": 14},
]
w["faq"] = [
    {"q": "When did AJ Styles debut in WWE?", "a": "AJ Styles debuted in WWE at the Royal Rumble on January 24, 2016, entering at number 3 to a massive crowd reaction — one of wrestling's great unannounced surprise appearances."},
    {"q": "Is AJ Styles the best wrestler of his generation?", "a": "Many argue AJ Styles is among the two or three most technically gifted performers in wrestling history, with a career spanning TNA, NJPW, ROH, and WWE producing an essentially matchless body of work across three decades."},
    {"q": "What are AJ Styles's finishing moves?", "a": "AJ Styles's finishing moves are the Styles Clash (a face-down piledriver variant) and the Phenomenal Forearm (a springboard forearm from the ring apron). He also uses the Calf Crusher as a submission finish."},
]
wrestlers.append(w)

# 4. KEVIN OWENS
w = {}
w["slug"] = "kevin-owens"
w["name"] = "Kevin Owens"
w["subtitle"] = "KO · Prize Fighter · WWE Universal Champion"
w["born"] = "May 7, 1984"
w["from"] = "Marieville, Quebec, Canada"
w["height"] = "6 ft (183 cm)"
w["weight"] = "266 lb (121 kg)"
w["trained"] = "Jacques Rougeau, Kris Kaefer"
w["debut"] = "2000"
w["style"] = "Brawler technician, suplex variants, apron powerbomb specialist, masterful heel psychology"
w["aliases"] = ["Kevin Owens", "Kevin Steen", "KO", "Kevin Owens Show", "The Prize Fighter"]
w["wins"] = 78
w["losses"] = 67
w["draws"] = 3
w["wl_strip"] = ('<i></i>'*6 + '<i class="l"></i>'*4)*7 + '<i></i>'*5 + '<i class="l"></i>'*2
w["bio"] = [
    "Kevin Owens is one of professional wrestling's most naturally gifted performers and its most consistently entertaining heel. His career on the independent circuit as Kevin Steen — including a legendary Ring of Honor run that produced some of that promotion's most compelling character work — established him as a performer capable of carrying a show on microphone alone.",
    "His NXT debut in 2015 — attacking John Cena during a title celebration without any provocation, sending him shoulder-first into the announce desk — was one of the great debut statements in recent memory. The crowd immediately understood that Owens was different: a heel who didn't need supernatural backup or gimmick assists, just attitude and a willingness to be the biggest jerk in the room.",
    "His Universal Championship reign (2016–2017) produced consistently entertaining television, particularly the running comedy-drama of his best-friendship with Chris Jericho — a program that unexpectedly became one of WWE's most beloved character relationships. The Festival of Friendship episode of Raw is studied as a masterclass in long-form character work.",
    "As Stone Cold Steve Austin's opponent at WrestleMania 38 in a No DQ Texas Stunner match, Owens was trusted with the responsibility of luring Austin back for one more match. The result was one of WrestleMania 38's genuine highlights — a crowd that was fully invested, a brawl that felt consequential, and Austin delivering a Stunner that the audience had been waiting years to see.",
]
w["finishers"] = [
    {"name": "Pop-Up Powerbomb", "desc": "Catches a running opponent into a devastating sitout powerbomb — the setup's theatrics give it exceptional visual impact."},
    {"name": "Stunner", "desc": "Steve Austin's move, adopted by Owens and made his own — Owens's version is faster and more reckless, fitting his character."},
    {"name": "Package Piledriver (as Kevin Steen)", "desc": "His original finisher on the independents — one of wrestling's most protected moves during his ROH era."},
]
w["championships"] = [
    cr("WWE Universal Championship", "1× (2016–2017)"),
    cr("WWE Championship", "1× (2021 — brief; won from Big E)"),
    cr("NXT Championship", "1×"),
    cr("WWE United States Championship", "2×"),
    cr("WWE Intercontinental Championship", "3×"),
    cr("ROH World Championship", "1× (as Kevin Steen)"),
]
w["personas"] = [
    {"name": "Kevin Steen", "era": "Indie / ROH 2000–2014", "desc": "The Kevin Steen Show — magnetic independent heel; ROH World Champion; one of wrestling's funniest and most infuriating performers."},
    {"name": "Kevin Owens (NXT/main roster)", "era": "WWE 2015–present", "desc": "The Prize Fighter — immediately credible on the main roster; Universal Champion; best-friends-with-Jericho."},
]
w["timeline"] = [
    {"year": "2000", "title": "Pro debut in Quebec", "desc": "Begins wrestling locally in Quebec after obsessive training — Steve Austin-influenced character from the start."},
    {"year": "2010–14", "title": "ROH era as Kevin Steen", "desc": "Peak independent run — ROH World Champion; feuds with El Generico (Sami Zayn) that are among ROH's finest."},
    {"year": "2014", "title": "WWE signing & NXT", "desc": "Signs with WWE and immediately shines in NXT — NXT title win establishes him as a ready main-roster performer."},
    {"year": "2015", "title": "NXT debut and John Cena attack", "desc": "Arrives on the main roster by attacking John Cena unprovoked — one of the decade's great debut statements."},
    {"year": "2016", "title": "Universal Champion", "desc": "Wins the inaugural WWE Universal Championship — begins the KO Show era."},
    {"year": "2016–17", "title": "Festival of Friendship with Jericho", "desc": "The Owens-Jericho best-friend storyline becomes WWE's most beloved character relationship in years."},
    {"year": "2022", "title": "WrestleMania 38 vs. Steve Austin", "desc": "Challenges Steve Austin out of retirement — their No DQ match is WM38's genuine highlight."},
]
w["sig_matches"] = [
    {"rating": "★★★★½", "title": "Kevin Owens vs. John Cena", "subtitle": "NXT Takeover: Unstoppable — May 20, 2015", "desc": "Owens's main roster coming-out match — before the debut, this NXT bout showed Owens could not only hang with Cena but had something Cena had never seen. Cena loses to Owens in a match neither man expected to be 4.5-star quality."},
    {"rating": "★★★★", "title": "Kevin Owens vs. Steve Austin", "subtitle": "WrestleMania 38 — Apr 2, 2022", "desc": "No DQ Texas Stunner match — Austin lured back for the first time since WM19. The crowd erupts for every Austin spot; Owens plays the heel perfectly; Austin takes a beer bath and ends with Stunners that bring the house down."},
    {"rating": "★★★★", "title": "Kevin Owens vs. Sami Zayn", "subtitle": "Series — WWE/NXT 2015–2023", "desc": "The longest-running feud in modern wrestling — from their ROH/indie days through NXT and multiple WWE programmes, including their 2023 Elimination Chamber tag match. The best sustained rivalry of the decade."},
]
rows = []
rows.append(row(w,"ppv",a("john-cena","John Cena"),"NXT Takeover: Unstoppable","May 20, 2015","NXT Championship (open challenge)","Owens wins — coming-out performance that makes him an immediate main-roster call"))
rows.append(row(w,"ppv",a("john-cena","John Cena"),"Elimination Chamber","May 31, 2015","US Championship open challenge","Cena wins — their rematch; Owens's best showing on the main roster","L"))
rows.append(row(w,"ppv",a("seth-rollins","Seth Rollins"),"WWE Universal Championship","2016","Universal Championship","Owens wins Rollins's vacated title — his biggest prize"))
rows.append(row(w,"ppv","Chris Jericho","WrestleMania 33","Apr 2, 2017","United States Championship — Friendship is over","Jericho wins — Festival of Friendship payoff; Owens vs. Jericho is all-time","L"))
rows.append(row(w,"ppv",a("roman-reigns","Roman Reigns"),"Hell in a Cell","Oct 25, 2020","Universal Championship — I Quit","Reigns wins — one of 2020's best WWE matches","L"))
rows.append(row(w,"ppv",a("stone-cold-steve-austin","Steve Austin"),"WrestleMania 38","Apr 2, 2022","No DQ Texas Stunner match","Austin wins — one of WM38's best moments","L"))
rows.append(row(w,"ppv","Sami Zayn","WrestleMania 39","Apr 1, 2023","Undisputed Tag Championship — with Zayn vs. Usos","KO and Zayn win — the Bloodline arc payoff for both men"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall", "pct": 48},
    {"label": "Pop-Up Powerbomb", "pct": 22},
    {"label": "Countout/DQ", "pct": 16},
    {"label": "Submission", "pct": 8},
    {"label": "Special stipulation", "pct": 6},
]
w["faq"] = [
    {"q": "Did Kevin Owens wrestle Steve Austin at WrestleMania?", "a": "Yes — Kevin Owens faced Steve Austin in a No DQ Texas Stunner match at WrestleMania 38 (April 2, 2022), luring Austin out of retirement for his first match since WrestleMania XIX (2003). Austin won."},
    {"q": "What is the Festival of Friendship?", "a": "The Festival of Friendship was a January 2017 Raw segment in which Kevin Owens threw an elaborate party for his best friend Chris Jericho, only for Jericho to turn on him and end the friendship — one of the decade's great character storytelling moments."},
]
wrestlers.append(w)

# 5. SAVIO VEGA
w = {}
w["slug"] = "savio-vega"
w["name"] = "Savio Vega"
w["subtitle"] = "The Puerto Rican Powerhouse · Strap Match Specialist"
w["born"] = "April 14, 1964"
w["from"] = "Vega Baja, Puerto Rico"
w["height"] = "6 ft 1 in (185 cm)"
w["weight"] = "260 lb (118 kg)"
w["trained"] = "Victor Jovica, Carlos Colon"
w["debut"] = "1985"
w["style"] = "Caribbean brawler, strap match specialist, durable heavyweight"
w["aliases"] = ["Savio Vega", "Juan Rivera", "Kwang", "TNT (Puerto Rico)"]
w["wins"] = 54
w["losses"] = 47
w["draws"] = 6
w["wl_strip"] = ('<i></i>'*6 + '<i class="l"></i>'*4)*5 + '<i></i>'*4 + '<i class="l"></i>'*4
w["bio"] = [
    "Savio Vega is one of the most historically significant performers in the story of Stone Cold Steve Austin — though the significance flows not from what Savio won, but from what happened when Austin lost. Their strap match at In Your House: Beware of Dog in 1996 is the match that ended the Ted DiBiase manager relationship and, more importantly, led directly to Austin's King of the Ring 1996 victory.",
    "Vega was a mainstay of WWF's mid-card through 1995–1997, a reliable heavyweight who could work a physical match with any opponent and generate crowd heat with Puerto Rican pride. He had chemistry with Austin from their earliest encounters, and their extended programme gave Austin the platform to develop the Rattlesnake character that would change wrestling history.",
    "After WWF, Vega founded the Puerto Rican promotion WWC and has remained active in Caribbean wrestling, where he is regarded as a legend. His contributions to launching Austin's babyface turn — by being the opponent who pushed Austin into the King of the Ring tournament — are an underappreciated footnote in wrestling history.",
]
w["finishers"] = [
    {"name": "Spinning Heel Kick", "desc": "A quick spinning heel kick used as both a setup and finish — effective mid-card offense with surprising height."},
    {"name": "Strap Match expertise", "desc": "Vega was one of WWF's most experienced strap match workers — capable of structuring the touch-all-four-corners drama that made the stipulation work."},
]
w["championships"] = [
    cr("WWC Universal Championship", "Multiple reigns (Puerto Rico's top title)"),
    cr("WWC Caribbean Championship", "Multiple reigns"),
    cr("WWF Tag Team Championship", "1× (with Razor Ramon, the Bad News Bears)"),
]
w["personas"] = [
    {"name": "TNT / Juan Rivera", "era": "Puerto Rico / Caribbean 1985–1994", "desc": "His territory career — a fixture of Caribbean wrestling before the WWF call."},
    {"name": "Kwang", "era": "WWF 1993–1995", "desc": "A masked ninja gimmick — not the ideal character for Vega's skillset, but it got him on the main roster."},
    {"name": "Savio Vega", "era": "WWF 1995–1998", "desc": "Unmasked and presented as himself — the Puerto Rican crowd connection was genuine and effective."},
]
w["timeline"] = [
    {"year": "1985", "title": "Pro debut in Puerto Rico", "desc": "Begins wrestling in the Caribbean, trained by WWC legends Carlos Colon and Victor Jovica."},
    {"year": "1993", "title": "WWF debut as Kwang", "desc": "Arrives in WWF under a masked ninja gimmick — the character doesn't capture his natural charisma."},
    {"year": "1995", "title": "Unmasked as Savio Vega", "desc": "Presented as himself — the Puerto Rican pride babyface connects better with the WWF audience."},
    {"year": "1995–96", "title": "Feud with Steve Austin", "desc": "Extended programme with Austin through 1995–96 — the strap match at Beware of Dog leads directly to Austin's KOTR 1996 opportunity."},
    {"year": "1996", "title": "KOTR strap match — Austin loses DiBiase", "desc": "Their strap match causes Austin to lose Ted DiBiase as his manager — the moment that fully liberates the Rattlesnake character."},
    {"year": "1996–97", "title": "Los Boricuas leader", "desc": "Leads the Puerto Rican heel stable Los Boricuas — a gang-warfare angle with Disciples of Apocalypse and Nation of Domination."},
    {"year": "1998–present", "title": "Return to Puerto Rico — WWC promotion", "desc": "Departs WWF and establishes himself as a promoter and star in Puerto Rican wrestling — a legendary figure in the region."},
]
w["sig_matches"] = [
    {"rating": "★★★", "title": "Savio Vega vs. Steve Austin", "subtitle": "In Your House: Beware of Dog — May 26, 1996", "desc": "Strap match — Vega wins, costing Austin his DiBiase manager alliance. The loss liberates Austin and sends him toward KOTR 1996. The most historically significant Savio Vega match."},
    {"rating": "★★½", "title": "Savio Vega vs. Steve Austin", "subtitle": "In Your House: International Incident — Jul 21, 1996", "desc": "Their rematch — Austin wins; the feud is largely concluded; Austin's KOTR promo has already changed the game. Solid mid-card brawl."},
    {"rating": "★★½", "title": "Savio Vega vs. Triple H", "subtitle": "King of the Ring 1996", "desc": "KOTR Quarter-final — HHH wins; Savio's last major tournament appearance in WWF."},
]
rows = []
rows.append(row(w,"ppv",a("stone-cold-steve-austin","Steve Austin"),"In Your House: Beware of Dog","May 26, 1996","Strap Match — Austin loses DiBiase if Savio wins","Savio wins — Austin's manager relationship ends; Rattlesnake fully unleashed"))
rows.append(row(w,"ppv","Razor Ramon","In Your House 2","Jul 23, 1995","WWF Tag Team Championship","Savio and Razor (Bad News Bears) lose tag titles","L"))
rows.append(row(w,"ppv",a("stone-cold-steve-austin","Steve Austin"),"In Your House: International Incident","Jul 21, 1996","Singles — feud continuation","Austin wins — their feud's conclusion; Austin heading toward bigger things","L"))
rows.append(row(w,"ppv",a("triple-h","Triple H"),"King of the Ring 1996","Jun 23, 1996","KOTR Quarter-final","HHH wins — Savio's last major KOTR run","L"))
rows.append(row(w,"tv","Faarooq (Ron Simmons)","Raw","1997","Gang warfare — Los Boricuas vs. Nation","Boricuas vs. Nation faction warfare — mid-card gang angle"))
rows.append(row(w,"ppv",a("stone-cold-steve-austin","Steve Austin"),"Raw 1995","First televised encounter","Jan 1996","Early Austin-Savio match — Austin still DiBiase's Ringmaster","W"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall", "pct": 48},
    {"label": "Strap match (4 corners)", "pct": 20},
    {"label": "Submission", "pct": 12},
    {"label": "Countout/DQ", "pct": 20},
]
w["faq"] = [
    {"q": "What is Savio Vega's connection to Stone Cold Steve Austin?", "a": "Savio Vega and Steve Austin had an extended mid-1990s feud that included a pivotal strap match at In Your House: Beware of Dog in 1996, where Vega's win cost Austin his manager Ted DiBiase. This freed Austin to develop the Rattlesnake character that led to his King of the Ring 1996 victory and the Austin 3:16 promo."},
    {"q": "Did Savio Vega win any WWF titles?", "a": "Savio Vega won the WWF Tag Team Championship once with Razor Ramon. He was primarily a mid-card performer in WWF but held multiple championship reigns in Puerto Rican wrestling (WWC)."},
]
wrestlers.append(w)

# ---------------------------------------------------------------------------
for w in wrestlers:
    html = build_page(w)
    path = os.path.join(BASE, w["slug"], "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)
    print(f"✅ {w['slug']} — {html.count(chr(10))} lines")

print("\nBatch 4b complete.")
