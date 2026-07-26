/* Wrestle Lore — HOME engagement layer ("home-explore").
   Home-only. Injects: a sticky bottom "Keep exploring" rail of real harvested
   links, a bottom-right "Surprise me" Discover floater, and stamps count-up
   targets for the existing enhance.js observer. Re-presents anchors already on
   the page (nav + main) and window.MAT_SEARCH_INDEX. No dependencies, no storage,
   reduced-motion aware, hover-gated niceties. All injected nodes use the .he- prefix. */
(function () {
  'use strict';

  /* ---- gate: home only ---- */
  var isHome = document.body.hasAttribute('data-home') ||
    (document.querySelector('main#main.hv3') && !document.querySelector('.athlete-hero'));
  if (!isHome) return;

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia && window.matchMedia('(hover:hover) and (pointer:fine)').matches;
  var here = location.pathname;
  var norm = function (u) { return (u || '').replace(/index\.html$/, '').replace(/\/$/, ''); };
  var hereN = norm(here);

  function rand(arr) { return arr.length ? arr[Math.floor(Math.random() * arr.length)] : null; }
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function clean(s) { return (s || '').replace(/\s+/g, ' ').trim(); }
  function cap(s, n) { s = clean(s); return s.length > n ? s.slice(0, n - 1).trim() + '…' : s; }

  /* label from an anchor: prefer a meaningful child, else its text */
  function labelOf(a) {
    var sel = ['.tile__name', '.bnm2', '.nm', '.enm', '.bnm', '.chn'];
    for (var i = 0; i < sel.length; i++) { var el = a.querySelector(sel[i]); if (el && clean(el.textContent)) return cap(el.textContent, 42); }
    return cap(a.textContent, 42);
  }

  /* clean canonical titles keyed by normalized url (from the on-page search index) */
  var urlTitle = {};
  (window.MAT_SEARCH_INDEX || []).forEach(function (e) { if (e && e.u && e.t) urlTitle[norm(e.u)] = clean(e.t); });

  /* ---- harvest real internal links from the whole document (nav + main) ---- */
  var pools = { match: [], champ: [], hub: [] };
  var seen = {};
  function push(kind, a) {
    var href = a.getAttribute('href');
    if (!href || href.charAt(0) !== '/') return;
    var n = norm(href);
    if (n === hereN || n === '') return;
    var key = kind + '|' + n;
    if (seen[key]) return;
    var t = urlTitle[n] ? cap(urlTitle[n], 42) : labelOf(a);
    if (!t) return;
    seen[key] = 1;
    pools[kind].push({ t: t, u: href, kind: kind });
  }
  var HUB_RE = /^\/(rankings|moments|rivalries|factions|tag-teams|hall-of-fame|wrestlers|events|titles|promotions)\/?$/;
  Array.prototype.forEach.call(document.querySelectorAll('a[href^="/"]'), function (a) {
    var href = a.getAttribute('href');
    if (/^\/matches\//.test(href)) { push('match', a); return; }
    if (/^\/titles\/[a-z0-9-]+\//.test(href) || a.classList.contains('mono7c')) { push('champ', a); return; }
    if (HUB_RE.test(href) || /^\/promotions\/(wwe|tna|njpw|wcw|ecw|nxt|aew)\//.test(href)) { push('hub', a); return; }
  });

  /* interleave the three pools into one deduped, shuffled chip list */
  function buildChipSet(cap8) {
    var m = shuffle(pools.match), c = shuffle(pools.champ), h = shuffle(pools.hub);
    var out = [], i = 0, used = {};
    while (out.length < cap8 && (i < m.length || i < c.length || i < h.length)) {
      [m[i], c[i], h[i]].forEach(function (x) {
        if (x && out.length < cap8 && !used[x.kind + '|' + norm(x.u)]) { used[x.kind + '|' + norm(x.u)] = 1; out.push(x); }
      });
      i++;
    }
    return out;
  }

  var KICK = { match: 'Five-star', champ: 'Champion', hub: 'Hub' };

  /* ---- search index for the "Surprise me" instant jump ---- */
  var idx = (window.MAT_SEARCH_INDEX || []).filter(function (e) { return e && e.u && norm(e.u) !== hereN; });
  var lastShown = []; /* in-memory ring buffer, de-prioritise last 3 */
  function surprise() {
    var pick = null, tries = 0;
    if (!idx.length) return null;
    do { pick = idx[Math.floor(Math.random() * idx.length)]; tries++; }
    while (pick && lastShown.indexOf(norm(pick.u)) !== -1 && tries < 12);
    if (pick) { lastShown.push(norm(pick.u)); if (lastShown.length > 3) lastShown.shift(); }
    return pick;
  }

  /* ---- harvest page-local "Did you know" facts, each with a real link ---- */
  function harvestFacts() {
    var facts = [];
    /* champion reign fact from the live belt plate */
    var live = document.querySelector('.belt--live');
    if (live) {
      var name = clean((live.querySelector('.pf--champ') || {}).textContent);
      var title = clean((live.querySelector('.bnm2') || {}).textContent);
      var days = clean((live.querySelector('.pdays') || {}).textContent);
      var href = live.getAttribute('href');
      if (name && title && href) {
        facts.push({ p: 1, t: name + ' holds the ' + title + (days ? ', ' + days.toLowerCase() + ' of the reign' : '') + '.', u: href, lbl: 'See the lineage' });
      }
    }
    /* five-star match fact from the Five-Star Classics tiles */
    Array.prototype.forEach.call(document.querySelectorAll('.grid-spot .tile'), function (t) {
      var nm = clean((t.querySelector('.tile__name') || {}).textContent);
      var ki = clean((t.querySelector('.tile__kicker') || {}).textContent);
      var href = t.getAttribute('href');
      if (nm && href) facts.push({ p: 2, t: nm + ' earned a perfect five stars at ' + (ki || 'a landmark card') + '.', u: href, lbl: 'View the breakdown' });
    });
    /* a featured stat line (e.g. 25-2 at WrestleMania) with its anchor */
    Array.prototype.forEach.call(document.querySelectorAll('.featstat'), function (f) {
      var a = f.closest('a[href^="/"]'); var v = clean(f.textContent);
      if (a && v && /\d/.test(v) && !/^[★☆\s.0-9]+$/.test(v)) {
        var nm = clean((a.querySelector('h3') || {}).textContent) || labelOf(a);
        facts.push({ p: 3, t: (nm ? nm + ': ' : '') + v + '.', u: a.getAttribute('href'), lbl: 'Open the profile' });
      }
    });
    facts.sort(function (a, b) { return a.p - b.p; });
    return facts;
  }
  var FACTS = harvestFacts();
  var factI = 0;

  /* ============================ 1. BOTTOM RAIL ============================ */
  var chipCount = window.matchMedia('(max-width:640px)').matches ? 6 : 8;
  var rail = document.createElement('aside');
  rail.className = 'he-rail';
  rail.setAttribute('aria-label', 'Keep exploring');
  rail.setAttribute('data-state', 'hidden');
  rail.innerHTML =
    '<div class="he-rail__in">' +
      '<span class="he-rail__lbl">Keep exploring</span>' +
      '<div class="he-rail__track" role="list"></div>' +
      '<button class="he-rail__more" type="button">Show another set</button>' +
      '<button class="he-rail__x" type="button" aria-label="Hide">Hide</button>' +
    '</div>';
  var track = rail.querySelector('.he-rail__track');

  function renderChips() {
    var set = buildChipSet(chipCount);
    if (!set.length) return false;
    track.innerHTML = set.map(function (c) {
      return '<a class="he-chip" role="listitem" data-kind="' + c.kind + '" href="' + c.u + '">' +
        '<span class="he-chip__k">' + KICK[c.kind] + '</span>' +
        '<span class="he-chip__n">' + c.t + '</span></a>';
    }).join('');
    return true;
  }

  var railBuilt = false, railDismissed = false, autoSwapped = false, autoTimer = null;
  function initRail() {
    if (railBuilt) return;
    if (!renderChips()) return; /* nothing to show */
    document.body.appendChild(rail);
    railBuilt = true;
    rail.querySelector('.he-rail__more').addEventListener('click', function () { renderChips(); clearTimeout(autoTimer); autoSwapped = true; });
    rail.querySelector('.he-rail__x').addEventListener('click', dismissRail);
  }
  function showRail() {
    if (!railBuilt || railDismissed) return;
    rail.setAttribute('data-state', 'shown');
    document.documentElement.classList.add('has-bottom-rail');
    /* one-shot content swap if untouched ~25s */
    if (!autoSwapped) autoTimer = setTimeout(function () { if (!autoSwapped && !railDismissed) { renderChips(); autoSwapped = true; } }, 25000);
  }
  function hideRail() {
    rail.setAttribute('data-state', 'hidden');
    document.documentElement.classList.remove('has-bottom-rail');
  }
  function dismissRail() {
    railDismissed = true;
    clearTimeout(autoTimer);
    hideRail();
    setTimeout(function () { if (rail.parentNode) rail.parentNode.removeChild(rail); }, 320);
  }

  /* reveal after ~25% scroll depth, once; then detach */
  var revealed = false;
  function onScrollReveal() {
    var depth = window.scrollY / Math.max(1, (document.documentElement.scrollHeight - window.innerHeight));
    if (!revealed && depth > 0.25) {
      revealed = true;
      initRail();
      showRail();
      window.removeEventListener('scroll', onScrollReveal);
    }
  }
  window.addEventListener('scroll', onScrollReveal, { passive: true });
  onScrollReveal();

  /* footer guard: never cover the footer */
  var footer = document.querySelector('footer.site-footer');
  if (footer && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!railBuilt || railDismissed) return;
        if (e.isIntersecting) hideRail();
        else if (revealed) showRail();
      });
    }, { threshold: 0.01 }).observe(footer);
  }

  /* ============================ 2. DISCOVER FLOATER ============================ */
  var fab = document.createElement('div');
  fab.className = 'he-fab';
  fab.innerHTML =
    '<div class="he-fab__core">' +
      '<button class="he-fab__go" type="button" aria-label="Surprise me, jump to a random page">Surprise me</button>' +
      '<button class="he-fab__toggle" type="button" aria-expanded="false" aria-label="Open Discover">' +
        '<span class="he-fab__chev" aria-hidden="true">⌃</span></button>' +
    '</div>' +
    '<div class="he-pop" role="dialog" aria-label="Discover" aria-live="polite" hidden></div>';
  document.body.appendChild(fab);
  var goBtn = fab.querySelector('.he-fab__go');
  var toggle = fab.querySelector('.he-fab__toggle');
  var pop = fab.querySelector('.he-pop');

  /* instant "Surprise me" jump */
  goBtn.addEventListener('click', function () {
    var p = surprise();
    if (p) location.href = p.u;
  });

  /* Stumble: prefer matches, then champions, then hubs */
  function stumblePick() {
    var order = shuffle(pools.match).concat(shuffle(pools.champ), shuffle(pools.hub));
    return order.length ? order[Math.floor(Math.random() * Math.min(order.length, 12))] : null;
  }
  var curStumble = null;

  function buildPop() {
    var rows = [];
    var fact = FACTS.length ? FACTS[factI % FACTS.length] : null;
    factI++;
    if (fact) {
      rows.push('<div class="he-pop__sec he-pop__fact"><span class="he-pop__h">Did you know</span>' +
        '<p class="he-fact__t">' + fact.t + '</p>' +
        '<a class="he-pop__link" href="' + fact.u + '">' + (fact.lbl || 'Open') + '</a></div>');
    }
    curStumble = stumblePick();
    rows.push('<div class="he-pop__sec"><span class="he-pop__h">Stumble the roster</span>' +
      '<p class="he-stumble__pv" data-stumble-pv>' + (curStumble ? KICK[curStumble.kind] + ': ' + curStumble.t : 'Explore the archive') + '</p>' +
      '<div class="he-pop__acts">' +
        '<a class="he-pop__link" data-stumble-go href="' + (curStumble ? curStumble.u : '/wrestlers/') + '">Go</a>' +
        '<button class="he-pop__ghost" type="button" data-stumble-more>Show another</button>' +
      '</div></div>');
    rows.push('<a class="he-pop__row" href="/hall-of-fame/"><span class="he-pop__h">Hall of Fame</span><span class="he-pop__sub">The immortals</span></a>');
    rows.push('<button class="he-pop__row" type="button" data-cmdk-open><span class="he-pop__h">Search everything</span><span class="he-pop__sub">Press Cmd K</span></button>');
    pop.innerHTML = rows.join('');

    var more = pop.querySelector('[data-stumble-more]');
    if (more) more.addEventListener('click', function () {
      curStumble = stumblePick();
      var pv = pop.querySelector('[data-stumble-pv]'); var go = pop.querySelector('[data-stumble-go]');
      if (pv) pv.textContent = curStumble ? KICK[curStumble.kind] + ': ' + curStumble.t : 'Explore the archive';
      if (go) go.setAttribute('href', curStumble ? curStumble.u : '/wrestlers/');
    });
    pop.querySelectorAll('[data-cmdk-open]').forEach(function (b) {
      b.addEventListener('click', function () {
        var o = document.getElementById('cmdk');
        if (o) {
          o.classList.add('is-open');
          o.setAttribute('aria-hidden', 'false');
          var inp = o.querySelector('.cmdk__input');
          if (inp) setTimeout(function () { inp.focus(); }, 20);
        }
        closePop(true);
      });
    });
  }

  var idleTimer = null;
  function openPop() {
    buildPop();
    pop.hidden = false;
    fab.classList.add('is-open');
    toggle.setAttribute('aria-expanded', 'true');
    var first = pop.querySelector('a,button');
    if (first) setTimeout(function () { first.focus({ preventScroll: true }); }, 20);
    clearTimeout(idleTimer);
    idleTimer = setTimeout(function () { closePop(); }, 12000); /* auto-collapse ~12s idle */
  }
  function closePop(toGo) {
    pop.hidden = true;
    fab.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    clearTimeout(idleTimer);
    if (!toGo) toggle.focus({ preventScroll: true });
  }
  toggle.addEventListener('click', function () { fab.classList.contains('is-open') ? closePop() : openPop(); });
  document.addEventListener('click', function (e) { if (!fab.contains(e.target) && fab.classList.contains('is-open')) closePop(true); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && fab.classList.contains('is-open')) closePop(); });
  window.addEventListener('scroll', function () { if (fab.classList.contains('is-open')) closePop(true); }, { passive: true });

  /* one optional idle hint: a single gold-ring flare after ~20s collapsed */
  if (!reduce) {
    setTimeout(function () {
      if (!fab.classList.contains('is-open')) {
        fab.classList.add('he-fab--flare');
        setTimeout(function () { fab.classList.remove('he-fab--flare'); }, 700);
      }
    }, 20000);
  }

  /* Count-up: the hero readout numbers are stamped with data-count directly in
     index.html so the existing enhance.js observer (which collects [data-count] at
     parse time, before this deferred script runs) animates them. Nothing to do here. */
})();
