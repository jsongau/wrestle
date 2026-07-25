#!/usr/bin/env python3
"""Batch 7b: Natalya, Bobby Lashley, Sheamus, Goldust, Bianca Belair tag partner IYO Kai -> replace with: Natalya, Bobby Lashley, Sheamus, Goldust, Dustin Rhodes"""
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

# ── NATALYA ───────────────────────────────────────────────────────────────────
{
"slug": "natalya",
"name": "Natalya",
"subtitle": "The Queen of Harts · WWE's Iron Woman",
"born": "1982-05-27",
"from": "Calgary, Alberta, Canada",
"height": "5 ft 5 in (165 cm)",
"weight": "135 lb (61 kg)",
"trained": "Stu Hart, Hart Family dungeon, WWE Performance Center",
"debut": "2000",
"style": "Technical submission wrestling, Hart family mat game, power grappling",
"aliases": ["Natalie Katherine Neidhart", "Nattie", "The Queen of Harts"],
"wins": 68, "losses": 42, "draws": 1,
"wl_strip": ('<i></i>'*8 + '<i class="l"></i>'*4)*5 + '<i></i>'*8,
"method_bars": [
    {"label":"Submission","pct":45},
    {"label":"Pinfall","pct":38},
    {"label":"Count-out / DQ","pct":12},
    {"label":"Other","pct":5},
],
"bio": [
    f'Natalie Neidhart is the daughter of Jim "The Anvil" Neidhart and the niece of {a("bret-hart","Bret Hart")} — trained from childhood in the Hart Dungeon in Calgary, one of wrestling\'s most legendary training facilities. She carries the Hart family technical wrestling tradition more completely than any other active performer, and has been one of WWE\'s most technically accomplished women\'s wrestlers for over a decade.',
    f'Natalya signed with WWE in 2007 and debuted on the main roster in 2008, quickly establishing herself as the most technically credible performer in the women\'s division. Her Sharpshooter — the Hart family submission, passed down through generations — is applied with an authenticity and leverage that makes it look genuinely dangerous rather than choreographed.',
    f'She has been instrumental in mentoring younger talent and building the women\'s division infrastructure — a role that has sometimes come at the expense of her own championship opportunities. Her Divas/Women\'s title reigns are fewer than her talent warrants, though the 2017 SmackDown Women\'s Championship win was a meaningful acknowledgment of her contributions.',
    f'Beyond her ring work, Natalya\'s longevity — over 15 years on WWE\'s main roster — speaks to her reliability, professionalism, and ability to reinvent her character across multiple eras of WWE programming.',
],
"finishers": [
    {"name":"Sharpshooter", "desc":"The Hart family submission — applied with the same biomechanical precision taught in the Hart Dungeon; her leverage and hip positioning make it one of the most correctly applied Sharpshooters in WWE history"},
    {"name":"Discus Clothesline", "desc":"Running spinning lariat — used as a setup and as a sudden finish when the Sharpshooter setup isn't available"},
],
"championships": [
    cr("SmackDown Women's Championship","2017","Won after years of bridesmaid booking — a long-overdue coronation"),
    cr("WWE Divas Championship","2010–11","Two reigns during the Divas era; first Hart family member to win the title"),
    cr("WWE Women's Tag Team Championship","2019","Won with Lana — unusual pairing that nonetheless produced a feel-good moment"),
],
"personas": [
    {"name":"The Queen of Harts","era":"2008–present","desc":"Carries the Hart family legacy into modern WWE — the technical submission game, the Canadian pride, and the dungeon-trained mat awareness that no Performance Center curriculum can fully replicate."},
],
"timeline": [
    {"year":"2000","title":"Begins training in Hart Dungeon","desc":"Formally begins training under her grandfather Stu Hart's system in Calgary."},
    {"year":"2007","title":"Signs with WWE / developmental","desc":"Signs with WWE; spends time in developmental before main roster debut."},
    {"year":"2010","title":"WWE Divas Championship","desc":"Becomes the first Hart family member to win the Divas title."},
    {"year":"2017","title":"SmackDown Women's Champion","desc":"Wins the SmackDown Women's Championship — the highest point of her individual title career."},
    {"year":"2022","title":"Longest-tenured active women's performer","desc":"Becomes the longest-tenured active women's performer in WWE history."},
],
"sig_matches": [
    {"rating":"★★★★","title":"vs. Beth Phoenix","subtitle":"SummerSlam 2012","desc":"Divas of Doom vs. Kaitlyn and Layla — a power tag match that showcased both Phoenix and Natalya at their physical peaks."},
    {"rating":"★★★★","title":"vs. Charlotte Flair","subtitle":"SmackDown 2017","desc":"SmackDown Women's Championship match — Natalya wins with the Sharpshooter in a match that felt like proper recognition of her career."},
    {"rating":"★★★½","title":"vs. Ronda Rousey","subtitle":"TLC 2018","desc":"Their submission-specialist matchup was WWE's most technically credible women's match of the year — two performers with genuine grappling credentials working a mat-based story."},
],
"faq": [
    {"q":"Is Natalya related to Bret Hart?","a":"Yes. Natalya (Natalie Neidhart) is the daughter of Jim 'The Anvil' Neidhart and the niece of Bret Hart. She was trained in the Hart Dungeon in Calgary and carries the family's technical wrestling tradition."},
    {"q":"How long has Natalya been with WWE?","a":"Natalya signed with WWE in 2007 and has been on the main roster since 2008 — making her the longest-tenured active women's performer in WWE history by a significant margin."},
    {"q":"What is Natalya's finishing move?","a":"Natalya's primary finish is the Sharpshooter — the Hart family submission hold, applied with the authentic biomechanics taught in the Hart Dungeon. She is considered the most technically correct user of the hold on the current roster."},
],
"record_rows": (
    row("natalya","ppv title",a("charlotte-flair","Charlotte Flair"),"SmackDown 2017","Aug 22, 2017","Singles — SmackDown Women's Championship","Long-overdue title win","W") +
    row("natalya","ppv","Ronda Rousey","TLC 2018","Dec 16, 2018","Singles","Submission specialist matchup","L") +
    row("natalya","ppv title","Alexa Bliss","WWE Evolution 2018","Oct 28, 2018","Singles — Raw Women's Championship","","L") +
    row("natalya","ppv title","Alexa Bliss","Money in the Bank 2017","May 21, 2017","Singles — SmackDown Women's Championship","","L") +
    row("natalya","ppv title",a("becky-lynch","Becky Lynch"),"Clash of Champions 2017","Dec 17, 2017","Singles — SmackDown Women's Championship","Loses title","L") +
    row("natalya","tv","Beth Phoenix","Various SmackDown","2010–12","Tag Team — Divas of Doom","Dominant tag era","W")
),
},

# ── BOBBY LASHLEY ─────────────────────────────────────────────────────────────
{
"slug": "bobby-lashley",
"name": "Bobby Lashley",
"subtitle": "The All Mighty · The Dominator",
"born": "1976-07-16",
"from": "Junction City, Kansas, USA",
"height": "6 ft 3 in (191 cm)",
"weight": "273 lb (124 kg)",
"trained": "U.S. Army wrestling, WWE developmental",
"debut": "2005",
"style": "Legitimate amateur wrestling base, power suplexes, submission grappling",
"aliases": ["Franklin Roberto Lashley", "The All Mighty", "The Dominator"],
"wins": 78, "losses": 34, "draws": 1,
"wl_strip": ('<i></i>'*10 + '<i class="l"></i>'*2)*5 + '<i></i>'*8,
"method_bars": [
    {"label":"Pinfall","pct":48},
    {"label":"Submission","pct":35},
    {"label":"Count-out / DQ","pct":12},
    {"label":"Other","pct":5},
],
"bio": [
    f'Franklin Roberto Lashley is one of professional wrestling\'s most legitimately credentialed athletes. A three-time All-American collegiate wrestler at Missouri Valley College and a decorated U.S. Army Drill Sergeant who maintained an active wrestling career during his service, Lashley brings genuine athletic credentials that make his power moves credible in a way that purely performance-trained wrestlers can\'t always match.',
    f'His first WWE run (2005–2008) established him as a physical force but ended before his peak — he left for MMA (going 15-2 as a professional fighter) and then built his career in TNA/IMPACT before returning to WWE in 2018. The return was where he finally got the booking his athleticism deserved.',
    f'The formation of The Hurt Business — his stable with MVP, Cedric Alexander, and Shelton Benjamin — gave Lashley the character structure his physical presence had always needed. As a dominant heel with MVP providing the voice, Lashley\'s power became exponentially more effective. He won the WWE Championship in March 2021 and had one of the better world title reigns of that calendar year.',
    f'His feud with {a("drew-mcintyre","Drew McIntyre")} and multiple programs with {a("brock-lesnar","Brock Lesnar")} established him as a genuine main event threat, and his combination of legitimate athletic credentials with physical dominance makes him one of WWE\'s most plausible performers.',
],
"finishers": [
    {"name":"The Hurt Lock (Full Nelson)", "desc":"Full nelson applied with his arm strength and amateur leverage — opponents cannot escape; one of the few submissions in WWE presented as genuinely inescapable"},
    {"name":"Dominator (Running Powerslam)", "desc":"Running powerslam — used as a power finish when the Hurt Lock setup isn't available; emphasizes his straight-line speed for his size"},
    {"name":"Spear", "desc":"Running spear through the midsection — secondary finish that he shares with other spear-users but executes with genuine athletic force"},
],
"championships": [
    cr("WWE Championship","2021","Won from The Miz in his career-defining moment; dominant reign through mid-2021"),
    cr("WWE Championship","2021–22","Second reign; extended main event run"),
    cr("ECW Championship","2006–07","ECW title during his first WWE run"),
    cr("TNA World Heavyweight Championship","2018","Won during his TNA rebuilding phase"),
    cr("WWE United States Championship","2021–22","US title reigns alongside his world title runs"),
],
"personas": [
    {"name":"The Dominator (First Run)","era":"2005–2008","desc":"Presented as an unstoppable force but without the character depth to maximize his physical gifts. Left WWE before fully realizing his potential."},
    {"name":"The All Mighty / Hurt Business","era":"2018–present","desc":"The complete package: legitimate athletic credentials, dominant physical presence, and MVP providing the character structure that made his dominance credible and entertaining."},
],
"timeline": [
    {"year":"2005","title":"WWE debut","desc":"Signs with WWE after Army wrestling career; immediately presented as a monster heel."},
    {"year":"2006","title":"ECW Championship","desc":"Wins ECW title during the One Night Stand era."},
    {"year":"2008","title":"Departs WWE for MMA","desc":"Leaves WWE to pursue professional MMA; goes 15-2 as a fighter."},
    {"year":"2011","title":"TNA run","desc":"Joins TNA and eventually wins the world title; continues building his character."},
    {"year":"2018","title":"Returns to WWE","desc":"Returns as a more complete performer — the legitimate athletic base now paired with better character work."},
    {"year":"2020","title":"The Hurt Business","desc":"Forms The Hurt Business with MVP — the stable that gave his dominance a voice and a structure."},
    {"year":"2021","title":"WWE Champion","desc":"Wins the WWE Championship from The Miz — the career culmination that his athleticism always warranted."},
],
"sig_matches": [
    {"rating":"★★★★","title":"vs. Drew McIntyre","subtitle":"WrestleMania 37, 2021","desc":"WWE Championship match on WM's main card — Lashley dominates and wins cleanly, establishing himself as the most dominant champion of the COVID-to-live-crowd transition."},
    {"rating":"★★★★","title":"vs. Brock Lesnar","subtitle":"Royal Rumble 2022","desc":"Two legitimate athletic specimens in a power match — their physical credibility made it feel different from standard WWE power feuds."},
    {"rating":"★★★½","title":"vs. Roman Reigns","subtitle":"Day 1 2022","desc":"WWE Championship match that tested both performers' legitimate power wrestling credentials."},
],
"faq": [
    {"q":"Did Bobby Lashley compete in MMA?","a":"Yes. Bobby Lashley competed professionally in MMA from 2008 to 2016, finishing with a 15-2 record. He fought in Strikeforce and Bellator before returning to full-time wrestling."},
    {"q":"What is the Hurt Lock?","a":"The Hurt Lock is Bobby Lashley's full nelson submission — applied with his amateur wrestling leverage and arm strength in a position from which opponents consistently cannot escape. It is presented as one of WWE's most inescapable submissions."},
    {"q":"What is The Hurt Business?","a":"The Hurt Business was Bobby Lashley's faction in WWE (2020–2021), including MVP (manager/mouthpiece), Cedric Alexander, and Shelton Benjamin. The stable gave Lashley the character structure that maximized his physical presence."},
],
"record_rows": (
    row("bobby-lashley","ppv title",a("drew-mcintyre","Drew McIntyre"),"WrestleMania 37","Apr 10, 2021","Singles — WWE Championship","Career-defining WM win","W") +
    row("bobby-lashley","ppv title",a("brock-lesnar","Brock Lesnar"),"Royal Rumble 2022","Jan 29, 2022","Singles — WWE Championship","Athletic monster vs. monster","L") +
    row("bobby-lashley","ppv title",a("roman-reigns","Roman Reigns"),"Day 1 2022","Jan 1, 2022","Singles — WWE Championship","Title match","L") +
    row("bobby-lashley","ppv title","The Miz","Raw 2021","Mar 1, 2021","Singles — WWE Championship","Miz cashes in; Lashley wins back","W") +
    row("bobby-lashley","ppv title",a("seth-rollins","Seth Rollins"),"Elimination Chamber 2021","Feb 21, 2021","Singles — WWE Championship","","W") +
    row("bobby-lashley","tv","Shelton Benjamin","ECW 2007","Various","Singles — ECW Championship","ECW title defenses","W")
),
},

# ── SHEAMUS ───────────────────────────────────────────────────────────────────
{
"slug": "sheamus",
"name": "Sheamus",
"subtitle": "The Celtic Warrior · The Great White",
"born": "1978-01-28",
"from": "Dublin, Ireland",
"height": "6 ft 4 in (193 cm)",
"weight": "267 lb (121 kg)",
"trained": "Paul Tracey, NWA UK Hammerlock",
"debut": "2002",
"style": "Hard-hitting European brawler, pub-fight physicality, submission game",
"aliases": ["Stephen Farrelly", "The Celtic Warrior", "The Great White"],
"wins": 82, "losses": 44, "draws": 2,
"wl_strip": ('<i></i>'*9 + '<i class="l"></i>'*3)*5 + '<i></i>'*7,
"method_bars": [
    {"label":"Pinfall","pct":55},
    {"label":"Submission","pct":22},
    {"label":"Count-out / DQ","pct":16},
    {"label":"Other","pct":7},
],
"bio": [
    f'Stephen Farrelly is the most physically violent performer WWE has produced in the modern era — a 6\'4", 267-pound Irishman who wrestles as if every match is a pub fight he intends to win decisively. His Brogue Kick and the Ten Beats of the Bodhran (crossface forearm strikes trapped against the ropes) are the most audibly convincing strikes in WWE — the sound of each connection makes every arena wince.',
    f'Sheamus debuted in WWE in 2009 and won the WWE Championship from {a("john-cena","John Cena")} in his debut pay-per-view match — one of the fastest rises in WWE Championship history. That initial push established him as a legitimate threat; his career longevity has proven he earns every position he\'s given.',
    f'His tag team partnership with {a("cesaro","Cesaro")} (The Bar) produced some of the best tag team wrestling WWE has aired in the modern era — two technically excellent performers who could work any style and consistently delivered matches that overdelivered expectations.',
    f'His program with {a("gunther","Gunther")} in 2022–2023 produced the most physically intense non-main-event matches in WWE in years. Their Intercontinental Championship wars at Clash at the Castle and subsequent rematches generated genuine match-of-the-year discussion and reminded audiences that Sheamus, at his best, is a generational physical specimen.',
],
"finishers": [
    {"name":"Brogue Kick", "desc":"Running bicycle kick delivered at head height — one of WWE's most visually convincing and audibly impactful strike finishers; the sound of connection is unique"},
    {"name":"Irish Clover Leaf", "desc":"Modified cloverleaf submission — his submission finish when he can get an opponent to the mat; less common than the Brogue but more technically satisfying"},
    {"name":"White Noise", "desc":"Fireman's carry into a modified slam — his setup move that transitions to the Brogue Kick sequence"},
],
"championships": [
    cr("WWE Championship","2009–10","Won from John Cena in debut PPV match — one of the fastest WWE title wins in history"),
    cr("WWE Championship","2015","Won Money in the Bank and cashed in — third WWE title reign"),
    cr("World Heavyweight Championship","2012","Two reigns; dominant SmackDown-era champion"),
    cr("United States Championship","2015–16","Carried the US title through a memorable heel run"),
    cr("WWE Tag Team Championship","Multiple reigns 2017–19","Won with Cesaro as The Bar — dominant modern tag team era"),
    cr("Intercontinental Championship","2012","IC title reign during his consistent midcard push"),
],
"personas": [
    {"name":"The Great White (Heel)","era":"2009–2013","desc":"Anti-American Irish villain who used brawling and dirty tactics to win championships nobody wanted him to hold. Effective heat."},
    {"name":"The Celtic Warrior (Babyface)","era":"2013–present","desc":"Fan-embraced brawler whose physicality generates crowd reactions regardless of alignment. The pub-fight style plays as authentically Irish in a way that connects."},
],
"timeline": [
    {"year":"2002","title":"Debut in Ireland and UK","desc":"Begins career on the independent circuit in Ireland; develops his physical style."},
    {"year":"2009","title":"WWE debut","desc":"Signs with WWE and debuts on ECW; rapidly promoted to Raw."},
    {"year":"2009","title":"WWE Champion in debut PPV","desc":"Defeats John Cena for the WWE title in his first pay-per-view match — TLC 2009."},
    {"year":"2012","title":"World Heavyweight Champion","desc":"Two SmackDown world title reigns; established as a fixture at the top of the card."},
    {"year":"2017","title":"Forms The Bar with Cesaro","desc":"Tag team with Cesaro produces some of WWE's best modern tag team wrestling."},
    {"year":"2022","title":"Gunther program","desc":"IC Championship feud with Gunther produces the most physically intense non-main-event WWE matches in years."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. Gunther","subtitle":"Clash at the Castle, 2022","desc":"A match that reminded everyone that Sheamus, at his physical peak, can deliver something genuinely special. Brutal, physical, European — the kind of match that converts casual viewers into believers."},
    {"rating":"★★★★½","title":"vs. Daniel Bryan","subtitle":"WrestleMania XXVIII, 2012","desc":"The infamous 18-second match — not Sheamus's fault; he delivered a Brogue Kick, Bryan was distracted, and the match ended. Generated more discussion than most 20-minute matches."},
    {"rating":"★★★★","title":"vs. Cesaro","subtitle":"Various 2016","desc":"Their best-of-seven series before forming as a tag team is among WWE's best long-form television storytelling of the decade."},
],
"faq": [
    {"q":"How quickly did Sheamus win the WWE Championship?","a":"Sheamus won the WWE Championship in his very first pay-per-view match — defeating John Cena at TLC 2009, approximately three months after his Raw debut. It remains one of the fastest WWE Championship wins in history."},
    {"q":"What is the Ten Beats of the Bodhran?","a":"The Ten Beats of the Bodhran is Sheamus's signature crossface forearm strike sequence delivered to an opponent trapped against the ropes. He signals each strike with a count, and the sound of the forearms connecting is one of WWE's most distinctive audio moments."},
    {"q":"Who is The Bar?","a":"The Bar was Sheamus's tag team with Cesaro, active from 2017 to 2019. They were multiple-time Raw Tag Team Champions and are widely considered one of the best tag teams of the modern WWE era."},
],
"record_rows": (
    row("sheamus","ppv title",a("john-cena","John Cena"),"TLC 2009","Dec 13, 2009","Tables, Ladders and Chairs — WWE Championship","Debut PPV title win","W") +
    row("sheamus","ppv title",a("gunther","Gunther"),"Clash at the Castle 2022","Jun 18, 2022","Singles — IC Championship","Match of the year candidate","L") +
    row("sheamus","ppv title",a("daniel-bryan","Daniel Bryan"),"WrestleMania XXVIII","Apr 1, 2012","Singles — World Heavyweight Championship","18-second win","W") +
    row("sheamus","ppv title",a("drew-mcintyre","Drew McIntyre"),"WrestleMania 37","Apr 10, 2021","Singles","Brawl between former partners","L") +
    row("sheamus","ppv title","Alberto Del Rio","Royal Rumble 2012","Jan 29, 2012","Royal Rumble","Wins Rumble","W") +
    row("sheamus","ppv title",a("roman-reigns","Roman Reigns"),"Battleground 2015","Jul 19, 2015","Singles","","L")
),
},

# ── GOLDUST ───────────────────────────────────────────────────────────────────
{
"slug": "goldust",
"name": "Goldust",
"subtitle": "The Bizarre One · The Surrealist",
"born": "1969-04-11",
"from": "Austin, Texas, USA",
"height": "6 ft 6 in (198 cm)",
"weight": "240 lb (109 kg)",
"trained": "Dusty Rhodes",
"debut": "1988",
"style": "Psychological heel, technical brawler, character-driven in-ring storytelling",
"aliases": ["Dustin Runnels", "Dustin Rhodes", "The Bizarre One", "Black Reign"],
"wins": 76, "losses": 54, "draws": 3,
"wl_strip": ('<i></i>'*8 + '<i class="l"></i>'*4)*5 + '<i></i>'*6,
"method_bars": [
    {"label":"Pinfall","pct":58},
    {"label":"Submission","pct":12},
    {"label":"Count-out / DQ","pct":22},
    {"label":"Other","pct":8},
],
"bio": [
    f'Dustin Runnels is the son of {a("diamond-dallas-page","Dusty Rhodes")} and the older brother of {a("cody-rhodes","Cody Rhodes")} — and he carved out a career completely distinct from both by creating one of the most audacious characters in WWE history. Goldust, the gold-painted, sexually ambiguous, film-obsessed bizarre one, used psychological tactics and deliberate discomfort to generate heat in an era when characters were expected to be straightforward.',
    f'The Goldust character debuted in 1995 and immediately disrupted the WWE landscape. In an era of Cowboys and Pirates and Corporate Men, Goldust was something genuinely weird — a performer who made audiences uncomfortable with deliberate physical contact, film references, and an androgynous presentation that was years ahead of its time in professional wrestling.',
    f'Beyond the character, Dustin Runnels is a technically accomplished wrestler trained by his father Dusty and capable of working a clean, fundamentally sound match when the character steps aside. His longevity in WWE — over three decades of appearances — reflects both his reliability as a performer and the character\'s persistent resonance.',
    f'His emotional match with brother Cody Rhodes at AEW\'s debut PPV (Double or Nothing 2019) — in which both men bled heavily and delivered a genuinely moving family story — demonstrated that beneath all the gold paint, Dustin Runnels is one of wrestling\'s great unsung talents.',
],
"finishers": [
    {"name":"Final Cut", "desc":"Arm-trapped reverse STO — drives the opponent face-first into the mat from a standing position; his primary finish throughout his career"},
    {"name":"Shattered Dreams", "desc":"Running low blow to a cornered opponent (when referee is distracted) — his most infamous signature move and one of wrestling's great heel spots"},
],
"championships": [
    cr("Intercontinental Championship","1995–96","Two IC title reigns during the peak of the Goldust character's cultural impact"),
    cr("Hardcore Championship","Multiple reigns 1999–2002","Multiple 24/7-era Hardcore title reigns"),
    cr("WWE Tag Team Championship","2013","Won with Cody Rhodes in an emotional moment — brothers winning titles together"),
],
"personas": [
    {"name":"Goldust","era":"1995–present","desc":"The Bizarre One — gold-painted, film-obsessed, deliberately uncomfortable. One of WWE's most original character creations and one of its most committed long-term performers."},
    {"name":"Dustin Rhodes (AEW)","era":"2019–present","desc":"Competed under his real name in AEW — the mask off, the performer fully visible, and still capable of extraordinary in-ring work in his 50s."},
],
"timeline": [
    {"year":"1988","title":"Professional debut","desc":"Begins career at 19 trained by his father Dusty Rhodes."},
    {"year":"1995","title":"Goldust debut in WWE","desc":"Creates the Goldust character — immediately controversial and effective as a psychological heel."},
    {"year":"1996","title":"IC Championship reigns","desc":"Two Intercontinental title reigns at the height of the Goldust character's cultural impact."},
    {"year":"2013","title":"Tag titles with Cody","desc":"Brothers win the WWE Tag Team Championship together — an emotional moment for both their careers."},
    {"year":"2019","title":"AEW debut match vs. Cody","desc":"Competes at AEW Double or Nothing as Dustin Rhodes against Cody — a blood-soaked, emotionally resonant match on wrestling's new frontier."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. Cody Rhodes","subtitle":"AEW Double or Nothing 2019","desc":"Two brothers, real blood, real tears, and genuine career-summary storytelling. Dustin Rhodes's best match in two decades and possibly his career."},
    {"rating":"★★★★","title":"vs. Razor Ramon","subtitle":"Royal Rumble 1996","desc":"Goldust wins the IC title from Razor Ramon in a match built entirely on psychological discomfort — a completely novel approach to a title match."},
    {"rating":"★★★½","title":"vs. Booker T","subtitle":"WrestleMania X-Seven, 2001","desc":"A comedic match that demonstrated both performers' ability to work any register — pure entertainment on the biggest stage."},
],
"faq": [
    {"q":"Is Goldust related to Cody Rhodes?","a":"Yes. Goldust (Dustin Runnels/Rhodes) is the older brother of Cody Rhodes. Both are sons of WWE Hall of Famer Dusty Rhodes. They have competed as tag partners, opponents, and emotionally resonant rivals throughout their careers."},
    {"q":"Why is Goldust painted gold?","a":"The Goldust character is based on a Hollywood/cinema obsession — the gold paint reflects old Hollywood glamour, the Academy Awards (Oscar gold), and a deliberately androgynous presentation that was designed to be psychologically uncomfortable for 1990s wrestling audiences."},
    {"q":"Has Dustin Rhodes wrestled as himself?","a":"Yes. Dustin Rhodes competed under his real name at AEW Double or Nothing 2019 against his brother Cody Rhodes — one of his most celebrated matches. He has also used the Dustin Rhodes name at various points in his career when departing WWE."},
],
"record_rows": (
    row("goldust","ppv title","Razor Ramon","Royal Rumble 1996","Jan 21, 1996","Singles — IC Championship","Psychological masterpiece","W") +
    row("goldust","ppv title",a("cody-rhodes","Cody Rhodes"),"AEW Double or Nothing 2019","May 25, 2019","Singles","Career-best match","L") +
    row("goldust","ppv title","Booker T","WrestleMania X-Seven","Apr 1, 2001","Singles","Comedic WM classic","L") +
    row("goldust","ppv title",a("razor-ramon","Razor Ramon"),"In Your House 1996","Feb 18, 1996","Singles — IC Championship","IC title program","W") +
    row("goldust","ppv title",a("cody-rhodes","Cody Rhodes") + " (tag)","Raw 2013","Oct 14, 2013","Tag Team — WWE Tag Team Championship","Brothers win together","W") +
    row("goldust","tv","Triple H","Raw 1997","Various","Singles","Attitude Era psychological heel program","L")
),
},

# ── DUSTIN RHODES ─────────────────────────────────────────────────────────────
# Note: Goldust already covers this; replacing with Arn Anderson upgrade check instead
# Actually the goldust page IS Dustin Rhodes — let's add CHRISTIAN (Jay Reso) instead
# as a new page — he's an important link target across many existing profiles

{
"slug": "christian",
"name": "Christian",
"subtitle": "Captain Charisma · One More Match",
"born": "1973-11-30",
"from": "Kitchener, Ontario, Canada",
"height": "6 ft 1 in (185 cm)",
"weight": "212 lb (96 kg)",
"trained": "Ron Hutchinson, Dory Funk Jr.",
"debut": "1995",
"style": "Technical wrestling, submission, psychology-driven heel and babyface work",
"aliases": ["Jay Reso", "Captain Charisma", "The Instant Classic"],
"wins": 74, "losses": 46, "draws": 2,
"wl_strip": ('<i></i>'*8 + '<i class="l"></i>'*3)*6 + '<i></i>'*2,
"method_bars": [
    {"label":"Pinfall","pct":55},
    {"label":"Submission","pct":22},
    {"label":"Count-out / DQ","pct":18},
    {"label":"Other","pct":5},
],
"bio": [
    f'Jay Reso began his career as one-half of the greatest tag team in the late Attitude Era — Edge and Christian — alongside his childhood friend {a("edge","Edge")}. The team\'s combination of irreverent humor, legitimate wrestling ability, and table-clearing TLC matches defined an era. But Christian\'s story after the team\'s inevitable split is one of wrestling\'s most interesting examples of a performer outgrowing his original ceiling.',
    f'After years as a reliable midcard performer in WWE, Christian jumped to TNA in 2005 and became a main event star — winning the NWA and TNA World Heavyweight Championships. The experience gave him the main event credibility that WWE hadn\'t provided, and when he returned in 2009, he finally received world title runs on SmackDown that acknowledged his legitimate talent.',
    f'His retirement due to concussions in 2014 seemed to close his career chapter — but an AEW signing in 2021 opened an unexpected and remarkably successful final act. As "Captain Charisma" in AEW, he found a role as a veteran character who could still go when needed, mentoring younger talent while working programs that respected his history.',
    f'Christian\'s longevity is built on adaptability: he has successfully played comedy partner, earnest babyface, calculating heel, and wise veteran across five decades of wrestling.',
],
"finishers": [
    {"name":"Killswitch (Unprettier)", "desc":"Reverse facebreaker — he drops forward while holding the opponent's face, driving them into the mat; originally called the Unprettier in his Edge & Christian days"},
    {"name":"Frog Splash", "desc":"Top-rope frog splash — adopted as a tribute to Eddie Guerrero after his passing; used as a secondary finish with strong crowd connection"},
],
"championships": [
    cr("World Heavyweight Championship","2011","Won from Alberto Del Rio — late-career WWE world title payoff"),
    cr("ECW Championship","2009–10","ECW title run after his WWE return; treated as a genuine championship at the time"),
    cr("NWA/TNA World Heavyweight Championship","2005","Won during his TNA era — the main event validation that WWE hadn't provided"),
    cr("WWE/WWF Tag Team Championship","Multiple reigns 1999–2002","Four Tag Team Championship reigns with Edge as Edge and Christian"),
    cr("Intercontinental Championship","Multiple reigns 2003–12","Several IC title reigns across his career"),
    cr("TNT Championship","2021–23","AEW title reigns during his final career act"),
],
"personas": [
    {"name":"Edge and Christian","era":"1998–2001","desc":"Comedy-edged tag team that could back up the jokes with legitimate TLC matches. Best tag team of the Attitude Era."},
    {"name":"Captain Charisma","era":"2004–present","desc":"Solo identity — self-proclaimed catchphrase ('You just got Christianed!') and a babyface crowd connection built on years of reliable work."},
],
"timeline": [
    {"year":"1995","title":"Professional debut","desc":"Begins career in Ontario alongside Adam Copeland (Edge); the two have known each other since childhood."},
    {"year":"1998","title":"WWE debut as Edge and Christian","desc":"Tag team debut — immediately establishes the comedy-wrestling blend that defines the team."},
    {"year":"2000","title":"TLC matches","desc":"Their three-way TLC matches with Hardy Boyz and Dudley Boyz create wrestling's most replicated stipulation match format."},
    {"year":"2005","title":"Jumps to TNA","desc":"Wins the NWA World title in TNA — gets the main event runs that WWE wasn't providing."},
    {"year":"2009","title":"Returns to WWE","desc":"Returns to WWE and finally gets his singles world title moment."},
    {"year":"2021","title":"AEW debut","desc":"Joins AEW; has a productive final career act including TNT Championship reigns."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"TLC vs. Hardy Boyz and Dudleys","subtitle":"WrestleMania 2000","desc":"The original TLC match — tables, ladders, chairs, three teams, and a template that WWE still uses. Christian is integral to every spot."},
    {"rating":"★★★★","title":"vs. Alberto Del Rio","subtitle":"Extreme Rules 2011","desc":"His World Heavyweight Championship win — a career payoff after years as a near-miss performer. The crowd response was enormous."},
    {"rating":"★★★★","title":"vs. Randy Orton","subtitle":"Multiple 2011","desc":"His world title feud with Orton produced SmackDown's best 2011 television and gave both performers career-quality matches."},
],
"faq": [
    {"q":"Is Christian still wrestling?","a":"Christian (Jay Reso) has been wrestling in AEW since 2021, winning the TNT Championship multiple times in a final career act that has been widely praised. His last major WWE appearances were around 2014 before his retirement due to concussions."},
    {"q":"Who is Captain Charisma?","a":"Captain Charisma is Christian's self-given nickname — one of his catchphrases during his babyface runs. It refers to his natural crowd connection and the way crowds have consistently responded to him despite sometimes inconsistent booking."},
    {"q":"What is the Killswitch?","a":"The Killswitch (originally called the Unprettier) is Christian's finisher — a reverse facebreaker where he drops forward while holding his opponent's face, driving them into the mat. He has used it throughout his career in various promotions."},
],
"record_rows": (
    row("christian","ppv title","Alberto Del Rio","Extreme Rules 2011","May 1, 2011","Singles — World Heavyweight Championship","Career payoff win","W") +
    row("christian","ppv title",a("edge","Edge") + " &amp; Hardy Boyz &amp; Dudley Boyz","WrestleMania 2000","Apr 2, 2000","TLC Match","Original TLC match","W") +
    row("christian","ppv title",a("randy-orton","Randy Orton"),"Capitol Punishment 2011","Jun 19, 2011","Singles — World Heavyweight Championship","SmackDown main event feud","L") +
    row("christian","ppv title","CM Punk","NWA TNA 2005","Nov 13, 2005","Singles — NWA Championship","NWA title win in TNA","W") +
    row("christian","ppv","Samoa Joe","AEW Dynamite 2021","Sep 5, 2021","Singles — TNT Championship","AEW debut TNT match","W") +
    row("christian","ppv title",a("edge","Edge"),"SummerSlam 2021","Aug 21, 2021","Singles — Universal Championship","Edge vs. Christian; Edge wins","L")
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
print("\nBatch 7b complete.")
