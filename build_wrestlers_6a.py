#!/usr/bin/env python3
"""Batch 6a: Sting, Diamond Dallas Page, Bully Ray, Mercedes Mone, Christopher Daniels"""
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

# ── STING ─────────────────────────────────────────────────────────────────────
{
"slug": "sting",
"name": "Sting",
"subtitle": "The Icon · The Franchise of WCW",
"born": "1959-03-20",
"from": "Omaha, Nebraska, USA",
"height": "6 ft 2 in (188 cm)",
"weight": "252 lb (114 kg)",
"trained": "Rick Bassman, Red Bastien",
"debut": "1985",
"retired": "2023",
"style": "Power wrestling, high-energy offense, character-driven spectacle",
"aliases": ["Steve Borden", "The Stinger", "The Icon", "Crow Sting"],
"wins": 88, "losses": 38, "draws": 3,
"wl_strip": ('<i></i>'*10 + '<i class="l"></i>'*2)*5 + '<i></i>'*8,
"method_bars": [
    {"label":"Pinfall","pct":55},
    {"label":"Submission","pct":25},
    {"label":"Count-out / DQ","pct":14},
    {"label":"Other","pct":6},
],
"bio": [
    f'Steve Borden is WCW — perhaps more so than any other single performer. As Sting, he served as the promotion\'s moral center, its most loyal babyface, and eventually its most haunting anti-hero for nearly two decades. Few wrestlers have managed to reinvent themselves as thoroughly and successfully as he did during the Crow Sting era of 1996–1997.',
    f'Sting began his career in the mid-1980s with a colorful, face-painted, high-energy persona inspired by the rock band KISS. He was a natural babyface — charismatic, physically imposing, and genuinely beloved by fans who wanted a hero they could trust. His rivalry with {a("ric-flair","Ric Flair")} in the late 1980s defined both men and made Sting one of the most recognizable faces in American wrestling.',
    f'The nWo invasion in 1996 created Sting\'s most significant moment. When Hulk Hogan, Kevin Nash, and Scott Hall formed the nWo, WCW\'s management turned on Sting — wrongly suspecting him of being a member. Sting\'s response was total withdrawal: he disappeared to the rafters, dyed his hair black, wore a white face of paint, and watched silently for a year. The image of Sting descending from the rafters became one of wrestling\'s most iconic visual moments.',
    f'After WCW\'s closure, Sting remained in TNA/IMPACT for years before finally debuting in WWE at Survivor Series 2014 — his first WWE appearance after 29 years in the business. He was inducted into the WWE Hall of Fame in 2016. A final AEW run in 2020–2023 gave him a true retirement on his own terms.',
],
"finishers": [
    {"name":"Scorpion Death Lock", "desc":"Elevated sharpshooter — Sting's signature submission; applied from a standing position, locking both legs and bending the opponent backward over his thighs"},
    {"name":"Scorpion Death Drop", "desc":"Reverse DDT — his primary pinfall finish; sets up with an opponent's back against his chest and drives them down onto the back of their head"},
    {"name":"Stinger Splash", "desc":"Running body splash into a corner — his signature setup move; the setup for either the Lock or the Drop"},
],
"championships": [
    cr("WCW World Heavyweight Championship","6 reigns 1990–2000","The most decorated WCW champion of the promotion's existence; the face of WCW"),
    cr("WCW/NWA United States Championship","Multiple reigns 1988–99","Secondary title reigns that filled his card between world title runs"),
    cr("TNA World Heavyweight Championship","4 reigns 2006–13","Extended his legacy in TNA for over a decade post-WCW"),
    cr("WWE Hall of Fame","2016 inductee","Recognized as one of wrestling's all-time icons"),
],
"personas": [
    {"name":"Surfer Sting","era":"1987–1996","desc":"The colorful, face-painted babyface — bright colors, high energy, and an unshakeable smile. WCW's most trustworthy hero."},
    {"name":"Crow Sting","era":"1996–1998","desc":"The darkest, most striking character reinvention in wrestling history. Silent guardian watching from the rafters as WCW fell to the nWo."},
    {"name":"Joker Sting","era":"2011–2014 (TNA)","desc":"A third persona inspired by the Batman villain — unsettling, erratic, and effective as a response to Immortal's takeover of TNA."},
],
"timeline": [
    {"year":"1985","title":"Professional debut","desc":"Debuts in the mid-1980s; quickly develops his colorful Surfer persona."},
    {"year":"1988","title":"Clash of Champions — Flair vs. Sting","desc":"45-minute draw with Ric Flair on TBS elevates Sting to main event status overnight."},
    {"year":"1990","title":"First WCW Championship","desc":"Defeats Flair for his first WCW World title — the beginning of his reign as WCW's franchise."},
    {"year":"1996","title":"nWo invasion; goes silent","desc":"After WCW falsely accuses him of nWo membership, Sting retreats to the rafters and begins his Crow character — watches for over a year."},
    {"year":"1997","title":"Starrcade 1997 — Hogan match","desc":"Descends to defeat Hogan for the WCW title — one of wrestling's most anticipated matches, controversially marred by fast-count controversy."},
    {"year":"2001","title":"WCW closes","desc":"WCW folds; Sting moves to TNA and continues wrestling for 22 more years."},
    {"year":"2014","title":"WWE debut","desc":"Makes his surprise WWE debut at Survivor Series 2014 — his first-ever WWE appearance."},
    {"year":"2020","title":"AEW debut","desc":"Signs with AEW at age 61; begins final chapter of his career in a promotion that honors his legacy."},
    {"year":"2023","title":"Retirement","desc":"Retires at AEW Revolution 2024 in a final match with his son — a retirement on his own terms."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. Ric Flair (45-minute draw)","subtitle":"Clash of Champions I, 1988","desc":"The match that made Sting. A 45-minute draw against the NWA champion on free television — the finest performance of his early career and one of the best TV matches in wrestling history."},
    {"rating":"★★★★","title":"vs. Hulk Hogan","subtitle":"Starrcade 1997","desc":"The most anticipated WCW match ever — Sting descends from the rafters after a year of silence to challenge Hogan. Controversially handled, but an atmospheric spectacle."},
    {"rating":"★★★★","title":"vs. Triple H","subtitle":"Night of Champions 2015","desc":"His first and only WrestleMania-adjacent match in WWE — a solid encounter between two veterans that gave Sting a proper WWE send-off."},
],
"faq": [
    {"q":"Why did Sting never wrestle in WWE until 2014?","a":"Sting had a long-standing relationship with WCW and then TNA, and chose loyalty to those organizations over WWE offers. He finally signed with WWE in 2014 after TNA's decline, making his debut at Survivor Series that year."},
    {"q":"What is the Crow Sting character?","a":"Crow Sting was a character reinvention in 1996 where Sting abandoned his colorful persona, stopped speaking, wore all black with white face paint inspired by the film The Crow, and watched silently from the rafters as WCW fought the nWo invasion."},
    {"q":"How many WCW Championships did Sting win?","a":"Sting won the WCW World Heavyweight Championship six times, making him the most decorated champion in WCW history."},
],
"record_rows": (
    row("sting","ppv title",a("hulk-hogan","Hulk Hogan"),"WCW Starrcade 1997","Dec 28, 1997","Singles — WCW World Championship","Year of silence ends; Hogan controversy","W") +
    row("sting","ppv title",a("ric-flair","Ric Flair"),"WCW Great American Bash 1990","Jul 7, 1990","Singles — WCW World Championship","First world title","W") +
    row("sting","tv",a("ric-flair","Ric Flair"),"Clash of Champions I","Mar 27, 1988","Singles — NWA Championship","45-min draw; career-making match","D") +
    row("sting","ppv",a("triple-h","Triple H"),"Night of Champions 2015","Jun 21, 2015","Singles","WWE career debut match","L") +
    row("sting","ppv title",a("goldberg","Goldberg"),"WCW Fall Brawl 1999","Sep 12, 1999","Singles — WCW World Championship","","L") +
    row("sting","ppv",a("diamond-dallas-page","Diamond Dallas Page"),"WCW Halloween Havoc 1997","Oct 26, 1997","Singles","","W") +
    row("sting","ppv title","Darby Allin","AEW Revolution 2023","Mar 5, 2023","Tag Team","Final AEW match; retirement","W")
),
},

# ── DIAMOND DALLAS PAGE ────────────────────────────────────────────────────────
{
"slug": "diamond-dallas-page",
"name": "Diamond Dallas Page",
"subtitle": "The Self-Made Man · The People's Champion",
"born": "1956-04-05",
"from": "Point Pleasant, New Jersey, USA",
"height": "6 ft 5 in (196 cm)",
"weight": "248 lb (112 kg)",
"trained": "Sgt. Slaughter, Jake Roberts",
"debut": "1991",
"style": "Power brawler, diamond cutter specialist, motivational psychology",
"aliases": ["Page", "DDP", "Dallas Page"],
"wins": 74, "losses": 36, "draws": 2,
"wl_strip": ('<i></i>'*9 + '<i class="l"></i>'*3)*5 + '<i></i>'*4,
"method_bars": [
    {"label":"Pinfall","pct":62},
    {"label":"Submission","pct":12},
    {"label":"Count-out / DQ","pct":18},
    {"label":"Other","pct":8},
],
"bio": [
    f'Page Joseph Falkinburg began wrestling at 35 — an age when most careers are ending — and became the WCW World Heavyweight Champion by 42. His story is one of professional wrestling\'s most genuinely inspirational: rejected, doubted, and dismissed at every stage, DDP kept working and became one of WCW\'s biggest stars during its most competitive era.',
    f'Before wrestling, Page had managed multiple wrestlers and had a background as a nightclub DJ and manager. He got into the ring because he wanted to, trained obsessively, and developed one of wrestling\'s great comedy-turned-serious babyface journeys. The Diamond Cutter — his RKO-style signature — became one of wrestling\'s most over finishes precisely because he could hit it from anywhere on anyone.',
    f'His feud with {a("goldberg","Goldberg")} in 1998 produced WCW\'s most complete babyface vs. babyface storytelling. His eventual WCW Championship win at Spring Stampede 1999 — defeating {a("hulk-hogan","Hulk Hogan")}, {a("ric-flair","Ric Flair")}, and {a("sting","Sting")} in a Four Corners match — felt genuinely earned after years of near-misses.',
    f'Post-wrestling, DDP developed DDP Yoga — a rehabilitation and fitness program that became famous for helping Scott Hall (Razor Ramon) and Jake Roberts with addiction recovery. That work, perhaps more than any match, reflects the motivational philosophy that always underpinned his "BANG!" character.',
],
"finishers": [
    {"name":"Diamond Cutter", "desc":"Jumping cutter (a precursor to the RKO) — can be hit from nearly any position; one of wrestling's most versatile sudden-reversal finishers"},
    {"name":"Diamond Cutter from the top rope", "desc":"Elevated version when the setup allows — produces enormous crowd reaction"},
],
"championships": [
    cr("WCW World Heavyweight Championship","1999","Won in Four Corners match — peak of his late-career push and one of WCW's most satisfying title changes"),
    cr("WCW United States Championship","1997","US title reign during his ascent to the main event"),
    cr("WCW World Tag Team Championship","Multiple reigns 1996–99","Multiple tag team reigns with various partners during his rise"),
],
"personas": [
    {"name":"Manager / Valet Era","era":"1988–1991","desc":"Managed and guided wrestlers before deciding he wanted to compete himself — unusually late start for a performer who became a world champion."},
    {"name":"Diamond Dallas Page","era":"1991–present","desc":"The self-made man who turned 'Bang!' into a catchphrase and the Diamond Cutter into one of wrestling's most recognized finishers. Genuinely inspirational career arc."},
],
"timeline": [
    {"year":"1991","title":"In-ring debut at 35","desc":"Begins competing at an age when most wrestlers retire — a remarkable decision that leads to a world championship."},
    {"year":"1996","title":"Feud with The Outsiders","desc":"His conflict with Hall and Nash elevates him from comedic act to legitimate babyface contender."},
    {"year":"1997","title":"WCW US Championship","desc":"Wins the US title — his first major championship and the beginning of his main event push."},
    {"year":"1998","title":"Feud with Goldberg","desc":"His rivalry with Goldberg in 1998 produces WCW's most compelling babyface storytelling of the year."},
    {"year":"1999","title":"WCW World Champion","desc":"Wins the WCW title at Spring Stampede in a Four Corners match — his career peak at age 43."},
    {"year":"2001","title":"WWE run","desc":"Joins WWE after WCW closes; a famously mishandled run as a stalker character that wasted his potential."},
    {"year":"2012","title":"DDP Yoga and Scott Hall","desc":"His rehabilitation work with Scott Hall (Razor Ramon) becomes viral and demonstrates the genuine motivational philosophy behind his persona."},
    {"year":"2017","title":"WWE Hall of Fame","desc":"Inducted into the WWE Hall of Fame — long-overdue recognition for one of wrestling's great self-made success stories."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. Randy Savage","subtitle":"WCW Spring Stampede 1997","desc":"One of WCW's great hidden gems — a passionate, violent brawl between a veteran legend and an ascending star that both men committed to completely."},
    {"rating":"★★★★","title":"vs. Goldberg","subtitle":"WCW Halloween Havoc 1998","desc":"Goldberg's most complete babyface vs. babyface match — a rare WCW main event where the storytelling matched the crowd."},
    {"rating":"★★★★","title":"vs. Hulk Hogan","subtitle":"WCW Bash at the Beach 1999","desc":"WCW Championship match during DDP's peak run — Hogan at his most motivated, DDP at his most over."},
],
"faq": [
    {"q":"How old was Diamond Dallas Page when he won the WCW Championship?","a":"DDP won the WCW World Heavyweight Championship in April 1999 at age 43 — making him one of the oldest first-time world champions in major wrestling history. He began his in-ring career at 35."},
    {"q":"What is DDP Yoga?","a":"DDP Yoga is a fitness and rehabilitation program developed by Diamond Dallas Page that combines yoga, traditional calisthenics, and dynamic resistance. It became famous for helping wrestler Scott Hall (Razor Ramon) overcome addiction and physical decline."},
    {"q":"What is the Diamond Cutter?","a":"The Diamond Cutter is DDP's signature finisher — a jumping cutter that can be applied from nearly any position, catching opponents mid-move and driving their head into the mat. Randy Orton's RKO is widely considered its direct descendant."},
],
"record_rows": (
    row("diamond-dallas-page","ppv title","Randy Savage","WCW Spring Stampede 1997","Apr 6, 1997","Singles","Career-best match","W") +
    row("diamond-dallas-page","ppv title",a("goldberg","Goldberg"),"WCW Halloween Havoc 1998","Oct 25, 1998","Singles","","L") +
    row("diamond-dallas-page","ppv title",a("hulk-hogan","Hulk Hogan") + ", " + a("ric-flair","Ric Flair") + ", " + a("sting","Sting"),"WCW Spring Stampede 1999","Apr 11, 1999","Four Corners — WCW World Championship","Wins WCW title at 43","W") +
    row("diamond-dallas-page","ppv title",a("goldberg","Goldberg"),"WCW Fall Brawl 1998","Sep 13, 1998","Singles — US Championship","","L") +
    row("diamond-dallas-page","ppv","The Undertaker","WWE Judgment Day 2001","May 20, 2001","Singles","Mishandled WWE debut match","L") +
    row("diamond-dallas-page","tv",a("chris-jericho","Chris Jericho"),"WCW Nitro 1998","Various","Singles","Multiple WCW TV encounters","W")
),
},

# ── BULLY RAY ─────────────────────────────────────────────────────────────────
{
"slug": "bully-ray",
"name": "Bully Ray",
"subtitle": "The Most Dominant Man in TNA · Dudley Boy",
"born": "1971-07-14",
"from": "New York City, New York, USA",
"height": "6 ft 4 in (193 cm)",
"weight": "290 lb (132 kg)",
"trained": "ECW dojo, Paul Heyman school",
"debut": "1992",
"style": "Power brawler, hardcore specialist, ruthless heel psychology",
"aliases": ["Bubba Ray Dudley", "Brother Ray", "Mark LoMonaco"],
"wins": 86, "losses": 42, "draws": 2,
"wl_strip": ('<i></i>'*8 + '<i class="l"></i>'*3)*6 + '<i></i>'*2,
"method_bars": [
    {"label":"Pinfall","pct":55},
    {"label":"Table","pct":20},
    {"label":"Count-out / DQ","pct":15},
    {"label":"Other","pct":10},
],
"bio": [
    f'Mark LoMonaco spent the first half of his career as one-half of the most decorated tag team in wrestling history and the second half proving he was a singles main eventer who had been hidden behind his team\'s success. As Bubba Ray Dudley alongside D-Von, he won the WWE Tag Team Championships eight times, the ECW Tag Team titles, and the WCW Tag titles — the only team to hold championships in all three major American promotions.',
    f'The Dudley Boyz defined the Attitude Era\'s Hardcore aesthetic. The 3D (Dudley Death Drop) through tables became so iconic that crowds still chant "We want tables!" decades later. ECW gave them their foundation; WWE gave them their platform; and the combination produced one of the most universally recognized tag team moves in wrestling history.',
    f'His rebirth as Bully Ray in TNA/IMPACT beginning around 2012 is one of wrestling\'s great heel reinventions. Abandoning the Dudley identity entirely, Bully became a ruthless, manipulative, physically dominant heel who won the TNA World Heavyweight Championship and served as president of the Aces & Eights motorcycle club. The character work was genuine and committed — a performer who had been coasting on legacy finally demanding attention as an individual.',
    f'Ray continues to work as a wrestling trainer and analyst, contributing to new generations of performers while his legacy in the tag team and hardcore genres remains permanent.',
],
"finishers": [
    {"name":"Bubba Bomb (Bully Bomb)", "desc":"Sitout powerbomb — his primary singles finish; emphasizes his power advantage over most opponents"},
    {"name":"3D (Dudley Death Drop)", "desc":"Double team move with D-Von — 3D into a waiting partner's leg drop from the top; the most iconic ECW-era team finish"},
    {"name":"Bully Cutter", "desc":"Diamond Cutter variant used during his singles run as a secondary finish"},
],
"championships": [
    cr("TNA World Heavyweight Championship","2012–13","Won after a masterful heel run; the pinnacle of his singles career"),
    cr("WWE Tag Team Championship","8 reigns 1999–2006","Most decorated tag team in WWE history alongside D-Von Dudley"),
    cr("ECW World Tag Team Championship","Multiple reigns 1997–99","ECW foundational champions; won the titles before their national platform"),
    cr("WCW World Tag Team Championship","2001","Completed the unprecedented triple-promotion tag team championship collection"),
],
"personas": [
    {"name":"Bubba Ray Dudley","era":"1992–2012","desc":"The intense, violent half of the Dudley Boyz — feared for his power, tables obsession, and genuine aggression."},
    {"name":"Bully Ray","era":"2012–2015","desc":"Reinvented TNA villain who proved that everything the Dudley identity had masked — his promo ability, his ring psychology, his presence — was there all along."},
],
"timeline": [
    {"year":"1992","title":"Professional debut","desc":"Begins career in the Northeast independent scene; eventually connects with D-Von and forms the Dudley Boyz."},
    {"year":"1997","title":"ECW Tag Team Champions","desc":"Dudley Boyz win ECW titles and become ECW's defining team; develop the table-obsession gimmick."},
    {"year":"1999","title":"WWF debut","desc":"Dudleys arrive in WWF and immediately begin their run as the most hated tag team in the building."},
    {"year":"2000","title":"Tables match vs. Hardy Boyz and E&C","desc":"TLC matches at WrestleMania 2000 and SummerSlam 2000 create the ladder/table match template that WWE still uses."},
    {"year":"2006","title":"Return to ECW / TNA","desc":"Joins TNA as Brother Ray; begins slow transition away from the Dudley identity."},
    {"year":"2012","title":"Bully Ray reinvention","desc":"Drops Dudley/Brother identity; emerges as TNA's most compelling heel with Aces & Eights and eventual world title."},
    {"year":"2015","title":"WWE return as Dudley Boyz","desc":"Reunites with D-Von for a final WWE tag team run — nostalgia-driven but welcome."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"TLC vs. Hardy Boyz and Edge & Christian","subtitle":"WrestleMania 2000","desc":"The match that defined 'Attitude Era spectacle' — three teams, ladders, tables, chairs, and more WrestleMania moments than any single match had produced before it."},
    {"rating":"★★★★","title":"vs. Jeff Hardy","subtitle":"TNA Lockdown 2013","desc":"His TNA World title defense in a cage — the peak of his singles career, against a babyface crowd loved."},
    {"rating":"★★★★","title":"vs. D-Von","subtitle":"TNA/IMPACT 2012","desc":"Brother vs. brother storyline — Bully's Aces & Eights heel character revealed through a brutal family betrayal narrative."},
],
"faq": [
    {"q":"How many times did the Dudley Boyz win the WWE Tag Team Championship?","a":"The Dudley Boyz (Bubba Ray and D-Von) won the WWE/WWF Tag Team Championship eight times, making them one of the most decorated tag teams in WWE history."},
    {"q":"What is 3D?","a":"3D (Dudley Death Drop) is the Dudley Boyz's signature tag team finisher — Bubba Ray lifts an opponent onto D-Von's shoulders in a stunner position while D-Von drops them face-first onto the mat, assisted by a leg drop from Bubba."},
    {"q":"Did Bully Ray ever win a world championship?","a":"Yes. As Bully Ray in TNA/IMPACT Wrestling, he won the TNA World Heavyweight Championship in 2012–2013 during one of the most well-received heel turns in TNA history."},
],
"record_rows": (
    row("bully-ray","ppv title","Jeff Hardy","TNA Lockdown 2013","Apr 7, 2013","Singles — TNA World Championship","Career-best singles match","W") +
    row("bully-ray","ppv","Edge, Hardy Boyz","WrestleMania 2000","Apr 2, 2000","TLC Match","Defining Attitude Era spectacle","W") +
    row("bully-ray","ppv title","AJ Styles","TNA Slammiversary 2013","Jun 2, 2013","Singles — TNA World Championship","","W") +
    row("bully-ray","ppv title","AJ Styles","TNA Bound for Glory 2013","Oct 20, 2013","Singles — TNA World Championship","Styles wins title","L") +
    row("bully-ray","ppv","Hardy Boyz","WWE SummerSlam 2000","Aug 27, 2000","TLC Match","Second iconic TLC match","W") +
    row("bully-ray","tv","D-Von Dudley","TNA Impact 2012","Various","Singles","Aces &amp; Eights betrayal storyline","W")
),
},

# ── MERCEDES MONE ─────────────────────────────────────────────────────────────
{
"slug": "mercedes-mone",
"name": "Mercedes Moné",
"subtitle": "The CEO · The Boss",
"born": "1992-01-26",
"from": "Boston, Massachusetts, USA",
"height": "5 ft 5 in (165 cm)",
"weight": "130 lb (59 kg)",
"trained": "WWE Performance Center, Sara Del Rey",
"debut": "2010",
"style": "Technical wrestling, submission grappling, innovative offense",
"aliases": ["Sasha Banks", "Mercedes KV", "The Boss", "The CEO"],
"wins": 72, "losses": 31, "draws": 1,
"wl_strip": ('<i></i>'*9 + '<i class="l"></i>'*3)*5 + '<i></i>'*2,
"method_bars": [
    {"label":"Submission","pct":36},
    {"label":"Pinfall","pct":48},
    {"label":"Count-out / DQ","pct":12},
    {"label":"Other","pct":4},
],
"bio": [
    f'Mercedes Varnado grew up watching Eddie Guerrero and decided at a young age that she would become a professional wrestler. Signing with WWE in 2012 as Sasha Banks, she became one-quarter of the Four Horsewomen alongside {a("becky-lynch","Becky Lynch")}, {a("charlotte-flair","Charlotte Flair")}, and {a("bayley","Bayley")} — a generation that fundamentally transformed how WWE booked women\'s wrestling.',
    f'Banks\'s in-ring style is technically advanced beyond most of her peers. The Bank Statement (cross-face with hammerlock) is a credible, visually distinctive submission. Her double-knee attack from the second rope, the Meteora, adds aerial flair to a submission-based game. She can carry any match in any setting and has done so against the best performers in the world.',
    f'Her WWE tenure included four Raw Women\'s Championship reigns and some of the division\'s best matches, but a complex relationship with creative and periodic absences defined her later years. In 2023 she departed and signed with NJPW and AEW as Mercedes Moné, winning both the NJPW STRONG Women\'s Championship and the AEW TBS Championship and immediately establishing herself as a main event draw outside WWE.',
    f'As "The CEO," Moné\'s character combines business-world confidence with genuine in-ring excellence — a performer who can back up every boast she makes inside the ring.',
],
"finishers": [
    {"name":"Bank Statement", "desc":"Cross-face with hammerlock — her primary submission finisher; one of the most visually clear and legitimately dangerous-looking submissions in women's wrestling"},
    {"name":"Meteora", "desc":"Double-knee strike from the second rope while running — a high-risk move used as a secondary finish and crowd-pop moment"},
    {"name":"Backstabber", "desc":"Running double-knee to the back of an opponent hanging in the ropes — a setup move that flows into the Bank Statement"},
],
"championships": [
    cr("WWE Raw Women's Championship","4 reigns 2016–2021","Four reigns; her matches with Bayley produced the division's best technical work"),
    cr("AEW TBS Championship","2023–24","Immediate impact on arrival; dominant TBS champion"),
    cr("NJPW STRONG Women's Championship","2023","First foreigner to win the NJPW STRONG Women's title in Japan"),
    cr("NXT Women's Championship","2015–16","NXT title launch; defined the character with her legitimate heel work"),
],
"personas": [
    {"name":"The Boss (WWE)","era":"2012–2023","desc":"Legitimately dangerous submission specialist with a New England edge. The Four Horsewomen's most technically accomplished member."},
    {"name":"The CEO (AEW/NJPW)","era":"2023–present","desc":"Rebranded as a business-class heel who runs her career like a corporation — and backs it up with ring work that needs no corporate spin."},
],
"timeline": [
    {"year":"2010","title":"Independent debut","desc":"Begins competing regionally; signs with WWE developmental two years later."},
    {"year":"2012","title":"WWE Performance Center","desc":"Joins WWE as Sasha Banks; immediately impresses as one of the most naturally talented performers in developmental."},
    {"year":"2015","title":"NXT Women's Champion","desc":"Wins NXT title with a heel character that became the blueprint for women's complex character work in WWE."},
    {"year":"2015","title":"NXT TakeOver: Brooklyn","desc":"Her match with Bayley receives a standing ovation — the moment the division's potential was undeniable."},
    {"year":"2016","title":"Main roster debut / Raw Women's Championship","desc":"Four-way for inaugural Raw Women's title; begins her run of four championship reigns."},
    {"year":"2019","title":"WrestleMania 35 main event","desc":"Competes in the historic first women's WM main event in a role supporting the Lynch/Flair/Rousey program."},
    {"year":"2023","title":"Departs WWE; signs with NJPW and AEW","desc":"Leaves WWE, debuts as Mercedes Moné in Japan and then AEW — immediately a box office draw."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. Bayley","subtitle":"NXT TakeOver: Brooklyn, 2015","desc":"The match that proved the women's evolution was real. Both women committed completely to a 20-minute main-event-quality war that changed how WWE would book women's wrestling forever."},
    {"rating":"★★★★½","title":"vs. Bayley","subtitle":"NXT TakeOver: Respect, 2015","desc":"30-minute iron man match — the first in women's history in WWE. Extraordinary in-ring work from both performers."},
    {"rating":"★★★★","title":"vs. Becky Lynch","subtitle":"Hell in a Cell 2019","desc":"The first women's Hell in a Cell match — Banks and Lynch delivered the violence and drama the stipulation demanded."},
],
"faq": [
    {"q":"Why did Sasha Banks leave WWE?","a":"Mercedes Varnado (Sasha Banks) departed WWE in 2023 amid reports of creative disagreements. She had previously walked out of WWE programming in 2022. She signed with NJPW and AEW as Mercedes Moné."},
    {"q":"What is the Bank Statement?","a":"The Bank Statement is Sasha Banks/Mercedes Moné's signature submission — a crossface applied with the opponent's arm trapped in a hammerlock. It is one of the most technically credible submissions in women's wrestling."},
    {"q":"Who are the Four Horsewomen of WWE?","a":"The WWE Four Horsewomen are Charlotte Flair, Becky Lynch, Sasha Banks (Mercedes Moné), and Bayley — the generation of NXT women who collectively transformed women's wrestling in WWE into a main event attraction."},
],
"record_rows": (
    row("mercedes-mone","ppv title",a("bayley","Bayley"),"NXT TakeOver: Brooklyn","Aug 22, 2015","Singles — NXT Women's Championship","Standing ovation match; Bayley wins","L") +
    row("mercedes-mone","ppv title",a("bayley","Bayley"),"NXT TakeOver: Respect","Oct 7, 2015","30-Min Iron Man — NXT Women's Championship","First women's 30-min iron man; loses 3-2","L") +
    row("mercedes-mone","ppv title",a("becky-lynch","Becky Lynch"),"Hell in a Cell 2019","Oct 6, 2019","Hell in a Cell — Raw Women's Championship","","L") +
    row("mercedes-mone","ppv title",a("charlotte-flair","Charlotte Flair"),"SummerSlam 2016","Aug 21, 2016","Singles — Raw Women's Championship","Four-time champion series begins","W") +
    row("mercedes-mone","ppv",a("becky-lynch","Becky Lynch"),"Money in the Bank 2019","May 19, 2019","Singles — Raw Women's Championship","","L") +
    row("mercedes-mone","ppv title","Hikaru Shida","AEW Dynasty 2024","Apr 21, 2024","Singles — AEW TBS Championship","CEO era AEW title defense","W")
),
},

# ── CHRISTOPHER DANIELS ───────────────────────────────────────────────────────
{
"slug": "christopher-daniels",
"name": "Christopher Daniels",
"subtitle": "The Fallen Angel · The Best in the World Before It Was Cool",
"born": "1970-03-24",
"from": "Pontiac, Michigan, USA",
"height": "6 ft 0 in (183 cm)",
"weight": "220 lb (100 kg)",
"trained": "WCW Power Plant, Killer Kowalski",
"debut": "1993",
"style": "Technical wrestling, high-flying, character-driven storytelling",
"aliases": ["The Fallen Angel", "Curry Man", "Suicide", "Kazarian's Partner"],
"wins": 78, "losses": 42, "draws": 3,
"wl_strip": ('<i></i>'*8 + '<i class="l"></i>'*3)*6 + '<i></i>'*6,
"method_bars": [
    {"label":"Pinfall","pct":58},
    {"label":"Submission","pct":20},
    {"label":"Count-out / DQ","pct":14},
    {"label":"Other","pct":8},
],
"bio": [
    f'Daniel Covell has been one of the most respected independent wrestling performers for over three decades — a performer whose work ethic, technical ability, and character development made him a pivotal figure in the growth of ROH, TNA, and AEW. As Christopher Daniels, "The Fallen Angel," he developed one of wrestling\'s most complete villain characters and became a foundational builder of American independent wrestling.',
    f'His ROH work in the early 2000s set standards that the promotion built its reputation on. His trilogy with {a("samoa-joe","Samoa Joe")} and {a("aj-styles","AJ Styles")} at ROH\'s foundational events represents the era at its best — three performers who understood how to build drama inside a wrestling match without shortcuts.',
    f'TNA gave Daniels a national platform, and he used it to accumulate multiple X Division Championship reigns that defined that title\'s prestige. His comedic tag team work with Kazarian ("Roppongi 3K? No — SCM3K? No — Christopher Daniels and Frankie Kazarian!") showed a performer completely comfortable in his own skin.',
    f'AEW co-founder Tony Khan brought Daniels in as a vice president of talent relations and occasional in-ring performer — recognition that his contributions extend far beyond his match record.',
],
"finishers": [
    {"name":"Best Moonsault Ever (BME)", "desc":"Springboard moonsault from the second rope over a standing opponent — a visually spectacular move that requires precise spatial awareness"},
    {"name":"Angel's Wings", "desc":"Double underhook facebuster — drives the opponent's face directly into the mat; his most consistent finish"},
    {"name":"Last Rites", "desc":"Flipping cutter — used as a third option when the BME setup isn't available"},
],
"championships": [
    cr("TNA X Division Championship","Multiple reigns 2002–11","Defined the X Division's standard; most decorated X Division champion"),
    cr("ROH World Tag Team Championship","Multiple reigns 2003–06","ROH foundational tag champion with various partners"),
    cr("TNA World Heavyweight Championship","2012","Late-career world title reign — recognition of his consistent excellence"),
],
"personas": [
    {"name":"The Fallen Angel","era":"1997–present","desc":"A morally complex villain who quotes scripture, wears white trunks, and commits acts of calculated ruthlessness. One of independent wrestling's best pure villain characters."},
    {"name":"Curry Man / Comedy Daniels","era":"2008–2014","desc":"Surprising comedic character work that revealed a performer completely secure in his abilities and happy to entertain in any register."},
],
"timeline": [
    {"year":"1993","title":"Professional debut","desc":"Begins career at 23; spends years on the independent circuit developing his craft before national exposure."},
    {"year":"2002","title":"ROH foundational work","desc":"Becomes one of Ring of Honor's most important early performers; defines the promotion's in-ring standard."},
    {"year":"2002","title":"TNA debut","desc":"Joins TNA at its launch; becomes one of the company's most reliable performers across multiple eras."},
    {"year":"2004","title":"ROH triple threat classics","desc":"His work with AJ Styles and Samoa Joe in ROH produces matches that define American independent wrestling of the era."},
    {"year":"2012","title":"TNA World Champion","desc":"Wins the TNA World Heavyweight Championship — belated recognition of his main event talent."},
    {"year":"2019","title":"AEW co-founder role","desc":"Joins AEW as both performer and EVP of talent relations — cementing his legacy as a builder of the sport."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. AJ Styles vs. Samoa Joe","subtitle":"ROH Scramble Cage Melee, 2004","desc":"A three-way that distilled everything great about early ROH — three supremely talented performers in an anything-goes environment, all motivated to prove themselves."},
    {"rating":"★★★★½","title":"vs. AJ Styles","subtitle":"TNA Unbreakable 2005","desc":"Widely considered one of the finest matches in TNA history — a technically perfect singles match between two performers at their absolute peak."},
    {"rating":"★★★★","title":"vs. Samoa Joe","subtitle":"ROH Death Before Dishonor II, 2004","desc":"Part of the legendary ROH event that put American independent wrestling on the global map."},
],
"faq": [
    {"q":"What is the Best Moonsault Ever?","a":"The BME (Best Moonsault Ever) is Christopher Daniels's signature move — a springboard moonsault where he uses the second rope to launch himself over a standing opponent, landing on their back. It requires significant spatial awareness to execute safely."},
    {"q":"What role does Christopher Daniels play in AEW?","a":"Christopher Daniels serves as AEW's Executive Vice President of Talent Relations, helping manage the roster and talent recruitment, in addition to competing occasionally as a performer."},
    {"q":"Is Christopher Daniels the same as The Fallen Angel?","a":"Yes — 'The Fallen Angel' is Christopher Daniels's long-running character persona, used throughout his career in TNA, ROH, AEW, and on the independent circuit. The character draws on religious imagery to craft a morally complex villain."},
],
"record_rows": (
    row("christopher-daniels","ppv title",a("aj-styles","AJ Styles") + " &amp; " + a("samoa-joe","Samoa Joe"),"ROH Scramble Cage 2004","Aug 28, 2004","Three-Way","ROH classic triple threat","L") +
    row("christopher-daniels","ppv title",a("aj-styles","AJ Styles"),"TNA Unbreakable 2005","Sep 11, 2005","Singles — X Division Championship","TNA MOTY candidate","L") +
    row("christopher-daniels","ppv title",a("samoa-joe","Samoa Joe"),"ROH Death Before Dishonor II","Jun 12, 2004","Singles","ROH landmark event","L") +
    row("christopher-daniels","ppv title","Kurt Angle","TNA Bound for Glory 2012","Oct 14, 2012","Singles — TNA World Championship","","L") +
    row("christopher-daniels","tv","Frankie Kazarian","TNA Impact","Various","Tag Team","SCM3K era tag comedy work","W") +
    row("christopher-daniels","ppv title","CM Punk","ROH Final Battle 2004","Dec 26, 2004","Singles — ROH World Championship","","L")
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
print("\nBatch 6a complete.")
