# 00 — Design System · "Broadcast Bold"

> The foundation doc for the MAT homepage redesign. Every section file (01–11) inherits
> the tokens, type system, motion rules, and accessibility policy defined here.
> All classes/tokens referenced are **real** and live in `/css/site.css`
> (see the "BROADCAST BOLD UPGRADE (v2)" block, line ~358+).

---

## 1. Art direction

**Broadcast Bold** = ESPN / UFC / DAZN broadcast-graphic energy fused with editorial
restraint. The feeling is a championship pay-per-view lower-third: huge condensed type,
a warm-black arena lit by two off-axis spotlights (gold + red), film grain, one angled
cut per screen, and motion that *responds* rather than *loops*.

The five rules that keep it reading "expensive," not "generic" (from the visual research):

1. **Depth via layers, never flat fills.** Every dark surface stacks: base black → radial
   glow → conic sweep → grain → vignette. A single `background:#0a0b0d` reads unfinished.
2. **One loud gesture per screen.** Oversized display type OR one animated gradient OR one
   angled break — not all three fighting.
3. **Accent discipline (the 90/8/2 rule).** Gold and red are *events*, not surfaces.
4. **Texture kills the vector-art look.** A 3–5% film-grain overlay makes gradients read
   as broadcast/print instead of default CSS.
5. **Motion that responds.** Pointer spotlights and parallax feel bespoke; fast infinite
   loops feel like a template.

---

## 2. Color tokens & the 90/8/2 accent rule

Palette anchors: **black canvas + championship-gold `#d4af37` + blood-red `#c8102e`.**
Never use pure `#fff` on black — text is `--c-text #e8eaed`.

### 2.1 Live tokens (from `site.css` `:root`)

| Token | Value | Use |
|---|---|---|
| `--c-bg` | `#0a0b0d` | Page canvas (warm black, not pure #000) |
| `--c-bg-elev-1` | `#121418` | Raised surface / card |
| `--c-bg-elev-2` | `#1a1d23` | Higher surface / media wells |
| `--c-bg-elev-3` | `#23272f` | Inputs, chips |
| `--c-line` / `--c-line-strong` | `#2b3038` / `#3a414c` | Hairlines / stronger borders |
| `--c-text` / `--c-text-muted` / `--c-text-dim` | `#e8eaed` / `#a2a9b4` / `#6b727d` | Text hierarchy |
| `--c-gold` / `--c-gold-bright` / `--c-gold-dim` | `#d4af37` / `#f2cc4b` / `#8c7420` | The jewelry accent |
| `--c-red` / `--c-red-bright` / `--c-red-dim` | `#e11d2a` / `#ff3b48` / `#8f1219` | The alarm accent |
| `--c-gold-tint` / `--c-red-tint` | `rgba(...,.12)` | Tint washes over surfaces |
| `--c-win` / `--c-loss` / `--c-live` | `#2fbf71` / `#e05263` / `--c-red-bright` | Status |

> Note: the brand red in the type/visual research is `#c8102e`; the codebase token
> `--c-red` is `#e11d2a` (a hair brighter). **Use the token `--c-red`** so the build stays
> consistent — do not hard-code hex.

Composite tokens available: `--glow-gold`, `--glow-red`, `--edge-light`
(`inset 0 1px 0 rgba(255,255,255,.07)` — the "one pixel" top highlight that sells material),
`--shadow-1/2`, `--shadow-gold`.

### 2.2 The 90/8/2 accent rule (mandatory audit pass)

- **~90% neutral** — `--c-bg`, the three elevation surfaces, hairlines, muted text.
- **~8% gold** — ONE hero line, primary/gold CTAs, active nav, eyebrows, ratings,
  championship/stat highlights.
- **~2% red** — live badges, the "vs", one urgent CTA, one hover. Red is the blood; its
  scarcity is what makes it read as danger.

**Never place large gold and large red adjacent at full saturation** — they vibrate.
Separate with neutral space, or let one be a glow and the other a fill.

### 2.3 Metallic gold, not flat gold

Flat `#d4af37` looks like a swatch. Use the 3-stop vertical gradient used by `.btn--gold`
and `.hero-bb__title .accent`: `linear-gradient(180deg,#f7e08a,var(--c-gold) 55%,var(--c-gold-dim))`.
Light hits the top, shadow pools at the bottom → reads as *metal*.

---

## 3. Type system — Anton / Oswald / Inter

Two-role principle: a loud narrow all-caps **display** shout over a quiet humanist
mixed-case **body**. Contrast, don't compete. Live font tokens (`site.css` v2 block):

```css
--font-display:"Anton","Oswald","Arial Narrow",sans-serif;      /* the shout */
--font-cond:"Oswald","Bebas Neue","Arial Narrow",system-ui,sans-serif; /* UI / labels */
--font-sans:"Inter",system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans SC",sans-serif; /* body */
```

| Role | Family | Where |
|---|---|---|
| **Display** | **Anton** (single ~900 weight) | Hero title, section H2s, big stat numerals, tile monograms, poster names |
| **Condensed UI** | **Oswald** (200–700) | Eyebrows/kickers, nav, buttons, chips, table headers, marquee, labels |
| **Body** | **Inter** (400–700) | Paragraphs, ledes, form copy, FAQ answers, footer links |

**Load two families for perf; Anton is one tiny file, Inter is one variable file, Oswald is
the multi-weight UI face.** Global edition: Google Fonts with `&display=swap`, `preconnect`
to `fonts.gstatic.com`, and **preload only Anton** (above-the-fold display). China edition:
self-host Latin woff2 subsets, never call `fonts.gstatic.com`, fall CJK through to
`PingFang SC` / `Microsoft YaHei` (set CJK headings to weight 700 since Anton has no CJK).

### 3.1 Fluid scale (live tokens, clamp-based, no media queries)

```
--fs-300  0.78→0.875rem   captions / kickers / meta
--fs-400  0.94→1.05rem    body / nav
--fs-500  1.13→1.35rem    lead / card titles
--fs-600  1.35→1.80rem    h3
--fs-700  1.65→2.55rem    h2
--fs-800  2.05→3.60rem    h1 / big stat nums
--fs-900  2.60→5.00rem    hero-scale numerals
```

The hero title bypasses the token scale for maximum impact:
`font-size:clamp(3rem,7.5vw + .5rem,8rem)` with `line-height:.9`, `letter-spacing:-.005em`.
Line-height tokens: `--lh-tight 1.08` (display), `--lh-snug 1.28`, `--lh-body 1.6`.

### 3.2 Treatments

- **Gold-foil headline** — the `.accent` clip: `background-clip:text` + the metallic gold
  gradient + `drop-shadow(0 2px 12px rgba(212,175,55,.28))`. **One line per screen.**
- **Outline / "shout" text** — `.stroke`: `color:transparent;-webkit-text-stroke:1.6px rgba(232,234,237,.6)`.
- **Ghost numerals/monograms** — `.tile__mono`, `.poster .tile__mono`: huge Anton at
  `rgba(255,255,255,.06)` with a 1px stroke, bleeding off the card edge.
- Tracking rules: condensed caps display `-0.01em`→`0` (already tight); all-caps *label-size*
  text **adds** `.06–.12em` (caps need air); never letter-space lowercase body.
- `text-wrap:balance` on headings, `text-wrap:pretty` on paragraphs (both already in base).

---

## 4. Grain, texture & glass

- **Global film grain** — `<div class="grain" aria-hidden="true">` placed once before
  `</body>`. Fixed, `opacity:.05`, `mix-blend-mode:overlay`, inline SVG `feTurbulence`
  data-URI (zero HTTP requests). The hero scopes a denser copy via `.hero-bb__grain`
  (`opacity:.07`). Keep grain ≤ .07 or text legibility suffers.
- **Patterns** — `.pattern-hatch` (45° gold ring-apron hatch) behind CTAs/footers.
- **Glass** — `.glass`: `backdrop-filter:blur(14px) saturate(1.2)`, hairline border,
  `--edge-light` sheen, with an `@supports not` solid fallback. **Only on floating elements
  over content/color** (stats bar over hero, sticky nav). Never on a flat background — there's
  nothing to blur. Never stack glass on glass. Keep blur ≤ 16px.

---

## 5. Buttons & chips

**Buttons** (`.btn` base is Oswald, uppercase, `.04em` tracking, pill radius):

- `.btn--gold` — primary "premium/earned" action. Metallic gold gradient, `--edge-light`,
  a shine sweep on `:hover` via `::after` (auto-disabled under reduced motion).
- `.btn--primary` — blood-red action (waitlist/join urgency).
- `.btn--ghost` — quiet tertiary; on hover the border warms to gold + `--glow-gold`.
- `.btn--lg` — hero/CTA-band size.

**Chips** (`.chip`): neutral by default. Variants: `.chip--live` (red + pulsing dot),
`.chip--gold`, `.chip--win/--loss`, and per-promotion `.chip--wwe/--wcw/--ecw/--tna/--nxt`.

**Rating**: `.rating` (display stars via `--rating`), `.ratingbox` (big gold number panel),
`.meter`/`.meter__fill` (red→gold gradient bar).

---

## 6. Motion principles + reduced-motion policy

Guiding rules (from the motion research):

1. Animate **only `transform` and `opacity`** (compositor-only, 60fps). Never animate
   `top/left/width/height/margin`.
2. Prefer **`IntersectionObserver`** over scroll listeners (off-main-thread, batched).
3. **Throttle pointer work with `requestAnimationFrame`** — write custom props once per tick,
   never inside `pointermove`.
4. Gate pointer effects behind `matchMedia('(hover:hover) and (pointer:fine)')` so touch
   devices never run useless listeners.
5. Add `will-change` during interaction, drop it when idle.

**The homepage motion inventory** (each detailed in its section file, all reduced-motion safe):

| Effect | Mechanism | Section |
|---|---|---|
| Hero mesh drift | CSS `heroDrift` on `background-position`, 26s | 02 |
| Hero pointer parallax | rAF writes `--px/--py` to `.hero-bb__bg` | 02 |
| Scroll reveal / stagger | `[data-reveal]` + IO adds `.is-in` | all |
| Stat count-up | rAF + `IntersectionObserver` | 03 |
| Marquee ticker | CSS `marquee` translateX, pause on hover | 04 |
| Card / tile spotlight | rAF writes `--mx/--my` to `.tile__spot` | 06,07 |
| Gradient-border warm | CSS `::before` opacity on hover | 05 |
| Sticky header shadow | sentinel + IO toggles `.is-stuck` | 01 |
| Button shine sweep | CSS `::after` translateX on hover | all CTAs |

### Reduced-motion policy (the law)

`site.css` ships a **global reset**: under `prefers-reduced-motion:reduce`, all
animations/transitions collapse to `.01ms`. On top of that, **every component also handles
it explicitly** so nothing is left blank:

- `[data-reveal]` → `opacity:1;transform:none` (content shown).
- `.hero-bb__bg` → `animation:none` (static, still on-brand).
- `.marquee__track` → `animation:none;overflow-x:auto` (becomes manually scrollable, no
  content lost).
- Count-up → writes the final value instantly (no stuck "0").
- `.btn--gold::after` shine → `display:none`.
- Pointer effects (parallax, spotlight) → JS bails at init via `matchMedia`.

---

## 7. Accessibility (baseline for every section)

- **Semantics:** exactly one `<h1>` (hero); logical `h2`→`h3` down the page. Landmarks:
  `<header>`, `<nav aria-label>`, `<main>`, section `<section aria-labelledby>`, `<footer>`.
- **Skip link:** `.skip-link` to `#main` (already styled).
- **Focus:** visible `:focus-visible` ring (`--c-focus #5aa9ff`, 2px, offset 2px) globally;
  every hover affordance also fires on `:focus-visible` (keyboard parity).
- **Decorative layers** (`.grain`, `.hero-bb__bg`, `.hero-bb__grain`, marquee clone, tile
  monograms/spots) carry `aria-hidden="true"`.
- **Contrast:** gold on `--c-bg` ≈ 8.9:1 (AA/AAA). Red `#e11d2a` on black ≈ 4:1 → **large
  text / non-text only**; never body copy in red.
- **Touch targets** ≥ 44px (nav toggle, CTAs, bottom sticky bar).
- **Progressive enhancement:** all text is in server-rendered HTML; if JS/IO fails, reveals
  show, counters show final values, marquee is scrollable — nothing depends on JS to be read.
- Respect `prefers-reduced-motion` live via `matchMedia(...).matches` at init.

---

## 8. Layout primitives (shared)

- `.wrap` (max `--wrap 1200px`) / `.wrap--narrow` (`760px`) — centered containers.
- `.section` (`padding-block --sp-8`) / `.section--tight`.
- `.section-head` + `.eyebrow` + `.rule-gold` + `.link-more` — the standard left-aligned
  editorial section header (eyebrow → H2 → gold rule; "see all →" link right).
- `.stack` / `.stack-lg` / `.cluster` / `.center` — spacing helpers.
- Grids: `.grid-cards`, `.grid-2`, `.grid-3`, `.grid-spot` (tiles), `.bento`, `.tiers`.
- Spacing scale `--sp-1`…`--sp-8`; radii `--r-sm/md/lg/pill`.

---

## 9. SEO / GEO baseline

The homepage is simultaneously a **content site** (fans search a wrestler/match) and a
**conversion funnel**. Both require:

- **SSR/static HTML** — all copy (hero, tiles, benefits, FAQ) in the DOM, not JS-injected.
- **LCP < 2.5s** — preload only Anton; grain/gradients are CSS; images lazy-load below fold.
- **Schema:** `Organization` (page), `FAQPage` (section 10), `ItemList` (rails 06/07),
  `Product`/`Offer` (membership 09).
- **Citation-worthy stats** stated as *number + year in one sentence* ("30 five-star matches
  indexed as of 2026") — exactly what RAG engines lift.
- **Internal links** from rails + footer build topical depth and feed the funnel.
