#!/usr/bin/env python3
"""Batch 12 — Moments content type: famous in-ring incidents/moments with embedded video.
4 moment pages + /moments/ index. Broadcast Bold chrome, anti-AI copy standard.
Video: verified official WWE YouTube IDs embedded via existing facade; official-search
fallback where no official upload is confirmed. No fabricated IDs.
Domain: matwrestling.com (site canonical).
"""
import os, re

DOMAIN = "https://matwrestling.com"
OUT = "/root/wwe"

def a(slug, name):
    return f'<a href="/wrestlers/{slug}/">{name}</a>'

def yt_search(q):
    from urllib.parse import quote_plus
    return "https://www.youtube.com/results?search_query=" + quote_plus(q)

# ── chrome ──────────────────────────────────────────────────────────────────
def head(title, desc, canonical_path, extra_ld=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}{canonical_path}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://www.youtube-nocookie.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Oswald:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/site.css">
{extra_ld}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap"><nav class="nav" aria-label="Primary">
  <a class="brand" href="/"><span class="brand__mark"><span>M</span></span> MAT</a>
  <button class="nav__toggle" aria-label="Toggle menu" aria-controls="primary-menu" aria-expanded="false">&#9776;</button>
  <ul class="nav__menu" id="primary-menu">
    <li class="nav__item"><a class="nav__link" href="/wrestlers/">Wrestlers</a></li>
    <li class="nav__item"><a class="nav__link" href="/matches/">Matches</a></li>
    <li class="nav__item"><a class="nav__link" href="/events/">Events</a></li>
    <li class="nav__item"><a class="nav__link" href="/moments/">Moments</a></li>
    <li class="nav__item"><a class="nav__link" href="/rankings/">Rankings</a></li>
    <li class="nav__item"><a class="nav__cta" href="/membership/">Join MAT Insider</a></li>
  </ul>
</nav></div></header>
"""

def footer():
    return """<footer class="site-footer"><div class="wrap">
  <p>&copy; 2026 MAT Wrestling Database. All rights reserved.</p>
  <nav><a href="/about/">About</a> · <a href="/privacy/">Privacy</a> · <a href="/contact/">Contact</a></nav>
</div></footer>
<script src="/js/main.js"></script>
</body>
</html>"""

def crumbs(items):
    lis = ""
    for label, href in items:
        lis += f'<li><a href="{href}">{label}</a></li>' if href else f'<li aria-current="page">{label}</li>'
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{lis}</ol></nav>\n'

def faq_ld_items(faq):
    if not faq:
        return ""
    items = ""
    for q, ans in faq:
        sq = q.replace('"', '&quot;')
        sa = re.sub(r'<[^>]+>', '', ans).replace('"', '&quot;')
        items += f'{{"@type":"Question","name":"{sq}","acceptedAnswer":{{"@type":"Answer","text":"{sa}"}}}},'
    return items.rstrip(",")

def faq_block(faq):
    if not faq:
        return ""
    html = "".join(f'<details><summary>{q}</summary><div class="faq__body">{ans}</div></details>\n' for q, ans in faq)
    return '<div class="sec-h"><h2>FAQ</h2></div>\n<div class="faq faq-block">\n' + html + '</div>\n'

def video_html(m):
    """Embedded official clip, or official-search facade fallback."""
    v = m["video"]
    ph = v["ph"]
    if v["mode"] == "embed":
        vid = v["id"]
        return (
            f'<div class="embed">\n'
            f'  <button class="facade" data-provider="youtube" data-id="{vid}" '
            f'aria-label="Play the official WWE clip: {m["name"]}">\n'
            f'    <img class="facade__poster" src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" '
            f'alt="" loading="lazy" width="480" height="360">\n'
            f'    <span class="facade__ph">{ph}</span>\n'
            f'    <span class="facade__btn" aria-hidden="true">&#9654;</span>\n'
            f'  </button>\n'
            f'</div>\n'
            f'<p class="form-note">Official WWE upload. If the clip does not load in your region, '
            f'<a href="{v["search"]}" target="_blank" rel="noopener">search WWE on YouTube</a>. '
            f'In China, WWE clips are on Bilibili and Youku.</p>\n'
        )
    # search fallback
    return (
        f'<div class="embed">\n'
        f'  <button class="facade" type="button" '
        f'onclick="window.open(\'{v["search"]}\',\'_blank\',\'noopener\');return false;" '
        f'aria-label="Search the official WWE clip: {m["name"]}">\n'
        f'    <span class="facade__ph">{ph}</span>\n'
        f'    <span class="facade__btn" aria-hidden="true">&#9654;</span>\n'
        f'  </button>\n'
        f'</div>\n'
        f'<p class="form-note">Opens the official WWE search on YouTube. A verified embed ID drops '
        f'straight into this player once confirmed. In China, WWE clips are on Bilibili and Youku.</p>\n'
    )

def video_object_ld(m):
    v = m["video"]
    if v["mode"] != "embed":
        return ""  # no VideoObject without a specific verified video
    vid = v["id"]
    name = m["name"].replace('"', '&quot;')
    desc = m["ld_desc"].replace('"', '&quot;')
    return (
        ',\n    {"@type":"VideoObject",'
        f'"name":"{name}",'
        f'"description":"{desc}",'
        f'"thumbnailUrl":"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",'
        f'"embedUrl":"https://www.youtube-nocookie.com/embed/{vid}",'
        f'"contentUrl":"https://www.youtube.com/watch?v={vid}"'
        '}'
    )

# ═══════════════════════════════════════════════════════════════════════════
MOMENTS = [

{
    "slug": "triple-h-tears-his-quad-2001",
    "name": "Triple H Tears His Quad (2001)",
    "kicker": "Career-altering injury",
    "date_display": "May 21, 2001",
    "event": "Raw (WWF)",
    "city": "San Jose, California",
    "desc": "On May 21, 2001, Triple H tore his left quadriceps off the bone during a Raw tag title match, finished the bout, and lost eight months. It ended the Two-Man Power Trip.",
    "ld_desc": "Triple H tears his quadriceps during a WWF tag team title match on Raw, May 21, 2001.",
    "intro": (
        "On May 21, 2001, " + a("triple-h","Triple H") + " tore his left quadriceps muscle off the bone in the "
        "middle of a Raw tag team title match. He finished the bout on one leg, then spent roughly eight months "
        "out of action. The injury broke up the Two-Man Power Trip at the peak of its run."
    ),
    "video": {"mode":"search", "ph":"RAW 2001",
              "search": yt_search("WWE Triple H tears his quad Raw May 21 2001")},
    "body": (
        "<p>" + a("triple-h","Triple H") + " and " + a("stone-cold-steve-austin","Steve Austin") + " had spent "
        "the spring of 2001 as the Two-Man Power Trip, holding the WWF Championship, Intercontinental Championship, "
        "and Tag Team Championship between them. On the May 21 Raw, they defended the tag titles against "
        + a("chris-benoit","Chris Benoit") + " and " + a("chris-jericho","Chris Jericho") + ".</p>"
        "<p>Late in the match, Triple H's left quadriceps tore completely off the bone. He stayed in the match and "
        "finished it, but the damage required surgery and a rehabilitation that kept him out until his return in "
        "January 2002. The Power Trip ended that night, and Benoit and Jericho left as tag team champions.</p>"
        "<p>The injury and the comeback became part of Triple H's legend. His return at Madison Square Garden in "
        "2002 drew one of the loudest ovations of the era.</p>"
    ),
    "related": [("triple-h","Triple H"), ("stone-cold-steve-austin","Steve Austin"),
                ("chris-benoit","Chris Benoit"), ("chris-jericho","Chris Jericho")],
    "faq": [
        ("When did Triple H tear his quad?",
         "Triple H tore his left quadriceps on the May 21, 2001 episode of Raw, during a tag team title match teaming with Steve Austin against Chris Benoit and Chris Jericho."),
        ("How long was Triple H out after the quad injury?",
         "Triple H was out of action for roughly eight months. He returned in January 2002 to a major ovation and went on to headline WrestleMania X8."),
        ("What was the Two-Man Power Trip?",
         "The Two-Man Power Trip was the 2001 team of Triple H and Steve Austin, who together held the WWF, Intercontinental, and Tag Team Championships. It ended the night Triple H tore his quad."),
    ],
},

{
    "slug": "mankind-hell-in-a-cell-fall-1998",
    "name": "Mankind's Hell in a Cell Fall (1998)",
    "kicker": "The most famous bump in wrestling",
    "date_display": "June 28, 1998",
    "event": "King of the Ring",
    "city": "Pittsburgh, Pennsylvania",
    "desc": "At King of the Ring 1998, The Undertaker threw Mankind off the top of the 16-foot Hell in a Cell through the announce table, then chokeslammed him through the roof. JR called it: 'He is broken in half.'",
    "ld_desc": "The Undertaker throws Mankind off the top of the Hell in a Cell at King of the Ring, June 28, 1998.",
    "intro": (
        "At King of the Ring 1998, " + a("the-undertaker","The Undertaker") + " threw " + a("mick-foley","Mankind") +
        " off the top of the 16-foot Hell in a Cell structure and through the Spanish announce table below. "
        "Minutes later, a chokeslam sent Mankind through the roof of the cell to the mat. Jim Ross's call, "
        "\"As God as my witness, he is broken in half,\" became the most quoted line in wrestling commentary."
    ),
    "video": {"mode":"embed", "id":"9hMp65SzyTU", "ph":"KOTR 98",
              "search": yt_search("WWE Undertaker throws Mankind off Hell in a Cell King of the Ring 1998")},
    "body": (
        "<p>The match was the second-ever Hell in a Cell. Rather than wrestle inside the structure, "
        + a("mick-foley","Mankind") + " climbed to the top and " + a("the-undertaker","The Undertaker") +
        " followed. The first fall, a throw from the roof through the announce table, was planned. The second, a "
        "chokeslam that broke the cell panel and dropped Mankind to the ring, was not meant to happen the way it did.</p>"
        "<p>Foley suffered a dislocated shoulder, a bruised kidney, knocked-out teeth, and a concussion, yet he "
        "continued the match. The bout is studied as both a masterclass in drawing an emotional crowd response and a "
        "cautionary example of the physical cost of that era's spectacle.</p>"
        "<p>Foley has said he does not remember large portions of the match. It remains the moment most casual viewers "
        "associate with him and one of the most searched clips in wrestling history.</p>"
    ),
    "related": [("mick-foley","Mankind / Mick Foley"), ("the-undertaker","The Undertaker")],
    "faq": [
        ("What happened to Mankind at King of the Ring 1998?",
         "The Undertaker threw Mankind off the top of the Hell in a Cell through the announce table, then chokeslammed him through the roof of the cell to the mat. Mankind suffered a dislocated shoulder, a concussion, and knocked-out teeth but finished the match."),
        ("What did Jim Ross say during the Hell in a Cell fall?",
         "Jim Ross's call, 'As God as my witness, he is broken in half,' became the most famous line in wrestling commentary. He also shouted, 'Good God almighty, they've killed him,' after the second fall."),
        ("Did Mankind win the Hell in a Cell match?",
         "No. The Undertaker won the match. The bout is remembered for the two falls rather than the finish, and it is considered one of the defining moments of the Attitude Era."),
    ],
},

{
    "slug": "steve-austin-broken-neck-1997",
    "name": "Steve Austin Breaks His Neck (1997)",
    "kicker": "The botch that changed a career",
    "date_display": "August 3, 1997",
    "event": "SummerSlam",
    "city": "East Rutherford, New Jersey",
    "desc": "At SummerSlam 1997, a mistimed piledriver from Owen Hart compressed Steve Austin's neck and briefly paralyzed him. Austin still finished the match to win the Intercontinental title, but the injury reshaped his career.",
    "ld_desc": "Steve Austin suffers a neck injury from a piledriver at SummerSlam 1997 against Owen Hart.",
    "intro": (
        "At SummerSlam 1997, " + a("stone-cold-steve-austin","Steve Austin") + " faced " + a("owen-hart","Owen Hart") +
        " for the Intercontinental Championship. A mistimed sit-out piledriver landed Austin on the crown of his head, "
        "compressing his neck and leaving him temporarily unable to move. Austin recovered enough to roll Hart up for "
        "the win, but the injury changed the shape of his career."
    ),
    "video": {"mode":"search", "ph":"SS 1997",
              "search": yt_search("WWE Steve Austin Owen Hart SummerSlam 1997 Intercontinental Championship")},
    "body": (
        "<p>The spot was an accident. " + a("owen-hart","Owen Hart") + " was a careful, skilled worker, and the timing "
        "of a single move went wrong in a way that could have ended much worse. Austin lay motionless before managing "
        "a slow rollup to finish the match and claim the title.</p>"
        "<p>The injury left " + a("stone-cold-steve-austin","Austin") + " with lasting neck problems that shortened his "
        "in-ring prime and eventually forced his retirement after WrestleMania X-Seven in 2001. He adapted his style to "
        "protect his neck while becoming the biggest star of the Attitude Era.</p>"
        "<p>Owen Hart died in a separate in-ring accident in 1999. MAT documents his career on his "
        + a("owen-hart","memorial profile") + ".</p>"
    ),
    "related": [("stone-cold-steve-austin","Steve Austin"), ("owen-hart","Owen Hart")],
    "faq": [
        ("How did Steve Austin break his neck?",
         "At SummerSlam 1997, Owen Hart delivered a sit-out piledriver that landed Austin on the top of his head, compressing his neck and briefly paralyzing him. It was an accident, not intentional."),
        ("Did Steve Austin still win the match?",
         "Yes. Despite the injury, Austin recovered enough to roll Owen Hart up for the pin and win the Intercontinental Championship."),
        ("How did the injury affect Austin's career?",
         "The neck injury caused lasting damage that shortened Austin's in-ring prime and contributed to his retirement after WrestleMania X-Seven in 2001. He adjusted his wrestling style to protect his neck while remaining the top star of the era."),
    ],
},

{
    "slug": "kane-debut-badd-blood-1997",
    "name": "Kane's Debut: Tearing Off the Hell in a Cell Door (1997)",
    "kicker": "A debut with zero build needed",
    "date_display": "October 5, 1997",
    "event": "Badd Blood: In Your House",
    "city": "St. Louis, Missouri",
    "desc": "At Badd Blood 1997, during the first-ever Hell in a Cell match, Kane tore the cell door off its hinges, Tombstoned his storyline brother The Undertaker, and cost him the match. It is one of wrestling's greatest debuts.",
    "ld_desc": "Kane makes his debut by tearing the Hell in a Cell door off during Undertaker vs Shawn Michaels at Badd Blood 1997.",
    "intro": (
        "At Badd Blood 1997, during the first-ever Hell in a Cell match between " + a("the-undertaker","The Undertaker") +
        " and " + a("shawn-michaels","Shawn Michaels") + ", the arena went dark. " + a("kane","Kane") + " walked to the "
        "ring, tore the cell door off its hinges, and delivered a Tombstone to his storyline brother, costing the "
        "Undertaker the match. It remains one of the most effective debuts in wrestling history."
    ),
    "video": {"mode":"embed", "id":"4cEgYyvblDc", "ph":"BADD BLOOD 97",
              "search": yt_search("WWE Kane debut Badd Blood 1997 Hell in a Cell")},
    "body": (
        "<p>The debut paid off more than a year of storyline seeds about " + a("the-undertaker","The Undertaker") +
        "'s younger brother, presumed dead in a fire. When " + a("kane","Kane") + " finally appeared, the character was "
        "fully formed: the mask, the red and black, the silence, and the immediate physical dominance.</p>"
        "<p>The moment also protected " + a("shawn-michaels","Shawn Michaels") + ", who advanced from the first Hell in "
        "a Cell to his WrestleMania path, while launching a brother-versus-brother feud that ran for years. It is a "
        "textbook example of a debut that needed no explanation to land.</p>"
    ),
    "related": [("kane","Kane"), ("the-undertaker","The Undertaker"), ("shawn-michaels","Shawn Michaels")],
    "faq": [
        ("When did Kane debut in WWE?",
         "Kane debuted on October 5, 1997 at Badd Blood: In Your House, interrupting the first-ever Hell in a Cell match between The Undertaker and Shawn Michaels."),
        ("What did Kane do in his debut?",
         "Kane tore the Hell in a Cell door off its hinges, entered the ring, and delivered a Tombstone piledriver to The Undertaker, costing him the match against Shawn Michaels."),
        ("Why is Kane's debut considered one of the best?",
         "The character arrived fully formed after more than a year of storyline setup, needed no explanation, and immediately established credibility by dominating The Undertaker. It set up a multi-year feud between the storyline brothers."),
    ],
},

]

# ═══════════════════════════════════════════════════════════════════════════
def build_moment_page(m):
    ld = (
        '<script type="application/ld+json">\n'
        '{\n  "@context":"https://schema.org",\n  "@graph":[\n'
        '    {"@type":"BreadcrumbList","itemListElement":[\n'
        f'      {{"@type":"ListItem","position":1,"name":"Home","item":"{DOMAIN}/"}},\n'
        f'      {{"@type":"ListItem","position":2,"name":"Moments","item":"{DOMAIN}/moments/"}},\n'
        f'      {{"@type":"ListItem","position":3,"name":"{m["name"]}","item":"{DOMAIN}/moments/{m["slug"]}/"}}\n'
        '    ]}'
        + (',\n    {"@type":"FAQPage","mainEntity":[' + faq_ld_items(m["faq"]) + ']}' if m["faq"] else "")
        + video_object_ld(m)
        + '\n  ]\n}\n</script>'
    )

    related_cards = ""
    for slug, name in m["related"]:
        related_cards += f'<a class="related-links__a" href="/wrestlers/{slug}/">{name}</a>'

    title = f'{m["name"]}: What Happened &amp; Video | MAT'
    page = head(title, m["desc"], f'/moments/{m["slug"]}/', ld)
    page += f"""<main id="main">
<section class="ev-hero">
  <div class="wrap ev-hero__inner">
    {crumbs([("Home","/"),("Moments","/moments/"),(m["name"],None)])}
    <span class="ev-hero__brand">{m["kicker"]}</span>
    <h1>{m["name"]}</h1>
    <div class="meta-chips">
      <span class="meta-chip meta-chip--gold"><b>{m["date_display"]}</b></span>
      <span class="meta-chip">{m["event"]}</span>
      <span class="meta-chip">{m["city"]}</span>
    </div>
  </div>
</section>

<div class="wrap">
  <div class="ev-lede" style="margin-top:var(--sp-5)">
    <p>{m["intro"]}</p>
  </div>

  <div class="sec-h"><h2>Watch the moment</h2></div>
{video_html(m)}

  <div class="sec-h"><h2>What happened</h2></div>
  <div class="moment-body">
    {m["body"]}
  </div>

  <div class="sec-h"><h2>Wrestlers in this moment</h2></div>
  <nav class="related-links" aria-label="Wrestlers in this moment">
    {related_cards}
  </nav>

  {faq_block(m["faq"])}
</div>
</main>
"""
    page += footer()
    return page

def build_index():
    cards = ""
    for m in MOMENTS:
        cards += (f'<a class="ev-tile" href="/moments/{m["slug"]}/">'
                  f'<span class="ev-tile__date">{m["date_display"]} &middot; {m["event"]}</span>'
                  f'<h3 class="ev-tile__name">{m["name"]}</h3>'
                  f'<p class="ev-tile__sub">{m["kicker"]}</p></a>\n')
    desc = "Famous in-ring moments and incidents in wrestling history, with the story behind each and the official video. Triple H's quad tear, Mankind's Hell in a Cell fall, and more."
    title = "Famous Wrestling Moments &amp; Incidents: Video &amp; Story | MAT"
    ld = (
        '<script type="application/ld+json">\n'
        '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[\n'
        f'  {{"@type":"ListItem","position":1,"name":"Home","item":"{DOMAIN}/"}},\n'
        f'  {{"@type":"ListItem","position":2,"name":"Moments","item":"{DOMAIN}/moments/"}}\n'
        ']}\n</script>'
    )
    page = head(title, desc, "/moments/", ld)
    page += f"""<main id="main">
<section class="ev-hero">
  <div class="wrap ev-hero__inner">
    {crumbs([("Home","/"),("Moments",None)])}
    <span class="ev-hero__brand">Moments</span>
    <h1>Famous <span class="accent">Moments</span></h1>
    <p class="ev-lede">The in-ring incidents and moments that defined careers, with the story behind each and the official video.</p>
  </div>
</section>

<div class="wrap">
  <div class="sec-h"><h2>Every moment</h2></div>
  <div class="event-grid">
{cards}  </div>
</div>
</main>
"""
    page += footer()
    return page


if __name__ == "__main__":
    for m in MOMENTS:
        dest = os.path.join(OUT, "moments", m["slug"])
        os.makedirs(dest, exist_ok=True)
        with open(os.path.join(dest, "index.html"), "w") as f:
            f.write(build_moment_page(m))
        print(f"✅ moments/{m['slug']}  [{m['video']['mode']}]")
    dest = os.path.join(OUT, "moments")
    os.makedirs(dest, exist_ok=True)
    with open(os.path.join(dest, "index.html"), "w") as f:
        f.write(build_index())
    print("✅ moments/ (index)")
    print(f"\nBatch 12 complete — {len(MOMENTS)} moments + 1 index.")
