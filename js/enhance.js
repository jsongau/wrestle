/* =========================================================================
   MAT — enhance.js (Broadcast Bold motion layer)
   Vanilla, no deps, no storage. All effects bail out under reduced motion.
   Scroll-reveal · count-up · hero parallax · card spotlight · sticky header
   ========================================================================= */
(function () {
  'use strict';
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var finePointer = window.matchMedia && window.matchMedia('(hover:hover) and (pointer:fine)').matches;

  /* ---- Scroll reveal + count-up (one IntersectionObserver) ---- */
  var revealEls = [].slice.call(document.querySelectorAll('[data-reveal]'));
  var countEls = [].slice.call(document.querySelectorAll('[data-count]'));

  function runCount(el) {
    var target = parseFloat(el.getAttribute('data-count')) || 0;
    var suffix = el.getAttribute('data-suffix') || '';
    if (reduce) { el.textContent = target + suffix; return; }
    var start = null, dur = 1400;
    function step(ts) {
      if (start === null) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased) + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('is-in');
        if (e.target.hasAttribute('data-count')) runCount(e.target);
        io.unobserve(e.target);
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -8% 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
    countEls.forEach(function (el) { if (!el.hasAttribute('data-reveal')) io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-in'); });
    countEls.forEach(function (el) { el.textContent = el.getAttribute('data-count') + (el.getAttribute('data-suffix') || ''); });
  }

  /* ---- Hero pointer parallax ---- */
  var hero = document.querySelector('.hero-bb');
  if (hero && !reduce && finePointer) {
    var hraf = 0, htx = 0, hty = 0;
    hero.addEventListener('pointermove', function (e) {
      var r = hero.getBoundingClientRect();
      htx = (e.clientX - r.left) / r.width - 0.5;
      hty = (e.clientY - r.top) / r.height - 0.5;
      if (!hraf) hraf = requestAnimationFrame(applyHero);
    });
    hero.addEventListener('pointerleave', function () { htx = hty = 0; if (!hraf) hraf = requestAnimationFrame(applyHero); });
    function applyHero() { hraf = 0; hero.style.setProperty('--px', (htx * 18).toFixed(2) + 'px'); hero.style.setProperty('--py', (hty * 18).toFixed(2) + 'px'); }
  }

  /* ---- Card spotlight (delegated per grid) ---- */
  if (!reduce && finePointer) {
    [].slice.call(document.querySelectorAll('.grid-spot')).forEach(function (grid) {
      grid.addEventListener('pointermove', function (e) {
        var card = e.target.closest('.tile'); if (!card) return;
        var r = card.getBoundingClientRect();
        card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        card.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    });
  }

  /* ---- Sticky header shadow ---- */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () { header.classList.toggle('is-stuck', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }
})();
