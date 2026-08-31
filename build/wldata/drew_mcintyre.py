# -*- coding: utf-8 -*-
"""Drew McIntyre - dossier data.

Sources: web-verified August 31, 2026 (Wikipedia, Fightful, Bleacher Report, Yahoo
Sports, Sportsnaut/PWInsider). Every match row carries a day-precision date confirmed
in at least one of those sources.

Deliberate omissions:
  * No career win-loss total - no verified figure exists and none is invented.
  * A reported May 24, 2025 Saturday Night's Main Event steel cage loss to Damian
    Priest surfaced in only one automated read of Wikipedia and could not be
    corroborated; the row is left out rather than guessed at.
  * The date of the March 2026 title loss is published two ways: Wikipedia's title
    table gives March 6, 2026 (which produces the 56-day reign exactly), while a
    Yahoo Sports recap datelined the following morning says March 7. This module
    follows the arithmetic and flags the lag where the reign is described.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2020-01-26", promo="WWE", type="tag", landmark=True,
         event="Royal Rumble — Houston", opponent="The 2020 Royal Rumble field",
         stip="30-man Royal Rumble — eliminated Brock Lesnar on the way to the win", title=""),
    dict(result="W", date="2020-04-05", promo="WWE", landmark=True,
         event="WrestleMania 36 Night 2", opponent="Brock Lesnar",
         stip="Singles — first British WWE Champion, crowned in an empty Performance Center",
         title="WWE Championship"),
    dict(result="L", date="2020-10-25", promo="WWE",
         event="Hell in a Cell", opponent="Randy Orton",
         stip="Hell in a Cell — the 203-day reign ends", title="WWE Championship"),
    dict(result="W", date="2020-11-16", promo="WWE",
         event="Raw", opponent="Randy Orton",
         stip="Singles — regains the title 22 days later", title="WWE Championship"),
    dict(result="L", date="2021-02-21", promo="WWE", landmark=True,
         event="Elimination Chamber", opponent="The Miz",
         stip="Money in the Bank cash-in, minutes after McIntyre survived the Chamber",
         title="WWE Championship"),
    dict(result="L", date="2022-09-03", promo="WWE", landmark=True,
         event="Clash at the Castle — Cardiff", opponent="Roman Reigns",
         stip="Singles — challenge, before 62,000 in Wales",
         title="Undisputed WWE Universal Championship"),
    dict(result="L", date="2023-04-02", promo="WWE", type="tag",
         event="WrestleMania 39 Night 2", opponent="Gunther & Sheamus", opponent_html=True,
         stip="Triple threat — five stars (Meltzer); Gunther retains",
         title="WWE Intercontinental Championship"),
    dict(result="W", date="2024-04-07", promo="WWE", landmark=True,
         event="WrestleMania 40 Night 2", opponent="Seth Rollins",
         stip="Singles — first World Heavyweight Championship", title="World Heavyweight Championship"),
    dict(result="L", date="2024-04-07", promo="WWE", landmark=True,
         event="WrestleMania 40 Night 2", opponent="Damian Priest",
         stip="Money in the Bank cash-in — the reign ends at 5 minutes 46 seconds",
         title="World Heavyweight Championship"),
    dict(result="W", date="2024-08-03", promo="WWE",
         event="SummerSlam — Cleveland", opponent="CM Punk", opponent_html=True,
         stip="Singles — the feud's only McIntyre win", title=""),
    dict(result="L", date="2024-08-31", promo="WWE",
         event="Bash in Berlin", opponent="CM Punk", opponent_html=True,
         stip="Strap match", title=""),
    dict(result="L", date="2024-10-05", promo="WWE",
         event="Bad Blood", opponent="CM Punk", opponent_html=True,
         stip="Hell in a Cell — the blowoff", title=""),
    dict(result="W", date="2025-04-20", promo="WWE",
         event="WrestleMania 41 Night 2", opponent="Damian Priest",
         stip="Sin City Street Fight — Claymore into a chair-wrapped turnbuckle", title=""),
    dict(result="W", date="2026-01-09", promo="WWE", landmark=True,
         event="SmackDown", opponent="Cody Rhodes",
         stip="Three Stages of Hell — third WWE Championship, ending Rhodes' 159-day reign",
         title="Undisputed WWE Championship"),
    dict(result="W", date="2026-01-31", promo="WWE", landmark=True,
         event="Royal Rumble — Riyadh", opponent="Sami Zayn", opponent_html=True,
         stip="Singles — retains", title="Undisputed WWE Championship"),
    dict(result="L", date="2026-03-06", promo="WWE", landmark=True,
         event="SmackDown", opponent="Cody Rhodes",
         stip="Singles — Jacob Fatu strips the chair away; the 56-day reign ends",
         title="Undisputed WWE Championship"),
    dict(result="L", date="2026-04-18", promo="WWE", landmark=True,
         event="WrestleMania 42 Night 1 — Las Vegas", opponent="Jacob Fatu",
         stip="Unsanctioned match — his last bout to date", title=""),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"CM Punk": "cm-punk", "Sami Zayn": "sami-zayn",
                 "Gunther & Sheamus": "gunther"}[_r["opponent"]]
        _label = _r["opponent"]
        if _slug == "gunther":
            _r["opponent"] = ('<a class="opp-link" href="/wrestlers/gunther/">Gunther</a>'
                              ' &amp; Sheamus')
        else:
            _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _label)
        _r["opponent_html"] = True

DATA = dict(
    slug="drew-mcintyre",
    name="Drew McIntyre",
    realname="Andrew McLean Galloway IV",
    epithet="The Scottish Warrior",
    hook="Record & Titles",

    meta_desc=("Drew McIntyre is a four-time world champion in WWE, the first British WWE Champion, "
               "and the 2020 Royal Rumble winner. Full record, titles, factions, records and career."),
    og_desc=("The Scottish Warrior: three WWE Championship reigns, a World Heavyweight Championship "
             "that lasted 5 minutes 46 seconds, the 2020 Royal Rumble, and a second act built on being "
             "released and coming back better."),
    tw_desc="The Scottish Warrior: 4 WWE world title reigns, the 2020 Royal Rumble, and a 5:46 WHC reign.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2001",
    height_imp="6&#8242;5&#8243;",
    weight_lb="265",
    world_titles="4",
    vitals_tagline="The Chosen One, twice over",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="DM", title="WWE Shop", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable across the WWE 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="BK", title="A Chosen Destiny", sub="Autobiography, 2021",
             tag="Read", href="https://en.wikipedia.org/wiki/Drew_McIntyre"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/drew-mcintyre"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Chosen One &middot; The Scottish Psychopath &middot; formerly Drew Galloway",
    hero_tag="Ayr, Scotland &middot; <em>BCW &middot; WWE &middot; TNA &middot; ICW &middot; Evolve "
             "&middot; WWE again &middot; 2001&ndash;present</em>",
    now_label="NOW",
    now_bold="Away from WWE, filming",
    now_tail=" &middot; no match since the WrestleMania 42 unsanctioned loss to Jacob Fatu on April 18; "
             "shooting the Highlander reboot and The Last Druid, with no return written",
    hstats=[
        dict(value="4",    x=True,  label="World Title Reigns"),
        dict(value="203",  x=False, label="Day First WWE Reign"),
        dict(value="5:46", x=False, label="WHC Reign"),
        dict(value="1",    x=True,  label="Royal Rumble Win"),
    ],
    ghost_link="From the Chosen One to the empty-arena champion, twice around",
    vlabel="Est. 2001 &middot; Ayr, Scotland",
    mono="DM",

    # ---------------------------------------------------------------- 01 overview
    # index into overview of the correction paragraph -> the framed
    # "Setting one thing straight" callout (aside.corr) on the page
    correction=1,
    overview=[
        "<b>Drew McIntyre</b> is WWE&rsquo;s best argument that a failed pick can be re-picked. Vince "
        "McMahon anointed him &ldquo;The Chosen One&rdquo; on television in 2009, and by 2014 he had been "
        "repackaged into a comedy band and released. He rebuilt himself for three years on the "
        "independents and in TNA, came back through NXT, and in 2020 won the Royal Rumble and beat Brock "
        "Lesnar for the WWE Championship. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">4</span>'
        '<span class="pull-cap">world championship reigns in WWE &mdash; three WWE Championships and one World Heavyweight Championship</span></span>'
        "He is a 6&#8242;5&#8243; Scot who wrestles a power style built around the Claymore kick, "
        "the first British world champion in WWE history, and, as of August 2026, an absentee: he has "
        "not wrestled since losing an unsanctioned match to Jacob Fatu at WrestleMania 42 on April 18, "
        "and he is in Spain and a cutting room rather than a ring.",

        "The count you will read most often is &ldquo;two-time WWE Champion,&rdquo; and it stopped being "
        "true on January 9, 2026, when he beat Cody Rhodes in a Three Stages of Hell match on SmackDown "
        "for his third WWE Championship &mdash; his first world title since the 2024 reign that lasted "
        "5 minutes 46 seconds. The four world reigns break down as: 203 days from WrestleMania 36, when "
        "he beat Lesnar in an empty Performance Center at the start of the pandemic; 97 days after "
        "taking the title back from Randy Orton that November; the 5:46 World Heavyweight Championship "
        "reign at WrestleMania 40, ended by Damian Priest&rsquo;s Money in the Bank cash-in; and 56 days "
        "in 2026, ended by Rhodes on the March 6 SmackDown &mdash; a Yahoo recap datelined the next "
        "morning says March 7, but January 9 plus the recorded 56 days lands on March 6 exactly. Add "
        "the 2016 TNA World Heavyweight Championship and he has held five world titles across two "
        "companies.",

        "The first WWE run is the cautionary tale: signed at 22, championed on air by McMahon himself, "
        "Intercontinental Champion by the end of 2009 &mdash; and then four years of drift, 3MB, and a "
        "2014 release. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">5:46</span>'
        '<span class="pull-cap">the length of his World Heavyweight Championship reign &mdash; the cash-in at WrestleMania 40 that defined a year</span></span>'
        "What followed is the part he tells in his autobiography: as Drew Galloway he "
        "carried Evolve and ICW, took the TNA World Heavyweight Championship from Matt Hardy in March "
        "2016, and returned to WWE in 2017 to win the NXT Championship from Bobby Roode inside four "
        "months. The 2020 crowning was the redemption arc completed &mdash; won, surreally, with nobody "
        "in the building to see it, a fact he has been candid about ever since.",

        "The recent chapters run through other people&rsquo;s title reigns. He spent 2024 in a feud "
        "with CM Punk that produced three stipulation matches and one McIntyre win; he beat Priest in a "
        "Sin City Street Fight at WrestleMania 41 on April 20, 2025 to close that account; and his 2026 "
        "title win and title loss were both shaped by <b>Jacob Fatu</b> &mdash; a running collision that "
        "traces to a backstage attack in October 2025 which kept Fatu off television for months, and "
        "which ended, for now, with Fatu beating him in an unsanctioned match at WrestleMania 42. Since "
        "then, nothing: he is filming the Amazon MGM Highlander reboot and The Last Druid with Russell "
        "Crowe, PWInsider reports no talk of writing him back in, and this page treats him as what he "
        "currently is &mdash; a 41-year-old SmackDown wrestler on pause at the top of his game.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("4&times;",  "WWE world reigns"),
            ("203",       "Day first reign"),
            ("5:46",      "WHC reign"),
            ("1",         "Royal Rumble"),
            ("1",         "TNA World title"),
            ("2001",      "First match"),
        ],
        lead=("Seventeen documented bouts &mdash; the Rumble and the empty-arena crowning, every world "
              "title change in both directions, the Punk trilogy and the Fatu ending. This is a curated "
              "ledger, not a career count, and no career win&ndash;loss total is published because no "
              "verified one exists. A reported May 2025 steel cage loss to Damian Priest at Saturday "
              "Night&rsquo;s Main Event appeared in only one automated source read and is omitted "
              "rather than guessed at. Filter by match type, tap any column header to sort, and turn "
              "spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The two bouts with verified Wrestling Observer ratings at the top of his card "
                    "&mdash; one of them a loss, which tells you something about how his best matches "
                    "have been used. Ratings are as reproduced in published Observer round-ups, not "
                    "re-checked against archives."),
    signature=[
        dict(rating="5.0", event="WrestleMania 39 Night 2", opponent="Gunther & Sheamus",
             stip="Intercontinental Championship triple threat — Gunther retained"),
        dict(rating="4.5", event="Clash at the Castle 2022 — Cardiff", opponent="Roman Reigns",
             stip="Undisputed WWE Universal Championship — the home-country loss"),
    ],
    signature_count_word="two",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("3&times;", "WWE Championship"),
            ("1",        "World Heavyweight title"),
            ("1",        "TNA World title"),
            ("356",      "Days as WWE Champion, combined"),
        ],
        lead=("Five world championships across two companies, plus the full ladder underneath: "
              "Intercontinental, NXT, two tag lineages, and the independent titles that rebuilt him. "
              "Dates are as the published title histories give them."),
        rows=[
            dict(ic="W", name="WWE Championship / Undisputed WWE Championship", count="3",
                 sub="2020 &middot; def. Brock Lesnar at WrestleMania 36 Night 2, lost to Randy Orton "
                     "at Hell in a Cell &middot; <b>203 days</b> &middot; 2020&ndash;21 &middot; "
                     "regained from Orton on the November 16 Raw, lost to The Miz&rsquo;s cash-in at "
                     "Elimination Chamber &middot; 97 days &middot; 2026 &middot; def. Cody Rhodes in "
                     "Three Stages of Hell on the January 9 SmackDown, lost the rematch March 6 "
                     "&middot; 56 days"),
            dict(ic="H", name="World Heavyweight Championship", count="1",
                 sub="April 7, 2024 &middot; def. Seth Rollins at WrestleMania 40 Night 2, lost to "
                     "Damian Priest&rsquo;s Money in the Bank cash-in the same night &middot; "
                     "<b>5 minutes 46 seconds</b>"),
            dict(ic="I", name="WWE Intercontinental Championship", count="1",
                 sub="December 13, 2009 &ndash; May 23, 2010 &middot; won at TLC, lost to Kofi "
                     "Kingston at Over the Limit &middot; 161 days, in the Chosen One run"),
            dict(ic="N", name="NXT Championship", count="1",
                 sub="August 19 &ndash; November 18, 2017 &middot; def. Bobby Roode at TakeOver: "
                     "Brooklyn III, lost to Andrade Cien Almas at TakeOver: WarGames &middot; 91 days, "
                     "the comeback-run title"),
            dict(ic="R", name="Raw Tag Team Championship", count="1",
                 sub="September 3 &ndash; October 22, 2018 &middot; with Dolph Ziggler"),
            dict(ic="T", name="WWE Tag Team Championship", count="1",
                 sub="September 19 &ndash; October 24, 2010 &middot; with Cody Rhodes &mdash; the "
                     "same man on the other side of both 2026 title changes"),
            dict(ic="X", name="TNA World Heavyweight Championship", count="1",
                 sub="March 15 &ndash; June 12, 2016, as Drew Galloway &middot; 89 days &middot; plus "
                     "the Impact Grand Championship, January 19 &ndash; March 2, 2017"),
            dict(ic="E", name="Evolve Championship", count="1",
                 sub="August 8, 2014 &ndash; July 10, 2015, as Drew Galloway &middot; held alongside "
                     "the Open the Freedom Gate Championship from April 2015 &middot; plus 2 Evolve "
                     "tag reigns"),
            dict(ic="C", name="ICW World Heavyweight Championship", count="2",
                 sub="Insane Championship Wrestling, Glasgow &middot; first reign won November 2, 2014 "
                     "&middot; ICW Hall of Fame, February 1, 2018"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="One anointing that was not a faction, one band that was a punchline, and one tag team "
             "that worked.",
        cards=[
            dict(era="WWE &middot; 2009&ndash;2011",
                 name="The Chosen One",
                 members="Drew McIntyre, endorsed on air by Vince McMahon",
                 desc="Not a stable — a designation. McMahon introduced him on SmackDown as a future "
                      "world champion, an on-screen endorsement WWE had never really handed anyone so "
                      "directly. The Intercontinental Championship followed within months; the "
                      "prophecy then took eleven years, one release and one global pandemic to come "
                      "true."),
            dict(era="WWE &middot; 2012&ndash;2014",
                 name="3MB",
                 members="Drew McIntyre, Heath Slater, Jinder Mahal",
                 desc="The air-guitar jobber band, and the bottom of the arc. All three men were "
                      "released in June 2014; two of them — McIntyre and Mahal — came back to win the "
                      "WWE Championship, which remains one of the strangest afterlives any comedy "
                      "faction has produced."),
            dict(era="WWE &middot; 2018&ndash;2019",
                 name="McIntyre & Ziggler",
                 members="Drew McIntyre, Dolph Ziggler",
                 desc="The main-roster re-entry vehicle after the NXT comeback: Raw Tag Team Champions "
                      "within weeks of arriving, with McIntyre booked as the silent enforcer being "
                      "kept warm for singles work. The team dissolved on schedule once it had done its "
                      "job."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Two names and four versions of the same man: <b>Drew McIntyre</b> (2007&ndash;2014) "
             "&rarr; <b>Drew Galloway</b> (2014&ndash;2017) &rarr; <b>Drew McIntyre</b> again "
             "(2017&ndash;present). Galloway is his legal surname; McIntyre is the WWE creation he "
             "eventually made his own.",
        cards=[
            dict(mono="CO", era="WWE &middot; 2007&ndash;2014", name="The Chosen One / 3MB Drew",
                 desc="Signed at 22, publicly anointed by Vince McMahon in 2009, Intercontinental "
                      "Champion at 24 — then a slow slide into the 3MB comedy band and a June 2014 "
                      "release. The first act ended as a warning about anointings."),
            dict(mono="DG", era="Independents, Evolve, TNA &middot; 2014&ndash;2017", name="Drew Galloway",
                 desc="The rebuild under his real name: Evolve Champion, two-time ICW World Champion "
                      "in Glasgow, TNA World Heavyweight Champion in 2016. The version of him that "
                      "learned to carry a promotion rather than wait for one."),
            dict(mono="SW", era="WWE &middot; 2017&ndash;2024", name="The Scottish Warrior",
                 desc="NXT Champion within four months of returning, 2020 Royal Rumble winner, and "
                      "the man who beat Brock Lesnar for the WWE Championship in an empty room. The "
                      "pandemic-era champion who never got his stadium moment and said so."),
            dict(mono="SP", era="WWE &middot; 2024&ndash;present", name="The Scottish Psychopath",
                 desc="The bitter, grievance-keeping heel of the CM Punk and Cody Rhodes feuds — "
                      "self-aware about the empty-arena reign, contemptuous of crowd favourites, and "
                      "willing to fight in unsanctioned rules. The version currently on pause while "
                      "he films."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Ayr at sixteen to a third WWE Championship at forty.",
        rows=[
            dict(year="2001", title="Debut in Scotland",
                 desc="First matches for British Championship Wrestling as a teenager; signs with WWE "
                      "in 2007 at 22."),
            dict(year="2009", title="The Chosen One",
                 desc="Vince McMahon anoints him on SmackDown; he wins the Intercontinental "
                      "Championship at TLC on December 13."),
            dict(year="2014", title="Released",
                 desc="Cut in June after two years in 3MB. Rebuilds as Drew Galloway across Evolve, "
                      "ICW and the world's independents."),
            dict(year="2016", title="TNA World Heavyweight Champion",
                 desc="Beats Matt Hardy on March 15 and holds the title 89 days — a world champion "
                      "outside WWE before he was one inside it."),
            dict(year="2017", title="Returns; NXT Champion",
                 desc="Re-signs in April, beats Bobby Roode for the NXT Championship at TakeOver: "
                      "Brooklyn III on August 19."),
            dict(year="2020", title="Royal Rumble and the WWE Championship",
                 desc="Wins the Rumble on January 26, eliminating Brock Lesnar, then beats Lesnar at "
                      "WrestleMania 36 on April 5 — the first British WWE Champion, crowned in an "
                      "empty Performance Center."),
            dict(year="2021", title="Two reigns end",
                 desc="Loses the title to Randy Orton, regains it in November 2020, and loses it to "
                      "The Miz's cash-in at Elimination Chamber on February 21, 2021."),
            dict(year="2022", title="Cardiff",
                 desc="Challenges Roman Reigns for the Undisputed WWE Universal Championship at Clash "
                      "at the Castle on September 3 in front of a Welsh stadium, and loses."),
            dict(year="2024", title="5 minutes 46 seconds",
                 desc="Beats Seth Rollins for the World Heavyweight Championship at WrestleMania 40 on "
                      "April 7; Damian Priest cashes in minutes later. Spends the rest of the year in "
                      "a three-match feud with CM Punk, winning only SummerSlam."),
            dict(year="2025", title="Settles with Priest; collides with Fatu",
                 desc="Beats Damian Priest in a Sin City Street Fight at WrestleMania 41 on April 20. "
                      "An October backstage attack involving Jacob Fatu takes Fatu off TV for months "
                      "and lights the fuse on 2026."),
            dict(year="2026", title="Third WWE Championship, then the pause",
                 desc="Beats Cody Rhodes in Three Stages of Hell on January 9, retains against Sami "
                      "Zayn at the Royal Rumble on January 31, loses the rematch to Rhodes on March 6, "
                      "and loses an unsanctioned match to Fatu at WrestleMania 42 on April 18. Then "
                      "leaves to film."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="CM Punk", slug="cm-punk",
                 desc="The defining 2024 feud: McIntyre mocked Punk's Royal Rumble injury, stole and "
                      "wore his friendship bracelet, and got one win out of three — SummerSlam on "
                      "August 3, before losing the strap match at Bash in Berlin and the Hell in a "
                      "Cell blowoff at Bad Blood on October 5. It made him the best talker of his "
                      "career and the most hated man on the roster in the same year."),
            dict(name="Damian Priest",
                 desc="Priest's cash-in ended the 5:46 World Heavyweight Championship reign at "
                      "WrestleMania 40, and McIntyre chased the receipt for a year — finally pinning "
                      "him in a Sin City Street Fight at WrestleMania 41 on April 20, 2025, with a "
                      "Claymore into a chair-wrapped turnbuckle."),
            dict(name="Cody Rhodes",
                 desc="Tag team partners in 2010, world title trading partners in 2026: McIntyre took "
                      "the Undisputed WWE Championship from him in Three Stages of Hell on January 9 "
                      "and lost it back on March 6, with Jacob Fatu's interference bending both "
                      "finishes. Rhodes went on to WrestleMania; McIntyre went to Fatu."),
            dict(name="Jacob Fatu",
                 desc="The current account, unsettled. A backstage attack in October 2025 cost Fatu "
                      "months of appearances; Fatu's return blew up McIntyre's January title win, his "
                      "March title loss, and finally his WrestleMania 42 — an unsanctioned match Fatu "
                      "won on April 18, 2026. It is the last match McIntyre has had, and the feud WWE "
                      "has waiting whenever he returns."),
            dict(name="Roman Reigns",
                 desc="The stadium loss. Clash at the Castle in Cardiff on September 3, 2022 was built "
                      "as the home-country coronation McIntyre never got in 2020, and Reigns beat him "
                      "anyway — a 4.5-star match and the clearest statement of that era's pecking "
                      "order."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="The acting career is no longer a sideline — it is currently the reason he is not on "
             "television.",
        rows=[
            dict(when="2021", title="A Chosen Destiny: My Story", kind="Book",
                 desc="The autobiography covering the release, the rebuild and the empty-arena title "
                      "win."),
            dict(when="2024", title="The Killer's Game", kind="Film",
                 desc="Supporting role alongside Dave Bautista — his feature debut."),
            dict(when="2026", title="Highlander", kind="Film",
                 desc="Lead role in the Amazon MGM reboot, in post-production as of August 2026 "
                      "(Sportsnaut/PWInsider)."),
            dict(when="2026", title="The Last Druid", kind="Film",
                 desc="Historical action film with Russell Crowe, shooting in Spain — the project "
                      "keeping him off WWE television right now."),
            dict(when="2012&ndash;", title="WWE 2K", kind="Game",
                 desc="A playable roster regular across the WWE 2K series in both of his WWE runs."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated precisely — including the one that lasted less than six minutes.",
        stats=[
            ("1st",  "British WWE Champion"),
            ("356",  "Days as WWE Champion, combined"),
            ("5:46", "WHC reign"),
        ],
        rows=[
            dict(name="First British WWE Champion",
                 sub="WrestleMania 36 Night 2, April 5, 2020, beating Brock Lesnar. Also the first "
                     "Scot to hold the title, and it was won in an empty WWE Performance Center at the "
                     "start of the pandemic — a fact he has been openly ambivalent about since."),
            dict(name="Three WWE Championship reigns — 203, 97 and 56 days",
                 sub="April 5 to October 25, 2020; November 16, 2020 to February 21, 2021; January 9 "
                     "to March 6, 2026. The third is the one most bios have not caught up with: "
                     "&ldquo;two-time champion&rdquo; stopped being accurate in January 2026."),
            dict(name="2020 Royal Rumble winner",
                 sub="January 26, 2020, eliminating Brock Lesnar en route — the elimination that made "
                     "the WrestleMania 36 match."),
            dict(name="World Heavyweight Champion for 5 minutes 46 seconds",
                 sub="April 7, 2024, between beating Seth Rollins and Damian Priest's Money in the "
                     "Bank cash-in. One of the shortest world title reigns in WWE history, and the "
                     "engine of everything he did for the following year."),
            dict(name="World champion in two companies",
                 sub="TNA World Heavyweight Champion for 89 days in 2016 as Drew Galloway, four world "
                     "reigns in WWE since. One of the small group to hold the top title in both TNA "
                     "and WWE."),
            dict(name="Released in 2014, world champion in 2020",
                 sub="Cut from WWE in June 2014 out of 3MB; six years later he headlined WrestleMania. "
                     "The rebuild ran through Evolve (champion), ICW (twice) and TNA."),
            dict(name="A five-star match he lost",
                 sub="The WrestleMania 39 Night 2 Intercontinental triple threat with Gunther and "
                     "Sheamus, April 2, 2023 — rated five stars in published Observer round-ups; "
                     "Gunther retained."),
        ],
        footnote=("Deliberately absent: a career win-loss record, because no verified total exists; "
                  "and the reported May 24, 2025 cage match with Damian Priest, which one automated "
                  "source read surfaced and nothing else confirmed. His current absence is a filming "
                  "hiatus, not an injury and not a retirement — PWInsider reports only that no return "
                  "storyline has been written as of August 2026."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography",
             href="https://en.wikipedia.org/wiki/Drew_McIntyre"),
        dict(k="Sportsnaut", v="August 2026 status — filming, no return planned",
             href="https://sportsnaut.com/wwe/major-update-on-drew-mcintyre-wwe-return-august-2026"),
        dict(k="Fightful", v="Wins the Undisputed WWE Championship, January 9, 2026",
             href="https://www.fightful.com/wrestling/drew-mcintyre-wins-undisputed-wwe-championship-on-wwe-smackdown/"),
        dict(k="Yahoo Sports", v="Cody Rhodes regains the title, March 2026",
             href="https://sports.yahoo.com/articles/cody-rhodes-defeats-drew-mcintyre-041914030.html"),
        dict(k="Bleacher Report", v="WrestleMania 41 Sin City Street Fight",
             href="https://bleacherreport.com/articles/25184950-drew-mcintyre-beats-damian-priest-sin-city-street-fight-wwe-wrestlemania-41"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Why is Drew McIntyre not on WWE TV right now?",
            a="He is filming. His last match was the unsanctioned loss to Jacob Fatu at WrestleMania 42 "
              "on April 18, 2026; since then he has been in post-production on the Amazon MGM "
              "<b>Highlander</b> reboot, in which he has a lead role, and shooting <b>The Last "
              "Druid</b> with Russell Crowe in Spain. PWInsider reported in August 2026 that there has "
              "been no talk of writing him back into storylines. It is a hiatus, not an injury and not "
              "a retirement.",
            q_ld="Why is Drew McIntyre not on WWE television right now?",
            a_ld="Drew McIntyre has been away from WWE since WrestleMania 42 on April 18, 2026, where "
                 "he lost an unsanctioned match to Jacob Fatu. He is pursuing film work: he has a lead "
                 "role in the Amazon MGM Highlander reboot, which is in post-production, and is "
                 "shooting The Last Druid, a historical action film with Russell Crowe, in Spain. "
                 "PWInsider reported in August 2026 that WWE has not yet discussed writing him back "
                 "into storylines. His absence is a filming hiatus, not an injury or a retirement."),
        dict(
            q="How many times has Drew McIntyre been a world champion?",
            a="Five, across two companies. In WWE: the WWE Championship three times &mdash; 203 days "
              "from WrestleMania 36 in 2020, 97 days from November 2020, and 56 days from January 9, "
              "2026 &mdash; plus the World Heavyweight Championship for <b>5 minutes 46 seconds</b> at "
              "WrestleMania 40 in 2024, ended by Damian Priest&rsquo;s cash-in. Before any of that he "
              "was TNA World Heavyweight Champion for 89 days in 2016 as Drew Galloway. The "
              "&ldquo;two-time WWE Champion&rdquo; line many bios still carry is a year out of date.",
            q_ld="How many times has Drew McIntyre been a world champion?",
            a_ld="Drew McIntyre has held five world championships across two companies. In WWE he is a "
                 "three-time WWE Champion, with reigns of 203 days (2020), 97 days (2020-21) and 56 "
                 "days (2026), and a one-time World Heavyweight Champion, a reign of 5 minutes 46 "
                 "seconds at WrestleMania 40 in 2024 that ended with Damian Priest's Money in the Bank "
                 "cash-in. He was also TNA World Heavyweight Champion for 89 days in 2016 under the "
                 "name Drew Galloway."),
        dict(
            q="Did Drew McIntyre really win the WWE Championship in an empty arena?",
            a="Yes. He beat Brock Lesnar at WrestleMania 36 on April 5, 2020, in the WWE Performance "
              "Center in Orlando with no fans present, because the pandemic had moved the entire show "
              "into a closed facility. He was the first British wrestler ever to hold the WWE "
              "Championship, and the missing crowd became part of the character&rsquo;s story &mdash; "
              "WWE rebuilt the Clash at the Castle 2022 match with Roman Reigns in Cardiff largely as "
              "the stadium moment he never got. He lost that one.",
            q_ld="Did Drew McIntyre win the WWE Championship in an empty arena?",
            a_ld="Yes. Drew McIntyre defeated Brock Lesnar for the WWE Championship at WrestleMania 36 "
                 "on April 5, 2020, which was held without fans at the WWE Performance Center in "
                 "Orlando because of the COVID-19 pandemic. He was the first British wrestler to hold "
                 "the WWE Championship. WWE later booked him against Roman Reigns at Clash at the "
                 "Castle in Cardiff, Wales on September 3, 2022, widely framed as the stadium moment "
                 "his 2020 title win never had; Reigns won that match."),
        dict(
            q="What is Drew McIntyre&rsquo;s history with Jacob Fatu?",
            a="It has bent every big McIntyre result since late 2025. A backstage attack in October "
              "2025 kept Fatu off television for months; Fatu resurfaced during the January 9, 2026 "
              "Three Stages of Hell match in which McIntyre won the Undisputed WWE Championship, "
              "interfered again when McIntyre lost the title back to Cody Rhodes on March 6, and then "
              "beat McIntyre in an <b>unsanctioned match</b> at WrestleMania 42 on April 18 &mdash; "
              "McIntyre&rsquo;s last bout before his filming hiatus. The feud is unresolved.",
            q_ld="What is Drew McIntyre's history with Jacob Fatu?",
            a_ld="The Drew McIntyre and Jacob Fatu feud stems from a backstage attack in October 2025 "
                 "that kept Fatu off WWE television for several months. Fatu was involved in the "
                 "January 9, 2026 Three Stages of Hell match in which McIntyre won the Undisputed WWE "
                 "Championship from Cody Rhodes, interfered in the March 6, 2026 rematch in which "
                 "McIntyre lost the title back to Rhodes, and defeated McIntyre in an unsanctioned "
                 "match at WrestleMania 42 on April 18, 2026. That match is McIntyre's most recent "
                 "bout, and the feud remains unresolved."),
        dict(
            q="What happened between Drew McIntyre and CM Punk?",
            a="Three stipulation matches in 2024 and the best talking of McIntyre&rsquo;s career. He "
              "beat Punk at SummerSlam on August 3, lost the strap match at Bash in Berlin on August "
              "31, and lost the Hell in a Cell blowoff at Bad Blood on October 5. The feud ran on "
              "genuine needle &mdash; McIntyre stole and wore Punk&rsquo;s friendship bracelet and "
              "mocked the triceps injury Punk suffered eliminating him from the 2024 Royal Rumble.",
            q_ld="What happened between Drew McIntyre and CM Punk in 2024?",
            a_ld="Drew McIntyre and CM Punk had a three-match feud in 2024. McIntyre defeated Punk at "
                 "SummerSlam on August 3, 2024; Punk won a strap match at Bash in Berlin on August 31, "
                 "2024; and Punk won the Hell in a Cell match at Bad Blood on October 5, 2024. The "
                 "feud drew on Punk's real triceps injury from the 2024 Royal Rumble and on McIntyre "
                 "stealing and wearing Punk's friendship bracelet."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Andrew McLean Galloway IV"),
        dict(label="Born", value="June 6, 1985", sub="Ayr, Scotland &middot; age 41"),
        dict(label="Billed from", value="Ayr, Scotland"),
        dict(label="Height", value="6&#8242;5&#8243;", sub="196 cm"),
        dict(label="Weight", value="265 lb", sub="120 kg (billed)"),
        dict(label="Debut", value="2001", sub="British Championship Wrestling; WWE debut October 12, "
                                              "2007"),
        dict(label="Trained by", value="Mark Sloan and the British circuit",
             sub="Wikipedia also credits Justin Richards, James Tighe, Doug Williams, Paul Burchill "
                 "and Alex Shane, among others"),
        dict(label="Ring names", value="Drew McIntyre &rarr; Drew Galloway &rarr; Drew McIntyre",
             sub="2007&ndash;14 &middot; 2014&ndash;17 &middot; 2017&ndash;present &mdash; Galloway "
                 "is his legal surname"),
        dict(label="Signature", value="Claymore &middot; Future Shock DDT &middot; Glasgow Kiss"),
        dict(label="Brand", value="SmackDown", sub="inactive since April 18, 2026 &mdash; filming "
                                                   "hiatus"),
        dict(label="Also known as",
             value="The Scottish Warrior &middot; The Chosen One &middot; The Scottish Psychopath"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1985-06-06",
    bornplace="Ayr, Scotland",
    nationality="United Kingdom",
    height_cm=196,
    weight_kg=120,
    ld=dict(
        alternateName=["Andrew McLean Galloway IV", "Drew Galloway", "The Scottish Warrior",
                       "The Chosen One", "The Scottish Psychopath"],
        award=["WWE Championship (3 reigns)",
               "World Heavyweight Championship (1 reign)",
               "Royal Rumble winner (2020)",
               "WWE Intercontinental Championship (1 reign)",
               "NXT Championship (1 reign)",
               "Raw Tag Team Championship (1 reign)",
               "WWE Tag Team Championship (1 reign)",
               "TNA World Heavyweight Championship (1 reign)",
               "Impact Grand Championship (1 reign)",
               "Evolve Championship (1 reign)",
               "Open the Freedom Gate Championship (1 reign)",
               "ICW World Heavyweight Championship (2 reigns)",
               "ICW Hall of Fame (2018)"],
        knowsAbout=["Professional wrestling", "WWE", "TNA Wrestling", "Evolve", "Insane Championship "
                    "Wrestling", "Championship wrestling", "Acting"],
        description="Drew McIntyre, born Andrew McLean Galloway IV in Ayr, Scotland, is a Scottish "
                    "professional wrestler and actor signed to WWE. He won the 2020 Royal Rumble and "
                    "defeated Brock Lesnar at WrestleMania 36 to become the first British WWE "
                    "Champion, has held the WWE Championship three times and the World Heavyweight "
                    "Championship once, and was TNA World Heavyweight Champion in 2016 as Drew "
                    "Galloway. As of August 2026 he is on hiatus from WWE filming the Highlander "
                    "reboot and The Last Druid.",
        sameAs=["https://en.wikipedia.org/wiki/Drew_McIntyre",
                "https://www.wwe.com/superstars/drew-mcintyre"],
    ),
)
