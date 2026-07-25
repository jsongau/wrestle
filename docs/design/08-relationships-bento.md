# 08 — Relationships Bento (rivalries, factions, alliances)

## Purpose
Show the thing that makes MAT more than a stats table: the *web* of pro wrestling — rivalries,
factions, betrayals, tag teams. A mixed-span bento grid communicates "this database maps
relationships, not just results," creates visual hierarchy without any photography, and plants
the "advanced connections are a member feature" seed.

## Layout & structure
- `.section-head` (eyebrow → H2 → `.rule-gold`) over a `.bento` grid.
- `.bento` auto-fits `minmax(220px,1fr)`; feature cells use `.is-wide` (span 2 columns) to
  break the uniform-card look.
- Recommended composition (desktop):
  - **1 wide "hero rivalry" cell** (`.is-wide`) — the marquee feud, poster-styled.
  - **2–3 standard cells** — factions / tag teams / betrayals.
  - **1 wide "relationship graph" teaser** (`.is-wide`) — a stylized node/edge motif with a
    member-only marker.
- **Mobile (`≤560px`):** `.is-wide` reverts to single-column (`grid-column:auto`); everything
  stacks in reading order.

## Components & CSS classes
- `.section-head`, `.eyebrow`, `.rule-gold`, `.link-more`.
- `.bento`, `.bento > .is-wide`.
- Cells use `.card` (hover lift) or `.card--edge` (gradient border) for the feature cells;
  reuse `.tile__mono` for oversized ghost initials, `.rel` / `.rel__type` chips for the small
  relationship rows, and `.chip--gold` "Members" markers on the premium teaser.
- The rivalry cell can embed a compact `.tale` (Tale of the Tape) with the red `.vs`.
- `.pattern-hatch` behind the graph-teaser cell for "material" texture.

## Content
Section head: eyebrow `THE WEB`, H2 `Rivalries, factions & betrayals`.
Cells:

1. **Wide — Marquee rivalry:** kicker `GREATEST RIVALRY`, `Bret Hart vs Shawn Michaels`,
   a `.tale` line (`12 matches · 1992–2010 · The Montreal Screwjob`), CTA `See the feud →`.
2. **Faction:** `The nWo`, `.rel__type` "Faction", `WCW · 1996`, "14 members mapped".
3. **Tag team:** `The Hardy Boyz`, `.rel__type` "Tag Team", "TLC pioneers".
4. **Betrayal:** `Hulk Hogan turns heel`, `.rel__type` "Betrayal", `Bash at the Beach '96`.
5. **Wide — Graph teaser (member-only):** kicker `MEMBERS`, `Explore the relationship graph`,
   blurb `Every alliance, rivalry, and double-cross — mapped and filterable.`,
   `.chip--gold` "Member feature", CTA `Unlock with membership →`.

## Interactions & motion
- **Hover elevation** on `.card`/`.card--edge`; gradient border warms on feature cells.
- Optional `.tile__spot` pointer glow on the wide cells.
- **Scroll reveal + stagger:** bento children carry `[data-reveal]` + `--i`.
- The graph-teaser can have a subtle CSS "pulse" on its member marker (reuse `.chip--live`
  pulse or a gold variant) — reduced-motion safe (animation off).
- Reduced motion: reveals show instantly; borders warm without motion.

## Accessibility
- Each cell is a card with a single primary link (stretched-link pattern); ghost initials
  `aria-hidden`.
- The member-only teaser must be clearly labelled as such in text ("Member feature"), not
  color-only, so no fan feels tricked.
- Maintain reading order in the DOM to match visual order after the bento reflows on mobile.
- `.tale`/`.rel` content is real text with sufficient contrast.

## SEO/GEO notes
- Relationship data (feuds, factions, dates) as visible text is highly citable — phrase key
  facts as one-sentence statements ("The nWo debuted in WCW in 1996").
- Real internal links to feud/faction pages extend topical depth.
- Consider `ItemList` for the cells; individual feud pages can carry richer schema.
