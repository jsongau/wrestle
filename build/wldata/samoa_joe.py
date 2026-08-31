# -*- coding: utf-8 -*-
"""Samoa Joe - dossier data.

Sources: web research compiled August 31, 2026 - Wikipedia (Samoa Joe, The Opps, AEW
World Championship), Wrestling Inc. (planned-absence report), AllEliteWrestling.com /
411Mania (Full Gear 2025), PWMania (All In: London results, August 30, 2026), F4W
(All In tease). Day-precision dates come from those sources; classic ROH and TNA dates
are the standard published records.

Deliberate omissions and flags:
  * He did NOT appear at All In: London on August 30, 2026, despite teasing a return -
    the results are in and he is not in them. His hiatus is a planned filming absence
    (Twisted Metal, June 15 - August 26 in Toronto), not a departure; his AEW contract
    status is unaddressed by the coverage and is not guessed at here.
  * No career win-loss total: none verified across five promotions and 26 years.
  * No social links: no handle verified as official in this pass.
  * The Opps trios reign length is a printed conflict: Wikipedia says 273 days, but
    the April 16, 2025 - January 17, 2026 endpoints produce 276; the loss aired on
    tape delay, so the recognized change date is presumably the taping. Both numbers
    appear, neither is silently corrected.
  * US title and TNT/ROH TV reign dates were not re-verified in this pass and are
    hedged accordingly in the titles table.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2003-03-22", promo="ROH", landmark=True,
         event="Night of Champions — Philadelphia", opponent="Xavier",
         stip="Singles — the 645-day reign begins", title="ROH World Championship"),
    dict(result="D", date="2004-10-16", promo="ROH", landmark=True,
         event="Joe vs. Punk II — Chicago Ridge", opponent="CM Punk",
         stip="60-minute draw — five stars (Meltzer), the middle chapter of the trilogy",
         title="ROH World Championship"),
    dict(result="L", date="2004-12-26", promo="ROH", landmark=True,
         event="Final Battle", opponent="Austin Aries",
         stip="Singles — the 645-day reign ends", title="ROH World Championship"),
    dict(result="L", date="2005-10-01", promo="ROH", landmark=True,
         event="Joe vs. Kobashi — New York", opponent="Kenta Kobashi",
         stip="Dream match — five stars (Meltzer), 2005 Match of the Year", title=""),
    dict(result="L", date="2006-11-19", promo="TNA", landmark=True,
         event="Genesis", opponent="Kurt Angle",
         stip="Singles — the first loss of his TNA run ends the unbeaten streak", title=""),
    dict(result="W", date="2008-04-13", promo="TNA", landmark=True,
         event="Lockdown", opponent="Kurt Angle",
         stip="Six Sides of Steel — first TNA World Champion of the rivalry",
         title="TNA World Heavyweight Championship"),
    dict(result="L", date="2008-10-12", promo="TNA",
         event="Bound for Glory IV", opponent="Sting",
         stip="Singles — the 182-day reign ends", title="TNA World Heavyweight Championship"),
    dict(result="W", date="2016-04-21", promo="WWE", landmark=True,
         event="NXT — Lowell, Massachusetts", opponent="Finn Balor",
         stip="Singles — first NXT Championship, won at a live event", title="NXT Championship"),
    dict(result="W", date="2021-08-22", promo="WWE", landmark=True,
         event="NXT TakeOver 36", opponent="Karrion Kross",
         stip="Singles — a record third NXT Championship; vacated that September through injury",
         title="NXT Championship"),
    dict(result="W", date="2023-12-30", promo="AEW", landmark=True,
         event="Worlds End", opponent="MJF",
         stip="Singles — world champion in a third major promotion",
         title="AEW World Championship"),
    dict(result="L", date="2024-04-21", promo="AEW", landmark=True,
         event="Dynasty", opponent="Swerve Strickland",
         stip="Singles — the 113-day reign ends", title="AEW World Championship"),
    dict(result="W", date="2025-04-16", promo="AEW", type="tag",
         event="Dynamite: Spring BreakThru", opponent="The Death Riders",
         stip="Trios, with Katsuyori Shibata & Powerhouse Hobbs — Hook injured",
         title="AEW World Trios Championship"),
    dict(result="W", date="2025-07-12", promo="AEW", type="tag",
         event="All In: Texas", opponent="The Death Riders & Gabe Kidd",
         stip="Trios defense — retained, then beaten down after the bell",
         title="AEW World Trios Championship"),
    dict(result="W", date="2025-11-22", promo="AEW", landmark=True,
         event="Full Gear — Newark", opponent="Hangman Page",
         stip="Steel cage — Hook's belt shot decides it; second AEW World Championship",
         title="AEW World Championship"),
    dict(result="L", date="2025-12-27", promo="AEW", landmark=True,
         event="Worlds End", opponent="MJF",
         stip="Singles — the 35-day reign ends", title="AEW World Championship"),
    dict(result="L", date="2026-05-24", promo="AEW",
         event="Double or Nothing", opponent="Will Ospreay",
         stip="Owen Hart Cup first round — his last match before the filming hiatus", title=""),
]

DATA = dict(
    slug="samoa-joe",
    name="Samoa Joe",
    realname="Nuufolau Joel Seanoa",
    epithet="The Samoan Submission Machine",
    hook="Record & Titles",

    meta_desc=("Samoa Joe held the ROH World Championship a record 645 days and is the only "
               "man to win the ROH, TNA and AEW world titles. Currently on a Twisted Metal "
               "filming hiatus from AEW. Full record, titles, factions and career."),
    og_desc=("The Samoan Submission Machine: a record 645-day ROH reign, TNA and AEW world "
             "titles, three NXT Championships - and a 2026 hiatus spent playing Sweet Tooth, "
             "with the teased All In return still unpaid."),
    tw_desc="645 days in ROH, world titles in three promotions, three NXT titles - and a filming hiatus.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1999",
    height_imp="6&#8242;2&#8243;",
    weight_lb="282",
    world_titles="4",
    vitals_tagline="Sleep, fella",
    support_note="Merch &middot; Watch &middot; Play",
    sp_items=[
        dict(ic="SJ", title="AEW Shop", sub="Official merch · Shop AEW",
             tag="Shop", href="https://www.shopaew.com/"),
        dict(ic="TM", title="Twisted Metal", sub="As Sweet Tooth &middot; the 2026 hiatus",
             tag="Watch", href="https://en.wikipedia.org/wiki/Twisted_Metal_(TV_series)"),
        dict(ic="KS", title="Suicide Squad: Kill the Justice League", sub="Voice of King Shark",
             tag="Play", href="https://en.wikipedia.org/wiki/Suicide_Squad:_Kill_the_Justice_League"),
        dict(ic="AEW", title="All Elite Wrestling", sub="AEW.com", tag="Visit", charity=True,
             href="https://www.allelitewrestling.com/"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Samoan Submission Machine &middot; King of Television &middot; Sweet Tooth",
    hero_tag="Orange County, California &middot; <em>ROH &middot; TNA &middot; NJPW &middot; "
             "WWE &middot; AEW &middot; 1999&ndash;present</em>",
    now_label="NOW",
    now_bold="AEW, on a planned filming hiatus",
    now_tail=" &middot; shooting Twisted Metal in Toronto through late August; teased an All "
             "In: London return and did not appear there on August 30 &mdash; the return "
             "date is open",
    hstats=[
        dict(value="645", x=False, label="Day ROH Reign"),
        dict(value="4",   x=True,  label="World Titles"),
        dict(value="3",   x=True,  label="NXT Titles"),
        dict(value="3",   x=False, label="Promotions&rsquo; World Belts"),
    ],
    ghost_link="From a three-month training camp in 1999 to world titles in three promotions",
    vlabel="Est. 1999 &middot; Orange County, California",
    mono="SJ",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Samoa Joe</b> has been the most credible man in every room he has entered for "
        "twenty-six years, and in 2026 the room is a television set. He is the only "
        "wrestler to hold the ROH, TNA and AEW world championships &mdash; a fact Wikipedia "
        "states outright &mdash; plus a record three NXT Championships in WWE, and his "
        "645-day ROH reign from 2003 to 2004 remains the measuring stick for independent "
        "title runs. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">645</span>'
        '<span class="pull-cap">days as ROH World Champion, 2003&ndash;04 &mdash; still the record, with 29 defenses across two continents</span></span>'
        "He is a two-time AEW World Champion as recently as December 2025. He is also, "
        "right now, not wrestling at all: he announced a hiatus on the May 27, 2026 "
        "Dynamite to film the next season of Twisted Metal, in which he plays Sweet Tooth, "
        "and handed The Opps to Hook on his way out the door.",

        "The current-status record needs stating precisely, because the teases outran the "
        "facts. Joe&rsquo;s absence is a <b>planned filming break</b>, reported by "
        "Wrestling Inc. as running from a June 15 start to an August 26 wrap in Toronto "
        "&mdash; not a departure, not an injury, and not a retirement. Through August he "
        "publicly teased returning at All In: London (&ldquo;time will tell,&rdquo; he "
        "told interviewers); All In came and went at Wembley on <b>August 30, 2026</b>, "
        "and the full results carry no Samoa Joe appearance. His last match remains the "
        "<b>May 24, 2026</b> Owen Hart Cup loss to Will Ospreay at Double or Nothing "
        "&mdash; itself only a month after he returned from a roughly three-month injury "
        "layoff. His AEW contract status is unaddressed in any coverage found for this "
        "file, and this page does not guess at it. What is verifiable: filming has "
        "wrapped, the teased return has not happened, and the door is open.",

        "The legend was built fast and violently. Trained for roughly three months at the "
        "UIWA West Coast Dojo, he debuted in December 1999, and by March 22, 2003 he had "
        "beaten Xavier in Philadelphia for the ROH World Championship he would keep for "
        "645 days and 29 defenses. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">182</span>'
        '<span class="pull-cap">days as TNA World Heavyweight Champion in 2008, won from Kurt Angle inside the six-sided cage</span></span>'
        "The reign contained the CM Punk trilogy &mdash; the October 16, 2004 sixty-minute "
        "draw took five stars from Dave Meltzer &mdash; and ended against Austin Aries at "
        "Final Battle on December 26, 2004; the October 1, 2005 dream match with Kenta "
        "Kobashi, another five-star classic, won Match of the Year. TNA got the next "
        "decade: an unbeaten streak that Wikipedia logs at 19 months before Kurt Angle "
        "ended it at Genesis on November 19, 2006, the TNA World Heavyweight Championship "
        "won from Angle inside the cage at Lockdown on April 13, 2008, five X Division "
        "titles and the 18-month Angle rivalry that took PWI&rsquo;s Feud of the Year. "
        "WWE, from 2015, added three NXT Championships &mdash; the third won at TakeOver "
        "36 on August 22, 2021 and vacated through injury &mdash; two United States "
        "Championships, and two releases inside nine months, the second in January 2022 "
        "days after his induction in the ROH Hall of Fame&rsquo;s inaugural class.",

        "The AEW act has been the longest late peak in the business. He arrived in 2022, "
        "held the ROH Television and TNT titles simultaneously, and beat MJF at Worlds "
        "End on December 30, 2023 to complete the three-promotion world title set at "
        "age 44. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">35</span>'
        '<span class="pull-cap">days in the second AEW World Championship reign &mdash; Full Gear to Worlds End 2025, taken back by MJF</span></span>'
        "Swerve Strickland ended that first reign at Dynasty on April 21, 2024 after 113 "
        "days. The second act ran through The Opps &mdash; the stable he formed in "
        "February 2025 with Hook and Katsuyori Shibata &mdash; whose trios title win over "
        "the Death Riders on April 16, 2025 began a reign Wikipedia counts at 273 days. "
        "At Full Gear on November 22, 2025, Hook&rsquo;s belt shot inside a steel cage "
        "made Joe a two-time AEW World Champion over Hangman Page, and Swerve returned "
        "on the stage the same night; MJF took the title back at Worlds End on December "
        "27 after 35 days. A concussion-related layoff ate the early spring, Hook "
        "minded the store, Joe returned on April 22, lost to Ospreay in May, and left "
        "for Toronto. The mask he wears there belongs to Sweet Tooth; the one he "
        "wrestles in has never existed. Sleep, fella.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["ROH", "TNA", "WWE", "AEW"],
        promo_labels={"ROH": "ROH", "TNA": "TNA", "WWE": "WWE", "AEW": "AEW"},
        stats=[
            ("645",  "Day ROH reign"),
            ("4&times;", "World titles"),
            ("3&times;", "NXT Championship"),
            ("5&times;", "X Division"),
            ("2&times;", "AEW World"),
            ("29",   "ROH title defenses"),
        ],
        lead=("Sixteen documented bouts across four promotions and 23 years &mdash; the "
              "reign-defining matches in each company, both AEW World Championship "
              "changes in each direction, and the May 2026 Ospreay loss that stands as "
              "his last match before the filming hiatus. A curated ledger, not a career "
              "count: no verified win&ndash;loss total exists for a career this long and "
              "none is invented. The 2016 NXT title change happened at a non-televised "
              "live event in Lowell, Massachusetts, and is dated to the event itself. "
              "Filter by promotion or match type, tap any column header to sort, and "
              "turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("Three matches, two decades old, that still headline every "
                    "retrospective &mdash; the sixty-minute draw with CM Punk, the "
                    "Kobashi dream match, and the TNA three-way that put the promotion "
                    "on the map. The five-star ratings are Dave Meltzer&rsquo;s as "
                    "recorded by Wikipedia; the Punk and Kobashi matches are among the "
                    "most cited American matches of their decade."),
    signature=[
        dict(rating="5.0", event="Joe vs. Punk II — October 16, 2004", opponent="CM Punk",
             stip="ROH World Championship — 60-minute draw"),
        dict(rating="5.0", event="Joe vs. Kobashi — October 1, 2005", opponent="Kenta Kobashi",
             stip="Dream match — 2005 Match of the Year"),
        dict(rating="5.0", event="TNA Unbreakable — September 11, 2005",
             opponent="AJ Styles & Christopher Daniels",
             stip="Triple threat — TNA X Division Championship"),
    ],
    signature_count_word="three",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("4&times;", "World title reigns"),
            ("645",      "Day ROH reign"),
            ("3&times;", "NXT Championship"),
            ("3",        "Promotions&rsquo; world belts"),
        ],
        lead=("World championships in three promotions &mdash; a set nobody else has "
              "&mdash; plus a drawer of everything underneath. Reigns whose exact dates "
              "were not re-verified in this pass say so rather than guessing."),
        rows=[
            dict(ic="R", name="ROH World Championship", count="1",
                 sub="March 22, 2003 &ndash; December 26, 2004 &middot; def. Xavier at "
                     "Night of Champions, lost to Austin Aries at Final Battle &middot; "
                     "<b>645 days, the record</b>, with 29 defenses across the US and "
                     "Europe and the CM Punk trilogy inside it"),
            dict(ic="T", name="TNA World Heavyweight Championship", count="1",
                 sub="April 13 &ndash; October 12, 2008 &middot; def. Kurt Angle in the "
                     "Six Sides of Steel at Lockdown, lost to Sting at Bound for Glory "
                     "IV &middot; <b>182 days</b>"),
            dict(ic="A", name="AEW World Championship", count="2",
                 sub="2023&ndash;24 &middot; def. MJF at Worlds End on December 30, lost "
                     "to Swerve Strickland at Dynasty on April 21 &mdash; 113 days "
                     "&middot; 2025 &middot; def. Hangman Page in the Full Gear steel "
                     "cage on November 22, lost to MJF at Worlds End on December 27 "
                     "&mdash; 35 days &middot; the win made him the only man to hold "
                     "AEW, ROH and TNA world titles"),
            dict(ic="N", name="NXT Championship", count="3",
                 sub="2016 &middot; def. Finn Balor on April 21 in Lowell, lost to "
                     "Shinsuke Nakamura after 121 days &middot; 2016 &middot; a 14-day "
                     "second reign that November-December &middot; 2021 &middot; def. "
                     "Karrion Kross at TakeOver 36 on August 22, vacated that September "
                     "through injury &mdash; the record third reign"),
            dict(ic="O", name="AEW World Trios Championship", count="1",
                 sub="April 16, 2025 &ndash; January 2026, as The Opps &middot; won from "
                     "the Death Riders with Shibata and Hobbs, lost to Hangman Page and "
                     "JetSpeed &middot; <b>273 days per Wikipedia</b> &mdash; the loss "
                     "aired January 17 on tape delay, endpoints that produce 276, so the "
                     "recognized change is presumably the taping; both numbers printed"),
            dict(ic="X", name="TNA X Division Championship", count="5",
                 sub="Five reigns between 2005 and 2014, including the Unbreakable "
                     "triple threat era &middot; individual dates not re-verified in "
                     "this pass"),
            dict(ic="U", name="WWE United States Championship", count="2",
                 sub="Two reigns in 2019 &middot; exact dates not re-verified in this "
                     "pass and not guessed at"),
            dict(ic="V", name="AEW TNT Championship & ROH World Television Championship", count="3",
                 sub="Two TNT reigns and one record-setting ROH TV reign, 2022&ndash;23, "
                     "held overlapping &mdash; the &ldquo;King of Television&rdquo; era "
                     "&middot; reign dates not re-verified in this pass"),
            dict(ic="M", name="TNA World Tag Team & Television Championships", count="3",
                 sub="Two tag reigns and a 2012 Television title &middot; partners and "
                     "dates not re-verified in this pass"),
            dict(ic="P", name="ROH Pure Championship", count="1",
                 sub="2005 &middot; lost to Nigel McGuinness that August &middot; plus "
                     "the ROH Hall of Fame, inaugural class, January 2022"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Three stables across three eras &mdash; muscle for a prophet, a mafia "
             "seat, and finally his own crew.",
        cards=[
            dict(era="ROH &middot; 2002&ndash;03",
                 name="The Prophecy",
                 members="Christopher Daniels, Samoa Joe, and associates",
                 desc="His entry point to Ring of Honor: the heavy in Christopher "
                      "Daniels' anti-Code-of-Honor unit. He outgrew it almost "
                      "immediately — the ROH World Championship won in March 2003 "
                      "turned the enforcer into the franchise, and the reign outlived "
                      "the stable."),
            dict(era="TNA &middot; 2008&ndash;09",
                 name="The Main Event Mafia",
                 members="Kurt Angle, Sting, Kevin Nash, Booker T, Scott Steiner, Samoa Joe",
                 desc="The veteran supergroup he joined as its youngest made man, "
                      "during and after his world title year — an alliance of "
                      "champions that put him alongside the generation he had spent "
                      "2005-07 trying to knock over. His membership card read "
                      "differently than the others': he was the one who had come up "
                      "through the company."),
            dict(era="AEW &middot; 2025&ndash;present",
                 name="The Opps",
                 members="Samoa Joe, Hook, Katsuyori Shibata; Powerhouse Hobbs from April "
                         "2025 to January 2026; Anthony Bowens from April 2026",
                 desc="His own stable at last, debuted February 12, 2025. Won the AEW "
                      "World Trios Championship from the Death Riders on April 16, 2025 "
                      "— Hobbs subbing for an injured Hook — and held it into January "
                      "2026, with defenses at All In: Texas and Forbidden Door. Hook's "
                      "cage-side belt shot handed Joe the world title at Full Gear; "
                      "Hobbs left when his contract expired January 15, 2026; Hook has "
                      "led the group since February 7 and holds the reins through the "
                      "Twisted Metal hiatus. The name is the mission statement: "
                      "opposition, in bulk."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One name for twenty-six years &mdash; the reinventions have all been in "
             "role, not costume.",
        cards=[
            dict(mono="SSM", era="ROH, TNA &middot; 1999&ndash;2015", name="The Samoan Submission Machine",
                 desc="The nickname that defined the independent legend: a heavyweight "
                      "who moved like a junior, choked like a shooter and treated "
                      "selling as optional for the first thirty seconds. Rookie of the "
                      "Year in Southern California in 2000, unbeatable in TNA for "
                      "19 months by Wikipedia's count."),
            dict(mono="D", era="WWE &middot; 2015&ndash;22", name="The Destroyer",
                 desc="The NXT and main-roster heel: three NXT Championships, two US "
                      "titles, and a run as the promo of record — his 2017-18 Brock "
                      "Lesnar and AJ Styles programs were carried on the microphone as "
                      "much as the mat. Two releases inside nine months ended it; the "
                      "ROH Hall of Fame induction came the same January as the second."),
            dict(mono="KT", era="AEW &middot; 2022&ndash;24", name="The King of Television",
                 desc="The self-bestowed title of the TNT/ROH TV double-champion era, "
                      "and the best version of the late-career bully: squash matches, "
                      "short work, total contempt. It ran directly into the MJF program "
                      "that made him AEW World Champion at 44."),
            dict(mono="ST", era="AEW, television &middot; 2023&ndash;present", name="Sweet Tooth, and the boss of The Opps",
                 desc="The double life of the current era: leader of his own stable on "
                      "Wednesdays and the murderous clown of Twisted Metal on Peacock — "
                      "a role big enough that AEW writes his filming blocks into the "
                      "story. The 2026 hiatus is the third absence the show has papered "
                      "over with the character's own logic: the Opps hold his territory "
                      "until he gets back."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="A three-month training camp to world titles in three promotions, "
             "twenty-two years apart.",
        rows=[
            dict(year="1999", title="Debut after a three-month camp",
                 desc="Trains at the UIWA West Coast Dojo and debuts in December; named "
                      "Southern California Rookie of the Year for 2000."),
            dict(year="2003", title="The 645 days begin",
                 desc="Beats Xavier for the ROH World Championship on March 22 in "
                      "Philadelphia and holds it 645 days with 29 defenses — still the "
                      "record."),
            dict(year="2004", title="The Punk trilogy, and the end of the reign",
                 desc="Wrestles CM Punk to a five-star, sixty-minute draw on October 16; "
                      "Austin Aries ends the reign at Final Battle on December 26."),
            dict(year="2005", title="Kobashi, Unbreakable, and TNA",
                 desc="The Kobashi dream match on October 1 wins Match of the Year; the "
                      "Unbreakable triple threat with AJ Styles and Christopher Daniels "
                      "on September 11 becomes TNA's calling card; his TNA unbeaten run "
                      "is underway."),
            dict(year="2006", title="Angle ends the streak",
                 desc="Kurt Angle beats him at Genesis on November 19 — his first TNA "
                      "loss, ending a streak Wikipedia logs at 19 months — and ignites "
                      "the 18-month rivalry named PWI's 2007 Feud of the Year."),
            dict(year="2008", title="TNA World Heavyweight Champion",
                 desc="Beats Angle in the Six Sides of Steel at Lockdown on April 13 and "
                      "reigns 182 days, losing to Sting at Bound for Glory in October. "
                      "Joins the Main Event Mafia soon after."),
            dict(year="2016", title="NXT Champion, twice over",
                 desc="Beats Finn Balor at a Lowell live event on April 21 for his first "
                      "WWE title, loses it to Nakamura, regains it briefly in a 14-day "
                      "second reign."),
            dict(year="2021", title="The record third NXT title, then the cliff",
                 desc="Returns from release to beat Karrion Kross at TakeOver 36 on "
                      "August 22; injury forces him to vacate in September; WWE releases "
                      "him again in January 2022, days after his inaugural-class ROH "
                      "Hall of Fame induction."),
            dict(year="2023", title="The three-promotion set completes",
                 desc="After the King of Television run, beats MJF at Worlds End on "
                      "December 30 for the AEW World Championship — ROH, TNA and AEW "
                      "world titles, the only man with all three."),
            dict(year="2025", title="The Opps, and a second AEW World title",
                 desc="Forms The Opps in February; wins the trios titles April 16; beats "
                      "Hangman Page in the Full Gear cage on November 22 with Hook's "
                      "help; loses the title back to MJF at Worlds End on December 27, "
                      "after 35 days."),
            dict(year="2026", title="Injury, Ospreay, and Sweet Tooth",
                 desc="A roughly three-month injury layoff ends April 22; Will Ospreay "
                      "beats him in the Owen Hart Cup at Double or Nothing on May 24; he "
                      "announces the Twisted Metal filming hiatus on the May 27 Dynamite "
                      "and hands The Opps to Hook. Teases All In: London and does not "
                      "appear there on August 30. Return date open."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="CM Punk", slug="cm-punk",
                 desc="The trilogy that made two careers: three ROH World Championship "
                      "matches in 2004, the second a sixty-minute draw on October 16 "
                      "that took five stars from Dave Meltzer — by reputation the first "
                      "American match so rated in years — and made the case that the "
                      "independents were producing the best wrestling in the country. "
                      "Every subsequent Joe-Punk meeting, in any company, traded on it."),
            dict(name="Kurt Angle",
                 desc="The TNA rivalry of record: Angle ended the unbeaten streak at "
                      "Genesis in November 2006, Joe took the world title from him "
                      "inside the Lockdown cage in April 2008, and the 18-month arc "
                      "between was PWI's 2007 Feud of the Year. The rare feud where the "
                      "Olympian was the establishment and the submission machine was "
                      "the insurgency."),
            dict(name="AJ Styles & Christopher Daniels",
                 desc="The X Division triangle, peaking in the Unbreakable triple threat "
                      "of September 11, 2005 — five stars, TNA's first, and the match "
                      "the promotion used for years as proof of concept. Joe's five X "
                      "Division reigns are woven through it."),
            dict(name="Kenta Kobashi",
                 desc="One night only, October 1, 2005 in New York — the dream match "
                      "against the NOAH legend, a loss, five stars, and the 2005 Match "
                      "of the Year. Still the bout casual histories reach for first "
                      "when explaining what Joe was."),
            dict(name="MJF",
                 desc="The AEW book-ends: Joe beat MJF at Worlds End 2023 for his first "
                      "AEW World Championship — completing the three-promotion set — "
                      "and MJF took the second reign back at Worlds End 2025, 35 days "
                      "after Full Gear. Two Decembers, two title changes, one rivalry "
                      "conducted mostly in contempt."),
            dict(name="Hangman Page and Swerve Strickland",
                 desc="The 2024-25 world title triangle: Swerve ended Joe's first AEW "
                      "reign at Dynasty in April 2024; Joe ended Hangman's 133-day "
                      "reign in the Full Gear 2025 cage, with Hook's belt shot doing "
                      "the deciding; and Swerve returned on the stage that same night. "
                      "The thread AEW left hanging when the filming break began."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="The rare wrestler whose acting career is a booking consideration.",
        rows=[
            dict(when="2023&ndash;", title="Twisted Metal", kind="TV",
                 desc="Sweet Tooth — the body and menace of the killer clown — on the "
                      "Peacock series. The 2026 season's filming block, June 15 to "
                      "August 26 in Toronto per Wrestling Inc., is the reason for the "
                      "current AEW hiatus, and AEW has written all three of his "
                      "Twisted Metal absences into its television."),
            dict(when="2024", title="Suicide Squad: Kill the Justice League", kind="Game",
                 desc="The voice of King Shark in Rocksteady's DC game."),
            dict(when="2025", title="Like a Dragon: Pirate Yakuza in Hawaii", kind="Game",
                 desc="Plays antagonist Raymond Law — likeness and voice — in the Yakuza "
                      "spin-off, per Wikipedia."),
            dict(when="2022&ndash;", title="AEW commentary and video games", kind="Media",
                 desc="Fill-in commentary work during injury spells, and a playable "
                      "roster spot in AEW Fight Forever (2023)."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated with their sources &mdash; and one date-arithmetic "
             "conflict printed instead of resolved.",
        stats=[
            ("645", "Day ROH reign — the record"),
            ("3",   "Promotions' world titles"),
            ("3&times;", "NXT Championship — the record"),
        ],
        rows=[
            dict(name="The only man to hold ROH, TNA and AEW world championships",
                 sub="Wikipedia states it flatly. ROH in 2003, TNA in 2008, AEW in 2023 "
                     "and again in 2025 — a twenty-two-year spread between the first "
                     "and the last."),
            dict(name="645 days as ROH World Champion — still the record",
                 sub="March 22, 2003 to December 26, 2004, with 29 defenses across the "
                     "United States and Europe. The reign contains the Punk trilogy and "
                     "predates every other record-length modern reign it gets compared "
                     "to."),
            dict(name="A record three NXT Championships",
                 sub="2016, 2016 and 2021 — the third won at TakeOver 36 on August 22, "
                     "2021 and vacated through injury that September, on the same card "
                     "where Ilja Dragunov ended Gunther's 870-day NXT UK reign."),
            dict(name="Two AEW World Championship reigns after age 44",
                 sub="113 days from Worlds End 2023, ended by Swerve Strickland; 35 "
                     "days from Full Gear 2025 — won in a steel cage over Hangman Page "
                     "via Hook's belt shot — ended by MJF at Worlds End 2025."),
            dict(name="A 19-month unbeaten run in TNA",
                 sub="Wikipedia's figure, ended by Kurt Angle at Genesis on November "
                     "19, 2006. Coverage elsewhere often says 18 months; the June "
                     "2005 arrival and November 2006 first loss sit between the two "
                     "figures, so both circulate and both are flagged here."),
            dict(name="273 days as trios champion — or 276, depending how you count",
                 sub="The Opps' reign ran from April 16, 2025 to a loss that aired "
                     "January 17, 2026 on tape delay. Wikipedia says 273 days; the "
                     "aired endpoints produce 276; the recognized change date is "
                     "presumably the January 14 taping. Printed, not resolved."),
            dict(name="Three five-star matches across two promotions in 13 months",
                 sub="Joe vs. Punk II (October 2004), Unbreakable's triple threat "
                     "(September 2005) and Joe vs. Kobashi (October 2005) — the "
                     "stretch that made him the consensus best wrestler in North "
                     "America without a national television contract."),
            dict(name="King of Television",
                 sub="Held the AEW TNT Championship and ROH World Television "
                     "Championship simultaneously in 2022-23, the ROH reign a record "
                     "for that title per Wikipedia — exact dates not re-verified in "
                     "this pass."),
            dict(name="ROH Hall of Fame, inaugural class",
                 sub="January 2022 — announced days before WWE released him for the "
                     "second time, a sequence his biographies note without comment."),
        ],
        footnote=("Deliberately absent: a career win-loss total (none verified across "
                  "26 years and five promotions); social handles (unverified); his AEW "
                  "contract status (unaddressed by any coverage found — the hiatus is "
                  "reported as a planned filming break and nothing more is claimed); "
                  "and any assertion that he appeared at All In: London, because the "
                  "August 30, 2026 results show he did not, whatever the teases "
                  "suggested. US title and TNT/ROH TV reign dates are hedged in the "
                  "titles table rather than guessed."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Samoa_Joe"),
        dict(k="Wikipedia", v="The Opps — stable history", href="https://en.wikipedia.org/wiki/The_Opps"),
        dict(k="Wrestling Inc.", v="The planned Twisted Metal absence",
             href="https://www.wrestlinginc.com/2183646/aew-samoa-joe-twisted-metal-planned-absence-backstage-update/"),
        dict(k="411Mania", v="Full Gear 2025 — the second AEW World title",
             href="https://411mania.com/wrestling/samoa-joe-wins-aew-world-title-full-gear-2025/"),
        dict(k="PWMania", v="All In: London results, August 30, 2026 — no Joe",
             href="https://www.pwmania.com/aew-all-in-london-results-august-30-2026"),
        dict(k="Wikipedia", v="AEW World Championship — title history",
             href="https://en.wikipedia.org/wiki/AEW_World_Championship"),
        dict(k="F4W", v="The All In return tease",
             href="https://www.f4wonline.com/news/aew/samoa-joe-teases-return-at-aew-all-in/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Where is Samoa Joe? Is he still with AEW?",
            a="He is on a <b>planned filming hiatus</b>, announced on the May 27, 2026 "
              "Dynamite &mdash; shooting Twisted Metal, in which he plays Sweet Tooth, "
              "in Toronto from June 15 to an August 26 wrap, per Wrestling Inc. It is "
              "not a departure: the absence was written into AEW television, with Hook "
              "leading The Opps in his place. He teased returning at All In: London "
              "&mdash; &ldquo;time will tell&rdquo; &mdash; but the August 30, 2026 "
              "results contain no Samoa Joe appearance. His contract status is "
              "unaddressed in any coverage found for this page, and his last match "
              "remains the May 24 Owen Hart Cup loss to Will Ospreay at Double or "
              "Nothing.",
            q_ld="Where is Samoa Joe and is he still with AEW?",
            a_ld="Samoa Joe is on a planned hiatus from AEW, announced on the May 27, "
                 "2026 episode of Dynamite, to film the television series Twisted "
                 "Metal, in which he plays Sweet Tooth. Filming ran from June 15 to "
                 "August 26, 2026 in Toronto. He teased a return at All In: London on "
                 "August 30, 2026 but did not appear at the event. His last match was "
                 "a loss to Will Ospreay in the Owen Hart Cup at Double or Nothing on "
                 "May 24, 2026, and Hook is leading his stable The Opps in his "
                 "absence."),
        dict(
            q="Is Samoa Joe really the only man to win the ROH, TNA and AEW world titles?",
            a="Yes &mdash; Wikipedia states it outright. The set: the <b>ROH World "
              "Championship</b> won March 22, 2003 and held a record 645 days; the "
              "<b>TNA World Heavyweight Championship</b> won from Kurt Angle inside "
              "the Lockdown cage on April 13, 2008, held 182 days; and the <b>AEW "
              "World Championship</b> won from MJF at Worlds End on December 30, "
              "2023, then won a second time from Hangman Page at Full Gear on "
              "November 22, 2025. Add a record three NXT Championships in WWE and he "
              "has held the top title of four different companies.",
            q_ld="Is Samoa Joe the only wrestler to win the ROH, TNA and AEW world championships?",
            a_ld="Yes. Samoa Joe is the only wrestler to have held the ROH World "
                 "Championship, the TNA World Heavyweight Championship and the AEW "
                 "World Championship. He won the ROH title in March 2003 and held it "
                 "a record 645 days, won the TNA title from Kurt Angle at Lockdown in "
                 "April 2008, and won the AEW World Championship from MJF at Worlds "
                 "End on December 30, 2023 and again from Hangman Page at Full Gear "
                 "on November 22, 2025. He also holds a record three NXT "
                 "Championships in WWE."),
        dict(
            q="How did Samoa Joe win and lose the AEW World Championship in 2025?",
            a="Won in a steel cage at <b>Full Gear on November 22, 2025</b> in Newark: "
              "Hook &mdash; ostensibly estranged, actually loyal &mdash; blasted "
              "champion Hangman Page with the title belt, Joe finished the job, and "
              "commentary framed it as Hook having been with The Opps all along. "
              "Swerve Strickland returned on the stage minutes later. The reign "
              "lasted <b>35 days</b>: MJF beat him at Worlds End on December 27, "
              "taking back the title Joe had originally taken from him at Worlds End "
              "two years earlier.",
            q_ld="How did Samoa Joe win and lose the AEW World Championship in 2025?",
            a_ld="Samoa Joe won the AEW World Championship for a second time at Full "
                 "Gear on November 22, 2025 in Newark, defeating Hangman Page in a "
                 "steel cage match after Hook struck Page with the title belt. Swerve "
                 "Strickland returned the same night. Joe's reign lasted 35 days; MJF "
                 "defeated him for the title at Worlds End on December 27, 2025."),
        dict(
            q="What is Samoa Joe&rsquo;s most acclaimed match?",
            a="By the record, a three-way tie at five stars: the sixty-minute draw "
              "with <b>CM Punk</b> on October 16, 2004 &mdash; the second match of "
              "the ROH trilogy; the dream match with <b>Kenta Kobashi</b> on October "
              "1, 2005, which won Match of the Year; and TNA&rsquo;s <b>Unbreakable "
              "triple threat</b> with AJ Styles and Christopher Daniels on September "
              "11, 2005, the first five-star match in that promotion&rsquo;s "
              "history. Three matches inside thirteen months, in two promotions, "
              "none of them on national television when they happened.",
            q_ld="What is Samoa Joe's most acclaimed match?",
            a_ld="Samoa Joe has three matches rated five stars by Dave Meltzer: his "
                 "sixty-minute draw with CM Punk on October 16, 2004 in Ring of "
                 "Honor, his dream match with Kenta Kobashi on October 1, 2005, "
                 "which won Match of the Year, and the Unbreakable triple threat "
                 "with AJ Styles and Christopher Daniels on September 11, 2005, the "
                 "first five-star match in TNA's history."),
        dict(
            q="Who plays Sweet Tooth in Twisted Metal &mdash; and is that why he keeps "
              "disappearing from AEW?",
            a="Samoa Joe plays the body of Sweet Tooth, the series&rsquo; murderous "
              "clown, and yes &mdash; the absences are the show&rsquo;s. AEW has "
              "written his Twisted Metal filming blocks into its television "
              "repeatedly, with the 2026 block &mdash; June 15 to August 26 in "
              "Toronto &mdash; handled by putting Hook in charge of The Opps on "
              "screen. His screen work goes further: the voice of King Shark in "
              "Suicide Squad: Kill the Justice League and the antagonist Raymond Law "
              "in Like a Dragon: Pirate Yakuza in Hawaii.",
            q_ld="Does Samoa Joe play Sweet Tooth in Twisted Metal?",
            a_ld="Yes. Samoa Joe plays Sweet Tooth in the Twisted Metal television "
                 "series, and his AEW absences, including the June to August 2026 "
                 "hiatus, correspond to the show's filming blocks, which AEW writes "
                 "into its storylines. He also voiced King Shark in the game Suicide "
                 "Squad: Kill the Justice League and plays Raymond Law in Like a "
                 "Dragon: Pirate Yakuza in Hawaii."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Nuufolau Joel Seanoa"),
        dict(label="Born", value="March 17, 1979",
             sub="Orange County, California &middot; age 47"),
        dict(label="Billed from", value="Orange County, California"),
        dict(label="Height", value="6&#8242;2&#8243;", sub="188 cm &middot; billed"),
        dict(label="Weight", value="282 lb", sub="128 kg &middot; billed"),
        dict(label="Debut", value="December 1999",
             sub="after roughly three months&rsquo; training at the UIWA West Coast Dojo"),
        dict(label="Signature", value="Coquina Clutch &middot; Muscle Buster &middot; "
                                      "suicide elbow dive",
             sub="the Muscle Buster used sparingly in recent years"),
        dict(label="Last match", value="May 24, 2026",
             sub="Owen Hart Cup first round, Will Ospreay, Double or Nothing"),
        dict(label="Promotion", value="AEW", sub="on a planned filming hiatus since late May 2026"),
        dict(label="Faction", value="The Opps",
             sub="founder-leader &middot; Hook holding the reins since February 2026"),
        dict(label="Hall of Fame", value="ROH, inaugural class", sub="January 2022"),
        dict(label="Also known as",
             value="The Samoan Submission Machine &middot; King of Television &middot; "
                   "The Destroyer"),
        dict(label="Spouse", value="Jessica Seanoa", sub="married 2007"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1979-03-17",
    bornplace="Orange County, California",
    nationality="United States",
    height_cm=188,
    weight_kg=128,
    ld=dict(
        alternateName=["Nuufolau Joel Seanoa", "The Samoan Submission Machine",
                       "King of Television", "The Destroyer", "Sweet Tooth"],
        award=["ROH World Championship (1 reign, a record 645 days)",
               "TNA World Heavyweight Championship (1 reign, 182 days)",
               "AEW World Championship (2 reigns)",
               "NXT Championship (a record 3 reigns)",
               "AEW World Trios Championship (1 reign, with The Opps)",
               "AEW TNT Championship (2 reigns)",
               "ROH World Television Championship (1 reign, record length)",
               "TNA X Division Championship (5 reigns)",
               "TNA World Tag Team Championship (2 reigns)",
               "TNA Television Championship (1 reign)",
               "WWE United States Championship (2 reigns)",
               "ROH Pure Championship (1 reign)",
               "ROH Hall of Fame (inaugural class, 2022)",
               "PWI Feud of the Year (2007, vs. Kurt Angle)"],
        knowsAbout=["Professional wrestling", "Ring of Honor", "TNA Wrestling", "WWE", "AEW",
                    "Submission wrestling", "Championship wrestling", "Acting"],
        description="Samoa Joe, born Nuufolau Joel Seanoa, is an American professional "
                    "wrestler and actor signed to AEW, and the only wrestler to hold the "
                    "ROH, TNA and AEW world championships. His 645-day ROH World "
                    "Championship reign from 2003 to 2004 remains the record, he holds a "
                    "record three NXT Championships in WWE, and he is a two-time AEW World "
                    "Champion, most recently in late 2025. He leads The Opps stable and "
                    "plays Sweet Tooth in the Twisted Metal television series, the filming "
                    "of which accounts for his mid-2026 hiatus from AEW.",
        sameAs=["https://en.wikipedia.org/wiki/Samoa_Joe",
                "https://www.allelitewrestling.com/"],
    ),
)
