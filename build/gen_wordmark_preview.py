#!/usr/bin/env python3
"""Generate ONE portable, self-contained comparison page showing 3 full-bleed
nav concepts, each with a distinct WRESTLE/LORE wordmark + nav-tab font.
Fonts + belt logo are base64-inlined so the file works anywhere (Downloads)."""
import base64, os
ROOT = "/root/wwe"

def b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

LOGO = "data:image/png;base64," + b64(ROOT + "/assets/wrestle-lore-logo.png")
F = {
    "anton":   b64(ROOT + "/fonts/anton-latin-400-normal.woff2"),
    "osw400":  b64(ROOT + "/fonts/oswald-latin-400-normal.woff2"),
    "osw600":  b64(ROOT + "/fonts/oswald-latin-600-normal.woff2"),
    "osw700":  b64(ROOT + "/fonts/oswald-latin-700-normal.woff2"),
    "int400":  b64(ROOT + "/fonts/inter-latin-400-normal.woff2"),
    "int600":  b64(ROOT + "/fonts/inter-latin-600-normal.woff2"),
    "int700":  b64(ROOT + "/fonts/inter-latin-700-normal.woff2"),
    "mono":    b64(ROOT + "/fonts/jetbrains-mono-latin-400-normal.woff2"),
}
def face(fam, key, wt):
    return (f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{wt};"
            f"font-display:swap;src:url(data:font/woff2;base64,{F[key]}) format('woff2');}}")
FONTS = "\n".join([
    face("Anton","anton",400),
    face("Oswald","osw400",400), face("Oswald","osw600",600), face("Oswald","osw700",700),
    face("Inter","int400",400), face("Inter","int600",600), face("Inter","int700",700),
    face("JetBrains Mono","mono",400),
])

TABS = ["Superstars","Matches","Events","Promotions","Hall of Fame","Titles & Teams","Media"]

def tabs_html():
    return "".join(f'<a class="tab" href="#">{t}</a>' for t in TABS)

def bar(concept_class, brand_html):
    return f'''
    <header class="site-header nav7 {concept_class}">
      <nav class="bar" aria-label="Primary">
        <a class="brand7" href="#" aria-label="Wrestle Lore home">
          <span class="mark mark--logo"><img src="{LOGO}" alt="" width="141" height="96"><span class="sheen" aria-hidden="true"></span></span>
          {brand_html}
        </a>
        <div class="tabs7">{tabs_html()}</div>
        <span class="spacer"></span>
        <button class="pill" type="button"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg><span class="ph">Search wrestlers, matches, titles</span><span class="kbd7">⌘K</span></button>
        <a class="cta" href="#">Join Insider</a>
      </nav>
    </header>'''

# --- 3 brand lockups ---
BRAND_A = '<span class="bword bw-a"><b>Wrestle</b><span class="rule"></span><b>Lore</b></span>'
BRAND_B = '<span class="bword bw-b"><b>Wrestle</b><b>Lore</b></span>'
BRAND_C = '<span class="bword bw-c"><b class="w">Wrestle</b><b class="l">Lore</b></span>'

CSS = f'''
{FONTS}
*{{box-sizing:border-box;margin:0;padding:0;}}
:root{{
  --anton:'Anton',sans-serif; --osw:'Oswald',sans-serif; --inter:'Inter',system-ui,sans-serif; --mono7:'JetBrains Mono',monospace;
  --e1:#101216;--e2:#161a20;--e3:#1e232b;--line:#242a32;--line2:#39414c;
  --tx:#e8eaed;--mut:#9aa2ad;--dim:#828a96;
  --gold:#d4af37;--goldb:#f2cc4b;--golddim:#8c7420;--red:#e11d2a;--redb:#ff3b48;
  --bg:#0b0c10;
}}
html,body{{background:#07080b;color:var(--tx);font-family:var(--inter);}}
.page{{max-width:1180px;margin:0 auto;padding:34px 20px 80px;}}
.hd{{text-align:center;margin-bottom:8px;}}
.hd h1{{font-family:var(--anton);font-weight:400;font-size:30px;letter-spacing:.02em;text-transform:uppercase;}}
.hd p{{color:var(--mut);font-size:14px;margin-top:8px;max-width:640px;margin-inline:auto;line-height:1.5;}}
.demo{{margin:44px 0 0;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:var(--bg);}}
.demo__lbl{{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;padding:16px 22px 4px;}}
.demo__lbl .n{{font-family:var(--anton);font-weight:400;font-size:20px;color:var(--goldb);letter-spacing:.02em;}}
.demo__lbl .t{{font-family:var(--mono7);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--dim);}}
.demo__lbl .d{{color:var(--mut);font-size:13px;flex-basis:100%;line-height:1.5;padding-top:4px;}}
/* full-bleed frame: the bar spans the whole demo width edge-to-edge */
.frame{{margin-top:14px;background:linear-gradient(180deg,#0d0e13,#0a0b0f);}}

/* ===== SHARED NAV7 (full bleed) ===== */
.nav7{{position:relative;background:color-mix(in srgb,#0b0c0f 82%,transparent);border-bottom:1px solid var(--line);}}
.nav7 .bar{{display:flex;align-items:center;gap:4px;min-height:62px;
  /* FULL BLEED: no max-width wrap; just edge padding */
  width:100%;padding-inline:26px;}}
.nav7 .brand7{{display:flex;align-items:center;gap:.6em;color:#fff;text-decoration:none;margin-right:16px;white-space:nowrap;}}
.nav7 .mark--logo{{position:relative;display:flex;align-items:center;width:auto;height:96px;margin:-17px 0;overflow:visible;}}
.nav7 .mark--logo img{{width:auto;height:96px;object-fit:contain;display:block;filter:drop-shadow(0 3px 13px rgba(212,175,55,.36));}}
.nav7 .mark--logo .sheen{{position:absolute;inset:0;pointer-events:none;z-index:2;
  -webkit-mask:url("{LOGO}") center/contain no-repeat;mask:url("{LOGO}") center/contain no-repeat;
  background:linear-gradient(105deg,transparent 41%,rgba(255,255,255,.55) 48%,rgba(255,255,255,.95) 50%,rgba(255,246,210,.55) 52%,transparent 59%);
  background-size:220% 100%;background-repeat:no-repeat;background-position:190% 0;mix-blend-mode:screen;
  animation:wlgleam 6.5s cubic-bezier(.4,0,.2,1) infinite;}}
.nav7 .brand7:hover .mark--logo .sheen{{animation:wlgleam .75s cubic-bezier(.4,0,.2,1);}}
@keyframes wlgleam{{0%{{background-position:190% 0}}13%{{background-position:-90% 0}}100%{{background-position:-90% 0}}}}
.nav7 .tabs7{{display:flex;align-items:center;gap:2px;}}
.nav7 .tab{{display:inline-block;color:var(--mut);text-decoration:none;cursor:pointer;position:relative;white-space:nowrap;}}
.nav7 .tab:hover{{color:#fff;}}
.nav7 .spacer{{flex:1;}}
.nav7 .pill{{display:flex;align-items:center;gap:.55em;background:var(--e2);border:1px solid var(--line2);
  border-radius:99px;padding:.5em .9em;color:var(--dim);cursor:pointer;min-width:210px;
  font-size:13px;font-family:var(--inter);margin:0 12px 0 8px;}}
.nav7 .pill .kbd7{{margin-left:auto;font-family:var(--mono7);font-size:11px;background:var(--e3);border:1px solid var(--line2);border-radius:5px;padding:.1em .45em;color:var(--mut);}}
.nav7 .cta{{background:transparent;border:1px solid var(--red);color:var(--redb);font-family:var(--osw);
  text-transform:uppercase;letter-spacing:.06em;font-weight:600;font-size:13px;padding:.6em 1.05em;border-radius:4px;text-decoration:none;white-space:nowrap;}}
.nav7 .cta:hover{{background:var(--red);color:#fff;}}

/* base wordmark */
.nav7 .bword{{display:flex;flex-direction:column;text-transform:uppercase;color:#fff;}}
.nav7 .bword b{{font-weight:400;display:block;}}

/* =========================================================
   CONCEPT A — "Broadcast Plate": Anton stack + gold hairline
   Display font stays Anton. Tabs stay Oswald (condensed).
   ========================================================= */
.cA .bw-a{{font-family:var(--anton);font-size:19px;line-height:1.02;letter-spacing:.05em;gap:3px;}}
.cA .bw-a .rule{{height:2px;width:100%;background:linear-gradient(90deg,var(--goldb),var(--golddim));border-radius:2px;margin:1px 0;}}
.cA .bw-a b:last-child{{color:var(--goldb);}}
.cA .tab{{font-family:var(--osw);text-transform:uppercase;letter-spacing:.06em;font-weight:600;font-size:13.5px;padding:.85em .7em;}}
.cA .tab::after{{content:"";position:absolute;left:.7em;right:.7em;bottom:8px;height:2px;background:var(--red);transform:scaleX(0);transform-origin:left;transition:transform .1s;}}
.cA .tab:hover::after{{transform:scaleX(1);}}

/* =========================================================
   CONCEPT B — "Sport Modern": Oswald condensed, tracked wide.
   Wordmark switches to Oswald; NAV TABS switch to Inter (clean sans).
   ========================================================= */
.cB .bw-b{{font-family:var(--osw);font-weight:700;font-size:20px;line-height:1.06;letter-spacing:.22em;gap:4px;}}
.cB .bw-b b{{font-weight:700;}}
.cB .bw-b b:last-child{{color:var(--goldb);}}
.cB .tab{{font-family:var(--inter);font-weight:600;letter-spacing:.01em;font-size:13.5px;padding:.85em .7em;text-transform:none;}}
.cB .tab::after{{content:"";position:absolute;left:.7em;right:.7em;bottom:8px;height:2px;background:var(--gold);transform:scaleX(0);transform-origin:left;transition:transform .1s;}}
.cB .tab:hover::after{{transform:scaleX(1);}}

/* =========================================================
   CONCEPT C — "Masthead": big Anton WRESTLE + wide-tracked gold
   LORE subline, vertical divider between logo and text.
   Tabs = Oswald 400 lighter, wider tracking (airier directory).
   ========================================================= */
.cC .brand7{{gap:.85em;}}
.cC .bw-c{{position:relative;padding-left:16px;gap:2px;}}
.cC .bw-c::before{{content:"";position:absolute;left:0;top:3px;bottom:3px;width:2px;background:linear-gradient(180deg,var(--goldb),var(--golddim));border-radius:2px;}}
.cC .bw-c .w{{font-family:var(--anton);font-size:22px;line-height:.9;letter-spacing:.03em;}}
.cC .bw-c .l{{font-family:var(--osw);font-weight:600;font-size:12px;letter-spacing:.62em;color:var(--goldb);margin-top:2px;}}
.cC .tab{{font-family:var(--osw);font-weight:400;letter-spacing:.11em;font-size:14px;padding:.85em .68em;text-transform:uppercase;}}
.cC .tab::after{{content:"";position:absolute;left:.68em;right:.68em;bottom:8px;height:2px;background:var(--red);transform:scaleX(0);transform-origin:left;transition:transform .1s;}}
.cC .tab:hover::after{{transform:scaleX(1);}}

@media(max-width:900px){{.nav7 .tabs7{{display:none;}} .nav7 .pill{{min-width:0;}}}}
'''

DEMOS = [
    ("cA", "A", "Broadcast Plate", "Anton display + gold hairline rule",
     "Keeps the Anton title font. WRESTLE in white, LORE in gold, split by a thin gold rule that fixes the cramped gap. Nav directory stays Oswald condensed — the classic broadcast look.",
     BRAND_A),
    ("cB", "B", "Sport Modern", "Oswald condensed wordmark · Inter nav tabs",
     "Wordmark is tall condensed Oswald with wide tracking so the two lines breathe. The nav directory switches to Inter (clean modern sans) for a sharper contrast against the wordmark.",
     BRAND_B),
    ("cC", "C", "Masthead", "Big Anton WRESTLE + wide-tracked gold LORE",
     "Magazine masthead: oversized Anton WRESTLE with a slim gold divider, and LORE as a wide-tracked gold sub-line. Airier Oswald directory with looser tracking.",
     BRAND_C),
]

def demo_block(cls, letter, name, tag, desc, brand):
    return f'''
    <section class="demo">
      <div class="demo__lbl">
        <span class="n">Concept {letter}</span><span class="t">{tag}</span>
        <span class="d"><b style="color:#fff">{name}.</b> {desc}</span>
      </div>
      <div class="frame">{bar(cls, brand)}</div>
    </section>'''

HTML = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wrestle Lore — Nav wordmark concepts</title>
<style>{CSS}</style></head>
<body>
  <div class="page">
    <div class="hd">
      <h1>Full-Bleed Nav — 3 Wordmark Concepts</h1>
      <p>Each bar is full bleed (edge-to-edge) with the belt overflowing the 62px bar. Hover the belt to trigger the sheen. Pick a letter — A, B, or C — and I'll wire it into the live nav.</p>
    </div>
    {"".join(demo_block(*d) for d in DEMOS)}
  </div>
</body></html>'''

OUT = "/root/wwe/build/nav-wordmark-concepts-v1.html"
with open(OUT, "w") as f:
    f.write(HTML)
print("wrote", OUT, os.path.getsize(OUT)//1024, "KB")
