# -*- coding: utf-8 -*-
"""Jey Uso - dossier data.

Sources: web-verified August 31, 2026 (Wikipedia, PWTorch, CBS Sports, WWE.com Raw
recaps, TPWW/Wrestleview results archives, Yahoo Sports, TJR Wrestling and
TheSportster Observer round-ups, SmackDown Hotel). Every match row carries a
day-precision date confirmed in at least one of those sources.

Deliberate omissions:
  * No career win-loss total - no verified figure exists and none is invented.
  * One automated source read gave the October 2024 Intercontinental title loss as
    October 7; the results archives (Wrestleview, TPWW, Daily Caller) all date the
    Philadelphia Raw to October 21, 2024, which is used here.
  * The January 25, 2025 Saturday Night's Main Event title challenge against Gunther
    is referenced in the sources only by month in some reads; the SNME date itself
    is solid and the row is kept with that date.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="L", date="2020-10-25", promo="WWE", landmark=True,
         event="Hell in a Cell", opponent="Roman Reigns",
         stip="Hell in a Cell, I Quit — the loss that created The Bloodline",
         title="WWE Universal Championship"),
    dict(result="W", date="2021-04-09", promo="WWE", type="tag",
         event="SmackDown — WrestleMania 37 week", opponent="The Andre battle royal field",
         stip="Andre the Giant Memorial Battle Royal", title=""),
    dict(result="W", date="2022-05-20", promo="WWE", type="tag", landmark=True,
         event="SmackDown", opponent="RK-Bro",
         stip="Winners Take All unification — with Jimmy Uso",
         title="Undisputed WWE Tag Team Championship"),
    dict(result="L", date="2023-04-01", promo="WWE", type="tag", landmark=True,
         event="WrestleMania 39 Night 1", opponent="Kevin Owens & Sami Zayn",
         stip="Tag — the main event; the 622-day SmackDown reign ends; five stars (Meltzer)",
         title="Undisputed WWE Tag Team Championship"),
    dict(result="W", date="2023-07-01", promo="WWE", type="tag", landmark=True,
         event="Money in the Bank — London", opponent="Roman Reigns & Solo Sikoa",
         stip="Bloodline Civil War — Jey pins Reigns, Reigns' first pinfall loss since 2019",
         title=""),
    dict(result="L", date="2023-08-05", promo="WWE", landmark=True,
         event="SummerSlam — Detroit", opponent="Roman Reigns",
         stip="Tribal Combat — Jimmy pulls him off the table",
         title="Undisputed WWE Universal Championship"),
    dict(result="W", date="2024-04-06", promo="WWE",
         event="WrestleMania 40 Night 1", opponent="Jimmy Uso",
         stip="Brother vs. brother — the Bloodline account settled", title=""),
    dict(result="W", date="2024-09-23", promo="WWE", landmark=True,
         event="Raw", opponent="Bron Breakker",
         stip="Singles — first singles title in 17 years", title="WWE Intercontinental Championship"),
    dict(result="L", date="2024-10-21", promo="WWE",
         event="Raw — Philadelphia", opponent="Bron Breakker",
         stip="Singles — Jacob Fatu's ambush decides it; the 28-day reign ends",
         title="WWE Intercontinental Championship"),
    dict(result="L", date="2025-01-25", promo="WWE",
         event="Saturday Night's Main Event", opponent="Gunther", opponent_html=True,
         stip="Singles — challenge", title="World Heavyweight Championship"),
    dict(result="W", date="2025-02-01", promo="WWE", type="tag", landmark=True,
         event="Royal Rumble — Indianapolis", opponent="The 2025 Royal Rumble field",
         stip="30-man Royal Rumble — from No. 20, last eliminating John Cena", title=""),
    dict(result="W", date="2025-04-19", promo="WWE", landmark=True,
         event="WrestleMania 41 Night 1", opponent="Gunther", opponent_html=True,
         stip="Singles — wins by submission; first world title", title="World Heavyweight Championship"),
    dict(result="L", date="2025-06-09", promo="WWE", landmark=True,
         event="Raw", opponent="Gunther", opponent_html=True,
         stip="Singles — the 51-day reign ends", title="World Heavyweight Championship"),
    dict(result="L", date="2025-11-01", promo="WWE",
         event="Saturday Night's Main Event", opponent="CM Punk", opponent_html=True,
         stip="Singles for the vacated title", title="World Heavyweight Championship"),
    dict(result="W", date="2025-12-29", promo="WWE", type="tag",
         event="Raw", opponent="AJ Styles & Dragon Lee",
         stip="Tag — with Jimmy Uso; a fifth reign together on the Raw lineage",
         title="World Tag Team Championship"),
    dict(result="L", date="2026-03-30", promo="WWE", type="tag",
         event="Raw", opponent="The Vision (Logan Paul & Austin Theory)",
         stip="Street fight — the 91-day reign ends", title="World Tag Team Championship"),
    dict(result="W", date="2026-04-18", promo="WWE", type="tag",
         event="WrestleMania 42 Night 1 — Las Vegas", opponent="Logan Paul, Austin Theory & IShowSpeed",
         stip="Six-man tag — with Jimmy Uso and LA Knight", title=""),
    dict(result="L", date="2026-06-27", promo="WWE",
         event="Night of Champions — Riyadh", opponent="Oba Femi",
         stip="King of the Ring final — Fall From Grace in 7:56", title=""),
    dict(result="L", date="2026-08-01", promo="WWE", type="tag",
         event="SummerSlam Night 1 — Minneapolis", opponent="LA Knight, Solo Sikoa & Royce Keys",
         stip="Six-man tag — with Jimmy Uso and Jacob Fatu for The Bloodline", title=""),
    dict(result="W", date="2026-08-10", promo="WWE",
         event="Raw", opponent="Solo Sikoa",
         stip="Singles — loser delivered to Roman Reigns; Jimmy assists the finish", title=""),
    dict(result="NC", date="2026-08-24", promo="WWE", type="tag",
         event="Raw", opponent="Solo Sikoa & LA Knight",
         stip="Tag — with Jimmy Uso; thrown out when Royce Keys and OTM attack all four", title=""),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Gunther": "gunther", "CM Punk": "cm-punk"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="jey-uso",
    name="Jey Uso",
    realname="Joshua Samuel Fatu",
    epithet="Main Event Jey Uso",
    hook="Record & Titles",

    meta_desc=("Jey Uso won the 2025 Royal Rumble and submitted Gunther at WrestleMania 41 for the "
               "World Heavyweight Championship. Now he wears Roman Reigns' ula fala again in the "
               "reformed Bloodline. Full record, titles, factions, records and career."),
    og_desc=("Main Event Jey Uso: a 622-day tag reign, the 2025 Royal Rumble, a world title won by "
             "submission from Gunther - and a 2026 return to Roman Reigns' side, at war with his own "
             "brother Solo Sikoa."),
    tw_desc="Main Event Jey Uso: 2025 Rumble winner, former World Heavyweight Champion, Bloodline made man again.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2007",
    height_imp="6&#8242;1&#8243;",
    weight_lb="242",
    world_titles="1",
    vitals_tagline="YEET",
    support_note="Merch &middot; Games &middot; Watch",
    sp_items=[
        dict(ic="JU", title="WWE Shop", sub="Yeet tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable across the WWE 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="BL", title="The Bloodline story", sub="The 2020-2026 saga, ongoing on Raw",
             tag="Watch", href="https://www.wwe.com/shows/raw"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/jey-uso"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="One half of The Usos &middot; Right Hand Man &middot; YEET",
    hero_tag="San Francisco, California &middot; <em>WXW &middot; FCW &middot; WWE &middot; "
             "2007&ndash;present &middot; Anoa&#699;i family</em>",
    now_label="NOW",
    now_bold="Raw, The Bloodline, no championship",
    now_tail=" &middot; a made man again under Roman Reigns, at war with his brother Solo Sikoa and "
             "LA Knight &mdash; and, since August 24, with the debuting Royce Keys and OTM",
    hstats=[
        dict(value="1",   x=True,  label="World Title"),
        dict(value="1",   x=True,  label="Royal Rumble Win"),
        dict(value="622", x=False, label="Day Tag Reign"),
        dict(value="10",  x=True,  label="Tag Title Reigns"),
    ],
    ghost_link="From twin tag act to the man who made Gunther tap",
    vlabel="Est. 2007 &middot; San Francisco, California",
    mono="JU",

    # ---------------------------------------------------------------- 01 overview
    # index into overview of the correction paragraph -> the framed
    # "Setting one thing straight" callout (aside.corr) on the page
    correction=1,
    overview=[
        "<b>Jey Uso</b> has spent six years as the emotional centre of WWE's biggest story, usually "
        "against his will. He is one half of The Usos, the most decorated twin act the company has "
        "produced; the first man Roman Reigns broke to build The Bloodline in 2020; the first to walk "
        "out of it in 2023; and, in 2025, the payoff &mdash; a Royal Rumble win from No. 20 and a "
        "World Heavyweight Championship won by making Gunther tap in the opening match of "
        "WrestleMania 41. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">622</span>'
        '<span class="pull-cap">days as SmackDown Tag Team Champions with Jimmy &mdash; the longest male tag reign in WWE history</span></span>'
        "In 2026 the wheel has turned again: he and Jimmy stand inside a reformed "
        "Bloodline at Reigns&rsquo; right hand, wearing the ula fala of made men, in a civil war "
        "against their own brother Solo Sikoa and LA Knight.",

        "The tag record needs stating precisely, because it is usually inflated. The Usos&rsquo; "
        "fifth SmackDown Tag Team Championship reign ran July 18, 2021 to April 1, 2023 &mdash; "
        "<b>622 days</b>, ended by Kevin Owens and Sami Zayn in the WrestleMania 39 Night 1 main "
        "event &mdash; and the title histories log it as the longest <b>male</b> tag team reign in "
        "WWE history, not the longest outright, a qualifier most retellings drop. For part of it, "
        "from May 20, 2022, they held the Raw titles too as Undisputed champions. Jey&rsquo;s "
        "singles ledger is younger than his fame: his first singles championship of any kind came on "
        "September 23, 2024 &mdash; the Intercontinental title, seventeen years into his career "
        "&mdash; and his world title reign lasted 51 days before Gunther took it back on the June 9, "
        "2025 Raw.",

        "He was born Joshua Samuel Fatu in San Francisco on August 22, 1985, ten minutes around his "
        "twin Jonathan &mdash; Jimmy &mdash; sons of Rikishi, grandsons of the Anoa&#699;i "
        "wrestling dynasty that also produced Roman Reigns, their cousin, and Solo Sikoa, their "
        "younger brother. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">51</span>'
        '<span class="pull-cap">days as World Heavyweight Champion in 2025, with defences against Seth Rollins and Logan Paul</span></span>'
        "The twins debuted in 2007, reached WWE&rsquo;s main roster in 2010, and "
        "spent a decade as a superb, occasionally directionless tag team before the October 25, 2020 "
        "Hell in a Cell I Quit match &mdash; Reigns torturing Jey into submission &mdash; turned "
        "them into the foundation of the Bloodline story. Everything since flows from that night: "
        "the WarGames battles with Owens and Zayn, Jey pinning Reigns clean at Money in the Bank "
        "2023 in the Bloodline Civil War, the Tribal Combat loss at SummerSlam 2023 when Jimmy "
        "turned on him, the &ldquo;Main Event&rdquo; solo run on Raw with the arena-wide YEET "
        "chant.",

        "The 2026 story is the uncomfortable sequel. The twins reunited in December 2025, won the "
        "World Tag Team Championship from AJ Styles and Dragon Lee on December 29, and &mdash; after "
        "losing the belts to The Vision in a March street fight and beating them back with LA Knight "
        "at WrestleMania 42 &mdash; rejoined a reformed Bloodline under Reigns, now the World "
        "Heavyweight Champion, alongside Jacob Fatu. Knight spent the summer telling them they had "
        "seen this movie; Solo Sikoa said it louder. On August 10 Jey beat Solo with the stakes that "
        "the loser be &ldquo;delivered&rdquo; to Reigns; on August 17 the delivery blew up &mdash; "
        "Solo spiked Reigns and stood with Knight, minutes after Reigns had draped ula falas on the "
        "twins; and on August 24 the debuting Royce Keys and OTM flattened all four men in a "
        "no-contest. As of August 31, 2026 Jey holds no championship and stands, once again, exactly "
        "where the story needs him: in the middle.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("622",       "Day tag reign"),
            ("1",         "World title"),
            ("1",         "Royal Rumble"),
            ("10&times;", "Tag reigns, with Jimmy"),
            ("2024",      "First singles title"),
            ("2007",      "First match"),
        ],
        lead=("Twenty-one documented bouts &mdash; the I Quit match that built The Bloodline, the "
              "Civil War pin on Reigns, both ends of the world title reign, and the 2026 civil war "
              "in progress. This is a curated ledger, not a career count, and no career "
              "win&ndash;loss total is published because no verified one exists. The October 2024 "
              "Intercontinental loss is dated October 21 per the results archives; one automated "
              "read gave October 7 and is not followed. Filter by match type, tap any column header "
              "to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The rated peaks, as reproduced in published Observer round-ups &mdash; almost "
                    "all of them tags, which is the shape of the career. Ratings are as reported, "
                    "not re-checked against archives."),
    signature=[
        dict(rating="5.0", event="WrestleMania 39 Night 1", opponent="Kevin Owens & Sami Zayn",
             stip="Undisputed Tag Team Championship, with Jimmy Uso — the main event; the 622 days end"),
        dict(rating="4.5", event="Money in the Bank 2023 — London", opponent="Roman Reigns & Solo Sikoa",
             stip="Bloodline Civil War — Jey pins Reigns"),
        dict(rating="4.5", event="Money in the Bank 2022", opponent="The Street Profits",
             stip="Undisputed Tag Team Championship, with Jimmy Uso"),
        dict(rating="4.5", event="WrestleMania Backlash 2022", opponent="Drew McIntyre, Randy Orton & Riddle",
             stip="Six-man tag, with Roman Reigns and Jimmy Uso"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("1",         "World Heavyweight reign"),
            ("622",       "Day tag reign"),
            ("10&times;", "Tag reigns with Jimmy"),
            ("2024",      "First singles gold"),
        ],
        lead=("A tag resume with few equals and a singles column that only started filling in 2024. "
              "Tag reign counts follow the published title histories; the SmackDown lineage list "
              "below rolls the pre-2019 reigns together where exact endpoints were not verified in "
              "this pass."),
        rows=[
            dict(ic="H", name="World Heavyweight Championship", count="1",
                 sub="April 19 &ndash; June 9, 2025 &middot; won from Gunther by submission in the "
                     "opening match of WrestleMania 41 Night 1, lost it back to Gunther on Raw "
                     "&middot; <b>51 days</b>, with defences against Seth Rollins and Logan Paul"),
            dict(ic="I", name="WWE Intercontinental Championship", count="1",
                 sub="September 23 &ndash; October 21, 2024 &middot; won from Bron Breakker on Raw "
                     "&mdash; his first singles title, 17 years in &mdash; lost it back in "
                     "Philadelphia after Jacob Fatu's ambush &middot; 28 days"),
            dict(ic="S", name="SmackDown Tag Team Championship", count="5",
                 sub="All with Jimmy Uso &middot; first reign won March 21, 2017 &middot; the fifth, "
                     "July 18, 2021 &ndash; April 1, 2023, ran <b>622 days</b> &mdash; the longest "
                     "male tag team reign in WWE history &mdash; and ended against Owens and Zayn "
                     "in the WrestleMania 39 main event"),
            dict(ic="R", name="Raw / WWE Tag Team Championship lineage", count="4",
                 sub="With Jimmy except where noted &middot; 2014, a 202-day reign &middot; "
                     "2014&ndash;15 &middot; 2022, won May 20 by beating RK-Bro to become "
                     "Undisputed champions alongside the SmackDown belts &middot; 2023, a 9-day "
                     "reign with Cody Rhodes from Fastlane, October 7&ndash;16"),
            dict(ic="W", name="World Tag Team Championship", count="1",
                 sub="December 29, 2025 &ndash; March 30, 2026, with Jimmy &middot; won from AJ "
                     "Styles & Dragon Lee on Raw, lost to The Vision in a street fight &middot; 91 "
                     "days &middot; the tenth Uso reign overall"),
            dict(ic="F", name="FCW Florida Tag Team Championship", count="1",
                 sub="March 13 &ndash; June 3, 2010, with Jimmy, in WWE's developmental territory"),
            dict(ic="A", name="Andre the Giant Memorial Battle Royal", count="1",
                 sub="Won April 9, 2021 on the WrestleMania 37 week SmackDown"),
            dict(ic="K", name="King of the Ring", count="0",
                 sub="Runner-up, 2026 &middot; lost the final to Oba Femi at Night of Champions in "
                     "Riyadh on June 27, in 7:56"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="One tag team for life, and two versions of the same family empire — one he escaped, "
             "one he walked back into.",
        cards=[
            dict(era="WWE &middot; 2010&ndash;present",
                 name="The Usos",
                 members="Jey Uso, Jimmy Uso",
                 desc="The twin act: ten tag championship reigns across three lineages, the 622-day "
                      "SmackDown reign, and a genuine claim to being WWE's defining tag team of the "
                      "2010s and 2020s. Split by the Bloodline story in 2023-24 - including Jey "
                      "beating Jimmy at WrestleMania 40 - and reunited on the December 8, 2025 Raw. "
                      "Wrestling's rare tag team whose breakup and reunion both headlined."),
            dict(era="WWE &middot; 2020&ndash;2023",
                 name="The Bloodline (original)",
                 members="Roman Reigns, Jey Uso, Jimmy Uso, Solo Sikoa, Paul Heyman, Sami Zayn "
                         "(honorary)",
                 desc="Built on Jey's broken will: after the Hell in a Cell I Quit match in October "
                      "2020 he became the first follower, then the conscience, then the first to "
                      "leave - superkicking Reigns in June 2023 and pinning him at Money in the "
                      "Bank. The Tribal Combat loss at SummerSlam 2023, with Jimmy's betrayal, "
                      "closed his chapter of the original story."),
            dict(era="WWE &middot; 2026&ndash;present",
                 name="The Bloodline (reformed)",
                 members="Roman Reigns, Jey Uso, Jimmy Uso, Jacob Fatu",
                 desc="Reformed after WrestleMania 42 around Reigns, now World Heavyweight Champion "
                      "- with the twins as enforcers and, since August 17, official made men with "
                      "ula falas. LA Knight spent the summer telling them it is the same movie; "
                      "their brother Solo Sikoa proved the point by spiking Reigns during his own "
                      "'delivery.' The debut attack by Royce Keys and OTM on August 24 hit "
                      "Bloodline and rebels alike, and is the wild card in the story as of August "
                      "31, 2026."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One ring name since 2010 and four distinct men inside it &mdash; the arc is the "
             "character.",
        cards=[
            dict(mono="US", era="WWE &middot; 2010&ndash;2020", name="The Uso twin",
                 desc="Face-painted, interchangeable-by-design half of a great tag team - Samoan "
                      "dance entrances early, the Day One Ish era later. Ten years of craft with "
                      "almost no singles identity, which made what came next land harder."),
            dict(mono="RH", era="WWE &middot; 2020&ndash;2023", name="Right Hand Man",
                 desc="The first Bloodline convert: beaten into loyalty in the I Quit match, then "
                      "Reigns' enforcer with a visible conscience. The role that turned a career "
                      "tag wrestler into the best long-form actor on the roster."),
            dict(mono="ME", era="WWE &middot; 2023&ndash;2025", name="Main Event Jey Uso",
                 desc="The solo run: the self-bestowed nickname made literal on Raw, the YEET "
                      "call-and-response that swallowed arenas, the through-the-crowd entrance, "
                      "then the 2025 Royal Rumble and the WrestleMania 41 world title. WWE's most "
                      "over act of 2024-25 by crowd volume, with a Slammy for Most Aura of the "
                      "Year."),
            dict(mono="MM", era="WWE &middot; 2026&ndash;present", name="The made man",
                 desc="Back at Reigns' side with the ula fala and a hardening edge - fighting his "
                      "own brother Solo on the Tribal Chief's behalf. Whether it is loyalty or "
                      "relapse is the open question the story is currently asking."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Twin tag act to Rumble winner to made man, with every turn televised.",
        rows=[
            dict(year="2007", title="Debut",
                 desc="First matches with brother Jimmy in June 2007, trained by their father "
                      "Rikishi; the twins sign with WWE and win FCW tag gold in 2010."),
            dict(year="2010", title="Main roster",
                 desc="The Usos debut as a team and spend the decade collecting tag titles - "
                      "first Raw lineage reign in 2014, first SmackDown reign in 2017."),
            dict(year="2020", title="The I Quit match",
                 desc="Roman Reigns forces the words out of him at Hell in a Cell on October 25, "
                      "and The Bloodline is born from the surrender."),
            dict(year="2021", title="The 622 days begin",
                 desc="The Usos win the SmackDown Tag Team Championship on July 18, 2021 and do not "
                      "lose it for 622 days; Jey also wins the Andre battle royal in April."),
            dict(year="2022", title="Undisputed",
                 desc="Beat RK-Bro in a Winners Take All match on the May 20 SmackDown to hold both "
                      "tag lineages at once."),
            dict(year="2023", title="Civil War, Tribal Combat, exit",
                 desc="Loses the WrestleMania 39 main event to Owens and Zayn; superkicks Reigns in "
                      "June; pins him at Money in the Bank on July 1; loses Tribal Combat at "
                      "SummerSlam on August 5 when Jimmy turns; moves to Raw alone."),
            dict(year="2024", title="Main Event Jey; first singles gold",
                 desc="Beats Jimmy at WrestleMania 40 on April 6, then beats Bron Breakker on the "
                      "September 23 Raw for the Intercontinental Championship - his first singles "
                      "title, lost back on October 21 after Jacob Fatu's ambush."),
            dict(year="2025", title="Rumble and the world title",
                 desc="Wins the Royal Rumble from No. 20 on February 1, last eliminating John Cena; "
                      "submits Gunther at WrestleMania 41 on April 19 for the World Heavyweight "
                      "Championship; loses it back on June 9. Loses the vacated-title match to CM "
                      "Punk at Saturday Night's Main Event on November 1. Reunites with Jimmy in "
                      "December and wins tag gold on December 29."),
            dict(year="2026", title="The reformed Bloodline and the family war",
                 desc="Loses the tag titles to The Vision on March 30, wins the WrestleMania 42 "
                      "six-man with LA Knight on April 18, rejoins Reigns' reformed Bloodline, "
                      "loses the King of the Ring final to Oba Femi on June 27 - then spends August "
                      "fighting his brother Solo: a win on August 10, the failed delivery on August "
                      "17, and the OTM ambush on August 24."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with — mostly his own family.",
        cards=[
            dict(name="Roman Reigns",
                 desc="The relationship the whole saga runs on. Reigns broke him in the 2020 I Quit "
                      "match, made him Right Hand Man, and lost his first pinfall since 2019 to him "
                      "in the Bloodline Civil War at Money in the Bank on July 1, 2023; the Tribal "
                      "Combat title match at SummerSlam followed on August 5. In 2026 Jey took the "
                      "ula fala from the same hands - the story's point being that both things are "
                      "true at once."),
            dict(name="Jimmy Uso",
                 desc="Twin, partner in ten tag reigns, and twice the knife: Jimmy's SummerSlam "
                      "2023 betrayal cost Jey Tribal Combat, and Jey beat him one-on-one at "
                      "WrestleMania 40 Night 1 on April 6, 2024. Reunited since December 2025 - "
                      "currently made men together, which given this family guarantees nothing."),
            dict(name="Solo Sikoa",
                 desc="The little brother, and the 2026 civil war. Jey beat him on the August 10 "
                      "Raw with delivery to Reigns as the stakes; on August 17 Solo answered the "
                      "ceremony with a Samoan Spike to the Tribal Chief and sided with LA Knight; "
                      "the August 24 tag rematch died under the OTM ambush. Active and "
                      "unresolved."),
            dict(name="Gunther", slug="gunther",
                 desc="The credibility test passed on the third try: title-match losses in December "
                      "2023 and January 2025, then the WrestleMania 41 Night 1 submission win on "
                      "April 19, 2025 - Gunther's first WrestleMania loss and Jey's first world "
                      "title. Gunther took the belt back on the June 9 Raw, keeping the series "
                      "honest."),
            dict(name="Kevin Owens & Sami Zayn",
                 desc="The opposition of the Bloodline's golden era: WarGames 2022, the WrestleMania "
                      "39 Night 1 main event where the 622 days ended, and the awards-sweeping feud "
                      "of 2023. The rare rivalry where every man involved got over."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Thin by design — the verified list is short, and nothing is added to pad it.",
        rows=[
            dict(when="2011&ndash;", title="WWE 2K", kind="Game",
                 desc="A playable roster regular across the WWE 2K series, usually within a ratings "
                      "point of his twin."),
            dict(when="2023&ndash;", title="YEET", kind="Catchphrase",
                 desc="The call-and-response that defined the Main Event Jey run and turned his "
                      "entrance - through the crowd, arena bouncing - into the loudest sustained "
                      "pop of the 2024-25 television cycle."),
            dict(when="2025", title="Slammy Awards", kind="Honours",
                 desc="Most Aura of the Year, plus Faction of the Year with the OG Bloodline, per "
                      "the 2025 Slammys."),
            dict(when="2020&ndash;", title="The Bloodline coverage cycle", kind="Coverage",
                 desc="The 2020 Reigns feud took CBS Sports' Feud of the Year; the 2023 Bloodline "
                      "vs. Owens/Zayn program took the Observer's. No film roles, autobiography or "
                      "podcast could be verified, so none are listed."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, with their qualifiers attached — including the one everybody quotes "
             "without the word that makes it true.",
        stats=[
            ("622", "Day tag reign"),
            ("1",   "Royal Rumble win"),
            ("51",  "Day world title reign"),
        ],
        rows=[
            dict(name="Longest male tag team championship reign in WWE history — 622 days",
                 sub="July 18, 2021 to April 1, 2023, with Jimmy, on the SmackDown lineage - ended "
                     "by Owens and Zayn in the WrestleMania 39 Night 1 main event. The qualifier "
                     "male is the title histories' own, and it is the part most retellings drop."),
            dict(name="2025 Royal Rumble winner",
                 sub="February 1, 2025, from No. 20, last eliminating John Cena - the win that "
                     "converted the YEET run into a main event."),
            dict(name="Made Gunther submit at WrestleMania 41",
                 sub="April 19, 2025, opening match of Night 1 - his first world championship, and "
                     "Gunther's first defeat at a WrestleMania. Held 51 days with defences against "
                     "Seth Rollins and Logan Paul."),
            dict(name="First pinfall on Roman Reigns since December 2019",
                 sub="Money in the Bank, July 1, 2023, in the Bloodline Civil War tag - the pin "
                     "that proved the Tribal Chief could lose. Reigns' singles streak itself "
                     "survived until WrestleMania 40."),
            dict(name="Ten tag championship reigns with Jimmy Uso",
                 sub="Five SmackDown, three Raw lineage as a twin act plus Jey's Fastlane 2023 "
                     "reign with Cody Rhodes, and the 2025-26 World Tag Team reign - across three "
                     "different title lineages, plus FCW gold in developmental."),
            dict(name="Seventeen years to a first singles title",
                 sub="Debut 2007; first singles championship September 23, 2024, beating Bron "
                     "Breakker for the Intercontinental title - the longest apprenticeship of any "
                     "modern WWE world champion's road."),
            dict(name="Both Bloodline civil wars",
                 sub="Fought Reigns and Solo in 2023's Civil War tag and won; fighting Solo again "
                     "in 2026 from the other side of the family line - the only man to headline "
                     "the family fight from both directions."),
        ],
        footnote=("Deliberately absent: a career win-loss total, because no verified figure exists; "
                  "the exact endpoints of the 2017-19 SmackDown tag reigns, which were not "
                  "verified in this pass and are rolled into the reign count; and any result from "
                  "the August 31, 2026 Ottawa Raw, which had not aired when this page was "
                  "compiled."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography",
             href="https://en.wikipedia.org/wiki/Jey_Uso"),
        dict(k="PWTorch", v="Raw, August 17, 2026 — the delivery backfires",
             href="https://www.pwtorch.com/site/2026/08/17/wwe-raw-results-8-17-kellers-report-on-jey-uso-delivering-solo-sikoa-to-roman-reigns-sol-vs-lyra-chad-gable-vs-rey-mysterio-for-ic-title/"),
        dict(k="CBS Sports", v="Raw, August 24, 2026 — the OTM ambush",
             href="https://www.cbssports.com/wwe/news/wwe-raw-live-updates-results-review-grades-august-24-oba-femi-bron-breakker/live/"),
        dict(k="WWE.com", v="Raw, August 10, 2026 — Jey vs. Solo, delivery stakes",
             href="https://www.wwe.com/shows/raw/2026-08-10"),
        dict(k="TPWW", v="Raw, October 21, 2024 — the Intercontinental title loss",
             href="https://www.tpww.net/2024/10/wwe-raw-results-oct-21-2024-jey-uso-vs-bron-breakker/"),
        dict(k="Yahoo Sports", v="Night of Champions 2026 — King of the Ring final",
             href="https://sports.yahoo.com/wrestling/live/wwe-night-of-champions-2026-live-results-updates-grades-analysis-for-cody-rhodes-vs-gunther-vs-sami-zayn-060000373.html"),
        dict(k="TJR Wrestling", v="Observer ratings, Money in the Bank 2023",
             href="https://tjrwrestling.net/news/wwe-money-in-the-bank-dave-meltzer/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Jey Uso back in The Bloodline?",
            a="Yes &mdash; the reformed 2026 version, with Jimmy Uso and Jacob Fatu around Roman "
              "Reigns, who is the current World Heavyweight Champion. On the August 17, 2026 Raw, "
              "Reigns presented both twins with ula falas as &ldquo;made men.&rdquo; The same "
              "segment blew up: their younger brother <b>Solo Sikoa</b>, whom the twins had "
              "&ldquo;delivered&rdquo; to Reigns as punishment, hit Reigns with a Samoan Spike and "
              "sided with LA Knight against the group. A week later the debuting Royce Keys and "
              "OTM attacked Bloodline and rebels alike. As of August 31, 2026, Jey is a Bloodline "
              "made man in a three-sided war.",
            q_ld="Is Jey Uso a member of The Bloodline in 2026?",
            a_ld="Yes. Jey Uso rejoined a reformed Bloodline after WrestleMania 42 in April 2026, "
                 "alongside Jimmy Uso and Jacob Fatu, led by Roman Reigns, the current World "
                 "Heavyweight Champion. On the August 17, 2026 Raw, Reigns presented Jey and Jimmy "
                 "with ula falas as made men. In the same segment their brother Solo Sikoa "
                 "attacked Reigns with a Samoan Spike and aligned with LA Knight against the "
                 "group, and on August 24 the debuting faction of Royce Keys and OTM attacked all "
                 "sides, leaving the storyline a three-way conflict."),
        dict(
            q="How did Jey Uso win the World Heavyweight Championship, and how long did he hold it?",
            a="He made <b>Gunther</b> submit in the opening match of WrestleMania 41 Night 1 on "
              "April 19, 2025 &mdash; his first world championship, and Gunther&rsquo;s first "
              "WrestleMania loss &mdash; after winning the 2025 Royal Rumble from No. 20 on "
              "February 1, last eliminating John Cena. The reign ran <b>51 days</b>, with "
              "successful defences against Seth Rollins and Logan Paul, before Gunther beat him "
              "for the title on the June 9, 2025 Raw.",
            q_ld="How did Jey Uso win the World Heavyweight Championship and how long did he hold it?",
            a_ld="Jey Uso won the World Heavyweight Championship by making Gunther submit in the "
                 "opening match of WrestleMania 41 Night 1 on April 19, 2025, after winning the "
                 "2025 Royal Rumble on February 1 from the No. 20 position, last eliminating John "
                 "Cena. It was his first world championship. He held the title for 51 days, "
                 "defending it against Seth Rollins and Logan Paul, and lost it back to Gunther on "
                 "the June 9, 2025 episode of Raw."),
        dict(
            q="Do The Usos hold the longest tag team title reign in WWE history?",
            a="With the qualifier, yes. Their fifth SmackDown Tag Team Championship reign &mdash; "
              "July 18, 2021 to April 1, 2023, <b>622 days</b> &mdash; is logged by the title "
              "histories as the longest <b>male</b> tag team championship reign in WWE history. It "
              "ended against Kevin Owens and Sami Zayn in the main event of WrestleMania 39 Night "
              "1. From May 20, 2022 they also held the Raw titles simultaneously as Undisputed "
              "champions. Overall the twins have ten reigns together across three lineages.",
            q_ld="Do The Usos hold the longest tag team championship reign in WWE history?",
            a_ld="The Usos hold the longest male tag team championship reign in WWE history: 622 "
                 "days as SmackDown Tag Team Champions, from July 18, 2021 to April 1, 2023, when "
                 "Kevin Owens and Sami Zayn beat them in the main event of WrestleMania 39 Night "
                 "1. From May 20, 2022 they simultaneously held the Raw Tag Team Championship as "
                 "Undisputed WWE Tag Team Champions. The 'male' qualifier is how WWE's title "
                 "histories record it."),
        dict(
            q="What is happening between Jey Uso and Solo Sikoa?",
            a="A family civil war, live on Raw. Solo rejected the reformed Bloodline; Jey beat him "
              "on the August 10, 2026 Raw under &ldquo;loser gets delivered to Roman Reigns&rdquo; "
              "stakes, with Jimmy assisting the finish. At the delivery on August 17, Solo spiked "
              "Reigns, dumped the twins from the ring and stood with LA Knight. The August 24 tag "
              "match &mdash; Usos against Solo and Knight &mdash; ended in a no-contest when Royce "
              "Keys and OTM, debuting from NXT, attacked everyone with the ring steps. Solo and "
              "Knight had already beaten the Bloodline&rsquo;s trio at SummerSlam on August 1.",
            q_ld="What is the storyline between Jey Uso and Solo Sikoa in 2026?",
            a_ld="Jey Uso and his younger brother Solo Sikoa are on opposite sides of a Bloodline "
                 "civil war. Jey defeated Solo on the August 10, 2026 Raw in a match with the "
                 "stipulation that the loser be delivered to Roman Reigns. During the delivery on "
                 "August 17, Solo attacked Reigns with a Samoan Spike and aligned with LA Knight. "
                 "A tag match between The Usos and Solo Sikoa and LA Knight on August 24 ended in "
                 "a no-contest when the debuting Royce Keys and OTM attacked all four men. Knight, "
                 "Solo and Royce Keys had earlier defeated the Bloodline's Jey, Jimmy and Jacob "
                 "Fatu at SummerSlam Night 1 on August 1, 2026."),
        dict(
            q="When did Jey Uso win his first singles title?",
            a="September 23, 2024 &mdash; seventeen years after his debut. He beat Bron Breakker on "
              "Raw for the Intercontinental Championship, his first singles championship at any "
              "level of WWE, and lost it back to Breakker in Philadelphia on October 21 after "
              "Jacob Fatu ambushed him at ringside. The world title followed within seven months.",
            q_ld="When did Jey Uso win his first singles championship?",
            a_ld="Jey Uso won his first singles championship on September 23, 2024, defeating Bron "
                 "Breakker on Raw for the WWE Intercontinental Championship, seventeen years after "
                 "his 2007 debut. He lost the title back to Breakker on the October 21, 2024 Raw "
                 "in Philadelphia after interference by Jacob Fatu. He won his first world "
                 "championship at WrestleMania 41 on April 19, 2025."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Joshua Samuel Fatu"),
        dict(label="Born", value="August 22, 1985", sub="San Francisco, California &middot; age 41 "
                                                        "&middot; twin of Jimmy Uso"),
        dict(label="Billed from", value="San Francisco, California"),
        dict(label="Height", value="6&#8242;1&#8243;", sub="185 cm"),
        dict(label="Weight", value="242 lb", sub="110 kg (billed)"),
        dict(label="Debut", value="June 8, 2007", sub="with Jimmy, as Josh Fatu"),
        dict(label="Trained by", value="Rikishi", sub="his father, WWE Hall of Famer Solofa Fatu "
                                                      "Jr."),
        dict(label="Family", value="Anoa&#699;i dynasty",
             sub="Twin of Jimmy Uso &middot; brother of Solo Sikoa &middot; cousin of Roman Reigns "
                 "&middot; grandson of Afa"),
        dict(label="Signature", value="Uso Splash &middot; Superkick &middot; Spear &middot; 1D "
                                      "with Jimmy"),
        dict(label="Brand", value="Raw"),
        dict(label="Also known as", value="Main Event Jey Uso &middot; Right Hand Man &middot; "
                                          "YEET"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1985-08-22",
    bornplace="San Francisco, California",
    nationality="United States",
    height_cm=185,
    weight_kg=110,
    ld=dict(
        alternateName=["Joshua Samuel Fatu", "Josh Fatu", "Jules Uso", "Main Event Jey Uso",
                       "Right Hand Man"],
        award=["World Heavyweight Championship (1 reign, 51 days, 2025)",
               "WWE Intercontinental Championship (1 reign)",
               "Royal Rumble winner (2025)",
               "SmackDown Tag Team Championship (5 reigns, with Jimmy Uso; one of 622 days, the "
               "longest male tag reign in WWE history)",
               "Raw / WWE Tag Team Championship (4 reigns)",
               "World Tag Team Championship (1 reign, 2025-26)",
               "Andre the Giant Memorial Battle Royal (2021)",
               "FCW Florida Tag Team Championship (1 reign)",
               "Slammy Award for Most Aura of the Year (2025)"],
        knowsAbout=["Professional wrestling", "WWE", "The Bloodline", "The Usos", "Tag team "
                    "wrestling", "Anoa'i family", "Championship wrestling"],
        description="Jey Uso, born Joshua Samuel Fatu in San Francisco, is an American professional "
                    "wrestler signed to WWE and one half of The Usos with his twin brother Jimmy. "
                    "A member of the Anoa'i family and son of Rikishi, he holds ten tag team "
                    "championship reigns including a record 622-day SmackDown reign, won the 2025 "
                    "Royal Rumble, and defeated Gunther by submission at WrestleMania 41 for the "
                    "World Heavyweight Championship. In 2026 he is part of Roman Reigns' reformed "
                    "Bloodline, in a storyline war with his brother Solo Sikoa.",
        sameAs=["https://en.wikipedia.org/wiki/Jey_Uso",
                "https://www.wwe.com/superstars/jey-uso"],
    ),
)
