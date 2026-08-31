# -*- coding: utf-8 -*-
"""Ric Flair - dossier data.

Sources: web-verified August 31, 2026 - Wikipedia (main biography, Ric Flair's Last Match and
Bash at the Beach 1994 event pages), Slam Wrestling and F4WOnline on his August 2026 health
situation. Every match row carries a day-precision date from those sources or the canonical,
multiply-documented date of a major card.

Deliberate omissions:
  * No career win-loss total across a 50-year career - none exists to verify.
  * United States and tag championship reigns are listed with WWE's counts and without
    individual dates, which were not verified in this pass.
  * The world title count is presented as the dispute it is: 16 recognized, 21 most agreed,
    sources ranging to 25. No single number is stated as settled fact anywhere on this page.
"""

# ----------------------------------------------------------------- record rows
# Twelve documented bouts - the first and last NWA title wins, the Steamboat and Funk peaks,
# the WWF interlude, the Hogan and Michaels endings, and the 2022 farewell.
ROWS = [
    dict(result="W", date="1981-09-17", promo="NWA", landmark=True,
         event="Kansas City", opponent="Dusty Rhodes",
         stip="Singles — first NWA World title, Lou Thesz as referee", title="NWA World Heavyweight Championship"),
    dict(result="W", date="1983-11-24", promo="NWA", landmark=True,
         event="Starrcade — Greensboro", opponent="Harley Race",
         stip="Steel cage — A Flair for the Gold", title="NWA World Heavyweight Championship"),
    dict(result="L", date="1989-02-20", promo="NWA", landmark=True,
         event="Chi-Town Rumble", opponent="Ricky Steamboat",
         stip="Singles — the trilogy opens", title="NWA World Heavyweight Championship"),
    dict(result="L", date="1989-04-02", promo="NWA",
         event="Clash of the Champions VI — New Orleans", opponent="Ricky Steamboat",
         stip="Best of three falls — 55 minutes", title="NWA World Heavyweight Championship"),
    dict(result="W", date="1989-05-07", promo="NWA", landmark=True,
         event="WrestleWar — Nashville", opponent="Ricky Steamboat",
         stip="Singles — regains the title; PWI Match of the Year", title="NWA World Heavyweight Championship"),
    dict(result="W", date="1989-11-15", promo="NWA", landmark=True,
         event="Clash of the Champions IX — Troy", opponent="Terry Funk",
         stip="I Quit match", title=""),
    dict(result="W", date="1992-01-19", promo="WWE", landmark=True, type="tag",
         event="Royal Rumble — Albany", opponent="The 1992 Royal Rumble field",
         stip="Entered No. 3, won the vacant WWF Championship after an hour", title="WWF Championship"),
    dict(result="L", date="1992-04-05", promo="WWE",
         event="WrestleMania VIII — Hoosier Dome", opponent="Randy Savage", opponent_html=True,
         stip="Singles — the Elizabeth photos feud", title="WWF Championship"),
    dict(result="W", date="1992-09-01", promo="WWE",
         event="Prime Time Wrestling taping — Hershey", opponent="Randy Savage", opponent_html=True,
         stip="Singles — second WWF title; aired September 14", title="WWF Championship"),
    dict(result="L", date="1994-07-17", promo="WCW", landmark=True,
         event="Bash at the Beach — Orlando", opponent="Hulk Hogan", opponent_html=True,
         stip="Singles — Hogan's first WCW match takes the title", title="WCW World Heavyweight Championship"),
    dict(result="L", date="2008-03-30", promo="WWE", landmark=True,
         event="WrestleMania XXIV — Orlando", opponent="Shawn Michaels",
         stip="Career-threatening match — &ldquo;I'm sorry, I love you&rdquo;", title=""),
    dict(result="W", date="2022-07-31", promo="JCP", landmark=True, type="tag",
         event="Ric Flair's Last Match — Nashville", opponent="Jeff Jarrett & Jay Lethal",
         stip="Tag with Andrade El Idolo — the actual farewell, at 73", title=""),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Randy Savage": "randy-savage", "Hulk Hogan": "hulk-hogan"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="ric-flair",
    name="Ric Flair",
    realname="Richard Morgan Fliehr",
    epithet="The Nature Boy",
    hook="Record & Titles",

    meta_desc=("Ric Flair, the Nature Boy, is recognized as a 16-time world champion — a number he "
               "himself puts at 21. The Steamboat trilogy, the 1992 Royal Rumble, two retirements "
               "and a 2022 farewell at 73. Full record, titles and career."),
    og_desc=("The Nature Boy: 16 recognized world championships (21 by the most common count), the "
             "1989 Steamboat trilogy, a Royal Rumble won from the No. 3 spot, and a career that "
             "refused to end until July 31, 2022, when he was 73."),
    tw_desc="Ric Flair: 16 recognized world titles — he says 21 — and a 50-year career.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1972",
    height_imp="6&#8242;1&#8243;",
    weight_lb="243",
    world_titles="16",
    vitals_tagline="To be the man, you gotta beat the man",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="RF", title="WWE Shop", sub="Legacy merchandise · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable legend across the 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="WWE", title="Hall of Fame Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/ric-flair"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Nature Boy &middot; Naitch &middot; The Dirtiest Player in the Game",
    hero_tag="Memphis, Tennessee &middot; <em>AWA &middot; JCP/NWA &middot; WCW &middot; WWF/WWE &middot; TNA &middot; AEW &middot; 1972&ndash;2022</em>",
    now_label="NOW",
    now_bold="Retired &mdash; last match July 31, 2022",
    now_tail=" &middot; at 77 he accepted the Cauliflower Alley Club&rsquo;s Iron Mike Mazurki Award "
             "by video in August 2026, kept home by a blood clot in his leg that he says limits "
             "long travel",
    hstats=[
        dict(value="16", x=False, label="Recognized World Titles"),
        dict(value="21", x=True,  label="By His Own Count"),
        dict(value="2",  x=False, label="HOF Inductions"),
        dict(value="73", x=False, label="Age at Last Match"),
    ],
    ghost_link="From a broken back in 1975 to a farewell at 73",
    vlabel="Est. 1972 &middot; Memphis, Tennessee",
    mono="RF",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Ric Flair</b> is the most decorated world champion in the history of the business and "
        "its most complete performer over distance: a limousine-riding, jet-flying heel who could "
        "wrestle an hour every night of the week, in a different town, against a different local "
        "hero, and send the crowd home furious. Born February 25, 1949 &mdash; adopted as an infant "
        "in Memphis, an episode tied to the Tennessee Children's Home Society scandal &mdash; and "
        "raised in Minnesota, he debuted on December 10, 1972 in Rice Lake, Wisconsin, trained by "
        "Verne Gagne. Three years in, on October 4, 1975, a plane crash broke his back in three "
        "places; doctors told him at 26 that he was done, and he was wrestling again within months, "
        "having rebuilt himself from a 300-pound brawler into the figure-four-and-chops stylist the "
        "&ldquo;Nature Boy&rdquo; name required. Everything after &mdash; the robes, the "
        "&ldquo;Woooo!&rdquo;, the sixty-minute broadways &mdash; came out of that reinvention.",

        "Now the number. WWE recognizes Flair as a <b>16-time world champion</b>; Flair himself "
        "claims <b>21</b>, which is also the figure most sources land on; counts across the "
        "literature run as high as 25, depending on how you treat title changes the NWA later "
        "struck from the record and short reigns overseas. "
        ''
        "This page publishes the recognized 16 &mdash; commonly broken out as eight NWA, six WCW "
        "and two WWF reigns &mdash; and states the dispute rather than resolving it, because the "
        "sources genuinely disagree and the man himself is on the higher side. What no count "
        "disputes: the first reign began September 17, 1981 in Kansas City against Dusty Rhodes, "
        "with Lou Thesz refereeing, and for the following decade he was the touring NWA champion "
        "against whom every territory measured its best.",

        "The résumé peaks are specific. Starrcade 1983, November 24: he took the title from Harley "
        "Race in a steel cage, the match the first Starrcade was built around. The 1989 trilogy "
        "with Ricky Steamboat &mdash; Chi-Town Rumble on February 20, the 55-minute best-of-three "
        "at Clash VI on April 2, the regain at WrestleWar on May 7 &mdash; is the most acclaimed "
        "series of matches in American wrestling history, and he followed it immediately with the "
        "Terry Funk I Quit match at Clash IX on November 15. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">60</span>'
        '<span class="pull-cap">minutes in the 1992 Royal Rumble, entered at No. 3, to win the vacant WWF Championship</span></span>'
        "Fired by WCW in 1991, he walked into the WWF with the big gold belt as &ldquo;the Real "
        "World's Champion&rdquo; and won the vacant WWF Championship in the 1992 Royal Rumble on "
        "January 19 &mdash; entering third and surviving the hour, still the definitive Rumble "
        "performance. He traded that title with Randy Savage in 1992, went home to WCW, lost the "
        "unification match to Hulk Hogan at Bash at the Beach on July 17, 1994, and kept "
        "headlining, on and off, into his fifties.",

        "He has retired twice, and only the second one held. WWE gave him the send-off at "
        "WrestleMania XXIV on March 30, 2008 &mdash; a career-threatening match Shawn Michaels "
        "ended with &ldquo;I'm sorry, I love you&rdquo; before the superkick &mdash; followed by "
        "the only Hall of Fame induction ever staged for an active competitor's farewell. It "
        "lasted eighteen months; he wrestled on for TNA into 2011. The real ending was July 31, "
        "2022 in Nashville: Ric Flair's Last Match, a Starrcast event run under the revived Jim "
        "Crockett Promotions banner, where he and his son-in-law Andrade El Idolo beat Jeff "
        "Jarrett and Jay Lethal &mdash; Flair, 73, taking the pin-securing figure-four after brass "
        "knuckles found their way to him. Since then he has been a legends-deal presence &mdash; "
        "AEW signed him in that role in 2023, and he seconded Sting's retirement match at "
        "Revolution in March 2024. He survived a 2017 health collapse that put him in a medically "
        "induced coma, and as of August 2026, at 77, he is managing a blood clot in his leg that "
        "kept him from traveling to the Cauliflower Alley Club reunion &mdash; he accepted its "
        "Iron Mike Mazurki Award by video on August 26, with Jerry Lawler presenting, and reports "
        "himself otherwise well.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["NWA", "WWE", "WCW", "JCP"],
        promo_labels={"NWA": "JCP/NWA", "WWE": "WWF/WWE", "WCW": "WCW", "JCP": "JCP 2022"},
        stats=[
            ("16",  "Recognized world titles"),
            ("21",  "By his own count"),
            ("1",   "Royal Rumble win"),
            ("2",   "HOF inductions"),
            ("50",  "Years, debut to last match"),
            ("73",  "Age at final bell"),
        ],
        lead=("Twelve documented bouts across fifty years &mdash; the first and most famous NWA "
              "title wins, the full 1989 Steamboat trilogy, the Rumble hour, and both endings. A "
              "curated ledger, not a career count: nobody has a verifiable win&ndash;loss total for "
              "a man who worked sixty-minute draws in territories whose records are gone, and none "
              "is invented here. The September 1992 Savage row is dated to the Hershey taping; it "
              "aired September 14. Filter by match type, tap any column header to sort, and turn "
              "spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the reputation rests on. The 1989 runs against Steamboat and Funk "
                    "sit at the top of the American canon; the Steamboat matches' five-star Meltzer "
                    "ratings are among the most widely republished in the Observer's history, and "
                    "no rating is shown where one could not be verified."),
    signature=[
        dict(rating="5.0", event="Chi-Town Rumble 1989", opponent="Ricky Steamboat",
             stip="NWA World Heavyweight Championship — the trilogy opens"),
        dict(rating="5.0", event="Clash of the Champions VI", opponent="Ricky Steamboat",
             stip="NWA World title — 55 minutes, best of three falls"),
        dict(rating="5.0", event="WrestleWar 1989", opponent="Ricky Steamboat",
             stip="NWA World title — the regain; PWI Match of the Year"),
        dict(rating="&mdash;", event="Clash of the Champions IX", opponent="Terry Funk",
             stip="I Quit match — the year's other masterpiece"),
        dict(rating="&mdash;", event="Royal Rumble 1992", opponent="The 30-man field",
             stip="From No. 3, an hour, for the vacant WWF Championship"),
    ],
    signature_count_word="five",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("16",       "Recognized world reigns"),
            ("8",        "NWA World titles"),
            ("6",        "WCW World titles"),
            ("2",        "WWF Championships"),
        ],
        lead=("The most world championship reigns ever recognized for one man &mdash; and a count "
              "that has never once been settled. The breakdown below follows WWE's recognized 16; "
              "the alternative counts are explained where they diverge. Individual reign dates for "
              "the midcard and tag titles were not verified in this pass and are not invented."),
        rows=[
            dict(ic="N", name="NWA World Heavyweight Championship", count="8",
                 sub="First won September 17, 1981 from Dusty Rhodes in Kansas City, Lou Thesz "
                     "refereeing &middot; the Starrcade 1983 cage win over Harley Race and the "
                     "WrestleWar 1989 regain from Ricky Steamboat sit inside these reigns &middot; "
                     "counts above 16 mostly add reigns the NWA later struck from its records"),
            dict(ic="C", name="WCW World Heavyweight Championship", count="6",
                 sub="The post-1991 lineage &middot; last major loss of the unification era to Hulk "
                     "Hogan at Bash at the Beach, July 17, 1994 &middot; he won the final reign in "
                     "2000 during the company&rsquo;s chaotic last year"),
            dict(ic="W", name="WWF Championship", count="2",
                 sub="Both in 1992: the Royal Rumble win on January 19 &mdash; vacant title, No. 3 "
                     "entry, roughly an hour survived &mdash; and the regain from Randy Savage at "
                     "the September 1 Hershey taping"),
            dict(ic="I", name="WWE Intercontinental Championship", count="1",
                 sub="Won from Carlito at Unforgiven, September 18, 2005, at age 56 &mdash; making "
                     "him one of the oldest champions in the title&rsquo;s history"),
            dict(ic="U", name="United States Championship", count="6",
                 sub="NWA/WCW lineage, as WWE counts them &middot; individual reign dates not "
                     "verified in this pass"),
            dict(ic="T", name="World Tag Team Championship", count="1",
                 sub="Won with Roddy Piper from the Spirit Squad at Cyber Sunday in November 2006 "
                     "&middot; his lone WWE tag reign"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="He invented the modern wrestling stable, then joined its descendants.",
        cards=[
            dict(era="JCP/NWA &amp; WCW &middot; 1985&ndash;1999",
                 name="The Four Horsemen",
                 members="Ric Flair, Arn Anderson, Tully Blanchard, Ole Anderson, Barry Windham and "
                         "later members",
                 desc="The first modern stable and still the standard: four men in suits who "
                      "justified every screwjob finish as excellence in numbers. Formed organically "
                      "in 1985 out of the Andersons' kayfabe kinship with Flair, it protected his "
                      "NWA reigns for a decade across multiple incarnations. Inducted into the WWE "
                      "Hall of Fame as a unit in 2012 — Flair's second induction, making him the "
                      "first two-time inductee."),
            dict(era="WWE &middot; 2003&ndash;2005",
                 name="Evolution",
                 members="Triple H, Ric Flair, Batista, Randy Orton",
                 desc="Past, present and two futures — Flair as the living credential beside Triple "
                      "H's title reigns while Orton and Batista apprenticed. His late-career "
                      "renaissance as a worker and talker ran through it, and both apprentices "
                      "credit him as the education."),
            dict(era="TNA &middot; 2010&ndash;2011",
                 name="Fortune",
                 members="Ric Flair, AJ Styles, Kazarian, Beer Money and others",
                 desc="A deliberate Horsemen homage he fronted during his TNA run — the faction "
                      "gathering TNA's best pure wrestlers under his name. The run ended his "
                      "full-time wrestling; his last TNA match came in 2011."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One character, worn for half a century and adjusted by decade: the <b>Nature Boy</b> "
             "name was taken from Buddy Rogers, the act made permanent after the 1975 plane crash "
             "forced the rebuild.",
        cards=[
            dict(mono="NB", era="Mid-Atlantic &middot; 1974&ndash;1981", name="The Nature Boy, inherited",
                 desc="Adopted Buddy Rogers' moniker and settled the claim against Rogers himself in "
                      "a 1979 program. The robes, the strut and the bleached hair date from here; "
                      "the crash-enforced style change — from brawling heavyweight to cardio "
                      "machine — is what made the act tourable."),
            dict(mono="CH", era="NWA &middot; 1981&ndash;1991", name="The Touring Champion",
                 desc="The limousine-riding, jet-flying, kiss-stealing, wheelin'-dealin' son of a "
                      "gun — the custom-fit heel who defended the ten pounds of gold an hour a "
                      "night in every territory the NWA had. The 'dirtiest player in the game' "
                      "toolkit — the eye poke, the knee, the trunks, Woooo! — was standardized "
                      "here."),
            dict(mono="RW", era="WWF &middot; 1991&ndash;1993", name="The Real World's Champion",
                 desc="Arrived carrying the actual big gold belt after WCW fired him without "
                      "recovering it, and called himself the real champion on their television — a "
                      "shoot wearing an angle's clothes. Won the 1992 Rumble; the 'Elizabeth photos' "
                      "program with Randy Savage followed."),
            dict(mono="NA", era="WCW, WWE, TNA, AEW &middot; 1993&ndash;present", name="Naitch",
                 desc="The elder statesman version: Horsemen reunions, Evolution, the 2008 "
                      "WrestleMania farewell, the un-retirement, the 2022 Last Match, and the "
                      "legends-role years since — plus a cultural afterlife ('Ric Flair Drip', the "
                      "30 for 30) bigger than most active careers."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Rice Lake, 1972, to Nashville, 2022 — with a broken back three years in.",
        rows=[
            dict(year="1972", title="Debut under Verne Gagne",
                 desc="Debuts December 10, 1972 in Rice Lake, Wisconsin, out of Gagne's notoriously "
                      "brutal AWA camp."),
            dict(year="1975", title="The plane crash",
                 desc="Breaks his back in three places in the October 4 crash that killed the pilot "
                      "and paralyzed Johnny Valentine. Told he will never wrestle again at 26; "
                      "returns within months, rebuilt as a different kind of wrestler."),
            dict(year="1981", title="First NWA World Championship",
                 desc="Beats Dusty Rhodes in Kansas City on September 17, Lou Thesz refereeing. The "
                      "decade of the touring champion begins."),
            dict(year="1983", title="Starrcade is built around him",
                 desc="Takes the title from Harley Race in the Starrcade '83 steel cage on November "
                      "24 — the flagship event exists to crown him."),
            dict(year="1985", title="The Four Horsemen form",
                 desc="With Arn and Ole Anderson and Tully Blanchard — the modern stable is "
                      "invented around his title."),
            dict(year="1989", title="The greatest year anyone has had",
                 desc="The Steamboat trilogy (February 20, April 2, May 7) and the Funk I Quit "
                      "match (November 15) in a single calendar year — the peak of the American "
                      "in-ring canon."),
            dict(year="1992", title="WWF Champion",
                 desc="Wins the Royal Rumble on January 19 from the No. 3 spot for the vacant "
                      "title, trades it with Randy Savage through the year."),
            dict(year="1994", title="The torch passed at the Beach",
                 desc="Loses the unification match to Hulk Hogan at Bash at the Beach on July 17 — "
                      "Hogan's first WCW match."),
            dict(year="2008", title="The WrestleMania farewell",
                 desc="Loses the career-threatening match to Shawn Michaels at WrestleMania XXIV on "
                      "March 30, the night after his first Hall of Fame induction. The retirement "
                      "lasts until 2009."),
            dict(year="2012", title="First two-time Hall of Famer",
                 desc="Inducted again with the Four Horsemen, having wrestled his last TNA matches "
                      "in 2011."),
            dict(year="2017", title="The health collapse",
                 desc="A medically induced coma and surgery, chronicled in ESPN's 30 for 30 "
                      "'Nature Boy' that November. He survives it and keeps showing up."),
            dict(year="2022", title="The Last Match",
                 desc="July 31, Nashville, at 73: he and Andrade El Idolo beat Jeff Jarrett and Jay "
                      "Lethal at the Starrcast event run as Jim Crockett Promotions. This "
                      "retirement holds."),
            dict(year="2026", title="Mazurki Award, by video",
                 desc="At 77, accepts the Cauliflower Alley Club's Iron Mike Mazurki Award remotely "
                      "on August 26 — a blood clot in his leg limits long travel — with Jerry "
                      "Lawler presenting and Jimmy Hart on stage."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with — a list that is really a history of two decades of main events.",
        cards=[
            dict(name="Ricky Steamboat",
                 desc="The purest rivalry in American wrestling: perfect heel against perfect "
                      "babyface, run in the Mid-Atlantic in the late 1970s and perfected in the "
                      "1989 trilogy — Chi-Town Rumble, the Clash VI two-of-three-falls, WrestleWar. "
                      "All three are canon; the series has been the workrate benchmark for every "
                      "generation since."),
            dict(name="Dusty Rhodes",
                 desc="The bleached-blond aristocrat against the son of a plumber — the NWA's "
                      "defining class war. Flair won his first world title against Dusty in 1981, "
                      "and the Horsemen's on-screen breaking of Dusty's hand and leg gave the "
                      "territory era its most famous angles, and wrestling the term "
                      "&ldquo;Hard Times.&rdquo;"),
            dict(name="Harley Race",
                 desc="The champion he had to take it from twice — most famously in the Starrcade "
                      "'83 cage on November 24, 1983, after Race put a $25,000 bounty on his head. "
                      "The passing of the NWA torch, staged as such."),
            dict(name="Terry Funk",
                 desc="Funk attacked him after WrestleWar 1989 and piledrove him through a table; "
                      "the I Quit match at Clash IX on November 15, 1989 is the best-blood-feud "
                      "payoff of its decade, and the rare Flair program built on hatred rather "
                      "than the belt."),
            dict(name="Randy Savage", slug="randy-savage",
                 desc="The 1992 WWF program — Flair's fabricated claim of a past with Miss "
                      "Elizabeth, doctored photos and all — put the title on Savage at WrestleMania "
                      "VIII on April 5 and back on Flair at the September 1 Hershey taping. They "
                      "ran it back across WCW's mid-1990s."),
            dict(name="Hulk Hogan", slug="hulk-hogan",
                 desc="The match the WWF sat on in 1992 finally happened in WCW: Hogan took Flair's "
                      "title at Bash at the Beach on July 17, 1994, and the two traded main events "
                      "through the Nitro era — the wars of the 1980s' two defining champions, "
                      "fought a decade late."),
            dict(name="Shawn Michaels",
                 desc="One match, but the one everyone remembers: WrestleMania XXIV, March 30, "
                      "2008, career on the line — 'I'm sorry, I love you,' superkick, and the most "
                      "protected retirement the company has staged. That it did not stick is part "
                      "of the Flair story too."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Culture",
        lead="The rare wrestler whose catchphrase economy crossed entirely out of wrestling.",
        rows=[
            dict(when="2004", title="To Be the Man", kind="Book",
                 desc="The autobiography, a bestseller whose title is the front half of his own "
                      "law: to be the man, you gotta beat the man."),
            dict(when="2017", title="Nature Boy — ESPN 30 for 30", kind="Film",
                 desc="The unsparing documentary, filmed around his 2017 health collapse, that "
                      "fixed the public account of both the career and its costs."),
            dict(when="2018", title="&ldquo;Ric Flair Drip&rdquo;", kind="Music",
                 desc="Offset and Metro Boomin's hit built on his name and 'Woooo!' — the moment "
                      "the persona finished crossing into hip-hop vocabulary, where it had been "
                      "circulating for years."),
            dict(when="2022&ndash;", title="Woooo! Energy &amp; endorsements", kind="Business",
                 desc="The energy-drink brand and the licensing economy around the strut, the robes "
                      "and the catchphrases."),
            dict(when="2005&ndash;", title="WWE 2K series", kind="Game",
                 desc="A playable legend across generations of WWE games."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated with the disputes attached &mdash; starting with the only number "
             "about him anyone argues over.",
        stats=[
            ("16", "Recognized world reigns"),
            ("21", "Most agreed count"),
            ("2",  "Hall of Fame inductions"),
        ],
        rows=[
            dict(name="16 recognized world championship reigns — and a real dispute above that",
                 sub="WWE recognizes 16, commonly broken out as eight NWA, six WCW and two WWF "
                     "reigns. Flair himself claims 21, which Wikipedia calls the most agreed-upon "
                     "figure, and counts in the literature run to 25 — the gaps come from reigns "
                     "the NWA later struck from its records and short changes overseas. This site "
                     "publishes the recognized number and the dispute together, because that is "
                     "the honest state of the sources."),
            dict(name="First two-time WWE Hall of Fame inductee",
                 sub="2008 individually — the night before the WrestleMania XXIV farewell — and "
                     "2012 with the Four Horsemen."),
            dict(name="The 1992 Royal Rumble performance",
                 sub="Entered No. 3, survived roughly an hour, and won the vacant WWF Championship "
                     "on January 19, 1992 — the only time the Rumble itself has decided the "
                     "company's top title, and still the performance every long Rumble run is "
                     "measured against."),
            dict(name="The 1989 year",
                 sub="The Steamboat trilogy (February 20, April 2, May 7) plus the Funk I Quit "
                     "match (November 15) — four matches from one calendar year permanently "
                     "lodged in the American canon, with the Steamboat series' five-star Observer "
                     "ratings among the most republished in that publication's history."),
            dict(name="Came back from a broken back to a 50-year career",
                 sub="The October 4, 1975 plane crash broke his back in three places at age 26; he "
                     "returned within months. His last match came on July 31, 2022 — 49 years and "
                     "seven months after his debut — and he won it, at 73."),
            dict(name="An Intercontinental Champion at 56",
                 sub="Beat Carlito at Unforgiven on September 18, 2005 — among the oldest champions "
                     "in the title's history, in the middle of the Evolution-era renaissance."),
            dict(name="Iron Mike Mazurki Award, 2026",
                 sub="The Cauliflower Alley Club's highest honor, accepted by video on August 26, "
                     "2026 — a blood clot in his leg kept him from the Las Vegas reunion — with "
                     "Jerry Lawler presenting."),
        ],
        footnote=("Two things are deliberately loose here. The world title count is presented as a "
                  "range with a recognized floor, because that is what the sources support; any "
                  "page telling you Flair is simply 'a 16-time champion' or simply 'a 21-time "
                  "champion' is choosing a side without telling you. And no career win-loss total "
                  "is published: the territory-era records to build one do not exist."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Ric_Flair"),
        dict(k="Wikipedia", v="Ric Flair's Last Match — July 31, 2022",
             href="https://en.wikipedia.org/wiki/Ric_Flair%27s_Last_Match"),
        dict(k="Slam Wrestling", v="August 2026: dealing with health problems",
             href="https://slamwrestling.net/news/ric-flair-reveals-he-is-currently-dealing-with-health-problems/"),
        dict(k="F4WOnline", v="Blood clot kept him from the Cauliflower Alley Club reunion",
             href="https://www.f4wonline.com/news/aew/medical-issue-caused-ric-flair-to-miss-cauliflower-alley-club-reunion/"),
        dict(k="Wikipedia", v="Bash at the Beach 1994 — the Hogan unification loss",
             href="https://en.wikipedia.org/wiki/Bash_at_the_Beach_(1994)"),
        dict(k="WWE.com", v="Superstar profile", href="https://www.wwe.com/superstars/ric-flair"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Ric Flair a 16-time or 21-time world champion?",
            a="Both numbers are defensible, which is why this page carries the dispute rather than "
              "picking silently. <b>WWE recognizes 16 reigns</b> &mdash; commonly split as eight "
              "NWA, six WCW and two WWF. <b>Flair himself claims 21</b>, which Wikipedia describes "
              "as the most agreed-upon count, and some tallies reach 25 by including reigns the "
              "NWA later struck from its records and brief overseas changes. The recognized 16 is "
              "the floor every source accepts; everything above it depends on whose record book "
              "you trust.",
            q_ld="Is Ric Flair a 16-time or a 21-time world champion?",
            a_ld="Both figures are in circulation. WWE officially recognizes Ric Flair as a 16-time "
                 "world champion, commonly broken down as eight NWA World Heavyweight, six WCW "
                 "World Heavyweight and two WWF Championship reigns. Flair himself claims 21 "
                 "reigns, which is the most widely agreed alternative count, and some sources "
                 "count as many as 25 by including title changes later struck from official "
                 "records. The number 16 is the recognized minimum that all sources accept."),
        dict(
            q="Is Ric Flair still alive, and what is his status in 2026?",
            a="Yes &mdash; he is 77 and retired from the ring. As of late August 2026 he is "
              "managing a <b>blood clot in his leg</b> that he says prevents five- and six-hour "
              "trips; it kept him from traveling to the Cauliflower Alley Club reunion in Las "
              "Vegas, where he accepted the Iron Mike Mazurki Award by video on August 26, 2026, "
              "with Jerry Lawler presenting. He reports otherwise feeling well. He has held a "
              "legends-role deal with AEW since 2023 and seconded Sting&rsquo;s retirement match "
              "at Revolution in March 2024.",
            q_ld="Is Ric Flair still alive, and what is his current status?",
            a_ld="Yes. As of August 2026 Ric Flair is 77 years old and retired from wrestling. He "
                 "disclosed in August 2026 that a blood clot in his leg prevents him from making "
                 "long trips, which caused him to miss the Cauliflower Alley Club reunion in Las "
                 "Vegas; he accepted its Iron Mike Mazurki Award by video on August 26, 2026. He "
                 "otherwise reports feeling well, holds a legends role with All Elite Wrestling, "
                 "and appeared in Sting's corner for Sting's retirement match in March 2024."),
        dict(
            q="When was Ric Flair&rsquo;s actual last match?",
            a="July 31, 2022, at 73 &mdash; not WrestleMania XXIV. The 2008 Shawn Michaels match "
              "was staged and honored as the retirement, but he returned in TNA by 2009 and "
              "wrestled there into 2011. The real ending was <b>Ric Flair's Last Match</b> in "
              "Nashville, a Starrcast event run under the revived Jim Crockett Promotions banner, "
              "where he and Andrade El Idolo beat Jeff Jarrett and Jay Lethal &mdash; Flair "
              "winning with a figure-four after brass knuckles reached him from ringside.",
            q_ld="When was Ric Flair's last match?",
            a_ld="Ric Flair's final match took place on July 31, 2022, at the Nashville Municipal "
                 "Auditorium, at an event called Ric Flair's Last Match, when he was 73. Teaming "
                 "with his son-in-law Andrade El Idolo, Flair defeated Jeff Jarrett and Jay "
                 "Lethal. His earlier retirement match, a loss to Shawn Michaels at WrestleMania "
                 "XXIV on March 30, 2008, did not prove final, as he returned to wrestle for TNA "
                 "between 2009 and 2011."),
        dict(
            q="What happened in the 1975 plane crash?",
            a="On October 4, 1975, a chartered plane carrying several Mid-Atlantic wrestlers "
              "crashed, killing the pilot and paralyzing Johnny Valentine. Flair, 26, broke his "
              "back in three places and was told he would never wrestle again. He was back in "
              "months &mdash; having remade himself from a 300-pound brawler into the conditioned, "
              "chop-and-figure-four stylist the rest of the career was built on. Every history of "
              "him treats the crash as the hinge.",
            q_ld="What happened to Ric Flair in the 1975 plane crash?",
            a_ld="On October 4, 1975, a small plane carrying Ric Flair and several other "
                 "Mid-Atlantic wrestlers crashed, killing the pilot and paralyzing wrestler Johnny "
                 "Valentine. Flair, then 26, broke his back in three places and was told he would "
                 "never wrestle again. He returned to the ring within months and rebuilt his "
                 "wrestling style around conditioning and technical work, which shaped the rest "
                 "of his fifty-year career."),
        dict(
            q="What are the essential Ric Flair matches?",
            a="Start with 1989: the Ricky Steamboat trilogy &mdash; Chi-Town Rumble (February 20), "
              "the Clash VI best-of-three-falls (April 2) and WrestleWar (May 7) &mdash; then the "
              "Terry Funk I Quit match at Clash IX (November 15). Add the Starrcade '83 cage win "
              "over Harley Race, the 1992 Royal Rumble hour, and the WrestleMania XXIV farewell "
              "against Shawn Michaels for the arc of the whole career.",
            q_ld="What are Ric Flair's most essential matches?",
            a_ld="Ric Flair's most acclaimed matches include the 1989 trilogy against Ricky "
                 "Steamboat at Chi-Town Rumble on February 20, Clash of the Champions VI on April "
                 "2 and WrestleWar on May 7; the I Quit match against Terry Funk at Clash of the "
                 "Champions IX on November 15, 1989; the steel cage victory over Harley Race at "
                 "Starrcade on November 24, 1983; his 1992 Royal Rumble win from the No. 3 "
                 "position; and the retirement match against Shawn Michaels at WrestleMania XXIV "
                 "on March 30, 2008."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Richard Morgan Fliehr",
             sub="adopted in Memphis, 1949, amid the Tennessee Children&rsquo;s Home Society scandal"),
        dict(label="Born", value="February 25, 1949", sub="Memphis, Tennessee &middot; age 77"),
        dict(label="Billed from", value="Charlotte, North Carolina"),
        dict(label="Height", value="6&#8242;1&#8243;", sub="185 cm"),
        dict(label="Weight", value="243 lb", sub="110 kg (billed)"),
        dict(label="Debut", value="December 10, 1972", sub="Rice Lake, Wisconsin"),
        dict(label="Trained by", value="Verne Gagne"),
        dict(label="Last match", value="July 31, 2022",
             sub="Ric Flair&rsquo;s Last Match, Nashville, at 73 &mdash; a win"),
        dict(label="Signature", value="Figure-four leglock &middot; Knife-edge chops &middot; The Flair Flop",
             sub="and the low blow, the eye poke and the trunks &mdash; the dirtiest player&rsquo;s kit"),
        dict(label="Catchphrase", value="Woooo!",
             sub="&ldquo;To be the man, you gotta beat the man&rdquo;"),
        dict(label="Family", value="Father of Charlotte Flair and the late Reid Fliehr",
             sub="Andrade El Idolo, his 2022 tag partner, is his son-in-law"),
        dict(label="Hall of Fame", value="2008 &middot; 2012 (Four Horsemen)",
             sub="the first two-time inductee"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1949-02-25",
    bornplace="Memphis, Tennessee",
    nationality="United States",
    height_cm=185,
    weight_kg=110,
    ld=dict(
        alternateName=["Richard Morgan Fliehr", "The Nature Boy", "Naitch",
                       "The Dirtiest Player in the Game"],
        award=["NWA World Heavyweight Championship (8 recognized reigns)",
               "WCW World Heavyweight Championship (6 recognized reigns)",
               "WWF Championship (2 reigns)",
               "WWE Intercontinental Championship (1 reign, 2005)",
               "Royal Rumble winner (1992)",
               "WWE Hall of Fame (2008, individually; 2012, with the Four Horsemen)",
               "Cauliflower Alley Club Iron Mike Mazurki Award (2026)"],
        knowsAbout=["Professional wrestling", "NWA", "The Four Horsemen", "WCW", "WWE",
                    "Jim Crockett Promotions", "Championship wrestling"],
        description="Ric Flair, born Richard Morgan Fliehr, is an American retired professional "
                    "wrestler recognized by WWE as a 16-time world champion, a count he himself "
                    "puts at 21. He won his first NWA World Heavyweight Championship from Dusty "
                    "Rhodes on September 17, 1981, headlined the first Starrcade against Harley "
                    "Race in 1983, wrestled the acclaimed 1989 trilogy against Ricky Steamboat, "
                    "won the 1992 Royal Rumble for the vacant WWF Championship from the No. 3 "
                    "entry, and wrestled his final match on July 31, 2022 at age 73. He is a "
                    "two-time WWE Hall of Fame inductee.",
        sameAs=["https://en.wikipedia.org/wiki/Ric_Flair",
                "https://www.wwe.com/superstars/ric-flair"],
    ),
)
