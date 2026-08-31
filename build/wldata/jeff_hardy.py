# -*- coding: utf-8 -*-
"""Jeff Hardy - dossier data.

Sources: web-verified August 31, 2026 (Wikipedia's Jeff Hardy, Hardy Boyz and TNA World
Tag Team Championship pages; Slam Wrestling and PWTorch reports of the August 27, 2026
iMPACT). Every match row carries a day-precision date confirmed in those sources.

Status, verified for August 31, 2026: ACTIVE in TNA. On the August 27, 2026 iMPACT
from Brampton, Ontario, he was found attacked - part of TNA's running mystery-attacker
storyline - and left the show loaded into an ambulance, with Matt Hardy at his side.
IMPORTANT status correction established by this pass: the Hardys are NOT the current
TNA World Tag Team Champions. They lost the titles to The System (Brian Myers & Bear
Bronson) at Rebellion on April 11, 2026, and the Nemeths held and defended the belts
on the August 27 show. Any framing of Jeff as a reigning tag champion is out of date.

Deliberate omissions:
  * No career win-loss total - no verified figure exists.
  * No Meltzer star ratings in the signature block - not verified in this pass.
  * The identity of the August 27 attacker is unrevealed on-screen and unreported;
    nothing is speculated here.
"""

# ----------------------------------------------------------------- record rows
# 21 documented bouts - the ladder/TLC canon, all six world title changes, the TNA
# era's highs and lows, and the 2024-26 Hardys run.
ROWS = [
    dict(result="W", date="1999-10-17", promo="WWE", landmark=True, type="tag",
         event="No Mercy", opponent="Edge & Christian",
         stip="Ladder match, with Matt — the Terri Invitational that made both teams", title=""),
    dict(result="L", date="2000-08-27", promo="WWE", landmark=True, type="tag",
         event="SummerSlam", opponent="Edge & Christian; The Dudley Boyz",
         stip="The first TLC match", title="WWF Tag Team Championship"),
    dict(result="L", date="2001-04-01", promo="WWE", landmark=True, type="tag",
         event="WrestleMania X-Seven", opponent="Edge & Christian; The Dudley Boyz",
         stip="TLC II — the Swanton off the ladder through the tables era", title="WWF Tag Team Championship"),
    dict(result="W", date="2001-04-12", promo="WWE",
         event="SmackDown", opponent="Triple H",
         stip="Singles — the upset", title="WWF Intercontinental Championship"),
    dict(result="L", date="2002-07-01", promo="WWE",
         event="Raw", opponent="The Undertaker",
         stip="Ladder match — the loss that made him a singles act",
         title="WWE Undisputed Championship"),
    dict(result="W", date="2008-12-14", promo="WWE", landmark=True, type="tag",
         event="Armageddon", opponent="Edge & Triple H",
         stip="Triple threat — first world title, eight years in the making", title="WWE Championship"),
    dict(result="L", date="2009-01-25", promo="WWE",
         event="Royal Rumble", opponent="Edge",
         stip="Singles — Matt turns heel with the chair", title="WWE Championship"),
    dict(result="W", date="2009-06-07", promo="WWE", landmark=True,
         event="Extreme Rules", opponent="Edge",
         stip="Ladder match", title="World Heavyweight Championship"),
    dict(result="L", date="2009-06-07", promo="WWE",
         event="Extreme Rules", opponent="CM Punk",
         stip="Money in the Bank cash-in, minutes later", title="World Heavyweight Championship"),
    dict(result="W", date="2009-07-26", promo="WWE",
         event="Night of Champions", opponent="CM Punk",
         stip="Singles — second World Heavyweight reign", title="World Heavyweight Championship"),
    dict(result="L", date="2009-08-23", promo="WWE", landmark=True,
         event="SummerSlam", opponent="CM Punk",
         stip="TLC — days later he lost the cage match that wrote him out of WWE",
         title="World Heavyweight Championship"),
    dict(result="W", date="2010-10-10", promo="TNA", landmark=True, type="tag",
         event="Bound for Glory", opponent="Kurt Angle & Mr. Anderson",
         stip="Triple threat for the vacant title — the they/Immortal heel turn",
         title="TNA World Heavyweight Championship"),
    dict(result="L", date="2011-03-13", promo="TNA", landmark=True,
         event="Victory Road", opponent="Sting",
         stip="Singles, stopped in about 90 seconds — the lowest public moment, by his own account",
         title="TNA World Heavyweight Championship"),
    dict(result="W", date="2012-10-14", promo="TNA", landmark=True,
         event="Bound for Glory", opponent="Austin Aries",
         stip="Singles — the redemption reign, his third TNA world title",
         title="TNA World Heavyweight Championship"),
    dict(result="W", date="2017-04-02", promo="WWE", landmark=True, type="tag",
         event="WrestleMania 33 — Orlando", opponent="The Bar, Enzo & Cass, Gallows & Anderson",
         stip="Fatal four-way ladder match, with Matt — the surprise return",
         title="Raw Tag Team Championship"),
    dict(result="W", date="2018-04-16", promo="WWE",
         event="Raw", opponent="Jinder Mahal",
         stip="Singles — completes the WWE Grand Slam", title="WWE United States Championship"),
    dict(result="W", date="2024-10-26", promo="TNA", landmark=True, type="tag",
         event="Bound for Glory", opponent="The System & ABC",
         stip="Full Metal Mayhem, with Matt — TNA tag champions twenty-five years after No Mercy",
         title="TNA World Tag Team Championship"),
    dict(result="W", date="2025-07-20", promo="TNA", type="tag",
         event="Slammiversary — Long Island", opponent="The Nemeths, The Rascalz & Fir$t Cla$$",
         stip="Four-way ladder match, with Matt — the belts come back",
         title="TNA World Tag Team Championship"),
    dict(result="W", date="2025-10-07", promo="WWE", landmark=True, type="tag",
         event="NXT vs. TNA Showdown", opponent="DarkState",
         stip="Winners take all, with Matt — NXT and TNA tag titles held at once",
         title="NXT Tag Team Championship"),
    dict(result="L", date="2025-10-25", promo="WWE", type="tag",
         event="NXT Halloween Havoc", opponent="DarkState",
         stip="Broken Rules match, with Matt — the 18-day NXT reign ends",
         title="NXT Tag Team Championship"),
    dict(result="L", date="2026-04-11", promo="TNA", type="tag",
         event="Rebellion — Cleveland", opponent="The System",
         stip="Tag, with Matt — Brian Myers & Bear Bronson take the titles",
         title="TNA World Tag Team Championship"),
]

DATA = dict(
    slug="jeff-hardy",
    name="Jeff Hardy",
    realname="Jeffrey Nero Hardy",
    epithet="The Charismatic Enigma",
    hook="Record & Titles",

    meta_desc=("Jeff Hardy, the Charismatic Enigma, is active in TNA at 49 and was stretchered "
               "out of the August 27, 2026 iMPACT in a mystery-attacker storyline. Six world "
               "titles, the TLC canon, the Hardys. Full record, titles and career."),
    og_desc=("The Charismatic Enigma: the TLC matches that redefined risk, six world "
             "championships, three lives' worth of comebacks — and, as of August 27, 2026, a TNA "
             "whodunnit with his name on the stretcher."),
    tw_desc="Jeff Hardy: six world titles, the TLC canon, still active in TNA at 49.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1993",
    height_imp="6&#8242;1&#8243;",
    weight_lb="225",
    world_titles="6",
    vitals_tagline="The Charismatic Enigma",
    support_note="Merch &middot; Watch &middot; Read",
    sp_items=[
        dict(ic="JH", title="TNA Wrestling", sub="Official site — iMPACT weekly",
             tag="Visit", href="https://tnawrestling.com/"),
        dict(ic="PWT", title="Pro Wrestling Tees", sub="Independent merch marketplace",
             tag="Shop", href="https://www.prowrestlingtees.com/"),
        dict(ic="2K", title="WWE 2K", sub="A playable legend in past entries",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="W", title="Wikipedia", sub="Full biography", tag="Read", charity=True,
             href="https://en.wikipedia.org/wiki/Jeff_Hardy"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Charismatic Enigma &middot; Brother Nero &middot; Willow &middot; one half of The Hardys",
    hero_tag="Cameron, North Carolina &middot; <em>OMEGA &middot; WWE &middot; TNA &middot; AEW "
             "&middot; TNA again &middot; 1993&ndash;present</em>",
    now_label="NOW",
    now_bold="Active in TNA — and written out on a stretcher",
    now_tail=(" &middot; found attacked on the August 27, 2026 iMPACT and taken out by ambulance, "
              "the latest victim of TNA's mystery-attacker storyline on the road to Bound for "
              "Glory &middot; not currently a champion: the Hardys lost the TNA tag titles at "
              "Rebellion on April 11, 2026"),
    hstats=[
        dict(value="6",  x=False, label="World Titles"),
        dict(value="10", x=False, label="Tag Reigns w/ Matt in WWE"),
        dict(value="49", x=False, label="Years Old, Still Jumping"),
        dict(value="0",  x=True,  label="Current Titles"),
    ],
    ghost_link="From a Cameron backyard federation to every ladder that ever mattered",
    vlabel="Est. 1993 &middot; Cameron, North Carolina",
    mono="JH",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Jeff Hardy</b> turned 49 on August 31, 2026, is an active TNA wrestler, and four days "
        "earlier was carried out of the CAA Centre in Brampton, Ontario on a stretcher &mdash; "
        "storyline, to be clear. On the August 27 iMPACT he became the latest name on the victim "
        "list of TNA&rsquo;s running mystery-attacker angle, loaded into an ambulance with a "
        "confused, furious Matt Hardy alongside, as the company built its whodunnit toward Bound "
        "for Glory. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">6</span>'
        '<span class="pull-cap">world championships &mdash; one WWE, two World Heavyweight, three TNA</span></span>'
        "That a thirty-three-year veteran is the centrepiece of the fall storyline tells you what "
        "he still is to TNA: with Matt, the biggest mainstream names on the roster, and on his "
        "own, one of the most beloved high-risk performers wrestling has produced.",

        "One current-events correction, because it is widely gotten wrong: <b>the Hardys are not "
        "the reigning TNA World Tag Team Champions</b>. They lost the titles to The System &mdash; "
        "Brian Myers and Bear Bronson &mdash; at Rebellion in Cleveland on April 11, 2026, and on "
        "the very show where Jeff was stretchered out, the champions defending in the main event "
        "were the Nemeths. The Hardys&rsquo; 2024&ndash;26 TNA run was still remarkable: tag "
        "titles won in Full Metal Mayhem at Bound for Glory on October 26, 2024, lost and regained "
        "through 2025 including a four-way ladder win at Slammiversary on July 20, 2025, plus a "
        "winners-take-all victory over DarkState at NXT vs. TNA Showdown on October 7, 2025 that "
        "made them NXT and TNA tag champions simultaneously &mdash; for eighteen days, until "
        "Halloween Havoc. But as of August 31, 2026, Jeff holds no title, and the story TNA is "
        "telling with him is a mystery, not a reign.",

        "The legend rests on ladders. With Matt &mdash; his real brother, his tag partner since "
        "their backyard OMEGA promotion in Cameron, North Carolina &mdash; he redefined what a "
        "televised stunt could be: the No Mercy 1999 ladder match against Edge and Christian, the "
        "first TLC at SummerSlam 2000, TLC II at WrestleMania X-Seven, ten WWE tag championship "
        "reigns and gold in WCW-lineage, ROH, TNA and NXT besides. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">2008</span>'
        '<span class="pull-cap">WWE Champion at Armageddon &mdash; the people&rsquo;s payoff, eight years of falling included</span></span>'
        "As a singles act he was the underdog the audience adopted: the 2001 Intercontinental "
        "upset of Triple H, the 2002 ladder challenge to The Undertaker, and finally the WWE "
        "Championship at Armageddon on December 14, 2008 &mdash; then two World Heavyweight "
        "Championship reigns in 2009, bracketed by the CM Punk feud whose straight-edge-versus-"
        "recklessness subtext was barely subtext. In TNA he won three world championships, hit "
        "genuine bottom &mdash; the Victory Road 2011 match against Sting that was stopped in "
        "roughly ninety seconds because he was in no condition to perform &mdash; and built the "
        "redemption arc back to a fourth act nobody expected to last this long.",

        "The honest version of this page includes the record off the ladder too: the 2003 WWE "
        "release over reliability and substance problems, suspensions under the wellness policy, "
        "the 2011 nadir, the 2022 DUI arrest that got him suspended and sent to rehab during his "
        "AEW run. He has been open about all of it, sobriety included, and the 2024&ndash;26 TNA "
        "chapter &mdash; reliable, healthy, main-eventing pay-per-views with his brother in his "
        "late forties &mdash; is the part of the story his supporters waited twenty years to "
        "read. The Swanton Bomb still comes off the top; the crowd still holds its breath.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE", "TNA"],
        promo_labels={"WWE": "WWE", "TNA": "TNA"},
        stats=[
            ("1&times;", "WWE Championship"),
            ("2&times;", "World Heavyweight"),
            ("3&times;", "TNA World title"),
            ("10",       "WWE tag reigns w/ Matt"),
            ("5&times;", "Intercontinental"),
            ("3",        "TNA tag reigns w/ Matt"),
        ],
        lead=("Twenty-one documented bouts &mdash; the ladder and TLC canon, all six world title "
              "changes, the Victory Road nadir and the 2024&ndash;26 Hardys run. A curated ledger, "
              "not a career count; no career win&ndash;loss total is published because no verified "
              "one exists. His AEW matches (2022&ndash;24) are deliberately unlisted: none carried "
              "a title change, and this pass verified none to the day. Filter by match type, tap "
              "any column header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The bouts the reputation rests on. Star ratings are deliberately not "
                    "published: Observer figures were not verified in this pass, and this page "
                    "does not guess at numbers."),
    signature=[
        dict(rating="&mdash;", event="No Mercy 1999", opponent="Edge & Christian",
             stip="Ladder match, with Matt — the one that started the era"),
        dict(rating="&mdash;", event="WrestleMania X-Seven", opponent="Edge & Christian; The Dudley Boyz",
             stip="TLC II — the definitive multi-team car crash"),
        dict(rating="&mdash;", event="Raw, July 1, 2002", opponent="The Undertaker",
             stip="Ladder match for the Undisputed title — 'made' as a singles star in defeat"),
        dict(rating="&mdash;", event="SummerSlam 2009", opponent="CM Punk",
             stip="TLC for the World Heavyweight Championship — the exit masterpiece"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("6",  "World titles"),
            ("10", "WWE tag reigns"),
            ("5&times;", "Intercontinental"),
            ("0",  "Held right now"),
        ],
        lead=("Six world championships and a tag resume spread across four decades and five "
              "companies. Reign endpoints beyond those stated were not re-verified in this pass "
              "and are not invented here."),
        rows=[
            dict(ic="W", name="WWE Championship", count="1",
                 sub="Armageddon, December 14, 2008, in a triple threat over Triple H and Edge "
                     "&middot; lost to Edge at the Royal Rumble on January 25, 2009, with Matt "
                     "turning heel in the finish"),
            dict(ic="H", name="World Heavyweight Championship", count="2",
                 sub="Extreme Rules, June 7, 2009, in a ladder match over Edge &mdash; lost to CM "
                     "Punk&rsquo;s Money in the Bank cash-in minutes later &middot; regained from "
                     "Punk at Night of Champions on July 26, lost the SummerSlam TLC on August 23"),
            dict(ic="T", name="TNA World Heavyweight Championship", count="3",
                 sub="Bound for Glory, October 10, 2010 (vacant-title triple threat, the Immortal "
                     "turn) &middot; 2011 &middot; Bound for Glory, October 14, 2012, from Austin "
                     "Aries &mdash; the redemption reign"),
            dict(ic="G", name="WWF/WWE tag championships, with Matt", count="10",
                 sub="Six WWF/World Tag Team reigns in the original run, the Raw Tag Team "
                     "Championship won in the WrestleMania 33 return ladder match on April 2, "
                     "2017, and the SmackDown Tag Team titles in 2019 among them &middot; WWE "
                     "itself markets them as one of the greatest tag teams ever"),
            dict(ic="N", name="TNA World Tag Team Championship", count="3",
                 sub="With Matt: the Broken-era reign begun at Bound for Glory 2016, then Bound "
                     "for Glory 2024 (Full Metal Mayhem) and Slammiversary 2025 (four-way "
                     "ladder) &middot; lost the belts to The System at Rebellion on April 11, "
                     "2026 &mdash; the Hardys are not the current champions"),
            dict(ic="X", name="NXT Tag Team Championship", count="1",
                 sub="NXT vs. TNA Showdown, October 7, 2025, winners take all over DarkState "
                     "&middot; lost back to DarkState in a Broken Rules match at Halloween Havoc "
                     "on October 25 &mdash; an 18-day, two-company double reign"),
            dict(ic="I", name="WWE Intercontinental Championship", count="5",
                 sub="First won April 12, 2001, upsetting Triple H on SmackDown &middot; part of "
                     "the Grand Slam completed with the United States Championship win over "
                     "Jinder Mahal on April 16, 2018"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Teams &amp; Factions",
        lead="One team above everything, and two detours that defined eras anyway.",
        cards=[
            dict(era="1993&ndash;present",
                 name="The Hardys / The Hardy Boyz",
                 members="Jeff Hardy, Matt Hardy",
                 desc="Brothers from Cameron, North Carolina who started in their own backyard-"
                      "grown OMEGA promotion and became, per WWE's own framing, one of the "
                      "greatest tag teams in history — ten WWE tag reigns, the TLC trilogy, and "
                      "championship runs in TNA, ROH and NXT. The 2024-26 TNA reunion made them "
                      "double champions across two companies in October 2025, twenty-six years "
                      "after their first WWF tag titles."),
            dict(era="TNA &middot; 2010&ndash;2011",
                 name="Immortal",
                 members="Hulk Hogan, Eric Bischoff, Jeff Hardy, Abyss, and others",
                 desc="The heel mega-stable he joined by winning the vacant TNA World Heavyweight "
                      "Championship at Bound for Glory 2010 in the 'they' angle — his "
                      "'Antichrist of wrestling' heel run, cut short by the personal collapse "
                      "that produced Victory Road 2011."),
            dict(era="WWE &middot; 2000s",
                 name="Team Xtreme",
                 members="Matt Hardy, Jeff Hardy, Lita",
                 desc="The Hardys plus Lita — the trio that made the team a mainstream youth-"
                      "culture act at the Attitude Era's peak, all cargo pants, face paint and "
                      "top-rope recklessness."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One man, several frequencies: <b>Jeff Hardy</b> &rarr; <b>Willow the Wisp</b> "
             "&rarr; <b>Brother Nero</b> &rarr; back again. The enigma part was never an act.",
        cards=[
            dict(mono="TX", era="WWF/WWE &middot; 1998&ndash;2003", name="Team Xtreme daredevil",
                 desc="The rave-lights high-flyer of the Attitude Era tag division — the Swanton "
                      "off anything, the dancing entrance, the audience's adopted little brother."),
            dict(mono="CE", era="WWE &amp; TNA &middot; 2006&ndash;", name="The Charismatic Enigma",
                 desc="The singles identity: face paint, self-drawn imagery, his own music, an "
                      "underdog whose flaws were part of the bond with the crowd. Peaked with the "
                      "2008-09 world title arc."),
            dict(mono="WI", era="OMEGA &amp; TNA &middot; 1990s, 2014", name="Willow",
                 desc="The umbrella-carrying masked alter ego from the OMEGA days, revived in TNA "
                      "in 2014 — proof the enigma branding described a real interior world of "
                      "characters, paintings and concept albums."),
            dict(mono="BN", era="TNA &middot; 2016&ndash;2017", name="Brother Nero",
                 desc="His role in Matt's 'Broken' universe — the Broken Hardys' Deletion-era "
                      "surrealism became one of the most influential wrestling storytelling "
                      "experiments of the 2010s and set up the WrestleMania 33 return pop."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="A trampoline federation in Cameron to a stretcher angle in Brampton, thirty-three "
             "years apart.",
        rows=[
            dict(year="1993", title="OMEGA and the jobber years",
                 desc="Wrestles as a teenager in the brothers' OMEGA promotion; first WWF TV "
                      "appearances as enhancement talent follow in 1994, at sixteen."),
            dict(year="1999", title="The ladder era opens",
                 desc="The Hardy Boyz win the No Mercy ladder match over Edge and Christian on "
                      "October 17 — the match that creates the three-team era with the Dudleys."),
            dict(year="2001", title="Singles proof of concept",
                 desc="Upsets Triple H for the Intercontinental Championship on the April 12 "
                      "SmackDown while the TLC trilogy runs on."),
            dict(year="2003", title="Released",
                 desc="WWE lets him go in April over missed dates and substance problems — the "
                      "first public bottom."),
            dict(year="2008", title="WWE Champion",
                 desc="Wins the triple threat at Armageddon on December 14 — the payoff to the "
                      "most sustained underdog chase of the era."),
            dict(year="2009", title="The Punk feud and the exit",
                 desc="Two World Heavyweight Championship reigns inside three months; loses the "
                      "SummerSlam TLC to CM Punk on August 23 and leaves WWE days later."),
            dict(year="2010", title="TNA champion, heel, Immortal",
                 desc="Wins the vacant TNA World Heavyweight Championship at Bound for Glory on "
                      "October 10 and turns heel in the 'they' angle."),
            dict(year="2011", title="Victory Road",
                 desc="The Sting match on March 13 is stopped in roughly ninety seconds because "
                      "he is unable to perform — the public rock bottom he has since owned in "
                      "interviews."),
            dict(year="2012", title="The redemption reign",
                 desc="Beats Austin Aries at Bound for Glory on October 14 for his third TNA "
                      "world title, completing the sobriety-era comeback arc."),
            dict(year="2017", title="The WrestleMania 33 return",
                 desc="The Hardys surprise-enter the Raw tag title ladder match on April 2 and "
                      "win — among the loudest pops in WrestleMania history."),
            dict(year="2018", title="Grand Slam",
                 desc="Beats Jinder Mahal for the United States Championship on the April 16 Raw, "
                      "completing the WWE Grand Slam."),
            dict(year="2022", title="AEW, arrest, rehab",
                 desc="Joins Matt in AEW in March; a June DUI arrest brings suspension and "
                      "treatment; he returns in 2023 and finishes the contract quietly."),
            dict(year="2024", title="Home to TNA",
                 desc="Returns alongside Matt at Against All Odds on June 14; they win the TNA "
                      "World Tag Team Championship in Full Metal Mayhem at Bound for Glory on "
                      "October 26."),
            dict(year="2025", title="Double champions at 48",
                 desc="Regain the TNA tag titles in the Slammiversary ladder match on July 20, "
                      "beat DarkState winners-take-all on October 7 to add the NXT titles, and "
                      "retain against Team 3D in a tables match at Bound for Glory on October 12."),
            dict(year="2026", title="Titles lost, mystery begun",
                 desc="The System take the TNA tag titles at Rebellion on April 11; on the August "
                      "27 iMPACT Jeff is found attacked and stretchered into an ambulance — the "
                      "mystery-attacker storyline TNA is riding toward Bound for Glory."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Edge & Christian and The Dudley Boyz",
                 desc="The three-team rivalry that invented a genre: No Mercy 1999, the first TLC "
                      "at SummerSlam 2000, TLC II at WrestleMania X-Seven on April 1, 2001. Every "
                      "ladder match since works in its shadow, and all six men are read as "
                      "having made each other's Hall of Fame cases."),
            dict(name="CM Punk", slug="cm-punk",
                 desc="The 2009 feud that ended his WWE peak: straight-edge preacher against "
                      "flawed free spirit, with the subtext fully loaded. Punk cashed in on him "
                      "at Extreme Rules, lost the title back at Night of Champions, then won the "
                      "SummerSlam TLC and the loser-leaves-town cage match that wrote Jeff out "
                      "of the company."),
            dict(name="Edge",
                 desc="From TLC partners-in-history to the 2008-09 singles war — Edge took the "
                      "WWE Championship back at the 2009 Royal Rumble with Matt's help, and lost "
                      "the Extreme Rules ladder match that made Jeff a two-belt world champion. "
                      "Nobody's career is more entangled with his."),
            dict(name="Matt Hardy",
                 desc="Brother, partner, and twice the perfect enemy — the 2009 brother-vs-"
                      "brother feud after Matt's Royal Rumble betrayal, and the 2016 Broken-"
                      "universe version in TNA that reinvented both men. As of August 2026 they "
                      "are on the same side, and Matt walking beside the stretcher is the "
                      "emotional engine of the current angle."),
            dict(name="Sting",
                 desc="Linked forever by the worst night — Victory Road, March 13, 2011 — and by "
                      "the better matches around it. Sting's visible fury in the ring that night "
                      "became shorthand for the era of Jeff's career that the 2012 redemption "
                      "reign answered."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Music",
        lead="The enigma part extends well past the ring.",
        rows=[
            dict(when="2003&ndash;", title="Peroxwhy?gen", kind="Music",
                 desc="His band and recording project — original songs have soundtracked his own "
                      "entrances and storylines, including the Broken-era material."),
            dict(when="2016&ndash;2017", title="The Broken Universe / Final Deletion", kind="Television",
                 desc="Matt's creation, Jeff's Brother Nero as co-lead — the Cameron-compound "
                      "cinematic matches that changed how wrestling television gets shot."),
            dict(when="2000s&ndash;", title="WWE and TNA video games", kind="Game",
                 desc="A playable roster fixture across generations of WWE, TNA and AEW games "
                      "during his runs with each company."),
            dict(when="2009", title="Jeff Hardy: My Life, My Rules", kind="Video",
                 desc="WWE's documentary treatment of the first singles peak, art projects and "
                      "dirt-bike tracks included."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The marks, the milestones and the caveats, stated plainly.",
        stats=[
            ("6",  "World titles"),
            ("10", "WWE tag reigns"),
            ("2",  "Companies' tag belts at once"),
        ],
        rows=[
            dict(name="Six world championships across WWE and TNA",
                 sub="The WWE Championship (Armageddon 2008), two World Heavyweight Championships "
                     "(2009), and three TNA World Heavyweight Championships (2010-2012)."),
            dict(name="Ten WWE tag team championship reigns with Matt",
                 sub="From the Attitude Era originals through the WrestleMania 33 ladder-match "
                     "return win on April 2, 2017 and the 2019 SmackDown tag reign."),
            dict(name="WWE Grand Slam Champion",
                 sub="Completed April 16, 2018 by beating Jinder Mahal for the United States "
                     "Championship on Raw — added to world, Intercontinental, European, "
                     "Hardcore, Light Heavyweight and tag gold."),
            dict(name="NXT and TNA World Tag Team Champion simultaneously, at 48",
                 sub="October 7-25, 2025, after the winners-take-all Showdown win over DarkState "
                     "— an 18-day, two-company double reign with Matt."),
            dict(name="The TLC/ladder canon",
                 sub="No Mercy 1999, SummerSlam 2000, WrestleMania X-Seven and the 2009 "
                     "SummerSlam TLC — the risk vocabulary of two decades of wrestling traces "
                     "to these matches."),
            dict(name="The comeback that keeps holding",
                 sub="Released in 2003, stopped ninety seconds into a world title match in 2011, "
                     "suspended after a 2022 DUI arrest — and, in 2024-26, a reliable TNA "
                     "main-eventer with a stretcher angle built around how much the audience "
                     "cares. The falls are part of the record; so is the standing back up."),
        ],
        footnote=("Deliberately absent: a career win-loss total, star ratings, AEW rows this "
                  "pass could not date to the day, any guess at the August 27 attacker's "
                  "identity, and any claim that the Hardys currently hold tag gold &mdash; they "
                  "lost the TNA titles at Rebellion on April 11, 2026, and the Nemeths were the "
                  "defending champions on the show where Jeff was written out."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Jeff_Hardy"),
        dict(k="Wikipedia", v="The Hardy Boyz — the 2024-26 TNA/NXT run",
             href="https://en.wikipedia.org/wiki/The_Hardy_Boyz"),
        dict(k="Wikipedia", v="TNA World Tag Team Championship — the Rebellion 2026 title change",
             href="https://en.wikipedia.org/wiki/TNA_World_Tag_Team_Championship"),
        dict(k="Slam Wrestling", v="iMPACT report, Aug 27, 2026 — the ambulance angle",
             href="https://slamwrestling.net/report/tna-impact-results-08-27-2026-debuts-championships-and-statements-made-oh-my/"),
        dict(k="PWTorch", v="iMPACT TV results, Aug 27, 2026",
             href="https://www.pwtorch.com/site/2026/08/27/tna-impact-tv-results-8-27-stone-vs-elegance-elijah-vs-bronson-hartwell-appearance/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="What happened to Jeff Hardy on the August 27, 2026 iMPACT?",
            a="He was found attacked backstage and left the CAA Centre in Brampton, Ontario in an "
              "ambulance, with Matt Hardy at his side &mdash; the latest chapter in TNA&rsquo;s "
              "ongoing mystery-attacker storyline, in which several roster members have been "
              "taken out by an unrevealed assailant. It is an angle, not a legitimate injury, "
              "per the way both Slam Wrestling and PWTorch covered it. The attacker&rsquo;s "
              "identity had not been revealed on-screen or credibly reported as of August 31, "
              "2026, so this page names no suspects; the storyline is building toward Bound for "
              "Glory.",
            q_ld="What happened to Jeff Hardy on the August 27, 2026 episode of TNA iMPACT?",
            a_ld="On the TNA iMPACT episode of August 27, 2026, taped in Brampton, Ontario, Jeff "
                 "Hardy was found attacked as part of TNA's ongoing mystery-attacker storyline "
                 "and was shown being loaded into an ambulance, accompanied by Matt Hardy. It "
                 "was a storyline angle rather than a legitimate injury, and the attacker's "
                 "identity had not been revealed as of August 31, 2026. The storyline is part of "
                 "TNA's build toward Bound for Glory."),
        dict(
            q="Are The Hardys the current TNA World Tag Team Champions?",
            a="No &mdash; and this is the most common out-of-date claim about them. They lost "
              "the titles to The System (Brian Myers and Bear Bronson) at Rebellion in Cleveland "
              "on April 11, 2026, and by the August 27, 2026 iMPACT the champions defending in "
              "the main event were the Nemeths. The Hardys&rsquo; most recent reign ran from the "
              "Slammiversary 2025 ladder match (July 20, 2025) through Rebellion, including a "
              "stretch from October 7&ndash;25, 2025 when they held the NXT Tag Team "
              "Championship at the same time.",
            q_ld="Are The Hardys the current TNA World Tag Team Champions?",
            a_ld="No. The Hardys lost the TNA World Tag Team Championship to The System, Brian "
                 "Myers and Bear Bronson, at Rebellion on April 11, 2026 in Cleveland. As of "
                 "late August 2026 the champions were the Nemeths, who defended the titles on "
                 "the August 27, 2026 iMPACT. The Hardys' previous reign began at Slammiversary "
                 "on July 20, 2025, and for eighteen days in October 2025 they simultaneously "
                 "held the NXT Tag Team Championship."),
        dict(
            q="How many world titles has Jeff Hardy won?",
            a="Six &mdash; the WWE Championship (won in the Armageddon triple threat on December "
              "14, 2008), two World Heavyweight Championships (both in 2009, the first in the "
              "Extreme Rules ladder match against Edge), and three TNA World Heavyweight "
              "Championships (2010, 2011, and the Bound for Glory 2012 win over Austin Aries). "
              "He is also a WWE Grand Slam champion and, with Matt, one of the most decorated "
              "tag wrestlers ever, with ten WWE tag reigns plus TNA, ROH and NXT gold.",
            q_ld="How many world championships has Jeff Hardy won?",
            a_ld="Jeff Hardy has won six world championships: one WWE Championship in 2008, two "
                 "World Heavyweight Championships in 2009, and three TNA World Heavyweight "
                 "Championships between 2010 and 2012. He is also a WWE Grand Slam champion and "
                 "has won ten WWE tag team championship reigns with his brother Matt, plus tag "
                 "titles in TNA, ROH and NXT."),
        dict(
            q="What was Victory Road 2011?",
            a="The lowest public moment of his career: a TNA World Heavyweight Championship "
              "match against Sting on March 13, 2011 that was stopped in roughly ninety seconds "
              "because Hardy was in no condition to perform. Sting improvised the finish, the "
              "company pulled him from television, and Hardy has since discussed the night "
              "openly as rock bottom in his substance-abuse history. The reason it belongs on "
              "this page is the answer to it: the 2012 Bound for Glory title win over Austin "
              "Aries, earned sober, which TNA framed &mdash; accurately &mdash; as a redemption "
              "story.",
            q_ld="What happened at TNA Victory Road 2011 with Jeff Hardy?",
            a_ld="At TNA Victory Road on March 13, 2011, Jeff Hardy's world championship match "
                 "against Sting was stopped after roughly ninety seconds because Hardy was in no "
                 "condition to perform. Sting pinned him with an improvised finish. Hardy has "
                 "spoken openly about the night as the low point of his struggles with substance "
                 "abuse; his 2012 Bound for Glory world title win over Austin Aries, achieved "
                 "after getting sober, is regarded as the completion of his comeback."),
        dict(
            q="Is Jeff Hardy still wrestling in 2026?",
            a="Yes. He turned 49 on August 31, 2026 and is an active member of the TNA roster, "
              "teaming with Matt as The Hardys. The 2024&ndash;26 run has included two TNA tag "
              "title reigns, an NXT tag title reign, and pay-per-view main events; he is "
              "currently central to TNA&rsquo;s mystery-attacker storyline heading into Bound "
              "for Glory, having been written out of the August 27 iMPACT by ambulance.",
            q_ld="Is Jeff Hardy still an active wrestler in 2026?",
            a_ld="Yes. As of August 2026 Jeff Hardy, aged 49, is an active TNA wrestler, teaming "
                 "with his brother Matt as The Hardys. Since returning to TNA in June 2024 they "
                 "have won the TNA World Tag Team Championship twice and the NXT Tag Team "
                 "Championship once. He is currently involved in TNA's mystery-attacker "
                 "storyline heading into Bound for Glory."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Jeffrey Nero Hardy"),
        dict(label="Born", value="August 31, 1977",
             sub="Cameron, North Carolina &middot; turned 49 the day this page was compiled"),
        dict(label="Billed from", value="Cameron, North Carolina"),
        dict(label="Height", value="6&#8242;1&#8243;", sub="185 cm"),
        dict(label="Weight", value="225 lb", sub="102 kg (billed)"),
        dict(label="Debut", value="1993",
             sub="OMEGA, the brothers&rsquo; own promotion; first WWF TV appearances as "
                 "enhancement talent in 1994, at sixteen"),
        dict(label="Trained by", value="Largely self-taught with Matt Hardy",
             sub="through OMEGA, with early WWF polish from the developmental system of the era"),
        dict(label="Signature", value="Swanton Bomb &middot; Twist of Fate &middot; Whisper in "
                                      "the Wind &middot; Poetry in Motion"),
        dict(label="Brand", value="TNA", sub="with Matt as The Hardys; returned June 14, 2024 at "
                                             "Against All Odds"),
        dict(label="Also known as", value="The Charismatic Enigma &middot; Brother Nero &middot; "
                                          "Willow &middot; The Rainbow-Haired Warrior"),
        dict(label="Family", value="Brother of Matt Hardy",
             sub="the longest-running active brother tag team in major-promotion wrestling"),
        dict(label="Status", value="Active — written out by ambulance August 27, 2026",
             sub="mystery-attacker storyline; no championship currently held"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1977-08-31",
    bornplace="Cameron, North Carolina, United States",
    nationality="United States",
    height_cm=185,
    weight_kg=102,
    ld=dict(
        alternateName=["Jeffrey Nero Hardy", "The Charismatic Enigma", "Brother Nero", "Willow",
                       "The Rainbow-Haired Warrior"],
        award=["WWE Championship (1 reign, 2008)",
               "World Heavyweight Championship (2 reigns, 2009)",
               "TNA World Heavyweight Championship (3 reigns)",
               "WWE Intercontinental Championship (5 reigns)",
               "WWE United States Championship (1 reign)",
               "WWF/WWE tag team championships (10 reigns, with Matt Hardy)",
               "TNA World Tag Team Championship (3 reigns, with Matt Hardy)",
               "NXT Tag Team Championship (1 reign, with Matt Hardy)",
               "WWE Grand Slam Champion"],
        knowsAbout=["Professional wrestling", "Ladder matches", "TLC matches", "WWE", "TNA",
                    "AEW", "The Hardy Boyz", "OMEGA promotion", "Music"],
        description="Jeff Hardy, born Jeffrey Nero Hardy in Cameron, North Carolina, is an "
                    "American professional wrestler active in TNA. One half of The Hardys with "
                    "his brother Matt, he helped define the ladder and TLC match era, won six "
                    "world championships across WWE and TNA, and completed WWE's Grand Slam. In "
                    "2025 the Hardys held the TNA and NXT tag team championships simultaneously; "
                    "they lost the TNA titles in April 2026, and in August 2026 Hardy was "
                    "written out of TNA television by ambulance as part of a mystery-attacker "
                    "storyline building toward Bound for Glory.",
        sameAs=["https://en.wikipedia.org/wiki/Jeff_Hardy",
                "https://tnawrestling.com/"],
    ),
)
