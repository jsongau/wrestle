# Wrestle Lore Shell Components

Single source of truth for the universal site shell. Every page under /root/wwe
carries a stamped copy of these three fragments — the stamper (`build/apply_shell.py`)
reads these files at runtime and rewrites all ~226 pages.

| File | What it is |
|---|---|
| `meganav.html` | The full nav7 header: WL brand mark, 7 tabs (Superstars, Matches, Events, Promotions, Hall of Fame, Titles & Teams, Media), all 7 bespoke mega panels, the Gold-Standard search pill (`data-cmdk-open`), the red Join Insider CTA. The `.ticker7` strip is NOT part of this — it is a home-only element that lives in `index.html` above the header. |
| `footer.html` | The FT2 "Directory Grid" fat footer: brand strip + stat chips + gold Join Insider CTA, six mono-headed link columns, provenance line, legal bar. |
| `palette.html` | The `#cmdk` command-palette dialog (driven by `js/nav.js` + `js/search-index.js`). |

## The golden rule

**Edit components, never pages.** Any hand-edit to a header/footer/palette inside a
page file will be overwritten the next time the stamper runs — and worse, until then
that page silently diverges from the rest of the site.

## Update workflow

1. Edit the component file in this directory.
2. `python3 build/apply_shell.py` — stamps every page (idempotent, safe to re-run).
3. Verify locally (open a wrestler page, an index page, and the home page).
4. `git commit` and `git push` — Vercel auto-deploys.
