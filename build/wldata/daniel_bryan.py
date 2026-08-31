# -*- coding: utf-8 -*-
"""Daniel Bryan (Bryan Danielson) - dossier data.

Sources: web-verified August 31, 2026 (Wikipedia, WrestleTalk, Wrestling Inc, SEScoops,
Fightful). Every match row carries a day-precision date confirmed in those sources.

Status note, verified for August 31, 2026: Danielson has not wrestled a competitive
match since losing the AEW World Championship to Jon Moxley at WrestleDream on
October 12, 2024, billed as the final match of his full-time career. He works AEW
commentary, was moved from AEW's active roster to its broadcast-team listing in
late May 2026, and appeared on the All In: London Buy In commentary desk on August
30, 2026 - yesterday, relative to this page's compile date. He has pointedly not
declared himself officially retired ("I think I could," to Chris Van Vliet,
December 2025), so this page says "stepped back," not "retired."

Deliberate omissions:
  * No career win-loss total - no verified figure exists.
  * No Meltzer star ratings in the signature block - his catalog of high-rated
    matches is real but the individual figures were not verified in this pass, so
    none are printed.
"""

# ----------------------------------------------------------------- record rows
# 16 documented bouts - the ROH reign's bookends, the WWE arc from 18 seconds to
# WrestleMania XXX, the 2016 retirement's reversal, and the AEW final chapter.
ROWS = [
    dict(result="W", date="2005-09-17", promo="ROH", landmark=True,
         event="Glory By Honor IV", opponent="James Gibson",
         stip="Singles — the 462-day reign begins", title="ROH World Championship"),
    dict(result="W", date="2006-09-16", promo="ROH",
         event="Glory By Honor V Night 2", opponent="KENTA",
         stip="Singles — defending through a separated shoulder", title="ROH World Championship"),
    dict(result="L", date="2006-12-23", promo="ROH", landmark=True,
         event="Final Battle — New York", opponent="Homicide",
         stip="Singles — the reign ends after 462 days", title="ROH World Championship"),
    dict(result="W", date="2010-09-19", promo="WWE",
         event="Night of Champions", opponent="The Miz",
         stip="Singles — submission, months after the NXT 'firing'",
         title="WWE United States Championship"),
    dict(result="W", date="2011-12-18", promo="WWE",
         event="TLC", opponent="Big Show",
         stip="Money in the Bank cash-in", title="World Heavyweight Championship"),
    dict(result="L", date="2012-04-01", promo="WWE", landmark=True,
         event="WrestleMania XXVIII", opponent="Sheamus",
         stip="Singles — 18 seconds; the loss that started the YES Movement",
         title="World Heavyweight Championship"),
    dict(result="W", date="2013-08-18", promo="WWE", landmark=True,
         event="SummerSlam", opponent="John Cena",
         stip="Singles — clean with the running knee; Orton cashes in minutes later",
         title="WWE Championship"),
    dict(result="W", date="2014-04-06", promo="WWE", landmark=True,
         event="WrestleMania XXX — New Orleans", opponent="Triple H",
         stip="Singles — the opener, to earn the main event", title=""),
    dict(result="W", date="2014-04-06", promo="WWE", landmark=True, type="tag",
         event="WrestleMania XXX — New Orleans", opponent="Randy Orton & Batista",
         stip="Triple threat — Batista taps to the YES Lock",
         title="WWE World Heavyweight Championship"),
    dict(result="W", date="2018-04-08", promo="WWE", landmark=True, type="tag",
         event="WrestleMania 34", opponent="Kevin Owens & Sami Zayn",
         stip="Tag, with Shane McMahon — first match after the 2016 medical retirement", title=""),
    dict(result="W", date="2018-11-13", promo="WWE",
         event="SmackDown", opponent="AJ Styles",
         stip="Singles — the low blow, the heel turn, the last WWE title", title="WWE Championship"),
    dict(result="L", date="2019-04-07", promo="WWE",
         event="WrestleMania 35", opponent="Kofi Kingston",
         stip="Singles — KofiMania takes the title", title="WWE Championship"),
    dict(result="D", date="2021-09-22", promo="AEW", landmark=True,
         event="Dynamite: Grand Slam — Arthur Ashe Stadium", opponent="Kenny Omega",
         stip="Singles — 30-minute time-limit draw in his AEW in-ring debut", title=""),
    dict(result="W", date="2023-06-25", promo="AEW",
         event="Forbidden Door", opponent="Kazuchika Okada",
         stip="Singles — finishes the match with a broken forearm", title=""),
    dict(result="W", date="2024-08-25", promo="AEW", landmark=True,
         event="All In — Wembley Stadium", opponent="Swerve Strickland",
         stip="Title vs. career", title="AEW World Championship"),
    dict(result="L", date="2024-10-12", promo="AEW", landmark=True,
         event="WrestleDream — Tacoma", opponent="Jon Moxley",
         stip="Singles — loses the title in the billed final match of his full-time career",
         title="AEW World Championship"),
]

DATA = dict(
    slug="daniel-bryan",
    name="Daniel Bryan",
    realname="Bryan Lloyd Danielson",
    epithet="The American Dragon",
    hook="Record & Titles",

    meta_desc=("Daniel Bryan - Bryan Danielson - stepped back from full-time wrestling after "
               "losing the AEW World Championship at WrestleDream 2024 and now works AEW "
               "commentary. Six world titles, the YES Movement, WrestleMania XXX. Full record, "
               "titles and career."),
    og_desc=("The American Dragon: ROH's 462-day champion, the YES Movement, the WrestleMania XXX "
             "double, an AEW World Championship at Wembley - and a commentary chair, because he "
             "still won't say the word retired."),
    tw_desc="Daniel Bryan: six world titles, two retirements (one reversed, one unofficial), one YES Movement.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1999",
    height_imp="5&#8242;10&#8243;",
    weight_lb="210",
    world_titles="6",
    vitals_tagline="YES! YES! YES!",
    support_note="Merch &middot; Watch &middot; Read",
    sp_items=[
        dict(ic="DB", title="Shop AEW", sub="Official merchandise",
             tag="Shop", href="https://www.shopaew.com/"),
        dict(ic="AEW", title="All Elite Wrestling", sub="Broadcast team — Collision and PPVs",
             tag="Visit", href="https://www.allelitewrestling.com/"),
        dict(ic="2K", title="WWE 2K", sub="A playable legend in past entries as Daniel Bryan",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="W", title="Wikipedia", sub="Full biography", tag="Read", charity=True,
             href="https://en.wikipedia.org/wiki/Bryan_Danielson"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The American Dragon &middot; Bryan Danielson &middot; leader of the YES Movement",
    hero_tag="Aberdeen, Washington &middot; <em>ROH &middot; WWE &middot; AEW &middot; 1999&ndash;2024, "
             "at the desk since</em>",
    now_label="NOW",
    now_bold="AEW commentary, not officially retired",
    now_tail=(" &middot; last competitive match October 12, 2024 &middot; moved to AEW's "
              "broadcast-team roster in May 2026 &middot; called the All In: London Buy In from "
              "Wembley on August 30, 2026"),
    hstats=[
        dict(value="6",   x=False, label="World Titles"),
        dict(value="462", x=False, label="Day ROH Reign"),
        dict(value="18",  x=True,  label="Seconds at WM XXVIII"),
        dict(value="2",   x=False, label="WrestleMania XXX Wins"),
    ],
    ghost_link="From a sixteen-hour drive to Shawn Michaels' school to the double at WrestleMania XXX",
    vlabel="Est. 1999 &middot; Aberdeen, Washington",
    mono="DB",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Daniel Bryan</b> &mdash; billed as <b>Bryan Danielson</b> everywhere but WWE, because "
        "that is his name &mdash; has spent his whole career being told he was too small, and "
        "answering with the most complete technical-wrestling resume of his generation. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">6</span>'
        '<span class="pull-cap">world championships &mdash; four WWE, one World Heavyweight, one AEW</span></span>'
        "He held the ROH World Championship for 462 days across 2005&ndash;06, won six world "
        "championships between WWE and AEW, headlined WrestleMania XXX at the peak of a fan revolt "
        "he did not plan and could not have scripted better, and closed the in-ring chapter at AEW "
        "WrestleDream on October 12, 2024, losing the AEW World Championship to Jon Moxley in what "
        "was billed as the final match of his full-time career. Since then: a commentary chair, "
        "and a door he has left conspicuously ajar.",

        "Get the status exactly right, because most summaries round it off wrong: <b>he is not "
        "officially retired</b>, and he says so. Asked directly by Chris Van Vliet in an interview "
        "published December 11, 2025 whether he considers himself fully retired, his answer was "
        "&ldquo;I think I could&rdquo; &mdash; a man describing a capability, not signing a "
        "document. The verifiable facts: no competitive match since WrestleDream 2024 (his only "
        "in-ring appearance since is an eight-second comedy dark match against Max Caster in June "
        "2025); a move into AEW commentary in 2025; removal from AEW&rsquo;s active-roster page to "
        "its broadcast-team listing, reported May 27, 2026; and Tony Khan saying publicly that "
        "Danielson is &ldquo;beat up&rdquo; and being given time off the road. His most recent "
        "appearance was the All In: London Buy In on August 30, 2026, calling the TBS "
        "Championship match at Wembley to one of the pops of the night. Stepped back, at the "
        "desk, never quite saying never.",

        "The career splits into three distinct legends. First, the independent one: trained at "
        "Shawn Michaels&rsquo; Texas Wrestling Academy from 1999, a founding-night main-eventer of "
        "Ring of Honor in February 2002, and from September 17, 2005 the ROH World Champion for "
        "462 days &mdash; a reign with 38-odd defenses across three continents that made "
        "&ldquo;best wrestler in the world&rdquo; a serious argument rather than a t-shirt. "
        "Second, the WWE one, which runs on the gap between how the company saw him and how "
        "crowds did: the 18-second WrestleMania XXVIII loss to Sheamus on April 1, 2012 that was "
        "meant to bury the act and instead detonated the YES Movement; the clean SummerSlam 2013 "
        "win over John Cena; and WrestleMania XXX on April 6, 2014, where he beat Triple H in the "
        "opener and then Randy Orton and Batista in the main event, Batista tapping to the YES "
        "Lock in front of 75,000 people chanting a word he had turned into a shared possession. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">18</span>'
        '<span class="pull-cap">seconds at WrestleMania XXVIII &mdash; the burial that accidentally built the YES Movement</span></span>'
        "Third, the AEW one: the 2021 jump, the Blackpool Combat Club, a broken forearm he "
        "wrestled through against Kazuchika Okada, and the Wembley coronation over Swerve "
        "Strickland at All In on August 25, 2024, title versus career, fourteen days before "
        "turning 43.",

        "Threaded through all of it is the body. A concussion-and-neck history forced a full "
        "medical retirement on February 8, 2016, announced in the ring in Seattle; two years of "
        "second opinions got him cleared on March 20, 2018, and the comeback &mdash; from retired "
        "to WrestleMania 34 tag win in three weeks, to WWE Champion again by November 2018 &mdash; "
        "remains one of the strangest full reversals in the sport&rsquo;s medical history. The "
        "2024 stepping-back was the sustainable version of the same decision: leave while the "
        "matches are still great, stay in the building. He turned 45 in May 2026, has two "
        "children with Brie Bella, and spends his Saturdays explaining holds on television with "
        "the enthusiasm of a man who never actually left.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["ROH", "WWE", "AEW"],
        promo_labels={"ROH": "ROH", "WWE": "WWE", "AEW": "AEW"},
        stats=[
            ("6",   "World titles"),
            ("462", "Day ROH reign"),
            ("18",  "Seconds at WM XXVIII"),
            ("2",   "Wins at WM XXX"),
            ("1",   "AEW World title"),
            ("2016", "Retired, then unretired 2018"),
        ],
        lead=("Sixteen documented bouts &mdash; the ROH reign&rsquo;s bookends, the WWE arc from "
              "18 seconds to the WrestleMania XXX double, and the AEW final chapter. A curated "
              "ledger, not a career count; no career win&ndash;loss total is published because no "
              "verified one exists. The June 2025 Max Caster dark match &mdash; eight seconds, "
              "played for comedy &mdash; is noted here and deliberately not tabulated as a "
              "competitive bout. Filter by match type, tap any column header to sort, and turn "
              "spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The bouts the reputation rests on. He owns one of the largest catalogs of "
                    "maximum-rated matches of any American wrestler, but individual Observer "
                    "figures were not verified in this pass, so no numbers are printed."),
    signature=[
        dict(rating="&mdash;", event="Glory By Honor V Night 2, 2006", opponent="KENTA",
             stip="ROH World Championship — the defense that defined the reign"),
        dict(rating="&mdash;", event="SummerSlam 2013", opponent="John Cena",
             stip="WWE Championship — clean, with the running knee"),
        dict(rating="&mdash;", event="WrestleMania XXX", opponent="Triple H; then Orton & Batista",
             stip="Two matches, one night, one title"),
        dict(rating="&mdash;", event="Dynamite: Grand Slam 2021", opponent="Kenny Omega",
             stip="The 30-minute draw that opened the AEW chapter"),
        dict(rating="&mdash;", event="All In 2024", opponent="Swerve Strickland",
             stip="AEW World Championship, title vs. career, Wembley"),
    ],
    signature_count_word="five",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("4&times;", "WWE Championship"),
            ("1", "World Heavyweight"),
            ("1", "AEW World title"),
            ("462", "Day ROH reign"),
        ],
        lead=("Six world championships across three companies, a Grand Slam in WWE, and the ROH "
              "reign that started the legend. Reign endpoints beyond those stated were not "
              "re-verified in this pass and are not invented here."),
        rows=[
            dict(ic="W", name="WWE Championship", count="4",
                 sub="SummerSlam 2013 (def. John Cena clean; lost to Randy Orton&rsquo;s cash-in "
                     "minutes later) &middot; Night of Champions 2013 (def. Orton; stripped amid "
                     "the fast-count controversy) &middot; WrestleMania XXX, April 6, 2014, as WWE "
                     "World Heavyweight Championship (def. Orton and Batista; vacated June 2014 to "
                     "neck surgery) &middot; November 13, 2018 (def. AJ Styles on SmackDown; lost "
                     "to Kofi Kingston at WrestleMania 35)"),
            dict(ic="H", name="World Heavyweight Championship", count="1",
                 sub="TLC, December 18, 2011 &mdash; the Money in the Bank cash-in on Big Show; "
                     "lost to Sheamus in 18 seconds at WrestleMania XXVIII"),
            dict(ic="A", name="AEW World Championship", count="1",
                 sub="All In at Wembley, August 25, 2024, def. Swerve Strickland with his career "
                     "on the line &middot; lost to Jon Moxley at WrestleDream, October 12, 2024 "
                     "&mdash; his final full-time match"),
            dict(ic="R", name="ROH World Championship", count="1",
                 sub="September 17, 2005 &ndash; December 23, 2006 &middot; def. James Gibson at "
                     "Glory By Honor IV, lost to Homicide at Final Battle &middot; 462 days, "
                     "defended across the US, UK, Europe and Japan"),
            dict(ic="U", name="WWE United States Championship", count="1",
                 sub="Night of Champions, September 19, 2010, submitting The Miz"),
            dict(ic="I", name="WWE Intercontinental Championship", count="1",
                 sub="WrestleMania 31 ladder match, 2015 &mdash; the reign a concussion cut short"),
            dict(ic="T", name="WWE / SmackDown Tag Team Championship", count="2",
                 sub="With Kane as Team Hell No (2012&ndash;13) and with Rowan (2019) &mdash; "
                     "completing the WWE Grand Slam"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="For a lone-wolf technician, he kept ending up in perfect two-man and four-man units.",
        cards=[
            dict(era="WWE &middot; 2012&ndash;2013",
                 name="Team Hell No",
                 members="Daniel Bryan, Kane",
                 desc="The anger-management tag team — a comedy act with real gold, holding the "
                      "WWE Tag Team Championship for 245 days. The hug-it-out segments were the "
                      "most-quoted WWE comedy of the era, and the team is the reason the YES/NO "
                      "call-and-response existed as a duet before it became a stadium chant."),
            dict(era="WWE &middot; 2013&ndash;2014",
                 name="The YES Movement",
                 members="Daniel Bryan and, functionally, the entire audience",
                 desc="Not a stable — a fan uprising WWE eventually surrendered to. From the "
                      "Rumble 2014 walkout chants to the staged occupation of the ring that got "
                      "him into WrestleMania XXX, it stands as the clearest case of crowd pressure "
                      "rewriting a WrestleMania main event."),
            dict(era="AEW &middot; 2022&ndash;2024",
                 name="Blackpool Combat Club",
                 members="Bryan Danielson, Jon Moxley, Claudio Castagnoli, Wheeler Yuta; William "
                         "Regal as founder-manager",
                 desc="The shoot-style unit built around Regal's coaching lineage. It gave "
                      "Danielson his best late-career programs — and its slow souring is the story "
                      "AEW used to close his career, with Moxley's faction turning on him around "
                      "the WrestleDream title match that ended the full-time run."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Two names for one act, plus the movement that swallowed both: <b>Bryan Danielson</b> "
             "(1999&ndash;2009, 2021&ndash;present) and <b>Daniel Bryan</b> (WWE, 2010&ndash;2021). "
             "The character barely changed; the trademark did.",
        cards=[
            dict(mono="AD", era="Indies &amp; ROH &middot; 1999&ndash;2009", name="The American Dragon",
                 desc="The Texas Wrestling Academy prodigy turned ROH cornerstone — a "
                      "submission-first, strike-heavy pure wrestler whose 'Best in the World' "
                      "billing was earned match by match across three continents."),
            dict(mono="DB", era="WWE &middot; 2010&ndash;2021", name="Daniel Bryan",
                 desc="WWE's renaming, which he came to own so completely that the fake name now "
                      "outranks the real one in search traffic. Ran the full arc: NXT season one "
                      "punchline, US Champion, cash-in world champion, 18-second loser, YES "
                      "Movement icon, WrestleMania XXX headliner, and — post-2018 comeback — the "
                      "eco-preacher 'Planet's Champion' heel, his most underrated character work."),
            dict(mono="BD", era="AEW &middot; 2021&ndash;", name="Bryan Danielson, again",
                 desc="The name restored, the dream-match years: Omega, Okada, Zack Sabre Jr., "
                      "MJF, Will Ospreay. The final-countdown entrance clock at All In 2024 made "
                      "the career's mortality the story, on purpose."),
            dict(mono="MIC", era="AEW &middot; 2025&ndash;", name="The commentator",
                 desc="At the desk for Collision and pay-per-views — analytical, openly gleeful, "
                      "and the promotion's most credible explainer of why a hold hurts. Moved "
                      "formally to the broadcast-team roster in May 2026."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Aberdeen, Washington to Wembley Stadium, with two retirements in between.",
        rows=[
            dict(year="1999", title="Trained by Shawn Michaels",
                 desc="Debuts in December 1999 out of the Texas Wrestling Academy under Michaels "
                      "and Rudy Gonzalez; William Regal becomes the other formative influence."),
            dict(year="2002", title="Ring of Honor's founding night",
                 desc="Main-events The Era of Honor Begins on February 23, 2002 — one of ROH's "
                      "founding fathers alongside Low Ki and Christopher Daniels."),
            dict(year="2005", title="The 462 days begin",
                 desc="Beats James Gibson at Glory By Honor IV on September 17 for the ROH World "
                      "Championship and defends it for fifteen months across three continents."),
            dict(year="2010", title="WWE, fired, rehired",
                 desc="Debuts in the first NXT season, is released over the tie-choking incident "
                      "in the Nexus angle, and is back by SummerSlam — US Champion by September 19."),
            dict(year="2012", title="18 seconds",
                 desc="Loses the World Heavyweight Championship to Sheamus in 18 seconds at "
                      "WrestleMania XXVIII on April 1. The crowd response over the following year "
                      "turns YES! into the loudest chant in wrestling."),
            dict(year="2013", title="Cena, clean",
                 desc="Beats John Cena cleanly for the WWE Championship at SummerSlam on August "
                      "18; Randy Orton cashes in minutes later, starting the eight-month screwjob "
                      "arc."),
            dict(year="2014", title="WrestleMania XXX",
                 desc="Beats Triple H, then Orton and Batista, in one New Orleans night on April "
                      "6. Neck surgery forces him to vacate the title in June."),
            dict(year="2016", title="Retired",
                 desc="Announces a full medical retirement on the February 8 Raw in Seattle after "
                      "years of concussions — 'I've loved this in a way I've never loved anything "
                      "else.'"),
            dict(year="2018", title="Unretired",
                 desc="Cleared by WWE's doctors on March 20 after two years of outside opinions; "
                      "wins at WrestleMania 34 within three weeks and takes the WWE Championship "
                      "from AJ Styles on November 13."),
            dict(year="2021", title="All Elite",
                 desc="Debuts at AEW All Out in September; the Grand Slam draw with Kenny Omega on "
                      "September 22 opens the dream-match era, and the Blackpool Combat Club "
                      "follows in 2022."),
            dict(year="2024", title="Wembley, then Tacoma",
                 desc="Wins the AEW World Championship from Swerve Strickland at All In on August "
                      "25, title versus career; loses it to Jon Moxley at WrestleDream in Tacoma "
                      "on October 12, the billed end of his full-time career."),
            dict(year="2026", title="The desk",
                 desc="Formally moved from AEW's active roster to the broadcast team in late May; "
                      "returns to the booth for the All In: London Buy In at Wembley on August 30, "
                      "still declining to say the word retired."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="The Authority",
                 desc="Less an opponent than a weather system: Triple H and Stephanie McMahon's "
                      "on-screen regime spent 2013-14 declaring him a B+ player, and the angle "
                      "worked because it dramatized the real company's real skepticism. It ended "
                      "with Triple H beaten in the WrestleMania XXX opener and the machine "
                      "tapping out in the main event."),
            dict(name="John Cena",
                 desc="One match carries it: SummerSlam, August 18, 2013, where Cena — publicly "
                      "picking his own opponent — put him over clean with the running knee. The "
                      "respect was the story; the Orton cash-in that followed was the heat."),
            dict(name="Kenny Omega",
                 desc="The dream match AEW was built to make: the 30-minute draw at Grand Slam on "
                      "September 22, 2021 in his in-ring debut for the company, then the rematches "
                      "and BCC-Elite wars. The draw finish did exactly what it was designed to do "
                      "— proved the ceiling was higher than either man alone."),
            dict(name="Jon Moxley",
                 desc="Blackpool Combat Club brothers turned final opponents. Moxley choking him "
                      "out at WrestleDream on October 12, 2024 — title, career framing, faction "
                      "betrayal all in one — is the last image of full-time Bryan Danielson, and "
                      "AEW chose it deliberately."),
            dict(name="Sheamus",
                 desc="18 seconds at WrestleMania XXVIII on April 1, 2012 — the most productive "
                      "loss in modern wrestling. The two spent the next decade having the long, "
                      "hard-hitting matches the WrestleMania one wasn't allowed to be."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Commentary",
        lead="The paper trail of a career that keeps getting narrated in real time.",
        rows=[
            dict(when="2015", title="YES!: My Improbable Journey to the Main Event of WrestleMania",
                 kind="Book",
                 desc="His autobiography, written with Craig Tello around the WrestleMania XXX "
                      "arc and the first retirement's approach."),
            dict(when="2010&ndash;2021", title="Total Divas / Total Bellas", kind="Television",
                 desc="Years of reality-TV visibility through his marriage to Brie Bella — the "
                      "reason a submission wrestler from Aberdeen was a mainstream-known name "
                      "during the YES years."),
            dict(when="2025&ndash;", title="AEW Collision and pay-per-view commentary", kind="Broadcast",
                 desc="Moved to the desk in 2025 and to AEW's broadcast-team roster listing in May "
                      "2026; his most recent appearance was the All In: London Buy In on August "
                      "30, 2026."),
            dict(when="2025", title="INSIGHT with Chris Van Vliet", kind="Interview",
                 desc="The December 2025 interview containing the load-bearing status quote: asked "
                      "if he is fully retired — 'I think I could.'"),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records and the achievements, stated the way the sources state them.",
        stats=[
            ("462", "Day ROH reign"),
            ("6",   "World titles"),
            ("2",   "WrestleMania XXX wins"),
        ],
        rows=[
            dict(name="Six world championships across WWE and AEW",
                 sub="Four WWE Championship reigns, the 2011-12 World Heavyweight Championship, "
                     "and the 2024 AEW World Championship — plus the ROH World Championship "
                     "before any of them."),
            dict(name="The 462-day ROH World Championship reign",
                 sub="September 17, 2005 to December 23, 2006, defended dozens of times across "
                     "three continents — the reign that made 'Best in the World' an argument "
                     "rather than a slogan."),
            dict(name="Two wins in one night at WrestleMania XXX",
                 sub="April 6, 2014: Triple H in the opener, then Orton and Batista in the main "
                     "event, with Batista tapping to the YES Lock."),
            dict(name="WWE Grand Slam Champion",
                 sub="World titles plus the Intercontinental (WrestleMania 31 ladder match), "
                     "United States (2010) and tag championships (Team Hell No, and with Rowan in "
                     "2019)."),
            dict(name="A medical retirement fully reversed",
                 sub="Retired February 8, 2016; cleared March 20, 2018 after independent "
                     "evaluations; WWE Champion again by November 13, 2018. There is no real "
                     "precedent for that round trip at his level."),
            dict(name="AEW World Champion at 43, title vs. career, Wembley",
                 sub="All In, August 25, 2024, over Swerve Strickland — the capstone win, taken "
                     "with his career explicitly on the line."),
            dict(name="Still not officially retired",
                 sub="His own framing, December 2025: asked if he considers himself fully "
                     "retired — 'I think I could.' The last in-ring appearance of any kind is an "
                     "eight-second comedy dark match against Max Caster in June 2025."),
        ],
        footnote=("Deliberately absent: a career win-loss total (no verified figure), Observer "
                  "star ratings (not verified in this pass), and any prediction about a return "
                  "&mdash; the sources support 'stepped back and left the door open,' and that is "
                  "exactly what is published."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Bryan_Danielson"),
        dict(k="WrestleTalk", v="Moved off AEW's active roster to the broadcast team (May 2026)",
             href="https://wrestletalk.com/news/bryan-danielson-removed-aew-roster-broadcast-team/"),
        dict(k="Wrestling Inc", v="Commentary return at the All In: London Buy In (Aug 30, 2026)",
             href="https://www.wrestlinginc.com/2247094/aew-all-in-2026-buy-in-bryan-danielson-returns-commentary/"),
        dict(k="Fightful", v="All In commentary appearance and Tony Khan's 'beat up' framing",
             href="https://www.fightful.com/wrestling-news/bryan-danielson-returns-to-commentary-at-aew-all-in"),
        dict(k="SEScoops", v="'Not officially retired' — the Van Vliet interview (Dec 2025)",
             href="https://www.sescoops.com/article/bryan-danielson-says-hes-not-officially-retired-from-in-ring-competition"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Daniel Bryan retired?",
            a="Functionally yes, officially no &mdash; and he is precise about the difference. His "
              "last competitive match was the AEW World Championship loss to Jon Moxley at "
              "WrestleDream on October 12, 2024, billed as the final match of his full-time "
              "career. Since then he has worked AEW commentary, was moved to the company&rsquo;s "
              "broadcast-team roster listing in May 2026, and called the All In: London Buy In on "
              "August 30, 2026. But asked directly in December 2025 whether he considers himself "
              "fully retired, his answer was &ldquo;I think I could&rdquo; &mdash; so this page "
              "says stepped back, not retired.",
            q_ld="Is Daniel Bryan (Bryan Danielson) retired from wrestling?",
            a_ld="Bryan Danielson has not officially retired, but he has not wrestled a "
                 "competitive match since losing the AEW World Championship to Jon Moxley at "
                 "WrestleDream on October 12, 2024, which was billed as the final match of his "
                 "full-time career. He now works as an AEW commentator, was moved from AEW's "
                 "active roster to its broadcast team in May 2026, and appeared on commentary at "
                 "All In: London on August 30, 2026. In a December 2025 interview he declined to "
                 "call himself fully retired."),
        dict(
            q="Why did Daniel Bryan stop wrestling full-time?",
            a="Accumulated damage, managed honestly. Years of concussions and neck injuries "
              "forced a complete medical retirement on February 8, 2016; after being cleared in "
              "March 2018 he wrestled six more years, but he structured the AEW run explicitly as "
              "a final chapter &mdash; the All In 2024 title win over Swerve Strickland carried a "
              "title-versus-career stipulation, and the WrestleDream loss to Moxley that October "
              "was announced in advance as the end of full-time competition. Tony Khan has since "
              "said plainly that Danielson is &ldquo;beat up&rdquo; and being kept off the road "
              "to recover.",
            q_ld="Why did Bryan Danielson stop wrestling full-time?",
            a_ld="Bryan Danielson stepped back from full-time wrestling because of accumulated "
                 "neck and concussion injuries. He had already taken a full medical retirement "
                 "from February 2016 to March 2018. His 2024 AEW run was framed as a final "
                 "chapter: he won the AEW World Championship at All In on August 25, 2024 with "
                 "his career on the line, and lost it to Jon Moxley at WrestleDream on October "
                 "12, 2024 in the billed final match of his full-time career. AEW president Tony "
                 "Khan has said Danielson is being given time to rest and recover."),
        dict(
            q="What happened in the 18-second WrestleMania match?",
            a="At WrestleMania XXVIII on April 1, 2012, he lost the World Heavyweight "
              "Championship to Sheamus in 18 seconds &mdash; one good-luck kiss for AJ Lee, one "
              "Brogue Kick. It was booked as a dismissal and backfired historically: the crowd "
              "chanted YES! all night and for months afterward, and the momentum from the insult "
              "built directly to the SummerSlam 2013 Cena win and the WrestleMania XXX main "
              "event. It is the canonical example of an audience overruling a booking decision.",
            q_ld="What happened in Daniel Bryan's 18-second WrestleMania match?",
            a_ld="At WrestleMania XXVIII on April 1, 2012, Daniel Bryan lost the World "
                 "Heavyweight Championship to Sheamus in 18 seconds, beaten by a single Brogue "
                 "Kick after kissing AJ Lee. The fan backlash to the quick loss fueled the YES "
                 "Movement, which built over two years to Bryan winning the WWE World Heavyweight "
                 "Championship in the main event of WrestleMania XXX on April 6, 2014."),
        dict(
            q="Is he Daniel Bryan or Bryan Danielson?",
            a="Both, by era. He was born Bryan Lloyd Danielson and wrestled as Bryan Danielson "
              "&mdash; the American Dragon &mdash; from 1999 through his independent and ROH "
              "years. WWE renamed him Daniel Bryan in 2010 and owns that trademark, so on his "
              "2021 jump to AEW he reverted to his real name. This page uses the slug and title "
              "most readers search for; the man himself has been Bryan Danielson on screen since "
              "September 2021.",
            q_ld="Is his name Daniel Bryan or Bryan Danielson?",
            a_ld="Daniel Bryan and Bryan Danielson are the same wrestler. He was born Bryan Lloyd "
                 "Danielson and used his real name on the independents and in Ring of Honor from "
                 "1999 to 2009. WWE billed him as Daniel Bryan from 2010 to 2021 and retains that "
                 "trademark. Since joining AEW in September 2021 he has again been billed as "
                 "Bryan Danielson."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Bryan Lloyd Danielson"),
        dict(label="Born", value="May 22, 1981", sub="Aberdeen, Washington &middot; age 45"),
        dict(label="Billed from", value="Aberdeen, Washington"),
        dict(label="Height", value="5&#8242;10&#8243;", sub="178 cm"),
        dict(label="Weight", value="210 lb", sub="95 kg (billed)"),
        dict(label="Debut", value="December 1999",
             sub="Texas Wrestling Academy class; ROH founding-night main event February 23, 2002"),
        dict(label="Trained by", value="Shawn Michaels & Rudy Gonzalez",
             sub="with William Regal as the other acknowledged formative influence"),
        dict(label="Ring names", value="Bryan Danielson &rarr; Daniel Bryan &rarr; Bryan Danielson",
             sub="1999&ndash;2009 &middot; WWE 2010&ndash;21 &middot; AEW 2021&ndash;present"),
        dict(label="Signature", value="YES Lock &middot; Busaiku Knee &middot; Cattle Mutilation "
                                      "&middot; the YES! chant",
             sub="repeated stomps to the head as the closing sequence of the AEW years"),
        dict(label="Family", value="Married to Brie Bella", sub="two children"),
        dict(label="Last match", value="October 12, 2024",
             sub="AEW WrestleDream, Tacoma &mdash; lost the AEW World Championship to Jon Moxley"),
        dict(label="Status", value="AEW broadcast team",
             sub="moved off the active roster May 2026; not officially retired, per his own words"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1981-05-22",
    bornplace="Aberdeen, Washington, United States",
    nationality="United States",
    height_cm=178,
    weight_kg=95,
    ld=dict(
        alternateName=["Bryan Lloyd Danielson", "Bryan Danielson", "The American Dragon",
                       "The Planet's Champion"],
        award=["WWE Championship (4 reigns)",
               "World Heavyweight Championship (1 reign)",
               "AEW World Championship (1 reign, 2024)",
               "ROH World Championship (1 reign, 462 days)",
               "WWE Intercontinental Championship (1 reign)",
               "WWE United States Championship (1 reign)",
               "WWE Tag Team Championship (1 reign, with Kane)",
               "SmackDown Tag Team Championship (1 reign, with Rowan)",
               "WWE Grand Slam Champion"],
        knowsAbout=["Professional wrestling", "Catch wrestling", "Ring of Honor", "WWE", "AEW",
                    "Blackpool Combat Club", "The YES Movement", "Wrestling commentary"],
        description="Daniel Bryan, born Bryan Lloyd Danielson and billed in AEW under his real "
                    "name, is an American professional wrestler and commentator. He held the ROH "
                    "World Championship for 462 days, won six world championships across WWE and "
                    "AEW, led the YES Movement to the main event of WrestleMania XXX in 2014, and "
                    "won the AEW World Championship at Wembley Stadium in August 2024. He stepped "
                    "back from full-time wrestling after losing that title to Jon Moxley at "
                    "WrestleDream on October 12, 2024 and now works on AEW's broadcast team, "
                    "while declining to declare himself officially retired.",
        sameAs=["https://en.wikipedia.org/wiki/Bryan_Danielson",
                "https://www.allelitewrestling.com/"],
    ),
)
