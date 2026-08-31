# -*- coding: utf-8 -*-
"""Asuka - dossier data.

Compiled August 31, 2026. Sources are the web pages opened for this build
(Wrestlezone, Fightful x2, Yahoo Sports UK, Wikipedia's Kabuki Warriors article)
plus verified career history. Her status is reported exactly as the sources
report it: "semi-retired" per Dave Meltzer, "will remain aligned with the
company" per PWInsider — a live conflict, printed as one.

Deliberate omissions:
  * No career win-loss total — none verified.
  * The end of her first 2020 Raw Women's Championship reign is stated without a
    hard date: the Extreme Rules-era finish was contested on-screen and the
    published tables differ on the endpoint, so the hedge is printed instead.
  * Backlash 2026 is dated May 9 per Fightful's results URL; a Wrestlezone
    summary gave May 11, which contradicts the calendar and is not adopted.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2016-04-01", promo="WWE", landmark=True,
         event="NXT TakeOver: Dallas", opponent="Bayley", opponent_html=True,
         stip="Singles — the 510-day reign begins", title="NXT Women's Championship"),
    dict(result="W", date="2017-08-19", promo="WWE",
         event="NXT TakeOver: Brooklyn III", opponent="Ember Moon",
         stip="Singles — her final NXT title defense; she relinquished the belt "
              "undefeated that September",
         title="NXT Women's Championship"),
    dict(result="W", date="2018-01-28", promo="WWE", type="tag", landmark=True,
         event="Royal Rumble", opponent="The first women's Royal Rumble field",
         stip="Won the first women's Royal Rumble match in history", title=""),
    dict(result="L", date="2018-04-08", promo="WWE", landmark=True,
         event="WrestleMania 34", opponent="Charlotte Flair",
         stip="Singles — the undefeated streak ends at 914 days",
         title="SmackDown Women's Championship"),
    dict(result="W", date="2018-12-16", promo="WWE", type="tag", landmark=True,
         event="TLC", opponent="Becky Lynch & Charlotte Flair",
         stip="Triple threat TLC match — the first women's TLC match, and it closed the show",
         title="SmackDown Women's Championship"),
    dict(result="W", date="2019-10-06", promo="WWE", type="tag",
         event="Hell in a Cell", opponent="Alexa Bliss & Nikki Cross",
         stip="With Kairi Sane — the first Kabuki Warriors tag title win",
         title="WWE Women's Tag Team Championship"),
    dict(result="W", date="2020-05-10", promo="WWE", type="tag", landmark=True,
         event="Money in the Bank", opponent="Five other women",
         stip="The corporate ladder match — the briefcase turned out to contain the Raw "
              "Women's Championship itself",
         title=""),
    dict(result="W", date="2020-08-23", promo="WWE",
         event="SummerSlam", opponent="Sasha Banks", opponent_html=True,
         stip="Singles — regains the Raw Women's Championship, her second reign",
         title="WWE Raw Women's Championship"),
    dict(result="L", date="2021-04-11", promo="WWE",
         event="WrestleMania 37 Night 2", opponent="Rhea Ripley",
         stip="Singles — the 231-day reign ends", title="WWE Raw Women's Championship"),
    dict(result="W", date="2023-05-27", promo="WWE", landmark=True,
         event="Night of Champions — Jeddah", opponent="Bianca Belair",
         stip="Singles — ends Belair's 420-day reign", title="WWE Raw Women's Championship"),
    dict(result="L", date="2023-08-05", promo="WWE", type="tag",
         event="SummerSlam", opponent="Bianca Belair & Charlotte Flair",
         stip="Triple threat — Belair wins, and Iyo Sky cashes in on Belair minutes later",
         title="WWE Women's Championship"),
    dict(result="W", date="2025-11-10", promo="WWE", type="tag",
         event="Raw", opponent="Charlotte Flair & Alexa Bliss",
         stip="With Kairi Sane — the third Kabuki Warriors reign, with Nia Jax and Lash "
              "Legend interfering",
         title="WWE Women's Tag Team Championship"),
    dict(result="L", date="2026-01-05", promo="WWE", type="tag",
         event="Raw — Netflix anniversary show", opponent="Rhea Ripley & Iyo Sky",
         stip="With Kairi Sane — the 56-day reign ends",
         title="WWE Women's Tag Team Championship"),
    dict(result="L", date="2026-04-20", promo="WWE", type="tag",
         event="Raw", opponent="Rhea Ripley & Iyo Sky",
         stip="The Kabuki Warriors' final match — Kairi Sane was released four days later",
         title=""),
    dict(result="L", date="2026-05-09", promo="WWE", landmark=True,
         event="Backlash — Tampa", opponent="Iyo Sky",
         stip="Singles — Over the Moonsault; the embrace afterwards, and her last match to date",
         title=""),
]

# opponent_html rows carry a real <a>, so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Bayley": "bayley", "Sasha Banks": "mercedes-mone"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="asuka",
    name="Asuka",
    realname="Kanako Urai",
    epithet="The Empress of Tomorrow",
    hook="Record & Titles",

    meta_desc=("Asuka, The Empress of Tomorrow, went 914 days undefeated in WWE, won the first "
               "women's Royal Rumble and holds four world title reigns. Semi-retired as of 2026. "
               "Full record, titles, factions, records and career."),
    og_desc=("The Empress of Tomorrow: a 914-day undefeated streak, the first women's Royal Rumble, "
             "a 510-day NXT reign and four world titles — now semi-retired, on her own terms."),
    tw_desc="The Empress: 914 days unbeaten, the first women's Rumble, 4 world titles — semi-retired 2026.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2004",
    height_imp="5&#8242;3&#8243;",
    weight_lb="137",
    world_titles="4",
    vitals_tagline="Nobody is ready for Asuka",
    support_note="Merch &middot; Games &middot; Watch",
    x_url="https://x.com/WWEAsuka",
    ig_url="https://www.instagram.com/wwe_asuka/",
    sp_items=[
        dict(ic="AS", title="Asuka Merch", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable in 2K18 through 2K26",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="YT", title="KanaChanTV", sub="Her gaming YouTube channel",
             tag="Watch", href="https://www.youtube.com/@KanaChanTV"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/asuka"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Kana &middot; The Empress of Tomorrow &middot; Kabuki Warrior",
    hero_tag="Osaka, Japan &middot; <em>Japanese independents &middot; NXT &middot; WWE &middot; "
             "2004&ndash;present</em>",
    now_label="NOW",
    now_bold="Semi-retired, still aligned with WWE",
    now_tail=" &middot; her last match was the Backlash loss to Iyo Sky on May 9, 2026, ended with an "
             "embrace &mdash; Meltzer says semi-retired, PWInsider says she stays with the company",
    hstats=[
        dict(value="914", x=False, label="Day Undefeated Streak"),
        dict(value="4",   x=True,  label="World Titles"),
        dict(value="1st", x=False, label="Women's Rumble Winner"),
        dict(value="510", x=False, label="Day NXT Reign"),
    ],
    ghost_link="From Kana to the Empress, undefeated for two and a half years",
    vlabel="Est. 2004 &middot; Osaka, Japan",
    mono="AS",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Asuka</b> arrived in WWE already finished &mdash; a fully formed, mist-spitting, "
        "limb-snapping veteran of the Japanese independents &mdash; and the company responded by "
        "doing something it almost never does: it let her win, and kept letting her win, for two and "
        "a half years. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">914</span>'
        '<span class="pull-cap">days undefeated from her 2015 debut to WrestleMania 34 &mdash; the longest streak of the modern era</span></span>'
        "The record underneath the streak: a 510-day NXT Women's Championship reign relinquished "
        "undefeated, the <b>first women's Royal Rumble</b> win in 2018, four main-roster world title "
        "reigns, a Money in the Bank briefcase that turned out to have a world championship inside "
        "it, four Women's Tag Team Championship reigns, and recognition as WWE's second Women's "
        "Grand Slam and third Women's Triple Crown champion.",

        "The August 2026 line is that &ldquo;Asuka has retired.&rdquo; That is not what the sources "
        "say, and the distinction matters. After she lost to Iyo Sky at Backlash on <b>May 9, "
        "2026</b> &mdash; a match wrestled to &ldquo;We Want Kairi&rdquo; chants three weeks after "
        "WWE released her tag partner &mdash; she broke character and embraced Sky, and the goodbye "
        "readings wrote themselves. But Dave Meltzer's actual report was <b>&ldquo;semi-"
        "retired,&rdquo;</b> with Meltzer himself adding he had not gotten an exact meaning of the "
        "term, and PWInsider's Mike Johnson reported she will <b>remain aligned with WWE</b> and is "
        "expected to compete again on a reduced scale. She was at Raw in Knoxville after Backlash. "
        "Retired people do not do that. This page lists her as semi-retired with the conflict "
        "attached, and notes one small date wrinkle besides: Fightful's results dateline puts "
        "Backlash on May 9, while a Wrestlezone summary says May 11 &mdash; a Monday. The May 9 "
        "Saturday is adopted.",

        "She was born Kanako Urai in Osaka on September 26, 1981, and wrestled the Japanese "
        "independents from 2004 as <b>Kana</b> &mdash; while also working as a graphic designer and "
        "games journalist, a sideline that never really ended. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">510</span>'
        '<span class="pull-cap">days as NXT Women&rsquo;s Champion, 2016&ndash;17 &mdash; relinquished undefeated, never lost</span></span>'
        "WWE signed her in 2015 at thirty-three, past the age at which the machine usually invests, "
        "and NXT built its division around her: she took the NXT Women's Championship from Bayley at "
        "TakeOver: Dallas on April 1, 2016 and never lost it, relinquishing the belt in September "
        "2017 after 510 days with a broken collarbone and an intact zero in the loss column. The "
        "streak &mdash; 914 days across NXT and the main roster by WWE's count &mdash; ended in the "
        "match that was built to end it, against Charlotte Flair at WrestleMania 34 on April 8, "
        "2018. She cried, bowed, and got the biggest reaction of the night for losing.",

        "Everything since has been an argument that dominance was never the whole act. She won the "
        "SmackDown Women's Championship in the first women's TLC match in December 2018; the 2020 "
        "corporate ladder match handed her the Raw Women's Championship when Becky Lynch revealed "
        "the briefcase's contents and her own pregnancy in the same segment; she ended Bianca "
        "Belair's 420-day reign at Night of Champions in May 2023. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">3</span>'
        '<span class="pull-cap">Kabuki Warriors tag title reigns with Kairi Sane, 2019&ndash;2026 &mdash; the partnership WWE ended by releasing Sane</span></span>'
        "And through all of it ran the <b>Kabuki Warriors</b>: three tag championship reigns with "
        "Kairi Sane across seven years, the last won in November 2025 and lost on Raw's Netflix "
        "anniversary show in January 2026. The team's ending was not booked &mdash; WWE released "
        "Sane on April 24, 2026, four days after their final match, with Asuka saying the pair had "
        "been &ldquo;on standby&rdquo; to fill in at WrestleMania 42 that never called them. The "
        "Backlash match with Sky, and the hug after it, is where the story currently rests.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Highlight set",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("914",      "Day undefeated streak"),
            ("4&times;", "World titles"),
            ("4&times;", "Tag title reigns"),
            ("510",      "Day NXT reign"),
            ("2018",     "First women's Rumble"),
            ("2020",     "Money in the Bank"),
        ],
        lead=("Fifteen documented bouts &mdash; a highlight subset, not a career count, and no "
              "career win&ndash;loss total is published because none was verified; her Japanese "
              "independent record as Kana is outside the scope of this ledger entirely. The rows run "
              "from TakeOver: Dallas to the Backlash 2026 match that is, as of compilation, her "
              "last. Filter by match type, tap any column header to sort, and turn spoilers on to "
              "reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("Four bouts the reputation rests on. The ratings are this dossier's own "
                    "editorial grades, not Wrestling Observer figures &mdash; no Meltzer ratings "
                    "were verified in this pass and none are quoted."),
    signature=[
        dict(rating="4.5", event="WrestleMania 34", opponent="Charlotte Flair",
             stip="SmackDown Women's Championship — the streak dies standing"),
        dict(rating="4.5", event="TLC 2018", opponent="Becky Lynch & Charlotte Flair",
             stip="The first women's TLC match — CBS Sports' 2018 WWE Match of the Year"),
        dict(rating="4.0", event="Night of Champions 2023", opponent="Bianca Belair",
             stip="Raw Women's Championship — ending the 420-day reign"),
        dict(rating="4.0", event="Backlash 2026", opponent="Iyo Sky",
             stip="The farewell that is not officially a farewell"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("4&times;", "World title reigns"),
            ("4&times;", "Tag title reigns"),
            ("2nd",      "Women's Grand Slam"),
            ("3rd",      "Women's Triple Crown"),
        ],
        lead=("Four world championship reigns across two renamed lineages, four tag reigns with two "
              "partners, and an NXT reign that never ended in the ring. One endpoint is deliberately "
              "left soft: the finish of her first 2020 Raw title reign was contested on-screen and "
              "the published tables disagree, so no hard date is printed for it."),
        rows=[
            dict(ic="R", name="Raw Women's Championship / WWE Women's Championship", count="3",
                 sub="2020, the Money in the Bank briefcase revealed as the title itself on the May "
                     "11 Raw &mdash; the reign ended against Sasha Banks that July in a finish "
                     "contested on-screen; tables disagree on the exact date and none is adopted "
                     "&middot; 2020&ndash;21, regained from Banks at SummerSlam on August 23, "
                     "<b>231 days</b>, ended by Rhea Ripley at WrestleMania 37 &middot; 2023, def. "
                     "Bianca Belair at Night of Champions on May 27, ending a 420-day reign; the "
                     "belt was renamed the WWE Women's Championship in June and she lost the "
                     "SummerSlam triple threat on August 5"),
            dict(ic="S", name="SmackDown Women's Championship", count="1",
                 sub="2018&ndash;19 &middot; won in the first women's TLC match on December 16, "
                     "2018, over Becky Lynch and Charlotte Flair &middot; lost to Charlotte Flair "
                     "on the March 26, 2019 SmackDown"),
            dict(ic="T", name="WWE Women's Tag Team Championship", count="4",
                 sub="Three Kabuki Warriors reigns with Kairi Sane &mdash; October 6, 2019 (Hell in "
                     "a Cell) to WrestleMania 36; January 26, 2024 (SmackDown) to Backlash France "
                     "on May 4, 2024; November 10, 2025 (Raw) to the January 5, 2026 Netflix "
                     "anniversary Raw, 56 days &mdash; plus one reign with Charlotte Flair, won at "
                     "TLC on December 20, 2020 &middot; a Wrestlezone summary credits her with "
                     "five total reigns; the title-history tables support four, and four is "
                     "published"),
            dict(ic="N", name="NXT Women's Championship", count="1",
                 sub="April 1, 2016 &ndash; September 6, 2017 &middot; won from Bayley at TakeOver: "
                     "Dallas, relinquished undefeated with a broken collarbone after <b>510 "
                     "days</b> &mdash; the longest reign in the title's history, and she never "
                     "lost the belt in a match"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="One partnership that defined the second half of the career, and the faction it "
             "folded into.",
        cards=[
            dict(era="WWE &middot; 2019&ndash;2026",
                 name="The Kabuki Warriors",
                 members="Asuka, Kairi Sane; Paige as manager until October 2019",
                 desc="Formed April 16, 2019 with Paige managing — until Asuka misted her that "
                      "October, one of the era's great manager write-offs. Three Women's Tag Team "
                      "Championship reigns across seven years, spanning both women's separate "
                      "singles peaks and Sane's 2020-23 absence in Japan. It did not end in the "
                      "ring: after a final match on the April 20, 2026 Raw, WWE released Sane on "
                      "April 24 — a cut that landed so badly that Backlash three weeks later was "
                      "wrestled to \"We Want Kairi\" chants. Asuka said afterwards the two had "
                      "been on standby to appear at WrestleMania 42 and were never used."),
            dict(era="WWE &middot; 2023&ndash;25",
                 name="Damage CTRL",
                 members="Bayley, Iyo Sky, Dakota Kai, Asuka, Kairi Sane",
                 desc="Asuka and Sane joined Bayley's faction in late 2023, which put the Kabuki "
                      "Warriors inside the dominant unit of the division and set up the January "
                      "2024 tag title win. The faction's slow dissolution through 2024-25 left "
                      "the Warriors as its last functioning cell — and made Iyo Sky, a friend "
                      "from both Damage CTRL and the Japanese scene, the natural opponent for "
                      "what currently stands as Asuka's final match."),
            dict(era="Japan &middot; 2004&ndash;15",
                 name="The Kana office",
                 members="Kana, freelancing",
                 desc="Not a faction — the absence of one, listed for what it explains. As Kana "
                      "she was a freelancer who booked herself across promotions, produced her "
                      "own shows, and arrived in WWE with a finished style nobody there taught "
                      "her. The independence is the through-line: WWE never really gave Asuka a "
                      "character so much as a spotlight."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Two names, one wrestler &mdash; <b>Kana</b> (2004&ndash;15) &rarr; <b>Asuka</b> "
             "(2015&ndash;present), with the mask of the character shifting around a style that "
             "never changed.",
        cards=[
            dict(mono="KN", era="Japan &middot; 2004&ndash;15", name="Kana",
                 desc="The green-misted freelancer of the Japanese independents — stiff kicks, "
                      "cross armbreakers, and a sideline as a games journalist and graphic "
                      "designer. She debuted in 2004, retired briefly in 2006, and returned in "
                      "2007 to become one of the most respected workers in joshi."),
            dict(mono="EM", era="NXT &middot; 2015&ndash;17", name="The Empress of Tomorrow",
                 desc="Signed at thirty-three and booked like a final boss: a 510-day NXT "
                      "Women's Championship reign, relinquished rather than lost, and the start "
                      "of the 914-day streak. \"Nobody is ready for Asuka\" was the rare "
                      "catchphrase that was simply an accurate description."),
            dict(mono="ST", era="WWE &middot; 2017&ndash;20", name="The streak, and after",
                 desc="The undefeated run ended at WrestleMania 34 against Charlotte Flair, and "
                      "the character's second act became reinvention: the first women's Rumble "
                      "win, the TLC title victory, and then the 2020 pivot into the grinning, "
                      "unhinged Empress who won a world title out of a briefcase."),
            dict(mono="KW", era="WWE &middot; 2023&ndash;26", name="The Kabuki Warrior",
                 desc="The heel veteran era: misting friends, three-way title losses, tag gold "
                      "with Kairi Sane inside Damage CTRL, and a final singles run against Iyo "
                      "Sky that ended — for now — with an out-of-character embrace at Backlash "
                      "2026 and a Meltzer report reading \"semi-retired.\""),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Osaka to the first women's Royal Rumble, with a streak in the middle nobody has "
             "matched since.",
        rows=[
            dict(year="2004", title="Debuts as Kana",
                 desc="Begins on the Japanese independents at twenty-two, alongside work as a "
                      "graphic designer and video game journalist."),
            dict(year="2015", title="Signs with WWE at thirty-three",
                 desc="Debuts in NXT that October as Asuka. The losing stops immediately."),
            dict(year="2016", title="NXT Women's Champion",
                 desc="Beats Bayley at TakeOver: Dallas on April 1. She will hold the title 510 "
                      "days and never lose it, relinquishing it in September 2017 with a broken "
                      "collarbone."),
            dict(year="2018", title="The first women's Rumble, and the streak's end",
                 desc="Wins the inaugural women's Royal Rumble on January 28; Charlotte Flair "
                      "ends the 914-day undefeated streak at WrestleMania 34 on April 8; wins "
                      "the SmackDown Women's Championship in the first women's TLC match on "
                      "December 16."),
            dict(year="2019", title="Kabuki Warriors",
                 desc="Forms the team with Kairi Sane in April; they win the Women's Tag Team "
                      "Championship at Hell in a Cell on October 6, and Asuka mists manager "
                      "Paige out of the act."),
            dict(year="2020", title="A world title out of a briefcase",
                 desc="Wins the Money in the Bank corporate ladder match on May 10; Becky Lynch "
                      "reveals the case contained the Raw Women's Championship. Loses it to "
                      "Sasha Banks in a contested summer finish, regains it at SummerSlam on "
                      "August 23, and holds it 231 days."),
            dict(year="2021", title="The reign ends at WrestleMania",
                 desc="Rhea Ripley takes the Raw Women's Championship at WrestleMania 37 on "
                      "April 11. Injuries and a long hiatus follow."),
            dict(year="2023", title="Ends the 420-day reign",
                 desc="Beats Bianca Belair at Night of Champions on May 27 for the Raw Women's "
                      "Championship — renamed the WWE Women's Championship weeks later — and "
                      "loses it in the SummerSlam triple threat on August 5. Joins Damage CTRL "
                      "with Kairi Sane that autumn."),
            dict(year="2024", title="Tag gold, then a knee",
                 desc="Second Kabuki Warriors reign from January 26 to Backlash France on May 4; "
                      "knee trouble takes her off television for much of the year."),
            dict(year="2025", title="The third reign",
                 desc="Returns, reunites with Sane, and beats Charlotte Flair and Alexa Bliss on "
                      "the November 10 Raw for a third Kabuki Warriors tag championship."),
            dict(year="2026", title="The quiet ending, maybe",
                 desc="Loses the tag titles on the January 5 Netflix anniversary Raw; the "
                      "Warriors' final match comes on April 20 and WWE releases Sane on April "
                      "24; loses to Iyo Sky at Backlash on May 9 and embraces her afterwards. "
                      "Meltzer reports semi-retirement; PWInsider reports she stays with WWE."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who she went to war with.",
        cards=[
            dict(name="Charlotte Flair",
                 desc="The woman WWE chose to end the streak. WrestleMania 34, April 8, 2018 — "
                      "914 days of dominance ended by the Figure Eight, with Asuka bowing "
                      "through tears afterwards. Flair also took the SmackDown title back in "
                      "March 2019, and stood on the losing side of the November 2025 Raw where "
                      "the Kabuki Warriors won their last championship. The rivalry is the "
                      "streak's frame: it made the number matter."),
            dict(name="Becky Lynch",
                 desc="The counterweight rivalry of 2018-19: Asuka took the SmackDown Women's "
                      "Championship in the TLC triple threat that CBS Sports named its 2018 WWE "
                      "Match of the Year, and the becky-lynch dossier on this site calls Asuka "
                      "\"the opponent Lynch consistently could not put away cleanly.\" It was "
                      "Lynch who handed her the Raw Women's Championship in 2020 — the "
                      "briefcase reveal — which is its own kind of ending."),
            dict(name="Bianca Belair",
                 desc="One match, one statement: Night of Champions, May 27, 2023, ending "
                      "Belair's 420-day reign — the longest women's world title reign of the "
                      "modern era to that point — and proving the veteran could still be booked "
                      "as the one who beats the unbeatable."),
            dict(name="Iyo Sky",
                 desc="Friend, Damage CTRL stablemate, and the opponent of what currently "
                      "stands as her final match. Sky and Rhea Ripley took the Kabuki Warriors' "
                      "titles in January 2026 and beat them again in April; at Backlash on May "
                      "9, 2026, Sky won the singles match with the Over the Moonsault, and "
                      "Asuka broke character to embrace her. If that was the last image, it was "
                      "a chosen one."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="The rare wrestler whose gaming credentials are literal.",
        rows=[
            dict(when="2004&ndash;", title="Games journalism and design", kind="Career",
                 desc="Before and during the Kana years she worked as a graphic designer and "
                      "wrote about video games for Japanese outlets — a real second profession, "
                      "not a gimmick footnote."),
            dict(when="2018&ndash;", title="KanaChanTV", kind="YouTube",
                 desc="Her own gaming and lifestyle YouTube channel, run in character-adjacent "
                      "Japanese and maintained through injuries and hiatuses — the most direct "
                      "line to her the fanbase has."),
            dict(when="2018&ndash;", title="WWE 2K", kind="Game",
                 desc="Playable from WWE 2K18 through WWE 2K26."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, with their counting rules attached.",
        stats=[
            ("914", "Day undefeated streak"),
            ("510", "Day NXT reign"),
            ("1st", "Women's Rumble winner"),
        ],
        rows=[
            dict(name="A 914-day undefeated streak, 2015-18",
                 sub="From her October 2015 NXT debut to WrestleMania 34 on April 8, 2018, per "
                     "WWE's own framing of the number. The exact match count attached to the "
                     "streak varies by source and no figure is adopted here; the days do not."),
            dict(name="510 days as NXT Women's Champion — never beaten for it",
                 sub="April 1, 2016 to September 6, 2017. She relinquished the title with a "
                     "broken collarbone, undefeated — the longest reign in the championship's "
                     "history."),
            dict(name="Winner of the first women's Royal Rumble match",
                 sub="January 28, 2018. A first that can never be equalled, only shared by the "
                     "twenty-nine women she threw out — the last of them Nikki Bella."),
            dict(name="Won a world title via the Money in the Bank briefcase without a cash-in",
                 sub="May 10, 2020: the \"corporate ladder\" briefcase contained the Raw Women's "
                     "Championship itself, revealed by the pregnant champion Becky Lynch on the "
                     "May 11 Raw — the only world title in the match's history won inside the "
                     "briefcase."),
            dict(name="Part of the first women's TLC match, and won it",
                 sub="December 16, 2018, over Becky Lynch and Charlotte Flair, for the SmackDown "
                     "Women's Championship — CBS Sports' 2018 WWE Match of the Year."),
            dict(name="Second Women's Grand Slam Champion, third Women's Triple Crown Champion",
                 sub="Per the Kabuki Warriors article's accounting of WWE's recognition — behind "
                     "Bayley on the Grand Slam list."),
            dict(name="Four Women's Tag Team Championship reigns, three of them with Kairi Sane",
                 sub="2019-20, 2024 and 2025-26 as the Kabuki Warriors, plus 2020-21 with "
                     "Charlotte Flair. A five-reign figure circulates from one summary; the "
                     "tables support four."),
            dict(name="Ended the longest women's world title reign of the modern era",
                 sub="Bianca Belair's 420 days, at Night of Champions on May 27, 2023."),
        ],
        footnote=("No career win-loss total appears anywhere on this page; between the streak era "
                  "and the Kana years no verified aggregate exists, and nothing is guessed. Her "
                  "status is printed exactly as sourced: semi-retired per Meltzer, still aligned "
                  "with WWE per PWInsider, last match May 9, 2026."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="X / Twitter", v="@WWEAsuka", href="https://x.com/WWEAsuka"),
        dict(k="Instagram", v="@wwe_asuka", href="https://www.instagram.com/wwe_asuka/"),
        dict(k="Wrestlezone", v="Is Asuka retired? The semi-retirement reporting",
             href="https://www.wrestlezone.com/news/1638035-is-asuka-retired-wwe"),
        dict(k="Yahoo Sports", v="Backlash 2026 — the Iyo Sky match and the Kairi chants",
             href="https://uk.sports.yahoo.com/news/wwe-backlash-2026-results-iyo-235810279.html"),
        dict(k="Fightful", v="Kabuki Warriors win the tag titles, November 10, 2025",
             href="https://www.fightful.com/wrestling/kabuki-warriors-win-wwe-womens-tag-team-titles-on-wwe-raw/"),
        dict(k="Fightful", v="Asuka on losing the tag titles, January 2026",
             href="https://www.fightful.com/wrestling/asuka-on-kabuki-warriors-losing-wwe-womens-tag-titles-weve-got-another-chance-to-seize-the-championship-and-break-even-more-records/"),
        dict(k="Wikipedia", v="The Kabuki Warriors — reign dates",
             href="https://en.wikipedia.org/wiki/The_Kabuki_Warriors"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/asuka.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Has Asuka retired?",
            a="Not officially, and the word the reporting actually uses is <b>semi-retired</b>. "
              "After she lost to Iyo Sky at Backlash on May 9, 2026 and embraced her afterwards, "
              "Dave Meltzer reported she is semi-retired &mdash; while conceding he had not "
              "gotten an exact meaning of the term &mdash; and PWInsider's Mike Johnson reported "
              "she will remain aligned with WWE and is expected to wrestle again on a reduced "
              "schedule. She was in Knoxville for Raw after Backlash. No retirement has been "
              "announced by Asuka or WWE, so this page treats the Backlash match as her last to "
              "date, not her last.",
            q_ld="Has Asuka retired from WWE?",
            a_ld="Not officially. As of August 31, 2026, Asuka is described in reporting as "
                 "semi-retired: Dave Meltzer used that term after her loss to Iyo Sky at Backlash "
                 "on May 9, 2026, while PWInsider reported she will remain aligned with WWE and "
                 "is expected to compete again on a reduced schedule. Neither Asuka nor WWE has "
                 "announced a retirement. The Backlash 2026 match is her most recent match, not "
                 "a confirmed final one."),
        dict(
            q="How long was Asuka undefeated in WWE?",
            a="<b>914 days</b>, by WWE's count &mdash; from her NXT debut in October 2015 to "
              "WrestleMania 34 on April 8, 2018, when Charlotte Flair beat her for the SmackDown "
              "Women's Championship. Inside the streak sits the 510-day NXT Women's Championship "
              "reign she relinquished, undefeated, with a broken collarbone in September 2017. "
              "The match count attached to the streak varies between retellings, so this page "
              "publishes the days and leaves the match total alone.",
            q_ld="How long was Asuka's undefeated streak in WWE?",
            a_ld="Asuka was undefeated for 914 days by WWE's count, from her NXT debut in October "
                 "2015 until Charlotte Flair defeated her at WrestleMania 34 on April 8, 2018. "
                 "During the streak she held the NXT Women's Championship for 510 days, "
                 "relinquishing it undefeated in September 2017 due to a broken collarbone. "
                 "Published match counts for the streak vary by source."),
        dict(
            q="What happened to the Kabuki Warriors?",
            a="WWE ended them, not an opponent. The team lost the Women's Tag Team Championship "
              "to Rhea Ripley and Iyo Sky on the January 5, 2026 Netflix anniversary Raw after a "
              "56-day third reign, lost a rematch on the April 20 Raw &mdash; their final match "
              "&mdash; and four days later WWE <b>released Kairi Sane</b>, on April 24, 2026. "
              "Asuka has said the pair were on standby to appear at WrestleMania 42 and were "
              "never used. The release landed badly enough that her Backlash match with Sky was "
              "wrestled to &ldquo;We Want Kairi&rdquo; chants.",
            q_ld="Why did the Kabuki Warriors break up?",
            a_ld="The Kabuki Warriors ended because WWE released Kairi Sane on April 24, 2026, "
                 "four days after the team's final match on the April 20 episode of Raw. They "
                 "had lost the WWE Women's Tag Team Championship to Rhea Ripley and Iyo Sky on "
                 "January 5, 2026 after a 56-day third reign. Asuka has said the team was on "
                 "standby for WrestleMania 42 but was not used, and her Backlash 2026 match "
                 "against Iyo Sky featured We Want Kairi chants from the crowd."),
        dict(
            q="How did Asuka win a world title from the Money in the Bank briefcase without cashing in?",
            a="Because in 2020 the briefcase <i>was</i> the title. She won the May 10, 2020 "
              "women's Money in the Bank ladder match &mdash; the pandemic-era &ldquo;corporate "
              "ladder&rdquo; match filmed in WWE headquarters &mdash; and on the next night's "
              "Raw, Becky Lynch announced her pregnancy and revealed that the briefcase "
              "contained the Raw Women's Championship itself. Asuka became champion on the "
              "spot: the only time the briefcase has held a world title rather than a contract "
              "for one.",
            q_ld="How did Asuka win the Raw Women's Championship at Money in the Bank 2020?",
            a_ld="Asuka won the women's Money in the Bank ladder match on May 10, 2020, and on "
                 "the following night's Raw, the pregnant champion Becky Lynch revealed that "
                 "the briefcase contained the Raw Women's Championship itself rather than a "
                 "contract, making Asuka the champion immediately. It is the only time the "
                 "Money in the Bank briefcase has contained a world championship."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Kanako Urai"),
        dict(label="Born", value="September 26, 1981", sub="Osaka, Japan &middot; age 44"),
        dict(label="Billed from", value="Osaka, Japan"),
        dict(label="Height", value="5&#8242;3&#8243;", sub="160 cm"),
        dict(label="Weight", value="137 lb", sub="62 kg (billed)"),
        dict(label="Debut", value="June 2004", sub="Japanese independents, as Kana"),
        dict(label="WWE debut", value="October 2015", sub="NXT, at thirty-three"),
        dict(label="Ring names", value="Kana &rarr; Asuka",
             sub="2004&ndash;15 &middot; 2015&ndash;present"),
        dict(label="Finishers", value="Asuka Lock &middot; kicks &middot; green mist",
             sub="the mist is technically a foul, which is the point"),
        dict(label="Last match", value="May 9, 2026",
             sub="L to Iyo Sky at Backlash, Tampa &mdash; semi-retired per Meltzer since"),
        dict(label="Brand", value="Raw", sub="as of her last appearances"),
        dict(label="Also known as",
             value="The Empress of Tomorrow &middot; Kabuki Warrior &middot; Kana"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1981-09-26",
    bornplace="Osaka, Japan",
    nationality="Japan",
    height_cm=160,
    weight_kg=62,
    ld=dict(
        alternateName=["Kanako Urai", "Kana", "The Empress of Tomorrow"],
        award=["Raw Women's Championship / WWE Women's Championship (3 reigns)",
               "SmackDown Women's Championship (1 reign)",
               "WWE Women's Tag Team Championship (4 reigns — 3 as the Kabuki Warriors with "
               "Kairi Sane, 1 with Charlotte Flair)",
               "NXT Women's Championship (1 reign, 510 days, relinquished undefeated)",
               "First women's Royal Rumble winner (2018)",
               "Women's Money in the Bank winner (2020)",
               "914-day undefeated streak (2015-2018)",
               "Second WWE Women's Grand Slam Champion",
               "Third WWE Women's Triple Crown Champion"],
        knowsAbout=["Professional wrestling", "WWE", "Joshi puroresu", "NXT",
                    "Women's professional wrestling", "Video games", "Graphic design"],
        description="Asuka, born Kanako Urai in Osaka, Japan, is a Japanese professional wrestler "
                    "signed to WWE, known as The Empress of Tomorrow. She went 914 days undefeated "
                    "from her 2015 debut until WrestleMania 34, held the NXT Women's Championship "
                    "for a record 510 days without losing it, won the first women's Royal Rumble "
                    "in 2018, and has won four main-roster world championships and four Women's "
                    "Tag Team Championships, three as the Kabuki Warriors with Kairi Sane. As of "
                    "August 2026 she is reported as semi-retired, with her last match a loss to "
                    "Iyo Sky at Backlash on May 9, 2026.",
        sameAs=["https://x.com/WWEAsuka",
                "https://www.instagram.com/wwe_asuka/",
                "https://en.wikipedia.org/wiki/Asuka_(wrestler)",
                "https://www.wwe.com/superstars/asuka"],
    ),
)
