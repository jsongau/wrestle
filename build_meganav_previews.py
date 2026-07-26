#!/usr/bin/env python3
"""Three graphic-heavy mega-nav design directions for MAT. Self-contained previews.
A = Broadcast Control Room · B = Editorial Poster Wall · C = Arena Spotlight.
No Join CTA, no 中文. All graphics are CSS (gradients/monograms/SVG) — no images."""
import os

OUT = "/tmp"

# ── content data ────────────────────────────────────────────────────────────
PROMOS = [("WWE / WWF","#c8102e","WWE"),("WCW","#e2b13c","WCW"),("ECW","#b0b0b0","ECW"),
          ("TNA / Impact","#1e73be","TNA"),("NXT","#f5c518","NXT")]
FEATURED = [("Stone Cold Steve Austin","SA","/wrestlers/stone-cold-steve-austin/","#c8102e"),
            ("The Undertaker","UT","/wrestlers/the-undertaker/","#6b46c1"),
            ("Roman Reigns","RR","/wrestlers/roman-reigns/","#1f6f4a"),
            ("Rhea Ripley","RH","/wrestlers/rhea-ripley/","#7a1220"),
            ("Cody Rhodes","CR","/wrestlers/cody-rhodes/","#b8860b"),
            ("Becky Lynch","BL","/wrestlers/becky-lynch/","#c8102e")]
EVENTS_RECENT = [("WrestleMania 42","WM","Apr 18–19, 2026","/events/wrestlemania-42-2026/","#d4af37"),
                 ("Night of Champions 2026","NC","Jun 27, 2026","/events/night-of-champions-2026/","#d4af37"),
                 ("Backlash 2026","BL","May 9, 2026","/events/backlash-2026/","#c8102e")]
EVENTS_BRANDS = [("WrestleMania","/events/wrestlemania/"),("Royal Rumble","/events/royal-rumble/"),
                 ("Elimination Chamber","/events/elimination-chamber/"),("Night of Champions","/events/night-of-champions/"),
                 ("Backlash","/events/backlash/")]
MOMENTS = [("Mankind's Hell in a Cell Fall","MK","King of the Ring 1998","/moments/mankind-hell-in-a-cell-fall-1998/"),
           ("Triple H Tears His Quad","HHH","Raw 2001","/moments/triple-h-tears-his-quad-2001/"),
           ("Kane's Debut","KN","Badd Blood 1997","/moments/kane-debut-badd-blood-1997/"),
           ("Steve Austin Breaks His Neck","SA","SummerSlam 1997","/moments/steve-austin-broken-neck-1997/")]

SEARCH_INDEX = ('[{"t":"The Undertaker","u":"/wrestlers/the-undertaker/","k":"Wrestler"},'
 '{"t":"Stone Cold Steve Austin","u":"/wrestlers/stone-cold-steve-austin/","k":"Wrestler"},'
 '{"t":"Roman Reigns","u":"/wrestlers/roman-reigns/","k":"Wrestler"},'
 '{"t":"Cody Rhodes","u":"/wrestlers/cody-rhodes/","k":"Wrestler"},'
 '{"t":"WrestleMania 42","u":"/events/wrestlemania-42-2026/","k":"Event"},'
 '{"t":"Night of Champions 2026","u":"/events/night-of-champions-2026/","k":"Event"},'
 '{"t":"Mankind\\u2019s Hell in a Cell Fall","u":"/moments/mankind-hell-in-a-cell-fall-1998/","k":"Moment"},'
 '{"t":"Triple H Tears His Quad","u":"/moments/triple-h-tears-his-quad-2001/","k":"Moment"},'
 '{"t":"Kane\\u2019s Debut","u":"/moments/kane-debut-badd-blood-1997/","k":"Moment"},'
 '{"t":"Undertaker vs HBK at WM25","u":"/matches/undertaker-vs-hbk-wm25/","k":"Match"}]')

# tab icons (inline svg, currentColor stroke)
ICONS = {
 "wrestlers":'<svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/></svg>',
 "matches":'<svg viewBox="0 0 24 24"><path d="M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9 6.8 19.1l1-5.8L3.5 9.2l5.9-.9z"/></svg>',
 "events":'<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 9h18M8 3v4M16 3v4"/></svg>',
 "moments":'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M10 9l5 3-5 3z"/></svg>',
 "more":'<svg viewBox="0 0 24 24"><circle cx="5" cy="12" r="1.6"/><circle cx="12" cy="12" r="1.6"/><circle cx="19" cy="12" r="1.6"/></svg>',
 "search":'<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>',
}

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Anton&family=Oswald:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">')

BASE = """
:root{--bg:#0a0b0d;--e1:#121418;--e2:#1a1d23;--e3:#23272f;--line:#2b3038;--line2:#3a414c;
--tx:#e8eaed;--mut:#a2a9b4;--dim:#6b727d;--gold:#d4af37;--goldb:#f2cc4b;--goldd:#8c7420;
--goldt:rgba(212,175,55,.12);--red:#e11d2a;--redb:#ff3b48;--fdisp:'Anton',sans-serif;
--fcond:'Oswald',sans-serif;--fbody:'Inter',system-ui,sans-serif;--ease:cubic-bezier(.2,.7,.2,1);}
*{box-sizing:border-box;}
body{margin:0;background:var(--bg);color:var(--tx);font-family:var(--fbody);min-height:100vh;
background:radial-gradient(120% 80% at 20% -10%,rgba(212,175,55,.10),transparent 55%),
 radial-gradient(90% 70% at 90% -10%,rgba(200,16,46,.08),transparent 50%),var(--bg);}
a{color:inherit;text-decoration:none;}
.wrap{max-width:1240px;margin:0 auto;padding:0 24px;}
.demo-note{max-width:1240px;margin:0 auto;padding:28px 24px 0;color:var(--dim);font-family:var(--fcond);
 text-transform:uppercase;letter-spacing:.14em;font-size:12px;}
.demo-hero{max-width:1240px;margin:0 auto;padding:8vh 24px;}
.demo-hero h1{font-family:var(--fdisp);text-transform:uppercase;font-size:clamp(3rem,7vw,6rem);line-height:.9;
 margin:0;color:transparent;background:linear-gradient(180deg,#fff 40%,#c9ccd2);-webkit-background-clip:text;background-clip:text;}
.demo-hero h1 .g{background:linear-gradient(180deg,#f7e08a,var(--gold) 50%,var(--goldd));-webkit-background-clip:text;background-clip:text;color:transparent;}
.demo-hero p{color:var(--mut);max-width:52ch;font-size:1.1rem;}
/* command palette (shared) */
.cmdk{position:fixed;inset:0;z-index:200;display:none;background:rgba(6,7,9,.74);backdrop-filter:blur(5px);padding:12vh 20px 20px;}
.cmdk.on{display:block;}
.cmdk__box{max-width:640px;margin:0 auto;background:var(--e1);border:1px solid var(--line2);border-radius:16px;overflow:hidden;box-shadow:0 24px 80px rgba(0,0,0,.6);}
.cmdk__h{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--line);}
.cmdk__h svg{width:18px;height:18px;fill:none;stroke:var(--dim);stroke-width:2;}
.cmdk__in{flex:1;background:none;border:0;color:var(--tx);font-size:1.1rem;outline:none;font-family:var(--fbody);}
.cmdk__in::placeholder{color:var(--dim);}
.cmdk__esc{font-family:var(--fcond);text-transform:uppercase;font-size:12px;color:var(--dim);}
.cmdk__r{list-style:none;margin:0;padding:8px;max-height:50vh;overflow:auto;}
.cmdk__row{display:flex;align-items:center;gap:12px;padding:10px 12px;border-radius:10px;cursor:pointer;}
.cmdk__row.on,.cmdk__row:hover{background:var(--e2);}
.cmdk__k{font-family:var(--fcond);text-transform:uppercase;font-size:11px;letter-spacing:.05em;padding:2px 9px;border-radius:999px;border:1px solid var(--line2);color:var(--dim);min-width:78px;text-align:center;}
.cmdk__k.wrestler{color:var(--goldb);border-color:var(--goldd);background:var(--goldt);}
.cmdk__k.event{color:var(--goldb);border-color:var(--goldd);}
.cmdk__k.moment{color:var(--redb);border-color:#8f1219;background:rgba(225,29,42,.12);}
.cmdk__k.match{color:#8fb7ff;border-color:#2f4a78;}
.cmdk__t{font-size:.98rem;}
.cmdk__row.on .cmdk__t{color:var(--goldb);}
"""

JS = """
(function(){
 // dropdowns: hover + click + close-delay
 var items=document.querySelectorAll('.nav-item.has');
 items.forEach(function(it){
   var t;
   it.addEventListener('mouseenter',function(){clearTimeout(t);close(it);it.classList.add('open');});
   it.addEventListener('mouseleave',function(){t=setTimeout(function(){it.classList.remove('open');},180);});
   var b=it.querySelector('.nav-tab');
   b.addEventListener('click',function(e){e.preventDefault();var o=it.classList.contains('open');closeAll();if(!o)it.classList.add('open');});
 });
 function close(except){items.forEach(function(i){if(i!==except)i.classList.remove('open');});}
 function closeAll(){items.forEach(function(i){i.classList.remove('open');});}
 document.addEventListener('click',function(e){if(!e.target.closest('.nav-item'))closeAll();});
 // palette
 var IDX=%SEARCH%;
 var ov=document.getElementById('cmdk'),inp=ov.querySelector('.cmdk__in'),list=ov.querySelector('.cmdk__r'),act=-1,rows=[];
 function open(){ov.classList.add('on');inp.value='';render('');setTimeout(function(){inp.focus();},20);}
 function shut(){ov.classList.remove('on');act=-1;}
 function sc(it,q){var t=it.t.toLowerCase();if(t===q)return 100;if(t.indexOf(q)===0)return 80;if(t.indexOf(q)>-1)return 50;var p=t.split(/\\s+/);for(var i=0;i<p.length;i++)if(p[i].indexOf(q)===0)return 40;return -1;}
 function esc(s){return String(s).replace(/[&<>\"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;'}[c];});}
 function render(q){q=(q||'').trim().toLowerCase();var it=!q?IDX.slice(0,7):IDX.map(function(x){return{x:x,s:sc(x,q)};}).filter(function(o){return o.s>=0;}).sort(function(a,b){return b.s-a.s;}).slice(0,20).map(function(o){return o.x;});rows=it;act=it.length?0:-1;if(!it.length){list.innerHTML='<li class=\"cmdk__row\" style=\"color:var(--dim)\">No matches</li>';return;}list.innerHTML=it.map(function(x,i){return '<li class=\"cmdk__row'+(i===act?' on':'')+'\" data-u=\"'+x.u+'\"><span class=\"cmdk__k '+x.k.toLowerCase()+'\">'+x.k+'</span><span class=\"cmdk__t\">'+esc(x.t)+'</span></li>';}).join('');}
 function mv(d){if(!rows.length)return;act=(act+d+rows.length)%rows.length;var e=list.querySelectorAll('.cmdk__row');e.forEach(function(el,i){el.classList.toggle('on',i===act);});}
 inp.addEventListener('input',function(){render(inp.value);});
 inp.addEventListener('keydown',function(e){if(e.key==='ArrowDown'){e.preventDefault();mv(1);}else if(e.key==='ArrowUp'){e.preventDefault();mv(-1);}else if(e.key==='Enter'){if(rows[act])location.href=rows[act].u;}else if(e.key==='Escape')shut();});
 list.addEventListener('click',function(e){var r=e.target.closest('.cmdk__row');if(r&&r.dataset.u)location.href=r.dataset.u;});
 ov.addEventListener('click',function(e){if(e.target===ov)shut();});
 document.addEventListener('keydown',function(e){if((e.metaKey||e.ctrlKey)&&e.key.toLowerCase()==='k'){e.preventDefault();open();}else if(e.key==='/'&&!/input|textarea/i.test(e.target.tagName))(e.preventDefault(),open());});
 document.querySelectorAll('[data-open]').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();open();});});
})();
"""

def palette_html():
    return ('<div class="cmdk" id="cmdk" role="dialog" aria-modal="true" aria-label="Search">'
      '<div class="cmdk__box"><div class="cmdk__h">'+ICONS["search"].replace('<svg','<svg fill="none" stroke="currentColor" stroke-width="2"')+
      '<input class="cmdk__in" placeholder="Search wrestlers, events, moments, matches…" aria-label="Search"><span class="cmdk__esc">esc</span></div>'
      '<ul class="cmdk__r"></ul></div></div>')

def page(title, theme_css, bar_html, note):
    svg_fix = 'svg{fill:none;stroke:currentColor;stroke-width:2;}'
    return ("<!DOCTYPE html><html lang=en><head><meta charset=UTF-8>"
      "<meta name=viewport content='width=device-width,initial-scale=1'>"
      "<title>"+title+"</title>"+FONTS+"<style>"+BASE+svg_fix+theme_css+"</style></head><body>"
      +bar_html+palette_html()+
      "<div class=demo-note>"+note+"</div>"
      "<div class=demo-hero><h1>EVERY RIVALRY.<br>EVERY <span class=g>LEGEND.</span></h1>"
      "<p>Hover the tabs to open each panel. Press ⌘K, Ctrl-K, or / to search. This is a nav design preview.</p></div>"
      "<script>"+JS.replace('%SEARCH%',SEARCH_INDEX)+"</script></body></html>")

def mono(initials, accent, cls="mono"):
    return ('<span class="'+cls+'" style="--a:'+accent+'">'+initials+'</span>')

# ══════════════════════════════════════════════════════════════════════════
# THEME A — BROADCAST CONTROL ROOM
# ══════════════════════════════════════════════════════════════════════════
A_CSS = """
.hdr{position:sticky;top:0;z-index:100;background:linear-gradient(180deg,rgba(12,13,16,.96),rgba(12,13,16,.88));
 border-bottom:1px solid var(--line);backdrop-filter:blur(10px);}
.bar{display:flex;align-items:center;gap:6px;min-height:64px;}
.brand{display:flex;align-items:center;gap:10px;font-family:var(--fdisp);font-size:1.5rem;letter-spacing:.02em;margin-right:14px;}
.brand i{width:34px;height:34px;display:grid;place-items:center;background:linear-gradient(145deg,var(--goldb),var(--goldd));color:#0a0b0d;border-radius:8px;font-family:var(--fdisp);font-size:1.1rem;font-style:normal;}
.brand small{font-family:var(--fcond);font-size:10px;letter-spacing:.3em;color:var(--dim);text-transform:uppercase;align-self:flex-end;margin-bottom:4px;}
.nav-item{position:relative;}
.nav-tab{display:inline-flex;align-items:center;gap:8px;padding:20px 14px;color:var(--mut);font-family:var(--fcond);
 text-transform:uppercase;letter-spacing:.08em;font-weight:600;font-size:14px;cursor:pointer;border:0;background:none;position:relative;}
.nav-tab svg{width:16px;height:16px;color:var(--dim);}
.nav-item:hover .nav-tab,.nav-item.open .nav-tab{color:var(--tx);}
.nav-item.open .nav-tab svg,.nav-item:hover .nav-tab svg{color:var(--goldb);}
.nav-item.open .nav-tab::after{content:"";position:absolute;left:14px;right:14px;bottom:0;height:2px;background:var(--gold);}
.spacer{flex:1;}
.srch{display:inline-flex;align-items:center;gap:9px;padding:9px 14px;background:var(--e2);border:1px solid var(--line);
 border-radius:8px;color:var(--dim);font-family:var(--fcond);text-transform:uppercase;letter-spacing:.06em;font-size:12px;cursor:pointer;}
.srch svg{width:15px;height:15px;}
.srch:hover{border-color:var(--goldd);color:var(--tx);}
.srch kbd{font-family:var(--fcond);background:var(--e3);border:1px solid var(--line2);border-radius:4px;padding:1px 6px;font-size:11px;}
.panel{position:absolute;top:calc(100% + 1px);left:0;background:linear-gradient(180deg,#0e1014,#0b0c0f);
 border:1px solid var(--line2);border-radius:0 0 12px 12px;padding:22px;min-width:560px;display:none;
 box-shadow:0 30px 70px rgba(0,0,0,.6);}
.panel::before,.panel::after{content:"";position:absolute;width:14px;height:14px;border:2px solid var(--goldd);opacity:.6;}
.panel::before{top:10px;left:10px;border-right:0;border-bottom:0;}
.panel::after{bottom:10px;right:10px;border-left:0;border-top:0;}
.nav-item.open .panel{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;animation:fa .18s var(--ease);}
@keyframes fa{from{opacity:0;transform:translateY(-6px);}to{opacity:1;transform:none;}}
.col h4{font-family:var(--fcond);text-transform:uppercase;letter-spacing:.14em;font-size:11px;color:var(--gold);margin:0 0 12px;
 display:flex;align-items:center;gap:8px;}
.col h4::before{content:"";width:5px;height:5px;background:var(--red);border-radius:50%;box-shadow:0 0 6px var(--red);}
.crow{display:flex;align-items:center;gap:10px;padding:7px 8px;border-radius:8px;border:1px solid transparent;}
.crow:hover{background:var(--e2);border-color:var(--line);}
.mono{width:34px;height:34px;flex:none;display:grid;place-items:center;border-radius:7px;font-family:var(--fdisp);font-size:13px;
 color:#fff;background:linear-gradient(145deg,var(--a),#0c0d10 75%);border:1px solid rgba(255,255,255,.08);letter-spacing:.02em;}
.crow b{display:block;font-weight:600;font-size:14px;color:var(--tx);}
.crow small{color:var(--dim);font-family:var(--fcond);text-transform:uppercase;letter-spacing:.05em;font-size:10px;}
.pchip{display:flex;align-items:center;gap:9px;padding:8px;border-radius:8px;border-left:3px solid var(--a);background:var(--e1);margin-bottom:6px;}
.pchip b{font-size:13px;} .pchip small{color:var(--dim);font-size:10px;}
.tag{margin-left:auto;font-family:var(--fcond);font-size:10px;text-transform:uppercase;letter-spacing:.06em;color:var(--dim);}
"""
def A_panel_wrestlers():
    proms="".join('<a class="pchip" style="--a:%s" href="/promotions/%s/"><b>%s</b><small>Promotion</small></a>'%(c,ab.lower(),n) for n,c,ab in PROMOS[:5])
    feat="".join('<a class="crow" href="%s">%s<span><b>%s</b><small>Featured</small></span></a>'%(h,mono(i,c),n) for n,i,h,c in FEATURED[:4])
    return ('<div class="panel"><div class="col"><h4>By Promotion</h4>'+proms+'</div>'
      '<div class="col"><h4>Featured</h4>'+feat+'</div>'
      '<div class="col"><h4>Browse</h4>'
      '<a class="crow" href="/wrestlers/">'+mono("AZ","#8c7420")+'<span><b>All Wrestlers</b><small>Full roster</small></span></a>'
      '<a class="crow" href="/rankings/">'+mono("★","#8c7420")+'<span><b>Top Ranked</b><small>All-time</small></span></a></div></div>')
def A_panel_events():
    rec="".join('<a class="crow" href="%s">%s<span><b>%s</b><small>%s</small></span><span class="tag">PLE</span></a>'%(h,mono(i,c),n,d) for n,i,d,h,c in EVENTS_RECENT)
    br="".join('<a class="crow" href="%s">%s<span><b>%s</b><small>Brand</small></span></a>'%(h,mono("".join(w[0] for w in n.split()[:2]),"#8c7420"),n) for n,h in EVENTS_BRANDS[:5])
    return ('<div class="panel"><div class="col"><h4>Recent</h4>'+rec+'</div>'
      '<div class="col"><h4>Brands</h4>'+br+'</div>'
      '<div class="col"><h4>&nbsp;</h4><a class="crow" href="/events/">'+mono("ALL","#8c7420")+'<span><b>All Events</b><small>Results &amp; where to watch</small></span></a></div></div>')
def A_panel_moments():
    ms="".join('<a class="crow" href="%s">%s<span><b>%s</b><small>%s</small></span></a>'%(h,mono(i,"#8f1219"),n,s) for n,i,s,h in MOMENTS)
    return '<div class="panel" style="min-width:640px"><div class="col"><h4>Famous Moments</h4>'+ms[:len(ms)//2 if False else None if False else len(ms)]+'</div><div class="col"><h4>&nbsp;</h4><a class="crow" href="/moments/">'+mono("ALL","#8f1219")+'<span><b>All Moments</b><small>Iconic incidents, on video</small></span></a></div><div class="col"><h4>&nbsp;</h4></div></div>'

# ══════════════════════════════════════════════════════════════════════════
# THEME B — EDITORIAL POSTER WALL
# ══════════════════════════════════════════════════════════════════════════
B_CSS = """
.hdr{position:sticky;top:0;z-index:100;background:rgba(10,11,13,.9);border-bottom:1px solid var(--line);backdrop-filter:blur(12px);}
.bar{display:flex;align-items:center;gap:4px;min-height:70px;}
.brand{font-family:var(--fdisp);font-size:1.7rem;margin-right:22px;display:flex;align-items:center;gap:10px;}
.brand i{width:36px;height:36px;display:grid;place-items:center;background:#111;border:1px solid var(--goldd);color:var(--goldb);border-radius:10px;font-style:normal;font-size:1.2rem;}
.nav-item{position:relative;}
.nav-tab{display:inline-flex;align-items:center;gap:8px;padding:24px 16px;color:var(--mut);font-family:var(--fcond);
 text-transform:uppercase;letter-spacing:.1em;font-weight:600;font-size:15px;cursor:pointer;border:0;background:none;}
.nav-tab svg{width:15px;height:15px;color:var(--dim);}
.nav-item:hover .nav-tab,.nav-item.open .nav-tab{color:var(--goldb);}
.spacer{flex:1;}
.srch{display:inline-flex;align-items:center;gap:10px;padding:11px 18px;border:1px solid var(--line2);border-radius:999px;
 color:var(--dim);font-family:var(--fcond);text-transform:uppercase;letter-spacing:.08em;font-size:12px;cursor:pointer;}
.srch svg{width:15px;height:15px;}.srch:hover{border-color:var(--gold);color:var(--tx);}
.srch kbd{background:var(--e2);border:1px solid var(--line2);border-radius:5px;padding:1px 6px;font-family:var(--fcond);font-size:11px;}
.panel{position:absolute;top:100%;left:0;background:#0c0d10;border:1px solid var(--line);border-top:2px solid var(--gold);
 padding:30px;min-width:720px;display:none;box-shadow:0 40px 90px rgba(0,0,0,.65);}
.nav-item.open .panel{display:block;animation:fb .2s var(--ease);}
@keyframes fb{from{opacity:0;transform:translateY(-8px);}to{opacity:1;transform:none;}}
.phead{font-family:var(--fdisp);text-transform:uppercase;font-size:1.6rem;line-height:.95;margin:0 0 4px;}
.psub{color:var(--dim);font-family:var(--fcond);text-transform:uppercase;letter-spacing:.1em;font-size:11px;margin-bottom:20px;}
.posters{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;}
.poster{display:block;border-radius:12px;overflow:hidden;border:1px solid var(--line);transition:transform .18s var(--ease),border-color .18s var(--ease);}
.poster:hover{transform:translateY(-4px);border-color:var(--goldd);}
.poster .art{aspect-ratio:3/4;display:grid;place-items:center;position:relative;
 background:linear-gradient(155deg,var(--a),#0b0c0f 72%);}
.poster .art::after{content:"";position:absolute;inset:0;background:repeating-linear-gradient(0deg,transparent 0 2px,rgba(255,255,255,.03) 2px 3px);}
.poster .art b{font-family:var(--fdisp);font-size:2.2rem;color:rgba(255,255,255,.92);letter-spacing:.02em;}
.poster .cap{padding:10px 12px;background:var(--e1);}
.poster .cap b{display:block;font-size:13px;font-weight:600;}
.poster .cap small{color:var(--dim);font-family:var(--fcond);text-transform:uppercase;font-size:10px;letter-spacing:.05em;}
.plist{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px;}
.plink{padding:9px 16px;border:1px solid var(--line2);border-radius:999px;font-family:var(--fcond);text-transform:uppercase;
 letter-spacing:.05em;font-size:12px;color:var(--mut);}
.plink:hover{border-color:var(--gold);color:var(--goldb);}
.plink.on{border-color:var(--a,var(--goldd));color:var(--tx);}
"""
def B_poster(initials,name,sub,href,accent):
    return ('<a class="poster" href="%s"><div class="art" style="--a:%s"><b>%s</b></div>'
            '<div class="cap"><b>%s</b><small>%s</small></div></a>')%(href,accent,initials,name,sub)
def B_panel_wrestlers():
    ps="".join(B_poster(i,n,"Profile",h,c) for n,i,h,c in FEATURED[:4])
    chips="".join('<a class="plink" style="--a:%s" href="/promotions/%s/">%s</a>'%(c,ab.lower(),n) for n,c,ab in PROMOS)
    return ('<div class="panel"><div class="phead">Wrestlers</div><div class="psub">Featured profiles</div>'
      '<div class="posters">'+ps+'</div><div class="plist">'+chips+'<a class="plink" href="/wrestlers/">All Wrestlers</a></div></div>')
def B_panel_events():
    ps="".join(B_poster(i,n,d,h,c) for n,i,d,h,c in EVENTS_RECENT)
    ps+=B_poster("ALL","All Events","Results","/events/","#8c7420")
    chips="".join('<a class="plink" href="%s">%s</a>'%(h,n) for n,h in EVENTS_BRANDS)
    return ('<div class="panel"><div class="phead">Premium Live Events</div><div class="psub">Recent shows &amp; brands</div>'
      '<div class="posters">'+ps+'</div><div class="plist">'+chips+'</div></div>')
def B_panel_moments():
    ps="".join(B_poster(i,n,s,h,"#7a1220") for n,i,s,h in MOMENTS)
    return ('<div class="panel"><div class="phead">Famous Moments</div><div class="psub">Iconic incidents, on video</div>'
      '<div class="posters">'+ps+'</div><div class="plist"><a class="plink" href="/moments/">All Moments</a></div></div>')

# ══════════════════════════════════════════════════════════════════════════
# THEME C — ARENA SPOTLIGHT (cinematic, featured hero card)
# ══════════════════════════════════════════════════════════════════════════
C_CSS = """
.hdr{position:sticky;top:0;z-index:100;background:rgba(8,9,11,.82);border-bottom:1px solid rgba(212,175,55,.14);backdrop-filter:blur(14px);}
.bar{display:flex;align-items:center;gap:2px;min-height:66px;}
.brand{font-family:var(--fdisp);font-size:1.55rem;margin-right:20px;display:flex;align-items:center;gap:10px;letter-spacing:.03em;}
.brand i{width:34px;height:34px;display:grid;place-items:center;border-radius:50%;font-style:normal;
 background:radial-gradient(circle at 30% 30%,var(--goldb),var(--goldd));color:#0a0b0d;font-size:1.05rem;box-shadow:0 0 18px rgba(212,175,55,.4);}
.nav-item{position:relative;}
.nav-tab{display:inline-flex;align-items:center;gap:8px;padding:22px 16px;color:var(--mut);font-family:var(--fcond);
 text-transform:uppercase;letter-spacing:.09em;font-weight:600;font-size:14px;cursor:pointer;border:0;background:none;}
.nav-tab svg{width:15px;height:15px;color:var(--dim);}
.nav-item:hover .nav-tab,.nav-item.open .nav-tab{color:var(--tx);text-shadow:0 0 16px rgba(212,175,55,.5);}
.spacer{flex:1;}
.srch{display:inline-flex;align-items:center;gap:9px;padding:10px 16px;border-radius:999px;color:var(--dim);cursor:pointer;
 background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);font-family:var(--fcond);text-transform:uppercase;letter-spacing:.07em;font-size:12px;}
.srch svg{width:15px;height:15px;}.srch:hover{border-color:var(--goldd);color:var(--tx);box-shadow:0 0 20px rgba(212,175,55,.2);}
.srch kbd{background:rgba(255,255,255,.06);border:1px solid var(--line2);border-radius:5px;padding:1px 6px;font-family:var(--fcond);font-size:11px;}
.panel{position:absolute;top:calc(100% + 8px);left:0;min-width:720px;display:none;border-radius:16px;overflow:hidden;
 background:linear-gradient(180deg,#0e1015,#090a0c);border:1px solid var(--line2);
 box-shadow:0 40px 100px rgba(0,0,0,.7),0 0 0 1px rgba(212,175,55,.06);}
.nav-item.open .panel{display:grid;grid-template-columns:1fr 1.1fr;animation:fc .22s var(--ease);}
@keyframes fc{from{opacity:0;transform:translateY(-10px) scale(.99);}to{opacity:1;transform:none;}}
.pleft{padding:24px;border-right:1px solid var(--line);}
.pleft h4{font-family:var(--fcond);text-transform:uppercase;letter-spacing:.14em;font-size:11px;color:var(--gold);margin:0 0 14px;}
.lrow{display:flex;align-items:center;gap:12px;padding:11px 12px;border-radius:10px;}
.lrow:hover{background:rgba(255,255,255,.04);}
.lrow .ic{width:32px;height:32px;flex:none;border-radius:8px;display:grid;place-items:center;font-family:var(--fdisp);font-size:12px;color:#fff;
 background:linear-gradient(145deg,var(--a,#8c7420),#0c0d10 78%);}
.lrow b{font-size:14px;font-weight:600;}.lrow small{display:block;color:var(--dim);font-size:11px;}
.pfeat{position:relative;padding:26px;display:flex;flex-direction:column;justify-content:flex-end;min-height:280px;
 background:radial-gradient(120% 90% at 80% 10%,var(--a) 0%,transparent 55%),linear-gradient(200deg,#14161c,#0a0b0d);}
.pfeat::after{content:"";position:absolute;inset:0;background:repeating-linear-gradient(0deg,transparent 0 3px,rgba(255,255,255,.02) 3px 4px);pointer-events:none;}
.pfeat .badge{font-family:var(--fcond);text-transform:uppercase;letter-spacing:.14em;font-size:11px;color:var(--goldb);position:relative;}
.pfeat h3{font-family:var(--fdisp);text-transform:uppercase;font-size:2.4rem;line-height:.92;margin:6px 0 4px;position:relative;
 color:transparent;background:linear-gradient(180deg,#fff,#c9ccd2);-webkit-background-clip:text;background-clip:text;}
.pfeat p{color:var(--mut);font-size:.95rem;max-width:36ch;position:relative;margin:0 0 16px;}
.pfeat .go{position:relative;align-self:flex-start;padding:11px 22px;border-radius:999px;font-family:var(--fcond);text-transform:uppercase;
 letter-spacing:.06em;font-weight:700;font-size:13px;background:linear-gradient(135deg,var(--goldb),var(--goldd));color:#0a0b0d;}
.pfeat .mk{position:absolute;top:20px;right:26px;font-family:var(--fdisp);font-size:5rem;color:rgba(255,255,255,.07);letter-spacing:.02em;}
"""
def C_left(rows):
    return "".join('<a class="lrow" href="%s"><span class="ic" style="--a:%s">%s</span><span><b>%s</b><small>%s</small></span></a>'%(h,c,i,n,s) for n,i,s,h,c in rows)
def C_panel_wrestlers():
    rows=[(n,i,"Profile",h,c) for n,i,h,c in FEATURED[:4]]
    left=C_left(rows)
    return ('<div class="panel"><div class="pleft"><h4>Featured Wrestlers</h4>'+left+
      '<a class="lrow" href="/wrestlers/"><span class="ic">AZ</span><span><b>All Wrestlers</b><small>Full roster</small></span></a></div>'
      '<a class="pfeat" href="/wrestlers/the-undertaker/" style="--a:rgba(107,70,193,.5)"><span class="mk">UT</span>'
      '<span class="badge">Featured Profile</span><h3>The Undertaker</h3>'
      '<p>The Streak, seven world titles, and the biker era — the complete record.</p><span class="go">View profile</span></a></div>')
def C_panel_events():
    rows=[(n,i,d,h,c) for n,i,d,h,c in EVENTS_RECENT]
    left=C_left(rows)
    return ('<div class="panel"><div class="pleft"><h4>Recent Events</h4>'+left+
      '<a class="lrow" href="/events/"><span class="ic">ALL</span><span><b>All Events</b><small>Results &amp; where to watch</small></span></a></div>'
      '<a class="pfeat" href="/events/wrestlemania-42-2026/" style="--a:rgba(212,175,55,.45)"><span class="mk">WM</span>'
      '<span class="badge">Latest · Apr 18–19, 2026</span><h3>WrestleMania 42</h3>'
      '<p>Cody Rhodes and Roman Reigns close two nights with world title wins in Las Vegas.</p><span class="go">Full results</span></a></div>')
def C_panel_moments():
    rows=[(n,i,s,h,"rgba(225,29,42,.4)") for n,i,s,h in MOMENTS[:4]]
    left=C_left(rows)
    return ('<div class="panel"><div class="pleft"><h4>Famous Moments</h4>'+left+
      '<a class="lrow" href="/moments/"><span class="ic">ALL</span><span><b>All Moments</b><small>Iconic incidents, on video</small></span></a></div>'
      '<a class="pfeat" href="/moments/mankind-hell-in-a-cell-fall-1998/" style="--a:rgba(225,29,42,.45)"><span class="mk">MK</span>'
      '<span class="badge">On video · King of the Ring 1998</span><h3>Hell in a Cell Fall</h3>'
      '<p>The Undertaker throws Mankind off the 16-foot cell. "He is broken in half."</p><span class="go">Watch the moment</span></a></div>')

# ── bar assembly ────────────────────────────────────────────────────────────
def tab(label, key, href, panel="", has=True):
    cls="nav-item has" if has else "nav-item"
    inner='<a class="nav-tab" href="%s">%s%s</a>%s'%(href,ICONS[key],label,panel)
    return '<li class="%s">%s</li>'%(cls,inner)

def bar(theme, pw, pe, pm):
    more=('<div class="panel" style="min-width:420px">'
      +('<div class="col"><h4>Explore</h4>' if theme=="A" else '<div class="pleft" style="border:0"><h4>Explore</h4>')
      +''.join('<a class="%s" href="%s">%s<span><b>%s</b><small>%s</small></span></a>'%(
          ("crow" if theme=="A" else "lrow"),h,(mono("".join(w[0] for w in n.split()[:2]),"#8c7420") if theme=="A" else '<span class="ic">'+ "".join(w[0] for w in n.split()[:2])+'</span>'),n,s)
        for n,s,h in [("Rivalries","Storylines & feuds","/rivalries/"),("Relationships","The real-life web","/relationships/"),("Rankings","All-time lists","/rankings/"),("About","How we rate","/about/"),("Methodology","Our sourcing","/methodology/")])
      +'</div></div>')
    tabs=(tab("Wrestlers","wrestlers","/wrestlers/",pw)
      +tab("Matches","matches","/matches/", ('<div class="panel" style="min-width:420px"></div>') if False else _matches_panel(theme))
      +tab("Events","events","/events/",pe)
      +tab("Moments","moments","/moments/",pm)
      +tab("More","more","/rankings/",more))
    return ('<header class="hdr"><div class="wrap"><ul class="bar" style="list-style:none;margin:0;padding:0">'
      '<li class="brand"><i>M</i>MAT'+('<small>Match · Athlete · Timeline</small>' if theme=="A" else '')+'</li>'
      +tabs+'<li class="spacer"></li>'
      '<li><button class="srch" data-open aria-label="Search">'+ICONS["search"]+' Search <kbd>⌘K</kbd></button></li>'
      '</ul></div></header>')

def _matches_panel(theme):
    picks=[("Undertaker vs HBK","UH","WrestleMania 25","/matches/undertaker-vs-hbk-wm25/","#6b46c1"),
           ("CM Punk vs Cena","PC","MITB 2011","/matches/cm-punk-vs-cena-mitb-2011/","#1f6f4a")]
    if theme=="A":
        rows="".join('<a class="crow" href="%s">%s<span><b>%s</b><small>%s</small></span></a>'%(h,mono(i,c),n,s) for n,i,s,h,c in picks)
        return ('<div class="panel" style="min-width:460px"><div class="col"><h4>Explore</h4>'
          '<a class="crow" href="/matches/">'+mono("ALL","#8c7420")+'<span><b>All Matches</b><small>Every rated bout</small></span></a>'
          '<a class="crow" href="/rankings/">'+mono("★","#8c7420")+'<span><b>Top-Rated (5★)</b><small>Five-star club</small></span></a></div>'
          '<div class="col"><h4>Editors’ Picks</h4>'+rows+'</div><div class="col"><h4>&nbsp;</h4></div></div>')
    if theme=="B":
        ps="".join(B_poster(i,n,s,h,c) for n,i,s,h,c in picks)
        return ('<div class="panel" style="min-width:520px"><div class="phead">Matches</div><div class="psub">Editors’ picks</div>'
          '<div class="posters" style="grid-template-columns:repeat(2,1fr)">'+ps+'</div>'
          '<div class="plist"><a class="plink" href="/matches/">All Matches</a><a class="plink" href="/rankings/">Top-Rated (5★)</a></div></div>')
    rows=[(n,i,s,h,c) for n,i,s,h,c in picks]
    return ('<div class="panel"><div class="pleft"><h4>Editors’ Picks</h4>'+C_left(rows)+
      '<a class="lrow" href="/matches/"><span class="ic">ALL</span><span><b>All Matches</b><small>Every rated bout</small></span></a></div>'
      '<a class="pfeat" href="/matches/undertaker-vs-hbk-wm25/" style="--a:rgba(107,70,193,.45)"><span class="mk">★</span>'
      '<span class="badge">5.0 · WrestleMania 25</span><h3>Taker vs HBK</h3><p>The match many call the greatest WrestleMania bout ever.</p><span class="go">Full breakdown</span></a></div>')

builds=[
 ("A","MAT Mega Nav — A · Broadcast Control Room", A_CSS,
   "Direction A · Broadcast Control Room — HUD telemetry, corner brackets, compact poster chips",
   A_panel_wrestlers(),A_panel_events(),A_panel_moments()),
 ("B","MAT Mega Nav — B · Editorial Poster Wall", B_CSS,
   "Direction B · Editorial Poster Wall — large duotone poster tiles, magazine typography",
   B_panel_wrestlers(),B_panel_events(),B_panel_moments()),
 ("C","MAT Mega Nav — C · Arena Spotlight", C_CSS,
   "Direction C · Arena Spotlight — cinematic glow, list + featured hero card",
   C_panel_wrestlers(),C_panel_events(),C_panel_moments()),
]
names={"A":"A-control-room","B":"B-editorial","C":"C-cinematic"}
for theme,title,css,note,pw,pe,pm in builds:
    html=page(title,css,bar(theme,pw,pe,pm),note)
    p=os.path.join(OUT,"MAT-meganav-%s.html"%names[theme])
    open(p,"w").write(html)
    print("wrote",p, round(len(html)/1024,1),"KB")
