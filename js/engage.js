/* Wrestle Lore — engagement layer for wrestler profiles.
   Injects: sticky LEFT rail (scroll-spy section nav + quick actions),
   sticky BOTTOM rail ("Keep going" related wrestlers from this page's own links),
   bottom-right FLOATER ("Discover" — random relevant + random legend + rate).
   Self-gates to profile pages (.athlete-hero). Vanilla, no storage, reduced-motion aware. */
(function () {
  var hero = document.querySelector('.athlete-hero');
  if (!hero) return;
  var main = document.querySelector('main') || document.body;
  var here = location.pathname;
  var name = (document.querySelector('.athlete-hero h1') || {}).textContent || 'this wrestler';

  /* ---- collect this character's related wrestlers from in-body links ---- */
  var related = [];
  var seen = {};
  var norm = function (u) { return u.replace(/index\.html$/, '').replace(/\/$/, ''); };
  main.querySelectorAll('a[href^="/wrestlers/"]').forEach(function (a) {
    var href = a.getAttribute('href');
    if (norm(href) === norm(here) || seen[href] || !/^\/wrestlers\/[a-z0-9-]+\/$/.test(href)) return;
    seen[href] = 1;
    related.push({ t: a.textContent.trim(), u: href });
  });
  var idx = (window.MAT_SEARCH_INDEX || []).filter(function (e) { return e.k === 'Wrestler' && e.u !== here; });

  function mono(t) { var w = t.replace(/[^A-Za-z ]/g, '').split(' ').filter(Boolean); return ((w[0] || t)[0] + (w[1] ? w[1][0] : (w[0] || 'x')[1] || '')).toUpperCase(); }
  function rand(arr) { return arr.length ? arr[Math.floor((Date.now() / 1000 % arr.length))] : null; }

  /* ---- harvest a page-local "Did you know" fact ---- */
  function harvestFact() {
    var facts = [];
    main.querySelectorAll('.stat-card dt').forEach(function (dt) {
      var k = dt.textContent.trim(), v = (dt.nextElementSibling || {}).textContent || '';
      if (/finisher/i.test(k) && v) facts.push(name + "'s finisher: " + v.trim() + '.');
      if (/born/i.test(k) && v) facts.push(name + ' was born ' + v.trim() + '.');
      if (/debut/i.test(k) && v) facts.push(name + ' debuted in ' + v.trim() + '.');
    });
    var tl = main.querySelector('.timeline li');
    if (tl) facts.push(tl.textContent.trim().replace(/\s+/g, ' '));
    return facts.length ? facts[Math.floor(Date.now() / 60000) % facts.length] : null;
  }

  /* ---- LEFT RAIL: scroll-spy section nav + quick actions ---- */
  var heads = Array.prototype.slice.call(main.querySelectorAll('h2')).filter(function (h) { return h.offsetParent !== null; });
  if (heads.length > 2) {
    heads.forEach(function (h, i) { if (!h.id) h.id = 'sec-' + i + '-' + (h.textContent || '').toLowerCase().replace(/[^a-z]+/g, '-').replace(/^-|-$/g, ''); });
    var rail = document.createElement('nav');
    rail.className = 'engage-left'; rail.setAttribute('aria-label', 'On this page');
    rail.innerHTML = '<p class="engage-left__h">On this page</p>' +
      heads.map(function (h) { return '<a class="engage-left__a" href="#' + h.id + '">' + h.textContent + '</a>'; }).join('') +
      '<p class="engage-left__h">Explore</p>' +
      '<a class="engage-left__a engage-left__act" data-random>Random wrestler</a>' +
      (related[0] ? '<a class="engage-left__a engage-left__act" href="' + related[0].u + '">Go to ' + related[0].t + '</a>' : '');
    document.body.appendChild(rail);
    var links = rail.querySelectorAll('a[href^="#"]');
    var byId = {}; links.forEach(function (l) { byId[l.getAttribute('href').slice(1)] = l; });
    if ('IntersectionObserver' in window) {
      var obs = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) { links.forEach(function (l) { l.classList.remove('is-active'); }); if (byId[e.target.id]) byId[e.target.id].classList.add('is-active'); } });
      }, { rootMargin: '-45% 0px -50% 0px' });
      heads.forEach(function (h) { obs.observe(h); });
    }
    /* reveal rail only after scrolling past the hero (research: avoid top clutter) */
    var reveal = function () { rail.classList.toggle('is-in', window.scrollY > (hero.offsetHeight || 300) * 0.6); };
    window.addEventListener('scroll', reveal, { passive: true }); reveal();
  }

  /* ---- BOTTOM RAIL: "Keep going" related wrestlers ---- */
  if (related.length) {
    var pool = related.slice(0, 12);
    var bar = document.createElement('aside');
    bar.className = 'engage-bottom'; bar.setAttribute('aria-label', 'Keep exploring');
    bar.innerHTML = '<div class="engage-bottom__in"><span class="engage-bottom__lbl">Keep going</span><div class="engage-bottom__row">' +
      pool.map(function (r) { return '<a class="engage-chip" href="' + r.u + '"><span class="engage-chip__m">' + mono(r.t) + '</span>' + r.t + '</a>'; }).join('') +
      '</div><button class="engage-bottom__x" aria-label="Dismiss">&#10005;</button></div>';
    document.body.appendChild(bar);
    /* scroll-aware: slide in after 25% depth, not on load (research: earn the interruption) */
    var shown = false;
    var onScroll = function () {
      var depth = window.scrollY / Math.max(1, document.body.scrollHeight - window.innerHeight);
      if (!shown && depth > 0.22) { shown = true; bar.classList.add('is-in'); window.removeEventListener('scroll', onScroll); }
    };
    window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
    bar.querySelector('.engage-bottom__x').addEventListener('click', function () { bar.classList.remove('is-in'); setTimeout(function () { bar.remove(); }, 300); });
  }

  /* ---- FLOATER: Discover ---- */
  var fab = document.createElement('div');
  fab.className = 'engage-fab';
  fab.innerHTML = '<button class="engage-fab__btn" aria-expanded="false" aria-label="Discover more">' +
    '<span class="engage-fab__spark">&#9733;</span> Discover</button>' +
    '<div class="engage-fab__pop" role="menu" hidden></div>';
  document.body.appendChild(fab);
  var btn = fab.querySelector('.engage-fab__btn'), pop = fab.querySelector('.engage-fab__pop');
  function buildPop() {
    var relPick = rand(related), legend = idx.length ? idx[Math.floor(Math.random() * idx.length)] : null;
    var stumble = (Math.random() < 0.5 && related.length) ? related[Math.floor(Math.random() * related.length)] : legend;
    var rows = [];
    var fact = harvestFact();
    if (fact) rows.push('<p class="engage-fab__fact"><span>Did you know</span>' + fact + '</p>');
    if (stumble) rows.push('<a class="engage-fab__row engage-fab__row--hot" href="' + stumble.u + '"><b>Stumble</b><span>Jump to ' + stumble.t + '</span></a>');
    if (relPick) rows.push('<a class="engage-fab__row" href="' + relPick.u + '"><b>Rivals &amp; connections</b><span>' + relPick.t + '</span></a>');
    rows.push('<button class="engage-fab__row" data-cmdk-open><b>Search everything</b><span>Press &#8984;K</span></button>');
    rows.push('<a class="engage-fab__row" href="/hall-of-fame/"><b>Hall of Fame</b><span>The immortals</span></a>');
    pop.innerHTML = rows.join('');
    // rewire cmdk buttons inside pop
    pop.querySelectorAll('[data-cmdk-open]').forEach(function (b) { b.addEventListener('click', function () { var o = document.getElementById('cmdk'); if (o) { o.classList.add('is-open'); var i = o.querySelector('.cmdk__input'); if (i) setTimeout(function(){i.focus();}, 20); } close(); }); });
  }
  function open() { buildPop(); pop.hidden = false; fab.classList.add('is-open'); btn.setAttribute('aria-expanded', 'true'); }
  function close() { pop.hidden = true; fab.classList.remove('is-open'); btn.setAttribute('aria-expanded', 'false'); }
  btn.addEventListener('click', function () { fab.classList.contains('is-open') ? close() : open(); });
  document.addEventListener('click', function (e) { if (!fab.contains(e.target)) close(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });

  /* random-wrestler quick action */
  document.addEventListener('click', function (e) {
    var r = e.target.closest('[data-random]');
    if (r && idx.length) { e.preventDefault(); location.href = idx[Math.floor(Math.random() * idx.length)].u; }
  });
})();
