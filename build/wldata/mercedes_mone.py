# -*- coding: utf-8 -*-
"""Mercedes Mone - dossier data.

Compiled August 31, 2026, one day after she won the AEW Women's World Championship
at All In: London. Sources are the web pages opened for this build (Wrestling Inc.,
POST Wrestling, F4W, SEScoops, Fox News, eWrestlingNews, 411Mania, Bleacher Report)
plus verified career history. Nothing is invented; where publishers disagree the
conflict is printed rather than resolved.

Deliberate omissions:
  * No career win-loss total. Cagematch was not consulted and no verified aggregate
    exists in the sources opened for this pass.
  * The exact end mechanism and date of the IWGP Women's Championship reign (2023)
    is stated only as far as the sources support: the reign ended around the May
    2023 ankle injury and she did not lose the belt in the ring.
  * Reign lengths for most of the 2025 independent collection are not published
    individually; the SEScoops tracker's win dates are used and the April 4, 2026
    zero-titles endpoint is POST Wrestling's.
"""

# ----------------------------------------------------------------- record rows
# Seventeen documented bouts: the NXT/WWE landmarks as Sasha Banks, the NJPW and
# CMLL chapters, and the AEW arc through All In: London on August 30, 2026.
ROWS = [
    dict(result="W", date="2015-02-11", promo="WWE", type="tag", landmark=True,
         event="NXT TakeOver: Rival", opponent="Charlotte, Bayley & Becky Lynch",
         stip="Fatal four-way, as Sasha Banks — her first championship in WWE",
         title="NXT Women's Championship"),
    dict(result="L", date="2015-10-07", promo="WWE", landmark=True,
         event="NXT TakeOver: Respect", opponent="Bayley", opponent_html=True,
         stip="30-minute Iron Man match — the first women's Iron Man match in WWE, "
              "and the first women's main event of a TakeOver",
         title="NXT Women's Championship"),
    dict(result="W", date="2016-07-25", promo="WWE", landmark=True,
         event="Raw", opponent="Charlotte",
         stip="Singles — the first of four Raw Women's Championship reigns",
         title="WWE Raw Women's Championship"),
    dict(result="L", date="2016-10-30", promo="WWE", landmark=True,
         event="Hell in a Cell", opponent="Charlotte Flair",
         stip="The first women's Hell in a Cell match, and the first women's match "
              "to main event a WWE pay-per-view",
         title="WWE Raw Women's Championship"),
    dict(result="W", date="2019-02-17", promo="WWE", type="tag", landmark=True,
         event="Elimination Chamber", opponent="Five other teams",
         stip="Tag team Elimination Chamber, with Bayley — the inaugural champions",
         title="WWE Women's Tag Team Championship"),
    dict(result="W", date="2020-10-25", promo="WWE", landmark=True,
         event="Hell in a Cell", opponent="Bayley", opponent_html=True,
         stip="Hell in a Cell — the Boss 'n' Hug breakup blowoff",
         title="WWE SmackDown Women's Championship"),
    dict(result="L", date="2021-04-10", promo="WWE", landmark=True,
         event="WrestleMania 37 Night 1", opponent="Bianca Belair", opponent2_html=True,
         stip="Main event — the first two Black women to main event WrestleMania",
         title="WWE SmackDown Women's Championship"),
    dict(result="W", date="2023-02-18", promo="NJPW", landmark=True,
         event="NJPW Battle in the Valley — San Jose", opponent="KAIRI",
         stip="Her first match after walking out of WWE, debuting as Mercedes Mone",
         title="IWGP Women's Championship"),
    dict(result="L", date="2023-05-21", promo="NJPW",
         event="NJPW Resurgence", opponent="Willow Nightingale",
         stip="Match one of the Willow series — decision match for the inaugural "
              "title; the ankle injury that cost her nearly a year",
         title="NJPW Strong Women's Championship"),
    dict(result="W", date="2024-05-26", promo="AEW", landmark=True,
         event="Double or Nothing — Las Vegas", opponent="Willow Nightingale",
         stip="AEW in-ring debut — the 584-day TBS reign begins",
         title="AEW TBS Championship"),
    dict(result="W", date="2025-05-25", promo="AEW",
         event="Double or Nothing — Glendale", opponent="Jamie Hayter",
         stip="Owen Hart Cup final — earns the All In: Texas title shot", title=""),
    dict(result="W", date="2025-06-18", promo="AEW",
         event="Grand Slam: Mexico — Arena Mexico", opponent="Zeuxis",
         stip="Singles — a CMLL title won on an AEW show",
         title="CMLL World Women's Championship"),
    dict(result="L", date="2025-07-12", promo="AEW",
         event="All In: Texas", opponent="Toni Storm",
         stip="Singles — the challenge comes up short", title="AEW Women's World Championship"),
    dict(result="L", date="2025-12-31", promo="AEW", landmark=True,
         event="Dynamite — New Year's Eve", opponent="Willow Nightingale",
         stip="Singles — the 584-day TBS reign ends and the collection starts to fall",
         title="AEW TBS Championship"),
    dict(result="L", date="2026-03-06", promo="AEW",
         event="CMLL La Noche de las Amazonas", opponent="Persephone",
         stip="Singles — springboard frog splash ends the CMLL reign",
         title="CMLL World Women's Championship"),
    dict(result="W", date="2026-06-28", promo="AEW",
         event="Forbidden Door — San Jose", opponent="Maya World",
         stip="Owen Hart Cup final — the first two-time winner", title=""),
    dict(result="W", date="2026-08-30", promo="AEW", landmark=True,
         event="All In: London — Wembley Stadium", opponent="Willow Nightingale",
         stip="Statement Maker — her first AEW Women's World Championship",
         title="AEW Women's World Championship"),
]

# opponent_html rows carry a real <a>, so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Bayley": "bayley"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True
    if _r.pop("opponent2_html", False):
        _slug = {"Bianca Belair": "bianca-belair"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="mercedes-mone",
    name="Mercedes Mone",
    realname="Mercedes Justine Kaestner-Varnado",
    epithet="The CEO",
    hook="Record & Titles",

    meta_desc=("Mercedes Mone, The CEO, won the AEW Women's World Championship at All In: London on "
               "August 30, 2026 — after holding a record 13 belts at once and then losing every one of "
               "them. Full record, titles, factions, records and career."),
    og_desc=("The CEO: 13 championships held at once, a 584-day TBS reign, five WWE world title reigns "
             "as Sasha Banks, and — as of August 30, 2026 — her first AEW Women's World Championship."),
    tw_desc="The CEO: 13 belts at once, then zero, then the one that mattered — AEW Women's World Champion.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2010",
    height_imp="5&#8242;5&#8243;",
    weight_lb="114",
    world_titles="6",
    vitals_tagline="The CEO",
    support_note="Merch &middot; Games &middot; Watch",
    x_url="https://x.com/MercedesVarnado",
    ig_url="https://www.instagram.com/mercedesvarnado/",
    sp_items=[
        dict(ic="MM", title="Mercedes Mone Merch", sub="Official tees · ShopAEW",
             tag="Shop", href="https://www.shopaew.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable as Sasha Banks, 2K17–2K23",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="SW", title="The Mandalorian", sub="Koska Reeves · Season 2",
             tag="Watch", href="https://en.wikipedia.org/wiki/The_Mandalorian"),
        dict(ic="AEW", title="Official Roster Page", sub="AllEliteWrestling.com", tag="Visit", charity=True,
             href="https://www.allelitewrestling.com/aew-roster"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Boss &middot; The Legit Boss &middot; The Belt Collector &middot; formerly Sasha Banks",
    hero_tag="Fairfield, California &middot; <em>Chaotic Wrestling &middot; WWE &middot; NJPW &middot; "
             "AEW &middot; 2010&ndash;present</em>",
    now_label="NOW",
    now_bold="AEW Women's World Champion — day two of her first reign",
    now_tail=" &middot; beat Willow Nightingale at All In: London on August 30, 2026, fourteen months "
             "after failing against Toni Storm at the same event",
    hstats=[
        dict(value="13",  x=False, label="Belts Held at Once"),
        dict(value="584", x=False, label="Day TBS Reign"),
        dict(value="6",   x=True,  label="World Title Reigns"),
        dict(value="2",   x=True,  label="Owen Hart Cups"),
    ],
    ghost_link="From Mercedes KV to the one belt that outweighed thirteen",
    vlabel="Est. 2010 &middot; Fairfield, California",
    mono="MM",

    # ---------------------------------------------------------------- 01 overview
    # index into overview of the correction paragraph -> the framed
    # "Setting one thing straight" callout (aside.corr) on the page
    correction=1,
    overview=[
        "<b>Mercedes Mone</b> won the AEW Women's World Championship on August 30, 2026, submitting "
        "Willow Nightingale with the Statement Maker in the co-main event of All In: London at Wembley "
        "Stadium, and it is the first time in her AEW run that she has held the belt that actually sits "
        "at the top of the company. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">1</span>'
        '<span class="pull-cap">championship held as of August 31, 2026 &mdash; the AEW Women&rsquo;s World title, and nothing else</span></span>'
        "That sentence needs the second half: she holds exactly one championship today. The wrestler who "
        "spent 2025 setting a record by holding <b>thirteen belts simultaneously</b> arrived at All In "
        "with none at all, and the story of how the collection was built, why it collapsed, and what "
        "replaced it is the real shape of the last two years of her career.",

        "The line that will trail this page is &ldquo;Mercedes Mone, holder of a dozen championships.&rdquo; "
        "It is out of date, and the correction runs in both directions. At the peak &mdash; reached at "
        "Full Gear in November 2025 &mdash; she held a record <b>13 titles at once</b>, spanning AEW, "
        "CMLL, RevPro, and independent promotions from Denmark to Poland to Malaysia, with the Owen Hart "
        "Cup counted among them by the trackers that kept score. Then it all went: the interim ROH "
        "Women's World Television Championship to Red Velvet on December 5, 2025; the TBS Championship "
        "to Willow Nightingale on the New Year's Eve Dynamite, ending a 584-day reign; the CMLL World "
        "Women's Championship to Persephone on March 6, 2026; a run of independent belts to Alex "
        "Windsor, Jody Threat and others through the spring. On <b>April 4, 2026</b>, when she vacated "
        "the APAC Women's Championship over what 411Mania reported as budgetary issues, POST Wrestling "
        "recorded her as holding <b>no active championship at all</b>. As of August 31, 2026 the "
        "accurate count is <b>one</b> &mdash; and it is the first one of her AEW career that says "
        "&ldquo;World&rdquo; on it.",

        "She was born Mercedes Justine Kaestner-Varnado on January 26, 1992 in Fairfield, California, "
        "and debuted in 2010 for Chaotic Wrestling in Massachusetts as Mercedes KV. WWE signed her in "
        "August 2012 and made her <b>Sasha Banks</b>, The Boss: an NXT Women's Championship won in the "
        "four-way at TakeOver: Rival in February 2015, the Brooklyn and Iron Man classics with Bayley "
        "that made the women's revolution undeniable, four Raw Women's Championship reigns, the first "
        "women's Hell in a Cell match and the first women's main event of a WWE pay-per-view in 2016, "
        "the inaugural WWE Women's Tag Team Championship with Bayley in 2019, and the WrestleMania 37 "
        "main event against Bianca Belair &mdash; the first WrestleMania main event between two Black "
        "women. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">2022</span>'
        '<span class="pull-cap">the year she and Naomi walked out of Raw as tag champions &mdash; she never wrestled for WWE again</span></span>'
        "On May 16, 2022, she and Naomi &mdash; the reigning Women's Tag Team Champions &mdash; walked "
        "out of Raw over a creative dispute. She never wrestled for WWE again, resurfacing at Wrestle "
        "Kingdom 17 on January 4, 2023 as Mercedes Mone and beating KAIRI for the IWGP Women's "
        "Championship in San Jose that February.",

        "The AEW chapter has been a long setup with a one-night payoff. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">584</span>'
        '<span class="pull-cap">days as TBS Champion, from Double or Nothing 2024 to the New Year&rsquo;s Eve Dynamite &mdash; the longest reign in the title&rsquo;s history</span></span>'
        "She debuted at Big Business in Boston in March 2024, beat Willow Nightingale for the TBS "
        "Championship at Double or Nothing that May, and spent 2025 collecting belts on five countries' "
        "worth of independent shows while losing the only match that mattered &mdash; the All In: Texas "
        "challenge to Toni Storm on July 12, 2025. In 2026 the arc inverted: every belt gone by April, "
        "then a second straight Owen Hart Cup at Forbidden Door on June 28 &mdash; the first wrestler "
        "to win it twice &mdash; and then Wembley, where she and Nightingale ended their series at 2-2, "
        "Mone bleeding from the nose and Nightingale passing out in the hold rather than tapping. She "
        "is champion for the first morning of her reign as this page is compiled, with a Willow rematch "
        "the obvious first defense and nothing yet announced.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Highlight set",
        promo_order=["WWE", "NJPW", "AEW"],
        promo_labels={"WWE": "WWE", "NJPW": "NJPW", "AEW": "AEW"},
        stats=[
            ("13",       "Belts held at once"),
            ("584",      "Day TBS reign"),
            ("5&times;", "WWE world reigns"),
            ("1",        "AEW Women's World reign"),
            ("2&times;", "Owen Hart Cup"),
            ("2&ndash;2", "Willow series"),
        ],
        lead=("Seventeen documented bouts &mdash; a curated highlight set, not a career count, and no "
              "career win&ndash;loss total is published because none was verified. The WWE years are "
              "listed under the Sasha Banks name she worked them under; the row dates are day-precise "
              "and each is carried by at least one source opened for this build. One counting caution "
              "runs through everything here: the famous &ldquo;13 championships&rdquo; is a "
              "simultaneous-holdings record as the trackers scored it &mdash; the Owen Hart Cup's "
              "ceremonial belt included &mdash; not a count of title reigns. Filter by match type, tap "
              "any column header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("Four bouts the reputation rests on. The ratings are this dossier's own editorial "
                    "grades, not Wrestling Observer figures &mdash; no Meltzer ratings were verified in "
                    "this pass and none are quoted."),
    signature=[
        dict(rating="4.5", event="NXT TakeOver: Brooklyn 2015", opponent="Bayley",
             stip="NXT Women's Championship — the match that made the revolution undeniable"),
        dict(rating="4.5", event="NXT TakeOver: Respect 2015", opponent="Bayley",
             stip="30-minute Iron Man main event — NXT Women's Championship"),
        dict(rating="4.0", event="Hell in a Cell 2016", opponent="Charlotte Flair",
             stip="First women's Hell in a Cell match — Raw Women's Championship"),
        dict(rating="4.0", event="All In: London 2026", opponent="Willow Nightingale",
             stip="AEW Women's World Championship — the payoff, 22 minutes at Wembley"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("13",       "Belts held at once"),
            ("1",        "Held today"),
            ("5&times;", "WWE world reigns"),
            ("3&times;", "WWE tag reigns"),
        ],
        lead=("Championships across five companies and three continents, listed by lineage. The 2025 "
              "independent collection is grouped in one row because that is how it lived and died: "
              "won in a rush across the year, gone in another rush between December 2025 and April "
              "2026. As of August 31, 2026 she holds exactly one belt, and it is the top one."),
        rows=[
            dict(ic="A", name="AEW Women's World Championship", count="1",
                 sub="Won August 30, 2026 at All In: London, submitting Willow Nightingale with the "
                     "Statement Maker in front of Wembley Stadium &middot; her first reign, one day old "
                     "as this page is compiled &middot; earned via the 2026 Owen Hart Cup"),
            dict(ic="T", name="AEW TBS Championship", count="1",
                 sub="May 26, 2024 &ndash; December 31, 2025 &middot; won from Willow Nightingale in her "
                     "AEW in-ring debut at Double or Nothing, lost back to Nightingale on the New "
                     "Year's Eve Dynamite &middot; <b>584 days</b>, computed from those dates &mdash; "
                     "the longest reign in the title's history"),
            dict(ic="I", name="IWGP Women's Championship", count="1",
                 sub="Won February 18, 2023 from KAIRI at NJPW Battle in the Valley in San Jose, her "
                     "first match after leaving WWE &middot; the reign ended around the May 2023 ankle "
                     "injury suffered against Willow Nightingale at Resurgence &mdash; she did not lose "
                     "the belt in the ring"),
            dict(ic="S", name="NJPW Strong Women's Championship", count="1",
                 sub="Won June 30, 2024 from Stephanie Vaquer at Forbidden Door in a winner-take-all "
                     "match while TBS Champion &middot; lost to AZM at NJPW Resurgence in May 2025"),
            dict(ic="C", name="CMLL World Women's Championship", count="1",
                 sub="June 18, 2025 &ndash; March 6, 2026 &middot; won from Zeuxis at AEW Grand Slam: "
                     "Mexico in Arena Mexico, lost to Persephone at La Noche de las Amazonas &middot; "
                     "261 days by the dates, 262 as eWrestlingNews counts it, with three defenses"),
            dict(ic="R", name="WWE Raw Women's Championship", count="4",
                 sub="All as Sasha Banks &middot; three reigns in 2016 &mdash; the first won July 25 on "
                     "Raw from Charlotte &mdash; and a fourth at SummerSlam 2017 &middot; every one "
                     "ended within weeks; the reigns were short and the matches were the point"),
            dict(ic="D", name="WWE SmackDown Women's Championship", count="1",
                 sub="October 25, 2020 &ndash; April 10, 2021 &middot; won from Bayley inside Hell in a "
                     "Cell, lost to Bianca Belair in the WrestleMania 37 Night 1 main event"),
            dict(ic="G", name="WWE Women's Tag Team Championship", count="3",
                 sub="Inaugural champions with Bayley at Elimination Chamber on February 17, 2019 "
                     "&middot; a second reign with Bayley in 2020 &middot; a third with Naomi, won at "
                     "WrestleMania 38 &mdash; the reign that ended with the May 16, 2022 walkout, after "
                     "which WWE stripped the titles"),
            dict(ic="N", name="NXT Women's Championship", count="1",
                 sub="February 11, 2015 &ndash; August 22, 2015 &middot; won in the TakeOver: Rival "
                     "four-way, lost to Bayley at TakeOver: Brooklyn"),
            dict(ic="X", name="The 2025 collection", count="9",
                 sub="Chaotic Wrestling (a 2025 return to the title she first won there), EWA, Prime "
                     "Time Wrestling, BestYa, Discovery Wrestling Scottish, Bodyslam, Winnipeg Pro, "
                     "APAC and RevPro's Undisputed British Championship, plus an interim ROH Women's "
                     "World Television reign &middot; all gone between December 5, 2025 and April 4, "
                     "2026, the last of them &mdash; APAC &mdash; vacated over what 411Mania reported "
                     "as budgetary issues"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="One press label that was never a stable, two booked WWE units, and an AEW entourage.",
        cards=[
            dict(era="NXT &middot; 2013&ndash;15 &middot; press framing, not a booked unit",
                 name="The Four Horsewomen",
                 members="Sasha Banks, Charlotte Flair, Becky Lynch, Bayley",
                 desc="The legitimate framing with the standard caveat: never an on-screen alliance, "
                      "never booked as a unit. The name is a media and fan label for the four women who "
                      "came up through NXT together between 2013 and 2015, echoing Ric Flair's Four "
                      "Horsemen. What it describes is real — the four matches those four had with each "
                      "other rebuilt the division — and Banks' TakeOver: Rival win in the four-way that "
                      "contained all four of them is where this page's ledger starts."),
            dict(era="WWE &middot; 2015&ndash;16",
                 name="Team B.A.D.",
                 members="Sasha Banks, Naomi, Tamina",
                 desc="Her faction during the 2015 \"Divas Revolution\" three-way war against Team PCB "
                      "and Team Bella. It dissolved as Banks moved into the Charlotte title series, but "
                      "the Naomi alliance it created resurfaced twice: the 2022 tag championship, and "
                      "the walkout that ended both of their WWE runs."),
            dict(era="WWE &middot; 2016&ndash;20",
                 name="The Boss 'n' Hug Connection",
                 members="Sasha Banks, Bayley",
                 desc="The most consequential relationship of her career: inaugural WWE Women's Tag Team "
                      "Champions at Elimination Chamber 2019, a second reign in 2020, and then the slow "
                      "on-screen betrayal that produced the Hell in a Cell 2020 match where Banks took "
                      "the SmackDown Women's Championship from her. Friends, champions, enemies — in "
                      "that order, twice."),
            dict(era="AEW &middot; 2024&ndash;25",
                 name="The CEO's office",
                 members="Mercedes Mone, Kamille",
                 desc="Not a faction so much as an executive with security: Kamille worked as Mone's "
                      "hired enforcer through the first year of the TBS reign. The pairing wound down "
                      "as 2025 went on — the exact end date is not verified in this pass — and Mone "
                      "has worked the collection era and the 2026 rebuild alone."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Three names in sixteen years, and the third one she built herself &mdash; "
             "<b>Mercedes KV</b> (2010&ndash;12) &rarr; <b>Sasha Banks</b> (2012&ndash;22) &rarr; "
             "<b>Mercedes Mone</b> (2023&ndash;present).",
        cards=[
            dict(mono="KV", era="Chaotic Wrestling &middot; 2010&ndash;12", name="Mercedes KV",
                 desc="The teenage New England independent run, built at Chaotic Wrestling in "
                      "Massachusetts, where she won her first championship. She returned to the same "
                      "promotion's title in March 2025 as a belt-collection stop — a deliberate "
                      "full-circle flourish."),
            dict(mono="SB", era="WWE &middot; 2012&ndash;22", name="Sasha Banks, The Boss",
                 desc="The name WWE gave her and the character that made her famous: swagger, rings, "
                      "and a claim to being the best wrestler in the building that the Bayley series "
                      "kept proving true. Five world title reigns, the 2016 firsts, the inaugural tag "
                      "titles, the WrestleMania 37 main event — and an ending with no match at all, "
                      "walking out of Raw on May 16, 2022 as a champion."),
            dict(mono="MM", era="NJPW, AEW &middot; 2023&ndash;present", name="Mercedes Mone, The CEO",
                 desc="The self-owned rebrand — the money pun spelled without the accent on this site — "
                      "debuting at Wrestle Kingdom 17 and built explicitly as a business: The CEO, "
                      "eight-figure contract talk, championships as acquisitions. AEW from March 2024."),
            dict(mono="BC", era="AEW and everywhere else &middot; 2024&ndash;26", name="The Belt Collector",
                 desc="A layer on top of The CEO rather than a replacement: through 2025 she treated "
                      "every independent title within reach as a portfolio position, peaking at a "
                      "record thirteen at once after Full Gear in November 2025. The gimmick's honest "
                      "epilogue is that the portfolio went to zero by April 4, 2026 — and the character "
                      "won the one belt that mattered four months later."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Fairfield to Wembley, with a record-setting detour through every belt she could reach.",
        rows=[
            dict(year="2010", title="Debuts as Mercedes KV",
                 desc="Starts at Chaotic Wrestling in Massachusetts, winning her first championship "
                      "there before WWE signs her in August 2012."),
            dict(year="2015", title="The NXT year",
                 desc="Wins the NXT Women's Championship in the TakeOver: Rival four-way on February "
                      "11, then loses the Brooklyn and Iron Man classics to Bayley — the matches that "
                      "made the women's revolution a main-event proposition."),
            dict(year="2016", title="Three Raw title reigns and two firsts",
                 desc="Trades the Raw Women's Championship with Charlotte three times, then loses the "
                      "first women's Hell in a Cell match on October 30 — the first women's main event "
                      "of a WWE pay-per-view."),
            dict(year="2019", title="Inaugural tag champion",
                 desc="Wins the first WWE Women's Tag Team Championship with Bayley in the Elimination "
                      "Chamber on February 17."),
            dict(year="2020", title="SmackDown Women's Champion",
                 desc="Beats Bayley inside Hell in a Cell on October 25 and holds the title into the "
                      "WrestleMania 37 main event against Bianca Belair — the first between two Black "
                      "women — which she loses on April 10, 2021."),
            dict(year="2022", title="The walkout",
                 desc="Walks out of Raw on May 16 with tag partner Naomi over a creative dispute, "
                      "while champions. WWE strips the titles; she never wrestles for the company "
                      "again."),
            dict(year="2023", title="Mercedes Mone, IWGP Women's Champion",
                 desc="Debuts at Wrestle Kingdom 17 on January 4, beats KAIRI for the IWGP Women's "
                      "Championship in San Jose on February 18, then shatters her ankle against Willow "
                      "Nightingale at Resurgence in May — out for nearly a year."),
            dict(year="2024", title="AEW, and the 584-day reign begins",
                 desc="Debuts at Big Business in Boston in March, beats Nightingale for the TBS "
                      "Championship at Double or Nothing on May 26, and adds the NJPW Strong Women's "
                      "title from Stephanie Vaquer at Forbidden Door."),
            dict(year="2025", title="Thirteen belts, and the one that got away",
                 desc="Wins the Owen Hart Cup, the CMLL World Women's Championship and a shelf of "
                      "independent titles, peaking at a record thirteen at once — but loses the All "
                      "In: Texas world title match to Toni Storm on July 12, and drops the TBS title "
                      "to Nightingale on New Year's Eve."),
            dict(year="2026", title="Zero to one",
                 desc="Loses or vacates everything by April 4. Wins a second straight Owen Hart Cup at "
                      "Forbidden Door on June 28 — the first two-time winner — and beats Nightingale "
                      "at All In: London on August 30 for her first AEW Women's World Championship."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who she went to war with.",
        cards=[
            dict(name="Bayley", slug="bayley",
                 desc="The defining series of her career and arguably of the entire women's revolution: "
                      "Brooklyn 2015, the 30-minute Iron Man at TakeOver: Respect — the first women's "
                      "TakeOver main event — the inaugural tag championship together in 2019, and the "
                      "betrayal that ended at Hell in a Cell 2020 with Banks taking the SmackDown "
                      "title. Ten years of friend-enemy-friend, currently dormant across two "
                      "companies."),
            dict(name="Charlotte Flair",
                 desc="The 2016 rivalry that carried Raw's new women's division: three title changes "
                      "in six months, the first women's Hell in a Cell match, and the first women's "
                      "main event of a WWE pay-per-view on October 30, 2016 — a match Banks lost, "
                      "which is the detail the anniversary retellings tend to soften."),
            dict(name="Bianca Belair", slug="bianca-belair",
                 desc="One match that mattered more than most careers: the WrestleMania 37 Night 1 "
                      "main event on April 10, 2021, the first WrestleMania main event between two "
                      "Black women, which Belair won. It is the biggest match Banks ever lost, and "
                      "the one she is most associated with winning anyway — as a moment."),
            dict(name="Willow Nightingale",
                 desc="The AEW-era arch-rival, now level at 2-2 across three years and two companies: "
                      "Nightingale won the 2023 Resurgence match where Mone's ankle gave out, Mone "
                      "took the TBS title from her at Double or Nothing 2024, Nightingale took it back "
                      "on New Year's Eve 2025, and Mone submitted her at Wembley on August 30, 2026 "
                      "for the AEW Women's World Championship. A rematch is the obvious first "
                      "defense; nothing is announced."),
            dict(name="Toni Storm",
                 desc="The one she has not solved. Storm beat her clean at All In: Texas on July 12, "
                      "2025 with the world title on the line — the loss that made the whole thirteen-"
                      "belt collection read as compensation. Mone finally winning the title a year "
                      "later, against someone else, leaves this the obvious unfinished business in "
                      "the division."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Beyond the ring.",
        rows=[
            dict(when="2020", title="The Mandalorian", kind="TV",
                 desc="Koska Reeves in season two of the Disney+ series — two episodes, and still the "
                      "most prominent scripted acting role of any active women's wrestler of her "
                      "generation."),
            dict(when="2016&ndash;2023", title="WWE 2K", kind="Game",
                 desc="Playable as Sasha Banks from WWE 2K17 through WWE 2K23, with the 2K23 "
                      "appearance shipping after her walkout. No AEW video game appearance is "
                      "verified in this pass, so none is listed."),
            dict(when="2019&ndash;", title="Hip-hop and fashion crossovers", kind="Culture",
                 desc="A first cousin of Snoop Dogg — who rapped her to the ring at WrestleMania 32 "
                      "and has appeared on-screen with her since — and a recurring presence in "
                      "fashion and sneaker press as The CEO brand. Reported business ventures beyond "
                      "merchandise were not verified for this page and are not listed."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated with their counting rules attached &mdash; because almost every "
             "number attached to her name depends on what you count.",
        stats=[
            ("13",  "Belts held at once"),
            ("584", "Day TBS reign"),
            ("2",   "Owen Hart Cups"),
        ],
        rows=[
            dict(name="A record 13 championships held simultaneously",
                 sub="Reached by Full Gear in November 2025, spanning AEW, CMLL, RevPro, ROH (interim) "
                     "and independents across Denmark, Poland, Scotland, Canada, Malaysia-based APAC "
                     "and the US — as scored by trackers that counted the Owen Hart Cup's ceremonial "
                     "belt among them. It is a simultaneous-holdings record, not a reign count, and by "
                     "April 4, 2026 every one of them was gone."),
            dict(name="Longest TBS Championship reign in history — 584 days",
                 sub="May 26, 2024 to December 31, 2025, computed from the verified endpoints; won and "
                     "lost against the same person, Willow Nightingale."),
            dict(name="First AEW Women's World Championship, August 30, 2026",
                 sub="All In: London, submitting Nightingale with the Statement Maker in roughly 22 "
                     "minutes. F4W frames it as her first major world title run since her WWE "
                     "SmackDown Women's Championship reign of 2020-21."),
            dict(name="First two-time Owen Hart Cup winner",
                 sub="2025 (beating Jamie Hayter in the final at Double or Nothing) and 2026 (beating "
                     "Maya World in the final at Forbidden Door on June 28) — per Fox News, the first "
                     "wrestler to win the women's tournament twice."),
            dict(name="Half of the first women's main event of a WWE pay-per-view",
                 sub="Hell in a Cell, October 30, 2016, against Charlotte Flair — also the first "
                     "women's Hell in a Cell match. She lost it, a fact the milestone framing "
                     "routinely omits."),
            dict(name="Inaugural WWE Women's Tag Team Champion",
                 sub="With Bayley, in the tag team Elimination Chamber on February 17, 2019."),
            dict(name="Half of the first WrestleMania main event between two Black women",
                 sub="WrestleMania 37 Night 1, April 10, 2021, against Bianca Belair — a milestone "
                     "the two of them share exactly evenly, and another headline match she lost."),
            dict(name="Championships in WWE, NJPW, CMLL, ROH and AEW",
                 sub="Five distinct major-promotion lineages across three countries, plus the 2025 "
                     "independent collection. Stated as a list rather than a superlative — no "
                     "\"only wrestler ever\" claim is verified, so none is made."),
        ],
        footnote=("Two absences are deliberate. No career win-loss total appears anywhere on this page "
                  "— Cagematch was not consulted and no verified aggregate exists in the sources "
                  "opened for this build. And no Wrestling Observer star ratings are quoted: the "
                  "signature-match grades above are this dossier's own."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="X / Twitter", v="@MercedesVarnado", href="https://x.com/MercedesVarnado"),
        dict(k="Instagram", v="@mercedesvarnado", href="https://www.instagram.com/mercedesvarnado/"),
        dict(k="Wrestling Inc.", v="All In: London — the title win",
             href="https://www.wrestlinginc.com/2247145/aew-all-in-london-2026-mercedes-mone-willow-nightingale-beats-captures-world-title/"),
        dict(k="POST Wrestling", v="All In: London — the Statement Maker finish",
             href="https://www.postwrestling.com/2026/08/30/mercedes-mone-puts-willow-nightingale-to-sleep-captures-aew-womens-world-championship-at-all-in-2026/"),
        dict(k="POST Wrestling", v="April 2026 — down to zero active titles",
             href="https://www.postwrestling.com/2026/04/04/mercedes-mone-left-with-no-active-titles-after-vacating-apac-womens-championship/"),
        dict(k="SEScoops", v="The championship tracker at eleven, December 2025",
             href="https://www.sescoops.com/article/mercedes-mone-championship-tracker"),
        dict(k="Fox News", v="Forbidden Door 2026 — a second Owen Hart Cup",
             href="https://www.foxnews.com/sports/mercedes-mone-wins-owen-hart-womens-tournament-aew-forbidden-door-earns-title-shot"),
        dict(k="eWrestlingNews", v="Losing the CMLL World Women's Championship",
             href="https://www.ewrestlingnews.com/news/aew/mercedes-mone-loses-cmll-world-womens-championship"),
        dict(k="F4W", v="All In: London — first Women's World title",
             href="https://www.f4wonline.com/news/aew/mercedes-mone-women-world-title-aew-all-in-2026-willow-nightingale/"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/mercedes-mone.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="How many championships does Mercedes Mone hold right now?",
            a="<b>One</b> &mdash; the AEW Women's World Championship, won from Willow Nightingale at "
              "All In: London on August 30, 2026. The &ldquo;dozen belts&rdquo; image is over: at her "
              "peak, reached around Full Gear in November 2025, she held a record <b>13 titles "
              "simultaneously</b>, but every one of them was lost or vacated between December 5, 2025 "
              "and April 4, 2026, when POST Wrestling recorded her as holding no active championship at "
              "all after she vacated the APAC Women's Championship. The one she holds today is the "
              "first of the whole AEW run that says World on it.",
            q_ld="How many championships does Mercedes Mone hold right now?",
            a_ld="As of August 31, 2026, Mercedes Mone holds exactly one championship: the AEW Women's "
                 "World Championship, which she won from Willow Nightingale at All In: London on August "
                 "30, 2026. At her peak in November 2025 she held a record 13 titles simultaneously, "
                 "but she lost or vacated all of them between December 5, 2025 and April 4, 2026, when "
                 "she vacated the APAC Women's Championship and was left with no active titles. The "
                 "AEW Women's World Championship is her first reign with that title."),
        dict(
            q="Is Mercedes Mone the same person as Sasha Banks?",
            a="Yes. She wrestled for WWE from 2012 to 2022 as <b>Sasha Banks</b> &mdash; five world "
              "title reigns, the inaugural Women's Tag Team Championship with Bayley, the 2016 Hell in "
              "a Cell firsts and the WrestleMania 37 main event. On May 16, 2022 she and tag partner "
              "Naomi walked out of Raw over a creative dispute while holding the tag titles, and she "
              "never wrestled for WWE again. She resurfaced at NJPW's Wrestle Kingdom 17 on January 4, "
              "2023 under her real first name as <b>Mercedes Mone</b> &mdash; a name she owns.",
            q_ld="Is Mercedes Mone the same person as Sasha Banks?",
            a_ld="Yes. Mercedes Mone wrestled for WWE from 2012 to 2022 as Sasha Banks, winning five "
                 "world championships, the inaugural WWE Women's Tag Team Championship with Bayley, and "
                 "main-eventing WrestleMania 37. On May 16, 2022 she and Naomi walked out of Raw over a "
                 "creative dispute while holding the Women's Tag Team Championship, and she never "
                 "wrestled for WWE again. She debuted for New Japan Pro-Wrestling at Wrestle Kingdom 17 "
                 "on January 4, 2023 as Mercedes Mone."),
        dict(
            q="What happened to the 13 belts?",
            a="They fell almost as fast as they were won. The interim ROH Women's World Television "
              "Championship went to Red Velvet on December 5, 2025; the TBS Championship went back to "
              "Willow Nightingale on the New Year's Eve Dynamite, ending the 584-day reign; the CMLL "
              "World Women's Championship went to Persephone on March 6, 2026; and a string of "
              "independent titles went to Alex Windsor, Jody Threat and others through the spring. The "
              "end came on <b>April 4, 2026</b>, when she vacated the APAC Women's Championship &mdash; "
              "over budgetary issues, per 411Mania &mdash; and was left with nothing but the ceremonial "
              "Owen Hart Cup belt. Four months later she won the AEW Women's World Championship.",
            q_ld="What happened to the 13 championships Mercedes Mone held?",
            a_ld="Mercedes Mone lost or vacated all 13 championships between December 2025 and April "
                 "2026. She lost the interim ROH Women's World Television Championship to Red Velvet on "
                 "December 5, 2025, the TBS Championship to Willow Nightingale on December 31, 2025 "
                 "after 584 days, and the CMLL World Women's Championship to Persephone on March 6, "
                 "2026, with a series of independent titles lost to Alex Windsor, Jody Threat and "
                 "others. On April 4, 2026 she vacated the APAC Women's Championship, reportedly over "
                 "budgetary issues, leaving her with no active titles until she won the AEW Women's "
                 "World Championship on August 30, 2026."),
        dict(
            q="What is her record against Willow Nightingale?",
            a="Level: <b>2-2</b> across three years and two companies. Nightingale beat her at NJPW "
              "Resurgence on May 21, 2023 &mdash; the match where Mone's ankle gave out &mdash; to "
              "become the inaugural Strong Women's Champion; Mone took the TBS Championship from her at "
              "Double or Nothing on May 26, 2024; Nightingale took it back on the December 31, 2025 "
              "Dynamite; and Mone submitted her for the AEW Women's World Championship at All In: "
              "London on August 30, 2026, Nightingale passing out in the Statement Maker rather than "
              "tapping. A title rematch is the obvious next chapter, and none is announced.",
            q_ld="What is Mercedes Mone's record against Willow Nightingale?",
            a_ld="Mercedes Mone and Willow Nightingale are 2-2 in their series. Nightingale won at NJPW "
                 "Resurgence on May 21, 2023, when Mone suffered an ankle injury; Mone won the TBS "
                 "Championship from Nightingale at AEW Double or Nothing on May 26, 2024; Nightingale "
                 "regained the TBS Championship on the December 31, 2025 episode of Dynamite; and Mone "
                 "defeated Nightingale for the AEW Women's World Championship at All In: London on "
                 "August 30, 2026."),
        dict(
            q="Did she really break her nose winning the title at Wembley?",
            a="She finished the match bloodied &mdash; Cageside Seats' report is headlined around her "
              "breaking her nose, and F4W and Wrestling Inc. describe a bloody nose through the closing "
              "stretch. Whether it was clinically broken has not been confirmed by AEW as of August 31, "
              "2026, so this page reports the injury as the outlets reported it: she won her first AEW "
              "Women's World Championship bleeding, submitting a Willow Nightingale who was herself "
              "working with an injured left hand that Mone targeted all match.",
            q_ld="Was Mercedes Mone injured winning the AEW Women's World Championship at All In: London?",
            a_ld="Mercedes Mone finished the All In: London match on August 30, 2026 with a bloody "
                 "nose, which Cageside Seats reported as a broken nose. AEW has not medically confirmed "
                 "a break as of August 31, 2026. She won the match by submitting Willow Nightingale, "
                 "who was wrestling with an injured left hand that Mone targeted throughout."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Mercedes Justine Kaestner-Varnado"),
        dict(label="Born", value="January 26, 1992", sub="Fairfield, California &middot; age 34"),
        dict(label="Billed from", value="Boston, Massachusetts"),
        dict(label="Height", value="5&#8242;5&#8243;", sub="165 cm"),
        dict(label="Weight", value="114 lb", sub="52 kg (billed)"),
        dict(label="Debut", value="2010", sub="Chaotic Wrestling, Massachusetts, as Mercedes KV"),
        dict(label="WWE tenure", value="August 2012 &ndash; May 16, 2022",
             sub="as Sasha Banks &mdash; ended by the Raw walkout with Naomi, not a match"),
        dict(label="Ring names", value="Mercedes KV &rarr; Sasha Banks &rarr; Mercedes Mone",
             sub="2010&ndash;12 &middot; 2012&ndash;22 &middot; 2023&ndash;present &mdash; this site "
                 "spells Mone without the accent"),
        dict(label="Signature", value="Statement Maker &middot; Mone Maker &middot; Bank Statement "
                                      "&middot; Meteora",
             sub="the Statement Maker ended All In: London"),
        dict(label="Company", value="AEW", sub="since March 2024 &middot; with NJPW and CMLL crossovers"),
        dict(label="Family", value="First cousin of Snoop Dogg"),
        dict(label="Also known as",
             value="The CEO &middot; The Boss &middot; The Legit Boss &middot; The Belt Collector"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1992-01-26",
    bornplace="Fairfield, California, United States",
    nationality="United States",
    height_cm=165,
    weight_kg=52,
    ld=dict(
        alternateName=["Sasha Banks", "Mercedes KV", "Mercedes Varnado", "The Boss", "The Legit Boss",
                       "The CEO", "The Belt Collector"],
        award=["AEW Women's World Championship (1 reign, current, won August 30, 2026)",
               "AEW TBS Championship (1 reign, 584 days, the longest in the title's history)",
               "IWGP Women's Championship (1 reign)",
               "NJPW Strong Women's Championship (1 reign)",
               "CMLL World Women's Championship (1 reign)",
               "WWE Raw Women's Championship (4 reigns, as Sasha Banks)",
               "WWE SmackDown Women's Championship (1 reign, as Sasha Banks)",
               "WWE Women's Tag Team Championship (3 reigns, inaugural champion with Bayley)",
               "NXT Women's Championship (1 reign)",
               "Owen Hart Foundation Women's Tournament (2025, 2026 — the first two-time winner)",
               "A record 13 championships held simultaneously (2025)"],
        knowsAbout=["Professional wrestling", "WWE", "AEW", "New Japan Pro-Wrestling", "CMLL",
                    "Women's professional wrestling", "Championship wrestling"],
        description="Mercedes Mone, formerly known in WWE as Sasha Banks, is an American professional "
                    "wrestler signed to AEW. She won the AEW Women's World Championship for the first "
                    "time on August 30, 2026 at All In: London, defeating Willow Nightingale. She held "
                    "the AEW TBS Championship for a record 584 days, held a record 13 championships "
                    "simultaneously in 2025 across AEW, CMLL, ROH and international independents, and "
                    "in WWE won five world championships, the inaugural WWE Women's Tag Team "
                    "Championship with Bayley, and main-evented WrestleMania 37.",
        sameAs=["https://x.com/MercedesVarnado",
                "https://www.instagram.com/mercedesvarnado/",
                "https://en.wikipedia.org/wiki/Mercedes_Mon%C3%A9"],
    ),
)
