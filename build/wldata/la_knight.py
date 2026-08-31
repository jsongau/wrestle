# -*- coding: utf-8 -*-
"""LA Knight - dossier data.

Sources: web-verified August 31, 2026 (Wikipedia, Sports Illustrated/FanNation, CBS
Sports, SmackDown Hotel profile and event archives). Every match row carries a
day-precision date confirmed in at least one of those sources.

Deliberate omissions:
  * No career win-loss total - no verified figure exists and none is invented.
  * No signature-match ratings section: no Wrestling Observer rating for any LA
    Knight match could be verified in this pass, and none is invented. The lead for
    that slot explains the absence in place.
  * The Impact World Championship reign is asserted by every source, but the
    published table's day count (146) does not reconcile with its own endpoints
    (August 24, 2017 - February 1, 2018 is 161 days); only the reign and its rough
    span are published here.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2021-06-13", promo="WWE", landmark=True,
         event="NXT TakeOver: In Your House", opponent="Cameron Grimes",
         stip="Ladder match — first WWE championship", title="Million Dollar Championship"),
    dict(result="L", date="2022-04-02", promo="WWE",
         event="NXT Stand & Deliver", opponent="Gunther", opponent_html=True,
         stip="Singles — his final NXT match", title=""),
    dict(result="W", date="2023-08-05", promo="WWE", type="tag",
         event="SummerSlam — Detroit", opponent="The Slim Jim Battle Royal field",
         stip="Battle royal — the breakout summer's first trophy", title=""),
    dict(result="W", date="2023-09-02", promo="WWE",
         event="Payback", opponent="The Miz",
         stip="Singles — John Cena as special guest referee", title=""),
    dict(result="L", date="2023-11-04", promo="WWE", landmark=True,
         event="Crown Jewel — Riyadh", opponent="Roman Reigns",
         stip="Singles — first world title match, eight months into the run",
         title="Undisputed WWE Universal Championship"),
    dict(result="L", date="2024-01-27", promo="WWE", type="tag",
         event="Royal Rumble — St. Petersburg", opponent="Roman Reigns, Randy Orton & AJ Styles",
         stip="Fatal four-way — Reigns retains", title="Undisputed WWE Universal Championship"),
    dict(result="W", date="2024-04-07", promo="WWE", landmark=True,
         event="WrestleMania 40 Night 2", opponent="AJ Styles",
         stip="Singles — his first WrestleMania match, at 41", title=""),
    dict(result="W", date="2024-08-03", promo="WWE", landmark=True,
         event="SummerSlam — Cleveland", opponent="Logan Paul",
         stip="Singles — first main-roster title", title="WWE United States Championship"),
    dict(result="W", date="2024-11-02", promo="WWE", type="tag",
         event="Crown Jewel — Riyadh", opponent="Andrade & Carmelo Hayes",
         stip="Triple threat — retains", title="WWE United States Championship"),
    dict(result="L", date="2024-11-30", promo="WWE",
         event="Survivor Series: WarGames", opponent="Shinsuke Nakamura",
         stip="Singles — the 119-day reign ends", title="WWE United States Championship"),
    dict(result="W", date="2025-03-07", promo="WWE",
         event="SmackDown", opponent="Shinsuke Nakamura",
         stip="Singles — the receipt, and a second reign", title="WWE United States Championship"),
    dict(result="L", date="2025-04-19", promo="WWE", landmark=True,
         event="WrestleMania 41 Night 1", opponent="Jacob Fatu",
         stip="Singles — the 43-day reign ends", title="WWE United States Championship"),
    dict(result="W", date="2025-07-12", promo="WWE",
         event="Saturday Night's Main Event XL — Atlanta", opponent="Seth Rollins",
         stip="Singles — his win on the card where Gunther retired Goldberg", title=""),
    dict(result="L", date="2025-08-31", promo="WWE", type="tag",
         event="Clash in Paris", opponent="Seth Rollins, CM Punk & Damian Priest",
         stip="Fatal four-way — Rollins retains", title="World Heavyweight Championship"),
    dict(result="W", date="2026-04-18", promo="WWE", type="tag", landmark=True,
         event="WrestleMania 42 Night 1 — Las Vegas", opponent="Logan Paul, Austin Theory & IShowSpeed",
         stip="Six-man tag — with The Usos against The Vision's trio", title=""),
    dict(result="W", date="2026-08-01", promo="WWE", type="tag", landmark=True,
         event="SummerSlam Night 1 — Minneapolis", opponent="The Bloodline",
         stip="Six-man tag — with Solo Sikoa and Royce Keys over Jacob Fatu and The Usos", title=""),
    dict(result="NC", date="2026-08-24", promo="WWE", type="tag",
         event="Raw", opponent="The Usos",
         stip="Tag — with Solo Sikoa; thrown out when Royce Keys and OTM attack all four", title=""),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Gunther": "gunther"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="la-knight",
    name="LA Knight",
    realname="Shaun Edward Ricker",
    epithet="The Megastar",
    hook="Record & Titles",

    meta_desc=("LA Knight, The Megastar, is a two-time United States Champion and former Impact "
               "World Champion who broke out in WWE at 40. Now he leads the fight against Roman "
               "Reigns' reformed Bloodline. Full record, titles, factions, records and career."),
    og_desc=("YEAH! The Megastar: a 20-year overnight success, two United States Championship "
             "reigns, an Impact World title as Eli Drake - and a 2026 war against the reformed "
             "Bloodline, with Solo Sikoa at his side."),
    tw_desc="LA Knight: the 20-year overnight success - 2x US Champion, Impact World Champion, Bloodline resistance leader.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2003",
    height_imp="6&#8242;1&#8243;",
    weight_lb="234",
    world_titles="1",
    vitals_tagline="YEAH!",
    support_note="Merch &middot; Games &middot; Watch",
    sp_items=[
        dict(ic="LA", title="WWE Shop", sub="Yeah! tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable in recent WWE 2K entries",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="IW", title="Impact/TNA archive", sub="The Eli Drake years, 2015-2019",
             tag="Watch", href="https://www.thesmackdownhotel.com/wrestlers/la-knight"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/la-knight"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Eli Drake &middot; Max Dupri &middot; The Megastar",
    hero_tag="Hagerstown, Maryland &middot; billed from Los Angeles &middot; <em>Independents "
             "&middot; TNA/Impact &middot; NWA &middot; NXT &middot; WWE &middot; "
             "2003&ndash;present</em>",
    now_label="NOW",
    now_bold="Raw, no championship",
    now_tail=" &middot; leading the resistance to Roman Reigns&rsquo; reformed Bloodline with Solo "
             "Sikoa at his side &mdash; and, since August 24, with Royce Keys and OTM attacking "
             "everyone",
    hstats=[
        dict(value="2",    x=True,  label="US Title Reigns"),
        dict(value="1",    x=True,  label="Impact World Title"),
        dict(value="40",   x=False, label="Age at the WWE Breakout"),
        dict(value="2003", x=False, label="First Match"),
    ],
    ghost_link="Twenty years of names, one catchphrase that finally stuck",
    vlabel="Est. 2003 &middot; Hagerstown, Maryland",
    mono="LA",

    # ---------------------------------------------------------------- 01 overview
    # index into overview of the correction paragraph -> the framed
    # "Setting one thing straight" callout (aside.corr) on the page
    correction=1,
    overview=[
        "<b>LA Knight</b> got over on his own and made WWE catch up. Through 2023 the crowds "
        "adopted his &ldquo;YEAH!&rdquo; call-and-response faster than the company adopted him, "
        "and by that autumn a man who had been repackaged as a talent agent eighteen months "
        "earlier was challenging Roman Reigns at Crown Jewel. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">40</span>'
        '<span class="pull-cap">his age when the breakout hit &mdash; twenty years after his first match</span></span>'
        "The peak so far: two United States Championship reigns &mdash; the first won from "
        "Logan Paul at SummerSlam 2024 &mdash; and, in 2026, the role of chief dissident against "
        "Roman Reigns&rsquo; reformed Bloodline, a campaign that has put him alongside Solo Sikoa "
        "and, at SummerSlam on August 1, on the winning side of a six-man over the "
        "Bloodline&rsquo;s full trio.",

        "The &ldquo;overnight success at 40&rdquo; framing undersells him by two decades. Shaun "
        "Ricker had his first match in 2003, worked WWE developmental as Slate Randall in "
        "2013&ndash;14, and spent 2015&ndash;19 in TNA/Impact as <b>Eli Drake</b> &mdash; where he "
        "won the <b>Impact World Championship</b> in the August 2017 Gauntlet for the Gold and "
        "held it into early 2018. He arrived in WWE already a former world champion with a decade "
        "of talking behind him; the published Impact table&rsquo;s day count (146) does not "
        "reconcile with its own endpoints, so this page asserts the reign and its span rather "
        "than a day figure. What was new in 2023 was not the act. It was the audience size.",

        "The WWE run itself has been a study in resilience against repackaging: the Million "
        "Dollar Championship ladder-match win in NXT in June 2021, the Max Dupri talent-agent "
        "detour of 2022, and then the rebuild &mdash; the Slim Jim battle royal and Miz feud in "
        "the breakout summer, the Reigns title shots, and a first WrestleMania match at 41, "
        "beating AJ Styles at WrestleMania 40. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">119</span>'
        '<span class="pull-cap">days of the first United States Championship reign, won from Logan Paul at SummerSlam 2024</span></span>'
        "The United States Championship followed twice &mdash; 119 days from SummerSlam 2024, 43 "
        "more in 2025 &mdash; before Jacob Fatu took the belt at WrestleMania 41. A 2025 detour "
        "into the World Heavyweight picture produced a clean win over Seth Rollins at Saturday "
        "Night&rsquo;s Main Event XL and a four-way loss at Clash in Paris.",

        "The 2026 story is the one he called in advance. From his May 19 return onward he told "
        "The Usos on television that their arrangement with Roman Reigns was the same movie as "
        "the original Bloodline; they took the ula falas anyway. Solo Sikoa proved Knight right "
        "on the August 17 Raw, spiking Reigns mid-ceremony and standing with him &mdash; a week "
        "after Knight and Solo had beaten the Bloodline&rsquo;s trio at SummerSlam with Royce "
        "Keys. Then the week after that, Keys and his debuting OTM faction attacked Knight, Solo "
        "and The Usos alike, collapsing the August 24 main event into a no-contest. As of August "
        "31, 2026 Knight holds no championship, wrestles on Raw, and is the man who saw all of it "
        "coming &mdash; which, as he would note at length, is the whole gimmick.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("2&times;", "United States"),
            ("119",      "Day first US reign"),
            ("1",        "Impact World title"),
            ("1",        "Million Dollar title"),
            ("41",       "Age at first WrestleMania"),
            ("2003",     "First match"),
        ],
        lead=("Seventeen documented WWE bouts &mdash; the Million Dollar ladder match, the breakout "
              "summer, both United States reigns at both ends, and the 2026 Bloodline resistance "
              "in progress. The Eli Drake years appear in the titles section rather than here: "
              "day-precision dates for the TNA/Impact matches were not verified in this pass. No "
              "career win&ndash;loss total is published because no verified one exists. Filter by "
              "match type, tap any column header to sort, and turn spoilers on to reveal "
              "results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("Nothing is listed here by design: no Wrestling Observer rating for an LA "
                    "Knight match could be verified in this pass, and this site does not invent "
                    "them. The bouts his reputation actually rests on are in the record above "
                    "&mdash; the Cena-refereed Payback win over The Miz, the SummerSlam 2024 Logan "
                    "Paul match, and the 2026 six-mans against the reformed Bloodline &mdash; and "
                    "his case has always been prosecuted on the microphone anyway."),
    signature_count_word="zero",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("2&times;", "United States reigns"),
            ("1",        "Impact World title"),
            ("1",        "Million Dollar title"),
            ("0",        "WWE world titles — so far"),
        ],
        lead=("A world title from the Impact years, two United States reigns from the WWE peak, "
              "and one deliberately odd heirloom in between. Where a published table conflicts "
              "with its own arithmetic, the conflict is printed rather than resolved."),
        rows=[
            dict(ic="S", name="WWE United States Championship", count="2",
                 sub="2024 &middot; def. Logan Paul at SummerSlam on August 3, lost to Shinsuke "
                     "Nakamura at Survivor Series: WarGames on November 30 &middot; <b>119 "
                     "days</b>, with a Crown Jewel triple-threat defence &middot; 2025 &middot; "
                     "regained from Nakamura on the March 7 SmackDown, lost to Jacob Fatu at "
                     "WrestleMania 41 Night 1 &middot; 43 days"),
            dict(ic="W", name="Impact World Championship", count="1",
                 sub="As Eli Drake &middot; won the Gauntlet for the Gold in August 2017, held "
                     "into early 2018 &middot; the published table gives August 24, 2017 &ndash; "
                     "February 1, 2018 alongside a 146-day count that does not follow from those "
                     "endpoints, so no day figure is adopted here"),
            dict(ic="M", name="Million Dollar Championship", count="1",
                 sub="June 13 &ndash; August 22, 2021 &middot; won the ladder match against "
                     "Cameron Grimes at NXT TakeOver: In Your House, with Ted DiBiase's blessing "
                     "and then his interference &middot; 70 days"),
            dict(ic="K", name="TNA King of the Mountain Championship", count="1",
                 sub="May 31 &ndash; August 4, 2016, as Eli Drake"),
            dict(ic="T", name="Impact World Tag Team Championship", count="1",
                 sub="April 22 &ndash; May 17, 2018, with Scott Steiner"),
            dict(ic="B", name="Slim Jim Battle Royal", count="1",
                 sub="SummerSlam, August 5, 2023 &mdash; the breakout summer's first trophy"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Alliances",
        lead="A career act built on working alone, and the two 2026 alliances that broke the "
             "rule.",
        cards=[
            dict(era="WWE &middot; 2022",
                 name="Maximum Male Models",
                 members="Max Dupri (LA Knight), ma.&ccedil;&eacute;, man.soor, Maxxine Dupri",
                 desc="The repackage he escaped: WWE rebooted him as Max Dupri, a fashion-agency "
                      "impresario who did not wrestle. He walked off the gimmick on the September "
                      "30, 2022 SmackDown and took the LA Knight name back; the breakout followed "
                      "within a year. Regularly cited since as the modern case for letting a "
                      "wrestler keep the act that works."),
            dict(era="WWE &middot; 2026",
                 name="Knight & The Usos",
                 members="LA Knight, Jey Uso, Jimmy Uso",
                 desc="The WrestleMania 42 alliance - a six-man win over The Vision's Logan Paul, "
                      "Austin Theory and IShowSpeed on April 18. It dissolved over principle: when "
                      "the twins rejoined Roman Reigns' reformed Bloodline, Knight spent the "
                      "summer telling them, on television, that they had seen this movie before, "
                      "and became the story's designated truth-teller."),
            dict(era="WWE &middot; 2026&ndash;present",
                 name="Knight & Solo Sikoa",
                 members="LA Knight, Solo Sikoa, with Royce Keys briefly alongside",
                 desc="The resistance: Knight, Solo and Royce Keys beat the Bloodline's Jacob Fatu "
                      "and The Usos at SummerSlam on August 1; Solo formally crossed over on "
                      "August 17, spiking Reigns mid-ceremony and standing with Knight. Then Keys "
                      "and his debuting OTM faction attacked everyone on August 24 - so the "
                      "alliance is two men, at war on two fronts, as of August 31, 2026."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Five names in twenty-three years, and the last one only worked once he was allowed "
             "to keep it: <b>Deuce</b> &rarr; <b>Slate Randall</b> &rarr; <b>Eli Drake</b> &rarr; "
             "<b>Max Dupri</b> &rarr; <b>LA Knight</b>.",
        cards=[
            dict(mono="SR", era="Independents &amp; NXT &middot; 2003&ndash;2014", name="Deuce / Slate Randall",
                 desc="The journeyman decade: an HWA debut in 2003, television extra work, and a "
                      "2013-14 NXT developmental run as Slate Randall that went nowhere. The reps "
                      "were real even when the bookings were not."),
            dict(mono="ED", era="TNA/Impact &amp; NWA &middot; 2014&ndash;2021", name="Eli Drake",
                 desc="The proof of concept: Impact World Champion in 2017, King of the Mountain "
                      "Champion, tag gold with Scott Steiner, and the 'Dummy, yeah!' vocabulary "
                      "that LA Knight's catchphrase grew out of. A world champion talker waiting "
                      "for a bigger room."),
            dict(mono="MD", era="WWE &middot; 2022", name="Max Dupri",
                 desc="The cautionary tale: a non-wrestling talent-agent gimmick fronting Maximum "
                      "Male Models. He abandoned it on air within months - the rare repackage "
                      "reversed by sheer refusal."),
            dict(mono="LA", era="WWE &middot; 2021, 2022&ndash;present", name="The Megastar",
                 desc="The act as he always intended it: third-person self-promotion, the YEAH! "
                      "call-and-response, 'Let me talk to ya.' Crowd-adopted in 2023 before WWE "
                      "fully committed, US Champion twice since, Bloodline dissident now."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Twenty years of almosts, then the loudest catchphrase in the company.",
        rows=[
            dict(year="2003", title="Debut",
                 desc="First matches in the Heartland Wrestling Association as Deuce, after "
                      "starting training in March 2003."),
            dict(year="2013", title="First WWE run",
                 desc="NXT developmental as Slate Randall, 2013-14. Released without a television "
                      "story to his name."),
            dict(year="2017", title="Impact World Champion",
                 desc="As Eli Drake, wins the Gauntlet for the Gold in August 2017 and carries "
                      "TNA/Impact's top title into 2018."),
            dict(year="2021", title="Back to WWE; Million Dollar Champion",
                 desc="Debuts in NXT as LA Knight and wins the Million Dollar Championship ladder "
                      "match at TakeOver: In Your House on June 13."),
            dict(year="2022", title="Max Dupri, briefly",
                 desc="Repackaged as a talent agent on SmackDown in May; walks off the gimmick by "
                      "September 30 and reclaims the LA Knight name."),
            dict(year="2023", title="The breakout",
                 desc="The crowd adopts YEAH! wholesale: the Slim Jim Battle Royal at SummerSlam "
                      "on August 5, the Cena-refereed Payback win over The Miz on September 2, "
                      "and a Crown Jewel title match with Roman Reigns on November 4."),
            dict(year="2024", title="United States Champion",
                 desc="Beats AJ Styles at WrestleMania 40 on April 7 - his first WrestleMania "
                      "match, at 41 - then takes the US title from Logan Paul at SummerSlam on "
                      "August 3 and holds it 119 days."),
            dict(year="2025", title="Second reign, and the world-title detour",
                 desc="Regains the title from Nakamura on March 7, loses it to Jacob Fatu at "
                      "WrestleMania 41 on April 19, beats Seth Rollins at Saturday Night's Main "
                      "Event XL on July 12, and drops the Clash in Paris four-way on August 31."),
            dict(year="2026", title="The Bloodline resistance",
                 desc="Wins the WrestleMania 42 six-man with The Usos on April 18, spends the "
                      "summer warning them about Roman Reigns, beats the reformed Bloodline at "
                      "SummerSlam on August 1 with Solo Sikoa and Royce Keys, gains Solo as an "
                      "ally on August 17 - and gets ambushed by Keys' OTM on August 24."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Roman Reigns and The Bloodline",
                 desc="Two chapters. In 2023 he was the hot challenger fed to the Tribal Chief at "
                      "Crown Jewel on November 4 and in the Royal Rumble four-way. In 2026 he is "
                      "the resistance: months of telling The Usos their reformed Bloodline is a "
                      "rerun, a SummerSlam six-man win over the group's trio on August 1, and the "
                      "recruitment - by argument - of Solo Sikoa. The rare feud where the "
                      "monologue is the weapon."),
            dict(name="Logan Paul",
                 desc="The SummerSlam 2024 title change, August 3 in Cleveland - Knight's first "
                      "main-roster championship, taken from the most protected part-timer in the "
                      "company - and the 2026 rematch by proxy, with Paul on the losing Vision "
                      "side of the WrestleMania 42 six-man."),
            dict(name="Jacob Fatu",
                 desc="The man who ended the second US reign at WrestleMania 41 on April 19, 2025, "
                      "and beat him again in the Backlash four-way that May. Now the enforcer on "
                      "the Bloodline side of Knight's 2026 war - the account is open on both "
                      "levels."),
            dict(name="The Miz",
                 desc="The breakout feud: two loud talkers arguing over which of them was the "
                      "act's rightful owner, settled at Payback on September 2, 2023 with John "
                      "Cena as special guest referee and the crowd entirely one-way. The night "
                      "the YEAH! movement stopped being deniable."),
            dict(name="Seth Rollins and The Vision",
                 desc="The 2025 world-title detour: a clean win over Rollins at Saturday Night's "
                      "Main Event XL on July 12, a DQ mess on Raw, and the Clash in Paris four-way "
                      "loss on August 31. The Vision's Logan Paul and Austin Theory then took the "
                      "tag titles from Knight's future allies The Usos - the threads all crossed "
                      "at WrestleMania 42."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Thin by design — the verified list is short, and nothing is added to pad it.",
        rows=[
            dict(when="2023", title="Slim Jim", kind="Sponsorship",
                 desc="Fronted the brand's WWE partnership in his breakout summer, including the "
                      "SummerSlam 2023 Slim Jim Battle Royal, which he won."),
            dict(when="2023&ndash;", title="WWE 2K", kind="Game",
                 desc="Playable in recent WWE 2K entries; Eli Drake has never appeared in a WWE "
                      "game."),
            dict(when="2016&ndash;19", title="The Fact of Life", kind="Television",
                 desc="His Impact-era talk segment as Eli Drake - the laboratory where most of "
                      "the current vocabulary was developed."),
            dict(when="2005&ndash;12", title="Reality and extra work", kind="Television",
                 desc="Pre-fame screen appearances, including a brief 2006 WWE cameo as 'Dick "
                      "Rick.' No film roles, autobiography or podcast could be verified, so none "
                      "are listed."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records and the milestones — a short list with a long runway behind it.",
        stats=[
            ("2",   "US title reigns"),
            ("1",   "Impact World title"),
            ("41",  "Age at first WrestleMania"),
        ],
        rows=[
            dict(name="Impact World Champion, 2017-18",
                 sub="Won the Gauntlet for the Gold in August 2017 as Eli Drake - a world "
                     "champion seven years before most WWE viewers had heard of him. The "
                     "published reign-length figure conflicts with its own dates and is not "
                     "repeated here."),
            dict(name="Two United States Championship reigns",
                 sub="119 days from beating Logan Paul at SummerSlam on August 3, 2024; 43 more "
                     "from March 7, 2025. Both reigns ended against the same family he is now at "
                     "war with - Nakamura aside: the second fell to Jacob Fatu at WrestleMania "
                     "41."),
            dict(name="First WrestleMania match at 41",
                 sub="WrestleMania 40 Night 2, April 7, 2024, beating AJ Styles - twenty-one "
                     "years after his first match. Among the latest first WrestleManias of any "
                     "featured modern star."),
            dict(name="Million Dollar Champion",
                 sub="Won the ladder match at NXT TakeOver: In Your House on June 13, 2021 - one "
                     "of only a handful of men to hold DiBiase's heirloom title since 1996."),
            dict(name="Got over without the machine",
                 sub="The 2023 YEAH! breakout was crowd-driven for months before WWE's booking "
                     "reflected it - the Payback win over The Miz with John Cena refereeing, on "
                     "September 2, 2023, is the accepted turning point."),
            dict(name="Beat the reformed Bloodline's trio at SummerSlam 2026",
                 sub="August 1, 2026, with Solo Sikoa and Royce Keys, over Jacob Fatu and The "
                     "Usos - the first clean six-man loss the reformed group had taken, and the "
                     "match that legitimised the resistance storyline."),
            dict(name="The repackage he reversed himself",
                 sub="Walked off the Max Dupri gimmick on the September 30, 2022 SmackDown and "
                     "took his name back - cited ever since as the modern precedent for trusting "
                     "a wrestler's own act."),
        ],
        footnote=("Deliberately absent: a career win-loss total, because no verified figure "
                  "exists; Observer ratings, because none could be verified for any Knight match; "
                  "and day-precision dates for the TNA/Impact and independent matches, which were "
                  "not verified in this pass. His billed home is Los Angeles; his actual origin "
                  "is Hagerstown, Maryland, and this page carries both."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography",
             href="https://en.wikipedia.org/wiki/LA_Knight"),
        dict(k="Sports Illustrated", v="2026 status — the return and the Usos storyline",
             href="https://www.si.com/fannation/wrestling/wwe/the-latest-update-on-la-knight-wwe-status"),
        dict(k="CBS Sports", v="Raw, August 24, 2026 — the OTM ambush",
             href="https://www.cbssports.com/wwe/news/wwe-raw-live-updates-results-review-grades-august-24-oba-femi-bron-breakker/live/"),
        dict(k="SmackDown Hotel", v="Profile — vitals, moves, title history",
             href="https://www.thesmackdownhotel.com/wrestlers/la-knight"),
        dict(k="SmackDown Hotel", v="SummerSlam 2026 full results",
             href="https://www.thesmackdownhotel.com/events-results/ppv-special/wwe-summerslam-2026"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="What is LA Knight doing in the 2026 Bloodline storyline?",
            a="He is the resistance. From his May 19, 2026 return onward he told The Usos on "
              "television that their arrangement with Roman Reigns&rsquo; reformed Bloodline was "
              "a rerun of the story they once escaped. At SummerSlam on August 1 he, Solo Sikoa "
              "and Royce Keys beat the Bloodline&rsquo;s Jacob Fatu and The Usos; on the August "
              "17 Raw, Solo &mdash; mid-&ldquo;delivery&rdquo; to Reigns &mdash; spiked the "
              "Tribal Chief and formally stood with Knight. Then on August 24, Keys and his "
              "debuting OTM faction attacked Knight, Solo and The Usos alike. As of August 31, "
              "2026 he is fighting the Bloodline and OTM at once, with Solo as his one ally.",
            q_ld="What is LA Knight's role in the 2026 Bloodline storyline?",
            a_ld="LA Knight leads the opposition to Roman Reigns' reformed Bloodline on Raw. After "
                 "returning on May 19, 2026, he spent the summer warning The Usos that their "
                 "alliance with Reigns repeated the original Bloodline story. At SummerSlam on "
                 "August 1, 2026, Knight, Solo Sikoa and Royce Keys defeated the Bloodline's "
                 "Jacob Fatu, Jey Uso and Jimmy Uso. On the August 17 Raw, Solo Sikoa attacked "
                 "Reigns and aligned with Knight. On August 24, the debuting faction of Royce "
                 "Keys and OTM attacked Knight, Sikoa and The Usos, ending their match in a "
                 "no-contest."),
        dict(
            q="Was LA Knight ever a world champion?",
            a="Yes &mdash; outside WWE. As <b>Eli Drake</b> he won the Impact World Championship "
              "in the Gauntlet for the Gold in August 2017 and carried TNA/Impact&rsquo;s top "
              "title into early 2018. In WWE his championships are the United States title, twice "
              "&mdash; 119 days from SummerSlam 2024 and 43 days in 2025 &mdash; and the Million "
              "Dollar Championship from NXT in 2021. He has challenged for WWE world titles "
              "&mdash; Roman Reigns at Crown Jewel 2023 and in the 2024 Royal Rumble four-way, "
              "Seth Rollins in the Clash in Paris four-way &mdash; without winning one, so far.",
            q_ld="Has LA Knight ever been a world champion?",
            a_ld="LA Knight was a world champion outside WWE: as Eli Drake he won the Impact "
                 "World Championship in August 2017 and held it into early 2018. In WWE he is a "
                 "two-time United States Champion, with reigns of 119 days (won from Logan Paul "
                 "at SummerSlam on August 3, 2024) and 43 days (2025), and held the Million "
                 "Dollar Championship in NXT in 2021. He has challenged for WWE's world "
                 "championships against Roman Reigns and Seth Rollins but has not yet won one."),
        dict(
            q="Is LA Knight really an overnight success who came from nowhere at 40?",
            a="No &mdash; the age is right and the &ldquo;nowhere&rdquo; is wrong. His first "
              "match was in <b>2003</b>. He worked WWE developmental as Slate Randall in "
              "2013&ndash;14, was a world champion in Impact as Eli Drake in 2017, and briefly "
              "fronted the NWA before returning to WWE in 2021. What happened in 2023 was not a "
              "debut but an adoption: the crowd took up the YEAH! call-and-response faster than "
              "the booking did, and WWE caught up. Twenty years of reps, one year of "
              "discovery.",
            q_ld="Is LA Knight an overnight success who came from nowhere?",
            a_ld="No. LA Knight, real name Shaun Ricker, had his first professional match in 2003, "
                 "worked in WWE developmental as Slate Randall in 2013-14, won the Impact World "
                 "Championship as Eli Drake in 2017, and appeared in the NWA before returning to "
                 "WWE in 2021. His 2023 breakout at age 40, driven by the crowd's adoption of his "
                 "YEAH! catchphrase, came twenty years into his career."),
        dict(
            q="Why was LA Knight called Max Dupri, and what happened to that gimmick?",
            a="WWE repackaged him in May 2022 as Max Dupri, the non-wrestling head of a "
              "modelling agency called Maximum Male Models. He lasted four months: on the "
              "September 30, 2022 SmackDown he walked off the act, took the LA Knight name back, "
              "and returned to wrestling. Within a year the YEAH! breakout made him one of the "
              "most popular performers in the company, and the episode is now the standard "
              "argument for letting wrestlers keep the act that already works.",
            q_ld="Why was LA Knight renamed Max Dupri in WWE?",
            a_ld="WWE repackaged LA Knight as Max Dupri in May 2022, a non-wrestling talent-agent "
                 "character who led the Maximum Male Models faction on SmackDown. He abandoned "
                 "the gimmick on the September 30, 2022 episode of SmackDown, resumed wrestling "
                 "under the LA Knight name, and broke out as one of WWE's most popular "
                 "performers in 2023."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Shaun Edward Ricker"),
        dict(label="Born", value="November 1, 1982", sub="Hagerstown, Maryland &middot; age 43"),
        dict(label="Billed from", value="Los Angeles, California"),
        dict(label="Height", value="6&#8242;1&#8243;", sub="185 cm"),
        dict(label="Weight", value="234 lb", sub="106 kg (billed)"),
        dict(label="Debut", value="2003", sub="Heartland Wrestling Association, as Deuce; "
                                              "training began March 17, 2003"),
        dict(label="Ring names",
             value="Deuce &rarr; Slate Randall &rarr; Eli Drake &rarr; Max Dupri &rarr; LA Knight",
             sub="2003&ndash;05 &middot; 2013&ndash;14 &middot; 2014&ndash;21 &middot; 2022 "
                 "&middot; 2021, 2022&ndash;present"),
        dict(label="Signature", value="BFT (Blunt Force Trauma) &middot; jumping neckbreaker "
                                      "&middot; the pointed finger"),
        dict(label="Catchphrase", value="YEAH! &middot; Let me talk to ya &middot; L-A-Knight"),
        dict(label="Brand", value="Raw"),
        dict(label="Also known as", value="The Megastar &middot; The Defiant One"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1982-11-01",
    bornplace="Hagerstown, Maryland",
    nationality="United States",
    height_cm=185,
    weight_kg=106,
    ld=dict(
        alternateName=["Shaun Edward Ricker", "Shaun Ricker", "Eli Drake", "Max Dupri",
                       "Slate Randall", "The Megastar"],
        award=["WWE United States Championship (2 reigns)",
               "Impact World Championship (1 reign, as Eli Drake)",
               "Million Dollar Championship (1 reign)",
               "TNA King of the Mountain Championship (1 reign)",
               "Impact World Tag Team Championship (1 reign, with Scott Steiner)",
               "Slim Jim Battle Royal winner, SummerSlam 2023"],
        knowsAbout=["Professional wrestling", "WWE", "Impact Wrestling", "TNA", "NXT",
                    "Championship wrestling", "The Bloodline"],
        description="LA Knight, born Shaun Edward Ricker in Hagerstown, Maryland, is an American "
                    "professional wrestler signed to WWE. A former Impact World Champion under "
                    "the name Eli Drake, he broke out in WWE in 2023 at age 40 behind his YEAH! "
                    "catchphrase, won the United States Championship twice - taking the title "
                    "from Logan Paul at SummerSlam 2024 - and in 2026 leads the on-screen "
                    "resistance to Roman Reigns' reformed Bloodline alongside Solo Sikoa.",
        sameAs=["https://en.wikipedia.org/wiki/LA_Knight",
                "https://www.wwe.com/superstars/la-knight"],
    ),
)
