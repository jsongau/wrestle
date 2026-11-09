# -*- coding: utf-8 -*-
"""Matt Hardy - dossier data.

Built FROM data/matt-hardy.md (compiled November 9, 2026). Every fact below
traces to a source listed in that file: Wikipedia's Matt Hardy, Hardy Boyz and
title-history pages, the WWE event pages, Fightful, Wrestling Inc and PWTorch
reports for 2024-2026, and TNA's roster page.

Status, verified for November 9, 2026: ACTIVE in TNA, not a champion. The
Nemeths have held the TNA World Tag Team Championship since Lockdown on
August 23, 2026. Jeff Hardy is out in storyline after the October 29, 2026
Slaughterhouse syX match, and Matt teams with Moose against syX at Destination
X on November 15, 2026.

Harvest notes: the old page (~861 words) carried several errors that are NOT
repeated here. It placed the ECW title win at "No Mercy 2008 vs John Cena"
(it was the Unforgiven 2008 Championship Scramble), dated the first TLC to
"SummerSlam 1999" (it was SummerSlam 2000), called Final Deletion a Slammiversary
ladder match (it was a July 5, 2016 Impact special), and listed a 4-1 record
and finish-method percentages that no source supports.

Deliberate omissions:
  * No career win-loss total. Cagematch is JS-gated and no verified total exists.
  * No star ratings on the signature cards. No Observer figure was verified.
  * No walk-out theme band. No current entrance theme or Spotify id was verified.
  * No Right Now (pulse) section. No verified social posts were collected.
  * The Hardcore Championship win (April 24, 2000) has no row: the opponent
    was not verified.
"""

_LINK = {"Jeff Hardy": "jeff-hardy", "Edge": "edge", "Rey Mysterio": "rey-mysterio",
         "Kane": "kane"}

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="1999-07-05", promo="WWE", landmark=True, type="tag",
         event="Raw Is War", opponent="The Acolytes",
         stip="Tag, with Jeff. Their first WWF tag title", title="WWF Tag Team Championship"),
    dict(result="W", date="1999-10-17", promo="WWE", landmark=True, type="tag",
         event="No Mercy", opponent="Edge & Christian",
         stip="Ladder match, the Terri Invitational. The first tag team ladder match", title=""),
    dict(result="L", date="2000-04-02", promo="WWE", landmark=True, type="tag",
         event="WrestleMania 2000", opponent="Edge & Christian; The Dudley Boyz",
         stip="Triangle ladder match", title="WWF Tag Team Championship"),
    dict(result="L", date="2000-08-27", promo="WWE", landmark=True, type="tag",
         event="SummerSlam", opponent="Edge & Christian; The Dudley Boyz",
         stip="The first TLC match", title="WWF Tag Team Championship"),
    dict(result="W", date="2000-09-24", promo="WWE", type="tag",
         event="Unforgiven", opponent="Edge & Christian",
         stip="Steel cage match, with Jeff", title="WWF Tag Team Championship"),
    dict(result="L", date="2001-04-01", promo="WWE", landmark=True, type="tag",
         event="WrestleMania X-Seven", opponent="Edge & Christian; The Dudley Boyz",
         stip="TLC II", title="WWF Tag Team Championship"),
    dict(result="W", date="2001-04-24", promo="WWE",
         event="SmackDown (aired April 26)", opponent="Eddie Guerrero",
         stip="Singles. His first singles title", title="WWF European Championship"),
    dict(result="W", date="2001-10-08", promo="WWE", type="tag",
         event="Raw", opponent="Booker T & Test",
         stip="Tag, with Jeff, during the Invasion", title="WCW Tag Team Championship"),
    dict(result="W", date="2001-11-12", promo="WWE", type="tag",
         event="Raw", opponent="Booker T & Test",
         stip="Tag, with Jeff. Fifth World Tag reign", title="WWF Tag Team Championship"),
    dict(result="L", date="2001-11-18", promo="WWE", type="tag",
         event="Survivor Series", opponent="The Dudley Boyz",
         stip="Steel cage unification match", title="WWF Tag Team Championship"),
    dict(result="L", date="2001-12-09", promo="WWE",
         event="Vengeance", opponent="Jeff Hardy", opponent_html=True,
         stip="Brother vs. brother, Lita as special referee", title=""),
    dict(result="L", date="2002-03-17", promo="WWE", type="tag",
         event="WrestleMania X8", opponent="Billy & Chuck; The APA; The Dudley Boyz",
         stip="Four corners elimination match", title="WWF Tag Team Championship"),
    dict(result="W", date="2003-02-23", promo="WWE", landmark=True,
         event="No Way Out", opponent="Billy Kidman",
         stip="Singles. Version 1 cuts weight and wins gold", title="WWE Cruiserweight Championship"),
    dict(result="W", date="2003-03-30", promo="WWE", landmark=True,
         event="WrestleMania XIX", opponent="Rey Mysterio", opponent_html=True,
         stip="Singles, title defense", title="WWE Cruiserweight Championship"),
    dict(result="L", date="2003-06-05", promo="WWE",
         event="SmackDown", opponent="Rey Mysterio", opponent_html=True,
         stip="Singles, main event", title="WWE Cruiserweight Championship"),
    dict(result="L", date="2004-08-15", promo="WWE",
         event="SummerSlam", opponent="Kane", opponent_html=True,
         stip="Till Death Do Us Part. The loss forced Lita to marry Kane", title=""),
    dict(result="L", date="2005-08-21", promo="WWE", landmark=True,
         event="SummerSlam", opponent="Edge", opponent_html=True,
         stip="Singles, stopped by the referee after Matt bled heavily", title=""),
    dict(result="W", date="2005-09-18", promo="WWE",
         event="Unforgiven", opponent="Edge", opponent_html=True,
         stip="Steel cage, won with a leg drop off the top of the cage", title=""),
    dict(result="L", date="2005-10-03", promo="WWE", landmark=True,
         event="Raw Homecoming", opponent="Edge", opponent_html=True,
         stip="Loser Leaves Raw ladder match", title=""),
    dict(result="L", date="2006-04-02", promo="WWE", type="tag",
         event="WrestleMania 22", opponent="Money in the Bank field",
         stip="Money in the Bank ladder match, won by Rob Van Dam", title=""),
    dict(result="L", date="2007-04-01", promo="WWE", type="tag",
         event="WrestleMania 23", opponent="Money in the Bank field",
         stip="Money in the Bank ladder match, won by Mr. Kennedy", title=""),
    dict(result="W", date="2007-04-02", promo="WWE", type="tag",
         event="Raw", opponent="Ten-team battle royal",
         stip="With Jeff. Sixth World Tag reign", title="World Tag Team Championship"),
    dict(result="W", date="2007-08-31", promo="WWE", type="tag",
         event="SmackDown (taped August 28)", opponent="Deuce 'n Domino",
         stip="Tag, with rival MVP", title="WWE Tag Team Championship"),
    dict(result="W", date="2008-04-27", promo="WWE", landmark=True,
         event="Backlash", opponent="MVP",
         stip="Singles, opening match", title="WWE United States Championship"),
    dict(result="W", date="2008-09-07", promo="WWE", landmark=True, type="tag",
         event="Unforgiven", opponent="Mark Henry, The Miz, Chavo Guerrero, Finlay",
         stip="Championship Scramble. Ahead when the 20-minute limit expired",
         title="ECW Championship"),
    dict(result="L", date="2009-01-13", promo="WWE",
         event="ECW (taped January 12)", opponent="Jack Swagger",
         stip="Singles", title="ECW Championship"),
    dict(result="W", date="2009-04-05", promo="WWE", landmark=True,
         event="WrestleMania 25", opponent="Jeff Hardy", opponent_html=True,
         stip="Extreme Rules match, after the Royal Rumble chair betrayal", title=""),
    dict(result="L", date="2009-04-26", promo="WWE",
         event="Backlash", opponent="Jeff Hardy", opponent_html=True,
         stip="I Quit match. Matt broke his hand for real", title=""),
    dict(result="L", date="2010-03-28", promo="WWE", type="tag",
         event="WrestleMania XXVI", opponent="Money in the Bank field",
         stip="Money in the Bank ladder match, won by Jack Swagger", title=""),
    dict(result="W", date="2015-03-16", promo="TNA", type="tag",
         event="Impact (aired April 17)", opponent="Aries & Roode; King & Low Ki; EC3 & Bram",
         stip="Ultimate X for the vacant title, with Jeff", title="TNA World Tag Team Championship"),
    dict(result="W", date="2015-10-04", promo="TNA", landmark=True, type="tag",
         event="Bound for Glory", opponent="Ethan Carter III; Drew Galloway",
         stip="Three-way, Jeff as guest referee. First world title",
         title="TNA World Heavyweight Championship"),
    dict(result="W", date="2016-01-08", promo="TNA",
         event="Impact (aired January 19)", opponent="Ethan Carter III",
         stip="Last man standing. Matt would have left TNA with a loss",
         title="TNA World Heavyweight Championship"),
    dict(result="L", date="2016-03-15", promo="TNA",
         event="Impact", opponent="Drew Galloway",
         stip="Galloway's Feast or Fired title win", title="TNA World Heavyweight Championship"),
    dict(result="W", date="2016-07-05", promo="TNA", landmark=True,
         event="Impact: The Final Deletion", opponent="Jeff Hardy", opponent_html=True,
         stip="Cinematic match at the Hardy compound for the Hardy brand", title=""),
    dict(result="W", date="2016-10-02", promo="TNA", landmark=True, type="tag",
         event="Bound for Glory", opponent="Decay",
         stip="The Great War, as the Broken Hardys", title="TNA World Tag Team Championship"),
    dict(result="W", date="2017-03-04", promo="ROH", type="tag",
         event="Manhattan Mayhem VI", opponent="The Young Bucks",
         stip="Tag, with Jeff", title="ROH World Tag Team Championship"),
    dict(result="L", date="2017-04-01", promo="ROH", type="tag",
         event="Supercard of Honor XI", opponent="The Young Bucks",
         stip="Ladder match, the night before WrestleMania", title="ROH World Tag Team Championship"),
    dict(result="W", date="2017-04-02", promo="WWE", landmark=True, type="tag",
         event="WrestleMania 33", opponent="Gallows & Anderson; Cesaro & Sheamus; Enzo & Cass",
         stip="Fatal four-way ladder match. The surprise return", title="Raw Tag Team Championship"),
    dict(result="L", date="2017-06-04", promo="WWE", type="tag",
         event="Extreme Rules", opponent="Cesaro & Sheamus",
         stip="Steel cage, escape rules", title="Raw Tag Team Championship"),
    dict(result="W", date="2018-03-19", promo="WWE", landmark=True,
         event="Raw: The Ultimate Deletion", opponent="Bray Wyatt",
         stip="Cinematic match as Woken Matt Hardy", title=""),
    dict(result="W", date="2018-04-08", promo="WWE", type="tag",
         event="WrestleMania 34 Kickoff", opponent="30-man field",
         stip="Andre the Giant Memorial Battle Royal, with Bray Wyatt's help", title=""),
    dict(result="W", date="2018-04-27", promo="WWE", type="tag",
         event="Greatest Royal Rumble", opponent="Cesaro & Sheamus",
         stip="Tag, with Bray Wyatt, for the vacant title", title="Raw Tag Team Championship"),
    dict(result="L", date="2018-07-15", promo="WWE", type="tag",
         event="Extreme Rules", opponent="The B-Team",
         stip="Tag, with Bray Wyatt", title="Raw Tag Team Championship"),
    dict(result="W", date="2019-04-09", promo="WWE", type="tag",
         event="SmackDown", opponent="The Usos",
         stip="Tag, with Jeff", title="SmackDown Tag Team Championship"),
    dict(result="W", date="2020-05-23", promo="AEW", landmark=True, type="tag",
         event="Double or Nothing", opponent="The Inner Circle",
         stip="Stadium Stampede, with The Elite", title=""),
    dict(result="W", date="2020-09-05", promo="AEW",
         event="All Out", opponent="Sammy Guevara",
         stip="Broken Rules match. Matt was hospitalized after, then cleared", title=""),
    dict(result="W", date="2022-05-29", promo="AEW", type="tag",
         event="Double or Nothing", opponent="The Young Bucks",
         stip="Tag, with Jeff, back together in AEW", title=""),
    dict(result="L", date="2024-06-14", promo="TNA",
         event="Against All Odds", opponent="Moose",
         stip="Broken Rules match. Jeff returned after it", title=""),
    dict(result="W", date="2024-10-26", promo="TNA", landmark=True, type="tag",
         event="Bound for Glory", opponent="The System; ABC",
         stip="Full Metal Mayhem, with Jeff", title="TNA World Tag Team Championship"),
    dict(result="L", date="2025-04-27", promo="TNA", type="tag",
         event="Rebellion", opponent="The Nemeths",
         stip="Tag, with Jeff. The 183-day reign ends", title="TNA World Tag Team Championship"),
    dict(result="W", date="2025-07-20", promo="TNA", type="tag",
         event="Slammiversary", opponent="The Nemeths; The Rascalz; Fir$t Cla$$",
         stip="Four-way ladder match, with Jeff", title="TNA World Tag Team Championship"),
    dict(result="W", date="2025-10-07", promo="WWE", landmark=True, type="tag",
         event="NXT vs. TNA Showdown", opponent="DarkState",
         stip="Winners take all, with Jeff", title="NXT Tag Team Championship"),
    dict(result="W", date="2025-10-12", promo="TNA", landmark=True, type="tag",
         event="Bound for Glory", opponent="Team 3D",
         stip="Tables match, Team 3D's retirement match", title="TNA World Tag Team Championship"),
    dict(result="L", date="2025-10-25", promo="WWE", type="tag",
         event="NXT Halloween Havoc", opponent="DarkState",
         stip="Broken Rules match, with Jeff", title="NXT Tag Team Championship"),
    dict(result="L", date="2026-04-11", promo="TNA", type="tag",
         event="Rebellion", opponent="The System",
         stip="Tag, with Jeff. The 265-day reign ends", title="TNA World Tag Team Championship"),
    dict(result="W", date="2026-06-28", promo="TNA", landmark=True, type="tag",
         event="Slammiversary", opponent="The System; The Righteous; The Great Hands",
         stip="Four-way ladder match, as the Broken Hardys. Fifth TNA tag reign",
         title="TNA World Tag Team Championship"),
    dict(result="L", date="2026-08-23", promo="TNA", type="tag",
         event="Lockdown", opponent="The Nemeths",
         stip="Steel cage tag match, with Jeff", title="TNA World Tag Team Championship"),
    dict(result="L", date="2026-09-10", promo="TNA", landmark=True,
         event="iMPACT", opponent="Nic Nemeth",
         stip="No DQ, main event. Nemeth won with a low blow and a wrench shot",
         title="TNA World Championship"),
    dict(result="L", date="2026-10-08", promo="TNA", type="tag",
         event="iMPACT", opponent="The Nemeths",
         stip="Title rematch, lost after a syX distraction", title="TNA World Tag Team Championship"),
    dict(result="L", date="2026-10-11", promo="TNA", type="tag",
         event="Bound for Glory", opponent="syX",
         stip="Falls Count Anywhere, with Jeff. Erick Redbeard interfered", title=""),
    dict(result="L", date="2026-10-29", promo="TNA", type="tag",
         event="iMPACT", opponent="syX",
         stip="Slaughterhouse syX match, with Jeff. Jeff written out injured", title=""),
]

# opponent_html rows carry a real <a>, so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (
            _LINK[_r["opponent"]], _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="matt-hardy",
    art="matt-hardy",
    name="Matt Hardy",
    realname="Matthew Moore Hardy",
    epithet="The Broken One",
    hook="Record & Titles",

    meta_desc=("Matt Hardy is active in TNA at 52. Twelve WWE tag reigns, five TNA tag reigns, "
               "two TNA world titles, the ECW title, Version 1 and Broken Matt Hardy. Full "
               "record, titles and career, verified November 2026."),
    og_desc=("The Broken One: the TLC era with Jeff, Version 1, the ECW Championship, the Final "
             "Deletion and an AEW run. In November 2026 he is still wrestling for TNA."),
    tw_desc="Matt Hardy: 12 WWE tag reigns, 5 TNA tag reigns, still active in TNA at 52.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1992",
    height_imp="6&#8242;2&#8243;",
    weight_lb="236",
    vitals_tagline="Delete",
    support_note="Watch &middot; Read &middot; Play",
    x_url="https://x.com/matthardybrand",
    ig_url="https://www.instagram.com/matthardybrand",
    sp_items=[
        dict(ic="TNA", title="TNA Wrestling", sub="Official roster page",
             tag="Visit", href="https://tnawrestling.com/roster/matt-hardy"),
        dict(ic="PWT", title="Pro Wrestling Tees", sub="Independent merch marketplace",
             tag="Shop", href="https://www.prowrestlingtees.com/"),
        dict(ic="2K", title="WWE 2K26", sub="Ringside Pass Season 4",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="W", title="Wikipedia", sub="Full biography", tag="Read", charity=True,
             href="https://en.wikipedia.org/wiki/Matt_Hardy"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Broken Matt &middot; Version 1 &middot; Big Money Matt &middot; one half of The Hardys",
    hero_tag="Cameron, North Carolina &middot; <em>OMEGA &middot; WWE &middot; TNA &middot; ROH "
             "&middot; AEW &middot; TNA again &middot; 1992&ndash;present</em>",
    now_label="NOW",
    now_bold="Active in TNA, out for revenge on syX",
    now_tail=(" &middot; teams with Moose against syX at Destination X on November 15, 2026, with "
              "Jeff written out injured after the October 29 Slaughterhouse match &middot; not a "
              "champion: the Nemeths took the TNA tag titles at Lockdown on August 23, 2026"),
    hstats=[
        dict(value="2",  x=False, label="TNA World Heavyweight Reigns"),
        dict(value="12", x=False, label="WWE Tag Title Reigns"),
        dict(value="5",  x=False, label="TNA Tag Title Reigns"),
        dict(value="52", x=False, label="Years Old, Still Active"),
    ],
    ghost_link="From a Cameron backyard promotion to the Final Deletion and back",
    vlabel="Est. 1992 &middot; Cameron, North Carolina",
    mono="MH",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Matt Hardy</b> is 52, under contract to TNA, and still in a weekly storyline. On "
        "the October 29, 2026 iMPACT, syX beat the Hardys in a Slaughterhouse syX match and "
        "left Jeff written out with storyline head trauma. Matt answered by teaming with Moose, "
        "one of syX&rsquo;s earlier victims, for a match at Destination X on November 15. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">34</span>'
        '<span class="pull-cap">years since his first match on October 15, 1992</span></span>'
        "He started before the internet era and outlasted most of it. He booked his own "
        "backyard shows as a teenager, built a character out of online fandom, and turned a "
        "rural compound into a television set.",

        "A correction, because it is often out of date: <b>the Hardys are not the current TNA "
        "World Tag Team Champions</b>. Their fifth TNA reign began at Slammiversary in Boston on "
        "June 28, 2026, in a four-way ladder match, and ended 56 days later. The Nemeths won "
        "the steel cage match at Lockdown in Chicago on August 23, 2026, and beat the Hardys "
        "again in an October 8 rematch. In between, on September 10, Matt challenged Nic Nemeth "
        "for the TNA World Championship in a No DQ main event and lost to a wrench shot. As of "
        "November 9, 2026, Matt holds no title.",

        "The foundation is the tag team. Matt and Jeff ran their own promotion, OMEGA, in "
        "Cameron, North Carolina, then won the first tag team ladder match at No Mercy in 1999 "
        "and fought the TLC trilogy with Edge and Christian and the Dudley Boyz. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">12</span>'
        '<span class="pull-cap">WWE tag title reigns, six of them in the original World Tag lineage</span></span>'
        "Matt has twelve WWE tag reigns, five TNA tag reigns, one ROH tag reign and one NXT tag "
        "reign. All but two came with Jeff. The exceptions were a WWE Tag reign with MVP in 2007 "
        "and a Raw Tag reign with Bray Wyatt in 2018.",

        "On his own he kept reinventing. Version 1 in 2002 made him a smug heel with Mattitude "
        "and a follower in Shannon Moore, and it won him the Cruiserweight title. After WWE "
        "released him in 2005 during the Edge and Lita affair, the fan reaction brought him back "
        "for a real-life feud on television. He won the United States title in April 2008 and "
        "the ECW title that September. In TNA in 2016 he created Broken Matt Hardy, and the "
        "Final Deletion on July 5 changed how wrestling shoots cinematic matches. "
        '<span class="pull pull--q" aria-hidden="true"><span class="pull-quote">Delete. The catchphrase that defined Broken Matt Hardy.</span></span>'
        "He took the same character to WrestleMania 33, Raw, AEW and back to TNA in 2024.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE", "TNA", "ROH", "AEW"],
        promo_labels={"WWE": "WWE / WWF", "TNA": "TNA", "ROH": "ROH", "AEW": "AEW"},
        stats=[
            ("12",       "WWE tag reigns"),
            ("5",        "TNA tag reigns"),
            ("2&times;", "TNA World Heavyweight"),
            ("1&times;", "ECW Championship"),
            ("1&times;", "United States"),
            ("10",       "WrestleMania appearances"),
        ],
        lead=("Sixty-one documented bouts: every WrestleMania appearance, the ladder and TLC "
              "matches, the title changes and the 2026 TNA run. This is a selected ledger, not "
              "a career count, and no win&ndash;loss total is given because no verified one "
              "exists. Taped television is dated by the taping, with the air date in the event "
              "name. Filter by match type, sort any column, and turn spoilers on to see results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches his reputation rests on. Star ratings are left off on purpose: "
                    "no Observer figure was verified for this page."),
    signature=[
        dict(rating="&mdash;", event="No Mercy 1999", opponent="Edge & Christian",
             stip="The Terri Invitational, the first tag team ladder match"),
        dict(rating="&mdash;", event="SummerSlam 2000", opponent="Edge & Christian; The Dudley Boyz",
             stip="The first TLC match"),
        dict(rating="&mdash;", event="WrestleMania X-Seven", opponent="Edge & Christian; The Dudley Boyz",
             stip="TLC II", url="/matches/tlc-2-wrestlemania-x-seven-2001/"),
        dict(rating="&mdash;", event="Impact, July 5, 2016", opponent="Brother Nero (Jeff Hardy)",
             stip="The Final Deletion at the Hardy compound"),
        dict(rating="&mdash;", event="WrestleMania 33", opponent="Gallows & Anderson; Cesaro & Sheamus; Enzo & Cass",
             stip="The surprise return, Raw Tag titles in a ladder match"),
    ],
    signature_count_word="five",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("12", "WWE tag reigns"),
            ("5",  "TNA tag reigns"),
            ("2",  "TNA world titles"),
            ("0",  "Held right now"),
        ],
        lead=("Gold in WWE, TNA, ROH and NXT across four decades. He never won a title in AEW. "
              "Counts follow the Wikipedia title histories as of November 2026."),
        rows=[
            dict(ic="G", name="WWF / World Tag Team Championship, with Jeff", count="6",
                 sub="First won July 5, 1999 on Raw over The Acolytes &middot; the Unforgiven 2000 "
                     "cage win over Edge &amp; Christian &middot; the sixth on April 2, 2007, from a "
                     "ten-team battle royal"),
            dict(ic="R", name="WWE Tag Team / Raw Tag Team Championship", count="3",
                 sub="With MVP from August 31, 2007 &middot; with Jeff at WrestleMania 33 on April "
                     "2, 2017 &middot; with Bray Wyatt at the Greatest Royal Rumble on April 27, 2018"),
            dict(ic="S", name="SmackDown, WCW and NXT tag titles, with Jeff", count="3",
                 sub="WCW Tag on October 8, 2001 &middot; SmackDown Tag on April 9, 2019 over The "
                     "Usos &middot; NXT Tag on October 7, 2025 over DarkState, lost October 25"),
            dict(ic="N", name="TNA World Tag Team Championship, with Jeff", count="5",
                 sub="Ultimate X in 2015 &middot; the Great War at Bound for Glory 2016 &middot; Full "
                     "Metal Mayhem at Bound for Glory 2024 &middot; Slammiversary 2025 &middot; "
                     "Slammiversary 2026, lost to the Nemeths at Lockdown on August 23, 2026"),
            dict(ic="T", name="TNA World Heavyweight Championship", count="2",
                 sub="Bound for Glory, October 4, 2015, vacated two days later in the storyline "
                     "injunction &middot; won back from Ethan Carter III in a last man standing "
                     "match taped January 8, 2016, lost to Drew Galloway on March 15"),
            dict(ic="E", name="ECW Championship", count="1",
                 sub="Unforgiven, September 7, 2008, in the Championship Scramble &middot; lost to "
                     "Jack Swagger on January 13, 2009 &middot; WWE&rsquo;s 2006&ndash;2010 ECW "
                     "title, not the original ECW world title"),
            dict(ic="U", name="WWE United States Championship", count="1",
                 sub="Backlash, April 27, 2008, over MVP &middot; lost to Shelton Benjamin at The "
                     "Great American Bash on July 20, 2008"),
            dict(ic="C", name="Cruiserweight, European and Hardcore", count="3",
                 sub="Cruiserweight from Billy Kidman at No Way Out 2003 &middot; European from "
                     "Eddie Guerrero in April 2001 &middot; Hardcore for three days in April 2000"),
            dict(ic="O", name="ROH World Tag Team Championship, with Jeff", count="1",
                 sub="Manhattan Mayhem VI, March 4, 2017, over The Young Bucks &middot; lost back to "
                     "them in a ladder match at Supercard of Honor XI on April 1"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Teams &amp; Factions",
        lead="One team above everything, and the groups he led on his own.",
        cards=[
            dict(era="1997&ndash;present",
                 name="The Hardy Boyz / The Hardys",
                 members="Matt Hardy, Jeff Hardy",
                 desc="Brothers from Cameron who founded OMEGA in 1997, signed full time with the "
                      "WWF in 1998 and won tag gold in WWE, TNA, ROH and NXT. Their 2024-26 TNA run "
                      "produced three more TNA tag reigns."),
            dict(era="WWF &middot; 2000&ndash;2002",
                 name="Team Xtreme",
                 members="Matt Hardy, Jeff Hardy, Lita",
                 desc="The Hardys with Lita at ringside, the trio at the center of the TLC era. "
                      "The 2005 Edge and Lita affair later became Matt's most personal feud."),
            dict(era="WWE &middot; 2003",
                 name="Mattitude Followers",
                 members="Matt Hardy, Shannon Moore",
                 desc="The Version 1 cult of one follower. Matt disbanded it in November 2003 and "
                      "went back to Raw."),
            dict(era="AEW &middot; 2021&ndash;2024",
                 name="Hardy Family Office",
                 members="Matt Hardy, Private Party, and later Andrade El Idolo as co-owner",
                 desc="Formed after Revolution 2021 as the Matt Hardy Empire, then renamed. Andrade "
                      "bought a 51% stake in storyline. The Hardy Party ended on the January 5, "
                      "2024 Rampage."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Five characters, one performer who keeps rewriting himself.",
        cards=[
            dict(mono="HB", era="WWF &middot; 1998&ndash;2002", name="Hardy Boyz daredevil",
                 desc="The steadier half of the ladder team. Twist of Fate, Side Effect, and "
                      "the first tag team ladder match at No Mercy 1999."),
            dict(mono="V1", era="WWE &middot; 2002&ndash;2003", name="Matt Hardy Version 1",
                 desc="Heel turn on August 12, 2002, then SmackDown, Mattitude and a "
                      "Cruiserweight title. A Best Gimmick winner from the Wrestling Observer."),
            dict(mono="BR", era="TNA &middot; 2016&ndash;2017, 2024&ndash;", name="Broken Matt Hardy",
                 desc="Debuted May 17, 2016. The Final Deletion, Delete or Decay and the Great "
                      "War followed. He brought it back for the 2024 TNA return."),
            dict(mono="WK", era="WWE &middot; 2018", name="Woken Matt Hardy",
                 desc="The Broken character under a new name for WWE. The Ultimate Deletion "
                      "with Bray Wyatt aired on Raw on March 19, 2018."),
            dict(mono="BM", era="AEW &middot; 2020&ndash;2024", name="Big Money Matt",
                 desc="The cash-flashing manager persona behind Private Party and the Hardy "
                      "Family Office."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="From a backyard promotion in 1992 to a TNA storyline in November 2026.",
        rows=[
            dict(year="1992", title="Debut",
                 desc="First match on October 15, 1992. First WWF match on May 23, 1994, a loss "
                      "to Nikolai Volkoff on Raw."),
            dict(year="1997", title="OMEGA",
                 desc="Founds the Organization of Modern Extreme Grappling Arts with Jeff. It "
                      "closes in October 1999 after both sign with the WWF."),
            dict(year="1999", title="First tag titles, first ladder match",
                 desc="Wins the WWF Tag titles on July 5, then the No Mercy ladder match over "
                      "Edge and Christian on October 17."),
            dict(year="2000", title="The first TLC",
                 desc="Loses the triangle ladder match at WrestleMania 2000 and the first TLC at "
                      "SummerSlam on August 27."),
            dict(year="2001", title="TLC II and singles gold",
                 desc="TLC II at WrestleMania X-Seven on April 1, the European title that April, "
                      "and the WCW and World tag titles in the fall."),
            dict(year="2002", title="Version 1",
                 desc="Turns on Jeff on the August 12 Raw and becomes Matt Hardy Version 1 on "
                      "SmackDown."),
            dict(year="2003", title="Cruiserweight Champion",
                 desc="Beats Billy Kidman at No Way Out on February 23 and retains against Rey "
                      "Mysterio at WrestleMania XIX."),
            dict(year="2005", title="Released, then back",
                 desc="Released on April 11 after the Edge and Lita affair went public. He returns "
                      "in August and fights Edge at SummerSlam, Unforgiven and Raw Homecoming."),
            dict(year="2008", title="US and ECW Champion",
                 desc="Wins the United States title at Backlash on April 27 and the ECW title at "
                      "Unforgiven on September 7."),
            dict(year="2009", title="Brother against brother",
                 desc="Costs Jeff the WWE title at the Royal Rumble on January 25, beats him at "
                      "WrestleMania 25, and loses the Backlash I Quit match."),
            dict(year="2010", title="WWE release",
                 desc="Sent home from a European tour in September. WWE announces his release on "
                      "October 15."),
            dict(year="2011", title="TNA, arrest, release",
                 desc="Debuts in TNA on January 9. He is released after an August 20 DUI arrest."),
            dict(year="2015", title="TNA World Champion",
                 desc="Wins the TNA tag titles in Ultimate X and the TNA World Heavyweight "
                      "Championship at Bound for Glory on October 4."),
            dict(year="2016", title="Broken",
                 desc="Debuts Broken Matt Hardy on May 17, airs the Final Deletion on July 5, and "
                      "wins the TNA tag titles at Bound for Glory on October 2."),
            dict(year="2017", title="ROH, then WrestleMania",
                 desc="Holds the ROH tag titles from March 4 to April 1, then returns to WWE at "
                      "WrestleMania 33 the next night and wins the Raw Tag titles."),
            dict(year="2018", title="Woken",
                 desc="Beats Bray Wyatt in the Ultimate Deletion, wins the WrestleMania 34 battle "
                      "royal, then wins the Raw Tag titles with Wyatt on April 27."),
            dict(year="2020", title="AEW",
                 desc="Debuts on the March 18 Dynamite, wins the Stadium Stampede on May 23, and "
                      "beats Sammy Guevara at All Out on September 5."),
            dict(year="2022", title="The Hardys in AEW",
                 desc="Jeff arrives on March 9. They beat the Young Bucks at Double or Nothing on "
                      "May 29."),
            dict(year="2024", title="Home to TNA",
                 desc="His AEW deal expires in April. He returns at Rebellion on April 20, and the "
                      "Hardys win the TNA tag titles at Bound for Glory on October 26."),
            dict(year="2025", title="Double champions",
                 desc="Regains the TNA tag titles at Slammiversary on July 20, adds the NXT titles "
                      "on October 7, and beats Team 3D in their retirement match on October 12."),
            dict(year="2026", title="Gold, then syX",
                 desc="Wins a fifth TNA tag reign on June 28 and loses it at Lockdown on August "
                      "23. Challenges Nic Nemeth for the TNA World title in a No DQ match on "
                      "September 10, then loses to syX at Bound for Glory and in the October 29 "
                      "Slaughterhouse match."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Edge & Christian and The Dudley Boyz",
                 desc="The three-team rivalry behind No Mercy 1999, the first TLC at SummerSlam "
                      "2000 and TLC II at WrestleMania X-Seven. Every multi-team ladder match since "
                      "borrows from it."),
            dict(name="Edge", slug="edge",
                 desc="In 2005 the feud was real. After the Edge and Lita affair and his release, "
                      "Matt came back to lose at SummerSlam, win the Unforgiven cage match, and "
                      "lose the Loser Leaves Raw ladder match on October 3."),
            dict(name="Jeff Hardy", slug="jeff-hardy",
                 desc="His brother and his best opponent. Vengeance 2001, the 2009 chair "
                      "betrayal and WrestleMania 25, and the 2016 Final Deletion against Brother "
                      "Nero."),
            dict(name="Bray Wyatt",
                 desc="The 2018 Woken feud ended in the Ultimate Deletion, then turned into a "
                      "tag team that won the Raw Tag titles."),
            dict(name="Rey Mysterio", slug="rey-mysterio",
                 desc="Version 1 beat him at WrestleMania XIX to keep the Cruiserweight title, "
                      "then lost it to him on SmackDown on June 5, 2003."),
            dict(name="The Nemeths", slug="nic-nemeth",
                 desc="Nic and Ryan Nemeth took the TNA tag titles from the Hardys at Rebellion "
                      "2025 and again at Lockdown 2026, then held them in the October 8 rematch."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Books, television, a podcast and decades of video games.",
        rows=[
            dict(when="2003", title="The Hardy Boyz: Exist 2 Inspire", kind="Book",
                 desc="The brothers' autobiography, written with Michael Krugman."),
            dict(when="2008", title="Twist of Fate: The Matt and Jeff Hardy Story", kind="Video",
                 desc="WWE's documentary on the brothers, released April 29, 2008."),
            dict(when="2002", title="Fear Factor", kind="Television",
                 desc="Won $50,000 for the American Cancer Society on the February 25, 2002 episode."),
            dict(when="2013", title="Pro Wrestlers vs Zombies", kind="Film",
                 desc="Played himself alongside his wife, Reby Sky."),
            dict(when="1999&ndash;2026", title="WWE, AEW and 2K games", kind="Game",
                 desc="Debuted in WWF WrestleMania 2000. Later AEW Fight Forever (2023) and WWE "
                      "2K26 Ringside Pass Season 4 (2026)."),
            dict(when="Ongoing", title="The Extreme Life of Matt Hardy", kind="Podcast",
                 desc="His podcast, where he discussed re-signing with TNA in November 2024."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The marks and milestones, with the caveats stated plainly.",
        stats=[
            ("18", "Tag reigns in WWE, TNA and ROH"),
            ("10", "WrestleMania appearances"),
            ("2",  "Best Gimmick awards"),
        ],
        rows=[
            dict(name="Twelve WWE tag team championship reigns",
                 sub="Six World Tag, three WWE/Raw Tag, one SmackDown Tag, one WCW Tag and one "
                     "NXT Tag. Wikipedia credits him as WWE's fourth Tag Team Triple Crown "
                     "Champion."),
            dict(name="Five TNA World Tag Team Championship reigns with Jeff",
                 sub="2015, 2016, 2024, 2025 and 2026, per the TNA title history as of November "
                     "2026."),
            dict(name="Ten WrestleMania appearances",
                 sub="From the WrestleMania 2000 ladder match to the WrestleMania 34 battle royal. "
                     "Wins at XIX, 25, 33 and 34."),
            dict(name="Best Gimmick, twice",
                 sub="Wrestling Observer awards for Version 1 and for Broken Matt Hardy."),
            dict(name="PWI honors",
                 sub="Match of the Year 2000 and 2001, Tag Team of the Year 2000 and 2025, Feud of "
                     "the Year 2005 and Comeback of the Year 2017."),
            dict(name="Andre the Giant Memorial Battle Royal winner",
                 sub="WrestleMania 34 Kickoff, April 8, 2018."),
        ],
        footnote=("Not published: a career win-loss total, star ratings, and an entrance theme. "
                  "None could be verified. The Hardys are not current champions, and Matt has "
                  "not been inducted into the WWE Hall of Fame."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Matt_Hardy"),
        dict(k="Wikipedia", v="The Hardy Boyz", href="https://en.wikipedia.org/wiki/The_Hardy_Boyz"),
        dict(k="Wikipedia", v="TNA World Tag Team Championship history",
             href="https://en.wikipedia.org/wiki/List_of_TNA_World_Tag_Team_Champions"),
        dict(k="TNA", v="Official roster page", href="https://tnawrestling.com/roster/matt-hardy"),
        dict(k="PWTorch", v="Lockdown 2026 results", href="https://www.pwtorch.com/site/?p=221276"),
        dict(k="Wrestling Inc", v="Bound for Glory 2026 results",
             href="https://www.wrestlinginc.com/2283301/tna-bound-for-glory-2026-results/"),
        dict(k="Fightful", v="Matt Hardy & Moose vs. syX set for Destination X",
             href="https://www.fightful.com/?p=337679"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Matt Hardy still wrestling in 2026?",
            a="Yes. He is on the TNA roster at 52. After syX beat the Hardys in the October 29, "
              "2026 Slaughterhouse syX match and Jeff was written out injured, Matt was booked "
              "to team with Moose against syX at Destination X on November 15, 2026.",
            q_ld="Is Matt Hardy still an active wrestler in 2026?",
            a_ld="Yes. As of November 2026 Matt Hardy, aged 52, is an active TNA wrestler. After "
                 "the Hardys lost a Slaughterhouse syX match on October 29, 2026 and Jeff Hardy was "
                 "written out with a storyline injury, Matt Hardy was booked to team with Moose "
                 "against syX at TNA Destination X on November 15, 2026."),
        dict(
            q="Are the Hardys the current TNA World Tag Team Champions?",
            a="No. Their fifth TNA reign began at Slammiversary on June 28, 2026 and ended at "
              "Lockdown on August 23, 2026, when the Nemeths won a steel cage match. The Nemeths "
              "also beat them in an October 8 rematch.",
            q_ld="Are The Hardys the current TNA World Tag Team Champions?",
            a_ld="No. The Hardys won the TNA World Tag Team Championship for a fifth time at "
                 "Slammiversary on June 28, 2026 and lost it to Nic and Ryan Nemeth at Lockdown on "
                 "August 23, 2026. The Nemeths retained against the Hardys on October 8, 2026."),
        dict(
            q="How many tag team titles has Matt Hardy won?",
            a="Twelve WWE tag reigns (six World Tag, three WWE/Raw Tag, one SmackDown Tag, one "
              "WCW Tag and one NXT Tag), five TNA World Tag Team reigns and one ROH World Tag "
              "Team reign. All but two came with Jeff. The others were with MVP in 2007 and Bray "
              "Wyatt in 2018.",
            q_ld="How many tag team championships has Matt Hardy won?",
            a_ld="Matt Hardy has twelve WWE tag team championship reigns, five TNA World Tag Team "
                 "Championship reigns and one ROH World Tag Team Championship reign. Most were "
                 "with his brother Jeff Hardy; one WWE reign was with MVP in 2007 and one with Bray "
                 "Wyatt in 2018."),
        dict(
            q="Has Matt Hardy been a world champion?",
            a="He won the TNA World Heavyweight Championship twice, at Bound for Glory on "
              "October 4, 2015 and in a last man standing match taped January 8, 2016. In WWE he "
              "held the ECW Championship from September 7, 2008 to January 13, 2009.",
            q_ld="Has Matt Hardy won a world championship?",
            a_ld="Yes. Matt Hardy won the TNA World Heavyweight Championship twice, first at Bound "
                 "for Glory on October 4, 2015 and again in January 2016. In WWE he held the ECW "
                 "Championship, WWE's 2006 to 2010 ECW title, from September 2008 to January 2009."),
        dict(
            q="What was Matt Hardy Version 1?",
            a="His 2002&ndash;2003 heel character. He turned on Jeff on the August 12, 2002 Raw, "
              "moved to SmackDown, preached Mattitude with Shannon Moore as his follower, and won "
              "the Cruiserweight title from Billy Kidman at No Way Out 2003.",
            q_ld="What was the Matt Hardy Version 1 gimmick?",
            a_ld="Matt Hardy Version 1 was his heel character from 2002 to 2003 in WWE. After "
                 "attacking Jeff Hardy on Raw on August 12, 2002, he moved to SmackDown, led the "
                 "Mattitude Followers with Shannon Moore, and won the Cruiserweight Championship "
                 "from Billy Kidman at No Way Out 2003."),
        dict(
            q="What was the Final Deletion?",
            a="A cinematic match that aired on Impact on July 5, 2016. Broken Matt Hardy beat "
              "his brother Jeff at the Hardy compound in Cameron, North Carolina, and took sole "
              "ownership of the Hardy brand in storyline. It was followed by Delete or Decay on "
              "September 8, 2016.",
            q_ld="What was the Final Deletion in TNA?",
            a_ld="The Final Deletion was a cinematic match that aired on TNA Impact on July 5, "
                 "2016, in which Broken Matt Hardy defeated Jeff Hardy at the Hardy family "
                 "property in North Carolina and took sole ownership of the Hardy brand in "
                 "storyline."),
        dict(
            q="Why did WWE release Matt Hardy in 2005?",
            a="WWE released him on April 11, 2005, after his public online conduct following the "
              "affair between Lita, his girlfriend of six years, and Edge. Fan backlash followed, "
              "and WWE brought him back that summer for a televised feud with Edge.",
            q_ld="Why was Matt Hardy released by WWE in 2005?",
            a_ld="WWE released Matt Hardy on April 11, 2005, after his online conduct following "
                 "Lita's affair with Edge. After fan backlash he returned in August 2005 and feuded "
                 "with Edge at SummerSlam, Unforgiven and Raw Homecoming."),
        dict(
            q="What did Matt Hardy do in AEW?",
            a="He debuted on the March 18, 2020 Dynamite, won the Stadium Stampede on May 23, "
              "2020, managed as Big Money Matt and led the Hardy Family Office. Jeff joined in "
              "2022. He won no AEW championship, and his contract expired in April 2024.",
            q_ld="What did Matt Hardy do in AEW?",
            a_ld="Matt Hardy worked for AEW from March 2020 to April 2024. He won the Stadium "
                 "Stampede match at Double or Nothing 2020, used the Big Money Matt persona, led "
                 "the Hardy Family Office, and reunited with Jeff Hardy in 2022. He did not win an "
                 "AEW championship."),
        dict(
            q="Is Matt Hardy in the WWE Hall of Fame?",
            a="No. Matt has said he expects the Hardys to go in eventually but does not think "
              "they are ready while they are still wrestling.",
            q_ld="Is Matt Hardy in the WWE Hall of Fame?",
            a_ld="No. As of November 2026 Matt Hardy has not been inducted into the WWE Hall of "
                 "Fame. He has said he expects the Hardys to be inducted eventually but does not "
                 "feel they are ready while still actively competing."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Matthew Moore Hardy"),
        dict(label="Born", value="September 23, 1974", sub="Cameron, North Carolina &middot; age 52"),
        dict(label="Billed from", value="Cameron, North Carolina"),
        dict(label="Height", value="6&#8242;2&#8243;", sub="188 cm (billed)"),
        dict(label="Weight", value="236 lb", sub="107 kg (billed)"),
        dict(label="Debut", value="October 15, 1992",
             sub="first WWF match May 23, 1994; full-time WWF contract 1998"),
        dict(label="Trained by", value="Dory Funk Jr."),
        dict(label="Signature", value="Twist of Fate &middot; Side Effect"),
        dict(label="Promotion", value="TNA", sub="returned April 20, 2024 at Rebellion"),
        dict(label="Also known as", value="Version 1 &middot; Broken Matt &middot; Woken Matt "
                                          "&middot; Big Money Matt"),
        dict(label="Family", value="Brother of Jeff Hardy",
             sub="married Reby Sky on October 5, 2013; four children"),
        dict(label="Status", value="Active, no title held",
             sub="Destination X vs. syX with Moose, November 15, 2026"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1974-09-23",
    bornplace="Cameron, North Carolina, United States",
    nationality="United States",
    height_cm=188,
    weight_kg=107,
    ld=dict(
        alternateName=["Matthew Moore Hardy", "Matt Hardy Version 1", "Broken Matt Hardy",
                       "Woken Matt Hardy", "Big Money Matt"],
        award=["TNA World Heavyweight Championship (2 reigns)",
               "ECW Championship (1 reign, 2008-2009)",
               "WWE United States Championship (1 reign, 2008)",
               "WWE Cruiserweight Championship (1 reign, 2003)",
               "WWF European Championship (1 reign, 2001)",
               "WWF Hardcore Championship (1 reign, 2000)",
               "WWE tag team championships (12 reigns)",
               "TNA World Tag Team Championship (5 reigns, with Jeff Hardy)",
               "ROH World Tag Team Championship (1 reign, with Jeff Hardy)"],
        knowsAbout=["Professional wrestling", "Ladder matches", "TLC matches", "WWE", "TNA",
                    "AEW", "Ring of Honor", "The Hardy Boyz", "OMEGA promotion",
                    "Cinematic wrestling matches"],
        description="Matt Hardy, born Matthew Moore Hardy in Cameron, North Carolina, is an "
                    "American professional wrestler active in TNA. With his brother Jeff he forms "
                    "The Hardy Boyz, who helped define the ladder and TLC era. He has held twelve "
                    "WWE tag team championships, five TNA World Tag Team Championships, two TNA "
                    "World Heavyweight Championships and the ECW Championship, and created the "
                    "Version 1 and Broken Matt Hardy characters.",
        sameAs=["https://en.wikipedia.org/wiki/Matt_Hardy",
                "https://tnawrestling.com/roster/matt-hardy",
                "https://x.com/matthardybrand",
                "https://www.instagram.com/matthardybrand"],
    ),
)
