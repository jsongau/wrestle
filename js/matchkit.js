/* matchkit.js — winner spoiler reveal for /matches/ detail pages.
   One page, one secret (who won). Any reveal control unlocks every winner-bearing
   element at once by marking <html> with .wl-revealed. The VS card itself is a
   reveal control (tap anywhere on it that is not a link).
   Progressive enhancement: with no JS the winner is plainly visible (SEO + GEO safe).
   Loading this file marks <html> as .js so the CSS covers engage. */
(function () {
  var d = document, root = d.documentElement;
  if (root) root.classList.add('js');

  function revealAll() {
    if (!root || root.classList.contains('wl-revealed')) return;
    root.classList.add('wl-revealed');
    var controls = d.querySelectorAll('.wl-sp__reveal,.wl-spoiler-block__cover');
    for (var i = 0; i < controls.length; i++) controls[i].setAttribute('aria-expanded', 'true');
    /* move focus to the now-visible result for screen-reader users */
    var v = d.querySelector('.wl-sp__verdict.chip--win') || d.querySelector('.wl-spoiler-block .answer');
    if (v) { v.setAttribute('tabindex', '-1'); try { v.focus({ preventScroll: true }); } catch (e) {} }
  }

  d.addEventListener('click', function (e) {
    var t = e.target;
    if (!t || !t.closest) return;
    if (t.closest('.wl-sp__reveal') || t.closest('.wl-spoiler-block__cover')) { revealAll(); return; }
    /* tap anywhere on the VS card reveals, unless the tap was on a link */
    var card = t.closest('.wl-sp__card');
    if (card && !t.closest('a')) revealAll();
  });
})();
