/* rankings.js — spoiler winner reveal for the Five-Star Club hub.
   Winners live in the DOM (crawlable); this only toggles the CSS blur. */
(function () {
  'use strict';
  function reveal(sp) {
    if (!sp || sp.classList.contains('is-on')) return;
    sp.classList.add('is-on');
    var b = sp.querySelector('.spoiler__btn');
    if (b) { b.setAttribute('aria-expanded', 'true'); b.hidden = true; }
  }
  function conceal(sp) {
    if (!sp) return;
    sp.classList.remove('is-on');
    var b = sp.querySelector('.spoiler__btn');
    if (b) { b.setAttribute('aria-expanded', 'false'); b.hidden = false; }
  }
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('.spoiler__btn');
    if (btn) { e.preventDefault(); reveal(btn.closest('.spoiler')); return; }
    var all = e.target.closest('.reveal-all');
    if (all) {
      var on = all.getAttribute('aria-pressed') === 'true';
      var sps = document.querySelectorAll('.spoiler');
      for (var i = 0; i < sps.length; i++) { on ? conceal(sps[i]) : reveal(sps[i]); }
      all.setAttribute('aria-pressed', on ? 'false' : 'true');
      var t = all.querySelector('.reveal-all__txt');
      if (t) t.textContent = on ? 'Reveal all winners' : 'Hide all winners';
    }
  });

  /* ---- hero spotlight: side rail changes the main stage ---- */
  (function () {
    var hero = document.querySelector('.rank-hero');
    if (!hero) return;
    var slides = [].slice.call(hero.querySelectorAll('.rhero__slide'));
    var rails = [].slice.call(hero.querySelectorAll('.rrail'));
    if (slides.length < 2) return;
    var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion:reduce)').matches;
    var DUR = 6000, timer = null, paused = false, i = 0;
    for (var k = 0; k < slides.length; k++) if (slides[k].classList.contains('is-active')) i = k;

    function show(n) {
      n = (n + slides.length) % slides.length;
      slides[i].classList.remove('is-active');
      if (rails[i]) { rails[i].classList.remove('is-on'); rails[i].setAttribute('aria-current', 'false'); }
      i = n;
      slides[i].classList.add('is-active');
      if (rails[i]) { rails[i].classList.add('is-on'); rails[i].setAttribute('aria-current', 'true'); }
    }
    function play() { if (reduce || paused) return; stop(); timer = setInterval(function () { show(i + 1); }, DUR); }
    function stop() { if (timer) { clearInterval(timer); timer = null; } }

    rails.forEach(function (r, n) { r.addEventListener('click', function () { show(n); play(); }); });

    var pb = hero.querySelector('.rhero__pause');
    if (pb) pb.addEventListener('click', function () {
      paused = !paused;
      if (paused) { stop(); pb.textContent = '►'; pb.setAttribute('aria-label', 'Play the rotation'); }
      else { pb.textContent = '❚❚'; pb.setAttribute('aria-label', 'Pause the rotation'); play(); }
    });
    hero.addEventListener('mouseenter', stop);
    hero.addEventListener('mouseleave', function () { if (!paused) play(); });
    hero.addEventListener('focusin', stop);
    hero.addEventListener('focusout', function () { if (!paused) play(); });

    // hero "Watch" reuses the shared theater modal by triggering the matching grid facade
    hero.addEventListener('click', function (e) {
      var w = e.target.closest('.rhero__watch'); if (!w) return;
      var id = w.getAttribute('data-yt');
      var f = document.querySelector('.yt[data-yt-id="' + id + '"] .yt__link');
      if (f) f.click();
    });

    play();
  })();

  /* ---- match explorer: filter (rating + promotion) + sort + paginate ---- */
  (function () {
    var root = document.querySelector('.rank-explorer');
    if (!root) return;
    var grid = root.querySelector('.rex-grid');
    var countEl = root.querySelector('.rex-count');
    var pager = root.querySelector('.rex-pager');
    var empty = root.querySelector('.rex-empty');
    var cards = [].slice.call(grid.querySelectorAll('.rank-card')).map(function (el, i) {
      return { el: el, i: i,
        rating: parseFloat(el.getAttribute('data-rating')) || 0,
        year: parseInt(el.getAttribute('data-year'), 10) || 0,
        name: (el.getAttribute('data-name') || '').toLowerCase(),
        promo: el.getAttribute('data-promo') || '' };
    });
    var state = { rate: 'ALL', promo: 'ALL', sort: 'rating', page: 1, per: 9 };

    function okRate(c) {
      if (state.rate === 'ALL') return true;
      if (state.rate === '5') return c.rating === 5;
      if (state.rate === '4.5') return c.rating === 4.5;
      if (state.rate === '4') return c.rating <= 4;
      return true;
    }
    function okPromo(c) { return state.promo === 'ALL' || c.promo === state.promo; }
    function sortFn(a, b) {
      switch (state.sort) {
        case 'year-desc': return b.year - a.year || a.i - b.i;
        case 'year-asc': return a.year - b.year || a.i - b.i;
        case 'name': return a.name < b.name ? -1 : a.name > b.name ? 1 : 0;
        default: return b.rating - a.rating || b.year - a.year || a.i - b.i;
      }
    }
    function apply() {
      var filt = cards.filter(function (c) { return okRate(c) && okPromo(c); });
      filt.sort(sortFn);
      cards.forEach(function (c) { c.el.style.display = 'none'; });
      filt.forEach(function (c) { grid.appendChild(c.el); });          // reorder DOM to sorted order
      var pages = Math.max(1, Math.ceil(filt.length / state.per));
      if (state.page > pages) state.page = pages;
      var start = (state.page - 1) * state.per, end = start + state.per;
      filt.slice(start, end).forEach(function (c) { c.el.style.display = ''; });
      if (empty) empty.hidden = filt.length > 0;
      if (countEl) countEl.textContent = filt.length
        ? ('Showing ' + (start + 1) + '–' + Math.min(end, filt.length) + ' of ' + filt.length)
        : '';
      renderPager(pages);
      grid.classList.add('rex-fade');
      requestAnimationFrame(function () { grid.classList.remove('rex-fade'); });
    }
    function renderPager(pages) {
      if (!pager) return;
      if (pages <= 1) { pager.innerHTML = ''; return; }
      var h = '<button class="rex-pg rex-pg--nav" data-pg="prev"' + (state.page === 1 ? ' disabled' : '') + ' aria-label="Previous page">‹</button>';
      for (var p = 1; p <= pages; p++) h += '<button class="rex-pg' + (p === state.page ? ' is-on' : '') + '" data-pg="' + p + '" aria-label="Page ' + p + '">' + p + '</button>';
      h += '<button class="rex-pg rex-pg--nav" data-pg="next"' + (state.page === pages ? ' disabled' : '') + ' aria-label="Next page">›</button>';
      pager.innerHTML = h;
    }

    root.addEventListener('click', function (e) {
      var seg = e.target.closest('.rex-seg button');
      if (seg) {
        var g = seg.parentNode;
        [].forEach.call(g.querySelectorAll('button'), function (b) { b.classList.toggle('is-on', b === seg); });
        if (g.getAttribute('data-ctl') === 'rate') state.rate = seg.getAttribute('data-rate');
        if (g.getAttribute('data-ctl') === 'sort') state.sort = seg.getAttribute('data-sort');
        state.page = 1; apply(); return;
      }
      var chip = e.target.closest('.rfil');
      if (chip) {
        [].forEach.call(root.querySelectorAll('.rfil'), function (b) { b.classList.toggle('is-on', b === chip); });
        state.promo = chip.getAttribute('data-f'); state.page = 1; apply(); return;
      }
      var pg = e.target.closest('.rex-pg');
      if (pg && !pg.disabled) {
        var v = pg.getAttribute('data-pg');
        if (v === 'prev') state.page--; else if (v === 'next') state.page++; else state.page = parseInt(v, 10);
        apply();
        var top = root.getBoundingClientRect().top + window.pageYOffset - 90;
        window.scrollTo({ top: top, behavior: 'smooth' });
        return;
      }
    });

    apply();
  })();
})();
