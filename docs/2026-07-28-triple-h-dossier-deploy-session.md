# Triple H Dossier — Integrate → Production Deploy (2026-07-28)

## What shipped
`wrestlers/triple-h/index.html` is now the reference **"dossier" profile template** for the roster.
Modules: sticky nav stack (mega-nav → sub-nav → id-bar mini-nav with breadcrumbs + social + a
"Support" expander), full-bleed hero (gradient Anton title + roster/photo card), a sticky
**Tale-of-the-Tape** rail, a tabbed **win/loss record** (ALL 15 / WINS 7 / LOSSES 8) with
sortable Opponent/Event/Time columns, a championships ledger (9 WWE / 5 WHC / IC / European / tag),
a **career & gimmick-era timeline** (Terra Ryzing → Jean-Paul Lévesque → Hunter Hearst Helmsley →
DX → Evolution → King of Kings → The Authority → Chief Content Officer), rivalries with intensity
meters, **Media & Recent Work** (WWE: Unreal S2 latest-work module), and a fixed bottom
"Related superstars" bar. A discreet 5-star rating (4.5 / 10 ratings) sits in the rail.

New files: `css/profile.css` (scoped design system) + `js/profile.js`, loaded **only** on this page.
`data/triple-h.md` = the sourced fact dossier the page is built from. `CLAUDE.md` §6 = new rule to
keep `data/{slug}.md` updated whenever a wrestler is scraped.

## Architecture / why
- **Same integration pattern the repo already proved** (2026-07-27 template-fix session): transform
  ONLY the `athlete-hero … </main>` region; leave head/nav/footer byte-identical. Verified by diff:
  the only head/footer changes are the 5 intended edits (meta description, JSON-LD, `profile.css`
  link, body swap, `profile.js` link). Minimal, reviewable blast radius.
- **CSS fully scoped under `.wl-dossier`** (specificity 0,2,0 beats site.css's 0,1,0). Recursive
  audit (incl. inside `@media`): **0 unscoped selectors** — `profile.css` cannot affect site.css or
  the other 107 pages. Re-audited against the CURRENT `site.css` (which now defines global
  `.subnav` / `.hero` / `.rail`): my `.wl-dossier .rail{display:grid;overflow:auto}` correctly
  overrides site.css's flex-scroller `.rail`; hero + subnav computed styles confirm no bleed.
- **Fonts:** dropped ~190KB of base64 `@font-face` that the preview inlined — `site.css` already
  ships Anton/Oswald/Inter/JetBrains Mono. `profile.css` is 45KB, zero embedded fonts.
- **Cache-busting:** `site.css`/JS links kept at the live `?v=0fbbcf2b` (untouched); the new
  `profile.css`/`profile.js` carry **content-hash** `?v` (186d9b79 / f63f3a59) so they self-version
  and don't depend on the stamper.
- **JSON-LD rebuilt as valid JSON.** The shell's FAQPage used single-quoted strings + a trailing
  comma = invalid JSON that Google silently drops. Now: Person (alternateName incl. **"HHH"** +
  AggregateRating 4.5/10), BreadcrumbList, FAQPage (3 Q&As) — all parse.

## Decisions made / rejected
- **Scope under `.wl-dossier`** rather than rename 27 colliding classes: one wrapper, zero risk to
  other pages, and the design becomes portable to every wrestler.
- **Keep AggregateRating on Person** (valid schema) even though Google doesn't render review stars
  for `Person` — honest representation; a guaranteed star snippet needs a different entity model
  (follow-up).
- **Curated "landmark ledger" (15 bouts, 7W/8L)** framed as landmark matches, NOT a career win% —
  avoids the misleading "22% win rate" trap (same philosophy as `undertaker-record.md`).
- **Rejected re-running `build_wrestlers_*.py`** (inconsistent one-off artifacts that would re-break
  pages, per the 07-27 doc). The committed HTML is the deploy source.

## Traps discovered
- `device_stage_files` returned a **stale snapshot** (showed `?v=80f08ae7` when the device file was
  `?v=0fbbcf2b`). Fix: `cp` to a fresh path on-device, stage THAT, verify by md5. (Matches the
  07-27 staging-lag trap.)
- **git through the device-bridge mount leaves a stale `.git/index.lock`** (can create, can't
  remove — "Operation not permitted"). ⇒ all git ops for this deploy run in the Mac's **local
  Terminal**, not the bridge. Files reach disk via file-write only.
- `max(styles, key=len)` picked the 200KB base64 **font** `<style>` block, not the 43KB design CSS —
  the design silently vanished. Fixed by selecting the largest block with no `base64`.
- A CSS comment glued onto an `@font-face` prelude defeated the font-drop — strip comments before parsing.

## Verification
- Playwright headless Chromium against the **current** `site.css`: overflow sweep 375 / 768 / 1440.
  Mobile = 0 overflow, 0 JS errors. Desktop overflow == the pre-existing nav7 mega-menu baseline
  (proven identical on the un-spliced page); my content adds **0** page width (`docW` == baseline).
  Rail/hero/subnav computed styles confirm no site.css bleed. JS-off 1:1 slices visually confirm
  every module renders.
- Head/nav/footer byte-identical (diff: only the 5 intended edits). JSON-LD parses.

## Deploy target (confirmed)
- **GitHub:** `origin  https://github.com/jsongau/wrestle.git`, branch `main`.
- **Vercel:** project `cover-capy/wrestle` (push to `main` auto-deploys).
- **Commit file set:** `css/profile.css`, `js/profile.js`, `wrestlers/triple-h/index.html`,
  `data/triple-h.md`, `CLAUDE.md`, `CHANGELOG.md`, `docs/2026-07-28-triple-h-dossier-deploy-session.md`.
  (Left untouched: your in-progress `css/site.css`, `rankings/*`, events-ticketing + membership docs.)

## Exact next steps
1. **Backend (highest leverage): wire the rating + "Join Insider"/Support to Supabase.** Two tables
   — `wrestler_ratings` (slug, rating, ip/session, created_at) and `waitlist` (email, source_slug,
   created_at). The ★ widget and Support/Join currently fire console intent events only. Schema + API
   first, then swap the front-end hooks.
2. **Templatize:** generalize `.wl-dossier` + `profile.css`/`profile.js` into ONE generator that
   stamps all ~108 pages from each `data/{slug}.md` (folds the 3 template families into one — the
   07-27 durability note). Define the wrestler data schema (front-matter or JSON) the generator reads.
3. Real portrait images for the hero "PHOTO SLOT" + the KNOWN FOR cards.

## Stack / approach notes
- Static HTML site; single `css/site.css` with design tokens (`--c-*`, `--font-cond/display`,
  `--fs-*`, `--sp-*`); per-feature CSS added as separate files loaded per-page and scoped.
- Verify visually with headless Chromium over a local static server rooted at a mirror of the
  absolute `/css /js /fonts` paths.
- Deploy reality: bridge git is broken (index.lock) → **local Terminal git only**; files delivered
  via the bridge's file-write. Push to `main` = live on Vercel.

## Mini-nav refinement (same session, 2026-07-28)
Replaced the original centered pill with a nameplate treatment (eyebrow, name, gold diamond status mark, museum vitals line), kept centered with breadcrumbs at the far-left gutter and the right column left open for the Tale-of-the-Tape rail to rise into. Breadcrumbs fade out on scroll (not sticky-locked). Condense reworked to one expo-out curve: eyebrow and vitals collapse gracefully, plate settles with a deeper shadow and brighter mark. Fixed social icons (SVG paths had no fill, so they rendered black; set fill:currentColor -> white). Support restored to all 6 links (had been trimmed to 3 by mistake) as cards, Connor's Cure charity accented red. Removed the bottom-left match floater (.reel). Scoped mini-nav CSS appended to profile.css (0 leaks), JS to profile.js; re-verified against the CURRENT FT3 site.css (dfb0876d) after a site-wide footer re-stamp moved the repo. index.html assembled ON-DEVICE per the new preview-delivery rule (device_commit_files transits Downloads, so raw deploy HTML is written on-device from verified bytes instead of sent as a download).
