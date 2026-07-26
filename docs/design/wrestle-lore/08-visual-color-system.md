# Wrestle Lore — Visual Color & Separation System (Spec 08)

Visual-systems deliverable. This is the "more colors / more separation / more categories" backbone.
It defines the palette, the token layer (CSS custom properties, themeable), the badge/chip shape+color
grammar, the duotone poster-tile spec, the brand-card spec, section theming, and a full
clickable → link-target table. It builds directly on the existing single stylesheet
`/root/wwe/css/site.css` (all additions are additive; no existing class changes behavior).

- Date: 2026-07-26. Author: visual systems designer.
- Grounded in: `00-content-data-research.md` (facts, streaming, HOF, gaps) and `01-inspiration-research.md`
  (badge/color-as-load-bearing, hub-spoke, poster density). No new facts are invented here; anything a
  card must state that is not yet verified is carried through with a `VERIFY` flag from doc 00.
- Reuse rule: existing tokens in `site.css` §1 stay as the source of truth. This spec ADDS tokens and
  components and never redefines an existing hex.

---

## 1. Design problem and the governing principle

The user wants MORE colors and MORE separation without the wall turning into confetti. The failure
mode of "add more colors" is a rainbow where nothing reads. The fix is a strict **role hierarchy plus
shape-encodes-axis, color-encodes-category** grammar (the load-bearing-badge pattern from doc 01 A3/D1).

**Two independent channels carry meaning so a tile is never ambiguous:**
- **SHAPE encodes the AXIS** (what kind of fact this is): pill = status, squared chip = division,
  color-bar tag = promotion, plaque = Hall of Fame, play-mark = Moment, plain condensed text = era.
- **COLOR encodes the CATEGORY within that axis** (which value): red = current, gold = legend,
  magenta = women's, per-promotion accents, purple = media, etc.

Because the axis is already told by shape, two categories can safely share a hue family (e.g. CURRENT
and MOMENTS are both red) without confusion — one is a pulsing pill, the other a play-marked tag.

**Loudness tiers (only one "tier 1" color per tile, so density stays legible):**

| Tier | Carries | Visual weight | Where it lives on a tile |
|---|---|---|---|
| **Tier 1 — Promotion accent** | The single dominant identity color; drives the duotone gradient. | Loudest: full-bleed gradient field + monogram. | Whole `.tile__media`. |
| **Tier 2 — Status + Division badges** | CURRENT/LEGEND, WOMEN'S/MEN'S. | Small solid/outline badges, top-left cluster. | `.tile__badges` overlay. |
| **Tier 3 — Era / meta** | Era band, rating. | Muted condensed text; rating chip bottom-right. | `.tile__body`, `.tile__rating`. |
| **Section theme** | HOF gold, Moments red, Media purple. | Owns the hub via one `--accent` swap. | Hub wrapper `.theme-*`. |

This is what makes it "themeable": every component reads a **semantic `--accent`** variable; a hub or a
tile sets `--accent` once (via `data-promo` or `.theme-*`) and the whole subtree recolors.

---

## 2. Palette — full token set (CSS custom properties)

### 2.1 Existing base tokens (source of truth, do NOT redefine — listed for reference)

From `site.css` §1: `--c-bg:#0a0b0d`, `--c-bg-elev-1:#121418`, `--c-bg-elev-2:#1a1d23`,
`--c-bg-elev-3:#23272f`, `--c-line:#2b3038`, `--c-line-strong:#3a414c`, `--c-text:#e8eaed`,
`--c-text-muted:#a2a9b4`, `--c-text-dim:#6b727d`, `--c-gold:#d4af37`, `--c-gold-bright:#f2cc4b`,
`--c-gold-dim:#8c7420`, `--c-gold-tint:rgba(212,175,55,.12)`, `--c-red:#e11d2a`,
`--c-red-bright:#ff3b48`, `--c-red-dim:#8f1219`, `--c-red-tint:rgba(225,29,42,.12)`,
`--c-win:#2fbf71`, `--c-loss:#e05263`, `--c-focus:#5aa9ff`, and promotion accents
`--c-wwe:#c8102e`, `--c-wcw:#e2b13c`, `--c-ecw:#b0b0b0`, `--c-tna:#1e73be`, `--c-nxt:#f5c518`.

### 2.2 NEW tokens to add to `:root` (this spec)

```css
:root{
  /* ---- NEW promotion accent: NJPW (Requirement 5) ---- */
  /* NJPW brand red; kept distinct from --c-wwe / --c-red by PAIRING (see §2.3), not hue alone. */
  --c-njpw:#d81f26;               /* VERIFY exact hex vs official NJPW branding (doc 00 §4) */
  --c-njpw-bright:#ff4a4f;        /* text-on-dark safe variant */
  --c-njpw-tint:rgba(216,31,38,.14);
  --c-njpw-sun:#ffffff;           /* rising-sun rule = NJPW's distinguishing pairing signal */

  /* ---- Reserved external promotion (cross-links only; no hub page yet) ---- */
  --c-aew:#c8a24a;                /* AEW gold-bronze; RESERVED/VERIFY, used only in text cross-links */

  /* ---- Category axes (non-promotion) ---- */
  /* Axis A — status. CURRENT reuses red family; LEGEND reuses gold family. */
  --c-current:var(--c-red);       --c-current-bright:var(--c-red-bright); --c-current-tint:var(--c-red-tint);
  --c-legend:var(--c-gold);       --c-legend-bright:var(--c-gold-bright); --c-legend-tint:var(--c-gold-tint);

  /* Axis B — division / gender. WOMEN'S = magenta (new, distinct). MEN'S = neutral steel. */
  --c-womens:#e0409f;             --c-womens-bright:#f26bbb; --c-womens-dim:#8f2464; --c-womens-tint:rgba(224,64,159,.14);
  --c-mens:#8593a6;               --c-mens-tint:rgba(133,147,166,.12);   /* desaturated on purpose: reads "neutral", not "blue=male" */

  /* Section themes */
  --c-hof:#e8b923;                --c-hof-bright:#ffd24a; --c-hof-deep:#7a5c12; --c-hof-tint:rgba(232,185,35,.14); /* Hall of Fame: warmer gold than --c-gold */
  --c-moment:var(--c-red-bright); --c-moment-tint:var(--c-red-tint);       /* Moments (video incidents) */
  --c-media:#a855f7;              --c-media-bright:#c084fc; --c-media-dim:#6b21a8; --c-media-tint:rgba(168,85,247,.14); /* Media & Creators (Requirement 7) */

  /* Era bands (Tier 3, deliberately MUTED so promotion/status stay dominant) */
  --c-era-golden:#c9a35b;   /* 80s     */
  --c-era-newgen:#9bb0c4;   /* early90s */
  --c-era-attitude:#d0563f; /* late90s  */
  --c-era-ruthless:#7f8fa6; /* 2000s    */
  --c-era-pg:#6f9f8f;       /* 2010s    */
  --c-era-modern:#b9c2cf;   /* 2020s    */

  /* ---- Semantic accent alias (the themeable hook; defaults to gold) ---- */
  --accent:var(--c-gold);
  --accent-bright:var(--c-gold-bright);
  --accent-dim:var(--c-gold-dim);
  --accent-tint:var(--c-gold-tint);
  --accent-on:#000;               /* text color that sits ON a solid --accent fill */
}
```

### 2.3 NJPW-vs-WWE-vs-site-red separation (explicit design decision)

Three reds now exist (`--c-red`, `--c-wwe`, `--c-njpw`). Hue alone will not separate them at tile scale.
The system separates them by **pairing and shape**, which is the honest visual-systems answer:

- **WWE** = crimson `--c-wwe` field, no white rule, block monogram "W".
- **NJPW** = `--c-njpw` field **plus a white `--c-njpw-sun` rising-ray gradient** at the top-right and a
  1px white top rule. The **white sunburst is unique to NJPW** and is the instant differentiator; WWE
  never uses it. Monogram is the NJPW lion-inspired "N" over a thin white rule.
- **site red (`--c-red`)** is a UI/action color (buttons, live dots, Moments), never used as a
  promotion field. So on a poster wall, a red *field* is always a promotion, disambiguated by the sun.

`VERIFY` (doc 00 §4): confirm the exact NJPW brand red before locking `--c-njpw`.

---

## 3. WCAG AA contrast — verified pairings and rules

Background is `--c-bg #0a0b0d` (relative luminance L≈0.0033). Ratios below are computed against it.
AA thresholds: **4.5:1** normal text, **3.0:1** large text (≥24px, or ≥18.66px bold) and UI/graphical
objects. Every color has a documented safe use.

| Token | Hex | L | Ratio on --c-bg | Body text? | Large/UI? | Rule |
|---|---|---|---|---|---|---|
| --c-gold | #d4af37 | .447 | 8.4:1 | yes | yes | any text |
| --c-gold-bright | #f2cc4b | .62 | 11.6:1 | yes | yes | preferred for gold body text |
| --c-red | #e11d2a | .170 | 4.13:1 | **no** | yes | fills, large headings, dots — not body text |
| --c-red-bright | #ff3b48 | .249 | 5.6:1 | yes | yes | use for red *text* |
| --c-wwe | #c8102e | .128 | 3.35:1 | no | yes | fill/large only; body text → #fff on fill |
| --c-wcw | #e2b13c | .49 | 9.1:1 | yes | yes | any text |
| --c-ecw | #b0b0b0 | .435 | 8.7:1 | yes | yes | any text |
| --c-tna | #1e73be | .162 | 3.98:1 | **no** | yes | fill/large only; brighten for body |
| --c-nxt | #f5c518 | .63 | 11.8:1 | yes | yes | any text |
| --c-njpw | #d81f26 | ~.17 | ~4.1:1 | no | yes | fill/large; body → --c-njpw-bright |
| --c-njpw-bright | #ff4a4f | ~.27 | ~5.9:1 | yes | yes | red text on dark |
| --c-womens | #e0409f | .220 | 5.06:1 | yes | yes | text ok; on fill use dark text |
| --c-womens-bright | #f26bbb | ~.33 | ~7:1 | yes | yes | preferred women's text |
| --c-mens | #8593a6 | .287 | 6.3:1 | yes | yes | neutral chip text/fill |
| --c-hof | #e8b923 | ~.55 | ~10:1 | yes | yes | any text |
| --c-media | #a855f7 | .216 | 4.99:1 | yes(borderline) | yes | prefer --c-media-bright for body |
| --c-media-bright | #c084fc | ~.36 | ~7.5:1 | yes | yes | media text on dark |

**Text-ON-solid-fill pairings (for chips/badges):**

| Fill | Text color | Ratio | Verdict |
|---|---|---|---|
| --c-wwe #c8102e | #ffffff | 5.9:1 | AA |
| --c-wcw #e2b13c | #000 | 10.8:1 | AA (existing) |
| --c-ecw #b0b0b0 | #000 | 9.7:1 | AA (existing) |
| --c-tna #1e73be | #ffffff | 4.95:1 | AA (existing) |
| --c-nxt #f5c518 | #000 | 12:1 | AA (existing) |
| --c-njpw #d81f26 | #ffffff | ~5.5:1 | AA |
| --c-womens #e0409f | #1a0812 (near-black) | 5.4:1 | AA — dark text on magenta |
| --c-media #a855f7 | #15082a (near-black) | 5.3:1 | AA — dark text on purple |
| --c-mens #8593a6 | #12161d | 6.7:1 | AA — dark text on steel |
| --c-hof #e8b923 | #000 | ~11:1 | AA |

**Two hard rules for implementers:**
1. Never set body text in `--c-red`, `--c-wwe`, `--c-tna`, or `--c-njpw` (the sub-4.5 colors). Use the
   `-bright` variant for text, or reserve those hexes for fills/large display/graphics.
2. Every solid chip/badge pairs its fill with the text color in the table above (dark text on the
   light-ish category colors: gold/wcw/nxt/womens/media/mens; white text on the deep ones: wwe/tna/njpw).

Focus ring stays `--c-focus #5aa9ff` (2px, offset 2px) site-wide — unchanged, AA against all fills.

---

## 4. Themeable accent system (the `--accent` swap)

One mechanism recolors everything. A container sets the four accent vars; descendants (tiles, badges,
rails, buttons-ghost, section heads) read `--accent*`. Two entry points:

```css
/* A) Promotion scope — put data-promo on a tile, a rail, or a hub <body>/<section>. */
[data-promo="wwe"]  {--accent:var(--c-wwe);  --accent-bright:#ff5566; --accent-dim:#7a0a1c; --accent-tint:rgba(200,16,46,.14);  --accent-on:#fff;}
[data-promo="wcw"]  {--accent:var(--c-wcw);  --accent-bright:#f3c85e; --accent-dim:#8a6b18; --accent-tint:rgba(226,177,60,.14);  --accent-on:#000;}
[data-promo="ecw"]  {--accent:var(--c-ecw);  --accent-bright:#d6d6d6; --accent-dim:#6d6d6d; --accent-tint:rgba(176,176,176,.14); --accent-on:#000;}
[data-promo="tna"]  {--accent:var(--c-tna);  --accent-bright:#4a97e0; --accent-dim:#123f66; --accent-tint:rgba(30,115,190,.16);  --accent-on:#fff;}
[data-promo="nxt"]  {--accent:var(--c-nxt);  --accent-bright:#ffd84a; --accent-dim:#8a6f0a; --accent-tint:rgba(245,197,24,.14);  --accent-on:#000;}
[data-promo="njpw"] {--accent:var(--c-njpw); --accent-bright:var(--c-njpw-bright); --accent-dim:#7a1216; --accent-tint:var(--c-njpw-tint); --accent-on:#fff;}

/* B) Section theme scope — put on the hub wrapper. */
.theme-hof     {--accent:var(--c-hof);    --accent-bright:var(--c-hof-bright);   --accent-dim:var(--c-hof-deep); --accent-tint:var(--c-hof-tint);    --accent-on:#000;}
.theme-moments {--accent:var(--c-moment); --accent-bright:var(--c-red-bright);   --accent-dim:var(--c-red-dim);  --accent-tint:var(--c-red-tint);    --accent-on:#fff;}
.theme-media   {--accent:var(--c-media);  --accent-bright:var(--c-media-bright); --accent-dim:var(--c-media-dim); --accent-tint:var(--c-media-tint);  --accent-on:#15082a;}
.theme-current {--accent:var(--c-current);--accent-bright:var(--c-current-bright);--accent-dim:var(--c-red-dim); --accent-tint:var(--c-current-tint);--accent-on:#fff;}
.theme-legends {--accent:var(--c-legend); --accent-bright:var(--c-legend-bright);--accent-dim:var(--c-gold-dim);--accent-tint:var(--c-legend-tint); --accent-on:#000;}
.theme-women   {--accent:var(--c-womens); --accent-bright:var(--c-womens-bright);--accent-dim:var(--c-womens-dim);--accent-tint:var(--c-womens-tint);--accent-on:#1a0812;}
```

Components that should read `--accent` (refactor to var, keeps current default because `--accent`
defaults to gold): `.tile__kicker`, `.tile:hover` ring, `.tile__spot` spotlight, `.section-head h2`
underline, `.eyebrow`, `.rail` header rule, `.btn--ghost:hover` border. Existing hardcoded-gold rules
still render identically until a scope overrides `--accent`.

---

## 5. Badge & chip grammar (shape = axis, color = category)

### 5.1 The matrix

| Axis (SHAPE) | Component | Radius / form | Values → color | Text pairing |
|---|---|---|---|---|
| **Status** | `.badge-status` (pill) | `--r-pill`, filled or hairline | CURRENT = filled `--c-current-tint` + red border + pulsing dot; LEGEND = transparent + `--c-gold` 1px hairline | current: `--c-red-bright` text; legend: `--c-gold-bright` text |
| **Division** | `.badge-div` (squared chip) | `--r-sm` (square-ish) | WOMEN'S = `--c-womens` fill; MEN'S = `--c-mens` fill (or omit — default) | dark text per §3 |
| **Promotion** | `.tag-promo` (color-bar tag) | `--r-sm`, 3px left color bar | per `--accent` from `data-promo` | `--c-text` + accent bar |
| **Hall of Fame** | `.badge-hof` (plaque) | `--r-md`, squared, laurel glyph | `--c-hof` gold gradient | `#000` |
| **Moment** | `.tag-moment` (play tag) | `--r-sm` + ▸ leading glyph | `--c-moment` | `#fff` |
| **Era** | `.badge-era` (plain text) | none (condensed uppercase) | muted era hue (Tier 3) | era hue on dark |
| **Rating** | `.tile__rating` (existing) | `--r-sm` on scrim | `--c-gold-bright` | on `rgba(0,0,0,.55)` |

Why this resolves the "two reds / two golds" overlap: CURRENT (red pill w/ dot) vs MOMENT (red tag w/ ▸)
vs WWE (red promo bar) are three shapes; LEGEND (gold hairline pill) vs HOF (gold plaque) vs WCW/NXT
(gold/yellow promo bar) are distinct shapes. Color family repeats, meaning never collides.

### 5.2 CSS (additive)

```css
/* status pills */
.badge-status{display:inline-flex;align-items:center;gap:.4em;padding:.2em .6em;border-radius:var(--r-pill);
  font-family:var(--font-cond);text-transform:uppercase;letter-spacing:.05em;font-size:var(--fs-300);
  font-weight:700;line-height:1;border:1px solid transparent;}
.badge-status--current{color:var(--c-red-bright);background:var(--c-current-tint);border-color:var(--c-red-dim);}
.badge-status--current::before{content:"";width:.5em;height:.5em;border-radius:50%;background:var(--c-red-bright);
  box-shadow:0 0 0 0 rgba(255,59,72,.7);animation:pulse 1.4s infinite;}   /* reuses existing @keyframes pulse */
.badge-status--legend{color:var(--c-gold-bright);background:transparent;border-color:var(--c-gold);}

/* division chips (squared) */
.badge-div{display:inline-flex;align-items:center;padding:.22em .55em;border-radius:var(--r-sm);
  font-family:var(--font-cond);text-transform:uppercase;letter-spacing:.04em;font-size:var(--fs-300);font-weight:700;line-height:1;}
.badge-div--women{background:var(--c-womens);color:#1a0812;}
.badge-div--men{background:var(--c-mens);color:#12161d;}

/* promotion color-bar tag */
.tag-promo{display:inline-flex;align-items:center;gap:.45em;padding:.2em .55em .2em .5em;border-radius:var(--r-sm);
  background:var(--c-bg-elev-3);color:var(--c-text);font-family:var(--font-cond);text-transform:uppercase;
  letter-spacing:.04em;font-size:var(--fs-300);font-weight:700;border:1px solid var(--c-line);
  border-left:3px solid var(--accent);}

/* HOF plaque */
.badge-hof{display:inline-flex;align-items:center;gap:.4em;padding:.25em .7em;border-radius:var(--r-md);
  background:linear-gradient(180deg,var(--c-hof-bright),var(--c-hof) 60%,var(--c-hof-deep));color:#000;
  font-family:var(--font-cond);text-transform:uppercase;letter-spacing:.05em;font-weight:800;font-size:var(--fs-300);
  box-shadow:0 0 0 1px var(--c-hof-deep),0 4px 14px rgba(232,185,35,.20);}
.badge-hof::before{content:"\1F3C6";}   /* trophy glyph; swap for inline-SVG laurel at build if preferred */
.badge-hof--2x::after{content:"×2";margin-left:.25em;font-weight:800;}  /* most-decorated (Ric Flair) */

/* Moment play tag */
.tag-moment{display:inline-flex;align-items:center;gap:.35em;padding:.2em .55em;border-radius:var(--r-sm);
  background:var(--c-moment);color:#fff;font-family:var(--font-cond);text-transform:uppercase;
  letter-spacing:.04em;font-size:var(--fs-300);font-weight:700;}
.tag-moment::before{content:"\25B8";}   /* ▸ play mark = the Moment differentiator */

/* era label upgrade (existing .badge-era stays; add colored variants) */
.badge-era--golden{color:var(--c-era-golden);}   .badge-era--newgen{color:var(--c-era-newgen);}
.badge-era--attitude{color:var(--c-era-attitude);} .badge-era--ruthless{color:var(--c-era-ruthless);}
.badge-era--pg{color:var(--c-era-pg);}            .badge-era--modern{color:var(--c-era-modern);}

/* media chip (for /media/ tab) */
.chip--media{color:var(--c-media-bright);background:var(--c-media-tint);border-color:var(--c-media-dim);}
.chip--njpw{color:#fff;background:var(--c-njpw);border-color:var(--c-njpw);}  /* extends existing .chip--wwe set */
```

---

## 6. Duotone poster-tile spec (accent-driven upgrade)

Builds on the existing `.tile` / `.tile__media` / `.tile__mono` / `.tile__spot` in `site.css`. The one
change: swap the hardcoded `--c-red` in the gradient for `--accent`, so a tile auto-themes from its
`data-promo` (or a status theme). Existing tiles keep working (default `--accent` = gold; add
`data-promo` to opt into promotion color).

```css
/* accent-driven duotone (replaces hardcoded red in .tile__media background) */
.tile__media{
  background:
    linear-gradient(calc(var(--seed,220)*1deg),
      color-mix(in oklab,var(--accent) 55%,#000) 0%, #0c0d10 58%),
    var(--c-bg-elev-2);
}
/* NJPW rising-sun pairing overlay (only NJPW tiles) */
[data-promo="njpw"] .tile__media::before{content:"";position:absolute;inset:0;z-index:0;pointer-events:none;
  background:radial-gradient(120% 90% at 100% 0%,rgba(255,255,255,.18),transparent 42%);}
[data-promo="njpw"] .tile__media{border-top:1px solid var(--c-njpw-sun);}
/* hover ring + monogram + spotlight now follow accent */
.tile:hover{box-shadow:var(--shadow-2),0 0 0 1px var(--accent-dim);}
.tile:hover .tile__mono{color:color-mix(in srgb,var(--accent) 30%,transparent);}
.tile__spot{background:radial-gradient(220px circle at var(--mx,50%) var(--my,50%),
  color-mix(in srgb,var(--accent) 22%,transparent),transparent 60%);}
.tile__kicker{color:var(--accent);}
```

**`--seed` per tile** (0–360) varies the duotone angle so a grid of same-promotion tiles is not
identical — set inline `style="--seed:140"` from a hash of the slug at build time. Purely cosmetic.

**Tile HTML template (the canonical clickable poster):**

```html
<a class="tile" href="/wrestlers/aj-styles/" data-promo="njpw" style="--seed:200">
  <span class="tile__media" aria-hidden="true"><span class="tile__mono">A</span></span>
  <span class="tile__spot" aria-hidden="true"></span>
  <span class="tile__badges">                     <!-- Tier-2 overlay, top-left -->
    <span class="badge-status badge-status--current">Current</span>
    <span class="badge-div badge-div--men">Men's</span>
  </span>
  <span class="tile__rating">4.7</span>            <!-- Tier-3, bottom-right (if rated) -->
  <span class="tile__body">
    <span class="tile__kicker">NJPW · Bullet Club</span>
    <span class="tile__name">AJ Styles</span>
    <span class="badge-era badge-era--modern">Modern</span>
  </span>
</a>
```

Add the badge-overlay positioner (top-left cluster, mirrors existing `.tile__badge`):

```css
.tile__badges{position:absolute;top:var(--sp-2);left:var(--sp-2);z-index:3;display:flex;flex-wrap:wrap;gap:.3em;max-width:calc(100% - var(--sp-4));}
```

Accessibility: the gradient/monogram are `aria-hidden`; the accessible name comes from `.tile__name`
text inside the same `<a>`. Whole tile is one link (one clear target, no nested interactive elements).

---

## 7. Brand / streaming card spec (Requirement 4)

Promotion card = accent header + monogram + a "Where to watch" row of **text platform chips** (not
logos, per doc 01 D2 — avoids trademark image issues), a one-line positioning fact, and links to that
promotion's hub, events, and top wrestlers. Streaming facts are lifted verbatim from doc 00 §1.

```html
<article class="card--edge brandcard" data-promo="njpw">
  <header class="brandcard__head">
    <span class="brandcard__mono">NJPW</span>
    <h3>New Japan Pro-Wrestling</h3>
  </header>
  <p class="brandcard__line">Japan's largest promotion. Flagship event Wrestle Kingdom at the Tokyo Dome each January.</p>
  <p class="brandcard__watch-label">Where to watch</p>
  <div class="cluster">
    <span class="chip chip--njpw">NJPW World</span>
    <span class="chip">TrillerTV</span>
    <span class="chip">TV Asahi (Japan)</span>
  </div>
  <div class="cluster brandcard__links">
    <a class="btn btn--ghost" href="/promotions/njpw/">Promotion page</a>
    <a class="btn btn--ghost" href="/promotions/njpw/#events">Events</a>
    <a class="btn btn--ghost" href="/wrestlers/aj-styles/">AJ Styles</a>
  </div>
</article>
```

```css
.brandcard{padding:var(--sp-5);display:grid;gap:var(--sp-3);}
.brandcard__head{display:flex;align-items:center;gap:var(--sp-3);border-bottom:1px solid var(--accent-dim);padding-bottom:var(--sp-2);}
.brandcard__mono{display:inline-grid;place-content:center;min-width:56px;height:40px;padding-inline:.4em;
  border-radius:var(--r-sm);background:var(--accent);color:var(--accent-on);
  font-family:var(--font-display);letter-spacing:.02em;}
.brandcard__watch-label{font-family:var(--font-cond);text-transform:uppercase;letter-spacing:.08em;
  color:var(--c-text-dim);font-size:var(--fs-300);margin-top:var(--sp-1);}
```

**Verified card copy (doc 00 §1) — chips per promotion (US home in bold intent; label US vs Intl in copy):**
- **WWE** `data-promo="wwe"`: chips `Netflix (Raw)`, `USA Network (SmackDown)`, `The CW (NXT)`,
  `ESPN — US PLEs`, `Netflix — PLEs intl`. Line: "Raw streams on Netflix. SmackDown airs on USA Network.
  Premium Live Events run on ESPN in the US and Netflix internationally."
- **AEW** (reserved, cross-link card only): chips `TBS`, `TNT`, `HBO Max`, `AEW Plus / TrillerTV (intl)`.
- **NJPW** `data-promo="njpw"`: chips `NJPW World`, `TrillerTV`, `TV Asahi (Japan)`. (see HTML above)
- **TNA** `data-promo="tna"`: chips `AMC (live)`, `AMC+`, `TNA+`, `Prime Video (library)`. Line:
  "Thursday Night iMPACT airs on AMC and AMC+, with TNA+ for streaming and library seasons on Prime Video."
- **WCW / ECW** `data-promo="wcw"|"ecw"`: chip `WWE archive (Netflix)` with a `VERIFY` note (doc 00 §1
  flags the exact 2026 US archive host). Line: "Defunct promotion; library owned by WWE."

---

## 8. Section theming — HOF, Moments, Media, and the faceted hubs

Each new hub wraps its content in a `.theme-*` class from §4, so its rails, tile hovers, section-head
underline, eyebrow, and ghost buttons recolor to one accent. Layout is the dense poster wall
(`.grid-spot`) + a "Keep going" block (doc 01 B2) + JSON-LD (doc 01 Part C). Color rules per hub:

- **Hall of Fame `/hall-of-fame/` `.theme-hof`** (gold): hero panel = Ric Flair "most-decorated"
  with `.badge-hof badge-hof--2x`; a "Two-Time Club" rail (Michaels, Booker T, Scott Hall, Kevin Nash,
  Hulk Hogan); then a "Last 5 Classes" rail of class cards (2021–2025). Class cards use gold hairline
  edge (`.card--edge`), each inductee is a poster tile linking to a profile (or a GAP stub — §10).
- **Moments `/moments/` `.theme-moments`** (red): tiles carry `.tag-moment` (▸), 16:9 `.tile__media--wide`.
- **Media & Creators `/media/` `.theme-media`** (purple): Chris Van Vliet hero; grid of media tiles with
  `.chip--media`; every unverified name shows a small `VERIFY` note in the card body (do not print
  unverified affiliations as fact). Sami Zayn is NOT here — he stays on the wrestler grid (doc 00 §6).
- **Faceted wrestler hubs** `/wrestlers/current/` `.theme-current` (red), `/wrestlers/legends/`
  `.theme-legends` (gold), `/wrestlers/women/` `.theme-women` (magenta), `/wrestlers/men/` (neutral,
  no theme override). Each = dense `.grid-spot` of accent-tinted tiles → rail → keep-going block.

Rail color rule: a rail titled "More from {promotion}" sets `data-promo` on the rail element so its
header rule and tile accents match the promotion; a status/section rail uses the hub's `.theme-*`.

---

## 9. Interaction layers

- **Hover (pointer, ≥ fine):** tile lifts `translateY(-4px)`, accent ring, monogram tints to accent,
  radial spotlight follows cursor via `--mx/--my` (existing JS sets these; now accent-colored). Brand
  cards raise their gradient edge (`.card--edge:hover`). All ≤ 250ms, `--ease`.
- **Focus:** every tile/card is a single `<a>`; `:focus-visible` shows the 2px `--c-focus` ring
  (unchanged). Focus and hover states are visually distinct (ring vs lift+glow).
- **Touch / no-hover:** the hover fact/overlay is not required to read the tile — name, badges, and
  rating are always in normal flow, visible without hover (doc 01 B6). Spotlight simply no-ops.
- **Reduced motion:** covered by existing `@media (prefers-reduced-motion:reduce)` — pulse dot,
  transforms, and spotlight transitions collapse to near-instant. No parallax anywhere.
- **No JS dependency for meaning:** color/shape/text all render server-side in raw HTML (crawlable).
  JS only enhances (spotlight coordinates, ⌘K). Removing JS loses no information or navigation.

---

## 10. Clickable → link-target table

Every showcased clickable in the new/updated sections and its href. `EXISTS` = page already built under
`/root/wwe/`; `GAP` = must be built/stubbed so the clickable does not 404 (consolidated in §11).
Sources for who-links-where: doc 00 §2–§6, §8.

| # | Clickable (label) | Section / hub | Href | Status |
|---|---|---|---|---|
| 1 | Wrestlers | Nav / hub | `/wrestlers/` | EXISTS |
| 2 | Current | Nav → Wrestlers | `/wrestlers/current/` | GAP (facet hub) |
| 3 | Legends | Nav → Wrestlers | `/wrestlers/legends/` | GAP |
| 4 | Women's | Nav → Wrestlers | `/wrestlers/women/` | GAP |
| 5 | Men's | Nav → Wrestlers | `/wrestlers/men/` | GAP |
| 6 | Matches | Nav / hub | `/matches/` | EXISTS |
| 7 | Events | Nav / hub | `/events/` | EXISTS |
| 8 | Moments | Nav / hub | `/moments/` | EXISTS |
| 9 | Promotions | Nav / hub | `/promotions/` | EXISTS |
| 10 | Hall of Fame | Nav → More | `/hall-of-fame/` | GAP |
| 11 | Media & Creators | Nav → More | `/media/` | GAP |
| 12 | WWE | Promotions / brand card | `/promotions/wwe/` | EXISTS |
| 13 | WCW | Promotions / brand card | `/promotions/wcw/` | EXISTS |
| 14 | ECW | Promotions / brand card | `/promotions/ecw/` | EXISTS |
| 15 | TNA | Promotions / brand card | `/promotions/tna/` | EXISTS |
| 16 | NXT | Promotions / brand card | `/promotions/nxt/` | EXISTS |
| 17 | NJPW | Promotions / brand card | `/promotions/njpw/` | **GAP (build — Req 5)** |
| 18 | Ric Flair (most-decorated hero) | HOF | `/wrestlers/ric-flair/` | EXISTS |
| 19 | Shawn Michaels | HOF Two-Time Club | `/wrestlers/shawn-michaels/` | EXISTS |
| 20 | Booker T | HOF Two-Time Club | `/wrestlers/booker-t/` | EXISTS |
| 21 | Scott Hall | HOF Two-Time Club | `/wrestlers/razor-ramon/` | EXISTS |
| 22 | Kevin Nash | HOF Two-Time Club | `/wrestlers/kevin-nash/` | EXISTS |
| 23 | Hulk Hogan | HOF Two-Time Club | `/wrestlers/hulk-hogan/` | EXISTS |
| 24 | Triple H (2025 class) | HOF Last 5 Classes | `/wrestlers/triple-h/` | EXISTS |
| 25 | Lex Luger (2025) | HOF Last 5 Classes | `/wrestlers/lex-luger/` | EXISTS |
| 26 | Michelle McCool (2025) | HOF Last 5 Classes | `/wrestlers/michelle-mccool/` | GAP |
| 27 | Paul Heyman (2024) | HOF Last 5 Classes | `/wrestlers/paul-heyman/` | GAP |
| 28 | Rey Mysterio (2023) | HOF Last 5 Classes | `/wrestlers/rey-mysterio/` | EXISTS |
| 29 | The Great Muta (2023) | HOF Last 5 Classes | `/wrestlers/the-great-muta/` | GAP |
| 30 | The Undertaker (2022) | HOF Last 5 Classes | `/wrestlers/the-undertaker/` | EXISTS |
| 31 | Vader (2022) | HOF Last 5 Classes | `/wrestlers/vader/` | EXISTS |
| 32 | Kane (2021) | HOF Last 5 Classes | `/wrestlers/kane/` | EXISTS |
| 33 | Rob Van Dam (2021) | HOF Last 5 Classes | `/wrestlers/rob-van-dam/` | GAP |
| 34 | Eric Bischoff (2021) | HOF Last 5 Classes | `/wrestlers/eric-bischoff/` | GAP |
| 35 | AJ Styles (hero) | AJ Styles / NJPW showcase | `/wrestlers/aj-styles/` | EXISTS |
| 36 | Shinsuke Nakamura | NJPW / Bullet Club rail | `/wrestlers/shinsuke-nakamura/` | EXISTS |
| 37 | Jon Moxley | NJPW rail | `/wrestlers/jon-moxley/` | EXISTS |
| 38 | Finn Balor | NJPW / Bullet Club rail | `/wrestlers/finn-balor/` | EXISTS |
| 39 | Kenny Omega | NJPW / Bullet Club rail | `/wrestlers/kenny-omega/` | GAP |
| 40 | Will Ospreay | NJPW rail | `/wrestlers/will-ospreay/` | GAP |
| 41 | Chris Van Vliet (hero) | Media & Creators | `/media/chris-van-vliet/` | GAP |
| 42 | Renee Paquette | Media & Creators | `/media/renee-paquette/` | GAP (VERIFY) |
| 43 | Peter Rosenberg | Media & Creators | `/media/peter-rosenberg/` | GAP (VERIFY) |
| 44 | Ariel Helwani | Media & Creators | `/media/ariel-helwani/` | GAP (VERIFY) |
| 45 | Sean Ross Sapp | Media & Creators | `/media/sean-ross-sapp/` | GAP (VERIFY) |
| 46 | Denise Salcedo | Media & Creators | `/media/denise-salcedo/` | GAP (VERIFY) |
| 47 | Sami Zayn (cross-note, NOT in media) | Wrestler grid | `/wrestlers/sami-zayn/` | EXISTS |
| 48 | Platform chips (Netflix/ESPN/HBO Max/NJPW World/TNA+/AMC/The CW/Prime Video) | Brand cards | none (text only, non-link) | n/a — avoids trademark logos |
| 49 | Streaming brand-card → events anchor | Brand cards | `/promotions/{slug}/#events` | EXISTS (except njpw = GAP) |

Event separation (Req 3) reuses existing pages; the new facet routes are hubs to build:
`/events/2026/`, `/events/wwe/`, `/events/wrestlemania/` (series) — all GAP hubs pointing at the 10
existing event pages under `/events/`.

---

## 11. Gap list — pages a clickable above targets that do not exist yet

Build or stub these so no showcased clickable 404s (mirrors doc 00 §8; add facet hubs):
- **Promotion:** `/promotions/njpw/` (Req 5, required).
- **Faceted wrestler hubs:** `/wrestlers/current/`, `/legends/`, `/women/`, `/men/`.
- **Section hubs:** `/hall-of-fame/`, `/media/`, event facets `/events/2026/`, `/events/wwe/`, `/events/wrestlemania/`.
- **HOF inductee profiles missing:** Michelle McCool, Paul Heyman, The Great Muta, Rob Van Dam, Eric Bischoff.
- **NJPW/Bullet Club stars missing:** Kenny Omega, Will Ospreay.
- **Media profiles (all new):** Chris Van Vliet (hero, HIGH), Renee Paquette, Peter Rosenberg, Ariel
  Helwani, Sean Ross Sapp, Denise Salcedo (all `VERIFY` affiliation before publishing).
- Until a GAP profile exists, the HOF/NJPW/Media tile should link to the hub anchor (e.g.
  `/hall-of-fame/#class-2024`) rather than a dead profile URL, so the wall stays fully navigable.

---

## 12. Implementation checklist (for the CSS build)

1. Add §2.2 tokens to `site.css` `:root` (additive; no existing hex changed).
2. Add §4 `[data-promo]` and `.theme-*` accent scopes.
3. Refactor `.tile__media` gradient, `.tile:hover` ring, `.tile__mono`, `.tile__spot`, `.tile__kicker`
   to read `--accent` (§6); add `.tile__badges` positioner and NJPW rising-sun overlay.
4. Add §5.2 badge/chip classes; extend the existing `.chip--*` promotion set with `.chip--njpw`,
   `.chip--media`.
5. Add §7 `.brandcard*` classes.
6. Verify every fill/text pairing against §3 (AA) in a contrast checker before commit; NJPW red and any
   `VERIFY`-flagged copy stay flagged until confirmed.
7. Keep everything crawlable: color/shape/text render in raw HTML; JS only sets `--mx/--my` and ⌘K.

---

## Appendix — the color legend (ship as a small on-site "key")

A tiny legend block (on hubs / an /about/style page) teaches the grammar in one glance, reinforcing
"instantly parseable": red pulse = Current · gold hairline = Legend · magenta = Women's · gold plaque =
Hall of Fame · ▸ red = Moment · purple = Media & Creators · color bar = promotion (WWE crimson, WCW
gold, ECW silver, TNA blue, NXT yellow, NJPW red + white sun).
