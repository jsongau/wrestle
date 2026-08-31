# -*- coding: utf-8 -*-
"""Oba Femi - dossier data.

Sources: web research compiled August 31, 2026 - Wikipedia (Oba Femi), WWE.com (official
profile, SummerSlam and Sunday Night's Main Event pages, Raw previews), Sports
Illustrated (New Year's Evil 2026 walk-away, the SummerSlam title-shot decision),
Wrestling Inc. (Raw results, August 24, 2026), Bleacher Report (King of the Ring final).
Every match row carries a day-precision date stated in one of those sources.

Deliberate omissions and flags:
  * No career win-loss total: none is verified anywhere.
  * No social links: no handle verified as official in this pass.
  * The North American Championship reign length is a live conflict: WWE.com's profile
    says 272 days, Wikipedia says 273 - and the January 9 to October 8, 2024 endpoints
    arithmetically produce 273. Both figures are printed; the arithmetic is noted.
  * "Youngest North American Champion in history" is WWE.com's claim and is published
    here as WWE's claim, not independently verified.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2024-01-02", promo="WWE", landmark=True,
         event="NXT New Year's Evil", opponent="Riley Osborne",
         stip="2023 NXT Men's Breakout Tournament final", title=""),
    dict(result="W", date="2024-01-09", promo="WWE", landmark=True,
         event="NXT", opponent="Dragon Lee",
         stip="Breakout contract cash-in — one week after winning it",
         title="NXT North American Championship"),
    dict(result="W", date="2024-04-06", promo="WWE", type="tag",
         event="NXT Stand & Deliver", opponent="Dijak & Josh Briggs",
         stip="Triple threat — NXT's 2024 Match of the Year",
         title="NXT North American Championship"),
    dict(result="L", date="2024-10-08", promo="WWE", landmark=True,
         event="NXT", opponent="Tony D'Angelo",
         stip="Singles — the record 273-day reign ends, with his 2024 winning streak",
         title="NXT North American Championship"),
    dict(result="W", date="2025-01-07", promo="WWE", type="tag", landmark=True,
         event="NXT New Year's Evil", opponent="Trick Williams & Eddy Thorpe",
         stip="Triple threat — takes the top title", title="NXT Championship"),
    dict(result="W", date="2025-04-19", promo="WWE", type="tag",
         event="NXT Stand & Deliver", opponent="Trick Williams & Je'Von Evans",
         stip="Triple threat — NXT's 2025 Match of the Year", title="NXT Championship"),
    dict(result="L", date="2025-09-27", promo="WWE",
         event="NXT No Mercy", opponent="Ricky Saints",
         stip="Singles — the 263-day reign ends", title="NXT Championship"),
    dict(result="W", date="2025-12-06", promo="WWE", landmark=True,
         event="NXT Deadline", opponent="Ricky Saints",
         stip="Singles — second NXT Championship", title="NXT Championship"),
    dict(result="NC", date="2025-12-13", promo="WWE",
         event="Saturday Night's Main Event XLII", opponent="Cody Rhodes",
         stip="Champion vs. champion, non-title — thrown out on Drew McIntyre's interference",
         title=""),
    dict(result="W", date="2026-01-06", promo="WWE", landmark=True,
         event="NXT New Year's Evil", opponent="Leon Slater",
         stip="Singles — retains, then leaves the belt in the ring and walks out",
         title="NXT Championship"),
    dict(result="L", date="2026-01-31", promo="WWE", type="tag",
         event="Royal Rumble match — Riyadh", opponent="The 2026 Royal Rumble field",
         stip="Entered No. 1, five eliminations — including Bron Breakker in seconds — "
              "eliminated by Brock Lesnar", title=""),
    dict(result="W", date="2026-04-19", promo="WWE", landmark=True,
         event="WrestleMania 42 Night 2", opponent="Brock Lesnar",
         stip="Singles — answers the open challenge and wins", title=""),
    dict(result="W", date="2026-06-27", promo="WWE", landmark=True,
         event="Night of Champions — Riyadh", opponent="Jey Uso",
         stip="King of the Ring final", title=""),
    dict(result="W", date="2026-08-01", promo="WWE", landmark=True,
         event="SummerSlam Night 1 — Minneapolis", opponent="Brock Lesnar",
         stip="Hell in a Cell — Lesnar declares him the future afterward", title=""),
]

DATA = dict(
    slug="oba-femi",
    name="Oba Femi",
    realname="Isaac Odugbesan",
    epithet="The Ruler",
    hook="Record & Titles",

    meta_desc=("Oba Femi, The Ruler, held the NXT North American Championship for a record 273 "
               "days, won the NXT Championship twice, beat Brock Lesnar twice in 2026 and faces "
               "Bron Breakker at Sunday Night's Main Event. Full record, titles and career."),
    og_desc=("The Ruler: a record 273-day North American reign, two NXT Championships, the 2026 "
             "King of the Ring, two wins over Brock Lesnar — and Bron Breakker on September 6."),
    tw_desc="The Ruler: 273 days, two NXT titles, King of the Ring 2026, two wins over Lesnar.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2022",
    height_imp="6&#8242;6&#8243;",
    weight_lb="302",
    world_titles="0",
    vitals_tagline="The Ruler. The Conqueror.",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="OF", title="WWE Shop", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="AL", title="Alabama Track & Field", sub="SEC shot put champion, 2021-22",
             tag="Read", href="https://rolltide.com/"),
        dict(ic="NIL", title="WWE Next In Line", sub="Signed December 8, 2021",
             tag="Read", href="https://www.wwe.com/"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/oba-femi"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Ruler &middot; The Conqueror &middot; the NIL program&rsquo;s first champion",
    hero_tag="Lagos, Nigeria &middot; <em>NXT &middot; WWE &middot; 2022&ndash;present</em>",
    now_label="NOW",
    now_bold="Raw, no championship",
    now_tail=" &middot; faces Bron Breakker at Sunday Night&rsquo;s Main Event on September 6, "
             "fresh off beating Brock Lesnar inside Hell in a Cell at SummerSlam",
    hstats=[
        dict(value="273", x=False, label="Day NA Title Reign"),
        dict(value="2",   x=True,  label="NXT Titles"),
        dict(value="2026", x=False, label="King of the Ring"),
        dict(value="2",   x=False, label="Wins Over Lesnar"),
    ],
    ghost_link="From the Lagos shot put circle to leaving the NXT title in the ring",
    vlabel="Est. 2022 &middot; Lagos, Nigeria",
    mono="OF",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Oba Femi</b> is the wrestler WWE&rsquo;s college-athlete recruitment program was "
        "invented to produce, and 2026 has been the year the company said so out loud. He is a "
        "6&#8242;6&#8243; Nigerian former shot putter who signed through the Name, Image and "
        "Likeness program in December 2021, held the NXT North American Championship for a "
        "record 273 days, won the NXT Championship twice, and then &mdash; champion, unbeaten "
        "in the match, nothing left to take &mdash; retained one last time and left the belt "
        "lying in the ring. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">273</span>'
        '<span class="pull-cap">days as North American Champion &mdash; the longest reign in that title&rsquo;s history</span></span>'
        "Since walking out of NXT in January 2026 he has beaten Brock Lesnar twice &mdash; at "
        "WrestleMania 42 and inside Hell in a Cell at SummerSlam &mdash; won the King of the "
        "Ring, and been endorsed as the future of the company by Lesnar himself. The next test "
        "is Bron Breakker at Sunday Night&rsquo;s Main Event on September 6, a match built "
        "entirely on that endorsement.",

        "One number needs setting straight, and it is his employer&rsquo;s. WWE.com&rsquo;s "
        "profile calls the North American reign <b>272 days</b> and calls him the youngest "
        "North American Champion in history; Wikipedia logs the reign at <b>273 days</b>. The "
        "endpoints are not in dispute &mdash; he cashed in his Breakout Tournament contract on "
        "Dragon Lee on <b>January 9, 2024</b> and lost to Tony D&rsquo;Angelo on <b>October 8, "
        "2024</b> &mdash; and those dates arithmetically produce 273, so this page leads with "
        "273 and prints WWE&rsquo;s 272 beside it. The &ldquo;youngest champion&rdquo; line is "
        "WWE&rsquo;s claim and is reported here as such. Either way the reign is the longest in "
        "the title&rsquo;s history, and it ended along with a winning streak that had run "
        "through all of 2024 &mdash; thirty matches, per Wikipedia.",

        "He was born Isaac Odugbesan in Lagos on April 22, 1998, won ten medals at the "
        "Nigerian University Games as a University of Lagos freshman, moved to the United "
        "States in 2017, and threw shot put for Middle Tennessee State and then Alabama, where "
        "he took SEC indoor and outdoor titles in 2021&ndash;22 and a visual arts degree. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">263</span>'
        '<span class="pull-cap">days in his first NXT Championship reign, ended by Ricky Saints at No Mercy 2025</span></span>'
        "WWE signed him on December 8, 2021 through the NIL program; he reached the "
        "Performance Center in August 2022 and lost his first NXT ring appearances, which is "
        "worth remembering given what the record became. The turn came at New Year&rsquo;s "
        "Evil on January 2, 2024, when he won the Breakout Tournament final and, seven days "
        "later, cashed the contract in on a champion rather than waiting for a contendership. "
        "The first NXT Championship followed on January 7, 2025, in a triple threat over Trick "
        "Williams and Eddy Thorpe, and ran 263 days; the second was won back from Ricky Saints "
        "at Deadline on December 6, 2025 and surrendered voluntarily after 32 days.",

        "The 2026 main-roster run has been built almost entirely on Brock Lesnar, which is "
        "not a sentence written about many second-year wrestlers. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">2</span>'
        '<span class="pull-cap">wins over Brock Lesnar in 2026 &mdash; WrestleMania 42, then Hell in a Cell at SummerSlam</span></span>'
        "Femi entered the Royal Rumble at No. 1 on January 31, threw out five men &mdash; "
        "including Bron Breakker, in seconds &mdash; and was eliminated by Lesnar; he answered "
        "Lesnar&rsquo;s open challenge on the March 16 Raw and beat him at WrestleMania 42 "
        "Night 2 on April 19; he won the King of the Ring final over Jey Uso at Night of "
        "Champions on June 27, earning a guaranteed world title match at SummerSlam &mdash; "
        "and then gave it up. Lesnar returned on the June 29 Raw, attacked him mid-coronation, "
        "and Femi chose the grudge over the guarantee, forfeiting the title shot to take "
        "Lesnar inside Hell in a Cell. He won that too, on August 1 in Minneapolis, and Lesnar "
        "declared him the future afterward. Whether the forfeited title shot survives in some "
        "form has never been clarified on air; what exists instead is Breakker, September 6, "
        "and a contract Femi signed himself after putting Austin Theory through a table.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("273",  "Day NA reign"),
            ("2&times;", "NXT Championship"),
            ("263",  "Day first NXT reign"),
            ("2026", "King of the Ring"),
            ("2",    "Wins over Lesnar"),
            ("5",    "2026 Rumble eliminations"),
        ],
        lead=("Fourteen documented bouts &mdash; the tournament wins, every championship "
              "change, and the entire 2026 Lesnar arc. This is a curated ledger, not a career "
              "count; no verified win&ndash;loss total exists and none is invented. The one "
              "no-contest is real: the December 2025 champion-vs-champion match with Cody "
              "Rhodes was thrown out when Drew McIntyre interfered. Filter by match type, tap "
              "any column header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("No Wrestling Observer ratings are published here &mdash; none could be "
                    "verified for his matches in this pass, and this page does not assign its "
                    "own. NXT&rsquo;s year-end awards are the documented stand-in: the Stand "
                    "&amp; Deliver triple threat with Dijak and Josh Briggs was NXT&rsquo;s "
                    "2024 Match of the Year, and the Stand &amp; Deliver triple threat with "
                    "Trick Williams and Je&rsquo;Von Evans took the same award for 2025. Both "
                    "are in the record table with dates."),
    signature_count_word="two",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("2&times;", "NXT Championship"),
            ("273",      "Day NA reign"),
            ("1",        "King of the Ring"),
            ("0",        "Main-roster titles"),
        ],
        lead=("Three championship reigns, all in NXT, all ended either by upset or by his own "
              "choice &mdash; plus the tournament wins that bracket them. He has held no "
              "main-roster championship yet; the one guaranteed world title shot he earned, he "
              "traded for Brock Lesnar inside Hell in a Cell."),
        rows=[
            dict(ic="N", name="NXT Championship", count="2",
                 sub="2025 &middot; won January 7 in a triple threat over Trick Williams and "
                     "Eddy Thorpe at New Year&rsquo;s Evil, lost to Ricky Saints at No Mercy on "
                     "September 27 &mdash; <b>263 days</b> &middot; 2025&ndash;26 &middot; "
                     "regained from Saints at Deadline on December 6, retained against TNA "
                     "X-Division Champion Leon Slater at New Year&rsquo;s Evil on January 6, "
                     "2026, then left the belt in the ring &mdash; vacated January 7 after 32 "
                     "days, undefeated in the reign"),
            dict(ic="A", name="NXT North American Championship", count="1",
                 sub="January 9 &ndash; October 8, 2024 &middot; won by cashing in the Breakout "
                     "Tournament contract on Dragon Lee, lost to Tony D&rsquo;Angelo &middot; "
                     "<b>273 days, the longest reign in the title&rsquo;s history</b> &mdash; "
                     "WWE.com says 272, Wikipedia says 273, and the endpoints produce 273 "
                     "exactly &middot; WWE also bills him the youngest champion in the "
                     "title&rsquo;s history, a claim not independently verified here"),
            dict(ic="K", name="King of the Ring", count="2026",
                 sub="Won the final over Jey Uso at Night of Champions in Riyadh on June 27, "
                     "2026 &middot; the guaranteed SummerSlam world title match it carried was "
                     "forfeited two days later, traded for Lesnar inside Hell in a Cell"),
            dict(ic="B", name="NXT Men's Breakout Tournament", count="2023",
                 sub="Won the final over Riley Osborne at New Year&rsquo;s Evil on January 2, "
                     "2024, and cashed in the title-shot contract seven days later &middot; the "
                     "first NIL-program signee to win a tournament and go on to hold both a "
                     "secondary and a top NXT championship"),
            dict(ic="S", name="Men's Iron Survivor Challenge", count="2024",
                 sub="Won at NXT Deadline 2024, per Wikipedia &middot; the exact date was not "
                     "re-verified in this pass"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="None &mdash; ever, in either NXT or WWE. What he has instead is a growing file "
             "of endorsements from people who do not hand them out.",
        cards=[
            dict(era="NXT &middot; 2022&ndash;26",
                 name="A lone act by design",
                 members="Oba Femi, alone",
                 desc="From the Chase University segment that first put him on screen in "
                      "September 2022 to the night he left the NXT Championship in the ring, "
                      "he was booked without a stable, a manager or a regular second. The "
                      "Ruler character is the reason: a man who calls himself royalty does not "
                      "take instructions. No faction membership appears anywhere in his "
                      "history, which for a modern NXT main-eventer is genuinely unusual."),
            dict(era="WWE &middot; 2026",
                 name="The Lesnar endorsement",
                 members="Oba Femi; Brock Lesnar, unlikely advocate",
                 desc="Not an alliance — a torch-passing conducted at full force. Lesnar "
                      "eliminated him from the Royal Rumble, lost to him at WrestleMania 42, "
                      "attacked him during his King of the Ring coronation, lost to him again "
                      "inside Hell in a Cell at SummerSlam on August 1, 2026 — and then "
                      "declared him the future of WWE. Paul Heyman's newfound public respect "
                      "for Femi followed the same arc, which is precisely what set Bron "
                      "Breakker off."),
            dict(era="WWE &middot; August 2026",
                 name="Against The Vision",
                 members="Oba Femi vs. Bron Breakker, Bronson Reed, Austin Theory & Paul Heyman",
                 desc="The current program: Femi interrupted a Vision beatdown on the August "
                      "10 Raw and confronted Breakker; Heyman and Adam Pearce converted the "
                      "stand-offs into a Sunday Night's Main Event match on August 17; and at "
                      "the August 24 contract signing Femi absorbed a blindside forearm, put "
                      "Austin Theory through a ringside table and signed the contract himself. "
                      "One man against a faction, which is how his pages have always read."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Two names, one character. &ldquo;Oba&rdquo; is a Yoruba word for king, and the "
             "gimmick has never been anything but the word made literal.",
        cards=[
            dict(mono="IO", era="Track &amp; field &middot; 2016&ndash;2022", name="Isaac Odugbesan",
                 desc="The birth name, and the athletic resume the NIL program bought: ten "
                      "medals at the Nigerian University Games as a Lagos freshman, Conference "
                      "USA Male Freshman of the Year at Middle Tennessee State, SEC indoor and "
                      "outdoor shot put titles at Alabama in 2021 and 2022, and a visual arts "
                      "degree finished in May 2022 while WWE's contract sat signed."),
            dict(mono="OF", era="NXT &middot; 2022&ndash;24", name="Oba Femi, prospect",
                 desc="First on-screen appearance in a Chase University segment on September "
                      "27, 2022; in-ring debut that November, a loss. The early record was "
                      "unremarkable — which makes the January 2024 heel turn at New Year's "
                      "Evil, winning the Breakout Tournament and cashing in on a champion "
                      "within a week, the actual character debut."),
            dict(mono="RU", era="NXT &middot; 2024&ndash;26", name="The Ruler",
                 desc="The finished article: a champion who treated challengers as petitioners "
                      "and title defenses as administrative work. WWE.com's own epithet stack — "
                      "\"The Ruler. The Conqueror. The Destroyer of Worlds.\" — dates from "
                      "this run. The character's defining act was its exit: retaining the NXT "
                      "Championship one last time on January 6, 2026 and leaving the belt in "
                      "the ring, on the logic that a ruler does not defend territory he has "
                      "already outgrown."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Lagos to the Performance Center to two wins over Brock Lesnar, in under five "
             "years of matches.",
        rows=[
            dict(year="2016", title="Nigerian University Games",
                 desc="Wins ten medals as a University of Lagos freshman, specializing in shot "
                      "put; moves to the United States in 2017."),
            dict(year="2021", title="SEC titles and a WWE contract",
                 desc="Takes SEC shot put titles at Alabama across 2021-22 and signs with WWE "
                      "through the NIL program on December 8, 2021."),
            dict(year="2022", title="Performance Center and first appearances",
                 desc="Reports to Orlando in August; first on-screen appearance September 27 in "
                      "a Chase University segment; loses his in-ring debut in November."),
            dict(year="2024", title="The Breakout win and the record reign",
                 desc="Wins the Breakout Tournament final on January 2, cashes in on Dragon Lee "
                      "for the North American Championship on January 9, and holds it 273 days "
                      "— a title record — while running a 30-match winning streak through the "
                      "year. Wins the Iron Survivor Challenge in December."),
            dict(year="2025", title="NXT Champion, twice",
                 desc="Wins the NXT Championship in a New Year's Evil triple threat on January "
                      "7 and holds it 263 days; loses it to Ricky Saints at No Mercy on "
                      "September 27; wins it back at Deadline on December 6. Fights Undisputed "
                      "WWE Champion Cody Rhodes to a no-contest at Saturday Night's Main Event "
                      "on December 13."),
            dict(year="2026", title="Walks out of NXT, beats Lesnar twice, signs for Breakker",
                 desc="Leaves the NXT title in the ring on January 6; enters the Royal Rumble "
                      "at No. 1 on January 31 with five eliminations; beats Brock Lesnar at "
                      "WrestleMania 42 on April 19; wins King of the Ring over Jey Uso on June "
                      "27, forfeits the SummerSlam title shot it carried, and beats Lesnar "
                      "inside Hell in a Cell on August 1. Faces Bron Breakker at Sunday "
                      "Night's Main Event on September 6."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Brock Lesnar",
                 desc="The feud that made the main-roster run, conducted almost entirely in "
                      "Lesnar's language. Lesnar eliminated him from the Royal Rumble on "
                      "January 31, 2026; Femi answered his open challenge on the March 16 Raw "
                      "and beat him at WrestleMania 42 Night 2 on April 19; Lesnar returned on "
                      "June 29 to wreck the King of the Ring coronation; and Femi gave up his "
                      "guaranteed world title match to beat him inside Hell in a Cell at "
                      "SummerSlam on August 1 — after which Lesnar declared him the future. "
                      "Two wins over Lesnar in one calendar year is a resume very few active "
                      "wrestlers can match."),
            dict(name="Trick Williams",
                 desc="The NXT-era standard-bearer he had to go through repeatedly: the "
                      "January 2025 triple threat where Femi took the NXT Championship, and "
                      "the Stand & Deliver 2025 triple threat with Je'Von Evans that NXT named "
                      "its Match of the Year. Williams was the face of the brand; Femi was the "
                      "wall the brand ran into."),
            dict(name="Ricky Saints",
                 desc="The only man to beat him for a championship one-on-one — No Mercy, "
                      "September 27, 2025, ending the 263-day reign. Femi took the title back "
                      "at Deadline on December 6, which set up the walk-away: having answered "
                      "the one loss that needed answering, he had nothing left in NXT."),
            dict(name="Tony D'Angelo",
                 desc="The upset. D'Angelo ended the record North American reign on October 8, "
                      "2024 — taking the 2024 winning streak with it — and beat Femi again in "
                      "the Halloween Havoc rematch. The rare opponent the Ruler character "
                      "never fully solved on the way up."),
            dict(name="Bron Breakker",
                 desc="The live one. Femi threw an ambushed Breakker out of the Royal Rumble "
                      "in seconds in January; the program proper began August 10 when Femi "
                      "shut down a Vision beatdown, and closed to a contract on August 24 in a "
                      "signing that ended with Austin Theory through a table. Breakker's "
                      "stated grievance is the premise itself — that Lesnar and Paul Heyman "
                      "keep calling Femi the future. Femi's counter, delivered at the signing: "
                      "in another era Breakker might have been the future, but it is 2026, and "
                      "he has the misfortune of running against the man who actually is. "
                      "Sunday Night's Main Event, September 6."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Thin by design &mdash; the career is five years old and the verified list is "
             "short.",
        rows=[
            dict(when="2016&ndash;22", title="Collegiate shot put", kind="Athletics",
                 desc="University of Lagos, then Middle Tennessee State (Conference USA Male "
                      "Freshman of the Year) and Alabama, where he won SEC indoor and outdoor "
                      "shot put titles across 2021-22. The throwing mechanics are visible in "
                      "how he launches larger men than himself."),
            dict(when="2021&ndash;", title="WWE's NIL program", kind="Program",
                 desc="Signed December 8, 2021 in the Next In Line initiative's early "
                      "classes, and now its flagship outcome: the first NIL signee to win "
                      "both a secondary and a top NXT championship."),
            dict(when="2026", title="Interviews on the walk-away", kind="Interviews",
                 desc="His on-record explanations of vacating the NXT Championship — including "
                      "a 411Mania-covered interview that also traces the origin of his "
                      "entrance — are the closest thing to out-of-character media he has "
                      "done. No film, television or documentary credit could be verified, and "
                      "his video game debut could not be confirmed in this pass, so neither "
                      "is listed."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, with the one number his own employer disputes printed both ways.",
        stats=[
            ("273", "Day NA reign"),
            ("263", "Day NXT reign"),
            ("30",  "Match 2024 win streak"),
        ],
        rows=[
            dict(name="Longest NXT North American Championship reign in history",
                 sub="January 9 to October 8, 2024 — 273 days by Wikipedia's count and by the "
                     "arithmetic of the endpoints; WWE.com's profile says 272. WWE also bills "
                     "him as the youngest champion in the title's history, reported here as "
                     "WWE's claim."),
            dict(name="A 30-match winning streak across 2024",
                 sub="Per Wikipedia, ended by Tony D'Angelo on October 8, 2024 in the same "
                     "match that ended the record reign."),
            dict(name="Two NXT Championship reigns, the second ended by choice",
                 sub="263 days from January 7, 2025, then 32 days from December 6 — retained "
                     "against Leon Slater on January 6, 2026, then left the belt in the ring. "
                     "He was never beaten for the title in the second reign."),
            dict(name="First NIL signee to hold both a secondary and top NXT title",
                 sub="Per Wikipedia — the Breakout Tournament, the North American Championship "
                     "and the NXT Championship, all within 20 months."),
            dict(name="Two wins over Brock Lesnar in 2026",
                 sub="WrestleMania 42 Night 2 on April 19, answering an open challenge, and "
                     "Hell in a Cell at SummerSlam on August 1 — after which Lesnar publicly "
                     "declared him the future of WWE."),
            dict(name="King of the Ring, 2026 — and the title shot he refused",
                 sub="Beat Jey Uso in the final at Night of Champions on June 27. The crown "
                     "carried a guaranteed world title match at SummerSlam; when Lesnar "
                     "attacked him during the June 29 coronation, Femi forfeited the "
                     "guarantee to take the Cell match instead. Whether any claim on a future "
                     "shot survives has never been clarified on air."),
            dict(name="Five eliminations from the No. 1 spot in the 2026 Royal Rumble",
                 sub="Including Bron Breakker in seconds, moments after a masked man ambushed "
                     "Breakker on the ramp — the accidental first chapter of the September 6 "
                     "match. Lesnar eliminated Femi."),
            dict(name="NXT Male Superstar of the Year 2024, and two straight NXT Matches of the Year",
                 sub="The 2024 award for the Stand & Deliver triple threat with Dijak and Josh "
                     "Briggs, and the 2025 award for the Stand & Deliver triple threat with "
                     "Trick Williams and Je'Von Evans."),
        ],
        footnote=("Deliberately absent: a career win-loss total, which no source verifies; "
                  "social handles, unverified; Wrestling Observer ratings, none verified; and "
                  "a video game debut, unconfirmed. The 272-vs-273 conflict and the "
                  "\"youngest champion\" claim are printed above as they stand. Wikipedia "
                  "gives his billed weight as 310 pounds against WWE.com's 302; the WWE "
                  "figure is used."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/oba-femi"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Oba_Femi"),
        dict(k="Sports Illustrated", v="New Year's Evil 2026 — walking away from the NXT title",
             href="https://www.si.com/fannation/wrestling/wwe/nxt-new-year-evil-results-oba-femi-walks-away-from-the-nxt-championship"),
        dict(k="Sports Illustrated", v="Forfeiting the SummerSlam title shot for the Cell",
             href="https://www.si.com/fannation/wrestling/wwe/oba-femi-makes-stunning-decision-on-his-world-title-shot-at-wwe-summerslam"),
        dict(k="WWE.com", v="Sunday Night's Main Event preview — Femi vs. Breakker",
             href="https://www.wwe.com/shows/snme/2026-09-06/oba-femi-vs-bron-breakker"),
        dict(k="Wrestling Inc.", v="Raw results, August 24, 2026 — the contract signing",
             href="https://www.wrestlinginc.com/2243203/wwe-raw-august-24-stephanie-vaquer-roxanne-perez-contract-signing-more/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Why did Oba Femi vacate the NXT Championship?",
            a="Because he had nothing left to prove with it, and he said so with the belt "
              "rather than a speech. At New Year&rsquo;s Evil on <b>January 6, 2026</b> he "
              "retained against TNA X-Division Champion Leon Slater, then left the "
              "championship lying in the centre of the ring and walked out of the Performance "
              "Center; the title was formally vacated the next day, ending a 32-day second "
              "reign in which he was never beaten. He entered the Royal Rumble at No. 1 "
              "twenty-five days later, and the main-roster run &mdash; two wins over Brock "
              "Lesnar, the King of the Ring &mdash; followed from there.",
            q_ld="Why did Oba Femi vacate the NXT Championship in January 2026?",
            a_ld="Oba Femi vacated the NXT Championship after retaining it against Leon Slater "
                 "at NXT New Year's Evil on January 6, 2026. He left the championship belt in "
                 "the ring and walked out, and the title was vacated on January 7, ending a "
                 "32-day reign in which he was never defeated. He then moved to WWE's main "
                 "roster, entering the 2026 Royal Rumble at number one on January 31."),
        dict(
            q="Did Oba Femi really beat Brock Lesnar twice?",
            a="Yes &mdash; twice in under four months, which no one else has done in this "
              "era. He answered Lesnar&rsquo;s open challenge on the March 16, 2026 Raw and "
              "beat him at <b>WrestleMania 42 Night 2</b> on April 19; then, after Lesnar "
              "wrecked his King of the Ring coronation on June 29, he beat him again inside "
              "<b>Hell in a Cell</b> at SummerSlam on August 1 &mdash; surviving a tombstone "
              "piledriver along the way, per Cageside Seats &mdash; and Lesnar declared him "
              "the future of WWE afterward. The cost was real: Femi forfeited the guaranteed "
              "world title match his King of the Ring win carried to take the Cell match.",
            q_ld="Has Oba Femi beaten Brock Lesnar?",
            a_ld="Yes, twice in 2026. Oba Femi defeated Brock Lesnar at WrestleMania 42 Night "
                 "2 on April 19, 2026, after answering Lesnar's open challenge, and beat him "
                 "again inside Hell in a Cell at SummerSlam on August 1, 2026, after which "
                 "Lesnar publicly declared Femi the future of WWE. Femi forfeited the "
                 "guaranteed world championship match he had earned by winning the 2026 King "
                 "of the Ring in order to take the Hell in a Cell match."),
        dict(
            q="How long did Oba Femi hold the NXT North American Championship?",
            a="<b>273 days</b> by Wikipedia&rsquo;s count &mdash; January 9 to October 8, "
              "2024, from cashing in his Breakout Tournament contract on Dragon Lee to losing "
              "to Tony D&rsquo;Angelo &mdash; and those endpoints arithmetically produce 273. "
              "WWE.com&rsquo;s profile says <b>272</b>. Either way it is the longest reign in "
              "the title&rsquo;s history, and WWE additionally bills him as the youngest "
              "champion in the title&rsquo;s history, a claim this page reports without "
              "independently verifying.",
            q_ld="How long did Oba Femi hold the NXT North American Championship?",
            a_ld="Oba Femi held the NXT North American Championship from January 9 to October "
                 "8, 2024 — 273 days per Wikipedia, and the dates arithmetically produce 273, "
                 "though WWE.com's profile states 272 days. It is the longest reign in the "
                 "title's history. He won it by cashing in his 2023 Breakout Tournament "
                 "contract on Dragon Lee and lost it to Tony D'Angelo."),
        dict(
            q="Is Oba Femi a champion right now, and what is next for him?",
            a="No title, as of August 31, 2026 &mdash; by his own choosing twice over: he "
              "walked away from the NXT Championship in January and forfeited a guaranteed "
              "world title shot in June. What is next is signed and dated: <b>Bron Breakker, "
              "Sunday Night&rsquo;s Main Event, September 6</b>, made official at the August "
              "24 Raw contract signing that ended with Femi putting Austin Theory through a "
              "table. The stated stakes are which man is WWE&rsquo;s future; the practical "
              "stakes are his claim to the world title picture he keeps deferring.",
            q_ld="Is Oba Femi a champion right now?",
            a_ld="No. As of August 31, 2026 Oba Femi holds no championship. He vacated the NXT "
                 "Championship in January 2026 and forfeited his guaranteed world title match "
                 "in June 2026 to face Brock Lesnar instead. His next match is against Bron "
                 "Breakker at WWE Sunday Night's Main Event on September 6, 2026."),
        dict(
            q="What was Oba Femi before wrestling?",
            a="A shot putter, and a decorated one. Born Isaac Odugbesan in Lagos, he won ten "
              "medals at the Nigerian University Games as a University of Lagos freshman, "
              "moved to the United States in 2017, was Conference USA&rsquo;s Male Freshman "
              "of the Year at Middle Tennessee State, and won SEC indoor and outdoor shot put "
              "titles at Alabama in 2021&ndash;22 while finishing a visual arts degree. WWE "
              "signed him through its Name, Image and Likeness program on December 8, 2021 "
              "&mdash; and he is that program&rsquo;s first signee to win both a secondary "
              "and a top NXT championship.",
            q_ld="What did Oba Femi do before professional wrestling?",
            a_ld="Oba Femi, born Isaac Odugbesan in Lagos, Nigeria, was a collegiate shot "
                 "putter. He won ten medals at the Nigerian University Games for the "
                 "University of Lagos, was Conference USA Male Freshman of the Year at Middle "
                 "Tennessee State, and won SEC indoor and outdoor shot put titles at the "
                 "University of Alabama in 2021 and 2022. WWE signed him through its Name, "
                 "Image and Likeness program on December 8, 2021."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Isaac Odugbesan"),
        dict(label="Born", value="April 22, 1998", sub="Lagos, Nigeria &middot; age 28"),
        dict(label="Billed from", value="Lagos, Nigeria"),
        dict(label="Height", value="6&#8242;6&#8243;", sub="198 cm"),
        dict(label="Weight", value="302 lb",
             sub="per WWE.com &middot; Wikipedia lists 310 lb / 140 kg"),
        dict(label="Signed", value="December 8, 2021", sub="via WWE&rsquo;s NIL program"),
        dict(label="In-ring debut", value="November 11, 2022",
             sub="NXT live event &mdash; a loss to Channing Lorenzo"),
        dict(label="Trained at", value="WWE Performance Center", sub="from August 2022"),
        dict(label="Education", value="University of Alabama",
             sub="visual arts, 2022 &middot; SEC shot put champion indoors and out"),
        dict(label="Brand", value="Raw", sub="since walking out of NXT in January 2026"),
        dict(label="Also known as",
             value="The Ruler &middot; The Conqueror &middot; The Destroyer of Worlds",
             sub="the stack WWE.com&rsquo;s own profile uses"),
        dict(label="Next", value="Bron Breakker",
             sub="Sunday Night&rsquo;s Main Event &middot; September 6, 2026"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1998-04-22",
    bornplace="Lagos, Nigeria",
    nationality="Nigeria",
    alumni="University of Alabama",
    height_cm=198,
    weight_kg=137,
    ld=dict(
        alternateName=["Isaac Odugbesan", "The Ruler", "The Conqueror", "The Destroyer of Worlds"],
        award=["NXT Championship (2 reigns, 263 and 32 days)",
               "NXT North American Championship (1 reign, a record 273 days)",
               "WWE King of the Ring (2026)",
               "NXT Men's Breakout Tournament (2023)",
               "Men's Iron Survivor Challenge (2024)",
               "NXT Male Superstar of the Year (2024)",
               "NXT Match of the Year (2024, 2025)",
               "SEC shot put champion, indoor and outdoor (University of Alabama, 2021-22)"],
        knowsAbout=["Professional wrestling", "WWE", "NXT", "Shot put", "Track and field",
                    "Championship wrestling"],
        description="Oba Femi, born Isaac Odugbesan in Lagos, Nigeria, is a Nigerian "
                    "professional wrestler signed to WWE's Raw brand, billed as The Ruler. A "
                    "former SEC champion shot putter signed through WWE's NIL program in 2021, "
                    "he held the NXT North American Championship for a record 273 days, won "
                    "the NXT Championship twice, and voluntarily vacated it in January 2026. "
                    "On the main roster he beat Brock Lesnar at WrestleMania 42 and inside "
                    "Hell in a Cell at SummerSlam 2026, and won the 2026 King of the Ring. He "
                    "faces Bron Breakker at Sunday Night's Main Event on September 6, 2026.",
        sameAs=["https://en.wikipedia.org/wiki/Oba_Femi",
                "https://www.wwe.com/superstars/oba-femi"],
    ),
)
