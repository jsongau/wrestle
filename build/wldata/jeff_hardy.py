# -*- coding: utf-8 -*-
"""Jeff Hardy - dossier data.

Built from data/jeff-hardy.md (compiled November 9, 2026). Refresh of the August 31, 2026
module. Shared tag history follows data/matt-hardy.md (researched the same day); the
Jeff-specific parts were confirmed against Wikipedia's Jeff Hardy page and 2026 event
coverage (Wrestling Inc, Fightful, PWTorch). Every match row carries a day-precision date
confirmed in those sources.

Status, verified for November 9, 2026: ACTIVE in TNA, but out indefinitely in storyline.
syX (Joseph Sawyer and Samuel Shaw) were revealed as the backstage attackers on the
September 24, 2026 iMPACT, beat the Hardys at Bound for Glory on October 11, and beat them
again in a Slaughterhouse syX match on the October 29 iMPACT. The storyline injury report
listed lacerations and head trauma. Matt Hardy and Moose face syX at Destination X on
November 15, 2026 without Jeff. The Hardys are not champions: they won the TNA tag titles
for a fifth time at Slammiversary on June 28, 2026 and lost them to the Nemeths in a steel
cage at Lockdown on August 23, 2026.

Corrections made by this refresh (old claim, new claim):
  * TNA World Tag Team reigns with Matt: 3, now 5 (2015, 2016, 2024, 2025, 2026).
  * Debut: 1993, now May 23, 1994 (first WWF match, per Wikipedia's infobox).
  * Trainer: "largely self-taught", now Dory Funk Jr. and Michael Hayes.
  * Grand Slam: the 2018 US title completed the MODERN Grand Slam; the original format
    was completed earlier.
  * WWE tag count: "10 WWE tag reigns" plus NXT listed separately double counted. The
    10 is 9 main-roster reigns plus 1 NXT reign.
  * Armageddon 2008 and Bound for Glory 2010 rows were typed as tag matches; they were
    singles triple threats.

Deliberate omissions:
  * No career win-loss total. No verified figure exists.
  * No Meltzer star ratings in the signature block. Not verified.
  * No walk-out theme band. No current entrance theme or Spotify id was verified.
  * No key art: assets/art/jeff-hardy.svg does not exist yet, so DATA["art"] is unset.
  * The 2015 Ultimate X opponents come from the Matt Hardy module and were not
    re-verified independently in this pass.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="1999-07-05", promo="WWE", landmark=True, type="tag",
         event="Raw Is War", opponent="The Acolytes",
         stip="Tag, with Matt. Their first WWF tag title", title="WWF Tag Team Championship"),
    dict(result="W", date="1999-10-17", promo="WWE", landmark=True, type="tag",
         event="No Mercy", opponent="Edge & Christian",
         stip="Ladder match, with Matt. The Terri Invitational final", title=""),
    dict(result="L", date="2000-04-02", promo="WWE", landmark=True, type="tag",
         event="WrestleMania 2000", opponent="Edge & Christian; The Dudley Boyz",
         stip="Triangle ladder match", title="WWF Tag Team Championship"),
    dict(result="L", date="2000-08-27", promo="WWE", landmark=True, type="tag",
         event="SummerSlam", opponent="Edge & Christian; The Dudley Boyz",
         stip="The first TLC match", title="WWF Tag Team Championship"),
    dict(result="W", date="2000-09-24", promo="WWE", type="tag",
         event="Unforgiven", opponent="Edge & Christian",
         stip="Steel cage match, with Matt", title="WWF Tag Team Championship"),
    dict(result="L", date="2001-04-01", promo="WWE", landmark=True, type="tag",
         event="WrestleMania X-Seven", opponent="Edge & Christian; The Dudley Boyz",
         stip="TLC II", title="WWF Tag Team Championship"),
    dict(result="W", date="2001-04-12", promo="WWE",
         event="SmackDown (taped April 10)", opponent="Triple H",
         stip="Singles. The upset", title="WWF Intercontinental Championship"),
    dict(result="L", date="2001-11-18", promo="WWE", type="tag",
         event="Survivor Series", opponent="The Dudley Boyz",
         stip="Steel cage unification match, with Matt", title="WWF Tag Team Championship"),
    dict(result="W", date="2001-12-09", promo="WWE",
         event="Vengeance", opponent="Matt Hardy",
         stip="Brother vs. brother, Lita as special referee", title=""),
    dict(result="L", date="2002-07-01", promo="WWE", landmark=True,
         event="Raw", opponent="The Undertaker",
         stip="Ladder match. The loss that made him a singles act",
         title="WWE Undisputed Championship"),
    dict(result="W", date="2002-07-08", promo="WWE",
         event="Raw", opponent="William Regal",
         stip="Singles", title="WWE European Championship"),
    dict(result="W", date="2006-10-02", promo="WWE",
         event="Raw", opponent="Johnny Nitro",
         stip="Singles. Second Intercontinental reign", title="WWE Intercontinental Championship"),
    dict(result="W", date="2006-11-13", promo="WWE",
         event="Raw", opponent="Johnny Nitro",
         stip="Singles. Third Intercontinental reign", title="WWE Intercontinental Championship"),
    dict(result="W", date="2007-09-03", promo="WWE",
         event="Raw", opponent="Umaga",
         stip="Singles. Fourth Intercontinental reign", title="WWE Intercontinental Championship"),
    dict(result="W", date="2008-12-14", promo="WWE", landmark=True,
         event="Armageddon", opponent="Edge; Triple H",
         stip="Triple threat. First world title", title="WWE Championship"),
    dict(result="L", date="2009-01-25", promo="WWE",
         event="Royal Rumble", opponent="Edge",
         stip="Singles. Matt turns on him with a chair", title="WWE Championship"),
    dict(result="L", date="2009-04-05", promo="WWE",
         event="WrestleMania 25", opponent="Matt Hardy",
         stip="Extreme Rules match, after the Royal Rumble betrayal", title=""),
    dict(result="W", date="2009-06-07", promo="WWE", landmark=True,
         event="Extreme Rules", opponent="Edge",
         stip="Ladder match", title="World Heavyweight Championship"),
    dict(result="L", date="2009-06-07", promo="WWE",
         event="Extreme Rules", opponent="CM Punk",
         stip="Money in the Bank cash-in, minutes later", title="World Heavyweight Championship"),
    dict(result="W", date="2009-07-26", promo="WWE",
         event="Night of Champions", opponent="CM Punk",
         stip="Singles. Second World Heavyweight reign", title="World Heavyweight Championship"),
    dict(result="L", date="2009-08-23", promo="WWE", landmark=True,
         event="SummerSlam", opponent="CM Punk",
         stip="TLC. Days later a cage loss to Punk wrote him out of WWE",
         title="World Heavyweight Championship"),
    dict(result="W", date="2010-10-10", promo="TNA", landmark=True,
         event="Bound for Glory", opponent="Kurt Angle; Mr. Anderson",
         stip="Three-way for the vacant title. The heel turn that became Immortal",
         title="TNA World Heavyweight Championship"),
    dict(result="L", date="2011-01-09", promo="TNA",
         event="Genesis", opponent="Mr. Anderson",
         stip="Singles", title="TNA World Heavyweight Championship"),
    dict(result="W", date="2011-02-13", promo="TNA",
         event="Against All Odds", opponent="Mr. Anderson",
         stip="Ladder match. Second TNA world title", title="TNA World Heavyweight Championship"),
    dict(result="L", date="2011-03-13", promo="TNA", landmark=True,
         event="Victory Road", opponent="Sting",
         stip="Singles, stopped in about 90 seconds. The public low point",
         title="TNA World Heavyweight Championship"),
    dict(result="W", date="2012-10-14", promo="TNA", landmark=True,
         event="Bound for Glory", opponent="Austin Aries",
         stip="Singles. The redemption reign, his third TNA world title",
         title="TNA World Heavyweight Championship"),
    dict(result="L", date="2013-03-10", promo="TNA",
         event="Lockdown", opponent="Bully Ray",
         stip="Steel cage match", title="TNA World Heavyweight Championship"),
    dict(result="W", date="2015-03-16", promo="TNA", type="tag",
         event="Impact (aired April 17)", opponent="Aries & Roode; King & Low Ki; EC3 & Bram",
         stip="Ultimate X for the vacant title, with Matt", title="TNA World Tag Team Championship"),
    dict(result="L", date="2016-07-05", promo="TNA",
         event="Impact: The Final Deletion", opponent="Matt Hardy",
         stip="Cinematic match at the Hardy compound, as Brother Nero", title=""),
    dict(result="W", date="2016-10-02", promo="TNA", type="tag",
         event="Bound for Glory", opponent="Decay",
         stip="The Great War, as the Broken Hardys", title="TNA World Tag Team Championship"),
    dict(result="W", date="2017-04-02", promo="WWE", landmark=True, type="tag",
         event="WrestleMania 33", opponent="Gallows & Anderson; Cesaro & Sheamus; Enzo & Cass",
         stip="Fatal four-way ladder match, with Matt. The surprise return",
         title="Raw Tag Team Championship"),
    dict(result="L", date="2017-06-04", promo="WWE", type="tag",
         event="Extreme Rules", opponent="Cesaro & Sheamus",
         stip="Steel cage, with Matt", title="Raw Tag Team Championship"),
    dict(result="W", date="2018-04-16", promo="WWE",
         event="Raw", opponent="Jinder Mahal",
         stip="Singles. Completes the modern Grand Slam", title="WWE United States Championship"),
    dict(result="W", date="2019-04-09", promo="WWE", type="tag",
         event="SmackDown", opponent="The Usos",
         stip="Tag, with Matt", title="SmackDown Tag Team Championship"),
    dict(result="W", date="2020-08-21", promo="WWE",
         event="SmackDown", opponent="AJ Styles",
         stip="Singles. Fifth Intercontinental reign", title="WWE Intercontinental Championship"),
    dict(result="W", date="2022-05-29", promo="AEW", type="tag",
         event="Double or Nothing", opponent="The Young Bucks",
         stip="Tag, with Matt, back together in AEW", title=""),
    dict(result="L", date="2024-02-14", promo="AEW",
         event="Rampage", opponent="Sammy Guevara",
         stip="No DQ. His last AEW match", title=""),
    dict(result="W", date="2024-10-26", promo="TNA", landmark=True, type="tag",
         event="Bound for Glory", opponent="The System; ABC",
         stip="Full Metal Mayhem, with Matt. Third TNA tag reign",
         title="TNA World Tag Team Championship"),
    dict(result="L", date="2025-04-27", promo="TNA", type="tag",
         event="Rebellion", opponent="The Nemeths",
         stip="Tag, with Matt. The 183-day reign ends", title="TNA World Tag Team Championship"),
    dict(result="W", date="2025-07-20", promo="TNA", type="tag",
         event="Slammiversary", opponent="The Nemeths; The Rascalz; Fir$t Cla$$",
         stip="Four-way ladder match, with Matt. Fourth TNA tag reign",
         title="TNA World Tag Team Championship"),
    dict(result="W", date="2025-10-07", promo="WWE", landmark=True, type="tag",
         event="NXT vs. TNA Showdown", opponent="DarkState",
         stip="Winners take all, with Matt. NXT and TNA tag titles at once",
         title="NXT Tag Team Championship"),
    dict(result="W", date="2025-10-12", promo="TNA", landmark=True, type="tag",
         event="Bound for Glory", opponent="Team 3D",
         stip="Tables match, Team 3D's retirement match", title="TNA World Tag Team Championship"),
    dict(result="L", date="2025-10-25", promo="WWE", type="tag",
         event="NXT Halloween Havoc", opponent="DarkState",
         stip="Broken Rules match, with Matt. The 18-day NXT reign ends",
         title="NXT Tag Team Championship"),
    dict(result="L", date="2026-04-11", promo="TNA", type="tag",
         event="Rebellion", opponent="The System",
         stip="Tag, with Matt. The 265-day reign ends", title="TNA World Tag Team Championship"),
    dict(result="W", date="2026-06-28", promo="TNA", landmark=True, type="tag",
         event="Slammiversary", opponent="The System; The Righteous; The Great Hands",
         stip="Four-way ladder match, as the Broken Hardys. Fifth TNA tag reign",
         title="TNA World Tag Team Championship"),
    dict(result="L", date="2026-08-23", promo="TNA", type="tag",
         event="Lockdown", opponent="The Nemeths",
         stip="Steel cage, with Matt. The 56-day reign ends", title="TNA World Tag Team Championship"),
    dict(result="L", date="2026-10-08", promo="TNA", type="tag",
         event="iMPACT", opponent="The Nemeths",
         stip="Title rematch. Nic Nemeth rolled Jeff up after a syX distraction",
         title="TNA World Tag Team Championship"),
    dict(result="L", date="2026-10-11", promo="TNA", landmark=True, type="tag",
         event="Bound for Glory", opponent="syX",
         stip="Falls Count Anywhere, with Matt. Erick Redbeard interfered", title=""),
    dict(result="L", date="2026-10-29", promo="TNA", landmark=True, type="tag",
         event="iMPACT", opponent="syX",
         stip="Slaughterhouse syX match, with Matt. Jeff written out injured", title=""),
]

DATA = dict(
    slug="jeff-hardy",
    name="Jeff Hardy",
    realname="Jeffrey Nero Hardy",
    epithet="The Charismatic Enigma",
    hook="Record & Titles",

    meta_desc=("Jeff Hardy, the Charismatic Enigma, is on the TNA roster at 49 and out in storyline "
               "after syX's October 29, 2026 Slaughterhouse match. Six world titles, the TLC "
               "canon, five TNA tag reigns. Full record, titles and career."),
    og_desc=("The Charismatic Enigma: the TLC matches that redefined risk, six world "
             "championships, a fifth TNA tag reign in 2026, and a storyline exit at the hands "
             "of syX."),
    tw_desc="Jeff Hardy: six world titles, the TLC canon, five TNA tag reigns, still in TNA at 49.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1994",
    height_imp="6&#8242;1&#8243;",
    weight_lb="225",
    world_titles="6",
    vitals_tagline="The Charismatic Enigma",
    support_note="Merch &middot; Watch &middot; Read",
    sp_items=[
        dict(ic="JH", title="TNA Wrestling", sub="Official site, iMPACT weekly",
             tag="Visit", href="https://tnawrestling.com/"),
        dict(ic="PWT", title="Pro Wrestling Tees", sub="Independent merch marketplace",
             tag="Shop", href="https://www.prowrestlingtees.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable in WWE 2K26 (Season 4 pass)",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="W", title="Wikipedia", sub="Full biography", tag="Read", charity=True,
             href="https://en.wikipedia.org/wiki/Jeff_Hardy"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Charismatic Enigma &middot; Brother Nero &middot; Willow &middot; one half of The Hardys",
    hero_tag="Cameron, North Carolina &middot; <em>WWE &middot; TNA &middot; AEW "
             "&middot; TNA again &middot; 1994&ndash;present</em>",
    now_label="NOW",
    now_bold="On the TNA roster, out injured in storyline",
    now_tail=(" &middot; syX left him with &ldquo;lacerations and head trauma&rdquo; in the "
              "Slaughterhouse match on the October 29, 2026 iMPACT &middot; Matt Hardy and Moose "
              "face syX at Destination X on November 15 &middot; not a champion: the Nemeths "
              "took the TNA tag titles at Lockdown on August 23"),
    hstats=[
        dict(value="6",  x=False, label="World Titles"),
        dict(value="10", x=False, label="WWE Tag Reigns w/ Matt, NXT incl."),
        dict(value="5",  x=False, label="TNA Tag Reigns w/ Matt"),
        dict(value="0",  x=True,  label="Current Titles"),
    ],
    ghost_link="From a Cameron trampoline federation to every ladder that ever mattered",
    vlabel="Est. 1994 &middot; Cameron, North Carolina",
    mono="JH",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Jeff Hardy</b> is 49, still on the TNA roster, and out indefinitely in storyline. "
        "The mystery attack that left him in an ambulance on the August 27, 2026 iMPACT got its "
        "answer on September 24, when Joseph Sawyer and Samuel Shaw unmasked over the Hardys as "
        "syX. They beat the brothers in a Falls Count Anywhere match at Bound for Glory in Tampa "
        "on October 11, with Erick Redbeard interfering. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">6</span>'
        '<span class="pull-cap">world championships: one WWE, two World Heavyweight, three TNA</span></span>'
        "Then came the Slaughterhouse syX match on the October 29 iMPACT. It ended with Jeff "
        "struck with axes while wearing a trash can, and TNA&rsquo;s storyline injury report "
        "listed lacerations and head trauma. Matt goes on without him, teaming with Moose "
        "against syX at Destination X on November 15, 2026.",

        "One current-events correction, because it is often gotten wrong: <b>the Hardys are not "
        "the reigning TNA World Tag Team Champions</b>. They lost the titles to The System at "
        "Rebellion on April 11, 2026, won them back as the Broken Hardys in a four-way ladder "
        "match at Slammiversary in Boston on June 28, and lost them to Nic and Ryan Nemeth in a "
        "steel cage at Lockdown in Chicago on August 23. That was their fifth TNA tag reign, not "
        "their third. The full run: Ultimate X in 2015, the Great War at Bound for Glory 2016, "
        "Full Metal Mayhem at Bound for Glory 2024, Slammiversary 2025 and Slammiversary 2026. "
        "A rematch on the October 8 iMPACT ended when Nic Nemeth rolled Jeff up after a syX "
        "distraction. As of November 9, 2026, Jeff holds no title.",

        "The legend rests on ladders. With Matt, his real brother and his partner since their "
        "trampoline federation in Cameron, North Carolina, he changed what a televised stunt "
        "could be: the No Mercy 1999 ladder match against Edge and Christian, the first TLC at "
        "SummerSlam 2000, TLC II at WrestleMania X-Seven. Inside WWE the brothers hold nine "
        "main-roster tag reigns and one NXT reign, with ROH and five TNA reigns besides. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">2008</span>'
        '<span class="pull-cap">WWE Champion at Armageddon, the payoff to years of falling</span></span>'
        "As a singles act he was the underdog the audience adopted: the 2001 Intercontinental "
        "upset of Triple H, the 2002 ladder challenge to The Undertaker, and finally the WWE "
        "Championship at Armageddon on December 14, 2008. Two World Heavyweight Championship "
        "reigns followed in 2009, around the CM Punk feud, whose straight-edge-versus-"
        "recklessness subtext was barely subtext. In TNA he won three world championships and "
        "hit bottom at Victory Road 2011, where his match with Sting was stopped in about ninety "
        "seconds because he was in no condition to perform.",

        "The honest version of this page includes the record off the ladder too: the April 22, "
        "2003 WWE release, wellness-policy suspensions, the 2011 nadir, and the June 2022 DUI "
        "arrest that got him suspended by AEW and sent to rehab. He returned to AEW on April 12, "
        "2023, came home to TNA on June 14, 2024, and has been a reliable pay-per-view act with "
        "his brother since. The Swanton Bomb still comes off the top. At Bound for Glory 2026 it "
        "came off a balcony.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE", "TNA", "AEW"],
        promo_labels={"WWE": "WWE / WWF", "TNA": "TNA", "AEW": "AEW"},
        stats=[
            ("1&times;", "WWE Championship"),
            ("2&times;", "World Heavyweight"),
            ("3&times;", "TNA World title"),
            ("5&times;", "Intercontinental"),
            ("10",       "WWE tag reigns w/ Matt"),
            ("5",        "TNA tag reigns w/ Matt"),
        ],
        lead=("A ledger of documented bouts: the ladder and TLC canon, every world title change, "
              "all five Intercontinental wins, the Victory Road low point and the 2024&ndash;26 "
              "Hardys run through the syX storyline. It is a selection, not a career count. No "
              "career win&ndash;loss total is published because no verified one exists. Filter by "
              "match type, tap any column header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The bouts the reputation rests on. Star ratings are deliberately not "
                    "published: Observer figures were not verified, and this page does not guess "
                    "at numbers."),
    signature=[
        dict(rating="&mdash;", event="No Mercy 1999", opponent="Edge & Christian",
             stip="Ladder match, with Matt. The one that started the era"),
        dict(rating="&mdash;", event="WrestleMania X-Seven", opponent="Edge & Christian; The Dudley Boyz",
             stip="TLC II, the definitive multi-team ladder match"),
        dict(rating="&mdash;", event="Raw, July 1, 2002", opponent="The Undertaker",
             stip="Ladder match for the Undisputed title. Made as a singles star in defeat"),
        dict(rating="&mdash;", event="SummerSlam 2009", opponent="CM Punk",
             stip="TLC for the World Heavyweight Championship. The exit match"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("6",  "World titles"),
            ("15", "Tag reigns w/ Matt, WWE + TNA"),
            ("5&times;", "Intercontinental"),
            ("0",  "Held right now"),
        ],
        lead=("Six world championships, five Intercontinental reigns, and a tag record with Matt "
              "spread across WWE, NXT, ROH and TNA. Counts are as of November 9, 2026."),
        rows=[
            dict(ic="W", name="WWE Championship", count="1",
                 sub="Armageddon, December 14, 2008, in a triple threat over Edge and Triple H "
                     "&middot; lost to Edge at the Royal Rumble on January 25, 2009, after Matt "
                     "hit him with a chair"),
            dict(ic="H", name="World Heavyweight Championship", count="2",
                 sub="Extreme Rules, June 7, 2009, in a ladder match over Edge, lost minutes later "
                     "to CM Punk&rsquo;s Money in the Bank cash-in &middot; regained from Punk at "
                     "Night of Champions on July 26, lost the SummerSlam TLC on August 23"),
            dict(ic="T", name="TNA World Heavyweight Championship", count="3",
                 sub="Bound for Glory, October 10, 2010 (vacant-title three-way, the Immortal "
                     "turn), lost to Mr. Anderson January 9, 2011 &middot; Against All Odds, "
                     "February 13, 2011 (ladder over Anderson), lost to Sting February 24 &middot; "
                     "Bound for Glory, October 14, 2012, over Austin Aries, lost to Bully Ray at "
                     "Lockdown on March 10, 2013"),
            dict(ic="N", name="TNA World Tag Team Championship", count="5",
                 sub="With Matt: Ultimate X (taped March 16, 2015) &middot; the Great War at "
                     "Bound for Glory, October 2, 2016 &middot; Full Metal Mayhem at Bound for "
                     "Glory, October 26, 2024 &middot; Slammiversary ladder, July 20, 2025 "
                     "&middot; Slammiversary ladder as the Broken Hardys, June 28, 2026, lost to "
                     "the Nemeths in a Lockdown cage on August 23, 2026"),
            dict(ic="G", name="WWF/WWE tag championships, with Matt", count="9",
                 sub="Six WWF/World Tag Team reigns (first won July 5, 1999), one WCW Tag Team "
                     "reign (2001), the Raw Tag Team Championship from the WrestleMania 33 "
                     "ladder match on April 2, 2017, and the SmackDown Tag Team titles on April "
                     "9, 2019"),
            dict(ic="X", name="NXT Tag Team Championship", count="1",
                 sub="NXT vs. TNA Showdown, October 7, 2025, winners take all over DarkState "
                     "&middot; lost back to DarkState in a Broken Rules match at Halloween Havoc "
                     "on October 25. An 18-day, two-company double reign"),
            dict(ic="I", name="WWE Intercontinental Championship", count="5",
                 sub="Triple H (2001) &middot; Johnny Nitro, October 2 and November 13, 2006 "
                     "&middot; Umaga, September 3, 2007 &middot; AJ Styles, August 21, 2020"),
            dict(ic="U", name="WWE United States Championship", count="1",
                 sub="Beat Jinder Mahal on Raw, April 16, 2018, completing the modern Grand Slam "
                     "after he had already completed the original format"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Teams &amp; Factions",
        lead="One team above everything, and two detours that defined eras anyway.",
        cards=[
            dict(era="1990s&ndash;present",
                 name="The Hardys / The Hardy Boyz",
                 members="Jeff Hardy, Matt Hardy",
                 desc="Brothers from Cameron, North Carolina who grew a trampoline federation "
                      "into OMEGA and then took over the WWF tag division. Nine main-roster WWE "
                      "tag reigns, one in NXT, one in ROH and five in TNA. They won the TNA titles "
                      "for a fifth time as the Broken Hardys at Slammiversary 2026."),
            dict(era="TNA &middot; 2010&ndash;2011",
                 name="Immortal",
                 members="Hulk Hogan, Eric Bischoff, Jeff Hardy, Abyss, and others",
                 desc="The heel stable he joined by winning the vacant TNA World Heavyweight "
                      "Championship at Bound for Glory 2010. The run was cut short by the "
                      "personal collapse that produced Victory Road 2011."),
            dict(era="WWF &middot; 2000&ndash;2002",
                 name="Team Xtreme",
                 members="Matt Hardy, Jeff Hardy, Lita",
                 desc="The Hardys plus Lita. The trio made the team a mainstream youth act at the "
                      "Attitude Era&rsquo;s peak: cargo pants, face paint and top-rope "
                      "recklessness."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One man, several frequencies: <b>Jeff Hardy</b>, <b>Willow</b>, <b>Brother "
             "Nero</b>, and back again. The enigma part was never an act.",
        cards=[
            dict(mono="TX", era="WWF/WWE &middot; 1998&ndash;2003", name="Team Xtreme daredevil",
                 desc="The high-flyer of the Attitude Era tag division: the Swanton off anything, "
                      "the dancing entrance, the audience&rsquo;s adopted little brother."),
            dict(mono="CE", era="WWE &amp; TNA &middot; 2006&ndash;", name="The Charismatic Enigma",
                 desc="The singles identity: face paint, self-drawn imagery, his own music, an "
                      "underdog whose flaws were part of the bond with the crowd. Peaked with the "
                      "2008&ndash;09 world title run."),
            dict(mono="WI", era="OMEGA &amp; TNA &middot; 1990s, 2014", name="Willow",
                 desc="The masked alter ego from the OMEGA days, revived in TNA vignettes from "
                      "February 2014."),
            dict(mono="BN", era="TNA &middot; 2016&ndash;2017, 2026", name="Brother Nero",
                 desc="His role in Matt&rsquo;s Broken universe. The Final Deletion in July 2016 "
                      "and the Great War tag win that October set up the WrestleMania 33 return. "
                      "Brother Nero came back for the Slammiversary 2026 title win."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="A trampoline federation in Cameron to a storyline exit in Dothan, Alabama, "
             "thirty-two years after his first WWF match.",
        rows=[
            dict(year="1994", title="First WWF match",
                 desc="Faces Razor Ramon on May 23 in Youngstown, Ohio, at sixteen, after years "
                      "of trampoline and backyard matches with Matt."),
            dict(year="1999", title="The ladder era opens",
                 desc="The Hardy Boyz win their first WWF tag titles on July 5 and the No Mercy "
                      "ladder match over Edge and Christian on October 17."),
            dict(year="2001", title="Singles proof of concept",
                 desc="Upsets Triple H for the Intercontinental Championship on SmackDown (aired "
                      "April 12) while the TLC matches run on."),
            dict(year="2003", title="Released",
                 desc="WWE lets him go on April 22. The first public bottom."),
            dict(year="2008", title="WWE Champion",
                 desc="Wins the triple threat at Armageddon on December 14, the payoff to the "
                      "longest underdog chase of the era."),
            dict(year="2009", title="The Punk feud and the exit",
                 desc="Two World Heavyweight Championship reigns inside three months. Loses the "
                      "SummerSlam TLC to CM Punk on August 23 and leaves WWE days later."),
            dict(year="2010", title="TNA champion, heel, Immortal",
                 desc="Wins the vacant TNA World Heavyweight Championship at Bound for Glory on "
                      "October 10 and turns heel with Hogan and Bischoff."),
            dict(year="2011", title="Victory Road",
                 desc="The Sting match on March 13 is stopped in about ninety seconds because he "
                      "is unable to perform. He has since owned it in interviews."),
            dict(year="2012", title="The redemption reign",
                 desc="Beats Austin Aries at Bound for Glory on October 14 for his third TNA "
                      "world title."),
            dict(year="2017", title="The WrestleMania 33 return",
                 desc="The Hardys surprise-enter the Raw tag title ladder match on April 2 and "
                      "win."),
            dict(year="2018", title="Modern Grand Slam",
                 desc="Beats Jinder Mahal for the United States Championship on the April 16 Raw."),
            dict(year="2020", title="Fifth Intercontinental reign",
                 desc="Beats AJ Styles on the August 21 SmackDown."),
            dict(year="2022", title="AEW, arrest, rehab",
                 desc="Joins Matt in AEW in March. A June DUI arrest brings an indefinite "
                      "suspension and treatment. He returns on April 12, 2023."),
            dict(year="2024", title="Home to TNA",
                 desc="Returns alongside Matt at Against All Odds on June 14. They win the TNA "
                      "World Tag Team Championship in Full Metal Mayhem at Bound for Glory on "
                      "October 26."),
            dict(year="2025", title="Double champions at 48",
                 desc="Regain the TNA tag titles in the Slammiversary ladder match on July 20, "
                      "beat DarkState winners-take-all on October 7 to add the NXT titles, and "
                      "beat Team 3D in a tables match at Bound for Glory on October 12."),
            dict(year="2026", title="Fifth reign, then syX",
                 desc="Lose the titles to The System on April 11, regain them as the Broken "
                      "Hardys at Slammiversary on June 28, and lose them to the Nemeths in a "
                      "Lockdown cage on August 23. Attacked backstage on August 27. syX are "
                      "revealed on September 24, win at Bound for Glory on October 11, and write "
                      "Jeff out in the Slaughterhouse match on October 29."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Edge & Christian and The Dudley Boyz",
                 desc="The three-team rivalry behind No Mercy 1999, the first TLC at SummerSlam "
                      "2000 and TLC II at WrestleMania X-Seven on April 1, 2001. Every ladder "
                      "match since works in its shadow."),
            dict(name="CM Punk", slug="cm-punk",
                 desc="The 2009 feud that ended his WWE peak: straight-edge preacher against "
                      "flawed free spirit. Punk cashed in on him at Extreme Rules, lost the title "
                      "back at Night of Champions, then won the SummerSlam TLC and the cage match "
                      "that wrote Jeff out of the company."),
            dict(name="Edge", slug="edge",
                 desc="From TLC rival to the 2008&ndash;09 singles war. Edge took the WWE "
                      "Championship back at the 2009 Royal Rumble with Matt&rsquo;s help, then "
                      "lost the Extreme Rules ladder match that made Jeff World Heavyweight "
                      "Champion."),
            dict(name="Matt Hardy", slug="matt-hardy",
                 desc="Brother, partner, and the perfect enemy when the story needed one: "
                      "Vengeance 2001, the 2009 feud after the Royal Rumble betrayal, and the "
                      "2016 Final Deletion. In 2026 Matt carries on against syX without him."),
            dict(name="Sting", slug="sting",
                 desc="Linked by the worst night, Victory Road on March 13, 2011, after Sting had "
                      "taken the TNA title from him on February 24. The 2012 redemption reign "
                      "answered it."),
            dict(name="The Nemeths and syX",
                 desc="The 2025&ndash;26 TNA opponents. The Nemeths took the tag titles at "
                      "Rebellion 2025 and in the Lockdown 2026 cage. syX, Joseph Sawyer and "
                      "Samuel Shaw, beat the Hardys at Bound for Glory 2026 and in the October 29 "
                      "Slaughterhouse match."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Music",
        lead="The enigma part extends well past the ring.",
        rows=[
            dict(when="2003&ndash;", title="PeroxWhy?Gen", kind="Music",
                 desc="The band he formed in 2003. Albums include Plurality of Worlds (2013), "
                      "Within the Cygnus Rift (2015), Precession of the Equinoxes (2017) and The "
                      "Omega Sessions: II (2024)."),
            dict(when="2016&ndash;2017", title="The Broken Universe / Final Deletion", kind="Television",
                 desc="Matt&rsquo;s creation, with Jeff as Brother Nero. The cinematic matches at "
                      "the Hardy compound changed how wrestling television gets shot."),
            dict(when="1999&ndash;2026", title="Video games", kind="Game",
                 desc="Debuted in WWF WrestleMania 2000. Later in WWE 2K18 through 2K22, AEW "
                      "Fight Forever (2023) and the WWE 2K26 Season 4 pass."),
            dict(when="2009", title="Jeff Hardy: My Life, My Rules", kind="Video",
                 desc="WWE&rsquo;s December 2009 documentary on the first singles peak."),
            dict(when="2008", title="Twist of Fate: The Matt and Jeff Hardy Story", kind="Video",
                 desc="WWE&rsquo;s April 29, 2008 documentary on the brothers."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The marks, the milestones and the caveats, stated plainly.",
        stats=[
            ("6",  "World titles"),
            ("5",  "TNA tag reigns"),
            ("2",  "Companies' tag belts at once"),
        ],
        rows=[
            dict(name="Six world championships across WWE and TNA",
                 sub="The WWE Championship (Armageddon 2008), two World Heavyweight Championships "
                     "(2009), and three TNA World Heavyweight Championships (2010&ndash;2012)."),
            dict(name="Ten tag reigns with Matt inside WWE",
                 sub="Nine on the main roster, from July 5, 1999 through the SmackDown tag reign "
                     "of April 9, 2019, plus the 2025 NXT reign."),
            dict(name="Five TNA World Tag Team reigns with Matt",
                 sub="2015, 2016, 2024, 2025 and 2026. The fifth began as the Broken Hardys at "
                     "Slammiversary on June 28, 2026 and lasted 56 days."),
            dict(name="Triple Crown and Grand Slam Champion",
                 sub="WWE&rsquo;s 18th Triple Crown and 9th Grand Slam champion. The April 16, "
                     "2018 United States title win made him the second man to complete the "
                     "modern Grand Slam."),
            dict(name="NXT and TNA World Tag Team Champion at the same time, at 48",
                 sub="October 7&ndash;25, 2025, after the winners-take-all Showdown win over "
                     "DarkState."),
            dict(name="The comeback that keeps holding",
                 sub="Released in 2003, stopped ninety seconds into a title match in 2011, "
                     "suspended after a 2022 DUI arrest. Then a reliable TNA pay-per-view act from "
                     "2024 on. The falls are part of the record. So is standing back up."),
        ],
        footnote=("Deliberately absent: a career win-loss total, star ratings, an entrance theme, "
                  "and any claim that the Hardys hold tag gold. They lost the TNA titles to the "
                  "Nemeths at Lockdown on August 23, 2026."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Jeff_Hardy"),
        dict(k="Wikipedia", v="The Hardy Boyz", href="https://en.wikipedia.org/wiki/The_Hardy_Boyz"),
        dict(k="Wikipedia", v="Slammiversary 2026, the fifth TNA tag title win",
             href="https://en.wikipedia.org/wiki/Slammiversary_(2026)"),
        dict(k="Wrestling Inc", v="Lockdown 2026 results, the cage loss to the Nemeths",
             href="https://www.wrestlinginc.com/2242072/tna-lockdown-2026-five-titles-on-line-lethal-lockdown-match-more/"),
        dict(k="Wrestling Inc", v="syX unmasked on iMPACT, Sept 24, 2026",
             href="https://www.wrestlinginc.com/2268499/tna-impact-joseph-sawyer-samuel-shaw-joe-gacy-dexter-lumis-arrive/"),
        dict(k="Wrestling Inc", v="Bound for Glory 2026 results",
             href="https://www.wrestlinginc.com/2283301/tna-bound-for-glory-2026-results/"),
        dict(k="Wrestling Inc", v="The Slaughterhouse aftermath and Destination X",
             href="https://www.wrestlinginc.com/2308796/tna-destination-x-matt-hardy-moose-syx-team-against/"),
        dict(k="Fightful", v="syX vs. Matt Hardy &amp; Moose set for Destination X",
             href="https://www.fightful.com/?p=337679"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="What happened to Jeff Hardy in TNA in fall 2026?",
            a="He was written out in storyline. After a backstage attack on the August 27, 2026 "
              "iMPACT, syX (Joseph Sawyer and Samuel Shaw) were revealed as the attackers on "
              "September 24. They beat the Hardys in a Falls Count Anywhere match at Bound for "
              "Glory on October 11 with help from Erick Redbeard, then won a Slaughterhouse syX "
              "match on the October 29 iMPACT. TNA&rsquo;s storyline injury report said Jeff "
              "suffered lacerations and head trauma and is out indefinitely. It is an angle, not "
              "a reported legitimate injury.",
            q_ld="What happened to Jeff Hardy in TNA in fall 2026?",
            a_ld="Jeff Hardy was written out of TNA television in storyline. After a backstage "
                 "attack on the August 27, 2026 episode of iMPACT, Joseph Sawyer and Samuel Shaw, "
                 "known as syX, were revealed as the attackers on September 24, 2026. They beat "
                 "the Hardys in a Falls Count Anywhere match at Bound for Glory on October 11, "
                 "2026 and in a Slaughterhouse syX match on the October 29, 2026 iMPACT. TNA's "
                 "storyline injury report said Jeff suffered lacerations and head trauma and is "
                 "out indefinitely."),
        dict(
            q="Who are syX?",
            a="Joseph Sawyer and Samuel Shaw, formerly Joe Gacy and Dexter Lumis of WWE&rsquo;s "
              "Wyatt Sicks. They unmasked standing over the Hardys on the September 24, 2026 "
              "iMPACT after a run of backstage attacks, including the one on Jeff. Matt Hardy and "
              "Moose face them at Destination X on November 15, 2026.",
            q_ld="Who are syX in TNA?",
            a_ld="syX are Joseph Sawyer and Samuel Shaw, formerly known in WWE as Joe Gacy and "
                 "Dexter Lumis of the Wyatt Sicks. They were revealed as TNA's mystery attackers "
                 "on the September 24, 2026 episode of iMPACT, standing over Matt and Jeff Hardy. "
                 "Matt Hardy and Moose face them at TNA Destination X on November 15, 2026."),
        dict(
            q="Are The Hardys the current TNA World Tag Team Champions?",
            a="No. They won the titles for a fifth time as the Broken Hardys at Slammiversary in "
              "Boston on June 28, 2026, then lost them to Nic and Ryan Nemeth in a steel cage at "
              "Lockdown in Chicago on August 23, 2026. A rematch on the October 8 iMPACT also went "
              "to the Nemeths.",
            q_ld="Are The Hardys the current TNA World Tag Team Champions?",
            a_ld="No. The Hardys won the TNA World Tag Team Championship for the fifth time at "
                 "Slammiversary on June 28, 2026 in Boston and lost it to Nic and Ryan Nemeth in a "
                 "steel cage match at Lockdown on August 23, 2026 in Chicago. The Nemeths also "
                 "won the rematch on the October 8, 2026 episode of iMPACT."),
        dict(
            q="How many times have the Hardys won the TNA World Tag Team Championship?",
            a="Five: Ultimate X for the vacant title (taped March 16, 2015), the Great War at "
              "Bound for Glory on October 2, 2016, Full Metal Mayhem at Bound for Glory on "
              "October 26, 2024, the Slammiversary ladder match on July 20, 2025, and the "
              "Slammiversary ladder match on June 28, 2026.",
            q_ld="How many times have Matt and Jeff Hardy won the TNA World Tag Team Championship?",
            a_ld="Five times: in an Ultimate X match taped March 16, 2015, at Bound for Glory on "
                 "October 2, 2016, at Bound for Glory on October 26, 2024, at Slammiversary on "
                 "July 20, 2025, and at Slammiversary on June 28, 2026."),
        dict(
            q="How many world titles has Jeff Hardy won?",
            a="Six: the WWE Championship (Armageddon, December 14, 2008), two World Heavyweight "
              "Championships (both in 2009, the first in the Extreme Rules ladder match against "
              "Edge), and three TNA World Heavyweight Championships (2010, 2011, and the Bound for "
              "Glory 2012 win over Austin Aries). He also holds five Intercontinental reigns and "
              "is a Triple Crown and Grand Slam champion.",
            q_ld="How many world championships has Jeff Hardy won?",
            a_ld="Jeff Hardy has won six world championships: one WWE Championship in 2008, two "
                 "World Heavyweight Championships in 2009, and three TNA World Heavyweight "
                 "Championships between 2010 and 2012. He has also held the Intercontinental "
                 "Championship five times and is a WWE Triple Crown and Grand Slam champion."),
        dict(
            q="Is Jeff Hardy a Grand Slam champion?",
            a="Yes, in both formats. Wikipedia lists him as WWE&rsquo;s 18th Triple Crown and 9th "
              "Grand Slam champion. His United States Championship win over Jinder Mahal on the "
              "April 16, 2018 Raw made him the second man to complete the modern Grand Slam.",
            q_ld="Is Jeff Hardy a WWE Grand Slam champion?",
            a_ld="Yes. Jeff Hardy is WWE's 18th Triple Crown Champion and 9th Grand Slam Champion. "
                 "His United States Championship win over Jinder Mahal on Raw on April 16, 2018 "
                 "made him the second person to complete the modern Grand Slam format, after he "
                 "had completed the original format separately."),
        dict(
            q="What was Victory Road 2011?",
            a="The lowest public moment of his career: a TNA World Heavyweight Championship match "
              "against Sting on March 13, 2011 that was stopped in about ninety seconds because "
              "Hardy was in no condition to perform. He has since discussed the night openly. The "
              "answer to it was the October 14, 2012 Bound for Glory title win over Austin Aries.",
            q_ld="What happened at TNA Victory Road 2011 with Jeff Hardy?",
            a_ld="At TNA Victory Road on March 13, 2011, Jeff Hardy's world championship match "
                 "against Sting was stopped after about ninety seconds because Hardy was in no "
                 "condition to perform. Hardy has spoken openly about the night. His Bound for "
                 "Glory title win over Austin Aries on October 14, 2012 is regarded as the "
                 "completion of his comeback."),
        dict(
            q="When did Jeff Hardy debut?",
            a="His first WWF match was against Razor Ramon on May 23, 1994 in Youngstown, Ohio. "
              "He was sixteen. Before that he and Matt wrestled in their own trampoline "
              "federation, which later became OMEGA. He was trained by Dory Funk Jr. and Michael "
              "Hayes.",
            q_ld="When did Jeff Hardy make his wrestling debut?",
            a_ld="Jeff Hardy's first WWF match was against Razor Ramon on May 23, 1994 in "
                 "Youngstown, Ohio, when he was 16. He and his brother Matt had earlier wrestled "
                 "in their own trampoline federation, which became OMEGA. He was trained by Dory "
                 "Funk Jr. and Michael Hayes."),
        dict(
            q="Is Jeff Hardy still wrestling in 2026?",
            a="He is on the TNA roster but out of action in storyline. He turned 49 on August 31, "
              "2026. The Hardys won the TNA tag titles in June and lost them in August, and the "
              "October 29 Slaughterhouse match against syX wrote him out indefinitely. Matt "
              "continues the feud with Moose at Destination X on November 15.",
            q_ld="Is Jeff Hardy still an active wrestler in 2026?",
            a_ld="Jeff Hardy, aged 49, is on the TNA roster as of November 2026 but is out "
                 "indefinitely in storyline after the October 29, 2026 Slaughterhouse match "
                 "against syX. Earlier in 2026 he and Matt won and lost the TNA World Tag Team "
                 "Championship for the fifth time."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Jeffrey Nero Hardy"),
        dict(label="Born", value="August 31, 1977", sub="Cameron, North Carolina &middot; age 49"),
        dict(label="Billed from", value="Cameron, North Carolina"),
        dict(label="Height", value="6&#8242;1&#8243;", sub="185 cm (billed)"),
        dict(label="Weight", value="225 lb", sub="102 kg (billed)"),
        dict(label="Debut", value="May 23, 1994",
             sub="WWF, against Razor Ramon in Youngstown, Ohio, at sixteen"),
        dict(label="Trained by", value="Dory Funk Jr. &middot; Michael Hayes"),
        dict(label="Signature", value="Swanton Bomb &middot; Twist of Fate &middot; Whisper in "
                                      "the Wind &middot; Poetry in Motion"),
        dict(label="Brand", value="TNA", sub="with Matt as The Hardys; returned June 14, 2024 at "
                                             "Against All Odds"),
        dict(label="Also known as", value="The Charismatic Enigma &middot; Brother Nero &middot; "
                                          "Willow"),
        dict(label="Family", value="Brother of Matt Hardy"),
        dict(label="Status", value="Active, out injured in storyline",
             sub="since the October 29, 2026 Slaughterhouse match; no championship held"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1977-08-31",
    bornplace="Cameron, North Carolina, United States",
    nationality="United States",
    height_cm=185,
    weight_kg=102,
    ld=dict(
        alternateName=["Jeffrey Nero Hardy", "The Charismatic Enigma", "Brother Nero", "Willow"],
        award=["WWE Championship (1 reign, 2008)",
               "World Heavyweight Championship (2 reigns, 2009)",
               "TNA World Heavyweight Championship (3 reigns)",
               "WWE Intercontinental Championship (5 reigns)",
               "WWE United States Championship (1 reign)",
               "WWE European Championship (1 reign)",
               "WWF/WWE Hardcore Championship (3 reigns)",
               "WWF Light Heavyweight Championship (1 reign)",
               "WWF/WWE tag team championships (9 reigns, with Matt Hardy)",
               "NXT Tag Team Championship (1 reign, with Matt Hardy)",
               "ROH World Tag Team Championship (1 reign, with Matt Hardy)",
               "TNA World Tag Team Championship (5 reigns, with Matt Hardy)",
               "WWE Triple Crown Champion",
               "WWE Grand Slam Champion"],
        knowsAbout=["Professional wrestling", "Ladder matches", "TLC matches", "WWE", "TNA",
                    "AEW", "The Hardy Boyz", "OMEGA promotion", "Music"],
        description="Jeff Hardy, born Jeffrey Nero Hardy in Cameron, North Carolina, is an "
                    "American professional wrestler on the TNA roster. One half of The Hardys "
                    "with his brother Matt, he helped define the ladder and TLC match era, won "
                    "six world championships across WWE and TNA, and is a WWE Triple Crown and "
                    "Grand Slam champion. The Hardys won the TNA World Tag Team Championship for "
                    "the fifth time in June 2026 and lost it in August 2026. In October 2026 he "
                    "was written out of TNA television in storyline after losses to syX.",
        sameAs=["https://en.wikipedia.org/wiki/Jeff_Hardy",
                "https://tnawrestling.com/"],
    ),
)
