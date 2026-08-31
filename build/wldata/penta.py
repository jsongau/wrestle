# -*- coding: utf-8 -*-
"""Penta - dossier data.

Sources: web research compiled August 31, 2026 - Wikipedia (Penta), WWE.com (official
profile, World Heavyweight Championship No. 1 Contender's Tournament article, Raw
previews), POST Wrestling (WrestleMania 42 ladder match, SummerSlam IC change),
Wrestling Inc. (Raw results, August 24, 2026), Cageside Seats (2025 Royal Rumble iron
man analysis), Newsweek (the November 2025 injury). Day-precision dates come from
those sources; several early lucha dates are Wikipedia's and are marked where the
record is thin.

Deliberate omissions and flags:
  * His real name is not published. It has never been publicly disclosed, in the lucha
    libre tradition - he has never been unmasked. The realname field says so rather
    than guessing.
  * No career win-loss total: nothing verified exists across five promotions.
  * No social links: handles could not be verified as official in this pass.
  * WWE.com's profile still lists him as Intercontinental Champion; he lost the title
    to Chad Gable at SummerSlam on August 2, 2026. The page flags the lag.
  * The tournament final against Rey Fenix is scheduled for TONIGHT, August 31, 2026,
    and has not happened as this module is compiled. Nothing about its result is
    stated or implied.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2017-06-26", promo="LU", landmark=True,
         event="Ultima Lucha Tres", opponent="Prince Puma",
         stip="Loser Must Retire — Wikipedia's taping date for a season finale that aired later",
         title="Lucha Underground Championship"),
    dict(result="W", date="2018-04-22", promo="Impact", landmark=True,
         event="Redemption", opponent="Austin Aries",
         stip="Singles — wins Impact's world title in his debut month",
         title="Impact World Championship"),
    dict(result="W", date="2021-09-05", promo="AEW", type="tag", landmark=True,
         event="All Out", opponent="The Young Bucks",
         stip="Steel cage, with Rey Fenix — WON Match of the Year",
         title="AEW World Tag Team Championship"),
    dict(result="L", date="2022-01-05", promo="AEW", type="tag",
         event="Dynamite", opponent="Jurassic Express",
         stip="Tag, with Rey Fenix — the 122-day reign ends",
         title="AEW World Tag Team Championship"),
    dict(result="W", date="2022-09-07", promo="AEW", type="tag",
         event="Dynamite", opponent="Best Friends",
         stip="Trios, with Pac & Rey Fenix as Death Triangle",
         title="AEW World Trios Championship"),
    dict(result="L", date="2023-01-11", promo="AEW", type="tag",
         event="Dynamite", opponent="The Elite",
         stip="Ladder match — match seven of the series ends the trios reign",
         title="AEW World Trios Championship"),
    dict(result="W", date="2025-01-13", promo="WWE", landmark=True,
         event="Raw", opponent="Chad Gable",
         stip="Singles — WWE debut, a week after the Netflix premiere teaser", title=""),
    dict(result="L", date="2025-02-01", promo="WWE", type="tag",
         event="Royal Rumble match", opponent="The 2025 Royal Rumble field",
         stip="Official iron man at 42:04 — with an asterisk printed below", title=""),
    dict(result="L", date="2025-04-20", promo="WWE", type="tag", landmark=True,
         event="WrestleMania 41 Night 2", opponent="Dominik Mysterio, Bron Breakker & Finn Balor",
         stip="Fatal four-way — Mysterio takes Breakker's title",
         title="WWE Intercontinental Championship"),
    dict(result="L", date="2025-05-10", promo="WWE",
         event="Backlash", opponent="Dominik Mysterio",
         stip="Singles — El Grande Americano's interference decides it",
         title="WWE Intercontinental Championship"),
    dict(result="W", date="2026-03-02", promo="WWE", landmark=True,
         event="Raw", opponent="Dominik Mysterio",
         stip="Singles — first WWE championship", title="WWE Intercontinental Championship"),
    dict(result="W", date="2026-04-19", promo="WWE", type="tag", landmark=True,
         event="WrestleMania 42 Night 2",
         opponent="Je'Von Evans, Dragon Lee, Rey Mysterio, Rusev & JD McDonagh",
         stip="Six-man ladder match — retains in the ESPN opener",
         title="WWE Intercontinental Championship"),
    dict(result="L", date="2026-08-02", promo="WWE", landmark=True,
         event="SummerSlam Night 2 — Minneapolis", opponent="Chad Gable",
         stip="Singles — Gable wins his first singles title at home; the 153-day reign ends",
         title="WWE Intercontinental Championship"),
    dict(result="W", date="2026-08-10", promo="WWE",
         event="Raw", opponent="Laredo Kid",
         stip="World title No. 1 Contender's Tournament quarterfinal", title=""),
    dict(result="W", date="2026-08-24", promo="WWE",
         event="Raw", opponent="La Parka",
         stip="Tournament semifinal — won with a springboard Mexican Destroyer", title=""),
]

DATA = dict(
    slug="penta",
    name="Penta",
    realname="Not publicly disclosed",
    epithet="Cero Miedo",
    hook="Record & Titles",

    meta_desc=("Penta, the masked luchador of Cero Miedo, is a former Impact World, Lucha "
               "Underground and WWE Intercontinental Champion who faces his brother Rey Fenix "
               "in a tournament final to challenge Roman Reigns. Full record, titles and "
               "career."),
    og_desc=("Cero Miedo: world titles in Impact and Lucha Underground, tag gold across five "
             "promotions with Rey Fenix, a 153-day Intercontinental reign — and a tournament "
             "final against his own brother, winner to Roman Reigns."),
    tw_desc="Cero Miedo: Impact and LU world titles, 153 days as IC Champion, and his brother in a final.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2007",
    height_imp="5&#8242;11&#8243;",
    weight_lb="207",
    world_titles="2",
    vitals_tagline="Cero Miedo",
    support_note="Merch &middot; Games &middot; Watch",
    sp_items=[
        dict(ic="PT", title="WWE Shop", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="FF", title="AEW Fight Forever", sub="Playable, from the AEW years",
             tag="Play", href="https://www.aewgames.com/"),
        dict(ic="LU", title="Lucha Underground", sub="Four seasons on El Rey Network",
             tag="Watch", href="https://en.wikipedia.org/wiki/Lucha_Underground"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/penta"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Pentagon Jr. &middot; Pentagon Dark &middot; Penta El Zero Miedo",
    hero_tag="Ecatepec, State of Mexico &middot; <em>AAA &middot; Lucha Underground &middot; "
             "Impact &middot; AEW &middot; WWE &middot; 2007&ndash;present</em>",
    now_label="NOW",
    now_bold="Raw, tournament finalist",
    now_tail=" &middot; faces his brother Rey Fenix tonight, August 31, in the World Heavyweight "
             "title No. 1 Contender&rsquo;s Tournament final &mdash; the winner meets Roman "
             "Reigns in Mexico City on September 14",
    hstats=[
        dict(value="153", x=False, label="Day IC Reign"),
        dict(value="2",   x=True,  label="World Titles"),
        dict(value="42:04", x=False, label="2025 Rumble Iron Man"),
        dict(value="0",   x=False, label="Times Unmasked"),
    ],
    ghost_link="From Ecatepec to a final against his own brother",
    vlabel="Est. 2007 &middot; Ecatepec, Mexico",
    mono="PT",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Penta</b> arrives at the biggest week of his WWE run with the two things that have "
        "defined twenty years of work: a mask that has never come off, and a brother on the "
        "other side of the ring. He is the former Pentagon Jr., the Lucha Underground and "
        "Impact World Champion whose &ldquo;Cero Miedo&rdquo; &mdash; zero fear &mdash; became "
        "a two-fingered gesture recognised far outside wrestling, and who spent 2019&ndash;24 "
        "in AEW winning tag team gold with Rey Fenix as the Lucha Brothers. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">153</span>'
        '<span class="pull-cap">days as WWE Intercontinental Champion in 2026 &mdash; March 2 to August 2, his first WWE title</span></span>'
        "In WWE since January 2025, he won the Intercontinental Championship from Dominik "
        "Mysterio on March 2, 2026, held it 153 days through a WrestleMania 42 ladder match, "
        "and lost it to Chad Gable at SummerSlam. Tonight &mdash; the August 31, 2026 Raw "
        "&mdash; he faces Rey Fenix in the final of the World Heavyweight Championship No. 1 "
        "Contender&rsquo;s Tournament. The winner challenges Roman Reigns in Mexico City on "
        "September 14. As this page is compiled, the final has not yet happened, and nothing "
        "here assumes its result.",

        "The famous statistic needs its asterisk. Penta is the official iron man of the 2025 "
        "men&rsquo;s Royal Rumble at <b>42 minutes and 4 seconds</b> &mdash; and Cageside "
        "Seats, reviewing the tape, concluded he probably should not be: at roughly 1:45 into "
        "the match, both of his feet appear to touch the floor as Rey Mysterio dumps him over "
        "the top rope. No referee called it, WWE showed no replay, and the elimination never "
        "officially happened, so the record stands. This page prints the official figure and "
        "the doubt together, because that is what the sources do. Two smaller flags while the "
        "ledger is open: WWE.com&rsquo;s profile still lists him as Intercontinental Champion "
        "&mdash; Chad Gable beat him for it on August 2, 2026 &mdash; and his real name is "
        "absent from this page not as an oversight but because it has never been publicly "
        "disclosed. He has never been unmasked in a ring.",

        "The road here ran through every major promotion on the continent. Born in Ecatepec "
        "on February 26, 1985 and trained by Skayde, he debuted in 2007, took the Pentagon "
        "Jr. name in AAA in December 2012, and answered the legend that the Pentagon name "
        "carried a curse with the catchphrase that became the brand. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig pull-fig--sm">CERO MIEDO</span>'
        '<span class="pull-cap">zero fear &mdash; the answer to a supposed curse on the Pentagon name, now the whole identity</span></span>'
        "Lucha Underground made him a cult star &mdash; the arm-breaking sacrifices, the "
        "Pentagon Dark turn, and the Lucha Underground Championship won from Prince Puma in "
        "the match that retired Puma. Impact made him a world champion inside a month in "
        "2018, beating Austin Aries at Redemption on April 22. AEW made the Lucha Brothers "
        "the best tag team in the world by acclamation: the steel cage win over the Young "
        "Bucks at All Out on September 5, 2021 took the Wrestling Observer&rsquo;s Match of "
        "the Year, and Death Triangle&rsquo;s trios run with Pac followed. His AEW contract "
        "expired December 1, 2024; WWE teased him during Raw&rsquo;s Netflix premiere and he "
        "debuted on January 13, 2025, beating Chad Gable &mdash; the same man who would take "
        "his title nineteen months later.",

        "The 2026 season has been shaped by an injury and a family. A shoulder injury "
        "suffered against Solo Sikoa on the November 24, 2025 Raw ended his year; he "
        "returned in the Royal Rumble on January 31 at No. 28, took the Intercontinental "
        "Championship from Dominik Mysterio on March 2, and retained it in the six-man "
        "ladder match that opened WrestleMania 42&rsquo;s Sunday card &mdash; eliminating "
        "Je&rsquo;Von Evans with a Mexican Destroyer before pulling the belt down. After "
        "Gable beat him in Minneapolis, WWE announced an eight-man tournament of luchadors "
        "from Raw, SmackDown and AAA for Roman Reigns&rsquo; World Heavyweight Championship; "
        "Penta beat Laredo Kid on August 10 and La Parka on August 24, Fenix beat El Fiscal "
        "and Dragon Lee, and the brothers touched foreheads in the ring when the final was "
        "set. They have held tag titles together in AEW, ROH, Impact, PWG and MLW. They have "
        "never needed to settle which of them goes first &mdash; until tonight.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE", "AEW", "Impact", "LU"],
        promo_labels={"WWE": "WWE", "AEW": "AEW", "Impact": "Impact", "LU": "Lucha Underground"},
        stats=[
            ("153",   "Day IC reign"),
            ("2",     "World titles"),
            ("42:04", "2025 Rumble iron man"),
            ("5",     "Promotions with tag gold"),
            ("2007",  "Debut year"),
            ("0",     "Times unmasked"),
        ],
        lead=("Fifteen documented bouts across four promotions &mdash; the world title wins, "
              "the tag championships with Rey Fenix, and the complete WWE arc through the "
              "August 24 semifinal. A curated ledger, not a career count: no verified "
              "win&ndash;loss total exists across a career this scattered, and none is "
              "invented. The Ultima Lucha Tres date is Wikipedia&rsquo;s taping date for a "
              "television season that aired months later, and is flagged in the row. The "
              "August 31 final against Fenix is deliberately absent &mdash; it has not "
              "happened yet. Filter by match type, tap any column header to sort, and turn "
              "spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("One rating is verified and it is the big one: the Wrestling Observer "
                    "Newsletter named the All Out 2021 steel cage match its Match of the "
                    "Year. No other Observer ratings for his matches were verified in this "
                    "pass, so only that entry is listed &mdash; the WrestleMania 42 ladder "
                    "match and the Ultima Lucha Tres retirement match live in the record "
                    "table instead."),
    signature=[
        dict(rating="5.0", event="All Out 2021", opponent="The Young Bucks",
             stip="Steel cage, with Rey Fenix — AEW World Tag Team Championship; WON Match "
                  "of the Year"),
    ],
    signature_count_word="one",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("2",        "World title reigns"),
            ("153",      "Day IC reign"),
            ("5",        "Promotions with tag gold"),
            ("3&times;", "AAA World Tag reigns"),
        ],
        lead=("Two world championships, one WWE singles title, and tag gold in five different "
              "promotions &mdash; almost all of it with his brother. Early lucha reign dates "
              "are given as Wikipedia gives them; where the record is thin it says so."),
        rows=[
            dict(ic="I", name="WWE Intercontinental Championship", count="1",
                 sub="March 2 &ndash; August 2, 2026 &middot; def. Dominik Mysterio on Raw, "
                     "lost to Chad Gable at SummerSlam Night 2 &middot; <b>153 days</b> "
                     "&middot; defenses included El Grande Americano, Dragon Lee, Kofi "
                     "Kingston, El Hijo del Vikingo and the WrestleMania 42 six-man ladder "
                     "match &middot; WWE.com&rsquo;s profile still lists him as champion; "
                     "this page follows the result"),
            dict(ic="W", name="Impact World Championship", count="1",
                 sub="April 22 &ndash; May 2018 &middot; def. Austin Aries at Redemption in "
                     "his debut month, defended against Eli Drake, lost back to Aries on the "
                     "episode aired May 31 &middot; his biggest singles title before WWE"),
            dict(ic="L", name="Lucha Underground Championship", count="1",
                 sub="Won from Prince Puma in a Loser Must Retire match at Ultima Lucha Tres "
                     "&mdash; Wikipedia&rsquo;s taping date is June 26, 2017; the episode "
                     "aired later that year &middot; he had won the Gift of the Gods "
                     "Championship in a ladder match the night before, by the same reckoning"),
            dict(ic="T", name="AEW World Tag Team Championship", count="1",
                 sub="September 5, 2021 &ndash; January 5, 2022, with Rey Fenix &middot; won "
                     "from the Young Bucks in the All Out steel cage, lost to Jurassic "
                     "Express &middot; 122 days"),
            dict(ic="D", name="AEW World Trios Championship", count="1",
                 sub="September 7, 2022 &ndash; January 11, 2023, as Death Triangle with Pac "
                     "and Rey Fenix &middot; lost the seventh match of the series with The "
                     "Elite, a ladder match"),
            dict(ic="R", name="ROH World Tag Team Championship", count="1",
                 sub="March 31 &ndash; July 21, 2023, with Rey Fenix &middot; won in a "
                     "six-team ladder match, lost to Aussie Open &middot; dates per Wikipedia"),
            dict(ic="X", name="Impact, PWG & MLW tag championships", count="3",
                 sub="Impact World Tag (2019, with Fenix, lost to LAX at Rebellion) &middot; "
                     "PWG World Tag (2017, with Fenix, 216 days per Wikipedia) &middot; MLW "
                     "World Tag (2018, with Fenix) &middot; individual dates not re-verified "
                     "in this pass"),
            dict(ic="A", name="AAA championships", count="5",
                 sub="AAA Latin American Championship (2016 &mdash; def. Psycho Clown July 3, "
                     "lost to Johnny Mundo August 28, per Wikipedia) &middot; AAA World Tag "
                     "Team Championship, 3 reigns, with Joe Lider and with Rey Fenix &middot; "
                     "AAA World Mixed Tag, with Sexy Star &middot; plus the 2016 Rey de Reyes "
                     "tournament &middot; reign dates not re-verified"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Two units, both family in one sense or the other &mdash; and the partnership "
             "that tonight&rsquo;s final briefly suspends.",
        cards=[
            dict(era="Everywhere &middot; 2017&ndash;present",
                 name="The Lucha Brothers",
                 members="Penta, Rey Fenix",
                 desc="Actual brothers, and the most decorated tag team of their generation "
                      "across promotions: AEW, ROH, Impact, PWG, MLW and AAA gold, the WON "
                      "Tag Team of the Year award for 2019, and the 2021 Match of the Year in "
                      "the All Out cage. In WWE they have appeared as allies rather than a "
                      "booked team — after the August 24 semifinals they touched foreheads in "
                      "the ring. Tonight they wrestle each other for the right to challenge "
                      "Roman Reigns; the respect, on every appearance so far, is the story "
                      "WWE is telling."),
            dict(era="AEW &middot; 2020&ndash;23",
                 name="Death Triangle",
                 members="Pac, Penta, Rey Fenix",
                 desc="Formed March 4, 2020. Won the AEW World Trios Championship on "
                      "September 7, 2022 and defended it through a celebrated seven-match "
                      "series with The Elite, losing the decider — a ladder match — on "
                      "January 11, 2023. The unit that proved Penta could anchor main-event "
                      "trios wrestling without the mask ever slipping toward comedy."),
            dict(era="Lucha Underground &middot; 2015&ndash;18",
                 name="The cult of Pentagon Dark",
                 members="Pentagon Jr., alone — apprenticed to Vampiro",
                 desc="Not a stable but a storyline church: the arm-breaking \"sacrifices\" "
                      "offered to his unseen master, revealed as Vampiro, and the Pentagon "
                      "Dark persona that followed. It is where the American audience learned "
                      "the gesture, the catchphrase and the sadism, and it fed directly into "
                      "everything he has played since."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Five names under one mask, and the mask is the constant &mdash; it has never "
             "come off in a ring.",
        cards=[
            dict(mono="DD", era="Mexico &middot; 2007&ndash;12", name="Dark Dragon and before",
                 desc="The apprenticeship years under trainer Skayde, working early "
                      "personas including Zaius and Dark Dragon on the Mexican independents. "
                      "First verified match: April 9, 2008, per Wikipedia."),
            dict(mono="PJ", era="AAA &middot; 2012&ndash;17", name="Pentagon Jr.",
                 desc="Adopted December 2, 2012 in AAA. The legend that the Pentagon name "
                      "carried a curse got the answer that became the brand: Cero Miedo — "
                      "zero fear. Rey de Reyes winner in 2016; left AAA in January 2017 "
                      "citing feeling restricted."),
            dict(mono="PD", era="Lucha Underground &middot; 2015&ndash;18", name="Pentagon Dark",
                 desc="The darker evolution built on broken arms and sacrifice, and the "
                      "promotion's biggest homegrown star by its end: Gift of the Gods and "
                      "Lucha Underground Champion, and the first man to win Aztec Warfare "
                      "while holding the title, in the June 2018 season four opener."),
            dict(mono="PZ", era="Impact, AEW &middot; 2018&ndash;24", name="Penta El Zero Miedo",
                 desc="The name of the world-title and Lucha Brothers years — Impact World "
                      "Champion in 2018, AEW tag and trios champion, one half of the WON "
                      "2019 Tag Team of the Year and 2021 Match of the Year. His AEW "
                      "contract expired December 1, 2024."),
            dict(mono="P", era="WWE &middot; 2025&ndash;present", name="Penta",
                 desc="WWE shortened the name and changed nothing else — the mask, the "
                      "gesture, the Mexican Destroyer and the Penta Driver all survived "
                      "intact. His three daughters attended the January 13, 2025 debut; NFL "
                      "tight end George Kittle, a friend, throws the Cero Miedo gesture in "
                      "touchdown celebrations."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Ecatepec to a Mexico City title match that runs through his own brother.",
        rows=[
            dict(year="2007", title="Debut",
                 desc="Debuts on the Mexican independents, trained by Skayde; Wikipedia's "
                      "first verified match is April 9, 2008."),
            dict(year="2012", title="Becomes Pentagon Jr.",
                 desc="Takes the name in AAA on December 2, 2012, and answers the Pentagon "
                      "curse legend with Cero Miedo."),
            dict(year="2017", title="Lucha Underground Champion",
                 desc="Wins the Gift of the Gods ladder match and then the Lucha Underground "
                      "Championship from Prince Puma in the Loser Must Retire match at "
                      "Ultima Lucha Tres."),
            dict(year="2018", title="Impact World Champion in his debut month",
                 desc="Beats Austin Aries at Redemption on April 22; loses the title back "
                      "within six weeks; wrestles Sami Callihan in the mask-vs-hair match at "
                      "Slammiversary."),
            dict(year="2021", title="The cage match",
                 desc="With Rey Fenix, beats the Young Bucks in the All Out steel cage on "
                      "September 5 for the AEW World Tag Team Championship — the Wrestling "
                      "Observer's Match of the Year."),
            dict(year="2022", title="Death Triangle's trios reign",
                 desc="Wins the AEW World Trios Championship with Pac and Fenix on September "
                      "7 and defends it through the seven-match Elite series, losing the "
                      "ladder-match decider in January 2023."),
            dict(year="2025", title="WWE debut, and an injury",
                 desc="Debuts January 13, beating Chad Gable; officially survives 42:04 in "
                      "the Royal Rumble; loses the WrestleMania 41 and Backlash "
                      "Intercontinental matches to Dominik Mysterio's ecosystem; a shoulder "
                      "injury against Solo Sikoa on November 24 ends his year."),
            dict(year="2026", title="Champion, ex-champion, finalist",
                 desc="Returns in the Royal Rumble at No. 28; beats Dominik Mysterio for the "
                      "Intercontinental Championship on March 2; retains in the WrestleMania "
                      "42 ladder match; loses to Chad Gable at SummerSlam on August 2; beats "
                      "Laredo Kid and La Parka to reach the August 31 tournament final "
                      "against Rey Fenix — winner challenges Roman Reigns in Mexico City on "
                      "September 14."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Rey Fenix",
                 desc="Brother, career-long partner, and — tonight — opponent. They have won "
                      "tag titles together in five promotions and have been booked in WWE as "
                      "allies who end each other's matches with a forehead touch. The August "
                      "31 tournament final is their first singles meeting in WWE, with a "
                      "September 14 World Heavyweight Championship match against Roman "
                      "Reigns in Mexico City behind it. Their AEW and indie singles matches "
                      "were rare and treated as occasions; WWE is treating this one the same "
                      "way."),
            dict(name="Chad Gable",
                 desc="The bookends of the WWE run so far: Penta beat Gable in his January "
                      "13, 2025 debut, and Gable beat Penta for the Intercontinental "
                      "Championship at SummerSlam on August 2, 2026 — in his home market, in "
                      "tears, for his first singles title. Between the two matches sat "
                      "Gable's El Grande Americano project, whose interference had cost "
                      "Penta the Backlash 2025 title match."),
            dict(name="Dominik Mysterio",
                 desc="The long chase for the Intercontinental Championship: the WrestleMania "
                      "41 fatal four-way, the Backlash 2025 singles loss with El Grande "
                      "Americano involved, an October 2025 defense, and finally the March 2, "
                      "2026 Raw win that made Penta a WWE champion for the first time."),
            dict(name="Sami Callihan",
                 desc="The Impact-era blood feud, peaking in the mask-vs-hair match at "
                      "Slammiversary XVI on July 22, 2018 — the highest-stakes match a "
                      "masked man can take, and Penta's mask survived it."),
            dict(name="The Young Bucks",
                 desc="The AEW rivalry that produced his most acclaimed match: the September "
                      "5, 2021 All Out steel cage, Lucha Brothers versus Bucks for the tag "
                      "titles, the Wrestling Observer's 2021 Match of the Year and the "
                      "Dynamite Award winner for best brawl."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="The mask travels well.",
        rows=[
            dict(when="2014&ndash;18", title="Lucha Underground", kind="TV",
                 desc="Four seasons on El Rey Network as Pentagon Jr. and Pentagon Dark — "
                      "scripted, serialized television that made him a cult star in the "
                      "United States before any national promotion signed him."),
            dict(when="2023", title="AEW Fight Forever", kind="Game",
                 desc="Playable as Penta El Zero Miedo, from the AEW years. His WWE video "
                      "game debut could not be confirmed in this pass and is not claimed."),
            dict(when="2019&ndash;", title="Cero Miedo in the wild", kind="Culture",
                 desc="The two-fingered Cero Miedo gesture circulates beyond wrestling — "
                      "NFL tight end George Kittle, a friend, uses it in touchdown "
                      "celebrations, and WWE's own profile leads with the hand sign as his "
                      "identifier."),
            dict(when="2025", title="The WWE debut broadcast", kind="TV",
                 desc="Teased in a video during Raw's Netflix premiere on January 6, 2025 "
                      "and debuted a week later against Chad Gable, with his three daughters "
                      "at ringside — the rare WWE debut framed around a family in the "
                      "building."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records and the asterisks &mdash; including an iron-man run that comes "
             "with its own footnote.",
        stats=[
            ("153",   "Day IC reign"),
            ("42:04", "Official 2025 Rumble time"),
            ("5",     "Promotions with tag gold"),
        ],
        rows=[
            dict(name="World champion in two promotions",
                 sub="The Lucha Underground Championship, won in the match that retired "
                     "Prince Puma, and the Impact World Championship, won April 22, 2018 at "
                     "Redemption in his debut month with the company."),
            dict(name="153 days as WWE Intercontinental Champion",
                 sub="March 2 to August 2, 2026 — his first WWE title, won from Dominik "
                     "Mysterio and lost to Chad Gable. The defense list ran through El "
                     "Grande Americano, Dragon Lee, Kofi Kingston, El Hijo del Vikingo and "
                     "the WrestleMania 42 six-man ladder match."),
            dict(name="Official iron man of the 2025 men's Royal Rumble — 42:04, asterisk included",
                 sub="The longest official survival time in that match. Cageside Seats' "
                     "review found both feet appearing to touch the floor at roughly 1:45, "
                     "unruled and unreplayed. The record stands because no referee called "
                     "it; the footnote stands because the tape exists."),
            dict(name="Tag team championships in five promotions with the same partner",
                 sub="AEW, ROH, Impact, PWG and MLW, all with Rey Fenix — plus three AAA "
                     "tag reigns. The Lucha Brothers were the Wrestling Observer's 2019 Tag "
                     "Team of the Year."),
            dict(name="Wrestling Observer Match of the Year, 2021",
                 sub="The All Out steel cage against the Young Bucks, September 5, 2021, "
                     "with Fenix."),
            dict(name="First to win Aztec Warfare as champion",
                 sub="Lucha Underground's season four opener, June 2018 by Wikipedia's "
                     "taping-based dating — winning the promotion's Rumble-equivalent while "
                     "holding its title."),
            dict(name="The mask has never come off",
                 sub="No unmasking in nineteen years, including the mask-vs-hair stakes "
                     "against Sami Callihan at Slammiversary XVI. His real name has never "
                     "been publicly disclosed, and this page does not publish one."),
            dict(name="A final against his own brother, winner to Roman Reigns",
                 sub="The World Heavyweight Championship No. 1 Contender's Tournament — "
                     "eight luchadors from Raw, SmackDown and AAA — comes down to Penta vs. "
                     "Rey Fenix on the August 31, 2026 Raw. The winner challenges Reigns on "
                     "the September 14 Raw in Mexico City. Not yet wrestled as this page is "
                     "compiled; no result is implied."),
        ],
        footnote=("Deliberately absent: a real name, never publicly disclosed; a career "
                  "win-loss total, never verified; social handles, unverified; and any "
                  "result for tonight's final. WWE.com's stale Intercontinental Champion "
                  "listing is flagged above. Early Lucha Underground dates are Wikipedia's "
                  "taping dates for a television show that aired on delay, and are marked "
                  "as such wherever used."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/penta"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Penta_(wrestler)"),
        dict(k="WWE.com", v="The No. 1 Contender's Tournament bracket",
             href="https://www.wwe.com/article/world-heavyweight-title-number-one-contenders-tournament"),
        dict(k="POST Wrestling", v="WrestleMania 42 — the six-man ladder match",
             href="https://www.postwrestling.com/2026/04/19/penta-wins-hectic-six-man-ladder-match-to-retain-intercontinental-title-at-wrestlemania-42/"),
        dict(k="Wrestling Inc.", v="Raw results, August 24, 2026 — the semifinals",
             href="https://www.wrestlinginc.com/2243203/wwe-raw-august-24-stephanie-vaquer-roxanne-perez-contract-signing-more/"),
        dict(k="Cageside Seats", v="The 2025 Rumble iron-man asterisk",
             href="https://www.cagesideseats.com/wwe/2025/2/3/24357462/wwe-royal-rumble-2025-mens-survival-times-complete-list-iron-man-penta-elimination-controversy-cena"),
        dict(k="Newsweek", v="The November 2025 shoulder injury",
             href="https://www.newsweek.com/sports/wrestling/injured-wwe-star-penta-targeting-ple-return-in-2026-11281651"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="When does Penta face Rey Fenix, and what is at stake?",
            a="Tonight &mdash; the <b>August 31, 2026</b> Raw &mdash; in the final of the "
              "World Heavyweight Championship No. 1 Contender&rsquo;s Tournament, an "
              "eight-man field of luchadors from Raw, SmackDown and AAA. The winner "
              "challenges World Heavyweight Champion <b>Roman Reigns</b> on the September 14 "
              "Raw in Mexico City. Penta beat Laredo Kid in the quarterfinals on August 10 "
              "and La Parka in the semifinals on August 24; Fenix beat El Fiscal and Dragon "
              "Lee. They are brothers, career-long tag partners, and &mdash; as of this "
              "page&rsquo;s compilation &mdash; the match has not yet happened, so no result "
              "is given anywhere here.",
            q_ld="When does Penta face Rey Fenix and what is at stake?",
            a_ld="Penta faces his brother Rey Fenix on the August 31, 2026 episode of WWE "
                 "Raw, in the final of the World Heavyweight Championship No. 1 Contender's "
                 "Tournament. The winner challenges World Heavyweight Champion Roman Reigns "
                 "on the September 14, 2026 Raw in Mexico City. Penta defeated Laredo Kid "
                 "and La Parka to reach the final; Rey Fenix defeated El Fiscal and Dragon "
                 "Lee."),
        dict(
            q="Is Penta still the Intercontinental Champion?",
            a="No &mdash; though WWE.com&rsquo;s profile still says so, which is why the "
              "question keeps coming up. <b>Chad Gable</b> beat him for the title at "
              "SummerSlam Night 2 on <b>August 2, 2026</b> in Minneapolis, Gable&rsquo;s "
              "home market, winning his first singles championship in tears. Penta&rsquo;s "
              "reign ran <b>153 days</b> from March 2, 2026, when he beat Dominik Mysterio "
              "on Raw, and included the six-man ladder match that opened WrestleMania 42 "
              "Night 2. This page follows the result and flags the profile lag.",
            q_ld="Is Penta still the WWE Intercontinental Champion?",
            a_ld="No. Penta lost the WWE Intercontinental Championship to Chad Gable at "
                 "SummerSlam Night 2 on August 2, 2026, ending a 153-day reign that began "
                 "on March 2, 2026 when he defeated Dominik Mysterio on Raw. WWE.com's "
                 "profile page has not yet been updated and still lists Penta as champion."),
        dict(
            q="Was Penta really the iron man of the 2025 Royal Rumble?",
            a="Officially yes: <b>42 minutes and 4 seconds</b>, the longest survival time "
              "in the 2025 men&rsquo;s match. Honestly: with an asterisk. Cageside "
              "Seats&rsquo; review of the tape found that at roughly 1:45 into the match, "
              "both of Penta&rsquo;s feet appear to touch the floor as Rey Mysterio sends "
              "him over the top rope. No referee ruled it, WWE showed no replay, and no "
              "elimination was recorded, so the record stands &mdash; and so does the "
              "footnote. Both are printed on this page because both are what the sources "
              "say.",
            q_ld="Was Penta the iron man of the 2025 men's Royal Rumble?",
            a_ld="Officially yes. Penta's 42 minutes and 4 seconds was the longest official "
                 "survival time in the 2025 men's Royal Rumble. However, Cageside Seats' "
                 "review of the footage found that both of Penta's feet appear to touch the "
                 "floor about 1 minute 45 seconds into the match when Rey Mysterio threw "
                 "him over the top rope; no referee ruled an elimination and WWE showed no "
                 "replay, so the official record stands with that documented caveat."),
        dict(
            q="What is Penta&rsquo;s real name?",
            a="It has never been publicly disclosed, and this page does not publish one. "
              "That is the lucha libre tradition working as intended: he has wrestled under "
              "a mask since 2007, put it at stake exactly once &mdash; the mask-vs-hair "
              "match against Sami Callihan at Slammiversary XVI in 2018, which he won "
              "&mdash; and has never been unmasked in a ring. What is public: born February "
              "26, 1985 in Ecatepec, State of Mexico; trained by Skayde; the younger "
              "brother is Rey Fenix.",
            q_ld="What is Penta's real name?",
            a_ld="Penta's real name has never been publicly disclosed, in keeping with "
                 "lucha libre tradition. He has never been unmasked in a ring and won the "
                 "one match in which his mask was at stake, against Sami Callihan at "
                 "Slammiversary XVI in 2018. He was born on February 26, 1985 in Ecatepec, "
                 "State of Mexico, and his brother is the wrestler Rey Fenix."),
        dict(
            q="What does &ldquo;Cero Miedo&rdquo; mean?",
            a="&ldquo;Zero fear.&rdquo; It began in AAA as an answer to the legend that the "
              "Pentagon name carried a curse &mdash; his position was that he feared "
              "nothing, curse included &mdash; and became the catchphrase, the two-fingered "
              "hand gesture and effectively the whole brand. WWE&rsquo;s profile leads with "
              "the gesture; NFL tight end George Kittle, a friend, throws it in touchdown "
              "celebrations; and the shortened ring name he uses now, Penta, sits under "
              "the same two words on every piece of merchandise.",
            q_ld="What does Cero Miedo mean?",
            a_ld="Cero Miedo is Spanish for zero fear. It originated in AAA as Penta's "
                 "answer to a legend that the Pentagon ring name carried a curse, and "
                 "became his catchphrase and signature two-fingered hand gesture. NFL "
                 "tight end George Kittle, a friend of Penta's, uses the gesture in "
                 "touchdown celebrations."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Not publicly disclosed",
             sub="never unmasked &mdash; the lucha libre tradition holds"),
        dict(label="Born", value="February 26, 1985",
             sub="Ecatepec, State of Mexico &middot; age 41"),
        dict(label="Billed from", value="Mexico"),
        dict(label="Height", value="5&#8242;11&#8243;", sub="180 cm &middot; per WWE.com"),
        dict(label="Weight", value="207 lb", sub="94 kg &middot; per WWE.com"),
        dict(label="Debut", value="2007",
             sub="trained by Skayde &middot; first verified match April 9, 2008"),
        dict(label="Family", value="Brother of Rey Fenix",
             sub="tag gold together in five promotions"),
        dict(label="Signature", value="Mexican Destroyer &middot; Penta Driver &middot; The "
                                      "Sacrifice",
             sub="the arm-breaker carried over from Lucha Underground"),
        dict(label="Ring names",
             value="Dark Dragon &rarr; Pentagon Jr. &rarr; Pentagon Dark &rarr; Penta El "
                   "Zero Miedo &rarr; Penta",
             sub="2007&ndash;12 &middot; 2012&ndash;17 &middot; LU era &middot; "
                 "2018&ndash;24 &middot; 2025&ndash;present"),
        dict(label="Brand", value="Raw", sub="since January 13, 2025"),
        dict(label="Also known as", value="Cero Miedo &middot; one half of the Lucha Brothers"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1985-02-26",
    bornplace="Ecatepec, State of Mexico, Mexico",
    nationality="Mexico",
    height_cm=180,
    weight_kg=94,
    ld=dict(
        alternateName=["Pentagon Jr.", "Pentagon Dark", "Penta El Zero Miedo", "Dark Dragon",
                       "Cero Miedo"],
        award=["WWE Intercontinental Championship (1 reign, 153 days)",
               "Impact World Championship (1 reign)",
               "Lucha Underground Championship (1 reign)",
               "Lucha Underground Gift of the Gods Championship (1 reign)",
               "AEW World Tag Team Championship (1 reign, with Rey Fenix)",
               "AEW World Trios Championship (1 reign, with Pac and Rey Fenix)",
               "ROH World Tag Team Championship (1 reign, with Rey Fenix)",
               "Impact World Tag Team Championship (1 reign, with Rey Fenix)",
               "PWG World Tag Team Championship (1 reign, with Rey Fenix)",
               "MLW World Tag Team Championship (1 reign, with Rey Fenix)",
               "AAA Latin American Championship (1 reign)",
               "AAA World Tag Team Championship (3 reigns)",
               "AAA World Mixed Tag Team Championship (1 reign, with Sexy Star)",
               "AAA Rey de Reyes (2016)",
               "Wrestling Observer Newsletter Tag Team of the Year (2019, with Rey Fenix)",
               "Wrestling Observer Newsletter Match of the Year (2021, vs. the Young Bucks)"],
        knowsAbout=["Professional wrestling", "Lucha libre", "WWE", "AEW", "Lucha Underground",
                    "Impact Wrestling", "AAA", "Tag team wrestling"],
        description="Penta is a Mexican masked luchador signed to WWE's Raw brand, formerly "
                    "known as Pentagon Jr. and Penta El Zero Miedo. Famous for the Cero Miedo "
                    "catchphrase and gesture, he is a former Lucha Underground Champion, "
                    "Impact World Champion and WWE Intercontinental Champion, and won tag "
                    "team gold in five promotions with his brother Rey Fenix as the Lucha "
                    "Brothers, including a Wrestling Observer Match of the Year steel cage "
                    "win over the Young Bucks at AEW All Out 2021. He faces Rey Fenix in a "
                    "tournament final on August 31, 2026, with the winner challenging Roman "
                    "Reigns for the World Heavyweight Championship in Mexico City.",
        sameAs=["https://en.wikipedia.org/wiki/Penta_(wrestler)",
                "https://www.wwe.com/superstars/penta"],
    ),
)
