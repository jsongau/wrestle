# CLAUDE.md — START HERE (agent handoff)

You are picking up **Wrestle Lore** (`wrestlelore.com`) — a static, crawlable pro-wrestling
database + review network. This file is the contract for working on it. Read it fully before
touching anything. If you only read one file, read this one.

> **Owner:** Jay (Nathan J. Song), jsongaum@gmail.com. Treat Jay as a builder, not a trained
> engineer — teach while you build (see §7). This project is his portfolio artifact for a
> WWE/TKO **Membership Growth** role, so every feature must serve **acquisition, retention,
> engagement, trust, revenue, or operational efficiency** — not decoration.

---

## 1. What this is (30-second version)

- **Sherdog/Tapology for pro wrestling**: interlinked wrestler / match / event / title pages,
  a Cagematch-style rating layer, and a dense relationship graph, all engineered as a
  **membership-growth funnel** (SEO/GEO traffic → engagement → waitlist → paid tiers).
- **Static site. No build framework.** Hand-authored HTML5 + ONE stylesheet (`css/site.css`) +
  vanilla JS in `js/`. It runs with zero build step — open a file, or `python3 -m http.server`.
- **~264 pages**, ~108 wrestler profiles. Fully crawlable (every nav/footer link is in the
  served HTML, not injected by JS). No browser storage anywhere (in-memory only).
- Deeper vision + funnel/SEO/GEO/China strategy lives in **`PROJECT.md`** and **`README.md`**.
  (Note: those two still use the old working title "MAT" in places — the site has since been
  **rebranded to Wrestle Lore**. Branding is applied at stamp time by `build/apply_shell.py`'s
  RENAMES list; don't mass-edit pages to fix old "MAT" strings, fix the RENAMES map instead.)

---

## 2. The ONE rule that breaks the site if you miss it: the universal shell

The mega-nav, search palette, and footer are **NOT edited in page files.** They live once, as
components, and are **stamped** into all ~264 pages:

- `components/meganav.html` — the `<header class="site-header nav7">`: belt-logo brand lockup,
  7 tabs (Superstars, Matches, Events, Promotions, Hall of Fame, Titles & Teams, Media), 7
  bespoke mega-panels, the `data-cmdk-open` search pill, and the red **Join Insider** CTA.
- `components/palette.html` — the `#cmdk` command palette.
- `components/footer.html` — the FT2 "Directory Grid" fat footer.

**Workflow for ANY nav/footer/palette change:**
1. Edit the **component file** (never a page's inline copy).
2. Run `python3 build/apply_shell.py` (stamps all pages; idempotent; safe to re-run).
3. Verify (see §5), then commit, then push only when Jay says "deploy" (see §4).

`build/apply_shell.py` also: self-hosts fonts (strips Google Fonts, preloads Anton), injects
favicons/theme-color, applies the MAT→Wrestle Lore RENAMES, and **cache-busts** every css/js
link with `?v=<md5 hash>` (see §6 — this is critical). It excludes `/zh/ /china/ /content/
/docs/ /assets/`.

There is a skill for this: **`wrestle-lore-shell`**. Full deep-dive in `docs/UNIVERSAL-SHELL.md`.
The failure mode this prevents: editing one page by hand and silently forking the shell.

Sister rule — **the mega-nav is a fixed 7-tab instrument.** Never add an 8th tab. New content
routes into an existing dropdown panel or a hub page. Depth via hubs, not more tabs.

---

## 3. Repo layout

```
/                     index.html (home) + all section index.html pages
components/           meganav.html · palette.html · footer.html  (SINGLE SOURCE OF TRUTH)
css/site.css          the ONE stylesheet (~2700 lines; nav7 section ~line 1300, 2660+)
js/                   nav.js (mega-nav + reign counters), media.js (Viewing Gallery),
                      home-engage.js, search-index.js, engage.js, main.js, facets.js …
build/                apply_shell.py (STAMPER) · build_gallery.py · build_roster.py
                      gen_wordmark_preview.py, wl_shell_preview.py (throwaway preview generators)
wrestlers/{slug}/     ~108 profiles   matches/ events/ promotions/ media/ archive/ etc.
assets/               wrestle-lore-logo.png (transparent belt buckle) + imagery
docs/                 UNIVERSAL-SHELL.md + dated session summaries
PROJECT.md README.md CHANGELOG.md
fonts/                self-hosted woff2: Anton, Oswald (400/600/700), Inter (400/600/700), JetBrains Mono
```

**Design system "Broadcast Bold":** Anton (`--anton`, display), Oswald (`--osw`, condensed UI),
Inter (`--inter`, body), JetBrains Mono (`--mono7`, telemetry). Dark arena theme; gold `#d4af37`
(bright `#f2cc4b`), red `#e11d2a`. CSS custom properties defined ~line 1271 of `css/site.css`.

---

## 4. Deploy pipeline + Jay's deploy protocol (read before pushing)

- **GitHub:** `https://github.com/jsongau/wrestle.git` (branch `main`).
- **Vercel:** team `cover-capy` (`team_RgXcylGLXtdbEkjyjdtq6p6A`), project **`wrestle`**
  (`prj_3gm5ZwPULhTRekxF0EIIQcKD532y`) → auto-deploys `main` → **wrestlelore.com**.
- **DNS:** Porkbun; apex `wrestlelore.com` (no-www) via ALIAS → `cname.vercel-dns.com`.

**Jay runs several projects at once and never wants them crossed.** Before any push:
- **Confirm the target out loud** (GitHub repo + Vercel project) and **show the git remote**.
- **"commit" = saved forever (local/GitHub), NOT live. "push"/"deploy" = LIVE.** Only push when
  Jay explicitly says deploy/push. Picking/approving a design = commit it; still wait to deploy.
- **Prefer to push yourself from the cloud.** Auth: Jay supplies a short-lived fine-grained
  GitHub PAT (Contents R/W on `jsongau/wrestle`). Use it ONLY for the push, then **immediately
  scrub it** — reset the remote back to the clean `https://github.com/jsongau/wrestle.git`.
  Never commit or write the token into any file. (There is no token stored in this repo.)
- If Jay must run Terminal commands, make them **paste-safe**: no comment lines, no parentheses,
  full absolute paths (never `~/path/to/...`), one command per line.
- **Verify the deploy at the source of truth** — the Vercel deployments API (commit SHA matches,
  `state: READY`) — not by scraping the page. `WebFetch` silently truncates large files like
  `css/site.css` and gives false negatives.
- **Rollback** = Vercel "Promote" a previous deployment, or `git revert`. Never from a saved
  local copy.

**⚠ Parallel-session hazard:** more than one Claude session (across accounts) sometimes works
this same repo. **Always `git fetch origin main` and confirm you're a fast-forward before
pushing.** If diverged: `git fetch` → `git reset --hard origin/main` → re-apply your edits →
re-stamp → push. Two agents on one `main` WILL collide otherwise.

---

## 5. How to verify before you commit (Jay approves evidence, not promises)

- Serve locally: `cd /root/wwe && python3 -m http.server 8231` (or wherever the repo is).
- Screenshot with headless Chromium (Playwright is available; browsers at
  `/opt/pw-browsers/chromium`, `PLAYWRIGHT_BROWSERS_PATH` is set — do NOT run `playwright install`).
  Check the real page at multiple widths (1440 / 1280 / 1152 / 1024 / 390) and read the PNG.
- For nav work: confirm the belt overflows the 62px bar, tabs fit / degrade correctly, and
  the browser console has **zero errors**.
- **Every preview/iteration Jay sees comes with proof** (screenshot, test output, or diff).
- Deliver preview iterations to Jay as **view-only files named `-v2/-v3/-v4`** (disposable
  copies for his Downloads). **Version-numbered files NEVER go into the repo** (anything
  committed deploys as a live public page). Work happens on the ONE live repo folder; no dated
  or versioned files inside it. Keep `CHANGELOG.md` to a one-line entry per working day.

---

## 6. Gotchas that have already burned time (don't rediscover these)

- **Cache-busting is load-bearing.** If you change `css/site.css` or a JS file and the deploy
  "does nothing," it's almost always stale CSS. `apply_shell.py` appends `?v=<hash>` so a deploy
  serves fresh assets — but you MUST re-run the stamper after editing css/js, or the hash won't
  update. Symptoms of missing this: "the logo went tiny," "my change didn't show."
- **The belt logo overflows on purpose.** `.nav7 .mark--logo` is 96px tall with `margin:-17px 0`
  so the bar stays 62px while the belt visually spills 17px above/below. Don't "fix" this by
  growing the bar.
- **The nav is full-bleed** (as of 2026-07-27): the `.wrap` max-width wrapper was removed from
  `meganav.html`; `.nav7 .bar` spans 100% with `padding-inline`. Current wordmark is Concept C
  "Masthead" — Anton `WRESTLE` over wide-tracked gold Oswald `LORE`, slim gold divider.
- **The sheen is masked to the belt shape** (`mask-image: url(logo)`) so light gleams THROUGH
  the metal — never an unmasked box on top.
- **Reign-day counters** on the Titles panel are computed live by `js/nav.js` from `data-start`
  attributes. If you add a belt, set `data-start`.
- **No invented facts.** Every wrestling claim (dates, results, reigns, roles) must be verified
  by web search. Zero 404 internal links — every link you add must resolve.

---

## 7. How Jay wants you to work (his standing preferences — honor these)

Jay's Cowork account has global instructions that may NOT be loaded in your account, so they're
distilled here:

- **Be his technical lead, not just an implementer.** Before building anything that touches a
  database, adds an API endpoint, or spans multiple pages: lay out the plan first — architecture,
  affected files, schema, data flow, trade-offs, success criteria — and wait for approval.
  **Backend-first:** if a feature needs persistence/auth/analytics, propose schema + API before UI.
- **Simplest solution that survives the next year.** No new abstractions/libraries without
  demonstrated need. Improve existing patterns rather than inventing new ones.
- **Stop him from building the wrong thing.** If he drifts toward cosmetic work, name the
  highest-leverage backend/infra task instead. Don't agree just because he asked.
- **When he pushes back / complains:** respond to the complaint FIRST — one line on what went
  wrong, one line on why, a brief apology for the misread, and how he could phrase it next time.
  Then move on. No defensiveness, even if you were technically right.
- **Teach while you build.** After meaningful work, end with a short plain-English section:
  what you built, how it works, why this approach over alternatives, and the one concept worth
  remembering (named, so he can look it up). Flag a better option you skipped and the trade-off.
- **Grow him as a builder.** After meaningful changes add three short notes: (1) **monetization**
  — what it could earn/unlock; (2) **transfer** — which other projects could reuse it; (3) one
  thing to learn next that stretches him past front-end (backend, DBs, APIs, analytics, growth).
- **Session summaries.** At the end of any session with real decisions/debugging/architecture,
  write a dated `.md` into `docs/` (follow the existing naming) capturing what changed and why,
  decisions made and rejected, traps found, and exact next steps. Commit it with the work.
- **File delivery:** deliver files view-only that auto-download when viewed. Preview iterations
  `-v2/-v3` are welcome in chat; never in the repo.

---

## 8. Current live state (as of 2026-07-27)

- Live commit: `7066fdd` — "Nav: full-bleed bar + Masthead wordmark …" — deployed READY on
  wrestlelore.com.
- Recent work: universal shell/component system; Viewing Gallery (YouTube-style theater modal,
  per-video SEO pages under `/media/w/<slug>/`); belt-logo brand + masked sheen; full-bleed nav.

## 9. Next tasks (highest-leverage first)

1. **Join Insider waitlist backend (THE priority).** The red "Join Insider" CTA is the whole
   retention/revenue funnel and currently links nowhere. Stand up a **Supabase** table
   (email, source_page, created_at, referral) + a serverless insert endpoint, wire the form,
   add success/error states. Backend-first: propose schema + API to Jay before UI. (Supabase
   MCP tools are available in-session.)
2. Profile-page `js/engage.js` empty-selector console error — small fix.
3. ~16 legacy gap-wrestler profiles still to build.
4. AAA promotion hub + Worlds Collide event page + El Grande Americano page (nav cells
   currently point at the `/promotions/` and `/media/` hubs as placeholders).

---

*If anything here conflicts with what Jay tells you in the session, Jay wins — but tell him
you noticed the conflict so this file can be updated. Keep this file current: when the shell
contract, deploy target, or working rules change, edit CLAUDE.md in the same commit.*
