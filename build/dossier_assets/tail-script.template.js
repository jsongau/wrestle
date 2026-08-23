
(function(){
  'use strict';
  /* cap a ledger at 8 visible rows; the rest scrolls inside the frame */
  function capRows(sc,tb,n){
    var th=sc.querySelector('thead');var rs=[].slice.call(tb.querySelectorAll('tr')).filter(function(r){return r.offsetHeight>0;});
    if(!th||rs.length<=n)return;
    var h=th.getBoundingClientRect().height;
    for(var i=0;i<n;i++){h+=rs[i].getBoundingClientRect().height;}
    sc.style.maxHeight=Math.ceil(h+1)+'px';
  }
  function capAll(){
    var b1=document.getElementById('rec2-body');
    if(b1)capRows(b1.closest('.rec2-scroll'),b1,8);
    var b2=document.getElementById('film-body');
    if(b2)capRows(b2.closest('.rec2-scroll'),b2,8);
  }
  if(document.readyState==='complete'){capAll();}else{window.addEventListener('load',capAll);}
  if(document.fonts&&document.fonts.ready){document.fonts.ready.then(capAll);}

  /* ===== Record ledger: spoilers + sorting + tri-scope filter + W/L stats ===== */
    var body=document.getElementById('rec2-body');
    if(body){
      var scroller=body.closest('.rec2-scroll');
      var thead=body.closest('table').querySelector('thead');
      var rows=[].slice.call(body.querySelectorAll('tr.rec2-row'));
      var shown=document.getElementById('rec2-shown');
      var countEl=document.getElementById('rec2-count');
      var emptyRow=document.getElementById('rec2-empty');
      var wlPanel=document.getElementById('rec2-wl');
      rows.forEach(function(r,i){r.setAttribute('data-idx',i);});
      /* spoiler shield */
      scroller.classList.add('rec2-spoiler');
      rows.forEach(function(r){
        var td=r.cells[0];if(!td||!td.querySelector('.rw'))return;
        var b=document.createElement('button');
        b.type='button';b.className='rw-show';b.textContent='Show';
        b.title='Click to show result';b.setAttribute('aria-label','Show result');
        td.insertBefore(b,td.firstChild);
        b.addEventListener('click',function(){r.classList.add('rev-open');});
      });
      /* win/loss stats panel, visible while spoilers are on */
      var DCIRC=2*Math.PI*44;
      function dseg(id,count,tot,off){
        var el=document.getElementById(id);if(!el)return off;
        var len=tot?DCIRC*count/tot:0;
        el.setAttribute('stroke-dasharray',len+' '+(DCIRC-len));
        el.setAttribute('stroke-dashoffset',String(-off));
        return off+len;
      }
      function setTxt(id,v){var el=document.getElementById(id);if(el)el.textContent=v;}
      function updateStats(){
        if(!wlPanel)return;
        var c={W:0,L:0,D:0,NC:0};
        rows.forEach(function(r){
          if(r.style.display==='none')return;
          var v=r.getAttribute('data-result');
          if(c.hasOwnProperty(v))c[v]++;
        });
        var tot=c.W+c.L+c.D+c.NC;
        var off=0;
        off=dseg('dn-w',c.W,tot,off);
        off=dseg('dn-l',c.L,tot,off);
        off=dseg('dn-d',c.D,tot,off);
        dseg('dn-n',c.NC,tot,off);
        setTxt('dn-pct',(tot?Math.round(100*c.W/tot):0)+'%');
        var rec=c.W+'-'+c.L;if(c.D)rec+='-'+c.D;
        setTxt('wl-rec',rec);
        setTxt('wl-w',c.W);setTxt('wl-l',c.L);setTxt('wl-d',c.D);setTxt('wl-n',c.NC);
      }
      var tgl=document.getElementById('splTgl');
      if(tgl){tgl.addEventListener('click',function(){
        var on=tgl.getAttribute('aria-pressed')!=='true';
        tgl.setAttribute('aria-pressed',on?'true':'false');
        tgl.querySelector('.spl-lbl').textContent=on?'Spoilers on':'Spoilers off';
        tgl.title=on?'Hide every result':'Show every win and loss';
        scroller.classList.toggle('rec2-spoiler',!on);
        setVeil(!on);
      });}
      function setVeil(veiled){
        if(!wlPanel)return;
        wlPanel.classList.toggle('rec2-wl-veiled',veiled);
        var g=wlPanel.querySelector('.rec2-donut'),s=wlPanel.querySelector('.rec2-wl-side');
        if(g)g.setAttribute('aria-hidden',veiled?'true':'false');
        if(s)s.setAttribute('aria-hidden',veiled?'true':'false');
        if(!veiled)updateStats();
      }
      var unveil=wlPanel?wlPanel.querySelector('.rec2-wl-unveil'):null;
      if(unveil&&tgl){unveil.addEventListener('click',function(){tgl.click();});}

      /* column sorting */
      function cellTxt(r,sel){var c=r.querySelector(sel);return c?c.textContent.trim().toLowerCase():'';}
      function keyVal(r,k){
        if(k==='date')return r.getAttribute('data-sort')||'';
        if(k==='res')return r.getAttribute('data-result')==='W'?'0':'1';
        if(k==='event')return cellTxt(r,'.rec2-ev');
        if(k==='opp')return cellTxt(r,'.rec2-opp').replace(/^[^a-z0-9]+/,'');
        if(k==='promo')return (r.getAttribute('data-promo')||'').toLowerCase();
        if(k==='stip')return cellTxt(r,'.rec2-stip');
        if(k==='title')return cellTxt(r,'.rec2-title').replace(/^[—\s]+/,'')||'zzz';
        return '';
      }
      var st={key:null,dir:1};
      thead.addEventListener('click',function(e){
        var th=e.target.closest('.rec2-sort');if(!th)return;
        var k=th.getAttribute('data-skey');
        if(st.key===k){st.dir=-st.dir;}else{st={key:k,dir:1};}
        thead.querySelectorAll('.rec2-sort').forEach(function(h){h.setAttribute('aria-sort','none');});
        th.setAttribute('aria-sort',st.dir===1?'ascending':'descending');
        rows.slice().sort(function(a,b){
          var va=keyVal(a,k),vb=keyVal(b,k);
          if(va<vb)return -st.dir;if(va>vb)return st.dir;
          return(+a.getAttribute('data-idx'))-(+b.getAttribute('data-idx'));
        }).forEach(function(r){body.appendChild(r);});
        if(emptyRow)body.appendChild(emptyRow);
        scroller.scrollTop=0;
      });

      /* tri-scope filter: scope (career-defining / full) + promo + type */
      var scopeFilter='cf',promoFilter='all',typeFilter='all';
      var PROMO_LABEL={PROMO_LABEL_JSON};
      function updatePillCounts(){
        var attr=(scopeFilter==='cf')?'data-clm':'data-cfull';
        [].forEach.call(document.querySelectorAll('#rec2-promo-filters [data-f],#rec2-type-filters [data-ft]'),function(btn){
          var span=btn.querySelector('span');if(!span)return;
          var v=btn.getAttribute(attr);if(v!==null)span.textContent=v;
        });
      }
      function capVisibleEight(){
        if(!scroller||!thead)return;
        var vis=rows.filter(function(r){return r.style.display!=='none';});
        if(vis.length<=8){scroller.style.maxHeight='';return;}
        var h=thead.getBoundingClientRect().height;
        for(var i=0;i<8;i++){h+=vis[i].getBoundingClientRect().height;}
        scroller.style.maxHeight=Math.ceil(h+1)+'px';
      }
      function applyFilters(){
        var n=0;
        rows.forEach(function(r){
          var scopeOk=scopeFilter==='all'||r.getAttribute('data-landmark')==='1';
          var promoOk=promoFilter==='all'||(r.getAttribute('data-promo')||'').toLowerCase()===promoFilter;
          var typeOk=typeFilter==='all'||(r.getAttribute('data-type')||'singles')===typeFilter;
          var ok=scopeOk&&promoOk&&typeOk;
          r.style.display=ok?'':'none';
          if(ok)n++;
        });
        if(emptyRow)emptyRow.hidden=(n!==0);
        if(shown)shown.textContent=n;
        if(countEl){
          var scopeWord=scopeFilter==='cf'?'career-defining ':'';
          var promoWord=promoFilter==='all'?'':(PROMO_LABEL[promoFilter]+' ');
          var typeWord=typeFilter==='tag'?'tag ':'';
          var noun=scopeFilter==='cf'?'bouts':'matches';
          countEl.textContent='Showing '+n+' '+scopeWord+promoWord+typeWord+noun+' of {TOTAL_MATCHES} total';
        }
        capVisibleEight();
        updateStats();
        if(scroller)scroller.scrollTop=0;
      }
      /* scope segmented control */
      var sfb=[].slice.call(document.querySelectorAll('#rec2-scope [data-scope]'));
      function setScope(v){
        scopeFilter=v;
        sfb.forEach(function(x){var on=x.getAttribute('data-scope')===v;x.classList.toggle('on',on);x.setAttribute('aria-checked',on?'true':'false');});
        updatePillCounts();applyFilters();
      }
      sfb.forEach(function(btn){btn.addEventListener('click',function(){setScope(btn.getAttribute('data-scope'));});});
      /* promo filter buttons */
      var pfb=[].slice.call(document.querySelectorAll('#rec2-promo-filters [data-f]'));
      pfb.forEach(function(btn){btn.addEventListener('click',function(){
        pfb.forEach(function(x){x.classList.remove('on');});
        btn.classList.add('on');
        promoFilter=btn.getAttribute('data-f');
        applyFilters();
      });});
      /* type filter buttons */
      var tfb=[].slice.call(document.querySelectorAll('#rec2-type-filters [data-ft]'));
      tfb.forEach(function(btn){btn.addEventListener('click',function(){
        tfb.forEach(function(x){x.classList.remove('on');});
        btn.classList.add('on');
        typeFilter=btn.getAttribute('data-ft');
        applyFilters();
      });});
      /* empty-state escape hatch */
      if(emptyRow){
        var seeAll=emptyRow.querySelector('[data-see-all]');
        if(seeAll){
          seeAll.addEventListener('click',function(){setScope('all');});
          seeAll.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();setScope('all');}});
        }
      }
      /* init: career-defining default */
      updatePillCounts();
      applyFilters();
    }

/* ===== Filmography: sorting + filters ===== */
  var fbody=document.getElementById('film-body');
  if(fbody){
    var ftable=fbody.closest('table'),fhead=ftable.querySelector('thead');
    var fscroll=ftable.closest('.rec2-scroll');
    var frows=[].slice.call(fbody.querySelectorAll('tr'));
    frows.forEach(function(r,i){r.setAttribute('data-idx',i);});
    var fshown=document.getElementById('film-shown');
    function fval(r,k){
      if(k==='year')return r.getAttribute('data-sort')||'';
      var sel=k==='role'?'.rec2-opp':(k==='note'?'td.dim:last-child':'.rec2-ev');
      var c=r.querySelector(sel);
      return c?c.textContent.trim().toLowerCase().replace(/^the /,''):'';
    }
    var fst={key:null,dir:1};
    fhead.addEventListener('click',function(e){
      var th=e.target.closest('.rec2-sort');if(!th)return;
      var k=th.getAttribute('data-fkey');
      if(fst.key===k){fst.dir=-fst.dir;}else{fst={key:k,dir:1};}
      fhead.querySelectorAll('.rec2-sort').forEach(function(h){h.setAttribute('aria-sort','none');});
      th.setAttribute('aria-sort',fst.dir===1?'ascending':'descending');
      frows.slice().sort(function(a,b){
        var va=fval(a,k),vb=fval(b,k);
        if(va<vb)return -fst.dir;if(va>vb)return fst.dir;
        return(+a.getAttribute('data-idx'))-(+b.getAttribute('data-idx'));
      }).forEach(function(r){fbody.appendChild(r);});
      fscroll.scrollTop=0;
    });
    var ffb=[].slice.call(document.querySelectorAll('[data-ff]'));
    ffb.forEach(function(btn){btn.addEventListener('click',function(){
      ffb.forEach(function(x){x.classList.remove('on');});
      btn.classList.add('on');
      var f=btn.getAttribute('data-ff'),n=0;
      frows.forEach(function(r){
        var ok=f==='all'
          ||(f==='disney'&&r.getAttribute('data-disney')==='1')
          ||(f==='voice'&&r.getAttribute('data-voice')==='1');
        r.style.display=ok?'':'none';if(ok)n++;
      });
      if(fshown)fshown.textContent=n;
      fscroll.scrollTop=0;
    });});

    /* ===== Concierge movie modal ===== */
    var host=document.querySelector('.wl-dossier')||document.body;
    var modal=document.createElement('div');
    modal.className='mv-modal';modal.hidden=true;
    modal.innerHTML='<div class="mv-backdrop" data-mv-close></div>'
      +'<div class="mv-card" role="dialog" aria-modal="true" aria-labelledby="mvTitle">'
      +'<button class="mv-x" type="button" data-mv-close aria-label="Close">&times;</button>'
      +'<p class="mv-eyebrow">Wrestle Lore Concierge</p>'
      +'<h3 class="mv-title" id="mvTitle"></h3>'
      +'<p class="mv-meta"></p>'
      +'<p class="mv-lead">The rating, or a place to watch it. Your call.</p>'
      +'<div class="mv-actions">'
      +'<a class="mv-btn mv-rt" target="_blank" rel="noopener noreferrer nofollow"><span class="mv-ic">RT</span><span class="mv-bt"><b>Rotten Tomatoes</b><span>See the Tomatometer &amp; reviews</span></span></a>'
      +'<a class="mv-btn mv-az" target="_blank" rel="noopener noreferrer nofollow"><span class="mv-ic">PV</span><span class="mv-bt"><b>Prime Video</b><span>Rent, buy or stream</span></span></a>'
      +'</div>'
      +'<p class="mv-note">Both open in a new tab and take you off Wrestle Lore to <b>Rotten Tomatoes</b> or <b>Prime Video</b>. We just point the way.</p>'
      +'</div>';
    host.appendChild(modal);
    var mvTitle=modal.querySelector('.mv-title'),mvMeta=modal.querySelector('.mv-meta'),
        mvRT=modal.querySelector('.mv-rt'),mvAZ=modal.querySelector('.mv-az'),
        mvClose=modal.querySelector('.mv-x'),lastFocus=null;
    function openMV(title,year,role){
      mvTitle.textContent=title;
      mvMeta.textContent=year+(role?'  ·  '+role:'');
      mvRT.href='https://www.rottentomatoes.com/search?search='+encodeURIComponent(title);
      mvAZ.href='https://www.amazon.com/s?k='+encodeURIComponent(title+' Dwayne Johnson')+'&i=instant-video';
      lastFocus=document.activeElement;
      modal.hidden=false;document.body.style.overflow='hidden';mvClose.focus();
    }
    function closeMV(){modal.hidden=true;document.body.style.overflow='';if(lastFocus&&lastFocus.focus)lastFocus.focus();}
    modal.addEventListener('click',function(e){if(e.target.hasAttribute('data-mv-close'))closeMV();});
    document.addEventListener('keydown',function(e){if(!modal.hidden&&e.key==='Escape')closeMV();});
    frows.forEach(function(r){
      var titleEl=r.querySelector('.rec2-ev');if(!titleEl)return;
      var title=titleEl.textContent.trim();
      var year=r.getAttribute('data-yr')||'';
      var role=r.children[2]?r.children[2].textContent.trim():'';
      var noteCell=r.children[3]||titleEl;
      var hint=document.createElement('span');hint.className='mv-hint';hint.textContent='Rate · Watch';
      noteCell.appendChild(hint);
      r.setAttribute('tabindex','0');r.setAttribute('role','button');
      r.setAttribute('aria-label','Ratings and where to watch '+title);
      r.addEventListener('click',function(){openMV(title,year,role);});
      r.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();openMV(title,year,role);}});
    });
  }
})();
