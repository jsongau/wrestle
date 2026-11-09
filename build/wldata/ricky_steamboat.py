# -*- coding: utf-8 -*-
"""Ricky Steamboat - dossier data.

Compiled November 9, 2026 from data/ricky-steamboat.md (every fact there carries a URL).
Sources: Wikipedia (biography, the four championship lists, Meltzer's 5-star list and the
event pages for every dated row), WWE.com profile, prowrestling.net's 2009 Hall of Fame
report, the Mid-Atlantic Gateway almanac, F4W, Fightful, POST Wrestling, Wrestling Inc,
PWInsider and Ringside News.

He is a living legend, not an active wrestler. Status lines describe what was verified:
last match November 27, 2022; last TV appearance found November 12, 2025 (AEW Blood &
Guts); a February 2026 death scare that PWInsider and his wife both denied. No 2026
activity beyond that was found, and none is implied.

Deliberate omissions:
  * No walk-out theme band. Neither WWE.com nor Wikipedia names an entrance theme, and
    no other source checked did either.
  * No social links. No account could be verified as his.
  * No career win-loss total. Cagematch is JS-gated and no total is published elsewhere.
  * slot5 is "before" (the Mid-Atlantic years, 1976-1985). He was never in a faction, and
    his two great partners (Paul Jones, Jay Youngblood) have no tag-team page.
  * The 1977 and 1978 US title rows carry date conflicts (see the .md, flagged there).
    Only the 1978 Greensboro cage match is a record row, and its stip says so.
  * The old page's errors (Hall of Fame 2010, a Meltzer five-star WM III, a Backlash 2009
    win, a 1990 Clash win, a WrestleMania V match, an "Exotic Richard Blood" persona and
    invented finish percentages) are all removed; see the .md for the list.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="1977-06-15", promo="NWA", landmark=True,
         event="Mid-Atlantic Championship Wrestling, WRAL studio, Raleigh", opponent="Ric Flair",
         stip="TV studio match, aired June 18. A double thrust off the top rope for the pin. His first title",
         title="NWA Mid-Atlantic Television Championship"),
    dict(result="W", date="1978-04-23", promo="NWA", type="tag",
         event="Greensboro Coliseum", opponent="Masked Superstar & Ken Patera",
         stip="Tournament final, with Paul Jones", title="NWA World Tag Team Championship"),
    dict(result="W", date="1978-12-30", promo="NWA", landmark=True,
         event="Greensboro Coliseum", opponent="Ric Flair",
         stip="Steel cage, his hair vs. the title. Mid-Atlantic Gateway dates the change here; Wikipedia's title list says December 17 in Toronto",
         title="NWA United States Heavyweight Championship"),
    dict(result="W", date="1983-11-24", promo="NWA", type="tag", landmark=True,
         event="Starrcade, Greensboro", opponent="Jack & Jerry Brisco",
         stip="With Jay Youngblood. Angelo Mosca as guest referee", title="NWA World Tag Team Championship"),
    dict(result="W", date="1985-03-31", promo="WWE",
         event="WrestleMania, Madison Square Garden", opponent="Matt Borne",
         stip="Flying crossbody, 4:39", title=""),
    dict(result="W", date="1985-11-02", promo="WWE",
         event="Saturday Night's Main Event", opponent="Mr. Fuji",
         stip="Kung-fu challenge", title=""),
    dict(result="W", date="1986-04-07", promo="WWE",
         event="WrestleMania 2, Los Angeles", opponent="Hercules Hernandez",
         stip="Flying body press, 7:27", title=""),
    dict(result="W", date="1986-08-28", promo="WWE",
         event="The Big Event, Toronto", opponent="Jake Roberts",
         stip="Snake Pit match, no disqualification, 10:17", title=""),
    dict(result="W", date="1987-03-29", promo="WWE", landmark=True,
         event="WrestleMania III, Pontiac Silverdome", opponent="Randy Savage",
         stip="Small package reversing a slam at 14:35, George Steele in his corner. PWI and Observer Match of the Year",
         title="WWF Intercontinental Championship"),
    dict(result="L", date="1987-06-02", promo="WWE",
         event="Superstars taping", opponent="The Honky Tonk Man",
         stip="Title change taped June 2 and aired in mid-June. A 65-day reign ends",
         title="WWF Intercontinental Championship"),
    dict(result="L", date="1988-03-27", promo="WWE",
         event="WrestleMania IV, Atlantic City", opponent="Greg Valentine",
         stip="Tournament first round, 9:12. His last WWF pay-per-view of the decade",
         title="WWF Championship"),
    dict(result="W", date="1989-02-20", promo="NWA", landmark=True,
         event="Chi-Town Rumble, Chicago", opponent="Ric Flair",
         stip="Small package out of a figure-four attempt, 23:18. Meltzer: five stars",
         title="NWA World Heavyweight Championship"),
    dict(result="W", date="1989-03-18", promo="NWA",
         event="House show, Landover, Maryland", opponent="Ric Flair",
         stip="Untelevised. Small package. Meltzer: six stars, labeled unofficial",
         title="NWA World Heavyweight Championship"),
    dict(result="W", date="1989-04-02", promo="NWA", landmark=True,
         event="Clash of the Champions VI, New Orleans", opponent="Ric Flair",
         stip="Two out of three falls, 55:49. Flair's foot was under the rope on the deciding pin. Meltzer: five stars",
         title="NWA World Heavyweight Championship"),
    dict(result="L", date="1989-05-07", promo="NWA", landmark=True,
         event="WrestleWar, Nashville", opponent="Ric Flair",
         stip="Judges Terry Funk, Pat O'Connor and Lou Thesz. Inside cradle after his knee gave out. Meltzer: five stars",
         title="NWA World Heavyweight Championship"),
    dict(result="L", date="1989-07-23", promo="NWA",
         event="The Great American Bash, Baltimore", opponent="Lex Luger",
         stip="Disqualification. He hit Luger with a chair", title="NWA United States Heavyweight Championship"),
    dict(result="W", date="1991-11-19", promo="WCW", type="tag", landmark=True,
         event="Clash of the Champions XVII, Savannah", opponent="The Enforcers",
         stip="Surprise partner for Dustin Rhodes. His WCW return",
         title="WCW World Tag Team Championship"),
    dict(result="L", date="1992-02-29", promo="WCW",
         event="SuperBrawl II, Milwaukee", opponent="Rick Rude",
         stip="A masked Paul E. Dangerously hit him with a phone", title="WCW United States Heavyweight Championship"),
    dict(result="W", date="1992-05-17", promo="WCW", type="tag", landmark=True,
         event="WrestleWar, Jacksonville", opponent="The Dangerous Alliance",
         stip="WarGames, for Sting's Squadron with Sting, Barry Windham, Dustin Rhodes and Nikita Koloff. Meltzer: five stars",
         title=""),
    dict(result="W", date="1992-06-20", promo="WCW",
         event="Beach Blast, Mobile", opponent="Rick Rude",
         stip="30-minute Iron Man match, won 4-3. The last fall came at 29:30", title=""),
    dict(result="W", date="1992-09-02", promo="WCW",
         event="Clash of the Champions XX, Atlanta", opponent="Steve Austin",
         stip="Singles. His first WCW singles title", title="WCW World Television Championship"),
    dict(result="W", date="1992-11-18", promo="WCW", type="tag",
         event="Clash of the Champions XXI, Macon", opponent="Barry Windham & Dustin Rhodes",
         stip="With Shane Douglas", title="NWA and WCW World Tag Team Championships"),
    dict(result="L", date="1993-03-02", promo="WCW", type="tag",
         event="WCW Power Hour taping", opponent="The Hollywood Blonds (Steve Austin & Brian Pillman)",
         stip="With Shane Douglas. Taped March 2, aired March 27", title="NWA and WCW World Tag Team Championships"),
    dict(result="W", date="1993-08-18", promo="WCW",
         event="Clash of the Champions XXIV, Daytona Beach", opponent="Paul Orndorff",
         stip="Singles", title="WCW World Television Championship"),
    dict(result="L", date="1993-09-19", promo="WCW",
         event="Fall Brawl, Houston", opponent="Lord Steven Regal",
         stip="Singles", title="WCW World Television Championship"),
    dict(result="D", date="1993-12-27", promo="WCW",
         event="Starrcade, Charlotte", opponent="Lord Steven Regal",
         stip="Time-limit draw", title="WCW World Television Championship"),
    dict(result="D", date="1994-04-17", promo="WCW", landmark=True,
         event="Spring Stampede, Rosemont", opponent="Ric Flair",
         stip="Double pin out of a double chickenwing, 32:19. The title was vacated; Flair won the May 14 rematch",
         title="WCW World Heavyweight Championship"),
    dict(result="L", date="1994-07-17", promo="WCW",
         event="Bash at the Beach, Orlando", opponent="Steve Austin",
         stip="Austin rolled through a crossbody, 20:06", title="WCW United States Heavyweight Championship"),
    dict(result="W", date="1994-08-24", promo="WCW", landmark=True,
         event="Clash of the Champions XXVIII, Cedar Rapids", opponent="Steve Austin",
         stip="He hurt his back in this match and never wrestled for WCW again",
         title="WCW United States Heavyweight Championship"),
    dict(result="L", date="2009-04-05", promo="WWE", type="tag", landmark=True,
         event="WrestleMania 25, Houston", opponent="Chris Jericho",
         stip="3-on-1 handicap elimination with Jimmy Snuka and Roddy Piper, Ric Flair in their corner. Last man eliminated, by Codebreaker; 8:33",
         title=""),
    dict(result="L", date="2009-04-26", promo="WWE",
         event="Backlash, Providence", opponent="Chris Jericho",
         stip="Walls of Jericho after a Codebreaker countered his crossbody, 12:32", title=""),
    dict(result="W", date="2022-11-27", promo="IND", type="tag", landmark=True,
         event="Big Time Wrestling, Return of the Dragon, Raleigh", opponent="Nick Aldis, Jay Lethal & Brock Anderson",
         stip="With FTR. All three opponents tapped to figure-four leglocks. His first match in 12 years, at 69",
         title=""),
]

DATA = dict(
    slug="ricky-steamboat",
    name="Ricky Steamboat",
    realname="Richard Henry Blood",
    epithet="The Dragon",
    hook="Record & Titles",
    art="ricky-steamboat",

    meta_desc=("Ricky Steamboat beat Ric Flair for the NWA World title in 1989, beat Randy Savage at "
               "WrestleMania III, won eight World tag titles and entered the WWE Hall of Fame in "
               "2009. Full record, titles, rivalries and career."),
    og_desc=("The Dragon: the 1989 Flair series, the WrestleMania III classic, two Match of the Year "
             "awards with two different opponents, and a winning return at 69."),
    tw_desc="Ricky Steamboat: NWA World Champion, WrestleMania III, the Flair series, and a 2022 win at 69.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1976",
    height_imp="6&#8242;0&#8243;",
    weight_lb="235",
    world_titles="1",
    vitals_tagline="The Dragon",
    support_note="Watch &middot; Games &middot; Profile",
    sp_items=[
        dict(ic="RS", title="WWE Shop", sub="Legends merchandise · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable legend, most recently in WWE 2K25",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/rickysteamboat"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="NWA World Champion &middot; Hall of Fame 2009 &middot; the babyface every great heel wanted across the ring",
    hero_tag="Honolulu, Hawaii (billed) &middot; <em>Mid-Atlantic &middot; WWF &middot; NWA/WCW &middot; 1976&ndash;1994 &middot; and one more in 2022</em>",
    now_label="NOW",
    now_bold="Legend, last match November 27, 2022",
    now_tail=(" &middot; won a six-man tag with FTR in Raleigh at 69; most recent TV appearance found is "
              "AEW Blood &amp; Guts on November 12, 2025; reported well in February 2026 after a "
              "false death scare"),
    hstats=[
        dict(value="1989", x=False, label="NWA World Champion"),
        dict(value="8",    x=True,  label="World Tag Title Reigns"),
        dict(value="2009", x=False, label="Hall of Fame Class"),
        dict(value="69",   x=False, label="Age at 2022 Return Win"),
    ],
    ghost_link="From Rick Blood in the AWA to the Silverdome and the Superdome",
    vlabel="Est. 1976 &middot; Honolulu, Hawaii",
    mono="RS",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Ricky Steamboat</b> is the babyface that wrestling's best heels measured themselves "
        "against. He won the NWA World Heavyweight Championship from Ric Flair at Chi-Town Rumble "
        "on February 20, 1989, and his WrestleMania III win over Randy Savage on March 29, 1987 "
        "ranks among the most praised matches in WrestleMania history. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">2</span>'
        '<span class="pull-cap">Match of the Year awards from both PWI and the Observer, 1987 vs. Savage and 1989 vs. Flair</span></span>'
        "Both feuds won Match of the Year from Pro Wrestling Illustrated and the Wrestling Observer: "
        "1987 for Savage, 1989 for Flair. Around those peaks sit four United States title reigns, four "
        "Television title reigns, eight World tag title reigns, a WWF Intercontinental "
        "Championship and a 2009 WWE Hall of Fame induction, delivered by Flair.",

        "Three things repeated about him are wrong, and this page used to repeat them. He entered "
        "the WWE Hall of Fame in <b>2009</b>, not 2010; Flair inducted him the night before "
        "WrestleMania 25 in Houston. The WrestleMania III match was never a Dave Meltzer five-star "
        "match; it does not appear on Meltzer's list. The 1989 Flair matches do, all three "
        "televised ones at five stars, plus an untelevised Landover house show on March 18, 1989 "
        "that Meltzer rated six stars and called unofficial. And he did not win at Backlash 2009. "
        "Chris Jericho made him tap to the Walls of Jericho.",

        "He was born Richard Henry Blood on February 28, 1953, in West Point, New York, to a "
        "Japanese American mother and a white father. He was a Florida state amateur champion, "
        "trained under Verne Gagne and The Iron Sheik, and debuted in the AWA in 1976 as Rick "
        "Blood. Eddie Graham renamed him in Florida after Sammy Steamboat, whom he resembled. The "
        "two were not related. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig pull-fig--sm">1977</span>'
        '<span class="pull-cap">his first title: the Mid-Atlantic TV belt, from Ric Flair, in a Raleigh TV studio</span></span>'
        "Jim Crockett's Mid-Atlantic office hired him in 1977 on Wahoo McDaniel's word. On June 15, "
        "1977, in a TV studio in Raleigh, he pinned Ric Flair for the Mid-Atlantic Television "
        "title. That started the longest-running rivalry of both men's careers. Through 1983 he "
        "traded the United States title with Flair and won World tag titles with Paul Jones and "
        "Jay Youngblood, the last of them at the first Starrcade.",

        "The WWF signed him in 1985 and dressed him as The Dragon. Savage crushed his throat with "
        "the ring bell in late 1986, and the payoff at the Pontiac Silverdome went 14:35 and "
        "ended with a small package. He left the WWF after WrestleMania IV, came back to the NWA "
        "in January 1989, and beat Flair for the world title. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">55:49</span>'
        '<span class="pull-cap">the length of the two-out-of-three-falls Clash VI match in New Orleans, April 2, 1989</span></span>'
        "He kept it at Clash of the Champions VI on April 2 in a two-out-of-three-falls match that "
        "ran 55:49, then lost it at WrestleWar on May 7 when his knee gave out. His WCW run from "
        "1991 to 1994 added the WarGames match, an Iron Man win over Rick Rude, and a long series "
        "with \"Stunning\" Steve Austin. The last match of it, at Clash of the Champions XXVIII on "
        "August 24, 1994, won him the US title and hurt his back. Eric Bischoff fired him by FedEx "
        "that September.",

        "Since then he has refereed for TNA, worked a 2004 program opposite CM Punk in Ring of "
        "Honor, produced for WWE from 2005, and trained wrestlers in WWE developmental. He wrestled Jericho "
        "twice in 2009. On November 27, 2022, at 69, he teamed with FTR in Raleigh and won his "
        "first match in 12 years. His later work has been AEW cameos: guest enforcer for CM Punk "
        "vs. Ricky Starks in 2023, and a November 12, 2025 segment where FTR attacked him at his "
        "own request for \"firm\" offense. In February 2026 a Ric Flair post set off a false death "
        "scare. PWInsider reported him \"100% OK,\" and his wife said there had been no emergency. "
        "No match is booked.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Highlight set",
        promo_order=["NWA", "WWE", "WCW", "IND"],
        promo_labels={"NWA": "Mid-Atlantic/NWA", "WWE": "WWF/WWE", "WCW": "WCW", "IND": "Indies"},
        stats=[
            ("1",      "NWA World title"),
            ("4&times;", "US title reigns"),
            ("4&times;", "TV title reigns"),
            ("8&times;", "World tag reigns"),
            ("1",      "IC title"),
            ("2022",   "Last match"),
        ],
        lead=("Thirty-two documented bouts across 45 years. This is a highlight set, not a career "
              "count, and no win&ndash;loss total is published because none could be verified. "
              "The Flair matches run from a 1977 TV studio to a 1994 double pin. Every date comes "
              "from a title history or an event page. Where a taping date and an air date differ, "
              "the row says so. Filter by promotion or match type, sort any column, and turn "
              "spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the reputation rests on. Ratings are Dave Meltzer's, as listed in "
                    "Wikipedia's record of his five-star matches. WrestleMania III is not on that "
                    "list, so it shows a dash instead of an invented number."),
    signature=[
        dict(rating="5.0", event="Chi-Town Rumble 1989", opponent="Ric Flair",
             stip="NWA World Heavyweight Championship, the title win"),
        dict(rating="5.0", event="Clash of the Champions VI", opponent="Ric Flair",
             stip="NWA World title, two out of three falls, 55:49"),
        dict(rating="5.0", event="WrestleWar 1989", opponent="Ric Flair",
             stip="NWA World title, the loss, with three Hall of Fame judges at ringside"),
        dict(rating="5.0", event="WrestleWar 1992", opponent="The Dangerous Alliance",
             stip="WarGames, with Sting's Squadron"),
        dict(rating="&mdash;", event="WrestleMania III", opponent="Randy Savage",
             stip="Intercontinental Championship, 1987 Match of the Year"),
    ],
    signature_count_word="five",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("1",        "NWA World title"),
            ("76",       "Days as NWA World Champion"),
            ("8&times;", "World tag reigns"),
            ("2009",     "WWE Hall of Fame"),
        ],
        lead=("Gold in three promotions over 17 years. The counts below follow Wikipedia's "
              "championship lists. Two of them conflict with the same site's biography text, and "
              "the conflicts are noted rather than settled."),
        rows=[
            dict(ic="W", name="NWA World Heavyweight Championship", count="1",
                 sub="Won from Ric Flair at Chi-Town Rumble, Chicago, February 20, 1989 &middot; "
                     "retained at Clash of the Champions VI on April 2 &middot; lost to Flair at "
                     "WrestleWar, Nashville, May 7, 1989 &middot; <b>76 days</b>"),
            dict(ic="IC", name="WWF Intercontinental Championship", count="1",
                 sub="Won from Randy Savage at WrestleMania III, March 29, 1987 &middot; lost to The "
                     "Honky Tonk Man at a June 2, 1987 TV taping that aired in mid-June &middot; 65 "
                     "days (64 as WWE recognizes it)"),
            dict(ic="US", name="NWA / WCW United States Heavyweight Championship", count="4",
                 sub="1977 and 1978, both from Ric Flair; sources disagree on both dates and "
                     "places &middot; April 21, 1984 in Greensboro, lost to Wahoo McDaniel June 24 "
                     "&middot; August 24, 1994 from Steve Austin at Clash of the Champions XXVIII, "
                     "given up at Fall Brawl on September 18 because of a back injury. Wikipedia's "
                     "biography text says three reigns; its title list and infobox say four"),
            dict(ic="TV", name="Mid-Atlantic / NWA / WCW World Television Championship", count="4",
                 sub="June 15, 1977 from Ric Flair, his first title &middot; 1979 from Paul Jones, "
                     "vacated when he won the tag titles &middot; September 2, 1992 from Steve "
                     "Austin, lost to Scott Steiner September 29 &middot; August 18, 1993 from Paul "
                     "Orndorff, lost to Lord Steven Regal at Fall Brawl &middot; 314 days in all"),
            dict(ic="T", name="NWA / WCW World Tag Team Championship", count="8",
                 sub="Paul Jones (1978) &middot; Jay Youngblood, five times from 1979 to 1983, the "
                     "last at the first Starrcade &middot; Dustin Rhodes (November 1991) &middot; "
                     "Shane Douglas (November 1992 to March 1993, lost to the Hollywood Blonds) "
                     "&middot; 554 days in all"),
            dict(ic="MA", name="NWA Mid-Atlantic Heavyweight Championship", count="2",
                 sub="Two reigns in the Crockett years; the dates were not verified for this page"),
            dict(ic="MT", name="NWA Mid-Atlantic Tag Team Championship", count="4",
                 sub="With Paul Jones, Dino Bravo and Jay Youngblood. Wikipedia's text says four "
                     "reigns and its infobox says five"),
        ],
    ),

    # ---------------------------------------------------------------- 05 before
    slot5=dict(
        id="before",
        lead="Nine years in the territories before the WWF ever called.",
        cards=[
            dict(era="AWA &middot; 1976",
                 name="Rick Blood",
                 members="Trained by Verne Gagne and The Iron Sheik",
                 desc="Debuted in Minneapolis as a babyface under his own name. He left in May "
                      "1976, after a two-ring battle royal won by Mad Dog Vachon and Larry Hennig."),
            dict(era="Florida &middot; 1976",
                 name="Ricky Steamboat is born",
                 members="Championship Wrestling from Florida",
                 desc="Eddie Graham renamed him for his likeness to Sammy Steamboat and pitched him "
                      "as Sammy's nephew. The name stuck for 50 years. The family tie never existed."),
            dict(era="Mid-Atlantic &middot; 1977&ndash;79",
                 name="Steamboat vs. Flair, act one",
                 members="Ric Flair",
                 desc="A June 15, 1977 TV title win over Flair in a Raleigh studio made him a star "
                      "inside a year. They traded the US title into 1979, including a December 1978 "
                      "cage match in Greensboro where Steamboat's hair was on the line."),
            dict(era="Mid-Atlantic &middot; 1978&ndash;79",
                 name="Steamboat & Paul Jones",
                 members="Paul Jones",
                 desc="World tag champions in April 1978 and PWI's Tag Team of the Year. Jones "
                      "turned on him at a Charlotte battle royal on December 3, 1978, and the "
                      "partners became a feud."),
            dict(era="Mid-Atlantic &middot; 1979&ndash;83",
                 name="Steamboat & Jay Youngblood",
                 members="Jay Youngblood",
                 desc="Five World tag title reigns and the Observer's 1983 Tag Team of the Year. "
                      "The last reign began at the first Starrcade, over Jack and Jerry Brisco, "
                      "and ended on Christmas Day 1983 when Steamboat announced his retirement. "
                      "He was back by April 1984."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One babyface for 18 years, in four costumes.",
        cards=[
            dict(mono="RB", era="AWA &middot; 1976", name="Rick Blood",
                 desc="His real surname, a good amateur background, and no gimmick at all."),
            dict(mono="RS", era="Mid-Atlantic &middot; 1976&ndash;85", name="Ricky Steamboat",
                 desc="The territory star with the chops, the arm drags and the crossbody. Billed "
                      "from Honolulu and booked as the clean opposite of Flair."),
            dict(mono="DR", era="WWF &middot; 1985&ndash;88", name="The Dragon",
                 desc="Keikogi, long tights and a kung-fu frame, including a 1985 kung-fu challenge "
                      "win over Mr. Fuji. The look sold him to a national audience; the matches "
                      "with Jake Roberts and Randy Savage kept him there."),
            dict(mono="FB", era="WWF &middot; 1991", name="The Dragon, fire-breather",
                 desc="Billed with no surname, introduced in February 1991 vignettes breathing "
                      "fire. It lasted until late 1991, when he quit before Survivor Series and "
                      "went to WCW."),
            dict(mono="LG", era="2005&ndash;present", name="The legend",
                 desc="WWE producer, developmental trainer, 2009 Hall of Famer, and since 2022 a "
                      "guest who keeps getting jumped on AEW television, at his own suggestion."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="From the AWA in 1976 to an AEW segment in 2025, with the best work in the middle.",
        rows=[
            dict(year="1976", title="Debut as Rick Blood",
                 desc="Starts in the AWA, then moves to Florida in May, where Eddie Graham names him Ricky Steamboat."),
            dict(year="1977", title="First title, from Flair",
                 desc="Joins Jim Crockett Promotions and pins Ric Flair for the Mid-Atlantic TV title on June 15. PWI names him Rookie of the Year."),
            dict(year="1978", title="Tag gold and a hair match",
                 desc="Wins the World tag titles with Paul Jones in April, loses Jones to a heel turn in December, and regains the US title from Flair in a Greensboro cage with his hair at stake."),
            dict(year="1983", title="Starrcade and a short retirement",
                 desc="Wins the World tag titles with Jay Youngblood at the first Starrcade on November 24, then announces his retirement in December. He is back the next spring."),
            dict(year="1985", title="WWF and WrestleMania",
                 desc="Signs with the WWF as The Dragon and beats Matt Borne at the first WrestleMania on March 31."),
            dict(year="1986", title="Roberts and the bell",
                 desc="Jake Roberts DDTs him on the concrete; Steamboat wins their Snake Pit match in front of 61,470 paid in Toronto. Randy Savage then crushes his throat with the ring bell."),
            dict(year="1987", title="WrestleMania III",
                 desc="Beats Savage for the Intercontinental title on March 29, the first IC title change at a WrestleMania. Drops it to The Honky Tonk Man in June."),
            dict(year="1988", title="Leaves the WWF",
                 desc="Loses to Greg Valentine in the WrestleMania IV tournament on March 27 and departs."),
            dict(year="1989", title="World champion",
                 desc="Returns to the NWA in January, beats Flair at Chi-Town Rumble on February 20, keeps the belt at Clash VI on April 2, and loses it at WrestleWar on May 7. Lex Luger turns on him that summer. He leaves over his contract at year's end."),
            dict(year="1990", title="Japan and the independents",
                 desc="Foot surgery, then work for the NAWA/SAPW group in the Carolinas and a New Japan tour in September and October."),
            dict(year="1991", title="The Dragon, then WCW",
                 desc="Back in the WWF as a fire-breathing Dragon from March. He quits before Survivor Series and debuts in WCW on November 19 as Dustin Rhodes's surprise partner, winning the tag titles that night."),
            dict(year="1992", title="WarGames and the Iron Man",
                 desc="Fights the Dangerous Alliance all year: the five-star WarGames on May 17 and a 4-3 Iron Man win over Rick Rude on June 20. Takes the TV title from Steve Austin and the tag titles with Shane Douglas."),
            dict(year="1993", title="The Blonds and Regal",
                 desc="Loses the tag titles to Austin and Brian Pillman, wins the TV title from Paul Orndorff in August, and loses it to Lord Steven Regal in September."),
            dict(year="1994", title="Last WCW run",
                 desc="Double pin with Flair at Spring Stampede on April 17. Wins the US title from Austin on August 24 but hurts his back, gives up the belt in September, and is fired by Eric Bischoff by FedEx."),
            dict(year="2004", title="Ring of Honor",
                 desc="After refereeing for TNA, works a 2004 program in ROH against CM Punk, then Mick Foley."),
            dict(year="2005", title="WWE producer",
                 desc="Rejoins WWE as a producer and is reintroduced as a Legend on Raw in October."),
            dict(year="2009", title="Hall of Fame and two Jericho matches",
                 desc="Inducted by Ric Flair on April 4 in Houston. Wrestles Chris Jericho at WrestleMania 25 the next night and again at Backlash on April 26. PWI names him Most Inspirational."),
            dict(year="2010", title="The Nexus attack",
                 desc="Teams with his son Richie in FCW on June 18. Ten days later The Nexus attack him on Raw while he promotes his DVD; in 2024 he said the injury kept him in hospital three weeks."),
            dict(year="2014", title="Leaves WWE",
                 desc="Released on July 19 after years as a developmental trainer and ambassador."),
            dict(year="2022", title="Return of the Dragon",
                 desc="Teams with FTR on November 27 in Raleigh to beat Nick Aldis, Jay Lethal and Brock Anderson. All three tap to figure-fours. He is 69."),
            dict(year="2023", title="AEW cameos",
                 desc="Guest enforcer for CM Punk vs. Ricky Starks on August 5; Starks beats him with his own belt, a spot Steamboat says he pitched. Turns down a backstage producer job because of the travel."),
            dict(year="2025", title="FTR again",
                 desc="Appears at AEW Blood & Guts on November 12 to tell a Flair story and is attacked by FTR, his 2022 partners."),
            dict(year="2026", title="A false alarm",
                 desc="A February post by Ric Flair is read as a eulogy. PWInsider reports him fine and his wife confirms there was no emergency. No match is booked as of November 9."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with, in order of how much it mattered.",
        cards=[
            dict(name="Ric Flair", slug="ric-flair",
                 desc="Seventeen years of it. A 1977 TV title in a Raleigh studio, US title "
                      "trades through 1979, and the 1989 series: Chi-Town Rumble, the six-star "
                      "Landover house show, Clash VI and WrestleWar. Then a 1994 double pin at "
                      "Spring Stampede. Flair inducted him into the Hall of Fame in 2009 and "
                      "walked him to the ring at WrestleMania 25."),
            dict(name="Randy Savage", slug="randy-savage",
                 desc="Savage dropped the ring bell on his throat from the top rope in late 1986. "
                      "The six-month build ended at WrestleMania III on March 29, 1987, with "
                      "George Steele stopping Savage's bell and Steamboat winning the title with a "
                      "small package. It was 1987 Match of the Year for PWI and the Observer."),
            dict(name="Steve Austin",
                 desc="Steamboat's main WCW opponent, back when Austin was \"Stunning\" Steve "
                      "Austin. Steamboat took his TV title in 1992, lost the tag titles to "
                      "Austin's Hollywood Blonds in 1993, and swapped wins with him over the US "
                      "title in 1994. The last of those matches ended Steamboat's career in WCW."),
            dict(name="Jake Roberts",
                 desc="The 1986 program built on a DDT onto the concrete that knocked Steamboat "
                      "out for real. Steamboat won the Snake Pit match at The Big Event in "
                      "Toronto and the Saturday Night's Main Event rematch in October."),
            dict(name="Rick Rude",
                 desc="The face of the Dangerous Alliance in 1992. Rude kept the US title at "
                      "SuperBrawl II with a ninja-disguised Paul E. Dangerously's help; Steamboat "
                      "beat him 4-3 in a 30-minute Iron Man match at Beach Blast."),
            dict(name="Chris Jericho",
                 desc="The 2009 coda. At WrestleMania 25 Steamboat outlasted Jimmy Snuka and Roddy "
                      "Piper in a handicap match before Jericho's Codebreaker; at Backlash he "
                      "tapped to the Walls. PWI named him its Most Inspirational Wrestler that "
                      "year, at 56."),
            dict(name="Lex Luger",
                 desc="Luger turned on him at Clash of the Champions VII in June 1989. Their "
                      "Great American Bash match on July 23 ended with Steamboat disqualified for "
                      "using the chair Luger brought in."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="A short shelf. The matches did the selling.",
        rows=[
            dict(when="1989&ndash;2025", title="Video games", kind="Game",
                 desc="Fourteen wrestling games, from WCW: World Championship Wrestling in 1989 to WWE 2K25, per Wikipedia's count."),
            dict(when="2010", title="Ricky Steamboat: The Life Story of the Dragon", kind="DVD",
                 desc="WWE's career DVD set. He was promoting it on Raw on June 28, 2010 when The Nexus attacked him."),
            dict(when="2024", title="Biography: WWE Legends", kind="TV",
                 desc="His episode of the A&E documentary series aired June 2, 2024."),
            dict(when="2022&ndash;25", title="AEW television", kind="TV",
                 desc="Guest timekeeper on Dynamite in 2022, guest enforcer on Collision and the All Out commentary desk in 2023, the Revolution 2024 timekeeper for Sting's final match, a Dynamite guest in August 2024, and the FTR segment at Blood & Guts in 2025."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, with the counting rules that keep them true.",
        stats=[
            ("5",  "Meltzer 5+ star matches"),
            ("2",  "Match of the Year years"),
            ("12", "Years between matches, 2010-22"),
        ],
        rows=[
            dict(name="Match of the Year from PWI and the Observer in 1987 and again in 1989",
                 sub="1987 for WrestleMania III against Randy Savage; 1989 for the series with Ric Flair. Two different opponents, two different companies."),
            dict(name="Five matches rated five stars or more by Dave Meltzer",
                 sub="Chi-Town Rumble, Clash VI and WrestleWar in 1989 (five each), the Landover house show of March 18, 1989 (six, labeled unofficial), and WarGames at WrestleWar 1992 (five). WrestleMania III is not one of them."),
            dict(name="The first Intercontinental title change at a WrestleMania",
                 sub="March 29, 1987, at the Pontiac Silverdome. The WWF announced 93,173 fans; later analyses put the real figure near 78,000."),
            dict(name="Eight World tag title reigns with four partners",
                 sub="Paul Jones once, Jay Youngblood five times, Dustin Rhodes once, Shane Douglas once: 554 days in all, per Wikipedia's championship list."),
            dict(name="A 55:49 two-out-of-three-falls world title match on free TV",
                 sub="Clash of the Champions VI, April 2, 1989, at the Louisiana Superdome, aired on TBS."),
            dict(name="Three halls of fame",
                 sub="Wrestling Observer (1996), WWE (2009), NWA (2012), plus the Cauliflower Alley Club's Lou Thesz Award in 2012."),
            dict(name="A winning return at 69",
                 sub="November 27, 2022, in Raleigh, with FTR. His previous match had been in June 2010."),
        ],
        footnote=("No career win-loss total appears on this page; none could be verified. His height is "
                  "billed at 6'0\" by most sources and listed at 5'10\" by WWE.com. Both appear in the "
                  "tape and neither is adopted silently."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Ricky_Steamboat"),
        dict(k="WWE.com", v="Hall of Fame profile", href="https://www.wwe.com/superstars/rickysteamboat"),
        dict(k="Prowrestling.net", v="2009 Hall of Fame report",
             href="https://prowrestling.net/artman/publish/WWE/article1005268.shtml"),
        dict(k="Wikipedia", v="Meltzer's five-star match list",
             href="https://en.wikipedia.org/wiki/List_of_professional_wrestling_matches_rated_5_or_more_stars_by_Dave_Meltzer"),
        dict(k="Mid-Atlantic Gateway", v="December 1978 almanac",
             href="https://midatlanticwrestling.net/almanac/history/1978_12.htm"),
        dict(k="F4W", v="The 2022 return match",
             href="https://www.f4wonline.com/news/other-wrestling/ricky-the-dragon-steamboat-victorious-in-return-to-the-ring"),
        dict(k="PWInsider", v="February 2026 update",
             href="https://www.pwinsider.com/article/204844/ricky-steamboat-update.html?p=1"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/ricky-steamboat.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Ricky Steamboat still alive, and is he still wrestling?",
            a="He is alive, and he is not wrestling. A February 2026 Ric Flair post set off a false "
              "death scare; PWInsider reported him &ldquo;100% OK&rdquo; and his wife said there had "
              "been no emergency. His last match was <b>November 27, 2022</b>, a six-man tag win "
              "with FTR in Raleigh at 69. His most recent TV appearance found is AEW Blood &amp; "
              "Guts on November 12, 2025. As of November 9, 2026, nothing is booked.",
            q_ld="Is Ricky Steamboat still alive and wrestling in 2026?",
            a_ld="Ricky Steamboat is alive and is not actively wrestling as of November 9, 2026. A "
                 "February 2026 social media post by Ric Flair prompted false reports of his death, "
                 "which PWInsider and his wife both refuted. His last match was a six-man tag team "
                 "win with FTR at Big Time Wrestling in Raleigh, North Carolina on November 27, 2022, "
                 "at age 69, and his most recent television appearance was on AEW Dynamite: Blood "
                 "and Guts on November 12, 2025."),
        dict(
            q="Did Ricky Steamboat win the NWA World Heavyweight Championship?",
            a="Yes, once. He beat Ric Flair at Chi-Town Rumble in Chicago on <b>February 20, 1989</b> "
              "with a small package, kept the title against Flair at Clash of the Champions VI on "
              "April 2, and lost it back at WrestleWar on May 7. The reign lasted 76 days.",
            q_ld="Did Ricky Steamboat win the NWA World Heavyweight Championship?",
            a_ld="Yes. Ricky Steamboat won the NWA World Heavyweight Championship from Ric Flair at "
                 "Chi-Town Rumble in Chicago on February 20, 1989, retained it at Clash of the "
                 "Champions VI on April 2, 1989, and lost it to Flair at WrestleWar in Nashville on "
                 "May 7, 1989, a reign of 76 days."),
        dict(
            q="What is the Steamboat and Flair trilogy?",
            a="Three televised 1989 NWA World title matches: Chi-Town Rumble (February 20, Steamboat "
              "wins the belt), Clash of the Champions VI (April 2, Steamboat keeps it two falls to "
              "one in 55:49), and WrestleWar (May 7, Flair wins it back). Dave Meltzer rated all "
              "three five stars. An untelevised March 18 match in Landover, Maryland got six. The "
              "two had already been feuding since 1977.",
            q_ld="What were the Ricky Steamboat vs Ric Flair matches in 1989?",
            a_ld="Ricky Steamboat and Ric Flair wrestled three televised NWA World Heavyweight "
                 "Championship matches in 1989: Chi-Town Rumble on February 20, where Steamboat won "
                 "the title; Clash of the Champions VI on April 2, where Steamboat retained in a "
                 "two-out-of-three-falls match lasting 55 minutes 49 seconds; and WrestleWar on May "
                 "7, where Flair regained the title. Dave Meltzer rated all three five stars and "
                 "gave an untelevised March 18, 1989 match in Landover, Maryland six stars."),
        dict(
            q="Was Steamboat vs. Savage at WrestleMania III a five-star match?",
            a="Not by Dave Meltzer. The match is not on Meltzer's list of five-star matches, though "
              "it is often described that way. What it did win is <b>1987 Match of the Year</b> "
              "from both Pro Wrestling Illustrated and the Wrestling Observer. Steamboat won the "
              "Intercontinental title with a small package at 14:35, with George Steele in his corner.",
            q_ld="Did Dave Meltzer rate Steamboat vs Savage at WrestleMania III five stars?",
            a_ld="No. Ricky Steamboat vs Randy Savage at WrestleMania III on March 29, 1987 does not "
                 "appear on the list of matches Dave Meltzer rated five stars or more. It did win "
                 "1987 Match of the Year from both Pro Wrestling Illustrated and the Wrestling "
                 "Observer Newsletter. Steamboat won the WWF Intercontinental Championship in the "
                 "match with a small package after 14 minutes 35 seconds."),
        dict(
            q="When was Ricky Steamboat inducted into the WWE Hall of Fame?",
            a="In <b>2009</b>, not 2010. Ric Flair inducted him at the Toyota Center in Houston the "
              "night before WrestleMania 25. In his speech he pointed at Mickey Rourke and said, "
              "&ldquo;Tonight, this is my Oscar.&rdquo;",
            q_ld="When was Ricky Steamboat inducted into the WWE Hall of Fame?",
            a_ld="Ricky Steamboat was inducted into the WWE Hall of Fame in 2009 by Ric Flair, at the "
                 "ceremony held at the Toyota Center in Houston the night before WrestleMania 25."),
        dict(
            q="Why did Ricky Steamboat leave WCW in 1994?",
            a="He hurt his back beating Steve Austin for the US title at Clash of the Champions "
              "XXVIII on August 24, 1994. He could not defend it at Fall Brawl on September 18, so "
              "WCW gave the title to Austin. That September, while he was still injured, Eric "
              "Bischoff fired him by FedEx.",
            q_ld="Why did Ricky Steamboat leave WCW in 1994?",
            a_ld="Ricky Steamboat injured his back while winning the WCW United States Championship "
                 "from Steve Austin at Clash of the Champions XXVIII on August 24, 1994. He had to "
                 "give up the title at Fall Brawl on September 18, 1994, and WCW President Eric "
                 "Bischoff fired him by FedEx in September 1994 while he was injured."),
        dict(
            q="Did Ricky Steamboat wrestle after 1994?",
            a="Rarely. Four matches stand out. He wrestled Chris Jericho at WrestleMania 25 on April "
              "5, 2009 (a handicap match with Jimmy Snuka and Roddy Piper) and at Backlash on April "
              "26, 2009, losing both. He teamed with his son Richie in FCW on June 18, 2010. Then, "
              "after 12 years away, he won with FTR at Big Time Wrestling on November 27, 2022.",
            q_ld="Did Ricky Steamboat wrestle after he retired in 1994?",
            a_ld="Yes. Ricky Steamboat lost to Chris Jericho at WrestleMania 25 on April 5, 2009 and "
                 "at Backlash on April 26, 2009, wrestled with his son Richie in Florida Championship "
                 "Wrestling on June 18, 2010, and returned after 12 years to win a six-man tag team "
                 "match with FTR at Big Time Wrestling in Raleigh on November 27, 2022."),
        dict(
            q="Is Ricky Steamboat related to Sammy Steamboat?",
            a="No. His real name is Richard Henry Blood. Florida promoter Eddie Graham gave him the "
              "Steamboat name in 1976 because he looked like the Hawaiian wrestler Sammy Steamboat, "
              "and billed him as Sammy's nephew. His real family in wrestling is his younger brother "
              "Vic Steamboat and his son Richie.",
            q_ld="Is Ricky Steamboat related to Sammy Steamboat?",
            a_ld="No. Ricky Steamboat was born Richard Henry Blood. Promoter Eddie Graham gave him the "
                 "Steamboat name because of his resemblance to Sammy Steamboat and presented him as "
                 "Sammy's nephew, but they were not related. His brother Vic Steamboat and son Richie "
                 "Steamboat also wrestled."),
        dict(
            q="How is Ricky Steamboat connected to Steve Austin?",
            a="He was the veteran Austin learned against in WCW. Steamboat took Austin's TV title on "
              "September 2, 1992. Austin and Brian Pillman's Hollywood Blonds took the tag titles "
              "from Steamboat and Shane Douglas in March 1993. In 1994 Austin beat him at Bash at "
              "the Beach and Steamboat beat Austin for the US title at Clash XXVIII. Steamboat "
              "mentioned that last match in his 2009 Hall of Fame speech.",
            q_ld="What was the rivalry between Ricky Steamboat and Steve Austin?",
            a_ld="In WCW, Ricky Steamboat won the World Television Championship from Steve Austin on "
                 "September 2, 1992; Austin and Brian Pillman, the Hollywood Blonds, won the World "
                 "Tag Team Championship from Steamboat and Shane Douglas in March 1993; and in 1994 "
                 "Austin beat Steamboat at Bash at the Beach before Steamboat won the United States "
                 "Championship from Austin at Clash of the Champions XXVIII on August 24, 1994."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Richard Henry Blood"),
        dict(label="Born", value="February 28, 1953", sub="West Point, New York &middot; age 73"),
        dict(label="Billed from", value="Honolulu, Hawaii", sub="also billed from Charlotte, North Carolina"),
        dict(label="Height", value="6&#8242;0&#8243;",
             sub="183 cm as billed &middot; WWE.com lists 5&#8242;10&#8243;, a standing conflict"),
        dict(label="Weight", value="235 lb", sub="107 kg (billed)"),
        dict(label="Debut", value="1976",
             sub="AWA, as Rick Blood &middot; Wikipedia gives both February 15 and March"),
        dict(label="Trained by", value="Verne Gagne &middot; The Iron Sheik"),
        dict(label="Last match", value="November 27, 2022",
             sub="W with FTR, Big Time Wrestling, Raleigh"),
        dict(label="Signature", value="Flying crossbody",
             sub="plus the small package and the double chickenwing that beat Flair"),
        dict(label="Family", value="Brother of Vic Steamboat", sub="father of Richie Steamboat"),
        dict(label="Hall of Fame", value="WWE Class of 2009", sub="inducted by Ric Flair"),
        dict(label="Also known as", value="The Dragon &middot; Rick Blood"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1953-02-28",
    bornplace="West Point, New York",
    nationality="United States",
    height_cm=183,
    weight_kg=107,
    ld=dict(
        alternateName=["Richard Henry Blood", "The Dragon", "Rick Blood", "Ricky The Dragon Steamboat"],
        award=["NWA World Heavyweight Championship (1 reign, 1989)",
               "WWF Intercontinental Championship (1 reign, 1987)",
               "NWA/WCW United States Heavyweight Championship (4 reigns)",
               "NWA/WCW World Television Championship (4 reigns)",
               "NWA/WCW World Tag Team Championship (8 reigns)",
               "PWI and Wrestling Observer Match of the Year (1987, 1989)",
               "WWE Hall of Fame (Class of 2009)",
               "NWA Hall of Fame (2012)",
               "Wrestling Observer Newsletter Hall of Fame (1996)"],
        knowsAbout=["Professional wrestling", "NWA", "WWF", "WCW", "WrestleMania",
                    "Jim Crockett Promotions"],
        description="Ricky Steamboat, born Richard Henry Blood, is an American professional wrestler "
                    "known as The Dragon. He won the NWA World Heavyweight Championship from Ric "
                    "Flair at Chi-Town Rumble in 1989, beat Randy Savage for the WWF Intercontinental "
                    "Championship at WrestleMania III in 1987, and won Match of the Year from Pro "
                    "Wrestling Illustrated and the Wrestling Observer for both feuds. He was inducted "
                    "into the WWE Hall of Fame in 2009 and won his most recent match, alongside FTR, "
                    "in 2022 at age 69.",
        sameAs=["https://en.wikipedia.org/wiki/Ricky_Steamboat",
                "https://www.wwe.com/superstars/rickysteamboat"],
    ),
)
