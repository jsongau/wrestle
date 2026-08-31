# -*- coding: utf-8 -*-
"""Sheamus - dossier data.

Sources: web research compiled August 31, 2026 - Wikipedia (Sheamus), WWE.com (official
profile, opened August 31, 2026), POST Wrestling (July 5 and July 19, 2026 contract
reports), NoDQ (April 2026 Off The Ball interview). Day-precision dates come from those
sources.

Deliberate omissions and flags:
  * His WWE status is REPORTED, not announced. Fightful Select (via POST Wrestling)
    reported he rejected a restructured extension and that his contract runs to October
    1, 2026; he posted an Irish-language goodbye on July 10 and his social accounts now
    read "S. Farrelly." Neither WWE nor Sheamus has confirmed the departure on the
    record, and his WWE.com profile still read as an active-superstar page when opened
    for this file. The page prints the reporting as reporting.
  * No social links: his handles were renamed and de-branded in July 2026, and no
    current official handle is verified.
  * No career win-loss total: none verified.
  * His WWE signing year is a live conflict - Wikipedia has him joining developmental
    (FCW) in October 2007; POST Wrestling's exit report says he signed in 2006. Both
    are printed, neither adopted as the single truth.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2009-12-13", promo="WWE", landmark=True,
         event="TLC: Tables, Ladders & Chairs", opponent="John Cena",
         stip="Tables match — first Irish-born WWE Champion, 166 days after his main-roster debut",
         title="WWE Championship"),
    dict(result="W", date="2010-06-20", promo="WWE", type="tag", landmark=True,
         event="Fatal 4-Way", opponent="John Cena, Randy Orton & Edge",
         stip="Fatal four-way — becomes the 100th WWE Champion",
         title="WWE Championship"),
    dict(result="W", date="2012-01-29", promo="WWE", type="tag", landmark=True,
         event="Royal Rumble", opponent="The 2012 Royal Rumble field",
         stip="Wins the Rumble, last eliminating Chris Jericho", title=""),
    dict(result="W", date="2012-04-01", promo="WWE", landmark=True,
         event="WrestleMania XXVIII", opponent="Daniel Bryan",
         stip="Singles — wins in 18 seconds with a Brogue Kick",
         title="World Heavyweight Championship"),
    dict(result="L", date="2012-10-28", promo="WWE", landmark=True,
         event="Hell in a Cell", opponent="Big Show",
         stip="Singles — the 210-day reign ends",
         title="World Heavyweight Championship"),
    dict(result="W", date="2015-06-14", promo="WWE", type="tag",
         event="Money in the Bank", opponent="The 2015 ladder-match field",
         stip="Money in the Bank ladder match — wins the contract", title=""),
    dict(result="W", date="2015-11-22", promo="WWE", landmark=True,
         event="Survivor Series", opponent="Roman Reigns",
         stip="Money in the Bank cash-in, minutes after Reigns won the vacant title",
         title="WWE Championship"),
    dict(result="W", date="2016-12-18", promo="WWE", type="tag", landmark=True,
         event="Roadblock: End of the Line", opponent="The New Day",
         stip="Tag, with Cesaro — ends the record 483-day reign",
         title="Raw Tag Team Championship"),
    dict(result="L", date="2022-09-03", promo="WWE", landmark=True,
         event="Clash at the Castle — Cardiff", opponent="Gunther",
         stip="Singles — five stars (Meltzer); loses the match, leaves to a standing ovation",
         title="WWE Intercontinental Championship"),
    dict(result="W", date="2024-04-15", promo="WWE",
         event="Raw", opponent="Ivar",
         stip="Singles — the return after eight months out", title=""),
    dict(result="W", date="2024-10-07", promo="WWE",
         event="Raw", opponent="Pete Dunne",
         stip="Good Old Fashioned Donnybrook match", title=""),
    dict(result="L", date="2024-11-30", promo="WWE", type="tag",
         event="Survivor Series: WarGames", opponent="Bron Breakker & Ludwig Kaiser",
         stip="Triple threat — Breakker retains; the Intercontinental gap stays open",
         title="WWE Intercontinental Championship"),
    dict(result="L", date="2025-08-31", promo="WWE",
         event="Clash in Paris", opponent="Rusev",
         stip="Good Old Fashioned Donnybrook match — worked on the failing shoulder", title=""),
    dict(result="W", date="2025-11-10", promo="WWE",
         event="Raw", opponent="Shinsuke Nakamura",
         stip="The Last Time Is Now tournament, first round", title=""),
    dict(result="W", date="2025-11-17", promo="WWE", type="tag", landmark=True,
         event="Raw", opponent="Dominik Mysterio, Finn Balor & JD McDonagh",
         stip="Six-man tag with John Cena & Rey Mysterio — Cena's final Raw, and, to date, "
              "Sheamus' final WWE match", title=""),
]

DATA = dict(
    slug="sheamus",
    name="Sheamus",
    realname="Stephen Farrelly",
    epithet="The Celtic Warrior",
    hook="Record & Titles",

    meta_desc=("Sheamus, The Celtic Warrior, is a four-time world champion, 2012 Royal Rumble "
               "winner and the first Irish-born WWE Champion - reported to be leaving WWE in "
               "2026 with the Intercontinental Championship still unwon. Full record, titles "
               "and career."),
    og_desc=("The Celtic Warrior: four world titles, the 2012 Royal Rumble, King of the Ring, "
             "Money in the Bank, an 18-second WrestleMania win - and a reported 2026 WWE exit "
             "with one belt forever missing."),
    tw_desc="Four world titles, the 2012 Rumble, 18 seconds at WrestleMania - and no Intercontinental title, ever.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2002",
    height_imp="6&#8242;3&#8243;",
    weight_lb="267",
    world_titles="4",
    vitals_tagline="Laoch",
    support_note="Merch &middot; Watch &middot; Train",
    sp_items=[
        dict(ic="SH", title="WWE Shop", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="CW", title="Celtic Warrior Workouts", sub="His long-running fitness channel",
             tag="Watch", href="https://www.youtube.com/"),
        dict(ic="RS", title="TMNT: Out of the Shadows", sub="As Rocksteady, 2016",
             tag="Watch", href="https://en.wikipedia.org/wiki/Teenage_Mutant_Ninja_Turtles:_Out_of_the_Shadows"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/sheamus"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Celtic Warrior &middot; The Irish Curse &middot; the Fella",
    hero_tag="Cabra, Dublin, Ireland &middot; <em>Independents &middot; FCW &middot; WWE "
             "&middot; 2002&ndash;2026(?)</em>",
    now_label="NOW",
    now_bold="Off WWE television; reported to be leaving",
    now_tail=" &middot; last match November 17, 2025; contract reported to run to October 1, "
             "2026; a goodbye posted in Irish on July 10 &mdash; and nothing confirmed on the "
             "record by either side",
    hstats=[
        dict(value="4",   x=True,  label="World Titles"),
        dict(value="18",  x=False, label="Seconds at WM XXVIII"),
        dict(value="210", x=False, label="Day WHC Reign"),
        dict(value="0",   x=False, label="IC Title Reigns"),
    ],
    ghost_link="From Cabra to the 18-second WrestleMania main-card win",
    vlabel="Est. 2002 &middot; Dublin, Ireland",
    mono="SH",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Sheamus</b> is one of the most decorated wrestlers of his generation and, as of "
        "August 31, 2026, a career that appears to be ending in the passive voice. He is a "
        "four-time world champion &mdash; three WWE Championships and a World Heavyweight "
        "Championship &mdash; the first Irish-born WWE Champion in history, the 2012 Royal "
        "Rumble winner, the 2010 King of the Ring, the 2015 Money in the Bank winner, a "
        "three-time United States Champion and a five-time tag team champion with Cesaro as "
        "The Bar. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">4</span>'
        '<span class="pull-cap">world championship reigns &mdash; and with Edge, one of only two men to win King of the Ring, the Royal Rumble and Money in the Bank</span></span>'
        "He has not wrestled since November 17, 2025. He has not, per the reporting, re-signed "
        "with WWE. And he has never won the Intercontinental Championship, which is somehow "
        "the fact that organises everything else on this page.",

        "Set the status straight first, because nothing about it is official. What is on the "
        "record: his last match was the <b>November 17, 2025</b> Raw &mdash; a six-man tag "
        "alongside John Cena and Rey Mysterio, on Cena&rsquo;s final Raw &mdash; followed by "
        "shoulder surgery in December. What is reported, by Fightful Select via POST "
        "Wrestling: WWE offered a restructured contract extension, he turned it down "
        "quickly, and his deal runs to <b>October 1, 2026</b>. What he did in public: on "
        "July 10, 2026 he renamed his social accounts &ldquo;S. Farrelly,&rdquo; stripped "
        "the WWE references and posted a goodbye to his WWE friends in Irish. What has NOT "
        "happened: any confirmation from WWE or from Sheamus himself &mdash; and his "
        "WWE.com profile still read as an active-superstar page, not an alumni page, when "
        "it was opened for this file on August 31. POST reported an alumni-section move in "
        "July; the live page disagrees. This dossier prints the conflict rather than "
        "declaring him gone.",

        "He was born Stephen Farrelly on January 28, 1978 in Cabra, Dublin &mdash; a "
        "Gaelic footballer, a rugby player, a choirboy in the Palestrina Choir until "
        "thirteen, and at times a bodyguard for Bono and Larry Mullen Jr. before Larry "
        "Sharpe&rsquo;s Monster Factory trained him in 2002. A botched hip toss in one of "
        "his first matches broke his neck and cost him two years. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">166</span>'
        '<span class="pull-cap">days from main-roster debut to WWE Champion &mdash; the fastest rise to the title of its era</span></span>'
        "He worked the European independents as Sheamus O&rsquo;Shaunessy, joined "
        "WWE&rsquo;s developmental system &mdash; Wikipedia dates the FCW arrival to "
        "October 2007, POST Wrestling&rsquo;s exit report says he signed in 2006, and both "
        "versions are printed here &mdash; debuted on ECW in June 2009, and by December 13, "
        "2009 had put John Cena through a table at TLC to win the WWE Championship 166 days "
        "into his main-roster run. The 2012 peak followed: the Royal Rumble win, then the "
        "18-second Brogue Kick that beat Daniel Bryan for the World Heavyweight "
        "Championship at WrestleMania XXVIII &mdash; a finish so despised by the crowd it "
        "accidentally launched the Yes Movement &mdash; and a 210-day reign, the "
        "third-longest in that title&rsquo;s history.",

        "The last act made him beloved in a way the championships never quite did. The "
        "2022 Brawling Brutes run produced the Clash at the Castle match with Gunther on "
        "September 3, 2022 &mdash; five stars from Dave Meltzer, a standing ovation in "
        "defeat &mdash; and a series of &ldquo;bangers,&rdquo; his word, that turned the "
        "chase for the one title he has never held into the defining story of his late "
        "career. It never closed. The Intercontinental Championship &mdash; the only "
        "thing between him and a Grand Slam &mdash; survived Gunther in Cardiff, survived "
        "the Breakker-Kaiser triple threat at Survivor Series: WarGames in 2024, and "
        "survived him. A shoulder that began failing in mid-2025, by his own account to "
        "Off The Ball, was worked through the Rusev Donnybrook at Clash in Paris on "
        "August 31, 2025, and gave out for good after the Cena farewell tag; surgery "
        "followed on December 30, 2025. &ldquo;I&rsquo;m dying to get back in that "
        "ring,&rdquo; he said in April 2026. The reporting since suggests the ring he "
        "gets back into will not be WWE&rsquo;s.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("4&times;", "World titles"),
            ("2012",     "Royal Rumble"),
            ("2010",     "King of the Ring"),
            ("2015",     "Money in the Bank"),
            ("3&times;", "US Championship"),
            ("5&times;", "Tag titles with Cesaro"),
        ],
        lead=("Fifteen documented bouts from a 24-year career &mdash; the four world title "
              "wins, the 18 seconds, the Cardiff five-star loss, and the November 17, 2025 "
              "six-man tag that stands, as of this writing, as his final WWE match. A "
              "curated ledger, not a career count; no verified win&ndash;loss total exists "
              "and none is published. Filter by match type, tap any column header to sort, "
              "and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The two matches with verified five-star ratings, both against the same "
                    "man, both losses &mdash; which tells you what the late-career story "
                    "was. Dave Meltzer&rsquo;s ratings as recorded on the Gunther dossier "
                    "on this site; no other Observer ratings for his matches were verified "
                    "in this pass."),
    signature=[
        dict(rating="5.0", event="Clash at the Castle 2022 — Cardiff", opponent="Gunther",
             stip="WWE Intercontinental Championship — standing ovation in defeat"),
        dict(rating="5.0", event="WrestleMania 39", opponent="Gunther & Drew McIntyre",
             stip="Intercontinental Championship — triple threat"),
    ],
    signature_count_word="two",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("4&times;", "World title reigns"),
            ("3&times;", "US Championship"),
            ("5&times;", "Tag team titles"),
            ("0",        "Intercontinental — the gap"),
        ],
        lead=("Nine championships across every tier WWE has &mdash; except one. The "
              "Intercontinental Championship is the single title missing from a Grand "
              "Slam, chased explicitly from 2022 to 2024 and never won."),
        rows=[
            dict(ic="W", name="WWE Championship", count="3",
                 sub="2009&ndash;10 &middot; def. John Cena in a tables match at TLC on "
                     "December 13, 2009 &mdash; the first Irish-born WWE Champion &mdash; "
                     "lost at Elimination Chamber in February &middot; 2010 &middot; won "
                     "the June 20 fatal four-way to become the 100th WWE Champion, lost to "
                     "Randy Orton in September &middot; 2015 &middot; cashed in Money in "
                     "the Bank on Roman Reigns at Survivor Series on November 22, minutes "
                     "after Reigns won the vacant title; Reigns took it back that December"),
            dict(ic="H", name="World Heavyweight Championship", count="1",
                 sub="April 1 &ndash; October 28, 2012 &middot; won from Daniel Bryan in 18 "
                     "seconds at WrestleMania XXVIII, lost to Big Show at Hell in a Cell "
                     "&middot; <b>210 days</b> &mdash; the third-longest reign in the "
                     "title&rsquo;s 2002&ndash;13 history, per Wikipedia"),
            dict(ic="U", name="WWE United States Championship", count="3",
                 sub="2011 &middot; def. Daniel Bryan on March 14 &middot; 2014 &middot; "
                     "won a 20-man battle royal on May 5 &middot; 2021 &middot; def. Matt "
                     "Riddle at WrestleMania 37 on April 11, lost to Damian Priest at "
                     "SummerSlam on August 21 &mdash; 132 days"),
            dict(ic="R", name="Raw Tag Team Championship", count="4",
                 sub="All with Cesaro as The Bar &middot; first won December 18, 2016 at "
                     "Roadblock: End of the Line, ending The New Day&rsquo;s record "
                     "483-day reign &middot; the fourth reign ended at WrestleMania 34 "
                     "against Braun Strowman and ten-year-old Nicholas &mdash; the "
                     "youngest champion in WWE history, at their expense"),
            dict(ic="S", name="SmackDown Tag Team Championship", count="1",
                 sub="October 16, 2018 &middot; won on the SmackDown 1000 special with "
                     "Cesaro, held into January 2019"),
            dict(ic="K", name="King of the Ring", count="2010",
                 sub="Won the November 29, 2010 final &middot; with the 2012 Royal Rumble "
                     "and 2015 Money in the Bank, he and Edge are the only men to hold all "
                     "three crowns, per Wikipedia"),
            dict(ic="I", name="WWE Intercontinental Championship", count="0",
                 sub="Never won, and not for lack of trying: Gunther at Clash at the "
                     "Castle 2022 and WrestleMania 39, Bron Breakker and Ludwig Kaiser at "
                     "Survivor Series: WarGames 2024, and more between. The missing Grand "
                     "Slam piece &mdash; printed here as a title row because its absence "
                     "is the most-discussed championship fact of his career"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Three units across three eras &mdash; a villain cartel, a bar, and a fight "
             "club.",
        cards=[
            dict(era="WWE &middot; 2015&ndash;16",
                 name="The League of Nations",
                 members="Sheamus, Alberto Del Rio, Rusev, King Barrett",
                 desc="The multinational heel bloc assembled around his third WWE "
                      "Championship reign after the Survivor Series 2015 cash-in. "
                      "Short-lived and never especially loved, but it produced the "
                      "WrestleMania 32 program and a decade-long thread with Rusev that "
                      "was still being pulled at Clash in Paris in 2025."),
            dict(era="WWE &middot; 2016&ndash;19",
                 name="The Bar",
                 members="Sheamus, Cesaro",
                 desc="Born out of a 2016 best-of-seven series that ended 3-3 and a "
                      "forced partnership that became the era's best tag team: four Raw "
                      "Tag Team Championship reigns and a SmackDown reign, the first won "
                      "by ending The New Day's record 483-day run at Roadblock on "
                      "December 18, 2016. \"We don't just set the bar - we ARE The Bar\" "
                      "was the pitch, and for three years it held up."),
            dict(era="WWE &middot; 2021&ndash;24",
                 name="The Brawling Brutes",
                 members="Sheamus, Ridge Holland, Butch (Pete Dunne)",
                 desc="The fight-club faction of the late run, built around the "
                      "\"banger\" era — hard-hitting matches as their own reward. It gave "
                      "the Gunther series its context and ended in the best way factions "
                      "end: Butch reverted to Pete Dunne and fought Sheamus in a Good Old "
                      "Fashioned Donnybrook on October 7, 2024. Sheamus won, and declared "
                      "Butch dead afterward — affectionately."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One gimmick, deliberately mythological rather than stereotypical &mdash; he "
             "built the character on Celtic legend specifically to avoid leprechaun "
             "Irishness.",
        cards=[
            dict(mono="SOS", era="Independents &middot; 2002&ndash;07", name="Sheamus O'Shaunessy",
                 desc="The European independent run out of Larry Sharpe's Monster Factory, "
                      "interrupted almost immediately by a broken neck from a botched hip "
                      "toss that cost him two years. The name survived into film: his 2008 "
                      "acting debut in The Escapist is credited to Sheamus O'Shaunessy."),
            dict(mono="CW", era="WWE &middot; 2009&ndash;14", name="The Celtic Warrior",
                 desc="The pale destroyer built on Celtic mythology — he designed the "
                      "crossos pendant himself, a Celtic cross fused with a war sword — "
                      "who went from ECW debut to WWE Champion in under six months, then "
                      "King of the Ring, the Rumble and the 18 seconds. The Irish Curse "
                      "nickname predates the polish: it came from early low blows."),
            dict(mono="LN", era="WWE &middot; 2015&ndash;16", name="The mohawked heel",
                 desc="The \"era of underdogs is over\" reinvention: braided mohawk, "
                      "League of Nations, a Money in the Bank cash-in on Roman Reigns 5 "
                      "minutes and 15 seconds into Reigns' first reign. The least loved "
                      "version and, by title count, among the most effective."),
            dict(mono="BB", era="WWE &middot; 2021&ndash;25", name="The banger merchant",
                 desc="The late-career face run in which the matches themselves became the "
                      "character: the Brawling Brutes, the Donnybrooks, Cardiff. He spent "
                      "it openly chasing the Intercontinental Championship as legacy "
                      "business and never caught it — the sympathetic engine of everything "
                      "written about him since."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Cabra to Cardiff, with a reported quiet ending.",
        rows=[
            dict(year="2002", title="Monster Factory, and a broken neck",
                 desc="Trains under Larry Sharpe from April 2002; debuts in May; a botched "
                      "hip toss breaks his neck and costs him roughly two years."),
            dict(year="2007", title="WWE developmental",
                 desc="Joins Florida Championship Wrestling — October 2007 per Wikipedia; "
                      "POST Wrestling's 2026 exit report says he signed in 2006. Both "
                      "versions are printed here."),
            dict(year="2009", title="The fastest rise of the era",
                 desc="Debuts on ECW June 30, moves to Raw in October, and beats John Cena "
                      "in a tables match at TLC on December 13 — WWE Champion 166 days "
                      "into his main-roster run, and the first Irish-born WWE Champion."),
            dict(year="2010", title="100th champion, King of the Ring",
                 desc="Wins the WWE Championship again in the June 20 fatal four-way, "
                      "becoming the 100th champion in the title's history, and takes King "
                      "of the Ring on November 29."),
            dict(year="2012", title="The Rumble, and 18 seconds",
                 desc="Wins the Royal Rumble on January 29, then beats Daniel Bryan in 18 "
                      "seconds at WrestleMania XXVIII for the World Heavyweight "
                      "Championship — a finish that accidentally births the Yes Movement — "
                      "and holds it 210 days."),
            dict(year="2015", title="Money in the Bank, and the cash-in",
                 desc="Wins the ladder match on June 14 and cashes in on Roman Reigns at "
                      "Survivor Series on November 22, minutes after Reigns wins the "
                      "vacant title."),
            dict(year="2016", title="The Bar begins",
                 desc="A best-of-seven with Cesaro ends 3-3; the forced team wins the Raw "
                      "Tag titles at Roadblock on December 18, ending The New Day's "
                      "record reign. Four Raw reigns and a SmackDown reign follow."),
            dict(year="2022", title="Cardiff",
                 desc="The Brawling Brutes era peaks at Clash at the Castle on September "
                      "3: five stars against Gunther, a standing ovation in defeat, and "
                      "the Intercontinental chase that will define the rest of the run."),
            dict(year="2024", title="Return, Donnybrook, and the gap unclosed",
                 desc="Returns April 15 to beat Ivar; beats Pete Dunne in the October 7 "
                      "Donnybrook; loses the Intercontinental triple threat at Survivor "
                      "Series: WarGames on November 30 to champion Bron Breakker."),
            dict(year="2025", title="The shoulder, and the Cena farewell",
                 desc="Returns in May; loses the Clash in Paris Donnybrook to Rusev on "
                      "August 31 on a failing shoulder; beats Nakamura in the Last Time Is "
                      "Now tournament on November 10; teams with John Cena and Rey "
                      "Mysterio on November 17 — his last match to date — and has shoulder "
                      "surgery December 30."),
            dict(year="2026", title="The reported goodbye",
                 desc="Rejects a restructured extension per Fightful Select; renames his "
                      "social accounts S. Farrelly and posts an Irish-language farewell "
                      "on July 10; contract reported to run to October 1. Nothing "
                      "confirmed on the record by either side as of August 31."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Gunther",
                 desc="The defining opponent of the final act. Cardiff on September 3, "
                      "2022 — five stars, a standing ovation, and the loss that made him "
                      "more beloved than any win had — then the WrestleMania 39 triple "
                      "threat with Drew McIntyre, also rated five stars. Gunther's own "
                      "dossier on this site treats the series as the proof that a "
                      "chop-based, credibility-first match could headline. Sheamus never "
                      "took the title from him."),
            dict(name="John Cena",
                 desc="The career-maker: the tables match at TLC on December 13, 2009 made "
                      "Sheamus WWE Champion 166 days into his main-roster run, and Cena "
                      "programs recurred through 2010. Fittingly, Sheamus' last WWE match "
                      "to date — November 17, 2025 — was at Cena's side, on Cena's final "
                      "Raw."),
            dict(name="Daniel Bryan",
                 desc="Eighteen seconds at WrestleMania XXVIII on April 1, 2012 — the most "
                      "infamous world title match of its decade. The crowd's fury at "
                      "Bryan's instant loss became the Yes Movement; Sheamus, the winner, "
                      "spent years as the era's accidental heel in retrospect. They had "
                      "traded the US title the year before."),
            dict(name="Cesaro",
                 desc="Rival first — a 2016 best-of-seven that ended 3-3 without a winner "
                      "— then the partner of his life as The Bar: five tag championships, "
                      "the end of The New Day's record reign, and the rare forced-team "
                      "gimmick that became genuinely great."),
            dict(name="Drew McIntyre",
                 desc="The longest thread: friends and rivals since the mid-2000s "
                      "independents, when McIntyre wrestled as Drew Galloway. WWE turned "
                      "the real friendship into a 2021 feud with No Holds Barred matches "
                      "at Fastlane, and the WrestleMania 39 triple threat put them in the "
                      "same five-star frame."),
            dict(name="Pete Dunne and Rusev",
                 desc="The Donnybrook era: the October 7, 2024 win over Dunne — his former "
                      "Brute, whose \"Butch is dead\" epitaph Sheamus delivered himself — "
                      "and the August 31, 2025 loss to Rusev at Clash in Paris, worked on "
                      "the shoulder that would end his run. Two Good Old Fashioned "
                      "Donnybrooks, one win, one loss, all bangers."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="A real filmography, a fitness channel, and one famous rhino.",
        rows=[
            dict(when="2016", title="Teenage Mutant Ninja Turtles: Out of the Shadows", kind="Film",
                 desc="Rocksteady — the mutant rhino — in a major studio release, his "
                      "biggest acting role. His actual film debut came earlier: The "
                      "Escapist (2008), credited as Sheamus O'Shaunessy."),
            dict(when="2015&ndash;", title="Celtic Warrior Workouts", kind="YouTube",
                 desc="His long-running training channel, filming workouts with wrestlers "
                      "across and beyond WWE — the most consistent out-of-ring project of "
                      "his career."),
            dict(when="2019", title="Fighting with My Family", kind="Film",
                 desc="A cameo as himself in the Paige biopic."),
            dict(when="2009&ndash;", title="WWE video games", kind="Game",
                 desc="A playable roster fixture since the SmackDown vs. Raw era through "
                      "the WWE 2K line. Never a cover star."),
            dict(when="2002&ndash;", title="Before wrestling", kind="Life",
                 desc="Palestrina Choir chorister until thirteen, Gaelic footballer for "
                      "Erin's Isle, rugby at the National College of Ireland, IT "
                      "technician, nightclub security — and occasional bodyguard for Bono "
                      "and Larry Mullen Jr. of U2, per Wikipedia."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records &mdash; and the one that is a hole rather than a number.",
        stats=[
            ("166", "Days, debut to WWE title"),
            ("18",  "Seconds at WrestleMania"),
            ("100", "th WWE Champion"),
        ],
        rows=[
            dict(name="First Irish-born WWE Champion",
                 sub="December 13, 2009, tables match, John Cena, TLC — 166 days after "
                     "his main-roster debut, the fastest rise to the WWE Championship of "
                     "its era per Wikipedia."),
            dict(name="The 100th WWE Champion",
                 sub="June 20, 2010, winning the Fatal 4-Way pay-per-view's title match "
                     "— a numbering per Wikipedia's count of the lineage."),
            dict(name="An 18-second world title win at WrestleMania",
                 sub="WrestleMania XXVIII, April 1, 2012, one Brogue Kick to Daniel "
                     "Bryan for the World Heavyweight Championship. The backlash to the "
                     "finish — not the man — helped create the Yes Movement, and the "
                     "210-day reign that followed was the third-longest in that title's "
                     "history."),
            dict(name="King of the Ring, Royal Rumble and Money in the Bank",
                 sub="2010, 2012 and 2015 — he and Edge are the only two men to win all "
                     "three, per Wikipedia. The 2015 briefcase became his third WWE "
                     "Championship via the Survivor Series cash-in on Roman Reigns."),
            dict(name="Five tag team championships with Cesaro",
                 sub="Four Raw reigns and one SmackDown reign as The Bar, the first won "
                     "by ending The New Day's record 483-day reign at Roadblock: End of "
                     "the Line on December 18, 2016."),
            dict(name="Zero Intercontinental Championships",
                 sub="The gap that keeps him off the Grand Slam list, chased explicitly "
                     "from Cardiff 2022 through the 2024 WarGames triple threat and "
                     "never closed. If the reported exit holds, it closes never — which "
                     "is why it leads half the coverage of his departure."),
            dict(name="Two five-star matches, both against Gunther's Intercontinental reign",
                 sub="Clash at the Castle 2022 and the WrestleMania 39 triple threat, "
                     "per the Meltzer ratings recorded on this site's Gunther dossier. "
                     "Both losses."),
            dict(name="A 24-year career bookended by injuries",
                 sub="A broken neck in 2002 that cost two years at the start; a shoulder "
                     "that failed through 2025 and was operated on December 30, 2025 at, "
                     "reportedly, the end. \"I'm dying to get back in that ring,\" he "
                     "told Off The Ball in April 2026."),
        ],
        footnote=("Deliberately absent: any assertion that he has left WWE — the "
                  "extension rejection, the October 1 contract date and the alumni move "
                  "are Fightful Select and POST Wrestling reporting, his July 10 "
                  "farewell post is real, and neither he nor WWE has confirmed anything "
                  "on the record; his still-active WWE.com profile is the counterweight "
                  "and both are printed. Also absent: a career win-loss total (none "
                  "verified), social links (the handles were renamed and de-branded in "
                  "July 2026), and his 2026 in-ring record, which is empty — he has not "
                  "wrestled this year."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="WWE.com", v="Official profile — still live as of August 31, 2026",
             href="https://www.wwe.com/superstars/sheamus"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Sheamus"),
        dict(k="POST Wrestling", v="July 19, 2026 — contract runs to October 1",
             href="https://www.postwrestling.com/2026/07/19/report-sheamus-remains-under-wwe-contract-until-october-1/"),
        dict(k="POST Wrestling", v="July 5, 2026 — the rejected extension",
             href="https://www.postwrestling.com/2026/07/05/report-sheamus-to-exit-wwe-after-rejecting-restructured-contract-extension/"),
        dict(k="NoDQ", v="April 2026 — the Off The Ball interview on the shoulder",
             href="https://nodq.com/news/sheamus-addresses-his-absence-from-wwe-television-in-2026/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Has Sheamus left WWE?",
            a="Reported, not confirmed &mdash; and this page is careful about the "
              "difference. Fightful Select (via POST Wrestling) reported that he "
              "<b>rejected a restructured contract extension</b> and that his deal runs "
              "to <b>October 1, 2026</b>; on July 10, 2026 he renamed his social "
              "accounts &ldquo;S. Farrelly&rdquo; and posted a goodbye to his WWE "
              "friends in Irish. But neither WWE nor Sheamus has confirmed a departure "
              "on the record, he was not released, and his WWE.com profile still read "
              "as an active-superstar page when opened for this dossier on August 31, "
              "2026 &mdash; despite a July report of an alumni-section move. He has not "
              "wrestled since November 17, 2025.",
            q_ld="Has Sheamus left WWE?",
            a_ld="It is reported but not officially confirmed. Fightful Select, via POST "
                 "Wrestling, reported that Sheamus rejected a restructured contract "
                 "extension and that his WWE contract runs until October 1, 2026. On "
                 "July 10, 2026 he renamed his social media accounts S. Farrelly and "
                 "posted a farewell to his WWE friends in the Irish language. Neither "
                 "WWE nor Sheamus has publicly confirmed his departure, and he has not "
                 "wrestled since November 17, 2025."),
        dict(
            q="Has Sheamus ever won the Intercontinental Championship?",
            a="No &mdash; and it is the most consequential zero in his record. He has "
              "won everything else: three WWE Championships, the World Heavyweight "
              "Championship, three United States titles, five tag titles, King of the "
              "Ring, the Royal Rumble and Money in the Bank. The Intercontinental "
              "Championship &mdash; the last piece of a Grand Slam &mdash; survived his "
              "entire late-career chase: the five-star Cardiff loss to Gunther in 2022, "
              "the WrestleMania 39 triple threat, the 2024 WarGames triple threat "
              "against champion Bron Breakker. If the reported exit stands, the gap is "
              "permanent.",
            q_ld="Has Sheamus ever won the WWE Intercontinental Championship?",
            a_ld="No. Sheamus has never won the WWE Intercontinental Championship, the "
                 "only major WWE title missing from his record. He is a four-time world "
                 "champion, three-time United States Champion, five-time tag team "
                 "champion, and won King of the Ring in 2010, the Royal Rumble in 2012 "
                 "and Money in the Bank in 2015, but lost his Intercontinental "
                 "Championship matches, including five-star bouts against Gunther at "
                 "Clash at the Castle 2022 and WrestleMania 39."),
        dict(
            q="What really happened in the 18-second WrestleMania match?",
            a="Exactly what it sounds like. At WrestleMania XXVIII on April 1, 2012, "
              "Sheamus &mdash; that year&rsquo;s Royal Rumble winner &mdash; beat World "
              "Heavyweight Champion Daniel Bryan with a single Brogue Kick in <b>18 "
              "seconds</b>, before the match had meaningfully begun. The crowd&rsquo;s "
              "revolt at the finish did more for Bryan than a victory would have "
              "&mdash; it fed directly into the Yes Movement &mdash; while Sheamus "
              "held the title <b>210 days</b>, the third-longest reign in that "
              "belt&rsquo;s history, per Wikipedia.",
            q_ld="What happened in Sheamus' 18-second match at WrestleMania XXVIII?",
            a_ld="At WrestleMania XXVIII on April 1, 2012, Sheamus defeated Daniel "
                 "Bryan for the World Heavyweight Championship in 18 seconds with a "
                 "single Brogue Kick. The crowd backlash to the instant finish helped "
                 "fuel the Yes Movement around Bryan, while Sheamus went on to hold the "
                 "championship for 210 days, the third-longest reign in that title's "
                 "history."),
        dict(
            q="When was Sheamus&rsquo; last match, and what was his injury?",
            a="<b>November 17, 2025</b>, on Raw: a six-man tag with John Cena and Rey "
              "Mysterio against Dominik Mysterio, Finn Balor and JD McDonagh, on "
              "Cena&rsquo;s final Raw appearance &mdash; a win. His shoulder had been "
              "failing since roughly May or June 2025 by his own account; he worked "
              "the Clash in Paris Donnybrook against Rusev through it, was pulled "
              "from the Last Time Is Now tournament, and had surgery on <b>December "
              "30, 2025</b>. &ldquo;I&rsquo;m dying to get back in that ring... "
              "I&rsquo;ve got cabin fever,&rdquo; he told Off The Ball in April 2026.",
            q_ld="When was Sheamus' last WWE match?",
            a_ld="Sheamus' most recent match was on the November 17, 2025 episode of "
                 "Raw, where he teamed with John Cena and Rey Mysterio to defeat "
                 "Dominik Mysterio, Finn Balor and JD McDonagh on Cena's final Raw "
                 "appearance. He had been working through a shoulder injury that began "
                 "in mid-2025 and underwent shoulder surgery on December 30, 2025."),
        dict(
            q="Why is he called the Celtic Warrior and not something more leprechaun?",
            a="Deliberate design. He built the character on Celtic mythology "
              "specifically to avoid stage-Irish stereotypes &mdash; no leprechauns, "
              "no lucky charms &mdash; and created the &ldquo;crossos&rdquo; pendant "
              "himself, fusing a Celtic cross with a Celtic war sword. The other "
              "nicknames came honestly: &ldquo;the Irish Curse&rdquo; from early "
              "low-blow spots, &ldquo;Fella&rdquo; from his own catchphrase, and "
              "&ldquo;Laoch&rdquo; &mdash; Irish for warrior &mdash; from a "
              "fluently Irish-speaking Dubliner who sang in the Palestrina Choir "
              "until he was thirteen.",
            q_ld="Why is Sheamus called the Celtic Warrior?",
            a_ld="Sheamus built his character on Celtic mythology deliberately to "
                 "avoid Irish stereotypes such as leprechauns. He designed his crossos "
                 "pendant himself, combining a Celtic cross with a Celtic war sword. "
                 "Born in Dublin and educated in Irish-speaking schools, he is fluent "
                 "in the Irish language and sang in the Palestrina Choir until age "
                 "thirteen."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Stephen Farrelly"),
        dict(label="Born", value="January 28, 1978", sub="Cabra, Dublin, Ireland &middot; age 48"),
        dict(label="Billed from", value="Dublin, Ireland"),
        dict(label="Height", value="6&#8242;3&#8243;", sub="191 cm &middot; per WWE.com"),
        dict(label="Weight", value="267 lb", sub="121 kg"),
        dict(label="Debut", value="May 2002",
             sub="Monster Factory-trained &middot; a broken neck cost the next two years"),
        dict(label="WWE developmental", value="FCW, October 2007",
             sub="per Wikipedia &mdash; POST Wrestling&rsquo;s exit report says signed 2006"),
        dict(label="Last match", value="November 17, 2025",
             sub="six-man tag with John Cena &amp; Rey Mysterio &middot; shoulder surgery "
                 "December 30"),
        dict(label="Finisher", value="Brogue Kick",
             sub="plus the Cloverleaf, Irish Curse backbreaker and White Noise"),
        dict(label="Contract", value="Reported through October 1, 2026",
             sub="extension reportedly declined &middot; unconfirmed by either side"),
        dict(label="Spouse", value="Isabella Revilla", sub="married 2022"),
        dict(label="Also known as",
             value="The Celtic Warrior &middot; The Irish Curse &middot; Fella &middot; "
                   "Sheamus O&rsquo;Shaunessy"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1978-01-28",
    bornplace="Cabra, Dublin, Ireland",
    nationality="Ireland",
    alumni="National College of Ireland",
    height_cm=191,
    weight_kg=121,
    ld=dict(
        alternateName=["Stephen Farrelly", "The Celtic Warrior", "Sheamus O'Shaunessy",
                       "The Irish Curse", "Fella"],
        award=["WWE Championship (3 reigns, first Irish-born champion)",
               "World Heavyweight Championship (1 reign, 210 days)",
               "WWE United States Championship (3 reigns)",
               "Raw Tag Team Championship (4 reigns, with Cesaro)",
               "SmackDown Tag Team Championship (1 reign, with Cesaro)",
               "King of the Ring (2010)",
               "Royal Rumble winner (2012)",
               "Money in the Bank winner (2015)"],
        knowsAbout=["Professional wrestling", "WWE", "Championship wrestling", "Irish sport",
                    "Strength training", "Tag team wrestling"],
        description="Sheamus, born Stephen Farrelly in Dublin, is an Irish professional "
                    "wrestler and the first Irish-born WWE Champion. A four-time world "
                    "champion, he won the WWE Championship three times and the World "
                    "Heavyweight Championship once - the latter in 18 seconds at "
                    "WrestleMania XXVIII - plus the 2010 King of the Ring, the 2012 Royal "
                    "Rumble, the 2015 Money in the Bank contract, three United States "
                    "Championships and five tag team titles with Cesaro as The Bar. He "
                    "has never won the Intercontinental Championship. His last match was "
                    "November 17, 2025, and his departure from WWE was reported, though "
                    "not officially confirmed, in July 2026.",
        sameAs=["https://en.wikipedia.org/wiki/Sheamus",
                "https://www.wwe.com/superstars/sheamus"],
    ),
)
