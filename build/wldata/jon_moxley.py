# -*- coding: utf-8 -*-
"""Jon Moxley - dossier data.

Sources: web research compiled August 31, 2026, the day after Moxley retained the AEW
Continental Championship over Nigel McGuinness in the Continental Challenge Cup final at
All In: London. WWE-era dates cross-checked against Wikipedia; AEW/NJPW dates against
AEW.com's championship history, Fightful, POST Wrestling and Wrestling Inc coverage.
Nothing is invented.

Deliberate omissions:
  * No career win-loss total - none verified.
  * His first Intercontinental Championship win (over Kevin Owens, December 2015) is
    absent from the match rows: consulted sources conflicted on the exact date, so it
    appears in prose at month precision instead.
  * The length of the second IWGP US reign is not printed as a day count - the "564
    days" figure circulating does not match the verified endpoints, so only the
    endpoints are given.
  * No social links and no theme entry - not verified in this pass.
"""

# ----------------------------------------------------------------- record rows
# Twenty-one documented bouts from a career that has lapped three companies. A curated
# ledger, not a career count.
ROWS = [
    dict(result="W", date="2012-12-16", promo="WWE", type="tag", landmark=True,
         event="TLC", opponent="Team Hell No & Ryback",
         stip="Six-man TLC — The Shield's first match, with Rollins and Reigns", title=""),
    dict(result="W", date="2013-05-19", promo="WWE",
         event="Extreme Rules", opponent="Kofi Kingston",
         stip="Singles — a 351-day reign begins", title="WWE United States Championship"),
    dict(result="W", date="2016-06-19", promo="WWE", landmark=True,
         event="Money in the Bank", opponent="Seth Rollins",
         stip="Won the ladder match and cashed in the same night", title="WWE Championship"),
    dict(result="W", date="2019-06-05", promo="NJPW", landmark=True,
         event="Best of the Super Juniors 26 finals night", opponent="Juice Robinson",
         stip="Singles — NJPW debut, six weeks after leaving WWE",
         title="IWGP United States Championship"),
    dict(result="W", date="2019-11-09", promo="AEW",
         event="Full Gear", opponent="Kenny Omega", opponent_html=True,
         stip="Unsanctioned Lights Out match", title=""),
    dict(result="W", date="2020-01-04", promo="NJPW",
         event="Wrestle Kingdom 14 Night 1", opponent="Lance Archer",
         stip="Texas Deathmatch — regains the vacated title",
         title="IWGP United States Championship"),
    dict(result="W", date="2020-02-29", promo="AEW", landmark=True,
         event="Revolution", opponent="Chris Jericho",
         stip="Singles — first reign begins", title="AEW World Championship"),
    dict(result="W", date="2022-08-24", promo="AEW",
         event="Dynamite", opponent="CM Punk",
         stip="Title unification — over in about three minutes", title="AEW World Championship"),
    dict(result="W", date="2022-09-21", promo="AEW",
         event="Dynamite: Grand Slam", opponent="Bryan Danielson",
         stip="Tournament final for the vacated title — third reign", title="AEW World Championship"),
    dict(result="L", date="2022-11-19", promo="AEW", landmark=True,
         event="Full Gear", opponent="MJF", opponent_html=True,
         stip="Singles — MJF wins with the Dynamite Diamond Ring", title="AEW World Championship"),
    dict(result="W", date="2023-09-03", promo="AEW",
         event="All Out", opponent="Orange Cassidy",
         stip="Singles — ends Cassidy's 326-day reign", title="AEW International Championship"),
    dict(result="W", date="2024-04-12", promo="NJPW", landmark=True,
         event="Windy City Riot — Chicago", opponent="Tetsuya Naito",
         stip="Singles — first man to win WWE, AEW and IWGP world titles",
         title="IWGP World Heavyweight Championship"),
    dict(result="W", date="2024-10-12", promo="AEW", landmark=True,
         event="WrestleDream", opponent="Bryan Danielson",
         stip="Singles — fourth reign; the loss ends Danielson's full-time career",
         title="AEW World Championship"),
    dict(result="L", date="2025-07-12", promo="AEW", landmark=True,
         event="All In: Texas", opponent="Hangman Adam Page",
         stip="Texas Deathmatch — 5.5 stars (Meltzer); the 273-day reign ends",
         title="AEW World Championship"),
    dict(result="W", date="2025-12-27", promo="AEW", landmark=True,
         event="Worlds End", opponent="Kazuchika Okada", opponent_html=True,
         stip="Continental Classic final — ends Okada's 648-day reign",
         title="AEW Continental Championship"),
    dict(result="D", date="2026-02-14", promo="AEW",
         event="Grand Slam: Australia", opponent="Konosuke Takeshita",
         stip="Time-limit draw — title retained", title="AEW Continental Championship"),
    dict(result="W", date="2026-03-15", promo="AEW",
         event="Revolution", opponent="Konosuke Takeshita",
         stip="No time limit — Takeshita choked out", title="AEW Continental Championship"),
    dict(result="W", date="2026-04-12", promo="AEW",
         event="Dynasty", opponent="Will Ospreay", opponent_html=True,
         stip="Singles — Ospreay's first singles match back from surgery",
         title="AEW Continental Championship"),
    dict(result="W", date="2026-05-24", promo="AEW",
         event="Double or Nothing", opponent="Kyle O'Reilly",
         stip="Singles — submission", title="AEW Continental Championship"),
    dict(result="W", date="2026-06-28", promo="AEW",
         event="Forbidden Door — San Jose", opponent="Bandido",
         stip="Singles", title="AEW Continental Championship"),
    dict(result="W", date="2026-08-30", promo="AEW", landmark=True,
         event="All In: London — Wembley", opponent="Nigel McGuinness",
         stip="Continental Challenge Cup final — ankle lock submission",
         title="AEW Continental Championship"),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Kenny Omega": "kenny-omega", "MJF": "mjf",
                 "Kazuchika Okada": "kazuchika-okada", "Will Ospreay": "will-ospreay"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="jon-moxley",
    name="Jon Moxley",
    realname="Jonathan David Good",
    epithet="The Death Rider",
    hook="Record & Titles",

    meta_desc=("Jon Moxley is a four-time AEW World Champion, former WWE Champion as Dean Ambrose, "
               "former IWGP World Heavyweight Champion, and the reigning AEW Continental Champion "
               "who won the Continental Challenge Cup at All In: London. Full record, titles, "
               "factions and career."),
    og_desc=("The Death Rider: world titles in WWE, AEW and NJPW — the first man to hold all "
             "three — four AEW World Championship reigns, and the Continental Championship he "
             "defended at Wembley on August 30, 2026."),
    tw_desc="The Death Rider: WWE, AEW and IWGP world titles, and the AEW Continental belt today.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2004",
    height_imp="6&#8242;4&#8243;",
    weight_lb="234",
    world_titles="6",
    vitals_tagline="Wherever, whenever",
    support_note="Merch &middot; Read &middot; Watch",
    x_url="https://x.com/JonMoxley",
    sp_items=[
        dict(ic="MX", title="AEW Shop", sub="Official tees · Shop AEW",
             tag="Shop", href="https://shop.aew.com/"),
        dict(ic="AEW", title="AEW Roster Profile", sub="AllEliteWrestling.com", tag="Visit",
             href="https://www.allelitewrestling.com/aew-roster"),
        dict(ic="BK", title="MOX", sub="His 2021 autobiography",
             tag="Read", href="https://en.wikipedia.org/wiki/Jon_Moxley"),
        dict(ic="W", title="Wikipedia", sub="Full biography", tag="Read", charity=True,
             href="https://en.wikipedia.org/wiki/Jon_Moxley"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Formerly Dean Ambrose &middot; The Purveyor of Violence &middot; Death Riders' "
              "founder",
    hero_tag="Cincinnati, Ohio &middot; <em>HWA &middot; CZW &middot; WWE &middot; NJPW &middot; "
             "AEW &middot; 2004&ndash;present</em>",
    now_label="NOW",
    now_bold="AEW Continental Champion — and Continental Challenge Cup winner",
    now_tail=" &middot; submitted Nigel McGuinness with an ankle lock in the cup final at All In: "
             "London, August 30, 2026",
    hstats=[
        dict(value="4",   x=True,  label="AEW World Titles"),
        dict(value="620", x=False, label="Combined Days, AEW Champ"),
        dict(value="1st", x=False, label="WWE-AEW-IWGP Triple"),
        dict(value="246", x=False, label="Days as Continental Champ"),
    ],
    ghost_link="From Cincinnati deathmatches to titles in three majors",
    vlabel="Est. 2004 &middot; Cincinnati, Ohio",
    mono="MX",

    # ---------------------------------------------------------------- 01 overview
    correction=2,
    overview=[
        "<b>Jon Moxley</b> walked out of Wembley Stadium on August 30, 2026 still the AEW "
        "Continental Champion, having submitted Nigel McGuinness with an ankle lock in the final "
        "of the inaugural Continental Challenge Cup at All In: London. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">4</span>'
        '<span class="pull-cap">AEW World Championship reigns &mdash; 620 combined days, the most of anyone</span></span>'
        "The reign began when he beat Kazuchika Okada in the Continental Classic final at Worlds "
        "End on December 27, 2025 &mdash; ending Okada&rsquo;s 648-day run &mdash; and he has "
        "spent 2026 grinding through challengers: a time-limit draw and then a no-time-limit "
        "choke-out of Konosuke Takeshita, Will Ospreay at Dynasty, Kyle O&rsquo;Reilly, Bandido, "
        "and now McGuinness. It is the label that fits the whole career: he does not headline "
        "every show anymore, he just never stops holding something.",

        "The resume is a three-company matter. In WWE, as <b>Dean Ambrose</b>, he debuted as a "
        "third of The Shield at Survivor Series 2012, won the WWE Championship by taking the "
        "Money in the Bank briefcase and cashing it in on Seth Rollins the same night &mdash; "
        "June 19, 2016 &mdash; and finished as the company&rsquo;s 27th Triple Crown and 16th "
        "Grand Slam champion, with three Intercontinental reigns, a 351-day United States reign "
        "and two tag titles alongside Rollins. In AEW he has won the World Championship four "
        "times &mdash; 2020, twice in 2022, and 2024 &mdash; for 620 combined days, the most in "
        "company history per Wikipedia. In NJPW he won the IWGP United States Championship in "
        "his debut match in June 2019 and, at Windy City Riot on April 12, 2024, beat Tetsuya "
        "Naito for the IWGP World Heavyweight Championship to become the first man ever to hold "
        "WWE&rsquo;s, AEW&rsquo;s and New Japan&rsquo;s top titles.",

        "One bookkeeping correction his own reign count needs: the <b>second</b> AEW World reign "
        "has two start dates depending on who is counting. He won the <i>interim</i> "
        "championship at Forbidden Door on June 26, 2022, beating Hiroshi Tanahashi, and became "
        "the undisputed champion by beating CM Punk in about three minutes on the August 24, "
        "2022 Dynamite &mdash; the date Wikipedia&rsquo;s championship list uses for the reign "
        "proper. Retellings that date it from June overstate the reign by two months. However "
        "counted, he lost it back to Punk at All Out on September 4, then won the vacated title "
        "again seventeen days later when Punk&rsquo;s tenure imploded &mdash; two reigns whose "
        "entire shape was another man&rsquo;s exit.",

        "The current chapter is the <b>Death Riders</b>, the faction he built by turning on "
        "Bryan Danielson at All Out on September 7, 2024 &mdash; a plastic bag over the head of "
        "his old Blackpool Combat Club partner &mdash; and formalized that November. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">1st</span>'
        '<span class="pull-cap">man to hold the WWE, AEW and IWGP world championships &mdash; completed April 12, 2024 in Chicago</span></span>'
        "As its head he took the AEW World Championship from Danielson at WrestleDream on "
        "October 12, 2024 &mdash; the loss that ended Danielson&rsquo;s full-time career &mdash; "
        "held it 273 days through a fortress-booking reign, and lost it to Hangman Page in a "
        "5.5-star Texas Deathmatch at All In: Texas on July 12, 2025. The 2026 wrinkle was Will "
        "Ospreay: recruited in July, gone by July 29 after refusing Moxley&rsquo;s order to "
        "suffocate Kenny Omega, and unpunished on the way out &mdash; by Moxley&rsquo;s "
        "standards, practically a blessing.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["AEW", "WWE", "NJPW"],
        promo_labels={"AEW": "AEW", "WWE": "WWE", "NJPW": "NJPW"},
        stats=[
            ("4&times;", "AEW World Champion"),
            ("620",  "Combined days, AEW World"),
            ("6",    "World titles, 3 companies"),
            ("273",  "Day fourth reign"),
            ("2&times;", "IWGP US Champion"),
            ("246",  "Days as Continental champ"),
        ],
        lead=("Twenty-one documented bouts across WWE, NJPW and AEW &mdash; the Shield's first "
              "match, the same-night cash-in, all four AEW World wins or their endings, and "
              "every 2026 Continental defense. This is a curated ledger, not a career count; no "
              "win&ndash;loss total is published because none could be verified, and the 2015 "
              "Intercontinental win is in prose rather than a row because sources conflicted on "
              "its exact date. Filter by match type, tap any column header to sort, and turn "
              "spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("Not a ratings-chaser by trade, but the violent epics have piled up "
                    "anyway. Ratings are Dave Meltzer's as published; the Hangman figure was "
                    "widely reported from the Observer after All In: Texas."),
    signature=[
        dict(rating="5.5", event="All In: Texas 2025", opponent="Hangman Adam Page",
             stip="Texas Deathmatch — the AEW World Championship reign ends"),
        dict(rating="5.0", event="Revolution 2023", opponent="Hangman Adam Page",
             stip="Texas Deathmatch — the first war of the pair"),
        dict(rating="5.0", event="G1 Climax 29, day 4", opponent="Tomohiro Ishii",
             stip="His first NJPW tournament — an instant styles bullseye"),
        dict(rating="5.0", event="Double or Nothing 2022", opponent="Jericho Appreciation Society",
             stip="The inaugural Anarchy in the Arena, with the Blackpool Combat Club side"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("6",   "World title reigns"),
            ("4&times;", "AEW World"),
            ("351", "Day US title reign"),
            ("1",   "Continental reign, current"),
        ],
        lead=("Six world championship reigns across three companies, plus the mid-card belts "
              "that made him WWE's 16th Grand Slam champion. Independent-era reign dates were "
              "not verified in this pass and are summarized rather than itemized."),
        rows=[
            dict(ic="A", name="AEW World Championship", count="4",
                 sub="2020 (def. Jericho at Revolution, February 29) &middot; 2022 (unified over "
                     "CM Punk, August 24, after the interim win at Forbidden Door) &middot; 2022 "
                     "(tournament final over Danielson at Grand Slam, September 21) &middot; "
                     "2024&ndash;25 (def. Danielson at WrestleDream, October 12; lost to Hangman "
                     "Page after 273 days) &middot; <b>620 combined days</b>, the most in AEW "
                     "history per Wikipedia"),
            dict(ic="C", name="AEW Continental Championship", count="1",
                 sub="December 27, 2025 &ndash; present &middot; won the Continental Classic "
                     "final over Kazuchika Okada at Worlds End, ending the 648-day reign &middot; "
                     "defenses against Takeshita (twice), Ospreay, O&rsquo;Reilly, Bandido and "
                     "McGuinness &middot; Continental Challenge Cup winner, August 30, 2026"),
            dict(ic="W", name="WWE Championship", count="1",
                 sub="June 19 &ndash; September 11, 2016 &middot; won the Money in the Bank "
                     "ladder match and cashed in on Seth Rollins the same night; lost to AJ "
                     "Styles at Backlash"),
            dict(ic="G", name="IWGP World Heavyweight Championship", count="1",
                 sub="April 12 &ndash; June 2024 &middot; def. Tetsuya Naito at Windy City Riot "
                     "in Chicago &mdash; the win that completed the WWE-AEW-NJPW triple &middot; "
                     "lost back to Naito at Forbidden Door on June 30"),
            dict(ic="U", name="IWGP United States Championship", count="2",
                 sub="June 5 &ndash; October 13, 2019 (won in his NJPW debut over Juice Robinson; "
                     "vacated when a typhoon stranded a defense) &middot; January 4, 2020 &ndash; "
                     "August 14, 2021 (regained from Lance Archer in a Texas Deathmatch at "
                     "Wrestle Kingdom 14, lost back to Archer at Resurgence)"),
            dict(ic="I", name="AEW International Championship", count="1",
                 sub="September 3 &ndash; 20, 2023 &middot; def. Orange Cassidy at All Out, lost "
                     "to Rey Fenix at Grand Slam &mdash; 17 days, per AEW&rsquo;s own title "
                     "history"),
            dict(ic="S", name="WWE United States Championship", count="1",
                 sub="May 19, 2013 &ndash; May 2014 &middot; def. Kofi Kingston at Extreme Rules "
                     "&middot; <b>351 days</b>, the longest reign of WWE&rsquo;s ownership era at "
                     "the time"),
            dict(ic="IC", name="WWE Intercontinental Championship", count="3",
                 sub="December 2015 (from Kevin Owens) &middot; January 2017 (from The Miz) "
                     "&middot; December 2018 (from Seth Rollins at TLC) &mdash; part of the "
                     "resume that made him WWE&rsquo;s 27th Triple Crown and 16th Grand Slam "
                     "champion"),
            dict(ic="T", name="WWE Raw Tag Team Championship", count="2",
                 sub="Both with Seth Rollins, 2017 and 2018"),
            dict(ic="Z", name="Independent deathmatch titles", count="—",
                 sub="CZW World Heavyweight Champion and HWA champion in the 2000s Jon Moxley "
                     "era &middot; individual reign dates not verified in this pass"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Three units, each one a different theory of violence.",
        cards=[
            dict(era="WWE &middot; 2012&ndash;2014, 2017&ndash;2019",
                 name="The Shield",
                 members="Dean Ambrose, Seth Rollins, Roman Reigns",
                 desc="Debuted at Survivor Series on November 18, 2012 and won their first match "
                      "— a six-man TLC — that December. Three main-event careers came out of "
                      "one unit, an almost unrepeatable hit rate. Ambrose was its unstable "
                      "conscience, betrayed by Rollins in 2014 and central to every reunion "
                      "through his 2019 exit."),
            dict(era="AEW &middot; 2022&ndash;2024",
                 name="Blackpool Combat Club",
                 members="Jon Moxley, Bryan Danielson, Claudio Castagnoli, Wheeler Yuta, William "
                         "Regal (manager)",
                 desc="Formed in March 2022 around William Regal — a shoot-style guild built on "
                      "hard sparring and mutual respect. It produced five-star chaos (both early "
                      "Anarchy in the Arena matches) and ended the only way a Moxley story ends: "
                      "with the respect withdrawn."),
            dict(era="AEW &middot; 2024&ndash;present",
                 name="Death Riders",
                 members="Jon Moxley (leader), Claudio Castagnoli, Wheeler Yuta, Marina Shafir, "
                         "PAC, Daniel Garcia; Will Ospreay, July 2026 only",
                 desc="Born September 7, 2024 at All Out, when Moxley and Castagnoli turned on "
                      "Danielson with a plastic bag; renamed from the BCC that November, after "
                      "his NJPW nickname. The group carried his 273-day World Championship reign "
                      "and his current Continental one. Ospreay joined July 1, 2026 and handed "
                      "his patch back on July 29 after refusing to suffocate Kenny Omega; "
                      "Moxley, uncharacteristically, let him go."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Three names, one temperament: <b>Jon Moxley</b> (2004&ndash;2011) &rarr; <b>Dean "
             "Ambrose</b> (2011&ndash;2019) &rarr; <b>Jon Moxley</b> again (2019&ndash;present), "
             "now with the NJPW-coined <b>Death Rider</b> layered on top.",
        cards=[
            dict(mono="MOX", era="Indies &middot; 2004&ndash;2011", name="Jon Moxley, deathmatch kid",
                 desc="A Cincinnati dropout trained in the HWA system who became one of CZW's "
                      "defining deathmatch champions — glass, tacks and monologues that already "
                      "sounded like his later promos."),
            dict(mono="DA", era="WWE &middot; 2011&ndash;2019", name="Dean Ambrose",
                 desc="The Lunatic Fringe: Shield enforcer, 351-day United States Champion, "
                      "same-night Money in the Bank cash-in, Triple Crown and Grand Slam. He "
                      "left when his contract expired on April 30, 2019, publicly citing "
                      "creative frustration."),
            dict(mono="JM", era="AEW &amp; NJPW &middot; 2019&ndash;present", name="Jon Moxley, reclaimed",
                 desc="The name buyback is the whole story: within six weeks of leaving WWE he "
                      "had debuted in AEW at Double or Nothing and won the IWGP US title in his "
                      "first NJPW match. Four AEW World Championships followed."),
            dict(mono="DR", era="AEW &middot; 2024&ndash;present", name="The Death Rider",
                 desc="The nickname NJPW gave his finisher, made flesh as a faction leader: "
                      "paranoid, doctrinaire, violence-as-philosophy. The plastic bag is its "
                      "sacrament — used on Danielson in 2024, refused by Ospreay in 2026."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Cincinnati deathmatches to a Wembley submission win, twenty-two years on.",
        rows=[
            dict(year="2004", title="Debut",
                 desc="First matches in the Cincinnati-area HWA orbit; the CZW deathmatch run "
                      "that made the name follows in the late 2000s."),
            dict(year="2012", title="The Shield",
                 desc="Debuts at Survivor Series on November 18 with Seth Rollins and Roman "
                      "Reigns; the trio wins its first match at TLC on December 16."),
            dict(year="2016", title="WWE Champion in one night",
                 desc="June 19: wins the Money in the Bank ladder match, then cashes in on Seth "
                      "Rollins the same evening."),
            dict(year="2019", title="The exit and the double debut",
                 desc="Leaves WWE when his contract expires April 30; debuts at AEW Double or "
                      "Nothing on May 25 and wins the IWGP US title in his NJPW debut on June 5."),
            dict(year="2020", title="First AEW World Championship",
                 desc="Beats Chris Jericho at Revolution on February 29 and carries the company "
                      "through the pandemic year."),
            dict(year="2022", title="Two more reigns and the BCC",
                 desc="Forms the Blackpool Combat Club in March; unifies the title over CM Punk "
                      "on August 24; wins the vacated title again over Danielson at Grand Slam "
                      "on September 21; loses to MJF at Full Gear on November 19."),
            dict(year="2024", title="The IWGP World title and the Death Riders",
                 desc="Beats Naito at Windy City Riot on April 12 to complete the WWE-AEW-NJPW "
                      "triple; turns on Danielson at All Out on September 7; takes the AEW World "
                      "Championship from him at WrestleDream on October 12."),
            dict(year="2025", title="The 273-day reign falls, then a new belt",
                 desc="Loses the Texas Deathmatch to Hangman Page at All In: Texas on July 12 — "
                      "5.5 stars — then wins the Continental Classic and the Continental "
                      "Championship from Okada at Worlds End on December 27."),
            dict(year="2026", title="The Continental grind",
                 desc="Retains against Takeshita (draw, then choke-out at Revolution), Ospreay, "
                      "O'Reilly and Bandido; loses Ospreay from the Death Riders in July; "
                      "submits Nigel McGuinness to win the inaugural Continental Challenge Cup "
                      "at All In: London on August 30."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Kenny Omega", slug="kenny-omega",
                 desc="The Lights Out match at Full Gear on November 9, 2019 — unsanctioned, "
                      "barbed wire, a mission statement for early AEW — went to Moxley; Omega "
                      "answered by taking the AEW World Championship from him at Winter Is "
                      "Coming on December 2, 2020. In 2026 Moxley hunted Omega's second reign "
                      "through proxies until his own recruit refused the kill."),
            dict(name="Bryan Danielson",
                 desc="Partner and victim, twice over. Moxley beat him for the vacated title at "
                      "Grand Slam 2022, co-founded the BCC with him, then turned on him with a "
                      "plastic bag at All Out 2024 and took his championship — and his full-time "
                      "career — at WrestleDream on October 12, 2024."),
            dict(name="Hangman Adam Page",
                 desc="Two Texas Deathmatches, both landmarks: Revolution 2023, five stars, "
                      "Moxley's win; All In: Texas 2025, five and a half, Page's — the match "
                      "that ended the 273-day fortress reign and remains the highest-rated AEW "
                      "match of its year."),
            dict(name="CM Punk",
                 desc="Beat Punk in three minutes to unify the titles on August 24, 2022; lost "
                      "the rematch at All Out on September 4 — three days before Punk's AEW "
                      "world detonated at the Brawl Out press conference, handing Moxley the "
                      "vacated title chase he won."),
            dict(name="Kazuchika Okada", slug="kazuchika-okada",
                 desc="One match, maximum leverage: the Continental Classic final at Worlds End "
                      "on December 27, 2025, where Moxley's Paradigm Shift ended Okada's 648-day "
                      "Continental reign and split the Unified Championship in two."),
            dict(name="Nigel McGuinness",
                 desc="The Wembley final. McGuinness — whose in-ring comeback began as a "
                      "surprise Casino Gauntlet entrant at All In 2024, his first match since "
                      "2011 — made the Continental Challenge Cup final in his home city and "
                      "tapped to the ankle lock on August 30, 2026."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Beyond",
        lead="Short list, verified only.",
        rows=[
            dict(when="2021", title="MOX", kind="Book",
                 desc="His autobiography, written without a ghostwriter's varnish — the "
                      "Cincinnati years, WWE frustrations and sobriety all on the page."),
            dict(when="2015", title="12 Rounds 3: Lockdown", kind="Film",
                 desc="WWE Studios action lead during the Ambrose years."),
            dict(when="2020", title="Cagefighter: Worlds Collide", kind="Film",
                 desc="Post-WWE film appearance, per Wikipedia."),
            dict(when="2017&ndash;", title="Renee Paquette", kind="Personal",
                 desc="Married to the broadcaster since 2017; she now works AEW's own desk. "
                      "Their household spans the company's kayfabe wall and everyone seems fine "
                      "with it."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated the way the sources actually state them.",
        stats=[
            ("1st", "WWE-AEW-IWGP triple"),
            ("620", "Combined days, AEW World"),
            ("4",   "AEW World reigns"),
        ],
        rows=[
            dict(name="First man to win the WWE, AEW and IWGP world championships",
                 sub="Completed April 12, 2024 at Windy City Riot in Chicago, beating Tetsuya "
                     "Naito for the IWGP World Heavyweight title — on top of the 2016 WWE "
                     "Championship and four AEW World Championships."),
            dict(name="Four AEW World Championship reigns, 620 combined days",
                 sub="Both the reign count and the combined-days figure are the most in company "
                     "history, per Wikipedia's championship list."),
            dict(name="Same-night Money in the Bank cash-in",
                 sub="June 19, 2016: won the ladder match, then beat Seth Rollins for the WWE "
                     "Championship before the show ended."),
            dict(name="WWE's 27th Triple Crown and 16th Grand Slam champion",
                 sub="As Dean Ambrose — WWE, Intercontinental (3), United States and tag titles "
                     "all collected by 2017."),
            dict(name="351 days as WWE United States Champion",
                 sub="May 19, 2013 to May 2014 — at the time the longest reign of the title's "
                     "WWE era, per Wikipedia."),
            dict(name="Won a title in his first match in two different major companies",
                 sub="The IWGP United States Championship in his NJPW debut on June 5, 2019. In "
                     "AEW he debuted unannounced at Double or Nothing 2019 and was champion "
                     "within nine months."),
            dict(name="AEW Continental Champion and Continental Challenge Cup winner",
                 sub="Won the belt by ending Okada's 648-day reign in the 2025 Continental "
                     "Classic final; 246 days into the reign, took the inaugural Challenge Cup "
                     "at Wembley on August 30, 2026 over Nigel McGuinness."),
            dict(name="Most AEW pay-per-view main events",
                 sub="Wikipedia credits him with the most PPV headline appearances in AEW "
                     "history — a single-sourced tally, reported as such."),
            dict(name="Five-plus matches at five stars or better",
                 sub="Meltzer's list includes the Ishii G1 2019 match, both early Anarchy in the "
                     "Arena wars, the Revolution 2023 Texas Deathmatch, a 2023 NJPW trios "
                     "classic, and the 5.5-star All In: Texas loss to Hangman Page."),
        ],
        footnote=("Deliberately absent: a career win-loss total (none verified); a day-precision "
                  "date for the December 2015 Intercontinental win (sources conflict); the "
                  "circulating 564-day figure for the second IWGP US reign, which does not match "
                  "the verified endpoints and is therefore not printed."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Fightful", v="All In: London 2026 — the ankle-lock final",
             href="https://www.fightful.com/wrestling-news/jon-moxley-taps-out-nigel-mcguinness-wins-continental-challenge-cup-and-retains-aew-continental-championship-at-aew-all-in"),
        dict(k="Fightful", v="Worlds End 2025 — Continental Classic win over Okada",
             href="https://www.fightful.com/wrestling/jon-moxley-wins-2025-continental-classic-tournament-captures-aew-continental-championship-at-worlds-end-ppv/"),
        dict(k="Wikipedia", v="Full biography",
             href="https://en.wikipedia.org/wiki/Jon_Moxley"),
        dict(k="Wikipedia", v="List of AEW World Champions",
             href="https://en.wikipedia.org/wiki/List_of_AEW_World_Champions"),
        dict(k="AEW", v="International Championship history",
             href="https://www.allelitewrestling.com/aew-international-championship-history"),
        dict(k="Wikipedia", v="Death Riders",
             href="https://en.wikipedia.org/wiki/Death_Riders"),
        dict(k="ITR Wrestling", v="The five-star match ledger",
             href="https://itrwrestling.com/news/jon-moxley-awarded-fifth-career-5-star-match-following-recent-njpw-appearance/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="What title does Jon Moxley hold right now?",
            a="The <b>AEW Continental Championship</b>, held since December 27, 2025, when he "
              "beat Kazuchika Okada in the Continental Classic final at Worlds End &mdash; "
              "ending Okada&rsquo;s 648-day reign. On August 30, 2026 he retained it against "
              "Nigel McGuinness by ankle-lock submission in the final of the inaugural "
              "Continental Challenge Cup at All In: London, his sixth successful defense of "
              "2026 by this page&rsquo;s count.",
            q_ld="What championship does Jon Moxley currently hold?",
            a_ld="Jon Moxley holds the AEW Continental Championship, which he won on December "
                 "27, 2025 by defeating Kazuchika Okada in the Continental Classic final at "
                 "Worlds End. He most recently retained it on August 30, 2026 at AEW All In: "
                 "London, submitting Nigel McGuinness with an ankle lock to win the inaugural "
                 "Continental Challenge Cup."),
        dict(
            q="Was Moxley really the first to win WWE, AEW and IWGP world titles?",
            a="Yes. The WWE Championship came June 19, 2016 as Dean Ambrose; the AEW World "
              "Championship first came February 29, 2020; and the IWGP World Heavyweight "
              "Championship came April 12, 2024, beating Tetsuya Naito at Windy City Riot in "
              "Chicago &mdash; making him the first man to hold the top title of all three "
              "companies. He is a six-time world champion across them: one WWE, four AEW, one "
              "IWGP.",
            q_ld="Was Jon Moxley the first wrestler to win the WWE, AEW and IWGP world "
                 "championships?",
            a_ld="Yes. Jon Moxley won the WWE Championship in June 2016 as Dean Ambrose, the "
                 "AEW World Championship for the first time in February 2020, and the IWGP "
                 "World Heavyweight Championship on April 12, 2024 by defeating Tetsuya Naito "
                 "at NJPW Windy City Riot, becoming the first man to hold all three companies' "
                 "top titles. He has six world championship reigns across the three promotions."),
        dict(
            q="How many times has Moxley been AEW World Champion?",
            a="<b>Four</b> &mdash; 2020, twice in 2022, and 2024&ndash;25, for 620 combined "
              "days, the most in company history. One counting caution: the second reign is "
              "sometimes dated from the interim title win at Forbidden Door (June 26, 2022) "
              "rather than the unification win over CM Punk (August 24, 2022) that "
              "Wikipedia&rsquo;s list uses; the difference is two months of &ldquo;interim"
              "&rdquo; status, not a separate reign.",
            q_ld="How many AEW World Championship reigns has Jon Moxley had?",
            a_ld="Four. Jon Moxley won the AEW World Championship in February 2020, twice in "
                 "2022, and again in October 2024, for a combined 620 days as champion, the "
                 "most in AEW history. His second reign is officially dated from his August "
                 "24, 2022 unification win over CM Punk, though he had held the interim "
                 "championship since June 26, 2022."),
        dict(
            q="What are the Death Riders?",
            a="The faction Moxley leads &mdash; Claudio Castagnoli, Wheeler Yuta, Marina "
              "Shafir, PAC and Daniel Garcia &mdash; formed when he and Castagnoli turned on "
              "Bryan Danielson at All Out on September 7, 2024, and renamed from the Blackpool "
              "Combat Club that November after his NJPW nickname. Will Ospreay was a member "
              "for four weeks of July 2026, leaving after he refused Moxley&rsquo;s order to "
              "suffocate Kenny Omega with a plastic bag at Redemption.",
            q_ld="What is the Death Riders faction?",
            a_ld="The Death Riders are Jon Moxley's AEW faction, formed on September 7, 2024 "
                 "when Moxley and Claudio Castagnoli attacked Bryan Danielson at All Out, and "
                 "renamed from the Blackpool Combat Club in November 2024. Members include "
                 "Castagnoli, Wheeler Yuta, Marina Shafir, PAC and Daniel Garcia. Will Ospreay "
                 "joined on July 1, 2026 and left on July 29, 2026 after refusing to suffocate "
                 "Kenny Omega on Moxley's orders."),
        dict(
            q="Why did Nigel McGuinness get a title match at Wembley?",
            a="He earned the final of the inaugural <b>Continental Challenge Cup</b>, the 2026 "
              "summer tournament attached to Moxley&rsquo;s Continental Championship, and got "
              "the match in his home city of London. McGuinness&rsquo;s comeback is its own "
              "story &mdash; his return match, at All In 2024, was his first since retiring in "
              "2011. Moxley submitted him with an ankle lock after a match built on "
              "technical wrestling rather than plunder.",
            q_ld="Why did Jon Moxley face Nigel McGuinness at All In: London 2026?",
            a_ld="Nigel McGuinness reached the final of the inaugural Continental Challenge "
                 "Cup, a 2026 tournament whose final was contested for Jon Moxley's AEW "
                 "Continental Championship at All In: London on August 30, 2026. McGuinness, "
                 "a London native whose in-ring comeback began at All In 2024 after a 2011 "
                 "retirement, lost by submission to Moxley's ankle lock."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Jonathan David Good"),
        dict(label="Born", value="December 7, 1985", sub="Cincinnati, Ohio &middot; age 40"),
        dict(label="Billed from", value="Cincinnati, Ohio"),
        dict(label="Height", value="6&#8242;4&#8243;", sub="193 cm"),
        dict(label="Weight", value="234 lb", sub="106 kg (billed)"),
        dict(label="Debut", value="2004", sub="Cincinnati-area independents"),
        dict(label="Trained by", value="Les Thatcher &amp; Cody Hawk", sub="HWA system"),
        dict(label="Signature", value="Paradigm Shift / Death Rider &middot; Bulldog choke "
                                      "&middot; King Kong lariat",
             sub="The NJPW rename of his finisher named his faction"),
        dict(label="Current title", value="AEW Continental Championship",
             sub="Since December 27, 2025 &middot; Continental Challenge Cup winner"),
        dict(label="Family", value="Married to Renee Paquette", sub="Since 2017"),
        dict(label="Also known as",
             value="Dean Ambrose &middot; The Purveyor of Violence &middot; The Death Rider"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1985-12-07",
    bornplace="Cincinnati, Ohio, United States",
    nationality="United States",
    height_cm=193,
    weight_kg=106,
    ld=dict(
        alternateName=["Jonathan David Good", "Dean Ambrose", "The Death Rider",
                       "The Purveyor of Violence"],
        award=["AEW World Championship (4 reigns, 620 combined days)",
               "AEW Continental Championship (1 reign, current)",
               "AEW International Championship (1 reign)",
               "WWE Championship (1 reign)",
               "IWGP World Heavyweight Championship (1 reign)",
               "IWGP United States Championship (2 reigns)",
               "WWE Intercontinental Championship (3 reigns)",
               "WWE United States Championship (1 reign, 351 days)",
               "WWE Raw Tag Team Championship (2 reigns)",
               "Money in the Bank winner (2016)",
               "Continental Classic winner (2025)",
               "Continental Challenge Cup winner (2026)"],
        knowsAbout=["Professional wrestling", "Deathmatch wrestling", "All Elite Wrestling",
                    "WWE", "New Japan Pro-Wrestling", "The Shield", "Death Riders"],
        description="Jon Moxley, born Jonathan Good in Cincinnati, is an American professional "
                    "wrestler and the reigning AEW Continental Champion. Formerly WWE's Dean "
                    "Ambrose, he is a four-time AEW World Champion, a former WWE Champion and "
                    "IWGP World Heavyweight Champion — the first man to hold all three "
                    "companies' top titles — and leader of the Death Riders. He won the "
                    "inaugural Continental Challenge Cup at All In: London on August 30, 2026.",
        sameAs=["https://en.wikipedia.org/wiki/Jon_Moxley",
                "https://www.allelitewrestling.com/aew-roster"],
    ),
)
