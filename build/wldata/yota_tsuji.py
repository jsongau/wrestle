# -*- coding: utf-8 -*-
"""Yota Tsuji - dossier data.

Built from data/yota-tsuji.md (compiled November 9, 2026). Every fact there carries
a URL; this module adds no fact that is not in the .md. Sources include PostWrestling,
Fightful, Wrestling Inc, PWTorch, Cultaholic, F4W, Sports Illustrated, Daily Sports
(daily.co.jp, Japanese) and Japanese and English Wikipedia. The old thin page was
harvested and every claim re-checked; its "reinstated January 6" line is half right
(revealed January 5, made official January 6) and it ignored the April to June 2026
gap when Callum Newman held the title.

Slot 5 is "factions", not "before": the generator's "before" heading reads "Before
WWE", which is wrong for a wrestler who has never worked for WWE.

Deliberate omissions:
  * No Signature section. No star rating for any Tsuji match was verified, and the
    research rule is never to invent one.
  * No walk-out band. His entrance theme could not be verified.
  * No social handles. Not verified.
  * No career win-loss total. Cagematch is JavaScript-gated; the record total is the
    honest row count.
  * The November 7, 2026 MLW match with Trevor Lee is mentioned but not listed as a
    row: no result was found at compile time.
  * Height and weight are billed figures from Wikipedia only; NJPW's profile page is
    JavaScript-gated and returned nothing.
"""

def _omega(name="Kenny Omega"):
    return '<a class="opp-link" href="/wrestlers/kenny-omega/">%s</a>' % name

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="L", date="2018-04-10", promo="NJPW", landmark=True,
         event="Lion's Gate Project 11, Shinjuku FACE", opponent="Tomoyuki Oka",
         stip="Singles, in-ring debut; Oka (later Great-O-Khan) wins with a Boston crab",
         title=""),
    dict(result="L", date="2021-08-01", promo="NJPW",
         event="Summer Struggle, Korakuen Hall", opponent="Tetsuya Naito",
         stip="Singles, the send-off match before his overseas excursion", title=""),
    dict(result="L", date="2023-06-04", promo="NJPW", landmark=True,
         event="Dominion 6.4, Osaka-jo Hall", opponent="Sanada",
         stip="Singles, a world title shot one month after returning from excursion",
         title="IWGP World Heavyweight Championship"),
    dict(result="W", date="2024-02-24", promo="NJPW",
         event="The New Beginning in Sapporo, Night 2", opponent="Yuya Uemura",
         stip="Hair vs. hair; Uemura's head is shaved", title=""),
    dict(result="W", date="2024-03-20", promo="NJPW", landmark=True,
         event="New Japan Cup 2024 final, Niigata", opponent="Hirooki Goto",
         stip="Tournament final; Goto kicks out of one Gene Blaster, a second ends it",
         title=""),
    dict(result="L", date="2024-04-06", promo="NJPW",
         event="Sakura Genesis, Ryogoku Kokugikan", opponent="Tetsuya Naito",
         stip="Singles, the New Japan Cup winner's title shot against his own L.I.J. leader",
         title="IWGP World Heavyweight Championship"),
    dict(result="W", date="2024-06-09", promo="NJPW", type="tag",
         event="Dominion 6.9, Osaka-jo Hall",
         opponent="Hiroshi Tanahashi, Boltin Oleg & Toru Yano",
         stip="Six-man tag with Bushi and Hiromu Takahashi; Tsuji pins Tanahashi",
         title="NEVER Openweight 6-Man Tag Team Championship"),
    dict(result="L", date="2024-08-18", promo="NJPW", landmark=True,
         event="G1 Climax 34 final, Ryogoku Kokugikan", opponent="Zack Sabre Jr.",
         stip="Tournament final, about 31 minutes; Sabre wins with the Clarky Cat",
         title=""),
    dict(result="L", date="2024-08-27", promo="IND",
         event="CMLL Martes de Glamour, Arena Coliseo Guadalajara", opponent="Gran Guerrero",
         stip="Singles title challenge; finish and exact date conflict across sources",
         title="CMLL World Heavyweight Championship"),
    dict(result="W", date="2025-01-04", promo="NJPW", landmark=True,
         event="Wrestle Kingdom 19, Tokyo Dome", opponent="David Finlay",
         stip="Singles; powerbomb, then the Gene Blaster. His first singles title",
         title="IWGP Global Heavyweight Championship"),
    dict(result="W", date="2025-01-05", promo="NJPW",
         event="Wrestle Dynasty, Tokyo Dome", opponent="Jack Perry",
         stip="Singles, first defense, the next night", title="IWGP Global Heavyweight Championship"),
    dict(result="L", date="2025-06-15", promo="NJPW",
         event="Dominion 6.15, Osaka-jo Hall", opponent="Gabe Kidd",
         stip="Singles; the first reign ends at 162 days and four defenses",
         title="IWGP Global Heavyweight Championship"),
    dict(result="L", date="2025-08-16", promo="NJPW",
         event="G1 Climax 35 semifinal, Ariake Arena", opponent="Evil",
         stip="Referee stoppage in the Darkness Scorpion after House of Torture interference",
         title=""),
    dict(result="W", date="2025-10-13", promo="NJPW", landmark=True,
         event="King of Pro-Wrestling, Ryogoku Kokugikan", opponent="Gabe Kidd",
         stip="Singles, Boston crab at 24:19; the War Dogs alliance follows in the ring",
         title="IWGP Global Heavyweight Championship"),
    dict(result="W", date="2025-11-02", promo="NJPW",
         event="Tanahashi Final Homecoming", opponent="Hiroshi Tanahashi",
         stip="Singles, a title defense against the retiring ace",
         title="IWGP Global Heavyweight Championship"),
    dict(result="W", date="2026-01-04", promo="NJPW", landmark=True,
         event="Wrestle Kingdom 20, Tokyo Dome", opponent="Konosuke Takeshita",
         stip="Winner-takes-all; Gene Blaster, then a Boston crab for the tap",
         title="IWGP World Heavyweight Championship"),
    dict(result="W", date="2026-02-11", promo="NJPW",
         event="The New Beginning in Osaka, EDION Arena", opponent="Jake Lee",
         stip="Singles, 23:40; first defense of the revived title",
         title="IWGP Heavyweight Championship"),
    dict(result="W", date="2026-02-27", promo="NJPW",
         event="The New Beginning USA, Trenton, New Jersey", opponent="Andrade El Idolo",
         stip="Singles, submission at 26:41", title="IWGP Global Heavyweight Championship"),
    dict(result="L", date="2026-04-04", promo="NJPW", landmark=True,
         event="Sakura Genesis, Ryogoku Kokugikan", opponent="Callum Newman",
         stip="Singles, 24:17; a low blow behind the referee's back sets up Make Way",
         title="IWGP Heavyweight Championship"),
    dict(result="L", date="2026-05-03", promo="NJPW",
         event="Wrestling Dontaku, Night 1, Fukuoka", opponent="Andrade El Idolo",
         stip="Rematch; the second reign ends at 202 days",
         title="IWGP Global Heavyweight Championship"),
    dict(result="W", date="2026-06-14", promo="NJPW", landmark=True,
         event="Dominion 6.14, Osaka-jo Hall", opponent="Callum Newman",
         stip="Singles, 24:32; two Gene Blasters, then a side suplex. Second reign begins",
         title="IWGP Heavyweight Championship"),
    dict(result="W", date="2026-07-11", promo="NJPW",
         event="G1 Climax 36, Night 1, Hoffman Estates, Illinois", opponent="Konosuke Takeshita",
         stip="A Block opener, won with the Gene Blaster", title=""),
    dict(result="L", date="2026-08-06", promo="NJPW",
         event="G1 Climax 36, Night 12", opponent="Boltin Oleg",
         stip="A Block match", title=""),
    dict(result="L", date="2026-08-15", promo="NJPW",
         event="G1 Climax 36 semifinal", opponent="Yuya Uemura",
         stip="Semifinal; Uemura pins the champion with the Dead Bolt suplex", title=""),
    dict(result="W", date="2026-09-27", promo="NJPW",
         event="Destruction in Kobe", opponent="Hirooki Goto",
         stip="Singles, first defense of the second reign", title="IWGP Heavyweight Championship"),
    dict(result="W", date="2026-10-12", promo="NJPW",
         event="King of Pro-Wrestling, Ryogoku Kokugikan", opponent="Ryohei Oiwa",
         stip="Singles, 35:10, against the G1 Climax 36 winner",
         title="IWGP Heavyweight Championship"),
    dict(result="L", date="2026-11-03", promo="NJPW", landmark=True, type="tag",
         event="Power Struggle, Hiroshima", opponent=_omega() + " &amp; Boltin Oleg",
         opponent_html=True,
         stip="Non-title three-way; Omega pins Tsuji and earns the Tokyo Dome title match",
         title=""),
]

DATA = dict(
    slug="yota-tsuji",
    art="yota-tsuji",
    name="Yota Tsuji",
    realname="Yota Tsuji",
    epithet="The Unbound Champion",
    hook="Record & Titles",

    meta_desc=("Yota Tsuji is the IWGP Heavyweight Champion, the man who revived the title in "
               "January 2026, and faces Kenny Omega at Wrestle Kingdom 21. Full record, titles, "
               "factions and career."),
    og_desc=("Young Lion, excursion, L.I.J., 2024 New Japan Cup winner, two IWGP Global reigns, "
             "and two IWGP Heavyweight reigns. Next: Kenny Omega at the Tokyo Dome on January 4, 2027."),
    tw_desc="Yota Tsuji: IWGP Heavyweight Champion, the title's reviver, and Kenny Omega's Wrestle Kingdom 21 opponent.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2018",
    height_imp="5&#8242;11&#8243;",
    weight_lb="227",
    world_titles="2",
    vitals_tagline="Not bound by anyone",
    support_note="Watch &middot; Read",
    sp_items=[
        dict(ic="NJ", title="NJPW", sub="Official site · NJPW1972.com", tag="Visit",
             href="https://www.njpw1972.com/"),
        dict(ic="NW", title="NJPW World", sub="Streaming archive", tag="Watch",
             href="https://njpwworld.com/"),
        dict(ic="W", title="Wikipedia", sub="Full biography", tag="Read", charity=True,
             href="https://en.wikipedia.org/wiki/Yota_Tsuji"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="IWGP Heavyweight Champion &middot; Unbound Co. &middot; 2024 New Japan Cup winner",
    hero_tag="Yokohama, Kanagawa, Japan &middot; <em>NJPW &middot; 2018&ndash;present</em>",
    now_label="NOW",
    now_bold="IWGP Heavyweight Champion, second reign",
    now_tail=(" &middot; won June 14, 2026 at Dominion &middot; defends against Kenny Omega in the "
              "Wrestle Kingdom 21 main event, January 4, 2027"),
    hstats=[
        dict(value="2",   x=True,  label="IWGP Heavyweight Reigns"),
        dict(value="2",   x=True,  label="IWGP Global Reigns"),
        dict(value="364", x=False, label="Days as Global Champion"),
        dict(value="1",   x=True,  label="New Japan Cup Win"),
    ],
    ghost_link="From a 2018 debut loss to the man who brought the old belt back",
    vlabel="Est. 2018 &middot; Yokohama, Kanagawa",
    mono="YT",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Yota Tsuji</b> is the IWGP Heavyweight Champion as of November 9, 2026, in his second "
        "reign. He took the title back from Callum Newman at Dominion in Osaka-jo Hall on June 14, "
        "2026, then defended it against Hirooki Goto in Kobe and against G1 Climax winner Ryohei "
        "Oiwa at Ryogoku on October 12. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig pull-fig--sm">Jan. 4, 2027</span>'
        '<span class="pull-cap">Tsuji vs. Kenny Omega closes Wrestle Kingdom 21 at the Tokyo Dome</span></span>'
        "Kenny Omega laid him out after that defense, pinned him in a non-title three-way at Power "
        "Struggle on November 3, and now gets the title match that closes Wrestle Kingdom 21 at the "
        "Tokyo Dome on January 4, 2027.",

        "Get the title history right, because the short version is wrong. Tsuji did not hold the "
        "IWGP Heavyweight Championship continuously from January 2026. He beat Konosuke Takeshita "
        "for the IWGP World Heavyweight Championship at Wrestle Kingdom 20 on January 4, 2026, in a "
        "winner-takes-all match that also put his IWGP Global title on the line. He revealed the "
        "revived Heavyweight belt at New Year Dash the next night, and NJPW made the revival official "
        "at a January 6 press conference, merging the World title lineage into it and naming him the "
        "87th champion. Callum Newman then beat him at Sakura Genesis on April 4, after 90 days. The "
        "current reign started June 14. That is two reigns, with a ten-week gap between them.",

        "The rise was fast once it started. He debuted on April 10, 2018 as a Young Lion and lost to "
        "Tomoyuki Oka, spent his excursion in the UK with RevPro and in Mexico with CMLL, and came "
        "home at Wrestling Dontaku on May 3, 2023 to attack Sanada and join Los Ingobernables de "
        "Japon. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">2024</span>'
        '<span class="pull-cap">New Japan Cup winner, then G1 Climax runner-up five months later</span></span>'
        "He won the 2024 New Japan Cup over Hirooki Goto, reached the G1 Climax final that August, "
        "and won his first singles title, the IWGP Global Heavyweight Championship, from David "
        "Finlay at Wrestle Kingdom 19 on January 4, 2025.",

        "When Tetsuya Naito left NJPW in May 2025 and L.I.J. ended, Tsuji kept its remnants together "
        "as the Unaffiliated. He regained the Global title from Gabe Kidd on October 13, 2025, and "
        "the War Dogs came to the ring to shake hands. On January 5, 2026 he announced that both "
        "groups would fight as one unit, Unbound Co. His stance as champion is NJPW first: the "
        "Heavyweight title is defended only in Japan, and he has said he wants an equal relationship "
        "with AEW.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["NJPW", "IND"],
        promo_labels={"NJPW": "NJPW", "IND": "CMLL"},
        stats=[
            ("2&times;", "IWGP Heavyweight"),
            ("2&times;", "IWGP Global"),
            ("202", "Day Global reign"),
            ("2024", "New Japan Cup"),
            ("3", "G1 semis or better"),
            ("1&times;", "NEVER 6-Man"),
        ],
        lead=("Twenty-seven documented bouts: the debut, the send-off, every IWGP title change he "
              "was part of, his tournament finals and semifinals, and the 2026 road to the Tokyo "
              "Dome. This is a selected ledger, not a career count, and no win&ndash;loss total is "
              "published because none could be verified. His November 7, 2026 MLW match with "
              "Trevor Lee is left out because no result was found. Filter by match type, tap any "
              "column header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("2&times;", "IWGP Heavyweight"),
            ("2&times;", "IWGP Global"),
            ("87th", "Heavyweight champion"),
            ("Final", "Intercontinental champion"),
        ],
        lead=("Four IWGP singles reigns across two belts in under two years, plus a trios title "
              "and the 2024 New Japan Cup. For three months in 2026 he held the top title and the "
              "Global title at the same time."),
        rows=[
            dict(ic="H", name="IWGP Heavyweight Championship", count="2",
                 sub="January 4 &ndash; April 4, 2026 (won as the IWGP World Heavyweight title from "
                     "Konosuke Takeshita at Wrestle Kingdom 20, revived as the Heavyweight title "
                     "January 5&ndash;6, lost to Callum Newman at Sakura Genesis after <b>90 days</b>) "
                     "&middot; June 14, 2026 &ndash; present (def. Newman at Dominion 6.14; "
                     "defenses vs. Hirooki Goto and Ryohei Oiwa)"),
            dict(ic="G", name="IWGP Global Heavyweight Championship", count="2",
                 sub="January 4 &ndash; June 15, 2025 (def. David Finlay at Wrestle Kingdom 19, lost "
                     "to Gabe Kidd at Dominion, <b>162 days</b>, four defenses) &middot; October 13, "
                     "2025 &ndash; May 3, 2026 (def. Kidd at King of Pro-Wrestling, lost to Andrade "
                     "El Idolo at Wrestling Dontaku, <b>202 days</b>)"),
            dict(ic="I", name="IWGP Intercontinental Championship", count="1",
                 sub="Recognized as the final champion when the World title was split back into "
                     "its parts in January 2026; he then retired the belt because it overlapped "
                     "with the Global title"),
            dict(ic="6", name="NEVER Openweight 6-Man Tag Team Championship", count="1",
                 sub="June 9, 2024 with Bushi and Hiromu Takahashi, def. Hiroshi Tanahashi, Boltin "
                     "Oleg and Toru Yano at Dominion; Tsuji pinned Tanahashi"),
            dict(ic="N", name="New Japan Cup", count="1",
                 sub="2024, def. Hirooki Goto in the final in Niigata on March 20"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Three units in three years, and he led the last two.",
        cards=[
            dict(era="NJPW &middot; 2023&ndash;2025",
                 name="Los Ingobernables de Japon",
                 members="Tetsuya Naito, Hiromu Takahashi, Shingo Takagi, Bushi, Titán, Tsuji",
                 desc="He returned from excursion on May 3, 2023 by attacking Sanada and Just 5 "
                      "Guys, and formally joined the unit that June. The stable ended in NJPW "
                      "after Naito and Bushi's final match on May 4, 2025. Tsuji joined the last "
                      "roll call under the name at Fantastica Mania Mexico on June 20, 2025."),
            dict(era="NJPW &middot; 2025",
                 name="The Unaffiliated",
                 members="The L.I.J. remnants, Tsuji among them",
                 desc="A loose alliance with no banner. After Tsuji regained the Global title from "
                      "Gabe Kidd on October 13, 2025, the Bullet Club War Dogs came out and shook "
                      "hands with the group in the ring."),
            dict(era="NJPW &middot; 2026&ndash;present",
                 name="Unbound Co.",
                 members="Tsuji, Shingo Takagi, Taiji Ishimori, Robbie X, Titán, Drilla Moloney, "
                         "Oskar, Yuto-Ice, Daiki Nagai, Jeff Cobb, Gedo (manager)",
                 desc="Tsuji announced it at New Year Dash on January 5, 2026, merging the War Dogs "
                      "and the Unaffiliated into one unit. Hiromu Takahashi, David Finlay and Clark "
                      "Connors left in early 2026, and Gabe Kidd left on April 4 by attacking Tsuji "
                      "after the Sakura Genesis loss."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead=("One name throughout, his own. Four phases: <b>Young Lion</b> (2018&ndash;2021), "
              "<b>excursion</b> (2021&ndash;2023), <b>L.I.J.&rsquo;s new era</b> (2023&ndash;2025), "
              "and <b>the Unbound champion</b> (2026&ndash;present)."),
        cards=[
            dict(mono="YL", era="NJPW &middot; 2018&ndash;2021", name="Young Lion",
                 desc="Debuted on April 10, 2018 and lost to Tomoyuki Oka. Wrestled the dojo "
                      "undercard for three years, then lost a send-off match to Tetsuya Naito at "
                      "Korakuen Hall on August 1, 2021."),
            dict(mono="EX", era="UK &amp; Mexico &middot; 2021&ndash;2023", name="The excursion",
                 desc="About 18 months mostly with RevPro in the UK, then CMLL in Mexico from late "
                      "2022, billed simply as Yota. He has said he dodged the LA Dojo on purpose, "
                      "because its graduates all wrestled like clones."),
            dict(mono="LJ", era="NJPW &middot; 2023&ndash;2025", name="The new era",
                 desc="Came home in May 2023 under the L.I.J. banner. After winning the 2024 New "
                      "Japan Cup he called himself the leader of the new era and pointed at his own "
                      "stable leader, Naito, for the title."),
            dict(mono="UB", era="NJPW &middot; 2026&ndash;present", name="The Unbound champion",
                 desc="Revived the old IWGP Heavyweight belt, retired the Intercontinental title, "
                      "and set the rule that the top title stays in Japan. Lost it once in 2026 and "
                      "won it back."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Shinjuku FACE in 2018 to the Tokyo Dome main event in 2027.",
        rows=[
            dict(year="2018", title="Debut",
                 desc="Loses to Tomoyuki Oka at Lion's Gate Project 11 at Shinjuku FACE on April 10."),
            dict(year="2021", title="Send-off and excursion",
                 desc="Loses to Tetsuya Naito at Korakuen Hall on August 1, then leaves for the UK, "
                      "where he works mostly for RevPro."),
            dict(year="2022", title="CMLL",
                 desc="Moves to Mexico late in the year and wrestles for CMLL as Yota."),
            dict(year="2023", title="Home, and straight into a title match",
                 desc="Returns at Wrestling Dontaku on May 3 by attacking Sanada and Just 5 Guys, "
                      "joins L.I.J., and loses to Sanada for the IWGP World Heavyweight title at "
                      "Dominion on June 4."),
            dict(year="2024", title="New Japan Cup winner, G1 finalist",
                 desc="Shaves Yuya Uemura's head in a hair match on February 24, wins the New Japan "
                      "Cup over Hirooki Goto on March 20, loses to Naito at Sakura Genesis on April "
                      "6, wins the NEVER 6-Man titles on June 9, and loses the G1 Climax final to "
                      "Zack Sabre Jr. on August 18."),
            dict(year="2025", title="First singles gold, twice",
                 desc="Beats David Finlay for the IWGP Global title at Wrestle Kingdom 19, loses it "
                      "to Gabe Kidd on June 15, reaches the G1 semifinals, regains it from Kidd on "
                      "October 13, and turns back Hiroshi Tanahashi on November 2."),
            dict(year="2026", title="Double champion, then the revival",
                 desc="Beats Konosuke Takeshita at Wrestle Kingdom 20, launches Unbound Co. and the "
                      "revived IWGP Heavyweight title, loses it to Callum Newman on April 4 and the "
                      "Global title to Andrade El Idolo on May 3, and wins the Heavyweight title "
                      "back from Newman on June 14."),
            dict(year="2026", title="The road to the Dome",
                 desc="Loses the G1 Climax 36 semifinal to Uemura on August 15, defends against "
                      "Goto and Ryohei Oiwa, and is pinned by Kenny Omega in a non-title three-way "
                      "at Power Struggle on November 3."),
            dict(year="2027", title="Wrestle Kingdom 21",
                 desc="Booked to defend against Kenny Omega in the Tokyo Dome main event on "
                      "January 4."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he has gone to war with.",
        cards=[
            dict(name="Gabe Kidd",
                 desc="Three IWGP Global title matches in 2025: a double knockout, Kidd's win at "
                      "Dominion on June 15, and Tsuji's Boston crab win at King of Pro-Wrestling on "
                      "October 13. They became stablemates in Unbound Co., until Kidd attacked "
                      "him after the April 4, 2026 title loss and left."),
            dict(name="Callum Newman",
                 desc="Took the IWGP Heavyweight title from him at Sakura Genesis on April 4, 2026 "
                      "with a low blow and Make Way. Tsuji took it back at Dominion on June 14."),
            dict(name="Konosuke Takeshita",
                 desc="Tsuji was his first NJPW opponent in 2023 and beat him in the 2024 G1 "
                      "playoffs. At Wrestle Kingdom 20 Tsuji made him tap in a winner-takes-all "
                      "match, and he beat him again on the first night of G1 Climax 36."),
            dict(name="Kenny Omega", slug="kenny-omega",
                 desc="Laid him out with the One Winged Angel after the October 12, 2026 defense, "
                      "pinned him in the Power Struggle three-way on November 3, and gets the "
                      "IWGP Heavyweight title match in the Wrestle Kingdom 21 main event."),
            dict(name="Tetsuya Naito",
                 desc="His send-off opponent in 2021 and his L.I.J. leader from 2023. Naito beat "
                      "him for the IWGP World Heavyweight title at Sakura Genesis on April 6, "
                      "2024, the night after Tsuji's New Japan Cup claim on the belt."),
            dict(name="Yuya Uemura",
                 desc="A fellow Young Lion. Tsuji shaved his head after the February 2024 hair "
                      "match. Uemura answered by beating the champion in the G1 Climax 36 "
                      "semifinal on August 15, 2026."),
            dict(name="Andrade El Idolo",
                 desc="Tsuji made him submit in Trenton on February 27, 2026. Andrade won the "
                      "rematch at Wrestling Dontaku on May 3 and ended the 202-day Global reign."),
            dict(name="Hirooki Goto",
                 desc="Lost the 2024 New Japan Cup final to Tsuji in a match Wikipedia records as "
                      "Tokyo Sports' Best Bout of 2024, and challenged him for the Heavyweight "
                      "title in Kobe on September 27, 2026."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Recognition",
        lead=("Short by design. No film, book or video-game credit could be verified, so none is "
              "listed."),
        rows=[
            dict(when="2023", title="ESPN: best wrestlers under 30", kind="List",
                 desc="Ranked No. 23 of 30, per Wikipedia's citation."),
            dict(when="2024", title="POST Wrestling interview", kind="Interview",
                 desc="Explained that he gave NJPW an excuse about his US visa to avoid the LA Dojo, "
                      "whose graduates he called clones of Katsuyori Shibata."),
            dict(when="2024", title="Tokyo Sports Best Bout", kind="Award",
                 desc="For the March 20, 2024 New Japan Cup final against Hirooki Goto, per Wikipedia."),
            dict(when="2025", title="The twin decoy", kind="Story",
                 desc="His identical twin Shota, a stuntman, appeared as a decoy during an April 5, "
                      "2025 match, per Wikipedia."),
            dict(when="2026", title="PWI 500", kind="List",
                 desc="Ranked No. 7, per Wikipedia's Unbound Co. article."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="What the record actually shows, stated the way the sources state it.",
        stats=[
            ("202", "Day Global reign"),
            ("90",  "Days, first Heavyweight reign"),
            ("364", "Days as Global champion"),
        ],
        rows=[
            dict(name="Revived the IWGP Heavyweight Championship",
                 sub="Revealed at New Year Dash on January 5, 2026 and made official on January 6. "
                     "The World Heavyweight lineage was folded into it and he was recognized as the "
                     "87th champion."),
            dict(name="The final IWGP Intercontinental Champion",
                 sub="The World title split back into the Heavyweight and Intercontinental belts. "
                     "He retired the Intercontinental title because it overlapped with the Global "
                     "title."),
            dict(name="IWGP Heavyweight and Global Champion at once",
                 sub="January 4 to April 4, 2026, after the Wrestle Kingdom 20 winner-takes-all "
                     "match with Konosuke Takeshita."),
            dict(name="Two IWGP Global reigns, 364 days in total",
                 sub="162 days in 2025 with four defenses, then 202 days from October 13, 2025 to "
                     "May 3, 2026."),
            dict(name="2024 New Japan Cup winner",
                 sub="Beat Jeff Cobb, El Phantasmo, Ren Narita, Evil and Hirooki Goto, per Wikipedia; "
                     "the final in Niigata on March 20."),
            dict(name="Three straight G1 Climax runs to the last four",
                 sub="Runner-up in 2024, semifinalist in 2025 and 2026."),
        ],
        footnote=("Deliberately absent: a career win-loss total, star ratings, social handles and an "
                  "entrance theme, none verified. Height and weight are billed figures from "
                  "Wikipedia."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Yota_Tsuji"),
        dict(k="Wikipedia (JA)", v="辻陽太", href="https://ja.wikipedia.org/wiki/辻陽太"),
        dict(k="Daily Sports", v="Oiwa defense and Omega's attack (Japanese)",
             href="https://www.daily.co.jp/ring/2026/10/13/0020921775.shtml"),
        dict(k="Wrestling Inc", v="Wrestle Kingdom 21: Tsuji vs. Omega announced",
             href="https://www.wrestlinginc.com/2305275/aew-njpw-wrestle-kingdom-21-kenny-omega-jon-moxley-will-ospreay-mjf-gabe-kidd-matches-announced/"),
        dict(k="Fightful", v="Omega pins Tsuji at Power Struggle 2026",
             href="https://www.fightful.com/?p=337176"),
        dict(k="POST Wrestling", v="Dominion 6.14: Tsuji regains the title",
             href="https://www.postwrestling.com/?p=136536"),
        dict(k="Cultaholic", v="NJPW officially reinstates the IWGP Heavyweight title",
             href="https://cultaholic.com/posts/njpw-officially-reinstates-the-iwgp-heavyweight-championship"),
        dict(k="Wrestling Inc", v="Wrestle Kingdom 20: Tsuji submits Takeshita",
             href="https://www.wrestlinginc.com/2067048/njpw-yota-tsuji-submits-aew-konosuke-takeshita-win-world-title-wrestle-kingdom-20"),
        dict(k="Wikipedia", v="Unbound Co.", href="https://en.wikipedia.org/wiki/Unbound_Co."),
        dict(k="NJPW", v="Official site", href="https://www.njpw1972.com/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Yota Tsuji a champion right now?",
            a="Yes. He is the <b>IWGP Heavyweight Champion</b> as of November 9, 2026, in his second "
              "reign. He won it back from Callum Newman at Dominion on June 14, 2026, and has "
              "defended it against Hirooki Goto and Ryohei Oiwa.",
            q_ld="Is Yota Tsuji currently a champion?",
            a_ld="Yes. Yota Tsuji is the IWGP Heavyweight Champion as of November 9, 2026. He began "
                 "his second reign by defeating Callum Newman at NJPW Dominion 6.14 on June 14, "
                 "2026, and has since defended the title against Hirooki Goto and Ryohei Oiwa."),
        dict(
            q="Who does Tsuji face at Wrestle Kingdom 21?",
            a="Kenny Omega, for the IWGP Heavyweight Championship, in the closing match at the Tokyo "
              "Dome on January 4, 2027. Omega earned it by pinning Tsuji in a non-title three-way "
              "with Boltin Oleg at Power Struggle on November 3, 2026.",
            q_ld="Who is Yota Tsuji facing at Wrestle Kingdom 21?",
            a_ld="Yota Tsuji defends the IWGP Heavyweight Championship against Kenny Omega in the "
                 "main event of NJPW Wrestle Kingdom 21 at the Tokyo Dome on January 4, 2027. Omega "
                 "earned the match by pinning Tsuji in a non-title three-way that included Boltin "
                 "Oleg at Power Struggle on November 3, 2026."),
        dict(
            q="Why did Tsuji bring back the IWGP Heavyweight Championship?",
            a="After winning the IWGP World Heavyweight title at Wrestle Kingdom 20, he split it "
              "back into its original parts. He revealed the old Heavyweight belt on January 5, "
              "2026, and NJPW made it official on January 6 with the World lineage merged in. He "
              "retired the Intercontinental half because it overlapped with the Global title, and "
              "ruled that the Heavyweight title is defended only in Japan.",
            q_ld="Why was the IWGP Heavyweight Championship revived in 2026?",
            a_ld="Yota Tsuji won the IWGP World Heavyweight Championship at Wrestle Kingdom 20 on "
                 "January 4, 2026 and split it back into the IWGP Heavyweight and Intercontinental "
                 "titles. He revealed the revived Heavyweight belt on January 5, NJPW made it "
                 "official on January 6 with the World title lineage merged into it, and Tsuji "
                 "retired the Intercontinental title because it overlapped with the IWGP Global "
                 "Heavyweight Championship."),
        dict(
            q="Has Tsuji held the title since January 2026?",
            a="No. Callum Newman beat him at Sakura Genesis on April 4, 2026, ending the first reign "
              "after 90 days. Tsuji regained the title on June 14, so he is a two-time champion.",
            q_ld="Has Yota Tsuji held the IWGP Heavyweight Championship continuously since January 2026?",
            a_ld="No. Yota Tsuji's first reign, which began at Wrestle Kingdom 20 on January 4, 2026, "
                 "ended when Callum Newman defeated him at Sakura Genesis on April 4, 2026. Tsuji "
                 "regained the IWGP Heavyweight Championship from Newman at Dominion 6.14 on June "
                 "14, 2026."),
        dict(
            q="How many times has Tsuji been IWGP Global Heavyweight Champion?",
            a="Twice. He beat David Finlay at Wrestle Kingdom 19 and held it 162 days until Gabe "
              "Kidd won it on June 15, 2025. He took it back from Kidd on October 13, 2025 and held "
              "it 202 days until Andrade El Idolo won it on May 3, 2026.",
            q_ld="How many times has Yota Tsuji held the IWGP Global Heavyweight Championship?",
            a_ld="Yota Tsuji has held the IWGP Global Heavyweight Championship twice: from January "
                 "4, 2025, when he defeated David Finlay at Wrestle Kingdom 19, to June 15, 2025 (162 "
                 "days), and from October 13, 2025, when he defeated Gabe Kidd, to May 3, 2026, when "
                 "Andrade El Idolo won the title (202 days)."),
        dict(
            q="Has Tsuji won the G1 Climax or the New Japan Cup?",
            a="He won the <b>2024 New Japan Cup</b>, beating Hirooki Goto in the final on March 20. "
              "He has not won the G1 Climax. He lost the 2024 final to Zack Sabre Jr. and lost in "
              "the semifinals in 2025 (to Evil) and 2026 (to Yuya Uemura).",
            q_ld="Has Yota Tsuji won the G1 Climax or the New Japan Cup?",
            a_ld="Yota Tsuji won the 2024 New Japan Cup, defeating Hirooki Goto in the final on March "
                 "20, 2024. He has not won the G1 Climax: he lost the 2024 final to Zack Sabre Jr. "
                 "and lost in the semifinals to Evil in 2025 and to Yuya Uemura in 2026."),
        dict(
            q="What is Unbound Co.?",
            a="The NJPW unit Tsuji announced on January 5, 2026, merging the Bullet Club War Dogs "
              "with the Unaffiliated, the remnants of Los Ingobernables de Japon. Shingo Takagi, "
              "Taiji Ishimori, Robbie X and the Knock Out Brothers are among its members.",
            q_ld="What is Unbound Co. in NJPW?",
            a_ld="Unbound Co. is a New Japan Pro-Wrestling stable announced by Yota Tsuji at New Year "
                 "Dash on January 5, 2026. It merged the Bullet Club War Dogs with the Unaffiliated, "
                 "the former members of Los Ingobernables de Japon, and includes Shingo Takagi, Taiji "
                 "Ishimori, Robbie X, Oskar and Yuto-Ice."),
        dict(
            q="Where did Tsuji go on excursion?",
            a="The UK first, mainly RevPro, for about 18 months from 2021. He moved to CMLL in "
              "Mexico in late 2022 and wrestled there as Yota before returning to NJPW on May 3, "
              "2023. He has said he avoided the LA Dojo on purpose.",
            q_ld="Where did Yota Tsuji go on his NJPW excursion?",
            a_ld="Yota Tsuji spent his excursion first in the United Kingdom, mainly with Revolution "
                 "Pro Wrestling, from 2021, then with CMLL in Mexico from late 2022, wrestling as "
                 "Yota. He returned to NJPW at Wrestling Dontaku on May 3, 2023."),
        dict(
            q="What is the Gene Blaster?",
            a="His spear, and the move that has won most of his biggest matches, including the "
              "Wrestle Kingdom 19 title win over David Finlay. He also finishes with a Boston crab, "
              "which made Konosuke Takeshita tap at Wrestle Kingdom 20.",
            q_ld="What is Yota Tsuji's finishing move?",
            a_ld="Yota Tsuji's finishing move is the Gene Blaster, a spear. He also wins with a Boston "
                 "crab, which he used to make Konosuke Takeshita submit at Wrestle Kingdom 20 on "
                 "January 4, 2026."),
        dict(
            q="When did Tsuji debut?",
            a="April 10, 2018, at Lion's Gate Project 11 at Shinjuku FACE in Tokyo. He lost to "
              "Tomoyuki Oka, now Great-O-Khan, by Boston crab.",
            q_ld="When did Yota Tsuji make his wrestling debut?",
            a_ld="Yota Tsuji debuted on April 10, 2018 at NJPW Lion's Gate Project 11 at Shinjuku FACE "
                 "in Tokyo, losing to Tomoyuki Oka, later known as Great-O-Khan."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Yota Tsuji", sub="辻陽太 &middot; ring name and legal name match"),
        dict(label="Born", value="September 8, 1993", sub="Yokohama, Kanagawa, Japan &middot; age 33"),
        dict(label="Height", value="5&#8242;11&#8243;", sub="182 cm, billed, per Wikipedia"),
        dict(label="Weight", value="227 lb", sub="103 kg, billed, per Wikipedia"),
        dict(label="Debut", value="April 10, 2018", sub="Lion's Gate Project 11, lost to Tomoyuki Oka"),
        dict(label="Trained at", value="NJPW Dojo", sub="Young Lion, 2018&ndash;2021"),
        dict(label="College", value="Nippon Sport Science University",
             sub="Played American football; also taekwondo and baseball"),
        dict(label="Signature", value="Gene Blaster &middot; Boston crab &middot; Curb Stomp"),
        dict(label="Current title", value="IWGP Heavyweight Championship",
             sub="Second reign, won June 14, 2026 at Dominion"),
        dict(label="Unit", value="Unbound Co. (2026&ndash;)",
             sub="Before: L.I.J. (2023&ndash;2025), the Unaffiliated (2025)"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1993-09-08",
    bornplace="Yokohama, Kanagawa, Japan",
    nationality="Japan",
    alumni="Nippon Sport Science University",
    height_cm=182,
    weight_kg=103,
    ld=dict(
        alternateName=["辻陽太", "Yota"],
        award=["IWGP Heavyweight Championship (2 reigns, current; 87th champion)",
               "IWGP Global Heavyweight Championship (2 reigns)",
               "IWGP Intercontinental Championship (final champion)",
               "NEVER Openweight 6-Man Tag Team Championship (1 reign)",
               "New Japan Cup winner (2024)"],
        knowsAbout=["Professional wrestling", "New Japan Pro-Wrestling",
                    "Los Ingobernables de Japon", "Unbound Co.", "CMLL"],
        description="Yota Tsuji is a Japanese professional wrestler with New Japan Pro-Wrestling and "
                    "the IWGP Heavyweight Champion as of November 2026. He revived the title in "
                    "January 2026, is a two-time IWGP Global Heavyweight Champion, won the 2024 New "
                    "Japan Cup, and defends against Kenny Omega at Wrestle Kingdom 21 on January 4, "
                    "2027.",
        sameAs=["https://en.wikipedia.org/wiki/Yota_Tsuji",
                "https://ja.wikipedia.org/wiki/%E8%BE%BB%E9%99%BD%E5%A4%AA"],
    ),
)
