# MAT — "Super Cool" Web Design Styles & Trends (2025–2026)

**Purpose:** A visual/art-director scan of current premium web aesthetics that could give MAT (pro-wrestling database — black + championship-gold `#d4af37` + blood-red `#e11d2a`; Anton / Oswald / Inter; static HTML/CSS/vanilla JS, no framework, no build, no browser storage) a distinctive, high-end, memorable identity — with a bias toward the **header / hero / mega-nav**.

**Constraints honored throughout:** every technique below ships as plain HTML + CSS + one optional vanilla-JS listener. No frameworks, no build step, no `localStorage`/`sessionStorage`/cookies. Snippets are copy-ready and use MAT's tokens.

**How to read this:** Part A = 10 distinct named styles (vibe → signature moves → copy-ready CSS → a11y/perf caveats → how it shapes MAT's header/hero). Part B = 3 cohesive "design style packages" that combine several styles into buildable prototype directions. Sources cited inline and listed at the end.

---

## Design tokens (assumed baseline for all snippets)

```css
:root{
  --ink:#0a0a0b;          /* near-black canvas   */
  --ink-2:#141416;        /* raised surface       */
  --gold:#d4af37;         /* championship gold    */
  --blood:#e11d2a;        /* blood red            */
  --paper:#f4f1ea;        /* bone/off-white text  */
  --muted:#9a9aa2;
  --edge:rgba(212,175,55,.22);
  --font-display:"Anton",sans-serif;   /* fight-poster caps */
  --font-head:"Oswald",sans-serif;     /* condensed headers */
  --font-body:"Inter",system-ui,sans-serif;
}
```

---

# PART A — Named styles

## 1. Dark Cinematic / Broadcast

**Vibe.** The house lights are off; a single key light rakes across the champion. This is the default "premium entertainment" register in 2025–26 — dark mode is now a design-system commitment, not a toggle, and delivers measurable engagement (studies cite ~18% longer sessions and OLED battery savings). ([studiomeyer/dev.to](https://dev.to/studiomeyer_io/web-design-trends-2026-what-actually-held-up-after-six-months-23p8))

**Signature visual moves.** True black canvas with layered elevation (never flat `#000` everywhere); a single warm key-light gradient behind the hero subject; cinematic letterboxing (thin top/bottom bars); high-contrast gold/red accents used sparingly like broadcast lower-thirds; vignette to pull the eye center.

**Copy-ready CSS.**
```css
.hero-cinematic{
  position:relative; min-height:82vh; background:var(--ink); overflow:hidden;
  display:grid; place-items:center; isolation:isolate;
}
/* warm key light on the subject */
.hero-cinematic::before{
  content:""; position:absolute; inset:0; z-index:-1;
  background:
    radial-gradient(60% 55% at 50% 38%, rgba(212,175,55,.20), transparent 70%),
    radial-gradient(120% 90% at 50% 120%, rgba(225,29,42,.12), transparent 60%);
}
/* vignette + letterbox */
.hero-cinematic::after{
  content:""; position:absolute; inset:0; z-index:2; pointer-events:none;
  box-shadow:inset 0 0 240px 60px rgba(0,0,0,.9);
  border-top:6px solid #000; border-bottom:6px solid #000;
}
```

**A11y / perf.** Keep body text at ≥ `#c9c9d0` on `--ink` for AA contrast; pure white on pure black causes halation — use `--paper`. Vignettes must not sit over interactive text. No perf cost (pure paint).

**Shapes MAT's header/hero.** Hero = full-bleed champion cutout under a gold key light with a broadcast-style lower-third ("WORLD HEAVYWEIGHT CHAMPION"). Header = slim, dark, letterboxed bar that reads like an on-air chyron.

---

## 2. Bento Grids

**Vibe.** A control panel of self-contained tiles — the structural default now used by Apple, Google, Microsoft, Spotify. Reported ~23% more scroll depth vs. a traditional 12-column grid. ([studiomeyer/dev.to](https://dev.to/studiomeyer_io/web-design-trends-2026-what-actually-held-up-after-six-months-23p8), [Figma](https://www.figma.com/resource-library/web-design-trends/))

**Signature visual moves.** Modular, asymmetric rounded tiles of varying span; each tile one job (featured match, top-ranked, latest title change, trending rivalry); mixed density; consistent gutters; subtle per-tile hover lift.

**Copy-ready CSS.**
```css
.bento{
  display:grid; gap:14px; padding:14px;
  grid-template-columns:repeat(4,1fr); grid-auto-rows:180px;
}
.bento > *{
  background:var(--ink-2); border:1px solid var(--edge); border-radius:18px;
  padding:20px; transition:transform .25s ease, border-color .25s ease;
}
.bento > *:hover{ transform:translateY(-4px); border-color:var(--gold); }
.bento .feature{ grid-column:span 2; grid-row:span 2; }  /* main event */
.bento .wide{ grid-column:span 2; }
@media (max-width:720px){ .bento{ grid-template-columns:repeat(2,1fr); } }
```

**A11y / perf.** Give each tile a real heading and a wrapping `<a>` so it is keyboard-focusable; don't rely on hover-only affordances. Zero perf cost.

**Shapes MAT's header/hero.** The hero itself becomes a bento "command board": one large main-event tile plus satellite tiles for rankings, latest title change, and this-week's card. Mega-nav dropdown panels can reuse the same tile grammar.

---

## 3. Glassmorphism 2.0

**Vibe.** Frosted broadcast glass — depth without weight. Held up in 2026 but **only** for nav bars, modals, and feature cards, not full pages. ([studiomeyer/dev.to](https://dev.to/studiomeyer_io/web-design-trends-2026-what-actually-held-up-after-six-months-23p8), [Figma](https://www.figma.com/resource-library/web-design-trends/))

**Signature visual moves.** `backdrop-filter: blur()` panels; hairline gold border + faint inner highlight; slight translucency so the dark canvas and hero glow bleed through.

**Copy-ready CSS.**
```css
.glass{
  background:rgba(20,20,22,.55);
  -webkit-backdrop-filter:blur(14px) saturate(120%);
  backdrop-filter:blur(14px) saturate(120%);
  border:1px solid rgba(212,175,55,.28);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.06), 0 8px 30px rgba(0,0,0,.5);
  border-radius:14px;
}
@supports not (backdrop-filter:blur(4px)){ .glass{ background:rgba(18,18,20,.92); } }
```

**A11y / perf.** Real cost: measured **15–30% FPS drops** on mid-tier Android — never blur a large or scrolling surface. Restrict to the sticky nav and modals; always ship the `@supports` opaque fallback for contrast. ([studiomeyer/dev.to](https://dev.to/studiomeyer_io/web-design-trends-2026-what-actually-held-up-after-six-months-23p8))

**Shapes MAT's header/hero.** The sticky top nav is a single frosted-glass bar floating over the cinematic hero — the champion glow reads faintly through it. Mega-nav panel = one frosted sheet.

---

## 4. Kinetic / Oversized Editorial Typography

**Vibe.** The wordmark *is* the graphic — fight-poster scale, letters that move. Bold/oversized type and variable fonts are a leading 2026 trend; kinetic type is powerful but overpromised in production. ([Figma](https://www.figma.com/resource-library/web-design-trends/), [envato](https://elements.envato.com/learn/web-design-trends), [studiomeyer/dev.to](https://dev.to/studiomeyer_io/web-design-trends-2026-what-actually-held-up-after-six-months-23p8))

**Signature visual moves.** `clamp()`-scaled display type filling the viewport; tight tracking; type layered over/behind the subject; a gold text-clip gradient; restrained motion (weight shift or slow reveal), not constant animation.

**Copy-ready CSS.**
```css
.kinetic{
  font-family:var(--font-display); line-height:.86; letter-spacing:-.02em;
  font-size:clamp(3rem,13vw,11rem); text-transform:uppercase;
  background:linear-gradient(180deg,var(--paper),var(--gold));
  -webkit-background-clip:text; background-clip:text; color:transparent;
}
.kinetic span{ display:inline-block; animation:rise .8s cubic-bezier(.2,.7,.2,1) both; }
.kinetic span:nth-child(2){ animation-delay:.08s; }
@keyframes rise{ from{ transform:translateY(.35em); opacity:0 } to{ transform:none; opacity:1 } }
@media (prefers-reduced-motion:reduce){ .kinetic span{ animation:none } }
```

**A11y / perf.** Kinetic type "fights screen readers, fights crawlers, and adds layout shift" — keep the accessible text in real DOM, animate transforms only, and **always** honor `prefers-reduced-motion`. Reserve space to avoid CLS. ([studiomeyer/dev.to](https://dev.to/studiomeyer_io/web-design-trends-2026-what-actually-held-up-after-six-months-23p8))

**Shapes MAT's header/hero.** Hero headline = "MAT" or the event name at 11rem, gold-clipped, letters rising once on load, with the champion cutout punching through the descenders.

---

## 5. Neo-Brutalist Accents

**Vibe.** Raw, loud, honest — hard edges and offset shadows as a counter-move to smooth bento sameness. Best used as **accents**, not whole-page. ([setproduct](https://www.setproduct.com/blog/retro-brutalist-ui-design-2026), [Figma](https://www.figma.com/resource-library/web-design-trends/))

**Signature visual moves.** Hard 2px borders, zero radius, sharp offset shadows (no blur), monospace labels, stark limited palette, intentional asymmetry. ([setproduct](https://www.setproduct.com/blog/retro-brutalist-ui-design-2026))

**Copy-ready CSS.**
```css
.brutal{
  background:var(--ink); color:var(--paper);
  border:2px solid var(--paper); border-radius:0;
  box-shadow:8px 8px 0 var(--gold);
  font-family:"Departure Mono",ui-monospace,monospace;
  padding:12px 18px; text-transform:uppercase; letter-spacing:.04em;
}
.brutal--danger{ box-shadow:8px 8px 0 var(--blood); border-color:var(--blood); }
.brutal:hover{ box-shadow:4px 4px 0 var(--gold); transform:translate(4px,4px); }
```

**A11y / perf.** Keep hit areas ≥44px and contrast high (brutalism actually helps contrast). Avoid `-webkit-font-smoothing:none` on body copy — crispness at display sizes only. Zero perf cost.

**Shapes MAT's header/hero.** Use for high-energy accents: a blood-red "LIVE" / "TITLE CHANGE" tag with hard offset shadow, monospace stat chips (record, reign length) under the hero, and blocky mega-nav category labels.

---

## 6. "Command Center" / HUD / Sports-Broadcast Overlay

**Vibe.** You're in the production truck — telemetry, tale-of-the-tape, live tickers, corner brackets. Draws on esports/broadcast HUD language (redesigned LoL/MSI overlays, sports lower-thirds) and the 2026 "technical mono / surveillance" aesthetic. ([LoL Esports HUD](https://x.com/lolesports/status/1934989910521380916), [aigoodies/Medium](https://medium.com/design-bootcamp/aesthetics-in-the-ai-era-visual-web-design-trends-for-2026-5a0f75a10e98))

**Signature visual moves.** Corner-bracket frames; monospace data readouts with labels; thin scan-lines; "REC ●" / "LIVE" indicators; tale-of-the-tape stat columns; gridlines and tick marks; gold/red status colors.

**Copy-ready CSS.**
```css
.hud{ position:relative; padding:22px; font-family:ui-monospace,monospace; color:var(--paper); }
.hud::before,.hud::after{
  content:""; position:absolute; width:26px; height:26px; border:2px solid var(--gold);
}
.hud::before{ top:8px; left:8px; border-right:0; border-bottom:0; }
.hud::after{ bottom:8px; right:8px; border-left:0; border-top:0; }
.hud .live{ color:var(--blood); font-weight:700; letter-spacing:.1em; }
.hud .live::before{ content:"● "; animation:blink 1.4s steps(2,start) infinite; }
.hud .scan{ position:absolute; inset:0; pointer-events:none;
  background:repeating-linear-gradient(0deg,transparent 0 3px,rgba(255,255,255,.03) 3px 4px); }
@keyframes blink{ 50%{ opacity:.25 } }
@media (prefers-reduced-motion:reduce){ .hud .live::before{ animation:none } }
```

**A11y / perf.** Monospace tickers are noisy for screen readers — mark decorative HUD chrome `aria-hidden` and keep the real data in a semantic table. Keep scan-line opacity ≤ .04 to avoid a moiré flicker. Cheap to render.

**Shapes MAT's header/hero.** Hero = tale-of-the-tape for the featured match (two wrestlers, HUD stat columns, corner brackets, blinking "LIVE/RESULT"). Header = a broadcast status strip. This is MAT's most *ownable* register — few wrestling DBs commit to it.

---

## 7. Grain / Texture

**Vibe.** Analog imperfection — film grain and noise signal authenticity and human presence against sterile AI-smoothness ("embrace of imperfection" is a defining 2026 theme). ([aigoodies/Medium](https://medium.com/design-bootcamp/aesthetics-in-the-ai-era-visual-web-design-trends-for-2026-5a0f75a10e98))

**Signature visual moves.** A subtle noise layer over dark gradients (kills banding on OLED); grain intensifies richness of gold; paired with gradient-mesh for a "grainy gradient."

**Copy-ready CSS (inline SVG `feTurbulence`, no image asset).**
```css
.grain::after{
  content:""; position:fixed; inset:0; z-index:9999; pointer-events:none;
  opacity:.05; mix-blend-mode:overlay;
  background-image:url("data:image/svg+xml,\
%3Csvg xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E\
%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='2'/%3E\
%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
```

**A11y / perf.** `feTurbulence` is GPU-cheap as a static tile; keep `opacity ≤ .06` so it never lowers text contrast. Do **not** animate grain (repaints are expensive and can trigger motion sensitivity). ([Frontend Masters — Grainy Gradients](https://frontendmasters.com/blog/grainy-gradients/))

**Shapes MAT's header/hero.** A single fixed grain layer over the whole hero unifies the champion cutout, gold glow, and type into one filmic plane — the difference between "flat dark theme" and "premium."

---

## 8. Gradient-Mesh

**Vibe.** Soft, dimensional colored light — the modern replacement for flat brand color, giving the dark canvas depth and a "lit arena" glow. ([Figma](https://www.figma.com/resource-library/web-design-trends/), [aigoodies/Medium](https://medium.com/design-bootcamp/aesthetics-in-the-ai-era-visual-web-design-trends-for-2026-5a0f75a10e98))

**Signature visual moves.** Multiple overlapping radial gradients at different positions to fake a mesh; low-saturation on dark; best when grain is layered on top to prevent banding.

**Copy-ready CSS (pure CSS, no `<canvas>`).**
```css
.mesh{
  background:
    radial-gradient(40% 40% at 15% 20%, rgba(212,175,55,.28), transparent 60%),
    radial-gradient(45% 45% at 85% 15%, rgba(225,29,42,.22), transparent 60%),
    radial-gradient(60% 60% at 70% 90%, rgba(212,175,55,.14), transparent 65%),
    var(--ink);
}
/* optional very slow drift */
@media (prefers-reduced-motion:no-preference){
  .mesh{ background-size:200% 200%; animation:drift 24s ease-in-out infinite alternate; }
}
@keyframes drift{ to{ background-position:100% 100% } }
```

**A11y / perf.** CSS radial-gradient mesh is far cheaper than a WebGL/Spline mesh (a single Spline scene loads 800KB–2MB of JS and collapses Lighthouse). Keep the drift slow and gated behind `prefers-reduced-motion`. Layer `.grain` on top to kill 8-bit banding. ([studiomeyer/dev.to](https://dev.to/studiomeyer_io/web-design-trends-2026-what-actually-held-up-after-six-months-23p8))

**Shapes MAT's header/hero.** The hero backdrop: gold and blood-red light pools behind the champion, drifting almost imperceptibly — reads as arena lighting, not a "gradient."

---

## 9. Marquee / Ticker Motion

**Vibe.** ESPN bottom-line energy — a constantly moving results/rumors crawl signals "live, always-updating database." Motion design and scroll-based narrative are core 2026 trends. ([Figma](https://www.figma.com/resource-library/web-design-trends/), [envato](https://elements.envato.com/learn/web-design-trends))

**Signature visual moves.** Horizontal infinite crawl of latest results/title changes; oversized display-type marquee as a hero band; pause-on-hover; gold separators between items.

**Copy-ready CSS (transform-based, GPU-friendly, duplicate the content for seamless loop).**
```css
.ticker{ overflow:hidden; border-block:1px solid var(--edge); background:var(--ink-2); }
.ticker__track{ display:inline-flex; gap:2.5rem; white-space:nowrap;
  padding:.6rem 0; will-change:transform; animation:crawl 30s linear infinite; }
.ticker:hover .ticker__track{ animation-play-state:paused; }
.ticker__item{ font-family:var(--font-head); text-transform:uppercase; letter-spacing:.04em; }
.ticker__item b{ color:var(--gold); }  .ticker__item .win{ color:var(--blood); }
@keyframes crawl{ to{ transform:translateX(-50%) } }  /* -50% because content is duplicated */
@media (prefers-reduced-motion:reduce){ .ticker__track{ animation:none; overflow-x:auto } }
```

**A11y / perf.** Animate `transform` only (not `left`/`margin`) to stay on the compositor. Provide pause-on-hover **and** a reduced-motion fallback that becomes a scrollable strip. Duplicate items visually but hide the dupes with `aria-hidden` so screen readers hear the list once.

**Shapes MAT's header/hero.** A thin results ticker sits directly under the sticky nav ("● LIVE RESULTS"), plus an optional giant single-line marquee of legendary names as a hero texture band.

---

## 10. Hover-Reactive Spotlight

**Vibe.** The cursor becomes a stage light — cards and the hero "illuminate" where the pointer goes. Interactive hover/micro-motion is a headline 2026 trend and a cheap way to feel bespoke. ([Figma](https://www.figma.com/resource-library/web-design-trends/))

**Signature visual moves.** A radial-gradient that follows the mouse via a CSS custom property updated by one `pointermove` listener; gold glow on dark; often paired with bento tiles (spotlight border reveal).

**Copy-ready CSS + minimal vanilla JS.**
```css
.spotlight{ position:relative; background:var(--ink-2); border:1px solid var(--edge);
  border-radius:16px; overflow:hidden; }
.spotlight::before{
  content:""; position:absolute; inset:0; pointer-events:none; transition:opacity .3s;
  opacity:0; background:radial-gradient(240px circle at var(--mx) var(--my),
    rgba(212,175,55,.18), transparent 60%); }
.spotlight:hover::before{ opacity:1; }
```
```html
<script>
  document.querySelectorAll('.spotlight').forEach(el=>{
    el.addEventListener('pointermove',e=>{
      const r=el.getBoundingClientRect();
      el.style.setProperty('--mx',(e.clientX-r.left)+'px');
      el.style.setProperty('--my',(e.clientY-r.top)+'px');
    });
  });
</script>
```

**A11y / perf.** Pure decoration — must never gate content behind hover; touch devices simply won't see it (fine). Throttle isn't needed for a `setProperty` on `pointermove`, but avoid layout-triggering reads in the handler (the `getBoundingClientRect` is cheap here). No `prefers-reduced-motion` concern (no keyframes), but respect it if you add easing.

**Shapes MAT's header/hero.** Every bento tile and mega-nav card glows gold under the cursor; the hero champion portrait gets a spotlight that tracks the mouse, making the whole header feel physically lit.

---

# PART B — Three cohesive design style packages

Each package bundles a few Part-A styles into a coherent, buildable direction for a distinct homepage + mega-nav prototype. All stay within static HTML/CSS/vanilla-JS and MAT's tokens.

---

## Package 1 — "MAIN EVENT" (Dark Cinematic Broadcast)
**Combines:** Dark Cinematic (#1) + Gradient-Mesh (#8) + Grain (#7) + Kinetic Editorial Type (#4) + Glass nav (#3).

**Direction.** The most *premium/theatrical* option. The homepage is a lit arena: drifting gold/red mesh behind a full-bleed champion cutout, a single fixed film-grain plane over everything, an 11rem gold-clipped headline rising on load, and a frosted-glass sticky nav floating on top. Feels like a pay-per-view intro.

**Header/hero.** Letterboxed cinematic hero + key-light glow; glass mega-nav whose dropdown panels are frosted sheets; headline is the event/wordmark at poster scale.

**Why it wins / risks.** Highest "wow," lowest novelty risk (all held-up trends). Watch glass FPS on mobile (limit blur to the nav bar) and CLS on the kinetic headline (reserve space, reduced-motion fallback).

---

## Package 2 — "PRODUCTION TRUCK" (Sports-Broadcast HUD)
**Combines:** Command-Center/HUD (#6) + Marquee/Ticker (#9) + Bento (#2) + Neo-Brutalist mono accents (#5).

**Direction.** The most *distinctive and ownable* option — leans into the thing wrestling sites rarely commit to: a live-broadcast control room. Corner-bracket HUD frames, monospace telemetry, a "● LIVE RESULTS" crawl under the nav, and a bento command-board of stat tiles. Blood-red status tags with hard offset shadows.

**Header/hero.** Hero = tale-of-the-tape HUD for the featured match (two competitors, stat columns, corner brackets, blinking status). Header = broadcast status strip + results ticker. Mega-nav categories rendered as blocky monospace labels.

**Why it wins / risks.** Maximum differentiation and "data authority" — perfect for a *database*. Risks: monospace/ticker noise for screen readers (mark chrome `aria-hidden`, keep real data in semantic tables), and don't let brutalist mono creep into long body copy.

---

## Package 3 — "GOLD STANDARD" (Modern Editorial Command Board)
**Combines:** Bento (#2) + Hover-Reactive Spotlight (#10) + Gradient-Mesh (#8) + restrained Kinetic Type (#4) + Grain (#7).

**Direction.** The most *balanced, conversion-friendly* option — a clean, modern, tactile editorial grid that still feels alive. A bento command board of rankings/matches/rivalries where every tile lights up gold under the cursor, sitting on a soft mesh + grain canvas, topped by one oversized (but calm) headline. The "Apple-keynote-for-wrestling" register.

**Header/hero.** Hero is itself a bento board (large main-event tile + satellites) with spotlight-reactive tiles; a simple dark nav (optionally glass); headline present but secondary to the grid. Mega-nav dropdowns reuse the bento tile grammar with spotlight glow.

**Why it wins / risks.** Best scroll-depth and scannability (bento's measured ~23% lift), easiest to keep accessible and fast, most future-proof. Risk: least "loud" — lean on grain + spotlight + a strong hero tile so it doesn't read generic.

---

## Cross-cutting rules (apply to all packages)
- **Motion:** every animation (kinetic type, mesh drift, ticker, blink) must have a `@media (prefers-reduced-motion:reduce)` off-switch. ([studiomeyer/dev.to](https://dev.to/studiomeyer_io/web-design-trends-2026-what-actually-held-up-after-six-months-23p8))
- **Contrast:** body text `--paper`/`#c9c9d0` on `--ink`, never pure white on pure black (halation). Gold `#d4af37` passes AA on `--ink` for large text only — don't use it for small body copy.
- **Perf budget:** prefer CSS gradients over WebGL/Spline (800KB–2MB JS kills Core Web Vitals); blur only the nav; grain as a single static SVG tile; animate `transform`/`opacity` only. ([studiomeyer/dev.to](https://dev.to/studiomeyer_io/web-design-trends-2026-what-actually-held-up-after-six-months-23p8))
- **Semantics first:** decorative HUD/marquee chrome `aria-hidden`; real data in headings, links, and tables so keyboard + screen-reader users and crawlers get everything.
- **No storage:** none of the above requires `localStorage`/cookies; theme is dark-native so no persisted toggle is needed.

---

## Sources
- studiomeyer — *Web Design Trends 2026: What Actually Held Up After Six Months* (dev.to): https://dev.to/studiomeyer_io/web-design-trends-2026-what-actually-held-up-after-six-months-23p8
- Figma — *Top Web Design Trends for 2026*: https://www.figma.com/resource-library/web-design-trends/
- Ioana Teleanu / Bootcamp (Medium) — *Aesthetics in the AI Era: Visual + Web Design Trends for 2026*: https://medium.com/design-bootcamp/aesthetics-in-the-ai-era-visual-web-design-trends-for-2026-5a0f75a10e98
- Setproduct — *Retro & Brutalist UI Design: a 2026 Field Guide*: https://www.setproduct.com/blog/retro-brutalist-ui-design-2026
- Envato Elements — *Web design trends for 2026: kinetic type, broken grids and the return of visual personality*: https://elements.envato.com/learn/web-design-trends
- Frontend Masters — *Grainy Gradients*: https://frontendmasters.com/blog/grainy-gradients/
- LoL Esports — *MSI 2025 broadcast HUD redesign* (X): https://x.com/lolesports/status/1934989910521380916
```