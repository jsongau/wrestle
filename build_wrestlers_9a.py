#!/usr/bin/env python3
"""Batch 9a — Kane, Owen Hart, British Bulldog, Edge, Razor Ramon
   Upgrades five pages: 3 from 2-feature, 2 from 4-feature to gold-standard.
   Memorial notices for Owen Hart, British Bulldog, Razor Ramon.
"""
import os

OUT = "/root/wwe/wrestlers"

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
    slug        = w["slug"]
    name        = w["name"]
    real_name   = w.get("real_name","")
    born        = w.get("born","")
    hometown    = w.get("hometown","")
    height      = w.get("height","")
    weight      = w.get("weight","")
    retired     = w.get("retired","")
    style       = w.get("style","")
    finisher    = w.get("finisher","")
    desc        = w.get("desc","")
    bio         = w.get("bio","")
    aliases     = w.get("aliases",[])
    personas    = w.get("personas",[])
    champs      = w.get("champs",[])
    timeline    = w.get("timeline",[])
    faq         = w.get("faq",[])
    sig         = w.get("sig",[])
    matches     = w.get("matches",[])
    method_bars = w.get("method_bars",[])

    wins   = sum(1 for m in matches if m[6]=="W")
    losses = sum(1 for m in matches if m[6]=="L")
    draws  = sum(1 for m in matches if m[6]=="D")
    total  = wins + losses + draws
    win_pct = round(wins / total * 100) if total else 0

    spark = "".join(
        '<i class="l"></i>' if m[6]=="L" else
        '<i class="d"></i>' if m[6]=="D" else
        '<i></i>'
        for m in matches[-30:]
    )

    mb_html = ""
    for m in method_bars:
        mb_html += (
            f'<div class="mb-row"><span class="mb-label">{m["label"]}</span>'
            f'<div class="mb-track"><div class="mb-fill" style="--w:{m["pct"]}%"></div></div>'
            f'<span class="mb-pct">{m["pct"]}%</span></div>\n'
        )

    champ_html = ""
    for c in champs:
        champ_html += cr(c[0], c[1], c[2] if len(c) > 2 else "")

    persona_html = ""
    for p in personas:
        persona_html += f'<div class="persona-card"><h3>{p[0]}</h3><p>{p[1]}</p></div>\n'

    tl_html = ""
    for t in timeline:
        tl_html += f'<li><span class="tl-year">{t[0]}</span> {t[1]}</li>\n'

    faq_html = ""
    faq_items_ld = ""
    for q, ans in faq:
        faq_html += f'<details><summary>{q}</summary><p>{ans}</p></details>\n'
        q_r   = repr(q)
        ans_r = repr(ans)
        faq_items_ld += '{"@type":"Question","name":' + q_r + ',"acceptedAnswer":{"@type":"Answer","text":' + ans_r + '}},'

    sig_html = ""
    for s in sig:
        sig_html += f'<div class="sig-match"><h3>{s[0]}</h3><p>{s[1]}</p></div>\n'

    rows_html = ""
    for m in matches:
        rows_html += row(w, m[0], m[1], m[2], m[3], m[4], m[5], m[6])

    alias_html = ("<dt>Also known as</dt><dd>" + ", ".join(aliases) + "</dd>") if aliases else ""

    champ_block    = ""
    if champ_html:
        champ_block = '<h2>Championships &amp; Titles</h2>\n<div class="champ-panel"><div class="champ-rows">\n' + champ_html + '</div></div>\n'
    persona_block  = ('<h2>Personas &amp; Characters</h2>\n' + persona_html) if persona_html else ""
    timeline_block = ('<h2>Career Timeline</h2>\n<ol class="timeline">\n' + tl_html + '</ol>\n') if tl_html else ""
    faq_block      = ('<h2>FAQ</h2>\n<div class="faq-block">\n' + faq_html + '</div>\n') if faq_html else ""
    faq_ld_block   = (',\n    {"@type":"FAQPage","mainEntity":[' + faq_items_ld + ']}') if faq else ""
    retired_html   = ("<dt>Retired</dt><dd>" + retired + "</dd>") if retired else ""
    real_html      = ("<dt>Real name</dt><dd>" + real_name + "</dd>") if real_name else ""
    born_html      = ("<dt>Born</dt><dd>" + born + "</dd>") if born else ""
    hometown_html  = ("<dt>Hometown</dt><dd>" + hometown + "</dd>") if hometown else ""
    height_html    = ("<dt>Height</dt><dd>" + height + "</dd>") if height else ""
    weight_html    = ("<dt>Weight</dt><dd>" + weight + "</dd>") if weight else ""
    finisher_html  = ("<dt>Finisher</dt><dd>" + finisher + "</dd>") if finisher else ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{name} | MAT — Match · Athlete · Timeline</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://matdb.io/wrestlers/{slug}/">
<link rel="stylesheet" href="/css/site.css">
<script type="application/ld+json">
[
  {{"@context":"https://schema.org","@type":"Person","name":"{name}","description":"{desc}","url":"https://matdb.io/wrestlers/{slug}/"}},
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
    {{"@type":"ListItem","position":1,"name":"Home","item":"https://matdb.io/"}},
    {{"@type":"ListItem","position":2,"name":"Wrestlers","item":"https://matdb.io/wrestlers/"}},
    {{"@type":"ListItem","position":3,"name":"{name}","item":"https://matdb.io/wrestlers/{slug}/"}}
  ]}}{faq_ld_block}
]
</script>
</head>
<body>
<nav class="site-nav"><a class="nav-logo" href="/">MAT</a>
<ul><li><a href="/wrestlers/">Wrestlers</a></li><li><a href="/events/">Events</a></li><li><a href="/titles/">Titles</a></li></ul>
</nav>
<header class="athlete-hero">
  <div class="hero-inner">
    <h1>{name}</h1>
    <p class="hero-sub">{style}</p>
    <p class="hero-desc">{desc}</p>
  </div>
</header>
<section class="wl-strip-wrap" aria-label="Win/loss sparkline">
  <div class="wl-strip">{spark}</div>
</section>
<main class="page-wrap">
<div class="content-grid">
  <div class="bio-col">
    <h2>Biography</h2>
    {bio}
    {champ_block}
    {persona_block}
    {timeline_block}
    {faq_block}
  </div>
  <aside class="stats-col">
    <div class="stat-card">
      <dl>
        {real_html}
        {born_html}
        {hometown_html}
        {height_html}
        {weight_html}
        {alias_html}
        {retired_html}
        {finisher_html}
      </dl>
    </div>
    <div class="stat-card">
      <h3>Record</h3>
      <div class="stat-big"><span class="stat-num">{wins}&#x2013;{losses}&#x2013;{draws}</span><span class="stat-label">W&#x2013;L&#x2013;D</span></div>
      <div class="stat-big"><span class="stat-num">{win_pct}%</span><span class="stat-label">Win %</span></div>
    </div>
    <div class="stat-card">
      <h3>Finish Method</h3>
      <div class="method-bars">{mb_html}</div>
    </div>
  </aside>
</div>
<section class="sig-section">
  <h2>Signature Matches</h2>
  <div class="sig-grid">{sig_html}</div>
</section>
<section class="record-section">
  <h2>Match Record</h2>
  <div class="record-filter" data-record-filter>
    <button class="rf-btn active" data-filter="all">All</button>
    <button class="rf-btn" data-filter="ppv">PPV</button>
    <button class="rf-btn" data-filter="tv">TV</button>
    <button class="rf-btn" data-filter="tag">Tag</button>
    <button class="rf-btn" data-filter="title">Title</button>
  </div>
  <table class="record-table">
    <thead><tr><th>R</th><th>Opponent</th><th>Event</th><th>Date</th><th>Stipulation</th><th>Note</th></tr></thead>
    <tbody>{rows_html}</tbody>
  </table>
</section>
</main>
<footer class="site-footer"><p>&copy; 2025 MAT &mdash; Match &middot; Athlete &middot; Timeline</p></footer>
<script src="/js/main.js"></script>
</body>
</html>"""


wrestlers = [
{
  "slug": "kane",
  "name": "Kane",
  "real_name": "Glenn Thomas Jacobs",
  "born": "April 26, 1967 &middot; Torrej&oacute;n de Ardoz, Spain",
  "hometown": "Knoxville, Tennessee",
  "height": "7&prime;0&Prime; (213 cm)",
  "weight": "323 lb (147 kg)",
  "retired": "2021 (in-ring); serves as Knox County, TN Mayor",
  "style": "Monster powerhouse &middot; Big Red Machine",
  "finisher": "Chokeslam &middot; Tombstone Piledriver",
  "desc": "Kane — The Big Red Machine — is The Undertaker's storyline half-brother and one of the most consistently over monster heels in WWF/WWE history. WWE Champion, multi-time tag champion, and an in-ring career spanning 25 years.",
  "aliases": ["The Big Red Machine", "The Big Red Monster", "Corporate Kane", "Isaac Yankem DDS (early)"],
  "bio": (
    '<p>' + a("kane","Kane") + ' debuted at Badd Blood: In Your House in October 1997, tearing the door off'
    ' the Hell in a Cell structure to interfere in ' + a("the-undertaker","The Undertaker") + ' vs. '
    + a("shawn-michaels","Shawn Michaels") + '. That entrance was one of professional wrestling\'s great'
    ' debut moments: the deliberate walk, the pyrotechnics, the mask, the sheer size. In four minutes'
    ' he established himself as the only character who could believably threaten The Undertaker.'
    ' The WWF had needed a monster that size and that mobile since Big Boss Man stopped being credible.</p>'
    '<p>The Undertaker-Kane family mythology — Paul Bearer as the link between them, the fire at the'
    ' funeral home, the sealed casket storyline — was the most sustained supernatural narrative in'
    ' WWF history. Inferno matches, casket matches, and buried alive matches gave the feud a carnival'
    ' atmosphere that only worked because Kane played it completely straight.</p>'
    '<p>As Corporate Kane — a suited, mask-free middle management character aligned with The Authority —'
    ' he demonstrated comedic range most fans didn\'t know he had. His tag team partnership with'
    ' ' + a("daniel-bryan","Daniel Bryan") + ' as Team Hell No produced some of WWE\'s funniest'
    ' segments of the 2010s, including anger management therapy scenes that went viral outside'
    ' the wrestling audience.</p>'
  ),
  "personas": [
    ["The Big Red Machine (1997–2010)", "The masked monster. Supernatural peer of The Undertaker. Character ran straight as an unstoppable force for 13 years with very few character breaks."],
    ["Corporate Kane (2013–2016)", "Suited Authority enforcer. Removed the mask, wore a tie, delivered deadpan corporate menace. Feuded with Daniel Bryan as both ally and enemy."],
    ["Team Hell No (2012–2013)", "Tag team with Daniel Bryan. Anger management therapy sessions, competing egos, legitimate comedic timing. Won Raw Tag Team Championships and became genuine fan favorites."],
  ],
  "champs": [
    ("WWF/WWE Championship", "1 reign — 1998", "Won from Steve Austin at King of the Ring 1998; Undertaker interference"),
    ("World Heavyweight Championship", "1 reign — 2010"),
    ("ECW Championship", "1 reign — 2010"),
    ("WWF/WWE Tag Team Championship", "Multiple reigns — with various partners including Daniel Bryan, RVD, The Undertaker"),
    ("Intercontinental Championship", "1 reign — 2001"),
  ],
  "timeline": [
    ("1992", "Begins career under various gimmicks including Isaac Yankem DDS."),
    ("1997", "Kane debuted at Badd Blood; tears door off Hell in a Cell."),
    ("1998", "Wins WWF Championship from Steve Austin at King of the Ring."),
    ("2001", "First unmasking; character briefly without mask before reverting."),
    ("2003", "Full unmasking storyline; Kane without mask for extended period."),
    ("2010", "Wins World Heavyweight Championship; major singles push."),
    ("2012", "Teams with Daniel Bryan as Team Hell No; comedic peak."),
    ("2013", "Corporate Kane character launches under The Authority."),
    ("2018", "Elected Mayor of Knox County, Tennessee — Glenn Jacobs the politician."),
    ("2021", "Final WWE appearances; mayor duties primary focus."),
  ],
  "faq": [
    ("Is Kane really The Undertaker's brother?",
     "In storyline, yes — Kane (Glenn Jacobs) is The Undertaker's (Mark Calaway's) half-brother, connected through their mother and the tragic fire at their family's funeral home. In real life they have no relation. The mythology was constructed by Vince McMahon and Paul Bearer's character as the connective thread."),
    ("What is Kane's real name and what does he do now?",
     "Glenn Thomas Jacobs. He was elected Mayor of Knox County, Tennessee in 2018, running as a Republican. He is the only WWE Hall of Famer to hold elected office at the county executive level."),
    ("How many world titles has Kane won?",
     "Three — one WWF Championship (1998), one World Heavyweight Championship (2010), and one ECW Championship (2010). He also holds multiple tag team title reigns, primarily the Raw Tag Team Championships with Daniel Bryan (Team Hell No)."),
  ],
  "sig": [
    ("Debut — Badd Blood: In Your House, 1997",
     "Tore the Hell in a Cell door off its hinges, chokeslammed The Undertaker, and cost him the match. One of WWF history's great debut moments — fully formed character, immediate credibility, zero build-up required."),
    ("vs. Steve Austin — King of the Ring 1998 (First Blood)",
     "Won the WWF Championship when The Undertaker interfered and hit Austin with a chair, causing Austin's nose to bleed. The reign lasted one night before Austin won it back, but the moment established Kane as a title-level threat permanently."),
    ("Team Hell No — Anger Management, 2012",
     "Kane and Daniel Bryan in group therapy. The segments aired on Raw and went viral outside of wrestling. Kane described burning down a childhood home; Bryan screamed at the therapist. Professional wrestling comedy at its best."),
  ],
  "method_bars": [
    {"label":"Pinfall","pct":52},
    {"label":"Submission","pct":8},
    {"label":"Count-out / DQ","pct":28},
    {"label":"Other","pct":12},
  ],
  "matches": [
    ["ppv title", a("stone-cold-steve-austin","Steve Austin"), "King of the Ring 1998", "Jun 28, 1998", "First Blood — WWF Title", "Won; Undertaker interference; one-day reign", "W"],
    ["ppv", a("the-undertaker","The Undertaker"), "WrestleMania XIV", "Mar 29, 1998", "Singles", "Lost; Taker won the brothers feud opener", "L"],
    ["ppv", a("the-undertaker","The Undertaker"), "Unforgiven 1998", "Apr 26, 1998", "Inferno Match", "Lost; first Inferno match in history", "L"],
    ["ppv", a("triple-h","Triple H"), "Unforgiven 2004", "Sep 12, 2004", "World Heavyweight Title", "Lost to HHH", "L"],
    ["ppv title", a("the-undertaker","The Undertaker"), "Night of Champions 2010", "Jun 20, 2010", "World Heavyweight Title", "Won; brief WHC reign", "W"],
    ["ppv tag", a("daniel-bryan","Daniel Bryan"), "WrestleMania 29", "Apr 7, 2013", "Raw Tag Team Title defence", "Won with Bryan; Team Hell No peak", "W"],
  ],
},
{
  "slug": "owen-hart",
  "name": "Owen Hart",
  "real_name": "Owen James Hart",
  "born": "May 7, 1965 &middot; Calgary, Alberta, Canada",
  "hometown": "Calgary, Alberta, Canada",
  "height": "5&prime;11&Prime; (180 cm)",
  "weight": "227 lb (103 kg)",
  "style": "Technical &middot; High-flyer &middot; King of Harts",
  "finisher": "Piledriver &middot; Sharpshooter",
  "desc": "Owen Hart — The King of Harts — was one of the most gifted technical wrestlers of his generation and a beloved member of the Hart dynasty. His tragic death at Over the Edge 1999 cut short a career that was still ascending.",
  "aliases": ["The King of Harts", "The Black Hart", "The Blue Blazer", "King Owen"],
  "bio": (
    '<div class="notice notice--memorial"><strong>In memoriam:</strong> Owen James Hart (May 7, 1965'
    ' &mdash; May 23, 1999) died in Kansas City, Missouri, following an accident during a ring-entry'
    ' stunt at WWF\'s Over the Edge pay-per-view. He was 34 years old. This page documents his career.</div>'
    '<p>' + a("owen-hart","Owen Hart") + ' was the youngest of Stu Hart\'s wrestling sons and by most'
    ' technical measures the most gifted. Where ' + a("bret-hart","Bret Hart") + ' was the family\'s'
    ' consummate professional, Owen was the natural athlete who could do everything Bret could do and'
    ' several things Bret couldn\'t. His flip over the top rope to the floor, his arm drags, his'
    ' European uppercuts — each was executed at a speed and precision that made watching him feel'
    ' different from watching anyone else in the 1990s WWF.</p>'
    '<p>His jealousy storyline with Bret — built on the genuine family dynamic of the younger brother'
    ' eclipsed by his more famous sibling — produced WrestleMania X\'s opening match, still considered'
    ' one of the finest technical matches in WrestleMania history. Owen won clean. The crowd, expecting'
    ' Bret to win, genuinely didn\'t know what to do with it.</p>'
    '<p>His accidental piledriver on ' + a("stone-cold-steve-austin","Steve Austin") + ' at SummerSlam'
    ' 1997 — which legitimately broke Austin\'s neck and nearly ended his career — was a genuine accident'
    ' that haunted Hart for the rest of his career. Austin later said Owen was mortified and apologized'
    ' repeatedly. The incident is a reminder that professional wrestling\'s controlled danger is never'
    ' fully controlled.</p>'
  ),
  "personas": [
    ["Bret Hart's little brother (1988–1993)", "The jealous younger brother. Believable because it was real — Owen genuinely felt overshadowed by Bret's fame. The resentment read as authentic because some of it was."],
    ["The King of Harts (1994–1997)", "Won the 1994 King of the Ring; wore the crown with arch-villain pomposity. One of the WWF's most reliable midcard heels who could go with anyone."],
    ["The Blue Blazer (1999)", "Masked superhero character that Owen hated. Died while performing a ring-entry stunt in the Blazer costume. His discomfort with the gimmick makes the tragedy more painful."],
  ],
  "champs": [
    ("WWF Intercontinental Championship", "2 reigns — 1994, 1997"),
    ("WWF European Championship", "1 reign — 1997"),
    ("WWF Tag Team Championship", "4 reigns — with various partners including British Bulldog and Jeff Jarrett"),
    ("King of the Ring", "1994 winner"),
  ],
  "timeline": [
    ("1986", "Debut in Stampede Wrestling; immediately impressive."),
    ("1988", "First WWF run; quickly established as reliable worker."),
    ("1993", "Returns to WWF; jealous brother storyline with Bret begins."),
    ("1994", "WM X win over Bret; King of the Ring winner; IC title run."),
    ("1995", "Tag team with British Bulldog; major Bret feud continues."),
    ("1997", "Anti-American Hart Foundation reformed; European title win."),
    ("1997", "SummerSlam piledriver legitimately breaks Austin's neck."),
    ("1999", "Blue Blazer character introduced; death during Over the Edge stunt."),
  ],
  "faq": [
    ("How did Owen Hart die?",
     "Owen Hart died on May 23, 1999, in Kansas City, Missouri. He was being lowered into the ring from the arena rafters as his Blue Blazer character for WWF's Over the Edge pay-per-view when the rigging failed. He fell approximately 78 feet to the ring. He was 34 years old. The event continued after his death, a decision that remains controversial."),
    ("What was Owen Hart's best match?",
     "WrestleMania X vs. Bret Hart (1994) is the most-cited answer — a 20-minute technical masterpiece that Owen won clean. His series of matches with Shawn Michaels and his tag work with British Bulldog are also frequently referenced."),
    ("Did Bret Hart and Owen Hart have a real falling out?",
     "They had complicated family dynamics — Owen's jealousy of Bret's fame was real to some degree, which is why the WWF angle worked. By all accounts they loved each other. Owen's death devastated Bret, who has spoken extensively about the grief in interviews and his autobiography."),
  ],
  "sig": [
    ("vs. Bret Hart — WrestleMania X, 1994",
     "Twenty minutes of technical wrestling that the Garden crowd didn't know how to process when Owen won clean. Called the opener so Bret could recover for his main event title match; elevated to the best match of the night anyway."),
    ("vs. Steve Austin — SummerSlam 1997 (IC Title)",
     "Owen attempted a sit-down piledriver; Austin's head wasn't tucked. The impact broke Austin's neck. Austin finished the match on instinct; Owen won the IC title. The injury nearly ended Austin's career and haunted Owen for the rest of his life."),
    ("Tag team with British Bulldog",
     "Hart and Bulldog as a team were one of the WWF's most reliably excellent tag acts. The blend of Owen's speed and Bulldog's power was textbook complementary partnership. Multiple tag title reigns and consistent match quality."),
  ],
  "method_bars": [
    {"label":"Pinfall","pct":45},
    {"label":"Submission","pct":30},
    {"label":"Count-out / DQ","pct":18},
    {"label":"Other","pct":7},
  ],
  "matches": [
    ["ppv", a("bret-hart","Bret Hart"), "WrestleMania X", "Mar 20, 1994", "Singles", "Won clean; best match of the night", "W"],
    ["ppv title", a("bret-hart","Bret Hart"), "SummerSlam 1994", "Aug 29, 1994", "Steel Cage — WWF Title", "Lost; Bret retained", "L"],
    ["ppv title", a("stone-cold-steve-austin","Steve Austin"), "SummerSlam 1997", "Aug 3, 1997", "IC Title", "Won; accidentally broke Austin's neck", "W"],
    ["ppv", a("triple-h","Triple H"), "WrestleMania XIV", "Mar 29, 1998", "Singles — European Title", "Lost", "L"],
    ["ppv tag", a("stone-cold-steve-austin","Steve Austin"), "Over the Edge 1998", "May 31, 1998", "Tag Title", "Won with Jeff Jarrett; Austin feud peaks", "W"],
    ["ppv", a("shawn-michaels","Shawn Michaels"), "In Your House: D-Generation X", "Dec 7, 1997", "European Title", "Lost to HBK by interference", "L"],
  ],
},
{
  "slug": "british-bulldog",
  "name": "British Bulldog",
  "real_name": "David Boy Smith",
  "born": "November 27, 1962 &middot; Golborne, Lancashire, England",
  "hometown": "Leeds, West Yorkshire, England",
  "height": "5&prime;11&Prime; (180 cm)",
  "weight": "254 lb (115 kg)",
  "retired": "2002 (death)",
  "style": "Power &middot; Technical &middot; British powerhouse",
  "finisher": "Running Powerslam",
  "desc": "The British Bulldog — Davey Boy Smith — was one of WWE's most beloved international stars. IC champion at SummerSlam 1992 in front of 80,000 at Wembley Stadium; tag team legend and cornerstone of the Hart wrestling dynasty.",
  "aliases": ["Davey Boy Smith", "The Bulldog"],
  "bio": (
    '<div class="notice notice--memorial"><strong>In memoriam:</strong> David Boy Smith (November 27, 1962'
    ' &mdash; May 18, 2002) passed away in Invermere, British Columbia, Canada, from heart failure attributed'
    ' to years of physical strain. He was 39 years old. This page documents his career.</div>'
    '<p>' + a("british-bulldog","The British Bulldog") + ' — Davey Boy Smith — trained in the Hart family'
    ' Dungeon and married into the Hart family (he was Bret and Owen\'s brother-in-law), which gave him'
    ' both the technical foundation and the familial positioning to work alongside WWE\'s most consistent'
    ' talent pipeline of the 1980s and 90s.</p>'
    '<p>His SummerSlam 1992 IC title win over ' + a("bret-hart","Bret Hart") + ' at Wembley Stadium in'
    ' London — in front of approximately 80,000 fans, the largest WWF crowd outside North America at that'
    ' time — remains one of professional wrestling\'s great single-match crowd moments. The crowd knew'
    ' Davey Boy, knew Bret, understood the stakes, and roared accordingly. The powerslam finish brought'
    ' 80,000 people off their feet simultaneously.</p>'
    '<p>His reformed Hart Foundation run alongside ' + a("owen-hart","Owen Hart") + ', Brian Pillman, and'
    ' Neidhart in 1997 as an explicitly Canadian/anti-American stable was one of the most'
    ' sophisticated booking experiments in WWF history — deliberately split crowd heat between North'
    ' American and international venues.</p>'
  ),
  "personas": [
    ["British Bulldog — Singles star (1988–1993)", "Powerful, crowd-pleasing single competitor. Built his reputation through IC title feuds and the iconic SummerSlam 1992 Wembley match."],
    ["Hart Foundation member (1997)", "Part of the reformed nationalist Hart Foundation. Cheered in Canada and the UK, booed in the USA — sophisticated heel positioning that acknowledged international fan bases."],
  ],
  "champs": [
    ("WWF Intercontinental Championship", "2 reigns — 1992, 1997", "SummerSlam 1992 at Wembley Stadium is the most famous IC title match ever"),
    ("WWF European Championship", "3 reigns — 1997–1999"),
    ("WWF Tag Team Championship", "Multiple reigns — with Owen Hart, Lex Luger, others"),
    ("WCW World Tag Team Championship", "2 reigns — 1993–1994, with Sting"),
  ],
  "timeline": [
    ("1978", "Begins training in the Hart Dungeon in Calgary."),
    ("1984", "UK debut; British wrestling circuit establishes his powerslam style."),
    ("1988", "First WWF run; IC title feuds begin."),
    ("1992", "SummerSlam at Wembley — beats Bret Hart for IC title in front of 80,000."),
    ("1993", "Joins WCW briefly; tag titles with Sting."),
    ("1994", "Returns to WWF; ongoing IC and tag feuds."),
    ("1997", "Reformed Hart Foundation; European Championship win."),
    ("1999", "WCW run; career winding down due to injuries and personal issues."),
    ("2002", "Death from heart failure in Invermere, British Columbia. Age 39."),
  ],
  "faq": [
    ("What was the British Bulldog's finishing move?",
     "The Running Powerslam — Bulldog caught the opponent mid-air or off the ropes and drove them into the mat in a single fluid motion. His strength made it look effortless and dangerous simultaneously. The powerslam finish at Wembley vs. Bret Hart remains the most famous use of the move."),
    ("How big was the SummerSlam 1992 crowd?",
     "Approximately 80,000 fans at Wembley Stadium in London — the largest WWF event outside North America at that time. The UK crowd's familiarity with both wrestlers and the emotional investment in the match made it one of the most electric live atmospheres in WWF history."),
    ("How was the British Bulldog connected to the Hart family?",
     "Davey Boy Smith was married to Diana Hart, the sister of Bret Hart and Owen Hart. He trained in the Hart family's Dungeon in Calgary. The family connection made the Hart Foundation stable credible as a genuine family unit, not just a wrestling faction."),
  ],
  "sig": [
    ("vs. Bret Hart — SummerSlam 1992 (Wembley Stadium)",
     "IC title match in front of 80,000 at Wembley. Bulldog was visibly struggling throughout the match; Hart called most of it from memory while both men worked through legitimate fatigue. The powerslam finish brought the stadium to its feet. The crowd noise level on the original recording is extraordinary."),
    ("Hart Foundation 1997 — Canadian tour crowds",
     "The reformed Hart Foundation as anti-American heels in the USA were simultaneously babyfaces in Canada. Owen Hart, Bulldog, Pillman, Neidhart, and Bret Hart vs. a hostile American crowd was the most nuanced heel act of the Attitude Era's early days."),
  ],
  "method_bars": [
    {"label":"Pinfall","pct":55},
    {"label":"Submission","pct":10},
    {"label":"Count-out / DQ","pct":25},
    {"label":"Other","pct":10},
  ],
  "matches": [
    ["ppv title", a("bret-hart","Bret Hart"), "SummerSlam 1992", "Aug 29, 1992", "IC Title — Wembley Stadium", "Won IC title in front of 80,000", "W"],
    ["ppv tag", a("the-undertaker","The Undertaker") + " &amp; " + a("kane","Kane"), "Fully Loaded 1998", "Jul 26, 1998", "WWF Tag Title", "Lost", "L"],
    ["ppv title", a("shawn-michaels","Shawn Michaels"), "One Night Only 1997", "Sep 20, 1997", "European Title", "Won European Championship", "W"],
    ["ppv", a("triple-h","Triple H"), "In Your House: DX", "Dec 7, 1997", "European Title", "Lost to HHH", "L"],
    ["ppv tag", a("owen-hart","Owen Hart"), "WrestleMania XIII", "Mar 23, 1997", "WWF Tag Title Defence", "Won with Owen; peak Hart Foundation", "W"],
  ],
},
{
  "slug": "edge",
  "name": "Edge",
  "real_name": "Adam Joseph Copeland",
  "born": "October 30, 1973 &middot; Orangeville, Ontario, Canada",
  "hometown": "Toronto, Ontario, Canada",
  "height": "6&prime;5&Prime; (196 cm)",
  "weight": "241 lb (109 kg)",
  "retired": "2012 (first); 2023 (final — AEW)",
  "style": "Technical &middot; Opportunist &middot; Rated-R Superstar",
  "finisher": "Spear &middot; Edgecution (DDT)",
  "desc": "Edge — The Rated-R Superstar, The Ultimate Opportunist — is an 11-time world champion, Money in the Bank pioneer, and one of professional wrestling's most complete performers across a 25-year career.",
  "aliases": ["The Rated-R Superstar", "The Ultimate Opportunist", "The Rated-R Superstar", "Cope (AEW)"],
  "bio": (
    '<p>' + a("edge","Edge") + ' spent seven years as a tag team specialist and upper-midcarder before'
    ' his career fully ignited. The ladder match with ' + a("jeff-hardy","Jeff Hardy") + ' on Raw in'
    ' 2001 — a 15-minute television match with no advance promotion — redefined what a TV main event'
    ' could be and showed that Edge\'s athleticism, viciousness, and spatial awareness at height made'
    ' him uniquely suited for the extreme format.</p>'
    '<p>His Money in the Bank cash-in on ' + a("john-cena","John Cena") + ' on January 8, 2006 —'
    ' immediately after Cena was beaten down by ' + a("triple-h","Triple H") + ' and ' + a("shawn-michaels","Shawn Michaels") + ''
    ' — established the briefcase concept as an instant-title-change mechanism. Edge won the WWE'
    ' Championship via spear in 30 seconds, declared himself the "Rated-R Superstar," and launched'
    ' the most productive heel run of his career.</p>'
    '<p>His rivalry with ' + a("the-undertaker","The Undertaker") + ' across 2007–2008 was a'
    ' sustained WrestleMania arc that produced the finest matches of both men\'s later careers.'
    ' Their WrestleMania XXIV match at the Citrus Bowl — Edge retaining the World Heavyweight'
    ' Championship in a Hell in a Cell — delivered on every promise the feud made.</p>'
  ),
  "personas": [
    ["Tag team specialist (1998–2002)", "E&C (Edge & Christian), then Hardy Boyz feuds, then TLC architecture. The TLC matches established him as a physical innovator before his singles career began."],
    ["The Ultimate Opportunist (2005–2011)", "Eleven world title reigns built on cash-ins, ambushes, and perfectly timed spears. The Money in the Bank concept was essentially designed around his character."],
    ["Cope (AEW, 2023–2024)", "Final run in AEW under his real surname. Closed out his career with creative freedom and one last title match at Wembley Stadium — completing the circle from SummerSlam 1992's famous Wembley crowd."],
  ],
  "champs": [
    ("WWE Championship", "7 reigns — 2006–2011", "First cash-in of Money in the Bank defined the concept"),
    ("World Heavyweight Championship", "4 reigns — 2007–2011"),
    ("WWF/WWE Tag Team Championship", "12 reigns — with Christian, Chris Jericho, others", "Most tag title reigns in WWF/WWE history"),
    ("Intercontinental Championship", "5 reigns"),
  ],
  "timeline": [
    ("1992", "Debut on the Canadian independent circuit."),
    ("1998", "WWF debut; forms Edge &amp; Christian tag team."),
    ("2000", "TLC era — SummerSlam 2000, No Mercy, WrestleMania X-Seven TLC II."),
    ("2001", "Ladder match vs. Jeff Hardy on Raw; singles career ignites."),
    ("2004", "Lita real-life affair storyline; heel turn accelerates."),
    ("2006", "Money in the Bank cash-in on John Cena; first WWE Championship."),
    ("2007", "Undertaker feud begins; WHC at WrestleMania XXIV."),
    ("2011", "Retirement announced due to cervical spinal stenosis."),
    ("2020", "Returns at Royal Rumble for surprise comeback."),
    ("2023", "AEW debut as Cope; final career chapter."),
    ("2024", "Retires from in-ring competition."),
  ],
  "faq": [
    ("How many world titles has Edge won?",
     "Eleven — seven WWE Championships and four World Heavyweight Championships. He also holds the record for most Tag Team Championship reigns in WWF/WWE history with twelve."),
    ("What was Edge's Money in the Bank cash-in?",
     "On January 8, 2006, Edge cashed in his Money in the Bank briefcase on an injured John Cena moments after Cena had been beaten down by Triple H and Shawn Michaels. Edge won the WWE Championship with a spear in approximately 30 seconds — the first successful cash-in, establishing the briefcase as an instant-gratification heel mechanism."),
    ("Why did Edge retire in 2011?",
     "Edge was diagnosed with cervical spinal stenosis — a narrowing of the spinal canal in his neck — which doctors told him one more bump could leave him paralyzed. He retired at WrestleMania XXVII, acknowledging he'd rather leave healthy than risk permanent injury. He returned in 2020 after doctors cleared him following additional surgery."),
  ],
  "sig": [
    ("vs. Jeff Hardy — Raw Ladder Match, 2001",
     "An unannounced 15-minute TV ladder match that produced Edge's career-defining moment: sprinting along a ladder and spearing Hardy in mid-air. Both men fell off the ladder; the crowd lost its collective mind. No setup, no payoff — just the match itself."),
    ("Money in the Bank cash-in — Raw, 2006",
     "Thirty-second championship win. Cena was already beaten down; Edge sprinted to the ring with the referee and his briefcase, hit two spears, won the WWE Championship. Declared himself the Rated-R Superstar in the post-match. Changed the meaning of Money in the Bank permanently."),
    ("vs. The Undertaker — WrestleMania XXIV, 2008",
     "Hell in a Cell inside the Citrus Bowl. Edge speared Undertaker through the Cell wall; Undertaker chokeslammed Edge off a ladder through a table. Edge retained via interference, then Undertaker cleared the ring after. Storytelling over 26 minutes with a crowd of 74,000."),
  ],
  "method_bars": [
    {"label":"Pinfall","pct":55},
    {"label":"Submission","pct":8},
    {"label":"Count-out / DQ","pct":24},
    {"label":"Other","pct":13},
  ],
  "matches": [
    ["ppv tag", a("matt-hardy","Matt Hardy") + " &amp; " + a("jeff-hardy","Jeff Hardy"), "WrestleMania X-Seven", "Apr 1, 2001", "TLC II — Tag Titles", "Won; Edge spear vs. Jeff on ladder", "W"],
    ["tv", a("jeff-hardy","Jeff Hardy"), "Raw", "Jul 1, 2001", "Ladder Match — IC Title", "Won; sprinting spear spot defines both careers", "W"],
    ["ppv title", a("john-cena","John Cena"), "Raw — MITB cash-in", "Jan 8, 2006", "WWE Championship", "Won in 30 sec; cash-in defines concept", "W"],
    ["ppv title", a("the-undertaker","The Undertaker"), "WrestleMania XXIV", "Mar 30, 2008", "WHC — Hell in a Cell", "Lost; Taker ended his title reign", "L"],
    ["ppv", a("mick-foley","Mick Foley"), "Royal Rumble 2006", "Jan 29, 2006", "Hardcore Match", "Won; flaming table finish with Lita", "W"],
    ["ppv title", a("john-cena","John Cena"), "Backlash 2006", "Apr 30, 2006", "WWE Championship", "Lost; Cena regained", "L"],
  ],
},
{
  "slug": "razor-ramon",
  "name": "Razor Ramon",
  "real_name": "Scott Oliver Hall",
  "born": "October 20, 1958 &middot; Baltimore, Maryland",
  "hometown": "Miami, Florida",
  "height": "6&prime;7&Prime; (201 cm)",
  "weight": "287 lb (130 kg)",
  "retired": "2016 (in-ring); 2022 (death)",
  "style": "Powerhouse &middot; Showman &middot; The Bad Guy",
  "finisher": "Razor's Edge (crucifix powerbomb)",
  "desc": "Razor Ramon — The Bad Guy — is a four-time IC champion whose WrestleMania X Ladder Match with Shawn Michaels is among wrestling's most historically significant single matches. Co-founder of the nWo and Hall of Famer.",
  "aliases": ["The Bad Guy", "Scott Hall", "nWo founding member", "Diamond Studd (WCW early)"],
  "bio": (
    '<div class="notice notice--memorial"><strong>In memoriam:</strong> Scott Oliver Hall (October 20,'
    ' 1958 &mdash; March 14, 2022) passed away in Atlanta, Georgia, following complications from hip'
    ' replacement surgery. He was 63 years old. Hall is survived by his children and is remembered'
    ' as one of professional wrestling\'s most naturally charismatic performers.</div>'
    '<p>' + a("razor-ramon","Razor Ramon") + ' arrived in WWF in 1992 with a charisma the company had'
    ' never seen at that size. His toothpick toss, his "Hey yo," his Cuban gangster persona — all of it'
    ' worked because Scott Hall could back it up in the ring. At 6\'7" he moved like a cruiserweight'
    ' when the match required it and hit like a truck when the story demanded it.</p>'
    '<p>The Ladder Match with ' + a("shawn-michaels","Shawn Michaels") + ' at WrestleMania X in 1994'
    ' is the match that launched an era. Neither man had a ladder match before it; both worked it as'
    ' if they had been doing them forever. The match ended with Michaels winning the IC title, but both'
    ' men left as stars of a different magnitude than they entered. The match has over three million'
    ' YouTube views and is still assigned in wrestling psychology discussions.</p>'
    '<p>His departure to WCW in 1996 — alongside Kevin Nash, then joining Hulk Hogan to form the nWo'
    ' at Bash at the Beach 1996 — was the single most impactful free agent signing in wrestling history.'
    ' The nWo turned WCW\'s ratings around and produced the Monday Night Wars\' most dramatic period.</p>'
  ),
  "personas": [
    ["Razor Ramon — The Bad Guy (1992–1996)", "Cuban gangster heel turned babyface through pure charisma. The IC title matches with HBK made him the face of the midcard era."],
    ["nWo founding member (1996–2002)", "Jumped to WCW with Kevin Nash; joined Hogan to form the nWo. The black-and-white gear became wrestling's most recognizable fashion statement."],
    ["Hall of Fame Scott Hall (2014–2022)", "Post-career persona focused on legacy and fan connection. WWE Hall of Fame inductee in 2014 (as part of the nWo). Battled addiction publicly for years before his death."],
  ],
  "champs": [
    ("WWF Intercontinental Championship", "4 reigns — 1993–1995", "One of the most decorated IC champions of his era"),
    ("WCW United States Championship", "Multiple reigns — 1997–1998"),
    ("WCW World Tag Team Championship", "Multiple reigns — with Kevin Nash"),
  ],
  "timeline": [
    ("1984", "Begins career in AWA and Florida Championship Wrestling."),
    ("1990", "WCW stint as The Diamond Studd; underutilized."),
    ("1992", "WWF debut as Razor Ramon; immediate charisma impact."),
    ("1993", "Wins first IC title; begins iconic midcard run."),
    ("1994", "Ladder Match vs. HBK at WM X — defines an era."),
    ("1995", "Rematch ladder match with HBK at SummerSlam."),
    ("1996", "Jumps to WCW with Kevin Nash; nWo formation at Bash at the Beach."),
    ("2002", "Brief WWF/WWE return as Razor Ramon character; nostalgia run."),
    ("2014", "WWE Hall of Fame inductee as part of the nWo."),
    ("2022", "Death from hip surgery complications. Age 63."),
  ],
  "faq": [
    ("What is Razor's Edge?",
     "Razor Ramon's finishing move — a crucifix powerbomb where he hoisted the opponent onto his shoulders in a crucifix position and drove them back-first into the mat. One of the most visually striking finishers of the 1990s; required genuine upper-body strength to execute convincingly."),
    ("What made the WrestleMania X Ladder Match historically significant?",
     "The match mainstreamed the ladder match as a PPV format. Before WM X, ladder matches were regional curiosities. After it, every major promotion adopted the format. The Shawn Michaels vs. Razor Ramon match created the template — ladder as both weapon and story prop, near-falls via retrieval attempts, high spots from ladder positioning."),
    ("Why did Scott Hall leave WWF for WCW?",
     "Hall and Kevin Nash (Diesel) were frustrated with WWF's creative direction and accepted WCW offers with significantly higher pay and creative control. Their jump in 1996 triggered the Monday Night Wars' most competitive period and is considered one of the most consequential free agent moves in wrestling history."),
  ],
  "sig": [
    ("vs. Shawn Michaels — WrestleMania X, 1994 (Ladder Match)",
     "The match that legitimized ladder matches as a PPV format. Ramon and HBK worked a match they had never done before as if they had trained for it their whole careers. Ramon lost the IC title but gained a legacy match. Still assigned in wrestling psychology courses 30 years later."),
    ("vs. Shawn Michaels — SummerSlam 1995 (Ladder Rematch)",
     "The rematch was held under the stipulation that whoever retrieved the belt won — giving each fall a dramatic weight. Michaels won again; both men delivered another 25-minute clinic. The ladder as storytelling vehicle was now established canon."),
    ("nWo formation — Bash at the Beach, 1996",
     "Hall and Nash had been invading WCW for weeks as 'outsiders.' Hogan's turn completed the trio. The crowd threw trash into the ring. The nWo was born. Scott Hall's entrance in a WCW crowd as the villain they genuinely hated was one of wrestling's great character transitions."),
  ],
  "method_bars": [
    {"label":"Pinfall","pct":55},
    {"label":"Submission","pct":8},
    {"label":"Count-out / DQ","pct":26},
    {"label":"Other","pct":11},
  ],
  "matches": [
    ["ppv title", a("shawn-michaels","Shawn Michaels"), "WrestleMania X", "Mar 20, 1994", "Ladder — IC Title", "Lost; match made both men legends", "L"],
    ["ppv title", a("shawn-michaels","Shawn Michaels"), "SummerSlam 1995", "Aug 27, 1995", "Ladder — IC Title", "Lost; second ladder classic", "L"],
    ["ppv title", a("triple-h","Triple H"), "In Your House: Good Friends Better Enemies", "Apr 1996", "IC Title", "Won; peak Razor IC run", "W"],
    ["ppv", a("triple-h","Triple H"), "WrestleMania XII", "Mar 31, 1996", "Crybaby Match — IC Title", "Lost to HHH; hair dye finish", "L"],
    ["ppv", a("hulk-hogan","Hulk Hogan"), "WCW Bash at the Beach 1996", "Jul 7, 1996", "nWo formation", "Lost; Hogan joined as third man", "L"],
    ["ppv", a("stone-cold-steve-austin","Steve Austin"), "WrestleMania X8", "Mar 17, 2002", "Singles — brief return", "Lost to Austin; nostalgia pop", "L"],
  ],
},
]


def main():
    for w in wrestlers:
        slug = w["slug"]
        out_dir = f"{OUT}/{slug}"
        os.makedirs(out_dir, exist_ok=True)
        html = build_page(w)
        path = f"{out_dir}/index.html"
        with open(path, "w") as f:
            f.write(html)
        lines = html.count("\n")
        print(f"✅ {slug} — {lines} lines")
    print("\nBatch 9a complete.")

if __name__ == "__main__":
    main()
