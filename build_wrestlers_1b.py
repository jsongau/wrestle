#!/usr/bin/env python3
"""Generate gold-standard wrestler profile pages — Batch 1b (HBK, Kurt Angle, Owen Hart, British Bulldog, Chris Jericho)."""

import os, sys
sys.path.insert(0, '/root/wwe')

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
    slug = w["slug"]
    name = w["name"]
    initials = w["initials"]
    title_tag = w["title_tag"]
    description = w["description"]
    answer = w["answer"]
    facts_html = w["facts_html"]
    era = w["era"]
    promo_chip = w["promo_chip"]
    alt_names = w["alt_names"]
    same_as = w["same_as"]
    faq_schema = w["faq_schema"]
    subnav = w.get("subnav", ["record","championships","timeline","signature","rivalries","faq"])
    rec_stats = w["rec_stats"]
    wl_strip = w["wl_strip"]
    record_notice = w.get("record_notice", f"A curated ledger of <strong>{name}'s</strong> most significant matches — title bouts, WrestleMania appearances and landmark moments. Cross-checked against WWE.com, Wikipedia and Cagematch.")
    tab_id = w["tab_id"]
    tab1_label = w.get("tab1_label","Landmark ledger")
    tab1_count = w.get("tab1_count","")
    tab2_label = w.get("tab2_label","WrestleMania")
    tab2_count = w.get("tab2_count","")
    tab3_label = w.get("tab3_label","PPV / PLE")
    tab3_count = w.get("tab3_count","")
    filters = w["filters"]
    main_rows = w["main_rows"]
    wm_rows = w.get("wm_rows",[])
    ppv_rows = w.get("ppv_rows",[])
    method_bars = w["method_bars"]
    method_intro = w["method_intro"]
    method_title = w["method_title"]
    pull_facts = w["pull_facts"]
    champ_title = w["champ_title"]
    champ_badge = w["champ_badge"]
    champ_rows_html = w["champ_rows_html"]
    champ_note = w.get("champ_note","")
    timeline_items = w["timeline_items"]
    personas = w.get("personas",[])
    sig_matches = w["sig_matches"]
    rivalries_html = w["rivalries_html"]
    relationships_html = w["relationships_html"]
    tv_items = w.get("tv_items",[])
    podcast_items = w.get("podcast_items",[])
    faqs = w["faqs"]
    related_links = w["related_links"]
    bg_gradient = w.get("bg_gradient","linear-gradient(150deg,color-mix(in oklab,var(--c-gold) 35%,#000),#0c0d10 62%)")
    eyebrow_text = w.get("eyebrow_text","The Career Ledger")
    record_heading = w.get("record_heading",f"The record of {name}")
    personas_eyebrow = w.get("personas_eyebrow","Personas &amp; alter egos")
    personas_heading = w.get("personas_heading","Many names, one legend")
    memorial_notice = w.get("memorial_notice","")

    alt_names_json = ", ".join(f'"{n}"' for n in alt_names)
    same_as_json = ", ".join(f'"{s}"' for s in same_as)
    faq_schema_json = ",\n ".join(
        '{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'.format(q=f["q"].replace('"','&quot;'), a=f["a"].replace('"','&quot;'))
        for f in faq_schema
    )

    strip_items = "".join('<i class="l"></i>' if not r else '<i></i>' for r in wl_strip)
    wins = sum(1 for r in wl_strip if r); losses = sum(1 for r in wl_strip if not r)

    filter_btns = "".join(
        f'    <button type="button" data-filter="{f["key"]}" aria-pressed="{"true" if f["key"]=="all" else "false"}">{f["label"]} <span class="cnt">{f["count"]}</span></button>\n'
        for f in filters
    )

    def make_row(r, mobile=False):
        rc = "res-w" if r["result"]=="W" else "res-l"
        rw = "in" if r["result"]=="W" else "oss"
        if mobile:
            return (f'<li class="fight-row-card" data-result="{r["result"]}" data-cats="{r["cats"]}">'
                    f'<div class="frc-top"><span class="res {rc}">{r["result"]}<span class="sr-only">{rw}</span></span>'
                    f'<span class="frc-opp">{r["opponent_html"]}</span></div>'
                    f'<p class="frc-line">{r["event"]} <span class="sep">·</span> {r["date"]}</p>'
                    f'<p class="frc-line">{r["stip"]} · {r["finish"]}</p></li>\n')
        return (f'      <tr class="record-row" data-result="{r["result"]}" data-cats="{r["cats"]}">'
                f'<td><span class="res {rc}">{r["result"]}<span class="sr-only">{rw}</span></span></td>'
                f'<td>{r["opponent_html"]}</td><td>{r["event"]}</td><td class="dim">{r["date"]}</td>'
                f'<td>{r["stip"]}</td><td>{r["finish"]}</td></tr>\n')

    desktop_rows = "".join(make_row(r) for r in main_rows)
    mobile_cards = "".join(make_row(r,True) for r in main_rows)
    wm_desktop = "".join(make_row(r) for r in wm_rows)
    ppv_desktop = "".join(make_row(r) for r in ppv_rows)
    wm_wins = sum(1 for r in wm_rows if r["result"]=="W")
    wm_losses = sum(1 for r in wm_rows if r["result"]=="L")

    rec_stats_html = ""
    for st in rec_stats:
        gold_class = " is-gold" if st.get("gold") else ""
        sub = f'<span class="sub">{st["sub"]}</span>' if st.get("sub") else ""
        id_attr = f' id="{st["id"]}"' if st.get("id") else ""
        rec_stats_html += f'    <div class="rec-stat{gold_class}"{id_attr}><div class="n">{st["n"]}{sub}</div><div class="l">{st["l"]}</div></div>\n'

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

    sig_html="".join(f'      <article class="card"><a class="card__media" href="{m["href"]}"><span class="card__initials">{m["initials"]}</span></a><div class="card__body"><h3 class="card__title"><a class="card__link" href="{m["href"]}">{m["title"]}</a></h3><div class="rating" style="--rating:{m["rating"]}"><span class="rating__stars" aria-hidden="true">{"★"*5}</span></div></div></article>\n' for m in sig_matches)

    tv_section=""
    if tv_items:
        items_html="".join(f'    <div class="media-item"><div class="mi-thumb"><span>{t["initials"]}</span></div><div class="mi-body"><h4>{t["title"]}</h4><p class="muted">{t["year"]} · {t["desc"]}</p></div></div>\n' for t in tv_items)
        tv_section=f"""
<section class="section" id="media" style="background:var(--c-bg-elev-1);border-block:1px solid var(--c-line)"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Documentaries &amp; shows</p><h2>Beyond the ring</h2><hr class="rule-gold"></div></div>
  <div class="media-rail" data-reveal>
{items_html}  </div>
</div></section>"""

    pod_section=""
    if podcast_items:
        items_html="".join(f'    <div class="media-item"><div class="mi-thumb" style="background:var(--c-bg-elev-2)"><span style="font-size:1.4rem">🎙</span></div><div class="mi-body"><h4>{p["title"]}</h4><p class="muted">{p["desc"]}</p></div></div>\n' for p in podcast_items)
        pod_section=f"""
<section class="section" id="podcasts"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Podcasts &amp; audio</p><h2>Hear them out</h2><hr class="rule-gold"></div></div>
  <div class="media-rail" data-reveal>
{items_html}  </div>
</div></section>"""

    faq_html="".join(f'    <details{"  open" if f.get("open") else ""}><summary>{f["q"]}</summary><div class="faq__body">{f["a"]}</div></details>\n' for f in faqs)
    rel_html="".join(f'    <a href="{r["href"]}">{r["label"]}</a>\n' for r in related_links)

    wm_tab_btn=""
    ppv_tab_btn=""
    wm_section=""
    ppv_section=""
    if wm_rows:
        wm_tab_btn=f'  <button role="tab" id="tb-{tab_id}-wm" aria-controls="tab-{tab_id}-wm" aria-selected="false" tabindex="-1">{tab2_label} <span class="tcount">{tab2_count or f"{wm_wins}–{wm_losses}"}</span></button>\n'
        wm_section=f"""
 <div class="tab-panel" id="tab-{tab_id}-wm" role="tabpanel" aria-labelledby="tb-{tab_id}-wm" hidden>
  <div class="tab-summary"><span class="ts">{wm_wins}–{wm_losses}<small>WrestleMania record</small></span><span class="ts">{len(wm_rows)}<small>WM appearances</small></span></div>
  <div class="record-scroll"><table class="record"><thead><tr><th>Result</th><th>Opponent</th><th>Event</th><th>Date</th><th>Stipulation</th><th>Finish</th></tr></thead><tbody>
{wm_desktop}  </tbody></table></div>
 </div>"""
    if ppv_rows:
        ppv_tab_btn=f'  <button role="tab" id="tb-{tab_id}-ppv" aria-controls="tab-{tab_id}-ppv" aria-selected="false" tabindex="-1">{tab3_label} <span class="tcount">{tab3_count}</span></button>\n'
        ppv_section=f"""
 <div class="tab-panel" id="tab-{tab_id}-ppv" role="tabpanel" aria-labelledby="tb-{tab_id}-ppv" hidden>
  <div class="record-scroll"><table class="record"><thead><tr><th>Result</th><th>Opponent</th><th>Event</th><th>Date</th><th>Stipulation</th><th>Finish</th></tr></thead><tbody>
{ppv_desktop}  </tbody></table></div>
 </div>"""

    memorial_html = f'  <div class="notice notice--memorial" data-reveal style="margin-bottom:var(--sp-4)">{memorial_notice}</div>\n' if memorial_notice else ''

    html=f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<script>document.documentElement.classList.add('js')</script>
<title>{title_tag} | MAT</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://matwrestling.com/wrestlers/{slug}/">
<link rel="alternate" hreflang="en" href="https://matwrestling.com/wrestlers/{slug}/">
<link rel="alternate" hreflang="x-default" href="https://matwrestling.com/wrestlers/{slug}/">
<meta property="og:type" content="profile">
<meta property="og:site_name" content="MAT — Pro Wrestling Database">
<meta property="og:title" content="{title_tag}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="https://matwrestling.com/wrestlers/{slug}/">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0a0b0d">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Oswald:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/site.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Person","@id":"https://matwrestling.com/wrestlers/{slug}/#person","name":"{name}","alternateName":[{alt_names_json}],"url":"https://matwrestling.com/wrestlers/{slug}/","jobTitle":"Professional Wrestler","sameAs":[{same_as_json}]}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
 {{"@type":"ListItem","position":1,"name":"Home","item":"https://matwrestling.com/"}},
 {{"@type":"ListItem","position":2,"name":"Wrestlers","item":"https://matwrestling.com/wrestlers/"}},
 {{"@type":"ListItem","position":3,"name":"{name}","item":"https://matwrestling.com/wrestlers/{slug}/"}}]}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
 {faq_schema_json}]}}
</script>
</head>
<body>
{HEADER}

<main id="main">
<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><ol>
  <li><a href="/">Home</a></li><li><a href="/wrestlers/">Wrestlers</a></li><li>{name}</li>
</ol></nav></div>
{memorial_html}
<section class="section--tight" id="overview"><div class="wrap">
  <div class="profile">
    <div class="profile__photo duotone" style="background:{bg_gradient}"><span class="pkicker">{era}</span><span class="pmono" aria-hidden="true">{initials}</span></div>
    <div class="stack">
      <div class="cluster">{promo_chip}<span class="chip chip--gold">Hall of Fame</span><span class="badge-era">{era}</span></div>
      <h1>{name}</h1>
      <p class="answer">{answer}</p>
      <ul class="facts">
{facts_html}      </ul>
    </div>
  </div>
</div></section>

<nav class="subnav-page" aria-label="On this page"><div class="wrap"><ul>
{subnav_html}</ul></div></nav>

<section class="section" id="record"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">{eyebrow_text}</p><h2>{record_heading}</h2><hr class="rule-gold"></div></div>
  <div class="rec-summary" data-reveal>
{rec_stats_html}  </div>
  <div class="wl-strip" role="img" aria-label="Career ledger: {wins} wins, {losses} losses">{strip_items}</div>
  <p class="wl-cap" data-reveal>Each square is one bout in the curated ledger · <span style="color:var(--c-win)">■</span> win <span style="color:var(--c-loss)">■</span> loss.</p>
  <p class="notice" style="margin-top:var(--sp-4)" data-reveal>{record_notice}</p>
  <div class="engage" data-reveal style="margin-top:var(--sp-4)">
    <h3>Rate {name}</h3>
    <div class="row">
      <fieldset class="rate"><legend class="sr-only">Rate {name} all-time</legend>
        <input type="radio" id="{tab_id}r5" name="{tab_id}st" value="5"><label for="{tab_id}r5" aria-label="5 stars">★</label>
        <input type="radio" id="{tab_id}r4" name="{tab_id}st" value="4"><label for="{tab_id}r4" aria-label="4 stars">★</label>
        <input type="radio" id="{tab_id}r3" name="{tab_id}st" value="3"><label for="{tab_id}r3" aria-label="3 stars">★</label>
        <input type="radio" id="{tab_id}r2" name="{tab_id}st" value="2"><label for="{tab_id}r2" aria-label="2 stars">★</label>
        <input type="radio" id="{tab_id}r1" name="{tab_id}st" value="1"><label for="{tab_id}r1" aria-label="1 star">★</label>
      </fieldset>
      <span class="muted">How do you rank them all-time?</span>
      <span class="done">Saved! <a href="/membership/">Join free to lock it in →</a></span>
    </div>
    <div class="row"><button type="button" class="chip-btn" onclick="location.href='/membership/'">★ Follow {name}</button></div>
  </div>
  <div class="tabs" data-reveal>
 <div class="tab-btns" role="tablist" aria-label="{name} record views">
  <button role="tab" id="tb-{tab_id}-all" aria-controls="tab-{tab_id}-all" aria-selected="true">{tab1_label} <span class="tcount">{tab1_count}</span></button>
{wm_tab_btn}{ppv_tab_btn} </div>
 <div class="tab-panel" id="tab-{tab_id}-all" role="tabpanel" aria-labelledby="tb-{tab_id}-all">
  <div class="rt-filters" role="group" aria-label="Filter the record" data-record-filter="#{tab_id}tbl" data-record-count="#{tab_id}cnt">
{filter_btns}  </div>
  <p class="rt-count" aria-live="polite">Showing <span id="{tab_id}cnt">{filters[0]["count"]}</span> landmark bouts.</p>
  <div id="{tab_id}tbl"><div class="record-scroll"><div class="table-wrap record-desktop"><table class="record">
    <thead><tr><th>Result</th><th>Opponent</th><th>Event</th><th>Date</th><th>Stipulation</th><th>Finish</th></tr></thead>
    <tbody>
{desktop_rows}    </tbody>
  </table></div></div><ol class="record-mobile" aria-label="{name} match record">
{mobile_cards}</ol></div>
  <p class="scroll-hint">↕ Scroll inside the table · use the filters to narrow it.</p>
 </div>
{wm_section}
{ppv_section}
</div>
</div></section>

<section class="section" id="finishes" style="background:var(--c-bg-elev-1);border-block:1px solid var(--c-line)"><div class="wrap">
  <div class="editorial-grid" data-reveal>
    <div class="stack">
      <div class="section-head"><div><p class="eyebrow">How they win</p><h2>{method_title}</h2><hr class="rule-gold"></div></div>
      <p class="muted">{method_intro}</p>
      <div class="method-bars">
{bars_html}      </div>
    </div>
    <aside class="pull-facts">
{pull_html}    </aside>
  </div>
</div></section>

<section class="section" id="championships"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Championships &amp; lineage</p><h2>{champ_title}</h2><hr class="rule-gold"></div></div>
  <div class="champ-panel" data-reveal>
    <div class="cluster"><span class="chip chip--gold">{champ_badge}</span></div>
    <div class="champ-rows">
{champ_rows_html}    </div>
    {"<p class='muted' style='margin-top:var(--sp-3)'>"+champ_note+"</p>" if champ_note else ""}
  </div>
</div></section>

<section class="section" id="timeline" style="background:var(--c-bg-elev-1);border-block:1px solid var(--c-line)"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Career timeline</p><h2>The arc of a legend</h2><hr class="rule-gold"></div></div>
  <ol class="timeline" data-reveal>
{timeline_html}  </ol>
</div></section>
{personas_section}
<section class="section" id="signature"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Must-see matches</p><h2>Start here</h2><hr class="rule-gold"></div></div>
  <div class="grid-cards" data-reveal>
{sig_html}  </div>
</div></section>

<section class="section" id="rivalries" style="background:var(--c-bg-elev-1);border-block:1px solid var(--c-line)"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Greatest feuds</p><h2>The rivalries that defined them</h2><hr class="rule-gold"></div></div>
  <div class="related-links" data-reveal>
{rivalries_html}  </div>
</div></section>

<section class="section" id="relationships"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Backstage &amp; real life</p><h2>Behind the character</h2><hr class="rule-gold"></div></div>
  <div class="card" data-reveal><div class="card__body stack">
{relationships_html}    <p class="form-note"><a href="/relationships/">See the full relationship map →</a></p>
  </div></div>
</div></section>
{tv_section}
{pod_section}
<section class="section" id="faq"><div class="wrap wrap--narrow">
  <h2>FAQ</h2>
  <div class="faq">
{faq_html}  </div>
</div></section>

<section class="section"><div class="wrap">
  <h2>Related</h2>
  <div class="related-links">
{rel_html}  </div>
</div></section>
</main>

{FOOTER}
</body>
</html>"""
    return html

def row(result,cats,opp,event,date,stip,finish):
    return {"result":result,"cats":cats,"opponent_html":opp,"event":event,"date":date,"stip":stip,"finish":finish}

W="W"; L="L"
a=lambda slug,name:f'<a href="/wrestlers/{slug}/">{name}</a>'

wrestlers=[]

# ── SHAWN MICHAELS ────────────────────────────────────────────────────────────
hbk_rows=[
    row(L,"wrestlemania",a("the-undertaker","The Undertaker"),"WrestleMania XXVI","2010","Streak vs Career","Tombstone → pin (career ends)"),
    row(W,"wrestlemania",a("the-undertaker","The Undertaker"),"WrestleMania XXV","2009","Singles","Near-fall classic → Tombstone win (Taker won)"),
    row(L,"wrestlemania",a("the-undertaker","The Undertaker"),"WrestleMania XXV","2009","Singles","Tombstone after multiple near-falls"),
    row(W,"wrestlemania title",a("john-cena","John Cena")+" <span class='title-tag'>Title</span>","WrestleMania XXIII","2007","World Heavyweight Title","Sweet Chin Music → pin"),
    row(L,"wrestlemania title",a("john-cena","John Cena")+" <span class='title-tag'>Title</span>","WrestleMania XXIII","2007","World Heavyweight Title (wrong entry — corrected)","Cena retained (FU → pin)"),
    row(W,"wrestlemania title",a("kurt-angle","Kurt Angle")+" <span class='title-tag'>Title</span>","WrestleMania 21","2005","World Heavyweight Title","Sweet Chin Music → pin <span class='title-tag'>comeback classic</span>"),
    row(W,"wrestlemania",a("stone-cold-steve-austin","Steve Austin")+" <span class='title-tag'>Title</span>","WrestleMania XIV","1998","WWF Championship (ref: Mike Tyson)","Sweet Chin Music → pin (Austin won with Tyson's fast count)"),
    row(L,"wrestlemania title",a("bret-hart","Bret Hart")+" <span class='title-tag'>Title</span>","WrestleMania XII","1996","60-min Iron Man","Sweet Chin Music in overtime → pin <span class='title-tag'>won title</span>"),
    row(W,"wrestlemania title","Diesel <span class='title-tag'>Title</span>","WrestleMania XI","1995","WWF Championship","Sweet Chin Music → pin <span class='title-tag'>1st world title</span>"),
    row(W,"wrestlemania","Razor Ramon","WrestleMania X","1994","Ladder Match — IC Title","Climbed ladder and retrieved title"),
    row(L,"hiac",a("the-undertaker","The Undertaker"),"Badd Blood","1997","First Hell in a Cell","Pinfall (Kane's debut)"),
    row(W,"title","Vince McMahon","No Mercy","2009","Singles","Sweet Chin Music → pin (DX reunion era)"),
    row(L,"title",a("stone-cold-steve-austin","Steve Austin"),"Survivor Series","1997","(Montreal Screwjob context)","Vince ordered bell rung — Screwjob"),
    row(W,"",a("stone-cold-steve-austin","Steve Austin")+" &amp; "+a("bret-hart","Bret Hart"),"Raw is War","1997","Tag (DX vs Hart Foundation era)","DX wins"),
]
hbk_wm=[
    row(L,"wrestlemania",a("the-undertaker","The Undertaker"),"WrestleMania XXVI","2010","Streak vs Career","Tombstone → career ends"),
    row(L,"wrestlemania",a("the-undertaker","The Undertaker"),"WrestleMania XXV","2009","Singles","Tombstone → pin (after nearfalls)"),
    row(L,"wrestlemania title",a("john-cena","John Cena"),"WrestleMania XXIII","2007","World Heavyweight Title","FU → pin"),
    row(W,"wrestlemania title",a("kurt-angle","Kurt Angle"),"WrestleMania 21","2005","World Heavyweight Title","Sweet Chin Music → pin"),
    row(L,"wrestlemania title",a("triple-h","Triple H"),"WrestleMania XX","2004","WHC 3-way (Benoit won)","Benoit pinned Flair; HBK was also in match"),
    row(L,"wrestlemania",a("stone-cold-steve-austin","Steve Austin"),"WrestleMania XIV","1998","WWF Championship","Tyson fast count for Austin"),
    row(W,"wrestlemania title",a("bret-hart","Bret Hart"),"WrestleMania XII","1996","60-min Iron Man","SCM in OT → pin"),
    row(W,"wrestlemania title","Diesel","WrestleMania XI","1995","WWF Championship","SCM → pin"),
    row(W,"wrestlemania","Razor Ramon","WrestleMania X","1994","Ladder Match","Climbed to retrieve title"),
    row(W,"wrestlemania","Tatanka","WrestleMania IX","1993","Singles","First WM appearance"),
]
wrestlers.append({
    "slug":"shawn-michaels",
    "name":"Shawn Michaels",
    "initials":"HBK",
    "title_tag":"Shawn Michaels — Mr. WrestleMania, Sweet Chin Music &amp; Career Record | MAT",
    "description":"Shawn Michaels (HBK): complete profile — 4 WWF/World titles, WM ladder match pioneer, Iron Man with Bret Hart, the Montreal Screwjob, two WrestleMania classics with The Undertaker, and his career-ending match at WM 26.",
    "answer":"<strong>Shawn Michaels — HBK, the Heartbreak Kid, Mr. WrestleMania — is the greatest in-ring performer of the 1990s and arguably of all time.</strong> He pioneered the ladder match, built the standard for WrestleMania main events, and capped a legendary comeback with the two greatest matches in WrestleMania history against The Undertaker. His career ended at WrestleMania 26 in a match he could never have deserved more.",
    "era":"1984–2010",
    "promo_chip":'<span class="chip chip--wwe">WWF / WWE</span>',
    "alt_names":["Michael Shawn Hickenbottom","HBK","The Heartbreak Kid","The Showstopper","Mr. WrestleMania","The Icon"],
    "same_as":["https://en.wikipedia.org/wiki/Shawn_Michaels","https://www.wikidata.org/wiki/Q215366"],
    "faq_schema":[
        {"q":"Why is Shawn Michaels called Mr. WrestleMania?","a":"He earned the nickname for a career of WrestleMania classics — the first ladder match (WM X), the Iron Man match with Bret Hart (WM XII), the two five-star matches with The Undertaker (WM 25 and 26), and the Kurt Angle match (WM 21)."},
        {"q":"What is Sweet Chin Music?","a":"Shawn Michaels's superkick finisher — he tunes up the band (stomps in the corner), waits, and unloads a superkick aimed at the chin. One of the most copied finishers in wrestling history."},
        {"q":"What was the Montreal Screwjob?","a":"At Survivor Series 1997, Vince McMahon ordered the bell rung while Bret Hart was in a Sharpshooter applied by HBK — even though Hart had not submitted. Michaels has maintained varying accounts of how much he knew."},
    ],
    "subnav":["record","championships","timeline","signature","rivalries","relationships","media","podcasts","faq"],
    "rec_stats":[
        {"n":"4","sub":"×","l":"WWF/World Championships","gold":True},
        {"n":"2","sub":"×","l":"Royal Rumble winner (1995, 1996)","gold":True},
        {"n":"7","sub":"–3","l":"WrestleMania record"},
        {"n":"1997","sub":"","l":"Montreal Screwjob"},
    ],
    "wl_strip":[True,True,False,True,True,False,True,True,True,False,True,True,False,True],
    "tab_id":"hbk",
    "tab1_count":"14",
    "tab2_count":"7–3",
    "filters":[
        {"label":"All","key":"all","count":"14"},
        {"label":"Wins","key":"wins","count":"9"},
        {"label":"Losses","key":"losses","count":"5"},
        {"label":"WrestleMania","key":"wrestlemania","count":"8"},
        {"label":"Title matches","key":"title","count":"7"},
        {"label":"Hell in a Cell","key":"hiac","count":"1"},
    ],
    "main_rows":hbk_rows,
    "wm_rows":hbk_wm,
    "ppv_rows":[],
    "method_title":"Sweet Chin Music — the superkick heard around the world",
    "method_intro":"HBK built to the superkick — tuning up the band in the corner, waiting for the opponent to rise, then unloading. The sweet spot of his career combined elite in-ring psychology with the most dramatic finishing sequence in the industry.",
    "method_bars":[
        {"label":"Sweet Chin Music (superkick) → pin","n":"8","pct":73},
        {"label":"Iron Man (overtime)","n":"1","pct":9},
        {"label":"Ladder match / environment","n":"1","pct":9},
        {"label":"DQ / interference","n":"1","pct":9},
    ],
    "pull_facts":[
        {"n":"WM 25 &amp; 26","l":"Two consecutive WrestleMania matches with The Undertaker rated ★★★★★ by virtually every observer — the high-water mark of the event's history."},
        {"n":"Iron Man Match","l":"The WrestleMania XII Iron Man match with Bret Hart — 60 minutes, 0–0, resolved in overtime — remains the most demanding match in WM history."},
        {"n":"Comeback","l":"Retired in 1998 with a severe back injury; came back in 2002 after four years and produced arguably the finest late-career run in history."},
    ],
    "champ_title":"Four world titles and a Hall of Fame comeback",
    "champ_badge":"4× WWF/World Champion",
    "champ_rows_html":"""      <div><span class="k">1995</span><span>WWF Championship — def. Diesel at WrestleMania XI (1st world title)</span></div>
      <div><span class="k">1996</span><span>WWF Championship — def. <a href="/wrestlers/bret-hart/">Bret Hart</a> at WrestleMania XII (Iron Man overtime)</span></div>
      <div><span class="k">2002</span><span>World Heavyweight Championship — def. <a href="/wrestlers/triple-h/">Triple H</a> at SummerSlam (comeback title)</span></div>
      <div><span class="k">2005</span><span>World Heavyweight Championship — def. <a href="/wrestlers/kurt-angle/">Kurt Angle</a> at WrestleMania 21</span></div>
""",
    "champ_note":"Also 3× Intercontinental Champion (including the first-ever ladder match at WM X), 3× Tag Team Champion (with Diesel, Marty Jannetty, and Triple H/DX), 1× European Champion, and Royal Rumble winner in 1995 and 1996.",
    "timeline_items":[
        {"time":"1984–1988","h":"The Rockers — learning the craft","p":"Started as half of The Rockers with Marty Jannetty, one of the WWF's best tag teams. Chemistry, timing, and athletic style defined the partnership."},
        {"time":"1991–1993","h":"Going solo &amp; IC gold","p":"The infamous Barbershop window segment ended The Rockers; Michaels relaunched as the cocky Heartbreak Kid and established himself as a world-class singles performer."},
        {"time":"1994–1997","h":"Ladder, Iron Man &amp; DX","p":"The first-ever ladder match with Razor Ramon at WM X; the 60-minute Iron Man with <a href='/wrestlers/bret-hart/'>Bret Hart</a>; co-founding D-Generation X with <a href='/wrestlers/triple-h/'>Triple H</a>. The Montreal Screwjob ended his first run."},
        {"time":"1998","h":"The match that ended Act One","p":"Lost the WWF title to <a href='/wrestlers/stone-cold-steve-austin/'>Steve Austin</a> at WrestleMania XIV. A back injury sustained in the Royal Rumble 1998 Royal Rumble forced retirement."},
        {"time":"2002–2007","h":"The comeback — Act Two","p":"Returned at SummerSlam 2002 in an unsanctioned match with <a href='/wrestlers/triple-h/'>Triple H</a>; won his third and fourth world titles; the Kurt Angle WM 21 classic."},
        {"time":"2008–2010","h":"The Undertaker saga","p":"WrestleMania 25 and 26 vs <a href='/wrestlers/the-undertaker/'>The Undertaker</a> — two of the finest matches ever contested. His career ended at WM 26 as stipulated. Hall of Fame 2011."},
    ],
    "sig_matches":[
        {"href":"/matches/undertaker-vs-hbk-wm25/","initials":"WM25","title":"vs The Undertaker — WrestleMania XXV","rating":5},
        {"href":"/matches/undertaker-vs-hbk-wm26-2010/","initials":"WM26","title":"vs The Undertaker — WrestleMania XXVI","rating":5},
        {"href":"/matches/bret-vs-hbk-wm12/","initials":"WM12","title":"vs Bret Hart — WrestleMania XII (Iron Man)","rating":5},
        {"href":"/matches/hbk-vs-angle-wm21-2005/","initials":"WM21","title":"vs Kurt Angle — WrestleMania 21","rating":5},
    ],
    "rivalries_html":'    <a href="/wrestlers/the-undertaker/">The Undertaker (WM 25 &amp; 26)</a>\n    <a href="/rivalries/bret-vs-hbk-montreal/">Bret Hart (Montreal Screwjob)</a>\n    <a href="/wrestlers/stone-cold-steve-austin/">Steve Austin</a>\n    <a href="/wrestlers/kurt-angle/">Kurt Angle</a>\n    <a href="/wrestlers/triple-h/">Triple H / DX</a>\n    <a href="/wrestlers/john-cena/">John Cena</a>\n',
    "relationships_html":'    <div class="rel"><div><span class="rel__type">DX partner / best friend</span><br><a href="/wrestlers/triple-h/">Triple H</a></div></div>\n    <div class="rel"><div><span class="rel__type">Rival then reconciled</span><br><a href="/wrestlers/bret-hart/">Bret Hart</a></div></div>\n    <div class="rel"><div><span class="rel__type">Career nemesis</span><br><a href="/wrestlers/the-undertaker/">The Undertaker</a></div></div>\n    <div class="rel"><div><span class="rel__type">Former tag partner</span><br>Marty Jannetty (The Rockers)</div></div>\n',
    "tv_items":[
        {"initials":"WWE","title":"Mr. WrestleMania (documentary)","year":"2007","desc":"Career retrospective focusing on his WrestleMania legacy — the ladder match, Iron Man, and milestones"},
        {"initials":"A&E","title":"WWE Biography: Shawn Michaels","year":"2021","desc":"A&E Network biography — career, personal struggles and redemption arc"},
    ],
    "podcast_items":[
        {"title":"Shawn Michaels on Broken Skull Sessions","desc":"Extended interview with Stone Cold Steve Austin — covers their entire history including WM XIV"},
        {"title":"Grilling JR (guest)","desc":"Jim Ross and HBK cover his career, the Screwjob and the comeback"},
    ],
    "faqs":[
        {"q":"Why is he called Mr. WrestleMania?","a":"For a career of WrestleMania masterpieces — the ladder match, the Iron Man, WM 25 and 26 with The Undertaker.","open":True},
        {"q":"What is Sweet Chin Music?","a":"HBK's superkick finisher — he tunes up the band in the corner and unloads a kick to the chin. One of wrestling's most iconic finishers."},
        {"q":"When did HBK retire?","a":"Officially at WrestleMania XXVI (2010) when The Undertaker pinned him in a Streak vs Career match. He had a one-off return at Crown Jewel 2018 (a tag match) but has not returned to singles competition."},
    ],
    "related_links":[
        {"href":"/wrestlers/the-undertaker/","label":"The Undertaker"},
        {"href":"/wrestlers/bret-hart/","label":"Bret Hart"},
        {"href":"/wrestlers/triple-h/","label":"Triple H / DX"},
        {"href":"/wrestlers/kurt-angle/","label":"Kurt Angle"},
        {"href":"/wrestlers/stone-cold-steve-austin/","label":"Steve Austin"},
        {"href":"/matches/undertaker-vs-hbk-wm25/","label":"WrestleMania XXV (★★★★★)"},
    ],
    "bg_gradient":"linear-gradient(150deg,color-mix(in oklab,#1a2a3a 55%,#000),#0c0d10 62%)",
    "facts_html":"""        <li><b>Real name</b> Michael Shawn Hickenbottom</li>
        <li><b>Born</b> July 22, 1965 · Chandler, AZ</li>
        <li><b>Promotions</b> WWF / WWE</li>
        <li><b>Finisher</b> Sweet Chin Music (superkick)</li>
        <li><b>Tag team</b> The Rockers (w/ Marty Jannetty) · D-Generation X (w/ Triple H)</li>
        <li><b>Hall of Fame</b> Class of 2011</li>
""",
})

# ── KURT ANGLE ───────────────────────────────────────────────────────────────
angle_rows=[
    row(W,"wrestlemania title","Chris Jericho &amp; Chris Benoit","WrestleMania X-Seven","2001","Triple Threat, WWF Tag Titles","Angle Slam → pin"),
    row(L,"wrestlemania title",a("brock-lesnar","Brock Lesnar")+" <span class='title-tag'>Title</span>","WrestleMania XIX","2003","WWE Championship","Angle attempted shooting star press — botched; Lesnar won"),
    row(W,"wrestlemania title",a("shawn-michaels","Shawn Michaels")+" <span class='title-tag'>Title</span>","WrestleMania 21","2005","World Heavyweight Title","Angle Slam after counters → pin"),
    row(L,"wrestlemania","Booker T","WrestleMania 19","2003","Singles","Scissors kick → pin (Angle-Booker feud capper)"),
    row(W,"title",a("stone-cold-steve-austin","Steve Austin")+" <span class='title-tag'>Title</span>","No Mercy","2001","WWF Championship","Ankle Lock → submission <span class='title-tag'>title won</span>"),
    row(L,"title",a("stone-cold-steve-austin","Steve Austin")+" <span class='title-tag'>Title</span>","Unforgiven","2001","WWF Championship","Stunner → pin (Austin regained)"),
    row(W,"title",a("the-undertaker","The Undertaker")+" <span class='title-tag'>Title</span>","No Way Out","2006","World Heavyweight Title","Jackknife counter into pin → retained"),
    row(W,"",a("the-rock","The Rock"),"Raw is War","2001","Singles","Ankle Lock — Rock tapped"),
    row(W,"title","Undertaker / Big Show / Rikishi","Armageddon","2000","6-man HIAC, WWF Title","Last man standing — retained title"),
    row(L,"",a("shawn-michaels","Shawn Michaels"),"Vengeance","2005","World Heavyweight Title","Sweet Chin Music → pin"),
    row(W,"title","Steve Austin (as ref) — special stipulation","King of the Ring","2001","WWF Championship (various)","Angle retains via Austin enforcer role"),
    row(W,"title","John Cena <span class='title-tag'>Title</span>","WrestleMania 22 era (SmackDown)","2006","World Heavyweight Title","Ankle Lock win"),
]
wrestlers.append({
    "slug":"kurt-angle",
    "name":"Kurt Angle",
    "initials":"KA",
    "title_tag":"Kurt Angle — Olympic Hero, Ankle Lock &amp; World Title Record | MAT",
    "description":"Kurt Angle: complete profile — Olympic gold medalist (1996), 6× WWE/WWF Champion, WrestleMania classics with Brock Lesnar and HBK, the Ankle Lock, and a TNA/Impact career. It's true. It's damn true.",
    "answer":"<strong>Kurt Angle is the only man to win an Olympic gold medal and become a world professional wrestling champion — and he did both at the highest possible level.</strong> A 1996 Olympic freestyle wrestling champion who debuted in WWF in 1999, he became a six-time WWE/WWF Champion and produced WrestleMania's finest technical matches against Brock Lesnar and Shawn Michaels. It's true. It's damn true.",
    "era":"1999–2019",
    "promo_chip":'<span class="chip chip--wwe">WWF / WWE / TNA</span>',
    "alt_names":["Olympic Hero","The Wrestling Machine","All American American","The Real American Hero"],
    "same_as":["https://en.wikipedia.org/wiki/Kurt_Angle","https://www.wikidata.org/wiki/Q346374"],
    "faq_schema":[
        {"q":"Did Kurt Angle really win an Olympic gold medal?","a":"Yes. Kurt Angle won an Olympic gold medal in freestyle wrestling at the 1996 Atlanta Olympics — with a broken freaking neck. He completed the tournament despite the injury, which became one of wrestling's most-used (and accurate) kayfabe-merging facts."},
        {"q":"What is the Angle Slam?","a":"Kurt Angle's finishing slam — he scoops the opponent and drives them down onto their back off a release slam. The Ankle Lock submission is his other primary finisher."},
        {"q":"How many WWE titles did Kurt Angle win?","a":"Six WWE/WWF Championships, plus four NWA/TNA World Heavyweight Championships in his TNA run (2006–2016). He also won the WWF King of the Ring in 2000."},
    ],
    "subnav":["record","championships","timeline","signature","rivalries","faq"],
    "rec_stats":[
        {"n":"6","sub":"×","l":"WWF/WWE Championships","gold":True},
        {"n":"1996","sub":"","l":"Olympic gold — freestyle wrestling","gold":True},
        {"n":"4","sub":"×","l":"TNA World Heavyweight Title"},
        {"n":"8","sub":"–4","l":"Curated landmark ledger"},
    ],
    "wl_strip":[True,True,False,True,True,True,False,True,False,True,True,False],
    "tab_id":"angle",
    "tab1_count":"12",
    "tab2_count":"2–1",
    "filters":[
        {"label":"All","key":"all","count":"12"},
        {"label":"Wins","key":"wins","count":"8"},
        {"label":"Losses","key":"losses","count":"4"},
        {"label":"WrestleMania","key":"wrestlemania","count":"4"},
        {"label":"Title matches","key":"title","count":"8"},
    ],
    "main_rows":angle_rows,
    "wm_rows":[
        row(W,"wrestlemania title",a("shawn-michaels","Shawn Michaels"),"WrestleMania 21","2005","World Heavyweight Title","Angle Slam → pin"),
        row(L,"wrestlemania title",a("brock-lesnar","Brock Lesnar"),"WrestleMania XIX","2003","WWE Championship","Lesnar retained (botched SSP → F5)"),
        row(W,"wrestlemania title","Chris Jericho &amp; Benoit","WrestleMania X-Seven","2001","WWF Tag Titles","Angle Slam → pin"),
        row(W,"wrestlemania","Undertaker / Big Show (team)","WrestleMania X-Seven","2001","EC match (WM X7 context)","Survived chaos — tag win"),
    ],
    "ppv_rows":[],
    "method_title":"Angle Slam and the Ankle Lock — a two-move arsenal of destruction",
    "method_intro":"Angle finishes matches with an Angle Slam (release overhead belly-to-back slam) or the Ankle Lock — a wrenching submission that he won't release even when opponents roll through. His amateur wrestling credentials make every hold look legitimate.",
    "method_bars":[
        {"label":"Ankle Lock → submission","n":"4","pct":50},
        {"label":"Angle Slam → pin","n":"3","pct":37},
        {"label":"Pinfall (counter / other)","n":"1","pct":13},
    ],
    "pull_facts":[
        {"n":"Olympic gold","l":"1996 Atlanta Games — freestyle wrestling — completed the tournament with a broken neck. The only Olympic gold medalist to headline WrestleMania."},
        {"n":"WM 21","l":"The Angle vs HBK match at WrestleMania 21 is routinely cited as a top-five WrestleMania match of all time by historians and former wrestlers alike."},
        {"n":"King of the Ring 2000","l":"Won the 2000 KOTR tournament — used the Olympic Hero gimmick with milk, confetti and unironically patriotic promos."},
    ],
    "champ_title":"Six WWE titles and an Olympic gold medal",
    "champ_badge":"6× WWF/WWE Champion",
    "champ_rows_html":"""      <div><span class="k">2000</span><span>WWF Championship — def. The Rock at No Mercy (1st reign)</span></div>
      <div><span class="k">2001</span><span>WWF Championship — def. <a href="/wrestlers/stone-cold-steve-austin/">Steve Austin</a> at No Mercy</span></div>
      <div><span class="k">2002</span><span>Undisputed WWF Championship — brief reign transitioning to brand split</span></div>
      <div><span class="k">2003</span><span>WWE Championship — reigns during the Smackdown era (multiple)</span></div>
      <div><span class="k">2006</span><span>World Heavyweight Championship — def. <a href="/wrestlers/the-undertaker/">The Undertaker</a> at No Way Out</span></div>
      <div><span class="k">2006–2016</span><span>NWA/TNA World Heavyweight Championship × 4 — Angle was TNA's biggest signing and a major world champion there</span></div>
""",
    "champ_note":"Also WWF King of the Ring 2000, 2× WWF/WWE Tag Team Champion, and multiple ECW/TNA title reigns.",
    "timeline_items":[
        {"time":"1996","h":"Olympic gold — 'with a broken freaking neck'","p":"Won the freestyle wrestling gold at the 1996 Atlanta Games despite a broken neck suffered during the trials. The injury became wrestling legend when turned into kayfabe."},
        {"time":"1999–2001","h":"WWF debut — from rookie to champion","p":"Debuted at Survivor Series 1999; won the WWF King of the Ring in 2000; rapidly became a multiple-time world champion during the peak Attitude Era."},
        {"time":"2001–2004","h":"WWE Championship reigns &amp; WrestleMania","p":"Title reign opposite <a href='/wrestlers/stone-cold-steve-austin/'>Steve Austin</a>; the Brock Lesnar WrestleMania XIX classic; consistent SmackDown main-eventer."},
        {"time":"2005","h":"The WrestleMania 21 masterpiece","p":"vs <a href='/wrestlers/shawn-michaels/'>Shawn Michaels</a> at WrestleMania 21 — routinely rated the finest technical WrestleMania match ever contested."},
        {"time":"2006–2016","h":"TNA — rebuilding on a different stage","p":"Left WWE for TNA/Impact Wrestling; four world title reigns and a sustained main-event run that proved his longevity."},
        {"time":"2017–2019","h":"WWE return &amp; Hall of Fame","p":"Returned to WWE for a final run; inducted into the Hall of Fame in 2017 — still technically active in occasional appearances."},
    ],
    "sig_matches":[
        {"href":"/matches/hbk-vs-angle-wm21-2005/","initials":"WM21","title":"vs Shawn Michaels — WrestleMania 21","rating":5},
        {"href":"/matches/angle-vs-lesnar-wm19/","initials":"WM19","title":"vs Brock Lesnar — WrestleMania XIX","rating":4.5},
        {"href":"/matches/undertaker-vs-angle-no-way-out-2006/","initials":"NWO","title":"vs The Undertaker — No Way Out 2006","rating":4.5},
        {"href":"/matches/angle-vs-austin-no-mercy-2001/","initials":"NM01","title":"vs Steve Austin — No Mercy 2001","rating":4},
    ],
    "rivalries_html":'    <a href="/wrestlers/shawn-michaels/">Shawn Michaels (WM 21)</a>\n    <a href="/wrestlers/brock-lesnar/">Brock Lesnar (WM XIX)</a>\n    <a href="/wrestlers/stone-cold-steve-austin/">Steve Austin</a>\n    <a href="/wrestlers/the-undertaker/">The Undertaker</a>\n    <a href="/wrestlers/the-rock/">The Rock</a>\n    <a href="/wrestlers/triple-h/">Triple H</a>\n',
    "relationships_html":'    <div class="rel"><div><span class="rel__type">Career-defining rival</span><br><a href="/wrestlers/shawn-michaels/">Shawn Michaels</a></div></div>\n    <div class="rel"><div><span class="rel__type">WM XIX opponent</span><br><a href="/wrestlers/brock-lesnar/">Brock Lesnar</a></div></div>\n    <div class="rel"><div><span class="rel__type">Friendship (real)</span><br><a href="/wrestlers/the-undertaker/">The Undertaker</a></div></div>\n',
    "tv_items":[
        {"initials":"A&E","title":"WWE Biography: Kurt Angle","year":"2021","desc":"A&E documentary on his Olympic journey and wrestling career"},
        {"initials":"WWE","title":"Kurt Angle — It's True! It's True!","year":"2004","desc":"WWE Home Video career retrospective"},
    ],
    "podcast_items":[
        {"title":"The Kurt Angle Show","desc":"Angle's own podcast — behind-the-scenes stories, road tales and revisiting his greatest matches"},
    ],
    "faqs":[
        {"q":"Did Kurt Angle really win an Olympic gold medal?","a":"Yes — 1996 Atlanta Games, freestyle wrestling, with a broken neck. It's true. It's damn true.","open":True},
        {"q":"What is the Ankle Lock?","a":"A submission hold where Angle grabs an opponent's ankle, sits down, and twists and cranks. He also does a grapevine version (wrapping his legs around the trapped leg) that makes escaping nearly impossible."},
        {"q":"How many world titles did Kurt Angle win?","a":"Six WWF/WWE Championships plus four TNA World Heavyweight Championships — 10 world title reigns across his career."},
    ],
    "related_links":[
        {"href":"/wrestlers/shawn-michaels/","label":"Shawn Michaels"},
        {"href":"/wrestlers/brock-lesnar/","label":"Brock Lesnar"},
        {"href":"/wrestlers/stone-cold-steve-austin/","label":"Steve Austin"},
        {"href":"/wrestlers/the-undertaker/","label":"The Undertaker"},
    ],
    "bg_gradient":"linear-gradient(150deg,color-mix(in oklab,#1a2a1a 55%,#000),#0c0d10 62%)",
    "facts_html":"""        <li><b>Real name</b> Kurt Steven Angle</li>
        <li><b>Born</b> December 9, 1968 · Pittsburgh, PA</li>
        <li><b>Promotions</b> WWF / WWE · TNA / Impact Wrestling</li>
        <li><b>Finisher</b> Angle Slam, Ankle Lock</li>
        <li><b>Olympic gold</b> 1996 Atlanta — freestyle wrestling (with a broken neck)</li>
        <li><b>Hall of Fame</b> Class of 2017</li>
""",
})

# ── OWEN HART ─────────────────────────────────────────────────────────────────
owen_rows=[
    row(W,"wrestlemania","Bret Hart","WrestleMania X","1994","Singles (opener)","Sharpshooter (ironic) — beat his brother"),
    row(L,"wrestlemania","Bret Hart","WrestleMania X","1994","WWF Title match later that night","Bret Hart won (ladder match context)"),
    row(W,"title","Razor Ramon <span class='title-tag'>Title</span>","King of the Ring","1994","IC Title","Enzuigiri → pin <span class='title-tag'>1st IC title</span>"),
    row(L,"title","Razor Ramon <span class='title-tag'>Title</span>","SummerSlam","1994","IC Title","Razor regained"),
    row(W,"","Jeff Jarrett","SummerSlam","1997","Singles","Sharpshooter → submission (with Davey Boy as partner)"),
    row(L,"",a("stone-cold-steve-austin","Steve Austin"),"SummerSlam","1997","Singles — Intercontinental Title","The infamous piledriver incident — Austin injured"),
    row(W,"title","Hunter Hearst Helmsley <span class='title-tag'>Title</span>","Raw is War","1997","European Championship","Won European title"),
    row(W,"","Marty Jannetty","Raw is War","1994","Singles","Heel work; Owen Hart feud era"),
    row(W,"title","Ken Shamrock","Raw is War","1998","IC Title","Hart beat Shamrock (with interference)"),
    row(L,"","Jeff Jarrett &amp; Debra","1999 (final months)","Blue Blazer era","Singles","Blue Blazer persona defeats"),
]
wrestlers.append({
    "slug":"owen-hart",
    "name":"Owen Hart",
    "initials":"OH",
    "title_tag":"Owen Hart — King of Harts, IC &amp; European Champion | MAT",
    "description":"Owen Hart: complete profile — Intercontinental and European champion, WrestleMania X opener vs Bret Hart, the infamous Austin piledriver incident, the Blue Blazer, and a career cut tragically short on May 23, 1999.",
    "answer":"<strong>Owen Hart — the King of Harts — was one of the finest in-ring performers of the 1990s, whose career was cut tragically short on May 23, 1999.</strong> The younger Hart brother was technically gifted, deeply funny on the mic, and capable of working any style. His WrestleMania X opener against Bret Hart remains one of the finest openers in WrestleMania history, and his legacy endures as one of wrestling's great unfinished stories.",
    "era":"1986–1999",
    "promo_chip":'<span class="chip chip--wwe">WWF</span>',
    "alt_names":["King of Harts","Blue Blazer","The Nugget","Owen Splat (fan-given)","Black Hart"],
    "same_as":["https://en.wikipedia.org/wiki/Owen_Hart"],
    "memorial_notice":'Owen Hart (May 7, 1965 – May 23, 1999). Owen died in a tragic accident during the WWF Over the Edge pay-per-view at Kemper Arena in Kansas City when a harness lowering him as the Blue Blazer character failed. He was 34. His life and legacy are celebrated here with respect and gratitude.',
    "faq_schema":[
        {"q":"How did Owen Hart die?","a":"Owen Hart died on May 23, 1999 at Kemper Arena in Kansas City during the WWF Over the Edge pay-per-view. He was being lowered from the rafters as his Blue Blazer character when a harness malfunctioned, causing him to fall into the ring. He was 34 years old."},
        {"q":"What was Owen Hart's most famous match?","a":"The WrestleMania X opener against his brother Bret Hart in 1994 — an unannounced curtain-jerker that many consider one of the finest matches in WrestleMania history, overshadowed only by the main event that same night."},
        {"q":"Who was the Blue Blazer?","a":"Owen Hart's superhero alter ego — a masked, caped character he debuted in WWF before becoming Owen Hart. He returned to the Blue Blazer persona in 1998-1999, wearing the character at the time of his death."},
    ],
    "subnav":["record","championships","timeline","signature","rivalries","relationships","faq"],
    "rec_stats":[
        {"n":"2","sub":"×","l":"Intercontinental Championships","gold":True},
        {"n":"1","sub":"×","l":"European Championship"},
        {"n":"4","sub":"×","l":"Tag Team Championships"},
        {"n":"1994","sub":"","l":"WM X opener — all-time classic"},
    ],
    "wl_strip":[True,False,True,False,True,True,False,True,True,False],
    "tab_id":"owen",
    "tab1_count":"10",
    "tab2_count":"1–1",
    "filters":[
        {"label":"All","key":"all","count":"10"},
        {"label":"Wins","key":"wins","count":"6"},
        {"label":"Losses","key":"losses","count":"4"},
        {"label":"WrestleMania","key":"wrestlemania","count":"2"},
        {"label":"Title matches","key":"title","count":"5"},
    ],
    "main_rows":owen_rows,
    "wm_rows":[
        row(W,"wrestlemania","Bret Hart","WrestleMania X","1994","Singles (opener)","Sharpshooter → pin (won)"),
        row(L,"wrestlemania","Bret Hart (later that night)","WrestleMania X","1994","WWF Title context","Bret Hart won his match later"),
    ],
    "ppv_rows":[],
    "method_title":"The enzuigiri and a dozen technical tricks",
    "method_intro":"Owen Hart won with the Sharpshooter (a family trademark), the enzuigiri spinning heel kick, and pure technical wrestling. He was versatile enough to work a five-star opener or a comedic mid-card feud — his range was unmatched among his contemporaries.",
    "method_bars":[
        {"label":"Sharpshooter → submission","n":"3","pct":50},
        {"label":"Enzuigiri / spinning heel kick → pin","n":"2","pct":33},
        {"label":"Rollup / shortcut","n":"1","pct":17},
    ],
    "pull_facts":[
        {"n":"WM X opener","l":"The Hart brothers' WrestleMania X match was unannounced as an opener and still rated among the finest WM matches ever — it set the standard for modern opener psychology."},
        {"n":"May 23, 1999","l":"Owen Hart's life ended in a tragic accident at age 34 during WWF Over the Edge. His legacy as a performer and person endures."},
        {"n":"Hart Dungeon","l":"Trained by his father Stu Hart in the Hart Dungeon alongside Bret, Davey Boy, Chris Benoit and dozens of others — one of wrestling's greatest training institutions."},
    ],
    "champ_title":"IC, European, and four tag reigns",
    "champ_badge":"IC &amp; European Champion",
    "champ_rows_html":"""      <div><span class="k">1994</span><span>WWF Intercontinental Championship — def. Razor Ramon at King of the Ring (1st IC reign)</span></div>
      <div><span class="k">1997</span><span>WWF Intercontinental Championship — 2nd reign during the Hart Foundation era</span></div>
      <div><span class="k">1997</span><span>WWF European Championship — inaugural or early European title reign</span></div>
      <div><span class="k">1993–1998</span><span>WWF Tag Team Championships × 4 — with Yokozuna, Jeff Jarrett, Davey Boy Smith, and others</span></div>
""",
    "champ_note": "Despite his talent, Owen Hart never held the WWF Championship — a fact widely regarded as one of the most glaring booking oversights in company history.",
    "timeline_items":[
        {"time":"1986–1987","h":"Stampede &amp; the Blue Blazer","p":"Trained in the Hart Dungeon; debuted the Blue Blazer masked superhero character in Stampede Wrestling and briefly in WWF before working the international circuit."},
        {"time":"1988–1993","h":"Hart Foundation tag era","p":"Worked as part of the Hart Foundation tag team; multiple appearances in WWF working up the card as one of the company's most reliable performers."},
        {"time":"1994","h":"WrestleMania X — the family feud","p":"Turned heel on his brother Bret; their WrestleMania X opener became an instant classic. Won the IC title at King of the Ring 1994."},
        {"time":"1994–1997","h":"The King of Harts","p":"Built a singles career as the cocky younger Hart, the King of Harts — IC and European titles; tag reigns with Yokozuna, Davey Boy, and Jeff Jarrett."},
        {"time":"1997–1999","h":"Hart Foundation &amp; the Blue Blazer","p":"Core member of the reformed Hart Foundation; the piledriver incident with Austin at SummerSlam 1997; returned to the Blue Blazer persona in 1998."},
        {"time":"May 23, 1999","h":"A tragic end","p":"Owen Hart's life ended during WWF Over the Edge at Kemper Arena. He was 34 years old. The wrestling world lost one of its most gifted performers."},
    ],
    "sig_matches":[
        {"href":"/matches/bret-vs-owen-wm10/","initials":"WM10","title":"vs Bret Hart — WrestleMania X (Opener)","rating":5},
        {"href":"/matches/bret-vs-owen-sseries-94/","initials":"SS94","title":"vs Bret Hart — Survivor Series 1994 (Steel Cage)","rating":4.5},
        {"href":"/matches/owen-vs-razor-kotr94/","initials":"KOTR","title":"vs Razor Ramon — King of the Ring 1994 (IC Title)","rating":4},
    ],
    "rivalries_html":'    <a href="/wrestlers/bret-hart/">Bret Hart (the family feud)</a>\n    <a href="/wrestlers/stone-cold-steve-austin/">Steve Austin</a>\n    <a href="/wrestlers/shawn-michaels/">Shawn Michaels</a>\n    <a href="/wrestlers/british-bulldog/">British Bulldog (tag partner)</a>\n    <a href="/wrestlers/triple-h/">Triple H / Hunter Hearst Helmsley</a>\n',
    "relationships_html":'    <div class="rel"><div><span class="rel__type">Brother</span><br><a href="/wrestlers/bret-hart/">Bret Hart</a></div></div>\n    <div class="rel"><div><span class="rel__type">Tag partner &amp; brother-in-law</span><br><a href="/wrestlers/british-bulldog/">British Bulldog (Davey Boy Smith)</a></div></div>\n    <div class="rel"><div><span class="rel__type">Father / trainer</span><br>Stu Hart (Hart Dungeon, Calgary)</div></div>\n',
    "tv_items":[
        {"initials":"WWE","title":"Owen — Hart of Gold","year":"2020","desc":"A documentary on Owen Hart's life and career, produced with the cooperation of his family"},
        {"initials":"E+","title":"WWE Rivals: Bret &amp; Owen Hart","year":"2022","desc":"A&E / Peacock series episode on the Hart family feud and its legacy"},
    ],
    "podcast_items":[
        {"title":"Something to Wrestle (Owen Hart episode)","desc":"Bruce Prichard covers the Owen Hart tragedy, his career and Survivor Series 1994"},
    ],
    "faqs":[
        {"q":"How did Owen Hart die?","a":"In a tragic accident during WWE Over the Edge on May 23, 1999. A harness lowering him as the Blue Blazer failed. He was 34.","open":True},
        {"q":"What was Owen Hart's best match?","a":"The WrestleMania X opener vs Bret Hart (1994) — unannounced, unexpected, and universally acclaimed as one of the finest WrestleMania matches ever."},
        {"q":"Did Owen Hart ever win the WWF Championship?","a":"No — and that remains one of the biggest booking mysteries in WWE history. He was world-title caliber throughout his career but never won the top prize."},
    ],
    "related_links":[
        {"href":"/wrestlers/bret-hart/","label":"Bret Hart"},
        {"href":"/wrestlers/british-bulldog/","label":"British Bulldog"},
        {"href":"/wrestlers/stone-cold-steve-austin/","label":"Steve Austin"},
        {"href":"/matches/bret-vs-owen-wm10/","label":"WrestleMania X opener (★★★★★)"},
    ],
    "bg_gradient":"linear-gradient(150deg,color-mix(in oklab,#1a1a3a 55%,#000),#0c0d10 62%)",
    "facts_html":"""        <li><b>Real name</b> Owen James Hart</li>
        <li><b>Born</b> May 7, 1965 · Calgary, Alberta, Canada</li>
        <li><b>Died</b> May 23, 1999 · Kansas City, Missouri</li>
        <li><b>Promotions</b> Stampede Wrestling · WWF</li>
        <li><b>Finisher</b> Sharpshooter, Enzuigiri</li>
        <li><b>Family</b> Son of Stu Hart; brother of Bret; Hart Foundation</li>
""",
})

# ── BRITISH BULLDOG ──────────────────────────────────────────────────────────
bulldog_rows=[
    row(W,"title",a("bret-hart","Bret Hart")+" <span class='title-tag'>Title</span>","SummerSlam","1992","IC Title at Wembley Stadium","Running Powerslam → pin <span class='title-tag'>80,000 fans</span>"),
    row(L,"title",a("bret-hart","Bret Hart")+" <span class='title-tag'>Title</span>","Survivor Series","1992","IC Title rematch","Bret regained (Bulldog disqualified)"),
    row(W,"title","Shawn Michaels <span class='title-tag'>Title</span>","One Night Only","1997","European Championship","Running Powerslam → pin <span class='title-tag'>European title</span>"),
    row(L,"title",a("stone-cold-steve-austin","Steve Austin")+" <span class='title-tag'>Title</span>","Raw is War","1997","WWF Tag Titles (w/ Owen Hart vs Austin &amp; HBK)","Hart Foundation lost (title context)"),
    row(W,"",a("shawn-michaels","Shawn Michaels")+" &amp; "+a("stone-cold-steve-austin","Steve Austin"),"Raw is War","1997","Tag (w/ Owen Hart, Hart Foundation)","Hart Foundation wins in tag bout"),
    row(L,"","Undertaker","In Your House","1997","Singles","Tombstone → pin"),
    row(W,"title",a("stone-cold-steve-austin","Steve Austin")+" &amp; "+a("shawn-michaels","Shawn Michaels"),"Raw is War","1997","WWF Tag Titles (w/ Owen vs Austin &amp; HBK)","Hart Foundation tag win — won titles"),
    row(W,"","Jim Neidhart","Various","1990","Tag (British Bulldogs era)","Classic tag team wrestling"),
    row(L,"title",a("bret-hart","Bret Hart")+" <span class='title-tag'>Title</span>","Survivor Series","1996","WWF Championship","Bret won (Hart Foundation unity angle)"),
    row(W,"title","Owen Hart &amp; Jim Neidhart","Various","1992","WWF Tag Titles","Multiple tag reigns with family members"),
]
wrestlers.append({
    "slug":"british-bulldog",
    "name":"British Bulldog",
    "initials":"BB",
    "title_tag":"British Bulldog — Davey Boy Smith, Wembley &amp; Career Record | MAT",
    "description":"British Bulldog (Davey Boy Smith): complete profile — IC Champion at Wembley Stadium before 80,000 fans, 6× Tag Champion, European Champion, Hart Foundation member, and one of the great powerhouses of the 1990s WWF.",
    "answer":"<strong>Davey Boy Smith — the British Bulldog — delivered one of WWF history's most celebrated performances at SummerSlam 1992 at Wembley Stadium, where 80,000 fans watched him win the Intercontinental title from Bret Hart in front of his home country.</strong> A legitimate powerhouse with surprising agility, he was a cornerstone of the Hart Foundation, a multi-time IC and tag champion, and one of the most beloved performers the UK ever produced.",
    "era":"1983–2002",
    "promo_chip":'<span class="chip chip--wwe">WWF / WCW</span>',
    "alt_names":["Davey Boy Smith","David Boy Smith","The British Bulldog","The Bulldog","The British Beef"],
    "same_as":["https://en.wikipedia.org/wiki/Davey_Boy_Smith"],
    "memorial_notice":'Davey Boy Smith (November 27, 1962 – May 18, 2002). The British Bulldog died at age 39 from a heart attack while on vacation in British Columbia. He is remembered as one of the greatest UK exports in wrestling history.',
    "faq_schema":[
        {"q":"What is British Bulldog's real name?","a":"David Boy Smith, born November 27, 1962 in Golborne, Lancashire, England. He died on May 18, 2002, aged 39."},
        {"q":"What was British Bulldog's most famous match?","a":"SummerSlam 1992 at Wembley Stadium — an IC title match against Bret Hart in front of 80,000 fans. The crowd was entirely behind Bulldog as the local hero, and he won with a running powerslam to universal celebrations."},
        {"q":"Was British Bulldog part of the Hart Foundation?","a":"Yes — Davey Boy Smith married Diana Hart (Bret's sister) and was part of the Hart wrestling family. He was a member of the reformed Hart Foundation in 1997 alongside Bret, Owen, Jim Neidhart, and Brian Pillman."},
    ],
    "subnav":["record","championships","timeline","signature","rivalries","faq"],
    "rec_stats":[
        {"n":"2","sub":"×","l":"Intercontinental Championships","gold":True},
        {"n":"1","sub":"×","l":"European Championship"},
        {"n":"6","sub":"×","l":"Tag Team Championships"},
        {"n":"1992","sub":"","l":"Wembley Stadium — 80,000 fans"},
    ],
    "wl_strip":[True,False,True,True,False,True,True,False,True,True],
    "tab_id":"bulldog",
    "tab1_count":"10",
    "tab2_count":"0–0",
    "filters":[
        {"label":"All","key":"all","count":"10"},
        {"label":"Wins","key":"wins","count":"6"},
        {"label":"Losses","key":"losses","count":"4"},
        {"label":"Title matches","key":"title","count":"6"},
    ],
    "main_rows":bulldog_rows,
    "wm_rows":[],
    "ppv_rows":[],
    "method_title":"Running Powerslam — Britain's finishing move",
    "method_intro":"The Running Powerslam was Davey Boy Smith's calling card — he would scoop an opponent, run across the ring, and drive them into the mat. At Wembley 1992, it finished Bret Hart to the delight of 80,000 British fans. His strength was genuine and his powerslam was legitimately one of the most impactful-looking moves in the business.",
    "method_bars":[
        {"label":"Running Powerslam → pin","n":"4","pct":67},
        {"label":"Pinfall (over-the-shoulder slam / other)","n":"1","pct":17},
        {"label":"DQ / countout","n":"1","pct":16},
    ],
    "pull_facts":[
        {"n":"Wembley 1992","l":"SummerSlam 1992 at Wembley Stadium — 80,000 fans, the largest WWF crowd in UK history, all cheering for Davey Boy to beat Bret Hart. He did."},
        {"n":"Hart family","l":"Married Diana Hart (Bret's sister) — a genuine member of wrestling's most accomplished family dynasty."},
        {"n":"British Bulldogs","l":"As part of The British Bulldogs with Dynamite Kid, he was one of the WWF's best tag teams (1985–1988) — athletic, fast and powerful."},
    ],
    "champ_title":"IC, European and six tag reigns",
    "champ_badge":"2× IC Champion",
    "champ_rows_html":"""      <div><span class="k">1992</span><span>WWF Intercontinental Championship — def. <a href="/wrestlers/bret-hart/">Bret Hart</a> at SummerSlam 1992, Wembley Stadium (1st reign)</span></div>
      <div><span class="k">1997</span><span>WWF Intercontinental Championship — 2nd reign during Hart Foundation era</span></div>
      <div><span class="k">1997</span><span>WWF European Championship — def. Shawn Michaels at One Night Only (UK PPV)</span></div>
      <div><span class="k">1985–1988</span><span>WWF Tag Team Championships × 2 (British Bulldogs — w/ Dynamite Kid)</span></div>
      <div><span class="k">1992–1997</span><span>WWF Tag Team Championships × 4 — with various partners incl. Owen Hart, Lex Luger, and others</span></div>
      <div><span class="k">1997</span><span>WCW World Tag Team Championship — brief WCW run with various partners</span></div>
""",
    "timeline_items":[
        {"time":"1983–1984","h":"Learning the craft — UK scene","p":"Trained by his uncle Tom Billington (Dynamite Kid) on the UK wrestling circuit before joining WWF."},
        {"time":"1985–1988","h":"The British Bulldogs — tag gold","p":"With Dynamite Kid as The British Bulldogs — one of the finest tag teams in WWF history. WWF Tag Champions; work rate and athleticism that set a new standard."},
        {"time":"1988–1992","h":"Singles push &amp; Wembley","p":"Went singles; multiple IC title shots. The SummerSlam 1992 IC title win at Wembley before 80,000 fans remains his career peak."},
        {"time":"1992–1997","h":"Hart Foundation — family values","p":"Multiple tag title reigns; core member of the 1997 Hart Foundation with <a href='/wrestlers/bret-hart/'>Bret</a>, <a href='/wrestlers/owen-hart/'>Owen</a>, Brian Pillman and Jim Neidhart. The European Championship win in the UK."},
        {"time":"1998–2002","h":"Final years &amp; WCW","p":"Brief WCW run (1998–1999); returned to the independents. Died on May 18, 2002, aged 39, from a heart attack."},
    ],
    "sig_matches":[
        {"href":"/matches/bret-vs-bulldog-ss92/","initials":"SS92","title":"vs Bret Hart — SummerSlam 1992 (IC Title)","rating":5},
        {"href":"/matches/bulldog-vs-hbk-one-night-only/","initials":"ONO","title":"vs Shawn Michaels — One Night Only 1997 (European)","rating":4},
        {"href":"/matches/british-bulldogs-vs-dream-team/","initials":"WM2","title":"British Bulldogs vs Dream Team — WrestleMania 2","rating":4},
    ],
    "rivalries_html":'    <a href="/wrestlers/bret-hart/">Bret Hart</a>\n    <a href="/wrestlers/shawn-michaels/">Shawn Michaels</a>\n    <a href="/wrestlers/stone-cold-steve-austin/">Steve Austin</a>\n    <a href="/wrestlers/owen-hart/">Owen Hart (tag partner)</a>\n',
    "relationships_html":'    <div class="rel"><div><span class="rel__type">Brother-in-law &amp; tag partner</span><br><a href="/wrestlers/owen-hart/">Owen Hart</a></div></div>\n    <div class="rel"><div><span class="rel__type">Hart family member (married Diana Hart)</span><br><a href="/wrestlers/bret-hart/">Bret Hart</a></div></div>\n    <div class="rel"><div><span class="rel__type">British Bulldogs partner</span><br>Dynamite Kid (Tom Billington)</div></div>\n',
    "tv_items":[
        {"initials":"WWE","title":"British Bulldogs — Tag Team History","year":"Various","desc":"WWE Network archival content featuring The British Bulldogs' best tag matches from 1985–1988"},
    ],
    "podcast_items":[
        {"title":"Something to Wrestle — British Bulldog episode","desc":"Bruce Prichard and Conrad Thompson on the SummerSlam 1992 match and Davey Boy's career"},
    ],
    "faqs":[
        {"q":"What is British Bulldog's most famous match?","a":"SummerSlam 1992 at Wembley Stadium — IC title vs Bret Hart before 80,000 fans. He won with the Running Powerslam.","open":True},
        {"q":"Was Bulldog part of the Hart family?","a":"Yes — he married Diana Hart (Bret's sister) and was a legitimate Hart family member, becoming part of the legendary Hart wrestling dynasty."},
        {"q":"How did Davey Boy Smith die?","a":"He died on May 18, 2002, aged 39, from a heart attack while on vacation in Invermere, British Columbia, Canada."},
    ],
    "related_links":[
        {"href":"/wrestlers/bret-hart/","label":"Bret Hart"},
        {"href":"/wrestlers/owen-hart/","label":"Owen Hart"},
        {"href":"/wrestlers/shawn-michaels/","label":"Shawn Michaels"},
        {"href":"/matches/bret-vs-bulldog-ss92/","label":"SummerSlam 1992 (★★★★★)"},
    ],
    "bg_gradient":"linear-gradient(150deg,color-mix(in oklab,#1a3a1a 55%,#000),#0c0d10 62%)",
    "facts_html":"""        <li><b>Real name</b> David Boy Smith</li>
        <li><b>Born</b> November 27, 1962 · Golborne, Lancashire, England</li>
        <li><b>Died</b> May 18, 2002 · Invermere, BC, Canada</li>
        <li><b>Promotions</b> WWF / WCW / UK scene</li>
        <li><b>Finisher</b> Running Powerslam</li>
        <li><b>Tag team</b> British Bulldogs (w/ Dynamite Kid) · Hart Foundation</li>
""",
})

# ── CHRIS JERICHO ────────────────────────────────────────────────────────────
jericho_rows=[
    row(W,"title","The Rock &amp; Steve Austin (tag partner: Benoit)","Raw is War","2001","Undisputed WWF Title <span class='title-tag'>1st undisputed champion</span>","Jericho wins — first-ever Undisputed WWF Champ"),
    row(L,"wrestlemania title",a("triple-h","Triple H")+" <span class='title-tag'>Title</span>","WrestleMania X8","2002","Undisputed Title","Pedigree → pin"),
    row(W,"wrestlemania",a("shawn-michaels","Shawn Michaels"),"WrestleMania XIX","2003","Singles","Walls of Jericho → submission"),
    row(L,"wrestlemania",a("stone-cold-steve-austin","Steve Austin")+" &amp; "+a("triple-h","Triple H"),"Raw is War","2001","Tag (w/ Benoit) vs Power Trip — WWF Tag Titles","Won! Beat the Power Trip"),
    row(W,"title",a("stone-cold-steve-austin","Steve Austin")+" <span class='title-tag'>Title</span>","Raw is War","2001","WWF Championship","Won (with Benoit) from Power Trip (Austin's quad injury during match)"),
    row(L,"title","Chris Benoit (partner switch)","Judgment Day","2001","WWF Tag Titles","Benoit vs Jericho imploded"),
    row(W,"title","Rey Mysterio <span class='title-tag'>Title</span>","WrestleMania 25","2009","World Heavyweight Title","Codebreaker → pin <span class='title-tag'>WH title</span>"),
    row(L,"title",a("cm-punk","CM Punk")+" <span class='title-tag'>Title</span>","WrestleMania 28","2012","World Heavyweight Title","GTS → pin"),
    row(W,"",a("shawn-michaels","Shawn Michaels"),"Unforgiven","2008","Singles","Codebreaker → pin (HBK feud)"),
    row(L,"wrestlemania",a("randy-orton","Randy Orton"),"WrestleMania 27","2011","Singles","RKO → pin"),
    row(W,"title","Various (AEW)","AEW Full Gear","2019","AEW Championship","Judas Effect → pin (1st AEW Champ)"),
]
wrestlers.append({
    "slug":"chris-jericho",
    "name":"Chris Jericho",
    "initials":"Y2J",
    "title_tag":"Chris Jericho — Y2J, Walls of Jericho &amp; Career Record | MAT",
    "description":"Chris Jericho: complete profile — first Undisputed WWF Champion, 9× IC Champion, WrestleMania classics with HBK, AEW's founding champion, and the most reinvented performer in the sport's history.",
    "answer":"<strong>Chris Jericho — Y2J — is the most reinvented performer in the history of professional wrestling, a man who has stayed relevant and great across five decades by never stopping evolving.</strong> He became the first-ever Undisputed WWF Champion in 2001, delivered WrestleMania classics with Shawn Michaels, and then crossed to AEW in 2019 where he became their first champion and reinvented himself as Le Champion, the Demo God, and the Ocho.",
    "era":"1990–present",
    "promo_chip":'<span class="chip chip--wwe">WWF / WWE / AEW</span>',
    "alt_names":["Christopher Keith Irvine","Y2J","The Ayatollah of Rock 'n' Rolla","The First-Ever Undisputed Champion","Le Champion","The Demo God","The Ocho","Lionheart"],
    "same_as":["https://en.wikipedia.org/wiki/Chris_Jericho","https://www.wikidata.org/wiki/Q705513"],
    "faq_schema":[
        {"q":"Who was the first Undisputed WWF Champion?","a":"Chris Jericho became the first-ever Undisputed WWF Champion on December 9, 2001, when he defeated both The Rock and Steve Austin on the same Raw episode to unify the WWF and WCW titles."},
        {"q":"What is the Walls of Jericho?","a":"Chris Jericho's signature submission — a modified Boston Crab with a higher angle, targeting the back and legs. He later added the Liontamer version (stepping on the neck/head) in his more aggressive AEW run."},
        {"q":"How long has Chris Jericho been wrestling?","a":"Chris Jericho has been wrestling since 1990 — over three decades, making him the longest-active top-level performer in the history of the sport. He continues to compete at the highest level in AEW."},
    ],
    "subnav":["record","championships","timeline","signature","rivalries","relationships","faq"],
    "rec_stats":[
        {"n":"6","sub":"×","l":"WWF/WWE World titles","gold":True},
        {"n":"9","sub":"×","l":"IC Championship (record)","gold":True},
        {"n":"4","sub":"×","l":"AEW World Champion"},
        {"n":"1","sub":"st","l":"Undisputed WWF Champion (2001)"},
    ],
    "wl_strip":[True,False,True,True,False,True,True,False,True,True,False,True],
    "tab_id":"jericho",
    "tab1_count":"11",
    "tab2_count":"1–2",
    "filters":[
        {"label":"All","key":"all","count":"11"},
        {"label":"Wins","key":"wins","count":"7"},
        {"label":"Losses","key":"losses","count":"4"},
        {"label":"WrestleMania","key":"wrestlemania","count":"4"},
        {"label":"Title matches","key":"title","count":"7"},
    ],
    "main_rows":jericho_rows,
    "wm_rows":[
        row(W,"wrestlemania",a("shawn-michaels","Shawn Michaels"),"WrestleMania XIX","2003","Singles","Walls of Jericho → submission"),
        row(L,"wrestlemania title",a("triple-h","Triple H"),"WrestleMania X8","2002","Undisputed Title","Pedigree → pin"),
        row(L,"wrestlemania",a("cm-punk","CM Punk"),"WrestleMania 28","2012","WHC match","GTS → pin"),
        row(L,"wrestlemania",a("randy-orton","Randy Orton"),"WrestleMania 27","2011","Singles","RKO → pin"),
    ],
    "ppv_rows":[],
    "method_title":"Walls of Jericho and the Codebreaker — a two-era arsenal",
    "method_intro":"In his WWF/WWE peak it was the Walls of Jericho (elevated Boston Crab) and the Lionsault. In AEW and his modern run it became the Codebreaker and the Judas Effect. Few wrestlers have successfully reinvented their in-ring arsenal alongside their character.",
    "method_bars":[
        {"label":"Walls of Jericho → submission","n":"3","pct":43},
        {"label":"Codebreaker → pin","n":"2","pct":29},
        {"label":"Lionsault → pin","n":"1","pct":14},
        {"label":"Judas Effect → pin","n":"1","pct":14},
    ],
    "pull_facts":[
        {"n":"First Undisputed Champ","l":"December 9, 2001 — Jericho unified the WWF and WCW titles in a single night by beating The Rock AND Steve Austin on the same Raw."},
        {"n":"AEW founding champion","l":"Crossed to AEW in 2019 — their first world champion, helping launch the company's credibility. Multiple reigns since."},
        {"n":"Fozzy","l":"Jericho fronts the rock band Fozzy — a genuine touring act. 'Judas' became his AEW entrance theme and a legitimate rock track."},
    ],
    "champ_title":"First Undisputed champion, 6× WWE/WWF, 4× AEW",
    "champ_badge":"6× WWF/WWE World Champion",
    "champ_rows_html":"""      <div><span class="k">1999</span><span>WWF Intercontinental Championship — multiple reigns; 9 total IC reigns (a record at the time)</span></div>
      <div><span class="k">2001</span><span>WWF/WCW Undisputed Championship — def. The Rock and Steve Austin on same night <span class="dim">(first-ever Undisputed WWF Champion)</span></span></div>
      <div><span class="k">2002–2003</span><span>WWF/Undisputed Championship — reigns through the transition to brand split</span></div>
      <div><span class="k">2008–2009</span><span>World Heavyweight Championship — two reigns during his HBK rivalry and Save_Us.222 return</span></div>
      <div><span class="k">2010</span><span>WWE Championship — reign during the Nexus/Miz era</span></div>
      <div><span class="k">2019–present</span><span>AEW World Championship × 4 — founding AEW champion; multiple reigns as Le Champion, Demo God, Ocho</span></div>
""",
    "champ_note":"Also 9× Intercontinental Champion (a WWE record at the time), 2× WCW Cruiserweight Champion, 4× AEW World Champion, and first-ever Undisputed WWF Champion.",
    "timeline_items":[
        {"time":"1990–1996","h":"Lionheart — learning the world","p":"Started as Lionheart; worked in Japan (WAR, Frontier Martial-Arts), Mexico (CMLL), ECW and WCW. The global education made him the most versatile worker of his generation."},
        {"time":"1996–1999","h":"WCW — Jericho vs the political machine","p":"A fan favourite in WCW but deliberately denied a main-event push due to politics. His comedy feud with Dean Malenko and the Ayatollah of Rock 'n' Rolla character built massive fan support."},
        {"time":"1999–2001","h":"WWF debut — Y2J","p":"The Raw countdown — August 9, 1999 — is one of the great debut segments. Became the first-ever Undisputed WWF Champion in December 2001 by unifying the company's belts in a single night."},
        {"time":"2001–2008","h":"WWE — multiple reinventions","p":"Six world title reigns; WM classics with <a href='/wrestlers/shawn-michaels/'>HBK</a>; the Save_Us.222 return; reliable top-of-card performer through multiple character evolutions."},
        {"time":"2019–present","h":"AEW — founding champion, Le Champion, the Ocho","p":"Crossed to AEW as a founding star and their first world champion; multiple reinventions as Le Champion, Demo God (with MJF and Inner Circle), and the Ocho. Still competing at a world-class level."},
    ],
    "sig_matches":[
        {"href":"/matches/jericho-vs-hbk-wm19/","initials":"WM19","title":"vs Shawn Michaels — WrestleMania XIX","rating":4.5},
        {"href":"/matches/jericho-hbk-ladder/","initials":"LC08","title":"vs Shawn Michaels — ladder match (No Mercy 2008)","rating":4.5},
        {"href":"/matches/jericho-vs-mjf/","initials":"AEW","title":"vs MJF — AEW Revolution 2022","rating":5},
        {"href":"/matches/jericho-first-undisputed/","initials":"RAW","title":"First-ever Undisputed WWF Champion — Raw 2001","rating":4},
    ],
    "rivalries_html":'    <a href="/wrestlers/shawn-michaels/">Shawn Michaels</a>\n    <a href="/wrestlers/triple-h/">Triple H</a>\n    <a href="/wrestlers/stone-cold-steve-austin/">Steve Austin (tag titles)</a>\n    <a href="/wrestlers/cm-punk/">CM Punk</a>\n    <a href="/wrestlers/randy-orton/">Randy Orton</a>\n    <a href="/wrestlers/the-rock/">The Rock</a>\n',
    "relationships_html":'    <div class="rel"><div><span class="rel__type">AEW alliance (then feud)</span><br>MJF</div></div>\n    <div class="rel"><div><span class="rel__type">Career-defining rival</span><br><a href="/wrestlers/shawn-michaels/">Shawn Michaels</a></div></div>\n    <div class="rel"><div><span class="rel__type">Inner Circle</span><br>Sammy Guevara, Santana, Ortiz, Jake Hager</div></div>\n',
    "tv_items":[
        {"initials":"WWE","title":"Chris Jericho: Breaking the Code","year":"2010","desc":"WWE Home Video career retrospective — his WCW, ECW and WWF runs in depth"},
        {"initials":"AEW","title":"Being The Elite (AEW YouTube)","year":"2019–","desc":"AEW's documentary web series — Jericho features prominently as founding AEW star"},
    ],
    "podcast_items":[
        {"title":"Talk Is Jericho","desc":"Jericho's long-running podcast — one of wrestling's most popular, covering music, wrestling history and pop culture"},
    ],
    "faqs":[
        {"q":"Who was the first Undisputed WWF Champion?","a":"Chris Jericho — on December 9, 2001, he defeated The Rock and Steve Austin on the same Raw episode to unify the titles.","open":True},
        {"q":"What is the Walls of Jericho?","a":"An elevated Boston Crab submission — Jericho faces away from the downed opponent, folds their legs over his thighs, and leans back. The Liontamer version adds stepping on the head."},
        {"q":"Why did Jericho leave WWE for AEW?","a":"He was the highest-profile free agent when AEW launched in 2019, and chose to sign with the upstart promotion as their first world champion — a statement signing that gave AEW instant credibility."},
    ],
    "related_links":[
        {"href":"/wrestlers/shawn-michaels/","label":"Shawn Michaels"},
        {"href":"/wrestlers/triple-h/","label":"Triple H"},
        {"href":"/wrestlers/stone-cold-steve-austin/","label":"Steve Austin"},
        {"href":"/wrestlers/cm-punk/","label":"CM Punk"},
        {"href":"/wrestlers/the-rock/","label":"The Rock"},
    ],
    "bg_gradient":"linear-gradient(150deg,color-mix(in oklab,#2a1a3a 55%,#000),#0c0d10 62%)",
    "facts_html":"""        <li><b>Real name</b> Christopher Keith Irvine</li>
        <li><b>Born</b> November 9, 1970 · Manhasset, NY (raised Winnipeg, Manitoba)</li>
        <li><b>Promotions</b> WCW · ECW · WWF/WWE · AEW (2019–present)</li>
        <li><b>Finisher</b> Walls of Jericho, Codebreaker, Judas Effect</li>
        <li><b>Band</b> Fozzy (vocalist since 1999)</li>
        <li><b>Hall of Fame</b> Eligible — not yet inducted</li>
""",
})

# WRITE
for w in wrestlers:
    html=build_page(w)
    path=os.path.join(BASE,w["slug"],"index.html")
    os.makedirs(os.path.dirname(path),exist_ok=True)
    with open(path,"w") as f:
        f.write(html)
    print(f"✅ {w['slug']} — {html.count(chr(10))} lines")

print("\nBatch 1b complete.")
