# -*- coding: utf-8 -*-
"""Damian Priest - dossier data.

Sources: web research compiled August 31, 2026 - Wikipedia's Damian Priest article,
WWE.com's profile, Wrestling Inc.'s March 20 and August 21, 2026 SmackDown reports,
NoDQ's August 14, 2026 title-change report and Sportskeeda's Damian Priest Live piece.
Every match row carries a day-precision date stated in one of those sources.

Deliberate omissions:
  * No career win-loss total - no verified figure exists.
  * The exact date the Judgment Day regained the tag titles from Cody Rhodes and Jey Uso
    in October 2023 was not re-verified in this pass; the reign is described without it.
  * Ring of Honor reign dates (as Punishment Martinez) were not verified and are not
    invented.
  * No social handles - official accounts were not verified in this pass.
"""

# ----------------------------------------------------------------- record rows
# Title changes and turning points from NXT TakeOver XXX to the August 2026 tag title
# rematch. The February 28, 2022 date for the US title loss follows WWE's own video
# archive and the 191-day reign length; see the correction paragraph.
ROWS = [
    dict(result="W", date="2020-08-22", promo="WWE", type="tag", landmark=True,
         event="NXT TakeOver XXX", opponent="The five-man ladder field",
         stip="Ladder match — first title", title="NXT North American Championship"),
    dict(result="L", date="2020-10-28", promo="WWE",
         event="NXT Halloween Havoc", opponent="Johnny Gargano",
         stip="Devil's Playground match — the reign ends", title="NXT North American Championship"),
    dict(result="W", date="2021-04-10", promo="WWE", type="tag", landmark=True,
         event="WrestleMania 37 Night 1", opponent="The Miz & John Morrison",
         stip="Tag — with Bad Bunny", title=""),
    dict(result="W", date="2021-08-21", promo="WWE", landmark=True,
         event="SummerSlam — Las Vegas", opponent="Sheamus",
         stip="Singles — first main-roster title", title="WWE United States Championship"),
    dict(result="L", date="2022-02-28", promo="WWE",
         event="Raw", opponent="Finn Balor",
         stip="Singles — the 191-day reign ends; Priest snaps after",
         title="WWE United States Championship"),
    dict(result="W", date="2023-07-01", promo="WWE", type="tag", landmark=True,
         event="Money in the Bank — London", opponent="The six-man ladder field",
         stip="Money in the Bank ladder match", title=""),
    dict(result="W", date="2023-09-02", promo="WWE", type="tag",
         event="Payback", opponent="Kevin Owens & Sami Zayn",
         stip="Tag — with Finn Balor", title="Undisputed WWE Tag Team Championship"),
    dict(result="W", date="2024-04-07", promo="WWE", landmark=True,
         event="WrestleMania XL Night 2", opponent="Drew McIntyre",
         stip="Money in the Bank cash-in — minutes after McIntyre won the title",
         title="World Heavyweight Championship"),
    dict(result="W", date="2024-07-06", promo="WWE", landmark=True,
         event="Money in the Bank — Toronto", opponent="Gunther",
         stip="Singles — retains against the King of the Ring", title="World Heavyweight Championship"),
    dict(result="L", date="2024-08-03", promo="WWE", landmark=True,
         event="SummerSlam — Cleveland", opponent="Gunther",
         stip="Singles — the 118-day reign ends", title="World Heavyweight Championship"),
    dict(result="L", date="2025-04-20", promo="WWE",
         event="WrestleMania 41 Night 2", opponent="Drew McIntyre",
         stip="Sin City Street Fight", title=""),
    dict(result="W", date="2025-05-24", promo="WWE",
         event="Saturday Night's Main Event", opponent="Drew McIntyre",
         stip="Steel cage — ends the feud", title=""),
    dict(result="L", date="2025-10-10", promo="WWE",
         event="SmackDown", opponent="Aleister Black",
         stip="Last Man Standing — Zelina Vega interferes", title=""),
    dict(result="W", date="2026-01-02", promo="WWE",
         event="SmackDown", opponent="Aleister Black",
         stip="Ambulance match — ends the feud", title=""),
    dict(result="W", date="2026-03-20", promo="WWE", type="tag", landmark=True,
         event="SmackDown", opponent="The MFT (Tama Tonga & JC Mateo)",
         stip="Tag — with R-Truth; Truth pins Mateo", title="WWE Tag Team Championship"),
    dict(result="W", date="2026-06-19", promo="WWE", type="tag",
         event="SmackDown", opponent="Tama Tonga & Talla Tonga",
         stip="Tag — retain; Solo Sikoa's interference splinters the MFT",
         title="WWE Tag Team Championship"),
    dict(result="L", date="2026-08-14", promo="WWE", type="tag", landmark=True,
         event="SmackDown", opponent="The MFTs (Tama Tonga & Talla Tonga)",
         stip="Triple threat with The War Raiders — the 147-day reign ends",
         title="WWE Tag Team Championship"),
    dict(result="L", date="2026-08-21", promo="WWE", type="tag",
         event="SmackDown", opponent="The MFTs (Tama Tonga & Talla Tonga)",
         stip="Rematch — the Tongas hit the Red Cross on R-Truth",
         title="WWE Tag Team Championship"),
]

DATA = dict(
    slug="damian-priest",
    name="Damian Priest",
    realname="Luis Martinez",
    epithet="The Archer of Infamy",
    hook="Record & Titles",

    meta_desc=("Damian Priest, the Archer of Infamy, cashed in Money in the Bank at WrestleMania XL "
               "to win the World Heavyweight Championship and held it 118 days. Full record, titles, "
               "factions, records and career."),
    og_desc=("The Archer of Infamy: a WrestleMania cash-in, a 118-day World Heavyweight reign, a "
             "191-day US title run, three tag team championships and the Judgment Day years."),
    tw_desc="The Archer of Infamy: World Heavyweight Champion via WrestleMania cash-in, 118 days.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2005",
    height_imp="6&#8242;5&#8243;",
    weight_lb="249",
    world_titles="1",
    vitals_tagline="Live forever",
    support_note="Merch &middot; Games &middot; Watch",
    sp_items=[
        dict(ic="DP", title="WWE Shop", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable in the current 2K entries",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="24", title="Damian Priest: WWE 24", sub="Documentary · premiered August 2, 2024",
             tag="Watch", href="https://www.wwe.com/"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/damian-priest"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Archer of Infamy &middot; formerly Punishment Martinez &middot; ex-Judgment Day",
    hero_tag="New York City, raised in Vega Baja, Puerto Rico &middot; <em>Independents &middot; ROH "
             "&middot; NXT &middot; WWE &middot; 2005&ndash;present</em>",
    now_label="NOW",
    now_bold="SmackDown, no championship",
    now_tail=" &middot; dropped the WWE Tag Team Championship to the MFTs on August 14 and lost the "
             "rematch a week later, with visible tension building between him and R-Truth",
    hstats=[
        dict(value="118", x=False, label="Day World Title Reign"),
        dict(value="191", x=False, label="Day US Reign"),
        dict(value="3",   x=True,  label="Tag Team Titles"),
        dict(value="1",   x=False, label="MITB Cash-In"),
    ],
    ghost_link="From the Monster Factory of the indies to a WrestleMania cash-in",
    vlabel="Est. 2005 &middot; New York City",
    mono="DP",

    # ---------------------------------------------------------------- 01 overview
    # index into overview of the correction paragraph -> the framed
    # "Setting one thing straight" callout (aside.corr) on the page
    correction=2,
    overview=[
        "<b>Damian Priest</b> waited nineteen years for the twenty seconds that define him. A New "
        "Yorker raised in Vega Baja, Puerto Rico, he debuted on the East Coast independents in 2005, "
        "spent 2015 to 2018 in Ring of Honor as Punishment Martinez, and did not reach WWE's main "
        "roster until he was 38. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">118</span>'
        '<span class="pull-cap">days as World Heavyweight Champion in 2024, from a WrestleMania XL '
        'cash-in to the SummerSlam loss against Gunther</span></span>'
        "Then it compounded fast: the United States Championship for 191 days in 2021&ndash;22, the "
        "Money in the Bank briefcase in 2023, and the cash-in at WrestleMania XL on April 7, 2024 "
        "&mdash; moments after Drew McIntyre had won the World Heavyweight Championship and stopped "
        "to taunt CM Punk &mdash; that made him champion for 118 days. He is also a three-time tag "
        "team champion across two partners who could not be less alike: two reigns with Finn Balor "
        "at the Judgment Day's peak, and one in 2026 with R-Truth.",

        "The Judgment Day is the spine of the middle of the career. He joined at WrestleMania 38 in "
        "April 2022 as Edge's first recruit, helped vote Edge out that June, and spent two years as "
        "the group's enforcer and tag champion &mdash; until the group expelled <i>him</i> in August "
        "2024, days after Gunther took the world title off him at SummerSlam. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">3</span>'
        '<span class="pull-cap">tag team championship reigns &mdash; two with Finn Balor in the Judgment '
        'Day, one with R-Truth in 2026</span></span>'
        "The SmackDown move followed on January 24, 2025, and with it the two long feuds of his "
        "post-Judgment Day life: Drew McIntyre &mdash; the Sin City Street Fight loss at WrestleMania "
        "41 on April 20, 2025, answered with the steel cage win at Saturday Night's Main Event on May "
        "24 &mdash; and Aleister Black, a half-year blood feud that ran from a Last Man Standing loss "
        "on October 10, 2025 to the ambulance-match win that ended it on January 2, 2026.",

        "One date in circulation needs setting straight. A widely mirrored summary of his career "
        "dates the end of the United States Championship reign to February 21, 2022 &mdash; while "
        "also calling it a 191-day reign. Those two facts cannot both be true: 191 days from the "
        "SummerSlam win on August 21, 2021 lands on <b>February 28, 2022</b>, and WWE's own video "
        "archive titles the footage &ldquo;Damian Priest snaps after Finn Balor wins the United "
        "States Title: Raw, Feb. 28, 2022.&rdquo; This page publishes February 28 and treats the "
        "arithmetic and the primary source as the citation. The &ldquo;snaps&rdquo; part matters "
        "too: that loss triggered the heel turn that eventually delivered him to the Judgment Day.",

        "The 2026 chapter is the odd couple. Paired with the 54-year-old R-Truth, he won the WWE Tag "
        "Team Championship from the MFT's Tama Tonga and JC Mateo on the March 20 SmackDown &mdash; "
        "R-Truth pinning Mateo with, of all things, John Cena's Attitude Adjustment &mdash; and held "
        "it 147 days through the MFT's collapse, including the June 19 defense Solo Sikoa's "
        "interference wrecked for the challengers. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">147</span>'
        '<span class="pull-cap">days as WWE Tag Team Champions with R-Truth in 2026, ended by the '
        'Tongas&rsquo; triple-threat win on August 14</span></span>'
        "Tama and Talla Tonga took the titles back in a triple threat with the War Raiders on August "
        "14, 2026 and beat Priest and R-Truth clean in the rematch a week later, hitting the Red "
        "Cross on Truth. Wrestling Inc.'s report of the rematch noted Priest was &ldquo;noticeably "
        "unhappy with his partner&rdquo; afterward &mdash; but still helped him up. As of August 31, "
        "2026 he holds no championship, and whether the partnership survives September is the "
        "question his television time is being spent on.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Curated ledger",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("118", "Day world title reign"),
            ("191", "Day US reign"),
            ("3&times;", "Tag team champion"),
            ("147", "Day tag reign with R-Truth"),
            ("1",   "Money in the Bank"),
            ("2",   "Ladder-match titles"),
        ],
        lead=("Eighteen documented bouts &mdash; the title changes, the cash-in, and the feud "
              "bookends. This is a curated ledger, not a career count, and no career win&ndash;loss "
              "total is published because none is verified. The February 28, 2022 United States "
              "title loss follows WWE's own video archive and the 191-day reign arithmetic rather "
              "than the February 21 date some summaries carry. Filter by match type, tap any column "
              "header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The bouts the reputation rests on. No star ratings are printed because none "
                    "were verified against Observer archives in this pass &mdash; these are selected "
                    "for what they meant, not how they were scored."),
    signature=[
        dict(rating="&mdash;", event="WrestleMania XL Night 2", opponent="Drew McIntyre",
             stip="Money in the Bank cash-in — the World Heavyweight Championship in under a minute"),
        dict(rating="&mdash;", event="SummerSlam 2024 — Cleveland", opponent="Gunther",
             stip="World Heavyweight Championship — the 118-day reign ends by technical submission"),
        dict(rating="&mdash;", event="Money in the Bank 2024 — Toronto", opponent="Gunther",
             stip="World Heavyweight Championship — the defense he won before the rematch he lost"),
        dict(rating="&mdash;", event="WrestleMania 41 Night 2", opponent="Drew McIntyre",
             stip="Sin City Street Fight — the feud WWE built two stipulation matches to finish"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("1",   "World title reign"),
            ("191", "Day US reign"),
            ("3&times;", "Tag team reigns"),
            ("1",   "NXT North American"),
        ],
        lead=("Six WWE championship reigns and a Ring of Honor run under another name. Both of his "
              "singles titles ended in matches that changed his direction: the US loss triggered the "
              "heel turn, the world title loss triggered his expulsion from the Judgment Day."),
        rows=[
            dict(ic="H", name="World Heavyweight Championship", count="1",
                 sub="April 7, 2024 &ndash; August 3, 2024 &middot; won by Money in the Bank cash-in "
                     "on Drew McIntyre at WrestleMania XL, lost to Gunther at SummerSlam by technical "
                     "submission &middot; <b>118 days</b>"),
            dict(ic="U", name="WWE United States Championship", count="1",
                 sub="August 21, 2021 &ndash; February 28, 2022 &middot; def. Sheamus at SummerSlam, "
                     "lost to Finn Balor on Raw &middot; <b>191 days</b> &middot; a mirrored summary's "
                     "February 21 end date contradicts its own reign length and is not published here"),
            dict(ic="T", name="WWE Tag Team Championship", count="1",
                 sub="March 20, 2026 &ndash; August 14, 2026 &middot; won with R-Truth from the MFT's "
                     "Tama Tonga and JC Mateo on SmackDown, lost to Tama and Talla Tonga in a triple "
                     "threat with the War Raiders &middot; <b>147 days</b>"),
            dict(ic="J", name="Undisputed WWE Tag Team Championship", count="2",
                 sub="With Finn Balor &middot; won from Kevin Owens and Sami Zayn at Payback on "
                     "September 2, 2023; the reigns bracket a brief October 2023 interruption by Cody "
                     "Rhodes and Jey Uso, whose exact regain date was not re-verified in this pass; "
                     "ended in the WrestleMania XL Night 1 six-pack ladder match on April 6, 2024"),
            dict(ic="N", name="NXT North American Championship", count="1",
                 sub="August 22, 2020 &ndash; October 28, 2020 &middot; won the TakeOver XXX ladder "
                     "match, lost to Johnny Gargano in a Devil's Playground match"),
            dict(ic="R", name="ROH World Television Championship", count="1",
                 sub="As Punishment Martinez &middot; reign dates not verified in this pass and not "
                     "invented"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="One faction, three phases: recruit, enforcer, expelled champion.",
        cards=[
            dict(era="WWE &middot; 2022",
                 name="The Judgment Day — Edge's version",
                 members="Edge, Damian Priest, Rhea Ripley",
                 desc="Priest was the founding recruit, joining Edge at WrestleMania 38 in April "
                      "2022. The recruitment pitch was rebirth for a stalled career, and it worked "
                      "in the least expected way: within two months, Priest, Ripley and new arrival "
                      "Finn Balor voted Edge out of his own group."),
            dict(era="WWE &middot; 2022&ndash;2024",
                 name="The Judgment Day — the peak",
                 members="Damian Priest, Finn Balor, Rhea Ripley, Dominik Mysterio, JD McDonagh",
                 desc="The group's imperial phase, with Priest as its heavy and half of its tag "
                      "championship: two Undisputed WWE Tag Team title reigns with Balor from "
                      "September 2023 to April 2024, plus the Money in the Bank briefcase he carried "
                      "for nine months. The internal tension — Balor eyeing the briefcase, Priest "
                      "eyeing the exits — was the best long-form character work of the group's run."),
            dict(era="WWE &middot; 2024",
                 name="The expulsion",
                 members="Priest out; Balor, Mysterio, McDonagh, Morgan, Rodriguez in",
                 desc="Days after Gunther beat him at SummerSlam 2024, the Judgment Day threw him "
                      "out, with Finn Balor leading the coup — the exact mirror of what they had "
                      "done to Edge. Priest left as a babyface, feuded with the group into the "
                      "autumn, and moved to SmackDown on January 24, 2025."),
            dict(era="WWE &middot; 2026&ndash;present",
                 name="With R-Truth",
                 members="Damian Priest, R-Truth",
                 desc="Not a faction — a comedy-and-violence tag team that won real gold. Truth's "
                      "Attitude Adjustment on JC Mateo won the WWE Tag Team Championship on March "
                      "20, 2026; the pair held it 147 days. Since losing the titles and the August "
                      "21 rematch, Priest's frustration with his partner has been the on-screen "
                      "story, and WWE reporting has openly speculated about a heel turn."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Three names in twenty-one years: <b>Damian Martinez</b> on the early independents "
             "&rarr; <b>Punishment Martinez</b> in Ring of Honor (2015&ndash;2018) &rarr; <b>Damian "
             "Priest</b> from NXT in 2018 onward.",
        cards=[
            dict(mono="DM", era="Independents &middot; 2005&ndash;2015", name="Damian Martinez",
                 desc="A decade of East Coast independents before anyone was watching — the long "
                      "apprenticeship that makes him one of the latest bloomers among modern WWE "
                      "champions."),
            dict(mono="PM", era="Ring of Honor &middot; 2015&ndash;2018", name="Punishment Martinez",
                 desc="The breakout: a 6'5\" agile heavy in ROH, where he became World Television "
                      "Champion. The silhouette of the WWE character — gothic, long-limbed, "
                      "spin-kick-heavy — was built here."),
            dict(mono="AP", era="WWE &middot; 2018&ndash;present", name="Damian Priest, the Archer of Infamy",
                 desc="Signed in 2018, rebuilt in NXT, main roster from February 1, 2021 with a win "
                      "over The Miz. The archer imagery, the “live forever” catchphrase and "
                      "the rock-star aura carried him from Bad Bunny's WrestleMania partner to world "
                      "champion inside four years."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Nineteen years to the main roster, then the fastest four years of his life.",
        rows=[
            dict(year="2005", title="Debut",
                 desc="Starts on the East Coast independents at 23."),
            dict(year="2015", title="Ring of Honor",
                 desc="Debuts as Punishment Martinez; becomes ROH World Television Champion before "
                      "leaving for WWE."),
            dict(year="2020", title="NXT North American Champion",
                 desc="Wins the TakeOver XXX ladder match on August 22; loses the title to Johnny "
                      "Gargano at Halloween Havoc on October 28."),
            dict(year="2021", title="Main roster, Bad Bunny, US title",
                 desc="Debuts February 1 beating The Miz; wins the WrestleMania 37 tag with Bad "
                      "Bunny on April 10; beats Sheamus for the United States Championship at "
                      "SummerSlam on August 21."),
            dict(year="2022", title="The snap and the Judgment Day",
                 desc="Loses the US title to Finn Balor on February 28 and turns; joins Edge's "
                      "Judgment Day at WrestleMania 38; helps vote Edge out in June."),
            dict(year="2023", title="Senor Money in the Bank",
                 desc="Wins the briefcase in London on July 1; wins the Undisputed WWE Tag Team "
                      "Championship with Balor at Payback on September 2."),
            dict(year="2024", title="World champion, then expelled",
                 desc="Cashes in on Drew McIntyre at WrestleMania XL on April 7; retains against "
                      "Gunther at Money in the Bank on July 6; loses to Gunther at SummerSlam on "
                      "August 3 and is thrown out of the Judgment Day days later."),
            dict(year="2025", title="SmackDown, McIntyre, Black",
                 desc="Moves to SmackDown January 24; loses the WrestleMania 41 street fight to "
                      "McIntyre on April 20 but wins the May 24 steel cage; opens the Aleister "
                      "Black blood feud, losing the October 10 Last Man Standing match."),
            dict(year="2026", title="Tag gold with R-Truth",
                 desc="Closes the Black feud in the January 2 ambulance match; wins the WWE Tag "
                      "Team Championship with R-Truth on March 20; loses it to the Tongas on August "
                      "14 and the rematch on August 21."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Gunther", slug="gunther",
                 desc="The defining championship rivalry: Priest beat him at Money in the Bank on "
                      "July 6, 2024 in Toronto, and Gunther took the World Heavyweight Championship "
                      "by technical submission at SummerSlam on August 3 — the loss that ended the "
                      "118-day reign and, within days, his Judgment Day membership."),
            dict(name="Drew McIntyre",
                 desc="Two years of unfinished business in three stipulations. Priest's WrestleMania "
                      "XL cash-in stole the title McIntyre had held for five minutes; McIntyre took "
                      "the WrestleMania 41 Sin City Street Fight on April 20, 2025; Priest closed it "
                      "inside a steel cage at Saturday Night's Main Event on May 24, 2025."),
            dict(name="Aleister Black",
                 desc="The blood feud of his SmackDown run, from June 2025 to January 2026. Black "
                      "took the Last Man Standing match on October 10, 2025 with Zelina Vega's "
                      "help; Priest ended it by winning the ambulance match on the January 2, 2026 "
                      "SmackDown."),
            dict(name="Finn Balor", slug="finn-balor",
                 desc="Partner and nemesis in alternating order: Balor took his US title on "
                      "February 28, 2022 and triggered the heel turn; then they held the tag titles "
                      "together twice; then Balor led the vote that expelled him in August 2024. No "
                      "WWE relationship of his has produced more plot."),
            dict(name="The MFTs",
                 desc="The 2026 tag rivalry. Priest and R-Truth beat Tama Tonga and JC Mateo for "
                      "the titles on March 20, retained against the Tongas on June 19 when Solo "
                      "Sikoa's interference backfired on his own men, then lost the titles in the "
                      "August 14 triple threat and the August 21 rematch — with Haku at ringside "
                      "and the Red Cross double powerbomb as the full stop."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Thin by design — the verified list is short, and nothing is added to pad it.",
        rows=[
            dict(when="2024", title="Damian Priest: WWE 24", kind="Documentary",
                 desc="The career documentary premiered August 2, 2024 at the Damian Priest Live "
                      "event at The Agora in Cleveland during SummerSlam weekend, with a panel "
                      "alongside Rhea Ripley and Dominik Mysterio and interviews with Triple H, The "
                      "Undertaker and Paul Heyman."),
            dict(when="2021", title="The Bad Bunny partnership", kind="Crossover",
                 desc="Tag partner for Bad Bunny's celebrated WrestleMania 37 match against The Miz "
                      "and John Morrison — the crossover that put Priest in front of a global "
                      "non-wrestling audience two months into his main-roster run."),
            dict(when="2021&ndash;", title="WWE 2K", kind="Game",
                 desc="Playable in the current WWE 2K entries; his first appearance in the series "
                      "was not verified in this pass and is not claimed."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated the way the sources state them &mdash; with the one bad date in "
             "circulation corrected.",
        stats=[
            ("118", "Days as world champion"),
            ("191", "Days as US Champion"),
            ("147", "Days as tag champion in 2026"),
        ],
        rows=[
            dict(name="Won the World Heavyweight Championship by WrestleMania cash-in",
                 sub="April 7, 2024, WrestleMania XL Night 2 — cashed in Money in the Bank on Drew "
                     "McIntyre minutes after McIntyre beat Seth Rollins for the title and stopped to "
                     "taunt CM Punk. Held it 118 days, with a successful defense against Gunther at "
                     "Money in the Bank before the SummerSlam rematch went the other way."),
            dict(name="191 days as United States Champion",
                 sub="August 21, 2021 to February 28, 2022, from beating Sheamus at SummerSlam to "
                     "losing to Finn Balor on Raw. The February 21 end date carried by one mirrored "
                     "summary contradicts its own 191-day figure and WWE's video archive, and is "
                     "not published anywhere on this page."),
            dict(name="Three tag team championship reigns with two partners",
                 sub="Two Undisputed WWE Tag Team reigns with Finn Balor (2023-24) and the 147-day "
                     "WWE Tag Team reign with R-Truth (March 20 to August 14, 2026). Wrestling "
                     "Inc. notes the R-Truth reign made both men three-time tag champions."),
            dict(name="Two titles won in ladder matches",
                 sub="The NXT North American Championship at TakeOver XXX on August 22, 2020, and "
                     "the Money in the Bank briefcase in London on July 1, 2023."),
            dict(name="Beat Gunther before Gunther beat him",
                 sub="The July 6, 2024 Money in the Bank defense is one of the few singles losses "
                     "in Gunther's 2024, and the SummerSlam reversal four weeks later is the loss "
                     "Priest's entire second act pivots on."),
            dict(name="Founding member — and second expellee — of the Judgment Day",
                 sub="Joined Edge at WrestleMania 38, helped vote Edge out two months later, and "
                     "was himself voted out in August 2024. The group has now expelled two of its "
                     "own founders; Priest is both of them minus one."),
            dict(name="Main-roster champion after a nineteen-year climb",
                 sub="Debuted 2005; first main-roster title August 2021; world champion April 2024, "
                     "at 41 — one of the oldest first-time world champions of WWE's modern era. His "
                     "age at the cash-in is computed from his September 26, 1982 birth date."),
        ],
        footnote=("Deliberately absent: a career win-loss total, which no source verifies; exact "
                  "dates for the Ring of Honor and October 2023 tag-title-regain reigns, which were "
                  "not re-verified in this pass; and social handles, which were not verified "
                  "either."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Damian_Priest"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/damian-priest"),
        dict(k="Wrestling Inc.", v="March 20, 2026 — Priest and R-Truth win the WWE Tag Team Championship",
             href="https://www.wrestlinginc.com/2128495/wwe-smackdown-damian-priest-r-truth-mfts-tag-team-championship/"),
        dict(k="NoDQ", v="August 14, 2026 — the Tongas take the titles in a triple threat",
             href="https://nodq.com/news/tama-and-talla-tonga-capture-the-wwe-tag-team-titles-on-smackdown/"),
        dict(k="Wrestling Inc.", v="August 21, 2026 — the rematch, and the Priest–R-Truth tension",
             href="https://www.wrestlinginc.com/2242038/wwe-smackdown-mft-damian-priest-r-truth-first-defense-tag-titles/"),
        dict(k="Sportskeeda", v="Damian Priest Live and the WWE 24 documentary",
             href="https://sportskeeda.com/wwe/what-damian-priest-live-all-need-know-newest-addition-wwe-summerslam-weekend"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="How did Damian Priest win the World Heavyweight Championship?",
            a="By cashing in Money in the Bank at WrestleMania XL on April 7, 2024. Drew McIntyre "
              "had just beaten Seth Rollins for the title and paused to taunt CM Punk at ringside; "
              "Punk attacked McIntyre, Priest's music hit, and the cash-in match was over in under "
              "a minute. He held the championship for <b>118 days</b>, beating Gunther at Money in "
              "the Bank on July 6 before losing it to him at SummerSlam on August 3, 2024 by "
              "technical submission.",
            q_ld="How did Damian Priest win the World Heavyweight Championship?",
            a_ld="Damian Priest won the World Heavyweight Championship by cashing in his Money in "
                 "the Bank contract at WrestleMania XL on April 7, 2024, immediately after Drew "
                 "McIntyre defeated Seth Rollins for the title. CM Punk attacked McIntyre after "
                 "McIntyre taunted him at ringside, and Priest won the cash-in match in under a "
                 "minute. Priest held the title for 118 days, retaining against Gunther at Money in "
                 "the Bank on July 6, 2024 before losing it to Gunther at SummerSlam on August 3, "
                 "2024."),
        dict(
            q="Why was Damian Priest kicked out of the Judgment Day?",
            a="Because the group ate its founder a second time. Priest was Edge's first recruit at "
              "WrestleMania 38, helped vote Edge out in June 2022, and became the stable's enforcer "
              "and tag champion. Days after Gunther beat him for the World Heavyweight Championship "
              "at SummerSlam 2024, the Judgment Day &mdash; with Finn Balor at the front &mdash; "
              "expelled him exactly as he had helped expel Edge. He left as a babyface and moved to "
              "SmackDown on January 24, 2025.",
            q_ld="Why was Damian Priest expelled from the Judgment Day?",
            a_ld="The Judgment Day expelled Damian Priest in August 2024, shortly after he lost the "
                 "World Heavyweight Championship to Gunther at SummerSlam 2024, with Finn Balor "
                 "leading the move. It mirrored Priest's own history with the group: he had joined "
                 "as Edge's first recruit at WrestleMania 38 in April 2022 and helped vote Edge out "
                 "in June 2022. After the expulsion Priest turned babyface and moved to SmackDown "
                 "on January 24, 2025."),
        dict(
            q="Is Damian Priest still a tag team champion with R-Truth?",
            a="No. The 147-day reign ended on the August 14, 2026 SmackDown, when the MFTs "
              "&mdash; Tama Tonga and Talla Tonga, with their father Haku at ringside &mdash; won a "
              "triple threat that also involved the War Raiders, pinning R-Truth after the Red "
              "Cross double powerbomb. Priest and Truth got the rematch a week later on August 21 "
              "and lost that too. Priest was visibly frustrated with his partner afterward, and "
              "the state of the team is the current story.",
            q_ld="Is Damian Priest still a WWE Tag Team Champion with R-Truth?",
            a_ld="No. Damian Priest and R-Truth lost the WWE Tag Team Championship to Tama Tonga "
                 "and Talla Tonga of the MFTs on the August 14, 2026 episode of SmackDown, in a "
                 "triple threat match that also included the War Raiders, ending their reign at 147 "
                 "days. They lost the rematch on August 21, 2026, and tension between Priest and "
                 "R-Truth has been part of the storyline since."),
        dict(
            q="When did Damian Priest lose the United States Championship &mdash; February 21 or 28, 2022?",
            a="<b>February 28, 2022</b>, to Finn Balor on Raw. A widely mirrored career summary "
              "says February 21 while also calling it a 191-day reign &mdash; but 191 days from the "
              "August 21, 2021 SummerSlam win is February 28, and WWE's own video archive dates the "
              "footage of the loss, and of Priest snapping afterward, to February 28. The snap "
              "matters more than the date: it started the heel run that led to the Judgment Day.",
            q_ld="When did Damian Priest lose the United States Championship?",
            a_ld="Damian Priest lost the WWE United States Championship to Finn Balor on the "
                 "February 28, 2022 episode of Raw, ending a 191-day reign that began at SummerSlam "
                 "on August 21, 2021. Some summaries give February 21, 2022, but that date is "
                 "inconsistent with the 191-day reign length, and WWE's own video archive dates the "
                 "title change to February 28, 2022."),
        dict(
            q="What is Damian Priest's real name and background?",
            a="Luis Martinez, born September 26, 1982 in New York City and raised in Vega Baja, "
              "Puerto Rico. He debuted in 2005, wrestled Ring of Honor as Punishment Martinez from "
              "2015 to 2018 and became ROH World Television Champion, then signed with WWE in 2018. "
              "The finisher, South of Heaven, is named after the Slayer album &mdash; the metal "
              "obsession is genuine, not gimmick.",
            q_ld="What is Damian Priest's real name and background?",
            a_ld="Damian Priest's real name is Luis Martinez. He was born September 26, 1982 in New "
                 "York City and raised in Vega Baja, Puerto Rico. He debuted on the independents in "
                 "2005, wrestled in Ring of Honor as Punishment Martinez from 2015 to 2018, where "
                 "he held the ROH World Television Championship, and signed with WWE in 2018. His "
                 "finishing move, South of Heaven, is named after the Slayer album."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Luis Martinez"),
        dict(label="Born", value="September 26, 1982",
             sub="New York City &middot; raised in Vega Baja, Puerto Rico &middot; age 43"),
        dict(label="Height", value="6&#8242;5&#8243;", sub="196 cm &middot; per WWE.com"),
        dict(label="Weight", value="249 lb", sub="113 kg (billed)"),
        dict(label="Debut", value="2005", sub="East Coast independents"),
        dict(label="Ring names", value="Damian Martinez &rarr; Punishment Martinez &rarr; Damian Priest",
             sub="independents &middot; ROH 2015&ndash;18 &middot; WWE 2018&ndash;present"),
        dict(label="Signature", value="South of Heaven &middot; Reckoning &middot; Broken Arrow",
             sub="per WWE.com; South of Heaven is named for the Slayer album"),
        dict(label="Catchphrase", value="&ldquo;Live forever&rdquo;"),
        dict(label="Brand", value="SmackDown", sub="since January 24, 2025"),
        dict(label="Also known as", value="The Archer of Infamy &middot; Senor Money in the Bank (2023&ndash;24)"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1982-09-26",
    bornplace="New York City, United States",
    nationality="United States",
    height_cm=196,
    weight_kg=113,
    ld=dict(
        alternateName=["Luis Martinez", "Punishment Martinez", "The Archer of Infamy"],
        award=["World Heavyweight Championship (1 reign, 118 days)",
               "WWE United States Championship (1 reign, 191 days)",
               "Undisputed WWE Tag Team Championship (2 reigns, with Finn Balor)",
               "WWE Tag Team Championship (1 reign, 147 days, with R-Truth)",
               "NXT North American Championship (1 reign)",
               "ROH World Television Championship (1 reign, as Punishment Martinez)",
               "Men's Money in the Bank (2023)"],
        knowsAbout=["Professional wrestling", "The Judgment Day", "WWE", "NXT", "Ring of Honor",
                    "Championship wrestling"],
        description="Damian Priest, born Luis Martinez in New York City and raised in Vega Baja, "
                    "Puerto Rico, is an American professional wrestler signed to WWE. He won the "
                    "2023 Men's Money in the Bank contract and cashed it in at WrestleMania XL on "
                    "April 7, 2024 to win the World Heavyweight Championship, which he held for 118 "
                    "days. A former United States Champion for 191 days and three-time tag team "
                    "champion, he wrestled in Ring of Honor as Punishment Martinez and was a "
                    "founding member of the Judgment Day.",
        sameAs=["https://en.wikipedia.org/wiki/Damian_Priest",
                "https://www.wwe.com/superstars/damian-priest"],
    ),
)
