# -*- coding: utf-8 -*-
"""Dominik Mysterio - dossier data.

Sources: web research compiled August 31, 2026 - Wikipedia's Dominik Mysterio article
and List of NXT North American Champions, Fightful's Triplemania 34 coverage, POST
Wrestling and Bleacher Report on WrestleMania 42, The Sportster's SummerSlam 2026
Night 2 report, and Yahoo/Sports coverage of the Danhausen stipulation. Every match
row carries a day-precision date stated in one of the opened sources.

Deliberate omissions:
  * No career win-loss total - no verified figure exists.
  * His failed AAA Mega Championship challenge at Triplemania XXXIII (August 2025) is
    described in prose without a day-precision date, which was not re-verified.
  * No social handles - official accounts were not verified in this pass.
"""

# ----------------------------------------------------------------- record rows
# The title changes and the family matches. The NXT North American sequence follows the
# champions-list table (won July 18, lost at No Mercy, regained October 3, lost at
# Deadline); a biography summary in circulation reverses two of those dates - see the
# correction paragraph.
ROWS = [
    dict(result="L", date="2020-08-23", promo="WWE", landmark=True,
         event="SummerSlam", opponent="Seth Rollins",
         stip="Singles — in-ring debut at 23, with kendo sticks", title=""),
    dict(result="W", date="2021-05-16", promo="WWE", type="tag", landmark=True,
         event="WrestleMania Backlash", opponent="Dolph Ziggler & Robert Roode",
         stip="Tag — with Rey Mysterio; first father-son champions in WWE history",
         title="WWE SmackDown Tag Team Championship"),
    dict(result="L", date="2023-04-01", promo="WWE", landmark=True,
         event="WrestleMania 39 Night 1", opponent="Rey Mysterio",
         stip="Singles — father vs. son", title=""),
    dict(result="W", date="2023-07-18", promo="WWE", landmark=True,
         event="NXT", opponent="Wes Lee",
         stip="Singles — first singles title", title="NXT North American Championship"),
    dict(result="L", date="2023-09-30", promo="WWE",
         event="NXT No Mercy", opponent="Trick Williams",
         stip="Singles — the 74-day reign ends", title="NXT North American Championship"),
    dict(result="W", date="2023-10-03", promo="WWE",
         event="NXT", opponent="Trick Williams",
         stip="Singles — regains it three days later", title="NXT North American Championship"),
    dict(result="L", date="2023-12-09", promo="WWE",
         event="NXT Deadline", opponent="Dragon Lee",
         stip="Singles — the second reign ends at 67 days", title="NXT North American Championship"),
    dict(result="W", date="2025-04-20", promo="WWE", type="tag", landmark=True,
         event="WrestleMania 41 Night 2", opponent="Finn Balor, Penta & Bron Breakker",
         stip="Fatal four-way — pins Breakker after Balor's inadvertent assist",
         title="WWE Intercontinental Championship"),
    dict(result="W", date="2025-08-03", promo="WWE",
         event="SummerSlam Night 2", opponent="AJ Styles",
         stip="Singles — retains", title="WWE Intercontinental Championship"),
    dict(result="W", date="2025-09-12", promo="AAA", landmark=True,
         event="Worlds Collide: Las Vegas", opponent="El Hijo del Vikingo",
         stip="Singles — first non-WWE title", title="AAA Mega Championship"),
    dict(result="L", date="2025-11-10", promo="WWE", landmark=True,
         event="Raw", opponent="John Cena",
         stip="Singles — the 204-day reign ends; Cena completes the Grand Slam",
         title="WWE Intercontinental Championship"),
    dict(result="W", date="2025-11-29", promo="WWE", landmark=True,
         event="Survivor Series — San Diego", opponent="John Cena",
         stip="Singles — regains it in his hometown", title="WWE Intercontinental Championship"),
    dict(result="L", date="2026-03-02", promo="WWE", landmark=True,
         event="Raw", opponent="Penta",
         stip="Singles — the 93-day reign ends after Balor withholds the hammer",
         title="WWE Intercontinental Championship"),
    dict(result="W", date="2026-03-14", promo="AAA",
         event="AAA Rey de Reyes", opponent="El Hijo del Vikingo",
         stip="Singles — retains", title="AAA Mega Championship"),
    dict(result="L", date="2026-04-19", promo="WWE", landmark=True,
         event="WrestleMania 42 Night 2", opponent="The Demon Finn Balor",
         stip="Street fight — Coup de Grace through a table", title=""),
    dict(result="L", date="2026-08-02", promo="WWE",
         event="SummerSlam Night 2 — Minneapolis", opponent="Danhausen",
         stip="Human Monies on a Pole match — $100,000 above the ring", title=""),
]

DATA = dict(
    slug="dominik-mysterio",
    name="Dominik Mysterio",
    realname="Dominik Oscar Gutierrez",
    epithet="Dirty Dom",
    hook="Record & Titles",

    meta_desc=("Dominik Mysterio, Dirty Dom, is a two-time Intercontinental Champion, the reigning "
               "AAA Mega Champion, and the Judgment Day's loudest heel. Full record, titles, "
               "factions, records and career."),
    og_desc=("Dirty Dom: two Intercontinental Championship reigns, an AAA Mega Championship held "
             "since September 2025, a win over John Cena, and the most reliably booed voice in "
             "WWE."),
    tw_desc="Dirty Dom: 2x Intercontinental Champion, reigning AAA Mega Champion, professionally booed.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2020",
    height_imp="6&#8242;1&#8243;",
    weight_lb="200",
    world_titles="1",
    vitals_tagline="Dirty Dominik",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="DM", title="WWE Shop", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable in the current 2K entries",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="AAA", title="Lucha Libre AAA", sub="Reigning Mega Champion",
             tag="Visit", href="https://en.wikipedia.org/wiki/AAA_Mega_Championship"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/dominik-mysterio"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Dirty Dom &middot; ex-con of storyline fame &middot; The Judgment Day",
    hero_tag="San Diego, California &middot; <em>WWE &middot; AAA &middot; third-generation Mysterio "
             "&middot; 2020&ndash;present</em>",
    now_label="NOW",
    now_bold="Raw, reigning AAA Mega Champion",
    now_tail=" &middot; lost $100,000 to Danhausen at SummerSlam and defends the AAA title against "
             "El Grande Americano at Triplemania 34 in Mexico City on September 13",
    hstats=[
        dict(value="204", x=False, label="Day IC Reign"),
        dict(value="2",   x=True,  label="IC Title Reigns"),
        dict(value="1",   x=True,  label="AAA Mega Title"),
        dict(value="2",   x=True,  label="NXT NA Reigns"),
    ],
    ghost_link="From the kid in the Eddie Guerrero custody angle to Dirty Dom",
    vlabel="Est. 2020 &middot; San Diego, California",
    mono="DM",

    # ---------------------------------------------------------------- 01 overview
    # index into overview of the correction paragraph -> the framed
    # "Setting one thing straight" callout (aside.corr) on the page
    correction=2,
    overview=[
        "<b>Dominik Mysterio</b> was on WWE television eight years before his first match &mdash; "
        "as the eight-year-old at the centre of the 2005 Eddie Guerrero custody storyline &mdash; "
        "and the arc of his career since has been the slow, deliberate weaponising of that "
        "familiarity. The dutiful son who debuted against Seth Rollins at SummerSlam 2020 and won "
        "tag team gold with his father became, from September 3, 2022, the Judgment Day's "
        "&ldquo;Dirty Dom&rdquo;: the most reliably booed man in the company, a two-time "
        "Intercontinental Champion, and &mdash; as of August 31, 2026 &mdash; the reigning "
        "<b>AAA Mega Champion</b>, a title he has now held since September 12, 2025. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">204</span>'
        '<span class="pull-cap">days in his first Intercontinental Championship reign, ended by John '
        'Cena on the November 10, 2025 Raw</span></span>'
        "He is a third-generation wrestler &mdash; grandson of Rey Mysterio Sr., son of Rey "
        "Mysterio &mdash; who has built a career on being the family disappointment on purpose.",

        "The title record is stronger than the sneer suggests. He and Rey became the first "
        "father-son tag team champions in WWE history at WrestleMania Backlash on May 16, 2021. "
        "The heel run brought two NXT North American Championship reigns in 2023, then the "
        "Intercontinental Championship at WrestleMania 41 on April 20, 2025 &mdash; winning the "
        "fatal four-way by pinning Bron Breakker after Finn Balor's Coup de Grace inadvertently "
        "set it up, the accident the next year of Judgment Day television was built on. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">2</span>'
        '<span class="pull-cap">Intercontinental reigns &mdash; 204 days, then 93, both ended by men he '
        'had wronged</span></span>'
        "He held it 204 days, lost it to John Cena on the November 10, 2025 Raw &mdash; the win "
        "that completed Cena's Grand Slam &mdash; and took it back 19 days later at Survivor "
        "Series in his hometown of San Diego, one of the final losses of Cena's career. The AAA "
        "Mega Championship came in between: after AJ Styles' involvement helped wreck his first "
        "challenge at Triplemania XXXIII in August 2025, he beat El Hijo del Vikingo for it at "
        "Worlds Collide in Las Vegas on September 12, 2025, and has defended it since, including "
        "against Vikingo at Rey de Reyes on March 14, 2026.",

        "One sequence needs setting straight, because a biography summary in circulation has it "
        "backwards. That summary says Dominik <i>won</i> the NXT North American Championship on "
        "September 30, 2023 and <i>lost</i> it to Trick Williams on October 3. The champions-list "
        "table &mdash; where the reign arithmetic actually lives &mdash; says the reverse: "
        "<b>Trick Williams beat him at No Mercy on September 30</b>, ending a 74-day first reign, "
        "and <b>Dominik regained the title three days later</b> on the October 3 NXT, starting the "
        "67-day second reign Dragon Lee ended at Deadline on December 9. Only the table's order "
        "fits the reign lengths both sources quote, so that is the order this page publishes.",

        "The 2026 story is consequences. On the March 2 Raw he lost the Intercontinental "
        "Championship to Penta when Finn Balor stopped JD McDonagh handing him the hammer he "
        "wanted; the confrontation that followed got Balor beaten down and expelled from the "
        "Judgment Day, and got Dominik a date with <b>The Demon</b> at WrestleMania 42, where "
        "Balor put him through a table with the Coup de Grace to win their April 19 street fight. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">100K</span>'
        '<span class="pull-cap">the dollars Danhausen stole from the Judgment Day and then won outright '
        'in the SummerSlam Human Monies on a Pole match</span></span>'
        "The summer brought farce instead: Danhausen stole $100,000 from the Judgment Day, WWE "
        "literalised the dispute by hanging the cash above the ring at SummerSlam, and Danhausen "
        "climbed the pole on August 2. Dominik still leads what remains of the Judgment Day on "
        "Raw &mdash; McDonagh, Liv Morgan, Raquel Rodriguez &mdash; and his September is already "
        "booked: El Grande Americano challenges for the AAA Mega Championship at Triplemania 34 in "
        "Mexico City on September 13.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Curated ledger",
        promo_order=["WWE", "AAA"],
        promo_labels={"WWE": "WWE", "AAA": "AAA"},
        stats=[
            ("204", "Day IC reign"),
            ("2&times;", "Intercontinental"),
            ("353", "Days as AAA Mega Champion"),
            ("2&times;", "NXT North American"),
            ("1",   "Win over John Cena"),
            ("2005","First TV appearance"),
        ],
        lead=("Sixteen documented bouts &mdash; the title changes, the family matches and the "
              "Danhausen farce. This is a curated ledger, not a career count, and no career "
              "win&ndash;loss total is published because none is verified. The NXT North American "
              "sequence follows the champions-list table rather than the biography summary that "
              "reverses it; the AAA rows carry the AAA tab. Filter by match type, tap any column "
              "header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The bouts the reputation rests on. No star ratings are printed because none "
                    "were verified against Observer archives in this pass &mdash; these are "
                    "selected for what they meant, not how they were scored."),
    signature=[
        dict(rating="&mdash;", event="WrestleMania 39 Night 1", opponent="Rey Mysterio",
             stip="Father vs. son — the payoff of the best-built family feud of the decade"),
        dict(rating="&mdash;", event="WrestleMania 41 Night 2", opponent="Finn Balor, Penta & Bron Breakker",
             stip="Intercontinental Championship fatal four-way — the win that made him a champion heel"),
        dict(rating="&mdash;", event="Survivor Series 2025 — San Diego", opponent="John Cena",
             stip="Intercontinental Championship — beating Cena in his own hometown farewell tour"),
        dict(rating="&mdash;", event="WrestleMania 42 Night 2", opponent="The Demon Finn Balor",
             stip="Street fight — ten minutes of chairs, a 619 through a chair, and a table finish"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("2&times;", "Intercontinental reigns"),
            ("1",   "AAA Mega Championship"),
            ("2&times;", "NXT North American"),
            ("1",   "Tag title with Rey"),
        ],
        lead=("Six championship reigns across two companies, one of them still running: the AAA "
              "Mega Championship is at 353 days as of August 31, 2026, with a Triplemania defense "
              "booked for September 13."),
        rows=[
            dict(ic="A", name="AAA Mega Championship", count="1",
                 sub="September 12, 2025 &ndash; present &middot; def. El Hijo del Vikingo at "
                     "Worlds Collide: Las Vegas &middot; defended against Vikingo at Rey de Reyes "
                     "on March 14, 2026 &middot; <b>353 days and counting</b> as of August 31, "
                     "2026 &middot; El Grande Americano challenges at Triplemania 34 on September 13"),
            dict(ic="I", name="WWE Intercontinental Championship", count="2",
                 sub="April 20, 2025 &ndash; November 10, 2025 &middot; won the WrestleMania 41 "
                     "fatal four-way, lost to John Cena on Raw &middot; <b>204 days</b> &middot; "
                     "then November 29, 2025 &ndash; March 2, 2026 &middot; regained from Cena at "
                     "Survivor Series in San Diego, lost to Penta on Raw &middot; <b>93 days</b>"),
            dict(ic="N", name="NXT North American Championship", count="2",
                 sub="July 18, 2023 &ndash; September 30, 2023 &middot; def. Wes Lee, lost to Trick "
                     "Williams at No Mercy &middot; 74 days &middot; regained October 3, 2023, lost "
                     "to Dragon Lee at Deadline on December 9 &middot; 67 days &middot; a "
                     "circulating summary reverses the September 30 / October 3 order; the "
                     "champions-list table does not"),
            dict(ic="T", name="WWE SmackDown Tag Team Championship", count="1",
                 sub="May 16, 2021 &ndash; July 2021 &middot; won with Rey Mysterio at WrestleMania "
                     "Backlash from Dolph Ziggler and Robert Roode &middot; the first father-son "
                     "tag team champions in WWE history &middot; lost to The Usos"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Two acts: the family, and the family he chose to spite it.",
        cards=[
            dict(era="WWE &middot; 2020&ndash;2022",
                 name="The Mysterios",
                 members="Rey Mysterio, Dominik Mysterio",
                 desc="The father-son act that made history at WrestleMania Backlash on May 16, "
                      "2021 — the first father-son tag team champions WWE has ever had. It ended "
                      "the night of Clash at the Castle, September 3, 2022, when Dominik attacked "
                      "both Edge and his own father, and it stayed dead through the WrestleMania 39 "
                      "singles match Rey won on April 1, 2023."),
            dict(era="WWE &middot; 2022&ndash;present",
                 name="The Judgment Day",
                 members="Dominik Mysterio, JD McDonagh, Liv Morgan, Raquel Rodriguez; formerly "
                         "Finn Balor, Damian Priest, Rhea Ripley, Edge",
                 desc="He joined the group that recruited him away from his father on September 3, "
                      "2022 and outlasted every bigger name in it: Edge voted out in 2022, Priest "
                      "expelled in 2024, Rhea Ripley drifting off, and Finn Balor beaten down and "
                      "ousted in March 2026 after he cost Dominik the Intercontinental "
                      "Championship. What began as Dominik's adoptive family is now effectively "
                      "his faction — which the Danhausen money storyline treats as a small "
                      "criminal enterprise with $100,000 in petty cash."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One ring name, three characters: <b>the storyline kid</b> (2005) &rarr; <b>the "
             "dutiful son</b> (2019&ndash;2022) &rarr; <b>Dirty Dom</b> (2022&ndash;present).",
        cards=[
            dict(mono="05", era="WWE &middot; 2005", name="The kid in the custody angle",
                 desc="Eight years old, on television as the child at the centre of the Rey "
                      "Mysterio–Eddie Guerrero custody storyline that headlined SummerSlam 2005 in "
                      "a ladder match. No other active wrestler's character work leans this hard "
                      "on footage of themselves in elementary school."),
            dict(mono="DS", era="WWE &middot; 2019&ndash;2022", name="The dutiful son",
                 desc="Returned to the story as Rey's defender against Brock Lesnar in 2019, "
                      "debuted in-ring against Seth Rollins at SummerSlam on August 23, 2020, and "
                      "won tag gold with his father in 2021. Earnest, athletic, and — by his own "
                      "later admission in character — a prop in his father's career."),
            dict(mono="DD", era="WWE &middot; 2022&ndash;present", name="Dirty Dom",
                 desc="The Clash at the Castle turn, the prison cosplay after a storyline arrest, "
                      "the “Oscar” from Rhea Ripley, and a voice designed to be talked "
                      "over by boos. The joke with teeth: the character built on unearned "
                      "entitlement has quietly become one of the most decorated young champions on "
                      "the roster."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="From a storyline prop at eight to a two-company champion at 29.",
        rows=[
            dict(year="2005", title="The custody angle",
                 desc="Appears at eight as the child in the Rey Mysterio–Eddie Guerrero custody "
                      "storyline, culminating in the SummerSlam ladder match."),
            dict(year="2020", title="In-ring debut",
                 desc="Debuts against Seth Rollins at SummerSlam on August 23, 2020, at 23 years "
                      "old, without a developmental run."),
            dict(year="2021", title="History with his father",
                 desc="Wins the SmackDown Tag Team Championship with Rey at WrestleMania Backlash "
                      "on May 16 — the first father-son champions in WWE history."),
            dict(year="2022", title="The turn",
                 desc="Attacks Edge and Rey the night of Clash at the Castle, September 3, and "
                      "joins the Judgment Day."),
            dict(year="2023", title="Dirty Dom, champion",
                 desc="Loses to Rey at WrestleMania 39 on April 1; wins the NXT North American "
                      "Championship twice — July 18 from Wes Lee and October 3 from Trick "
                      "Williams — before Dragon Lee ends it at Deadline on December 9."),
            dict(year="2025", title="The Intercontinental year",
                 desc="Wins the IC title in the WrestleMania 41 fatal four-way on April 20; beats "
                      "AJ Styles at SummerSlam; wins the AAA Mega Championship from El Hijo del "
                      "Vikingo at Worlds Collide on September 12; loses the IC title to John Cena "
                      "on November 10 and regains it at Survivor Series on November 29."),
            dict(year="2026", title="Consequences",
                 desc="Loses the IC title to Penta on March 2 after Finn Balor withholds the "
                      "hammer; retains the AAA title at Rey de Reyes on March 14; loses the "
                      "WrestleMania 42 street fight to The Demon on April 19 and the Human Monies "
                      "on a Pole match to Danhausen at SummerSlam on August 2. Triplemania 34 "
                      "awaits on September 13."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Family, chosen family, and one demon of his own making.",
        cards=[
            dict(name="Rey Mysterio",
                 desc="The defining feud: the son who attacked his father at Clash at the Castle "
                      "on September 3, 2022 and spent months goading him — “deadbeat "
                      "dad” promos included — into the WrestleMania 39 match Rey won on "
                      "April 1, 2023. The angle worked because the family is real; the estrangement "
                      "is the character."),
            dict(name="Finn Balor", slug="finn-balor",
                 desc="Stablemate to nemesis across four years. Balor's stray Coup de Grace helped "
                      "hand Dominik the Intercontinental Championship at WrestleMania 41; Balor's "
                      "withheld hammer cost him the title against Penta on March 2, 2026; and "
                      "after the Judgment Day beat Balor down and threw him out, The Demon "
                      "answered with a table-breaking street fight win at WrestleMania 42 on "
                      "April 19."),
            dict(name="John Cena",
                 desc="Two title changes on Cena's farewell tour: Cena took the Intercontinental "
                      "Championship — and the last piece of his Grand Slam — on the November 10, "
                      "2025 Raw at Madison Square Garden's expense of Dominik's 204-day reign, and "
                      "Dominik took it back 19 days later at Survivor Series in San Diego, "
                      "becoming one of the final men to beat Cena."),
            dict(name="El Hijo del Vikingo",
                 desc="The AAA rivalry. Vikingo survived him at Triplemania XXXIII in August 2025 "
                      "amid AJ Styles' involvement, lost the Mega Championship at Worlds Collide "
                      "on September 12, and failed to regain it at Rey de Reyes on March 14, 2026. "
                      "El Grande Americano inherits the challenge at Triplemania 34."),
            dict(name="Danhausen",
                 desc="The comedy feud that cost real money: Danhausen stole $100,000 from the "
                      "Judgment Day, WWE hung the cash above the ring at SummerSlam Night 2, and "
                      "on August 2, 2026 Danhausen climbed the pole. Very nice, very evil, and — "
                      "for Dominik — very expensive."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Thin by design — the verified list is short, and nothing is added to pad it.",
        rows=[
            dict(when="2005", title="The SummerSlam 2005 custody angle", kind="Television",
                 desc="His first WWE appearance predates his debut by fifteen years — the "
                      "eight-year-old at the centre of the Rey Mysterio–Eddie Guerrero ladder "
                      "match storyline."),
            dict(when="2022&ndash;", title="WWE 2K", kind="Game",
                 desc="Playable in the current WWE 2K entries; his first appearance in the series "
                      "was not verified in this pass and is not claimed."),
            dict(when="2025&ndash;", title="Lucha Libre AAA", kind="Crossover",
                 desc="As Mega Champion he works both companies' television — Worlds Collide, Rey "
                      "de Reyes, and the September 13, 2026 Triplemania 34 defense — the most "
                      "prominent WWE-AAA crossover act since the companies' partnership began. No "
                      "film or scripted role could be verified, so none is listed."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated the way the sources state them &mdash; including the reversed "
             "sequence one summary gets wrong.",
        stats=[
            ("204", "Day IC reign"),
            ("353", "Days as AAA Mega Champion"),
            ("1st", "Father-son tag champions"),
        ],
        rows=[
            dict(name="First father-son tag team champions in WWE history",
                 sub="With Rey Mysterio, WrestleMania Backlash, May 16, 2021 — the record that can "
                     "only ever be tied, never taken."),
            dict(name="204 days as Intercontinental Champion",
                 sub="April 20 to November 10, 2025, the longer of his two reigns. Fightful marked "
                     "the 200-day milestone before John Cena ended it on Raw — the win that "
                     "completed Cena's Grand Slam, making Dominik a footnote in two histories at "
                     "once."),
            dict(name="AAA Mega Champion for 353 days and counting",
                 sub="Since beating El Hijo del Vikingo at Worlds Collide on September 12, 2025 — "
                     "held across a WWE Intercontinental reign, a WrestleMania loss and a "
                     "SummerSlam pole match, with the Triplemania 34 defense against El Grande "
                     "Americano set for September 13, 2026. Day count computed to August 31, "
                     "2026."),
            dict(name="Beat John Cena on the farewell tour",
                 sub="Survivor Series, November 29, 2025, in San Diego — his hometown — to regain "
                     "the Intercontinental Championship 19 days after losing it to Cena. Cena's "
                     "career ended two weeks later against Gunther."),
            dict(name="Two NXT North American reigns as a main-roster invader",
                 sub="74 days from July 18, 2023 and 67 from October 3, 2023 — per the "
                     "champions-list table, whose September 30 / October 3 order a circulating "
                     "biography summary reverses. Only the table's order fits the reign lengths "
                     "both sources quote."),
            dict(name="Held WWE and AAA gold simultaneously",
                 sub="From September 12, 2025 (Worlds Collide) to March 2, 2026 (the Penta loss), "
                     "he was Intercontinental Champion and AAA Mega Champion at once — 171 days "
                     "of double gold, computed from verified endpoints."),
            dict(name="The most-booed entrance pop in WWE",
                 sub="Not a measurable record and not published as one — but the “Dirty "
                     "Dom” reaction is the reason WWE keeps microphones near him, and it is "
                     "the asset every championship above rests on."),
        ],
        footnote=("Deliberately absent: a career win-loss total, which no source verifies; the "
                  "day-precision date of the Triplemania XXXIII loss, which was not re-verified; "
                  "and social handles, which were not verified in this pass."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography",
             href="https://en.wikipedia.org/wiki/Dominik_Mysterio"),
        dict(k="Wikipedia", v="List of NXT North American Champions — the reign table",
             href="https://en.wikipedia.org/wiki/List_of_NXT_North_American_Champions"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/dominik-mysterio"),
        dict(k="Fightful", v="Triplemania 34 Night Two — the El Grande Americano defense",
             href="https://www.fightful.com/wrestling/dominik-mysterio-vs-el-grande-americano-for-aaa-mega-title-confirmed-for-night-two-of-triplemania-34/"),
        dict(k="POST Wrestling", v="WrestleMania 42 — The Demon's street fight win",
             href="https://www.postwrestling.com/2026/04/19/demon-finn-balor-wins-street-fight-against-dominik-mysterio-at-wrestlemania-42/"),
        dict(k="The Sportster", v="SummerSlam 2026 Night 2 — the Human Monies on a Pole match",
             href="https://www.thesportster.com/wwe-summerslam-2026-night-2-results-recap-august-2-2026/"),
        dict(k="Yahoo Sports", v="The Danhausen stipulation explained",
             href="https://sports.yahoo.com/articles/wwe-makes-summerslam-match-stipulation-063824286.html"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Dominik Mysterio still the AAA Mega Champion?",
            a="Yes. As of August 31, 2026 he has held the AAA Mega Championship for 353 days, "
              "since beating El Hijo del Vikingo at Worlds Collide in Las Vegas on September 12, "
              "2025. He retained against Vikingo at Rey de Reyes on March 14, 2026, and his next "
              "defense is set: <b>El Grande Americano</b> at Triplemania 34, Night Two, at Arena "
              "CDMX in Mexico City on September 13, 2026.",
            q_ld="Is Dominik Mysterio still the AAA Mega Champion?",
            a_ld="Yes. As of August 31, 2026, Dominik Mysterio has held the AAA Mega Championship "
                 "for 353 days, having won it from El Hijo del Vikingo at Worlds Collide in Las "
                 "Vegas on September 12, 2025. He retained it against Vikingo at Rey de Reyes on "
                 "March 14, 2026, and is scheduled to defend it against El Grande Americano at "
                 "Triplemania 34 Night Two in Mexico City on September 13, 2026."),
        dict(
            q="How many times has Dominik Mysterio been Intercontinental Champion?",
            a="Twice. He won the title in the WrestleMania 41 fatal four-way on April 20, 2025 "
              "&mdash; over Finn Balor, Penta and Bron Breakker &mdash; and held it <b>204 "
              "days</b> until John Cena beat him on the November 10, 2025 Raw, completing Cena's "
              "Grand Slam. He regained it from Cena at Survivor Series in San Diego on November "
              "29, 2025 and held it 93 more days until Penta beat him on the March 2, 2026 Raw, "
              "in the match where Finn Balor refused to pass him the hammer.",
            q_ld="How many times has Dominik Mysterio been WWE Intercontinental Champion?",
            a_ld="Twice. Dominik Mysterio first won the WWE Intercontinental Championship in a "
                 "fatal four-way at WrestleMania 41 on April 20, 2025 and held it for 204 days "
                 "before losing to John Cena on the November 10, 2025 episode of Raw. He regained "
                 "the title from Cena at Survivor Series on November 29, 2025 in San Diego and "
                 "held it for 93 days until losing to Penta on the March 2, 2026 episode of Raw."),
        dict(
            q="What happened between Dominik Mysterio and Finn Balor?",
            a="A four-year partnership collapsed over a hammer. Balor's stray Coup de Grace helped "
              "Dominik win the Intercontinental title at WrestleMania 41; on the March 2, 2026 Raw, "
              "Balor stopped JD McDonagh from handing Dominik a hammer, and Dominik lost the title "
              "to Penta. In the confrontation that followed, Balor suggested Rey Mysterio had been "
              "right about his son &mdash; and the Judgment Day beat Balor down and threw him out. "
              "Balor answered at WrestleMania 42 on April 19, 2026, reviving The Demon and putting "
              "Dominik through a table with the Coup de Grace to win their street fight.",
            q_ld="Why did Finn Balor and Dominik Mysterio split, and who won at WrestleMania 42?",
            a_ld="Finn Balor was expelled from the Judgment Day in March 2026 after he prevented JD "
                 "McDonagh from handing Dominik Mysterio a hammer during the March 2, 2026 title "
                 "match Dominik lost to Penta, and then criticised Dominik in the confrontation "
                 "that followed. The Judgment Day attacked Balor and threw him out. At WrestleMania "
                 "42 on April 19, 2026, Balor returned as The Demon and defeated Dominik Mysterio "
                 "in a street fight, finishing with a Coup de Grace through a table."),
        dict(
            q="What is a Human Monies on a Pole match, and did Dominik win it?",
            a="A first-of-its-kind stipulation from SummerSlam 2026, and no, he did not. Danhausen "
              "had stolen $100,000 from the Judgment Day, so WWE hung the money above the ring at "
              "SummerSlam Night 2 on August 2, 2026, first climb wins. Danhausen retrieved it. The "
              "name is Danhausen's own grammar; the money, as of the bell, is Danhausen's own "
              "money.",
            q_ld="What was the Human Monies on a Pole match at SummerSlam 2026?",
            a_ld="The Human Monies on a Pole match at SummerSlam 2026 was a first-time stipulation "
                 "in which $100,000 that Danhausen had stolen from the Judgment Day was hung above "
                 "the ring, with the winner being the first to retrieve it. Danhausen defeated "
                 "Dominik Mysterio in the match on August 2, 2026, at SummerSlam Night 2 in "
                 "Minneapolis, and kept the money."),
        dict(
            q="Was Dominik Mysterio really on WWE TV as a child?",
            a="Yes &mdash; in 2005, at eight years old, as the child at the centre of the Rey "
              "Mysterio&ndash;Eddie Guerrero custody storyline, which climaxed in a ladder match "
              "at SummerSlam 2005 with his &ldquo;custody papers&rdquo; above the ring. His "
              "in-ring debut came fifteen years later, against Seth Rollins at SummerSlam on "
              "August 23, 2020. He is a third-generation wrestler: grandson of Rey Mysterio Sr., "
              "son of Rey Mysterio.",
            q_ld="Was Dominik Mysterio on WWE television as a child?",
            a_ld="Yes. In 2005, at age eight, Dominik Mysterio appeared on WWE television as the "
                 "child at the centre of the custody storyline between his father Rey Mysterio and "
                 "Eddie Guerrero, which culminated in a ladder match at SummerSlam 2005. His "
                 "in-ring debut came fifteen years later against Seth Rollins at SummerSlam on "
                 "August 23, 2020."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Dominik Oscar Gutierrez"),
        dict(label="Born", value="April 5, 1997", sub="San Diego, California &middot; age 29"),
        dict(label="Family", value="Son of Rey Mysterio",
             sub="third-generation &middot; grandson of Rey Mysterio Sr. &middot; married Marie "
                 "Juliette, March 7, 2024"),
        dict(label="Height", value="6&#8242;1&#8243;", sub="185 cm"),
        dict(label="Weight", value="200 lb", sub="91 kg (billed)"),
        dict(label="Debut", value="August 23, 2020", sub="SummerSlam, vs. Seth Rollins"),
        dict(label="First TV appearance", value="2005",
             sub="the Eddie Guerrero custody angle, at age eight"),
        dict(label="Signature", value="Frog splash &middot; 619 &middot; Three Amigos",
             sub="the family arsenal, used with maximum insolence"),
        dict(label="Brand", value="Raw", sub="also appearing for AAA as Mega Champion"),
        dict(label="Also known as", value="Dirty Dom &middot; &ldquo;Oscar&rdquo; (per Rhea Ripley)"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1997-04-05",
    bornplace="San Diego, California",
    nationality="United States",
    height_cm=185,
    weight_kg=91,
    ld=dict(
        alternateName=["Dominik Oscar Gutierrez", "Dirty Dom", "Dirty Dominik Mysterio"],
        award=["WWE Intercontinental Championship (2 reigns, 204 and 93 days)",
               "AAA Mega Championship (1 reign, current as of August 31, 2026)",
               "NXT North American Championship (2 reigns)",
               "WWE SmackDown Tag Team Championship (1 reign, with Rey Mysterio - first "
               "father-son champions in WWE history)"],
        knowsAbout=["Professional wrestling", "The Judgment Day", "WWE", "Lucha Libre AAA",
                    "NXT", "Championship wrestling"],
        description="Dominik Mysterio, born Dominik Oscar Gutierrez in San Diego, California, is "
                    "an American professional wrestler signed to WWE and the son of Rey Mysterio. "
                    "A member of the Judgment Day since September 2022, he is a two-time WWE "
                    "Intercontinental Champion, a two-time NXT North American Champion, and the "
                    "reigning AAA Mega Champion, a title he has held since September 12, 2025. "
                    "With Rey Mysterio he became half of the first father-son tag team champions "
                    "in WWE history in 2021.",
        sameAs=["https://en.wikipedia.org/wiki/Dominik_Mysterio",
                "https://www.wwe.com/superstars/dominik-mysterio"],
    ),
)
