#!/usr/bin/env python3
"""Batch 4a: Roman Reigns, CM Punk, Eddie Guerrero, Brock Lesnar, Randy Orton"""
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

    # Conditional blocks — no \n inside f-string {…} (Python 3.11)
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

# 1. ROMAN REIGNS
w = {}
w["slug"] = "roman-reigns"
w["name"] = "Roman Reigns"
w["subtitle"] = "The Tribal Chief · 4× World Champion"
w["born"] = "May 25, 1985"
w["from"] = "Pensacola, Florida"
w["height"] = "6 ft 3 in (191 cm)"
w["weight"] = "265 lb (120 kg)"
w["trained"] = "Florida Championship Wrestling (WWE developmental)"
w["debut"] = "2010"
w["style"] = "Power, technical powerhouse, submission sequences, methodical storytelling"
w["aliases"] = ["Roman Reigns", "Leati Joseph Anoa'i", "The Big Dog", "The Tribal Chief", "The Head of the Table"]
w["wins"] = 76
w["losses"] = 44
w["draws"] = 3
w["wl_strip"] = ('<i></i>'*8 + '<i class="l"></i>'*2)*7 + '<i></i>'*6
w["bio"] = [
    "Roman Reigns's career trajectory is one of the most dramatic in wrestling history: a five-year period of being one of the most-rejected babyfaces in WWE history, followed by a character reinvention in 2020 that produced the greatest sustained heel run of the modern era.",
    "After a decade of forced character development that the audience actively rejected (reaching a nadir at WrestleMania 32 where a Texas crowd booed him out of the building despite winning the title), Reigns returned from a COVID hiatus in August 2020 as a fully heel Tribal Chief. The character drew immediately and has since produced arguably the best sustained main-event run in WWE history.",
    "As the Tribal Chief, Reigns's Undisputed WWE Universal Championship reign reached 1,316 days — the longest world title reign in WWE/WWF history. His work with Paul Heyman as Special Counsel, the Bloodline storyline, the Sami Zayn arc, and the WrestleMania 39 double championship defense against Cody Rhodes produced some of the best wrestling television of the decade.",
    "Reigns's athletic background (NFL draftee, Jacksonville Jaguars 2006 before injury) and family legacy (third-generation wrestler from the Anoa'i family) give him a pedigree that matches his physical presence. His ring work under the Tribal Chief character — deliberate, methodical, psychologically driven — is far superior to the smile-and-spear era audiences rejected.",
]
w["finishers"] = [
    {"name": "Spear", "desc": "Running spear — impactful and crowd-pleasing; used as a setup or finish depending on the match."},
    {"name": "Superman Punch", "desc": "Jumping punch with theatrics — more of a signature spot than a finisher, but consistently over."},
    {"name": "Guillotine Choke", "desc": "Added under the Tribal Chief character — a submission that made him appear more dangerous and methodical."},
]
w["championships"] = [
    cr("WWE Universal Championship", "3× (2016, 2020–2023 — 1,316-day reign)"),
    cr("WWE Championship", "2× (2015, 2022 — unified Undisputed title)"),
    cr("Intercontinental Championship", "1×"),
    cr("United States Championship", "1×"),
    cr("WWE Tag Team Championship", "1× (with Seth Rollins)"),
]
w["personas"] = [
    {"name": "The Shield member", "era": "WWE 2012–2014", "desc": "Debuted as the silent enforcer of The Shield — working as a unit with Rollins and Ambrose before the faction dissolved."},
    {"name": "The Big Dog", "era": "WWE 2014–2020", "desc": "The poorly received babyface era — repeatedly pushed as the face of WWE despite audience rejection."},
    {"name": "The Tribal Chief", "era": "WWE 2020–present", "desc": "The character reinvention — heel Reigns as Head of the Table is the best sustained character work in WWE in two decades."},
]
w["timeline"] = [
    {"year": "2010", "title": "WWE debut (FCW)", "desc": "Begins in WWE's developmental system; Samoan heritage and physical frame immediately set him apart."},
    {"year": "2012", "title": "The Shield debut at Survivor Series", "desc": "Debuts alongside Seth Rollins and Dean Ambrose — interference that signals the Shield's arrival."},
    {"year": "2014", "title": "Shield disbands — singles push", "desc": "The Shield splits in June 2014; Reigns pushed immediately to the top of the card."},
    {"year": "2015", "title": "First WWE title reign", "desc": "Wins his first WWE Championship — the crowd reception ranges from tepid to hostile."},
    {"year": "2016", "title": "WrestleMania 32 — stadium boo", "desc": "Wins the WWE title in front of 101,763 (Texas Stadium record) — gets booed throughout by a wrestling crowd that found the push manufactured."},
    {"year": "2018", "title": "Leukemia announcement", "desc": "Relinquishes the Universal title and announces a leukemia diagnosis — the audience response immediately changes; genuine outpouring of support."},
    {"year": "2020", "title": "The Tribal Chief — character reinvention", "desc": "Returns after COVID hiatus as a heel Tribal Chief — the character immediately clicks. Paul Heyman appointed Special Counsel."},
    {"year": "2020–2023", "title": "1,316-day title reign", "desc": "Longest WWE world title reign in history — encompasses the entire Bloodline storyline, Sami Zayn arc, and WrestleMania 39 main event."},
    {"year": "2024", "title": "Reign ends vs. Cody Rhodes", "desc": "Cody Rhodes defeats Reigns at WrestleMania XL to end the reign and 'finish the story.'"},
]
w["sig_matches"] = [
    {"rating": "★★★★½", "title": "Roman Reigns vs. Sami Zayn", "subtitle": "Elimination Chamber — Feb 18, 2023", "desc": "The Bloodline arc's emotional peak — Zayn turns on Reigns after months of character development. The crowd is on their feet for the entire finishing sequence. One of the best WWE TV matches of the decade."},
    {"rating": "★★★★½", "title": "Roman Reigns vs. Cody Rhodes", "subtitle": "WrestleMania XL Night 2 — Apr 7, 2024", "desc": "The finish-the-story payoff — Rhodes wins the undisputed title in a Philadelphia crowd that was heavily invested. One of WM's great recent emotional moments."},
    {"rating": "★★★★", "title": "Roman Reigns vs. Daniel Bryan", "subtitle": "WrestleMania 30 — Apr 6, 2014", "desc": "Triple Threat (with Batista) — Bryan wins in one of WM's most-deserved title changes. Reigns is the heel muscle; the crowd loved it."},
]
rows = []
rows.append(row(w,"ppv","Daniel Bryan","WrestleMania XXX","Apr 6, 2014","WWE Championship — Triple Threat (with Batista)","Bryan wins — Reigns plays the heel powerhouse perfectly","L"))
rows.append(row(w,"ppv","Seth Rollins","Money in the Bank","Jun 14, 2015","WWE Championship","Rollins retains — Reigns's best singles match to this point","L"))
rows.append(row(w,"ppv",a("triple-h","Triple H"),"WrestleMania 32","Apr 3, 2016","WWE Championship","Reigns wins in front of 101,763 — massively booed despite win"))
rows.append(row(w,"ppv","Brock Lesnar","WrestleMania 34","Apr 8, 2018","WWE Universal Championship","Lesnar retains — Reigns's best babyface performance","L"))
rows.append(row(w,"ppv","The Fiend Bray Wyatt","Payback","Aug 30, 2020","Universal Championship — First Tribal Chief match","Reigns wins — debut of the Tribal Chief character; immediate heat"))
rows.append(row(w,"ppv","Kevin Owens","Survivor Series","Nov 22, 2020","Universal Championship — I Quit match","Reigns wins — KO's best match in years; Tribal Chief arc building"))
rows.append(row(w,"ppv","Sami Zayn","Elimination Chamber","Feb 18, 2023","Universal Championship","Reigns wins — Zayn turns on him after months of Bloodline development"))
rows.append(row(w,"ppv","Cody Rhodes","WrestleMania XL Night 2","Apr 7, 2024","Undisputed WWE Universal Championship","Rhodes wins — 1,316-day reign ends; finish-the-story payoff","L"))
rows.append(row(w,"tv",a("john-cena","John Cena"),"No Mercy","Oct 22, 2017","Singles — torch pass","Reigns wins — Cena's best loss in years; torch-passing moment"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall", "pct": 55},
    {"label": "Submission (Guillotine)", "pct": 18},
    {"label": "Countout/DQ", "pct": 14},
    {"label": "Special stipulation", "pct": 13},
]
w["faq"] = [
    {"q": "How long was Roman Reigns's WWE title reign?", "a": "Roman Reigns held the Undisputed WWE Universal Championship for 1,316 days — from August 2020 to April 2024 — the longest world title reign in WWE/WWF history."},
    {"q": "Who defeated Roman Reigns for the title?", "a": "Cody Rhodes defeated Roman Reigns at WrestleMania XL Night 2 on April 7, 2024 in Philadelphia, ending the 1,316-day reign."},
    {"q": "What is the Bloodline storyline?", "a": "The Bloodline is WWE's most acclaimed long-form storyline of the 2020s, centered on Roman Reigns as the Tribal Chief and Head of the Table commanding his Samoan family members (The Usos, Solo Sikoa) with Paul Heyman as Special Counsel."},
]
wrestlers.append(w)

# 2. CM PUNK
w = {}
w["slug"] = "cm-punk"
w["name"] = "CM Punk"
w["subtitle"] = "The Best in the World · Twice WWE Champion"
w["born"] = "October 26, 1978"
w["from"] = "Chicago, Illinois"
w["height"] = "6 ft 2 in (188 cm)"
w["weight"] = "218 lb (99 kg)"
w["trained"] = "Ace Steel, Dory Funk Jr., Ring of Honor school"
w["debut"] = "1999"
w["style"] = "Technical, submission emphasis, crowd psychology, storytelling-first"
w["aliases"] = ["CM Punk", "Phillip Jack Brooks", "The Second City Saint", "The Best in the World", "The Voice of the Voiceless"]
w["wins"] = 82
w["losses"] = 57
w["draws"] = 3
w["wl_strip"] = ('<i></i>'*7 + '<i class="l"></i>'*3)*7 + '<i></i>'*5 + '<i class="l"></i>'*2
w["bio"] = [
    "CM Punk is the most important anti-establishment performer in professional wrestling since Steve Austin. His 2011 'Pipe Bomb' promo — delivered while sitting cross-legged on the stage, mic in hand, with a smirk that dared WWE management to cut his mic — remains the most compelling promo in WWE since the Attitude Era.",
    "Punk's rise is a story of independent wrestling credibility meeting mainstream opportunity. After years on the Ring of Honor and independent circuit developing one of the most sophisticated in-ring games of his generation, Punk arrived in WWE in 2006 and spent five years being alternately elevated and misused before the 2011 moment that changed everything.",
    "His 434-day WWE Championship reign (2011–2013) — the longest of the modern era — produced excellent matches against John Cena, Daniel Bryan, Chris Jericho, Dolph Ziggler, Ryback, and The Undertaker. The Undertaker match at WrestleMania 29 remains one of the Streak's three or four best matches.",
    "Punk's departure from WWE in January 2014, subsequent legal disputes, and return to wrestling via AEW (2021) and later WWE (2023) added chapters to a career story that seemed to resist easy narrative. His 2024 WWE return as a heel — and subsequent injury — demonstrates that the business still orbits around his magnetic presence when he is healthy.",
]
w["finishers"] = [
    {"name": "GTS (Go To Sleep)", "desc": "Fireman's carry knee lift to the face — one of the decade's most distinctive finishers; the setup and delivery were both perfectly timed."},
    {"name": "Anaconda Vise", "desc": "Crossface-style arm trap submission — used throughout his career as both a finish and a second-rope spot."},
]
w["championships"] = [
    cr("WWE Championship", "2× (2011–2013 — 434 days combined)"),
    cr("World Heavyweight Championship", "2× (2008–2009)"),
    cr("ECW Championship", "1×"),
    cr("Intercontinental Championship", "1×"),
    cr("ROH World Championship", "1× (2005–2007 — record reign at the time)"),
    cr("WWE Tag Team Championship", "1× (with Kofi Kingston)"),
]
w["personas"] = [
    {"name": "The Second City Saint", "era": "ROH / indie 1999–2005", "desc": "The Chicago antihero — straight-edge, countercultural, technically extraordinary on the indie circuit."},
    {"name": "ECW/WWE CM Punk", "era": "WWE 2006–2010", "desc": "The misdirected years — creative never fully committed, but multiple world title reigns showed the company's acknowledgement of his value."},
    {"name": "The Voice of the Voiceless", "era": "WWE 2011–2014", "desc": "The Pipe Bomb era — Punk at his peak as the audience's representative against authority."},
    {"name": "AEW / Return CM Punk", "era": "AEW 2021–2023 / WWE 2023–present", "desc": "The return chapter — polarizing backstage reputation, extraordinary in-ring output when healthy."},
]
w["timeline"] = [
    {"year": "1999", "title": "Pro debut", "desc": "Begins wrestling in the Chicago independent scene — immediately distinguishable by promo ability and ring intelligence."},
    {"year": "2005", "title": "ROH World Champion", "desc": "Wins the Ring of Honor world title in what becomes the longest ROH world title reign in history to that point."},
    {"year": "2006", "title": "WWE debut", "desc": "Arrives in ECW (WWE brand) — the crowd response is immediate and positive."},
    {"year": "2008", "title": "First World Heavyweight Championship", "desc": "Cashes in his Money in the Bank on an injured Edge — his first world title and the beginning of a complicated relationship with main-event booking."},
    {"year": "2011", "title": "The Pipe Bomb", "desc": "June 27, 2011 — delivers the most talked-about WWE promo since Austin at WM13; sits cross-legged on the stage and demolishes WWE management while his contract expires."},
    {"year": "2011", "title": "Money in the Bank — WWE Champion", "desc": "Defeats John Cena in Chicago, walks out with the title and leaves WWE — the beginning of his 434-day reign that revitalized the championship's prestige."},
    {"year": "2013", "title": "The Shield — longest WM streak match", "desc": "His WrestleMania 29 match with The Undertaker (including the Paul Bearer tribute angle) is one of the Streak's finest."},
    {"year": "2014", "title": "WWE departure", "desc": "Walks out of WWE in January — a departure that roiled the industry and led to years of legal disputes."},
    {"year": "2021", "title": "AEW debut", "desc": "Returns to professional wrestling in AEW to a rapturous Chicago crowd — one of the great comeback moments in wrestling history."},
    {"year": "2023", "title": "WWE return", "desc": "Returns to WWE at Survivor Series 2023 — the prodigal son narrative closes."},
]
w["sig_matches"] = [
    {"rating": "★★★★★", "title": "CM Punk vs. John Cena", "subtitle": "Money in the Bank — Jun 27, 2011", "desc": "The Pipe Bomb made the match; the match made the event; the event redefined what WWE could be in the modern era. Punk wins the WWE title in Chicago while his contract expires — and walks out with the belt. A perfect professional wrestling story."},
    {"rating": "★★★★½", "title": "CM Punk vs. The Undertaker", "subtitle": "WrestleMania 29 — Apr 7, 2013", "desc": "The Streak's second-best match — Punk works the Paul Bearer tribute angle brilliantly and produces a 22-minute masterclass with Undertaker. The near-falls are genuinely convincing."},
    {"rating": "★★★★", "title": "CM Punk vs. Chris Jericho", "subtitle": "WrestleMania XXVIII — Apr 1, 2012", "desc": "Best vs. Best in the World — Jericho's best match in years; Punk retains the WWE title. An underrated WM match that rewards repeat viewing."},
]
rows = []
rows.append(row(w,"ppv","Edge","SummerSlam — MITB cash-in","Jul 25, 2008","World Heavyweight Championship — MITB cash-in","Punk wins his first world title cashing in on injured Edge"))
rows.append(row(w,"ppv",a("john-cena","John Cena"),"Money in the Bank","Jun 27, 2011","WWE Championship — last night on contract","Punk wins — 5-star match; leaves WWE with the title"))
rows.append(row(w,"ppv",a("chris-jericho","Chris Jericho"),"WrestleMania XXVIII","Apr 1, 2012","WWE Championship","Punk retains in underrated WM classic"))
rows.append(row(w,"ppv","The Undertaker","WrestleMania 29","Apr 7, 2013","The Streak — 20-0 vs. 21-0","Undertaker wins at 21-0 — Punk's best WM performance","L"))
rows.append(row(w,"ppv","Brock Lesnar","SummerSlam","Aug 18, 2013","Singles — No Holds Barred","Lesnar wins brutally — Heyman turns on Punk","L"))
rows.append(row(w,"ppv","Samoa Joe","AEW Double or Nothing","May 29, 2022","Singles","Punk wins — return match and a statement win"))
rows.append(row(w,"ppv",a("roman-reigns","Roman Reigns"),"WWE Royal Rumble","Jan 27, 2024","Royal Rumble match involvement","Reigns eliminates Punk — Punk vs. Reigns feud begins"))
rows.append(row(w,"tv",a("stone-cold-steve-austin","Steve Austin"),"WWE Raw — Punk era","2011–2012","Promo interaction / GM angle","Austin-Punk era overlap; Austin as RAW GM during Punk's title reign"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall", "pct": 50},
    {"label": "Submission (Anaconda Vise)", "pct": 22},
    {"label": "Countout/DQ", "pct": 15},
    {"label": "Special stipulation", "pct": 13},
]
w["faq"] = [
    {"q": "What is the Pipe Bomb promo?", "a": "CM Punk's June 27, 2011 promo before Money in the Bank — delivered sitting cross-legged on the stage, microphone in hand — in which he attacked WWE management, John Cena, and the structure of the company. Widely considered the best WWE promo since Stone Cold Steve Austin's WrestleMania 13 promo."},
    {"q": "How long was CM Punk's WWE Championship reign?", "a": "CM Punk's combined WWE Championship reign in 2011-2013 lasted 434 days — the longest world title reign in WWE in the modern era."},
    {"q": "Why did CM Punk leave WWE in 2014?", "a": "CM Punk walked out of WWE in January 2014, citing creative frustrations, physical exhaustion, and feeling undervalued. He later detailed his reasons in a podcast interview with Colt Cabana that became one of wrestling's most-discussed media moments."},
]
wrestlers.append(w)

# 3. EDDIE GUERRERO
w = {}
w["slug"] = "eddie-guerrero"
w["name"] = "Eddie Guerrero"
w["subtitle"] = "Latino Heat · WWE Champion · Hall of Famer"
w["born"] = "October 9, 1967"
w["from"] = "El Paso, Texas"
w["height"] = "5 ft 8 in (173 cm)"
w["weight"] = "220 lb (100 kg)"
w["trained"] = "Black Cat (WCW), Rey Mysterio Sr., Art Barr"
w["debut"] = "1987"
w["notice_html"] = """<div class="notice notice--memorial" role="note">
  <strong>Eddie Guerrero (October 9, 1967 – November 13, 2005).</strong>
  Eddie Guerrero passed away on November 13, 2005, in Minneapolis, Minnesota, from acute heart failure attributed to atherosclerotic cardiovascular disease. He is remembered as one of the greatest professional wrestlers of all time.
</div>"""
w["aliases"] = ["Eddie Guerrero", "Latino Heat", "El Calor Latino", "Eduardo Gory Guerrero Llanes"]
w["wins"] = 78
w["losses"] = 62
w["draws"] = 5
w["wl_strip"] = ('<i></i>'*7 + '<i class="l"></i>'*3)*7 + '<i></i>'*7
w["bio"] = [
    "Eddie Guerrero is one of professional wrestling's most complete performers in history — and its most heartbreaking story. Born into the legendary Guerrero wrestling dynasty (father Gory, brothers Chavo Sr., Mando, and Hector), Eddie combined natural athleticism, extraordinary ring intelligence, lucha libre technique, and an unmatched ability to generate crowd response in every phase of a match.",
    "His peak came in three phases: the WCW/ECW cruiserweight era of the 1990s (stunning matches with Rey Mysterio, Dean Malenko, and Chris Jericho), a battle with substance abuse and near-career-ending personal struggles in the early 2000s, and finally a triumphant WWE run that culminated in a WWE Championship win over Brock Lesnar at No Way Out 2004 that brought tears to everyone who had followed the journey.",
    "The crowd response to Eddie's championship win is one of wrestling's most genuinely emotional moments: thousands of fans who knew what Eddie had been through — the addiction, the car crash, the near-death — chanting his name as he stood on the turnbuckle with the belt. No story of manufactured triumph touches it.",
    "His death at 38 in November 2005 robbed the business of its most charismatic storyteller. His friendship with Rey Mysterio — and Mysterio's subsequent 2006 Royal Rumble-to-WrestleMania championship run dedicated to Eddie's memory — is the most emotionally complete tribute story professional wrestling has produced.",
]
w["finishers"] = [
    {"name": "Frog Splash", "desc": "Eddie's aerial signature — a frog splash from the top rope with exceptional body control that made it look like it hurt the sender as much as the receiver."},
    {"name": "Three Amigos (Rolling German Suplexes)", "desc": "Three rolling German suplexes before the Frog Splash — the crowd counted along every single time and the crowd response never diminished."},
    {"name": "Lasso from El Paso", "desc": "Texas cloverleaf variant submission — an alternative finish used in technical matches."},
]
w["championships"] = [
    cr("WWE Championship", "1× (Feb 15, 2004 — Apr 22, 2004)"),
    cr("WCW United States Championship", "2×"),
    cr("WCW Cruiserweight Championship", "2×"),
    cr("ECW Television Championship", "1×"),
    cr("WWF Intercontinental Championship", "2×"),
    cr("WWE United States Championship", "1×"),
    cr("WWE Tag Team Championship", "2× (with Rey Mysterio and others)"),
    cr("WWF/WWE Tag Team Championship", "4×"),
]
w["personas"] = [
    {"name": "WCW Cruiserweight Eddie", "era": "WCW 1995–2000", "desc": "The technically extraordinary era — matches with Mysterio, Malenko, and Jericho that define the WCW cruiserweight division."},
    {"name": "Latino Heat", "era": "WWE 2000–2005", "desc": "The lie-cheat-steal character — the charismatic heel/tweener who could work any crowd and make them love hating him."},
    {"name": "WWE Champion Eddie", "era": "2004", "desc": "The culmination — babyface champion whose title win was one of the decade's most emotionally resonant moments."},
]
w["timeline"] = [
    {"year": "1987", "title": "Pro debut", "desc": "Begins wrestling at age 19 in Mexico, following four generations of Guerrero family tradition."},
    {"year": "1995", "title": "WCW debut", "desc": "Arrives in WCW to work the cruiserweight division — immediately one of the best wrestlers in America."},
    {"year": "1997", "title": "Guerrero vs. Mysterio — Halloween Havoc", "desc": "Produces what many consider the finest cruiserweight match in WCW history — a 5-star performance."},
    {"year": "2001", "title": "Car crash and rock bottom", "desc": "A serious car crash and ongoing personal struggles — the darkest period of Eddie's life. WWE releases him."},
    {"year": "2002", "title": "Return and redemption", "desc": "Returns to WWE clean and with renewed purpose — the crowd response reflects their awareness of the journey."},
    {"year": "2004", "title": "WWE Champion", "desc": "Defeats Brock Lesnar at No Way Out — the tears in the crowd are real. One of wrestling's most emotional championship moments."},
    {"year": "2005", "title": "Feud with Rey Mysterio — WM22 setup", "desc": "Works a programme with Mysterio that planted seeds for the Eddie tribute storyline that continues after his death."},
    {"year": "2005", "title": "Death", "desc": "Eddie Guerrero passes away on November 13, 2005, from acute heart failure. He was 38."},
    {"year": "2006", "title": "WrestleMania 22 — Mysterio tribute", "desc": "Rey Mysterio dedicates his Royal Rumble win and WM22 title victory to Eddie's memory — the most emotionally resonant tribute storyline wrestling has produced."},
    {"year": "2006", "title": "WWE Hall of Fame (posthumous)", "desc": "Inducted posthumously into the WWE Hall of Fame — Vickie Guerrero and their daughters accept on his behalf."},
]
w["sig_matches"] = [
    {"rating": "★★★★★", "title": "Eddie Guerrero vs. Rey Mysterio", "subtitle": "WCW Halloween Havoc — Oct 26, 1997", "desc": "The best cruiserweight match in WCW history — 14 minutes of flawless lucha-meets-technical wrestling. The hurricanrana reversal and the structure are studied in wrestling schools."},
    {"rating": "★★★★½", "title": "Eddie Guerrero vs. Brock Lesnar", "subtitle": "No Way Out — Feb 15, 2004", "desc": "WWE Championship — Eddie wins and the crowd erupts. The frog splash pin is one of wrestling's most emotional title changes, made more so by the awareness of what Eddie had survived to get here."},
    {"rating": "★★★★", "title": "Eddie Guerrero vs. Kurt Angle", "subtitle": "WrestleMania XX — Mar 14, 2004", "desc": "WWE Championship — Angle wins via rollup reversal, but the match is a technical showcase that both men are proud of. Angle and Guerrero at WM is automatic quality."},
]
rows = []
rows.append(row(w,"ppv",a("rey-mysterio","Rey Mysterio"),"WCW Halloween Havoc","Oct 26, 1997","WCW Cruiserweight Championship","Guerrero wins — 5-star cruiserweight classic; the genre's gold standard"))
rows.append(row(w,"ppv","Dean Malenko","WCW Bash at the Beach","Jul 12, 1998","WCW Cruiserweight Championship","Malenko wins — technical masterpiece with another ring general","L"))
rows.append(row(w,"ppv","Brock Lesnar","No Way Out","Feb 15, 2004","WWE Championship","Eddie wins — one of wrestling's most emotional championship moments"))
rows.append(row(w,"ppv",a("kurt-angle","Kurt Angle"),"WrestleMania XX","Mar 14, 2004","WWE Championship","Angle wins via rollup reversal — one of WM's more underrated bouts","L"))
rows.append(row(w,"ppv",a("rey-mysterio","Rey Mysterio"),"WrestleMania XXI","Apr 3, 2005","Singles","Rey wins — Eddie working as tweener; the programme plants seeds for 2006","L"))
rows.append(row(w,"ppv",a("chris-jericho","Chris Jericho"),"WCW","1997-1998","Various","Jericho-Guerrero cruiserweight programme — some of WCW's best TV matches"))
rows.append(row(w,"tv",a("stone-cold-steve-austin","Steve Austin"),"SmackDown","2003","Singles","Guerrero-Austin interaction during SmackDown's main-event era — both at their peaks"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall", "pct": 52},
    {"label": "Submission", "pct": 20},
    {"label": "Countout/DQ", "pct": 16},
    {"label": "Special stipulation", "pct": 12},
]
w["faq"] = [
    {"q": "What happened to Eddie Guerrero?", "a": "Eddie Guerrero passed away on November 13, 2005, in Minneapolis, Minnesota, from acute heart failure attributed to atherosclerotic cardiovascular disease. He was 38 years old."},
    {"q": "Did Eddie Guerrero win the WWE Championship?", "a": "Yes — Eddie Guerrero defeated Brock Lesnar for the WWE Championship at No Way Out on February 15, 2004 — one of the most emotionally resonant championship wins in wrestling history."},
    {"q": "What is Eddie Guerrero's finishing move?", "a": "Eddie Guerrero's signature finish is the Frog Splash, typically set up by his Three Amigos rolling German suplexes. The crowd would count along to all three suplexes and chant 'Eddie' throughout the sequence."},
]
wrestlers.append(w)

# 4. BROCK LESNAR
w = {}
w["slug"] = "brock-lesnar"
w["name"] = "Brock Lesnar"
w["subtitle"] = "The Beast Incarnate · 9× World Champion"
w["born"] = "July 12, 1977"
w["from"] = "Webster, South Dakota"
w["height"] = "6 ft 3 in (191 cm)"
w["weight"] = "286 lb (130 kg)"
w["trained"] = "Richard Steinborn (Minnesota), WWE developmental"
w["debut"] = "2000"
w["style"] = "Dominant power, amateur wrestling base, German suplex chain, F5 as definitive finisher"
w["aliases"] = ["Brock Lesnar", "The Beast Incarnate", "The Next Big Thing", "The Conqueror"]
w["wins"] = 72
w["losses"] = 28
w["draws"] = 3
w["wl_strip"] = ('<i></i>'*9 + '<i class="l"></i>'*1)*5 + '<i></i>'*9 + '<i class="l"></i>'*1 + '<i></i>'*12
w["bio"] = [
    "Brock Lesnar is the most physically dominant WWE performer of the modern era. An NCAA Division I national champion in amateur wrestling (at 286 pounds) and later a legitimate UFC Heavyweight Champion, Lesnar's legitimacy extends beyond kayfabe — when he hits an F5 or throws a German suplex, the weight of the move is real.",
    "His first WWE run (2002–2004) was extraordinary: arrival, immediate push, WWE Championship by SummerSlam 2002 at age 25. His departure to pursue NFL and MMA careers was a genuine business decision rather than a character arc, and his return in 2012 — headlined by a legitimate-looking fight with John Cena on the Raw after WrestleMania — confirmed that the audience had missed the real thing.",
    "The defining moment of Lesnar's second run was ending The Undertaker's WrestleMania Streak at WM30 — a decision still debated by wrestling fans but undeniably the most shocking single result in WrestleMania history. The Suplex City era that followed (2014-2019) produced matches against John Cena, Seth Rollins, Randy Orton, AJ Styles, Roman Reigns, and others that showcase Lesnar's ability to anchor a match with minimal but maximally impactful offense.",
    "Lesnar's relationship with WWE is defined by leverage: he negotiates part-time schedules, main-event spots on the most important shows, and title reigns that often serve to hold a championship until a major payoff story is ready. The business model is unusual but consistently effective from an investment standpoint.",
]
w["finishers"] = [
    {"name": "F5", "desc": "Fireman's carry into a facebreaker slam — one of wrestling's most impactful finishers; looks legitimately dangerous at his size."},
    {"name": "Kimura Lock", "desc": "A legitimate arm submission from his MMA background — used as a secondary submission finish that lends UFC credibility to his character."},
]
w["championships"] = [
    cr("WWE Championship", "5× (2002, 2004, 2014–2015, 2017–2018, 2019)"),
    cr("WWE Universal Championship", "3× (2017, 2019, 2021–2022)"),
    cr("NCAA Division I Heavyweight Championship", "1× (Minnesota, 2000)"),
    cr("UFC Heavyweight Championship", "1× (2008–2010)"),
    cr("WWE Tag Team Championship", "1× (with Kurt Angle)"),
]
w["personas"] = [
    {"name": "The Next Big Thing", "era": "WWE 2002–2004", "desc": "The invincible rookie who demolished everyone — the most successful first-year push since Goldberg."},
    {"name": "UFC/NFL interlude", "era": "2004–2012", "desc": "Genuine athletic crossover — NFL tryout (Minnesota Vikings/Carolina Panthers), UFC heavyweight champion."},
    {"name": "The Beast Incarnate / Suplex City", "era": "WWE 2012–2022", "desc": "The part-time monster whose appearances were events; the Suplex City formula was maximally effective."},
]
w["timeline"] = [
    {"year": "2000", "title": "NCAA Champion", "desc": "Wins the NCAA Division I heavyweight wrestling championship at Minnesota — a legitimate athletic credential."},
    {"year": "2002", "title": "WWE debut", "desc": "Arrives in WWE as The Next Big Thing — receives one of the most aggressive first-year pushes in company history."},
    {"year": "2002", "title": "WWE Champion at SummerSlam", "desc": "Defeats The Rock for the WWE Championship at SummerSlam — the youngest WWE champion at the time at 25."},
    {"year": "2004", "title": "WrestleMania XX vs. Goldberg", "desc": "A match neither man wanted in a hostile MSG crowd — Stone Cold stuns both; both leave WWE shortly after."},
    {"year": "2008", "title": "UFC Heavyweight Champion", "desc": "Defeats Randy Couture for the UFC Heavyweight title — the greatest mainstream athletic crossover in wrestling history."},
    {"year": "2012", "title": "WWE return — defeats Cena", "desc": "Returns to WWE at WrestleMania XXVIII; defeats John Cena on the Raw after WM in a legitimacy-establishing statement."},
    {"year": "2014", "title": "Ends The Streak", "desc": "Defeats The Undertaker at WrestleMania 30 to end the 21-0 streak — the most shocking single result in WrestleMania history. Crowd silent for minutes."},
    {"year": "2014–15", "title": "Suplex City era", "desc": "Dominant WWE title reign; defeats Cena in a 16-suplex squash at SummerSlam that resets the business's understanding of a one-sided squash."},
    {"year": "2022", "title": "Final full-time year", "desc": "Extended Universal title reign followed by WM 38 matches — Lesnar at 44 still the most physically dominant performer on the roster."},
]
w["sig_matches"] = [
    {"rating": "★★★★", "title": "Brock Lesnar vs. John Cena", "subtitle": "SummerSlam — Aug 17, 2014", "desc": "Suplex City — 16 German suplexes, one F5, and a completely one-sided 25-minute match that reset the audience's understanding of both men. Cena looks humanly fallible for the first time in years."},
    {"rating": "★★★★", "title": "Brock Lesnar vs. The Undertaker", "subtitle": "WrestleMania 30 — Apr 6, 2014", "desc": "The Streak ends at 21-0 — the crowd goes silent and the entire arena goes into a genuine state of shock. Regardless of its technical quality, this is the most impactful single result in WrestleMania history."},
    {"rating": "★★★★", "title": "Brock Lesnar vs. AJ Styles", "subtitle": "Survivor Series — Nov 19, 2017", "desc": "Brand supremacy match — Lesnar and Styles produce one of Lesnar's most complete performances; AJ almost gets the upset multiple times in a great match."},
]
rows = []
rows.append(row(w,"ppv",a("the-rock","The Rock"),"SummerSlam","Aug 25, 2002","WWE Championship","Lesnar wins at 25 — youngest WWE champion at the time"))
rows.append(row(w,"ppv",a("kurt-angle","Kurt Angle"),"WrestleMania XIX","Mar 30, 2003","WWE Championship","Lesnar wins in Angle's best-ever WM match — Lesnar lands on his head on SSP attempt"))
rows.append(row(w,"ppv",a("john-cena","John Cena"),"Extreme Rules","Apr 29, 2012","No Holds Barred","Lesnar wins on return — legitimacy re-established immediately"))
rows.append(row(w,"ppv","The Undertaker","WrestleMania 30","Apr 6, 2014","The Streak — 21-0 vs. 22-0","Lesnar wins — the Streak ends; arena goes silent; most shocking WM result ever"))
rows.append(row(w,"ppv",a("john-cena","John Cena"),"SummerSlam","Aug 17, 2014","WWE Championship","Lesnar wins via 16 suplexes — Suplex City era begins; Cena's most devastating loss"))
rows.append(row(w,"ppv",a("roman-reigns","Roman Reigns"),"WrestleMania 31","Mar 29, 2015","WWE Championship","Seth Rollins MITB cash-in — Lesnar vs. Reigns interrupted; Rollins wins","D"))
rows.append(row(w,"ppv","Goldberg","Survivor Series","Nov 20, 2016","Singles","Goldberg wins in under 90 seconds — Lesnar's most shocking loss","L"))
rows.append(row(w,"ppv",a("roman-reigns","Roman Reigns"),"WrestleMania 38 Night 2","Apr 3, 2022","Undisputed WWE Universal Championship","Reigns wins — Lesnar's last WM main event","L"))
rows.append(row(w,"tv",a("stone-cold-steve-austin","Steve Austin"),"Raw — 2012 era","2012","Promo interaction","Austin-Lesnar cross-era moment during Lesnar's return run"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall", "pct": 58},
    {"label": "Submission (Kimura)", "pct": 20},
    {"label": "Countout/DQ", "pct": 12},
    {"label": "Special stipulation", "pct": 10},
]
w["faq"] = [
    {"q": "Did Brock Lesnar really end The Undertaker's WrestleMania streak?", "a": "Yes — Brock Lesnar defeated The Undertaker at WrestleMania 30 (April 6, 2014) to end the streak at 21-0. The result is the most shocking single result in WrestleMania history."},
    {"q": "Is Brock Lesnar a legitimate athlete?", "a": "Yes — Lesnar won the NCAA Division I heavyweight wrestling championship in 2000 and later won the UFC Heavyweight Championship in 2008, defeating Randy Couture. He is one of the few wrestlers with legitimately elite combat sports credentials."},
    {"q": "How many world titles has Brock Lesnar won?", "a": "Brock Lesnar has won 9 world titles in WWE: 5 WWE Championships and 3 WWE Universal Championships, plus 1 UFC Heavyweight Championship."},
]
wrestlers.append(w)

# 5. RANDY ORTON
w = {}
w["slug"] = "randy-orton"
w["name"] = "Randy Orton"
w["subtitle"] = "The Viper · RKO OUTTA NOWHERE · 14× World Champion"
w["born"] = "April 1, 1980"
w["from"] = "St. Louis, Missouri"
w["height"] = "6 ft 5 in (196 cm)"
w["weight"] = "250 lb (113 kg)"
w["trained"] = "Bob Orton Sr., Harley Race, WWE OVW"
w["debut"] = "2000"
w["style"] = "Methodical psychology, signature spot exploitation, RKO as counter-from-anything finisher"
w["aliases"] = ["Randy Orton", "The Viper", "The Legend Killer", "The Apex Predator", "The New Face of WWE"]
w["wins"] = 89
w["losses"] = 62
w["draws"] = 5
w["wl_strip"] = ('<i></i>'*7 + '<i class="l"></i>'*3)*8 + '<i></i>'*5
w["bio"] = [
    "Randy Orton is one of the most consistent main-event performers of his generation. A third-generation wrestler (grandfather Bob Orton Sr., uncle Barry Orton, father Bob Orton Jr.) with natural gifts for the business — a silky-smooth in-ring style, legitimate intensity, and a snake-like stillness between moves — Orton became the youngest world champion in WWE history at WrestleMania XX at 24.",
    "The Legend Killer character (2004–2005) — in which Orton stalked and defeated retired legends — was perhaps the most legitimate character motivation in WWE in years: audiences believed Orton had the arrogance and talent to do what he claimed. His heel work during this period is studied as textbook character heel psychology.",
    "Orton's career has two clear peaks: the Legend Killer era (2004–2008, including his feud with Triple H and the McMahon family) and the Viper era (2009–2013, featuring outstanding matches with John Cena, Christian, and CM Punk). The RKO — an instantaneous cutter that can be applied from literally any position — became the decade's most over individual wrestling move.",
    "Consistent world title reigns across two decades (14 world titles) and a matchless hit rate for producing good-to-great matches with wrestlers of varying styles make Orton one of WWE's most reliable performers regardless of where he sits in the card.",
]
w["finishers"] = [
    {"name": "RKO", "desc": "Jumping cutter from any position — the crowd's reaction to an out-of-nowhere RKO became a meme, a gif, and a genuine piece of cultural shorthand."},
    {"name": "Punt Kick", "desc": "Running kick to a grounded opponent's head — used as a devastating match-ender during his most intense heel runs."},
]
w["championships"] = [
    cr("WWE Championship", "8× (2004–2020)"),
    cr("World Heavyweight Championship", "6× (2007–2011)"),
    cr("Intercontinental Championship", "1× (youngest at the time)"),
    cr("WWE Tag Team Championship", "2× (with Riddle as RK-Bro)"),
]
w["personas"] = [
    {"name": "The Legend Killer", "era": "WWE 2004–2006", "desc": "Third-generation superstar who stalked and defeated legends — Undertaker, Shawn Michaels, Foley, and more. Best sustained character work of his career."},
    {"name": "The Viper", "era": "WWE 2008–present", "desc": "The evolved version — predatory patience, calculated strikes, the RKO as cultural phenomenon."},
    {"name": "RK-Bro", "era": "WWE 2021–2022", "desc": "Tag team with Matt Riddle — a fish-out-of-water comedy partnership that produced surprising crowd warmth."},
]
w["timeline"] = [
    {"year": "2000", "title": "WWE developmental", "desc": "Begins in WWE developmental alongside John Cena and Batista — all three debut within months of each other."},
    {"year": "2003", "title": "WWE debut & IC title", "desc": "Arrives on Raw; wins the Intercontinental title — the youngest IC champion in history at the time."},
    {"year": "2004", "title": "Evolution member — World Heavyweight Champion", "desc": "Wins the World Heavyweight title at SummerSlam, defeating Chris Benoit — youngest world champion in WWE history at 24."},
    {"year": "2004", "title": "Legend Killer era begins", "desc": "Turns on Benoit and begins stalking legends — Foley, Undertaker, Shawn Michaels all targeted."},
    {"year": "2007", "title": "I Hear Voices era — WWE Champion", "desc": "First WWE Championship reign — begins the Viper persona with the new entrance music and coiled-snake posturing."},
    {"year": "2009", "title": "WrestleMania XXV — Legacy stable", "desc": "Triple Threat at WM25 with Triple H and Shane McMahon — the McMahon family feud at its peak."},
    {"year": "2009", "title": "First vs. Cena — extended feud", "desc": "Year-long feud with John Cena produces the best output of either man's career during this period."},
    {"year": "2013", "title": "vs. Daniel Bryan — the Orton heel run", "desc": "The Randy Orton vs. Daniel Bryan feud is the foundation of the Yes Movement — Orton as the obstructionist is excellent villain work."},
    {"year": "2021–22", "title": "RK-Bro with Riddle", "desc": "Unexpected comedic success as a tag team — Orton and Matt Riddle win multiple tag titles."},
    {"year": "2024", "title": "Return from major injury", "desc": "Returns from a spinal fusion surgery — the crowd reception demonstrates his lasting connection."},
]
w["sig_matches"] = [
    {"rating": "★★★★½", "title": "Randy Orton vs. Christian", "subtitle": "Over the Limit — May 22, 2011", "desc": "Their best singles match — Orton and Christian produce one of 2011's finest bouts in a feud that elevated both men's in-ring credibility."},
    {"rating": "★★★★", "title": "Randy Orton vs. John Cena", "subtitle": "Hell in a Cell — Oct 4, 2009", "desc": "Hell in a Cell — their most complete encounter; the structure and escalation are both excellent. Orton wins in a cell match that made both men look great."},
    {"rating": "★★★★", "title": "Randy Orton vs. CM Punk", "subtitle": "SummerSlam — Aug 14, 2011", "desc": "One of SummerSlam's most underrated matches — Punk and Orton in the most technically complete match Orton produced that year."},
]
rows = []
rows.append(row(w,"ppv","Chris Benoit","SummerSlam","Aug 15, 2004","World Heavyweight Championship","Orton wins at 24 — youngest world champion in WWE history"))
rows.append(row(w,"ppv","Shawn Michaels","WrestleMania 21","Apr 3, 2005","Singles — Legend Killer","HBK wins — their best singles match; Legend Killer era peak","L"))
rows.append(row(w,"ppv",a("triple-h","Triple H"),"WrestleMania XXV","Apr 5, 2009","WWE Championship — Triple Threat","HHH wins — Orton as the best villain in the McMahon family feud","L"))
rows.append(row(w,"ppv",a("john-cena","John Cena"),"Hell in a Cell","Oct 4, 2009","WWE Championship — Hell in a Cell","Orton wins — their best match; cell structure works for both men"))
rows.append(row(w,"ppv","Christian","Over the Limit","May 22, 2011","World Heavyweight Championship","Orton retains — their best singles match; one of 2011's best WWE bouts"))
rows.append(row(w,"ppv","CM Punk","SummerSlam","Aug 14, 2011","Singles","Orton wins — their best match; technically complete; SummerSlam underrated gem"))
rows.append(row(w,"ppv","Daniel Bryan","Night of Champions","Sep 15, 2013","WWE Championship","Orton wins with HHH involvement — the heel Orton vs. Bryan is excellent character work"))
rows.append(row(w,"ppv",a("roman-reigns","Roman Reigns"),"WrestleMania 37 Night 2","Apr 11, 2021","Tag Match with Riddle vs. Usos","RK-Bro loses — Orton and Riddle as surprising crowd favorites","L"))
rows.append(row(w,"tv",a("stone-cold-steve-austin","Steve Austin"),"Raw 20th Anniversary","2013","Promo interaction","Austin-Orton cross-era segment — Stone Cold delivers Stunner"))
w["record_rows"] = "".join(rows)
w["method_bars"] = [
    {"label": "Pinfall (RKO)", "pct": 62},
    {"label": "Submission", "pct": 8},
    {"label": "Countout/DQ", "pct": 16},
    {"label": "Special stipulation", "pct": 14},
]
w["faq"] = [
    {"q": "How many world titles has Randy Orton won?", "a": "Randy Orton has won 14 world titles: 8 WWE Championships and 6 World Heavyweight Championships."},
    {"q": "Who is the youngest world champion in WWE history?", "a": "Randy Orton became the youngest WWE world champion in history when he defeated Chris Benoit for the World Heavyweight Championship at SummerSlam 2004 at age 24."},
    {"q": "What is Randy Orton's finishing move?", "a": "Randy Orton's finishing move is the RKO — a jumping cutter that Orton can execute from virtually any position, including as a counter from mid-air. The 'RKO outta nowhere' became one of wrestling's most replicated viral moments."},
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

print("\nBatch 4a complete.")
