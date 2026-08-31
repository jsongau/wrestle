# -*- coding: utf-8 -*-
"""Charlotte Flair - dossier data.

Sources: web research compiled August 31, 2026 - Wikipedia, TheSmackDownHotel,
Cagematch, Fox News, Bleacher Report, Yahoo Sports, Wrestling Inc and WWE.com show
pages, all opened during this pass. Every match row carries a day-precision date
from one of those sources. No career win-loss total is published: none was verified.

Deliberate omissions:
  * No social links - handles were not verified in this pass.
  * No Meltzer ratings are invented for the signature list; where no rating was
    verified, none is printed.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2014-05-29", promo="WWE", landmark=True,
         event="NXT TakeOver", opponent="Natalya",
         stip="Tournament final for the vacant title - her first championship",
         title="NXT Women's Championship"),
    dict(result="W", date="2015-09-20", promo="WWE", landmark=True,
         event="Night of Champions", opponent="Nikki Bella",
         stip="Singles - first main-roster title", title="WWE Divas Championship"),
    dict(result="W", date="2016-04-03", promo="WWE", landmark=True,
         event="WrestleMania 32", opponent="Becky Lynch & Sasha Banks",
         stip="Triple threat - inaugural champion of the new lineage",
         title="WWE Women's Championship"),
    dict(result="W", date="2016-10-30", promo="WWE", landmark=True,
         event="Hell in a Cell", opponent="Sasha Banks",
         stip="First women's Hell in a Cell match and first women's WWE PPV main event",
         title="Raw Women's Championship"),
    dict(result="L", date="2018-10-28", promo="WWE",
         event="Evolution", opponent="Becky Lynch",
         stip="Last Woman Standing - WWE's own 2018 Match of the Year",
         title="SmackDown Women's Championship"),
    dict(result="L", date="2019-04-07", promo="WWE", type="tag", landmark=True,
         event="WrestleMania 35", opponent="Becky Lynch & Ronda Rousey",
         stip="Winner Takes All triple threat - first women's match to main event WrestleMania",
         title="Raw & SmackDown Women's Championships"),
    dict(result="W", date="2020-01-26", promo="WWE", type="tag", landmark=True,
         event="Royal Rumble", opponent="The 2020 women's Royal Rumble field",
         stip="First Royal Rumble win", title=""),
    dict(result="W", date="2025-02-01", promo="WWE", type="tag", landmark=True,
         event="Royal Rumble", opponent="The 2025 women's Royal Rumble field",
         stip="Entered No. 27, last eliminated Roxanne Perez - first woman to win two Rumbles",
         title=""),
    dict(result="L", date="2025-04-19", promo="WWE", landmark=True,
         event="WrestleMania 41 Night 1", opponent="Tiffany Stratton",
         stip="Singles - challenge", title="WWE Women's Championship"),
    dict(result="W", date="2025-08-02", promo="WWE", type="tag", landmark=True,
         event="SummerSlam Night 1", opponent="Raquel Rodriguez & Roxanne Perez",
         stip="With Alexa Bliss - first tag titles as a team",
         title="WWE Women's Tag Team Championship"),
    dict(result="L", date="2025-11-10", promo="WWE", type="tag",
         event="Raw - Boston", opponent="The Kabuki Warriors",
         stip="With Alexa Bliss - the 100-day reign ends after Nia Jax and Lash Legend interfere",
         title="WWE Women's Tag Team Championship"),
    dict(result="L", date="2026-01-31", promo="WWE", type="tag",
         event="Royal Rumble match - Riyadh", opponent="The 2026 women's Royal Rumble field",
         stip="Entered No. 1, lasted over 59 minutes, eliminated by Lash Legend", title=""),
    dict(result="L", date="2026-04-18", promo="WWE", type="tag",
         event="WrestleMania 42 Night 1", opponent="Brie Bella & Paige, The Irresistible Forces, Bayley & Lyra Valkyria",
         stip="Fatal four-way with Alexa Bliss - Paige pinned Bliss",
         title="WWE Women's Tag Team Championship"),
    dict(result="L", date="2026-08-02", promo="WWE", type="tag",
         event="SummerSlam Night 2", opponent="Chelsea Green, Jade Cargill, Tiffany Stratton, Lash Legend",
         stip="Five-way ladder match - Green won", title="Interim WWE Women's Championship"),
    dict(result="W", date="2026-08-07", promo="WWE",
         event="SmackDown", opponent="Jade Cargill",
         stip="Singles - Alexa Bliss and debuting Tatum Paxley neutralised The Baddies", title=""),
]

DATA = dict(
    slug="charlotte-flair",
    name="Charlotte Flair",
    realname="Ashley Elizabeth Fliehr",
    epithet="The Queen",
    hook="Record & Titles",

    meta_desc=("Charlotte Flair, The Queen, is a record 14-time world champion, a two-time Royal "
               "Rumble winner and the first woman to main event a WWE pay-per-view. Full record, "
               "titles, factions, records and career."),
    og_desc=("The Queen: 14 world championships, two Royal Rumble wins, the first women's Hell in a "
             "Cell and the first women's WWE PPV main event. Full record, titles, factions and career."),
    tw_desc="The Queen: 14 world titles, 2 Royal Rumbles, and the first women's WWE PPV main event.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2012",
    height_imp="5&#8242;10&#8243;",
    weight_lb="143",
    world_titles="14",
    vitals_tagline="Bow down to the Queen",
    support_note="Merch &middot; Books &middot; Games",
    sp_items=[
        dict(ic="CF", title="Charlotte Flair Merch", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable across the 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="SN", title="Second Nature", sub="2017 memoir with Ric Flair",
             tag="Read", href="https://en.wikipedia.org/wiki/Charlotte_Flair"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/charlotte-flair"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Queen &middot; Second-generation Flair &middot; Genetically superior",
    hero_tag="Charlotte, North Carolina &middot; <em>NXT &middot; WWE &middot; 2012&ndash;present</em>",
    now_label="NOW",
    now_bold="SmackDown, no championship",
    now_tail=" &middot; beat Jade Cargill on the August 7 SmackDown and runs the Allies of "
             "Convenience with Alexa Bliss and Tatum Paxley while the Cargill feud burns on",
    hstats=[
        dict(value="14",   x=True,  label="World Titles"),
        dict(value="2",    x=True,  label="Royal Rumble Wins"),
        dict(value="2016", x=False, label="First women's PPV main event"),
        dict(value="100",  x=False, label="Day Tag Reign with Bliss"),
    ],
    ghost_link="From WCW's front row at age seven to fourteen world championships",
    vlabel="Est. 2012 &middot; Charlotte, North Carolina",
    mono="CF",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Charlotte Flair</b> is the most decorated women's wrestler WWE has ever produced, and the "
        "one whose milestones the rest of the division is measured against. She is a record "
        "<b>14-time world champion</b>, the inaugural holder of two of the four titles in that count, "
        "the final Divas Champion, a two-time NXT Women's Champion, and the only woman with two Royal "
        "Rumble wins &mdash; 2020 and 2025. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">14</span>'
        '<span class="pull-cap">world championship reigns &mdash; the record her own father&rsquo;s 16 is always compared against</span></span>'
        "With Sasha Banks she main-evented Hell in a Cell on October 30, 2016 &mdash; the first "
        "women's match to main event a WWE pay-per-view and the first women's Hell in a Cell match "
        "&mdash; and she was one third of the first women's match to main event WrestleMania, at "
        "WrestleMania 35 in 2019. The daughter of Ric Flair, she came to wrestling late, at twenty-six, "
        "and passed nearly everyone anyway.",

        "The number that follows her around needs its arithmetic shown. The <b>14</b> counts world "
        "titles only: one Divas Championship, six reigns in the Raw Women's / WWE Women's lineage and "
        "seven in the SmackDown Women's / Women's World lineage. It does <i>not</i> include her two NXT "
        "Women's Championships or her two Women's Tag Team Championships &mdash; add those and "
        "TheSmackDownHotel counts <b>18 total championships</b>, which is where the bigger figures in "
        "circulation come from. And she has <b>not</b> passed Ric Flair's recognised 16 world titles: "
        "14 is two short, a gap WWE's own commentary keeps alive on purpose. One more count worth "
        "fixing: she is 'the first woman to main event a WWE pay-per-view' with Sasha Banks in 2016, "
        "but the WrestleMania main-event first, in 2019, is shared three ways with Becky Lynch and "
        "Ronda Rousey &mdash; it was a triple threat, and the milestone belongs to the match.",

        "She was born Ashley Elizabeth Fliehr on April 5, 1986 in Charlotte, North Carolina, appeared "
        "on WCW television as a child, and signed with WWE on May 17, 2012 with no wrestling "
        "background beyond her surname. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">2</span>'
        '<span class="pull-cap">Royal Rumble wins, 2020 and 2025 &mdash; the first woman ever to win more than one</span></span>'
        "Trained in NXT partly by Sara Del Rey, she won the NXT Women's Championship from Natalya at "
        "the first TakeOver on May 29, 2014, took the Divas Championship from Nikki Bella in September "
        "2015, and became the inaugural WWE Women's Champion in the WrestleMania 32 triple threat on "
        "April 3, 2016 when the Divas belt was retired. The Four Horsewomen framing &mdash; Flair, "
        "Lynch, Banks, Bayley &mdash; was press shorthand rather than a booked stable, but the four of "
        "them genuinely did rebuild the division, and Flair collected more of its firsts than anyone.",

        "The current chapter is stranger than the resume. She returned from a year off at the 2025 "
        "Royal Rumble and won it from No. 27, lost to Tiffany Stratton at WrestleMania 41, then "
        "reinvented as half of the <b>Allies of Convenience</b> with Alexa Bliss &mdash; Women's Tag "
        "Team Champions for 100 days from SummerSlam 2025 until the Kabuki Warriors took the belts on "
        "November 10. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">100</span>'
        '<span class="pull-cap">days as Women&rsquo;s Tag Team Champions with Alexa Bliss, August 2 to November 10, 2025</span></span>'
        "In 2026 she entered the Royal Rumble at No. 1 and lasted over 59 minutes, lost the "
        "WrestleMania 42 tag title four-way when Paige pinned Bliss, and then inserted herself into "
        "the WWE Women's Championship picture from the outside: at Clash in Italy on May 31 she came "
        "out of the crowd, unasked and unexplained, to help Rhea Ripley beat Jade Cargill. Cargill "
        "has taken it personally ever since. Flair attacked her on the July 31 SmackDown, lost the "
        "SummerSlam interim-title ladder match on August 2, and beat Cargill one-on-one on the August "
        "7 SmackDown after Bliss and the debuting Tatum Paxley cancelled out The Baddies. That feud, "
        "and whatever she wants from Ripley's title, is where she stands as of August 31, 2026.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Highlight set",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("14&times;", "World titles"),
            ("7&times;",  "SmackDown / Women's World"),
            ("6&times;",  "Raw / WWE Women's"),
            ("2&times;",  "Royal Rumbles"),
            ("2&times;",  "NXT Women's"),
            ("2&times;",  "Women's Tag Team"),
        ],
        lead=("Fifteen documented bouts - a highlight subset spanning the first NXT TakeOver to the "
              "August 7, 2026 SmackDown, not a career count. No career win-loss total is published, "
              "because none was verified in this pass. The 2026 rows are the live story: the No. 1 "
              "Rumble entry, the WrestleMania 42 tag four-way, the SummerSlam ladder match and the "
              "Jade Cargill singles win. Filter by match type, tap any column header to sort, and "
              "turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("Three bouts the reputation rests on. No star ratings are printed here because "
                    "none were verified in this pass - these are selected for what they changed, not "
                    "for a number."),
    signature=[
        dict(rating="—", event="Hell in a Cell 2016", opponent="Sasha Banks",
             stip="First women's Hell in a Cell and first women's WWE PPV main event"),
        dict(rating="—", event="WrestleMania 35", opponent="Becky Lynch & Ronda Rousey",
             stip="Winner Takes All triple threat — first women's WrestleMania main event"),
        dict(rating="—", event="Evolution 2018", opponent="Becky Lynch",
             stip="Last Woman Standing — WWE's own 2018 Match of the Year"),
    ],
    signature_count_word="three",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("14&times;", "World title reigns"),
            ("18",        "Total championships"),
            ("4th",       "Women's Grand Slam"),
            ("5th",       "Women's Triple Crown"),
        ],
        lead=("Fourteen world championships across four belts, two of which she was the first ever to "
              "hold and one of which she was the last. The count excludes NXT and the tag titles - "
              "which is exactly where the inflated versions of the number come from."),
        rows=[
            dict(ic="S", name="SmackDown Women's Championship / Women's World Championship", count="7",
                 sub="The lineage she has won most - seven reigns between 2017 and 2023, including the "
                     "title's first defence era on the brand. Renamed the Women's World Championship "
                     "in June 2023."),
            dict(ic="R", name="WWE Women's Championship / Raw Women's Championship", count="6",
                 sub="Inaugural champion, won in the WrestleMania 32 triple threat over Becky Lynch and "
                     "Sasha Banks on April 3, 2016, when the Divas Championship was retired. Six reigns "
                     "in the lineage."),
            dict(ic="D", name="WWE Divas Championship", count="1",
                 sub="Won from Nikki Bella at Night of Champions on September 20, 2015 - the belt was "
                     "retired with her holding it, making her the final Divas Champion."),
            dict(ic="N", name="NXT Women's Championship", count="2",
                 sub="First reign from May 29, 2014, beating Natalya in a tournament final at the first "
                     "TakeOver; a second reign followed in 2020, making her the first woman to hold NXT "
                     "gold after main-roster stardom."),
            dict(ic="T", name="WWE Women's Tag Team Championship", count="2",
                 sub="2023 with Asuka; 2025 with Alexa Bliss - won at SummerSlam Night 1 on August 2, "
                     "lost to The Kabuki Warriors on November 10 after 100 days, when Nia Jax and Lash "
                     "Legend interfered."),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="One press label that was never booked, one 2015 relic, and the 2025-26 alliance that is "
             "her current act.",
        cards=[
            dict(era="NXT &middot; 2013&ndash;15 &middot; press framing, not a booked unit",
                 name="The Four Horsewomen",
                 members="Charlotte Flair, Becky Lynch, Sasha Banks, Bayley",
                 desc="Never an on-screen alliance - a media and fan label for the four women who came "
                      "up through NXT together, deliberately echoing her father's Four Horsemen. What "
                      "it describes is real: the division was rebuilt around these four from 2015, and "
                      "Flair took more of the resulting firsts than anyone."),
            dict(era="WWE &middot; 2015",
                 name="Team PCB",
                 members="Paige, Charlotte Flair, Becky Lynch",
                 desc="Formed during the 2015 Divas Revolution three-way faction war. The feud won the "
                      "Wrestling Observer Newsletter's Worst Feud of the Year award for 2015, which "
                      "remains the honest verdict on the era it came from."),
            dict(era="WWE &middot; 2025&ndash;present",
                 name="Allies of Convenience",
                 members="Charlotte Flair, Alexa Bliss, Tatum Paxley (from August 2026)",
                 desc="Started in June 2025 as a reluctant Bliss pitch and became the most productive "
                      "partnership of her late career: Women's Tag Team Champions for 100 days from "
                      "SummerSlam 2025, then joint Rumble entrants at No. 1 and No. 2 in 2026 - where "
                      "Flair accidentally eliminated Bliss - and a WrestleMania 42 four-way together. "
                      "Tatum Paxley attached herself to the pair on her August 2026 call-up, running "
                      "interference in the Jade Cargill match on August 7 and beating Cargill's ally "
                      "Michin in her SmackDown in-ring debut on August 28."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One ring name for the whole career - the reinventions happened inside it.",
        cards=[
            dict(mono="NX", era="NXT &middot; 2012&ndash;15", name="The prodigy with the surname",
                 desc="Signed May 17, 2012 at twenty-six with no wrestling background, initially worked "
                      "as a genetically-gifted athlete trading on the Flair name - and won the NXT "
                      "Women's Championship within two years."),
            dict(mono="Q", era="WWE &middot; 2016&ndash;present", name="The Queen",
                 desc="The defining character: entitled, imperious, robe-wearing, backed by the Figure "
                      "Eight. Built through the 2016 heel run with her father at ringside, and durable "
                      "enough to survive a dozen face and heel turns since."),
            dict(mono="TG", era="WWE &middot; 2025", name="Top Girl",
                 desc="The post-Rumble 2025 heel edge - bragging about lineage and calling herself the "
                      "Top Girl on the way to WrestleMania 41, where Tiffany Stratton beat her anyway. "
                      "It burned out within months and the Bliss alliance replaced it."),
            dict(mono="AC", era="WWE &middot; 2025&ndash;26", name="Ally of Convenience",
                 desc="The current register: a veteran who teams with Alexa Bliss on explicitly "
                      "transactional terms, and whose unexplained interventions - the Clash in Italy "
                      "assist for Rhea Ripley on May 31, 2026 chief among them - keep her motives the "
                      "open question of the SmackDown women's division."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="From WCW's front row as a child to the record 14, with the current Cargill feud live.",
        rows=[
            dict(year="2012", title="Signs with WWE at twenty-six",
                 desc="Signs May 17, 2012, trains in NXT under Sara Del Rey among others, and debuts on "
                      "NXT television on July 17, 2013 against Bayley."),
            dict(year="2014", title="NXT Women's Champion",
                 desc="Beats Natalya in a tournament final at the first NXT TakeOver on May 29, 2014 "
                      "for the vacant title - her first championship."),
            dict(year="2015", title="Main roster, Divas Champion",
                 desc="Called up in the Divas Revolution, wins the Divas Championship from Nikki Bella "
                      "at Night of Champions on September 20, 2015. She would be the belt's last holder."),
            dict(year="2016", title="Two firsts in one year",
                 desc="Becomes inaugural WWE Women's Champion in the WrestleMania 32 triple threat on "
                      "April 3, then main events Hell in a Cell against Sasha Banks on October 30 - the "
                      "first women's Hell in a Cell match and first women's WWE PPV main event."),
            dict(year="2019", title="The WrestleMania 35 main event",
                 desc="One third of the first women's match to main event WrestleMania, the Winner "
                      "Takes All triple threat Becky Lynch won on April 7."),
            dict(year="2020", title="First Royal Rumble win",
                 desc="Wins the women's Royal Rumble on January 26, 2020."),
            dict(year="2025", title="Returns, wins a second Rumble, turns, then teams",
                 desc="Returns from over a year away at the Royal Rumble on February 1 and wins from "
                      "No. 27 - the first woman with two Rumble wins. Loses to Tiffany Stratton at "
                      "WrestleMania 41 on April 19, runs the Top Girl heel turn, then goes face and "
                      "wins the Women's Tag Team Championship with Alexa Bliss at SummerSlam on August "
                      "2. The reign ends at 100 days on November 10."),
            dict(year="2026", title="No. 1 in the Rumble, the Italy intervention, the Cargill feud",
                 desc="Lasts over 59 minutes from No. 1 in the January 31 Rumble; loses the "
                      "WrestleMania 42 tag four-way on April 18; helps Rhea Ripley retain against Jade "
                      "Cargill at Clash in Italy on May 31 without explanation; loses the SummerSlam "
                      "interim-title ladder match on August 2; beats Cargill on the August 7 SmackDown."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who she went to war with.",
        cards=[
            dict(name="Becky Lynch", slug="becky-lynch",
                 desc="The spine of both careers: PCB teammates, then the SummerSlam 2018 turn that "
                      "made Lynch The Man at Flair's expense, the Evolution Last Woman Standing match "
                      "on October 28, 2018, the WrestleMania 35 triple threat, and Money in the Bank "
                      "2019, where Flair ended the Becky Two Belts run. No opponent has defined her "
                      "public standing more."),
            dict(name="Sasha Banks",
                 desc="The 2016 series that carried the division's biggest firsts - the WrestleMania 32 "
                      "triple threat, a summer of title trading, and the October 30, 2016 Hell in a "
                      "Cell main event, the first women's match to headline a WWE pay-per-view."),
            dict(name="Tiffany Stratton", slug="tiffany-stratton",
                 desc="The generational checkpoint: Stratton retained the WWE Women's Championship over "
                      "her at WrestleMania 41 Night 1 on April 19, 2025 - the veteran putting over the "
                      "champion of the next class, and the loss that triggered the Top Girl heel "
                      "phase."),
            dict(name="Jade Cargill", slug="jade-cargill",
                 desc="The live feud. It started at Clash in Italy on May 31, 2026, when Flair came "
                      "through the crowd to break up Cargill's pin and help Rhea Ripley retain - "
                      "unexplained then, unexplained still. Cargill and The Baddies answered through "
                      "the summer; Flair attacked Cargill on the July 31 SmackDown, both lost the "
                      "SummerSlam ladder match, and Flair won the first singles meeting on August 7 "
                      "after Alexa Bliss and Tatum Paxley neutralised Michin and B-Fab."),
            dict(name="Rhea Ripley",
                 desc="The unfinished thread inside the Cargill story. Flair's Italy save earned a long "
                      "stare-down with the champion rather than a thank-you, and Fox News read it as "
                      "Flair positioning for a title shot. Ripley's knee injury and surgery froze that "
                      "question - she is projected back around the Royal Rumble."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Books",
        lead="A shorter list than the fame suggests - only what was verified is here.",
        rows=[
            dict(when="2017", title="Second Nature", kind="Book",
                 desc="Joint memoir with Ric Flair, published 2017 - her half covers the late start, "
                      "the death of her brother Reid, and the first NXT years."),
            dict(when="2016&ndash;", title="WWE 2K series", kind="Game",
                 desc="A playable roster fixture across the modern WWE 2K series. Her exact debut "
                      "entry was not verified in this pass, so no year is claimed for it."),
            dict(when="1993", title="WCW television, age seven", kind="TV",
                 desc="On camera in her father's corner as a child at Starrcade-era WCW shows - the "
                      "earliest footage of her in a wrestling ring predates her career by two decades."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated with their arithmetic shown - including the counts that get "
             "inflated and the one that has not been broken.",
        stats=[
            ("14",  "World title reigns"),
            ("2",   "Royal Rumble wins"),
            ("18",  "Total championships"),
        ],
        rows=[
            dict(name="Record 14 world championship reigns",
                 sub="One Divas, six Raw Women's / WWE Women's, seven SmackDown Women's / Women's "
                     "World. The most of any woman in WWE history. It does not include her two NXT "
                     "Women's or two Women's Tag Team reigns - TheSmackDownHotel's 18-championship "
                     "total does."),
            dict(name="Has not passed Ric Flair's 16",
                 sub="Worth stating because it is routinely blurred: her recognised world title count "
                     "is 14, two short of her father's recognised 16. Versions that put her ahead are "
                     "adding non-world belts to one side of the ledger only."),
            dict(name="First woman to main event a WWE pay-per-view",
                 sub="Hell in a Cell, October 30, 2016, against Sasha Banks at TD Garden - also the "
                     "first women's Hell in a Cell match. Shared with Banks, and two and a half years "
                     "before the WrestleMania 35 main event."),
            dict(name="Part of the first women's WrestleMania main event - shared three ways",
                 sub="WrestleMania 35, April 7, 2019, the Winner Takes All triple threat with Becky "
                     "Lynch and Ronda Rousey. The milestone belongs to the match, not to one woman."),
            dict(name="First woman to win two Royal Rumbles",
                 sub="2020, and again on February 1, 2025 from the No. 27 spot after more than a year "
                     "out injured. In 2026 she entered at No. 1 and lasted over 59 minutes."),
            dict(name="Inaugural champion twice over, and a final champion once",
                 sub="First WWE Women's Champion (2016) and first champion of the modern women's "
                     "division era it started; last-ever Divas Champion when that belt was retired at "
                     "WrestleMania 32. Fourth Women's Grand Slam and fifth Women's Triple Crown "
                     "champion per Wikipedia."),
        ],
        footnote=("No career win-loss total appears on this page because none was verified. Social "
                  "handles are omitted for the same reason. Her billed weight of 143 lb is "
                  "TheSmackDownHotel's figure; WWE.com does not publish one."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Charlotte_Flair"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/charlotte-flair"),
        dict(k="SmackDown Hotel", v="Profile and championship history",
             href="https://www.thesmackdownhotel.com/wrestlers/charlotte-flair"),
        dict(k="SmackDown Hotel", v="Women's Tag Team title history, 2025-26",
             href="https://www.thesmackdownhotel.com/title-history/wwe/wwe-women-s-tag-team-championship"),
        dict(k="Fox News", v="Clash in Italy - the unexplained save for Rhea Ripley",
             href="https://www.foxnews.com/sports/rhea-ripley-curiously-gets-help-charlotte-flair-retain-womens-title-wwe-clash-italy"),
        dict(k="Cagematch", v="Flair vs. Cargill, SmackDown, August 7, 2026",
             href="https://www.cagematch.net/?id=111&nr=144741"),
        dict(k="Bleacher Report", v="SummerSlam 2026 interim-title ladder match",
             href="https://bleacherreport.com/articles/25460215-chelsea-green-wins-interim-wwe-womens-title-ladder-match-summerslam-after-ripleys-injury"),
        dict(k="Yahoo Sports", v="WrestleMania 42 full results",
             href="https://sports.yahoo.com/articles/wrestlemania-42-full-winners-list-042619263.html"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="How many championships has Charlotte Flair won?",
            a="Fourteen <b>world</b> championships &mdash; one Divas, six in the Raw Women&rsquo;s / "
              "WWE Women&rsquo;s lineage, seven in the SmackDown Women&rsquo;s / Women&rsquo;s World "
              "lineage &mdash; which is the record. Add her two NXT Women&rsquo;s Championships and "
              "two Women&rsquo;s Tag Team Championships and TheSmackDownHotel counts 18 total. The "
              "figures in between usually come from mixing the two ledgers. She has <i>not</i> passed "
              "Ric Flair&rsquo;s recognised 16 world titles.",
            q_ld="How many championships has Charlotte Flair won?",
            a_ld="Charlotte Flair has won a record 14 world championships in WWE: one Divas "
                 "Championship, six reigns in the Raw Women's and WWE Women's Championship lineage, "
                 "and seven reigns in the SmackDown Women's and Women's World Championship lineage. "
                 "Counting her two NXT Women's Championships and two WWE Women's Tag Team "
                 "Championships as well, she has 18 total championships. She has not surpassed Ric "
                 "Flair's recognised 16 world championships."),
        dict(
            q="Was Charlotte Flair the first woman to main event a WWE pay-per-view?",
            a="Yes, jointly with Sasha Banks &mdash; they closed Hell in a Cell on <b>October 30, "
              "2016</b> in the first women's Hell in a Cell match, which was also the first women's "
              "match to main event a WWE pay-per-view. The WrestleMania version of the first came two "
              "and a half years later, at WrestleMania 35 on April 7, 2019, and is shared three ways "
              "with Becky Lynch and Ronda Rousey, because it was a triple threat.",
            q_ld="Was Charlotte Flair the first woman to main event a WWE pay-per-view?",
            a_ld="Yes, jointly with Sasha Banks. Charlotte Flair and Sasha Banks main-evented Hell in "
                 "a Cell on October 30, 2016 in the first women's Hell in a Cell match, which was the "
                 "first women's match to main event a WWE pay-per-view. The first women's WrestleMania "
                 "main event came at WrestleMania 35 on April 7, 2019 and is shared with Becky Lynch "
                 "and Ronda Rousey."),
        dict(
            q="Is Charlotte Flair a champion right now, and what is she doing?",
            a="No. As of August 31, 2026 she holds no title. Her last championship was the "
              "Women&rsquo;s Tag Team Championship with Alexa Bliss, lost to The Kabuki Warriors on "
              "November 10, 2025 after 100 days. She is on <b>SmackDown</b>, working with Bliss and "
              "Tatum Paxley as the Allies of Convenience, and in a live feud with Jade Cargill that "
              "began when Flair helped Rhea Ripley retain against Cargill at Clash in Italy on May 31, "
              "2026 &mdash; a save she has never explained. She beat Cargill one-on-one on the August "
              "7 SmackDown.",
            q_ld="Is Charlotte Flair a champion right now?",
            a_ld="No. As of August 31, 2026 Charlotte Flair holds no championship. Her most recent "
                 "title was the WWE Women's Tag Team Championship with Alexa Bliss, lost to The Kabuki "
                 "Warriors on November 10, 2025 after 100 days. She is on SmackDown in an alliance "
                 "with Alexa Bliss and Tatum Paxley and is feuding with Jade Cargill, whom she "
                 "defeated on the August 7, 2026 SmackDown."),
        dict(
            q="Why did Charlotte Flair help Rhea Ripley at Clash in Italy?",
            a="No on-screen explanation has been given. At Clash in Italy on <b>May 31, 2026</b> she "
              "came through the crowd during the WWE Women&rsquo;s Championship match, neutralised "
              "Jade Cargill&rsquo;s allies B-Fab and Michin, broke up a Cargill pin, and Ripley "
              "retained with the Riptide. Flair and Ripley then exchanged a long stare rather than an "
              "alliance, and Fox News read the whole thing as Flair positioning herself for a title "
              "shot &mdash; a question Ripley&rsquo;s knee surgery has left open.",
            q_ld="Why did Charlotte Flair help Rhea Ripley retain at Clash in Italy 2026?",
            a_ld="No explanation has been given on screen. At Clash in Italy on May 31, 2026, "
                 "Charlotte Flair emerged from the crowd during the WWE Women's Championship match, "
                 "neutralised Jade Cargill's allies B-Fab and Michin, and broke up a pin, after which "
                 "Rhea Ripley retained. Flair and Ripley exchanged a stare-down afterward, and "
                 "reporting characterised the intervention as Flair positioning herself for a future "
                 "championship match, a question left open by Ripley's knee surgery."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Ashley Elizabeth Fliehr"),
        dict(label="Born", value="April 5, 1986", sub="Charlotte, North Carolina &middot; age 40"),
        dict(label="Billed from", value="Charlotte, North Carolina"),
        dict(label="Height", value="5&#8242;10&#8243;", sub="178 cm"),
        dict(label="Weight", value="143 lb", sub="65 kg per SmackDown Hotel &middot; WWE.com lists none"),
        dict(label="Signed", value="May 17, 2012", sub="NXT televised debut July 17, 2013, vs. Bayley"),
        dict(label="Trained by", value="WWE Performance Center", sub="including Sara Del Rey"),
        dict(label="Family", value="Daughter of Ric Flair",
             sub="his recognised 16 world titles remain two ahead of her 14"),
        dict(label="Finishers", value="Figure Eight &middot; Natural Selection"),
        dict(label="Brand", value="SmackDown"),
        dict(label="Allies", value="Alexa Bliss &middot; Tatum Paxley",
             sub="Allies of Convenience, 2025&ndash;present"),
        dict(label="Also known as", value="The Queen &middot; Top Girl"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1986-04-05",
    bornplace="Charlotte, North Carolina, United States",
    nationality="United States",
    height_cm=178,
    weight_kg=65,
    ld=dict(
        alternateName=["Ashley Elizabeth Fliehr", "The Queen", "Charlotte"],
        award=["WWE Divas Championship (1 reign, final champion)",
               "WWE Women's Championship / Raw Women's Championship (6 reigns, inaugural champion)",
               "SmackDown Women's Championship / Women's World Championship (7 reigns)",
               "NXT Women's Championship (2 reigns)",
               "WWE Women's Tag Team Championship (2 reigns, with Asuka and with Alexa Bliss)",
               "Royal Rumble winner (2020, 2025 - first woman to win twice)",
               "WWE Women's Grand Slam Champion (fourth)",
               "WWE Women's Triple Crown Champion (fifth)",
               "Pro Wrestling Illustrated Woman of the Year (2016)"],
        knowsAbout=["Professional wrestling", "WWE", "Women's professional wrestling",
                    "Championship wrestling", "The Flair wrestling family"],
        description="Charlotte Flair, born Ashley Elizabeth Fliehr, is an American professional "
                    "wrestler signed to WWE and the daughter of Ric Flair. She is a record 14-time "
                    "world champion in WWE, the inaugural WWE Women's Champion, the final Divas "
                    "Champion, a two-time NXT Women's Champion and the first woman to win two Royal "
                    "Rumble matches, in 2020 and 2025. With Sasha Banks she main-evented Hell in a "
                    "Cell in October 2016, the first women's match to main event a WWE pay-per-view.",
        sameAs=["https://en.wikipedia.org/wiki/Charlotte_Flair",
                "https://www.wwe.com/superstars/charlotte-flair"],
    ),
)
