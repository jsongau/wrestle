#!/usr/bin/env python3
"""Regenerate /wrestlers/ index with ALL wrestler pages (was stale at 41). Cards from filesystem."""
import glob, re, html as H
DOMAIN="https://wrestlelore.com"
PROMOS=["wwe","wcw","ecw","tna","nxt","njpw","aew"]
def name_of(p):
    h=open(p).read()
    m=re.search(r'<h1[^>]*>(.*?)</h1>',h,re.DOTALL) or re.search(r'<title>(.*?)</title>',h,re.DOTALL)
    t=re.sub(r'<[^>]+>','',m.group(1)) if m else p.split('/')[-2]
    t=H.unescape(t); t=re.split(r'\s[—|]\s',t)[0]; t=re.sub(r'\s*\|\s*Wrestle Lore.*$','',t)
    return t.strip(), h
def promo_of(h):
    c={}
    for m in re.findall(r'/promotions/(%s)/'%'|'.join(PROMOS),h): c[m]=c.get(m,0)+1
    return max(c,key=c.get) if c else ""
def mono(t):
    w=re.sub(r'[^A-Za-z ]','',t).split()
    return ((w[0][0] if w else t[0])+(w[1][0] if len(w)>1 else (w[0][1:2] if w and len(w[0])>1 else ''))).upper()
rows=[]
for p in sorted(glob.glob("wrestlers/*/index.html")):
    slug=p.split('/')[-2]
    nm,h=name_of(p); pr=promo_of(h)
    rows.append((nm,slug,pr))
rows.sort(key=lambda r:re.sub(r'^(the |"|\u201c)','',r[0].lower()))
cards=""
for nm,slug,pr in rows:
    letter=(re.sub(r'^(the |"|\u201c)','',nm.lower())[:1] or '#').upper()
    if not letter.isalpha(): letter='#'
    cards+=('<article class="card" data-letter="%s">'
            '<a class="card__media" href="/wrestlers/%s/" aria-label="%s"><span class="card__initials">%s</span></a>'
            '<div class="card__body"><h3 class="card__title"><a class="card__link" href="/wrestlers/%s/">%s</a></h3>'
            '</div></article>\n')%(letter,slug,H.escape(nm),mono(nm),slug,H.escape(nm))
n=len(rows)
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Anton&family=Oswald:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
ld='{"@context":"https://schema.org","@type":"CollectionPage","name":"All Wrestlers","numberOfItems":%d,"url":"%s/wrestlers/"}'%(n,DOMAIN)
letters=sorted({(re.sub(r'^(the |"|\u201c)','',n.lower())[:1] or '#').upper() if (re.sub(r'^(the |"|\u201c)','',n.lower())[:1] or '#').isalpha() else '#' for n,_,_ in rows})
bar=('<div class="facetbar" data-facet-target="#roster" data-facet-group="letter" role="group" aria-label="Jump by letter">'
 '<span class="facetbar__label">A&ndash;Z</span>'
 '<button class="fbtn is-active" data-facet="all" aria-pressed="true">All</button>'
 +''.join('<button class="fbtn" data-facet="letter:%s" aria-pressed="false">%s</button>'%(L,L) for L in letters)
 +'<span class="facet-count" data-facet-count></span></div>')
page=('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">'
 '<meta name="viewport" content="width=device-width,initial-scale=1">'
 '<title>All Wrestlers ('+str(n)+') — A to Z Roster | Wrestle Lore</title>'
 '<meta name="description" content="Every wrestler profiled on Wrestle Lore: '+str(n)+' superstars across WWE, WCW, ECW, TNA, NXT, NJPW and AEW, filterable by promotion.">'
 '<link rel="canonical" href="'+DOMAIN+'/wrestlers/">'+FONTS+
 '<link rel="stylesheet" href="/css/site.css">'
 '<script type="application/ld+json">'+ld+'</script></head><body>'
 '<header class="site-header"></header>'
 '<main id="main-wrap"><section class="ev-hero"><div class="wrap ev-hero__inner">'
 '<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li aria-current="page">Wrestlers</li></ol></nav>'
 '<span class="ev-hero__brand">The Roster</span><h1>All <span class="accent">Wrestlers</span></h1>'
 '<p class="ev-lede">Every one of the '+str(n)+' superstars profiled on Wrestle Lore, A to Z. Filter by letter or open the command palette to jump.</p>'
 '</div></section><div class="wrap">'+bar+
 '<div class="grid-cards" id="roster">\n'+cards+'</div>'
 '<p class="facet-empty" style="display:none">No wrestlers match that filter.</p>'
 '</div></main><footer class="site-footer"></footer>'
 '<script src="/js/facets.js" defer></script></body></html>')
open("wrestlers/index.html","w").write(page)
print("roster rebuilt:",n,"wrestlers")
from collections import Counter
print(dict(Counter(r[2] or 'none' for r in rows)))
