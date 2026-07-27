/* =========================================================================
   WRESTLE LORE — MEDIA KIT (kit.js)
   Dependency-free vanilla JS. Exposes a small global `WL`.
   Pairs with kit.css (+ base.css). No build step, no imports.

   Public API
   ----------
   WL.mountFacades(root=document)         upgrade every .yt[data-yt-id] facade
   WL.initFeed({container, data, renderCard, batch=8, loops=3, onRender})
   WL.autoplayOnScroll(opts?)             muted autoplay-on-scroll for opt-in players
   WL.miniPlayer                          sticky mini-player controller { dock, restore, close }
   WL.reveals(root=document)              IntersectionObserver reveal-on-scroll (+ stagger)
   WL.scrollProgress()                    top progress bar (CSS scroll-timeline w/ JS fallback)
   WL.backToTop()                         back-to-top button
   WL.init(opts?)                         convenience: reveals + progress + backToTop + mountFacades

   Degradation: with no JS the .yt facade is a real <a> link to the video.
   Everything is keyboard-accessible and every iframe gets a title.
   ========================================================================= */
(function (global) {
  'use strict';

  /* mark JS on so base.css reveal start-states apply (content stays visible w/o JS) */
  try { document.documentElement.classList.add('js'); } catch (e) {}

  var hasIO = typeof IntersectionObserver !== 'undefined';
  var reduceMotion = (function () {
    try { return matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) { return false; }
  })();
  var saveData = (function () {
    var c = navigator.connection || navigator.webkitConnection || navigator.mozConnection;
    return !!(c && (c.saveData === true || /(^|-)2g$/.test(c.effectiveType || '')));
  })();

  var NOCOOKIE = 'https://www.youtube-nocookie.com/embed/';
  var THUMB = function (id) { return 'https://i.ytimg.com/vi/' + encodeURIComponent(id) + '/hqdefault.jpg'; };
  var WATCH = function (id) { return 'https://www.youtube.com/watch?v=' + encodeURIComponent(id); };
  var IFRAME_ALLOW = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; web-share';
  var MAX_LIVE = 2; /* cap concurrent live iframes (perf) */

  function esc(s) { return String(s == null ? '' : s); }
  function initialsOf(s) {
    var words = esc(s).replace(/[^\w\s]/g, ' ').trim().split(/\s+/).filter(Boolean);
    if (!words.length) return 'WL';
    return (words[0][0] + (words[1] ? words[1][0] : (words[0][1] || ''))).toUpperCase();
  }

  /* ------------------------------------------------------------------ *
   * YouTube IFrame API — loaded lazily, only when a player needs it.   *
   * ------------------------------------------------------------------ */
  var ytPromise = null;
  function ensureYT() {
    if (ytPromise) return ytPromise;
    ytPromise = new Promise(function (resolve) {
      if (global.YT && global.YT.Player) { resolve(global.YT); return; }
      var prev = global.onYouTubeIframeAPIReady;
      global.onYouTubeIframeAPIReady = function () {
        if (typeof prev === 'function') { try { prev(); } catch (e) {} }
        resolve(global.YT);
      };
      var tag = document.createElement('script');
      tag.src = 'https://www.youtube.com/iframe_api';
      tag.async = true;
      tag.onerror = function () { /* API blocked/offline: players just stay dumb iframes */ };
      (document.head || document.documentElement).appendChild(tag);
    });
    return ytPromise;
  }

  /* Registry of activated facades (FIFO for concurrency cap). */
  var live = [];

  function safePlayer(yt) { return yt && yt.__wlPlayer; }
  function callPlayer(yt, method) {
    var p = safePlayer(yt);
    try { if (p && typeof p[method] === 'function') p[method](); } catch (e) {}
  }

  function registerPlayer(yt) {
    var iframe = yt.querySelector('iframe');
    if (!iframe) return;
    ensureYT().then(function (YT) {
      if (!YT || !YT.Player || yt.__wlPlayer || !yt.isConnected) return;
      try {
        yt.__wlPlayer = new YT.Player(iframe, {
          events: {
            onStateChange: function (e) {
              /* remember whether this player is actively playing */
              if (e.data === YT.PlayerState.PLAYING) yt.__wlPlaying = true;
              if (e.data === YT.PlayerState.PAUSED || e.data === YT.PlayerState.ENDED) yt.__wlPlaying = false;
            }
          }
        });
      } catch (e) {}
    });
  }

  /* Tear a facade back down to its lightweight state (frees ~1-2MB). */
  function teardown(yt) {
    if (!yt || !yt.classList.contains('is-active')) return;
    if (WL.miniPlayer && WL.miniPlayer.current === yt) return; /* never kill the docked player */
    var p = yt.__wlPlayer;
    if (p && typeof p.destroy === 'function') { try { p.destroy(); } catch (e) {} }
    yt.__wlPlayer = null; yt.__wlPlaying = false;
    var f = yt.querySelector('iframe');
    if (f) f.remove();
    yt.classList.remove('is-active');
    var i = live.indexOf(yt); if (i > -1) live.splice(i, 1);
  }

  function enforceCap() {
    for (var n = live.length - 1; n >= 0 && live.length > MAX_LIVE; n--) {
      var yt = live[0];
      if (WL.miniPlayer && WL.miniPlayer.current === yt) { /* keep docked, try next */
        live.push(live.shift());
        // avoid infinite loop if everything is docked (only one can be)
        continue;
      }
      teardown(yt);
    }
  }

  /* ------------------------------------------------------------------ *
   * Shared observers for activated players: dock/pause when offscreen. *
   * ------------------------------------------------------------------ */
  var playerIO = hasIO ? new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      var yt = en.target;
      if (!yt.classList.contains('is-active')) return;
      if (!en.isIntersecting) {
        /* scrolled away: dock the primary into the mini-player, else pause */
        if (!saveData && WL.miniPlayer && !WL.miniPlayer.current && yt.__wlPrimary) {
          WL.miniPlayer.dock(yt);
        } else if (WL.miniPlayer && WL.miniPlayer.current !== yt) {
          callPlayer(yt, 'pauseVideo');
        }
      } else {
        /* scrolled back: restore from the mini-player */
        if (WL.miniPlayer && WL.miniPlayer.current === yt) WL.miniPlayer.restore();
      }
    });
  }, { threshold: 0.1 }) : null;

  /* ------------------------------------------------------------------ *
   * 1. FACADES                                                          *
   * ------------------------------------------------------------------ */
  var thumbIO = hasIO ? new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      loadThumb(en.target);
      thumbIO.unobserve(en.target);
    });
  }, { rootMargin: '300px 0px' }) : null;

  function loadThumb(yt) {
    var id = yt.getAttribute('data-yt-id');
    var img = yt.querySelector('.yt__thumb');
    if (!img || img.src) return;
    img.onerror = function () { yt.classList.add('is-broken'); };
    img.src = THUMB(id);
  }

  function mountFacade(yt) {
    if (yt.__wlMounted) return;
    var id = yt.getAttribute('data-yt-id');
    if (!id) return;
    yt.__wlMounted = true;

    var title = yt.getAttribute('data-yt-title') || 'wrestling video';
    var creator = yt.getAttribute('data-yt-creator') || '';
    var dur = yt.getAttribute('data-yt-dur') || '';

    /* ensure the progressive-enhancement anchor exists (real link w/o JS) */
    var link = yt.querySelector('.yt__link');
    if (!link) {
      link = document.createElement('a');
      link.className = 'yt__link';
      link.href = WATCH(id);
      yt.insertBefore(link, yt.firstChild);
    }
    link.setAttribute('aria-label', 'Play: ' + title);
    link.textContent = ''; /* clear no-JS fallback text; chrome injected below */

    /* thumbnail (lazy) */
    var img = document.createElement('img');
    img.className = 'yt__thumb';
    img.loading = 'lazy'; img.decoding = 'async';
    img.width = 480; img.height = 270; img.alt = '';
    link.appendChild(img);

    /* broken-thumbnail fallback (gradient + mono initials) */
    var fb = document.createElement('span');
    fb.className = 'yt__fallback'; fb.setAttribute('aria-hidden', 'true');
    fb.textContent = initialsOf(creator || title);
    link.appendChild(fb);

    /* top meta overlay */
    var meta = document.createElement('span');
    meta.className = 'yt__meta'; meta.setAttribute('aria-hidden', 'true');
    var t = document.createElement('span'); t.className = 'yt__title'; t.textContent = title;
    meta.appendChild(t);
    if (creator) { var c = document.createElement('span'); c.className = 'yt__creator'; c.textContent = creator; meta.appendChild(c); }
    link.appendChild(meta);

    /* play button (decorative) */
    var play = document.createElement('span');
    play.className = 'yt__play'; play.setAttribute('aria-hidden', 'true');
    play.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>';
    link.appendChild(play);

    /* duration pill */
    if (dur) { var d = document.createElement('span'); d.className = 'yt__dur'; d.textContent = dur; link.appendChild(d); }

    yt.classList.add('is-mounted');

    /* lazy thumbnail load */
    if (thumbIO) thumbIO.observe(yt); else loadThumb(yt);

    /* activate on click / Enter (anchor => keyboard works natively).
       User clicks open the MODAL player (reliable from file:// and prod);
       scroll-autoplay still uses inline activate() for the muted preview. */
    link.addEventListener('click', function (e) {
      e.preventDefault();
      openModal(yt.getAttribute('data-yt-id'), yt.getAttribute('data-yt-title') || 'YouTube video player', {
        service: yt.getAttribute('data-yt-service'),
        serviceUrl: yt.getAttribute('data-yt-service-url')
      });
    });
  }

  /* ------------------------------------------------------------------ *
   * MODAL / LIGHTBOX PLAYER  (primary click-to-play; clean embed)      *
   * ------------------------------------------------------------------ */
  var modal = null, modalEsc = null;
  function buildModal() {
    if (modal) return modal;
    var ov = document.createElement('div');
    ov.className = 'wl-modal'; ov.hidden = true;
    ov.setAttribute('role', 'dialog'); ov.setAttribute('aria-modal', 'true');
    ov.setAttribute('aria-label', 'Video player');
    ov.innerHTML =
      '<div class="wl-modal__backdrop"></div>' +
      '<div class="wl-modal__box">' +
        '<button class="wl-modal__close" type="button" aria-label="Close video">✕</button>' +
        '<div class="wl-modal__stage"></div>' +
        '<div class="wl-modal__bar"><span class="wl-modal__title"></span>' +
        '<span class="wl-modal__links">' +
        '<a class="wl-modal__svc" target="_blank" rel="noopener" hidden></a>' +
        '<a class="wl-modal__yt" target="_blank" rel="noopener">Watch on YouTube ↗</a></span></div>' +
      '</div>';
    document.body.appendChild(ov);
    ov.querySelector('.wl-modal__backdrop').addEventListener('click', closeModal);
    ov.querySelector('.wl-modal__close').addEventListener('click', closeModal);
    modal = ov;
    return ov;
  }
  function openModal(id, title, opts) {
    if (!id) return;
    opts = opts || {};
    var ov = buildModal();
    var stage = ov.querySelector('.wl-modal__stage');
    stage.innerHTML = '';
    var iframe = document.createElement('iframe');
    /* CLEAN params only — no enablejsapi/origin, so the player config is valid
       from a file:// preview AND from production. */
    iframe.src = NOCOOKIE + encodeURIComponent(id) + '?autoplay=1&rel=0&playsinline=1';
    iframe.title = title || 'YouTube video player';
    iframe.setAttribute('allow', IFRAME_ALLOW);
    iframe.setAttribute('allowfullscreen', '');
    iframe.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
    stage.appendChild(iframe);
    ov.querySelector('.wl-modal__title').textContent = title || '';
    ov.querySelector('.wl-modal__yt').href = 'https://www.youtube.com/watch?v=' + id;
    var svc = ov.querySelector('.wl-modal__svc');
    if (opts.service && opts.serviceUrl) {
      svc.href = opts.serviceUrl;
      svc.textContent = 'Full show on ' + opts.service + ' ↗';
      svc.hidden = false;
    } else {
      svc.hidden = true; svc.removeAttribute('href');
    }
    ov.__lastFocus = document.activeElement;
    ov.hidden = false;
    document.documentElement.style.overflow = 'hidden';
    modalEsc = function (e) { if (e.key === 'Escape') closeModal(); };
    document.addEventListener('keydown', modalEsc);
    try { ov.querySelector('.wl-modal__close').focus(); } catch (e) {}
  }
  function closeModal() {
    if (!modal || modal.hidden) return;
    modal.querySelector('.wl-modal__stage').innerHTML = ''; /* stop playback */
    modal.hidden = true;
    document.documentElement.style.overflow = '';
    if (modalEsc) { document.removeEventListener('keydown', modalEsc); modalEsc = null; }
    try { if (modal.__lastFocus && modal.__lastFocus.focus) modal.__lastFocus.focus(); } catch (e) {}
  }

  function activate(yt, opts) {
    if (yt.classList.contains('is-active')) return;
    opts = opts || {};
    var id = yt.getAttribute('data-yt-id');
    if (!id) return;
    var title = yt.getAttribute('data-yt-title') || 'YouTube video player';

    /* file:// has no valid origin for the JS API, which triggers the
       "player configuration" error (153). Omit enablejsapi/origin there. */
    var isFile = location.protocol === 'file:';
    var params = 'autoplay=1&rel=0&playsinline=1';
    if (!isFile) params += '&enablejsapi=1&origin=' + encodeURIComponent(location.origin);
    if (opts.mute || saveData) params += '&mute=1';

    var iframe = document.createElement('iframe');
    iframe.src = NOCOOKIE + encodeURIComponent(id) + '?' + params;
    iframe.title = title;
    iframe.setAttribute('allow', IFRAME_ALLOW);
    iframe.setAttribute('allowfullscreen', '');
    iframe.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
    iframe.loading = 'eager';
    yt.appendChild(iframe);
    yt.classList.add('is-active');
    if (!opts.autoScroll) yt.__wlPrimary = true; /* user-clicked => can dock to mini */

    live.push(yt);
    enforceCap();

    if (playerIO) playerIO.observe(yt);
    registerPlayer(yt);

    /* move focus into the newly-mounted player for keyboard users */
    iframe.addEventListener('load', function () { try { iframe.focus(); } catch (e) {} }, { once: true });
  }

  function mountFacades(root) {
    root = root || document;
    var list = root.querySelectorAll ? root.querySelectorAll('.yt[data-yt-id]') : [];
    for (var i = 0; i < list.length; i++) mountFacade(list[i]);
    return list.length;
  }

  /* ------------------------------------------------------------------ *
   * 2. STICKY MINI-PLAYER  (moves the SAME iframe node => uninterrupted)*
   * ------------------------------------------------------------------ */
  var miniPlayer = {
    el: null, stage: null, label: null, current: null, origin: null,
    _build: function () {
      if (this.el) return this.el;
      var box = document.createElement('section');
      box.className = 'wl-mini';
      box.setAttribute('aria-label', 'Mini player');
      var bar = document.createElement('div'); bar.className = 'wl-mini__bar';
      var grip = document.createElement('span'); grip.className = 'wl-mini__grip';
      grip.innerHTML = '<i></i><i></i><i></i><i></i><i></i><i></i>';
      var label = document.createElement('span'); label.className = 'wl-mini__label'; label.textContent = 'NOW PLAYING';
      var close = document.createElement('button');
      close.type = 'button'; close.className = 'wl-mini__close';
      close.setAttribute('aria-label', 'Close mini player'); close.innerHTML = '&times;';
      var self = this;
      close.addEventListener('click', function () { self.close(); });
      bar.appendChild(grip); bar.appendChild(label); bar.appendChild(close);
      var stage = document.createElement('div'); stage.className = 'wl-mini__stage';
      box.appendChild(bar); box.appendChild(stage);
      document.body.appendChild(box);
      this.el = box; this.stage = stage; this.label = label;
      this._makeDraggable(box, bar);
      return box;
    },
    dock: function (yt) {
      if (!yt || this.current) return;
      var iframe = yt.querySelector('iframe');
      if (!iframe) return;
      this._build();
      this.origin = yt; this.current = yt;
      var t = yt.getAttribute('data-yt-title');
      if (t) this.label.textContent = t;
      this.stage.appendChild(iframe); /* move same node — playback continues */
      this.el.classList.add('is-open');
    },
    restore: function () {
      if (!this.current) return;
      var iframe = this.stage.querySelector('iframe');
      if (iframe && this.origin) this.origin.appendChild(iframe);
      this.el.classList.remove('is-open');
      this.current = null; this.origin = null;
    },
    close: function () {
      if (!this.current) { if (this.el) this.el.classList.remove('is-open'); return; }
      var yt = this.origin;
      var iframe = this.stage.querySelector('iframe');
      if (iframe && yt) yt.appendChild(iframe);
      this.el.classList.remove('is-open');
      var cur = this.current;
      this.current = null; this.origin = null;
      teardown(cur); /* fully release now that it's dismissed */
    },
    _makeDraggable: function (box, handle) {
      var dragging = false, sx = 0, sy = 0, ox = 0, oy = 0;
      handle.addEventListener('pointerdown', function (e) {
        if (e.target.closest('.wl-mini__close')) return;
        dragging = true;
        var r = box.getBoundingClientRect();
        ox = r.left; oy = r.top; sx = e.clientX; sy = e.clientY;
        box.style.right = 'auto'; box.style.bottom = 'auto';
        box.style.left = ox + 'px'; box.style.top = oy + 'px';
        try { handle.setPointerCapture(e.pointerId); } catch (err) {}
      });
      handle.addEventListener('pointermove', function (e) {
        if (!dragging) return;
        var nx = Math.max(4, Math.min(window.innerWidth - box.offsetWidth - 4, ox + (e.clientX - sx)));
        var ny = Math.max(4, Math.min(window.innerHeight - box.offsetHeight - 4, oy + (e.clientY - sy)));
        box.style.left = nx + 'px'; box.style.top = ny + 'px';
      });
      handle.addEventListener('pointerup', function (e) {
        dragging = false;
        try { handle.releasePointerCapture(e.pointerId); } catch (err) {}
      });
    }
  };

  /* ------------------------------------------------------------------ *
   * 3. INFINITE FEED                                                    *
   * ------------------------------------------------------------------ */
  function shuffle(arr) {
    var a = arr.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = a[i]; a[i] = a[j]; a[j] = tmp;
    }
    return a;
  }

  function skeleton() {
    var s = document.createElement('div');
    s.className = 'skel';
    s.setAttribute('aria-hidden', 'true');
    s.innerHTML = '<div class="skel__media"></div><div class="skel__lines">' +
      '<div class="skel__bar w-70"></div><div class="skel__bar w-40"></div></div>';
    return s;
  }

  function initFeed(cfg) {
    cfg = cfg || {};
    var container = typeof cfg.container === 'string' ? document.querySelector(cfg.container) : cfg.container;
    if (!container) return null;
    var data = (cfg.data || []).slice();
    var renderCard = cfg.renderCard;
    var batch = cfg.batch || 8;
    var maxLoops = cfg.loops == null ? 3 : cfg.loops;
    if (!renderCard || !data.length) return null;

    /* infrastructure */
    var status = document.createElement('div');
    status.className = 'feed-status'; status.setAttribute('role', 'status'); status.setAttribute('aria-live', 'polite');
    var loading = document.createElement('div');
    loading.className = 'feed-loading'; loading.hidden = true;
    loading.innerHTML = '<span class="pip"></span> Loading more classics';
    var brk = document.createElement('div');
    brk.className = 'feed-break'; brk.hidden = true;
    brk.setAttribute('role', 'group'); brk.setAttribute('aria-label', "You're caught up");
    var sentinel = document.createElement('div');
    sentinel.className = 'feed-sentinel'; sentinel.setAttribute('aria-hidden', 'true');

    container.appendChild(status);
    container.appendChild(loading);
    container.appendChild(brk);
    container.appendChild(sentinel);

    var playlist = shuffle(data);
    var cursor = 0, loops = 0, loading_ = false, done = false;

    function extend() {
      loops++;
      if (loops >= maxLoops) { done = true; return; }
      var more = shuffle(data);
      /* de-dupe the seam so the loop isn't obvious */
      var lastIds = {};
      playlist.slice(-Math.min(batch, playlist.length)).forEach(function (v) { lastIds[v.id] = 1; });
      more = more.filter(function (v, i) { return i > 4 || !lastIds[v.id]; });
      playlist = playlist.concat(more);
    }

    function showBreak() {
      io && io.disconnect();
      brk.innerHTML =
        '<span class="feed-break__kicker">// press row // you\'re caught up</span>' +
        '<h3 class="feed-break__title">That\'s a wrap for now</h3>' +
        '<p class="feed-break__body">You\'ve rolled through a full card of classics. ' +
        'Take a breather — or keep the marathon going. Your call.</p>';
      var keep = document.createElement('button');
      keep.type = 'button'; keep.className = 'btn btn--gold';
      keep.textContent = 'Keep scrolling';
      keep.addEventListener('click', function () {
        brk.hidden = true;
        done = false; loops = 0;
        playlist = playlist.concat(shuffle(data));
        if (io) io.observe(sentinel);
        renderBatch();
        keep.blur();
      });
      brk.appendChild(keep);
      brk.hidden = false;
    }

    function renderBatch() {
      if (loading_ || done) return;
      if (cursor >= playlist.length) { extend(); if (done) { showBreak(); return; } }
      loading_ = true;
      loading.hidden = false;

      /* skeletons while "loading" */
      var skels = [];
      var end = Math.min(cursor + batch, playlist.length);
      for (var s = 0; s < (end - cursor); s++) { var k = skeleton(); skels.push(k); container.insertBefore(k, sentinel); }

      setTimeout(function () {
        skels.forEach(function (k) { k.remove(); });
        var frag = document.createDocumentFragment();
        var startIdx = cursor;
        for (var i = cursor; i < end; i++) {
          var node = renderCard(playlist[i], i);
          if (node) { node.setAttribute && node.setAttribute('data-reveal', ''); frag.appendChild(node); }
        }
        container.insertBefore(frag, sentinel);
        cursor = end;
        loading.hidden = true;
        loading_ = false;
        status.textContent = 'Loaded ' + cursor + ' videos';

        /* upgrade newly-added facades + wire reveals for the new nodes */
        mountFacades(container);
        reveals(container);

        if (typeof cfg.onRender === 'function') { try { cfg.onRender(startIdx, cursor); } catch (e) {} }

        if (cursor >= playlist.length) { extend(); if (done) showBreak(); }
      }, reduceMotion ? 120 : 480);
    }

    var io = hasIO ? new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting) renderBatch();
    }, { root: null, rootMargin: '800px 0px', threshold: 0 }) : null;

    if (io) io.observe(sentinel); else {
      /* no IO: render everything as a plain paginated fallback */
      while (cursor < playlist.length && loops === 0) { renderBatch(); }
    }

    renderBatch(); /* initial paint */

    return {
      loadMore: renderBatch,
      get cursor() { return cursor; },
      destroy: function () { if (io) io.disconnect(); }
    };
  }

  /* ------------------------------------------------------------------ *
   * 4. AUTOPLAY-ON-SCROLL (muted) via IFrame API — opt-in players       *
   * Targets .yt[data-yt-autoplay]; plays the most-in-view one muted,    *
   * pauses the rest. Disabled under reduced-motion or Save-Data.        *
   * ------------------------------------------------------------------ */
  function autoplayOnScroll(opts) {
    opts = opts || {};
    if (reduceMotion || saveData || !hasIO) return; /* honor prefs: no autoplay */
    var sel = opts.selector || '.yt[data-yt-autoplay]';
    var ratios = new WeakMap();
    var candidates = [];

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { ratios.set(en.target, en.intersectionRatio); });
      /* choose the single most-in-view player */
      var best = null, bestR = 0.6; /* require >=60% visible to start */
      candidates.forEach(function (yt) {
        var r = ratios.get(yt) || 0;
        if (r > bestR) { bestR = r; best = yt; }
      });
      candidates.forEach(function (yt) {
        if (yt === best) {
          if (!yt.classList.contains('is-active')) activate(yt, { mute: true, autoScroll: true });
          callPlayer(yt, 'mute'); callPlayer(yt, 'playVideo');
        } else if (yt.classList.contains('is-active')) {
          callPlayer(yt, 'pauseVideo');
        }
      });
    }, { threshold: [0, 0.6, 0.9] });

    document.querySelectorAll(sel).forEach(function (yt) { candidates.push(yt); io.observe(yt); });
    return { destroy: function () { io.disconnect(); } };
  }

  /* ------------------------------------------------------------------ *
   * 5. REVEAL-ON-SCROLL (with stagger). base.css supplies visuals.      *
   * ------------------------------------------------------------------ */
  var revealIO = hasIO ? new IntersectionObserver(function (entries, obs) {
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      en.target.classList.add('is-in');
      obs.unobserve(en.target);
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 }) : null;

  function reveals(root) {
    root = root || document;
    var els = root.querySelectorAll('[data-reveal]');
    /* stagger index within each grid/rail parent */
    var groups = root.querySelectorAll('.vgrid, .rail, .feed');
    groups.forEach(function (g) {
      var kids = g.children, n = 0;
      for (var i = 0; i < kids.length; i++) {
        if (kids[i].hasAttribute && kids[i].hasAttribute('data-reveal')) {
          kids[i].style.setProperty('--i', (n++ % 8));
        }
      }
    });
    if (reduceMotion || !revealIO) {
      els.forEach(function (el) { el.classList.add('is-in'); });
      return;
    }
    els.forEach(function (el) { if (!el.classList.contains('is-in')) revealIO.observe(el); });
  }

  /* ------------------------------------------------------------------ *
   * 6. SCROLL PROGRESS BAR                                              *
   * ------------------------------------------------------------------ */
  function scrollProgress() {
    var bar = document.querySelector('.wl-progress');
    if (!bar) { bar = document.createElement('div'); bar.className = 'wl-progress'; bar.setAttribute('aria-hidden', 'true'); document.body.appendChild(bar); }
    var cssTimeline = false;
    try { cssTimeline = CSS.supports('animation-timeline: scroll()'); } catch (e) {}
    if (cssTimeline && !reduceMotion) { bar.classList.add('is-css'); return; }
    /* JS fallback: rAF + passive listener */
    var ticking = false;
    function update() {
      var h = document.documentElement;
      var max = (h.scrollHeight - h.clientHeight) || 1;
      var p = Math.min(1, Math.max(0, h.scrollTop / max));
      bar.style.transform = 'scaleX(' + p + ')';
      ticking = false;
    }
    addEventListener('scroll', function () {
      if (ticking) return; ticking = true; requestAnimationFrame(update);
    }, { passive: true });
    addEventListener('resize', function () { requestAnimationFrame(update); }, { passive: true });
    update();
  }

  /* ------------------------------------------------------------------ *
   * 7. BACK-TO-TOP                                                      *
   * ------------------------------------------------------------------ */
  function backToTop() {
    var btn = document.querySelector('.wl-totop');
    if (!btn) {
      btn = document.createElement('button');
      btn.type = 'button'; btn.className = 'wl-totop';
      btn.setAttribute('aria-label', 'Back to top'); btn.innerHTML = '&uarr;';
      document.body.appendChild(btn);
    }
    btn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
      var target = document.querySelector('a[href], button');
      if (target && target !== btn) { try { target.focus(); } catch (e) {} }
    });
    var ticking = false;
    function update() {
      var show = (window.scrollY || document.documentElement.scrollTop) > 600;
      btn.classList.toggle('is-show', show);
      ticking = false;
    }
    addEventListener('scroll', function () {
      if (ticking) return; ticking = true; requestAnimationFrame(update);
    }, { passive: true });
    update();
  }

  /* ------------------------------------------------------------------ *
   * Convenience bootstrap                                               *
   * ------------------------------------------------------------------ */
  function init(opts) {
    opts = opts || {};
    if (opts.reveals !== false) reveals(document);
    if (opts.scrollProgress !== false) scrollProgress();
    if (opts.backToTop !== false) backToTop();
    if (opts.mountFacades !== false) mountFacades(document);
    return WL;
  }

  var WL = {
    mountFacades: mountFacades,
    activate: activate,
    openModal: openModal,
    closeModal: closeModal,
    initFeed: initFeed,
    autoplayOnScroll: autoplayOnScroll,
    miniPlayer: miniPlayer,
    reveals: reveals,
    scrollProgress: scrollProgress,
    backToTop: backToTop,
    init: init,
    _teardown: teardown,
    get live() { return live.slice(); }
  };

  global.WL = WL;
})(typeof window !== 'undefined' ? window : this);

/* ==================================================================== *
 * AUTO-INIT for Wrestle Lore media pages.                              *
 * Facade thumbnail -> click -> modal player (WL wires this in mount).  *
 * No autoplay-on-scroll: click-to-modal only, per product decision.    *
 * Generic single-select chip filter:                                   *
 *   <div data-wl-filters data-wl-grid="#sel"> buttons [data-f][data-group]
 *   filtering [data-wl-item][data-tags="a b c"] inside the grid.        *
 * ==================================================================== */
(function () {
  function initFilters() {
    var bars = document.querySelectorAll('[data-wl-filters]');
    for (var b = 0; b < bars.length; b++) (function (bar) {
      var gridSel = bar.getAttribute('data-wl-grid');
      var grid = (gridSel && document.querySelector(gridSel)) || bar.nextElementSibling;
      if (!grid) return;
      var state = {};
      bar.addEventListener('click', function (e) {
        var btn = e.target.closest('[data-f]'); if (!btn) return;
        var group = btn.getAttribute('data-group') || 'default';
        var val = btn.getAttribute('data-f');
        state[group] = (val === 'all') ? null : val;
        var chips = bar.querySelectorAll('[data-f]');
        for (var i = 0; i < chips.length; i++) {
          if ((chips[i].getAttribute('data-group') || 'default') === group)
            chips[i].setAttribute('aria-pressed', chips[i] === btn ? 'true' : 'false');
        }
        var items = grid.querySelectorAll('[data-wl-item]'), shown = 0;
        for (var j = 0; j < items.length; j++) {
          var tags = ' ' + (items[j].getAttribute('data-tags') || '') + ' ', ok = true;
          for (var g in state) { if (state[g] && tags.indexOf(' ' + state[g] + ' ') === -1) { ok = false; break; } }
          items[j].hidden = !ok; if (ok) shown++;
        }
        var live = bar.parentNode.querySelector('[data-wl-count]');
        if (live) live.textContent = shown;
      });
    })(bars[b]);
  }
  function boot() {
    if (!window.WL) return;
    try { WL.init(); } catch (e) {}
    try { initFilters(); } catch (e) {}
  }
  if (document.readyState !== 'loading') boot();
  else document.addEventListener('DOMContentLoaded', boot);
})();
