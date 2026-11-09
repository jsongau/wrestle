# -*- coding: utf-8 -*-
"""Owen Hart - dossier data.

Built from data/owen-hart.md (web-verified November 9, 2026). Sources: Wikipedia (Owen Hart; the
Intercontinental, European and 1971-2010 World Tag Team title lists; the event pages for Survivor
Series 1993, Royal Rumble 1994, WrestleMania X, King of the Ring 1994, SummerSlam 1994, Canadian
Stampede, SummerSlam 1997, WrestleMania XIV, Over the Edge 1998, SummerSlam 1998, WrestleMania XV,
Over the Edge 1999; Owen Hart Cup; Slammy Award; Dark Side of the Ring), F4W, Wrestling Inc,
TJR Wrestling, Sports Illustrated, CBS Sports, Bleacher Report, the Owen Hart Foundation and the
Calgary Foundation. Every record row carries a day-precision date from those sources.

Memorial page. Owen Hart died May 23, 1999. The status line describes legacy only. The death is
stated plainly (date, place, a fall during a stunt entrance) with no graphic detail. The fall
height differs between sources (78 ft vs about 90 ft) and is deliberately not published.

Harvest audit: the old page claimed Owen won the Intercontinental title at SummerSlam 1997 (Austin
won it) and listed an Over the Edge 1998 tag title win with Jeff Jarrett over Austin (that show was
a Nation vs DX six-man). Both are corrected. Its "3-3-0, 50%" record block was a placeholder and is
gone.

Deliberate omissions:
  * No career win-loss total. None is published or verifiable.
  * No walk-out theme band. No entrance-theme track title and streaming link could be verified.
  * No social links. None existed in his lifetime.
  * No "Right Now" pulse. He died in 1999; legacy items live in the career, media and FAQ sections.
  * USWA Unified World Heavyweight reign (1993) is listed without a date, which was not verified.

Generator workarounds (remove when build_dossier.py is fixed):
  * "Over the Edge" in section text carries a U+2060 word joiner inside "Edge". Without it the
    prose autolinker links the word Edge to /wrestlers/edge/.
  * Both Bret Hart signature cards carry url="/wrestlers/bret-hart/". Without it the resolver
    matches the bare alias "hart" plus the "wm" key and links the WrestleMania X card to
    /matches/bret-hart-vs-austin-wm13/, a different match.
"""

ROWS = [
    dict(result="W", date="1988-05-27", promo="NJPW", landmark=True,
         event="New Japan, Sendai", opponent="Hiroshi Hase",
         stip="Singles. Champion at 23", title="IWGP Junior Heavyweight Championship"),
    dict(result="L", date="1988-06-24", promo="NJPW",
         event="New Japan", opponent="Shiro Koshinaka",
         stip="Singles. The reign ends after 28 days", title="IWGP Junior Heavyweight Championship"),
    dict(result="L", date="1989-04-02", promo="WWF",
         event="WrestleMania V, Atlantic City", opponent="Mr. Perfect",
         stip="Singles, as the Blue Blazer", title=""),
    dict(result="L", date="1991-05-29", promo="IND",
         event="Naucalpan, Mexico", opponent="El Canek",
         stip="Mask vs mask. The Blue Blazer mask is lost", title=""),
    dict(result="W", date="1992-04-05", promo="WWF",
         event="WrestleMania VIII, Indianapolis", opponent="Skinner",
         stip="Singles", title=""),
    dict(result="W", date="1993-11-24", promo="WWF", landmark=True, type="tag",
         event="Survivor Series, Boston Garden", opponent="Shawn Michaels & his Knights",
         stip="Hart family elimination match. Owen is eliminated after colliding with Bret; the feud starts",
         title=""),
    dict(result="L", date="1994-01-22", promo="WWF", landmark=True, type="tag",
         event="Royal Rumble, Providence", opponent="The Quebecers",
         stip="With Bret. Stopped on Bret's knee injury; Owen kicks the leg afterward", title="WWF Tag Team Championship"),
    dict(result="W", date="1994-03-20", promo="WWF", landmark=True,
         event="WrestleMania X, Madison Square Garden", opponent="Bret Hart",
         stip="The opener. Clean pin of his brother in 20:21", title=""),
    dict(result="W", date="1994-06-19", promo="WWF",
         event="King of the Ring, Baltimore", opponent="Tatanka",
         stip="Tournament quarterfinal", title=""),
    dict(result="W", date="1994-06-19", promo="WWF",
         event="King of the Ring, Baltimore", opponent="The 1-2-3 Kid",
         stip="Tournament semifinal, Sharpshooter", title=""),
    dict(result="W", date="1994-06-19", promo="WWF", landmark=True,
         event="King of the Ring, Baltimore", opponent="Razor Ramon",
         stip="Tournament final. Crowned the King of Harts", title="King of the Ring"),
    dict(result="L", date="1994-08-29", promo="WWF", landmark=True,
         event="SummerSlam, Chicago", opponent="Bret Hart",
         stip="Steel cage, 32:22. Five stars from the Wrestling Observer", title="WWF Championship"),
    dict(result="W", date="1995-04-02", promo="WWF", landmark=True, type="tag",
         event="WrestleMania XI, Hartford", opponent="The Smoking Gunns",
         stip="With Yokozuna, the mystery partner", title="WWF Tag Team Championship"),
    dict(result="W", date="1996-09-22", promo="WWF", landmark=True, type="tag",
         event="In Your House: Mind Games, Philadelphia", opponent="The Smoking Gunns",
         stip="With the British Bulldog. A 246-day reign follows", title="WWF Tag Team Championship"),
    dict(result="L", date="1997-02-26", promo="WWF",
         event="Raw, Berlin", opponent="British Bulldog",
         stip="Tournament final for the new title", title="WWF European Championship"),
    dict(result="W", date="1997-04-28", promo="WWF", landmark=True,
         event="Raw, Omaha", opponent="Rocky Maivia",
         stip="Singles. First Intercontinental title", title="WWF Intercontinental Championship"),
    dict(result="L", date="1997-05-26", promo="WWF", type="tag",
         event="Raw", opponent="Stone Cold Steve Austin & Shawn Michaels",
         stip="With the British Bulldog", title="WWF Tag Team Championship"),
    dict(result="W", date="1997-07-06", promo="WWF", landmark=True, type="tag",
         event="Canadian Stampede, Calgary", opponent="Austin, Shamrock, Goldust & the Legion of Doom",
         stip="Ten-man tag for the Hart Foundation. Owen scores the winning roll-up at home", title=""),
    dict(result="L", date="1997-08-03", promo="WWF", landmark=True,
         event="SummerSlam, East Rutherford", opponent="Stone Cold Steve Austin",
         stip="A botched piledriver injures Austin's neck; Austin wins with a roll-up", title="WWF Intercontinental Championship"),
    dict(result="W", date="1997-10-05", promo="WWF",
         event="Badd Blood, St. Louis", opponent="Faarooq",
         stip="Tournament final for the vacant title", title="WWF Intercontinental Championship"),
    dict(result="L", date="1997-11-09", promo="WWF",
         event="Survivor Series, Montreal", opponent="Stone Cold Steve Austin",
         stip="Singles, on the night of the Montreal Screwjob", title="WWF Intercontinental Championship"),
    dict(result="W", date="1998-01-20", promo="WWF",
         event="Raw taping, Davis, California", opponent="Goldust",
         stip="Goldust dressed as Triple H. WWE dates the reign from the January 22 air date",
         title="WWF European Championship"),
    dict(result="L", date="1998-03-29", promo="WWF",
         event="WrestleMania XIV, Boston", opponent="Triple H",
         stip="Singles, Chyna handcuffed to Sgt. Slaughter", title="WWF European Championship"),
    dict(result="W", date="1998-05-31", promo="WWF", type="tag",
         event="Over the Edge, Milwaukee", opponent="Triple H, Billy Gunn & Road Dogg",
         stip="Nation vs DX six-man. Owen pins Triple H with his own Pedigree", title=""),
    dict(result="L", date="1998-08-30", promo="WWF",
         event="SummerSlam, Madison Square Garden", opponent="Ken Shamrock",
         stip="Lion's Den match. Taps to the ankle lock", title=""),
    dict(result="W", date="1999-01-25", promo="WWF", landmark=True, type="tag",
         event="Raw Is War, Phoenix", opponent="Ken Shamrock & the Big Boss Man",
         stip="With Jeff Jarrett. His fourth tag title reign", title="WWF Tag Team Championship"),
    dict(result="W", date="1999-03-28", promo="WWF", type="tag",
         event="WrestleMania XV, Philadelphia", opponent="Test & D'Lo Brown",
         stip="With Jeff Jarrett. Title retained", title="WWF Tag Team Championship"),
    dict(result="L", date="1999-03-30", promo="WWF", type="tag",
         event="Raw taping", opponent="Kane & X-Pac",
         stip="With Jeff Jarrett. Aired April 5, 1999", title="WWF Tag Team Championship"),
]

DATA = dict(
    slug="owen-hart",
    name="Owen Hart",
    realname="Owen James Hart",
    epithet="The King of Harts",
    hook="Record & Legacy",
    art="owen-hart",

    meta_desc=("Owen Hart, 1965-1999: the 1994 King of the Ring, four WWF tag title reigns, two "
               "Intercontinental reigns, the WrestleMania X win over Bret Hart, and the legacy "
               "carried by the Owen Hart Foundation and AEW's Owen Hart Cup."),
    og_desc=("The youngest Hart brother: IWGP junior champion at 23, the clean WrestleMania X win "
             "over Bret, King of the Ring 1994, tag gold with Yokozuna, the British Bulldog and Jeff "
             "Jarrett. He died May 23, 1999, at Over the Edge. He was 34."),
    tw_desc="Owen Hart, 1965-1999: WrestleMania X, King of the Ring 1994, and a legacy that outlived WWE.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1986",
    height_imp="5&#8242;10&#8243;",
    weight_lb="227",
    vitals_tagline="King of Harts",
    support_note="Foundation &middot; Tournament &middot; Read",
    sp_items=[
        dict(ic="OHF", title="Owen Hart Foundation", sub="Scholarships and home ownership, Calgary",
             tag="Give", charity=True, href="https://owenhartfoundation.org/"),
        dict(ic="AEW", title="Owen Hart Cup", sub="The annual AEW tournament in his name",
             tag="Read", href="https://en.wikipedia.org/wiki/Owen_Hart_Cup"),
        dict(ic="DSR", title="Dark Side of the Ring", sub="The Final Days of Owen Hart, Vice, 2020",
             tag="Watch", href="https://en.wikipedia.org/wiki/Dark_Side_of_the_Ring"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Rocket &middot; The Blue Blazer &middot; The King of Harts",
    hero_tag="Calgary, Alberta &middot; <em>Stampede &middot; New Japan &middot; WWF &middot; 1986&ndash;1999</em>",
    now_label="1965&ndash;1999",
    now_bold="Died May 23, 1999, at 34",
    now_tail=(" &middot; after a fall during a stunt entrance at Over the Edge in Kansas City &middot; "
              "remembered through the Owen Hart Foundation and AEW&rsquo;s Owen Hart Cup"),
    hstats=[
        dict(value="4",    x=True,  label="WWF Tag Team reigns"),
        dict(value="2",    x=True,  label="Intercontinental reigns"),
        dict(value="1994", x=False, label="King of the Ring"),
        dict(value="1988", x=False, label="IWGP Junior Champion"),
    ],
    ghost_link="From the Hart Dungeon to WrestleMania X",
    vlabel="Est. 1986 &middot; Calgary, Alberta",
    mono="OH",

    # ---------------------------------------------------------------- 01 overview
    correction=3,
    overview=[
        "<b>Owen Hart</b> was the youngest of the twelve children of Stu and Helen Hart, trained in "
        "his father&rsquo;s Dungeon in Calgary. Born Owen James Hart on May 7, 1965, he debuted for Stampede Wrestling on May 30, "
        "1986, won the Stampede International Tag Team titles with Ben Bassarab that year, and was "
        "named Pro Wrestling Illustrated&rsquo;s Rookie of the Year in 1987. The Wrestling Observer "
        "named him Best Flying Wrestler in 1987 and again in 1988. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">23</span>'
        '<span class="pull-cap">his age when he beat Hiroshi Hase for the IWGP Junior Heavyweight '
        'Championship in Sendai, May 27, 1988</span></span>'
        "New Japan saw it first. On May 27, 1988 in Sendai he beat Hiroshi Hase for the IWGP Junior "
        "Heavyweight Championship, and held it until Shiro Koshinaka took it on June 24. The WWF "
        "signed him that summer and put him under a mask as the Blue Blazer. The character never "
        "broke through, and he lost the mask to El Canek in Mexico on May 29, 1991.",

        "The break came from inside the family. At Survivor Series on November 24, 1993, Owen ran "
        "into Bret on the apron, was eliminated, and blamed his brother. At the Royal Rumble on "
        "January 22, 1994, after Bret&rsquo;s knee gave out in their tag title match against the "
        "Quebecers, Owen kicked the injured leg and left him lying in the ring. At WrestleMania X on "
        "March 20, 1994 in Madison Square Garden, he pinned Bret clean in the opener after 20:21. "
        "Dave Meltzer rated it four and three-quarter stars. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">5&#9733;</span>'
        '<span class="pull-cap">the Wrestling Observer grade for the SummerSlam 1994 steel cage '
        'match against Bret</span></span>'
        "He won the King of the Ring on June 19, 1994 in Baltimore, beating Tatanka, the 1-2-3 Kid "
        "and Razor Ramon in one night, and crowned himself the King of Harts. The feud peaked in a "
        "32-minute steel cage match for the WWF Championship at SummerSlam on August 29, 1994. Bret "
        "won it. Meltzer gave it five stars.",

        "Owen spent the rest of the decade in the WWF title picture, much of it in tag teams. He won the WWF Tag Team Championship four times: with Yokozuna at "
        "WrestleMania XI on April 2, 1995 (the titles changed hands and came back to them that "
        "September), with the British Bulldog on September 22, 1996, and with Jeff Jarrett on "
        "January 25, 1999. He won the Intercontinental Championship from Rocky Maivia, later known "
        "as The Rock, on April 28, 1997, and the vacant title again at Badd Blood on October 5, 1997. "
        "He held the European Championship in early 1998. In 1997 he stood with Bret, the Bulldog, "
        "Jim Neidhart and Brian Pillman in the reformed Hart Foundation, and scored the winning pin "
        "of the Canadian Stampede ten-man tag in Calgary on July 6. After Bret left in November "
        "1997 he stayed, and in 1998 he joined the Nation of Domination.",

        "One correction. The old version of this page said Owen won the Intercontinental title at "
        "SummerSlam 1997 when he injured Stone Cold Steve Austin. He did not. On August 3, 1997 in "
        "East Rutherford, Owen was the champion. A piledriver went wrong and hurt Austin&rsquo;s "
        "neck, and Austin, who could barely move, won the title with a roll-up. Owen got the belt "
        "back only after Austin vacated it, by beating Faarooq in the October tournament final, "
        "and Austin took it from him again at Survivor Series in Montreal on November 9, 1997.",

        "On May 23, 1999, at Kemper Arena in Kansas City, Missouri, Owen Hart died after a fall "
        "during a stunt entrance at the WWF&rsquo;s Over the Edge pay-per-view. He was to be lowered "
        "into the ring from the rafters as the Blue Blazer for an Intercontinental title match with "
        "The Godfather. He was 34. Television viewers did not see the fall, and the show continued. "
        "His family sued, and the WWF settled for US$18 million on November 2, 2000. His widow, "
        "Martha Hart, used part of the settlement to set up the Owen Hart Foundation, which funds "
        "scholarships and a home ownership program in Calgary. Since 2022 AEW has run the Owen Hart "
        "Cup with the foundation. He is not in the WWE Hall of Fame, and Martha Hart has said he "
        "never will be.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["NJPW", "WWF", "IND"],
        promo_labels={"NJPW": "New Japan", "WWF": "WWF", "IND": "Mexico"},
        stats=[
            ("4&times;",  "WWF Tag Team Champion"),
            ("2&times;",  "Intercontinental Champion"),
            ("1&times;",  "European Champion"),
            ("1994",      "King of the Ring"),
            ("4.75",      "WrestleMania X, Observer"),
            ("5.0",       "SummerSlam 1994 cage"),
        ],
        lead=("Twenty-eight documented bouts, from the 1988 IWGP junior title win in Sendai to the "
              "last tag title loss in March 1999. Every title change he was part of is here, with "
              "the PPV matches that defined him. This is a selected ledger, not a career count. No "
              "verified win&ndash;loss total exists, and none is published. Two rows are dated to "
              "the taping, with the air date noted. Filter by match type, tap any column header to "
              "sort, and turn spoilers on to see results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the reputation rests on. The two Bret matches carry Wrestling "
                    "Observer grades. Where the rating shows a dash, no grade was verified, so "
                    "none is claimed."),
    signature=[
        dict(rating="5.0", event="SummerSlam 1994, Chicago", opponent="Bret Hart",
             stip="Steel cage for the WWF Championship, 32:22", url="/wrestlers/bret-hart/"),
        dict(rating="4.75", event="WrestleMania X, Madison Square Garden", opponent="Bret Hart",
             stip="The opener. Owen wins clean", url="/wrestlers/bret-hart/"),
        dict(rating="&mdash;", event="King of the Ring 1994, Baltimore", opponent="Razor Ramon",
             stip="Tournament final. Three wins in one night"),
        dict(rating="&mdash;", event="WrestleMania XI, Hartford", opponent="The Smoking Gunns",
             stip="Tag titles, with Yokozuna revealed as the mystery partner"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("4&times;", "WWF Tag Team"),
            ("2&times;", "Intercontinental"),
            ("1&times;", "European"),
            ("1&times;", "IWGP Junior Heavyweight"),
        ],
        lead=("Four tag reigns with three partners, two Intercontinental reigns, the European title "
              "and a junior heavyweight title in Japan before he turned 24. Dates come from the "
              "published title histories; where WWE dates a reign from the air date, both are "
              "given."),
        rows=[
            dict(ic="T", name="WWF World Tag Team Championship", count="4",
                 sub="With Yokozuna: won April 2, 1995 at WrestleMania XI from the Smoking Gunns, "
                     "175 days. The titles went to Diesel and Shawn Michaels at In Your House on "
                     "September 24, 1995, with the Bulldog standing in for Owen, then were handed "
                     "back on Raw the next night and lost to the Gunns &middot; With the British "
                     "Bulldog: September 22, 1996 to May 26, 1997, 246 days &middot; With Jeff "
                     "Jarrett: January 25, 1999 to the March 30 taping that aired April 5"),
            dict(ic="I", name="WWF Intercontinental Championship", count="2",
                 sub="April 28, 1997, def. Rocky Maivia on Raw in Omaha; lost to Stone Cold Steve "
                     "Austin at SummerSlam, August 3 &middot; October 5, 1997, def. Faarooq in the "
                     "Badd Blood tournament final; lost to Austin at Survivor Series in Montreal, "
                     "November 9"),
            dict(ic="E", name="WWF European Championship", count="1",
                 sub="Won on the Raw taped January 20, 1998 (WWE dates it January 22) from Goldust "
                     "dressed as Triple H; lost to Triple H on March 16, 1998. He had lost the first "
                     "tournament final for the title to the British Bulldog in Berlin, February 26, "
                     "1997"),
            dict(ic="J", name="IWGP Junior Heavyweight Championship", count="1",
                 sub="May 27, 1988, def. Hiroshi Hase in Sendai; lost to Shiro Koshinaka, June 24, "
                     "1988"),
            dict(ic="K", name="King of the Ring", count="1",
                 sub="June 19, 1994, Baltimore: Tatanka, the 1-2-3 Kid, then Razor Ramon in the "
                     "final"),
            dict(ic="U", name="USWA Unified World Heavyweight Championship", count="1",
                 sub="Won from Papa Shango in 1993, during the WWF and USWA crossover. Date not "
                     "verified in this pass"),
            dict(ic="S", name="Stampede International Tag Team Championship", count="1",
                 sub="With Ben Bassarab, 1986, in his debut year"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        lead=('Owen was a natural partner. His family stable has its own page: '
              '<a class="opp-link" href="/tag-teams/the-hart-foundation/">The Hart Foundation</a>.'),
        cards=[
            dict(era="WWF &middot; 1992",
                 name="New Foundation and High Energy",
                 members="Owen Hart with Jim Neidhart, then Koko B. Ware",
                 desc=("As The Rocket he teamed with Jim Neidhart and beat the Orient "
                       "Express at the January 1992 Royal Rumble, then formed High Energy with Koko "
                       "B. Ware. The team lost to the Headshrinkers at Survivor Series 1992 and was "
                       "dropped early in 1993.")),
            dict(era="WWF &middot; 1995",
                 name="Owen Hart and Yokozuna",
                 members="Owen Hart, Yokozuna",
                 desc=("Owen revealed Yokozuna as his mystery partner at WrestleMania XI on April 2, "
                       "1995, and they beat the Smoking Gunns for the tag titles. The reign lasted "
                       "175 days before the September title switch and reversal.")),
            dict(era="WWF &middot; 1996&ndash;1997",
                 name="Owen Hart and the British Bulldog",
                 members="Owen Hart, British Bulldog",
                 desc=("Tag champions for 246 days from September 22, 1996. "
                       "During the reign the Bulldog became the first European Champion, beating "
                       "Owen in the Berlin final, and Owen became Intercontinental Champion. Austin "
                       "and Shawn Michaels ended it on May 26, 1997.")),
            dict(era="WWF &middot; 1997",
                 name="The Hart Foundation",
                 members="Bret Hart, Owen Hart, British Bulldog, Jim Neidhart, Brian Pillman",
                 desc=("Bret stopped a Bulldog vs Owen European title match on March 31, 1997 and "
                       "rebuilt the family stable. It headlined Canadian "
                       "Stampede in Calgary on July 6, 1997, where Owen pinned for the win, and "
                       "it broke up after Montreal.")),
            dict(era="WWF &middot; 1998",
                 name="Nation of Domination",
                 members="The Rock, Owen Hart, D'Lo Brown, Kama Mustafa, Mark Henry",
                 desc=("After turning on Ken Shamrock, Owen joined The Rock's Nation. At Over the "
                       "Edge on May 31, 1998 he pinned Triple H with a Pedigree to win the Nation vs "
                       "DX six-man. DX mocked him as the nugget, and the chant stuck.")),
            dict(era="WWF &middot; 1998&ndash;1999",
                 name="Owen Hart and Jeff Jarrett",
                 members="Owen Hart, Jeff Jarrett, with Debra",
                 desc=("Paired after SummerSlam 1998, they won the tag titles from Ken Shamrock and "
                       "the Big Boss Man on January 25, 1999, kept them at WrestleMania XV, and lost "
                       "them to Kane and X-Pac at the March 30 taping.")),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead=("Six looks across eleven WWF years: the mask he never wanted, the rocket, the crown, "
              "the family stable, the Nation, and the mask again."),
        cards=[
            dict(mono="BB", era="WWF &middot; 1988&ndash;1991", name="The Blue Blazer",
                 desc=("First pitched as the Blue Angel. A masked high flyer who lost to Mr. Perfect "
                       "at WrestleMania V and never got past the midcard. The mask came off for good "
                       "in a mask vs mask loss to El Canek in Naucalpan on May 29, 1991.")),
            dict(mono="RK", era="WWF &middot; 1991&ndash;1994", name="The Rocket",
                 desc=("The babyface flyer of the New Foundation and High Energy years. He dropped the "
                       "name after winning the 1994 King of the Ring.")),
            dict(mono="KH", era="WWF &middot; 1994&ndash;1997", name="The King of Harts",
                 desc=("The jealous younger brother, in pink and black, with Bret's Sharpshooter. He "
                       "beat Bret at WrestleMania X, crowned himself after King of the Ring, and tricked "
                       "their mother into throwing in the towel at Survivor Series 1994.")),
            dict(mono="HF", era="WWF &middot; 1997", name="Hart Foundation Owen",
                 desc=("The family stable year. Austin attacked him while he sang the Canadian anthem "
                       "the night after Canadian Stampede, and the feud ran all year. Afterward he wore an Owen 3:16 shirt that "
                       "read I Just Broke Your Neck.")),
            dict(mono="BH", era="WWF &middot; 1997&ndash;1998", name="The Black Hart",
                 desc=("The Lone Hart and Black Hart names covered the months after Montreal, when he "
                       "was the last Hart left in the company. In 1998 he turned on Shamrock and "
                       "joined the Nation.")),
            dict(mono="BB", era="WWF &middot; 1998&ndash;1999", name="The Blue Blazer, revived",
                 desc=("The mask came back as a comedy superhero who parodied Hulk Hogan's vitamins "
                       "and prayers line and drew unintended cheers. It was the character he was playing on May 23, "
                       "1999.")),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="From the Dungeon to Sendai, to Madison Square Garden, to the foundation in his name.",
        rows=[
            dict(year="1986", title="Debut in Stampede Wrestling",
                 desc=("Debuts May 30 in his father's promotion and wins the Stampede International "
                       "Tag Team titles with Ben Bassarab.")),
            dict(year="1987", title="Rookie of the Year",
                 desc=("PWI Rookie of the Year. The Wrestling Observer names him Best Flying Wrestler, "
                       "and does again in 1988.")),
            dict(year="1988", title="IWGP Junior Champion, then the WWF",
                 desc=("Beats Hiroshi Hase for the IWGP Junior Heavyweight title in Sendai on May 27 "
                       "and loses it to Shiro Koshinaka on June 24. Signs with the WWF that summer as "
                       "the Blue Blazer.")),
            dict(year="1991", title="WCW, Mexico, and back",
                 desc=("Appears on WCW TV from March 16 but never signs, because he will not move to "
                       "Atlanta. Loses the Blazer mask to El Canek on May 29. Returns to the WWF.")),
            dict(year="1992", title="The Rocket",
                 desc=("Wins at the Royal Rumble with Jim Neidhart and beats Skinner at WrestleMania "
                       "VIII. Teams with Koko B. Ware as High Energy.")),
            dict(year="1993", title="Survivor Series, Boston",
                 desc=("Collides with Bret on the apron and is eliminated on November 24. The "
                       "argument afterward starts the brother feud.")),
            dict(year="1994", title="The year of the King of Harts",
                 desc=("Kicks Bret's knee at the Royal Rumble, pins him at WrestleMania X on March 20, "
                       "wins King of the Ring on June 19, and loses the five-star cage match at "
                       "SummerSlam on August 29. PWI names it Feud of the Year.")),
            dict(year="1995", title="Tag champion with Yokozuna",
                 desc="Wins the WWF Tag Team titles at WrestleMania XI on April 2."),
            dict(year="1996", title="Tag champion with the Bulldog",
                 desc="Wins the titles at In Your House: Mind Games on September 22 and holds them 246 days."),
            dict(year="1997", title="Hart Foundation and two IC reigns",
                 desc=("Wins the Intercontinental title on April 28, pins for the win at Canadian "
                       "Stampede on July 6, loses the title and injures Austin at SummerSlam, wins it "
                       "back at Badd Blood, and loses it in Montreal on November 9.")),
            dict(year="1998", title="European title and the Nation",
                 desc=("Wins the European title in January and loses to Triple H at WrestleMania XIV. "
                       "Joins the Nation, loses the Lion's Den match to Shamrock at SummerSlam, and "
                       "teams with Jeff Jarrett as the Blue Blazer returns.")),
            dict(year="1999", title="Fourth tag reign, and May 23",
                 desc=("Wins the tag titles with Jarrett on January 25 and keeps them at WrestleMania "
                       "XV. Dies May 23 after a fall during a stunt entrance at Over the Edge in "
                       "Kansas City. Raw Is Owen airs from St. Louis the next night.")),
            dict(year="2000", title="Settlement",
                 desc=("The family's wrongful death suit is settled for US$18 million on November 2. "
                       "Martha Hart uses part of it to set up the Owen Hart Foundation.")),
            dict(year="2020", title="Dark Side of the Ring",
                 desc=("Vice airs The Final Days of Owen Hart on May 19. Martha Hart says she is very "
                       "pleased with it.")),
            dict(year="2022", title="The first Owen Hart Cup",
                 desc=("AEW, which announced the tournament with the foundation on September 20, 2021, "
                       "crowns Adam Cole and Dr. Britt Baker at Double or Nothing on May 29.")),
            dict(year="2026", title="Fifth edition",
                 desc=("Will Ospreay and Mercedes Moné win the 2026 tournaments at Forbidden Door on "
                       "June 28. It is Moné's second straight win.")),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="The brother first. Then the men who shared the most famous nights of his career.",
        cards=[
            dict(name="Bret Hart",
                 desc=("The brother feud ran from Survivor Series 1993 into 1995. Owen won clean in "
                       "the WrestleMania X opener (4.75 stars) and lost the SummerSlam 1994 cage match "
                       "(5 stars), and PWI made it Feud of the Year. They were reunited in the 1997 "
                       "Hart Foundation.")),
            dict(name="Stone Cold Steve Austin",
                 desc=("Austin attacked Owen during the anthem the night after Canadian Stampede. At "
                       "SummerSlam 1997 a piledriver went wrong and injured Austin's neck. Austin won "
                       "the Intercontinental title that night, and took it from Owen again in "
                       "Montreal. The Observer named the Hart Foundation vs Austin its 1997 Feud of "
                       "the Year.")),
            dict(name="Triple H",
                 desc=("Owen took the European title from Goldust dressed as Triple H in January "
                       "1998, lost it back, and lost again at WrestleMania XIV. At Over the Edge 1998 "
                       "he pinned Triple H with his own Pedigree.")),
            dict(name="Ken Shamrock",
                 desc=("Owen injured Shamrock's ankle to turn heel in spring 1998. The feud ended in "
                       "the Lion's Den at SummerSlam on August 30, 1998, where Owen tapped to the "
                       "ankle lock.")),
            dict(name="British Bulldog",
                 desc=("Tag partner for 246 days, and the man who beat him in the "
                       "first European title final in Berlin on February 26, 1997.")),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Memory",
        lead="Documentaries, games and the book his widow wrote. Verified entries only.",
        rows=[
            dict(when="1999", title="Raw Is Owen", kind="Tribute",
                 desc=("The May 24, 1999 Raw from the Kiel Center in St. Louis, given over to tributes. "
                       "It drew a 7.2 Nielsen rating.")),
            dict(when="2002", title="Broken Harts", kind="Book",
                 desc=("Martha Hart's book, The Life and Death of Owen Hart. Wikipedia gives 2002 in "
                       "its text and 2004 in its bibliography.")),
            dict(when="2002&ndash;2004", title="Legends of Wrestling II and Showdown", kind="Games",
                 desc=("Playable in Legends of Wrestling II (2002) and Showdown: Legends of Wrestling "
                       "(2004). WWF Attitude had been dedicated to him.")),
            dict(when="2015", title="Owen: Hart of Gold", kind="Film",
                 desc="Documentary released on DVD and Blu-ray on December 7, 2015 (UK) and December 8 (US)."),
            dict(when="2020", title="Dark Side of the Ring", kind="TV",
                 desc=("Season 2, Episode 10, The Final Days of Owen Hart, aired on Vice on May 19, "
                       "2020.")),
            dict(when="2023", title="AEW Fight Forever", kind="Game",
                 desc=("Released June 29, 2023. His first playable video game appearance since 2004, "
                       "through the deal with the Owen Hart Foundation.")),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The honors and records the sources support.",
        stats=[
            ("4",  "Tag title reigns"),
            ("3",  "Tag partners"),
            ("5",  "Owen Hart Cup editions"),
        ],
        rows=[
            dict(name="King of the Ring, 1994",
                 sub="Three wins in one night in Baltimore on June 19, 1994: Tatanka, the 1-2-3 Kid, Razor Ramon."),
            dict(name="Five stars against his brother",
                 sub=("The SummerSlam 1994 cage match is one of two Bret Hart matches Dave Meltzer "
                      "rated five stars. WrestleMania X got 4.75.")),
            dict(name="Feud of the Year, twice",
                 sub=("PWI for 1994, against Bret. The Wrestling Observer for 1997, as part of the "
                      "Hart Foundation against Austin.")),
            dict(name="Rookie of the Year and Best Flying Wrestler",
                 sub="PWI Rookie of the Year 1987. Wrestling Observer Best Flying Wrestler 1987 and 1988."),
            dict(name="IWGP Junior Heavyweight Champion at 23",
                 sub=("May 27, 1988 in Sendai. Wikipedia calls him the first non-Japanese holder of "
                      "the title.")),
            dict(name="Four tag reigns, three partners",
                 sub="Yokozuna (1995), the British Bulldog (1996), Jeff Jarrett (1999)."),
            dict(name="Halls of fame outside WWE",
                 sub=("Pro Wrestling Hall of Fame (2019), Tragos/Thesz (2018), Prairie Wrestling "
                      "Alliance (2010), Legends Pro Wrestling (2011), Canadian Wrestling Hall of Fame.")),
            dict(name="The Owen Hart Cup",
                 sub=("AEW's annual tournament with the Owen Hart Foundation, held every year from "
                      "2022 through 2026.")),
        ],
        footnote=("No career win-loss total is published because none can be verified. Wikipedia's "
                  "Owen Hart article credits him with three Slammy Awards; the Slammy Award list "
                  "records one, plus the 1997 Best Bow Tie award he stole on air, so no count is "
                  "given here."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Owen_Hart"),
        dict(k="Wikipedia", v="WrestleMania X, the Bret match", href="https://en.wikipedia.org/wiki/WrestleMania_X"),
        dict(k="Wikipedia", v="King of the Ring 1994", href="https://en.wikipedia.org/wiki/King_of_the_Ring_(1994)"),
        dict(k="Wikipedia", v="Over the Edge 1999", href="https://en.wikipedia.org/wiki/Over_the_Edge_(1999)"),
        dict(k="Wikipedia", v="Owen Hart Cup", href="https://en.wikipedia.org/wiki/Owen_Hart_Cup"),
        dict(k="Sports Illustrated", v="Martha Hart, May 2020",
             href="https://www.si.com/wrestling/2020/05/18/owen-hart-widow-martha-dark-side-of-the-ring"),
        dict(k="Owen Hart Foundation", v="Official site", href="https://owenhartfoundation.org/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="How did Owen Hart die?",
            a=("He died on <b>May 23, 1999</b>, at Kemper Arena in Kansas City, Missouri, after a fall "
               "during a stunt entrance at the WWF&rsquo;s Over the Edge pay-per-view. He was to be "
               "lowered into the ring from the rafters as the Blue Blazer. He was 34. Television "
               "viewers did not see the fall. His family sued, and the WWF settled for US$18 million "
               "on November 2, 2000."),
            q_ld="How did Owen Hart die?",
            a_ld=("Owen Hart died on May 23, 1999, at Kemper Arena in Kansas City, Missouri, after a "
                  "fall during a stunt entrance at the WWF Over the Edge pay-per-view, where he was to "
                  "be lowered into the ring as the Blue Blazer. He was 34. His family's lawsuit "
                  "against the WWF was settled for US$18 million on November 2, 2000.")),
        dict(
            q="Is Owen Hart in the WWE Hall of Fame?",
            a=("No. His widow, Martha Hart, has refused. In May 2020 she told "
               "Sports Illustrated: &ldquo;I&rsquo;d never want him recognized by a company responsible "
               "for his death and that has been so disrespectful to his family.&rdquo; Bret Hart has "
               "argued the other way, saying in 2018 that Owen belongs in it. He is in the Pro "
               "Wrestling Hall of Fame (2019) and several others."),
            q_ld="Is Owen Hart in the WWE Hall of Fame?",
            a_ld=("No. Owen Hart's widow, Martha Hart, has refused WWE Hall of Fame induction. In May "
                  "2020 she told Sports Illustrated she would never want him recognized by a company "
                  "she holds responsible for his death. Bret Hart has said Owen belongs in it. Owen "
                  "Hart was inducted into the Pro Wrestling Hall of Fame in 2019.")),
        dict(
            q="Did Owen Hart beat Bret Hart at WrestleMania X?",
            a=("Yes, clean. On March 20, 1994 at Madison Square Garden, Owen pinned Bret in the "
               "opening match after 20:21. Dave Meltzer rated it four and three-quarter stars. Bret "
               "won the WWF Championship from Yokozuna later the same night. Bret won the rematch, a "
               "five-star steel cage match at SummerSlam on August 29, 1994."),
            q_ld="Did Owen Hart beat Bret Hart at WrestleMania X?",
            a_ld=("Yes. Owen Hart pinned Bret Hart in the opening match of WrestleMania X at Madison "
                  "Square Garden on March 20, 1994, after 20 minutes 21 seconds. The Wrestling "
                  "Observer's Dave Meltzer rated it 4.75 stars. Bret won their steel cage rematch at "
                  "SummerSlam on August 29, 1994.")),
        dict(
            q="What is the Owen Hart Cup?",
            a=("AEW&rsquo;s annual tournament, run with the Owen Hart Foundation and announced on "
               "September 20, 2021. Winners: Adam Cole and Dr. Britt Baker (2022), Ricky Starks and "
               "Willow Nightingale (2023), Bryan Danielson and Mariah May (2024), &ldquo;Hangman&rdquo; "
               "Adam Page and Mercedes Moné (2025), and "
               '<a class="opp-link" href="/wrestlers/will-ospreay/">Will Ospreay</a> and '
               '<a class="opp-link" href="/wrestlers/mercedes-mone/">Mercedes Moné</a> (2026, at '
               "Forbidden Door on June 28)."),
            q_ld="What is the Owen Hart Cup?",
            a_ld=("The Owen Hart Cup is an annual All Elite Wrestling tournament held with the Owen "
                  "Hart Foundation, announced on September 20, 2021. Winners have been Adam Cole and "
                  "Britt Baker (2022), Ricky Starks and Willow Nightingale (2023), Bryan Danielson "
                  "and Mariah May (2024), Adam Page and Mercedes Mone (2025), and Will Ospreay and "
                  "Mercedes Mone (2026).")),
        dict(
            q="What titles did Owen Hart win?",
            a=("Four WWF Tag Team Championships (with Yokozuna, the British Bulldog and Jeff Jarrett), "
               "two Intercontinental Championships (1997), one European Championship (1998), the 1994 "
               "King of the Ring, the IWGP Junior Heavyweight Championship in New Japan (1988), the "
               "USWA Unified World Heavyweight title (1993) and the Stampede International Tag Team "
               "titles (1986). He never held a WWF world title."),
            q_ld="What championships did Owen Hart win?",
            a_ld=("Owen Hart won the WWF Tag Team Championship four times, the WWF Intercontinental "
                  "Championship twice, the WWF European Championship once, the 1994 King of the Ring "
                  "tournament, the IWGP Junior Heavyweight Championship in 1988, the USWA Unified "
                  "World Heavyweight Championship and the Stampede International Tag Team "
                  "Championship.")),
        dict(
            q="Who was the Blue Blazer?",
            a=("Owen&rsquo;s masked character. The WWF introduced it when he signed in 1988, and he "
               "lost the mask to El Canek in Mexico on May 29, 1991. The WWF revived it in 1998 "
               "as a comedy superhero. He was playing the Blue Blazer when he died at Over the Edge on "
               "May 23, 1999."),
            q_ld="Who was the Blue Blazer?",
            a_ld=("The Blue Blazer was Owen Hart's masked character in the WWF, used from 1988 until he "
                  "lost the mask to El Canek on May 29, 1991, and revived in 1998. He was "
                  "performing as the Blue Blazer at Over the Edge on May 23, 1999.")),
        dict(
            q="What happened between Owen Hart and Steve Austin at SummerSlam 1997?",
            a=("Owen defended the Intercontinental title against Austin on August 3, 1997. A "
               "piledriver went wrong and injured Austin&rsquo;s neck, leaving him temporarily unable "
               "to move. Austin recovered enough to win the title with a roll-up. Owen did not win "
               "the belt that night, which older pages, including this one, used to get wrong."),
            q_ld="What happened between Owen Hart and Steve Austin at SummerSlam 1997?",
            a_ld=("At SummerSlam on August 3, 1997, Owen Hart defended the WWF Intercontinental "
                  "Championship against Stone Cold Steve Austin. A botched piledriver injured Austin's "
                  "neck. Austin won the title with a roll-up. Owen Hart regained the vacated title at "
                  "Badd Blood on October 5, 1997.")),
        dict(
            q="Was Owen Hart in the Nation of Domination?",
            a=("Yes, in 1998. After turning on Ken Shamrock he joined The Rock&rsquo;s Nation, and at "
               "Over the Edge on May 31, 1998 he pinned Triple H with a Pedigree to win the Nation vs "
               "DX six-man. D-Generation X&rsquo;s parodies gave him the nickname nugget."),
            q_ld="Was Owen Hart in the Nation of Domination?",
            a_ld=("Yes. Owen Hart joined the Nation of Domination, led by The Rock, in 1998. At Over the "
                  "Edge on May 31, 1998, he pinned Triple H to win a six-man tag match against "
                  "D-Generation X.")),
        dict(
            q="What does the Owen Hart Foundation do?",
            a=("Martha Hart set it up with part of the wrongful death settlement. It funds ten $4,000 "
               "scholarships a year for Calgary high school students and runs the Owen Hart Home "
               "Owners Program with Momentum, which matches low-income families&rsquo; down-payment "
               "savings. The foundation says more than 100 homes have been bought through it."),
            q_ld="What does the Owen Hart Foundation do?",
            a_ld=("The Owen Hart Foundation, set up by Martha Hart with part of her wrongful death "
                  "settlement, funds annual scholarships for Calgary high school students and runs a "
                  "home ownership program with Momentum that matches down-payment savings for "
                  "low-income families. It also partners with AEW on the Owen Hart Cup.")),
        dict(
            q="Who were Owen Hart&rsquo;s tag team partners?",
            a=("His four WWF tag title reigns came with Yokozuna (1995, two reigns on the books), the "
               "British Bulldog (1996&ndash;1997) and Jeff Jarrett (1999). Earlier he teamed with Ben "
               "Bassarab in Stampede, Jim Neidhart as the New Foundation and Koko B. Ware as High "
               "Energy."),
            q_ld="Who were Owen Hart's tag team partners?",
            a_ld=("Owen Hart won the WWF Tag Team Championship with Yokozuna in 1995, the British "
                  "Bulldog in 1996 and Jeff Jarrett in 1999. He also teamed with Ben Bassarab in "
                  "Stampede Wrestling, Jim Neidhart as the New Foundation and Koko B. Ware as High "
                  "Energy.")),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Owen James Hart"),
        dict(label="Born", value="May 7, 1965", sub="Calgary, Alberta, Canada"),
        dict(label="Died", value="May 23, 1999",
             sub="Kansas City, Missouri &middot; age 34 &middot; fall during a stunt entrance at Over the Edge"),
        dict(label="Billed from", value="Calgary, Alberta"),
        dict(label="Height", value="5&#8242;10&#8243;",
             sub="178 cm, billed &middot; older sources, including this page&rsquo;s previous version, said 5&#8242;11&#8243;"),
        dict(label="Weight", value="227 lb", sub="103 kg, billed"),
        dict(label="Debut", value="May 30, 1986", sub="Stampede Wrestling"),
        dict(label="Trained by", value="Stu Hart", sub="in the family&rsquo;s Dungeon, Calgary"),
        dict(label="Family", value="Youngest of Stu and Helen Hart&rsquo;s 12 children",
             sub="brother of Bret Hart &middot; married Martha Patterson July 1, 1989"),
        dict(label="Ring names", value="Blue Blazer &middot; The Rocket &middot; King of Harts",
             sub="also the Black Hart and the Lone Hart, 1997&ndash;1998"),
        dict(label="Finisher", value="Sharpshooter", sub="adopted after Survivor Series 1993"),
        dict(label="Hall of Fame", value="Pro Wrestling HOF, 2019",
             sub="not in the WWE Hall of Fame; his widow has refused it"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1965-05-07",
    bornplace="Calgary, Alberta, Canada",
    nationality="Canada",
    height_cm=178,
    weight_kg=103,
    ld=dict(
        alternateName=["Owen James Hart", "The King of Harts", "The Blue Blazer", "The Rocket",
                       "The Black Hart"],
        deathDate="1999-05-23",
        deathPlace="Kansas City, Missouri",
        award=["WWF World Tag Team Championship (4 reigns)",
               "WWF Intercontinental Championship (2 reigns)",
               "WWF European Championship (1 reign)",
               "King of the Ring (1994)",
               "IWGP Junior Heavyweight Championship (1 reign)",
               "PWI Rookie of the Year (1987)",
               "PWI Feud of the Year (1994, vs Bret Hart)",
               "Pro Wrestling Hall of Fame (2019)"],
        knowsAbout=["Professional wrestling", "The Hart Foundation", "WWF", "Stampede Wrestling",
                    "New Japan Pro-Wrestling", "Tag team wrestling"],
        description=("Owen Hart, born Owen James Hart in Calgary, Alberta, was a Canadian professional "
                     "wrestler and the youngest child of Stu Hart. He won the IWGP Junior Heavyweight "
                     "Championship in 1988, the 1994 King of the Ring, four WWF Tag Team "
                     "Championships, two Intercontinental Championships and the European "
                     "Championship, and beat his brother Bret Hart at WrestleMania X. He died on May "
                     "23, 1999, after a fall during a stunt entrance at the WWF Over the Edge "
                     "pay-per-view in Kansas City. He is honored by the Owen Hart Foundation and "
                     "AEW's Owen Hart Cup."),
        sameAs=["https://en.wikipedia.org/wiki/Owen_Hart"],
    ),
)
