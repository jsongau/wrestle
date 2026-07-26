#!/usr/bin/env python3
"""Batch 8b — The Undertaker, Bret Hart, Chris Jericho, Kurt Angle, Matt Hardy
   Upgrades four 2-feature pages; Matt Hardy is new.
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
<div class="wl-strip" title="Last 30 matches (oldest→newest)">{spark}</div>
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
  "slug": "the-undertaker",
  "name": "The Undertaker",
  "real_name": "Mark William Calaway",
  "born": "March 24, 1965 &middot; Houston, Texas",
  "hometown": "Death Valley, California",
  "height": "6&prime;10&Prime; (208 cm)",
  "weight": "309 lb (140 kg)",
  "retired": "2020 (final Buried Alive match at Survivor Series)",
  "style": "Powerhouse &middot; Technical &middot; The Phenom",
  "finisher": "Tombstone Piledriver &middot; Hell's Gate (gogoplata)",
  "desc": "The Undertaker — The Phenom, The Deadman — ran a 21-1 WrestleMania streak across 30 years and remains the most dominant character in wrestling history. Seven-time world champion across WWF and WCW eras.",
  "aliases": ["The Deadman", "The Phenom", "Mean Mark Callous (WCW)", "The American Badass", "Big Evil"],
  "bio": (
    f'<p>{a("the-undertaker","The Undertaker")} debuted at Survivor Series 1990 and worked the same character for '
    f'30 years — an unprecedented run of character consistency in an industry that reinvents performers every '
    f'18 months. The Deadman persona, managed by Paul Bearer, was played straight from 1990 through 1998: '
    f'supernatural, methodical, unstoppable. His Survivor Series debut win over {a("hulk-hogan","Hulk Hogan")}\'s '
    f'team announced him as an immediate main event presence.</p>'
    f'<p>The WrestleMania Streak — 21 consecutive WrestleMania wins — became the most sacred number in '
    f'professional wrestling. The Streak gave every WrestleMania match against the Undertaker an existential '
    f'weight: not just a title match, but a genuine test of whether the unbreakable could be broken. His '
    f'matches with {a("shawn-michaels","Shawn Michaels")} at WM XXV and XXVI, '
    f'{a("triple-h","Triple H")} at WM XXVII and XXVIII, and {a("cm-punk","CM Punk")} at WM XXIX are the '
    f'definitive arguments for the WrestleMania match format as storytelling vehicle.</p>'
    f'<p>Brock Lesnar ending the Streak at WrestleMania XXX with an F-5 remains one of the most shocking '
    f'moments in wrestling history — the crowd sat in stunned silence as the 21–1 graphic appeared. '
    f'{a("brock-lesnar","Lesnar")} was the only choice: a genuine outside threat, not a roster member '
    f'built around the Undertaker\'s myth.</p>'
  ),
  "personas": [
    ["The Deadman (1990–1998)", "The original supernatural persona. Black hat, urn, Paul Bearer management. Walked slowly, sat up after being pinned, performed Old School. Played completely straight — no irony, no humor."],
    ["The American Badass / Big Evil (2000–2003)", "Biker persona with Kid Rock entrance music. A real-person version of Mark Calaway. Loved by some, considered a creative mistake by others. Returned the Deadman character in 2003."],
    ["The Phenom (2003–2020)", "Refined Deadman — slower, more theatrical, but with technical additions including the Hell's Gate submission. WrestleMania specialization made him the event's defining performer."],
  ],
  "champs": [
    ("WWF/WWE Championship", "4 reigns — 1991, 1997, 1999, 2002", "First title win over Hulk Hogan at Survivor Series 1991"),
    ("World Heavyweight Championship", "3 reigns — 2007–2009"),
    ("WWF Tag Team Championship", "Multiple reigns — with Big Show, Steve Austin, Kane"),
  ],
  "timeline": [
    ("1987", "Begins career as Texas Red / Mark Callous on regional circuit."),
    ("1989", "Joins WCW as Mean Mark Callous; managed by Percy Pringle (Paul Bearer)."),
    ("1990", "Debut at Survivor Series under The Undertaker character; immediate impact."),
    ("1991", "Wins first WWF Championship over Hulk Hogan at Survivor Series."),
    ("1994", "Casket Match vs. Yokozuna; 'killed' at Royal Rumble; returns at SummerSlam from the sky."),
    ("1997", "Buried Alive Match innovations; Hell in a Cell debut vs. Shawn Michaels."),
    ("1998", "Hell in a Cell vs. Mick Foley — drops Foley twice; defines hardcore era."),
    ("2000", "Returns as The American Badass biker; changes persona."),
    ("2003", "Returns Deadman persona at WrestleMania XIX."),
    ("2007", "First ECW brand championship; World Heavyweight title reign begins."),
    ("2010", "WM XXVI — beats HBK; Streak hits 18–0."),
    ("2014", "WM XXX — loses to Brock Lesnar; Streak ends at 21–1."),
    ("2017", "Retires at WrestleMania 33 after losing to Roman Reigns."),
    ("2020", "Final Boneyard match at WrestleMania 36; Buried Alive at Survivor Series."),
  ],
  "faq": [
    ("What was the Undertaker's WrestleMania Streak?",
     "The Undertaker won 21 consecutive WrestleMania matches from WM7 (1991) through WM29 (2013). The Streak ended at WrestleMania XXX (2014) when Brock Lesnar pinned him with an F-5. The 21–1 graphic appearing on screen remains one of the most shocking images in wrestling history."),
    ("Who ended the Undertaker's WrestleMania Streak?",
     "Brock Lesnar, at WrestleMania XXX in New Orleans on April 6, 2014. Lesnar hit three F-5s to pin him. The crowd response — stunned, then silent — was unprecedented. Even hardened wrestling veterans have described their genuine shock."),
    ("What is the Tombstone Piledriver?",
     "The Undertaker's primary finishing move — an inverted piledriver where the opponent is held upside down, head between the Undertaker's thighs, and driven into the mat. The follow-up pin, with Taker crossing the opponent's arms and rolling his eyes back, is one of wrestling's iconic visual sequences."),
  ],
  "sig": [
    ("vs. Shawn Michaels — WrestleMania XXV, 2009",
     "Voted the greatest WrestleMania match in history in most polls. Undertaker caught HBK mid-dive from the top rope in a deadlift, then the top-rope elbow to the floor nearly broke both men. The near-falls were genuine — crowds genuinely believed HBK might break the Streak."),
    ("vs. Mick Foley — King of the Ring 1998 (Hell in a Cell)",
     "Threw Foley off the cage roof, then through the cage top. Neither spot was a planned safe bump. Defined the extreme era and established HIAC as a match type with genuine stakes."),
    ("vs. Brock Lesnar — WrestleMania XXX, 2014",
     "The Streak ends. Lesnar pinned Undertaker after three F-5s. The silence in the Superdome as the 21–1 graphic appeared is the most stunning crowd reaction in WrestleMania history."),
    ("vs. Triple H — WrestleMania XXVIII (HIAC), 2012",
     "The End of an Era match. Shawn Michaels as special guest referee, Triple H's career on the line. Undertaker won but needed a stretcher exit. The storytelling density across 30-plus minutes made it a once-in-a-generation performance."),
  ],
  "method_bars": [
    {"label":"Pinfall","pct":50},
    {"label":"Submission","pct":18},
    {"label":"Count-out / DQ","pct":20},
    {"label":"Other","pct":12},
  ],
  "matches": [
    ["ppv title", a("hulk-hogan","Hulk Hogan"), "Survivor Series 1991", "Nov 27, 1991", "WWF Title", "Won first WWF Championship", "W"],
    ["ppv", a("shawn-michaels","Shawn Michaels"), "Badd Blood 1997", "Oct 5, 1997", "Hell in a Cell (first ever)", "Won; Hell in a Cell debut", "W"],
    ["ppv", a("mick-foley","Mick Foley"), "King of the Ring 1998", "Jun 28, 1998", "Hell in a Cell", "Won; two historic cage falls", "W"],
    ["ppv", a("stone-cold-steve-austin","Steve Austin"), "SummerSlam 1998", "Aug 30, 1998", "WWF Title", "Lost to Austin", "L"],
    ["ppv", a("shawn-michaels","Shawn Michaels"), "WrestleMania XXV", "Apr 5, 2009", "Singles", "Won; Streak 17–0; MOTY", "W"],
    ["ppv", a("shawn-michaels","Shawn Michaels"), "WrestleMania XXVI", "Mar 28, 2010", "Streak vs. Career", "Won; Streak 18–0; HBK retires", "W"],
    ["ppv", a("triple-h","Triple H"), "WrestleMania XXVII", "Apr 3, 2011", "No Holds Barred", "Won; Streak 19–0", "W"],
    ["ppv", a("triple-h","Triple H"), "WrestleMania XXVIII", "Apr 1, 2012", "Hell in a Cell — HBK as ref", "Won; Streak 20–0; End of an Era", "W"],
    ["ppv", a("cm-punk","CM Punk"), "WrestleMania XXIX", "Apr 7, 2013", "Singles", "Won; Streak 21–0", "W"],
    ["ppv", a("brock-lesnar","Brock Lesnar"), "WrestleMania XXX", "Apr 6, 2014", "Singles", "Lost; Streak ends 21–1", "L"],
    ["ppv", a("roman-reigns","Roman Reigns"), "WrestleMania 33", "Apr 2, 2017", "Singles", "Lost; symbolic retirement moment", "L"],
  ],
},
{
  "slug": "bret-hart",
  "name": "Bret Hart",
  "real_name": "Bret Sergeant Hart",
  "born": "July 2, 1957 &middot; Calgary, Alberta, Canada",
  "hometown": "Calgary, Alberta, Canada",
  "height": "6&prime;0&Prime; (183 cm)",
  "weight": "235 lb (107 kg)",
  "retired": "2000 (stroke); brief return 2010",
  "style": "Technical &middot; Scientific &middot; The Excellence of Execution",
  "finisher": "Sharpshooter (scorpion deathlock)",
  "desc": "Bret Hart — The Hitman, The Excellence of Execution — is the greatest technical wrestler of his generation. Five-time WWF Champion whose double-turn with Steve Austin and the Montreal Screwjob defined the Attitude Era's origins.",
  "aliases": ["The Hitman", "The Excellence of Execution", "The Best There Is, Was, and Ever Will Be"],
  "bio": (
    f'<p>{a("bret-hart","Bret Hart")} was trained by his father Stu Hart in the infamous Dungeon — a basement '
    f'wrestling school that produced more legitimate technical wrestlers than any comparable institution. '
    f'The Dungeon training showed in everything Hart did: clean execution, real-looking holds, transitions '
    f'that felt earned rather than choreographed.</p>'
    f'<p>His Hart Foundation tag team with {a("jim-neidhart","Jim Neidhart")} gave him the WWF exposure needed '
    f'to launch a singles career. His IC title run and subsequent WWF Championship reigns established him '
    f'as the cornerstone of the early 1990s WWF — the excellence against which everything else was measured.</p>'
    f'<p>The double-turn with {a("stone-cold-steve-austin","Steve Austin")} at WrestleMania 13 is professional '
    f'wrestling\'s most perfectly constructed single match. Hart applied the Sharpshooter; Austin bled; '
    f'Austin refused to submit and passed out. Hart left a heel, Austin a babyface, and the Attitude Era '
    f'was functionally born in that moment. Neither man planned it — they read the crowd and adjusted in real time.</p>'
    f'<p>The Montreal Screwjob — Vince McMahon ordering the referee to ring the bell during Hart\'s Sharpshooter '
    f'on {a("shawn-michaels","Shawn Michaels")} at Survivor Series 1997 — ended Hart\'s WWF career and created '
    f'the Mr. McMahon heel character that fueled the Attitude Era for three years. It also destroyed Hart\'s '
    f'relationship with WWE for over a decade, ending only with his Hall of Fame induction in 2006.</p>'
  ),
  "personas": [
    ["Hart Foundation tag team (1985–1991)", "Tag team with Jim Neidhart managed by Jimmy Hart. WWF Tag Team Champions; one of the 1980s' most reliable teams."],
    ["The Hitman — Singles star (1991–1997)", "IC champion then WWF Champion. The technical perfectionist who made every opponent look better. Canada's national wrestling hero."],
    ["Anti-American Hart Foundation (1997)", "Reformed Hart Foundation with Neidhart, Owen Hart, British Bulldog, and Brian Pillman as explicitly Canadian/anti-American faction. Cheered in Canada, booed everywhere else — a real crowd split."],
  ],
  "champs": [
    ("WWF Championship", "5 reigns — 1992–1998", "Third-most WWF title reigns in the pre-Attitude era"),
    ("WWF Intercontinental Championship", "2 reigns — 1991, 1992"),
    ("WWF Tag Team Championship", "2 reigns — with Jim Neidhart (Hart Foundation)"),
    ("WCW World Heavyweight Championship", "2 reigns — 1999", "WCW stint after Montreal Screwjob"),
  ],
  "timeline": [
    ("1976", "Begins training in Stu Hart's Dungeon in Calgary."),
    ("1984", "Signs with WWF; forms Hart Foundation with Jim Neidhart."),
    ("1987", "Wins first WWF Tag Team Championships with Neidhart."),
    ("1991", "Wins first IC title; begins singles push."),
    ("1992", "Wins first WWF Championship at SummerSlam vs. Ric Flair."),
    ("1994", "WWF title iron man match with Lex Luger; wins in 1994 SummerSlam."),
    ("1996", "60-minute Iron Man Match loss to Shawn Michaels at WM XII."),
    ("1997", "Double-turn with Austin at WM 13; Montreal Screwjob at Survivor Series."),
    ("1997", "Signs with WCW; disappointing run due to booking."),
    ("1999", "WCW Championship reigns but creatively misused."),
    ("2000", "Retirement after suffering a stroke caused by a Goldberg kick."),
    ("2006", "WWE Hall of Fame inductee; reconciliation with WWE."),
    ("2010", "Returns for limited Raw appearances; WrestleMania 26 appearance."),
  ],
  "faq": [
    ("What is the Sharpshooter?",
     "Bret Hart's finishing submission — a scorpion deathlock applied from behind. Hart crosses the opponent's legs, steps between them, and applies pressure by leaning back. The Montreal Screwjob involved the referee calling for the bell while Hart had the Sharpshooter applied on Shawn Michaels."),
    ("What was the Montreal Screwjob?",
     "At Survivor Series 1997, Vince McMahon secretly ordered referee Earl Hebner to call for the bell (signaling Shawn Michaels had submitted) while Hart had the Sharpshooter applied. Hart had not submitted. McMahon screwed Hart out of the WWF Championship on Hart's last night before jumping to WCW. The incident is wrestling's most documented real-world controversy."),
    ("What happened to Bret Hart in WCW?",
     "Hart was creatively misused in WCW, stuck in midcard feuds despite being the company's highest-paid performer. He suffered a concussion from a Goldberg kick in 1999 that caused a stroke. He retired in 2000, never returning to full-time competition."),
  ],
  "sig": [
    ("vs. Steve Austin — WrestleMania 13, 1997 (Submission Match)",
     "The double-turn. Hart applied the Sharpshooter; Austin bled from the face and refused to submit. Both men worked with total commitment. Hart left a heel; Austin left a babyface. The crowd switch happened in real time. Wrestling's most precisely constructed character moment."),
    ("vs. Shawn Michaels — WrestleMania XII, 1996 (Iron Man Match)",
     "60 minutes, 0–0 through regulation. Hart wanted to go over; Michaels won in overtime. The match itself is a masterpiece of pacing and endurance — both men maintained legitimate athletic intensity across the full hour."),
    ("vs. Steve Owen Hart — SummerSlam 1994",
     "A technical clinic between brothers. Owen had won the King of the Ring and earned the title shot; Bret retained via small package. One of the WWF's best pure wrestling matches of the decade."),
  ],
  "method_bars": [
    {"label":"Pinfall","pct":42},
    {"label":"Submission","pct":35},
    {"label":"Count-out / DQ","pct":16},
    {"label":"Other","pct":7},
  ],
  "matches": [
    ["ppv title", a("ric-flair","Ric Flair"), "SummerSlam 1992", "Aug 29, 1992", "WWF Title", "Won first WWF Championship", "W"],
    ["ppv title", a("shawn-michaels","Shawn Michaels"), "WrestleMania XII", "Mar 31, 1996", "60-Min Iron Man — WWF Title", "Lost in overtime", "L"],
    ["ppv", a("stone-cold-steve-austin","Steve Austin"), "WrestleMania 13", "Mar 23, 1997", "Submission Match", "Won; Austin passed out; double-turn", "W"],
    ["ppv title", a("shawn-michaels","Shawn Michaels"), "Survivor Series 1997", "Nov 9, 1997", "WWF Title — Montreal", "Lost via screwjob; left WWF", "L"],
    ["ppv title", a("stone-cold-steve-austin","Steve Austin"), "Survivor Series 1996", "Nov 17, 1996", "WWF Title", "Lost", "L"],
    ["ppv", a("the-undertaker","The Undertaker"), "SummerSlam 1997", "Aug 3, 1997", "WWF Title (special ref HBK)", "Lost via ref bump interference", "L"],
  ],
},
{
  "slug": "chris-jericho",
  "name": "Chris Jericho",
  "real_name": "Christopher Keith Irvine",
  "born": "November 9, 1970 &middot; Manhasset, New York",
  "hometown": "Winnipeg, Manitoba, Canada",
  "height": "6&prime;0&Prime; (183 cm)",
  "weight": "227 lb (103 kg)",
  "style": "Technical &middot; Showman &middot; Le Champion",
  "finisher": "Walls of Jericho (elevated Boston crab) &middot; Judas Effect (back elbow)",
  "desc": "Chris Jericho — Y2J, Le Champion, The Painmaker — is the most adaptable performer in wrestling history. First Undisputed Champion, AEW founding star, and a performer who has reinvented himself successfully every five years across 30-plus years.",
  "aliases": ["Y2J", "Le Champion", "The Painmaker", "The Demo God", "Lionheart (early career)"],
  "bio": (
    f'<p>{a("chris-jericho","Chris Jericho")} debuted in WWF on August 9, 1999, interrupting {a("the-rock","The Rock")} '
    f'at 2:52 AM with the Y2J countdown and an immediate pop that announced him as a made main eventer from '
    f'day one. The debut is studied as a masterclass in introduction — the moment, the setting, the confidence '
    f'of his first line. He\'d earned it through years of work in Mexico, Japan, WCW, and ECW.</p>'
    f'<p>His feuds with {a("the-rock","The Rock")} and {a("stone-cold-steve-austin","Steve Austin")} and '
    f'{a("triple-h","Triple H")} established his credential. His 2001 Undisputed Championship — first in '
    f'wrestling history, unifying the WWF and WCW titles — was the historic peak of his Attitude Era run.</p>'
    f'<p>But Jericho\'s greatest achievement may be his reinvention. The Walls of Jericho became the Liontamer '
    f'again; the rock band Fozzy became part of the gimmick; the scarf, the jacket, the List of Jericho, '
    f'the Inner Circle — each iteration drew fresh audiences. His AEW arrival in 2019 as founding champion '
    f'provided the promotion with immediate credibility it couldn\'t have bought otherwise.</p>'
  ),
  "personas": [
    ["Y2J (1999–2005)", "The millennium countdown debut, the lists, the Walls of Jericho. Cocky, funny, legitimately dangerous. The perfect Attitude Era mix of comedy and technical excellence."],
    ["The Best in the World (2008–2012)", "More serious heel, the Lite-Brite jacket era. Feuds with Shawn Michaels and CM Punk. Longer matches, less comedy, more psychological depth."],
    ["Le Champion / The Demo God (2019–present)", "AEW era. Blood and Guts, the Inner Circle, the Jericho Appreciation Society. Proved that reinvention can happen indefinitely when the performer is skilled enough."],
  ],
  "champs": [
    ("WWF/WWE Undisputed Championship", "1 reign — 2001–2002", "First Undisputed Champion in history — unified WWF and WCW titles"),
    ("WWF/WWE Championship", "6 reigns — various", "Including the famous simultaneous Raw and SmackDown championship"),
    ("AEW World Championship", "Multiple reigns — 2019–present", "AEW's founding champion; gave the promotion immediate credibility"),
    ("IC / Intercontinental Championship", "9 reigns", "Record-holder for most Intercontinental title reigns"),
  ],
  "timeline": [
    ("1990", "Debut in Calgary; trains in Hart family tradition."),
    ("1993", "Mexico and Japan tours; technical credibility established."),
    ("1996", "Joins WCW; underutilized despite excellent matches."),
    ("1999", "WWF debut interrupts The Rock at 2:52 AM — instant main eventer."),
    ("2001", "Wins Undisputed Championship — first in wrestling history."),
    ("2005", "Departs WWE; focuses on Fozzy."),
    ("2007", "Returns to WWE; more serious character approach."),
    ("2012", "Departs again; multi-year AEW/indie run begins."),
    ("2019", "AEW founding debut and inaugural champion."),
  ],
  "faq": [
    ("What is the Walls of Jericho?",
     "Jericho's submission — an elevated Boston crab where he sits on the opponent's back and pulls their legs toward their head, bending the spine. Originally applied as the Liontamer with more direct pressure on the neck. The Walls became his signature submission after the move was softened for WWF."),
    ("Was Chris Jericho really the first Undisputed Champion?",
     "Yes — Jericho unified the WWF Championship (won from The Rock) and the WCW Championship (won from Steve Austin) in the same night on December 9, 2001, to become the first Undisputed WWF Champion in history. The Undisputed title format continues today as the basis of the Unified WWE Championship."),
    ("How many times has Chris Jericho reinvented himself?",
     "At least four major persona shifts: Y2J (1999–2005), the serious heel Best in the World era (2007–2012), the scarf-wearing rock star era (2013–2018), and the AEW Le Champion/Demo God era (2019–present). Each reinvention drew new audiences while retaining the existing fanbase."),
  ],
  "sig": [
    ("vs. The Rock and Steve Austin — No Mercy 2001 (Undisputed Title)",
     "Won the WWF Championship from The Rock, then later the same night won the WCW Championship from Steve Austin to unify both titles. The first Undisputed Champion in history, celebrated by pouring champagne on a prone Austin."),
    ("vs. Shawn Michaels — No Mercy 2008",
     "A series of matches built on Jericho's obsession with HBK that escalated across the year. Their ladder match and subsequent bouts showed Jericho at his most psychologically complex as a heel."),
    ("vs. CM Punk — WrestleMania XXVIII, 2012",
     "Jericho's best work vs. Punk's peak as WWE Champion. A match built on real-world details — Punk's straight-edge family, Jericho's verbal cruelty — that the crowd read as authentic."),
  ],
  "method_bars": [
    {"label":"Pinfall","pct":48},
    {"label":"Submission","pct":30},
    {"label":"Count-out / DQ","pct":16},
    {"label":"Other","pct":6},
  ],
  "matches": [
    ["ppv title", a("the-rock","The Rock"), "Vengeance 2001", "Dec 9, 2001", "WWF Title — Undisputed unification", "Won first title; Undisputed history", "W"],
    ["ppv title", a("stone-cold-steve-austin","Steve Austin"), "Vengeance 2001", "Dec 9, 2001", "WCW Title — Undisputed unification", "Won; first Undisputed Champion", "W"],
    ["ppv title", a("triple-h","Triple H"), "WrestleMania X8", "Mar 17, 2002", "Undisputed Title", "Lost; HHH won the title", "L"],
    ["ppv", a("shawn-michaels","Shawn Michaels"), "No Mercy 2008", "Oct 5, 2008", "Ladder — IC Title", "Won; best match of this feud", "W"],
    ["ppv", a("cm-punk","CM Punk"), "WrestleMania XXVIII", "Apr 1, 2012", "Singles — WWE Title", "Lost to Punk", "L"],
    ["ppv", a("roman-reigns","Roman Reigns"), "AEW/WWE crossover feuds", "2021–2022", "Various", "Major feuds in both promotions", "L"],
  ],
},
{
  "slug": "kurt-angle",
  "name": "Kurt Angle",
  "real_name": "Kurt Steven Angle",
  "born": "December 9, 1968 &middot; Pittsburgh, Pennsylvania",
  "hometown": "Pittsburgh, Pennsylvania",
  "height": "6&prime;2&Prime; (188 cm)",
  "weight": "220 lb (100 kg)",
  "retired": "2019 (final match at WrestleMania 35)",
  "style": "Amateur wrestling &middot; Submission specialist &middot; Legitimate athlete",
  "finisher": "Angle Slam &middot; Ankle Lock",
  "desc": "Kurt Angle — the only Olympic gold medalist to become a professional wrestling world champion. Six-time world champion whose technical legitimacy, comedic timing, and intensity across 20 years place him among the five greatest performers in wrestling history.",
  "aliases": ["The Wrestling Machine", "The Olympic Hero", "The Gold Medalist"],
  "bio": (
    f'<p>{a("kurt-angle","Kurt Angle")} won the Olympic gold medal in freestyle wrestling at the 1996 Atlanta '
    f'Games — with a broken frickin\' neck, as he reminded audiences approximately twice per promo. When he '
    f'arrived in WWF in 1999, the legitimate athletic credibility was instantly apparent. He could make every '
    f'opponent\'s offense look real because he knew exactly how to absorb it, and he could make his own offense '
    f'look devastating because it sometimes actually was.</p>'
    f'<p>His early heel run — as the obnoxious, rule-quoting, milk-drinking Olympic hero — was comedic gold '
    f'executed by a man who could back up every claim in the ring. The contrast produced a character type '
    f'wrestling rarely achieves: genuinely funny AND genuinely threatening. His matches with '
    f'{a("chris-benoit","Chris Benoit")}, {a("shawn-michaels","Shawn Michaels")}, and '
    f'{a("brock-lesnar","Brock Lesnar")} are technical clinics that required no suspension of disbelief.</p>'
    f'<p>His WrestleMania XXI match with {a("shawn-michaels","Shawn Michaels")} — combining Angle\'s legitimate '
    f'wrestling base with HBK\'s bump-taking genius — is frequently cited alongside WM XXV as the two '
    f'greatest WrestleMania technical matches. Both men gave the other their best.</p>'
  ),
  "personas": [
    ["The Olympic Hero — Comedic Heel (1999–2001)", "Rule-quoting, milk-drinking, 'you suck' chant-inspiring heel who lectured crowds on intensity, integrity, and intelligence. Legitimately funny while being legitimately terrifying in the ring."],
    ["The Wrestling Machine — Serious Heel (2001–2006)", "Stripped-down, intense version. Feuded with Brock Lesnar, Undertaker, and HBK with pure technical focus. Won multiple world titles in this era."],
    ["TNA Hall of Fame Run (2006–2016)", "TNA Championship runs and creative freedom. Critically acclaimed matches with AJ Styles and Samoa Joe before returning to WWE."],
  ],
  "champs": [
    ("WWF/WWE Championship", "4 reigns — 2000–2006"),
    ("World Heavyweight Championship", "2 reigns — 2005–2007"),
    ("WWF European Championship", "1 reign — 2000"),
    ("WWF/WWE Intercontinental Championship", "1 reign"),
    ("TNA World Heavyweight Championship", "Multiple reigns — 2006–2016"),
  ],
  "timeline": [
    ("1996", "Wins Olympic gold medal at Atlanta Games — freestyle wrestling."),
    ("1998", "Signs developmental deal with WWF."),
    ("1999", "WWF debut; immediate push as comedic-but-dangerous heel."),
    ("2000", "Wins first WWF Championship; begins serious main event run."),
    ("2002", "Brock Lesnar's rise; Angle-Lesnar feud produces technical classics."),
    ("2005", "WM XXI vs. HBK — career-best singles match."),
    ("2006", "Leaves WWE for TNA; multiple championship reigns."),
    ("2017", "Returns to WWE as Raw GM; limited in-ring schedule."),
    ("2019", "Final match at WrestleMania 35 vs. Baron Corbin; retires."),
  ],
  "faq": [
    ("Did Kurt Angle really win an Olympic gold medal?",
     "Yes — Angle won the gold in freestyle wrestling (220 lb class) at the 1996 Atlanta Olympic Games. He did so while competing with a broken neck suffered at the Olympic trials, which became the basis of his most famous character claim: 'I won an Olympic gold medal with a broken frickin' neck.'"),
    ("What is the Ankle Lock?",
     "Angle's finishing submission — he grabs the opponent's ankle and applies a 90-degree twist while dropping his body weight backward. Legitimately painful due to his amateur wrestling background and the real mechanics of the torque applied. Often countered by a roll-through, requiring Angle to re-apply."),
    ("What was Angle's best match?",
     "Debated, but WrestleMania XXI vs. Shawn Michaels (2005) is the most cited answer. The match combined Angle's legitimate wrestling base with HBK's selling and storytelling in 27 minutes that built to a believable near-fall sequence. Their rematch on Raw is also considered a TV classic."),
  ],
  "sig": [
    ("vs. Shawn Michaels — WrestleMania XXI, 2005",
     "Twenty-seven minutes of technical and theatrical perfection. Angle applied the Ankle Lock five times; HBK nearly submitted each time. The final sequence — HBK rolling through into a crucifix — was a finish so clean that both men stood up and embraced afterward. Standing ovation."),
    ("vs. Brock Lesnar — WrestleMania XIX, 2003",
     "Lesnar attempted a Shooting Star Press from the top rope and landed on his head in one of wrestling's scariest moments. Angle covered for him immediately, called the match to its finish, and got a full crowd response despite the near-disaster."),
    ("vs. Chris Benoit — Royal Rumble 2003",
     "A 30-minute technical masterpiece between two legitimate wrestlers. Every hold had counters; every counter had counters. Benoit submitted with the crossface; Angle kicked out of it. The finish was a German suplex sequence that drew the crowd to its feet."),
  ],
  "method_bars": [
    {"label":"Pinfall","pct":42},
    {"label":"Submission","pct":38},
    {"label":"Count-out / DQ","pct":14},
    {"label":"Other","pct":6},
  ],
  "matches": [
    ["ppv title", a("the-rock","The Rock"), "No Mercy 2000", "Oct 22, 2000", "WWF Title", "Won first WWF Championship", "W"],
    ["ppv title", a("brock-lesnar","Brock Lesnar"), "WrestleMania XIX", "Mar 30, 2003", "WWE Title", "Lost; Lesnar botched SSP but they finished", "L"],
    ["ppv", a("shawn-michaels","Shawn Michaels"), "WrestleMania XXI", "Apr 3, 2005", "Singles", "Lost in a match of the year classic", "L"],
    ["ppv title", a("john-cena","John Cena"), "Unforgiven 2005", "Sep 18, 2005", "WWE Title", "Lost to Cena", "L"],
    ["ppv", a("rey-mysterio","Rey Mysterio") + " &amp; " + a("randy-orton","Randy Orton"), "WrestleMania 22", "Apr 2, 2006", "World Heavyweight Title (Triple Threat)", "Lost to Rey Mysterio; Eddie tribute match", "L"],
    ["ppv", a("samoa-joe","Samoa Joe"), "TNA Lockdown 2008", "Apr 13, 2008", "TNA World Title — Steel Cage", "Lost to Joe; great cage match", "L"],
  ],
},
{
  "slug": "matt-hardy",
  "name": "Matt Hardy",
  "real_name": "Matthew Moore Hardy",
  "born": "September 23, 1974 &middot; Cameron, North Carolina",
  "hometown": "Cameron, North Carolina",
  "height": "6&prime;2&Prime; (188 cm)",
  "weight": "236 lb (107 kg)",
  "style": "Powerhouse &middot; Brawler &middot; Resilient storyteller",
  "finisher": "Twist of Fate &middot; Swanton Bomb (as Woken Matt)",
  "desc": "Matt Hardy — Version 1, WOKEN — is the cerebral Hardy who outlasted everyone's expectations. Tag team legend, solo champion, and architect of wrestling's most surrealist extended storyline: The Hardy Compound universe.",
  "aliases": ["Version 1", "WOKEN Matt Hardy", "Broken Matt Hardy", "The Sensei of Mattitude"],
  "bio": (
    f'<p>{a("matt-hardy","Matt Hardy")} was always the thinking Hardy — where {a("jeff-hardy","Jeff Hardy")} '
    f'threw himself off ladders, Matt studied tape, developed systems, and built one of the early internet\'s '
    f'most passionate wrestling fanbases. The Hardy Boyz tag team ran on complementary contrasts: Jeff\'s '
    f'instinct vs. Matt\'s calculation, Jeff\'s recklessness vs. Matt\'s structure.</p>'
    f'<p>His "Matt Hardy Version 1" solo gimmick — complete with the Mattitude philosophy, the MFer (Matt '
    f'Facts) graphics, and Shannon Moore as a Mattitude follower — was one of the most creative uses of '
    f'internet-era wrestling fandom, acknowledging and absorbing the character\'s online following into the '
    f'storyline itself.</p>'
    f'<p>The Broken/WOKEN Matt Hardy saga, originating in TNA in 2016, was professional wrestling\'s most '
    f'genuinely surrealist creative achievement. Matt "deleted" his brother Jeff into the character Brother '
    f'Nero; they battled across the Hardy Compound in cinematic match segments years before cinematic matches '
    f'became a pandemic-era staple. The "DELETE!" chants became a legitimate cultural phenomenon.</p>'
  ),
  "personas": [
    ["Hardy Boyz (1998–2002, 2017)", "Tag team with Jeff Hardy. TLC architects and one of wrestling's most beloved teams. The brothers were equally matched in the ring; the tag chemistry was the point."],
    ["Matt Hardy Version 1 (2003–2005)", "Solo heel character with the Mattitude philosophy. Matt Facts on the titantron, Shannon Moore as a follower. Funny, committed, underrated as a solo run."],
    ["Broken / WOKEN Matt Hardy (2016–2019)", "Surrealist character with cinematic battles at the Hardy Compound. 'DELETE!' became a genuine crowd phenomenon. Brought the character to WWE as WOKEN Matt Hardy in 2018."],
  ],
  "champs": [
    ("WWE/ECW Championship", "Multiple reigns — ECW Championship 2009"),
    ("WWF/WWE Tag Team Championship", "Multiple reigns — with Jeff Hardy", "Hardy Boyz among the most beloved tag teams in history"),
    ("WWF European Championship", "Multiple reigns — 2001–2002"),
    ("TNA World Tag Team Championship", "Multiple reigns — with Jeff Hardy", "Broken Hardy Boyz TNA run produced iconic segments"),
  ],
  "timeline": [
    ("1993", "First professional match in North Carolina backyard circuit."),
    ("1998", "Hardy Boyz formally established in WWF; TLC era begins."),
    ("2002", "Turns heel as Matt Hardy Version 1; solo run begins."),
    ("2005", "Released by WWE; internet backlash storyline with Lita and Edge."),
    ("2006", "Returns to WWE SmackDown."),
    ("2009", "Wins ECW Championship; first major solo title."),
    ("2016", "TNA debut of Broken Matt Hardy — surrealist masterpiece begins."),
    ("2017", "Hardy Boyz return at WrestleMania 33 with Jeff."),
    ("2018", "WOKEN Matt Hardy debuts on Raw; 'DELETE!' era in WWE."),
    ("2019", "Joins AEW at Double or Nothing."),
  ],
  "faq": [
    ("What is Matt Hardy's Twist of Fate?",
     "A cutter/stunner-style move where Hardy grabs the opponent's head with both hands and drops to a sitting position, driving the opponent's face toward the mat. Popularized as part of the Hardy Boyz tandem offense in the TLC era."),
    ("What was the Broken Matt Hardy storyline?",
     "In 2016, Matt Hardy developed a surrealist heel character in TNA where he 'broke' himself and others through a combination of real-world location shoots at the Hardy Compound, drone warfare, and philosophical pronouncements in an exaggerated accent. DELETE! became a crowd chant. The storyline is considered professional wrestling's most creative character work of the 2010s."),
    ("Did Matt Hardy and Jeff Hardy ever reunite?",
     "Multiple times — most memorably at WrestleMania 33 in 2017, where both brothers made a surprise return to win the Raw Tag Team Championships. They later reunited in AEW in 2020, continuing their career-spanning partnership."),
  ],
  "sig": [
    ("TLC II — WrestleMania X-Seven, 2001",
     "Hardy Boyz vs. Dudley Boyz vs. Edge &amp; Christian. The greatest tag team match in WrestleMania history. Matt's positioning and ring awareness in multi-man chaos showed his structural instincts alongside Jeff's improvised high spots."),
    ("vs. Edge — Ladder Match, Raw 2001",
     "Matt against the man who would steal his real-life girlfriend Lita years later. The irony of their ladder match chemistry makes the later real-world feud more resonant in retrospect."),
    ("FINAL DELETION — TNA Impact, 2016",
     "Broken Matt Hardy vs. Jeff Hardy (Brother Nero) in the Hardy Compound. Drone warfare, fireworks, a lake battle, and a genuinely funny surrealist wrestling match. The segment changed what people thought professional wrestling's non-ring segments could look like."),
  ],
  "method_bars": [
    {"label":"Pinfall","pct":52},
    {"label":"Submission","pct":12},
    {"label":"Count-out / DQ","pct":24},
    {"label":"Other","pct":12},
  ],
  "matches": [
    ["ppv tag", a("edge","Edge") + " &amp; Christian", "WrestleMania X-Seven", "Apr 1, 2001", "TLC II — Tag Titles", "Lost; match of the year", "L"],
    ["ppv tag", a("edge","Edge") + " &amp; Christian", "SummerSlam 1999", "Aug 22, 1999", "TLC I — Tag Titles", "Won; TLC era begins", "W"],
    ["ppv title", a("john-cena","John Cena"), "No Mercy 2008", "Oct 5, 2008", "ECW Title (after injury)", "Won ECW Championship", "W"],
    ["ppv tag", a("sheamus","Sheamus") + " &amp; Cesaro", "WrestleMania 33", "Apr 2, 2017", "Raw Tag Team Title — surprise return", "Won; massive pop with Jeff", "W"],
    ["ppv", a("jeff-hardy","Jeff Hardy (Brother Nero)"), "TNA Slammiversary XIV", "Jun 12, 2016", "Ladder Match for Broken glory", "Won; Broken universe begins", "W"],
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
    print("\nBatch 8b complete.")

if __name__ == "__main__":
    main()
