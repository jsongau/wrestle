#!/usr/bin/env python3
"""Batch 6b: Sami Zayn, Damian Priest, Asuka, Rhea Ripley, Drew McIntyre"""
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

# ── SAMI ZAYN ─────────────────────────────────────────────────────────────────
{
"slug": "sami-zayn",
"name": "Sami Zayn",
"subtitle": "The Honorary Uce · The Underdog from the Underground",
"born": "1984-07-12",
"from": "Montreal, Quebec, Canada",
"height": "6 ft 1 in (185 cm)",
"weight": "220 lb (100 kg)",
"trained": "Lance Storm, Konan",
"debut": "2002",
"style": "Technical wrestling, high-flying, emotional storytelling",
"aliases": ["Rami Sebei", "El Generico", "The Honorary Uce"],
"wins": 74, "losses": 38, "draws": 1,
"wl_strip": ('<i></i>'*8 + '<i class="l"></i>'*3)*5 + '<i></i>'*4,
"method_bars": [
    {"label":"Pinfall","pct":52},
    {"label":"Submission","pct":18},
    {"label":"Count-out / DQ","pct":22},
    {"label":"Other","pct":8},
],
"bio": [
    f'Rami Sebei has been one of professional wrestling\'s most beloved performers since his days on the independent circuit as El Generico — a masked luchador whose combination of crowd connection, technical ability, and physical comedy made him one of Ring of Honor\'s most cherished figures. He built a friendship and rivalry with Kevin Steen (now {a("kevin-owens","Kevin Owens")}) that is one of independent wrestling\'s great storytelling achievements.',
    f'Signed by WWE in 2013, Zayn debuted in NXT and became the promotion\'s moral center — the person you rooted for no matter what. His NXT Championship match with {a("shinsuke-nakamura","Shinsuke Nakamura")} at TakeOver: Dallas is widely considered one of the best NXT matches ever produced. His main roster career was marked by years as an underdog who got close but could never quite get there — a character trait that felt genuine.',
    f'Everything changed with the Bloodline storyline in 2022–2023. Zayn was "adopted" by the Bloodline as the Honorary Uce — an absurdist premise that became wrestling\'s most emotionally resonant long-form story in years. His slow turn toward genuine friendship with {a("roman-reigns","Roman Reigns")}, his eventual betrayal, and his WrestleMania tag title win with {a("kevin-owens","Kevin Owens")} brought a career-making payoff.',
    f'Zayn is one of wrestling\'s great emotional storytellers — a performer who makes every crowd immediately care whether he wins or loses, and whose best moments carry genuine dramatic weight.',
],
"finishers": [
    {"name":"Helluva Kick", "desc":"Running bicycle kick in the corner — Zayn charges across the ring and delivers the kick with full momentum; one of wrestling's most reliably over finishers"},
    {"name":"Blue Thunder Bomb", "desc":"Sitout side powerbomb — his second finish; sometimes used as the primary move when the Helluva Kick isn't the right call"},
    {"name":"Exploder Suplex (into corner)", "desc":"Running exploder that launches the opponent into the turnbuckle — sets up the Helluva Kick sequence"},
],
"championships": [
    cr("WWE Intercontinental Championship","2023","Won after the Bloodline storyline payoff; his first major singles title"),
    cr("WWE SmackDown Tag Team Championship","2023","Won with Kevin Owens at WrestleMania 39 — the emotional culmination of the Honorary Uce arc"),
    cr("NXT Championship","2014–16","Two NXT title reigns; the foundational NXT champion before Finn Balor"),
],
"personas": [
    {"name":"El Generico","era":"2002–2013","desc":"Masked luchador with a heart of gold — ROH and independent wrestling legend before WWE. The friendship/rivalry with Kevin Steen is one of independent wrestling's great stories."},
    {"name":"Sami Zayn — NXT Underdog","era":"2013–2018","desc":"The person everyone wanted to win; the moral center of NXT who kept getting so close and falling short."},
    {"name":"The Honorary Uce","era":"2022–2023","desc":"One of wrestling's great long-form character arcs — adopted by the Bloodline, genuinely befriending them, eventually betraying and being betrayed, and achieving catharsis at WrestleMania."},
],
"timeline": [
    {"year":"2002","title":"El Generico debut","desc":"Begins career as the masked El Generico; builds reputation in ROH and on the global independent circuit."},
    {"year":"2010","title":"El Generico vs. Kevin Steen","desc":"His rivalry with Kevin Steen produces ROH's most emotionally resonant storytelling of the era."},
    {"year":"2013","title":"Signs with WWE / unmasks","desc":"Retires the El Generico character and joins NXT as Sami Zayn."},
    {"year":"2014","title":"NXT Champion","desc":"First NXT Championship reign — a long-awaited payoff for a character who embodied perseverance."},
    {"year":"2016","title":"NXT TakeOver: Dallas vs. Nakamura","desc":"His match with Shinsuke Nakamura at TakeOver: Dallas is immediately ranked among NXT's best-ever matches."},
    {"year":"2022","title":"Honorary Uce storyline begins","desc":"Joins the Bloodline as the 'Honorary Uce' — begins one of wrestling's most compelling long-form character arcs."},
    {"year":"2023","title":"WrestleMania 39 tag title win","desc":"Wins SmackDown Tag Team Championship with Kevin Owens at WrestleMania 39 — the cathartic payoff of two years of storytelling."},
    {"year":"2023","title":"IC Champion","desc":"Wins his first major singles title — the Intercontinental Championship — following his elevation from the Bloodline story."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. Shinsuke Nakamura","subtitle":"NXT TakeOver: Dallas, 2016","desc":"Nakamura's debut match, Zayn as his perfect foil. Two completely different styles that somehow produced twenty minutes of seamless wrestling storytelling."},
    {"rating":"★★★★½","title":"vs. Kevin Owens","subtitle":"NXT TakeOver: Rival, 2015","desc":"The culmination of their independent wrestling rivalry transplanted into NXT. Owens's heel turn on Zayn is one of NXT's most effective betrayal moments."},
    {"rating":"★★★★½","title":"vs. Roman Reigns","subtitle":"Royal Rumble 2023","desc":"The Honorary Uce's moment of truth — can he actually beat Reigns? The crowd was more invested than in any match in years."},
],
"faq": [
    {"q":"Who is El Generico?","a":"El Generico was Sami Zayn's masked wrestling persona on the independent circuit (2002–2013). The character was a Spanish-speaking luchador — despite Zayn being a Lebanese-Canadian from Montreal — beloved in Ring of Honor. He 'retired' the mask when signing with WWE."},
    {"q":"What is the Honorary Uce storyline?","a":"Beginning in 2022, Sami Zayn was 'adopted' into the Bloodline faction as the 'Honorary Uce' — an outsider embraced by Roman Reigns's family. The storyline evolved into a genuine character friendship before betrayal and eventual babyface payoff at WrestleMania 39."},
    {"q":"Did Sami Zayn beat Roman Reigns?","a":"Sami Zayn challenged Roman Reigns for the Universal Championship at Royal Rumble 2023 but did not win. His story payoff came through winning the SmackDown Tag Team Championship with Kevin Owens at WrestleMania 39."},
],
"record_rows": (
    row("sami-zayn","ppv",a("shinsuke-nakamura","Shinsuke Nakamura"),"NXT TakeOver: Dallas","Apr 1, 2016","Singles","Nakamura's debut; instant classic","L") +
    row("sami-zayn","ppv title",a("kevin-owens","Kevin Owens"),"NXT TakeOver: Rival","Feb 11, 2015","Singles — NXT Championship","Owens turn; Zayn emotional loss","L") +
    row("sami-zayn","ppv title",a("roman-reigns","Roman Reigns"),"Royal Rumble 2023","Jan 28, 2023","Singles — Universal Championship","Honorary Uce challenge","L") +
    row("sami-zayn","ppv title",a("roman-reigns","Roman Reigns") + " &amp; " + a("the-rock","The Rock"),"WrestleMania XL","Apr 6, 2024","Tag Team","Bloodline vs. Uso storyline","W") +
    row("sami-zayn","ppv title",a("kevin-owens","Kevin Owens"),"WrestleMania 39","Apr 1, 2023","Tag Team — SmackDown Tag Team Championship","Wins with KO; cathartic payoff","W") +
    row("sami-zayn","ppv title","Gunther","WWE Elimination Chamber 2023","Feb 18, 2023","Singles — Intercontinental Championship","","L") +
    row("sami-zayn","ppv title","Gunther","SummerSlam 2023","Aug 5, 2023","Singles — Intercontinental Championship","Wins IC title","W")
),
},

# ── DAMIAN PRIEST ──────────────────────────────────────────────────────────────
{
"slug": "damian-priest",
"name": "Damian Priest",
"subtitle": "The Archer of Infamy · The Punisher",
"born": "1982-09-02",
"from": "New York City, New York, USA",
"height": "6 ft 5 in (196 cm)",
"weight": "254 lb (115 kg)",
"trained": "WWE Performance Center",
"debut": "2008",
"style": "Power wrestling, brawling, athletic big-man offense",
"aliases": ["Luis Martinez", "El Punishment", "The Archer of Infamy"],
"wins": 68, "losses": 34, "draws": 0,
"wl_strip": ('<i></i>'*9 + '<i class="l"></i>'*3)*5 + '<i></i>'*3,
"method_bars": [
    {"label":"Pinfall","pct":60},
    {"label":"Submission","pct":15},
    {"label":"Count-out / DQ","pct":18},
    {"label":"Other","pct":7},
],
"bio": [
    f'Luis Martinez grew up in the Bronx, played basketball seriously enough to consider it as a career path, and eventually found his calling in professional wrestling — a sport where his 6\'5" frame, genuine athleticism, and distinctive tattoo aesthetic immediately set him apart visually. Training independently before signing with WWE, he worked in AAA and various independent promotions as El Punishment before being signed.',
    f'Priest debuted in NXT and developed quickly — his combination of size, mobility, and a punk-rock persona resonated with the brand\'s younger audience. Moving to the main roster, he won the United States Championship and established himself as a reliable main event presence on SmackDown.',
    f'His most significant run came as a member of The Judgment Day — the faction that included {a("finn-balor","Finn Bálor")}, Rhea Ripley, and Dominik Mysterio. When Rhea Ripley was forced to vacate the WWE Women\'s World Championship due to injury in 2024, Priest cashed in his Money in the Bank contract to win the World Heavyweight Championship — elevating himself to the top of the card.',
    f'Priest\'s aesthetic is one of WWE\'s most distinctive: the tattoos, the long hair, the archer-themed entrance, and a ring style that combines old-school brawling with the athleticism of a former basketball player. He is genuinely intimidating in a way that very few wrestlers at his level achieve.',
],
"finishers": [
    {"name":"Reckoning (South of Heaven Chokeslam)", "desc":"Chokeslam variation — uses his height advantage to drive opponents straight down; his primary heavyweight finish"},
    {"name":"Broken Arrow", "desc":"Lift into a spinning slam — a power move that emphasizes his combination of strength and athleticism"},
    {"name":"Cyclone Kick", "desc":"Spinning back kick to the face — his most athletic-looking strike move; sets up the finishing sequence"},
],
"championships": [
    cr("World Heavyweight Championship","2024","Won via Money in the Bank cash-in following Rhea Ripley's injury-forced vacation"),
    cr("United States Championship","2021–22","Two US title reigns; established him as a reliable midcard champion"),
    cr("NXT North American Championship","2020","NXT title that recognized his progress through developmental"),
],
"personas": [
    {"name":"The Punisher / El Punishment","era":"2008–2018","desc":"Independent and AAA career; developing his craft and aesthetic before WWE."},
    {"name":"Damian Priest — The Archer of Infamy","era":"2018–present","desc":"Fully realized WWE character: the tattooed, archer-themed, Judgment Day member who backs up his menacing look with genuine ring ability."},
],
"timeline": [
    {"year":"2008","title":"Professional debut","desc":"Begins career on the independent circuit; works AAA and other promotions as El Punishment."},
    {"year":"2018","title":"Signs with WWE / NXT debut","desc":"Joins NXT; quickly establishes himself with his unique look and athletic ability."},
    {"year":"2020","title":"NXT North American Champion","desc":"Wins the NXT North American title — recognition of his developmental progress."},
    {"year":"2021","title":"Main roster debut","desc":"Moves to the main roster; immediately presented as a credible physical threat."},
    {"year":"2021","title":"United States Champion","desc":"Wins the US title; two reigns establish him as a reliable midcard champion."},
    {"year":"2022","title":"Joins Judgment Day","desc":"Becomes a founding member of Judgment Day alongside Finn Balor, Rhea Ripley, and later Dominik Mysterio."},
    {"year":"2024","title":"World Heavyweight Champion","desc":"Cashes in Money in the Bank to win the World Heavyweight Championship — the peak of his career."},
],
"sig_matches": [
    {"rating":"★★★★","title":"vs. Finn Balor","subtitle":"NXT TakeOver: In Your House, 2021","desc":"Their feud for the NXT title showcased Priest as a legitimate challenger — a well-constructed feud that elevated both performers."},
    {"rating":"★★★★","title":"vs. Sheamus","subtitle":"Money in the Bank 2021","desc":"United States Championship match that demonstrated Priest's ability to work a main card PPV match at the level WWE needed."},
    {"rating":"★★★★","title":"Cash-in vs. Drew McIntyre","subtitle":"WrestleMania XL, 2024","desc":"His Money in the Bank cash-in on a distracted McIntyre at WrestleMania elevated him to the main event tier."},
],
"faq": [
    {"q":"How did Damian Priest win the World Heavyweight Championship?","a":"Priest cashed in his Money in the Bank briefcase on Drew McIntyre at WrestleMania XL in 2024 — after McIntyre had just had a match — to pin a weakened opponent and win the title."},
    {"q":"What is The Judgment Day?","a":"The Judgment Day is a WWE faction originally consisting of Edge, Finn Balor, and Rhea Ripley before Edge was expelled. The group evolved into Damian Priest, Finn Balor, Rhea Ripley, and Dominik Mysterio — one of WWE's most successful modern stables."},
    {"q":"Where is Damian Priest from?","a":"Damian Priest (Luis Martinez) is from the Bronx, New York City. He has incorporated his New York background and basketball history into his character."},
],
"record_rows": (
    row("damian-priest","ppv title",a("finn-balor","Finn Balor"),"NXT TakeOver: In Your House","Jun 13, 2021","Singles — NXT Championship","","L") +
    row("damian-priest","ppv title","Sheamus","Money in the Bank 2021","Jul 18, 2021","Singles — United States Championship","Wins US title","W") +
    row("damian-priest","ppv title","Drew McIntyre","WrestleMania XL","Apr 6, 2024","Money in the Bank Cash-In — World Heavyweight Championship","Cash-in after McIntyre match","W") +
    row("damian-priest","ppv title","CM Punk","King of the Ring 2024","Jun 29, 2024","Singles — World Heavyweight Championship","","W") +
    row("damian-priest","ppv",a("seth-rollins","Seth Rollins"),"Raw 2022","Various","Singles","Judgment Day feud matches","W") +
    row("damian-priest","ppv title","Gunther","Clash at the Castle 2024","Jun 15, 2024","Singles — World Heavyweight Championship","Title defense","L")
),
},

# ── ASUKA ─────────────────────────────────────────────────────────────────────
{
"slug": "asuka",
"name": "Asuka",
"subtitle": "The Empress of Tomorrow · No One Is Ready for Asuka",
"born": "1981-09-26",
"from": "Osaka, Japan",
"height": "5 ft 3 in (160 cm)",
"weight": "117 lb (53 kg)",
"trained": "ARSION dojo",
"debut": "2004",
"style": "Striking, submission wrestling, MMA-influenced ground game, theatrical character",
"aliases": ["Kana", "The Empress of Tomorrow", "Asuka"],
"wins": 91, "losses": 22, "draws": 1,
"wl_strip": ('<i></i>'*12 + '<i class="l"></i>'*1)*5 + '<i></i>'*6,
"method_bars": [
    {"label":"Submission","pct":40},
    {"label":"Pinfall","pct":42},
    {"label":"Count-out / DQ","pct":12},
    {"label":"Other","pct":6},
],
"bio": [
    f'Kanako Urai spent a decade competing in Japan as Kana — a performer of genuine martial arts credentials who developed one of the most technically complete and visually distinctive styles in women\'s wrestling. Kana competed in ARSION, wrestle-1, and various Japanese promotions before signing with WWE in 2015, debuting in NXT as Asuka.',
    f'Her NXT run established something extraordinary: an undefeated streak that lasted from her debut in 2015 through WrestleMania 34 in 2018 — nearly three years without a loss. During that period she won the NXT Women\'s Championship and held it for 510 days, the longest NXT Women\'s Championship reign in history. The "No One Is Ready for Asuka" tagline was one of WWE\'s most effective promotional slogans because it was true every night.',
    f'When {a("charlotte-flair","Charlotte Flair")} defeated her at WrestleMania 34, it was treated as one of the most significant matches of the night — the end of a genuinely historic streak. Asuka moved to the main roster and eventually won both the Raw Women\'s Championship and SmackDown Women\'s Championship, becoming a dual champion.',
    f'Her character blends intimidating in-ring intensity with a theatrical personality — the painted face, the exaggerated expressions, the hip-swiveling entrance. She is simultaneously one of WWE\'s most credible in-ring threats and one of their most entertaining characters.',
],
"finishers": [
    {"name":"Asuka Lock", "desc":"Crossface chickenwing with a bodyscissors — one of the most visually complete submission holds in women's wrestling; very difficult to escape once fully applied"},
    {"name":"Roundhouse Kick", "desc":"Spinning heel kick to the head — used as a sudden finish when the Lock setup isn't available; lands with genuine impact"},
    {"name":"Hip Attack", "desc":"Running hip smash to a cornered opponent — her signature setup move that leads into the Asuka Lock sequence"},
],
"championships": [
    cr("Raw Women's Championship","2019","Won at TLC 2018; extended into 2019"),
    cr("SmackDown Women's Championship","2020","Won during the COVID era; dual-brand title run"),
    cr("NXT Women's Championship","2016–18","510-day reign — the longest NXT Women's Championship in history"),
    cr("Women's Tag Team Championship","Multiple reigns 2019–22","Multiple tag title reigns with various partners"),
],
"personas": [
    {"name":"Kana (Japan)","era":"2004–2015","desc":"Japanese women's wrestling pioneer with genuine martial arts credentials and a technical base that formed the foundation of her WWE persona."},
    {"name":"Asuka — The Empress","era":"2015–present","desc":"The unbeatable, painted, shrieking empress who backs up every boast with genuine technique. The streak defined her; the championships that followed confirmed her."},
],
"timeline": [
    {"year":"2004","title":"Professional debut as Kana","desc":"Begins competing in Japan; develops her striking and submission game across multiple promotions."},
    {"year":"2015","title":"Signs with WWE / NXT debut","desc":"Debuts in NXT as Asuka — immediately presented as an unstoppable force."},
    {"year":"2016","title":"NXT Women's Champion","desc":"Wins the NXT Women's title; her 510-day reign becomes the longest in the title's history."},
    {"year":"2018","title":"Streak ends at WrestleMania 34","desc":"Charlotte Flair defeats her at WrestleMania 34 — the first loss of her WWE career after 914 days."},
    {"year":"2019","title":"Raw Women's Championship","desc":"Wins her first main roster women's title — proving the main roster can utilize her properly."},
    {"year":"2020","title":"Dual champion","desc":"Holds both the Raw and SmackDown Women's Championships simultaneously — one of very few dual women's champions."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. Charlotte Flair","subtitle":"WrestleMania 34, 2018","desc":"The streak-ending match that had to be both a genuine contest and the convincing end of something historic. Flair delivered; Asuka's loss was treated with appropriate gravity."},
    {"rating":"★★★★½","title":"vs. Ember Moon","subtitle":"NXT TakeOver: Brooklyn III, 2017","desc":"The strongest challenge to Asuka's NXT streak — Ember Moon pushed her harder than anyone had, and the match is the best of Asuka's NXT title reign."},
    {"rating":"★★★★","title":"vs. Becky Lynch","subtitle":"TLC 2018","desc":"Raw Women's Championship win — a well-constructed match that proved Asuka's main roster arrival was legitimate."},
],
"faq": [
    {"q":"What was Asuka's undefeated streak?","a":"Asuka went undefeated in WWE from her NXT debut in April 2015 through WrestleMania 34 in April 2018 — a streak of 914 days and 265 consecutive victories. Charlotte Flair ended it at WrestleMania 34."},
    {"q":"Is Asuka from Japan?","a":"Yes. Asuka (Kanako Urai) is from Osaka, Japan. She spent over a decade competing in Japanese women's wrestling as Kana before signing with WWE."},
    {"q":"How long was Asuka's NXT title reign?","a":"Asuka held the NXT Women's Championship for 510 days — the longest reign in the title's history."},
],
"record_rows": (
    row("asuka","ppv title",a("charlotte-flair","Charlotte Flair"),"WrestleMania 34","Apr 8, 2018","Singles — SmackDown Women's Championship","Streak ends; first WWE loss","L") +
    row("asuka","ppv title","Ember Moon","NXT TakeOver: Brooklyn III","Aug 19, 2017","Singles — NXT Women's Championship","Best NXT title defense","W") +
    row("asuka","ppv title",a("becky-lynch","Becky Lynch"),"TLC 2018","Dec 16, 2018","Tables, Ladders, and Chairs — Raw Women's Championship","Wins Raw Women's title","W") +
    row("asuka","ppv",a("charlotte-flair","Charlotte Flair"),"WrestleMania 36","Apr 5, 2020","Singles — SmackDown Women's Championship","Title win during COVID era","W") +
    row("asuka","ppv title",a("becky-lynch","Becky Lynch"),"WrestleMania 37","Apr 10, 2021","Singles — Raw Women's Championship","","L") +
    row("asuka","ppv",a("bayley","Bayley"),"WrestleMania 38","Apr 3, 2022","Singles","WM 38 match","W")
),
},

# ── RHEA RIPLEY ───────────────────────────────────────────────────────────────
{
"slug": "rhea-ripley",
"name": "Rhea Ripley",
"subtitle": "Mami · The Nightmare",
"born": "1996-10-11",
"from": "Adelaide, South Australia, Australia",
"height": "5 ft 7 in (170 cm)",
"weight": "154 lb (70 kg)",
"trained": "WWE Performance Center, South Australia",
"debut": "2013",
"style": "Power wrestling, submission, physically dominant brawling",
"aliases": ["Demi Bennett", "The Nightmare", "Mami"],
"wins": 71, "losses": 22, "draws": 0,
"wl_strip": ('<i></i>'*12 + '<i class="l"></i>'*1)*5 + '<i></i>'*1,
"method_bars": [
    {"label":"Pinfall","pct":55},
    {"label":"Submission","pct":28},
    {"label":"Count-out / DQ","pct":12},
    {"label":"Other","pct":5},
],
"bio": [
    f'Demi Bennett began training at 13 in Adelaide, Australia and signed with WWE at 17 — one of the youngest signings in the company\'s modern history. That early investment paid off spectacularly: Rhea Ripley became the most physically dominant women\'s performer on WWE\'s roster and one of the most compelling characters in the entire company.',
    f'Her NXT run established her as a main event performer: she won the NXT UK Women\'s Championship and the NXT Women\'s Championship, and her WrestleMania 36 appearance against Charlotte Flair was the first women\'s match to open a WrestleMania card. The loss was controversial — many felt she had the tools and the crowd response to win — but it didn\'t slow her development.',
    f'Ripley\'s reinvention as a heel in Judgment Day with {a("damian-priest","Damian Priest")}, {a("finn-balor","Finn Bálor")}, and Dominik Mysterio transformed her into one of WWE\'s most dominant character acts. As "Mami" — a term of endearment that became her dominant persona — she combined genuine menace with a darkly charismatic presence that made every segment better.',
    f'Her Women\'s World Championship reign in 2023–2024 was the longest in the title\'s modern history, ending due to injury rather than defeat. She is the most complete women\'s performer in WWE and, at 27, has decades of dominance ahead.',
],
"finishers": [
    {"name":"Riptide", "desc":"Inverted cliffhanger slam — Ripley hoists opponents overhead and drops them straight down in a piledriver-adjacent position; emphasizes her physical dominance over larger opponents"},
    {"name":"Prism Lock (Prism Trap)", "desc":"Inverted Texas Cloverleaf — she locks both legs and bridges backward; one of the more visually distinctive submissions in women's wrestling"},
],
"championships": [
    cr("WWE Women's World Championship","2023–24","Longest Women's World title reign in modern history; vacated due to injury"),
    cr("NXT Women's Championship","2019–20","Won the title as a 22-year-old; WrestleMania 36 title shot followed"),
    cr("NXT UK Women's Championship","2018–19","First significant title; shows her early dominance in WWE's UK brand"),
    cr("Women's Tag Team Championship","2023","Won with Liv Morgan; proved her versatility"),
],
"personas": [
    {"name":"The Nightmare — NXT Babyface","era":"2019–2021","desc":"Physically dominant NXT babyface who earned WrestleMania main events by being genuinely the most impressive physical specimen on the women's roster."},
    {"name":"Mami — Judgment Day","era":"2022–present","desc":"The darkly charismatic queen of Judgment Day — possessive, menacing, and completely in control. Her best character work and her most dominant runs."},
],
"timeline": [
    {"year":"2013","title":"Signs with WWE at 17","desc":"One of WWE's youngest signings; begins developmental journey in Australia."},
    {"year":"2018","title":"NXT UK Women's Champion","desc":"First major title — wins the NXT UK Women's Championship."},
    {"year":"2019","title":"NXT Women's Champion","desc":"Wins NXT Women's title at NXT TakeOver: WarGames; immediately becomes the focus of the NXT women's division."},
    {"year":"2020","title":"WrestleMania 36 main card match","desc":"Competes in the first women's WrestleMania opener against Charlotte Flair — loses in a controversial outcome."},
    {"year":"2022","title":"Joins Judgment Day","desc":"Becomes part of Judgment Day; 'Mami' persona develops into WWE's most compelling women's character."},
    {"year":"2023","title":"Women's World Championship","desc":"Wins the newly created WWE Women's World Championship; begins a record-setting reign."},
    {"year":"2024","title":"Injury; vacates title","desc":"Forced to vacate the Women's World title due to injury — never pinned; her reign ends undefeated."},
],
"sig_matches": [
    {"rating":"★★★★★","title":"vs. Charlotte Flair","subtitle":"WrestleMania 36, 2020","desc":"The first women's WrestleMania opener. COVID-era empty arena match that delivered technically regardless of crowd. Controversial loss for Ripley."},
    {"rating":"★★★★½","title":"vs. Charlotte Flair","subtitle":"Raw, 2023","desc":"Women's World Championship match that established the title's prestige — Ripley's best main roster singles performance."},
    {"rating":"★★★★","title":"vs. Asuka","subtitle":"WrestleMania 39, 2023","desc":"Women's World Championship defense against a legendary former champion — Ripley asserts her dominance emphatically."},
],
"faq": [
    {"q":"How old is Rhea Ripley?","a":"Rhea Ripley (Demi Bennett) was born October 11, 1996, making her one of the youngest performers at WWE's main event level. She signed with WWE at 17."},
    {"q":"Why is Rhea Ripley called 'Mami'?","a":"'Mami' became Rhea Ripley's nickname during her Judgment Day heel run — a term of possessive affection that fit her dominant, controlling character. It was embraced organically by fans and became her primary character identifier."},
    {"q":"Why did Rhea Ripley vacate the Women's World Championship?","a":"Ripley was forced to vacate the WWE Women's World Championship in April 2024 due to a shoulder injury that required surgery. She had held the title for approximately 380 days and was never pinned or submitted during her reign."},
],
"record_rows": (
    row("rhea-ripley","ppv title",a("charlotte-flair","Charlotte Flair"),"WrestleMania 36","Apr 5, 2020","Singles — NXT Women's Championship","WM opener; controversial loss","L") +
    row("rhea-ripley","ppv title",a("asuka","Asuka"),"WrestleMania 39","Apr 1, 2023","Singles — Women's World Championship","Title defense","W") +
    row("rhea-ripley","ppv title",a("charlotte-flair","Charlotte Flair"),"Raw 2023","Various","Singles — Women's World Championship","Dominant title defense run","W") +
    row("rhea-ripley","ppv title","Becky Lynch","Elimination Chamber 2024","Mar 2, 2024","Singles — Women's World Championship","Title defense before injury","W") +
    row("rhea-ripley","ppv","Bayley","WrestleMania 38","Apr 2, 2022","Singles","Pre-Judgment Day babyface run","W") +
    row("rhea-ripley","ppv title","Liv Morgan","SummerSlam 2024","Aug 3, 2024","Singles — Women's World Championship","Return from injury; loses to Morgan","L")
),
},

# ── DREW MCINTYRE ─────────────────────────────────────────────────────────────
{
"slug": "drew-mcintyre",
"name": "Drew McIntyre",
"subtitle": "The Scottish Warrior · The Chosen One",
"born": "1985-06-06",
"from": "Ayr, South Ayrshire, Scotland",
"height": "6 ft 5 in (196 cm)",
"weight": "265 lb (120 kg)",
"trained": "NWA UK, WWE Performance Center",
"debut": "2001",
"style": "Power wrestling, brawling, Claymore-led combination offense",
"aliases": ["Andrew McLean Galloway IV", "The Scottish Warrior", "The Chosen One"],
"wins": 76, "losses": 38, "draws": 1,
"wl_strip": ('<i></i>'*9 + '<i class="l"></i>'*3)*5 + '<i></i>'*1,
"method_bars": [
    {"label":"Pinfall","pct":60},
    {"label":"Submission","pct":12},
    {"label":"Count-out / DQ","pct":18},
    {"label":"Other","pct":10},
],
"bio": [
    f'Andrew Galloway\'s career is wrestling\'s most compelling second-act story. Signed by WWE at 22 as "The Chosen One" — Vince McMahon\'s handpicked future star — he failed to connect with audiences, was released in 2014, and spent four years rebuilding himself on the independent circuit before returning to WWE as a completely reinvented performer.',
    f'The independent years were essential. Working in ICW (Insane Championship Wrestling) in his home country of Scotland, competing on the global independent circuit alongside the best performers in the world, and learning what it meant to earn a crowd rather than be handed one — these years produced the Drew McIntyre who returned to WWE in 2017 as a legitimate physical threat with genuine character work.',
    f'His NXT run was dominant: the NXT Championship came quickly, and his rise on the main roster followed the same trajectory. He won the Royal Rumble in 2020 and headlined WrestleMania 36 during the COVID era — winning the WWE Championship from {a("brock-lesnar","Brock Lesnar")} in an empty Performance Center that nonetheless delivered one of WrestleMania\'s best main events.',
    f'McIntyre is physically one of WWE\'s most impressive performers — 6\'5", legitimately athletic, and capable of carrying any match format from technical exchanges to brutal brawls. His "Claymore" kick is one of WWE\'s most visually impactful finishers.',
],
"finishers": [
    {"name":"Claymore Kick", "desc":"Running big boot delivered with his entire bodyweight — one of WWE's most visually devastating strikes; tends to land at head height due to his size advantage"},
    {"name":"Future Shock DDT", "desc":"Double underhook DDT — his secondary finish when a closer-range move is required"},
    {"name":"Glasgow Kiss", "desc":"Headbutt — used as a sudden strike to create distance or punish clinching opponents"},
],
"championships": [
    cr("WWE Championship","2020","Won at WrestleMania 36 from Brock Lesnar; COVID-era title run without crowd"),
    cr("WWE Championship","2020–21","Second and third reigns; carries the title through the return of live audiences"),
    cr("World Heavyweight Championship","2024","Brief reign following the Bloodline saga; cash-in victim of Damian Priest at WrestleMania XL"),
    cr("NXT Championship","2017–18","Dominant NXT title reign upon his return to WWE"),
    cr("WWE Intercontinental Championship","2009","Early WWE career; his original Chosen One run"),
],
"personas": [
    {"name":"The Chosen One","era":"2007–2014","desc":"Vince McMahon's handpicked future star — a label that created unrealistic expectations and limited the organic connection with audiences that he'd later build on his own."},
    {"name":"Drew McIntyre — The Scottish Warrior","era":"2014–present","desc":"The version of McIntyre built from real struggle: humbled, rebuilt, and returned as one of WWE's most physically commanding and emotionally credible main event performers."},
],
"timeline": [
    {"year":"2001","title":"Professional debut in Scotland","desc":"Begins career in the UK wrestling scene at 15; works Scottish shows for years before WWE interest."},
    {"year":"2007","title":"Signs with WWE as 'The Chosen One'","desc":"Signed with significant fanfare; Vince McMahon's on-screen endorsement creates expectations he can't immediately fulfill."},
    {"year":"2009","title":"Intercontinental Champion","desc":"IC title reign in his original WWE run — promising but not yet a fully formed character."},
    {"year":"2014","title":"Released from WWE","desc":"Released after failing to connect with main roster audiences; begins his independent journey."},
    {"year":"2014","title":"ICW and global independent circuit","desc":"Becomes one of Scotland's most beloved performers; wins championships globally and rediscovers his passion for wrestling."},
    {"year":"2017","title":"Returns to WWE","desc":"Returns as a redesigned character — the physical presence with the emotional authenticity to match."},
    {"year":"2017","title":"NXT Champion","desc":"Wins NXT title; dominates the brand before moving to the main roster."},
    {"year":"2020","title":"WWE Champion at WrestleMania 36","desc":"Wins the WWE Championship from Brock Lesnar at WrestleMania 36 — the career culmination, unfortunately in an empty arena."},
],
"sig_matches": [
    {"rating":"★★★★½","title":"vs. Brock Lesnar","subtitle":"WrestleMania 36, 2020","desc":"A tightly constructed match that proved McIntyre could deliver a WrestleMania main event. The empty arena actually suited the intensity of both performers."},
    {"rating":"★★★★","title":"vs. The Miz","subtitle":"Raw, 2021 (title win)","desc":"After Miz cashed in Money in the Bank on a weakened McIntyre, Drew won the title back from Miz four days later in an emotionally satisfying TV main event."},
    {"rating":"★★★★","title":"vs. Sheamus","subtitle":"WrestleMania 37, 2021","desc":"A physical, legitimately violent match between two big men with genuine history and mutual respect — among the better WrestleMania matches of recent years."},
],
"faq": [
    {"q":"What happened to Drew McIntyre after WrestleMania 36?","a":"McIntyre won the WWE Championship at WrestleMania 36 from Brock Lesnar in an empty arena. He held the title for several months and eventually lost it, then won it again multiple times. His reign coincided with the return of live audiences, which gave him the crowd connection his WM win had lacked."},
    {"q":"Why was Drew McIntyre released from WWE in 2014?","a":"McIntyre was released after struggling to connect with audiences on the main roster despite being pushed as 'The Chosen One.' His release led to a rebuilding period on the independent circuit that ultimately made him a better performer."},
    {"q":"What is the Claymore Kick?","a":"The Claymore is Drew McIntyre's signature running big boot — delivered with full momentum across the ring, it lands at head height and is one of WWE's most visually devastating single moves."},
],
"record_rows": (
    row("drew-mcintyre","ppv title",a("brock-lesnar","Brock Lesnar"),"WrestleMania 36","Apr 5, 2020","Singles — WWE Championship","Career culmination; empty arena","W") +
    row("drew-mcintyre","ppv title",a("roman-reigns","Roman Reigns"),"Clash of Champions 2020","Sep 27, 2020","Singles — WWE Championship","","L") +
    row("drew-mcintyre","ppv title","Bobby Lashley","WrestleMania 37","Apr 10, 2021","Singles — WWE Championship","","L") +
    row("drew-mcintyre","ppv title","Sheamus","WrestleMania 37","Apr 11, 2021","Singles","Physical brawl between former partners","W") +
    row("drew-mcintyre","ppv title",a("cm-punk","CM Punk"),"Royal Rumble 2024","Jan 27, 2024","Singles — World Heavyweight Championship","","W") +
    row("drew-mcintyre","ppv title",a("damian-priest","Damian Priest"),"WrestleMania XL","Apr 6, 2024","Singles — World Heavyweight Championship","Cash-in victim; Priest wins","L") +
    row("drew-mcintyre","ppv",a("seth-rollins","Seth Rollins"),"Clash at the Castle 2022","Jun 18, 2022","Singles","Home country Scotland crowd","L")
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
print("\nBatch 6b complete.")
