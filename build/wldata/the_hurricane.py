# -*- coding: utf-8 -*-
"""The Hurricane (Gregory Shane Helms) - dossier data.

Compiled November 9, 2026 from data/the-hurricane.md, which carries a source URL
on every claim. Replaces the old variant-X page (~2,064 words): every harvested
claim was re-verified, and five were corrected (2021 Rumble entry number, the 2002
tag title's name, the scope of the "longest Cruiserweight reign" record, the debut
year, the billed weight).

The record is a verified sample: every pay-per-view match found on Wikipedia event
pages plus the TV matches where a title changed hands. Cagematch's match list could
not be fetched (proxy blocked), so no win-loss total is published and record.total
is the honest row count.

Deliberate omissions:
  * Signature cards carry no star rating. No Observer or Cagematch grade was
    verified for any of these matches, and this site never invents one.
  * No Instagram link (none verified). The X account is listed on Wikipedia.
  * No pulse section: there is no verified current feed. Status is in now_* and FAQ.
  * No Spotify player: no verified track id for "Eye of the Hurricane," so the
    walk-out band ships with links only.
  * A March 10, 2006 champion vs champion loss is left out under the site's
    Chris Benoit policy.
"""

ROWS = [
    # ---------------- WCW 2000-2001
    dict(result="W", date="2000-02-28", promo="WCW", type="tag", landmark=True,
         event="Nitro", opponent="Brian Knobbs",
         stip="3 Count win the title together and defend it under the Freebird Rule",
         title="WCW Hardcore Championship"),
    dict(result="L", date="2000-03-19", promo="WCW", type="tag",
         event="Uncensored", opponent="Brian Knobbs",
         stip="Hardcore gauntlet; Knobbs pinned all three members of 3 Count",
         title="WCW Hardcore Championship"),
    dict(result="W", date="2000-08-13", promo="WCW", type="tag",
         event="New Blood Rising", opponent="The Jung Dragons",
         stip="Gold Record ladder match, 3 Count with Tank Abbott", title=""),
    dict(result="L", date="2000-09-17", promo="WCW", type="tag",
         event="Fall Brawl", opponent="The Misfits in Action",
         stip="Six-man tag as 3 Count", title=""),
    dict(result="W", date="2000-11-26", promo="WCW", type="tag",
         event="Mayhem", opponent="Evan Karagias & Jamie Knoble; The Jung Dragons",
         stip="Triple threat tag with Shannon Moore", title=""),
    dict(result="W", date="2000-12-17", promo="WCW", type="tag", landmark=True,
         event="Starrcade", opponent="The Jung Dragons; Evan Karagias & Jamie Knoble",
         stip="Ladder match for a Cruiserweight title shot, with Shannon Moore", title=""),
    dict(result="L", date="2001-01-14", promo="WCW",
         event="Sin", opponent="Chavo Guerrero Jr.",
         stip="Opening match; pinned after a brainbuster", title="WCW Cruiserweight Championship"),
    dict(result="W", date="2001-02-18", promo="WCW",
         event="SuperBrawl Revenge", opponent="Shannon Moore and four others",
         stip="Six-way elimination, the night 3 Count split", title=""),
    dict(result="W", date="2001-03-18", promo="WCW", landmark=True,
         event="Greed", opponent="Chavo Guerrero Jr.",
         stip="Title win at WCW's last pay-per-view", title="WCW Cruiserweight Championship"),
    # ---------------- WWF/WWE 2001-2003
    dict(result="L", date="2001-07-05", promo="WWE",
         event="SmackDown", opponent="Billy Kidman",
         stip="WWF debut as Hollywood Gregory Helms (WWE-recognized air date)",
         title="WCW Cruiserweight Championship"),
    dict(result="W", date="2001-08-27", promo="WWE", landmark=True,
         event="Raw is War", opponent="Matt Hardy",
         stip="The Hurricane's debut night, with help from Ivory", title="WWF European Championship"),
    dict(result="L", date="2001-10-22", promo="WWE",
         event="Raw", opponent="Bradshaw", stip="Singles", title="WWF European Championship"),
    dict(result="L", date="2002-01-20", promo="WWE",
         event="Royal Rumble", opponent="29 others",
         stip="Rumble entrant No. 23, out in 39 seconds", title=""),
    dict(result="W", date="2002-03-17", promo="WWE", landmark=True,
         event="WrestleMania X8", opponent="Spike Dudley",
         stip="24/7 rule; swung in on a rope and pinned Spike backstage", title="WWF Hardcore Championship"),
    dict(result="L", date="2002-03-17", promo="WWE",
         event="WrestleMania X8", opponent="Mighty Molly",
         stip="24/7 rule; his sidekick hit him with a frying pan", title="WWF Hardcore Championship"),
    dict(result="W", date="2002-05-16", promo="WWE", landmark=True,
         event="SmackDown", opponent="Tajiri & Billy Kidman",
         stip="Triple threat", title="WWE Cruiserweight Championship"),
    dict(result="L", date="2002-06-23", promo="WWE",
         event="King of the Ring", opponent="Jamie Noble",
         stip="Singles, Columbus", title="WWE Cruiserweight Championship"),
    dict(result="W", date="2002-09-23", promo="WWE", type="tag", landmark=True,
         event="Raw", opponent="Christian & Lance Storm",
         stip="Tag with Kane", title="World Tag Team Championship"),
    dict(result="L", date="2002-10-14", promo="WWE", type="tag",
         event="Raw", opponent="Chris Jericho & Christian",
         stip="Tag with Kane", title="World Tag Team Championship"),
    dict(result="W", date="2003-03-10", promo="WWE", landmark=True,
         event="Raw", opponent="The Rock",
         stip="Roll-up after Steve Austin's arrival distracted The Rock, Cleveland", title=""),
    # ---------------- WWE 2004-2005
    dict(result="L", date="2004-01-19", promo="WWE",
         event="Raw", opponent="Randy Orton", stip="Singles", title=""),
    dict(result="L", date="2004-01-25", promo="WWE",
         event="Royal Rumble", opponent="29 others",
         stip="Rumble entrant No. 10, eliminated by Matt Morgan", title=""),
    dict(result="L", date="2005-01-30", promo="WWE",
         event="Royal Rumble", opponent="29 others",
         stip="Rumble entrant No. 3, out in 1:04", title=""),
    dict(result="W", date="2005-05-01", promo="WWE", type="tag", landmark=True,
         event="Backlash", opponent="La Résistance and three other teams",
         stip="Tag Team Turmoil with Rosey; Hurricane pinned off Rosey's shoulders",
         title="World Tag Team Championship"),
    dict(result="L", date="2005-08-08", promo="WWE", type="tag",
         event="Raw", opponent="The Heart Throbs & Victoria",
         stip="Mixed six-person tag with Rosey and Super Stacy", title=""),
    dict(result="L", date="2005-09-18", promo="WWE", type="tag",
         event="Unforgiven", opponent="Lance Cade & Trevor Murdoch",
         stip="Tag with Rosey", title="World Tag Team Championship"),
    dict(result="W", date="2005-11-07", promo="WWE",
         event="Raw", opponent="Rosey",
         stip="First big win as Gregory Helms, over his old partner", title=""),
    # ---------------- WWE 2006-2009
    dict(result="W", date="2006-01-29", promo="WWE", landmark=True,
         event="Royal Rumble", opponent="Kid Kash, Funaki, Jamie Noble, Nunzio & Paul London",
         stip="Cruiserweight Open; pinned Funaki after a Shining Wizard. Day 1 of 385",
         title="WWE Cruiserweight Championship"),
    dict(result="L", date="2006-06-16", promo="WWE",
         event="SmackDown", opponent="Rey Mysterio",
         stip="Champion vs champion, non-title", title=""),
    dict(result="L", date="2006-07-07", promo="WWE",
         event="SmackDown", opponent="Bobby Lashley",
         stip="Champion vs champion, non-title", title=""),
    dict(result="L", date="2006-10-08", promo="WWE",
         event="No Mercy", opponent="Matt Hardy",
         stip="Non-title, in Raleigh, North Carolina", title=""),
    dict(result="W", date="2006-12-17", promo="WWE",
         event="Armageddon", opponent="Jimmy Wang Yang",
         stip="Singles, Richmond", title="WWE Cruiserweight Championship"),
    dict(result="L", date="2007-02-18", promo="WWE", landmark=True,
         event="No Way Out", opponent="Chavo Guerrero and six others",
         stip="Cruiserweight Open; Chavo pinned Jimmy Wang Yang. The 385-day reign ends",
         title="WWE Cruiserweight Championship"),
    dict(result="W", date="2008-12-05", promo="WWE",
         event="SmackDown", opponent="MVP",
         stip="In-ring return after the 2007 neck surgery", title=""),
    dict(result="W", date="2009-11-17", promo="WWE", landmark=True,
         event="ECW", opponent="Paul Burchill",
         stip="Mask vs career, as The Hurricane", title=""),
    # ---------------- cameos
    dict(result="L", date="2018-01-28", promo="WWE", landmark=True,
         event="Royal Rumble", opponent="29 others",
         stip="Surprise entrant No. 21, eliminated by John Cena after 45 seconds", title=""),
    dict(result="L", date="2021-01-31", promo="WWE",
         event="Royal Rumble", opponent="29 others",
         stip="Entrant No. 23 at the ThunderDome, eliminated by Big E and Bobby Lashley. His last WWE match",
         title=""),
]

DATA = dict(
    slug="the-hurricane",
    name="The Hurricane",
    realname="Gregory Shane Helms",
    epithet="The Superhero of Raw",
    hook="WCW, WWE & WWE Producer",
    art="the-hurricane",

    meta_desc=("The Hurricane, Gregory Shane Helms: 3 Count and WCW Cruiserweight Champion, the WWE "
               "superhero who pinned The Rock, a 385-day Cruiserweight reign as Gregory Helms, and a "
               "WWE producer since 2019. Verified record, titles and FAQ."),
    og_desc=("Sugar Shane, The Hurricane, Gregory Helms. Eight major-promotion reigns, a pin on The "
             "Rock, the longest reign in Cruiserweight title history, then the producer's chair."),
    tw_desc="The Hurricane: WCW Cruiserweight Champion, the man who pinned The Rock, WWE producer.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1990",
    height_imp="6&#8242;0&#8243;",
    weight_lb="215",
    vitals_tagline="Sugar Shane to superhero",
    x_url="https://x.com/ShaneHelmsCom",
    support_note="Profile &middot; Games &middot; Watch",
    sp_items=[
        dict(ic="WWE", title="Official Profile", sub="WWE.com superstar page", tag="Visit",
             href="https://www.wwe.com/superstars/thehurricane"),
        dict(ic="X", title="@ShaneHelmsCom", sub="His account on X", tag="Follow",
             href="https://x.com/ShaneHelmsCom"),
        dict(ic="2K", title="WWE 2K26", sub="Playable legend", tag="Play",
             href="https://wwe.2k.com/"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="3 Count &middot; Sugar Shane &middot; The Hurricane &middot; Gregory Helms &middot; WWE producer",
    hero_tag="Smithfield, North Carolina &middot; <em>WCW 1999&ndash;2001 &middot; WWF/WWE 2001&ndash;2010 &middot; WWE producer 2019&ndash;</em>",
    now_label="NOW",
    now_bold="WWE backstage producer",
    now_tail=(" &middot; hired January 2019, furloughed April to November 2020, Legends deal March 2022. "
              "Fightful still listed him as a WWE producer in July 2026. Last match: 2021 Royal Rumble."),
    hstats=[
        dict(value="385",  x=False, label="Days, Record Cruiserweight Reign"),
        dict(value="8",    x=False, label="Major-Promotion Title Reigns"),
        dict(value="2003", x=False, label="The Night He Pinned The Rock"),
        dict(value="2019", x=False, label="WWE Producer Since"),
    ],
    ghost_link="From a boy band parody to the producer's headset",
    vlabel="Est. 1990 &middot; Smithfield, North Carolina",
    mono="HH",

    # ---------------------------------------------------------------- 01 overview
    correction=2,
    overview=[
        "<b>The Hurricane</b> is Gregory Shane Helms, a cruiserweight from Smithfield, North "
        "Carolina who got over in three different costumes. In WCW he was one third of 3 Count, a "
        "boy band parody, and then Sugar Shane, the company's last Cruiserweight Champion before "
        "the sale. In the WWF he put on a green mask and cape and became a comic-book superhero who "
        "won the European, Hardcore, Cruiserweight and World Tag Team titles. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">385</span>'
        '<span class="pull-cap">days as Cruiserweight Champion, 2006&ndash;07, the longest reign in that title&rsquo;s history</span></span>'
        "On March 10, 2003 he pinned The Rock on Raw. Then he took the mask off. As Gregory Helms "
        "he held the Cruiserweight Championship for 385 days, from the 2006 Royal Rumble to No Way "
        "Out 2007.",

        "He has spent more of the last seven years behind the curtain than in front of it. WWE "
        "hired him as a backstage producer in January 2019. He was furloughed in April 2020, "
        "worked one AEW appearance that November, and was back producing for WWE within weeks. He "
        "signed a Legends deal in March 2022. His last WWE match was a 30-second cameo in the 2021 "
        "Royal Rumble. As of November 2026 the most recent reports still describe him as a WWE "
        "producer.",

        "Three things on the old version of this page needed fixing. First, the 385-day reign is "
        "the record for the Cruiserweight title that started in WCW and was retired in 2007. The "
        "separate 2016&ndash;2022 Cruiserweight title had a longer reign, Jordan Devlin&rsquo;s 439 "
        "days. Second, the belts he won with Kane in 2002 were Raw&rsquo;s World Tag Team "
        "Championship. Third, he entered the 2021 Royal Rumble at No. 23, not No. 24. His debut "
        "date is also disputed: two sources say July 6, 1990, and one says 1991.",

        "He started in the Carolinas, where he and Mike Maverick won the OMEGA tag titles twice in "
        "the Hardys&rsquo; home promotion. WCW signed him with Shannon Moore in May 1999. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig pull-fig--sm">2001</span>'
        '<span class="pull-cap">WCW Cruiserweight Champion at Greed, March 18, WCW&rsquo;s last pay-per-view</span></span>'
        "3 Count held the WCW Hardcore title for 20 days in 2000 and won a ladder match at "
        "Starrcade for a title shot. Helms beat Chavo Guerrero Jr. for the Cruiserweight title at "
        "Greed and carried it into the WWF, where he lost it to Billy Kidman in July 2001. The "
        "Hurricane debuted on August 27 and won the European title from Matt Hardy that night.",

        "The superhero years brought sidekicks. Mighty Molly turned on him at WrestleMania X8. "
        "Rosey, the Super Hero in Training, won the World Tag Team title with him at Backlash 2005, "
        "and Stacy Keibler joined them as Super Stacy. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">2</span>'
        '<span class="pull-cap">vertebrae broken in his neck, reported May 18, 2007</span></span>'
        "A Kurt Angle beating in October 2005 turned him into Gregory Helms. A broken neck in 2007 "
        "cost him about 18 months. He came back in December 2008, revived the mask on ECW in 2009, "
        "and was released in February 2010. He worked the independents, then TNA as an agent and "
        "on-screen leader of The Helms Dynasty from 2015 to 2017, then ROH in 2018, before WWE "
        "brought him back as a producer.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Verified sample",
        promo_order=["WCW", "WWE"],
        promo_labels={"WCW": "WCW", "WWE": "WWF/WWE"},
        stats=[
            ("37",   "Bouts in this sample"),
            ("8",    "Title reigns"),
            ("385",  "Days, longest reign"),
            ("5",    "Royal Rumble matches"),
            ("2000", "First logged PPV"),
            ("2021", "Last WWE match"),
        ],
        lead=("This table is a verified sample, not his full record. Listed: every pay-per-view match "
              "found on the event results, plus the TV matches where a title changed hands. "
              "Cagematch&rsquo;s match log could not be read, so no win-loss total is published. "
              "Royal Rumble entry numbers follow WWE.com and Wrestling Inc; some event pages print "
              "the elimination order instead. Turn spoilers on to see results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("Five nights that define him. No star rating is printed: no Observer or Cagematch "
                    "grade was verified for any of them."),
    signature=[
        dict(rating="&mdash;", event="Raw, March 10, 2003", opponent="The Rock",
             stip="The roll-up in Cleveland after Steve Austin's music hit"),
        dict(rating="&mdash;", event="Greed 2001", opponent="Chavo Guerrero Jr.",
             stip="WCW Cruiserweight title at WCW's last pay-per-view"),
        dict(rating="&mdash;", event="Royal Rumble 2006", opponent="Kid Kash, Funaki, Noble, Nunzio, London",
             stip="Cruiserweight Open, the start of the 385-day reign"),
        dict(rating="&mdash;", event="Starrcade 2000", opponent="The Jung Dragons; Karagias & Knoble",
             stip="3 Count's ladder match for a Cruiserweight title shot"),
        dict(rating="&mdash;", event="Backlash 2005", opponent="Tag Team Turmoil",
             stip="World Tag Team title with Rosey, won off Rosey's shoulders"),
    ],
    signature_count_word="five",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("8",   "Major-promotion reigns"),
            ("3",   "Cruiserweight reigns"),
            ("2",   "World Tag Team reigns"),
            ("385", "Days, record reign"),
        ],
        lead=("Eight reigns across WCW and WWE, from hardcore belts to tag gold. Reign counts follow "
              "Wikipedia&rsquo;s title histories; the record line names its counting rule."),
        rows=[
            dict(ic="C", name="WCW / WWE Cruiserweight Championship", count="3",
                 sub="As Shane Helms at Greed, March 18, 2001 &middot; as The Hurricane on SmackDown, "
                     "May 16, 2002 &middot; as Gregory Helms at the Royal Rumble, January 29, 2006, held "
                     "385 days (384 by WWE&rsquo;s count) until No Way Out, February 18, 2007. The "
                     "record is for this WCW-origin title; the separate 2016&ndash;22 title had a "
                     "439-day reign"),
            dict(ic="T", name="World Tag Team Championship", count="2",
                 sub="With Kane, September 23 to October 14, 2002 &middot; with Rosey, Backlash May 1 "
                     "to Unforgiven September 18, 2005"),
            dict(ic="E", name="WWF European Championship", count="1",
                 sub="Won from Matt Hardy on Raw is War, August 27, 2001, the night The Hurricane "
                     "debuted &middot; lost to Bradshaw October 22, 2001"),
            dict(ic="H", name="WWF Hardcore Championship", count="1",
                 sub="Won from Spike Dudley and lost to Mighty Molly under the 24/7 rule, both at "
                     "WrestleMania X8, March 17, 2002"),
            dict(ic="H", name="WCW Hardcore Championship", count="1",
                 sub="As 3 Count with Shannon Moore and Evan Karagias, Freebird Rule &middot; won from "
                     "Brian Knobbs on Nitro February 28, 2000 &middot; lost to him at Uncensored, 20 "
                     "days later"),
            dict(ic="O", name="Wrestling Observer Best Gimmick, 2001", count="&mdash;",
                 sub="For The Hurricane, per Wikipedia and The SmackDown Hotel"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Teams &amp; Sidekicks",
        lead="A boy band, a tag team in the Hardys' backyard, and a superhero's supporting cast.",
        cards=[
            dict(era="Carolina indies &middot; 1997&ndash;98",
                 name="The Serial Thrillaz",
                 members="Shane Helms, Mike Maverick",
                 desc="Two-time OMEGA Tag Team Champions in the Cameron, North Carolina promotion run "
                      "by Matt and Jeff Hardy of The Hardy Boyz, plus the SCW tag titles."),
            dict(era="WCW &middot; 1999&ndash;2001",
                 name="3 Count",
                 members="Shane Helms, Shannon Moore, Evan Karagias; Tank Abbott as enforcer",
                 desc="Jimmy Hart's boy band parody. Debuted on Thunder on December 23, 1999, won the "
                      "WCW Hardcore title as a trio, and won the Gold Record ladder match at New Blood "
                      "Rising. Karagias was thrown out, and Helms and Moore split in February 2001."),
            dict(era="WWF &middot; 2001&ndash;02",
                 name="The Hurricane & Mighty Molly",
                 members="The Hurricane, Molly Holly",
                 desc="Molly became his superhero sidekick in September 2001. At WrestleMania X8 she "
                      "hit him with a frying pan, took his Hardcore title and went solo."),
            dict(era="WWE &middot; 2002",
                 name="Kane & The Hurricane",
                 members="Kane, The Hurricane",
                 desc="The odd couple that beat Christian and Lance Storm for Raw's World Tag Team "
                      "title on September 23, 2002. Chris Jericho and Christian took it three weeks "
                      "later."),
            dict(era="WWE &middot; 2003&ndash;05",
                 name="The Hurricane & Rosey",
                 members="The Hurricane, Rosey (Super Hero in Training); Super Stacy in 2005",
                 desc="Rosey became his trainee hero in 2003. They won the World Tag Team title at "
                      "Backlash 2005 and lost it at Unforgiven. Stacy Keibler joined as Super Stacy "
                      "until her trade to SmackDown in August 2005."),
            dict(era="TNA &middot; 2016&ndash;17",
                 name="The Helms Dynasty",
                 members="Gregory Shane Helms, Trevor Lee, Andrew Everett",
                 desc="Formed after Helms helped Lee win the X Division title on February 2, 2016. "
                      "Helms led it on screen while working as a TNA agent."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Three main characters, one man, and a mask that kept coming back.",
        cards=[
            dict(mono="SS", era="WCW &middot; 2000&ndash;01", name="Sugar Shane",
                 desc="The solo cruiserweight after 3 Count, with the Vertebreaker as his finisher. "
                      "WCW Cruiserweight Champion when the company was sold."),
            dict(mono="HG", era="WWF &middot; 2001", name="Hollywood Gregory Helms",
                 desc="His first WWF character, an Alliance member who debuted on SmackDown on July "
                      "5, 2001 and lost the WCW Cruiserweight title to Billy Kidman."),
            dict(mono="TH", era="WWF/WWE &middot; 2001&ndash;05, 2009&ndash;10", name="The Hurricane",
                 desc="Green mask, cape, the Hurri-Cycle and a chokeslam far too big for him. Won the "
                      "European, Hardcore, Cruiserweight and tag titles and the 2001 Observer award "
                      "for Best Gimmick. Revived on ECW in 2009."),
            dict(mono="GH", era="WWE &middot; 2005&ndash;09", name="Gregory Helms",
                 desc="The serious heel who said he had been carrying Rosey. No cape, Shining Wizard "
                      "and Nightmare on Helms Street, and the 385-day Cruiserweight reign."),
            dict(mono="HH", era="2010&ndash;present", name="Hurricane Helms",
                 desc="The name that joins both halves, used on the independents, in TNA as Gregory "
                      "Shane Helms, at the 2018 and 2021 Royal Rumbles, and in WWE 2K22 onward."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Carolina indies to the producer's headset, with three costumes in between.",
        rows=[
            dict(year="1990", title="Debut in North Carolina",
                 desc="July 6, 1990 per Wikipedia's infobox and Cagematch; Wikipedia's body text says "
                      "1991. Wins the SWA Light Heavyweight title early."),
            dict(year="1997", title="The Serial Thrillaz",
                 desc="Wins the OMEGA tag titles twice with Mike Maverick in the Hardys' promotion."),
            dict(year="1999", title="WCW and 3 Count",
                 desc="Signs with WCW in May with Shannon Moore. 3 Count debuts on Thunder on "
                      "December 23."),
            dict(year="2000", title="Hardcore Champions",
                 desc="3 Count wins the WCW Hardcore title on February 28 and loses it at Uncensored. "
                      "Wins the Starrcade ladder match for a Cruiserweight title shot on December 17."),
            dict(year="2001", title="Cruiserweight Champion, then The Hurricane",
                 desc="Beats Chavo Guerrero Jr. at Greed on March 18. Loses the belt to Billy Kidman in "
                      "the WWF in July. Debuts as The Hurricane on August 27 and wins the European "
                      "title."),
            dict(year="2002", title="Three more belts",
                 desc="Hardcore title at WrestleMania X8, the Cruiserweight title on May 16, and the "
                      "World Tag Team title with Kane on September 23."),
            dict(year="2003", title="He pins The Rock",
                 desc="Rolls up The Rock on Raw in Cleveland on March 10. Rosey becomes his Super Hero "
                      "in Training."),
            dict(year="2005", title="Tag champions, then the turn",
                 desc="Wins the World Tag Team title with Rosey at Backlash, adds Super Stacy, loses "
                      "the belts at Unforgiven, and turns heel as Gregory Helms in October."),
            dict(year="2006", title="The 385-day reign begins",
                 desc="Wins the Cruiserweight Open at the Royal Rumble on January 29 and holds the title "
                      "through the year."),
            dict(year="2007", title="Reign ends, neck breaks",
                 desc="Loses the title in the No Way Out Cruiserweight Open on February 18. WWE reports "
                      "two broken vertebrae on May 18."),
            dict(year="2008", title="Comeback",
                 desc="Returns on September 19 and beats MVP on SmackDown on December 5."),
            dict(year="2009", title="The mask on ECW",
                 desc="Drafted to ECW, revives The Hurricane, and beats Paul Burchill in a mask vs "
                      "career match on November 17. Released February 26, 2010."),
            dict(year="2015", title="TNA agent",
                 desc="Hired by TNA in March. Debuts on screen at Bound for Glory and leads The Helms "
                      "Dynasty from 2016. Leaves in June 2017."),
            dict(year="2018", title="Rumble cameo and ROH",
                 desc="Surprise Royal Rumble entrant No. 21 on January 28. Signs with ROH in June."),
            dict(year="2019", title="WWE producer",
                 desc="Returns to WWE as a backstage producer, reported January 28."),
            dict(year="2020", title="Furlough and return",
                 desc="Furloughed April 15. Appears at AEW Full Gear on November 7. Back producing for "
                      "WWE by Survivor Series weekend."),
            dict(year="2021", title="Last match",
                 desc="Royal Rumble entrant No. 23 at the ThunderDome on January 31."),
            dict(year="2022", title="Legends deal",
                 desc="Signs a WWE Legends contract on March 24 while still producing."),
            dict(year="2026", title="Still producing",
                 desc="Fightful describes him as a WWE producer in June and July 2026. He is playable "
                      "in WWE 2K26."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="The upset everybody remembers, and the men he traded belts with.",
        cards=[
            dict(name="The Rock", slug="the-rock",
                 desc="The Hurricane pinned The Rock on Raw on March 10, 2003 in Cleveland after "
                      "Steve Austin's arrival distracted him. Helms later called it a debt he can never "
                      "repay."),
            dict(name="Chavo Guerrero Jr.",
                 desc="Beat Helms at Sin in January 2001, lost the Cruiserweight title to him at Greed "
                      "two months later, and won the Cruiserweight Open that ended the 385-day reign "
                      "in 2007."),
            dict(name="Matt Hardy", slug="matt-hardy",
                 desc="Old friend from OMEGA. The Hurricane took his European title on debut night in "
                      "2001, and Hardy beat Gregory Helms at No Mercy 2006 in Raleigh."),
            dict(name="Rosey",
                 desc="Partner from 2003 and World Tag Team Champion with him in 2005, then the man "
                      "Gregory Helms said he had been carrying. Helms beat him on Raw on November 7, "
                      "2005."),
            dict(name="Shannon Moore",
                 desc="3 Count bandmate from the Carolinas to WCW. Moore turned on him in early 2001, "
                      "and Helms won the six-way at SuperBrawl Revenge."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="A theme on a WWE album, a movie stunt job and twenty video games.",
        rows=[
            dict(when="1999&ndash;2000", title="Can't Get You Outta My Heart", kind="Music",
                 desc="The Jimmy Hart song 3 Count lip-synced on Nitro, later replaced by Dance With "
                      "3 Count."),
            dict(when="2000", title="Ready to Rumble", kind="Screen",
                 desc="Stunt double for David Arquette in the WCW movie."),
            dict(when="2002", title="Eye of the Hurricane, WWE Anthology", kind="Music",
                 desc="His Jim Johnston theme, disc 3 track 10, released November 12, 2002."),
            dict(when="2011", title="Lizard Lick Towing", kind="TV",
                 desc="Guest appearance on the truTV series."),
            dict(when="2000&ndash;2007", title="WCW and WWE games", kind="Game",
                 desc="WCW Backstage Assault as Shane Helms, then WrestleMania X8, Shut Your Mouth, "
                      "Here Comes the Pain, WrestleMania 21 and SmackDown vs. Raw 2006 to 2008."),
            dict(when="2022&ndash;2026", title="WWE 2K22 to WWE 2K26", kind="Game",
                 desc="Playable as Hurricane Helms in 2K22 and as a legend through 2K26."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="Records and firsts, each with the rule that makes it true.",
        stats=[
            ("385", "Days, Cruiserweight reign"),
            ("20",  "Days, 3 Count Hardcore reign"),
            ("25",  "WCW contracts in the WWF purchase, his among them"),
        ],
        rows=[
            dict(name="Longest reign in Cruiserweight Championship history",
                 sub="385 days (384 recognized by WWE), January 29, 2006 to February 18, 2007. Applies "
                     "to the WCW-origin title retired in 2007, where it is the only reign of a year or "
                     "more."),
            dict(name="Longest reign of any SmackDown champion, at the time",
                 sub="Per Wikipedia's Helms biography, describing the record as of 2007."),
            dict(name="Pinned The Rock on Raw",
                 sub="March 10, 2003, Gund Arena, Cleveland, a roll-up after Steve Austin distracted "
                     "The Rock."),
            dict(name="First trio to hold the WCW Hardcore title",
                 sub="3 Count, February 28, 2000, under the Freebird Rule."),
            dict(name="European champion on debut night",
                 sub="The Hurricane's first night, August 27, 2001, over Matt Hardy."),
            dict(name="Wrestling Observer Best Gimmick, 2001",
                 sub="For The Hurricane character."),
        ],
        footnote=("No win-loss total appears on this page because none is verified. His billed height "
                  "and weight differ by source (6 ft 0 in and 215 lb on WWE.com, 5 ft 11 in and 216 lb "
                  "on Cagematch), and his birth year is 1974 on Wikipedia and 1972 on Cagematch."),
    ),

    # ---------------------------------------------------------------- walk-out
    theme=dict(
        kicker="Entrance theme",
        since="WWE Anthology &middot; 2002",
        track="Eye of the Hurricane",
        artist="Jim Johnston",
        meta="WWE Anthology &middot; disc 3, track 10 &middot; November 12, 2002 &middot; 2:51",
        note=("Jim Johnston wrote and performed The Hurricane's theme, and WWE put it on the third "
              "disc of WWE Anthology in 2002. He used it from 2001 to 2005 and again when the mask came "
              "back on ECW in 2009. As Gregory Helms he walked out to other music."),
        source_label="Links only &middot; no player",
        links=[
            dict(svc="Wikipedia", sub="WWE Anthology track list",
                 href="https://en.wikipedia.org/wiki/WWE_Anthology"),
            dict(svc="YouTube", sub="Search the track",
                 href="https://www.youtube.com/results?search_query=Eye+of+the+Hurricane+WWE+theme"),
            dict(svc="SmackDown Hotel", sub="Theme history by era",
                 href="https://www.thesmackdownhotel.com/wrestlers/gregory-helms-the-hurricane"),
        ],
        foot=('Sources: <a href="https://en.wikipedia.org/wiki/WWE_Anthology" target="_blank" '
              'rel="noopener">Wikipedia, WWE Anthology</a>, '
              '<a href="https://www.thesmackdownhotel.com/wrestlers/gregory-helms-the-hurricane" '
              'target="_blank" rel="noopener">The SmackDown Hotel</a>.'),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/thehurricane"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Gregory_Helms"),
        dict(k="Cagematch", v="Wrestler profile", href="https://www.cagematch.net/?id=2&nr=464"),
        dict(k="Wikipedia", v="Cruiserweight title history",
             href="https://en.wikipedia.org/wiki/WCW_Cruiserweight_Championship"),
        dict(k="Fightful", v="2019: back to WWE as a producer",
             href="https://www.fightful.com/wrestling/exclusives/exclusive-details-shane-helms-heading-wwe"),
        dict(k="Fightful", v="2026: Helms and AJ Styles",
             href="https://www.fightful.com/wrestling-news/aj-styles-opens-up-about-emotional-moment-with-shane-hurricane-helms-following-wwe-retirement-match/"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/the-hurricane.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Who is The Hurricane?",
            a="Gregory Shane Helms, a cruiserweight from Smithfield, North Carolina. He was Sugar "
              "Shane and one third of 3 Count in WCW, then The Hurricane, a masked superhero, in WWE "
              "from 2001. He also wrestled as Gregory Helms and Hurricane Helms.",
            q_ld="Who is The Hurricane in WWE?",
            a_ld="The Hurricane is Gregory Shane Helms, an American wrestler from Smithfield, North "
                 "Carolina. He wrestled in WCW as Shane Helms and Sugar Shane, then in WWE from 2001 as "
                 "The Hurricane, a masked superhero, and as Gregory Helms."),
        dict(
            q="Is The Hurricane still with WWE?",
            a="Yes, as a backstage producer. WWE hired him in January 2019, furloughed him in April "
              "2020 and brought him back that November. He signed a Legends deal in March 2022, and "
              "Fightful still described him as a WWE producer in July 2026.",
            q_ld="Does Shane Helms still work for WWE in 2026?",
            a_ld="Yes. Shane Helms has been a WWE backstage producer since January 2019, apart from a "
                 "furlough from April to November 2020. Fightful described him as a WWE producer in "
                 "June and July 2026."),
        dict(
            q="Did The Hurricane really beat The Rock?",
            a="Yes. On Raw on March 10, 2003 in Cleveland, Steve Austin's arrival distracted The Rock "
              "and The Hurricane rolled him up for the pin. Helms later called it a debt he can never "
              "repay.",
            q_ld="Did The Hurricane beat The Rock?",
            a_ld="Yes. The Hurricane pinned The Rock with a roll-up on the March 10, 2003 episode of WWE "
                 "Raw in Cleveland, after Steve Austin's arrival distracted The Rock."),
        dict(
            q="How long was Gregory Helms Cruiserweight Champion?",
            a="385 days. He won the Cruiserweight Open at the Royal Rumble on January 29, 2006 and "
              "lost the title in the No Way Out Cruiserweight Open on February 18, 2007. WWE counts it "
              "as 384 days.",
            q_ld="How long was Gregory Helms' Cruiserweight Championship reign?",
            a_ld="Gregory Helms held the WWE Cruiserweight Championship for 385 days, 384 by WWE's "
                 "count, from the Royal Rumble on January 29, 2006 to No Way Out on February 18, "
                 "2007."),
        dict(
            q="Is that the longest Cruiserweight reign ever?",
            a="For the original Cruiserweight title, the one that began in WCW and was retired in "
              "2007, yes. It is the only reign of a year or more. The separate 2016&ndash;2022 "
              "Cruiserweight title had a longer one: Jordan Devlin held it for 439 days.",
            q_ld="Is Gregory Helms the longest-reigning Cruiserweight Champion?",
            a_ld="Gregory Helms' 385-day reign is the longest in the history of the original WCW and "
                 "WWE Cruiserweight Championship, retired in 2007. The separate 2016 to 2022 "
                 "Cruiserweight Championship had a longer reign, Jordan Devlin's 439 days."),
        dict(
            q="What titles did The Hurricane win?",
            a="Eight reigns in WCW and WWE: the Cruiserweight title three times, the World Tag Team "
              "title twice (with Kane and with Rosey), and the WWF European, WWF Hardcore and WCW "
              "Hardcore titles once each.",
            q_ld="What championships did The Hurricane win?",
            a_ld="Gregory Helms won the WCW/WWE Cruiserweight Championship three times, the World Tag "
                 "Team Championship twice with Kane and with Rosey, and the WWF European, WWF Hardcore "
                 "and WCW Hardcore Championships once each."),
        dict(
            q="What was 3 Count?",
            a="A WCW boy band parody put together by Jimmy Hart: Shane Helms, Shannon Moore and Evan "
              "Karagias. They debuted on Thunder on December 23, 1999, held the WCW Hardcore title "
              "together for 20 days in 2000, and broke up in early 2001.",
            q_ld="What was 3 Count in WCW?",
            a_ld="3 Count was a WCW boy band parody of Shane Helms, Shannon Moore and Evan Karagias, "
                 "created by Jimmy Hart. It debuted on December 23, 1999 and held the WCW Hardcore "
                 "Championship as a trio in 2000."),
        dict(
            q="Who was Super Stacy?",
            a='<a href="/wrestlers/stacy-keibler/">Stacy Keibler</a>, who joined The Hurricane and '
              "Rosey as a superhero sidekick after they won the World Tag Team title at Backlash in "
              "May 2005. It lasted until she was traded to SmackDown that August.",
            q_ld="Who was Super Stacy in WWE?",
            a_ld="Super Stacy was Stacy Keibler, who joined The Hurricane and Rosey as their superhero "
                 "sidekick in 2005 after they won the World Tag Team Championship at Backlash."),
        dict(
            q="Why did The Hurricane become Gregory Helms?",
            a="Kurt Angle attacked him on Raw on October 17, 2005. He skipped a title match the next "
              "week, came back unmasked as Gregory Helms, said he had been carrying Rosey, and beat "
              "Rosey on November 7.",
            q_ld="Why did The Hurricane turn into Gregory Helms?",
            a_ld="After Kurt Angle attacked The Hurricane on October 17, 2005, Shane Helms dropped the "
                 "mask, turned heel as Gregory Helms, claimed he had been carrying Rosey, and beat "
                 "Rosey on November 7, 2005."),
        dict(
            q="Did The Hurricane wrestle in AEW or TNA?",
            a="Briefly. He was a TNA agent from March 2015 to June 2017 and led The Helms Dynasty on "
              "screen. His only AEW appearance was in the Elite Deletion match at Full Gear on "
              "November 7, 2020, while WWE had him furloughed.",
            q_ld="Did Shane Helms work for AEW or TNA?",
            a_ld="Shane Helms worked for TNA as an agent and on-screen talent from March 2015 to June "
                 "2017. He made one AEW appearance, in the Elite Deletion match at Full Gear on "
                 "November 7, 2020."),
        dict(
            q="What was The Hurricane's entrance theme?",
            a="<b>Eye of the Hurricane</b>, written and performed by Jim Johnston. It appears on WWE "
              "Anthology, released November 12, 2002.",
            q_ld="What was The Hurricane's WWE entrance theme?",
            a_ld="The Hurricane's WWE entrance theme was Eye of the Hurricane by Jim Johnston, released "
                 "on the WWE Anthology album in 2002."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Gregory Shane Helms"),
        dict(label="Born", value="July 12, 1974",
             sub="Smithfield, North Carolina &middot; Cagematch says 1972"),
        dict(label="Billed from", value="Smithfield / Raleigh, North Carolina"),
        dict(label="Height", value="6&#8242;0&#8243;", sub="183 cm WWE.com &middot; Cagematch 5&#8242;11&#8243;"),
        dict(label="Weight", value="215 lb", sub="98 kg WWE.com &middot; Cagematch 216 lb"),
        dict(label="Debut", value="July 6, 1990", sub="Wikipedia body text says 1991"),
        dict(label="WWF debut", value="July 5, 2001", sub="SmackDown, Hollywood Gregory Helms"),
        dict(label="Hurricane debut", value="August 27, 2001", sub="Raw is War, won the European title"),
        dict(label="Finishers", value="Vertebreaker &middot; Eye of the Hurricane &middot; Shining Wizard"),
        dict(label="Last WWE match", value="January 31, 2021", sub="Royal Rumble, entrant No. 23"),
        dict(label="Today", value="WWE producer", sub="since January 2019 &middot; Legends deal 2022"),
        dict(label="Also known as", value="Sugar Shane &middot; Gregory Helms &middot; Hurricane Helms"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1974-07-12",
    bornplace="Smithfield, North Carolina, United States",
    nationality="United States",
    height_cm=183,
    weight_kg=98,
    ld=dict(
        alternateName=["Gregory Shane Helms", "Shane Helms", "Gregory Helms", "Sugar Shane",
                       "Hurricane Helms", "Hollywood Gregory Helms"],
        award=["WCW/WWE Cruiserweight Championship (3 reigns)",
               "World Tag Team Championship (2 reigns)",
               "WWF European Championship", "WWF Hardcore Championship",
               "WCW Hardcore Championship",
               "Wrestling Observer Newsletter Best Gimmick (2001)"],
        knowsAbout=["Professional wrestling", "WWE", "WCW", "Cruiserweight wrestling",
                    "Wrestling match production"],
        description="The Hurricane is the ring name of Gregory Shane Helms, an American professional "
                    "wrestler and WWE backstage producer. He was a member of 3 Count and WCW "
                    "Cruiserweight Champion in WCW, then wrestled in WWE from 2001 to 2010 as The "
                    "Hurricane and Gregory Helms, winning eight major-promotion title reigns, including "
                    "a 385-day Cruiserweight Championship reign from 2006 to 2007. He has worked as a "
                    "WWE producer since 2019.",
        sameAs=["https://en.wikipedia.org/wiki/Gregory_Helms",
                "https://www.wwe.com/superstars/thehurricane",
                "https://www.cagematch.net/?id=2&nr=464",
                "https://x.com/ShaneHelmsCom"],
    ),
)
