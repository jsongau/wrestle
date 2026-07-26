#!/usr/bin/env python3
"""Generate gold-standard wrestler profile pages — Batch 1a (The Rock, Bret Hart, Triple H, Kane, Mick Foley)."""

import os

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

def chip(label, cls=""):
    return f'<span class="chip{" "+cls if cls else ""}">{label}</span>'

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
    alt_names = w["alt_names"]  # list of strings
    same_as = w["same_as"]  # list of strings
    faq_schema = w["faq_schema"]  # list of {q, a}
    subnav = w.get("subnav", ["record","championships","timeline","signature","rivalries","faq"])
    rec_stats = w["rec_stats"]  # list of {n, sub, l, gold?}
    wl_strip = w["wl_strip"]  # list of True/False (True=win, False=loss)
    record_notice = w.get("record_notice", f"A curated ledger of <strong>{name}'s</strong> most significant matches — title bouts, WrestleMania appearances and landmark moments. Not a complete career record; cross-checked against WWE.com, Wikipedia and Cagematch.")
    tab1_label = w.get("tab1_label", "Landmark ledger")
    tab1_count = w.get("tab1_count", "")
    tab2_label = w.get("tab2_label", "WrestleMania")
    tab2_count = w.get("tab2_count", "")
    tab3_label = w.get("tab3_label", "PPV / PLE")
    tab3_count = w.get("tab3_count", "")
    tab_id = w["tab_id"]  # short prefix like "rock", "bret"
    filters = w["filters"]  # list of {label, key, count}
    main_rows = w["main_rows"]  # list of {result, cats, opponent_html, event, date, stip, finish}
    wm_rows = w.get("wm_rows", [])
    ppv_rows = w.get("ppv_rows", [])
    method_bars = w["method_bars"]  # list of {label, n, pct}
    method_intro = w["method_intro"]
    method_title = w["method_title"]
    pull_facts = w["pull_facts"]  # list of {n, l}
    champ_title = w["champ_title"]
    champ_badge = w["champ_badge"]
    champ_rows_html = w["champ_rows_html"]
    champ_note = w.get("champ_note", "")
    timeline_items = w["timeline_items"]  # list of {time, h, p}
    personas = w.get("personas", [])  # list of {name, slug, era, desc}
    sig_matches = w["sig_matches"]  # list of {href, initials, title, rating}
    rivalries_html = w["rivalries_html"]
    relationships_html = w["relationships_html"]
    tv_items = w.get("tv_items", [])  # list of {img, title, year, desc, href}
    podcast_items = w.get("podcast_items", [])
    faqs = w["faqs"]  # list of {q, a, open?}
    related_links = w["related_links"]  # list of {href, label}
    bg_gradient = w.get("bg_gradient", "linear-gradient(150deg,color-mix(in oklab,var(--c-gold) 35%,#000),#0c0d10 62%)")
    eyebrow_text = w.get("eyebrow_text", "The Career Ledger")
    record_heading = w.get("record_heading", f"The record of {name}")
    color_accent = w.get("color_accent", "var(--c-gold)")
    personas_eyebrow = w.get("personas_eyebrow", "Personas &amp; alter egos")
    personas_heading = w.get("personas_heading", "Many names, one legend")

    # JSON-LD
    alt_names_json = ", ".join(f'"{n}"' for n in alt_names)
    same_as_json = ", ".join(f'"{s}"' for s in same_as)
    faq_schema_json = ",\n ".join(
        '{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'.format(q=f["q"].replace('"', '&quot;'), a=f["a"].replace('"', '&quot;'))
        for f in faq_schema
    )

    # wl strip
    strip_items = "".join('<i class="l"></i>' if not r else '<i></i>' for r in wl_strip)
    wins = sum(1 for r in wl_strip if r)
    losses = sum(1 for r in wl_strip if not r)
    strip_label = f"{wins} wins and {losses} losses"

    # filters
    filter_btns = "".join(
        f'    <button type="button" data-filter="{f["key"]}" aria-pressed="{"true" if f["key"]=="all" else "false"}">{f["label"]} <span class="cnt">{f["count"]}</span></button>\n'
        for f in filters
    )

    # main table rows
    def make_row(r, mobile=False):
        res_class = "res-w" if r["result"] == "W" else "res-l"
        res_word = "in" if r["result"] == "W" else "oss"
        if mobile:
            return (
                f'<li class="fight-row-card" data-result="{r["result"]}" data-cats="{r["cats"]}">'
                f'<div class="frc-top"><span class="res {res_class}">{r["result"]}<span class="sr-only">{res_word}</span></span>'
                f'<span class="frc-opp">{r["opponent_html"]}</span></div>'
                f'<p class="frc-line">{r["event"]} <span class="sep">·</span> {r["date"]}</p>'
                f'<p class="frc-line">{r["stip"]} · {r["finish"]}</p>'
                f'</li>\n'
            )
        else:
            return (
                f'      <tr class="record-row" data-result="{r["result"]}" data-cats="{r["cats"]}">'
                f'<td><span class="res {res_class}">{r["result"]}<span class="sr-only">{res_word}</span></span></td>'
                f'<td>{r["opponent_html"]}</td>'
                f'<td>{r["event"]}</td>'
                f'<td class="dim">{r["date"]}</td>'
                f'<td>{r["stip"]}</td>'
                f'<td>{r["finish"]}</td>'
                f'</tr>\n'
            )

    desktop_rows = "".join(make_row(r) for r in main_rows)
    mobile_cards = "".join(make_row(r, mobile=True) for r in main_rows)

    # wm rows
    wm_desktop = "".join(make_row(r) for r in wm_rows)
    wm_mobile = "".join(make_row(r, mobile=True) for r in wm_rows)
    wm_wins = sum(1 for r in wm_rows if r["result"] == "W")
    wm_losses = sum(1 for r in wm_rows if r["result"] == "L")

    # ppv rows
    ppv_desktop = "".join(make_row(r) for r in ppv_rows)

    # rec stats
    rec_stats_html = ""
    for st in rec_stats:
        gold_class = " is-gold" if st.get("gold") else ""
        sub = f'<span class="sub">{st["sub"]}</span>' if st.get("sub") else ""
        id_attr = f' id="{st["id"]}"' if st.get("id") else ""
        rec_stats_html += f'    <div class="rec-stat{gold_class}"{id_attr}><div class="n">{st["n"]}{sub}</div><div class="l">{st["l"]}</div></div>\n'

    # subnav
    subnav_labels = {
        "record": "Record", "championships": "Championships", "timeline": "Career",
        "personas": "Personas", "signature": "Signature matches", "rivalries": "Rivalries",
        "relationships": "Relationships", "media": "Media", "podcasts": "Podcasts", "faq": "FAQ"
    }
    subnav_html = "".join(f'  <li><a href="#{s}">{subnav_labels.get(s, s.title())}</a></li>\n' for s in subnav)

    # method bars
    bars_html = ""
    for b in method_bars:
        bars_html += f'        <div class="mb-row"><div class="mb-head"><span>{b["label"]}</span><span class="v">{b["n"]}</span></div><div class="mb-track" role="img" aria-label="{b["label"]}: {b["n"]}"><div class="mb-fill" style="--w:{b["pct"]}%"></div></div></div>\n'

    # pull facts
    pull_html = "".join(f'      <div><p class="n">{p["n"]}</p><p class="l">{p["l"]}</p></div>\n' for p in pull_facts)

    # champ rows
    # champ_rows_html is pre-built

    # timeline
    timeline_html = ""
    for t in timeline_items:
        timeline_html += f'    <li><time>{t["time"]}</time><h3 style="font-size:var(--fs-500)">{t["h"]}</h3><p class="muted">{t["p"]}</p></li>\n'

    # personas
    personas_section = ""
    if personas:
        cards_html = ""
        for p in personas:
            href = f'/wrestlers/{p["slug"]}/'
            cards_html += f'    <a class="persona" href="{href}"><span class="era">{p["era"]}</span><h4>{p["name"]}</h4><p>{p["desc"]}</p></a>\n'
        personas_section = f"""
<!-- PERSONAS -->
<section class="section" id="personas"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">{personas_eyebrow}</p><h2>{personas_heading}</h2><hr class="rule-gold"></div></div>
  <div class="persona-grid" data-reveal>
{cards_html}  </div>
</div></section>
"""

    # signature matches
    sig_html = ""
    for m in sig_matches:
        stars = "★" * int(m["rating"]) + ("½" if m["rating"] % 1 else "")
        sig_html += f'      <article class="card"><a class="card__media" href="{m["href"]}"><span class="card__initials">{m["initials"]}</span></a><div class="card__body"><h3 class="card__title"><a class="card__link" href="{m["href"]}">{m["title"]}</a></h3><div class="rating" style="--rating:{m["rating"]}"><span class="rating__stars" aria-hidden="true">{"★"*5}</span></div></div></article>\n'

    # TV / media
    tv_section = ""
    if tv_items:
        items_html = ""
        for t in tv_items:
            items_html += f'    <div class="media-item"><div class="mi-thumb"><span>{t["initials"]}</span></div><div class="mi-body"><h4>{t["title"]}</h4><p class="muted">{t["year"]} · {t["desc"]}</p></div></div>\n'
        tv_section = f"""
<section class="section" id="media" style="background:var(--c-bg-elev-1);border-block:1px solid var(--c-line)"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Documentaries &amp; shows</p><h2>Beyond the ring</h2><hr class="rule-gold"></div></div>
  <div class="media-rail" data-reveal>
{items_html}  </div>
</div></section>
"""

    # podcasts
    pod_section = ""
    if podcast_items:
        items_html = ""
        for p in podcast_items:
            items_html += f'    <div class="media-item"><div class="mi-thumb" style="background:var(--c-bg-elev-2)"><span style="font-size:1.4rem">🎙</span></div><div class="mi-body"><h4>{p["title"]}</h4><p class="muted">{p["desc"]}</p></div></div>\n'
        pod_section = f"""
<section class="section" id="podcasts"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Podcasts &amp; audio</p><h2>Hear him out</h2><hr class="rule-gold"></div></div>
  <div class="media-rail" data-reveal>
{items_html}  </div>
</div></section>
"""

    # faqs
    faq_html = ""
    for f in faqs:
        open_attr = " open" if f.get("open") else ""
        faq_html += f'    <details{open_attr}><summary>{f["q"]}</summary><div class="faq__body">{f["a"]}</div></details>\n'

    # related
    rel_html = "".join(f'    <a href="{r["href"]}">{r["label"]}</a>\n' for r in related_links)

    # WM tab section
    wm_section = ""
    if wm_rows:
        wm_section = f"""
 <div class="tab-panel" id="tab-{tab_id}-wm" role="tabpanel" aria-labelledby="tb-{tab_id}-wm" hidden>
  <div class="tab-summary"><span class="ts">{wm_wins}–{wm_losses}<small>WrestleMania record</small></span><span class="ts">{len(wm_rows)}<small>WM appearances</small></span></div>
  <div class="record-scroll"><table class="record"><thead><tr><th>Result</th><th>Opponent</th><th>Event</th><th>Date</th><th>Stipulation</th><th>Finish</th></tr></thead><tbody>
{wm_desktop}  </tbody></table></div>
  <p class="scroll-hint">↕ Scroll · WrestleMania record only.</p>
 </div>"""

    ppv_section = ""
    if ppv_rows:
        ppv_section = f"""
 <div class="tab-panel" id="tab-{tab_id}-ppv" role="tabpanel" aria-labelledby="tb-{tab_id}-ppv" hidden>
  <div class="record-scroll"><table class="record"><thead><tr><th>Result</th><th>Opponent</th><th>Event</th><th>Date</th><th>Stipulation</th><th>Finish</th></tr></thead><tbody>
{ppv_desktop}  </tbody></table></div>
  <p class="scroll-hint">↕ Scroll · curated PPV / PLE record.</p>
 </div>"""

    wm_tab_btn = ""
    ppv_tab_btn = ""
    if wm_rows:
        wm_tab_btn = f'  <button role="tab" id="tb-{tab_id}-wm" aria-controls="tab-{tab_id}-wm" aria-selected="false" tabindex="-1">{tab2_label} <span class="tcount">{tab2_count or f"{wm_wins}–{wm_losses}"}</span></button>\n'
    if ppv_rows:
        ppv_tab_btn = f'  <button role="tab" id="tb-{tab_id}-ppv" aria-controls="tab-{tab_id}-ppv" aria-selected="false" tabindex="-1">{tab3_label} <span class="tcount">{tab3_count}</span></button>\n'

    tab_label_attr = f'{name} record views'

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<script>document.documentElement.classList.add('js')</script>
<title>{title_tag} | MAT</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://wrestlelore.com/wrestlers/{slug}/">
<link rel="alternate" hreflang="en" href="https://wrestlelore.com/wrestlers/{slug}/">
<link rel="alternate" hreflang="x-default" href="https://wrestlelore.com/wrestlers/{slug}/">
<meta property="og:type" content="profile">
<meta property="og:site_name" content="MAT — Pro Wrestling Database">
<meta property="og:title" content="{title_tag}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="https://wrestlelore.com/wrestlers/{slug}/">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0a0b0d">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Oswald:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/site.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Person","@id":"https://wrestlelore.com/wrestlers/{slug}/#person","name":"{name}","alternateName":[{alt_names_json}],"url":"https://wrestlelore.com/wrestlers/{slug}/","jobTitle":"Professional Wrestler","sameAs":[{same_as_json}]}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
 {{"@type":"ListItem","position":1,"name":"Home","item":"https://wrestlelore.com/"}},
 {{"@type":"ListItem","position":2,"name":"Wrestlers","item":"https://wrestlelore.com/wrestlers/"}},
 {{"@type":"ListItem","position":3,"name":"{name}","item":"https://wrestlelore.com/wrestlers/{slug}/"}}]}}
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

<!-- HERO -->
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

<!-- SUB-NAV -->
<nav class="subnav-page" aria-label="On this page"><div class="wrap"><ul>
{subnav_html}</ul></div></nav>

<!-- RECORD -->
<section class="section" id="record"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">{eyebrow_text}</p><h2>{record_heading}</h2><hr class="rule-gold"></div></div>
  <div class="rec-summary" data-reveal>
{rec_stats_html}  </div>
  <div class="wl-strip" role="img" aria-label="Career ledger outcomes: {strip_label}">{strip_items}</div>
  <p class="wl-cap" data-reveal>Each square is one bout in the curated ledger · <span style="color:var(--c-win)">■</span> win <span style="color:var(--c-loss)">■</span> loss.</p>
  <p class="notice" style="margin-top:var(--sp-4)" data-reveal>{record_notice}</p>
  <div class="engage" data-reveal style="margin-top:var(--sp-4)">
    <h3>Rate {name}</h3>
    <div class="row">
      <fieldset class="rate"><legend class="sr-only">Rate {name} all-time</legend>
        <input type="radio" id="{tab_id}r5" name="{tab_id}stars" value="5"><label for="{tab_id}r5" aria-label="5 stars">★</label>
        <input type="radio" id="{tab_id}r4" name="{tab_id}stars" value="4"><label for="{tab_id}r4" aria-label="4 stars">★</label>
        <input type="radio" id="{tab_id}r3" name="{tab_id}stars" value="3"><label for="{tab_id}r3" aria-label="3 stars">★</label>
        <input type="radio" id="{tab_id}r2" name="{tab_id}stars" value="2"><label for="{tab_id}r2" aria-label="2 stars">★</label>
        <input type="radio" id="{tab_id}r1" name="{tab_id}stars" value="1"><label for="{tab_id}r1" aria-label="1 star">★</label>
      </fieldset>
      <span class="muted">How do you rank them all-time?</span>
      <span class="done">Saved! <a href="/membership/">Join free to lock it in →</a></span>
    </div>
    <div class="row">
      <button type="button" class="chip-btn" onclick="location.href='/membership/'">★ Follow {name}</button>
    </div>
  </div>
  <div class="tabs" data-reveal>
 <div class="tab-btns" role="tablist" aria-label="{tab_label_attr}">
  <button role="tab" id="tb-{tab_id}-all" aria-controls="tab-{tab_id}-all" aria-selected="true">{tab1_label} <span class="tcount">{tab1_count}</span></button>
{wm_tab_btn}{ppv_tab_btn} </div>
 <div class="tab-panel" id="tab-{tab_id}-all" role="tabpanel" aria-labelledby="tb-{tab_id}-all">
  <div class="rt-filters" role="group" aria-label="Filter the record" data-record-filter="#{tab_id}table" data-record-count="#{tab_id}count">
{filter_btns}  </div>
  <p class="rt-count" aria-live="polite">Showing <span id="{tab_id}count">{filters[0]["count"]}</span> of {filters[0]["count"]} landmark bouts.</p>
  <div id="{tab_id}table"><div class="record-scroll"><div class="table-wrap record-desktop"><table class="record">
    <thead><tr><th>Result</th><th>Opponent</th><th>Event</th><th>Date</th><th>Stipulation</th><th>Finish</th></tr></thead>
    <tbody>
{desktop_rows}    </tbody>
  </table></div></div><ol class="record-mobile" aria-label="{name} match record, as cards">
{mobile_cards}</ol></div>
  <p class="scroll-hint">↕ Scroll inside the table · use the filters to narrow it.</p>
 </div>
{wm_section}
{ppv_section}
</div>
</div></section>

<!-- FINISHES -->
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

<!-- CHAMPIONSHIPS -->
<section class="section" id="championships"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Championships &amp; lineage</p><h2>{champ_title}</h2><hr class="rule-gold"></div></div>
  <div class="champ-panel" data-reveal>
    <div class="cluster"><span class="chip chip--gold">{champ_badge}</span></div>
    <div class="champ-rows">
{champ_rows_html}    </div>
    {"<p class='muted' style='margin-top:var(--sp-3)'>"+champ_note+"</p>" if champ_note else ""}
  </div>
</div></section>

<!-- CAREER TIMELINE -->
<section class="section" id="timeline" style="background:var(--c-bg-elev-1);border-block:1px solid var(--c-line)"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Career timeline</p><h2>The arc of a legend</h2><hr class="rule-gold"></div></div>
  <ol class="timeline" data-reveal>
{timeline_html}  </ol>
</div></section>
{personas_section}
<!-- SIGNATURE MATCHES -->
<section class="section" id="signature"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Must-see matches</p><h2>Start here</h2><hr class="rule-gold"></div></div>
  <div class="grid-cards" data-reveal>
{sig_html}  </div>
</div></section>

<!-- RIVALRIES -->
<section class="section" id="rivalries" style="background:var(--c-bg-elev-1);border-block:1px solid var(--c-line)"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Greatest feuds</p><h2>The rivalries that defined them</h2><hr class="rule-gold"></div></div>
  <div class="related-links" data-reveal>
{rivalries_html}  </div>
</div></section>

<!-- RELATIONSHIPS -->
<section class="section" id="relationships"><div class="wrap">
  <div class="section-head" data-reveal><div><p class="eyebrow">Backstage &amp; real life</p><h2>Behind the character</h2><hr class="rule-gold"></div></div>
  <div class="card" data-reveal><div class="card__body stack">
{relationships_html}    <p class="form-note"><a href="/relationships/">See the full relationship map →</a></p>
  </div></div>
</div></section>
{tv_section}
{pod_section}
<!-- FAQ -->
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

# ─── WRESTLER DATA ──────────────────────────────────────────────────────────────

def row(result, cats, opp, event, date, stip, finish):
    return {"result": result, "cats": cats, "opponent_html": opp, "event": event, "date": date, "stip": stip, "finish": finish}

W = "W"; L = "L"
a = lambda slug, name: f'<a href="/wrestlers/{slug}/">{name}</a>'

wrestlers = []

# ── 1. THE ROCK ──────────────────────────────────────────────────────────────
rock_rows = [
    row(W,"wrestlemania title",a("john-cena","John Cena")+" <span class='title-tag'>Title</span>","WrestleMania 29","2013","WWE Championship","Rock Bottom → pin (rematch win)"),
    row(L,"wrestlemania title",a("john-cena","John Cena")+" <span class='title-tag'>Title</span>","WrestleMania 28","2012","Singles","AA → pin (Once in a Lifetime)"),
    row(W,"wrestlemania title",a("cm-punk","CM Punk")+" <span class='title-tag'>Title</span>","Royal Rumble","2013","WWE Championship","Rock Bottom → pin (won title)"),
    row(W,"wrestlemania",a("john-cena","John Cena"),"WrestleMania 29","2013","Singles","Rock Bottom → pin (twice in a lifetime)"),
    row(L,"wrestlemania",a("stone-cold-steve-austin","Steve Austin")+" <span class='title-tag'>Title</span>","WrestleMania XIX","2003","Singles","Stunner × 3 → pin (final match)"),
    row(W,"wrestlemania title","Hollywood Hulk Hogan","WrestleMania X8","2002","Singles","Rock Bottom → pin (Icon vs Icon)"),
    row(L,"wrestlemania title",a("stone-cold-steve-austin","Steve Austin")+" <span class='title-tag'>Title</span>","WrestleMania X-Seven","2001","WWF Championship","Stunner → pin (Austin heel turn)"),
    row(W,"title",a("kurt-angle","Kurt Angle")+" <span class='title-tag'>Title</span>","No Mercy","2001","WWF Championship","Rock Bottom → pin"),
    row(W,"wrestlemania",a("stone-cold-steve-austin","Steve Austin")+" <span class='title-tag'>Title</span>","WrestleMania XV","1999","WWF Championship","Rock Bottom → pin <span class='title-tag'>1st title</span>"),
    row(W,"title",a("triple-h","Triple H")+" <span class='title-tag'>Title</span>","Backlash","2000","WWF Championship","People's Elbow → pin"),
    row(L,"title",a("triple-h","Triple H")+" <span class='title-tag'>Title</span>","SummerSlam","1998","IC Title","Pedigree → pin"),
    row(W,"title",a("triple-h","Triple H")+" <span class='title-tag'>Title</span>","Raw is War","1998","IC Title","Rock Bottom → pin (Faarooq interference)"),
    row(W,"title",a("mick-foley","Mankind")+" <span class='title-tag'>Title</span>","Survivor Series","1998","WWF Championship","People's Elbow → pin <span class='title-tag'>1st title, won as corporate champ</span>"),
    row(L,"",a("stone-cold-steve-austin","Steve Austin"),"Raw is War","1997","Singles (debut)","Stunner → pin (debut feud)"),
    row(W,"",a("mick-foley","Mankind"),"Royal Rumble","1999","I Quit Match","Repeated chair shots (controversial)"),
]
rock_wm = [
    row(W,"wrestlemania title",a("john-cena","John Cena"),"WrestleMania 29","2013","Singles","Rock Bottom → pin"),
    row(L,"wrestlemania title",a("john-cena","John Cena"),"WrestleMania 28","2012","Singles","AA → pin"),
    row(L,"wrestlemania title",a("stone-cold-steve-austin","Steve Austin"),"WrestleMania XIX","2003","Singles","Stunner×3 → pin"),
    row(W,"wrestlemania","Hollywood Hulk Hogan","WrestleMania X8","2002","Singles","Rock Bottom → pin"),
    row(L,"wrestlemania",a("stone-cold-steve-austin","Steve Austin"),"WrestleMania X-Seven","2001","WWF Championship","Stunner → pin (heel turn)"),
    row(W,"wrestlemania",a("stone-cold-steve-austin","Steve Austin"),"WrestleMania XV","1999","WWF Championship","Rock Bottom → pin"),
    row(W,"wrestlemania","Ken Shamrock","WrestleMania XIV","1998","IC Title","DQ — debut WM main run"),
]
rock_ppv = [
    row(W,"title",a("kurt-angle","Kurt Angle"),"No Mercy","2001","WWF Championship","Rock Bottom → pin"),
    row(L,"title",a("kurt-angle","Kurt Angle"),"Unforgiven","2001","WWF Championship","Angle Slam → pin"),
    row(W,"title",a("triple-h","Triple H"),"Backlash","2000","WWF Championship","People's Elbow → pin"),
    row(W,"",a("mick-foley","Mankind"),"Royal Rumble","1999","I Quit Match","Repeated chair shots → Mankind quits"),
    row(W,"title",a("mick-foley","Mankind"),"Survivor Series","1998","WWF Championship","People's Elbow → pin"),
    row(L,"",a("stone-cold-steve-austin","Steve Austin"),"King of the Ring","1998","Ladder — IC Title","Austin climbed and won"),
]

wrestlers.append({
    "slug": "the-rock",
    "name": "The Rock",
    "initials": "TR",
    "title_tag": "The Rock — Record, Titles &amp; Matches | MAT",
    "description": "The Rock (Dwayne Johnson): complete profile — 8 world titles, the People's Elbow, the Rock Bottom, the Austin trilogy at WrestleMania, and Hollywood legend. Greatest of all time contender.",
    "answer": "<strong>The Rock (Dwayne Johnson) is an 8-time world champion, a three-time WrestleMania main-eventer opposite Steve Austin, and the most electrifying man in sports-entertainment history.</strong> From Nation of Domination rookie to Hollywood's biggest action star, he defined the Attitude Era alongside Stone Cold and became the most crossover-successful pro wrestler of all time.",
    "era": "1996–2013",
    "promo_chip": '<span class="chip chip--wwe">WWF / WWE</span>',
    "alt_names": ["Dwayne Johnson","The People's Champion","The Great One","The Brahma Bull","Dwayne Douglas Johnson","Rocky Maivia","The Corporate Champion"],
    "same_as": ["https://en.wikipedia.org/wiki/Dwayne_Johnson","https://www.wikidata.org/wiki/Q44176","https://www.instagram.com/therock/"],
    "faq_schema": [
        {"q":"What is The Rock's real name?","a":"The Rock's real name is Dwayne Douglas Johnson, born May 2, 1972 in Hayward, California."},
        {"q":"How many WWE titles did The Rock win?","a":"The Rock won 8 world championships: 6 WWF/WWE Championships and 2 WCW/World Championships, becoming one of the most decorated champions in history."},
        {"q":"What is the Rock Bottom finisher?","a":"The Rock Bottom is a side-effect slam where The Rock scoops an opponent and drives them into the mat. Paired with the People's Elbow, it was his signature finishing sequence throughout the Attitude Era."},
    ],
    "subnav": ["record","championships","timeline","signature","rivalries","relationships","faq"],
    "rec_stats": [
        {"n":"8","sub":"×","l":"World Championships","gold":True},
        {"n":"3","sub":"×","l":"WrestleMania vs Austin","gold":True},
        {"n":"6","sub":"×","l":"WWF/WWE Title reigns"},
        {"n":"12","sub":"–3","l":"Curated landmark ledger"},
    ],
    "wl_strip": [True,True,False,True,True,False,True,False,True,True,True,True,False,True,True],
    "tab_id": "rock",
    "tab1_label": "Landmark ledger",
    "tab1_count": "15",
    "tab2_label": "WrestleMania",
    "tab2_count": "5–2",
    "tab3_label": "PPV / PLE",
    "tab3_count": "6 featured",
    "filters": [
        {"label":"All","key":"all","count":"15"},
        {"label":"Wins","key":"wins","count":"10"},
        {"label":"Losses","key":"losses","count":"5"},
        {"label":"WrestleMania","key":"wrestlemania","count":"7"},
        {"label":"Title matches","key":"title","count":"9"},
    ],
    "main_rows": rock_rows,
    "wm_rows": rock_wm,
    "ppv_rows": rock_ppv,
    "method_title": "The People's Elbow closed the show",
    "method_intro": "The Rock finished matches with the Rock Bottom slam setting up the theatrical People's Elbow — a sequence that became iconic for its showmanship. Against Austin he needed three Stunners back at WrestleMania XIX to finally keep him down, a testament to his selling and narrative craft.",
    "method_bars": [
        {"label":"Rock Bottom → People's Elbow","n":"8","pct":53},
        {"label":"Rock Bottom (alone)","n":"4","pct":27},
        {"label":"DQ / count-out / other","n":"3","pct":20},
    ],
    "pull_facts": [
        {"n":"3× Austin","l":"Faced Stone Cold at WrestleMania XV, X-Seven and XIX — the greatest trilogy in the history of the event."},
        {"n":"8 titles","l":"Only six men in history won more world titles in WWE/WWF than The Rock."},
        {"n":"Debut 1996","l":"Rocky Maivia debuted at Survivor Series 1996 — booed. Within two years he was the company's biggest heel, then its biggest babyface."},
    ],
    "champ_title": "Eight world titles across two eras",
    "champ_badge": "8× World Champion",
    "champ_rows_html": """      <div><span class="k">1998</span><span>WWF Championship — def. <a href="/wrestlers/mick-foley/">Mankind</a> at Survivor Series (1st reign, as Corporate Champion)</span></div>
      <div><span class="k">1999</span><span>WWF Championship — def. <a href="/wrestlers/mick-foley/">Mankind</a> at Royal Rumble (Raw title win)</span></div>
      <div><span class="k">1999</span><span>WWF Championship — def. <a href="/wrestlers/triple-h/">Triple H</a> at Backlash (3rd reign)</span></div>
      <div><span class="k">2001</span><span>WCW/World Championship — def. <a href="/wrestlers/kurt-angle/">Kurt Angle</a> at No Mercy</span></div>
      <div><span class="k">2001</span><span>WWF Undisputed Championship — def. <a href="/wrestlers/chris-jericho/">Chris Jericho</a> (brief, vacated)</span></div>
      <div><span class="k">2002</span><span>WWF Championship — def. <a href="/wrestlers/triple-h/">Triple H</a> on Raw (6th WWF/E title)</span></div>
      <div><span class="k">2013</span><span>WWE Championship — def. <a href="/wrestlers/cm-punk/">CM Punk</a> at Royal Rumble (7th world title reign)</span></div>
      <div><span class="k">2013</span><span>WWE Championship — def. <a href="/wrestlers/john-cena/">John Cena</a> at WrestleMania 29 (8th world title reign)</span></div>
""",
    "champ_note": "Also a 2-time Intercontinental Champion (1997–98) and holds the record for most matches against Steve Austin at WrestleMania (three).",
    "timeline_items": [
        {"time":"1996–1997","h":"Rocky Maivia — the rejected rookie","p":"Debuted at Survivor Series 1996; fan backlash to the corporate push led to a 'Die Rocky Die' chant at Madison Square Garden. The rejection forged the character."},
        {"time":"1997–1999","h":"Nation of Domination &amp; the Corporation","p":"Joined and eventually led the Nation of Domination; reinvented as a charismatic heel who coined 'If you smell what the Rock is cooking.' Feuded intensely with <a href='/wrestlers/stone-cold-steve-austin/'>Steve Austin</a> and won his first world title."},
        {"time":"1999–2001","h":"The People's Champion — Attitude Era peak","p":"Turned babyface to massive pops; the Austin vs Rock trilogy defined WrestleMania for a generation. Earned the <em>People's Champion</em> and <em>The Great One</em> monikers."},
        {"time":"2002–2004","h":"'Hollywood' Rock &amp; Hollywood","p":"A brief heel run as Hollywood Rock; feuded with <a href='/wrestlers/goldberg/'>Goldberg</a>, transitioned out of full-time wrestling and into film. <em>The Scorpion King</em> (2002) launched a blockbuster career."},
        {"time":"2011–2013","h":"The comeback","p":"Returned to a record Royal Rumble pop (2011); hosted WrestleMania XXVII; faced <a href='/wrestlers/john-cena/'>John Cena</a> in two successive WrestleMania main events (WM 28 &amp; 29) and captured the WWE title at Royal Rumble 2013."},
    ],
    "sig_matches": [
        {"href":"/matches/austin-vs-rock-wm17/","initials":"WM17","title":"vs Steve Austin — WrestleMania X-Seven","rating":5},
        {"href":"/matches/undertaker-vs-hbk-wm25/","initials":"WM28","title":"vs John Cena — WrestleMania 28","rating":4.5},
        {"href":"/matches/rock-vs-foley-royal-rumble-1999/","initials":"RR99","title":"vs Mankind — Royal Rumble I Quit","rating":4.5},
        {"href":"/matches/austin-vs-rock-wm19/","initials":"WM19","title":"vs Steve Austin — WrestleMania XIX","rating":5},
    ],
    "rivalries_html": '    <a href="/rivalries/austin-vs-rock/">Austin vs Rock (the trilogy)</a>\n    <a href="/wrestlers/stone-cold-steve-austin/">Stone Cold Steve Austin</a>\n    <a href="/wrestlers/triple-h/">Triple H</a>\n    <a href="/wrestlers/mick-foley/">Mick Foley</a>\n    <a href="/wrestlers/kurt-angle/">Kurt Angle</a>\n    <a href="/wrestlers/john-cena/">John Cena</a>\n    <a href="/wrestlers/cm-punk/">CM Punk</a>\n',
    "relationships_html": '    <div class="rel"><div><span class="rel__type">Greatest rival</span><br><a href="/wrestlers/stone-cold-steve-austin/">Stone Cold Steve Austin</a></div></div>\n    <div class="rel"><div><span class="rel__type">Anoa\'i family</span><br><a href="/wrestlers/roman-reigns/">Roman Reigns</a> (cousin), Samoa Joe (cousin)</div></div>\n    <div class="rel"><div><span class="rel__type">Hollywood rival</span><br><a href="/wrestlers/john-cena/">John Cena</a></div></div>\n',
    "tv_items": [
        {"initials":"HBO","title":"Rock &amp; Roll (30 for 30)","year":"ESPN","desc":"ESPN 30 for 30 documentary on his wrestling and Hollywood ascent"},
        {"initials":"BL","title":"Ballers","year":"2015–2019","desc":"HBO sports drama; Rock starred as Spencer Strasmore, 5 seasons"},
        {"initials":"YT","title":"Young Rock","year":"2021–2023","desc":"NBC sitcom dramatizing Dwayne Johnson's youth"},
    ],
    "podcast_items": [
        {"title":"The Pivot Podcast","desc":"Guest appearance — discusses his transition from wrestling to Hollywood"},
    ],
    "faqs": [
        {"q":"What is The Rock's real name?","a":"Dwayne Douglas Johnson, born May 2, 1972 in Hayward, California.","open":True},
        {"q":"How many WWE titles did The Rock win?","a":"Eight world championships total — six WWF/WWE Championships and two WCW/World Championships."},
        {"q":"Why is The Rock called The People's Champion?","a":"Because of his explosive rapport with live crowds. Despite debuting as a face who got booed (Rocky Maivia), he earned the People's Champion nickname as a babyface in 1999–2001 when he became the company's top draw."},
        {"q":"What is the People's Elbow?","a":"The Rock's theatrical finisher — after laying an opponent out, he removes an elbow pad, runs the ropes twice, and lands a flying elbow drop. Mocked as the worst finisher by some commentators, but one of wrestling's most over signatures."},
    ],
    "related_links": [
        {"href":"/wrestlers/stone-cold-steve-austin/","label":"Stone Cold Steve Austin"},
        {"href":"/wrestlers/mick-foley/","label":"Mick Foley"},
        {"href":"/wrestlers/triple-h/","label":"Triple H"},
        {"href":"/wrestlers/kurt-angle/","label":"Kurt Angle"},
        {"href":"/wrestlers/john-cena/","label":"John Cena"},
        {"href":"/rivalries/austin-vs-rock/","label":"The Austin-Rock trilogy"},
    ],
    "bg_gradient": "linear-gradient(150deg,color-mix(in oklab,#1a3a2a 55%,#000),#0c0d10 62%)",
    "facts_html": """        <li><b>Real name</b> Dwayne Douglas Johnson</li>
        <li><b>Born</b> May 2, 1972 · Hayward, CA</li>
        <li><b>Debut</b> 1996 (as Rocky Maivia)</li>
        <li><b>Promotions</b> WWF / WWE</li>
        <li><b>Finisher</b> Rock Bottom, People's Elbow</li>
        <li><b>Hall of Fame</b> Class of 2008 (grandfather Peter Maivia induction; Dwayne inducted 2012 by John Cena)</li>
""",
})

# ── 2. BRET HART ────────────────────────────────────────────────────────────
bret_rows = [
    row(L,"wrestlemania title",a("shawn-michaels","Shawn Michaels")+" <span class='title-tag'>Title</span>","WrestleMania XII","1996","60-min Iron Man Match","Overtime — Sweet Chin Music → pin"),
    row(W,"wrestlemania",a("stone-cold-steve-austin","Steve Austin"),"WrestleMania 13","1997","Submission match","Sharpshooter — Austin passed out (double turn)"),
    row(L,"",a("stone-cold-steve-austin","Steve Austin"),"Survivor Series","1996","Singles","Stunner → pin (Austin's big win)"),
    row(W,"title","Mr. Perfect","King of the Ring","1993","WWF Championship","Sharpshooter → submission <span class='title-tag'>1st title</span>"),
    row(W,"wrestlemania title","Yokozuna <span class='title-tag'>Title</span>","WrestleMania X","1994","WWF Championship","Sharpshooter → ref stop (regained)"),
    row(L,"title","Yokozuna <span class='title-tag'>Title</span>","WrestleMania IX","1993","WWF Championship","Yokozuna won with salt to face"),
    row(W,"wrestlemania title","Roddy Piper","WrestleMania VIII","1992","IC Title","Pin (outstanding technical match)"),
    row(L,"title","Diesel <span class='title-tag'>Title</span>","Survivor Series","1994","WWF Championship","Diesel won (kicked off title reign)"),
    row(W,"title","Diesel <span class='title-tag'>Title</span>","Survivor Series","1995","WWF Championship","Sharpshooter → pinfall reversal <span class='title-tag'>2nd reign</span>"),
    row(W,"title",a("shawn-michaels","Shawn Michaels"),"In Your House 6","1995","WWF Championship","Retained (disqualification)"),
    row(L,"title",a("the-undertaker","The Undertaker")+" <span class='title-tag'>Title</span>","SummerSlam","1997","WWF Championship","HBK chair shot; title changes hands"),
    row(W,"",a("stone-cold-steve-austin","Steve Austin"),"SummerSlam","1997","Tag (w/ British Bulldog vs Austin &amp; HBK)","Hart Foundation wins (great tag match)"),
    row(L,"",a("stone-cold-steve-austin","Steve Austin"),"WCW Monday Nitro","1998","Singles","Sting interference (WCW run)"),
    row(W,"title","Goldberg <span class='title-tag'>Title</span>","WCW Starrcade","1998","WCW Championship","Sharpshooter → submission <span class='title-tag'>WCW title won</span>"),
]
bret_wm = [
    row(W,"wrestlemania",a("stone-cold-steve-austin","Steve Austin"),"WrestleMania 13","1997","Submission match","Sharpshooter — Austin passed out"),
    row(L,"wrestlemania title",a("shawn-michaels","Shawn Michaels"),"WrestleMania XII","1996","60-min Iron Man Match","Overtime — Sweet Chin Music → pin"),
    row(W,"wrestlemania title","Yokozuna","WrestleMania X","1994","WWF Championship","Sharpshooter → regain"),
    row(L,"wrestlemania title","Yokozuna","WrestleMania IX","1993","WWF Championship","Yokozuna retained"),
    row(W,"wrestlemania","Roddy Piper","WrestleMania VIII","1992","IC Title","Technical classic — pin"),
    row(W,"wrestlemania","Skinner","WrestleMania VII","1991","Singles","First WM appearance — quick win"),
]
wrestlers.append({
    "slug": "bret-hart",
    "name": "Bret \"Hitman\" Hart",
    "initials": "BH",
    "title_tag": "Bret \"Hitman\" Hart — Record, Sharpshooter &amp; Five Titles | MAT",
    "description": "Bret Hart: complete profile — 5 WWF Championships, 2 WCW titles, the 1997 Montreal Screwjob, WrestleMania 13 classic vs Austin, the Sharpshooter, and the Hart Foundation legacy.",
    "answer": "<strong>Bret \"Hitman\" Hart — the Excellence of Execution — is a five-time WWF Champion whose rivalry with Steve Austin produced WrestleMania 13's greatest double-turn, and whose 1997 Montreal Screwjob remains the most talked-about event in wrestling history.</strong> The technical backbone of the WWF through the late eighties and nineties, Hart was the best there is, the best there was, and the best there ever will be.",
    "era": "1984–2011",
    "promo_chip": '<span class="chip chip--wwe">WWF / WCW</span>',
    "alt_names": ["Bret Sergeant Hart","The Hitman","The Excellence of Execution","The Best There Is, The Best There Was, The Best There Ever Will Be","The Pink &amp; Black Attack"],
    "same_as": ["https://en.wikipedia.org/wiki/Bret_Hart","https://www.wikidata.org/wiki/Q347866"],
    "faq_schema": [
        {"q":"What is Bret Hart's finishing move?","a":"The Sharpshooter — a double-leg submission hold where Hart steps through an opponent's legs, crosses them, and turns them over to apply spinal pressure. One of wrestling's most iconic finishes."},
        {"q":"What happened at the 1997 Montreal Screwjob?","a":"At Survivor Series 1997, WWE Chairman Vince McMahon ordered referee Earl Hebner to ring the bell while Bret Hart was in the Sharpshooter applied by Shawn Michaels — even though Hart had not submitted. Hart was about to leave for WCW and McMahon did not want the WWF title going there."},
        {"q":"How many WWF titles did Bret Hart win?","a":"Bret Hart won five WWF Championships, plus two WCW Championships, two Intercontinental titles, and multiple WWF Tag Team titles with Jim Neidhart as The Hart Foundation."},
    ],
    "subnav": ["record","championships","timeline","signature","rivalries","relationships","faq"],
    "rec_stats": [
        {"n":"5","sub":"×","l":"WWF Championships","gold":True},
        {"n":"7","sub":"×","l":"World Title reigns total","gold":True},
        {"n":"1997","sub":"","l":"Montreal Screwjob"},
        {"n":"10","sub":"–4","l":"Curated landmark ledger"},
    ],
    "wl_strip": [True,True,False,True,True,False,True,True,False,True,True,True,False,True],
    "tab_id": "bret",
    "tab1_count": "14",
    "tab2_count": "3–2",
    "tab3_count": "ppv",
    "filters": [
        {"label":"All","key":"all","count":"14"},
        {"label":"Wins","key":"wins","count":"9"},
        {"label":"Losses","key":"losses","count":"5"},
        {"label":"WrestleMania","key":"wrestlemania","count":"5"},
        {"label":"Title matches","key":"title","count":"9"},
    ],
    "main_rows": bret_rows,
    "wm_rows": bret_wm,
    "ppv_rows": [],
    "method_title": "The Sharpshooter rarely needed help",
    "method_intro": "Bret Hart won with the Sharpshooter submission or a rollup off a reversal more than any other finish — his matches were built around psychology, body-part targeting, and a submission that looked genuinely painful. When he needed a shortcut, he took it, but the Sharpshooter could win any match.",
    "method_bars": [
        {"label":"Sharpshooter → submission","n":"5","pct":56},
        {"label":"Pinfall (reversal / technical)","n":"3","pct":33},
        {"label":"Countout / DQ / other","n":"1","pct":11},
    ],
    "pull_facts": [
        {"n":"WM 13","l":"The Austin vs Bret Hart submission match at WrestleMania 13 executed the most organic double-turn in wrestling history."},
        {"n":"Montreal","l":"The 1997 Screwjob ended his WWF career and permanently changed the relationship between wrestlers and management."},
        {"n":"Hart Dynasty","l":"Son of Stampede Wrestling's Stu Hart; brother of Owen, brother-in-law of the Bulldogs — the most complete wrestling family in history."},
    ],
    "champ_title": "Five WWF and two WCW titles",
    "champ_badge": "5× WWF Champion",
    "champ_rows_html": """      <div><span class="k">1992</span><span>WWF Championship — def. Ric Flair at Survivor Series (1st reign)</span></div>
      <div><span class="k">1993</span><span>WWF Championship — def. Mr. Perfect at King of the Ring</span></div>
      <div><span class="k">1994</span><span>WWF Championship — def. Yokozuna at WrestleMania X (regained)</span></div>
      <div><span class="k">1995</span><span>WWF Championship — def. Diesel at Survivor Series (4th reign)</span></div>
      <div><span class="k">1996–1997</span><span>WWF Championship — def. <a href="/wrestlers/shawn-michaels/">Shawn Michaels</a> at Survivor Series 1996 (5th reign — before Screwjob)</span></div>
      <div><span class="k">1998</span><span>WCW Championship — def. Goldberg at Starrcade 1998</span></div>
      <div><span class="k">1999</span><span>WCW Championship — def. Ric Flair (2nd WCW reign, before injury/retirement)</span></div>
""",
    "champ_note": "Also 2× Intercontinental Champion and 2× WWF Tag Team Champion (with Jim Neidhart — The Hart Foundation), plus multiple titles in Stampede Wrestling.",
    "timeline_items": [
        {"time":"1984–1988","h":"Stampede Wrestling heritage","p":"Trained by father Stu Hart in the Hart Dungeon, Bret broke through in Stampede and briefly in Japan before signing with the WWF in 1984."},
        {"time":"1988–1992","h":"The Hart Foundation &amp; IC gold","p":"Tag team with Jim Neidhart; transitioned to a singles star with the Intercontinental title and a reputation as the most reliable in-ring worker in the company."},
        {"time":"1992–1996","h":"Five-time WWF Champion","p":"Five world title reigns defined this era; feuds with <a href='/wrestlers/shawn-michaels/'>HBK</a>, Diesel, and the Undertaker — and the storied, politically charged rivalry with <a href='/wrestlers/stone-cold-steve-austin/'>Steve Austin</a>."},
        {"time":"1997","h":"The Hart Foundation &amp; Montreal","p":"Led a faction resisting the American Attitude era; the year culminated in the Screwjob at Survivor Series — he left for WCW that night."},
        {"time":"1998–2000","h":"WCW &amp; the concussion that ended it","p":"Two WCW titles; his ring career ended when a Goldberg kick gave him a concussion he never fully recovered from. Retired from in-ring competition."},
        {"time":"2010","h":"Return &amp; Hall of Fame","p":"Returned for a brief angle with <a href='/wrestlers/shawn-michaels/'>Shawn Michaels</a> at WrestleMania XXVI; inducted into the WWE Hall of Fame, Class of 2006."},
    ],
    "sig_matches": [
        {"href":"/matches/austin-vs-bret-wm13/","initials":"WM13","title":"vs Steve Austin — WrestleMania 13 (Submission)","rating":5},
        {"href":"/matches/bret-vs-hbk-wm12/","initials":"WM12","title":"vs Shawn Michaels — WrestleMania XII (Iron Man)","rating":5},
        {"href":"/matches/bret-vs-owen-wm10/","initials":"WM10","title":"vs Owen Hart — WrestleMania X (Opener)","rating":5},
        {"href":"/matches/bret-vs-bulldog-ss92/","initials":"SS92","title":"vs British Bulldog — SummerSlam 1992","rating":5},
    ],
    "rivalries_html": '    <a href="/rivalries/bret-vs-hbk-montreal/">Bret vs HBK (Montreal Screwjob)</a>\n    <a href="/wrestlers/stone-cold-steve-austin/">Steve Austin</a>\n    <a href="/wrestlers/shawn-michaels/">Shawn Michaels</a>\n    <a href="/wrestlers/triple-h/">Triple H</a>\n    <a href="/wrestlers/the-undertaker/">The Undertaker</a>\n    <a href="/wrestlers/owen-hart/">Owen Hart (brother)</a>\n',
    "relationships_html": '    <div class="rel"><div><span class="rel__type">Estranged brother</span><br><a href="/wrestlers/owen-hart/">Owen Hart</a></div></div>\n    <div class="rel"><div><span class="rel__type">Brother-in-law / tag partner</span><br><a href="/wrestlers/british-bulldog/">British Bulldog</a></div></div>\n    <div class="rel"><div><span class="rel__type">Career-long rival</span><br><a href="/wrestlers/shawn-michaels/">Shawn Michaels</a></div></div>\n    <div class="rel"><div><span class="rel__type">Father / trainer</span><br>Stu Hart (Hart Dungeon)</div></div>\n',
    "tv_items": [
        {"initials":"HT","title":"Hart &amp; Soul: The Hart Family Anthology","year":"2010","desc":"WWE Home Video retrospective on the Hart family legacy in wrestling"},
        {"initials":"SE","title":"Bret Hart: The Best There Is, Was &amp; Will Be","year":"2005","desc":"Career retrospective DVD — one of WWE's most detailed wrestler documentaries"},
        {"initials":"BS","title":"WWE Biography: Bret Hart","year":"2021","desc":"A&amp;E Network Biography series — career and personal life in depth"},
    ],
    "podcast_items": [
        {"title":"Oral Sessions with Renee Paquette","desc":"Extended interview covering the Montreal Screwjob, WCW and legacy"},
    ],
    "faqs": [
        {"q":"What is Bret Hart's finishing move?","a":"The Sharpshooter — a submission hold that targets the back and legs. Applied by stepping through an opponent's legs and turning them face-down.","open":True},
        {"q":"What happened at the Montreal Screwjob?","a":"At Survivor Series 1997, Vince McMahon ordered the bell rung while HBK had the Sharpshooter on Hart — even though Hart hadn't tapped. Hart was leaving for WCW and this was McMahon's way of preventing him from taking the title."},
        {"q":"Who trained Bret Hart?","a":"His father, Stu Hart, in the legendary Hart Dungeon in Calgary, Alberta — the same training school that produced Davey Boy Smith, Owen Hart, Chris Benoit and many others."},
    ],
    "related_links": [
        {"href":"/wrestlers/shawn-michaels/","label":"Shawn Michaels"},
        {"href":"/wrestlers/stone-cold-steve-austin/","label":"Steve Austin"},
        {"href":"/wrestlers/owen-hart/","label":"Owen Hart"},
        {"href":"/wrestlers/british-bulldog/","label":"British Bulldog"},
        {"href":"/rivalries/bret-vs-hbk-montreal/","label":"Montreal Screwjob"},
    ],
    "bg_gradient": "linear-gradient(150deg,color-mix(in oklab,#3a1a2a 55%,#000),#0c0d10 62%)",
    "facts_html": """        <li><b>Real name</b> Bret Sergeant Hart</li>
        <li><b>Born</b> July 2, 1957 · Calgary, Alberta, Canada</li>
        <li><b>Promotions</b> Stampede Wrestling · WWF · WCW</li>
        <li><b>Finisher</b> Sharpshooter (submission)</li>
        <li><b>Hall of Fame</b> Class of 2006</li>
        <li><b>Family</b> Son of Stu Hart; brother of Owen, brother-in-law of British Bulldog</li>
""",
})

# ── 3. TRIPLE H ──────────────────────────────────────────────────────────────
hhh_rows = [
    row(W,"wrestlemania hiac",a("the-undertaker","The Undertaker"),"WrestleMania XXVIII","2012","Hell in a Cell (end of an era)","Pedigree → pin (HBK as ref)"),
    row(L,"wrestlemania",a("the-undertaker","The Undertaker"),"WrestleMania XXVII","2011","No Holds Barred","Hell's Gate → submission"),
    row(L,"wrestlemania title",a("daniel-bryan","Daniel Bryan")+" <span class='title-tag'>Title</span>","WrestleMania XXX","2014","Singles","Running knee → pin (WM main)"),
    row(W,"title",a("john-cena","John Cena")+" <span class='title-tag'>Title</span>","Unforgiven","2002","World Heavyweight Title","Pedigree → pin <span class='title-tag'>1st WHC reign</span>"),
    row(W,"wrestlemania title","Booker T <span class='title-tag'>Title</span>","WrestleMania XIX","2003","World Heavyweight Title","Pedigree → pin"),
    row(L,"wrestlemania title",a("batista","Batista")+" <span class='title-tag'>Title</span>","WrestleMania 21","2005","World Heavyweight Title","Batista Bomb → pin"),
    row(W,"wrestlemania title",a("john-cena","John Cena")+" <span class='title-tag'>Title</span>","WrestleMania 22","2006","WWE Championship","Pedigree → pin"),
    row(L,"wrestlemania title",a("the-undertaker","The Undertaker"),"WrestleMania X-Seven","2001","Singles","Pinfall (Tombstone)"),
    row(W,"title",a("stone-cold-steve-austin","Steve Austin")+" <span class='title-tag'>Title</span>","Backlash","2001","Tag (w/ Austin) vs Taker &amp; Kane","Power Trip won WWF Tag Titles"),
    row(L,"title",a("stone-cold-steve-austin","Steve Austin")+" <span class='title-tag'>Title</span>","Raw is War","2001","WWF Tag — Power Trip","Lost tag titles; quad tear ended Power Trip"),
    row(W,"wrestlemania title","Chris Jericho <span class='title-tag'>Title</span>","WrestleMania X8","2002","Undisputed Title","Pedigree → pin"),
    row(W,"",a("shawn-michaels","Shawn Michaels"),"Summerslam","2002","Unsanctioned Street Fight","Sledgehammer finish (HBK's comeback)"),
    row(L,"wrestlemania",a("shawn-michaels","Shawn Michaels")+" &amp; "+a("chris-jericho","Jericho"),"WrestleMania XX","2004","Triple Threat, WHC","Benoit / HBK pin — lost"),
    row(W,"title",a("randy-orton","Randy Orton")+" <span class='title-tag'>Title</span>","Unforgiven","2004","World Heavyweight Title","Pedigree → pin (Evolution implosion)"),
    row(W,"title","Cactus Jack <span class='title-tag'>Title</span>","Royal Rumble","2000","Street Fight, WWF Title","Pedigree → pin"),
]
hhh_wm = [
    row(W,"wrestlemania hiac",a("the-undertaker","The Undertaker"),"WrestleMania XXVIII","2012","Hell in a Cell","Pedigree → pin"),
    row(L,"wrestlemania",a("the-undertaker","The Undertaker"),"WrestleMania XXVII","2011","No Holds Barred","Hell's Gate → submission"),
    row(L,"wrestlemania title",a("daniel-bryan","Daniel Bryan"),"WrestleMania XXX","2014","Singles","Running knee → pin"),
    row(W,"wrestlemania title","Booker T","WrestleMania XIX","2003","World Heavyweight Title","Pedigree → pin"),
    row(W,"wrestlemania title","Chris Jericho","WrestleMania X8","2002","Undisputed Title","Pedigree → pin"),
    row(L,"wrestlemania title",a("batista","Batista"),"WrestleMania 21","2005","World Heavyweight Title","Batista Bomb → pin"),
    row(W,"wrestlemania title",a("john-cena","John Cena"),"WrestleMania 22","2006","WWE Championship","Pedigree → pin"),
    row(L,"wrestlemania",a("the-undertaker","The Undertaker"),"WrestleMania X-Seven","2001","Singles","Tombstone → pin"),
    row(W,"wrestlemania title",a("mick-foley","Cactus Jack"),"WrestleMania 2000","2000","Street Fight, WWF Title","Pedigree → pin"),
    row(L,"wrestlemania",a("shawn-michaels","Shawn Michaels"),"WrestleMania XII","1996","Tag (as HHH)","DX era warm-up"),
]
wrestlers.append({
    "slug": "triple-h",
    "name": "Triple H",
    "initials": "HHH",
    "title_tag": "Triple H — Record, Pedigree &amp; Championships | MAT",
    "description": "Triple H (Paul Levesque): complete profile — 14 world title reigns, DX, the Two-Man Power Trip, WrestleMania classics vs The Undertaker and Daniel Bryan, and his role as WWE's Executive VP of creative.",
    "answer": "<strong>Triple H (Paul Levesque) is a 14-time world champion, co-founder of D-Generation X, and one of the Attitude Era's defining performers.</strong> As a wrestler, The Cerebral Assassin engineered some of wrestling's most compelling long-term storylines. Today, as WWE's Head of Creative, he shapes the product from the boardroom.",
    "era": "1992–2019",
    "promo_chip": '<span class="chip chip--wwe">WWF / WWE</span>',
    "alt_names": ["Paul Levesque","The Game","The Cerebral Assassin","The King of Kings","HHH","Terra Ryzing","Jean-Paul Lévesque"],
    "same_as": ["https://en.wikipedia.org/wiki/Triple_H","https://www.wikidata.org/wiki/Q265413"],
    "faq_schema": [
        {"q":"What is Triple H's finishing move?","a":"The Pedigree — a double underhook facebreaker where HHH wraps the opponent's arms behind their head and drives their face into the mat. Considered one of the most devastating-looking finishers in WWE history."},
        {"q":"How many world titles did Triple H win?","a":"14 world championship reigns — a record he shares at or near the top of WWE history — combining WWF/WWE Championships and World Heavyweight Championship reigns."},
        {"q":"What is the Two-Man Power Trip?","a":"A 2001 WWE faction of Triple H and Steve Austin that simultaneously held the WWF Championship, Intercontinental Championship, and Tag Team Championship. It ended when Triple H tore his quad in a match against Chris Benoit and Chris Jericho."},
    ],
    "subnav": ["record","championships","timeline","signature","rivalries","relationships","faq"],
    "rec_stats": [
        {"n":"14","sub":"×","l":"World Championships","gold":True},
        {"n":"5","sub":"×","l":"Intercontinental Title","gold":False},
        {"n":"9","sub":"–8","l":"WrestleMania record (all-time)"},
        {"n":"2001","sub":"","l":"Two-Man Power Trip (w/ Austin)"},
    ],
    "wl_strip": [True,True,False,True,True,True,False,True,False,True,True,False,True,True,False],
    "tab_id": "hhh",
    "tab1_count": "15",
    "tab2_count": "5–4",
    "tab3_count": "ppv",
    "filters": [
        {"label":"All","key":"all","count":"15"},
        {"label":"Wins","key":"wins","count":"9"},
        {"label":"Losses","key":"losses","count":"6"},
        {"label":"WrestleMania","key":"wrestlemania","count":"8"},
        {"label":"Title matches","key":"title","count":"10"},
        {"label":"Hell in a Cell","key":"hiac","count":"2"},
    ],
    "main_rows": hhh_rows,
    "wm_rows": hhh_wm,
    "ppv_rows": [],
    "method_title": "The Pedigree as a political instrument",
    "method_intro": "Triple H finished with the Pedigree — but his real signature was the cerebral build to get there. As a heel he held titles through management interference, contract clauses, and Evolution's muscle. As a face the Pedigree landed clean and the crowd popped huge.",
    "method_bars": [
        {"label":"Pedigree → pin","n":"8","pct":62},
        {"label":"Submission (figure four, Hell's Gate counter)","n":"1","pct":8},
        {"label":"DQ / interference / other","n":"3","pct":23},
        {"label":"Loss (opponent's finish)","n":"1","pct":7},
    ],
    "pull_facts": [
        {"n":"14 titles","l":"14 world title reigns — a number that draws debate but stands as one of the highest in WWE history."},
        {"n":"DX co-founder","l":"D-Generation X (with Shawn Michaels) was the Attitude Era's premier rebel faction."},
        {"n":"Now: EVP","l":"Paul Levesque became WWE's Head of Creative / EVP after Vince McMahon's retirement, reshaping NXT and the main roster."},
    ],
    "champ_title": "14 world titles across a 25-year career",
    "champ_badge": "14× World Champion",
    "champ_rows_html": """      <div><span class="k">1999</span><span>WWF Championship — def. Mankind on Raw (1st reign)</span></div>
      <div><span class="k">2000</span><span>WWF Championship — def. Cactus Jack at Royal Rumble; holds title through WrestleMania 2000</span></div>
      <div><span class="k">2002</span><span>World Heavyweight Championship — def. <a href="/wrestlers/john-cena/">Shawn Michaels</a> (1st WHC reign after brand split)</span></div>
      <div><span class="k">2002</span><span>WWF / Undisputed Championship — def. Chris Jericho at WrestleMania X8</span></div>
      <div><span class="k">2003</span><span>World Heavyweight Championship — def. Booker T at WrestleMania XIX</span></div>
      <div><span class="k">2003–2004</span><span>World Heavyweight Championship — back-to-back reigns through Evolution era (4th and 5th WHC)</span></div>
      <div><span class="k">2004</span><span>World Heavyweight Championship — def. <a href="/wrestlers/randy-orton/">Randy Orton</a> at Unforgiven (Evolution power play)</span></div>
      <div><span class="k">2006</span><span>WWE Championship — def. <a href="/wrestlers/john-cena/">John Cena</a> at WrestleMania 22</span></div>
      <div><span class="k">2008–2009</span><span>WWE/World Heavyweight Championship — two reigns through Randy Orton feud era</span></div>
      <div><span class="k">2016</span><span>WWE Championship — Royal Rumble win into WrestleMania 32 main event</span></div>
""",
    "champ_note": "Also 5× Intercontinental Champion, 2× European Champion, 6× WWF/WWE Tag Team Champion (with DX, the Rockers, Austin), and Royal Rumble 2002 winner.",
    "timeline_items": [
        {"time":"1992–1995","h":"Terra Ryzing / Jean-Paul Lévesque","p":"Started as Terra Ryzing in WCWA and IWF; signed with WWF as Jean-Paul Lévesque, a French-Canadian blue-blood character."},
        {"time":"1995–1997","h":"Connecticut Blueblood &amp; DX founding","p":"Repackaged as Hunter Hearst Helmsley, a wealthy Connecticut socialite. Co-founded D-Generation X with <a href='/wrestlers/shawn-michaels/'>Shawn Michaels</a> and Chyna in 1997."},
        {"time":"1999–2002","h":"The Game — Attitude Era peak","p":"Emerged as one of wrestling's top heels; multiple WWF title reigns, the Power Trip with <a href='/wrestlers/stone-cold-steve-austin/'>Austin</a>, and an in-ring career that set the standard for main-event storytelling."},
        {"time":"2002–2008","h":"Evolution &amp; long title runs","p":"Led Evolution (with Ric Flair, Randy Orton, Batista); held the World Heavyweight title for extended periods — both praised as dominant booking and criticized as overly political."},
        {"time":"2009–2019","h":"Final chapter &amp; WrestleMania epics","p":"WrestleMania classics vs <a href='/wrestlers/the-undertaker/'>The Undertaker</a> (WM 27, 28); match vs <a href='/wrestlers/daniel-bryan/'>Daniel Bryan</a> at WM 30; last in-ring years."},
        {"time":"2022–present","h":"EVP of Creative","p":"After Vince McMahon's retirement, Levesque became WWE's Head of Creative — reshaping the product, reviving NXT, and bringing back talent."},
    ],
    "sig_matches": [
        {"href":"/matches/undertaker-vs-triple-h-wm28-2012/","initials":"WM28","title":"vs The Undertaker — WrestleMania 28 (HIAC)","rating":5},
        {"href":"/matches/hhh-vs-foley-royal-rumble-2000/","initials":"RR00","title":"vs Cactus Jack — Royal Rumble 2000","rating":5},
        {"href":"/matches/hhh-vs-hbk-summerslam-2002/","initials":"SS02","title":"vs Shawn Michaels — SummerSlam 2002","rating":4.5},
        {"href":"/matches/hhh-vs-cena-wm22/","initials":"WM22","title":"vs John Cena — WrestleMania 22","rating":4},
    ],
    "rivalries_html": '    <a href="/wrestlers/the-undertaker/">The Undertaker (WM trilogy)</a>\n    <a href="/wrestlers/shawn-michaels/">Shawn Michaels / DX</a>\n    <a href="/wrestlers/stone-cold-steve-austin/">Steve Austin (Two-Man Power Trip)</a>\n    <a href="/wrestlers/mick-foley/">Mick Foley / Cactus Jack</a>\n    <a href="/wrestlers/daniel-bryan/">Daniel Bryan</a>\n    <a href="/wrestlers/randy-orton/">Randy Orton (Evolution)</a>\n',
    "relationships_html": '    <div class="rel"><div><span class="rel__type">DX partner / close friend</span><br><a href="/wrestlers/shawn-michaels/">Shawn Michaels</a></div></div>\n    <div class="rel"><div><span class="rel__type">Power Trip partner</span><br><a href="/wrestlers/stone-cold-steve-austin/">Steve Austin</a></div></div>\n    <div class="rel"><div><span class="rel__type">Married</span><br>Stephanie McMahon (daughter of Vince)</div></div>\n    <div class="rel"><div><span class="rel__type">Evolution stablemates</span><br><a href="/wrestlers/ric-flair/">Ric Flair</a>, <a href="/wrestlers/batista/">Batista</a>, <a href="/wrestlers/randy-orton/">Randy Orton</a></div></div>\n',
    "tv_items": [
        {"initials":"WWE","title":"Triple H: Thy Kingdom Come","year":"2013","desc":"WWE documentary on his career, legacy and political role in wrestling"},
        {"initials":"A&E","title":"WWE Biography: Triple H","year":"2021","desc":"A&E Network in-depth career retrospective"},
    ],
    "podcast_items": [
        {"title":"Cheap Heat with Rosenberg","desc":"Multiple appearances discussing NXT and WWE creative philosophy"},
    ],
    "faqs": [
        {"q":"What is Triple H's finishing move?","a":"The Pedigree — a double underhook facebreaker where he drives the opponent's face into the mat. One of WWE's most iconic finishers.","open":True},
        {"q":"How many world titles did Triple H win?","a":"14 world titles across his career — one of the highest totals in WWE history, spanning WWF/WWE Championships and World Heavyweight Championships."},
        {"q":"What was the Two-Man Power Trip?","a":"A 2001 faction of Triple H and Steve Austin, who simultaneously held multiple titles until HHH tore his quad in May 2001 in a match against Benoit and Jericho."},
    ],
    "related_links": [
        {"href":"/wrestlers/stone-cold-steve-austin/","label":"Steve Austin"},
        {"href":"/wrestlers/shawn-michaels/","label":"Shawn Michaels / DX"},
        {"href":"/wrestlers/the-undertaker/","label":"The Undertaker"},
        {"href":"/wrestlers/mick-foley/","label":"Mick Foley"},
        {"href":"/wrestlers/daniel-bryan/","label":"Daniel Bryan"},
        {"href":"/wrestlers/randy-orton/","label":"Randy Orton"},
    ],
    "bg_gradient": "linear-gradient(150deg,color-mix(in oklab,var(--c-gold) 30%,#000),#0c0d10 62%)",
    "facts_html": """        <li><b>Real name</b> Paul Michael Levesque</li>
        <li><b>Born</b> July 27, 1969 · Nashua, NH</li>
        <li><b>Promotions</b> WWF / WWE (1995–2019)</li>
        <li><b>Finisher</b> Pedigree (double underhook facebreaker)</li>
        <li><b>Hall of Fame</b> Class of 2019</li>
        <li><b>Now</b> WWE EVP of Talent, Creative &amp; Live Events</li>
""",
})

# ── 4. KANE ─────────────────────────────────────────────────────────────────
kane_rows = [
    row(W,"wrestlemania title","The Undertaker (2nd appearance)","WrestleMania XX","2004","Singles","Tombstone reversal → pin"),
    row(L,"wrestlemania",a("the-undertaker","The Undertaker"),"WrestleMania XIV","1998","Singles","3× Tombstone → pin"),
    row(W,"title",a("stone-cold-steve-austin","Steve Austin")+" <span class='title-tag'>Title</span>","King of the Ring","1998","WWF Championship","Pinfall (interference) <span class='title-tag'>1st WWF Title</span>"),
    row(L,"title",a("stone-cold-steve-austin","Steve Austin")+" <span class='title-tag'>Title</span>","Raw is War","1998","WWF Championship","Stunner → pin (Austin regained)"),
    row(L,"hiac",a("the-undertaker","The Undertaker"),"King of the Ring","1998","Hell in a Cell","Tombstone → pin (most dangerous HIAC)"),
    row(W,"title","Rey Mysterio <span class='title-tag'>Title</span>","Extreme Rules","2010","ECW Championship","Chokeslam → pin"),
    row(W,"title",a("the-undertaker","The Undertaker")+" <span class='title-tag'>Title</span>","Hell in a Cell","2010","World Heavyweight Title","Chokeslam (Paul Bearer betrayal) → pin"),
    row(L,"title",a("stone-cold-steve-austin","Steve Austin")+" &amp; "+a("the-undertaker","The Undertaker"),"Fully Loaded","1998","Tag (vs Austin &amp; Taker) — WWF Tag Titles","Lost tag titles"),
    row(W,"title",a("stone-cold-steve-austin","Steve Austin")+" <span class='title-tag'>Title</span>","Backlash","2001","Tag (w/ Taker vs Austin &amp; HHH)","Regained tag titles from Power Trip"),
    row(W,"","Mankind","Survivor Series","1997","Singles","Chokeslam → pin (debut era)"),
    row(L,"title",a("triple-h","Triple H")+" <span class='title-tag'>Title</span>","No Mercy","1999","WWF Title (Last Man Standing)","HHH won on a count"),
    row(W,"title","Rob Van Dam <span class='title-tag'>Title</span>","Raw","2012","WWE Championship","Chokeslam → pin"),
]
wrestlers.append({
    "slug": "kane",
    "name": "Kane",
    "initials": "KN",
    "title_tag": "Kane — Record, Big Red Machine &amp; World Titles | MAT",
    "description": "Kane (Glen Jacobs): complete profile — WWF/WWE Champion, 12× Tag Champion, ECW Champion, the most decorated monster in WWE history, and current Mayor of Knox County, Tennessee.",
    "answer": "<strong>Kane — the Big Red Machine — is arguably the most consistently over monster character in WWE history.</strong> He debuted at Badd Blood 1997, delivered one of WrestleMania's great debut angles at WM XIV, and remained a legitimate main-event threat for two decades — winning a WWF Championship, ECW title, and a record 12 tag titles.",
    "era": "1995–2019",
    "promo_chip": '<span class="chip chip--wwe">WWF / WWE</span>',
    "alt_names": ["Glen Jacobs","Big Red Machine","The Devil's Favorite Demon","Issac Yankem DDS","Fake Diesel","The Monster Among Men"],
    "same_as": ["https://en.wikipedia.org/wiki/Kane_(wrestler)"],
    "faq_schema": [
        {"q":"What is Kane's real name?","a":"Kane's real name is Glen Thomas Jacobs, born April 26, 1969. He is also the Mayor of Knox County, Tennessee (elected 2018)."},
        {"q":"When did Kane debut?","a":"Kane debuted at Badd Blood: In Your House on October 5, 1997, breaking through the cell door during The Undertaker vs Shawn Michaels' first Hell in a Cell match. His WrestleMania XIV match against The Undertaker followed."},
        {"q":"How many tag team titles did Kane win?","a":"Kane holds the record for the most tag team championship reigns in WWE history — 12 — with partners including The Undertaker, Rob Van Dam, Big Show, X-Pac, and others."},
    ],
    "subnav": ["record","championships","timeline","signature","rivalries","faq"],
    "rec_stats": [
        {"n":"1","sub":"×","l":"WWF Championship","gold":True},
        {"n":"12","sub":"×","l":"Tag Team Championships (record)","gold":True},
        {"n":"1997","sub":"","l":"Badd Blood debut"},
        {"n":"8","sub":"–4","l":"Curated landmark ledger"},
    ],
    "wl_strip": [True,False,True,False,True,True,False,True,True,False,True,False],
    "tab_id": "kane",
    "tab1_count": "12",
    "tab2_count": "2–2",
    "filters": [
        {"label":"All","key":"all","count":"12"},
        {"label":"Wins","key":"wins","count":"7"},
        {"label":"Losses","key":"losses","count":"5"},
        {"label":"WrestleMania","key":"wrestlemania","count":"2"},
        {"label":"Title matches","key":"title","count":"9"},
        {"label":"Hell in a Cell","key":"hiac","count":"2"},
    ],
    "main_rows": kane_rows,
    "wm_rows": [
        row(W,"wrestlemania",a("the-undertaker","The Undertaker"),"WrestleMania XX","2004","Singles","Tombstone reversal → pin"),
        row(L,"wrestlemania",a("the-undertaker","The Undertaker"),"WrestleMania XIV","1998","Singles","3× Tombstone → pin"),
    ],
    "ppv_rows": [],
    "method_title": "Chokeslam and monster authority",
    "method_intro": "Kane wins with the Chokeslam and Tombstone Piledriver (learned from his brother). As a monster heel he also wins via disqualification or count-out, protecting his aura of invincibility across 20+ years as a main-roster threat.",
    "method_bars": [
        {"label":"Chokeslam → pin","n":"5","pct":62},
        {"label":"Tombstone Piledriver","n":"1","pct":13},
        {"label":"Pinfall (opponent's error / assist)","n":"1","pct":13},
    ],
    "pull_facts": [
        {"n":"12 tag reigns","l":"The most tag team championship reigns in WWE history — a record that reflects his versatility as both a powerhouse and a team threat."},
        {"n":"Mayor of Knox Co.","l":"Glen Jacobs was elected Mayor of Knox County, Tennessee in 2018 — perhaps wrestling's most successful pivot to politics."},
        {"n":"Debut vs HBK/Taker","l":"Few debut angles in wrestling history matched his 1997 HIAC appearance — he turned what was already a landmark match into a generational moment."},
    ],
    "champ_title": "Monster champion across three decades",
    "champ_badge": "WWF + ECW Champion",
    "champ_rows_html": """      <div><span class="k">1998</span><span>WWF Championship — def. <a href="/wrestlers/stone-cold-steve-austin/">Steve Austin</a> at King of the Ring (1-day reign — vacated/lost on Raw)</span></div>
      <div><span class="k">2010</span><span>World Heavyweight Championship — def. <a href="/wrestlers/the-undertaker/">The Undertaker</a> at Hell in a Cell (Paul Bearer betrayal)</span></div>
      <div><span class="k">2010</span><span>ECW Championship — def. Rey Mysterio at Extreme Rules</span></div>
      <div><span class="k">2012</span><span>WWE Championship — def. CM Punk on Raw (brief reign)</span></div>
      <div><span class="k">1997–2019</span><span>WWF/WWE Tag Team Championships × 12 — record-holder; partners include The Undertaker, Rob Van Dam, Big Show, and X-Pac</span></div>
""",
    "champ_note": "Also a 1× Intercontinental Champion and holds the record for most WWE tag title reigns at 12.",
    "timeline_items": [
        {"time":"1995–1997","h":"Issac Yankem &amp; Fake Diesel","p":"Debuted as Isaac Yankem DDS, Jerry Lawler's dentist heel. Later repackaged as a fake Diesel in 1996 — neither gimmick clicked. The character was quietly shelved."},
        {"time":"1997","h":"Kane debuts at Badd Blood","p":"October 5, 1997 — he tore through the cell door during the first-ever Hell in a Cell. A debut angle that immediately elevated him to main-event credibility."},
        {"time":"1997–2005","h":"The Big Red Machine era","p":"WrestleMania XIV match vs The Undertaker; WWF title win over <a href='/wrestlers/stone-cold-steve-austin/'>Austin</a>; 12 tag title reigns; the unmasking in 2003; a feud with Shane McMahon and an enduring main-roster presence."},
        {"time":"2006–2019","h":"Corporate Kane &amp; later career","p":"World Heavyweight title (2010); partnerships with Daniel Bryan as Team Hell No (2012–13, fan-favourite comedy); final active years as a comedy-serious hybrid character."},
        {"time":"2018–present","h":"Mayor of Knox County","p":"Glen Jacobs won the Mayor of Knox County, Tennessee election in 2018 — one of sports entertainment's most unusual off-screen success stories."},
    ],
    "sig_matches": [
        {"href":"/matches/kane-vs-undertaker-wm14/","initials":"WM14","title":"vs The Undertaker — WrestleMania XIV","rating":4},
        {"href":"/matches/undertaker-vs-mankind-king-of-ring-1998/","initials":"KOTR98","title":"Taker vs Mankind (HIAC) — Kane was the catalyst","rating":5},
        {"href":"/matches/kane-vs-austin-kotr-1998/","initials":"KOTR98","title":"vs Steve Austin — King of the Ring 1998 (Title win)","rating":3.5},
    ],
    "rivalries_html": '    <a href="/wrestlers/the-undertaker/">The Undertaker (brother)</a>\n    <a href="/wrestlers/stone-cold-steve-austin/">Steve Austin</a>\n    <a href="/wrestlers/triple-h/">Triple H</a>\n    <a href="/wrestlers/mick-foley/">Mankind</a>\n    <a href="/wrestlers/daniel-bryan/">Daniel Bryan (Team Hell No)</a>\n',
    "relationships_html": '    <div class="rel"><div><span class="rel__type">Kayfabe brother</span><br><a href="/wrestlers/the-undertaker/">The Undertaker</a></div></div>\n    <div class="rel"><div><span class="rel__type">Team Hell No partner</span><br><a href="/wrestlers/daniel-bryan/">Daniel Bryan</a></div></div>\n    <div class="rel"><div><span class="rel__type">Power Trip opponents</span><br><a href="/wrestlers/stone-cold-steve-austin/">Steve Austin</a></div></div>\n',
    "tv_items": [
        {"initials":"WWE","title":"See No Evil (film)","year":"2006","desc":"WWE Films — Glen Jacobs starred as the monster Jacob Goodnight, a slasher horror role"},
        {"initials":"A&E","title":"WWE Biography: Kane","year":"2022","desc":"A&E career retrospective covering his WWE run and political career"},
    ],
    "podcast_items": [
        {"title":"Grilling JR (guest)","desc":"Jim Ross interviewed Glen Jacobs about the Kane character's creation and 20-year longevity"},
    ],
    "faqs": [
        {"q":"What is Kane's real name?","a":"Glen Thomas Jacobs — and he's also the Mayor of Knox County, Tennessee.","open":True},
        {"q":"When did Kane debut?","a":"October 5, 1997 at Badd Blood: In Your House — he tore through the Hell in a Cell door during the Undertaker vs HBK match."},
        {"q":"How many tag titles did Kane win?","a":"12 — the most in WWE history, with partners including The Undertaker, Rob Van Dam, Big Show, and Daniel Bryan."},
    ],
    "related_links": [
        {"href":"/wrestlers/the-undertaker/","label":"The Undertaker"},
        {"href":"/wrestlers/stone-cold-steve-austin/","label":"Steve Austin"},
        {"href":"/wrestlers/mick-foley/","label":"Mankind"},
        {"href":"/wrestlers/daniel-bryan/","label":"Daniel Bryan (Team Hell No)"},
    ],
    "bg_gradient": "linear-gradient(150deg,color-mix(in oklab,var(--c-red) 50%,#000),#0c0d10 62%)",
    "facts_html": """        <li><b>Real name</b> Glen Thomas Jacobs</li>
        <li><b>Born</b> April 26, 1969 · Torrejón de Ardoz, Spain (raised USA)</li>
        <li><b>Promotions</b> WWF / WWE (1995–2019)</li>
        <li><b>Finisher</b> Chokeslam, Tombstone Piledriver</li>
        <li><b>Alter egos</b> Issac Yankem DDS (1995), Fake Diesel (1996)</li>
        <li><b>Real world</b> Mayor of Knox County, TN (2018–present)</li>
""",
})

# ── 5. MICK FOLEY ────────────────────────────────────────────────────────────
foley_rows = [
    row(L,"hiac",a("the-undertaker","The Undertaker"),"King of the Ring","1998","Hell in a Cell","The cell fall / Tombstone → pin (the greatest bump ever)"),
    row(W,"wrestlemania",a("edge","Edge"),"WrestleMania 22","2006","Hardcore Match","Spear through flaming table (Edge later won)"),
    row(W,"title",a("the-rock","The Rock")+" <span class='title-tag'>Title</span>","Raw is War","1999","WWF Championship (as Mankind) <span class='title-tag'>1st title</span>","Pin (vacated within days)"),
    row(L,"",a("the-rock","The Rock"),"Royal Rumble","1999","I Quit Match — as Mankind","Chair shots; Mankind passed out / \"quit\""),
    row(W,"title",a("the-rock","The Rock")+" <span class='title-tag'>Title</span>","Halftime Heat","1999","Empty arena match — WWF Title","Pinfall in boiler room (3rd title)"),
    row(W,"",a("the-undertaker","The Undertaker"),"Survivor Series","1996","Singles — as Mankind","Won (upset) — Mankind debut year highlight"),
    row(L,"title","HHH <span class='title-tag'>Title</span>","Royal Rumble","2000","Street Fight (as Cactus Jack) — WWF Title","Pedigree on thumbtacks → pin"),
    row(W,"",a("stone-cold-steve-austin","Steve Austin"),"Raw is War","1997","Tag (as Dude Love, w/ Austin) — WWF Tag Titles","Won vacant tag titles (surprise partner)"),
    row(L,"",a("stone-cold-steve-austin","Steve Austin"),"Over the Limit","1998","Singles — WWF Title shot (as Dude Love)","Stunner → pin (corporate backup failed)"),
    row(L,"hiac","Undertaker / various","Boiler Room Brawl","1996","Boiler Room Brawl — as Mankind","Paul Bearer turned on Mankind"),
    row(W,"","Shane McMahon","WrestleMania 2000","2000","2-on-1 (w/ Vince) as Commissioner","Socko / corporate drama"),
]
wrestlers.append({
    "slug": "mick-foley",
    "name": "Mick Foley",
    "initials": "MF",
    "title_tag": "Mick Foley — Mankind, Dude Love, Cactus Jack &amp; Hardcore Legend | MAT",
    "description": "Mick Foley: complete profile — three WWF titles as Mankind, Cactus Jack's war with Triple H, the King of the Ring 1998 cell fall, Dude Love, and the Hardcore Legend who redefined what a wrestling match could cost.",
    "answer": "<strong>Mick Foley — across three personas: Mankind, Dude Love, and Cactus Jack — is the most beloved brawler in wrestling history and the man who took the most memorable bump in the sport's recorded history.</strong> The cell fall at King of the Ring 1998 remains a defining moment not just for one match but for an entire era. Three WWF titles, a Hall of Fame career, and a genuine gift for comedy balanced against real violence.",
    "era": "1983–2012",
    "promo_chip": '<span class="chip chip--wwe">WWF / WWE</span>',
    "alt_names": ["Mankind","Cactus Jack","Dude Love","Michael Francis Foley","Mrs. Foley's Baby Boy","The Hardcore Legend","Have a Nice Day"],
    "same_as": ["https://en.wikipedia.org/wiki/Mick_Foley","https://www.wikidata.org/wiki/Q313543"],
    "faq_schema": [
        {"q":"What is Mick Foley's most famous moment?","a":"The Hell in a Cell match at King of the Ring 1998 — thrown off the top of the cell by The Undertaker (a 16-foot fall), then chokeslammed through the cell ceiling in a spot that was not planned. Often cited as the greatest bump in wrestling history."},
        {"q":"How many WWF titles did Mick Foley win?","a":"Three WWF Championships — as Mankind (1999), in an empty arena, and a third reign. He's also a multi-time tag team champion and held the WWF Hardcore title an uncountable number of times."},
        {"q":"Who are Mick Foley's wrestling personas?","a":"Three distinct personas: Mankind (deranged, masked, tortured), Dude Love (tie-dye hippie, surprise WWF tag partner for Steve Austin in 1997), and Cactus Jack (violent hardcore brawler from his early career and ECW run)."},
    ],
    "subnav": ["record","championships","timeline","personas","signature","rivalries","faq"],
    "rec_stats": [
        {"n":"3","sub":"×","l":"WWF Championships","gold":True},
        {"n":"3","sub":"","l":"Personas (Mankind / Dude Love / Cactus Jack)"},
        {"n":"1998","sub":"","l":"The cell fall — KOTR"},
        {"n":"7","sub":"–4","l":"Curated landmark ledger"},
    ],
    "wl_strip": [False,True,True,False,True,True,False,True,True,False,True],
    "tab_id": "foley",
    "tab1_count": "11",
    "tab2_count": "0–2",
    "filters": [
        {"label":"All","key":"all","count":"11"},
        {"label":"Wins","key":"wins","count":"7"},
        {"label":"Losses","key":"losses","count":"4"},
        {"label":"WrestleMania","key":"wrestlemania","count":"2"},
        {"label":"Title matches","key":"title","count":"6"},
        {"label":"Hell in a Cell","key":"hiac","count":"2"},
    ],
    "main_rows": foley_rows,
    "wm_rows": [
        row(W,"wrestlemania",a("edge","Edge"),"WrestleMania 22","2006","Hardcore Match","Spear through flaming table"),
        row(L,"wrestlemania title","Triple H (as Cactus Jack)","WrestleMania 2000","2000","Street Fight, WWF Title","Pedigree on thumbtacks → pin"),
    ],
    "ppv_rows": [],
    "method_title": "Mandible Claw and the will to absorb punishment",
    "method_intro": "Foley didn't win clean often — his career was built on absorbing punishment until opponents couldn't continue. The Mandible Claw (Socko) put people out; in brawls, it was often the last man standing who won, and Foley had an inhuman tolerance for violence.",
    "method_bars": [
        {"label":"Mandible Claw (Mr. Socko)","n":"3","pct":43},
        {"label":"Pinfall (after brawling)","n":"3","pct":43},
        {"label":"Forfeit / title vacated","n":"1","pct":14},
    ],
    "pull_facts": [
        {"n":"The Cell Fall","l":"King of the Ring 1998 — thrown from 16 feet by The Undertaker. When he returned minutes later, Jim Ross said: 'That's it, he's dead.' He wasn't."},
        {"n":"3 personas","l":"Mankind, Dude Love, and Cactus Jack — three fully developed wrestling identities from one performer."},
        {"n":"Author","l":"His memoir <em>Have a Nice Day</em> (1999) debuted at #1 on the New York Times bestseller list — handwritten."},
    ],
    "champ_title": "Three WWF Titles and uncounted Hardcore reigns",
    "champ_badge": "3× WWF Champion",
    "champ_rows_html": """      <div><span class="k">Jan 1999</span><span>WWF Championship — def. <a href="/wrestlers/the-rock/">The Rock</a> on Raw (as Mankind, 1st title)</span></div>
      <div><span class="k">Jan 1999</span><span>WWF Championship — def. The Rock in the Halftime Heat empty-arena match (3rd title — brief)</span></div>
      <div><span class="k">Aug 1999</span><span>WWF Championship — brief 3rd reign during the McMahon-Helmsley era</span></div>
      <div><span class="k">1997</span><span>WWF Tag Team Championships — won vacant titles w/ <a href="/wrestlers/stone-cold-steve-austin/">Steve Austin</a> on Raw as Dude Love (surprise partner)</span></div>
      <div><span class="k">multiple</span><span>WWF Hardcore Championship — held it a record number of times under the 24/7 rule and in legitimate hardcore matches</span></div>
""",
    "champ_note": "Also a 2× WWF Tag Team Champion (with Austin and with Al Snow) and the definitive king of the Hardcore Championship era.",
    "timeline_items": [
        {"time":"1983–1993","h":"Cactus Jack — the early years","p":"Started as Cactus Jack in NWA/WCW — a fearless brawler who built a reputation on death-defying violence and genuine storytelling in the independent circuit."},
        {"time":"1993–1996","h":"ECW &amp; the promo that launched him","p":"ECW run included a famous anti-ECW promo that was secretly designed to make Foley a face star — one of wrestling's great worked shoots. Left for WWF in 1996."},
        {"time":"1996–1999","h":"Mankind, Dude Love &amp; the WWF peak","p":"Debuted as the deranged Mankind; co-founded 'Dude Love' as <a href='/wrestlers/stone-cold-steve-austin/'>Austin</a>'s tag partner; won three WWF titles. The King of the Ring 1998 cell match defined his legacy."},
        {"time":"2000–2006","h":"Cactus Jack returns &amp; Commissioner","p":"The Cactus Jack Royal Rumble 2000 match vs Triple H; served as WWF Commissioner (comedic); WrestleMania 22 hardcore match with Edge."},
        {"time":"2006–2012","h":"Hall of Fame &amp; appearances","p":"Inducted into the Hall of Fame in 2013; regular appearances and promos; wrote multiple bestselling books about his career."},
    ],
    "personas": [
        {"name":"Cactus Jack","slug":"cactus-jack","era":"1983–2000","desc":"The violent hardcore original — pre-WWE persona from NWA/WCW and ECW. Brought back for specific feuds."},
        {"name":"Mankind","slug":"mick-foley","era":"1996–1999","desc":"The deranged, masked, tortured soul. His primary WWF persona and the one who won three WWF titles."},
        {"name":"Dude Love","slug":"mick-foley","era":"1997","desc":"The tie-dye hippie — a comedic character who debuted as <a href='/wrestlers/stone-cold-steve-austin/'>Austin</a>'s mystery tag partner and briefly challenged as a corporate hire."},
    ],
    "sig_matches": [
        {"href":"/matches/undertaker-vs-mankind-king-of-ring-1998/","initials":"KOTR98","title":"vs The Undertaker — King of the Ring 1998 (HIAC)","rating":5},
        {"href":"/matches/hhh-vs-foley-royal-rumble-2000/","initials":"RR00","title":"vs Triple H — Royal Rumble 2000 (Street Fight)","rating":5},
        {"href":"/matches/rock-vs-foley-royal-rumble-1999/","initials":"RR99","title":"vs The Rock — Royal Rumble 1999 (I Quit)","rating":4.5},
        {"href":"/matches/foley-vs-edge-wm22/","initials":"WM22","title":"vs Edge — WrestleMania 22 (Hardcore)","rating":4.5},
    ],
    "rivalries_html": '    <a href="/wrestlers/the-undertaker/">The Undertaker (the cell match)</a>\n    <a href="/wrestlers/triple-h/">Triple H (Royal Rumble 2000)</a>\n    <a href="/wrestlers/the-rock/">The Rock (I Quit match)</a>\n    <a href="/wrestlers/stone-cold-steve-austin/">Steve Austin (Dude Love era)</a>\n    <a href="/wrestlers/edge/">Edge (WrestleMania 22)</a>\n    <a href="/wrestlers/randy-orton/">Randy Orton</a>\n',
    "relationships_html": '    <div class="rel"><div><span class="rel__type">Tag partner (Dude Love era)</span><br><a href="/wrestlers/stone-cold-steve-austin/">Steve Austin</a></div></div>\n    <div class="rel"><div><span class="rel__type">Long-time nemesis</span><br><a href="/wrestlers/triple-h/">Triple H</a></div></div>\n    <div class="rel"><div><span class="rel__type">WWF Title rival</span><br><a href="/wrestlers/the-rock/">The Rock</a></div></div>\n    <div class="rel"><div><span class="rel__type">Close friend (real)</span><br><a href="/wrestlers/the-undertaker/">The Undertaker</a></div></div>\n',
    "tv_items": [
        {"initials":"WWE","title":"Beyond the Mat (documentary)","year":"1999","desc":"Theatrical documentary by Barry Blaustein — the most intimate portrait of Foley's life and family during his wrestling peak"},
        {"initials":"WWE","title":"Mick Foley: Greatest Hits &amp; Misses","year":"2004","desc":"WWE Home Video retrospective with career highlights and the cell fall"},
    ],
    "podcast_items": [
        {"title":"Foley is Pod","desc":"Mick Foley's own podcast — interviewing wrestling legends and sharing career stories"},
        {"title":"Something to Wrestle with Bruce Prichard (guest)","desc":"Deep dive on the creation of Mankind and the 1998 KOTR cell match"},
    ],
    "faqs": [
        {"q":"What is Mick Foley's most famous moment?","a":"The cell fall at King of the Ring 1998 — thrown 16 feet by The Undertaker. Jim Ross said 'That's it, he's dead.' He wasn't.","open":True},
        {"q":"Who are Mick Foley's three personas?","a":"Mankind (deranged masked character), Dude Love (tie-dye hippie; Austin's surprise tag partner), and Cactus Jack (violent hardcore original from his pre-WWE career)."},
        {"q":"How many WWF titles did Foley win?","a":"Three WWF Championships, all as Mankind — plus countless Hardcore title reigns and two tag title reigns."},
    ],
    "related_links": [
        {"href":"/wrestlers/the-undertaker/","label":"The Undertaker"},
        {"href":"/wrestlers/triple-h/","label":"Triple H"},
        {"href":"/wrestlers/the-rock/","label":"The Rock"},
        {"href":"/wrestlers/stone-cold-steve-austin/","label":"Steve Austin"},
        {"href":"/wrestlers/edge/","label":"Edge"},
    ],
    "bg_gradient": "linear-gradient(150deg,color-mix(in oklab,#2a1a0a 65%,#000),#0c0d10 62%)",
    "facts_html": """        <li><b>Real name</b> Michael Francis Foley</li>
        <li><b>Born</b> June 7, 1965 · Bloomington, Indiana (raised on Long Island, NY)</li>
        <li><b>Promotions</b> WWF / WWE · WCW · ECW</li>
        <li><b>Personas</b> Mankind · Dude Love · Cactus Jack</li>
        <li><b>Finisher</b> Mandible Claw (Mr. Socko), DDT (as Cactus Jack)</li>
        <li><b>Hall of Fame</b> Class of 2013</li>
""",
})


# ── WRITE ALL PAGES ────────────────────────────────────────────────────────────
for w in wrestlers:
    html = build_page(w)
    path = os.path.join(BASE, w["slug"], "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)
    lines = html.count('\n')
    print(f"✅ {w['slug']} — {lines} lines")

print("\nBatch 1a complete.")
