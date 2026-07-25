# 11 — Footer (SEO/crawl hub + trust + legal)

## Purpose
For a hybrid content+funnel site, the footer is a **full SEO link hub**, not a minimal
landing-page footer. It distributes crawl equity across the database, captures late deciders
with one more email field, closes the trust/legal loop, and reinforces the MAT entity for GEO.

## Layout & structure
- `.site-footer` (top border, elevated background, top margin `--sp-8`).
- `.footer-grid` inside `.wrap` — auto-fit `minmax(min(200px,100%),1fr)` columns; multi-column
  on desktop, stacked on mobile.
- A `.footer-bottom` strip below the grid: legal links (left) + copyright (right).
- Optional final CTA band **above** the footer (see Content) — a full-width contrasting band
  restating the value prop with the same primary CTA.
- **Mobile:** columns stack; consider making each column heading a collapsible accordion
  (progressive enhancement) to shorten the footer.

## Components & CSS classes
- `.site-footer`, `.footer-grid` (with `h3` gold Oswald headings + `ul` link lists),
  `.footer-bottom`, `.disclaimer`.
- Reuse `.form` / `.field` / `.input` / `.btn` for the secondary email capture column.
- Reuse `.brand` / `.brand__mark` for the footer logo lockup.
- For the final CTA band: a full-width section using `.pattern-hatch`, a `.center` Anton
  restatement, and a `.btn.btn--gold.btn--lg`.

## Content
**Final CTA band (optional, above footer):**
- H2 (Anton): `EVERY MATCH. EVERY RIVALRY. EVERY ERA.`
- Line: `Don't watch from the crowd — get in the ring.`
- CTA: `Join the waitlist →` (same identity as hero/nav).

**Footer columns:**
- **Browse:** By Promotion · By Era · Championships · A–Z Wrestlers · Five-Star Matches ·
  Rankings.
- **Storylines:** Rivalries · Factions · Tag Teams · Betrayals · This Week in History.
- **Membership:** Plans & Pricing · Waitlist · Member Perks · Gift Membership.
- **Company:** About MAT · Data & Sources · Contact · Careers.
- **Stay in the loop:** email field (`Get wrestling updates`) + `.btn--primary` `Subscribe`;
  `.form-note` "No spam. Unsubscribe anytime."

**Footer bottom:**
- Legal: `Privacy` · `Terms` · `SMS Terms` · `Cookie Settings`.
- Copyright: `© 2026 MAT — The Ultimate Pro Wrestling Database.`
- `.disclaimer`: a short line clarifying MAT is a fan-built database, not affiliated with any
  promotion; trademarks belong to their owners.

## Interactions & motion
- Link hover: color shift to gold (already in `.footer-grid a:hover`).
- Optional mobile accordion columns (toggle `hidden` on `ul`) — progressive enhancement.
- Email field: same inline-submit success pattern as section 09 (`.form-success`).
- No decorative motion beyond hover; global reduced-motion reset applies.

## Accessibility
- `<footer role="contentinfo">`; each column under a real `<h3>` with an associated `<nav
  aria-label>` (or list).
- Secondary email form has a labelled field (`type=email`, `autocomplete=email`).
- Accordion (if used) uses `aria-expanded` on the column toggle button and keeps content in
  the DOM.
- Sufficient contrast for muted footer links (`--c-text-muted` on `--c-bg-elev-1` ≥ AA).
- Focus rings visible; tap targets ≥44px on mobile.

## SEO/GEO notes
- The footer link grid is the primary **internal-linking surface** — deep links into every
  database hub build topical depth that ranks content pages and feeds the funnel.
- Add **`Organization` JSON-LD** (name, logo, url, `contactPoint`, `sameAs` → official social
  profiles) here for entity clarity in search + AI engines.
- Keep NAP/entity info consistent sitewide; the disclaimer's factual "fan-built database"
  statement is useful, citable context.
- All links are real crawlable `<a href>` in server-rendered HTML.
