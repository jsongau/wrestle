#!/usr/bin/env python3
"""Idempotent match-page kit. Swaps the search-facade for a real .yt modal facade,
wraps the winner in the spoiler card, blurs the Result row and the answer TL;DR,
de-auto-opens the winner-spoiling FAQ item, and links css/matchkit.css + media.js +
matchkit.js (fresh cache-bust). Reads data/matches.json (source of truth). Leaves
site.css untouched. Preserves all hand-authored prose. Safe to re-run. WL_ROOT + hash argv[1]."""
import os, re, json, sys, html, glob
ROOT = os.environ.get("WL_ROOT", "."); H = sys.argv[1] if len(sys.argv) > 1 else "0000000"
SVC = {"WWE":("Peacock","https://www.peacocktv.com/"),"WWF":("Peacock","https://www.peacocktv.com/"),
       "WCW":("Peacock","https://www.peacocktv.com/"),"ECW":("Peacock","https://www.peacocktv.com/"),
       "NXT":("Peacock","https://www.peacocktv.com/"),"TNA":("TNA+","https://watch.tnawrestling.com/"),
       "ROH":("HonorClub","https://www.rohwrestling.com/")}
def svc(p): return SVC.get((p or "WWE").upper(), SVC["WWE"])
def esc(s): return html.escape(s or "", quote=True)
def yt_facade(m):
    v=m["video"]; s,url=svc(m.get("promotion")); title="%s, %s"%(m["title"],m.get("event",""))
    return ('<div class="yt" data-yt-id="%s" data-yt-title="%s" data-yt-creator="%s" data-yt-service="%s" data-yt-service-url="%s">'
            '<a class="yt__link" href="https://www.youtube.com/watch?v=%s">Play: %s (official %s upload)</a></div>'
            %(esc(v["id"]),esc(title),esc(v.get("channel","WWE")),esc(s),esc(url),esc(v["id"]),esc(m["title"]),esc(v.get("channel","WWE"))))
def poster(m):
    s,url=svc((m or {}).get("promotion","WWE"))
    return ('<div class="yt"><a class="yt__link" href="%s" target="_blank" rel="noopener">No official clip on YouTube. Watch on %s.</a></div>'%(esc(url),esc(s)))
EMBED=re.compile(r'<div class="embed">\s*<button class="facade".*?</button>\s*</div>',re.S)
SIDE=r'<div><div class="tale__name">.*?</div><span class="chip[^"]*">.*?</span></div>'
TALE=re.compile(r'<div class="tale">\s*('+SIDE+r')\s*<div class="vs">VS</div>\s*('+SIDE+r')\s*</div>',re.S)
RESULT=re.compile(r'(<tr><th>Result</th><td>)(.*?)(</td></tr>)',re.S)
ANSWER=re.compile(r'<p class="answer">.*?</p>',re.S)
NOTE_OLD='<p class="form-note">▶ Opens the official WWE match search. Verified embed IDs (YouTube &amp; Bilibili for China) drop straight into this player.</p>'
def t_embed(d,m):
    if not EMBED.search(d): return d,False,None
    real=bool(m and m["video"]["id"])
    if real: rep=yt_facade(m)
    else: rep=poster(m)
    service=svc((m or {}).get("promotion","WWE"))[0]
    return EMBED.sub(lambda _:rep,d,count=1),True,(real,service)
def t_note(d,info):
    if NOTE_OLD not in d: return d,False
    if info is None: return d,False
    real,service=info
    new=('<p class="form-note">▶ Plays right here in our player — official upload, verified.</p>' if real else
         '<p class="form-note">▶ No official clip is embedded yet. This link opens to watch on %s.</p>'%esc(service))
    return d.replace(NOTE_OLD,new,1),True
def t_tale(d):
    m=TALE.search(d)
    if not m: return d,False
    full,a,b=m.group(0),m.group(1),m.group(2)
    w="left" if "chip--win" in a else ("right" if "chip--win" in b else "draw")
    lbl="Tap to reveal winner" if w!="draw" else "Tap to reveal result"
    blk=re.sub(r'(<span class="chip[^"]*)(")',r'\1 wl-sp__verdict\2',full)
    blk=blk.replace('<div class="tale">','<div class="tale wl-sp__card">',1)
    pill='<button class="wl-sp__reveal" type="button" aria-expanded="false" aria-label="%s"><span class="wl-sp__reveal-ic" aria-hidden="true">◆</span> %s</button>'%(lbl,lbl)
    i=blk.rfind('</div>'); blk=blk[:i]+"        "+pill+"\n      "+blk[i:]
    return d.replace(full,'<div class="wl-spoiler" data-winner="%s">\n      %s\n      </div>'%(w,blk),1),True
def t_result(d):
    m=RESULT.search(d)
    if not m or "wl-sp__hide" in m.group(2): return d,False
    return d.replace(m.group(0),m.group(1)+'<span class="wl-sp__hide">'+m.group(2)+'</span>'+m.group(3),1),True
def t_answer(d):
    if 'wl-spoiler-block' in d: return d,False
    m=ANSWER.search(d)
    if not m: return d,False
    cover=('<button class="wl-spoiler-block__cover" type="button" aria-expanded="false" aria-label="Reveal the result">'
           '<span class="wl-spoiler-block__badge">Spoiler alert</span>'
           '<span class="wl-spoiler-block__cue">Tap to reveal the result</span></button>')
    return d.replace(m.group(0),'<div class="wl-spoiler-block">'+m.group(0)+cover+'</div>',1),True
def t_faq(d):
    if '<details open>' not in d: return d,False
    return d.replace('<details open>','<details>',1),True
def t_assets(d):
    ch=False
    if '/css/matchkit.css' not in d:
        d=re.sub(r'(<link rel="stylesheet" href="/css/site\.css\?v=[0-9a-f]+">)',r'\1\n<link rel="stylesheet" href="/css/matchkit.css?v=%s">'%H,d,count=1); ch=True
    if '/js/matchkit.js' not in d:
        d=d.replace('</body>','<script src="/js/media.js?v=%s" defer></script>\n<script src="/js/matchkit.js?v=%s" defer></script>\n</body>'%(H,H),1); ch=True
    return d,ch
def transform(d,m):
    d,a,info=t_embed(d,m); d,n=t_note(d,info); d,b=t_tale(d); d,c=t_result(d); d,e=t_answer(d); d,g=t_faq(d); d,f=t_assets(d)
    return d,dict(embed=a,note=n,tale=b,result=c,answer=e,faq=g,assets=f)
def main():
    data={x["slug"]:x for x in json.load(open(os.path.join(ROOT,"data/matches.json")))}
    for f in sorted(glob.glob(os.path.join(ROOT,"matches/*/index.html"))):
        slug=os.path.basename(os.path.dirname(f)); doc=open(f,encoding="utf-8").read()
        out,st=transform(doc,data.get(slug))
        if out!=doc: open(f,"w",encoding="utf-8").write(out)
        print(slug,"->",{k:v for k,v in st.items() if v})
if __name__=="__main__": main()
