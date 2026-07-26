#!/usr/bin/env python3
"""Phase 0 site-wide apply: swap every page's header+footer for the single-source Wrestle Lore
shell (existing-pages-only nav, 404-safe), ensure the cmdk palette + scripts, rename MAT->Wrestle
Lore in visible brand spots, unify canonical domain to matwrestling.com. Preserves <main>.
Excludes /zh/ and /china/ (localized). Reports per-file what matched. Idempotent-ish (safe to re-run)."""
import os, re, glob

ROOT = "/root/wwe"
EXCLUDE = ("/zh/", "/china/", "/content/", "/docs/", "/assets/")

NAV = """<header class="site-header" data-wl-shell><div class="wrap"><nav class="nav" aria-label="Primary">
  <a class="brand" href="/"><span class="brand__mark"><span>WL</span></span> Wrestle Lore</a>
  <button class="nav__toggle" aria-label="Toggle menu" aria-controls="primary-menu" aria-expanded="false">&#9776;</button>
  <ul class="nav__menu" id="primary-menu">
    <li class="nav__item"><a class="nav__link" href="/wrestlers/" aria-haspopup="true" aria-expanded="false">Wrestlers</a>
      <div class="mega mega--wide">
        <div class="mega__col"><h3>By Status</h3>
          <a class="mega__link" href="/current/"><b>Current Stars</b></a>
          <a class="mega__link" href="/legends/"><b>Legends</b></a>
          <a class="mega__link" href="/women/"><b>Women's Division</b></a>
          <a class="mega__link" href="/wrestlers/"><b>All Wrestlers</b></a></div>
        <div class="mega__col"><h3>By Promotion</h3>
          <a class="mega__link" href="/promotions/wwe/"><b>WWE / WWF</b></a>
          <a class="mega__link" href="/promotions/wcw/"><b>WCW</b></a>
          <a class="mega__link" href="/promotions/njpw/"><b>NJPW</b></a>
          <a class="mega__link" href="/promotions/tna/"><b>TNA / Impact</b></a></div>
        <div class="mega__col"><h3>Featured</h3>
          <a class="mega__link" href="/wrestlers/stone-cold-steve-austin/"><b>Stone Cold Steve Austin</b></a>
          <a class="mega__link" href="/wrestlers/aj-styles/"><b>AJ Styles</b></a>
          <a class="mega__link" href="/wrestlers/the-undertaker/"><b>The Undertaker</b></a>
          <a class="mega__link" href="/wrestlers/roman-reigns/"><b>Roman Reigns</b></a>
          <a class="mega__link" href="/wrestlers/ric-flair/"><b>Ric Flair</b></a></div>
      </div></li>
    <li class="nav__item"><a class="nav__link" href="/matches/" aria-haspopup="true" aria-expanded="false">Matches</a>
      <div class="mega"><div class="mega__col"><h3>Explore</h3>
          <a class="mega__link" href="/matches/"><b>All Matches</b></a>
          <a class="mega__link" href="/rankings/"><b>Top-Rated (5★)</b></a></div>
        <div class="mega__col"><h3>Editors' Picks</h3>
          <a class="mega__link" href="/matches/undertaker-vs-hbk-wm25/"><b>Undertaker vs HBK at WM25</b></a>
          <a class="mega__link" href="/matches/cm-punk-vs-cena-mitb-2011/"><b>CM Punk vs Cena at MITB '11</b></a></div></div></li>
    <li class="nav__item"><a class="nav__link" href="/events/" aria-haspopup="true" aria-expanded="false">Events</a>
      <div class="mega mega--wide"><div class="mega__col"><h3>Recent</h3>
          <a class="mega__link" href="/events/wrestlemania-42-2026/"><b>WrestleMania 42</b></a>
          <a class="mega__link" href="/events/night-of-champions-2026/"><b>Night of Champions 2026</b></a>
          <a class="mega__link" href="/events/backlash-2026/"><b>Backlash 2026</b></a></div>
        <div class="mega__col"><h3>Brands</h3>
          <a class="mega__link" href="/events/wrestlemania/"><b>WrestleMania</b></a>
          <a class="mega__link" href="/events/royal-rumble/"><b>Royal Rumble</b></a>
          <a class="mega__link" href="/events/elimination-chamber/"><b>Elimination Chamber</b></a></div>
        <div class="mega__col"><h3>&nbsp;</h3>
          <a class="mega__link" href="/events/"><b>All Events</b></a>
          <a class="mega__link" href="/moments/"><b>Moments</b></a>
          <a class="mega__link" href="/events/backlash/"><b>Backlash</b></a></div></div></li>
    <li class="nav__item"><a class="nav__link" href="/promotions/" aria-haspopup="true" aria-expanded="false">Promotions</a>
      <div class="mega"><div class="mega__col"><h3>Active</h3>
          <a class="mega__link" href="/promotions/wwe/"><b>WWE</b></a>
          <a class="mega__link" href="/promotions/aew/"><b>AEW</b></a>
          <a class="mega__link" href="/promotions/njpw/"><b>NJPW</b></a>
          <a class="mega__link" href="/promotions/tna/"><b>TNA / Impact</b></a></div>
        <div class="mega__col"><h3>Legacy &amp; NXT</h3>
          <a class="mega__link" href="/promotions/wcw/"><b>WCW</b></a>
          <a class="mega__link" href="/promotions/ecw/"><b>ECW</b></a>
          <a class="mega__link" href="/promotions/nxt/"><b>NXT</b></a>
          <a class="mega__link" href="/promotions/"><b>All Promotions</b></a></div></div></li>
    <li class="nav__item"><a class="nav__link" href="/hall-of-fame/" aria-haspopup="true" aria-expanded="false">Hall of Fame</a>
      <div class="mega theme-hof"><div class="mega__col"><h3>Classes</h3>
          <a class="mega__link" href="/hall-of-fame/2026/"><b>Class of 2026</b></a>
          <a class="mega__link" href="/hall-of-fame/2025/"><b>Class of 2025</b></a>
          <a class="mega__link" href="/hall-of-fame/"><b>All Classes</b></a></div>
        <div class="mega__col"><h3>Legends</h3>
          <a class="mega__link" href="/wrestlers/ric-flair/"><b>Ric Flair</b></a>
          <a class="mega__link" href="/wrestlers/aj-styles/"><b>AJ Styles (2026)</b></a>
          <a class="mega__link" href="/showcases/aj-styles/"><b>AJ Styles Showcase</b></a></div></div></li>
    <li class="nav__item"><a class="nav__link" href="/media/" aria-haspopup="true" aria-expanded="false">Media</a>
      <div class="mega theme-media"><div class="mega__col"><h3>Creators</h3>
          <a class="mega__link" href="/media/chris-van-vliet/"><b>Chris Van Vliet</b></a>
          <a class="mega__link" href="/media/"><b>All Media</b></a></div></div></li>
    <li class="nav__item"><a class="nav__link" href="/rankings/" aria-haspopup="true" aria-expanded="false">More</a>
      <div class="mega mega--wide"><div class="mega__col"><h3>Titles &amp; Teams</h3>
          <a class="mega__link" href="/titles/"><b>Championships</b></a>
          <a class="mega__link" href="/factions/"><b>Factions &amp; Stables</b></a>
          <a class="mega__link" href="/tag-teams/"><b>Tag Teams</b></a></div>
        <div class="mega__col"><h3>Explore</h3>
          <a class="mega__link" href="/rivalries/"><b>Rivalries</b></a>
          <a class="mega__link" href="/relationships/"><b>Relationships</b></a>
          <a class="mega__link" href="/rankings/"><b>Rankings</b></a></div>
        <div class="mega__col"><h3>More</h3>
          <a class="mega__link" href="/about/"><b>About</b></a>
          <a class="mega__link" href="/methodology/"><b>Methodology</b></a>
          <a class="mega__link" href="/membership/"><b>Insider</b></a></div></div></li>
    <li class="nav__spacer" aria-hidden="true"></li>
    <li class="nav__item nav__item--search"><button class="nav__search" type="button" data-cmdk-open aria-label="Search (Command-K)">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
      Search <kbd>&#8984;K</kbd></button></li>
  </ul>
</nav></div></header>"""

PALETTE = """<div class="cmdk" id="cmdk" role="dialog" aria-modal="true" aria-label="Search Wrestle Lore" aria-hidden="true" data-wl-shell>
  <div class="cmdk__box"><div class="cmdk__head">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
    <input class="cmdk__input" type="text" placeholder="Search wrestlers, events, moments, matches…" aria-label="Search" autocomplete="off">
    <span class="cmdk__hint">Esc</span></div>
    <ul class="cmdk__results" role="listbox" aria-label="Search results"></ul>
    <div class="cmdk__foot"><span><kbd>&#8593;&#8595;</kbd> navigate</span><span><kbd>&#8629;</kbd> open</span><span><kbd>esc</kbd> close</span></div>
  </div></div>"""

FOOTER = """<footer class="site-footer" data-wl-shell><div class="wrap">
  <p>&copy; 2026 Wrestle Lore. All rights reserved.</p>
  <nav><a href="/about/">About</a> · <a href="/methodology/">Methodology</a> · <a href="/membership/">Insider</a></nav>
</div></footer>"""

SCRIPTS = '<script src="/js/search-index.js" defer></script>\n<script src="/js/nav.js" defer></script>\n'

RENAMES = [
  ("https://matdb.io", "https://matwrestling.com"),
  ("MAT — Match · Athlete · Timeline", "Wrestle Lore"),
  ("MAT Wrestling Database", "Wrestle Lore"),
  ("MAT — Pro Wrestling Database", "Wrestle Lore — Pro Wrestling Database"),
  ("MAT Wrestling", "Wrestle Lore"),
  ("MAT Insider", "Wrestle Lore Insider"),
  ("Join MAT", "Join Wrestle Lore"),
  ("| MAT<", "| Wrestle Lore<"),
  ("| MAT ", "| Wrestle Lore "),
  ('"MAT"', '"Wrestle Lore"'),
  (">MAT<", ">Wrestle Lore<"),
  ("MAT (Match", "Wrestle Lore (Match"),
  ("about MAT", "about Wrestle Lore"),
  ("MAT is ", "Wrestle Lore is "),
]

def apply(html):
    report = []
    # header: site-header wrapper OR old site-nav
    if re.search(r'<header class="site-header".*?</header>', html, re.DOTALL):
        html = re.sub(r'<header class="site-header".*?</header>', NAV, html, count=1, flags=re.DOTALL); report.append("hdr")
    elif re.search(r'<nav class="site-nav">.*?</nav>', html, re.DOTALL):
        html = re.sub(r'<nav class="site-nav">.*?</nav>', NAV, html, count=1, flags=re.DOTALL); report.append("oldnav")
    else:
        report.append("NOHDR")
    # palette: replace existing or inject after header
    if re.search(r'<div class="cmdk"[^>]*id="cmdk".*?</div>\s*</div>', html, re.DOTALL):
        html = re.sub(r'<div class="cmdk"[^>]*id="cmdk".*?</div>\s*</div>\s*</div>', PALETTE, html, count=1, flags=re.DOTALL)
    elif '</header>' in html:
        html = html.replace('</header>', '</header>\n' + PALETTE, 1); report.append("pal+")
    # footer
    if re.search(r'<footer[^>]*>.*?</footer>', html, re.DOTALL):
        html = re.sub(r'<footer[^>]*>.*?</footer>', FOOTER, html, count=1, flags=re.DOTALL); report.append("ftr")
    else:
        report.append("NOFTR")
    # scripts: ensure search-index + nav.js present before </body>
    if '/js/nav.js' not in html:
        i = html.rfind('</body>')
        if i != -1:
            html = html[:i] + SCRIPTS + html[i:]; report.append("js+")
    # renames + domain
    for a, b in RENAMES:
        html = html.replace(a, b)
    return html, report

def targets():
    out = []
    for p in glob.glob(ROOT + "/**/index.html", recursive=True):
        rel = p[len(ROOT):]
        if any(x in rel for x in EXCLUDE):
            continue
        out.append(p)
    return sorted(out)

if __name__ == "__main__":
    files = targets()
    stats = {"NOHDR":0,"NOFTR":0,"oldnav":0,"hdr":0}
    for p in files:
        html = open(p).read()
        new, rep = apply(html)
        if new != html:
            open(p, "w").write(new)
        for k in stats:
            if k in rep: stats[k]+=1
        if "NOHDR" in rep or "NOFTR" in rep:
            print("  WARN", p[len(ROOT):], rep)
    print(f"\nApplied shell to {len(files)} pages. header-swapped: {stats['hdr']+stats['oldnav']} (old-nav: {stats['oldnav']}) | NOHDR: {stats['NOHDR']} | NOFTR: {stats['NOFTR']}")
