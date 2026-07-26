# MAT BUILD MANIFEST — canonical slugs + shared markup (agents MUST follow exactly)

All pages are static HTML at `/root/wwe/`. Link CSS as `/css/site.css` and JS as `/js/main.js`
(already built — DO NOT recreate them). Base URL for canonical/OG tags: `https://wrestlelore.com`.

## Slug rule
Lowercase; drop periods, apostrophes, quotes, parentheses; spaces → hyphens.

## Wrestler slugs (path: /wrestlers/<slug>/index.html)
1 stone-cold-steve-austin · 2 the-rock · 3 the-undertaker (DONE) · 4 shawn-michaels · 5 triple-h ·
6 mick-foley · 7 bret-hart · 8 hulk-hogan · 9 sting · 10 goldberg · 11 diamond-dallas-page ·
12 chris-jericho · 13 eddie-guerrero · 14 rey-mysterio · 15 kurt-angle · 16 brock-lesnar · 17 kane ·
18 batista · 19 john-cena · 20 randy-orton · 21 edge · 22 cm-punk · 23 daniel-bryan · 24 aj-styles ·
25 samoa-joe · 26 christopher-daniels · 27 bully-ray · 28 seth-rollins · 29 roman-reigns ·
30 jon-moxley · 31 kevin-owens · 32 finn-balor · 33 shinsuke-nakamura · 34 becky-lynch ·
35 charlotte-flair · 36 mercedes-mone · 37 bayley · 38 trish-stratus · 39 lita · 40 cody-rhodes · 41 ric-flair

When cross-linking a wrestler, ONLY link if they are one of the 41 above (use `/wrestlers/<slug>/`).
Anyone else (e.g. Kane's Team Hell No partner is fine, but Michelle McCool, Sami Zayn, Gargano,
Ciampa, Stephanie McMahon, AJ Lee, The Usos, Dominik) → plain text, no link.

## Match slugs (path: /matches/<slug>/index.html) — from data/matches.md
bret-hart-vs-austin-wm13 · hbk-vs-undertaker-badd-blood-1997 · rey-mysterio-vs-eddie-guerrero-halloween-havoc-1997 ·
nwo-formation-bash-at-the-beach-1996 · sting-vs-hogan-starrcade-1997 · goldberg-vs-hogan-nitro-1998 ·
terry-funk-vs-sabu-born-to-be-wired-1997 · tlc-2-wrestlemania-x-seven-2001 · rock-vs-austin-wm-x-seven-2001 ·
angle-vs-benoit-royal-rumble-2003 · lesnar-vs-angle-wm19-2003 · benoit-vs-triple-h-vs-hbk-wm20-2004 ·
hbk-vs-angle-wm21-2005 · undertaker-vs-angle-no-way-out-2006 · undertaker-vs-hbk-wm25 (DONE) ·
undertaker-vs-hbk-wm26-2010 · cm-punk-vs-cena-mitb-2011 · undertaker-vs-triple-h-wm28-2012 ·
bryan-vs-cena-summerslam-2013 · daniel-bryan-wm30-2014 · rollins-cash-in-wm31-2015 ·
rousey-charlotte-becky-wm35-2019 · styles-vs-daniels-vs-joe-unbreakable-2005 · samoa-joe-vs-cm-punk-roh-2004 ·
sami-zayn-vs-neville-takeover-revolution-2014 · bayley-vs-sasha-banks-takeover-brooklyn-2015 ·
almas-vs-gargano-takeover-philadelphia-2018 · gargano-vs-ciampa-takeover-new-orleans-2018 ·
adam-cole-vs-gargano-takeover-xxv-2019 · sasha-banks-vs-bianca-belair-wm37-2021

## Rivalry slugs (path: /rivalries/<slug>/index.html)
austin-vs-mcmahon · rock-vs-austin · undertaker-vs-kane · the-bloodline · gargano-vs-ciampa ·
nwo-invasion · bret-vs-hbk-montreal · shield-rise-and-betrayal · yes-movement · cm-punk-pipebomb ·
eddie-vs-rey · tlc-tag-wars · attitude-era-invasion · sting-vs-flair · dx-vs-nation

## Promotion slugs (path: /promotions/<slug>/index.html): wwe · wcw · ecw · tna · nxt

===================================================================================
## SHARED HEADER (paste verbatim right after <body> and the skip-link)
===================================================================================
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap"><nav class="nav" aria-label="Primary">
  <a class="brand" href="/"><span class="brand__mark"><span>M</span></span> MAT</a>
  <button class="nav__toggle" aria-label="Toggle menu" aria-controls="primary-menu" aria-expanded="false">&#9776;</button>
  <ul class="nav__menu" id="primary-menu">
    <li class="nav__item"><a class="nav__link" href="/wrestlers/">Wrestlers</a></li>
    <li class="nav__item"><a class="nav__link" href="/matches/">Matches</a></li>
    <li class="nav__item"><a class="nav__link" href="/rivalries/">Rivalries</a></li>
    <li class="nav__item"><a class="nav__link" href="/relationships/">Relationships</a></li>
    <li class="nav__item"><a class="nav__link" href="/rankings/">Rankings</a></li>
    <li class="nav__item"><a class="nav__link" href="/zh/">中文</a></li>
    <li class="nav__item"><a class="nav__cta" href="/membership/">Join MAT Insider</a></li>
  </ul>
</nav></div></header>

===================================================================================
## SHARED FOOTER (paste verbatim before <script> at end of <body>)
===================================================================================
<footer class="site-footer"><div class="wrap"><div class="footer-bottom">
  <span>© <span data-year>2026</span> MAT — Pro Wrestling Database.</span>
  <span class="disclaimer">Fan-made educational project. Not affiliated with, endorsed by or sponsored by WWE or TKO Group Holdings. All trademarks and match footage are property of their respective owners.</span>
</div></div></footer>
<script src="/js/main.js" defer></script>

===================================================================================
## VIDEO EMBED (use this — opens official search; verified IDs drop in later)
===================================================================================
<div class="embed">
  <button class="facade" type="button"
    onclick="window.open('https://www.youtube.com/results?search_query=WWE+OFFICIAL+SEARCH+TERMS','_blank','noopener');return false;"
    aria-label="Watch DESCRIPTION">
    <span class="facade__ph">LABEL</span><span class="facade__btn" aria-hidden="true">▶</span>
    <span class="facade__label">Watch on WWE / YouTube — official upload</span>
  </button>
</div>

## PAGE REQUIREMENTS (every page)
- <!doctype html><html lang="en"> ; <meta charset> ; viewport ; unique <title> and meta description.
- <link rel="canonical"> + hreflang en / zh-Hans (/zh/...) / x-default ; OG + Twitter tags ; theme-color #0a0b0d.
- <link rel="stylesheet" href="/css/site.css">.
- JSON-LD: BreadcrumbList always; Person for wrestlers; SportsEvent + Review(with reviewRating/aggregateRating) for matches; FAQPage where an FAQ is shown.
- Breadcrumb nav (.crumbs) at top of <main id="main">.
- Answer-first `<p class="answer">` opening summary (GEO). 3+ FAQ (<details> in .faq) with matching FAQPage JSON-LD.
- Dense internal links to related wrestlers/matches/rivalries (the link graph is the point).
- End every page with a "Related" .related-links block.
