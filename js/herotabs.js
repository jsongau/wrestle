/* herotabs.js - tabbed hero roster card: FIGHT METRICS / LIVE FEED.
   Loaded by every dossier page; exits instantly when the page has no
   .portrait[data-fm-tabs] figure. No storage, no globals.

   FEED loader contract:
   - on first reveal of the FEED panel (or on load when it is the default tab),
     inject platform.twitter.com/widgets.js once and mount a twitter-timeline
     anchor in .fm-feed-live;
   - the curated .fm-feed-fallback ships VISIBLE in markup (no-JS safe) and is
     hidden only while a live attempt is actually pending;
   - hard fallback: navigator.onLine === false or script onerror -> immediately;
     otherwise if no iframe has rendered inside the mount within 4s -> fallback.
   - .fm-feed-body carries a fixed min-height so the swap cannot move layout.

   METRICS ring: only wired here for figures carrying data-fm-generated.
   cm-punk's hand page wires its own ring in its inline tail script; wiring it
   twice would double-toggle the veil, so that page ships without the flag. */
(function () {
  'use strict';
  var fig = document.querySelector('.portrait[data-fm-tabs]');
  if (!fig) return;

  var tabs = [].slice.call(fig.querySelectorAll('.fm-tab[role="tab"]'));
  if (!tabs.length) return;
  var panels = tabs.map(function (t) {
    return document.getElementById(t.getAttribute('aria-controls'));
  });

  /* ---------------- tab switching (click + arrow keys) ---------------- */
  function select(i, focus) {
    tabs.forEach(function (t, j) {
      var on = j === i;
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.tabIndex = on ? 0 : -1;
      if (panels[j]) panels[j].hidden = !on;
    });
    if (focus) tabs[i].focus();
    if ((tabs[i].getAttribute('data-tab') || '') === 'feed') ensureFeed();
  }
  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () { select(i, false); });
    t.addEventListener('keydown', function (e) {
      var n = null;
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') n = (i + 1) % tabs.length;
      else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') n = (i - 1 + tabs.length) % tabs.length;
      else if (e.key === 'Home') n = 0;
      else if (e.key === 'End') n = tabs.length - 1;
      if (n !== null) { e.preventDefault(); select(n, true); }
    });
  });

  /* ---------------- feed: X widget with hard fallback ---------------- */
  var feed = fig.querySelector('.fm-feed');
  var feedStarted = false;

  function showFallback() {
    if (!feed) return;
    var live = feed.querySelector('.fm-feed-live');
    var fb = feed.querySelector('.fm-feed-fallback');
    if (live) { live.innerHTML = ''; live.hidden = true; }
    if (fb) fb.hidden = false;
    feed.classList.remove('is-pending');
    feed.classList.add('is-fallback');
  }

  function ensureFeed() {
    if (!feed || feedStarted) return;
    feedStarted = true;
    var handle = feed.getAttribute('data-x-handle');
    var live = feed.querySelector('.fm-feed-live');
    var fb = feed.querySelector('.fm-feed-fallback');
    /* no X handle (e.g. CM Punk, X dormant): never attempt, cards stay up */
    if (!handle || !live) { showFallback(); return; }
    if (navigator.onLine === false) { showFallback(); return; }

    /* live attempt begins: hide the fallback only now */
    if (fb) fb.hidden = true;
    live.hidden = false;
    feed.classList.add('is-pending');

    var h = Math.round(live.getBoundingClientRect().height) || 344;
    if (h < 200) h = 344;
    var a = document.createElement('a');
    a.className = 'twitter-timeline';
    a.setAttribute('data-theme', 'dark');
    a.setAttribute('data-chrome', 'noheader nofooter noborders transparent');
    a.setAttribute('data-height', String(h));
    a.setAttribute('data-dnt', 'true');
    a.href = 'https://twitter.com/' + handle;
    a.textContent = 'Loading posts by @' + handle + ' …';
    live.appendChild(a);

    var settled = false, timer = null, mo = null;
    function fail() {
      if (settled) return; settled = true;
      if (timer) clearTimeout(timer);
      if (mo) mo.disconnect();
      showFallback();
    }
    function ok() {
      if (settled) return; settled = true;
      if (timer) clearTimeout(timer);
      if (mo) mo.disconnect();
      feed.classList.remove('is-pending');
      feed.classList.add('is-live');
    }
    /* hard deadline: 4s with no iframe in the mount = the widget is not coming */
    timer = setTimeout(function () {
      if (live.querySelector('iframe')) ok(); else fail();
    }, 4000);
    /* settle early on success so the deadline never races a rendered iframe */
    if (window.MutationObserver) {
      mo = new MutationObserver(function () {
        if (live.querySelector('iframe')) ok();
      });
      mo.observe(live, { childList: true, subtree: true });
    }

    var src = 'https://platform.twitter.com/widgets.js';
    var s = document.querySelector('script[src^="' + src + '"]');
    if (!s) {
      s = document.createElement('script');
      s.src = src;
      s.async = true;
      s.onerror = fail; /* blocked/refused sooner than 4s -> fall back sooner */
      s.onload = function () {
        try {
          if (window.twttr && window.twttr.widgets && window.twttr.widgets.load) {
            window.twttr.widgets.load(live);
          }
        } catch (e) { /* the 4s deadline still decides */ }
      };
      document.head.appendChild(s);
    } else if (window.twttr && window.twttr.widgets && window.twttr.widgets.load) {
      window.twttr.widgets.load(live);
    }
  }

  /* ------------- metrics ring wiring for GENERATED pages ------------- */
  /* Mirrors cm-punk's inline implementation exactly: full-book tally from
     #rec2-body rows, veil synced to #splTgl, unveil button proxies the
     toggle. Guarded so the hand-wired cm-punk page is never double-wired. */
  if (fig.hasAttribute('data-fm-generated')) {
    var fmWl = document.getElementById('fm-wl');
    var tgl = document.getElementById('splTgl');
    if (fmWl && tgl) {
      var rows = [].slice.call(document.querySelectorAll('#rec2-body tr[data-result]'));
      var C = { W: 0, L: 0, D: 0, NC: 0 };
      rows.forEach(function (r) {
        var v = r.getAttribute('data-result');
        if (C.hasOwnProperty(v)) C[v]++;
      });
      var T = C.W + C.L + C.D + C.NC;
      var CIRC = 2 * Math.PI * 44;
      var seg = function (id, count, off) {
        var el = document.getElementById(id);
        if (!el) return off;
        var len = T ? CIRC * count / T : 0;
        el.setAttribute('stroke-dasharray', len + ' ' + (CIRC - len));
        el.setAttribute('stroke-dashoffset', String(-off));
        return off + len;
      };
      var setTxt = function (id, v) {
        var el = document.getElementById(id);
        if (el) el.textContent = v;
      };
      var fmFill = function () {
        var off = 0;
        off = seg('fm-w', C.W, off); off = seg('fm-l', C.L, off);
        off = seg('fm-d', C.D, off); seg('fm-n', C.NC, off);
        setTxt('fm-pct', (T ? Math.round(100 * C.W / T) : 0) + '%');
        setTxt('fm-rec', C.W + '-' + C.L + (C.D ? '-' + C.D : ''));
      };
      var fmVeil = function (veiled) {
        fmWl.classList.toggle('rec2-wl-veiled', veiled);
        var g = fmWl.querySelector('.rec2-donut'), sd = fmWl.querySelector('.fm-wl-rec');
        if (g) g.setAttribute('aria-hidden', veiled ? 'true' : 'false');
        if (sd) sd.setAttribute('aria-hidden', veiled ? 'true' : 'false');
        if (!veiled) fmFill();
      };
      /* registered after the inline tail script's own splTgl listener, so
         aria-pressed is already flipped when this reads it - same contract
         as cm-punk's hand-wired block */
      tgl.addEventListener('click', function () {
        fmVeil(tgl.getAttribute('aria-pressed') !== 'true');
      });
      var fmU = fmWl.querySelector('.rec2-wl-unveil');
      if (fmU) fmU.addEventListener('click', function () { tgl.click(); });
    }
  }

  /* ---------------- boot: honour the markup's default tab ---------------- */
  var start = 0;
  for (var i = 0; i < tabs.length; i++) {
    if (tabs[i].getAttribute('aria-selected') === 'true') { start = i; break; }
  }
  select(start, false);
})();
