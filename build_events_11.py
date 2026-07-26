#!/usr/bin/env python3
"""Batch 11 — Events/PPV content type launch.
5 edition pages (2026 events, real sourced results) + 5 brand hub pages + /events/ index.
Domain: wrestlelore.com (README-canonical; matches homepage/promotions/matches templates).
Watch links: ESPN (US live PLE home from 2026) + Netflix (international live / US archive).
"""
import os, re

DOMAIN = "https://wrestlelore.com"
OUT = "/root/wwe"
ESPN_URL = "https://www.espn.com/wwe/"
NETFLIX_URL = "https://www.netflix.com/browse/genre/81921064"

def a(slug, name):
    return f'<a href="/wrestlers/{slug}/">{name}</a>'

def ev(slug, name):
    return f'<a href="/events/{slug}/">{name}</a>'

def hub(slug, name):
    return f'<a href="/events/{slug}/">{name}</a>'

# ── shared chrome ──────────────────────────────────────────────────────────
def head(title, desc, canonical_path, faq_ld_block=""):
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
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Oswald:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/site.css">
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@graph":[
    {{"@type":"BreadcrumbList","itemListElement":[
      {{"@type":"ListItem","position":1,"name":"Home","item":"{DOMAIN}/"}},
      {{"@type":"ListItem","position":2,"name":"Events","item":"{DOMAIN}/events/"}}
    ]}}{faq_ld_block}
  ]
}}
</script>
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
    """items: list of (label, href_or_None). Last item is current page."""
    lis = ""
    for label, href in items:
        if href:
            lis += f'<li><a href="{href}">{label}</a></li>'
        else:
            lis += f'<li aria-current="page">{label}</li>'
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{lis}</ol></nav>\n'

def hero_title(name):
    """Accent the trailing number/year in gold (WrestleMania <42>, Backlash <2026>)."""
    parts = name.rsplit(" ", 1)
    if len(parts) == 2 and any(ch.isdigit() for ch in parts[1]):
        return f'{parts[0]} <span class="accent">{parts[1]}</span>'
    return name

def watch_panel():
    return f"""<section class="watch2" aria-label="Where to watch">
  <div class="watch2__card watch2__card--espn">
    <p class="watch2__region">Watch in the US</p>
    <p class="watch2__plat">ESPN</p>
    <p>Every WWE Premium Live Event streams live on ESPN, and only on ESPN, starting with the 2026 calendar.</p>
    <a class="watch2__btn" href="{ESPN_URL}" target="_blank" rel="noopener">Watch on ESPN</a>
  </div>
  <div class="watch2__card watch2__card--nflx">
    <p class="watch2__region">Watch internationally</p>
    <p class="watch2__plat">Netflix</p>
    <p>Outside the US, Premium Live Events stream live on Netflix, alongside Raw, SmackDown, NXT and the event archive.</p>
    <a class="watch2__btn watch2__btn--ghost" href="{NETFLIX_URL}" target="_blank" rel="noopener">Watch on Netflix</a>
  </div>
</section>
"""

def faq_ld(faq):
    if not faq:
        return ""
    items = ""
    for q, ans in faq:
        safe_q = q.replace('"', '&quot;')
        safe_a = re.sub(r'<[^>]+>', '', ans).replace('"', '&quot;')
        items += f'{{"@type":"Question","name":"{safe_q}","acceptedAnswer":{{"@type":"Answer","text":"{safe_a}"}}}},'
    items = items.rstrip(",")
    return ',\n    {"@type":"FAQPage","mainEntity":[' + items + ']}'

def faq_html_block(faq):
    if not faq:
        return ""
    html = "".join(
        f'<details><summary>{q}</summary><div class="faq__body">{ans}</div></details>\n'
        for q, ans in faq)
    return ('<div class="sec-h"><h2>FAQ</h2></div>\n'
            '<div class="faq faq-block">\n' + html + '</div>\n')

def me_matchup(html):
    """Winner in gold, 'def.' as a small dim connector."""
    if " def. " in html:
        w, l = html.split(" def. ", 1)
        return f'<span class="win">{w}</span><span class="def">def.</span>{l}'
    return f'<span class="win">{html}</span>'

def me_card(m):
    stip = f'<p class="me-card__stip">{m["stip"]}</p>' if m["stip"] else ""
    note = f'<p class="me-card__note">{m["note"]}</p>' if m.get("note") else ""
    return (f'<article class="me-card"><span class="me-card__tag">Main Event</span>'
            f'{stip}<p class="me-card__match">{me_matchup(m["html"])}</p>{note}</article>\n')

def res_list(rows):
    lis = ""
    for m in rows:
        stip = f'<span class="res-stip">{m["stip"]}</span>' if m["stip"] else ""
        note = f'<p class="res-note">{m["note"]}</p>' if m.get("note") else ""
        match = m["html"].replace(" def. ", ' <span class="def">def.</span> ')
        lis += (f'<li><span class="res-w" aria-hidden="true">W</span>'
                f'<div class="res-body">{stip}<div class="res-match">{match}</div>{note}</div></li>\n')
    return f'<ul class="res-list">\n{lis}</ul>\n'

def results_html(e):
    """Group by night when matches carry a 'night' key; main events lead each group."""
    mains, card = e["main_events"], e["card"]
    nights = []
    for m in mains + card:
        n = m.get("night")
        if n and n not in nights:
            nights.append(n)
    if not nights:
        html = "".join(me_card(m) for m in mains)
        if card:
            html += res_list(card)
        return html
    html = ""
    for n in nights:
        html += f'<h3 class="night-h">{n}</h3>\n'
        for m in mains:
            if m.get("night") == n:
                html += me_card(m)
        rows = [m for m in card if m.get("night") == n]
        if rows:
            html += res_list(rows)
    return html

# ═══════════════════════════════════════════════════════════════════════════
# EDITION PAGES — real, sourced 2026 results
# ═══════════════════════════════════════════════════════════════════════════

EDITIONS = [

{
    "slug": "royal-rumble-2026",
    "brand_slug": "royal-rumble",
    "brand_name": "Royal Rumble",
    "name": "Royal Rumble 2026",
    "date_display": "January 31, 2026",
    "venue": "Riyadh Season Stadium",
    "city": "Riyadh, Saudi Arabia",
    "desc": "Royal Rumble 2026 results: Roman Reigns and Liv Morgan win the men's and women's Royal Rumble matches, punching their tickets to WrestleMania 42.",
    "intro": (
        '<p>' + ev("royal-rumble-2026", "Royal Rumble 2026") + ' kicked off WWE\'s Road to WrestleMania 42 from Riyadh Season Stadium in Saudi Arabia. '
        'The two signature 30-entrant Rumble matches determined the men\'s and women\'s WrestleMania main-event challengers, '
        'with ' + a("roman-reigns","Roman Reigns") + ' and Liv Morgan both punching their tickets.</p>'
    ),
    "main_events": [
        {"stip":"Men's Royal Rumble Match", "html": a("roman-reigns","Roman Reigns") + " wins", "note":"Reigns outlasts 29 other entrants to earn a WrestleMania 42 world title opportunity.", "main": True},
        {"stip":"Women's Royal Rumble Match", "html": "Liv Morgan wins", "note":"Morgan earns her WrestleMania 42 title opportunity.", "main": True},
    ],
    "card": [
        {"stip":"Undisputed WWE Championship", "html": "Title match on the card", "note":"AJ Styles' in-ring career storyline reaches its conclusion on the undercard."},
    ],
    "faq": [
        ("Who won the 2026 Men's Royal Rumble?",
         f"{a('roman-reigns','Roman Reigns')} won the 2026 Men's Royal Rumble match, earning a world championship match at WrestleMania 42."),
        ("Who won the 2026 Women's Royal Rumble?",
         "Liv Morgan won the 2026 Women's Royal Rumble match, earning a women's championship match at WrestleMania 42."),
        ("Where was Royal Rumble 2026 held?",
         "Royal Rumble 2026 took place on January 31, 2026 at Riyadh Season Stadium in Riyadh, Saudi Arabia, part of WWE's continued partnership bringing marquee events to the Kingdom."),
        ("Where can I watch Royal Rumble 2026?",
         "In the US, WWE Premium Live Events including Royal Rumble stream on ESPN. Internationally, they stream live on Netflix."),
    ],
},

{
    "slug": "elimination-chamber-2026",
    "brand_slug": "elimination-chamber",
    "brand_name": "Elimination Chamber",
    "name": "Elimination Chamber 2026",
    "date_display": "February 28, 2026",
    "venue": "United Center",
    "city": "Chicago, Illinois",
    "desc": "Elimination Chamber 2026 results: Randy Orton and Rhea Ripley win the men's and women's Chamber matches; AJ Lee captures the Women's Intercontinental Championship.",
    "intro": (
        '<p>' + ev("elimination-chamber-2026", "Elimination Chamber 2026") + ' brought WWE\'s signature steel-structure match to the United Center in Chicago, '
        'setting the final WrestleMania 42 championship matches. Randy Orton and Rhea Ripley both survived their respective '
        'six-person Chambers to earn title opportunities.</p>'
    ),
    "main_events": [
        {"stip":"Men's Elimination Chamber", "html": a("randy-orton","Randy Orton") + " def. LA Knight, Cody Rhodes, Je'Von Evans, Trick Williams, Logan Paul", "note":"Orton earns a WrestleMania 42 championship match against Drew McIntyre. Seth Rollins returned to attack Logan Paul mid-match, costing Paul the win.", "main": True},
        {"stip":"Women's Elimination Chamber", "html": "Rhea Ripley def. Tiffany Stratton, Alexa Bliss, Asuka, Kiana James, Raquel Rodriguez", "note":"Ripley earns a WrestleMania 42 championship match against Jade Cargill.", "main": True},
    ],
    "card": [
        {"stip":"Women's Intercontinental Championship", "html": "AJ Lee def. " + a("becky-lynch","Becky Lynch"), "note":"Lee captures the title."},
        {"stip":"WWE World Heavyweight Championship", "html": "CM Punk def. Finn B&aacute;lor", "note":"Punk retains heading into his WrestleMania 42 program with Roman Reigns."},
    ],
    "faq": [
        ("Who won the Men's Elimination Chamber in 2026?",
         f"{a('randy-orton','Randy Orton')} won the 2026 Men's Elimination Chamber, defeating LA Knight, Cody Rhodes, Je'Von Evans, Trick Williams, and Logan Paul to earn a WrestleMania 42 title shot."),
        ("Who won the Women's Elimination Chamber in 2026?",
         "Rhea Ripley won the 2026 Women's Elimination Chamber, defeating Tiffany Stratton, Alexa Bliss, Asuka, Kiana James, and Raquel Rodriguez to earn a WrestleMania 42 title opportunity."),
        ("What happened with Seth Rollins at Elimination Chamber 2026?",
         "Seth Rollins made a surprise return during the Men's Elimination Chamber match, attacking Logan Paul and costing him elimination. It set up a program that continued through the following months."),
        ("Where can I watch Elimination Chamber 2026?",
         "In the US, WWE Premium Live Events stream on ESPN. Internationally, they stream live on Netflix."),
    ],
},

{
    "slug": "wrestlemania-42-2026",
    "brand_slug": "wrestlemania",
    "brand_name": "WrestleMania",
    "name": "WrestleMania 42",
    "date_display": "April 18–19, 2026",
    "venue": "Allegiant Stadium",
    "city": "Las Vegas, Nevada",
    "desc": "WrestleMania 42 results: Cody Rhodes defeats Randy Orton for the Undisputed WWE Championship on Night 1; Roman Reigns defeats CM Punk for the World Heavyweight Championship on Night 2.",
    "intro": (
        '<p>' + ev("wrestlemania-42-2026", "WrestleMania 42") + ', WWE\'s two-night "Showcase of the Immortals," was held at Allegiant Stadium in Las Vegas '
        'on April 18–19, 2026. Each night closed with a world championship main event: '
        + a("cody-rhodes","Cody Rhodes") + ' dethroning ' + a("randy-orton","Randy Orton") + ' for the Undisputed WWE Championship on Night 1, '
        'and ' + a("roman-reigns","Roman Reigns") + ' defeating CM Punk for the World Heavyweight Championship on Night 2.</p>'
    ),
    "main_events": [
        {"stip":"Undisputed WWE Championship", "night":"Night 1", "html": a("cody-rhodes","Cody Rhodes") + " def. " + a("randy-orton","Randy Orton"), "note":"Rhodes captures the Undisputed WWE Championship.", "main": True},
        {"stip":"World Heavyweight Championship", "night":"Night 2", "html": a("roman-reigns","Roman Reigns") + " def. CM Punk", "note":"Reigns wins the World Heavyweight Championship.", "main": True},
    ],
    "card": [
        {"stip":"Six-Man Tag", "night":"Night 1", "html": "LA Knight, Jey Uso &amp; Jimmy Uso def. Logan Paul, Austin Theory &amp; IShowSpeed", "note":""},
        {"stip":"", "night":"Night 1", "html": "Jacob Fatu def. Drew McIntyre", "note":""},
        {"stip":"Women's Tag Team Championship &middot; Fatal 4-Way", "night":"Night 1", "html": "Brie Bella &amp; Paige def. Alexa Bliss/Charlotte Flair, Bayley/Lyra Valkyria, Nia Jax/Lash Legend", "note":""},
        {"stip":"Women's Intercontinental Championship", "night":"Night 1", "html": a("becky-lynch","Becky Lynch") + " def. AJ Lee", "note":""},
        {"stip":"", "night":"Night 1", "html": "Gunther def. Seth Rollins", "note":""},
        {"stip":"Women's World Championship", "night":"Night 1", "html": "Liv Morgan def. Stephanie Vaquer", "note":""},
        {"stip":"", "night":"Night 2", "html": "Oba Femi def. Brock Lesnar", "note":""},
        {"stip":"Intercontinental Championship &middot; Ladder Match", "night":"Night 2", "html": "Penta def. Je'Von Evans, Dragon Lee, Rusev, JD McDonagh, " + a("rey-mysterio","Rey Mysterio"), "note":""},
        {"stip":"United States Championship", "night":"Night 2", "html": "Trick Williams def. Sami Zayn", "note":""},
        {"stip":"", "night":"Night 2", "html": "Finn B&aacute;lor def. Dominik Mysterio", "note":""},
        {"stip":"Women's Championship", "night":"Night 2", "html": "Rhea Ripley def. Jade Cargill", "note":""},
    ],
    "faq": [
        ("Who won at WrestleMania 42?",
         f"On Night 1, {a('cody-rhodes','Cody Rhodes')} defeated {a('randy-orton','Randy Orton')} for the Undisputed WWE Championship. On Night 2, {a('roman-reigns','Roman Reigns')} defeated CM Punk for the World Heavyweight Championship."),
        ("Where was WrestleMania 42 held?",
         "WrestleMania 42 was held April 18–19, 2026 at Allegiant Stadium in Las Vegas, Nevada, continuing WWE's stadium-era two-night WrestleMania format."),
        ("How many nights is WrestleMania 42?",
         "WrestleMania 42 was a two-night event, following the format WWE established for WrestleMania 35 onward. The card splits across Saturday and Sunday."),
        ("Where can I watch WrestleMania 42?",
         "In the US, WrestleMania 42 streamed live on ESPN as part of WWE's new Premium Live Event deal. Internationally, it streamed live on Netflix."),
    ],
},

{
    "slug": "backlash-2026",
    "brand_slug": "backlash",
    "brand_name": "Backlash",
    "name": "Backlash 2026",
    "date_display": "May 9, 2026",
    "venue": "Benchmark International Arena",
    "city": "Tampa, Florida",
    "desc": "Backlash 2026 results: Roman Reigns retains the World Heavyweight Championship over Jacob Fatu; Bron Breakker defeats Seth Rollins; John Cena announces the John Cena Classic.",
    "intro": (
        '<p>' + ev("backlash-2026", "Backlash 2026") + ' was WWE\'s first post-WrestleMania blow-off show of the year, held at Benchmark International Arena in Tampa. '
        + a("roman-reigns","Roman Reigns") + ' made his first World Heavyweight Championship defense since winning it at WrestleMania 42, '
        'and John Cena used the show to announce a new cross-brand tournament, the John Cena Classic.</p>'
    ),
    "main_events": [
        {"stip":"World Heavyweight Championship", "html": a("roman-reigns","Roman Reigns") + " def. Jacob Fatu", "note":"Reigns makes his first successful defense since WrestleMania 42.", "main": True},
    ],
    "card": [
        {"stip":"", "html": "Bron Breakker def. Seth Rollins", "note":"Breakker continues his momentum following his WrestleMania return."},
        {"stip":"United States Championship", "html": "Trick Williams def. Sami Zayn", "note":"Williams retains."},
        {"stip":"", "html": "Danhausen &amp; The Minihausens def. The Miz &amp; Kit Wilson", "note":""},
        {"stip":"", "html": "Iyo Sky def. Asuka", "note":""},
    ],
    "faq": [
        ("Who won the main event of Backlash 2026?",
         f"{a('roman-reigns','Roman Reigns')} defeated Jacob Fatu to retain the World Heavyweight Championship. It was his first defense since winning the title at WrestleMania 42."),
        ("What is the John Cena Classic?",
         "The John Cena Classic is a tournament announced by John Cena at Backlash 2026, featuring stars from both the main roster and NXT competing for a new championship voted on by fans."),
        ("Where was Backlash 2026 held?",
         "Backlash 2026 was held May 9, 2026 at Benchmark International Arena in Tampa, Florida."),
        ("Where can I watch Backlash 2026?",
         "In the US, Backlash 2026 streamed live on ESPN. Internationally, it streamed live on Netflix."),
    ],
},

{
    "slug": "night-of-champions-2026",
    "brand_slug": "night-of-champions",
    "brand_name": "Night of Champions",
    "name": "Night of Champions 2026",
    "date_display": "June 27, 2026",
    "venue": "Kingdom Arena",
    "city": "Riyadh, Saudi Arabia",
    "desc": "Night of Champions 2026 results: Sami Zayn wins the Undisputed WWE Championship in a triple threat over Cody Rhodes and Gunther; Oba Femi and Iyo Sky win King and Queen of the Ring.",
    "intro": (
        '<p>' + ev("night-of-champions-2026", "Night of Champions 2026") + ' returned to Kingdom Arena in Riyadh, Saudi Arabia, headlined by a triple-threat '
        'Undisputed WWE Championship match and the finals of the 2026 King and Queen of the Ring tournaments. Sami Zayn '
        'stunned the field to capture the top title, while Oba Femi and Iyo Sky were crowned King and Queen of the Ring.</p>'
    ),
    "main_events": [
        {"stip":"Undisputed WWE Championship &middot; Triple Threat", "html": "Sami Zayn def. " + a("cody-rhodes","Cody Rhodes") + " &amp; Gunther", "note":"Zayn captures the Undisputed WWE Championship.", "main": True},
    ],
    "card": [
        {"stip":"King of the Ring Final", "html": "Oba Femi def. Jey Uso", "note":"Femi is crowned 2026 King of the Ring."},
        {"stip":"Queen of the Ring Final", "html": "Iyo Sky def. Liv Morgan", "note":"Sky is crowned 2026 Queen of the Ring and announces a SummerSlam title challenge."},
        {"stip":"United States Championship", "html": "Trick Williams def. Ricky Saints", "note":"Williams retains."},
        {"stip":"Women's United States Championship", "html": "Tiffany Stratton def. Jade Cargill", "note":"Stratton retains."},
        {"stip":"Steel Cage Match", "html": "Seth Rollins def. Bron Breakker", "note":""},
    ],
    "faq": [
        ("Who won the WWE Championship at Night of Champions 2026?",
         f"Sami Zayn won the Undisputed WWE Championship at Night of Champions 2026, defeating champion {a('cody-rhodes','Cody Rhodes')} and Gunther in a triple-threat main event."),
        ("Who won King and Queen of the Ring in 2026?",
         "Oba Femi won the 2026 King of the Ring tournament, defeating Jey Uso in the final. Iyo Sky won the 2026 Queen of the Ring tournament, defeating Liv Morgan in the final."),
        ("Where was Night of Champions 2026 held?",
         "Night of Champions 2026 was held June 27, 2026 at Kingdom Arena in Riyadh, Saudi Arabia."),
        ("Where can I watch Night of Champions 2026?",
         "Night of Champions 2026 aired on ESPN Unlimited in the US and streamed live on Netflix internationally."),
    ],
},

]

# ═══════════════════════════════════════════════════════════════════════════
# BRAND HUB PAGES
# ═══════════════════════════════════════════════════════════════════════════

HUBS = [
{
    "slug": "wrestlemania",
    "name": "WrestleMania",
    "tagline": "The Showcase of the Immortals",
    "desc": "WrestleMania is WWE's flagship annual event, running since 1985. Explore its history, legendary moments, and the latest edition, WrestleMania 42.",
    "body": (
        '<p>WrestleMania is WWE\'s flagship event, "The Showcase of the Immortals," held every spring since March 31, 1985 '
        'at Madison Square Garden. It has grown from a single-arena gamble into a two-night stadium spectacle drawing over '
        '70,000 fans, and it remains the event around which the entire wrestling calendar is built.</p>'
        '<p>Landmark editions include WrestleMania III (1987, Pontiac Silverdome, the Hogan/Andre bodyslam), WrestleMania X-Seven '
        '(2001, widely called the best-ever card), and the modern two-night stadium era running from WrestleMania 35 onward.</p>'
        '<p>Careers are defined by WrestleMania moments. ' + a("the-undertaker","The Undertaker") + '\'s undefeated Streak ran 21–0 '
        'before ending at WrestleMania 30, and dozens of championship reigns have been made or broken on this stage.</p>'
    ),
    "editions": [
        {"slug":"wrestlemania-42-2026", "name":"WrestleMania 42", "date":"April 18–19, 2026", "note":"Cody Rhodes over Randy Orton (N1); Roman Reigns over CM Punk (N2)"},
    ],
    "faq": [
        ("When did WrestleMania start?",
         "WrestleMania began on March 31, 1985 at Madison Square Garden in New York City, headlined by Hulk Hogan and Mr. T against Roddy Piper and Paul Orndorff."),
        ("Why is WrestleMania two nights now?",
         "WWE expanded WrestleMania to a two-night format starting with WrestleMania 35 (2019) to accommodate a growing roster and card length, splitting championship matches and marquee bouts across Saturday and Sunday."),
        ("What is the most famous WrestleMania moment?",
         "Hulk Hogan bodyslamming Andre the Giant at WrestleMania III (1987) before 93,000+ fans in the Pontiac Silverdome is widely considered wrestling's most iconic single image."),
    ],
},
{
    "slug": "royal-rumble",
    "name": "Royal Rumble",
    "tagline": "30 Superstars. One Winner. A Ticket to WrestleMania.",
    "desc": "The Royal Rumble kicks off WWE's Road to WrestleMania every January with its signature 30-entrant elimination match.",
    "body": (
        '<p>The Royal Rumble match debuted on a 1988 USA Network special before becoming its own PPV in 1989. '
        'The format has become the most imitated match concept in wrestling: 30 entrants, staggered timed entries, and '
        'eliminations by going over the top rope with both feet touching the floor.</p>'
        '<p>Since 1993, winning the Royal Rumble has guaranteed a world championship match at WrestleMania, making every January '
        'edition the true starting gun for WWE\'s biggest storytelling season. Historic winners include Ric Flair (1992, entering at #3 '
        'and winning the vacant WWF Title) and Chris Benoit\'s iron-man run from the #1 spot in 2004.</p>'
        '<p>The women\'s Royal Rumble launched in 2018, instantly becoming an equally prestigious showcase.</p>'
    ),
    "editions": [
        {"slug":"royal-rumble-2026", "name":"Royal Rumble 2026", "date":"January 31, 2026", "note":"Roman Reigns and Liv Morgan win"},
    ],
    "faq": [
        ("What do you win at the Royal Rumble?",
         "Since 1993, winning the men's or women's Royal Rumble match earns a world championship match of the winner's choosing at that year's WrestleMania."),
        ("How many wrestlers are in a Royal Rumble match?",
         "A standard Royal Rumble match features 30 entrants, who enter one at a time at staggered intervals (traditionally every 90 seconds), with eliminations occurring when a wrestler is thrown over the top rope with both feet touching the floor."),
        ("When did the women's Royal Rumble start?",
         "The first women's Royal Rumble match was held in 2018, won by Asuka."),
    ],
},
{
    "slug": "elimination-chamber",
    "name": "Elimination Chamber",
    "tagline": "Six Enter. One Survives.",
    "desc": "Elimination Chamber is WWE's steel-structure gauntlet match, held annually since 2010, deciding major championship contenders.",
    "body": (
        '<p>The Elimination Chamber match debuted at Survivor Series 2002 and became its own annual February PPV in 2010, '
        'rebranding the slot previously held by No Way Out. Six competitors start two at a time inside a domed steel structure '
        'with four enclosed pods, with the remaining four entering at timed intervals.</p>'
        '<p>The match has become a reliable Road-to-WrestleMania fixture, frequently used to set the spring\'s championship matches. '
        'Shawn Michaels won the inaugural Chamber to capture the World Heavyweight Championship in 2002.</p>'
    ),
    "editions": [
        {"slug":"elimination-chamber-2026", "name":"Elimination Chamber 2026", "date":"February 28, 2026", "note":"Randy Orton and Rhea Ripley win"},
    ],
    "faq": [
        ("How many wrestlers compete in an Elimination Chamber match?",
         "Six wrestlers compete. Two begin the match in the ring, while the other four wait inside enclosed pods and enter at timed intervals, similar to a Royal Rumble but inside a fully enclosed steel structure."),
        ("When did Elimination Chamber become its own PPV?",
         "The Elimination Chamber match debuted at Survivor Series 2002, but the event became its own standalone annual PPV starting in February 2010."),
    ],
},
{
    "slug": "backlash",
    "name": "Backlash",
    "tagline": "The Post-Mania Blow-Off",
    "desc": "Backlash is WWE's spring PPV, historically positioned as the show that pays off, or restarts, feuds coming out of WrestleMania.",
    "body": (
        '<p>Backlash was first held April 25, 1999, and has long served as WWE\'s "day after" show, resolving storylines that '
        'didn\'t get a full close at WrestleMania. In recent years it has also become a flagship for WWE\'s international expansion, '
        'with editions held in Puerto Rico (2023), Lyon, France (2024), and Tampa, Florida (2026).</p>'
    ),
    "editions": [
        {"slug":"backlash-2026", "name":"Backlash 2026", "date":"May 9, 2026", "note":"Roman Reigns retains over Jacob Fatu; John Cena Classic announced"},
    ],
    "faq": [
        ("When was the first Backlash?",
         "The first Backlash was held April 25, 1999, establishing the tradition of a post-WrestleMania blow-off show."),
        ("Is Backlash always held in the US?",
         "No. Backlash has increasingly been used as an international showcase, with recent editions in Puerto Rico, France, and other markets outside the traditional US arena circuit."),
    ],
},
{
    "slug": "night-of-champions",
    "name": "Night of Champions",
    "tagline": "Every Title Match on One Card",
    "desc": "Night of Champions is WWE's Saudi Arabia-based event historically built around championship matches across the roster.",
    "body": (
        '<p>Night of Champions revived a concept WWE has used intermittently since 2004, a card built primarily around '
        'championship matches, and re-anchored it as a marquee stop on WWE\'s Saudi Arabia partnership calendar. '
        'The 2026 edition doubled as the finals stage for the King and Queen of the Ring tournaments, crowning Oba Femi '
        'and Iyo Sky before a triple-threat Undisputed WWE Championship main event.</p>'
    ),
    "editions": [
        {"slug":"night-of-champions-2026", "name":"Night of Champions 2026", "date":"June 27, 2026", "note":"Sami Zayn wins Undisputed WWE Championship; Oba Femi and Iyo Sky crowned King/Queen of the Ring"},
    ],
    "faq": [
        ("What is unique about Night of Champions?",
         "Night of Champions is traditionally built with multiple championship matches on a single card, rather than being centered on one storyline blow-off. The name reflects the format."),
        ("Where is Night of Champions usually held?",
         "In its modern revival, Night of Champions has been held in Saudi Arabia as part of WWE's ongoing partnership bringing premium live events to the Kingdom."),
    ],
},
]

# ═══════════════════════════════════════════════════════════════════════════
# BUILDERS
# ═══════════════════════════════════════════════════════════════════════════

def build_edition_page(e):
    faq_ld_block = faq_ld(e["faq"])
    faq_block = faq_html_block(e["faq"])
    n_matches = len(e["main_events"]) + len(e["card"])

    title = f'{e["name"]}: Results, Card &amp; Main Event | MAT'
    page = head(title, e["desc"], f'/events/{e["slug"]}/', faq_ld_block)
    page += f"""<main id="main">
<section class="ev-hero">
  <div class="wrap ev-hero__inner">
    {crumbs([("Home","/"),("Events","/events/"),(e['brand_name'],f"/events/{e['brand_slug']}/"),(e['name'],None)])}
    <a class="ev-hero__brand" href="/events/{e['brand_slug']}/">{e['brand_name']}</a>
    <h1>{hero_title(e['name'])}</h1>
    <div class="meta-chips">
      <span class="meta-chip meta-chip--gold"><b>{e['date_display']}</b></span>
      <span class="meta-chip">{e['venue']}</span>
      <span class="meta-chip">{e['city']}</span>
    </div>
  </div>
</section>

<div class="wrap">
  <div class="ev-lede" style="margin-top:var(--sp-5)">
    {e['intro']}
  </div>

  {watch_panel()}

  <div class="sec-h"><h2>Full Results</h2><span class="count">{n_matches} matches</span></div>
{results_html(e)}
  {faq_block}
</div>
</main>
"""
    page += footer()
    return page

def build_hub_page(h):
    faq_ld_block = faq_ld(h["faq"])
    faq_block = faq_html_block(h["faq"])
    ed_cards = ""
    for e in h["editions"]:
        ed_cards += (f'<a class="ev-tile" href="/events/{e["slug"]}/">'
                     f'<span class="ev-tile__date">{e["date"]}</span>'
                     f'<h3 class="ev-tile__name">{e["name"]}</h3>'
                     f'<p class="ev-tile__sub">{e["note"]}</p></a>\n')

    title = f'{h["name"]}: History &amp; Every Edition | MAT'
    page = head(title, h["desc"], f'/events/{h["slug"]}/', faq_ld_block)
    page += f"""<main id="main">
<section class="ev-hero">
  <div class="wrap ev-hero__inner">
    {crumbs([("Home","/"),("Events","/events/"),(h['name'],None)])}
    <span class="ev-hero__brand">{h['tagline']}</span>
    <h1>{h['name']}</h1>
  </div>
</section>

<div class="wrap">
  <div class="ev-lede" style="margin-top:var(--sp-5)">
    {h['body']}
  </div>

  <div class="sec-h"><h2>Editions on MAT</h2></div>
  <div class="event-grid">
{ed_cards}  </div>

  {faq_block}
</div>
</main>
"""
    page += footer()
    return page

def build_index_page(editions, hubs):
    recent_cards = ""
    for e in editions[::-1]:  # most recent first (list is chronological, so reverse)
        main_note = e["main_events"][0]["html"] if e["main_events"] else ""
        main_note = re.sub(r'<[^>]+>', '', main_note)
        recent_cards += (f'<a class="ev-tile" href="/events/{e["slug"]}/">'
                          f'<span class="ev-tile__date">{e["date_display"]} &middot; {e["city"]}</span>'
                          f'<h3 class="ev-tile__name">{e["name"]}</h3>'
                          f'<p class="ev-tile__sub">{main_note}</p></a>\n')
    hub_cards = ""
    for h in hubs:
        hub_cards += (f'<a class="ev-tile ev-tile--red" href="/events/{h["slug"]}/">'
                       f'<h3 class="ev-tile__name">{h["name"]}</h3>'
                       f'<p class="ev-tile__sub">{h["tagline"]}</p></a>\n')

    desc = "WWE Premium Live Events on MAT. Full results, main events, and where to watch every recent pay-per-view, from Royal Rumble to WrestleMania to Night of Champions."
    title = "WWE Premium Live Events: Results &amp; Where to Watch | MAT"
    page = head(title, desc, "/events/")
    page += f"""<main id="main">
<section class="ev-hero">
  <div class="wrap ev-hero__inner">
    {crumbs([("Home","/"),("Events",None)])}
    <span class="ev-hero__brand">Premium Live Events</span>
    <h1>WWE <span class="accent">Events</span></h1>
    <p class="ev-lede">Full results, main events, and where to watch, starting with the most recent shows.</p>
  </div>
</section>

<div class="wrap">
  {watch_panel()}

  <div class="sec-h"><h2>Most Recent Events</h2></div>
  <div class="event-grid">
{recent_cards}  </div>

  <div class="sec-h"><h2>Event Brands</h2></div>
  <div class="event-grid">
{hub_cards}  </div>
</div>
</main>
"""
    page += footer()
    return page


if __name__ == "__main__":
    for e in EDITIONS:
        dest = os.path.join(OUT, "events", e["slug"])
        os.makedirs(dest, exist_ok=True)
        with open(os.path.join(dest, "index.html"), "w") as f:
            f.write(build_edition_page(e))
        print(f"✅ events/{e['slug']}")

    for h in HUBS:
        dest = os.path.join(OUT, "events", h["slug"])
        os.makedirs(dest, exist_ok=True)
        with open(os.path.join(dest, "index.html"), "w") as f:
            f.write(build_hub_page(h))
        print(f"✅ events/{h['slug']} (hub)")

    dest = os.path.join(OUT, "events")
    os.makedirs(dest, exist_ok=True)
    with open(os.path.join(dest, "index.html"), "w") as f:
        f.write(build_index_page(EDITIONS, HUBS))
    print("✅ events/ (index)")

    print("\nBatch 11 complete — 5 editions + 5 hubs + 1 index = 11 pages.")
