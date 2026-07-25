/* =========================================================================
   MAT — main.js
   Dependency-free. No localStorage/sessionStorage/cookies (in-memory only).
   Handles: mobile nav, mega-panel toggles, facade video embeds,
            roster/match search+filter, waitlist form (mock).
   ========================================================================= */
(function () {
  'use strict';

  /* ---------- Mobile nav toggle ---------- */
  var toggle = document.querySelector('.nav__toggle');
  var menu = document.querySelector('.nav__menu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.innerHTML = open ? '&#10005;' : '&#9776;';
    });
  }

  /* ---------- Mega-panel: click to open on touch/mobile ---------- */
  document.querySelectorAll('.nav__link[aria-haspopup]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      // Only intercept on narrow screens where hover doesn't apply
      if (window.matchMedia('(max-width:900px)').matches) {
        var panel = link.parentElement.querySelector('.mega');
        if (panel) {
          e.preventDefault();
          var open = panel.classList.toggle('is-open');
          link.setAttribute('aria-expanded', open ? 'true' : 'false');
        }
      }
    });
  });

  /* ---------- Facade click-to-load video (YouTube + Bilibili) ---------- */
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('.facade');
    if (!btn) return;
    var p = btn.dataset.provider, src;
    if (p === 'youtube') {
      src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(btn.dataset.id) +
            '?autoplay=1&rel=0&modestbranding=1';
    } else if (p === 'bilibili') {
      src = 'https://player.bilibili.com/player.html?bvid=' + encodeURIComponent(btn.dataset.bvid) +
            '&autoplay=1&high_quality=1&danmaku=0';
    } else { return; }
    var iframe = document.createElement('iframe');
    iframe.src = src;
    iframe.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen';
    iframe.setAttribute('allowfullscreen', '');
    iframe.setAttribute('title', btn.getAttribute('aria-label') || 'Embedded video');
    iframe.loading = 'lazy';
    iframe.referrerPolicy = 'strict-origin-when-cross-origin';
    btn.replaceWith(iframe);
  });

  /* ---------- Live search / filter for index grids & tables ----------
     Wire up any input[data-filter] to filter elements marked [data-search]
     within the container named by data-filter-target. Filters by data-name
     and data-tags text. Also supports promotion filter buttons [data-promo].  */
  function normalize(s) { return (s || '').toLowerCase(); }

  document.querySelectorAll('[data-filter]').forEach(function (input) {
    var targetSel = input.getAttribute('data-filter-target');
    var container = targetSel ? document.querySelector(targetSel) : document;
    if (!container) return;
    var items = Array.prototype.slice.call(container.querySelectorAll('[data-search]'));
    var counter = document.querySelector(input.getAttribute('data-filter-count') || '');

    function apply() {
      var q = normalize(input.value);
      var promo = container.getAttribute('data-active-promo') || 'all';
      var shown = 0;
      items.forEach(function (el) {
        var hay = normalize(el.getAttribute('data-name') + ' ' + el.getAttribute('data-tags'));
        var elPromo = el.getAttribute('data-promo') || '';
        var matchQ = !q || hay.indexOf(q) !== -1;
        var matchP = promo === 'all' || elPromo.split(' ').indexOf(promo) !== -1;
        var show = matchQ && matchP;
        el.classList.toggle('hide', !show);
        if (show) shown++;
      });
      if (counter) counter.textContent = shown;
    }
    input.addEventListener('input', apply);

    // promotion filter buttons that target this container
    container.querySelectorAll('[data-promo]').forEach(function (b) {
      b.addEventListener('click', function () {
        container.setAttribute('data-active-promo', b.getAttribute('data-promo'));
        container.querySelectorAll('[data-promo]').forEach(function (x) { x.classList.remove('is-active'); });
        b.classList.add('is-active');
        apply();
      });
    });
    input._apply = apply;
  });

  // Standalone promotion filters (no search box)
  document.querySelectorAll('[data-promo-standalone]').forEach(function (container) {
    var items = Array.prototype.slice.call(container.querySelectorAll('[data-search]'));
    container.querySelectorAll('[data-promo]').forEach(function (b) {
      b.addEventListener('click', function () {
        var promo = b.getAttribute('data-promo');
        container.querySelectorAll('[data-promo]').forEach(function (x) { x.classList.remove('is-active'); });
        b.classList.add('is-active');
        items.forEach(function (el) {
          var elPromo = el.getAttribute('data-promo') || '';
          el.classList.toggle('hide', !(promo === 'all' || elPromo.split(' ').indexOf(promo) !== -1));
        });
      });
    });
  });

  /* ---------- Waitlist / membership form (mock, in-memory) ----------
     Demonstrates the top-of-funnel capture. No storage; simulates success
     and reveals the confirmation + a shareable next step. In production this
     POSTs to a CRM/ESP (Klaviyo/Braze/Iterable) and fires an analytics event. */
  document.querySelectorAll('form[data-waitlist]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = form.querySelector('input[type="email"]');
      if (email && !email.checkValidity()) { email.reportValidity(); return; }
      var success = form.parentElement.querySelector('.form-success');
      // Simulated funnel event (would be a real analytics/CRM call in prod)
      if (window.console) {
        console.log('[MAT funnel] waitlist_signup', {
          email: email ? email.value : '',
          source: form.getAttribute('data-source') || 'unknown',
          ts: new Date().toISOString()
        });
      }
      form.classList.add('hide');
      if (success) success.classList.add('is-visible');
    });
  });

  /* ---------- Current year in footers ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
