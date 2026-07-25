# Membership & Conversion UX Research — MAT Wrestling

> **Scope:** owned-channel growth for a freemium content funnel — free wrestling
> database → free **Insider** account → paid **Ringside** tier, fed by an
> email/SMS **waitlist**. Built as the evidence base for the WWE/TKO *Manager,
> Membership Growth* portfolio.
>
> **How to read this:** every section gives a **Principle**, a **Source**, and an
> **→ Apply to MAT** note that references the real pages/elements we ship:
> `/membership/` (tier cards `.tiers` / `.tier--featured`, `.waitlist-cta`),
> `/membership/growth-strategy/`, the gated full-star-ratings idea, and the
> free-for-SEO content graph (`/wrestlers/`, `/matches/`, `/rivalries/`).
>
> **Current MAT tier reality (as built):** **Fan** `$0/forever` (no signup, full
> crawlable DB) · **Insider** `$0/free to join` (unlocks full star-ratings, classic
> archive, weekly newsletter — *this is the email-capture account*) · **Ringside**
> `$6/mo` (premium archive, watch-alongs, community, member drops, ad-free, early
> features). Waitlist state on page: **12,840 signups, 38% waitlist→member target,
> 4 lifecycle emails.**

---

## 0. The funnel MAT is actually optimizing

```
ACQUIRE            ACTIVATE              CONVERT               RETAIN
SEO/GEO/China  →   free Insider acct  →  Insider → Ringside →  streak/lifecycle
free content       "aha": first        paywall on premium     habit + win-back
pulls traffic      full-rating unlock  archive + watch-along   + referral loop
```

This maps 1:1 to the four-stage model on `/membership/growth-strategy/`
("1 · Acquire … 4 · Convert"). The report below deepens each stage with cited
practice. The single most important framing for the whole document:

> **Principle — Activation is the gate on everything downstream.** "Don't ignore
> activation — or the rest doesn't matter." Baseline freemium→paid conversion sits
> around **~2%**, and improving the **first 5 minutes of onboarding lifts LTV by
> ~50%**. Acquisition volume is wasted if users never reach first value.
> **Source:** CXL, *Optimizing Freemium Conversions Through User Onboarding.*
> **→ Apply to MAT:** treat the **free Insider signup** (not the Ringside
> purchase) as the primary activation event to instrument and optimize. It is the
> hinge: it converts anonymous SEO traffic into a first-party-data owned-channel
> contact, exactly the NYT registration-wall move (below).

---

## 1. Acquisition — free, crawlable content as the top of funnel

**Principle.** In freemium publishing the top of funnel is *content that ranks and
gets cited*, not ads. Keep discovery content free and open; convert on depth and
utility, not on access to the basics. NYT keeps most content free initially "to
encourage discovery and engagement, blocking only after readers demonstrate
sufficient interest."
**Source:** The Audiencers, *The NYT Dynamic Paywall Model, Analyzed*; NYT 2022
annual report (registration lifted conversion **>40%**).

**→ Apply to MAT.** The entire entity graph — `/wrestlers/`, `/matches/`,
`/rivalries/`, `/relationships/` — stays free and crawlable (the **Fan
$0/forever** tier). This is deliberate: those pages are the SEO/GEO acquisition
engine (JSON-LD `Person`/`SportsEvent`/`Review`, `/content/*.md` mirror,
`llms.txt`). **Never gate the pages you want Google and AI answer engines to
index and cite.** Gate the *value-add layer* on top (full numeric star-ratings,
premium archive), which is invisible to and irrelevant for crawlers. The
`/membership/growth-strategy/` "How SEO, GEO & China feed the top of funnel"
section is the correct articulation — keep it.

---

## 2. Activation — the free Insider account & the "aha moment"

**Principle — define one aha moment and drive time-to-value toward it.** The aha
moment is the point a user first *feels* the core value. Best-in-class onboarding
(a) asks 1–3 prequalifying questions to personalize, (b) uses **user-initiated**
tours (self-started tours are **123% more likely to complete** than auto-tours),
(c) surfaces the sticky feature early, and (d) adds *purpose-driven friction* —
Pinterest's "pick 5 topics," which increases investment.
**Source:** CXL (freemium onboarding); Reforge, *Activation: Defining Your Aha
Moment* (setup moment → aha moment distinction).

**→ Apply to MAT.** Define the MAT aha moment explicitly as:

> **"I unlocked the full star-rating on a match I care about."**

Concrete activation flow:
1. **Prequalify at signup** — one question: *"Pick your promotion/era"* (WWE / WCW
   / ECW / TNA / NXT). Mirrors Pinterest soft-friction; personalizes the newsletter
   segment immediately (feeds the `/membership/growth-strategy/` "Segmentation →
   Content fit" plan).
2. **Setup moment** = account created + one follow chosen. **Aha moment** = first
   full rating revealed on a page they arrived on from search.
3. **Instrument** the % of new Insiders who reveal ≥1 gated rating within session 1
   as the north-star activation metric.

---

## 3. Sign-up friction reduction

**Principle.** Ask for the minimum, defer the rest. Single-field-first capture,
no forced password (magic-link / email-code), inline validation, one primary
action per screen, social/OS login options, and never ask twice for data you can
derive. Every extra field measurably drops completion; "purpose-driven friction"
is the *only* friction worth keeping (it raises lead quality).
**Source:** NN/g form-usability guidance; CXL (soft-friction as quality lever);
login/signup UX best-practice guides (2025).

**→ Apply to MAT.** The `.waitlist-cta` already leads with **first name +
email** — good. Rules to hold to:
- **Waitlist = email only** (first name optional). SMS is a *second, separate*
  ask after confirmation, not a launch-blocker (carrier consent needs its own
  explicit opt-in — see §4/§7).
- **Insider signup = email + magic link.** No password wall. Wrestling fans on
  mobile (360px-first) abandon password creation.
- **Never re-ask** the promotion picked at waitlist when they later create the
  Insider account — pass it through.
- Keep the form to **one column, ≥44px targets** (already in the design system).

---

## 4. Waitlist UX & double opt-in

**Principle — confirm intent, then reward it.** Double opt-in trades a little
volume for a much cleaner, higher-deliverability, higher-engagement list: it kills
bot/typo addresses, cuts spam complaints, and protects domain reputation. The
confirmation email must be **transactional, single-CTA, on-brand**, sent
**immediately**, and land on a **celebratory confirmation page** that suggests the
next step. The one downside is losing users who never confirm — mitigate with a
resend.
**Source:** Customer.io, *Double Opt-In Best Practices*; Oracle Marketing Cloud;
Retainful double opt-in examples.

**→ Apply to MAT.** The `.waitlist-cta` copy ("first access at launch + a
founding-member badge … welcome → onboarding → first-value → conversion") is
correctly framed. Add/confirm:
- **Double opt-in on the waitlist.** Confirmation email subject: single job —
  "Confirm your MAT founding spot." The **founding-member badge is the reward for
  confirming**, not for submitting — that turns the extra click into a benefit,
  not a chore.
- **Confirmation landing page** = show live position ("You're #12,841") + the
  referral share module (§9) + a one-tap "Also text me event drops" SMS opt-in.
- Show the **social-proof counter** (12,840 on the waitlist) and the **38%
  target** as momentum signals — visible progress motivates completion (same
  mechanic as Dropbox's referral dashboard, §9).
- **The waitlist → Insider handoff at launch** is the real conversion event:
  every confirmed waitlister should be dropped into the welcome series (§6) with
  a one-click "Claim your free Insider account" magic link — no re-registration.

---

## 5. Free-vs-paid value framing & gating strategy

**Principle — gate on depth/recency/experience, keep discovery free; use a
registration wall as the mid-funnel step.** NYT's three-stage model is the
template: **anonymous → (registration wall) → registered gets more → paywall.**
The registration wall alone lifted conversion **>40%** because it captures
first-party data and enables personalized metering by *propensity to subscribe*.
Gate what deepens engagement for fans who've already shown intent; never gate the
crawlable discovery layer.
**Source:** The Audiencers / INMA (NYT dynamic paywall & ML metering); Zuora
(metered-paywall definition).

**→ Apply to MAT — three-layer gate that matches the built tiers:**

| Layer | Content | Tier | Why |
|---|---|---|---|
| **Free & open** | All entity pages, bios, match lists, relationship graph, *directional* rating (e.g. star icon, "highly rated") | **Fan $0** | SEO/GEO fuel — must stay crawlable & citable |
| **Registration-gated** | **Full numeric star-ratings**, classic-match archive, weekly newsletter | **Insider $0 (signup)** | The registration wall = owned-channel capture; the *"notify me / unlock full rating"* prompt is the conversion surface |
| **Paywalled** | Premium archive, watch-alongs, community, member drops, ad-free, early features | **Ringside $6/mo** | Depth + experience + identity, for die-hards |

- The **gated full-ratings idea is the linchpin**: the page ranks and is cited on
  the *directional* rating, but the *exact* score is the carrot behind the free
  Insider wall. This is NYT's "read the summary free, register for the rest."
- **Feature-gating with explanation** converts better than hard blocks: show the
  rating meter *shrouded* with "Unlock the full MAT rating — free" (Mixpanel-style
  shroud, per CXL), not a dead end.
- **Reverse-trial** the Ringside archive to highly-engaged Insiders (grant a few
  premium reads, then prompt) rather than a blank paywall — CXL flags reverse
  trials as a top freemium→paid lever.

---

## 6. Pricing-page UX & tier design

**Principle.** Three tiers, ordered low→high, with the **recommended tier visually
highlighted** ("Most popular" badge) to anchor choice; scannable benefit rows with
the *difference* between tiers obvious; one clear CTA per card; price framed with
the billing period explicit; anchor the paid tier against a credible "everything
in the tier below" baseline. Reduce choice overload — more than 3–4 tiers depresses
decisions.
**Source:** Baymard (pricing/product-page research); Figma & UXcel pricing-page
best-practice libraries.

**→ Apply to MAT.** The `.tiers` block already does most of this right:
- ✅ 3 tiers, ✅ `tier--featured` + `tier__badge` "Most popular" on **Insider**,
  ✅ "Everything in Insider" anchor line on Ringside, ✅ month-to-month + cancel-
  anytime reassurance in the FAQ (`FAQPage` schema — doubles as GEO).
- **Fixes / tests:**
  - The middle featured tier (Insider) is **free** — unusual but *strategically
    correct*: it makes the "most popular" choice zero-risk and maximizes the
    email-capture registration wall. Keep Insider featured, but make the **Ringside
    CTA the visually dominant paid action** so revenue intent isn't buried.
  - Frame Ringside as **"$6/mo"** with a **micro-anchor** ("less than one PPV
    replay" / annual option at a discount to lift LTV — Headspace's 40%-off annual
    is the cited pattern for habit-forming LTV gains).
  - Make the **benefit delta scannable**: Ringside card should show only the
    *incremental* rows (watch-alongs, premium archive, drops, ad-free) under
    "Everything in Insider," not repeat the full list.
  - **CTA copy per tier:** "Browse free" / "Join free" / "Go Ringside" (already
    good — verbs, not "Submit").

---

## 7. Lifecycle email/SMS UX

**Principle.** Onboarding email sequences must *demonstrate value*, not just
confirm; segment by declared + behavioral data; time conversion prompts to
motivation+ability+trigger (**BJ Fogg model**); reserve SMS for high-urgency,
time-boxed moments (events/drops) with its own explicit consent. Sales-y
interruption during signup fails (**80% of onboarding calls go to voicemail**) —
make deeper touches opt-in.
**Source:** CXL (email onboarding, Fogg-timed prompts); double-opt-in
deliverability guidance; `/membership/growth-strategy/` "Lifecycle campaigns."

**→ Apply to MAT.** The page already commits to **4 lifecycle emails**. Concrete
journey:
1. **Welcome / confirm** (double opt-in) — deliver the founding-member badge; one
   CTA.
2. **First-value** — "Here are the 5 highest-rated matches of the modern era" →
   drives the first full-rating unlock (the aha moment, §2).
3. **Habit** — "New ratings on wrestlers you follow" (behavioral segment from the
   promotion/era picked at signup).
4. **Convert** — reverse-trial Ringside archive/watch-along, Fogg-timed to a live
   event surge ("PPV this Saturday — watch along with Ringside").
- **SMS** = event-surge muscle only (matches `/membership/growth-strategy/`
  "Event-surge muscle"): separate opt-in, used for live drops and PPV watch-along
  reminders, never for routine newsletter.
- **Win-back** journey for lapsed Insiders and churned Ringside (see §11).

---

## 8. Social proof & trust signals

**Principle.** Trust signals lift conversion most when they are **specific,
recent, and near the decision point** — real numbers, named testimonials, and
transparent methodology beat generic badges. For a ratings/authority product,
*editorial credibility* (how you rate) is itself a trust signal (E-E-A-T).
**Source:** Baymard/NN/g trust-UX research; UserIntuition *Trust UX*; The Good,
*Leveraging Social Proof*.

**→ Apply to MAT.**
- **Live counters as social proof:** the **12,840-on-the-waitlist** figure is
  strong proof — surface it on `/membership/` *and* near the Insider signup, not
  just in the `.waitlist-cta`.
- **Methodology = trust:** link `/methodology/` and `/about/` prominently from the
  pricing page — "here's exactly how we rate" answers the "why should I trust the
  score I'm paying to see" objection behind the gate.
- **Named fan testimonials** in a secondary proof strip (already scoped in the
  homepage conversion research) — specific > generic ("rated 3,000 matches"
  beats "great site").
- **Reassurance micro-copy** at the point of payment: "cancel anytime,
  month-to-month, keep access to period end" (already in FAQ — repeat it *on the
  Ringside CTA card*, where the decision happens).

---

## 9. Referral / virality loops

**Principle — double-sided incentive + frictionless share + visible progress.**
Dropbox grew **3,900% in 15 months (100k→4M users)** with a two-sided reward
(both sides get 500MB), placed as the **last step of onboarding** (peak
enthusiasm), a **one-page frictionless share** (contact sync), and a **dashboard
showing progress** toward a cap. The loop is sustained by "thank-you" re-engagement
emails.
**Source:** GrowSurf / Prefinery, *Dropbox Referral Program: 3,900% Growth.*

**→ Apply to MAT — two loops:**
1. **Waitlist referral loop (pre-launch):** on the double-opt-in confirmation page,
   "**Move up the waitlist** — refer 3 friends, jump the line + earn the founding
   Ringside-month." Show live position + progress bar (Dropbox dashboard mechanic).
   This is the highest-leverage pre-launch growth move because the waitlist is
   already the top of funnel.
2. **Member referral loop (post-launch):** two-sided — referrer and friend each get
   **1 free Ringside month**. Place it as the **last step of Insider onboarding**
   and after the aha moment. Frictionless share of a specific asset ("Send a friend
   this match's full rating").

---

## 10. Churn reduction & retention UX

**Principle — build the habit, then defend it; make cancellation a save-flow, not a
button.** Retention comes from (a) a recurring habit loop — Duolingo doubled DAU to
30M+ and grew revenue 45% YoY on **streaks powered by loss aversion + streak-freeze
safety nets** (and monetized the emotional investment); and (b) a **cancellation
flow with save offers** (pause, downgrade, discount, "you'll lose X") instead of a
one-click cancel, plus **dunning** (smart retries + card-update prompts) for
involuntary churn.
**Source:** JustAnotherPM / StriveCloud (Duolingo streak psychology & numbers);
ProsperStack (cancellation-flow examples); Churn Buster (dunning/involuntary churn).

**→ Apply to MAT.**
- **Habit loop = a ratings/prediction streak.** "Rate a match a day" / "predict the
  PPV" streak with a **streak-freeze** (earned or Ringside-perk) — directly maps
  Duolingo's loss-aversion mechanic to wrestling fandom, which is inherently
  event-cadenced (weekly TV + monthly PPV = a natural engagement rhythm).
- **Loss-framed retention email** for lapsing Insiders: "You'll lose your
  400-match streak / your founding badge."
- **Ringside cancellation = save-flow:** offer **pause** (skip a month), **downgrade
  to Insider** (don't lose them to the free tier — keep the owned-channel contact),
  or a **retention discount**, and state exactly what they lose (premium archive,
  watch-alongs, drops). One-click cancel out of the funnel is a leak.
- **Dunning** for the $6/mo card: retry + "update card" email before treating a
  failed charge as churn (involuntary churn is often the largest, most recoverable
  bucket).

---

## 11. Key funnel metrics to instrument

**Principle.** Instrument one primary metric per funnel stage plus the guardrails,
and report weekly (mirrors the job's "weekly funnel readout" duty — already scoped
on `/membership/growth-strategy/` "The weekly funnel readout").
**Source:** Reforge activation/retention framework; CXL benchmarks; NYT metering.

**→ Apply to MAT — the readout:**

| Stage | Primary metric | Guardrail / target |
|---|---|---|
| **Acquire** | Organic + AI-referral sessions to entity pages | Crawl/index coverage, AI-citation count |
| **Capture** | Waitlist signups; **waitlist confirm rate** (double opt-in) | 12,840 → growth rate; % confirmed |
| **Activate** | % new Insiders who unlock ≥1 full rating in session 1 (**aha rate**) | Time-to-first-unlock; onboarding completion |
| **Engage** | WAU/MAU on ratings; streak retention | Follows per user; newsletter CTR |
| **Convert** | **Insider → Ringside %**; **waitlist → member %** (target **38%**) | LP conversion; checkout completion; free→paid (~2% industry baseline to beat) |
| **Monetize** | ARPU; annual-plan take rate | Reverse-trial → paid % |
| **Retain** | Monthly logo + revenue retention; save-flow accept rate | Involuntary (dunning) recovery %; win-back reactivation |
| **Refer** | Viral coefficient (k); referrals per member | Waitlist queue-jump participation |

**A/B test backlog (owned-channel):** waitlist headline & counter visibility ·
double-opt-in subject line · rating-shroud copy ("Unlock" vs "Notify me") ·
Ringside CTA prominence & price framing ($6/mo vs annual anchor) · welcome-series
sequence & send timing · save-flow offer (pause vs discount vs downgrade). This is
the `/membership/growth-strategy/` "A/B testing plan" made concrete.

---

## 12. Cross-platform funnel patterns worth stealing

- **The Athletic / NYT** — registration wall as the mid-funnel data-capture step;
  ML-metered, propensity-based gating; bundle depth for retention. **→ MAT:** free
  Insider = the registration wall; personalize gating by engagement over time.
- **Spotify / Duolingo** — free tier is a genuine product, not a crippled demo;
  habit loop + loss aversion drive retention; premium removes friction (ads) and
  adds depth. **→ MAT:** Fan tier must feel complete; Ringside removes ads + adds
  experience.
- **Patreon / Substack** — creator/community identity and *belonging* convert
  superfans; tiers sell access + status, not just content; the free list is the
  asset that paid is built on. **→ MAT:** founding-member badge, Ringside community
  + drops sell identity; the free Insider list is the durable owned-channel asset.

---

## Sources

- CXL — [Optimizing Freemium Conversions Through User Onboarding](https://cxl.com/blog/freemium-conversions/)
- Reforge — [Activation: Defining Your Aha Moment](https://www.reforge.com/c/retention-series-eg/activation/aha-moment)
- Lenny's Newsletter / Hila Qu — [The Ultimate Guide to Adding a PLG Motion](https://www.lennysnewsletter.com/p/summary-the-ultimate-guide-to-adding)
- The Audiencers — [The New York Times Dynamic Paywall Model, Analyzed](https://theaudiencers.com/the-new-york-times-dynamic-paywall-model-analyzed/)
- INMA — [NYT uses machine learning to create a smarter paywall](https://www.inma.org/blogs/ideas/post.cfm/new-york-times-uses-machine-learning-to-create-a-smarter-paywall)
- Nieman Lab — [NYT adds The Athletic to its all-access digital subscription](https://www.niemanlab.org/2022/06/the-new-york-times-has-added-the-athletic-to-its-all-access-digital-subscription/)
- Zuora — [Metered Paywall: Definition, Implementation, Strategic Benefits](https://zuora.com/glossary/metered-paywall)
- Baymard Institute — [Pricing](https://baymard.com/pricing) · [Product Page UX Research](https://baymard.com/research/product-page)
- Figma — [Pricing Page Best Practices + Examples](https://www.figma.com/resource-library/pricing-page-best-practices/)
- Customer.io — [Double Opt-In Best Practices](https://customer.io/learn/deliverability/double-opt-in-best-practices)
- Oracle Marketing Cloud — [Double Opt-In Best Practices](https://blogs.oracle.com/marketingcloud/double-opt-in-best-practices-for-email-marketing)
- GrowSurf — [The Dropbox Referral Program: 3900% Growth in 15 Months](https://growsurf.com/blog/dropbox-referral-program/)
- Prefinery — [Dropbox Referral Program: 3900% Growth Study](https://www.prefinery.com/blog/dropbox-referral-program-3900percent-growth-study/)
- JustAnotherPM — [The Psychology Behind Duolingo's Streak Feature](https://www.justanotherpm.com/blog/the-psychology-behind-duolingos-streak-feature)
- StriveCloud — [Duolingo Gamification Explained](https://www.strivecloud.io/blog/gamification-examples-boost-user-retention-duolingo)
- ProsperStack — [7 Cancellation Flow Examples — Reduce Churn](https://prosperstack.com/blog/cancellation-flow/)
- Churn Buster — [Subscriber Churn Management](https://churnbuster.io/articles/subscriber-churn-management)
- The Good — [Leveraging Social Proof to Improve Your Conversion Rate](https://thegood.com/insights/social-proof/)
- UserIntuition — [Trust UX: Badges, Proof, and the Research Behind Them](https://www.userintuition.ai/reference-guides/trust-ux-badges-proof-and-the-research-behind-them/)
- Userpilot — [Why Freemium-to-Premium Conversions Are Flopping](https://userpilot.com/blog/freemium-to-premium/)

*Compiled 2026-07-25 for the MAT membership-growth portfolio. Synthesized from the
sources above; figures cited to their originators.*
