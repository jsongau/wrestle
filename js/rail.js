/* ==========================================================================
   rail.js — the "Tale of the Tape" sticky rail, made reachable
   --------------------------------------------------------------------------
   THE DEFECT IT SERVES
   `.wl-dossier .rail` (profile.css:237) is `position:sticky;top:112px` with no
   bound, so a tape taller than `100vh - 112px` has an unreachable bottom.

   PROGRESSIVE ENHANCEMENT ONLY. The disclosure itself is native <details>,
   emitted by build/build_dossier.py (the 8 generated dossiers) and by
   build/migrate_tape.py (the hand-authored ones). With this file absent every
   fact is still visible, every source note is still one click or Enter away on
   its own row with the correct expanded state in the accessibility tree, and
   the credibility line ("14/14 SOURCED") still states the page's provenance.

   What this file adds:

     1. THE CARD CONTROL. The static <p class="tt-cred"> is upgraded in place to
        a <button aria-expanded aria-controls> that opens or closes every note
        at once. Its accessible name is the full sentence, "14 of 14 entries
        carry a source note".

     2. FOLD ONLY WHAT DOES NOT FIT, AND TIGHTEN ONLY WHAT FOLDING CANNOT SAVE.
        A four-rung ladder, re-run on resize, on the webfont swap, and whenever
        a row's height changes:

          A. the rail fits its slot fully expanded
             -> no state class at all. ORIGINAL profile.css metrics, every note
                open. cm-punk at 1440x900 lives here, and so does every page in
                its uncapped state. This is the rung the prototype never had.
          B. it does not fit expanded, but does fit folded
             -> .tt-cap on the rail: bounded flex card, the ledger scrolls in
                its own frame, notes folded. METRICS STILL ORIGINAL.
          C. it does not fit even folded
             -> .tt-dense as well: the tighter tape setting, and only here.
          D. it does not fit even folded and dense — a tape whose values wrap
             several times (cody-rhodes at 1440x700 is the only one in this
             tree)
             -> .tt-tight as well. Last resort, per page AND per viewport.

     3. the scroll-fade and scrollable-region bookkeeping for the case where the
        reader opens everything inside a bounded card.

   TWO THINGS THAT LOOK LIKE OVER-ENGINEERING AND ARE NOT
     * the measurement runs across animation frames, not synchronously. This
       browser defers style recalculation for a subtree that is far off screen:
       a class put on the rail is not reflected in the rows' computed style
       inside the same task, so a synchronous ladder run at load time — when the
       rail sits ~1200px below the fold — measures the PREVIOUS rung's layout.
       Observed directly: the card flipped between rungs several times a second
       for as long as the page was open.
     * the ladder does not run at all until the rail is within 500px of the
       viewport. Until then the card wears the safe default (bounded, folded),
       which nobody can see and which is reachable whatever the content.
   ========================================================================== */
(function () {
  'use strict';

  var rail = document.querySelector('.wl-dossier .rail');
  if (!rail) return;                       /* not a dossier page, or no rail */

  var card = rail.querySelector('.card.tott[data-tape]');
  if (!card) return;                       /* un-migrated page: leave alone */

  var dl = card.querySelector('dl');
  if (!dl) return;
  if (!dl.id) dl.id = 'tott-dl';

  var items   = Array.prototype.slice.call(card.querySelectorAll('details.tsrc'));
  var rows    = card.querySelectorAll('.row').length;
  var touched = false;      /* true once a human has operated any control */

  /* ---------------------------------------------------------------- control */
  var cred = card.querySelector('.tt-cred');
  var btn  = null;
  if (cred && items.length) {
    btn = document.createElement('button');
    btn.type = 'button';
    btn.className = cred.className;
    btn.setAttribute('aria-expanded', 'false');
    btn.setAttribute('aria-controls', dl.id);
    if (cred.title) btn.title = cred.title;
    btn.innerHTML = cred.innerHTML + '<span class="tt-ic" aria-hidden="true"></span>';
    cred.parentNode.replaceChild(btn, cred);
  }
  function claim() { return items.length + ' of ' + rows + ' entries carry a source note.'; }

  /* ------------------------------------------------------------------ state */
  var mq = window.matchMedia('(min-width:961px)');

  function setAll(open) { for (var i = 0; i < items.length; i++) items[i].open = open; }
  function anyOpen()    { for (var i = 0; i < items.length; i++) if (items[i].open) return true; return false; }

  var RUNGS = [
    { cap: false, dense: false, tight: false, open: true  },   /* A */
    { cap: true,  dense: false, tight: false, open: false },   /* B */
    { cap: true,  dense: true,  tight: false, open: false },   /* C */
    { cap: true,  dense: true,  tight: true,  open: false }    /* D */
  ];
  var MOBILE = RUNGS[0];

  function applyState(st, setOpen) {
    rail.classList.toggle('tt-cap',   !!st.cap);
    rail.classList.toggle('tt-dense', !!st.dense);
    rail.classList.toggle('tt-tight', !!st.tight);
    if (setOpen) setAll(st.open);
  }

  /* The sticky slot. profile.css pins the rail at top:112px; the few px of
     slack keep sub-pixel rounding from pushing the last hairline off-screen. */
  function slot()    { return window.innerHeight - 116; }
  function capSlot() { return window.innerHeight - 124; }  /* == the CSS max-height */

  /* ------------------------------------------------------------ measurement
     Measure the card (or the whole rail, when uncapped) in a hypothetical
     state. Everything — the class toggles, the open flags, the read and the
     restore — happens inside ONE synchronous block, so no other code and no
     observer ever sees an intermediate state. */
  function probe(openAll, cap, dense, tight) {
    var saved  = items.map(function (d) { return d.open; });
    var hadCap = rail.classList.contains('tt-cap');
    var hadDen = rail.classList.contains('tt-dense');
    var hadTig = rail.classList.contains('tt-tight');
    rail.classList.toggle('tt-cap',   !!cap);
    rail.classList.toggle('tt-dense', !!dense);
    rail.classList.toggle('tt-tight', !!tight);
    card.classList.add('tt-measure');
    setAll(openAll);
    var h = (cap ? card : rail).getBoundingClientRect().height;
    card.classList.remove('tt-measure');
    for (var i = 0; i < items.length; i++) items[i].open = saved[i];
    rail.classList.toggle('tt-cap',   hadCap);
    rail.classList.toggle('tt-dense', hadDen);
    rail.classList.toggle('tt-tight', hadTig);
    return h;
  }

  /* ------------------------------------------------- scrollable bookkeeping */
  function measure() {
    var over = rail.classList.contains('tt-cap') && dl.scrollHeight - dl.clientHeight > 2;
    card.classList.toggle('is-scrollable', over);
    card.classList.toggle('is-end',
      !over || dl.scrollTop + dl.clientHeight >= dl.scrollHeight - 4);
    /* WCAG 2.1.1: a scrollable region needs to be reachable by keyboard, so the
       ledger becomes a tab stop only while it actually scrolls. */
    if (over) {
      dl.setAttribute('tabindex', '0');
      dl.setAttribute('role', 'group');
      dl.setAttribute('aria-label', 'Tale of the Tape, scrollable');
    } else {
      dl.removeAttribute('tabindex');
      dl.removeAttribute('role');
      dl.removeAttribute('aria-label');
    }
  }

  function sync() {
    if (btn) {
      var open = anyOpen();
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.setAttribute('aria-label',
        claim() + ' ' + (open ? 'Hide all source notes.' : 'Show all source notes.'));
    }
    measure();
  }

  /* -------------------------------------------------------------- the ladder
     A pure function of the content and the viewport: it re-derives the rung
     from scratch every time, so re-running it is idempotent.

     It is re-run often, because the webfont swap changes how many tape values
     WRAP — rhea-ripley's folded card measures 505px against the fallback face
     and 791px against Inter, so deciding once, early, latches the wrong rung.

     Re-running often is also how you get a flip-flop, and one was observed:
     under `prefers-reduced-motion: reduce` this browser returned stale computed
     styles for the tape rows straight after a class change, so consecutive
     evaluations disagreed and the card changed rung several times a second for
     as long as the page was open. Hence: commit the first reading at once (the
     card must never be left unbounded while we deliberate); after that, only
     step DOWN to a looser rung when two consecutive readings agree on it, and
     step UP to a more restrictive one immediately. An over-tight card is
     legible; an under-bounded one is unreachable. A hard evaluation cap per
     viewport size is the backstop, and a resize resets it. */
  var lastKey = '', applied = -1, proposed = -1, evals = 0, floorRung = 0;

  function commit(rung) {
    applyState(RUNGS[rung], !touched);
    applied = rung;
    sync();
  }


  function decide() {
    if (!mq.matches) {                       /* <=960px: static rail, no problem */
      applyState(MOBILE, !touched); applied = 0; sync(); return;
    }
    var key = window.innerWidth + 'x' + window.innerHeight;
    if (key !== lastKey) { lastKey = key; proposed = -1; evals = 0; floorRung = 0; }
    if (evals > 10) return;
    evals++;

    var rung = probe(true,  false, false, false) <= slot()    ? 0
             : probe(false, true,  false, false) <= capSlot() ? 1
             : probe(false, true,  true,  false) <= capSlot() ? 2
             : 3;
    /* never go below a rung that the reality check has already had to impose
       at this viewport size — that would undo the fix on the next reading. */
    if (rung < floorRung) rung = floorRung;

    if (applied < 0)      { proposed = rung; commit(rung); scheduleVerify(); return; }
    if (rung === applied) { proposed = rung; sync(); scheduleVerify(); return; }
    if (rung > applied)   { proposed = rung; commit(rung); scheduleVerify(); return; }
    if (rung !== proposed) { proposed = rung; return; }                /* loosen: confirm */
    commit(rung); scheduleVerify();
  }

  /* ------------------------------------------------------- trust, then verify
     The ladder above measures HYPOTHETICAL states, and a hypothetical
     measurement can be wrong: under `prefers-reduced-motion: reduce` this
     browser was observed reporting a stale layout for the tape rows straight
     after a class change, which made the ladder pick a rung too loose and leave
     the last rows clipped on five of the twelve pages at 1440x700.

     This step measures REALITY instead — the card as it is actually rendered,
     with no class toggling in front of the read — and steps up a rung whenever
     reality says the card still does not fit. It only ever tightens, it is
     bounded by the four rungs, and it cannot fire on a page that fits, because
     both of its conditions are literal failures of the two things the rail has
     to guarantee: the card inside its slot, and no folded row out of reach. */
  var vt = 0, vLeft = 0;
  function scheduleVerify() { vLeft = 6; clearTimeout(vt); vt = setTimeout(verify, 160); }

  function verify() {
    if (vLeft-- <= 0) return;
    clearTimeout(vt); vt = setTimeout(verify, 200);     /* keep watching: the
       webfont swap and late layout can undo a rung that was right at commit */
    if (!mq.matches || applied < 0 || applied >= 3) return;
    var tooTall = rail.getBoundingClientRect().height > slot() + 2;
    var clipped = !anyOpen() && dl.scrollHeight - dl.clientHeight > 2;
    if (!tooTall && !clipped) return;
    commit(applied + 1);
    floorRung = applied;
    vLeft = 6;
  }

  /* ------------------------------------------------------------------ wiring */
  if (btn) {
    btn.addEventListener('click', function () {
      touched = true;
      setAll(!anyOpen());
      sync();
    });
  }

  for (var i = 0; i < items.length; i++) {
    /* <details> fires `toggle` asynchronously; sync() is idempotent and cheap,
       so it is called straight from each one rather than coalesced. */
    items[i].addEventListener('toggle', sync);
    var sum = items[i].querySelector('summary');
    if (sum) {
      /* `touched` must come from a real interaction, never from a programmatic
         open/close, so it is bound to the summary, not to `toggle`. */
      sum.addEventListener('click', function () { touched = true; });
      sum.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ' || e.key === 'Spacebar') touched = true;
      });
    }
  }

  var seen = false, rt = 0;
  function rerun(delay) {
    if (!seen) return;
    clearTimeout(rt);
    rt = setTimeout(decide, delay || 60);
  }
  function onResize() { if (!seen) return; clearTimeout(rt); rt = setTimeout(decide, 140); }

  window.addEventListener('resize', onResize);
  if (mq.addEventListener) mq.addEventListener('change', onResize);
  else if (mq.addListener) mq.addListener(onResize);
  dl.addEventListener('scroll', measure, { passive: true });

  /* the safe default, worn until the first real measurement */
  applyState(mq.matches ? RUNGS[1] : MOBILE, true);
  sync();

  if (window.IntersectionObserver) {
    new IntersectionObserver(function (entries) {
      for (var e = 0; e < entries.length; e++) {
        if (!entries[e].isIntersecting) continue;
        if (!seen) { seen = true; lastKey = ''; applied = -1; }
        rerun(30);
      }
    }, { rootMargin: '500px 0px' }).observe(rail);
  } else {
    seen = true;
    decide();
  }

  /* Ask for the exact faces the tape uses and re-decide when they land.
     `document.fonts.ready` alone is not enough: it resolves whenever nothing is
     *pending*, which includes the moment before the tape's faces have been
     requested at all. rhea-ripley's folded card measures 505px against the
     fallback face and 791px against Inter, so this is not a rounding matter. */
  if (document.fonts) {
    try {
      var faces = [];
      ['dt', 'dd', '.cm'].forEach(function (sel) {
        var el = card.querySelector(sel);
        if (!el) return;
        var cs = getComputedStyle(el);
        faces.push(cs.fontStyle + ' ' + cs.fontWeight + ' ' + cs.fontSize + ' ' + cs.fontFamily);
      });
      Promise.all(faces.map(function (f) {
        return document.fonts.load(f, 'Mg').catch(function () {});
      })).then(function () { rerun(); });
    } catch (e) { /* the Font Loading API refused the shorthand; the hooks below cover it */ }
    if (document.fonts.ready && document.fonts.ready.then) {
      document.fonts.ready.then(function () { rerun(); });
    }
  }

  /* Every row is observed, not just the first: a webfont swap need not change a
     one-line row's height at all — what it changes is how many rows WRAP. */
  if (window.ResizeObserver) {
    var ro = new ResizeObserver(function () { rerun(); });
    var all = card.querySelectorAll('.row');
    for (var ri = 0; ri < all.length; ri++) ro.observe(all[ri]);
  }

  window.addEventListener('load', function () { rerun(); });
  setTimeout(function () { rerun(); }, 600);
  setTimeout(function () { rerun(); }, 1800);
})();
