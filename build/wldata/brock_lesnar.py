# -*- coding: utf-8 -*-
"""Brock Lesnar - dossier data.

Sources: web-verified August 31, 2026 (Wikipedia, PWTorch, TMZ, Cultaholic, event pages).
Every match row carries a day-precision date confirmed in one of those sources.

Deliberate omissions:
  * No career win-loss total - no verified figure exists and none is invented.
  * No social links - Lesnar has no verified public social media accounts; he has
    famously avoided them, so nothing is linked.
  * No Meltzer star ratings in the signature block - not verified in this pass, so
    the column is published blank rather than guessed at.
  * The Janel Grant lawsuit is reported here exactly as reputable sources state it:
    Lesnar was named in the amended complaint but is not a defendant, and he has not
    publicly responded. Nothing beyond that is asserted.
"""

# ----------------------------------------------------------------- record rows
# 21 documented bouts - the world title changes, the streak, the UFC-era bookends in
# New Japan, and the 2025-26 farewell run against Oba Femi. Dates verified against
# Wikipedia's career history and 2026 event coverage.
ROWS = [
    dict(result="W", date="2002-04-21", promo="WWE", landmark=True,
         event="Backlash", opponent="Jeff Hardy",
         stip="First televised singles match — referee stoppage", title=""),
    dict(result="W", date="2002-08-25", promo="WWE", landmark=True,
         event="SummerSlam", opponent="The Rock",
         stip="Singles — youngest WWE Champion ever at 25", title="WWE Championship"),
    dict(result="W", date="2003-03-30", promo="WWE", landmark=True,
         event="WrestleMania XIX", opponent="Kurt Angle",
         stip="Singles — the botched shooting star press", title="WWE Championship"),
    dict(result="L", date="2004-02-15", promo="WWE", landmark=True,
         event="No Way Out — Daly City", opponent="Eddie Guerrero",
         stip="Singles — frog splash after a Goldberg spear", title="WWE Championship"),
    dict(result="L", date="2004-03-14", promo="WWE",
         event="WrestleMania XX", opponent="Goldberg",
         stip="Steve Austin as guest referee — both men leaving", title=""),
    dict(result="W", date="2005-10-08", promo="NJPW", landmark=True, type="tag",
         event="NJPW Toukon Souzou New Chapter — Tokyo Dome",
         opponent="Kazuyuki Fujita & Masahiro Chono",
         stip="Triple threat", title="IWGP Heavyweight Championship"),
    dict(result="L", date="2012-04-29", promo="WWE",
         event="Extreme Rules", opponent="John Cena",
         stip="Extreme rules — first WWE match in eight years", title=""),
    dict(result="W", date="2014-04-06", promo="WWE", landmark=True,
         event="WrestleMania XXX", opponent="The Undertaker",
         stip="Singles — ends the 21-0 streak", title=""),
    dict(result="W", date="2014-08-17", promo="WWE", landmark=True,
         event="SummerSlam", opponent="John Cena",
         stip="Singles — sixteen German suplexes", title="WWE World Heavyweight Championship"),
    dict(result="W", date="2017-04-02", promo="WWE",
         event="WrestleMania 33", opponent="Goldberg",
         stip="Singles — first Universal title", title="WWE Universal Championship"),
    dict(result="L", date="2018-08-19", promo="WWE",
         event="SummerSlam", opponent="Roman Reigns",
         stip="Singles — the 504-day reign ends", title="WWE Universal Championship"),
    dict(result="W", date="2019-07-14", promo="WWE",
         event="Extreme Rules", opponent="Seth Rollins",
         stip="Money in the Bank cash-in", title="WWE Universal Championship"),
    dict(result="L", date="2020-04-05", promo="WWE",
         event="WrestleMania 36 Night 2", opponent="Drew McIntyre",
         stip="Singles — the empty-arena WrestleMania", title="WWE Championship"),
    dict(result="W", date="2022-02-19", promo="WWE", type="tag",
         event="Elimination Chamber — Jeddah",
         opponent="Bobby Lashley, Seth Rollins, AJ Styles, Riddle & Austin Theory",
         stip="Elimination Chamber match", title="WWE Championship"),
    dict(result="L", date="2022-04-03", promo="WWE", landmark=True,
         event="WrestleMania 38 Night 2", opponent="Roman Reigns",
         stip="Winner take all — title unification", title="WWE Championship"),
    dict(result="L", date="2023-08-05", promo="WWE", landmark=True,
         event="SummerSlam", opponent="Cody Rhodes",
         stip="Singles — last match before the two-year absence", title=""),
    dict(result="W", date="2025-09-20", promo="WWE", landmark=True,
         event="Wrestlepalooza", opponent="John Cena",
         stip="Singles — first match back", title=""),
    dict(result="L", date="2026-01-31", promo="WWE", type="tag",
         event="Royal Rumble match — Riyadh", opponent="The 2026 Royal Rumble field",
         stip="Eliminated by Cody Rhodes and LA Knight", title=""),
    dict(result="L", date="2026-04-19", promo="WWE", landmark=True,
         event="WrestleMania 42 — Las Vegas", opponent="Oba Femi",
         stip="Singles — boots left in the ring, a retirement that was a ruse", title=""),
    dict(result="W", date="2026-05-31", promo="WWE",
         event="Clash in Italy", opponent="Oba Femi",
         stip="Singles — the rematch", title=""),
    dict(result="L", date="2026-08-01", promo="WWE", landmark=True,
         event="SummerSlam Night 1 — Minneapolis", opponent="Oba Femi",
         stip="Hell in a Cell — the final match", title=""),
]

DATA = dict(
    slug="brock-lesnar",
    name="Brock Lesnar",
    realname="Brock Edward Lesnar",
    epithet="The Beast Incarnate",
    hook="Record & Titles",

    meta_desc=("Brock Lesnar retired on August 4, 2026 after a Hell in a Cell loss to Oba Femi at "
               "SummerSlam. Ten WWE world championships, the UFC Heavyweight Championship, an NCAA "
               "title and the end of The Undertaker's streak. Full record, titles and career."),
    og_desc=("The Beast Incarnate: ten world championships in WWE, UFC Heavyweight Champion, 2000 NCAA "
             "champion, the man who ended the streak — and, since August 4, 2026, retired."),
    tw_desc="Brock Lesnar: ten WWE world titles, one UFC title, one streak ended. Retired August 2026.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2000",
    height_imp="6&#8242;3&#8243;",
    weight_lb="286",
    world_titles="10",
    vitals_tagline="Eat. Sleep. Suplex. Repeat.",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="BL", title="WWE Shop", sub="Legends tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Removed from 2K24 in 2024; back for 2K26",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="UFC", title="UFC.com", sub="Former UFC Heavyweight Champion",
             tag="Visit", href="https://www.ufc.com/"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com — moved to Alumni", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/brock-lesnar"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Beast Incarnate &middot; The Next Big Thing &middot; The Conqueror",
    hero_tag="Webster, South Dakota &middot; <em>WWE &middot; NJPW &middot; UFC &middot; 2000&ndash;2026</em>",
    now_label="NOW",
    now_bold="Retired",
    now_tail=(" &middot; announced August 4, 2026 on The Pat McAfee Show, three days after losing a "
              "Hell in a Cell match to Oba Femi at SummerSlam"),
    hstats=[
        dict(value="10", x=False, label="WWE World Titles"),
        dict(value="1",  x=True,  label="UFC Heavyweight Title"),
        dict(value="504", x=False, label="Day Universal Reign"),
        dict(value="21-1", x=False, label="He Is the 1"),
    ],
    ghost_link="From a Webster dairy farm to the only man to win the NCAA, WWE and UFC heavyweight crowns",
    vlabel="Est. 2000 &middot; Webster, South Dakota",
    mono="BL",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Brock Lesnar</b> is retired, and this time it is on the record: he said so himself on The "
        "Pat McAfee Show on August 4, 2026 &mdash; &ldquo;I am retired and I wanted to say a big thank "
        "you to everybody&rdquo; &mdash; three days after Oba Femi beat him inside Hell in a Cell at "
        "SummerSlam in Minneapolis on August 1. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">10</span>'
        '<span class="pull-cap">world championships in WWE &mdash; seven WWE Championships and a record three Universal Championships</span></span>'
        "He left his gloves and boots in the ring and raised Femi&rsquo;s hand, and WWE moved his "
        "profile to the alumni section. What he leaves is a resume nobody else in combat sports has: "
        "the 2000 NCAA Division I heavyweight wrestling championship, ten world championships in WWE, "
        "the IWGP Heavyweight Championship, and the UFC Heavyweight Championship, won inside his fourth "
        "professional MMA fight. He was the youngest WWE Champion ever at 25, and the man who ended "
        "The Undertaker&rsquo;s 21-0 WrestleMania streak.",

        "Two things about the record get told wrong. First, the title count: he is called a "
        "&ldquo;seven-time&rdquo; and a &ldquo;ten-time&rdquo; champion in different write-ups, and "
        "both are defensible &mdash; seven WWE Championship reigns plus three Universal Championship "
        "reigns makes ten world titles in WWE, and this page uses the ten. Second, the retirement: "
        "he had already faked one. After Oba Femi beat him at WrestleMania 42 on April 19, 2026 he "
        "left his gloves and boots in the ring, WWE moved him to the alumni page on May 7 and aired a "
        "tribute video &mdash; and on the May 18 Raw he returned, revealed the retirement as a ruse "
        "and attacked Femi, then beat him at Clash in Italy on May 31. The August retirement is the "
        "real one, sourced to his own words rather than a gesture, but the spring ruse is why this "
        "page dates his retirement to the McAfee announcement and not to the boots.",

        "The complicated part of the last act is not storyline. In January 2024, Janel Grant&rsquo;s "
        "lawsuit against Vince McMahon and WWE alleged, among other things, that McMahon used her as "
        "leverage in negotiations with an unnamed wrestler and former UFC fighter; the Wall Street "
        "Journal identified that wrestler as Lesnar, and Grant named him outright in an amended "
        "complaint in January 2025 &mdash; as a named figure in the allegations, not as a defendant. "
        "WWE scrapped his planned early-2024 return, and removed him from WWE 2K24 and SuperCard. "
        "He had not appeared since losing to Cody Rhodes at SummerSlam on August 5, 2023, and he "
        "stayed gone for two years, until WWE brought him back to close SummerSlam 2025 on August 3 "
        "with an F-5 on John Cena &mdash; a return Grant&rsquo;s representatives publicly criticised. "
        "Lesnar has not publicly commented on the allegations, and this page reports the situation "
        "as the sources do, no further.",

        "The career itself splits into four acts. 2002&ndash;2004: The Next Big Thing, from a "
        "Backlash debut against Jeff Hardy to WWE Champion at 25, out the door after WrestleMania XX. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">21-1</span>'
        '<span class="pull-cap">he is the 1 &mdash; The Undertaker&rsquo;s WrestleMania streak ended April 6, 2014</span></span>'
        "2004&ndash;2011: the outside years &mdash; a Minnesota Vikings training camp, the IWGP "
        "Heavyweight Championship in New Japan, and a real UFC Heavyweight Championship, taken from "
        "Randy Couture in 2008 and defended until diverticulitis and Cain Velasquez ended it. "
        "2012&ndash;2023: the part-time apex predator era under Paul Heyman &mdash; Suplex City, the "
        "streak, a 504-day Universal reign held mostly in absentia. 2025&ndash;2026: the farewell, "
        "ending on his back, 49 years old, putting over the 25-year-old Oba Femi in his final three "
        "matches&rsquo; defining feud &mdash; the same age he was when he took the title from The Rock.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE", "NJPW"],
        promo_labels={"WWE": "WWE", "NJPW": "NJPW"},
        stats=[
            ("10",   "WWE world titles"),
            ("1",    "UFC Heavyweight title"),
            ("504",  "Day Universal reign"),
            ("2000", "NCAA champion"),
            ("2",    "Royal Rumbles (2003, 2022)"),
            ("25",   "Youngest WWE Champion"),
        ],
        lead=("Twenty-one documented bouts &mdash; the title changes, the streak, the Tokyo Dome and "
              "the farewell series against Oba Femi. This is a curated ledger, not a career count; no "
              "career win&ndash;loss total is published because no verified one exists. His UFC fights "
              "are deliberately not listed here &mdash; a 5&ndash;3 (1 NC) MMA record belongs to a "
              "different sport and is covered under Feats. Filter by match type, tap any column header "
              "to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The bouts the reputation rests on. Star ratings are deliberately not published: "
                    "Observer figures for these matches were not verified in this pass, and this page "
                    "does not guess at numbers."),
    signature=[
        dict(rating="&mdash;", event="WrestleMania XIX", opponent="Kurt Angle",
             stip="WWE Championship — champion vs. champion, the shooting star press"),
        dict(rating="&mdash;", event="No Way Out 2004", opponent="Eddie Guerrero",
             stip="WWE Championship — the loss that made Guerrero"),
        dict(rating="&mdash;", event="WrestleMania XXX", opponent="The Undertaker",
             stip="The end of the 21-0 streak"),
        dict(rating="&mdash;", event="SummerSlam 2014", opponent="John Cena",
             stip="WWE World Heavyweight Championship — Suplex City is born"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("7&times;", "WWE Championship"),
            ("3&times;", "Universal Championship"),
            ("1",        "UFC Heavyweight title"),
            ("1",        "IWGP Heavyweight title"),
        ],
        lead=("Ten world championships in WWE, one in New Japan, one in the UFC and one NCAA "
              "heavyweight crown &mdash; the only man to hold all four kinds. Individual reign lengths "
              "beyond the 504-day Universal figure were not re-verified in this pass and are not "
              "invented here."),
        rows=[
            dict(ic="W", name="WWE Championship", count="7",
                 sub="2002 (SummerSlam, def. The Rock at 25 &mdash; youngest ever) &middot; 2003 "
                     "&times;2 (WrestleMania XIX; the SmackDown iron man vs. Kurt Angle) &middot; 2014 "
                     "(as WWE World Heavyweight, def. John Cena at SummerSlam) &middot; 2019 (def. "
                     "Kofi Kingston on SmackDown) &middot; 2022 &times;2 (Day 1; Elimination Chamber) "
                     "&middot; lost for the last time to Roman Reigns in the WrestleMania 38 "
                     "unification"),
            dict(ic="U", name="WWE Universal Championship", count="3",
                 sub="2017&ndash;18 (def. Goldberg at WrestleMania 33; the 504-day reign, lost to "
                     "Roman Reigns at SummerSlam 2018) &middot; 2018&ndash;19 (Crown Jewel) &middot; "
                     "2019 (Money in the Bank cash-in on Seth Rollins at Extreme Rules) &middot; "
                     "record three reigns"),
            dict(ic="I", name="IWGP Heavyweight Championship", count="1",
                 sub="October 8, 2005 at the Tokyo Dome, in a triple threat over Kazuyuki Fujita and "
                     "Masahiro Chono &middot; NJPW later stripped him over contract and visa disputes; "
                     "he kept the physical belt and lost the promotion&rsquo;s &ldquo;third belt&rdquo; "
                     "version to Kurt Angle in TNA-adjacent circumstances in 2007"),
            dict(ic="U", name="UFC Heavyweight Championship", count="1",
                 sub="Def. Randy Couture at UFC 91, November 15, 2008, in his fourth professional MMA "
                     "fight &middot; unified vs. Frank Mir at UFC 100 &middot; lost to Cain Velasquez "
                     "at UFC 121, October 23, 2010, after diverticulitis"),
            dict(ic="N", name="NCAA Division I Heavyweight Championship", count="1",
                 sub="2000, for the University of Minnesota &middot; runner-up in 1999"),
            dict(ic="K", name="King of the Ring", count="1",
                 sub="2002 &mdash; the win that set up the SummerSlam title shot at The Rock"),
            dict(ic="R", name="Royal Rumble", count="2",
                 sub="2003 and 2022 &mdash; one of a handful of multiple-time winners"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Alliances",
        lead="Lesnar never worked in stables. He worked with one advocate, twice, and briefly against "
             "him &mdash; the alliances are really one relationship.",
        cards=[
            dict(era="WWE &middot; 2002&ndash;2004, 2012&ndash;2023",
                 name="With Paul Heyman",
                 members="Brock Lesnar, Paul Heyman",
                 desc="The defining pairing. Heyman introduced him as The Next Big Thing in 2002, "
                      "carried the talking for the part-time years, and coined most of the language "
                      "the character is remembered in — the Beast Incarnate, the Conqueror, Suplex "
                      "City as a lifestyle. Heyman left the arrangement when he sided with Roman "
                      "Reigns in 2021, which fueled the last great Lesnar-Reigns program through "
                      "WrestleMania 38."),
            dict(era="WWE &middot; 2025",
                 name="Heyman again, one last time",
                 members="Brock Lesnar, Paul Heyman, The Vision (Seth Rollins, Bron Breakker, Bronson Reed)",
                 desc="At Survivor Series: WarGames on November 29, 2025 he allied with Heyman's "
                      "Vision, teaming with the faction plus Logan Paul and Drew McIntyre to beat "
                      "Roman Reigns' team. It was an association for one storyline rather than a "
                      "membership, and it did not carry into 2026, where he wrestled the Femi series "
                      "alone."),
            dict(era="OVW &middot; 2000&ndash;2002",
                 name="The Minnesota Stretching Crew",
                 members="Brock Lesnar, Shelton Benjamin",
                 desc="The developmental tag team with his University of Minnesota roommate — two "
                      "amateur credentials in one unit, multiple OVW Southern Tag Team Championship "
                      "reigns, and the only conventional tag team run of his career."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One name for twenty-six years &mdash; the packaging changed around it. Brock Lesnar has "
             "never wrestled under a gimmick name; the evolution is in the billing.",
        cards=[
            dict(mono="NBT", era="WWE &middot; 2002&ndash;2004", name="The Next Big Thing",
                 desc="The Heyman-introduced monster rookie: King of the Ring at his first attempt, "
                      "WWE Champion at 25, wrestling agile enough for a shooting star press he should "
                      "never have attempted at WrestleMania XIX."),
            dict(mono="MMA", era="NJPW &amp; UFC &middot; 2004&ndash;2011", name="The real athlete",
                 desc="An NFL training camp with the Vikings, the IWGP Heavyweight Championship, then "
                      "the UFC — where the wrestling persona became a genuine fighting resume, "
                      "UFC Heavyweight Champion within four professional fights."),
            dict(mono="BI", era="WWE &middot; 2012&ndash;2023", name="The Beast Incarnate",
                 desc="The part-timer as natural disaster: appears rarely, wins violently, holds "
                      "titles in absentia. Suplex City, the conquered streak, and a 504-day Universal "
                      "reign built the most protected aura in modern wrestling."),
            dict(mono="49", era="WWE &middot; 2025&ndash;2026", name="The farewell Beast",
                 desc="Grayer, cowboy-hatted, still F-5ing people through announce desks. The last "
                      "act was built almost entirely around Oba Femi — three matches, a faked "
                      "retirement and a real one, ending with Lesnar raising Femi's hand."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Webster, South Dakota to a Hell in a Cell farewell in Minneapolis.",
        rows=[
            dict(year="2000", title="NCAA champion; signs with WWE",
                 desc="Wins the NCAA Division I heavyweight championship for Minnesota, then signs "
                      "and reports to Ohio Valley Wrestling, trained on the pro side by Marty Morgan."),
            dict(year="2002", title="The fastest rise in company history",
                 desc="Debuts on television in March, wins King of the Ring in June, beats The Rock "
                      "at SummerSlam on August 25 to become the youngest WWE Champion ever at 25."),
            dict(year="2004", title="Walks away",
                 desc="Loses the title to Eddie Guerrero at No Way Out on February 15, loses to "
                      "Goldberg at WrestleMania XX, and leaves to try out for the Minnesota Vikings."),
            dict(year="2005", title="IWGP Heavyweight Champion",
                 desc="Beats Kazuyuki Fujita and Masahiro Chono in a Tokyo Dome triple threat on "
                      "October 8 to win New Japan's top title in his first match there."),
            dict(year="2008", title="UFC Heavyweight Champion",
                 desc="Beats Randy Couture at UFC 91 on November 15, in his fourth professional MMA "
                      "fight, then unifies the title against Frank Mir at UFC 100."),
            dict(year="2012", title="Back to WWE",
                 desc="Returns the night after WrestleMania XXVIII; loses the return match to John "
                      "Cena at Extreme Rules on April 29, then settles into the part-time monster role."),
            dict(year="2014", title="The 1 in 21-1",
                 desc="Ends The Undertaker's WrestleMania streak on April 6, then destroys John Cena "
                      "at SummerSlam on August 17 for the WWE World Heavyweight Championship."),
            dict(year="2017", title="The 504 days",
                 desc="Beats Goldberg at WrestleMania 33 for the Universal Championship and holds it "
                      "until SummerSlam 2018 — 504 days, mostly defended in absentia."),
            dict(year="2022", title="Unification loser, last full year",
                 desc="Wins the WWE Championship twice more (Day 1 and Elimination Chamber), loses "
                      "the winner-take-all unification to Roman Reigns at WrestleMania 38 on April 3."),
            dict(year="2023", title="The Cody trilogy, then silence",
                 desc="Loses the rubber match to Cody Rhodes at SummerSlam on August 5 and disappears "
                      "from WWE programming for two years."),
            dict(year="2024", title="Named, and shelved",
                 desc="After the Janel Grant lawsuit is filed in January 2024, WWE scraps his planned "
                      "return and removes him from its video games. Grant names him in an amended "
                      "complaint in January 2025; he is not a defendant and has not commented."),
            dict(year="2025", title="The return",
                 desc="Closes SummerSlam on August 3 with an F-5 on John Cena, beats Cena at "
                      "Wrestlepalooza on September 20, and works Survivor Series: WarGames with "
                      "Heyman's Vision on November 29."),
            dict(year="2026", title="The Femi series and retirement",
                 desc="Loses to Oba Femi at WrestleMania 42 on April 19 and fakes a retirement; wins "
                      "the rematch at Clash in Italy on May 31; loses Hell in a Cell at SummerSlam on "
                      "August 1 and retires for real on The Pat McAfee Show on August 4, at 49."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Kurt Angle",
                 desc="The amateur-credentials rivalry — Olympic gold against NCAA gold. The "
                      "WrestleMania XIX main event on March 30, 2003 ended with the botched shooting "
                      "star press that nearly broke Lesnar's neck, and the 60-minute iron man match "
                      "that September was the best long-form wrestling of his career."),
            dict(name="Eddie Guerrero",
                 desc="One match, and one of the most important losses in WWE history: No Way Out, "
                      "February 15, 2004, where a Goldberg spear and a frog splash ended Lesnar's "
                      "reign and made Guerrero WWE Champion. Lesnar has spent twenty years being "
                      "gracious about it, and the match reads now as the great passing-of-belief "
                      "moment of the era."),
            dict(name="John Cena",
                 desc="Bookends. Cena beat him at Backlash 2003 and in the bloody 2012 return match; "
                      "Lesnar answered with the sixteen-suplex SummerSlam 2014 demolition that "
                      "invented Suplex City, and the last chapter was Wrestlepalooza on September 20, "
                      "2025 — Lesnar's return win in Cena's farewell year."),
            dict(name="The Undertaker",
                 desc="The streak. April 6, 2014, WrestleMania XXX, the quietest crowd in the show's "
                      "history staring at the 21-1 graphic. They ran it back at SummerSlam 2015 and "
                      "in Hell in a Cell, but nothing touches the first result."),
            dict(name="Roman Reigns",
                 desc="The defining opponent of the part-time era — WrestleMania 31, the Greatest "
                      "Royal Rumble, SummerSlam 2018, and finally the winner-take-all WrestleMania 38 "
                      "unification on April 3, 2022, which Reigns won. Paul Heyman changing sides is "
                      "what made the last act personal."),
            dict(name="Oba Femi",
                 desc="The farewell feud, and a deliberate torch-passing: Femi beat him at "
                      "WrestleMania 42 on April 19, 2026, lost the Clash in Italy rematch on May 31, "
                      "then beat him inside Hell in a Cell at SummerSlam on August 1. Lesnar left his "
                      "gloves and boots in the ring and raised Femi's hand, and retired three days "
                      "later at 49 — Femi is 25, roughly the age Lesnar was when he beat The Rock."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Thin for a star this size, by his own choice &mdash; no social media, few interviews, "
             "one book.",
        rows=[
            dict(when="2003&ndash;", title="WWE video games", kind="Game",
                 desc="A cover star of WWE 2K17. Removed from WWE 2K24 and WWE SuperCard in 2024 "
                      "after the Grant lawsuit was filed; returned to the series after his 2025 "
                      "comeback."),
            dict(when="2011", title="Death Clutch: My Story of Determination, Domination, and Survival",
                 kind="Book",
                 desc="His autobiography, covering the farm, the NCAA title, the diverticulitis that "
                      "nearly killed him, and the UFC run."),
            dict(when="2008&ndash;2011", title="UFC pay-per-views", kind="MMA",
                 desc="Headlined some of the highest-selling UFC events ever, including UFC 100. "
                      "Final MMA record 5-3 with one no contest, the 2016 UFC 200 win over Mark Hunt "
                      "overturned after a failed drug test."),
            dict(when="2026", title="The Pat McAfee Show", kind="Interview",
                 desc="The August 4, 2026 appearance where he announced his retirement — 'I am "
                      "retired and I wanted to say a big thank you to everybody.'"),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated the way the sources state them.",
        stats=[
            ("10",   "WWE world titles"),
            ("504",  "Day Universal reign"),
            ("4",    "Fights to a UFC title"),
        ],
        rows=[
            dict(name="Youngest WWE Champion in history, at 25",
                 sub="SummerSlam, August 25, 2002, over The Rock — a record that still stands as of "
                     "August 2026."),
            dict(name="Ended The Undertaker's WrestleMania streak at 21-0",
                 sub="April 6, 2014, WrestleMania XXX in New Orleans. The most protected unbeaten "
                     "run in wrestling ended on a third F-5."),
            dict(name="The only man to win NCAA, WWE and UFC heavyweight titles",
                 sub="NCAA Division I heavyweight champion 2000; WWE Champion 2002; UFC Heavyweight "
                     "Champion 2008. No one else has all three."),
            dict(name="Record three Universal Championship reigns, including 504 days",
                 sub="The first reign, April 2, 2017 to August 19, 2018, is the longest in the "
                     "title's history."),
            dict(name="Two Royal Rumble wins, nineteen years apart",
                 sub="2003 and 2022 — the longest gap between wins for any multiple-time winner."),
            dict(name="UFC Heavyweight Champion in his fourth professional fight",
                 sub="UFC 91, November 15, 2008, over Randy Couture; unified against Frank Mir in "
                     "the UFC 100 headliner, one of the biggest-selling UFC events ever."),
            dict(name="A retirement, a ruse, then a retirement",
                 sub="Boots left in the ring at WrestleMania 42 on April 19, 2026; alumni page May "
                     "7; ruse revealed on the May 18 Raw; the real announcement came August 4, 2026 "
                     "on The Pat McAfee Show, after the SummerSlam Hell in a Cell loss to Oba Femi."),
        ],
        footnote=("Deliberately absent: a career win-loss total (no verified figure exists), social "
                  "media handles (he has none that are verified), and any characterisation of the "
                  "Janel Grant lawsuit beyond what reputable outlets report — he was named in the "
                  "January 2025 amended complaint, he is not a defendant, and he has not publicly "
                  "responded."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Brock_Lesnar"),
        dict(k="PWTorch", v="Retirement announcement, August 4, 2026",
             href="https://www.pwtorch.com/site/2026/08/04/brock-lesnar-announces-retirement-from-wrestling/"),
        dict(k="TMZ", v="Retirement announcement details and quotes",
             href="https://www.tmz.com/2026/08/04/brock-lesnar-officially-announces-retirement/"),
        dict(k="Cultaholic", v="The 2025 return and the Janel Grant lawsuit context",
             href="https://cultaholic.com/posts/wwe-brings-back-brock-lesnar-at-summerslam-2025-despite-him-being-named-in-janel-grants-lawsuit"),
        dict(k="Wikipedia", v="SummerSlam 2026 — the Hell in a Cell final match",
             href="https://en.wikipedia.org/wiki/SummerSlam_(2026)"),
        dict(k="Wikipedia", v="No Way Out 2004 — the Guerrero title change",
             href="https://en.wikipedia.org/wiki/No_Way_Out_(2004)"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Brock Lesnar retired?",
            a="Yes. He announced it himself on The Pat McAfee Show on August 4, 2026: &ldquo;I am "
              "retired and I wanted to say a big thank you to everybody.&rdquo; His final match was a "
              "Hell in a Cell loss to Oba Femi at SummerSlam Night 1 in Minneapolis on August 1, "
              "2026, after which he left his gloves and boots in the ring and raised Femi&rsquo;s "
              "hand. One caution: he had faked exactly this once already &mdash; boots left in the "
              "ring at WrestleMania 42 in April 2026, alumni page and tribute video, then a return "
              "three weeks later. The difference this time is his own on-record statement.",
            q_ld="Is Brock Lesnar retired from WWE?",
            a_ld="Yes. Brock Lesnar announced his retirement from professional wrestling on The Pat "
                 "McAfee Show on August 4, 2026, saying he was retired and thanking fans. His final "
                 "match was a Hell in a Cell loss to Oba Femi at SummerSlam Night 1 in Minneapolis on "
                 "August 1, 2026, after which he left his gloves and boots in the ring. He had "
                 "previously staged a false retirement after losing to Femi at WrestleMania 42 in "
                 "April 2026, but the August announcement was made in his own words and WWE lists him "
                 "as an alumnus."),
        dict(
            q="What is Brock Lesnar&rsquo;s connection to the Janel Grant lawsuit?",
            a="Grant&rsquo;s January 2024 lawsuit against Vince McMahon and WWE alleged McMahon used "
              "her as leverage in negotiations with an unnamed WWE wrestler and former UFC fighter; "
              "the Wall Street Journal identified that wrestler as Lesnar, and Grant named him "
              "explicitly in an amended complaint in January 2025. He is named in the allegations "
              "but is <b>not a defendant</b>. WWE shelved his planned 2024 return and removed him "
              "from its video games; he returned at SummerSlam on August 3, 2025, a decision "
              "Grant&rsquo;s representatives publicly criticised. Lesnar has not publicly commented. "
              "This page reports what reputable outlets have published and asserts nothing beyond it.",
            q_ld="What is Brock Lesnar's connection to the Janel Grant lawsuit?",
            a_ld="Janel Grant's January 2024 lawsuit against Vince McMahon and WWE alleged that "
                 "McMahon used her as leverage in contract negotiations with an unnamed WWE wrestler "
                 "and former UFC fighter, whom the Wall Street Journal identified as Brock Lesnar. "
                 "Grant named Lesnar explicitly in an amended complaint in January 2025. Lesnar is "
                 "named in the allegations but is not a defendant in the lawsuit. WWE cancelled his "
                 "planned 2024 return and removed him from its video games before bringing him back "
                 "at SummerSlam on August 3, 2025. Lesnar has not publicly commented on the "
                 "allegations."),
        dict(
            q="How many world titles did Brock Lesnar win?",
            a="Ten in WWE &mdash; seven WWE Championship reigns (2002, two in 2003, 2014, 2019, and "
              "two in 2022) and a record three Universal Championship reigns (2017, 2018, 2019), the "
              "first of which ran 504 days. Add the IWGP Heavyweight Championship won at the Tokyo "
              "Dome in 2005 and the UFC Heavyweight Championship won at UFC 91 in 2008 and the "
              "cross-sport total is twelve major heavyweight titles, plus the 2000 NCAA Division I "
              "heavyweight championship. Different write-ups quote seven or ten; both are countings "
              "of the same WWE facts.",
            q_ld="How many world championships did Brock Lesnar win?",
            a_ld="Brock Lesnar won ten world championships in WWE: seven WWE Championship reigns and "
                 "a record three Universal Championship reigns, the first of which lasted 504 days. "
                 "He also won the IWGP Heavyweight Championship in New Japan Pro-Wrestling in 2005, "
                 "the UFC Heavyweight Championship in 2008, and the NCAA Division I heavyweight "
                 "wrestling championship in 2000, making him the only person to win NCAA, WWE and "
                 "UFC heavyweight titles."),
        dict(
            q="Who was Brock Lesnar&rsquo;s last opponent?",
            a="Oba Femi, three times in 2026 &mdash; and Femi won the series. Femi beat him at "
              "WrestleMania 42 on April 19, lost the rematch at Clash in Italy on May 31, and won "
              "the decider inside Hell in a Cell at SummerSlam on August 1. Lesnar, 49, called "
              "himself &ldquo;the past&rdquo; and Femi &ldquo;the future,&rdquo; and raised the "
              "25-year-old&rsquo;s hand before leaving his gloves and boots in the ring.",
            q_ld="Who was Brock Lesnar's last opponent before retiring?",
            a_ld="Brock Lesnar's final opponent was Oba Femi. They wrestled three times in 2026: Femi "
                 "won at WrestleMania 42 on April 19, Lesnar won the rematch at Clash in Italy on May "
                 "31, and Femi won the final meeting inside Hell in a Cell at SummerSlam Night 1 on "
                 "August 1, 2026. That was Lesnar's last match; he retired on August 4, 2026, at age "
                 "49, calling himself the past and Femi the future."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Brock Edward Lesnar"),
        dict(label="Born", value="July 12, 1977", sub="Webster, South Dakota &middot; age 49"),
        dict(label="Billed from", value="Minneapolis, Minnesota / Webster, South Dakota"),
        dict(label="Height", value="6&#8242;3&#8243;", sub="191 cm"),
        dict(label="Weight", value="286 lb", sub="130 kg (billed)"),
        dict(label="Debut", value="2000", sub="Ohio Valley Wrestling; first televised WWE match "
                                              "April 21, 2002, vs. Jeff Hardy at Backlash"),
        dict(label="Trained by", value="Marty Morgan",
             sub="pro wrestling &middot; MMA under Greg Nelson and Erik Paulson"),
        dict(label="Amateur pedigree", value="NCAA Division I heavyweight champion, 2000",
             sub="University of Minnesota &middot; runner-up 1999"),
        dict(label="Signature", value="F-5 &middot; German suplex &middot; Kimura lock",
             sub="the F-5 was called The Verdict in NJPW"),
        dict(label="MMA record", value="5&ndash;3 (1 NC)",
             sub="UFC Heavyweight Champion 2008&ndash;2010; UFC 200 win over Mark Hunt overturned"),
        dict(label="Final match", value="August 1, 2026",
             sub="Hell in a Cell loss to Oba Femi, SummerSlam Night 1, Minneapolis"),
        dict(label="Status", value="Retired",
             sub="announced August 4, 2026 on The Pat McAfee Show; WWE.com lists him as an alumnus"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1977-07-12",
    bornplace="Webster, South Dakota, United States",
    nationality="United States",
    height_cm=191,
    weight_kg=130,
    ld=dict(
        alternateName=["The Beast Incarnate", "The Next Big Thing", "The Conqueror", "The Beast"],
        award=["WWE Championship (7 reigns)",
               "WWE Universal Championship (3 reigns, record; longest reign 504 days)",
               "IWGP Heavyweight Championship (1 reign)",
               "UFC Heavyweight Championship (2008-2010)",
               "NCAA Division I Heavyweight Wrestling Championship (2000)",
               "King of the Ring (2002)",
               "Royal Rumble winner (2003, 2022)"],
        knowsAbout=["Professional wrestling", "Mixed martial arts", "Amateur wrestling", "WWE",
                    "UFC", "New Japan Pro-Wrestling", "Freestyle wrestling"],
        description="Brock Lesnar is a retired American professional wrestler and mixed martial "
                    "artist. He won ten world championships in WWE, the IWGP Heavyweight "
                    "Championship, the UFC Heavyweight Championship and the 2000 NCAA Division I "
                    "heavyweight wrestling title, and ended The Undertaker's 21-0 WrestleMania "
                    "streak in 2014. He retired on August 4, 2026, three days after losing a Hell "
                    "in a Cell match to Oba Femi at SummerSlam.",
        sameAs=["https://en.wikipedia.org/wiki/Brock_Lesnar",
                "https://www.wwe.com/superstars/brock-lesnar"],
    ),
)
