# 2026-07-29 — Match-page spoiler reveal + video modal rollout

## What changed

All 30 `/matches/<slug>/` pages now share the same treatment the Undertaker vs
HBK WM25 flagship got approved for:

- **Winner reveal.** The VS card (`.tale`) is now the click target itself —
  "Tap to reveal winner" (or "Tap to reveal result" for the two draws). Tapping
  it unblurs the Result table row and the TL;DR paragraph at the same time
  (one `.wl-revealed` class on `<html>` unlocks everything on the page in
  sync). The FAQ's first `<details>` no longer auto-expands with the winner in
  it either — same fix as the flagship, applied everywhere. All of this is
  progressive enhancement: with JS off, nothing is hidden — full text, full
  SEO/GEO value, nothing to index around.
- **Real video, played in our modal.** The old `.embed`/`.facade` stub (a
  button that just opened a YouTube search — see `matches/*/index.html` prior
  version) is replaced with a real `.yt` facade wired to the site's existing
  `WL.openModal` engine (`js/media.js`), sourced from the verified id in
  `data/matches.json`. 26 of the 30 matches have a verified official upload
  and now play inline, centered, without leaving the site. The 4 that
  genuinely have no official clip (Funk/Sabu, Sting/Hogan Starrcade, Benoit
  fatal four-way WM20, and — as of this session's rebuild of `data/matches.json`,
  Angle/Benoit Royal Rumble '03) get an honest "watch on Peacock/HonorClub/etc."
  link instead of a fake embed. The caption under the player now describes
  which of those two states you're in, instead of the old "opens a search"
  copy that no longer matched reality.
- **New shared files:** `css/matchkit.css` and `js/matchkit.js` (both scoped,
  additive — `css/site.css` was not touched). `build/build_match_kit.py` is
  the idempotent transform that applied all of the above; safe to re-run
  against any future new match page.
- The flagship (`undertaker-vs-hbk-wm25`) also got its full content rebuild:
  buildup, beat-by-beat, 4 related-match embeds, a two-column career
  trajectory timeline for both wrestlers, and the Last Ride documentary embed
  — spec'd in `docs/2026-07-29-match-reveal-video-modal-and-undertaker-build.md`.

## Decisions made (and why)

- **Reveal lives on the card, not a separate meter.** First pass used a
  sweeping "excitement meter" under the names — you didn't like it, so it's
  gone. The VS card itself is the tap target now. Simpler, and it's one fewer
  animated thing to maintain.
- **Blur, don't just collapse.** The TL;DR paragraph stays in the DOM and gets
  a CSS blur + "Spoiler alert" cover, not a JS-only reveal — so search engines
  and AI answer engines still see the real sentence, only human eyes see the
  blur (and only when JS runs at all).
- **One shared secret per page.** Any of the three reveal controls (card,
  result row is passive — it unlocks with the others, TL;DR cover) flips one
  `.wl-revealed` class. Simpler than tracking three separate reveal states,
  and it matches how a person actually thinks about it: I either know the
  winner or I don't.
- **New CSS file instead of extending site.css.** `css/site.css` had
  unrelated in-flight changes from another session working in this same repo
  at the same time (see Traps). Isolating matchkit's CSS into its own file
  meant zero risk of a merge fight over site.css.

## Traps hit this session (worth remembering)

- **This repo had another active session working in it concurrently** —
  floaters, ticker, events/membership planning docs, all landing real commits
  while this rollout was in progress. Local HEAD moved twice (`1a966de` →
  `c019cce`) without any action on my part. Lesson: before trusting "the repo
  is synced," re-check `git rev-parse HEAD` immediately before the final
  write, not just once at the start of a long session.
- **The device bridge's file-staging tool served stale, cached bytes** for 6
  files (`data/matches.json`, 4 match pages, `css/site.css`) even after the
  underlying files had changed on disk and `git status` showed the tree as
  clean. This looked at first like a serious regression — 14 previously-
  verified YouTube IDs appeared to have been wiped from `matches.json`. They
  hadn't; my copy was just stale. Caught it by independently re-hashing the
  live file with `git hash-object` over a fresh `base64`-piped read, not by
  trusting the staging tool a second time. Lesson: when a data file looks
  like it regressed and you can't explain why, re-fetch it a completely
  different way before reporting a false alarm or, worse, "fixing" something
  that was never broken.
- **The per-page FAQ auto-opened its first item with the winner in the
  answer** — same spoiler leak as the TL;DR, just on every page, not only the
  flagship. Wouldn't have caught it without grepping `<details open>` across
  all 30 pages instead of assuming the flagship's fix generalized automatically.

## Next steps

- Waiting on you to run the push (command below) — once that's live, I'll
  confirm the Vercel deployment actually picked it up before calling this done.
- Optional, separate from this commit: 3 slugs in `data/matches.json`
  (`gargano-vs-ciampa-takeover-new-orleans-2018`, `adam-cole-vs-gargano-takeover-xxv-2019`,
  `almas-vs-gargano-takeover-philadelphia-2018`) have video IDs that came from
  the other session's restructure commit, not from my own oEmbed verification.
  Worth a quick re-check pass if you want extra confidence before they get
  more traffic.
- The "Rate the Deadman" style widget pattern already exists on the Undertaker
  page (join-to-save 5-star rating) — the same pattern, generalized, is the
  natural first real (write-to-a-database) feature for match pages: ratings
  per match, aggregate score, "your rating" persisted per logged-in user.
  That's the first genuinely backend task sitting on top of this work.

## Preferred stack note
Static HTML/CSS/JS site, Python build scripts (no framework), GitHub → Vercel
auto-deploy on push to `main`. No database yet — first candidate is
Supabase for the ratings/membership features already stubbed in the UI.

---

*Separately this session: walked through what git and GitHub actually are and
why the current multi-session workflow is slower than editing a single file
and having it appear on GitHub instantly — no code changes, just context for
why the safety steps (stash/pull/verify HEAD) exist and are worth the extra
time on a real, growing site with more than one thing touching it at once.*
