# -*- coding: utf-8 -*-
"""Jacob Fatu - dossier data.

Sources: web research compiled August 31, 2026 - Wikipedia's Jacob Fatu and MLW World
Heavyweight Championship articles plus 411Mania, WrestleZone, POST Wrestling and CBS
Sports coverage. Every match row carries a day-precision date stated in one of the
opened sources.

Deliberate omissions:
  * No career win-loss total - no verified figure exists.
  * Battle Riot IV: Wikipedia's summary dates his win November 3, 2022, which could not
    be corroborated against MLW's own records in this pass; the win is listed in feats
    without a date rather than with a doubtful one.
  * The nature of the late-2025 injury was never disclosed - reported October 16, 2025
    as non-wrestling-related with specifics kept private - and no diagnosis is invented.
  * No social handles - official accounts were not verified in this pass.
"""

# ----------------------------------------------------------------- record rows
# MLW bookends first, then the WWE run. The two MLW rows are the reign's endpoints as
# Wikipedia's title-history table states them; the WWE rows follow the article and the
# event coverage opened for this file.
ROWS = [
    dict(result="W", date="2019-07-06", promo="MLW", landmark=True,
         event="MLW Fusion — Kings of Colosseum", opponent="Tom Lawlor",
         stip="Singles — the 819-day reign begins", title="MLW World Heavyweight Championship"),
    dict(result="L", date="2021-10-02", promo="MLW", landmark=True,
         event="MLW Fightland — Philadelphia", opponent="Alexander Hammerstone",
         stip="Title vs. title — the longest reign in MLW history ends",
         title="MLW World Heavyweight Championship"),
    dict(result="W", date="2024-07-06", promo="WWE", type="tag", landmark=True,
         event="Money in the Bank — Toronto", opponent="Cody Rhodes, Randy Orton & Kevin Owens",
         stip="Six-man — in-ring WWE debut, with Solo Sikoa & Tama Tonga", title=""),
    dict(result="W", date="2024-08-02", promo="WWE", type="tag", landmark=True,
         event="SmackDown", opponent="DIY",
         stip="Tag — with Tama Tonga", title="WWE Tag Team Championship"),
    dict(result="L", date="2024-10-25", promo="WWE", type="tag",
         event="SmackDown", opponent="The Motor City Machine Guns",
         stip="Tag — with Tama Tonga; the 84-day reign ends", title="WWE Tag Team Championship"),
    dict(result="L", date="2024-11-30", promo="WWE", type="tag",
         event="Survivor Series: WarGames", opponent="The OG Bloodline & CM Punk",
         stip="WarGames — with Solo Sikoa's Bloodline", title=""),
    dict(result="W", date="2025-04-19", promo="WWE", landmark=True,
         event="WrestleMania 41 Night 1", opponent="LA Knight",
         stip="Singles — first WWE singles title", title="WWE United States Championship"),
    dict(result="L", date="2025-06-28", promo="WWE", landmark=True,
         event="Night of Champions — Riyadh", opponent="Solo Sikoa",
         stip="Singles — the 70-day reign ends", title="WWE United States Championship"),
    dict(result="L", date="2025-08-03", promo="WWE",
         event="SummerSlam Night 2", opponent="Solo Sikoa",
         stip="Steel cage — challenge", title="WWE United States Championship"),
    dict(result="W", date="2026-04-18", promo="WWE", landmark=True,
         event="WrestleMania 42 Night 1", opponent="Drew McIntyre",
         stip="Unsanctioned match", title=""),
    dict(result="L", date="2026-05-09", promo="WWE", landmark=True,
         event="Backlash", opponent="Roman Reigns",
         stip="Singles — challenge", title="World Heavyweight Championship"),
    dict(result="L", date="2026-08-01", promo="WWE", type="tag",
         event="SummerSlam Night 1 — Minneapolis", opponent="Solo Sikoa, LA Knight & Royce Keys",
         stip="Six-man — with The Usos", title=""),
]

DATA = dict(
    slug="jacob-fatu",
    name="Jacob Fatu",
    realname="Jacob Fatu",
    epithet="The Samoan Werewolf",
    hook="Record & Titles",

    meta_desc=("Jacob Fatu, the Samoan Werewolf, held the MLW World Heavyweight Championship for a "
               "record 819 days and the WWE United States Championship for 70. Full record, titles, "
               "factions, records and career."),
    og_desc=("The Samoan Werewolf: an 819-day MLW World Heavyweight reign - the longest in that "
             "promotion's history - a United States Championship, and a place in every version of "
             "the Bloodline since 2024."),
    tw_desc="The Samoan Werewolf: 819 days as MLW World Champion, 70 as WWE United States Champion.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2012",
    height_imp="6&#8242;2&#8243;",
    weight_lb="285",
    world_titles="1",
    vitals_tagline="The Werewolf runs at night",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="JF", title="WWE Shop", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable in the current 2K entries",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="W", title="Wikipedia", sub="Full biography", tag="Read",
             href="https://en.wikipedia.org/wiki/Jacob_Fatu"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/jacob-fatu"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Samoan Werewolf &middot; ex-Contra Unit &middot; the Bloodline's wildest weapon",
    hero_tag="Sacramento, California &middot; <em>Independents &middot; MLW &middot; WWE &middot; "
             "2012&ndash;present</em>",
    now_label="NOW",
    now_bold="Raw, in Roman Reigns' Bloodline — and wavering",
    now_tail=" &middot; stood in the corner while Solo Sikoa spiked Reigns on August 17, and was told "
             "to stay backstage by The Usos a week later",
    hstats=[
        dict(value="819", x=False, label="Day MLW World Reign"),
        dict(value="70",  x=False, label="Day US Reign"),
        dict(value="1",   x=True,  label="World Title"),
        dict(value="3",   x=False, label="Bloodline Versions"),
    ],
    ghost_link="From the Contra Unit to the last man standing in Roman's corner",
    vlabel="Est. 2012 &middot; Sacramento, California",
    mono="JF",

    # ---------------------------------------------------------------- 01 overview
    # index into overview of the correction paragraph -> the framed
    # "Setting one thing straight" callout (aside.corr) on the page
    correction=1,
    overview=[
        "<b>Jacob Fatu</b> is a 285-pound man who does moonsaults, and for five years that sentence "
        "was the whole sales pitch. The fuller record: he held the MLW World Heavyweight Championship "
        "for <b>819 days</b> &mdash; July 6, 2019 to October 2, 2021, the longest reign in that "
        "promotion's history &mdash; as the masked ace of the Contra Unit, then arrived in WWE on the "
        "June 21, 2024 SmackDown as the wildest weapon in Solo Sikoa's Bloodline. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">819</span>'
        '<span class="pull-cap">days as MLW World Heavyweight Champion &mdash; the longest reign in the '
        'promotion&rsquo;s history</span></span>'
        "Within a year of the WWE debut he had a Tag Team Championship with Tama Tonga, ESPN's Debut "
        "of the Year award, and the United States Championship, won from LA Knight at WrestleMania "
        "41. He is the son of Sam Fatu &mdash; the Tonga Kid &mdash; which makes him Solo Sikoa's "
        "cousin and a member of the Anoa'i dynasty whose 2026 civil war he is currently standing in "
        "the middle of, on Roman Reigns' side, for now.",

        "One date needs setting straight, because the sources disagree by five days. Wikipedia's "
        "Jacob Fatu article says he lost the MLW World Heavyweight Championship to Alexander "
        "Hammerstone on <b>October 7, 2021</b>. The MLW World Heavyweight Championship title history "
        "&mdash; the table the reign math actually lives in &mdash; puts the loss at <b>Fightland on "
        "October 2, 2021</b>, and only October 2 produces the 819 days both pages agree the reign "
        "lasted. This page publishes October 2 and treats the arithmetic as the citation. The reign "
        "figure itself has no conflict behind it: 819 days, the longest in MLW history, from beating "
        "Tom Lawlor at Kings of Colosseum to losing the title-versus-title match against "
        "Hammerstone.",

        "The WWE run divides at the injury. Before it: the June 21, 2024 debut attacking Cody "
        "Rhodes, a winning in-ring debut in the Money in the Bank six-man on July 6, the WWE Tag "
        "Team Championship with Tama Tonga from August 2 to October 25, 2024, and the 2025 singles "
        "breakout &mdash; the United States title from LA Knight at WrestleMania 41 on April 19, "
        "held 70 days until his own Tribal Chief, Solo Sikoa, took it at Night of Champions with the "
        "MFT's help, then the steel cage loss to Sikoa at SummerSlam. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">70</span>'
        '<span class="pull-cap">days as United States Champion in 2025, his first WWE singles title, '
        'won at WrestleMania 41</span></span>'
        "In October 2025 a non-wrestling-related injury &mdash; reported October 16, specifics kept "
        "private &mdash; shut the run down; he had last wrestled on September 12, and WWE paused "
        "what reporting described as major creative plans. He returned on the January 9, 2026 "
        "SmackDown, attacking Drew McIntyre and Cody Rhodes, beat McIntyre in an unsanctioned match "
        "at WrestleMania 42 on April 18, and challenged Roman Reigns for the World Heavyweight "
        "Championship at Backlash on May 9, losing but landing inside Reigns' rebuilt Bloodline.",

        "Which is where it gets complicated. As of August 31, 2026 he is a Bloodline member on Raw "
        "alongside Reigns and The Usos &mdash; and the cracks are on camera. He and The Usos lost "
        "the SummerSlam six-man to Solo Sikoa, LA Knight and Royce Keys on August 1. When Sikoa "
        "spiked Reigns on the August 17 Raw and the brawl broke out, Fatu <b>stayed in the corner "
        "and did not fight</b>. A week later The Usos told him to stay backstage entirely, and the "
        "match they wrestled without him ended with Royce Keys and OTM laying out everyone in it. "
        "Every party in the story is now waiting on the same question: which side of the family the "
        "Werewolf actually runs with.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Curated ledger",
        promo_order=["WWE", "MLW"],
        promo_labels={"WWE": "WWE", "MLW": "MLW"},
        stats=[
            ("819", "Day MLW World reign"),
            ("70",  "Day US reign"),
            ("84",  "Day WWE Tag reign"),
            ("1",   "ESPN Debut of the Year"),
            ("3",   "Bloodline versions"),
            ("2024","WWE debut"),
        ],
        lead=("Twelve documented bouts &mdash; the MLW reign's two endpoints and the WWE run's title "
              "changes and turning points. This is a curated ledger, not a career count; no career "
              "win&ndash;loss total is published because none is verified. The MLW title-loss date is "
              "the title history's October 2, 2021, not the biography's October 7 &mdash; only "
              "October 2 produces the 819-day reign length both pages state. Filter by match type, "
              "tap any column header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The bouts the reputation rests on. No star ratings are printed because none were "
                    "verified against Observer archives in this pass &mdash; these are selected for "
                    "what they meant, not how they were scored."),
    signature=[
        dict(rating="&mdash;", event="MLW Fightland 2021", opponent="Alexander Hammerstone",
             stip="Title vs. title — the 819-day reign ends against the National Openweight Champion"),
        dict(rating="&mdash;", event="WrestleMania 41 Night 1", opponent="LA Knight",
             stip="United States Championship — the WWE singles breakout"),
        dict(rating="&mdash;", event="SummerSlam 2025 Night 2", opponent="Solo Sikoa",
             stip="Steel cage — the blow-off of the Bloodline's best 2025 feud"),
        dict(rating="&mdash;", event="WrestleMania 42 Night 1", opponent="Drew McIntyre",
             stip="Unsanctioned match — the post-injury statement win"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("819", "Day MLW World reign"),
            ("70",  "Day US reign"),
            ("84",  "Day WWE Tag reign"),
            ("0",   "WWE world titles"),
        ],
        lead=("Four championships across two companies, anchored by the longest world title reign in "
              "MLW history. The one WWE world title match he has had &mdash; Backlash 2026 &mdash; "
              "he lost, to the head of his own faction."),
        rows=[
            dict(ic="M", name="MLW World Heavyweight Championship", count="1",
                 sub="July 6, 2019 &ndash; October 2, 2021 &middot; def. Tom Lawlor at Kings of "
                     "Colosseum, lost to Alexander Hammerstone at Fightland &middot; <b>819 days</b>, "
                     "the longest reign in the title's history &middot; the biography's October 7 "
                     "loss date does not produce 819 days; the title history's October 2 does"),
            dict(ic="U", name="WWE United States Championship", count="1",
                 sub="April 19, 2025 &ndash; June 28, 2025 &middot; def. LA Knight at WrestleMania 41 "
                     "Night 1, lost to Solo Sikoa at Night of Champions &middot; <b>70 days</b> "
                     "&middot; his first WWE singles title"),
            dict(ic="T", name="WWE Tag Team Championship", count="1",
                 sub="August 2, 2024 &ndash; October 25, 2024 &middot; won with Tama Tonga from DIY "
                     "on SmackDown, lost to the Motor City Machine Guns &middot; 84 days, six weeks "
                     "into his WWE run"),
            dict(ic="O", name="MLW National Openweight Championship", count="1",
                 sub="Won April 6, 2023 &middot; the reign's end was not verified in this pass and no "
                     "end date is invented"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Three units, one constant: he has never been booked as a man who works alone.",
        cards=[
            dict(era="MLW &middot; 2019&ndash;2021",
                 name="Contra Unit",
                 members="Jacob Fatu, Josef Samael, Simon Gotch, Ikuro Kwon, others",
                 desc="The paramilitary invasion faction that defined MLW's peak years, with Fatu as "
                      "its masked ace and champion for the entire 819-day reign. Contra burned "
                      "banners, jumped opponents and held the promotion's main title hostage for two "
                      "years — the run that made WWE's interest inevitable."),
            dict(era="WWE &middot; 2024&ndash;2025",
                 name="The Bloodline — Solo Sikoa's version",
                 members="Solo Sikoa, Jacob Fatu, Tama Tonga, Tonga Loa, JC Mateo (later)",
                 desc="Debuted June 21, 2024 on SmackDown attacking Cody Rhodes, imported by Sikoa as "
                      "the enforcer's enforcer. Won the WWE Tag Team Championship with Tama Tonga "
                      "within six weeks and fought the WarGames match that November. The alliance "
                      "cracked in 2025: he cost Sikoa the Money in the Bank ladder match on June 7, "
                      "lost the US title to him at Night of Champions on June 28 with the MFT "
                      "swarming, and lost the cage rematch at SummerSlam. He never joined the "
                      "MFT rebrand."),
            dict(era="WWE &middot; 2026&ndash;present",
                 name="The Bloodline — Roman Reigns' version",
                 members="Roman Reigns, The Usos, Jacob Fatu",
                 desc="The strangest turn of the story: after losing to Reigns at Backlash on May 9, "
                      "2026, Fatu ended up inside the rebuilt original Bloodline, opposite his old "
                      "boss Sikoa. The membership is already fraying on camera — he stood motionless "
                      "through the August 17 mutiny and was told to stay backstage on August 24."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One ring name his whole career &mdash; Jacob Fatu is his real name &mdash; and three "
             "distinct versions of the act: <b>the independent journeyman</b> (2012&ndash;2019) "
             "&rarr; <b>the Samoan Werewolf of Contra</b> (2019&ndash;2024) &rarr; <b>the "
             "Bloodline's wild card</b> (2024&ndash;present).",
        cards=[
            dict(mono="IN", era="Independents &middot; 2012&ndash;2019", name="The journeyman",
                 desc="A decade on the California circuit before the break, carrying the family name "
                      "without the family push — his father Sam Fatu wrestled as the Tonga Kid and "
                      "Tama. The agility-at-285-pounds act was already fully formed; the platform "
                      "was not."),
            dict(mono="SW", era="MLW &middot; 2019&ndash;2024", name="The Samoan Werewolf",
                 desc="Signed January 17, 2019, aligned with Contra Unit, and champion within six "
                      "months. The nickname, the mask iconography and the springboard moonsault all "
                      "date from here, along with an 819-day reign and a Battle Riot win. He left as "
                      "a free agent on February 1, 2024."),
            dict(mono="BL", era="WWE &middot; 2024&ndash;present", name="The Bloodline's wild card",
                 desc="ESPN's 2024 Debut of the Year: the laugh, the frenzied double-stomp entrances, "
                      "the sense that nobody — including his own faction — controls him. Two "
                      "Bloodlines and one injury later, that unpredictability is now the actual "
                      "story: three weeks of TV have been built on not knowing whose side he is on."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Sacramento to the centre of the Bloodline, the long way around.",
        rows=[
            dict(year="2012", title="Debuts on the independents",
                 desc="First match September 22, 2012 in California, trained by Rikishi, Black "
                      "Pearl, Gangrel and Sinn Bodhi — a second-generation Anoa'i, son of Sam Fatu, "
                      "the Tonga Kid."),
            dict(year="2019", title="Signs with MLW; wins the world title",
                 desc="Signs January 17; joins Contra Unit; beats Tom Lawlor for the MLW World "
                      "Heavyweight Championship at Kings of Colosseum on July 6."),
            dict(year="2021", title="The 819-day reign ends",
                 desc="Alexander Hammerstone beats him in the title-versus-title match at Fightland "
                      "on October 2 — still the longest reign in MLW history."),
            dict(year="2023", title="Openweight champion",
                 desc="Wins the MLW National Openweight Championship on April 6, his last major "
                      "title outside WWE."),
            dict(year="2024", title="WWE debut, tag gold, Debut of the Year",
                 desc="Leaves MLW February 1; debuts on the June 21 SmackDown attacking Cody Rhodes; "
                      "wins the WWE Tag Team Championship with Tama Tonga on August 2; drops it to "
                      "the Motor City Machine Guns October 25; loses WarGames November 30. ESPN "
                      "names him Debut of the Year."),
            dict(year="2025", title="US Champion, the Sikoa feud, the injury",
                 desc="Beats LA Knight at WrestleMania 41 on April 19 for the United States "
                      "Championship; loses it to Solo Sikoa at Night of Champions on June 28 and the "
                      "cage rematch at SummerSlam on August 3. Last match September 12; a private, "
                      "non-wrestling-related injury is reported October 16 and ends his year."),
            dict(year="2026", title="Return, WrestleMania, and Roman's Bloodline",
                 desc="Returns January 9 attacking McIntyre and Rhodes; beats McIntyre unsanctioned "
                      "at WrestleMania 42 on April 18; loses to Roman Reigns at Backlash on May 9 "
                      "and joins his Bloodline; by late August the loyalty question is the story."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Solo Sikoa", slug="solo-sikoa",
                 desc="The cousin who imported him, then took his title. Fatu cost Sikoa the Money in "
                      "the Bank ladder match on June 7, 2025; Sikoa beat him for the United States "
                      "Championship at Night of Champions on June 28 with the MFT interfering, and "
                      "kept it in the SummerSlam steel cage. In 2026 they stand on opposite sides of "
                      "the family war — from reversed corners, with Fatu now in Roman Reigns' "
                      "Bloodline and Sikoa outside it."),
            dict(name="Alexander Hammerstone",
                 desc="The MLW rivalry — world champion against National Openweight champion, "
                      "settled title-versus-title at Fightland on October 2, 2021. Hammerstone's win "
                      "ended the 819-day reign and remains the only defining loss of the MLW run."),
            dict(name="LA Knight",
                 desc="The WrestleMania 41 opponent for the US title on April 19, 2025 - Fatu's "
                      "singles arrival in WWE. The rivalry inverted within a year: by SummerSlam "
                      "2026 Knight stood with Solo Sikoa across the ring from Fatu and The Usos, "
                      "and won."),
            dict(name="Drew McIntyre",
                 desc="The post-injury feud. Fatu returned on the January 9, 2026 SmackDown by "
                      "putting McIntyre through the announce desk, and the unsanctioned match at "
                      "WrestleMania 42 on April 18 — won clean of any stipulation protections — was "
                      "framed by Forbes and POST Wrestling as revenge for the attack that had "
                      "written him off television."),
            dict(name="Cody Rhodes",
                 desc="His first WWE target — the June 21, 2024 debut attack — and a recurring one: "
                      "the Money in the Bank six-man three weeks later, Bad Blood alongside Sikoa "
                      "that October, and the January 2026 return attack. They have never had a "
                      "one-on-one match; the record is entirely multi-man and angle."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Thin by design — the verified list is short, and nothing is added to pad it.",
        rows=[
            dict(when="2025&ndash;", title="WWE 2K", kind="Game",
                 desc="Playable in the current WWE 2K entries; his first appearance in the series "
                      "was not verified in this pass and is not claimed."),
            dict(when="2019&ndash;2024", title="MLW Fusion", kind="Television",
                 desc="The Contra Unit years ran through MLW's flagship show — the masked, "
                      "flag-burning invasion act that made the 819-day reign a weekly television "
                      "story."),
            dict(when="2026", title="August 2026 interview circuit", kind="Interviews",
                 desc="An August 2026 interview covered the development of the high-flying style and "
                      "his family's relocation to Orlando (Pro Wrestling News Source). No film, "
                      "scripted television role, autobiography or documentary centred on him could "
                      "be verified, so none is listed."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated the way the sources state them &mdash; including the one date the "
             "sources get wrong.",
        stats=[
            ("819", "Days as MLW World Champion"),
            ("70",  "Days as US Champion"),
            ("1",   "Debut of the Year"),
        ],
        rows=[
            dict(name="819 consecutive days as MLW World Heavyweight Champion",
                 sub="July 6, 2019 to October 2, 2021 — the longest reign in the title's history, "
                     "per the championship's own Wikipedia title table. The biography article's "
                     "October 7 loss date is arithmetically incompatible with 819 days and is not "
                     "published here."),
            dict(name="First WWE singles title inside a year of arriving",
                 sub="Debuted June 21, 2024; United States Champion by April 19, 2025, beating LA "
                     "Knight at WrestleMania 41 Night 1. The 70-day reign ended against Solo Sikoa "
                     "at Night of Champions."),
            dict(name="WWE Tag Team Champion six weeks into the run",
                 sub="August 2, 2024 with Tama Tonga, from DIY on SmackDown — subbing into a "
                     "division he had barely appeared in. Lost to the Motor City Machine Guns on "
                     "October 25 amid the Bloodline's civil-war distractions."),
            dict(name="ESPN Debut of the Year, 2024",
                 sub="Per Wikipedia. The frenzied debut summer — the Rhodes attack, the Money in the "
                     "Bank six-man, the tag title — is the body of evidence."),
            dict(name="Battle Riot winner",
                 sub="Won MLW's 40-man Battle Riot IV per Wikipedia, which dates it November 3, 2022 "
                     "— a date this pass could not corroborate against MLW's records, so the win is "
                     "listed and the date is not endorsed."),
            dict(name="MLW National Openweight Champion",
                 sub="Won April 6, 2023, his final title outside WWE. Reign end not verified."),
            dict(name="PWI 500: No. 20, twice, five years apart",
                 sub="Ranked 20th in 2020 (the MLW reign) and 20th again in 2025 (the US title run), "
                     "per Wikipedia — the same ceiling in two different companies."),
            dict(name="Member of three major factions without ever leading one",
                 sub="Contra Unit, Solo Sikoa's Bloodline, Roman Reigns' Bloodline. The 2026 story "
                     "is explicitly about whether that streak ends."),
        ],
        footnote=("Deliberately absent: any diagnosis of the late-2025 injury, which was reported "
                  "October 16, 2025 as non-wrestling-related with specifics kept private and has "
                  "never been disclosed; a career win-loss total, which no source verifies; and "
                  "social media handles, which were not verified in this pass."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Jacob_Fatu"),
        dict(k="Wikipedia", v="MLW World Heavyweight Championship title history",
             href="https://en.wikipedia.org/wiki/MLW_World_Heavyweight_Championship"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/jacob-fatu"),
        dict(k="411Mania", v="October 2025 injury report",
             href="https://411mania.com/wrestling/jacob-fatu-reportedly-injured-out-2026/"),
        dict(k="WrestleZone", v="SummerSlam 2026 Night 1 — the Bloodline six-man",
             href="https://www.wrestlezone.com/news/1655239-wwe-summerslam-night-1-results-review-grades-card-august-1"),
        dict(k="CBS Sports", v="August 24, 2026 Raw — benched by The Usos; OTM attack",
             href="https://www.cbssports.com/wwe/news/wwe-raw-live-updates-results-review-grades-august-24-oba-femi-bron-breakker/live/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="How long was Jacob Fatu MLW World Heavyweight Champion?",
            a="<b>819 days</b> &mdash; July 6, 2019 to October 2, 2021, the longest reign in the "
              "title's history. He won it from Tom Lawlor at Kings of Colosseum and lost it to "
              "Alexander Hammerstone in a title-versus-title match at Fightland in Philadelphia. One "
              "caution: Wikipedia's biography article dates the loss October 7, 2021, but the "
              "championship's own title history says October 2 &mdash; and only October 2 produces "
              "the 819 days both pages agree on.",
            q_ld="How long was Jacob Fatu MLW World Heavyweight Champion?",
            a_ld="Jacob Fatu held the MLW World Heavyweight Championship for 819 days, from July 6, "
                 "2019 to October 2, 2021, the longest reign in the title's history. He won it from "
                 "Tom Lawlor at MLW Kings of Colosseum and lost it to Alexander Hammerstone in a "
                 "title-versus-title match at MLW Fightland in Philadelphia. Wikipedia's biography "
                 "article gives an October 7, 2021 loss date, but the championship's title history "
                 "records October 2, 2021, which is the only date consistent with the stated 819-day "
                 "reign length."),
        dict(
            q="Is Jacob Fatu related to Solo Sikoa and The Usos?",
            a="Yes. He is the son of Sam Fatu, who wrestled as the Tonga Kid and Tama, which makes "
              "him a member of the Anoa'i wrestling dynasty and a cousin of Solo Sikoa, The Usos and "
              "Roman Reigns. Jacob Fatu is his real name, not a gimmick. The family split on WWE "
              "television is storyline; the family is not.",
            q_ld="Is Jacob Fatu related to Solo Sikoa and The Usos?",
            a_ld="Yes. Jacob Fatu is the son of Sam Fatu, who wrestled as the Tonga Kid and Tama, and "
                 "is a member of the Anoa'i wrestling dynasty. That makes him a cousin of Solo Sikoa, "
                 "The Usos and Roman Reigns. Jacob Fatu is his real name."),
        dict(
            q="What happened to Jacob Fatu in late 2025?",
            a="An injury with no public diagnosis. He last wrestled on September 12, 2025, appeared "
              "in a September 26 segment with Drew McIntyre, and on October 16 it was reported "
              "(BodySlam+, via 411Mania) that a <b>non-wrestling-related injury</b> &mdash; "
              "specifics kept private &mdash; would sideline him well into 2026, pausing what were "
              "described as major creative plans. He was written out around an October 17 backstage "
              "attack angle and returned on the January 9, 2026 SmackDown, attacking McIntyre and "
              "Cody Rhodes.",
            q_ld="Why was Jacob Fatu off WWE television in late 2025?",
            a_ld="Jacob Fatu suffered a non-wrestling-related injury whose specifics were kept "
                 "private. He last wrestled on September 12, 2025, and the injury was reported on "
                 "October 16, 2025, with an expected absence running well into 2026. He was written "
                 "off television with a backstage attack angle in mid-October 2025 and returned on "
                 "the January 9, 2026 episode of SmackDown, attacking Drew McIntyre and Cody "
                 "Rhodes."),
        dict(
            q="Is Jacob Fatu in the Bloodline now, and whose side is he on?",
            a="He is a member of <b>Roman Reigns' rebuilt Bloodline</b> on Raw as of August 31, 2026 "
              "&mdash; he joined after losing to Reigns at Backlash on May 9 &mdash; but the "
              "membership is visibly cracking. He and The Usos lost the SummerSlam six-man to Solo "
              "Sikoa, LA Knight and Royce Keys on August 1; when Sikoa spiked Reigns on the August "
              "17 Raw, Fatu stood in the corner and stayed out of it; and on August 24 The Usos told "
              "him to remain backstage. WWE is playing his next move as an open question, and this "
              "page does not guess at it.",
            q_ld="Is Jacob Fatu in the Bloodline now?",
            a_ld="As of August 31, 2026, Jacob Fatu is a member of Roman Reigns' Bloodline on WWE "
                 "Raw, having joined after unsuccessfully challenging Reigns for the World "
                 "Heavyweight Championship at Backlash on May 9, 2026. His loyalty is in question on "
                 "television: he stayed neutral when Solo Sikoa attacked Reigns on the August 17, "
                 "2026 Raw, and The Usos asked him to stay backstage on the August 24 episode."),
        dict(
            q="Has Jacob Fatu ever held a WWE world championship?",
            a="No. His one WWE world title match to date was at Backlash on May 9, 2026, a loss to "
              "World Heavyweight Champion Roman Reigns. His WWE titles are the United States "
              "Championship (70 days in 2025) and the WWE Tag Team Championship with Tama Tonga (84 "
              "days in 2024). His world championship &mdash; the 819-day reign &mdash; was in MLW.",
            q_ld="Has Jacob Fatu ever held a WWE world championship?",
            a_ld="No. Jacob Fatu's only WWE world championship match so far was a loss to World "
                 "Heavyweight Champion Roman Reigns at Backlash on May 9, 2026. In WWE he has held "
                 "the United States Championship for 70 days in 2025 and the WWE Tag Team "
                 "Championship with Tama Tonga for 84 days in 2024. His world title reign, 819 days, "
                 "was with the MLW World Heavyweight Championship."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Jacob Fatu", sub="not a ring name"),
        dict(label="Born", value="April 18, 1992", sub="Sacramento, California &middot; age 34"),
        dict(label="Family", value="Son of Sam Fatu (the Tonga Kid)",
             sub="Anoa'i dynasty &middot; cousin of Solo Sikoa, The Usos and Roman Reigns"),
        dict(label="Height", value="6&#8242;2&#8243;", sub="188 cm"),
        dict(label="Weight", value="285 lb", sub="129 kg (billed)"),
        dict(label="Debut", value="September 22, 2012", sub="California independents"),
        dict(label="Trained by", value="Rikishi",
             sub="with Black Pearl, Gangrel and Sinn Bodhi (Wikipedia infobox)"),
        dict(label="Signature", value="Springboard moonsault &middot; Samoan drop &middot; "
                                      "running hip attack",
             sub="the moonsault at 285 pounds is the calling card"),
        dict(label="MLW tenure", value="January 17, 2019 &ndash; February 1, 2024",
             sub="signed, crowned, and left as a free agent"),
        dict(label="WWE debut", value="June 21, 2024", sub="SmackDown, attacking Cody Rhodes"),
        dict(label="Brand", value="Raw", sub="with Roman Reigns' Bloodline, per the August 2026 booking"),
        dict(label="Also known as", value="The Samoan Werewolf"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1992-04-18",
    bornplace="Sacramento, California",
    nationality="United States",
    height_cm=188,
    weight_kg=129,
    ld=dict(
        alternateName=["The Samoan Werewolf"],
        award=["MLW World Heavyweight Championship (1 reign, a record 819 days)",
               "WWE United States Championship (1 reign, 70 days)",
               "WWE Tag Team Championship (1 reign, with Tama Tonga)",
               "MLW National Openweight Championship (1 reign)",
               "MLW Battle Riot winner",
               "ESPN Debut of the Year (2024)",
               "PWI 500 No. 20 (2020, 2025)"],
        knowsAbout=["Professional wrestling", "MLW", "Contra Unit", "The Bloodline", "WWE",
                    "Anoa'i family", "Championship wrestling"],
        description="Jacob Fatu is an American professional wrestler signed to WWE and a member of "
                    "the Anoa'i wrestling dynasty, the son of Sam Fatu. Known as the Samoan "
                    "Werewolf, he held the MLW World Heavyweight Championship for a record 819 days "
                    "between July 6, 2019 and October 2, 2021, and after debuting in WWE in June "
                    "2024 won the WWE Tag Team Championship with Tama Tonga and the WWE United "
                    "States Championship at WrestleMania 41. As of August 2026 he is part of Roman "
                    "Reigns' Bloodline on Raw.",
        sameAs=["https://en.wikipedia.org/wiki/Jacob_Fatu",
                "https://www.wwe.com/superstars/jacob-fatu"],
    ),
)
