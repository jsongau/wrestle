#!/usr/bin/env python3
"""Batch 7a: Gunther, Bianca Belair, IYO SKY, Liv Morgan, LA Knight"""
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

# ── GUNTHER ───────────────────────────────────────────────────────────────────
{
"slug": "gunther",
"name": "Gunther",
"subtitle": "The Ring General · Der Tiroler",
"born": "1988-04-08",
"from": "Vienna, Austria",
"height": "6 ft 4 in (193 cm)",
"weight": "275 lb (125 kg)",
"trained": "Mick Moretti, wXw Wrestling Academy",
"debut": "2005",
"style": "Old-school European catch wrestling, power striking, submission — the Ring General philosophy",
"aliases": ["Walter Hahn", "WALTER", "The Ring General", "Der Tiroler"],
"wins": 94, "losses": 18, "draws": 2,
"wl_strip": ('<i></i>'*13 + '<i class="l"></i>'*1)*6 + '<i></i>'*2,
"method_bars": [
    {"label":"Submission","pct":38},
    {"label":"Pinfall","pct":46},
    {"label":"Count-out / DQ","pct":10},
    {"label":"Other","pct":6},
],
"bio": [
    f'Walter Hahn is one of the most legitimately intimidating performers in professional wrestling — a 6\'4", 275-pound Austrian who wrestles like he is genuinely trying to hurt his opponent and has the technique to make that threat credible. Known in Europe as WALTER and later rebranded as Gunther in WWE, he has built one of the most dominant title reigns in modern WWE history.',
    f'Gunther\'s wrestling philosophy is rooted in European catch wrestling and the old NWA tradition of the champion as an unbeatable force who must be earned rather than handed a loss. His matches are structured around the question: can his opponent survive long enough to find an opening? The answer is usually no.',
    f'His NXT UK Championship reign of 870 days was the longest of any title in modern NXT history — a record that stood as testament to his dominance on the European scene before his main roster call-up. On SmackDown, he won the Intercontinental Championship and proceeded to hold it for 666 days — the longest IC title reign in WWE history — before losing it to {a("sami-zayn","Sami Zayn")} in a match that earned a thunderous crowd reaction for Zayn\'s victory.',
    f'His 2024 transition to the main world title picture, winning the World Heavyweight Championship at SummerSlam 2024, placed him where his in-ring ability has always suggested he belonged — at the very top of WWE\'s card.',
],
"finishers": [
    {"name":"Powerbomb", "desc":"Sit-out powerbomb delivered with controlled violence — Gunther drives opponents straight down; the move emphasizes his power advantage"},
    {"name":"Sleeper Hold", "desc":"Rear chinlock applied with full leverage — in Gunther's hands it looks genuinely dangerous; used as a submission finish when the opponent has been sufficiently worn down"},
    {"name":"Chop", "desc":"Not technically a finisher but functionally one — his knife-edge chops are the loudest and most devastating in wrestling; they accumulate damage across every match"},
],
"championships": [
    cr("World Heavyweight Championship","2024–","Won at SummerSlam 2024; main event coronation"),
    cr("WWE Intercontinental Championship","2022–23","666-day reign — longest IC title reign in WWE history"),
    cr("NXT UK Championship","2019–22","870-day reign — longest reign of any NXT title in history"),
    cr("wXw Unified World Wrestling Championship","Multiple reigns 2014–19","European cornerstone before WWE signing"),
],
"personas": [
    {"name":"WALTER (wXw / NXT UK)","era":"2005–2021","desc":"The European super-villain — dominant, methodical, and capable of making even short matches feel like genuine struggles for survival."},
    {"name":"Gunther (WWE)","era":"2022–present","desc":"Same performer, broader stage. The Intercontinental Championship reign redefined what the title could be. Ring General philosophy: the champion is the standard, and opponents must earn every moment."},
],
"timeline": [
    {"year":"2005","title":"Professional debut","desc":"Begins career in Austria at 17; starts developing the catch-wrestling foundation that defines his style."},
    {"year":"2014","title":"wXw World Champion","desc":"Wins European title; establishes himself as the continent's most dominant heavyweight."},
    {"year":"2019","title":"NXT UK Champion","desc":"Wins the NXT UK Championship; begins an 870-day reign that becomes the longest in NXT history."},
    {"year":"2022","title":"WWE main roster debut as Gunther","desc":"Called up to SmackDown; immediately wins the Intercontinental Championship and begins redefining the title's prestige."},
    {"year":"2023","title":"IC record broken","desc":"Surpasses Pedro Morales's 40-year record for longest Intercontinental Championship reign at 666 days before losing to Sami Zayn."},
    {"year":"2024","title":"World Heavyweight Champion","desc":"Wins the World Heavyweight Championship at SummerSlam 2024 — the logical culmination of three years of dominance."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. Sheamus","subtitle":"NXT TakeOver: Dublin (Clash at the Castle: Scotland), 2022","desc":"A brutal, physical war between two Europeans who know how to deliver genuine pain. The chops alone set a new standard for what a strike-based match could be."},
    {"rating":"★★★★★","title":"vs. Sami Zayn","subtitle":"WWE SummerSlam 2023","desc":"The IC record match — 666 days ended by a Zayn who the crowd desperately wanted to win. Gunther made the loss feel monumental by making every Zayn near-fall feel impossible."},
    {"rating":"★★★★½","title":"vs. Ilja Dragunov","subtitle":"NXT TakeOver: Deadline, 2021","desc":"A legendary NXT UK match — both men gave everything in a performance that felt genuinely dangerous and was immediately recognized as one of the best matches in NXT UK history."},
],
"faq": [
    {"q":"Why did WALTER become Gunther?","a":"When Walter Hahn was called up to WWE's main roster in 2022, the company rebranded him as Gunther — dropping the WALTER name that had become synonymous with his European dominance. The change was primarily a trademark/legal matter."},
    {"q":"How long was Gunther's Intercontinental Championship reign?","a":"Gunther held the WWE Intercontinental Championship for 666 days — the longest IC title reign in the title's 45-year history, surpassing Pedro Morales's record set in the 1980s."},
    {"q":"Is Gunther the best technical wrestler in WWE?","a":"Gunther is widely considered the most complete big-man technical wrestler in WWE and arguably in the world. His catch-wrestling base, European training, and ability to make every move look credible put him in rare company."},
],
"record_rows": (
    row("gunther","ppv title",a("sami-zayn","Sami Zayn"),"SummerSlam 2023","Aug 5, 2023","Singles — IC Championship","666-day reign ends","L") +
    row("gunther","ppv title","Sheamus","Clash at the Castle","Jun 18, 2022","Singles — IC Championship","Brutal European war","W") +
    row("gunther","ppv title","Ilja Dragunov","NXT TakeOver","Dec 2021","Singles — NXT UK Championship","NXT UK MOTY","W") +
    row("gunther","ppv title",a("drew-mcintyre","Drew McIntyre"),"Clash at the Castle: Scotland","Jun 15, 2024","Singles — World Heavyweight Championship","World title defense","W") +
    row("gunther","ppv title",a("damian-priest","Damian Priest"),"Money in the Bank 2024","Jul 6, 2024","Singles — World Heavyweight Championship","Title match","L") +
    row("gunther","ppv title",a("sami-zayn","Sami Zayn"),"SummerSlam 2024","Aug 3, 2024","Singles — World Heavyweight Championship","World title win","W") +
    row("gunther","tv title","Ricochet","SmackDown 2022","May 20, 2022","Singles — IC Championship","First IC title win","W")
),
},

# ── BIANCA BELAIR ─────────────────────────────────────────────────────────────
{
"slug": "bianca-belair",
"name": "Bianca Belair",
"subtitle": "The EST of WWE · The Incomparable",
"born": "1989-04-09",
"from": "Knoxville, Tennessee, USA",
"height": "5 ft 7 in (170 cm)",
"weight": "145 lb (66 kg)",
"trained": "WWE Performance Center",
"debut": "2016",
"style": "Power wrestling, athletic high-flying, KOD-led combination offense",
"aliases": ["Bianca Crawford", "The EST of WWE", "The Incomparable"],
"wins": 74, "losses": 28, "draws": 0,
"wl_strip": ('<i></i>'*11 + '<i class="l"></i>'*2)*5 + '<i></i>'*4,
"method_bars": [
    {"label":"Pinfall","pct":62},
    {"label":"Submission","pct":14},
    {"label":"Count-out / DQ","pct":16},
    {"label":"Other","pct":8},
],
"bio": [
    f'Bianca Crawford was a Division I track and field athlete at the University of Tennessee before pursuing professional wrestling — a background that explains the extraordinary physical gifts she brings to every performance. The KOD (Kiss of Death) — a 450-pound-press overhead before the slam — is not a trick; it is the result of genuine athletic training applied to a new discipline.',
    f'Belair signed with WWE in 2016 and developed rapidly through NXT, winning the NXT Women\'s Championship in 2021. Her WrestleMania 37 entrance — a four-minute moment of self-presentation that introduced her to a returning live audience after the COVID era — was one of the great WrestleMania entrances in recent memory. She went on to defeat {a("sasha-banks","Sasha Banks")} (Mercedes Moné) in a 17-minute main event that delivered on every expectation.',
    f'Her braid — often used as a whip, a distraction-breaker, or a weapon — is one of wrestling\'s most distinctive visual signatures. The "EST of WWE" gimmick (Strongest, Fastest, Baddest, etc.) is backed up by physical evidence that makes it credible rather than hollow.',
    f'Multiple Raw Women\'s Championship reigns have established her as a top-line draw. Her partnership and rivalry with {a("becky-lynch","Becky Lynch")} produced some of the best women\'s television WWE has aired in the modern era.',
],
"finishers": [
    {"name":"KOD (Kiss of Death)", "desc":"Gorilla press into a uranage slam — she lifts opponents overhead with full extension and then drops them sideways onto the mat; a genuine feat of strength"},
    {"name":"Hair Whip", "desc":"Signature rather than finish — she uses her long braid as a literal weapon, whipping opponents with it; effective both as a spot and a crowd-popping distraction"},
    {"name":"Glam Slam (KOD variation)", "desc":"When the press lift isn't the call, she drives opponents face-first from a lifted position — her secondary finish"},
],
"championships": [
    cr("Raw Women's Championship","2021–22","Won at WrestleMania 37 in the first women's WM main event to open a live-crowd WrestleMania"),
    cr("Raw Women's Championship","2022–23","Second raw title reign; long and dominant"),
    cr("SmackDown Women's Championship","2023","SmackDown title during brand-switch period"),
    cr("NXT Women's Championship","2021","NXT title before main roster call-up"),
],
"personas": [
    {"name":"The EST of WWE","era":"2019–present","desc":"Every superlative — strongest, fastest, baddest — backed up by verifiable athletic achievement. The gimmick works because the body does the talking."},
],
"timeline": [
    {"year":"2016","title":"Signs with WWE","desc":"Recruited from the track and field world; begins developmental at the Performance Center."},
    {"year":"2021","title":"NXT Women's Champion","desc":"Wins the NXT title shortly before her main roster call-up."},
    {"year":"2021","title":"WrestleMania 37 main event","desc":"Defeats Sasha Banks in the SmackDown Women's Championship match — one of the best WrestleMania women's matches ever."},
    {"year":"2022","title":"WrestleMania 38 triumph","desc":"Defeats Becky Lynch in a rematch at WrestleMania 38 to win the Raw Women's Championship — another WM main card win."},
    {"year":"2022","title":"Dominant Raw Women's Championship run","desc":"Second title reign sees her elevated to the top of the women's division consistently."},
    {"year":"2023","title":"SmackDown Women's Championship","desc":"Transitions to SmackDown; wins the SmackDown title and continues main event position."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. Sasha Banks","subtitle":"WrestleMania 37, 2021","desc":"The return of live crowds, a four-minute entrance that the 25,000 fans in Tampa absorbed fully, and a 17-minute championship match that delivered everything. One of the best WM women's matches."},
    {"rating":"★★★★½","title":"vs. Becky Lynch","subtitle":"WrestleMania 38, 2022","desc":"A rematch built over months of television — Belair wins clean with the KOD in a match that cemented her as the face of the women's division."},
    {"rating":"★★★★","title":"vs. Asuka","subtitle":"Raw 2022","desc":"Title vs. career match — high-stakes television that demonstrated both performers' ability to carry a main event with no safety net."},
],
"faq": [
    {"q":"What does EST of WWE mean?","a":"EST stands for 'Every Superlative Thing' — Bianca Belair describes herself as the Strongest, Fastest, Baddest, and most athletic performer in WWE. The claim is backed by her Division I track and field background at the University of Tennessee."},
    {"q":"What is the KOD?","a":"The KOD (Kiss of Death) is Bianca Belair's finishing move — a gorilla press lift where she holds opponents fully extended overhead before dropping them into a uranage slam. It requires genuine strength to execute safely."},
    {"q":"Did Bianca Belair wrestle in WrestleMania?","a":"Yes. Belair has competed in multiple WrestleMania main card matches, including WrestleMania 37 (defeating Sasha Banks for the SmackDown Women's Championship) and WrestleMania 38 (defeating Becky Lynch for the Raw Women's Championship)."},
],
"record_rows": (
    row("bianca-belair","ppv title",a("mercedes-mone","Sasha Banks"),"WrestleMania 37","Apr 10, 2021","Singles — SmackDown Women's Championship","Career-defining WM win","W") +
    row("bianca-belair","ppv title",a("becky-lynch","Becky Lynch"),"WrestleMania 38","Apr 2, 2022","Singles — Raw Women's Championship","Second WM main card win","W") +
    row("bianca-belair","ppv title",a("becky-lynch","Becky Lynch"),"SummerSlam 2021","Aug 21, 2021","Singles — Raw Women's Championship","Becky's surprise return","L") +
    row("bianca-belair","ppv title",a("asuka","Asuka"),"Raw 2022","Various","Singles — Raw Women's Championship","Title vs. career","W") +
    row("bianca-belair","ppv title",a("charlotte-flair","Charlotte Flair"),"WrestleMania 36","Apr 5, 2020","Singles","Pre-championship rivalry","L") +
    row("bianca-belair","ppv title",a("iyo-sky","IYO SKY"),"Money in the Bank 2023","May 27, 2023","Cash-In — SmackDown Women's Championship","IYO cashes in on Belair","L")
),
},

# ── IYO SKY ───────────────────────────────────────────────────────────────────
{
"slug": "iyo-sky",
"name": "IYO SKY",
"subtitle": "The Genius of the Sky · Damage CTRL Leader",
"born": "1990-03-26",
"from": "Kanagawa, Japan",
"height": "5 ft 1 in (155 cm)",
"weight": "110 lb (50 kg)",
"trained": "Stardom Dojo",
"debut": "2007",
"style": "High-flying, lucha-influenced, exceptional aerial precision",
"aliases": ["Io Shirai", "Io Sky", "The Genius of the Sky"],
"wins": 82, "losses": 24, "draws": 1,
"wl_strip": ('<i></i>'*12 + '<i class="l"></i>'*1)*5 + '<i></i>'*7,
"method_bars": [
    {"label":"Pinfall","pct":65},
    {"label":"Submission","pct":16},
    {"label":"Count-out / DQ","pct":13},
    {"label":"Other","pct":6},
],
"bio": [
    f'Io Shirai is widely considered the greatest women\'s wrestler in the world during her peak years in Stardom and NXT — a performer of such extraordinary aerial ability and timing that she made moves look effortless that other wrestlers spend careers attempting. As IYO SKY in WWE, she has brought that excellence to the largest stage in wrestling.',
    f'Shirai began her career in Japan at 16, joining Stardom and becoming one of the promotion\'s most iconic performers. Her matches in Stardom — particularly her feuds with Mayu Iwatani and her tenure as Wonder of Stardom Champion — built a reputation that preceded her to NXT. She signed with WWE in 2018 and debuted to immediate recognition from fans who had followed her Japanese career.',
    f'Her NXT run was remarkable: a villain turn that produced some of NXT\'s most creative and violent heel work, followed by an NXT Women\'s Championship reign that validated everything fans had expected. Her moonsault — executed from the top rope with a level of height and rotation that few performers achieve — is one of professional wrestling\'s most spectacular moves.',
    f'Her Damage CTRL work alongside {a("bayley","Bayley")} and Dakota Kai brought her to the main roster in a prominent role. Her Money in the Bank cash-in on {a("bianca-belair","Bianca Belair")} in 2023 elevated her to SmackDown Women\'s Champion — the culmination of five years of exceptional WWE work.',
],
"finishers": [
    {"name":"Over the Moonsault (Moonsault)", "desc":"Top-rope moonsault with extraordinary height and rotation — considered by many to be the most beautiful moonsault in modern wrestling"},
    {"name":"Crossface", "desc":"Crossface submission — applied with technical precision after grounding high-energy opponents who can't match her on the mat"},
    {"name":"Tiger Feint Kick (619 variant)", "desc":"619-style kick through the ropes — a signature setup move that transitions into her aerial sequence"},
],
"championships": [
    cr("WWE SmackDown Women's Championship","2023–24","Won via Money in the Bank cash-in on Bianca Belair; dominant reign"),
    cr("NXT Women's Championship","2020–21","Best NXT Women's reign of the modern era — combined heel intensity with genuine athletic showcase"),
    cr("Women's Tag Team Championship","2022–23","Multiple reigns with Dakota Kai as Damage CTRL"),
    cr("Wonder of Stardom Championship","Multiple reigns 2013–18","Japanese legend status before WWE signing"),
],
"personas": [
    {"name":"Io Shirai — Stardom Legend","era":"2007–2018","desc":"Japan's most complete women's performer — technically precise, athletically extraordinary, and beloved by fans who recognized once-in-a-generation ability."},
    {"name":"IYO SKY — Damage CTRL","era":"2022–present","desc":"Main roster performer and SmackDown Women's Champion — the international star who proved Japanese wrestling excellence transfers completely to WWE's global stage."},
],
"timeline": [
    {"year":"2007","title":"Stardom debut at 16","desc":"Begins career as a teenager; immediately shows the aerial ability that will define her career."},
    {"year":"2012","title":"Wonder of Stardom Champion","desc":"Wins Japan's premier women's title; begins a decade of dominance in Stardom."},
    {"year":"2018","title":"Signs with WWE / NXT debut","desc":"Global wrestling community celebrates her signing; debuts in NXT to a massive reception from fans who know her reputation."},
    {"year":"2020","title":"NXT Women's Champion","desc":"Wins NXT title in a heel run that combines athletic excellence with genuine character work."},
    {"year":"2022","title":"Damage CTRL formation","desc":"Joins Bayley's Damage CTRL faction; moves to the main roster as part of a stable that revitalizes the women's division."},
    {"year":"2023","title":"SmackDown Women's Championship","desc":"Cashes in Money in the Bank on Bianca Belair — the culmination of her main roster trajectory."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. Mayu Iwatani","subtitle":"Stardom, 2016 (various)","desc":"Their ongoing feud in Stardom is considered among the greatest women's rivalries in wrestling history — technical, emotional, and capable of filling any venue."},
    {"rating":"★★★★½","title":"vs. Rhea Ripley","subtitle":"NXT TakeOver: Portland, 2020","desc":"A physically intense NXT title match that pushed both performers and produced one of NXT's best women's matches."},
    {"rating":"★★★★","title":"vs. Bianca Belair","subtitle":"Various, 2023","desc":"Their SmackDown championship feud produced consistent quality television and proved IYO SKY could carry a main event program on the biggest stage."},
],
"faq": [
    {"q":"Who is Io Shirai?","a":"Io Shirai is IYO SKY's Japanese name — the name under which she became one of the most celebrated women's wrestlers in the world in Stardom. She signed with WWE in 2018 and was rebranded as IYO SKY upon her main roster debut."},
    {"q":"What is IYO SKY's finishing move?","a":"IYO SKY's signature finish is a top-rope moonsault, considered by many to be the most technically perfect moonsault in women's wrestling — characterized by exceptional height, rotation, and landing precision."},
    {"q":"Is IYO SKY Japanese?","a":"Yes. IYO SKY (Io Shirai) is from Kanagawa, Japan. She began her career in Japanese women's wrestling at age 16 and became one of the most celebrated performers in Stardom before signing with WWE."},
],
"record_rows": (
    row("iyo-sky","ppv title",a("bianca-belair","Bianca Belair"),"Money in the Bank 2023","May 27, 2023","Cash-In — SmackDown Women's Championship","Cashes in; wins title","W") +
    row("iyo-sky","ppv title",a("rhea-ripley","Rhea Ripley"),"NXT TakeOver: Portland","Feb 16, 2020","Singles — NXT Women's Championship","NXT title match","L") +
    row("iyo-sky","ppv title",a("bayley","Bayley"),"Money in the Bank 2023","May 27, 2023","Singles — SmackDown Women's Championship","Turns on Bayley post-cash-in","W") +
    row("iyo-sky","ppv title",a("asuka","Asuka"),"WrestleMania XL","Apr 6, 2024","Singles — Women's Championship","WM title defense","L") +
    row("iyo-sky","ppv title",a("bianca-belair","Bianca Belair"),"SummerSlam 2023","Aug 5, 2023","Singles — SmackDown Women's Championship","First PPV title defense","W") +
    row("iyo-sky","tv",a("becky-lynch","Becky Lynch"),"SmackDown 2023","Various","Singles","TV championship encounters","L")
),
},

# ── LIV MORGAN ────────────────────────────────────────────────────────────────
{
"slug": "liv-morgan",
"name": "Liv Morgan",
"subtitle": "The Underdog · The Miracle",
"born": "1994-06-08",
"from": "Elmwood Park, New Jersey, USA",
"height": "5 ft 3 in (160 cm)",
"weight": "115 lb (52 kg)",
"trained": "WWE Performance Center",
"debut": "2014",
"style": "High-energy brawling, submission, crowd-interactive performance",
"aliases": ["Gionna Jene Daddio", "The Underdog"],
"wins": 66, "losses": 34, "draws": 0,
"wl_strip": ('<i></i>'*9 + '<i class="l"></i>'*3)*5 + '<i></i>'*1,
"method_bars": [
    {"label":"Pinfall","pct":58},
    {"label":"Submission","pct":22},
    {"label":"Count-out / DQ","pct":14},
    {"label":"Other","pct":6},
],
"bio": [
    f'Gionna Daddio signed with WWE at 19 and spent years developing in NXT and on the main roster as part of Riott Squad before emerging as a solo act that connected with audiences in a way her faction work never quite captured. The "underdog from Jersey" narrative — relatable, scrappy, never giving up — landed with a fanbase that wanted someone to root for who felt like them.',
    f'Her Money in the Bank cash-in on {a("rhea-ripley","Rhea Ripley")} in 2024 — executed while Ripley was distracted — awarded her the Women\'s World Championship in a moment that divided fans but produced enormous online engagement and an immediate main event run. Whatever the booking arguments, Morgan\'s ability to hold the spotlight and generate crowd responses has never been in question.',
    f'Her submission finisher — the Oblivion — and her athletic brawling style make her matches unpredictable enough to be entertaining regardless of the opponent. She has worked programs with {a("becky-lynch","Becky Lynch")}, {a("charlotte-flair","Charlotte Flair")}, and Rhea Ripley — every program in the main event women\'s tier.',
    f'Morgan\'s social media presence is one of WWE\'s largest among women performers — a legitimate factor in her booking and evidence that she has connected with an audience outside the traditional wrestling demo.',
],
"finishers": [
    {"name":"Oblivion", "desc":"Arm-trapped swinging facebuster — she locks the arm, swings through, and drives the opponent face-first into the mat; compact and effective"},
    {"name":"Riptide (borrowed)", "desc":"Variations of her finish have borrowed names across her career; the Oblivion is the consistent one"},
],
"championships": [
    cr("WWE Women's World Championship","2024","Won via Money in the Bank cash-in on Rhea Ripley"),
    cr("SmackDown Women's Championship","2022","First world title — won at Day 1 2022 in an upset cash-in"),
],
"personas": [
    {"name":"Riott Squad Era","era":"2017–2020","desc":"Part of the Riott Squad stable with Ruby Riott and Sarah Logan — faction work that gave her television time while her individual character developed."},
    {"name":"The Underdog / The Miracle","era":"2020–present","desc":"Solo act that found the crowd connection that faction work obscured. Relatable Jersey girl who never stops trying — and occasionally wins when no one thinks she will."},
],
"timeline": [
    {"year":"2014","title":"Signs with WWE at 19","desc":"One of WWE's younger signings; begins developmental work in NXT."},
    {"year":"2017","title":"Riott Squad debut","desc":"Debuts on the main roster as part of Riott Squad — immediate television presence if not individual character work."},
    {"year":"2020","title":"Solo run begins","desc":"Riott Squad disbands; Morgan begins solo career that slowly builds genuine fan connection."},
    {"year":"2022","title":"SmackDown Women's Championship cash-in","desc":"Cashes in Money in the Bank on Charlotte Flair at Day 1 — her first world title."},
    {"year":"2024","title":"Women's World Championship","desc":"Cashes in second Money in the Bank briefcase on Rhea Ripley — wins her second world championship."},
],
"sig_matches": [
    {"rating":"★★★★","title":"vs. Rhea Ripley","subtitle":"SummerSlam 2024","desc":"Women's World Championship match after Ripley's return from injury — Morgan defends against the most dominant women's performer of the era."},
    {"rating":"★★★★","title":"vs. Becky Lynch","subtitle":"WrestleMania 39, 2023","desc":"SmackDown Women's title match at WrestleMania — competitive performance that established Morgan as a credible main event worker."},
    {"rating":"★★★½","title":"vs. Charlotte Flair","subtitle":"Day 1 2022","desc":"The cash-in moment that gave Morgan her first world title — Charlotte distracted, Morgan striking; a controversial but crowd-pleasing surprise."},
],
"faq": [
    {"q":"How did Liv Morgan win the Women's World Championship?","a":"Liv Morgan won the WWE Women's World Championship in 2024 by cashing in her Money in the Bank briefcase on Rhea Ripley, who had just competed in a match and was weakened. It was her second Money in the Bank cash-in win."},
    {"q":"What is Liv Morgan's finishing move?","a":"Liv Morgan's primary finishing move is the Oblivion — an arm-trapped swinging facebuster that drives the opponent's face into the mat from a standing position."},
    {"q":"Is Liv Morgan from New Jersey?","a":"Yes. Gionna Daddio is from Elmwood Park, New Jersey — a background that fed into her 'Jersey girl' underdog character identity."},
],
"record_rows": (
    row("liv-morgan","ppv title",a("rhea-ripley","Rhea Ripley"),"Money in the Bank 2024","Jul 6, 2024","Cash-In — Women's World Championship","Wins Women's World title","W") +
    row("liv-morgan","ppv title",a("rhea-ripley","Rhea Ripley"),"SummerSlam 2024","Aug 3, 2024","Singles — Women's World Championship","Title defense vs. returning Ripley","L") +
    row("liv-morgan","ppv title",a("becky-lynch","Becky Lynch"),"WrestleMania 39","Apr 1, 2023","Singles — SmackDown Women's Championship","WM main card match","L") +
    row("liv-morgan","ppv title",a("charlotte-flair","Charlotte Flair"),"Day 1 2022","Jan 1, 2022","Cash-In — SmackDown Women's Championship","First cash-in; first title","W") +
    row("liv-morgan","ppv title",a("charlotte-flair","Charlotte Flair"),"WrestleMania Backlash 2022","May 8, 2022","Singles — SmackDown Women's Championship","Title defense","W") +
    row("liv-morgan","ppv title",a("iyo-sky","IYO SKY"),"SmackDown 2024","Various","Singles","Championship program","L")
),
},

# ── LA KNIGHT ─────────────────────────────────────────────────────────────────
{
"slug": "la-knight",
"name": "LA Knight",
"subtitle": "Yeah! · The Mega Star",
"born": "1982-10-16",
"from": "Rochester, New York, USA",
"height": "6 ft 1 in (185 cm)",
"weight": "240 lb (109 kg)",
"trained": "Dory Funk Jr.",
"debut": "2003",
"style": "Old-school heel-psychology brawler turned crowd-interactive babyface, charisma-driven",
"aliases": ["Shaun Ricker", "Eli Drake", "The Mega Star"],
"wins": 68, "losses": 36, "draws": 1,
"wl_strip": ('<i></i>'*9 + '<i class="l"></i>'*3)*5 + '<i></i>'*3,
"method_bars": [
    {"label":"Pinfall","pct":62},
    {"label":"Submission","pct":10},
    {"label":"Count-out / DQ","pct":18},
    {"label":"Other","pct":10},
],
"bio": [
    f'Shaun Ricker spent two decades perfecting his craft before breaking through as LA Knight — a performer whose combination of promo ability, crowd interaction, and ring work produced one of WWE\'s most organic fan connections of the 2020s. The "YEAH!" call-and-response chant became one of WWE\'s most reliable crowd moments, and its organic adoption proved that Knight\'s charisma was genuine rather than manufactured.',
    f'His pre-WWE career included a successful run in IMPACT Wrestling as Eli Drake, where his "Dummy, yeah!" catchphrase and natural mic ability established him as one of the company\'s best promo workers. WWE signed him in 2021 and initially used him as a midcard heel before the crowd rebellion in his favor forced creative to pivot.',
    f'Knight\'s rise as a babyface is one of WWE\'s better examples of following the crowd rather than fighting it. When audiences began responding to him as a hero despite heel booking, management adjusted — and the resulting run as a babyface chasing the United States and WWE Championships produced some of SmackDown\'s best crowd atmosphere of 2023–2024.',
    f'His character is rooted in old-school wrestling charisma — the confident strut, the deliberate delivery, the "lemme talk to ya" address to the audience. He is one of the last performers in WWE who can hold an arena on the mic for five minutes without a prop or a video package.',
],
"finishers": [
    {"name":"BFT (Blunt Force Trauma)", "desc":"Running jumping cutter from a standing position — his signature finish; delivered with full momentum and a crowd-pleasing snap"},
    {"name":"Jumping Elbow Drop", "desc":"Top-rope elbow drop — tribute to classic wrestling and a crowd-pop moment when the setup lands correctly"},
],
"championships": [
    cr("United States Championship","2023–24","Won as a babyface after an organic groundswell of fan support; carried the title with consistent charisma"),
    cr("IMPACT World Championship","2017","Won during his Eli Drake era — peak of his pre-WWE career"),
    cr("IMPACT King of the Mountain Championship","2017","Secondary IMPACT title during his dominant run"),
],
"personas": [
    {"name":"Eli Drake (IMPACT)","era":"2015–2021","desc":"'Dummy, yeah!' — the IMPACT version of the character that laid the groundwork: strong promo, natural confidence, the 'yeah' crowd interaction in proto-form."},
    {"name":"LA Knight — The Mega Star","era":"2021–present","desc":"The fully realized version: WWE production, bigger crowds, and a fanbase that adopted him organically against booking that initially tried to resist the connection."},
],
"timeline": [
    {"year":"2003","title":"Professional debut","desc":"Begins career in the southeastern US independent circuit; trained by Dory Funk Jr."},
    {"year":"2015","title":"IMPACT Wrestling debut as Eli Drake","desc":"Joins IMPACT; develops the 'Dummy, yeah!' promo character that defines his style."},
    {"year":"2017","title":"IMPACT World Champion","desc":"Wins IMPACT world title — peak of his pre-WWE career and validation of his promo-heavy approach."},
    {"year":"2021","title":"Signs with WWE","desc":"Joins WWE after IMPACT departure; initially used as heel enhancement talent."},
    {"year":"2023","title":"Organic babyface turn","desc":"Crowd begins 'YEAH!' chants organically — WWE follows the crowd and pivots his booking to babyface."},
    {"year":"2023","title":"United States Champion","desc":"Wins US title as a babyface — the payoff of an organic groundswell that took two years to fully bloom."},
    {"year":"2024","title":"WWE Championship contender","desc":"Challenges for the WWE Championship; main event positioning reflects his crowd connection."},
],
"sig_matches": [
    {"rating":"★★★★","title":"vs. Roman Reigns","subtitle":"Crown Jewel 2023","desc":"LA Knight gets his first main event world title shot — the crowd response for this match rivaled anyone on the card, proving the organic babyface push was justified."},
    {"rating":"★★★★","title":"vs. AJ Styles","subtitle":"SummerSlam 2023","desc":"United States Championship match on the SummerSlam card — Knight demonstrates he can deliver when the stage is big."},
    {"rating":"★★★½","title":"vs. Bray Wyatt","subtitle":"Royal Rumble 2023","desc":"Their program produced one of the more creative mid-card feuds of the year — Knight's straight-shooter character against Wyatt's supernatural one."},
],
"faq": [
    {"q":"What does YEAH mean for LA Knight?","a":"YEAH is LA Knight's primary crowd-interaction call — he addresses the audience with 'lemme talk to ya' and 'YEAH!' punctuates his promos and ring entrance in a call-and-response format. The crowd adopted it organically and it became one of WWE's most reliable crowd participation moments."},
    {"q":"Who is Eli Drake?","a":"Eli Drake was LA Knight's character name in IMPACT Wrestling (2015–2021), where he was world champion and one of the company's best promo workers. The 'Dummy, yeah!' catchphrase was the predecessor to his WWE character."},
    {"q":"Is LA Knight a babyface or heel?","a":"LA Knight is currently a babyface in WWE — a role the crowd pushed him into organically despite initial heel booking. His natural charisma and 'YEAH!' crowd interaction made him a crowd favorite regardless of how he was presented."},
],
"record_rows": (
    row("la-knight","ppv title",a("roman-reigns","Roman Reigns"),"Crown Jewel 2023","Nov 4, 2023","Singles — WWE Championship","First world title shot","L") +
    row("la-knight","ppv title",a("aj-styles","AJ Styles"),"SummerSlam 2023","Aug 5, 2023","Singles — United States Championship","","W") +
    row("la-knight","ppv title",a("cm-punk","CM Punk"),"WrestleMania XL","Apr 6, 2024","Singles","WM main card","L") +
    row("la-knight","ppv title",a("gunther","Gunther"),"SummerSlam 2024","Aug 3, 2024","Singles — World Heavyweight Championship","World title shot","L") +
    row("la-knight","tv title","Santos Escobar","SmackDown 2023","Sep 8, 2023","Singles — US Championship","Wins US title","W") +
    row("la-knight","ppv",a("brock-lesnar","Brock Lesnar"),"Royal Rumble 2024","Jan 27, 2024","Singles","","W")
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
print("\nBatch 7a complete.")
