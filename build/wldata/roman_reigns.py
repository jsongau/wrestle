# -*- coding: utf-8 -*-
"""Roman Reigns - dossier data.

Sources: /tmp/research/roman-reigns.md (web-verified, compiled Aug 23 2026) and the
harvested match/signature/tape/bio data from the previous /wrestlers/roman-reigns/ page.
Nothing here is invented: every match row carries a date that appears in one of those two.
Career win-loss totals are deliberately NOT published - Cagematch was unreadable for the
research file, and the old page's "76-44" headline is flagged by the harvester as
inconsistent with its own sparkline.
"""

# ----------------------------------------------------------------- record rows
# 9 rows harvested from the existing page (all career-defining highlights) plus
# 16 rows whose dates and outcomes are stated explicitly in the research dossier.
ROWS = [
    dict(result="W", date="2013-05-19", promo="WWE", type="tag",
         event="Extreme Rules", opponent="Team Hell No (Daniel Bryan & Kane)",
         stip="Tag w/ Seth Rollins", title="WWE Tag Team Championship"),
    dict(result="L", date="2013-10-14", promo="WWE", type="tag",
         event="Raw", opponent="Cody Rhodes & Goldust",
         stip="No DQ tag w/ Seth Rollins", title="WWE Tag Team Championship"),
    dict(result="L", date="2014-04-06", promo="WWE", type="tag", landmark=True,
         event="WrestleMania XXX", opponent="Daniel Bryan & Batista",
         stip="Triple threat — Bryan wins the title", title="WWE Championship"),
    dict(result="L", date="2015-06-14", promo="WWE", landmark=True,
         event="Money in the Bank", opponent="Seth Rollins",
         stip="Singles — his best singles match to that point", title="WWE Championship"),
    dict(result="W", date="2015-11-22", promo="WWE", landmark=True,
         event="Survivor Series — tournament final", opponent="Dean Ambrose",
         stip="Vacant-title tournament final", title="WWE Championship"),
    dict(result="L", date="2015-11-22", promo="WWE", landmark=True,
         event="Survivor Series — Money in the Bank cash-in", opponent="Sheamus",
         stip="Cash-in, minutes after the win", title="WWE Championship"),
    dict(result="W", date="2015-12-14", promo="WWE", landmark=True,
         event="Raw", opponent="Sheamus", stip="Singles — 41-day reign begins",
         title="WWE Championship"),
    dict(result="L", date="2016-01-24", promo="WWE", type="tag",
         event="Royal Rumble", opponent="Triple H and the Rumble field",
         stip="Royal Rumble match contested for the title", title="WWE Championship"),
    dict(result="W", date="2016-04-03", promo="WWE", landmark=True,
         event="WrestleMania 32", opponent="Triple H", opponent_html=True,
         stip="Singles — booed through a stadium win", title="WWE Championship"),
    dict(result="L", date="2016-06-19", promo="WWE", landmark=True,
         event="Money in the Bank", opponent="Seth Rollins",
         stip="Singles — ends the 77-day reign", title="WWE Championship"),
    dict(result="W", date="2016-09-25", promo="WWE",
         event="Clash of Champions", opponent="Rusev", stip="Singles",
         title="United States Championship"),
    dict(result="L", date="2017-01-09", promo="WWE",
         event="Raw", opponent="Chris Jericho", stip="Singles — ends a 106-day reign",
         title="United States Championship"),
    dict(result="W", date="2017-10-22", promo="WWE", landmark=True,
         event="No Mercy", opponent="John Cena", opponent_html=True,
         stip="Singles — the torch-pass", title=""),
    dict(result="W", date="2017-11-20", promo="WWE",
         event="Raw", opponent="The Miz", stip="Singles",
         title="Intercontinental Championship"),
    dict(result="L", date="2018-01-22", promo="WWE",
         event="Raw", opponent="The Miz", stip="Singles — ends a 63-day reign",
         title="Intercontinental Championship"),
    dict(result="L", date="2018-04-08", promo="WWE", landmark=True,
         event="WrestleMania 34", opponent="Brock Lesnar",
         stip="Singles — his best babyface performance", title="Universal Championship"),
    dict(result="W", date="2018-08-19", promo="WWE", landmark=True,
         event="SummerSlam", opponent="Brock Lesnar",
         stip="Singles — first Universal reign, vacated in October", title="Universal Championship"),
    dict(result="W", date="2020-08-30", promo="WWE", type="tag", landmark=True,
         event="Payback", opponent="“The Fiend” Bray Wyatt & Braun Strowman",
         stip="Triple threat — the Tribal Chief debuts", title="Universal Championship"),
    dict(result="W", date="2020-11-22", promo="WWE", landmark=True,
         event="Survivor Series", opponent="Kevin Owens",
         stip="I Quit match", title="Universal Championship"),
    dict(result="W", date="2022-04-03", promo="WWE", landmark=True,
         event="WrestleMania 38 Night 2", opponent="Brock Lesnar",
         stip="Title unification — winner takes all", title="WWE & Universal Championships"),
    dict(result="W", date="2023-02-18", promo="WWE", landmark=True,
         event="Elimination Chamber", opponent="Sami Zayn",
         stip="Singles — Montreal; Zayn turns after the bell", title="Undisputed WWE Universal Championship"),
    dict(result="L", date="2024-04-07", promo="WWE", landmark=True,
         event="WrestleMania XL Night 2", opponent="Cody Rhodes", opponent_html=True,
         stip="Bloodline Rules — the 1,316-day reign ends", title="Undisputed WWE Universal Championship"),
    dict(result="W", date="2026-01-31", promo="WWE", type="tag", landmark=True,
         event="Royal Rumble", opponent="The 2026 Royal Rumble field",
         stip="Royal Rumble match — his second, eleven years after the first", title=""),
    dict(result="W", date="2026-04-19", promo="WWE", landmark=True,
         event="WrestleMania 42 Night 2 — Allegiant Stadium", opponent="CM Punk", opponent_html=True,
         stip="Singles — ★★★★★ (Meltzer)", title="World Heavyweight Championship"),
    dict(result="W", date="2026-08-02", promo="WWE", landmark=True,
         event="SummerSlam Night 2 — U.S. Bank Stadium", opponent="Seth Rollins", opponent_html=True,
         stip="Singles — pinfall; ESPN framed it as the end of the rivalry",
         title="World Heavyweight Championship"),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Triple H": "triple-h", "John Cena": "john-cena", "Cody Rhodes": "cody-rhodes",
                 "CM Punk": "cm-punk", "Seth Rollins": "seth-rollins"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="roman-reigns",
    name="Roman Reigns",
    realname="Leati Joseph Anoa’i",
    epithet="The Tribal Chief",
    hook="Record & Titles",

    meta_desc=("Roman Reigns, The Tribal Chief, is a seven-time world champion whose 1,316-day "
               "Universal Championship reign is the fourth-longest world title reign in WWE history. "
               "Full record, titles, factions, records and career."),
    og_desc=("The Tribal Chief: 7 world title reigns, a 1,316-day Universal Championship run, "
             "11 WrestleMania main events, two Royal Rumbles. Full record, titles, factions and career."),
    tw_desc="The Tribal Chief: 7 world titles, a 1,316-day Universal reign, 11 WrestleMania main events.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2010",
    height_imp="6&#8242;3&#8243;",
    weight_lb="265",
    world_titles="7",
    vitals_tagline="Acknowledge me",
    support_note="Merch &middot; Games &middot; Watch",
    x_url="https://x.com/WWERomanReigns",
    ig_url="https://www.instagram.com/officialreigns/",
    sp_items=[
        dict(ic="RR", title="Tribal Chief Merch", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="In 21 wrestling games, 2K14 to 2K26",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="SF", title="Street Fighter", sub="Plays Akuma · October 16, 2026",
             tag="Watch", href="https://en.wikipedia.org/wiki/Street_Fighter_(2026_film)"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/roman-reigns"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Head of the Table &middot; The Big Dog &middot; The Original Tribal Chief",
    hero_tag="Anoa&rsquo;i Family Bloodline &middot; <em>FCW &middot; WWE &middot; 2010&ndash;present</em>",
    now_label="NOW",
    now_bold="World Heavyweight Champion",
    now_tail=" &middot; 126 days into a first reign, and a villain again",
    hstats=[
        dict(value="7",    x=True,  label="World Titles"),
        dict(value="1316", x=False, label="Day Universal Reign"),
        dict(value="11",   x=False, label="WrestleMania Main Events"),
        dict(value="2",    x=True,  label="Royal Rumble Wins"),
    ],
    ghost_link="From Georgia Tech to the Head of the Table",
    vlabel="Est. 2010 &middot; Pensacola, FL",
    mono="RR",

    # ---------------------------------------------------------------- 01 overview
    # index into overview of the correction paragraph -> the framed
    # "Setting one thing straight" callout (aside.corr) on the page
    correction=1,
    overview=[
        "<b>Roman Reigns</b> is the wrestler WWE built its post-Cena decade around, and the numbers "
        "are the argument: a single Universal Championship reign of 1,316 days, eleven WrestleMania "
        "main events, and a run as the promotion&rsquo;s top-billed act across two ownership structures "
        "and a platform shift to Netflix. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">1,316</span>'
        '<span class="pull-cap">days as Universal Champion &mdash; the longest reign in that title&rsquo;s history</span></span>'
        "He is also the rare case where the company&rsquo;s first plan "
        "failed in public and the second one worked. Pushed as a smiling franchise hero from 2014 to "
        "2020 against loud, sustained rejection, he came back from a COVID-era layoff as &ldquo;The "
        "Tribal Chief,&rdquo; a heel built on his real Samoan wrestling lineage, and became the most "
        "credible main-event act of his era.",

        "The 1,316 days are worth stating precisely, because the way the figure travels is wrong twice "
        "over. It is a <b>Universal Championship</b> number, August 30, 2020 to April 7, 2024. The "
        "<i>Undisputed</i> WWE Universal Championship did not exist until he beat Brock Lesnar at "
        "WrestleMania 38 on April 3, 2022 and unified the belts &mdash; so his <b>WWE Championship</b> "
        "reign ran 735 days, not 1,316, and for the first 581 days of the longer run someone else "
        "(Big E, Lesnar, Bobby Lashley) was WWE Champion. Nor is it the longest world title reign in "
        "company history: it is the <b>fourth-longest</b>, behind Bruno Sammartino&rsquo;s first WWWF "
        "reign (2,803 days), Bob Backlund (2,135) and Hulk Hogan&rsquo;s first WWF reign (1,474). He "
        "reached fourth on January 20, 2024 by passing Sammartino&rsquo;s second reign, which is exactly "
        "how Fightful, 411Mania and Cageside Seats reported it at the time. The accurate superlatives "
        "are narrower and still enormous: the longest Universal Championship reign ever, and the longest "
        "recognised world title reign in WWE since Hogan&rsquo;s ended in 1988.",

        '<span class="pull" aria-hidden="true"><span class="pull-fig">11</span>'
        '<span class="pull-cap">WrestleMania main events</span></span>'
        "He was born Leati Joseph Anoa&rsquo;i on May 25, 1985 in Pensacola, Florida, son of Sika of the "
        "Wild Samoans and a first cousin once removed to Jimmy Uso, Jey Uso and Solo Sikoa. Wrestling "
        "was the second career: defensive tackle at Georgia Tech, three-year starter, senior captain, "
        "first-team All-ACC in 2006, then a Minnesota Vikings contract in May 2007 that ended when a "
        "team physical found leukemia. He signed with WWE developmental in 2010 and debuted as Roman "
        "Leakee that August. The main-roster run started as a supporting one &mdash; enforcer of The "
        "Shield from Survivor Series 2012, tag champion with Seth Rollins, nearly two years without a "
        "clean loss &mdash; and the singles push that followed produced a Royal Rumble win, four WWE "
        "Championship reigns and four straight WrestleMania main events without ever producing the "
        "crowd reaction WWE wanted. The reset came at Payback on August 30, 2020.",

        "Since losing to Cody Rhodes at WrestleMania XL he has worked a reduced schedule. He returned "
        "in August 2024 as the Original Tribal Chief, reclaimed the seat on the January 6, 2025 Netflix "
        "premiere of Raw, won the 2026 Royal Rumble on January 31 &mdash; his second, eleven years after "
        "his first &mdash; and cashed it in at WrestleMania 42 on April 19, 2026, beating CM Punk for the "
        "World Heavyweight Championship in a match Dave Meltzer gave the full five stars. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig pull-fig--sm">5&nbsp;STARS</span>'
        '<span class="pull-cap">Meltzer&rsquo;s full rating for the WrestleMania 42 win over CM Punk</span></span>'
        "He retained "
        "against Rollins at SummerSlam on August 2 and has since drifted back to villainy; the August 3, "
        "2026 Raw, where he endorsed Jacob Fatu maiming Royce Keys, is the segment most reports treat as "
        "the turn, though TheSmackDownHotel&rsquo;s database dates the switch to June and WWE has "
        "announced nothing. He also plays Akuma in Paramount&rsquo;s <i>Street Fighter</i>, out October 16, 2026.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("7&times;",  "World titles"),
            ("4&times;",  "WWE Championship"),
            ("2&times;",  "Universal Championship"),
            ("1&times;",  "World Heavyweight"),
            ("1,316",     "Longest reign (days)"),
            ("11",        "WrestleMania main events"),
        ],
        lead=("Twenty-five documented bouts &mdash; every title change, the WrestleMania main events and "
              "the matches that turned the character. This is a curated ledger, not a complete career "
              "count: Cagematch is JavaScript-gated and could not be read for this file, so no career "
              "win&ndash;loss total is published here rather than guessed. Filter by match type, tap any "
              "column header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The nights that made The Tribal Chief, by acclaim (Meltzer / Cagematch, as reported). "
                    "The WrestleMania 42 main event is the only five-star rating of his career."),
    signature=[
        dict(rating="5.0", event="WrestleMania 42 Night 2", opponent="CM Punk",
             stip="World Heavyweight Championship", url="/wrestlers/cm-punk/"),
        dict(rating="4.5", event="Elimination Chamber 2023", opponent="Sami Zayn",
             stip="Undisputed WWE Universal Championship"),
        dict(rating="4.5", event="WrestleMania XL Night 2", opponent="Cody Rhodes",
             stip="Bloodline Rules — the reign ends", url="/wrestlers/cody-rhodes/"),
        dict(rating="4.0", event="WrestleMania XXX", opponent="Daniel Bryan & Batista",
             stip="WWE Championship — triple threat"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("7&times;", "World title reigns"),
            ("11",       "Major titles"),
            ("28th",     "Triple Crown"),
            ("17th",     "Grand Slam"),
        ],
        lead=("Seven world title reigns across three belts, plus the secondary and tag championships that "
              "made him a Grand Slam champion. Reign lengths are calculated from the win and loss dates; "
              "where databases disagree, both figures are shown."),
        rows=[
            dict(ic="W", name="WWE Championship", count="4",
                 sub="2015 Survivor Series &mdash; under a day, Sheamus cashes in &middot; 2015&ndash;16, "
                     "41 days &middot; 2016 WrestleMania 32, 77 days &middot; 2022&ndash;24, the 735-day "
                     "unified reign"),
            dict(ic="U", name="Universal Championship", count="2",
                 sub="2018 SummerSlam &mdash; 63 days (Wikipedia) or 64 (ITR), vacated on the leukemia "
                     "announcement &middot; 2020&ndash;24, the 1,316-day reign &middot; WWE recognises him "
                     "as the final Universal Champion; the belt was retired rather than passed on"),
            dict(ic="H", name="World Heavyweight Championship", count="1",
                 sub="2026&ndash; &middot; def. CM Punk at WrestleMania 42 Night 2, Allegiant Stadium "
                     "&middot; 126 days as of August 23, 2026 &middot; next defense Raw, Mexico City, "
                     "September 14, 2026"),
            dict(ic="I", name="WWE Intercontinental Championship", count="1",
                 sub="2017&ndash;18 &middot; def. The Miz on Raw, lost it back to him &middot; 63 days"),
            dict(ic="S", name="WWE United States Championship", count="1",
                 sub="2016&ndash;17 &middot; def. Rusev at Clash of Champions, lost to Chris Jericho "
                     "&middot; 106 days"),
            dict(ic="T", name="WWE Tag Team Championship", count="1",
                 sub="2013 &middot; with Seth Rollins, def. Team Hell No at Extreme Rules &middot; 148 days"),
            dict(ic="F", name="FCW Florida Tag Team Championship", count="1",
                 sub="2012 developmental &middot; partner listed as Mike Dalton (Wikipedia) and Tyler Breeze "
                     "(TheSmackDownHotel) &mdash; the same wrestler, earlier ring name &middot; reign length "
                     "not verified"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Three groups, one family tree &mdash; and the storyline that ran WWE for four straight years.",
        cards=[
            dict(era="WWE &middot; 2012&ndash;14, reunions 2017&ndash;19",
                 name="The Shield",
                 members="Roman Reigns, Dean Ambrose, Seth Rollins",
                 desc="Debuted at Survivor Series 2012 interfering in the WWE Championship match; a "
                      "mercenary unit in riot gear that entered through the crowd and went nearly two "
                      "years without a clean loss. Reigns and Rollins took the WWE Tag Team Championship, "
                      "Ambrose the United States title. It ended when Rollins turned on the other two in "
                      "June 2014. All three went on to hold world titles."),
            dict(era="WWE &middot; 2020&ndash;24, reformed 2025 and 2026",
                 name="The Bloodline",
                 members="Roman Reigns, Paul Heyman, Jimmy Uso, Jey Uso, Solo Sikoa, Sami Zayn, "
                         "Jacob Fatu, Tama Tonga, Tonga Loa",
                 desc="Built on the real Anoa’i lineage — the “acknowledge me” framing borrows from actual "
                      "Samoan wrestling hierarchy. It carried WWE’s main-event storyline for four straight "
                      "years, produced the 2023 Jey Uso and Sami Zayn arcs, and split into a civil war when "
                      "Solo Sikoa claimed leadership in April 2024. As of August 2026 the group is Reigns, "
                      "both Usos and Jacob Fatu; the Usos were named captains on the August 17 Raw and Solo "
                      "refused to rejoin, turning on Reigns alongside LA Knight."),
            dict(era="WWE &middot; 2024&ndash;25",
                 name="The OG Bloodline",
                 members="Roman Reigns, Jey Uso, Jimmy Uso, Sami Zayn",
                 desc="The splinter faction Reigns assembled against Solo Sikoa’s version after his August "
                      "2024 return. It dissolved once he reclaimed the Tribal Chief position on the "
                      "January 6, 2025 Netflix premiere of Raw."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One man, four characters &mdash; and the only franchise reset of the modern era that worked.",
        cards=[
            dict(mono="SH", era="WWE &middot; 2012&ndash;14", name="The Shield Enforcer",
                 desc="Silent muscle of a three-man unit. The spear became the finish and the Superman "
                      "Punch was added; the promos came later. Before that, two years in FCW as Roman "
                      "Leakee with finishers — the Moment of Silence and a spinning bulldog called "
                      "Checkmate — that did not survive the call-up."),
            dict(mono="BD", era="WWE &middot; 2014&ndash;20", name="The Big Dog",
                 desc="The solo babyface franchise push, booked as the successor to John Cena and rejected "
                      "loudest between 2015 and 2018. Four WWE Championships and four straight WrestleMania "
                      "main events came out of it; the reaction never did."),
            dict(mono="TC", era="WWE &middot; 2020&ndash;24", name="The Tribal Chief",
                 desc="The pivot. Heel, Paul Heyman as advocate, Samoan-lineage authority framing, "
                      "“acknowledge me.” Slower, colder and promo-driven, and it produced the 1,316-day "
                      "Universal Championship reign."),
            dict(mono="OTC", era="WWE &middot; 2024&ndash;present", name="The Original Tribal Chief",
                 desc="A face turn on the return from WrestleMania XL, the seat reclaimed in January 2025, "
                      "and a part-time schedule. Villainy has crept back in through 2026 — the turn date is "
                      "disputed, June per TheSmackDownHotel and August 3 per the Sportsnaut report, with no "
                      "on-air announcement either way."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Pensacola to Georgia Tech to the Head of the Table.",
        rows=[
            dict(year="2007", title="Leukemia ends the NFL path",
                 desc="Signed by the Minnesota Vikings in May 2007 and released after a team physical "
                      "detected leukemia; a brief Jacksonville stint and five CFL games for Edmonton in "
                      "2008 followed before he quit football."),
            dict(year="2010", title="Signs with WWE developmental",
                 desc="Trained by Steve Keirn in FCW; debuts August 19, 2010 as Roman Leakee."),
            dict(year="2012", title="The Shield debuts",
                 desc="Main-roster debut November 18, 2012 at Survivor Series alongside Dean Ambrose and "
                      "Seth Rollins."),
            dict(year="2015", title="Royal Rumble win, first WrestleMania main event",
                 desc="Wins the 2015 Rumble to a hostile reaction and main-events WrestleMania 31 against "
                      "Brock Lesnar."),
            dict(year="2018", title="Leukemia returns, then remission",
                 desc="Vacates the Universal Championship on the October 22, 2018 Raw; returns February 25, "
                      "2019 announcing remission."),
            dict(year="2020", title="The Tribal Chief",
                 desc="Returns at SummerSlam after a five-month COVID-related absence, wins the Universal "
                      "Championship at Payback on August 30 and turns heel with Paul Heyman."),
            dict(year="2022", title="Unifies the world titles",
                 desc="Beats Brock Lesnar at WrestleMania 38 on April 3 to hold the WWE and Universal "
                      "Championships at the same time."),
            dict(year="2024", title="The reign ends",
                 desc="Loses to Cody Rhodes at WrestleMania XL Night 2 on April 7 — 1,316 days as Universal "
                      "Champion, 735 as WWE Champion."),
            dict(year="2026", title="Second Royal Rumble, first World Heavyweight Championship",
                 desc="Wins the January 31 Royal Rumble, then beats CM Punk at WrestleMania 42 on April 19 "
                      "in a five-star match."),
            dict(year="2026", title="Bloodline rebuilt, heel again",
                 desc="Retains against Seth Rollins at SummerSlam on August 2; endorses Jacob Fatu’s "
                      "violence on the August 3 Raw; Solo Sikoa turns on him on August 17."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Brock Lesnar",
                 desc="Seven years and roughly a dozen matches from WrestleMania 31 through SummerSlam "
                      "2022, including three WrestleMania main events. The 2015 opener is still the match "
                      "people use to argue Reigns was better than the crowd allowed; the Last Man Standing "
                      "win in 2022 is the moment he had clearly passed Lesnar as WWE’s protected top act."),
            dict(name="Seth Rollins", slug="seth-rollins",
                 desc="The longest-running relationship of his career: Shield brothers and tag champions, "
                      "then enemies after the 2014 turn, then partners, then enemies again. Rollins took "
                      "the WWE Championship off him at Money in the Bank 2016; Reigns closed the loop on "
                      "August 2, 2026, beating him to retain the World Heavyweight Championship."),
            dict(name="Jey Uso", slug="jey-uso",
                 desc="The Bloodline civil war. Jey’s 2023 challenge and Solo Sikoa’s April 2024 coup "
                      "turned a stable into a succession story about who gets to be Tribal Chief, gave WWE "
                      "its best-reviewed long-form television of the decade, and is the direct ancestor of "
                      "the 2026 angle in which Solo again refuses to fall in line."),
            dict(name="Cody Rhodes", slug="cody-rhodes",
                 desc="Two consecutive WrestleMania main events with opposite outcomes: Reigns retained at "
                      "WrestleMania 39 via Solo Sikoa interference, then lost the Bloodline Rules match at "
                      "WrestleMania XL that ended the 1,316-day reign. The single most consequential result "
                      "of either man’s career."),
            dict(name="CM Punk", slug="cm-punk",
                 desc="A rivalry that could not have happened for a decade because Punk had left the "
                      "business. It peaked across WrestleMania 41 Night 1 and WrestleMania 42 Night 2, "
                      "where Reigns beat him for the World Heavyweight Championship in the only match Dave "
                      "Meltzer has given Reigns five stars."),
            dict(name="The Undertaker",
                 desc="One match, at WrestleMania 33 in 2017, but a load-bearing one: Reigns won, Undertaker "
                      "left his gear in the ring, and WWE staged it as a literal passing of the torch. It "
                      "also drew some of the loudest hostility of the babyface run — part of why the Tribal "
                      "Chief reset happened at all."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Beyond the ring.",
        rows=[
            dict(when="2026", title="Street Fighter", kind="Film",
                 desc="Plays Akuma in Paramount’s adaptation, out October 16, 2026, alongside Cody Rhodes "
                      "as Guile, Andrew Koji as Ryu, Noah Centineo as Ken, Callina Liang as Chun-Li, David "
                      "Dastmalchian as M. Bison, Jason Momoa as Blanka and 50 Cent as Balrog. He was "
                      "written off television from August to September 2025 to film it."),
            dict(when="2019", title="Fast & Furious Presents: Hobbs & Shaw", kind="Film",
                 desc="Cameo as Mateo Hobbs, brother to Dwayne Johnson’s character — his first theatrical "
                      "film appearance."),
            dict(when="2013&ndash;", title="WWE 2K", kind="Game",
                 desc="Playable in 21 wrestling games per TheSmackDownHotel’s database, from WWE 2K14 "
                      "through WWE 2K26."),
            dict(when="2016&ndash;", title="WWE 24, WWE Rivals, Wrestling With Fame", kind="TV",
                 desc="Covered across WWE’s documentary and reality output. No standalone feature "
                      "documentary and no autobiography is verified; WWE published a children’s biography, "
                      "but a full memoir is not confirmed to exist."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The numbers behind the reign, stated the way the sources actually state them.",
        stats=[
            ("1,316", "Days as Universal Champion"),
            ("735",   "Days as WWE Champion"),
            ("11",    "WrestleMania main events"),
        ],
        rows=[
            dict(name="1,316 consecutive days as Universal Champion",
                 sub="August 30, 2020 to April 7, 2024. The longest reign in that title's history, the "
                     "4th-longest world title reign in WWE history, and the longest recognised WWE world "
                     "title reign since 1988. He reached 4th on January 20, 2024 by passing Bruno "
                     "Sammartino's second WWWF reign of 1,237 days."),
            dict(name="735 consecutive days as WWE Champion",
                 sub="April 3, 2022 to April 7, 2024 — the unified half of the run, which began only when "
                     "he beat Brock Lesnar at WrestleMania 38. The two figures are not additive and only "
                     "the shorter one is an Undisputed number."),
            dict(name="First to hold a WWE world title 1,000+ consecutive days in 35+ years",
                 sub="The last man to do it before him was Hulk Hogan, whose first WWF reign ended in 1988."),
            dict(name="Final Universal Champion",
                 sub="WWE retired the Universal Championship rather than passing it on, and recognises "
                     "Reigns as its last holder (Fightful and Cageside Seats, April 22, 2025)."),
            dict(name="11 WrestleMania main events",
                 sub="ESPN counts 10 through WrestleMania 41, with WrestleMania 42 the 11th. The commonly "
                     "repeated 'five straight' is wrong — the consecutive run was four, WrestleMania 31 "
                     "through 34. WrestleMania 35 was main-evented by Rousey, Flair and Lynch, and Reigns "
                     "worked a mid-card match with Drew McIntyre that night."),
            dict(name="2x Royal Rumble winner, eleven years apart",
                 sub="2015 and January 31, 2026 — the second of which he cashed in at WrestleMania 42."),
            dict(name="PWI 500 number one in 2016 and 2022",
                 sub="The 2026 list had not been published as of August 23, 2026; it normally appears in "
                     "September."),
            dict(name="Five stars from Dave Meltzer, once",
                 sub="vs. CM Punk, WrestleMania 42 Night 2, April 19, 2026 — the highest-rated match of his "
                     "career. On the same card Oba Femi vs. Brock Lesnar drew four stars and the "
                     "Intercontinental ladder match 4.75."),
            dict(name="Sports Illustrated Wrestler of the Year, 2021",
                 sub="Note that a Wrestling Observer Newsletter Wrestler of the Year award is often "
                     "attributed to him and is not verified — that award went to Kenny Omega in 2021, Jon "
                     "Moxley in 2022, Cody Rhodes in 2024 and Mistico in 2025."),
            dict(name="WrestleMania 42 drew somewhere between 97,126 and 106,072",
                 sub="WWE's April 22, 2026 release said 106,072 across two nights at Allegiant Stadium; "
                     "POST Wrestling's tally of WWE's own nightly figures came to 106,071, one short. The "
                     "Las Vegas Stadium Authority reported 97,126, about 8.4% lower. All three measures "
                     "agree the show was down 15-18% on WrestleMania 41, and TKO attributed a $33.7 million "
                     "live-events decline to it."),
        ],
        footnote=("No Cagematch career totals appear anywhere on this page: the site is JavaScript-gated and "
                  "returned only a redirect stub to every fetch made for this file, so nothing was cited "
                  "rather than guessed. Database totals also differ by methodology — TheSmackDownHotel "
                  "counts 7 world championships and 11 major titles, while Wikipedia lists the same "
                  "underlying reigns without a consolidated number, and WWE.com publishes categories with "
                  "no day counts at all."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Instagram", v="@officialreigns", href="https://www.instagram.com/officialreigns/"),
        dict(k="X / Twitter", v="@WWERomanReigns", href="https://x.com/WWERomanReigns"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/roman-reigns"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Roman_Reigns"),
        dict(k="ESPN", v="Ranking his 10 WrestleMania main events",
             href="https://www.espn.com/wwe/story/_/id/48386716/ranking-roman-reigns-10-wwe-wrestlemania-main-events-brock-lesnar-cody-rhodes"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/roman-reigns.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="How many world championships has Roman Reigns won?",
            a="Seven world title reigns: four WWE Championship, two Universal Championship and one World "
              "Heavyweight Championship. TheSmackDownHotel counts that as 7 world championships and 11 "
              "major titles overall. You will sometimes see six, because his first WWE Championship reign "
              "on November 22, 2015 lasted only minutes before Sheamus cashed in Money in the Bank &mdash; "
              "WWE.com still counts it and lists him as a 4-time WWE Champion.",
            q_ld="How many world championships has Roman Reigns won?",
            a_ld="Roman Reigns has seven world title reigns: four WWE Championship reigns, two Universal "
                 "Championship reigns and one World Heavyweight Championship reign. Some counts say six "
                 "because his first WWE Championship reign on November 22, 2015 lasted only minutes before "
                 "Sheamus cashed in Money in the Bank, but WWE.com counts it and lists Roman Reigns as a "
                 "4-time WWE Champion."),
        dict(
            q="How long was Roman Reigns champion, exactly?",
            a="1,316 days as <b>Universal</b> Champion (August 30, 2020 to April 7, 2024) and 735 days as "
              "<b>WWE</b> Champion (April 3, 2022 to April 7, 2024). Those overlap, so they are not "
              "additive, and 1,316 is not an &ldquo;Undisputed&rdquo; figure &mdash; the Undisputed title "
              "did not exist until he unified the belts at WrestleMania 38. It is the fourth-longest world "
              "title reign in WWE history, behind Bruno Sammartino, Bob Backlund and Hulk Hogan, not the "
              "longest.",
            q_ld="How long was Roman Reigns the champion?",
            a_ld="Roman Reigns held the Universal Championship for 1,316 days, from August 30, 2020 to "
                 "April 7, 2024, and the WWE Championship for 735 days, from April 3, 2022 to April 7, "
                 "2024. The two reigns overlap and are not additive, and the 1,316-day figure is a "
                 "Universal Championship figure rather than an Undisputed one, because the Undisputed WWE "
                 "Universal Championship did not exist until Roman Reigns unified the titles at "
                 "WrestleMania 38 on April 3, 2022. The 1,316-day reign is the fourth-longest world "
                 "championship reign in WWE history, behind Bruno Sammartino, Bob Backlund and Hulk Hogan."),
        dict(
            q="What championship does Roman Reigns hold right now?",
            a="The World Heavyweight Championship, his first reign, won from CM Punk in the main event of "
              "WrestleMania 42 Night 2 on April 19, 2026 at Allegiant Stadium. He retained it against Seth "
              "Rollins at SummerSlam on August 2, 2026, and his next announced defense is on Raw in Mexico "
              "City on September 14, 2026, against the winner of a luchador tournament announced by Rey "
              "Mysterio.",
            q_ld="What championship does Roman Reigns hold right now?",
            a_ld="Roman Reigns holds the World Heavyweight Championship, his first reign with that title, "
                 "won from CM Punk in the main event of WrestleMania 42 Night 2 on April 19, 2026 at "
                 "Allegiant Stadium in Las Vegas. Roman Reigns retained it against Seth Rollins at "
                 "SummerSlam on August 2, 2026, and his next announced defense is on Raw in Mexico City on "
                 "September 14, 2026."),
        dict(
            q="Did Roman Reigns turn heel again?",
            a="He is being presented as a villain, but there has been no on-air turn. The closest marker is "
              "the August 3, 2026 Raw, where he endorsed Jacob Fatu&rsquo;s assault on Royce Keys, and a "
              "report published August 18, 2026 says WWE lists him internally as a heel. Note the sources "
              "disagree on timing: TheSmackDownHotel&rsquo;s database dates the switch to June 2026 instead.",
            q_ld="Did Roman Reigns turn heel again?",
            a_ld="Roman Reigns is currently presented as a villain, but WWE has not announced a turn on "
                 "air. The clearest marker is the August 3, 2026 episode of Raw, where Roman Reigns "
                 "endorsed Jacob Fatu's assault on Royce Keys, and a report published August 18, 2026 says "
                 "WWE lists him internally as a heel. Sources disagree on the date: TheSmackDownHotel's "
                 "database dates the switch to June 2026."),
        dict(
            q="Is Roman Reigns retiring?",
            a="No retirement has been announced. He has worked a reduced, part-time schedule since 2024, "
              "took time out in late 2025 to film <i>Street Fighter</i>, and is the reigning World "
              "Heavyweight Champion with a title defense booked for Raw in Mexico City on September 14, 2026.",
            q_ld="Is Roman Reigns retiring?",
            a_ld="No. Roman Reigns has not announced a retirement. He has worked a reduced, part-time "
                 "schedule since 2024 and took time away in late 2025 to film Street Fighter, but he is the "
                 "reigning World Heavyweight Champion with a title defense booked for Raw in Mexico City on "
                 "September 14, 2026."),
        dict(
            q="Is Roman Reigns actually related to The Rock and The Usos?",
            a="The family is real, not a storyline. He is the son of Sika of the Wild Samoans, brother of "
              "Rosey, first cousin once removed to Jimmy Uso, Jey Uso and Solo Sikoa, and part of the "
              "Anoa&rsquo;i family that also includes Yokozuna, Rikishi and Umaga. Dwayne Johnson is "
              "connected through the family&rsquo;s traditional bond with the Maivia line rather than by "
              "blood. The &ldquo;Tribal Chief&rdquo; title itself is a storyline construction built on top "
              "of that real lineage.",
            q_ld="Is Roman Reigns really related to The Rock and The Usos?",
            a_ld="Yes. Roman Reigns belongs to the Anoa'i wrestling family: he is the son of Sika of the "
                 "Wild Samoans, the brother of Rosey, and a first cousin once removed to Jimmy Uso, Jey Uso "
                 "and Solo Sikoa. The family also includes Yokozuna, Rikishi and Umaga. Dwayne Johnson is "
                 "connected through the family's traditional bond with the Maivia line rather than by "
                 "blood, and the Tribal Chief title is a storyline construction built on top of the real "
                 "lineage."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Leati Joseph Anoa&rsquo;i"),
        dict(label="Born", value="May 25, 1985", sub="Pensacola, Florida"),
        dict(label="Billed from", value="Pensacola, Florida"),
        dict(label="Height", value="6&#8242;3&#8243;", sub="191 cm"),
        dict(label="Weight", value="265 lb", sub="120 kg (billed)"),
        dict(label="Debut", value="August 19, 2010", sub="FCW, as Roman Leakee"),
        dict(label="Main-roster debut", value="November 18, 2012", sub="Survivor Series"),
        dict(label="Trained by", value="Steve Keirn", sub="FCW"),
        dict(label="Finishers", value="Spear &middot; Superman Punch &middot; Guillotine choke"),
        dict(label="College", value="Georgia Tech", sub="first-team All-ACC, 2006"),
        dict(label="Brand", value="Raw"),
        dict(label="Also known as",
             value="The Tribal Chief &middot; The Big Dog &middot; The Head of the Table &middot; "
                   "The Original Tribal Chief"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1985-05-25",
    bornplace="Pensacola, Florida, United States",
    nationality="United States",
    alumni="Georgia Institute of Technology",
    height_cm=191,
    weight_kg=120,
    ld=dict(
        alternateName=["Leati Joseph Anoa’i", "The Tribal Chief", "The Big Dog",
                       "The Head of the Table", "The Original Tribal Chief", "Roman Leakee"],
        award=["WWE Championship (4 reigns)",
               "Universal Championship (2 reigns, including a record 1,316-day reign)",
               "World Heavyweight Championship (1 reign)",
               "WWE Intercontinental Championship (1 reign)",
               "WWE United States Championship (1 reign)",
               "WWE Tag Team Championship (1 reign, with Seth Rollins)",
               "Royal Rumble winner (2015, 2026)",
               "Elimination Chamber winner (2018)",
               "WWE Triple Crown Champion (28th)",
               "WWE Grand Slam Champion (17th)",
               "Pro Wrestling Illustrated 500 number one (2016, 2022)",
               "Sports Illustrated Wrestler of the Year (2021)",
               "Slammy Award, Superstar of the Year (2014)"],
        knowsAbout=["Professional wrestling", "The Bloodline", "The Shield",
                    "Anoa’i wrestling family", "WWE", "Championship wrestling", "American football"],
        description="Roman Reigns is an American professional wrestler signed to WWE and a member of the "
                    "Anoa’i family. A seven-time world champion, he held the Universal Championship for "
                    "1,316 consecutive days between August 30, 2020 and April 7, 2024 — the "
                    "fourth-longest world championship reign in WWE history and the longest since 1988 — "
                    "and the WWE Championship for 735 days after unifying the titles at WrestleMania 38. "
                    "A former Georgia Tech defensive tackle, he debuted in WWE developmental in 2010, "
                    "reached the main roster with The Shield in 2012, and leads The Bloodline. He is the "
                    "reigning World Heavyweight Champion.",
        sameAs=["https://x.com/WWERomanReigns",
                "https://www.instagram.com/officialreigns/",
                "https://en.wikipedia.org/wiki/Roman_Reigns",
                "https://www.wwe.com/superstars/roman-reigns"],
    ),
)
