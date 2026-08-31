# -*- coding: utf-8 -*-
"""Sami Zayn - dossier data.

Sources: web-verified August 31, 2026 (Wikipedia, Fox News, Fightful, F4W/WON,
Last Word on Sports, IWNerd Observer round-ups). Every match row carries a
day-precision date confirmed in at least one of those sources.

Deliberate omissions:
  * No career win-loss total - no verified figure exists and none is invented.
  * The July 18, 2026 Saturday Night's Main Event tag match (with Gunther, against
    CM Punk and Cody Rhodes) is advertised on WWE.com but no result was verified in
    this pass, so it appears nowhere.
  * Independent-era reign lengths (PWG, IWS) are listed by count only where exact
    dates were not verified.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2014-12-11", promo="WWE", landmark=True,
         event="NXT TakeOver: R Evolution", opponent="Adrian Neville",
         stip="Singles — title or quit; 4.75 stars (Meltzer)", title="NXT Championship"),
    dict(result="L", date="2015-02-11", promo="WWE", landmark=True,
         event="NXT TakeOver: Rival", opponent="Kevin Owens", opponent_html=True,
         stip="Singles — ref stoppage; the 62-day reign and the friendship both end",
         title="NXT Championship"),
    dict(result="W", date="2020-03-08", promo="WWE",
         event="Elimination Chamber", opponent="Braun Strowman",
         stip="3-on-1 handicap, with Nakamura and Cesaro — first Intercontinental title",
         title="WWE Intercontinental Championship"),
    dict(result="W", date="2020-09-27", promo="WWE",
         event="Clash of Champions", opponent="Jeff Hardy & AJ Styles",
         stip="Ladder match — unifies the disputed claims", title="WWE Intercontinental Championship"),
    dict(result="L", date="2023-02-18", promo="WWE", landmark=True,
         event="Elimination Chamber — Montreal", opponent="Roman Reigns",
         stip="Singles — the hometown challenge after leaving The Bloodline",
         title="Undisputed WWE Universal Championship"),
    dict(result="W", date="2023-04-01", promo="WWE", type="tag", landmark=True,
         event="WrestleMania 39 Night 1", opponent="The Usos",
         stip="Tag — with Kevin Owens; main event, five stars (Meltzer)",
         title="Undisputed WWE Tag Team Championship"),
    dict(result="L", date="2023-09-02", promo="WWE", type="tag",
         event="Payback", opponent="The Judgment Day",
         stip="Steel City Street Fight — the 154-day reign ends",
         title="Undisputed WWE Tag Team Championship"),
    dict(result="W", date="2024-04-06", promo="WWE", landmark=True,
         event="WrestleMania 40 Night 1", opponent="Gunther", opponent_html=True,
         stip="Singles — ends the 666-day reign; five stars (Meltzer)",
         title="WWE Intercontinental Championship"),
    dict(result="L", date="2024-08-03", promo="WWE",
         event="SummerSlam — Cleveland", opponent="Bron Breakker",
         stip="Singles — the 119-day reign ends", title="WWE Intercontinental Championship"),
    dict(result="L", date="2025-03-01", promo="WWE", landmark=True,
         event="Elimination Chamber — Toronto", opponent="Kevin Owens", opponent_html=True,
         stip="Unsanctioned match — the feud's floor", title=""),
    dict(result="W", date="2025-08-29", promo="WWE",
         event="SmackDown", opponent="Solo Sikoa",
         stip="Singles — first United States Championship", title="WWE United States Championship"),
    dict(result="L", date="2025-10-17", promo="WWE",
         event="SmackDown", opponent="Ilja Dragunov",
         stip="Singles — the 49-day reign ends", title="WWE United States Championship"),
    dict(result="L", date="2026-01-31", promo="WWE",
         event="Royal Rumble — Riyadh", opponent="Drew McIntyre", opponent_html=True,
         stip="Singles — challenge", title="Undisputed WWE Championship"),
    dict(result="W", date="2026-03-27", promo="WWE",
         event="SmackDown", opponent="Carmelo Hayes",
         stip="Singles — second United States Championship", title="WWE United States Championship"),
    dict(result="L", date="2026-04-19", promo="WWE",
         event="WrestleMania 42 Night 2 — Las Vegas", opponent="Trick Williams",
         stip="Singles — the 23-day reign ends", title="WWE United States Championship"),
    dict(result="W", date="2026-06-27", promo="WWE", type="tag", landmark=True,
         event="Night of Champions — Riyadh", opponent="Cody Rhodes & Gunther",
         stip="Triple threat — rolls up Rhodes; first world title, 24 years in",
         title="Undisputed WWE Championship"),
    dict(result="L", date="2026-07-06", promo="WWE", landmark=True,
         event="Raw — Chicago", opponent="CM Punk", opponent_html=True,
         stip="Singles — the reign ends at nine days", title="Undisputed WWE Championship"),
    dict(result="L", date="2026-08-02", promo="WWE", type="tag",
         event="SummerSlam Night 2 — Minneapolis", opponent="Kevin Owens, Finn Balor & Gunther",
         stip="Fatal four-way, No. 1 contendership — Owens pins Zayn", title=""),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Kevin Owens": "kevin-owens", "Gunther": "gunther",
                 "Drew McIntyre": "drew-mcintyre", "CM Punk": "cm-punk"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="sami-zayn",
    name="Sami Zayn",
    realname="Rami Sebei",
    epithet="The Underdog from the Underground",
    hook="Record & Titles",

    meta_desc=("Sami Zayn won his first world championship, the Undisputed WWE Championship, at Night "
               "of Champions 2026, 24 years into his career - and lost it in nine days. Full record, "
               "titles, factions, records and career."),
    og_desc=("The Underdog from the Underground: the miracle in Riyadh, a nine-day Undisputed WWE "
             "Championship reign, the end of Gunther's 666 days, the Bloodline story, and the belt "
             "shot that turned him."),
    tw_desc="Sami Zayn: first world title after 24 years, held nine days - and then the heel turn.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2002",
    height_imp="6&#8242;1&#8243;",
    weight_lb="212",
    world_titles="1",
    vitals_tagline="The miracle in Riyadh",
    support_note="Merch &middot; Games &middot; Give",
    sp_items=[
        dict(ic="SZ", title="WWE Shop", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable across the WWE 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="SFS", title="Sami for Syria", sub="Mobile clinic fund with the Syrian American "
                                                   "Medical Society, est. 2017",
             tag="Give", charity=True, href="https://www.sams-usa.net/"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit",
             href="https://www.wwe.com/superstars/sami-zayn"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="El Generico &middot; The Honorary Uce &middot; The Last Real Good Guy",
    hero_tag="Laval, Quebec, Canada &middot; <em>IWS &middot; ROH &middot; PWG &middot; NXT &middot; "
             "WWE &middot; 2002&ndash;present</em>",
    now_label="NOW",
    now_bold="SmackDown, no championship",
    now_tail=" &middot; turned on Kevin Owens with the title belt on the August 21 SmackDown and says "
             "CM Punk&rsquo;s Undisputed WWE Championship is still rightfully his",
    hstats=[
        dict(value="9",   x=False, label="Day World Title Reign"),
        dict(value="4",   x=True,  label="Intercontinental Reigns"),
        dict(value="24",  x=False, label="Years to the Top Title"),
        dict(value="1st", x=False, label="Arab WWE World Champion"),
    ],
    ghost_link="From the mask in Montreal to the miracle in Riyadh",
    vlabel="Est. 2002 &middot; Laval, Quebec",
    mono="SZ",

    # ---------------------------------------------------------------- 01 overview
    # index into overview of the correction paragraph -> the framed
    # "Setting one thing straight" callout (aside.corr) on the page
    correction=1,
    overview=[
        "<b>Sami Zayn</b> spent twenty-four years building toward one night and then had nine days to "
        "enjoy it. On June 27, 2026, at Night of Champions in Riyadh, he rolled up Cody Rhodes in a "
        "triple threat that also contained Gunther and won the Undisputed WWE Championship &mdash; his "
        "first world title anywhere, called &ldquo;a miracle in Riyadh&rdquo; on the broadcast. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">9</span>'
        '<span class="pull-cap">days as Undisputed WWE Champion &mdash; June 27 to July 6, 2026, ended by CM Punk in Chicago</span></span>'
        "CM Punk beat him for it on the July 6 Raw at the Allstate Arena, cleanly by "
        "Punk&rsquo;s own account, and the two months since have turned the most reliable babyface of "
        "his generation into something else: on the August 21 SmackDown he hit Kevin Owens &mdash; his "
        "oldest friend &mdash; with the title belt, cost him the championship match, and declared the "
        "title rightfully his.",

        "Two things get collapsed in the retelling. First, the opponent: because Zayn&rsquo;s most "
        "famous singles win is ending Gunther&rsquo;s 666-day Intercontinental reign at WrestleMania 40 "
        "on April 6, 2024, the Riyadh result is often remembered as &ldquo;Zayn finally beat "
        "Gunther for the big one.&rdquo; He did not &mdash; Gunther was in the match, but the fall was "
        "a rollup on <b>Cody Rhodes</b>, the defending champion. Second, the reign: nine days invites "
        "the word &ldquo;shortest,&rdquo; and it is not close to that &mdash; WWE world reigns have "
        "ended in minutes, including Drew McIntyre&rsquo;s 5-minute-46-second World Heavyweight "
        "Championship in 2024. What the win did settle, permanently: it made him a Grand Slam "
        "champion, and the first Arab and first Syrian world champion in WWE history.",

        "He was born Rami Sebei in Laval, Quebec on July 12, 1984, to Syrian parents, debuted in 2002, "
        "and spent eleven years as <b>El Generico</b>, a masked luchador with a cult following and, in "
        "storyline, an orphanage in Tijuana. The mask worked everywhere: two PWG World Championships, "
        "ROH tag titles with Kevin Steen, a wXw title in Germany, a KO-D Openweight title in Japan "
        "lost to Kenny Omega. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">666</span>'
        '<span class="pull-cap">days of Gunther&rsquo;s Intercontinental reign, ended by Zayn at WrestleMania 40 &mdash; still his signature singles win</span></span>'
        "WWE signed him in 2013, unmasked; as Sami Zayn he won the NXT "
        "Championship from Adrian Neville at TakeOver: R Evolution in December 2014 and lost it to a "
        "debuting, turncoat Kevin Owens seven weeks later &mdash; the first WWE chapter of a "
        "friendship-and-betrayal story the two men have now been telling for over twenty years, most "
        "recently in reverse.",

        "The modern run is built on two stories. The Bloodline: from comedy hanger-on in May 2022 to "
        "&ldquo;Honorary Uce&rdquo; to conscience of the group, then the chair shot on Roman Reigns at "
        "the 2023 Royal Rumble and a title challenge in his own Montreal at Elimination Chamber "
        "&mdash; a loss, but the loudest one of the decade &mdash; before he and Owens took the tag "
        "titles from The Usos in the WrestleMania 39 Night 1 main event. And the slow climb after: "
        "Intercontinental Champion a fourth time, United States Champion twice in 2025&ndash;26, a "
        "failed title shot at Drew McIntyre at the 2026 Royal Rumble, and then Riyadh. Since losing "
        "the title he has kept the &ldquo;Last Real Good Guy&rdquo; label he adopted in May 2026 while "
        "behaving like its opposite &mdash; wrecking the August 28 No. 1 contender triple threat, "
        "flooring the referee, and brawling with Punk. As of August 31, 2026 he holds no championship "
        "and is the most dangerous unresolved thread on SmackDown.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("9",        "Day world title reign"),
            ("4&times;", "Intercontinental"),
            ("2&times;", "United States"),
            ("1",        "Tag title, with Owens"),
            ("5.0",      "Stars, twice (Meltzer)"),
            ("2002",     "First match"),
        ],
        lead=("Eighteen documented bouts &mdash; the NXT title change in each direction, the Bloodline "
              "arc, the WrestleMania 40 win over Gunther, both United States reigns, and the "
              "nine-day world title bracketed by the two matches that created and ended it. This is a "
              "curated ledger, not a career count, and no career win&ndash;loss total is published "
              "because no verified one exists. Filter by match type, tap any column header to sort, "
              "and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The rated peaks, as reproduced in published Observer round-ups &mdash; two "
                    "five-star matches sixteen months apart, and the NXT-era classics that made his "
                    "name. Ratings are as reported, not re-checked against archives."),
    signature=[
        dict(rating="5.0", event="WrestleMania 40 Night 1", opponent="Gunther",
             stip="Intercontinental Championship — the 666-day reign ends"),
        dict(rating="5.0", event="WrestleMania 39 Night 1", opponent="The Usos",
             stip="Undisputed Tag Team Championship, with Kevin Owens — the main event"),
        dict(rating="4.75", event="NXT TakeOver: R Evolution", opponent="Adrian Neville",
             stip="NXT Championship — title or quit"),
        dict(rating="4.5", event="NXT TakeOver: Dallas", opponent="Shinsuke Nakamura",
             stip="Nakamura's WWE debut — the send-off match of the NXT era"),
        dict(rating="4.5", event="Battleground 2016", opponent="Kevin Owens",
             stip="Singles — the definitive chapter of the WWE feud"),
    ],
    signature_count_word="five",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("1",        "World title reign"),
            ("4&times;", "Intercontinental"),
            ("2&times;", "United States"),
            ("13th",     "Grand Slam Champion"),
        ],
        lead=("One world title, nine days, and a full Grand Slam underneath it &mdash; completed the "
              "moment the world title landed, 24 years into the career. Independent reign dates are "
              "given where verified and counted where not."),
        rows=[
            dict(ic="U", name="Undisputed WWE Championship", count="1",
                 sub="June 27 &ndash; July 6, 2026 &middot; won from Cody Rhodes in a triple threat "
                     "also containing Gunther at Night of Champions in Riyadh, lost to CM Punk on Raw "
                     "in Chicago &middot; <b>9 days</b> &middot; first Arab and first Syrian world "
                     "champion in WWE history, and his Grand Slam completer"),
            dict(ic="I", name="WWE Intercontinental Championship", count="4",
                 sub="2020 &middot; won in a 3-on-1 handicap at Elimination Chamber, vacated during "
                     "his pandemic absence after 65 days &middot; 2020 &middot; won the ladder match "
                     "at Clash of Champions, lost to Big E on the Christmas Day SmackDown, 89 days "
                     "&middot; 2022 &middot; a 21-day reign WWE recognises as 13 &middot; "
                     "2024 &middot; def. Gunther at WrestleMania 40 Night 1, ending the record "
                     "666-day reign; lost to Bron Breakker at SummerSlam, <b>119 days</b>"),
            dict(ic="S", name="WWE United States Championship", count="2",
                 sub="2025 &middot; def. Solo Sikoa on the August 29 SmackDown, lost to Ilja Dragunov "
                     "on October 17 &middot; 49 days &middot; 2026 &middot; def. Carmelo Hayes on the "
                     "March 27 SmackDown, lost to Trick Williams at WrestleMania 42 &middot; 23 days"),
            dict(ic="T", name="Undisputed WWE Tag Team Championship", count="1",
                 sub="April 1 &ndash; September 2, 2023, with Kevin Owens &middot; won from The Usos "
                     "in the WrestleMania 39 Night 1 main event, lost to The Judgment Day in a Steel "
                     "City Street Fight at Payback &middot; 154 days"),
            dict(ic="N", name="NXT Championship", count="1",
                 sub="December 11, 2014 &ndash; February 11, 2015 &middot; won from Adrian Neville at "
                     "TakeOver: R Evolution, lost to Kevin Owens at TakeOver: Rival &middot; 62 days"),
            dict(ic="P", name="PWG World Championship", count="2",
                 sub="As El Generico, 2007 and 2011 &middot; plus 5 PWG World Tag Team reigns "
                     "&middot; individual reign dates not verified in this pass"),
            dict(ic="R", name="ROH World Tag Team Championship", count="1",
                 sub="September 19, 2008 &ndash; April 10, 2009, with Kevin Steen &middot; plus the "
                     "ROH World Television Championship, June 26 &ndash; August 13, 2011"),
            dict(ic="W", name="wXw Unified World Wrestling Championship", count="1",
                 sub="May 19 &ndash; August 12, 2012, as El Generico"),
            dict(ic="K", name="KO-D Openweight Championship", count="1",
                 sub="September 30 &ndash; December 23, 2012, DDT Pro-Wrestling, Japan &middot; lost "
                     "to Kenny Omega &middot; plus 2 IWS World Heavyweight reigns at home in "
                     "Montreal, dates not verified"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="One partnership that predates the fame, and one infiltration that became the best "
             "long-form story WWE has told this decade.",
        cards=[
            dict(era="Independents &amp; WWE &middot; 2003&ndash;present",
                 name="Steen & Generico / Owens & Zayn",
                 members="Sami Zayn (El Generico), Kevin Owens (Kevin Steen)",
                 desc="Best friends since 2002-03, tag champions in ROH in 2008, blood enemies on "
                      "three continents in between. In WWE the cycle has run at least four full "
                      "revolutions: Owens' 2015 NXT betrayal, the 2016-17 wars, the 2023 reunion that "
                      "won the Undisputed Tag Team Championship at WrestleMania 39, the 2025 "
                      "unsanctioned match in Toronto - and now Zayn's own August 2026 belt-shot "
                      "betrayal, the first time the knife has gone in from his side."),
            dict(era="WWE &middot; 2022&ndash;2023",
                 name="The Bloodline",
                 members="Roman Reigns, Jey Uso, Jimmy Uso, Solo Sikoa, Sami Zayn (Honorary Uce)",
                 desc="Attached himself in May 2022 as a transparent sycophant, was declared Honorary "
                      "Uce in September, and slowly became the group's conscience - especially Jey "
                      "Uso's. It ended at the Royal Rumble on January 28, 2023, with a chair across "
                      "Roman Reigns' back in Montreal. Widely treated as the high-water mark of "
                      "modern WWE storytelling, and the reason the Elimination Chamber 2023 crowd "
                      "sounded like that."),
            dict(era="WWE &middot; 2026",
                 name="The Last Real Good Guy",
                 members="Sami Zayn, alone",
                 desc="The self-designation adopted in May 2026 for his self-styled 'Ride or Die' "
                      "fans - and, since the August 21 belt shot on Kevin Owens, an increasingly "
                      "ironic one. Not a stable: a man arguing with the definition of himself, in "
                      "public, on Friday nights."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Two identities across twenty-four years: <b>El Generico</b> (2002&ndash;2013) &rarr; "
             "<b>Sami Zayn</b> (2013&ndash;present). The first was a mask with a fake orphanage; the "
             "second turned out to be the more complicated character.",
        cards=[
            dict(mono="EG", era="Independents &middot; 2002&ndash;2013", name="El Generico",
                 desc="The masked 'generic luchador' with the Ole! chant, storyline proceeds to an "
                      "orphanage in Tijuana, and a genuinely world-class resume: PWG World Champion "
                      "twice, ROH tag champion with Kevin Steen, titles in Germany and Japan. The "
                      "mask 'retired to the orphanage' when WWE signed him in 2013 and has never "
                      "officially been acknowledged since."),
            dict(mono="UD", era="NXT &amp; WWE &middot; 2013&ndash;2022", name="The Underdog from the Underground",
                 desc="The unmasked babyface: NXT Champion in 2014, three Intercontinental reigns, "
                      "and a decade of being the most sympathetic man on the card - interrupted by a "
                      "2019-21 heel stretch as a conspiracy-theorist documentarian. The version every "
                      "later turn trades against."),
            dict(mono="HU", era="WWE &middot; 2022&ndash;2023", name="The Honorary Uce",
                 desc="The Bloodline infiltration - part comedy, part tragedy, entirely his. It won "
                      "him the 2022 awards-season sweep for storyline of the year and set up the "
                      "Montreal title match and the WrestleMania 39 tag title win with Owens."),
            dict(mono="RG", era="WWE &middot; 2026&ndash;present", name="The Last Real Good Guy",
                 desc="Adopted in May 2026 after losing the United States title at WrestleMania 42; "
                      "vindicated, briefly, by the Riyadh title win; and curdling since the nine-day "
                      "reign ended. The belt shot on Owens on August 21, 2026 is the hinge WWE has "
                      "not yet named a heel turn out loud."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="A mask in a Montreal loft to the Undisputed WWE Championship, the long way.",
        rows=[
            dict(year="2002", title="Debut in Quebec",
                 desc="First matches at seventeen; within a year he is El Generico, the masked "
                      "mainstay of Montreal's IWS."),
            dict(year="2008", title="ROH tag champion with Kevin Steen",
                 desc="Wins the ROH World Tag Team Championship on September 19 - the first title in "
                      "the twenty-year Steen/Owens double act."),
            dict(year="2013", title="Signs with WWE; the mask retires",
                 desc="El Generico 'returns to the orphanage'; Rami Sebei becomes Sami Zayn in NXT."),
            dict(year="2014", title="NXT Champion",
                 desc="Beats Adrian Neville at TakeOver: R Evolution on December 11 in a title-or-quit "
                      "match; Kevin Owens turns on him the same night, and takes the title at "
                      "TakeOver: Rival seven weeks later."),
            dict(year="2016", title="The Nakamura send-off and the Owens war",
                 desc="The TakeOver: Dallas match with Shinsuke Nakamura on April 1 and the "
                      "Battleground singles with Owens on July 24 - both rated 4.5 - bracket his move "
                      "to the main roster."),
            dict(year="2020", title="Two Intercontinental reigns",
                 desc="Wins the title at Elimination Chamber in March, vacates it during a pandemic "
                      "absence, and wins the ladder match at Clash of Champions in September."),
            dict(year="2022", title="The Honorary Uce",
                 desc="Attaches himself to The Bloodline in May; by WarGames in November he is the "
                      "story WWE television is organised around."),
            dict(year="2023", title="Montreal, and the WrestleMania main event",
                 desc="Chairs Roman Reigns at the Royal Rumble on January 28, challenges him in "
                      "Montreal at Elimination Chamber on February 18, and wins the Undisputed Tag "
                      "Team Championship with Owens in the WrestleMania 39 Night 1 main event on "
                      "April 1."),
            dict(year="2024", title="Ends the 666 days",
                 desc="Beats Gunther in the opening match of WrestleMania 40 Night 1 on April 6 - "
                      "five stars, and the reign-ender WWE had spent two years building. Loses the "
                      "title to Bron Breakker at SummerSlam on August 3."),
            dict(year="2025", title="United States Champion; the Owens floor",
                 desc="Loses an unsanctioned match to Owens at Elimination Chamber in Toronto on "
                      "March 1, before Owens' neck injury freezes the feud. Wins his first United "
                      "States Championship from Solo Sikoa on August 29."),
            dict(year="2026", title="The miracle in Riyadh, nine days, and the turn",
                 desc="Loses a title shot at Drew McIntyre at the Royal Rumble on January 31; wins "
                      "and loses a second US title in the spring; rolls up Cody Rhodes at Night of "
                      "Champions on June 27 for the Undisputed WWE Championship; loses it to CM Punk "
                      "on July 6; and on August 21 turns the belt on Kevin Owens."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Kevin Owens", slug="kevin-owens",
                 desc="The career-length one. Best friends since 2002-03, ROH tag champions, then the "
                      "2015 NXT betrayal that Owens authored and a decade of wars and reunions - "
                      "WrestleMania 39 tag champions in 2023, an unsanctioned match in Toronto in "
                      "2025 that Owens won before a neck injury shelved him. In August 2026 Zayn "
                      "finally reversed the polarity: at SummerSlam Owens pinned him in the four-way, "
                      "and on August 21 Zayn hit him with the title belt and cost him the "
                      "championship. Twenty-three years in, the roles have swapped for the first "
                      "time."),
            dict(name="Roman Reigns and The Bloodline",
                 desc="The 2022-23 infiltration story: sycophant to Honorary Uce to conscience to "
                      "traitor, ending with a chair shot at the Royal Rumble and a title match in "
                      "his own Montreal at Elimination Chamber on February 18, 2023 that he lost to "
                      "the loudest crowd of the era. It rehabilitated long-form storytelling in WWE "
                      "and made Jey Uso's later face turn possible."),
            dict(name="Gunther", slug="gunther",
                 desc="Two title matches, one immortal: Zayn ended Gunther's 666-day "
                      "Intercontinental Championship reign in the opener of WrestleMania 40 Night 1 "
                      "on April 6, 2024, a five-star match built on two years of the belt feeling "
                      "unwinnable. Gunther was also the third man in Riyadh when Zayn won the world "
                      "title, and one of the four he outlasted arguments with in the August 2026 "
                      "contender picture."),
            dict(name="CM Punk", slug="cm-punk",
                 desc="The nine-day grudge. Punk beat him for the Undisputed WWE Championship on the "
                      "July 6, 2026 Raw in Chicago - 'clean,' as Punk put it - and Zayn has treated "
                      "the loss as a theft ever since, attacking Punk after the August 21 Owens "
                      "match and brawling with him through the August 28 contender chaos. The next "
                      "singles match between them is the most obvious unbooked main event in WWE."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Beyond",
        lead="The most consequential item here is a fleet of mobile clinics.",
        rows=[
            dict(when="2017&ndash;", title="Sami for Syria", kind="Charity",
                 desc="His fund with the Syrian American Medical Society backing a mobile medical "
                      "clinic in Syria - over $105,000 raised by mid-2018, and still the cause he "
                      "fronts. He is the son of Syrian immigrants and speaks Arabic, English and "
                      "French."),
            dict(when="2015&ndash;", title="WWE 2K", kind="Game",
                 desc="Playable across the WWE 2K series since his NXT years. El Generico has never "
                      "appeared in a WWE game."),
            dict(when="2022&ndash;23", title="The Bloodline story press cycle", kind="Coverage",
                 desc="The Honorary Uce run drew mainstream sports-media coverage rare for a "
                      "non-champion, and swept storyline-of-the-year honours for 2022."),
            dict(when="2026", title="Post-title-loss promo", kind="Television",
                 desc="The July 6 promo after losing to CM Punk - carried by Fox News and others for "
                      "its unbleeped fury - is the pivot point of the current character. No film or "
                      "scripted TV roles, no autobiography and no podcast could be verified, so none "
                      "are listed."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records and the milestones, including the ones the nine days cannot take back.",
        stats=[
            ("1st", "Arab WWE world champion"),
            ("9",   "Day world title reign"),
            ("2",   "Five-star matches"),
        ],
        rows=[
            dict(name="First Arab and first Syrian world champion in WWE history",
                 sub="Won June 27, 2026 at Night of Champions in Riyadh. Coverage also noted he is "
                     "the first Muslim WWE world champion since The Iron Sheik in 1983-84."),
            dict(name="Grand Slam Champion",
                 sub="Completed by the Undisputed WWE Championship win, on top of the "
                     "Intercontinental (4 reigns), United States (2) and Undisputed Tag Team (1) "
                     "titles."),
            dict(name="Ended the longest Intercontinental Championship reign ever",
                 sub="Gunther's 666 days, at WrestleMania 40 Night 1 on April 6, 2024 - a five-star "
                     "match and the win his singles career is most identified with."),
            dict(name="Two five-star matches in sixteen months",
                 sub="The WrestleMania 39 Night 1 tag main event with Kevin Owens against The Usos "
                     "(April 1, 2023) and the WrestleMania 40 Gunther match (April 6, 2024), as "
                     "Observer round-ups reproduce the ratings."),
            dict(name="A world title 24 years after his debut",
                 sub="First match March 2002; first world championship June 27, 2026, at age 41 - "
                     "among the longest waits to a first world title of any WWE champion."),
            dict(name="The nine-day reign",
                 sub="June 27 to July 6, 2026. Short, but not the record - WWE world reigns have "
                     "ended inside an hour, including Drew McIntyre's 5-minute-46-second World "
                     "Heavyweight reign in 2024. The number to hold onto is 24 years up, nine days "
                     "at the top."),
            dict(name="Main-evented WrestleMania Night 1",
                 sub="April 1, 2023, winning the Undisputed WWE Tag Team Championship with Kevin "
                     "Owens from The Usos - the first tag title match to main-event a WrestleMania "
                     "night in the modern era."),
            dict(name="NXT Championship, title or quit",
                 sub="Beat Adrian Neville at TakeOver: R Evolution on December 11, 2014 under a "
                     "stipulation that would have ended his NXT title pursuit - rated 4.75, and the "
                     "night the Owens betrayal began."),
        ],
        footnote=("Deliberately absent: a career win-loss total, because no verified figure exists; "
                  "the July 18, 2026 Saturday Night's Main Event tag result, which could not be "
                  "confirmed; and any claim that WWE has formally labelled the August 21 belt shot a "
                  "heel turn - the behaviour is documented, the label is not."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography",
             href="https://en.wikipedia.org/wiki/Sami_Zayn"),
        dict(k="Fox News", v="Wins the Undisputed WWE Championship at Night of Champions",
             href="https://www.foxnews.com/sports/sami-zayn-shocks-wrestling-world-pulls-off-miracle-win-undisputed-wwe-championship-night-champions"),
        dict(k="Fightful", v="CM Punk on beating Zayn 'fair and square,' July 2026",
             href="https://www.fightful.com/wrestling/cm-punk-discusses-beating-sami-zayn-for-undisputed-wwe-title-i-beat-that-41-year-old-youngster-fair-square/"),
        dict(k="F4W/WON", v="The August 21 belt shot on Kevin Owens",
             href="https://www.f4wonline.com/news/wwe/result-cm-punk-vs-kevin-owens-wwe-title-match-smackdown/"),
        dict(k="Last Word on Sports", v="The August 28 No. 1 contender chaos",
             href="https://lastwordonsports.com/prowrestling/2026/08/24/wwe-smackdown-spoilers-8-28-new-undisputed-wwe-champion-1-contender-crowned/"),
        dict(k="IWNerd", v="Observer ratings, WrestleMania 39",
             href="https://www.iwnerd.com/dave-meltzer-star-ratings-wrestlemania-39-2023/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="How did Sami Zayn win the Undisputed WWE Championship, and how long did he hold it?",
            a="He won it on June 27, 2026 at Night of Champions in Riyadh, in a triple threat with "
              "defending champion <b>Cody Rhodes</b> and Gunther &mdash; slipping out of a Cross "
              "Rhodes and rolling Rhodes up for the pin, a finish Michael Cole called &ldquo;a "
              "miracle in Riyadh.&rdquo; It was his first world title in a career that began in "
              "2002. He held it <b>nine days</b>: CM Punk beat him on the July 6 Raw at the Allstate "
              "Arena in Chicago. Note the common error &mdash; he beat Rhodes, not Gunther, for the "
              "title.",
            q_ld="How did Sami Zayn win the Undisputed WWE Championship and how long did he hold it?",
            a_ld="Sami Zayn won the Undisputed WWE Championship on June 27, 2026 at Night of "
                 "Champions in Riyadh, Saudi Arabia, pinning defending champion Cody Rhodes with a "
                 "rollup in a triple threat match that also included Gunther. It was his first world "
                 "championship in a career that began in 2002. He held the title for nine days, "
                 "losing it to CM Punk on the July 6, 2026 episode of Raw at the Allstate Arena near "
                 "Chicago."),
        dict(
            q="Did Sami Zayn turn heel on Kevin Owens?",
            a="The actions are on tape; WWE has not used the word. On the August 2, 2026 SummerSlam "
              "four-way, Owens pinned Zayn to become No. 1 contender. On the <b>August 21 "
              "SmackDown</b>, during Owens&rsquo; title match with CM Punk, Zayn urged Owens to use "
              "the belt as a weapon, Owens refused &mdash; and Zayn hit Owens with it himself, "
              "handing Punk the win, then attacked both men and declared the title rightfully his. "
              "On August 28 he wrecked the No. 1 contender triple threat and struck the referee. "
              "After twenty-three years of Owens being the betrayer in this friendship, the knife "
              "has changed hands.",
            q_ld="Did Sami Zayn turn heel on Kevin Owens in 2026?",
            a_ld="Sami Zayn attacked Kevin Owens with the championship belt during Owens' Undisputed "
                 "WWE Championship match against CM Punk on the August 21, 2026 SmackDown, after "
                 "Owens refused Zayn's urging to use the belt as a weapon. The interference cost "
                 "Owens the match, and Zayn then attacked both Owens and Punk and declared the title "
                 "rightfully his. On the August 28 SmackDown Zayn disrupted the No. 1 contender "
                 "triple threat and struck the referee. WWE has not formally announced a heel turn, "
                 "but the August 21 attack reversed the dynamic of a friendship-and-betrayal story "
                 "the two men have told since 2015, in which Owens had always been the betrayer."),
        dict(
            q="Who was El Generico?",
            a="Sami Zayn, masked &mdash; though neither he nor WWE has ever quite said so on the "
              "record. From 2002 to 2013 he wrestled as El Generico, a &ldquo;generic&rdquo; masked "
              "luchador whose storyline earnings supported an orphanage in Tijuana. The resume under "
              "the mask was elite: two PWG World Championships, the ROH World Tag Team Championship "
              "with Kevin Steen (now Kevin Owens), a wXw title in Germany and DDT&rsquo;s KO-D "
              "Openweight Championship in Japan, lost to Kenny Omega. When WWE signed him in 2013 "
              "the character &ldquo;retired to the orphanage,&rdquo; and Rami Sebei debuted "
              "unmasked as Sami Zayn.",
            q_ld="Who was El Generico and what happened to him?",
            a_ld="El Generico was the masked ring persona Sami Zayn (real name Rami Sebei) used from "
                 "2002 to 2013 on the independent circuit. The character was a generic masked "
                 "luchador whose storyline earnings supported an orphanage in Tijuana. As El "
                 "Generico he won the PWG World Championship twice, the ROH World Tag Team "
                 "Championship with Kevin Steen, wXw's Unified World Wrestling Championship in "
                 "Germany and DDT's KO-D Openweight Championship in Japan. When WWE signed him in "
                 "2013 the character was retired, and he has performed unmasked as Sami Zayn since."),
        dict(
            q="Is Sami Zayn a Grand Slam Champion?",
            a="Yes, as of June 27, 2026. The Undisputed WWE Championship completed the set on top of "
              "four Intercontinental Championship reigns, two United States Championship reigns and "
              "the Undisputed WWE Tag Team Championship he held with Kevin Owens in 2023. The world "
              "title also made him the first Arab and first Syrian world champion in WWE history.",
            q_ld="Is Sami Zayn a Grand Slam Champion in WWE?",
            a_ld="Yes. Sami Zayn completed WWE's Grand Slam on June 27, 2026 when he won the "
                 "Undisputed WWE Championship, adding a world title to his four Intercontinental "
                 "Championship reigns, two United States Championship reigns and one Undisputed WWE "
                 "Tag Team Championship reign with Kevin Owens. The win also made him the first Arab "
                 "and first Syrian world champion in WWE history."),
        dict(
            q="What is Sami Zayn&rsquo;s history with The Bloodline?",
            a="He talked his way in as a hanger-on in May 2022, was formally declared the "
              "&ldquo;Honorary Uce&rdquo; that September, and spent months as the group&rsquo;s "
              "comic relief and then its conscience. It ended when he hit Roman Reigns with a chair "
              "at the Royal Rumble on January 28, 2023 rather than help beat down Kevin Owens. The "
              "payoffs: the Elimination Chamber title match in his own Montreal on February 18, 2023 "
              "&mdash; a loss with the loudest crowd of the decade &mdash; and the WrestleMania 39 "
              "Night 1 main event on April 1, 2023, where he and Owens took the tag titles from The "
              "Usos.",
            q_ld="What is Sami Zayn's history with The Bloodline?",
            a_ld="Sami Zayn attached himself to The Bloodline in May 2022 and was declared the "
                 "group's Honorary Uce by Roman Reigns in September 2022. He left by attacking "
                 "Reigns with a chair at the Royal Rumble on January 28, 2023. He then challenged "
                 "Reigns for the Undisputed WWE Universal Championship in his hometown of Montreal "
                 "at Elimination Chamber on February 18, 2023 and lost, and won the Undisputed WWE "
                 "Tag Team Championship with Kevin Owens from The Usos in the main event of "
                 "WrestleMania 39 Night 1 on April 1, 2023."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Rami Sebei"),
        dict(label="Born", value="July 12, 1984", sub="Laval, Quebec, Canada &middot; age 42 "
                                                      "&middot; Syrian parents"),
        dict(label="Billed from", value="Montreal, Quebec, Canada"),
        dict(label="Height", value="6&#8242;1&#8243;", sub="185 cm"),
        dict(label="Weight", value="212 lb", sub="96 kg (billed)"),
        dict(label="Debut", value="March 1, 2002", sub="Quebec independents, at seventeen"),
        dict(label="Ring names", value="El Generico &rarr; Sami Zayn",
             sub="2002&ndash;13 &middot; 2013&ndash;present &mdash; briefly Stevie McFly in 2002"),
        dict(label="Signature", value="Helluva Kick &middot; Blue Thunder Bomb &middot; Exploder "
                                      "suplex into the turnbuckle"),
        dict(label="Brand", value="SmackDown"),
        dict(label="Languages", value="English &middot; Arabic &middot; French"),
        dict(label="Also known as",
             value="The Underdog from the Underground &middot; The Honorary Uce &middot; The Last "
                   "Real Good Guy"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1984-07-12",
    bornplace="Laval, Quebec, Canada",
    nationality="Canada",
    height_cm=185,
    weight_kg=96,
    ld=dict(
        alternateName=["Rami Sebei", "El Generico", "The Underdog from the Underground",
                       "The Honorary Uce", "The Last Real Good Guy"],
        award=["Undisputed WWE Championship (1 reign, 9 days, 2026)",
               "WWE Intercontinental Championship (4 reigns)",
               "WWE United States Championship (2 reigns)",
               "Undisputed WWE Tag Team Championship (1 reign, with Kevin Owens)",
               "NXT Championship (1 reign)",
               "WWE Grand Slam Champion (2026)",
               "PWG World Championship (2 reigns, as El Generico)",
               "ROH World Tag Team Championship (1 reign, with Kevin Steen)",
               "ROH World Television Championship (1 reign)",
               "wXw Unified World Wrestling Championship (1 reign)",
               "KO-D Openweight Championship (1 reign)",
               "IWS World Heavyweight Championship (2 reigns)"],
        knowsAbout=["Professional wrestling", "WWE", "NXT", "The Bloodline", "Ring of Honor",
                    "Pro Wrestling Guerrilla", "Lucha libre", "Championship wrestling"],
        description="Sami Zayn, born Rami Sebei in Laval, Quebec, is a Canadian professional "
                    "wrestler of Syrian descent signed to WWE, formerly the masked independent star "
                    "El Generico. He won his first world championship, the Undisputed WWE "
                    "Championship, at Night of Champions on June 27, 2026 - becoming the first Arab "
                    "and first Syrian world champion in WWE history and completing the Grand Slam - "
                    "and lost it to CM Punk nine days later. He ended Gunther's record 666-day "
                    "Intercontinental Championship reign at WrestleMania 40 and was central to The "
                    "Bloodline storyline of 2022-23.",
        sameAs=["https://en.wikipedia.org/wiki/Sami_Zayn",
                "https://www.wwe.com/superstars/sami-zayn"],
    ),
)
