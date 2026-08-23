# -*- coding: utf-8 -*-
"""Gunther - dossier data.

Sources: /tmp/research/gunther.md (web-verified, compiled Aug 23 2026) and the harvest
of the previous /wrestlers/gunther/ page. Every match row carries a day-precision date
that appears in one of those two; the harvested "Dec 2021" row was month-precision only
and is omitted rather than guessed at.

Deliberate omissions:
  * No career win-loss total. The old page's own headline (94-18) disagreed with its own
    Win% (82% vs 84%) and with its own sparkline (86 marks / 6 losses), and the research
    file has no career total. Nothing is published rather than propagating a bad number.
  * No social links. The research file surfaced @gunther_aut vs @gunther_wwe (Instagram)
    and @Gunther_AUT vs @GuntherOfficial (X) and could not establish which of each pair is
    official. x_url/ig_url are omitted and the social rows are dropped from `reference`.
  * The Wikipedia summary figure of "August 3, 2024 - November 2, 2024 (92 days)" for the
    first World Heavyweight Championship reign is wrong and is not published anywhere here:
    Jey Uso took that title at WrestleMania 41 on April 19, 2025 (Forbes, CBS Sports,
    Cageside Seats, 411Mania, Fox).
"""

# ----------------------------------------------------------------- record rows
# 5 bouts reused from the harvest of the previous page (dates and one opponent corrected
# against the research file, which is the source of truth), 2 more taken from that page's
# own 2024 rows, and 10 whose dates and outcomes are stated explicitly in the research
# dossier. The harvested "vs. Ilja Dragunov, Dec 2021" row is dropped: it was dated to the
# month only, and it recorded a win in a match the research file records as his loss.
ROWS = [
    dict(result="W", date="2019-04-05", promo="WWE", landmark=True,
         event="NXT UK TakeOver: New York", opponent="Pete Dunne",
         stip="Singles — ends Dunne's 685-day reign", title="NXT United Kingdom Championship"),
    dict(result="L", date="2021-08-22", promo="WWE", landmark=True,
         event="NXT TakeOver 36", opponent="Ilja Dragunov",
         stip="Singles — ends the 870-day reign", title="NXT United Kingdom Championship"),
    dict(result="W", date="2022-06-10", promo="WWE", landmark=True,
         event="SmackDown", opponent="Ricochet",
         stip="Singles — the 666-day reign begins", title="WWE Intercontinental Championship"),
    dict(result="W", date="2022-09-03", promo="WWE", landmark=True,
         event="Clash at the Castle — Cardiff", opponent="Sheamus",
         stip="Singles — five stars (Meltzer)", title="WWE Intercontinental Championship"),
    dict(result="L", date="2024-04-06", promo="WWE", landmark=True,
         event="WrestleMania 40 Night 1", opponent="Sami Zayn",
         stip="Singles — the 666-day reign ends", title="WWE Intercontinental Championship"),
    dict(result="W", date="2024-06-15", promo="WWE",
         event="Clash at the Castle: Scotland", opponent="Drew McIntyre",
         stip="Singles", title=""),
    dict(result="L", date="2024-07-06", promo="WWE",
         event="Money in the Bank", opponent="Damian Priest",
         stip="Singles — challenge", title="World Heavyweight Championship"),
    dict(result="W", date="2024-08-03", promo="WWE", landmark=True,
         event="SummerSlam — Cleveland", opponent="Damian Priest",
         stip="Singles — first world title", title="World Heavyweight Championship"),
    dict(result="L", date="2025-04-19", promo="WWE", landmark=True,
         event="WrestleMania 41 Night 1", opponent="Jey Uso", opponent_html=True,
         stip="Singles — submission; ends a 259-day reign", title="World Heavyweight Championship"),
    dict(result="W", date="2025-06-09", promo="WWE", landmark=True,
         event="Raw", opponent="Jey Uso", opponent_html=True,
         stip="Singles — second world title", title="World Heavyweight Championship"),
    dict(result="W", date="2025-07-12", promo="WWE", landmark=True,
         event="Saturday Night's Main Event XL — Atlanta", opponent="Goldberg",
         stip="Goldberg's retirement match", title=""),
    dict(result="L", date="2025-08-02", promo="WWE", landmark=True,
         event="SummerSlam Night 1", opponent="CM Punk", opponent_html=True,
         stip="Singles — 54-day reign ends; broken nose", title="World Heavyweight Championship"),
    dict(result="W", date="2025-12-13", promo="WWE", landmark=True,
         event="Saturday Night's Main Event", opponent="John Cena", opponent_html=True,
         stip="Cena's final match — Cena gave up", title=""),
    dict(result="W", date="2026-01-31", promo="WWE", landmark=True,
         event="Royal Rumble — Riyadh", opponent="AJ Styles", opponent_html=True,
         stip="Styles' retirement match", title=""),
    dict(result="L", date="2026-01-31", promo="WWE", type="tag",
         event="Royal Rumble match — Riyadh", opponent="The 2026 Royal Rumble field",
         stip="Entered No. 30, last man eliminated", title=""),
    dict(result="L", date="2026-06-27", promo="WWE", type="tag",
         event="Night of Champions — Riyadh", opponent="Sami Zayn & Cody Rhodes",
         stip="Triple threat — Zayn retains", title="Undisputed WWE Championship"),
    dict(result="W", date="2026-08-01", promo="WWE",
         event="SummerSlam Night 1 — Minneapolis", opponent="Nick Aldis",
         stip="Grudge match — rear-naked choke", title=""),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Jey Uso": "jey-uso", "CM Punk": "cm-punk", "John Cena": "john-cena",
                 "AJ Styles": "aj-styles"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="gunther",
    name="Gunther",
    realname="Walter Hahn",
    epithet="The Ring General",
    hook="Record & Titles",

    meta_desc=("Gunther, The Ring General, held the WWE Intercontinental Championship for a record "
               "666 days and the NXT United Kingdom Championship for 870. Full record, titles, "
               "factions, records and career."),
    og_desc=("The Ring General: a 666-day Intercontinental Championship reign, 870 days with the NXT "
             "UK title, two world championships and the longest Royal Rumble survival time ever."),
    tw_desc="The Ring General: 666 days as Intercontinental Champion, 870 as NXT UK Champion.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2005",
    height_imp="6&#8242;4&#8243;",
    weight_lb="250",
    world_titles="2",
    vitals_tagline="Die Matte ist heilig",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="GU", title="WWE Shop", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable in 2K22 through 2K26",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="wXw", title="wXw Wrestling Academy", sub="Head trainer, 2015–2020",
             tag="Visit", href="https://www.wxw-wrestling.com/"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/gunther"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Der Ringgeneral &middot; The Career Killer &middot; formerly WALTER",
    hero_tag="Vienna, Austria &middot; <em>wXw &middot; PROGRESS &middot; NXT UK &middot; WWE &middot; 2005&ndash;present</em>",
    now_label="NOW",
    now_bold="SmackDown, no championship",
    now_tail=" &middot; pointed at the Undisputed WWE Championship after choking out Nick Aldis at SummerSlam",
    hstats=[
        dict(value="666", x=False, label="Day IC Reign"),
        dict(value="870", x=False, label="Day NXT UK Reign"),
        dict(value="2",   x=True,  label="World Titles"),
        dict(value="3",   x=False, label="Careers Ended"),
    ],
    ghost_link="From Bern, 2005, to the longest reign the belt has ever had",
    vlabel="Est. 2005 &middot; Vienna, Austria",
    mono="GU",

    # ---------------------------------------------------------------- 01 overview
    overview=[
        "<b>Gunther</b> held the WWE Intercontinental Championship for 666 days, and almost everything "
        "else about him follows from that. He is a 6&#8242;4&#8243; Austrian who wrestles a European "
        "catch style built on knife-edge chops and submissions, who spent thirteen years on the "
        "independents as Big Van Walter, Big Daddy Walter and then WALTER before WWE renamed him, and "
        "who has been booked since 2024 as the wall that other careers end against. He is a two-time "
        "World Heavyweight Champion, the 2024 King of the Ring, and the holder of the longest survival "
        "time in Royal Rumble history at 71 minutes 25 seconds. He is <i>not</i> a Triple Crown or Grand "
        "Slam champion &mdash; he has never held a WWE tag team or United States title &mdash; and that "
        "gap is the shape of the career: one belt, held for an unreasonable length of time.",

        "The line you will read everywhere is that he &ldquo;broke The Honky Tonk Man&rsquo;s all-time "
        "Intercontinental record.&rdquo; That record did not exist. Honky Tonk Man held the longest "
        "<b>single reign</b> &mdash; 454 days from June 1987 to August 1988, logged by Wikipedia as 454 "
        "held and 453 as WWE recognises it. The record for the <b>most total days</b> belonged to "
        "<b>Pedro Morales</b>, who put together 619 days across two reigns between December 1980 and "
        "January 1983. Two records, two men, and Gunther passed them at two different moments inside the "
        "same run: Honky Tonk Man&rsquo;s mark in September 2023 at 455 days, on the Raw where he "
        "defended against Chad Gable (CBS Sports), and Morales&rsquo;s 619 combined days later in the "
        "same reign (SEScoops). The reign itself ran June 10, 2022 to April 6, 2024 &mdash; <b>666 "
        "days</b> &mdash; and that is one of the few numbers on this page with no conflict at all behind "
        "it: WWE.com&rsquo;s own profile and Wikipedia state it identically. The other common framing, a "
        "&ldquo;35-year-old record,&rdquo; measures from when Honky Tonk Man&rsquo;s reign ended, not "
        "from when it was set.",

        "He was born Walter Hahn on August 20, 1987 in Vienna and debuted at eighteen, on November 19, "
        "2005 in Bern, Switzerland, trained by Michael Kovac &mdash; Wikipedia also credits Riki Choshu, "
        "Tatsuhito Takaiwa and Tomohiro Ishii, which is where the strong-style edge in the work comes "
        "from. He won wXw&rsquo;s 16 Carat Gold tournament in 2010 at twenty-two, the youngest winner at "
        "the time, took the wXw Unified World Wrestling Championship three times and the tag titles four, "
        "and ran the wXw Wrestling Academy as head trainer from 2015 to 2020. Then came the run that "
        "moved him: as WALTER he beat Pete Dunne at NXT UK TakeOver: New York on April 5, 2019, ending "
        "Dunne&rsquo;s 685-day reign, and kept the NXT United Kingdom Championship for <b>870 days</b> "
        "until Ilja Dragunov beat him at NXT TakeOver 36 on August 22, 2021. That was the longest reign "
        "of any WWE championship in the modern era &mdash; until Roman Reigns&rsquo; second Universal "
        "Championship reign passed it in January 2023, a caveat almost every retelling drops.",

        "Since 2024 he has been the gatekeeper. He beat Damian Priest for the World Heavyweight "
        "Championship at SummerSlam on August 3, 2024 and held it 259 days until Jey Uso made him tap at "
        "WrestleMania 41 on April 19, 2025; he took it back on the June 9, 2025 Raw and lost it to CM "
        "Punk at SummerSlam on August 2, 2025 after 54 days, working the finish with a broken nose that "
        "cost him roughly two months. WWE then handed him three retirements in seven months &mdash; "
        "Goldberg, John Cena and AJ Styles &mdash; and the &ldquo;Career Killer&rdquo; framing its own "
        "profile now leads with. He turned 39 in August 2026 and is currently without a title, working "
        "<b>SmackDown</b>: WWE.com&rsquo;s profile summary still lists him on Raw, but the 2026 booking "
        "&mdash; the Night of Champions triple threat, the feud with SmackDown general manager Nick "
        "Aldis, the August 21 backstage segment with Kevin Owens and Finn B&aacute;lor &mdash; is "
        "SmackDown throughout, so this page follows the booking and flags the lag.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("666",    "Day IC reign"),
            ("870",    "Day NXT UK reign"),
            ("2&times;", "World Heavyweight"),
            ("71:25",  "Royal Rumble iron man"),
            ("3",      "Careers ended"),
            ("1",      "King of the Ring"),
        ],
        lead=("Seventeen documented bouts &mdash; the two record reigns at both ends, the world title "
              "changes and the three retirement matches. This is a curated ledger, not a career count, "
              "and no career win&ndash;loss total is published: the previous version of this page carried "
              "a 94&ndash;18 headline that disagreed with its own 82% win rate and with its own "
              "sparkline, and the research file has no verified total to replace it with. Two 2024 rows "
              "(Clash at the Castle: Scotland and Money in the Bank) come from that older page rather "
              "than the research dossier; the Scotland bout is listed without a title, because Damian "
              "Priest held the World Heavyweight Championship on that date. Filter by match type, tap any "
              "column header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the reputation rests on. Wikipedia credits him with five Dave Meltzer "
                    "five-star matches, four of them in WWE, and names these three among them &mdash; a "
                    "single-sourced count that could not be corroborated against Observer archives, so "
                    "read the ratings as reported rather than confirmed."),
    signature=[
        dict(rating="5.0", event="Clash at the Castle 2022 — Cardiff", opponent="Sheamus",
             stip="WWE Intercontinental Championship"),
        dict(rating="5.0", event="WrestleMania 39", opponent="Sheamus & Drew McIntyre",
             stip="Intercontinental Championship — triple threat"),
        dict(rating="5.0", event="WrestleMania 40 Night 1", opponent="Sami Zayn",
             stip="Intercontinental Championship — the 666-day reign ends"),
        dict(rating="4.5", event="NXT TakeOver 36", opponent="Ilja Dragunov",
             stip="NXT United Kingdom Championship — the 870-day reign ends"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("2&times;", "World title reigns"),
            ("666",      "Day IC reign"),
            ("870",      "Day NXT UK reign"),
            ("0",        "Tag or US titles"),
        ],
        lead=("Nine championships, seventeen reigns, and a conspicuous hole where the tag team and "
              "United States titles would be &mdash; which is why he is neither a Triple Crown nor a "
              "Grand Slam champion, a thing frequently assumed about him. Independent reign lengths and "
              "exact dates were not verified in this pass and are not invented here."),
        rows=[
            dict(ic="I", name="WWE Intercontinental Championship", count="1",
                 sub="June 10, 2022 &ndash; April 6, 2024 &middot; def. Ricochet on SmackDown, lost to "
                     "Sami Zayn at WrestleMania 40 Night 1 &middot; <b>666 days</b>, the longest reign in "
                     "the title&rsquo;s history &middot; first Austrian to hold it"),
            dict(ic="U", name="NXT United Kingdom Championship", count="1",
                 sub="April 5, 2019 &ndash; August 22, 2021 &middot; def. Pete Dunne at TakeOver: New "
                     "York, lost to Ilja Dragunov at TakeOver 36 &middot; <b>870 days</b> per WWE.com "
                     "&middot; a Wikipedia summary gives April 4, 2019 &ndash; August 31, 2021, which "
                     "does not produce 870; the April 5 / August 22 endpoints do, exactly"),
            dict(ic="H", name="World Heavyweight Championship", count="2",
                 sub="2024&ndash;25 &middot; def. Damian Priest at SummerSlam, lost to Jey Uso at "
                     "WrestleMania 41 &mdash; 259 days, computed from those dates rather than cited "
                     "&middot; 2025 &middot; def. Jey Uso on Raw, lost to CM Punk at SummerSlam Night 1 "
                     "&mdash; 54 days"),
            dict(ic="W", name="wXw Unified World Wrestling Championship", count="3",
                 sub="Germany&rsquo;s flagship heavyweight title &middot; individual reign dates not "
                     "verified in this pass"),
            dict(ic="T", name="wXw World Tag Team Championship", count="4",
                 sub="His only tag championships anywhere &middot; reign dates not verified"),
            dict(ic="P", name="PROGRESS World Championship", count="1",
                 sub="The London promotion that styled the name in all caps &mdash; WALTER &middot; "
                     "reign dates not verified"),
            dict(ic="A", name="PROGRESS Atlas Championship", count="3",
                 sub="PROGRESS&rsquo;s heavyweight-division title &middot; reign dates not verified"),
            dict(ic="O", name="OTT World Championship", count="1",
                 sub="Over the Top Wrestling, Ireland &middot; reign dates not verified"),
            dict(ic="G", name="PWG World Championship", count="1",
                 sub="Pro Wrestling Guerrilla, California &middot; reign dates not verified"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Two units and one philosophy &mdash; the European group that produced the character, and "
             "the WWE group that protected the reigns.",
        cards=[
            dict(era="Independents &middot; 2016&ndash;2019",
                 name="Ringkampf",
                 members="WALTER, Axel Dieter Jr., Timothy Thatcher (associated)",
                 desc="The German-Austrian unit Imperium grew out of, built with Axel Dieter Jr. — later "
                      "Ludwig Kaiser. Its identity was an argument rather than a gimmick: European "
                      "catch-style, no theatrics, respect for the sport, and “die Matte ist "
                      "heilig” — the mat is sacred. That is a shoot position he still states in "
                      "interviews, and it is the philosophy the WWE character is a straight translation "
                      "of."),
            dict(era="WWE &middot; 2019&ndash;2024",
                 name="Imperium",
                 members="Gunther (WALTER), Ludwig Kaiser (Marcel Barthel), Giovanni Vinci (Fabian "
                         "Aichner), Alexander Wolfe",
                 desc="Debuted May 22, 2019 on NXT UK, when WALTER beat Pete Dunne with Barthel and "
                      "Aichner interfering. Functionally it was a protection racket for his title "
                      "reigns: it covered the ring during the 870-day NXT UK run and again through the "
                      "666-day Intercontinental run, while Kaiser and Aichner took the NXT Tag Team "
                      "Championship twice. Wolfe was out by May 18, 2021; Vinci was gone by April 22, "
                      "2024. It dissolved with no on-air announcement at all after a final appearance "
                      "together on the December 23, 2024 Raw. Gunther kept the entrance music."),
            dict(era="WWE &middot; 2022&ndash;present",
                 name="The Ring General era",
                 members="Gunther, alone",
                 desc="Not a stable — a designation, and the absence of one. Since Imperium ended he has "
                      "been booked as a singles act with no seconds, and he has said publicly (Fightful, "
                      "Wrestling Inc.) that he has worked alone for most of his career and prefers it. "
                      "Ludwig Kaiser has discussed in interviews who suggested the split. Reunion teases "
                      "have come and gone, including one in the NXT era at Clash at the Castle, but no "
                      "reunion has actually happened as of August 2026."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Four ring names in twenty-one years, and only one of them was invented by a wrestling "
             "company: <b>Big Van Walter</b> (2005&ndash;2014) &rarr; <b>Big Daddy Walter</b> "
             "(2014&ndash;2018) &rarr; <b>WALTER</b> (2018&ndash;2022) &rarr; <b>Gunther</b> (2022&ndash;"
             "present). Walter is his legal first name. WWE did not create WALTER; it retired it.",
        cards=[
            dict(mono="BVW", era="Independents &middot; 2005&ndash;2014", name="Big Van Walter",
                 desc="The debut name on the European independents, an homage to Big Van Vader. Heavier, "
                      "slower, brawler-based — a long way from the sparse, technical act that came out "
                      "the other end."),
            dict(mono="BDW", era="wXw &amp; Europe &middot; 2014&ndash;2018", name="Big Daddy Walter",
                 desc="The transitional name, and the years when the chop-based, physically intimidating "
                      "style hardened into the thing people travelled to see. He founded Ringkampf in "
                      "the middle of it."),
            dict(mono="W", era="PROGRESS, PWG, NXT UK &middot; 2018&ndash;2022", name="WALTER",
                 desc="The name that made him internationally famous, styled in all caps by PROGRESS "
                      "branding — not an acronym and not a construction, just his actual first name. "
                      "PROGRESS, PWG and wXw first, then NXT UK from 2019 and an 870-day title reign."),
            dict(mono="RG", era="WWE &middot; 2022&ndash;present", name="Gunther, the Ring General",
                 desc="WWE renamed him in January 2022 on arrival to NXT 2.0. The footnote most bios "
                      "skip: the company trademarked the full name “Gunther Stark” on January "
                      "13, 2022 and abandoned it on January 19 after it emerged that Günther Stark "
                      "was a Nazi military commander (Cageside Seats, Sports Illustrated). He was never "
                      "billed with the surname on air. The character itself is authoritarian, "
                      "humourless and sport-first, and it is Ringkampf's argument with a bigger budget."),
            dict(mono="CK", era="WWE &middot; 2025&ndash;2026", name="The Career Killer",
                 desc="A layer added on top rather than a replacement — WWE.com's own profile now leads "
                      "on retiring legends. Goldberg, John Cena and AJ Styles all finished their careers "
                      "losing to him inside seven months."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Bern at eighteen to the longest Intercontinental Championship reign ever held.",
        rows=[
            dict(year="2005", title="Debut at eighteen",
                 desc="Debuts November 19, 2005 in Bern, Switzerland as Big Van Walter, trained by "
                      "Michael Kovac."),
            dict(year="2010", title="Wins wXw 16 Carat Gold",
                 desc="Takes Europe's most prestigious tournament at twenty-two, the youngest winner at "
                      "the time."),
            dict(year="2016", title="Founds Ringkampf",
                 desc="The “mat is sacred” unit with Axel Dieter Jr. that becomes the template "
                      "for Imperium and for the WWE character."),
            dict(year="2019", title="Beats Pete Dunne for the NXT UK Championship",
                 desc="April 5, 2019 at TakeOver: New York, ending Dunne's 685-day reign. Imperium "
                      "debuts on May 22."),
            dict(year="2021", title="The 870-day reign ends",
                 desc="Ilja Dragunov beats him at NXT TakeOver 36 on August 22, 2021, ending what was "
                      "then the longest WWE title reign of the modern era."),
            dict(year="2022", title="Renamed Gunther; wins the Intercontinental Championship",
                 desc="Renamed in January 2022, after WWE briefly trademarked “Gunther Stark” "
                      "and abandoned it within a week. Beats Ricochet on June 10, three months into the "
                      "SmackDown run."),
            dict(year="2023", title="Breaks the Intercontinental record; sets the Rumble record",
                 desc="Passes The Honky Tonk Man's 454-day single-reign mark in September 2023 at 455 "
                      "days, and later in the same reign passes Pedro Morales' 619 combined days. He "
                      "also lasts 71:25 in the January 2023 Royal Rumble, the longest ever."),
            dict(year="2024", title="The reign ends, then King of the Ring and a world title",
                 desc="Sami Zayn beats him at WrestleMania 40 Night 1 on April 6 after 666 days; he wins "
                      "King of the Ring, then beats Damian Priest for the World Heavyweight Championship "
                      "at SummerSlam on August 3."),
            dict(year="2025", title="Two world title losses and the Career Killer turn",
                 desc="Jey Uso submits him at WrestleMania 41 on April 19; he regains the title on the "
                      "June 9 Raw and loses it to CM Punk on August 2 with a broken nose. He retires "
                      "Goldberg on July 12 and John Cena on December 13."),
            dict(year="2026", title="Retires AJ Styles, chases the WWE title, beats the GM",
                 desc="Ends AJ Styles' career at the Royal Rumble on January 31, enters that Rumble at "
                      "No. 30 and is the last man Roman Reigns eliminates; loses the Undisputed WWE "
                      "Championship triple threat at Night of Champions on June 27; chokes out Nick "
                      "Aldis at SummerSlam on August 1."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Sheamus",
                 desc="The series that made the Intercontinental reign matter — two heavyweights hitting "
                      "each other with open hands in front of a Cardiff stadium at Clash at the Castle "
                      "on September 3, 2022, then the WrestleMania 39 triple threat with Drew McIntyre. "
                      "Both are among the small number of WWE matches Dave Meltzer has given five stars, "
                      "and together they argued that a chop-based, credibility-first match could headline "
                      "rather than fill a card."),
            dict(name="Sami Zayn",
                 desc="Zayn ended the 666 days in the opening match of WrestleMania 40 Night 1 on April "
                      "6, 2024, and the length of the reign was the entire dramatic engine: WWE spent "
                      "nearly two years making the belt feel unwinnable so that one man could win it. It "
                      "is the rare modern payoff built on patience instead of a swerve, and it remains "
                      "the most-cited Gunther match outside the Sheamus series. They met again in the "
                      "Night of Champions triple threat in June 2026, with Zayn retaining."),
            dict(name="Pete Dunne and Ilja Dragunov",
                 desc="The two matches that bookend NXT UK. Dunne's 685-day reign ended against him on "
                      "April 5, 2019; Dragunov ended his 870 on August 22, 2021. The Dragunov match is "
                      "the one that got him moved to the main roster."),
            dict(name="Jey Uso", slug="jey-uso",
                 desc="Uso made him tap in the opening match of WrestleMania 41 on April 19, 2025 to win "
                      "his first world championship; Gunther took it straight back on the June 9 Raw. It "
                      "matters because WWE used him as the credibility test a homegrown fan-favourite had "
                      "to pass, which is the role he has occupied ever since."),
            dict(name="CM Punk", slug="cm-punk",
                 desc="Punk beat him for the World Heavyweight Championship at SummerSlam on August 2, "
                      "2025, and Gunther finished with a broken nose that kept him out roughly two "
                      "months. The title changed hands twice that night, because Seth Rollins cashed in "
                      "Money in the Bank on Punk minutes later. It is the moment he stopped being a "
                      "champion and started being a gatekeeper."),
            dict(name="Nick Aldis",
                 desc="Months of accusing the SmackDown general manager of favouritism and calling him "
                      "“a failed wrestler,” until Aldis gave up the job to fight him at "
                      "SummerSlam Night 1 on August 1, 2026 — and got choked out. It is the first "
                      "Gunther programme in years built on personal contempt rather than a "
                      "championship, and Aldis, a former TNA and NWA World Champion, got a real send-off "
                      "out of it: standing ovation, “you still got it” chants, a B+ from "
                      "Forbes."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Thin by design — the verified list is short, and nothing is added to pad it.",
        rows=[
            dict(when="2022&ndash;", title="WWE 2K", kind="Game",
                 desc="Playable in WWE 2K22, 2K23, 2K24, 2K25 and 2K26. He has never been a cover star."),
            dict(when="2015&ndash;2020", title="wXw Wrestling Academy", kind="Training",
                 desc="Head trainer for five years, which matters more than most media credits: a "
                      "meaningful share of the current European roster came through that school while he "
                      "was running it."),
            dict(when="2019&ndash;", title="Dvořák, Symphony No. 9", kind="Music",
                 desc="The entrance theme is the fourth movement of the Symphony No. 9 in E minor, "
                      "“From the New World” — kept after Imperium dissolved."),
            dict(when="2024&ndash;", title="Fightful, Wrestling Inc.", kind="Interviews",
                 desc="His on-record interviews are where the Imperium split and his preference for "
                      "working alone are documented. No film or scripted television role, no "
                      "autobiography, no podcast and no WWE Chronicle or WWE 24 episode centred on him "
                      "could be verified, so none are listed."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated the way the sources actually state them — including the two separate "
             "Intercontinental records that get collapsed into one wrong sentence.",
        stats=[
            ("666",   "Days as IC Champion"),
            ("870",   "Days as NXT UK Champion"),
            ("71:25", "Royal Rumble iron man"),
        ],
        rows=[
            dict(name="666 consecutive days as Intercontinental Champion",
                 sub="June 10, 2022 to April 6, 2024 — the longest reign in the title's history, and one "
                     "of the very few figures on this page with no source conflict behind it: WWE.com's "
                     "own profile says “a record 666 days” and Wikipedia agrees."),
            dict(name="Passed The Honky Tonk Man's longest-single-reign record, September 2023",
                 sub="Honky Tonk Man held the Intercontinental Championship for 454 days from June 1987 "
                     "to August 1988 — logged by Wikipedia as 454 days held and 453 as WWE recognises "
                     "it. Gunther went past it at 455 days on the Raw where he defended against Chad "
                     "Gable (CBS Sports). Note what that record is not: it is the longest single reign, "
                     "not the all-time total."),
            dict(name="Passed Pedro Morales' most-total-days record, later in the same reign",
                 sub="Morales accumulated 619 days as Intercontinental Champion across two reigns — 194 "
                     "days from December 1980 to June 1981 and 425 from November 1981 to January 1983. "
                     "That was the all-time total record, and SEScoops covered Gunther passing it as a "
                     "separate milestone from the Honky Tonk Man one. Two records, two men, two dates, "
                     "one reign."),
            dict(name="First Austrian to hold the Intercontinental Championship",
                 sub="Per Wikipedia. He is billed from Vienna and was born there."),
            dict(name="870 consecutive days as NXT United Kingdom Champion",
                 sub="April 5, 2019 to August 22, 2021 (WWE.com), ending Pete Dunne's own 685-day reign "
                     "to start it. It was the longest reign of any WWE championship in the modern era "
                     "until Roman Reigns' second Universal Championship reign passed it in January 2023 "
                     "— the caveat most retellings drop. A Wikipedia summary gives the endpoints as "
                     "April 4, 2019 to August 31, 2021, which does not arithmetically produce 870; the "
                     "April 5 / August 22 dates do, exactly."),
            dict(name="Longest survival time in Royal Rumble history: 71 minutes 25 seconds",
                 sub="Set in the 2023 men's Royal Rumble and still standing in 2026. For scale, the 2026 "
                     "iron man was Je'Von Evans at 40:58 and the entire 2026 match ran 58:22 bell to "
                     "bell, the first Rumble under an hour since 2022 (Cageside Seats)."),
            dict(name="2026 Royal Rumble: entered No. 30, last man eliminated",
                 sub="Roman Reigns put him out to win it — after Gunther had already wrestled AJ Styles' "
                     "retirement match earlier the same night (CBS Sports). He lasted 7:50 in the Rumble "
                     "itself."),
            dict(name="Three retirement matches won in seven months",
                 sub="Goldberg on July 12, 2025 at Saturday Night's Main Event XL in Atlanta; John Cena "
                     "on December 13, 2025, in Cena's final match, which Cena gave up; AJ Styles on "
                     "January 31, 2026 at the Royal Rumble in Riyadh. Cena said publicly in February "
                     "2026 (PWTorch) that he came up with the finish to his own retirement match."),
            dict(name="King of the Ring, 2024",
                 sub="His only tournament win in WWE, and the reason the SummerSlam 2024 world title "
                     "match happened."),
            dict(name="Two-time World Heavyweight Champion — 259 days, then 54",
                 sub="August 3, 2024 to April 19, 2025, then June 9 to August 2, 2025. The 259 is "
                     "computed from verified endpoints rather than cited, so treat the dates as the "
                     "citation. A Wikipedia summary that ends the first reign on November 2, 2024 at 92 "
                     "days is simply wrong — Jey Uso won that title at WrestleMania 41 on April 19, "
                     "2025, per Forbes, CBS Sports, Cageside Seats, 411Mania and Fox — and that figure "
                     "is not published anywhere on this page."),
            dict(name="Not a Triple Crown or Grand Slam Champion",
                 sub="Worth stating because it is a common assumption. He has never held a WWE tag team "
                     "championship or the United States Championship. His only tag titles anywhere are "
                     "the four wXw World Tag Team Championship reigns."),
            dict(name="Awards: ESPN Wrestler of the Year 2023 and 2024",
                 sub="Plus Wrestling Observer Newsletter Europe MVP in 2018, 2019 and 2020, and ninth on "
                     "Sports Illustrated's 2023 top-ten wrestlers list (Wikipedia). PWI 500: fourth in "
                     "2023 and third in 2025; the 2024 placement could not be verified and the 2026 list "
                     "had not been published as of August 23, 2026."),
            dict(name="wXw 16 Carat Gold, 2010 — youngest winner at the time",
                 sub="He was twenty-two. Individual reign dates and lengths for his independent "
                     "championships were not verified in this pass and are not estimated here."),
        ],
        footnote=("Two things are deliberately absent. No career win-loss record: the previous version of "
                  "this page published 94-18 alongside an 82% win rate that does not follow from it, and "
                  "no verified total exists to replace it. No social handles: the research turned up "
                  "@gunther_aut against @gunther_wwe on Instagram and @Gunther_AUT against "
                  "@GuntherOfficial on X without establishing which of either pair is official, so "
                  "nothing is linked rather than pointing readers at a possibly fake account. The "
                  "five-star match count of five is Wikipedia's figure and is single-sourced."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/gunther"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Gunther_(wrestler)"),
        dict(k="CBS Sports", v="Breaking the Honky Tonk Man single-reign mark",
             href="https://www.cbssports.com/wwe/news/gunther-breaks-intercontinental-title-record-wwe-superstar-surpasses-35-year-old-mark-held-by-honky-tonk-man"),
        dict(k="SEScoops", v="Breaking Pedro Morales' combined-days record",
             href="https://www.sescoops.com/article/gunther-breaks-pedro-morales-record-for-the-most-days-as-wwe-intercontinental-champion"),
        dict(k="Wikipedia", v="List of WWE Intercontinental Champions",
             href="https://en.wikipedia.org/wiki/List_of_WWE_Intercontinental_Champions"),
        dict(k="Cageside Seats", v="WWE backs away from the name “Gunther Stark”",
             href="https://www.cagesideseats.com/wwe/2022/1/20/22893722/wwe-walter-name-change-gunther-stark-trademark-nxt"),
        dict(k="Forbes", v="SummerSlam 2026 — Gunther chokes out Nick Aldis",
             href="https://www.forbes.com/sites/alfredkonuwa/2026/08/01/wwe-summerslam-2026-results-as-gunther-chokes-out-nick-aldis-in-return-from-retirement/"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/gunther.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Did Gunther break The Honky Tonk Man&rsquo;s all-time Intercontinental record?",
            a="Not as usually stated, because that record never existed. The Honky Tonk Man held the "
              "longest <b>single</b> Intercontinental Championship reign &mdash; 454 days from June 1987 "
              "to August 1988, which Wikipedia logs as 454 held and 453 as WWE recognises it. The record "
              "for the <b>most total days</b> belonged to <b>Pedro Morales</b>, 619 days across two "
              "reigns. Gunther broke them separately inside the same run: Honky Tonk Man&rsquo;s mark in "
              "September 2023 at 455 days (CBS Sports), Morales&rsquo;s 619 later in the same reign "
              "(SEScoops). The reign itself ran June 10, 2022 to April 6, 2024 &mdash; 666 days &mdash; "
              "and WWE.com and Wikipedia agree on that figure exactly.",
            q_ld="Did Gunther break The Honky Tonk Man's all-time Intercontinental Championship record?",
            a_ld="Not as it is usually stated. The Honky Tonk Man never held the all-time Intercontinental "
                 "Championship record. He held the record for the longest single reign, 454 days from "
                 "June 1987 to August 1988, which Wikipedia logs as 454 days held and 453 days as "
                 "recognised by WWE. The record for the most total days as Intercontinental Champion "
                 "belonged to Pedro Morales, who accumulated 619 days across two reigns between December "
                 "1980 and January 1983. Gunther broke the two records separately inside the same reign: "
                 "he passed The Honky Tonk Man's single-reign mark in September 2023 at 455 days, and "
                 "passed Pedro Morales' 619 combined days later in the same reign. Gunther's reign ran "
                 "from June 10, 2022 to April 6, 2024, a total of 666 days, a figure on which WWE.com and "
                 "Wikipedia agree."),
        dict(
            q="Why did WALTER become Gunther?",
            a="Because WWE renamed him in January 2022, on arrival to NXT 2.0, for trademark reasons. "
              "&ldquo;WALTER&rdquo; was never a gimmick name to begin with &mdash; he was born Walter "
              "Hahn in Vienna, and PROGRESS simply styled his real first name in all caps. There is a "
              "footnote most bios skip: WWE filed for the full name <b>&ldquo;Gunther Stark&rdquo;</b> on "
              "January 13, 2022 and abandoned that trademark on January 19, after it emerged that "
              "G&uuml;nther Stark was the name of a Nazi military commander (Cageside Seats, Sports "
              "Illustrated). He was only ever billed on air as Gunther. The full name history runs Big "
              "Van Walter (2005&ndash;2014) &rarr; Big Daddy Walter (2014&ndash;2018) &rarr; WALTER "
              "(2018&ndash;2022) &rarr; Gunther (2022&ndash;present).",
            q_ld="Why did WALTER change his name to Gunther?",
            a_ld="WWE renamed WALTER as Gunther in January 2022 when he arrived on NXT 2.0, for trademark "
                 "reasons. WALTER was not a gimmick name: he was born Walter Hahn in Vienna, Austria, and "
                 "the PROGRESS promotion styled his real first name in capital letters. WWE originally "
                 "filed a trademark for the full name Gunther Stark on January 13, 2022 and abandoned it "
                 "on January 19, 2022 after it emerged that Gunther Stark was the name of a Nazi military "
                 "commander. He was only ever billed on air as Gunther. His full ring-name history is Big "
                 "Van Walter from 2005 to 2014, Big Daddy Walter from 2014 to 2018, WALTER from 2018 to "
                 "2022, and Gunther from 2022 to the present."),
        dict(
            q="Is Gunther a champion right now, and is he on Raw or SmackDown?",
            a="He holds no championship as of August 23, 2026. His last title was the World Heavyweight "
              "Championship, lost to CM Punk at SummerSlam on August 2, 2025. On brand: WWE.com&rsquo;s "
              "profile summary and 2025 press still describe him as a Raw star, but his 2026 booking is "
              "<b>SmackDown</b> throughout &mdash; the Night of Champions triple threat, the feud with "
              "SmackDown general manager Nick Aldis, the August 21, 2026 SmackDown backstage segment with "
              "Kevin Owens and Finn B&aacute;lor. This page follows the booking and flags the WWE.com lag. "
              "He is currently being pointed at the Undisputed WWE Championship, held by CM Punk since "
              "July 6, 2026.",
            q_ld="Is Gunther a champion right now, and is he on Raw or SmackDown?",
            a_ld="Gunther holds no championship as of August 23, 2026. His most recent title was the World "
                 "Heavyweight Championship, which he lost to CM Punk at SummerSlam on August 2, 2025. He "
                 "is on SmackDown: WWE.com's profile summary and older 2025 press still list Gunther as a "
                 "Raw star, but his 2026 booking is entirely on SmackDown, including the Night of "
                 "Champions triple threat, the feud with SmackDown general manager Nick Aldis, and the "
                 "August 21, 2026 SmackDown. Gunther is currently being positioned toward the Undisputed "
                 "WWE Championship, held by CM Punk since July 6, 2026."),
        dict(
            q="Which legends has Gunther retired?",
            a="Three, in seven months. <b>Goldberg</b> on July 12, 2025 at Saturday Night&rsquo;s Main "
              "Event XL in Atlanta; <b>John Cena</b> on December 13, 2025, in Cena&rsquo;s final match, "
              "which Cena gave up; and <b>AJ Styles</b> on January 31, 2026 at the Royal Rumble in "
              "Riyadh. That is the basis of the &ldquo;Career Killer&rdquo; designation WWE now leads with "
              "on his own profile. Cena said publicly in February 2026 that he came up with the finish to "
              "his own retirement match.",
            q_ld="Which wrestlers has Gunther retired?",
            a_ld="Gunther has won three retirement matches in seven months: Goldberg on July 12, 2025 at "
                 "Saturday Night's Main Event XL in Atlanta, John Cena on December 13, 2025 in Cena's "
                 "final match, which Cena gave up, and AJ Styles on January 31, 2026 at the Royal Rumble "
                 "in Riyadh. This is the basis of the Career Killer designation WWE now leads with on "
                 "Gunther's official profile. John Cena said publicly in February 2026 that he devised "
                 "the finish to his own retirement match against Gunther."),
        dict(
            q="Does Gunther still hold the Royal Rumble iron man record?",
            a="Yes. His 71 minutes 25 seconds in the 2023 men&rsquo;s Royal Rumble is still the longest "
              "survival time in the match&rsquo;s history as of 2026. Nothing has come close since: the "
              "2026 iron man was Je&rsquo;Von Evans at 40 minutes 58 seconds, and the whole 2026 Rumble "
              "ran 58:22 bell to bell. Gunther entered that one at number 30 and lasted 7:50, going out "
              "last to Roman Reigns.",
            q_ld="Does Gunther still hold the Royal Rumble iron man record?",
            a_ld="Yes. Gunther's 71 minutes and 25 seconds in the 2023 men's Royal Rumble remains the "
                 "longest survival time in Royal Rumble history as of 2026. The 2026 men's Royal Rumble "
                 "iron man was Je'Von Evans at 40 minutes and 58 seconds, and the entire 2026 match ran "
                 "58 minutes and 22 seconds. Gunther entered the 2026 Royal Rumble at number 30, lasted 7 "
                 "minutes and 50 seconds, and was the last man eliminated, by Roman Reigns."),
        dict(
            q="How long did Gunther hold the NXT UK Championship?",
            a="870 days, per WWE.com &mdash; April 5, 2019 to August 22, 2021, from beating Pete Dunne at "
              "TakeOver: New York (ending Dunne&rsquo;s own 685-day reign) to losing to Ilja Dragunov at "
              "TakeOver 36. One caution on the dates: a Wikipedia summary gives April 4, 2019 to August "
              "31, 2021, which does not arithmetically produce 870 days; the April 5 / August 22 "
              "endpoints do, exactly. And one caution on the record: it was the longest reign of any WWE "
              "championship in the modern era only <i>until</i> Roman Reigns&rsquo; second Universal "
              "Championship reign passed it in January 2023.",
            q_ld="How long did Gunther hold the NXT United Kingdom Championship?",
            a_ld="Gunther held the NXT United Kingdom Championship for 870 days, from April 5, 2019 to "
                 "August 22, 2021, according to WWE.com. He won it from Pete Dunne at NXT UK TakeOver: "
                 "New York, ending Dunne's own 685-day reign, and lost it to Ilja Dragunov at NXT "
                 "TakeOver 36. A Wikipedia summary gives the dates as April 4, 2019 to August 31, 2021, "
                 "which does not arithmetically produce 870 days, while April 5, 2019 to August 22, 2021 "
                 "produces exactly 870. The reign was the longest of any WWE championship in the modern "
                 "era only until Roman Reigns' second Universal Championship reign surpassed it in "
                 "January 2023."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Walter Hahn"),
        dict(label="Born", value="August 20, 1987", sub="Vienna, Austria &middot; age 39"),
        dict(label="Billed from", value="Vienna, Austria"),
        dict(label="Height", value="6&#8242;4&#8243;", sub="193 cm"),
        dict(label="Weight", value="250 lb", sub="113 kg (billed)"),
        dict(label="Debut", value="November 19, 2005", sub="Bern, Switzerland, as Big Van Walter"),
        dict(label="Trained by", value="Michael Kovac",
             sub="Wikipedia also credits Riki Choshu, Tatsuhito Takaiwa and Tomohiro Ishii"),
        dict(label="Ring names",
             value="Big Van Walter &rarr; Big Daddy Walter &rarr; WALTER &rarr; Gunther",
             sub="2005&ndash;14 &middot; 2014&ndash;18 &middot; 2018&ndash;22 &middot; 2022&ndash;present "
                 "&mdash; Walter is his legal first name, not a gimmick; WWE retired it rather than "
                 "invented it, and its own &ldquo;Gunther Stark&rdquo; trademark was filed January 13, "
                 "2022 and abandoned January 19"),
        dict(label="Signature", value="Knife-edge chops &middot; Powerbomb &middot; Sleeper / rear-naked "
                                      "choke &middot; Boston crab",
             sub="WWE.com lists no single named finisher"),
        dict(label="Entrance theme", value="Dvo&#345;&aacute;k, Symphony No. 9",
             sub="&ldquo;From the New World,&rdquo; fourth movement"),
        dict(label="Brand", value="SmackDown", sub="per 2026 booking &mdash; WWE.com still lists Raw"),
        dict(label="Also known as",
             value="The Ring General &middot; Der Ringgeneral &middot; The Career Killer"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1987-08-20",
    bornplace="Vienna, Austria",
    nationality="Austria",
    height_cm=193,
    weight_kg=113,
    ld=dict(
        alternateName=["Walter Hahn", "WALTER", "Big Van Walter", "Big Daddy Walter",
                       "The Ring General", "Der Ringgeneral", "The Career Killer"],
        award=["WWE Intercontinental Championship (1 reign, a record 666 days)",
               "NXT United Kingdom Championship (1 reign, 870 days)",
               "World Heavyweight Championship (2 reigns)",
               "WWE King of the Ring (2024)",
               "Longest survival time in Royal Rumble history (71 minutes 25 seconds, 2023)",
               "wXw Unified World Wrestling Championship (3 reigns)",
               "wXw World Tag Team Championship (4 reigns)",
               "wXw 16 Carat Gold Tournament (2010)",
               "PROGRESS World Championship (1 reign)",
               "PROGRESS Atlas Championship (3 reigns)",
               "OTT World Championship (1 reign)",
               "PWG World Championship (1 reign)",
               "ESPN Men's Wrestler of the Year (2023, 2024)",
               "Wrestling Observer Newsletter Europe MVP (2018, 2019, 2020)"],
        knowsAbout=["Professional wrestling", "European catch wrestling", "Imperium", "Ringkampf",
                    "WWE", "NXT UK", "wXw", "Championship wrestling"],
        description="Gunther, born Walter Hahn in Vienna, Austria, is an Austrian professional wrestler "
                    "signed to WWE and known in Europe as WALTER. He held the WWE Intercontinental "
                    "Championship for a record 666 days between June 10, 2022 and April 6, 2024, passing "
                    "The Honky Tonk Man's 454-day longest-single-reign record in September 2023 and Pedro "
                    "Morales' 619-day most-total-days record later in the same reign. He also held the "
                    "NXT United Kingdom Championship for 870 days, is a two-time World Heavyweight "
                    "Champion, won King of the Ring in 2024, and holds the longest survival time in Royal "
                    "Rumble history at 71 minutes 25 seconds.",
        sameAs=["https://en.wikipedia.org/wiki/Gunther_(wrestler)",
                "https://www.wwe.com/superstars/gunther"],
    ),
)
