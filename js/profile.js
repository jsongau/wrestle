document.documentElement.classList.add('js');
(function(){
  'use strict';
  var RM = window.matchMedia('(prefers-reduced-motion: reduce)');

  /* ---- smooth scroll for the discover button ---- */
  document.querySelectorAll('[data-scroll]').forEach(function(b){
    b.addEventListener('click',function(){
      var t=document.querySelector(b.getAttribute('data-scroll'));
      if(t) t.scrollIntoView({behavior:RM.matches?'auto':'smooth',block:'start'});
    });
  });

  /* ---- sub-nav scroll-spy + sliding indicator ---- */
  (function(){
    var bar=document.querySelector('.subnav'); if(!bar||!('IntersectionObserver'in window)) return;
    var ind=bar.querySelector('.subnav-ind');
    var css=getComputedStyle(document.documentElement);
    var stack=(parseInt(css.getPropertyValue('--nav-h'))||60)+(parseInt(css.getPropertyValue('--subnav-h'))||44)+(parseInt(css.getPropertyValue('--idbar-h'))||52);
    var links={}; bar.querySelectorAll('a').forEach(function(a){ links[a.hash.slice(1)]=a; });
    function moveInd(l){ if(!ind||!l) return; var br=bar.getBoundingClientRect(), lr=l.getBoundingClientRect();
      ind.style.left=(lr.left-br.left)+'px'; ind.style.width=lr.width+'px'; }
    function setActive(l){ bar.querySelectorAll('a[aria-current]').forEach(function(a){a.removeAttribute('aria-current');});
      l.setAttribute('aria-current','true'); moveInd(l); l.scrollIntoView({inline:'center',block:'nearest'}); }
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){ if(!e.isIntersecting) return; var l=links[e.target.id]; if(l) setActive(l); });
    },{rootMargin:'-'+(stack+10)+'px 0px -55% 0px',threshold:0});
    document.querySelectorAll('main section[id]').forEach(function(s){io.observe(s);});
    var first=bar.querySelector('a'); if(first){ requestAnimationFrame(function(){ moveInd(first); }); }
    window.addEventListener('resize',function(){ moveInd(bar.querySelector('a[aria-current]')||first); });
  })();

  /* ---- record tabs (APG pattern; all panels pre-rendered) ---- */
  document.querySelectorAll('[data-tabs]').forEach(function(g){
    var tabs=[].slice.call(g.querySelectorAll('[role="tab"]'));
    function sel(tab){
      tabs.forEach(function(t){
        var on=t===tab; t.setAttribute('aria-selected',on); t.tabIndex=on?0:-1;
        g.querySelector('#'+t.getAttribute('aria-controls')).hidden=!on;
      });
    }
    g.addEventListener('click',function(e){var t=e.target.closest('[role="tab"]');if(t)sel(t);});
    g.addEventListener('keydown',function(e){
      var i=tabs.indexOf(document.activeElement); if(i<0) return; var n;
      if(e.key==='ArrowRight')n=(i+1)%tabs.length; else if(e.key==='ArrowLeft')n=(i-1+tabs.length)%tabs.length;
      else if(e.key==='Home')n=0; else if(e.key==='End')n=tabs.length-1; else return;
      e.preventDefault(); tabs[n].focus(); sel(tabs[n]);
    });
  });

  /* ---- count-up stats (real number preserved) ---- */
  (function(){
    var els=document.querySelectorAll('[data-count]'); if(!('IntersectionObserver'in window)) return;
    els.forEach(function(el){
      var end=+el.getAttribute('data-count'); var suffix=el.querySelector('.x'); var sfx=suffix?suffix.outerHTML:'';
      var comma=el.getAttribute('data-format')==='comma';
      if(RM.matches) return;
      var io=new IntersectionObserver(function(es,ob){
        if(!es[0].isIntersecting) return; ob.disconnect();
        var t0=performance.now();
        (function tick(now){
          var p=Math.min((now-t0)/900,1); var v=Math.round(end*(1-Math.pow(1-p,3)));
          el.innerHTML=(comma?v.toLocaleString():v)+sfx;
          if(p<1) requestAnimationFrame(tick);
        })(t0);
      },{threshold:.6}); io.observe(el);
    });
  })();

  /* ---- match reel carousel ---- */
  (function(){
    var reel=document.querySelector('[data-reel]'); if(!reel) return;
    var slides=[].slice.call(reel.querySelectorAll('.track li'));
    var dots=[].slice.call(reel.querySelectorAll('.dots button'));
    var live=reel.querySelector('.track'); var playBtn=reel.querySelector('[data-play]');
    var i=0,timer=null;
    function show(n){
      slides[i].hidden=true; dots[i].setAttribute('aria-selected','false');
      i=(n+slides.length)%slides.length;
      slides[i].hidden=false; dots[i].setAttribute('aria-selected','true');
    }
    function play(){ if(RM.matches||timer) return; live.setAttribute('aria-live','off');
      timer=setInterval(function(){show(i+1);},5000); playBtn.textContent='❚❚'; playBtn.setAttribute('aria-label','Pause automatic rotation'); }
    function stop(){ clearInterval(timer); timer=null; live.setAttribute('aria-live','polite');
      playBtn.textContent='▶'; playBtn.setAttribute('aria-label','Start automatic rotation'); }
    reel.addEventListener('mouseenter',function(){ if(timer) stop(); });
    reel.addEventListener('mouseleave',function(){ if(!RM.matches&&!timer) play(); });
    reel.addEventListener('focusin',function(){ if(timer) stop(); });
    dots.forEach(function(d,n){ d.addEventListener('click',function(){ stop(); show(n); }); });
    playBtn.addEventListener('click',function(){ timer?stop():play(); });
    reel.querySelector('[data-dismiss]').addEventListener('click',function(){ stop(); reel.classList.add('gone'); });
    var hero=document.querySelector('#top');
    if(hero&&'IntersectionObserver'in window){
      new IntersectionObserver(function(es){
        if(!es[0].isIntersecting){ reel.classList.add('in'); play(); }
        else { reel.classList.remove('in'); stop(); }
      },{threshold:0}).observe(hero);
    } else { reel.classList.add('in'); play(); }
    var foot=document.querySelector('.foot');
    if(foot&&'IntersectionObserver'in window){
      new IntersectionObserver(function(es){ reel.classList.toggle('atfoot',es[0].isIntersecting); if(es[0].isIntersecting) stop(); },{rootMargin:'0px'}).observe(foot);
    }
  })();

  /* ---- action bar auto-hide at footer & at very top ---- */
  (function(){
    var ab=document.querySelector('[data-actionbar]'); var foot=document.querySelector('.foot');
    if(!ab) return;
    if(foot&&'IntersectionObserver'in window){
      new IntersectionObserver(function(es){ ab.classList.toggle('hide',es[0].isIntersecting); },{rootMargin:'0px'}).observe(foot);
    }
  })();

  /* ---- scroll reveal ---- */
  (function(){
    var els=document.querySelectorAll('.reveal'); if(!els.length) return;
    if(!('IntersectionObserver'in window)){ els.forEach(function(el){el.classList.add('in');}); return; }
    var io=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } }); },{rootMargin:'0px 0px -12% 0px',threshold:.08});
    els.forEach(function(el){ io.observe(el); });
  })();

  /* ---- shop / support panel ---- */
  (function(){
    var btn=document.querySelector('.shop-btn'), panel=document.getElementById('shop-panel'); if(!btn||!panel) return;
    function close(){ btn.setAttribute('aria-expanded','false'); panel.hidden=true; }
    btn.addEventListener('click',function(e){ e.stopPropagation();
      var open=btn.getAttribute('aria-expanded')==='true'; btn.setAttribute('aria-expanded',String(!open)); panel.hidden=open; });
    document.addEventListener('click',function(e){ if(!panel.hidden && !panel.contains(e.target)) close(); });
    document.addEventListener('keydown',function(e){ if(e.key==='Escape' && !panel.hidden){ close(); btn.focus(); } });
  })();

  /* ---- sortable record tables ---- */
  (function(){
    var MON={jan:0,feb:1,mar:2,apr:3,may:4,jun:5,jul:6,aug:7,sep:8,oct:9,nov:10,dec:11};
    function dateVal(s){ var m=s.match(/([A-Za-z]{3})\s+(\d{1,2})\s+'(\d{2})/); if(!m) return 0;
      var y=+m[3]; y+=(y>40?1900:2000); return new Date(y,MON[m[1].toLowerCase()]||0,+m[2]).getTime(); }
    function val(row,col){
      if(col==='result') return row.getAttribute('data-r')==='win'?1:0;
      if(col==='date'){ var d=row.querySelector('.dt'); return d?dateVal(d.textContent):0; }
      var c=row.querySelector(col==='opp'?'.opp':'.ev'); return c?c.textContent.trim().toLowerCase():'';
    }
    document.querySelectorAll('.rec-table').forEach(function(table){
      var ths=[].slice.call(table.querySelectorAll('th.sortable'));
      ths.forEach(function(th){
        th.setAttribute('tabindex','0'); th.setAttribute('role','button');
        function sort(){
          var col=th.getAttribute('data-col');
          var dir=th.getAttribute('aria-sort')==='ascending'?'descending':'ascending';
          ths.forEach(function(t){ t.removeAttribute('aria-sort'); });
          th.setAttribute('aria-sort',dir);
          var tb=table.querySelector('tbody'); var rows=[].slice.call(tb.querySelectorAll('tr'));
          rows.sort(function(a,b){ var va=val(a,col),vb=val(b,col); return (va<vb?-1:va>vb?1:0)*(dir==='ascending'?1:-1); });
          rows.forEach(function(r){ tb.appendChild(r); });
        }
        th.addEventListener('click',sort);
        th.addEventListener('keydown',function(e){ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); sort(); } });
      });
    });
  })();
})();

/* ===== mini-nav interactions ===== */
(function(){
  var idn=document.getElementById('idn'), hero=document.querySelector('.wl-dossier .hero');
  // Not every .wl-dossier page carries the sticky identity plate: the faction
  // pages use an .ev-hero instead. Without this guard onScroll() throws on the
  // first (immediate) call and takes the rest of this IIFE with it.
  if(!idn) return;
  function onScroll(){
    idn.classList.toggle('scrolled', window.scrollY > 40);           // breadcrumbs leave early
    var past = hero ? (window.scrollY > hero.offsetTop+hero.offsetHeight-180) : window.scrollY>220;
    idn.classList.toggle('condensed',past);                          // plate condenses past the hero
  }
  window.addEventListener('scroll',onScroll,{passive:true}); onScroll();
  var btn=document.querySelector('.js-idn'), panel=document.getElementById('idnPanel');
  if(btn){btn.addEventListener('click',function(e){e.stopPropagation();var o=panel.classList.toggle('open');btn.setAttribute('aria-expanded',o);});
    document.addEventListener('click',function(){panel.classList.remove('open');btn.setAttribute('aria-expanded',false);});}
})();
