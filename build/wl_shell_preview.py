#!/usr/bin/env python3
"""Phase 0 preview: stamp the single-source Wrestle Lore shell (7-tab nav + palette + footer)
onto real pages of each type, rename MAT->Wrestle Lore, unify domain, inline assets -> /tmp.
Does NOT modify the 169 real files. Demonstrates the substrate before the site-wide apply."""
import os, re

ROOT = "/root/wwe"

# tab: (label, href, theme-class, exists?, panel-cols)  panel col = (heading, [(label, href, gap?), ...])
def L(label, href, gap=False):
    return (label, href, gap)

TABS = [
  ("Wrestlers", "/wrestlers/", "", True, [
     ("Status", [L("Current Stars","/current/",True), L("Legends","/legends/",True)]),
     ("Division", [L("Women's","/women/",True), L("Men's","/men/",True), L("All Wrestlers","/wrestlers/")]),
     ("Promotion", [L("WWE","/promotions/wwe/"), L("WCW","/promotions/wcw/"), L("ECW","/promotions/ecw/"),
                    L("TNA","/promotions/tna/"), L("NXT","/promotions/nxt/"), L("NJPW","/promotions/njpw/",True)]),
     ("Featured", [L("AJ Styles","/wrestlers/aj-styles/"), L("The Undertaker","/wrestlers/the-undertaker/"),
                   L("Roman Reigns","/wrestlers/roman-reigns/"), L("Rhea Ripley","/wrestlers/rhea-ripley/")]),
  ]),
  ("Matches", "/matches/", "", True, [
     ("Explore", [L("All Matches","/matches/"), L("Top-Rated (5★)","/rankings/")]),
     ("Editors' Picks", [L("Undertaker vs HBK at WM25","/matches/undertaker-vs-hbk-wm25/"),
                         L("CM Punk vs Cena at MITB '11","/matches/cm-punk-vs-cena-mitb-2011/")]),
  ]),
  ("Events", "/events/", "", True, [
     ("Recent", [L("WrestleMania 42","/events/wrestlemania-42-2026/"),
                 L("Night of Champions 2026","/events/night-of-champions-2026/"),
                 L("Backlash 2026","/events/backlash-2026/")]),
     ("Brands", [L("WrestleMania","/events/wrestlemania/"), L("Royal Rumble","/events/royal-rumble/"),
                 L("Elimination Chamber","/events/elimination-chamber/"), L("All Events","/events/")]),
  ]),
  ("Promotions", "/promotions/", "", True, [
     ("Active", [L("WWE","/promotions/wwe/"), L("AEW","/promotions/aew/",True), L("NJPW","/promotions/njpw/",True), L("TNA","/promotions/tna/")]),
     ("Legacy & NXT", [L("WCW","/promotions/wcw/"), L("ECW","/promotions/ecw/"), L("NXT","/promotions/nxt/"), L("All Promotions","/promotions/")]),
  ]),
  ("Hall of Fame", "/hall-of-fame/", "theme-hof", False, [
     ("Classes", [L("Class of 2026","/hall-of-fame/2026/",True), L("Class of 2025","/hall-of-fame/2025/",True), L("All Classes","/hall-of-fame/",True)]),
     ("Legends", [L("Ric Flair (2×)","/wrestlers/ric-flair/"), L("The Undertaker","/wrestlers/the-undertaker/"), L("AJ Styles (2026)","/wrestlers/aj-styles/")]),
  ]),
  ("Media", "/media/", "theme-media", False, [
     ("Creators", [L("Chris Van Vliet","/media/chris-van-vliet/",True), L("All Media","/media/",True)]),
  ]),
  ("More", "/rankings/", "", True, [
     ("Explore", [L("Rivalries","/rivalries/"), L("Relationships","/relationships/"), L("Rankings","/rankings/"), L("Moments","/moments/")]),
     ("About", [L("Methodology","/methodology/"), L("About","/about/"), L("Insider","/membership/")]),
  ]),
]

def panel(cols, theme):
    wide = " mega--wide" if len(cols) >= 3 else ""
    inner = ""
    for heading, links in cols:
        rows = ""
        for label, href, gap in links:
            tag = ' <small style="color:var(--c-hof-bright)">soon</small>' if gap else ""
            hh = href if not gap else "#"
            rows += f'<a class="mega__link" href="{hh}"><b>{label}{tag}</b></a>'
        inner += f'<div class="mega__col"><h3>{heading}</h3>{rows}</div>'
    return f'<div class="mega{wide} {theme}">{inner}</div>'

def header(active=""):
    lis = ""
    for label, href, theme, exists, cols in TABS:
        soon = "" if exists else ' <span class="tab-soon">soon</span>'
        lis += (f'<li class="nav__item">'
                f'<a class="nav__link" href="{href}" aria-haspopup="true" aria-expanded="false">{label}{soon}</a>'
                f'{panel(cols, theme)}</li>')
    return (
      '<header class="site-header"><div class="wrap"><nav class="nav" aria-label="Primary">'
      '<a class="brand" href="/"><span class="brand__mark"><span>WL</span></span> Wrestle Lore</a>'
      '<button class="nav__toggle" aria-label="Toggle menu" aria-controls="primary-menu" aria-expanded="false">&#9776;</button>'
      f'<ul class="nav__menu" id="primary-menu">{lis}'
      '<li class="nav__spacer" aria-hidden="true"></li>'
      '<li class="nav__item nav__item--search"><button class="nav__search" type="button" data-cmdk-open aria-label="Search (Command-K)">'
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>'
      ' Search <kbd>&#8984;K</kbd></button></li>'
      '</ul></nav></div></header>'
    )

PALETTE = ('<div class="cmdk" id="cmdk" role="dialog" aria-modal="true" aria-label="Search Wrestle Lore" aria-hidden="true">'
  '<div class="cmdk__box"><div class="cmdk__head">'
  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>'
  '<input class="cmdk__input" type="text" placeholder="Search wrestlers, events, moments, matches…" aria-label="Search" autocomplete="off">'
  '<span class="cmdk__hint">Esc</span></div><ul class="cmdk__results" role="listbox"></ul>'
  '<div class="cmdk__foot"><span><kbd>&#8593;&#8595;</kbd> navigate</span><span><kbd>&#8629;</kbd> open</span><span><kbd>esc</kbd> close</span></div></div></div>')

FOOTER = ('<footer class="site-footer"><div class="wrap">'
  '<p>&copy; 2026 Wrestle Lore. All rights reserved.</p>'
  '<nav><a href="/about/">About</a> · <a href="/methodology/">Methodology</a> · <a href="/membership/">Insider</a></nav>'
  '</div></footer>')

EXTRA_CSS = """
.tab-soon,.mega__link small{font-family:var(--font-cond);text-transform:uppercase;letter-spacing:.05em;font-size:.6em;
 color:var(--c-hof-bright);border:1px solid var(--c-hof-deep);border-radius:999px;padding:0 .4em;margin-left:.3em;vertical-align:.15em;}
.mega.theme-hof h3{color:var(--c-hof-bright);}
.mega.theme-hof .mega__link:hover{background:var(--c-hof-tint);}
.mega.theme-media h3{color:var(--c-media-bright);}
.mega.theme-media .mega__link:hover{background:var(--c-media-tint);}
.nav__item:has(.theme-hof) .nav__link:hover{color:var(--c-hof-bright);}
.nav__item:has(.theme-media) .nav__link:hover{color:var(--c-media-bright);}
"""

def strip_and_stamp(html, active=""):
    # remove existing header / old nav / footer / existing palette
    html = re.sub(r'<header class="site-header">.*?</header>', '', html, count=1, flags=re.DOTALL)
    html = re.sub(r'<nav class="site-nav">.*?</nav>', '', html, count=1, flags=re.DOTALL)
    html = re.sub(r'<div class="cmdk"[^>]*id="cmdk".*?</div>\s*</div>\s*</div>', '', html, count=1, flags=re.DOTALL)
    html = re.sub(r'<footer[^>]*>.*?</footer>', '', html, count=1, flags=re.DOTALL)
    html = re.sub(r'<nav class="breadcrumb".*?</nav>', '', html, count=1, flags=re.DOTALL)
    # inject new shell right after <body...>
    html = re.sub(r'(<body[^>]*>)', r'\1\n' + header(active) + '\n' + PALETTE + '\n', html, count=1)
    # footer before </body>
    i = html.rfind('</body>')
    html = html[:i] + FOOTER + '\n' + html[i:]
    # rename brand + unify domain (preview-scope, visible brand spots)
    html = html.replace('https://matdb.io', 'https://wrestlelore.com')
    html = html.replace('| MAT<', '| Wrestle Lore<').replace(' | MAT ', ' | Wrestle Lore ')
    html = re.sub(r'\bMAT\b(?=\s*(—|\||<|&))', 'Wrestle Lore', html)
    html = html.replace('MAT Wrestling Database', 'Wrestle Lore')
    return html

def inline(html):
    css = open(f"{ROOT}/css/site.css").read() + EXTRA_CSS
    js = [open(f"{ROOT}/js/{f}").read() for f in ["main.js","enhance.js","search-index.js","nav.js"]]
    html = re.sub(r'<link rel="stylesheet" href="/css/site.css">', '<style>\n'+css+'\n</style>', html, count=1)
    for f in ["main.js","enhance.js","search-index.js","nav.js"]:
        html = html.replace(f'<script src="/js/{f}" defer></script>','').replace(f'<script src="/js/{f}"></script>','')
    inject = '<script>\n'+"\n;\n".join(js)+'\n</script>\n'
    i = html.rfind('</body>')
    return html[:i] + inject + html[i:]

PAGES = [
  ("index.html", "/tmp/WL-home.html", "Wrestlers"),
  ("wrestlers/the-undertaker/index.html", "/tmp/WL-wrestler.html", "Wrestlers"),
  ("events/wrestlemania-42-2026/index.html", "/tmp/WL-event.html", "Events"),
  ("moments/mankind-hell-in-a-cell-fall-1998/index.html", "/tmp/WL-moment.html", "More"),
]
if __name__ == "__main__":
    for src, out, active in PAGES:
        p = os.path.join(ROOT, src)
        if not os.path.isfile(p):
            print("skip (missing)", src); continue
        html = inline(strip_and_stamp(open(p).read(), active))
        open(out, "w").write(html)
        print("wrote", out, round(len(html)/1024,1), "KB")
