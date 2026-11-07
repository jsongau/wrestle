# Superstar Pages — Dead-Template Rescue (2026-07-27)

## Problem
65 of ~108 wrestler profile pages (Cody Rhodes, Hulk Hogan, Roman Reigns, most of the roster)
rendered as unstyled stacked text: breadcrumb as a numbered list, vitals dumped vertically,
"Method Breakdown" floating with no card. The Undertaker page rendered correctly.

## Root cause
Three page templates coexist in /wrestlers:
- OLD (65, broken): hero-eyebrow / hero-name / hero-meta / hero-stat-block / content-grid(section) / sig-matches / match-record / breadcrumb.
- NEW "athlete-hero" (33, correct — the Undertaker): hero-inner / page-wrap / stat-card / sig-section / record-section.
- PROFILE/persona (10): hero--profile (booker-t style) and section--tight (stone-cold + persona/alias pages).
A later CSS refactor renamed the hero/section classes and DELETED the old names from css/site.css.
The 65 OLD pages kept referencing the deleted classes, so the browser had nothing to style them with.
Content was fully intact — only the class-name wrappers were dead. build_wrestlers_*.py are inconsistent
one-off patch artifacts (some emit old markup, some new); re-running them would re-break pages, so they are
NOT a clean generator. data/ is markdown research notes, not a data source. => fix = transform HTML in place.

## What changed
1. wl_transform.py (deterministic BeautifulSoup transformer, run on-device). Rewrites ONLY the
   <nav breadcrumb>…</main> region per page; head/nav/footer left byte-for-byte identical:
   - hero -> <header class="athlete-hero"><div class="hero-inner"><h1>NAME</h1><p class="hero-sub">eyebrow</p></div></header>
   - move vitals dl + W/L/Win% + method bars into sidebar .stat-card blocks (Vitals / Record / Finish Method)
   - <p class="dim">: "Also known as …" -> alias row; otherwise (Heel/Face) -> "Alignment" row
   - content-grid section->div, bio-col article->div, main -> main.page-wrap, hero+wl-strip moved before main
   - sig-matches -> sig-section, match-record -> record-section; data-record-filter moved onto the filter row (enhance.js hook)
   - drop the unstyled visible breadcrumb (BreadcrumbList JSON-LD in <head> retained for SEO)
   Applied to all 65 -> 0 old-template pages remain; 98 pages now on athlete-hero.
2. css/site.css: appended .hero--profile hero/badge/name/bio/facts + .subnav rules (design-token based;
   grid-areas so the name/bio get the wide column, facts card the narrow one). Fixes the 5 hero--profile pages.
   The 5 section--tight persona pages were already styled — untouched.

## Decisions (made / rejected)
- Deterministic script OVER 65 agents: pages were structurally uniform, so one reviewed transform is safer,
  faster, and consistent vs 65 LLM edits. Agents used where they add value: parallel VISUAL QA.
- Kept the "Finishing Moves" bio section (50/65 have it) rather than folding finisher into the sidebar — no content loss.
- Profile pages: ADDED CSS (keep richer rivalries/relationships/related content) rather than converting to
  athlete-hero (which would drop those sections). Per user approval.
- Rejected regenerating from build_wrestlers_*.py (inconsistent, would re-break pages).

## Traps discovered
- 15 sparse legends had NO vitals <dl> and used <p class="dim"> for ALIGNMENT (Heel/Face), not alias.
  First pass mislabeled them "Also known as"; caught by the parallel visual-QA agents (big-show). Fixed.
- git through the cloud device-bridge mount CANNOT unlink .git/index.lock ("Operation not permitted") —
  git can create the lock but not remove it, so commits/status leave stale locks. Local Terminal git on the Mac is fine.
- device_stage_files returned a STALE cached snapshot right after an in-place edit (device file was correct; the
  staged copy lagged). Trust the device file; re-verify via device_bash, not the staged copy.

## Verification
- Structural audit on all 98 athlete-hero pages: 0 anomalies.
- Byte-level content + link preservation proven on Cody (0 text/link loss).
- 30 pages visually QA'd by 3 parallel subagents (29 pass + the big-show catch) + 15 rendered locally across
  every variant (with/without sig-matches, men/women, legends, sparse, profile).

## Next steps
- On DEPLOY: bump the css cache-buster (?v=51709c29) so returning visitors get the new profile-hero CSS.
  Confirm target (repo jsongau/wrestle, Vercel project cover-capy/wrestle) before push.
- Optional: backfill real vitals (born/height/debut) for the 15 sparse legends — they currently carry only Alignment + Record.
- Durability win: fold the 3 template families into ONE generator to prevent future class-name drift.

## Stack / approach notes
- Static HTML site; single css/site.css with design tokens (--c-*, --font-display/cond, --fs-*, --sp-*, --wrap, --r-lg).
- Editing pattern that worked: transform only the <main> region, leave head/nav/footer byte-identical -> minimal reviewable diffs.
- Verify visually with headless Chromium (Playwright) over a local http.server rooted at a mirror of the absolute /css /js /fonts paths.
