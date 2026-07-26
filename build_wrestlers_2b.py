#!/usr/bin/env python3
"""Generate gold-standard wrestler profile pages — Batch 2b (Razor Ramon, Vince McMahon, Chris Benoit, Edge, Booker T)."""
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
      <p class="dim" style="margin-top:1rem">WrestleMania record: <strong>{wm_wins}-{wm_losses}</strong></p>
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

    sig_html="".join(
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

  <section class="wl-strip-wrap" aria-label="Win/loss sparkline">
  <div class="wl-strip">
    {strip_items}
  </div>
  </section>

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
  <fieldset class="rate" aria-label="Rate this career">
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
    note_html='<span class="cr-note">'+note+'</span>' if note else ""
    return f'    <div class="champ-row"><span class="cr-title">{title}</span><span class="cr-reign">{reign}</span>{note_html}</div>\n'

wrestlers=[

# ── 1. RAZOR RAMON / SCOTT HALL ─────────────────────────────────────────────
{"slug":"razor-ramon","name":"Razor Ramon (Scott Hall)","initials":"RR",
"title_tag":"Razor Ramon (Scott Hall) — Career Record, Ladder Match & Title History | MAT Database",
"description":"Razor Ramon (Scott Hall): 4× WWF Intercontinental Champion, nWo founding member, and one of the most naturally charismatic performers in wrestling history. Full career record and ladder match legacy.",
"answer":"Razor Ramon — the character that made Scott Hall famous — was the WWF's slickest bad guy: a 4× Intercontinental Champion whose two ladder matches against Shawn Michaels at WrestleMania X and XI changed what wrestling matches could look like.",
"facts_html":"""<dl class="facts">
  <div><dt>Born</dt><dd>Oct 20, 1958</dd></div>
  <div><dt>Died</dt><dd>Mar 14, 2022 (age 63)</dd></div>
  <div><dt>Hometown</dt><dd>Miami, Florida</dd></div>
  <div><dt>Height / Wt</dt><dd>6'7" / 287 lb</dd></div>
  <div><dt>Active</dt><dd>1984–2016</dd></div>
  <div><dt>Signature</dt><dd>Razor's Edge</dd></div>
</dl>""",
"era":"WWF · WCW/nWo · TNA  •  1992–2016",
"promo_chip":"4× WWF Intercontinental Champion",
"alt_names":["The Bad Guy","Scott Hall","Razor Ramon","Big Scott Hall"],
"same_as":["https://en.wikipedia.org/wiki/Scott_Hall","https://www.wwe.com/superstars/razor-ramon"],
"bg_gradient":"linear-gradient(150deg,color-mix(in oklab,#5c1a1a 45%,#000),#0c0d10 65%)",
"notice_html":"""<div class="notice notice--memorial" role="note">
  <strong>Scott Hall (October 20, 1958 – March 14, 2022).</strong>
  Scott Hall passed away on March 14, 2022, following complications from hip replacement surgery. He was 63. Hall's natural charisma and the Razor Ramon character remain among the most beloved in wrestling history.
</div>""",
"subnav":["record","championships","timeline","personas","signature","rivalries","faq"],
"rec_stats":[
  {"n":"4×","l":"WWF Intercontinental Champion — record at the time","gold":True},
  {"n":"nWo","l":"Founding member — changed wrestling's landscape in 1996"},
  {"n":"WM X","l":"Ladder match vs. HBK — redefined modern match presentation"},
  {"n":"2014","l":"WWE Hall of Fame induction"},
],
"wl_strip":[True,True,True,True,False,True,True,True,False,True,True,False,True,True,False],
"tab_id":"razor",
"tab1_label":"Landmark ledger","tab1_count":"",
"tab2_label":"WrestleMania","tab2_count":"",
"filters":[
  {"key":"all","label":"All","count":""},
  {"key":"W","label":"Wins","count":""},
  {"key":"L","label":"Losses","count":""},
  {"key":"title","label":"IC title matches","count":""},
  {"key":"wm","label":"WrestleMania","count":""},
],
"main_rows":[
  row(W,"title","Marty Jannetty","WWF Raw","May 17, 1993","WWF Intercontinental Championship","Razor's Edge — first IC title win"),
  row(W,"wm title",a("shawn-michaels","Shawn Michaels"),"WrestleMania X","Mar 20, 1994","WWF Intercontinental Championship — Ladder Match","Hall retrieves belt — all-time classic ladder match (1st)"),
  row(L,"title",a("shawn-michaels","Shawn Michaels"),"WrestleMania XI","Apr 2, 1995","WWF Intercontinental Championship — Ladder Match","HBK wins — ladder match sequel"),
  row(W,"title",a("goldust","Goldust"),"WWF Raw","Jan 22, 1996","WWF Intercontinental Championship","Razor wins title back — 4th IC reign"),
  row(L,"all",a("goldust","Goldust"),"In Your House 5","Jan 21, 1996","WWF Intercontinental Championship","Goldust wins — transitional loss"),
  row(W,"all",a("shawn-michaels","Shawn Michaels"),"WWF Raw","1993","Singles","Early WWF win over HBK during IC title build"),
  row(W,"all",a("the-undertaker","The Undertaker"),"WWF Royal Rumble","Jan 22, 1994","Royal Rumble match — eliminated Taker","Hall eliminates Undertaker in the Rumble"),
  row(L,"all",a("stone-cold-steve-austin","Steve Austin"),"WWF house show","1996","Singles","Austin on his way up — Hall losing mid-card"),
],
"wm_rows":[
  row(W,"wm title",a("shawn-michaels","Shawn Michaels"),"WrestleMania X","Mar 20, 1994","WWF IC Championship — Ladder Match","One of the greatest WM matches ever — Razor retrieves belt"),
  row(L,"wm title",a("shawn-michaels","Shawn Michaels"),"WrestleMania XI","Apr 2, 1995","WWF IC Championship — Ladder Match","HBK sequel win — both matches historic"),
],
"method_bars":[
  {"label":"Razor's Edge (powerbomb pin)","n":"55%","pct":55},
  {"label":"Ladder retrieval","n":"10%","pct":10},
  {"label":"DQ / countout","n":"20%","pct":20},
  {"label":"Clean loss","n":"15%","pct":15},
],
"method_intro":"The Razor's Edge — a crucifix powerbomb — was one of WWF's most visually devastating finishers. At 6'7\" and nearly 300 pounds, Hall's physical presence made the move look genuinely dangerous for opponents of any size.",
"method_title":"The Bad Guy method",
"pull_facts":[
  {"n":"4×","l":"WWF IC Champion — more reigns than anyone at the time of his departure"},
  {"n":"1996","l":"Jumped to WCW — his appearance on Nitro alongside Kevin Nash launched the nWo angle that changed wrestling"},
  {"n":"WM X","l":"Ladder match vs. HBK — Dave Meltzer gave it 4.5 stars; modern consensus says even higher"},
  {"n":"2022","l":"Passed away March 14 — one of wrestling's most naturally gifted performers"},
],
"champ_title":"Championship history",
"champ_badge":"IC",
"champ_rows_html":(
  cr("WWF Intercontinental Championship","4× (1993, 1994, 1995, 1996)","Most IC reigns at the time of his WWF departure")+
  cr("WCW United States Championship","1× (1996–97)","Won after nWo jump; part of the WCW title picture")+
  cr("WCW World Tag Team Championship","6× (w/ Kevin Nash as Outsiders)","Outsiders dominated WCW tag division 1996–1998")+
  cr("NWA/AWA regional titles","Multiple","Pre-WWF territory reigns")
),
"timeline_items":[
  {"time":"1984","h":"Pro debut","p":"Begins in NWA territories — quickly noted for his size, look, and natural charisma."},
  {"time":"1992","h":"Razor Ramon debut — WWF","p":"Debuts the Razor Ramon character — a Cuban crime boss with a toothpick and a sneer. One of WWF's most immediately over characters despite being a heel."},
  {"time":"1993","h":"4× WWF Intercontinental Champion","p":"Wins the IC title four times over two years — becomes the belt's most decorated holder of the era."},
  {"time":"1994","h":"WrestleMania X Ladder Match","p":"vs. Shawn Michaels in a Ladder Match at WM X — the match that changed wrestling. Both men walk away legends."},
  {"time":"1996","h":"nWo founding — WCW jump","p":"Jumps to WCW; Razor Ramon becomes Scott Hall. He and Kevin Nash (the Outsiders) appear on Nitro and form the nWo with Hulk Hogan — the angle that beat the WWF in the Monday Night Wars."},
  {"time":"1996–99","h":"WCW/nWo peak","p":"WCW United States Champion; 6× WCW Tag Team Champion with Nash. Personal struggles begin to affect his ring work."},
  {"time":"2014","h":"WWE Hall of Fame","p":"Inducted into the WWE Hall of Fame (as Razor Ramon, Class of 2014). Presented by Shawn Michaels."},
  {"time":"2022","h":"Passing","p":"Passes away March 14, 2022, following complications from hip replacement surgery. 63 years old."},
],
"personas":[
  {"slug":"razor-ramon","era":"WWF 1992–1996","name":"Razor Ramon","desc":"The Bad Guy — Cuban crime boss heel turned unlikely fan favourite. Toothpick, gold chains, and one of wrestling's best natural characters."},
  {"slug":"razor-ramon","era":"WCW 1996–1999","name":"Scott Hall / The Outsider","desc":"Himself — real name as the kayfabe-breaking nWo Outsider alongside Kevin Nash."},
],
"sig_matches":[
  {"rating":"★★★★★","title":"vs. Shawn Michaels — WrestleMania X (1994)","subtitle":"WWF Intercontinental Championship Ladder Match · March 20, 1994","desc":"The match that invented modern ladder match presentation. Both men use the ladder as an extension of storytelling, not just a prop. Considered by many the greatest WM match of the pre-Attitude era."},
  {"rating":"★★★★","title":"vs. Shawn Michaels — WrestleMania XI (1995)","subtitle":"WWF Intercontinental Championship Ladder Match · April 2, 1995","desc":"The sequel to WM X — nearly as good, and further cemented ladder matches as a WWF institution. Both matches together changed the visual language of pro wrestling."},
],
"rivalries_html":(
  f'    <div class="rivalry-card"><h3>{a("shawn-michaels","Shawn Michaels")}</h3><p>Two Ladder matches at WM X and XI — the defining rivalry of both careers at that moment. Hall and Michaels together created the template for spectacular wrestling.</p></div>\n'
  f'    <div class="rivalry-card"><h3>{a("goldust","Goldust")}</h3><p>1995–96 IC title programme — Goldust beat Hall for the title at In Your House 5; Hall won it back. A character-driven feud that was more than the sum of its parts.</p></div>\n'
  f'    <div class="rivalry-card"><h3>Kevin Nash</h3><p>The Outsiders tag team in WCW — one of wrestling history\'s most dominant tag acts, winning the WCW tag titles six times.</p></div>\n'
),
"relationships_html":(
  f'    <div class="rel-card"><h4>Tag partner</h4><p>Kevin Nash — The Outsiders in WCW; nWo founding members alongside Hulk Hogan.</p></div>\n'
  f'    <div class="rel-card"><h4>Son</h4><p>Cody Hall — also a professional wrestler who competed in Japan and NXT.</p></div>\n'
  f'    <div class="rel-card"><h4>Close friend</h4><p>{a("shawn-michaels","Shawn Michaels")} — real-life friendship behind the professional rivalry; Michaels presented Hall at the Hall of Fame.</p></div>\n'
),
"faqs":[
  {"q":"How many times did Razor Ramon win the WWF Intercontinental Championship?","a":"Razor Ramon (Scott Hall) won the WWF Intercontinental Championship four times between 1993 and 1996 — more reigns than any holder at the time of his departure for WCW."},
  {"q":"What is the famous Razor Ramon vs. Shawn Michaels ladder match?","a":"The ladder match at WrestleMania X on March 20, 1994 is considered one of the greatest matches in wrestling history. Hall and Michaels spent 18+ minutes using the ladder as a storytelling device, not just a prop. The match established the template for all future ladder matches in WWE."},
  {"q":"When did Scott Hall join the nWo?","a":"Scott Hall jumped from WWF to WCW in 1996. He and Kevin Nash appeared on WCW Monday Nitro as 'invaders' — the angle that led to the formation of the New World Order (nWo) when Hulk Hogan turned heel and joined them at Bash at the Beach 1996. The nWo angle drove WCW to beat WWF in TV ratings for 83 consecutive weeks."},
  {"q":"How did Scott Hall die?","a":"Scott Hall died on March 14, 2022, following complications from hip replacement surgery. He was 63. Hall had struggled with well-documented health and addiction issues throughout his later career."},
],
"faq_schema":[
  {"q":"How many times did Razor Ramon win the WWF Intercontinental Championship?","a":"Four times (1993-1996) — more reigns than any holder at that time."},
  {"q":"What is the famous Razor Ramon vs. Shawn Michaels ladder match?","a":"WrestleMania X, March 20, 1994 — widely considered one of the greatest wrestling matches ever; established the template for all future ladder matches."},
  {"q":"How did Scott Hall die?","a":"Scott Hall died March 14, 2022, following complications from hip replacement surgery. He was 63."},
],
"related_links":[
  {"slug":"shawn-michaels","name":"Shawn Michaels"},{"slug":"goldust","name":"Goldust"},
  {"slug":"stone-cold-steve-austin","name":"Steve Austin"},{"slug":"triple-h","name":"Triple H"},
  {"slug":"the-undertaker","name":"The Undertaker"},{"slug":"bret-hart","name":"Bret Hart"},
]},

# ── 2. VINCE McMAHON ────────────────────────────────────────────────────────
{"slug":"vince-mcmahon","name":"Vince McMahon","initials":"VM",
"title_tag":"Vince McMahon — Career Record, Austin Rivalry & WWE Legacy | MAT Database",
"description":"Vince McMahon: WWE Chairman, the most powerful figure in wrestling history, and Austin's greatest rival. The Mr. McMahon villain character and the Austin feud drove the Attitude Era. Full career and storyline record.",
"answer":"Vince McMahon is simultaneously wrestling's greatest promoter and its most memorable villain — the 'Mr. McMahon' character's feud with Steve Austin from 1997 to 2001 is credited with saving the WWF and launching the Attitude Era that beat WCW.",
"facts_html":"""<dl class="facts">
  <div><dt>Born</dt><dd>Aug 24, 1945</dd></div>
  <div><dt>Hometown</dt><dd>Hartsville, South Carolina</dd></div>
  <div><dt>Height / Wt</dt><dd>6'2" / 248 lb</dd></div>
  <div><dt>Role</dt><dd>Chairman / CEO, WWE (1982–2023)</dd></div>
  <div><dt>Signature</dt><dd>Clothesline; Shane McMahon interference</dd></div>
  <div><dt>Storyline</dt><dd>Mr. McMahon — tyrannical boss villain</dd></div>
</dl>""",
"era":"WWF · WWE  •  1997–2009 (on-screen)",
"promo_chip":"Mr. McMahon — The Boss",
"alt_names":["Mr. McMahon","Vincent Kennedy McMahon","Vince","The Chairman"],
"same_as":["https://en.wikipedia.org/wiki/Vince_McMahon","https://www.wwe.com/superstars/mr-mcmahon"],
"bg_gradient":"linear-gradient(150deg,color-mix(in oklab,#1a1a1a 45%,#000),#0c0d10 65%)",
"subnav":["record","championships","timeline","signature","rivalries","faq"],
"rec_stats":[
  {"n":"Austin","l":"The feud that saved the WWF","gold":True},
  {"n":"1998","l":"Year Austin vs. McMahon became the top programme in wrestling"},
  {"n":"Royal Rumble","l":"Won the 1999 Royal Rumble match — a genuine storyline achievement"},
  {"n":"ECW","l":"Became the on-screen ECW Champion in 2001 storyline"},
],
"wl_strip":[False,True,False,False,True,False,False,True,False,False,True,False,False,False,True],
"tab_id":"vince",
"tab1_label":"Landmark ledger","tab1_count":"",
"filters":[
  {"key":"all","label":"All","count":""},
  {"key":"W","label":"McMahon wins","count":""},
  {"key":"L","label":"McMahon losses","count":""},
],
"main_rows":[
  row(L,"all",a("stone-cold-steve-austin","Steve Austin"),"WWF Raw","Apr 13, 1998","Street fight angle — Austin vs. McMahon first confrontation","Dude Love attacks Austin as corporate hireling — angle not a match"),
  row(L,"all",a("stone-cold-steve-austin","Steve Austin"),"WWF Over the Edge","May 31, 1998","Steve Austin vs. Dude Love — McMahon as special referee","McMahon tries to screw Austin; Austin wins anyway"),
  row(W,"all","Shane McMahon","WWF Raw","various 1998","Tag — McMahons vs. Austin","McMahon Family briefly got one over on Austin via numbers"),
  row(W,"all",a("stone-cold-steve-austin","Steve Austin"),"Royal Rumble 1999","Jan 24, 1999","Royal Rumble Match (McMahon wins)","McMahon wins the Royal Rumble — drawing massive heat"),
  row(L,"all",a("stone-cold-steve-austin","Steve Austin"),"WWF St. Valentine's Day Massacre","Feb 14, 1999","Steel Cage Match","Austin wins the cage match; McMahon loses but gets protected by Big Show interference"),
  row(L,"all",a("stone-cold-steve-austin","Steve Austin"),"WWF Raw","Feb 15, 1999","Street fight — night after cage","Austin gets his receipt; McMahon beaten in the ring"),
  row(W,"all",a("triple-h","Triple H") +" &amp; "+a("shane-mcmahon","Shane McMahon"),"WWE No Mercy 2003","Oct 19, 2003","Tag — Vince &amp; Shane vs. La Resistance (brand-crossing angle)","McMahons win the tag — storyline win"),
  row(L,"all",a("bret-hart","Bret Hart"),"WWE Raw","Feb 8, 2010","No Holds Barred Match","Hart beats McMahon — Hitman's revenge for Montreal Screwjob 13 years later"),
],
"method_bars":[
  {"label":"Angle / storyline win (non-clean)","n":"60%","pct":60},
  {"label":"By DQ / disqualification","n":"25%","pct":25},
  {"label":"Clean win (rare)","n":"8%","pct":8},
  {"label":"Submission","n":"7%","pct":7},
],
"method_intro":"McMahon as a wrestler was always secondary to McMahon as a character — the point was never for him to win clean, but for Austin to overcome the corrupt authority figure. McMahon's in-ring work served the story, not his own performance.",
"method_title":"Authority as character",
"pull_facts":[
  {"n":"1997","l":"The Montreal Screwjob — McMahon orders the bell rung on Bret Hart at Survivor Series; the real event that created the Mr. McMahon villain"},
  {"n":"1998","l":"Austin vs. McMahon becomes the biggest angle in wrestling — WWF overtakes WCW in Monday Night Wars"},
  {"n":"Royal Rumble 1999","l":"McMahon wins the Rumble match — one of wrestling's greatest heel moments"},
  {"n":"2023","l":"Retires from WWE Board amid personal legal matters — leaves the company he built over 40 years"},
],
"champ_title":"Storyline championship history",
"champ_badge":"WWE",
"champ_rows_html":(
  cr("ECW Championship","1× (2001 — storyline)","Won the ECW title in a storyline during the WWF/WCW Invasion angle")+
  cr("WWF Royal Rumble","Won (1999)","McMahon wins the Royal Rumble match — entered as a late entrant and went to WrestleMania XV")+
  cr("WWE Chairmanship","Real role — 1982–2023","Built WWE from a regional NWA territory into a global publicly-traded entertainment company")
),
"champ_note":"McMahon's real championship is the company he built. His storyline championship wins were always designed to generate crowd heat, never to establish him as a competitor.",
"timeline_items":[
  {"time":"1982","h":"Buys the WWF from his father","p":"Vince McMahon Jr. purchases the WWF from his father Vince Sr. and immediately begins expanding nationally — against the unwritten territory agreement."},
  {"time":"1985","h":"WrestleMania I","p":"Produces the first WrestleMania at Madison Square Garden — a gamble that works and establishes the WWE pay-per-view model."},
  {"time":"1993–96","h":"WWF's difficult years","p":"WCW, the steroid trial, and competition from nWo-era WCW put WWF on the defensive. McMahon responds by reinventing the product."},
  {"time":"1997","h":"Montreal Screwjob — Mr. McMahon born","p":"Orders the bell rung on Bret Hart at Survivor Series 1997. The real incident creates the Mr. McMahon character — a corporate villain who plays the rules against the talent."},
  {"time":"1998","h":"Austin vs. McMahon — Attitude Era","p":"The Austin feud becomes the biggest angle in wrestling — 83 episodes of head-to-head competition with WCW and WWF wins."},
  {"time":"1999","h":"Royal Rumble win — WrestleMania XV","p":"McMahon wins the Royal Rumble; main events WrestleMania XV vs. Austin. WM XV main event is a spectacle built on two years of storytelling."},
  {"time":"2001","h":"WWF buys WCW","p":"McMahon purchases WCW's library and trademarks from Ted Turner's AOL Time Warner. Wrestling's Monday Night War ends."},
  {"time":"2023","h":"Retirement","p":"Retires from WWE Board amid personal legal matters. Leaves the company he built from a regional territory into a multi-billion-dollar global brand."},
],
"personas":[
  {"slug":"vince-mcmahon","era":"1993–1997","name":"Vince McMahon, Announcer","desc":"Straight announcer and backstage authority — before the character was born."},
  {"slug":"vince-mcmahon","era":"1997–2009","name":"Mr. McMahon","desc":"The power-mad corporate villain — the Austin foil that saved the WWF."},
],
"sig_matches":[
  {"rating":"Historic","title":"Austin vs. McMahon — The Feud (1997–2001)","subtitle":"WWF storyline · 1997–2001","desc":"The most commercially successful wrestling angle of the 20th century. Austin represented the blue-collar worker; McMahon the corrupt boss. The crowd invested because the archetype was universal and both performers executed it brilliantly."},
  {"rating":"★★★½","title":"vs. Bret Hart — No Holds Barred (WWE Raw, 2010)","subtitle":"February 8, 2010","desc":"Thirteen years after Montreal, Bret Hart gets his receipt. The match was basic — McMahon was 64 — but the emotional payoff was enormous and the segment was genuinely moving."},
],
"rivalries_html":(
  f'    <div class="rivalry-card"><h3>{a("stone-cold-steve-austin","Steve Austin")}</h3><p>THE rivalry of the Attitude Era — tyrannical boss vs. rebellious employee. McMahon\'s villain and Austin\'s anti-hero defined late 1990s wrestling and drove WWF past WCW in the Monday Night Wars.</p></div>\n'
  f'    <div class="rivalry-card"><h3>{a("bret-hart","Bret Hart")}</h3><p>Montreal Screwjob — McMahon ordered the bell rung on Hart at Survivor Series 1997. The real incident that created the Mr. McMahon character, and one of wrestling\'s most controversial moments.</p></div>\n'
  f'    <div class="rivalry-card"><h3>{a("triple-h","Triple H")}</h3><p>Long-time real-life son-in-law (married Stephanie McMahon) and on-screen rival. The McMahon-Helmsley Era 1999–2000 was built on their real relationship.</p></div>\n'
),
"relationships_html":(
  f'    <div class="rel-card"><h4>Son-in-law</h4><p>{a("triple-h","Triple H")} — married Stephanie McMahon in 2003. The McMahon-Helmsley connection is both real and a major storyline thread.</p></div>\n'
  f'    <div class="rel-card"><h4>Son</h4><p>Shane McMahon — on-screen rival and ally; real-life son who left WWE to pursue his own ventures.</p></div>\n'
  f'    <div class="rel-card"><h4>Daughter</h4><p>Stephanie McMahon — on-screen heel authority figure; real-life WWE Chief Brand Officer until 2023.</p></div>\n'
),
"faqs":[
  {"q":"Did Vince McMahon ever wrestle Steve Austin?","a":"Yes. The Austin vs. McMahon feud included multiple physical confrontations and matches from 1997 to 2001. Their most notable formal match was a Steel Cage match at St. Valentine's Day Massacre (February 14, 1999), which Austin won. McMahon also won the 1999 Royal Rumble match as part of the ongoing programme."},
  {"q":"What is the Montreal Screwjob?","a":"The Montreal Screwjob occurred at WWE Survivor Series on November 9, 1997. McMahon ordered referee Earl Hebner to call for the bell while Bret Hart was locked in the Sharpshooter — declaring Shawn Michaels the winner without Hart submitting. The incident was not pre-agreed with Hart and is one of wrestling's most controversial real events."},
  {"q":"When did Vince McMahon retire from WWE?","a":"Vince McMahon announced his retirement from the WWE Board of Directors in January 2023, amid personal legal matters. He had served as WWE Chairman/CEO since purchasing the company from his father in 1982."},
],
"faq_schema":[
  {"q":"Did Vince McMahon ever wrestle Steve Austin?","a":"Yes — most notably a Steel Cage match at St. Valentine's Day Massacre (Feb 14, 1999), which Austin won. McMahon also won the 1999 Royal Rumble match."},
  {"q":"What is the Montreal Screwjob?","a":"At Survivor Series 1997, McMahon ordered the referee to ring the bell while Bret Hart was in the Sharpshooter — declaring Michaels the winner without Hart submitting. A genuine controversy."},
  {"q":"When did Vince McMahon retire from WWE?","a":"January 2023 — retired from the WWE Board amid personal legal matters after building the company from a regional territory since 1982."},
],
"related_links":[
  {"slug":"stone-cold-steve-austin","name":"Steve Austin"},{"slug":"bret-hart","name":"Bret Hart"},
  {"slug":"triple-h","name":"Triple H"},{"slug":"shawn-michaels","name":"Shawn Michaels"},
  {"slug":"the-undertaker","name":"The Undertaker"},{"slug":"the-rock","name":"The Rock"},
]},

# ── 3. EDGE ─────────────────────────────────────────────────────────────────
{"slug":"edge","name":"Edge","initials":"E",
"title_tag":"Edge (Adam Copeland) — Career Record, 11x World Champion & Title History | MAT Database",
"description":"Edge (Adam Copeland): 11x World Champion, Money in the Bank originator, and one of WWE's most decorated performers ever. Full career record, championship history, and rivalry tracker.",
"answer":"Edge is one of WWE's most decorated performers — an 11× World Champion (7 WWE + 4 WHC) whose Money in the Bank cash-in at New Year's Revolution 2006 on a weakened John Cena set the template for opportunistic title wins across wrestling.",
"facts_html":"""<dl class="facts">
  <div><dt>Born</dt><dd>Oct 30, 1973</dd></div>
  <div><dt>Hometown</dt><dd>Orangeville, Ontario, Canada</dd></div>
  <div><dt>Height / Wt</dt><dd>6'5" / 241 lb</dd></div>
  <div><dt>Active</dt><dd>1992–2023</dd></div>
  <div><dt>Signature</dt><dd>Spear, Edgecution (DDT)</dd></div>
  <div><dt>Tag</dt><dd>E&amp;C (w/ Christian); La Resistance foil</dd></div>
</dl>""",
"era":"WWF · WWE · AEW  •  1998–2023",
"promo_chip":"11× World Champion",
"alt_names":["The Rated-R Superstar","Edge","Adam Copeland","The Ultimate Opportunist"],
"same_as":["https://en.wikipedia.org/wiki/Edge_(wrestler)","https://www.wwe.com/superstars/edge"],
"bg_gradient":"linear-gradient(150deg,color-mix(in oklab,#1a3a5c 45%,#000),#0c0d10 65%)",
"subnav":["record","championships","timeline","personas","signature","rivalries","faq"],
"rec_stats":[
  {"n":"11×","l":"World Champion — 7× WWE + 4× World Heavyweight","gold":True},
  {"n":"7×","l":"WWF/WWE Tag Team Champion — with Christian and others"},
  {"n":"2010","l":"Forced retirement — neck injury after WrestleMania XXVI"},
  {"n":"2020","l":"Royal Rumble return — 9 years after retirement"},
],
"wl_strip":[True,True,True,False,True,True,True,True,False,True,True,True,False,True,True],
"tab_id":"edge",
"tab1_label":"Landmark ledger","tab1_count":"",
"tab2_label":"WrestleMania","tab2_count":"",
"filters":[
  {"key":"all","label":"All","count":""},
  {"key":"W","label":"Wins","count":""},
  {"key":"L","label":"Losses","count":""},
  {"key":"title","label":"World title","count":""},
  {"key":"wm","label":"WrestleMania","count":""},
],
"main_rows":[
  row(W,"title",a("john-cena","John Cena"),"New Year's Revolution 2006","Jan 8, 2006","WWE Championship — Money in the Bank cash-in","Edge spears exhausted Cena after Cell match — first MITB cash-in"),
  row(L,"title",a("john-cena","John Cena"),"Royal Rumble 2006","Jan 29, 2006","WWE Championship","Cena regains — Edge only held it 3 weeks"),
  row(W,"title",a("john-cena","John Cena"),"New Year's Revolution 2006","Jan 8, 2006","WWE Championship — MITB cash-in","See above — template-setting opportunistic win"),
  row(W,"wm",a("the-undertaker","The Undertaker"),"WrestleMania XXIV","Mar 30, 2008","World Heavyweight Championship","Edge retains — pin in one of WM's best matches"),
  row(L,"wm title",a("the-undertaker","The Undertaker"),"WrestleMania XXV","Apr 5, 2009","World Heavyweight Championship","Undertaker wins — WM Streak continues"),
  row(W,"all",a("the-undertaker","The Undertaker"),"WWE SmackDown","Apr 30, 2010","World Heavyweight Championship","Edge retains — last title reign before injury retirement"),
  row(L,"all",a("the-undertaker","The Undertaker"),"WWE SmackDown","May 2010","World Heavyweight Championship","Undertaker ultimately ends Edge's final reign"),
  row(W,"all","Dolph Ziggler","WWE SmackDown","2012","World Heavyweight Championship","Post-comeback second reign begins"),
  row(L,"all",a("the-undertaker","The Undertaker"),"WrestleMania XXXVII","Apr 10, 2021","Hell in a Cell","Edge loses cell match — in first return WM main event"),
],
"wm_rows":[
  row(W,"wm title","Kurt Angle &amp; "+a("chris-jericho","Chris Jericho"),"WrestleMania X8","Mar 17, 2002","Undisputed Tag Team Championship — w/ Booker T","Edge &amp; Booker T win tag titles in dual-brand match"),
  row(W,"wm",a("mick-foley","Mick Foley"),"WrestleMania 22","Apr 2, 2006","Hardcore Match","Edge wins in brutal bout — Foley covered in flaming tables"),
  row(W,"wm title",a("the-undertaker","The Undertaker"),"WrestleMania XXIV","Mar 30, 2008","World Heavyweight Championship","Edge retains — one of WM's all-time great title matches"),
  row(L,"wm title",a("the-undertaker","The Undertaker"),"WrestleMania XXV","Apr 5, 2009","World Heavyweight Championship","Taker wins — continuation of Taker WM streak"),
],
"method_bars":[
  {"label":"Spear (running tackle)","n":"50%","pct":50},
  {"label":"Edgecution (reverse DDT)","n":"15%","pct":15},
  {"label":"MITB / opportunistic cash-in","n":"10%","pct":10},
  {"label":"DQ / interference win","n":"15%","pct":15},
  {"label":"Clean loss","n":"10%","pct":10},
],
"method_intro":"Edge's Spear was one of WWE's most convincing high-impact finishers — the velocity of a 6'5\" athlete running full-speed at an opponent produced a believable collision. The Edgecution was his secondary finish for mat-wrestling sequences.",
"method_title":"The Rated-R arsenal",
"pull_facts":[
  {"n":"11×","l":"World Champion — most world title reigns in WWE history alongside HHH and Cena (at various points)"},
  {"n":"MITB","l":"First Money in the Bank cash-in ever (January 2006) — set the template for 15+ years of subsequent cash-ins"},
  {"n":"Undertaker","l":"Five WM interactions including two title matches at XXIV and XXV — the best Undertaker programme of the 2000s"},
  {"n":"2020","l":"Returns from retirement at Royal Rumble — 9 years after a cervical spine surgery forced him to stop"},
],
"champ_title":"Championship history",
"champ_badge":"Edge",
"champ_rows_html":(
  cr("WWE Championship","7× (2006–2009)","Most WWE title reigns at various points; cash-in win over Cena; feuds with Cena, Undertaker, Hardy")+
  cr("World Heavyweight Championship","4× (2004–2011)","Including back-to-back reigns in 2007 and 2010")+
  cr("WWF/WWE Tag Team Championship","7× (1999–2002)","Six with Christian; one with Hulk Hogan")+
  cr("WWF/WWE Intercontinental Championship","5×","Mid-card excellence before his main event push")
),
"timeline_items":[
  {"time":"1992","h":"Debut — Canadian independents","p":"Begins wrestling in Toronto-area independents as a teenager. Works for years before getting the WWF call."},
  {"time":"1998","h":"WWF debut","p":"Debuts on WWF Raw in 1998 as a mysterious vampire-inspired character. Quickly transitions to a more straightforward persona."},
  {"time":"1999–2002","h":"Edge & Christian — tag team excellence","p":"With Christian, wins 7 WWF Tag Team Championships and produces some of the best tag team work of the era (TLC matches with Hardy Boyz and Dudley Boyz)."},
  {"time":"2004","h":"First World Heavyweight Championship","p":"Wins his first World Heavyweight Championship — finally breaking through to the main event."},
  {"time":"2006","h":"First WWE Championship — MITB cash-in","p":"Cashes in the inaugural Money in the Bank briefcase on a weakened John Cena after an Elimination Chamber match. The cash-in becomes one of WWE's defining modern moments."},
  {"time":"2007–09","h":"Undertaker rivalry","p":"Multiple feuds with the Undertaker — WM XXIV world title match, WM XXV world title match, and a series of SmackDown programme. Considered by many the Undertaker's best non-WM storyline of the 2000s."},
  {"time":"2011","h":"Retirement","p":"Forced to retire due to a cervical spine injury — doctors tell him one more bump could leave him paralyzed. Announces retirement on SmackDown in April 2011."},
  {"time":"2012","h":"WWE Hall of Fame","p":"Inducted into the WWE Hall of Fame, Class of 2012 — at age 38, one of the youngest inductees ever."},
  {"time":"2020","h":"Return","p":"Returns at Royal Rumble 2020 — 9 years after retirement. Doctors clear him for limited competition. Begins a second career run that lasts until 2023."},
],
"personas":[
  {"slug":"edge","era":"1998","name":"The Vampire","desc":"Brief initial WWF character — quickly abandoned for a more grounded persona."},
  {"slug":"edge","era":"1999–2004","name":"Edge (babyface)","desc":"Charismatic fan favourite; tag team specialist with Christian."},
  {"slug":"edge","era":"2004–2011","name":"The Rated-R Superstar","desc":"Ruthless heel World Champion — the character that made Edge a genuine main event star."},
],
"sig_matches":[
  {"rating":"★★★★★","title":"TLC II — E&C vs. Hardyz vs. Dudleyz (WrestleMania X-Seven)","subtitle":"WWF Tag Team Championship · April 1, 2001","desc":"The defining TLC match — three teams, 20 minutes of escalating carnage, and Edge's diving spear off the top of a 20-foot ladder onto Jeff Hardy became one of wrestling's most iconic images."},
  {"rating":"★★★★½","title":"vs. The Undertaker — WrestleMania XXIV (2008)","subtitle":"World Heavyweight Championship · March 30, 2008","desc":"Edge retains against an in-his-prime Undertaker in a match widely considered one of WrestleMania's ten greatest. Both wrestlers told a complete story over 22 minutes."},
  {"rating":"★★★★","title":"vs. Mick Foley — WrestleMania 22 (2006)","subtitle":"Hardcore Match · April 2, 2006","desc":"Edge vs. Foley in a hardcore match that produced one of wrestling's most visually spectacular sequences — Edge spearing Foley through a flaming table. Foley called it one of his favourite matches."},
],
"rivalries_html":(
  f'    <div class="rivalry-card"><h3>{a("the-undertaker","The Undertaker")}</h3><p>The defining Edge rivalry — WM XXIV title match (Edge wins), WM XXV title match (Taker wins), and years of SmackDown feuds. Two of WWE\'s best performers at their peak.</p></div>\n'
  f'    <div class="rivalry-card"><h3>{a("john-cena","John Cena")}</h3><p>The WWE title feud of 2006 — Edge\'s cash-in over a beaten Cena set up a year of back-and-forth that drove SmackDown\'s rating.</p></div>\n'
  f'    <div class="rivalry-card"><h3>Christian</h3><p>Tag team partner (E&amp;C) — six tag title reigns together and one of the great tag acts of the late 1990s/early 2000s. Later on-screen rivals.</p></div>\n'
  f'    <div class="rivalry-card"><h3>{a("mick-foley","Mick Foley")}</h3><p>WM 22 hardcore match — Foley brought out Edge\'s career-best performance in a match that validated Edge as a main event heel.</p></div>\n'
),
"relationships_html":(
  f'    <div class="rel-card"><h4>Tag partner</h4><p>Christian (Jay Reso) — real-life friend and tag partner who developed alongside Edge in the Toronto independent scene and WWF.</p></div>\n'
  f'    <div class="rel-card"><h4>Wife</h4><p>Beth Phoenix — WWE Hall of Famer, former Divas Champion. Married Edge in 2016; two daughters.</p></div>\n'
),
"tv_items":[
  {"url":"https://www.imdb.com/title/tt14218918/","label":"TV Series","title":"Edge (AEW TV appearances 2023)","sub":"TNT/TBS — Edge appears in AEW after WWE contract ends"},
],
"faqs":[
  {"q":"How many world titles did Edge win?","a":"Edge won 11 World Championships — 7 WWE Championships and 4 World Heavyweight Championships. He also won the WWF/WWE Tag Team Championship 7 times, the Intercontinental Championship 5 times, and the inaugural Money in the Bank ladder match in 2005."},
  {"q":"What was Edge's Money in the Bank cash-in?","a":"Edge cashed in the inaugural Money in the Bank briefcase on January 8, 2006, at New Year's Revolution. John Cena had just survived an Elimination Chamber match and Edge immediately appeared and speared him twice, winning the WWE Championship. It was wrestling's first ever MITB cash-in and set the template for all future cash-ins."},
  {"q":"Why did Edge retire in 2011?","a":"Edge retired in April 2011 due to a cervical spine injury — a serious neck condition that doctors told him could result in paralysis if he continued wrestling. He announced his retirement on SmackDown. He was later cleared for limited competition and returned in 2020 at the Royal Rumble."},
],
"faq_schema":[
  {"q":"How many world titles did Edge win?","a":"11 World Championships — 7 WWE + 4 World Heavyweight. Also 7x Tag Team Champion, 5x IC Champion."},
  {"q":"What was Edge's Money in the Bank cash-in?","a":"January 8, 2006 — Edge cashed in on an exhausted John Cena after an Elimination Chamber match, winning the WWE Championship. The first-ever MITB cash-in."},
  {"q":"Why did Edge retire in 2011?","a":"A cervical spine injury — doctors told him one more serious bump could cause paralysis. He was later cleared and returned in 2020."},
],
"related_links":[
  {"slug":"the-undertaker","name":"The Undertaker"},{"slug":"john-cena","name":"John Cena"},
  {"slug":"mick-foley","name":"Mick Foley"},{"slug":"bret-hart","name":"Bret Hart"},
  {"slug":"shawn-michaels","name":"Shawn Michaels"},{"slug":"kurt-angle","name":"Kurt Angle"},
]},

# ── 4. BOOKER T ─────────────────────────────────────────────────────────────
{"slug":"booker-t","name":"Booker T","initials":"BT",
"title_tag":"Booker T — Career Record, 5x WCW Champion & King Booker History | MAT Database",
"description":"Booker T: 5× WCW World Heavyweight Champion, 1× WWE Champion, Hall of Famer, and one of wrestling's greatest mid-card-to-main-event breakout stories. Full career record and Spinaroonie legacy.",
"answer":"Booker T is one of wrestling's great crossover success stories — a 5× WCW World Heavyweight Champion who transitioned to WWF/WWE and became a 1× WWE Champion, Hall of Famer, and one of the most entertaining performers of two eras.",
"facts_html":"""<dl class="facts">
  <div><dt>Born</dt><dd>Mar 1, 1965</dd></div>
  <div><dt>Hometown</dt><dd>Plainview, Texas</dd></div>
  <div><dt>Height / Wt</dt><dd>6'3" / 256 lb</dd></div>
  <div><dt>Active</dt><dd>1989–2012</dd></div>
  <div><dt>Signature</dt><dd>Scissors Kick, Spinaroonie</dd></div>
  <div><dt>Tag</dt><dd>Harlem Heat (w/ Stevie Ray)</dd></div>
</dl>""",
"era":"WCW · WWF/WWE · TNA  •  1993–2012",
"promo_chip":"5× WCW World Heavyweight Champion",
"alt_names":["King Booker","Booker T","GI Bro","BookDust (w/ Goldust)"],
"same_as":["https://en.wikipedia.org/wiki/Booker_T_(wrestler)","https://www.wwe.com/superstars/booker-t"],
"bg_gradient":"linear-gradient(150deg,color-mix(in oklab,#1a5c3a 45%,#000),#0c0d10 65%)",
"subnav":["record","championships","timeline","personas","signature","rivalries","faq"],
"rec_stats":[
  {"n":"5×","l":"WCW World Heavyweight Champion","gold":True},
  {"n":"1×","l":"WWE Championship reign (2006)"},
  {"n":"Spinaroonie","l":"One of wrestling's most beloved signature poses"},
  {"n":"2013","l":"WWE Hall of Fame induction"},
],
"wl_strip":[True,True,False,True,True,True,False,True,True,False,True,True,True,False,True],
"tab_id":"booker",
"tab1_label":"Landmark ledger","tab1_count":"",
"tab2_label":"WrestleMania","tab2_count":"",
"filters":[
  {"key":"all","label":"All","count":""},
  {"key":"W","label":"Wins","count":""},
  {"key":"L","label":"Losses","count":""},
  {"key":"title","label":"Title matches","count":""},
  {"key":"wm","label":"WrestleMania","count":""},
],
"main_rows":[
  row(W,"title","Jeff Jarrett","WCW Bash at the Beach 2000","Jul 9, 2000","WCW World Heavyweight Championship","Booker T wins 5th WCW title — Goldberg assists"),
  row(L,"wm",a("triple-h","Triple H"),"WrestleMania XIX","Mar 30, 2003","World Heavyweight Championship","HHH retains — controversial loss many fans felt was wrong call"),
  row(W,"title","Rey Mysterio","WWE SmackDown","Mar 2006","WWE Championship — King of the Ring tournament path","Booker T wins via King of the Ring; reigns as King Booker"),
  row(L,"title",a("batista","Batista"),"SummerSlam 2006","Aug 20, 2006","World Heavyweight Championship","Batista wins — King Booker loses throne"),
  row(W,"all",a("stone-cold-steve-austin","Steve Austin"),"WWE SmackDown (Supermarket Brawl)","Dec 13, 2001","Unsanctioned brawl segment","Booker T and Austin brawl through a grocery store — iconic comedy segment"),
  row(W,"title","Goldberg","WCW Thunder","Aug 2000","WCW Title — later reign","Booker T beats Goldberg in WCW title match during the InVasion build"),
  row(L,"wm",a("triple-h","Triple H"),"WrestleMania XIX","Mar 30, 2003","World Heavyweight Championship","HHH wins — Booker T loses in controversial finish"),
  row(W,"all",a("the-rock","The Rock"),"WCW Nitro","2001","WCW Championship — InVasion era","Booker T in WCW/WWF crossover storyline with The Rock during Invasion"),
],
"wm_rows":[
  row(L,"wm title",a("triple-h","Triple H"),"WrestleMania XIX","Mar 30, 2003","World Heavyweight Championship","HHH retains — widely considered one of WM's most controversial finishes (many felt Booker should have won)"),
  row(W,"wm","Big Show &amp; Kane (tag)","WrestleMania X8","Mar 17, 2002","Tag — w/ Edge","Booker T &amp; Edge win tag titles — cross-brand WM match"),
],
"method_bars":[
  {"label":"Scissors Kick (axe kick variation)","n":"50%","pct":50},
  {"label":"Harlem Hangover (360 leg drop)","n":"15%","pct":15},
  {"label":"Spinaroonie + pin","n":"10%","pct":10},
  {"label":"DQ / countout","n":"15%","pct":15},
  {"label":"Clean loss","n":"10%","pct":10},
],
"method_intro":"The Scissors Kick was one of WCW's most visually impactful finishers — a high-impact axe kick that Booker T combined with the Spinaroonie to create one of wrestling's most crowd-pleasing finish sequences.",
"method_title":"Can you dig it?",
"pull_facts":[
  {"n":"5×","l":"WCW World Champion — most WCW title reigns of his era alongside Goldberg and Sting"},
  {"n":"WM XIX","l":"HHH vs. Booker T — one of wrestling's most debated WM finishes; most fans felt Booker T should have won"},
  {"n":"Supermarket Brawl","l":"Austin vs. Booker T grocery store segment (Dec 13, 2001 SmackDown) — one of WWE's most beloved comedy segments"},
  {"n":"Commentator","l":"Current WWE SmackDown commentary team member — second career as a broadcaster"},
],
"champ_title":"Championship history",
"champ_badge":"WCW",
"champ_rows_html":(
  cr("WCW World Heavyweight Championship","5× (1998–2000)","Tied for most WCW title reigns of his era")+
  cr("WWE Championship","1× (2006 — as King Booker)","Won during King of the Ring tournament; lost to Batista at SummerSlam 2006")+
  cr("WCW World Tag Team Championship","10× (Harlem Heat)","With Stevie Ray — dominant WCW tag team of the early 1990s")+
  cr("WWF/WWE Intercontinental/US Championships","Multiple","Mid-card excellence after WCW move to WWF")+
  cr("World Heavyweight Championship","1× (2006)","SmackDown title reign as King Booker")
),
"timeline_items":[
  {"time":"1989","h":"Pro debut","p":"Begins career in Texas independents. Early career largely unremarkable — becomes a tag team specialist in WCW with his brother Stevie Ray."},
  {"time":"1993","h":"Harlem Heat formed","p":"Teams with brother Stevie Ray as Harlem Heat in WCW — becomes one of the tag division's most dominant teams, winning the WCW Tag Championship 10 times."},
  {"time":"1997","h":"Singles breakthrough — WCW TV Title","p":"Breaks out as a singles star, winning the WCW Television Championship and establishing himself as a credible mid-card to upper-mid-card performer."},
  {"time":"1998–2000","h":"5× WCW World Heavyweight Champion","p":"Wins the WCW World title five times — cementing himself as one of WCW's top performers in its final years."},
  {"time":"2001","h":"WWF InVasion","p":"Crosses to WWF after WCW purchase — one of the WCW stars integrated into the InVasion angle. The grocery store brawl with Austin (December 13, 2001 SmackDown) becomes immediately iconic."},
  {"time":"2003","h":"WM XIX title shot","p":"vs. Triple H for the World Heavyweight Championship at WrestleMania XIX — one of WM's most debated finishes; most observers felt Booker T should have won."},
  {"time":"2006","h":"King Booker — WWE Champion","p":"Wins the King of the Ring tournament and rebrands as 'King Booker' with Queen Sharmell. Wins the WWE Championship — his only WWE title reign."},
  {"time":"2011","h":"TNA / retirement from in-ring","p":"Brief TNA run; transitions to commentary. Now a permanent member of WWE SmackDown commentary team."},
  {"time":"2013","h":"WWE Hall of Fame","p":"Inducted into the WWE Hall of Fame, Class of 2013."},
],
"personas":[
  {"slug":"booker-t","era":"WCW 1993–2001","name":"Booker T","desc":"Harlem Heat tag specialist turned 5× WCW World Champion."},
  {"slug":"booker-t","era":"WWE 2006","name":"King Booker","desc":"Regal British king character with Queen Sharmell — theatrical, comedic, surprisingly over."},
  {"slug":"booker-t","era":"1990–91","name":"GI Bro","desc":"Early independent gimmick — military-themed persona before WCW."},
],
"sig_matches":[
  {"rating":"★★★★","title":"vs. Goldberg — WCW Thunder (2000)","subtitle":"WCW World Heavyweight Championship · August 2000","desc":"Booker T defeating Goldberg during WCW's final year was a genuine surprise — and demonstrated that Booker had grown into one of WCW's most credible world champions."},
  {"rating":"★★★½","title":"vs. Triple H — WrestleMania XIX (2003)","subtitle":"World Heavyweight Championship · March 30, 2003","desc":"The match most fans remember for the wrong reason — HHH retaining. But Booker T's performance was exceptional throughout, and the crowd wanted him to win loudly. One of WM's most controversial outcomes."},
  {"rating":"Iconic Segment","title":"vs. Steve Austin — Supermarket Brawl (SmackDown, 2001)","subtitle":"Segment · December 13, 2001","desc":"Austin and Booker T brawling through a grocery store — knocking over displays, fighting into the parking lot, milking the comedy throughout. One of WWE's most beloved non-match segments ever filmed."},
],
"rivalries_html":(
  f'    <div class="rivalry-card"><h3>{a("triple-h","Triple H")}</h3><p>WM XIX World title match — one of WM\'s most debated finishes. Booker T was arguably the more over performer; HHH retained in a controversial decision.</p></div>\n'
  f'    <div class="rivalry-card"><h3>{a("the-rock","The Rock")}</h3><p>WCW/InVasion crossover matches in 2001 — including The Rock defending WWE interests against WCW champion Booker T. A rare inter-promotional programme of genuine star power.</p></div>\n'
  f'    <div class="rivalry-card"><h3>{a("stone-cold-steve-austin","Steve Austin")}</h3><p>The grocery store brawl (2001) — not a traditional rivalry but one of the most memorable Austin segments of his final active years.</p></div>\n'
),
"relationships_html":(
  f'    <div class="rel-card"><h4>Tag partner (brother)</h4><p>Stevie Ray — real-life brother; Harlem Heat tag team, 10× WCW Tag Champions together.</p></div>\n'
  f'    <div class="rel-card"><h4>Manager</h4><p>Queen Sharmell (wife) — on-screen Queen during King Booker era; real-life wife since 2005.</p></div>\n'
  f'    <div class="rel-card"><h4>Current role</h4><p>WWE SmackDown color commentator — second career as a broadcaster alongside Michael Cole.</p></div>\n'
),
"faqs":[
  {"q":"How many world titles did Booker T win?","a":"Booker T won the WCW World Heavyweight Championship 5 times and the WWE Championship once (as King Booker in 2006), plus the World Heavyweight Championship once on SmackDown. He also won the WCW World Tag Team Championship 10 times with his brother Stevie Ray as Harlem Heat."},
  {"q":"What is the Austin vs. Booker T supermarket brawl?","a":"On December 13, 2001, Steve Austin and Booker T had an unsanctioned brawl that started backstage and spilled into a nearby grocery store on SmackDown. The segment — featuring both men fighting through store aisles, knocking over displays, and brawling into the parking lot — became one of WWE's most beloved comedy segments."},
  {"q":"Why is WrestleMania XIX controversial for Booker T?","a":"Triple H vs. Booker T for the World Heavyweight Championship at WrestleMania XIX (March 30, 2003) ended with HHH retaining in a manner many fans and critics felt was wrong — Booker T had been built up strongly and the crowd was behind him. The loss is cited as one of WrestleMania's most controversial and disappointing outcomes."},
  {"q":"What is the Spinaroonie?","a":"The Spinaroonie is Booker T's signature pose — a spinning breakdance move performed on the mat after a big win. It became one of wrestling's most recognized crowd-pleasing moments and was regularly performed by Booker T throughout his career."},
],
"faq_schema":[
  {"q":"How many world titles did Booker T win?","a":"5x WCW World Heavyweight Champion, 1x WWE Champion (as King Booker, 2006), 1x World Heavyweight Champion. Also 10x WCW Tag Team Champion."},
  {"q":"What is the Austin vs. Booker T supermarket brawl?","a":"December 13, 2001 SmackDown — Austin and Booker T brawled through a grocery store in one of WWE's most beloved comedy segments."},
  {"q":"Why is WrestleMania XIX controversial for Booker T?","a":"Triple H retained the World Heavyweight Championship in a match many felt Booker T should have won — widely cited as one of WM's most disappointing outcomes."},
],
"related_links":[
  {"slug":"triple-h","name":"Triple H"},{"slug":"the-rock","name":"The Rock"},
  {"slug":"stone-cold-steve-austin","name":"Steve Austin"},{"slug":"goldust","name":"Goldust"},
  {"slug":"edge","name":"Edge"},{"slug":"kurt-angle","name":"Kurt Angle"},
]},

# ── 5. CHRIS BENOIT ─────────────────────────────────────────────────────────
{"slug":"chris-benoit","name":"Chris Benoit","initials":"CB",
"title_tag":"Chris Benoit — Career Record, Title History & WrestleMania XX | MAT Database",
"description":"Chris Benoit: WCW and WWF/WWE World Champion, one of technical wrestling's finest performers. Career record preserved as historical documentation. WWE removed Benoit from official records following events of June 2007.",
"answer":"Chris Benoit was one of professional wrestling's most technically accomplished performers — a WCW and WWE World Heavyweight Champion whose in-ring work is documented here as historical record. WWE removed Benoit from its official archives following the events of June 2007.",
"facts_html":"""<dl class="facts">
  <div><dt>Born</dt><dd>May 21, 1967</dd></div>
  <div><dt>Died</dt><dd>Jun 24, 2007 (age 40)</dd></div>
  <div><dt>Hometown</dt><dd>Edmonton, Alberta, Canada</dd></div>
  <div><dt>Height / Wt</dt><dd>5'10" / 220 lb</dd></div>
  <div><dt>Active</dt><dd>1985–2007</dd></div>
  <div><dt>Signature</dt><dd>Crippler Crossface, Flying Headbutt</dd></div>
</dl>""",
"era":"WCW · ECW · WWF/WWE  •  1985–2007",
"promo_chip":"WCW &amp; WWE World Champion",
"alt_names":["The Crippler","The Canadian Crippler","Chris Benoit"],
"same_as":["https://en.wikipedia.org/wiki/Chris_Benoit"],
"bg_gradient":"linear-gradient(150deg,color-mix(in oklab,#1a1a1a 45%,#000),#0c0d10 65%)",
"notice_html":"""<div class="notice notice--warning" role="note" style="background:color-mix(in oklab,#7c1a1a 30%,#111);border-left:4px solid #e11d2a;padding:1rem 1.25rem;margin:0 0 0 0">
  <strong>Historical record notice.</strong>
  Chris Benoit's in-ring career (1985–2007) is documented here as a matter of historical record. WWE removed Benoit from its official archives following the events of June 2007, in which Benoit killed his wife Nancy and son Daniel before taking his own life. Subsequent CTE research has identified severe chronic traumatic encephalopathy in Benoit's brain tissue. The match data below reflects his documented career; it does not endorse or diminish the gravity of the 2007 tragedy.
</div>""",
"subnav":["record","championships","timeline","signature","rivalries","faq"],
"rec_stats":[
  {"n":"WM XX","l":"Triple threat World Heavyweight title win — one of WM's most celebrated main events","gold":True},
  {"n":"2001","l":"Crippler Crossface forces Austin 'submission' on Raw — controversial Montreal-style finish"},
  {"n":"★★★★★","l":"Multiple five-star matches during 1999–2004 peak"},
  {"n":"CTE","l":"Severe chronic traumatic encephalopathy identified posthumously"},
],
"wl_strip":[True,True,True,True,False,True,True,True,True,True,False,True,True,True,False],
"tab_id":"benoit",
"tab1_label":"Landmark ledger","tab1_count":"",
"tab2_label":"WrestleMania","tab2_count":"",
"filters":[
  {"key":"all","label":"All","count":""},
  {"key":"W","label":"Wins","count":""},
  {"key":"L","label":"Losses","count":""},
  {"key":"title","label":"World title","count":""},
  {"key":"wm","label":"WrestleMania","count":""},
],
"main_rows":[
  row(W,"wm title",a("triple-h","Triple H")+" &amp; "+a("shawn-michaels","Shawn Michaels"),"WrestleMania XX","Mar 14, 2004","World Heavyweight Championship — Triple Threat","Benoit makes both tap — Crossface on HHH; Sharpshooter on HBK"),
  row(W,"title",a("stone-cold-steve-austin","Steve Austin"),"WWF Raw","May 28, 2001","WWF Championship — Montreal-style finish","Vince orders bell rung with Austin in Crossface"),
  row(L,"title",a("stone-cold-steve-austin","Steve Austin")+" &amp; "+a("triple-h","Triple H"),"WWF Backlash 2001","Apr 29, 2001","WWF Tag Team Championship — w/ Chris Jericho","Power Trip beats Benoit &amp; Jericho for tag titles"),
  row(W,"title",a("stone-cold-steve-austin","Steve Austin")+" &amp; "+a("triple-h","Triple H"),"WWF Raw","May 21, 2001","WWF Tag Team Championship","Benoit &amp; Jericho win — Triple H tears quad; Power Trip ends"),
  row(W,"all",a("kurt-angle","Kurt Angle"),"WWE Royal Rumble 2003","Jan 19, 2003","Singles — submission match","Benoit wins submission bout — all-time technical classic"),
  row(W,"all",a("kurt-angle","Kurt Angle"),"WWE SmackDown","various 2002","Best-of-7 submission series","Benoit wins the submission series — one of WWE's best TV programmes"),
  row(L,"title","WCW title — Sid Vicious","WCW Starrcade 2000","Dec 17, 2000","WCW World Heavyweight Championship","Benoit vacated title before this — technical championship controversy"),
  row(L,"all",a("chris-jericho","Chris Jericho"),"WWE Raw","2004","Singles — post-WM XX","Jericho wins in post-WM programme"),
],
"wm_rows":[
  row(W,"wm title",a("triple-h","Triple H")+" &amp; "+a("shawn-michaels","Shawn Michaels"),"WrestleMania XX","Mar 14, 2004","World Heavyweight Championship — Triple Threat","Benoit wins — makes HBK tap to Sharpshooter"),
  row(L,"wm",a("kurt-angle","Kurt Angle"),"WrestleMania X-Seven","Apr 1, 2001","Singles — submission count-anywhere","Angle wins — classic submission bout"),
],
"method_bars":[
  {"label":"Crippler Crossface (submission)","n":"45%","pct":45},
  {"label":"Flying Headbutt (high-risk pin)","n":"20%","pct":20},
  {"label":"German Suplex series","n":"20%","pct":20},
  {"label":"Sharpshooter","n":"10%","pct":10},
  {"label":"Clean loss","n":"5%","pct":5},
],
"method_intro":"Benoit's technical toolkit was among the deepest in wrestling — the Crossface, the rolling German suplexes, the headbutt, and the Sharpshooter gave him multiple credible submission and pin paths in any match. His intensity made every move look genuinely dangerous.",
"method_title":"Technical precision",
"pull_facts":[
  {"n":"WM XX","l":"Triple threat title win — one of WrestleMania's most celebrated main events in real time (before June 2007)"},
  {"n":"2001","l":"Power Trip programme with Austin and Jericho — produced some of Raw's greatest matches of the era"},
  {"n":"Crossface","l":"One of the most protected submission holds in wrestling — rarely escaped, always decisive"},
  {"n":"CTE","l":"Posthumous brain research found Benoit had the CTE of an 89-year-old — now cited in concussion research across sports"},
],
"champ_title":"Championship history",
"champ_badge":"WWE",
"champ_rows_html":(
  cr("WWE World Heavyweight Championship","1× (2004 — WM XX)","Triple threat win over HHH and HBK; reign ended by injury")+
  cr("WCW World Heavyweight Championship","1× (2000)","Brief reign — vacated when Benoit left for WWF")+
  cr("WWF/WWE Intercontinental Championship","4×","Multiple IC reigns 2000–2006")+
  cr("WWF/WWE Tag Team Championship","3×","Including with Chris Jericho (defeating Two-Man Power Trip) and others")+
  cr("WCW United States Championship","3×","Mid-card excellence in WCW 1995–1999")
),
"timeline_items":[
  {"time":"1985","h":"Debut","p":"Begins in Stu Hart's Dungeon in Calgary — same system as Bret Hart and Brian Pillman."},
  {"time":"1993","h":"WCW arrival — The Crippler","p":"Develops the 'Crippler' character in WCW — credible, intense, and technically elite."},
  {"time":"1999","h":"WCW peak","p":"Multiple five-star matches during 1999 in WCW. Wins the WCW World Heavyweight Championship briefly in January 2000 before immediately leaving for WWF."},
  {"time":"2000","h":"WWF arrival","p":"Joins WWF at Royal Rumble 2000. Immediately positioned as a serious title contender."},
  {"time":"2001","h":"Two-Man Power Trip programme","p":"Feuds with Steve Austin and Triple H over the WWF Championship and Tag Team titles — some of Raw's best matches of the era."},
  {"time":"2004","h":"WrestleMania XX — World Heavyweight Champion","p":"Wins the World Heavyweight Championship in the triple threat main event at WrestleMania XX, making both HHH and HBK submit. Celebrated as one of WM's greatest main events."},
  {"time":"2007","h":"Career and life end","p":"Chris Benoit, his wife Nancy, and their son Daniel are found dead on June 25, 2007. The investigation concluded it was a murder-suicide. WWE removes him from official records. Subsequent research identifies severe CTE in Benoit's brain tissue."},
],
"personas":[],
"sig_matches":[
  {"rating":"★★★★★","title":"vs. Kurt Angle — Royal Rumble 2003","subtitle":"Submission Match · January 19, 2003","desc":"Benoit and Angle in a 30-minute submission masterclass — one of the greatest pure wrestling matches in WWE history. Angle and Benoit were so evenly matched technically that every hold felt decisive."},
  {"rating":"★★★★★","title":"vs. Triple H & HBK — WrestleMania XX (2004)","subtitle":"World Heavyweight Championship Triple Threat · March 14, 2004","desc":"The main event of WrestleMania XX — Benoit wins the World Heavyweight title by making both Triple H and Shawn Michaels submit. Real-time considered one of WM's greatest main events."},
  {"rating":"★★★★","title":"vs. Chris Jericho (Two-Man Power Trip feud) — WWF Raw (2001)","subtitle":"WWF Tag Team Championship · May 21, 2001","desc":"Benoit and Jericho defeat Austin and Triple H for the tag titles — Triple H tears his quadriceps live on television; Austin pins Jericho but Benoit pins Austin; one of Raw's greatest matches."},
],
"rivalries_html":(
  f'    <div class="rivalry-card"><h3>{a("kurt-angle","Kurt Angle")}</h3><p>The technical wrestling rivalry — multiple five-star matches, a best-of-7 submission series, and a Royal Rumble 2003 bout. Two of wrestling\'s finest technical workers at their peak.</p></div>\n'
  f'    <div class="rivalry-card"><h3>{a("stone-cold-steve-austin","Steve Austin")}</h3><p>Two-Man Power Trip programme in 2001 — the Montreal-style Raw finish (Vince orders the bell with Austin in the Crossface) and the tag title programme produced Raw\'s best matches of that spring.</p></div>\n'
  f'    <div class="rivalry-card"><h3>{a("chris-jericho","Chris Jericho")}</h3><p>Tag team partners and sometime rivals — their WCW and WWF work together was consistently excellent; the Power Trip tag win together is one of Raw\'s greatest moments.</p></div>\n'
),
"relationships_html":(
  f'    <div class="rel-card"><h4>Tag partner</h4><p>{a("chris-jericho","Chris Jericho")} — tag team partnership in WCW and WWF that defeated the Two-Man Power Trip (Austin &amp; Triple H) for the tag titles.</p></div>\n'
  f'    <div class="rel-card"><h4>Trained by</h4><p>Stu Hart (Dungeon) — same Calgary system that produced Bret Hart, Brian Pillman, and others.</p></div>\n'
),
"faqs":[
  {"q":"Did Chris Benoit win the WWE Championship?","a":"Chris Benoit won the World Heavyweight Championship (at the time the equivalent of the WWE title on the Raw brand) at WrestleMania XX on March 14, 2004, in a triple threat match against Triple H and Shawn Michaels. He made both men submit — Michaels in a Sharpshooter and HHH in the Crossface. WWE removed this and other Benoit content from its official archives following the events of June 2007."},
  {"q":"What happened to Chris Benoit?","a":"Chris Benoit, his wife Nancy, and their son Daniel were found dead on June 25, 2007. The investigation concluded that Benoit had murdered his wife and son before taking his own life. Subsequent brain research identified severe chronic traumatic encephalopathy (CTE) in Benoit's tissue — among the worst CTE cases documented, equivalent to an 89-year-old. The case became a catalyst for concussion research in sports."},
  {"q":"Why did WWE remove Chris Benoit from its records?","a":"WWE removed Chris Benoit from its official records, Hall of Fame consideration, and video archive following the June 2007 murders of his wife and son. The company determined it could not appropriately celebrate the career of someone who had committed those acts. MAT Database preserves this record as historical documentation only."},
],
"faq_schema":[
  {"q":"Did Chris Benoit win the WWE Championship?","a":"Benoit won the World Heavyweight Championship at WrestleMania XX (March 14, 2004), making both Triple H and Shawn Michaels submit. WWE has since removed this from official records."},
  {"q":"What happened to Chris Benoit?","a":"Benoit murdered his wife Nancy and son Daniel, then took his own life in June 2007. Posthumous research found severe CTE in his brain tissue."},
  {"q":"Why did WWE remove Chris Benoit from its records?","a":"Following the June 2007 murders, WWE determined it could not celebrate Benoit's career and removed him from official archives, Hall of Fame consideration, and video content."},
],
"related_links":[
  {"slug":"kurt-angle","name":"Kurt Angle"},{"slug":"chris-jericho","name":"Chris Jericho"},
  {"slug":"stone-cold-steve-austin","name":"Steve Austin"},{"slug":"triple-h","name":"Triple H"},
  {"slug":"shawn-michaels","name":"Shawn Michaels"},{"slug":"bret-hart","name":"Bret Hart"},
]},

]

for w in wrestlers:
    html=build_page(w)
    path=os.path.join(BASE,w["slug"],"index.html")
    os.makedirs(os.path.dirname(path),exist_ok=True)
    with open(path,"w") as f:
        f.write(html)
    print(f"✅ {w['slug']} — {html.count(chr(10))} lines")

print("\nBatch 2b complete.")
