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

/* ===================================================================
   NAV7 + HOME V3 (home page only; no-op on every other page)
   Runs only when the page carries the .nav7 header. Handles:
   hover-intent + click tab opening, Esc / outside-click / focus-out
   close, viewport clamping, live reign-day counters from data-start,
   touch tap-to-reveal champs. The belt-rack crest draw-on (Crest
   Craft) is pure CSS, keyed off the .open class set here: each
   crest's stroke-dashoffset animation restarts on every panel open,
   staggered 80ms per strap via the belts' inline --i custom property.
   The search pill uses [data-cmdk-open], handled by the palette above.
   =================================================================== */
(function () {
  'use strict';
  var root = document.querySelector('.nav7');
  if (!root) return;

  var items = Array.prototype.slice.call(root.querySelectorAll('.navitem'));
  var openItem = null, hoverTimer = null, leaveTimer = null;
  var finePointer = window.matchMedia('(hover:hover) and (pointer:fine)').matches;

  function clampPanel(item) {
    var mega = item.querySelector('.mega7');
    if (!mega) return;
    mega.style.left = '0px';
    var r = mega.getBoundingClientRect();
    var pad = 12, dx = 0;
    if (r.right > window.innerWidth - pad) dx = (window.innerWidth - pad) - r.right;
    if (r.left + dx < pad) dx = pad - r.left;
    mega.style.left = dx + 'px';
  }
  function openPanel(item) {
    if (openItem && openItem !== item) closePanel(openItem);
    item.classList.add('open');
    var tab = item.querySelector('.tab');
    if (tab) tab.setAttribute('aria-expanded', 'true');
    openItem = item;
    clampPanel(item);
  }
  function closePanel(item) {
    item.classList.remove('open');
    var tab = item.querySelector('.tab');
    if (tab) tab.setAttribute('aria-expanded', 'false');
    if (openItem === item) openItem = null;
  }
  function closeAll() { items.forEach(closePanel); }

  items.forEach(function (item) {
    var tab = item.querySelector('.tab');
    // hover intent (mouse only): 50ms in, 140ms grace out
    item.addEventListener('pointerenter', function (e) {
      if (e.pointerType !== 'mouse' || !finePointer) return;
      clearTimeout(leaveTimer);
      hoverTimer = setTimeout(function () { openPanel(item); }, 50);
    });
    item.addEventListener('pointerleave', function (e) {
      if (e.pointerType !== 'mouse' || !finePointer) return;
      clearTimeout(hoverTimer);
      leaveTimer = setTimeout(function () { closePanel(item); }, 140);
    });
    // click: first activation opens the panel, second follows the real link
    if (tab) {
      tab.addEventListener('click', function (e) {
        if (!item.classList.contains('open')) {
          e.preventDefault();
          openPanel(item);
        }
      });
    }
  });
  document.addEventListener('click', function (e) {
    if (openItem && !openItem.contains(e.target)) closeAll();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    var pal = document.getElementById('cmdk');
    if (pal && pal.classList.contains('is-open')) return; // palette owns Esc
    if (openItem) {
      var t = openItem.querySelector('.tab');
      closeAll();
      if (t) t.focus();
    }
  });
  // close panels when keyboard focus leaves the bar
  document.addEventListener('focusin', function (e) {
    if (openItem && !openItem.contains(e.target)) closeAll();
  });
  window.addEventListener('resize', function () {
    if (openItem) clampPanel(openItem);
  });

  /* ---- reign-day counters from data-start (UTC date math) ---- */
  function reignDays(iso) {
    return Math.max(1, Math.floor((Date.now() - new Date(iso).getTime()) / 86400000));
  }
  Array.prototype.forEach.call(root.querySelectorAll('.belt .plate[data-start]'), function (p) {
    var days = reignDays(p.getAttribute('data-start'));
    var d = p.querySelector('.pdays');
    if (d) d.textContent = 'DAY ' + days;
    var belt = p.closest ? p.closest('a.belt') : null;
    if (belt) belt.setAttribute('title', 'Day ' + days + ' of reign');
  });
  /* intel rows elsewhere in the shell also tick from data-start */
  Array.prototype.forEach.call(root.querySelectorAll('.ldg-days[data-start]'), function (el) {
    el.textContent = 'DAY ' + reignDays(el.getAttribute('data-start'));
  });

  /* ---- touch: first tap flips a strap to the champion, second follows the link ---- */
  if (window.matchMedia('(hover:none)').matches) {
    var beltEls = Array.prototype.slice.call(root.querySelectorAll('a.belt'));
    beltEls.forEach(function (b) {
      b.addEventListener('click', function (e) {
        if (!b.classList.contains('flipped')) {
          e.preventDefault();
          beltEls.forEach(function (o) { o.classList.remove('flipped'); });
          b.classList.add('flipped');
        }
      });
    });
    document.addEventListener('click', function (e) {
      if (!e.target.closest || !e.target.closest('a.belt')) {
        beltEls.forEach(function (o) { o.classList.remove('flipped'); });
      }
    });
  }
})();
