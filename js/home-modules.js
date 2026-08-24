/* Home interactive modules: mdx gorilla dossier, rfx roster files, ptk production truck. Ported from home-lower-v1. */

/* ============ HOME LOWER: roster files + production truck ============ */
(function(){
  'use strict';

  /* ---------- A. ROSTER FILES ---------- */
  var FILES=[
    {slug:'the-rock',mono:'R',name:'The Rock',aka:'The People’s Champion',era:'ATTITUDE // HOLLYWOOD',stamp:'FILE // LEGEND',
     stats:[{v:10,s:'World reigns',k:'8 WWE + 2 WCW'},{v:11,s:'Mania matches',k:'RECORD 6 AND 5'},{v:5,s:'Tag reigns',k:'PLUS 2 IC'}],
     extra:'ROYAL RUMBLE 2000 WINNER',
     blurb:'Third-generation star out of the Anoa’i line. Eight WWF and WWE Championships, two WCW World Championships, a record run of WrestleMania main events, then the biggest crossover to Hollywood the business has ever produced.',
     aliases:['ROCKY MAIVIA','THE BRAHMA BULL','THE GREAT ONE','THE FINAL BOSS']},
    {slug:'stone-cold-steve-austin',mono:'316',name:'Stone Cold Steve Austin',aka:'The Texas Rattlesnake',era:'ATTITUDE // 3:16',stamp:'FILE // LEGEND',
     stats:[{v:6,s:'WWF title reigns',k:'TOP OF THE CARD'},{v:3,s:'Royal Rumbles',k:'MOST ALL TIME'},{v:8,s:'Mania matches',k:'RECORD 6 AND 2'}],
     extra:'AUSTIN 3:16 SAID IT AT KING OF THE RING 1996',
     blurb:'The engine of the Attitude Era. Six WWF Championships, three Royal Rumble wins and a nightly war with the boss that turned Monday nights into the hottest show on television.',
     aliases:['THE RINGMASTER','STUNNING STEVE','THE RATTLESNAKE','THE BIONIC REDNECK']},
    {slug:'the-undertaker',mono:'21',name:'The Undertaker',aka:'The Phenom',era:'1990 TO 2020 // THE DEADMAN',stamp:'FILE // LEGEND',
     stats:[{v:21,s:'Streak wins',k:'21 AND 1 AT MANIA'},{v:7,s:'World reigns',k:'WWF AND WWE'},{v:30,s:'Years in the yard',k:'SURVIVOR SERIES 1990'}],
     extra:'THE STREAK STOOD FOR 23 YEARS',
     blurb:'Thirty years under the hat, from Survivor Series 1990 to the Boneyard. The Streak ran twenty one straight at WrestleMania and remains the measuring stick every big-match wrestler is held against.',
     aliases:['THE AMERICAN BADASS','BIG EVIL','THE DEADMAN','THE LORD OF DARKNESS']},
    {slug:'cm-punk',mono:'CP',name:'CM Punk',aka:'The Best in the World',era:'ACTIVE // CHAMPION',stamp:'FILE // ACTIVE',
     stats:[{v:434,s:'Days, 2011 reign',k:'MODERN ERA RECORD'},{v:0,s:'Days, current reign',k:'LIVE COUNT',live:'2026-07-06'},{v:2,s:'Money in the Bank',k:'BACK TO BACK'}],
     extra:'REIGNING UNDISPUTED WWE CHAMPION',
     blurb:'The pipebomb made him the voice of the voiceless; the 434-day reign made him a record book entry. Back from the wilderness and holding the Undisputed WWE Championship at the top of the current card.',
     aliases:['THE SECOND CITY SAINT','THE STRAIGHT EDGE SUPERSTAR','THE VOICE OF THE VOICELESS']}
  ];

  var rfx=document.getElementById('rfx');
  if(rfx){
    var tabs=rfx.querySelector('.rfx-tabs'),file=rfx.querySelector('.rfx-file'),sheet=rfx.querySelector('.rfx-sheet');
    var cur=0,aliasTimer=null,countRaf=null;
    FILES.forEach(function(f,i){
      var b=document.createElement('button');
      b.type='button';b.className='rfx-tab'+(i===0?' is-on':'');b.setAttribute('role','tab');
      b.innerHTML='<span class="rfx-tab__mono">'+f.mono+'</span><span><span class="rfx-tab__nm">'+f.name+'</span><span class="rfx-tab__era">'+f.era+'</span></span><span class="rfx-tab__pull">PULL</span>';
      b.addEventListener('click',function(){if(cur!==i){cur=i;render();}});
      tabs.appendChild(b);
    });
    function days(iso){return Math.max(1,Math.floor((Date.now()-new Date(iso+'T00:00:00Z').getTime())/864e5));}
    function render(){
      var f=FILES[cur];
      [].forEach.call(tabs.children,function(t,i){t.classList.toggle('is-on',i===cur);t.setAttribute('aria-selected',i===cur?'true':'false');});
      var statHtml=f.stats.map(function(s){
        var v=s.live?days(s.live):s.v;
        return '<div class="rfx-stat"><span class="rfx-stat__k">'+s.k+'</span><span class="rfx-stat__v" data-n="'+v+'">0</span><span class="rfx-stat__s">'+s.s+'</span></div>';
      }).join('');
      sheet.innerHTML=
        '<div class="rfx-head"><div><span class="rfx-kl">'+f.era+'</span>'+
        '<h3 class="rfx-name">'+f.name+'</h3><span class="rfx-aka">'+f.aka+'</span></div>'+
        '<span class="rfx-stamp">'+f.stamp+'</span></div>'+
        '<hr class="rfx-hair"><div class="rfx-stats">'+statHtml+'</div>'+
        '<p class="rfx-blurb">'+f.blurb+'</p>'+
        '<div class="rfx-alias"><b>ALSO ANSWERED TO</b><span class="rfx-alias-roll"><span>'+f.aliases[0]+'</span></span></div>'+
        '<div class="rfx-foot"><a class="rfx-open" href="https://wrestlelore.com/wrestlers/'+f.slug+'/">OPEN THE FULL FILE</a>'+
        '<span class="rfx-note">'+f.extra+'</span></div>';
      file.classList.remove('is-pulling');void file.offsetWidth;file.classList.add('is-pulling');
      countUp();aliasRoll(f);
    }
    function countUp(){
      if(countRaf)cancelAnimationFrame(countRaf);
      var els=[].slice.call(sheet.querySelectorAll('.rfx-stat__v')),t0=null;
      function step(ts){
        if(!t0)t0=ts;var p=Math.min(1,(ts-t0)/900),e=1-Math.pow(1-p,3);
        els.forEach(function(el){el.textContent=Math.round(e*parseInt(el.getAttribute('data-n'),10));});
        if(p<1)countRaf=requestAnimationFrame(step);
      }
      countRaf=requestAnimationFrame(step);
    }
    function aliasRoll(f){
      if(aliasTimer)clearInterval(aliasTimer);
      var k=0;
      aliasTimer=setInterval(function(){
        var roll=sheet.querySelector('.rfx-alias-roll');
        if(!roll){clearInterval(aliasTimer);return;}
        k=(k+1)%f.aliases.length;
        roll.innerHTML='<span>'+f.aliases[k]+'</span>';
      },2600);
    }
    render();
  }

  /* ---------- B. PRODUCTION TRUCK ---------- */
  var FEEDS=[
    {id:'wrestlers',cam:'CAM 1',name:'Wrestlers',s:'107 FILES',href:'/wrestlers/',sub:'107 PROFILES ON RECORD // CURRENT, LEGENDS, WOMEN'},
    {id:'matches',cam:'CAM 2',name:'Matches',s:'30 RATED',href:'/matches/',sub:'30 BOUTS ON THE FIVE STAR LADDER'},
    {id:'events',cam:'CAM 3',name:'Events',s:'2026 SEASON',href:'/events/',sub:'SUMMERSLAM // US BANK STADIUM // MINNEAPOLIS'},
    {id:'promotions',cam:'CAM 4',name:'Promotions',s:'7 FEEDS',href:'/promotions/',sub:'SEVEN PROMOTIONS PLUS AAA THROUGH THE WWE PARTNERSHIP'},
    {id:'hof',cam:'CAM 5',name:'Hall of Fame',s:'CLASS OF 26',href:'/hall-of-fame/',sub:'AJ STYLES HEADLINES THE CLASS OF 2026'},
    {id:'titles',cam:'CAM 6',name:'Titles &amp; Teams',s:'11 LINEAGES',href:'/titles/',sub:'REIGN CLOCKS RUN LIVE // 11 LINEAGES TRACKED'},
    {id:'media',cam:'CAM 7',name:'Media',s:'THE WIRE',href:'/media/',sub:'PRESS ROW, THE LORE FEED AND THE ISO CAM'}
  ];
  var ROSTER=['ROMAN REIGNS','CODY RHODES','RHEA RIPLEY','CM PUNK','GUNTHER','THE ROCK','STONE COLD','THE UNDERTAKER'];
  var CLASSICS=[['UNDERTAKER VS MICHAELS','WRESTLEMANIA XXV // 2009',5],['PUNK VS CENA','MONEY IN THE BANK // 2011',5],['GARGANO VS CIAMPA','TAKEOVER NEW ORLEANS // 2018',5],['REY VS EDDIE','HALLOWEEN HAVOC // 1997',5]];
  var WIRE=['<b>Kenny Omega</b> retains the AEW World Championship at Redemption','<b>Cody Rhodes</b> and CM Punk come face to face on SmackDown','<b>Gunther</b> leaves Nick Aldis laid out at the contract signing','<b>Willow Nightingale</b> captures the AEW Women’s World Championship'];
  var REIGNS=[['Undisputed WWE Championship','CM PUNK','2026-07-06'],['World Heavyweight Championship','ROMAN REIGNS','2026-04-19'],['Intercontinental Championship','PENTA','2026-03-02']];

  var ptk=document.getElementById('ptk');
  if(ptk){
    var bank=ptk.querySelector('.ptk-bank'),vig=ptk.querySelector('.ptk-vig'),
        pgmname=ptk.querySelector('.ptk-pgmname'),take=ptk.querySelector('.ptk-take'),
        sub=ptk.querySelector('.ptk-sub'),clock=ptk.querySelector('.ptk-clock');
    var on=0,cycle=null,inner=null,hold=false;
    FEEDS.forEach(function(fd,i){
      var b=document.createElement('button');
      b.type='button';b.className='ptk-cam'+(i===0?' is-on':'');b.setAttribute('role','tab');
      b.innerHTML='<span class="ptk-cam__id">'+fd.cam+'</span><span class="ptk-cam__nm">'+fd.name+'</span><span class="ptk-cam__s">'+fd.s+'</span>';
      b.addEventListener('click',function(){take2(i,true);});
      bank.appendChild(b);
    });
    function dd(iso){return Math.max(1,Math.floor((Date.now()-new Date(iso+'T00:00:00Z').getTime())/864e5));}
    function pad(n){return (n<10?'0':'')+n;}
    var V={
      wrestlers:function(){
        vig.innerHTML='<span class="ptk-kl">THE ROSTER ROLL</span><div class="ptk-big"><span class="ptk-flip">'+ROSTER[0]+'</span></div><div class="ptk-under"><b>107</b> FILES ON RECORD // CURRENT, LEGENDS, WOMEN</div>';
        var k=0,big=vig.querySelector('.ptk-big');
        inner=setInterval(function(){k=(k+1)%ROSTER.length;big.innerHTML='<span class="ptk-flip">'+ROSTER[k]+'</span>';},1500);
      },
      matches:function(){
        function show(k){
          var c=CLASSICS[k];
          vig.innerHTML='<span class="ptk-kl">'+c[1]+'</span><div class="ptk-big ptk-flip">'+c[0]+'</div>'+
          '<div class="ptk-stars">&starf;&starf;&starf;&starf;&starf;<span class="on" style="--fill:'+(c[2]*20)+'%">&starf;&starf;&starf;&starf;&starf;</span></div>'+
          '<div class="ptk-under"><b>'+c[2].toFixed(1)+'</b> ON THE LADDER // <b>30</b> BOUTS RATED</div>';
        }
        show(0);var k=0;
        inner=setInterval(function(){k=(k+1)%CLASSICS.length;show(k);},3400);
      },
      events:function(){
        vig.innerHTML='<span class="ptk-kl">NEXT STOP // SUNDAY NIGHT\'S MAIN EVENT // SEP 6</span><div class="ptk-count">'+
          '<div class="ptk-cell"><b data-u="d">0</b><span>DAYS</span></div><div class="ptk-cell"><b data-u="h">0</b><span>HRS</span></div>'+
          '<div class="ptk-cell"><b data-u="m">0</b><span>MIN</span></div><div class="ptk-cell"><b data-u="s">0</b><span>SEC</span></div></div>'+
          '<div class="ptk-under">STATE FARM ARENA // ATLANTA // ONE NIGHT</div>';
        var T=new Date('2026-09-06T20:00:00-04:00').getTime();
        function tick(){
          var ms=Math.max(0,T-Date.now()),d=Math.floor(ms/864e5),h=Math.floor(ms/36e5)%24,m=Math.floor(ms/6e4)%60,s=Math.floor(ms/1e3)%60;
          var q=function(u){var el=vig.querySelector('[data-u="'+u+'"]');return el;};
          if(!q('d'))return;
          q('d').textContent=pad(d);q('h').textContent=pad(h);q('m').textContent=pad(m);q('s').textContent=pad(s);
        }
        tick();inner=setInterval(tick,1000);
      },
      promotions:function(){
        var B=[['WWE','#c8102e',1.7],['WCW','#e8b50c',2.1],['ECW','#b8b8bc',1.4],['TNA','#2f7de1',1.9],['NXT','#c9a227',1.6],['NJPW','#7f4fd0',2.2],['AEW','#c9a86a','1.8'],['AAA','#0aa574',2.0]];
        vig.innerHTML='<span class="ptk-kl">EVERY TERRITORY ON THE BOARD</span><div class="ptk-eq">'+
          B.map(function(x,i){return '<div class="ptk-bar" style="--bc:'+x[1]+';height:'+(58+((i*29)%52))+'px;animation-duration:'+x[2]+'s"><i>'+x[0]+'</i></div>';}).join('')+
          '</div><div class="ptk-under" style="margin-top:26px"><b>7</b> PROMOTION HUBS // AAA THROUGH THE WWE PARTNERSHIP</div>';
      },
      hof:function(){
        vig.innerHTML='<span class="ptk-kl">CLASS OF 2026 // FIRST IN</span>'+
          '<div class="ptk-medal"><svg viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="53" fill="none" stroke="currentColor" stroke-width="1" opacity=".55"/><circle cx="60" cy="60" r="45" fill="none" stroke="currentColor" stroke-width=".5" opacity=".32"/><g stroke="currentColor" stroke-width="1" opacity=".38"><line x1="60" y1="4" x2="60" y2="12"/><line x1="60" y1="108" x2="60" y2="116"/><line x1="4" y1="60" x2="12" y2="60"/><line x1="108" y1="60" x2="116" y2="60"/></g><text class="ptk-mono" x="60" y="69">AJ</text></svg></div>'+
          '<div class="ptk-big" style="font-size:clamp(26px,3.4vw,38px)">AJ STYLES</div>'+
          '<div class="ptk-under">THE PHENOMENAL ONE GOES IN FIRST // <b>CLASS OF 2026</b></div>';
      },
      titles:function(){
        vig.innerHTML='<span class="ptk-kl">THE REIGN CLOCKS // RUNNING LIVE</span><div class="ptk-reigns">'+
          REIGNS.map(function(r){return '<div class="ptk-reign"><span class="ptk-reign__t">'+r[1]+'<em>'+r[0]+'</em></span><span class="ptk-reign__d">DAY '+dd(r[2])+'</span></div>';}).join('')+
          '</div>';
      },
      media:function(){
        function show(k){
          vig.innerHTML='<span class="ptk-rec"><i></i>REC // THE WIRE</span><p class="ptk-wire ptk-flip">'+WIRE[k]+'</p>'+
            '<div class="ptk-under" style="margin-top:14px">PRESS ROW // ISO CAM // LORE FEED</div>';
        }
        show(0);var k=0;
        inner=setInterval(function(){k=(k+1)%WIRE.length;show(k);},3200);
      }
    };
    function take2(i,user){
      if(inner){clearInterval(inner);inner=null;}
      on=i;var fd=FEEDS[i];
      [].forEach.call(bank.children,function(c,j){c.classList.toggle('is-on',j===i);c.setAttribute('aria-selected',j===i?'true':'false');});
      pgmname.textContent=fd.name.replace('&amp;','&');take.setAttribute('href',fd.href);sub.textContent=fd.sub;
      ptk.classList.remove('is-cutting');void ptk.offsetWidth;ptk.classList.add('is-cutting');
      V[fd.id]();
      if(user){hold=true;clearTimeout(take2._h);take2._h=setTimeout(function(){hold=false;},22000);}
    }
    setInterval(function(){
      if(hold||ptk.matches(':hover'))return;
      var r=ptk.getBoundingClientRect();
      if(r.bottom<0||r.top>innerHeight)return;
      take2((on+1)%FEEDS.length,false);
    },6500);
    setInterval(function(){
      var d=new Date();
      clock.textContent=pad(d.getHours())+':'+pad(d.getMinutes())+':'+pad(d.getSeconds());
    },1000);
    take2(0,false);
  }
})();


/* ---- block ---- */


/* ===================== MATCH DESK V2 — controller ===================== */
(function () {
  'use strict';
  var grid = document.querySelector('[data-mdx]');
  if (!grid) return;
  var $ = function (sel) { return grid.querySelector(sel); };

  var HOME = '';
  var MATCHES = [
    {
      id: 'Gd54flkPtL4', slug: 'undertaker-vs-hbk-wm25',
      title: 'The Undertaker vs Shawn Michaels',
      short: 'Undertaker vs Michaels',
      event: 'WrestleMania XXV · 2009 · Reliant Stadium, Houston',
      meta: 'WrestleMania XXV · 2009',
      rate: '5.0', stars: 5, tag: 'Five-Star Club', chip: 'WWE', chipCls: 'chip chip--wwe', era: 'Ruthless Aggression',
      klbl: 'GOLD EDGE // MATCH OF RECORD',
      srcM: 'Meltzer ★★★★¾ (4.75)', srcC: 'Cagematch ~9.6 / 10',
      hook: 'Two legends in their forties staged the most dramatic false-finish war WrestleMania has ever seen, and it is regularly voted the greatest Mania match of all time.',
      winner: 'The Undertaker', result: 'Undertaker def. Michaels (17–0)',
      frame: 1, art: ['maxresdefault', 'sd3', 'hqdefault']
    },
    {
      id: '0MS9CY_Gn7E', slug: 'hbk-vs-razor-ramon-wrestlemania-x',
      title: 'Shawn Michaels vs Razor Ramon',
      short: 'Michaels vs Razor Ramon',
      event: 'WrestleMania X · 1994 · Madison Square Garden',
      meta: 'WrestleMania X · 1994',
      rate: '5.0', stars: 5, tag: 'Five-Star Club', chip: 'WWF', chipCls: 'chip chip--wwe', era: 'New Generation',
      klbl: 'CUE 02 // THE LADDER BLUEPRINT',
      srcM: 'Meltzer ★★★★★ (5.0)', srcC: '',
      hook: 'The ladder match that invented the genre. Two Intercontinental Titles hung above the ring, and every ladder spot of the next thirty years traces back to this night.',
      winner: 'Razor Ramon', result: 'Razor Ramon def. Michaels (unified the Intercontinental Title)',
      frame: 2, art: ['maxresdefault', 'sd1', 'hqdefault']
    },
    {
      id: 'BvZ2KQuCTds', slug: 'hbk-vs-undertaker-badd-blood-1997',
      title: 'Shawn Michaels vs The Undertaker',
      short: 'Michaels vs Undertaker',
      event: 'In Your House 18: Badd Blood · 1997 · Kiel Center',
      meta: 'Badd Blood · 1997',
      rate: '4.5', stars: 4.5, tag: 'Near Miss', chip: 'WWF', chipCls: 'chip chip--wwe', era: 'Attitude Era',
      klbl: 'CUE 03 // THE FIRST CELL',
      srcM: 'Meltzer ★★★★¾ (4.75)', srcC: 'Cagematch ~9.0 / 10',
      hook: 'The first Hell in a Cell. Sixteen feet of steel, a bloodied Showstopper, and a mid-match debut that rewired the main event scene for a decade.',
      winner: 'Shawn Michaels', result: 'Michaels def. Undertaker (Kane debut)',
      frame: 3
    },
    {
      id: 'ljb34LNhGQw', slug: 'undertaker-vs-hbk-wm26-2010',
      title: 'The Undertaker vs Shawn Michaels (Streak vs Career)',
      short: 'Streak vs Career',
      event: 'WrestleMania XXVI · 2010 · University of Phoenix Stadium',
      meta: 'WrestleMania XXVI · 2010',
      rate: '4.5', stars: 4.5, tag: 'Near Miss', chip: 'WWE', chipCls: 'chip chip--wwe', era: 'PG Era',
      klbl: 'CUE 04 // STREAK VS CAREER',
      srcM: 'Meltzer ★★★★½ (4.5)', srcC: 'Cagematch ~9.4 / 10',
      hook: 'No belt on the line. If the Streak survives, the Showstopper retires. A sequel with stakes the original never had.',
      winner: 'The Undertaker', result: 'Undertaker def. Michaels (18–0); HBK retired',
      frame: 1, art: ['maxresdefault', 'sd2', 'hqdefault']
    },
    {
      id: 'RnTd_Gznjd8', slug: 'hbk-vs-jericho-wm19-2003',
      title: 'Shawn Michaels vs Chris Jericho',
      short: 'Michaels vs Jericho',
      event: 'WrestleMania XIX · 2003 · Safeco Field, Seattle',
      meta: 'WrestleMania XIX · 2003',
      rate: '4.5', stars: 4.5, tag: 'Near Miss', chip: 'WWE', chipCls: 'chip chip--wwe', era: 'Ruthless Aggression',
      klbl: 'CUE 05 // IDOL VS UNDERSTUDY',
      srcM: 'Meltzer ★★★★¼ (4.25)', srcC: '',
      hook: 'Jericho grew up studying the Showstopper, then met him at Safeco Field to prove the understudy had passed the original. Twenty two minutes of one-upmanship between mentor and mirror.',
      winner: 'Shawn Michaels', result: 'Michaels def. Jericho (bridging roll-up at 22:34)',
      frame: 2, page: '/matches/'
    },
    {
      id: 'jphS4xGOBFQ', slug: 'triple-h-vs-hbk-summerslam-2002',
      title: 'Triple H vs Shawn Michaels',
      short: 'Triple H vs Michaels',
      event: 'SummerSlam 2002 · 2002 · Nassau Coliseum',
      meta: 'SummerSlam 2002',
      rate: '4.0', stars: 4, tag: 'Rated Classic', chip: 'WWE', chipCls: 'chip chip--wwe', era: 'Ruthless Aggression',
      klbl: 'CUE 06 // THE DX CIVIL WAR',
      srcM: 'Meltzer ★★★★¼ (4.25)', srcC: '',
      hook: 'Michaels had not wrestled in over four years and a broken back was supposed to have ended him. His best friend turned on him, and they settled it in an unsanctioned street fight of ladders, chairs, and history.',
      winner: 'Shawn Michaels', result: 'Michaels def. Triple H',
      frame: 3, art: ['maxresdefault', 'sd1', 'hqdefault']
    },
    {
      id: 'NTpGZUO3gFE', slug: 'rockers-vs-brain-busters-msg-1989',
      title: 'The Rockers vs The Brain Busters',
      short: 'The Rockers vs the Busters',
      event: 'WWE on MSG · Jan 23, 1989 · Madison Square Garden',
      meta: 'MSG · 1989',
      rate: '4.5', stars: 4.5, tag: 'Vault Classic', chip: 'WWF', chipCls: 'chip chip--wwe', era: 'Golden Era',
      klbl: 'CUE 07 // THE ROCKERS FILE',
      srcM: 'Tape classic · MSG, Jan 23 1989', srcC: '',
      hook: 'Before the Showstopper there were the Rockers. Michaels and Jannetty against Anderson and Blanchard, four of the sharpest tag wrestlers alive trading holds at full speed in the Garden.',
      winner: 'The Brain Busters', result: 'Anderson & Blanchard def. The Rockers (Anderson tripped Jannetty from the floor)',
      frame: 1, art: ['sd3', 'hq3', 'hqdefault'], page: '/matches/'
    }
  ];

  /* distinct art from the /matches/ page: film-strip frames instead of the default thumb,
     with an optional per-match override (m.art = ordered list of frame names) */
  function art(m) {
    var base = 'https://i.ytimg.com/vi/' + m.id + '/';
    var names = m.art || ['sd' + m.frame, 'hq' + m.frame, 'hqdefault'];
    return names.map(function (n) { return 'url(' + base + n + '.jpg)'; }).join(',');
  }
  function pageUrl(m) { return m.page || (HOME + '/matches/' + m.slug + '/'); }
  function starsRow(n) {
    var full = Math.floor(n), half = n % 1 >= 0.5;
    var s = '';
    for (var i = 0; i < full; i++) s += '★';
    if (half) s += '½';
    return s;
  }

  var el = {
    hspot: document.querySelector('.hspot[data-hspot]'),
    hgrid: document.querySelector('.hrl-grid'),
    playBtn: document.querySelector('.hspot__play'),
    picks: $('[data-mdx-picks]'),
    screen: $('[data-mdx-screen]'),
    bgA: $('[data-mdx-bg-a]'), bgB: $('[data-mdx-bg-b]'),
    klbl: $('[data-mdx-klbl]'),
    info: $('[data-mdx-info]'),
    rank: $('[data-mdx-rank]'), tag: $('[data-mdx-tag]'), chip: $('[data-mdx-chip]'), era: $('[data-mdx-era]'),
    title: $('[data-mdx-title]'), event: $('[data-mdx-event]'), hook: $('[data-mdx-hook]'),
    starsrow: $('[data-mdx-starsrow]'), score: $('[data-mdx-score]'), srcM: $('[data-mdx-src-m]'), srcC: $('[data-mdx-src-c]'),
    watch1: $('[data-mdx-watch]'), watch2: $('[data-mdx-watch2]'),
    break1: $('[data-mdx-break]'), break2: $('[data-mdx-break2]'),
    play: $('[data-mdx-play]'),
    open1: $('[data-mdx-open]'), close: $('[data-mdx-close]'),
    bell: $('[data-mdx-bell]'), ringOpen: $('[data-mdx-ring-open]'), ringClose: $('[data-mdx-ring-close]'),
    spoiler: $('[data-mdx-spoiler]'), winner: $('[data-mdx-winner]'), result: $('[data-mdx-result]'), reveal: $('[data-mdx-reveal]'),
    stars: $('[data-mdx-stars]'), rateval: $('[data-mdx-rateval]'),
    insider: $('[data-mdx-insider]'), insiderTxt: $('[data-mdx-insider-txt]'), insiderNo: $('[data-mdx-insider-no]')
  };

  var cur = 0, deskOpen = false, frontIsA = false;
  var revealed = {}, ballots = {}, wasPlaying = false;

  /* ---------- build the picker rail ---------- */
  MATCHES.forEach(function (m, k) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'mdx-pick' + (k === cur ? ' is-on' : '');
    b.setAttribute('data-k', k);
    b.setAttribute('aria-pressed', k === cur ? 'true' : 'false');
    b.innerHTML =
      '<span class="mdx-pick__no">0' + (k + 1) + '</span>' +
      '<span class="mdx-pick__body"><span class="mdx-pick__nm"></span><span class="mdx-pick__meta"></span></span>' +
      '<span class="mdx-pick__sc">' + m.rate + '</span>';
    b.querySelector('.mdx-pick__nm').textContent = m.title;
    b.querySelector('.mdx-pick__meta').textContent = m.meta;
    b.addEventListener('click', function () { select(k); });
    el.picks.appendChild(b);
  });

  /* ---------- render the screen for match k ---------- */
  function render(k, animate) {
    var m = MATCHES[k];
    cur = k;

    /* crossfade the two art layers */
    var front = frontIsA ? el.bgA : el.bgB;
    var back = frontIsA ? el.bgB : el.bgA;
    back.style.backgroundImage = art(m);
    back.classList.add('is-live');
    back.style.opacity = '1';
    front.style.opacity = '0';
    front.classList.remove('is-live');
    frontIsA = !frontIsA;

    el.klbl.textContent = m.klbl;
    el.rank.innerHTML = (m.stars === 5 ? '5★' : '4½★');
    el.tag.textContent = m.tag;
    el.chip.textContent = m.chip;
    el.era.textContent = m.era;
    el.title.textContent = m.title;
    el.event.textContent = m.event;
    el.hook.textContent = m.hook;
    el.starsrow.textContent = starsRow(m.stars);
    el.score.textContent = m.rate;
    el.srcM.textContent = m.srcM;
    el.srcC.textContent = m.srcC || '';
    el.srcC.hidden = !m.srcC;
    el.winner.textContent = m.winner;
    el.result.textContent = m.result;
    [el.watch1, el.watch2, el.break1, el.break2].forEach(function (a) { if (a) a.href = pageUrl(m); });
    el.screen.setAttribute('aria-label', 'Featured match: ' + m.title + ', ' + m.event);

    /* sealed state per match */
    var open = !!revealed[m.slug];
    el.spoiler.classList.toggle('is-open', open);
    el.reveal.setAttribute('aria-expanded', open ? 'true' : 'false');
    el.reveal.lastChild.textContent = open ? 'On the record' : 'Reveal winner';

    /* ballot per match */
    paintStars(ballots[m.slug] || 0, false);
    el.rateval.textContent = ballots[m.slug] ? ballots[m.slug] + '.0' : '';
    el.insider.classList.remove('is-on');

    /* picker state */
    [].slice.call(el.picks.children).forEach(function (p, i) {
      p.classList.toggle('is-on', i === k);
      p.setAttribute('aria-pressed', i === k ? 'true' : 'false');
    });

    if (animate) {
      el.info.classList.remove('is-in');
      void el.info.offsetHeight;
      el.info.classList.add('is-in');
    }
    var onPick = el.picks.children[k];
    if (deskOpen && onPick && onPick.scrollIntoView) { try { onPick.scrollIntoView({ block: 'nearest' }); } catch (err) {} }
  }

  /* ---------- compact-mode shuffle: the featured match rotates until the bell rings ----------
     Two triggers: (1) every time the carousel cycles back to slide 1, deal the next match;
     (2) while slide 1 stays on screen (carousel paused or wrapped), rotate on a timer. */
  var slide1 = grid.closest('.hspot__slide');
  var hovered = false;
  grid.addEventListener('mouseenter', function () { hovered = true; });
  grid.addEventListener('mouseleave', function () { hovered = false; });
  function shuffleNext() { render((cur + 1) % MATCHES.length, false); }
  if (slide1 && typeof MutationObserver !== 'undefined') {
    var wasActive = slide1.classList.contains('is-active');
    new MutationObserver(function () {
      var isActive = slide1.classList.contains('is-active');
      if (isActive && !wasActive && !deskOpen) shuffleNext();
      wasActive = isActive;
    }).observe(slide1, { attributes: true, attributeFilter: ['class'] });
  }
  setInterval(function () {
    if (deskOpen || hovered || document.hidden) return;
    if (slide1 && !slide1.classList.contains('is-active')) return;
    shuffleNext();
  }, 8000);

  function select(k) { if (k !== cur) render(k, true); }

  /* ---------- the modal theater ---------- */
  function playCurrent(e) {
    if (e) e.preventDefault();
    var m = MATCHES[cur];
    if (window.WL && window.WL.openModal) {
      window.WL.openModal(m.id, m.title + ', ' + m.meta, {
        service: 'Peacock',
        serviceUrl: 'https://www.peacocktv.com/sports/wwe',
        page: pageUrl(m)
      });
    } else {
      window.open('https://www.youtube.com/watch?v=' + m.id, '_blank', 'noopener');
    }
  }
  [el.watch1, el.watch2, el.play].forEach(function (b) { if (b) b.addEventListener('click', playCurrent); });
  el.screen.addEventListener('click', function (e) {
    if (deskOpen) return; /* in desk mode the inner controls own the clicks */
    if (e.target.closest('a,button')) return;
    playCurrent(e);
  });

  /* ---------- desk open and close ---------- */
  function pauseCarousel() {
    if (!el.playBtn) return;
    wasPlaying = el.playBtn.getAttribute('data-playing') === 'true';
    if (wasPlaying) el.playBtn.click();
  }
  function resumeCarousel() {
    if (el.playBtn && wasPlaying && el.playBtn.getAttribute('data-playing') === 'false') el.playBtn.click();
  }
  function openDesk() {
    if (deskOpen) return;
    deskOpen = true;
    pauseCarousel();
    grid.classList.add('is-desk');
    if (el.hgrid) el.hgrid.classList.add('is-desk');
    if (el.hspot) el.hspot.classList.add('is-desk');
    el.open1.setAttribute('aria-expanded', 'true');
    syncBell();
    render(cur, true);
    el.close.focus({ preventScroll: true });
  }
  function closeDesk() {
    if (!deskOpen) return;
    deskOpen = false;
    grid.classList.remove('is-desk');
    if (el.hgrid) el.hgrid.classList.remove('is-desk');
    if (el.hspot) el.hspot.classList.remove('is-desk');
    el.open1.setAttribute('aria-expanded', 'false');
    syncBell();
    render(0, false);
    resumeCarousel();
    el.open1.focus({ preventScroll: true });
    try { window.dispatchEvent(new Event('resize')); } catch (err) {}
  }
  /* ---------- the bell's voice: a synthesized ring bell, no audio files ---------- */
  var actx = null;
  function strike(t, vol) {
    /* inharmonic partials approximating a struck steel ring bell */
    var partials = [[1046, 1], [1735, .55], [2310, .38], [2940, .22], [640, .3]];
    partials.forEach(function (p) {
      var o = actx.createOscillator(), g = actx.createGain();
      o.type = 'sine';
      o.frequency.setValueAtTime(p[0] * (1 + (Math.sin(p[0]) * .002)), t);
      g.gain.setValueAtTime(.0001, t);
      g.gain.exponentialRampToValueAtTime(vol * p[1], t + .006);
      g.gain.exponentialRampToValueAtTime(.0001, t + 1.15);
      o.connect(g); g.connect(actx.destination);
      o.start(t); o.stop(t + 1.25);
    });
  }
  function bellSound(times) {
    try {
      actx = actx || new (window.AudioContext || window.webkitAudioContext)();
      if (actx.state === 'suspended') actx.resume();
      for (var i = 0; i < times; i++) strike(actx.currentTime + .02 + i * .24, .085);
    } catch (e) {}
  }
  function clang(times) {
    bellSound(times || 1);
    el.bell.classList.remove('is-ringing');
    void el.bell.getBoundingClientRect();
    el.bell.classList.add('is-ringing');
    setTimeout(function () { el.bell.classList.remove('is-ringing'); }, 700);
  }
  function syncBell() {
    el.bell.classList.toggle('is-rung', deskOpen);
    el.bell.setAttribute('aria-expanded', deskOpen ? 'true' : 'false');
    el.bell.setAttribute('aria-label', deskOpen ? 'Ring the bell: go home and close the Gorilla Position' : 'Ring the bell: open the Gorilla Position');
    el.ringOpen.hidden = deskOpen;
    el.ringClose.hidden = !deskOpen;
  }
  el.open1.addEventListener('click', function () { if (!deskOpen) { clang(3); openDesk(); } });
  el.bell.addEventListener('click', function () { if (deskOpen) { clang(1); closeDesk(); } else { clang(3); openDesk(); } });
  el.close.addEventListener('click', closeDesk);
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape' || !deskOpen) return;
    var theater = document.querySelector('.wl-modal');
    if (theater && !theater.hidden) return; /* the theater owns Esc first */
    closeDesk();
  });

  /* ---------- sealed result ---------- */
  el.reveal.addEventListener('click', function () {
    var m = MATCHES[cur];
    revealed[m.slug] = true;
    el.spoiler.classList.add('is-open');
    el.reveal.setAttribute('aria-expanded', 'true');
    el.reveal.lastChild.textContent = 'On the record';
  });

  /* ---------- your ballot ---------- */
  var starBtns = [].slice.call(el.stars.querySelectorAll('.mdx-star'));
  function paintStars(n, hot) {
    starBtns.forEach(function (s, i) {
      s.classList.toggle(hot ? 'is-hot' : 'is-set', i < n);
      if (!hot) s.classList.remove('is-hot');
    });
  }
  el.stars.addEventListener('mouseover', function (e) {
    var b = e.target.closest('.mdx-star');
    if (b) paintStars(+b.getAttribute('data-v'), true);
  });
  el.stars.addEventListener('mouseleave', function () {
    starBtns.forEach(function (s) { s.classList.remove('is-hot'); });
    paintStars(ballots[MATCHES[cur].slug] || 0, false);
  });
  starBtns.forEach(function (b) {
    b.addEventListener('click', function () {
      var v = +b.getAttribute('data-v');
      var m = MATCHES[cur];
      ballots[m.slug] = v;
      paintStars(v, false);
      b.classList.remove('is-pop'); void b.offsetHeight; b.classList.add('is-pop');
      el.rateval.textContent = v + '.0';
      el.insiderTxt.innerHTML = '<b>' + starsRow(v) + ' filed for ' + m.short + '.</b> Insider ballots go on the record, count toward the Wrestle Lore rating, and unlock the full vault.';
      el.insider.classList.add('is-on');
    });
  });
  el.insiderNo.addEventListener('click', function () { el.insider.classList.remove('is-on'); });

  /* ---------- boot ---------- */
  render(0, false);
})();

