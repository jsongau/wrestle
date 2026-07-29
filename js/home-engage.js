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
    matches.push({ u: href, title: cap(nm, 44), kick: 'Explore', tag: 'Match', kind: 'match',
      reason: (ev ? ev : 'A classic on the record') + '.', stars: stars });
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

  /* Surprise Me uses a curated fact - no auto-generation */

  /* ---- Explore card: a hand-picked marquee rotation (curated, not auto-harvested) ----
     Every href is a real page; no Benoit/Gargano, no scraped hub titles. One live "Watch"
     entry reuses a real, build-maintained video facade already on the page, so it opens the
     shared theater modal (media.js) and never goes stale. */
  function buildCuratedCards() {
    var picks = [
      { kind: 'profile', u: '/wrestlers/triple-h/',                        kick: 'Superstar',     title: 'Triple H',                reason: 'The Game. The Cerebral Assassin.' },
      { kind: 'match',   u: '/matches/undertaker-vs-hbk-wm25/',            kick: 'Classic match', title: 'Undertaker vs Michaels',  reason: 'WrestleMania XXV. Many call it the greatest ever.' },
      { kind: 'profile', u: '/wrestlers/the-rock/',                        kick: 'Superstar',     title: 'The Rock',                reason: 'The most electrifying man in sports entertainment.' },
      { kind: 'match',   u: '/matches/rock-vs-austin-wm-x-seven-2001/',    kick: 'Classic match', title: 'Rock vs Austin',          reason: 'No Disqualification. WrestleMania X-Seven, 2001.' },
      { kind: 'profile', u: '/wrestlers/the-undertaker/',                  kick: 'Superstar',     title: 'The Undertaker',          reason: 'The Deadman. 21-0 at WrestleMania before the fall.' },
      { kind: 'match',   u: '/matches/bret-hart-vs-austin-wm13/',          kick: 'Classic match', title: 'Bret Hart vs Austin',     reason: 'WrestleMania 13. The double turn.' },
      { kind: 'profile', u: '/wrestlers/stone-cold-steve-austin/',         kick: 'Superstar',     title: 'Stone Cold Steve Austin', reason: 'Austin 3:16. The face of the Attitude Era.' },
      { kind: 'match',   u: '/matches/undertaker-vs-triple-h-wm28-2012/',  kick: 'Classic match', title: 'Undertaker vs Triple H',  reason: 'Hell in a Cell. The End of an Era.' }
    ];
    var yt = document.querySelector('.yt[data-yt-id]');
    if (yt) {
      picks.splice(2, 0, {
        kind: 'watch',
        u: yt.getAttribute('data-yt-page') || '/gallery/',
        kick: 'Watch',
        title: cap(yt.getAttribute('data-yt-title') || 'This week in wrestling', 40),
        reason: 'Play the video right here, no new tab.',
        video: yt.getAttribute('data-yt-id'),
        vtitle: yt.getAttribute('data-yt-title') || 'Wrestle Lore',
        ytEl: yt
      });
    }
    return picks;
  }
  var cardList = buildCuratedCards();
  if (!cardList.length && !idx.length) return;

  /* ============================ SVG icons ============================ */
  var SVG_SEARCH = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="M21 21l-4.3-4.3"></path></svg>';
  var SVG_STAR = '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12 2.6l2.7 5.9 6.4.7-4.8 4.3 1.3 6.3L12 17l-5.6 3.1 1.3-6.3L2.9 9.5l6.4-.7z"></path></svg>';
  var SVG_CHEV = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 15l6-6 6 6"></path></svg>';
  var SPARK_S = '<svg class="f2-spark" viewBox="0 0 24 24" width="14" height="14" fill="currentColor" aria-hidden="true"><path d="M12 2C12.6 8 16 11.4 22 12 16 12.6 12.6 16 12 22 11.4 16 8 12.6 2 12 8 11.4 11.4 8 12 2Z"></path></svg>';

  /* ============================ BOTTOM-LEFT: poster card ============================ */
  var card = document.createElement('div');
  card.className = 'f2-explore';
  card.setAttribute('role', 'region');
  card.setAttribute('aria-label', 'Explore: featured picks');
  card.innerHTML = '<div class="f2-stub" tabindex="0" role="button" aria-label="Explore featured picks"><span class="f2-stub__gleam"></span><span class="f2-stub__v">Explore</span></div><aside class="f2-card"></aside>';
  document.body.appendChild(card);
  var vault = card.querySelector('.f2-card');

  var cardIdx = 0;
  function starStr(n) { var s = ''; for (var i = 0; i < 5; i++) s += i < n ? '★' : '☆'; return s; }
  function renderCard() {
    if (!cardList.length) return;
    var c = cardList[cardIdx % cardList.length];
    var ctaLabel = c.kind === 'watch' ? 'Watch' : 'View';
    vault.innerHTML =
      '<a class="f2-card__link" href="' + esc(c.u) + '">' +
        '<span class="f2-card__kick"><span>' + esc(c.kick) + '</span></span>' +
        '<span class="f2-card__title">' + esc(c.title) + '</span>' +
        '<span class="f2-card__reason">' + esc(c.reason) + '</span>' +
      '</a>' +
      '<div class="f2-card__foot">' +
        '<a class="f2-card__cta" href="' + esc(c.u) + '">' + ctaLabel + '</a>' +
        '<button class="f2-card__next" type="button" aria-label="Show another">Next</button>' +
      '</div>';
    vault.querySelector('.f2-card__next').addEventListener('click', function () { cardIdx++; renderCard(); });
    if (c.kind === 'watch' && c.video) {
      var play = function (e) {
        if (e) e.preventDefault();
        var lnk = c.ytEl && c.ytEl.querySelector('.yt__link');
        if (lnk) { lnk.click(); return; }                       // reuse the page's real facade -> theater modal
        if (window.WL && window.WL.openModal) { window.WL.openModal(c.video, c.vtitle || c.title, { page: c.u }); return; }
        location.href = c.u;                                     // last-ditch fallback
      };
      vault.querySelector('.f2-card__cta').addEventListener('click', play);
      vault.querySelector('.f2-card__link').addEventListener('click', play);
    }
  }
  var cardDismissed = false;
  renderCard();
  var stubEl = card.querySelector('.f2-stub');
  function freshCard() { if (cardList.length) { cardIdx++; renderCard(); } }
  card.addEventListener('mouseenter', freshCard);
  if (stubEl) stubEl.addEventListener('focus', freshCard);

  /* ==================== BOTTOM-RIGHT: Surprise Me (approved v3_2, verbatim) ==================== */
  var SPARK_WG = '<svg class="wglyph wglyph--sale" viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><g class="wg-spin"><path class="wg-spark" d="M12 1.6 C12.7 8.1 15.9 11.3 22.4 12 C15.9 12.7 12.7 15.9 12 22.4 C11.3 15.9 8.1 12.7 1.6 12 C8.1 11.3 11.3 8.1 12 1.6 Z"></path></g><circle class="wg-core" cx="12" cy="12" r="1.9"></circle></svg>';
  var wres = idx.filter(function (e) { return e.u.indexOf('/wrestlers/') === 0; });
  var mats = idx.filter(function (e) { return e.u.indexOf('/matches/') === 0; });
  function doWrestler() { var p = ringPick(wres, surpRing); if (p) location.href = p.u; }
  function doMatch() { var p = ringPick(mats, surpRing); if (p) location.href = p.u; }
  var FACTS = [
    'The Undertaker went 21-0 at WrestleMania before Brock Lesnar ended the streak in 2014.',
    '"Stone Cold" Steve Austin\'s "Austin 3:16" promo at the 1996 King of the Ring lit the fuse on the Attitude Era.',
    'The Montreal Screwjob at Survivor Series 1997 saw Bret Hart lose the WWF title in a finish he never agreed to.',
    'Mick Foley was thrown off the top of Hell in a Cell at the 1998 King of the Ring, then crashed through it.',
    'Hulk Hogan body-slammed the 500-pound Andre the Giant at WrestleMania III in 1987.',
    'WWE recognizes Ric Flair as a 16-time world champion.',
    'The nWo was born in 1996 when Hulk Hogan turned heel to join Scott Hall and Kevin Nash.',
    'Kurt Angle won Olympic freestyle wrestling gold in 1996 with a broken freakin\' neck.',
    'Chris Jericho became the first Undisputed WWF Champion in 2001, unifying the WWF and WCW titles.',
    'The Rock is a third-generation star, grandson of Peter Maivia and son of Rocky Johnson.',
    'The first WrestleMania was held at Madison Square Garden in 1985.',
    'Trish Stratus and Lita made history in 2004 as the first women to main-event Monday Night Raw.',
    'Shawn Michaels and Razor Ramon stole WrestleMania X in 1994 with a ladder match for the ages.',
    'Rey Mysterio has spent most of his Hall of Fame career behind a mask, sacred ground in lucha libre.'
  ];
  var lastFact = -1;
  function pickFact() {
    if (FACTS.length < 2) return FACTS[0];
    var i; do { i = Math.floor(Math.random() * FACTS.length); } while (i === lastFact);
    lastFact = i; return FACTS[i];
  }
  var ctrl = document.createElement('div');
  ctrl.className = 'sm-ctrl';
  ctrl.setAttribute('role', 'region');
  ctrl.setAttribute('aria-label', 'Surprise me');
  ctrl.innerHTML =
    '<div class="sm-panel" role="group" aria-label="Explore more">' +
      '<div class="sm-dyk"><span class="sm-dyk__h">Did you know</span>' +
        '<p class="sm-dyk__t">' + esc(pickFact()) + '</p></div>' +
      '<button class="sm-row sm-row--wrestler" type="button"><span class="sm-row__i"><svg class="ico-mask" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3c-3.7 0-6.2 2.3-6.2 6.4 0 4.3 2.6 8.6 6.2 8.6s6.2-4.3 6.2-8.6C18.2 5.3 15.7 3 12 3Z"></path><path d="M6.4 8.6c1.8-1 9.4-1 11.2 0"></path><circle class="eye" cx="9.2" cy="11" r="1.15" stroke="none"></circle><circle class="eye" cx="14.8" cy="11" r="1.15" stroke="none"></circle><path d="M9.4 15.2c1.4.9 3.8.9 5.2 0"></path></svg></span><span class="sm-row__t">Lore Wrestler</span></button>' +
      '<button class="sm-row sm-row--match" type="button"><span class="sm-row__i"><svg class="ico-ring" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4.5 8.5 7 5.5h10l2.5 3v9.5a1 1 0 0 1-1 1H5.5a1 1 0 0 1-1-1Z"></path><path class="rope" d="M4.5 11h15M4.5 14h15" opacity=".5"></path><circle class="post" cx="4.7" cy="8.5" r="1.1" fill="currentColor" stroke="none"></circle><circle class="post" cx="19.3" cy="8.5" r="1.1" fill="currentColor" stroke="none"></circle></svg></span><span class="sm-row__t">Lore Match</span></button>' +
      '<button class="sm-row sm-row--search" type="button"><span class="sm-row__i"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="M21 21l-4.3-4.3"></path></svg></span><span class="sm-row__t">Search everything</span><span class="sm-row__s">&#8984;K</span></button>' +
    '</div>' +
    '<button class="sm-btn" type="button" aria-label="Surprise me, jump to a random page">' + SPARK_WG + '<span class="sm-btn__lbl">Surprise me</span></button>';
  document.body.appendChild(ctrl);

  function doLegend() { var p = legendPick(); location.href = p ? p.u : hofHref; }
  function doSearch() {
    var o = document.getElementById('cmdk');
    if (o) {
      o.classList.add('is-open'); o.setAttribute('aria-hidden', 'false'); document.body.style.overflow = 'hidden';
      var inp = o.querySelector('.cmdk__input');
      if (inp) { inp.value = ''; try { inp.dispatchEvent(new Event('input')); } catch (e) {} setTimeout(function () { inp.focus(); }, 20); }
    }
  }
  ctrl.querySelector('.sm-btn').addEventListener('click', function () { var p = surprise(); if (p) location.href = p.u; });
  ctrl.querySelector('.sm-row--search').addEventListener('click', doSearch);
  ctrl.querySelector('.sm-row--wrestler').addEventListener('click', doWrestler);
  ctrl.querySelector('.sm-row--match').addEventListener('click', doMatch);
  var dykT = ctrl.querySelector('.sm-dyk__t');
  function freshFact() { if (dykT) dykT.textContent = pickFact(); }
  ctrl.addEventListener('mouseenter', freshFact);
  ctrl.addEventListener('focusin', freshFact);

  /* ============================ VISIBILITY STATE ============================ */
  var revealed = false, atFoot = false;
  function sync() {
    var show = revealed && !atFoot;
    card.classList.toggle('is-live', show);
    ctrl.classList.toggle('is-live', show);
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

