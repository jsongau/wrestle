import base64, os

ROOT = "/root/wwe"
OUT = "/root/wrestle-lore-logo-3-markonly.html"

with open(os.path.join(ROOT, "index.html"), encoding="utf-8") as f:
    h = f.read()
with open(os.path.join(ROOT, "css/site.css"), encoding="utf-8") as f:
    css = f.read()

# ---- 1. base64-embed fonts into the CSS via str.replace loop (NOT regex) ----
fonts = [
    "anton-latin-400-normal.woff2",
    "oswald-latin-400-normal.woff2",
    "oswald-latin-600-normal.woff2",
    "oswald-latin-700-normal.woff2",
    "inter-latin-400-normal.woff2",
    "inter-latin-600-normal.woff2",
    "inter-latin-700-normal.woff2",
    "jetbrains-mono-latin-400-normal.woff2",
    "jetbrains-mono-latin-600-normal.woff2",
]
for fn in fonts:
    p = os.path.join(ROOT, "fonts", fn)
    b = base64.b64encode(open(p, "rb").read()).decode("ascii")
    dataurl = "data:font/woff2;base64," + b
    css = css.replace('/fonts/' + fn, dataurl)

# ---- 2. redesign the .brand7 lockup CSS (block A) ----
OLD_CSS_A = (
'.nav7 .brand7{display:flex;align-items:center;gap:.5em;font-family:var(--anton);font-weight:400;font-size:22px;\n'
'  letter-spacing:.02em;color:#fff;text-decoration:none;margin-right:14px;white-space:nowrap;user-select:none;}\n'
'.nav7 .brand7:hover{color:#fff;}\n'
'.nav7 .mark{position:relative;overflow:hidden;width:33px;height:33px;display:grid;place-content:center;border-radius:4px;\n'
'  color:#1a1400;font-family:var(--anton);font-size:15px;background:linear-gradient(180deg,#f7e08a,var(--gold) 55%,var(--golddim));\n'
'  box-shadow:0 0 0 1px var(--golddim),0 4px 14px rgba(212,175,55,.18);}\n'
'.nav7 .wlshim{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;mix-blend-mode:screen;}\n'
'.nav7 .wlsweep{animation:wlsweep7 6s linear infinite;}\n'
'@keyframes wlsweep7{0%{transform:translateX(-16px)}9%{transform:translateX(48px)}100%{transform:translateX(48px)}}'
)
assert OLD_CSS_A in css, "brand7 CSS block A not found"

NEW_CSS_A = (
'/* ===== brand lockup L3 "PURE MARK" (belt is the hero + mono kicker) ===== */\n'
'.nav7 .brand7{display:flex;align-items:center;gap:11px;color:#fff;text-decoration:none;margin-right:16px;\n'
'  white-space:nowrap;user-select:none;-webkit-tap-highlight-color:transparent;}\n'
'.nav7 .brand7:hover{color:#fff;}\n'
'.nav7 .brand7:hover .brand7__logo{filter:drop-shadow(0 2px 11px rgba(242,204,75,.48));}\n'
'.nav7 .brand7:hover .brand7__kick{color:#fff;}\n'
'.nav7 .brand7:focus-visible{outline:2px solid var(--goldb);outline-offset:3px;border-radius:3px;}\n'
'.nav7 .brand7__mark{position:relative;display:block;flex:0 0 auto;width:71px;height:48px;}\n'
'.nav7 .brand7__logo{display:block;width:100%;height:100%;object-fit:contain;\n'
'  filter:drop-shadow(0 2px 8px rgba(212,175,55,.30));transition:filter .2s ease;}\n'
'/* dual-streak specular gleam, MASKED to the belt shape so light travels through the metal */\n'
'.nav7 .brand7__sheen{position:absolute;inset:0;pointer-events:none;opacity:0;z-index:1;\n'
'  -webkit-mask-image:url("/assets/wrestle-lore-logo.png");mask-image:url("/assets/wrestle-lore-logo.png");\n'
'  -webkit-mask-size:contain;mask-size:contain;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;\n'
'  -webkit-mask-position:center;mask-position:center;\n'
'  background-image:linear-gradient(116deg,\n'
'    transparent 38%,rgba(255,246,214,.45) 42.5%,rgba(255,255,255,.98) 46%,rgba(255,246,214,.4) 49.5%,transparent 54%,\n'
'    transparent 60%,rgba(255,244,206,.38) 63.5%,rgba(255,255,255,.82) 66.5%,rgba(255,244,206,.32) 69.5%,transparent 74%);\n'
'  background-repeat:no-repeat;background-size:260% 260%;background-position:-62% -62%;\n'
'  mix-blend-mode:plus-lighter;}\n'
'.nav7 .brand7.is-gleam .brand7__sheen{animation:brandGleam .86s cubic-bezier(.38,.05,.28,1) forwards;}\n'
'@keyframes brandGleam{0%{opacity:0;background-position:-62% -62%;}12%{opacity:1;}84%{opacity:1;}100%{opacity:0;background-position:162% 162%;}}\n'
'/* low-key mono kicker: belt already reads "WL", so the wordmark stays quiet and space-saving */\n'
'.nav7 .brand7__kick{align-self:center;font-family:var(--mono7);font-weight:600;font-size:10px;\n'
'  line-height:1;text-transform:uppercase;letter-spacing:.30em;text-indent:.30em;\n'
'  color:var(--goldb);transition:color .2s ease;}'
)
css = css.replace(OLD_CSS_A, NEW_CSS_A)

# ---- 3. update reduced-motion rule to reference new classes ----
css = css.replace(
    '.nav7 .wlsweep,.nav7 .nv-t .cspark path,.nav7 .pf--champ,.nav7 .pf--day{animation:none !important;}\n'
    '  .nav7 .wlshim{display:none !important;}',
    '.nav7 .brand7.is-gleam .brand7__sheen,.nav7 .nv-t .cspark path,.nav7 .pf--champ,.nav7 .pf--day{animation:none !important;}\n'
    '  .nav7 .brand7__sheen{display:none !important;}'
)

# ---- 3b. mobile: hide the kicker to save width, belt stands alone ----
css = css.replace('.nav7 .brand7 .bword{display:none;}',
                  '.nav7 .brand7 .brand7__kick{display:none;}')

# ---- 3c. neutralize the old .mark--logo sizing block (unused classes now) ----
OLD_MARK_BLOCK = (
'/* ---------- NAV LOGO MARK (belt PNG + kept sheen) + stacked wordmark ---------- */\n'
'.nav7 .mark--logo{width:auto;height:42px;background:none;box-shadow:none;border-radius:0;overflow:visible;}\n'
'.nav7 .mark--logo img{width:auto;height:100%;object-fit:contain;display:block;filter:drop-shadow(0 2px 8px rgba(212,175,55,.22));}\n'
'.nav7 .mark--logo .wlshim{width:100%;height:100%;}\n'
'.nav7 .bword--stack{display:flex;flex-direction:column;line-height:.86;letter-spacing:.03em;font-family:var(--anton);text-transform:uppercase;font-size:17px;}\n'
'.nav7 .bword--stack b{font-weight:400;display:block;}'
)
assert OLD_MARK_BLOCK in css, "old mark--logo block not found"
css = css.replace(OLD_MARK_BLOCK,
                  '/* ---------- NAV LOGO MARK: superseded by L3 "PURE MARK" lockup above ---------- */')

# ---- 4. remove preload font links (no google-fonts links present) ----
h = h.replace(
    '<link rel="preload" href="/fonts/anton-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>\n', '')
h = h.replace(
    '<link rel="preload" href="/fonts/jetbrains-mono-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>\n', '')

# ---- 5. inline the stylesheet ----
assert '<link rel="stylesheet" href="/css/site.css">' in h
h = h.replace('<link rel="stylesheet" href="/css/site.css">',
              '<style>\n' + css + '\n</style>')

# ---- 6. replace the brand lockup markup ----
OLD_MARK = ('<a class="brand7" href="/" aria-label="Wrestle Lore, home"><span class="mark mark--logo">'
'<img src="/assets/wrestle-lore-logo.png" alt="" width="61" height="40" decoding="async">'
'<svg class="wlshim" viewBox="0 0 33 33" aria-hidden="true" focusable="false"><defs>'
'<linearGradient id="wlsg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
'<stop offset=".5" stop-color="#fff" stop-opacity=".5"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>'
'</linearGradient></defs><g class="wlsweep"><rect x="-2" y="-6" width="9" height="45" fill="url(#wlsg)" '
'transform="skewX(-18)"/></g></svg></span><span class="bword bword--stack"><b>Wrestle</b><b>Lore</b></span></a>')
assert OLD_MARK in h, "brand markup not found"

NEW_MARK = ('<a class="brand7" href="/" aria-label="Wrestle Lore, home">'
'<span class="brand7__mark">'
'<img class="brand7__logo" src="/assets/wrestle-lore-logo.png" alt="" width="71" height="48" decoding="async">'
'<span class="brand7__sheen" aria-hidden="true"></span>'
'</span>'
'<span class="brand7__kick" aria-hidden="true">Wrestle Lore</span></a>')
h = h.replace(OLD_MARK, NEW_MARK)

# ---- 7. base64-embed the logo PNG (str.replace on the path) ----
logo_b = base64.b64encode(open(os.path.join(ROOT, "assets/wrestle-lore-logo.png"), "rb").read()).decode("ascii")
logo_data = "data:image/png;base64," + logo_b
h = h.replace('/assets/wrestle-lore-logo.png', logo_data)  # hits img src AND mask-image

# ---- 8. remove external script tags, inline the required JS before </body> ----
for tag in [
    '<script src="/js/main.js" defer></script>\n',
    '<script src="/js/enhance.js" defer></script>\n',
    '<script src="/js/search-index.js" defer></script>\n',
    '<script src="/js/nav.js" defer></script>\n',
    '<script src="/js/home-engage.js" defer></script>\n',
    '<script src="/js/media.js" defer></script>\n',
]:
    h = h.replace(tag, '')

inline_order = ["search-index.js", "nav.js", "enhance.js", "main.js", "home-engage.js"]
blocks = []
for jf in inline_order:
    src = open(os.path.join(ROOT, "js", jf), encoding="utf-8").read()
    blocks.append('<script>\n/* ' + jf + ' */\n' + src + '\n</script>')

# tiny vanilla click-sheen handler: dual-streak sweep, click-only, bails on reduced-motion
sheen_js = '''<script>
/* brand click-sheen: masked dual-streak specular sweep, click-only, bails on reduced-motion */
(function(){
  var mq = window.matchMedia && window.matchMedia('(prefers-reduced-motion:reduce)');
  if (mq && mq.matches) return;
  var brand = document.querySelector('.nav7 .brand7');
  if (!brand) return;
  var sheen = brand.querySelector('.brand7__sheen');
  if (!sheen) return;
  var running = false;
  function fire(){ if (running) return; running = true; brand.classList.add('is-gleam'); }
  sheen.addEventListener('animationend', function(){ brand.classList.remove('is-gleam'); running = false; });
  brand.addEventListener('click', fire);
  brand.addEventListener('keydown', function(e){ if (e.key === 'Enter' || e.key === ' ') fire(); });
})();
</script>'''
blocks.append(sheen_js)

idx = h.rfind('</body>')
assert idx != -1
h = h[:idx] + '\n'.join(blocks) + '\n' + h[idx:]

with open(OUT, "w", encoding="utf-8") as f:
    f.write(h)

print("wrote", OUT, len(h), "bytes")
print("data-url logo occurrences:", h.count(logo_data))
print("mask-image present:", 'mask-image:url("data:image/png' in h)
print("remaining /fonts/ refs:", h.count('/fonts/'))
print("remaining /js/ src refs:", h.count('src="/js/'))
print("remaining /css/ refs:", h.count('/css/site.css'))
print("preload links remaining:", h.count('rel="preload"'))
