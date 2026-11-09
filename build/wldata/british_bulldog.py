# -*- coding: utf-8 -*-
"""The British Bulldog (Davey Boy Smith) - dossier data.

Compiled November 9, 2026 from data/british-bulldog.md, which carries a source URL for
every claim (Wikipedia biography and event/title-history pages, WWE.com, Fox Sports,
Wrestling Inc, TJR Wrestling, Wrestling Heritage, ESPN The Magazine, Slam Wrestling,
britwrestling.co.uk, PWInsider, Fightful, CTV, A&E listing, The SmackDown Hotel).

He died on May 18, 2002. The "now" fields describe legacy only: the Class of 2020 Hall
of Fame induction and his son Harry Smith carrying the name. No activity is invented.

The old page (about 834 words) was harvested and checked. Claims it made that the
sources do not support, all dropped here and corrected in the overview:
  * two Intercontinental reigns (there was one, 1992)
  * three European reigns (there were two, 1997 and 1999)
  * WCW World Tag Team title reigns with Sting (he never held a WCW title)
  * a WWF tag title with Lex Luger (the Allied Powers lost their only title shot)
  * a powerslam finish at Wembley (he countered a sunset flip)
  * 254 lb and a Leeds hometown (WWE.com bills 260 lb from Manchester)

Deliberate omissions:
  * No walk-out theme band. Wikipedia confirms a "Rule, Britannia!" remix in the early
    WWF run, but no track title, composer or listen link was verifiable, and the band
    needs real https listen links.
  * No career win-loss total. None was verified; record.total is the row count.
  * Signature grades are this dossier's editorial grades, labelled as such. No
    Wrestling Observer rating was verified.
  * Fall Brawl 1998 (the trapdoor injury) has no record row because the source did not
    give the result. It is in the career timeline.
  * Place of death is given as "British Columbia" because sources split between
    Invermere and Fairmont Hot Springs (flagged in the .md).
  * The tag-team page /tag-teams/the-hart-foundation/ is linked from the factions slot
    by the prose auto-linker. To keep that first mention in the factions card, earlier
    sections write "the Hart Foundation" in lower case or name the members.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="1982-07-09", promo="IND", landmark=True,
         event="Stampede Wrestling, Calgary", opponent="Dynamite Kid",
         stip="Singles, against his cousin. His first North American title",
         title="Stampede British Commonwealth Mid-Heavyweight Championship"),
    dict(result="W", date="1986-04-07", promo="WWF", type="tag", landmark=True,
         event="WrestleMania 2, Rosemont", opponent="Greg Valentine & Brutus Beefcake",
         stip="Tag, with Dynamite Kid. Ozzy Osbourne and Lou Albano in the corner, 13:03",
         title="WWF Tag Team Championship"),
    dict(result="L", date="1987-01-26", promo="WWF", type="tag",
         event="Superstars taping, Tampa", opponent="Bret Hart & Jim Neidhart",
         stip="Tag, with Dynamite Kid, who could barely walk after a December 1986 back injury",
         title="WWF Tag Team Championship"),
    dict(result="L", date="1987-03-29", promo="WWF", type="tag",
         event="WrestleMania III, Pontiac", opponent="Bret Hart, Jim Neidhart & Danny Davis",
         stip="Six-man, with Dynamite Kid and Tito Santana. Davis pinned Smith after a megaphone shot",
         title=""),
    dict(result="L", date="1988-11-24", promo="WWF", type="tag",
         event="Survivor Series", opponent="Demolition's team",
         stip="10-on-10 tag elimination. The Bulldogs fell at 36:02; their side won. Last PPV as a team",
         title=""),
    dict(result="W", date="1991-03-24", promo="WWF",
         event="WrestleMania VII, Los Angeles", opponent="The Warlord",
         stip="Singles, running powerslam, 8:15", title=""),
    dict(result="L", date="1992-01-19", promo="WWF", type="tag",
         event="Royal Rumble, Albany", opponent="The 30-man Rumble field",
         stip="Entrant No. 1. Lasted 23:33 before Ric Flair threw him out", title=""),
    dict(result="W", date="1992-08-29", promo="WWF", landmark=True,
         event="SummerSlam, Wembley Stadium", opponent="Bret Hart",
         stip="Singles, 25:40. Countered a sunset flip for the pin. PWI Match of the Year",
         title="WWF Intercontinental Championship"),
    dict(result="L", date="1992-10-27", promo="WWF",
         event="Saturday Night's Main Event XXXI", opponent="Shawn Michaels",
         stip="Singles. Taped in Terre Haute, aired November 14",
         title="WWF Intercontinental Championship"),
    dict(result="W", date="1993-02-21", promo="WCW",
         event="SuperBrawl III, Asheville", opponent="Bill Irwin",
         stip="Singles, his WCW debut, 5:49", title=""),
    dict(result="W", date="1993-05-23", promo="WCW",
         event="Slamboree, Atlanta", opponent="Vader",
         stip="Won by disqualification, so the title stayed with Vader",
         title="WCW World Heavyweight Championship"),
    dict(result="L", date="1995-01-22", promo="WWF", type="tag",
         event="Royal Rumble, Tampa", opponent="The 30-man Rumble field",
         stip="Entered No. 2 and reached the final two. Michaels skinned the cat and won", title=""),
    dict(result="W", date="1995-04-02", promo="WWF", type="tag",
         event="WrestleMania XI, Hartford", opponent="Eli & Jacob Blu",
         stip="Tag, with Lex Luger as the Allied Powers, 6:34", title=""),
    dict(result="W", date="1995-10-22", promo="WWF",
         event="In Your House 4, Winnipeg", opponent="Diesel",
         stip="Won by disqualification after Bret Hart interfered. Title stays with Diesel",
         title="WWF Championship"),
    dict(result="L", date="1995-12-17", promo="WWF",
         event="In Your House 5, Hershey", opponent="Bret Hart",
         stip="Singles, 21:09", title="WWF Championship"),
    dict(result="D", date="1996-05-26", promo="WWF",
         event="In Your House 8: Beware of Dog", opponent="Shawn Michaels",
         stip="Both men pinned at once. Ruled a draw; Michaels kept the title",
         title="WWF Championship"),
    dict(result="L", date="1996-06-23", promo="WWF",
         event="King of the Ring, Milwaukee", opponent="Shawn Michaels",
         stip="Singles, superkick, 26:24. Mr. Perfect was the outside referee",
         title="WWF Championship"),
    dict(result="W", date="1996-09-22", promo="WWF", type="tag", landmark=True,
         event="In Your House: Mind Games, Philadelphia", opponent="The Smoking Gunns",
         stip="Tag, with Owen Hart. Powerslam on Bart Gunn, 10:59",
         title="WWF Tag Team Championship"),
    dict(result="W", date="1997-02-26", promo="WWF", landmark=True,
         event="Raw, Berlin", opponent="Owen Hart",
         stip="Tournament final, about 20 minutes. Crowned the first European Champion. Aired March 3",
         title="WWF European Championship"),
    dict(result="W", date="1997-07-06", promo="WWF", type="tag", landmark=True,
         event="In Your House 16: Canadian Stampede, Calgary",
         opponent="Steve Austin, Ken Shamrock, Goldust & the Legion of Doom",
         stip="10-man tag for the reunited Hart family stable, before 12,151", title=""),
    dict(result="L", date="1997-09-20", promo="WWF", landmark=True,
         event="One Night Only, Birmingham", opponent="Shawn Michaels",
         stip="Main event, technical submission, 22:53. Ended a 206-day reign",
         title="WWF European Championship"),
    dict(result="W", date="1997-11-09", promo="WWF", type="tag",
         event="Survivor Series, Montreal", opponent="Vader, Goldust, Marc Mero & Steve Blackman",
         stip="Team Canada vs Team USA. Sole survivor, pinned Vader, 17:05", title=""),
    dict(result="L", date="1999-09-26", promo="WWF", type="tag",
         event="Unforgiven, Charlotte", opponent="Six-pack challenge field",
         stip="Vacant title. Hit The Rock with a chair; Triple H won", title="WWF Championship"),
    dict(result="W", date="1999-10-02", promo="WWF",
         event="Rebellion, Birmingham", opponent="X-Pac",
         stip="Singles, 5:23", title=""),
    dict(result="W", date="1999-10-26", promo="WWF",
         event="SmackDown taping, Springfield", opponent="D'Lo Brown",
         stip="Singles. WWE dates the reign from the October 28 broadcast",
         title="WWF European Championship"),
    dict(result="L", date="1999-12-12", promo="WWF", type="tag",
         event="Armageddon, Sunrise", opponent="Val Venis & D'Lo Brown",
         stip="Triple threat. Venis pinned him", title="WWF European Championship"),
    dict(result="W", date="2000-05-06", promo="WWF",
         event="Insurrextion, London", opponent="Crash Holly",
         stip="Singles, 3:37. Holly took it back five days later",
         title="WWF Hardcore Championship"),
    dict(result="W", date="2002-05-11", promo="IND", type="tag", landmark=True,
         event="Southdale Community Centre, Winnipeg", opponent="TJ Bratt, Robby Royce & The Axe",
         stip="Six-man, with his son Harry Smith and Zack Mercury. Powerslam for the pin. A week before his death",
         title=""),
]

DATA = dict(
    slug="british-bulldog",
    name="British Bulldog",
    realname="David Smith",
    epithet="Davey Boy Smith",
    hook="Record & Titles",
    art="british-bulldog",

    meta_desc=("The British Bulldog, Davey Boy Smith: WWF tag champion with Dynamite Kid at "
               "WrestleMania 2, beat Bret Hart at Wembley in 1992, first European Champion, "
               "Hall of Fame 2020. Full record, titles and career."),
    og_desc=("Davey Boy Smith: tag gold at WrestleMania 2, the Wembley win over Bret Hart, the "
             "first WWF European Championship, the 1997 Hart family stable, and the Hall of Fame "
             "in 2020."),
    tw_desc="The British Bulldog: WrestleMania 2 tag gold, Wembley 1992, the first European title, HOF 2020.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1978",
    height_imp="5&#8242;11&#8243;",
    weight_lb="260",
    vitals_tagline="The British Bulldog",
    support_note="Shop &middot; Games &middot; Watch",
    sp_items=[
        dict(ic="WWE", title="WWE Shop", sub="Legends merchandise",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K22", sub="Playable legend · Clowning Around Pack",
             tag="Play", href="https://www.thesmackdownhotel.com/roster/wwe2k22/the-british-bulldog"),
        dict(ic="A&E", title="Biography: WWE Legends", sub="\"British Bulldog\" · March 24, 2024",
             tag="Watch", href="https://thetvdb.com/series/biography-wwe-legends/episodes/10257914"),
        dict(ic="HOF", title="Official Profile", sub="WWE.com · Hall of Fame 2020", tag="Visit",
             charity=True, href="https://www.wwe.com/superstars/britishbulldog"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The British Bulldogs &middot; Wembley 1992 &middot; first European Champion &middot; Hall of Fame 2020",
    hero_tag="Golborne, Lancashire &middot; billed from Manchester, England &middot; "
             "<em>Britain &middot; Stampede &middot; Japan &middot; WWF &middot; WCW &middot; 1978&ndash;2002</em>",
    now_label="LEGACY",
    now_bold="WWE Hall of Fame, Class of 2020",
    now_tail=(" &middot; died May 18, 2002, aged 39 &middot; his son Harry Smith wrestles as Davey "
              "Boy Smith Jr. and recovered his father's stolen Hall of Fame ring in February 2026"),
    hstats=[
        dict(value="2",    x=True,  label="WWF Tag Titles"),
        dict(value="1st",  x=False, label="European Champion"),
        dict(value="1992", x=False, label="Wembley Main Event"),
        dict(value="2020", x=False, label="Hall of Fame Class"),
    ],
    ghost_link="From a Lancashire mill town to the Wembley main event",
    vlabel="1962&ndash;2002 &middot; Golborne, Lancashire",
    mono="BB",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Davey Boy Smith</b> headlined the biggest crowd the WWF had drawn outside North "
        "America, and he did it at home. On August 29, 1992 at Wembley Stadium he beat his "
        "brother-in-law Bret Hart for the Intercontinental Championship, with his wife Diana, "
        "Bret's sister, at ringside. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">78,927</span>'
        '<span class="pull-cap">the cited Wembley attendance for SummerSlam 1992. The WWF claimed 80,355</span></span>'
        "The rest of the record fits around that night. He won the WWF Tag Team Championship "
        "with his cousin Dynamite Kid at WrestleMania 2. He won it again with Owen Hart in "
        "1996. He became the first WWF European Champion in Berlin in 1997 and held that belt "
        "for 206 days, the longest reign it ever had. WWE inducted him into the Hall of Fame "
        "as part of the Class of 2020.",

        "The old version of this page got several titles wrong, and the errors are common "
        "elsewhere too. He held the Intercontinental Championship once, not twice. He held "
        "the European Championship twice, not three times. He never held a WCW title of any "
        "kind, with Sting or anyone else. The Allied Powers team with Lex Luger lost its only "
        "tag title shot, at In Your House 2 in 1995. The Wembley finish was not a powerslam: "
        "Hart went for a sunset flip and Smith sat down on it for the pin. One more number "
        "needs care. The WWF announced 80,355 for that show, and the cited figure is 78,927. "
        "This page uses the cited figure and flags the claim.",

        "He was born David Smith on November 27, 1962 in Golborne, Lancashire. He was trained "
        "by Ted Betley and was on British television as Young David by 1978, at about 15. "
        "In 1981 he left for Calgary and Stu Hart's Stampede Wrestling. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">294</span>'
        '<span class="pull-cap">days as WWF Tag Team Champions with Dynamite Kid, from WrestleMania 2 to January 1987</span></span>'
        "There he and Tom Billington, the Dynamite Kid, became The British Bulldogs. The team "
        "worked Stampede, New Japan and All Japan before the WWF signed them in 1984. They won "
        "the tag titles from Greg Valentine and Brutus Beefcake on April 7, 1986, with Ozzy "
        "Osbourne in their corner. Dynamite Kid hurt his back badly that December, and the "
        "belts went to Bret Hart and Jim Neidhart, the original Hart Foundation team, on "
        "January 26, 1987. He married Diana Hart in October 1984. That made him family to the "
        "men he would spend the next decade facing and joining.",

        "The singles career ran in pieces. He returned to the WWF in 1990, beat The Warlord at "
        "WrestleMania VII, and was released after losing the Intercontinental title to Shawn "
        "Michaels in late 1992. WCW had him for most of 1993. Back in the WWF from 1994, he "
        "reached the final two of the 1995 Royal Rumble and turned on Diesel that August. He "
        "then challenged for the WWF Championship against Diesel, Bret Hart and Michaels. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">206</span>'
        '<span class="pull-cap">days as the first WWF European Champion, the longest reign in the title&rsquo;s history</span></span>'
        "In 1997 he joined Bret Hart, Owen Hart, Jim Neidhart and Brian Pillman in the "
        "reunited Hart family stable. The group was cheered in Canada and Europe and booed in "
        "the United States. He left for WCW after the Montreal Survivor Series. A back injury "
        "on a ring trapdoor at Fall Brawl in September 1998 led to a spinal infection and about "
        "six months in hospital. He came back to the WWF in 1999, won the European and "
        "Hardcore titles, and left in May 2000.",

        "Davey Boy Smith died of a heart attack on May 18, 2002, while on vacation in British "
        "Columbia. He was 39. A week earlier he had teamed with his son Harry in a six-man "
        "match in Winnipeg. WWE announced his Hall of Fame induction on March 12, 2020. The "
        "pandemic delayed the ceremony, and Harry, his daughter Georgia and Diana Hart-Smith "
        "inducted him on the broadcast of April 6, 2021. As of November 9, 2026, Harry still "
        "wrestles under the family name as Davey Boy Smith Jr. In February 2026 he got back "
        "his father's Hall of Fame ring after it was stolen from a ring truck in Canada.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Highlight set",
        promo_order=["WWF", "WCW", "IND"],
        promo_labels={"WWF": "WWF", "WCW": "WCW", "IND": "Stampede &amp; indies"},
        stats=[
            ("2&times;", "WWF tag titles"),
            ("1&times;", "Intercontinental title"),
            ("2&times;", "European titles"),
            ("2&times;", "Hardcore titles"),
            ("5",        "WWF title shots"),
            ("2002",     "Last match"),
        ],
        lead=("Twenty-eight documented bouts from 1982 to 2002. This is a highlight set, not a "
              "career count. No career win&ndash;loss total is published because none was "
              "verified. The British television years and most of the Stampede and Japan "
              "tours are outside this ledger. The 1996 In Your House 8 match is logged as a "
              "draw, as the event report describes it. The two Royal Rumbles and the Unforgiven "
              "six-pack are filed under multi-man bouts. Filter by promotion or match type, "
              "tap a column header to sort, and turn spoilers on to see results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("Four matches the reputation rests on. The grades are this dossier's own "
                    "editorial placeholders, not Wrestling Observer ratings. No Observer rating "
                    "was verified for this page and none is quoted."),
    signature=[
        dict(rating="4.5", event="SummerSlam 1992", opponent="Bret Hart",
             stip="Wembley Stadium main event for the Intercontinental title. PWI Match of the Year"),
        dict(rating="4.0", event="Raw, February 26, 1997", opponent="Owen Hart",
             stip="Berlin tournament final. Crowned the first WWF European Champion"),
        dict(rating="4.0", event="One Night Only 1997", opponent="Shawn Michaels",
             stip="European title main event in Birmingham. The reign ends on British soil"),
        dict(rating="3.5", event="King of the Ring 1996", opponent="Shawn Michaels",
             stip="WWF Championship challenge, 26:24, with Mr. Perfect outside"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("2&times;", "WWF tag reigns"),
            ("1&times;", "Intercontinental reign"),
            ("2&times;", "European reigns"),
            ("2020",     "Hall of Fame"),
        ],
        lead=("Seven WWF reigns across four titles, plus a Stampede trophy shelf. He never held "
              "a world title, and he never held a WCW title. Reign lengths come from the title "
              "histories cited in the research file."),
        rows=[
            dict(ic="T", name="WWF World Tag Team Championship", count="2",
                 sub="With Dynamite Kid: won from Greg Valentine &amp; Brutus Beefcake at "
                     "WrestleMania 2, April 7, 1986, held 294 days, lost to Bret Hart &amp; Jim "
                     "Neidhart on January 26, 1987 &middot; With Owen Hart: won from the "
                     "Smoking Gunns at In Your House: Mind Games, September 22, 1996, held 246 "
                     "days, lost to Steve Austin &amp; Shawn Michaels on Raw, May 26, 1997"),
            dict(ic="IC", name="WWF Intercontinental Championship", count="1",
                 sub="Won from Bret Hart at SummerSlam, Wembley Stadium, August 29, 1992 "
                     "&middot; lost to Shawn Michaels at Saturday Night's Main Event, taped "
                     "October 27 and aired November 14, 1992 &middot; 59 days (WWE counts 58)"),
            dict(ic="EU", name="WWF European Championship", count="2",
                 sub="Inaugural champion: beat Owen Hart in the tournament final in Berlin, "
                     "February 26, 1997, held 206 days, the longest reign in the title's "
                     "history, lost to Shawn Michaels at One Night Only, September 20, 1997 "
                     "&middot; Won from D'Lo Brown on SmackDown, October 26, 1999 (WWE dates it "
                     "October 28), lost to Val Venis at Armageddon, December 12, 1999"),
            dict(ic="HC", name="WWF Hardcore Championship", count="2",
                 sub="Won from Big Boss Man, September 9, 1999, and forfeited it the same night "
                     "&middot; won from Crash Holly at Insurrextion in London, May 6, 2000; "
                     "Holly regained it May 11"),
            dict(ic="S", name="Stampede Wrestling titles", count="8",
                 sub="British Commonwealth Mid-Heavyweight (1, won from Dynamite Kid, July 9, "
                     "1982) &middot; World Mid-Heavyweight (1) &middot; North American "
                     "Heavyweight (2) &middot; International Tag Team (2 with Bruce Hart, 2 "
                     "with Dynamite Kid) &middot; Stampede Wrestling Hall of Fame, 1995"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Teams &amp; Factions",
        lead="Nearly every team he joined was family by blood or by marriage.",
        cards=[
            dict(era="Stampede &middot; Japan &middot; WWF &middot; 1983&ndash;1989",
                 name="The British Bulldogs",
                 members="Davey Boy Smith, Dynamite Kid (Tom Billington)",
                 desc="Two cousins from the Wigan area who met again in Calgary. Their power and "
                      "speed won the Wrestling Observer's Tag Team of the Year in 1985 and the "
                      "WWF titles at WrestleMania 2, with Matilda the bulldog as the team "
                      "mascot. They left the WWF after the 1988 Survivor Series and split in "
                      "Stampede in May 1989. The relationship soured badly afterward, "
                      "including a fight over who could use the British Bulldog name."),
            dict(era="WWF &middot; 1995",
                 name="The Allied Powers",
                 members="Lex Luger, British Bulldog",
                 desc="A short babyface pairing built on an American and a Briton. It won at "
                      "WrestleMania XI and lost its one tag title match at In Your House 2. It "
                      "ended in August 1995 when Smith attacked Diesel and went over to Jim "
                      "Cornette."),
            dict(era="WWF &middot; 1995&ndash;1997",
                 name="Camp Cornette / Owen Hart &amp; British Bulldog",
                 members="Owen Hart, British Bulldog, with Yokozuna and Vader in the wider camp",
                 desc="The in-laws as a heel tag team. They debuted together at WrestleMania XII, "
                      "took the tag titles from the Smoking Gunns in September 1996 and held "
                      "them 246 days. The partnership cracked when Smith beat Owen for the "
                      "European title in February 1997, and it was repaired on Raw that March."),
            dict(era="WWF &middot; 1997",
                 name="The 1997 Hart family stable",
                 members="Bret Hart, Owen Hart, British Bulldog, Jim Neidhart, Brian Pillman",
                 desc="The Hart Foundation began as the tag team of Bret Hart and Jim Neidhart, "
                      "and in 1997 Bret rebuilt it as a five-man stable. The group was "
                      "pro-Canada and anti-American, heroes in Calgary and Birmingham and "
                      "villains in the US. It won the 10-man main event at Canadian Stampede, "
                      "and its war with Steve Austin was the Observer's Feud of the Year. It "
                      "ended with the Montreal Survivor Series in November 1997."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One name for most of the career. The eras changed with the company around him.",
        cards=[
            dict(mono="YD", era="Britain &middot; 1978&ndash;1981", name="Young David",
                 desc="A teenage television wrestler trained by Ted Betley. He was briefly a tag "
                      "partner for Big Daddy, and in December 1979 he took two falls from "
                      "welterweight champion Jim Breaks in a title match the officials "
                      "disallowed."),
            dict(mono="BD", era="Stampede &middot; WWF &middot; 1983&ndash;1988", name="Davey Boy Smith of the Bulldogs",
                 desc="The power half of the Dynamite Kid team: short hair, Union Jack gear, a "
                      "bulldog named Matilda. The Observer's best move award in 1984 went to "
                      "his power clean dropkick."),
            dict(mono="UK", era="WWF &middot; 1990&ndash;1997", name="The British Bulldog",
                 desc="The singles star, billed at 260 lb from Manchester, finishing with the "
                      "running powerslam. A babyface through Wembley, a heel in Camp Cornette, "
                      "and a national hero again in the 1997 Hart family stable."),
            dict(mono="WC", era="WCW &middot; 1993, 1997&ndash;1998", name="Davey Boy Smith in WCW",
                 desc="Two stints. The first, in 1993, ended with his release that December. The "
                      "second, after Montreal, ended with the Fall Brawl trapdoor injury and a "
                      "six-month hospital stay."),
            dict(mono="99", era="WWF &middot; 1999&ndash;2000", name="The jeans-era heel",
                 desc="Back in September 1999 in denim, siding with Triple H at Unforgiven. He "
                      "won the European title one more time and the Hardcore title in London, "
                      "and left in May 2000."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Lancashire to Calgary to Wembley, in twenty-four years.",
        rows=[
            dict(year="1978", title="Young David",
                 desc="Television debut at about 15, trained by Ted Betley."),
            dict(year="1981", title="To Calgary",
                 desc="A month in South Africa, then Stu Hart's Stampede Wrestling, where he "
                      "trains in the Hart family Dungeon."),
            dict(year="1982", title="First Stampede title",
                 desc="Beats Dynamite Kid for the British Commonwealth Mid-Heavyweight "
                      "Championship on July 9."),
            dict(year="1984", title="The Bulldogs and the WWF",
                 desc="The team wins its first Stampede International tag title in March and "
                      "joins the WWF when Vince McMahon buys Stampede. Smith marries Diana Hart "
                      "in October."),
            dict(year="1986", title="Tag champions at WrestleMania 2",
                 desc="Beat Greg Valentine and Brutus Beefcake on April 7 with Ozzy Osbourne in "
                      "the corner. Dynamite Kid's back gives out in December."),
            dict(year="1987", title="The belts go to the in-laws",
                 desc="Lose the titles to Bret Hart and Jim Neidhart on January 26, then lose "
                      "the WrestleMania III six-man on March 29."),
            dict(year="1988", title="Out of the WWF",
                 desc="The 1988 Survivor Series on November 24 is the team's last WWF "
                      "pay-per-view. They leave after backstage trouble with the Rougeaus."),
            dict(year="1990", title="A singles return",
                 desc="The team's last match is January 28 in All Japan. Smith is back in the WWF "
                      "by October."),
            dict(year="1992", title="Wembley",
                 desc="Enters the Royal Rumble first on January 19 and lasts 23:33. Beats Bret "
                      "Hart at SummerSlam on August 29, loses the title to Shawn Michaels, and is "
                      "released."),
            dict(year="1993", title="WCW, briefly",
                 desc="Debuts at SuperBrawl III on February 21 and wins by disqualification "
                      "over Vader at Slamboree on May 23. Released in December."),
            dict(year="1994", title="Home again",
                 desc="Returns to the WWF at SummerSlam on August 29, in the middle of the Hart "
                      "family feud."),
            dict(year="1995", title="Final two, then a turn",
                 desc="Runner-up in the Royal Rumble from No. 2, a WrestleMania XI win with Lex "
                      "Luger, a heel turn on Diesel in August, and WWF title shots against Diesel "
                      "and Bret Hart."),
            dict(year="1996", title="Title shots and tag gold",
                 desc="A draw and a loss against Shawn Michaels for the WWF Championship, then "
                      "the tag titles with Owen Hart on September 22."),
            dict(year="1997", title="The first European Champion",
                 desc="Wins the Berlin final on February 26, rejoins Bret in the Hart family "
                      "stable, loses the belt at One Night Only on September 20, survives the "
                      "Montreal Survivor Series on November 9, and leaves for WCW."),
            dict(year="1998", title="The trapdoor",
                 desc="Hurt on a ring trapdoor at Fall Brawl on September 13. A spinal infection "
                      "keeps him in hospital about six months, and WCW ends his contract."),
            dict(year="1999", title="One more WWF run",
                 desc="Returns in September, sides with Triple H at Unforgiven, beats X-Pac at "
                      "Rebellion, and holds the European title from October 26 to December 12."),
            dict(year="2000", title="Last WWF title",
                 desc="Wins the Hardcore title in London on May 6 and leaves the company on "
                      "May 15."),
            dict(year="2002", title="Death at 39",
                 desc="Teams with his son Harry in Winnipeg on May 11. Dies of a heart attack on "
                      "May 18 while on vacation in British Columbia."),
            dict(year="2020", title="Hall of Fame",
                 desc="Announced on March 12. The ceremony, delayed by the pandemic, is broadcast "
                      "April 6, 2021, with Harry, Georgia and Diana inducting him."),
            dict(year="2026", title="The ring comes home",
                 desc="Harry's gear bag is stolen from a ring truck in Canada in February. The "
                      "Hall of Fame ring inside it is recovered after an attempted pawn."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Most of his great opponents were also his partners at some point.",
        cards=[
            dict(name="Bret Hart", slug="bret-hart",
                 desc="His brother-in-law, and the opponent of his career. Bret's team took the "
                      "tag titles from the Bulldogs in 1987. Smith took the Intercontinental "
                      "title from Bret at Wembley in 1992, and Bret beat him for the WWF "
                      "Championship at In Your House 5 in 1995. In 1997 they stood together in "
                      "the Hart family stable. Bret has called the Wembley match his favorite."),
            dict(name="Shawn Michaels", slug="shawn-michaels",
                 desc="The man who ended his two best singles reigns. Michaels took the "
                      "Intercontinental title in 1992 and the European title at One Night Only "
                      "in 1997. In between came the 1995 Rumble final two, a 1996 draw, and the "
                      "King of the Ring title match."),
            dict(name="Owen Hart", slug="owen-hart",
                 desc="Brother-in-law, tag partner and the first European final opponent. They "
                      "won the tag titles in 1996, fought for the new belt in Berlin in 1997, "
                      "brawled on Raw a month later, and were pulled back together by Bret."),
            dict(name="Dynamite Kid",
                 desc="Cousin, partner and later bitter rival. They feuded in Stampede after the "
                      "1989 split, and they fought over the British Bulldog name for years. "
                      "Tom Billington died on December 5, 2018, his 60th birthday."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        lead="Television, games, and a documentary still in the works.",
        rows=[
            dict(when="2024", title="Biography: WWE Legends, \"British Bulldog\"", kind="TV",
                 desc="A&E's season 4 episode on his life, which aired March 24, 2024."),
            dict(when="2022", title="WWE 2K22", kind="Game",
                 desc="A playable legend, added in the Clowning Around Pack. He also appears on "
                      "the WWE 2K16 and 2K19 rosters."),
            dict(when="2021", title="Davey Boy (in development)", kind="Film",
                 desc="A feature documentary announced by The City Talking Studios in Leeds. No "
                      "release date was found."),
            dict(when="1992", title="SummerSlam at Wembley", kind="Event",
                 desc="Aired on tape delay on August 31, 1992. WWE has called his match with Bret "
                      "Hart the greatest moment in SummerSlam history."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="Firsts and finals, each with a source behind it.",
        stats=[
            ("1st", "WWF European Champion"),
            ("206", "Days, longest European reign"),
            ("1992", "PWI Match of the Year"),
        ],
        rows=[
            dict(name="The first WWF European Champion",
                 sub="Beat Owen Hart in the tournament final in Berlin on February 26, 1997. His "
                     "206-day first reign is the longest in the title's history."),
            dict(name="Main event at Wembley Stadium",
                 sub="Beat Bret Hart for the Intercontinental title on August 29, 1992, before a "
                     "cited 78,927 (the WWF claimed 80,355). WWE now recognizes it as the "
                     "show's main event."),
            dict(name="PWI Match of the Year, 1992",
                 sub="For the Wembley match with Bret Hart."),
            dict(name="WWF Tag Team Champion with two partners",
                 sub="With Dynamite Kid in 1986 and Owen Hart in 1996."),
            dict(name="Sole survivor in Montreal",
                 sub="Pinned Vader to win Team Canada's match at Survivor Series, November 9, "
                     "1997."),
            dict(name="Royal Rumble final two, 1995",
                 sub="Entered second and lasted to the end against Shawn Michaels."),
            dict(name="Wrestling Observer awards",
                 sub="Tag Team of the Year 1985 with Dynamite Kid, Best Wrestling Maneuver 1984, "
                     "and Feud of the Year 1997 as part of the Hart family stable against Steve "
                     "Austin."),
            dict(name="Hall of Fame recognition",
                 sub="WWE Hall of Fame Class of 2020, Stampede Wrestling Hall of Fame 1995, and "
                     "both Canadian wrestling halls of fame."),
        ],
        footnote=("No career win-loss total appears on this page. None was verified, and the "
                  "British and Stampede records are mostly undocumented in the sources used."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="WWE.com", v="Official Hall of Fame profile", href="https://www.wwe.com/superstars/britishbulldog"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Davey_Boy_Smith"),
        dict(k="Wikipedia", v="The British Bulldogs", href="https://en.wikipedia.org/wiki/The_British_Bulldogs"),
        dict(k="Wrestling Heritage", v="The Young David years in Britain",
             href="https://wrestlingheritage.co.uk/davey-boy-smith/"),
        dict(k="Wrestling Inc", v="Hall of Fame 2020 ceremony recap",
             href="https://www.wrestlinginc.com/news/2021/04/wwe-hall-of-fame-induction-ceremony-live-recap-your-feedback-and-viewing-party"),
        dict(k="PWInsider", v="Hall of Fame ring recovered, February 2026",
             href="https://pwinsider.com/article/205446/davey-boy-smiths-wwe-hall-of-fame-ring-recovered.html?p=1"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/british-bulldog.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="How did the British Bulldog die?",
            a="Davey Boy Smith died of a <b>heart attack on May 18, 2002</b>, while on vacation "
              "in British Columbia, Canada. He was 39. Reports name the town as Invermere or "
              "nearby Fairmont Hot Springs. A week earlier he had wrestled alongside his son "
              "Harry in Winnipeg.",
            q_ld="How did the British Bulldog Davey Boy Smith die?",
            a_ld="Davey Boy Smith, the British Bulldog, died of a heart attack on May 18, 2002, "
                 "while on vacation in British Columbia, Canada. He was 39 years old."),
        dict(
            q="Is the British Bulldog in the WWE Hall of Fame?",
            a="Yes. WWE announced him for the <b>Class of 2020</b> on March 12, 2020. The "
              "pandemic pushed the ceremony back, and he was inducted on the broadcast of April "
              "6, 2021 by his son Harry, his daughter Georgia and Diana Hart-Smith.",
            q_ld="Is the British Bulldog in the WWE Hall of Fame?",
            a_ld="Yes. Davey Boy Smith was inducted into the WWE Hall of Fame as part of the Class "
                 "of 2020. The ceremony was delayed by the pandemic and broadcast on April 6, "
                 "2021, with his son Harry Smith, daughter Georgia Smith and Diana Hart-Smith "
                 "inducting him."),
        dict(
            q="Who won at SummerSlam 1992, and how big was the crowd?",
            a="The British Bulldog beat <b>Bret Hart</b> for the Intercontinental Championship "
              "at Wembley Stadium on August 29, 1992, countering a sunset flip for the pin after "
              "25:40. The cited attendance is 78,927. The WWF claimed 80,355. Pro Wrestling "
              "Illustrated named it Match of the Year.",
            q_ld="Who won the SummerSlam 1992 main event at Wembley Stadium?",
            a_ld="The British Bulldog, Davey Boy Smith, defeated Bret Hart for the WWF "
                 "Intercontinental Championship at SummerSlam on August 29, 1992 at Wembley "
                 "Stadium in London. The cited attendance is 78,927; the WWF claimed 80,355. "
                 "Pro Wrestling Illustrated named it the 1992 Match of the Year."),
        dict(
            q="Was the British Bulldog the first WWF European Champion?",
            a="Yes. He beat <b>Owen Hart</b> in the tournament final in Berlin on February 26, "
              "1997, which aired on Raw on March 3. He held it 206 days, the longest reign in the "
              "title's history, and lost it to Shawn Michaels at One Night Only in Birmingham. "
              "He won it a second time from D'Lo Brown in October 1999.",
            q_ld="Was the British Bulldog the first WWF European Champion?",
            a_ld="Yes. The British Bulldog won the inaugural WWF European Championship by "
                 "defeating Owen Hart in a tournament final in Berlin on February 26, 1997. His "
                 "206-day first reign is the longest in the title's history. He held the title "
                 "twice."),
        dict(
            q="Who was in The British Bulldogs tag team?",
            a="Davey Boy Smith and his cousin <b>Tom Billington, the Dynamite Kid</b>. They "
              "formed in Stampede Wrestling, won the WWF Tag Team Championship at WrestleMania 2 "
              "on April 7, 1986, and held it 294 days. They split in 1989. Dynamite Kid died in "
              "2018.",
            q_ld="Who were The British Bulldogs in wrestling?",
            a_ld="The British Bulldogs were Davey Boy Smith and his cousin Tom Billington, known "
                 "as the Dynamite Kid. They won the WWF Tag Team Championship from Greg "
                 "Valentine and Brutus Beefcake at WrestleMania 2 on April 7, 1986 and held it "
                 "for 294 days."),
        dict(
            q="How was the British Bulldog related to Bret Hart?",
            a="He married <b>Diana Hart</b>, sister of Bret and Owen Hart, in October 1984. That "
              "made both men his brothers-in-law. He trained in Stu Hart's Dungeon in Calgary, "
              "and he joined Bret and Owen in the 1997 Hart family stable. The marriage ended in "
              "divorce in January 2000.",
            q_ld="How was the British Bulldog related to Bret Hart?",
            a_ld="Davey Boy Smith married Diana Hart, the sister of Bret Hart and Owen Hart, in "
                 "October 1984, making him their brother-in-law. They divorced in January 2000."),
        dict(
            q="How many championships did the British Bulldog win in WWF?",
            a="Seven reigns across four titles: the <b>World Tag Team Championship twice</b> "
              "(with Dynamite Kid and Owen Hart), the <b>Intercontinental Championship once</b>, "
              "the <b>European Championship twice</b>, and the <b>Hardcore Championship twice</b>. "
              "He never won a world title. Claims of a second IC reign, a third European reign, "
              "or WCW tag titles with Sting are wrong.",
            q_ld="How many championships did the British Bulldog win in WWF?",
            a_ld="The British Bulldog held seven WWF championship reigns: the World Tag Team "
                 "Championship twice, the Intercontinental Championship once, the European "
                 "Championship twice and the Hardcore Championship twice. He never held a world "
                 "title or any WCW title."),
        dict(
            q="What was the British Bulldog's finishing move?",
            a="The <b>running powerslam</b>. He won with it at WrestleMania VII against The "
              "Warlord and to take the tag titles at In Your House: Mind Games. His biggest win "
              "came another way: at Wembley he sat down on a Bret Hart sunset flip for the pin.",
            q_ld="What was the British Bulldog's finishing move?",
            a_ld="The British Bulldog's finishing move was the running powerslam. His SummerSlam "
                 "1992 win over Bret Hart came from countering a sunset flip instead."),
        dict(
            q="Is Harry Smith the British Bulldog's son?",
            a="Yes. <b>Harry Smith</b>, born August 2, 1985 in Calgary, wrestled in WWE as DH "
              "Smith and David Hart Smith, winning tag gold with Tyson Kidd in 2010, and later "
              "became Davey Boy Smith Jr. He held the IWGP tag titles three times and the AJPW "
              "Triple Crown in 2024. In 2015 he acquired the British Bulldog trademark.",
            q_ld="Is Harry Smith the son of the British Bulldog?",
            a_ld="Yes. Harry Smith, known as Davey Boy Smith Jr., is the son of Davey Boy Smith "
                 "and Diana Hart. He won WWE tag team gold with Tyson Kidd as The Hart Dynasty in "
                 "2010, and later held the IWGP Tag Team Championship and the AJPW Triple Crown "
                 "Heavyweight Championship."),
        dict(
            q="What was the British Bulldog's real name?",
            a="<b>David Smith</b>. He was born November 27, 1962 in Golborne, Lancashire, worked "
              "as Young David as a teenager, and became Davey Boy Smith in Stampede. WWE bills "
              "him from Manchester.",
            q_ld="What was the British Bulldog's real name?",
            a_ld="The British Bulldog's real name was David Smith. He was born on November 27, "
                 "1962 in Golborne, Lancashire, England."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="David Smith"),
        dict(label="Born", value="November 27, 1962", sub="Golborne, Lancashire, England"),
        dict(label="Died", value="May 18, 2002", sub="Heart attack, British Columbia &middot; aged 39"),
        dict(label="Billed from", value="Manchester, England", sub="per WWE.com"),
        dict(label="Height", value="5&#8242;11&#8243;", sub="180 cm &middot; billed"),
        dict(label="Weight", value="260 lb", sub="118 kg &middot; billed"),
        dict(label="Debut", value="1978", sub="British TV, as Young David"),
        dict(label="Trained by", value="Ted Betley &middot; Stu Hart", sub="the Hart family Dungeon, Calgary"),
        dict(label="Finisher", value="Running powerslam"),
        dict(label="Tag partners", value="Dynamite Kid &middot; Owen Hart &middot; Lex Luger"),
        dict(label="Last match", value="May 11, 2002", sub="W, six-man in Winnipeg with son Harry"),
        dict(label="Hall of Fame", value="Class of 2020", sub="inducted by Harry, Georgia and Diana"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1962-11-27",
    bornplace="Golborne, Lancashire, England",
    nationality="United Kingdom",
    height_cm=180,
    weight_kg=118,
    ld=dict(
        alternateName=["Davey Boy Smith", "David Smith", "The British Bulldog", "Young David"],
        award=["WWF World Tag Team Championship (2 reigns: with Dynamite Kid, 1986; with Owen Hart, 1996)",
               "WWF Intercontinental Championship (1 reign, 1992)",
               "WWF European Championship (2 reigns, inaugural champion, 1997)",
               "WWF Hardcore Championship (2 reigns)",
               "WWE Hall of Fame (Class of 2020)",
               "Pro Wrestling Illustrated Match of the Year (1992)"],
        knowsAbout=["Professional wrestling", "WWE", "Tag team wrestling", "Stampede Wrestling",
                    "British wrestling"],
        description="Davey Boy Smith, the British Bulldog, was an English professional wrestler "
                    "and 2020 WWE Hall of Fame inductee. With his cousin Dynamite Kid he won the "
                    "WWF Tag Team Championship at WrestleMania 2. He beat Bret Hart for the "
                    "Intercontinental Championship at SummerSlam 1992 at Wembley Stadium, became "
                    "the first WWF European Champion in 1997, and was part of the 1997 Hart "
                    "Foundation stable. He died of a heart attack on May 18, 2002, aged 39.",
        sameAs=["https://www.wwe.com/superstars/britishbulldog",
                "https://en.wikipedia.org/wiki/Davey_Boy_Smith"],
    ),
)
