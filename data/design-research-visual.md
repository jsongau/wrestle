# Premium Visual Design Research — MAT (Pro-Wrestling Database + Membership)

> **Goal:** Make a dark "arena"-themed sports/entertainment site look **expensive and non-generic** *without any licensed photography*. Every technique below is synthesized from award-winning sports/entertainment sites and design galleries, then rewritten as **original, copy-ready CSS/HTML** that drops straight into this codebase.
>
> **Constraints honored:** No framework, no build step, no browser storage, plain HTML/CSS/vanilla JS. All snippets use the tokens already defined in `/css/site.css` (`--c-bg`, `--c-gold`, `--c-red`, `--font-cond`, `--ease`, etc.) so they paste in without redefinition.
>
> **What was studied (for technique synthesis only — no code/assets copied):** Awwwards sports & dark-mode collections, CSS Design Awards sport gallery, SiteInspire, Lapa Ninja, Land-book, Godly.website; and the visual language of UFC.com, ESPN, DAZN, The Athletic, Bleacher Report, Sherdog, Tapology, F1.com, NBA.com, and Nike/Jordan. Technique sources are cited inline and listed at the end.

---

## 0. The five things that separate "expensive" from "generic"

Distilled from studying the reference set. When a photo-less site looks cheap, it is almost always failing one of these:

1. **Depth via layers, never flat fills.** Premium dark UIs stack 3–5 translucent layers (base → radial glow → mesh → grain → vignette). A single `background:#0a0b0d` reads as "unfinished." (Awwwards dark-mode collection; DAZN, F1.com hero treatments.)
2. **One loud gesture per screen.** Oversized condensed type OR one animated gradient OR one angled break — not all three fighting. UFC/Nike restraint.
3. **Accent discipline.** Gold and red are *events*, not surfaces. ~90% neutral, ~8% one accent, ~2% the second. (The Athletic, Sherdog editorial restraint.)
4. **Texture kills the "vector-art" look.** A 3–5% grain overlay makes gradients read as film/print instead of default CSS. (CSS-Tricks *Grainy Gradients*; Codrops *feTurbulence*.)
5. **Motion that responds, not loops.** Pointer-driven spotlights and parallax feel bespoke; infinite keyframe loops feel like a template. (Awwwards interaction trend.)

---

## 1. HERO — drama without a single photograph

The hero is where "no photography" is won or lost. The strategy: **build the drama out of light and type, then texture it so it never looks like flat CSS.**

### 1.1 Layered "arena spotlight" background (the core technique)

Stack, from back to front: base black → two off-center radial glows (gold + red) → a subtle conic sweep → grain → a vignette that darkens the edges and pushes the eye to center. This is the single highest-impact snippet in this doc.

```html
<section class="hero">
  <div class="hero__bg" aria-hidden="true"></div>
  <div class="hero__grain" aria-hidden="true"></div>
  <div class="wrap hero__inner">
    <p class="eyebrow">The Ultimate Pro-Wrestling Database</p>
    <h1 class="hero__title">EVERY RIVALRY.<br>EVERY&nbsp;MATCH.<br><span class="hero__accent">EVERY LEGEND.</span></h1>
    <p class="hero__lede">Four decades of storylines, five-star matches, and the feuds that defined an era — indexed, ranked, and remembered.</p>
    <div class="cluster">
      <a class="btn btn--gold" href="/wrestlers/">Explore the Roster</a>
      <a class="btn btn--ghost" href="/membership/">Join MAT Insider</a>
    </div>
  </div>
</section>
```

```css
.hero{position:relative;isolation:isolate;overflow:hidden;
  min-height:clamp(560px,88vh,900px);display:grid;align-items:center;}

/* Layer 1+2+3: base black, two spotlights, a cool conic sweep for "stage light" */
.hero__bg{position:absolute;inset:0;z-index:-2;
  background:
    radial-gradient(60% 80% at 18% 12%, rgba(212,175,55,.22), transparent 60%),
    radial-gradient(50% 70% at 88% 90%, rgba(225,29,42,.20), transparent 55%),
    conic-gradient(from 210deg at 50% -10%, #14161b, #0a0b0d 40%, #101217 70%, #0a0b0d);
}
/* Layer 4: vignette — darkens edges, focuses center (studied on F1/DAZN heroes) */
.hero::after{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;
  background:radial-gradient(120% 120% at 50% 40%, transparent 55%, rgba(0,0,0,.55) 100%);
}
```

The grain layer (`.hero__grain`) is defined in §5.1 — add it and the hero instantly stops looking like default CSS.

**Why it reads premium:** two off-axis light sources create implied 3D depth; the conic sweep mimics a stage-light gradient; the vignette is the classic cinematic focus trick. Synthesized from Awwwards dark-mode heroes and F1.com/DAZN broadcast-style backgrounds.

### 1.2 Animated mesh gradient (opt-in, GPU-cheap, reduced-motion safe)

Slow-drifting blobs give life without video. Animate `background-position` on a fixed-size multi-radial background — cheaper and smoother than animating the gradient stops themselves.

```css
.hero--animated .hero__bg{
  background-size:180% 180%, 200% 200%, 100% 100%;
  animation:heroDrift 24s ease-in-out infinite alternate;
}
@keyframes heroDrift{
  0%{background-position:0% 0%, 100% 100%, 0 0;}
  100%{background-position:30% 20%, 70% 80%, 0 0;}
}
@media (prefers-reduced-motion:reduce){ .hero--animated .hero__bg{animation:none;} }
```

Keep it ≥20s and `ease-in-out` — fast mesh motion is the #1 tell of a template. (Awwwards gradient trend; the site already ships a global `prefers-reduced-motion` reset so this degrades correctly.)

### 1.3 Oversized condensed type with a "printed" gradient fill

Big condensed caps are the signature of UFC/Nike/Bleacher hero type. Push `--font-cond` (Oswald) far larger than the token scale, tighten tracking, and give ONE line a metallic gold gradient via `background-clip:text`.

```css
.hero__title{
  font-family:var(--font-cond);text-transform:uppercase;font-weight:700;
  font-size:clamp(2.8rem,7vw + 1rem,7.5rem);
  line-height:.92;letter-spacing:-.01em;text-wrap:balance;
  /* faint outline glow lifts white type off the dark bg */
  text-shadow:0 1px 0 rgba(255,255,255,.06),0 20px 60px rgba(0,0,0,.6);
}
.hero__accent{
  background:linear-gradient(180deg,#f7e08a 0%,var(--c-gold) 45%,var(--c-gold-dim) 100%);
  -webkit-background-clip:text;background-clip:text;color:transparent;
  /* subtle top highlight = "brushed metal" championship feel */
  filter:drop-shadow(0 2px 10px rgba(212,175,55,.25));
}
.hero__lede{max-width:52ch;color:var(--c-text-muted);font-size:var(--fs-500);margin-top:var(--sp-4);}
```

**Pro move (kinetic energy):** set the second line in outline-only text so the eye reads it as a "shout." Works great for a rotating tagline.

```css
.hero__title .stroke{
  color:transparent;-webkit-text-stroke:1.5px rgba(232,234,237,.55);
}
```

### 1.4 Diagonal "impact" clip on the hero base

A single angled bottom edge gives the hero forward momentum (fight-poster energy). Pair with the section below sliding under it.

```css
.hero{clip-path:polygon(0 0,100% 0,100% calc(100% - 4vw),0 100%);}
/* pull the next section up so its content tucks into the notch */
.hero + .section{margin-top:-2vw;padding-top:calc(var(--sp-8) + 2vw);}
```

Keep the angle shallow (3–5vw). Steep angles clip text on mobile — see §4.1 for the responsive-safe pattern. (CSS-Tricks *Create Diagonal Layouts*; Viget *Angled Edges*.)

### 1.5 Pointer-parallax glow (bespoke feel, ~10 lines of JS)

The hero light follows the cursor slightly. This is the difference between "designed" and "generated." Vanilla, throttled with `requestAnimationFrame`, and inert under reduced-motion.

```js
// hero-parallax.js — add <script src="/js/hero-parallax.js" defer></script>
(() => {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const hero = document.querySelector('.hero'); if (!hero) return;
  let raf = 0, tx = 0, ty = 0;
  hero.addEventListener('pointermove', (e) => {
    const r = hero.getBoundingClientRect();
    tx = (e.clientX - r.left) / r.width - 0.5;   // -0.5 .. 0.5
    ty = (e.clientY - r.top) / r.height - 0.5;
    if (!raf) raf = requestAnimationFrame(apply);
  });
  hero.addEventListener('pointerleave', () => { tx = ty = 0; if (!raf) raf = requestAnimationFrame(apply); });
  function apply(){ raf = 0;
    hero.style.setProperty('--px', (tx * 18).toFixed(2) + 'px');
    hero.style.setProperty('--py', (ty * 18).toFixed(2) + 'px');
  }
})();
```

```css
.hero__bg{transition:transform .3s var(--ease);
  transform:translate3d(var(--px,0),var(--py,0),0) scale(1.06); /* scale prevents edge gaps */
}
```

Technique synthesized from Awwwards pointer-reactive heroes and the CSS-custom-property spotlight pattern (Frontend Masters / Cruip).

---

## 2. COLOR & LIGHT — black + championship-gold + blood-red, layered

The palette is already tokenized (`--c-gold #d4af37`, `--c-red #e11d2a`, neutrals `#0a0b0d → #23272f`). The upgrade is in **how** they're used: as light and gradient, never as flat fills.

### 2.1 The 90/8/2 accent rule

- **~90% neutral** surfaces (`--c-bg`, `--c-bg-elev-1/2/3`).
- **~8% gold** — one hero line, primary CTAs, active nav, championship/stat highlights.
- **~2% red** — live badges, destructive/urgent, one hover state. Red is the "blood"; scarcity is what makes it read as danger.

Never place large gold and large red adjacent at full saturation — they vibrate. Separate them with neutral space or let one be a glow, the other a fill. (The Athletic / Sherdog editorial discipline.)

### 2.2 Metallic gold instead of flat gold

Flat `#d4af37` looks like a swatch. A 3-stop vertical gradient reads as *metal* (light hits the top, shadow pools at the bottom). Use for medals, championship pills, award tiles.

```css
.gold-metal{
  background:linear-gradient(180deg,#f7e08a 0%,#e8c34a 30%,var(--c-gold) 55%,var(--c-gold-dim) 100%);
  color:#1a1400;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.5), inset 0 -2px 6px rgba(0,0,0,.25),
             0 4px 14px rgba(212,175,55,.25);
}
```

### 2.3 Glows do the work fills can't

A colored `box-shadow`/blur behind an element implies a light source. Reserve gold glow for "premium/earned" and red glow for "live/urgent."

```css
:root{
  --glow-gold:0 0 0 1px var(--c-gold-dim), 0 8px 30px rgba(212,175,55,.22);
  --glow-red: 0 0 0 1px var(--c-red-dim),  0 8px 30px rgba(225,29,42,.25);
}
.badge--live{color:#fff;background:linear-gradient(180deg,var(--c-red-bright),var(--c-red));
  box-shadow:var(--glow-red);}
.badge--live::before{content:"";width:.5em;height:.5em;border-radius:50%;background:#fff;
  box-shadow:0 0 8px #fff;animation:pulse 1.6s var(--ease) infinite;}
@keyframes pulse{0%,100%{opacity:1;}50%{opacity:.35;}}
```

### 2.4 Duotone tint layer for any surface (the photo-substitute)

A gold- or red-tinted radial over an elevated surface gives "brand light" cheaply. Great for section backgrounds and empty states.

```css
.tint-gold{position:relative;isolation:isolate;background:var(--c-bg-elev-1);}
.tint-gold::before{content:"";position:absolute;inset:0;z-index:-1;
  background:radial-gradient(80% 120% at 100% 0%, var(--c-gold-tint), transparent 60%);}
```

### 2.5 Gradient text & rules for hierarchy

Use a hairline gradient rule (gold fading to nothing) instead of a flat `--c-line` divider under section titles — it signals "premium editorial."

```css
.rule-gold{height:2px;border:0;width:min(120px,30%);
  background:linear-gradient(90deg,var(--c-gold),transparent);}
```

---

## 3. CARDS & TILES — premium treatments for a photo-less roster

Cards are 80% of a database site's surface area. These make placeholder tiles look **intentional**, not "missing image."

### 3.1 Duotone / initial-based placeholder that looks designed

Instead of a gray box, generate a **deterministic duotone gradient + oversized monogram** per wrestler. Looks like a curated poster, needs zero assets. Vary the angle/hue per card with an inline `--seed` custom property (set once in HTML from the name's first letter, or just hardcode per entry).

```html
<a class="tile" href="/wrestlers/the-undertaker/" style="--seed:277">
  <div class="tile__media" aria-hidden="true"><span class="tile__mono">U</span></div>
  <div class="tile__body">
    <p class="tile__kicker">The Phenom</p>
    <h3 class="tile__name">The Undertaker</h3>
  </div>
</a>
```

```css
.tile__media{
  position:relative;aspect-ratio:3/4;overflow:hidden;border-radius:var(--r-md);
  /* duotone: dark base -> accent, angle driven by --seed for variety */
  background:
    linear-gradient(calc(var(--seed,220) * 1deg),
      color-mix(in oklab, var(--c-red) 55%, #000) 0%,
      #0c0d10 55%),
    var(--c-bg-elev-2);
}
/* faint diagonal "field lines" pattern so the flat area has texture */
.tile__media::after{content:"";position:absolute;inset:0;opacity:.10;
  background:repeating-linear-gradient(115deg,#fff 0 1px,transparent 1px 9px);
  mix-blend-mode:overlay;}
.tile__mono{
  position:absolute;inset:auto -.08em -.22em auto;font-family:var(--font-cond);
  font-size:11rem;line-height:1;font-weight:700;color:rgba(255,255,255,.06);
  -webkit-text-stroke:1px rgba(255,255,255,.10);pointer-events:none;}
```

Swap `--c-red` for `--c-gold` on legends/champions to signal status through color alone. Duotone-via-gradient technique from CSS-Tricks blend-mode / duotone articles, adapted to gradients so it needs no image.

### 3.2 Gradient border (the "premium card" signal)

A hairline gradient border is the most reliable "this is expensive" cue. Do it with a `border` + `mask` composite so the fill stays dark and only the 1px edge is gradient — no wrapper element.

```css
.card--edge{position:relative;background:var(--c-bg-elev-1);border-radius:var(--r-lg);
  border:1px solid transparent;}
.card--edge::before{content:"";position:absolute;inset:0;border-radius:inherit;padding:1px;
  background:linear-gradient(140deg,var(--c-gold),transparent 40%,transparent 60%,var(--c-red));
  /* show only the border ring */
  -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite:xor;mask-composite:exclude;
  opacity:.5;transition:opacity var(--dur) var(--ease);}
.card--edge:hover::before{opacity:1;}
```

(Gradient-border-via-mask technique: CSS-Tricks masks guide; widely used on Awwwards dark cards.)

### 3.3 Hover elevation — lift, don't just recolor

Premium hover = the card physically rises: small `translateY`, deeper shadow, border warms. Keep it fast (`--dur`) and spring-eased (`--ease`).

```css
.tile{display:block;background:var(--c-bg-elev-1);border:1px solid var(--c-line);
  border-radius:var(--r-lg);overflow:hidden;
  transition:transform var(--dur) var(--ease),box-shadow var(--dur) var(--ease),border-color var(--dur) var(--ease);}
.tile:hover{transform:translateY(-4px);border-color:var(--c-line-strong);
  box-shadow:var(--shadow-2),0 0 0 1px var(--c-gold-dim);}
.tile:hover .tile__mono{color:rgba(212,175,55,.14);transition:color var(--dur) var(--ease);}
```

### 3.4 Pointer spotlight on cards (grid-wide, one listener)

A radial glow that tracks the cursor across a card grid. This is the marquee "bespoke" interaction — one delegated listener drives the whole grid via `--mx`/`--my` custom properties.

```css
.spot{position:relative;isolation:isolate;}
.spot::before{content:"";position:absolute;inset:0;z-index:1;pointer-events:none;
  border-radius:inherit;opacity:0;transition:opacity .25s var(--ease);
  background:radial-gradient(240px circle at var(--mx,50%) var(--my,50%),
            rgba(212,175,55,.16),transparent 60%);}
.spot:hover::before{opacity:1;}
```

```js
// card-spotlight.js — one listener for the whole grid (event delegation)
(() => {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const grid = document.querySelector('.grid-spot'); if (!grid) return;
  grid.addEventListener('pointermove', (e) => {
    const card = e.target.closest('.spot'); if (!card) return;
    const r = card.getBoundingClientRect();
    card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
    card.style.setProperty('--my', (e.clientY - r.top) + 'px');
  });
})();
```

Technique from Cruip / Frontend Masters spotlight patterns, reduced to vanilla + delegation for this no-build site.

### 3.5 Featured "poster" card (asymmetric, editorial)

For a hero match or headliner, break the grid: one wide card with the monogram bleeding off-edge and metadata bottom-left, like a fight poster.

```css
.poster{grid-column:span 2;aspect-ratio:16/9;position:relative;overflow:hidden;
  border-radius:var(--r-lg);background:
    radial-gradient(70% 100% at 80% 20%,var(--c-red-tint),transparent 60%),var(--c-bg-elev-2);}
.poster .tile__mono{font-size:22rem;inset:auto -3rem -6rem auto;}
.poster__meta{position:absolute;left:var(--sp-5);bottom:var(--sp-5);z-index:2;}
```

---

## 4. SECTION RHYTHM, DIVIDERS & LAYOUT

Generic sites are a stack of identical centered boxes. Premium sites vary **rhythm, alignment, and edges.**

### 4.1 Angled section break (responsive-safe)

`clip-path` angles are crisp but can clip content on narrow screens. Safe pattern: use a shallow angle expressed in `vw` on the *container*, and flatten it on mobile.

```css
.section--angle{position:relative;
  clip-path:polygon(0 0,100% 0,100% 100%,0 calc(100% - 3.5vw));
  padding-bottom:calc(var(--sp-8) + 3.5vw);}
@media (max-width:640px){ .section--angle{clip-path:none;} } /* flatten on mobile */
```

For a two-tone angled seam without clipping the box model, use an absolutely-positioned skewed pseudo-element instead:

```css
.seam{position:relative;background:var(--c-bg);}
.seam::before{content:"";position:absolute;top:-4vw;left:0;right:0;height:8vw;
  background:var(--c-bg-elev-1);transform:skewY(-2.2deg);transform-origin:0;z-index:-1;}
```

(CSS-Tricks *Diagonal Layouts*; Viget *Angled Edges with Masks and Transforms*.)

### 4.2 Sticky sub-header / section nav

A slim sticky bar that gains a background + shadow only after scroll = "app-grade." Detect scroll with a tiny listener toggling a class (no storage).

```css
.subnav{position:sticky;top:0;z-index:40;backdrop-filter:blur(8px);
  background:color-mix(in srgb,var(--c-bg) 70%,transparent);
  border-bottom:1px solid transparent;transition:border-color var(--dur),box-shadow var(--dur);}
.subnav.is-stuck{border-color:var(--c-line);box-shadow:var(--shadow-1);}
```

```js
// sticky-shadow.js
(() => { const el=document.querySelector('.subnav'); if(!el) return;
  const io=new IntersectionObserver(([e])=>el.classList.toggle('is-stuck',e.intersectionRatio<1),
    {threshold:[1]});
  const s=document.createElement('div'); s.style.cssText='position:absolute;top:-1px;height:1px;width:1px';
  el.parentNode.insertBefore(s,el); io.observe(el);
})();
```

### 4.3 Editorial asymmetry & the golden section header

Break center-alignment. Left-align section heads with an eyebrow + gradient rule; let the content grid lean. The `.section-head` / `.eyebrow` / `.rule-gold` primitives already exist — use them consistently.

```html
<div class="section-head">
  <div>
    <p class="eyebrow">Five-Star Classics</p>
    <h2>Matches that defined an era</h2>
    <hr class="rule-gold">
  </div>
  <a class="link-more" href="/matches/">All matches →</a>
</div>
```

### 4.4 Bento / mixed-span grid (kills the uniform-card look)

A responsive grid where a few tiles span 2 cols/rows creates hierarchy and rhythm with zero art.

```css
.bento{display:grid;gap:var(--sp-4);grid-template-columns:repeat(auto-fit,minmax(220px,1fr));}
.bento > .is-wide{grid-column:span 2;}
.bento > .is-tall{grid-row:span 2;}
@media (max-width:560px){ .bento>.is-wide,.bento>.is-tall{grid-column:auto;grid-row:auto;} }
```

(Bento layout trend: Awwwards / Godly.website 2024–25.)

---

## 5. DEPTH & TEXTURE — grain, patterns, tasteful glass

This is the layer that most cheaply converts "flat CSS" into "designed object."

### 5.1 Grain / film-noise overlay (data-URI, zero requests)

An inline SVG `feTurbulence` noise as a repeating background. No HTTP request, tiny, tiles seamlessly. Apply globally as a fixed overlay at 3–5% opacity.

```css
.grain{position:fixed;inset:0;z-index:1;pointer-events:none;opacity:.045;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  background-size:180px 180px;mix-blend-mode:overlay;}
```

```html
<!-- place once, just before </body> -->
<div class="grain" aria-hidden="true"></div>
```

For the hero specifically, scope a denser grain to `.hero__grain` with the same data-URI at `opacity:.06`. Tune with `baseFrequency` (higher = finer grain) and `opacity` (keep ≤.06 or text legibility suffers). Source: CSS-Tricks *Grainy Gradients* and Codrops *feTurbulence* — confirmed `type='fractalNoise'`, `stitchTiles='stitch'` for seamless tiling.

**Performance/a11y notes:** it's a static raster the browser rasterizes once; cheaper than an animated filter. Keep `pointer-events:none` and `aria-hidden`. On very large 4K screens bump `background-size` so grain doesn't disappear.

### 5.2 Subtle repeating patterns (mat texture / stat backgrounds)

Faint geometric patterns behind stat blocks or footers read as "material." Use CSS gradients so there's no image.

```css
/* fine grid — good behind data tables / stat panels */
.pattern-grid{background-image:
  linear-gradient(rgba(255,255,255,.03) 1px,transparent 1px),
  linear-gradient(90deg,rgba(255,255,255,.03) 1px,transparent 1px);
  background-size:28px 28px;}

/* diagonal "ring apron" hatch — good behind CTAs / footers */
.pattern-hatch{background-image:
  repeating-linear-gradient(45deg,rgba(212,175,55,.05) 0 2px,transparent 2px 12px);}

/* dot field — good behind quotes / editorial */
.pattern-dots{background-image:radial-gradient(rgba(255,255,255,.05) 1px,transparent 1.4px);
  background-size:22px 22px;}
```

### 5.3 Glassmorphism — tasteful, sparing

Frosted glass belongs on **floating** elements over content/color: sticky nav, a stat-line over the hero, modal chrome. Never on a plain dark background (there's nothing to blur → it just looks muddy).

```css
.glass{
  background:color-mix(in srgb,var(--c-bg-elev-2) 55%,transparent);
  backdrop-filter:blur(14px) saturate(1.2);
  -webkit-backdrop-filter:blur(14px) saturate(1.2);
  border:1px solid rgba(255,255,255,.08);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.06),var(--shadow-2);
  border-radius:var(--r-lg);}
/* always provide a solid fallback */
@supports not (backdrop-filter:blur(2px)){ .glass{background:var(--c-bg-elev-2);} }
```

Example use — a floating stat bar overlapping the hero's bottom edge:

```html
<div class="glass stats-bar">
  <div class="stat"><b>41</b><span>Legends</span></div>
  <div class="stat"><b>30</b><span>Classic Matches</span></div>
  <div class="stat"><b>15</b><span>Defining Rivalries</span></div>
</div>
```

```css
.stats-bar{display:flex;gap:var(--sp-6);justify-content:center;
  width:min(100% - 2rem,var(--wrap));margin:-3.5rem auto 0;position:relative;z-index:2;
  padding:var(--sp-4) var(--sp-6);}
.stats-bar .stat b{font-family:var(--font-cond);font-size:var(--fs-800);color:var(--c-gold);display:block;}
.stats-bar .stat span{color:var(--c-text-muted);text-transform:uppercase;letter-spacing:.1em;font-size:var(--fs-300);}
```

### 5.4 Inner highlight — the "one pixel" that sells material

The cheapest premium trick: a 1px top inner highlight (`inset 0 1px 0 rgba(255,255,255,.06)`) on cards, buttons, and panels simulates a light hitting the top edge. Add it everywhere raised. Already in `--shadow-gold`; generalize it:

```css
:root{ --edge-light:inset 0 1px 0 rgba(255,255,255,.07); }
.card,.btn,.glass,.stat-panel{box-shadow:var(--edge-light),var(--shadow-1);}
```

---

## 6. Buttons & CTAs (the accent payoff)

CTAs are where gold earns its keep. Solid metallic gold primary, ghost secondary, with a sweep-shine on hover.

```css
.btn{display:inline-flex;align-items:center;gap:.5em;font-family:var(--font-cond);
  text-transform:uppercase;letter-spacing:.04em;font-weight:700;
  padding:.8em 1.4em;border-radius:var(--r-pill);border:1px solid transparent;
  transition:transform var(--dur) var(--ease),box-shadow var(--dur) var(--ease),background var(--dur);}
.btn:hover{transform:translateY(-1px);}
.btn--gold{color:#1a1400;background:linear-gradient(180deg,#f7e08a,var(--c-gold) 55%,var(--c-gold-dim));
  box-shadow:var(--edge-light),0 6px 20px rgba(212,175,55,.28);position:relative;overflow:hidden;}
.btn--gold::after{content:"";position:absolute;inset:0;transform:translateX(-120%);
  background:linear-gradient(105deg,transparent 40%,rgba(255,255,255,.45) 50%,transparent 60%);
  transition:transform .6s var(--ease);}
.btn--gold:hover::after{transform:translateX(120%);}   /* shine sweep */
.btn--ghost{color:var(--c-text);border-color:var(--c-line-strong);background:transparent;}
.btn--ghost:hover{border-color:var(--c-gold);color:var(--c-gold-bright);box-shadow:var(--glow-gold);}
@media (prefers-reduced-motion:reduce){ .btn--gold::after{display:none;} }
```

(Shine-sweep is a Nike/Jordan CTA idiom; kept subtle and reduced-motion-safe.)

---

## 7. Implementation checklist (drop-in order)

1. Add the global `.grain` div before `</body>` and its CSS (§5.1). Biggest instant win.
2. Rebuild the homepage hero with the layered background + vignette (§1.1) and oversized gradient title (§1.3).
3. Convert roster/match tiles to duotone-monogram placeholders (§3.1) + hover elevation (§3.3).
4. Add gradient borders (§3.2) to featured cards only — keep it rare so it stays special.
5. Wire the two tiny JS files (`hero-parallax.js` §1.5, `card-spotlight.js` §3.4) — both bail out under reduced motion.
6. Introduce ONE angled section seam (§4.1) and the sticky sub-nav (§4.2). Don't over-angle.
7. Apply the 90/8/2 accent rule (§2.1) as a global audit pass: demote most gold/red to neutral, keep it for events.

**Guardrails:** every motion effect already inherits the site's global `prefers-reduced-motion` reset; keep grain ≤.06 opacity; never stack glass on flat backgrounds; gold and red never adjacent at full saturation.

---

## Sources (studied for technique synthesis — no code or assets copied)

**Galleries & award sites (visual reference):**
- [Awwwards — Sports](https://www.awwwards.com/websites/sports/) and [Dark Mode collection](https://www.awwwards.com/awwwards/collections/dark-mode/)
- [Awwwards — Trendy Gradients in Web Design](https://www.awwwards.com/gradients-in-web-design-elements.html)
- [CSS Design Awards — Sport gallery](https://www.cssdesignawards.com/website-gallery?industry=sport)
- [SliderRevolution — Award-Winning Website Design Examples](https://www.sliderrevolution.com/design/award-winning-websites/)
- [Muffin Group — Sports Website Design Examples](https://muffingroup.com/blog/sports-website-design/)

**Technique sources (methods synthesized into original CSS above):**
- Grain/noise: [CSS-Tricks — Grainy Gradients](https://css-tricks.com/grainy-gradients/); [Codrops — SVG Filter Effects: feTurbulence](https://tympanus.net/codrops/2019/02/19/svg-filter-effects-creating-texture-with-feturbulence/); [freeCodeCamp — Grainy CSS Backgrounds Using SVG Filters](https://www.freecodecamp.org/news/grainy-css-backgrounds-using-svg-filters/)
- Diagonal/angled sections: [CSS-Tricks — Create Diagonal Layouts Like it's 2020](https://css-tricks.com/create-diagonal-layouts-like-its-2020/); [Viget — Angled Edges with CSS Masks and Transforms](https://www.viget.com/articles/angled-edges-with-css-masks-and-transforms)
- Gradient borders & masks: [CSS-Tricks — Fancy Image Decorations: Masks and Advanced Hover Effects](https://css-tricks.com/fancy-image-decorations-masks-and-advanced-hover-effects/)
- Duotone: [egghead — Duotone with pseudo-elements + mix-blend-mode](https://egghead.io/lessons/css-use-css-pseudo-elements-and-mix-blend-mode-to-create-a-duotone-style-effect); [freefrontend — CSS Duotone examples](https://freefrontend.com/css-duotone/)
- Spotlight / pointer hover: [Frontend Masters — CSS Spotlight Effect](https://frontendmasters.com/blog/css-spotlight-effect/); [Cruip — Spotlight Card Hover Effect](https://cruip.com/how-to-create-a-spotlight-card-hover-effect-with-tailwind-css/)
- Sports typography reference: [Creative Market — Best Sports Fonts](https://creativemarket.com/blog/best-sports-fonts)

**Brand visual language referenced (no assets used):** UFC.com, ESPN, DAZN, The Athletic, Bleacher Report, Sherdog, Tapology, F1.com, NBA.com, Nike/Jordan.
