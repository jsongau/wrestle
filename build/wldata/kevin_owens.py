# -*- coding: utf-8 -*-
"""Kevin Owens - dossier data.

Sources: web-verified August 31, 2026 (Wikipedia, CBS Sports, F4W/WON, Last Word on
Sports, IWNerd and TheSportster Observer round-ups, SmackDown Hotel). Every match row
carries a day-precision date confirmed in at least one of those sources.

Deliberate omissions:
  * No career win-loss total - no verified figure exists and none is invented.
  * The August 7, 2026 SmackDown return segment is described by WWE.com only as
    Owens "shaking up SmackDown"; no verifiable match detail, so no row.
  * Exact dates for the PWG and IWS reigns were not verified in this pass and are
    counted, not dated.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2015-02-11", promo="WWE", landmark=True,
         event="NXT TakeOver: Rival", opponent="Sami Zayn", opponent_html=True,
         stip="Singles — ref stoppage, two months after turning on him", title="NXT Championship"),
    dict(result="W", date="2015-05-31", promo="WWE", landmark=True,
         event="Elimination Chamber", opponent="John Cena",
         stip="Non-title — pins Cena clean in his first main-roster match", title=""),
    dict(result="L", date="2015-07-04", promo="WWE",
         event="The Beast in the East — Tokyo", opponent="Finn Balor",
         stip="Singles — the 143-day NXT reign ends in Japan", title="NXT Championship"),
    dict(result="W", date="2016-08-29", promo="WWE", type="tag", landmark=True,
         event="Raw — Houston", opponent="Seth Rollins, Big Cass & Roman Reigns",
         stip="Fatal four-way for the vacated title — Triple H intervenes",
         title="WWE Universal Championship"),
    dict(result="W", date="2017-01-29", promo="WWE",
         event="Royal Rumble — San Antonio", opponent="Roman Reigns",
         stip="No disqualification, Chris Jericho in a shark cage — retains",
         title="WWE Universal Championship"),
    dict(result="L", date="2017-03-05", promo="WWE", landmark=True,
         event="Fastlane", opponent="Goldberg",
         stip="Singles — 22 seconds; the 188-day reign ends", title="WWE Universal Championship"),
    dict(result="W", date="2017-04-02", promo="WWE",
         event="WrestleMania 33", opponent="Chris Jericho",
         stip="Singles — the Festival of Friendship bill comes due",
         title="WWE United States Championship"),
    dict(result="L", date="2022-04-02", promo="WWE", landmark=True,
         event="WrestleMania 38 Night 1 — Dallas", opponent="Steve Austin",
         stip="No Holds Barred — Austin's first match in 19 years", title=""),
    dict(result="W", date="2023-04-01", promo="WWE", type="tag", landmark=True,
         event="WrestleMania 39 Night 1", opponent="The Usos",
         stip="Tag — with Sami Zayn; main event, five stars (Meltzer)",
         title="Undisputed WWE Tag Team Championship"),
    dict(result="L", date="2023-09-02", promo="WWE", type="tag",
         event="Payback", opponent="The Judgment Day",
         stip="Steel City Street Fight — the 154-day reign ends",
         title="Undisputed WWE Tag Team Championship"),
    dict(result="L", date="2025-02-01", promo="WWE",
         event="Royal Rumble — Indianapolis", opponent="Cody Rhodes",
         stip="Ladder match — challenge", title="Undisputed WWE Championship"),
    dict(result="W", date="2025-03-01", promo="WWE", landmark=True,
         event="Elimination Chamber — Toronto", opponent="Sami Zayn", opponent_html=True,
         stip="Unsanctioned match — his last bout before the neck injury", title=""),
    dict(result="W", date="2026-08-02", promo="WWE", type="tag", landmark=True,
         event="SummerSlam Night 2 — Minneapolis", opponent="Sami Zayn, Finn Balor & Gunther",
         stip="Fatal four-way — returns after 17 months out and pins Zayn for the No. 1 "
              "contendership", title=""),
    dict(result="L", date="2026-08-21", promo="WWE", landmark=True,
         event="SmackDown — Toronto", opponent="CM Punk", opponent_html=True,
         stip="Singles — Zayn's belt shot decides it", title="Undisputed WWE Championship"),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Sami Zayn": "sami-zayn", "CM Punk": "cm-punk"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="kevin-owens",
    name="Kevin Owens",
    realname="Kevin Yanick Steen",
    epithet="The Prizefighter",
    hook="Record & Titles",

    meta_desc=("Kevin Owens held the WWE Universal Championship for 188 days, returned at SummerSlam "
               "2026 from a 17-month neck injury, and lost the title match that followed to a belt "
               "shot from Sami Zayn. Full record, titles, factions, records and career."),
    og_desc=("The Prizefighter: a 188-day Universal Championship reign remembered for its 22-second "
             "ending, a WrestleMania against Stone Cold, a five-star tag main event with Sami Zayn - "
             "and now a comeback from spinal surgery and a betrayal from the same man."),
    tw_desc="The Prizefighter: Universal Champion for 188 days, back from a broken neck - and betrayed by Sami Zayn.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2000",
    height_imp="6&#8242;0&#8243;",
    weight_lb="266",
    world_titles="1",
    vitals_tagline="Fight Owens Fight",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="KO", title="WWE Shop", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable across the WWE 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="ROH", title="Ring of Honor", sub="ROH World Champion, 2012-13, as Kevin Steen",
             tag="Visit", href="https://www.rohwrestling.com/"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/kevin-owens"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Mr. Wrestlemania&rsquo;s opponent &middot; The KO Show &middot; formerly Kevin Steen",
    hero_tag="Saint-Jean-sur-Richelieu, Quebec, Canada &middot; <em>IWS &middot; ROH &middot; PWG "
             "&middot; NXT &middot; WWE &middot; 2000&ndash;present</em>",
    now_label="NOW",
    now_bold="SmackDown, no championship",
    now_tail=" &middot; back from a 17-month neck layoff; lost the August 21 title match to CM Punk "
             "when Sami Zayn hit him with the belt, and the August 28 contender rematch collapsed in "
             "chaos",
    hstats=[
        dict(value="1",   x=True,  label="Universal Title"),
        dict(value="188", x=False, label="Day Universal Reign"),
        dict(value="5",   x=True,  label="IC & US Reigns"),
        dict(value="17",  x=False, label="Month Neck Comeback"),
    ],
    ghost_link="From the Quebec indies to the Universal title, twice through the fire",
    vlabel="Est. 2000 &middot; Marieville, Quebec",
    mono="KO",

    # ---------------------------------------------------------------- 01 overview
    # index into overview of the correction paragraph -> the framed
    # "Setting one thing straight" callout (aside.corr) on the page
    correction=1,
    overview=[
        "<b>Kevin Owens</b> was supposed to be finished. His neck and spinal cord injuries, announced "
        "on April 4, 2025, required surgery, pulled him from WrestleMania 41 and kept him out for "
        "roughly seventeen months &mdash; long enough that his surprise entry into the SummerSlam "
        "fatal four-way on August 2, 2026 was covered as a return from a career that had nearly "
        "ended. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">17</span>'
        '<span class="pull-cap">months between the unsanctioned Zayn match in March 2025 and the SummerSlam 2026 return</span></span>'
        "He won that four-way, pinning Sami Zayn with a Stunner to become No. 1 contender to "
        "CM Punk&rsquo;s Undisputed WWE Championship, and told the post-show he had no intention of "
        "being careful with the rebuilt neck. Nineteen days later he lost the title match &mdash; not "
        "to Punk, exactly, but to Zayn, who hit him with the belt after Owens refused to use it.",

        "The number attached to him is 22 seconds &mdash; the Goldberg match at Fastlane on March 5, "
        "2017 &mdash; and it has swallowed the reign it ended. Owens won the vacated WWE Universal "
        "Championship on the August 29, 2016 Raw, in a fatal four-way against Seth Rollins, Big Cass "
        "and Roman Reigns decided by Triple H&rsquo;s interference, and held it <b>188 days</b>, "
        "through a No. 1 contender&rsquo;s gauntlet of a Raw main-event scene and a Royal Rumble 2017 "
        "defence against Reigns with Chris Jericho suspended above the ring in a shark cage. It was, "
        "at the time, the longest reign the young title had had. The 22 seconds were the ending "
        "WWE chose for it, not the measure of it.",

        "He was born Kevin Steen in Saint-Jean-sur-Richelieu, Quebec, on May 7, 1984, and debuted on "
        "his sixteenth birthday, trained by Serge Jodoin, Jacques Rougeau and later Terry Taylor. As "
        "<b>Kevin Steen</b> he was ROH World Champion and a three-time PWG World Champion, working an "
        "anti-hero brawler act years ahead of its market. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">22</span>'
        '<span class="pull-cap">seconds against Goldberg at Fastlane 2017 &mdash; the ending that swallowed a 188-day reign</span></span>'
        "WWE signed him in August 2014, and the "
        "efficiency of what followed is still startling: NXT debut December 11, 2014, NXT Champion by "
        "February 11, 2015 &mdash; beating his oldest friend Sami Zayn by referee stoppage &mdash; "
        "and a clean pin over John Cena in his first main-roster match at Elimination Chamber on May "
        "31, 2015. No one arrives better than that.",

        "The friendship is the career&rsquo;s spine, and it has just inverted. Owens and Zayn came up "
        "together from 2002-03, won ROH tag gold in 2008, and in WWE have alternated between blood "
        "feud and the WrestleMania 39 Night 1 main event, where they took the Undisputed Tag Team "
        "Championship from The Usos &mdash; a five-star match and the emotional payoff of the "
        "Bloodline era. Owens was the betrayer every previous time, including the March 1, 2025 "
        "unsanctioned match in Toronto he won just before his body gave out. Now the ledger has "
        "flipped: at SummerSlam the two embraced before Owens pinned him; on August 21 Zayn cost him "
        "the title with the belt; on August 28 the No. 1 contender triple threat with Gunther and "
        "Finn Balor ended in a Zayn-fuelled no-contest with Owens pinning Gunther and no referee "
        "conscious to count. As of August 31, 2026 he holds no championship, the contendership is "
        "unresolved, and the next Owens-Zayn match will be the first where Owens is the wronged "
        "man.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("188",      "Day Universal reign"),
            ("22",       "Seconds at Fastlane"),
            ("3&times;", "United States"),
            ("2&times;", "Intercontinental"),
            ("5.0",      "Stars at WrestleMania 39"),
            ("2000",     "First match, at sixteen"),
        ],
        lead=("Fourteen documented bouts &mdash; the arrival double of 2015, the Universal reign at "
              "both ends, Austin at WrestleMania 38, the Zayn arc from Rival to the belt shot. This "
              "is a curated ledger, not a career count, and no career win&ndash;loss total is "
              "published because no verified one exists. The August 28, 2026 contender triple threat "
              "is absent by design: it ended in chaos with no decision rendered. Filter by match "
              "type, tap any column header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The rated peaks, as reproduced in published Observer round-ups &mdash; a "
                    "five-star WrestleMania main event and a cluster of 4.5s from the two years when "
                    "he main-evented everything. Ratings are as reported, not re-checked against "
                    "archives."),
    signature=[
        dict(rating="5.0", event="WrestleMania 39 Night 1", opponent="The Usos",
             stip="Undisputed Tag Team Championship, with Sami Zayn — the main event"),
        dict(rating="4.5", event="Royal Rumble 2017", opponent="Roman Reigns",
             stip="Universal Championship, no DQ — Jericho in the shark cage"),
        dict(rating="4.5", event="Battleground 2016", opponent="Sami Zayn",
             stip="Singles — the definitive chapter of the WWE feud"),
        dict(rating="4.5", event="Elimination Chamber 2015", opponent="John Cena",
             stip="Non-title — the debut upset"),
        dict(rating="4.5", event="Money in the Bank 2015", opponent="John Cena",
             stip="Non-title rematch — Cena evens the series"),
    ],
    signature_count_word="five",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("1",        "Universal reign"),
            ("3&times;", "United States"),
            ("2&times;", "Intercontinental"),
            ("1",        "ROH World title"),
        ],
        lead=("Nine WWE championships across five titles, and a full independent resume as Kevin "
              "Steen underneath. Dates are as the published title histories give them; PWG and IWS "
              "reigns are counted, not dated, because the individual dates were not verified in this "
              "pass."),
        rows=[
            dict(ic="U", name="WWE Universal Championship", count="1",
                 sub="August 29, 2016 &ndash; March 5, 2017 &middot; won the vacated title in a "
                     "fatal four-way on Raw with Triple H&rsquo;s help, lost to Goldberg at Fastlane "
                     "in 22 seconds &middot; <b>188 days</b>, the longest reign the title had had at "
                     "the time"),
            dict(ic="S", name="WWE United States Championship", count="3",
                 sub="All in 2017, all against the same two men &middot; def. Chris Jericho at "
                     "WrestleMania 33 on April 2, lost it back at Payback on April 30 &middot; "
                     "regained May 2 on SmackDown &middot; lost to AJ Styles at a Madison Square "
                     "Garden house show on July 7 &mdash; a non-televised title change &mdash; "
                     "regained at Battleground on July 23, lost to Styles again on the July 25 "
                     "SmackDown"),
            dict(ic="I", name="WWE Intercontinental Championship", count="2",
                 sub="2015 &middot; def. Ryback at Night of Champions on September 20, lost to Dean "
                     "Ambrose at TLC on December 13 &middot; 2016 &middot; regained from Ambrose on "
                     "the February 15 Raw, lost in the WrestleMania 32 seven-man ladder match to "
                     "Zack Ryder on April 3"),
            dict(ic="T", name="Undisputed WWE Tag Team Championship", count="1",
                 sub="April 1 &ndash; September 2, 2023, with Sami Zayn &middot; won from The Usos "
                     "in the WrestleMania 39 Night 1 main event, lost to The Judgment Day at Payback "
                     "&middot; 154 days"),
            dict(ic="N", name="NXT Championship", count="1",
                 sub="February 11 &ndash; July 4, 2015 &middot; won from Sami Zayn at TakeOver: "
                     "Rival, lost to Finn Balor at The Beast in the East in Tokyo &middot; 143 days"),
            dict(ic="R", name="ROH World Championship", count="1",
                 sub="May 12, 2012 &ndash; April 5, 2013, as Kevin Steen &middot; won from Davey "
                     "Richards at Border Wars, lost to Jay Briscoe at Supercard of Honor VII "
                     "&middot; plus 1 ROH World Tag Team reign with El Generico"),
            dict(ic="P", name="PWG World Championship", count="3",
                 sub="Pro Wrestling Guerrilla, California, as Kevin Steen &middot; plus 3 PWG tag "
                     "reigns &middot; individual dates not verified"),
            dict(ic="W", name="IWS World Heavyweight Championship", count="3",
                 sub="The Montreal promotion where he and Sami Zayn both started &middot; dates not "
                     "verified &middot; plus the CZW Iron Man Championship, 1 reign"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Alliances",
        lead="He has mostly worked alone. The partnerships that mattered were two, and both ended "
             "with a betrayal — only one of them his.",
        cards=[
            dict(era="Independents &amp; WWE &middot; 2003&ndash;present",
                 name="Steen & Generico / Owens & Zayn",
                 members="Kevin Owens (Kevin Steen), Sami Zayn (El Generico)",
                 desc="The longest-running double act in modern wrestling: friends and rivals since "
                      "the Montreal indies, ROH World Tag Team Champions in 2008, enemies in the "
                      "famous 2010-2012 ROH blood feud, and the same cycle in WWE from the 2015 NXT "
                      "betrayal through the WrestleMania 39 title win to the 2025 unsanctioned "
                      "match. Owens wrote every betrayal until August 21, 2026, when Zayn hit him "
                      "with the championship belt. That reversal is the current story of both "
                      "careers."),
            dict(era="WWE &middot; 2016&ndash;2017",
                 name="JeriKO",
                 members="Kevin Owens, Chris Jericho",
                 desc="The best-friends act that protected his Universal Championship reign - "
                      "scarves, The List of Jericho, and a slow-burn split staged as the 'Festival "
                      "of Friendship' on the February 13, 2017 Raw, still one of the most-praised "
                      "breakup segments WWE has produced. Owens beat Jericho for the United States "
                      "Championship at WrestleMania 33 to close it."),
            dict(era="WWE &middot; 2024&ndash;2025",
                 name="The grudge run",
                 members="Kevin Owens, alone",
                 desc="Not a faction - a mode. The post-Bad Blood 2024 attack on Cody Rhodes, the "
                      "package piledrivers, the stolen title belt, the ladder match at the 2025 "
                      "Royal Rumble and the unsanctioned Zayn match in Toronto. It was cut off "
                      "mid-arc by the neck injury, which is why the 2026 version of Owens returned "
                      "insisting he owed nobody an apology."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Two names, one act: <b>Kevin Steen</b> (2000&ndash;2014) &rarr; <b>Kevin Owens</b> "
             "(2014&ndash;present). WWE renamed him for trademark reasons; he chose Owens for his "
             "son, named for Owen Hart.",
        cards=[
            dict(mono="KS", era="Independents &middot; 2000&ndash;2014", name="Kevin Steen",
                 desc="Mr. Wrestling: the anti-hero brawler of ROH and PWG, package piledriving his "
                      "way through the same buildings as El Generico. ROH World Champion in 2012 "
                      "after a feud with the company itself; three PWG World Championships in "
                      "California."),
            dict(mono="PF", era="NXT &amp; WWE &middot; 2014&ndash;2022", name="The Prizefighter",
                 desc="The fight-for-my-family mercenary who beat Zayn for the NXT title and pinned "
                      "Cena in his first main-roster match. Universal Champion within two years - "
                      "prone to powerbombing people onto ring aprons and explaining, correctly, that "
                      "it paid."),
            dict(mono="KO", era="WWE &middot; 2022&ndash;2024", name="The reformed brawler",
                 desc="The babyface stretch: the Stone Cold match at WrestleMania 38, the Bloodline "
                      "resistance with Zayn, the WrestleMania 39 tag title main event, sixteen "
                      "months as tag champion and conscience."),
            dict(mono="GR", era="WWE &middot; 2024&ndash;present", name="The grudge-keeper",
                 desc="Turned on Cody Rhodes in October 2024 over the Bloodline's sins being "
                      "forgiven, and has wrestled ever since as a man auditing everyone else's "
                      "hypocrisy. The neck injury and 2026 return added the one thing the character "
                      "lacked: something real to be furious about."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="A sixteenth-birthday debut in Quebec to a comeback from spinal surgery, 26 years on.",
        rows=[
            dict(year="2000", title="Debut at sixteen",
                 desc="First match on May 7, 2000 - his birthday - in Quebec, trained by Serge "
                      "Jodoin and Jacques Rougeau."),
            dict(year="2008", title="ROH tag champion with El Generico",
                 desc="Wins the ROH World Tag Team Championship on September 19 with the future Sami "
                      "Zayn - the partnership half of a twenty-year story."),
            dict(year="2012", title="ROH World Champion",
                 desc="Beats Davey Richards at Border Wars on May 12 and holds the title nearly a "
                      "year as the company's resident menace."),
            dict(year="2014", title="Signs with WWE",
                 desc="August 12, 2014. Debuts at NXT TakeOver: R Evolution on December 11 - and "
                      "attacks Sami Zayn, the new NXT Champion, the same night."),
            dict(year="2015", title="NXT Champion; pins Cena",
                 desc="Takes the title from Zayn by stoppage at TakeOver: Rival on February 11, then "
                      "pins John Cena clean at Elimination Chamber on May 31 in his first "
                      "main-roster match. Loses the NXT title to Finn Balor in Tokyo on July 4."),
            dict(year="2016", title="Universal Champion",
                 desc="Wins the vacated Universal Championship in a fatal four-way on the August 29 "
                      "Raw, with an assist from Triple H, and holds it 188 days behind JeriKO."),
            dict(year="2017", title="22 seconds, then the US title year",
                 desc="Loses the title to Goldberg at Fastlane on March 5 in 22 seconds; splits from "
                      "Jericho at the Festival of Friendship and beats him for the United States "
                      "Championship at WrestleMania 33 - the first of three US reigns that year."),
            dict(year="2022", title="Stone Cold",
                 desc="Talks Steve Austin into a No Holds Barred match at WrestleMania 38 on April 2 "
                      "- Austin's first match in 19 years - and loses it in the best possible "
                      "cause."),
            dict(year="2023", title="The WrestleMania 39 main event",
                 desc="Wins the Undisputed WWE Tag Team Championship with Sami Zayn from The Usos in "
                      "the Night 1 main event on April 1, five stars, and holds it 154 days."),
            dict(year="2025", title="The injury",
                 desc="Wins the unsanctioned match with Zayn at Elimination Chamber in Toronto on "
                      "March 1; on April 4 announces neck and spinal cord injuries requiring "
                      "surgery, and vanishes from WrestleMania 41 and everything after."),
            dict(year="2026", title="The comeback and the betrayal",
                 desc="Returns unannounced into the SummerSlam Night 2 fatal four-way on August 2, "
                      "pins Zayn for the No. 1 contendership, loses the August 21 title match to CM "
                      "Punk when Zayn uses the belt, and is left in the wreckage of the August 28 "
                      "contender triple threat."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Sami Zayn", slug="sami-zayn",
                 desc="Twenty-three years of the same story with the roles finally reversed. Owens "
                      "betrayed him in NXT in 2014, beat him for the title at Rival, warred with him "
                      "through 2016-17, reunited to win the WrestleMania 39 main event, and won "
                      "their unsanctioned Toronto match in March 2025 as his own body failed. At "
                      "SummerSlam 2026 they embraced before Owens pinned him; on August 21 Zayn hit "
                      "him with the championship belt and cost him the title. For the first time in "
                      "the whole saga, Owens is the one owed."),
            dict(name="CM Punk", slug="cm-punk",
                 desc="Champion and challenger, briefly and violently. Punk retained the Undisputed "
                      "WWE Championship over him on the August 21, 2026 SmackDown - a finish made by "
                      "Zayn's belt shot after Owens refused to cheat, which is the detail that "
                      "defines where Owens now stands. Reports frame the singles series as done for "
                      "now; the contender picture it wrecked is not."),
            dict(name="John Cena",
                 desc="The 2015 arrival feud: a clean pin on Cena at Elimination Chamber in his "
                      "first main-roster match, a Cena win at Money in the Bank, a Cena win at "
                      "Battleground - two of the three rated 4.5. No debut in the modern era has "
                      "been handed more, or cashed it better."),
            dict(name="Chris Jericho",
                 desc="Partner first, opponent after: JeriKO carried his Universal reign, the "
                      "Festival of Friendship ended it as television, and the WrestleMania 33 United "
                      "States title match settled it in the ring. The shark cage at the 2017 Royal "
                      "Rumble - Jericho suspended above an Owens-Reigns No DQ match - remains the "
                      "reign's best image."),
            dict(name="Cody Rhodes",
                 desc="The 2024-25 grudge: Owens attacked Rhodes after Bad Blood over the "
                      "rehabilitation of the Bloodline's allies, stole the championship belt, and "
                      "took the feud to a ladder match at the 2025 Royal Rumble, which Rhodes won. "
                      "The neck injury froze the account a month later."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Thin by design — the verified list is short, and nothing is added to pad it.",
        rows=[
            dict(when="2015&ndash;", title="WWE 2K", kind="Game",
                 desc="Playable across the WWE 2K series since 2K16. Kevin Steen has never appeared "
                      "in a WWE game."),
            dict(when="2016&ndash;", title="The KO Show", kind="Television",
                 desc="His recurring in-ring talk segment - the delivery mechanism for most of his "
                      "turns, including the Festival of Friendship response and the Austin "
                      "WrestleMania challenge."),
            dict(when="2026", title="SummerSlam post-show comments", kind="Press",
                 desc="The August 2026 return interviews - CBS Sports and Cageside Seats coverage of "
                      "the neck injury, the 17-month absence, and his stated refusal to wrestle "
                      "carefully - are the primary sources on his current condition."),
            dict(when="2012&ndash;14", title="ROH and PWG catalogue", kind="Archive",
                 desc="The Steen-era matches - the Generico feud, the ROH title run - circulate on "
                      "Honor Club and PWG's releases. No film roles, autobiography or podcast could "
                      "be verified, so none are listed."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated the way the sources actually state them — starting with the reign "
             "the 22 seconds erased from memory.",
        stats=[
            ("188", "Day Universal reign"),
            ("22",  "Seconds at Fastlane"),
            ("5.0", "Stars at WrestleMania 39"),
        ],
        rows=[
            dict(name="188 days as Universal Champion",
                 sub="August 29, 2016 to March 5, 2017 - the longest reign in the title's short "
                     "history at the time, won in a fatal four-way and defended through the Raw "
                     "main-event scene of that winter. The 22-second Goldberg loss ended it; it did "
                     "not define it."),
            dict(name="Pinned John Cena clean in his first main-roster match",
                 sub="Elimination Chamber, May 31, 2015, eleven days after his main-roster debut "
                     "confrontation - an arrival WWE has never quite repeated for anyone since."),
            dict(name="Beat Sami Zayn for the NXT Championship 62 days after turning on him",
                 sub="TakeOver: Rival, February 11, 2015, by referee stoppage - the fastest "
                     "signing-to-champion arc NXT had produced, at 92 days from his December debut."),
            dict(name="Wrestled Steve Austin's first match in 19 years",
                 sub="WrestleMania 38 Night 1, April 2, 2022, No Holds Barred in Dallas. He lost, "
                     "which was the point; being chosen for it was the honour."),
            dict(name="A five-star WrestleMania main event",
                 sub="Night 1 of WrestleMania 39, April 1, 2023, winning the Undisputed Tag Team "
                     "Championship with Zayn from The Usos, as Observer round-ups reproduce the "
                     "rating."),
            dict(name="Three United States Championship reigns in one calendar year",
                 sub="2017, all involving Chris Jericho and AJ Styles - including losing the title "
                     "at a non-televised Madison Square Garden house show on July 7, one of the rare "
                     "modern off-TV title changes."),
            dict(name="Returned from neck and spinal surgery after 17 months",
                 sub="Injury announced April 4, 2025; returned August 2, 2026 in the SummerSlam "
                     "Night 2 four-way and won it, pinning Zayn with a Stunner. CBS Sports framed "
                     "the injury as one that had threatened his career outright."),
            dict(name="Champion in ROH, PWG and IWS before WWE",
                 sub="ROH World Champion 2012-13, three-time PWG World Champion, three-time IWS "
                     "World Heavyweight Champion - the resume that made the 2014 signing overdue "
                     "rather than a gamble."),
        ],
        footnote=("Deliberately absent: a career win-loss total, because no verified figure exists; "
                  "a result for the August 28, 2026 contender triple threat, which ended with no "
                  "decision; and any date for a Punk rematch or an Owens-Zayn match, because none "
                  "was announced as of August 31, 2026."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography",
             href="https://en.wikipedia.org/wiki/Kevin_Owens"),
        dict(k="CBS Sports", v="The SummerSlam 2026 return after the neck injury",
             href="https://www.cbssports.com/wwe/news/kevin-owens-return-wwe-summerslam-2026/"),
        dict(k="F4W/WON", v="The August 21 title match and Zayn's belt shot",
             href="https://www.f4wonline.com/news/wwe/result-cm-punk-vs-kevin-owens-wwe-title-match-smackdown/"),
        dict(k="Last Word on Sports", v="The August 28 contender-match chaos",
             href="https://lastwordonsports.com/prowrestling/2026/08/24/wwe-smackdown-spoilers-8-28-new-undisputed-wwe-champion-1-contender-crowned/"),
        dict(k="TheSportster", v="Observer ratings round-up",
             href="https://www.thesportster.com/wrestling/kevin-owens-highest-rated-dave-meltzer/"),
        dict(k="SmackDown Hotel", v="SummerSlam 2026 full results",
             href="https://www.thesmackdownhotel.com/events-results/ppv-special/wwe-summerslam-2026"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="What happened to Kevin Owens&rsquo; neck, and how long was he out?",
            a="On April 4, 2025 he announced neck and spinal cord injuries requiring surgery, which "
              "pulled him from WrestleMania 41 and shut down his feud with Sami Zayn mid-arc. His "
              "last match before the layoff was the unsanctioned win over Zayn at Elimination "
              "Chamber in Toronto on March 1, 2025; his first match back was the SummerSlam Night 2 "
              "fatal four-way on August 2, 2026 &mdash; roughly <b>seventeen months</b> without "
              "performing. He won it, and told the post-show he had no intention of wrestling "
              "carefully despite medical advice to protect the rebuilt neck.",
            q_ld="What happened to Kevin Owens' neck and how long was he out of WWE?",
            a_ld="Kevin Owens announced on April 4, 2025 that he had neck and spinal cord injuries "
                 "requiring surgery, which removed him from WrestleMania 41. His last match before "
                 "the injury was an unsanctioned match he won against Sami Zayn at Elimination "
                 "Chamber in Toronto on March 1, 2025. He returned after approximately seventeen "
                 "months on August 2, 2026, winning a fatal four-way at SummerSlam Night 2 in "
                 "Minneapolis to become No. 1 contender to the Undisputed WWE Championship."),
        dict(
            q="Why did Kevin Owens lose the title match to CM Punk in August 2026?",
            a="Because of Sami Zayn. On the August 21, 2026 SmackDown, Owens hit Punk with a Stunner "
              "for a near-fall; Zayn then urged him to use the championship belt as a weapon, and "
              "when Owens refused, <b>Zayn hit Owens with the belt himself</b>. Punk followed with "
              "the Go To Sleep and pinned him. Zayn attacked both men afterward and declared the "
              "title rightfully his. The August 28 triple threat to re-decide the No. 1 contender "
              "&mdash; Owens, Gunther, Finn Balor &mdash; collapsed when Zayn took out the referee, "
              "leaving Owens pinning Gunther with nobody to count.",
            q_ld="Why did Kevin Owens lose his Undisputed WWE Championship match against CM Punk?",
            a_ld="Kevin Owens lost to CM Punk on the August 21, 2026 SmackDown because of "
                 "interference by Sami Zayn. After Owens refused Zayn's urging to use the "
                 "championship belt as a weapon, Zayn struck Owens with the belt, and Punk "
                 "capitalized with a Go To Sleep for the pinfall. Zayn then attacked both Owens and "
                 "Punk and claimed the title was rightfully his. A No. 1 contender triple threat "
                 "between Owens, Gunther and Finn Balor on the August 28 SmackDown ended without a "
                 "winner after Zayn's further interference."),
        dict(
            q="Was Kevin Owens really Universal Champion for only 22 seconds?",
            a="No &mdash; that is the loss, not the reign. Owens held the WWE Universal Championship "
              "for <b>188 days</b>, from the August 29, 2016 Raw (a fatal four-way over Seth "
              "Rollins, Big Cass and Roman Reigns, decided by Triple H) to Fastlane on March 5, "
              "2017, where <b>Goldberg beat him in 22 seconds</b>. At the time it was the longest "
              "reign the Universal title had had. The 22 seconds belong to the ending WWE booked "
              "for it, and they are usually quoted with the reign amputated.",
            q_ld="How long was Kevin Owens' Universal Championship reign?",
            a_ld="Kevin Owens held the WWE Universal Championship for 188 days, from August 29, 2016, "
                 "when he won a fatal four-way on Raw against Seth Rollins, Big Cass and Roman "
                 "Reigns with help from Triple H, until March 5, 2017, when Goldberg defeated him at "
                 "Fastlane in 22 seconds. The 22-second figure refers only to the length of the "
                 "losing match, not the reign, which was the longest in the title's history at the "
                 "time."),
        dict(
            q="What is Kevin Owens&rsquo; history with Sami Zayn?",
            a="The longest continuous story in modern wrestling: friends from the Montreal indies "
              "since 2002-03, ROH tag champions in 2008, enemies in ROH&rsquo;s bloodiest feud of "
              "the early 2010s, and the same cycle in WWE &mdash; Owens turned on him in NXT in "
              "December 2014, beat him for the NXT title, warred with him through 2016-17, reunited "
              "to win the WrestleMania 39 Night 1 main event in 2023, and beat him in an "
              "unsanctioned match in March 2025. Every betrayal was Owens&rsquo;s &mdash; until "
              "August 21, 2026, when Zayn hit him with the title belt. The next chapter writes "
              "itself; WWE had not booked it as of August 31, 2026.",
            q_ld="What is the history between Kevin Owens and Sami Zayn?",
            a_ld="Kevin Owens and Sami Zayn have been friends and rivals since meeting on the "
                 "Montreal independent scene around 2002-03. They won the ROH World Tag Team "
                 "Championship together in 2008, feuded violently in ROH from 2010 to 2012, and "
                 "repeated the cycle in WWE: Owens turned on Zayn in NXT in December 2014, took the "
                 "NXT Championship from him in February 2015, feuded with him through 2016 and "
                 "2017, won the Undisputed WWE Tag Team Championship with him in the main event of "
                 "WrestleMania 39 Night 1 in 2023, and defeated him in an unsanctioned match on "
                 "March 1, 2025. On August 21, 2026, Zayn betrayed Owens for the first time, "
                 "striking him with the championship belt and costing him his title match against "
                 "CM Punk."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Kevin Yanick Steen"),
        dict(label="Born", value="May 7, 1984", sub="Saint-Jean-sur-Richelieu, Quebec &middot; "
                                                    "raised in Marieville &middot; age 42"),
        dict(label="Billed from", value="Marieville, Quebec, Canada"),
        dict(label="Height", value="6&#8242;0&#8243;", sub="183 cm"),
        dict(label="Weight", value="266 lb", sub="121 kg (billed)"),
        dict(label="Debut", value="May 7, 2000", sub="his sixteenth birthday, in Quebec"),
        dict(label="Trained by", value="Serge Jodoin &middot; Jacques Rougeau &middot; Terry Taylor"),
        dict(label="Ring names", value="Kevin Steen &rarr; Kevin Owens",
             sub="2000&ndash;14 &middot; 2014&ndash;present &mdash; Owens honours his son, named "
                 "for Owen Hart"),
        dict(label="Signature", value="Stunner &middot; Pop-up powerbomb &middot; Package "
                                      "piledriver (indies) &middot; Frog splash"),
        dict(label="Brand", value="SmackDown"),
        dict(label="Also known as", value="The Prizefighter &middot; KO &middot; Mr. Wrestling "
                                          "(as Steen)"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1984-05-07",
    bornplace="Saint-Jean-sur-Richelieu, Quebec, Canada",
    nationality="Canada",
    height_cm=183,
    weight_kg=121,
    ld=dict(
        alternateName=["Kevin Yanick Steen", "Kevin Steen", "The Prizefighter", "KO"],
        award=["WWE Universal Championship (1 reign, 188 days)",
               "WWE United States Championship (3 reigns)",
               "WWE Intercontinental Championship (2 reigns)",
               "Undisputed WWE Tag Team Championship (1 reign, with Sami Zayn)",
               "NXT Championship (1 reign)",
               "ROH World Championship (1 reign, as Kevin Steen)",
               "ROH World Tag Team Championship (1 reign, with El Generico)",
               "PWG World Championship (3 reigns)",
               "PWG World Tag Team Championship (3 reigns)",
               "IWS World Heavyweight Championship (3 reigns)",
               "CZW Iron Man Championship (1 reign)"],
        knowsAbout=["Professional wrestling", "WWE", "NXT", "Ring of Honor", "Pro Wrestling "
                    "Guerrilla", "Championship wrestling"],
        description="Kevin Owens, born Kevin Yanick Steen in Saint-Jean-sur-Richelieu, Quebec, is a "
                    "Canadian professional wrestler signed to WWE. He held the WWE Universal "
                    "Championship for 188 days in 2016-17, won the Undisputed WWE Tag Team "
                    "Championship with Sami Zayn in the main event of WrestleMania 39 Night 1, and "
                    "wrestled Steve Austin's first match in 19 years at WrestleMania 38. After neck "
                    "and spinal surgery sidelined him for seventeen months, he returned at "
                    "SummerSlam 2026, won a No. 1 contender four-way, and lost his title match "
                    "against CM Punk on August 21, 2026 after interference by Zayn.",
        sameAs=["https://en.wikipedia.org/wiki/Kevin_Owens",
                "https://www.wwe.com/superstars/kevin-owens"],
    ),
)
