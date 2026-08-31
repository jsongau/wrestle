# -*- coding: utf-8 -*-
"""Finn Balor - dossier data.

Sources: web research compiled August 31, 2026 - Wikipedia's Finn Balor article, POST
Wrestling and Bleacher Report on WrestleMania 42, WrestleTalk and Sportskeeda on the
tag title changes, The Sportster's SummerSlam 2026 Night 2 report and TJR Wrestling's
August 28, 2026 SmackDown report. Every match row carries a day-precision date stated
in one of the opened sources. House style drops diacritics, so the name is rendered
Balor throughout.

Deliberate omissions:
  * No career win-loss total - no verified figure exists.
  * NJPW match rows: his IWGP Junior Heavyweight reigns and Best of the Super Juniors
    wins are listed in titles and feats, but no NJPW bout carried a day-precision date
    in the opened sources, so none appears in the record table.
  * The exact date he lost the United States Championship to Austin Theory in April
    2022 was not re-verified; the reign is described without it.
  * No social handles - official accounts were not verified in this pass.
"""

# ----------------------------------------------------------------- record rows
# WWE bouts only - see the omissions note for why NJPW is absent. The August 28, 2026
# triple threat is carried as a no-contest: Sami Zayn attacked everyone in it, referee
# included, and no winner was declared in the report used here.
ROWS = [
    dict(result="W", date="2015-07-04", promo="WWE", landmark=True,
         event="The Beast in the East — Tokyo", opponent="Kevin Owens",
         stip="Singles — wins the title in Sumo Hall", title="NXT Championship"),
    dict(result="L", date="2016-04-21", promo="WWE", landmark=True,
         event="NXT live event — Lowell, Massachusetts", opponent="Samoa Joe",
         stip="Singles — the 292-day reign ends off-television", title="NXT Championship"),
    dict(result="W", date="2016-08-21", promo="WWE", landmark=True,
         event="SummerSlam", opponent="Seth Rollins",
         stip="Singles — becomes the first Universal Champion, hurt mid-match",
         title="WWE Universal Championship"),
    dict(result="W", date="2019-02-17", promo="WWE",
         event="Elimination Chamber", opponent="Bobby Lashley & Lio Rush",
         stip="Two-on-one handicap — wins the title", title="WWE Intercontinental Championship"),
    dict(result="W", date="2019-04-07", promo="WWE", landmark=True,
         event="WrestleMania 35", opponent="Bobby Lashley",
         stip="Singles — as The Demon", title="WWE Intercontinental Championship"),
    dict(result="L", date="2019-07-14", promo="WWE",
         event="Extreme Rules", opponent="Shinsuke Nakamura",
         stip="Singles — the second IC reign ends", title="WWE Intercontinental Championship"),
    dict(result="W", date="2020-09-08", promo="WWE", landmark=True,
         event="NXT Super Tuesday II", opponent="Adam Cole",
         stip="Singles — second NXT Championship", title="NXT Championship"),
    dict(result="L", date="2021-04-08", promo="WWE",
         event="NXT TakeOver: Stand & Deliver", opponent="Karrion Kross",
         stip="Singles — the second reign ends", title="NXT Championship"),
    dict(result="W", date="2022-02-28", promo="WWE",
         event="Raw", opponent="Damian Priest",
         stip="Singles — Priest snaps and turns after", title="WWE United States Championship"),
    dict(result="L", date="2023-04-02", promo="WWE", landmark=True,
         event="WrestleMania 39 Night 2", opponent="Edge",
         stip="Hell in a Cell — The Demon's first WWE defeat", title=""),
    dict(result="L", date="2023-08-05", promo="WWE",
         event="SummerSlam — Detroit", opponent="Seth Rollins",
         stip="Singles — challenge", title="World Heavyweight Championship"),
    dict(result="W", date="2023-09-02", promo="WWE", type="tag", landmark=True,
         event="Payback", opponent="Kevin Owens & Sami Zayn",
         stip="Tag — with Damian Priest", title="Undisputed WWE Tag Team Championship"),
    dict(result="W", date="2024-06-24", promo="WWE", type="tag",
         event="Raw", opponent="Awesome Truth (The Miz & R-Truth)",
         stip="Tag — with JD McDonagh", title="World Tag Team Championship"),
    dict(result="L", date="2024-12-16", promo="WWE", type="tag",
         event="Raw", opponent="The War Raiders",
         stip="Tag — the 175-day reign ends", title="World Tag Team Championship"),
    dict(result="L", date="2025-04-20", promo="WWE", type="tag",
         event="WrestleMania 41 Night 2", opponent="Dominik Mysterio, Penta & Bron Breakker",
         stip="Fatal four-way — his own Coup de Grace hands Dominik the win",
         title="WWE Intercontinental Championship"),
    dict(result="W", date="2025-06-30", promo="WWE", type="tag",
         event="Raw", opponent="The New Day",
         stip="Tag — with JD McDonagh; second reign together", title="World Tag Team Championship"),
    dict(result="L", date="2025-10-20", promo="WWE", type="tag",
         event="Raw", opponent="AJ Styles & Dragon Lee",
         stip="Tag — a defense forced by Dominik Mysterio's complaints",
         title="World Tag Team Championship"),
    dict(result="L", date="2025-11-03", promo="WWE", type="tag",
         event="Raw", opponent="AJ Styles & Dragon Lee",
         stip="Tag — the rematch falls short", title="World Tag Team Championship"),
    dict(result="W", date="2026-04-19", promo="WWE", landmark=True,
         event="WrestleMania 42 Night 2", opponent="Dominik Mysterio",
         stip="Street fight — as The Demon; Coup de Grace through a table", title=""),
    dict(result="L", date="2026-08-02", promo="WWE", type="tag", landmark=True,
         event="SummerSlam Night 2 — Minneapolis", opponent="Kevin Owens, Gunther & Sami Zayn",
         stip="Fatal four-way for the No. 1 contendership — Owens returns and pins Zayn", title=""),
    dict(result="NC", date="2026-08-28", promo="WWE", type="tag",
         event="SmackDown", opponent="Kevin Owens & Gunther",
         stip="Triple threat for the No. 1 contendership — Sami Zayn destroys the match", title=""),
]

DATA = dict(
    slug="finn-balor",
    name="Finn Balor",
    realname="Fergal Devitt",
    epithet="The Prince",
    hook="Record & Titles",

    meta_desc=("Finn Balor, the Prince, founded the Bullet Club, became WWE's first Universal "
               "Champion, and revived The Demon to beat Dominik Mysterio at WrestleMania 42. Full "
               "record, titles, factions, records and career."),
    og_desc=("The Prince: Bullet Club founder, first Universal Champion, two NXT Championship "
             "reigns, ten WWE title reigns in all - and The Demon, back at WrestleMania 42."),
    tw_desc="The Prince: Bullet Club founder, first Universal Champion, The Demon at WrestleMania 42.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2001",
    height_imp="5&#8242;11&#8243;",
    weight_lb="190",
    world_titles="1",
    vitals_tagline="Everyone pays a price",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="FB", title="WWE Shop", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable across the modern 2K era",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="W", title="Wikipedia", sub="Full biography", tag="Read",
             href="https://en.wikipedia.org/wiki/Finn_B%C3%A1lor"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/finn-balor"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Prince &middot; The Demon &middot; formerly Prince Devitt",
    hero_tag="Bray, County Wicklow, Ireland &middot; <em>NJPW &middot; NXT &middot; WWE &middot; "
             "2001&ndash;present</em>",
    now_label="NOW",
    now_bold="SmackDown, no championship",
    now_tail=" &middot; had the August 28 No. 1 contender triple threat won until Sami Zayn pulled "
             "him off the pin and wrecked the match",
    hstats=[
        dict(value="292", x=False, label="Day NXT Title Reign"),
        dict(value="22",  x=False, label="Hour Universal Reign"),
        dict(value="10",  x=False, label="WWE Title Reigns"),
        dict(value="2",   x=True,  label="Best of the Super Juniors"),
    ],
    ghost_link="From founding the Bullet Club to reviving The Demon",
    vlabel="Est. 2001 &middot; Bray, Ireland",
    mono="FB",

    # ---------------------------------------------------------------- 01 overview
    # index into overview of the correction paragraph -> the framed
    # "Setting one thing straight" callout (aside.corr) on the page
    correction=1,
    overview=[
        "<b>Finn Balor</b> has founded or co-anchored three of the most consequential factions of "
        "the last quarter-century &mdash; and been thrown out of the most recent one, which is how "
        "he became a babyface again at 44. As Prince Devitt he founded New Japan's <b>Bullet "
        "Club</b> in May 2013; in WWE he became the inaugural Universal Champion at SummerSlam "
        "2016 and spent almost four years inside the Judgment Day before it expelled him in March "
        "2026. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">10</span>'
        '<span class="pull-cap">WWE championship reigns &mdash; one Universal, two NXT, two '
        'Intercontinental, one United States and four tag &mdash; plus three IWGP Junior Heavyweight '
        'reigns before any of them</span></span>'
        "The ledger runs ten WWE championship reigns: the Universal title, two NXT Championships "
        "&mdash; including a 292-day reign that was then the longest in the belt's history &mdash; "
        "two Intercontinental, one United States, two Undisputed WWE Tag Team reigns with Damian "
        "Priest and two World Tag Team reigns with JD McDonagh. And over all of it hangs The "
        "Demon, the paint-and-dread alter ego he has deployed perhaps a dozen times in a decade, "
        "most recently to put Dominik Mysterio through a table at WrestleMania 42.",

        "The line that follows him everywhere &mdash; &ldquo;he lost the Universal Championship "
        "the next night&rdquo; &mdash; is wrong in the way that matters. Balor <b>never lost</b> "
        "the Universal Championship. He beat Seth Rollins at SummerSlam on August 21, 2016 to "
        "become the title's first holder, tore the labrum in his right shoulder <i>during the "
        "match he won</i>, and <b>relinquished</b> the undefeated belt roughly 22 hours later, on "
        "the August 22 Raw. No one has ever beaten him for that championship. The injury cost him "
        "the better part of a year; the distinction &mdash; vacated, not dethroned &mdash; is the "
        "one his career-shortest reign statistic always drops.",

        "The middle years were the Judgment Day. He joined on June 6, 2022, helped expel Edge from "
        "the group Edge founded, took the tag titles twice with Damian Priest &mdash; then led the "
        "vote that expelled Priest in August 2024 &mdash; and twice more with JD McDonagh in 2024 "
        "and 2025. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">4</span>'
        '<span class="pull-cap">tag team championship reigns inside the Judgment Day &mdash; two with '
        'the man he later exiled, two with the man who watched him get exiled</span></span>'
        "The group ate him last. On the March 2, 2026 Raw he stopped McDonagh from handing Dominik "
        "Mysterio a hammer; Dominik lost the Intercontinental Championship to Penta, Balor told "
        "him his father might have been right about him, and the Judgment Day beat Balor down and "
        "threw him out &mdash; the same script it had run on Edge and on Priest, finally reaching "
        "its co-author. The answer came at WrestleMania 42 on April 19, 2026: The Demon, revived "
        "for a street fight added to the card that afternoon, and a Coup de Grace through a table "
        "to beat Dominik in ten minutes.",

        "Since June 2026 he has been a SmackDown wrestler &mdash; moved in a straight trade "
        "reported that month rather than a full draft &mdash; and the title chase is live. At "
        "SummerSlam on August 2 he was one of the four in the surprise No. 1 contender match that "
        "Kevin Owens returned to win, pinning Sami Zayn. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">8.28</span>'
        '<span class="pull-cap">the August SmackDown where Balor had the No. 1 contender triple threat '
        'won &mdash; until Sami Zayn pulled him out of the ring</span></span>'
        "On the August 28 SmackDown he hit the Coup de Grace on Gunther in the triple threat for "
        "the next shot at CM Punk's Undisputed WWE Championship and had the match won &mdash; "
        "until Zayn dragged him off the cover, flattened the referee, and beat down all four men "
        "with the title belt, champion included. As of August 31, 2026 Balor holds no "
        "championship, and the contendership he nearly earned twice in a month is still "
        "unresolved.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Curated ledger",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("292",  "Day NXT reign"),
            ("22",   "Hour Universal reign"),
            ("2&times;", "Intercontinental"),
            ("4&times;", "Tag team champion"),
            ("3&times;", "IWGP Junior Heavyweight"),
            ("2013", "Bullet Club founded"),
        ],
        lead=("Twenty-one documented WWE bouts &mdash; the title changes, the Demon appearances "
              "and the 2026 turn of fortune. This is a curated ledger, not a career count; no "
              "career win&ndash;loss total is published, and the NJPW years are covered in the "
              "titles and feats sections because no New Japan bout carried a day-precision date in "
              "the sources opened for this file. The August 28, 2026 triple threat is a no-contest "
              "&mdash; Sami Zayn attacked everyone in it. Filter by match type, tap any column "
              "header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The bouts the reputation rests on. No star ratings are printed because none "
                    "were verified against Observer archives in this pass &mdash; these are "
                    "selected for what they meant, not how they were scored."),
    signature=[
        dict(rating="&mdash;", event="The Beast in the East 2015 — Tokyo", opponent="Kevin Owens",
             stip="NXT Championship — winning WWE gold in the Sumo Hall he left Japan a star of"),
        dict(rating="&mdash;", event="SummerSlam 2016", opponent="Seth Rollins",
             stip="Universal Championship — first holder, torn labrum and all"),
        dict(rating="&mdash;", event="WrestleMania 39 Night 2", opponent="Edge",
             stip="Hell in a Cell — The Demon's first WWE defeat, bloodied mid-match"),
        dict(rating="&mdash;", event="WrestleMania 42 Night 2", opponent="Dominik Mysterio",
             stip="Street fight — The Demon revived to end the Judgment Day story"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("10",  "WWE title reigns"),
            ("3&times;", "IWGP Junior Heavyweight"),
            ("6&times;", "IWGP Junior Tag"),
            ("1",   "Universal Championship"),
        ],
        lead=("Ten WWE reigns and a decade of New Japan gold before them. The pattern worth "
              "noticing: every WWE singles title he has held, he won within his first year of "
              "reaching that roster or returning to it &mdash; and all four tag reigns came inside "
              "the Judgment Day."),
        rows=[
            dict(ic="U", name="WWE Universal Championship", count="1",
                 sub="August 21, 2016 &ndash; August 22, 2016 &middot; def. Seth Rollins at "
                     "SummerSlam to become the inaugural champion &middot; relinquished after "
                     "roughly 22 hours with a torn labrum suffered in the match &middot; never "
                     "lost it"),
            dict(ic="N", name="NXT Championship", count="2",
                 sub="July 4, 2015 &ndash; April 21, 2016 &middot; def. Kevin Owens at The Beast in "
                     "the East in Tokyo, lost to Samoa Joe in Lowell, Massachusetts &middot; "
                     "<b>292 days</b>, then the longest reign in the title's history &middot; "
                     "second reign September 8, 2020 &ndash; April 8, 2021, def. Adam Cole, lost "
                     "to Karrion Kross"),
            dict(ic="I", name="WWE Intercontinental Championship", count="2",
                 sub="February 17, 2019 &ndash; March 11, 2019 &middot; won the Elimination "
                     "Chamber handicap match over Bobby Lashley and Lio Rush &middot; regained "
                     "from Lashley at WrestleMania 35 as The Demon, April 7, 2019, lost to "
                     "Shinsuke Nakamura at Extreme Rules on July 14"),
            dict(ic="S", name="WWE United States Championship", count="1",
                 sub="February 28, 2022 &ndash; April 2022 &middot; def. Damian Priest on Raw "
                     "&middot; lost to Austin Theory; the exact date was not re-verified in this "
                     "pass and is not invented"),
            dict(ic="T", name="Undisputed WWE Tag Team Championship", count="2",
                 sub="With Damian Priest &middot; won from Kevin Owens and Sami Zayn at Payback on "
                     "September 2, 2023 &middot; the reigns bracket a brief October 2023 "
                     "interruption by Cody Rhodes and Jey Uso &middot; ended in the WrestleMania "
                     "XL Night 1 ladder match on April 6, 2024"),
            dict(ic="W", name="World Tag Team Championship", count="2",
                 sub="With JD McDonagh &middot; June 24, 2024 &ndash; December 16, 2024, from "
                     "Awesome Truth to the War Raiders, <b>175 days</b> &middot; June 30, 2025 "
                     "&ndash; October 20, 2025, from The New Day to AJ Styles and Dragon Lee"),
            dict(ic="J", name="IWGP Junior Heavyweight Championship", count="3",
                 sub="As Prince Devitt, NJPW &middot; individual reign dates not verified in this "
                     "pass"),
            dict(ic="G", name="IWGP Junior Heavyweight Tag Team Championship", count="6",
                 sub="As Prince Devitt, mostly with Ryusuke Taguchi as Apollo 55 &middot; reign "
                     "dates not verified"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="He founded the most influential faction of the modern era, then spent four years in "
             "one that ran on expulsions &mdash; and finally ran the script on him.",
        cards=[
            dict(era="NJPW &middot; 2013&ndash;2014",
                 name="Bullet Club",
                 members="Prince Devitt (founder), Karl Anderson, Bad Luck Fale, Tama Tonga, Doc "
                         "Gallows, others",
                 desc="Founded in May 2013 when Devitt turned on Ryusuke Taguchi — the "
                      "foreigner-heel faction whose T-shirts, Too Sweets and alumni (AJ Styles, "
                      "Kenny Omega, The Young Bucks) reshaped the business worldwide. Devitt left "
                      "for WWE in 2014; the club outlived its founder by more than a decade and is "
                      "the single biggest reason his name carries weight with fans who never watched "
                      "him wrestle in Japan."),
            dict(era="WWE &middot; 2022&ndash;2026",
                 name="The Judgment Day",
                 members="Finn Balor, Damian Priest, Rhea Ripley, Dominik Mysterio, JD McDonagh, "
                         "Liv Morgan, Raquel Rodriguez; Edge, briefly",
                 desc="Joined June 6, 2022 and immediately helped vote out Edge, the founder. Four "
                      "tag title reigns followed — two with Priest, whose expulsion he led in "
                      "August 2024, and two with McDonagh. In March 2026 the machine turned on "
                      "him: after he refused to help Dominik Mysterio cheat on March 2 and told "
                      "him Rey might have been right about him, the group beat him down and threw "
                      "him out. Every expulsion in the group's history now traces through Balor — "
                      "twice as executioner, once as the condemned."),
            dict(era="WWE &middot; 2026&ndash;present",
                 name="Unaligned on SmackDown",
                 members="Finn Balor, alone",
                 desc="Traded to SmackDown in June 2026 and running as a singles babyface for the "
                      "first time since 2021 — publicly delighted by Kevin Owens' SummerSlam "
                      "return, and directly in the queue for CM Punk's Undisputed WWE Championship "
                      "alongside Owens and Gunther, with Sami Zayn burning the queue down weekly."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Two names, three faces: <b>Prince Devitt</b> (2001&ndash;2014) &rarr; <b>Finn "
             "Balor</b> (2014&ndash;present) &rarr; and, on the nights that call for it, <b>The "
             "Demon</b>.",
        cards=[
            dict(mono="PD", era="Ireland &amp; NJPW &middot; 2001&ndash;2014", name="Prince Devitt",
                 desc="Debuted in 2001 per Wikipedia's dating and became New Japan's standout "
                      "junior heavyweight: three IWGP Junior Heavyweight Championships, six junior "
                      "tag reigns with Apollo 55, Best of the Super Juniors wins in 2010 and 2013, "
                      "and in May 2013 the founding of the Bullet Club — the heel turn that "
                      "changed two companies, one of them his future employer."),
            dict(mono="FB", era="WWE &middot; 2014&ndash;present", name="Finn Balor",
                 desc="The name is a WWE construction with Irish bones — Finn the folklore hero, "
                      "Balor the demon king of Irish myth, a duality chosen deliberately. First "
                      "NXT Champion to come from Japan's junior ranks, first Universal Champion, "
                      "and one of the few men on the roster whose babyface and heel runs both "
                      "landed."),
            dict(mono="DE", era="Special occasions &middot; 2015&ndash;present", name="The Demon",
                 desc="The body-paint alter ego reserved for the biggest nights — TakeOvers, "
                      "SummerSlam 2016, WrestleMania 35. Its WWE record was unblemished until "
                      "Edge beat it inside Hell in a Cell at WrestleMania 39 on April 2, 2023; "
                      "its revival to destroy Dominik Mysterio at WrestleMania 42 on April 19, "
                      "2026 was the exclamation point on the Judgment Day breakup."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Bray, County Wicklow to the Bullet Club to both ends of the Judgment Day's guillotine.",
        rows=[
            dict(year="2001", title="Debut",
                 desc="Begins wrestling per Wikipedia's dating; reaches New Japan's dojo system by "
                      "2006 as Prince Devitt."),
            dict(year="2013", title="Founds the Bullet Club",
                 desc="Turns on Ryusuke Taguchi in May 2013 and founds the faction that outgrows "
                      "him, New Japan, and arguably every company it touched."),
            dict(year="2015", title="NXT Champion in Tokyo",
                 desc="Beats Kevin Owens at The Beast in the East on July 4, 2015 and holds the "
                      "NXT Championship 292 days — then the longest reign in its history."),
            dict(year="2016", title="First Universal Champion, for 22 hours",
                 desc="Beats Seth Rollins at SummerSlam on August 21 with a labrum torn mid-match; "
                      "relinquishes the title the next day, unbeaten."),
            dict(year="2019", title="The Demon at WrestleMania",
                 desc="Wins the Intercontinental Championship twice — the Elimination Chamber "
                      "handicap match in February, and WrestleMania 35 as The Demon on April 7."),
            dict(year="2020", title="The NXT return",
                 desc="Beats Adam Cole at Super Tuesday II on September 8 for a second NXT "
                      "Championship, held into 2021."),
            dict(year="2022", title="US Champion, then the Judgment Day",
                 desc="Takes the United States title from Damian Priest on February 28 — then "
                      "joins Priest's new faction on June 6 and helps expel its founder, Edge."),
            dict(year="2023", title="Rollins, and tag gold",
                 desc="Loses the World Heavyweight Championship challenge to Seth Rollins at "
                      "SummerSlam on August 5; wins the Undisputed WWE Tag Team Championship with "
                      "Priest at Payback on September 2. The Demon loses for the first time, to "
                      "Edge, at WrestleMania 39 on April 2."),
            dict(year="2024", title="New partner, same gold",
                 desc="Leads Priest's expulsion in August; wins the World Tag Team Championship "
                      "with JD McDonagh on June 24 and holds it 175 days."),
            dict(year="2025", title="The slow break",
                 desc="His stray Coup de Grace hands Dominik Mysterio the Intercontinental "
                      "Championship at WrestleMania 41 on April 20; a second tag reign with "
                      "McDonagh runs June 30 to October 20, ended by AJ Styles and Dragon Lee "
                      "after Dominik's complaints forced the defense."),
            dict(year="2026", title="Expelled, avenged, traded, blocked",
                 desc="Thrown out of the Judgment Day in March; beats Dominik as The Demon at "
                      "WrestleMania 42 on April 19; traded to SmackDown in June; loses the "
                      "SummerSlam No. 1 contender four-way to the returning Kevin Owens on August "
                      "2, and has the August 28 triple threat stolen by Sami Zayn."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Dominik Mysterio", slug="dominik-mysterio",
                 desc="Four years of stablemate friction that detonated over a hammer on March 2, "
                      "2026 — Balor refused to enable the cheat, Dominik lost the Intercontinental "
                      "title to Penta, and the Judgment Day beat Balor out of the group. The Demon "
                      "settled it at WrestleMania 42 on April 19, a street fight added to the card "
                      "that afternoon, ending with a Coup de Grace through a table."),
            dict(name="Seth Rollins",
                 desc="The opponent for both ends of the world-title story: the SummerSlam 2016 "
                      "match that made Balor the first Universal Champion and cost him his "
                      "shoulder, and the SummerSlam 2023 World Heavyweight Championship match "
                      "Rollins won in Detroit with Damian Priest's briefcase looming over both "
                      "men."),
            dict(name="Kevin Owens",
                 desc="Opponent, then adjacent champion, then friend. Balor took the NXT title "
                      "from Owens in Tokyo in 2015; Owens inherited the Universal title Balor "
                      "vacated in 2016; Balor and Priest beat Owens and Sami Zayn for the tag "
                      "titles at Payback 2023. In 2026 they are allies and rivals at once — Owens "
                      "pinned Zayn in the SummerSlam four-way Balor was in, and Balor has said "
                      "publicly he was happy just to be there for the return."),
            dict(name="Sami Zayn",
                 desc="The active antagonist. Zayn's open-challenge era ended long ago; the 2026 "
                      "version lost the Undisputed WWE Championship to CM Punk, lost the "
                      "SummerSlam four-way, and has since made himself the lock on the door Balor "
                      "keeps reaching for — pulling him off the winning pin on the August 28 "
                      "SmackDown and laying out all four men in the title picture with the belt."),
            dict(name="Edge",
                 desc="The Judgment Day's founder, expelled with Balor's help in June 2022 — and "
                      "the man who took The Demon's undefeated record inside Hell in a Cell at "
                      "WrestleMania 39 on April 2, 2023, in what became Edge's final WrestleMania "
                      "match for WWE."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Thin by design — the verified list is short, and nothing is added to pad it.",
        rows=[
            dict(when="2016&ndash;", title="WWE 2K", kind="Game",
                 desc="A series regular across the modern era, with The Demon frequently included "
                      "as a separate playable character; specific editions were not re-verified in "
                      "this pass."),
            dict(when="2013&ndash;", title="Bullet Club merchandise era", kind="Business",
                 desc="The faction he founded became one of wrestling's best-selling merchandise "
                      "brands and a case study in wrestlers owning their iconography — the "
                      "commercial legacy predates and outlasts his own WWE run."),
            dict(when="2026", title="Post-SummerSlam interviews", kind="Interviews",
                 desc="His August 2026 comments on Kevin Owens' return — “I was very, very "
                      "happy to be there” (411Mania, WrestleTalk) — are the current "
                      "on-record source for where the character stands. No film, autobiography or "
                      "documentary centred on him was verified in this pass, so none is listed."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated the way the sources state them &mdash; with the vacated-not-lost "
             "distinction kept where most retellings drop it.",
        stats=[
            ("1st", "Universal Champion"),
            ("292", "Day NXT reign"),
            ("10",  "WWE title reigns"),
        ],
        rows=[
            dict(name="First Universal Champion in WWE history",
                 sub="August 21, 2016, beating Seth Rollins at SummerSlam. He relinquished the "
                     "title roughly 22 hours later with a labrum torn during the match — the "
                     "shortest world reign in the company's history, and the only one never lost "
                     "in a match."),
            dict(name="292 days as NXT Champion",
                 sub="July 4, 2015 to April 21, 2016 — then the longest reign in the title's "
                     "history, won from Kevin Owens in Tokyo's Sumo Hall and ended by Samoa Joe "
                     "at a non-televised event in Lowell, Massachusetts."),
            dict(name="Founded the Bullet Club",
                 sub="May 2013, NJPW. The faction's later membership — AJ Styles, Kenny Omega, "
                     "the Young Bucks — built the merchandise empire and the cross-promotional "
                     "web that reshaped 2010s wrestling. He left for WWE within a year of "
                     "founding it."),
            dict(name="Ten WWE championship reigns across five titles",
                 sub="One Universal, two NXT, two Intercontinental, one United States, two "
                     "Undisputed WWE Tag Team (with Damian Priest), two World Tag Team (with JD "
                     "McDonagh). All four tag reigns came inside the Judgment Day."),
            dict(name="The Demon lost exactly once in WWE",
                 sub="To Edge, inside Hell in a Cell, at WrestleMania 39 on April 2, 2023. The "
                     "persona returned three years later at WrestleMania 42 and won — its record "
                     "across a decade of selective use remains one loss."),
            dict(name="Three IWGP Junior Heavyweight Championships and two Best of the Super Juniors",
                 sub="As Prince Devitt, with tournament wins in 2010 and 2013 and six junior tag "
                     "reigns alongside. Individual reign dates were not verified in this pass and "
                     "are not invented."),
            dict(name="Present at three faction expulsions - on both ends of the mechanism",
                 sub="Helped expel Edge (June 2022), led the expulsion of Damian Priest (August "
                     "2024), and was himself beaten down and expelled (March 2026). No other "
                     "wrestler's Judgment Day tenure touches all three."),
        ],
        footnote=("Deliberately absent: a career win-loss total; NJPW reign dates, which were not "
                  "verified in the opened sources; the exact April 2022 date of the United States "
                  "title loss to Austin Theory; and social handles. House style renders the name "
                  "without diacritics throughout - the trademark spelling uses them."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography",
             href="https://en.wikipedia.org/wiki/Finn_B%C3%A1lor"),
        dict(k="POST Wrestling", v="WrestleMania 42 — The Demon beats Dominik Mysterio",
             href="https://www.postwrestling.com/2026/04/19/demon-finn-balor-wins-street-fight-against-dominik-mysterio-at-wrestlemania-42/"),
        dict(k="Bleacher Report", v="The Judgment Day expulsion, explained",
             href="https://bleacherreport.com/articles/25415881-finn-balor-beats-dominik-mysterio-wwe-wrestlemania-42-after-judgment-days-surprise-turn"),
        dict(k="TJR Wrestling", v="August 28, 2026 SmackDown — Zayn destroys the triple threat",
             href="https://tjrwrestling.net/news/breaking-ex-wwe-champion-lays-out-cm-punk-kevin-owens-gunther-finn-balor-on-smackdown/"),
        dict(k="The Sportster", v="SummerSlam 2026 Night 2 — the Owens four-way",
             href="https://www.thesportster.com/wwe-summerslam-2026-night-2-results-recap-august-2-2026/"),
        dict(k="Sportskeeda", v="October 2025 — losing the World Tag Team titles",
             href="https://www.sportskeeda.com/wwe/news-finn-balor-breaks-silence-losing-wwe-world-tag-team-titles-raw"),
        dict(k="WrestleTalk", v="Balor on Kevin Owens' SummerSlam return",
             href="https://wrestletalk.com/news/finn-balor-kevin-owens-wwe-return-thoughts/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Did Finn Balor lose the Universal Championship the night after SummerSlam 2016?",
            a="No &mdash; he never lost it at all. He beat Seth Rollins at SummerSlam on August "
              "21, 2016 to become the <b>first Universal Champion</b>, tore the labrum in his "
              "right shoulder during that match, and <b>relinquished</b> the title on the August "
              "22 Raw, roughly 22 hours into the reign. It is the shortest world title reign in "
              "WWE history, and the only one that ended with the champion undefeated. The injury "
              "kept him out until the following spring.",
            q_ld="Did Finn Balor lose the WWE Universal Championship in a match?",
            a_ld="No. Finn Balor never lost the WWE Universal Championship. He defeated Seth "
                 "Rollins at SummerSlam on August 21, 2016 to become the first Universal Champion, "
                 "suffered a torn labrum in his right shoulder during the match, and relinquished "
                 "the title on the August 22, 2016 episode of Raw, about 22 hours after winning "
                 "it. It is the shortest world championship reign in WWE history, and it ended by "
                 "vacation due to injury, not by defeat."),
        dict(
            q="Why was Finn Balor kicked out of the Judgment Day?",
            a="Because he refused to help Dominik Mysterio cheat. On the March 2, 2026 Raw, Balor "
              "stopped JD McDonagh from handing Dominik a hammer mid-match; Dominik lost the "
              "Intercontinental Championship to Penta, confronted Balor, and was told his "
              "estranged father might have been right about him. The Judgment Day &mdash; "
              "Dominik, McDonagh, Liv Morgan and Raquel Rodriguez &mdash; beat Balor down and "
              "expelled him, the same treatment the group had given Edge in 2022 and Damian "
              "Priest in 2024, both times with Balor's participation. He answered as The Demon at "
              "WrestleMania 42, beating Dominik in a street fight on April 19, 2026.",
            q_ld="Why was Finn Balor expelled from the Judgment Day?",
            a_ld="Finn Balor was expelled from the Judgment Day in March 2026 after he prevented "
                 "JD McDonagh from handing Dominik Mysterio a hammer during Dominik's March 2, "
                 "2026 Intercontinental Championship defense, which Dominik lost to Penta. In the "
                 "confrontation that followed, Balor suggested Rey Mysterio had been right about "
                 "his son, and the group attacked him and threw him out. Balor got his revenge at "
                 "WrestleMania 42 on April 19, 2026, defeating Dominik Mysterio in a street fight "
                 "as The Demon."),
        dict(
            q="Is Finn Balor on Raw or SmackDown, and is he chasing a title?",
            a="<b>SmackDown</b>, since a June 2026 trade, and yes: CM Punk's Undisputed WWE "
              "Championship. He was in the surprise No. 1 contender four-way at SummerSlam on "
              "August 2, 2026, which the returning Kevin Owens won by pinning Sami Zayn, and in "
              "the triple threat with Owens and Gunther on the August 28 SmackDown, which he had "
              "won &mdash; Coup de Grace delivered, cover made &mdash; until Zayn pulled him out "
              "of the ring, flattened the referee, and beat down all four men in the title "
              "picture. The contendership remains unsettled as of August 31, 2026.",
            q_ld="Is Finn Balor on Raw or SmackDown in 2026?",
            a_ld="Finn Balor has been on SmackDown since being traded there in June 2026. As of "
                 "August 31, 2026 he is pursuing CM Punk's Undisputed WWE Championship: he "
                 "competed in the number one contender fatal four-way at SummerSlam on August 2, "
                 "2026, won by the returning Kevin Owens, and in a triple threat with Kevin Owens "
                 "and Gunther on the August 28 SmackDown that ended without a winner when Sami "
                 "Zayn attacked all of the participants and the referee."),
        dict(
            q="What is The Demon's record in WWE?",
            a="Effectively unbeaten, with one asterisk-free exception. Across a decade of "
              "selective appearances &mdash; NXT TakeOvers, SummerSlam 2016, WrestleMania 35, "
              "WrestleMania 42 &mdash; the paint has lost once: to Edge, inside Hell in a Cell, "
              "at WrestleMania 39 on April 2, 2023. Its most recent outing beat Dominik Mysterio "
              "in the WrestleMania 42 street fight on April 19, 2026, finished with a Coup de "
              "Grace through a table.",
            q_ld="What is The Demon Finn Balor's win-loss record in WWE?",
            a_ld="The Demon, Finn Balor's painted alter ego, has lost only once in WWE: to Edge "
                 "inside Hell in a Cell at WrestleMania 39 on April 2, 2023. Its appearances are "
                 "reserved for major events, including the SummerSlam 2016 Universal Championship "
                 "win, the WrestleMania 35 Intercontinental Championship win over Bobby Lashley, "
                 "and most recently the WrestleMania 42 street fight win over Dominik Mysterio on "
                 "April 19, 2026."),
        dict(
            q="Did Finn Balor really found the Bullet Club?",
            a="Yes. As Prince Devitt in New Japan, he turned on his tag partner Ryusuke Taguchi "
              "and founded the Bullet Club in <b>May 2013</b>, leading it until his 2014 "
              "departure for WWE. The faction's later leaders and members &mdash; AJ Styles, "
              "Kenny Omega, the Young Bucks &mdash; turned it into a global brand, but the "
              "founding turn was his. In WWE he has never led a faction of his own creation; the "
              "Judgment Day, which he joined on June 6, 2022, was Edge's.",
            q_ld="Did Finn Balor found the Bullet Club?",
            a_ld="Yes. Wrestling as Prince Devitt in New Japan Pro-Wrestling, Finn Balor founded "
                 "the Bullet Club in May 2013 after turning on his tag team partner Ryusuke "
                 "Taguchi, and led the faction until he left for WWE in 2014. Later members such "
                 "as AJ Styles, Kenny Omega and the Young Bucks grew it into a global brand after "
                 "his departure."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Fergal Devitt"),
        dict(label="Born", value="July 25, 1981",
             sub="Bray, County Wicklow, Ireland &middot; age 45"),
        dict(label="Height", value="5&#8242;11&#8243;", sub="180 cm"),
        dict(label="Weight", value="190 lb", sub="86 kg (billed)"),
        dict(label="Debut", value="November 23, 2001", sub="per Wikipedia's dating"),
        dict(label="Ring names", value="Prince Devitt &rarr; Finn Balor",
             sub="NJPW 2006&ndash;14 &middot; WWE 2014&ndash;present &mdash; the WWE name splices "
                 "Irish myth: Finn the hero, Balor the demon king"),
        dict(label="Signature", value="Coup de Grace &middot; 1916 &middot; Sling Blade &middot; "
                                      "shotgun dropkick",
             sub="the Coup de Grace top-rope double stomp is the constant across eras"),
        dict(label="Alter ego", value="The Demon", sub="one WWE loss in a decade of appearances"),
        dict(label="Faction history", value="Bullet Club (founder) &middot; Balor Club &middot; "
                                            "The Judgment Day"),
        dict(label="Brand", value="SmackDown", sub="traded from Raw in June 2026"),
        dict(label="Also known as", value="The Prince &middot; The Demon King"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1981-07-25",
    bornplace="Bray, County Wicklow, Ireland",
    nationality="Ireland",
    height_cm=180,
    weight_kg=86,
    ld=dict(
        alternateName=["Fergal Devitt", "Prince Devitt", "The Prince", "The Demon",
                       "The Demon King"],
        award=["WWE Universal Championship (inaugural champion, 2016)",
               "NXT Championship (2 reigns, including 292 days)",
               "WWE Intercontinental Championship (2 reigns)",
               "WWE United States Championship (1 reign)",
               "Undisputed WWE Tag Team Championship (2 reigns, with Damian Priest)",
               "World Tag Team Championship (2 reigns, with JD McDonagh)",
               "IWGP Junior Heavyweight Championship (3 reigns, as Prince Devitt)",
               "IWGP Junior Heavyweight Tag Team Championship (6 reigns)",
               "Best of the Super Juniors winner (2010, 2013)"],
        knowsAbout=["Professional wrestling", "Bullet Club", "The Judgment Day", "NJPW", "NXT",
                    "WWE", "Championship wrestling"],
        description="Finn Balor, born Fergal Devitt in Bray, County Wicklow, is an Irish "
                    "professional wrestler signed to WWE. As Prince Devitt in New Japan "
                    "Pro-Wrestling he founded the Bullet Club in 2013 and held the IWGP Junior "
                    "Heavyweight Championship three times. In WWE he became the first Universal "
                    "Champion at SummerSlam 2016, held the NXT Championship for 292 days, and has "
                    "accumulated ten championship reigns. Expelled from the Judgment Day in March "
                    "2026, he beat Dominik Mysterio as The Demon at WrestleMania 42 and now "
                    "wrestles on SmackDown.",
        sameAs=["https://en.wikipedia.org/wiki/Finn_B%C3%A1lor",
                "https://www.wwe.com/superstars/finn-balor"],
    ),
)
