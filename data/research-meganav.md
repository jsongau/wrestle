# Mega-Navigation Design Research — MAT (The Ultimate Pro Wrestling Database)

> Scope: distinct mega-nav **archetypes** with copy-ready HTML/CSS technique for a
> premium **dark "arena"** site. Static HTML/CSS/vanilla JS, no framework, no build,
> **no browser storage**. Palette: gold `#d4af37`, red `#e11d2a`; fonts Anton/Oswald/Inter.
> All snippets are written against the existing MAT design tokens (`--c-gold`,
> `--c-red`, `--font-cond`, `--fs-*`, `--sp-*`, `--r-*`, `--ease`, `--dur`) so they
> drop into `css/site.css` and `js/main.js` with minimal glue.
>
> This report is a companion to `data/ux-research-nav-ia-search.md` (IA, search,
> facets). That file covers *what goes in the nav*; this file covers *how the
> mega-panel looks, moves, and behaves* across three build-ready archetypes.

---

## 0. Grounding: what MAT ships today

Current header (`index.html` L48–86) + CSS (`css/site.css` L80–130):

- A sticky, blurred `.site-header` with a horizontal `.nav__menu`.
- Two hover/focus mega panels: **Wrestlers** (`.mega.mega--wide`, 3 columns:
  *By Promotion*, spillover column, *Featured*) and **Matches** (`.mega`, 2
  columns: *Explore*, *Editors' Picks*).
- Plain links for Rivalries, Relationships, Rankings, 中文, and a red `.nav__cta`
  → `/membership/`.
- Panels open on `:hover`/`:focus-within` (desktop) and on **click** below 900px
  via `main.js`. No hover-intent delay, no `Esc` handling, no focus return.

**Real routes to wire into any archetype:**
`/wrestlers/` · `/matches/` · `/rivalries/` · `/relationships/` · `/rankings/` ·
`/promotions/wwe/` · `/promotions/wcw/` · `/promotions/ecw/` · `/promotions/tna/` ·
`/promotions/nxt/` · `/membership/` · `/zh/`.

**Three accessibility gaps in the current markup to fix while re-skinning** (see §5):
1. `aria-expanded` and `aria-haspopup` sit on the **`<a>`** links. Per Roselli, a
   link that also toggles a panel confuses SR users — the destination and the
   disclosure toggle should be separate affordances (link + `<button>`).
2. Panels are **hover-only** on desktop; keyboard users get `:focus-within` but
   there is no `Esc`-to-close or focus return.
3. No hover-intent delay → panels flicker when the pointer crosses siblings
   (Baymard's most common mega-menu defect).

---

## 1. Cross-archetype principles (evidence base)

These hold for **every** archetype below; the per-archetype sections only add
what's specific.

- **Group into scannable, labeled columns — never a wall of links.** NN/g: mega
  menus can carry 2–3 tiers well *if* grouped under clear headings; images/icons
  are *supportive*, never a replacement for text labels. [NN/g]
- **Hover-intent delay of ~300–500 ms.** Baymard found **61 % of sites** open
  panels with zero delay, causing flicker as the pointer crosses siblings; a
  300–500 ms intent delay (open **and** close) is the single highest-value fix.
  [Baymard]
- **Treat click/tap as first-class; never hover-only.** Hover excludes touch and
  keyboard users and mis-fires. NN/g and Level Access both recommend
  click-activation as the primary contract, with hover as progressive
  enhancement. [NN/g, 216digital]
- **Use link + disclosure-button, not `role="menu"`.** For *site navigation*
  (not an app menu), `role="menu"/"menuitem"` forces AT into application mode and
  obliges you to implement arrow-key roving focus. Roselli's recommended pattern:
  real `<a>` for the destination + a sibling `<button aria-expanded>` for the
  toggle, inside a plain `<nav><ul>`. Tab moves through links; `Esc` closes.
  [Roselli, MakeThingsAccessible]
- **Clickable section headers.** Baymard: make column headers real parent-category
  links (e.g. the *WWE* heading → `/promotions/wwe/`), not inert text.
- **Show current scope.** Baymard: **95 %** of sites fail to highlight the user's
  current section; mark it with `aria-current="page"` + a gold underline.
- **Thumbnails as visual labels.** Baymard: **55 %** of sites omit representative
  thumbnails; when used, keep them small and instantly interpretable.
- **Respect `prefers-reduced-motion`.** MAT already zeroes transitions under the
  reduce query (`site.css` L45); every animation below must degrade to instant.

Sources are consolidated in §7.

---

## 2. Archetype A — Full-width columned mega panel with featured cards

The workhorse. A wide, edge-to-edge (or wrap-width) panel of labeled link
columns, anchored by 1–2 **featured cards** with thumbnail + kicker + title.
This is a direct, premium evolution of MAT's existing `.mega--wide`.

### When to use
- Broad sections with many equally-important children: **Wrestlers** (by
  promotion + featured roster) and **Matches** (explore + editors' picks). This
  is the default for MAT's two deepest hubs.
- When you want to surface *editorial* picks (5★ matches, marquee wrestlers)
  beside utilitarian A–Z links.

### Layout & structure
- Grid: 3–4 link columns + 1 wider "featured" rail. On MAT tokens:
  `grid-template-columns: repeat(3, minmax(150px,1fr)) 1.4fr;`
- Each column = a clickable `<h3>` header (parent route) + a short list. Cap
  each list at ~6 items (Baymard: users overwhelmed past ~10).
- Featured rail = one or two `.mega-card`s: 16:10 thumbnail, gold kicker
  ("5★ MATCH"), title, one-line dek.
- Full-bleed option: let the panel span the viewport width but constrain inner
  content to `--wrap` (1200px) so it reads as a broadcast lower-third band.

```html
<!-- Replace the current Wrestlers <li> body. Link + disclosure button. -->
<li class="nav__item" data-mega>
  <a class="nav__link" href="/wrestlers/">Wrestlers</a>
  <button class="nav__disc" type="button"
          aria-expanded="false" aria-controls="mega-wrestlers"
          aria-label="Open Wrestlers menu"></button>

  <div class="mega mega--full" id="mega-wrestlers" role="group"
       aria-label="Wrestlers">
    <div class="mega__inner wrap">
      <nav class="mega__cols" aria-label="Browse wrestlers">
        <div class="mega__col">
          <h3><a href="/promotions/wwe/">WWE / WWF</a></h3>
          <a class="mega__link" href="/wrestlers/stone-cold-steve-austin/">Stone Cold</a>
          <a class="mega__link" href="/wrestlers/the-undertaker/">The Undertaker</a>
          <a class="mega__link" href="/wrestlers/roman-reigns/">Roman Reigns</a>
        </div>
        <div class="mega__col">
          <h3><a href="/promotions/wcw/">WCW</a></h3>
          <a class="mega__link" href="/promotions/wcw/">Sting, Goldberg, nWo…</a>
          <h3 class="mt"><a href="/promotions/ecw/">ECW</a></h3>
          <a class="mega__link" href="/promotions/ecw/">Foley, RVD, Sabu…</a>
        </div>
        <div class="mega__col">
          <h3><a href="/promotions/tna/">TNA / Impact</a></h3>
          <a class="mega__link" href="/promotions/tna/">AJ Styles, Samoa Joe…</a>
          <h3 class="mt"><a href="/promotions/nxt/">NXT</a></h3>
          <a class="mega__link" href="/wrestlers/">All wrestlers A–Z →</a>
        </div>
      </nav>

      <a class="mega-card" href="/wrestlers/becky-lynch/">
        <span class="mega-card__media" aria-hidden="true"></span>
        <span class="mega-card__kick">FEATURED</span>
        <span class="mega-card__title">Becky Lynch</span>
        <span class="mega-card__dek">The Man — championship résumé & rivalries</span>
      </a>
    </div>
  </div>
</li>
```

```css
/* Full-bleed band that still aligns inner content to the 1200px wrap */
.mega--full{
  position:absolute; left:50%; transform:translateX(-50%) translateY(6px);
  top:calc(100% + 6px); width:min(100vw,1280px);
  background:var(--c-bg-elev-1); border:1px solid var(--c-line-strong);
  border-radius:var(--r-lg); box-shadow:var(--shadow-2);
  opacity:0; visibility:hidden;
  transition:opacity var(--dur) var(--ease), transform var(--dur) var(--ease), visibility var(--dur);
}
.mega--full[data-open]{ opacity:1; visibility:visible; transform:translateX(-50%) translateY(0); }
.mega__inner{ display:grid; grid-template-columns:repeat(3,minmax(150px,1fr)) 1.4fr;
  gap:var(--sp-5) var(--sp-6); padding:var(--sp-6); }
.mega__cols{ display:contents; }              /* let columns sit on the parent grid */
.mega__col h3{ font-family:var(--font-cond); text-transform:uppercase;
  letter-spacing:.06em; font-size:var(--fs-300); margin-bottom:var(--sp-2);
  border-bottom:1px solid var(--c-line); padding-bottom:var(--sp-1); }
.mega__col h3 a{ color:var(--c-gold); text-decoration:none; }
.mega__col h3.mt{ margin-top:var(--sp-4); }
.mega__link{ display:block; padding:.4em .5em; border-radius:var(--r-sm);
  color:var(--c-text-muted); text-decoration:none; }
.mega__link:hover{ background:var(--c-bg-elev-2); color:var(--c-text); }
.mega__link[aria-current="page"]{ color:var(--c-gold-bright);
  box-shadow:inset 2px 0 0 var(--c-gold); }

/* Featured card */
.mega-card{ display:grid; align-content:start; gap:.25rem; padding:var(--sp-3);
  background:var(--c-bg-elev-2); border:1px solid var(--c-line);
  border-radius:var(--r-md); text-decoration:none; color:var(--c-text);
  transition:border-color var(--dur) var(--ease), transform var(--dur) var(--ease); }
.mega-card:hover{ border-color:var(--c-gold-dim); transform:translateY(-2px); }
.mega-card__media{ display:block; aspect-ratio:16/10; border-radius:var(--r-sm);
  /* seedable diagonal gradient stand-in until real art is wired */
  background:linear-gradient(135deg,color-mix(in oklab,var(--c-gold) 45%,#000),#0c0d10);
  margin-bottom:var(--sp-2); }
.mega-card__kick{ font-family:var(--font-cond); font-size:var(--fs-300);
  letter-spacing:.12em; color:var(--c-gold); }
.mega-card__title{ font-family:var(--font-cond); font-size:var(--fs-500);
  text-transform:uppercase; }
.mega-card__dek{ color:var(--c-text-dim); font-size:var(--fs-300); }
```

### Interaction & motion
- Open on **click** of `.nav__disc` (primary); enhance with **hover-intent** on
  the `.nav__item` (300 ms open / 200 ms close, §5 JS).
- Motion: fade + 6px rise (`transform:translateY`), 180 ms `--ease`. Keep it
  subtle — this is a broadcast overlay, not a bounce. Optionally stagger column
  reveal with a 20–30 ms CSS delay per column, but only above `prefers-reduced-motion`.
- Full-bleed panels benefit from a faint top hairline in gold
  (`box-shadow:inset 0 1px 0 var(--c-gold-dim)`) to echo the header underline.

### Mobile behavior (< 900px)
- Panel becomes an in-flow **accordion** under the tapped item (MAT already does
  this via `.mega{position:static;display:none}` → `.is-open{display:grid}`).
- Collapse to a single column; the featured card drops to the bottom, full-width,
  thumbnail on top.
- Include full scope in labels ("All wrestlers A–Z", not "All") — Baymard.

### Accessibility
- Markup: `<a>` (destination) + sibling `<button aria-expanded aria-controls>`
  (toggle). No `role="menu"`. [Roselli]
- Keyboard: Tab reaches the link, then the disclosure button; `Enter`/`Space`
  toggles; `Tab` continues into the panel's links; `Esc` closes and returns focus
  to the disclosure button. [216digital, APG disclosure]
- **No focus trap** — a nav disclosure is not a modal; users must be able to Tab
  straight out. (Focus trapping is reserved for Archetype C's overlay.)
- Section headers are real links, so SR users can jump to `/promotions/wwe/`
  directly. Mark the active section with `aria-current="page"`.
- Hover-intent delay must not gate keyboard/click opening — those are instant.

### Apply to MAT
This is the **primary retrofit** of the existing `.mega--wide` (Wrestlers) and
`.mega` (Matches) panels. Concretely:
- **Wrestlers** → 3 promotion columns (WWE/WCW/ECW, TNA/NXT, All A–Z) + one
  featured wrestler card. Headers link to `/promotions/{wwe,wcw,ecw,tna,nxt}/`.
- **Matches** → columns *Explore* (`/matches/`, `/rankings/` "5★ club") and
  *Editors' Picks* (2–3 curated `/matches/{slug}/`) + a featured 5★ match card
  (e.g. `/matches/undertaker-vs-hbk-wm25/`) with a "5★ MATCH" gold kicker.

---

## 3. Archetype B — Image/poster-rich cinematic flyout

A visually dominant panel where **large imagery leads** and links are secondary:
poster tiles, hero portraits, or a split hero-image + link-list. This is the
Netflix/Nike/UFC register — emotional, scannable-by-picture, on-brand for a
"premium dark arena."

### When to use
- Sections where the *entity is the draw* and a face/poster communicates faster
  than a label: **Rivalries** (dramatic two-face split posters) and a promotion
  switcher (WWE/WCW/ECW/TNA/NXT logo-lockup tiles).
- Marketing-forward moments (a Rivalry-of-the-month promo). Not for dense A–Z
  utility lists — those stay in Archetype A.

### Layout & structure
- **Poster grid:** 3–5 tiles, each `aspect-ratio:3/4` (wrestler) or `16/9`
  (match/rivalry), with a bottom-anchored gradient scrim + title. Baymard: every
  image must be a *single hit area* and lead to the products/entities it depicts.
- **Split flyout (alt):** left = one large cinematic hero image (~55 %), right =
  a tidy link list. Good for a "spotlight rivalry + related links" combo.
- Keep the panel to `--wrap` width or full-bleed band; imagery does the heavy
  lifting so keep link density low.

```html
<li class="nav__item" data-mega>
  <a class="nav__link" href="/rivalries/">Rivalries</a>
  <button class="nav__disc" type="button" aria-expanded="false"
          aria-controls="mega-riv" aria-label="Open Rivalries menu"></button>

  <div class="mega mega--posters" id="mega-riv" role="group" aria-label="Rivalries">
    <div class="mega__inner wrap">
      <a class="poster" href="/rivalries/austin-vs-mcmahon/">
        <span class="poster__img" aria-hidden="true"
              style="--seed:12"></span>
        <span class="poster__meta">
          <span class="poster__kick">FEUD</span>
          <span class="poster__title">Austin vs. McMahon</span>
        </span>
      </a>
      <a class="poster" href="/rivalries/hbk-vs-bret-hart/">
        <span class="poster__img" aria-hidden="true" style="--seed:280"></span>
        <span class="poster__meta">
          <span class="poster__kick">FEUD</span>
          <span class="poster__title">HBK vs. Bret Hart</span>
        </span>
      </a>
      <a class="poster" href="/rivalries/cena-vs-punk/">
        <span class="poster__img" aria-hidden="true" style="--seed:150"></span>
        <span class="poster__meta">
          <span class="poster__kick">FEUD</span>
          <span class="poster__title">Cena vs. CM Punk</span>
        </span>
      </a>
      <a class="poster poster--all" href="/rivalries/">
        <span class="poster__title">All rivalries →</span>
      </a>
    </div>
  </div>
</li>
```

```css
.mega--posters{ /* same open/close mechanics as .mega--full */ }
.mega--posters .mega__inner{ display:grid;
  grid-template-columns:repeat(4,1fr); gap:var(--sp-4); padding:var(--sp-6); }
.poster{ position:relative; display:block; aspect-ratio:16/9; overflow:hidden;
  border-radius:var(--r-md); border:1px solid var(--c-line);
  text-decoration:none; color:#fff;
  transition:transform var(--dur) var(--ease), border-color var(--dur) var(--ease); }
.poster:hover{ transform:translateY(-3px); border-color:var(--c-gold-dim); }
.poster__img{ position:absolute; inset:0;
  background:linear-gradient(calc(var(--seed,220)*1deg),
    color-mix(in oklab,var(--c-red) 50%,#000), #0b0c0f 70%);
  transition:transform 400ms var(--ease); }
.poster:hover .poster__img{ transform:scale(1.06); }   /* slow Ken-Burns push */
.poster::after{ content:""; position:absolute; inset:0;
  background:linear-gradient(to top,rgba(0,0,0,.85) 8%,transparent 55%); }
.poster__meta{ position:absolute; left:var(--sp-3); bottom:var(--sp-3); z-index:1;
  display:grid; gap:2px; }
.poster__kick{ font-family:var(--font-cond); font-size:var(--fs-300);
  letter-spacing:.14em; color:var(--c-gold-bright); }
.poster__title{ font-family:var(--font-cond); font-size:var(--fs-500);
  text-transform:uppercase; line-height:var(--lh-tight); }
.poster--all{ display:grid; place-content:center; aspect-ratio:16/9;
  background:var(--c-bg-elev-2); }
.poster--all::after{ display:none; }
@media (prefers-reduced-motion:reduce){
  .poster:hover .poster__img{ transform:none; }
  .poster:hover{ transform:none; }
}
```

### Interaction & motion
- Signature move: a **slow scale/Ken-Burns push** on the image (scale 1.0→1.06
  over ~400 ms) + a 3px card lift on hover. Restrained — one accent, not many.
- Panel entrance: same fade+rise as Archetype A. Optionally a very light
  parallax on pointer-move reusing MAT's existing hero-parallax approach from
  `enhance.js` (bail under reduced-motion / coarse pointer).
- Because images are heavy, **lazy-load real art** (`loading="lazy"`,
  `decoding="async"`) and keep a CSS gradient placeholder (MAT already uses
  seedable gradients via `--seed`, see `.tile--gold` in `site.css`) so the panel
  never opens to empty boxes.

### Mobile behavior
- Collapse the poster grid to a **1- or 2-column** stack inside the accordion;
  keep `aspect-ratio` so posters stay cinematic. Titles overlay stays legible via
  the scrim. Ensure each poster is one large tap target (≥44px, Baymard/NN/g).
- Consider a horizontal **snap-scroll** row of posters on mobile as an
  alternative to a tall stack (`overflow-x:auto; scroll-snap-type:x mandatory`).

### Accessibility
- Same link + disclosure-button structure and `Esc` behavior as Archetype A.
- The decorative gradient/image layer is `aria-hidden`; the **accessible name
  comes from the visible title text**, so each poster is a self-describing link.
- Do not rely on color/image alone — the gold kicker + title text carry meaning
  for low-vision and SR users. Maintain scrim contrast so overlaid white text
  clears 4.5:1 on the busiest image region.
- Provide real `alt` when swapping in photographs (wrestler/feud name), not
  filenames.

### Apply to MAT
- **Rivalries** becomes a cinematic 4-poster flyout: 3 marquee feuds (16:9 split
  scrim posters) + an "All rivalries →" tile → `/rivalries/`. Wire real feud art
  later; ship with `--seed` gradients now (red-biased to signal conflict).
- **Promotions switcher** (new top-level or nested under Wrestlers): five tiles
  for `/promotions/{wwe,wcw,ecw,tna,nxt}/` using each promotion's accent token
  already defined in `site.css` (`--c-wwe`, `--c-wcw`, `--c-ecw`, `--c-tna`,
  `--c-nxt`) as the tile gradient hue — instantly branded, zero image assets.

---

## 4. Archetype C — Command-palette / search-first overlay (⌘K)

A centered, modal search overlay (Linear/Vercel register) that fuses **global
search + navigation + actions**. Instead of hovering menus, the user hits ⌘K
(Ctrl+K) or clicks a search affordance and *types* to jump anywhere: a wrestler,
a match, a promotion, a route.

### When to use
- As a **complement**, not a replacement, to the visual mega panels — this is the
  power-user express lane and simultaneously **fills MAT's biggest gap: there is
  no global search today** (flagged in `ux-research-nav-ia-search.md` §3). One
  component solves both.
- Ideal for a large entity database (40+ wrestlers, 30+ matches, rivalries,
  promotions) where typing a name beats drilling menus.

### Layout & structure
- A dimmed backdrop + a centered card (~560–640px wide, top-anchored ~12vh).
- Structure: search `<input role="combobox">` at top → grouped result
  `role="listbox"` below (groups: *Wrestlers*, *Matches*, *Rivalries*,
  *Promotions*, *Pages/Actions*). [UX Patterns, cmdk]
- Each row: small avatar/thumb + primary label + muted context (e.g. "WWE ·
  16-time champ") + optional `↵` hint. Cap visible rows (~8–10) and scroll.
- **Static index, no storage:** since MAT bans browser storage, ship a small
  in-page JS array (or inline `<script type="application/json">`) of
  `{title, url, type, tags}` built at author time from the roster/match set. No
  network, no localStorage — pure in-memory filtering.

```html
<!-- Trigger lives in the header, replacing/《beside》the current search gap -->
<button class="cmdk-trigger" type="button" aria-keyshortcuts="Meta+K Control+K"
        aria-haspopup="dialog" aria-controls="cmdk">
  <span aria-hidden="true">⌕</span> Search…
  <kbd class="cmdk-kbd">⌘K</kbd>
</button>

<!-- Overlay (hidden until opened). Use <dialog> for free focus containment. -->
<dialog class="cmdk" id="cmdk" aria-label="Search MAT">
  <div class="cmdk__box">
    <input class="cmdk__input" type="text" role="combobox"
           aria-expanded="true" aria-controls="cmdk-list"
           aria-activedescendant="" autocomplete="off"
           placeholder="Search wrestlers, matches, rivalries…" />
    <ul class="cmdk__list" id="cmdk-list" role="listbox" aria-label="Results">
      <li class="cmdk__group" role="presentation">Wrestlers</li>
      <li id="r1" class="cmdk__opt" role="option" data-url="/wrestlers/stone-cold-steve-austin/">
        <span class="cmdk__title">Stone Cold Steve Austin</span>
        <span class="cmdk__ctx">WWE · Attitude Era</span>
      </li>
      <!-- …rendered from the in-memory index… -->
    </ul>
    <p class="cmdk__empty" hidden>No matches. Try “Undertaker”, “WrestleMania”, “nWo”.</p>
  </div>
</dialog>
```

```css
.cmdk-trigger{ display:inline-flex; align-items:center; gap:.5em;
  padding:.5em .8em; background:var(--c-bg-elev-2); border:1px solid var(--c-line);
  border-radius:var(--r-pill); color:var(--c-text-muted); cursor:pointer; }
.cmdk-trigger:hover{ color:var(--c-text); border-color:var(--c-line-strong); }
.cmdk-kbd,.cmdk__opt kbd{ font-family:var(--font-mono); font-size:var(--fs-300);
  background:var(--c-bg-elev-3); border:1px solid var(--c-line);
  border-radius:var(--r-sm); padding:0 .35em; color:var(--c-text-dim); }

.cmdk{ width:min(92vw,620px); margin:12vh auto auto; padding:0; border:0;
  background:transparent; }
.cmdk::backdrop{ background:rgba(0,0,0,.6); backdrop-filter:blur(4px); }
.cmdk__box{ background:var(--c-bg-elev-1); border:1px solid var(--c-line-strong);
  border-radius:var(--r-lg); box-shadow:var(--shadow-2); overflow:hidden;
  /* subtle gold rim to match arena theme */
  box-shadow:var(--shadow-2),0 0 0 1px var(--c-gold-dim); }
.cmdk__input{ width:100%; padding:var(--sp-4) var(--sp-5); font-size:var(--fs-500);
  background:transparent; border:0; border-bottom:1px solid var(--c-line);
  color:var(--c-text); }
.cmdk__input:focus{ outline:none; }
.cmdk__list{ list-style:none; margin:0; padding:var(--sp-2); max-height:56vh;
  overflow-y:auto; }
.cmdk__group{ font-family:var(--font-cond); text-transform:uppercase;
  letter-spacing:.1em; font-size:var(--fs-300); color:var(--c-gold);
  padding:var(--sp-2) var(--sp-2) var(--sp-1); }
.cmdk__opt{ display:flex; align-items:center; gap:.75em; padding:.55em .6em;
  border-radius:var(--r-sm); cursor:pointer; }
.cmdk__opt[aria-selected="true"]{ background:var(--c-bg-elev-2); }
.cmdk__opt[aria-selected="true"] .cmdk__title{ color:var(--c-gold-bright); }
.cmdk__ctx{ margin-left:auto; color:var(--c-text-dim); font-size:var(--fs-300); }
.cmdk__empty{ padding:var(--sp-5); color:var(--c-text-dim); text-align:center; }
@media (prefers-reduced-motion:no-preference){
  .cmdk[open]{ animation:cmdk-in 160ms var(--ease); }
  @keyframes cmdk-in{ from{opacity:0; transform:translateY(-6px) scale(.98);} }
}
```

```js
// Minimal, storage-free wiring. Pair with an in-memory INDEX array.
(function(){
  var dlg = document.getElementById('cmdk');
  var input = dlg && dlg.querySelector('.cmdk__input');
  var list = document.getElementById('cmdk-list');
  var trigger = document.querySelector('.cmdk-trigger');
  if (!dlg || !input) return;
  var opts = [], active = -1;

  function open(){ if (!dlg.open){ dlg.showModal(); input.value=''; render(''); input.focus(); } }
  function close(){ if (dlg.open) dlg.close(); }              // <dialog> returns focus to trigger

  trigger && trigger.addEventListener('click', open);
  document.addEventListener('keydown', function(e){
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase()==='k'){ e.preventDefault(); open(); }
  });

  input.addEventListener('input', function(){ render(input.value); });
  input.addEventListener('keydown', function(e){
    if (e.key==='ArrowDown'){ e.preventDefault(); move(1); }
    else if (e.key==='ArrowUp'){ e.preventDefault(); move(-1); }
    else if (e.key==='Enter'){ e.preventDefault(); go(); }
    else if (e.key==='Escape'){ close(); }
  });
  // click a result
  list.addEventListener('click', function(e){
    var li = e.target.closest('.cmdk__opt'); if (li && li.dataset.url) location.href = li.dataset.url;
  });

  function render(q){ /* filter window.MAT_INDEX by q, group by type, build <li role=option> */ }
  function move(d){ /* update active, set aria-selected + aria-activedescendant, scroll into view */ }
  function go(){ var li = opts[active]; if (li) location.href = li.dataset.url; }
})();
```

### Interaction & motion
- **Open:** ⌘K / Ctrl+K anywhere, or click the header pill. Instant focus into
  the input.
- **Keys:** ↑/↓ move the active row, `Enter` navigates, `Esc` closes.
  [UX Patterns, cmdk]
- Focus stays in the input; the highlighted row is tracked via
  `aria-activedescendant` (combobox pattern) — **do not** move DOM focus row to
  row. [UX Patterns]
- Motion: 160 ms fade + slight scale-in of the card; backdrop blur. Nothing more.
- **States to design:** empty (before typing → show *Recent/Popular* or top
  wrestlers), no-results (with suggested queries), and typing (live filter).
  [UX Patterns] Since there's no storage, "Recent" = a static "Popular" list.

### Mobile behavior
- The overlay becomes near-full-screen: input pinned top, results fill the
  viewport, generous 44px+ rows. The ⌘K hint is hidden (`kbd` display:none on
  touch); the trigger is a search icon in the header. Software keyboard pushes
  the list; keep the input sticky at top.

### Accessibility
- Use native **`<dialog>` + `showModal()`**: it gives you a **real focus trap and
  focus return** for free (focus goes back to the trigger on close) — no custom
  trap code, which is exactly what you *do* want here (unlike the nav
  disclosures, an overlay *should* trap). [APG/native]
- Input is `role="combobox"` with `aria-expanded`, `aria-controls` → the
  `role="listbox"`; rows are `role="option"` with `aria-selected`; the active row
  is pointed to by `aria-activedescendant`. [UX Patterns, cmdk]
- Announce result counts / empty / loading via a polite live region.
- `Esc` closes; `<dialog>` handles backdrop click + Esc, but keep the explicit
  `Escape` handler for the row-highlight reset case.
- Expose the shortcut with `aria-keyshortcuts="Meta+K Control+K"` on the trigger.

### Apply to MAT
Build a single `window.MAT_INDEX` array (authored, in-memory — respects the
no-storage rule) covering every `/wrestlers/{slug}/`, `/matches/{slug}/`,
`/rivalries/{slug}/`, and the five `/promotions/{…}/` hubs, each tagged with
type + aliases/nicknames ("The Man" → Becky, "The Rattlesnake" → Austin) so
alias search works (a requirement from the nav-IA research §3.3). Add a header
search pill (currently missing) that opens the palette; this doubles as MAT's
global search entry point. Include a *Pages/Actions* group for `/rankings/`,
`/membership/`, and the `/zh/` language switch.

---

## 5. Shared enhancement: hover-intent + Esc for the disclosure panels (A & B)

Both visual archetypes need the same small, storage-free JS layer. This replaces
the current hover-only CSS behavior and the link-mounted `aria-expanded`.

```js
// Progressive enhancement for [data-mega] items: click-to-toggle (button),
// hover-intent on desktop, Esc to close, click-outside to close.
(function(){
  var OPEN_DELAY = 320, CLOSE_DELAY = 220;                 // Baymard 300–500ms range
  var fine = matchMedia('(hover:hover) and (pointer:fine)').matches;
  document.querySelectorAll('[data-mega]').forEach(function(item){
    var btn = item.querySelector('.nav__disc');
    var panel = item.querySelector('.mega');
    if (!btn || !panel) return;
    var t;
    function set(open){ btn.setAttribute('aria-expanded', open?'true':'false');
      panel.toggleAttribute('data-open', open); }
    btn.addEventListener('click', function(){ set(btn.getAttribute('aria-expanded')!=='true'); });
    if (fine){
      item.addEventListener('pointerenter', function(){ clearTimeout(t); t=setTimeout(function(){set(true);}, OPEN_DELAY); });
      item.addEventListener('pointerleave', function(){ clearTimeout(t); t=setTimeout(function(){set(false);}, CLOSE_DELAY); });
    }
    item.addEventListener('keydown', function(e){ if (e.key==='Escape'){ set(false); btn.focus(); } });
  });
  document.addEventListener('click', function(e){
    if (e.target.closest('[data-mega]')) return;
    document.querySelectorAll('[data-mega] .mega[data-open]').forEach(function(p){
      p.removeAttribute('data-open');
      p.parentElement.querySelector('.nav__disc').setAttribute('aria-expanded','false');
    });
  });
})();
```

Notes:
- Uses a `data-open` attribute (not `.is-open`) so the CSS `[data-open]` selectors
  above drive visibility; keep the old `.is-open` mobile path or migrate it.
- Delays apply to **hover only**; click and keyboard are always instant (NN/g).
- No storage, no dependencies — fits MAT's constraints and mirrors the existing
  `main.js` style.

---

## 6. Secondary patterns (use inside A/B, not as standalone top-levels)

### 6.1 Tabbed mega panel
Vertical tabs on the left switch the right-hand content **without closing** the
panel — good when one section spans several distinct sub-worlds. Examples:
Atlassian, Asana, Microsoft. [Banana Produced]
- **MAT fit:** a single "Browse" mega with left tabs *Wrestlers / Matches /
  Rivalries / Promotions*, each tab swapping in that section's columns or
  posters. Reduces the top bar to fewer items — supports the "don't grow the bar"
  rule from the nav-IA research.
- **A11y:** this *is* a legitimate `role="tablist"`/`role="tab"`/`role="tabpanel"`
  case (arrow-key roving within the tablist), distinct from the nav disclosure —
  but only inside an already-open panel, and still avoid `role="menu"`.
- **Motion:** cross-fade the tabpanel (120–160 ms); never slide the whole panel.

### 6.2 Bento mega panel
An asymmetric grid mixing tile sizes (one large hero tile + several small link
tiles + a stat tile), Apple/Linear-marketing register. Premium, editorial,
low-density. [Banana Produced: "Minimal" — Apple/Stripe/Notion]
- **MAT fit:** a "Featured" mega combining a large *Rivalry of the Month* poster
  (2×2), a *5★ Match* card, a *#1 ranked wrestler* stat tile pulling MAT's
  count-up stat style, and 3–4 quick links. Great for the homepage-adjacent
  "discovery" entry.
- **Build:** `display:grid; grid-template-columns:repeat(4,1fr); grid-auto-rows:
  minmax(96px,auto);` with `grid-column/row: span N` on hero tiles. Reuse
  `.tile--gold` gradient + `--seed` from `site.css`; reuse `[data-count]` from
  `enhance.js` for the stat tile.
- **A11y/motion:** same link + disclosure contract; keep tiles as plain links;
  stagger reveal only above reduced-motion.

---

## 7. Recommendation for MAT

**Prototype these three, in this order:**

1. **Archetype A (full-width columned + featured cards)** — retrofit Wrestlers &
   Matches. Highest ROI, closest to existing markup, fixes the a11y gaps.
2. **Archetype C (⌘K command palette)** — ships MAT's missing global search *and*
   a power-user nav in one storage-free component; biggest capability jump.
3. **Archetype B (cinematic poster flyout)** — for Rivalries + a Promotions
   switcher; delivers the "premium arena" feeling using existing `--seed`
   gradients and promotion accent tokens, no image pipeline required to start.

Defer tabbed/bento to a v2 consolidation of the bar.

---

## Sources

- Nielsen Norman Group — *Menu-Design Checklist: 17 UX Guidelines* (click-vs-hover, carets, mega vs cascading, images as supportive labels). https://www.nngroup.com/articles/menu-design/
- Baymard Institute — *Homepage & Navigation UX Best Practices 2025* (300–500 ms hover delay/61 %, clickable headers, thumbnails/55 %, current-scope/95 %, single hit areas, mobile scope-in-label). https://baymard.com/blog/ecommerce-navigation-best-practice
- W3C WAI-ARIA APG — *Disclosure Pattern* (aria-expanded, aria-controls, Enter/Space). https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/
- Adrian Roselli — *Link + Disclosure Widget Navigation* / *Don't Use ARIA Menu Roles for Site Nav* (link + button, no role=menu, Esc, no focus trap for nav). http://adrianroselli.com/2019/06/link-disclosure-widget-navigation.html · http://adrianroselli.com/2017/10/dont-use-aria-menu-roles-for-site-nav.html
- Make Things Accessible — *Site navigation is not an ARIA menu*. https://www.makethingsaccessible.com/guides/site-navigation-is-not-an-aria-menu/
- 216digital — *How to Make Mega Menus More Accessible* (Tab/Enter/Esc, aria-expanded on buttons, avoid hover-only, focus return). https://216digital.com/how-to-make-mega-menus-more-accessible/
- UX Patterns for Developers — *Command Palette Pattern* (combobox/listbox, ↑↓/Enter/Esc, aria-activedescendant, grouping, empty/loading states, mobile). https://uxpatterns.dev/patterns/advanced/command-palette
- techinterview — *Build a Command Palette: Cmd+K Like Linear and Vercel*. https://www.techinterview.org/post/3233475212/build-command-palette-cmd-k/
- cmdk (React command menu) reference articles (search-first, groups, recent-first). https://miraseeman.com/cmdk-react-command-menu-setup-examples-advanced-usage/
- Banana Produced — *Mega Menu Design Examples: 15 Navigation Patterns* (columned grid, image/visual, tabbed, content-rich, minimal/bento archetypes + brand examples). https://www.bananaproduced.com/mega-menu-design-examples-15-navigation-patterns-that-improve-ux/
- Companion internal doc: `data/ux-research-nav-ia-search.md` (IA, search, facets, "don't grow the bar").

*Synthesized in the author's own words; no code copied verbatim from sources. All
snippets are original and written against MAT's existing design tokens.*
