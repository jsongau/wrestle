/* MAT — command palette (⌘K / Ctrl+K) global search.
   Reads window.MAT_SEARCH_INDEX (js/search-index.js). No deps, no storage. */
(function () {
  var idx = window.MAT_SEARCH_INDEX || [];
  var overlay = document.getElementById('cmdk');
  if (!overlay) return;
  var input = overlay.querySelector('.cmdk__input');
  var list  = overlay.querySelector('.cmdk__results');
  var active = -1, rows = [];

  function open() {
    overlay.classList.add('is-open');
    overlay.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    input.value = '';
    render('');
    setTimeout(function () { input.focus(); }, 20);
  }
  function close() {
    overlay.classList.remove('is-open');
    overlay.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    active = -1;
  }
  function score(item, q) {
    var t = item.t.toLowerCase();
    if (t === q) return 100;
    if (t.indexOf(q) === 0) return 80;
    if (t.indexOf(q) > -1) return 50;
    // token start match
    var parts = t.split(/\s+/);
    for (var i = 0; i < parts.length; i++) if (parts[i].indexOf(q) === 0) return 40;
    return -1;
  }
  function render(q) {
    q = (q || '').trim().toLowerCase();
    var items;
    if (!q) {
      items = idx.slice(0, 8);
    } else {
      items = idx.map(function (it) { return { it: it, s: score(it, q) }; })
                 .filter(function (o) { return o.s >= 0; })
                 .sort(function (a, b) { return b.s - a.s; })
                 .slice(0, 30)
                 .map(function (o) { return o.it; });
    }
    rows = items;
    active = items.length ? 0 : -1;
    if (!items.length) {
      list.innerHTML = '<li class="cmdk__empty">No matches for &ldquo;' + esc(q) + '&rdquo;</li>';
      return;
    }
    list.innerHTML = items.map(function (it, i) {
      return '<li class="cmdk__row' + (i === active ? ' is-active' : '') + '" role="option" data-url="' +
        it.u + '"><span class="cmdk__kind cmdk__kind--' + it.k.toLowerCase() + '">' + it.k +
        '</span><span class="cmdk__title">' + esc(it.t) + '</span></li>';
    }).join('');
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) {
    return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function move(d) {
    if (!rows.length) return;
    active = (active + d + rows.length) % rows.length;
    var els = list.querySelectorAll('.cmdk__row');
    els.forEach(function (el, i) { el.classList.toggle('is-active', i === active); });
    var el = els[active]; if (el) el.scrollIntoView({ block: 'nearest' });
  }
  function go() { if (active > -1 && rows[active]) window.location.href = rows[active].u; }

  input.addEventListener('input', function () { render(input.value); });
  input.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowDown') { e.preventDefault(); move(1); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); move(-1); }
    else if (e.key === 'Enter') { e.preventDefault(); go(); }
    else if (e.key === 'Escape') { close(); }
  });
  list.addEventListener('click', function (e) {
    var row = e.target.closest('.cmdk__row');
    if (row) window.location.href = row.dataset.url;
  });
  overlay.addEventListener('click', function (e) { if (e.target === overlay) close(); });

  document.addEventListener('keydown', function (e) {
    if ((e.metaKey || e.ctrlKey) && (e.key === 'k' || e.key === 'K')) { e.preventDefault(); open(); }
    else if (e.key === '/' && !/input|textarea|select/i.test((e.target.tagName || ''))) {
      e.preventDefault(); open();
    }
  });
  document.querySelectorAll('[data-cmdk-open]').forEach(function (b) {
    b.addEventListener('click', function (e) { e.preventDefault(); open(); });
  });
})();
