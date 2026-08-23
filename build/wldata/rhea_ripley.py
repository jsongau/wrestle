# -*- coding: utf-8 -*-
"""Rhea Ripley - dossier data.

Sources: /tmp/research/rhea-ripley.md (web-verified, compiled Aug 23 2026) and the
harvested match/signature/tape data from the previous /wrestlers/rhea-ripley/ page.
Nothing here is invented. Every match row carries a date stated in one of those two,
and the harvested bout dated "Various" is dropped rather than given a guessed date.

Two things the old page got wrong and this one does not:
  * "longest Women's World Championship reign" - it is a TIE with Bayley at 380 days
    (379 each as WWE recognises them), because the SmackDown Women's Championship was
    renamed the Women's World Championship in June 2023 and Bayley's reign is on the
    same lineage table.
  * "vacated the title due to injury" in 2026 - WWE did not vacate anything; it created
    an Interim WWE Women's Championship and left the real one on Ripley.

No career win-loss total is published: the old page's 71-22 headline is flagged by the
harvester as inconsistent with its own sparkline (66 marks / 5 losses) and Cagematch was
excluded from research as JavaScript-gated.
"""

# ----------------------------------------------------------------- record rows
# 5 usable rows harvested from the existing page (the 6th, dated "Various", is dropped)
# plus rows whose dates and outcomes are stated explicitly in the research dossier.
ROWS = [
    dict(result="W", date="2018-08-26", promo="WWE", landmark=True,
         event="NXT UK — Birmingham, England",
         opponent="Toni Storm",
         stip="Tournament final — inaugural champion",
         title="NXT UK Women's Championship"),
    dict(result="L", date="2019-01-12", promo="WWE",
         event="NXT UK TakeOver: Blackpool",
         opponent="Toni Storm",
         stip="Singles — ends the 139-day inaugural reign",
         title="NXT UK Women's Championship"),
    dict(result="W", date="2019-12-18", promo="WWE", landmark=True,
         event="NXT — Winter Park, Florida",
         opponent="Not named in any source consulted",
         stip="Singles — 10th NXT Women's Champion",
         title="NXT Women's Championship"),
    dict(result="L", date="2020-04-05", promo="WWE", landmark=True,
         event="WrestleMania 36 Night 2",
         opponent="Charlotte Flair", opponent_html=True,
         stip="Singles — ends a 109-day reign",
         title="NXT Women's Championship"),
    dict(result="W", date="2021-04-11", promo="WWE", landmark=True,
         event="WrestleMania 37 — Tampa, Florida",
         opponent="Asuka", opponent_html=True,
         stip="Singles — first main-roster championship",
         title="Raw Women's Championship"),
    dict(result="L", date="2021-07-18", promo="WWE",
         event="Money in the Bank",
         opponent="Charlotte Flair", opponent_html=True,
         stip="Singles — ends a 98-day reign",
         title="Raw Women's Championship"),
    dict(result="W", date="2023-01-28", promo="WWE", type="tag", landmark=True,
         event="Royal Rumble",
         opponent="The 2023 women's Royal Rumble field",
         stip="Royal Rumble match — entry #1, 1:01:08 in the match",
         title=""),
    dict(result="W", date="2023-04-01", promo="WWE", landmark=True,
         event="WrestleMania 39 Night 1 — SoFi Stadium",
         opponent="Charlotte Flair", opponent_html=True,
         stip="Singles — PWI Match of the Year; the 380-day reign begins",
         title="SmackDown Women's Championship"),
    dict(result="W", date="2024-03-02", promo="WWE",
         event="Elimination Chamber",
         opponent="Becky Lynch",
         stip="Singles — title defense",
         title="Women's World Championship"),
    dict(result="L", date="2024-08-03", promo="WWE", landmark=True,
         event="SummerSlam",
         opponent="Liv Morgan",
         stip="Singles — the return from injury",
         title="Women's World Championship"),
    dict(result="L", date="2025-04-20", promo="WWE", type="tag", landmark=True,
         event="WrestleMania 41 Night 2",
         opponent="Iyo Sky & Bianca Belair",
         stip="Triple threat — five stars from Dave Meltzer; Sky retains",
         title="Women's World Championship"),
    dict(result="W", date="2026-02-28", promo="WWE", type="tag", landmark=True,
         event="Elimination Chamber",
         opponent="The 2026 women's Elimination Chamber field",
         stip="Elimination Chamber match",
         title=""),
    dict(result="W", date="2026-04-19", promo="WWE", landmark=True,
         event="WrestleMania 42 — Paradise, Nevada",
         opponent="Jade Cargill",
         stip="Singles — her second reign with this belt, not her first",
         title="WWE Women's Championship"),
    dict(result="W", date="2026-05-31", promo="WWE", landmark=True,
         event="Clash in Italy — Inalpi Arena, Turin",
         opponent="Jade Cargill",
         stip="Singles — her last match to date",
         title="WWE Women's Championship"),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Charlotte Flair": "charlotte-flair", "Asuka": "asuka"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="rhea-ripley",
    name="Rhea Ripley",
    realname="Demi Bennett",
    epithet="Mami",
    hook="Record & Titles",

    meta_desc=("Rhea Ripley, Mami, is a four-time world champion whose 380-day Women's World "
               "Championship reign is tied with Bayley for the longest in that title's history, not "
               "ahead of it. Full record, titles, factions and career."),
    og_desc=("Mami: 4 world title reigns, a 380-day Women's World Championship run tied with Bayley, "
             "the women's Grand Slam at 26. Full record, titles, factions and career."),
    tw_desc="Mami: 4 world titles, a 380-day reign tied with Bayley, the women's Grand Slam at 26.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2013",
    height_imp="5&#8242;7&#8243;",
    weight_lb="",          # three published figures and WWE.com lists none - see the tape
    world_titles="4",
    vitals_tagline="Mami is always on top",
    support_note="Merch &middot; Games &middot; Sources",
    x_url="https://x.com/rhearipley_wwe",
    ig_url="https://www.instagram.com/rhearipley_wwe/",
    sp_items=[
        dict(ic="RR", title="Rhea Ripley Merch", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Cover star, WWE 2K24 Deluxe Edition",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com superstar page",
             tag="Visit", href="https://www.wwe.com/superstars/rhea-ripley"),
        dict(ic="WL", title="Research Dossier", sub="Every source behind this page",
             tag="Read", charity=True, href="/data/rhea-ripley.md"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Eradicator &middot; The Nightmare &middot; Demi Bennett",
    hero_tag="Adelaide, South Australia &middot; <em>RCW &middot; NXT UK &middot; WWE &middot; 2013&ndash;present</em>",
    now_label="NOW",
    now_bold="WWE Women's Champion",
    now_tail=" &middot; injured, no announced return date as of August 23, 2026",
    hstats=[
        dict(value="4",   x=True,  label="World Title Reigns"),
        dict(value="380", x=False, label="Day Reign, Tied"),
        dict(value="5",   x=False, label="Grand Slam Titles"),
        dict(value="1",   x=True,  label="Royal Rumble Win"),
    ],
    ghost_link="From Adelaide to the Grand Slam at 26",
    vlabel="Est. 2013 &middot; Adelaide, SA",
    mono="RR",

    # ---------------------------------------------------------------- 01 overview
    overview=[
        "<b>Rhea Ripley</b> is the wrestler who proved WWE could build a women&rsquo;s division around "
        "an archetype it had spent forty years avoiding: a tall, heavy-hitting heel who beats opponents "
        "rather than out-athletes them. The concrete measure is the trophy cabinet. She has held all five "
        "championships in the WWE women&rsquo;s Grand Slam set &mdash; NXT UK Women&rsquo;s, NXT "
        "Women&rsquo;s, the Raw/WWE Women&rsquo;s Championship lineage, the SmackDown/Women&rsquo;s World "
        "Championship lineage and the Women&rsquo;s Tag Team Championship &mdash; and completed the set "
        "at 26, the fifth woman to do it. Her WrestleMania 41 triple threat with Iyo Sky and Bianca Belair "
        "drew five stars from Dave Meltzer, and she is the first Australian woman to hold a championship "
        "in WWE.",

        "The number attached to her most famous run is <b>380 days</b>, and the sentence usually wrapped "
        "around it is wrong. That reign &mdash; WrestleMania 39 on April 1, 2023 through April 15, 2024 "
        "&mdash; is <b>not</b> the longest in the Women&rsquo;s World Championship&rsquo;s history. "
        "Wikipedia&rsquo;s article on the title states it flatly: Bayley&rsquo;s second reign and "
        "Ripley&rsquo;s first are <i>tied</i> for the longest singular reign at 380 days, and by "
        "WWE&rsquo;s own recognised count the figure is 379 for both. Bayley belongs on that list because "
        "the belt is not a 2023 creation: it was established on August 23, 2016 as the <b>SmackDown "
        "Women&rsquo;s Championship</b> and renamed the Women&rsquo;s World Championship in June 2023, "
        "when the draft moved it to Raw with Ripley. That rename is the entire reason the error spreads "
        "&mdash; treat the title as new and 380 days looks unmatched. Treat it as one lineage, which it "
        "is, and Bayley&rsquo;s October 11, 2019 &ndash; October 25, 2020 reign is level with it. The "
        "honest superlative is narrower and still large: nobody has held it longer.",

        "She was born Demi Bennett in Adelaide, South Australia on October 11, 1996 and came up through "
        "the Australian independents &mdash; two Riot City Wrestling Women&rsquo;s Championship reigns, "
        "tours of Japan in 2015 for Pro Wrestling Zero1 and Sendai Girls. Her debut date is genuinely "
        "unsettled; four sources publish four answers, listed in the tape. She signed with WWE in 2017, "
        "wrestled the inaugural Mae Young Classic, and was renamed on July 13, 2017 after the Greek "
        "goddess Rhea and Ellen Ripley of <i>Alien</i>. The breakout was NXT UK, where she became the "
        "inaugural champion, then NXT, then the Raw Women&rsquo;s Championship at WrestleMania 37. The "
        "run that made her a headliner started in May 2022 when she joined The Judgment Day: the 2023 "
        "Royal Rumble won from the number-one entry, the first singles win over Charlotte Flair in a "
        "WrestleMania match, and 380 days on top.",

        "She is currently the WWE Women&rsquo;s Champion and currently unable to defend it. She took the "
        "title from Jade Cargill at WrestleMania 42 on April 19, 2026, moved to SmackDown with it, "
        "retained against Cargill at Clash in Italy in Turin on May 31, and has not wrestled since. WWE "
        "did <b>not</b> vacate the championship &mdash; several outlets reported that it did, and they "
        "are wrong. Instead the company created an <b>Interim WWE Women&rsquo;s Championship</b>, won by "
        "Chelsea Green in a five-woman ladder match at SummerSlam Night 2 on August 2, 2026, with a "
        "unification match promised once Ripley is medically cleared. The injury itself is reported two "
        "irreconcilable ways, both set out in the FAQ below, and no return date has been announced.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full ledger",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("4&times;", "World title reigns"),
            ("8",        "WWE title reigns"),
            ("380",      "Longest reign (days)"),
            ("7th",      "Women’s Triple Crown"),
            ("5th",      "Women’s Grand Slam"),
            ("1&times;", "Royal Rumble win"),
        ],
        lead=("Fourteen documented bouts &mdash; the title changes, the WrestleMania matches and the "
              "nights that turned the character. This is a <b>highlight subset, not a complete career "
              "ledger</b>, and no career win&ndash;loss total is published here: the previous edition of "
              "this page carried a 71&ndash;22 headline that the harvester flags as inconsistent with its "
              "own sparkline (66 marks, five losses), and Cagematch was excluded from research as "
              "JavaScript-gated. One harvested bout was dated only &ldquo;Various&rdquo; and is dropped "
              "rather than given a guessed date; one row leaves the opponent unnamed because no source "
              "consulted named her. Filter by match type, tap any column header to sort, and turn "
              "spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("Three cards, and their provenance differs &mdash; which is the point. Only the "
                    "WrestleMania 41 rating is sourced: Dave Meltzer gave the triple threat five stars, "
                    "reported by Wrestlezone, and the research file identifies it as the highest-rated "
                    "women&rsquo;s match on his scale. The other two ratings are carried over from the "
                    "previous edition of this page and are <b>not corroborated</b> by any source in the "
                    "file. They are kept because the bouts are real; the numbers beside them are not "
                    "independently verified."),
    signature=[
        dict(rating="5.0", event="WrestleMania 41 Night 2 · April 20, 2025",
             opponent="Iyo Sky & Bianca Belair",
             stip="Women's World Championship — triple threat (Meltzer, sourced)"),
        dict(rating="5.0", event="WrestleMania 36 Night 2 · 2020", opponent="Charlotte Flair",
             stip="NXT Women's Championship — rating carried over, unverified",
             url="/wrestlers/charlotte-flair/"),
        dict(rating="4.5", event="Raw · 2023", opponent="Charlotte Flair",
             stip="Women's World Championship — rating and date carried over, unverified",
             url="/wrestlers/charlotte-flair/"),
    ],

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("4&times;", "World title reigns"),
            ("8",        "WWE title reigns"),
            ("7th",      "Women’s Triple Crown"),
            ("5th",      "Women’s Grand Slam"),
        ],
        lead=("Eight WWE championship reigns across five belts, plus two independent reigns whose dates "
              "are not verified. Read the lineage notes before counting: <b>her WrestleMania 42 win over "
              "Jade Cargill is her second WWE Women&rsquo;s Championship, not her first</b>. The Raw "
              "Women&rsquo;s Championship she won from Asuka at WrestleMania 37 in 2021 is the same "
              "physical title, renamed WWE Women&rsquo;s Championship on June 9, 2023 when the draft "
              "moved it to SmackDown &mdash; WWE.com lists her as a two-time holder for exactly that "
              "reason. Outlets that called the 2026 win her first are miscounting a rename as a new belt, "
              "the same mistake that produces the 380-day claim above."),
        rows=[
            dict(ic="W", name="WWE Women's Championship", count="2",
                 sub="2021 &mdash; won as the <i>Raw Women&rsquo;s Championship</i>, def. Asuka at "
                     "WrestleMania 37 in Tampa, 98 days, lost to Charlotte Flair at Money in the Bank "
                     "&middot; 2026&ndash; &mdash; def. Jade Cargill at WrestleMania 42, 126 days as of "
                     "August 23, 2026 and ongoing &middot; the belt was established April 3, 2016, "
                     "renamed Raw Women&rsquo;s Championship in September 2016 and reverted to WWE "
                     "Women&rsquo;s Championship on June 9, 2023 &mdash; all three names, one title"),
            dict(ic="V", name="Women's World Championship", count="2",
                 sub="2023&ndash;24 &mdash; def. Charlotte Flair at WrestleMania 39 Night 1, <b>380 days "
                     "(Wikipedia) or 379 (WWE&rsquo;s recognised count)</b>, relinquished April 15, 2024 "
                     "&middot; <b>tied</b> with Bayley&rsquo;s second reign for the longest in the "
                     "lineage, not ahead of it &middot; 2025 &mdash; regained January 6, 56 days, ended "
                     "March 3 &middot; the belt was created August 23, 2016 as the SmackDown Women&rsquo;s "
                     "Championship and renamed on June 12, 2023"),
            dict(ic="N", name="NXT Women's Championship", count="1",
                 sub="2019&ndash;20 &middot; won December 18, 2019 in Winter Park, Florida &mdash; 10th "
                     "champion overall &middot; 109 days &middot; lost to Charlotte Flair at WrestleMania "
                     "36 Night 2 on April 5, 2020"),
            dict(ic="U", name="NXT UK Women's Championship", count="1",
                 sub="2018&ndash;19 &middot; inaugural champion, def. Toni Storm in the tournament final "
                     "&middot; 139 days &middot; <b>start date disputed</b>: the match was taped August "
                     "26, 2018 in Birmingham, but WWE recognises the reign as beginning November 28, "
                     "2018, the tape-delay air date &middot; lost to Toni Storm at TakeOver: Blackpool, "
                     "January 12, 2019 &middot; title retired September 4, 2022"),
            dict(ic="T", name="WWE Women's Tag Team Championship", count="2",
                 sub="2021 &mdash; with Nikki A.S.H. as &ldquo;Super Brutality,&rdquo; won September 20 "
                     "on Raw in Raleigh, 63 days, lost to Natalya &amp; Tamina &middot; 2026 &mdash; with "
                     "Iyo Sky as &ldquo;Rhiyo,&rdquo; won January 5 on Raw in New York, 53 days, lost to "
                     "Asuka &amp; Kairi Sane"),
            dict(ic="R", name="Riot City Wrestling Women's Championship", count="2",
                 sub="Australian independents, as Demi Bennett &middot; reign dates and lengths <b>not "
                     "verified</b> by any source consulted &mdash; listed by TheSmackDownHotel with no "
                     "figures attached"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="One faction made her a headliner. Being thrown out of it made her a babyface.",
        cards=[
            dict(era="WWE &middot; May 2022 &ndash; August 2024",
                 name="The Judgment Day",
                 members="Rhea Ripley, Edge, Damian Priest, Finn Bálor, Dominik Mysterio, "
                         "JD McDonagh, Carlito, Liv Morgan, Raquel Rodriguez, Roxanne Perez",
                 desc="Formed at WrestleMania 38 in April 2022 by Edge, who recruited Damian Priest; "
                      "Ripley joined in May 2022 and the group dropped Edge and his leadership structure "
                      "by June, running afterwards as a heel unit with no stated leader. It is where the "
                      "Mami character was built and where her biggest year happened: the 2023 Royal "
                      "Rumble, the WrestleMania 39 title win, the 380-day reign. Between them the members "
                      "collected a World Heavyweight Championship, three Women's World Championship "
                      "reigns, Intercontinental and NXT North American runs and two women's Royal Rumble "
                      "wins. Ripley and Priest were removed from the group on the Raw after SummerSlam "
                      "2024, dated August 3, 2024, once the Dominik Mysterio and Liv Morgan storyline "
                      "turned the faction against them. She did not walk out; she was thrown out."),
            dict(era="WWE &middot; 2024&ndash;present",
                 name="The Terror Twins",
                 members="Rhea Ripley, Damian Priest",
                 desc="The tag team the two of them formed after being expelled from The Judgment Day, "
                      "and the vehicle for her turn back to a babyface. No championships are recorded for "
                      "the pairing in any source consulted."),
            dict(era="WWE &middot; 2025&ndash;26",
                 name="Rhiyo",
                 members="Rhea Ripley, Iyo Sky",
                 desc="A rivalry converted into a tag team. Sky had ended Ripley's second Women's World "
                      "Championship reign in March 2025 and beaten her again in the WrestleMania 41 "
                      "triple threat; they won the Women's Tag Team Championship together on January 5, "
                      "2026 in New York and held it 53 days before losing to Asuka and Kairi Sane."),
            dict(era="WWE &middot; 2021&ndash;22",
                 name="Super Brutality",
                 members="Rhea Ripley, Nikki A.S.H.",
                 desc="Her first tag team and first tag championship: 63 days as Women's Tag Team "
                      "Champions from September 20, 2021, won on Raw in Raleigh and lost to Natalya and "
                      "Tamina. TheSmackDownHotel also lists a short-lived 2022 pairing with Liv Morgan "
                      "billed as “Liv for Brutality,” which no other source consulted confirms."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Four characters, one escalation &mdash; from a mohawked NXT UK brawler to the most over "
             "women&rsquo;s act of her era.",
        cards=[
            dict(mono="UK", era="WWE &middot; 2017&ndash;2019", name="The NXT UK Era",
                 desc="Renamed on July 13, 2017 after the Greek goddess Rhea and Ellen Ripley of Alien, "
                      "she wrestled the inaugural Mae Young Classic and then became the first NXT UK "
                      "Women's Champion as a shaved-side, aggressive brawler. The finishes of the period "
                      "were the Riptide and a Full Nelson Slam, the latter used from October 25, 2017 to "
                      "August 27, 2019. Before all of it: five years as Demi Bennett on the Australian "
                      "independents and in Japan."),
            dict(mono="NM", era="WWE &middot; 2019&ndash;2021", name="The Nightmare",
                 desc="A darker, gothic presentation on the move from NXT UK to NXT, documented under "
                      "that nickname by F4W. It carried the NXT Women's Championship from December 2019, "
                      "the WrestleMania 36 match against Charlotte Flair that opened the show, and the "
                      "call-up that produced her first main-roster title at WrestleMania 37."),
            dict(mono="MM", era="WWE &middot; 2022&ndash;2024", name="Mami",
                 desc="The character that made her a headliner, built inside The Judgment Day: a dominant "
                      "heel who curdled into an antihero as the crowd refused to boo, the Dominik "
                      "Mysterio dynamic, and the entrance theme “Demon In Your Dreams” by def "
                      "rebel featuring Motionless in White. The Prism Trap, a standing inverted Texas "
                      "cloverleaf, was added as a second finish from May 9, 2022."),
            dict(mono="ER", era="WWE &middot; 2024&ndash;present", name="The Eradicator, On Her Own",
                 desc="Expelled from the faction in August 2024 and rebuilt as a top babyface: the Terror "
                      "Twins with Damian Priest, Rhiyo with Iyo Sky, the 2026 Elimination Chamber, and "
                      "SmackDown's WWE Women's Champion from April 2026. WWE.com's current profile still "
                      "leads with the Eradicator framing; Mami and The Nightmare both remain in use."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Adelaide to the Grand Slam, and the fastest anyone has completed it.",
        rows=[
            dict(year="2013", title="Debuts in Australia as Demi Bennett",
                 desc="Starts on the Australian independents with Riot City Wrestling and New Horizon "
                      "Pro Wrestling. The exact debut date is disputed four ways across published "
                      "sources — see the tape."),
            dict(year="2015", title="Tours Japan",
                 desc="Works for Pro Wrestling Zero1 and Sendai Girls, and holds the Riot City Wrestling "
                      "Women's Championship twice around it."),
            dict(year="2017", title="Signs with WWE and gets the name",
                 desc="Competes in the inaugural Mae Young Classic and is renamed Rhea Ripley on July 13, "
                      "2017, after the Greek goddess Rhea and Ellen Ripley of Alien."),
            dict(year="2018", title="Inaugural NXT UK Women's Champion",
                 desc="Beats Toni Storm in the tournament final, taped August 26, 2018 in Birmingham and "
                      "recognised by WWE from the November 28 air date. The reign runs 139 days."),
            dict(year="2019", title="NXT Women's Champion",
                 desc="Wins the title on December 18, 2019 in Winter Park, Florida and holds it 109 days. "
                      "Named Breakthrough Wrestler of the Year by both CBS Sports and ESPN."),
            dict(year="2021", title="First main-roster championship",
                 desc="Beats Asuka at WrestleMania 37 on April 11 for the Raw Women's Championship — the "
                      "same belt now called the WWE Women's Championship — and wins her first Women's Tag "
                      "Team Championship with Nikki A.S.H. in September."),
            dict(year="2022", title="Joins The Judgment Day",
                 desc="Enters the faction in May 2022. The Mami character takes hold and the Prism Trap "
                      "is added to the arsenal."),
            dict(year="2023", title="The career year",
                 desc="Wins the women's Royal Rumble from entry number one on January 28, beats Charlotte "
                      "Flair at WrestleMania 39 on April 1, and is named PWI's number one in the Women's "
                      "250, PWI Woman of the Year and the Wrestling Observer's Women's Wrestling MVP."),
            dict(year="2024", title="The 380 days end, and so does the faction",
                 desc="Relinquishes the Women's World Championship on April 15 after 380 days, returns at "
                      "SummerSlam and loses to Liv Morgan, and is removed from The Judgment Day on "
                      "August 3."),
            dict(year="2025", title="Second world reign and a five-star match",
                 desc="Regains the Women's World Championship on January 6 for 56 days; the WrestleMania "
                      "41 triple threat against Iyo Sky and Bianca Belair earns five stars from Dave "
                      "Meltzer and Sports Illustrated's Match of the Year."),
            dict(year="2026", title="WWE Women's Champion, then sidelined",
                 desc="Wins the Women's Tag Team Championship with Iyo Sky on January 5, the Elimination "
                      "Chamber on February 28, and the WWE Women's Championship from Jade Cargill at "
                      "WrestleMania 42 on April 19, moving to SmackDown. Her last match is the Turin "
                      "rematch on May 31; a knee injury follows and Chelsea Green is crowned interim "
                      "champion on August 2."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who she went to war with.",
        cards=[
            dict(name="Charlotte Flair", slug="charlotte-flair",
                 desc="The measuring stick, and the scoreboard runs both ways: Flair beat her for the NXT "
                      "Women's Championship at WrestleMania 36 and took the Raw Women's Championship off "
                      "her at Money in the Bank 2021. Then Ripley beat her at WrestleMania 39 on April 1, "
                      "2023 — the first woman to win a singles match against Flair at WrestleMania — in a "
                      "match Pro Wrestling Illustrated named its 2023 Match of the Year. That win started "
                      "the 380 days."),
            dict(name="Liv Morgan", slug="liv-morgan",
                 desc="The feud that ended her faction era. Morgan's storyline pursuit of Dominik Mysterio "
                      "and the attack that wrote Ripley off television led to the Women's World "
                      "Championship being relinquished on April 15, 2024, a losing return at SummerSlam, "
                      "and Ripley and Damian Priest being thrown out of The Judgment Day in August. "
                      "Morgan took two Women's World Championship reigns out of it."),
            dict(name="Iyo Sky", slug="iyo-sky",
                 desc="Sky ended Ripley's second Women's World Championship reign on March 3, 2025 and "
                      "then retained against Ripley and Bianca Belair in the WrestleMania 41 triple "
                      "threat — the five-star match, and the highest-rated women's match WWE has had on "
                      "Meltzer's scale. The rivalry then converted into Rhiyo, the tag team that won the "
                      "Women's Tag Team Championship in January 2026."),
            dict(name="Jade Cargill", slug="jade-cargill",
                 desc="The current program, and the one that moved Ripley to SmackDown as champion. She "
                      "took the WWE Women's Championship from Cargill at WrestleMania 42 on April 19, "
                      "2026 and retained the rematch at Clash in Italy in Turin on May 31 in front of an "
                      "announced 12,000. That rematch is her last match to date, and one of the two "
                      "conflicting injury reports places the knee injury in it."),
            dict(name="Bianca Belair", slug="bianca-belair",
                 desc="The third corner of the WrestleMania 41 triple threat and a recurring opponent "
                      "across the 2023 to 2025 title runs. Detail on their earlier singles meetings is "
                      "not verified in the research file, so none is claimed here."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="What is verified, and what is not.",
        rows=[
            dict(when="2019&ndash;2026", title="WWE 2K series", kind="Game",
                 desc="Playable in WWE 2K20, WWE 2K Battlegrounds, WWE 2K22, WWE 2K23, WWE 2K24, WWE 2K25 "
                      "and WWE 2K26 — and the cover star of the WWE 2K24 Deluxe Edition."),
            dict(when="2024", title="Call of Duty: Modern Warfare III", kind="Game",
                 desc="Unlockable operator. One Wikipedia read described her as a Season 5 operator; that "
                      "season detail is not verified and is not asserted here."),
            dict(when="2022&ndash;", title="Demon In Your Dreams", kind="Music",
                 desc="Her entrance theme, by def rebel featuring Motionless in White and co-written by "
                      "the band. Performed live at WrestleMania XL."),
            dict(when="&mdash;", title="Film and television", kind="Not verified",
                 desc="No filmography is published here because none is verified. Wikipedia's other-media "
                      "section lists only video games and the theme song; her IMDb page is blocked to "
                      "automated retrieval by robots.txt and TV Guide's credits page returned nothing "
                      "parseable. A role in Terrifier 4 has been covered as a potential role only and is "
                      "unconfirmed. There is no autobiography."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The numbers, stated the way the sources actually state them &mdash; ties included.",
        stats=[
            ("380",     "Day title reign (tied)"),
            ("1:01:08", "Longest women’s Rumble"),
            ("5th",     "Women’s Grand Slam"),
        ],
        rows=[
            dict(name="380 days with the Women's World Championship — tied, not first",
                 sub="April 1, 2023 to April 15, 2024. Wikipedia's title article states that Bayley's "
                     "second reign and Ripley's first are tied for the longest singular reign at 380 "
                     "days, and that WWE recognises 379 days for both. Bayley's reign (October 11, 2019 "
                     "to October 25, 2020) sits on the same lineage table because the SmackDown Women's "
                     "Championship was renamed the Women's World Championship in June 2023."),
            dict(name="First woman to win a Royal Rumble from the number-one entry",
                 sub="January 28, 2023. She also set the record for longest time in a women's Royal "
                     "Rumble at 1:01:08 — a record Bayley broke the following year at 1:03:03, so it is "
                     "no longer hers."),
            dict(name="5th WWE Women's Grand Slam Champion, 7th Women's Triple Crown Champion",
                 sub="Wikipedia adds that she is the only wrestler to have held all five titles in the "
                     "women's Grand Slam set and the youngest Grand Slam champion of either gender at 26. "
                     "Both of those claims are single-sourced to Wikipedia and were not corroborated "
                     "elsewhere, so they are reported as attributed rather than as settled fact."),
            dict(name="First Australian woman to hold a WWE championship",
                 sub="Note the qualifier. Buddy Murphy's 2018 Cruiserweight Championship predates it, so "
                     "the version of this claim without the word 'woman' is wrong."),
            dict(name="Five stars from Dave Meltzer, once",
                 sub="Ripley vs. Iyo Sky vs. Bianca Belair, WrestleMania 41 Night 2, April 20, 2025, "
                     "reported by Wrestlezone. Sports Illustrated also named it its 2025 Match of the "
                     "Year."),
            dict(name="PWI number one in the Women's 250, 2023",
                 sub="Plus PWI Woman of the Year 2023, Faction of the Year 2023 for The Judgment Day and "
                     "Match of the Year 2023 for the WrestleMania 39 match with Charlotte Flair. Her "
                     "Women's 250 placings for 2024, 2025 and 2026 are not verified and are not guessed "
                     "at here."),
            dict(name="Wrestling Observer Women's Wrestling MVP, 2023",
                 sub="Alongside Sports Illustrated's number two overall wrestler of 2023 and number seven "
                     "women's wrestler of 2019, WWE Slammy Awards for Female Superstar, Faction and Match "
                     "of the Year in 2024, CBS Sports and ESPN Breakthrough Wrestler of the Year in 2019, "
                     "and the Women's Wrestling Hall of Fame's Pro Wrestler of the Year for 2025."),
            dict(name="Royal Rumble 2023 attendance is two different numbers",
                 sub="WWE announced 51,338 at the Alamodome. Wrestlenomics counted 42,928 tickets "
                     "scanned. Both figures are published; neither has been reconciled."),
            dict(name="WrestleMania 39 drew 134,856 across two nights",
                 sub="WWE's figures: 67,303 on Night 1, when she beat Charlotte Flair for the title, and "
                     "67,553 on Night 2. Her last match, Clash in Italy on May 31, 2026, drew an "
                     "announced 12,000 at the Inalpi Arena in Turin."),
        ],
        footnote=("No career win-loss total appears anywhere on this page. Cagematch was excluded from "
                  "research as JavaScript-gated, and the previous edition of this page published a 71-22 "
                  "record that the harvester flags as inconsistent with its own sparkline, which carries "
                  "66 marks and five losses and is decorative rather than data. Where two sources give "
                  "two numbers — 380 against 379 days, 51,338 against 42,928 tickets, five published "
                  "heights and weights between them — both are shown rather than one being chosen."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Instagram", v="@rhearipley_wwe", href="https://www.instagram.com/rhearipley_wwe/"),
        dict(k="X / Twitter", v="@RheaRipley_WWE", href="https://x.com/rhearipley_wwe"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/rhea-ripley"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Rhea_Ripley"),
        dict(k="Wikipedia", v="Women's World Championship lineage",
             href="https://en.wikipedia.org/wiki/Women%27s_World_Championship_(WWE)"),
        dict(k="F4W / WON", v="Injury update, July 11, 2026",
             href="https://www.f4wonline.com/news/wwe/rhea-ripley-provides-injury-update-says-timeline-to-return-up-in-the-air/"),
        dict(k="Bleacher Report", v="Interim title at SummerSlam 2026",
             href="https://bleacherreport.com/articles/25460215-chelsea-green-wins-interim-wwe-womens-title-ladder-match-summerslam-after-ripleys-injury"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/rhea-ripley.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Rhea Ripley&rsquo;s 380-day reign the longest in Women&rsquo;s World Championship history?",
            a="No &mdash; it is a <b>tie</b>. Wikipedia&rsquo;s article on the title states that "
              "Bayley&rsquo;s second reign and Ripley&rsquo;s first are tied for the longest singular "
              "reign at 380 days, and that WWE recognises 379 days for both. Ripley held it from April 1, "
              "2023 to April 15, 2024; Bayley held it from October 11, 2019 to October 25, 2020. "
              "Bayley&rsquo;s reign counts on the same list because the belt was created on August 23, "
              "2016 as the <b>SmackDown Women&rsquo;s Championship</b> and only renamed the Women&rsquo;s "
              "World Championship in June 2023 &mdash; and that rename is exactly why the &ldquo;longest "
              "ever&rdquo; claim spreads. Treat the title as though it began in 2023 and Ripley&rsquo;s "
              "number looks unmatched; treat it as the single lineage it actually is and she is level "
              "with Bayley. Nobody has held it longer, which is the accurate way to say it.",
            q_ld="Is Rhea Ripley's 380-day reign the longest in Women's World Championship history?",
            a_ld="No. It is a tie. Wikipedia's Women's World Championship article states that Bayley's "
                 "second reign and Rhea Ripley's first reign are tied for the longest singular reign at "
                 "380 days, with 379 days recognised by WWE for both. Rhea Ripley held the title from "
                 "April 1, 2023 to April 15, 2024 and Bayley held it from October 11, 2019 to October 25, "
                 "2020. Bayley's reign belongs to the same lineage because the championship was "
                 "established on August 23, 2016 as the SmackDown Women's Championship and was renamed "
                 "the Women's World Championship in June 2023. The accurate statement is that no one has "
                 "held the title longer than Rhea Ripley, not that she holds it alone."),
        dict(
            q="Is Rhea Ripley still the WWE Women&rsquo;s Champion?",
            a="Yes. She has held the title since April 19, 2026 and WWE did <b>not</b> vacate it when she "
              "was injured &mdash; despite several outlets reporting that she &ldquo;vacated&rdquo; a "
              "championship. Instead WWE created a separate <b>Interim WWE Women&rsquo;s "
              "Championship</b>, won by Chelsea Green in a five-woman ladder match at SummerSlam Night 2 "
              "on August 2, 2026 over Charlotte Flair, Jade Cargill, Tiffany Stratton and Lash Legend, "
              "with a unification match promised for Ripley&rsquo;s return. Two further details often get "
              "garbled: the belt is the WWE Women&rsquo;s Championship, not the SmackDown Women&rsquo;s "
              "Championship, and the interim belt is not a Women&rsquo;s World Championship.",
            q_ld="Is Rhea Ripley still the WWE Women's Champion?",
            a_ld="Yes. Rhea Ripley has held the WWE Women's Championship since April 19, 2026, and WWE "
                 "did not vacate the title when she was injured. WWE instead created a separate Interim "
                 "WWE Women's Championship, won by Chelsea Green in a five-woman ladder match at "
                 "SummerSlam Night 2 on August 2, 2026, with a unification match promised for Rhea "
                 "Ripley's return. Reports describing a vacated SmackDown Women's Championship or an "
                 "interim Women's World Championship are inaccurate on both counts."),
        dict(
            q="What is Rhea Ripley&rsquo;s injury, and when is she coming back?",
            a="No return date has been announced as of August 23, 2026, and the injury itself is reported "
              "two ways that do not reconcile. On <b>July 11, 2026</b>, F4W/Wrestling Observer quoted "
              "Ripley herself describing &ldquo;a slight tear in her meniscus,&rdquo; suffered on "
              "<b>June 3, 2026 at a house show in Lisbon</b>, with no surgery mentioned and a timeline "
              "she called &ldquo;a little bit up in the air.&rdquo; On <b>August 11, 2026</b>, Athlon "
              "Sports reported a <b>severe meniscus tear</b> in the right knee suffered on <b>May 31 at "
              "Clash in Italy</b> against Jade Cargill, followed by failed rehab and <b>surgery</b>, and "
              "cited the Wrestling Observer saying WWE hoped to have her cleared for the Royal Rumble. "
              "Different date, different severity, different treatment. Both are published; neither is "
              "presented here as settled, and the Royal Rumble target is a reported hope rather than a "
              "booking.",
            q_ld="What is Rhea Ripley's injury and when is she coming back?",
            a_ld="No return date has been announced for Rhea Ripley as of August 23, 2026, and the injury "
                 "is reported in two irreconcilable ways. On July 11, 2026, F4W/Wrestling Observer quoted "
                 "Rhea Ripley describing a slight tear in her meniscus suffered on June 3, 2026 at a WWE "
                 "house show in Lisbon, Portugal, with no surgery mentioned and a return timeline she "
                 "said was up in the air. On August 11, 2026, Athlon Sports reported a severe meniscus "
                 "tear in the right knee suffered on May 31, 2026 at Clash in Italy against Jade Cargill, "
                 "followed by rehab and then surgery, and cited the Wrestling Observer Newsletter saying "
                 "WWE hoped she would be cleared in time for the Royal Rumble. Both accounts are "
                 "published and they conflict on date, severity and treatment."),
        dict(
            q="How many world championships has Rhea Ripley won?",
            a="Four world title reigns across two lineages: two <b>Women&rsquo;s World Championship</b> "
              "reigns (2023&ndash;24 and 2025) and two <b>WWE Women&rsquo;s Championship</b> reigns (2021 "
              "and 2026). The 2021 one counts because the Raw Women&rsquo;s Championship she took from "
              "Asuka at WrestleMania 37 is the same belt, renamed the WWE Women&rsquo;s Championship on "
              "June 9, 2023 &mdash; which is why her WrestleMania 42 win over Jade Cargill is her second "
              "reign with it, not her first, and why WWE.com lists her as a two-time holder. Counting all "
              "WWE championships rather than world titles: eight reigns across five belts.",
            q_ld="How many world championships has Rhea Ripley won?",
            a_ld="Rhea Ripley has won four world championship reigns across two lineages: two Women's "
                 "World Championship reigns, in 2023 to 2024 and in 2025, and two WWE Women's "
                 "Championship reigns, in 2021 and in 2026. The 2021 reign counts because the Raw Women's "
                 "Championship that Rhea Ripley won from Asuka at WrestleMania 37 is the same title, "
                 "renamed the WWE Women's Championship on June 9, 2023. That also means her WrestleMania "
                 "42 win over Jade Cargill is her second reign with that championship rather than her "
                 "first. Across all WWE titles she has eight reigns with five different championships."),
        dict(
            q="Why did Rhea Ripley leave The Judgment Day?",
            a="She did not leave &mdash; she was thrown out. On the Raw following SummerSlam 2024, dated "
              "August 3, 2024, Ripley and Damian Priest were removed from the group by the remaining "
              "members, the endpoint of the Dominik Mysterio and Liv Morgan storyline that had already "
              "cost Ripley the Women&rsquo;s World Championship in April. The two of them formed the "
              "Terror Twins afterwards, and the expulsion is what turned her babyface.",
            q_ld="Why did Rhea Ripley leave The Judgment Day?",
            a_ld="Rhea Ripley did not leave The Judgment Day; she was removed from it. On the Raw "
                 "following SummerSlam 2024, dated August 3, 2024, Rhea Ripley and Damian Priest were "
                 "thrown out of the group by the remaining members, the conclusion of the Dominik "
                 "Mysterio and Liv Morgan storyline that had already led to Rhea Ripley relinquishing "
                 "the Women's World Championship in April 2024. She and Damian Priest then formed the "
                 "Terror Twins."),
        dict(
            q="When did Rhea Ripley make her professional wrestling debut?",
            a="Four sources publish four answers, so no single date is asserted here. Wikipedia says "
              "<b>June 22, 2013</b>; TheSmackDownHotel says <b>June 29, 2013</b>; Pro Wrestling Fandom "
              "says <b>June 2013</b> with Riot City Wrestling; and F4W says <b>May 24, 2014</b> with New "
              "Horizon Pro Wrestling. Three of the four put it in June 2013 on the Australian "
              "independents as Demi Bennett, which is the most that can honestly be claimed. Her WWE "
              "signing followed in 2017. No source consulted names an individual trainer from her "
              "Australian years; Wikipedia credits the WWE Performance Center only.",
            q_ld="When did Rhea Ripley make her professional wrestling debut?",
            a_ld="Rhea Ripley's debut date is disputed across four published sources. Wikipedia gives "
                 "June 22, 2013; TheSmackDownHotel gives June 29, 2013; Pro Wrestling Fandom gives June "
                 "2013 with Riot City Wrestling; and F4W gives May 24, 2014 with New Horizon Pro "
                 "Wrestling. Three of the four place the debut in June 2013 on the Australian "
                 "independent scene, where she wrestled as Demi Bennett before signing with WWE in 2017. "
                 "No source consulted names an individual trainer from her Australian years; Wikipedia "
                 "credits only the WWE Performance Center."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Demi Bennett",
             sub="TheSmackDownHotel writes &ldquo;Demiti Bennett&rdquo;"),
        dict(label="Born", value="October 11, 1996", sub="Adelaide, South Australia"),
        dict(label="Billed from", value="Adelaide, South Australia", sub="WWE.com"),
        dict(label="Height", value="5&#8242;7&#8243;",
             sub="170 cm per WWE.com, Wikipedia and F4W &middot; 5&#8242;9&#8243; per TheSmackDownHotel"),
        dict(label="Weight", value="Disputed",
             sub="137 lb (F4W) &middot; 170 lb (TheSmackDownHotel) &middot; 154 lb on the previous "
                 "edition of this page &middot; WWE.com lists none"),
        dict(label="Debut", value="Disputed &mdash; June 2013 or May 2014",
             sub="Wikipedia June 22, 2013 &middot; TheSmackDownHotel June 29, 2013 &middot; Fandom "
                 "June 2013 (Riot City Wrestling) &middot; F4W May 24, 2014 (New Horizon Pro Wrestling)"),
        dict(label="Ring name from", value="July 13, 2017",
             sub="the Greek goddess Rhea and Ellen Ripley of <i>Alien</i>"),
        dict(label="Trained by", value="WWE Performance Center",
             sub="no individual Australian trainer is named in any source consulted"),
        dict(label="Finishers", value="Riptide &middot; Prism Trap",
             sub="pumphandle sit-out powerbomb &middot; standing inverted Texas cloverleaf, which "
                 "TheSmackDownHotel calls the &ldquo;Prison&rdquo;"),
        dict(label="Earlier finisher", value="Full Nelson Slam",
             sub="October 25, 2017 &ndash; August 27, 2019"),
        dict(label="Signatures", value="Big boot &middot; headbutt &middot; missile dropkick",
             sub="plus the Northern Lights suplex"),
        dict(label="Theme", value="Demon In Your Dreams",
             sub="def rebel feat. Motionless in White"),
        dict(label="Brand", value="SmackDown", sub="WWE.com"),
        dict(label="Also known as", value="Demi Bennett &middot; Mami &middot; The Nightmare &middot; "
                                          "The Eradicator",
             sub="all three nicknames remain in current use"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1996-10-11",
    bornplace="Adelaide, South Australia, Australia",
    nationality="Australia",
    height_cm=170,
    ld=dict(
        alternateName=["Demi Bennett", "Mami", "The Nightmare", "The Eradicator"],
        award=["WWE Women's Championship (2 reigns, 2021 as the Raw Women's Championship and 2026)",
               "Women's World Championship (2 reigns; the first, of 380 days, is tied with Bayley "
               "for the longest in the title's history)",
               "NXT Women's Championship (1 reign)",
               "NXT UK Women's Championship (1 reign, inaugural champion)",
               "WWE Women's Tag Team Championship (2 reigns, with Nikki A.S.H. and with Iyo Sky)",
               "Riot City Wrestling Women's Championship (2 reigns)",
               "Women's Royal Rumble winner (2023, from the number-one entry)",
               "Women's Elimination Chamber winner (2026)",
               "5th WWE Women's Grand Slam Champion",
               "7th WWE Women's Triple Crown Champion",
               "Pro Wrestling Illustrated number one in the Women's 250 (2023)",
               "Pro Wrestling Illustrated Woman of the Year (2023)",
               "Wrestling Observer Newsletter Women's Wrestling MVP (2023)",
               "WWE Slammy Award, Female Superstar of the Year (2024)"],
        knowsAbout=["Professional wrestling", "The Judgment Day", "WWE", "NXT UK",
                    "Championship wrestling", "Australian professional wrestling"],
        description="Rhea Ripley, born Demi Bennett in Adelaide, South Australia, is an Australian "
                    "professional wrestler signed to WWE and the reigning WWE Women's Champion. A "
                    "four-time world champion across two title lineages, she held the Women's World "
                    "Championship for 380 days between April 1, 2023 and April 15, 2024 — a figure tied "
                    "with Bayley's second reign for the longest in that title's history, and recognised "
                    "by WWE as 379 days for both. She was the inaugural NXT UK Women's Champion, the 5th "
                    "WWE Women's Grand Slam Champion at the age of 26, the 2023 women's Royal Rumble "
                    "winner from the number-one entry position, and a member of The Judgment Day from "
                    "May 2022 until August 2024.",
        sameAs=["https://x.com/rhearipley_wwe",
                "https://www.instagram.com/rhearipley_wwe/",
                "https://en.wikipedia.org/wiki/Rhea_Ripley",
                "https://www.wwe.com/superstars/rhea-ripley"],
    ),
)
