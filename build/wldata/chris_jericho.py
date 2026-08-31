# -*- coding: utf-8 -*-
"""Chris Jericho - dossier data.

Sources: web-verified August 31, 2026 (Wikipedia; Yahoo Sports on the April 2026
return; Wrestling Inc on the Casino Gauntlet declaration and the October 2024 ROH
title win; F4W on the TNT title challenge; NoDQ on the All In: London Casino
Gauntlet). Every match row carries a day-precision date from those sources or the
standard event record.

Deliberate omissions:
  * No career win-loss total - none verified across 36 years and six countries.
  * Tag team reign counts are not published as a number - partners are listed
    instead, because the count was not verified in this pass.
  * No social links - handles were not verified in this pass.
  * No Observer star ratings - none verified against archives in this pass.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2001-10-21", promo="WWE", landmark=True,
         event="No Mercy — St. Louis", opponent="The Rock",
         stip="Singles — his first world championship, at 30, after a decade of being told he was too small", title="WCW Championship"),
    dict(result="W", date="2001-12-09", promo="WWE", landmark=True,
         event="Vengeance — San Diego", opponent="The Rock",
         stip="Semi-final of the unification night — takes the WCW/World Championship", title="WCW/World Championship"),
    dict(result="W", date="2001-12-09", promo="WWE", landmark=True,
         event="Vengeance — San Diego", opponent="Stone Cold Steve Austin",
         stip="Final of the unification night — becomes the first Undisputed Champion", title="Undisputed WWF Championship"),
    dict(result="L", date="2002-03-17", promo="WWE",
         event="WrestleMania X8 — Toronto", opponent="Triple H",
         stip="Singles — the Undisputed reign ends", title="Undisputed WWF Championship"),
    dict(result="W", date="2008-10-05", promo="WWE", landmark=True,
         event="No Mercy — Portland", opponent="Shawn Michaels",
         stip="Ladder match — the peak of the 2008 feud that reinvented him", title="World Heavyweight Championship"),
    dict(result="W", date="2009-06-07", promo="WWE",
         event="Extreme Rules — New Orleans", opponent="Rey Mysterio",
         stip="No holds barred — a record ninth Intercontinental Championship", title="WWE Intercontinental Championship"),
    dict(result="L", date="2009-06-28", promo="WWE",
         event="The Bash — Sacramento", opponent="Rey Mysterio",
         stip="Title vs. mask — Mysterio keeps the mask and takes the title back", title="WWE Intercontinental Championship"),
    dict(result="W", date="2010-02-21", promo="WWE", type="tag",
         event="Elimination Chamber — St. Louis", opponent="The Chamber field",
         stip="Elimination Chamber match — a third World Heavyweight Championship", title="World Heavyweight Championship"),
    dict(result="L", date="2012-04-01", promo="WWE",
         event="WrestleMania XXVIII — Miami", opponent="CM Punk",
         stip="Singles — the 'best in the world' argument, settled Punk's way", title="WWE Championship"),
    dict(result="W", date="2016-04-03", promo="WWE",
         event="WrestleMania 32 — Dallas", opponent="AJ Styles",
         stip="Singles — the veteran wins the exchange, the rookie wins the year", title=""),
    dict(result="L", date="2018-01-04", promo="NJPW", landmark=True,
         event="Wrestle Kingdom 12 — Tokyo Dome", opponent="Kenny Omega",
         stip="Alpha vs. Omega, no disqualification — the match that made the late-career pivot real", title="IWGP United States Championship"),
    dict(result="W", date="2019-08-31", promo="AEW", landmark=True,
         event="All Out — Chicago", opponent="Adam Page",
         stip="Singles — becomes the first AEW World Champion, exactly seven years to the day before this page's dateline", title="AEW World Championship"),
    dict(result="L", date="2020-02-29", promo="AEW", landmark=True,
         event="Revolution — Chicago", opponent="Jon Moxley",
         stip="Singles — the 182-day inaugural reign ends", title="AEW World Championship"),
    dict(result="W", date="2022-09-21", promo="AEW", landmark=True,
         event="Dynamite: Grand Slam — New York", opponent="Claudio Castagnoli",
         stip="Singles — wins the ROH World Championship, a title he'd never touched in 32 years", title="ROH World Championship"),
    dict(result="W", date="2024-04-21", promo="AEW",
         event="Dynasty — St. Louis", opponent="HOOK",
         stip="FTW rules — the Learning Tree era's one belt", title="FTW Championship"),
    dict(result="L", date="2024-08-25", promo="AEW",
         event="All In — Wembley Stadium", opponent="HOOK",
         stip="FTW rules — HOOK takes it back with Taz at ringside", title="FTW Championship"),
    dict(result="W", date="2024-10-23", promo="AEW", landmark=True,
         event="Dynamite — Ladder War", opponent="Mark Briscoe",
         stip="Ladder War — a second ROH World Championship and, by Wrestling Inc's count, a ninth world title", title="ROH World Championship"),
    dict(result="L", date="2025-04-06", promo="AEW", landmark=True,
         event="Dynasty — Philadelphia", opponent="Bandido",
         stip="Title vs. mask — Bandido keeps the mask, takes the title; Jericho disappears from AEW for a year", title="ROH World Championship"),
    dict(result="L", date="2026-08-12", promo="AEW",
         event="Dynamite — Las Vegas", opponent="Kevin Knight",
         stip="TNT Championship challenge — a Don Callis screwdriver shot keeps the belt on Knight", title="AEW TNT Championship"),
    dict(result="L", date="2026-08-30", promo="AEW", type="tag",
         event="All In: London — Wembley Stadium", opponent="The Casino Gauntlet field",
         stip="Casino Gauntlet for a world title shot — entered sixth, eliminated Ciampa, locked the Walls on MJF; Andrade won", title=""),
]

DATA = dict(
    slug="chris-jericho",
    name="Chris Jericho",
    realname="Christopher Keith Irvine",
    epithet="Le Champion",
    hook="Record & Titles",

    meta_desc=("Chris Jericho was the first Undisputed WWF Champion and the first AEW World "
               "Champion - nine world titles, a record nine Intercontinental reigns, and a 2026 "
               "AEW return after a year away. Full record, titles, factions and career."),
    og_desc=("Le Champion: first Undisputed WWF Champion, first AEW World Champion, nine world "
             "titles, nine Intercontinental reigns, and a career reinvented more times than "
             "anyone's - back in AEW as of 2026."),
    tw_desc="First Undisputed Champion. First AEW Champion. Nine world titles. Still going at 55.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1990",
    height_imp="6&#8242;0&#8243;",
    weight_lb="227",
    world_titles="9",
    vitals_tagline="A little bit of the bubbly",
    support_note="Merch &middot; Music &middot; Listen",
    sp_items=[
        dict(ic="FZ", title="Fozzy", sub="His metal band since 1999 — 'Judas' went platinum-adjacent",
             tag="Listen", href="https://www.fozzyrock.com/"),
        dict(ic="AEW", title="AEW Shop", sub="Official Jericho merch",
             tag="Shop", href="https://www.shopaew.com/"),
        dict(ic="TV", title="All Elite Wrestling", sub="Dynamite & Collision — where he wrestles now",
             tag="Watch", href="https://www.allelitewrestling.com/"),
        dict(ic="WWE", title="WWE Alumni Profile", sub="WWE.com", charity=True,
             tag="Visit", href="https://www.wwe.com/superstars/chris-jericho"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Y2J &middot; The Painmaker &middot; The Ocho &middot; The Learning Tree",
    hero_tag="Winnipeg, Manitoba &middot; <em>CMLL &middot; WAR &middot; ECW &middot; WCW &middot; WWF/WWE &middot; NJPW &middot; AEW &middot; 1990&ndash;present</em>",
    now_label="NOW",
    now_bold="AEW, no championship",
    now_tail=" &middot; back since April 2026 after a year away &mdash; came up short against Kevin Knight and in the All In: London Casino Gauntlet, still hunting world title number ten",
    hstats=[
        dict(value="9", x=True, label="World Titles"),
        dict(value="9", x=True, label="IC Title Reigns"),
        dict(value="1st", x=False, label="Undisputed & AEW Champ"),
        dict(value="36", x=False, label="Years In The Ring"),
    ],
    ghost_link="From a Ponoka time-limit draw to two inaugural world championships",
    vlabel="Est. 1990 &middot; Winnipeg, MB",
    mono="CJ",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Chris Jericho</b> has been the first champion of two different companies&rsquo; "
        "flagship titles, twenty years apart &mdash; the only wrestler who can say it. On December "
        "9, 2001 at Vengeance he beat The Rock and Stone Cold Steve Austin in one night to become "
        "the first <b>Undisputed WWF Champion</b>; on August 31, 2019 at All Out he beat Adam Page "
        "to become the first <b>AEW World Champion</b>. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">9</span>'
        '<span class="pull-cap">Intercontinental Championship reigns &mdash; the record, the ninth won from Rey Mysterio in 2009</span></span>'
        "Around those bookends: a record nine "
        "Intercontinental Championship reigns, two ROH World Championships, an IWGP "
        "Intercontinental Championship, the FTW title, a platinum-selling metal band, and more "
        "full-scale reinventions than any wrestler of his era. He turned 55 in November 2025 and is "
        "an active AEW wrestler as of August 31, 2026 &mdash; one day after losing the Casino "
        "Gauntlet at All In: London.",

        "His world title count is quoted as everything from six to ten, so here is the arithmetic "
        "this page uses. In WWE: two WCW/World Championship reigns (the first won from The Rock at "
        "No Mercy on October 21, 2001), the Undisputed WWF Championship (Vengeance, December 9, "
        "2001), and three World Heavyweight Championship reigns (2008 twice, 2010) &mdash; six. Add "
        "the inaugural AEW World Championship (2019) and two ROH World Championships (2022 and "
        "2024) and you reach <b>nine</b>, the figure Wrestling Inc used when the ninth arrived in "
        "October 2024. The confusion is built in: the Vengeance night contains a WCW reign and the "
        "Undisputed reign in the same two hours, and WWE-only counts stop at six. He has spent 2026 "
        "saying out loud that he wants a tenth.",

        "The long version of the career is a study in leaving at the right time: Winnipeg to "
        "Calgary&rsquo;s Hart Brothers school, debut October 2, 1990; Mexico, Germany and "
        "Japan&rsquo;s WAR promotion; ECW; three years of being misused in WCW while inventing the "
        "conspiracy-victim heel; the August 9, 1999 WWF debut interrupting The Rock; the 2008 "
        "Shawn Michaels feud that produced the suit-wearing sociopath most wrestlers still copy "
        "when they need a serious heel; the List, the scarf, the Festival of Friendship. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">182</span>'
        '<span class="pull-cap">days as the inaugural AEW World Champion &mdash; Le Champion is the reason the company&rsquo;s first year worked</span></span>'
        "Then the pivot nobody his age had tried: Wrestle Kingdom 12 against Kenny Omega on January "
        "4, 2018 as the Painmaker, and in 2019 the leap to the AEW startup, where the Inner Circle, "
        "&ldquo;a little bit of the bubbly&rdquo; and Judas sung by twenty thousand people turned "
        "him into the promotion&rsquo;s founding authority figure and its first champion.",

        "The last two years are the strangest chapter. The Learning Tree run &mdash; 2024&rsquo;s "
        "deliberately insufferable mentor gimmick with Big Bill and Bryan Keith &mdash; won him the "
        "FTW title and a second ROH World Championship in the October 23, 2024 Ladder War, before "
        "Bandido took the belt in a title-versus-mask match at Dynasty on <b>April 6, 2025</b>. "
        "Then: nothing. He vanished from AEW television for a year while his contract quietly ran "
        "on &mdash; reportedly frozen during the absence &mdash; and the wrestling press spent the "
        "gap forecasting a WWE homecoming that never came. He returned on the <b>April 1, 2026</b> "
        "Dynamite in Winnipeg &mdash; &ldquo;I&rsquo;m home&rdquo; &mdash; and the 2026 run has "
        "been a pointed exercise in earning rather than coasting: a TNT Championship challenge "
        "lost to Kevin Knight on August 12 when Don Callis put a screwdriver in his back, and the "
        "All In: London Casino Gauntlet on August 30, where he entered sixth, dumped Tommaso "
        "Ciampa to a stadium singing Judas, locked the Walls on MJF, and watched Andrade win the "
        "title shot he wanted. No championship, one stated goal: AEW World Champion again.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE", "NJPW", "AEW"],
        promo_labels={"WWE": "WWF/WWE", "NJPW": "NJPW", "AEW": "AEW"},
        stats=[
            ("9&times;", "World champion"),
            ("9&times;", "Intercontinental"),
            ("1st", "Undisputed Champion"),
            ("1st", "AEW World Champion"),
            ("2&times;", "ROH World Champion"),
            ("36", "Years active"),
        ],
        lead=("Twenty documented bouts &mdash; the unification night as two rows, the AEW founding "
              "reign at both ends, both ROH title changes, and the full 2026 comeback so far. This "
              "is a curated ledger, not a career count; nothing approaching a verified win&ndash;loss "
              "total exists for a career spanning six countries and 36 years, and none is invented. "
              "Filter by match type, tap any column header to sort, and turn spoilers on to reveal "
              "results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the reputation rests on. No Observer star ratings are published "
                    "here &mdash; none were verified against archives in this pass."),
    signature=[
        dict(rating="—", event="Vengeance 2001 — San Diego", opponent="The Rock, then Steve Austin",
             stip="Both in one night — the Undisputed Championship unification"),
        dict(rating="—", event="No Mercy 2008 — Portland", opponent="Shawn Michaels",
             stip="Ladder match — the summit of the feud that reinvented him"),
        dict(rating="—", event="Wrestle Kingdom 12 — Tokyo Dome", opponent="Kenny Omega",
             stip="Alpha vs. Omega — the pivot that made the second act possible"),
        dict(rating="—", event="All Out 2019 — Chicago", opponent="Adam Page",
             stip="The night AEW got its first world champion"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("9&times;", "World title reigns"),
            ("9&times;", "Intercontinental (record)"),
            ("2&times;", "ROH World"),
            ("1st", "Champion, twice over"),
        ],
        lead=("Nine world championships across three companies, and the Intercontinental record "
              "that stood before any of them. Tag reigns are listed by partner rather than count "
              "&mdash; the total was not verified in this pass and is not guessed."),
        rows=[
            dict(ic="U", name="Undisputed WWF Championship", count="1",
                 sub="The first. Def. The Rock (WCW/World title) and Steve Austin (WWF title) in one "
                     "night at Vengeance, December 9, 2001; lost to Triple H at WrestleMania X8, "
                     "March 17, 2002"),
            dict(ic="C", name="WCW/World Championship", count="2",
                 sub="First won from The Rock at No Mercy, October 21, 2001 &mdash; his first world "
                     "title, at 30; the second is the Vengeance semi-final, folded into the "
                     "unification"),
            dict(ic="H", name="World Heavyweight Championship", count="3",
                 sub="The Unforgiven 2008 championship scramble; a cage-match reign that November; "
                     "the Elimination Chamber win of February 21, 2010"),
            dict(ic="A", name="AEW World Championship", count="1",
                 sub="The inaugural champion &mdash; def. Adam Page at All Out, August 31, 2019; "
                     "lost to Jon Moxley at Revolution, February 29, 2020, after 182 days"),
            dict(ic="R", name="ROH World Championship", count="2",
                 sub="Def. Claudio Castagnoli at Dynamite: Grand Slam, September 21, 2022; def. Mark "
                     "Briscoe in the October 23, 2024 Ladder War; lost to Bandido, title vs. mask, "
                     "at Dynasty, April 6, 2025"),
            dict(ic="I", name="WWE Intercontinental Championship", count="9",
                 sub="The record. The ninth won from Rey Mysterio at Extreme Rules, June 7, 2009 "
                     "&mdash; and lost back to him in a title-vs-mask match three weeks later"),
            dict(ic="J", name="IWGP Intercontinental Championship", count="1",
                 sub="Won from Tetsuya Naito in 2018 during the Painmaker run"),
            dict(ic="F", name="FTW Championship", count="1",
                 sub="Def. HOOK at Dynasty, April 21, 2024; lost it back to HOOK at All In on August "
                     "25, 2024"),
            dict(ic="T", name="Tag team championships", count="&mdash;",
                 sub="World Tag Team Championship reigns with partners including Chris Benoit, The "
                     "Rock, Edge and Big Show &mdash; the exact count across belts was not verified "
                     "in this pass and is not published"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Three AEW-era units, each an era of the gimmick &mdash; he does not join factions so "
             "much as institutionalise whatever he is currently doing.",
        cards=[
            dict(era="AEW &middot; 2019&ndash;2022",
                 name="The Inner Circle",
                 members="Chris Jericho, Jake Hager, Sammy Guevara, Santana, Ortiz",
                 desc="Formed weeks after he won the inaugural AEW World Championship — the "
                      "company's first supergroup, built to give a startup instant main-event "
                      "structure. 'A little bit of the bubbly' came out of its first celebration; "
                      "the Stadium Stampede matches against The Elite carried AEW through the "
                      "pandemic era. It ended when Guevara's generation outgrew it, which was "
                      "roughly the point."),
            dict(era="AEW &middot; 2022&ndash;2023",
                 name="The Jericho Appreciation Society",
                 members="Chris Jericho, Daniel Garcia, 2point0, Jake Hager, Anna Jay, Tay Melo",
                 desc="The 'sports entertainers versus wrestlers' stable — Jericho as cult leader "
                      "teaching young grapplers to embrace entertainment over craft, feuding with "
                      "the Blackpool Combat Club and Ring of Honor's old guard while he held the "
                      "ROH World Championship."),
            dict(era="AEW &middot; 2024&ndash;2025",
                 name="The Learning Tree",
                 members="Chris Jericho, Big Bill, Bryan Keith",
                 desc="The final pre-hiatus form: a patronising mentor who insists he is helping "
                      "while stealing HOOK's FTW title and calling everyone 'kiddo.' Deliberately "
                      "irritating by design, and the faction whose collapse — a confrontation with "
                      "Bill and Keith in April 2025 — was his exit ramp into the year-long "
                      "absence."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="The industry's most committed serial reinventor. The famous versions, in order: "
             "<b>Lionheart</b> &rarr; <b>Y2J</b> &rarr; the suit &rarr; <b>the List</b> &rarr; "
             "<b>the Painmaker / Le Champion</b> &rarr; <b>the Learning Tree</b>.",
        cards=[
            dict(mono="LH", era="Mexico, Japan, ECW, WCW &middot; 1990&ndash;1999", name="Lionheart",
                 desc="The globe-trotting junior heavyweight: CMLL, WAR's junior division, ECW TV "
                      "Champion, WCW Cruiserweight Champion — and, in WCW's midcard, the inventor "
                      "of the whiny conspiracy-victim heel ('1,004 holds') that previewed "
                      "everything after."),
            dict(mono="Y2", era="WWF/WWE &middot; 1999&ndash;2005", name="Y2J",
                 desc="Debuted August 9, 1999, interrupting The Rock mid-promo with the millennium "
                      "countdown. Motor-mouthed, sequin-shirted, and underneath the catchphrases "
                      "the man who beat Rock and Austin in one night to unify the belts."),
            dict(mono="SU", era="WWE &middot; 2008&ndash;2010", name="The suit",
                 desc="The post-Michaels-feud sociopath: slow cadence, tailored suits, 'gelatinous "
                      "parasites.' Three World Heavyweight reigns came out of it, and it remains "
                      "the template heels reach for when they want to be taken seriously."),
            dict(mono="LI", era="WWE &middot; 2016&ndash;2017", name="The List of Jericho",
                 desc="Scarves, 'stupid idiot,' Gillberg-adjacent pettiness, and a clipboard that "
                      "became the hottest prop in wrestling. The Festival of Friendship breakup "
                      "with Kevin Owens is the era's masterpiece."),
            dict(mono="PM", era="NJPW/AEW &middot; 2018&ndash;2022", name="The Painmaker / Le Champion",
                 desc="Leather, spikes and violence for the Omega and Naito matches in Japan; then "
                      "AEW's founding champion, demanding respect in a suit while a stadium sang "
                      "his entrance music at him."),
            dict(mono="LT", era="AEW &middot; 2024&ndash;present", name="The Learning Tree / the Cornerstone",
                 desc="The heat-seeking mentor of 2024-25, retired by the hiatus. Since the April "
                      "2026 Winnipeg return the presentation is closer to earnest legacy-mode — a "
                      "'Cornerstone' trademark was filed during the absence — with the stated goal "
                      "of a tenth world title."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="A ten-minute draw in Ponoka, Alberta to first champion of two companies.",
        rows=[
            dict(year="1990", title="Debut",
                 desc="October 2, 1990, a time-limit draw with Lance Storm — both trained at the "
                      "Hart Brothers school in Calgary."),
            dict(year="1994", title="The world tour",
                 desc="CMLL in Mexico, Germany, then Japan's WAR promotion — the junior-heavyweight "
                      "education that built the style."),
            dict(year="1996", title="ECW, then WCW",
                 desc="ECW Television Champion; signs with WCW that summer, wins the Cruiserweight "
                      "title and invents the conspiracy-heel act the company never pushed."),
            dict(year="1999", title="The countdown hits zero",
                 desc="August 9, 1999: the Y2J debut, interrupting The Rock on Raw in Chicago."),
            dict(year="2001", title="Undisputed",
                 desc="First world title from The Rock at No Mercy on October 21; then Rock and "
                      "Austin in one night at Vengeance on December 9 to become the first "
                      "Undisputed WWF Champion."),
            dict(year="2008", title="The reinvention",
                 desc="The Shawn Michaels feud — Wrestlemania match, the punch through the "
                      "JeriTron, the No Mercy ladder match — births the suit-wearing heel and "
                      "three World Heavyweight reigns."),
            dict(year="2016", title="The List",
                 desc="The scarf-and-clipboard renaissance, and the Festival of Friendship with "
                      "Kevin Owens in early 2017."),
            dict(year="2018", title="The Painmaker pivot",
                 desc="Wrestle Kingdom 12 against Kenny Omega on January 4 — a 47-year-old "
                      "legend voluntarily becoming an outsider again. IWGP Intercontinental "
                      "Championship follows."),
            dict(year="2019", title="First AEW World Champion",
                 desc="Signs with the startup in January; beats Adam Page at All Out on August 31 "
                      "for the inaugural title; forms the Inner Circle."),
            dict(year="2022", title="The Wednesday institution",
                 desc="ROH World Championship from Claudio Castagnoli at Grand Slam on September "
                      "21; the Jericho Appreciation Society era."),
            dict(year="2024", title="The Learning Tree",
                 desc="FTW Championship from HOOK in April; loses it at Wembley in August; wins "
                      "the Ladder War over Mark Briscoe on October 23 for a second ROH World "
                      "Championship — world title nine."),
            dict(year="2025", title="The vanishing",
                 desc="Loses the ROH title to Bandido, title vs. mask, at Dynasty on April 6 — "
                      "then disappears from AEW television for a year while WWE rumors swirl and "
                      "the contract reportedly freezes."),
            dict(year="2026", title="Home",
                 desc="Returns April 1 in Winnipeg — 'I'm home.' Loses the TNT title challenge to "
                      "Kevin Knight on August 12 via Don Callis screwdriver; enters the All In: "
                      "London Casino Gauntlet on August 30 chasing a tenth world title and comes "
                      "up short as Andrade wins."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Shawn Michaels",
                 desc="The 2008 feud is the standard modern heel-turn syllabus: the idol worship, "
                      "the punch through the JeriTron 5000 that hit Michaels' wife, the "
                      "unsanctioned match, the No Mercy ladder match of October 5, 2008. It "
                      "transformed Jericho from nostalgic act to the most hated man on the "
                      "roster, and he has called it his favorite work of his career."),
            dict(name="Rey Mysterio",
                 desc="The 2009 masterclass: Jericho weaponised 1990s Mexico footage, kept "
                      "snatching at the mask, took a record ninth Intercontinental Championship "
                      "off Mysterio at Extreme Rules on June 7, 2009, and lost the rematch that "
                      "mattered — title versus mask at The Bash on June 28, with Mysterio "
                      "unmasking him mid-move for the finish."),
            dict(name="Kenny Omega",
                 desc="Alpha vs. Omega at Wrestle Kingdom 12, January 4, 2018 — the surprise that "
                      "reset his career's ceiling and previewed the AEW signing. The Painmaker "
                      "run and the credibility it bought him with a new generation trace to this "
                      "one bet on himself."),
            dict(name="MJF",
                 desc="The multi-year AEW apprenticeship-as-blood-feud: the Inner Circle "
                      "recruitment, the betrayal, the Labour of Love, and a dynamic that "
                      "resurfaced instantly when they collided in the All In: London Casino "
                      "Gauntlet on August 30, 2026, Jericho locking the Walls on him mid-match."),
            dict(name="CM Punk",
                 desc="The 'best in the world' feud of 2012 — WrestleMania XXVIII on April 1 and "
                      "the Chicago Street Fight rematch — fought explicitly over Jericho's own "
                      "catchphrase, and lost."),
            dict(name="HOOK and Bandido",
                 desc="The Learning Tree's two reckonings: the generational FTW feud with HOOK "
                      "through 2024's Dynasty and Wembley bookends, and the Bandido "
                      "title-versus-mask match at Dynasty on April 6, 2025 — the loss he "
                      "disappeared on, and the last image of Jericho before the year away."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Music",
        lead="The busiest extracurricular resume in wrestling &mdash; kept to the flagship items.",
        rows=[
            dict(when="1999&ndash;", title="Fozzy", kind="Band",
                 desc="Lead vocalist since 1999. 'Judas' (2017) became a streaming phenomenon and "
                      "doubles as his AEW entrance theme, sung by entire arenas."),
            dict(when="2013&ndash;", title="Talk Is Jericho", kind="Podcast",
                 desc="Twice-weekly interview podcast, one of wrestling's longest-running."),
            dict(when="2007&ndash;", title="A Lion's Tale and sequels", kind="Books",
                 desc="A Lion's Tale (2007), Undisputed, Best in the World and more — the "
                      "multi-volume autobiography project."),
            dict(when="2011", title="Dancing with the Stars", kind="TV",
                 desc="Season 12 contestant — one entry in a long broadcast resume that also "
                      "includes hosting and metal-scene documentary work."),
            dict(when="2018&ndash;", title="Chris Jericho's Rock 'N' Wrestling Rager at Sea", kind="Cruise",
                 desc="The periodic themed cruise combining Fozzy, wrestling and the extended "
                      "Jericho universe."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The firsts and records, with the arithmetic shown.",
        stats=[
            ("2", "Inaugural world titles"),
            ("9", "World title reigns"),
            ("9", "IC reigns"),
        ],
        rows=[
            dict(name="First Undisputed WWF Champion",
                 sub="Vengeance, December 9, 2001: beat The Rock for the WCW/World Championship "
                     "and Steve Austin for the WWF Championship in the same night, unifying the "
                     "two lineages. Nobody else has won both in one evening."),
            dict(name="First AEW World Champion",
                 sub="All Out, August 31, 2019, over Adam Page — then held the title 182 days "
                     "through the company's launch. The only man to be the first champion of two "
                     "major promotions' top titles."),
            dict(name="Nine world championship reigns",
                 sub="Six in WWE (two WCW/World, one Undisputed, three World Heavyweight), one "
                     "AEW, two ROH — the count Wrestling Inc published when the ninth arrived in "
                     "the October 23, 2024 Ladder War. WWE-only counts stop at six, which is why "
                     "sources disagree."),
            dict(name="Record nine Intercontinental Championship reigns",
                 sub="Still the record in 2026 — the ninth taken from Rey Mysterio at Extreme "
                     "Rules on June 7, 2009."),
            dict(name="The 2025-26 vanishing act",
                 sub="Last match April 6, 2025; returned April 1, 2026 in Winnipeg. He no-showed "
                     "a year of WWE-return prophecies — Meltzer and Fightful both reported he was "
                     "not expected in WWE at all — while AEW reportedly froze the contract "
                     "clock."),
            dict(name="Champion in five decades of calendar years",
                 sub="Titles won in the 1990s (WCW Cruiserweight, ECW TV), 2000s, 2010s and 2020s "
                     "— with the 2024 ROH reign extending the streak past age 54."),
            dict(name="The Wembley Casino Gauntlet, August 30, 2026",
                 sub="Entered sixth at 55, eliminated Tommaso Ciampa while the stadium sang "
                     "Judas, and had MJF in the Walls when the next entrant broke it up. Andrade "
                     "won the world title shot; Jericho's stated target remains a tenth world "
                     "championship."),
        ],
        footnote=("Deliberately absent: a tag team reign count (partners are documented, the "
                  "total was not verified), a career win-loss record (none exists), social "
                  "handles, and Observer ratings. The nine-world-title figure is the "
                  "cross-promotion count; WWE materials recognise six."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Chris_Jericho"),
        dict(k="Yahoo Sports", v="The April 2026 Winnipeg return and what the hiatus was",
             href="https://sports.yahoo.com/articles/chris-jericho-returns-home-aew-123616813.html"),
        dict(k="Wrestling Inc", v="Declaring for the All In: London Casino Gauntlet",
             href="https://www.wrestlinginc.com/2245187/chris-jericho-more-declare-aew-casino-gauntlet-wembley/"),
        dict(k="F4W/WON", v="The Kevin Knight TNT Championship challenge",
             href="https://www.f4wonline.com/news/aew/mjf-casino-gauntlet-qualifier-chris-jericho-tnt-title-challenge-aew-dynamite/"),
        dict(k="NoDQ", v="Casino Gauntlet results, All In: London",
             href="https://nodq.com/news/results-of-casino-gauntlet-match-at-aew-all-in-london-2026/"),
        dict(k="Wrestling Inc", v="The 2024 Ladder War &mdash; world title number nine",
             href="https://www.wrestlinginc.com/1696261/returning-njpw-star-confronts-chris-jericho-roh-world-title-win-aew-dynamite/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Chris Jericho still in AEW, or did he go back to WWE?",
            a="He is in AEW. After his April 6, 2025 loss to Bandido he disappeared from television "
              "for a year, his contract reportedly frozen during the absence, and the rumor mill "
              "spent that year booking his WWE homecoming &mdash; he no-showed every predicted "
              "date, and both Dave Meltzer and Fightful reported he was not expected in WWE at all. "
              "He returned on the April 1, 2026 Dynamite in his hometown of Winnipeg with two "
              "words: &ldquo;I&rsquo;m home.&rdquo; Since then he has challenged Kevin Knight for "
              "the TNT Championship (August 12, a loss via Don Callis screwdriver) and entered the "
              "Casino Gauntlet at All In: London on August 30, 2026, stating plainly that he wants "
              "to be AEW World Champion again.",
            q_ld="Is Chris Jericho still in AEW, or did he return to WWE?",
            a_ld="Chris Jericho is in AEW. He was absent from AEW television for a year after "
                 "losing to Bandido on April 6, 2025, during which WWE return rumors circulated "
                 "but reporters at the Wrestling Observer and Fightful said no WWE return was "
                 "expected. He returned on the April 1, 2026 episode of Dynamite in Winnipeg, "
                 "unsuccessfully challenged Kevin Knight for the TNT Championship on August 12, "
                 "2026, and competed in the Casino Gauntlet at All In: London on August 30, 2026, "
                 "which Andrade won."),
        dict(
            q="How many world titles has Chris Jericho won?",
            a="Nine, by the cross-promotion count: six in WWE &mdash; two WCW/World Championship "
              "reigns, the first Undisputed WWF Championship, three World Heavyweight "
              "Championships &mdash; plus the inaugural AEW World Championship and two ROH World "
              "Championships. You will also see &ldquo;six&rdquo; (WWE-only) and &ldquo;seven&rdquo; "
              "(pre-2024 cross-promotion counts); the nine figure is the one Wrestling Inc used "
              "when the second ROH reign arrived in October 2024, and this page adopts it with the "
              "arithmetic shown.",
            q_ld="How many world championships has Chris Jericho won?",
            a_ld="Nine, counting across promotions: two WCW/World Championship reigns, one "
                 "Undisputed WWF Championship, three World Heavyweight Championships, the "
                 "inaugural AEW World Championship, and two ROH World Championships. Counts that "
                 "consider only WWE-recognised reigns give six, which is why published figures "
                 "differ."),
        dict(
            q="What happened in the Casino Gauntlet at All In: London?",
            a="Jericho entered sixth in the match for a future AEW World Championship shot on "
              "August 30, 2026 at Wembley. He eliminated Tommaso Ciampa &mdash; the crowd sang "
              "&ldquo;Judas&rdquo; &mdash; and had MJF in the Walls of Jericho before the next "
              "entrant broke it up. <b>Andrade El Idolo</b> won the match and the title shot. It "
              "was Jericho&rsquo;s first All In appearance since losing the FTW title at Wembley "
              "in 2024, and it leaves him at nine world titles, still one short of the tenth he "
              "returned for.",
            q_ld="What happened with Chris Jericho in the Casino Gauntlet at AEW All In: London 2026?",
            a_ld="At All In: London on August 30, 2026, Chris Jericho entered the Casino Gauntlet "
                 "as the sixth competitor in a match for a future AEW World Championship "
                 "opportunity. He eliminated Tommaso Ciampa while the Wembley crowd sang Judas, "
                 "and applied the Walls of Jericho to MJF before being interrupted. Andrade El "
                 "Idolo won the match."),
        dict(
            q="Was Jericho really the first Undisputed Champion?",
            a="Yes &mdash; and it took beating The Rock and Stone Cold Steve Austin in the same "
              "night. At Vengeance on December 9, 2001 he defeated The Rock to win the WCW/World "
              "Championship, then defeated Austin to add the WWF Championship, unifying the two "
              "lineages into the Undisputed WWF Championship. He held it until Triple H beat him "
              "at WrestleMania X8 on March 17, 2002. Eighteen years later he became the first AEW "
              "World Champion too &mdash; the only wrestler to be the inaugural holder of two "
              "major promotions&rsquo; top titles.",
            q_ld="Was Chris Jericho the first Undisputed WWF Champion?",
            a_ld="Yes. At Vengeance on December 9, 2001, Chris Jericho defeated The Rock to win "
                 "the WCW/World Championship and then defeated Stone Cold Steve Austin to win the "
                 "WWF Championship in the same night, unifying the titles as the first Undisputed "
                 "WWF Champion. He lost the championship to Triple H at WrestleMania X8 on March "
                 "17, 2002. In 2019 he also became the first AEW World Champion."),
        dict(
            q="Does Jericho still hold the Intercontinental record?",
            a="Yes &mdash; <b>nine reigns</b>, still the record as of August 2026. The ninth came "
              "against Rey Mysterio at Extreme Rules on June 7, 2009, in the middle of the feud "
              "where he kept trying to unmask him; Mysterio took the title back three weeks later "
              "in a title-versus-mask match. For context on the other kind of IC record: "
              "Gunther&rsquo;s 666-day single reign (2022&ndash;24) is the longest reign, while "
              "Jericho&rsquo;s nine remain the most.",
            q_ld="Does Chris Jericho still hold the record for most Intercontinental Championship reigns?",
            a_ld="Yes. Chris Jericho holds the record with nine WWE Intercontinental Championship "
                 "reigns, the ninth won from Rey Mysterio at Extreme Rules on June 7, 2009. The "
                 "separate record for the longest single reign belongs to Gunther at 666 days."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Christopher Keith Irvine"),
        dict(label="Born", value="November 9, 1970",
             sub="Manhasset, New York; raised in Winnipeg, Manitoba &middot; age 55"),
        dict(label="Billed from", value="Winnipeg, Manitoba",
             sub="dual American-Canadian citizen; son of NHL player Ted Irvine"),
        dict(label="Height", value="6&#8242;0&#8243;", sub="183 cm (billed)"),
        dict(label="Weight", value="227 lb", sub="103 kg (billed)"),
        dict(label="Debut", value="October 2, 1990",
             sub="Ponoka, Alberta &mdash; a ten-minute draw with Lance Storm"),
        dict(label="Trained by", value="Hart Brothers school, Calgary"),
        dict(label="Ring name", value="Chris Jericho",
             sub="from Helloween's album Walls of Jericho; variants Lionheart, Y2J, the Painmaker, "
                 "Le Champion, the Ocho, the Learning Tree"),
        dict(label="Signature", value="Walls of Jericho &middot; Codebreaker &middot; Judas Effect "
                                      "&middot; Lionsault"),
        dict(label="Entrance theme", value="&ldquo;Judas&rdquo; by Fozzy",
             sub="his own band &mdash; the crowd sings it back, including at Wembley on August 30, 2026"),
        dict(label="Brand", value="AEW", sub="returned April 1, 2026 after a year away"),
        dict(label="Also known as", value="Y2J &middot; Le Champion &middot; The Painmaker &middot; The Ocho"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1970-11-09",
    bornplace="Manhasset, New York",
    nationality="Canada",
    height_cm=183,
    weight_kg=103,
    ld=dict(
        alternateName=["Christopher Keith Irvine", "Y2J", "Lionheart", "Le Champion",
                       "The Painmaker", "The Ocho", "The Learning Tree"],
        award=["Undisputed WWF Championship (first champion, 2001)",
               "WCW/World Championship (2 reigns)",
               "World Heavyweight Championship (3 reigns)",
               "AEW World Championship (inaugural champion, 2019)",
               "ROH World Championship (2 reigns)",
               "WWE Intercontinental Championship (record 9 reigns)",
               "IWGP Intercontinental Championship (1 reign)",
               "FTW Championship (1 reign)",
               "WCW Cruiserweight Championship",
               "ECW World Television Championship"],
        knowsAbout=["Professional wrestling", "WWE", "AEW", "NJPW", "Heavy metal music",
                    "Podcasting", "Lucha libre"],
        description="Chris Jericho, born Christopher Keith Irvine, is a Canadian-American "
                    "professional wrestler, musician and podcaster. He became the first Undisputed "
                    "WWF Champion on December 9, 2001 by beating The Rock and Steve Austin in one "
                    "night, and the inaugural AEW World Champion on August 31, 2019. He has won "
                    "nine world championships across WWE, AEW and ROH, holds the record nine WWE "
                    "Intercontinental Championship reigns, fronts the metal band Fozzy, and hosts "
                    "the Talk Is Jericho podcast. After a year-long absence he returned to AEW on "
                    "April 1, 2026 and remains active as of August 2026.",
        sameAs=["https://en.wikipedia.org/wiki/Chris_Jericho",
                "https://www.wwe.com/superstars/chris-jericho"],
    ),
)
