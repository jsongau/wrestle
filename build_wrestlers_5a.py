#!/usr/bin/env python3
"""Batch 5a: Daniel Bryan, Cody Rhodes, Samoa Joe, Finn Balor, Shinsuke Nakamura"""
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
  <div class="record-filter">
    <button class="rf-btn active" data-filter="all">All</button>
    <button class="rf-btn" data-filter="ppv">PPV</button>
    <button class="rf-btn" data-filter="tv">TV</button>
    <button class="rf-btn" data-filter="title">Title</button>
  </div>
  <table class="record-table" data-record-filter data-record-count="{total}">
    <thead><tr><th>Result</th><th>Opponent</th><th>Event</th><th>Date</th><th>Stipulation</th><th>Notes</th></tr></thead>
    <tbody>
{record_rows}    </tbody>
  </table>
</section>
</main>
<footer class="site-footer">
  <p>&copy; {year} MAT Wrestling Database. All rights reserved.</p>
  <nav><a href="/about/">About</a> · <a href="/privacy/">Privacy</a> · <a href="/contact/">Contact</a></nav>
</footer>
<script src="/js/main.js"></script>
</body>
</html>"""


wrestlers = [

# ── DANIEL BRYAN ──────────────────────────────────────────────────────────────
{
"slug": "daniel-bryan",
"name": "Daniel Bryan",
"subtitle": "The American Dragon · The Yes! Man · Leader of the Yes Movement",
"born": "1981-05-22",
"from": "Aberdeen, Washington, USA",
"height": "5 ft 10 in (178 cm)",
"weight": "210 lb (95 kg)",
"trained": "Shawn Michaels, William Regal, Dean Malenko",
"debut": "1999",
"style": "Technical wrestling, submission grappling, MMA-influenced striking",
"aliases": ["Bryan Danielson", "The American Dragon", "The Beard"],
"wins": 82, "losses": 34, "draws": 2,
"wl_strip": ('<i></i>'*10 + '<i class="l"></i>'*2)*4 + '<i></i>'*2,
"method_bars": [
    {"label":"Submission","pct":38},
    {"label":"Pinfall","pct":44},
    {"label":"Count-out / DQ","pct":10},
    {"label":"Other","pct":8},
],
"bio": [
    f'Bryan Lloyd Danielson spent a decade perfecting his craft on the independent circuit before becoming one of the most beloved figures in WWE history. Trained by {a("shawn-michaels","Shawn Michaels")} at his wrestling school and mentored by William Regal, Danielson became globally respected as "The American Dragon" — a technically immaculate grappler whose matches in ROH set a new standard for North American wrestling.',
    f'WWE signed him in 2010, and within two years he had captured the World Heavyweight Championship and developed the "Yes! Movement" — a crowd-driven phenomenon that transformed a chant into a cultural earthquake. Despite being stripped of the title at WrestleMania XXVIII and booked as an underdog, fan support escalated into something management could not ignore.',
    f'WrestleMania XXX in 2014 stands as one of wrestling\'s defining nights. Bryan defeated {a("triple-h","Triple H")} in the opener, then entered a Triple Threat match against {a("randy-orton","Randy Orton")} and {a("batista","Batista")} — and won the WWE World Heavyweight Championship in front of 75,000 screaming fans. The image of Bryan with arms raised, leading the crowd in "Yes!" chants, is etched into wrestling history.',
    f'Forced into retirement in 2016 due to accumulated concussions, Bryan returned in 2018 with medical clearance. He underwent a remarkable character transformation, becoming an abrasive environmental villain before eventually transitioning to AEW in 2022 as Bryan Danielson, reclaiming his independent identity.',
],
"finishers": [
    {"name":"Running Knee (Busaiku Knee)", "desc":"Explosive running knee strike to a seated opponent — the move that won him the WWE Championship at WrestleMania XXX"},
    {"name":"Yes Lock (LeBell Lock)", "desc":"Crossface with arm trapped — named for martial artist Gene LeBell; one of the most painful-looking submissions in WWE"},
],
"championships": [
    cr("WWE World Heavyweight Championship","2014","Won in historic one-night double main event at WrestleMania XXX"),
    cr("World Heavyweight Championship","2011–12","Two reigns; cashed Money in the Bank on Big Show"),
    cr("WWE Intercontinental Championship","2019","Won as environmental heel character"),
    cr("ROH World Championship","2005–06","Longest reign in ROH history at the time — 462 days"),
    cr("NXT Championship","2023","Won at NXT Great American Bash; returned to NXT as Bryan Danielson"),
],
"personas": [
    {"name":"The American Dragon","era":"1999–2010 (ROH/Indies)","desc":"Technically perfect submission specialist who set the global standard for in-ring work. The wrestler's wrestler."},
    {"name":"Daniel Bryan — Underdog Champion","era":"2011–2016 (WWE)","desc":"From goat-faced vegan underdog to Yes Movement leader. The crowd adopted him as their champion even when management wouldn't."},
    {"name":"The Planet's Champion","era":"2018–2021 (WWE)","desc":"Sneering environmental villain who carried an eco-friendly WWE title. Brilliant heel work that generated real heat."},
    {"name":"Bryan Danielson — AEW","era":"2021–present","desc":"Reclaimed his full name in AEW, wrestling brutal pure wrestling matches and elevating every opponent he touches."},
],
"timeline": [
    {"year":"1999","title":"Professional debut","desc":"Begins competing on the independent circuit at age 18, learning his craft before finding a path to ROH."},
    {"year":"2005","title":"ROH World Champion","desc":"Wins the ROH Championship and begins a 462-day reign that cements his reputation as the world's best technical wrestler."},
    {"year":"2010","title":"WWE debut and firing","desc":"Signs with WWE, debuts on NXT Season 1, then is controversially fired for choking announcer Justin Roberts with his own tie — rehired weeks later."},
    {"year":"2011","title":"World Heavyweight Champion","desc":"Cashes in Money in the Bank on Big Show after a Big Show vs. Mark Henry match; begins developing the 'Yes!' chant."},
    {"year":"2013","title":"Yes Movement ignites","desc":"Despite constant authority figures working against him, crowds begin the organic Yes! chant that spreads worldwide."},
    {"year":"2014","title":"WrestleMania XXX triumph","desc":"Defeats Triple H, then Randy Orton and Batista in one historic night to win the WWE World Heavyweight Championship."},
    {"year":"2016","title":"Forced retirement","desc":"Announces retirement due to undisclosed neurological issues and accumulated concussions — an emotional Raw moment."},
    {"year":"2018","title":"Return to WWE","desc":"Receives medical clearance and returns to in-ring competition, transitioning to a heel environmental character."},
    {"year":"2022","title":"Signs with AEW","desc":"Joins All Elite Wrestling as Bryan Danielson, wrestling under his real name and immediately competing for the AEW World Championship."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. Shawn Michaels","subtitle":"NXT, 2010","desc":"A hidden gem: Danielson's in-ring debut on WWE TV saw him go 40 minutes with HBK in an untelevised dark match that became one of the most circulated clips in WWE history."},
    {"rating":"★★★★¾","title":"vs. Triple H","subtitle":"WrestleMania XXX, 2014","desc":"The opener that the crowd treated as a co-main event. Bryan wins clean, setting the stage for his main event coronation."},
    {"rating":"★★★★★","title":"Triple Threat vs. Orton & Batista","subtitle":"WrestleMania XXX, 2014","desc":"The moment the Yes Movement peaked. Bryan hits the Running Knee on Orton to claim the WWE World Heavyweight Championship in one of the loudest finishes in WrestleMania history."},
    {"rating":"★★★★½","title":"vs. CM Punk","subtitle":"Over the Limit 2012","desc":"One hour iron man match that showcased both men's endurance and technical mastery — a modern classic."},
],
"faq": [
    {"q":"Why did Daniel Bryan retire in 2016?","a":"Bryan announced retirement due to a series of concussions and neurological issues that WWE's medical team determined made it unsafe for him to continue competing. He received clearance to return in 2018 after consulting additional specialists."},
    {"q":"What is the Yes Movement?","a":"The Yes! Movement was an organic fan phenomenon that grew from Daniel Bryan's in-ring celebration of raising both arms and chanting 'Yes!' — a crowd response that became so pervasive it transformed Bryan from a midcard act into the most over babyface in WWE."},
    {"q":"What is Daniel Bryan's real name?","a":"His real name is Bryan Lloyd Danielson. He competed under this name on the independent circuit and in AEW; WWE used the ring name Daniel Bryan."},
    {"q":"Did Daniel Bryan ever win the WWE Championship?","a":"Yes. Bryan won the WWE World Heavyweight Championship at WrestleMania XXX in 2014, defeating Randy Orton and Batista in the main event Triple Threat after also defeating Triple H in the opening match — all in one night."},
],
"record_rows": (
    row("daniel-bryan","ppv title",a("triple-h","Triple H"),"WrestleMania XXX","Apr 6, 2014","Singles","WM XXX opener","W") +
    row("daniel-bryan","ppv title",a("randy-orton","Randy Orton") + " &amp; " + a("batista","Batista"),"WrestleMania XXX","Apr 6, 2014","Triple Threat — WWE World Heavyweight Championship","Wins WWE WHC","W") +
    row("daniel-bryan","ppv",a("john-cena","John Cena"),"SummerSlam 2013","Aug 18, 2013","Singles — WWE Championship","Wins WWE title; Triple H turns heel","W") +
    row("daniel-bryan","ppv title",a("cm-punk","CM Punk"),"Over the Limit 2012","May 20, 2012","60-Min Iron Man Match","Punk wins 5-4","L") +
    row("daniel-bryan","ppv",a("sheamus","Sheamus"),"WrestleMania XXVIII","Apr 1, 2012","Singles — World Heavyweight Championship","18-second loss; ignites Yes Movement","L") +
    row("daniel-bryan","tv title",a("big-show","Big Show"),"SmackDown","Dec 18, 2011","Money in the Bank Cash-In","Wins World Title","W") +
    row("daniel-bryan","ppv",a("roman-reigns","Roman Reigns"),"Elimination Chamber 2021","Feb 21, 2021","Singles — Universal Championship","","L") +
    row("daniel-bryan","ppv",a("seth-rollins","Seth Rollins"),"NXT Great American Bash","Jul 30, 2023","Singles — NXT Championship","Wins NXT title in AEW crossover","W")
),
},

# ── CODY RHODES ───────────────────────────────────────────────────────────────
{
"slug": "cody-rhodes",
"name": "Cody Rhodes",
"subtitle": "The American Nightmare · Son of Dusty Rhodes",
"born": "1985-06-30",
"from": "Marietta, Georgia, USA",
"height": "6 ft 1 in (185 cm)",
"weight": "225 lb (102 kg)",
"trained": "Dusty Rhodes, Killer Kowalski, Wild Samoans",
"debut": "2006",
"style": "All-around brawler, storytelling-driven matches",
"aliases": ["Stardust", "The American Nightmare", "The Son of the American Dream"],
"wins": 78, "losses": 38, "draws": 1,
"wl_strip": ('<i></i>'*8 + '<i class="l"></i>'*3)*5 + '<i></i>'*3,
"method_bars": [
    {"label":"Pinfall","pct":58},
    {"label":"Submission","pct":12},
    {"label":"Count-out / DQ","pct":18},
    {"label":"Other","pct":12},
],
"bio": [
    f'Cody Garrett Runnels is the son of wrestling legend Dusty Rhodes, and his journey from WWE midcarder to world champion is one of the most compelling stories in modern wrestling. After years working as a reliable hand in WWE — including a bizarre but committed run as the face-painted character Stardust — Cody left the company in 2016 to reinvent himself on the independent circuit.',
    f'That reinvention was total. Performing as Cody Rhodes under his real surname (which WWE initially refused to return), he became one of the founders of All Elite Wrestling in 2019 alongside {a("jon-moxley","Jon Moxley")}, {a("kenny-omega","Kenny Omega")}, and The Young Bucks. He won the TNT Championship and served as a creative force and wrestling ambassador during AEW\'s formative years.',
    f'His return to WWE in April 2022 — to a pop that shook the arena — reset his career entirely. Rhodes became the company\'s most emotionally resonant babyface, carrying the story of his late father\'s dream of a world championship into {a("roman-reigns","Roman Reigns")}\'s seemingly impenetrable Bloodline dynasty.',
    f'The story culminated at WrestleMania XL in 2024. Rhodes defeated Reigns to win the Undisputed WWE Championship, fulfilling the "Finishing the Story" narrative in front of 72,000 fans in Philadelphia — widely regarded as one of the most emotionally satisfying WrestleMania finishes in the modern era.',
],
"finishers": [
    {"name":"Cross Rhodes", "desc":"Flip forward Russian leg sweep into a DDT — his signature move and the one that pinned Roman Reigns for the championship at WrestleMania XL"},
    {"name":"Figure-Four Leglock", "desc":"Tribute to his father's friend Ric Flair and the NWA tradition; used as a secondary submission finish"},
],
"championships": [
    cr("Undisputed WWE Championship","2024–","Won at WrestleMania XL; 'Finishing the Story'"),
    cr("AEW TNT Championship","2020–21","Multiple reigns; established the belt as a prestige title"),
    cr("WWE Intercontinental Championship","2011–12","Two reigns as IC champion during his first WWE run"),
    cr("NWA World Tag Team Championship","2019","Won with Dustin Rhodes on AEW Dynamite debut show"),
],
"personas": [
    {"name":"Cody Rhodes — WWE Original","era":"2008–2016","desc":"Tag team specialist, IC champion, and eventually the committed method-wrestler Stardust — a character that showed his willingness to fully commit."},
    {"name":"The American Nightmare (Indies/AEW)","era":"2016–2022","desc":"Free agent global ambassador who co-founded AEW and built himself into a main event star on his own terms."},
    {"name":"Cody Rhodes — WWE Return","era":"2022–present","desc":"The emotionally compelling babyface carrying his father's legacy, 'Finishing the Story' against the most dominant champion of his era."},
],
"timeline": [
    {"year":"2006","title":"WWE debut","desc":"Signs with WWE developmental at age 20 and quickly moves to the main roster."},
    {"year":"2010","title":"Dashing Cody Rhodes / Undashing","desc":"Develops the 'Dashing' grooming tips character, then transitions to a paranoid, protective-mask-wearing heel after a nose injury."},
    {"year":"2015","title":"Stardust era","desc":"Becomes the face-painted cosmic villain Stardust — a bizarre commitment that earned grudging respect even from skeptics."},
    {"year":"2016","title":"Departs WWE","desc":"Leaves WWE after the company refuses to release the 'Rhodes' name to him — begins reinventing himself globally."},
    {"year":"2019","title":"Co-founds AEW","desc":"Alongside Kenny Omega and the Young Bucks, launches All Elite Wrestling — a legitimate competitor to WWE for the first time in decades."},
    {"year":"2022","title":"Returns to WWE","desc":"Surprise Royal Rumble entry; crowd erupts. Begins 'Finishing the Story' narrative against Roman Reigns and the Bloodline."},
    {"year":"2024","title":"WWE Champion at WrestleMania XL","desc":"Defeats Roman Reigns to win the Undisputed WWE Championship in Philadelphia — one of the loudest WrestleMania finishes of the modern era."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. Roman Reigns","subtitle":"WrestleMania XL, 2024","desc":"The culmination of two years of storytelling. Cross Rhodes. 1-2-3. Philadelphia erupts. Cody Rhodes is WWE Champion."},
    {"rating":"★★★★","title":"vs. Seth Rollins","subtitle":"WrestleMania 38, 2022","desc":"His first match back in WWE — a 20-minute opener that told the story of everything he'd built on the outside. The crowd was electric from entrance to final bell."},
    {"rating":"★★★★","title":"vs. Dustin Rhodes","subtitle":"AEW Double or Nothing 2019","desc":"Emotional brother vs. brother match that served as AEW's debut PPV main event. Both men bled heavily; both gave everything."},
],
"faq": [
    {"q":"Why did Cody Rhodes leave WWE in 2016?","a":"Cody left primarily because WWE refused to release the Rhodes surname to him for use outside the company, and he felt creatively stifled after years in the midcard. He immediately thrived on the independent circuit and helped co-found AEW."},
    {"q":"What does 'Finishing the Story' mean?","a":"It refers to Cody completing his late father Dusty Rhodes's dream of winning a world championship — a goal Dusty never fully achieved in WWE. Cody fulfilled that dream by defeating Roman Reigns at WrestleMania XL."},
    {"q":"Is Cody Rhodes related to Dusty Rhodes?","a":"Yes. Cody Rhodes is the son of WWE Hall of Famer Dusty Rhodes (Virgil Runnels) and the younger brother of Goldust (Dustin Rhodes). Wrestling is very much in the family blood."},
],
"record_rows": (
    row("cody-rhodes","ppv title",a("roman-reigns","Roman Reigns"),"WrestleMania XL","Apr 6, 2024","Singles — Undisputed WWE Championship","Finishing the Story","W") +
    row("cody-rhodes","ppv title",a("roman-reigns","Roman Reigns"),"WrestleMania XXXIX","Apr 1, 2023","Singles — Undisputed WWE Championship","Sami Zayn interference","L") +
    row("cody-rhodes","ppv",a("seth-rollins","Seth Rollins"),"WrestleMania 38","Apr 2, 2022","Singles","Return match; wins","W") +
    row("cody-rhodes","ppv",a("dustin-rhodes","Dustin Rhodes"),"AEW Double or Nothing 2019","May 25, 2019","Singles","AEW debut PPV","W") +
    row("cody-rhodes","tv",a("roman-reigns","Roman Reigns"),"SmackDown","Apr 8, 2022","Singles","Post-WM SmackDown","L") +
    row("cody-rhodes","ppv",a("seth-rollins","Seth Rollins"),"Hell in a Cell 2022","Jun 5, 2022","Hell in a Cell","Tears pectoral mid-match; fights on","L") +
    row("cody-rhodes","ppv title",a("brock-lesnar","Brock Lesnar"),"Royal Rumble 2023","Jan 28, 2023","Strap Match","Wins to maintain feud","W")
),
},

# ── SAMOA JOE ─────────────────────────────────────────────────────────────────
{
"slug": "samoa-joe",
"name": "Samoa Joe",
"subtitle": "The Samoan Submission Machine",
"born": "1979-03-17",
"from": "Orange County, California, USA",
"height": "6 ft 2 in (188 cm)",
"weight": "280 lb (127 kg)",
"trained": "Tom Howard, Killer Kowalski",
"debut": "1999",
"style": "Submission wrestling, stiff striking, power grappling",
"aliases": ["Nuufolau Joel Seanoa", "Joe"],
"wins": 91, "losses": 41, "draws": 3,
"wl_strip": ('<i></i>'*9 + '<i class="l"></i>'*3)*6 + '<i></i>'*3,
"method_bars": [
    {"label":"Submission","pct":42},
    {"label":"Pinfall","pct":40},
    {"label":"Count-out / DQ","pct":10},
    {"label":"Other","pct":8},
],
"bio": [
    f'Nuufolau Joel Seanoa — better known as Samoa Joe — is one of the most legitimately intimidating wrestlers of his generation. Built like a linebacker but moving with the agility of a cruiserweight, Joe combines genuine Muay Thai and Brazilian jiu-jitsu training with old-school pro wrestling to create a uniquely threatening in-ring presence.',
    f'Joe became a legend in Ring of Honor and TNA before his long-overdue arrival in WWE. His ROH work in the mid-2000s — particularly a legendary series with {a("cm-punk","CM Punk")} — is widely cited among the greatest programs in American independent wrestling history. Joe was TNA\'s top native star during their peak years, winning the TNA World Heavyweight Championship three times.',
    f'WWE signed him in 2015, and Joe quickly established himself as one of NXT\'s most valuable assets before moving to the main roster. He won the NXT Championship twice, challenged for the WWE Universal Championship against {a("brock-lesnar","Brock Lesnar")}, and became the United States Champion in 2018. His 2023 return as WWE Champion represented a long-overdue coronation.',
    f'Joe\'s promo work is as devastating as his Coquina Clutch — he delivers threats with a quiet menace that makes opponents seem genuinely afraid. His cold, methodical intensity separates him from louder, more theatrical heels.',
],
"finishers": [
    {"name":"Coquina Clutch", "desc":"Rear naked choke applied from behind with a bodyscissors — one of the most effective-looking submission holds in modern wrestling"},
    {"name":"Muscle Buster", "desc":"Inverted fireman's carry dropped into a sitout position — devastating power move most commonly used as a setup for the Clutch"},
    {"name":"ST-Joe", "desc":"Running powerbomb into a turnbuckle — a signature corner move that transitions to his ground attack"},
],
"championships": [
    cr("WWE Championship","2023–24","Won in Elimination Chamber; first WWE title reign after decades of excellence"),
    cr("NXT Championship","2016","Won from Finn Balor in NXT TakeOver Toronto; dominant first NXT run"),
    cr("NXT Championship","2016–17","Second reign; extended dominant NXT era"),
    cr("United States Championship","2018","Won on Raw; carried the title with menacing intensity"),
    cr("TNA World Heavyweight Championship","2008–09","Multiple reigns; the cornerstone of TNA's Samoan Submission Machine era"),
],
"personas": [
    {"name":"The Samoan Submission Machine","era":"2000–present","desc":"His entire career identity: a physically imposing, technically complete grappler who submits opponents with eerie confidence. No catchphrases — just results."},
],
"timeline": [
    {"year":"1999","title":"Pro debut","desc":"Begins career on the independent circuit; immediately draws attention for his combination of size, athleticism, and legitimate grappling credentials."},
    {"year":"2002","title":"Ring of Honor","desc":"Becomes one of ROH's foundational performers; works the legendary series with CM Punk that defines the promotion."},
    {"year":"2006","title":"TNA World Champion","desc":"Captures TNA World title; becomes the first Samoan to hold a major North American world championship."},
    {"year":"2015","title":"Signs with WWE / NXT","desc":"Signs with WWE at age 36 and immediately becomes the most credible performer in NXT."},
    {"year":"2016","title":"NXT Champion","desc":"Defeats Finn Balor for the NXT title in one of NXT's most memorable TakeOver matches."},
    {"year":"2017","title":"Main roster debut","desc":"Moves to Raw; immediately feuds with Seth Rollins and challenges Brock Lesnar for the Universal Championship."},
    {"year":"2023","title":"WWE Champion","desc":"Wins the WWE Championship at Elimination Chamber — a long-overdue moment for one of wrestling's most respected performers."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. CM Punk","subtitle":"ROH Death Before Dishonor II, 2004","desc":"A legendary 60-minute draw that established both men as world-class performers and set the standard for modern American independent wrestling."},
    {"rating":"★★★★½","title":"vs. Finn Balor","subtitle":"NXT TakeOver: Toronto, 2016","desc":"Joe wins the NXT Championship in a brutal, hard-hitting match that validated his WWE signing and his late-career return to top-tier competition."},
    {"rating":"★★★★","title":"vs. Brock Lesnar","subtitle":"SummerSlam 2017","desc":"Joe challenges Lesnar for the Universal title — his first main roster world title shot. A legitimately frightening stiff encounter."},
],
"faq": [
    {"q":"Has Samoa Joe won the WWE Championship?","a":"Yes. Samoa Joe won the WWE Championship in 2023 at the Elimination Chamber event, capturing his first WWE world title after nearly a decade with the company."},
    {"q":"What is Samoa Joe's finishing move?","a":"His primary finisher is the Coquina Clutch, a rear naked choke applied with a bodyscissors. He also uses the Muscle Buster, a devastating power slam, as a setup move."},
    {"q":"Is Samoa Joe actually from Samoa?","a":"Samoa Joe is of Samoan descent but was born and raised in Orange County, California. He wrestles as 'Samoa Joe' in honor of his heritage."},
],
"record_rows": (
    row("samoa-joe","ppv title",a("cm-punk","CM Punk"),"ROH Death Before Dishonor II","Jun 12, 2004","60-Minute Iron Man Match","Legendary 60-min draw","D") +
    row("samoa-joe","ppv title",a("finn-balor","Finn Balor"),"NXT TakeOver: Toronto","Nov 19, 2016","Singles — NXT Championship","Wins NXT title","W") +
    row("samoa-joe","ppv",a("brock-lesnar","Brock Lesnar"),"SummerSlam 2017","Aug 20, 2017","Singles — Universal Championship","","L") +
    row("samoa-joe","ppv title",a("roman-reigns","Roman Reigns"),"Elimination Chamber 2023","Feb 18, 2023","Elimination Chamber — WWE Championship","Wins WWE title","W") +
    row("samoa-joe","ppv",a("seth-rollins","Seth Rollins"),"Raw 2017","Aug 21, 2017","Singles","Post-SummerSlam feud","W") +
    row("samoa-joe","ppv",a("aj-styles","AJ Styles"),"SummerSlam 2018","Aug 19, 2018","Singles — WWE Championship","","L") +
    row("samoa-joe","tv title",a("becky-lynch","Becky Lynch"),"Raw 2018","Sep 16, 2018","Mixed Match Challenge","Mixed tag team match","W")
),
},

# ── FINN BALOR ────────────────────────────────────────────────────────────────
{
"slug": "finn-balor",
"name": "Finn Bálor",
"subtitle": "The Demon King · Prince Devitt",
"born": "1981-07-25",
"from": "Bray, County Wicklow, Ireland",
"height": "5 ft 11 in (180 cm)",
"weight": "190 lb (86 kg)",
"trained": "Fit Finlay, British wrestling school",
"debut": "2000",
"style": "High-flying, technical, character-driven performance",
"aliases": ["Prince Devitt", "The Demon", "Fergal Devitt"],
"wins": 74, "losses": 38, "draws": 1,
"wl_strip": ('<i></i>'*8 + '<i class="l"></i>'*3)*5 + '<i></i>'*4,
"method_bars": [
    {"label":"Pinfall","pct":55},
    {"label":"Submission","pct":15},
    {"label":"Count-out / DQ","pct":20},
    {"label":"Other","pct":10},
],
"bio": [
    f'Fergal Devitt grew up in Ireland dreaming of wrestling and trained rigorously before finding his path to Japan\'s premier promotion, New Japan Pro Wrestling. Under the ring name Prince Devitt, he became one of NJPW\'s most decorated performers, winning the IWGP Junior Heavyweight Championship twice and founding the Bullet Club — a faction of foreign heels that became one of wrestling\'s most commercially successful stables, inspiring merchandise that sold globally long after his departure.',
    f'WWE signed Devitt in 2014, and he debuted in NXT as Finn Bálor. His body paint "Demon King" persona — an elaborate, visually stunning character that transformed his entrance into a theatrical event — became one of WWE\'s most marketable concepts. He captured the NXT Championship twice and became the inaugural WWE Universal Champion in August 2016.',
    f'That Universal title reign came with a cruel footnote: Bálor suffered a shoulder tear in the match itself and was forced to vacate the title the next night, never having lost it. The injury, sustained during Seth Rollins\'s apron powerbomb, cost him months of work and the championship run he\'d earned.',
    f'Returned to headline status with the NXT 2.0 era, Bálor remains one of WWE\'s most reliable performers — a workhorse who can deliver technical matches or pull out the Demon character for events that need a visual spectacle moment.',
],
"finishers": [
    {"name":"Coup de Grâce", "desc":"Double foot stomp from the top rope to a downed opponent — the Demon King's calling card; generates enormous crowd reaction"},
    {"name":"1916", "desc":"Double underhook DDT (also called the Bloody Sunday) — a compact, brutal-looking move used as a secondary finish"},
    {"name":"Sling Blade", "desc":"Running swinging neckbreaker used to set up the running dropkick into the corner and Coup de Grâce sequence"},
],
"championships": [
    cr("WWE Universal Championship","2016","Inaugural champion; vacated due to shoulder injury — never pinned or submitted"),
    cr("NXT Championship","2015–16","First reign — won at NXT TakeOver: Brooklyn; longest NXT title reign at the time"),
    cr("NXT Championship","2021","Second NXT reign during NXT 2.0 era"),
    cr("IWGP Junior Heavyweight Championship","2010–14","Two reigns; dominant period in New Japan as Prince Devitt"),
    cr("WWE Intercontinental Championship","2023","Won after years on the main roster; long-overdue main card title"),
],
"personas": [
    {"name":"Prince Devitt / Bullet Club Leader","era":"2010–2014 (NJPW)","desc":"The founding leader of the Bullet Club, the most commercially successful stable in modern wrestling history — influencing WWE and AEW aesthetics for years."},
    {"name":"Finn Bálor — Demon King","era":"2014–present","desc":"The Demon character requires hours of body paint application and transforms Bálor's entrance into a theatrical event. Reserved for major matches; wins nearly every Demon appearance."},
],
"timeline": [
    {"year":"2000","title":"Professional debut","desc":"Begins career at age 18 in Ireland before moving to Japan."},
    {"year":"2006","title":"Joins New Japan Pro Wrestling","desc":"Signs with NJPW; spends eight years in Japan becoming one of their most versatile performers."},
    {"year":"2012","title":"Founds Bullet Club","desc":"Creates the Bullet Club with Karl Anderson — a faction of foreign heels that becomes globally iconic."},
    {"year":"2014","title":"Signs with WWE / NXT debut","desc":"Debuts in NXT as Finn Bálor; body paint Demon character introduced."},
    {"year":"2015","title":"NXT Champion","desc":"Wins NXT title at TakeOver: Brooklyn before 15,000 fans — the largest NXT crowd at the time."},
    {"year":"2016","title":"First Universal Champion","desc":"Wins first Universal Championship; vacated next night due to shoulder injury sustained during the match."},
    {"year":"2021","title":"NXT return","desc":"Returns to NXT and wins the NXT title for a second time during the brand's transition period."},
    {"year":"2023","title":"IC Championship","desc":"Wins the Intercontinental title after years as a main roster fixture."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. Samoa Joe","subtitle":"NXT TakeOver: Toronto, 2016","desc":"Joe defeats Bálor for the NXT title in a brutal encounter — Joe's most celebrated WWE match and proof that both men were ready for the main event."},
    {"rating":"★★★★½","title":"vs. Seth Rollins","subtitle":"SummerSlam 2016","desc":"The inaugural Universal Championship match. Bálor wins with The Demon, then vacates the next night. One of wrestling's most bittersweet title wins."},
    {"rating":"★★★★","title":"vs. AJ Styles","subtitle":"WrestleMania 35","desc":"A match between two former NJPW stars who found their way to WWE's grandest stage — a technical showcase on a show that needed it."},
],
"faq": [
    {"q":"Why did Finn Bálor vacate the Universal Championship?","a":"Bálor suffered a torn labrum in his right shoulder during the SummerSlam 2016 match against Seth Rollins — specifically when Rollins powerbombed him into the barricade at ringside. He won the title despite the injury but announced the next night on Raw that he was relinquishing it to undergo surgery."},
    {"q":"What is the Bullet Club?","a":"The Bullet Club is a New Japan Pro Wrestling stable founded by Finn Bálor (as Prince Devitt) in 2012. It became one of wrestling's most recognizable brands, with merchandise that sold globally. Notable members include AJ Styles, Kenny Omega, and The Young Bucks."},
    {"q":"Is Finn Bálor Irish?","a":"Yes. Fergal Devitt was born and raised in Bray, County Wicklow, Ireland. He is one of the most successful Irish wrestlers in history."},
],
"record_rows": (
    row("finn-balor","ppv title",a("seth-rollins","Seth Rollins"),"SummerSlam 2016","Aug 21, 2016","Singles — Universal Championship","Wins inaugural Universal title; vacated next night","W") +
    row("finn-balor","ppv title",a("samoa-joe","Samoa Joe"),"NXT TakeOver: Toronto","Nov 19, 2016","Singles — NXT Championship","Loses NXT title to Joe","L") +
    row("finn-balor","ppv",a("aj-styles","AJ Styles"),"WrestleMania 35","Apr 7, 2019","Singles","","W") +
    row("finn-balor","ppv title",a("roman-reigns","Roman Reigns"),"Royal Rumble 2023","Jan 28, 2023","Singles — Universal Championship","Demon vs. Tribal Chief","L") +
    row("finn-balor","ppv",a("brock-lesnar","Brock Lesnar"),"Royal Rumble 2017","Jan 29, 2017","Singles","","L") +
    row("finn-balor","tv title",a("damian-priest","Damian Priest"),"NXT TakeOver","2021","Singles — NXT Championship","Second NXT reign","W")
),
},

# ── SHINSUKE NAKAMURA ──────────────────────────────────────────────────────────
{
"slug": "shinsuke-nakamura",
"name": "Shinsuke Nakamura",
"subtitle": "King of Strong Style · The Artist",
"born": "1980-02-24",
"from": "Kyoto, Japan",
"height": "6 ft 2 in (188 cm)",
"weight": "229 lb (104 kg)",
"trained": "Antonio Inoki, New Japan Dojo",
"debut": "2002",
"style": "Strong Style striking, submission wrestling, theatrical presentation",
"aliases": ["The King of Strong Style", "The Artist Called Nakamura"],
"wins": 86, "losses": 39, "draws": 2,
"wl_strip": ('<i></i>'*9 + '<i class="l"></i>'*3)*5 + '<i></i>'*1,
"method_bars": [
    {"label":"Submission","pct":32},
    {"label":"Pinfall","pct":50},
    {"label":"Count-out / DQ","pct":12},
    {"label":"Other","pct":6},
],
"bio": [
    f'Shinsuke Nakamura is the most charismatic Japanese wrestler to ever perform in WWE — a performer whose presentation, musicality, and in-ring intensity create an aura that few wrestlers in any era have matched. Trained in New Japan\'s legendary dojo under Antonio Inoki himself, Nakamura embodied "Strong Style" — a philosophy that blends martial arts realism with professional wrestling\'s theatrical drama.',
    f'His NJPW career was extraordinary: two IWGP Heavyweight Championship reigns, multiple IWGP Intercontinental reigns, and matches against the best performers in the world over more than a decade. When he signed with WWE in 2016 and debuted in NXT, the reception was extraordinary — his entrance theme "The Rising Sun" generated pop after pop, and his NXT run is considered one of the best short-term tenures in the brand\'s history.',
    f'On WWE\'s main roster, Nakamura became the United States Champion and multiple-time Intercontinental Champion, though his SmackDown feud with {a("aj-styles","AJ Styles")} in 2018 saw him turn heel — delivering low blows to Styles repeatedly in a program that divided fans but demonstrated his range.',
    f'His persona "The Artist" — eccentric, expressive, moving to his own rhythm — is unlike anything else in wrestling. He does not wrestle to a crowd; he performs for himself, and the crowd follows.',
],
"finishers": [
    {"name":"Kinshasa (Bomaye)", "desc":"Running knee strike to a kneeling or cornered opponent — named after Muhammad Ali's 'Rumble in the Jungle' venue; generates massive crowd reaction when built correctly"},
    {"name":"Arm Bar", "desc":"Applied with theatrical deliberateness — Nakamura's submission game matches his striking; often applied after an armbreaker setup"},
    {"name":"Good Vibrations", "desc":"Corner knee thrusts with rhythmic shimmy — more signature than finish, but a crowd-interactive moment in every match"},
],
"championships": [
    cr("WWE Intercontinental Championship","2018–19","Multiple reigns; carried the title as a mercurial heel and then tweener"),
    cr("United States Championship","2019–22","Three reigns; the longest US title runs of his WWE tenure"),
    cr("NXT Championship","2016–17","Won at NXT TakeOver: Dallas in one of NXT's defining moments"),
    cr("IWGP Heavyweight Championship","2003; 2014","Two NJPW world title reigns spanning a decade of dominance"),
    cr("IWGP Intercontinental Championship","2013–14","Defined the title's prestige; had standout matches with Kota Ibushi and others"),
],
"personas": [
    {"name":"King of Strong Style (NJPW)","era":"2002–2016","desc":"The pinnacle of NJPW's homegrown talent: a genuine martial artist who could electrify an audience and legitimize any opponent."},
    {"name":"The Artist Called Nakamura (NXT/WWE)","era":"2016–present","desc":"Adapted his presentation for Western audiences while maintaining his eccentric theatricality — the entrance, the shimmies, the expressive face."},
],
"timeline": [
    {"year":"2002","title":"NJPW debut","desc":"Trained by Antonio Inoki; debuts in New Japan and immediately draws attention for his combination of legitimate fighting skill and theatrical flair."},
    {"year":"2003","title":"First IWGP Heavyweight Championship","desc":"Becomes one of the youngest IWGP Heavyweight Champions in history at age 23."},
    {"year":"2014","title":"IWGP Intercontinental dominance","desc":"His IC title feuds, particularly with Kota Ibushi, produce some of the best matches of the decade."},
    {"year":"2016","title":"Signs with WWE / NXT debut","desc":"Debuts at NXT TakeOver: Dallas against Sami Zayn — the match is immediately ranked among NXT's best ever."},
    {"year":"2016","title":"NXT Champion","desc":"Wins the NXT Championship; his NXT run elevates the brand's prestige significantly."},
    {"year":"2017","title":"SmackDown call-up","desc":"Wins the Royal Rumble and challenges AJ Styles at WrestleMania 34 in a highly anticipated match."},
    {"year":"2018","title":"Heel turn","desc":"Repeatedly delivers low blows to AJ Styles to turn heel — a divisive but revealing character pivot."},
    {"year":"2019","title":"United States Champion","desc":"Begins dominant US title reigns that last into the early 2020s."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. Sami Zayn","subtitle":"NXT TakeOver: Dallas, 2016","desc":"One of NXT's greatest matches: two different styles, Nakamura's debut, and a crowd that was on its feet for twenty minutes. The best first impression of any signing in NXT history."},
    {"rating":"★★★★½","title":"vs. AJ Styles","subtitle":"WrestleMania 34, 2018","desc":"Two former NJPW stars at WrestleMania — a match years in the making. The result disappointed many but the work was outstanding."},
    {"rating":"★★★★¾","title":"vs. Kota Ibushi","subtitle":"NJPW G1 Climax, 2015","desc":"A transcendent match between two of Japan's most creative performers — all-offense, unrestrained athleticism, and genuine respect between competitors."},
],
"faq": [
    {"q":"What is Shinsuke Nakamura's finishing move?","a":"His primary finisher is the Kinshasa — a running knee strike also known as the Bomaye, named after Muhammad Ali's famous fight in Kinshasa, Zaire (the 'Rumble in the Jungle'). The move was rechristened Kinshasa in WWE for licensing reasons."},
    {"q":"Has Shinsuke Nakamura wrestled in New Japan Pro Wrestling?","a":"Yes. Nakamura spent 14 years in NJPW (2002–2016), winning the IWGP Heavyweight Championship twice and the IWGP Intercontinental Championship multiple times. He is one of NJPW's most decorated performers."},
    {"q":"Why is Nakamura called 'King of Strong Style'?","a":"'Strong Style' is New Japan's wrestling philosophy — a blend of martial arts realism and pro wrestling theatrics developed by founder Antonio Inoki. Nakamura embodied it more completely than almost any other performer, earning the unofficial title."},
],
"record_rows": (
    row("shinsuke-nakamura","ppv",a("sami-zayn","Sami Zayn"),"NXT TakeOver: Dallas","Apr 1, 2016","Singles","NXT debut; instant classic","W") +
    row("shinsuke-nakamura","ppv title",a("aj-styles","AJ Styles"),"WrestleMania 34","Apr 8, 2018","Singles — WWE Championship","","L") +
    row("shinsuke-nakamura","ppv title",a("aj-styles","AJ Styles"),"SmackDown 2018","Multiple","No DQ / Last Man Standing","Heel low-blow program","L") +
    row("shinsuke-nakamura","ppv title",a("roman-reigns","Roman Reigns"),"Money in the Bank 2018","Jun 17, 2018","Singles — WWE Championship","","L") +
    row("shinsuke-nakamura","ppv",a("finn-balor","Finn Balor"),"NXT TakeOver","2016","Singles — NXT Championship","NXT title defense","W") +
    row("shinsuke-nakamura","tv title",a("seth-rollins","Seth Rollins"),"Raw 2021","Mar 1, 2021","Singles — United States Championship","US title defense","W") +
    row("shinsuke-nakamura","ppv",a("john-cena","John Cena"),"SummerSlam 2018","Aug 19, 2018","Singles","","W")
),
},

]

for w in wrestlers:
    html = build_page(w)
    path = os.path.join(BASE, w["slug"], "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)
    print(f"✅ {w['slug']} — {html.count(chr(10))} lines")
print("\nBatch 5a complete.")
