/* Wrestle Lore — faceted filter bar for card grids. No deps, no storage.
   Markup: a <div class="facetbar" data-facet-target="#grid"> of
   <button class="fbtn" data-facet="promo:wwe"> ... data-facet="all" for reset.
   Cards in the target carry data-promo / data-status / data-gender / data-div.
   Single-select within an axis, AND across axes, live count, hash-reflected. */
(function () {
  document.querySelectorAll('.facetbar').forEach(function (bar) {
    var grid = document.querySelector(bar.getAttribute('data-facet-target'));
    if (!grid) return;
    var cards = Array.prototype.slice.call(grid.querySelectorAll('.card'));
    var countEl = bar.querySelector('[data-facet-count]');
    var state = {}; // axis -> value

    function apply() {
      var shown = 0;
      cards.forEach(function (c) {
        var ok = Object.keys(state).every(function (axis) {
          return state[axis] === 'all' || c.getAttribute('data-' + axis) === state[axis];
        });
        c.style.display = ok ? '' : 'none';
        if (ok) shown++;
      });
      // hide a section header whose following grid has no visible cards
      grid.querySelectorAll('.sec-h').forEach(function (h) {
        var g = h.nextElementSibling;
        while (g && !g.classList.contains('grid-cards')) g = g.nextElementSibling;
        if (g) { var vis = g.querySelectorAll('.card:not([style*="display: none"])').length; h.style.display = vis ? '' : 'none'; }
      });
      if (countEl) countEl.textContent = shown + (shown === 1 ? ' wrestler' : ' wrestlers');
    }
    bar.querySelectorAll('.fbtn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var f = btn.getAttribute('data-facet');
        var group = btn.closest('[data-facet-group]');
        // clear active in this group
        if (group) group.querySelectorAll('.fbtn').forEach(function (b) { b.classList.remove('is-active'); b.setAttribute('aria-pressed', 'false'); });
        btn.classList.add('is-active'); btn.setAttribute('aria-pressed', 'true');
        if (f === 'all') {
          if (group) { var ax = group.getAttribute('data-facet-group'); delete state[ax]; }
          else state = {};
        } else {
          var parts = f.split(':'); state[parts[0]] = parts[1];
        }
        apply();
      });
    });
    apply();
  });
})();
