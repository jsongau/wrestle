# Universal Shell — component-based mega nav + fat footer

The whole site (226 pages) carries one shell: the nav7 mega nav (formerly home-only),
the #cmdk command palette, and the FT2 "Directory Grid" fat footer. All three live as
component files and are stamped into every page at build time.

## Architecture

**Single source of truth: `/components/*.html`.**

- `components/meganav.html` — `<header class="site-header nav7">`: WL brand mark,
  7 tabs (Superstars, Matches, Events, Promotions, Hall of Fame, Titles & Teams,
  Media), the 7 bespoke mega panels (roster dossier, ladder+desk, T-01..T-06 event
  timeline, 8-card promotions grid, Ring-of-Honor HOF with Two-Time Club, equal-strap
  belt rack with `data-start` reign counters + P crest SVGs, media studio), the
  Gold-Standard search pill (`data-cmdk-open`), and the red Join Insider CTA.
- `components/palette.html` — the `#cmdk` search dialog.
- `components/footer.html` — the FT2 fat footer: brand strip + 4 stat chips + gold
  Join Insider CTA, six mono-headed link columns, provenance line, legal bar.

**Build-time stamping, not runtime includes.** `build/apply_shell.py` reads the three
components at runtime and rewrites the shell into every page's raw HTML. Why raw-HTML
stamping instead of runtime JS includes (fetch/injection):

- **Crawlability** — every nav and footer link is in the served HTML, so search
  engines and LLM crawlers see the full internal-link graph on every page. A
  JS-injected shell is invisible to non-rendering crawlers.
- **Push-is-deploy makes it equally instant** — Vercel redeploys the whole static
  tree on every push, so "edit component + stamp + push" propagates a shell change
  exactly as fast as a runtime include would, with none of the FOUC/latency cost.

The home page's `.ticker7` strip is a home-only element that lives in `index.html`
ABOVE the `<header>` element, so it survives stamping.

## The change workflow

1. Edit the component: `components/meganav.html`, `components/footer.html`, or
   `components/palette.html`. Never edit the shell inside a page file.
2. Stamp: `python3 build/apply_shell.py` — expect "Applied shell to 226 pages …
   NOHDR: 0 | NOFTR: 0". Idempotent; safe to re-run.
3. Verify: open the home page, a wrestler page, and a hub page locally
   (`python3 -m http.server` from the repo root). Check a mega panel opens and the
   footer renders.
4. `git add -A && git commit && git push` — Vercel auto-deploys.

## File map

| Path | Role |
|---|---|
| `components/meganav.html` | nav7 header markup (single source) |
| `components/footer.html` | FT2 fat footer markup (single source) |
| `components/palette.html` | #cmdk palette markup (single source) |
| `build/apply_shell.py` | the stamper: replaces header/#cmdk/footer in all pages, ensures scripts/fonts/favicons, MAT->Wrestle Lore renames |
| `css/site.css` | nav7 styles (scoped under `.nav7`, section "MAIN PAGE V3"); footer styles under "UNIVERSAL FOOTER (FT2 directory grid)" scoped under `.site-footer--fat`; legacy `.nav`/`.mega`/`.footer-grid` rules retained (still serve /zh/ + /china/; harmless elsewhere) |
| `js/nav.js` | palette + nav7 behavior (hover intent, clamping, Esc/outside close, live reign-day counters from `data-start`, touch reveal). Gates on `document.querySelector('.nav7')` so it lights up wherever the header lands |
| `js/search-index.js` | palette search corpus |

## Rules

- **Never edit per-page shells.** The stamper will overwrite them; until it does,
  the page silently forks from the site.
- **Never grow the 7-tab bar.** New content routes into an existing mega panel
  (or a panel's "all" link), never a new top-level tab.
- **Real hrefs only.** Every link in a component must resolve to an existing page
  under the repo root — the stamp multiplies a dead link by 226.
- **Design contract: density, no gold wash.** Panels stay information-dense
  instruments; gold is an accent (rules, heads, counters), never a background wash.
- **Reign dates via `data-start`.** Belt-rack day counters are computed by
  `js/nav.js` from ISO dates in `data-start` attributes — update the date, never
  hand-write a day count.

## Troubleshooting

- **`WARN … ['NOHDR', …]` from the stamper** — that page's header doesn't match
  `<header class="site-header …">`. Someone hand-edited or removed the header.
  Restore a `<header class="site-header">…</header>` element (contents don't
  matter — the stamper replaces them) and re-run.
- **NOFTR** — same, for `<footer …>…</footer>`. The stamper replaces the FIRST
  `<footer>` in the page, so never add a decorative `<footer>` inside `<main>`.
- **Idempotency** — running the stamper twice must produce zero diffs. If a re-run
  keeps changing files, a component file probably contains markup the stamper's own
  regexes re-match differently (e.g. a nested `</header>`, an extra `<footer>`, or
  three consecutive `</div>`s early inside the palette). Keep components free of
  nested shell tags.
- **Nav dead on a page** — check the page includes `/js/nav.js` + `/js/search-index.js`
  (the stamper appends them before `</body>` when missing) and that the header still
  carries the `nav7` class.
