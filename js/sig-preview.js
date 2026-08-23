/* sig-preview.js - hover/focus preview for linked Signature Matches cards.
   Loaded by every dossier page; exits instantly when the page has no
   .sig2-card--link[data-sp-title]. No storage, no globals, no network.

   THE CLIPPING PROBLEM, and why the panel lives on <body>:
   .sig2-reel is `overflow-x:auto`. That makes it a scroll container, and a
   scroll container clips its descendants on BOTH axes (overflow-x:auto forces
   the used overflow-y to `auto` too). Clipping is not paint order, so no
   z-index, stacking context or transform on a child can escape it - an
   absolutely-positioned panel inside a card would be sliced off at the reel's
   padding box, and any part hanging below would also trip a scrollbar. The fix
   is to leave the subtree: ONE .sig-prev node is appended to <body>, positioned
   `fixed` from the card's getBoundingClientRect(). It is out of flow, so it
   cannot shift layout, and it is `pointer-events:none`, so it can never come
   between the cursor and the card it describes.

   CONTENT is baked at build time into data-sp-* on the card (title, date,
   where, event, rate, stars, hook) by build/build_dossier.py :: sig_preview,
   read straight out of the target match page. Hovering fetches nothing.

   INPUT CONTRACT:
   - pointer: opens only where a real hover exists, (hover:hover) and
     (pointer:fine). Touch gets nothing at all - a tap just follows the link,
     which is the whole point of the card - so there is no panel to strand.
   - keyboard: opens on :focus-visible, closes on blur. Escape dismisses and
     stays dismissed until focus moves, so Escape is never a toggle-fight.
   - scrolling (window OR the reel) repositions on rAF, and closes once the
     card leaves the viewport, so the panel can never float free of its card. */
(function () {
  "use strict";
  var SEL = ".sig2-card--link[data-sp-title]";
  if (!document.querySelector(SEL)) return;

  var fine = window.matchMedia && matchMedia("(hover:hover) and (pointer:fine)");
  var panel = null, host = null, hushed = null, frame = 0;
  var F = ["title", "date", "where", "event", "rate", "stars", "hook"];

  function build() {
    if (panel) return panel;
    panel = document.createElement("div");
    panel.className = "sig-prev";
    panel.setAttribute("role", "tooltip");
    panel.id = "sig-prev";
    panel.setAttribute("aria-hidden", "true");
    panel.innerHTML =
      '<div class="sig-prev-head"><h4 class="sig-prev-ttl"></h4>' +
      '<div><span class="sig-prev-rate"></span><span class="sig-prev-stars"></span></div></div>' +
      '<p class="sig-prev-meta"></p><p class="sig-prev-hook"></p>' +
      '<span class="sig-prev-cue">Read the full breakdown</span>';
    document.body.appendChild(panel);
    return panel;
  }

  function fill(card) {
    var d = {}, i;
    for (i = 0; i < F.length; i++) d[F[i]] = card.getAttribute("data-sp-" + F[i]) || "";
    var q = function (c) { return panel.querySelector(c); };
    q(".sig-prev-ttl").textContent = d.title;
    q(".sig-prev-rate").textContent = d.rate;
    q(".sig-prev-stars").textContent = d.stars;
    // dateline: EVENT / DATE / VENUE, only the parts the target page actually had
    var meta = [];
    if (d.event) meta.push("<b>" + esc(d.event) + "</b>");
    if (d.date) meta.push(esc(d.date));
    if (d.where) meta.push(esc(d.where));
    q(".sig-prev-meta").innerHTML = meta.join(" &middot; ");
    q(".sig-prev-meta").hidden = !meta.length;
    q(".sig-prev-hook").textContent = d.hook;
    q(".sig-prev-hook").hidden = !d.hook;
  }

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  /* Below the card by default; flipped above when the panel would run past the
     fold; clamped to the viewport on x so a card at the far edge of the reel
     still gets a fully readable panel. */
  function place() {
    if (!host || !panel) return;
    var c = host.getBoundingClientRect();
    var vw = document.documentElement.clientWidth;
    var vh = document.documentElement.clientHeight;
    if (c.bottom < 8 || c.top > vh - 8) { close(); return; }
    var p = panel.getBoundingClientRect();
    var w = p.width || 320, h = p.height || 160, gap = 10;
    var top = c.bottom + gap;
    if (top + h > vh - 12) {
      var above = c.top - gap - h;
      top = above >= 12 ? above : Math.max(12, vh - h - 12);
    }
    var left = c.left + c.width / 2 - w / 2;
    left = Math.max(12, Math.min(left, vw - w - 12));
    panel.style.left = Math.round(left) + "px";
    panel.style.top = Math.round(top) + "px";
  }

  function open(card) {
    if (card === host) return;
    close();
    host = card;
    build();
    fill(card);
    panel.classList.add("is-open");
    panel.setAttribute("aria-hidden", "false");
    card.setAttribute("aria-describedby", "sig-prev");
    card.classList.add("is-previewing");
    place();          // measured once visible, so width/height are real
    place();
  }

  function close() {
    if (!host) return;
    host.classList.remove("is-previewing");
    host.removeAttribute("aria-describedby");
    host = null;
    if (panel) { panel.classList.remove("is-open"); panel.setAttribute("aria-hidden", "true"); }
  }

  function card(e) {
    var t = e.target;
    return t && t.closest ? t.closest(SEL) : null;
  }

  // Opening is a mouseover concern; CLOSING is strictly mouseout's, which knows
  // where the pointer actually went. Closing here on "mouseover of anything that
  // is not a card" looked equivalent and was not: any scroll under a stationary
  // cursor (wheel over the reel, a reveal animation settling, smooth-scroll still
  // running) retargets the pointer and fires mouseover on a neighbour, which tore
  // the panel down a frame after it opened.
  document.addEventListener("mouseover", function (e) {
    if (fine && !fine.matches) return;
    var c = card(e);
    if (!c || c === hushed) return;
    hushed = null;                     // moving to a different card clears the hush
    open(c);
  });
  document.addEventListener("mouseout", function (e) {
    var c = card(e);
    if (!c || c.contains(e.relatedTarget)) return;
    // Trust geometry over the event. A .reveal transition settling, or the reel
    // scrolling, moves the card out from under a STATIONARY cursor and fires a
    // mouseout even though the pointer never left the card's box - which read as
    // "the user left" and killed the panel a frame after it appeared. If the
    // pointer is still inside the card, this is a retarget, not a departure:
    // re-place the panel against the card's new position and stay open.
    var b = c.getBoundingClientRect();
    if (e.clientX >= b.left && e.clientX <= b.right &&
        e.clientY >= b.top && e.clientY <= b.bottom) {
      if (c === host) place();
      return;
    }
    if (c === hushed) hushed = null;   // left it; a later hover may open it again
    if (c === host) close();
  });

  document.addEventListener("focusin", function (e) {
    var c = card(e);
    hushed = null;
    if (!c) { close(); return; }
    // pointer focus (a tap or a click) must not open a panel nobody asked for
    var vis = true;
    try { vis = c.matches(":focus-visible"); } catch (err) { vis = true; }
    if (vis) open(c);
  });
  document.addEventListener("focusout", function (e) {
    if (card(e) === host) close();
  });

  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape" && e.key !== "Esc") return;
    if (!host) return;
    hushed = host;            // stays shut until focus moves elsewhere
    close();
  });

  // a tap/click resolves to navigation; never leave a panel behind it
  document.addEventListener("pointerdown", function () { close(); }, true);

  function nudge() {
    if (!host || frame) return;
    frame = requestAnimationFrame(function () { frame = 0; place(); });
  }
  addEventListener("scroll", nudge, true);   // capture: the reel's own scroll too
  addEventListener("resize", nudge);
})();
