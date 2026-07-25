# MAT — Mobile / Touch UX & Accessibility (WCAG 2.2) Research

**Scope:** dark-themed, static, mobile-first sports/entertainment site (MAT) with a membership/waitlist funnel.
**Method:** synthesized current best practice (W3C WCAG 2.2 / WAI-ARIA APG, Nielsen Norman Group, Baymard, web.dev, Apple HIG, Material) against the *real* MAT components.
**Audited components:** `.nav__toggle` + mega-nav (`.nav`, `.nav__menu`, `.nav__link[aria-haspopup]`, `.mega`), `.faq` native `<details>`, the `.waitlist-cta` `.form` (`#wl-email`, `#j-email`, `#j-sms`, `#j-name`, `#j-fav`), `.tile`, `.btn`, and `[data-reveal]` motion, plus the palette tokens in `css/site.css` `:root`.
**Date:** 2026-07-25.

> **How to read the "Apply to MAT" notes:** each references the concrete selector/file and a specific change. Contrast numbers are computed from the actual token hex values (see §10).

---

## 0. Executive summary — what's already strong, what fails

**Already good (keep):**
- Fluid `clamp()` type scale, non-pure text on non-pure black (`#e8eaed` on `#0a0b0d` = **16.3:1**), skip-link, landmarks, native `<details>` FAQ, `.nav__toggle` at 44×44, and an *exemplary* `prefers-reduced-motion` implementation (global reset + per-effect JS bailout + `finePointer` gating).

**Must-fix (detail in sections):**
1. **Contrast FAILURES (WCAG AA):** `--c-text-dim #6b727d` (4.06:1 body text), `--c-loss #e05263` (3.96:1), and `--c-red #e11d2a` used as *normal-size* text (4.14:1). See §10.
2. **Primary conversion CTA ("Join MAT Insider") is hidden on mobile** inside the collapsed hamburger, in the hardest-to-reach top corner. No sticky/thumb-zone CTA. See §2–§3.
3. **Form status message is invisible to screen readers** — `.form-success` is toggled by class with no `role="status"`/live region and no focus move (WCAG 4.1.3). See §5, §8.
4. **Inputs likely trigger iOS auto-zoom** — `.input` uses `--fs-400` (min ≈15px < 16px). See §4, §5.
5. **`.input:focus{outline:none}`** strips the focus ring, leaving only a 1px hue change (WCAG 2.4.7 risk / 2.4.13). See §7.
6. **Mega-nav keyboard/AT gaps:** `aria-expanded` desynced on desktop, no Esc-to-close, no focus management when the mobile menu opens, `aria-haspopup="true"` misrepresents a link group as a menu. See §7, §8.

---

## 1. Tap-target sizing & spacing

**Principle.** Three thresholds matter and they are not the same:
- **WCAG 2.2 SC 2.5.8 Target Size (Minimum), AA:** interactive targets must be **≥ 24×24 CSS px**, unless spacing (a 24px-diameter circle around each target doesn't overlap a neighbor), inline text, or an equivalent control exempts them.
- **Apple HIG:** minimum **44×44 pt** hit area for any control.
- **Material Design:** minimum **48×48 dp** touch target (with ≥8dp spacing).
Treat **24px as the legal floor and ~44–48px as the usability target**; the delta reduces mis-taps and repeat interactions (which also hurt INP).

**Source.** [W3C Understanding SC 2.5.8 Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html); [TetraLogical — Foundations: target sizes](https://tetralogical.com/blog/2022/12/20/foundations-target-size/); [LogRocket — accessible touch target sizes](https://blog.logrocket.com/ux-design/all-accessible-touch-target-sizes/).

**Apply to MAT.**
- `.nav__toggle` = `width:44px;height:44px` → **passes Apple 44, exceeds WCAG 24**; nudge toward 48 to match Material. Good.
- `.btn` (`padding:.75em 1.4em`) and `.btn--lg` (`.9em 1.8em`) render ≥ ~44px tall — OK. `.input` (`padding:.8em 1em`) ≈ 44px — OK.
- **`.mega__link` (`padding:.4em .5em`) is the weak spot:** at `--fs-400` these disclosure links compute to roughly ~30–34px tall and, on mobile, stack with only `--sp-1` gaps. They clear the 24px legal minimum but fail the 44/48 usability target and the 24px *spacing* ring is marginal. Bump to `padding:.7em .6em` and increase inter-item gap to `--sp-2` in the `max-width:900px` block.
- `.rate` star inputs (`font-size:var(--fs-600)`, `gap:.1em`) — verify the clickable `label` area is ≥24px and non-overlapping; the 0.1em gap risks adjacent-target overlap. Add horizontal padding to each `.rate label`.
- `.faq summary` (`padding:var(--sp-4) var(--sp-5)`) — comfortably large. Good.

---

## 2. Thumb-zone / reachability & sticky bottom CTAs

**Principle.** One-handed phone use makes the **bottom-center the easy zone** and the **top corners the hard/uncomfortable zone** (NN/g "thumb zone"). Primary, high-frequency actions — especially a conversion CTA — belong low and central; destructive/rare actions can live top. A **sticky bottom CTA** on mobile puts the funnel's key action permanently in the reachable zone without a scroll hunt.

**Source.** [NN/g — The Thumb Zone / designing for mobile reach](https://www.nngroup.com/articles/thumb-zone-mobile/); [Parachute Design — Mastering the Thumb Zone](https://parachutedesign.ca/blog/thumb-zone-ux/).

**Apply to MAT.**
- Today the primary CTA (`.nav__cta` "Join MAT Insider") sits **top-right and is collapsed inside the hamburger on mobile** — the hardest reach *and* hidden. The waitlist `.form` is mid/low page.
- **Add a mobile-only sticky bottom CTA bar** (e.g., `.cta-dock`, shown only `@media (max-width:900px)`), containing one `.btn.btn--gold` → `/membership/` (or a `#join` jump). Respect the notch with `padding-bottom:env(safe-area-inset-bottom)` (the page already sets `viewport-fit=cover`).
- Keep it out of the way of the OS home indicator; hide it once the user reaches the on-page `.waitlist-cta` (IntersectionObserver, reusing the existing observer in `enhance.js`) to avoid CTA duplication.
- Ensure the dock and the sticky `.site-header` don't sandwich content; give `main` scroll-margin so in-page anchors clear both bars.

---

## 3. Mobile nav — hamburger vs bottom bar

**Principle.** **Hamburger menus** hide IA behind a tap and reliably lower discoverability/engagement of the hidden items; they're acceptable for large or secondary IA. **Bottom tab bars** keep 3–5 top destinations always visible in the thumb zone and outperform for core, frequently-used navigation, at the cost of screen space and a hard 5-item ceiling. Hybrid is common: bottom bar for the 3–5 core destinations + a "More"/hamburger for the long tail.

**Source.** [NN/g — Thumb Zone / mobile navigation](https://www.nngroup.com/articles/thumb-zone-mobile/); [Medium (UI/UX Trends) — Mobile App Navigation Design: 2026 best practices](https://medium.com/ui-ux-designing-trends/mobile-app-navigation-design-2026-ux-best-practices-5b2db901790d).

**Apply to MAT.**
- MAT's mega-nav (`.nav__menu` sliding down via `transform:translateY(-120%)`, mega panels becoming static accordions) is a reasonable hamburger for the **full IA** (Wrestlers/Matches/Rivalries/Relationships/Rankings/中文). Keep it for breadth.
- **But do not bury the conversion action in it.** Two options: (a) keep the hamburger for browse IA *and* add the §2 sticky bottom CTA for "Join"; or (b) promote a light 4-item bottom bar (Wrestlers · Matches · Rankings · **Join**) and demote the rest to the hamburger. Option (a) is less invasive for a static site.
- Language toggle (中文) should remain reachable; don't hide it two levels deep — it's an accessibility/i18n affordance, not "long tail."

---

## 4. Responsive typography & readability on dark

**Principle.** On dark themes, **avoid pure `#fff` on pure `#000`** — the high luminance delta causes halation/ghosting for many readers, especially astigmatism. Use a slightly-off-white on a near-black (dark grey) and keep body ≥ ~16px with generous line-height and measure (~45–75ch). Fluid type (`clamp()`) is best practice. Body/input text ≥16px on mobile also prevents iOS Safari's focus auto-zoom.

**Source.** [W3C Understanding SC 1.4.3 Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) (large-text = 18pt/≈24px or 14pt bold/≈18.5px); [web.dev — Learn Accessibility: color & contrast](https://web.dev/learn/accessibility/); [Baymard — mobile form usability](https://baymard.com/blog/mobile-forms-avoid-inline-labels) (16px min to avoid zoom).

**Apply to MAT.**
- **Excellent baseline:** body text is `--c-text #e8eaed` (off-white) on `--c-bg #0a0b0d` (near-black, not `#000`) = **16.3:1**, and the fluid `--fs-*` clamp scale is exactly right. Keep.
- **`--fs-400` min is `0.94rem` (~15px).** For **`.input`/`select`/`.form-note` and body on the smallest screens, raise the floor to `1rem` (16px)** to (a) prevent iOS auto-zoom on focus and (b) improve small-text legibility on dark. Simplest fix: set `.input{font-size:16px}` (or `max(16px, var(--fs-400))`).
- Constrain measure on long dark paragraphs — `.hero-bb__lede`/`.muted` blocks; the codebase already uses `max-width:52ch` on `.hero__lead` — extend that discipline to membership copy.
- Reserve pure `#fff` for text sitting on **saturated fills** (chips/buttons), never on the page background. Current usage is compliant on that front.

---

## 5. Form UX on mobile (inputs, labels, autofill, errors)

**Principle.**
- **Persistent labels above the field** — never placeholder-as-label. Placeholders vanish on input, destroying context during error correction; use them only for format hints.
- **Right input type + `inputmode` + `autocomplete`** summons the correct keyboard and enables one-tap autofill: `type="email" inputmode="email" autocomplete="email"`, `type="tel" inputmode="tel" autocomplete="tel"`, names use `autocomplete="given-name"`. Add `enterkeyhint` where useful.
- **Inline, specific, forgiving error handling:** validate on blur/submit (not on every keystroke), show the message adjacent to the field, wire `aria-describedby` + `aria-invalid`, and move focus to the first error.
- **16px min font** on inputs to avoid iOS zoom.

**Source.** [Baymard — Mobile Form Usability: Never Use Inline Labels](https://baymard.com/blog/mobile-forms-avoid-inline-labels); [Smashing — Best Practices for Mobile Form Design](https://www.smashingmagazine.com/2018/08/best-practices-for-mobile-form-design/); [UXPin — Error feedback on mobile forms](https://www.uxpin.com/studio/blog/error-feedback-best-practices-mobile-forms/).

**Apply to MAT.**
- **Doing well:** every field has a real `<label for>` above it (`#wl-email`, `#j-name`, `#j-email`, `#j-sms`, `#j-fav`); placeholders are examples not labels; `type="email"`, `type="tel"` and `autocomplete="email|given-name|tel"` are present. This matches Baymard/APG.
- **Add `inputmode`:** `inputmode="email"` on the email inputs and `inputmode="tel"` on `#j-sms` (belt-and-suspenders with `type`, and it fixes keyboards on some Android browsers). Add `enterkeyhint="send"` on the submit-triggering field.
- **Raise input font-size to ≥16px** (see §4) — the waitlist inputs currently inherit `--fs-400`.
- **Error handling is thin:** `main.js` only calls `email.reportValidity()`; `#j-name`/`#j-sms` get no feedback and there's no visible, associated inline error text. Add per-field error `<span id="…-err" class="field__error">` linked via `aria-describedby`, set `aria-invalid="true"` on failure, and focus the first invalid field. Consider `novalidate` on the form + custom messaging for consistent styling/announcement.
- **Success is not announced (critical):** on submit, `main.js` adds `.hide` to the form and `.is-visible` to `.form-success`, but `.form-success` has **no `role="status"`/`aria-live` and focus is never moved** → screen-reader and many keyboard users get no confirmation (WCAG 4.1.3 Status Messages). Fix: add `role="status"` (or `aria-live="polite"`) to `.form-success` **and** move focus to it (`tabindex="-1"; el.focus()`) after reveal.
- The `#j-fav` `<select>` (favorite promotion) is fine; per Baymard, never use an inline/placeholder label on a select — MAT already labels it. Good.

---

## 6. Motion & prefers-reduced-motion

**Principle.** Motion can trigger vestibular symptoms (nausea, dizziness). Honor `@media (prefers-reduced-motion: reduce)` — remove/deaden non-essential parallax, auto-count, large translate/scale reveals, and continuous animation; keep essential motion minimal and short. A "reduce-first" mindset (opt into motion) is safest. Relates to WCAG 2.3.3 Animation from Interactions (AAA) and 2.2.2 Pause/Stop/Hide.

**Source.** [web.dev — Animation and motion (Learn Accessibility)](https://web.dev/learn/accessibility/motion); [MDN — prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion); [Tatiana Mac — no-motion-first](https://www.tatianamac.com/posts/prefers-reduced-motion).

**Apply to MAT.** This is a **model implementation — keep it:**
- `css/site.css` has a global `@media (prefers-reduced-motion:reduce){*{animation/transition-duration:.01ms; scroll-behavior:auto}}` **and** a targeted rule forcing `[data-reveal]{opacity:1;transform:none}`.
- `enhance.js` reads `matchMedia('(prefers-reduced-motion: reduce)')` and **bails per-effect**: `runCount()` snaps to the final value, hero pointer-parallax and `.tile` spotlight are gated behind `!reduce && finePointer` (so they also never run on touch).
- Minor polish: the global `*{transition-duration:.01ms !important}` is fine but heavy; if any *state* feedback (e.g., focus ring appearance) ever depends on a transition, it'll be flattened — acceptable here. No change required.

---

## 7. Focus management & keyboard nav — mega-nav, accordions, modals

**Principle.**
- **Mega-nav / disclosure:** the trigger needs a synced `aria-expanded`; the panel should be reachable in DOM order; **Esc closes and returns focus** to the trigger; `aria-haspopup="true"` should be used *only* for actual menu/menu-like widgets (it announces "menu"), not for a group of plain links (use a **disclosure** pattern instead).
- **Mobile menu:** opening should move focus into the menu (or to a close control), trap or at least logically contain focus, Esc closes, and the toggle's `aria-expanded` reflects state.
- **Accordions:** native `<details>/<summary>` is keyboard-accessible for free (Enter/Space, focusable summary).
- **Modals (`<dialog>`):** trap focus, Esc closes, focus moves in on open and **returns to the invoking element on close**, background is inert.
- **Visible focus:** every interactive element needs a clearly visible focus indicator (2.4.7); WCAG 2.2 adds 2.4.11 Focus Not Obscured (AA) and 2.4.13 Focus Appearance (AAA, ≥2px-equivalent, sufficient contrast).

**Source.** [WAI-ARIA Authoring Practices Guide (APG) — Disclosure & Dialog patterns](https://www.w3.org/WAI/ARIA/apg/); [UXPin — Accessible modals with focus traps (2026)](https://www.uxpin.com/studio/blog/how-to-build-accessible-modals-with-focus-traps/); [W3C Understanding SC 2.4.11 Focus Not Obscured](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html).

**Apply to MAT.**
- **`.faq` accordions — compliant.** Native `<details>/<summary>` with custom `+`/`–` marker; `:focus-visible` gives a 2px `#5aa9ff` ring. Keep. (One `<details open>` default is fine.)
- **Mega-nav desktop:** panels open via CSS `:focus-within`/`:hover`, so keyboard tabbing *reveals* them — good — but **`aria-expanded` is only toggled by the mobile-width branch in `main.js`; on desktop it stays `"false"` while the panel is visually open** (AT mismatch). Sync it in the `focusin`/`focusout` handlers. Also add **Esc-to-close** returning focus to the `.nav__link`, and consider `aria-controls` pointing the link at its `.mega` panel id.
- **`aria-haspopup="true"` is semantically wrong here** — the `.mega` is a group of links, not a menu. Either drop `aria-haspopup` and treat it as a disclosure, or switch to a proper button-based disclosure. Announcing "menu" then presenting links confuses SR users.
- **Mobile menu focus:** `.nav__toggle` click toggles `.is-open` and `aria-expanded` and swaps the ☰/✕ glyph (good), **but focus is not moved into `.nav__menu`, there's no Esc handler, and background isn't inert.** Add: on open, focus the first link (or the menu container with `tabindex="-1"`); Esc closes and returns focus to `.nav__toggle`; consider `inert` on `<main>` while open.
- **Inputs lose their focus ring:** `.input:focus{outline:none}` replaces the global 2px `#5aa9ff` `:focus-visible` outline with a **1px gold border color change only**. Gold-on-`elev-3` is 7.1:1 (passes non-text contrast) but a 1px hue-only change is a weak indicator and risks 2.4.7/2.4.13. **Restore a visible ring:** use `:focus-visible{outline:2px solid var(--c-focus); outline-offset:2px}` and drop `outline:none`, or add `box-shadow:0 0 0 3px var(--c-focus)`.
- **Modals:** none exist today (the video `.facade` is a `<button>` that opens a new tab / swaps in a lazy iframe — accessible). **If** a signup/paywall modal is added later, use `<dialog>` with focus trap, Esc, and focus-return per APG.

---

## 8. Screen-reader semantics (landmarks, ARIA, alt, live regions)

**Principle.** One `<main>`, labeled `<nav>`, `<header>`/`<footer>` landmarks; a skip link; images need meaningful `alt` (or `alt=""`+`aria-hidden` if decorative); icon-only controls need an accessible name; dynamic status needs a **live region** (`role="status"`/`aria-live`); don't misuse roles.

**Source.** [W3C WAI — ARIA APG & landmark regions](https://www.w3.org/WAI/ARIA/apg/); [W3C Understanding SC 4.1.3 Status Messages](https://www.w3.org/WAI/WCAG21/Understanding/status-messages.html); [MDN — Using media queries / ARIA basics](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA).

**Apply to MAT.**
- **Good:** `<a class="skip-link" href="#main">`, `<header>` → `<nav aria-label="Primary">` → `<main id="main">`, `html lang="en"` with `hreflang`/`zh` alternates, decorative bits marked `aria-hidden` (`.hero-bb__bg`, `.tile__mono`, `.tile__spot`, star glyphs), and the hamburger `<button aria-label="Toggle menu" aria-controls="primary-menu" aria-expanded>` (name survives the ☰→✕ glyph swap).
- **Live region gap (critical, see §5):** `.form-success` must be `role="status"` so the "You're on the list!" confirmation is announced (WCAG 4.1.3).
- **Ratings:** `.rating__stars` is `aria-hidden` and only the numeric `.rating__num`/`.tile__rating` ("5.0") is exposed — SR reads "5.0" with no unit. Add visually-hidden context, e.g. `<span class="sr-only">rated 5.0 out of 5</span>`.
- **Alt text (forward-looking):** the home page currently renders monogram/gradient placeholders (no content `<img>`). **When real wrestler/match photography is added,** give descriptive `alt` (wrestler name + context) and mark purely decorative art `alt=""`. The `og:image` metas are fine as-is.
- **`aria-haspopup` misuse** on `.nav__link` — see §7.

---

## 9. Performance-as-UX on mobile

**Principle.** On mobile, speed *is* UX. Track Core Web Vitals: **LCP ≤ 2.5s**, **CLS ≤ 0.1**, and **INP ≤ 200ms** (INP measures responsiveness of tap/click/keyboard interactions across the visit, reported near the 75th-percentile-of-loads / worst-interaction; 200–500ms = needs work, >500ms = poor). Defer/lazy-load offscreen media, avoid layout shift by reserving media dimensions, self-host or preload fonts, and keep main-thread work light.

**Source.** [web.dev — Interaction to Next Paint (INP)](https://web.dev/articles/inp) (Good ≤200ms; Needs improvement 200–500ms; Poor >500ms); [web.dev — Optimize INP](https://web.dev/articles/optimize-inp).

**Apply to MAT.**
- **Strong foundation:** static HTML, single `css/site.css`, **vanilla JS with zero dependencies** (low main-thread cost → healthy INP), an **IntersectionObserver reveal** (not scroll listeners for animation), a **click-to-load video `.facade`** (no YouTube/Bilibili iframe on first paint → protects LCP and INP), and a `passive` scroll listener for the header shadow.
- **Fonts are the main risk:** three families (Anton, Oswald, Inter) loaded render-blocking from `fonts.googleapis.com`. Already using `preconnect` + `display=swap` (good). Further: **self-host the WOFF2 and `<link rel="preload">` the display face** used in the LCP `<h1>` to cut a round-trip and reduce FOUT/CLS; subset to Latin (+ handle the `/zh/` fonts separately).
- **CLS:** ensure media boxes reserve space. The hero poster/embed and `.tile__media` should have explicit `aspect-ratio` so the `[data-reveal]` translate and image loads don't shift layout. Add `width`/`height` (or `aspect-ratio`) when real images land, and `loading="lazy"` below the fold (the facade iframe already sets `loading="lazy"`).
- **`backdrop-filter:blur(10px)`** on the sticky `.site-header` is GPU-costly on low-end Androids; acceptable, but if you see jank, swap to a semi-opaque solid on `(max-width:900px)`.
- **INP:** current interactions (nav toggle, mega toggle, filter `input` handler, facade swap) are light. The live `[data-filter]` search filters DOM on every `input` event — fine at current list sizes; if roster/match lists grow large, debounce (~120ms) to keep INP ≤200ms.

---

## 10. Color-contrast audit — black + gold `#d4af37` + red `#e11d2a` (computed)

Ratios computed from the actual `:root` tokens against real usage. **AA = 4.5:1 normal text, 3:1 large text (≥24px, or ≥18.66px bold) and non-text UI/graphics.** Large-text = 18pt≈24px / 14pt bold≈18.5px per [SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html); non-text per [SC 1.4.11](https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html).

### ❌ FAILURES (fix these)

| Foreground | Background | Ratio | Verdict | Where it's used |
|---|---|---|---|---|
| `--c-text-dim #6b727d` | `--c-bg #0a0b0d` | **4.06:1** | ❌ FAIL (normal text) | `.form-note`, `.mega__link small` (nav descriptions), `.card__meta`, `.dim` |
| `--c-text-dim #6b727d` | `--c-bg-elev-1 #121418` | **3.80:1** | ❌ FAIL (normal text) | same, on raised surfaces |
| `--c-loss #e05263` | `--c-bg-elev-3 #23272f` | **3.96:1** | ❌ FAIL (normal text) | `.chip--loss` |
| `--c-red #e11d2a` (as text) | `--c-bg #0a0b0d` | **4.14:1** | ❌ FAIL as *normal* text; ✅ OK only as **large text / non-text fill/border** | any red text < 24px; `.tale .vs` (large) passes at 3.87:1 |

**Fixes:**
- **`--c-text-dim`:** lighten to ~`#7d8590` (≈4.7:1 on `#0a0b0d`) or reserve `#6b727d` strictly for *disabled* text (exempt from 1.4.3). It is currently used for real content (waitlist note, mega-nav sublabels) — those must pass.
- **`--c-loss`:** brighten to ~`#f0687a` for chip text, or pair it with an icon/label so color isn't the only cue.
- **`--c-red`:** never set as normal-size body text. It's fine as a **fill** (`#fff` on red = 4.76:1, passes) and as a **border/graphic** (non-text 3:1). Where red *text* is wanted, use `--c-red-bright #ff3b48` (**5.60:1** on `#0a0b0d`, passes).

### ✅ PASSES (verified)

| Foreground | Background | Ratio | Note |
|---|---|---|---|
| `--c-text #e8eaed` | `#0a0b0d` | 16.34:1 | body — AAA; correctly avoids pure white/black |
| `--c-text-muted #a2a9b4` | `#0a0b0d` / elev-1 | 8.32 / 7.79:1 | AAA |
| `--c-gold #d4af37` | `#0a0b0d` / elev-1 | 9.36 / 8.77:1 | eyebrows, `.mega__col h3`, FAQ `+` marker — AAA |
| `--c-gold-bright #f2cc4b` | `#0a0b0d` | 12.67:1 | links, `.rating__num` — AAA |
| `#000` on `.btn--gold` `#d4af37` | — | 9.99:1 | gold button label — AAA |
| `#000` on gradient end `--c-gold-dim #8c7420` | — | 4.63:1 | AA pass but **thin** — darkest end of the `.btn--gold` gradient; keep text on the lighter half or darken text weight |
| `#fff` on `--c-red #e11d2a` | — | 4.76:1 | `.nav__cta`, `.btn--primary`, `.chip--live` — AA pass (AAA fail) |
| `#fff` on `.chip--wwe #c8102e` | — | 5.88:1 | AA |
| `#000` on `.chip--wcw #e2b13c` | — | 10.59:1 | AAA |
| `#000` on `.chip--ecw #b0b0b0` | — | 9.68:1 | AAA |
| `#fff` on `.chip--tna #1e73be` | — | 4.94:1 | AA (close — don't darken this blue) |
| `#000` on `.chip--nxt #f5c518` | — | 12.88:1 | AAA |
| `--c-gold-bright` on `.chip--gold` tint (eff. `#221f12`) | — | 10.62:1 | AAA |
| `--c-win #2fbf71` on elev-3 | — | 6.28:1 | AA |
| `--c-focus #5aa9ff` on bg / elev-3 | — | 8.02 / 6.10:1 | focus ring passes non-text 3:1 comfortably |
| `--c-gold` input border on elev-3 | — | 7.12:1 | non-text pass (but 1px — see §7) |

**Palette verdict:** the black+gold system is very strong (gold is a high-contrast accent on near-black). The **only genuine AA failures are the dim grey (`#6b727d`), the loss red (`#e05263`), and using base red (`#e11d2a`) as small text.** Red and gold are otherwise safe as fills, large text, and non-text UI.

---

## Sources
- [W3C — Understanding SC 2.5.8 Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- [W3C — Understanding SC 1.4.3 Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- [W3C — Understanding SC 1.4.11 Non-text Contrast](https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html)
- [W3C — Understanding SC 2.4.11 Focus Not Obscured (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)
- [W3C — Understanding SC 4.1.3 Status Messages](https://www.w3.org/WAI/WCAG21/Understanding/status-messages.html)
- [W3C — WAI-ARIA Authoring Practices Guide (APG)](https://www.w3.org/WAI/ARIA/apg/)
- [NN/g — The Thumb Zone / designing for mobile reach](https://www.nngroup.com/articles/thumb-zone-mobile/)
- [Baymard — Mobile Form Usability: Never Use Inline Labels](https://baymard.com/blog/mobile-forms-avoid-inline-labels)
- [web.dev — Interaction to Next Paint (INP)](https://web.dev/articles/inp) · [Optimize INP](https://web.dev/articles/optimize-inp)
- [web.dev — Animation and motion (Learn Accessibility)](https://web.dev/learn/accessibility/motion)
- [MDN — prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)
- [Apple Human Interface Guidelines — Buttons / hit targets (44pt)](https://developer.apple.com/design/human-interface-guidelines/buttons) · [TetraLogical — target sizes](https://tetralogical.com/blog/2022/12/20/foundations-target-size/) · [LogRocket — touch target sizes](https://blog.logrocket.com/ux-design/all-accessible-touch-target-sizes/)
- [Smashing Magazine — Best Practices for Mobile Form Design](https://www.smashingmagazine.com/2018/08/best-practices-for-mobile-form-design/) · [UXPin — Error feedback on mobile forms](https://www.uxpin.com/studio/blog/error-feedback-best-practices-mobile-forms/)
- [UXPin — Accessible modals with focus traps (2026)](https://www.uxpin.com/studio/blog/how-to-build-accessible-modals-with-focus-traps/)
- [Tatiana Mac — prefers-reduced-motion: no-motion-first](https://www.tatianamac.com/posts/prefers-reduced-motion)
