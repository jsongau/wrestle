# -*- coding: utf-8 -*-
"""Seth Rollins - dossier data.

Sources: /tmp/research/seth-rollins.md (web-verified, compiled Aug 23 2026) and the
harvested match / signature data from the previous /wrestlers/seth-rollins/ page.

Three deliberate departures from the harvested page, all because the research file is
the source of truth and the old page contradicts it on its own terms:

  1. Money in the Bank, June 19 2016. The old page logged "L vs Roman Reigns". The
     research file (and the roman-reigns dossier) both have Rollins BEATING Reigns for
     the WWE Championship that night and losing it to Dean Ambrose's cash-in minutes
     later. Same bout, corrected result, plus the cash-in row it implies.
  2. Royal Rumble, January 25 2015. The old page tagged it "WWE Championship - Rollins
     retains". Rollins' first WWE Championship reign began March 29 2015, so the title
     column is left blank; the result is kept as harvested.
  3. WrestleMania XL Night 1, April 6 2024. The old page's match row names CM Punk as
     the opponent while its own signature card names Cody Rhodes; Cody is used. The
     old page also books it as a World Heavyweight Championship loss, which cannot be
     squared with a 316-day reign ending the NEXT night to Damian Priest's cash-in, so
     no title is claimed on that row and the disagreement is surfaced in the
     Championships section instead.

No career win-loss total is published: the harvester flags the old page's "81-58"
headline as inconsistent with its own sparkline (77 marks / 21 losses) and with its own
eight-row table. The 26 rows below are a highlight ledger and are labelled as one.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2012-12-16", promo="WWE", type="tag", landmark=True,
         event="TLC", opponent="Team Hell No (Daniel Bryan & Kane) & Ryback",
         stip="TLC match — The Shield’s first match", title=""),
    dict(result="W", date="2015-01-25", promo="WWE",
         event="Royal Rumble", opponent="John Cena", opponent_html=True,
         stip="Singles", title=""),
    dict(result="L", date="2015-03-29", promo="WWE",
         event="WrestleMania 31", opponent="Randy Orton",
         stip="Singles — earlier the same night", title=""),
    dict(result="W", date="2015-03-29", promo="WWE", type="tag", landmark=True,
         event="WrestleMania 31 — Money in the Bank cash-in",
         opponent="Brock Lesnar & Roman Reigns",
         stip="Cash-in during the main event, turning it into a triple threat",
         title="WWE Championship"),
    dict(result="W", date="2015-08-23", promo="WWE", landmark=True,
         event="SummerSlam", opponent="John Cena", opponent_html=True,
         stip="Singles — holds the WWE and United States titles at once",
         title="United States Championship"),
    dict(result="L", date="2015-09-20", promo="WWE",
         event="Night of Champions", opponent="John Cena", opponent_html=True,
         stip="Singles — ends a 28-day reign", title="United States Championship"),
    dict(result="W", date="2016-06-19", promo="WWE", landmark=True,
         event="Money in the Bank", opponent="Roman Reigns", opponent_html=True,
         stip="Singles — second WWE Championship", title="WWE Championship"),
    dict(result="L", date="2016-06-19", promo="WWE", landmark=True,
         event="Money in the Bank — cash-in", opponent="Dean Ambrose",
         stip="Cash-in minutes later — reign of roughly two minutes",
         title="WWE Championship"),
    dict(result="L", date="2017-01-28", promo="WWE",
         event="Royal Rumble", opponent="AJ Styles", opponent_html=True,
         stip="Singles", title=""),
    dict(result="W", date="2018-08-19", promo="WWE",
         event="SummerSlam", opponent="Dolph Ziggler",
         stip="Singles — 119-day reign begins", title="Intercontinental Championship"),
    dict(result="L", date="2018-12-16", promo="WWE",
         event="TLC", opponent="Dean Ambrose", stip="Singles",
         title="Intercontinental Championship"),
    dict(result="W", date="2019-04-07", promo="WWE", landmark=True,
         event="WrestleMania 35", opponent="Brock Lesnar",
         stip="Singles — opens the show, ends the Lesnar reign",
         title="Universal Championship"),
    dict(result="L", date="2019-07-14", promo="WWE",
         event="Extreme Rules", opponent="Brock Lesnar",
         stip="Money in the Bank cash-in — ends a 98-day reign",
         title="Universal Championship"),
    dict(result="W", date="2019-08-11", promo="WWE", landmark=True,
         event="SummerSlam", opponent="Brock Lesnar",
         stip="Singles — first man to beat Lesnar at both WrestleMania and SummerSlam",
         title="Universal Championship"),
    dict(result="L", date="2019-10-31", promo="WWE",
         event="Crown Jewel", opponent="“The Fiend” Bray Wyatt",
         stip="Falls Count Anywhere", title="Universal Championship"),
    dict(result="W", date="2022-10-10", promo="WWE",
         event="Raw", opponent="Bobby Lashley", stip="Singles",
         title="United States Championship"),
    dict(result="L", date="2022-11-26", promo="WWE",
         event="Survivor Series WarGames", opponent="Austin Theory",
         stip="Triple threat — ends a 47-day reign", title="United States Championship"),
    dict(result="W", date="2023-05-27", promo="WWE", landmark=True,
         event="Night of Champions — Jeddah", opponent="AJ Styles", opponent_html=True,
         stip="Tournament final — inaugural champion",
         title="World Heavyweight Championship"),
    dict(result="L", date="2024-04-06", promo="WWE", landmark=True,
         event="WrestleMania XL Night 1", opponent="Cody Rhodes", opponent_html=True,
         stip="Night 1 main event — the 45-minute match", title=""),
    dict(result="L", date="2024-04-07", promo="WWE", landmark=True,
         event="WrestleMania XL Night 2", opponent="Damian Priest",
         stip="Money in the Bank cash-in — ends the 316-day reign",
         title="World Heavyweight Championship"),
    dict(result="W", date="2025-06-07", promo="WWE", type="tag",
         event="Money in the Bank", opponent="The 2025 Money in the Bank ladder match field",
         stip="Ladder match — his second briefcase", title=""),
    dict(result="W", date="2025-08-02", promo="WWE", landmark=True,
         event="SummerSlam Night 1 — MetLife Stadium", opponent="CM Punk", opponent_html=True,
         stip="Cash-in on crutches, minutes after Punk won it",
         title="World Heavyweight Championship"),
    dict(result="W", date="2025-10-11", promo="WWE", landmark=True,
         event="Crown Jewel — Perth", opponent="Cody Rhodes", opponent_html=True,
         stip="Singles — first singles win over Rhodes; the shoulder goes",
         title="WWE Crown Jewel Championship"),
    dict(result="L", date="2026-05-09", promo="WWE",
         event="Backlash", opponent="Bron Breakker",
         stip="Singles — Heyman interference", title=""),
    dict(result="W", date="2026-06-27", promo="WWE",
         event="Night of Champions — Riyadh", opponent="Bron Breakker",
         stip="Steel cage — finished with a Stomp off the top", title=""),
    dict(result="L", date="2026-08-02", promo="WWE", landmark=True,
         event="SummerSlam Night 2 — U.S. Bank Stadium", opponent="Roman Reigns",
         opponent_html=True, stip="Singles — clean; both men closed the story afterwards",
         title="World Heavyweight Championship"),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"John Cena": "john-cena", "Roman Reigns": "roman-reigns",
                 "AJ Styles": "aj-styles", "Cody Rhodes": "cody-rhodes",
                 "CM Punk": "cm-punk"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="seth-rollins",
    name="Seth Rollins",
    realname="Colby Daniel Lopez",
    epithet="The Visionary",
    hook="Record & Titles",

    meta_desc=("Seth Rollins, The Visionary, is a six-time WWE world champion whose 316-day inaugural "
               "World Heavyweight Championship reign is still the record for that belt. Full record, "
               "titles, factions, personas and career — including the 2025 knee injury that was a work."),
    og_desc=("The Visionary: 6 world title reigns, the 316-day inaugural World Heavyweight Championship "
             "run, the only WrestleMania main-event cash-in, and the July 2025 injury that was an angle."),
    tw_desc=("The Visionary: 6 world titles, a record 316-day World Heavyweight reign, and the fake knee "
             "injury that fooled mainstream sports media."),

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2004",
    height_imp="6&#8242;1&#8243;",
    weight_lb="225",
    world_titles="6",
    vitals_tagline="Burn it down",
    support_note="Merch &middot; Games &middot; School",
    x_url="https://x.com/WWERollins",
    ig_url="https://www.instagram.com/wwerollins/",
    sp_items=[
        dict(ic="SR", title="Seth Rollins Merch", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K18", sub="Cover Superstar, 2017",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="BB", title="Black and Brave", sub="Wrestling academy he co-owns",
             tag="Train", charity=True, href="https://www.blackandbrave.com/"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit",
             href="https://www.wwe.com/superstars/seth-rollins"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Architect &middot; The Kingslayer &middot; The Monday Night Messiah",
    hero_tag="Davenport, Iowa &middot; <em>ROH &middot; WWE &middot; 2004&ndash;present</em>",
    now_label="NOW",
    now_bold="WWE Crown Jewel Champion",
    now_tail=" &middot; no weekly-brand title, and no announced next match as of August 23, 2026",
    hstats=[
        dict(value="6",   x=True,  label="World Titles"),
        dict(value="316", x=False, label="Day World Heavyweight Reign"),
        dict(value="3",   x=False, label="WrestleMania Main Events"),
        dict(value="2",   x=True,  label="Money in the Bank Wins"),
    ],
    ghost_link="From Tyler Black to The Vision",
    vlabel="Est. 2004 &middot; Davenport, IA",
    mono="SR",

    # ---------------------------------------------------------------- 01 overview
    overview=[
        "<b>Seth Rollins</b> is the hinge WWE reaches for when it wants a story to turn. Six world title "
        "reigns &mdash; two WWE Championships, two Universal Championships, two World Heavyweight "
        "Championships &mdash; sit alongside the two things nobody else has: the only Money in the Bank "
        "cash-in ever executed inside a WrestleMania main event, on March 29, 2015, and a 316-day inaugural "
        "reign with the 2023 World Heavyweight Championship that is still the record for that belt as of "
        "August 2026. He is also the inaugural NXT Champion, WWE&rsquo;s 29th Triple Crown and 19th Grand "
        "Slam winner, a two-time Money in the Bank holder (2014 and 2025), the 2019 Royal Rumble winner, and "
        "a three-time PWI 500 number one.",

        "The correction this page exists to make: <b>the July 2025 knee injury was a work</b>, and the "
        "databases logging it as a fact are logging an angle. Rollins faked the injury on July 12, 2025 at "
        "Saturday Night&rsquo;s Main Event in Atlanta, landing awkwardly off a moonsault against LA Knight. "
        "Four days later, on July 16, he took it to <i>The Rich Eisen Show</i> &mdash; a mainstream sports "
        "programme, not a wrestling one &mdash; and described specialists in Birmingham, Alabama and an "
        "extended period on the shelf; it became that show&rsquo;s most-watched July content. Fewer than ten "
        "people knew, among them his wife Becky Lynch and Paul Heyman. The ruse ended at SummerSlam on "
        "August 2, 2025: he came out on crutches after CM Punk won the World Heavyweight Championship, "
        "dropped them, and cashed in Money in the Bank. Rollins laid the whole thing out to ESPN in a piece "
        "published September 18, 2025. His <b>real</b> injury came three months later &mdash; the shoulder, "
        "in the Crown Jewel win over Cody Rhodes in Perth on October 11, 2025. That is what forced the "
        "World Heavyweight Championship vacancy on the October 20, 2025 Raw and cost him roughly four "
        "months. The knee cost him nothing.",

        "He was born Colby Daniel Lopez on May 28, 1986 in Iowa, trained at Danny Daniels&rsquo; school on "
        "the Chicago/Oak Park border, and debuted on August 21, 2004 as &ldquo;Gixx.&rdquo; From 2005 to "
        "2010 he was <b>Tyler Black</b> on the American independents &mdash; Ring of Honor, Full Impact Pro, "
        "Pro Wrestling Guerrilla &mdash; a founding figure in the Age of the Fall, ROH World Champion for "
        "210 days and a two-time ROH World Tag Team Champion with Jimmy Jacobs. WWE signed him to Florida "
        "Championship Wrestling, and he became the first NXT Champion in the Gold Rush tournament final: "
        "the taping was July 26, 2012, the broadcast August 29, and only the August 29 date squares with the "
        "133-day length both databases agree on. The Shield debuted at Survivor Series on November 18, 2012; "
        "Rollins ended it with a chair on the June 2, 2014 Raw and walked into The Authority as its "
        "protected champion.",

        "The modern run is three peaks and one reset. He beat Brock Lesnar for the Universal Championship at "
        "WrestleMania 35 and again at SummerSlam 2019 &mdash; the first man to beat Lesnar at both. He beat "
        "AJ Styles in Jeddah on May 27, 2023 to become the inaugural World Heavyweight Champion and held it "
        "316 days as Seth &ldquo;Freakin&rdquo; Rollins. Then, after WrestleMania 41 in April 2025, he "
        "turned heel with Paul Heyman and built <b>The Vision</b> with Bron Breakker and Bronson Reed &mdash; "
        "the stable that turned on him during his shoulder layoff and holds the World Tag Team Championship "
        "without him. He returned on March 1, 2026 at Elimination Chamber, hunted his own group through "
        "Backlash and Night of Champions, and lost cleanly to Roman Reigns in the SummerSlam Night 2 main "
        "event on August 2, 2026 &mdash; a match both men and the press treated as the ending of the story "
        "the 2014 chair shot started. He is 40, holds the annually-defended WWE Crown Jewel Championship, "
        "and has no announced next match.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full highlight ledger",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("6&times;",  "World titles"),
            ("316",       "Longest reign (days)"),
            ("2&times;",  "Money in the Bank"),
            ("1&times;",  "Royal Rumble"),
            ("3",         "WrestleMania main events"),
            ("29th",      "Triple Crown"),
        ],
        lead=("Twenty-six documented bouts &mdash; every world and secondary title change with a sourced "
              "date, plus the matches that turned the character. <b>This is a highlight subset, not a "
              "complete career count.</b> The previous version of this page carried an 81&ndash;58 career "
              "headline that did not agree with its own eight-row table or its own sparkline, so no career "
              "win&ndash;loss total is published here rather than guessed. Bouts without a day-precise "
              "sourced date &mdash; the 2014 Money in the Bank win, the 2019 Royal Rumble, the WrestleMania "
              "33 win over Triple H &mdash; are covered in the timeline instead of being dated by "
              "inference. Filter by match type, tap any column header to sort, and turn spoilers on to "
              "reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The three matches the previous edition of this file rated highest, carried over "
                    "unchanged (Meltzer / Cagematch, as reported). The ratings are that file&rsquo;s; two of "
                    "the title claims attached to them do not survive the sources, and are corrected in "
                    "The Record and Championships."),
    signature=[
        dict(rating="5.0", event="WrestleMania XL Night 1", opponent="Cody Rhodes",
             stip="Night 1 main event, 45 minutes — logged as a title match by the old file",
             url="/wrestlers/cody-rhodes/"),
        dict(rating="4.5", event="Royal Rumble 2015", opponent="John Cena",
             stip="Singles — the best Cena performance of that year",
             url="/wrestlers/john-cena/"),
        dict(rating="4.5", event="Monday Night Raw, October 27, 2014", opponent="Shawn Michaels",
             stip="Singles — a surprise television match"),
    ],
    signature_count_word="three",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("6&times;", "World title reigns"),
            ("2&times;", "Money in the Bank"),
            ("29th",     "Triple Crown"),
            ("19th",     "Grand Slam"),
        ],
        lead=("Six world championship reigns across three belts, plus the secondary, tag and pre-WWE gold "
              "that made him a two-time Grand Slam champion. Reign counts and lengths for Rollins are one "
              "of the messier records in WWE: where Wikipedia, ESPN, TheSportster and wrestlingprofiles "
              "disagree, both figures are printed rather than one being quietly chosen."),
        rows=[
            dict(ic="W", name="WWE Championship", count="2",
                 sub="2015 &mdash; the WrestleMania 31 cash-in, vacated in November after a torn ACL and "
                     "MCL, never beaten out of him. <b>Length disputed:</b> 219 days recognised by WWE and "
                     "221 days held per Wikipedia, 221 per wrestlingprofiles, 220 in common press use. "
                     "&middot; 2016 &mdash; won from Roman Reigns at Money in the Bank and lost the same "
                     "night to Dean Ambrose&rsquo;s cash-in; roughly two minutes, the shortest reign in the "
                     "title&rsquo;s history short of Andr&eacute; the Giant&rsquo;s 1988 minute and 48 seconds."),
            dict(ic="U", name="WWE Universal Championship", count="2",
                 sub="2019 &mdash; def. Brock Lesnar at WrestleMania 35, 98 days, ended by Lesnar&rsquo;s "
                     "Extreme Rules cash-in &middot; 2019 &mdash; def. Lesnar again at SummerSlam, "
                     "<b>80 days (TheSportster) or 81 (wrestlingprofiles)</b>, lost to &ldquo;The "
                     "Fiend&rdquo; Bray Wyatt at Crown Jewel"),
            dict(ic="H", name="World Heavyweight Championship", count="2",
                 sub="2023&ndash;24 &mdash; inaugural champion, def. AJ Styles in Jeddah, <b>316 days</b>, "
                     "still the longest reign in the belt&rsquo;s history in August 2026; ended by Damian "
                     "Priest&rsquo;s cash-in at WrestleMania XL Night 2 on April 7, 2024. The previous "
                     "version of this page instead logged the reign ending to Cody Rhodes on Night 1, which "
                     "cannot be reconciled with a 316-day reign, so the Night 1 bout carries no title here. "
                     "&middot; 2025 &mdash; 79 days, taken from CM Punk by cash-in at SummerSlam and "
                     "vacated on the October 20 Raw after the shoulder injury"),
            dict(ic="I", name="WWE Intercontinental Championship", count="2",
                 sub="2018, 71 days from WrestleMania 34 &middot; 2018, 119 days from SummerSlam over Dolph "
                     "Ziggler, lost to Dean Ambrose at TLC. <b>Count disputed:</b> ESPN and TheSportster "
                     "both say two-time; the Wikipedia article&rsquo;s summary line reads &ldquo;once.&rdquo; "
                     "Two independent sources against one, and the two-reign version is the one with dates "
                     "attached, so it is used here."),
            dict(ic="S", name="WWE United States Championship", count="2",
                 sub="2015, 28 days &mdash; won from John Cena at SummerSlam while WWE Champion; ESPN calls "
                     "him the only superstar to hold both at once, a claim this file could not "
                     "independently verify and publishes as ESPN&rsquo;s &middot; 2022, 47 days &mdash; won "
                     "from Bobby Lashley on Raw, lost to Austin Theory at Survivor Series WarGames"),
            dict(ic="T", name="WWE / Raw Tag Team Championship", count="6",
                 sub="<b>Count disputed:</b> Wikipedia enumerates six reigns, ESPN&rsquo;s profile says "
                     "&ldquo;five-time Raw Tag Team Champion with various partners.&rdquo; Partners across "
                     "them: Roman Reigns, Dean Ambrose, Jason Jordan, Braun Strowman and Buddy Murphy. "
                     "Individual reign dates and lengths are not verified in this file."),
            dict(ic="N", name="NXT Championship", count="1",
                 sub="Inaugural champion, won in the Gold Rush tournament final, 133 days, lost January 9, "
                     "2013. <b>Date disputed:</b> wrestlingprofiles lists July 26, 2012, the taping; "
                     "TheSportster lists August 29, 2012, the broadcast. Only August 29 is arithmetically "
                     "consistent with the 133 days both give."),
            dict(ic="C", name="WWE Crown Jewel Championship", count="1",
                 sub="Current &middot; won October 11, 2025 in Perth from Cody Rhodes, his first career "
                     "singles win over him &middot; an annual title defended once a year, so it is not a "
                     "weekly-television championship"),
            dict(ic="R", name="ROH World Championship", count="1",
                 sub="2010, as Tyler Black &middot; 210 days (Wikipedia) &middot; the reign that made him "
                     "the most obvious independent signing of his year"),
            dict(ic="R", name="ROH World Tag Team Championship", count="2",
                 sub="With Jimmy Jacobs, out of the Age of the Fall &middot; individual reign lengths not "
                     "verified"),
            dict(ic="F", name="FIP, PWG and FCW championships", count="4",
                 sub="FIP World Heavyweight Championship &middot; PWG World Tag Team Championship &middot; "
                     "FCW Florida Heavyweight Championship &middot; FCW Jack Brisco 15 Championship, "
                     "completing the FCW Grand Slam &middot; dates and lengths not verified"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Five groups across twenty years &mdash; and in three of them, the betrayal is the whole point.",
        cards=[
            dict(era="ROH &middot; 2007&ndash;2009",
                 name="The Age of the Fall",
                 members="Tyler Black, Jimmy Jacobs",
                 desc="His breakout independent group, alongside Jimmy Jacobs. Black won the ROH World Tag "
                      "Team Championship twice with Jacobs out of it and went on from there to the ROH "
                      "World Championship — the run that got him signed."),
            dict(era="WWE &middot; 2012&ndash;14, reunions 2017, 2018 and 2019",
                 name="The Shield",
                 members="Seth Rollins, Roman Reigns, Dean Ambrose",
                 desc="Debuted as an interference unit at Survivor Series on November 18, 2012; their first "
                      "actual match was at TLC on December 16, 2012, beating Team Hell No and Ryback. A "
                      "three-man attack squad in tactical gear that entered through the crowd, initially "
                      "aligned in storyline with CM Punk. Rollins ended it on the June 2, 2014 Raw with a "
                      "chair to Reigns and Ambrose. Reunited twice around Ambrose's returns and once more "
                      "in 2019."),
            dict(era="WWE &middot; 2013&ndash;16",
                 name="The Authority",
                 members="Triple H, Stephanie McMahon, Seth Rollins, Kane, Jamie Noble, Joey Mercury",
                 desc="Triple H and Stephanie McMahon's on-screen regime. Rollins joined at the moment of "
                      "the Shield betrayal and became its protected champion, carrying the Money in the "
                      "Bank briefcase with Noble and Mercury as handlers. This is the run that converted "
                      "him from one third of a trio into a top-of-the-card singles heel — and he spent "
                      "2016 and 2017 dismantling it."),
            dict(era="WWE &middot; 2019&ndash;20",
                 name="AOP / the Monday Night Messiah group",
                 members="Seth Rollins, Akam, Rezar, Buddy Murphy",
                 desc="Rollins with the Authors of Pain and Buddy Murphy: a cult-flavoured heel unit that "
                      "beat down Kevin Owens, The Big Show and Rey Mysterio. It existed to give the Messiah "
                      "character disciples, and it disbanded when AOP left television."),
            dict(era="WWE &middot; 2025&ndash;present",
                 name="The Vision",
                 members="Seth Rollins (founder), Paul Heyman, Bron Breakker, Bronson Reed, Logan Paul, "
                         "Austin Theory",
                 desc="Formed after WrestleMania 41 in April 2025 when Rollins turned heel with Paul "
                      "Heyman. It won Money in the Bank and the World Heavyweight Championship inside three "
                      "months, took a WarGames match at Survivor Series on November 29, 2025, and added "
                      "Logan Paul and Austin Theory late that year. Then it turned on the man who built it "
                      "during his shoulder layoff. As of August 2026 The Vision is still active and still "
                      "holding the World Tag Team Championship — regained July 6, 2026 — with Rollins as "
                      "its enemy; Heyman has since left the group on Raw and named a replacement."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead=("One performer, four complete rebuilds. Databases list Visionary, Architect, Messiah and "
              "Revolutionary side by side as if they were nicknames &mdash; they are separate eras with "
              "different acts inside them."),
        cards=[
            dict(mono="TB", era="ROH / FIP / PWG &middot; 2005&ndash;2010", name="Tyler Black",
                 desc="The independent decade. Long-haired high-flyer turned Age of the Fall heel, ROH "
                      "World Champion for 210 days and two-time ROH World Tag Team Champion with Jimmy "
                      "Jacobs. Before that, one year as “Gixx” from his August 21, 2004 debut."),
            dict(mono="AR", era="WWE &middot; 2014&ndash;16", name="The Architect",
                 desc="Post-betrayal. Slicked back, suited, Authority-protected, briefcase in hand, winning "
                      "with help — the name was coined for him because he designed the Shield's collapse. "
                      "It produced the WrestleMania 31 cash-in and the simultaneous WWE and United States "
                      "Championship run of late 2015."),
            dict(mono="MM", era="WWE &middot; 2020", name="The Monday Night Messiah",
                 desc="The heel reinvention after the 2019 babyface peak: sermonising cult leader with AOP "
                      "and Buddy Murphy as disciples, “greater good” rhetoric, and the Rey Mysterio eye "
                      "angle. The most disliked version of the character and the one that proved he could "
                      "restart from nothing."),
            dict(mono="SF", era="WWE &middot; 2022&ndash;24", name="Seth “Freakin” Rollins",
                 desc="The mainstream-crossover version, officially renamed by WWE: garish suits, a "
                      "singalong entrance theme the whole building performs, laughing showman. Grew out of "
                      "the manic 2021–22 Visionary and carried the inaugural World Heavyweight "
                      "Championship for its record 316 days."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Davenport to the independents to the man WWE turns its stories on.",
        rows=[
            dict(year="2004", title="Debut as “Gixx”",
                 desc="Debuts August 21, 2004 on the Midwest independents after training at Danny Daniels' "
                      "school on the Chicago/Oak Park border."),
            dict(year="2010", title="ROH World Champion as Tyler Black",
                 desc="A 210-day reign that made him the most obvious WWE signing on the independents that "
                      "year."),
            dict(year="2012", title="Inaugural NXT Champion, then The Shield",
                 desc="Wins the first NXT Championship in the Gold Rush tournament final, aired August 29, "
                      "2012; debuts with Roman Reigns and Dean Ambrose at Survivor Series on November 18."),
            dict(year="2014", title="The betrayal, and the briefcase",
                 desc="Turns on The Shield with a chair on the June 2, 2014 Raw and joins The Authority; "
                      "wins Money in the Bank the same year."),
            dict(year="2015", title="The WrestleMania 31 cash-in",
                 desc="Cashes in during the March 29, 2015 main event to take the WWE Championship, adds "
                      "the United States title at SummerSlam, and tops the PWI 500 as Wrestler of the Year."),
            dict(year="2017", title="The Kingslayer",
                 desc="Beats Triple H in a non-sanctioned match at WrestleMania 33, completing the "
                      "babyface turn and finishing the Authority story he started."),
            dict(year="2019", title="Beats Brock Lesnar twice for the Universal Championship",
                 desc="Wins the Royal Rumble in January, then beats Lesnar at WrestleMania 35 on April 7 "
                      "and again at SummerSlam on August 11 — the first man to do both."),
            dict(year="2023", title="Inaugural World Heavyweight Champion",
                 desc="Beats AJ Styles on May 27, 2023 in Jeddah and holds the new belt 316 days, still its "
                      "record; PWI 500 number one and Wrestler of the Year for the second time."),
            dict(year="2025", title="The Vision, the fake injury, the cash-in",
                 desc="Turns heel with Paul Heyman after WrestleMania 41; wins Money in the Bank on June 7; "
                      "fakes a knee injury from July 12; cashes in on CM Punk at SummerSlam on August 2 for "
                      "the World Heavyweight Championship."),
            dict(year="2025", title="The real injury, and the Crown Jewel win",
                 desc="Beats Cody Rhodes on October 11 in Perth for the Crown Jewel Championship — his "
                      "first singles win over Rhodes — and hurts his shoulder doing it; the World "
                      "Heavyweight Championship is vacated on the October 20 Raw."),
            dict(year="2026", title="Return, revenge, and the Reigns coda",
                 desc="Returns March 1 at Elimination Chamber; loses to Bron Breakker at Backlash on May 9, "
                      "beats him in a steel cage at Night of Champions on June 27, and loses to Roman "
                      "Reigns in the SummerSlam Night 2 main event on August 2."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with &mdash; and who he sold out.",
        cards=[
            dict(name="Roman Reigns", slug="roman-reigns",
                 desc="Twelve years from the same chair shot, and the only WWE feud of the era with that "
                      "much accumulated history to spend. It peaked at SummerSlam Night 2 on August 2, "
                      "2026 in Minneapolis: Reigns won clean, the two bumped fists afterwards, and CBS "
                      "Sports, ESPN and Yahoo all read it as a deliberate close rather than a pause. CBS "
                      "graded it A+ and called it the match of the weekend. It matters because it finally "
                      "gives the 2014 split an ending, after WWE restarted and abandoned it across 2015, "
                      "2016 and 2022."),
            dict(name="Dean Ambrose / Jon Moxley",
                 desc="The immediate consequence of the betrayal, and the reason the split worked. Ambrose "
                      "chased him through Hell in a Cell 2014 and a Lumberjack match, and took the "
                      "Intercontinental Championship off him at TLC on December 16, 2018. Their June 19, "
                      "2016 sequence — Rollins beats Reigns for the WWE Championship, Ambrose cashes in on "
                      "Rollins minutes later — is the densest Shield-trio moment in WWE history and gave "
                      "Rollins his two-minute reign."),
            dict(name="Triple H and The Authority", slug="triple-h",
                 desc="Rollins spent 2014 and 2015 as the regime's protected champion, then spent 2016 and "
                      "2017 dismantling it; the non-sanctioned WrestleMania 33 match produced The "
                      "Kingslayer. It is the rare WWE long-form story where the same performer is the "
                      "authority figure's weapon and then his executioner."),
            dict(name="Brock Lesnar",
                 desc="The WrestleMania 31 cash-in happened inside a Lesnar match, and in 2019 Rollins beat "
                      "him for the Universal Championship at WrestleMania 35 and again at SummerSlam. "
                      "Wikipedia records him as the first man to beat Lesnar at both events — the "
                      "credential that moved him from great worker to the guy who beats the monster."),
            dict(name="CM Punk", slug="cm-punk",
                 desc="Rollins ended Punk's five-minute-and-ten-second World Heavyweight Championship reign "
                      "on August 2, 2025 with the cash-in that resolved the three-week worked-shoot injury "
                      "angle. They had also main-evented WrestleMania 41 Night 1 in a triple threat with "
                      "Roman Reigns, which Rollins won. It is the clearest example of WWE using Rollins as "
                      "its designated storyline detonator rather than as a champion in his own right."),
            dict(name="Bron Breakker and The Vision",
                 desc="The stable he built turned on him during his real injury layoff. Breakker beat him "
                      "at Backlash on May 9, 2026 with Heyman interference, and Rollins beat Breakker "
                      "inside a steel cage at Night of Champions on June 27, finishing with a Stomp off the "
                      "top. It matters because it is the first time the betrayal in a Rollins story ran in "
                      "the other direction."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Beyond the ring &mdash; and one appearance that was part of the act.",
        rows=[
            dict(when="2025", title="The Rich Eisen Show", kind="TV",
                 desc="July 16, 2025. Four days after faking the knee injury, Rollins went on a mainstream "
                      "sports programme and described specialists in Birmingham, Alabama and an extended "
                      "absence. Per ESPN's account it became the show's most-watched July content. It is "
                      "the most successful piece of media work of his career and none of it was true."),
            dict(when="2017", title="WWE 2K18", kind="Game",
                 desc="Cover Superstar, reported by ESPN and announced by Rollins himself. Playable "
                      "throughout the WWE 2K series."),
            dict(when="2015&ndash;", title="WWE 24 and WWE Chronicle", kind="TV",
                 desc="WWE Network and Peacock documentary episodes centred on him, credited on IMDb under "
                      "his legal name, Colby Lopez."),
            dict(when="2017", title="The Jetsons & WWE: Robo-WrestleMania!", kind="Film",
                 desc="Voice role. No scripted film or television credits beyond this are verified — IMDb "
                      "lists 260 credits under Colby Lopez, but the itemised table could not be fetched and "
                      "the vast majority are wrestling broadcasts. No autobiography and no hosted podcast "
                      "is confirmed to exist."),
            dict(when="Ongoing", title="Black and Brave Wrestling Academy", kind="Business",
                 desc="Co-owner of a wrestling school. Location conflict worth noting: ESPN's profile "
                      "places it in Illinois, while it is widely reported elsewhere as Davenport, Iowa. "
                      "Unresolved here."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated the way the sources actually state them &mdash; conflicts included.",
        stats=[
            ("316", "Days as World Heavyweight Champion"),
            ("2",   "Money in the Bank wins"),
            ("3",   "WrestleMania main events"),
        ],
        rows=[
            dict(name="The longest World Heavyweight Championship reign: 316 days",
                 sub="May 27, 2023 to April 7, 2024, as the belt's inaugural champion. Still the record as "
                     "of August 23, 2026 — Roman Reigns' current reign, from April 19, 2026, stands at 126 "
                     "days. Agreed by Wikipedia, wrestlingprofiles and TheSportster."),
            dict(name="The only Money in the Bank cash-in in a WrestleMania main event",
                 sub="March 29, 2015 at Levi's Stadium, converting Brock Lesnar vs. Roman Reigns into a "
                     "triple threat and winning the WWE Championship out of it. First and, to date, only."),
            dict(name="The July 2025 knee injury was a work, not an injury",
                 sub="Faked on July 12, 2025 against LA Knight at Saturday Night's Main Event, sold to "
                     "mainstream sports media on The Rich Eisen Show on July 16, and revealed at SummerSlam "
                     "on August 2 when he dropped the crutches and cashed in on CM Punk. Fewer than ten "
                     "people knew. Any database logging a 2025 knee injury against his record is logging an "
                     "angle as fact; the injury that actually cost him a title and four months was the "
                     "shoulder, on October 11, 2025."),
            dict(name="The only man to beat Brock Lesnar at both WrestleMania and SummerSlam",
                 sub="WrestleMania 35 on April 7, 2019 and SummerSlam on August 11, 2019, both for the "
                     "Universal Championship (Wikipedia)."),
            dict(name="Inaugural champion twice over",
                 sub="First NXT Champion in 2012 and first World Heavyweight Champion under the 2023 "
                     "revival. No one else holds both."),
            dict(name="Two Money in the Bank wins, eleven years apart",
                 sub="2014 and June 7, 2025 — and both were cashed in successfully, in 2015 and 2025."),
            dict(name="2019 Royal Rumble winner",
                 sub="Won in January 2019 and headlined WrestleMania 35 out of it."),
            dict(name="29th Triple Crown and 19th Grand Slam Champion",
                 sub="And the second wrestler to complete the Grand Slam twice under the revised 2015 "
                     "format (Wikipedia)."),
            dict(name="Three WrestleMania main events",
                 sub="WrestleMania 31, WrestleMania 40 Night 1 and WrestleMania 41 Night 1 (Wikipedia)."),
            dict(name="PWI 500 number one three times; Wrestler of the Year twice",
                 sub="Number one in 2015, 2019 and 2023; PWI Wrestler of the Year in 2015 and 2023. He "
                     "placed 8th on the 2025 list, behind Cody Rhodes at number one. The 2026 list had not "
                     "been published as of August 23, 2026; PWI normally publishes in September."),
            dict(name="Sports Illustrated Wrestler of the Year, 2022",
                 sub="No Wrestling Observer Newsletter headline award is claimed here: Rollins won none of "
                     "the 2025 categories — Wrestler of the Year went to Místico, Match of the Year to "
                     "Kenny Omega vs. Gabe Kidd — and his historical Observer record is not verified in "
                     "this file."),
            dict(name="2016 WWE Draft: number one overall pick",
                 sub="Per ESPN's profile."),
            dict(name="Slammy Awards: 10 or 9",
                 sub="Wikipedia says 10, ESPN says 9. Unresolved, so both are printed."),
        ],
        footnote=("Two things this page deliberately does not publish. First, no career win-loss record: "
                  "the previous edition's 81-58 headline disagreed with its own match table and its own "
                  "sparkline, and no database total was independently readable for this file. Second, no "
                  "attendance or viewership record attached to Rollins specifically — none was citable, so "
                  "none is estimated. Where a number here is arithmetic rather than a citation, it is said "
                  "so: the 316-day Crown Jewel Championship reign current as of August 23, 2026 is computed "
                  "from the sourced October 11, 2025 win date, not quoted from a source."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="X / Twitter", v="@WWERollins", href="https://x.com/WWERollins"),
        dict(k="Instagram", v="@wwerollins", href="https://www.instagram.com/wwerollins/"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/seth-rollins"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Seth_Rollins"),
        dict(k="ESPN", v="How Rollins pulled off the injury ruse",
             href="https://www.espn.com/wwe/story/_/id/46292440/wrestlepalooza-wwe-wrestling-seth-rollins-knee-injury-angle-money-bank"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/seth-rollins.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Was Seth Rollins&rsquo; 2025 knee injury real?",
            a="No. It was a work, and it is the single most-mislogged fact about him. He faked it on "
              "<b>July 12, 2025</b> at Saturday Night&rsquo;s Main Event in Atlanta, landing awkwardly off "
              "a moonsault against LA Knight. On <b>July 16</b> he took it to <i>The Rich Eisen Show</i> "
              "&mdash; mainstream sports media, not wrestling media &mdash; and described specialists in "
              "Birmingham, Alabama and an extended spell out; it became that show&rsquo;s most-watched July "
              "content. Fewer than ten people knew, among them Becky Lynch and Paul Heyman. He revealed it "
              "at <b>SummerSlam on August 2, 2025</b>, walking out on crutches after CM Punk won the World "
              "Heavyweight Championship, dropping them and cashing in Money in the Bank. He confirmed all "
              "of it to ESPN in September 2025. Reference sites that log a &ldquo;2025 knee injury&rdquo; "
              "against his record are logging an angle as a fact.",
            q_ld="Was Seth Rollins' 2025 knee injury real?",
            a_ld="No. Seth Rollins' July 2025 knee injury was a worked storyline, not a real injury. Seth "
                 "Rollins faked the injury on July 12, 2025 at Saturday Night's Main Event in a match "
                 "against LA Knight, then maintained it in a mainstream interview on The Rich Eisen Show on "
                 "July 16, 2025, saying he had seen specialists in Birmingham, Alabama and would be out for "
                 "an extended period. Fewer than ten people knew, including Becky Lynch and Paul Heyman. "
                 "Seth Rollins revealed the ruse at SummerSlam on August 2, 2025 by dropping his crutches "
                 "and cashing in Money in the Bank on CM Punk, and confirmed the whole plan to ESPN in "
                 "September 2025."),
        dict(
            q="Why did Seth Rollins vacate the World Heavyweight Championship in 2025?",
            a="A real <b>shoulder</b> injury, sustained in his Crown Jewel win over Cody Rhodes in Perth on "
              "October 11, 2025. The title was vacated on the <b>October 20, 2025</b> Raw, and Jey Uso won "
              "a battle royal that night to face CM Punk for the vacant belt at Saturday Night&rsquo;s Main "
              "Event on November 1. Surgery kept Rollins out roughly four months; he returned on March 1, "
              "2026. Note that two explanations are in circulation and they are not the same claim: "
              "WWE.com&rsquo;s own bio gives the storyline reason &mdash; The Vision turned on him and "
              "forced him to relinquish it &mdash; rather than the shoulder.",
            q_ld="Why did Seth Rollins vacate the World Heavyweight Championship in 2025?",
            a_ld="Seth Rollins vacated the World Heavyweight Championship because of a real shoulder injury "
                 "sustained in his Crown Jewel match against Cody Rhodes in Perth on October 11, 2025. The "
                 "title was vacated on the October 20, 2025 episode of Raw, and Jey Uso won a battle royal "
                 "that night to challenge CM Punk for the vacant championship at Saturday Night's Main "
                 "Event on November 1, 2025. Seth Rollins had surgery and was out roughly four months, "
                 "returning on March 1, 2026. WWE's on-screen explanation instead blames The Vision's "
                 "betrayal for forcing him to relinquish the title."),
        dict(
            q="How many world championships has Seth Rollins won?",
            a="Six in WWE: two WWE Championships, two Universal Championships and two World Heavyweight "
              "Championships &mdash; plus one ROH World Championship before he signed, which most WWE-only "
              "counts leave out. He was the inaugural holder of both the NXT Championship in 2012 and the "
              "2023 World Heavyweight Championship, and his 316-day first reign with the latter is still "
              "the record for that belt.",
            q_ld="How many world championships has Seth Rollins won?",
            a_ld="Seth Rollins has won six world championships in WWE: two WWE Championships, two Universal "
                 "Championships and two World Heavyweight Championships. He also held the ROH World "
                 "Championship for 210 days before signing with WWE, wrestling as Tyler Black. Seth Rollins "
                 "was the inaugural holder of both the NXT Championship in 2012 and the 2023 World "
                 "Heavyweight Championship, and his 316-day first reign with the World Heavyweight "
                 "Championship remains the longest in that title's history."),
        dict(
            q="Is Seth Rollins a champion right now?",
            a="Yes, but not on weekly television. He holds the <b>WWE Crown Jewel Championship</b>, won from "
              "Cody Rhodes on October 11, 2025 &mdash; an annual title defended once a year, so he is not a "
              "champion in the Raw or SmackDown sense. He lost his World Heavyweight Championship challenge "
              "to Roman Reigns at SummerSlam Night 2 on August 2, 2026 and has no announced next match as "
              "of August 23, 2026. That Crown Jewel reign runs to 316 days on August 23, 2026 &mdash; a "
              "figure computed from the sourced win date, not quoted from a source.",
            q_ld="Is Seth Rollins a champion right now?",
            a_ld="Yes, but not a weekly-television champion. Seth Rollins holds the WWE Crown Jewel "
                 "Championship, which he won from Cody Rhodes on October 11, 2025 in Perth. That title is "
                 "defended once a year, so Seth Rollins holds no Raw or SmackDown championship. He lost his "
                 "World Heavyweight Championship challenge against Roman Reigns at SummerSlam Night 2 on "
                 "August 2, 2026 and has no announced next match as of August 23, 2026."),
        dict(
            q="How long was Seth Rollins&rsquo; first WWE Championship reign?",
            a="The sources do not agree, so here is the spread: <b>219 days</b> as recognised by WWE, "
              "<b>220</b> as commonly repeated in press, and <b>221</b> as Wikipedia&rsquo;s "
              "&ldquo;days held&rdquo; figure and wrestlingprofiles&rsquo; number. All start from the "
              "WrestleMania 31 cash-in on March 29, 2015 &mdash; TheSportster prints 221 but dates the "
              "reign from March 31, which is not the WrestleMania 31 date. It ended without a loss: he tore "
              "his ACL and MCL in Dublin in November 2015 and the title was vacated. His second WWE "
              "Championship reign is the opposite extreme, roughly two minutes on June 19, 2016 before "
              "Dean Ambrose cashed in.",
            q_ld="How long was Seth Rollins' first WWE Championship reign?",
            a_ld="Sources disagree. WWE recognises 219 days, press coverage commonly says 220, and "
                 "Wikipedia's days-held figure and wrestlingprofiles.com both say 221. All of them start "
                 "from Seth Rollins' Money in the Bank cash-in at WrestleMania 31 on March 29, 2015. The "
                 "reign ended without a defeat: Seth Rollins tore his ACL and MCL in Dublin in November "
                 "2015 and the WWE Championship was vacated. His second WWE Championship reign lasted "
                 "roughly two minutes on June 19, 2016 before Dean Ambrose cashed in Money in the Bank."),
        dict(
            q="What happened to The Vision?",
            a="Rollins founded it with Paul Heyman after WrestleMania 41 in April 2025, alongside Bron "
              "Breakker and Bronson Reed, adding Logan Paul after Survivor Series: WarGames and Austin "
              "Theory in late 2025. It won Money in the Bank, the World Heavyweight Championship and a "
              "WarGames match inside seven months &mdash; then turned on him around his October 2025 "
              "shoulder injury. It is still active in August 2026 and still holds the World Tag Team "
              "Championship, regained on July 6, 2026, with Rollins working against it rather than leading "
              "it. Heyman has since left the group on Raw and named a replacement.",
            q_ld="What happened to The Vision?",
            a_ld="Seth Rollins founded The Vision with Paul Heyman after WrestleMania 41 in April 2025, "
                 "alongside Bron Breakker and Bronson Reed, later adding Logan Paul and Austin Theory. The "
                 "group won Money in the Bank in June 2025, the World Heavyweight Championship in August "
                 "2025 and a WarGames match at Survivor Series in November 2025, then turned on Seth "
                 "Rollins around his October 2025 shoulder injury. The Vision remains active in August 2026 "
                 "and holds the World Tag Team Championship, regained on July 6, 2026, with Seth Rollins "
                 "now working against the stable he built. Paul Heyman has since left the group."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Colby Daniel Lopez"),
        dict(label="Born", value="May 28, 1986", sub="age 40"),
        dict(label="Birthplace", value="Davenport, Iowa",
             sub="Wikipedia and ESPN; TheSmackDownHotel says Buffalo, Iowa, a small town nearby"),
        dict(label="Billed from", value="Davenport, Iowa"),
        dict(label="Height", value="6&#8242;1&#8243;",
             sub="185 cm per WWE.com and ESPN; wrestlingprofiles says 6&#8242;3&#8243;"),
        dict(label="Weight", value="225 lb", sub="102 kg per WWE.com; 217 lb was the older billing"),
        dict(label="Debut", value="August 21, 2004", sub="independents, as Gixx"),
        dict(label="Main-roster debut", value="November 18, 2012", sub="Survivor Series, with The Shield"),
        dict(label="Trained by", value="Danny Daniels", sub="Chicago / Oak Park border"),
        dict(label="Finisher", value="The Stomp",
             sub="the only finisher WWE.com lists; Pedigree, Falcon Arrow, Buckle Bomb and Phoenix Splash "
                 "are widely associated but unverified here"),
        dict(label="Brand", value="Raw"),
        dict(label="Also known as",
             value="Tyler Black &middot; The Architect &middot; The Kingslayer &middot; The Monday Night "
                   "Messiah &middot; The Visionary &middot; Seth &ldquo;Freakin&rdquo; Rollins"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1986-05-28",
    bornplace="Davenport, Iowa, United States",
    nationality="United States",
    height_cm=185,
    weight_kg=102,
    ld=dict(
        alternateName=["Colby Daniel Lopez", "Tyler Black", "The Architect", "The Kingslayer",
                       "The Monday Night Messiah", "The Visionary", "Seth “Freakin” Rollins",
                       "Gixx"],
        award=["WWE Championship (2 reigns)",
               "WWE Universal Championship (2 reigns)",
               "World Heavyweight Championship (2 reigns, including a record 316-day inaugural reign)",
               "WWE Intercontinental Championship (2 reigns per ESPN and TheSportster; 1 per Wikipedia)",
               "WWE United States Championship (2 reigns)",
               "WWE Raw Tag Team Championship (6 reigns per Wikipedia; 5 per ESPN)",
               "NXT Championship (inaugural champion, 2012)",
               "WWE Crown Jewel Championship (1 reign, current)",
               "ROH World Championship (1 reign, as Tyler Black)",
               "ROH World Tag Team Championship (2 reigns, with Jimmy Jacobs)",
               "Money in the Bank winner (2014, 2025)",
               "Royal Rumble winner (2019)",
               "WWE Triple Crown Champion (29th)",
               "WWE Grand Slam Champion (19th, twice under the revised format)",
               "Pro Wrestling Illustrated 500 number one (2015, 2019, 2023)",
               "PWI Wrestler of the Year (2015, 2023)",
               "Sports Illustrated Wrestler of the Year (2022)"],
        knowsAbout=["Professional wrestling", "The Shield", "The Authority", "The Vision",
                    "Ring of Honor", "WWE", "Championship wrestling",
                    "Black and Brave Wrestling Academy"],
        description="Seth Rollins is an American professional wrestler signed to WWE. A six-time world "
                    "champion, he is the inaugural NXT Champion and the inaugural World Heavyweight "
                    "Champion under the 2023 revival, whose 316-day reign remains the longest in that "
                    "title's history. He is the only wrestler to cash in Money in the Bank during a "
                    "WrestleMania main event, doing so on March 29, 2015, and the first to beat Brock "
                    "Lesnar at both WrestleMania and SummerSlam. Wrestling as Tyler Black, he was ROH World "
                    "Champion before signing with WWE. His widely reported July 2025 knee injury was a "
                    "worked storyline revealed at SummerSlam on August 2, 2025; his real injury was a "
                    "shoulder injury on October 11, 2025 that forced him to vacate the World Heavyweight "
                    "Championship. He is the reigning WWE Crown Jewel Champion.",
        sameAs=["https://x.com/WWERollins",
                "https://www.instagram.com/wwerollins/",
                "https://en.wikipedia.org/wiki/Seth_Rollins",
                "https://www.wwe.com/superstars/seth-rollins"],
    ),
)
