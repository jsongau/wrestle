# Match pages: spoiler reveal + video modal, and the Undertaker flagship build

Date: 2026-07-29
Author: technical build spec for Wrestle Lore
Scope: `/matches/*` detail pages (30 live) + the flagship `/matches/undertaker-vs-hbk-wm25/`

---

## 0. What this document is

Two jobs live in one request, at two different scopes. Keep them separate or the plan gets muddy.

- **Site-wide mechanic (all 30 match pages):** hide the winner behind a click-to-reveal cover with an oscillating "who wins" meter, and turn the fake video button into a real thumbnail that plays inside a centered on-page modal.
- **Flagship deep build (one page):** rebuild `undertaker-vs-hbk-wm25` into the reference example: full buildup, a playlist of embedded official videos, a career-trajectory timeline for both men, and a documentaries row.

The important architectural finding up front, because it changes everything: **the centered modal player already exists in this codebase and is fully built.** `css/site.css` defines `.wl-modal*` and the `.yt` media engine; `js/media.js` exposes `WL.openModal(id, title, opts)` and auto-mounts every `.yt[data-yt-id]` facade on load. It runs today on `/media/` and `/moments/`. The match pages simply never opted in — they use an older dumb `.facade` button that opens a YouTube *search* in a new tab. So the video half of this request is mostly wiring, not building. We reuse the approved component instead of inventing a second one.

---

## 1. Current state (verified in the repo)

- **30 match detail pages** under `matches/<slug>/index.html`, all hand-authored HTML (there is no per-page generator; `apply_shell.py` only stamps the shared nav/footer). The rich prose on each page is hand-written and must be preserved.
- **Winner is shown in the open** on 29 of 30 pages via `.tale` block: `<span class="chip chip--win">Winner</span>` / `chip--loss`. It is also stated in the "Result" row of the tale-of-the-tape table, in the opening sentence of "The Story", in the FAQ answer, and in the JSON-LD.
- **Video is fake.** Every page has:
  ```html
  <div class="embed">
    <button class="facade" onclick="window.open('https://www.youtube.com/results?search_query=...','_blank')">
      <span class="facade__ph">WM25</span><span class="facade__btn">▶</span>
      <span class="facade__label">Watch on WWE / YouTube — official upload</span>
    </button>
  </div>
  ```
  No real embed, no thumbnail, sends the user off-site to a search page. This is the box in the screenshot.
- **`data/matches.json`** already carries a verified `video.id` for most matches (the same IDs re-verified this session). This is our slug to video-ID source of truth.
- **Media engine contract** (from `media.js`), the markup we emit for a real facade:
  ```html
  <div class="yt" data-yt-id="VIDEOID" data-yt-title="…" data-yt-creator="WWE"
       data-yt-dur="30:45" data-yt-page="/matches/…/" data-yt-service="Peacock"
       data-yt-service-url="https://www.peacocktv.com/…">
    <a class="yt__link" href="https://www.youtube.com/watch?v=VIDEOID">Title fallback</a>
  </div>
  ```
  With no JS it degrades to the plain `<a>` link. With JS, `WL.init()` (auto-called on `DOMContentLoaded`) injects the thumbnail, play button and title chrome, and a click calls `WL.openModal` — the centered `.wl-modal` lightbox with a `youtube-nocookie` autoplay iframe, a "watch on YouTube" link, and a streaming-home promo card. Loading `media.js` also adds the `.js` class to `<html>`.
- **Bonus already in the engine:** `openModal` builds a playlist from *every* `.yt[data-yt-id]` on the page (`descriptorsFromDOM`) and auto-advances. So a page with five embeds becomes a five-video binge session inside the modal, at no extra cost. This is why the flagship page wants several embeds.

---

## 2. PART A — Winner spoiler reveal (all match pages)

### 2.1 The interaction

Replace the static Winner/Defeated chips in the `.tale` block with a cover the fan taps to reveal.

- The two names stay visible (that is the matchup, not the spoiler). What is hidden is *who won*.
- Over the result sits a cover reading **TAP TO REVEAL THE WINNER** with a small lock/eye glyph.
- Behind the label runs a tension meter: a glowing marker that sweeps left and right between the two names on a loop, as if it can't decide. This is the "back and forth to create excitement" beat.
- On hover (desktop) the cover brightens and the sweep speeds up. The cue is always readable, never a mystery-meat click.
- On click, the meter snaps to the winner's side, the cover dissolves, and the WINNER / DEFEATED chips animate in. The snap-to-winner is the payoff.
- The tale-of-the-tape "Result" row is covered by the same reveal so the winner can't leak from the table one line down.

### 2.2 Accessibility, SEO, and no-JS (non-negotiable)

This follows the existing `[data-reveal]` rule in `site.css` ("gated behind `.js` so content is ALWAYS visible without JS").

- The winner text stays in the DOM. The cover is CSS applied **only** when `.js` is present. Crawlers, the JSON-LD, and no-JS users see the winner plainly — no ranking or answer-box loss.
- The cover is a real `<button>` with `aria-expanded` and an accessible name ("Reveal the winner"). Keyboard: Enter/Space reveals. On reveal, focus moves to the result and it is announced.
- `prefers-reduced-motion: reduce` freezes the sweep to a centered static bar. No motion sickness, cue still legible.
- Reveal state is remembered for the session (in-memory; optional `localStorage` per slug on the live site) so it doesn't re-hide on back-button.

### 2.3 Markup + classes (new, scoped `.wl-sp*`)

```html
<div class="tale wl-spoiler" data-winner="left">   <!-- left|right|draw -->
  <div class="wl-sp__side">
    <div class="tale__name"><a href="/wrestlers/the-undertaker/">The Undertaker</a></div>
    <span class="chip chip--win wl-sp__verdict">Winner</span>
  </div>
  <div class="vs">VS</div>
  <div class="wl-sp__side">
    <div class="tale__name"><a href="/wrestlers/shawn-michaels/">Shawn Michaels</a></div>
    <span class="chip chip--loss wl-sp__verdict">Defeated</span>
  </div>

  <button class="wl-sp__cover" type="button" aria-expanded="false" aria-controls="tale-verdict">
    <span class="wl-sp__meter" aria-hidden="true"><i class="wl-sp__marker"></i></span>
    <span class="wl-sp__cue">Tap to reveal the winner</span>
  </button>
</div>
```

Result row in the table gets the same treatment, its value wrapped in `<span class="wl-sp__hide">…</span>` revealed by the same control (data attribute links them, or one control per page toggles a page-level `.is-revealed`).

CSS sketch (final version lives in `site.css`, scoped, tokens only — no new colors):
```css
.js .wl-spoiler .wl-sp__verdict{opacity:0;visibility:hidden;transition:opacity .35s var(--ease);}
.js .wl-spoiler .wl-sp__cover{position:absolute;inset:0;display:grid;place-content:center;gap:.6em;
  background:linear-gradient(160deg,var(--c-bg-elev-2),var(--c-bg-elev-1));cursor:pointer;border:0;}
.wl-sp__meter{position:relative;width:min(72%,320px);height:8px;border-radius:var(--r-pill);
  background:var(--c-bg-elev-3);overflow:hidden;}
.wl-sp__marker{position:absolute;top:0;bottom:0;width:34%;border-radius:inherit;
  background:linear-gradient(90deg,var(--c-red),var(--c-gold));animation:wl-sp-sweep 1.6s ease-in-out infinite alternate;}
@keyframes wl-sp-sweep{from{left:0;}to{left:66%;}}
.wl-sp__cover:hover .wl-sp__marker{animation-duration:.9s;}
.wl-sp__cue{font-family:var(--font-cond);letter-spacing:.06em;text-transform:uppercase;color:var(--c-gold-bright);}
.wl-spoiler.is-revealed .wl-sp__cover{opacity:0;pointer-events:none;transition:opacity .3s;}
.wl-spoiler.is-revealed .wl-sp__verdict{opacity:1;visibility:visible;}
@media (prefers-reduced-motion:reduce){.wl-sp__marker{animation:none;left:33%;}}
```

JS: ~15 lines. On click, add `.is-revealed`, snap the marker to `data-winner`, set `aria-expanded="true"`, move focus. Draws (e.g. Samoa Joe vs Punk, `data-winner="draw"`) reveal "Time-limit draw" and the marker parks center.

### 2.4 Scope question for you (see decision block at the end)

The at-a-glance result (VS card + Result row) is the clean spoiler target. The prose Story and the FAQ *discuss* the finish by nature — that is the deep-dive content people scroll for. Two options: (A) cover only the VS card + Result row, leave the narrative as reading you opt into; (B) also blur the winner's name in the Story's first sentence and the FAQ answer until reveal. A is simpler and standard; B is stricter. My recommendation is A.

---

## 3. PART A — Video thumbnail to centered modal (all match pages)

### 3.1 Approach: reuse the existing engine, do not build a new one

Swap the dumb `.facade` search button for a real `.yt` facade (section 1 markup) and include `/js/media.js` on the match pages. That is the whole feature:

- Real YouTube thumbnail (from `i.ytimg.com`), play button, title chrome — injected by `WL.mountFacades`.
- Click opens `WL.openModal`: the centered `.wl-modal` lightbox, autoplay `youtube-nocookie` iframe, Esc/backdrop/✕ to close, closing kills the iframe so audio stops. The fan never leaves the page — exactly the ask.
- The modal already shows a streaming-home promo card (Peacock for WWE/WCW/ECW/NXT, TNA+ for TNA, HonorClub for ROH) — good-will link that also reads as an official, rights-respecting site.

### 3.2 Which pages get a real embed

Only pages with an oembed-verified **official** upload (rule from project memory: never embed fan re-uploads). Source the ID from `matches.json`. Pages with `video.id: null` — the two Benoit matches (scrubbed), Sting/Hogan Starrcade (delisted), Terry Funk/Sabu (never posted), plus a few others — keep a **poster + link-out** to the official streaming home. No fake embed, no fan upload.

Slug to verified ID comes straight from `matches.json` (28 have IDs). The transform reads that file; no hand-mapping.

### 3.3 Per-page wiring

Each match page needs, once: the `/js/media.js` script tag (cache-busted by `apply_shell.py`). No inline init — `media.js` self-boots. The transform adds it if absent.

---

## 4. Rollout architecture (how we touch 30 pages safely)

**Chosen approach: one idempotent Python transform, in the existing `build_*.py` family.** Not 30 hand-edits (drift, error), not a from-scratch generator (would destroy hand-authored prose — see the `preserve-approved-work` rule).

`build/build_match_kit.py` (name TBD) does exactly three surgical edits per `matches/<slug>/index.html`, then leaves everything else byte-for-byte:

1. **Video:** find the `.facade` block, replace with the `.yt` facade using `matches.json[slug].video`. If `video.id` is null, replace with the poster + streaming link-out variant instead.
2. **Winner:** wrap the `.tale` block's verdict chips in the `.wl-spoiler` shell and cover; wrap the table "Result" value in `.wl-sp__hide`. Read `data-winner` side from `participants[].winner`.
3. **Assets:** ensure `<script src="/js/media.js">` and the tiny reveal script/class are present.

**Idempotency is mandatory** (same trap that bit `build_rankings.py`): the script must detect already-transformed pages (presence of `.yt` / `.wl-spoiler`) and no-op or re-sync rather than double-wrap. Runs clean on repeat. Verified across 3 runs before deploy.

**Affected files:**
- `css/site.css` — add the scoped `.wl-sp*` block (append; no edits to existing rules).
- `js/media.js` — already exists, no change. New tiny reveal handler: either append to an existing match-page JS or a small `js/matchkit.js` (~20 lines).
- `matches/<slug>/index.html` × 30 — transformed in place.
- `build/build_match_kit.py` — new generator.
- No schema, no backend, no data migration. `data/matches.json` is read-only input here.

**Success criteria:**
- Every match page: winner hidden until click; meter sweeps; reveal snaps + animates; no-JS shows winner.
- Every page with an official ID: thumbnail shows, click opens centered modal, closes cleanly, audio stops on close.
- Null-ID pages: poster + link-out, no fan upload, no broken embed.
- Lighthouse/CLS unaffected (facade is a thumbnail, iframe only mounts on click). JSON-LD winner intact. Reduced-motion respected. Keyboard reveal works.

---

## 5. PART B — The flagship: `undertaker-vs-hbk-wm25`

Built by hand (not the transform) so the deep prose is authored, not generated. It becomes the template every other match page aspires to. New section order:

1. **Hero** — title, event line, the WWE / The Streak / era chips (kept).
2. **The result, hidden** — the `.wl-spoiler` VS card is the first thing you meet: two legends, a sweeping meter, "tap to reveal". Rating box (5.0) stays beside it; the rating is not the spoiler, the winner is.
3. **Watch the match** — the real WM25 embed (`Gd54flkPtL4`) as the primary `.yt` facade → modal.
4. **The buildup** — how a match with no title and barely a feud became the anticipated one (section 5.1).
5. **The match, beat by beat** — entrances (light vs darkness), the near-falls, the dive that nearly went wrong, the finish, the ratings debate (section 5.2).
6. **Watch how it fits** — the embedded playlist: first meeting, the rematch, the trilogy capstone, the day the Streak died, the documentary (section 5.3). Because they are all `.yt` on one page, the modal auto-advances them.
7. **Where both men went next** — the trajectory timeline (section 5.4).
8. **Go deeper** — documentaries row (section 5.5).
9. **FAQ + Related** — kept, extended.

### 5.1 The buildup (facts to write from; cite the marked ones)

There was no long grudge and no belt. Michaels set his sights on the one thing in wrestling that could not be bought or booked: the Undertaker's undefeated WrestleMania Streak, 16-0 going in. WWE sold it as light against darkness — Michaels making his entrance bathed in white and descending from above, the Undertaker rising through smoke and dark. The hook was mystique versus the self-belief of the man who calls himself Mr. WrestleMania. The build was short and image-driven rather than a personal war; the personal war came a year later at WM26. [Sources: Bleacher Report "How Triple H, Undertaker, Shawn Michaels Crafted Epic 4-Year WrestleMania Saga"; Pro Wrestling Stories "Shawn Michaels and Undertaker: Secret History Behind Feud".]

### 5.2 The match (facts)

- WrestleMania XXV, April 5, 2009, Reliant Stadium, Houston. Crowd about 72,000. The Streak stood at 16-0; a win made it 17-0.
- The match built through a run of near-falls so convincing the live crowd repeatedly bought the Streak ending. Peak danger: the Undertaker's dive over the top rope to the floor, meant to be caught by a cameraman, went wrong and he landed close to head-first. The real risk sharpened the drama rather than breaking it. [Sources: Sportskeeda "moments that were unscripted"; TJR Wrestling review.]
- Finish: Michaels went for a moonsault, the Undertaker caught him and hit the Tombstone Piledriver for the three-count.
- Ratings: Dave Meltzer gave 4.75 stars; Cagematch community sits around 9.6/10; it won most 2009 match-of-the-year honors and is routinely voted the greatest WrestleMania match ever. Meltzer has since spoken about why it stopped just short of five. [Sources: Cagematch; ITR Wrestling "Meltzer reveals why it didn't get five stars".]

### 5.3 Embedded videos (all oembed-verified this session — official only)

| Role on page | Match | YouTube ID | Channel | Verified title |
|---|---|---|---|---|
| **The match** | Undertaker vs HBK, WM25 | `Gd54flkPtL4` | WWE | FULL MATCH: Undertaker vs. Shawn Michaels: WrestleMania XXV |
| **First meeting** (prequel) | Badd Blood 1997, first-ever Hell in a Cell | `BvZ2KQuCTds` | WWE Vault | FULL MATCH: Undertaker vs. Shawn Michaels — Hell in a Cell: Badd Blood 1997 |
| **The rematch** (follow-up / next chapter) | WM26, Streak vs Career | `ljb34LNhGQw` | WWE | FULL MATCH: The Undertaker vs. Shawn Michaels - Streak vs. Career No DQ |
| **Trilogy capstone** (trajectory) | WM28, End of an Era, HIAC, HBK as ref | `FOoSvAeFPP4` | WWE | FULL MATCH - Undertaker vs. Triple H – Hell in a Cell: WrestleMania XXVIII |
| **The Streak dies** (trajectory) | WM30, Lesnar 21-1 | `2mVEtkh5CQs` | WWE | Brock Lesnar snaps The Undertaker's Streak — WM30: 42 Greatest Moments |
| **Documentary** | The Last Ride, Chapter 1 | `k8yQlJIr7EY` | Undertaker (official channel) | FULL EPISODE: The Last Ride — Chapter 1 |

Note on the last one: `k8yQlJIr7EY` is the official Last Ride episode but posted on the verified **@Undertaker** channel, not @WWE. It is official WWE content, not a fan upload, so it satisfies the no-fan-uploads rule in spirit. Flagged for your call in the decision block; easy to swap for a @WWE-channel chapter or drop to link-out if you'd rather keep the allowlist strict.

Link-outs (not embedded, no verified single-official-video or better as a link): WM25 full entrances, Michaels' farewell speech the night after WM26, the other Last Ride chapters. All point at official WWE/Peacock.

### 5.4 Trajectory timeline (both men, after WM25)

**The Undertaker's Streak and long goodbye**
- WM25 (2009) 17-0 over Michaels.
- WM26 (2010) 18-0 over Michaels again — Streak vs Career, and Michaels retired. The rematch was set up when Michaels, denied a rematch, cost the Undertaker the World Heavyweight Championship at Elimination Chamber 2010 to force his hand. [Source: GiveMeSport; Sportskeeda WM26 rewind.]
- WM27 (2011) 19-0 over Triple H, No Holds Barred.
- WM28 (2012) 20-0 over Triple H inside Hell in a Cell, "End of an Era", Shawn Michaels the special referee — the trilogy's last chapter.
- WM29 (2013) 21-0 over CM Punk.
- WM30 (2014) **21-1** — Brock Lesnar ended it, one of the most stunned crowds in company history. [Source: WWE "42 Greatest Moments"; ESPN.]
- Later WrestleManias, then the Boneyard Match cinematic bout vs AJ Styles at WM36 (2020), a Final Farewell at Survivor Series in November 2020, and induction into the WWE Hall of Fame in 2022. [Source: Sportskeeda HOF 2022.]

**Shawn Michaels after the last bell**
- Retired at WM26 (2010); the WM25/WM26 pair is the send-off he has called his true farewell. [Source: Yardbarker.]
- WWE Hall of Fame, 2011.
- Broke an eight-year retirement once, at Crown Jewel 2018 (D-Generation X vs the Brothers of Destruction) — the exception that made the point.
- Now runs the developmental brand as WWE's head of creative for NXT and a senior talent-development executive, the trainer shaping the next generation.

### 5.5 Documentaries row

Card row linking the long-form: **Undertaker: The Last Ride** (2020 five-part docuseries; Chapter 1 embedded above, rest link to Peacock), plus a link to WWE's Shawn Michaels retrospectives. Each card is a poster + a "watch on Peacock / YouTube" line, styled like the `.yt` facades so the row reads as one system.

### 5.6 Copy rules (binding, from `my-writing-style`)

Every visible string on this page: no arrow glyphs in UI copy, no em-dash as a sentence separator, no underlined links, plain nouns, none of the banned hype words (unleash, elevate, dive into, game-changer, and the rest). Chinese pages pair characters with pinyin. Run the style self-check before ship. The buildup and match prose above is drafted in that voice; keep it there.

### 5.7 SEO / schema

Keep the winner in the DOM and the existing `SportsEvent` + `Review` + `FAQPage` + `BreadcrumbList` JSON-LD intact (the spoiler is visual only). Add `VideoObject` JSON-LD for the primary embed (name, description, thumbnailUrl from `i.ytimg.com`, uploadDate, embedUrl) — a real ranking win for a video page and currently missing. Extend Related links to the four embedded matches. Internal links to both wrestler profiles, the WM26 page, the WM28 page, and `/rankings/`.

---

## 6. Open decisions (need your call before the multi-page rollout)

1. **Reveal scope** — cover the VS card + Result row only (recommended), or also blur the winner in the Story/FAQ prose?
2. **Rollout order** — build the Undertaker flagship first and approve it as the template, then run the transform across the other 29 (recommended), or transform all 30 at once?
3. **Last Ride embed** — accept the official @Undertaker-channel documentary embed, or keep the strict @WWE-only allowlist and make it a link-out?

---

## 7. Sources

- WWE — Undertaker def. Shawn Michaels, WrestleMania 25 (official result).
- Cagematch — Shawn Michaels vs. The Undertaker (community rating).
- ITR Wrestling — Meltzer on why it fell short of five stars.
- TJR Wrestling — WM25 and WM26 match reviews.
- Bleacher Report — the four-year Undertaker/Michaels/Triple H saga.
- Pro Wrestling Stories — Michaels & Undertaker secret history.
- Sportskeeda — unscripted Undertaker moments; WM26 rewind; Hall of Fame 2022.
- GiveMeSport — retiring Michaels in 2010.
- Yardbarker — Michaels on WM26 as his true farewell.
- WWE / ESPN — Brock Lesnar ends the Streak, WM30.
- oembed verification (this session): Gd54flkPtL4, BvZ2KQuCTds, ljb34LNhGQw, FOoSvAeFPP4, 2mVEtkh5CQs (WWE / WWE Vault); k8yQlJIr7EY (Undertaker official channel).
