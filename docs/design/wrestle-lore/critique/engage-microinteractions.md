# Wrestle Lore — Micro-Interactions & Connective Polish (engagement rails)

Role: micro-interaction + visual-polish designer. Scope: the *feel* layer that sits on top of the
three engagement surfaces already shipped in `js/engage.js` / `css/site.css` — the **sticky left
rail** (`.engage-left`), the **sticky bottom rail** (`.engage-bottom`), and the **bottom-right
floater** (`.engage-fab`). The structure, link-sourcing, and mode logic of those rails are owned by
`engage-rails.md` and `engage-floater.md`; this doc owns only the micro-interactions and connective
visual cues that raise *perceived* quality and make cross-page links feel alive: hover previews and
peeks, count-up stats, reveal-on-scroll, magnetic/tilt affordances, tasteful state motion, and
"related" hover cards. It does not re-derive their content recipes.

## Buildability contract (matches the existing layer)

Everything below is buildable with the site's current stack: vanilla JS in one IIFE, appended after
content paint; one shared stylesheet using existing tokens; **no dependencies, no backend, no
browser storage** unless a line is flagged `[STORAGE]`. It reuses the guards already present in
`enhance.js`:

```js
var reduce      = matchMedia('(prefers-reduced-motion: reduce)').matches;      // bail on motion
var finePointer = matchMedia('(hover:hover) and (pointer:fine)').matches;      // gate hover niceties
```

Crawlability is untouched: every destination these interactions decorate is already a real
`<a href>` in the page body or shared nav (see `engage.js` line 17, which harvests
`a[href^="/wrestlers/"]` from `main`). The polish re-presents those edges; it never becomes the only
path to them. If JS never runs, nothing is lost. Copy standard inherited: no decorative arrows in UI
strings, no em-dash separators, no cliche marketing words.

The one existing motion tell to fix on sight: `.engage-fab__spark` runs an **infinite 2.4s pulse
loop** (`site.css` line 1057, `@keyframes fabpulse`). An always-looping pulse is the single most
"ad-chrome" signal a floating widget can emit; §A6 and §C replace it with a one-shot attention beat.

---

## What to steal, and from whom

- **Wikipedia Page Previews (hovercards).** The canonical connective micro-interaction: hover a blue
  link, and after a deliberate **650 ms hover-intent delay** a small card with a summary and thumb
  appears, so you taste a destination before committing. Wikipedia reports ~28% of its traffic is
  internal blue-link clicks and ~2M links are hovered per minute, and the delay exists specifically
  to suppress accidental previews from readers who track text with the cursor. Steal: the intent
  delay, preview-before-commit, and "every link is a node worth peeking".
  (https://diff.wikimedia.org/2018/04/18/how-we-designed-page-previews-for-wikipedia/)
- **GitHub hovercards.** The same pattern applied to an entity graph: hovering a user/issue/repo
  reference pops a typed card (avatar, meta, relation). Steal: hovercards for *typed* neighbors
  (rival, tag-partner, same-event), and the "html-over-the-wire but degrade to a plain link" build
  posture. (https://github.com/topics/hovercard ;
  https://boringrails.com/articles/hovercards-stimulus/)
- **Magnetic buttons (GSAP/vanilla).** A button that leans a fraction toward the cursor inside a
  small activation radius, then springs back. The documented technique: read
  `getBoundingClientRect()` center, translate by `delta * 0.25` within a ~120px radius, reset to
  `translate(0,0)` on exit, `transition: transform .25s ease-out`. Steal: the *0.25 damping* and the
  small radius, applied only to the floater token and the "Show another" control, never to body
  links. (https://en.inithtml.com/resources/magnetic-hover-effect-creating-cursor-attracted-buttons-with-vanilla-javascript/
  ; https://codepen.io/Course-Max-One/pen/QwyjPOg)
- **View Transitions API.** Native, progressively-enhanced shared-element morphs between DOM states
  and (with `@view-transition`) between same-origin pages — no framework, and it no-ops in
  unsupporting browsers. Steal: cross-fade + shared-element continuity so a click from a rail into a
  profile *feels* connected, wrapped in a support check and the reduced-motion guard.
  (https://developer.chrome.com/docs/web-platform/view-transitions/ ;
  https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using)
- **Count-up-on-reveal (already in the codebase).** `enhance.js` already animates `[data-count]`
  once, on IntersectionObserver entry, with a cubic ease-out over 1400 ms and a reduced-motion
  branch that snaps to the final value. Steal: extend this *same* observer to the rails' stat chips
  rather than adding a second observer. (in-repo `js/enhance.js` lines 15-44)
- **Josh Comeau / Smashing "respect motion preferences".** The rule that reduced-motion means
  *replace*, not *delete*: keep opacity fades and instant state changes, drop large translate/scale/
  parallax. Steal: the two-tier motion policy in §D.
  (https://www.joshwcomeau.com/react/prefers-reduced-motion/ ;
  https://www.smashingmagazine.com/2021/10/respecting-users-motion-preferences/)
- **Anti-slop guardrail.** Generic AI sites are flagged precisely by looping pulses, gratuitous
  parallax on everything, and hover effects with no information payload. Every interaction below
  earns its motion by carrying content or state. (https://www.925studios.co/blog/ai-slop-web-design-guide)

---

## Ranked, buildable list

Ranked by **leverage on perceived quality and connectivity per unit of build cost and risk**. Each
item names the rail(s) it lives on, the exact technique, and its reduced-motion behavior.

### A1 — Connective hovercards on rail chips and Keep-going links (HIGHEST leverage)

The single biggest connectivity upgrade. On the bottom rail's `.engage-chip` items and the left
rail's neighbor links, a **desktop-only, hover-intent-delayed** card previews the destination:
mono-crest, name, promotion accent bar, and one harvested fact line (finisher / era / "3-time
champ") — all pulled from the same `window.MAT_SEARCH_INDEX` and in-body links `engage.js` already
reads. It is Wikipedia Page Previews for the roster graph.

- **Trigger:** `mouseenter` starts a 500-650 ms timer (Wikipedia's intent delay); `mouseleave`
  clears it. Only when `finePointer` matches. Touch devices get nothing (the tap already navigates).
- **Content source:** zero new data. Look the chip's `href` up in `MAT_SEARCH_INDEX` for `k`, `t`,
  and any stored blurb; fall back to the chip's own text. No fetch, no storage.
- **Position:** absolutely positioned above the chip, clamped to viewport; card is a `role="tooltip"`
  referenced by `aria-describedby` so it is not a keyboard trap. It is decorative — the link works
  without it.
- **Motion:** 120 ms opacity + 6px rise in. Reduced motion: opacity only, no translate.
- **Crawlability:** the card is injected on hover and contains no unique links; every target is the
  chip's own `href`. Nothing to crawl that is not already crawlable.

```css
.wl-peek{position:fixed;z-index:90;width:236px;padding:.7em .8em;border-radius:var(--r-md);
  background:var(--c-bg-elev-2);border:1px solid var(--c-line-strong);
  box-shadow:0 10px 30px rgba(0,0,0,.45);opacity:0;transform:translateY(6px);
  transition:opacity 120ms var(--ease),transform 120ms var(--ease);pointer-events:none;}
.wl-peek.is-in{opacity:1;transform:none;}
.wl-peek__accent{height:3px;border-radius:2px;background:var(--peek-accent,var(--c-gold));margin-bottom:.5em;}
.wl-peek__name{font-family:var(--font-cond);text-transform:uppercase;letter-spacing:.02em;
  font-size:var(--fs-500);color:var(--c-text);}
.wl-peek__fact{font-size:var(--fs-300);color:var(--c-text-muted);margin-top:.15em;}
@media (prefers-reduced-motion:reduce){.wl-peek{transition:opacity 120ms linear;transform:none;}}
```

```js
// attach once to the bottom-rail row via delegation; requires finePointer && !reduce-optional
var peek, tHover;
function showPeek(a){
  var e = (window.MAT_SEARCH_INDEX||[]).find(function(x){return x.u===a.getAttribute('href');});
  if(!peek){peek=document.createElement('div');peek.className='wl-peek';peek.setAttribute('role','tooltip');document.body.appendChild(peek);}
  peek.innerHTML='<div class="wl-peek__accent"></div><div class="wl-peek__name">'+
    (e?e.t:a.textContent.trim())+'</div><div class="wl-peek__fact">'+(e&&e.blurb?e.blurb:'View profile')+'</div>';
  var r=a.getBoundingClientRect();
  peek.style.left=Math.min(r.left, innerWidth-248)+'px';
  peek.style.top=(r.top-peek.offsetHeight-8)+'px';
  requestAnimationFrame(function(){peek.classList.add('is-in');});
}
row.addEventListener('mouseover',function(ev){var a=ev.target.closest('a');if(!a||!finePointer)return;
  clearTimeout(tHover);tHover=setTimeout(function(){showPeek(a);},550);});
row.addEventListener('mouseout',function(){clearTimeout(tHover);if(peek)peek.classList.remove('is-in');});
```

Source: Wikipedia Page Previews (650 ms delay, preview-before-click); GitHub hovercards (typed
entity peek).

### A2 — Count-up on rail and floater stat chips (reuse existing observer)

Any number the rails surface (a wrestler's title count on a hovercard, "explored N today" in the
floater, a rivalry's match count) animates once on entry using the **existing** `[data-count]`
machinery in `enhance.js`, not a new timer. This borrows the site's own established motion vocabulary
so the rails feel native, and the reduced-motion branch (snap to value) is already written.

- **Build:** render the number as `<span data-count="3" data-suffix=" explored">` inside the injected
  rail DOM; because `engage.js` runs after `enhance.js`, call the existing observer's `observe()` on
  the new node, or simplest: expose a tiny `window.MAT.count(el)` from `enhance.js` and invoke it.
- **Reduced motion:** already handled — `enhance.js` sets `el.textContent = target + suffix` with no
  animation when `reduce` is true.

Source: in-repo `enhance.js` count-up (cubic ease-out, 1400 ms, reduced-motion snap).

### A3 — Reveal-on-entrance for the three rails (staggered, one-shot)

The rails should not just appear; they should *arrive* once, then be still. Reuse the existing
`data-reveal` fade-rise (`is-in` class, IntersectionObserver in `enhance.js`) rather than the current
naked `setTimeout(600)` on the bottom rail (`engage.js` line 59).

- **Bottom rail:** slide up from `translateY(110%)` (already implemented at `site.css` 1037) but gate
  it on first scroll past ~40% depth so it enters when the reader is actually browsing, not on load.
- **Left rail links:** stagger children with a CSS custom-property index so they cascade in over
  ~40 ms each — a Netflix/Linear "list assembling" feel — capped so the last item lands under 300 ms.
- **Reduced motion:** the existing rule `@media (prefers-reduced-motion:reduce){.engage-bottom{transition:none;}}`
  (line 1059) already snaps the bottom rail; add the same for the stagger (opacity to 1, no delay).

```css
.engage-left__a{--i:0;opacity:0;transform:translateX(-6px);
  transition:opacity 220ms var(--ease) calc(var(--i)*40ms),transform 220ms var(--ease) calc(var(--i)*40ms);}
.engage-left.is-in .engage-left__a{opacity:1;transform:none;}
@media (prefers-reduced-motion:reduce){
  .engage-left__a{transition:opacity 160ms linear;transform:none;}}
```

Source: reveal-on-scroll accessibility patterns; in-repo `data-reveal` observer.

### A4 — Active-section "travel" on the left rail (spring the marker, not the text)

The left rail already does scroll-spy (`is-active`, `engage.js` 42-47) but the active state just
snaps a border color. Upgrade it to a single **shared moving marker**: one absolutely-positioned gold
bar that slides between the active link's position, so the eye follows a continuous object down the
page (Linear/Vercel-style animated indicator) instead of a color blinking on and off.

- **Technique:** keep one `.engage-left__marker` element; on the existing IntersectionObserver
  callback, read the active link's `offsetTop`/`offsetHeight` and set the marker's transform, so only
  `transform` animates (compositor-only, no layout thrash).
- **Reduced motion:** marker jumps with `transition:none`; still communicates position.

```css
.engage-left{position:fixed;/* existing */}
.engage-left__marker{position:absolute;left:0;width:2px;background:var(--c-gold);border-radius:2px;
  transform:translateY(var(--y,0)) scaleY(var(--h,1));transform-origin:top;
  transition:transform 240ms var(--ease);}
@media (prefers-reduced-motion:reduce){.engage-left__marker{transition:none;}}
```

```js
function moveMarker(link){var mk=rail.querySelector('.engage-left__marker');
  mk.style.setProperty('--y', link.offsetTop+'px');
  mk.style.height = link.offsetHeight+'px';}
```

Source: animated active-indicator pattern (Linear/Vercel nav); in-repo scroll-spy observer.

### A5 — Magnetic pull + press on the floater token and "Show another" (restraint-gated)

Apply the magnetic effect to **exactly two** controls: the collapsed `.engage-fab__btn` and the
floater's "Show another" refresh. These are discretionary, delight-oriented buttons, which is exactly
where magnetism reads as quality rather than gimmick; body links and nav must never move.

- **Technique (documented):** on `pointermove` within the button's box, translate by `delta * 0.22`;
  reset to `0,0` on `pointerleave`; `transition: transform .25s ease-out`. Wrap in `finePointer &&
  !reduce`. Pair with an active-press `scale(.96)` for tactile feedback.
- **Reduced motion / touch:** effect never attaches; the button is a plain, fully-functional control.

```js
if (finePointer && !reduce) [btn, refreshBtn].forEach(function(el){ if(!el) return;
  el.addEventListener('pointermove',function(e){var r=el.getBoundingClientRect();
    el.style.transform='translate('+((e.clientX-(r.left+r.width/2))*0.22)+'px,'+
      ((e.clientY-(r.top+r.height/2))*0.22)+'px)';});
  el.addEventListener('pointerleave',function(){el.style.transform='translate(0,0)';});
});
```

```css
.engage-fab__btn{transition:transform .25s ease-out,box-shadow var(--dur) var(--ease);}
.engage-fab__btn:active{transform:scale(.96);}
@media (prefers-reduced-motion:reduce){.engage-fab__btn{transition:box-shadow var(--dur) var(--ease);}}
```

Source: magnetic-button vanilla technique (0.25 damping, `getBoundingClientRect` center, 120px radius,
.25s ease-out).

### A6 — Replace the floater's infinite pulse with a one-shot idle beat

Kill `@keyframes fabpulse` looping forever (`site.css` 1057). Replace with a **single** attention
beat: if the floater sits collapsed and untouched for ~20 s, it plays one 500 ms gold-ring flare and
optionally swaps its verb once (per `engage-floater.md` §4), then stays still. One hint, never a loop
— this is the difference between "alive" and "ad".

```css
.engage-fab__spark{animation:none;}                    /* remove the infinite loop */
.engage-fab.is-hinting .engage-fab__btn{animation:wl-beat 500ms var(--ease) 1;}
@keyframes wl-beat{0%{box-shadow:0 0 0 0 var(--c-gold-tint);}100%{box-shadow:0 0 0 14px transparent;}}
@media (prefers-reduced-motion:reduce){.engage-fab.is-hinting .engage-fab__btn{animation:none;}}
```

Source: FAB / floating-widget anti-patterns (looping pulse reads as ad-chrome).

### A7 — Reward beat on the floater "Rate this legend" control

When a reader taps a rating (floater Mode C), play a single short belt/gold "snap" — a scale-pop plus
a brief gold flare on the chosen icon — as the confirmation. This is the Duolingo satisfying-beat
without the streak-shame. One-shot only; no loop; the control remains a labeled radiogroup.

```css
.wl-rate__i.is-picked{animation:wl-pop 260ms var(--ease) 1;}
@keyframes wl-pop{0%{transform:scale(1);}45%{transform:scale(1.28);}100%{transform:scale(1);}}
@media (prefers-reduced-motion:reduce){.wl-rate__i.is-picked{animation:none;
  outline:2px solid var(--c-gold);}}   /* reduced motion: state shown by a static ring, not a pop */
```

Source: Duolingo micro-reward loop (cited in `engage-floater.md`); reduced-motion "replace not
delete".

### A8 — View-Transition continuity from rail click into the profile

When a reader clicks a rail chip or a floater neighbor into another profile, wrap the navigation in a
same-document (SPA-less: use the `@view-transition` cross-document opt-in for same-origin) transition
so the crest/name of the tapped chip *morphs* into the destination hero — the strongest possible
"these pages are connected" cue, and it makes the rabbit hole feel continuous.

- **Build posture:** progressive enhancement, two lines of CSS plus a JS support check. Unsupporting
  browsers navigate normally; nothing breaks. Same-origin only, so the crawler and Back button are
  unaffected.
- **Shared element:** give the tapped chip crest and the destination `.athlete-hero` mono a matching
  `view-transition-name` (set on the outgoing element right before nav). Keep it to *one* named pair
  to avoid janky multi-element morphs.
- **Reduced motion:** the API itself respects `prefers-reduced-motion` when you scope the
  `::view-transition-*` animations behind the media query; default to a plain cross-fade, and disable
  even that under reduce.

```css
@view-transition{ navigation: auto; }                 /* same-origin opt-in */
@media (prefers-reduced-motion:reduce){
  ::view-transition-group(*),::view-transition-old(*),::view-transition-new(*){animation:none !important;}
}
```

```js
// only name the shared element when supported; otherwise it is inert
if (document.startViewTransition && !reduce) chip.style.viewTransitionName = 'wl-hero-crest';
```

Source: View Transitions API (Chrome for Developers; MDN) — native, degrades cleanly, honors motion
prefs.

### A9 — Content-reveal "peek" on the bottom rail chips (scale + accent, no layout shift)

On `.engage-chip:hover`, the current CSS only recolors the border (`site.css` 1045). Add a compositor-
only lift + the chip's promotion accent bleeding into the mono-crest, so hovering the rail feels like
brushing physical cards. Transform/opacity only, so zero reflow and safe at 60fps on the fixed rail.

```css
.engage-chip{transition:transform var(--dur) var(--ease),border-color var(--dur) var(--ease);}
@media (hover:hover){
  .engage-chip:hover{transform:translateY(-3px);border-color:var(--c-gold);}
  .engage-chip:hover .engage-chip__m{background:linear-gradient(145deg,var(--c-gold),var(--c-gold-dim));}}
@media (prefers-reduced-motion:reduce){.engage-chip{transition:border-color var(--dur) var(--ease);}
  .engage-chip:hover{transform:none;}}
```

Source: card hover-lift micro-interaction convention; in-repo `.tile` spotlight pattern (`enhance.js`).

### A10 — Bottom-rail scroll affordance (edge fade + drag-scroll cursor)

The horizontal `.engage-bottom__row` scrolls but gives no signal there is more. Add a CSS mask edge-
fade that appears only when overflow exists, plus a grab cursor, so the rail advertises its own depth
(a small perceived-quality cue that also drives more clicks into the graph). No JS motion; pure CSS.

```css
.engage-bottom__row{-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 24px,#000 calc(100% - 24px),transparent 100%);
  mask-image:linear-gradient(90deg,transparent 0,#000 24px,#000 calc(100% - 24px),transparent 100%);
  cursor:grab;scroll-behavior:smooth;}
.engage-bottom__row:active{cursor:grabbing;}
@media (prefers-reduced-motion:reduce){.engage-bottom__row{scroll-behavior:auto;}}
```

Source: horizontal-rail edge-fade affordance (Netflix/App Store shelves).

---

## Global reduced-motion policy (the two-tier rule)

Follow the "replace, don't delete" doctrine (Josh Comeau; Smashing). Under
`prefers-reduced-motion: reduce`, every interaction above **keeps its information and state change**
and drops only the movement:

| Effect | Full motion | Reduced motion |
|---|---|---|
| Hovercard (A1) | opacity + 6px rise | opacity fade only |
| Count-up (A2) | 1400 ms ease-out | snap to final value (already coded) |
| Rail reveal / stagger (A3) | fade + translate + delay | fade only, no delay |
| Active marker (A4) | slides between links | jumps instantly |
| Magnetic / press (A5) | pull + scale | not attached; static button |
| Idle beat (A6) | one gold flare | no animation |
| Rate reward (A7) | scale-pop | static gold ring |
| View transition (A8) | morph / cross-fade | no `::view-transition` animation |
| Chip / edge-fade (A9/A10) | lift + accent | color change only; instant scroll |

One shared guard at the top of `engage.js` (`var reduce = matchMedia(...).matches;`) drives every JS
branch; the CSS mirrors it with `@media (prefers-reduced-motion:reduce)` blocks appended to the
existing `.engage-*` rules. Nothing above is motion-for-motion's-sake: each animation carries content
(a preview), a value (a count), or a state change (active section, rating) — the anti-slop test.

## Build & perf notes

- **One IIFE, one observer.** Extend `enhance.js`'s single IntersectionObserver for A2/A3 rather than
  adding a second; bind A1/A9 via event delegation on the rail container, not per-chip listeners.
- **Compositor-only.** Every animated property above is `opacity` or `transform` (plus a `box-shadow`
  one-shot); no `width`/`top`/`left` animation, so the fixed rails never thrash layout on scroll.
- **Fine-pointer gate.** A1 (hovercards) and A5 (magnetic) attach only when
  `matchMedia('(hover:hover) and (pointer:fine)')` matches, so touch users get fast taps with zero
  hover cruft.
- **Zero third-party, zero storage** (A7's cross-visit persistence is the only `[STORAGE]` candidate,
  and it is optional — session-memory by default). Well within the CWV budget the perf critique set.
- **Crawlability guaranteed.** All of A1-A10 are progressive enhancement injected after paint; every
  link they decorate already exists as a static `<a href>`. Turn JS off and the page is identical to
  today's crawlable baseline.

---

### Sources

- Wikipedia Page Previews (650 ms hover-intent, preview-before-click, rabbit-hole): https://diff.wikimedia.org/2018/04/18/how-we-designed-page-previews-for-wikipedia/
- GitHub-style hovercards (typed-entity peek, degrade-to-link build): https://github.com/topics/hovercard ; https://boringrails.com/articles/hovercards-stimulus/
- Magnetic button vanilla technique (0.25 damping, getBoundingClientRect center, 120px radius, .25s ease-out): https://en.inithtml.com/resources/magnetic-hover-effect-creating-cursor-attracted-buttons-with-vanilla-javascript/ ; https://codepen.io/Course-Max-One/pen/QwyjPOg
- View Transitions API (native, progressive, motion-pref aware): https://developer.chrome.com/docs/web-platform/view-transitions/ ; https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using
- prefers-reduced-motion "replace, don't delete": https://www.joshwcomeau.com/react/prefers-reduced-motion/ ; https://www.smashingmagazine.com/2021/10/respecting-users-motion-preferences/
- Micro-interactions raise perceived quality (patterns/examples): https://www.frontendtools.tech/blog/micro-interactions-ui-ux-guide ; https://altersquare.io/micro-interactions-that-actually-improve-user-experience-with-examples/
- Anti-slop guardrail (looping pulse / gratuitous motion as AI-tell): https://www.925studios.co/blog/ai-slop-web-design-guide
- In-repo prior art: `js/enhance.js` (count-up + reveal observer, reduced-motion + fine-pointer guards), `js/engage.js` (rail link harvest, scroll-spy), `css/site.css` (`.engage-*` tokens, `@keyframes fabpulse`).
