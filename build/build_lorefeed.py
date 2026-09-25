#!/usr/bin/env python3
"""Lore Feed generator — the newsroom of Wrestle Lore.
ONE source (DISPATCHES) emits, all in sync:
  /lore-feed/                    -> hub: current-week editorial front page + browse-by-week index
  /lore-feed/<YYYY-MM-DD>/       -> one SEO/GEO page per Monday-week (recap + dispatches + schema)
  components/meganav.html        -> the site-wide ticker's .rt-item markup = the rolling last-7-days items
  css/site.css                   -> the .lf-* editorial styles (idempotent block)
  sitemap.xml                    -> +weekly URLs
Then run `python3 build/apply_shell.py` to stamp the ticker across all pages.
To add news: append ONE dict to DISPATCHES, rerun this, then apply_shell.py.
Weekly PAGES bucket Monday..Sunday; the TICKER is a rolling 7-day window from build day.
ROOT overridable: WL_ROOT=/path python3 build/build_lorefeed.py ; date via WL_TODAY=YYYY-MM-DD.
Also emits self-contained previews to /tmp for review (WL_PREVIEW_DIR).
"""
import os, re, datetime, html as _html

ROOT = os.environ.get("WL_ROOT", "/root/wwe")
BASE = "https://wrestlelore.com"
TODAY = datetime.date.fromisoformat(os.environ["WL_TODAY"]) if os.environ.get("WL_TODAY") else datetime.date.today()
PREVIEW_DIR = os.environ.get("WL_PREVIEW_DIR", "/tmp/lf-preview")

def esc(s): return _html.escape(str(s), quote=True)

# ------------------------------------------------------------------ DATA
# cat: title|event|signing|departure|return|business|media|roster|retirement|passing
# promo: wwe|nxt|aew|tna|njpw|tko|industry   official: True=promotion-confirmed, False=trade report
DISPATCHES = [
  # ================= WEEK OF SEPTEMBER 21 - SEPTEMBER 25, 2026 (in progress) =================
  # Assembled Sep 25. 946 kidnaps Sikoa on Raw; Penta replaces him and qualifies
  # for MITB; Dusty Classic begins on NXT; AEW All Out go-home. SmackDown 9/25
  # airs tonight - preview card only, no results. See build/add_week_0921.py.

  # ---- WWE: Raw Sep 21 (San Antonio) ----
  dict(date="2026-09-21", promo="wwe", cat="event", official=True, who="Solo Sikoa", lead=True, mono="946 Strikes", home=True, htags="matches rivalries",
       hl="946 ambushes and kidnaps Solo Sikoa from Raw in San Antonio",
       dek="The faction 946 attacked Solo Sikoa backstage before his MITB qualifying match, threw him into an SUV and sped away. The Usos and Jacob Fatu pursued but could not intervene. Penta was inserted as Sikoa\u2019s replacement and won the triple threat to qualify for Money in the Bank.",
       src="Yahoo Sports", url="https://sports.yahoo.com/articles/solo-sikoa-attacked-kidnapped-946-021209655.html"),
  dict(date="2026-09-21", promo="wwe", cat="event", official=True, who="Penta",
       hl="Penta wins MITB qualifier after replacing kidnapped Solo Sikoa on Raw",
       dek="Penta beat Dominik Mysterio and Dragon Lee in a triple threat after being inserted into the match following Sikoa\u2019s abduction by 946. Penta earlier confronted Judgment Day, calling Mysterio the king of the pendejos.",
       src="WrestleView", url="https://www.wrestleview.com/wwe-raw-results/392979-live-wwe-raw-results-september-21-2026-san-antonio/"),
  dict(date="2026-09-21", promo="wwe", cat="event", official=True, who="Roxanne Perez",
       hl="Roxanne Perez qualifies for Women\u2019s Money in the Bank on Raw",
       dek="Perez pinned IYO SKY and La Catalina in a triple threat to earn her spot in the women\u2019s MITB ladder match on October 10 in New Orleans.",
       src="Fightful", url="https://www.fightful.com/wrestling/wwe-raw-results-9-21-2026-mitb-qualifiers-bayley-vs-lyra-valkyria-penta-la-knight-more/"),
  dict(date="2026-09-21", promo="wwe", cat="media", official=True, who="Liv Morgan",
       hl="Liv Morgan calls her title loss the Santiago Screwjob as Becky Lynch takes credit",
       dek="Morgan said she was robbed of the Women\u2019s World Championship on Raw and labelled the September 12 Chile live event the Santiago Screwjob. Becky Lynch claimed responsibility and demanded first dibs at a title match against new champion Stephanie Vaquer.",
       src="WrestleView", url="https://www.wrestleview.com/wwe-raw-results/392979-live-wwe-raw-results-september-21-2026-san-antonio/"),
  dict(date="2026-09-21", promo="wwe", cat="media", official=True, who="LA Knight",
       hl="LA Knight vows to take Roman Reigns\u2019 World Heavyweight Championship",
       dek="Knight cut a promo on Raw noting that Reigns has had no Bloodline interference recently and claiming he is the most self-made fighter in the game. He challenged Reigns for the World Heavyweight Title.",
       src="WrestleView", url="https://www.wrestleview.com/wwe-raw-results/392979-live-wwe-raw-results-september-21-2026-san-antonio/"),
  dict(date="2026-09-21", promo="wwe", cat="return", official=True, who="Oba Femi", home=True, htags="roster rivalries",
       hl="Oba Femi returns to Raw and attacks Bron Breakker after DQ finish",
       dek="After Je\u2019Von Evans beat Bron Breakker by disqualification when The Vision interfered, Oba Femi made a surprise return and laid out Breakker. The attack signals a feud between the two powerhouses.",
       src="Fightful", url="https://www.fightful.com/wrestling/wwe-raw-results-9-21-2026-mitb-qualifiers-bayley-vs-lyra-valkyria-penta-la-knight-more/"),

  # ---- NXT Sep 22 (The CW) ----
  dict(date="2026-09-22", promo="nxt", cat="event", official=True, who="Creed Brothers", home=True, htags="matches",
       hl="Dusty Rhodes Tag Team Classic kicks off on NXT with two first-round wins",
       dek="The Creed Brothers beat Jax Presley and Harley Riggins while Romeo Moreno and Noam Dar upset Los Americanos to advance to the quarterfinals. Robert Stone announced the tournament\u2019s return last week.",
       src="PW Torch", url="https://www.pwtorch.com/site/2026/09/23/nxt-tv-results-9-22-dusty-rhodes-tag-team-classic-legacy-zilla-fatu-ek-prosper-vs-birthright-kali-armstrong-vs-skylar-raye/"),
  dict(date="2026-09-22", promo="nxt", cat="media", official=True, who="Grayson Waller",
       hl="Grayson Waller and Mason Rook trade words as NXT Title feud heats up",
       dek="NXT Champion Waller and challenger Rook had a heated war of words, with Rook declaring himself the best big man in the game. Thea Hail earned a future title match by teaming with La Catalina to beat Zaria and Kelani Jordan.",
       src="WWE.com", url="https://www.wwe.com/shows/wwenxt/2026-09-22"),

  # ---- AEW: Dynamite + Collision Sep 23 (Indianapolis) ----
  dict(date="2026-09-23", promo="aew", cat="signing", official=True, who="Mike Bailey", home=True, htags="roster",
       hl="Speedball Mike Bailey joins Will Ospreay\u2019s United Empire on Dynamite",
       dek="Bailey officially debuted as a member of the United Empire alongside AEW World Champion Will Ospreay on the All Out go-home show. AEW confirmed Bailey\u2019s signing earlier in the week.",
       src="Fightful", url="https://www.fightful.com/wrestling/speedball-mike-bailey-joins-united-empire-on-aew-dynamite/"),
  dict(date="2026-09-23", promo="aew", cat="title", official=True, who="Persephone",
       hl="Persephone retains TBS Championship over Hyan and issues All Out open challenge",
       dek="The TBS Champion used an underhanded finish to beat Hyan on the Dynamite portion of the combined show, then announced a TBS Title open challenge for All Out on September 27.",
       src="AEW", url="https://www.allelitewrestling.com/post/aew-dynamite-collision-results-september-23-2026"),
  dict(date="2026-09-23", promo="aew", cat="title", official=True, who="Swerve Strickland",
       hl="Swerve and The New Level retain AEW World Trios Titles ahead of All Out",
       dek="Swerve Strickland and The New Level defended the World Trios Championship against The Demand on Dynamite. Their All Out opponents, The Good The Bad and The Ugly, were confirmed for the pay-per-view.",
       src="Fightful", url="https://www.fightful.com/wrestling/aew-dynamite-results-9-23-2026-persephone-vs-hyan-swerve-new-level-vs-demand-will-ospreay-more/"),
  dict(date="2026-09-23", promo="aew", cat="event", official=True, who="Will Ospreay",
       hl="Will Ospreay and Jon Moxley come face to face in final All Out build",
       dek="The AEW World Champion and his challenger closed the combined Dynamite-Collision show with a confrontation in Indianapolis. Ospreay defends against Moxley at All Out on Saturday, September 27 in Chicago.",
       src="AEW", url="https://www.allelitewrestling.com/post/aew-dynamite-collision-results-september-23-2026"),

  # ---- TNA iMPACT Sep 24 (San Antonio) ----
  dict(date="2026-09-24", promo="tna", cat="event", official=True, who="Syx", home=True, htags="rivalries",
       hl="Mystery faction Syx revealed as Joseph Sawyer and Samuel Shaw on iMPACT",
       dek="After weeks of ambushing wrestlers, the attackers of The Hardy Brothers unmasked as Joseph Sawyer and Samuel Shaw, forming the faction Syx. The Hardys challenged Sawyer and Shaw to a match next week.",
       src="TNA Wrestling", url="https://tnawrestling.com/news/tna-thursday-night-impact-on-amc-live-results-september-24-2026"),
  dict(date="2026-09-24", promo="tna", cat="title", official=True, who="Mustafa Ali",
       hl="Mustafa Ali retains TNA International Title in controversial triple threat",
       dek="Ali struck Trey Miguel with the championship belt and rolled him up to retain the International Championship in a triple threat that also featured Jason Hotch. Tasha Steelz assisted Ali during the finish.",
       src="TNA Wrestling", url="https://tnawrestling.com/news/tna-thursday-night-impact-on-amc-live-results-september-24-2026"),
  dict(date="2026-09-24", promo="tna", cat="event", official=True, who="Ryan Nemeth",
       hl="Ryan Nemeth qualifies for Bound for Glory X-Division Championship match",
       dek="Nemeth beat KJ Orso with the Hollywood Ending to secure his spot in the X-Division title match at Bound for Glory. Order 4 fractured as Mila Moore and John Skyler quit the faction after Ali discovered their relationship.",
       src="Ringside News", url="https://www.ringsidenews.com/tna-impact-results-highlights-key-moments-september-24-2026"),

  # ---- Industry / Business ----
  dict(date="2026-09-24", promo="industry", cat="business", official=True, who="WWE",
       hl="WWE Main Event moves to Rumble streaming platform starting October 14",
       dek="WWE and Rumble announced a long-term partnership to stream Main Event every Wednesday at 8 PM ET on Rumble.com and its apps, replacing its previous Peacock home. The move adds another distribution channel for weekly WWE content.",
       src="WWE Corporate", url="https://corporate.wwe.com/about/news/2026/09-24-2026-0"),
  dict(date="2026-09-25", promo="wwe", cat="event", official=True, who="CM Punk",
       hl="SmackDown tonight: CM Punk vs. Gunther vs. Finn Balor in MITB qualifier",
       dek="Tonight\u2019s SmackDown in Indianapolis features a triple threat to fill the last men\u2019s MITB spot, plus Trick Williams defends the United States Title against Baron Corbin in a steel cage and Charlotte Flair battles Giulia and Lash Legend for a women\u2019s ladder match spot.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-09-25"),
  # =============== end week of September 21 - September 25, 2026 ===============

  # ================= WEEK OF SEPTEMBER 14 - SEPTEMBER 20, 2026 (in progress) =================
  # Backfilled Sep 20, current through today. Reigns turns back Penta in Mexico
  # City; Zayn's first defense; RAF 13 in Miami. See build/add_week_0914.py.

  # ---- WWE: Raw Sep 14 (Arena CDMX) + SmackDown Sep 18 (Corpus Christi) ----
  dict(date="2026-09-14", promo="wwe", cat="title", official=True, who="Roman Reigns", lead=True, mono="World Title", home=True, htags="matches titles",
       hl="Roman Reigns spears Penta to retain World Heavyweight Title in Mexico City",
       dek="Reigns survives multiple Mexican Destroyers and pins Penta with a Superman Punch and spear at 22:25 before a devastated Arena CDMX crowd.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/09/14/wwe-raw-results-9-14-kellers-report-on-roman-reigns-vs-penta-for-the-world-title-gable-vs-lee-for-ic-title-mitb-qualifying-matches-more/"),
  dict(date="2026-09-18", promo="wwe", cat="title", official=True, who="Sami Zayn", home=True, htags="titles rivalries",
       hl="Sami Zayn retains WWE Title over Kevin Owens as CM Punk interferes on SmackDown",
       dek="In his first SmackDown as Undisputed WWE Champion, Zayn beats Owens after Punk strikes Owens with the title belt; Punk lays out both men to close the show.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/09/18/wwe-smackdown-results-9-18-kellers-report-on-sami-zayn-celebrating-his-wwe-title-win-mitb-qualifiers-cody-rhodes-addresses-orton/"),
  dict(date="2026-09-14", promo="wwe", cat="title", official=True, who="Chad Gable",
       hl="Chad Gable taps out Dragon Lee to keep Intercontinental Championship on Raw",
       dek="Gable counters a Styles Clash into a grapevined ankle lock and forces Lee to submit at 15:40, then raises his hand in a show of respect.",
       src="Wrestling Inc", url="https://www.wrestlinginc.com/2258569/wwe-raw-chad-gable-dragon-lee-mens-intercontinental-title-retains/"),
  dict(date="2026-09-14", promo="wwe", cat="event", official=True, who="Je'Von Evans",
       hl="Je'Von Evans and Lola Vice win Money in the Bank qualifiers on Raw",
       dek="Evans beats Austin Theory and Big Cass in a triple threat while Vice defeats Raquel Rodriguez and Kelani Jordan to reach the October 10 ladder matches in New Orleans.",
       src="Pro Wrestling Dot Net", url="https://prowrestling.net/site/2026/09/14/wwe-raw-results-9-14-powells-live-review-of-roman-reigns-vs-penta-for-the-world-heavyweight-championship-chad-gable-vs-dragon-lee-for-the-intercontinental-title-mitb-qualifiers/"),
  dict(date="2026-09-18", promo="wwe", cat="media", official=True, who="Cody Rhodes",
       hl="Cody Rhodes tells Michael Cole he will not repeat his mercy toward Randy Orton",
       dek="In a sit-down interview on SmackDown, Rhodes says he refuses to compromise himself to win but vows he will not make the same decision he made at Sunday Night's Main Event.",
       src="Pro Wrestling Dot Net", url="https://prowrestling.net/site/2026/09/18/wwe-smackdown-results-9-18-barnetts-live-review-of-new-wwe-champion-sami-zayns-appearance-michael-coles-interview-with-cody-rhodes-money-in-the-bank-qualifiers/"),
  dict(date="2026-09-18", promo="wwe", cat="event", official=True, who="Trick Williams",
       hl="Trick Williams and Jacy Jayne claim Money in the Bank spots on SmackDown",
       dek="Williams wins a triple threat over Randy Orton and Rey Fenix while Jayne pins Alexa Bliss in a three-way also involving Jade Cargill.",
       src="Fightful", url="https://www.fightful.com/wrestling/wwe-smackdown-results-9-18-2026-sami-zayn-appears-mitb-qualifiers-more/"),

  # ---- AEW: Dynamite Sep 16 (Norfolk) + Collision Sep 19 (Charleston) ----
  dict(date="2026-09-16", promo="aew", cat="event", official=True, who="Jon Moxley", home=True, htags="matches rivalries",
       hl="Death Riders lay out United Empire as Moxley trio wins Dynamite main event",
       dek="Jon Moxley, PAC and Gabe Kidd beat Will Ospreay, Andrade El Idolo and Francesco Akira in Norfolk, and the Death Riders and The Dogs beat down United Empire to close the show. Ospreay defends the AEW World Championship against Moxley at All Out in Chicago on September 26.",
       src="Fightful", url="https://www.fightful.com/wrestling-news/aew-dynamite-results-9-16-2026-united-empire-vs-death-riders-jamie-hayter-vs-lena-kross-more"),
  dict(date="2026-09-16", promo="aew", cat="roster", official=True, who="Mercedes Mone", home=True, htags="titles roster",
       hl="Mercedes Mone not medically cleared for All Out due to broken nose",
       dek="AEW announced the Women's World Champion, whose nose was broken by Willow Nightingale at All In, will miss All Out in Chicago. Nightingale faces Thekla at All Out with the winner challenging Mone at WrestleDream in Orlando this October.",
       src="SEScoops", url="https://www.sescoops.com/article/top-aew-champion-mercedes-mone-not-cleared-to-compete-at-all-out-2026"),
  dict(date="2026-09-14", promo="aew", cat="signing", official=False, who="Ilja Dragunov",
       hl="Ilja Dragunov reportedly set to sign with AEW after WWE exit",
       dek="Fightful Select reports the former WWE United States Champion is expected to sign with AEW barring unforeseen circumstances, after his WWE contract expired with no 90-day non-compete. The deal was not yet finalized as of the report.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/09/14/major-name-reportedly-expected-to-sign-with-aew/"),
  dict(date="2026-09-15", promo="aew", cat="media", official=True, who="All Elite Wrestling",
       hl="AEW announces Hulu Japan streaming deal for Dynamite, Collision and pay-per-views",
       dek="AEW and Hulu Japan jointly announced that Dynamite, Collision and live pay-per-view events will stream exclusively in Japan on Hulu Japan starting November 2026. New episodes will no longer be added to NJPW World.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/09/15/xaew-announces-that-dynamite-collision-and-ppvs-will-air-in-japan-on-hulu-japan/"),
  dict(date="2026-09-19", promo="aew", cat="title", official=True, who="Andrade El Idolo",
       hl="Andrade retains National Title on Collision and PAC issues All Out challenge",
       dek="Andrade El Idolo beat Daniel Garcia in Charleston to retain the AEW National Championship, after which PAC attacked him and challenged for the title at All Out. Darby Allin also retained the TNT Championship against Myron Reed.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/09/19/aew-collision-results-9-19-moxley-vs-zachary-wentz-darby-vs-myron-reed-for-the-tnt-title-thekla-vs-zayda-steel-andrade-vs-garcia-for-the-national-title/"),

  # ---- RAF 13 Sep 18 / NXT Sep 15 / TNA Sep 17 / NJPW / industry ----
  dict(date="2026-09-18", promo="raf", cat="event", official=True, who="Colby Covington", home=True, htags="matches",
       hl="Covington blanks Belal Muhammad 10-0 to retain RAF crossover crown at RAF 13",
       dek="Covington kept the Cruiserweight Crossover title with a 10-0 tech fall shutout in Miami. Khamzat Chimaev beat Gilbert Burns 15-4 and Joe Pyfer routed Luke Rockhold 14-3, while Arsen Harutyunyan took the bantamweight belt from Austin DeSanto 6-3.",
       src="Fightful", url="https://www.fightful.com/mma/raf-13-results-9-18-colby-covington-beats-belal-muhammad-khamzat-chimaev-wins/"),
  dict(date="2026-09-15", promo="nxt", cat="event", official=True, who="Mason Rook",
       hl="Mason Rook wins triple threat to earn NXT Title shot at Grayson Waller",
       dek="Rook beat Tony D'Angelo and Saquon Shugars to become number one contender. AAA champ La Catalina brawled with Kelani Jordan, and Robert Stone announced the return of the Dusty Tag Team Classic.",
       src="WWE.com", url="https://www.wwe.com/shows/wwenxt/2026-09-15"),
  dict(date="2026-09-17", promo="tna", cat="event", official=True, who="Moose",
       hl="Moose saves TNA career against Kazarian as Bound for Glory card takes shape",
       dek="Moose beat Frankie Kazarian in 16:54 with consecutive spears to keep his TNA job, then smashed a crown with a chair. Rich Swann pinned LJ Cleary to reach the X-Division title match at Bound for Glory, and Eddie Edwards challenged Ricky Sosa for the show.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/09/17/tna-impact-9-17-results-moose-saves-tna-career-rich-swann-advances-to-bound-for-glory/"),
  dict(date="2026-09-20", promo="njpw", cat="event", official=True, who="Yota Tsuji",
       hl="NJPW locks in full Destruction in Kobe card topped by Tsuji versus Goto",
       dek="Yota Tsuji defends the IWGP Heavyweight title against Hirooki Goto on September 27, with Gabe Kidd against Drilla Moloney for the Global belt and Konosuke Takeshita against Shun Skywalker for the TV title. G1 winner Ryohei Oiwa challenges the Kobe winner at King of Pro Wrestling on October 12.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/09/20/njpw-confirms-full-card-for-destruction-in-kobe/"),
  dict(date="2026-09-16", promo="industry", cat="business", official=False, who="CM Punk",
       hl="Allstate Arena advertises four matches for WWE and AAA Worlds Collide",
       dek="The Rosemont venue is promoting CM Punk, Rey Mysterio and El Grande Americano against Dominik Mysterio, JD McDonagh and Omos for September 26, plus Penta and Rey Fenix against Los Perros del Mal. Over 10,900 tickets are out for a show running opposite AEW All Out.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/09/16/allstate-arena-advertising-four-matches-for-wwe-worlds-collide/"),
  dict(date="2026-09-17", promo="industry", cat="roster", official=False, who="Flip Gordon",
       hl="Flip Gordon reenlists in Army National Guard while vowing ring return",
       dek="After 11 years as a pro, Gordon reenlisted in the Army National Guard and said his wrestling career continues, including a return to CMLL. The same update noted Chris Bey underwent his first stem cell therapy session in his neck injury recovery.",
       src="F4W/WON", url="https://www.f4wonline.com/news/daily-updates/daily-update-wwe-notes-flip-gordon-chris-bey/"),
  # =============== end week of September 14 - September 20, 2026 ===============

  # ================= WEEK OF SEPTEMBER 7 - SEPTEMBER 13, 2026 =================
  # Backfilled Sep 20. Zayn ends Punk's reign in Mexico City; Vaquer takes the
  # Women's World Title in Chile; AEW mourns The Butcher. See build/add_week_0907.py.

  # ---- WWE: Raw Sep 7 + SmackDown Sep 11 (Arena CDMX, Mexico City) ----
  dict(date="2026-09-11", promo="wwe", cat="title", official=True, who="Sami Zayn", lead=True, mono="WWE Title", home=True, htags="titles matches",
       hl="Sami Zayn stuns CM Punk to capture Undisputed WWE Championship in Mexico City",
       dek="Kevin Owens accidentally struck Punk with the belt and Zayn followed with a Helluva Kick to win the title at Arena CDMX, ending Punk's 67-day reign.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-09-11"),
  dict(date="2026-09-07", promo="wwe", cat="title", official=True, who="Liv Morgan", home=True, htags="titles rivalries",
       hl="Liv Morgan retains Women's World Title over Stephanie Vaquer with Judgment Day help",
       dek="Raquel Rodriguez and Roxanne Perez ran interference and Becky Lynch tried to even the odds, but Morgan struck Vaquer with the belt and hit Oblivion to retain on Raw.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-09-07"),
  dict(date="2026-09-12", promo="wwe", cat="title", official=False, who="Stephanie Vaquer", home=True, htags="titles",
       hl="Stephanie Vaquer beats Liv Morgan for Women's World Title at live event in Chile",
       dek="Five nights after falling to Morgan on Raw, Vaquer captured the Women's World Championship at a WWE live event in her native Chile, a rare title change away from television.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/09/12/stephanie-vaquer-wins-wwe-womens-world-championship-at-live-event-in-chile/"),
  dict(date="2026-09-07", promo="wwe", cat="return", official=True, who="Bayley",
       hl="Bayley makes shocking return during Money in the Bank qualifier on Raw",
       dek="Bayley pulled the referee out of the ring to cost Lyra Valkyria, allowing Sol Ruca to hit the Sol Snatcher and qualify for the Money in the Bank ladder match.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-09-07"),
  dict(date="2026-09-07", promo="wwe", cat="event", official=True, who="Bron Breakker",
       hl="Money in the Bank qualifiers begin as arson angle closes out Raw",
       dek="Bron Breakker speared Rey Mysterio to win a triple threat qualifier. Royce Keys, Bronco Nima and Lucien Price set The Usos car ablaze in an ominous warning.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-09-07"),
  dict(date="2026-09-08", promo="wwe", cat="business", official=True, who="WWE",
       hl="WWE announces eight new Raw and SmackDown dates across the United States",
       dek="The fall and winter run adds stops including Greenville, Fort Lauderdale, Raleigh, Wichita and Toledo from November 9 through December 7, with presale opening September 10.",
       src="WWE Corporate", url="https://corporate.wwe.com/about/news/2026/09-08-2026"),
  dict(date="2026-09-12", promo="wwe", cat="media", official=True, who="Cody Rhodes",
       hl="Cody Rhodes misses advertised Mexico City SmackDown, sit-down interview set",
       dek="Rhodes was advertised but did not appear following his Sunday Night's Main Event loss to Randy Orton. WWE announced a Michael Cole sit-down interview for the September 18 SmackDown in Corpus Christi.",
       src="TJRWrestling", url="https://tjrwrestling.net/news/cody-rhodes-immediate-wwe-future-confirmed/"),
  dict(date="2026-09-12", promo="wwe", cat="media", official=True, who="CM Punk",
       hl="CM Punk breaks silence on Instagram after losing WWE Title to Sami Zayn",
       dek="Punk posted to Instagram Stories that winners lose way more than losers do and vowed I will get MY title back, signing off BITW.",
       src="F4W Online", url="https://www.f4wonline.com/news/wwe/cm-punk-issues-statement-after-losing-wwe-title-to-sami-zayn/"),

  # ---- AEW: Rebel Heart Dynamite Sep 9 + Collision Sep 12 ----
  dict(date="2026-09-12", promo="aew", cat="passing", official=True, who="Andy Williams", home=True, htags="roster",
       hl="AEW honors Andy Williams as Daniel Garcia wins Butcher Battle Royale for charity",
       dek="Collision in Springfield opened with a 10-bell salute for The Butcher, dead at 48, with tributes from Brody King, Colt Cabana, Jeff Jarrett and a note from The Blade read by Tony Schiavone. Garcia last eliminated Josh Alexander to win the 12-man Butcher Battle Royale, earning 100,000 dollars for charity in Williams' memory and receiving his guitar.",
       src="All Elite Wrestling", url="https://www.allelitewrestling.com/post/aew-collision-results-september-12-2026"),
  dict(date="2026-09-09", promo="aew", cat="event", official=True, who="Will Ospreay",
       hl="Will Ospreay pins David Finlay in eliminator as Jon Moxley watches from commentary",
       dek="On the Rebel Heart edition of Dynamite from Akins Ford Arena in Athens, Georgia, world champion Ospreay countered a Finlay powerbomb and pinned him to keep his All Out date with Moxley intact. Andrade El Idolo retained the National Championship over The Beast Mortos, and the show opened with an In Memory Of graphic for Andy Williams plus a farewell ovation for Rebel.",
       src="WrestleView", url="https://www.wrestleview.com/top-story/392277-aew-dynamite-results-9-9-26-rebel-heart-dynamite-title-matches-return-of-the-waiting-room-and-more/"),
  dict(date="2026-09-09", promo="aew", cat="title", official=True, who="Swerve Strickland",
       hl="Swerve Strickland and New Level retain AEW World Trios titles on Rebel Heart Dynamite",
       dek="Strickland, Kofi and Austin Creed hit the Daybreak to put away Orange Cassidy, Kyle O'Reilly and Roderick Strong of the Conglomeration. Britt Baker also tapped out Hyan with the Lockjaw in six-woman action alongside new TBS champion Persephone and Hikaru Shida.",
       src="PWMania", url="https://www.pwmania.com/aew-dynamite-results-september-9-2026"),
  dict(date="2026-09-10", promo="aew", cat="media", official=False, who="Will Ospreay",
       hl="Ospreay clips drive AEW YouTube numbers after emotional Rebel Heart edition of Dynamite",
       dek="Eleven hours after upload, Rebel Heart Dynamite videos totaled 907k tracked views, with Ospreay-related clips at 252k, or 27.8 percent of all episode uploads. The top single video was Rebel handing Britt Baker her signature glove at 110k views.",
       src="F4W Online", url="https://www.f4wonline.com/news/aew/aew-dynamite-rebel-heart-youtube-metrics/"),
  dict(date="2026-09-12", promo="aew", cat="event", official=True, who="Jon Moxley",
       hl="Jon Moxley turns away Mike Bailey on Collision as Mercedes Mone watches from commentary",
       dek="Moxley hit the Death Rider near the 20-minute limit to win a Continental Title eliminator two weeks before challenging Ospreay at All Out. Women's world champion Mone sat in on commentary for Queen Aminata's win over Mina Shirakawa, PAC and The Dogs beat Bang Bang Gang, and AEW announced Blood and Guts for November 4 in Jacksonville.",
       src="Fightful", url="https://www.fightful.com/wrestling/aew-collision-results-9-12-2026-tribute-to-the-butcher-andy-williams/"),

  # ---- NXT Sep 8 / TNA Sep 10 / NJPW / RAF / industry ----
  dict(date="2026-09-10", promo="tna", cat="event", official=True, who="Nic Nemeth", home=True, htags="titles rivalries",
       hl="Nic Nemeth uses wrench to retain TNA World Title over Matt Hardy",
       dek="Nemeth beat Hardy in a No Disqualification main event in Brampton after Ryan Nemeth pulled the referee from the ring and a wrench shot set up the pin. Xia Brookside retained the Knockouts World Title over Gabby Forza with a belt shot behind the referee's back.",
       src="TNA Wrestling", url="https://tnawrestling.com/news/tna-thursday-night-impact-on-amc-results-september-10-2026"),
  dict(date="2026-09-08", promo="nxt", cat="event", official=False, who="Kelani Jordan",
       hl="Kelani Jordan retains NXT Women's Title as Waller challenger picture takes shape",
       dek="Jordan beat Jaida Parker and was attacked afterward by Wren Sinclair, who was suspended by Robert Stone; Jackson Drake also retained the North American Title over Tavion Heights. Tony D'Angelo, Mason Rook and Saquon Shugars won a six-man qualifier, setting next week's triple threat to name NXT Champion Grayson Waller's next challenger.",
       src="eWrestlingNews", url="https://www.ewrestlingnews.com/results/nxt-results/wwe-nxt-results-september-8-2026"),
  dict(date="2026-09-10", promo="tna", cat="event", official=True, who="Leon Slater",
       hl="Leon Slater found unconscious as Bound for Glory world title build turns violent",
       dek="Slater, who challenges Nemeth for the TNA World Title at Bound for Glory, was found laid out backstage before the main event, with the Nemeth brothers implicated. Frankie Kazarian accepted Moose's challenge for next week on the condition that Moose's entire TNA career is on the line.",
       src="TNA Wrestling", url="https://tnawrestling.com/news/tna-thursday-night-impact-on-amc-results-september-10-2026"),
  dict(date="2026-09-09", promo="njpw", cat="event", official=False, who="Hirooki Goto",
       hl="Goto and YOH beat Tsuji and Ishimori on Road to Destruction in Tokyo",
       dek="Hirooki Goto and YOH downed IWGP Heavyweight Champion Yota Tsuji and Taiji Ishimori in 13:30 at Korakuen Hall ahead of Goto's title challenge at Destruction in Kobe on September 27. Claudio Castagnoli also appeared on screen and accepted Shingo Takagi's challenge for the Kobe card.",
       src="Fightful", url="https://www.fightful.com/wrestling/njpw-road-to-destruction-results-9-9/"),
  dict(date="2026-09-08", promo="raf", cat="event", official=False, who="Khamzat Chimaev",
       hl="RAF 13 card finalized with Covington-Muhammad headliner and quick Chimaev return against Burns",
       dek="Real American Freestyle confirmed the full lineup for the Fox Nation card in Miami, topped by Colby Covington vs Belal Muhammad in a cruiserweight crossover bout. Khamzat Chimaev meets Gilbert Burns two weeks after beating Tyron Woodley at RAF Moscow, with Kennedy Blades vs Diana Avsaragova and Austin DeSanto vs Arsen Harutyunyan also set.",
       src="Sherdog", url="https://www.sherdog.com/news/news/RAF-13-full-card-confirmed-with-CovingtonMuhammad-ChimaevBurns-202730"),
  dict(date="2026-09-11", promo="industry", cat="media", official=False, who="Brandon Thurston",
       hl="TNA Impact on AMC drew 184,000 viewers for September 3 episode",
       dek="Per Wrestlenomics figures cited by Pro Wrestling Dot Net, the show did a 0.03 rating in 18-49 against college football competition. The counts exclude AMC+ and TNA+ streaming viewership.",
       src="Pro Wrestling Dot Net", url="https://prowrestling.net/site/2026/09/11/tna-impact-rating-9-3-how-did-the-final-show-fare-heading-into-labor-day-weekend/"),
  dict(date="2026-09-13", promo="industry", cat="media", official=False, who="Brandon Thurston",
       hl="NXT Heatwave fallout episode jumps to 768,000 viewers and 0.17 demo rating",
       dek="The September 1 NXT on The CW rose sharply from the prior week's 632,000 viewers and 0.09 demo, and topped the comparable 2025 episode's 654,000. ESPN Unlimited streaming figures are excluded from the counts.",
       src="Pro Wrestling Dot Net", url="https://prowrestling.net/site/2026/09/13/nxt-tv-rating-9-1-did-the-numbers-improve-for-the-nxt-heatwave-fallout-show/"),
  # =============== end week of September 7 - September 13, 2026 ===============

  # ============ WEEK OF AUGUST 31 - SEPTEMBER 6, 2026 - SEPT 2-6 FILL ============
  # Backfilled Sep 20 from the Sep 2-6 gap: Dynamite, iMPACT, SmackDown,
  # Collision, RAF Moscow, SNME, NJPW weekend. See build/fill_week_0831.py.

  # ---- WWE: SmackDown Sep 4 (Cleveland) + Sunday Night's Main Event Sep 6 (Atlanta) ----
  dict(date="2026-09-06", promo="wwe", cat="event", official=True, who="Randy Orton", lead=True, mono="SNME",
       hl="Randy Orton steals main event win over Cody Rhodes in Atlanta",
       dek="Orton low blows both Rhodes and the referee, then lands the RKO for the pin at State Farm Arena. Quavo opens the show with a live performance.",
       src="WWE.com", url="https://www.wwe.com/shows/snme/2026-09-06/results"),
  dict(date="2026-09-06", promo="wwe", cat="title", official=True, who="Trick Williams",
       hl="Trick Williams beats Baron Corbin to capture the United States Championship",
       dek="Lil Yachty survives a five minute Survive and Advance match to trigger the instant title shot. Williams counters End of Days and hits the Trick Shot to win.",
       src="WWE.com", url="https://www.wwe.com/shows/snme/2026-09-06/results"),
  dict(date="2026-09-06", promo="wwe", cat="return", official=True, who="Bronson Reed",
       hl="Bronson Reed returns and mauls Oba Femi to force disqualification finish",
       dek="Femi wins by DQ over Bron Breakker when Reed hits the ring with a steel chair. Reed follows with multiple Tsunamis as Breakker adds Super Spears.",
       src="WWE.com", url="https://www.wwe.com/shows/snme/2026-09-06/results"),
  dict(date="2026-09-04", promo="wwe", cat="event", official=True, who="CM Punk",
       hl="CM Punk survives Gargano and Zayn chaos to retain Undisputed WWE Title",
       dek="Punk pins Johnny Gargano with the GTS amid interference from Zayn, Owens, Gunther, Balor and LeRae. He then challenges Sami Zayn for Mexico City.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-09-04"),
  dict(date="2026-09-04", promo="wwe", cat="roster", official=True, who="Chelsea Green",
       hl="Chelsea Green cleared to return but must wear protective facemask",
       dek="Green is cleared from the orbital fracture suffered August 7, with a mandatory mask per WWE medical. She defends the Women's Title against Nia Jax next week in Mexico City.",
       src="WrestleZone", url="https://www.wrestlezone.com/news/1661119-chelsea-green-cleared-wwe-smackdown-catch-mask"),
  dict(date="2026-09-04", promo="wwe", cat="roster", official=True, who="Kyoki",
       hl="Kyoki makes SmackDown debut teaming with Shinsuke Nakamura as Bakusai",
       dek="The new duo beats The Miz and Kit Wilson in their first outing. Kyoki finishes with a Reverse Stunner.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-09-04"),

  # ---- AEW: Dynamite Sep 2 (Allen, TX) + Collision Sep 5 ----
  dict(date="2026-09-02", promo="aew", cat="title", official=True, who="Swerve Strickland",
       hl="Swerve Strickland and The New Level retain AEW World Trios Titles over The Rascalz",
       dek="Swerve hits the House Call on Dezmond Xavier and Kofi scores the pin at about 13 minutes on Dynamite in Allen, Texas.",
       src="Fightful", url="https://www.fightful.com/wrestling/aew-dynamite-results-9-2-2026-swerve-strickland-new-level-vs-rascalz-will-ospreay-mercedes-mone-more/"),
  dict(date="2026-09-02", promo="aew", cat="event", official=True, who="Mercedes Mone",
       hl="Thekla interrupts Mercedes Mone championship celebration and calls for a title match",
       dek="Mone, showing facial damage from the Willow Nightingale match, touts a fourth major title across different companies before Thekla crashes the party from the upper deck with a challenge.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/09/02/aew-dynamite-report-september-2-2026-allen-tex-at-credit-union-of-texas-event-center-aired-on-tbs-hbo-max-report-by-wade-keller-pwtorch-editor-commentators-excalibur-tony-schiavone/"),
  dict(date="2026-09-02", promo="aew", cat="event", official=True, who="Jon Moxley",
       hl="Jon Moxley challenges Will Ospreay for the AEW World Championship at All Out",
       dek="Moxley chokes out AR Fox with the Death Rider submission in a Continental eliminator, and the Ospreay title match is set for All Out on September 26 in Chicago.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/09/02/aew-dynamite-report-september-2-2026-allen-tex-at-credit-union-of-texas-event-center-aired-on-tbs-hbo-max-report-by-wade-keller-pwtorch-editor-commentators-excalibur-tony-schiavone/"),
  dict(date="2026-09-05", promo="aew", cat="title", official=True, who="Andrade El Idolo",
       hl="Andrade El Idolo turns back Gabe Kidd to keep the AEW National Championship",
       dek="Andrade retains on Collision and vows weekly defenses; Wrestling Inc calls the finisher the Destination Madrid while PWMania calls it The Message.",
       src="Wrestling Inc", url="https://www.wrestlinginc.com/2251732/aew-collision-september-5-2026-results/"),
  dict(date="2026-09-05", promo="aew", cat="roster", official=True, who="Motor City Machine Guns",
       hl="Motor City Machine Guns take their first AEW in-ring win on Saturday Collision",
       dek="Chris Sabin and Alex Shelley finish with Skull and Bones in their AEW in-ring debut; Wrestling Inc lists the opponents as Jay Lethal's Lethal Swirl while PWMania lists The Swirl's Blake Christian and Lee Johnson.",
       src="Wrestling Inc", url="https://www.wrestlinginc.com/2251732/aew-collision-september-5-2026-results/"),
  dict(date="2026-09-05", promo="aew", cat="media", official=False, who="AEW",
       hl="AEW Dynamite viewership ticks up to 796,000 viewers for post All In episode",
       dek="The September 2 Dynamite drew 796,000 viewers with a 0.21 in P18-49, up from 792,000 and 0.18 the prior week per Ringside News.",
       src="Ringside News", url="https://www.ringsidenews.com/aew-dynamite-viewership-sees-slight-increase-september-2-2026"),

  # ---- RAF Moscow Sep 5 / TNA Sep 3 / NJPW weekend / industry ----
  dict(date="2026-09-05", promo="raf", cat="event", official=True, who="Khamzat Chimaev",
       hl="Chimaev pins Woodley in 94 seconds as RAF Moscow card goes ahead",
       dek="Khamzat Chimaev scored push-out points, reversed a single-leg and pinned Tyron Woodley at 1:34 of the catchweight main event. Abdulrashid Sadulaev edged Zac Braunagel 8-6 and Jordan Burroughs teched Magomed Kurbanaliev 10-0.",
       src="MiddleEasy", url="https://middleeasy.com/mma-news/khamzat-chimaev-tyron-woodley-raf-moscow-pin-highlights"),
  dict(date="2026-09-05", promo="raf", cat="title", official=True, who="Kyle Snyder",
       hl="Snyder, Dake and Blades all retain RAF titles on Moscow card",
       dek="Kyle Snyder beat Akhmed Tazhudinov 11-5 to keep the light heavyweight title, his second win over Tazhudinov. Kyle Dake edged Mahamedkhabib Kadzimahamedau 7-6 in his cruiserweight defense and Kennedy Blades teched Vusala Parfianovich 10-0.",
       src="USA Wrestling", url="https://www.themat.com/news/2026/september/05/snyder-dake-blades-defend-titles-americans-roll-at-raf-moscow"),
  dict(date="2026-09-03", promo="raf", cat="media", official=True, who="Real American Freestyle",
       hl="RAF Moscow swaps venues two days out as Fox Nation declines to stream card",
       dek="RAF moved the card from VTB Arena, run by a subsidiary of sanctioned VTB Bank, to Arena Mytishchi to sidestep U.S. sanctions exposure. Fox Nation had declined to stream the event, and it ultimately aired with no U.S. streaming option.",
       src="Yahoo Sports", url="https://sports.yahoo.com/articles/sanctions-avoided-raf-moscow-abruptly-210000851.html"),
  dict(date="2026-09-03", promo="tna", cat="event", official=True, who="Matt Hardy",
       hl="Agent Zero wrecks Miguel vs Hotch as Hardy and Nemeth war escalates on iMPACT",
       dek="Trey Miguel vs Jason Hotch ended in a 19-minute no contest when Agent Zero attacked both men in Brampton. Matt Hardy blamed the Nemeths for the attack on Jeff, and Santino booked Hardy vs Nic Nemeth in a no-DQ match. Dutch beat BDE and KC Navarro won an X Division scramble qualifier.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/09/03/tna-impact-tv-results-9-3-hotch-vs-miguel-hartwell-hudson-vs-brookside-serrano-bde-vs-dutch/"),
  dict(date="2026-09-05", promo="njpw", cat="event", official=True, who="Shingo Takagi",
       hl="Takagi and Cobb topple United Empire as Road to Destruction opens in Tochigi",
       dek="Shingo Takagi and Jeff Cobb beat United Empire with the Burning Dragon at Light Cube Utsunomiya before 903 fans. NEVER Openweight champion Aaron Wolf tapped Hartley Jackson in six-man action and Chaos took the eight-man main event.",
       src="PWMania", url="https://www.pwmania.com/njpw-road-to-destruction-night-1-results-september-5-2026"),
  dict(date="2026-09-06", promo="njpw", cat="event", official=True, who="Yuji Nagata",
       hl="Nagata and Most Violent Players win Blue Justice XIX main event in Togane",
       dek="Yuji Nagata teamed with Togi Makabe and Toru Yano to beat Unbound Company in 15:24 before 1,258 fans at Togane Arena. Jeff Cobb pinned Zane Jay with the Tour of the Islands and House of Torture took the six-man tag.",
       src="PWMania", url="https://www.pwmania.com/njpw-blue-justice-xix-results-september-6-2026"),
  dict(date="2026-09-06", promo="industry", cat="passing", official=True, who="Andy Williams",
       hl="Andy The Butcher Williams, Every Time I Die guitarist and AEW alum, dies at 48",
       dek="Williams suffered a medical emergency and collapsed after a Butcher and Blade tag match with Braxton Sutter at an Enjoy Wrestling event in Millvale, Pennsylvania; he received CPR at ringside and the show was canceled. He co-founded Every Time I Die in 1998 and debuted in AEW in 2019.",
       src="Wrestling Inc", url="https://www.wrestlinginc.com/2251808/butcher-andy-williams-dead-aew-star-age-48/"),
  # ============ end Sept 2-6 fill, week of August 31 - September 6, 2026 ============

  # ================= WEEK OF AUGUST 31 - SEPTEMBER 6, 2026 (in progress) =================
  # Opened Sep 1 with Raw and the All In / Heatwave fallout. Fills nightly.

  # ---- WWE: Raw Aug 31, Rocket Arena, Cleveland ----
  dict(date="2026-08-31", promo="wwe", cat="event", official=True, who="Penta", home=True, htags="matches titles",
       hl="Penta defeats Rey Fenix to win the World Title number one contender tournament",
       dek="Penta pinned his brother with a Mexican Destroyer and challenges Roman Reigns for the World Heavyweight Championship September 14 in Mexico City.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/08/31/wwe-raw-results-8-31-kellers-report-on-roman-reigns-appearance-raquel-vs-sol-ruca-for-ic-title-penta-vs-rey-fenix-in-tournament-final-chad-gable-speaks/"),
  dict(date="2026-08-31", promo="wwe", cat="event", official=True, who="Roman Reigns", home=True, htags="rivalries",
       hl="Roman Reigns flattens LA Knight as Royce Keys and OTM ambush The Usos",
       dek="Keys, Bronco Nima and Lucien Price destroyed The Usos in the parking garage and Solo Sikoa was attacked. Reigns closed the night by Superman Punching Knight.",
       src="WrestleView", url="https://www.wrestleview.com/wwe-raw-results/391685-wwe-raw-results-august-31-2026-cleveland/"),
  dict(date="2026-08-31", promo="wwe", cat="title", official=True, who="Raquel Rodriguez",
       hl="Raquel Rodriguez retains the Womens Intercontinental Title against Sol Ruca",
       dek="Rodriguez hit the Tejana Bomb for the pin after Lyra Valkyria's interference cost Ruca the match in Cleveland.",
       src="WrestleView", url="https://www.wrestleview.com/wwe-raw-results/391685-wwe-raw-results-august-31-2026-cleveland/"),
  dict(date="2026-08-31", promo="wwe", cat="event", official=True, who="Dragon Lee",
       hl="Dragon Lee beats Ethan Page to earn an Intercontinental Title shot at Chad Gable",
       dek="Lee hit Operation Dragon to win and challenges Gable on the September 14 Raw in Mexico City.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/08/31/wwe-raw-results-8-31-kellers-report-on-roman-reigns-appearance-raquel-vs-sol-ruca-for-ic-title-penta-vs-rey-fenix-in-tournament-final-chad-gable-speaks/"),
  dict(date="2026-08-31", promo="wwe", cat="media", official=True, who="Quavo",
       hl="Quavo confirmed on Raw to open Sunday Nights Main Event in hometown Atlanta",
       dek="The rapper debuts an unreleased song September 6 at the special headlined by Oba Femi vs Bron Breakker and Cody Rhodes vs Randy Orton.",
       src="Wrestling Inc.", url="https://www.wrestlinginc.com/2248266/quavo-wwe-sunday-nights-main-event-perform-live/"),
  dict(date="2026-09-01", promo="wwe", cat="media", official=False, who="John Cena",
       hl="John Cena says WWE has finalized plans for the John Cena Classic",
       dek="Speaking at FanExpo Canada, Cena said all details of the NXT versus main roster tournament announced at Backlash are set but staying secret for now.",
       src="Blog of Doom", url="https://www.blogofdoom.com/2026/09/01/morning-daily-news-update-september-1-2026-john-cena-says-wwe-has-finalised-plans-for-john-cena-classic/"),

  # ---- AEW: All In fallout ----
  dict(date="2026-09-01", promo="aew", cat="signing", official=False, who="New Level", home=True, htags="roster",
       hl="New Level say their AEW contracts became official less than 24 hours before All In",
       dek="Kofi and Austin Creed told the Ariel Helwani Show their deals only solidified less than a day before the Wembley debut where they won the World Trios Titles.",
       src="Fightful", url="https://www.fightful.com/wrestling-news/new-level-say-they-officially-signed-their-aew-contracts-less-than-24-hours-before-aew-all-in"),
  dict(date="2026-08-31", promo="aew", cat="return", official=False, who="Britt Baker",
       hl="Britt Baker's All In return reportedly came together hours before the show",
       dek="Fightful Select reports Baker did not travel with the roster and arrived in London Sunday morning, after multiple return overtures during her nearly two-year absence.",
       src="Fightful", url="https://www.fightful.com/wrestling-news/details-about-britt-bakers-return-to-aew"),
  dict(date="2026-08-31", promo="aew", cat="roster", official=False, who="Mercedes Mone",
       hl="Mercedes Mone reveals a broken nose suffered early in her All In title win",
       dek="The new AEW Womens World Champion says she broke her nose early in the Willow Nightingale match and needed stitches, posting a bloodied photo captioned Heavy is the crown.",
       src="WrestleTalk", url="https://wrestletalk.com/news/aew-mercedes-mone-all-in-comment/"),
  dict(date="2026-08-31", promo="aew", cat="media", official=True, who="Will Ospreay",
       hl="Ospreay keeps one of Kenny Omega's side plates on the AEW World Title",
       dek="AEW footage of the new champion's side plate installation shows Ospreay retaining one of Omega's plates as a tribute to his predecessor.",
       src="411Mania", url="https://411mania.com/wrestling/will-ospreay-decides-to-retain-one-of-kenny-omegas-side-plates-on-aew-world-title-all-in-2026-triumph/"),

  # ---- NXT / TNA / RAF / industry ----
  dict(date="2026-09-01", promo="nxt", cat="event", official=True, who="Kelani Jordan", home=True, htags="matches",
       hl="NXT runs its Heatwave fallout show with new champion Kelani Jordan set to appear",
       dek="The live Performance Center episode features Nikkita Lyons vs Thea Hail and fallout from Heatwave's five title changes.",
       src="Pro Wrestling Dot Net", url="https://prowrestling.net/site/2026/09/01/nxt-tv-preview-tonights-nxt-heatwave-fallout-show/"),
  dict(date="2026-09-01", promo="tna", cat="event", official=True, who="Nic Nemeth",
       hl="TNA announces back to back September shows at San Antonio's Boeing Center",
       dek="Thursday Night iMPACT airs live from San Antonio September 24 and 25, with the Hardys, Nic Nemeth, Mustafa Ali and Leon Slater advertised.",
       src="TNA Wrestling", url="https://tnawrestling.com/news/tna-wrestling-returns-to-san-antonio-texas-backtoback-nights-of-actionpacked-pro-wrestling"),
  dict(date="2026-09-01", promo="raf", cat="event", official=False, who="Khamzat Chimaev", home=True, htags="rivalries",
       hl="Chimaev calls out four UFC middleweights days before the RAF Moscow match with Woodley",
       dek="Posting I'm ready, the Moscow headliner named Strickland, Du Plessis, Imavov and Borralho on X, and Borralho answered. Chimaev wrestles Tyron Woodley September 5.",
       src="Sherdog", url="https://www.sherdog.com/news/news/Khamzat-Chimaev-names-4-UFC-targets-Caio-Borralho-answers-the-call-202602"),
  dict(date="2026-09-01", promo="industry", cat="business", official=False, who="Tony Khan",
       hl="Brent Council data shows 41,102 turnstile attendance for AEW All In at Wembley",
       dek="Local government figures show 46,987 distributed tickets against Tony Khan's claim of close to 50,000. The count trails All In London 2023's 72,265 and 2024's 46,476 but tops All In Texas 2025's 21,973.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/09/01/aew-all-in-2026-records-41102-turnstile-count-attendance-according-to-local-government-in-london/"),
  dict(date="2026-09-01", promo="industry", cat="media", official=False, who="WWE",
       hl="Raw's August 24 Netflix episode draws 2.5 million global views, seventh on the weekly chart",
       dek="The show slipped from the prior week's 2.7 million views and sixth place finish on Netflix's most viewed weekly shows list.",
       src="Pro Wrestling Dot Net", url="https://prowrestling.net/site/2026/09/01/wwe-raw-on-netflix-viewership-how-did-the-show-featuring-the-usos-vs-la-knight-and-solo-sikoa-perform/"),
  dict(date="2026-09-01", promo="industry", cat="retirement", official=False, who="Carmella",
       hl="Carmella confirms she is retired from pro wrestling on her own podcast",
       dek="Leah Van Dale said I can't wrestle anymore, I'm retired. She has not wrestled since 2023 after the birth of her first child and drop foot complications.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/09/01/carmella-confirms-pro-wrestling-retirement/"),
  # =============== end week of August 31 - September 6, 2026 ===============

  # ================= WEEK OF AUGUST 24-30, 2026 =================
  # Two premium live events in one week: AEW All In: London (Wembley, Aug 30,
  # seven title changes) and WWE NXT Heatwave (Edinburg TX, Aug 30, five).

  # ---- AEW: All In: London, Wembley Stadium, Aug 30 ----
  dict(date="2026-08-30", promo="aew", cat="title", official=True, who="Will Ospreay",
       lead=True, mono="All In: London", home=True, htags="titles matches",
       hl="Will Ospreay beats Kenny Omega at Wembley Stadium for the AEW World Championship",
       dek="Ospreay ended a bloody main event with the Hidden Blade to win his first AEW World Title in front of his home country.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-all-in-london-results-august-30-2026"),
  dict(date="2026-08-30", promo="aew", cat="title", official=True, who="Mercedes Mone",
       home=True, htags="titles matches",
       hl="Mercedes Mone submits Willow Nightingale for the AEW Women's World Championship",
       dek="Mone worked the hand she injured in a backstage attack on Dynamite, then won the title for the first time with the Statement Maker.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-all-in-london-results-august-30-2026"),
  dict(date="2026-08-30", promo="aew", cat="signing", official=True, who="The New Level",
       hl="Kofi and Austin Creed debut in AEW as The New Level and win the World Trios Titles",
       dek="The former New Day members joined Swerve Strickland to win the 21-wrestler Trios Roulette Royale on the Buy In. Tony Khan confirmed both are signed.",
       src="Wrestling Inc.", url="https://www.wrestlinginc.com/2247106/aew-all-in-london-2026-austin-creed-kofi-swerve-strickland-new-level-debut-win-gold/"),
  dict(date="2026-08-30", promo="aew", cat="title", official=True, who="Darby Allin",
       hl="Darby Allin takes the TNT Championship from Kevin Knight in a Falls Count Anywhere match",
       dek="Allin won his third TNT Title with a Coffin Drop off the Wembley stage. Sting appeared with a bat to even the odds against the Don Callis Family.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-all-in-london-results-august-30-2026"),
  dict(date="2026-08-30", promo="aew", cat="title", official=True, who="Kazuchika Okada",
       hl="Kazuchika Okada regains the AEW International Championship in a Wembley three-way",
       dek="Okada hit the Rainmaker on champion Kyle Fletcher in a match that also included Konosuke Takeshita.",
       src="Fightful", url="https://www.fightful.com/wrestling/aew-all-in-results-8-30-2026-kenny-omega-vs-will-ospreay-willow-nightingale-vs-mercedes-mone-more/"),
  dict(date="2026-08-30", promo="aew", cat="title", official=True, who="Persephone",
       hl="Persephone beats Maya World for the TBS Championship as Britt Baker returns",
       dek="Persephone won the title with a crucifix powerbomb on the Buy In. The masked attacker who cost World the match unmasked as Dr. Britt Baker.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-all-in-london-results-august-30-2026"),
  dict(date="2026-08-30", promo="aew", cat="title", official=True, who="The Brawling Birds",
       hl="Jamie Hayter and Alex Windsor win the AEW Women's World Tag Team Titles at Wembley",
       dek="The Brawling Birds hit 2 Birds, 1 Stone on Lena Kross to take the belts from Divine Dominion in front of a home crowd.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-all-in-london-results-august-30-2026"),
  dict(date="2026-08-30", promo="aew", cat="title", official=True, who="Jon Moxley",
       hl="Jon Moxley submits Nigel McGuinness in the Continental Challenge Cup final",
       dek="Moxley kept the AEW Continental Championship, capping a tournament run that went through Claudio Castagnoli in the Glasgow semifinal.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-all-in-london-results-august-30-2026"),
  dict(date="2026-08-30", promo="aew", cat="event", official=True, who="Andrade El Idolo",
       hl="Andrade El Idolo wins the All In Casino Gauntlet and a guaranteed world title shot",
       dek="Andrade pinned Nick Wayne to win the ten-entrant gauntlet, which also featured MJF and a returning Chris Jericho.",
       src="PWMania", url="https://www.pwmania.com/aew-all-in-london-results-august-30-2026"),
  dict(date="2026-08-27", promo="aew", cat="business", official=True, who="Tony Khan",
       hl="Tony Khan says All In: London is approaching a six million dollar gate",
       dek="On the pre-show media call Khan said the Wembley card would run at most four hours and confirmed the Trios Roulette Royale for the Buy In.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/08/27/aew-all-in-london-2026-media-call-with-tony-khan-6-million-gate-four-hour-show-trios-title-match-on-buy-in/"),

  # ---- WWE NXT: Heatwave, Bert Ogden Arena, Edinburg TX, Aug 30 ----
  dict(date="2026-08-30", promo="nxt", cat="title", official=True, who="Grayson Waller",
       lead=True, mono="NXT Heatwave", home=True, htags="titles matches",
       hl="Grayson Waller wins the NXT Championship in a Heatwave Fatal 4-Way",
       dek="Waller stole the pin late over Tony D'Angelo, Zilla Fatu and Cruz Montana at the show co-branded with AAA as Ola de Calor.",
       src="WWE.com", url="https://www.wwe.com/nxt-heatwave-2026"),
  dict(date="2026-08-30", promo="nxt", cat="title", official=True, who="Kelani Jordan",
       hl="Kelani Jordan defeats Kendal Grey for the NXT Women's Championship",
       dek="Jordan worked over Grey's arm throughout and finished with a split-legged moonsault. It is her first NXT Women's Title reign.",
       src="Slam Wrestling", url="https://slamwrestling.net/news/wwe-nxt-heatwave-2026-results/"),
  dict(date="2026-08-30", promo="nxt", cat="title", official=True, who="Zaria",
       hl="Zaria unifies the NXT Women's North American and Women's Speed Championships",
       dek="Zaria beat Wren Sinclair and Kali Armstrong in the Heatwave opener with a spear and an F5. The two titles are now one championship.",
       src="Wrestling Inc.", url="https://www.wrestlinginc.com/2246913/wwe-nxt-heatwave-2026-several-championships-up-for-grabs-submission-match/"),
  dict(date="2026-08-30", promo="nxt", cat="title", official=True, who="Jackson Drake",
       hl="Jackson Drake defeats Myles Borne for the NXT North American Championship",
       dek="Vanity Project interference proved decisive. Borne afterward turned on partner Tavion Heights, having already lost the tag titles earlier in the night.",
       src="Slam Wrestling", url="https://slamwrestling.net/news/wwe-nxt-heatwave-2026-results/"),
  dict(date="2026-08-25", promo="nxt", cat="event", official=True, who="Tony D'Angelo",
       hl="The Heatwave Summit collapses into a brawl on the NXT go-home show",
       dek="The contract signing for the NXT and Women's Title matches broke down, leaving champions Tony D'Angelo and Kendal Grey laid out five days out.",
       src="WWE.com", url="https://www.wwe.com/shows/wwenxt/2026-08-25"),

  # ---- WWE: Raw Aug 24 and SmackDown Aug 28, both from Ottawa ----
  dict(date="2026-08-28", promo="wwe", cat="event", official=True, who="Sami Zayn",
       home=True, htags="rivalries titles",
       hl="Sami Zayn ends the SmackDown No. 1 Contender's Match in a no contest with the title belt",
       dek="Zayn dragged Finn Balor from the ring and attacked both referees, then hit Balor, Gunther, Kevin Owens and CM Punk with the WWE Championship.",
       src="Wrestling Inc.", url="https://www.wrestlinginc.com/2246899/wwe-smackdown-no-1-contenders-match-chaos-sami-zayn-cm-punk/"),
  dict(date="2026-08-28", promo="wwe", cat="title", official=True, who="Jacy Jayne",
       hl="Jacy Jayne retains the Women's United States Championship against Paige",
       dek="Fallon Henley and Lainey Reid distracted Paige from the apron and Jayne rolled her up. Nikki Bella attacked Paige after the match.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-08-28"),
  dict(date="2026-08-26", promo="wwe", cat="roster", official=False, who="AJ Lee",
       hl="AJ Lee is expected to wrestle again for WWE despite her absence since WrestleMania 42",
       dek="Fightful Select reported Lee has not had her final WWE match. She has not been in a storyline since losing the Women's Intercontinental Title to Becky Lynch.",
       src="Slam Wrestling", url="https://slamwrestling.net/news/backstage-update-emerges-on-aj-lees-wwe-future-wrestling-news-rumours-august-26-2026/"),
  dict(date="2026-08-24", promo="wwe", cat="event", official=True, who="Royce Keys",
       hl="Royce Keys returns with OTM and lays out The Usos, LA Knight and Solo Sikoa",
       dek="The Ottawa main event was thrown out as a no contest when Keys arrived with Bronco Nima and Lucien Price and put all four men down.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-08-24"),
  dict(date="2026-08-24", promo="wwe", cat="event", official=True, who="Stephanie Vaquer",
       hl="Stephanie Vaquer beats Roxanne Perez in her first match since WrestleMania 42",
       dek="Becky Lynch cut off Liv Morgan and Raquel Rodriguez before Vaquer finished with a face breaker. She was told backstage she challenges Morgan for the Women's World Title in two weeks.",
       src="Slam Wrestling", url="https://slamwrestling.net/news/wwe-raw-results-august-24-2026/"),
  dict(date="2026-08-24", promo="wwe", cat="event", official=True, who="Penta",
       hl="Penta and Rey Fenix win their semifinals to set a brothers' final for a Reigns title shot",
       dek="Penta beat La Parka with a Mexican Destroyer and Fenix beat Dragon Lee with the Mexican Muscle Buster. The winner challenges Roman Reigns.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-08-24/results"),
  dict(date="2026-08-24", promo="wwe", cat="return", official=True, who="Big Cass",
       hl="Big Cass beats Je'Von Evans in his first WWE match in over eight years",
       dek="Cass shoved Evans off the top rope and finished with a Big Boot. Dominik Mysterio and JD McDonagh attacked Evans after the bell.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-08-24/results"),
  dict(date="2026-08-24", promo="wwe", cat="event", official=True, who="Oba Femi",
       hl="Oba Femi and Bron Breakker brawl at a Raw contract signing for Sunday Night's Main Event",
       dek="Breakker blindsided Femi and Austin Theory joined the fight, but Femi recovered and sent Theory through the signing table.",
       src="Slam Wrestling", url="https://slamwrestling.net/news/wwe-raw-results-august-24-2026/"),

  # ---- TNA: iMPACT Aug 27 ----
  dict(date="2026-08-28", promo="tna", cat="signing", official=True, who="Zoey Serrano",
       home=True, htags="roster",
       hl="TNA confirms the signing of Zoey Serrano after her iMPACT debut",
       dek="The former WWE star known as Zoey Stark debuted on the Aug. 27 iMPACT by attacking Indi Hartwell alongside Xia Brookside.",
       src="Wrestling Inc.", url="https://www.wrestlinginc.com/2247236/tna-zoey-serrano-stark-signing-impact-debut/"),
  dict(date="2026-08-27", promo="tna", cat="title", official=True, who="M by Elegance",
       hl="M by Elegance wins the inaugural TNA Knockouts Television Championship",
       dek="Elegance targeted the arm and finished Jada Stone with a piledriver in the tournament final. She is the first holder of the new title.",
       src="Fightful", url="https://www.fightful.com/wrestling/tna-impact-results-8-27-knockouts-tv-title-tournament-final/"),
  dict(date="2026-08-27", promo="tna", cat="event", official=True, who="Leon Slater",
       hl="Leon Slater invokes Option C for a Bound for Glory world title shot",
       dek="Slater cashed in to challenge Nic Nemeth, saying he intends to become the youngest champion in company history.",
       src="Slam Wrestling", url="https://slamwrestling.net/report/tna-impact-results-08-27-2026-debuts-championships-and-statements-made-oh-my/"),
  dict(date="2026-08-27", promo="tna", cat="title", official=True, who="The Nemeths",
       hl="The Nemeths retain the TNA Tag Team Championship against Leon Slater and Ricky Sosa",
       dek="Nic and Ryan Nemeth turned back the challengers in their first defense since winning the belts at Lockdown.",
       src="Fightful", url="https://www.fightful.com/wrestling/tna-impact-results-8-27-knockouts-tv-title-tournament-final/"),
  dict(date="2026-08-27", promo="tna", cat="event", official=True, who="Jeff Hardy",
       hl="Jeff Hardy leaves iMPACT by ambulance after another mystery attack",
       dek="Hardy was found laid out and loaded onto a stretcher, with Matt Hardy helping him into the ambulance.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/08/27/tna-impact-tv-results-8-27-stone-vs-elegance-elijah-vs-bronson-hartwell-appearance/"),

  # ---- NJPW ----
  dict(date="2026-08-30", promo="njpw", cat="event", official=True, who="Hirooki Goto",
       home=True, htags="matches",
       hl="Hirooki Goto's team beats champion Yota Tsuji's side at NJPW Shimonoseki Impact",
       dek="Goto, YOH and YOSHI-HASHI won before a sold-out 1,817 in Yamaguchi, four weeks before Goto challenges Tsuji for the IWGP Heavyweight Championship at Destruction in Kobe.",
       src="Fightful", url="https://www.fightful.com/wrestling-news/njpw-shimonoseki-impact-results-8-30-26-hirooki-goto-yoh-yoshi-hashi-pick-up-win-in-main-event"),

  # ---- RAF: fallout from RAF 12, build to Moscow ----
  dict(date="2026-08-25", promo="raf", cat="event", official=False, who="Tyron Woodley",
       home=True, htags="matches",
       hl="Tyron Woodley says Khamzat Chimaev may be an easier test than Joaquin Buckley",
       dek="Woodley rallied from 8-1 down to beat Buckley 14-8 at RAF 12 and meets Chimaev in the September 5 Moscow main event. He said the absence of strikes favors his wrestling.",
       src="MiddleEasy", url="https://middleeasy.com/mma-news/tyron-woodley-khamzat-chimaev-raf-moscow-joaquin-buckley/"),
  dict(date="2026-08-25", promo="raf", cat="event", official=False, who="Colby Covington",
       hl="Colby Covington drops interest in a Bo Nickal match after Nickal's RAF 12 loss",
       dek="Nickal lost 3-2 to 2026 NCAA champion Max McEnelly in Cleveland. Covington said the mystique is not there anymore and cited the weight gap.",
       src="Yahoo Sports", url="https://sports.yahoo.com/articles/colby-covington-says-bo-nickal-225019899.html"),
  dict(date="2026-08-24", promo="raf", cat="event", official=False, who="Merab Dvalishvili",
       hl="Merab Dvalishvili addresses his 36-second loss to Henry Cejudo at RAF 12",
       dek="Cejudo pinned Dvalishvili in 36 seconds in Cleveland to take the lightweight title. Dvalishvili said he had been preparing for his UFC title defense rather than a full wrestling camp.",
       src="Heavy", url="https://heavy.com/sports/ufc/merab-dvalishvili-addresses-henry-cejudo-raf-loss/"),

  # ---- industry ----
  dict(date="2026-08-26", promo="industry", cat="media", official=True, who="SEScoops",
       hl="SEScoops retracts its ESPN report and parts ways with the writer",
       dek="The outlet said the subject deserved a direct chance to respond and that the step was not taken to the appropriate standard. Writer BJ Bethel said he stood by the story.",
       src="Awful Announcing", url="https://awfulannouncing.com/wwe/sescoops-retracts-espn-wwe-report.html"),
  dict(date="2026-08-25", promo="industry", cat="media", official=True, who="ESPN",
       hl="ESPN denies a report that it has decided not to renew its WWE deal",
       dek="ESPN said there is no truth to the report that it had decided against renewing the five-year, $1.6 billion premium live event agreement that runs to 2030.",
       src="Wrestling Attitude", url="https://www.wrestlingattitude.com/2026/08/espn-denies-wwe-ple-contract-non-renewal-reports.html"),
  # =============== end week of August 24-30, 2026 ===============

  dict(date="2026-08-22", promo="raf", cat="event", official=True, who="Real American Freestyle", home=True, htags="matches",
       hl="RAF returns to Cleveland for its one year anniversary card",
       dek="Merab Dvalishvili and Henry Cejudo meet again for the crossover lightweight title at Rocket Arena, a year after the league debuted in the same city.",
       src="Real American Freestyle", url="https://www.realamericanfreestyle.com/events/raf12"),
  dict(date="2026-08-17", promo="raf", cat="title", official=True, who="Kyle Snyder",
       hl="Kyle Snyder defends the light heavyweight title against Akhmed Tazhudinov",
       dek="RAF booked the rematch of their RAF 07 meeting for the September 5 card in Moscow.",
       src="Real American Freestyle", url="https://www.realamericanfreestyle.com/post/kyle-snyder-vs-akhmed-tazhudinov-circle-back-run-it-back"),
  dict(date="2026-08-13", promo="raf", cat="event", official=False, who="RAF 12",
       hl="RAF 12 gets a new main event as Covington and Muhammad move to RAF 13",
       dek="Cejudo and Dvalishvili take the Cleveland headline spot. Covington against Belal Muhammad shifts to September 19 in Miami.",
       src="Sherdog", url="https://www.sherdog.com/news/news/RAF-12-gets-new-main-event-with-Henry-CejudoMerab-Dvalishvili-3-202353"),
  dict(date="2026-08-11", promo="raf", cat="business", official=False, who="U.S. Air Force",
       hl="The U.S. Air Force signs on as an official RAF partner",
       dek="Heavyweight champion and Air Force second lieutenant Wyatt Hendrickson announced the multi event deal, which starts at RAF 12.",
       src="On3", url="https://www.on3.com/pro/news/real-american-freestyle-announces-partnership-with-us-air-force-wyatt-hendrickson-reacts/"),
  dict(date="2026-08-11", promo="raf", cat="event", official=False, who="Arman Tsarukyan", home=True, htags="matches",
       hl="Tsarukyan and Dillon Danis booked for the first crossover middleweight title",
       dek="The two meet October 3 at Fontainebleau Las Vegas on RAF 14 with a new belt on the line.",
       src="LowKick MMA", url="https://www.lowkickmma.com/arman-tsarukyan-vs-dillon-danis-raf-14/"),
  dict(date="2026-08-06", promo="raf", cat="title", official=True, who="Evan Wick",
       hl="Evan Wick defends the middleweight title against Jason Nolf at RAF 12",
       dek="A rematch of the RAF 01 bout Wick won 10-8 to become the first middleweight champion.",
       src="Real American Freestyle", url="https://www.realamericanfreestyle.com/post/evan-wick-vs-jason-nolf-long-awaited-middleweight-rematch"),
  dict(date="2026-07-30", promo="raf", cat="event", official=False, who="Khamzat Chimaev",
       hl="Khamzat Chimaev and Tyron Woodley to headline RAF Moscow",
       dek="RAF announced its first card in Russia for September 5, with Chimaev facing the former UFC welterweight champion.",
       src="MMA News", url="https://www.mmanews.com/article/khamzat-chimaev-tyron-woodley-raf-moscow-september-5"),
  dict(date="2026-07-18", promo="raf", cat="retirement", official=False, who="Ben Askren", home=True, htags="roster",
       hl="Ben Askren closes his career at RAF 11 and leaves his boots on the mat",
       dek="Askren lost 6-3 to Belal Muhammad in the co-main event, a year after a double lung transplant and a 40 day coma.",
       src="USA Wrestling", url="https://www.themat.com/news/2026/july/21/ben-askren-concludes-historic-wrestling-career-adeline-gray-and-trent-hidlay-pick-up-victories-at-raf11"),
  dict(date="2026-07-18", promo="raf", cat="title", official=False, who="Colby Covington",
       hl="Colby Covington beats Arman Tsarukyan for the first crossover cruiserweight title",
       dek="Covington won 5-3 in the RAF 11 main event in Milwaukee to become the inaugural champion of the MMA crossover division.",
       src="USA Wrestling", url="https://www.themat.com/news/2026/july/21/ben-askren-concludes-historic-wrestling-career-adeline-gray-and-trent-hidlay-pick-up-victories-at-raf11"),
  dict(date="2026-07-11", promo="raf", cat="title", official=False, who="Kyle Snyder",
       hl="Kyle Snyder pins Abdulrashid Sadulaev at RAF Georgia",
       dek="Snyder kept the light heavyweight title with a fall at 4:25 over the two time Olympic champion in Tbilisi.",
       src="USA Wrestling", url="https://www.themat.com/news/2026/july/11/snyder-pins-sadulaev-dake-and-maroulis-also-retain-belts-at-raf-georgia"),
  # ---------------------------------------------------------------- WEEK OF AUG 17
  dict(date="2026-08-21", promo="wwe", cat="title", official=True, who="CM Punk", lead=True, mono="WWE Title", home=True, htags="titles matches",
       hl="CM Punk keeps the Undisputed WWE Title as Sami Zayn turns on Kevin Owens",
       dek="Zayn hit Owens with the belt in Toronto and Punk finished with a Go to Sleep. Zayn then attacked both men and said the title was stolen from him.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-08-21/results"),
  dict(date="2026-08-21", promo="wwe", cat="title", official=True, who="The MFTs",
       hl="Tama and Talla Tonga hold the tag titles against Damian Priest and R-Truth",
       dek="Haku watched from ringside in Toronto as the champions finished R-Truth with the Red Cross High Low.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-08-21/results"),
  dict(date="2026-08-20", promo="wwe", cat="departure", official=False, who="Ilja Dragunov", home=True, htags="roster",
       hl="Ilja Dragunov leaves WWE as his contract expires",
       dek="WWE moved Dragunov to the alumni section of its site. His last singles match for the company was a loss to Carmelo Hayes on March 30.",
       src="Wrestling Inc.", url="https://www.wrestlinginc.com/2240986/ilja-dragunov-leaving-wwe-contract-expires/"),
  dict(date="2026-08-20", promo="aew", cat="event", official=False, who="AEW All In: London",
       hl="All In London locks in nine matches for Wembley on August 30",
       dek="The announced card includes Kenny Omega against Will Ospreay for the AEW World Title, Willow Nightingale against Mercedes Mone, and the Continental Challenge Cup final.",
       src="Pro Wrestling Dot Net", url="https://prowrestling.net/site/2026/08/20/aew-all-in-london-lineup-the-updated-card-for-the-annual-stadium-event/"),
  dict(date="2026-08-20", promo="tna", cat="event", official=True, who="The Hardys",
       hl="The Hardys, Moose and Elijah take the eight man main event before Lockdown",
       dek="They beat Nic Nemeth, Ryan Nemeth, AJ Francis and Frankie Kazarian on the go home show for TNA Lockdown.",
       src="TNA Wrestling", url="https://tnawrestling.com/news/tna-thursday-night-impact-on-amc-results-august-20-2026"),
  dict(date="2026-08-19", promo="aew", cat="event", official=True, who="Kenny Omega", home=True, htags="matches rivalries",
       hl="Kenny Omega puts Will Ospreay through a table eleven days out from All In",
       dek="Omega closed Dynamite in Baltimore with a One Winged Angel on the floor. The two meet for the AEW World Title at Wembley.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-dynamite-results-august-19-2026"),
  dict(date="2026-08-19", promo="aew", cat="event", official=True, who="Jon Moxley",
       hl="Moxley and Nigel McGuinness reach the Continental Challenge Cup semifinals",
       dek="Moxley submitted Jay White with a rear naked choke and McGuinness beat Hechicero. Maya World kept the TBS Title in a four way.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-dynamite-results-august-19-2026"),
  dict(date="2026-08-19", promo="tna", cat="media", official=True, who="TNA Wrestling",
       hl="TNA and REVOLT strike a content partnership for the fall",
       dek="Exclusive Xplosion matches and material from the 24 year TNA library head to REVOLT and REVOLT SPORTS starting in fall 2026.",
       src="TNA Wrestling", url="https://tnawrestling.com/news/tna-wrestling-and-revolt-announce-partnership-bringing-exclusive-xplosion-matches-and-classic-content-to-revolt"),
  dict(date="2026-08-19", promo="aew", cat="business", official=False, who="AEW All In: London",
       hl="All In London passes 40,000 tickets distributed for Wembley",
       dek="WrestleTix put distribution near 40,036 on August 19, with roughly 4,987 seats left in a 45,023 setup.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/08/19/aew-all-in-london-tickets-distributed-reaches-over-estimated-40000/"),
  dict(date="2026-08-18", promo="nxt", cat="signing", official=True, who="Zilla Fatu", home=True, htags="roster",
       hl="Zilla Fatu signs with NXT and joins the Heatwave title picture",
       dek="Fatu put his name to a contract on NXT. He, Grayson Waller and Cruz Montana are all set to challenge champion Tony D'Angelo at Heatwave.",
       src="WWE.com", url="https://www.wwe.com/shows/wwenxt/2026-08-18"),
  dict(date="2026-08-18", promo="aew", cat="return", official=False, who="Jim Ross",
       hl="Jim Ross aims to call All In after brain surgery",
       dek="Ross had surgery on August 12 to remove fluid from his brain. He said his goal is to work Wembley Stadium at the end of the month.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/08/18/jim-ross-provides-update-following-brain-surgery/"),
  dict(date="2026-08-17", promo="wwe", cat="event", official=True, who="Solo Sikoa", home=True, htags="rivalries roster",
       hl="Solo Sikoa sides with LA Knight and turns on Roman Reigns",
       dek="Jey Uso delivered Sikoa to Reigns on Raw in Buffalo. Sikoa joined LA Knight instead and helped lay out Reigns and The Usos.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-08-17"),
  dict(date="2026-08-17", promo="wwe", cat="title", official=True, who="Chad Gable", home=True, htags="titles",
       hl="Chad Gable keeps the Intercontinental Title in his first defense",
       dek="Gable countered a pin attempt from Rey Mysterio after two 619s to hold the title he won at SummerSlam.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-08-17"),
  dict(date="2026-08-17", promo="wwe", cat="event", official=True, who="Rey Fenix",
       hl="Rey Fenix and Dragon Lee advance in the World Title contender tournament",
       dek="Fenix beat El Fiscal and Dragon Lee beat El Hijo de Dr. Wagner Jr. on Raw as the bracket heads toward Mexico City.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-08-17"),
  dict(date="2026-08-17", promo="tko", cat="business", official=True, who="WWE",
       hl="WWE adds a second Honolulu show for October 17",
       dek="The October 16 night at Blaisdell Arena is nearly sold out. WWE will also hold a talent tryout at the venue.",
       src="WWE Corporate", url="https://corporate.wwe.com/about/news/2026/08-17-2026"),

  # ---------------------------------------------------------------- WEEK OF AUG 10
  dict(date="2026-08-16", promo="njpw", cat="event", official=False, who="Ryohei Oiwa", home=True, htags="matches",
       hl="Ryohei Oiwa wins G1 Climax 36 and calls his shot for October",
       dek="Oiwa submitted Yuya Uemura in the final at Ryogoku Sumo Hall and said he will challenge for the IWGP Heavyweight Title on October 12.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/08/16/njpw-g1-climax-36-final-results-ryohei-oiwa-wins-the-tournament-calls-title-shot-for-october/"),
  dict(date="2026-08-15", promo="njpw", cat="retirement", official=False, who="Hiroyoshi Tenzan",
       hl="Hiroyoshi Tenzan closes a 35 year career against Satoshi Kojima",
       dek="Kojima beat his longtime partner and rival with a lariat at 9:22 at Ryogoku Sumo Hall in Tenzan's retirement match.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/08/15/njpw-g1-climax-36-semifinals-results-yuya-uemura-vs-ryohei-oiwa-final-set-tenzan-retires/"),
  dict(date="2026-08-15", promo="aew", cat="title", official=True, who="Page, Bandido and Brody King",
       hl="Page, Bandido and Brody King survive their first trios defense",
       dek="The champions turned back The Lethal Twist on Collision. The Demand attacked all three after the bell and said the titles belong to them.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-collision-results-august-15-2026"),
  dict(date="2026-08-15", promo="aew", cat="event", official=True, who="Continental Challenge Cup",
       hl="Hechicero, McGuinness and O'Reilly move into the Continental Cup quarterfinals",
       dek="On Collision, Hechicero beat Brian Cage, Nigel McGuinness beat Katsuyori Shibata and Kyle O'Reilly beat Roderick Strong.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-collision-results-august-15-2026"),
  dict(date="2026-08-14", promo="wwe", cat="title", official=True, who="The MFTs", lead=True, mono="Tag Team Titles", home=True, htags="titles",
       hl="The MFTs win the WWE Tag Team Titles in a SmackDown triple threat",
       dek="Tama Tonga and Talla Tonga beat Damian Priest and R-Truth and The War Raiders, finishing R-Truth with The Brother's Keeper as Haku looked on.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-08-14"),
  dict(date="2026-08-14", promo="wwe", cat="title", official=True, who="Jacy Jayne", home=True, htags="titles",
       hl="Jacy Jayne takes the Women's United States Title from Tiffany Stratton",
       dek="Jayne caught Stratton with the Rolling Encore as she came back into the ring and pinned her for the title.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-08-14"),
  dict(date="2026-08-14", promo="wwe", cat="title", official=True, who="Baron Corbin",
       hl="Baron Corbin keeps the United States Title in Carmelo Hayes's hometown",
       dek="Corbin hit End of Days for the win. Trick Williams and Lil Yachty attacked him afterward.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-08-14"),
  dict(date="2026-08-13", promo="tna", cat="title", official=True, who="Nic Nemeth",
       hl="Nic Nemeth keeps the TNA World Title against Jeff Hardy",
       dek="Nemeth finished Hardy with the Danger Zone in the iMPACT main event from Philadelphia.",
       src="TNA Wrestling", url="https://tnawrestling.com/news/tna-thursday-night-impact-on-amc-results-august-13-2026"),
  dict(date="2026-08-12", promo="aew", cat="title", official=True, who="Kevin Knight",
       hl="Kevin Knight keeps the TNT Title after Don Callis attacks Chris Jericho",
       dek="Callis hit Jericho with a screwdriver behind the referee's back in Las Vegas and Knight followed with the Crash Landing.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-dynamite-results-august-12-2026"),
  dict(date="2026-08-12", promo="aew", cat="return", official=True, who="Swerve Strickland", home=True, htags="roster",
       hl="Swerve Strickland returns on Dynamite and confronts the trios champions",
       dek="Strickland came back to face Hangman Adam Page and Brodido, adding a new problem for the champions and The Demand.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-dynamite-results-august-12-2026"),
  dict(date="2026-08-12", promo="aew", cat="event", official=True, who="Kyle Fletcher",
       hl="Fletcher, Takeshita and Okada set for a three way at All In",
       dek="AEW announced the International Title match for Wembley, with champion Kyle Fletcher facing Konosuke Takeshita and Kazuchika Okada.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-dynamite-results-august-12-2026"),
  dict(date="2026-08-11", promo="nxt", cat="return", official=False, who="Zilla Fatu", home=True, htags="roster",
       hl="Zilla Fatu debuts on NXT and lays out Cruz Montana and Grayson Waller",
       dek="His interference ended the number one contender match in a disqualification. He then told the champion there is a new sheriff in town.",
       src="Slam Wrestling", url="https://slamwrestling.net/news/zilla-fatu-makes-wwe-nxt-debut/"),
  dict(date="2026-08-10", promo="wwe", cat="event", official=True, who="Jey Uso", home=True, htags="matches rivalries",
       hl="Jey Uso beats Solo Sikoa and hands him to Roman Reigns",
       dek="Jimmy Uso helped his brother close out the Bloodline match on Raw, making good on the promise to deliver Sikoa.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-08-10"),
  dict(date="2026-08-10", promo="wwe", cat="event", official=True, who="Penta",
       hl="Penta advances in the World Heavyweight Title contender tournament",
       dek="A Mexican Destroyer finished Laredo Kid on Raw and sent Penta through to the semifinals.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-08-10"),

  # ---------------------------------------------------------------- WEEK OF AUG 3
  dict(date="2026-08-09", promo="njpw", cat="event", official=False, who="Konosuke Takeshita",
       hl="Takeshita beats Sanada to keep the A Block lead in G1 Climax 36",
       dek="Takeshita won in 14 minutes 2 seconds on night 14 and knocked Sanada out of the block.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/08/10/njpw-g1-climax-36-results-night-14-8-9-takeshita-vs-sanada-boltin-oleg-vs-hirooki-goto-yuto-ice-vs-takagi-more/"),
  dict(date="2026-08-08", promo="aew", cat="event", official=True, who="Continental Challenge Cup",
       hl="The Continental Challenge Cup opens with Castagnoli, Cassidy and Kingston",
       dek="On Collision from Colorado Springs, Claudio Castagnoli beat Ace Austin, Orange Cassidy beat Matt Sydal and Eddie Kingston beat Jake Doyle.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-collision-results-august-8-2026"),
  dict(date="2026-08-07", promo="wwe", cat="return", official=True, who="Alexa Bliss", home=True, htags="roster",
       hl="Alexa Bliss returns and Tatum Paxley debuts on SmackDown",
       dek="Both women helped Charlotte Flair beat Jade Cargill. Paxley came off the top rope to the floor.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-08-07"),
  dict(date="2026-08-07", promo="wwe", cat="title", official=True, who="Baron Corbin",
       hl="Baron Corbin keeps the United States Title against Trick Williams",
       dek="Corbin used the belt behind the referee's back to pin the former champion on SmackDown.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-08-07"),
  dict(date="2026-08-07", promo="tko", cat="business", official=False, who="WWE and Vince McMahon",
       hl="The merger settlement stalls at 147.5 million dollars",
       dek="Court letters filed August 6 put the WWE share at 105 million dollars and the McMahon share at 42.5 million. The sides disagree over indemnification and insurance releases.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/08/07/narrow-disagreement-between-wwe-and-vince-mcmahon-sides-delay-merger-lawsuit-settlement-that-plaintiffs-say-totals-147-5-million/"),
  dict(date="2026-08-06", promo="tna", cat="title", official=True, who="Xia Brookside",
       hl="Xia Brookside keeps the Knockouts World Title against Wendy Choo",
       dek="Brookside finished Choo with the Darkside in the iMPACT main event from Philadelphia.",
       src="TNA Wrestling", url="https://tnawrestling.com/news/tna-thursday-night-impact-on-amc-results-august-6-2026"),
  dict(date="2026-08-05", promo="aew", cat="title", official=True, who="Page, Bandido and Brody King", lead=True, mono="Grand Slam Mexico", home=True, htags="titles",
       hl="Page, Bandido and Brody King take the trios titles at Grand Slam Mexico",
       dek="The trio beat The Demand at Arena Mexico. Page hit a Buckshot Lariat and Bandido finished Toa Liona with a hesitation 21 Plex.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-grand-slam-mexico-results-august-5-2026"),
  dict(date="2026-08-05", promo="aew", cat="return", official=True, who="MJF", home=True, htags="roster",
       hl="MJF returns at Grand Slam Mexico and attacks Andrade El Idolo",
       dek="MJF struck after Andrade won the number one Casino Gauntlet spot, then said he will wrestle for the number two spot in Las Vegas.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-grand-slam-mexico-results-august-5-2026"),
  dict(date="2026-08-04", promo="industry", cat="passing", official=False, who="Dory Funk Jr.", memoriam=True,
       hl="Dory Funk Jr. dies at 85",
       dek="Funk held the NWA World Heavyweight Title from 1969 to 1973 and entered the WWE Hall of Fame in 2009.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/08/04/former-nwa-champion-dory-funk-jr-dies-at-85/"),
  dict(date="2026-08-04", promo="nxt", cat="title", official=True, who="Myles Borne and Tavion Heights", home=True, htags="titles",
       hl="Myles Borne and Tavion Heights dethrone The Vanity Project for the NXT tag titles",
       dek="Borne and Heights beat Brad Baylor and Ricky Smokes in Orlando. It is the first NXT title for Heights.",
       src="WWE.com", url="https://www.wwe.com/shows/wwenxt/2026-08-04"),
  dict(date="2026-08-04", promo="nxt", cat="title", official=True, who="Kendal Grey",
       hl="Kendal Grey keeps the NXT Women's Title in an Underground match",
       dek="Grey was hurt early and still forced Lola Vice to tap to an armbar.",
       src="WWE.com", url="https://www.wwe.com/shows/wwenxt/2026-08-04"),
  dict(date="2026-08-04", promo="tko", cat="business", official=True, who="TKO Group Holdings",
       hl="Royal Rumble 2027 heads to State Farm Stadium in Arizona",
       dek="The 40th Royal Rumble lands in February 2027, announced with the Arizona Sports and Events Alliance and Legends Global alongside Noche UFC and the PBR World Finals.",
       src="WWE Corporate", url="https://corporate.wwe.com/about/news/2026/08-04-2026"),
  dict(date="2026-08-04", promo="wwe", cat="roster", official=True, who="Bianca Belair and Montez Ford",
       hl="Bianca Belair and Montez Ford announce the birth of their son",
       dek="The couple shared on August 4 that Romeo Leonardo Allen Crawford has been born.",
       src="WWE.com", url="https://www.wwe.com/article/bianca-belair-and-montez-ford-announce-the-birth-of-their-son"),
  dict(date="2026-08-03", promo="tko", cat="business", official=True, who="TKO Group Holdings",
       hl="TKO posts 1.547 billion dollars in second quarter revenue",
       dek="WWE segment revenue rose 12 percent to 620.9 million dollars. TKO raised its full year target to a range of 5.775 to 5.825 billion dollars.",
       src="TKO investor relations", url="https://investor.tkogrp.com/news/news-details/2026/TKO-Reports-Second-Quarter-2026-Results/default.aspx"),
  dict(date="2026-08-03", promo="wwe", cat="return", official=True, who="Becky Lynch", home=True, htags="roster rivalries",
       hl="Becky Lynch and Stephanie Vaquer return to Raw and go after The Judgment Day",
       dek="Both women came back on the Raw after SummerSlam and attacked the group.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-08-03"),
  dict(date="2026-08-03", promo="wwe", cat="return", official=True, who="Big Cass",
       hl="Big Cass returns to Raw and lays out Je'Von Evans",
       dek="Cass ambushed Evans after his win over Ethan Page and said Evans will not be the last one he leaves lying.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-08-03"),
  dict(date="2026-08-02", promo="wwe", cat="event", official=True, who="Roman Reigns", lead=True, mono="SummerSlam", home=True, htags="matches titles",
       hl="Roman Reigns retains and closes out Seth Rollins at SummerSlam",
       dek="The World Heavyweight Championship main event on night two keeps the title on the champion and ends the rivalry that ran all summer.",
       src="ESPN", url="https://www.espn.com/wwe/story/_/id/49465881/wwe-summerslam-2026-night-2-live-results-analysis-roman-reigns-vs-seth-rollins"),
  dict(date="2026-08-02", promo="wwe", cat="title", official=True, who="Chad Gable", home=True, htags="titles",
       hl="Chad Gable dethrones Penta for the Intercontinental Title",
       dek="A heavy favorite makes it count on night two, ending Penta's reign for Gable's first Intercontinental Championship.",
       src="The SmackDown Hotel", url="https://www.thesmackdownhotel.com/events-results/ppv-special/wwe-summerslam-2026"),
  dict(date="2026-08-02", promo="wwe", cat="title", official=True, who="Baron Corbin", home=True, htags="titles",
       hl="Baron Corbin takes the United States Title from Trick Williams",
       dek="Corbin catches Trick Williams on night two to claim the United States Championship.",
       src="The SmackDown Hotel", url="https://www.thesmackdownhotel.com/events-results/ppv-special/wwe-summerslam-2026"),
  dict(date="2026-08-02", promo="wwe", cat="title", official=True, who="Chelsea Green", home=True, htags="titles",
       hl="Chelsea Green wins the interim Women's Title in a five-way ladder match",
       dek="Green beats Charlotte Flair, Jade Cargill, Tiffany Stratton and Lash Legend to pull down the interim Women's Championship.",
       src="The SmackDown Hotel", url="https://www.thesmackdownhotel.com/events-results/ppv-special/wwe-summerslam-2026"),
  dict(date="2026-08-02", promo="wwe", cat="event", official=True, who="Kevin Owens",
       hl="Kevin Owens wins the number-one-contender match, next for CM Punk",
       dek="Owens outlasts Sami Zayn, Finn Balor and Gunther on night two to earn the next Undisputed WWE Title shot.",
       src="The SmackDown Hotel", url="https://www.thesmackdownhotel.com/events-results/ppv-special/wwe-summerslam-2026"),
  dict(date="2026-08-01", promo="wwe", cat="event", official=True, who="Oba Femi", mono="Hell in a Cell", home=True, htags="matches",
       hl="Oba Femi conquers Brock Lesnar inside Hell in a Cell",
       dek="The night-one signature match sees the young powerhouse stand tall over Brock Lesnar and Paul Heyman.",
       src="Forbes", url="https://www.forbes.com/sites/alfredkonuwa/2026/08/02/wwe-summerslam-night-2-results-winners-and-live-updates/"),
  dict(date="2026-08-01", promo="wwe", cat="event", official=True, who="CM Punk",
       hl="CM Punk turns back Cody Rhodes to keep the Undisputed WWE Title",
       dek="The champion retains on night one in a headline clash with Cody Rhodes.",
       src="The SmackDown Hotel", url="https://www.thesmackdownhotel.com/events-results/ppv-special/wwe-summerslam-2026"),
  dict(date="2026-08-01", promo="wwe", cat="event", official=True, who="Liv Morgan",
       hl="Liv Morgan retains the Women's World Title over IYO SKY",
       dek="Morgan keeps the Women's World Championship on the opening night of SummerSlam.",
       src="The SmackDown Hotel", url="https://www.thesmackdownhotel.com/events-results/ppv-special/wwe-summerslam-2026"),
  dict(date="2026-08-01", promo="wwe", cat="return", official=True, who="Randy Orton", home=True, htags="roster",
       hl="Randy Orton returns at SummerSlam",
       dek="The Viper is back, making a surprise night-one return.",
       src="Forbes", url="https://www.forbes.com/sites/alfredkonuwa/2026/08/02/wwe-summerslam-night-2-results-winners-and-live-updates/"),
  dict(date="2026-07-28", promo="nxt", cat="return", official=False, who="Grayson Waller",
       hl="Grayson Waller crashes NXT, calls his shot at Tony D'Angelo",
       dek="A surprise return promo put the whole men's roster on notice and the NXT Championship squarely in his sights.",
       src="Sports Illustrated", url="https://www.si.com/fannation/wrestling/wwe/grayson-waller-drops-pipebomb-promo-on-austin-theory-new-day-others-in-nxt-return"),
  dict(date="2026-07-28", promo="nxt", cat="signing", official=False, who="Cruz Montana",
       hl="Mike Santana lands in NXT under a new name, Cruz Montana",
       dek="The former TNA and AEW standout arrives in WWE developmental with a ring name honoring his late father.",
       src="Fightful", url="https://www.fightful.com/podcasts/cruz-montana-fka-mike-santana-arrives-in-wwe-nxt-7-28-26-full-show-review-highlights/"),
  dict(date="2026-07-27", promo="wwe", cat="title", official=True, who="Raquel Rodriguez",
       hl="Raquel Rodriguez pins Sol Ruca for the Women's Intercontinental Title",
       dek="Her first singles championship in WWE comes on the SummerSlam go-home Raw.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/07/27/wwe-raw-7-27-results-raquel-rodriguez-wins-womens-intercontinental-title-roman-reigns-and-seth-rollins-face-off-on-summerslam-go-home-show/"),
  dict(date="2026-07-27", promo="tko", cat="business", official=True, who="Club WWE",
       hl="WWE opens the doors on Club WWE, a paid membership tier",
       dek="A 99-dollar-a-year program bundling a match-used welcome kit, exclusive merch, early ticket access and a premium library, live July 31.",
       src="WWE.com", url="https://corporate.wwe.com/about/news/2026/07-27-2026"),
  dict(date="2026-07-26", promo="aew", cat="event", official=True, who="Kenny Omega", lead=True, mono="Redemption", home=True, htags="titles rivalries",
       hl="Omega survives Redemption, then lights the fuse on All In",
       dek="Kenny Omega turned back The Jet, Kevin Knight, to keep the AEW World Championship, then turned on the man he now meets in London: Will Ospreay, fresh off walking out on the Death Riders the same night.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-redemption-results-july-26-2026"),
  dict(date="2026-07-26", promo="aew", cat="title", official=True, who="Willow Nightingale",
       hl="Willow Nightingale dethrones Thekla for the Women's World Title",
       dek="A career-defining win at Redemption sets up a marquee defense against Mercedes Mone at All In: London.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-redemption-results-july-26-2026"),
  dict(date="2026-07-26", promo="aew", cat="title", official=True, who="Maya World",
       hl="Maya World takes the TBS Championship from Hikaru Shida",
       dek="One of four title switches on a stacked Redemption card.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-redemption-results-july-26-2026"),
  dict(date="2026-07-26", promo="aew", cat="title", official=True, who="Andrade",
       hl="Andrade beats Mark Davis for the AEW National Championship",
       dek="Gold to show for the split from the Don Callis Family weeks earlier.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-redemption-results-july-26-2026"),
  dict(date="2026-07-25", promo="wwe", cat="roster", official=True, who="Cody Rhodes",
       hl="Cody Rhodes and CM Punk come face to face on SmackDown",
       dek="The SummerSlam card sharpens as champion and challenger share the ring.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-07-24"),
  dict(date="2026-07-25", promo="wwe", cat="roster", official=True, who="Gunther",
       hl="The Ring General leaves Nick Aldis laid out on SmackDown",
       dek="A contract signing turns physical, escalating Gunther's path into SummerSlam.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-07-24"),
  dict(date="2026-07-23", promo="tko", cat="media", official=True, who="WWE Radio",
       hl="WWE Radio goes 24/7 on SiriusXM channel 156",
       dek="Live premium-event coverage plus podcasts from Cody Rhodes, The Undertaker and Stephanie McMahon.",
       src="WWE.com", url="https://corporate.wwe.com/about/news/2026/07-23-2026"),
  dict(date="2026-07-23", promo="wwe", cat="business", official=True, who="Mattel",
       hl="Mattel and WWE bring Lucha Libre AAA to the toy aisle",
       dek="A multi-year global licensing deal puts an AAA figure line on shelves in fall 2027.",
       src="WWE.com", url="https://corporate.wwe.com/about/news/2026/07-23-2026-0"),
  dict(date="2026-07-23", promo="wwe", cat="business", official=False, who="Free agency",
       hl="A wave of released WWE names clears its non-competes",
       dek="Kofi Kingston, Sheamus, Xavier Woods, Zelina Vega and the Motor City Machine Guns are reported free to sign elsewhere.",
       src="Fightful", url="https://www.fightful.com/wrestling/former-wwe-superstars-officially-free-agents-after-90-day-non-competes-expire/"),
  dict(date="2026-07-20", promo="wwe", cat="return", official=False, who="Nikki Bella",
       hl="Nikki Bella says she has cleared testing at the Performance Center",
       dek="The update points toward an in-ring return following April ankle surgery.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/07/20/nikki-bella-provides-update-on-injury-says-she-visited-pc-recently-to-get-cleared/"),
  dict(date="2026-07-18", promo="wwe", cat="title", official=True, who="Fatal Influence",
       hl="Fatal Influence take the Women's Tag Titles at Saturday Night's Main Event",
       dek="Fallon Henley and Lainey Reid beat Paige and Brie Bella, with Jacy Jayne lending a hand.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/07/18/fatal-influence-wins-wwe-womens-tag-team-championships-at-saturday-nights-main-event/"),
  dict(date="2026-07-16", promo="industry", cat="passing", official=False, who="Siva Afi", memoriam=True,
       hl="Siva Superfly Afi, 1949 to 2026",
       dek="The Samoan veteran of the 1980s WWF, later a working stuntman, has died at 77.",
       src="F4WOnline", url="https://www.f4wonline.com/news/wwe/siva-afi-passes-away-at-77/"),
  dict(date="2026-07-14", promo="wwe", cat="media", official=True, who="ReelShort",
       hl="WWE and ReelShort greenlight a vertical microdrama series",
       dek="A live-action series starring Drew McIntyre, Jacob Fatu and Joe Hendry is set for early fall 2026.",
       src="WWE.com", url="https://corporate.wwe.com/about/news/2026/07-14-2026"),
  dict(date="2026-07-13", promo="wwe", cat="event", official=True, who="Roman Reigns",
       hl="Roman Reigns vs Seth Rollins is official for SummerSlam",
       dek="The World Heavyweight Title clash headlines two nights at U.S. Bank Stadium in Minneapolis.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-07-13/roman-reigns-and-seth-rollins"),
  dict(date="2026-07-08", promo="aew", cat="signing", official=True, who="Jack Perry",
       hl="Jack Perry re-signs with AEW",
       dek="A Dynamite: Beach Break vignette confirms one of the Four Pillars is staying put.",
       src="Wrestling Headlines", url="https://wrestlingheadlines.com/aew-news-jack-perry-re-signs-with-aew-new-title-matches-set-big-match-added-to-aew-redemption-more/"),
  dict(date="2026-07-08", promo="tna", cat="signing", official=False, who="Rich Swann",
       hl="Former World Champion Rich Swann re-ups with TNA",
       dek="A new deal keeps the eight-year mainstay in the fold ahead of Lockdown in Chicago.",
       src="Pro Wrestling Dot Net", url="https://prowrestling.net/site/2026/07/08/tna-re-signs-a-former-world-champion/"),
  dict(date="2026-07-08", promo="tko", cat="business", official=True, who="TKO",
       hl="TKO will report second-quarter results on August 3",
       dek="Numbers land after market close, with an investor call to follow at 5 p.m. ET.",
       src="TKO Group Holdings", url="https://investor.tkogrp.com/news/news-details/2026/TKO-to-Announce-Second-Quarter-2026-Results/default.aspx"),
  dict(date="2026-07-06", promo="wwe", cat="title", official=True, who="CM Punk",
       hl="CM Punk returns and takes the Undisputed WWE Title from Sami Zayn",
       dek="A surprise Raw main event flips the top of the card heading toward SummerSlam.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-07-06"),
  dict(date="2026-07-06", promo="wwe", cat="title", official=True, who="The Vision",
       hl="Bron Breakker and Austin Theory capture the World Tag Team Titles",
       dek="The Vision beat The Street Profits on Raw with a timely assist from Maxxine Dupri.",
       src="F4WOnline", url="https://www.f4wonline.com/news/wwe/the-vision-win-world-tag-team-titles-on-wwe-raw-after-surprise-outside-help/"),
  dict(date="2026-07-06", promo="aew", cat="departure", official=False, who="Jake Roberts",
       hl="Jake The Snake Roberts announces his AEW departure",
       dek="The Hall of Famer confirms the end of a run that began alongside Lance Archer in 2020.",
       src="Fightful", url="https://www.fightful.com/wrestling/jake-the-snake-roberts-announces-aew-departure/"),
  dict(date="2026-07-05", promo="wwe", cat="departure", official=False, who="Sheamus",
       hl="Sheamus is reported to be leaving WWE",
       dek="The Celtic Warrior declined a restructured extension, with his profile moved to alumni.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/07/05/report-sheamus-to-exit-wwe-after-rejecting-restructured-contract-extension/"),
  dict(date="2026-07-04", promo="njpw", cat="retirement", official=True, who="Tomoaki Honma",
       hl="Tomoaki Honma sets his retirement after 29 years",
       dek="Citing neck issues, the NJPW veteran plans a farewell match in 2027.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/07/04/njpws-tomoaki-honma-announces-he-is-to-retire/"),
  dict(date="2026-06-28", promo="tna", cat="title", official=False, who="Nic Nemeth",
       hl="Nic Nemeth wins the TNA World Title at Slammiversary",
       dek="The Call Your Shot trophy delivers a second TNA World Championship over Mike Santana in Boston.",
       src="Sports Illustrated", url="https://www.si.com/fannation/wrestling/tna/tna-slammiversary-results-new-world-champions-crowned-former-wwe-star-debuts"),
  dict(date="2026-06-28", promo="tna", cat="title", official=False, who="Xia Brookside",
       hl="Xia Brookside is the new TNA Knockouts World Champion",
       dek="A Slammiversary win over Lei Ying Lee crowns a new Knockouts titleholder.",
       src="Wrestling Headlines", url="https://wrestlingheadlines.com/another-title-change-takes-place-at-tna-slammiversary-2026/"),
  dict(date="2026-06-28", promo="tna", cat="signing", official=False, who="Uhaa Nation",
       hl="Apollo Crews arrives in TNA as Uhaa Nation",
       dek="The former WWE star debuts under his independent name after his contract expired.",
       src="Sports Illustrated", url="https://www.si.com/fannation/wrestling/tna/tna-slammiversary-results-new-world-champions-crowned-former-wwe-star-debuts"),
  dict(date="2026-06-28", promo="aew", cat="event", official=True, who="Owen Hart Cup",
       hl="Ospreay and Mone win the Owen Hart Cups at Forbidden Door",
       dek="Will Ospreay beat Swerve Strickland and Mercedes Mone downed Maya World in the tournament finals.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-x-njpw-forbidden-door-results-june-28-2026"),
  dict(date="2026-06-28", promo="njpw", cat="event", official=True, who="Shota Umino",
       hl="Shota Umino turns back PAC to keep the IWGP Global Title",
       dek="A Forbidden Door defense holds the line for the champion.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-x-njpw-forbidden-door-results-june-28-2026"),
  dict(date="2026-06-28", promo="aew", cat="return", official=True, who="Jay White",
       hl="Jay White makes a surprise Forbidden Door return",
       dek="He aids Adam Copeland and Christian Cage as the tag champions retain.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-x-njpw-forbidden-door-results-june-28-2026"),
  dict(date="2026-06-28", promo="nxt", cat="title", official=True, who="Kendal Grey",
       hl="Kendal Grey wins the NXT Women's Title at Great American Bash",
       dek="A main-event victory over Lola Vice crowns a new NXT Women's Champion.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/06/28/nxt-the-great-american-bash-2026-results-kendal-grey-wins-womens-title-tony-dangelo-zaria-and-myles-borne-retain/"),
  dict(date="2026-06-09", promo="nxt", cat="title", official=True, who="Zaria",
       hl="Zaria captures the NXT Women's North American Title",
       dek="A win over Tatum Paxley puts new gold around her waist.",
       src="F4WOnline", url="https://www.f4wonline.com/news/nxt/zaria-wins-wwe-nxt-womens-north-american-championship/"),
  dict(date="2026-06-08", promo="tko", cat="business", official=False, who="TKO",
       hl="A shareholder suit over the WWE-Endeavor merger settles before trial",
       dek="A Delaware settlement is reached days before a scheduled trial; terms were not disclosed.",
       src="ESPN", url="https://www.espn.com/wwe/story/_/id/49002375/mcmahon-secures-deal-suit-seeking-misconduct-documents"),
]

# ------------------------------------------------------------------ MAPS
CAT = {  # cat -> (label, css-accent-var)
  "title":("Title Change","--c-gold-bright"), "event":("Event","--c-red-bright"),
  "signing":("Signing","--c-win"), "departure":("Departure","--c-red"),
  "return":("Return","--c-focus"), "business":("Business","#b7c1d0"),
  "media":("Media","--c-media"), "roster":("Roster","--c-gold"),
  "retirement":("Retirement","#b7c1d0"), "passing":("In Memoriam","#9aa3ad"),
}
PROMO = {  # promo -> (label, css-color-var for spine/sq, dark-text?)
  "wwe":("WWE","--c-wwe",False), "nxt":("NXT","--c-nxt",True), "aew":("AEW","--c-aew",False),
  "tna":("TNA","--c-tna",False), "njpw":("NJPW","--c-njpw",False),
  "tko":("Business","--c-mens",False), "industry":("Industry","--c-mens",False),
  "raf":("RAF","--c-raf",False),
}
MON = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
MONL = ["January","February","March","April","May","June","July","August","September","October","November","December"]

def d2date(s): return datetime.date.fromisoformat(s)
def monday(dt): return dt - datetime.timedelta(days=dt.weekday())
def wk_id(dt): return monday(dt).isoformat()
def wk_label(mon): return "Week of %s %d, %d" % (MONL[mon.month-1], mon.day, mon.year)
def short(dt): return "%s %d" % (MON[dt.month-1], dt.day)
def wk_range(mon):
    sun = mon + datetime.timedelta(days=6)
    if mon.month == sun.month:
        return "%s %d–%d, %d" % (MON[mon.month-1], mon.day, sun.day, mon.year)
    return "%s %d – %s %d, %d" % (MON[mon.month-1], mon.day, MON[sun.month-1], sun.day, sun.year)

for d in DISPATCHES:
    d["_dt"] = d2date(d["date"]); d["_wk"] = wk_id(d["_dt"])
DISPATCHES.sort(key=lambda d: d["_dt"], reverse=True)

# group into weeks (desc)
WEEKS = []  # list of (mon_date, [items])
_seen = {}
for d in DISPATCHES:
    _seen.setdefault(d["_wk"], []).append(d)
for wid in sorted(_seen.keys(), reverse=True):
    WEEKS.append((d2date(wid), _seen[wid]))

# ------------------------------------------------------------------ CARD RENDER
def card(d, lead=False):
    plabel, pvar, pdark = PROMO[d["promo"]]
    clabel, cvar = CAT[d["cat"]]
    tag = ('<span class="lf-tag lf-tag--official">Official</span>' if d["official"]
           else '<span class="lf-tag">Report</span>')
    memoriam = d.get("memoriam")
    dupe = plabel.lower() == clabel.lower()
    kicker = ('<span class="lf-cat">%s</span>%s%s' %
              (esc(clabel),
               "" if (memoriam or dupe) else '<span class="lf-promo">%s</span>' % esc(plabel),
               tag))
    cls = "lf-item" + (" is-lead" if lead else "") + (" is-memoriam" if memoriam else "")
    pc_val = "var(%s)" % pvar
    kc_val = "var(%s)" % cvar if cvar.startswith("--") else cvar
    inner = ('<div class="lf-kicker">%s</div>'
             '<h3 class="lf-hl">%s</h3><p class="lf-dek">%s</p>'
             '<div class="lf-foot"><span class="lf-when" data-date="%s">%s</span><span class="lf-src">%s</span></div>'
             % (kicker, esc(d["hl"]), esc(d["dek"]), d["date"], short(d["_dt"]), esc(d["src"])))
    # A lead card is a 2-column grid (copy | art); the copy MUST be one wrapper element
    # so the art can be the single second child. Non-lead cards are single-column.
    if lead:
        inner = '<div class="lf-lead__copy">%s</div>' % inner
    return (
      '<article class="%s" data-date="%s" data-promo="%s" data-cat="%s" data-official="%d" '
      'data-headline="%s" style="--pc:%s;--kc:%s">'
      '<a class="lf-item__link" href="%s" target="_blank" rel="noopener">%s</a></article>'
      % (cls, d["date"], d["promo"], d["cat"], 1 if d["official"] else 0, esc(d["hl"]),
         pc_val, kc_val, esc(d["url"]), inner))

_LEAD_CAT = {"title":8,"event":7,"signing":5,"return":4,"departure":4,"business":3,"media":2,"roster":3,"retirement":2,"passing":0}
def _lead_score(d):
    return (100 if d.get("lead") else 0) + (10 if d["official"] else 0) + _LEAD_CAT.get(d["cat"], 1)

def feed_block(items):
    """Lead = biggest story (explicit flag > official title/event > newest); river = the rest, date-sorted."""
    cands = [d for d in items if not d.get("memoriam")] or items
    lead = max(cands, key=lambda d: (_lead_score(d), d["_dt"])) if cands else None
    out = []
    if lead:
        plabel, pvar, pdark = PROMO[lead["promo"]]
        art = ('<div class="lf-lead__art" style="--pc:var(%s)" data-mono="%s">'
               '<span class="lf-lead__badge">The Main Event</span></div>'
               % (pvar, esc(lead.get("mono", plabel))))
        # lead card: wrap copy + art
        c = card(lead, lead=True)
        c = c.replace('</a></article>', art + '</a></article>')
        out.append('<div class="lf-lead">%s</div>' % c)
    river = [d for d in items if d is not lead]
    if river:
        out.append('<div class="lf-river">%s</div>' % "".join(card(d) for d in river))
    return "\n".join(out)

# ------------------------------------------------------------------ WEEK RECAP (real, entity-rich copy)
def recap(items, mon):
    def by(c): return [d for d in items if d["cat"] == c]
    titles, sign, dep = by("title"), by("signing"), by("departure")
    events, biz = by("event"), by("business") + by("media")
    ret, pas, rost, retire = by("return"), by("passing"), by("roster"), by("retirement")
    n = len(items)
    parts = ["The week of %s logged %d dispatch%s across professional wrestling." %
             (wk_range(mon), n, "" if n == 1 else "es")]
    if titles:
        names = "; ".join(t["hl"] for t in titles[:6])
        parts.append("Championships moved: %s." % names)
    if sign:
        parts.append("On the roster front: %s." % "; ".join(s["hl"] for s in sign[:4]))
    if dep or retire:
        parts.append("Departures and farewells: %s." % "; ".join(x["hl"] for x in (dep + retire)[:4]))
    if biz:
        parts.append("Off screen, the business desk tracked: %s." % "; ".join(b["hl"] for b in biz[:4]))
    if events and not titles:
        parts.append("In the ring: %s." % "; ".join(e["hl"] for e in events[:3]))
    return " ".join(parts)

# ------------------------------------------------------------------ SHELL
def shell(title, desc, canonical, main, extra_head=""):
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
      '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
      '<title>%s</title>\n<meta name="description" content="%s">\n<link rel="canonical" href="%s">\n'
      '<meta name="robots" content="index,follow">\n'
      '<meta property="og:type" content="website">\n<meta property="og:title" content="%s">\n'
      '<meta property="og:description" content="%s">\n<meta property="og:url" content="%s">\n'
      '<meta property="og:site_name" content="Wrestle Lore">\n%s'
      '<link rel="stylesheet" href="/css/site.css">\n</head>\n<body>\n'
      '<header class="site-header nav7"></header>\n<main id="main">\n%s\n</main>\n'
      '<footer class="site-footer site-footer--fat"></footer>\n'
      '<script src="/js/media.js" defer></script>\n%s\n</body>\n</html>\n'
      % (esc(title), esc(desc), canonical, esc(title), esc(desc), canonical, extra_head, main, FEED_JS_TAG))

# masthead + control desk (shared by hub + week pages)
def masthead(kicker, big, dateline, edition, standfirst):
    return ('<header class="lf-mast">'
      '<div class="lf-mast__rule"><span>Wrestle Lore</span>'
      '<span class="mid">Results · Title Changes · Signings · The Business</span>'
      '<span>%s</span></div><hr class="lf-hairline">'
      '<h1 class="lf-logo"><span class="the">%s</span>%s</h1><hr class="lf-hairline">'
      '<div class="lf-mast__foot"><span class="lf-dateline">%s</span>'
      '<span class="lf-standfirst">%s</span><span class="lf-editions">%s</span></div></header>'
      % (esc(edition), esc(kicker), esc(big), esc(dateline), esc(standfirst), esc(edition)))

def desk():
    promos = [("all","All",""),("wwe","WWE","--c-wwe"),("nxt","NXT","--c-nxt"),("aew","AEW","--c-aew"),
              ("tna","TNA","--c-tna"),("njpw","NJPW","--c-njpw"),("tko","Business","--c-mens")]
    cats = [("all","All"),("title","Title Changes"),("event","Events"),("signing","Signings"),
            ("departure","Departures"),("return","Returns"),("business","Business"),("roster","Roster")]
    pc = "".join('<button class="lf-chip" data-val="%s" aria-pressed="%s"%s>%s%s</button>'
                 % (v,"true" if v=="all" else "false",
                    (' style="--chip:var(%s)"'%c) if c else "",
                    ('<span class="lf-chip__dot"></span>' if c else ""), esc(l)) for v,l,c in promos)
    cc = "".join('<button class="lf-chip" data-val="%s" aria-pressed="%s">%s</button>'
                 % (v,"true" if v=="all" else "false", esc(l)) for v,l in cats)
    return ('<div class="lf-desk"><div class="lf-desk__row">'
      '<label class="lf-search"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>'
      '<input id="lf-q" type="search" placeholder="Search this feed by name, title or promotion" aria-label="Search" autocomplete="off"></label></div>'
      '<div class="lf-desk__row" style="margin-top:10px"><span class="lf-chiplabel">Promotion</span>'
      '<div class="lf-chiprow" data-facet="promo" style="width:auto;flex:1">%s</div></div>'
      '<div class="lf-desk__row" style="margin-top:8px"><span class="lf-chiplabel">Desk</span>'
      '<div class="lf-chiprow" data-facet="cat" style="width:auto;flex:1">%s</div></div></div>'
      '<p class="lf-count" id="lf-count"></p>' % (pc, cc))

COLOPHON = ('<p class="lf-colophon"><b>The Lore Feed</b> is the newsroom of Wrestle Lore. '
  'Dispatches are filed by hand from named outlets and carry an <b>Official</b> stamp when confirmed by a promotion, '
  'or <b>Report</b> when sourced from the trade press. Each week Monday through Sunday keeps its own page. '
  'Wrestle Lore is an independent, fan-made project and is not affiliated with WWE, TKO Group Holdings, AEW, TNA or NJPW.</p>')

# ------------------------------------------------------------------ WEEK SWITCHER
def week_switcher(current_mon):
    months = [m for m, _ in WEEKS]
    idx = months.index(current_mon) if current_mon in months else -1
    newer = months[idx-1] if idx > 0 else None
    older = months[idx+1] if 0 <= idx < len(months)-1 else None
    def navbtn(mon, label):
        if mon:
            return '<a class="lf-wb__nav" href="/lore-feed/%s/">%s</a>' % (mon.isoformat(), label)
        return '<span class="lf-wb__nav is-off">%s</span>' % label
    chips = []
    for mon, _ in WEEKS:
        cur = (mon == current_mon)
        chips.append('<a class="lf-wb__wk%s" href="/lore-feed/%s/"%s>%s</a>'
                     % (" is-cur" if cur else "", mon.isoformat(),
                        ' aria-current="page"' if cur else "", short(mon)))
    return ('<nav class="lf-weekbar" aria-label="Switch week">%s'
            '<div class="lf-wb__track">%s</div>%s</nav>'
            % (navbtn(newer, "Newer week"), "".join(chips), navbtn(older, "Older week")))

# ------------------------------------------------------------------ WEEK PAGE
def week_page(mon, items, older_mon, newer_mon):
    wid = mon.isoformat()
    label = wk_label(mon)
    title = "%s — WWE, AEW, TNA & NXT News | Wrestle Lore" % label
    desc = ("%s in professional wrestling: every title change, signing, result and business story across WWE, AEW, TNA, NXT and NJPW, dated and sourced." % label)
    canonical = "%s/lore-feed/%s/" % (BASE, wid)
    nav = []
    if newer_mon: nav.append('<a class="link-more" href="/lore-feed/%s/">Newer week</a>' % newer_mon.isoformat())
    nav.append('<a class="link-more" href="/lore-feed/">All weeks</a>')
    if older_mon: nav.append('<a class="link-more" href="/lore-feed/%s/">Older week</a>' % older_mon.isoformat())
    # JSON-LD: CollectionPage + ItemList + BreadcrumbList
    li = []
    for i, d in enumerate(items, 1):
        li.append('{"@type":"ListItem","position":%d,"name":"%s","url":"%s"}' % (i, esc(d["hl"]).replace('"','\\"'), esc(d["url"])))
    jsonld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage",'
      '"name":"%s","description":"%s","url":"%s","isPartOf":{"@type":"WebSite","name":"Wrestle Lore","url":"%s/"},'
      '"mainEntity":{"@type":"ItemList","numberOfItems":%d,"itemListElement":[%s]}}</script>\n'
      '<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
      '{"@type":"ListItem","position":1,"name":"Home","item":"%s/"},'
      '{"@type":"ListItem","position":2,"name":"Lore Feed","item":"%s/lore-feed/"},'
      '{"@type":"ListItem","position":3,"name":"%s","item":"%s"}]}</script>\n'
      % (esc(label), esc(desc), canonical, BASE, len(items), ",".join(li),
         BASE, BASE, esc(label), canonical))
    main = ('<div class="lf-wrap lf-wrap--week">'
      '<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li>'
      '<li><a href="/lore-feed/">Lore Feed</a></li><li aria-current="page">%s</li></ol></nav>'
      '%s'
      '%s%s'
      '<p class="lf-recap">%s</p>'
      '%s'
      '<div class="lf-weeknav">%s</div>%s</div>'
      % (esc(label), week_switcher(mon),
         masthead("The Week in Wrestling", label.replace("Week of ","Week of "), wk_range(mon),
                  "%d filed" % len(items), "Every result, title change, signing and passing, dated and sourced."),
         desk(), esc(recap(items, mon)), feed_block(items), " ".join(nav), COLOPHON))
    return shell(title, desc, canonical, main, extra_head=jsonld)

# ------------------------------------------------------------------ HUB PAGE
def week_index_card(mon, items):
    label = wk_label(mon)
    top = next((d for d in items if d.get("lead")), items[0])
    tallies = {}
    for d in items: tallies[d["cat"]] = tallies.get(d["cat"], 0) + 1
    chips = "".join('<span class="lf-wi__chip">%d %s</span>' % (n, CAT[c][0]) for c, n in
                    sorted(tallies.items(), key=lambda kv: -kv[1])[:3])
    return ('<a class="lf-wi" href="/lore-feed/%s/">'
      '<span class="lf-wi__k">%s</span><span class="lf-wi__n">%d dispatches</span>'
      '<span class="lf-wi__hl">%s</span><span class="lf-wi__chips">%s</span></a>'
      % (mon.isoformat(), esc(label), len(items), esc(top["hl"]), chips))

def hub_page(weeks):
    cur_mon, cur_items = weeks[0]
    title = "The Lore Feed — WWE, AEW, TNA & NXT News, Week by Week | Wrestle Lore"
    desc = ("The newsroom of Wrestle Lore: every title change, signing, result and business story across WWE, AEW, TNA, NXT and NJPW, filed weekly and archived by the week.")
    canonical = "%s/lore-feed/" % BASE
    dateline = "%s, %s %d, %d" % (["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][TODAY.weekday()],
                                  MONL[TODAY.month-1], TODAY.day, TODAY.year)
    li = []
    for i, (mon, items) in enumerate(weeks, 1):
        li.append('{"@type":"ListItem","position":%d,"name":"%s","url":"%s/lore-feed/%s/"}' %
                   (i, wk_label(mon), BASE, mon.isoformat()))
    jsonld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage",'
      '"name":"The Lore Feed","description":"%s","url":"%s","isPartOf":{"@type":"WebSite","name":"Wrestle Lore","url":"%s/"},'
      '"mainEntity":{"@type":"ItemList","name":"Weekly editions","numberOfItems":%d,"itemListElement":[%s]}}</script>\n'
      '<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
      '{"@type":"ListItem","position":1,"name":"Home","item":"%s/"},'
      '{"@type":"ListItem","position":2,"name":"Lore Feed","item":"%s"}]}</script>\n'
      % (esc(desc), canonical, BASE, len(weeks), ",".join(li), BASE, canonical))
    index = "".join(week_index_card(mon, items) for mon, items in weeks)
    main = ('<div class="lf-wrap">'
      '%s%s%s'
      '<div class="lf-dept"><span class="kk">// Front Page</span><h2>This Week</h2><span class="ln"></span>'
      '<a class="lf-dept__more" href="/lore-feed/%s/">Full week page</a></div>'
      '%s'
      '<div class="lf-dept"><span class="kk">// The Vault</span><h2>Browse by Week</h2><span class="ln"></span></div>'
      '<div class="lf-weekindex">%s</div>'
      '%s</div>'
      % (masthead("The Weekly", "Lore Feed", dateline, "Vol. I",
                  "Every result, title change, signing and passing across professional wrestling. Reported, dated, and filed."),
         desk(), week_switcher(cur_mon), cur_mon.isoformat(), feed_block(cur_items), index, COLOPHON))
    return shell(title, desc, canonical, main, extra_head=jsonld)

# ------------------------------------------------------------------ TICKER (rolling 7 days) -> meganav.html
def ticker_items(days=7, cap=8):
    cutoff = TODAY - datetime.timedelta(days=days)
    within = [d for d in DISPATCHES if d["_dt"] >= cutoff][:cap]
    if not within:  # never leave the ticker empty; fall back to newest
        within = DISPATCHES[:cap]
    return within

def ticker_markup():
    items = ticker_items()
    def sq(d):
        _, pvar, _ = PROMO[d["promo"]]
        return pvar
    lives = []
    for i, d in enumerate(items):
        lives.append('<a class="rt-item%s" href="%s" target="_blank" rel="noopener">'
          '<span class="rt-sq" style="background:var(%s)"></span>'
          '<span class="rt-name">%s</span><span class="rt-txt">%s</span>'
          '<span class="rt-t rf-time" datetime="%sT12:00:00Z">%s</span></a>'
          % (" is-on" if i == 0 else "", esc(d["url"]), sq(d), esc(d["who"]), esc(d["hl"]),
             d["date"], short(d["_dt"])))
    dots = "".join('<span class="rt-dot%s"></span>' % (" is-on" if i == 0 else "") for i in range(len(items)))
    live_svg = ('<span class="rt-live"><svg class="rt-live-mk" width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">'
      '<circle cx="16" cy="16" r="9.5" fill="none" stroke="#21e06a" stroke-width="0.9" opacity=".25"/>'
      '<circle cx="16" cy="16" r="4.4" fill="#21e06a"><animate attributeName="r" values="4.2;5.2;4.2" dur="2s" repeatCount="indefinite"/>'
      '<animate attributeName="opacity" values="1;.6;1" dur="2s" repeatCount="indefinite"/></circle>'
      '<circle cx="16" cy="16" r="2.1" fill="#8dffb9"/></svg></span>')
    return ('<div class="ticker7 rt" aria-label="Live wrestling headlines">\n'
      '  <div class="rt-tag">%sLIVE</div>\n'
      '  <div class="rt-stage">%s</div>\n'
      '  <div class="rt-dots" aria-hidden="true">%s</div>\n'
      '  <a class="rt-more" href="/lore-feed/">Lore Feed</a>\n'
      '</div>' % (live_svg, "".join(lives), dots))

def patch_meganav():
    p = os.path.join(ROOT, "components", "meganav.html")
    if not os.path.exists(p):
        print("!! meganav.html not found, skipping ticker patch"); return
    src = open(p, encoding="utf-8").read()
    new = ticker_markup()
    patched = re.sub(r'<div class="ticker7 rt".*?Lore Feed</a>\s*</div>', new, src, count=1, flags=re.S)
    if patched != src:
        open(p, "w", encoding="utf-8").write(patched)
        print("ticker patched into components/meganav.html (%d items, rolling 7d from %s)" % (len(ticker_items()), TODAY))
    else:
        print("!! ticker pattern not matched — check meganav.html")

# ------------------------------------------------------------------ CSS injection
def inject_css():
    p = os.path.join(ROOT, "css", "site.css")
    css = open(p, encoding="utf-8").read()
    block = "/* LOREFEED:START */\n" + LF_CSS + "\n/* LOREFEED:END */"
    if "/* LOREFEED:START */" in css:
        css = re.sub(r"/\* LOREFEED:START \*/.*?/\* LOREFEED:END \*/", block, css, flags=re.S)
    else:
        css = css.rstrip() + "\n\n" + block + "\n"
    open(p, "w", encoding="utf-8").write(css)
    print("css/site.css: LOREFEED block written")

# ------------------------------------------------------------------ sitemap
def update_sitemap():
    p = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(p): return
    xml = open(p, encoding="utf-8").read()
    urls = ["/lore-feed/"] + ["/lore-feed/%s/" % mon.isoformat() for mon, _ in WEEKS]
    add = ""
    for u in urls:
        loc = BASE + u
        if loc not in xml:
            add += '  <url><loc>%s</loc><changefreq>weekly</changefreq></url>\n' % loc
    if add:
        xml = xml.replace("</urlset>", add + "</urlset>")
        open(p, "w", encoding="utf-8").write(xml)
        print("sitemap +%d urls" % add.count("<url>"))

def write(path, htmlstr):
    full = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(htmlstr)

# ------------------------------------------------------------------ PREVIEW (self-contained)
def preview(path, htmlstr, style):
    os.makedirs(PREVIEW_DIR, exist_ok=True)
    h = htmlstr
    h = h.replace('<link rel="stylesheet" href="/css/site.css">', style)
    h = h.replace('<script src="/js/media.js" defer></script>', "")
    h = h.replace('<header class="site-header nav7"></header>',
                  '<header class="site-header nav7">%s<div class="pv-bar"><b>WRESTLE LORE</b><span>preview — brand fonts load from production</span></div></header>' % ticker_markup())
    h = h.replace('<footer class="site-footer site-footer--fat"></footer>', '')
    open(os.path.join(PREVIEW_DIR, path), "w", encoding="utf-8").write(h)

# ------------------------------------------------------------------ CSS + JS payloads
_here = os.path.dirname(os.path.abspath(__file__))
LF_CSS = open(os.path.join(_here, "lorefeed.css"), encoding="utf-8").read() if os.path.exists(os.path.join(_here, "lorefeed.css")) else ""
FEED_JS = open(os.path.join(_here, "lorefeed.js"), encoding="utf-8").read() if os.path.exists(os.path.join(_here, "lorefeed.js")) else ""
FEED_JS_TAG = "<script>%s</script>" % FEED_JS if FEED_JS else ""

PREVIEW_FONTS = """
@font-face{font-family:"Anton";font-display:swap;src:url("https://wrestlelore.com/fonts/anton-latin-400-normal.woff2") format("woff2");}
@font-face{font-family:"Oswald";font-weight:400;font-display:swap;src:url("https://wrestlelore.com/fonts/oswald-latin-400-normal.woff2") format("woff2");}
@font-face{font-family:"Oswald";font-weight:600;font-display:swap;src:url("https://wrestlelore.com/fonts/oswald-latin-600-normal.woff2") format("woff2");}
@font-face{font-family:"Oswald";font-weight:700;font-display:swap;src:url("https://wrestlelore.com/fonts/oswald-latin-700-normal.woff2") format("woff2");}
@font-face{font-family:"Inter";font-weight:400;font-display:swap;src:url("https://wrestlelore.com/fonts/inter-latin-400-normal.woff2") format("woff2");}
@font-face{font-family:"Inter";font-weight:600;font-display:swap;src:url("https://wrestlelore.com/fonts/inter-latin-600-normal.woff2") format("woff2");}
@font-face{font-family:"JetBrains Mono";font-weight:400;font-display:swap;src:url("https://wrestlelore.com/fonts/jetbrains-mono-latin-400-normal.woff2") format("woff2");}
"""
PREVIEW_TOKENS = """
:root{--c-bg:#0a0b0d;--c-bg-elev-1:#121418;--c-bg-elev-2:#1a1d23;--c-bg-elev-3:#23272f;
--c-line:#2b3038;--c-line-strong:#3a414c;--c-text:#e8eaed;--c-text-muted:#a2a9b4;--c-text-dim:#6b727d;
--c-gold:#d4af37;--c-gold-bright:#f2cc4b;--c-gold-dim:#8c7420;--c-red:#e11d2a;--c-red-bright:#ff3b48;
--c-win:#2fbf71;--c-focus:#5aa9ff;--c-media:#a855f7;--c-mens:#8593a6;
--c-wwe:#c8102e;--c-nxt:#f5c518;--c-tna:#1e73be;--c-njpw:#d81f26;--c-aew:#c8a24a;--line:#2b3038;--redb:#ff3b48;
--font-display:"Anton","Arial Narrow",sans-serif;--font-cond:"Oswald","Arial Narrow",sans-serif;
--font-body:"Inter",system-ui,Arial,sans-serif;--font-sans:var(--font-body);--font-mono:"JetBrains Mono",ui-monospace,Menlo,monospace;}
*{box-sizing:border-box;}
body{margin:0;background:var(--c-bg);color:var(--c-text);font-family:var(--font-body);font-size:16px;line-height:1.5;
background-image:radial-gradient(1200px 500px at 50% -8%,rgba(212,175,55,.05),transparent 60%);}
a{color:inherit;text-decoration:none;}::selection{background:var(--c-gold);color:#000;}
"""
TICKER_CSS = """
.ticker7{background:#000;border-bottom:1px solid var(--c-line);display:flex;align-items:stretch;height:38px;font-size:13px;}
.ticker7.rt{border-bottom:1px solid var(--c-line);}
.rt-tag{flex:0 0 auto;display:flex;align-items:center;gap:.55em;padding:0 16px;height:100%;font-family:var(--font-mono);font-size:10.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--c-text-muted);border-right:1px solid var(--c-line);white-space:nowrap;}
.rt-live{display:inline-flex;align-items:center;justify-content:center;width:16px;height:16px;flex:0 0 auto;}
.rt-live-mk{display:block;filter:drop-shadow(0 0 3px rgba(33,224,106,.85));}
.rt-stage{position:relative;flex:1;min-width:0;height:100%;}
.rt-item{position:absolute;inset:0;display:flex;align-items:center;gap:.75em;padding:0 22px;opacity:0;transition:opacity .6s ease;pointer-events:none;white-space:nowrap;}
.rt-item.is-on{opacity:1;pointer-events:auto;}
.rt-sq{width:7px;height:7px;border-radius:1px;flex:0 0 auto;}
.rt-name{font-family:var(--font-cond);text-transform:uppercase;letter-spacing:.06em;font-size:14px;color:var(--c-text);flex:0 0 auto;}
.rt-item:hover .rt-name{color:var(--c-gold-bright);}
.rt-txt{font-family:var(--font-body);font-size:13px;color:var(--c-text-muted);overflow:hidden;text-overflow:ellipsis;}
.rt-t{font-family:var(--font-mono);font-size:11px;color:var(--c-text-dim);margin-left:auto;flex:0 0 auto;padding-left:1em;letter-spacing:.03em;text-transform:uppercase;}
.rt-dots{flex:0 0 auto;display:flex;align-items:center;gap:5px;padding:0 15px;height:100%;border-left:1px solid var(--c-line);}
.rt-dot{width:5px;height:5px;border-radius:99px;background:var(--c-line-strong);}
.rt-dot.is-on{background:var(--c-gold);}
.rt-more{flex:0 0 auto;display:flex;align-items:center;height:100%;padding:0 16px;border-left:1px solid var(--c-line);font-family:var(--font-mono);font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--c-gold);white-space:nowrap;}
"""

def build_preview_style():
    return "<style>\n" + PREVIEW_FONTS + PREVIEW_TOKENS + TICKER_CSS + LF_CSS + "\n</style>"

# a tiny preview rotator so the ticker cycles in the standalone previews (prod uses js/nav.js)
PREVIEW_TICKER_JS = """<script>(function(){var s=document.querySelector('.rt-stage');if(!s)return;var it=[].slice.call(s.querySelectorAll('.rt-item')),d=[].slice.call(document.querySelectorAll('.rt-dot')),i=0;setInterval(function(){it[i].classList.remove('is-on');if(d[i])d[i].classList.remove('is-on');i=(i+1)%it.length;it[i].classList.add('is-on');if(d[i])d[i].classList.add('is-on');},3200);})();</script>"""

# ------------------------------------------------------------------ MAIN
import re as _re_rail
def rel_ago(d):
    n = (TODAY - d).days
    if n <= 0: return "today"
    if n == 1: return "1d ago"
    if n < 7: return "%dd ago" % n
    w = n // 7
    return "1w ago" if w == 1 else "%dw ago" % w
def home_rail_items(cap=7):
    feat = [d for d in DISPATCHES if d.get("home")]
    feat.sort(key=lambda x: x["date"], reverse=True)
    return feat[:cap]
def render_home_rail():
    out = []
    for d in home_rail_items():
        tags = d.get("htags") or "roster"
        out.append('<a class="hrl-d" data-tags="%s" href="%s" target="_blank" rel="noopener"><p class="hrl-dt">%s</p><h4 class="hrl-dh"><b>%s</b> %s</h4><p class="hrl-ds">Source: %s</p></a>' % (esc(tags), esc(d["url"]), esc(rel_ago(d2date(d["date"]))), esc(d["who"]), esc(d["dek"]), esc(d["src"])))
    return "".join(out)
def update_home_rail():
    p = os.path.join(ROOT, "index.html")
    if not os.path.exists(p): return
    html = open(p, encoding="utf-8").read()
    items = render_home_rail()
    new, n = _re_rail.subn(r'(<div class="hrl-list">).*?(<p class="hrl-empty")', lambda m: m.group(1) + items + m.group(2), html, count=1, flags=_re_rail.DOTALL)
    if n == 1 and new != html:
        open(p, "w", encoding="utf-8").write(new); print("home rail patched into index.html (%d items)" % len(home_rail_items()))
    elif n == 0:
        print("WARN: hrl-list not found in index.html")
    else:
        print("home rail already current")

if __name__ == "__main__":
    if not LF_CSS:
        raise SystemExit("build/lorefeed.css missing — write it first")
    # 1) real repo artifacts
    inject_css()
    for i, (mon, items) in enumerate(WEEKS):
        newer = WEEKS[i-1][0] if i > 0 else None
        older = WEEKS[i+1][0] if i < len(WEEKS)-1 else None
        write("/lore-feed/%s/index.html" % mon.isoformat(), week_page(mon, items, older, newer))
    write("/lore-feed/index.html", hub_page(WEEKS))
    patch_meganav()
    update_home_rail()
    update_sitemap()
    # 2) self-contained previews (for review only; not committed)
    style = build_preview_style()
    cur_mon, cur_items = WEEKS[0]
    older = WEEKS[1][0] if len(WEEKS) > 1 else None
    preview("lore-feed-hub-preview.html", hub_page(WEEKS).replace(FEED_JS_TAG, FEED_JS_TAG + PREVIEW_TICKER_JS), style)
    preview("lore-feed-week-preview.html",
            week_page(cur_mon, cur_items, older, None).replace(FEED_JS_TAG, FEED_JS_TAG + PREVIEW_TICKER_JS), style)
    print("previews -> %s" % PREVIEW_DIR)
    print("weeks: %d  dispatches: %d  ticker(7d): %d" % (len(WEEKS), len(DISPATCHES), len(ticker_items())))
    print("done. now run: python3 build/apply_shell.py")
