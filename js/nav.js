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
  function scoreText(t, q) {
    if (t === q) return 100;
    if (t.indexOf(q) === 0) return 80;
    if (t.indexOf(q) > -1) return 50;
    // token start match
    var parts = t.split(/\s+/);
    for (var i = 0; i < parts.length; i++) if (parts[i].indexOf(q) === 0) return 40;
    return -1;
  }
  function score(item, q) {
    var s = scoreText(item.t.toLowerCase(), q);
    item._aka = '';
    // aliases ("a": from each profile's alternateName) rank just under a title hit,
    // so "hhh" surfaces Triple H and "brahma bull" surfaces The Rock
    if (item.a) {
      for (var i = 0; i < item.a.length; i++) {
        var as = scoreText(item.a[i].toLowerCase(), q);
        if (as > -1 && as - 2 > s) { s = as - 2; item._aka = item.a[i]; }
      }
    }
    return s;
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
        '</span><span class="cmdk__title">' + esc(it.t) +
        (it._aka ? ' <span style="opacity:.55;font-size:.85em">&middot; ' + esc(it._aka) + '</span>' : '') + '</span></li>';
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

/* Ring ticker — rotate the live Lore Feed headlines (universal; ticker is stamped into the nav) */
(function(){
  function initRingTicker(){
    var items=[].slice.call(document.querySelectorAll('.rt-item')),
        dots=[].slice.call(document.querySelectorAll('.rt-dot'));
    if(items.length<2) return;
    var k=0;
    setInterval(function(){
      items[k].classList.remove('is-on'); if(dots[k])dots[k].classList.remove('is-on');
      k=(k+1)%items.length;
      items[k].classList.add('is-on'); if(dots[k])dots[k].classList.add('is-on');
    },5000);
  }
  if(document.readyState!=='loading')initRingTicker();else document.addEventListener('DOMContentLoaded',initRingTicker);
})();


/* ===== MOBILE: hamburger drawer + horizontal-scroll indicators ===== */

/* ---- mobile/nav.js ---- */
/* =====================================================================
   MOBILE NAV DRAWER  (append to js/nav.js)
   Toggle · scrim · Escape · focus trap · body scroll lock ·
   accordion expand/collapse · bottom scroll-fade.
   No dependencies. Wrapped in an IIFE and gated on the hamburger existing,
   so it is a no-op on any page/viewport where the burger is not present.
   The in-drawer search button reuses [data-cmdk-open] (handled by the
   command-palette IIFE above), so no search wiring is needed here.
   ===================================================================== */
(function () {
  'use strict';

  var burger = document.querySelector('.mnav-burger');
  var drawer = document.getElementById('mnav-drawer');
  var scrim  = document.querySelector('.mnav-scrim');
  if (!burger || !drawer || !scrim) return;

  var scrollwrap = drawer.querySelector('.mnav-scrollwrap');
  var body       = drawer.querySelector('.mnav-body');
  var isOpen = false;
  var lastFocus = null;

  var reduce = window.matchMedia('(prefers-reduced-motion:reduce)').matches;

  /* ---------- focusable helpers (recomputed per Tab, so collapsed
       accordion links — visibility:hidden — are correctly excluded) ---- */
  var FOCUSABLE = 'a[href],button:not([disabled]),input:not([disabled]),select,textarea,[tabindex]:not([tabindex="-1"])';
  function visible(el) {
    if (getComputedStyle(el).visibility === 'hidden') return false;
    return !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length);
  }
  function focusables() {
    return Array.prototype.filter.call(drawer.querySelectorAll(FOCUSABLE), visible);
  }

  /* ---------- open / close ---------- */
  function open() {
    if (isOpen) return;
    isOpen = true;
    lastFocus = document.activeElement;

    scrim.hidden = false;
    drawer.hidden = false;
    drawer.setAttribute('aria-hidden', 'false');
    // force reflow so the transition runs from the hidden state
    void drawer.offsetWidth;

    scrim.classList.add('is-open');
    drawer.classList.add('is-open');
    burger.setAttribute('aria-expanded', 'true');
    document.body.classList.add('mnav-open');

    updateFade();
    // move focus into the drawer (the close button)
    var close = drawer.querySelector('.mnav-close');
    (close || drawer).focus();
  }

  function finishClose() {
    if (isOpen) return;            // re-opened mid-transition
    drawer.hidden = true;
    scrim.hidden = true;
  }

  function close() {
    if (!isOpen) return;
    isOpen = false;

    scrim.classList.remove('is-open');
    drawer.classList.remove('is-open');
    drawer.setAttribute('aria-hidden', 'true');
    burger.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('mnav-open');

    // hide from layout after the slide/fade finishes
    if (reduce) {
      finishClose();
    } else {
      var done = false;
      var onEnd = function (e) {
        if (e.target !== drawer) return;
        done = true;
        drawer.removeEventListener('transitionend', onEnd);
        finishClose();
      };
      drawer.addEventListener('transitionend', onEnd);
      setTimeout(function () { if (!done) { drawer.removeEventListener('transitionend', onEnd); finishClose(); } }, 400);
    }

    // return focus to the trigger
    if (lastFocus && typeof lastFocus.focus === 'function') lastFocus.focus();
    else burger.focus();
  }

  function toggle() { isOpen ? close() : open(); }

  burger.addEventListener('click', function (e) { e.preventDefault(); toggle(); });
  Array.prototype.forEach.call(drawer.querySelectorAll('[data-mnav-close]'), function (b) {
    b.addEventListener('click', function (e) { e.preventDefault(); close(); });
  });
  scrim.addEventListener('click', close);

  /* ---------- Escape + focus trap ---------- */
  document.addEventListener('keydown', function (e) {
    if (!isOpen) return;
    // let the command palette own Escape while it is open above the drawer
    var pal = document.getElementById('cmdk');
    if (pal && pal.classList.contains('is-open')) return;

    if (e.key === 'Escape') { e.preventDefault(); close(); return; }
    if (e.key !== 'Tab') return;

    var f = focusables();
    if (!f.length) { e.preventDefault(); return; }
    var first = f[0], last = f[f.length - 1], act = document.activeElement;
    // keep focus inside the drawer
    if (!drawer.contains(act)) { e.preventDefault(); first.focus(); return; }
    if (e.shiftKey && act === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && act === last) { e.preventDefault(); first.focus(); }
  });

  /* ---------- accordions ---------- */
  var accs = Array.prototype.slice.call(drawer.querySelectorAll('.mnav-acc'));
  accs.forEach(function (acc) {
    var btn = acc.querySelector('.mnav-acc__btn');
    var panel = acc.querySelector('.mnav-acc__panel');
    if (!btn || !panel) return;

    btn.addEventListener('click', function () {
      var willOpen = !acc.classList.contains('is-open');
      acc.classList.toggle('is-open', willOpen);
      btn.setAttribute('aria-expanded', willOpen ? 'true' : 'false');
      if (willOpen) {
        panel.style.maxHeight = panel.scrollHeight + 'px';
      } else {
        // set an explicit px first (in case it is 'none') so the collapse animates
        panel.style.maxHeight = panel.scrollHeight + 'px';
        void panel.offsetWidth;
        panel.style.maxHeight = '0px';
      }
      // the drawer's scrollable height just changed
      updateFade();
    });

    // once expanded, release the fixed height so nested reflow can't clip
    panel.addEventListener('transitionend', function (e) {
      if (e.propertyName !== 'max-height') return;
      if (acc.classList.contains('is-open')) panel.style.maxHeight = 'none';
      updateFade();
    });
  });

  /* ---------- bottom scroll-fade affordance ---------- */
  function updateFade() {
    if (!scrollwrap || !body) return;
    var atEnd = body.scrollTop + body.clientHeight >= body.scrollHeight - 4;
    scrollwrap.classList.toggle('is-end', atEnd);
  }
  if (body) body.addEventListener('scroll', updateFade, { passive: true });
  window.addEventListener('resize', function () { if (isOpen) updateFade(); });
})();

/* ---- mobile/scroll.js ---- */
/* ==========================================================================
   wrestlelore.com  ·  MOBILE HORIZONTAL-SCROLL INDICATORS
   --------------------------------------------------------------------------
   Append this IIFE to js/nav.js. It enhances the homepage's intentional
   horizontal rails on phones (<=760px):

     · wraps each rail in a relative .hs-wrap (so the hint can be pinned)
     · tags the rail .js-hscroll and drives an edge-fade mask via the
       --hsl / --hsr custom properties (see sections.css)
     · shows a small "Swipe" pill that fades after the first scroll / touch,
       or after a few seconds, so it's obvious content continues off-screen

   Safe by design: no dependencies, gated on element presence, only active
   at <=760px, fully torn down (DOM restored) above 760px so desktop is
   untouched, and reduced-motion aware.
   ========================================================================== */
(function () {
  'use strict';

  if (typeof window === 'undefined' || !window.matchMedia) return;

  var MQ    = window.matchMedia('(max-width:760px)');
  var RM     = window.matchMedia('(prefers-reduced-motion:reduce)');
  var FADE   = '30px';           // must match sections.css --hsr default
  var HINT_TIMEOUT = 4600;       // ms before the swipe pill auto-hides

  /* The intentional horizontal scrollers, by their existing id/class hooks. */
  var SELECTORS = [
    '.thisweek .tw-rail',   // This Week video cards
    '.thisweek .tw-list',   // This Week promotion tabs
    '#wdeal',               // The Wrestlers card deck
    '.hv3 .filterrow',      // The Wrestlers chip/lane rail
    '#tpx .tpx-reel',       // The Moments Reel film strip
    '#clx .clx-rail'        // Five-Star Classics rail
  ];

  function each(list, fn) { Array.prototype.forEach.call(list, fn); }

  function collect() {
    var found = [];
    each(SELECTORS, function (sel) {
      each(document.querySelectorAll(sel), function (el) {
        if (found.indexOf(el) === -1) found.push(el);
      });
    });
    return found;
  }

  /* ---- enable one rail ------------------------------------------------- */
  function enable(el) {
    if (el.__hs) return;

    // wrap so the swipe hint has a stable, non-scrolling anchor
    var wrap = document.createElement('div');
    wrap.className = 'hs-wrap';
    el.parentNode.insertBefore(wrap, el);
    wrap.appendChild(el);
    el.classList.add('js-hscroll');

    // the swipe affordance (no arrows/dashes — a labelled pill + pulsing dots)
    var hint = document.createElement('div');
    hint.className = 'hs-hint';
    hint.setAttribute('aria-hidden', 'true');
    hint.innerHTML = '<span class="hs-hint__dots"><i></i><i></i><i></i></span>Swipe';
    wrap.appendChild(hint);

    var state = { wrap: wrap, hint: hint, timer: 0, dismissed: false, ro: null };
    el.__hs = state;

    function dismissHint() {
      if (state.dismissed) return;
      state.dismissed = true;
      if (state.timer) { clearTimeout(state.timer); state.timer = 0; }
      hint.classList.add('is-gone');
      window.setTimeout(function () {
        if (hint && hint.parentNode) hint.style.display = 'none';
      }, RM.matches ? 0 : 480);
    }

    function update() {
      var max = el.scrollWidth - el.clientWidth;
      var x   = el.scrollLeft;
      if (max <= 2) {                       // nothing to scroll: no fade, no hint
        el.style.setProperty('--hsl', '0px');
        el.style.setProperty('--hsr', '0px');
        if (!state.dismissed) hint.style.display = 'none';
        return;
      }
      if (!state.dismissed) hint.style.display = '';
      el.style.setProperty('--hsl', x > 4 ? FADE : '0px');
      el.style.setProperty('--hsr', x < max - 4 ? FADE : '0px');
    }
    state.update = update;

    state.onScroll = function () {
      if (el.scrollLeft > 6) dismissHint();
      update();
    };
    el.addEventListener('scroll', state.onScroll, { passive: true });
    el.addEventListener('pointerdown', dismissHint, { passive: true });
    el.addEventListener('touchstart', dismissHint, { passive: true });

    // recompute when content fills in late (e.g. the JS-built #wdeal deck)
    if (window.ResizeObserver) {
      state.ro = new ResizeObserver(update);
      state.ro.observe(el);
    }

    state.timer = window.setTimeout(dismissHint, HINT_TIMEOUT);
    update();
  }

  /* ---- disable one rail (restore original DOM) ------------------------- */
  function disable(el) {
    var s = el.__hs;
    if (!s) return;
    el.removeEventListener('scroll', s.onScroll);
    if (s.ro) s.ro.disconnect();
    if (s.timer) clearTimeout(s.timer);
    if (s.hint && s.hint.parentNode) s.hint.parentNode.removeChild(s.hint);
    el.classList.remove('js-hscroll');
    el.style.removeProperty('--hsl');
    el.style.removeProperty('--hsr');
    var w = s.wrap;
    if (w && w.parentNode) {                // unwrap
      w.parentNode.insertBefore(el, w);
      w.parentNode.removeChild(w);
    }
    el.__hs = null;
  }

  /* ---- sync to the current breakpoint ---------------------------------- */
  function sync() {
    var rails = collect();
    if (!rails.length) return;
    if (MQ.matches) each(rails, enable);
    else            each(rails, disable);
  }

  function refresh() {                      // recompute fades for active rails
    each(collect(), function (el) { if (el.__hs) el.__hs.update(); });
  }

  function boot() {
    sync();
    // late layout / font / async content settling
    window.addEventListener('load', refresh);
    window.addEventListener('resize', refresh, { passive: true });
    if (MQ.addEventListener) MQ.addEventListener('change', sync);
    else if (MQ.addListener) MQ.addListener(sync);   // older Safari
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
