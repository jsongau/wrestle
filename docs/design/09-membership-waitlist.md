# 09 — Membership + Waitlist Capture (conversion core)

## Purpose
The primary conversion moment. Translate features into fan benefits, contrast the generous
free tier against the paid upgrade, present pricing (three tiers, one highlighted), and
capture the lead with an **email-only** waitlist form. For a pre-launch membership, **the
waitlist IS the conversion** — treat email capture as the win.

## Layout & structure
Three stacked blocks inside one visually distinct band:

1. **Benefits / free-vs-member** — a `.grid-3` (or `.grid-2`) of benefit blocks, then a
   compact two-column Free-vs-Member comparison.
2. **Pricing tiers** — `.tiers` grid, 3 columns desktop → stacked mobile (highlighted tier
   first on mobile).
3. **Waitlist capture** — a `.waitlist-cta` panel with an inline single-field form + proof
   line.

- Full-width contrasting band; use `.pattern-hatch` behind it for texture (the "ring apron"
  hatch) and keep it distinct from the neutral rails above.
- **Mobile:** everything stacks single-column; the highlighted tier (`.tier--featured`) comes
  first; the form input is full-width with `inputmode`/`type=email`.

## Components & CSS classes
- **Benefits:** `.grid-3` of `.card` blocks (icon + Oswald headline + Inter line). Or reuse
  `.notice`/`.related-links` primitives for lighter blocks.
- **Comparison:** a simple `.tiers` two-column or a `table.data` with ✓/– (the `.tier li` /
  `.tier li.no` checkmark styling already exists).
- **Pricing:** `.tiers` → `.tier` / `.tier--featured` (gold border + `--shadow-gold`) with
  `.tier__badge` ("Most popular"), `.tier__name`, `.tier__price` (+ `small`), the ✓/– `ul`,
  and a `.btn` CTA per tier.
- **Waitlist:** `.waitlist-cta` panel; `.form` / `.field` / `.input`; primary
  `.btn.btn--primary` (or `.btn--gold`); `.form-note` reassurance; `.form-success`
  (`.is-visible` on submit) for the queue-position/referral state.

## Content
**Benefits (eyebrow `WHY MEMBERS GO DEEPER`, H2 `Everything a fan could argue about`):**
- **Never lose an argument** → Complete head-to-head match records.
- **Go beyond the results** → Advanced stats, win/loss splits, title lineages.
- **Track your favorites** → Follow wrestlers, get match-drop alerts.
- **Settle the GOAT debate** → Era-adjusted rankings and deep filters.

**Free vs Member (frame free as genuinely useful):**
- Free: `Browse every wrestler & match · Ratings · Basic profiles` (no card).
- Member: `+ Advanced stats · Full match archives · Relationship graph · Alerts · No ads`.

**Pricing (3 tiers, default annual, highlight the middle):**
| Tier | Price | Note |
|---|---|---|
| Free | `$0` | Browse the whole database |
| **Member** (`.tier--featured`, badge "Most popular") | `$6/mo` | Everything a superfan needs |
| Superfan (annual) | `$49/yr` | `Save 20% — 2 months free` |

Pre-launch variant: swap purchase CTAs for **`Join the waitlist to lock launch pricing`**.

**Waitlist (eyebrow `EARLY ACCESS`, H2 `Be first through the ropes`):**
- Blurb: `Members get first access to the full archive and locked-in launch pricing.`
- Field placeholder: `Enter your email`
- Button (first-person, action): **`Get my early access →`**
- Reassurance (`.form-note`): `Free to join. No spam, no card. Unsubscribe anytime.`
- Proof line: `You'll be #12,481 in line — 12,000+ fans already in.`
- Optional SMS step (post-email, opt-in, never a gate): `Want match-drop alerts by text? Add
  your number (optional).` + consent line: `By entering your number you agree to receive
  occasional SMS updates. Msg & data rates may apply. Reply STOP to opt out.`
- Success/referral (`.form-success`): `You're in. You're #12,481 — jump the line by inviting
  friends.` + button `Share my link`.

## Interactions & motion
- **Tier hover:** `.tier` lift; `.tier--featured` already glows (`--shadow-gold`).
- **CTA shine:** `.btn--gold::after` sweep (reduced-motion off).
- **Form submit:** progressive-enhancement JS reveals `.form-success.is-visible` and (if
  present) the optional SMS/referral step — no page reload, no modal (keeps it crawlable).
  Falls back to a normal POST if JS is off.
- **Annual/monthly toggle:** a small control that swaps `.tier__price` values (default:
  annual); pure DOM text swap, no layout thrash.
- `[data-reveal]` on blocks/tiers with stagger.

## Accessibility
- One `<form>` with a labelled email field (`<label for>` even if visually a placeholder;
  `type="email"`, `inputmode="email"`, `autocomplete="email"`, `required`).
- SMS number is a separate optional field with its own label + the consent text as visible,
  associated help text (TCPA); never required.
- The success state should move focus to the confirmation and/or use `aria-live="polite"` so
  it's announced.
- Highlighted tier's "Most popular" is text, not color-only; ✓/– rows include text meaning
  (the `li.no` uses "–" + dim color but the label conveys exclusion).
- CTAs ≥44px; visible focus rings.

## SEO/GEO notes
- Inline form (not a modal) so pricing/benefits text is crawlable.
- `Product`/`Offer` schema on the tiers (price, currency, availability); mirror the same
  primary CTA identity used in hero + nav for message consistency.
- Benefit headlines double as answer-first phrasing AI can lift ("Membership unlocks advanced
  stats, full match archives, and the relationship graph").
