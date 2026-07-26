#!/usr/bin/env python3
"""Batch 8a — Shawn Michaels, Triple H, Mick Foley, The Rock, Jeff Hardy
   Upgrades three 2-feature pages and adds Jeff Hardy (new).
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
  "slug": "shawn-michaels",
  "name": "Shawn Michaels",
  "real_name": "Michael Shawn Hickenbottom",
  "born": "October 22, 1965 &middot; Chandler, Arizona",
  "hometown": "San Antonio, Texas",
  "height": "6&prime;1&Prime; (185 cm)",
  "weight": "225 lb (102 kg)",
  "retired": "2010 (final); 2018 one-off return",
  "style": "High-flyer &middot; Technical &middot; Mr. WrestleMania",
  "finisher": "Sweet Chin Music (superkick)",
  "desc": "Shawn Michaels — HBK, Mr. WrestleMania — is the benchmark for in-ring excellence. Four-time world champion, DX co-founder, and architect of WrestleMania matches that defined an era.",
  "aliases": ["HBK", "The Heartbreak Kid", "Mr. WrestleMania", "The Showstopper"],
  "bio": (
    f'<p>{a("shawn-michaels","Shawn Michaels")} redefined what professional wrestling could be. From tag team origins with '
    f'{a("marty-jannetty","Marty Jannetty")} in <em>The Rockers</em> to legendary late-career classics against '
    f'{a("the-undertaker","The Undertaker")}, Michaels delivered match-of-the-night performances with such consistency '
    f'that the bar he set is still the standard modern wrestlers are measured against.</p>'
    f'<p>His Ladder Match with {a("razor-ramon","Razor Ramon")} at WrestleMania X (1994) legitimized the ladder match '
    f'as a PPV format. His 60-minute Iron Man match with {a("bret-hart","Bret Hart")} at WrestleMania XII pushed '
    f'endurance storytelling to its limit. And his WrestleMania XXV match with The Undertaker — frequently voted '
    f'the greatest WrestleMania match in history — showed what a main event looks like when both performers are '
    f'operating at their absolute ceiling.</p>'
    f'<p>After a career-ending back injury in 1998 forced him to forfeit the WWF title, he reinvented himself upon '
    f'his 2002 return: slower, more deliberate, arguably even better. His WrestleMania XXIV send-off of '
    f'{a("ric-flair","Ric Flair")} — delivering a tearful Sweet Chin Music — was among the most emotionally '
    f'complex match finishes in WrestleMania history.</p>'
  ),
  "personas": [
    ["The Rockers (1987–1992)", "High-flying tag duo with Marty Jannetty. Beloved despite never winning tag gold — a title win was vacated due to a contractual dispute."],
    ["The Heartbreak Kid (1992–1998)", "Cocky, flamboyant singles star. IC champion, then WWF Champion. The character that made him a main event force."],
    ["D-Generation X (1997–1998, 2006–2010)", "Co-founder with Triple H. The anti-authority faction defined Attitude Era tone alongside Austin and The Rock."],
    ["Mr. WrestleMania (2002–2010)", "Post-comeback identity. Eight years of consistently delivering the best match on every WrestleMania card he appeared on."],
  ],
  "champs": [
    ("WWF/WWE Championship", "4 reigns — 1996, 1997, 2002, 2004"),
    ("WWF Intercontinental Championship", "3 reigns — 1992, 1993, 1995", "Ladder Match vs. Ramon at WM X defined the IC title era"),
    ("WWF/WWE Tag Team Championship", "Multiple reigns — with Jannetty and Triple H"),
  ],
  "timeline": [
    ("1984", "Debut in the AWA as Shawn Michaels."),
    ("1987", "Joins The Rockers with Marty Jannetty in WWF."),
    ("1992", "Turns heel on Jannetty; launches singles career."),
    ("1994", "Ladder Match vs. Razor Ramon at WM X — match of the year."),
    ("1996", "Wins first WWF Championship: Iron Man match over Bret Hart."),
    ("1997", "Co-founds D-Generation X with Triple H."),
    ("1998", "Back injury at Royal Rumble; forfeits WWF title; retires."),
    ("2002", "Returns at SummerSlam; Street Fight win over Triple H."),
    ("2008", "Sends Ric Flair into retirement at WM XXIV."),
    ("2009", "WM XXV vs. Undertaker — voted greatest WM match ever."),
    ("2010", "Loses to Undertaker at WM XXVI under Streak vs. Career stipulation; retires."),
    ("2018", "One-off tag return at Crown Jewel alongside Triple H."),
  ],
  "faq": [
    ("Why is Shawn Michaels called Mr. WrestleMania?",
     "Michaels earned the nickname for delivering match-of-the-night performances at WrestleMania — the Razor ladder match, the Iron Man, the Undertaker classics, and the Ric Flair retirement bout — across three different decades."),
    ("How many times did Shawn Michaels retire?",
     "Twice formally: first in 1998 due to a back injury that required spinal fusion surgery, and again in 2010 after losing to The Undertaker at WrestleMania XXVI under a career vs. streak stipulation."),
    ("What is Sweet Chin Music?",
     "Michaels' finishing superkick — delivered at full sprint, often after tuning up the band (stomping in the corner). One of wrestling's most over finishers; the wind-up became as famous as the kick itself."),
  ],
  "sig": [
    ("vs. Razor Ramon — WrestleMania X, 1994",
     "The match that made ladder matches a PPV institution. HBK lost the IC title but both men left as stars. Nearly every TLC/ladder match since traces its DNA to this 18-minute classic."),
    ("vs. Bret Hart — WrestleMania XII, 1996",
     "The 60-minute Iron Man Match. Ended 0–0 through regulation; Michaels won in sudden-death overtime. Still the longest uninterrupted in-ring performance in WrestleMania history."),
    ("vs. Undertaker — WrestleMania XXV, 2009",
     "Consistently voted the greatest WrestleMania match ever. Thirty-plus minutes of storytelling that included a near-fall off a moonsault to the floor, multiple Tombstone reversals, and a standing ovation finish."),
    ("vs. Ric Flair — WrestleMania XXIV, 2008",
     "Michaels apologized before delivering the Sweet Chin Music that ended Flair's career. One of wrestling's most emotionally complex match finishes."),
  ],
  "method_bars": [
    {"label":"Pinfall","pct":50},
    {"label":"Submission","pct":14},
    {"label":"Count-out / DQ","pct":24},
    {"label":"Other","pct":12},
  ],
  "matches": [
    ["ppv title", a("razor-ramon","Razor Ramon"), "WrestleMania X", "Mar 20, 1994", "Ladder — IC Title", "Lost despite the better performance", "L"],
    ["ppv title", a("bret-hart","Bret Hart"), "WrestleMania XII", "Mar 31, 1996", "60-Min Iron Man — WWF Title", "Won in overtime 1–0", "W"],
    ["ppv title", a("diesel","Diesel"), "In Your House: Good Friends Better Enemies", "Apr 28, 1996", "No Holds Barred — WWF Title", "Retained", "W"],
    ["ppv title", a("mankind","Mankind"), "Mind Games", "Sep 22, 1996", "WWF Title", "DQ — retained", "W"],
    ["ppv title", a("stone-cold-steve-austin","Steve Austin"), "WrestleMania XIV", "Mar 29, 1998", "WWF Title (Tyson enforcer)", "Lost; Attitude Era begins", "L"],
    ["ppv", a("triple-h","Triple H"), "SummerSlam", "Aug 25, 2002", "Unsanctioned Street Fight", "Comeback win; emotional return", "W"],
    ["ppv", a("chris-jericho","Chris Jericho"), "WrestleMania XIX", "Mar 30, 2003", "Singles", "Won", "W"],
    ["ppv", a("ric-flair","Ric Flair"), "WrestleMania XXIV", "Mar 30, 2008", "Retirement Match", "Won; sent Flair into retirement", "W"],
    ["ppv", a("the-undertaker","The Undertaker"), "WrestleMania XXV", "Apr 5, 2009", "Singles", "Lost in match of the year/decade", "L"],
    ["ppv", a("the-undertaker","The Undertaker"), "WrestleMania XXVI", "Mar 28, 2010", "Streak vs. Career", "Lost; retired for good", "L"],
  ],
},
{
  "slug": "triple-h",
  "name": "Triple H",
  "real_name": "Paul Michael Levesque",
  "born": "July 27, 1969 &middot; Nashua, New Hampshire",
  "hometown": "Greenwich, Connecticut",
  "height": "6&prime;4&Prime; (193 cm)",
  "weight": "255 lb (116 kg)",
  "retired": "2022 (in-ring); continues as Chief Content Officer",
  "style": "Methodical powerhouse &middot; Cerebral Assassin",
  "finisher": "Pedigree (double underhook facebreaker)",
  "desc": "Triple H — The Game, The King of Kings — is a 14-time world champion, co-founder of DX, architect of NXT, and WWE's Chief Content Officer. The most powerful figure in wrestling history inside the ring and out.",
  "aliases": ["HHH", "The Game", "The Cerebral Assassin", "The King of Kings", "Terra Ryzing"],
  "bio": (
    f'<p>{a("triple-h","Triple H")} is the rare performer whose influence extends equally into the ring, the boardroom, '
    f'and the developmental system. As a 14-time world champion he main-evented more WrestleManias than any peer. '
    f'As architect of the NXT brand he built the developmental pipeline that produced '
    f'{a("kevin-owens","Kevin Owens")}, {a("finn-balor","Finn Bálor")}, {a("shinsuke-nakamura","Shinsuke Nakamura")}, '
    f'and dozens of other stars. As Chief Content Officer he replaced Vince McMahon and oversaw the Creative '
    f'turnaround of 2022–2025 that fans widely credit as a creative renaissance.</p>'
    f'<p>His in-ring style was cerebral and methodical — the perfect foil to '
    f'{a("shawn-michaels","Shawn Michaels")}\'s spontaneous high-flying. The contrast produced DX\'s chemistry. '
    f'Evolution — with {a("ric-flair","Ric Flair")}, {a("randy-orton","Randy Orton")}, and {a("batista","Batista")} — '
    f'was the most effective faction of the 2000s, producing three main event stars through a deliberate '
    f'Four Horsemen homage.</p>'
    f'<p>His feud with {a("mick-foley","Mick Foley")} (as Cactus Jack) in early 2000 produced two of the '
    f'most violent PPV matches in WWF history. His willingness to bleed, lose, and put talent over — '
    f'documented across {a("daniel-bryan","Daniel Bryan")}\'s WrestleMania XXX arc — showed the political '
    f'intelligence that translated naturally into executive leadership.</p>'
  ),
  "personas": [
    ["Terra Ryzing / Hunter Hearst Helmsley (1992–1997)", "WCW debut as Terra Ryzing; WWF arrival as Connecticut blue-blood aristocrat. Buried after the MSG Curtain Call incident; rebuilt methodically over 18 months."],
    ["D-Generation X (1997–2000, 2006–2010)", "After HBK's injury, Triple H became DX's leader. The faction's anti-authority posture defined Attitude Era tone."],
    ["Evolution (2003–2005)", "Led the stable with Ric Flair, Randy Orton, and Batista. A deliberate Four Horsemen tribute that succeeded in elevating all three members to main event status."],
    ["The Authority (2013–2016)", "Power couple with Stephanie McMahon, portraying the corporate heel COO. The foil that elevated Daniel Bryan, Dean Ambrose, and Roman Reigns."],
  ],
  "champs": [
    ("WWF/WWE Championship", "8 reigns — 1999–2009", "Third-most WWE title reigns in history"),
    ("World Heavyweight Championship", "5 reigns — 2002–2008", "Inaugural WHC on Raw after 2002 brand split"),
    ("WWF Intercontinental Championship", "5 reigns — 1997–2000"),
    ("Tag Team Championship", "Multiple reigns — with DX and McMahon"),
  ],
  "timeline": [
    ("1992", "Debuts in IWF, then WCW as Terra Ryzing."),
    ("1995", "Arrives in WWF as Hunter Hearst Helmsley."),
    ("1996", "MSG Curtain Call — Kliq breaks kayfabe; Triple H receives career punishment."),
    ("1997", "Rehabilitated; co-founds DX with Shawn Michaels."),
    ("1999", "Wins first WWF Championship; cements main event status."),
    ("2001", "Tears quad at Royal Rumble; out eight months."),
    ("2002", "Returns to massive ovation; immediately back in main events."),
    ("2003", "Forms Evolution with Flair, Orton, Batista."),
    ("2011", "Named Executive VP of Talent, Live Events and Creative."),
    ("2013", "The Authority character launches; creative and real-world roles blur."),
    ("2022", "Named Chief Content Officer after Vince McMahon's resignation."),
  ],
  "faq": [
    ("How many world titles has Triple H won?",
     "Fourteen — 8 WWE Championships and 5 World Heavyweight Championships (plus one more depending on the counting system used). Third-most world title reigns in WWE history."),
    ("What is the Pedigree?",
     "Triple H's finishing move — he hooks both of the opponent's arms behind their back in a double underhook position, then drops them face-first onto the mat. One of wrestling's most protected finishers; rarely kicked out of."),
    ("What happened at the MSG Curtain Call?",
     "In 1996, at a non-televised MSG show, Triple H, Shawn Michaels, Kevin Nash, and Scott Hall broke character to embrace in the ring — a public display of the real Kliq friendship. Nash and Hall were leaving for WCW, so the only person left to punish was Triple H, who lost his planned King of the Ring win and had to rebuild over 18 months."),
  ],
  "sig": [
    ("vs. Cactus Jack — Royal Rumble 2000",
     "A Street Fight that shocked WWF fans with its level of violence. Foley took a barbed-wire board to the face and Triple H took a DDT onto thumbtacks. Triple H retained; Foley was unmasked. Match of the year contender."),
    ("vs. Shawn Michaels — SummerSlam 2002 (Unsanctioned Street Fight)",
     "HBK's return after four years away. Triple H lost and did so with complete commitment — put Michaels fully over in his comeback match. One of wrestling's most emotional undercard performances."),
    ("vs. Daniel Bryan — WrestleMania XXX, 2014",
     "Triple H lost cleanly in the opener, then Bryan beat Orton and Batista in the main event. Triple H's agreement to lose twice in one night — once as opponent, then as absent obstacle — defined what the booking needed."),
  ],
  "method_bars": [
    {"label":"Pinfall","pct":56},
    {"label":"Submission","pct":12},
    {"label":"Count-out / DQ","pct":22},
    {"label":"Other","pct":10},
  ],
  "matches": [
    ["ppv", a("mick-foley","Mick Foley (Cactus Jack)"), "Royal Rumble 2000", "Jan 23, 2000", "Street Fight — WWF Title", "Retained; thumbtacks, barbed wire", "W"],
    ["ppv", a("mick-foley","Mick Foley (Cactus Jack)"), "No Way Out 2000", "Feb 27, 2000", "Hell in a Cell — WWF Title", "Retained; Foley unmasked", "W"],
    ["ppv title", a("the-rock","The Rock"), "WrestleMania 2000", "Apr 2, 2000", "Fatal 4-Way — WWF Title", "Lost to Rock; McMahons turned", "L"],
    ["ppv", a("shawn-michaels","Shawn Michaels"), "SummerSlam 2002", "Aug 25, 2002", "Unsanctioned Street Fight", "Lost; HBK comeback classic", "L"],
    ["ppv title", a("batista","Batista"), "WrestleMania 21", "Apr 3, 2005", "World Heavyweight Title", "Lost; Evolution ends", "L"],
    ["ppv", a("the-undertaker","The Undertaker"), "WrestleMania XXVII", "Apr 3, 2011", "No Holds Barred", "Lost; Streak continues 19–0", "L"],
    ["ppv", a("the-undertaker","The Undertaker"), "WrestleMania XXVIII", "Apr 1, 2012", "Hell in a Cell", "Lost; Streak continues 20–0", "L"],
    ["ppv", a("daniel-bryan","Daniel Bryan"), "WrestleMania XXX", "Apr 6, 2014", "Singles", "Lost cleanly; put Bryan over", "L"],
    ["ppv", a("roman-reigns","Roman Reigns"), "WrestleMania 32", "Apr 3, 2016", "WWE Title", "Lost; Reigns ascends", "L"],
  ],
},
{
  "slug": "mick-foley",
  "name": "Mick Foley",
  "real_name": "Michael Francis Foley",
  "born": "June 7, 1965 &middot; Bloomington, Indiana",
  "hometown": "Long Island, New York",
  "height": "6&prime;2&Prime; (188 cm)",
  "weight": "287 lb (130 kg)",
  "retired": "2012 (mostly)",
  "style": "Hardcore &middot; Brawler &middot; Storyteller",
  "finisher": "Mandible Claw &middot; Double-Arm DDT",
  "desc": "Mick Foley — Mankind, Cactus Jack, Dude Love — is the definitive hardcore legend. Three-time WWF Champion and architect of wrestling's most viscerally memorable moments, including the Hell in a Cell fall at King of the Ring 1998.",
  "aliases": ["Mankind", "Cactus Jack", "Dude Love", "The Hardcore Legend", "Mrs. Foley's Baby Boy"],
  "bio": (
    f'<p>{a("mick-foley","Mick Foley")} was never supposed to be a world champion. Too round, too slow, too odd. '
    f'What he had instead was an unmatched willingness to sacrifice his body, a gift for character work across '
    f'three distinct personas, and an authenticity that audiences recognized as real even when everything around '
    f'him was scripted.</p>'
    f'<p>The Hell in a Cell match against {a("the-undertaker","The Undertaker")} at King of the Ring 1998 produced '
    f'two images that defined an era: Foley thrown off the cage roof onto the announce table, then — after being '
    f'carried back up on a stretcher — falling through the top of the cage to the mat. These were not worked bumps. '
    f'He broke his jaw, dislocated his shoulder, and knocked out teeth on live television. Jim Ross\'s call — '
    f'"AS GOD AS MY WITNESS, HE IS BROKEN IN HALF!" — became wrestling\'s most famous commentary line.</p>'
    f'<p>His feud with {a("triple-h","Triple H")} in early 2000 produced perhaps the most violent mainstream '
    f'matches in WWF history: a Street Fight and a Hell in a Cell in which Foley took a barbed-wire board to the '
    f'face and was unmasked. He lost both. He was supposed to lose both. He knew it and did it anyway — '
    f'that willingness to absorb punishment in service of the story defined his entire career.</p>'
  ),
  "personas": [
    ["Cactus Jack (1986–1995, 1997–2000)", "The original persona. Unhinged deathmatch specialist, NWA/WCW/ECW veteran. Most brutal version of Foley — pure brawler, no mercy, no gimmick."],
    ["Mankind (1996–2000)", "WWF debut character. Disturbed, masked, lived in boiler rooms. Carried Mr. Socko. Evolved from monster heel to beloved babyface through sheer character work."],
    ["Dude Love (1997–1998)", "1970s flower-power alter ego played for comedy. Debuted when Steve Austin requested him as a tag partner. Short-lived but enduringly beloved."],
    ["Mick Foley (1999–present)", "The unmasked literary persona. Wrote three NYT bestselling books about professional wrestling. A genuine cultural crossover figure."],
  ],
  "champs": [
    ("WWF Championship", "3 reigns — all in 1999", "Won first title with assistance from The Rock and Vince McMahon's involvement"),
    ("WWF Tag Team Championship", "2 reigns — with The Rock", "Part of the unlikely but beloved Foley-Rock partnership"),
    ("WWF Hardcore Championship", "Multiple reigns", "24/7 rule era chaos; won and lost the title in famously absurd circumstances"),
  ],
  "timeline": [
    ("1983", "First professional match; trains under Dominic DeNucci."),
    ("1986", "Full-time as Cactus Jack; gains reputation on regional circuit."),
    ("1991", "Munich incident — loses ear in match against Vader; keeps going."),
    ("1992", "Joins WCW; feud with Vader produces legendary brutal matches."),
    ("1994", "Joins ECW; embraces extreme deathmatch environment."),
    ("1996", "Debuts in WWF as Mankind; immediate monster push."),
    ("1997", "Introduces Dude Love; teams with Steve Austin for tag titles."),
    ("1998", "Hell in a Cell vs. Undertaker — the most famous match in wrestling history."),
    ("1999", "Wins WWF title three times in one year; This Is Your Life with The Rock breaks Raw ratings record."),
    ("2000", "Street Fight and HIAC losses to Triple H; first retirement."),
    ("2004", "Returns to WWE in GM and sporadic match roles."),
    ("2006", "Hardcore match with Edge at Royal Rumble — comeback classic."),
    ("2009", "WWE Hall of Fame inductee, Class of 2013 (announced 2009 era)."),
  ],
  "faq": [
    ("How many times did Mick Foley fall off/through the Cell?",
     "Twice in the same match at King of the Ring 1998: first thrown off the top of the cage (16 feet) onto the Spanish announce table, then — after being brought back up — falling through the cage roof onto the mat when the roof gave way."),
    ("What is the Mandible Claw?",
     "Foley's finishing submission — he inserts two fingers under the tongue and applies pressure to specific nerve clusters in the mouth, often while wearing Mr. Socko (a sock puppet). Effective storytelling device that required opponents to sell unconsciousness convincingly."),
    ("Did Mick Foley really write bestselling books?",
     "Yes — Have a Nice Day (1999), Foley Is Good (2001), and The Hardcore Diaries (2006) all hit the New York Times bestseller list. The first sold over one million copies and is widely considered the best wrestling autobiography ever written."),
  ],
  "sig": [
    ("vs. Undertaker — King of the Ring 1998 (Hell in a Cell)",
     "Two falls off/through a steel cage structure. Foley's jaw, shoulder, and teeth all took real damage. Undertaker paused the match to check on him. Jim Ross's call made history. The match that defined what 'extreme' meant before ECW reached mainstream."),
    ("vs. Triple H — Royal Rumble 2000 (Street Fight)",
     "Foley took a barbed-wire board to the face and a DDT into thumbtacks. Triple H retained but left drenched in blood. Match of the year; both men at their absolute ceiling for this style."),
    ("vs. Edge — Royal Rumble 2006 (Hardcore Match)",
     "Foley out of semi-retirement, matching Edge's intensity across a brutal brawl that ended with both men going through a flaming table. Reinvented both wrestlers in one match and launched Edge's definitive heel arc."),
  ],
  "method_bars": [
    {"label":"Pinfall","pct":46},
    {"label":"Submission","pct":10},
    {"label":"Count-out / DQ","pct":30},
    {"label":"Other","pct":14},
  ],
  "matches": [
    ["ppv", a("the-undertaker","The Undertaker"), "King of the Ring 1998", "Jun 28, 1998", "Hell in a Cell", "Two cage falls; lost but made history", "L"],
    ["tv title", a("the-rock","The Rock"), "Raw is War", "Jan 4, 1999", "Singles — WWF Title", "Won first WWF title with McMahon's help", "W"],
    ["ppv", a("the-rock","The Rock"), "Halftime Heat", "Jan 31, 1999", "Empty Arena — WWF Title", "Won; famous empty arena brawl", "W"],
    ["ppv", a("triple-h","Triple H"), "Royal Rumble 2000", "Jan 23, 2000", "Street Fight — WWF Title", "Lost; barbed wire + thumbtacks", "L"],
    ["ppv", a("triple-h","Triple H"), "No Way Out 2000", "Feb 27, 2000", "Hell in a Cell — WWF Title", "Lost; unmasked as Cactus Jack", "L"],
    ["ppv", a("randy-orton","Randy Orton"), "Backlash 2004", "Apr 18, 2004", "Singles", "Lost via RKO; Orton ascends", "L"],
    ["ppv", a("edge","Edge"), "Royal Rumble 2006", "Jan 29, 2006", "Hardcore Match", "Lost; flaming table finish", "L"],
  ],
},
{
  "slug": "the-rock",
  "name": "The Rock",
  "real_name": "Dwayne Douglas Johnson",
  "born": "May 2, 1972 &middot; Hayward, California",
  "hometown": "Miami, Florida",
  "height": "6&prime;5&Prime; (196 cm)",
  "weight": "260 lb (118 kg)",
  "style": "Powerhouse &middot; Showman &middot; The Great One",
  "finisher": "Rock Bottom &middot; People's Elbow",
  "desc": "The Rock — The Great One, The People's Champion — is WWE's most electrifying performer and the most successful crossover star in wrestling history. Eight-time WWF/WWE Champion whose mic work, athleticism, and charisma remain unmatched.",
  "aliases": ["The Great One", "The People's Champion", "The Most Electrifying Man in Sports Entertainment", "Rocky Maivia"],
  "bio": (
    f'<p>{a("the-rock","The Rock")} arrived as Rocky Maivia — a third-generation star pushed too fast, too clean. '
    f'The crowds turned on him immediately and chanted "Die, Rocky, Die." He listened. He joined the Nation of '
    f'Domination as a heel, found his voice, and discovered that the most charismatic version of himself was '
    f'the one that didn\'t care what anyone thought. The phrase "Know your role and shut your mouth" landed '
    f'differently than any babyface line could have.</p>'
    f'<p>His rivalry with {a("stone-cold-steve-austin","Stone Cold Steve Austin")} is the most commercially '
    f'successful feud in wrestling history — three WrestleMania main events, two title changes, and a combined '
    f'draw that defined the Attitude Era\'s peak. Their WrestleMania XV, X-Seven, and XIX matches each told a '
    f'different story about the same two characters, which is nearly impossible to sustain over seven years.</p>'
    f'<p>His partnership with {a("mick-foley","Mick Foley")} — the Foley Is Good arc, the tag titles, "This Is '
    f'Your Life" — produced some of wrestling\'s greatest comedy, a reminder that The Rock\'s range extended '
    f'well beyond badass posturing. The People\'s Elbow, objectively the least effective finishing move in '
    f'wrestling, got the biggest reactions of any move in the Attitude Era. That was the joke. He knew it. '
    f'The crowd knew it. Everyone was in on it.</p>'
  ),
  "personas": [
    ["Rocky Maivia (1996–1997)", "Clean-cut babyface pushed too fast. Third-generation star (grandfather High Chief Peter Maivia, father Rocky Johnson). The crowd rejection forced the character evolution that made him a star."],
    ["Nation of Domination heel (1997–1998)", "Joined the Nation as a heel IC champion. Found his voice — the catchphrases, the third-person, the swagger — and the crowd turned back to him immediately."],
    ["The People's Champion (1998–2001)", "The definitive Rock era. WWF championship reigns, Austin rivalry, Hollywood crossover begins. Eight-time champion. The most electrifying man in sports entertainment."],
    ["Part-Time Hollywood Rock (2011–2016)", "Returned for WrestleMania 27 hosting, then main evented WM28 and WM29 against Cena and Punk. Box office star simultaneously filming the Fast & Furious franchise."],
  ],
  "champs": [
    ("WWF/WWE Championship", "8 reigns — 1998–2013", "Third-most WWE title reigns in history; first African-American WWF Champion"),
    ("WWF Intercontinental Championship", "2 reigns — 1997–1998"),
    ("WWF Tag Team Championship", "5 reigns — various partners including Mick Foley, Undertaker, and Chris Jericho"),
  ],
  "timeline": [
    ("1996", "WWF debut as Rocky Maivia; crowd turns on him immediately."),
    ("1997", "Joins Nation of Domination; discovers heel voice; wins IC title."),
    ("1998", "Turns babyface; wins first WWF Championship; Austin rivalry begins."),
    ("1999", "The Rock-McMahon-Foley triangle dominates Attitude Era."),
    ("2001", "WrestleMania X-Seven vs. Austin — one of the two greatest WM main events."),
    ("2003", "WrestleMania XIX loss to Austin — final match until 2011 return."),
    ("2011", "Returns to host WrestleMania XXVII; announces WM28 match vs. Cena."),
    ("2012", "Loses to Cena at WrestleMania 28 in Once in a Lifetime."),
    ("2013", "Wins WWE Championship from Punk at Royal Rumble; loses to Cena at WM29."),
    ("2023", "Returns as Board of Directors member; authority figure storyline."),
  ],
  "faq": [
    ("How many WWF/WWE Championships has The Rock won?",
     "Eight — making him one of only four performers in the eight-time club alongside Hulk Hogan, Triple H, and John Cena. He was also the first African-American WWF Champion."),
    ("What is the People's Elbow?",
     "The Rock's signature finishing move — a running elbow drop that involves removing the elbow pad, bouncing off the ropes twice, and landing a slow-motion elbow. Its deliberate theatricality was the point; the crowd reaction to the wind-up was larger than the impact itself."),
    ("Is The Rock the biggest crossover star from wrestling?",
     "By most measures, yes. Johnson transitioned from wrestling's biggest star to Hollywood's highest-paid actor, headlining the Fast & Furious franchise, Jumanji, and Black Adam while maintaining his connection to WWE. No other wrestler has achieved comparable mainstream film success."),
  ],
  "sig": [
    ("vs. Steve Austin — WrestleMania X-Seven, 2001",
     "The greatest WrestleMania main event. Austin turned heel by aligning with Vince McMahon to beat The Rock. The match had everything — a genuine crowd that erupted for Austin's win, then fell silent as Austin shook McMahon's hand."),
    ("vs. Mankind — I Quit Match, Royal Rumble 1999",
     "The Rock beat Foley with repeated chair shots while Foley's children watched from ringside. Dark, brutal, and brilliantly worked — the contrast between Rock's cruelty and Foley's refusal to quit made both men legends."),
    ("vs. Hulk Hogan — WrestleMania X8, 2002",
     "The crowd chose Hogan as the babyface, so both men went with it. The Rock lost the crowd and gave it back by selling Hogan's offense like a classic Hulkster comeback. A masterclass in real-time crowd reading."),
  ],
  "method_bars": [
    {"label":"Pinfall","pct":60},
    {"label":"Submission","pct":8},
    {"label":"Count-out / DQ","pct":22},
    {"label":"Other","pct":10},
  ],
  "matches": [
    ["ppv title", a("stone-cold-steve-austin","Steve Austin"), "WrestleMania XV", "Mar 28, 1999", "WWF Title", "Lost; Austin regained the title", "L"],
    ["ppv title", a("stone-cold-steve-austin","Steve Austin"), "WrestleMania X-Seven", "Apr 1, 2001", "No-DQ — WWF Title", "Lost; Austin's heel turn", "L"],
    ["ppv", a("hulk-hogan","Hulk Hogan"), "WrestleMania X8", "Mar 17, 2002", "Singles", "Won after Hogan babyface crowd reaction", "W"],
    ["ppv title", a("stone-cold-steve-austin","Steve Austin"), "WrestleMania XIX", "Mar 30, 2003", "Singles", "Won; Austin's last WM match", "W"],
    ["ppv", a("john-cena","John Cena"), "WrestleMania 28", "Apr 1, 2012", "Once in a Lifetime", "Lost to Cena in year-long buildup", "L"],
    ["ppv title", a("cm-punk","CM Punk"), "Royal Rumble 2013", "Jan 27, 2013", "WWE Title", "Won; Punk's 434-day reign ended", "W"],
    ["ppv title", a("john-cena","John Cena"), "WrestleMania 29", "Apr 7, 2013", "WWE Title", "Lost; Cena's 15th reign", "L"],
  ],
},
{
  "slug": "jeff-hardy",
  "name": "Jeff Hardy",
  "real_name": "Jeff Nero Hardy",
  "born": "August 31, 1977 &middot; Cameron, North Carolina",
  "hometown": "Cameron, North Carolina",
  "height": "6&prime;1&Prime; (185 cm)",
  "weight": "215 lb (98 kg)",
  "style": "High-flyer &middot; Daredevil &middot; Charismatic Enigma",
  "finisher": "Swanton Bomb",
  "desc": "Jeff Hardy — The Charismatic Enigma — brought daredevil high-flying and countercultural artistry to wrestling. Two-time WWE Champion, TLC legend, and the face of a generation of fans who wanted something real amid the spectacle.",
  "aliases": ["The Charismatic Enigma", "The Extreme Enigma", "Brother Nero (TNA)"],
  "bio": (
    f'<p>{a("jeff-hardy","Jeff Hardy")} was a genuine anomaly — a wrestler who dressed like a Mardi Gras float '
    f'and connected with crowds in ways that manufactured stars couldn\'t replicate. Where most WWE characters '
    f'were corporate constructs, Hardy was authentically strange: painting his face, wearing ripped fishnets, '
    f'and performing acts of physical recklessness that felt dangerous because they sometimes were.</p>'
    f'<p>The Hardy Boyz tag team with {a("matt-hardy","Matt Hardy")} against the Dudley Boyz and Edge &amp; '
    f'Christian produced the defining era of TLC matches, culminating in the WrestleMania X-Seven TLC II that '
    f'remains the standard against which all table/ladder/chair matches are measured. The image of Edge spearing '
    f'Jeff Hardy off a ladder — both men horizontal in mid-air — is the defining photograph of its era.</p>'
    f'<p>As a singles star, his feud with {a("cm-punk","CM Punk")} in 2009 was a masterclass in character '
    f'contrast: Punk\'s straight-edge sermons vs. Hardy\'s hedonism resonating as a genuine cultural debate '
    f'rather than a scripted wrestling storyline. Punk cashed in Money in the Bank on an injured Hardy, then '
    f'spent months cutting sermons to Hardy\'s adoring crowds — and the crowd hated every word, which meant '
    f'they were absolutely working.</p>'
  ),
  "personas": [
    ["Hardy Boyz (1998–2002, 2017)", "Tag team with Matt Hardy. Defined extreme tag wrestling with TLC matches, ladder spots, and matching face paint. One of the most beloved tag teams in history."],
    ["The Charismatic Enigma (2002–2009)", "Singles career — countercultural, face-painted, crowd-beloved. The character was essentially Jeff Hardy himself, amplified. Two WWE Championship reigns."],
    ["Brother Nero (TNA/Impact, 2016–2017)", "The Hardy Compound era. Matt Hardy 'deleted' Jeff into the Brother Nero character in one of wrestling's most bizarre and beloved creative arcs."],
  ],
  "champs": [
    ("WWE Championship", "2 reigns — 2008, 2009"),
    ("WWF/WWE Tag Team Championship", "Multiple reigns — with Matt Hardy", "Hardy Boyz among most beloved tag teams in history"),
    ("TNA/Impact World Championship", "Multiple reigns — 2011–2012"),
    ("IC / US Championship", "Multiple reigns across career"),
  ],
  "timeline": [
    ("1994", "Debuts at 16 in backyard shows in North Carolina."),
    ("1998", "Hardy Boyz formally established in WWF."),
    ("1999", "TLC era begins; Hardyz vs. Dudleyz vs. E&amp;C defines tag team wrestling."),
    ("2001", "WrestleMania X-Seven TLC II — career-defining match."),
    ("2003", "Released from WWE; signs with TNA."),
    ("2006", "Returns to WWE; builds toward singles push."),
    ("2008", "Wins first WWE Championship at Armageddon."),
    ("2009", "Feud with CM Punk; career-best promo work."),
    ("2010", "Departs WWE; returns to TNA."),
    ("2017", "Hardy Boyz return at WrestleMania 33 — standing ovation."),
  ],
  "faq": [
    ("What is Jeff Hardy's finishing move?",
     "The Swanton Bomb — a senton splash from the top rope with rotation, landing back-first on the opponent. Hardy frequently executes it from the top of ladders in TLC matches."),
    ("What happened between Jeff Hardy and CM Punk?",
     "In 2009, Punk turned heel by cashing in Money in the Bank on an injured Hardy to win the World Heavyweight Championship. He then spent months cutting straight-edge sermons to Hardy's devoted crowds, building one of WWE's most culturally resonant character contrasts of the era."),
    ("Did the Hardy Boyz ever fully reunite in WWE?",
     "Yes — in April 2017, Matt and Jeff Hardy made a surprise return at WrestleMania 33, immediately winning the Raw Tag Team Championships. The crowd reaction is widely cited as one of the most organic WrestleMania moments of the 2010s."),
  ],
  "sig": [
    ("TLC II — WrestleMania X-Seven, 2001",
     "Hardy Boyz vs. Dudley Boyz vs. Edge &amp; Christian. Edge spearing Hardy horizontally off a ladder produced the defining image of the Attitude Era. Both men dangled and fell. The match runs 16 minutes and never stops."),
    ("vs. Edge — Raw Ladder Match, 2001",
     "The one-on-one ladder match that launched TLC as a standalone concept. Hardy's high-risk spots made Edge look cruel and calculating by comparison — both men's careers elevated."),
    ("vs. CM Punk — SummerSlam 2009",
     "Loser-leaves-WWE stipulation. Punk won cleanly. Hardy left with a genuine emotional send-off that made the feud feel like a real-world moment. Both men gave everything in the most character-coherent match of either's career."),
  ],
  "method_bars": [
    {"label":"Pinfall","pct":54},
    {"label":"Submission","pct":8},
    {"label":"Count-out / DQ","pct":26},
    {"label":"Other","pct":12},
  ],
  "matches": [
    ["ppv tag", a("edge","Edge") + " &amp; Christian", "WrestleMania X-Seven", "Apr 1, 2001", "TLC II — Tag Titles", "Lost; iconic Edge spear spot", "L"],
    ["tv", a("edge","Edge"), "Raw is War", "Jul 1, 2001", "Ladder Match", "Lost; elevated both men's careers", "L"],
    ["ppv title", a("triple-h","Triple H"), "Armageddon 2008", "Dec 14, 2008", "Triple Threat — WWE Title", "Won first WWE Championship", "W"],
    ["ppv title", a("cm-punk","CM Punk"), "Raw", "Jun 8, 2009", "Singles — World Heavyweight Title", "Lost; Punk cash-in on injured Hardy", "L"],
    ["ppv", a("cm-punk","CM Punk"), "SummerSlam 2009", "Aug 23, 2009", "Loser Leaves WWE — WHC", "Lost; emotional farewell", "L"],
    ["ppv tag", a("sheamus","Sheamus") + " &amp; Cesaro", "WrestleMania 33", "Apr 2, 2017", "Raw Tag Team Championship", "Won on surprise return; massive pop", "W"],
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
    print("\nBatch 8a complete.")

if __name__ == "__main__":
    main()
