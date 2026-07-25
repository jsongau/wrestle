# 10 — FAQ (objection-busting + GEO fuel)

## Purpose
Kill the last friction (cost, cancellation, privacy, free-tier limits, SMS, data provenance)
before the final CTA, and feed search + AI engines structured, answer-first Q&A. This section
does double duty: conversion (removes objections) and GEO (FAQPage schema + liftable answers).

## Layout & structure
- `.section` with a `.wrap--narrow` container (FAQ reads best in a single narrow column).
- `.section-head` (eyebrow → H2 → `.rule-gold`).
- A single `.faq` block containing native `<details>`/`<summary>` accordion items.
- Optionally lead with one `.answer` callout (the gold-bordered answer-first box) restating
  the single biggest objection ("Yes — it's free to browse, no card").
- **Mobile:** the accordion is already single-column and touch-friendly (`summary` is a large
  tap target); no layout change needed.

## Components & CSS classes
- `.section-head`, `.eyebrow`, `.rule-gold`.
- `.faq` (bordered container) → `.faq details` → `.faq summary` (Oswald-weight question with a
  `+`/`–` gold marker) → `.faq__body` (Inter answer).
- `.answer` — the GEO answer-first callout (gold tint, left gold border) for the lead answer
  and optionally the first sentence of each answer.

## Content
Lead each answer with a one-sentence definitional statement (the format AI engines lift),
then 1–2 supporting sentences. 6–8 questions phrased the way fans ask them:

1. **Is it really free to browse?** — *Yes. Browsing every wrestler, match, and rating is
   free, with no account and no card required.* Membership adds advanced stats and archives.
2. **What do I get with membership vs. free?** — *Membership unlocks advanced stats, full
   match archives, the relationship graph, and match-drop alerts.* Free covers profiles,
   results, and ratings.
3. **How complete is the database and where does the data come from?** — *MAT indexes 40+
   years of pro wrestling, compiled and verified by longtime fans.* Every entry cites its
   event and date.
4. **Can I cancel anytime?** — *Yes — membership is month-to-month (or annual) and you can
   cancel anytime from your account.* No cancellation fees.
5. **What are the SMS alerts and can I opt out?** — *SMS match-drop alerts are optional and
   never required to join.* Reply STOP anytime to opt out; standard msg/data rates apply.
6. **When does membership launch and what's the waitlist?** — *Membership is launching soon;
   the waitlist gives you first access and locked-in launch pricing.* Joining is free.
7. **Do you sell my data?** — *No. We use your email only for launch and product updates, and
   you can unsubscribe anytime.*
8. **Which promotions are covered?** — *WWE, WCW, ECW, TNA/Impact, NXT and more across every
   major era.*

## Interactions & motion
- Native `<details>` open/close (no JS required). The `+`/`–` marker swaps via
  `[open] summary::after`.
- Optional: allow only one open at a time via a tiny JS handler (progressive enhancement) —
  but keep all answers in the DOM regardless.
- `[data-reveal]` on the block for entry.
- No motion concerns; global reduced-motion reset covers the open/close transition.

## Accessibility
- `<details>`/`<summary>` are natively keyboard-accessible and screen-reader friendly (state
  announced) — prefer them over a custom ARIA accordion.
- `summary` is a large tap target; visible focus ring.
- **All answer text is in server-rendered HTML** (not injected only on click) so it's readable
  without JS and crawlable.
- Don't rely on the `+`/`–` glyph alone; the native disclosure state carries the semantics.

## SEO/GEO notes
- Add **`FAQPage` JSON-LD** with every question/answer (answers must match the visible text).
- Answer-first sentences are exactly what RAG/AI engines cite — keep the first sentence a
  complete, standalone claim.
- Include number+year facts where natural ("40+ years", "as of 2026") for citation value.
- This is the highest-leverage GEO block on the page — prioritize accurate, self-contained
  answers over marketing fluff.
