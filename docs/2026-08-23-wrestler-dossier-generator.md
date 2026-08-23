# Wrestler dossiers: a generator, wave one, and 60 pages of invisible SEO damage

**Date:** 2026-08-23
**Scope:** `build/build_dossier.py`, `build/wldata/*`, `build/dossier_assets/*`, `build/fix_jsonld.py`, `css/dossier.css`, all 108 `/wrestlers/*/index.html`

---

## What the recon found, before any work started

The request was "50 wrestlers in the CM Punk format." A census of what actually existed changed the shape of the job:

| variant | count | marker |
|---|---|---|
| C — v2 dossier | 5 | `.wl-dossier` + `.sec.reveal` |
| A — old, `<section class="athlete-hero">` | 62 | richest; harvests cleanly |
| B — old, `<header class="athlete-hero">` | 31 | no tape, no match table, no ratings |
| ? — fourth variant | 10 | neither marker |

So this was never "build 50 new pages." It was **upgrade existing pages**, and the old ones already carried researched content — tale of the tape, a match table with results/opponents/events/dates/stipulations, signature matches with star ratings and analysis. Harvesting that and having agents verify it beat re-researching from zero.

Wave one took eight from variant A, the biggest bucket. `jey-uso` was in the original eight and was swapped out for `randy-orton` once the census showed it was variant B.

---

## The architecture decision

cm-punk is **228KB of hand-authored HTML** carrying a **36,092-byte page-local `<style>` block**, byte-identical (sha `cd8177fa`) across cm-punk, john-cena and aj-styles. the-rock ran a 31KB variant whose selectors are a strict subset.

Fifty pages built that way would have shipped **1.7MB of duplicated inline CSS** and been unmaintainable — change the design, edit fifty files.

What replaced it:

1. `build/build_dossier.py` — one generator, twelve sections, data in `build/wldata/<slug>.py`.
2. `css/dossier.css` — the block extracted once. All 13 dossier pages now link it; the four legacy ones shed their inline copies.
3. `build/dossier_assets/` — the two inline behaviour scripts the template carries (a 14.5KB record-ledger IIFE whose only two subject-specific values are templated, and a constant footer-fact shuffler). **In the repo, not `/tmp`**, so the generator works in a fresh checkout.

Generated pages are **75–86KB** against the hand-authored 228KB, and the stylesheet is cached once across the set.

---

## The invisible bug: 60 pages of broken structured data

**60 of 108 wrestler pages were emitting structured data that no parser could read.** Their FAQPage nodes were hand-written with single-quoted string values:

```
{"@type":"Question","name":'Why did WALTER become Gunther?', ...}
```

JSON has no single-quoted strings. A parser rejects the whole `<script>` block at the first one — so Google discarded not just the FAQ but the **Person, WebPage and BreadcrumbList nodes sharing that block**. Sixty pages looked perfect in a browser and were invisible to every rich-result and AI-citation pipeline.

**Three distinct defects, found one at a time:**

1. Single-quoted values. Fixed 47 of 60.
2. Single-quoted values **containing an apostrophe** — `'Glenn Jacobs. He is Knox County's mayor.'`. A naive `[^']*` scan stops at the inner apostrophe. The disambiguation: in this corpus a value only ever ends with an apostrophe followed by a JSON structural character (`,` `}` `]`), while an apostrophe in prose never is.
3. A **trailing comma** before a closing bracket — `"}},]}`.

Each was found by repairing the previous one and re-parsing what was left, not by assuming the first cause was the only cause.

**Result: 108/108 pages parse. 230 schema nodes and 251 FAQ questions are now indexable.** `build/fix_jsonld.py` is idempotent, refuses to save a file it cannot re-validate, and reports anything it cannot fix.

---

## The other production bug

`/wrestlers/triple-h/` was **rendering unstyled in production**. It carried `.wl-dossier` markup and seven `.sec` sections but shipped no dossier CSS and had no `athlete-hero` fallback — the same failure mode as the RAF profile earlier in the day. Fixed by linking `css/dossier.css`.

---

## Invariants the generator enforces

`verify()` fails the build rather than shipping a broken page:

- **Section numbers are a continuous ordinal over emitted sections**, never fixed slot numbers. Randy Orton has no star-rated match in any source, so he has no Signature section and renumbers 01–11. aj-styles proved this behaviour existed in the hand-authored pages.
- **Slot 5 is polymorphic** (`factions` | `before`) and **slot 10 is optional and polymorphic** (`mma` | `feats` | omitted, with different bodies).
- **The subnav lists only 9 sections** — `signature`, slot-10 and `reference` are always omitted from it even when present.
- The career-defining count must **agree in all three places it is printed**.
- FAQ HTML and FAQPage JSON-LD must match **1:1 in count and order**; JSON-LD answers use the full name because they are context-free.
- Exactly four hero stats. Every JSON-LD block must parse.

---

## Traps discovered

- **The hero `h1` clips for any name longer than "CM Punk".** The template joins the name with `&nbsp;` — one unbreakable token — under `clamp(64px,10vw,154px)`. "ROMAN REIGNS" rendered 797px wide in a 722px column. Two fixes, both needed: multi-word names keep a real space so they can wrap, and the max size is capped from the **longest single word**, which cannot wrap at all. Verified clip-free at 1440/1100/900/760/420.
- **A verification script can be the bug.** Mine wrapped the schema-walking in the same `try` as `json.loads`, so a `KeyError` on a page with an unusual graph shape counted as invalid JSON — and reported 32 broken pages when 13 were broken and nothing had regressed. Guard only the operation you are actually testing.
- **`.pchip-aew/-ecw/-ind/-ppv/-tv/-hs` and `.rw-n` were used in markup and defined nowhere.** john-cena patched three of them with a per-page `<style>`. Now in `dossier.css`.
- **Cagematch.net is JavaScript-gated** and returns redirect stubs to automated fetches. No career win-loss total was verifiable for any subject, so `record.total` is the honest row count and every record lead says so.
- **Agents caught two false premises in my own research briefs** — Bianca Belair was never in "Team B.A.D. & Blonde" (chronologically impossible; she signed to the PC after that WrestleMania 32 match), and "Team Little Big" is not a real name for any Becky Lynch team. Both would have shipped as fact.

---

## Next

- **42 more pages.** Variant A has 54 remaining; variant B (31) needs a thinner data path since it has no match table to harvest; the fourth variant (10) needs its own look.
- **RAF 12 results** — the card finished on the night of August 22 and the event page still shows the announced lineup.
- **The push is still blocked.** Ten commits are waiting on `jsongau/wrestle` being added to the GitHub token's repository access.
