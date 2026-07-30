# CM Punk Dossier Rebuild + SEO/GEO + Rail Fix + Triple H Veil — Production Deploy (2026-07-30)

## What shipped (3 production pushes, all on `main`)
- **`c934f696`** — CM Punk page rebuilt + home floater/cabinet + AJ Styles record fix.
- **`c54e1e87`** — CM Punk SEO title tweak (keeps career-record keywords + epithet).
- **`289bb215`** — sticky-rail spacing fix (all dossier pages) + Triple H kayfabe veil.

Approval tags: `cm-punk-30JUL26-approved` (c934f696), `rail-hhh-30JUL26-approved` (289bb215).

### CM Punk (`wrestlers/cm-punk/index.html`)
Rebuilt on the **AJ Styles `profile-main` template** (two-column layout + Tale-of-the-Tape rail),
replacing the old Biography-style page. 12 numbered sections: Overview, The Record, Signature
Matches, Championships, Factions, Personas, Career Timeline, Rivalries, Media & Gaming,
**MMA Record (UFC)**, Official & Reference, FAQ.
- **152-match rec2 ledger** in the AJ row format (Result · Date · Promo · Event · Opponent ·
  Stipulation · Title), driven by AJ's inline rec2 JS. 57 career-defining default scope; promo
  filter (ROH/TNA/ECW/WWE/AEW/IND) + tag filter with live counts; kayfabe W/L donut; sortable.
  Opponents are **plain text** (zero 404 risk). Only JS params swapped: `PROMO_LABEL` + total (→152).
- **Signature Matches = 8-card horizontal inline-scroll reel**; only the two matches with real pages
  link (`cm-punk-vs-cena-mitb-2011`, `samoa-joe-vs-cm-punk-roh-2004`), the rest are non-link plates.
- **MMA is spoiler-free** (own `.rec2-scroll`, never gets the record's `.rec2-spoiler` shield) with a
  Roufusport camp card (coach Duke Roufus; teammates A. Pettis, T. Woodley, B. Askren, S. Pettis).
  Placed **after** the wrestling sections per request.
- Fuller Overview + full 12-reign title history sourced from `data/cm-punk.md` (new).
- **SEO/GEO**: keyword title, enriched JSON-LD @graph (Person w/ `sameAs` to Wikipedia/WWE/IG/X,
  awards, height/weight, nationality, hasOccupation; WebPage w/ `speakable`; BreadcrumbList; FAQPage),
  `og:image` + `summary_large_image`, verified internal links (rivals, Overview entities). Already in
  sitemap.

### Home (`index.html`, `css/site.css`)
- Ticket floater (`.wev-a`) is **click-only** (minimized until clicked; `apply()` open condition
  reduced to `pinned`). Both corner floaters (`.wev-a`, `.f2-explore`) hidden at ≤760px.
- Cabinet "Pull a file" gains CM Punk + AJ Styles with custom branded **SVG marks** animated on hover
  (CM Punk Pepsi-globe + straight-edge X; AJ interlocked monogram). The cabinet FILES array + render
  live **inline in `index.html`** (NOT `js/home-modules.js`, which is a dead duplicate).

### AJ Styles (`wrestlers/aj-styles/index.html`)
- Removed the two W/L captions ("as booked on this card", "Change the card above and the book follows").
- **Fixed the record scroll window** (also fixes CM Punk): `capRows()` measured the first 8 rows in
  DOM order, but in career-defining scope most are `display:none` (height 0), so on `fonts.ready` it
  collapsed the window to ~175px (~2 rows). Now counts only visible rows (`offsetHeight>0`) → shows 8.

### Sticky rail spacing (`css/profile.css`) — all dossier pages
The `@media(min-width:1200px)` rule dropped `.rail` to `calc(var(--nav-h) + 14px)` = 76px, but the
sticky header stack (nav + subnav + idn) is taller, so the rail's top was tucked under the nav.
Both rail rules now use `calc(var(--stack-top) + 28px)` → clears the stack with an ~18px gap.
Note: `--nav-h:62px` / `--idbar-h:52px` are stale vs the rendered heights (the ticker/idn are taller);
fix is scoped to `.rail` to avoid touching subnav/idn sticky offsets.

### Triple H (`wrestlers/triple-h/index.html`)
Already on `profile-main`, but his W/L donut showed the 7–8 record **openly**. Added the **kayfabe
veil**: donut + legend blur behind a "The book is kayfabe protected / Turn spoilers on" panel
(`.record-top.is-veiled` + `.rt-veil`), wired to his existing `#hhhSpl` toggle plus a new unveil
button (`setSpoilers(on)` refactor). His curated 15-bout landmark ledger and data are untouched.

## Big trap discovered — the cloud clone had drifted from production
Before deploying, the cloud workspace `main` was **behind live prod by a 366-file / ~92k-line commit**
(`5e3bff6c`, "This Week widget… luxury-zoom thumbnails, blur removed") that this clone never fetched,
plus it carried a stale duplicate of the AJ rebuild already on prod. Bundling as-is would have
reverted that production work.
**Fix / lesson:** always `git fetch origin main` and compare before deploying from the cloud. Here:
`git reset --hard origin/main` to resync to live, then re-apply the session's edits onto the current
files (regenerate CM Punk from the live AJ template; re-apply floater/cabinet/AJ patches via a script
with exact-string asserts), re-verify, then push as a clean fast-forward.

## Deploy target (confirmed)
- **GitHub:** `origin https://github.com/jsongau/wrestle.git`, branch `main`. Push to `main`
  auto-deploys on Vercel.
- **Cloud sandbox has no push creds** by default (`git push` → "could not read Username"). This session
  pushed directly via a user-supplied **fine-grained PAT used inline only** (never written to the repo
  or to `origin`'s URL; user asked to revoke it after). Alternative path on file: bundle
  (`git bundle create wrestle-media.bundle HEAD --not origin/main`) → user runs `deploy.sh`.
- **Verify deploys** by WebFetch of the live URL with a cache-buster (`?v=...`), since WebFetch caches
  15 min per URL.

## Verification
- Playwright headless Chromium (local static server): CM Punk 152 rows / 8 in window / 8 signatures /
  spoiler-free MMA; AJ + CM Punk + HHH rail gap 18px, no cutoff; HHH donut veiled by default and
  reveals on toggle/unveil; JSON-LD parses; **zero 404s** in authored content; zero console errors.
- Live deploy confirmed via WebFetch: CM Punk title + Roufusport + Tale of the Tape live; HHH
  "kayfabe protected" + "Turn spoilers on" live.

## Known / pre-existing (not this session's scope)
- Three dead links in `components/meganav.html` site-wide: `/titles/nxt-championship/`,
  `/tag-teams/ftr/`, `/tag-teams/the-steiner-brothers/`. Fixing touches the shell + re-stamps all
  pages — deferred.

## Exact next steps (candidates)
1. Fix the three shell 404s (build the pages or render as non-link plates), then `apply_shell.py`.
2. Roll the same profile-main rebuild to `the-rock` and any remaining old-template wrestler pages.
3. Submit the CM Punk URL to Google Search Console for re-indexing.
4. Real portrait images for the hero "PHOTO SLOT".
