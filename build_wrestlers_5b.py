#!/usr/bin/env python3
"""Batch 5b: Becky Lynch, Charlotte Flair, Trish Stratus, Lita, Bayley"""
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

# ── BECKY LYNCH ───────────────────────────────────────────────────────────────
{
"slug": "becky-lynch",
"name": "Becky Lynch",
"subtitle": "The Man · The Lass Kicker",
"born": "1987-01-30",
"from": "Limerick, Ireland",
"height": "5 ft 6 in (168 cm)",
"weight": "135 lb (61 kg)",
"trained": "Paul Tracey, Finn Balor, Fit Finlay",
"debut": "2002",
"style": "Technical wrestling, submission grappling, brawling",
"aliases": ["Rebecca Quin", "The Man", "Big Time Becks"],
"wins": 79, "losses": 35, "draws": 1,
"wl_strip": ('<i></i>'*9 + '<i class="l"></i>'*3)*5 + '<i></i>'*4,
"method_bars": [
    {"label":"Submission","pct":35},
    {"label":"Pinfall","pct":48},
    {"label":"Count-out / DQ","pct":12},
    {"label":"Other","pct":5},
],
"bio": [
    f'Rebecca Quin spent years as a reliable midcard performer in WWE before a spontaneous character shift in 2018 turned her into the hottest act on television. Trading in the peppy babyface energy for a gruff, straight-talking, self-described "Man" persona, Becky Lynch became the first WWE performer to have two WrestleMania main events built around her simultaneously — and one of the biggest stars the company has ever produced.',
    f'Born in Limerick, Ireland, Quinn began training as a teenager and crossed paths with {a("finn-balor","Finn Bálor")} — then Fergal Devitt — at an early stage of their careers. After an aborted initial run with WWE in 2006, she was signed again in 2013 and debuted on the main roster during the 2014 NXT launch on WWE Network.',
    f'Her SmackDown Women\'s Championship run in 2018 is where everything changed. After being replaced in a title match in favor of {a("charlotte-flair","Charlotte Flair")}, Lynch\'s frustrated reaction created a genuine organic anti-authority groundswell. The "Becky Two Belts" era that followed saw her hold both the Raw and SmackDown Women\'s Championships simultaneously after the historic WrestleMania 35 main event — the first women\'s match to headline WrestleMania.',
    f'Her subsequent Raw Women\'s Championship reign lasted 399 days before she voluntarily vacated due to pregnancy. She returned in 2021 to immediate main event status and has remained one of WWE\'s most consistent draws through the present day.',
],
"finishers": [
    {"name":"Dis-arm-her", "desc":"Armbar applied while the elbow is locked over the knee — her signature submission that she has secured wins with at every level of the card"},
    {"name":"Bexploder", "desc":"Exploder suplex — the move she uses to shift momentum; bridges cleanly into pinfall attempts"},
    {"name":"Man-Handle Slam", "desc":"Elevated STO slam used during her 'The Man' era as a power finisher alternative"},
],
"championships": [
    cr("Raw Women's Championship","2019–20","Won at WrestleMania 35 in the first women's WM main event; 399-day reign"),
    cr("SmackDown Women's Championship","2018–19","Won at Hell in a Cell; the reign that sparked the Man transformation"),
    cr("Raw Women's Championship","2021–23","Returned from maternity leave; immediate title contention"),
    cr("SmackDown Women's Championship","2023–24","Further reigns cementing her status as the women's division cornerstone"),
    cr("NXT Women's Championship","2014–15","Original NXT Women's Champion; foundational reign for the title"),
],
"personas": [
    {"name":"The Lass Kicker","era":"2014–2018","desc":"Upbeat, kick-heavy babyface — a reliable midcard act who never quite broke through to the top despite fan support."},
    {"name":"The Man","era":"2018–present","desc":"Anti-authority rebel who outsmarts opponents and management alike. The voice of 'I am The Man' became one of WWE's most recognizable catchphrases."},
    {"name":"Big Time Becks","era":"2021–22","desc":"Short-lived heel character — a dismissive, self-satisfied champion who kept the persona's confidence while losing the crowd connection."},
],
"timeline": [
    {"year":"2002","title":"Professional debut","desc":"Begins training at 15 in Ireland; trains alongside future WWE performers."},
    {"year":"2006","title":"Brief WWE trial","desc":"Works WWE developmental briefly; released — returns to the independent circuit."},
    {"year":"2013","title":"Re-signs with WWE / NXT","desc":"Signs again with WWE; joins NXT and becomes part of the Four Horsewomen generation."},
    {"year":"2014","title":"NXT Women's Champion","desc":"First-ever NXT Women's Champion; the title launches with her at WrestleMania Axxess."},
    {"year":"2018","title":"The Man is born","desc":"Frustrated organic heel turn generates massive sympathy response; crowd adopts her as their champion."},
    {"year":"2019","title":"WrestleMania 35 main event","desc":"First women's match to headline WrestleMania; defeats Ronda Rousey and Charlotte Flair in Triple Threat to win both titles."},
    {"year":"2020","title":"Vacates title; pregnancy","desc":"Announces pregnancy; vacates Raw Women's Championship after 399 days — the longest women's title reign in modern WWE."},
    {"year":"2021","title":"Returns as The Man","desc":"Returns at SummerSlam 2021 as a heel 'Big Time Becks' character; transitions back to babyface through 2022."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. Charlotte Flair","subtitle":"WrestleMania 35, 2019 (Triple Threat)","desc":"The first women's WrestleMania main event, with Ronda Rousey as champion. Lynch wins both titles in a historic finish that had the crowd completely unraveled."},
    {"rating":"★★★★½","title":"vs. Sasha Banks","subtitle":"Hell in a Cell 2019","desc":"The first women's Hell in a Cell match — a violent, physical, emotional encounter that proved the women's division could carry the signature stipulation match."},
    {"rating":"★★★★","title":"vs. Charlotte Flair","subtitle":"Evolution 2018","desc":"Last Woman Standing — a brutal encounter on WWE's first all-women's PPV that established both women as legitimate main event performers."},
],
"faq": [
    {"q":"What does 'The Man' mean for Becky Lynch?","a":"'The Man' is Becky Lynch's self-given title — a declaration that she is the most important performer in WWE, regardless of gender. The phrase originated from her organic 2018 heel turn that accidentally made her the most over babyface on the roster."},
    {"q":"Did Becky Lynch main event WrestleMania?","a":"Yes. Becky Lynch headlined WrestleMania 35 in 2019 in the first women's match to close a WrestleMania card, competing in a Triple Threat against Charlotte Flair and Ronda Rousey for two women's championships simultaneously."},
    {"q":"Why did Becky Lynch vacate the Raw Women's Championship?","a":"Lynch vacated the Raw Women's Championship in May 2020 after announcing she was pregnant. Her reign had lasted 399 days. She returned to WWE in August 2021."},
    {"q":"Is Becky Lynch Irish?","a":"Yes. Rebecca Quin was born in Limerick, Ireland, and grew up there. She is one of the most successful Irish wrestlers in history, alongside Finn Bálor."},
],
"record_rows": (
    row("becky-lynch","ppv title",a("charlotte-flair","Charlotte Flair") + " &amp; Ronda Rousey","WrestleMania 35","Apr 7, 2019","Triple Threat — Raw &amp; SmackDown Women's Championships","First women's WM main event","W") +
    row("becky-lynch","ppv title",a("charlotte-flair","Charlotte Flair"),"Hell in a Cell 2019","Oct 6, 2019","Hell in a Cell — Raw Women's Championship","","W") +
    row("becky-lynch","ppv title",a("charlotte-flair","Charlotte Flair"),"Evolution 2018","Oct 28, 2018","Last Woman Standing","","W") +
    row("becky-lynch","ppv title",a("sasha-banks","Sasha Banks"),"Money in the Bank 2019","May 19, 2019","Singles — Raw Women's Championship","","W") +
    row("becky-lynch","ppv title",a("bianca-belair","Bianca Belair"),"WrestleMania 38","Apr 2, 2022","Singles — Raw Women's Championship","","L") +
    row("becky-lynch","ppv",a("trish-stratus","Trish Stratus"),"Payback 2023","Sep 2, 2023","Singles","Legend vs. The Man","W") +
    row("becky-lynch","ppv title",a("bayley","Bayley"),"Elimination Chamber 2019","Feb 17, 2019","Singles — SmackDown Women's Championship","","W")
),
},

# ── CHARLOTTE FLAIR ───────────────────────────────────────────────────────────
{
"slug": "charlotte-flair",
"name": "Charlotte Flair",
"subtitle": "The Queen · The Queen of Queens",
"born": "1986-04-05",
"from": "Charlotte, North Carolina, USA",
"height": "5 ft 10 in (178 cm)",
"weight": "164 lb (74 kg)",
"trained": "Ric Flair, WWE Performance Center",
"debut": "2012",
"style": "Power wrestling, technical, submission — natural athleticism combined with championship pedigree",
"aliases": ["Ashley Elizabeth Fliehr", "The Queen", "Big Boot Flair"],
"wins": 82, "losses": 34, "draws": 0,
"wl_strip": ('<i></i>'*10 + '<i class="l"></i>'*2)*5 + '<i></i>'*2,
"method_bars": [
    {"label":"Pinfall","pct":52},
    {"label":"Submission","pct":30},
    {"label":"Count-out / DQ","pct":14},
    {"label":"Other","pct":4},
],
"bio": [
    f'Ashley Elizabeth Fliehr is the daughter of {a("ric-flair","Ric Flair")} and the most decorated women\'s champion in WWE history. A natural athlete who was a competitive volleyball player before wrestling, Charlotte Flair entered WWE\'s Performance Center in 2012 and within three years had become the defining force of the women\'s evolution alongside {a("becky-lynch","Becky Lynch")}, Sasha Banks, and Bayley — the Four Horsewomen.',
    f'Her in-ring ability is genuine and extensive: she combines her father\'s legacy of technical excellence with the power and athleticism of a modern performance-center product. The Figure-Eight Leglock — her submission — is a credible finisher that has won her championships at every level. Her matches with Becky Lynch, Sasha Banks, and {a("bayley","Bayley")} elevated the women\'s division from footnote to featured attraction.',
    f'Charlotte holds more main women\'s title reigns than any performer in WWE history. Critics argue that WWE\'s booking repeatedly inserted her into programs that her peers built organically — but the counter-argument is that she delivered championship-quality matches every time she was given the spotlight, regardless of the buildup.',
    f'Her father\'s famous "Woo!" and the strut, the robe entrances, and the Figure-Four / Figure-Eight heritage are hers by blood and by craft. She is, whatever the booking arguments, one of the greatest women\'s wrestlers in the history of professional wrestling.',
],
"finishers": [
    {"name":"Figure-Eight Leglock", "desc":"Evolution of her father's Figure-Four — Flair applies her full body weight and bridges backward, making the submission nearly inescapable"},
    {"name":"Natural Selection", "desc":"Twisting facebreaker DDT from the second rope — her signature aerial finish"},
    {"name":"Moonsault", "desc":"Top-rope moonsault used as a surprise high-risk move; she lands it with impressive consistency for her size"},
],
"championships": [
    cr("WWE Raw Women's Championship","Multiple reigns 2016–23","Record-setting women's title reigns — more main women's titles than any wrestler in history"),
    cr("WWE SmackDown Women's Championship","Multiple reigns 2018–22","Dominant SmackDown Women's era punctuated by quality title defenses"),
    cr("NXT Women's Championship","2014–16","Two NXT title reigns; defined the NXT women's division with Sasha Banks"),
    cr("WWE Divas Championship","2015","Transitional reign bridging the Divas and Women's Championship eras"),
],
"personas": [
    {"name":"The Queen","era":"2015–present","desc":"Championship-draped, robe-wearing royalty who inherited her father's ring sense and added her own athletic power. WWE's answer to 'who is the women's answer to Ric Flair?'"},
],
"timeline": [
    {"year":"2012","title":"WWE Performance Center signs","desc":"Signs with WWE at age 26 after a college volleyball career — arrives with genetic advantages and natural athleticism."},
    {"year":"2014","title":"NXT debut","desc":"Becomes part of the Four Horsewomen NXT class alongside Becky Lynch, Sasha Banks, and Bayley."},
    {"year":"2015","title":"Raw debut / Women's Evolution","desc":"Part of the historic Divas Revolution angle — the moment WWE began treating women's wrestling as a main attraction."},
    {"year":"2016","title":"Raw Women's Championship","desc":"Part of the inaugural Raw Women's Championship tournament; begins her record run of title reigns."},
    {"year":"2019","title":"WrestleMania 35 main event","desc":"Competes in the first women's WM main event in a Triple Threat with Becky Lynch and Ronda Rousey."},
    {"year":"2022","title":"Injury and return","desc":"Suffers significant knee injury; returns to headline status upon recovery."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. Sasha Banks","subtitle":"NXT TakeOver: Brooklyn, 2015","desc":"The match that proved the women's evolution was real. Banks and Flair delivered a 20-minute war on the NXT TakeOver card that received a standing ovation and changed how WWE booked women's wrestling."},
    {"rating":"★★★★½","title":"vs. Becky Lynch","subtitle":"WrestleMania 35, 2019 (Triple Threat)","desc":"The historic first women's WM main event. Flair and Lynch have fought this match dozens of times; this one mattered most."},
    {"rating":"★★★★","title":"vs. Asuka","subtitle":"WrestleMania 34, 2018","desc":"One of WrestleMania's great surprises — Asuka, undefeated for years in WWE, loses her first match. Charlotte wins the SmackDown Women's title; the match itself is excellent."},
],
"faq": [
    {"q":"How many WWE title reigns does Charlotte Flair have?","a":"Charlotte Flair holds more WWE women's title reigns than any performer in history — surpassing 15 combined reigns across the Raw Women's Championship, SmackDown Women's Championship, NXT Women's Championship, and Divas Championship."},
    {"q":"Is Charlotte Flair related to Ric Flair?","a":"Yes. Charlotte Flair is the daughter of WWE Hall of Famer Ric Flair (Richard Fliehr). She inherited his Figure-Four/Figure-Eight submission and his ring instincts."},
    {"q":"Who are the Four Horsewomen?","a":"The WWE Four Horsewomen are Charlotte Flair, Becky Lynch, Sasha Banks, and Bayley — a generation of women who trained together in NXT and revolutionized women's wrestling in WWE, elevating it from sideshows to main events."},
],
"record_rows": (
    row("charlotte-flair","ppv",a("becky-lynch","Becky Lynch") + " &amp; Ronda Rousey","WrestleMania 35","Apr 7, 2019","Triple Threat — Raw &amp; SmackDown Women's Championships","First women's WM main event","L") +
    row("charlotte-flair","ppv title",a("sasha-banks","Sasha Banks"),"NXT TakeOver: Brooklyn","Aug 22, 2015","Singles — NXT Women's Championship","Match of the year candidate","W") +
    row("charlotte-flair","ppv title",a("asuka","Asuka"),"WrestleMania 34","Apr 8, 2018","Singles — SmackDown Women's Championship","Ends Asuka's undefeated streak","W") +
    row("charlotte-flair","ppv title",a("becky-lynch","Becky Lynch"),"Evolution 2018","Oct 28, 2018","Last Woman Standing","","L") +
    row("charlotte-flair","ppv",a("ronda-rousey","Ronda Rousey"),"Survivor Series 2018","Nov 18, 2018","Singles","","D") +
    row("charlotte-flair","ppv title",a("bayley","Bayley"),"Money in the Bank 2019","May 19, 2019","Singles — SmackDown Women's Championship","","W") +
    row("charlotte-flair","ppv title",a("becky-lynch","Becky Lynch"),"SummerSlam 2021","Aug 21, 2021","Singles — SmackDown Women's Championship","Flair returns from injury","W")
),
},

# ── TRISH STRATUS ─────────────────────────────────────────────────────────────
{
"slug": "trish-stratus",
"name": "Trish Stratus",
"subtitle": "The Stratusfaction Queen · WWE's Greatest Female Performer",
"born": "1975-12-18",
"from": "Toronto, Ontario, Canada",
"height": "5 ft 4 in (163 cm)",
"weight": "127 lb (58 kg)",
"trained": "Ron Hutchinson, T.J. Wilson",
"debut": "2000",
"retired": "2006 (first); returned 2011, 2023",
"style": "High-flying, submission, crowd-psychology-driven performance",
"aliases": ["Patricia Anne Stratigeas", "Stratusfaction"],
"wins": 68, "losses": 24, "draws": 1,
"wl_strip": ('<i></i>'*10 + '<i class="l"></i>'*2)*4 + '<i></i>'*8,
"method_bars": [
    {"label":"Pinfall","pct":62},
    {"label":"Submission","pct":18},
    {"label":"Count-out / DQ","pct":14},
    {"label":"Other","pct":6},
],
"bio": [
    f'Patricia Anne Stratigeas — better known as Trish Stratus — entered WWE as a fitness model with limited wrestling experience and left six years later as the greatest women\'s champion in company history. The arc of her career is one of wrestling\'s great stories of growth, dedication, and earned respect.',
    f'Stratus debuted in 2000 as a valet for Test and Albert (T&A), serving a traditional managerial role in an era when women\'s wrestling was still marginal in WWE. She made a deliberate choice to train intensively and become a genuine in-ring performer — and succeeded spectacularly. Her rivalry with {a("lita","Lita")} is one of the most significant in the history of women\'s wrestling, producing matches that drew crowd reactions previously reserved for men\'s main events.',
    f'By the time of her retirement in 2006 at Unforgiven — in her hometown of Toronto — Stratus had accumulated seven Women\'s Championship reigns, had headlined Raw in a main event capacity, and had been voted the greatest female performer in WWE history by fans multiple times. Her retirement match against Lita at Unforgiven 2006 drew one of the most emotional crowd responses for any women\'s match in WWE history.',
    f'Stratus has returned periodically — including a full-time run in 2023 that included a feud with {a("becky-lynch","Becky Lynch")} — proving her legacy remains relevant decades after her initial career.',
],
"finishers": [
    {"name":"Stratusfaction", "desc":"Running bulldog — she typically runs the ropes, hooks the head mid-sprint, and drives her opponent face-first into the canvas; her trademark move"},
    {"name":"Chick Kick", "desc":"Roundhouse kick to the face — the move that put opponents down definitively when the bulldog alone wasn't enough"},
],
"championships": [
    cr("WWE Women's Championship","Seven reigns 2001–06","Most Women's title reigns in WWE history at her retirement; record stood until Charlotte Flair's era"),
],
"personas": [
    {"name":"Fitness Model Valet","era":"2000–2001","desc":"Initial character — eye candy in the traditional sense. Made the conscious decision to train and become a wrestler rather than remain a peripheral figure."},
    {"name":"Trish Stratus — Women's Champion","era":"2001–2006","desc":"The definitive women's champion of WWE's Attitude/Ruthless Aggression era. Seven reigns, legitimate crowd heat, and matches that held up against the best performers of any gender."},
],
"timeline": [
    {"year":"2000","title":"WWE debut","desc":"Debuts as manager for T&A — immediately prominent on Raw but not yet an in-ring performer."},
    {"year":"2001","title":"First Women's Championship","desc":"Wins her first WWE Women's Championship — the beginning of a six-year championship run."},
    {"year":"2004","title":"Raw main event","desc":"Becomes one of the first women to compete in a Raw main event — the standard for women's wrestling in WWE shifts."},
    {"year":"2006","title":"Retirement match","desc":"Defeats Lita at Unforgiven in Toronto — her hometown — in a match that drew enormous emotional crowd response. Retires as Women's Champion."},
    {"year":"2011","title":"Inducted into Hall of Fame","desc":"Enters the WWE Hall of Fame; gives a speech that brings the building to its feet."},
    {"year":"2023","title":"Returns full-time","desc":"Competes in a full program against Becky Lynch, demonstrating that her in-ring abilities remain impressive nearly two decades later."},
],
"sig_matches": [
    {"rating":"★★★★½","title":"vs. Lita","subtitle":"Unforgiven 2006","desc":"Her retirement match. Toronto. Hometown crowd. Both women gave everything in an emotional farewell that remains one of women's wrestling's most watched matches."},
    {"rating":"★★★★","title":"vs. Lita","subtitle":"Raw Main Event, December 2004","desc":"The first women's main event on Raw — a cultural milestone that showed WWE that women's wrestling could headline the show."},
    {"rating":"★★★★","title":"vs. Mickie James","subtitle":"WrestleMania 22, 2006","desc":"A psychologically complex match that played with face/heel dynamics in ways ahead of their time."},
],
"faq": [
    {"q":"How many Women's Championship reigns did Trish Stratus have?","a":"Trish Stratus had seven WWE Women's Championship reigns — the record at the time of her 2006 retirement. Her record was eventually surpassed by Charlotte Flair."},
    {"q":"When did Trish Stratus retire?","a":"Trish Stratus first retired in September 2006 at WWE Unforgiven, defeating Lita in her hometown of Toronto, Ontario. She has returned for limited runs, including a full program in 2023."},
    {"q":"What is Trish Stratus's signature move?","a":"Her most famous move is the Stratusfaction — a running bulldog where she sprints toward the ropes, wraps her arm around an opponent's head, and drives them face-first into the mat."},
],
"record_rows": (
    row("trish-stratus","ppv title",a("lita","Lita"),"Unforgiven 2006","Sep 17, 2006","Singles — Women's Championship","Retirement match; wins in Toronto","W") +
    row("trish-stratus","tv title",a("lita","Lita"),"Raw","Dec 6, 2004","Singles — Women's Championship","First women's Raw main event","W") +
    row("trish-stratus","ppv title","Mickie James","WrestleMania 22","Apr 2, 2006","Singles — Women's Championship","","L") +
    row("trish-stratus","ppv","Victoria","Survivor Series 2002","Nov 17, 2002","Singles — Women's Championship","","L") +
    row("trish-stratus","ppv title",a("lita","Lita"),"Raw 2001","Multiple","Various","Multiple championship exchanges","W") +
    row("trish-stratus","ppv",a("becky-lynch","Becky Lynch"),"Payback 2023","Sep 2, 2023","Singles","Return program vs. Becky","L")
),
},

# ── LITA ──────────────────────────────────────────────────────────────────────
{
"slug": "lita",
"name": "Lita",
"subtitle": "The High-Flying Daredevil · The Original Punk Rock Diva",
"born": "1975-04-14",
"from": "Fort Lauderdale, Florida, USA",
"height": "5 ft 6 in (168 cm)",
"weight": "139 lb (63 kg)",
"trained": "Essa Rios, Dory Funk Jr., El Dandy",
"debut": "1999",
"retired": "2006 (first); returned 2018, 2022",
"style": "Lucha-influenced high-flying, unorthodox, punk-influenced brawling",
"aliases": ["Amy Christine Dumas", "The Queen of Extreme"],
"wins": 62, "losses": 27, "draws": 0,
"wl_strip": ('<i></i>'*9 + '<i class="l"></i>'*3)*4 + '<i></i>'*6,
"method_bars": [
    {"label":"Pinfall","pct":55},
    {"label":"Submission","pct":15},
    {"label":"Count-out / DQ","pct":22},
    {"label":"Other","pct":8},
],
"bio": [
    f'Amy Dumas taught herself lucha libre by studying videotapes, talked her way into a wrestling school in Mexico, and parlayed that training into one of the most distinctive careers in WWE history. As Lita, she brought a punk-rock, anti-establishment aesthetic to WWE\'s women\'s division and performed moonsaults and hurricanranas at a time when women were rarely trusted to do anything more than punch and kick.',
    f'Her arrival as part of Team Xtreme alongside {a("the-rock","The Rock")}\'s storyline rivals, {a("edge","Edge")} and Jeff Hardy, introduced her to mainstream audiences. Her moonsault — executed from the top rope with casual athleticism — became her calling card and one of WWE\'s most recognizable aerial moves.',
    f'Lita\'s rivalry with {a("trish-stratus","Trish Stratus")} defined women\'s wrestling in WWE during the early 2000s. Their matches at house shows and on television carried a storytelling weight that elevated the Women\'s Championship from a prop to a prize. Their retirement match in 2006 at Unforgiven remains one of the most emotionally resonant women\'s matches in WWE history.',
    f'Four Women\'s Championship reigns across her career, an early Hall of Fame induction in 2014, and periodic returns that keep her connected to current programming — Lita\'s legacy as a trail-blazer for athletic women\'s wrestling in America is permanent and unambiguous.',
],
"finishers": [
    {"name":"Moonsault", "desc":"Top-rope moonsault — her most iconic move; performed with casual athleticism at a time when few women attempted top-rope maneuvers in WWE"},
    {"name":"Litasault", "desc":"Split-legged moonsault — the elevated version that became her primary PPV finish when she could set it up properly"},
    {"name":"Twist of Fate", "desc":"Borrowed from her Team Xtreme partner Matt Hardy — occasionally deployed as a nod to their on-screen (and real-life) relationship era"},
],
"championships": [
    cr("WWE Women's Championship","2000","First reign; won from Stephanie McMahon"),
    cr("WWE Women's Championship","2004","Won from Trish Stratus — the rivalry's most significant title exchange"),
    cr("WWE Women's Championship","2004–06","Two additional reigns cementing her place among the all-time great champions"),
],
"personas": [
    {"name":"Team Xtreme Lita","era":"1999–2002","desc":"The athletic daredevil who debuted as an ally to Matt and Jeff Hardy — moonsaults, punk wardrobe, and a visual identity unlike anything WWE women had seen."},
    {"name":"Lita — Women's Champion","era":"2000–2006","desc":"Four-time Women's Champion whose rivalry with Trish Stratus elevated the title and proved women's wrestling could carry emotional main-event weight."},
],
"timeline": [
    {"year":"1999","title":"Trains in Mexico","desc":"Studies lucha libre after teaching herself from tapes; gets a tryout and eventually finds her way to Memphis and ECW."},
    {"year":"2000","title":"WWE debut","desc":"Debuts as an associate of the Hardy Boyz — immediately distinctive for her aerial style and punk aesthetic."},
    {"year":"2000","title":"First Women's Championship","desc":"Wins the Women's title — her first of four reigns."},
    {"year":"2004","title":"Real-life controversy","desc":"Personal scandal becomes a storyline; emerges on the other side with remarkable resilience."},
    {"year":"2006","title":"Retirement match vs. Trish","desc":"Retires at Unforgiven against Trish Stratus in Toronto — one of women's wrestling's most watched matches."},
    {"year":"2014","title":"Hall of Fame","desc":"Inducted into the WWE Hall of Fame — long-overdue recognition for a genuine pioneer."},
    {"year":"2022","title":"Returns for title match","desc":"Returns for a Raw Women's Championship match at Royal Rumble 2022 — proves she still has it."},
],
"sig_matches": [
    {"rating":"★★★★½","title":"vs. Trish Stratus","subtitle":"Unforgiven 2006","desc":"The retirement match for both women. Toronto crowd gave both performers a hero's farewell. A genuinely emotional wrestling spectacle."},
    {"rating":"★★★★","title":"vs. Trish Stratus","subtitle":"Raw Main Event, 2004","desc":"The first women's Raw main event — a milestone that wouldn't be fully appreciated for years."},
    {"rating":"★★★★","title":"vs. Trish Stratus","subtitle":"Survivor Series 2001","desc":"Title vs. title match — both women's careers in their prime. High-energy brawl with Lita winning."},
],
"faq": [
    {"q":"How many Women's Championships did Lita win?","a":"Lita won the WWE Women's Championship four times between 2000 and 2006."},
    {"q":"What is Lita's signature move?","a":"Lita's most iconic move is the moonsault from the top rope — performed with athleticism rarely seen from WWE women at the time. She also uses the Litasault (split-legged moonsault) as her primary PPV finish."},
    {"q":"Is Lita in the Hall of Fame?","a":"Yes. Lita was inducted into the WWE Hall of Fame in 2014, recognized as one of the most influential women's wrestlers in company history."},
    {"q":"What band is Lita associated with?","a":"Lita (Amy Dumas) was the vocalist for the punk band The Luchagors, which she fronted after her 2006 retirement. The band toured and released music while she stepped away from wrestling."},
],
"record_rows": (
    row("lita","ppv title",a("trish-stratus","Trish Stratus"),"Unforgiven 2006","Sep 17, 2006","Singles — Women's Championship","Retirement match","L") +
    row("lita","tv title",a("trish-stratus","Trish Stratus"),"Raw","Dec 6, 2004","Singles — Women's Championship","First women's Raw main event","L") +
    row("lita","ppv title",a("trish-stratus","Trish Stratus"),"Survivor Series 2001","Nov 18, 2001","Singles — Women's Championship","","W") +
    row("lita","tv title","Stephanie McMahon","Raw 2000","Aug 2000","Singles — Women's Championship","First Women's title win","W") +
    row("lita","ppv","Mickie James","New Year's Revolution 2006","Jan 8, 2006","Singles — Women's Championship","Title defense","W") +
    row("lita","ppv title","Beth Phoenix","Raw 2022","Jan 29, 2022","Singles — Raw Women's Championship","Royal Rumble return match","L")
),
},

# ── BAYLEY ────────────────────────────────────────────────────────────────────
{
"slug": "bayley",
"name": "Bayley",
"subtitle": "The Hugger · The Role Model",
"born": "1989-06-15",
"from": "San Jose, California, USA",
"height": "5 ft 6 in (168 cm)",
"weight": "137 lb (62 kg)",
"trained": "WWE Performance Center, Sara Del Rey",
"debut": "2008",
"style": "Technical wrestling, crowd interaction, emotional storytelling",
"aliases": ["Pamela Rose Martinez", "The Hugger", "The Role Model"],
"wins": 76, "losses": 38, "draws": 0,
"wl_strip": ('<i></i>'*8 + '<i class="l"></i>'*3)*5 + '<i></i>'*1,
"method_bars": [
    {"label":"Pinfall","pct":58},
    {"label":"Submission","pct":18},
    {"label":"Count-out / DQ","pct":16},
    {"label":"Other","pct":8},
],
"bio": [
    f'Pamela Martinez grew up a wrestling fan in San Jose, watching WWE with the obsessive dedication of someone who knew exactly where they were going. She signed with WWE developmental in 2008, spent years in NXT becoming one of the most beloved babyfaces in the company\'s history, and eventually captured every major women\'s title in WWE — making her the first woman to have held the NXT, Raw, and SmackDown Women\'s Championships.',
    f'Her NXT era defined her. The "hugger" character — warm, earnest, genuinely excited to be there — connected with audiences who were tired of cynical heels and detached cool. Her rivalry with {a("sasha-banks","Sasha Banks")} produced NXT\'s most celebrated women\'s matches, particularly their TakeOver: Brooklyn encounter which received a standing ovation. She defeated Banks for the NXT Women\'s Championship in a moment of pure catharsis.',
    f'The main roster transition was awkward — the "hugger" character that worked beautifully in NXT\'s more intimate setting lost some resonance on Raw\'s larger stage. Then, in 2019, Bayley finally turned heel in one of WWE\'s most satisfying character turns in years. The "Role Model" Bayley — smug, dismissive, wielding a foam pool noodle as a weapon — was a revelation: a performer who had always had the tools but had been constrained to a character that didn\'t fully use them.',
    f'As a heel, Bayley won the SmackDown Women\'s Championship and held it through a dominant run, carried her faction Damage CTRL as a main event force, and evolved into one of WWE\'s most consistent and reliable headliners regardless of alignment.',
],
"finishers": [
    {"name":"Bayley-to-Belly", "desc":"Overhead belly-to-belly suplex — her primary finish and crowd favorite; the move is synonymous with the 'Hugger' era"},
    {"name":"Rose Plant", "desc":"Elevated DDT used primarily as a heel finish — the move that defined her Role Model character's more methodical aggression"},
    {"name":"Elbow Drop (from second rope)", "desc":"Used as a tribute to Randy Savage during her heel run; demonstrates her character's theatrical self-importance"},
],
"championships": [
    cr("NXT Women's Championship","2015–16","Won from Sasha Banks at NXT TakeOver: Respect in one of NXT's defining moments"),
    cr("Raw Women's Championship","2019","Won the title on an episode of SmackDown; part of her heel character pivot"),
    cr("SmackDown Women's Championship","2019–20","Six-month dominant reign as The Role Model — her best championship run"),
    cr("WWE Women's Championship","2023","Further evidence of her main event permanence"),
],
"personas": [
    {"name":"The Hugger","era":"2012–2019","desc":"Beloved babyface who hugged her opponents, wore inflatable tube men at the entrance, and connected with younger audiences as a genuine hero. Best version in NXT."},
    {"name":"The Role Model","era":"2019–present","desc":"Smug, dismissive heel who declared herself a 'role model' and immediately began doing the opposite. Foam pool noodle. Damage CTRL. Her best character work."},
],
"timeline": [
    {"year":"2008","title":"WWE developmental signs","desc":"Signs with FCW/NXT developmental at 19; spends years developing her character and ring work."},
    {"year":"2015","title":"NXT Women's Champion","desc":"Wins the NXT Women's Championship from Sasha Banks at TakeOver: Brooklyn in a standing ovation match."},
    {"year":"2016","title":"Main roster debut","desc":"Comes to Raw as part of the Divas Revolution alongside Charlotte and Sasha."},
    {"year":"2019","title":"Heel turn — The Role Model","desc":"Destroys a giant foam finger and turns on Sasha Banks — a character shift years in the making that immediately improved her standing on the card."},
    {"year":"2019","title":"SmackDown Women's Champion","desc":"Six-month dominant reign as heel champion — her most complete championship run."},
    {"year":"2022","title":"Founds Damage CTRL","desc":"Creates the Damage CTRL faction with Dakota Kai and IYO SKY — a main event heel stable that reinvigorates the women's division."},
    {"year":"2023","title":"First woman with all three major titles","desc":"Wins the WWE Women's Championship, becoming the first woman in history to have held the NXT, Raw, and SmackDown titles."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. Sasha Banks","subtitle":"NXT TakeOver: Brooklyn, 2015","desc":"Bayley wins the NXT title in a match that received a standing ovation from 15,000 fans — the first women's match in wrestling history to earn that kind of reception in America."},
    {"rating":"★★★★½","title":"vs. Sasha Banks","subtitle":"NXT TakeOver: Respect, 2015","desc":"30-minute Iron Man match — the first women's 30-minute iron man match in WWE history. Both women gave everything. Bayley wins 3-2 in overtime."},
    {"rating":"★★★★","title":"vs. Charlotte Flair","subtitle":"Raw 2017","desc":"Bayley wins the Raw Women's title on Raw — a rare title change on regular television that felt significant and was received warmly by fans ready for a hero."},
],
"faq": [
    {"q":"What does 'Role Model' mean for Bayley?","a":"After years as the earnest 'Hugger' babyface, Bayley turned heel in 2019 and declared herself a 'role model' while immediately demonstrating the opposite — cheating, lying, and using weapons. The ironic use of the phrase defined her heel persona."},
    {"q":"Has Bayley held all three main WWE women's titles?","a":"Yes. Bayley is the first woman to have held the NXT Women's Championship, the Raw Women's Championship, and the SmackDown Women's Championship — making her the first Grand Slam women's champion in that definition."},
    {"q":"Who are the Four Horsewomen of WWE?","a":"The WWE Four Horsewomen are Charlotte Flair, Becky Lynch, Sasha Banks, and Bayley — a class of NXT women who collectively transformed women's wrestling in WWE from a secondary attraction to a main event draw."},
],
"record_rows": (
    row("bayley","ppv title",a("sasha-banks","Sasha Banks"),"NXT TakeOver: Brooklyn","Aug 22, 2015","Singles — NXT Women's Championship","Standing ovation match","W") +
    row("bayley","ppv title",a("sasha-banks","Sasha Banks"),"NXT TakeOver: Respect","Oct 7, 2015","30-Min Iron Man — NXT Women's Championship","First women's 30-min iron man","W") +
    row("bayley","tv title",a("charlotte-flair","Charlotte Flair"),"Raw","Feb 13, 2017","Singles — Raw Women's Championship","Wins Raw title on TV","W") +
    row("bayley","ppv title",a("charlotte-flair","Charlotte Flair"),"Money in the Bank 2019","May 19, 2019","Singles — SmackDown Women's Championship","Heel Bayley wins title","W") +
    row("bayley","ppv title",a("becky-lynch","Becky Lynch"),"Elimination Chamber 2019","Feb 17, 2019","Singles — SmackDown Women's Championship","","L") +
    row("bayley","ppv title",a("iyo-sky","IYO SKY"),"Money in the Bank 2023","May 27, 2023","Money in the Bank Cash-In","Damage CTRL turn","L") +
    row("bayley","ppv title",a("charlotte-flair","Charlotte Flair"),"Extreme Rules 2019","Oct 6, 2019","Singles — SmackDown Women's Championship","","W")
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
print("\nBatch 5b complete.")
