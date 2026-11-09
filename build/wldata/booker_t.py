# -*- coding: utf-8 -*-
"""Booker T - dossier data.

Compiled November 9, 2026 from data/booker-t.md, which carries a source URL for
every claim (Wikipedia event and title-history pages, WWE.com, Fightful,
PostWrestling, Sports Illustrated, Wrestling Inc, Online World of Wrestling,
AOL/WWE). Built FROM the .md, not from memory, and not from the old page: the
old "X" variant page was harvested and most of its record rows were wrong (it
gave him a WWE Championship he never held, a WrestleMania X8 tag win that was a
singles loss to Edge, and a SummerSlam 2006 title loss that was a DQ retention).

Status: he is not an active wrestler. As of November 9, 2026 he is NXT's
full-time color commentator with Vic Joseph, runs Reality of Wrestling (a WWE ID
partner) and coaches on WWE LFG. His last match was January 11, 2025 (def. Zilla
Fatu at ROW). The "now" fields describe exactly that and invent nothing.

Deliberate omissions:
  * No walk-out theme band: no source for his entrance theme title or composer
    was found in this pass, and a guessed theme is worse than none.
  * No "Right Now" pulse and no X/Instagram links: no hand-picked, press-verified
    posts were gathered and the handles were not checked.
  * No career win-loss total: Cagematch is JS-gated, so record.total is the
    honest row count.
  * Signature cards carry "NR" (not rated): no Wrestling Observer ratings were
    verified, so none are printed.
  * Slot 10 is "feats" (records and counting rules); there is no MMA history.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    # ---- WCW: Harlem Heat
    dict(result="W", date="1994-12-08", promo="WCW", type="tag", landmark=True,
         event="WCW Saturday Night", opponent="Stars and Stripes",
         stip="Tag, with Stevie Ray. Taped December 8, aired January 14, 1995. Harlem Heat's first of a record ten reigns",
         title="WCW World Tag Team Championship"),
    dict(result="W", date="1995-09-17", promo="WCW", type="tag",
         event="Fall Brawl 1995", opponent="Dick Slater & Bunkhouse Buck",
         stip="Tag, with Stevie Ray. The third reign, held for one day",
         title="WCW World Tag Team Championship"),
    dict(result="W", date="1996-06-24", promo="WCW", type="tag",
         event="Monday Nitro", opponent="Sting & Lex Luger",
         stip="Tag, with Stevie Ray. The fifth reign",
         title="WCW World Tag Team Championship"),
    # ---- WCW: singles breakout
    dict(result="W", date="1997-12-29", promo="WCW", landmark=True,
         event="Monday Nitro, Baltimore", opponent="Disco Inferno",
         stip="Singles. The first of a record six Television title reigns",
         title="WCW World Television Championship"),
    dict(result="W", date="1998-06-14", promo="WCW",
         event="The Great American Bash 1998", opponent="Chris Benoit",
         stip="Game 7 of a best-of-seven series, tied 3-3, for the No. 1 contendership. Won with two Harlem Sidekicks",
         title=""),
    dict(result="W", date="1998-06-14", promo="WCW",
         event="The Great American Bash 1998", opponent="Fit Finlay",
         stip="Singles, later the same night. The fifth Television title reign",
         title="WCW World Television Championship"),
    dict(result="W", date="1999-03-14", promo="WCW",
         event="Uncensored 1999", opponent="Scott Steiner",
         stip="Singles. The sixth and final Television title reign",
         title="WCW World Television Championship"),
    dict(result="W", date="1999-08-14", promo="WCW", type="tag",
         event="Road Wild 1999", opponent="Bam Bam Bigelow & Kanyon",
         stip="Tag, with Stevie Ray. The Harlem Heat reunion's first title, a record eighth team reign",
         title="WCW World Tag Team Championship"),
    dict(result="W", date="1999-10-24", promo="WCW", type="tag", landmark=True,
         event="Halloween Havoc 1999", opponent="Konnan & Billy Kidman; Brian Knobbs & Hugh Morrus",
         stip="Triple threat street fight, with Stevie Ray. The tenth team reign, still the record",
         title="WCW World Tag Team Championship"),
    # ---- WCW: the five world titles
    dict(result="W", date="2000-07-09", promo="WCW", landmark=True,
         event="Bash at the Beach 2000", opponent="Jeff Jarrett",
         stip="Impromptu singles match, booked after the Hogan and Russo incident earlier that night. First world title",
         title="WCW World Heavyweight Championship"),
    dict(result="L", date="2000-08-28", promo="WCW",
         event="Monday Nitro, Las Cruces", opponent="Kevin Nash",
         stip="Singles, Jeff Jarrett as special referee. First reign ends at 50 days",
         title="WCW World Heavyweight Championship"),
    dict(result="W", date="2000-09-17", promo="WCW", landmark=True,
         event="Fall Brawl 2000", opponent="Kevin Nash",
         stip="Caged Heat match. Second reign",
         title="WCW World Heavyweight Championship"),
    dict(result="L", date="2000-09-25", promo="WCW",
         event="Monday Nitro, Uniondale", opponent="Vince Russo",
         stip="Steel cage. Second reign ends at 8 days",
         title="WCW World Heavyweight Championship"),
    dict(result="W", date="2000-10-02", promo="WCW",
         event="Monday Nitro, Daly City", opponent="Jeff Jarrett",
         stip="San Francisco 49ers match for the vacant title. Third reign",
         title="WCW World Heavyweight Championship"),
    dict(result="L", date="2000-11-26", promo="WCW", landmark=True,
         event="Mayhem 2000", opponent="Scott Steiner",
         stip="Straitjacket Caged Heat match. Steiner used a chair, then the Steiner Recliner, for a technical submission at 13:10",
         title="WCW World Heavyweight Championship"),
    dict(result="W", date="2001-03-18", promo="WCW", landmark=True,
         event="Greed 2001", opponent="Rick Steiner",
         stip="Singles at WCW's last pay-per-view. Book End for the win; completes the WCW Triple Crown",
         title="WCW United States Heavyweight Championship"),
    dict(result="W", date="2001-03-26", promo="WCW", landmark=True,
         event="Monday Nitro, the final episode", opponent="Scott Steiner",
         stip="Winner take all, opening the last Nitro. Fourth world reign; leaves WCW as both world and US champion",
         title="WCW World Heavyweight Championship"),
    # ---- WWF/WWE: the Invasion
    dict(result="W", date="2001-07-22", promo="WWE", type="tag", landmark=True,
         event="Invasion", opponent="Steve Austin, Kurt Angle, Chris Jericho, Kane & The Undertaker",
         stip="Ten-man Inaugural Brawl for Team WCW/ECW. Austin turned on his team; Booker pinned Angle",
         title=""),
    dict(result="L", date="2001-07-24", promo="WWE",
         event="SmackDown, Pittsburgh", opponent="Kurt Angle",
         stip="Singles. Taped July 24, aired July 26",
         title="WCW Championship"),
    dict(result="W", date="2001-07-30", promo="WWE",
         event="Raw Is War, Philadelphia", opponent="Kurt Angle",
         stip="Singles. The fifth and final WCW world reign",
         title="WCW Championship"),
    dict(result="L", date="2001-08-19", promo="WWE", landmark=True,
         event="SummerSlam 2001", opponent="The Rock",
         stip="Singles, Shane McMahon in his corner. The Rock kipped up from the Spinaroonie and hit the Rock Bottom",
         title="WCW Championship"),
    dict(result="W", date="2001-09-25", promo="WWE", type="tag",
         event="SmackDown, Dayton", opponent="Kane & The Undertaker",
         stip="Tag, with Test. Aired September 27; his 11th WCW tag title, the individual record. Opponents as reported by Online World of Wrestling",
         title="WCW Tag Team Championship"),
    dict(result="L", date="2002-03-17", promo="WWE",
         event="WrestleMania X8", opponent="Edge",
         stip="Singles, 6:32. Edge won with the Edgecution",
         title=""),
    dict(result="W", date="2002-12-15", promo="WWE", type="tag", landmark=True,
         event="Armageddon 2002", opponent="Chris Jericho & Christian; Lance Storm & William Regal; The Dudley Boyz",
         stip="Four-way elimination, with Goldust. Booker pinned Jericho after a Book End",
         title="World Tag Team Championship"),
    dict(result="L", date="2003-03-30", promo="WWE", landmark=True,
         event="WrestleMania XIX", opponent="Triple H",
         stip="Singles, 18:45, Ric Flair at ringside. Booker's knee gave out after the Harlem Hangover; Pedigree",
         title="World Heavyweight Championship"),
    dict(result="W", date="2003-07-07", promo="WWE",
         event="Raw", opponent="Christian",
         stip="Singles. His only Intercontinental title reign",
         title="Intercontinental Championship"),
    dict(result="W", date="2004-02-16", promo="WWE", type="tag",
         event="Raw", opponent="Ric Flair & Batista",
         stip="Tag, with Rob Van Dam",
         title="World Tag Team Championship"),
    dict(result="W", date="2004-07-27", promo="WWE", type="tag",
         event="SmackDown, Cincinnati", opponent="John Cena, Rene Dupree, Kenzo Suzuki, Rob Van Dam, Billy Gunn, Charlie Haas & Luther Reigns",
         stip="Eight-man elimination for the vacant title. The 100th reign in the title's history",
         title="United States Championship"),
    dict(result="L", date="2004-10-03", promo="WWE",
         event="No Mercy 2004", opponent="John Cena",
         stip="Game 5 of a best-of-five series tied 2-2, 10:22",
         title="United States Championship"),
    dict(result="W", date="2005-10-18", promo="WWE",
         event="SmackDown, Reno", opponent="Chris Benoit",
         stip="Singles, with Sharmell's help. Aired October 21",
         title="United States Championship"),
    dict(result="L", date="2006-02-19", promo="WWE",
         event="No Way Out 2006", opponent="Chris Benoit",
         stip="The decider of the best-of-seven series for the vacated title",
         title="United States Championship"),
    # ---- WWE: King Booker
    dict(result="W", date="2006-05-21", promo="WWE", landmark=True,
         event="Judgment Day 2006", opponent="Bobby Lashley",
         stip="King of the Ring final. Sharmell distracted, Finlay used his shillelagh, scissors kick for the pin",
         title=""),
    dict(result="W", date="2006-07-23", promo="WWE", landmark=True,
         event="The Great American Bash 2006", opponent="Rey Mysterio",
         stip="Singles, 16:46. Chavo Guerrero hit Mysterio with a chair",
         title="World Heavyweight Championship"),
    dict(result="L", date="2006-08-20", promo="WWE",
         event="SummerSlam 2006", opponent="Batista",
         stip="Lost by disqualification when Sharmell attacked Batista, so King Booker kept the title",
         title="World Heavyweight Championship"),
    dict(result="L", date="2006-11-26", promo="WWE", landmark=True,
         event="Survivor Series 2006", opponent="Batista",
         stip="Singles, 13:58. Booker swung the belt; Batista countered and pinned him",
         title="World Heavyweight Championship"),
    dict(result="L", date="2007-04-01", promo="WWE", type="tag",
         event="WrestleMania 23", opponent="Mr. Kennedy, Edge, Randy Orton, Jeff Hardy, Matt Hardy, Finlay & CM Punk",
         stip="Money in the Bank ladder match. Mr. Kennedy won",
         title=""),
    # ---- TNA
    dict(result="L", date="2007-11-11", promo="TNA", type="tag",
         event="Genesis 2007", opponent="Kurt Angle & Kevin Nash",
         stip="Tag, as Sting's mystery partner. His TNA debut; Angle pinned Sting",
         title=""),
    dict(result="L", date="2009-03-15", promo="TNA",
         event="Destination X 2009", opponent="AJ Styles",
         stip="Singles for the title Booker had declared himself holder of in October 2008",
         title="TNA Legends Championship"),
    dict(result="W", date="2009-07-19", promo="TNA", type="tag", landmark=True,
         event="Victory Road 2009", opponent="Beer Money (James Storm & Robert Roode)",
         stip="Tag, with Scott Steiner, for the Main Event Mafia",
         title="TNA World Tag Team Championship"),
    dict(result="L", date="2009-10-18", promo="TNA", type="tag",
         event="Bound for Glory 2009", opponent="The British Invasion; Team 3D; Beer Money",
         stip="Full Metal Mayhem four-way with Scott Steiner, for the TNA and IWGP tag titles. His last TNA pay-per-view",
         title="TNA World Tag Team Championship"),
    # ---- WWE returns
    dict(result="L", date="2011-01-30", promo="WWE", type="tag",
         event="Royal Rumble 2011", opponent="The 40-man Royal Rumble field",
         stip="Surprise entrant No. 21. Mason Ryan threw him out right after a Spinaroonie",
         title=""),
    dict(result="L", date="2023-01-28", promo="WWE", type="tag",
         event="Royal Rumble 2023", opponent="The men's Royal Rumble field",
         stip="Surprise entrant No. 21. Gunther eliminated him after 42 seconds",
         title=""),
    # ---- Reality of Wrestling
    dict(result="W", date="2015-02-21", promo="IND", type="tag",
         event="ROW: The Final Heat", opponent="The New Heavenly Bodies",
         stip="Tag, with Stevie Ray. A Harlem Heat reunion in his own promotion",
         title="ROW Tag Team Championship"),
    dict(result="W", date="2025-01-11", promo="IND", landmark=True,
         event="ROW, Texas City", opponent="Zilla Fatu",
         stip="Singles. His first singles match since January 2019 and his most recent match",
         title=""),
]

DATA = dict(
    slug="booker-t",
    name="Booker T",
    realname="Booker T. Huffman Jr.",
    epithet="The Five-Time WCW Champion",
    hook="Record & Titles",
    art="booker-t",

    meta_desc=("Booker T: five WCW world title reigns, a record 11 WCW tag titles and 10 with "
               "Stevie Ray as Harlem Heat, six WCW TV titles, King Booker's 2006 World "
               "Heavyweight title, two Hall of Fame inductions. Full record and career."),
    og_desc=("Harlem Heat, five WCW world titles, King Booker and Queen Sharmell, TNA, two Hall "
             "of Fame inductions, and NXT's color commentator in 2026."),
    tw_desc=("Booker T: six world titles by WWE's count, a record 11 WCW tag titles, and the "
             "last WCW champion. Now calling NXT."),

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1990",
    height_imp="6&#8242;3&#8243;",
    weight_lb="256",
    world_titles="6",
    vitals_tagline="Can you dig it",
    support_note="Merch &middot; Games &middot; Watch",
    sp_items=[
        dict(ic="BT", title="Booker T Merch", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable legend in WWE 2K26",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/booker-t"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick=("Six-time world champion &middot; Harlem Heat &middot; Hall of Fame 2013 and "
               "2019 &middot; the last WCW champion"),
    hero_tag=("Houston, Texas &middot; <em>WCW &middot; WWF/WWE &middot; TNA &middot; "
              "1990&ndash;2025</em>"),
    now_label="NOW",
    now_bold="NXT color commentator",
    now_tail=(" &middot; calls NXT with Vic Joseph, runs Reality of Wrestling as a WWE ID "
              "partner and coaches on WWE LFG; last match January 11, 2025"),
    hstats=[
        dict(value="6",  x=True, label="World Titles"),
        dict(value="11", x=True, label="WCW Tag Titles"),
        dict(value="6",  x=True, label="WCW TV Titles"),
        dict(value="2",  x=True, label="Hall of Fame Inductions"),
    ],
    ghost_link="From a Houston prison sentence to the last WCW champion",
    vlabel="Est. 1990 &middot; Houston, Texas",
    mono="BT",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Booker T</b> held the WCW World Heavyweight Championship five times between July "
        "2000 and August 2001, and he was the man holding it when WCW closed. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">11</span>'
        '<span class="pull-cap">WCW World Tag Team Championship reigns, the individual record; '
        'ten of them with Stevie Ray as Harlem Heat</span></span>'
        "Before that he was half of Harlem Heat with his older brother Stevie Ray. The team won "
        "the WCW World Tag Team Championship ten times, a team record, and Booker's 11 reigns "
        "with that title (the last with Test in 2001) are the individual record. He also holds "
        "the record for WCW World Television Championship reigns with six. In WWE he became "
        "King Booker, won the 2006 King of the Ring and the World Heavyweight Championship, and "
        "went into the WWE Hall of Fame twice: alone in 2013 and with Harlem Heat in 2019.",

        "Two claims on old pages, including the one this dossier replaces, need fixing. The "
        "first is that King Booker won the WWE Championship in 2006. He did not. He beat Rey "
        "Mysterio for the World Heavyweight Championship at The Great American Bash on July "
        "23, 2006, and he never held the WWE Championship. The second is the count. WWE.com "
        "calls him a six-time world champion but lists only four WCW title reigns. Both are "
        "right by their own rules. He won the WCW title four times inside WCW, then a fifth "
        "time on Raw on July 30, 2001, after the WWF bought WCW, when the belt was billed as "
        "the WCW Championship. Add the 2006 World Heavyweight title and you get six.",

        "He was born Booker T. Huffman Jr. on March 1, 1965, in Plain Dealing, Louisiana, the "
        "youngest of eight children, and grew up in Houston after losing both parents. At 22 "
        "he pleaded guilty to two aggravated robberies of Wendy's restaurants and served 19 "
        "months in prison. He trained at Ivan Putski's school under Scott Casey and debuted in "
        "1990 as G.I. Bro. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig pull-fig--sm">2000</span>'
        '<span class="pull-cap">first WCW world title, beating Jeff Jarrett at Bash at the Beach on July 9</span></span>'
        "WCW signed the brothers in 1993 as Harlem Heat, first as Kole and Kane, and their first "
        "tag title came in December 1994. Booker's singles run began with the Television title "
        "on December 29, 1997, and a best-of-seven series with Chris Benoit in 1998. His first "
        "world title came on the strangest night in WCW history: at Bash at the Beach on July "
        "9, 2000, Vince Russo's angle with Hulk Hogan blew up, the title went back to Jeff "
        "Jarrett, and Booker beat him for it in an impromptu match. He traded it with Kevin Nash and "
        "Russo, lost it to Scott Steiner in a straitjacket cage at Mayhem on November 26, 2000, "
        "and took it back from Steiner in the opening match of the final Nitro.",

        "In the WWF he led the WCW side of the Invasion, pinned Kurt Angle in the Inaugural "
        "Brawl, and dropped the WCW title to The Rock at SummerSlam 2001. He lost a World "
        "Heavyweight title match to Triple H at WrestleMania XIX after a build that used his "
        "criminal record against him, a promo Michael Cole publicly questioned. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig pull-fig--sm">2006</span>'
        '<span class="pull-cap">King of the Ring, then the World Heavyweight Championship as King Booker with Queen Sharmell</span></span>'
        "Then came King Booker: a 2006 King of the Ring win over Bobby Lashley, a crown, a faux "
        "British accent, his wife Sharmell as Queen, and a World Heavyweight Championship reign "
        "from July to November 2006. TNA followed from 2007 to 2009, where he co-founded the "
        "Main Event Mafia and won the TNA tag titles with Scott Steiner. Since 2011 he has been "
        "a broadcaster, a SmackDown general manager and a promoter. As of November 9, 2026, he "
        "is NXT's full-time color commentator alongside Vic Joseph, runs Reality of Wrestling "
        "in Houston as a WWE ID partner, and coaches on WWE LFG. His last match was a win over "
        "Zilla Fatu at a Reality of Wrestling show on January 11, 2025. Trick Williams has "
        "challenged him for SummerSlam 2027. Booker said he never says never. Nothing is booked.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Highlight set",
        promo_order=["WCW", "WWE", "TNA", "IND"],
        promo_labels={"WCW": "WCW", "WWE": "WWF/WWE", "TNA": "TNA", "IND": "ROW"},
        stats=[
            ("5&times;",  "WCW world reigns"),
            ("1",         "World Heavyweight reign"),
            ("11&times;", "WCW tag titles"),
            ("6&times;",  "WCW TV titles"),
            ("2006",      "King of the Ring"),
            ("2025",      "Most recent match"),
        ],
        lead=("Forty-four documented bouts from 1994 to 2025. This is a highlight set, not a career "
              "count, and no career win&ndash;loss total is published because none was verified. "
              "Every WCW world title change he was part of is here, along with the Harlem Heat "
              "title wins that set the record, the King Booker year and the TNA tag run. Filter "
              "by promotion or match type, sort any column, and turn spoilers on to see results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("Six nights that define the career. NR means not rated: no Wrestling "
                    "Observer star ratings were verified in this pass, so none are printed."),
    signature=[
        dict(rating="NR", event="Bash at the Beach 2000", opponent="Jeff Jarrett",
             stip="The first WCW world title, won hours after the Hogan and Russo incident"),
        dict(rating="NR", event="Mayhem 2000", opponent="Scott Steiner",
             stip="Straitjacket Caged Heat match for the WCW title; the Steiner Recliner ends it"),
        dict(rating="NR", event="Final Monday Nitro, 2001", opponent="Scott Steiner",
             stip="Winner take all, WCW and US titles, opening WCW's last broadcast"),
        dict(rating="NR", event="SummerSlam 2001", opponent="The Rock",
             stip="WCW Championship, two men with the same side-slam finisher"),
        dict(rating="NR", event="WrestleMania XIX", opponent="Triple H",
             stip="World Heavyweight Championship after a build about his criminal record"),
        dict(rating="NR", event="The Great American Bash 2006", opponent="Rey Mysterio",
             stip="King Booker wins the World Heavyweight Championship"),
    ],
    signature_count_word="six",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("6&times;",  "World title reigns (WWE count)"),
            ("11&times;", "WCW tag titles, the record"),
            ("6&times;",  "WCW TV titles, the record"),
            ("2",         "Hall of Fame inductions"),
        ],
        lead=("Wikipedia's tally is 35 titles across WCW, WWF/WWE and TNA, 21 of them in WCW. "
              "These are the ones that matter, with the counting rules shown."),
        rows=[
            dict(ic="W", name="WCW World Heavyweight Championship", count="5",
                 sub="Jul 9, 2000, Bash at the Beach, def. Jeff Jarrett (50 days) &middot; Sep "
                     "17, 2000, Fall Brawl, def. Kevin Nash in a cage (8 days) &middot; Oct 2, "
                     "2000, Nitro, def. Jarrett for the vacant title (55 days) &middot; Mar 26, "
                     "2001, the final Nitro, def. Scott Steiner (120 days) &middot; Jul 30, 2001, "
                     "Raw, def. Kurt Angle as the WCW Championship (20 days). 253 days in all. "
                     "WWE.com counts the first four as WCW reigns."),
            dict(ic="WH", name="World Heavyweight Championship", count="1",
                 sub="Jul 23, 2006, The Great American Bash, def. Rey Mysterio as King Booker "
                     "&middot; kept it by DQ against Batista at SummerSlam &middot; lost to "
                     "Batista at Survivor Series, Nov 26, 2006"),
            dict(ic="T", name="WCW World Tag Team Championship", count="11",
                 sub="Ten reigns with Stevie Ray as Harlem Heat, Dec 8, 1994 to Oct 24, 1999, "
                     "470 days in all, the team record &middot; one with Test, Sep 25, 2001. "
                     "Eleven is the individual record"),
            dict(ic="TV", name="WCW World Television Championship", count="6",
                 sub="Dec 29, 1997 from Disco Inferno &middot; Feb 22, 1998 from Rick Martel "
                     "&middot; May 1 and May 3, 1998 at house shows, one day each &middot; Jun 14, "
                     "1998 from Fit Finlay &middot; Mar 14, 1999 from Scott Steiner. Six is the "
                     "record for the title"),
            dict(ic="US", name="United States Championship", count="4",
                 sub="WCW US title, Mar 18, 2001, def. Rick Steiner at Greed, completing the "
                     "WCW Triple Crown &middot; WWE US title three times: Jul 27, 2004 (the "
                     "100th reign), Oct 18, 2005, and Jan 10, 2006"),
            dict(ic="WT", name="World Tag Team Championship", count="3",
                 sub="With Test (Nov 2001) &middot; with Goldust, Armageddon, Dec 15, 2002 "
                     "&middot; with Rob Van Dam, Raw, Feb 16, 2004"),
            dict(ic="IC", name="Intercontinental Championship", count="1",
                 sub="Jul 7, 2003, Raw, def. Christian; lost back to him Aug 10, 2003"),
            dict(ic="H", name="Hardcore Championship", count="2",
                 sub="Both on May 4, 2002, at Insurrextion, under the 24/7 rule"),
            dict(ic="K", name="King of the Ring", count="1",
                 sub="2006, def. Bobby Lashley in the final at Judgment Day, May 21"),
            dict(ic="TNA", name="TNA World Tag Team Championship", count="1",
                 sub="With Scott Steiner, Jul 19, 2009 to Oct 18, 2009"),
            dict(ic="L", name="TNA Legends Championship", count="1",
                 sub="Inaugural holder: he declared himself champion on Impact, Oct 23, 2008; "
                     "AJ Styles beat him for it at Destination X, Mar 15, 2009"),
            dict(ic="HOF", name="WWE Hall of Fame", count="2",
                 sub="Class of 2013, inducted by Stevie Ray at Madison Square Garden &middot; "
                     "Class of 2019 as Harlem Heat, Barclays Center"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="A brother, a comedy partner, an invading army and a mafia of former world champions.",
        cards=[
            dict(era="WCW &middot; 1993&ndash;2000",
                 name="Harlem Heat",
                 members="Booker T, Stevie Ray; managed by Col. Robert Parker, Sister Sherri and later Jacqueline",
                 desc="The Huffman brothers debuted in WCW in 1993 as Kole and Kane and went back "
                      "to their own names in 1994. Ten WCW World Tag Team title reigns is the team "
                      "record. They split in 1998, reunited in 1999 for reigns eight through ten, "
                      "and broke up for good in 2000. WWE inducted them in 2019, and they reunited "
                      "once more in 2015 to win Reality of Wrestling's tag titles."),
            dict(era="WWF &middot; 2001",
                 name="The Alliance",
                 members="WCW and ECW talent; Shane McMahon in Booker's corner",
                 desc="Booker was the WCW world champion who walked into the WWF at King of the "
                      "Ring 2001 and attacked Steve Austin. He pinned Kurt Angle to win the "
                      "Invasion main event for Team WCW/ECW and held the WCW title until The Rock "
                      "took it at SummerSlam."),
            dict(era="WWE &middot; 2002&ndash;03",
                 name="Booker T &amp; Goldust",
                 members="Booker T, Goldust",
                 desc="The comedy tag team WWE.com still lists among his highlights. They won the "
                      "World Tag Team Championship in a four-way elimination at Armageddon 2002, "
                      "with Booker pinning Chris Jericho."),
            dict(era="WWE &middot; 2006&ndash;07",
                 name="King Booker &amp; Queen Sharmell",
                 members="King Booker, Queen Sharmell; help from Finlay and William Regal",
                 desc="William Regal crowned him on SmackDown after the 2006 King of the Ring. "
                      "Finlay's shillelagh had helped win that final, and Chavo Guerrero's chair "
                      "won him the World Heavyweight title. Sharmell's interference cost him the "
                      "belt to Batista at Survivor Series."),
            dict(era="TNA &middot; 2008&ndash;09",
                 name="Main Event Mafia",
                 members="Kurt Angle, Sting, Kevin Nash, Booker T; Scott Steiner joined a week later",
                 desc="Formed on Impact on October 23, 2008, the same night Booker unveiled the "
                      "Legends Championship. Booker and Scott Steiner won the TNA World Tag Team "
                      "Championship from Beer Money at Victory Road 2009, and Steiner is half of "
                      "the Steiner Brothers, the team Harlem Heat traded the WCW tag titles with "
                      "in 1996."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Four names, one Houston accent underneath all of them.",
        cards=[
            dict(mono="GB", era="WWA &middot; 1990", name="G.I. Bro",
                 desc="A Gulf War-era military gimmick tied to the Sgt. Slaughter angle, eight "
                      "weeks into his training at Ivan Putski's school."),
            dict(mono="KO", era="WCW &middot; 1993&ndash;94", name="Kole",
                 desc="His first WCW name, with his brother billed as Kane, as Harlem Heat debuted "
                      "under Col. Robert Parker. Both went back to their real first names in 1994."),
            dict(mono="BT", era="WCW &middot; WWE &middot; TNA &middot; 1994&ndash;", name="Booker T",
                 desc="The Spinaroonie, the Scissors Kick, the Book End and &ldquo;Sucka!&rdquo; "
                      "Tag specialist, record Television champion, five-time WCW world champion "
                      "and, later, the voice of NXT."),
            dict(mono="KB", era="WWE &middot; 2006&ndash;07", name="King Booker",
                 desc="Crowned on SmackDown after winning the 2006 King of the Ring, with a faux "
                      "British accent and Sharmell as Queen. WWE.com says many fans rank "
                      "the accent among wrestling's best. He won the World Heavyweight title in "
                      "the role."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Prison to the last WCW championship, then a king, then the broadcast desk.",
        rows=[
            dict(year="1987", title="Prison",
                 desc="Pleads guilty in December 1987 to two aggravated robberies of Houston "
                      "Wendy's restaurants. He serves 19 months and stays on parole until April "
                      "1992."),
            dict(year="1990", title="Debut as G.I. Bro",
                 desc="Debuts in the Western Wrestling Alliance after training under Scott Casey "
                      "at Ivan Putski's school."),
            dict(year="1993", title="Harlem Heat in WCW",
                 desc="Signs with WCW alongside his brother Lash, now Stevie Ray. They debut as "
                      "Kole and Kane, managed by Col. Robert Parker."),
            dict(year="1994", title="First tag title",
                 desc="Beats Stars and Stripes on December 8 for the WCW World Tag Team "
                      "Championship, the first of ten Harlem Heat reigns."),
            dict(year="1997", title="Singles breakout",
                 desc="Wins the WCW World Television Championship from Disco Inferno on December "
                      "29. He will hold it six times, the record."),
            dict(year="1998", title="The best-of-seven",
                 desc="Beats Chris Benoit in Game 7 at The Great American Bash on June 14, then "
                      "beats Fit Finlay for the TV title the same night."),
            dict(year="1999", title="Reunion and the record",
                 desc="Re-forms Harlem Heat, wins the tag titles at Road Wild, Fall Brawl and "
                      "Halloween Havoc, and reaches ten team reigns."),
            dict(year="2000", title="World champion",
                 desc="Beats Jeff Jarrett at Bash at the Beach on July 9, trades the title with "
                      "Kevin Nash and Vince Russo, wins it a third time in October, and loses it "
                      "to Scott Steiner at Mayhem on November 26."),
            dict(year="2001", title="The last WCW champion",
                 desc="Wins the US title at Greed and the world title on the final Nitro, enters "
                      "the WWF at King of the Ring, pins Kurt Angle at Invasion, and loses the WCW "
                      "title to The Rock at SummerSlam."),
            dict(year="2002", title="Booker and Goldust",
                 desc="Loses to Edge at WrestleMania X8 and wins the World Tag Team title with "
                      "Goldust at Armageddon on December 15."),
            dict(year="2003", title="WrestleMania XIX",
                 desc="Loses to Triple H for the World Heavyweight Championship in Seattle on "
                      "March 30, then wins the Intercontinental title from Christian in July."),
            dict(year="2004", title="The 100th US champion",
                 desc="Wins tag gold with Rob Van Dam in February and the vacant US title in "
                      "July, then loses it to John Cena in Game 5 at No Mercy."),
            dict(year="2006", title="King Booker",
                 desc="Wins King of the Ring on May 21, is crowned by William Regal, and beats "
                      "Rey Mysterio for the World Heavyweight Championship on July 23. Batista "
                      "takes it on November 26."),
            dict(year="2007", title="TNA",
                 desc="Leaves WWE in October and debuts in TNA at Genesis on November 11 as "
                      "Sting's mystery partner."),
            dict(year="2009", title="Main Event Mafia gold",
                 desc="Loses the Legends title to AJ Styles in March, wins the TNA tag titles "
                      "with Scott Steiner in July, and makes his last TNA pay-per-view appearance "
                      "at Bound for Glory in October."),
            dict(year="2011", title="Back to WWE, on the mic",
                 desc="Returns as a surprise Royal Rumble entrant on January 30 and joins the "
                      "SmackDown commentary team on February 1."),
            dict(year="2012", title="SmackDown general manager",
                 desc="Becomes SmackDown's on-screen general manager on August 3 and holds the "
                      "job until July 2013."),
            dict(year="2013", title="Hall of Fame",
                 desc="Inducted by Stevie Ray at Madison Square Garden on April 6."),
            dict(year="2019", title="Hall of Fame, again",
                 desc="Inducted with Harlem Heat at the Barclays Center on April 6."),
            dict(year="2022", title="The voice of NXT",
                 desc="Joins Vic Joseph on NXT commentary on October 6, on what was meant to be a "
                      "short stint. It became permanent."),
            dict(year="2025", title="One more win",
                 desc="Beats Zilla Fatu at Reality of Wrestling in Texas City on January 11, his "
                      "first singles match in six years and his most recent match."),
            dict(year="2026", title="Appreciation Night",
                 desc="NXT holds Booker T Appreciation Night in Houston on March 17. In July Trick "
                      "Williams challenges him for SummerSlam 2027, and in October he hands ROW's "
                      "Josiah Jean a WWE ID contract."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="The men he traded titles and blows with.",
        cards=[
            dict(name="Scott Steiner",
                 desc="Took the WCW title from him in a straitjacket cage at Mayhem 2000 with a "
                      "chair and the Steiner Recliner, then lost it back to him in the opening "
                      "match of the final Nitro. Eight years later they were TNA tag champions "
                      "together in the Main Event Mafia."),
            dict(name="Jeff Jarrett",
                 desc="The champion Booker beat for his first WCW world title at Bash at the "
                      "Beach 2000, and again in a San Francisco 49ers match for the vacant title "
                      "that October."),
            dict(name="Kevin Nash", slug="kevin-nash",
                 desc="Took the WCW title from Booker on Nitro on August 28, 2000, and lost it "
                      "back in a cage at Fall Brawl three weeks later. They met again in Booker's "
                      "TNA debut in 2007."),
            dict(name="The Rock", slug="the-rock",
                 desc="Won the WCW Championship from him at SummerSlam 2001, kipping up from the "
                      "Spinaroonie to hit a Rock Bottom. The two used nearly the same side slam as "
                      "a finisher: the Book End and the Rock Bottom."),
            dict(name="Stone Cold Steve Austin", slug="stone-cold-steve-austin",
                 desc="Booker's WWF arrival was an attack on Austin at King of the Ring 2001. Their "
                      "feud produced the supermarket brawl, filmed in one take in a real "
                      "California store and aired on SmackDown in late 2001."),
            dict(name="Triple H", slug="triple-h",
                 desc="WrestleMania XIX, March 30, 2003. Triple H's build leaned on Booker's "
                      "criminal record, and Michael Cole asked at the press conference whether it "
                      "was racially insensitive. Triple H won with a Pedigree after working the "
                      "knee."),
            dict(name="Batista", slug="batista",
                 desc="Challenged King Booker at SummerSlam 2006 and won only by DQ, then took "
                      "the World Heavyweight Championship at Survivor Series when Sharmell's "
                      "interference backfired."),
            dict(name="Chris Benoit",
                 desc="Two best-of-seven series eight years apart: the 1998 WCW series for a TV "
                      "title shot, which Booker won in Game 7, and the 2005&ndash;06 WWE series "
                      "over the US title, which Benoit won at No Way Out."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Business",
        lead="A promoter, a broadcaster and a podcaster, more than an actor.",
        rows=[
            dict(when="2005&ndash;", title="Reality of Wrestling", kind="Business",
                 desc="Founded in Houston as Pro Wrestling Alliance in 2005 and renamed in 2012. "
                      "It is now an official WWE ID partner, and Roxanne Perez came through it."),
            dict(when="2011&ndash;", title="Commentary", kind="TV",
                 desc="SmackDown color commentary from 2011, Raw from 2015, Kickoff panels, and "
                      "NXT with Vic Joseph since October 6, 2022."),
            dict(when="2012", title="From Prison to Promise", kind="Book",
                 desc="His memoir of life before wrestling, written with Andrew William Wright "
                      "and published by Medallion Press."),
            dict(when="2011", title="Tough Enough", kind="TV",
                 desc="Trainer on the 2011 season of WWE's competition series."),
            dict(when="2024&ndash;", title="Hall of Fame (radio and podcast)", kind="Audio",
                 desc="His long-running show went national on ESPN Radio through a Disney and "
                      "ESPN deal announced in June 2024."),
            dict(when="2025&ndash;", title="WWE LFG", kind="TV",
                 desc="A coach on all three seasons of WWE's Legends and Future Greats."),
            dict(when="2021", title="Bad Bunny's &ldquo;Booker T&rdquo;", kind="Music",
                 desc="Appears in the music video for the Bad Bunny song named after him."),
            dict(when="2026", title="WWE 2K26", kind="Game",
                 desc="Playable legend, and he recorded voice work for the game."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, with the counting rules that make them true.",
        stats=[
            ("11", "WCW tag reigns, individual record"),
            ("10", "Harlem Heat reigns, team record"),
            ("6",  "WCW TV reigns, the record"),
        ],
        rows=[
            dict(name="Most WCW World Tag Team Championship reigns, team and individual",
                 sub="Harlem Heat's ten reigns lead every team; the Steiner Brothers and the "
                     "Minnesota Wrecking Crew had seven each. Booker's 11 lead every wrestler; "
                     "Stevie Ray had ten."),
            dict(name="Most WCW World Television Championship reigns",
                 sub="Six, from December 29, 1997 to May 9, 1999. Two of them lasted one day each, "
                     "at house shows in May 1998."),
            dict(name="The last WCW World Heavyweight Champion of the WCW era",
                 sub="He won the title on the final Nitro on March 26, 2001, and carried it into "
                     "the WWF. The Rock beat him for it at SummerSlam 2001, and Chris Jericho "
                     "unified it at Vengeance that December."),
            dict(name="Ninth WCW Triple Crown winner",
                 sub="Completed with the United States title at Greed on March 18, 2001, WCW's "
                     "last pay-per-view."),
            dict(name="16th WWE Triple Crown and 8th Grand Slam winner",
                 sub="Completed with the World Heavyweight Championship in 2006, under the "
                     "original Grand Slam format."),
            dict(name="The 100th United States Champion",
                 sub="Won the vacant title in an eight-man elimination on SmackDown in July "
                     "2004."),
            dict(name="Two WWE Hall of Fame inductions",
                 sub="2013 alone and 2019 with Harlem Heat."),
            dict(name="A win at 59",
                 sub="Beat Zilla Fatu on January 11, 2025, at Reality of Wrestling, 35 years "
                     "after his debut."),
        ],
        footnote=("No career win-loss total appears on this page; none was verified. The world "
                  "title count depends on the counter: five WCW reigns plus one World Heavyweight "
                  "title makes six, while WWE.com lists four WCW reigns because the fifth came "
                  "after the WWF purchase."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/booker-t"),
        dict(k="WWE.com", v="Harlem Heat", href="https://www.wwe.com/superstars/harlemheat"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Booker_T_(wrestler)"),
        dict(k="Wikipedia", v="WCW World Heavyweight Champions list",
             href="https://en.wikipedia.org/wiki/List_of_WCW_World_Heavyweight_Champions"),
        dict(k="WWE.com", v="Booker T recalls the final Nitro",
             href="https://www.wwe.com/classics/wcw/booker-t-recalls-final-nitro"),
        dict(k="Fightful", v="On NXT commentary, October 2026", href="https://www.fightful.com/?p=332127"),
        dict(k="PostWrestling", v="Def. Zilla Fatu, January 2025",
             href="https://www.postwrestling.com/2025/01/12/booker-t-defeats-zilla-fatu-in-singles-match-at-reality-of-wrestling-event/"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/booker-t.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="What is Booker T doing in 2026?",
            a="He calls NXT. As of November 9, 2026, Booker T is NXT's full-time color "
              "commentator alongside Vic Joseph, a job he started on October 6, 2022. He also "
              "runs Reality of Wrestling in Houston, an official WWE ID partner, and coaches on "
              "WWE LFG. NXT held a Booker T Appreciation Night in Houston on March 17, 2026. His "
              "last match was a win over Zilla Fatu on <b>January 11, 2025</b>. Trick Williams "
              "has challenged him for SummerSlam 2027, and nothing is booked.",
            q_ld="What is Booker T doing in 2026?",
            a_ld="As of November 9, 2026, Booker T is the full-time color commentator on WWE NXT "
                 "alongside Vic Joseph, a role he began on October 6, 2022. He also runs the "
                 "Reality of Wrestling promotion in Houston, an official WWE ID partner, and "
                 "coaches on WWE LFG. His most recent match was a win over Zilla Fatu on January "
                 "11, 2025, and no future match is booked."),
        dict(
            q="How many world titles did Booker T win?",
            a="Six, by WWE's count: five reigns with the WCW World Heavyweight Championship "
              "(2000&ndash;2001) and one with the World Heavyweight Championship as King Booker "
              "(2006). WWE.com lists &ldquo;WCW Champion (4 times)&rdquo; because his fifth WCW "
              "reign came on Raw on July 30, 2001, after the WWF bought WCW.",
            q_ld="How many world championships did Booker T win?",
            a_ld="Booker T is a six-time world champion by WWE's count. He held the WCW World "
                 "Heavyweight Championship five times between July 2000 and August 2001, four "
                 "of them in WCW and one after the WWF purchased WCW, and he won the World "
                 "Heavyweight Championship once as King Booker in 2006."),
        dict(
            q="Was Booker T ever WWE Champion?",
            a="No. This gets repeated often, including on the page this dossier replaced. In "
              "2006 King Booker beat Rey Mysterio for the <b>World Heavyweight Championship</b>, "
              "the SmackDown world title, at The Great American Bash on July 23. He never held "
              "the WWE Championship.",
            q_ld="Was Booker T ever WWE Champion?",
            a_ld="No. Booker T never held the WWE Championship. His WWE world title was the World "
                 "Heavyweight Championship, which he won from Rey Mysterio as King Booker at The "
                 "Great American Bash on July 23, 2006, and lost to Batista at Survivor Series on "
                 "November 26, 2006."),
        dict(
            q="How many tag team titles did Harlem Heat win?",
            a="Ten WCW World Tag Team Championships between December 1994 and October 1999, "
              "the most of any team. Booker won the title an 11th time with Test in 2001, which "
              "makes his 11 the individual record. Booker also won three WWF/WWE World Tag Team "
              "titles, with Test, Goldust and Rob Van Dam, and the TNA tag titles with Scott "
              "Steiner.",
            q_ld="How many tag team championships did Harlem Heat win?",
            a_ld="Harlem Heat, Booker T and his brother Stevie Ray, won the WCW World Tag Team "
                 "Championship ten times between 1994 and 1999, the most of any team. Booker T "
                 "won it an 11th time with Test in 2001, the individual record for that title."),
        dict(
            q="How did Booker T win his first WCW title?",
            a="At Bash at the Beach on July 9, 2000, in Daytona Beach. Earlier that night Vince "
              "Russo had Jeff Jarrett lie down for Hulk Hogan, and the angle fell apart when "
              "Hogan left. Booker then beat Jarrett by pinfall in an impromptu match, 13:41, "
              "for the WCW World Heavyweight Championship.",
            q_ld="How did Booker T win his first WCW World Heavyweight Championship?",
            a_ld="Booker T won his first WCW World Heavyweight Championship by pinning Jeff "
                 "Jarrett in an impromptu match at Bash at the Beach on July 9, 2000, in Daytona "
                 "Beach, Florida, on the night of the Hulk Hogan and Vince Russo incident."),
        dict(
            q="What happened between Booker T and Scott Steiner at Mayhem 2000?",
            a="Steiner took the WCW World Heavyweight Championship from him in a Straitjacket "
              "Caged Heat match in Milwaukee on <b>November 26, 2000</b>, hitting him with a "
              "chair and knocking him out with the Steiner Recliner for a technical submission. "
              "Booker won it back from Steiner on the final Nitro on March 26, 2001. The two "
              "later teamed in TNA's Main Event Mafia and won the TNA World Tag Team titles in "
              "2009.",
            q_ld="What happened between Booker T and Scott Steiner at Mayhem 2000?",
            a_ld="At WCW Mayhem on November 26, 2000, Scott Steiner won the WCW World Heavyweight "
                 "Championship from Booker T in a Straitjacket Caged Heat match by technical "
                 "submission with the Steiner Recliner. Booker T regained the title from Steiner "
                 "on the final episode of Monday Nitro on March 26, 2001."),
        dict(
            q="Who were King Booker and Queen Sharmell?",
            a="Booker's 2006&ndash;07 WWE characters. He won the 2006 King of the Ring, beating "
              "Bobby Lashley in the final at Judgment Day on May 21. William Regal crowned him on "
              "SmackDown, and he named Sharmell, his real-life wife since 2005, his Queen. As "
              "King Booker he won the World Heavyweight Championship in July 2006.",
            q_ld="Who were King Booker and Queen Sharmell?",
            a_ld="King Booker was Booker T's WWE character from 2006 to 2007, created after he "
                 "won the 2006 King of the Ring tournament. William Regal crowned him on "
                 "SmackDown, and his real-life wife Sharmell played Queen Sharmell. As King "
                 "Booker he held the World Heavyweight Championship from July to November 2006."),
        dict(
            q="Why is WrestleMania XIX remembered for Booker T?",
            a="Because of the build. On the March 3, 2003, Raw, Triple H suggested that Booker, "
              "a convicted criminal, could never win a world title in WWE. Michael Cole asked at "
              "the WrestleMania press conference whether the promo was racially insensitive. "
              "Triple H then beat Booker in Seattle on March 30, and the finish was widely "
              "disliked.",
            q_ld="What happened in Booker T vs. Triple H at WrestleMania XIX?",
            a_ld="At WrestleMania XIX on March 30, 2003, in Seattle, Triple H retained the World "
                 "Heavyweight Championship against Booker T with a Pedigree after 18 minutes 45 "
                 "seconds. The build included a Triple H promo about Booker T's criminal record "
                 "that Michael Cole questioned as racially insensitive, and the finish was "
                 "widely disliked."),
        dict(
            q="Is Booker T in the Hall of Fame twice?",
            a="Yes. Stevie Ray inducted him as a singles wrestler at Madison Square Garden on "
              "April 6, 2013, and he went in again with Harlem Heat at the Barclays Center on "
              "April 6, 2019.",
            q_ld="Is Booker T a two-time WWE Hall of Famer?",
            a_ld="Yes. Booker T was inducted into the WWE Hall of Fame as a singles wrestler in "
                 "2013, inducted by his brother Stevie Ray, and again in 2019 as part of Harlem "
                 "Heat."),
        dict(
            q="What is Reality of Wrestling?",
            a="Booker T's own promotion in Houston, founded as Pro Wrestling Alliance in 2005 "
              "and renamed in 2012. It is now an official WWE ID partner. Harlem Heat won its "
              "tag titles in a 2015 reunion, Booker beat Zilla Fatu there in 2025, and in "
              "October 2026 he handed ROW's Josiah Jean a WWE ID contract.",
            q_ld="What is Reality of Wrestling?",
            a_ld="Reality of Wrestling is a Houston wrestling promotion owned by Booker T, "
                 "founded as Pro Wrestling Alliance in 2005 and renamed in 2012. It is an "
                 "official partner in WWE's ID developmental program."),
        dict(
            q="What is Booker T's real name, and where is he from?",
            a="Booker T. Huffman Jr., born March 1, 1965, in Plain Dealing, Louisiana. He grew "
              "up in Houston, and WWE bills him from there. He has said the &ldquo;T.&rdquo; "
              "does not stand for anything.",
            q_ld="What is Booker T's real name?",
            a_ld="Booker T's real name is Booker T. Huffman Jr. He was born on March 1, 1965, in "
                 "Plain Dealing, Louisiana, grew up in Houston, Texas, and is billed from "
                 "Houston."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Booker T. Huffman Jr.",
             sub="he says the &ldquo;T.&rdquo; stands for nothing"),
        dict(label="Born", value="March 1, 1965",
             sub="Plain Dealing, Louisiana &middot; age 61 &middot; often misreported as Houston"),
        dict(label="Billed from", value="Houston, Texas"),
        dict(label="Height", value="6&#8242;3&#8243;", sub="191 cm &middot; as billed by WWE.com"),
        dict(label="Weight", value="256 lb", sub="116 kg &middot; as billed by WWE.com"),
        dict(label="Debut", value="1990", sub="as G.I. Bro, Western Wrestling Alliance"),
        dict(label="Trained by", value="Scott Casey", sub="at Ivan Putski's school"),
        dict(label="Tag partner", value="Stevie Ray", sub="his older brother Lash, as Harlem Heat"),
        dict(label="Last match", value="January 11, 2025",
             sub="W vs. Zilla Fatu, Reality of Wrestling, Texas City"),
        dict(label="Finishers", value="Scissors Kick &middot; Book End",
             sub="plus the Harlem Hangover and the Spinaroonie"),
        dict(label="Hall of Fame", value="2013 &middot; 2019", sub="solo, then with Harlem Heat"),
        dict(label="Now", value="NXT color commentator", sub="with Vic Joseph, since October 2022"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1965-03-01",
    bornplace="Plain Dealing, Louisiana, United States",
    nationality="United States",
    height_cm=191,
    weight_kg=116,
    ld=dict(
        alternateName=["Booker T. Huffman Jr.", "King Booker", "Kole", "G.I. Bro"],
        award=["WCW World Heavyweight Championship (5 reigns, 2000-2001)",
               "World Heavyweight Championship (1 reign, 2006)",
               "WCW World Tag Team Championship (11 reigns, the individual record; 10 with Stevie Ray as Harlem Heat)",
               "WCW World Television Championship (6 reigns, the record)",
               "WCW United States Heavyweight Championship (1 reign)",
               "WWE United States Championship (3 reigns)",
               "WWE Intercontinental Championship (1 reign)",
               "World Tag Team Championship (3 reigns)",
               "WWE Hardcore Championship (2 reigns)",
               "King of the Ring (2006)",
               "TNA World Tag Team Championship (1 reign, with Scott Steiner)",
               "TNA Legends Championship (inaugural)",
               "WWE Hall of Fame (2013; 2019 as Harlem Heat)"],
        knowsAbout=["Professional wrestling", "WCW", "WWE", "TNA", "Tag team wrestling",
                    "Wrestling commentary", "Wrestling promotion"],
        description="Booker T is an American professional wrestler, commentator and promoter. "
                    "With his brother Stevie Ray as Harlem Heat he won a record ten WCW World Tag "
                    "Team Championships, and he held the WCW World Heavyweight Championship five "
                    "times, including when WCW closed in 2001. As King Booker he won the 2006 King "
                    "of the Ring and the World Heavyweight Championship. He is a two-time WWE Hall "
                    "of Famer (2013, 2019), owns Reality of Wrestling in Houston, and as of "
                    "November 2026 is WWE NXT's color commentator.",
        sameAs=["https://en.wikipedia.org/wiki/Booker_T_(wrestler)",
                "https://www.wwe.com/superstars/booker-t"],
    ),
)
