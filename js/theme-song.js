/* theme-song.js - the walk-out strip's Spotify player, with a hard fallback.
   Loaded by any dossier page that carries a theme module; exits instantly when
   the page has no [data-walkout]. No storage, no globals, one iframe.

   Same discipline as js/herotabs.js's X feed, applied to a first-party embed:

   - LAZY. Nothing is requested until an IntersectionObserver says the strip is
     within 240px of the viewport. On a browser without IO we start on load,
     because a player that never loads is worse than an early request.
   - NEVER AUTOPLAY. The `allow` list deliberately omits `autoplay`, so even a
     mis-parameterised embed URL cannot make noise on arrival.
   - HEIGHT IS RESERVED. .wo-stage is a fixed 154px box - 152px of iframe, the
     height Spotify's own oEmbed returns for a compact track player, plus its
     1px hairline each side - and both children are inset:0 inside it
     (css/dossier.css "THE WALK-OUT"), so the swap below cannot move the page.
     Measured at 1440/1280/760: CLS 0.000, geometry identical either side.
   - THE FALLBACK SHIPS VISIBLE. The listen row is in the markup, unhidden, so
     a no-JS or no-network visitor gets the useful thing with no work. It is
     hidden only while a live attempt is actually in flight, and it is never an
     error message - it is where to hear the song.

   Deciding whether the embed actually arrived is the whole problem, because a
   cross-origin frame tells you almost nothing:

     * a BLOCKED navigation still fires `load` (Chromium commits an error page),
       so `load` alone proves nothing - verified in this repo's sandbox;
     * reading fr.contentWindow.location.href throws SecurityError for BOTH a
       real Spotify document and an opaque-origin error page, so the classic
       same-origin probe only tells us the frame left about:blank.

   So the signals actually used are:

     CONFIRM  a postMessage whose origin is exactly https://open.spotify.com
              (only the real embed can send that) -> live, deadline cancelled.
     FAIL     navigator.onLine === false, or the iframe's `error` event, or
              `load` with the frame still readable (it never navigated).
     DEADLINE at 4s with no confirmation we ask a parallel no-cors fetch of the
              same embed URL whether open.spotify.com was reachable at all.
              Unreachable (or fetch unavailable) -> fall back. Reachable -> keep
              the frame: the host is up and the embed simply never spoke to us,
              and yanking a working player away from a visitor is the one
              outcome worse than showing the links.

   The extra reachability request is the deliberate cost of never stealing a
   working player. It is one cached GET of the same URL the frame is already
   fetching, and it is skipped entirely once the embed confirms itself. */
(function () {
  'use strict';

  var wo = document.querySelector('[data-walkout]');
  if (!wo) return;

  var src = wo.getAttribute('data-embed');
  var stage = wo.querySelector('.wo-stage');
  var live = wo.querySelector('.wo-live');
  var listen = wo.querySelector('.wo-listen');
  if (!src || !stage || !live || !listen) return;

  var ORIGIN = 'https://open.spotify.com';
  var DEADLINE = 4000;
  var started = false;

  /* the resting state: listen row up, nothing requested, nothing pending */
  function fallback() {
    live.innerHTML = '';
    live.hidden = true;
    listen.hidden = false;
    stage.classList.remove('is-pending');
    stage.classList.add('is-fallback');
  }

  function start() {
    if (started) return;
    started = true;

    /* known-offline: never attempt, never blink the listen row away */
    if (navigator.onLine === false) { fallback(); return; }

    listen.hidden = true;
    live.hidden = false;
    stage.classList.add('is-pending');

    var fr = document.createElement('iframe');
    fr.src = src;
    /* an iframe with no accessible name is a hole in the tab order */
    fr.title = wo.getAttribute('data-embed-title') || 'Spotify player';
    fr.setAttribute('loading', 'lazy');
    fr.setAttribute('allow', 'clipboard-write; encrypted-media; picture-in-picture');
    fr.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
    live.appendChild(fr);

    var settled = false, timer = null, reach = null, abort = null;

    function done(good) {
      if (settled) return;
      settled = true;
      if (timer) { clearTimeout(timer); timer = null; }
      if (abort) { try { abort.abort(); } catch (e) {} abort = null; }
      window.removeEventListener('message', onMsg);
      if (good) {
        stage.classList.remove('is-pending');
        stage.classList.add('is-live');
      } else {
        fallback();
      }
    }

    function onMsg(e) {
      if (e.origin === ORIGIN) done(true);
    }
    window.addEventListener('message', onMsg);

    fr.addEventListener('error', function () { done(false); });
    fr.addEventListener('load', function () {
      /* Reading the frame's location THROWS once it holds any cross-origin
         document - the real embed or an error page alike. Reading it
         successfully means the frame never left about:blank, which is a
         definite failure and worth acting on before the deadline. */
      try {
        var href = fr.contentWindow.location.href;
        if (!href || href === 'about:blank') { done(false); }
      } catch (e) { /* cross-origin: inconclusive, the deadline decides */ }
    });

    /* parallel reachability probe - the deadline's tie-breaker, see the header.
       Aborted the moment the embed confirms itself, so the happy path pays for
       at most the few hundred ms before the frame says hello. */
    if (window.fetch) {
      try {
        var opts = { mode: 'no-cors', credentials: 'omit', cache: 'force-cache' };
        if (window.AbortController) {
          abort = new AbortController();
          opts.signal = abort.signal;
        }
        fetch(src, opts).then(function () { reach = true; }, function () { reach = false; });
      } catch (e) { reach = false; }
    }

    timer = setTimeout(function () {
      /* reach === true means open.spotify.com answered: keep the player.
         false (refused) or null (no fetch, or still hanging at 4s) means we
         have no evidence the embed is coming, so show the links instead. */
      done(reach === true);
    }, DEADLINE);
  }

  /* offline mid-flight, before anything was requested: stay on the links */
  window.addEventListener('offline', function () { if (!started) { started = true; fallback(); } });

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      if (es[0].isIntersecting) { io.disconnect(); start(); }
    }, { rootMargin: '240px 0px' });
    io.observe(wo);
  } else {
    start();
  }
})();
