# -*- coding: utf-8 -*-
"""Kenny Omega - dossier data.

Sources: web research compiled August 31, 2026, the day after Omega lost the AEW World
Championship to Will Ospreay at All In: London. Dates verified against AEW.com's own
championship history page, Wikipedia's title tables, and event coverage from POST
Wrestling, Fightful, Wrestling Inc and Bleacher Report. Nothing is invented.

Deliberate omissions:
  * No career win-loss total - none verified.
  * No social links - handles not verified in this pass.
  * AAA Mega Championship reign endpoints are given at month precision only; the exact
    end of that reign was not verified and no day-precision date is fabricated for it.
  * No theme entry - no Spotify URL was verified.
"""

# ----------------------------------------------------------------- record rows
# Seventeen documented bouts - the Okada series, both AEW World reigns at both ends,
# and the 2026 run. A curated ledger, not a career count.
ROWS = [
    dict(result="W", date="2016-08-14", promo="NJPW", landmark=True,
         event="G1 Climax 26 final", opponent="Hirooki Goto",
         stip="Tournament final — first non-Japanese G1 winner", title=""),
    dict(result="L", date="2017-01-04", promo="NJPW", landmark=True,
         event="Wrestle Kingdom 11", opponent="Kazuchika Okada", opponent_html=True,
         stip="Singles — 6 stars (Meltzer), the rating scale breaks",
         title="IWGP Heavyweight Championship"),
    dict(result="D", date="2017-06-11", promo="NJPW",
         event="Dominion", opponent="Kazuchika Okada", opponent_html=True,
         stip="60-minute time-limit draw — 6.25 stars", title="IWGP Heavyweight Championship"),
    dict(result="W", date="2018-06-09", promo="NJPW", landmark=True,
         event="Dominion", opponent="Kazuchika Okada", opponent_html=True,
         stip="Two of three falls, no time limit — Meltzer's first 7-star match; ends the "
              "720-day reign",
         title="IWGP Heavyweight Championship"),
    dict(result="L", date="2019-01-04", promo="NJPW",
         event="Wrestle Kingdom 13", opponent="Hiroshi Tanahashi",
         stip="Singles — the reign and the NJPW run end", title="IWGP Heavyweight Championship"),
    dict(result="L", date="2019-11-09", promo="AEW",
         event="Full Gear", opponent="Jon Moxley", opponent_html=True,
         stip="Unsanctioned Lights Out match", title=""),
    dict(result="W", date="2020-12-02", promo="AEW", landmark=True,
         event="Dynamite: Winter Is Coming", opponent="Jon Moxley", opponent_html=True,
         stip="Singles — first reign begins", title="AEW World Championship"),
    dict(result="L", date="2021-11-13", promo="AEW", landmark=True,
         event="Full Gear", opponent="Hangman Adam Page",
         stip="Singles — the 346-day reign ends", title="AEW World Championship"),
    dict(result="W", date="2023-01-04", promo="NJPW", landmark=True,
         event="Wrestle Kingdom 17", opponent="Will Ospreay", opponent_html=True,
         stip="Singles — 6.25 stars", title="IWGP United States Championship"),
    dict(result="L", date="2023-06-25", promo="AEW",
         event="Forbidden Door", opponent="Will Ospreay", opponent_html=True,
         stip="Singles — Ospreay regains", title="IWGP United States Championship"),
    dict(result="W", date="2025-01-05", promo="NJPW", landmark=True,
         event="Wrestle Dynasty — Tokyo Dome", opponent="Gabe Kidd",
         stip="Singles — first match back from diverticulitis", title=""),
    dict(result="W", date="2025-03-09", promo="AEW", landmark=True,
         event="Revolution", opponent="Konosuke Takeshita",
         stip="Singles — becomes AEW's first Grand Slam champion",
         title="AEW International Championship"),
    dict(result="L", date="2025-07-12", promo="AEW", landmark=True,
         event="All In: Texas", opponent="Kazuchika Okada", opponent_html=True,
         stip="Winner-takes-all unification — Okada becomes first Unified Champion",
         title="AEW International Championship"),
    dict(result="L", date="2026-04-12", promo="AEW",
         event="Dynasty", opponent="MJF", opponent_html=True,
         stip="Singles — near 40 minutes; MJF retains with the Dynamite Diamond Ring",
         title="AEW World Championship"),
    dict(result="W", date="2026-07-08", promo="AEW", landmark=True,
         event="Dynamite: Beach Break", opponent="MJF", opponent_html=True,
         stip="Singles — second reign begins; Ospreay strips MJF's ring",
         title="AEW World Championship"),
    dict(result="W", date="2026-07-26", promo="AEW",
         event="Redemption", opponent="Kevin Knight",
         stip="Singles — retains", title="AEW World Championship"),
    dict(result="L", date="2026-08-30", promo="AEW", landmark=True,
         event="All In: London — Wembley", opponent="Will Ospreay", opponent_html=True,
         stip="Singles — the 53-day second reign ends", title="AEW World Championship"),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Kazuchika Okada": "kazuchika-okada", "Jon Moxley": "jon-moxley",
                 "Will Ospreay": "will-ospreay", "MJF": "mjf"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="kenny-omega",
    name="Kenny Omega",
    realname="Tyson Smith",
    epithet="The Best Bout Machine",
    hook="Record & Titles",

    meta_desc=("Kenny Omega is a two-time AEW World Champion who lost the title to Will Ospreay at "
               "All In: London on August 30, 2026, and the man in Dave Meltzer's first 7-star "
               "match. Full record, titles, factions, records and career."),
    og_desc=("The Best Bout Machine: two AEW World Championship reigns, the first 7-star match, "
             "the 2016 G1 Climax, and world titles in four companies."),
    tw_desc="The Best Bout Machine: 2x AEW World Champion, the first 7-star match, the 2016 G1.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2000",
    height_imp="6&#8242;0&#8243;",
    weight_lb="229",
    world_titles="2",
    vitals_tagline="Goodbye and good night",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="KO", title="AEW Shop", sub="Official tees · Shop AEW",
             tag="Shop", href="https://shop.aew.com/"),
        dict(ic="AEW", title="AEW Roster Profile", sub="AllEliteWrestling.com", tag="Visit",
             href="https://www.allelitewrestling.com/aew-roster"),
        dict(ic="NJ", title="NJPW", sub="The Golden Lovers years · NJPW1972.com",
             tag="Visit", href="https://www.njpw1972.com/"),
        dict(ic="W", title="Wikipedia", sub="Full biography", tag="Read", charity=True,
             href="https://en.wikipedia.org/wiki/Kenny_Omega"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Cleaner &middot; The Best Bout Machine &middot; The Belt Collector",
    hero_tag="Winnipeg, Manitoba &middot; <em>DDT &middot; NJPW &middot; AEW &middot; "
             "2000&ndash;present</em>",
    now_label="NOW",
    now_bold="No championship — lost the AEW World title at All In: London",
    now_tail=" &middot; the 53-day second reign ended against Will Ospreay on August 30, 2026; "
             "Omega handed him the belt afterward",
    hstats=[
        dict(value="2",   x=True,  label="AEW World Titles"),
        dict(value="7",   x=False, label="Star Match (Meltzer)"),
        dict(value="1st", x=False, label="Non-Japanese G1 Winner"),
        dict(value="4",   x=False, label="Companies, World Titles"),
    ],
    ghost_link="From Winnipeg basements to the first 7-star match",
    vlabel="Est. 2000 &middot; Winnipeg, Manitoba",
    mono="KO",

    # ---------------------------------------------------------------- 01 overview
    correction=2,
    overview=[
        "<b>Kenny Omega</b> spent 53 days of 2026 as AEW World Champion, and lost the title in the "
        "main event of All In: London at Wembley Stadium on August 30, 2026, to Will Ospreay &mdash; "
        "a 34-minute match after which Omega embraced the winner and handed him the belt. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">2</span>'
        '<span class="pull-cap">AEW World Championship reigns &mdash; 346 days in 2020&ndash;21, and 53 days in 2026</span></span>'
        "It was his second reign: he beat MJF on the Beach Break edition of Dynamite on July 8, 2026, "
        "five and a half years after winning his first from Jon Moxley at Winter Is Coming on "
        "December 2, 2020. Between the two reigns sit an executive title, a near career-ending "
        "illness, and the argument &mdash; which he has done more than almost anyone alive to earn "
        "&mdash; that he is the best in-ring performer of his generation.",

        "The case rests on Japan. He won the 2016 G1 Climax as the first non-Japanese winner in the "
        "tournament&rsquo;s history, and his series with Kazuchika Okada rewrote the sport&rsquo;s "
        "critical vocabulary: 6 stars from Dave Meltzer at Wrestle Kingdom 11 on January 4, 2017 "
        "&mdash; the first time the Observer&rsquo;s scale had been broken in decades &mdash; 6.25 "
        "for the 60-minute draw at Dominion that June, and then, on June 9, 2018, the first "
        "<b>7-star</b> match ever awarded, when Omega finally beat Okada in a two-of-three-falls, "
        "no-time-limit Dominion main event to win the IWGP Heavyweight Championship and end a "
        "720-day reign. He held that title 209 days, until Hiroshi Tanahashi beat him at Wrestle "
        "Kingdom 13 on January 4, 2019, and left for AEW that month as one of its founders and "
        "executive vice presidents.",

        "One correction, because the line gets repeated as gospel: <i>nobody kicks out of the "
        "One-Winged Angel</i>. Per Wikipedia&rsquo;s own accounting, two men have &mdash; Kota "
        "Ibushi, and MJF, in the near-40-minute Dynasty match of April 12, 2026 that Omega lost when "
        "MJF used the Dynamite Diamond Ring. The move&rsquo;s protection is real; the absolutism is "
        "not. The same precision applies to the belt-collector era: in 2021 he held the AEW, Impact "
        "and AAA world titles simultaneously, but the TNT and trios belts often added to that list "
        "in retellings came at other times or not at all.",

        "The 2026 reign was short and strange. Omega had returned from diverticulitis &mdash; the "
        "illness that took him out from December 2023 and, by his own telling, nearly killed him "
        "&mdash; at Wrestle Dynasty in the Tokyo Dome on January 5, 2025, beating Gabe Kidd, then "
        "took the International Championship from Konosuke Takeshita at Revolution on March 9, 2025 "
        "to become AEW&rsquo;s first Grand Slam champion. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">7</span>'
        '<span class="pull-cap">stars, Dominion, June 9, 2018 &mdash; the first rating of its size Dave Meltzer ever gave</span></span>'
        "He lost that belt to Okada in the winner-takes-all unification at All In: Texas on July 12, "
        "2025, reunited with the Young Bucks at Full Gear that November, failed against MJF at "
        "Dynasty in April 2026, then won the title at Beach Break on July 8 after Will Ospreay "
        "&mdash; then a Death Rider &mdash; stripped MJF of the Dynamite Diamond Ring. Ospreay "
        "refused his faction&rsquo;s order to suffocate Omega with a plastic bag at Redemption on "
        "July 26, quit the group, and beat Omega cleanly at Wembley five weeks later. Omega, 42, "
        "walked back up the ramp with Matt Jackson.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["AEW", "NJPW"],
        promo_labels={"AEW": "AEW", "NJPW": "NJPW"},
        stats=[
            ("2&times;", "AEW World Champion"),
            ("7",    "Stars, Dominion 2018"),
            ("346",  "Day first AEW reign"),
            ("53",   "Day second AEW reign"),
            ("1",    "G1 Climax (2016)"),
            ("209",  "Day IWGP reign"),
        ],
        lead=("Seventeen documented bouts &mdash; the Okada quadrilogy, both AEW World reigns at "
              "both ends, the Ospreay series and the comeback. This is a curated ledger, not a "
              "career count, and no career win&ndash;loss total is published because none could be "
              "verified. AEW title dates match AEW.com's own championship history page. Filter by "
              "match type, tap any column header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the reputation was built on, with Dave Meltzer's ratings as widely "
                    "published — reported here rather than re-verified against Observer archives."),
    signature=[
        dict(rating="7.0", event="Dominion 2018 — Osaka-jo Hall", opponent="Kazuchika Okada",
             stip="IWGP Heavyweight Championship, 2/3 falls — the first 7-star match ever given"),
        dict(rating="6.25", event="Wrestle Kingdom 17", opponent="Will Ospreay",
             stip="IWGP United States Championship — ESPN's 2023 match of the year series opener"),
        dict(rating="6.0", event="Wrestle Kingdom 11", opponent="Kazuchika Okada",
             stip="IWGP Heavyweight Championship — the night the 5-star scale broke"),
    ],
    signature_count_word="three",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("2&times;", "AEW World reigns"),
            ("1",   "IWGP Heavyweight reign"),
            ("4",   "Companies with world titles"),
            ("1st", "AEW Grand Slam champion"),
        ],
        lead=("World championships in AEW, NJPW, Impact and AAA, and AEW's first Triple Crown and "
              "first Grand Slam. Reign dates below are the verified ones; where only month "
              "precision was verified, only month precision is printed."),
        rows=[
            dict(ic="A", name="AEW World Championship", count="2",
                 sub="December 2, 2020 &ndash; November 13, 2021 &middot; def. Jon Moxley at Winter "
                     "Is Coming, lost to Hangman Page at Full Gear &mdash; <b>346 days</b> &middot; "
                     "July 8 &ndash; August 30, 2026 &middot; def. MJF at Beach Break, lost to Will "
                     "Ospreay at All In: London &mdash; 53 days"),
            dict(ic="I", name="AEW International Championship", count="1",
                 sub="March 9 &ndash; July 12, 2025 &middot; def. Konosuke Takeshita at Revolution "
                     "&mdash; the win that made him AEW&rsquo;s first Grand Slam champion &middot; "
                     "lost to Kazuchika Okada in the All In: Texas unification match, 125 days"),
            dict(ic="H", name="IWGP Heavyweight Championship", count="1",
                 sub="June 9, 2018 &ndash; January 4, 2019 &middot; def. Kazuchika Okada at Dominion "
                     "in the first 7-star match, lost to Hiroshi Tanahashi at Wrestle Kingdom 13"),
            dict(ic="U", name="IWGP United States Championship", count="2",
                 sub="Inaugural champion, 2017 &middot; regained at Wrestle Kingdom 17 on January 4, "
                     "2023 by beating Will Ospreay, lost it back at Forbidden Door on June 25, 2023"),
            dict(ic="J", name="IWGP Junior Heavyweight Championship", count="2",
                 sub="2014&ndash;2015, both reigns traded with the KUSHIDA era juniors division"),
            dict(ic="T", name="AEW World Tag Team Championship", count="1",
                 sub="2020&ndash;21 with Hangman Adam Page &mdash; the partnership whose breakup "
                     "built the Full Gear 2021 main event"),
            dict(ic="3", name="AEW World Trios Championship", count="2",
                 sub="With the Young Bucks as The Elite, including the inaugural reign in 2022"),
            dict(ic="X", name="Impact World Championship", count="1",
                 sub="April 25 &ndash; August 13, 2021 &middot; def. Rich Swann in a winner-takes-all "
                     "at Rebellion, lost to Christian Cage on Rampage&rsquo;s premiere"),
            dict(ic="M", name="AAA Mega Championship", count="1",
                 sub="Won October 2019 from Rey Fenix &middot; a multi-year reign through the "
                     "pandemic era; the exact end date was not verified in this pass and is not "
                     "guessed at here"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Three units, and every one of them changed the business.",
        cards=[
            dict(era="NJPW &middot; 2016&ndash;2018",
                 name="Bullet Club — The Elite era",
                 members="Kenny Omega (leader), The Young Bucks, Cody Rhodes, Marty Scurll, "
                         "Hangman Page, others",
                 desc="Omega took over Bullet Club leadership from AJ Styles in 2016 and, with the "
                      "Young Bucks, spun The Elite out of it — the t-shirt empire, Being The Elite, "
                      "and eventually the civil war with Cody Rhodes. The faction politics of "
                      "2016-2018 are the direct prehistory of AEW."),
            dict(era="DDT &amp; NJPW &middot; 2008&ndash;present",
                 name="Golden Lovers",
                 members="Kenny Omega &amp; Kota Ibushi",
                 desc="The tag team with Kota Ibushi, formed in DDT and portrayed with open romantic "
                      "overtones — decades ahead of the industry on that front. Their 2018 reunion, "
                      "after Omega's lowest Bullet Club moment, remains one of wrestling's most "
                      "replayed angles. Ibushi is one of only two men to kick out of the One-Winged "
                      "Angel."),
            dict(era="AEW &middot; 2019&ndash;present",
                 name="The Elite",
                 members="Kenny Omega, Matt &amp; Nick Jackson, at times Hangman Page, Kazuchika "
                         "Okada",
                 desc="Founders and EVPs of AEW itself. The Bucks turned on Omega in 2024 while he "
                      "was out sick; the reunion came at Full Gear on November 22, 2025, and Matt "
                      "Jackson walked him up the ramp after the Wembley loss on August 30, 2026. "
                      "Whatever the on-screen alignment, the off-screen fact stands: Omega is an "
                      "executive vice president of the company he wrestles for."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="The gimmick has always been the same man at different volumes: <b>the Cleaner</b> "
             "&rarr; <b>the Best Bout Machine</b> &rarr; <b>the Belt Collector</b> &rarr; the "
             "comeback. The name itself is borrowed from Final Fantasy&rsquo;s Omega Weapon.",
        cards=[
            dict(mono="DDT", era="DDT &amp; indies &middot; 2000&ndash;2014", name="The Winnipeg gamer",
                 desc="Debuted in 2000 at sixteen in Manitoba, made his name in Japan's DDT — where "
                      "comedy, invisible opponents and a nine-year-old girl were all opponents — and "
                      "built the video-game-native persona that still frames everything: Undertale's "
                      "Toby Fox later wrote him an entrance theme."),
            dict(mono="CL", era="NJPW &middot; 2014&ndash;2018", name="The Cleaner",
                 desc="The Bullet Club heavy — broom on the entrance, finger guns, the takeover of "
                      "the club's leadership in 2016, the G1 win that year, and the Okada series "
                      "that turned him into the critics' consensus best wrestler alive."),
            dict(mono="BC", era="AEW &middot; 2020&ndash;2022", name="The Belt Collector",
                 desc="The heel champion era with Don Callis: AEW, Impact and AAA world titles held "
                      "at once in 2021, defended across four promotions, ended by Hangman Page at "
                      "Full Gear 2021 and then by a body that was breaking down."),
            dict(mono="CB", era="AEW &middot; 2025&ndash;present", name="The comeback",
                 desc="Diverticulitis took him out in December 2023 and nearly ended more than the "
                      "career. The return arc — Tokyo Dome in January 2025, Grand Slam champion that "
                      "March, world champion again in July 2026 — ended at Wembley with the belt "
                      "handed over and an embrace, which read less like defeat than succession."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Winnipeg to the Tokyo Dome to Wembley, with the scale broken in between.",
        rows=[
            dict(year="2000", title="Debut at sixteen",
                 desc="First matches in Manitoba; a brief WWE developmental stint follows in the "
                      "mid-2000s before he walks away from it."),
            dict(year="2008", title="Japan, DDT and the Golden Lovers",
                 desc="Moves his career to Japan, forms the Golden Lovers with Kota Ibushi, and "
                      "becomes fluent in Japanese and in DDT's absurdism."),
            dict(year="2016", title="Bullet Club leader; first non-Japanese G1 winner",
                 desc="Takes over Bullet Club, then beats Hirooki Goto in the G1 Climax 26 final on "
                      "August 14 — the first non-Japanese winner ever."),
            dict(year="2017", title="The Okada series breaks the scale",
                 desc="6 stars at Wrestle Kingdom 11 on January 4; a 6.25-star, 60-minute draw at "
                      "Dominion on June 11."),
            dict(year="2018", title="IWGP Heavyweight Champion — the 7-star match",
                 desc="Beats Okada two falls to one at Dominion on June 9, ending the 720-day reign, "
                      "in the first match Dave Meltzer ever rated 7 stars."),
            dict(year="2019", title="Leaves for AEW",
                 desc="Loses the title to Tanahashi at Wrestle Kingdom 13 on January 4, then helps "
                      "found AEW as a wrestler and executive vice president."),
            dict(year="2020", title="AEW World Champion",
                 desc="Beats Jon Moxley at Winter Is Coming on December 2 and begins the 346-day "
                      "Belt Collector reign — AEW, Impact and AAA gold held at once in 2021."),
            dict(year="2021", title="The reign ends",
                 desc="Hangman Page beats him at Full Gear on November 13. Injuries pile up; the "
                      "long first hiatus follows."),
            dict(year="2023", title="The Ospreay series",
                 desc="Wins the IWGP US title from Will Ospreay at Wrestle Kingdom 17 on January 4 "
                      "(6.25 stars), loses it back at Forbidden Door on June 25 — ESPN's match of "
                      "the year territory, twice in six months."),
            dict(year="2024", title="Diverticulitis",
                 desc="The illness diagnosed in December 2023 keeps him out the entire year; the "
                      "Young Bucks write him out of The Elite on screen."),
            dict(year="2025", title="The comeback",
                 desc="Returns at Wrestle Dynasty on January 5, beats Takeshita for the "
                      "International Championship at Revolution on March 9 to become AEW's first "
                      "Grand Slam champion, loses the unification match to Okada at All In: Texas "
                      "on July 12, and reunites with the Young Bucks at Full Gear on November 22."),
            dict(year="2026", title="Champion again — for 53 days",
                 desc="Loses to MJF at Dynasty on April 12, beats him for the title at Beach Break "
                      "on July 8, retains over Kevin Knight at Redemption on July 26, and drops the "
                      "belt to Will Ospreay at All In: London on August 30, handing it to him "
                      "afterward."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Kazuchika Okada", slug="kazuchika-okada",
                 desc="The greatest rivalry of the modern era by critical consensus: 6 stars at "
                      "Wrestle Kingdom 11, a 60-minute 6.25-star draw at Dominion 2017, and the "
                      "first 7-star match at Dominion 2018, where Omega finally won the IWGP "
                      "Heavyweight Championship. Okada got the last word in AEW, beating him in the "
                      "All In: Texas unification match on July 12, 2025."),
            dict(name="Will Ospreay", slug="will-ospreay",
                 desc="Heir and executioner. They split their 2023 IWGP US title series — Omega at "
                      "Wrestle Kingdom 17, Ospreay at Forbidden Door — and in 2026 Ospreay refused "
                      "a Death Riders order to suffocate Omega at Redemption, quit the faction, and "
                      "then beat him for the AEW World Championship at Wembley on August 30. Omega "
                      "gave him the belt and an embrace on the way out."),
            dict(name="MJF", slug="mjf",
                 desc="The 2026 title rivalry: MJF survived a One-Winged Angel and retained with the "
                      "Dynamite Diamond Ring in a near-40-minute Dynasty match on April 12; Omega "
                      "took the title at Beach Break on July 8 after Ospreay stripped the ring away, "
                      "finishing with three V-Triggers and the One-Winged Angel."),
            dict(name="Jon Moxley", slug="jon-moxley",
                 desc="Moxley won the unsanctioned Lights Out match at Full Gear 2019 — the bout "
                      "that recalibrated how violent AEW was willing to be — and Omega answered "
                      "where it mattered, taking the AEW World Championship from him at Winter Is "
                      "Coming on December 2, 2020. In 2026 Moxley's faction targeted Omega's reign "
                      "until Ospreay broke ranks."),
            dict(name="Hangman Adam Page",
                 desc="Tag partner, estranged brother, conqueror: their team won AEW tag gold in "
                      "2020, the breakup fueled a year of storytelling, and Page ended Omega's "
                      "346-day title reign at Full Gear on November 13, 2021 in AEW's most complete "
                      "long-arc payoff."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="The most video-game-literate star in wrestling history, and it is all verifiable.",
        rows=[
            dict(when="2016&ndash;", title="Being The Elite", kind="Web series",
                 desc="The YouTube series with the Young Bucks whose storylines fed directly into "
                      "the founding of AEW."),
            dict(when="2019", title="Toby Fox collaboration", kind="Music",
                 desc="The Undertale creator wrote Omega an entrance theme, per Wikipedia — one of "
                      "several game-world crossovers, alongside the Final Fantasy-derived ring name "
                      "and the Street Fighter-styled offense (the Hadouken is a real spot)."),
            dict(when="2019&ndash;", title="AEW executive vice president", kind="Executive",
                 desc="A founding EVP of AEW, involved in creative and in the company's games. His "
                      "in-ring and back-office roles have coexisted, uneasily at times, since 2019."),
            dict(when="2020", title="Wrestling Observer Hall of Fame", kind="Honor",
                 desc="Inducted while still an active wrestler. Also Sports Illustrated's 2017 "
                      "Wrestler of the Year and PWI's number one in 2018 and 2021, per Wikipedia."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated the way the sources actually state them.",
        stats=[
            ("7",    "Stars — a first"),
            ("2&times;", "AEW World Champion"),
            ("1st",  "Non-Japanese G1 winner"),
        ],
        rows=[
            dict(name="The first 7-star match",
                 sub="Dominion, June 9, 2018, vs. Kazuchika Okada — two of three falls, no time "
                     "limit, the IWGP Heavyweight Championship won, the 720-day reign ended, and "
                     "the first rating of its size Dave Meltzer ever gave."),
            dict(name="First non-Japanese G1 Climax winner",
                 sub="Beat Hirooki Goto in the final on August 14, 2016 — 26 tournaments in before "
                     "a gaijin won one."),
            dict(name="Two-time AEW World Champion",
                 sub="346 days (December 2, 2020 to November 13, 2021) and 53 days (July 8 to "
                     "August 30, 2026). Both reign lengths are computed from verified endpoints."),
            dict(name="AEW's first Triple Crown and first Grand Slam champion",
                 sub="World, tag and trios titles made him the inaugural Triple Crown holder in "
                     "2022; the International Championship win over Takeshita at Revolution on "
                     "March 9, 2025 completed the first Grand Slam, per Wikipedia and AEW's own "
                     "coverage."),
            dict(name="World titles in four companies",
                 sub="AEW, NJPW (IWGP Heavyweight), Impact and AAA — with the AEW, Impact and AAA "
                     "belts held simultaneously during 2021's Belt Collector run."),
            dict(name="Inaugural IWGP United States Champion",
                 sub="Won the 2017 tournament; regained the title at 39 by beating Will Ospreay at "
                     "Wrestle Kingdom 17 on January 4, 2023, at 6.25 stars."),
            dict(name="The One-Winged Angel ledger",
                 sub="Two verified kickouts ever, per Wikipedia: Kota Ibushi, and MJF at Dynasty on "
                     "April 12, 2026. Every other attempt on record has ended the match."),
            dict(name="The comeback from diverticulitis",
                 sub="Out from December 2023; returned January 5, 2025 at Wrestle Dynasty in the "
                     "Tokyo Dome and won a world title eighteen months later at 42."),
        ],
        footnote=("Deliberately absent: a career win-loss total (none verified), social handles "
                  "(not verified), and a day-precision end date for the AAA Mega Championship "
                  "reign, which the sources consulted did not settle. Star ratings are reported as "
                  "published, not re-audited."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Fightful", v="All In: London 2026 full results",
             href="https://www.fightful.com/wrestling/aew-all-in-results-8-30-2026-kenny-omega-vs-will-ospreay-willow-nightingale-vs-mercedes-mone-more/"),
        dict(k="AEW", v="Dynamite: Beach Break results — Omega beats MJF for the title",
             href="https://www.allelitewrestling.com/post/aew-dynamite-beach-break-results-july-8-2026"),
        dict(k="Wikipedia", v="Full biography",
             href="https://en.wikipedia.org/wiki/Kenny_Omega"),
        dict(k="AEW", v="International Championship history",
             href="https://www.allelitewrestling.com/aew-international-championship-history"),
        dict(k="POST Wrestling", v="All In: London 2026 — Ospreay takes the title",
             href="https://www.postwrestling.com/2026/08/30/aew-all-in-london-2026-results-will-ospreay-takes-aew-world-title-off-rival-kenny-omega-at-wembley-stadium/"),
        dict(k="Fightful", v="Redemption 2026 — the plastic-bag refusal",
             href="https://www.fightful.com/wrestling/will-ospreay-refuses-to-suffocate-kenny-omega-fights-off-death-riders-omega-hits-ospreay-with-one-winged-angel-at-aew-redemption/"),
        dict(k="Wikipedia", v="List of AEW World Champions",
             href="https://en.wikipedia.org/wiki/List_of_AEW_World_Champions"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Kenny Omega still AEW World Champion?",
            a="No. He lost the title to Will Ospreay in the main event of All In: London at Wembley "
              "Stadium on <b>August 30, 2026</b>, ending a 53-day second reign that began when he "
              "beat MJF at Dynamite: Beach Break on July 8, 2026. He embraced Ospreay afterward and "
              "handed him the belt. His first reign ran 346 days, from December 2, 2020 to November "
              "13, 2021.",
            q_ld="Is Kenny Omega still the AEW World Champion?",
            a_ld="No. Kenny Omega lost the AEW World Championship to Will Ospreay in the main event "
                 "of AEW All In: London at Wembley Stadium on August 30, 2026. His second reign "
                 "lasted 53 days, having begun on July 8, 2026 when he defeated MJF on the Beach "
                 "Break edition of Dynamite. His first reign ran 346 days from December 2, 2020 to "
                 "November 13, 2021."),
        dict(
            q="What is the 7-star match?",
            a="Omega vs. Kazuchika Okada at Dominion on June 9, 2018 &mdash; two of three falls, no "
              "time limit, for the IWGP Heavyweight Championship. Dave Meltzer of the Wrestling "
              "Observer, whose scale had topped out at 5 stars for decades, rated it <b>7</b>, the "
              "first rating of its size ever given. Omega won, ending Okada&rsquo;s record 720-day "
              "reign. The same series had already produced 6 stars at Wrestle Kingdom 11 and 6.25 "
              "for the 60-minute Dominion 2017 draw.",
            q_ld="What is Kenny Omega's 7-star match?",
            a_ld="Kenny Omega versus Kazuchika Okada at NJPW Dominion on June 9, 2018, a "
                 "two-out-of-three-falls match with no time limit for the IWGP Heavyweight "
                 "Championship. Dave Meltzer of the Wrestling Observer Newsletter rated it 7 stars, "
                 "the first rating of that size he had ever given. Omega won the match and the "
                 "title, ending Okada's record 720-day reign."),
        dict(
            q="Has anyone kicked out of the One-Winged Angel?",
            a="Two men, per Wikipedia&rsquo;s accounting: <b>Kota Ibushi</b>, and <b>MJF</b>, who "
              "survived it during the near-40-minute AEW Dynasty match on April 12, 2026 before "
              "retaining his title with the Dynamite Diamond Ring. The &ldquo;nobody has ever "
              "kicked out&rdquo; line is repeated constantly and is wrong &mdash; but only just.",
            q_ld="Has anyone ever kicked out of Kenny Omega's One-Winged Angel?",
            a_ld="Yes, two wrestlers have kicked out of the One-Winged Angel according to "
                 "Wikipedia: Kota Ibushi, and MJF, who survived the move at AEW Dynasty on April "
                 "12, 2026 before retaining the AEW World Championship against Omega with the "
                 "Dynamite Diamond Ring."),
        dict(
            q="Why was Omega out of action in 2024?",
            a="Diverticulitis, diagnosed in December 2023 &mdash; a serious intestinal condition "
              "he has said posed a genuine threat to his life, not just his career. He missed all "
              "of 2024, during which the Young Bucks wrote him out of The Elite on television. He "
              "returned at Wrestle Dynasty in the Tokyo Dome on January 5, 2025, beating Gabe "
              "Kidd, and won the International Championship nine weeks later.",
            q_ld="Why was Kenny Omega out of action during 2024?",
            a_ld="Kenny Omega was sidelined by diverticulitis, a serious intestinal condition "
                 "diagnosed in December 2023. He missed all of 2024 and returned on January 5, "
                 "2025 at the Wrestle Dynasty event in the Tokyo Dome, where he defeated Gabe "
                 "Kidd. He won the AEW International Championship at Revolution that March."),
        dict(
            q="What did Will Ospreay have to do with Omega's 2026 title win?",
            a="Everything. At Beach Break on July 8, 2026, Ospreay &mdash; then a member of the "
              "Death Riders &mdash; pulled the Dynamite Diamond Ring off MJF&rsquo;s hand before "
              "it could be used, and Omega won the title with three V-Triggers and a One-Winged "
              "Angel. Eighteen days later Ospreay refused Jon Moxley&rsquo;s order to suffocate "
              "Omega with a plastic bag at Redemption, left the faction, and on August 30 beat "
              "Omega for the championship at Wembley.",
            q_ld="What role did Will Ospreay play in Kenny Omega's 2026 AEW World Championship win?",
            a_ld="At Dynamite: Beach Break on July 8, 2026, Will Ospreay removed MJF's Dynamite "
                 "Diamond Ring during the match, preventing its use, and Kenny Omega won the AEW "
                 "World Championship with three V-Triggers and a One-Winged Angel. Ospreay later "
                 "refused an order from Jon Moxley to suffocate Omega at AEW Redemption on July 26, "
                 "left the Death Riders, and defeated Omega for the title at All In: London on "
                 "August 30, 2026."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Tyson Smith"),
        dict(label="Born", value="October 16, 1983", sub="Winnipeg, Manitoba &middot; age 42"),
        dict(label="Billed from", value="Winnipeg, Manitoba, Canada"),
        dict(label="Height", value="6&#8242;0&#8243;", sub="183 cm"),
        dict(label="Weight", value="229 lb", sub="104 kg (billed)"),
        dict(label="Debut", value="2000", sub="Manitoba, at sixteen"),
        dict(label="Residence", value="Japan ties",
             sub="Japanese citizen per Wikipedia; longtime Tokyo resident, fluent in Japanese"),
        dict(label="Signature", value="One-Winged Angel &middot; V-Trigger &middot; Snap Dragon "
                                      "suplex &middot; Terminator dive",
             sub="Two verified One-Winged Angel kickouts ever: Ibushi and MJF"),
        dict(label="Ring name origin", value="Final Fantasy&rsquo;s Omega Weapon",
             sub="The video-game identity is literal, down to a Toby Fox entrance theme"),
        dict(label="Role", value="Wrestler and AEW executive vice president", sub="Since 2019"),
        dict(label="Also known as",
             value="The Cleaner &middot; The Best Bout Machine &middot; The Belt Collector"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1983-10-16",
    bornplace="Winnipeg, Manitoba, Canada",
    nationality="Canada",
    height_cm=183,
    weight_kg=104,
    ld=dict(
        alternateName=["Tyson Smith", "The Cleaner", "The Best Bout Machine",
                       "The Belt Collector"],
        award=["AEW World Championship (2 reigns)",
               "IWGP Heavyweight Championship (1 reign)",
               "IWGP United States Championship (2 reigns, inaugural champion)",
               "IWGP Junior Heavyweight Championship (2 reigns)",
               "AEW International Championship (1 reign)",
               "AEW World Tag Team Championship (1 reign, with Hangman Page)",
               "AEW World Trios Championship (2 reigns, with The Young Bucks)",
               "Impact World Championship (1 reign)",
               "AAA Mega Championship (1 reign)",
               "G1 Climax winner (2016, first non-Japanese winner)",
               "First AEW Triple Crown and Grand Slam champion",
               "Wrestling Observer Newsletter Hall of Fame (2020)"],
        knowsAbout=["Professional wrestling", "New Japan Pro-Wrestling", "All Elite Wrestling",
                    "DDT Pro-Wrestling", "Bullet Club", "The Elite", "Video games"],
        description="Kenny Omega, born Tyson Smith in Winnipeg, is a Canadian professional "
                    "wrestler and AEW executive vice president. A two-time AEW World Champion, he "
                    "lost the title to Will Ospreay at All In: London on August 30, 2026 after a "
                    "53-day second reign. He won the 2016 G1 Climax as its first non-Japanese "
                    "winner and beat Kazuchika Okada at Dominion 2018 in the first match Dave "
                    "Meltzer ever rated 7 stars.",
        sameAs=["https://en.wikipedia.org/wiki/Kenny_Omega",
                "https://www.allelitewrestling.com/aew-roster"],
    ),
)
