/* Wrestle Lore — HOME engagement layer, "Match Card & Control" (F2).
   Home-only (body[data-home]). A BALANCED PAIR of corner floaters that replace
   the old single full-width bottom rail:
     - BOTTOM-LEFT  : a compact dismissible "poster" discovery card (duotone
                      monogram, kicker, real entity title, star rating for a
                      match, one-line reason, VIEW, Next to cycle, dismiss X;
                      collapses to a small reopen tab).
     - BOTTOM-RIGHT : a round broadcast control cluster (a primary gold
                      "Surprise Me" disc + two satellite icon buttons: Search
                      opens the existing #cmdk palette, and Random legend; an
                      expand panel adds Did-you-know + Hall of Fame; dismiss to
                      a small recall icon).
   Every destination is a REAL harvested <a> href or a MAT_SEARCH_INDEX url.
   Vanilla, no storage, reduced-motion aware, z-index below #cmdk and the sticky
   header, never covers footer.site-footer. All nodes use the .f2- prefix and are
   styled by the external /css/site.css HOME ENGAGE LAYER block. */
(function () {
  'use strict';

  /* ---- gate: home only ---- */
  var isHome = document.body.hasAttribute('data-home') ||
    (document.querySelector('main#main.hv3') && !document.querySelector('.athlete-hero'));
  if (!isHome) return;

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var here = location.pathname;
  var norm = function (u) { return (u || '').replace(/index\.html$/, '').replace(/\/$/, ''); };
  var hereN = norm(here);
  var qa = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var txt = function (el) { return el ? el.textContent : ''; };
  function clean(s) { return (s || '').replace(/\s+/g, ' ').trim(); }
  function cap(s, n) { s = clean(s); return s.length > n ? s.slice(0, n - 1).trim() + '…' : s; }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function mono(s) { s = clean(s).replace(/^the\s+/i, ''); var m = s.match(/[A-Za-z0-9]/); return m ? m[0].toUpperCase() : '✦'; }

  function labelOf(a) {
    var sel = ['.tile__name', '.bnm2', '.nm', '.enm', '.bnm', '.chn'];
    for (var i = 0; i < sel.length; i++) { var el = a.querySelector(sel[i]); if (el && clean(el.textContent)) return cap(el.textContent, 44); }
    return cap(a.textContent, 44);
  }

  /* clean canonical titles keyed by normalized url (on-page search index) */
  var urlTitle = {};
  (window.MAT_SEARCH_INDEX || []).forEach(function (e) { if (e && e.u && e.t) urlTitle[norm(e.u)] = clean(e.t); });

  /* ============================ HARVEST (real links only) ============================ */
  var matches = [], champs = [], hubs = [], legends = [], seen = {};

  /* five-star match posters */
  qa('.grid-spot a.tile[href^="/matches/"]').forEach(function (a) {
    var href = a.getAttribute('href'), n = norm(href);
    if (!href || n === hereN || seen['m|' + n]) return; seen['m|' + n] = 1;
    var nm = clean(txt(a.querySelector('.tile__name'))) || urlTitle[n] || labelOf(a);
    var ev = clean(txt(a.querySelector('.tile__kicker')));
    var rt = clean(txt(a.querySelector('.tile__rating')));
    var stars = rt ? Math.max(0, Math.min(5, Math.round(parseFloat(rt) || 0))) : 5;
    matches.push({ u: href, title: cap(nm, 44), kick: 'Five-star match', tag: 'Match', kind: 'match',
      reason: (rt ? 'Rated ' + rt + ' stars' : 'A five-star classic') + (ev ? ' at ' + ev : '') + '.', stars: stars });
  });

  /* current champions from the live belt rack */
  qa('a.belt[href^="/titles/"]').forEach(function (a) {
    var href = a.getAttribute('href'), n = norm(href);
    if (!href || n === hereN || seen['c|' + n]) return; seen['c|' + n] = 1;
    var title = clean(txt(a.querySelector('.bnm2'))) || urlTitle[n] || labelOf(a);
    var champ = clean(txt(a.querySelector('.pf--champ')));
    var days = clean(txt(a.querySelector('.pdays')));
    champs.push({ u: href, title: cap(title, 44), kick: 'Current champion', tag: 'Champion', kind: 'champ',
      reason: (champ ? 'Held by ' + champ : 'On the record') + (days ? ', ' + days.toLowerCase() + ' of the reign' : '') + '.', stars: 0 });
  });

  /* hubs from real nav / page links */
  var HUB_RE = /^\/(rankings|moments|rivalries|factions|tag-teams|hall-of-fame|wrestlers|events|titles|promotions)\/?$/;
  var HUBW = { rankings: 'The current pecking order.', moments: 'Flashbulb moments on the record.', rivalries: 'Feuds that defined eras.', factions: 'Stables and their power plays.', 'tag-teams': 'The best of the tandems.', 'hall-of-fame': 'The immortals, enshrined.', wrestlers: 'Every profile on the record.', events: 'Cards worth the rewatch.', titles: 'Every belt and its lineage.', promotions: 'The companies behind it all.' };
  qa('a[href^="/"]').forEach(function (a) {
    var href = a.getAttribute('href'), n = norm(href);
    if (!href || n === hereN || !HUB_RE.test(href) || seen['h|' + n]) return; seen['h|' + n] = 1;
    var seg = (href.replace(/^\//, '').split('/')[0]) || '';
    hubs.push({ u: href, title: cap(urlTitle[n] || labelOf(a), 44), kick: 'Explore hub', tag: 'Hub', kind: 'hub',
      reason: HUBW[seg] || 'Browse the full section.', stars: 0 });
  });

  /* legends pool: real gold/HOF anchors on the page + index Hall of Fame kind */
  qa('a.tile--gold[href^="/"]').forEach(function (a) {
    var href = a.getAttribute('href'), n = norm(href);
    if (!href || n === hereN || seen['l|' + n]) return; seen['l|' + n] = 1;
    legends.push({ u: href, t: urlTitle[n] || labelOf(a) });
  });
  (window.MAT_SEARCH_INDEX || []).forEach(function (e) {
    if (!e || !e.u || e.k !== 'Hall of Fame') return; var n = norm(e.u);
    if (n === hereN || seen['l|' + n]) return; seen['l|' + n] = 1;
    legends.push({ u: e.u, t: clean(e.t) });
  });
  var hofHref = (document.querySelector('a[href="/hall-of-fame/"]') || {}).getAttribute
    ? document.querySelector('a[href="/hall-of-fame/"]').getAttribute('href') : '/hall-of-fame/';

  /* interleave the three card pools so consecutive Next hits vary the kind */
  function interleave() {
    var m = shuffle(matches), c = shuffle(champs), h = shuffle(hubs), out = [], i = 0;
    while (i < m.length || i < c.length || i < h.length) {
      if (m[i]) out.push(m[i]); if (c[i]) out.push(c[i]); if (h[i]) out.push(h[i]); i++;
    }
    return out;
  }

  /* ---- surprise / legend pickers with a small no-repeat ring buffer ---- */
  var idx = (window.MAT_SEARCH_INDEX || []).filter(function (e) { return e && e.u && norm(e.u) !== hereN; });
  function ringPick(arr, ring) {
    if (!arr.length) return null;
    var pick = null, tries = 0;
    do { pick = arr[Math.floor(Math.random() * arr.length)]; tries++; }
    while (pick && ring.indexOf(norm(pick.u)) !== -1 && tries < 12);
    if (pick) { ring.push(norm(pick.u)); if (ring.length > 3) ring.shift(); }
    return pick;
  }
  var surpRing = [], legRing = [];
  function surprise() { return ringPick(idx, surpRing); }
  function legendPick() { return legends.length ? ringPick(legends, legRing) : null; }

  /* ---- did-you-know facts, each with a real link ---- */
  function harvestFacts() {
    var facts = [];
    var live = document.querySelector('.belt--live');
    if (live) {
      var name = clean(txt(live.querySelector('.pf--champ')));
      var title = clean(txt(live.querySelector('.bnm2')));
      var days = clean(txt(live.querySelector('.pdays')));
      var href = live.getAttribute('href');
      if (name && title && href) facts.push({ p: 1, t: name + ' holds the ' + title + (days ? ', ' + days.toLowerCase() + ' of the reign' : '') + '.', u: href, lbl: 'See the lineage' });
    }
    qa('.grid-spot a.tile[href^="/matches/"]').forEach(function (t) {
      var nm = clean(txt(t.querySelector('.tile__name')));
      var ki = clean(txt(t.querySelector('.tile__kicker')));
      var href = t.getAttribute('href');
      if (nm && href) facts.push({ p: 2, t: nm + ' earned a perfect five stars at ' + (ki || 'a landmark card') + '.', u: href, lbl: 'View the breakdown' });
    });
    qa('.featstat').forEach(function (f) {
      var a = f.closest('a[href^="/"]'), v = clean(f.textContent);
      if (a && v && /\d/.test(v) && !/^[★☆\s.0-9]+$/.test(v)) {
        var nm = clean(txt(a.querySelector('h3'))) || labelOf(a);
        facts.push({ p: 3, t: (nm ? nm + ': ' : '') + v + '.', u: a.getAttribute('href'), lbl: 'Open the profile' });
      }
    });
    facts.sort(function (a, b) { return a.p - b.p; });
    return facts;
  }
  var FACTS = harvestFacts(), factI = 0;

  /* nothing to surface at all -> bail (keep self-contained + safe) */
  var cardList = interleave();
  if (!cardList.length && !idx.length) return;

  /* ============================ SVG icons ============================ */
  var SVG_SEARCH = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="M21 21l-4.3-4.3"></path></svg>';
  var SVG_STAR = '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12 2.6l2.7 5.9 6.4.7-4.8 4.3 1.3 6.3L12 17l-5.6 3.1 1.3-6.3L2.9 9.5l6.4-.7z"></path></svg>';
  var SVG_CHEV = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 15l6-6 6 6"></path></svg>';
  var SPARK_S = '<svg class="f2-spark" viewBox="0 0 24 24" width="14" height="14" fill="currentColor" aria-hidden="true"><path d="M12 2C12.6 8 16 11.4 22 12 16 12.6 12.6 16 12 22 11.4 16 8 12.6 2 12 8 11.4 11.4 8 12 2Z"></path></svg>';

  /* ============================ BOTTOM-LEFT: poster card ============================ */
  var card = document.createElement('aside');
  card.className = 'f2-card';
  card.setAttribute('role', 'region');
  card.setAttribute('aria-label', 'Keep exploring: featured destination');
  document.body.appendChild(card);

  var tab = document.createElement('button');
  tab.type = 'button';
  tab.className = 'f2-tab';
  tab.setAttribute('aria-label', 'Reopen the explore card');
  tab.hidden = true;
  tab.innerHTML = '<span class="f2-tab__i" aria-hidden="true">✦</span><span>Explore</span>';
  document.body.appendChild(tab);

  var cardIdx = 0;
  function starStr(n) { var s = ''; for (var i = 0; i < 5; i++) s += i < n ? '★' : '☆'; return s; }
  function renderCard() {
    if (!cardList.length) return;
    var c = cardList[cardIdx % cardList.length];
    card.innerHTML =
      '<button class="f2-card__x" type="button" aria-label="Dismiss the explore card">×</button>' +
      '<a class="f2-card__link" href="' + esc(c.u) + '">' +
        '<span class="f2-card__kick">' + SPARK_S + '<span>' + esc(c.kick) + '</span></span>' +
        '<span class="f2-card__title">' + esc(c.title) + '</span>' +
        (c.kind === 'match' ? '<span class="f2-card__stars" aria-hidden="true">' + starStr(c.stars) + '</span>' : '') +
        '<span class="f2-card__reason">' + esc(c.reason) + '</span>' +
      '</a>' +
      '<div class="f2-card__foot">' +
        '<a class="f2-card__cta" href="' + esc(c.u) + '">View</a>' +
        '<button class="f2-card__next" type="button" aria-label="Show another destination">Next</button>' +
      '</div>';
    card.querySelector('.f2-card__x').addEventListener('click', dismissCard);
    card.querySelector('.f2-card__next').addEventListener('click', function () { cardIdx++; renderCard(); });
  }
  var cardDismissed = false;
  function dismissCard() { cardDismissed = true; sync(); tab.focus({ preventScroll: true }); }
  tab.addEventListener('click', function () { cardDismissed = false; renderCard(); sync(); var l = card.querySelector('.f2-card__link'); if (l) l.focus({ preventScroll: true }); });
  renderCard();

  /* ============================ BOTTOM-RIGHT: control cluster ============================ */
  var ctrl = document.createElement('div');
  ctrl.className = 'f2-ctrl';
  ctrl.setAttribute('data-open', 'false');
  ctrl.setAttribute('role', 'region');
  ctrl.setAttribute('aria-label', 'Explore controls');
  ctrl.innerHTML =
    '<button class="f2-ctrl__x" type="button" aria-label="Hide the explore controls">×</button>' +
    '<div class="f2-ctrl__panel" role="group" aria-label="Discover more" hidden>' +
      '<div class="f2-dyk"><span class="f2-dyk__h">Did you know</span>' +
        '<p class="f2-dyk__t"></p>' +
        '<a class="f2-dyk__link" href="#"></a></div>' +
      '<button class="f2-prow f2-prow--search" type="button" aria-label="Search everything, opens the command palette"><span class="f2-prow__h">Search everything</span><span class="f2-prow__s">Press Cmd K</span></button>' +
      '<button class="f2-prow f2-prow--legend" type="button" aria-label="Jump to a random legend"><span class="f2-prow__h">Random legend</span><span class="f2-prow__s">Roll the dice</span></button>' +
      '<a class="f2-ctrl__hof" href="' + esc(hofHref) + '"><span class="f2-ctrl__hofh">Hall of Fame</span><span class="f2-ctrl__hofs">The immortals</span></a>' +
    '</div>' +
    '<div class="f2-ctrl__cluster">' +
      '<button class="f2-sat f2-sat--search" type="button" aria-label="Search everything, opens the command palette">' + SVG_SEARCH + '</button>' +
      '<button class="f2-sat f2-sat--legend" type="button" aria-label="Jump to a random legend">' + SVG_STAR + '</button>' +
      '<button class="f2-ctrl__more" type="button" aria-expanded="false" aria-label="Expand explore controls">' + SVG_CHEV + '</button>' +
      '<button class="f2-disc" type="button" aria-label="Surprise me, jump to a random page">' + SPARK_S + '<span class="f2-disc__lbl">Surprise me</span></button>' +
    '</div>';
  document.body.appendChild(ctrl);

  var recall = document.createElement('button');
  recall.type = 'button';
  recall.className = 'f2-recall';
  recall.setAttribute('aria-label', 'Show the explore controls');
  recall.hidden = true;
  recall.innerHTML = '<span aria-hidden="true">✦</span>';
  document.body.appendChild(recall);

  var disc = ctrl.querySelector('.f2-disc');
  var satSearch = ctrl.querySelector('.f2-sat--search');
  var satLegend = ctrl.querySelector('.f2-sat--legend');
  var more = ctrl.querySelector('.f2-ctrl__more');
  var panel = ctrl.querySelector('.f2-ctrl__panel');
  var dykT = ctrl.querySelector('.f2-dyk__t');
  var dykLink = ctrl.querySelector('.f2-dyk__link');
  var dyk = ctrl.querySelector('.f2-dyk');

  function fillFact() {
    if (!FACTS.length) { if (dyk) dyk.style.display = 'none'; return; }
    var f = FACTS[factI % FACTS.length]; factI++;
    dykT.textContent = f.t;
    dykLink.textContent = f.lbl || 'Open';
    dykLink.setAttribute('href', f.u);
  }

  var prowSearch = ctrl.querySelector('.f2-prow--search');
  var prowLegend = ctrl.querySelector('.f2-prow--legend');

  var ctrlOpen = false;
  function openCtrl() {
    if (ctrlOpen) return; ctrlOpen = true;
    fillFact();
    ctrl.setAttribute('data-open', 'true');
    more.setAttribute('aria-expanded', 'true');
    panel.hidden = false;
    document.documentElement.classList.add('f2-ctrl-open');
  }
  function closeCtrl(toFocus) {
    if (!ctrlOpen) return; ctrlOpen = false;
    ctrl.setAttribute('data-open', 'false');
    more.setAttribute('aria-expanded', 'false');
    panel.hidden = true;
    document.documentElement.classList.remove('f2-ctrl-open');
    if (toFocus) more.focus({ preventScroll: true });
  }
  more.addEventListener('click', function () { ctrlOpen ? closeCtrl(true) : openCtrl(); });

  /* desktop hover-reveal nicety (fine pointer only) */
  var fine = window.matchMedia && window.matchMedia('(hover:hover) and (pointer:fine)').matches;
  if (fine) {
    var leaveT = null;
    ctrl.addEventListener('mouseenter', function () { clearTimeout(leaveT); openCtrl(); });
    ctrl.addEventListener('mouseleave', function () { clearTimeout(leaveT); leaveT = setTimeout(function () { if (!ctrl.contains(document.activeElement)) closeCtrl(false); }, 320); });
  }

  function doLegend() { var p = legendPick(); location.href = p ? p.u : hofHref; }
  function doSearch() {
    var o = document.getElementById('cmdk');
    if (o) {
      o.classList.add('is-open');
      o.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      var inp = o.querySelector('.cmdk__input');
      if (inp) { inp.value = ''; try { inp.dispatchEvent(new Event('input')); } catch (e) {} setTimeout(function () { inp.focus(); }, 20); }
    }
    closeCtrl(false);
  }
  disc.addEventListener('click', function () { var p = surprise(); if (p) location.href = p.u; });
  satLegend.addEventListener('click', doLegend);
  satSearch.addEventListener('click', doSearch);
  if (prowLegend) prowLegend.addEventListener('click', doLegend);
  if (prowSearch) prowSearch.addEventListener('click', doSearch);

  var ctrlDismissed = false;
  ctrl.querySelector('.f2-ctrl__x').addEventListener('click', function () { ctrlDismissed = true; closeCtrl(false); sync(); recall.focus({ preventScroll: true }); });
  recall.addEventListener('click', function () { ctrlDismissed = false; sync(); disc.focus({ preventScroll: true }); });

  /* Esc closes the expanded cluster */
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && ctrlOpen) closeCtrl(true); });
  /* outside click / scroll collapses the expanded cluster */
  document.addEventListener('click', function (e) { if (ctrlOpen && !ctrl.contains(e.target)) closeCtrl(false); });
  window.addEventListener('scroll', function () { if (ctrlOpen) closeCtrl(false); }, { passive: true });

  /* ============================ VISIBILITY STATE ============================ */
  var revealed = false, atFoot = false;
  function sync() {
    var show = revealed && !atFoot;
    card.classList.toggle('is-live', show && !cardDismissed);
    tab.hidden = !(show && cardDismissed);
    ctrl.classList.toggle('is-live', show && !ctrlDismissed);
    recall.hidden = !(show && ctrlDismissed);
    if (!show || ctrlDismissed) closeCtrl(false);
  }

  /* reveal after ~25% scroll depth (once) */
  function onScrollReveal() {
    var max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    if (!revealed && (window.scrollY / max) > 0.25) {
      revealed = true; sync();
      window.removeEventListener('scroll', onScrollReveal);
    }
  }
  window.addEventListener('scroll', onScrollReveal, { passive: true });
  onScrollReveal();

  /* footer guard: never cover footer.site-footer */
  var footer = document.querySelector('footer.site-footer');
  if (footer && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (es) {
      es.forEach(function (e) { atFoot = e.isIntersecting; sync(); });
    }, { threshold: 0.01 }).observe(footer);
  }
})();

