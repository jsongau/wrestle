# -*- coding: utf-8 -*-
"""Solo Sikoa - dossier data.

Sources: web research compiled August 31, 2026 - Wikipedia's Solo Sikoa article plus
Wrestling Inc., WrestleZone, Khel Now and CBS Sports coverage of the June-August 2026
Bloodline storyline. Every match row carries a day-precision date stated in one of the
opened sources.

Deliberate omissions:
  * No career win-loss total - no verified figure exists and none is invented.
  * A "Crown Jewel 2024" claim that Sikoa pinned Roman Reigns surfaced in one summary and
    could not be corroborated anywhere else; it is not published here.
  * No social handles - official accounts were not verified in this pass.
  * The exact length of Sikoa's personal WWE Tag Team Championship reign is disputed in
    the sources (see the correction paragraph); the endpoints are published, the day
    count is flagged.
"""

# ----------------------------------------------------------------- record rows
# A curated ledger, not a career count. Every date below is stated explicitly in the
# research sources; nothing is estimated. The August 24, 2026 main event is carried as a
# no-contest because that is how it ended - OTM's attack threw the match out.
ROWS = [
    dict(result="W", date="2022-09-13", promo="WWE", landmark=True,
         event="NXT 2.0", opponent="Carmelo Hayes",
         stip="Singles — first WWE title", title="NXT North American Championship"),
    dict(result="W", date="2022-11-26", promo="WWE", type="tag",
         event="Survivor Series: WarGames", opponent="The Brawling Brutes, Drew McIntyre & Kevin Owens",
         stip="WarGames — with Roman Reigns, The Usos & Sami Zayn", title=""),
    dict(result="W", date="2023-11-04", promo="WWE", landmark=True,
         event="Crown Jewel — Riyadh", opponent="John Cena",
         stip="Singles — Cena's only match of 2023", title=""),
    dict(result="L", date="2024-08-03", promo="WWE", landmark=True,
         event="SummerSlam — Cleveland", opponent="Cody Rhodes",
         stip="Bloodline Rules — challenge", title="Undisputed WWE Championship"),
    dict(result="L", date="2024-10-05", promo="WWE", type="tag",
         event="Bad Blood", opponent="Roman Reigns & Cody Rhodes",
         stip="Tag — with Jacob Fatu", title=""),
    dict(result="L", date="2024-11-30", promo="WWE", type="tag",
         event="Survivor Series: WarGames", opponent="The OG Bloodline & CM Punk",
         stip="WarGames — his Bloodline loses to Reigns' loyalists", title=""),
    dict(result="L", date="2025-01-06", promo="WWE", landmark=True,
         event="Raw — Netflix premiere", opponent="Roman Reigns",
         stip="Tribal Combat — the Ula Fala on the line", title=""),
    dict(result="L", date="2025-06-07", promo="WWE", type="tag",
         event="Money in the Bank", opponent="The six-man ladder field",
         stip="Ladder match — Jacob Fatu costs him the briefcase", title=""),
    dict(result="W", date="2025-06-28", promo="WWE", landmark=True,
         event="Night of Champions — Riyadh", opponent="Jacob Fatu",
         stip="Singles — first United States title", title="WWE United States Championship"),
    dict(result="W", date="2025-08-03", promo="WWE", landmark=True,
         event="SummerSlam Night 2", opponent="Jacob Fatu",
         stip="Steel cage — retains", title="WWE United States Championship"),
    dict(result="L", date="2025-08-29", promo="WWE", landmark=True,
         event="SmackDown", opponent="Sami Zayn",
         stip="Open challenge — the 62-day reign ends", title="WWE United States Championship"),
    dict(result="W", date="2026-01-09", promo="WWE", type="tag", landmark=True,
         event="SmackDown", opponent="The Wyatt Sicks",
         stip="Tag — with Tama Tonga", title="WWE Tag Team Championship"),
    dict(result="W", date="2026-04-17", promo="WWE", type="tag",
         event="SmackDown — WrestleMania 42 go-home", opponent="The Wyatt Sicks",
         stip="Eight-man street fight — the MFT's last stand together", title=""),
    dict(result="W", date="2026-08-01", promo="WWE", type="tag", landmark=True,
         event="SummerSlam Night 1 — Minneapolis", opponent="Jey Uso, Jimmy Uso & Jacob Fatu",
         stip="Six-man — with LA Knight & Royce Keys; Knight pins Jey", title=""),
    dict(result="NC", date="2026-08-24", promo="WWE", type="tag",
         event="Raw — Ottawa", opponent="The Usos",
         stip="Tag — with LA Knight; thrown out when Royce Keys and OTM attack everyone", title=""),
]

DATA = dict(
    slug="solo-sikoa",
    name="Solo Sikoa",
    realname="Joseph Yokozuna Fatu",
    epithet="The Street Champion",
    hook="Record & Titles",

    meta_desc=("Solo Sikoa, the Street Champion, held the WWE United States Championship for 62 days, "
               "led his own Bloodline and the MFT, and spiked Roman Reigns on the August 17, 2026 Raw. "
               "Full record, titles, factions, records and career."),
    og_desc=("The Street Champion: enforcer of the Bloodline, then its usurper, then the MFT's boss, "
             "and since August 17, 2026 the man who drove a Samoan Spike into Roman Reigns' throat "
             "and walked out with LA Knight."),
    tw_desc="The Street Champion: US Champion for 62 days, two Bloodlines led, one Tribal Chief spiked.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2018",
    height_imp="6&#8242;2&#8243;",
    weight_lb="250",
    world_titles="0",
    vitals_tagline="My family tree",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="SS", title="WWE Shop", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable in the current 2K entries",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="W", title="Wikipedia", sub="Full biography", tag="Read",
             href="https://en.wikipedia.org/wiki/Solo_Sikoa"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/solo-sikoa"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Enforcer &middot; the self-styled Tribal Chief &middot; the MFT's boss",
    hero_tag="Anoa'i family &middot; <em>Independents &middot; NXT &middot; WWE &middot; 2018&ndash;present</em>",
    now_label="NOW",
    now_bold="Raw, allied with LA Knight",
    now_tail=" &middot; spiked Roman Reigns on the August 17 Raw, rejected the Bloodline, and was jumped "
             "by Royce Keys and OTM a week later &mdash; a war on two fronts",
    hstats=[
        dict(value="62", x=False, label="Day US Reign"),
        dict(value="3",  x=False, label="WWE Titles Held"),
        dict(value="2",  x=True,  label="Bloodlines Led"),
        dict(value="5",  x=False, label="MFT Members at Peak"),
    ],
    ghost_link="From Sefa Fatu to the man who spiked the Tribal Chief",
    vlabel="Est. 2018 &middot; Anoa'i family",
    mono="SS",

    # ---------------------------------------------------------------- 01 overview
    # index into overview of the correction paragraph -> the framed
    # "Setting one thing straight" callout (aside.corr) on the page
    correction=2,
    overview=[
        "<b>Solo Sikoa</b> is the youngest son of Rikishi, the younger brother of The Usos, and the "
        "member of the Anoa'i wrestling dynasty whose entire WWE career has been an argument about who "
        "the family answers to. He arrived at Clash at the Castle on September 3, 2022 as Roman "
        "Reigns' enforcer, took over the Bloodline in Reigns' absence in 2024, rebuilt it twice in his "
        "own image, and on August 17, 2026 ended the argument by driving a Samoan Spike into Reigns' "
        "throat on Raw rather than kneel to him. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">62</span>'
        '<span class="pull-cap">days as United States Champion in 2025 &mdash; per Wikipedia, the third '
        'member of the Anoa&rsquo;i family to hold the title</span></span>'
        "The championship resume is short for a wrestler this central &mdash; one United States "
        "Championship, one WWE Tag Team Championship, one NXT North American Championship &mdash; "
        "because the resume was never the point: for four years he has been the axis the Bloodline "
        "story turned on.",

        "The rise was fast. He debuted on the independents in April 2018 as Sefa Fatu, signed with WWE "
        "on August 30, 2021, and won the NXT North American Championship from Carmelo Hayes on "
        "September 13, 2022 &mdash; ten days after his main-roster debut had already happened, when he "
        "helped Reigns beat Drew McIntyre in Cardiff. He vacated the NXT title on September 20 and "
        "spent two years as the silent enforcer, spiking John Cena at Crown Jewel 2023 in Cena's only "
        "match of that year. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">2</span>'
        '<span class="pull-cap">Bloodlines led &mdash; the usurper version of 2024&ndash;25, and the MFT, '
        'his &ldquo;My Family Tree&rdquo; rebrand of 2025&ndash;26</span></span>'
        "After WrestleMania XL he expelled Jimmy Uso, claimed the Tribal Chief title for himself and "
        "recruited Tama Tonga, Tonga Loa and Jacob Fatu; the civil war that followed ran through "
        "SummerSlam 2024, WarGames, and the Tribal Combat match Reigns won on the January 6, 2025 "
        "Netflix premiere of Raw. He beat Jacob Fatu for the United States Championship at Night of "
        "Champions on June 28, 2025, kept it past a steel cage rematch at SummerSlam, and lost it to "
        "Sami Zayn's open challenge on August 29, 2025 after 62 days.",

        "One set of numbers on this page is published with a flag on it. Wikipedia records Sikoa and "
        "Tama Tonga winning the WWE Tag Team Championship from the Wyatt Sicks on January 9, 2026 and "
        "gives Sikoa's reign as <b>56 days</b> &mdash; but it also says the titles were lost to Damian "
        "Priest and R-Truth on March 20, 2026, and January 9 to March 20 is 70 days, not 56. Wrestling "
        "Inc.'s report of the March 20 SmackDown adds a further wrinkle: the men who actually dropped "
        "the belts that night were <b>Tama Tonga and JC Mateo</b>, not Sikoa. The most likely reading "
        "is that Sikoa's personal share of the reign ended before the titles changed hands, but no "
        "opened source states it outright, so this page publishes the verified endpoints &mdash; won "
        "January 9, lost March 20 &mdash; and declines to pick a day count.",

        "The 2026 story is the turn. The MFT dissolved on the June 26 SmackDown in London when Tama "
        "Tonga and Talla Tonga told him they had &ldquo;heard from the elders&rdquo; and walked, "
        "blaming his obsession with Reigns for the June 19 tag title loss. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">8.17</span>'
        '<span class="pull-cap">the date, month and day, that Sikoa answered Reigns&rsquo; demand to kneel '
        'with a Samoan Spike on Raw</span></span>'
        "Sikoa spent July courting a sceptical LA Knight, ate a beatdown from Reigns' rebuilt "
        "Bloodline on the July 20 Raw, and got his answer in at SummerSlam on August 1, when he, "
        "Knight and Royce Keys beat The Usos and Jacob Fatu. On August 17 Reigns demanded he fall in "
        "line and attack Knight to prove it; Sikoa spiked Reigns instead. A week later Royce Keys "
        "turned too, returning with OTM to lay out Sikoa, Knight and The Usos alike &mdash; so as of "
        "August 31, 2026 he is a babyface for the first time in his WWE career, fighting his own "
        "family on one side and a debuting faction on the other.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Curated ledger",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("62",   "Day US reign"),
            ("3",    "WWE titles held"),
            ("2",    "WarGames matches"),
            ("10+",  "Samoan Spikes on Cena"),
            ("2",    "Bloodlines led"),
            ("1",    "Tribal Chief spiked"),
        ],
        lead=("Fifteen documented bouts &mdash; the title changes, the Bloodline civil-war matches and "
              "the 2026 turn. This is a curated ledger, not a career count, and no career win&ndash;loss "
              "total is published because no verified total exists. The August 24, 2026 main event is "
              "recorded as a no-contest because that is how it ended: Royce Keys and OTM attacked "
              "everyone in it. Filter by match type, tap any column header to sort, and turn spoilers "
              "on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The bouts the reputation rests on. No star ratings are printed here because none "
                    "were verified against Observer archives in this pass &mdash; these are selected for "
                    "what they meant, not how they were scored."),
    signature=[
        dict(rating="&mdash;", event="SummerSlam 2024 — Cleveland", opponent="Cody Rhodes",
             stip="Bloodline Rules — the usurper's shot at the Undisputed WWE Championship"),
        dict(rating="&mdash;", event="Raw — Netflix premiere, January 6, 2025", opponent="Roman Reigns",
             stip="Tribal Combat — the Ula Fala settles who leads the family"),
        dict(rating="&mdash;", event="Night of Champions 2025 — Riyadh", opponent="Jacob Fatu",
             stip="United States Championship — beats his own enforcer for his first main-roster title"),
        dict(rating="&mdash;", event="SummerSlam 2025 Night 2", opponent="Jacob Fatu",
             stip="Steel cage — the feud blow-off, retaining the US title"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("62",  "Day US reign"),
            ("1",   "WWE Tag Team reign"),
            ("7",   "Days as NXT NA Champion"),
            ("0",   "World titles"),
        ],
        lead=("Three WWE championships and two independent ones &mdash; a short list for a wrestler "
              "who has main-evented premium live events, because his stories have been about the "
              "family, not the gold. The tag reign's day count is disputed in the sources and is "
              "flagged rather than resolved."),
        rows=[
            dict(ic="U", name="WWE United States Championship", count="1",
                 sub="June 28, 2025 &ndash; August 29, 2025 &middot; def. Jacob Fatu at Night of "
                     "Champions, lost to Sami Zayn's SmackDown open challenge &middot; <b>62 days</b> "
                     "&middot; per Wikipedia, the third Anoa'i family member to hold the title"),
            dict(ic="T", name="WWE Tag Team Championship", count="1",
                 sub="January 9, 2026 &ndash; March 20, 2026 (team endpoints) &middot; won with Tama "
                     "Tonga from the Wyatt Sicks on SmackDown &middot; the belts were lost by Tama "
                     "Tonga and JC Mateo; Wikipedia logs Sikoa's own share as 56 days, which does not "
                     "match the endpoints &mdash; flagged, not resolved"),
            dict(ic="N", name="NXT North American Championship", count="1",
                 sub="September 13, 2022 &ndash; September 20, 2022 &middot; def. Carmelo Hayes, "
                     "defended against Madcap Moss on SmackDown three nights later, then vacated when "
                     "the main-roster move stuck &middot; seven days"),
            dict(ic="F", name="FSW Nevada State Championship", count="1",
                 sub="January 25, 2019 &ndash; June 2019 &middot; 149 days per Wikipedia &middot; "
                     "Future Stars of Wrestling, Las Vegas, as Sefa Fatu"),
            dict(ic="A", name="AWF Heavyweight Championship", count="1",
                 sub="August 2019 &ndash; January 2021 &middot; 418 days per Wikipedia &middot; "
                     "Arizona Wrestling Federation"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Four alignments in four years, every one of them a claim about who runs the family.",
        cards=[
            dict(era="WWE &middot; 2022&ndash;2024",
                 name="The Bloodline — the enforcer",
                 members="Roman Reigns, The Usos, Solo Sikoa, Paul Heyman",
                 desc="Debuted at Clash at the Castle on September 3, 2022, interfering to save Roman "
                      "Reigns' Undisputed WWE Universal Championship against Drew McIntyre. For two "
                      "years he was the group's silent weapon — the WarGames win in November 2022, the "
                      "attack that set up WrestleMania 39's main event, the Samoan Spikes that ended "
                      "John Cena's night at Crown Jewel 2023. ESPN named the Bloodline story Best "
                      "Storyline in 2022 and 2023 with his enforcer run at its core."),
            dict(era="WWE &middot; 2024&ndash;2025",
                 name="The Bloodline — the usurper's version",
                 members="Solo Sikoa, Tama Tonga, Tonga Loa, Jacob Fatu, JC Mateo (later)",
                 desc="After WrestleMania XL, with Reigns gone, Sikoa expelled Jimmy Uso, removed Paul "
                      "Heyman's authority and claimed the Tribal Chief title, importing Tama Tonga, "
                      "Tonga Loa and Jacob Fatu. The civil war it started ran more than a year: "
                      "Bloodline Rules at SummerSlam 2024, the tag loss at Bad Blood, the WarGames "
                      "defeat at Survivor Series, and the Tribal Combat loss to Reigns on the January "
                      "6, 2025 Raw that settled the leadership question — against him."),
            dict(era="WWE &middot; 2025&ndash;2026",
                 name="MFT — My Family Tree",
                 members="Solo Sikoa, Tama Tonga, Tonga Loa, JC Mateo, Talla Tonga",
                 desc="The rebrand after the US title win: same idea, his tree instead of Reigns'. The "
                      "MFT feuded with Sami Zayn and the Wyatt Sicks, and Sikoa and Tama Tonga took "
                      "the WWE Tag Team Championship from the Sicks on January 9, 2026. It bled out in "
                      "stages: JC Mateo and Tonga Loa were released in April 2026, and on the June 26 "
                      "SmackDown in London, Tama and Talla Tonga told Sikoa they had heard from the "
                      "elders and were out — blaming his Reigns obsession for the June 19 tag title "
                      "loss. The Tongas went on to win the tag titles without him on August 14."),
            dict(era="WWE &middot; 2026&ndash;present",
                 name="With LA Knight",
                 members="Solo Sikoa, LA Knight (Royce Keys, until he turned)",
                 desc="Not a stable — an alliance of convenience that became the first babyface run of "
                      "his career. Knight refused to trust him at first, fearing he would crawl back "
                      "to the Bloodline; the SummerSlam six-man win on August 1 and the Samoan Spike "
                      "he gave Reigns on August 17 answered that. Royce Keys, the third man at "
                      "SummerSlam, turned on both of them a week later, returning with OTM on the "
                      "August 24 Raw."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One ring name in WWE and four distinct jobs inside it: <b>Sefa Fatu</b> "
             "(2018&ndash;2021) &rarr; <b>Solo Sikoa, the enforcer</b> (2021&ndash;2024) &rarr; "
             "<b>the self-styled Tribal Chief</b> (2024&ndash;2025) &rarr; <b>the MFT's boss</b> "
             "(2025&ndash;2026) &rarr; <b>the man who spiked Roman Reigns</b> (2026&ndash;).",
        cards=[
            dict(mono="SF", era="Independents &middot; 2018&ndash;2021", name="Sefa Fatu",
                 desc="The debut name, April 29, 2018, trained by his father Rikishi with Kenny King "
                      "and Sinn Bodhi. A football player first — American River College, then "
                      "Dickinson State — he came to wrestling late by family standards and won Nevada "
                      "and Arizona independent titles before WWE signed him on August 30, 2021."),
            dict(mono="EN", era="WWE &middot; 2021&ndash;2024", name="The Enforcer",
                 desc="Renamed Solo Sikoa in NXT, called up to stand at Roman Reigns' shoulder eleven "
                      "months later. The character barely spoke; the Samoan Spike did. His NXT North "
                      "American Championship lasted seven days because the Cardiff run-in worked too "
                      "well to reverse."),
            dict(mono="TC", era="WWE &middot; 2024&ndash;2025", name="The self-styled Tribal Chief",
                 desc="The heel turn on his own family: expelling Jimmy Uso, wearing his own Ula Fala, "
                      "demanding the acknowledgement Reigns had spent four years collecting. Reigns "
                      "took the claim apart in Tribal Combat on January 6, 2025."),
            dict(mono="MFT", era="WWE &middot; 2025&ndash;2026", name="The MFT's boss",
                 desc="“My Family Tree” — the same authoritarian idea rebuilt around the "
                      "Tonga side of the dynasty, with a United States Championship to legitimise it. "
                      "It ended with every member gone: two released, two walked, one of them now a "
                      "tag team champion without him."),
            dict(mono="SS", era="WWE &middot; 2026&ndash;present", name="The Street Champion, unaligned",
                 desc="The first face run of his career, built on refusing to kneel. WWE reporting "
                      "since August 17 frames him as a standalone threat rather than a member of "
                      "anyone's faction — including LA Knight's."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="From a Sacramento football field to the centre of the Bloodline story.",
        rows=[
            dict(year="2018", title="Debut as Sefa Fatu",
                 desc="First match April 29, 2018 on the independents, trained by Rikishi, Kenny King "
                      "and Sinn Bodhi after a college football career."),
            dict(year="2021", title="Signs with WWE",
                 desc="Signed August 30, 2021; debuts in NXT at Halloween Havoc on October 26, "
                      "attacking Grayson Waller, and wrestles his first NXT match on November 2."),
            dict(year="2022", title="NXT champion, then Cardiff",
                 desc="Main-roster debut first — the Clash at the Castle run-in on September 3 — then "
                      "the NXT North American Championship from Carmelo Hayes on September 13, vacated "
                      "seven days later. Wins WarGames with the Bloodline in November."),
            dict(year="2023", title="The enforcer year",
                 desc="Central to the WrestleMania 39 programme against Cody Rhodes; beats John Cena "
                      "at Crown Jewel on November 4 in Cena's only match of the year."),
            dict(year="2024", title="Takes the Bloodline",
                 desc="With Reigns gone after WrestleMania XL, expels Jimmy Uso, claims the Tribal "
                      "Chief mantle and recruits Tama Tonga, Tonga Loa and Jacob Fatu. Loses "
                      "Bloodline Rules to Cody Rhodes at SummerSlam and WarGames in November."),
            dict(year="2025", title="Tribal Combat, the US title, and the MFT",
                 desc="Loses Tribal Combat to Reigns on the January 6 Netflix Raw; beats Jacob Fatu "
                      "for the United States Championship at Night of Champions on June 28; retains in "
                      "the SummerSlam cage; loses it to Sami Zayn on August 29 and rebrands the group "
                      "as the MFT."),
            dict(year="2026", title="Tag gold, the collapse, and the turn",
                 desc="Wins the WWE Tag Team Championship with Tama Tonga on January 9; the MFT "
                      "dissolves on June 26; he allies with LA Knight, wins the SummerSlam six-man on "
                      "August 1, spikes Roman Reigns on August 17, and is ambushed by Royce Keys and "
                      "OTM on August 24."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Almost all of them are family.",
        cards=[
            dict(name="Roman Reigns",
                 desc="The relationship the whole career orbits. Enforcer from September 2022, usurper "
                      "from April 2024, defeated challenger in Tribal Combat on January 6, 2025 — and "
                      "on August 17, 2026, when Reigns demanded he kneel and prove loyalty by "
                      "attacking LA Knight, Sikoa answered with a Samoan Spike. It is the first time "
                      "the story has cast Sikoa as the sympathetic side of the feud."),
            dict(name="Jacob Fatu", slug="jacob-fatu",
                 desc="His own imported enforcer, and the best matches of his career. Fatu cost him "
                      "the Money in the Bank ladder match on June 7, 2025; Sikoa took the United "
                      "States title from him at Night of Champions on June 28 and kept it in the "
                      "SummerSlam steel cage on August 3. By 2026 they had swapped alignments "
                      "entirely — Fatu standing with Reigns' Bloodline, Sikoa opposite it."),
            dict(name="Cody Rhodes",
                 desc="The inherited feud. Sikoa attacked Rhodes through 2023 as Reigns' proxy, then "
                      "made it his own in 2024: the Bloodline Rules loss at SummerSlam in Cleveland "
                      "on August 3, and the tag loss alongside Fatu to Rhodes and a returning Reigns "
                      "at Bad Blood on October 5."),
            dict(name="Sami Zayn",
                 desc="Zayn's SmackDown open challenge on August 29, 2025 ended the US title reign at "
                      "62 days, and the MFT spent the autumn of 2025 feuding with him over it. The "
                      "loss is the hinge of the late-career story: the reign that legitimised the MFT "
                      "was gone within nine weeks."),
            dict(name="The Usos",
                 desc="He expelled Jimmy from the Bloodline in 2024, fought both brothers through the "
                      "civil war, and faced them again at SummerSlam 2026 from the other side — "
                      "beating them in the August 1 six-man, then mocking Jey's “run it "
                      "back” entrance. The August 24 Raw tag against them ended in a no-contest "
                      "when OTM attacked all four men, which may yet force the brothers and Sikoa "
                      "onto the same side."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Thin by design — the verified list is short, and nothing is added to pad it.",
        rows=[
            dict(when="2024&ndash;", title="WWE 2K", kind="Game",
                 desc="Playable in the current WWE 2K entries; his earliest appearance in the series "
                      "was not verified in this pass and is not claimed."),
            dict(when="2022&ndash;", title="The Bloodline storyline", kind="Television",
                 desc="The central long-form story of the Reigns era, named ESPN's Best Storyline in "
                      "2022 and 2023 with Sikoa's enforcer run at its core, and Pro Wrestling "
                      "Illustrated's Faction of the Year in 2022 and 2024."),
            dict(when="2018&ndash;2021", title="Independent circuit", kind="Origins",
                 desc="FSW in Las Vegas and AWF in Arizona as Sefa Fatu — the only stretch of his "
                      "career outside the family company. No film, scripted television, podcast or "
                      "documentary centred on him could be verified, so none is listed."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records and the flags, stated the way the sources state them.",
        stats=[
            ("62", "Days as US Champion"),
            ("7",  "Days as NXT NA Champion"),
            ("2",  "Bloodlines led"),
        ],
        rows=[
            dict(name="62 days as WWE United States Champion",
                 sub="June 28 to August 29, 2025, won from Jacob Fatu at Night of Champions and lost "
                     "to Sami Zayn's open challenge. Wikipedia calls him the third wrestler in the "
                     "Anoa'i family to win the title — a single-sourced framing published as "
                     "reported."),
            dict(name="WWE Tag Team Champion with a disputed day count",
                 sub="Won January 9, 2026 with Tama Tonga from the Wyatt Sicks; the belts left the "
                     "MFT on March 20, 2026 against Damian Priest and R-Truth, dropped that night by "
                     "Tama Tonga and JC Mateo. Wikipedia's 56-day figure for Sikoa's share does not "
                     "match those endpoints (70 days), so no day count is endorsed here."),
            dict(name="NXT North American Champion for seven days",
                 sub="Beat Carmelo Hayes on September 13, 2022, defended against Madcap Moss on "
                     "SmackDown, and vacated on September 20 — the main-roster debut ten days earlier "
                     "had already made the NXT run untenable."),
            dict(name="Two Survivor Series WarGames matches, one on each side of the family war",
                 sub="Won in 2022 inside Roman Reigns' Bloodline; lost in 2024 leading his own "
                     "version against Reigns' loyalists and CM Punk."),
            dict(name="Beat John Cena at Crown Jewel 2023",
                 sub="November 4, 2023, in Cena's only match of that year — the win WWE used to "
                     "certify the enforcer as a singles act."),
            dict(name="Led two factions before turning 34",
                 sub="The usurper Bloodline of 2024-25 and the MFT of 2025-26. Both ended the same "
                     "way: the membership walked, was expelled, or was released."),
            dict(name="Awards: storyline and faction honours, not singles ones",
                 sub="ESPN Best Storyline 2022 and 2023, and PWI Faction of the Year 2022 and 2024, "
                     "all for the Bloodline (per Wikipedia). No verified singles award is on record, "
                     "which is its own comment on how WWE has used him."),
        ],
        footnote=("Two things are deliberately absent. No career win-loss record: no verified total "
                  "exists and none is invented. And no Crown Jewel 2024 result: one summary claimed "
                  "Sikoa pinned Roman Reigns there, no second source corroborates it, and it "
                  "contradicts the verified arc of the civil war, so it is left out entirely."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Solo_Sikoa"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/solo-sikoa"),
        dict(k="Wrestling Inc.", v="August 17, 2026 — the Samoan Spike on Roman Reigns",
             href="https://www.wrestlinginc.com/2238834/wwe-raw-solo-sikoa-spikes-roman-reigns-rejects-bloodline-la-knight/"),
        dict(k="Wrestling Inc.", v="June 26, 2026 — the Tongas walk out and the MFT dissolves",
             href="https://www.wrestlinginc.com/2203080/wwe-smackdown-tama-tonga-talla-solo-sikoa-mft/"),
        dict(k="WrestleZone", v="SummerSlam 2026 Night 1 — the six-man with LA Knight and Royce Keys",
             href="https://www.wrestlezone.com/news/1655239-wwe-summerslam-night-1-results-review-grades-card-august-1"),
        dict(k="CBS Sports", v="August 24, 2026 Raw — Royce Keys and OTM attack",
             href="https://www.cbssports.com/wwe/news/wwe-raw-live-updates-results-review-grades-august-24-oba-femi-bron-breakker/live/"),
        dict(k="Khel Now", v="What's next after refusing the Bloodline",
             href="https://khelnow.com/wwe/whats-next-for-solo-sikoa-after-refusing-to-join-roman-reigns-bloodline-wwe-202608"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Why did Solo Sikoa turn on Roman Reigns?",
            a="Because Reigns demanded submission, not partnership. On the August 17, 2026 Raw, Reigns "
              "told Sikoa to fall in line and prove his loyalty to the family by attacking LA Knight. "
              "Sikoa answered with a Samoan Spike to Reigns and put Jey Uso into the barricade; Knight "
              "hit Jimmy Uso with the BFT and the two left together. The groundwork was months old "
              "&mdash; the MFT had dissolved on June 26 when Tama and Talla Tonga walked out blaming "
              "his obsession with Reigns, and Sikoa, Knight and Royce Keys had already beaten The Usos "
              "and Jacob Fatu at SummerSlam on August 1.",
            q_ld="Why did Solo Sikoa turn on Roman Reigns in 2026?",
            a_ld="On the August 17, 2026 episode of WWE Raw, Roman Reigns demanded that Solo Sikoa fall "
                 "in line and prove his loyalty to The Bloodline by attacking LA Knight. Sikoa refused "
                 "and hit Reigns with a Samoan Spike, then attacked The Usos alongside LA Knight. The "
                 "turn followed months of build: Sikoa's MFT faction dissolved on June 26, 2026 when "
                 "Tama Tonga and Talla Tonga walked out, and Sikoa, LA Knight and Royce Keys defeated "
                 "The Usos and Jacob Fatu at SummerSlam 2026 on August 1."),
        dict(
            q="Is Solo Sikoa really related to The Usos, Roman Reigns and The Rock?",
            a="Yes &mdash; this part of the storyline is real. He was born Joseph Yokozuna Fatu, the "
              "youngest son of Rikishi, which makes The Usos his actual older brothers. Roman Reigns "
              "and The Rock are members of the same extended Anoa'i wrestling dynasty. Jacob Fatu is "
              "his cousin, the son of Sam Fatu. His middle name honours Yokozuna, another family "
              "relation. The alignment wars are fiction; the family tree is not.",
            q_ld="Is Solo Sikoa really related to The Usos, Roman Reigns and The Rock?",
            a_ld="Yes. Solo Sikoa was born Joseph Yokozuna Fatu and is the youngest son of the WWE "
                 "wrestler Rikishi, making The Usos his real older brothers. He is part of the Anoa'i "
                 "wrestling dynasty, the same extended Samoan wrestling family as Roman Reigns and "
                 "Dwayne The Rock Johnson. Jacob Fatu is his cousin. His middle name honours the "
                 "former WWE Champion Yokozuna, also a relative."),
        dict(
            q="What championships has Solo Sikoa held?",
            a="Three in WWE: the <b>United States Championship</b> (62 days in 2025, won from Jacob "
              "Fatu, lost to Sami Zayn), the <b>WWE Tag Team Championship</b> with Tama Tonga (won "
              "January 9, 2026; the belts left the MFT on March 20), and the <b>NXT North American "
              "Championship</b> (seven days in September 2022, vacated on main-roster call-up). "
              "Before WWE he held Nevada and Arizona independent titles as Sefa Fatu. He has never "
              "held a world championship.",
            q_ld="What championships has Solo Sikoa held?",
            a_ld="Solo Sikoa has held three WWE championships: the WWE United States Championship for "
                 "62 days in 2025, the WWE Tag Team Championship with Tama Tonga from January 9, 2026 "
                 "until the MFT lost the titles on March 20, 2026, and the NXT North American "
                 "Championship for seven days in September 2022, which he vacated after his "
                 "main-roster call-up. On the independents he held the FSW Nevada State Championship "
                 "and the AWF Heavyweight Championship as Sefa Fatu. He has never held a world "
                 "championship."),
        dict(
            q="What happened to the MFT?",
            a="It came apart in stages across 2026. JC Mateo and Tonga Loa were released by WWE in "
              "April, part of the post-WrestleMania cuts. On the June 26 SmackDown in London, Tama "
              "Tonga and Talla Tonga told Sikoa they had &ldquo;heard from the elders&rdquo; and "
              "walked out, blaming his fixation on Roman Reigns for the June 19 tag title loss to "
              "Damian Priest and R-Truth. The Tongas then won the WWE Tag Team Championship without "
              "him on August 14, 2026, with their father Haku at ringside &mdash; so the faction "
              "Sikoa built holds gold he does not.",
            q_ld="What happened to Solo Sikoa's MFT faction?",
            a_ld="The MFT dissolved in stages during 2026. JC Mateo and Tonga Loa were released by WWE "
                 "in April 2026. On the June 26, 2026 SmackDown, Tama Tonga and Talla Tonga walked out "
                 "on Solo Sikoa, blaming his obsession with Roman Reigns for a tag team title loss. "
                 "Tama and Talla Tonga went on to win the WWE Tag Team Championship in a triple threat "
                 "match on the August 14, 2026 SmackDown, and retained the titles against Damian "
                 "Priest and R-Truth on August 21."),
        dict(
            q="Is Solo Sikoa a babyface now, and what brand is he on?",
            a="Yes, for the first time in his WWE career, and he is appearing on <b>Raw</b> &mdash; "
              "the turn happened there on August 17, 2026, and the follow-up tag with LA Knight "
              "against The Usos on August 24 did too. As of August 31, 2026 he holds no championship "
              "and is fighting on two fronts: Roman Reigns' rebuilt Bloodline on one side, and Royce "
              "Keys and OTM &mdash; the group that ambushed him, Knight and The Usos on August 24 "
              "&mdash; on the other.",
            q_ld="Is Solo Sikoa a babyface now, and what brand is he on?",
            a_ld="As of August 31, 2026, Solo Sikoa is a babyface for the first time in his WWE career "
                 "and is appearing on Raw. He turned on Roman Reigns on the August 17, 2026 Raw and "
                 "allied with LA Knight. He holds no championship and is involved in conflicts with "
                 "both Roman Reigns' Bloodline and the faction OTM, led by Royce Keys, which attacked "
                 "Sikoa, LA Knight and The Usos on the August 24, 2026 Raw."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Joseph Yokozuna Fatu",
             sub="the middle name honours Yokozuna, a family relation"),
        dict(label="Born", value="March 18, 1993", sub="age 33"),
        dict(label="Family", value="Son of Rikishi; brother of The Usos",
             sub="Anoa'i dynasty &middot; cousin of Jacob Fatu &middot; related to Roman Reigns and "
                 "The Rock"),
        dict(label="Height", value="6&#8242;2&#8243;", sub="188 cm"),
        dict(label="Weight", value="250 lb", sub="113 kg (billed)"),
        dict(label="Debut", value="April 29, 2018", sub="independents, as Sefa Fatu"),
        dict(label="Trained by", value="Rikishi",
             sub="with Kenny King, Sinn Bodhi and the WWE Performance Center"),
        dict(label="Signature", value="Samoan Spike &middot; Spinning Solo",
             sub="the Spike inherited from Umaga's lineage of thrust strikes"),
        dict(label="Education", value="American River College &middot; Dickinson State",
             sub="college football before wrestling"),
        dict(label="Brand", value="Raw", sub="per the August 2026 booking"),
        dict(label="Also known as",
             value="The Street Champion &middot; The Enforcer &middot; the self-styled Tribal Chief"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1993-03-18",
    bornplace="California, United States",
    nationality="United States",
    height_cm=188,
    weight_kg=113,
    ld=dict(
        alternateName=["Joseph Yokozuna Fatu", "Sefa Fatu", "The Street Champion",
                       "The Enforcer of the Bloodline"],
        award=["WWE United States Championship (1 reign, 62 days)",
               "WWE Tag Team Championship (1 reign, with Tama Tonga)",
               "NXT North American Championship (1 reign)",
               "FSW Nevada State Championship (1 reign)",
               "AWF Heavyweight Championship (1 reign)",
               "ESPN Best Storyline (2022, 2023, as part of The Bloodline)",
               "PWI Faction of the Year (2022, 2024, as part of The Bloodline)"],
        knowsAbout=["Professional wrestling", "The Bloodline", "MFT", "WWE", "NXT",
                    "Anoa'i family", "Championship wrestling"],
        description="Solo Sikoa, born Joseph Yokozuna Fatu, is an American professional wrestler "
                    "signed to WWE and a member of the Anoa'i wrestling dynasty - the youngest son of "
                    "Rikishi and brother of The Usos. He debuted as Roman Reigns' Bloodline enforcer "
                    "in September 2022, led his own version of the Bloodline and the MFT faction from "
                    "2024 to 2026, and held the WWE United States Championship for 62 days in 2025. "
                    "On August 17, 2026 he turned on Roman Reigns and allied with LA Knight.",
        sameAs=["https://en.wikipedia.org/wiki/Solo_Sikoa",
                "https://www.wwe.com/superstars/solo-sikoa"],
    ),
)
