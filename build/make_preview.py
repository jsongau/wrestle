#!/usr/bin/env python3
"""make_preview.py - turn a built page into a standalone file:// previewable copy.

Why this exists: pages under the repo link assets root-absolutely (/css/site.css,
/fonts/*.woff2). Opened from ~/Downloads they resolve against the filesystem root and
load nothing, so the preview arrives unstyled. This inlines every asset the page needs.

    WL_ROOT="$PWD" python3 build/make_preview.py <page-path> [<page-path> ...]

Three traps this file encodes, all of which cost real time:

  1. str.replace("</body>", ...) replaces EVERY occurrence. css/site.css has a comment
     reading `place <div class="grain"> before </body>`, so a global replace injects the
     script payload into the middle of the stylesheet and silently kills every CSS rule
     after that byte. Anchor on rfind() instead. Same applies to </head>.

  2. Do NOT concatenate site.css and profile.css into one <style>. Keep one block per
     sheet, in link order, so a parse error in the first cannot swallow the second.

  3. A general url\((.*?)\) regex is wrong: site.css embeds inline SVG data URIs that
     themselves contain url(%23n), and any non-greedy matcher truncates the data URI at
     that inner paren. Match the literal /fonts/ and /assets/ prefixes only.

Insert the inlined sheets BEFORE the page-local <style> block, not at </head>, or the
cascade flips and the page-local rules lose to profile.css.
"""

import base64, os, re, sys

ROOT = os.environ.get("WL_ROOT", os.getcwd())
OUT  = os.environ.get("WL_PREVIEW_OUT", "/tmp/wl-preview")
os.makedirs(OUT, exist_ok=True)

def b64(path, mime):
    with open(path, "rb") as f:
        return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode())

def inline_css(css):
    """Only rewrite the two root-absolute asset prefixes this site uses.

    A general url(...) regex is WRONG here: site.css embeds inline SVG data URIs
    that themselves contain url(%23n) for a filter reference, and any non-greedy
    matcher truncates the data URI at that inner paren, silently corrupting every
    rule after it. Match the literal prefixes instead.
    """
    for rel in sorted(set(re.findall(r'url\("(/(?:fonts|assets)/[^"]+)"\)', css))):
        p = os.path.join(ROOT, rel.lstrip("/"))
        if not os.path.exists(p):
            print("  MISSING ASSET:", rel); continue
        mime = "font/woff2" if p.endswith(".woff2") else "image/png"
        css = css.replace('url("%s")' % rel, 'url("%s")' % b64(p, mime))
    left = re.findall(r'url\("(/[^"]+)"\)', css)
    assert not left, "unresolved root-absolute urls: %s" % set(left)
    return css

LOGO = b64(os.path.join(ROOT, "assets/wrestle-lore-logo.png"), "image/png") \
       if os.path.exists(os.path.join(ROOT, "assets/wrestle-lore-logo.png")) else ""

_CSS_CACHE = {}
def css_block(rel):
    """Inline one stylesheet, cached. One <style> per sheet, never concatenated:
    an unterminated construct in the first would swallow the second."""
    if rel not in _CSS_CACHE:
        p = os.path.join(ROOT, rel.split("?")[0].lstrip("/"))   # apply_shell cache-busts hrefs
        assert os.path.exists(p), "stylesheet not found, preview would be unstyled: " + p
        _CSS_CACHE[rel] = "<style>%s</style>\n" % inline_css(open(p, encoding="utf-8").read())
    return _CSS_CACHE[rel]

_JS_CACHE = {}
def js_block(rel):
    """Inline one script, cached. One <script> per file so a throw in an early file
    does not silently kill every later one."""
    if rel not in _JS_CACHE:
        p = os.path.join(ROOT, rel.split("?")[0].lstrip("/"))   # apply_shell cache-busts srcs
        assert os.path.exists(p), "script not found: " + p
        _JS_CACHE[rel] = "<script>%s</script>\n" % open(p, encoding="utf-8").read()
    return _JS_CACHE[rel]

BANNER = (
  '<div id="wl-preview-note" style="position:fixed;left:12px;bottom:12px;z-index:99999;'
  'font:600 11px/1.4 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.08em;'
  'text-transform:uppercase;color:#0b0b0d;background:#d4af37;padding:7px 11px;border-radius:4px;'
  'box-shadow:0 6px 24px rgba(0,0,0,.5)">Preview &middot; standalone copy &middot; internal links are inert</div>')

def build_from(src, name):
    h = open(src, encoding="utf-8").read()

    # Take the asset list from the page itself, not a hardcoded one: an event page and
    # a profile page load different scripts, and forcing profile.js onto a page with no
    # .wl-dossier throws.
    sheets = re.findall(r'<link rel="stylesheet" href="(/[^"]+)">', h)
    scripts = re.findall(r'<script src="(/[^"]+)"[^>]*></script>', h)
    assert sheets, "no stylesheets found in " + src
    CSS = "".join(css_block(x) for x in sheets)
    JS  = "".join(js_block(x)  for x in scripts)

    h = re.sub(r'<link rel="stylesheet" href="/[^"]+">\s*', "", h)
    h = re.sub(r'<link rel="preload"[^>]*>\s*', "", h)
    h = re.sub(r'<script src="/[^"]+"[^>]*></script>\s*', "", h)

    # Insert the shared sheets BEFORE any page-local <style>, mirroring link order.
    # Inserting at </head> flips the cascade and the page-local rules lose.
    head_end = h.find("</head>")
    assert head_end != -1, "no </head> in " + src
    i = h.find("<style>", 0, head_end)
    if i == -1: i = head_end
    h = h[:i] + CSS + h[i:]

    # Anchor on the LAST </body>. str.replace would also hit the one inside a CSS
    # comment in site.css and inject the scripts into the middle of the stylesheet.
    j = h.rfind("</body>")
    assert j != -1, "no </body> in " + src
    h = h[:j] + BANNER + "\n" + JS + h[j:]

    if LOGO: h = h.replace('src="/assets/wrestle-lore-logo.png"', 'src="%s"' % LOGO)
    out = os.path.join(OUT, "%s-preview.html" % name)
    open(out, "w", encoding="utf-8").write(h)
    return out, len(h)

def main(argv):
    if not argv:
        print(__doc__); return 1
    os.makedirs(OUT, exist_ok=True)
    for rel in argv:
        rel = rel.strip("/")
        src = os.path.join(ROOT, rel)
        if os.path.isdir(src): src = os.path.join(src, "index.html")
        if not os.path.exists(src):
            print("  MISSING PAGE:", rel); continue
        name = rel.rstrip("/").replace("/index.html", "").strip("/").replace("/", "-")
        out, n = build_from(src, name)
        print("%-52s %6.1f KB" % (os.path.basename(out), n / 1024))
    print("out:", OUT)
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
