#!/usr/bin/env python3
"""UNIVERSAL SHELL STAMPER — the nav/footer/palette come from /components/*.html.
To change the nav or footer site-wide: edit the component file, run this script,
commit, push. (Vercel auto-deploys on push.)

Stamps every page (including the home page — its .ticker7 strip sits OUTSIDE the
<header> element so it survives) with the single-source shell:
  components/meganav.html  -> replaces <header class="site-header"...>...</header>
  components/palette.html  -> replaces (or injects) the #cmdk command palette
  components/footer.html   -> replaces <footer ...>...</footer>
Also ensures /js/search-index.js + /js/nav.js, self-hosted fonts (Anton preload,
Google Fonts stripped), favicon/theme-color head links, and MAT->Wrestle Lore
renames. Excludes /zh/ /china/ /content/ /docs/ /assets/. Idempotent — safe to
re-run any number of times."""
import os, re, glob

ROOT = "/root/wwe"
COMPONENTS = os.path.join(ROOT, "components")
EXCLUDE = ("/zh/", "/china/", "/content/", "/docs/", "/assets/")

def _component(name):
    with open(os.path.join(COMPONENTS, name), encoding="utf-8") as f:
        return f.read().strip()

NAV = _component("meganav.html")
PALETTE = _component("palette.html")
FOOTER = _component("footer.html")

SCRIPTS = '<script src="/js/search-index.js" defer></script>\n<script src="/js/nav.js" defer></script>\n'

# Cache-busting version: short hash of the CSS + key JS so a deploy always serves fresh assets.
import hashlib
def _ver():
    h = hashlib.md5()
    for p in ("/css/site.css", "/js/nav.js", "/js/media.js", "/js/home-engage.js"):
        try:
            h.update(open(ROOT + p, "rb").read())
        except OSError:
            pass
    return h.hexdigest()[:8]
VER = _ver()

def fix_version(html):
    """Append ?v=<hash> to local css/js links so browsers/CDN re-fetch when they change."""
    def bust(m):
        path = m.group(2)
        return m.group(1) + path + '?v=' + VER + m.group(4)
    # href="/css/....css"(?v=...)?  and  src="/js/....js"(?v=...)?
    html = re.sub(r'(href=")(/[^"?]+\.css)(\?v=[0-9a-f]+)?(")', bust, html)
    html = re.sub(r'(src=")(/[^"?]+\.js)(\?v=[0-9a-f]+)?(")', bust, html)
    return html

# Self-hosted fonts: preload Anton (the display/LCP font); faces live in site.css.
FONT_PRELOAD = '<link rel="preload" href="/fonts/anton-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>'

# Favicon / PWA head links (Wrestle Lore championship-plate mark).
FAVICONS = (
    '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
    '<link rel="icon" href="/favicon.ico" sizes="any">\n'
    '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n'
    '<link rel="manifest" href="/site.webmanifest">'
)

def fix_head(html):
    """Ensure favicon links + theme-color sit right before the site.css <link>. Idempotent."""
    changed = False
    if 'href="/favicon.svg"' not in html:
        m = re.search(r'<link[^>]+href="/css/site\.css"[^>]*>', html)
        if m:
            html = html[:m.start()] + FAVICONS + '\n' + html[m.start():]; changed = True
    # normalise theme-color to the brand near-black (update existing or inject)
    if re.search(r'<meta[^>]+name="theme-color"[^>]*>', html):
        new = re.sub(r'<meta[^>]+name="theme-color"[^>]*>',
                     '<meta name="theme-color" content="#0b0c10">', html, count=1)
        if new != html: html = new; changed = True
    else:
        m = re.search(r'<link[^>]+href="/css/site\.css"[^>]*>', html)
        if m:
            html = html[:m.start()] + '<meta name="theme-color" content="#0b0c10">\n' + html[m.start():]
            changed = True
    return html, changed

def fix_fonts(html):
    """Strip render-blocking Google Fonts (preconnect + stylesheet) and ensure the
    Anton preload sits right before the site.css link. Idempotent."""
    changed = False
    # remove google fonts preconnect + stylesheet links (any whitespace variants)
    patterns = [
        r'\s*<link[^>]*rel="preconnect"[^>]*fonts\.(?:googleapis|gstatic)\.com[^>]*>',
        r'\s*<link[^>]*fonts\.googleapis\.com/css2[^>]*>',
    ]
    for p in patterns:
        new = re.sub(p, '', html)
        if new != html: html = new; changed = True
    # ensure single Anton preload before the site.css <link>
    if FONT_PRELOAD not in html:
        m = re.search(r'<link[^>]+href="/css/site\.css"[^>]*>', html)
        if m:
            html = html[:m.start()] + FONT_PRELOAD + '\n' + html[m.start():]; changed = True
    return html, changed

RENAMES = [
  ("https://matdb.io", "https://wrestlelore.com"),
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
    # NOTE: [ "] after site-header so both the legacy stamp (class="site-header")
    # and the universal nav7 stamp (class="site-header nav7") match on re-runs.
    if re.search(r'<header class="site-header[ "].*?</header>', html, re.DOTALL):
        html = re.sub(r'<header class="site-header[ "].*?</header>', lambda m: NAV, html, count=1, flags=re.DOTALL); report.append("hdr")
    elif re.search(r'<nav class="site-nav">.*?</nav>', html, re.DOTALL):
        html = re.sub(r'<nav class="site-nav">.*?</nav>', lambda m: NAV, html, count=1, flags=re.DOTALL); report.append("oldnav")
    else:
        report.append("NOHDR")
    # palette: replace existing or inject after header
    if re.search(r'<div class="cmdk"[^>]*id="cmdk".*?</div>\s*</div>', html, re.DOTALL):
        html = re.sub(r'<div class="cmdk"[^>]*id="cmdk".*?</div>\s*</div>\s*</div>', lambda m: PALETTE, html, count=1, flags=re.DOTALL)
    elif '</header>' in html:
        html = html.replace('</header>', '</header>\n' + PALETTE, 1); report.append("pal+")
    # footer
    if re.search(r'<footer[^>]*>.*?</footer>', html, re.DOTALL):
        html = re.sub(r'<footer[^>]*>.*?</footer>', lambda m: FOOTER, html, count=1, flags=re.DOTALL); report.append("ftr")
    else:
        report.append("NOFTR")
    # scripts: ensure search-index + nav.js present before </body>
    if '/js/nav.js' not in html:
        i = html.rfind('</body>')
        if i != -1:
            html = html[:i] + SCRIPTS + html[i:]; report.append("js+")
    # fonts: self-host (strip Google Fonts, preload Anton)
    html, fchg = fix_fonts(html)
    if fchg: report.append("font")
    # head: favicon links + theme-color
    html, hchg = fix_head(html)
    if hchg: report.append("head")
    # cache-bust css/js so new styles actually load after a deploy
    html = fix_version(html)
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
    # standalone shells that aren't index.html
    for extra in ("/404.html",):
        if os.path.exists(ROOT + extra):
            out.append(ROOT + extra)
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
