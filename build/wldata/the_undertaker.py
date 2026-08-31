# -*- coding: utf-8 -*-
"""The Undertaker - dossier data.

Sources: web-verified August 31, 2026 - Wikipedia (The Undertaker; WrestleMania 13), WWE.com
(WWE LFG season two announcement; 1 deadMAN Show listing), ITR Wrestling (August 4, 2026 -
head of creative for AAA, from the Insight with Chris Van Vliet interview) and TWNP (August
2026, on winding down the Six Feet Under podcast). All record-row dates are day-precision.

Deliberate omissions:
  * No career win-loss total - none is reliably published, so none is invented.
  * No theme entry - the gong and "Rest in Peace" are famous, but no Spotify track URL was
    verified in this pass, so the block is omitted per house rule.
  * The Boneyard match is dated April 4, 2020, the night WrestleMania 36 Night 1 aired; it
    was taped in late March. The air date is used, consistently with how WWE lists it.
  * His pre-WWF names, including the WCW run as Mean Mark Callous, are covered at
    /wrestlers/mean-mark-callous/, and the 2000-2003 biker incarnation at
    /wrestlers/the-american-badass/. This page covers the Deadman.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="1990-11-22", promo="WWE", landmark=True, type="tag",
         event="Survivor Series — Hartford", opponent="Dusty Rhodes' Dream Team",
         stip="Elimination tag debut as the Million Dollar Team's mystery partner — "
              "eliminates two, exits by count-out, team survives", title=""),
    dict(result="W", date="1991-03-24", promo="WWE", landmark=True,
         event="WrestleMania VII — Los Angeles", opponent="Jimmy Snuka",
         stip="Singles — the Streak begins, 1-0", title=""),
    dict(result="W", date="1991-11-27", promo="WWE", landmark=True,
         event="Survivor Series — Detroit", opponent="Hulk Hogan",
         stip="Singles — first WWF Championship, at 26, a year into the run",
         title="WWF Championship"),
    dict(result="W", date="1997-03-23", promo="WWE", landmark=True,
         event="WrestleMania 13 — Rosemont", opponent="Sycho Sid",
         stip="No disqualification — second WWF Championship", title="WWF Championship"),
    dict(result="L", date="1997-10-05", promo="WWE", landmark=True,
         event="Badd Blood: In Your House — St. Louis", opponent="Shawn Michaels", opponent_html=True,
         stip="The first Hell in a Cell — Kane debuts and Tombstones him", title=""),
    dict(result="W", date="1998-03-29", promo="WWE",
         event="WrestleMania XIV — Boston", opponent="Kane", opponent_html=True,
         stip="Singles — three Tombstones to put his brother down", title=""),
    dict(result="W", date="1998-06-28", promo="WWE", landmark=True,
         event="King of the Ring — Pittsburgh", opponent="Mankind",
         stip="Hell in a Cell — Foley thrown off, then through, the cell", title=""),
    dict(result="W", date="2009-04-05", promo="WWE", landmark=True,
         event="WrestleMania 25 — Houston", opponent="Shawn Michaels", opponent_html=True,
         stip="Singles — 17-0; widely called the best WrestleMania match ever", title=""),
    dict(result="W", date="2010-03-28", promo="WWE", landmark=True,
         event="WrestleMania XXVI — Glendale", opponent="Shawn Michaels", opponent_html=True,
         stip="Streak vs. career — Michaels retires, 18-0", title=""),
    dict(result="L", date="2014-04-06", promo="WWE", landmark=True,
         event="WrestleMania XXX — New Orleans", opponent="Brock Lesnar",
         stip="Singles — the Streak ends at 21-1", title=""),
    dict(result="L", date="2017-04-02", promo="WWE",
         event="WrestleMania 33 — Orlando", opponent="Roman Reigns",
         stip="Singles — leaves hat, gloves and coat in the ring", title=""),
    dict(result="W", date="2020-04-04", promo="WWE", landmark=True,
         event="WrestleMania 36 Night 1", opponent="AJ Styles",
         stip="Boneyard match — cinematic, taped on location; his final match", title=""),
]

for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Shawn Michaels": "shawn-michaels", "Kane": "kane"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="the-undertaker",
    name="The Undertaker",
    realname="Mark William Calaway",
    epithet="The Deadman",
    hook="Record & Titles",

    meta_desc=("The Undertaker went 21-0 at WrestleMania before Brock Lesnar ended the Streak, won "
               "seven world championships across thirty years in WWE, and now runs creative for AAA. "
               "Full record, titles, the Streak and the 2020 farewell."),
    og_desc=("The Deadman: a 21-match WrestleMania winning streak, seven world titles, a thirty-year "
             "run under one gimmick, and a second act booking Lucha Libre AAA."),
    tw_desc="21 straight WrestleMania wins, 7 world titles, 30 years as the Deadman.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1987",
    height_imp="6&#8242;10&#8243;",
    weight_lb="309",
    world_titles="7",
    vitals_tagline="Rest in peace",
    support_note="Merch &middot; Games &middot; Watch",
    sp_items=[
        dict(ic="UT", title="WWE Shop", sub="Official Deadman merch · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable legend in the 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="A&E", title="WWE LFG", sub="Head coach, seasons one and two",
             tag="Watch", href="https://www.aetv.com/shows/wwe-lfg"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/undertaker"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Deadman &middot; The Phenom &middot; The Last Outlaw &middot; formerly Mean Mark",
    hero_tag="Houston, Texas &middot; <em>WCCW &middot; WCW &middot; WWF/WWE &middot; 1987&ndash;2020</em>",
    now_label="NOW",
    now_bold="Head of creative, Lucha Libre AAA",
    now_tail=" &middot; confirmed the role himself in August 2026; LFG coaching done after season "
             "two, and the Six Feet Under podcast winding down",
    hstats=[
        dict(value="21",       x=False, label="Straight Mania Wins"),
        dict(value="25&ndash;2", x=False, label="WrestleMania Record"),
        dict(value="7",        x=True,  label="World Titles"),
        dict(value="30",       x=False, label="Year WWE Career"),
    ],
    ghost_link="From a Texas funeral gimmick pitch to the longest-tenured character in WWE history",
    vlabel="Est. 1987 &middot; Houston, Texas",
    mono="UT",

    # ---------------------------------------------------------------- 01 overview
    correction=2,
    overview=[
        "<b>The Undertaker</b> played one character for thirty years, and the character worked for "
        "all thirty of them. Mark Calaway debuted the undead mortician at Survivor Series on "
        "November 22, 1990 and retired him at WrestleMania 36 in 2020 without the gimmick ever "
        "being retooled into irrelevance &mdash; the longest continuous run of any character in WWE "
        "history. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">21</span>'
        '<span class="pull-cap">consecutive WrestleMania wins between 1991 and 2013 &mdash; the Streak</span></span>'
        "The centre of the legend is the Streak: twenty-one consecutive WrestleMania victories, "
        "starting with Jimmy Snuka at WrestleMania VII on March 24, 1991 and running through Punk, "
        "Michaels, Triple H, Flair, Batista and Edge, until Brock Lesnar pinned him at WrestleMania "
        "XXX on April 6, 2014 and the Superdome went silent. He finished his WrestleMania career "
        "25&ndash;2, with the only other loss to Roman Reigns in 2017.",

        "The titles matter less than the streak, but they are real: seven world championships "
        "&mdash; four WWF/WWE Championships and three World Heavyweight Championships. The first "
        "came absurdly early, beating Hulk Hogan at Survivor Series on November 27, 1991, one year "
        "and five days into the character&rsquo;s existence; the second at WrestleMania 13 over "
        "Sycho Sid. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">7</span>'
        '<span class="pull-cap">world championships &mdash; four WWF/WWE, three World Heavyweight &mdash; across sixteen years</span></span>'
        "He also more or less owns two match types: Hell in a Cell, which he "
        "headlined at its invention against Shawn Michaels at Badd Blood on October 5, 1997 (the "
        "night Kane debuted) and made mythic by throwing Mick Foley off the roof of it at King of "
        "the Ring on June 28, 1998, and the casket and Buried Alive stipulations built entirely "
        "around him. From 2000 to 2003 the character rode a motorcycle instead of rising from "
        "coffins &mdash; that biker incarnation is covered on its own page, "
        "/wrestlers/the-american-badass/, as is the pre-WWF run as Mean Mark Callous.",

        "His last match is regularly misdated. The Final Farewell at Survivor Series on November "
        "22, 2020 &mdash; thirty years to the day after the debut &mdash; was a retirement "
        "ceremony, not a match; he thanked the crowd and left his hat in the ring. The final "
        "<b>match</b> was the Boneyard match against AJ Styles, a cinematic brawl taped on "
        "location and aired on Night 1 of WrestleMania 36 on April 4, 2020, in the empty-arena "
        "pandemic era &mdash; he won it, buried Styles with a front loader, and rode off. So the "
        "career ends on a win, in a graveyard, with no crowd, which he has said in interviews "
        "bothered him less than people assume: the match was widely regarded as the best thing on "
        "the show.",

        "In 2026 he has quietly become a company man with real power. He was inducted into the "
        "Hall of Fame by Vince McMahon in April 2022, coached the A&amp;E competition series WWE "
        "LFG through its first two seasons alongside his wife Michelle McCool (herself inducted "
        "in 2025), toured the 1 deadMAN Show one-man stage act until WrestleMania 41 week, and "
        "&mdash; the real job &mdash; runs creative for Lucha Libre AAA, the Mexican promotion "
        "WWE acquired in 2025. He confirmed it plainly in August 2026 on Insight with Chris Van "
        "Vliet: &ldquo;in layman&rsquo;s terms, I&rsquo;m the head of creative&rdquo; (ITR "
        "Wrestling). In the same round of interviews he said he will let the Six Feet Under "
        "podcast lapse when its contract runs out. He is 61, and the work is now entirely behind "
        "the curtain.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWF/WWE"},
        stats=[
            ("21&ndash;1", "The Streak, at its end"),
            ("25&ndash;2", "Final WrestleMania record"),
            ("4&times;",   "WWF/WWE Championship"),
            ("3&times;",   "World Heavyweight"),
            ("2007",       "Royal Rumble win"),
            ("2022",       "Hall of Fame"),
        ],
        lead=("Twelve documented bouts &mdash; the debut, the Streak's bookends, both first-blood "
              "Hell in a Cell landmarks, the Hogan title win and the Boneyard farewell. A curated "
              "ledger, not a career count; no career win&ndash;loss total is published because "
              "none is reliably sourced. The Mean Mark Callous and American Badass years live on "
              "their own pages. Filter by match type, tap any column header to sort, and turn "
              "spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the reputation rests on. Ratings are Wrestling Observer figures "
                    "as commonly reported; the WrestleMania 25 match is among the highest-rated "
                    "WWE matches of its decade in most retrospectives."),
    signature=[
        dict(rating="5.0", event="WrestleMania 25 — Houston", opponent="Shawn Michaels",
             stip="Singles — the Streak at 17-0"),
        dict(rating="4.75", event="WrestleMania XXVI — Glendale", opponent="Shawn Michaels",
             stip="Streak vs. career — Michaels' retirement"),
        dict(rating="4.5", event="King of the Ring 1998 — Pittsburgh", opponent="Mankind",
             stip="Hell in a Cell — the fall off the roof"),
        dict(rating="4.5", event="WrestleMania XXVIII", opponent="Triple H",
             stip="Hell in a Cell — End of an Era, Michaels as referee"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("4&times;", "WWF/WWE Championship"),
            ("3&times;", "World Heavyweight"),
            ("7&times;", "Tag team reigns"),
            ("1",        "Royal Rumble win"),
        ],
        lead=("Seven world championships across sixteen years, which understates how the character "
              "was booked: for most of three decades he did not need a belt to main-event. Tag "
              "reign counts vary slightly by source depending on how the WCW tag title from the "
              "Invasion era is counted; the number here follows WWE's own accounting."),
        rows=[
            dict(ic="W", name="WWF/WWE Championship", count="4",
                 sub="Won from Hulk Hogan at Survivor Series, November 27, 1991, six days past the "
                     "character's first birthday; from Sycho Sid at WrestleMania 13; from Stone "
                     "Cold Steve Austin at Over the Edge, May 23, 1999, with Vince McMahon as "
                     "referee; and from Hogan again at Judgment Day, May 19, 2002, as the "
                     "Undisputed title"),
            dict(ic="H", name="World Heavyweight Championship", count="3",
                 sub="Won at WrestleMania 23 (Batista, April 1, 2007), WrestleMania XXIV (Edge, "
                     "March 30, 2008) and Hell in a Cell 2009 (CM Punk, October 4, 2009)"),
            dict(ic="T", name="Tag team championships", count="7",
                 sub="Six WWF/World Tag reigns with Stone Cold, The Big Show, The Rock and Kane, "
                     "plus a WCW Tag reign with Kane during the Invasion &mdash; the Brothers of "
                     "Destruction reigns are the remembered ones"),
            dict(ic="R", name="Royal Rumble", count="1",
                 sub="2007, from the No. 30 spot &mdash; the first man to win from No. 30, "
                     "outlasting Shawn Michaels in a famous final pairing"),
            dict(ic="C", name="USWA Unified World Heavyweight Championship", count="1",
                 sub="1989, as Master of Pain &mdash; the pre-WWF title run, reign details on the "
                     "Mean Mark Callous page"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="A loner by design, but the exceptions ran deep — one satanic cult, one brotherhood, "
             "one corporate marriage of convenience.",
        cards=[
            dict(era="WWF &middot; 1990&ndash;1994",
                 name="With Paul Bearer",
                 members="The Undertaker &amp; Paul Bearer, the urn between them",
                 desc="Not a faction, the essential double act. William Moody's Paul Bearer carried "
                      "the urn that powered the Deadman and delivered every 'Ohhh yes' for over a "
                      "decade across three separate alliances. Bearer's betrayals — to Mankind in "
                      "1996, to Kane in 1998 — structured the character's biggest feuds. Moody died "
                      "in 2013; the Hall of Fame took him in posthumously the following year."),
            dict(era="WWF &middot; 1998&ndash;1999",
                 name="The Ministry of Darkness",
                 members="The Undertaker, The Acolytes, Mideon, Viscera, The Brood, Paul Bearer",
                 desc="The gimmick at its darkest — crucifixion angles, black weddings, an attempted "
                      "abduction of Stephanie McMahon — merged briefly with Shane McMahon's "
                      "Corporation into the Corporate Ministry, with Vince McMahon revealed as the "
                      "Higher Power in June 1999. Held the WWF Championship during it."),
            dict(era="WWF/WWE &middot; 1997&ndash;2020, intermittently",
                 name="The Brothers of Destruction",
                 members="The Undertaker &amp; Kane",
                 desc="The longest on-again, off-again act in company history: storyline half-"
                      "brothers who fought at WrestleManias XIV and XX and teamed for tag titles in "
                      "between, including a WCW Tag reign in 2001. Their final match together was "
                      "against D-Generation X at Crown Jewel on November 2, 2018 — a loss both men "
                      "have since laughed about."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One gimmick, several coats of paint &mdash; and a pre-history under other names that "
             "wrestlelore keeps on separate pages: <b>Mean Mark Callous</b> in WCW "
             "(1989&ndash;1990) and the <b>American Badass</b> biker years (2000&ndash;2003).",
        cards=[
            dict(mono="MM", era="WCW &middot; 1989&ndash;1990", name="Mean Mark Callous",
                 desc="The Skyscrapers tag man and Dan Spivey replacement — a tall, athletic heavy "
                      "with a heart-punch finisher and no mystique. Covered in full at "
                      "/wrestlers/mean-mark-callous/."),
            dict(mono="UT", era="WWF &middot; 1990&ndash;2000", name="The Deadman",
                 desc="Grey gloves, purple accents, the hat and the urn — an undead Western "
                      "mortician who no-sold everything and never spoke above a rasp. The gimmick "
                      "nobody thought could last a year lasted a decade before its first reinvention."),
            dict(mono="AB", era="WWF/WWE &middot; 2000&ndash;2003", name="The American Badass",
                 desc="Motorcycle, bandana, Limp Bizkit and Kid Rock entrances, and the only era he "
                      "spoke like a person on television. Polarising then, reappraised since. "
                      "Covered at /wrestlers/the-american-badass/."),
            dict(mono="DM", era="WWE &middot; 2004&ndash;2020", name="The Deadman, restored",
                 desc="Returned at WrestleMania XX in 2004 and never left again — the mature hybrid "
                      "with the MMA-flavored offense, the gong, and the Streak as annual "
                      "centrepiece. The version most of the record rows on this page belong to."),
            dict(mono="MC", era="Since 2020", name="Mark Calaway, out of character",
                 desc="The retirement's real novelty: after thirty years of kayfabe silence he "
                      "started talking — The Last Ride documentary series, the 1 deadMAN Show, a "
                      "podcast, LFG coaching, and now an actual office running AAA creative."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="A funeral-parlor gimmick nobody believed in to the longest character run the company "
             "has ever produced.",
        rows=[
            dict(year="1987", title="Debut in Texas",
                 desc="Breaks in for World Class in Dallas; USWA and WCW runs follow under other "
                      "names, none of which stick."),
            dict(year="1990", title="The Deadman arrives",
                 desc="Debuts November 22, 1990 at Survivor Series as the Million Dollar Team's "
                      "mystery partner and is the talk of the show by the end of the night."),
            dict(year="1991", title="Champion inside a year",
                 desc="Beats Hulk Hogan for the WWF Championship at Survivor Series on November 27, "
                      "1991 — six days after the character's first anniversary."),
            dict(year="1997", title="Second title, first Cell",
                 desc="Wins the WWF Championship at WrestleMania 13 on March 23; loses the first "
                      "Hell in a Cell to Shawn Michaels at Badd Blood on October 5 — the night "
                      "Kane debuts and the family feud begins."),
            dict(year="1998", title="The Foley cell match",
                 desc="Throws Mankind from the roof of the cell at King of the Ring on June 28, "
                      "1998 — the most replayed clip in the stipulation's history."),
            dict(year="2007", title="Rumble from No. 30, world title at 23",
                 desc="First man to win the Royal Rumble from the final spot, then beats Batista "
                      "at WrestleMania 23 on April 1 for his first World Heavyweight Championship."),
            dict(year="2009-10", title="The Michaels matches",
                 desc="Beats Shawn Michaels at WrestleMania 25 on April 5, 2009 in the match of "
                      "the era, then retires him in the rematch at WrestleMania XXVI on March 28, "
                      "2010. The Streak reaches 18-0."),
            dict(year="2014", title="The Streak dies",
                 desc="Brock Lesnar pins him at WrestleMania XXX on April 6, 2014. 21-1. The "
                      "arena-wide disbelief becomes its own piece of footage."),
            dict(year="2020", title="The Boneyard and the farewell",
                 desc="Beats AJ Styles in the cinematic Boneyard match aired April 4, 2020 — his "
                      "final match — then delivers the Final Farewell at Survivor Series on "
                      "November 22, 2020, thirty years to the day after debuting."),
            dict(year="2022", title="Hall of Fame",
                 desc="Inducted by Vince McMahon on April 1, 2022 in Dallas, in a speech that ran "
                      "long past its slot and nobody minded."),
            dict(year="2025-26", title="The second career",
                 desc="Coaches WWE LFG seasons one and two on A&E, tours and then retires the 1 "
                      "deadMAN stage show after WrestleMania 41 week, and takes over as head of "
                      "creative for Lucha Libre AAA — confirmed in his own words in August 2026."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Kane", slug="kane",
                 desc="The defining family feud: the storyline half-brother who debuted by ripping "
                      "the door off the first Hell in a Cell on October 5, 1997 and Tombstoning "
                      "him. They headlined WrestleMania XIV (Taker won with three Tombstones), "
                      "fought the first Inferno match, met again at WrestleMania XX, and in "
                      "between kept reuniting as the Brothers of Destruction — a two-decade "
                      "double-helix of feud and partnership no other pairing matches."),
            dict(name="Shawn Michaels", slug="shawn-michaels",
                 desc="Four matches that define two careers: the first Hell in a Cell in 1997 "
                      "(Michaels won), the WrestleMania 25 classic in 2009, and the WrestleMania "
                      "XXVI rematch in 2010 that ended Michaels' career against the Streak. "
                      "Michaels also refereed the End of an Era cell match with Triple H in 2012."),
            dict(name="Mankind / Mick Foley",
                 desc="The 1996-98 feud that gave the Deadman his first true equal in strangeness "
                      "— Boiler Room Brawls, Buried Alive, and the King of the Ring 1998 cell "
                      "match, in which Foley fell sixteen feet through the announce table and "
                      "finished the match anyway."),
            dict(name="Brock Lesnar",
                 desc="Three eras of collisions, one of which ended the Streak at WrestleMania XXX "
                      "on April 6, 2014 — a result so protected that even the announcers sounded "
                      "unbriefed. Their 2015 rematches at Battleground and Hell in a Cell drew "
                      "some of the biggest non-Mania numbers of the decade."),
            dict(name="Triple H",
                 desc="The WrestleMania trilogy of 2001, 2011 and 2012 — the last two built on "
                      "the Streak, the finale inside the cell with Shawn Michaels as referee, "
                      "billed as the End of an Era and living up to it."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; After",
        lead="Thirty years of silence, then everything at once.",
        rows=[
            dict(when="2020", title="Undertaker: The Last Ride", kind="Documentary",
                 desc="Five-part WWE Network series following his 2017-2020 attempts to retire, "
                      "the first time he broke character on camera at length."),
            dict(when="2022&ndash;2025", title="1 deadMAN Show", kind="Live",
                 desc="One-man stage show of stories and Q&A, toured around premium live events "
                      "— including SummerSlam 2024 weekend in Cleveland — and wound down after "
                      "WrestleMania 41 week in 2025."),
            dict(when="2024&ndash;2026", title="Six Feet Under", kind="Podcast",
                 desc="His podcast; he said in August 2026 he would let it end when the current "
                      "contract expires, telling Chris Van Vliet he would rather pull a tooth "
                      "than keep podcasting."),
            dict(when="2025&ndash;2026", title="WWE LFG", kind="TV",
                 desc="Head coach on A&E's competition series for seasons one and two alongside "
                      "Michelle McCool, Booker T and Bubba Ray Dudley; stepped away after season "
                      "two."),
            dict(when="2025&ndash;", title="Lucha Libre AAA", kind="Executive",
                 desc="Head of creative for the WWE-acquired Mexican promotion — the role he "
                      "confirmed on Insight with Chris Van Vliet in August 2026, and his actual "
                      "day job now."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated plainly.",
        stats=[
            ("21",  "Straight Mania wins"),
            ("30",  "Years, one character"),
            ("7",   "World titles"),
        ],
        rows=[
            dict(name="The Streak: 21 consecutive WrestleMania wins, 1991-2013",
                 sub="Snuka to Punk, ended by Brock Lesnar at WrestleMania XXX on April 6, 2014. "
                     "Final WrestleMania record: 25-2, the second loss to Roman Reigns in 2017."),
            dict(name="Longest character run in WWE history",
                 sub="November 22, 1990 to November 22, 2020, debut to Final Farewell, thirty "
                     "years to the day — the farewell was a ceremony; the last match was the "
                     "Boneyard, April 4, 2020."),
            dict(name="First man to win the Royal Rumble from No. 30",
                 sub="2007, last eliminating Shawn Michaels."),
            dict(name="Present at the creation of Hell in a Cell",
                 sub="Headlined the first cell match at Badd Blood on October 5, 1997, and has "
                     "wrestled more cell matches than anyone — a count WWE has put in the teens; "
                     "the exact figure varies by source and is not pinned down here."),
            dict(name="Seven world championships",
                 sub="Four WWF/WWE Championships (1991, 1997, 1999, 2002) and three World "
                     "Heavyweight Championships (2007, 2008, 2009)."),
            dict(name="Hall of Fame, class of 2022",
                 sub="Inducted by Vince McMahon on April 1, 2022. Michelle McCool, his wife, "
                     "followed in the class of 2025, inducted by The Undertaker himself."),
        ],
        footnote=("No career win-loss total is published; none is reliably sourced anywhere. Tag "
                  "team reign counts vary by source depending on how the Invasion-era WCW Tag "
                  "Championship is treated; this page follows WWE's accounting. No Spotify theme "
                  "block: the gong is famous, but no track URL was verified in this pass."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography",
             href="https://en.wikipedia.org/wiki/The_Undertaker"),
        dict(k="WWE.com", v="WWE LFG season two — coaching roster",
             href="https://www.wwe.com/article/ae-and-wwe-to-premiere-wwe-lfg-season-2-in-june"),
        dict(k="WWE.com", v="1 deadMAN Show, SummerSlam weekend listing",
             href="https://www.wwe.com/article/undertaker-1-deadman-show-added-to-summerslam-weekend"),
        dict(k="ITR Wrestling", v="Head of creative for AAA — his own confirmation, August 2026",
             href="https://itrwrestling.com/news/wwe-the-undertaker-aaa/"),
        dict(k="TWNP", v="Winding down the Six Feet Under podcast, August 2026",
             href="https://www.twnpnews.com/2026/08/undertaker-makes-bold-decision-that-may-hurt-wwe-future/"),
        dict(k="Wikipedia", v="WrestleMania 13 — the second WWF title win",
             href="https://en.wikipedia.org/wiki/WrestleMania_13"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="What was The Undertaker&rsquo;s WrestleMania streak, exactly?",
            a="Twenty-one consecutive WrestleMania wins, from beating Jimmy Snuka at WrestleMania "
              "VII on March 24, 1991 through CM Punk at WrestleMania 29 in 2013. Brock Lesnar "
              "ended it at WrestleMania XXX on April 6, 2014. He wrestled four more WrestleManias "
              "afterward, losing only to Roman Reigns in 2017, and finished with a 25&ndash;2 "
              "record at the event. The Streak was never a planned institution &mdash; it was "
              "noticed retroactively around 2005 and then booked as the biggest prize on the card.",
            q_ld="What was The Undertaker's WrestleMania streak?",
            a_ld="The Undertaker won twenty-one consecutive WrestleMania matches between 1991 and "
                 "2013, beginning with Jimmy Snuka at WrestleMania VII on March 24, 1991. Brock "
                 "Lesnar ended the streak at WrestleMania XXX on April 6, 2014. The Undertaker "
                 "finished his career with a 25-2 WrestleMania record, his only other loss coming "
                 "against Roman Reigns in 2017."),
        dict(
            q="What was The Undertaker&rsquo;s last match?",
            a="The Boneyard match against AJ Styles, a cinematic match taped on location and "
              "aired on Night 1 of WrestleMania 36 on April 4, 2020. He won. The Final Farewell "
              "at Survivor Series on November 22, 2020 &mdash; thirty years to the day after his "
              "debut &mdash; is often miscalled his last match, but it was a retirement ceremony "
              "with no bout. He has stayed retired since; his 2018 Crown Jewel tag with Kane "
              "against D-Generation X was his last traditional televised match in front of a "
              "crowd.",
            q_ld="What was The Undertaker's last match?",
            a_ld="The Undertaker's last match was the cinematic Boneyard match against AJ Styles, "
                 "which aired on Night 1 of WrestleMania 36 on April 4, 2020, and which he won. "
                 "His appearance at Survivor Series on November 22, 2020, thirty years to the day "
                 "after his debut, was a retirement ceremony called the Final Farewell, not a "
                 "match. He has not wrestled since."),
        dict(
            q="How many world titles did The Undertaker win?",
            a="Seven &mdash; four WWF/WWE Championships and three World Heavyweight "
              "Championships. The first came from Hulk Hogan at Survivor Series on November 27, "
              "1991, barely a year into the character; the World Heavyweight reigns came in "
              "2007 (Batista, WrestleMania 23), 2008 (Edge, WrestleMania XXIV) and 2009 (CM "
              "Punk, Hell in a Cell). For most of his career, though, WWE deliberately kept him "
              "above the title picture &mdash; the Streak was his championship.",
            q_ld="How many world championships did The Undertaker win?",
            a_ld="The Undertaker won seven world championships: four WWF/WWE Championships, the "
                 "first from Hulk Hogan at Survivor Series on November 27, 1991, and three World "
                 "Heavyweight Championships, won at WrestleMania 23 in 2007, WrestleMania XXIV "
                 "in 2008 and Hell in a Cell in 2009."),
        dict(
            q="What does The Undertaker do now, in 2026?",
            a="He is the head of creative for Lucha Libre AAA, the Mexican promotion WWE "
              "acquired &mdash; a role that had been rumoured since the acquisition and which he "
              "confirmed himself in August 2026 on Insight with Chris Van Vliet. He coached the "
              "first two seasons of A&amp;E&rsquo;s WWE LFG with his wife Michelle McCool before "
              "stepping away, retired the 1 deadMAN stage show after WrestleMania 41 week in "
              "2025, and said in August 2026 that his Six Feet Under podcast will end when its "
              "contract runs out. He was inducted into the Hall of Fame by Vince McMahon in "
              "2022 and inducted McCool himself in 2025.",
            q_ld="What does The Undertaker do now in 2026?",
            a_ld="In 2026 The Undertaker works as the head of creative for Lucha Libre AAA, the "
                 "Mexican wrestling promotion acquired by WWE, a role he confirmed in an August "
                 "2026 interview. He coached the first two seasons of the A&E series WWE LFG, "
                 "retired his 1 deadMAN stage show in 2025, and announced in August 2026 that "
                 "his Six Feet Under podcast will end when its contract expires. He no longer "
                 "wrestles."),
        dict(
            q="Was Kane really his brother?",
            a="In storyline, yes &mdash; his half-brother, introduced through Paul Bearer&rsquo;s "
              "1997 revelations about a funeral-home fire. In reality Mark Calaway and Glenn "
              "Jacobs are unrelated and are longtime friends. The angle produced the debut at "
              "the first Hell in a Cell on October 5, 1997, WrestleMania matches in 1998 and "
              "2004, and the recurring Brothers of Destruction tag team, whose last match "
              "together was at Crown Jewel in November 2018.",
            q_ld="Was Kane really The Undertaker's brother?",
            a_ld="Only in storyline. Kane was introduced in 1997 as The Undertaker's half-"
                 "brother, debuting at the first Hell in a Cell match on October 5, 1997. In "
                 "reality Mark Calaway and Glenn Jacobs are not related and are longtime "
                 "friends who also teamed for years as the Brothers of Destruction."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Mark William Calaway"),
        dict(label="Born", value="March 24, 1965", sub="Houston, Texas &middot; age 61"),
        dict(label="Billed from", value="Death Valley"),
        dict(label="Height", value="6&#8242;10&#8243;", sub="208 cm"),
        dict(label="Weight", value="309 lb", sub="140 kg (billed)"),
        dict(label="Debut", value="1987", sub="World Class, Texas &middot; WWF debut November 22, 1990"),
        dict(label="Last match", value="April 4, 2020",
             sub="def. AJ Styles, Boneyard match, WrestleMania 36 Night 1"),
        dict(label="Ring names",
             value="Texas Red &rarr; Master of Pain &rarr; Mean Mark Callous &rarr; The Undertaker",
             sub="the WCW run and the American Badass era have their own wrestlelore pages"),
        dict(label="Signature", value="Tombstone Piledriver &middot; Chokeslam &middot; Last Ride "
                                      "&middot; Hell's Gate &middot; Old School"),
        dict(label="Hall of Fame", value="2022", sub="inducted by Vince McMahon, April 1, 2022"),
        dict(label="Family", value="Married to Michelle McCool",
             sub="Hall of Fame class of 2025 &mdash; he inducted her"),
        dict(label="Now", value="Head of creative, Lucha Libre AAA",
             sub="confirmed August 2026; LFG coaching and podcasting wound down"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1965-03-24",
    bornplace="Houston, Texas, United States",
    nationality="United States",
    height_cm=208,
    weight_kg=140,
    ld=dict(
        alternateName=["Mark Calaway", "Mark William Calaway", "The Deadman", "The Phenom",
                       "The Last Outlaw", "Mean Mark Callous", "The American Badass",
                       "Big Evil"],
        award=["WWF/WWE Championship (4 reigns)",
               "World Heavyweight Championship (3 reigns)",
               "WWF/WWE tag team championships (7 reigns, various partners)",
               "Royal Rumble winner (2007)",
               "21 consecutive WrestleMania victories (1991-2013)",
               "WWE Hall of Fame (2022)"],
        knowsAbout=["Professional wrestling", "WWE", "WrestleMania", "Hell in a Cell",
                    "Lucha Libre AAA", "Talent development"],
        description="The Undertaker, born Mark William Calaway in Houston, Texas, is a retired "
                    "American professional wrestler who portrayed the same character in WWE for "
                    "thirty years, from November 22, 1990 to November 22, 2020. He won twenty-one "
                    "consecutive WrestleMania matches before Brock Lesnar ended the Streak in "
                    "2014, held seven world championships, and won the 2007 Royal Rumble from the "
                    "No. 30 position. Inducted into the WWE Hall of Fame in 2022, he now serves "
                    "as head of creative for Lucha Libre AAA.",
        sameAs=["https://en.wikipedia.org/wiki/The_Undertaker",
                "https://www.wwe.com/superstars/undertaker"],
    ),
)
