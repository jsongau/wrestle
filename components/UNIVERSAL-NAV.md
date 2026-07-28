# The Universal Mega Nav — the one canonical top bar

Every page on Wrestle Lore shows the **same** top navigation. There is exactly one
canonical version, and it lives in **`components/meganav.html`**. If a page's nav looks
different from the live homepage (`wrestlelore.com`), that page is wrong — not the homepage.

Read this before you build, edit, or "add the nav" to any page.

---

## What it must look like

The belt logo (the WL championship plate, which overflows the bar on purpose) + the wordmark
**"Wrestle Lore" as TWO words** — never "WrestleLore" — then the seven tabs
(Superstars · Matches · Events · Promotions · Hall of Fame · Titles & Teams · Media),
the Gold-Standard search pill, and the red **Join Insider** button.

The homepage is the reference. Match it exactly.

## The exact brand lockup

This is the only correct brand markup. Copy it from `components/meganav.html`; never retype it:

```html
<a class="brand7" href="/" aria-label="Wrestle Lore, home"><span class="mark mark--logo"><img src="/assets/wrestle-lore-logo.png" alt="" width="141" height="96" decoding="async"><span class="sheen" aria-hidden="true"></span></span><span class="bword bw-c"><b class="w">Wrestle</b><b class="l">Lore</b></span></a>
```

The wordmark is the part that keeps getting broken:

- ✅ **CORRECT:** `<span class="bword bw-c"><b class="w">Wrestle</b><b class="l">Lore</b></span>` — class `bw-c`, two `<b>` tags (Wrestle + Lore = two words, stacked with a gold divider).
- ❌ **RETIRED:** `<span class="bword bword--stack"><b>Wrestle</b><b>Lore</b></span>` — the class `bword--stack` is an OLD wordmark. Pages still using it render differently. Do not use it.
- ❌ **WRONG:** "WrestleLore" as a single word or a single `<b>`.

## How the nav gets onto a page — DO NOT hand-write it

The nav is **stamped**, not typed. This is the whole point of the shell system.

1. To change the nav anywhere, edit **only** `components/meganav.html` (once, for the whole site).
2. Run the stamper from the repo root:

   ```
   python3 build/apply_shell.py
   ```

   It replaces `<header class="site-header ...">…</header>` on every page with the canonical
   nav, refreshes the footer + command palette, bumps the `?v=` cache-buster, and is idempotent
   (safe to re-run any number of times).
3. **New page?** Give it any `<header class="site-header nav7"></header>` placeholder and run
   `apply_shell.py`. It swaps in the real nav. You never write the nav markup yourself.

> Note: `apply_shell.py` currently hardcodes `ROOT = "/root/wwe"` (a cloud build path). To run it
> on the local repo, point `ROOT` at the repo root first (or fix it to auto-detect — recommended:
> `ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))`).

**Hand-writing a nav into a page is exactly how drift happens.** `/events/tickets` was built by
hand in a session that used the retired `bword--stack` wordmark, so it fell out of sync with the
other 264 pages.

## Verify before you commit

Run these from the repo root. Both should come back clean:

```
grep -rl 'bword--stack' --include='index.html' . | grep -v '_to_delete'
```
→ must return **nothing**. Anything it lists is drifted; run `apply_shell.py` to fix it.

```
grep -rL 'bword bw-c' --include='index.html' . | grep -v -e '/zh/' -e '_to_delete'
```
→ should return **nothing** (every English page carries the canonical wordmark).

## Why this is documented

This project is a portfolio artifact; a nav that changes page-to-page reads as broken and kills
trust. The nav is a fixed instrument. One source of truth (`meganav.html`), one stamper
(`apply_shell.py`), one verification grep. That is the entire contract.
