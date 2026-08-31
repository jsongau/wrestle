# -*- coding: utf-8 -*-
"""Jade Cargill - dossier data.

Sources: web research compiled August 31, 2026 - Wikipedia, TheSmackDownHotel,
Sports Illustrated, Fox News, Cagematch, Wrestling Inc, Yahoo Sports and WWE.com
show pages, all opened during this pass. Every match row carries a day-precision
date from one of those sources.

Deliberate omissions:
  * No career win-loss total - none was verified beyond the AEW streak figure.
  * No social links - handles were not verified in this pass.
  * Her birthplace is printed as a live conflict: TheSmackDownHotel says Vero
    Beach, Florida; a Wikipedia read returned Gifford, Florida. Vero Beach is used
    in the structured data, and the conflict is flagged in the rail.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2021-03-03", promo="AEW", landmark=True,
         event="Dynamite: The Crossroads", opponent="Cody Rhodes & Red Velvet",
         stip="First match - tagging with Shaquille O'Neal", title="", type="tag"),
    dict(result="W", date="2022-01-05", promo="AEW", landmark=True,
         event="Dynamite", opponent="Ruby Soho",
         stip="Tournament final - inaugural champion", title="AEW TBS Championship"),
    dict(result="L", date="2023-05-28", promo="AEW", landmark=True,
         event="Double or Nothing", opponent="Kris Statlander",
         stip="Singles - the 508-day reign and the streak end in under a minute",
         title="AEW TBS Championship"),
    dict(result="L", date="2024-01-27", promo="WWE", type="tag",
         event="Royal Rumble", opponent="The 2024 women's Royal Rumble field",
         stip="WWE in-ring debut, entered No. 28", title=""),
    dict(result="W", date="2024-05-04", promo="WWE", type="tag", landmark=True,
         event="Backlash - Lyon", opponent="The Kabuki Warriors",
         stip="With Bianca Belair - first WWE gold",
         title="WWE Women's Tag Team Championship"),
    dict(result="L", date="2024-06-15", promo="WWE", type="tag",
         event="Clash at the Castle: Scotland", opponent="The Unholy Union",
         stip="With Bianca Belair - titles lost", title="WWE Women's Tag Team Championship"),
    dict(result="W", date="2024-08-31", promo="WWE", type="tag",
         event="Bash in Berlin", opponent="The Unholy Union",
         stip="With Bianca Belair - titles regained", title="WWE Women's Tag Team Championship"),
    dict(result="W", date="2025-04-19", promo="WWE", landmark=True,
         event="WrestleMania 41 Night 1", opponent="Naomi",
         stip="Singles - the payoff to the five-month attack mystery", title=""),
    dict(result="W", date="2025-06-28", promo="WWE", landmark=True,
         event="Night of Champions - Riyadh", opponent="Asuka",
         stip="Queen of the Ring final", title=""),
    dict(result="W", date="2025-07-13", promo="WWE",
         event="Evolution", opponent="Naomi",
         stip="No holds barred - the feud's blowoff", title=""),
    dict(result="L", date="2025-08-02", promo="WWE",
         event="SummerSlam Night 1", opponent="Tiffany Stratton",
         stip="Singles - the Queen's title shot comes up short", title="WWE Women's Championship"),
    dict(result="W", date="2025-11-01", promo="WWE", landmark=True,
         event="Saturday Night's Main Event XLI - Salt Lake City", opponent="Tiffany Stratton",
         stip="Singles - first world title, won as a heel working the injured knee",
         title="WWE Women's Championship"),
    dict(result="L", date="2026-04-19", promo="WWE", landmark=True,
         event="WrestleMania 42 Night 2", opponent="Rhea Ripley",
         stip="Singles - the 169-day reign ends after Iyo Sky's interference",
         title="WWE Women's Championship"),
    dict(result="W", date="2026-05-23", promo="WWE", type="tag",
         event="Saturday Night's Main Event XLIV", opponent="Team Rhea Ripley",
         stip="Six-woman tag with The Baddies - Cargill pins the champion", title=""),
    dict(result="L", date="2026-05-31", promo="WWE", landmark=True,
         event="Clash in Italy - Turin", opponent="Rhea Ripley",
         stip="Singles - Charlotte Flair's unexplained interference turns it",
         title="WWE Women's Championship"),
    dict(result="L", date="2026-08-02", promo="WWE", type="tag",
         event="SummerSlam Night 2", opponent="Chelsea Green, Charlotte Flair, Tiffany Stratton, Lash Legend",
         stip="Five-way ladder match - Green won", title="Interim WWE Women's Championship"),
    dict(result="L", date="2026-08-07", promo="WWE",
         event="SmackDown", opponent="Charlotte Flair",
         stip="Singles - Alexa Bliss and Tatum Paxley neutralise The Baddies", title=""),
]

DATA = dict(
    slug="jade-cargill",
    name="Jade Cargill",
    realname="Jade Cargill",
    epithet="The Storm",
    hook="Record & Titles",

    meta_desc=("Jade Cargill was the inaugural AEW TBS Champion for 508 days, ran a 60-match "
               "winning streak, and won the WWE Women's Championship in 2025. Full record, titles, "
               "factions and career."),
    og_desc=("The Storm: a 508-day reign as inaugural TBS Champion, 60 straight wins, the 2025 "
             "Queen of the Ring, and a WWE Women's Championship. Full record, titles and career."),
    tw_desc="The Storm: 508 days as inaugural TBS Champion, 60 straight wins, WWE Women's Champion.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2020",
    height_imp="5&#8242;10&#8243;",
    weight_lb="160",
    world_titles="1",
    vitals_tagline="A storm is coming",
    support_note="Merch &middot; Games &middot; Watch",
    sp_items=[
        dict(ic="JC", title="Jade Cargill Merch", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable in the current 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="TX", title="Texas Smoke", sub="Co-owner, Women's Pro Fastpitch",
             tag="Visit", href="https://en.wikipedia.org/wiki/Jade_Cargill"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/jade-cargill"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Inaugural TBS Champion &middot; Queen of the Ring 2025 &middot; The Baddies",
    hero_tag="Vero Beach, Florida &middot; <em>AEW &middot; WWE &middot; 2020&ndash;present</em>",
    now_label="NOW",
    now_bold="SmackDown, no championship",
    now_tail=" &middot; lost the first singles meeting with Charlotte Flair on August 7 and is "
             "running The Baddies at her in response, with the feud still open",
    hstats=[
        dict(value="508",  x=False, label="Day TBS Reign"),
        dict(value="60",   x=False, label="Match Win Streak"),
        dict(value="1",    x=True,  label="WWE Women's Title"),
        dict(value="2025", x=False, label="Queen of the Ring"),
    ],
    ghost_link="From college forward to inaugural champion in fourteen months of wrestling",
    vlabel="Est. 2020 &middot; Vero Beach, Florida",
    mono="JC",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Jade Cargill</b> has spent her entire six-year career being booked like a special "
        "attraction, because physically that is what she is: a 5&#8242;10&#8243; former college "
        "basketball forward who looks like the promotional artwork. In AEW she was the "
        "<b>inaugural TBS Champion</b> and held the belt for <b>508 days</b> &mdash; the entirety "
        "of the title's first era &mdash; across a winning streak of roughly sixty matches. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">508</span>'
        '<span class="pull-cap">days as the inaugural AEW TBS Champion, January 5, 2022 to May 28, 2023</span></span>'
        "In WWE she has won the Women's Tag Team Championship twice with Bianca Belair, the 2025 "
        "Queen of the Ring, and &mdash; on November 1, 2025, off the biggest heel turn of her "
        "career &mdash; the <b>WWE Women's Championship</b>, her first world title anywhere. She "
        "held it 169 days, into WrestleMania 42.",

        "The line that follows her from AEW &mdash; &ldquo;undefeated&rdquo; &mdash; needs its "
        "edges drawn. She was not undefeated in AEW: <b>Kris Statlander</b> beat her twice in 2023, "
        "first at Double or Nothing on May 28, taking the TBS Championship <b>in under a minute</b>, "
        "and again on the September 15 Rampage in Cargill's final AEW match. What is true is "
        "narrower and still remarkable: a winning streak of around <b>60 matches</b> spanning her "
        "March 2021 debut through the whole 508-day reign. And a second precision point on the WWE "
        "title win: the SI-reported reign length she ended was Tiffany Stratton's &mdash; 301 days "
        "by their count, 302 by Wikipedia's &mdash; while her own reign ran <b>169 days</b>, "
        "November 1, 2025 to April 19, 2026, ending when Rhea Ripley beat her at WrestleMania 42 "
        "with Iyo Sky lending the assist.",

        "She was born June 3, 1992 and played forward for Jacksonville University's basketball team "
        "from 2010 to 2014, then worked as a child psychologist with foster children until 2019 "
        "&mdash; wrestling is her second professional life. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">60</span>'
        '<span class="pull-cap">consecutive wins to open the AEW run &mdash; the streak Kris Statlander ended, twice</span></span>'
        "She debuted on the November 11, 2020 Dynamite interrupting Cody Rhodes, wrestled her first "
        "match on March 3, 2021 tagging with Shaquille O'Neal, and won the TBS tournament final "
        "over Ruby Soho on January 5, 2022, fourteen months into wrestling. WWE signed her in "
        "September 2023; the Royal Rumble in-ring debut came that January, the Belair tag "
        "partnership through 2024, and then the mystery-attacker angle that wrote her off "
        "television from November 2024 until Elimination Chamber 2025 &mdash; resolved into the "
        "Naomi feud she won at WrestleMania 41 and again, no holds barred, at Evolution.",

        "The 2026 shape is a feud she did not pick. After the WrestleMania 42 loss she rebuilt "
        "around <b>The Baddies</b> &mdash; her unit with Michin and B-Fab &mdash; and pinned "
        "champion Rhea Ripley in a six-woman tag at Saturday Night's Main Event on May 23 to force "
        "the Clash in Italy rematch on May 31. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">169</span>'
        '<span class="pull-cap">days as WWE Women&rsquo;s Champion, November 1, 2025 to April 19, 2026</span></span>'
        "She lost it when <b>Charlotte Flair</b> came out of the crowd, unexplained, to neutralise "
        "The Baddies and break up her pin &mdash; and everything since has flowed from that: the "
        "backstage brawls through July, the July 31 SmackDown attack by Flair, the SummerSlam "
        "interim-title ladder match both women lost on August 2, and the first one-on-one meeting "
        "on August 7, which Flair won after Alexa Bliss and the debuting Tatum Paxley cancelled out "
        "Michin and B-Fab. As of August 31, 2026 she is title-less on SmackDown, the feud is open, "
        "and she has not stopped being the division's most obviously protected long-term project.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Highlight set",
        promo_order=["AEW", "WWE"],
        promo_labels={"AEW": "AEW", "WWE": "WWE"},
        stats=[
            ("508",      "Day TBS reign"),
            ("60",       "Win streak (approx.)"),
            ("1&times;", "WWE Women's Championship"),
            ("169",      "Days as WWE champion"),
            ("2&times;", "Women's Tag Team"),
            ("2025",     "Queen of the Ring"),
        ],
        lead=("Seventeen documented bouts across two companies - a highlight subset, not a career "
              "count. The AEW streak figure of roughly 60 wins is Wikipedia's; no full career "
              "win-loss total is published because none was verified. The 2026 rows carry the live "
              "story: the champion pinned in a tag, the Italy loss Charlotte Flair caused, and the "
              "August 7 singles defeat. Filter by match type, tap any column header to sort, and "
              "turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("Three bouts that define the run. No star ratings are printed because none were "
                    "verified in this pass - Forbes called the WrestleMania 42 match a "
                    "match-of-the-night candidate, and that assessment is reported as theirs."),
    signature=[
        dict(rating="—", event="WrestleMania 42 Night 2", opponent="Rhea Ripley",
             stip="WWE Women's Championship — first-ever meeting; Forbes' match-of-the-night candidate"),
        dict(rating="—", event="Saturday Night's Main Event XLI", opponent="Tiffany Stratton",
             stip="WWE Women's Championship — the heel-turn payoff and first world title"),
        dict(rating="—", event="Dynamite, January 5, 2022", opponent="Ruby Soho",
             stip="TBS Championship tournament final — inaugural champion, 14 months into her career"),
    ],
    signature_count_word="three",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("1&times;", "WWE Women's Championship"),
            ("508",      "Day TBS reign"),
            ("2&times;", "Tag reigns with Belair"),
            ("2025",     "Queen of the Ring"),
        ],
        lead=("Four championships in six years, one per act: the AEW belt that made her, the tag "
              "partnership that settled her into WWE, and the world title the heel turn paid for."),
        rows=[
            dict(ic="W", name="WWE Women's Championship", count="1",
                 sub="November 1, 2025 &ndash; April 19, 2026 &middot; won from Tiffany Stratton at "
                     "Saturday Night&rsquo;s Main Event XLI in Salt Lake City after the October heel "
                     "turn, lost to Rhea Ripley at WrestleMania 42 Night 2 with Iyo Sky interfering "
                     "&middot; <b>169 days</b> &middot; her first world championship in any company"),
            dict(ic="T", name="AEW TBS Championship", count="1",
                 sub="January 5, 2022 &ndash; May 28, 2023 &middot; inaugural champion, beating Ruby "
                     "Soho in the tournament final &middot; <b>508 days</b>, the title&rsquo;s "
                     "entire first era, lost to Kris Statlander at Double or Nothing in under a "
                     "minute"),
            dict(ic="G", name="WWE Women's Tag Team Championship", count="2",
                 sub="Both with Bianca Belair &middot; won at Backlash in Lyon on May 4, 2024 from "
                     "The Kabuki Warriors, lost to The Unholy Union at Clash at the Castle: Scotland "
                     "on June 15 &middot; regained at Bash in Berlin on August 31, 2024; Naomi "
                     "replaced the injured-by-storyline Cargill in December &middot; PWI Tag Team of "
                     "the Year, 2024"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="One AEW entourage, one WWE super-team, and the unit she leads now.",
        cards=[
            dict(era="AEW &middot; 2021&ndash;2023",
                 name="The Baddies, original recipe",
                 members="Jade Cargill, with rotating associates",
                 desc="The AEW-era entourage branding around the TBS reign - Cargill as the "
                      "centrepiece with hired help around her. The name mattered enough that she "
                      "took it with her."),
            dict(era="WWE &middot; 2024",
                 name="With Bianca Belair",
                 members="Jade Cargill, Bianca Belair",
                 desc="The tag partnership that eased her into WWE: two Women's Tag Team "
                      "Championship reigns in 2024 and PWI's Tag Team of the Year. It ended by "
                      "storyline violence - the November 2024 mystery attack that wrote Cargill off "
                      "television and was eventually pinned on the Naomi feud."),
            dict(era="WWE &middot; 2026&ndash;present",
                 name="The Baddies",
                 members="Jade Cargill, Michin, B-Fab",
                 desc="Formed in March 2026 in the war with Rhea Ripley's side, and now her margin "
                      "in the Charlotte Flair feud. They gave her the May 23 six-woman tag win where "
                      "she pinned the champion; Flair's answer - Alexa Bliss and Tatum Paxley - "
                      "neutralised them on August 7, and Paxley beat Michin on the August 28 "
                      "SmackDown. The units are now feuding at full width."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One ring name - her real one - and three registers of the same imposing act.",
        cards=[
            dict(mono="TB", era="AEW &middot; 2020&ndash;2023", name="That B****",
                 desc="The AEW self-billing: untouchable, undefeated-until-she-wasn't, flanked by "
                      "Baddies. The look and the streak did the talking while the wrestling caught "
                      "up."),
            dict(mono="ST", era="WWE &middot; 2023&ndash;2025", name="The Storm",
                 desc="The WWE arrival act - 'a storm is coming' - built on spectacle entrances and "
                      "protected booking through the Belair partnership and the Naomi feud."),
            dict(mono="HL", era="WWE &middot; 2025&ndash;present", name="The heel who took the belt",
                 desc="Turned on October 24, 2025 by attacking Tiffany Stratton, took the WWE "
                      "Women's Championship a week later working the knee she had softened up, and "
                      "has stayed in that register since - now aimed at Charlotte Flair rather than "
                      "the title."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Basketball forward to world champion inside six years of wrestling.",
        rows=[
            dict(year="2014", title="Before wrestling",
                 desc="Finishes four years as a forward for Jacksonville University; works as a "
                      "child psychologist with foster children until 2019."),
            dict(year="2020", title="AEW debut",
                 desc="Debuts on the November 11, 2020 Dynamite, interrupting Cody Rhodes and "
                      "teasing Shaquille O'Neal's arrival."),
            dict(year="2021", title="First match, with Shaq",
                 desc="Wrestles her first match on March 3, 2021, tagging with Shaquille O'Neal "
                      "against Cody Rhodes and Red Velvet, and opens the winning streak. PWI and the "
                      "Wrestling Observer both name her Rookie of the Year."),
            dict(year="2022", title="Inaugural TBS Champion",
                 desc="Beats Ruby Soho in the tournament final on January 5, 2022 and holds the "
                      "title for its entire first era."),
            dict(year="2023", title="The streak ends, and the jump",
                 desc="Kris Statlander takes the title in under a minute at Double or Nothing on "
                      "May 28 and beats her again in her AEW farewell on September 15. WWE signs "
                      "her that month; she debuts at Fastlane in October."),
            dict(year="2024", title="Tag gold with Bianca Belair, then the mystery attack",
                 desc="Royal Rumble in-ring debut at No. 28 in January; two Women's Tag Team "
                      "Championship reigns with Belair; written off television in November by a "
                      "backstage attack angle."),
            dict(year="2025", title="Return, Queen of the Ring, heel turn, world champion",
                 desc="Returns at Elimination Chamber on March 1; beats Naomi at WrestleMania 41 and "
                      "again no-holds-barred at Evolution; wins Queen of the Ring over Asuka on June "
                      "28; loses the SummerSlam title match to Tiffany Stratton, turns heel on "
                      "October 24, and takes the WWE Women's Championship from Stratton on November "
                      "1."),
            dict(year="2026", title="The reign ends, and the Flair feud begins",
                 desc="Loses the title to Rhea Ripley at WrestleMania 42 on April 19 after Iyo Sky "
                      "interferes; forms The Baddies with Michin and B-Fab; pins Ripley in a "
                      "six-woman tag on May 23 but loses the Clash in Italy rematch on May 31 when "
                      "Charlotte Flair intervenes; loses the SummerSlam interim-title ladder match "
                      "on August 2 and the first Flair singles match on August 7."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who she went to war with.",
        cards=[
            dict(name="Charlotte Flair", slug="charlotte-flair",
                 desc="The live feud, and the first one aimed at her rather than a belt. Flair's "
                      "unexplained Clash in Italy interference on May 31, 2026 cost Cargill the "
                      "title rematch; the summer escalated through backstage attacks on both sides "
                      "to the August 7 SmackDown singles match, which Flair won once Alexa Bliss "
                      "and Tatum Paxley neutralised The Baddies. Cagematch logged the crowd verdict "
                      "as mixed, and the feud as unmistakably unfinished."),
            dict(name="Tiffany Stratton", slug="tiffany-stratton",
                 desc="The rivalry that made her a world champion. Stratton beat her clean at "
                      "SummerSlam on August 2, 2025; Cargill answered with the October heel turn, a "
                      "backstage attack, and the November 1 title win built entirely around "
                      "Stratton's damaged knee - the most complete heel performance of her career."),
            dict(name="Rhea Ripley",
                 desc="The 2026 championship rivalry: a first-ever meeting at WrestleMania 42 that "
                      "Forbes called a match-of-the-night candidate, won by Ripley with Iyo Sky's "
                      "help; Cargill's tag-match pin on the champion at Saturday Night's Main Event "
                      "on May 23; and the Clash in Italy rematch that Charlotte Flair's intervention "
                      "tilted. Ripley's knee surgery has paused it with the score unsettled."),
            dict(name="Naomi",
                 desc="The 2025 grudge: the mystery-attacker angle that had written Cargill off "
                      "television resolved into Naomi, and Cargill beat her at WrestleMania 41 on "
                      "April 19 and again, no holds barred, at Evolution on July 13. It was her "
                      "first long solo story in WWE and it made the heel turn that followed land "
                      "harder."),
            dict(name="Kris Statlander",
                 desc="The AEW asterisk: the only wrestler to beat her in that company, and she did "
                      "it twice in 2023 - the under-a-minute title win at Double or Nothing on May "
                      "28, and the September 15 Rampage farewell. Any 'undefeated' framing of "
                      "Cargill's AEW run has to route around Statlander."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Business",
        lead="Thin by design - the verified list is short, and the most interesting entry is not a "
             "screen credit.",
        rows=[
            dict(when="2023&ndash;", title="Texas Smoke, Women's Pro Fastpitch", kind="Business",
                 desc="Co-owner of the Austin-based professional softball franchise, announced March "
                      "2023 - a sports-ownership stake almost no active wrestler has."),
            dict(when="2024&ndash;", title="WWE 2K", kind="Game",
                 desc="A playable fixture of the current WWE 2K series. Her exact debut entry was "
                      "not verified in this pass, so no year is claimed for it."),
            dict(when="2021&ndash;2023", title="AEW television", kind="TV",
                 desc="The TBS Championship era made her one of AEW's most-featured acts on the "
                      "network the belt was named for. No film role, memoir or documentary could be "
                      "verified, so none is listed."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated with their edges drawn - especially the streak, which is "
             "routinely rounded up into a myth.",
        stats=[
            ("508", "Days as inaugural TBS Champion"),
            ("60",  "Consecutive wins (approx.)"),
            ("169", "Days as WWE Women's Champion"),
        ],
        rows=[
            dict(name="Inaugural AEW TBS Champion - 508 days",
                 sub="January 5, 2022 to May 28, 2023, from the tournament final over Ruby Soho to "
                     "the under-a-minute loss to Kris Statlander at Double or Nothing. She was the "
                     "title's only champion for its entire first era."),
            dict(name="A winning streak of roughly 60 matches - not an undefeated career",
                 sub="Wikipedia's figure for the run from her March 2021 debut through the TBS "
                     "reign. Kris Statlander beat her twice in 2023, so 'undefeated in AEW' is "
                     "false; 'unbeaten for her first two-plus years' is the accurate version."),
            dict(name="WWE Women's Champion - 169 days",
                 sub="November 1, 2025 to April 19, 2026. Won from Tiffany Stratton at Saturday "
                     "Night's Main Event XLI, ending a reign counted at 301 days by Sports "
                     "Illustrated and 302 by Wikipedia; lost to Rhea Ripley at WrestleMania 42 "
                     "after Iyo Sky's interference. Her first world title in any company."),
            dict(name="Queen of the Ring, 2025",
                 sub="Beat Asuka in the final at Night of Champions in Riyadh on June 28, 2025, "
                     "earning the SummerSlam title match Stratton turned back."),
            dict(name="Two Women's Tag Team Championship reigns with Bianca Belair",
                 sub="May 4 to June 15, 2024, and from August 31, 2024 until the storyline attack "
                     "removed her; PWI named them Tag Team of the Year for 2024."),
            dict(name="Second career, second sport",
                 sub="Four years a forward at Jacksonville University, then a child psychologist "
                     "working with foster children until 2019, then a wrestler at 28 - and co-owner "
                     "of the Texas Smoke softball franchise since 2023."),
        ],
        footnote=("No career win-loss total is published - the streak figure is Wikipedia's and is "
                  "stated as approximate. Social handles are omitted as unverified. Her birthplace "
                  "is printed as a conflict: TheSmackDownHotel says Vero Beach, Florida, while a "
                  "Wikipedia read returned Gifford, Florida - Vero Beach is used in the structured "
                  "data and both are flagged in the rail."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Jade_Cargill"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/jade-cargill"),
        dict(k="SmackDown Hotel", v="Profile and vitals",
             href="https://www.thesmackdownhotel.com/wrestlers/jade-cargill"),
        dict(k="Sports Illustrated", v="The November 1, 2025 title win over Tiffany Stratton",
             href="https://www.si.com/fannation/wrestling/wwe/jade-cargill-dominates-tiffany-stratton-to-win-wwe-women-championship"),
        dict(k="Fox News", v="Clash in Italy - Charlotte Flair's interference",
             href="https://www.foxnews.com/sports/rhea-ripley-curiously-gets-help-charlotte-flair-retain-womens-title-wwe-clash-italy"),
        dict(k="Cagematch", v="Flair vs. Cargill, SmackDown, August 7, 2026",
             href="https://www.cagematch.net/?id=111&nr=144741"),
        dict(k="Yahoo Sports", v="WrestleMania 42 full results",
             href="https://sports.yahoo.com/articles/wrestlemania-42-full-winners-list-042619263.html"),
        dict(k="Wrestling Inc", v="SmackDown results, August 7, 2026",
             href="https://www.wrestlinginc.com/2232927/wwe-smackdown-august-7-us-title-on-line-jade-cargill-charlotte-flair/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Was Jade Cargill undefeated in AEW?",
            a="No &mdash; and the true version is still extraordinary. She ran a winning streak of "
              "roughly <b>60 matches</b> from her March 3, 2021 debut through her entire 508-day "
              "TBS Championship reign. <b>Kris Statlander</b> ended it at Double or Nothing on May "
              "28, 2023, taking the title in under a minute, and beat her again on the September "
              "15, 2023 Rampage in her final AEW match. Two losses, both to the same woman, both "
              "in her last four months with the company.",
            q_ld="Was Jade Cargill undefeated in AEW?",
            a_ld="No. Jade Cargill ran a winning streak of roughly 60 matches from her AEW debut in "
                 "March 2021 through her 508-day reign as inaugural TBS Champion, but Kris "
                 "Statlander defeated her twice in 2023: at Double or Nothing on May 28, 2023, "
                 "winning the TBS Championship in under a minute, and again on the September 15, "
                 "2023 episode of Rampage in Cargill's final AEW match."),
        dict(
            q="Is Jade Cargill a champion right now, and what is she doing?",
            a="No. As of August 31, 2026 she holds nothing. Her WWE Women's Championship reign "
              "ended at <b>169 days</b> when Rhea Ripley beat her at WrestleMania 42 on April 19, "
              "with Iyo Sky interfering. Since then: a tag-match pin on Ripley in May, the Clash in "
              "Italy rematch Charlotte Flair's interference cost her on May 31, a loss in the "
              "SummerSlam interim-title ladder match on August 2, and a loss to Flair one-on-one on "
              "the August 7 SmackDown. She leads <b>The Baddies</b> &mdash; Michin and B-Fab "
              "&mdash; and the Flair feud is her live storyline.",
            q_ld="Is Jade Cargill a champion right now?",
            a_ld="No. As of August 31, 2026 Jade Cargill holds no championship. Her WWE Women's "
                 "Championship reign ended at 169 days when Rhea Ripley defeated her at "
                 "WrestleMania 42 on April 19, 2026, with interference from Iyo Sky. She is on "
                 "SmackDown leading The Baddies, with Michin and B-Fab, in an ongoing feud with "
                 "Charlotte Flair, who beat her one-on-one on the August 7, 2026 SmackDown."),
        dict(
            q="Why are Jade Cargill and Charlotte Flair feuding?",
            a="Because of Clash in Italy. On <b>May 31, 2026</b>, with Cargill challenging Rhea "
              "Ripley for the WWE Women's Championship in Turin, Flair came through the crowd "
              "unannounced, neutralised Michin and B-Fab, and broke up Cargill's pin after the "
              "Jaded &mdash; Ripley retained, and Flair has never explained herself. The feud ran "
              "through backstage attacks all summer, a shared ladder-match loss at SummerSlam, and "
              "the first singles meeting on August 7, which Flair won with her own numbers game. "
              "It was reportedly pitched for SummerSlam and landed on SmackDown instead.",
            q_ld="Why are Jade Cargill and Charlotte Flair feuding in 2026?",
            a_ld="The feud began at Clash in Italy on May 31, 2026, when Charlotte Flair emerged "
                 "from the crowd during Jade Cargill's WWE Women's Championship match against Rhea "
                 "Ripley, neutralised Cargill's allies Michin and B-Fab, and broke up a pin, "
                 "helping Ripley retain. Flair has given no explanation. The rivalry escalated "
                 "through the summer to their first singles match on the August 7, 2026 SmackDown, "
                 "which Flair won after interference from Alexa Bliss and Tatum Paxley."),
        dict(
            q="What did Jade Cargill do before wrestling?",
            a="Basketball, then social work. She played forward for Jacksonville University from "
              "2010 to 2014 and graduated with a social science degree, then worked as a <b>child "
              "psychologist with foster children until 2019</b>. She did not wrestle a match until "
              "March 2021, at 28 &mdash; and was a champion ten months later. She has also "
              "co-owned the Texas Smoke professional softball franchise since 2023.",
            q_ld="What did Jade Cargill do before becoming a wrestler?",
            a_ld="Jade Cargill played college basketball as a forward for Jacksonville University "
                 "from 2010 to 2014, graduated with a degree in social science, and worked as a "
                 "child psychologist with foster children until 2019. She wrestled her first match "
                 "in March 2021 at age 28 and won the inaugural AEW TBS Championship ten months "
                 "later. Since March 2023 she has been a co-owner of the Texas Smoke Women's Pro "
                 "Fastpitch softball franchise."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Jade Cargill", sub="her ring name is her legal name"),
        dict(label="Born", value="June 3, 1992",
             sub="Vero Beach, Florida per SmackDown Hotel &middot; a Wikipedia read returned "
                 "Gifford, Florida &middot; age 34"),
        dict(label="Height", value="5&#8242;10&#8243;", sub="178 cm"),
        dict(label="Weight", value="160 lb", sub="73 kg"),
        dict(label="Debut", value="November 11, 2020", sub="AEW Dynamite &middot; first match "
                                                           "March 3, 2021, with Shaquille O'Neal"),
        dict(label="WWE debut", value="October 7, 2023", sub="Fastlane, after signing in September"),
        dict(label="College", value="Jacksonville University", sub="basketball forward, 2010&ndash;14"),
        dict(label="Finisher", value="Jaded",
             sub="elevated double chickenwing into a facebuster"),
        dict(label="Faction", value="The Baddies", sub="with Michin and B-Fab, since March 2026"),
        dict(label="Brand", value="SmackDown"),
        dict(label="Also known as", value="The Storm"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1992-06-03",
    bornplace="Vero Beach, Florida, United States",
    nationality="United States",
    alumni="Jacksonville University",
    height_cm=178,
    weight_kg=73,
    ld=dict(
        alternateName=["The Storm"],
        award=["WWE Women's Championship (1 reign, 169 days)",
               "AEW TBS Championship (1 reign, inaugural champion, 508 days)",
               "WWE Women's Tag Team Championship (2 reigns, with Bianca Belair)",
               "Queen of the Ring (2025)",
               "Pro Wrestling Illustrated Rookie of the Year (2021)",
               "Wrestling Observer Newsletter Rookie of the Year (2021)",
               "Pro Wrestling Illustrated Tag Team of the Year (2024, with Bianca Belair)"],
        knowsAbout=["Professional wrestling", "WWE", "AEW", "Women's professional wrestling",
                    "College basketball", "Championship wrestling"],
        description="Jade Cargill is an American professional wrestler signed to WWE. A former "
                    "Jacksonville University basketball forward and child psychologist, she was the "
                    "inaugural AEW TBS Champion for 508 days across a winning streak of roughly 60 "
                    "matches, won the 2025 Queen of the Ring tournament, held the WWE Women's Tag "
                    "Team Championship twice with Bianca Belair, and won the WWE Women's "
                    "Championship from Tiffany Stratton on November 1, 2025, holding it 169 days "
                    "until WrestleMania 42.",
        sameAs=["https://en.wikipedia.org/wiki/Jade_Cargill",
                "https://www.wwe.com/superstars/jade-cargill"],
    ),
)
