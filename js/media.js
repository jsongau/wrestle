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
        serviceUrl: yt.getAttribute('data-yt-service-url'),
        page: yt.getAttribute('data-yt-page'),
        promo: yt.getAttribute('data-yt-creator')
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
        '<div class="wl-modal__brand">' +
          '<span class="wl-modal__mark">WL</span>' +
          '<a class="wl-modal__gallery" href="/gallery/">Wrestle Lore <b>Viewing Gallery</b></a>' +
          '<span class="wl-modal__note">Clips embedded from official channels. Watch the full show on its home network.</span>' +
        '</div>' +
        '<div class="wl-modal__body">' +
          '<div class="wl-modal__main">' +
            '<div class="wl-modal__frame"><div class="wl-velvet"><div class="wl-modal__stage"></div></div></div>' +
            '<div class="wl-modal__bar"><a class="wl-modal__title"></a>' +
            '<span class="wl-modal__links">' +
            '<a class="wl-modal__yt" target="_blank" rel="noopener">Watch on YouTube</a>' +
            '<button class="wl-modal__share" type="button"><svg class="wl-share-ico" viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path fill="currentColor" d="M18 16.08a2.9 2.9 0 0 0-2.05.86l-6.9-4.02a3 3 0 0 0 0-1.84l6.83-3.98A3 3 0 1 0 15 5a3 3 0 0 0 .06.6L8.24 9.58a3 3 0 1 0 0 4.84l6.88 4.02A3 3 0 1 0 18 16.08z"/></svg><span>Share</span></button></span></div>' +
          '</div>' +
          '<aside class="wl-modal__side">' +
            '<a class="wl-side__promo" target="_blank" rel="noopener" hidden>' +
              '<span class="wl-side__promo-k">Stream the full show</span>' +
              '<span class="wl-side__promo-net"></span>' +
              '<span class="wl-side__promo-sub"></span>' +
            '</a>' +
            '<div class="wl-side__tabs" role="tablist" aria-label="Filter by promotion"></div>' +
            '<span class="wl-side__head">Keep watching</span>' +
            '<div class="wl-side__list" aria-label="More videos"></div>' +
          '</aside>' +
        '</div>' +
      '</div>';
    document.body.appendChild(ov);
    ov.querySelector('.wl-modal__backdrop').addEventListener('click', closeModal);
    ov.querySelector('.wl-modal__close').addEventListener('click', closeModal);
    var shareBtn = ov.querySelector('.wl-modal__share');
    shareBtn.addEventListener('click', function () {
      var id = ov.__ytid; if (!id) return;
      /* clean page path only — never the title text (defensive strip) */
      var page = (ov.__ytpage || '').trim().split(/\s/)[0];
      var url = page ? (location.origin + page) : (location.origin + location.pathname + '#watch=' + id);
      var title = ov.__yttitle || 'Wrestle Lore';
      if (navigator.share) { navigator.share({ title: 'Wrestle Lore Viewing Gallery', text: title, url: url }).catch(function () {}); return; }
      var restore = function () { shareBtn.querySelector('span').textContent = 'Link copied'; setTimeout(function () { shareBtn.querySelector('span').textContent = 'Share'; }, 1600); };
      if (navigator.clipboard && navigator.clipboard.writeText) { navigator.clipboard.writeText(url).then(restore, function () { window.prompt('Copy this link', url); }); }
      else { window.prompt('Copy this link', url); }
    });
    /* promotion tabs filter the side rail */
    ov.querySelector('.wl-modal__side').addEventListener('click', function (e) {
      var tab = e.target.closest('.wl-side__tab');
      if (tab) { ov.__filter = tab.getAttribute('data-f') || 'ALL'; renderSide(ov); return; }
      var item = e.target.closest('.wl-side__item');
      if (item) {
        /* let the browser open the real page on modifier/middle click (crawlable + new tab) */
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button === 1) return;
        e.preventDefault();
        openModal(item.getAttribute('data-vid'), item.getAttribute('data-t') || 'Wrestle Lore', {
          page: item.getAttribute('data-page'), service: item.getAttribute('data-svc'),
          serviceUrl: item.getAttribute('data-svcurl'), promo: item.getAttribute('data-promo')
        });
      }
    });
    modal = ov;
    return ov;
  }

  function attr(s) { return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;'); }

  /* Homepage and gallery pages label promotions differently ("All Elite
     Wrestling" vs "AEW"). Fold any variant to one canonical code so the
     promotion tabs and autoplay-next work identically on every page. */
  function promoCode(raw) {
    var s = (raw || '').toUpperCase();
    if (/\bNXT\b/.test(s)) return 'NXT';
    if (/\bAEW\b/.test(s) || /ALL ELITE/.test(s)) return 'AEW';
    if (/\bTNA\b/.test(s) || /IMPACT/.test(s)) return 'TNA';
    if (/\bWWE\b/.test(s)) return 'WWE';
    return (raw || '').trim();
  }

  /* Gather every unique video on the page as {id,title,promo,code,page,service,serviceUrl}. */
  function descriptorsFromDOM() {
    var nodes = [].slice.call(document.querySelectorAll('.yt[data-yt-id]'));
    var seen = {}, out = [];
    for (var i = 0; i < nodes.length; i++) {
      var el = nodes[i], id = el.getAttribute('data-yt-id');
      if (!id || seen[id]) continue; seen[id] = 1;
      var raw = el.getAttribute('data-yt-creator') || '';
      out.push({
        id: id, title: el.getAttribute('data-yt-title') || 'Wrestle Lore',
        promo: raw, code: promoCode(raw), page: el.getAttribute('data-yt-page') || '',
        service: el.getAttribute('data-yt-service') || '', serviceUrl: el.getAttribute('data-yt-service-url') || ''
      });
    }
    return out;
  }

  /* Build the right-column promotion tabs + vertical recommended list. */
  function renderSide(ov) {
    var all = ov.__all || [];
    var order = ['WWE', 'AEW', 'TNA', 'NXT'];
    var present = order.filter(function (p) { return all.some(function (d) { return d.code === p; }); });
    /* append any non-standard codes present, preserving first-seen order */
    all.forEach(function (d) { if (d.code && order.indexOf(d.code) === -1 && present.indexOf(d.code) === -1) present.push(d.code); });
    var filter = ov.__filter || 'ALL';
    if (filter !== 'ALL' && present.indexOf(filter) === -1) filter = ov.__filter = 'ALL';
    var tabs = ov.querySelector('.wl-side__tabs');
    var th = '<button class="wl-side__tab" type="button" role="tab" data-f="ALL" aria-selected="' + (filter === 'ALL') + '">All</button>';
    present.forEach(function (p) { th += '<button class="wl-side__tab" type="button" role="tab" data-f="' + attr(p) + '" aria-selected="' + (filter === p) + '">' + attr(p) + '</button>'; });
    tabs.innerHTML = th;
    var filtered = all.filter(function (d) { return filter === 'ALL' || d.code === filter; });
    ov.__filtered = filtered; /* drives autoplay-next (includes current for wrap) */
    var list = ov.querySelector('.wl-side__list'), lh = '';
    filtered.forEach(function (d) {
      var cur = d.id === ov.__ytid ? ' is-current' : '';
      var href = d.page || ('#watch=' + d.id);
      lh += '<a class="wl-side__item' + cur + '" href="' + attr(href) + '" data-vid="' + attr(d.id) + '" data-t="' + attr(d.title) + '"'
        + ' data-page="' + attr(d.page) + '" data-svc="' + attr(d.service) + '" data-svcurl="' + attr(d.serviceUrl) + '" data-promo="' + attr(d.promo) + '">'
        + '<span class="wl-side__thumb" style="background-image:url(https://i.ytimg.com/vi/' + encodeURIComponent(d.id) + '/mqdefault.jpg)"></span>'
        + '<span class="wl-side__meta">' + (d.code ? '<span class="wl-side__ptag">' + attr(d.code) + '</span>' : '')
        + '<span class="wl-side__t">' + attr(d.title) + '</span></span></a>';
    });
    list.innerHTML = lh;
  }

  /* When a video ends, roll straight into the next one in the current filter. */
  function playNext(ov) {
    var list = ov.__filtered || [];
    if (list.length < 2) return;
    var i = -1;
    for (var k = 0; k < list.length; k++) { if (list[k].id === ov.__ytid) { i = k; break; } }
    var nx = list[(i + 1) % list.length];
    if (nx) openModal(nx.id, nx.title, { page: nx.page, service: nx.service, serviceUrl: nx.serviceUrl, promo: nx.promo });
  }

  /* Attach the IFrame API so we can detect ENDED. Needs a valid origin, so we
     only wire it on http(s); a file:// preview just plays without auto-advance. */
  function attachModalPlayer(ov, iframe) {
    if (location.protocol === 'file:') return;
    ensureYT().then(function (YT) {
      if (!YT || !YT.Player || !iframe.isConnected) return;
      try {
        ov.__player = new YT.Player(iframe, {
          events: { onStateChange: function (e) { if (e.data === YT.PlayerState.ENDED) playNext(ov); } }
        });
      } catch (e) {}
    });
  }

  function openModal(id, title, opts) {
    if (!id) return;
    opts = opts || {};
    var ov = buildModal();
    if (ov.__player && ov.__player.destroy) { try { ov.__player.destroy(); } catch (e) {} }
    ov.__player = null;
    var stage = ov.querySelector('.wl-modal__stage');
    stage.innerHTML = '';
    var isFile = location.protocol === 'file:';
    var params = 'autoplay=1&rel=0&playsinline=1';
    /* enablejsapi (+origin) only on the real site — invalid origin triggers 153 on file:// */
    if (!isFile) params += '&enablejsapi=1&origin=' + encodeURIComponent(location.origin);
    var iframe = document.createElement('iframe');
    iframe.src = NOCOOKIE + encodeURIComponent(id) + '?' + params;
    iframe.title = title || 'YouTube video player';
    iframe.setAttribute('allow', IFRAME_ALLOW);
    iframe.setAttribute('allowfullscreen', '');
    iframe.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
    stage.appendChild(iframe);

    /* resolve missing fields from the page's own data */
    ov.__all = descriptorsFromDOM();
    var self = null;
    for (var i = 0; i < ov.__all.length; i++) { if (ov.__all[i].id === id) { self = ov.__all[i]; break; } }
    var promo = (self && self.code) || promoCode(opts.promo) || '';
    var page = opts.page || (self && self.page) || '';
    var service = opts.service || (self && self.service) || '';
    var serviceUrl = opts.serviceUrl || (self && self.serviceUrl) || '';
    ov.__ytid = id; ov.__yttitle = title || ''; ov.__ytpage = page || null;

    /* title links to the video's own page */
    var tt = ov.querySelector('.wl-modal__title');
    tt.textContent = title || '';
    if (page) tt.setAttribute('href', page); else tt.removeAttribute('href');
    ov.querySelector('.wl-modal__yt').href = 'https://www.youtube.com/watch?v=' + id;

    /* streaming promo card (goodwill: sends viewers to the official platform) */
    var promoCard = ov.querySelector('.wl-side__promo');
    if (service && serviceUrl) {
      promoCard.href = serviceUrl;
      promoCard.querySelector('.wl-side__promo-net').textContent = service;
      promoCard.querySelector('.wl-side__promo-sub').textContent = (promo ? promo + ' — watch it all' : 'Watch the full show');
      promoCard.hidden = false;
    } else { promoCard.hidden = true; promoCard.removeAttribute('href'); }

    if (!ov.__filter) ov.__filter = 'ALL';
    renderSide(ov);
    try { var cur = ov.querySelector('.wl-side__item.is-current'); if (cur && cur.scrollIntoView) cur.scrollIntoView({ block: 'nearest' }); } catch (e) {}

    try { history.replaceState(null, '', location.pathname + location.search + '#watch=' + id); } catch (e) {}
    attachModalPlayer(ov, iframe);

    ov.__lastFocus = document.activeElement;
    ov.hidden = false;
    document.documentElement.style.overflow = 'hidden';
    modalEsc = function (e) { if (e.key === 'Escape') closeModal(); };
    document.addEventListener('keydown', modalEsc);
    try { ov.querySelector('.wl-modal__close').focus(); } catch (e) {}
  }
  function closeModal() {
    if (!modal || modal.hidden) return;
    if (modal.__player && modal.__player.destroy) { try { modal.__player.destroy(); } catch (e) {} modal.__player = null; }
    modal.querySelector('.wl-modal__stage').innerHTML = ''; /* stop playback */
    modal.hidden = true;
    document.documentElement.style.overflow = '';
    try { history.replaceState(null, '', location.pathname + location.search); } catch (e) {}
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
  /* Generic master-detail tabs: [data-wl-tabs] with [role=tab][aria-controls]
     toggling [role=tabpanel] by id. Shows the selected panel, hides the rest,
     and (re)mounts facades in the newly shown panel. */
  function initTabs() {
    var groups = document.querySelectorAll('[data-wl-tabs]');
    for (var g = 0; g < groups.length; g++) (function (grp) {
      var tabs = [].slice.call(grp.querySelectorAll('[role="tab"]'));
      function select(tab) {
        for (var i = 0; i < tabs.length; i++) {
          var on = tabs[i] === tab;
          tabs[i].setAttribute('aria-selected', on ? 'true' : 'false');
          tabs[i].tabIndex = on ? 0 : -1;
          var panel = document.getElementById(tabs[i].getAttribute('aria-controls'));
          if (panel) panel.hidden = !on;
        }
        var active = document.getElementById(tab.getAttribute('aria-controls'));
        if (active && window.WL && WL.mountFacades) { try { WL.mountFacades(active); } catch (e) {} }
      }
      grp.addEventListener('click', function (e) { var t = e.target.closest('[role="tab"]'); if (t) select(t); });
      grp.addEventListener('keydown', function (e) {
        if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
        var cur = tabs.indexOf(document.activeElement); if (cur < 0) return;
        e.preventDefault();
        var n = e.key === 'ArrowRight' ? (cur + 1) % tabs.length : (cur - 1 + tabs.length) % tabs.length;
        tabs[n].focus(); select(tabs[n]);
      });
    })(groups[g]);
  }
  /* Shareable deep links: /page#watch=<id> (or ?watch=/?v=) auto-opens the modal. */
  function openFromHash() {
    var src = (location.hash || '') + ' ' + (location.search || '');
    var m = src.match(/(?:watch|v)=([A-Za-z0-9_-]{6,})/);
    if (!m) return;
    var id = m[1];
    if (modal && !modal.hidden && modal.__ytid === id) return; /* already showing it */
    if (!(window.WL && window.WL.openModal)) return;
    var el = document.querySelector('.yt[data-yt-id="' + id + '"]');
    if (el) window.WL.openModal(id, el.getAttribute('data-yt-title') || 'Wrestle Lore', { service: el.getAttribute('data-yt-service'), serviceUrl: el.getAttribute('data-yt-service-url'), page: el.getAttribute('data-yt-page') });
    else window.WL.openModal(id, 'Wrestle Lore');
  }
  /* Per-video page: auto-mount + autoplay (muted so it always starts). */
  function mountPagePlayer() {
    var el = document.querySelector('[data-yt-page-player][data-yt-id]'); if (!el) return;
    var id = el.getAttribute('data-yt-id'); if (!id || el.querySelector('iframe')) return;
    var iframe = document.createElement('iframe');
    iframe.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(id) + '?autoplay=1&rel=0&playsinline=1&mute=1';
    iframe.title = document.title || 'Wrestle Lore video';
    iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share'); iframe.setAttribute('allowfullscreen', '');
    iframe.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
    el.appendChild(iframe);
  }
  /* Share button on the per-video page (data-share-url), copy-or-native-share. */
  function initPageShare() {
    document.addEventListener('click', function (e) {
      var b = e.target.closest('.wl-modal__share[data-share-url]'); if (!b) return;
      var v = b.getAttribute('data-share-url');
      var url = /^https?:/i.test(v) ? v : (location.origin + v);
      if (navigator.share) { navigator.share({ title: 'Wrestle Lore', url: url }).catch(function () {}); return; }
      var s = b.querySelector('span') || b;
      var done = function () { var o = s.textContent; s.textContent = 'Link copied'; setTimeout(function () { s.textContent = o; }, 1600); };
      if (navigator.clipboard && navigator.clipboard.writeText) { navigator.clipboard.writeText(url).then(done, function () { window.prompt('Copy this link', url); }); }
      else { window.prompt('Copy this link', url); }
    });
  }
  function boot() {
    if (!window.WL) return;
    try { WL.init(); } catch (e) {}
    try { initFilters(); } catch (e) {}
    try { initTabs(); } catch (e) {}
    try { mountPagePlayer(); } catch (e) {}
    try { initPageShare(); } catch (e) {}
    try { openFromHash(); } catch (e) {}
    window.addEventListener('hashchange', function () { try { openFromHash(); } catch (e) {} });
    window.addEventListener('load', function () { try { openFromHash(); } catch (e) {} });
  }
  if (document.readyState !== 'loading') boot();
  else document.addEventListener('DOMContentLoaded', boot);
})();
