# -*- coding: utf-8 -*-
"""Kazuchika Okada - dossier data.

Sources: web research compiled August 31, 2026, the day after Okada won the AEW
International Championship in a three-way at All In: London. NJPW reign dates from
Wikipedia's IWGP championship articles; AEW dates from AEW.com's own International
Championship history page and event coverage (Wrestling Inc, POST Wrestling, Fightful).
Nothing is invented.

Deliberate omissions:
  * No career win-loss total - none verified.
  * No social links - handles not verified in this pass.
  * The end of his second IWGP World Heavyweight reign (to Sanada, Sakura Genesis 2023)
    is printed at month precision: consulted sources gave both April 8 and April 9, 2023,
    and the conflict is noted rather than resolved.
  * No theme entry - no Spotify URL was verified.
"""

# ----------------------------------------------------------------- record rows
# Sixteen documented bouts spanning the Rainmaker era in two companies. A curated
# ledger, not a career count.
ROWS = [
    dict(result="W", date="2012-02-12", promo="NJPW", landmark=True,
         event="The New Beginning — Osaka", opponent="Hiroshi Tanahashi",
         stip="Singles — the Rainmaker Shock: champion at 24, one month after returning "
              "from excursion",
         title="IWGP Heavyweight Championship"),
    dict(result="L", date="2013-01-04", promo="NJPW",
         event="Wrestle Kingdom 7", opponent="Hiroshi Tanahashi",
         stip="Singles — challenge; the trilogy-of-eras rivalry hits the Dome",
         title="IWGP Heavyweight Championship"),
    dict(result="W", date="2013-04-07", promo="NJPW",
         event="Invasion Attack", opponent="Hiroshi Tanahashi",
         stip="Singles — second reign begins", title="IWGP Heavyweight Championship"),
    dict(result="W", date="2016-06-19", promo="NJPW", landmark=True,
         event="Dominion", opponent="Tetsuya Naito",
         stip="Singles — the record 720-day fourth reign begins",
         title="IWGP Heavyweight Championship"),
    dict(result="W", date="2017-01-04", promo="NJPW", landmark=True,
         event="Wrestle Kingdom 11", opponent="Kenny Omega", opponent_html=True,
         stip="Singles — 6 stars (Meltzer), the scale breaks", title="IWGP Heavyweight Championship"),
    dict(result="D", date="2017-06-11", promo="NJPW",
         event="Dominion", opponent="Kenny Omega", opponent_html=True,
         stip="60-minute time-limit draw — 6.25 stars", title="IWGP Heavyweight Championship"),
    dict(result="L", date="2018-06-09", promo="NJPW", landmark=True,
         event="Dominion", opponent="Kenny Omega", opponent_html=True,
         stip="Two of three falls, no time limit — the 720-day reign ends at V12; "
              "Meltzer's first 7-star match",
         title="IWGP Heavyweight Championship"),
    dict(result="W", date="2019-04-06", promo="NJPW",
         event="G1 Supercard — Madison Square Garden", opponent="Jay White",
         stip="Singles — fifth reign begins", title="IWGP Heavyweight Championship"),
    dict(result="L", date="2020-01-05", promo="NJPW",
         event="Wrestle Kingdom 14 Night 2", opponent="Tetsuya Naito",
         stip="Double gold dash — Naito takes both belts", title="IWGP Heavyweight Championship"),
    dict(result="W", date="2022-01-04", promo="NJPW", landmark=True,
         event="Wrestle Kingdom 16 Night 1", opponent="Shingo Takagi",
         stip="Singles — first IWGP World Heavyweight reign",
         title="IWGP World Heavyweight Championship"),
    dict(result="W", date="2023-01-04", promo="NJPW",
         event="Wrestle Kingdom 17", opponent="Jay White",
         stip="Singles — becomes a seven-time IWGP champion",
         title="IWGP World Heavyweight Championship"),
    dict(result="W", date="2024-03-20", promo="AEW", landmark=True,
         event="Dynamite", opponent="Eddie Kingston",
         stip="Singles — two weeks after signing; the 648-day reign begins",
         title="AEW Continental Championship"),
    dict(result="W", date="2024-12-28", promo="AEW",
         event="Worlds End", opponent="Will Ospreay", opponent_html=True,
         stip="Continental Classic final — wins the tournament as reigning champion", title=""),
    dict(result="W", date="2025-07-12", promo="AEW", landmark=True,
         event="All In: Texas", opponent="Kenny Omega", opponent_html=True,
         stip="Winner-takes-all — becomes the first AEW Unified Champion",
         title="AEW International Championship"),
    dict(result="L", date="2025-12-27", promo="AEW", landmark=True,
         event="Worlds End", opponent="Jon Moxley", opponent_html=True,
         stip="Continental Classic final — the 648-day Continental reign ends",
         title="AEW Continental Championship"),
    dict(result="L", date="2026-05-24", promo="AEW",
         event="Double or Nothing", opponent="Konosuke Takeshita",
         stip="Singles — the 316-day International reign ends",
         title="AEW International Championship"),
    dict(result="W", date="2026-08-30", promo="AEW", landmark=True, type="tag",
         event="All In: London — Wembley", opponent="Kyle Fletcher & Konosuke Takeshita",
         stip="Three-way — Rainmaker on Fletcher; second reign begins",
         title="AEW International Championship"),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Kenny Omega": "kenny-omega", "Will Ospreay": "will-ospreay",
                 "Jon Moxley": "jon-moxley"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="kazuchika-okada",
    name="Kazuchika Okada",
    realname="Kazuchika Okada",
    epithet="The Rainmaker",
    hook="Record & Titles",

    meta_desc=("Kazuchika Okada, the Rainmaker, is a seven-time IWGP champion and the current AEW "
               "International Champion, won at All In: London on August 30, 2026. Full record, "
               "titles, factions, records and career."),
    og_desc=("The Rainmaker: seven IWGP title reigns including a record 720 days, four G1 Climax "
             "wins, the first AEW Unified Championship, and the International title regained at "
             "Wembley."),
    tw_desc="The Rainmaker: 7 IWGP reigns, 4 G1s, and AEW International Champion again at Wembley.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2004",
    height_imp="6&#8242;3&#8243;",
    weight_lb="236",
    world_titles="7",
    vitals_tagline="Make it rain",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="KZ", title="AEW Shop", sub="Official tees · Shop AEW",
             tag="Shop", href="https://shop.aew.com/"),
        dict(ic="AEW", title="AEW Roster Profile", sub="AllEliteWrestling.com", tag="Visit",
             href="https://www.allelitewrestling.com/aew-roster"),
        dict(ic="NJ", title="NJPW", sub="The house the Rainmaker built · NJPW1972.com",
             tag="Visit", href="https://www.njpw1972.com/"),
        dict(ic="W", title="Wikipedia", sub="Full biography", tag="Read", charity=True,
             href="https://en.wikipedia.org/wiki/Kazuchika_Okada"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Rainmaker &middot; formerly of CHAOS &middot; ex-Toryumon",
    hero_tag="Anjo, Aichi, Japan &middot; <em>Toryumon &middot; NJPW &middot; AEW &middot; "
             "2004&ndash;present</em>",
    now_label="NOW",
    now_bold="AEW International Champion — second reign",
    now_tail=" &middot; won the three-way over champion Kyle Fletcher and Konosuke Takeshita at "
             "All In: London, August 30, 2026",
    hstats=[
        dict(value="720", x=False, label="Day IWGP Reign"),
        dict(value="7",   x=True,  label="IWGP Title Reigns"),
        dict(value="4",   x=True,  label="G1 Climax Wins"),
        dict(value="648", x=False, label="Day Continental Reign"),
    ],
    ghost_link="From Toryumon Mexico at sixteen to the Rainmaker",
    vlabel="Est. 2004 &middot; Anjo, Aichi, Japan",
    mono="KZ",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Kazuchika Okada</b> is the AEW International Champion again, as of August 30, 2026 "
        "&mdash; he pinned Kyle Fletcher with a Rainmaker in a three-way that also included "
        "Konosuke Takeshita at All In: London, reclaiming the title Takeshita had taken from him at "
        "Double or Nothing in May. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">720</span>'
        '<span class="pull-cap">days as IWGP Heavyweight Champion, 2016&ndash;18 &mdash; the longest reign in the title&rsquo;s history</span></span>'
        "That is the current chapter of a career that was already, by most sober accountings, the "
        "best of its generation before he left Japan: the man who main-evented the Tokyo Dome year "
        "after year, held the IWGP Heavyweight Championship for a record 720 days, and won the G1 "
        "Climax four times.",

        "Get the count right, because almost nobody does: &ldquo;seven-time IWGP champion&rdquo; "
        "collapses two different titles into one. Okada held the <b>IWGP Heavyweight "
        "Championship</b> &mdash; the historic belt &mdash; <b>five times</b> between 2012 and "
        "2020, and the <b>IWGP World Heavyweight Championship</b> &mdash; the successor created in "
        "2021 &mdash; <b>twice</b>, winning it from Shingo Takagi at Wrestle Kingdom 16 on January "
        "4, 2022 and from Jay White at Wrestle Kingdom 17 exactly a year later. Across those seven "
        "reigns he made 36 successful defenses, the most of any champion, per Wikipedia&rsquo;s "
        "title history; the fourth reign alone ran 720 days with a record twelve defenses, both "
        "still unmatched. One date is left loose on this page deliberately: sources consulted give "
        "both April 8 and April 9, 2023 for the Sanada loss that ended the seventh reign, so it is "
        "printed here at month precision only.",

        "The AEW chapter has been a title-machine of its own. He signed in March 2024, joined the "
        "Elite, and beat Eddie Kingston for the Continental Championship on the March 20, 2024 "
        "Dynamite &mdash; two weeks in. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">648</span>'
        '<span class="pull-cap">days as AEW Continental Champion &mdash; a reign that swallowed a whole second title on its way</span></span>'
        "He held that belt <b>648 days</b> (as Fightful counted it), winning the 2024 Continental "
        "Classic as reigning champion along the way &mdash; beating Will Ospreay in the Worlds End "
        "final on December 28, 2024 &mdash; and then, at All In: Texas on July 12, 2025, beat Kenny "
        "Omega in a winner-takes-all match to add the International Championship and become the "
        "first <b>AEW Unified Champion</b>. The run finally cracked at Worlds End on December 27, "
        "2025, when Jon Moxley beat him in the Continental Classic final to take the Continental "
        "half; Takeshita took the International half at Double or Nothing on May 24, 2026 after 316 "
        "days. Wembley put one of the two belts back on him.",

        "He is 38, he wrestles a fraction of his old NJPW schedule, and the Rainmaker apparatus "
        "&mdash; the money-raining entrance, the too-cool deliberateness, the single lariat that "
        "ends everything &mdash; has survived translation to American television intact. The "
        "trainer&rsquo;s stamp explains the oddity of his origin: he is a Toryumon product, trained "
        "by Ultimo Dragon, who debuted in <b>Mexico</b> on August 29, 2004 at sixteen before ever "
        "wrestling in Japan, and did a largely wasted TNA excursion before the January 2012 "
        "homecoming that changed New Japan&rsquo;s history.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["AEW", "NJPW"],
        promo_labels={"AEW": "AEW", "NJPW": "NJPW"},
        stats=[
            ("720",  "Day IWGP reign"),
            ("36",   "IWGP defenses, total"),
            ("7&times;", "IWGP champion"),
            ("4&times;", "G1 Climax winner"),
            ("648",  "Day Continental reign"),
            ("2&times;", "AEW International"),
        ],
        lead=("Sixteen documented bouts &mdash; the five Heavyweight reigns' hinges, the Omega "
              "series, both Wrestle Kingdom World title wins and the entire AEW title arc. This is "
              "a curated ledger, not a career count, and no win&ndash;loss total is published "
              "because none could be verified. The Sanada loss that ended the last IWGP reign is "
              "absent because its exact date conflicts across sources. Filter by match type, tap "
              "any column header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The Omega series is the spine of the modern star-ratings era, and Okada was "
                    "in every match of it. Ratings are Dave Meltzer's, as widely published — "
                    "reported rather than re-audited."),
    signature=[
        dict(rating="7.0", event="Dominion 2018 — Osaka-jo Hall", opponent="Kenny Omega",
             stip="IWGP Heavyweight Championship, 2/3 falls — the reign ends at 720 days and V12"),
        dict(rating="6.25", event="Dominion 2017", opponent="Kenny Omega",
             stip="IWGP Heavyweight Championship — 60-minute time-limit draw"),
        dict(rating="6.0", event="Wrestle Kingdom 11", opponent="Kenny Omega",
             stip="IWGP Heavyweight Championship — the first time the 5-star scale broke"),
    ],
    signature_count_word="three",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("5&times;", "IWGP Heavyweight"),
            ("2&times;", "IWGP World Heavyweight"),
            ("1st",  "AEW Unified Champion"),
            ("2&times;", "AEW International"),
        ],
        lead=("Seven IWGP reigns across two titles, and an AEW run that has already produced a "
              "648-day reign and the company's first unified championship. Early Toryumon-era "
              "credentials were not verified in this pass and are not listed."),
        rows=[
            dict(ic="H", name="IWGP Heavyweight Championship", count="5",
                 sub="2012 (The New Beginning, def. Tanahashi) &middot; 2013&ndash;14 &middot; "
                     "2015&ndash;16 &middot; 2016&ndash;18 &mdash; <b>720 days</b> and a record 12 "
                     "defenses, ended by Kenny Omega at Dominion &middot; 2019&ndash;20, ended by "
                     "Naito in the Wrestle Kingdom 14 double gold dash &middot; 36 total defenses, "
                     "the most of any champion per Wikipedia"),
            dict(ic="W", name="IWGP World Heavyweight Championship", count="2",
                 sub="January 4, 2022 &ndash; June 12, 2022 (def. Shingo Takagi at Wrestle Kingdom "
                     "16, lost to Jay White at Dominion) &middot; January 4, 2023 &ndash; April "
                     "2023 (def. Jay White at Wrestle Kingdom 17, lost to Sanada at Sakura Genesis "
                     "&mdash; exact date conflicts across sources)"),
            dict(ic="C", name="AEW Continental Championship", count="1",
                 sub="March 20, 2024 &ndash; December 27, 2025 &middot; def. Eddie Kingston on "
                     "Dynamite, lost to Jon Moxley in the Continental Classic final at Worlds End "
                     "&middot; <b>648 days</b> &middot; won the 2024 Continental Classic as "
                     "champion mid-reign"),
            dict(ic="I", name="AEW International Championship", count="2",
                 sub="July 12, 2025 &ndash; May 24, 2026 &middot; def. Kenny Omega at All In: Texas "
                     "to become the first AEW Unified Champion, lost to Konosuke Takeshita at "
                     "Double or Nothing after 316 days &middot; August 30, 2026 &ndash; present "
                     "&middot; def. Kyle Fletcher and Takeshita in a three-way at All In: London"),
            dict(ic="G", name="G1 Climax", count="4",
                 sub="2012, 2014, 2021, 2022 &mdash; second only to Masahiro Chono&rsquo;s five "
                     "wins, per Wikipedia"),
            dict(ic="N", name="New Japan Cup", count="2",
                 sub="2013 and 2019"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="One faction for twelve years, then a heel turn into the company he now works for.",
        cards=[
            dict(era="NJPW &middot; 2012&ndash;2024",
                 name="CHAOS",
                 members="Okada, Shinsuke Nakamura (founder era), Tomohiro Ishii, Hirooki Goto, "
                         "YOSHI-HASHI, Will Ospreay (2016&ndash;2020), others",
                 desc="He joined CHAOS on the night of his 2012 return and eventually led it. The "
                      "unit softened from Nakamura's villain gang into the establishment stable of "
                      "the 2010s — which is roughly what happened to Okada himself, from Rainmaker "
                      "shock heel to the company's ace. Will Ospreay was his CHAOS protege until "
                      "the 2020 betrayal that founded United Empire."),
            dict(era="AEW &middot; 2024&ndash;present",
                 name="The Elite",
                 members="Okada, The Young Bucks, at times Kenny Omega and Jack Perry",
                 desc="He debuted as a signed AEW talent on March 6, 2024 by joining the Young "
                      "Bucks' heel incarnation of The Elite — a deliberate inversion: the NJPW ace "
                      "arriving as an American company's smirking villain. The alignment has "
                      "shifted around him since the Bucks reconciled with Omega in late 2025; his "
                      "2026 business — Takeshita, Fletcher and the Don Callis Family's belts — has "
                      "been his own."),
            dict(era="Character &middot; 2012&ndash;present",
                 name="The Rainmaker",
                 members="Okada, and a shower of fake banknotes",
                 desc="Less a gimmick than a thesis: unhurried excellence, presented with money "
                      "raining from the ceiling. The pose, the wrist-clutch lariat and the "
                      "dropkick — routinely called the best in wrestling — survived the move west "
                      "without alteration, which was the point. Toryumon trained him; New Japan "
                      "made him; the character needed no translation."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Four phases, one name &mdash; his real one. <b>Toryumon trainee</b> (2004&ndash;2007) "
             "&rarr; <b>Young lion and TNA excursion</b> (2007&ndash;2012) &rarr; <b>The "
             "Rainmaker</b> (2012&ndash;2024) &rarr; <b>AEW&rsquo;s Rainmaker</b> "
             "(2024&ndash;present).",
        cards=[
            dict(mono="TM", era="Mexico &amp; Japan &middot; 2004&ndash;2007", name="Toryumon trainee",
                 desc="Trained by Ultimo Dragon and debuted in Mexico on August 29, 2004, at "
                      "sixteen — a lucha-school origin that almost nothing in the finished product "
                      "advertises."),
            dict(mono="YL", era="NJPW &amp; TNA &middot; 2007&ndash;2012", name="The excursion years",
                 desc="Joined New Japan in 2007, then spent an unglamorous American excursion in "
                      "TNA, used as an afterthought. The gap between that run and what followed is "
                      "part of the legend."),
            dict(mono="RM", era="NJPW &middot; 2012&ndash;2024", name="The Rainmaker",
                 desc="Returned in January 2012, challenged Tanahashi immediately, and won the IWGP "
                      "Heavyweight Championship at 24 on February 12, 2012 — the Rainmaker Shock. "
                      "Twelve years as the axis of New Japan followed: five Heavyweight reigns, "
                      "two World Heavyweight reigns, four G1s, and the Omega series."),
            dict(mono="AE", era="AEW &middot; 2024&ndash;present", name="AEW's Rainmaker",
                 desc="Left NJPW after The New Beginning in Sapporo in February 2024, signed with "
                      "AEW in March, and has spent the run since as a champion almost "
                      "continuously: 648 days with the Continental belt, the first Unified "
                      "Championship, and now a second International reign won at Wembley."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Mexico at sixteen to Wembley at 38.",
        rows=[
            dict(year="2004", title="Debut in Mexico",
                 desc="August 29, 2004, for Ultimo Dragon's Toryumon at sixteen."),
            dict(year="2012", title="The Rainmaker Shock",
                 desc="Returns from excursion in January, beats Hiroshi Tanahashi for the IWGP "
                      "Heavyweight Championship at The New Beginning on February 12 at age 24, and "
                      "wins his first G1 Climax that summer."),
            dict(year="2016", title="The 720-day reign begins",
                 desc="Beats Tetsuya Naito at Dominion on June 19. The fourth reign runs to June 9, "
                      "2018 with a record twelve defenses."),
            dict(year="2017", title="The Omega series breaks the scale",
                 desc="6 stars at Wrestle Kingdom 11 on January 4, a 6.25-star hour-long draw at "
                      "Dominion on June 11 — the ratings era's ground zero."),
            dict(year="2018", title="The reign ends at 7 stars",
                 desc="Omega wins the two-of-three-falls Dominion main event on June 9 — the first "
                      "7-star match Dave Meltzer ever awarded."),
            dict(year="2019", title="Fifth reign, from Madison Square Garden",
                 desc="Beats Jay White at G1 Supercard on April 6; holds the title until Naito "
                      "takes both belts at Wrestle Kingdom 14 on January 5, 2020."),
            dict(year="2022", title="IWGP World Heavyweight Champion",
                 desc="Beats Shingo Takagi at Wrestle Kingdom 16 on January 4; wins back-to-back "
                      "G1s in 2021 and 2022; regains the title from Jay White at Wrestle Kingdom "
                      "17 on January 4, 2023 — a seven-time IWGP champion."),
            dict(year="2024", title="Leaves Japan, wins gold in two weeks",
                 desc="Final NJPW match at The New Beginning in Sapporo in February; signs with "
                      "AEW in March, joins The Elite, and beats Eddie Kingston for the Continental "
                      "Championship on the March 20 Dynamite."),
            dict(year="2025", title="First AEW Unified Champion",
                 desc="Beats Kenny Omega winner-takes-all at All In: Texas on July 12 to hold the "
                      "Continental and International titles at once; Jon Moxley ends the 648-day "
                      "Continental reign in the Continental Classic final at Worlds End on "
                      "December 27."),
            dict(year="2026", title="Loses and regains the International title",
                 desc="Konosuke Takeshita beats him at Double or Nothing on May 24 after 316 days; "
                      "Okada reclaims the belt in the All In: London three-way over champion Kyle "
                      "Fletcher and Takeshita on August 30, pinning Fletcher with the Rainmaker."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Kenny Omega", slug="kenny-omega",
                 desc="The series that redefined what match ratings could say: 6 stars at Wrestle "
                      "Kingdom 11, the 6.25-star hour draw at Dominion 2017, and the 7-star "
                      "Dominion 2018 loss that ended the 720-day reign. Okada took the AEW-era "
                      "rubber match, beating Omega winner-takes-all at All In: Texas on July 12, "
                      "2025 to become the first Unified Champion."),
            dict(name="Hiroshi Tanahashi",
                 desc="The generational handover, conducted over years of Tokyo Dome main events. "
                      "Okada announced himself by beating Tanahashi in 2012 at 24, lost the Wrestle "
                      "Kingdom 7 challenge, and won the belt back from him at Invasion Attack 2013 "
                      "— the rivalry that made the Rainmaker the ace."),
            dict(name="Tetsuya Naito",
                 desc="Traded eras with him twice: Okada took the title from Naito to start the "
                      "720-day reign at Dominion 2016, and Naito took both belts from Okada in the "
                      "Wrestle Kingdom 14 double gold dash on January 5, 2020."),
            dict(name="Will Ospreay", slug="will-ospreay",
                 desc="Protege turned rival — Ospreay left CHAOS by turning on him in 2020. Okada "
                      "has kept the receipts since: the G1 Climax 32 final in 2022, and the "
                      "Continental Classic final at Worlds End on December 28, 2024, both Okada "
                      "wins."),
            dict(name="Jon Moxley", slug="jon-moxley",
                 desc="The man who finally cracked the AEW reign: Moxley beat him in the 2025 "
                      "Continental Classic final at Worlds End on December 27, 2025, ending 648 "
                      "days and splitting the Unified Championship back into halves."),
            dict(name="The Don Callis Family",
                 desc="The 2026 program: Takeshita took the International title from him at Double "
                      "or Nothing, Kyle Fletcher took it from Takeshita with Callis interference "
                      "in July, and Okada beat them both in one match at Wembley to end the "
                      "family's hold on the belt."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Presentation",
        lead="Thin by design &mdash; the verified list is short, and nothing is added to pad it.",
        rows=[
            dict(when="2012&ndash;", title="The money-rain entrance", kind="Presentation",
                 desc="The signature visual — banknotes falling from the rafters — has traveled "
                      "with him from Tokyo Dome main events to AEW pay-per-views unchanged."),
            dict(when="2012&ndash;2024", title="Tokyo Dome main events", kind="Legacy",
                 desc="Wikipedia credits him with nine Wrestle Kingdom headline appearances — the "
                      "most of his era — including the January 4-and-5 double-show years."),
            dict(when="2024&ndash;", title="AEW television", kind="TV",
                 desc="A weekly television character in English for the first time; the act works "
                      "mostly without dialogue, by design. No film roles, autobiography or "
                      "documentary series could be verified, so none are listed."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated the way the sources actually state them — including the "
             "two-titles-in-one-count problem that follows him everywhere.",
        stats=[
            ("720", "Day IWGP reign"),
            ("12",  "Defenses in one reign"),
            ("4",   "G1 Climax wins"),
        ],
        rows=[
            dict(name="720 consecutive days as IWGP Heavyweight Champion",
                 sub="June 19, 2016 to June 9, 2018 — the longest reign in the title's history, "
                     "with a record twelve successful defenses. Both records still stand."),
            dict(name="Seven IWGP title reigns — but across two belts",
                 sub="Five IWGP Heavyweight Championship reigns (2012-2020) plus two IWGP World "
                     "Heavyweight Championship reigns (2022, 2023). The compressed 'seven-time "
                     "champion' phrasing is accurate only if you name both titles."),
            dict(name="36 successful IWGP title defenses in total",
                 sub="The most of any champion across the title's history, per Wikipedia's "
                     "championship article."),
            dict(name="Four G1 Climax wins: 2012, 2014, 2021, 2022",
                 sub="Second all-time behind Masahiro Chono's five. The 2012 win came months into "
                     "the Rainmaker run; the 2021-22 pair came back to back."),
            dict(name="First AEW Unified Champion",
                 sub="Beat Kenny Omega winner-takes-all at All In: Texas on July 12, 2025, holding "
                     "the Continental and International Championships simultaneously until the "
                     "titles were split apart at Worlds End that December."),
            dict(name="A 648-day AEW Continental Championship reign",
                 sub="March 20, 2024 to December 27, 2025, ended by Jon Moxley — the figure as "
                     "Fightful counted it. He also won the 2024 Continental Classic as reigning "
                     "champion, beating Will Ospreay in the final."),
            dict(name="Two-time AEW International Champion",
                 sub="July 12, 2025 to May 24, 2026 (316 days), and again from August 30, 2026 — "
                     "the Wembley three-way over Kyle Fletcher and Konosuke Takeshita, won with a "
                     "Rainmaker on Fletcher."),
            dict(name="Champion at 24, one month after returning from excursion",
                 sub="The Rainmaker Shock: February 12, 2012, beating Hiroshi Tanahashi at The New "
                     "Beginning in Osaka, in his first title challenge after coming home from TNA."),
        ],
        footnote=("Deliberately absent: a career win-loss total (none verified), social handles "
                  "(not verified), and a day-precision date for the 2023 Sanada loss, where "
                  "consulted sources conflict between April 8 and April 9. Meltzer ratings are "
                  "reported as published."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wrestling Inc", v="All In 2026 — Okada wins the three-way",
             href="https://www.wrestlinginc.com/2247122/aew-all-in-london-2026-kazuchika-okada-konosuke-takeshita-kyle-fletcher-wins-three-way-new-international-champ/"),
        dict(k="AEW", v="International Championship history",
             href="https://www.allelitewrestling.com/aew-international-championship-history"),
        dict(k="Wikipedia", v="Full biography",
             href="https://en.wikipedia.org/wiki/Kazuchika_Okada"),
        dict(k="Wikipedia", v="List of IWGP Heavyweight Champions",
             href="https://en.wikipedia.org/wiki/List_of_IWGP_Heavyweight_Champions"),
        dict(k="Fightful", v="Worlds End 2025 — Moxley ends the 648-day reign",
             href="https://www.fightful.com/wrestling/jon-moxley-wins-2025-continental-classic-tournament-captures-aew-continental-championship-at-worlds-end-ppv/"),
        dict(k="Fightful", v="All In: London 2026 full results",
             href="https://www.fightful.com/wrestling/aew-all-in-results-8-30-2026-kenny-omega-vs-will-ospreay-willow-nightingale-vs-mercedes-mone-more/"),
        dict(k="Wikipedia", v="IWGP World Heavyweight Championship",
             href="https://en.wikipedia.org/wiki/IWGP_World_Heavyweight_Championship"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Okada a champion right now?",
            a="Yes &mdash; he is the <b>AEW International Champion</b>, as of August 30, 2026. He "
              "won the title for a second time at All In: London, pinning defending champion Kyle "
              "Fletcher with a Rainmaker in a three-way that also included Konosuke Takeshita. His "
              "first International reign ran 316 days (July 12, 2025 to May 24, 2026) and began as "
              "the AEW Unified Championship.",
            q_ld="Is Kazuchika Okada currently a champion?",
            a_ld="Yes. Kazuchika Okada is the AEW International Champion as of August 30, 2026, "
                 "when he defeated defending champion Kyle Fletcher and Konosuke Takeshita in a "
                 "three-way match at AEW All In: London at Wembley Stadium, pinning Fletcher with "
                 "the Rainmaker. It is his second reign with the title."),
        dict(
            q="How many times has Okada been IWGP champion?",
            a="Seven &mdash; but across two different titles, which most retellings blur. He held "
              "the historic <b>IWGP Heavyweight Championship five times</b> between 2012 and 2020, "
              "including the record 720-day reign, and the successor <b>IWGP World Heavyweight "
              "Championship twice</b>, won at Wrestle Kingdom 16 (January 4, 2022, from Shingo "
              "Takagi) and Wrestle Kingdom 17 (January 4, 2023, from Jay White). Across all seven "
              "reigns he made 36 defenses, the most ever per Wikipedia.",
            q_ld="How many IWGP championship reigns has Kazuchika Okada had?",
            a_ld="Seven, across two titles. Kazuchika Okada held the IWGP Heavyweight Championship "
                 "five times between 2012 and 2020, including a record 720-day fourth reign, and "
                 "the IWGP World Heavyweight Championship twice, winning it at Wrestle Kingdom 16 "
                 "in January 2022 and Wrestle Kingdom 17 in January 2023. He made 36 successful "
                 "defenses across those reigns, the most of any champion."),
        dict(
            q="What was the AEW Unified Championship?",
            a="The combined Continental and International Championships, created when Okada &mdash; "
              "already Continental Champion for over a year &mdash; beat International Champion "
              "Kenny Omega in a winner-takes-all match at All In: Texas on July 12, 2025. He was "
              "the first and only Unified Champion: Jon Moxley took the Continental half by "
              "winning the Continental Classic final at Worlds End on December 27, 2025, and the "
              "belts have run separately since.",
            q_ld="What was the AEW Unified Championship and who held it?",
            a_ld="The AEW Unified Championship was the combination of the AEW Continental and "
                 "International Championships. Kazuchika Okada became the first Unified Champion "
                 "by defeating Kenny Omega in a winner-takes-all match at All In: Texas on July "
                 "12, 2025, while already reigning as Continental Champion. The titles split "
                 "again when Jon Moxley won the Continental Championship at Worlds End on "
                 "December 27, 2025."),
        dict(
            q="What is the Rainmaker Shock?",
            a="The February 12, 2012 title win that created the modern Okada. Back from a "
              "little-regarded TNA excursion just one month earlier, he challenged ace Hiroshi "
              "Tanahashi at The New Beginning in Osaka and won the IWGP Heavyweight Championship "
              "at 24 &mdash; a result so unexpected the Japanese press named it for him. Four "
              "more IWGP reigns, four G1 Climax wins and a decade of Tokyo Dome main events "
              "followed.",
            q_ld="What was the Rainmaker Shock?",
            a_ld="The Rainmaker Shock refers to February 12, 2012, when a 24-year-old Kazuchika "
                 "Okada, one month removed from an unheralded excursion to TNA, defeated Hiroshi "
                 "Tanahashi for the IWGP Heavyweight Championship at NJPW The New Beginning in "
                 "Osaka. The upset launched the Rainmaker persona and Okada's run as New Japan's "
                 "defining star of the 2010s."),
        dict(
            q="How long did Okada hold the AEW Continental Championship?",
            a="<b>648 days</b>, as Fightful counted it &mdash; from beating Eddie Kingston on the "
              "March 20, 2024 Dynamite, two weeks after signing, to losing the Continental "
              "Classic final to Jon Moxley at Worlds End on December 27, 2025. Mid-reign he also "
              "won the 2024 Continental Classic as the sitting champion, beating Will Ospreay in "
              "the final, and folded the International title in at All In: Texas.",
            q_ld="How long was Kazuchika Okada's AEW Continental Championship reign?",
            a_ld="Kazuchika Okada held the AEW Continental Championship for 648 days, from March "
                 "20, 2024, when he defeated Eddie Kingston on Dynamite, until December 27, 2025, "
                 "when Jon Moxley defeated him in the Continental Classic final at Worlds End. "
                 "During the reign he won the 2024 Continental Classic and unified the title with "
                 "the International Championship."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Kazuchika Okada", sub="Ring name and legal name match"),
        dict(label="Born", value="November 8, 1987", sub="Anjo, Aichi, Japan &middot; age 38"),
        dict(label="Billed from", value="Anjo, Aichi, Japan"),
        dict(label="Height", value="6&#8242;3&#8243;", sub="191 cm"),
        dict(label="Weight", value="236 lb", sub="107 kg (billed)"),
        dict(label="Debut", value="August 29, 2004", sub="Toryumon, in Mexico, at sixteen"),
        dict(label="Trained by", value="Ultimo Dragon", sub="Toryumon system"),
        dict(label="Signature", value="Rainmaker lariat &middot; the dropkick &middot; Money Clip "
                                      "&middot; tombstone piledriver",
             sub="The dropkick is routinely called the best in the business"),
        dict(label="Current title", value="AEW International Championship",
             sub="Second reign, won August 30, 2026 at All In: London"),
        dict(label="Faction history", value="CHAOS (2012&ndash;2024) &middot; The Elite "
                                            "(2024&ndash;)"),
        dict(label="Also known as", value="The Rainmaker"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1987-11-08",
    bornplace="Anjo, Aichi, Japan",
    nationality="Japan",
    height_cm=191,
    weight_kg=107,
    ld=dict(
        alternateName=["The Rainmaker", "Okada"],
        award=["IWGP Heavyweight Championship (5 reigns, record 720-day reign, record 12 defenses "
               "in one reign)",
               "IWGP World Heavyweight Championship (2 reigns)",
               "AEW Continental Championship (1 reign, 648 days)",
               "AEW International Championship (2 reigns, current)",
               "First AEW Unified Champion (2025)",
               "G1 Climax winner (2012, 2014, 2021, 2022)",
               "New Japan Cup winner (2013, 2019)",
               "Continental Classic winner (2024)"],
        knowsAbout=["Professional wrestling", "New Japan Pro-Wrestling", "All Elite Wrestling",
                    "CHAOS", "The Elite", "Toryumon", "Championship wrestling"],
        description="Kazuchika Okada, the Rainmaker, is a Japanese professional wrestler signed "
                    "to AEW. A seven-time IWGP champion across the Heavyweight and World "
                    "Heavyweight titles, he holds the records for the longest IWGP Heavyweight "
                    "reign at 720 days and most defenses. In AEW he held the Continental "
                    "Championship for 648 days, became the first Unified Champion, and won the "
                    "International Championship for a second time at All In: London on August 30, "
                    "2026.",
        sameAs=["https://en.wikipedia.org/wiki/Kazuchika_Okada",
                "https://www.allelitewrestling.com/aew-roster"],
    ),
)
