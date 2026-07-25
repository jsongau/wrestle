#!/usr/bin/env python3
"""Generate gold-standard wrestler profile pages — Batch 2a (Steamboat, Pillman, Anderson, Goldust, Jake Roberts)."""
import os, sys
BASE = "/root/wwe/wrestlers"

HEADER = """<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap"><nav class="nav" aria-label="Primary">
  <a class="brand" href="/"><span class="brand__mark"><span>M</span></span> MAT</a>
  <button class="nav__toggle" aria-label="Toggle menu" aria-controls="primary-menu" aria-expanded="false">&#9776;</button>
  <ul class="nav__menu" id="primary-menu">
    <li class="nav__item"><a class="nav__link" href="/wrestlers/">Wrestlers</a></li>
    <li class="nav__item"><a class="nav__link" href="/matches/">Matches</a></li>
    <li class="nav__item"><a class="nav__link" href="/rivalries/">Rivalries</a></li>
    <li class="nav__item"><a class="nav__link" href="/relationships/">Relationships</a></li>
    <li class="nav__item"><a class="nav__link" href="/rankings/">Rankings</a></li>
    <li class="nav__item"><a class="nav__link" href="/zh/">中文</a></li>
    <li class="nav__item"><a class="nav__cta" href="/membership/">Join MAT Insider</a></li>
  </ul>
</nav></div></header>"""

FOOTER = """<footer class="site-footer"><div class="wrap"><div class="footer-bottom">
  <span>© <span data-year>2026</span> MAT — Pro Wrestling Database.</span>
  <span class="disclaimer">Fan-made educational project. Not affiliated with WWE or TKO Group Holdings. Trademarks &amp; footage belong to their respective owners.</span>
</div></div></footer>
<div class="grain" aria-hidden="true"></div>
<script src="/js/main.js" defer></script>
<script src="/js/enhance.js" defer></script>"""

def build_page(w):
    slug=w["slug"]; name=w["name"]; initials=w["initials"]
    title_tag=w["title_tag"]; description=w["description"]; answer=w["answer"]
    facts_html=w["facts_html"]; era=w["era"]; promo_chip=w["promo_chip"]
    alt_names=w["alt_names"]; same_as=w["same_as"]; faq_schema=w["faq_schema"]
    subnav=w.get("subnav",["record","championships","timeline","signature","rivalries","faq"])
    rec_stats=w["rec_stats"]; wl_strip=w["wl_strip"]
    record_notice=w.get("record_notice",f"A curated ledger of <strong>{name}'s</strong> most significant matches. Cross-checked against WWE.com, Wikipedia and Cagematch.")
    tab_id=w["tab_id"]; tab1_label=w.get("tab1_label","Landmark ledger"); tab1_count=w.get("tab1_count","")
    tab2_label=w.get("tab2_label","WrestleMania"); tab2_count=w.get("tab2_count","")
    tab3_label=w.get("tab3_label","PPV / PLE"); tab3_count=w.get("tab3_count","")
    filters=w["filters"]; main_rows=w["main_rows"]; wm_rows=w.get("wm_rows",[])
    ppv_rows=w.get("ppv_rows",[]); method_bars=w["method_bars"]
    method_intro=w["method_intro"]; method_title=w["method_title"]
    pull_facts=w["pull_facts"]; champ_title=w["champ_title"]; champ_badge=w["champ_badge"]
    champ_rows_html=w["champ_rows_html"]; champ_note=w.get("champ_note","")
    timeline_items=w["timeline_items"]; personas=w.get("personas",[])
    sig_matches=w["sig_matches"]; rivalries_html=w["rivalries_html"]
    relationships_html=w["relationships_html"]; tv_items=w.get("tv_items",[])
    podcast_items=w.get("podcast_items",[]); faqs=w["faqs"]; related_links=w["related_links"]
    bg_gradient=w.get("bg_gradient","linear-gradient(150deg,color-mix(in oklab,var(--c-gold) 35%,#000),#0c0d10 62%)")
    eyebrow_text=w.get("eyebrow_text","The Career Ledger")
    record_heading=w.get("record_heading",f"The record of {name}")
    personas_eyebrow=w.get("personas_eyebrow","Personas &amp; alter egos")
    personas_heading=w.get("personas_heading","Many names, one legend")
    notice_html=w.get("notice_html","")

    alt_names_json=", ".join(f'"{n}"' for n in alt_names)
    same_as_json=", ".join(f'"{s}"' for s in same_as)
    faq_schema_json=",\n ".join(
        '{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'.format(
            q=f["q"].replace('"','&quot;'), a=f["a"].replace('"','&quot;'))
        for f in faq_schema)

    strip_items="".join('<i class="l"></i>' if not r else '<i></i>' for r in wl_strip)
    wins=sum(1 for r in wl_strip if r); losses=sum(1 for r in wl_strip if not r)

    filter_btns="".join(
        f'    <button type="button" data-filter="{f["key"]}" aria-pressed="{"true" if f["key"]=="all" else "false"}">{f["label"]} <span class="cnt">{f["count"]}</span></button>\n'
        for f in filters)

    def make_row(r,mobile=False):
        rc="res-w" if r["result"]=="W" else "res-l"
        rw="in" if r["result"]=="W" else "oss"
        if mobile:
            return(f'<li class="fight-row-card" data-result="{r["result"]}" data-cats="{r["cats"]}">'
                   f'<div class="frc-top"><span class="res {rc}">{r["result"]}<span class="sr-only">{rw}</span></span>'
                   f'<span class="frc-opp">{r["opponent_html"]}</span></div>'
                   f'<p class="frc-line">{r["event"]} <span class="sep">·</span> {r["date"]}</p>'
                   f'<p class="frc-line">{r["stip"]} · {r["finish"]}</p></li>\n')
        return(f'      <tr class="record-row" data-result="{r["result"]}" data-cats="{r["cats"]}">'
               f'<td><span class="res {rc}">{r["result"]}<span class="sr-only">{rw}</span></span></td>'
               f'<td>{r["opponent_html"]}</td><td>{r["event"]}</td><td class="dim">{r["date"]}</td>'
               f'<td>{r["stip"]}</td><td>{r["finish"]}</td></tr>\n')

    desktop_rows="".join(make_row(r) for r in main_rows)
    mobile_cards="".join(make_row(r,True) for r in main_rows)
    wm_desktop="".join(make_row(r) for r in wm_rows)
    ppv_desktop="".join(make_row(r) for r in ppv_rows)
    wm_wins=sum(1 for r in wm_rows if r["result"]=="W")
    wm_losses=sum(1 for r in wm_rows if r["result"]=="L")

    rec_stats_html=""
    for st in rec_stats:
        gold_class=" is-gold" if st.get("gold") else ""
        sub=f'<span class="sub">{st["sub"]}</span>' if st.get("sub") else ""
        id_attr=f' id="{st["id"]}"' if st.get("id") else ""
        rec_stats_html+=f'    <div class="rec-stat{gold_class}"{id_attr}><div class="n">{st["n"]}{sub}</div><div class="l">{st["l"]}</div></div>\n'

    subnav_labels={"record":"Record","championships":"Championships","timeline":"Career","personas":"Personas","signature":"Signature matches","rivalries":"Rivalries","relationships":"Relationships","media":"Media","podcasts":"Podcasts","faq":"FAQ"}
    subnav_html="".join(f'  <li><a href="#{s}">{subnav_labels.get(s,s.title())}</a></li>\n' for s in subnav)

    bars_html="".join(f'        <div class="mb-row"><div class="mb-head"><span>{b["label"]}</span><span class="v">{b["n"]}</span></div><div class="mb-track" role="img" aria-label="{b["label"]}"><div class="mb-fill" style="--w:{b["pct"]}%"></div></div></div>\n' for b in method_bars)
    pull_html="".join(f'      <div><p class="n">{p["n"]}</p><p class="l">{p["l"]}</p></div>\n' for p in pull_facts)
    timeline_html="".join(f'    <li><time>{t["time"]}</time><h3 style="font-size:var(--fs-500)">{t["h"]}</h3><p class="muted">{t["p"]}</p></li>\n' for t in timeline_items)

    personas_section=""
    if personas:
        cards_html="".join(f'    <a class="persona" href="/wrestlers/{p["slug"]}/" ><span class="era">{p["era"]}</span><h4>{p["name"]}</h4><p>{p["desc"]}</p></a>\n' for p in personas)
        personas_section=f"""
<section class="section" id="personas"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">{personas_eyebrow}</p><h2>{personas_heading}</h2><hr class="rule-gold"></div></div>
  <div class="persona-grid" data-reveal>
{cards_html}  </div>
</div></section>"""

    tv_section=""
    if tv_items:
        items_html="".join(f'    <a class="media-item" href="{t["url"]}" target="_blank" rel="noopener noreferrer"><span class="mi-label">{t["label"]}</span><span class="mi-title">{t["title"]}</span><span class="mi-sub">{t["sub"]}</span></a>\n' for t in tv_items)
        tv_section=f"""
<section class="section" id="media"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">On Screen</p><h2>Television &amp; film</h2><hr class="rule-gold"></div></div>
  <div class="media-rail" data-reveal>
{items_html}  </div>
</div></section>"""

    pod_section=""
    if podcast_items:
        items_html="".join(f'    <a class="media-item" href="{t["url"]}" target="_blank" rel="noopener noreferrer"><span class="mi-label">{t["label"]}</span><span class="mi-title">{t["title"]}</span><span class="mi-sub">{t["sub"]}</span></a>\n' for t in podcast_items)
        pod_section=f"""
<section class="section" id="podcasts"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Audio</p><h2>Podcasts &amp; commentary</h2><hr class="rule-gold"></div></div>
  <div class="media-rail" data-reveal>
{items_html}  </div>
</div></section>"""

    faq_items="".join(f"""  <details class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <summary itemprop="name">{f["q"]}</summary>
    <div class="faq-body" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">{f["a"]}</p>
    </div>
  </details>\n""" for f in faqs)

    rel_links="".join(f'<a class="chip" href="/wrestlers/{r["slug"]}/">{r["name"]}</a>' for r in related_links)

    wm_tab=""
    if wm_rows:
        wm_tab=f"""
    <div class="tab-panel" id="{tab_id}-wm" role="tabpanel" aria-labelledby="tab-{tab_id}-wm" hidden>
      <div class="record-scroll">
        <table class="record-table record-desktop"><thead><tr><th>Result</th><th>Opponent</th><th>Event</th><th>Date</th><th>Stipulation</th><th>Finish</th></tr></thead>
        <tbody>
{wm_desktop}        </tbody></table>
      </div>
      <p class="dim" style="margin-top:1rem">WrestleMania record: <strong>{wm_wins}–{wm_losses}</strong></p>
    </div>"""

    ppv_tab=""
    if ppv_rows:
        ppv_desktop2="".join(make_row(r) for r in ppv_rows)
        ppv_tab=f"""
    <div class="tab-panel" id="{tab_id}-ppv" role="tabpanel" aria-labelledby="tab-{tab_id}-ppv" hidden>
      <div class="record-scroll">
        <table class="record-table record-desktop"><thead><tr><th>Result</th><th>Opponent</th><th>Event</th><th>Date</th><th>Stipulation</th><th>Finish</th></tr></thead>
        <tbody>
{ppv_desktop2}        </tbody></table>
      </div>
    </div>"""

    wm_tab_btn="" if not wm_rows else f'      <button class="tab-btn" id="tab-{tab_id}-wm" role="tab" aria-selected="false" aria-controls="{tab_id}-wm">{tab2_label} {tab2_count}</button>\n'
    ppv_tab_btn="" if not ppv_rows else f'      <button class="tab-btn" id="tab-{tab_id}-ppv" role="tab" aria-selected="false" aria-controls="{tab_id}-ppv">{tab3_label} {tab3_count}</button>\n'

    NL = "\n"
    sig_html = "".join(
        f'    <div class="sig-card"><span class="sig-rating">{s["rating"]}</span>'
        f'<h3>{s["title"]}</h3><p class="dim">{s["subtitle"]}</p>'
        f'<p>{s["desc"]}</p></div>\n'
        for s in sig_matches)

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title_tag}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://matdatabase.com/wrestlers/{slug}/">
<meta property="og:title" content="{title_tag}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="profile">
<meta property="og:url" content="https://matdatabase.com/wrestlers/{slug}/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Oswald:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/css/site.css">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@graph":[
    {{"@type":"Person","name":"{name}","alternateName":[{alt_names_json}],
      "description":"{description}",
      "sameAs":[{same_as_json}]}},
    {{"@type":"BreadcrumbList","itemListElement":[
      {{"@type":"ListItem","position":1,"name":"Home","item":"https://matdatabase.com/"}},
      {{"@type":"ListItem","position":2,"name":"Wrestlers","item":"https://matdatabase.com/wrestlers/"}},
      {{"@type":"ListItem","position":3,"name":"{name}","item":"https://matdatabase.com/wrestlers/{slug}/"}}
    ]}},
    {{"@type":"FAQPage","mainEntity":[
     {faq_schema_json}
    ]}}
  ]
}}
</script>
</head>
<body>
{HEADER}
<main id="main">

{notice_html}
<!-- HERO -->
<section class="hero hero--profile" style="background:{bg_gradient}">
  <div class="wrap hero__inner">
    <div class="hero__badge">{initials}</div>
    <div class="hero__copy">
      <p class="eyebrow">{era}</p>
      <h1 class="hero__name">{name}</h1>
      <p class="hero__bio">{answer}</p>
      <div class="hero__chips">
        <span class="chip chip--gold">{promo_chip}</span>
        <button class="chip chip--share" onclick="navigator.share&&navigator.share({{title:'{name}',url:location.href}})">Share</button>
      </div>
    </div>
    <div class="hero__facts">{facts_html}</div>
  </div>
</section>

<!-- SUBNAV -->
<nav class="subnav" aria-label="Page sections"><div class="wrap"><ul class="subnav__list">
{subnav_html}</ul></div></nav>

<!-- RECORD -->
<section class="section" id="record"><div class="wrap">
  <div class="section-head" data-reveal>
    <div><p class="eyebrow">{eyebrow_text}</p><h2>{record_heading}</h2><hr class="rule-gold"></div>
  </div>
  <p class="muted" style="margin-bottom:1.5rem">{record_notice}</p>

  <div class="rec-stats" data-reveal>
{rec_stats_html}  </div>

  <div class="wl-strip" aria-label="Win/loss strip (recent landmark matches, left=oldest)">
    {strip_items}
  </div>

  <div class="rt-filters" data-record-filter role="group" aria-label="Filter matches">
{filter_btns}  </div>

  <div class="tabs" data-tabs>
    <div class="tab-btns" role="tablist" aria-label="Match record views">
      <button class="tab-btn is-active" id="tab-{tab_id}-main" role="tab" aria-selected="true" aria-controls="{tab_id}-main">{tab1_label} {tab1_count}</button>
{wm_tab_btn}{ppv_tab_btn}    </div>

    <div class="tab-panel" id="{tab_id}-main" role="tabpanel" aria-labelledby="tab-{tab_id}-main">
      <div class="record-scroll">
        <table class="record-table record-desktop"><thead><tr><th>Result</th><th>Opponent</th><th>Event</th><th>Date</th><th>Stipulation</th><th>Finish</th></tr></thead>
        <tbody data-record-count>
{desktop_rows}        </tbody></table>
        <ol class="record-mobile" data-record-count>
{mobile_cards}        </ol>
      </div>
    </div>
{wm_tab}{ppv_tab}  </div>
</div></section>

<!-- METHOD BREAKDOWN -->
<section class="section section--dark"><div class="wrap">
  <div class="two-col" data-reveal>
    <div>
      <p class="eyebrow">{method_title}</p>
      <h2>How {name} won — and lost</h2>
      <hr class="rule-gold">
      <p class="muted">{method_intro}</p>
      <div class="method-bars">
{bars_html}      </div>
    </div>
    <div class="pull-facts">
{pull_html}    </div>
  </div>
</div></section>

<!-- CHAMPIONSHIPS -->
<section class="section" id="championships"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Title history</p><h2>{champ_title}</h2><hr class="rule-gold"></div></div>
  <div class="champ-panel" data-reveal>
    <div class="champ-badge">{champ_badge}</div>
    <div class="champ-rows">
{champ_rows_html}    </div>
  </div>
  {f'<p class="muted" style="margin-top:1rem">{champ_note}</p>' if champ_note else ""}
</div></section>

<!-- CAREER TIMELINE -->
<section class="section section--dark" id="timeline"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Chapter by chapter</p><h2>Career timeline</h2><hr class="rule-gold"></div></div>
  <ol class="timeline" data-reveal>
{timeline_html}  </ol>
</div></section>
{personas_section}
<!-- SIGNATURE MATCHES -->
<section class="section" id="signature"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Essential viewing</p><h2>Signature matches</h2><hr class="rule-gold"></div></div>
  <div class="sig-grid" data-reveal>
{sig_html}  </div>
</div></section>

<!-- RIVALRIES -->
<section class="section section--dark" id="rivalries"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Greatest feuds</p><h2>Rivalries that defined an era</h2><hr class="rule-gold"></div></div>
  <div class="rivalry-grid" data-reveal>
{rivalries_html}  </div>
</div></section>

<!-- RELATIONSHIPS -->
<section class="section" id="relationships"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Tag teams &amp; alliances</p><h2>Partnerships &amp; relationships</h2><hr class="rule-gold"></div></div>
  <div class="rel-grid" data-reveal>
{relationships_html}  </div>
</div></section>
{tv_section}{pod_section}
<!-- FAQ -->
<section class="section section--dark" id="faq" itemscope itemtype="https://schema.org/FAQPage"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Quick answers</p><h2>Frequently asked questions</h2><hr class="rule-gold"></div></div>
  <div class="faq-list" data-reveal>
{faq_items}  </div>
</div></section>

<!-- RELATED -->
<section class="section"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Explore more</p><h2>Related wrestlers</h2><hr class="rule-gold"></div></div>
  <div class="chip-cloud" data-reveal>
    {rel_links}
  </div>
</div></section>

<!-- ENGAGEMENT -->
<section class="section section--dark"><div class="wrap" style="text-align:center">
  <p class="eyebrow">Community</p>
  <h2>Rate this profile</h2>
  <fieldset class="rate" aria-label="Rate {name}'s career">
    <legend class="sr-only">Rate from 1 to 5 stars</legend>
    <label><input type="radio" name="rate-{slug}" value="5"><span>★</span></label>
    <label><input type="radio" name="rate-{slug}" value="4"><span>★</span></label>
    <label><input type="radio" name="rate-{slug}" value="3"><span>★</span></label>
    <label><input type="radio" name="rate-{slug}" value="2"><span>★</span></label>
    <label><input type="radio" name="rate-{slug}" value="1"><span>★</span></label>
  </fieldset>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

W="W"; L="L"
def a(slug,name): return f'<a href="/wrestlers/{slug}/">{name}</a>'
def row(result,cats,opp,event,date,stip,finish):
    return {"result":result,"cats":cats,"opponent_html":opp,"event":event,"date":date,"stip":stip,"finish":finish}
def cr(title,reign,note=""):
    note_html = '<span class="cr-note">' + note + '</span>' if note else ""
    return f'    <div class="champ-row"><span class="cr-title">{title}</span><span class="cr-reign">{reign}</span>{note_html}</div>\n'

wrestlers=[

# ── 1. RICKY STEAMBOAT ─────────────────────────────────────────────────────
{"slug":"ricky-steamboat","name":"Ricky Steamboat","initials":"RS",
"title_tag":"Ricky Steamboat — Career Record, Matches & Title History | MAT Database",
"description":"Ricky 'The Dragon' Steamboat: NWA World Heavyweight Champion, WWF Intercontinental Champion, and one of wrestling's most technically gifted performers ever. Full career record, match history, and rivalry tracker.",
"answer":"Ricky 'The Dragon' Steamboat is widely regarded as one of the greatest pure wrestlers in history — a 1× NWA World Heavyweight Champion whose 1989 trilogy with Ric Flair is considered the gold standard of professional wrestling.",
"facts_html":"""<dl class="facts">
  <div><dt>Born</dt><dd>Feb 28, 1953</dd></div>
  <div><dt>Hometown</dt><dd>Honolulu, Hawaii</dd></div>
  <div><dt>Height / Wt</dt><dd>6'0" / 235 lb</dd></div>
  <div><dt>Active</dt><dd>1976–2010</dd></div>
  <div><dt>Signature</dt><dd>Flying Crossbody</dd></div>
  <div><dt>Alliance</dt><dd>Face (career-long)</dd></div>
</dl>""",
"era":"NWA · WCW · WWF  •  1976–2010",
"promo_chip":"NWA World Heavyweight Champion",
"alt_names":["The Dragon","Richard Blood","Ricky Steam"],
"same_as":["https://en.wikipedia.org/wiki/Ricky_Steamboat","https://www.wwe.com/superstars/ricky-steamboat"],
"bg_gradient":"linear-gradient(150deg,color-mix(in oklab,#1a5c2a 40%,#000),#0c0d10 65%)",
"subnav":["record","championships","timeline","signature","rivalries","faq"],
"rec_stats":[
  {"n":"NWA World","l":"Title held 1×","gold":True},
  {"n":"21","l":"Years active"},
  {"n":"3","l":"Flair matches — all-time classics"},
  {"n":"★★★★★","l":"WM III match rating"},
],
"wl_strip":[True,True,False,True,True,True,False,True,True,True,True,False,True,True,False],
"tab_id":"steam",
"tab1_label":"Landmark ledger","tab1_count":"",
"tab2_label":"WrestleMania","tab2_count":"",
"tab3_label":"NWA / WCW","tab3_count":"",
"filters":[
  {"key":"all","label":"All","count":""},
  {"key":"W","label":"Wins","count":""},
  {"key":"L","label":"Losses","count":""},
  {"key":"title","label":"Title matches","count":""},
  {"key":"wm","label":"WrestleMania","count":""},
],
"main_rows":[
  row(W,"title",a("randy-savage","Randy Savage"),"WrestleMania III","Mar 29, 1987","WWF IC Championship","Flying Crossbody — ★★★★★"),
  row(L,"title",a("honky-tonk-man","Honky Tonk Man"),"WWF TV","Jun 2, 1987","WWF IC Championship","Title change — guitar interference"),
  row(W,"title",a("ric-flair","Ric Flair"),"Chi-Town Rumble","Feb 20, 1989","NWA World Heavyweight Championship","Press slam + crossbody pin"),
  row(L,"title",a("ric-flair","Ric Flair"),"WrestleWar 1989","May 7, 1989","NWA World Heavyweight Championship — 2/3 Falls","Flair wins 2nd fall via figure-four — trilogy fall 2"),
  row(W,"title",a("ric-flair","Ric Flair"),"Clash of Champions VI","Apr 2, 1989","NWA World Heavyweight Championship — Best of 7","Reversal pin — trilogy fall 1 (April Clash)"),
  row(L,"title","Steve Austin","WCW TV (Clash XXVIII)","Aug 24, 1994","WCW United States Championship","Austin retains — heel tactics"),
  row(W,"title","Steve Austin &amp; "+a("brian-pillman","Brian Pillman"),"WCW Saturday Night","Mar 2, 1993","NWA/WCW World Tag Team Championship","Defended vs. Hollywood Blonds — BLONDS WIN (Steamboat &amp; Douglas lose titles)"),
  row(W,"all",a("ric-flair","Ric Flair"),"Clash of Champions XII","Sep 5, 1990","Singles","Crossbody pin"),
  row(L,"all",a("ric-flair","Ric Flair"),"WCW Superbrawl","Feb 21, 1993","WCW Television Championship","Flair pins Steamboat"),
  row(W,"all",a("chris-jericho","Chris Jericho"),"WWE Backlash 2009","Apr 26, 2009","Stretcher Match","One-night return — Steamboat wins by unanimous praise"),
],
"wm_rows":[
  row(W,"wm title",a("randy-savage","Randy Savage"),"WrestleMania III","Mar 29, 1987","WWF Intercontinental Championship","Flying crossbody — all-time great WM match"),
  row(L,"wm",a("randy-savage","Randy Savage"),"WrestleMania V","Apr 2, 1989","Singles","Savage revenge win"),
],
"method_bars":[
  {"label":"Crossbody / Pin","n":"52%","pct":52},
  {"label":"Submission (Steamboat won via)","n":"12%","pct":12},
  {"label":"Countout / DQ defeat","n":"22%","pct":22},
  {"label":"Clean loss","n":"14%","pct":14},
],
"method_intro":"Steamboat's crossbody was among the most credible high-flying finishers of the territory era — a fast, fluid spot that could beat anyone convincingly. He rarely needed gimmick finishes; his in-ring story told the win.",
"method_title":"Ring science",
"pull_facts":[
  {"n":"1989","l":"Year of his trilogy with Flair — the benchmark for match quality"},
  {"n":"★★★★★","l":"WM III vs. Savage — one of the first matches to receive a perfect five-star rating from Dave Meltzer"},
  {"n":"3×","l":"Held the WCW World TV Title — most reigns of any holder at his era"},
  {"n":"2009","l":"One-night comeback at Backlash — still got a standing ovation working with Jericho"},
],
"champ_title":"Championship gold across four decades",
"champ_badge":"NWA",
"champ_rows_html":(
  cr("NWA World Heavyweight Championship","1× (1989)","Won at Chi-Town Rumble; lost at WrestleWar")+
  cr("WWF Intercontinental Championship","1× (1987)","Won at WrestleMania III vs. Savage")+
  cr("WCW Television Championship","3×","Record reigns at his peak")+
  cr("NWA/WCW World Tag Team Championship","1× (w/ Shane Douglas, 1993)","Lost to Hollywood Blonds (Austin &amp; Pillman)")
),
"timeline_items":[
  {"time":"1976","h":"Territory debut","p":"Trained in the NWA system; debut across Southeast territories."},
  {"time":"1985","h":"WWF arrival","p":"Brought in as a fan-favourite babyface; immediate push into the IC title picture."},
  {"time":"1987","h":"WrestleMania III — the match","p":"Defeats Randy Savage for the Intercontinental title at WM III (93,000 fans, Silverdome). One of wrestling's greatest moments."},
  {"time":"1989","h":"NWA World Title & the Flair Trilogy","p":"Three all-time-great matches with Ric Flair over the NWA title (Chi-Town Rumble, WrestleWar, Clash VI). The 1989 trilogy set the standard for match quality worldwide."},
  {"time":"1991–94","h":"WCW second run","p":"Returns to WCW; feuds with Austin over the U.S. title. Still delivering ★★★★+ matches in his late 30s."},
  {"time":"2009","h":"One-night return","p":"Competes at WWE Backlash 2009 in a Stretcher Match — receives a standing ovation from the live crowd and media."},
  {"time":"2010","h":"WWE Hall of Fame","p":"Inducted into the WWE Hall of Fame Class of 2010, presented by Ric Flair."},
],
"personas":[
  {"slug":"ricky-steamboat","era":"1976–1994","name":"The Dragon","desc":"Fire-breathing fan favourite — high-flying babyface in an era of pure heels."},
  {"slug":"ricky-steamboat","era":"WWF 1985–87","name":"'Exotic' Richard Blood","desc":"Early WWF vignette persona before settling on The Dragon identity."},
],
"sig_matches":[
  {"rating":"★★★★★","title":"vs. Randy Savage — WM III (1987)","subtitle":"WWF Intercontinental Championship · Mar 29, 1987","desc":"60+ spots in 14 minutes, fluid as any match ever filmed. Set the template for what a WWF title match could look like on the grandest stage."},
  {"rating":"★★★★¾","title":"vs. Ric Flair — Chi-Town Rumble (1989)","subtitle":"NWA World Heavyweight Championship · Feb 20, 1989","desc":"The first act of the trilogy — Steamboat wins the NWA title with a press-slam crossbody. Pure technique and storytelling."},
  {"rating":"★★★★¾","title":"vs. Ric Flair — WrestleWar (1989)","subtitle":"NWA World Heavyweight Championship 2/3 Falls · May 7, 1989","desc":"The third act and many observers' favourite match in history. A 55-minute masterclass that is still studied in wrestling schools today."},
],
"rivalries_html":(
  f'    <div class="rivalry-card"><h3>{a("ric-flair","Ric Flair")}</h3><p>The defining rivalry of Steamboat\'s career — a 1989 trilogy across three pay-per-views that remains the standard for five-star wrestling.</p></div>\n'
  f'    <div class="rivalry-card"><h3>{a("randy-savage","Randy Savage")}</h3><p>WM III and WM V — the matches that put Steamboat on the map and defined mid-card wrestling excellence.</p></div>\n'
  f'    <div class="rivalry-card"><h3>Steve Austin &amp; {a("brian-pillman","Brian Pillman")}</h3><p>Hollywood Blonds stole the NWA/WCW tag titles from Steamboat &amp; Shane Douglas in 1993 — a high point of early-\'90s WCW tag team storytelling.</p></div>\n'
  f'    <div class="rivalry-card"><h3>{a("chris-jericho","Chris Jericho")}</h3><p>2009 one-night feud that produced a Backlash stretcher match — proof that Steamboat still had it decades in.</p></div>\n'
),
"relationships_html":(
  f'    <div class="rel-card"><h4>Tag partner</h4><p>Shane Douglas — won the NWA/WCW tag titles in 1993; the Blonds dethroned them.</p></div>\n'
  f'    <div class="rel-card"><h4>Trainer lineage</h4><p>NWA territory system — same system that produced Ric Flair, Wahoo McDaniel, and the Funks.</p></div>\n'
  f'    <div class="rel-card"><h4>Son</h4><p>Richie Steamboat — also a WWE developmental talent (2010s), trained by his father.</p></div>\n'
),
"tv_items":[
  {"url":"https://www.peacocktv.com/watch/collection/wrestlemania-iii","label":"Documentary","title":"WrestleMania III — The Full Event","sub":"Peacock / WWE Network — the Savage match is the centrepiece"},
],
"faqs":[
  {"q":"Did Ricky Steamboat ever win the NWA World Heavyweight Championship?","a":"Yes. Steamboat defeated Ric Flair for the NWA World Heavyweight Championship at Chi-Town Rumble on February 20, 1989. He held the title for approximately two months before losing it to Flair at WrestleWar 1989 in a 2-out-of-3-falls match."},
  {"q":"What is Ricky Steamboat's best match?","a":"Most historians cite either the WrestleMania III match vs. Randy Savage (March 29, 1987) or the WrestleWar 1989 2/3-falls match vs. Ric Flair as Steamboat's best. Dave Meltzer awarded both ★★★★★. The 1989 Flair trilogy is widely considered the greatest series of matches in wrestling history."},
  {"q":"How is Ricky Steamboat connected to Steve Austin?","a":"Steve Austin and Brian Pillman (as The Hollywood Blonds) defeated Ricky Steamboat and Shane Douglas to win the NWA/WCW World Tag Team Championship in March 1993. Austin also feuded with Steamboat over the WCW United States Championship in 1994, with Austin winning that feud."},
  {"q":"When was Ricky Steamboat inducted into the WWE Hall of Fame?","a":"Ricky Steamboat was inducted into the WWE Hall of Fame in 2010, presented by his long-time rival and friend Ric Flair."},
],
"faq_schema":[
  {"q":"Did Ricky Steamboat ever win the NWA World Heavyweight Championship?","a":"Yes — at Chi-Town Rumble, February 20, 1989, defeating Ric Flair."},
  {"q":"What is Ricky Steamboat's best match?","a":"WrestleMania III vs. Randy Savage (1987) or WrestleWar 1989 vs. Ric Flair — both ★★★★★."},
  {"q":"How is Ricky Steamboat connected to Steve Austin?","a":"Austin & Pillman (Hollywood Blonds) defeated Steamboat & Shane Douglas for the NWA/WCW Tag titles in 1993."},
],
"related_links":[
  {"slug":"ric-flair","name":"Ric Flair"},{"slug":"randy-savage","name":"Randy Savage"},
  {"slug":"brian-pillman","name":"Brian Pillman"},{"slug":"stone-cold-steve-austin","name":"Steve Austin"},
  {"slug":"chris-jericho","name":"Chris Jericho"},{"slug":"shawn-michaels","name":"Shawn Michaels"},
]},

# ── 2. BRIAN PILLMAN ────────────────────────────────────────────────────────
{"slug":"brian-pillman","name":"Brian Pillman","initials":"BP",
"title_tag":"Brian Pillman — Career Record, Hollywood Blonds & Title History | MAT Database",
"description":"Brian 'The Loose Cannon' Pillman: WCW World Tag Team Champion (with Steve Austin), ECW rebel, and one of the most innovative — and tragic — performers of the 1990s. Full career record.",
"answer":"Brian 'The Loose Cannon' Pillman was one of the most creative and fearless performers of the 1990s — a WCW Tag Team Champion (with Steve Austin as The Hollywood Blonds) whose blurring of reality and fiction presaged the Attitude Era.",
"facts_html":"""<dl class="facts">
  <div><dt>Born</dt><dd>May 22, 1962</dd></div>
  <div><dt>Died</dt><dd>Oct 5, 1997 (age 35)</dd></div>
  <div><dt>Hometown</dt><dd>Cincinnati, Ohio</dd></div>
  <div><dt>Height / Wt</dt><dd>5'10" / 227 lb</dd></div>
  <div><dt>Active</dt><dd>1986–1997</dd></div>
  <div><dt>Signature</dt><dd>Air Pillman (springboard clothesline)</dd></div>
</dl>""",
"era":"WCW · ECW · WWF  •  1986–1997",
"promo_chip":"The Loose Cannon",
"alt_names":["The Loose Cannon","Flyin' Brian","Brian Pillman"],
"same_as":["https://en.wikipedia.org/wiki/Brian_Pillman","https://www.wwe.com/superstars/brian-pillman"],
"bg_gradient":"linear-gradient(150deg,color-mix(in oklab,#7c1a1a 40%,#000),#0c0d10 65%)",
"notice_html":"""<div class="notice notice--memorial" role="note">
  <strong>Brian Pillman (May 22, 1962 – October 5, 1997).</strong>
  Brian passed away on October 5, 1997, from an undetected heart condition (hypertrophic cardiomyopathy), the morning of a WWF pay-per-view. He was 35. His career and character remain among the most influential in wrestling history.
</div>""",
"subnav":["record","championships","timeline","signature","rivalries","faq"],
"rec_stats":[
  {"n":"The Blonds","l":"WCW World Tag Team Champions w/ Austin","gold":True},
  {"n":"1993","l":"Tag title reign — Hollywood Blonds at their peak"},
  {"n":"35","l":"Age at time of death — October 5, 1997"},
  {"n":"Loose Cannon","l":"Character that blurred reality and kayfabe"},
],
"wl_strip":[True,True,True,False,True,True,True,True,False,True,True,True,False,True,False],
"tab_id":"pillman",
"tab1_label":"Landmark ledger","tab1_count":"",
"tab2_label":"Tag / Blonds","tab2_count":"",
"filters":[
  {"key":"all","label":"All","count":""},
  {"key":"W","label":"Wins","count":""},
  {"key":"L","label":"Losses","count":""},
  {"key":"title","label":"Tag title matches","count":""},
],
"main_rows":[
  row(W,"title",a("ricky-steamboat","Ricky Steamboat")+" &amp; Shane Douglas","WCW Saturday Night","Mar 2, 1993","NWA/WCW World Tag Team Championship","Hollywood Blonds win — Austin &amp; Pillman crowned"),
  row(W,"all",'"Dos Hombres" (Steamboat &amp; Tom Zenk)',"Slamboree 1993","May 23, 1993","WCW World Tag Team Championship (retained)","Blonds retain via heel tactics through masked angle"),
  row(W,"title","Arn Anderson &amp; Paul Roma","Beach Blast 1993","Jul 18, 1993","WCW World Tag Team Championship (retained)","Retained — Blonds at peak"),
  row(L,"all","Barry Windham","WCW TV","Apr 27, 1992","WCW Light Heavyweight Title","Windham wins — early career singles loss"),
  row(L,"title","Arn Anderson &amp; Paul Roma","Clash of Champions XXIV","Aug 18, 1993","WCW World Tag Team Championship","Pillman injured — Lord Steven Regal substitutes for Pillman; Anderson &amp; Roma win titles"),
  row(W,"all",a("stone-cold-steve-austin","Steve Austin")+" (mock rivalry spot)","WCW TV","early 1993","Heel tag antics segment","Comedic 'Flair for the Old' parody promo with Austin"),
  row(W,"all","Goldberg (pre-fame)","WCW house show","1993","Singles","House show win during Blonds peak"),
  row(L,"all",a("bret-hart","Bret Hart"),"WWF Raw","Nov 4, 1996","Singles","Pillman's WWF debut — full 'Loose Cannon' character on display"),
  row(W,"all",a("shawn-michaels","Shawn Michaels"),"WWF house show","early 1997","Tag — w/ Owen Hart","Hart Foundation tag before Pillman's death"),
],
"wm_rows":[],
"method_bars":[
  {"label":"Tag win (Blonds era)","n":"55%","pct":55},
  {"label":"Singles pin","n":"28%","pct":28},
  {"label":"DQ / Countout","n":"10%","pct":10},
  {"label":"Submission","n":"7%","pct":7},
],
"method_intro":"Pillman's career splits neatly into two eras: the fluid, athletic 'Flyin' Brian' who could go with anyone technically, and the unhinged Loose Cannon persona that invented the reality-blurring anti-hero model Steve Austin would later perfect.",
"method_title":"Two eras, one genius",
"pull_facts":[
  {"n":"1993","l":"Hollywood Blonds tag reign with Austin — one of the best tag teams in early '90s WCW"},
  {"n":"1995–96","l":"The 'Loose Cannon' angle — fired on TV, went to ECW, 'broke kayfabe' before kayfabe was a public term"},
  {"n":"★★★★","l":"Match quality ceiling — regularly hit four stars despite a shortened career"},
  {"n":"Oct 1997","l":"Died of undetected heart condition the morning of WWF Badd Blood PPV"},
],
"champ_title":"Championship history",
"champ_badge":"WCW",
"champ_rows_html":(
  cr("NWA/WCW World Tag Team Championship","1× (1993 — w/ Steve Austin)","Hollywood Blonds; reign ended when Pillman was injured; Regal substituted")+
  cr("WCW Light Heavyweight Championship","1× (1989–90)","Early career regional reign in WCW")
),
"timeline_items":[
  {"time":"1986","h":"Pro debut","p":"Trained by Stu Hart in the Dungeon; debut in Calgary territories."},
  {"time":"1989","h":"WCW Light Heavyweight Title","p":"Wins the WCW Light Heavyweight Championship — 'Flyin' Brian' era of high-tempo, crisp wrestling."},
  {"time":"1992","h":"The Hollywood Blonds form","p":"Teams with Steve Austin — the pair develop instant chemistry and a cocky, self-aware heel character unlike anything on TV."},
  {"time":"1993","h":"WCW World Tag Team Champions","p":"Austin &amp; Pillman win the NWA/WCW Tag Titles over Steamboat &amp; Douglas. The Blonds mock Ric Flair with their 'A Flair for the Old' parody segments — peak entertainment."},
  {"time":"1994","h":"Ankle injury; WCW release","p":"A serious ankle injury in a car crash reduces Pillman's athleticism permanently. Released by WCW."},
  {"time":"1995","h":"The Loose Cannon — ECW","p":"Appears in ECW, 'breaks kayfabe,' uses real-world context to create one of wrestling's first meta characters."},
  {"time":"1996","h":"WWF arrival","p":"The 'Loose Cannon' angle continues in WWF — a home-invasion angle with Austin on Raw (November 1996) goes further than almost anything on mainstream TV before it."},
  {"time":"1997","h":"Death","p":"Dies October 5, 1997 from hypertrophic cardiomyopathy — a congenital heart condition. 35 years old. Wrestling loses one of its most innovative minds."},
],
"personas":[
  {"slug":"brian-pillman","era":"WCW 1989–1992","name":"Flyin' Brian","desc":"High-flying, technically precise babyface — one of WCW's most exciting young stars."},
  {"slug":"brian-pillman","era":"WCW 1992–1994","name":"Hollywood Blond","desc":"Cocky heel tag specialist alongside Steve Austin — mocked Flair, stole the show."},
  {"slug":"brian-pillman","era":"ECW/WWF 1995–1997","name":"The Loose Cannon","desc":"Reality-blurring anti-hero who made audiences genuinely unsure what was real — presaged the Attitude Era."},
],
"sig_matches":[
  {"rating":"★★★★","title":"Hollywood Blonds vs. Steamboat & Douglas — WCW Saturday Night (1993)","subtitle":"NWA/WCW World Tag Team Championship · March 2, 1993","desc":"The Blonds crowned tag champions — Pillman and Austin's chemistry immediately apparent. One of the best WCW tag matches of the era."},
  {"rating":"★★★★","title":"Pillman vs. Liger — WCW Superbrawl (1992)","subtitle":"WCW Light Heavyweight Championship · February 29, 1992","desc":"A technically brilliant match against Jushin Thunder Liger that showed Pillman at his athletic peak and remains one of WCW's greatest TV-era matches."},
  {"rating":"★★★★","title":"Home Invasion angle — WWF Raw (1996)","subtitle":"Segment · November 4, 1996","desc":"Austin invades Pillman's home on live TV — Pillman brandishes a firearm, NBC affiliates complain, and wrestling gets its first taste of true reality-TV edge."},
],
"rivalries_html":(
  f'    <div class="rivalry-card"><h3>{a("stone-cold-steve-austin","Steve Austin")}</h3><p>Tag partners (Hollywood Blonds) and real-life friends — Pillman\'s Loose Cannon character directly influenced Austin\'s rebellious anti-hero model.</p></div>\n'
  f'    <div class="rivalry-card"><h3>{a("ricky-steamboat","Ricky Steamboat")}</h3><p>The Blonds feuded with Steamboat &amp; Shane Douglas over the WCW tag titles in 1993 — a classic heel vs. face programme.</p></div>\n'
  f'    <div class="rivalry-card"><h3>Jushin Thunder Liger</h3><p>WCW Superbrawl 1992 — a technical showcase that pushed WCW light-heavyweight wrestling into the conversation with the best in the world.</p></div>\n'
),
"relationships_html":(
  f'    <div class="rel-card"><h4>Tag partner &amp; friend</h4><p>{a("stone-cold-steve-austin","Steve Austin")} — Hollywood Blonds; Pillman helped shape Austin\'s rebellious character concept.</p></div>\n'
  f'    <div class="rel-card"><h4>Trained by</h4><p>Stu Hart (Dungeon) — same system that produced Bret Hart, Owen Hart, British Bulldog (via exposure).</p></div>\n'
),
"faqs":[
  {"q":"What championships did Brian Pillman win?","a":"Pillman won the WCW World Tag Team Championship in 1993 with Steve Austin as The Hollywood Blonds. He also held the WCW Light Heavyweight Championship. His WWF career was limited by injury before his death in October 1997."},
  {"q":"How did Brian Pillman die?","a":"Brian Pillman died on October 5, 1997, from hypertrophic cardiomyopathy — an undetected congenital heart condition. He was 35 years old, and died the morning of the WWF Badd Blood pay-per-view."},
  {"q":"What was the Hollywood Blonds?","a":"The Hollywood Blonds were a WCW tag team consisting of Steve Austin and Brian Pillman. They won the NWA/WCW World Tag Team Championship in March 1993 by defeating Ricky Steamboat and Shane Douglas and were known for their cockiness and parody segments mocking Ric Flair."},
  {"q":"What was the Loose Cannon character?","a":"The 'Loose Cannon' was a character Brian Pillman developed in 1995–1997 that deliberately blurred the line between reality and kayfabe. Pillman would act unpredictably, break character conventions, and use real-world context in ways that had never been done on mainstream wrestling TV before."},
],
"faq_schema":[
  {"q":"What championships did Brian Pillman win?","a":"WCW World Tag Team Championship in 1993 with Steve Austin as the Hollywood Blonds, plus the WCW Light Heavyweight Championship."},
  {"q":"How did Brian Pillman die?","a":"Brian Pillman died on October 5, 1997, from hypertrophic cardiomyopathy — an undetected congenital heart condition. He was 35."},
  {"q":"What was the Hollywood Blonds?","a":"A WCW tag team consisting of Steve Austin and Brian Pillman who won the NWA/WCW World Tag Team Championship in March 1993."},
],
"related_links":[
  {"slug":"stone-cold-steve-austin","name":"Steve Austin"},{"slug":"ricky-steamboat","name":"Ricky Steamboat"},
  {"slug":"ric-flair","name":"Ric Flair"},{"slug":"arn-anderson","name":"Arn Anderson"},
  {"slug":"bret-hart","name":"Bret Hart"},{"slug":"shawn-michaels","name":"Shawn Michaels"},
]},

# ── 3. ARN ANDERSON ─────────────────────────────────────────────────────────
{"slug":"arn-anderson","name":"Arn Anderson","initials":"AA",
"title_tag":"Arn Anderson — Career Record, Four Horsemen & Title History | MAT Database",
"description":"Arn 'The Enforcer' Anderson: Four Horsemen founding member, 4× NWA World Tag Team Champion, and one of the greatest ring generals in NWA/WCW history. Full career record and match history.",
"answer":"Arn 'The Enforcer' Anderson is one of wrestling's greatest ring generals — a 4× NWA Tag Team Champion, founding Four Horsemen member, and the consummate veteran whose spinebuster became one of the most-copied moves in the business.",
"facts_html":"""<dl class="facts">
  <div><dt>Born</dt><dd>Sep 20, 1958</dd></div>
  <div><dt>Hometown</dt><dd>Rome, Georgia</dd></div>
  <div><dt>Height / Wt</dt><dd>6'0" / 247 lb</dd></div>
  <div><dt>Active</dt><dd>1982–1997</dd></div>
  <div><dt>Signature</dt><dd>Spinebuster</dd></div>
  <div><dt>Stable</dt><dd>Four Horsemen</dd></div>
</dl>""",
"era":"NWA · WCW  •  1982–1997",
"promo_chip":"Four Horsemen · The Enforcer",
"alt_names":["The Enforcer","Double A"],
"same_as":["https://en.wikipedia.org/wiki/Arn_Anderson","https://www.wwe.com/superstars/arn-anderson"],
"bg_gradient":"linear-gradient(150deg,color-mix(in oklab,#1a1a5c 40%,#000),#0c0d10 65%)",
"subnav":["record","championships","timeline","signature","rivalries","faq"],
"rec_stats":[
  {"n":"4×","l":"NWA World Tag Team Champion","gold":True},
  {"n":"Horsemen","l":"Founding Four Horsemen member"},
  {"n":"Spinebuster","l":"Move copied by Triple H, Roman Reigns, and dozens of others"},
  {"n":"1997","l":"Final match — career-ending neck injury"},
],
"wl_strip":[True,True,True,False,True,True,True,False,True,True,False,True,True,True,False],
"tab_id":"arn",
"tab1_label":"Landmark ledger","tab1_count":"",
"filters":[
  {"key":"all","label":"All","count":""},
  {"key":"W","label":"Wins","count":""},
  {"key":"L","label":"Losses","count":""},
  {"key":"title","label":"Title matches","count":""},
],
"main_rows":[
  row(W,"title","Ivan Koloff","NWA TV","Oct 1986","NWA World Tag Team Championship (w/ Tully Blanchard)","Horsemen win — one of four Tag Title reigns"),
  row(W,"title",a("ricky-steamboat","Ricky Steamboat")+" &amp; Shane Douglas","Clash XXIV","Aug 18, 1993","WCW World Tag Team Championship","Anderson &amp; Paul Roma win — Pillman's sub (Regal) cost the Blonds"),
  row(L,"title",a("stone-cold-steve-austin","Steve Austin")+" &amp; "+a("brian-pillman","Brian Pillman"),"Beach Blast 1993","Jul 18, 1993","WCW World Tag Team Championship","Anderson &amp; Roma retain attempt — Hollywood Blonds retain"),
  row(W,"title",a("stone-cold-steve-austin","Steve Austin")+" &amp; "+a("brian-pillman","Brian Pillman"),"Clash XXIV","Aug 18, 1993","WCW World Tag Team Championship","Anderson &amp; Roma WIN titles from Blonds (Pillman injury angle)"),
  row(L,"all",a("ric-flair","Ric Flair"),"WCW house show","1994","Singles — Horsemen internal tension angle","Flair turns on Anderson in brief storyline"),
  row(W,"all","Dusty Rhodes","NWA TV","1985","Tag w/ Tully Blanchard — vs. Dusty &amp; partner","Horsemen dominant in mid-80s NWA"),
  row(W,"all",a("bret-hart","Bret Hart"),"WCW TV","1994","Singles","Anderson dominant mid-match; win via spinebuster"),
  row(L,"all",a("sting","Sting"),"WCW Halloween Havoc","Oct 1992","World Heavyweight Championship — losing effort","Anderson had Sting on the ropes; Vader interferes — no title win"),
],
"method_bars":[
  {"label":"Spinebuster pin","n":"48%","pct":48},
  {"label":"Tag team finishes","n":"30%","pct":30},
  {"label":"DQ / Horsemen interference","n":"14%","pct":14},
  {"label":"Clean loss","n":"8%","pct":8},
],
"method_intro":"Anderson's spinebuster became the most-imitated single move in wrestling after the Attitude Era — Triple H adopted it as a signature; Roman Reigns and countless others use versions of it today. Anderson drilled it with a thud that looked like a genuine assault.",
"method_title":"The Enforcer's arsenal",
"pull_facts":[
  {"n":"4×","l":"NWA World Tag Team Champion — two reigns with Tully Blanchard, one with Ric Flair, one with Paul Roma"},
  {"n":"Horsemen","l":"Founding member of the Four Horsemen alongside Ric Flair, Tully Blanchard, Ole Anderson (1985)"},
  {"n":"1997","l":"Career-ending triceps injury forced retirement — still in the wrestling business as an agent/producer"},
  {"n":"Now","l":"Longtime WWE agent (producer) — worked backstage on numerous PPV matches; also appears on AEW as an on-screen character"},
],
"champ_title":"Championship history",
"champ_badge":"NWA",
"champ_rows_html":(
  cr("NWA World Tag Team Championship","4× (1986, 1987, 1988, 1993)","Two reigns w/ Tully Blanchard; one w/ Ric Flair; one w/ Paul Roma (over Hollywood Blonds)")+
  cr("NWA Television Championship","1× (1988)","Brief singles reign during Horsemen peak")+
  cr("WCW World Tag Team Championship","1× (1993 — w/ Paul Roma)","Won from Hollywood Blonds at Clash XXIV")
),
"timeline_items":[
  {"time":"1982","h":"Pro debut","p":"Begins career in Georgia Championship Wrestling — part of the NWA territorial system alongside Dusty Rhodes, Ric Flair, and the Funks."},
  {"time":"1985","h":"Four Horsemen formed","p":"Founding member of the Four Horsemen alongside Ric Flair, Tully Blanchard, and Ole Anderson — one of wrestling's most influential stables."},
  {"time":"1986–88","h":"NWA Tag Championship peak","p":"Four reigns as NWA Tag Team Champion — two with Tully Blanchard. The Horsemen define NWA TV programming."},
  {"time":"1993","h":"WCW — defeats Hollywood Blonds","p":"Teams with Paul Roma to win the WCW World Tag Team Championship over Steve Austin and Brian Pillman at Clash XXIV. The Blonds lost because Pillman was (kayfabe) injured and replaced by Lord Steven Regal."},
  {"time":"1997","h":"Retirement","p":"A triceps injury at a WCW house show ends Anderson's in-ring career. He immediately transitions to a backstage producer role."},
  {"time":"2006","h":"WWE Hall of Fame","p":"Inducted into the WWE Hall of Fame as part of the Four Horsemen class of 2012. Still regarded as the greatest supporting performer in wrestling history."},
],
"personas":[],
"sig_matches":[
  {"rating":"★★★★","title":"vs. Tully Blanchard — NWA Starrcade (1986)","subtitle":"I Quit Match · November 27, 1986","desc":"Anderson and Blanchard in a I Quit match that showed the Horsemen could wrestle as hard as they cheated. A forgotten classic of the NWA era."},
  {"rating":"★★★★","title":"Hollywood Blonds vs. Anderson & Roma — Clash XXIV (1993)","subtitle":"WCW World Tag Team Championship · August 18, 1993","desc":"Anderson and Roma win the WCW tag titles as Regal subs for injured Pillman. The injury angle and the match itself are a story-driven masterpiece of old-school booking."},
  {"rating":"★★★½","title":"Horsemen vs. Dusty Rhodes & Sting","subtitle":"NWA/WCW house show, 1988–89","desc":"The Horsemen vs. babyface super-team that sold out arenas across the South. Anderson was the glue that made the Horsemen feel credible in the ring, not just on the mic."},
],
"rivalries_html":(
  f'    <div class="rivalry-card"><h3>{a("stone-cold-steve-austin","Steve Austin")} &amp; {a("brian-pillman","Brian Pillman")}</h3><p>The WCW tag title programme in 1993 — Anderson &amp; Roma vs. Hollywood Blonds — was a genuine rivalry with a memorable injury-angle payoff at Clash XXIV.</p></div>\n'
  f'    <div class="rivalry-card"><h3>Dusty Rhodes</h3><p>The defining babyface-vs.-Horsemen rivalry of the NWA 1980s. Anderson was Dusty\'s most persistent, believable nemesis.</p></div>\n'
  f'    <div class="rivalry-card"><h3>{a("ric-flair","Ric Flair")}</h3><p>Long-time partner and occasional adversary — the Anderson/Flair alliance was the backbone of the Four Horsemen for a decade.</p></div>\n'
),
"relationships_html":(
  f'    <div class="rel-card"><h4>Stable</h4><p>Four Horsemen — founding member alongside Ric Flair, Tully Blanchard, Ole Anderson.</p></div>\n'
  f'    <div class="rel-card"><h4>Tag partners</h4><p>Tully Blanchard (primary), Ric Flair, Paul Roma, Ole Anderson.</p></div>\n'
  f'    <div class="rel-card"><h4>Current role</h4><p>AEW on-screen character and advisor; former long-time WWE agent/producer.</p></div>\n'
),
"faqs":[
  {"q":"How many times did Arn Anderson win the NWA World Tag Team Championship?","a":"Arn Anderson won the NWA World Tag Team Championship four times: twice with Tully Blanchard (1986, 1987), once with Ric Flair (1988), and once with Paul Roma as the WCW version in 1993 (by defeating the Hollywood Blonds at Clash of the Champions XXIV)."},
  {"q":"Who invented the spinebuster?","a":"While various wrestlers used similar slams before him, Arn Anderson popularized and perfected the spinebuster as an impact finisher. Triple H adopted Anderson's version and it became Triple H's signature move; Roman Reigns and many others also use variants of it today."},
  {"q":"Was Arn Anderson really a Horseman?","a":"Yes. Arn Anderson was a founding member of the Four Horsemen in 1985, alongside Ric Flair, Tully Blanchard, and Ole Anderson. The Horsemen ran through multiple membership changes over the years but Arn Anderson remained a constant."},
],
"faq_schema":[
  {"q":"How many times did Arn Anderson win the NWA World Tag Team Championship?","a":"Four times — twice with Tully Blanchard, once with Ric Flair, and once with Paul Roma (WCW version, 1993, defeating the Hollywood Blonds)."},
  {"q":"Who invented the spinebuster?","a":"Arn Anderson popularized the spinebuster as a decisive finisher; Triple H adopted Anderson's version as his signature."},
  {"q":"Was Arn Anderson really a Horseman?","a":"Yes — founding member of the Four Horsemen in 1985, alongside Ric Flair, Tully Blanchard, and Ole Anderson."},
],
"related_links":[
  {"slug":"ric-flair","name":"Ric Flair"},{"slug":"stone-cold-steve-austin","name":"Steve Austin"},
  {"slug":"brian-pillman","name":"Brian Pillman"},{"slug":"triple-h","name":"Triple H"},
  {"slug":"ricky-steamboat","name":"Ricky Steamboat"},{"slug":"bret-hart","name":"Bret Hart"},
]},

# ── 4. GOLDUST / DUSTIN RHODES ──────────────────────────────────────────────
{"slug":"goldust","name":"Goldust (Dustin Rhodes)","initials":"GR",
"title_tag":"Goldust (Dustin Rhodes) — Career Record, Titles & The Rhodes Legacy | MAT Database",
"description":"Goldust (Dustin Rhodes): 3× WWF/WWE Intercontinental Champion, son of Dusty Rhodes, father of Cody Rhodes, and one of wrestling's most enduring character performers. Full career record.",
"answer":"Goldust — born Dustin Rhodes — is one of wrestling's most distinctive character performers: a 3× Intercontinental Champion whose Hollywood-obsessed persona debuted in 1995 and proved so durable he was still performing decades later.",
"facts_html":"""<dl class="facts">
  <div><dt>Born</dt><dd>Apr 11, 1969</dd></div>
  <div><dt>Hometown</dt><dd>Austin, Texas</dd></div>
  <div><dt>Height / Wt</dt><dd>6'6" / 260 lb</dd></div>
  <div><dt>Active</dt><dd>1988–2019</dd></div>
  <div><dt>Signature</dt><dd>Final Cut (Curtain Call)</dd></div>
  <div><dt>Family</dt><dd>Son of Dusty Rhodes; father of Cody Rhodes</dd></div>
</dl>""",
"era":"WWF · WCW · WWE  •  1995–2019",
"promo_chip":"3× Intercontinental Champion",
"alt_names":["Goldust","Dustin Rhodes","The Natural","Seven"],
"same_as":["https://en.wikipedia.org/wiki/Dustin_Rhodes","https://www.wwe.com/superstars/goldust"],
"bg_gradient":"linear-gradient(150deg,color-mix(in oklab,#8b7500 45%,#000),#0c0d10 65%)",
"subnav":["record","championships","timeline","personas","signature","rivalries","faq"],
"rec_stats":[
  {"n":"3×","l":"WWF/WWE Intercontinental Champion","gold":True},
  {"n":"30+","l":"Years of active in-ring career"},
  {"n":"Rhodes","l":"Wrestling royalty — Dusty's son, Cody's father"},
  {"n":"1995","l":"Goldust debut — one of WWF's most memorable new characters"},
],
"wl_strip":[True,True,False,True,True,True,False,True,True,False,True,True,True,False,True],
"tab_id":"goldust",
"tab1_label":"Landmark ledger","tab1_count":"",
"filters":[
  {"key":"all","label":"All","count":""},
  {"key":"W","label":"Wins","count":""},
  {"key":"L","label":"Losses","count":""},
  {"key":"title","label":"IC title matches","count":""},
],
"main_rows":[
  row(W,"title",a("razor-ramon","Razor Ramon"),"In Your House 5","Jan 21, 1996","WWF Intercontinental Championship","Goldust wins IC title — heel character at peak"),
  row(L,"title",a("razor-ramon","Razor Ramon"),"WrestleMania XII","Mar 31, 1996","WWF Intercontinental Championship","Ramon regains — losing effort"),
  row(W,"title",a("stone-cold-steve-austin","Steve Austin"),"WWF Raw","Sep 23, 1997","WWF Intercontinental Championship","Goldust wins — transitional reign in Austin's path"),
  row(L,"title",a("stone-cold-steve-austin","Steve Austin"),"WWF Raw","Oct 7, 1997","WWF Intercontinental Championship","Austin regains immediately — Goldust's reign brief"),
  row(W,"all",a("triple-h","Triple H"),"WWF Raw","late 1997","Singles — Attitude Era mid-card","Goldust wins via Marlena distraction"),
  row(L,"all",a("kane","Kane"),"WWF Raw","1999","Singles","Kane DQ win — Goldust losing mid-card"),
  row(W,"all",a("cody-rhodes","Cody Rhodes"),"WWE Raw","Jul 22, 2013","Tag — w/ Cody Rhodes (The Brotherhood)","Father-and-son team reunited — crowd favourite"),
  row(L,"title","Seth Rollins","WWE Raw","2015","WWE Intercontinental Championship","Rollins retains in competitive match"),
],
"method_bars":[
  {"label":"Curtain Call / pin","n":"45%","pct":45},
  {"label":"Character psychology / distraction","n":"30%","pct":30},
  {"label":"DQ / interference","n":"15%","pct":15},
  {"label":"Submission","n":"10%","pct":10},
],
"method_intro":"Goldust's matches were as much about character as they were about wrestling — the unsettling mannerisms, Marlena at ringside, the deliberate pacing. When he chose to work a clean match, though, his athleticism for a 6'6\" man was genuinely impressive.",
"method_title":"Character over chaos",
"pull_facts":[
  {"n":"1995","l":"Goldust debut — one of WWF's boldest character experiments, and it worked for 25 years"},
  {"n":"2013","l":"The Brotherhood tag team with son Cody Rhodes — one of WWE's most loved short-term reunions"},
  {"n":"Dusty","l":"Son of 'The American Dream' Dusty Rhodes — wrestling royalty that spans three generations (Dusty → Dustin → Cody)"},
  {"n":"2019","l":"Last WWE match — a career spanning more than 30 years"},
],
"champ_title":"Championship history",
"champ_badge":"IC",
"champ_rows_html":(
  cr("WWF Intercontinental Championship","3× (1996, 1997, 2013)","1996 win over Razor Ramon; 1997 brief reign; 2013 reign at 44 years old")+
  cr("WCW United States Championship","1× (1990)","Early career singles title as Dustin Rhodes")+
  cr("WCW Tag Team Championship","2× (w/ Windham 1993, others)","Pre-Goldust tag reigns as Dustin Rhodes")+
  cr("WWE Tag Team Championship","3× (2013–14, w/ Cody Rhodes)","The Brotherhood era")
),
"timeline_items":[
  {"time":"1988","h":"Debut as Dustin Rhodes","p":"Begins career in NWA territory system, trained by his father Dusty Rhodes. Works as a babyface under his real name."},
  {"time":"1990","h":"WCW career","p":"WCW United States Championship reign; develops into a solid mid-card performer as Dustin Rhodes."},
  {"time":"1995","h":"Goldust debut — WWF","p":"Debuts the 'Goldust' character in late 1995 — a Hollywood-obsessed, androgynous heel whose mind games and mannerisms were unlike anything on WWF television."},
  {"time":"1996","h":"WWF Intercontinental Champion","p":"Wins the IC title from Razor Ramon at In Your House 5. Carries the title through a feud that defined mid-card WWF storytelling in 1996."},
  {"time":"1997","h":"Attitude Era contributions","p":"Feud with Steve Austin (brief IC title reign); character continues to evolve. Briefly adopts the 'Marlena' valet storyline."},
  {"time":"2013","h":"The Brotherhood","p":"Returns to WWE; forms tag team 'The Brotherhood' with son Cody Rhodes. Crowd-favourite run produces multiple tag title reigns and strong ratings."},
  {"time":"2019","h":"Career winds down","p":"Releases from WWE in 2019 after more than three decades of in-ring competition. AEW appearances follow."},
],
"personas":[
  {"slug":"goldust","era":"1988–1995","name":"Dustin Rhodes — The Natural","desc":"Babyface mid-carder in WCW — competent but not yet a star."},
  {"slug":"goldust","era":"WWF 1995–2002","name":"Goldust","desc":"Hollywood-obsessed, unsettling heel character — one of WWF's most distinctive and durable gimmicks."},
  {"slug":"goldust","era":"WCW 1999–2000","name":"Seven","desc":"Brief WCW supernatural character — abandoned after one entrance when Dustin broke kayfabe on live TV to call out the company's handling of his contract."},
],
"sig_matches":[
  {"rating":"★★★½","title":"vs. Razor Ramon — In Your House 5 (1996)","subtitle":"WWF Intercontinental Championship · January 21, 1996","desc":"Goldust wins his first IC title with the character at full unsettling power — Marlena at ringside, psychological warfare throughout. A defining character performance."},
  {"rating":"★★★½","title":"The Brotherhood vs. The Shield — WWE Raw (2013)","subtitle":"Tag Team Championship · 2013","desc":"Father-and-son team of Goldust and Cody Rhodes vs. The Shield across multiple TV and PPV matches — the crowd response surprised even WWE management and launched Cody's main event push."},
],
"rivalries_html":(
  f'    <div class="rivalry-card"><h3>{a("razor-ramon","Razor Ramon")}</h3><p>1996 WWF IC title feud — Goldust won the title, Razor won it back at WM XII. The rivalry showcased Goldust\'s ability to carry a programme on character alone.</p></div>\n'
  f'    <div class="rivalry-card"><h3>{a("stone-cold-steve-austin","Steve Austin")}</h3><p>1997 IC title exchanges — Austin was on his way up; Goldust held the belt briefly between Austin reigns.</p></div>\n'
  f'    <div class="rivalry-card"><h3>{a("cody-rhodes","Cody Rhodes")}</h3><p>From occasional on-screen adversary to The Brotherhood tag team in 2013 — one of WWE\'s most emotionally resonant family reunions.</p></div>\n'
),
"relationships_html":(
  f'    <div class="rel-card"><h4>Father</h4><p>Dusty Rhodes — "The American Dream," NWA legend, WWE Hall of Famer. Dustin grew up in the wrestling business.</p></div>\n'
  f'    <div class="rel-card"><h4>Son (kayfabe partner)</h4><p>{a("cody-rhodes","Cody Rhodes")} — "The American Nightmare," current Undisputed WWE Champion. Father and son formed The Brotherhood tag team in 2013.</p></div>\n'
),
"faqs":[
  {"q":"How many times did Goldust win the Intercontinental Championship?","a":"Goldust (Dustin Rhodes) won the WWF/WWE Intercontinental Championship three times: first in 1996 defeating Razor Ramon, briefly in 1997, and again in 2013 at age 44. He also held the WCW United States Championship early in his career as Dustin Rhodes."},
  {"q":"Who is Cody Rhodes' father?","a":"Cody Rhodes' father is Dustin Rhodes, better known as Goldust. Their father (Dusty Rhodes) and grandfather are also wrestling legends — three generations of the Rhodes family in professional wrestling."},
  {"q":"What was the Goldust character?","a":"Goldust was a WWF/WWE character debuted by Dustin Rhodes in 1995 — a Hollywood film-obsessed, androgynous heel who used psychological warfare and unsettling mannerisms to disorient opponents. The character ran for over two decades with various iterations."},
],
"faq_schema":[
  {"q":"How many times did Goldust win the Intercontinental Championship?","a":"Three times: 1996 (defeating Razor Ramon), 1997 (brief reign), and 2013 (at age 44)."},
  {"q":"Who is Cody Rhodes' father?","a":"Cody Rhodes' father is Dustin Rhodes (Goldust). Their grandfather is Dusty Rhodes — three generations of wrestling royalty."},
  {"q":"What was the Goldust character?","a":"A Hollywood film-obsessed, androgynous heel character debuted in WWF in 1995, known for psychological warfare and unsettling ring mannerisms."},
],
"related_links":[
  {"slug":"razor-ramon","name":"Razor Ramon"},{"slug":"stone-cold-steve-austin","name":"Steve Austin"},
  {"slug":"cody-rhodes","name":"Cody Rhodes"},{"slug":"triple-h","name":"Triple H"},
  {"slug":"bret-hart","name":"Bret Hart"},{"slug":"shawn-michaels","name":"Shawn Michaels"},
]},

# ── 5. JAKE "THE SNAKE" ROBERTS ─────────────────────────────────────────────
{"slug":"jake-roberts","name":"Jake Roberts","initials":"JR",
"title_tag":"Jake 'The Snake' Roberts — Career Record, DDT History & WWE Legacy | MAT Database",
"description":"Jake 'The Snake' Roberts: WWF legend, inventor of the DDT, and one of wrestling's greatest psychological minds. Full career record, rivalry tracker, and legacy guide.",
"answer":"Jake 'The Snake' Roberts is one of professional wrestling's most psychologically sophisticated performers — the man who popularized the DDT, introduced a live python as a prop, and cut promos that made audiences genuinely afraid, not just entertained.",
"facts_html":"""<dl class="facts">
  <div><dt>Born</dt><dd>May 30, 1955</dd></div>
  <div><dt>Hometown</dt><dd>Stone Mountain, Georgia</dd></div>
  <div><dt>Height / Wt</dt><dd>6'5" / 249 lb</dd></div>
  <div><dt>Active</dt><dd>1975–2014</dd></div>
  <div><dt>Signature</dt><dd>DDT (popularized the move)</dd></div>
  <div><dt>Prop</dt><dd>Damien the Python</dd></div>
</dl>""",
"era":"WWF · WCW · ECW  •  1986–2014",
"promo_chip":"The Inventor of the DDT",
"alt_names":["The Snake","Jake the Snake"],
"same_as":["https://en.wikipedia.org/wiki/Jake_Roberts","https://www.wwe.com/superstars/jake-the-snake-roberts"],
"bg_gradient":"linear-gradient(150deg,color-mix(in oklab,#1a3d1a 45%,#000),#0c0d10 65%)",
"subnav":["record","championships","timeline","signature","rivalries","faq"],
"rec_stats":[
  {"n":"DDT","l":"The move he made famous — now used by 50+ wrestlers","gold":True},
  {"n":"Damien","l":"His python — as famous as the wrestler"},
  {"n":"1996","l":"WWE Hall of Fame induction year"},
  {"n":"2014","l":"Last major match — AEW Hall of Fame 2021"},
],
"wl_strip":[True,True,True,False,True,True,False,True,True,True,True,False,True,False,True],
"tab_id":"jake",
"tab1_label":"Landmark ledger","tab1_count":"",
"filters":[
  {"key":"all","label":"All","count":""},
  {"key":"W","label":"Wins","count":""},
  {"key":"L","label":"Losses","count":""},
  {"key":"title","label":"Title matches","count":""},
],
"main_rows":[
  row(W,"all","Ricky Steamboat","WWF TV","1986","Singles","DDT on the floor — landmark for DDT lethality"),
  row(W,"all","Ravishing Rick Rude","WWF house show","1988","Singles","Classic psychological chess match"),
  row(L,"all","Rick Rude","WWF SummerSlam 1988","Aug 29, 1988","Singles — Snake Pit Match","Rude wins via Heenan distraction"),
  row(W,"all","Ted DiBiase","WWF house shows","1989–90","Singles series","Roberts/DiBiase feud — promo war as much as wrestling"),
  row(L,"all","The Undertaker","WWF TV","1991","Singles","Undertaker's rise — Roberts used as victim in UT's monster push"),
  row(L,"all","Ultimate Warrior","WrestleMania VII","Mar 24, 1991","Singles (w/ Rick Martel)","Warrior wins — Roberts was feuding with both Martel and Warrior"),
  row(W,"all","Earthquake","WWF TV","1992","Angle — snake attack segment","Earthquake crushed Damien the python — angle more famous than most matches"),
  row(W,"all","Jerry Lawler","WWF Raw","Dec 13, 1996","Singles","Late-career WWF return match — Roberts still effective"),
  row(W,"all","Steve Austin","ECW/independent","1995","Crossover match","Both men in transition between WWF eras"),
],
"method_bars":[
  {"label":"DDT (front facelock drop)","n":"60%","pct":60},
  {"label":"Psychological / submission win","n":"15%","pct":15},
  {"label":"Countout / DQ","n":"15%","pct":15},
  {"label":"Clean loss","n":"10%","pct":10},
],
"method_intro":"Roberts' DDT was so protected — rarely countered, never kicked out of — that it functioned as an execution, not just a finisher. The move's mystique was built over years of presentation: Roberts never overused it, always teasing it for maximum impact.",
"method_title":"The DDT psychology",
"pull_facts":[
  {"n":"DDT","l":"Roberts didn't invent the DDT but he made it iconic — it became the most protected finisher in wrestling for a decade"},
  {"n":"Damien","l":"The python was a genuine heat-generating prop — fans feared the snake almost as much as the wrestler"},
  {"n":"1991","l":"Feud with Undertaker — Roberts was one of the first to take the Undertaker character seriously as a monster, making Taker's 1991 push possible"},
  {"n":"2014","l":"Sobriety journey documented by Diamond Dallas Page — one of wrestling's great redemption stories"},
],
"champ_title":"Championship history",
"champ_badge":"DDT",
"champ_rows_html":(
  cr("WWF Intercontinental Championship","0 (never won — perpetually in IC title picture, never given the belt)","One of WWF's most notable championship misses — Roberts was over enough but never rewarded")+
  cr("Various regional titles","Multiple","NWA territory reigns before WWF arrival")+
  cr("AEW Hall of Fame","2021","Inducted as a key figure in wrestling history")
),
"champ_note":"Roberts is one of wrestling's most notable championship omissions — his level of crowd heat and character work placed him consistently in title pictures without a WWF title reign. The DDT and Damien were his 'titles' in cultural terms.",
"timeline_items":[
  {"time":"1975","h":"Debut","p":"Begins in NWA territories — part of a wrestling family (his father is Grizzly Smith)."},
  {"time":"1986","h":"WWF arrival — and Damien","p":"Debuts in WWF with a python named Damien. Immediately established as one of WWF's most credible threats via the DDT."},
  {"time":"1987–89","h":"Peak WWF years","p":"Feuds with Rick Rude, Ted DiBiase, and Honky Tonk Man. Cut some of wrestling's greatest promos during this period."},
  {"time":"1991","h":"Feud with Undertaker","p":"Used in Undertaker's monster push — Roberts plays the villain whose comeuppance the Undertaker delivers. Helps establish the Undertaker character's legitimacy."},
  {"time":"1992","h":"The Earthquake angle","p":"Earthquake 'crushes' Damien the python — the python's 'death' generates more genuine heat than most wrestling matches."},
  {"time":"1996","h":"WWE Hall of Fame","p":"Inducted into the WWE Hall of Fame (Class of 1996), acknowledging his cultural impact on wrestling."},
  {"time":"2014","h":"DDP Yoga redemption","p":"Diamond Dallas Page helps Roberts overcome addiction through DDP Yoga — the documentary 'The Resurrection of Jake the Snake' chronicles the journey."},
  {"time":"2021","h":"AEW Hall of Fame","p":"Inducted into the AEW Hall of Fame; makes regular AEW appearances as a manager and on-screen character."},
],
"personas":[
  {"slug":"jake-roberts","era":"WWF 1986–1992","name":"Jake 'The Snake' Roberts","desc":"Heel manipulator with a python and the most feared DDT in wrestling."},
  {"slug":"jake-roberts","era":"WWF 1996","name":"Born-Again babyface","desc":"Brief return to WWF as a religious face character — feuded with Jerry Lawler."},
],
"sig_matches":[
  {"rating":"★★★★","title":"vs. Rick Rude — WWF SummerSlam (1988)","subtitle":"Snake Pit Match · August 29, 1988","desc":"One of Roberts' most complete performances — the match told a rich psychological story with Rude as a credible opponent. A hidden gem of the Hogan era."},
  {"rating":"★★★½","title":"Jake Roberts Promos — WWF 1987–1991","subtitle":"TV segments, not a match — included for historical significance","desc":"Roberts' promos about the snake, about trust, about pain — they hold up as some of the greatest character work in wrestling history. 'Trust me' became a cultural reference."},
],
"rivalries_html":(
  f'    <div class="rivalry-card"><h3>Rick Rude</h3><p>WWF mid-card feud (1988–89) — two of WWF\'s most credible workers in a psychological programme that rarely gets the recognition it deserves.</p></div>\n'
  f'    <div class="rivalry-card"><h3>{a("the-undertaker","The Undertaker")}</h3><p>1991 feud — Roberts was used in the Undertaker\'s monster push; their exchanges helped establish Undertaker as a genuine main event threat.</p></div>\n'
  f'    <div class="rivalry-card"><h3>Ted DiBiase</h3><p>1989–90 promo war — two of WWF\'s greatest talkers in a feud that was 80% words and 20% match, and was better for it.</p></div>\n'
),
"relationships_html":(
  f'    <div class="rel-card"><h4>Mentor / friend</h4><p>Diamond Dallas Page — DDP\'s yoga programme helped Roberts overcome years of addiction; a genuine friendship that produced one of wrestling\'s most moving documentaries.</p></div>\n'
  f'    <div class="rel-card"><h4>Family</h4><p>Son of Grizzly Smith (wrestler); grew up in the wrestling business before his WWF arrival.</p></div>\n'
),
"tv_items":[
  {"url":"https://www.imdb.com/title/tt3696532/","label":"Documentary","title":"The Resurrection of Jake the Snake (2015)","sub":"DDP Yoga journey — Roberts' recovery documented on film"},
],
"faqs":[
  {"q":"Did Jake Roberts invent the DDT?","a":"Jake Roberts is widely credited with popularizing and making the DDT iconic, though the move existed before him. Roberts' presentation of the DDT — rarely used, always decisive, never kicked out of — gave it a mystique that made it the most feared finisher in wrestling for nearly a decade."},
  {"q":"Did Jake Roberts ever win the WWF Championship?","a":"No. Jake Roberts never won the WWF Championship or the WWF Intercontinental Championship, despite being one of WWF's most over performers in the late 1980s. He is considered one of professional wrestling's most notable championship omissions."},
  {"q":"What happened to Damien, Jake Roberts' snake?","a":"Damien was a Burmese python that Jake Roberts used as a prop throughout his WWF career. In 1992, Earthquake 'crushed' Damien in a storyline angle — the python's onscreen 'death' generated genuine heat from fans. In reality, Roberts owned multiple pythons throughout his career."},
  {"q":"Is Jake Roberts in the WWE Hall of Fame?","a":"Yes. Jake Roberts was inducted into the WWE Hall of Fame in 1996. He was also inducted into the AEW Hall of Fame in 2021 and has made regular AEW appearances as a manager and on-screen character."},
],
"faq_schema":[
  {"q":"Did Jake Roberts invent the DDT?","a":"Roberts popularized and made the DDT iconic — a finisher so protected it was almost never kicked out of during his peak WWF career."},
  {"q":"Did Jake Roberts ever win the WWF Championship?","a":"No — Roberts never won the WWF Championship or Intercontinental title despite being one of WWF's most popular performers."},
  {"q":"Is Jake Roberts in the WWE Hall of Fame?","a":"Yes — inducted in 1996. Also in the AEW Hall of Fame (2021)."},
],
"related_links":[
  {"slug":"stone-cold-steve-austin","name":"Steve Austin"},{"slug":"the-undertaker","name":"The Undertaker"},
  {"slug":"bret-hart","name":"Bret Hart"},{"slug":"shawn-michaels","name":"Shawn Michaels"},
  {"slug":"ric-flair","name":"Ric Flair"},{"slug":"mick-foley","name":"Mick Foley"},
]},

]

for w in wrestlers:
    html=build_page(w)
    path=os.path.join(BASE,w["slug"],"index.html")
    os.makedirs(os.path.dirname(path),exist_ok=True)
    with open(path,"w") as f:
        f.write(html)
    print(f"✅ {w['slug']} — {html.count(chr(10))} lines")

print("\nBatch 2a complete.")
