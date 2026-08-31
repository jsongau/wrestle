# -*- coding: utf-8 -*-
"""Lita - dossier data.

Compiled August 31, 2026. Sources are the web pages opened for this build
(Wikipedia, WWE.com profile, ITR Wrestling, 411Mania, WKDQ) plus verified
career history. She is a legend, not an active wrestler: the "now" fields
describe her real current standing — last match April 1, 2023, an April 2026
podcast statement that she is ready to face Iyo Sky, and convention bookings —
and invent no activity.

Deliberate omissions:
  * No career win-loss total — none verified.
  * One automated read of Wikipedia returned impossible dates for her fourth
    title reign (an "October 1" Cyber Sunday); the verified November 5, 2006
    Cyber Sunday date is used instead and the bad read is noted here rather
    than propagated.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2000-08-21", promo="WWE", landmark=True,
         event="Raw", opponent="Stephanie McMahon-Helmsley",
         stip="Singles, with The Rock as special referee — her first championship",
         title="WWF Women's Championship"),
    dict(result="L", date="2003-11-24", promo="WWE", landmark=True,
         event="Raw", opponent="Victoria",
         stip="The first women's steel cage match in Raw history",
         title=""),
    dict(result="W", date="2004-12-06", promo="WWE", landmark=True,
         event="Raw", opponent="Trish Stratus", opponent_html=True,
         stip="The first women's match to main event Raw — her second title",
         title="WWE Women's Championship"),
    dict(result="L", date="2005-01-09", promo="WWE",
         event="New Year's Revolution", opponent="Trish Stratus", opponent_html=True,
         stip="Singles — tore her ACL mid-match, and the reign ended with it",
         title="WWE Women's Championship"),
    dict(result="W", date="2006-08-14", promo="WWE",
         event="Raw", opponent="Mickie James",
         stip="Singles — a third title, in the Rated-R summer", title="WWE Women's Championship"),
    dict(result="L", date="2006-09-17", promo="WWE",
         event="Unforgiven — Toronto", opponent="Trish Stratus", opponent_html=True,
         stip="Trish's retirement match — the Sharpshooter ends it",
         title="WWE Women's Championship"),
    dict(result="W", date="2006-11-05", promo="WWE",
         event="Cyber Sunday", opponent="Mickie James",
         stip="Wins the title Trish vacated — her fourth and final reign",
         title="WWE Women's Championship"),
    dict(result="L", date="2006-11-26", promo="WWE", landmark=True,
         event="Survivor Series", opponent="Mickie James",
         stip="Her retirement match — the full-time career ends",
         title="WWE Women's Championship"),
    dict(result="L", date="2018-01-28", promo="WWE", type="tag", landmark=True,
         event="Royal Rumble", opponent="The first women's Royal Rumble field",
         stip="Part of the historic first field, twelve years after retiring", title=""),
    dict(result="W", date="2018-10-28", promo="WWE", type="tag", landmark=True,
         event="Evolution", opponent="Mickie James & Alicia Fox",
         stip="With Trish Stratus, at WWE's first all-women pay-per-view", title=""),
    dict(result="L", date="2022-01-29", promo="WWE", type="tag",
         event="Royal Rumble", opponent="The 2022 women's Rumble field",
         stip="A surprise entry at 46", title=""),
    dict(result="L", date="2022-02-19", promo="WWE",
         event="Elimination Chamber — Jeddah", opponent="Becky Lynch", opponent_html=True,
         stip="Singles — a Raw Women's Championship challenge, and a standing ovation",
         title="Raw Women's Championship"),
    dict(result="W", date="2023-02-27", promo="WWE", type="tag", landmark=True,
         event="Raw", opponent="Dakota Kai & Iyo Sky",
         stip="With Becky Lynch — tag team gold, seventeen years after her last title",
         title="WWE Women's Tag Team Championship"),
    dict(result="W", date="2023-04-01", promo="WWE", type="tag",
         event="WrestleMania 39 Night 1", opponent="Damage CTRL",
         stip="Six-woman tag with Becky Lynch & Trish Stratus — her most recent match", title=""),
]

# opponent_html rows carry a real <a>, so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Trish Stratus": "trish-stratus", "Becky Lynch": "becky-lynch"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="lita",
    name="Lita",
    realname="Amy Christine Dumas",
    epithet="The Extreme Diva",
    hook="Record & Titles",

    meta_desc=("Lita, the Extreme Diva, won four WWE Women's Championships, main-evented Raw in the "
               "first women's match to do it, and moonsaulted a generation of fans into wrestling. "
               "Full record, titles, factions, records and career."),
    og_desc=("The Extreme Diva: 4 Women's Championship reigns, the first women's Raw main event, the "
             "first women's steel cage match on Raw, the Hall of Fame in 2014 — and tag gold with "
             "Becky Lynch at 47."),
    tw_desc="Lita: 4 Women's titles, the first women's Raw main event, HOF 2014 — and gold again in 2023.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1998",
    height_imp="5&#8242;6&#8243;",
    weight_lb="135",
    world_titles="4",
    vitals_tagline="The Extreme Diva",
    support_note="Merch &middot; Music &middot; Meet",
    x_url="https://x.com/AmyDumas",
    ig_url="https://www.instagram.com/machetegirl/",
    sp_items=[
        dict(ic="LT", title="Lita Merch", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="LG", title="The Luchagors", sub="Her punk band — debut album 2007",
             tag="Listen", href="https://en.wikipedia.org/wiki/The_Luchagors"),
        dict(ic="RC", title="Evansville Raptor Con", sub="Meet & greet · September 12-13, 2026",
             tag="Meet", href="https://wkdq.com/wwe-lita-evansville-raptor-con/"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/lita"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Team Xtreme &middot; the moonsault &middot; four-time champion &middot; Hall of Fame 2014",
    hero_tag="Fort Lauderdale, Florida &middot; billed from Sanford, North Carolina &middot; "
             "<em>Mexico &middot; ECW &middot; WWF/WWE &middot; 1998&ndash;present</em>",
    now_label="NOW",
    now_bold="Legend — last match April 1, 2023",
    now_tail=" &middot; said on Busted Open in April 2026 she is ready to come back to face Iyo Sky; "
             "meanwhile it's podcasts, panels and a September convention in Evansville",
    hstats=[
        dict(value="4",   x=True,  label="Women's Titles"),
        dict(value="1st", x=False, label="Women's Raw Main Event"),
        dict(value="2014", x=False, label="Hall of Fame Class"),
        dict(value="1",   x=True,  label="Tag Title Reign"),
    ],
    ghost_link="From lucha libre fan with a one-way ticket to the Hall of Fame",
    vlabel="Est. 1998 &middot; via Mexico City",
    mono="LT",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Lita</b> got into wrestling by buying a ticket to Mexico City because she liked how "
        "lucha libre looked, and everything about the career that followed kept that shape: "
        "self-taught momentum over polish, a moonsault in an era of headlocks, thong-strap jeans in "
        "an era of evening gowns. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">4</span>'
        '<span class="pull-cap">WWE Women&rsquo;s Championship reigns between 2000 and 2006 &mdash; and a tag title seventeen years later</span></span>'
        "The concrete record: four WWF/WWE Women's Championship reigns between 2000 and 2006, the "
        "first women's match to main event Raw, the first women's steel cage match in Raw history, "
        "the 2014 Hall of Fame, and &mdash; the late plot twist &mdash; a WWE Women's Tag Team "
        "Championship won with Becky Lynch in 2023, seventeen years after her last title and "
        "twenty-three years after her first.",

        "One thing needs setting straight about how her 2023 run ended, because even the sources "
        "half-garble it. Her <b>last match is the WrestleMania 39 six-woman tag on April 1, "
        "2023</b> &mdash; the win with Becky Lynch and Trish Stratus over Damage CTRL &mdash; and "
        "<i>not</i> the April 10 Raw where the tag titles were lost. She was not in that match: "
        "she was taken out backstage beforehand in the angle that seeded Trish Stratus's heel "
        "turn, Lynch defended with a substitute, and the belts went to Liv Morgan and Raquel "
        "Rodriguez. 411Mania states it plainly &mdash; she has not competed since WrestleMania 39 "
        "and was written off television via the attack. So the tag reign's dates (February 27 to "
        "April 10, 2023) outrun her own last bell by nine days, a distinction almost every "
        "capsule bio flattens. One further note on this page's own sourcing: an automated read of "
        "Wikipedia returned an impossible date for her fourth title win; the verified Cyber "
        "Sunday date of November 5, 2006 is used instead.",

        "She was born Amy Christine Dumas on April 14, 1975 in Fort Lauderdale, found lucha libre "
        "on television, and went to Mexico in the late 1990s to learn it &mdash; debuting in 1998 "
        "and passing through ECW in 1999 before the WWF signed her. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">2000</span>'
        '<span class="pull-cap">the year of Team Xtreme, the Stephanie McMahon title win, and the moonsault that minted a generation of fans</span></span>'
        "Paired with Matt and Jeff Hardy as <b>Team Xtreme</b>, she became the rare valet who "
        "outdrew her team: the August 21, 2000 Raw title win over Stephanie McMahon-Helmsley, with "
        "The Rock refereeing, made her champion inside six months of her television debut. The "
        "years that followed were defined by the Trish Stratus rivalry &mdash; ringside brawls in "
        "2000, the first women's Raw main event on December 6, 2004, which Lita won for her "
        "second title, and the Unforgiven 2006 retirement match she lost &mdash; and by a broken "
        "neck in 2002, suffered filming a television stunt, that cost her a year and a half at "
        "her peak.",

        "The 2005&ndash;06 heel run &mdash; the real-life Edge storyline turned on-screen "
        "&ldquo;Rated-R&rdquo; era &mdash; made her the most jeered woman in the company, and her "
        "November 26, 2006 retirement match at Survivor Series was played as a heel's send-off "
        "rather than a farewell. Wrestling spent the next two decades correcting that. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">47</span>'
        '<span class="pull-cap">her age winning the WWE Women&rsquo;s Tag Team Championship with Becky Lynch, February 27, 2023</span></span>'
        "The 2014 Hall of Fame induction &mdash; by Trish Stratus &mdash; the first women's Royal "
        "Rumble in 2018, the Evolution tag win, the 2022 Elimination Chamber title challenge "
        "against Becky Lynch that ended in a standing ovation, and the 2023 tag championship all "
        "recast her as what she had actually been all along: the template for every high-flying, "
        "alternative-styled woman who came after. As of August 31, 2026 she is a legend at large "
        "&mdash; on Busted Open in April she named Iyo Sky as the one opponent she would come "
        "back for, and no such match is booked.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Highlight set",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("4&times;", "Women's titles"),
            ("1&times;", "Tag titles, 2023"),
            ("1st",      "Women's Raw main event"),
            ("1st",      "Women's cage match on Raw"),
            ("2014",     "Hall of Fame"),
            ("2023",     "Most recent match"),
        ],
        lead=("Fourteen documented bouts across twenty-three years &mdash; a highlight subset, not "
              "a career count, and no career win&ndash;loss total is published because none was "
              "verified; the Mexico and ECW years are outside this ledger entirely. Note the "
              "boundary flagged in the overview: the April 10, 2023 tag title loss is absent "
              "because she was not in that match &mdash; her last bout is the WrestleMania 39 "
              "six-woman tag. Filter by match type, tap any column header to sort, and turn "
              "spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("Four bouts the reputation rests on. The ratings are this dossier's own "
                    "editorial grades, not Wrestling Observer figures &mdash; no Meltzer ratings "
                    "were verified in this pass and none are quoted."),
    signature=[
        dict(rating="4.0", event="Raw, December 6, 2004", opponent="Trish Stratus",
             stip="The first women's main event in Raw history — she won the title"),
        dict(rating="3.5", event="Raw, November 24, 2003", opponent="Victoria",
             stip="The first women's steel cage match in Raw history"),
        dict(rating="3.5", event="Unforgiven 2006", opponent="Trish Stratus",
             stip="Trish's retirement match in Toronto — the rivalry's last word"),
        dict(rating="3.5", event="Elimination Chamber 2022", opponent="Becky Lynch",
             stip="Raw Women's Championship challenge at 46 — the ovation return"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("4&times;", "Women's title reigns"),
            ("1&times;", "Tag title reign"),
            ("17",       "Years between titles"),
            ("2014",     "Hall of Fame"),
        ],
        lead=("Four reigns with the original Women's Championship and one late-career tag reign "
              "&mdash; the seventeen-year gap between belts is believed to be among the longest "
              "of any woman in WWE history, though no source states a formal record and none is "
              "claimed."),
        rows=[
            dict(ic="W", name="WWF/WWE Women's Championship", count="4",
                 sub="2000, def. Stephanie McMahon-Helmsley on the August 21 Raw with The Rock "
                     "refereeing &mdash; 73 days &middot; 2004&ndash;05, def. Trish Stratus on "
                     "December 6 in the first women's Raw main event &mdash; ended at New "
                     "Year's Revolution on January 9, where she tore her ACL mid-match &middot; "
                     "2006, def. Mickie James on the August 14 Raw &mdash; lost to Trish "
                     "Stratus's retirement match at Unforgiven &middot; 2006, def. Mickie James "
                     "at Cyber Sunday on November 5 for the vacated title &mdash; lost to James "
                     "at Survivor Series on November 26, her retirement match"),
            dict(ic="T", name="WWE Women's Tag Team Championship", count="1",
                 sub="2023, with Becky Lynch &middot; won from Damage CTRL's Dakota Kai & Iyo "
                     "Sky on the February 27 Raw at age 47 &middot; the reign ended April 10 "
                     "against Liv Morgan & Raquel Rodriguez in a match Lita was written out of "
                     "via backstage attack &mdash; the becky-lynch dossier on this site logs "
                     "the reign as 41 or 42 days depending on the table"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="The team that defined an era of television, the storyline that defined a tabloid "
             "one, and the late alliance that got her gold again.",
        cards=[
            dict(era="WWF/WWE &middot; 2000&ndash;05",
                 name="Team Xtreme",
                 members="Matt Hardy, Jeff Hardy, Lita",
                 desc="The Hardy Boyz plus the valet who wrestled like a third Hardy. The trio "
                      "was arguably the most popular act of the early-2000s youth audience, and "
                      "Lita's moonsaults off their ladders are the reason a generation of women "
                      "cite her as the way in. WWE.com dates the partnership across roughly "
                      "five years."),
            dict(era="WWE &middot; 2005&ndash;06",
                 name="Edge & Lita",
                 members="Edge, Lita",
                 desc="The \"Rated-R\" pairing that grew out of a real-life story WWE chose to "
                      "put on television, making her the company's most-booed performer and, in "
                      "commercial terms, one of its most effective heels. It produced her 2006 "
                      "title reigns, the live \"celebration\" segment that still gets cited in "
                      "every retrospective on the era's excesses, and the heel-exit framing of "
                      "her retirement."),
            dict(era="WWE &middot; 2018&ndash;23",
                 name="Team Bestie / the Becky alliance",
                 members="Lita, Trish Stratus; later Becky Lynch",
                 desc="The legends' wing: Evolution 2018 with Trish, then the 2023 Becky Lynch "
                      "alliance that delivered the tag championship and the WrestleMania 39 "
                      "six-woman win over Damage CTRL — before the backstage-attack angle "
                      "wrote her out and turned Trish heel. Her last on-screen chapter to "
                      "date."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One name from the WWF debut onward &mdash; the eras are marked by who she stood "
             "next to.",
        cards=[
            dict(mono="AN", era="Mexico & ECW &middot; 1998&ndash;99", name="Angelica / Miss Congeniality",
                 desc="The self-financed apprenticeship: to Mexico as Angelica after falling for "
                      "lucha libre on TV, then ECW as Miss Congeniality — trained along the way "
                      "by names including Dory Funk Jr. and Ricky Santana. The high-risk style "
                      "was set before WWF ever saw her."),
            dict(mono="TX", era="WWF/WWE &middot; 2000&ndash;04", name="The Team Xtreme original",
                 desc="Cargo pants, thong straps, the moonsault. Champion within six months of "
                      "her TV debut, and half of the Trish rivalry that carried the division. A "
                      "broken neck in 2002 — from a television stunt, not a match — took a year "
                      "and a half out of the peak."),
            dict(mono="RR", era="WWE &middot; 2005&ndash;06", name="The Rated-R era",
                 desc="The heel run alongside Edge, engineered out of real-life tabloid material "
                      "and played to the loudest boos in the company. Two more title reigns, "
                      "and a retirement at Survivor Series 2006 staged as a villain's ejection "
                      "— the send-off the following two decades kept apologising for."),
            dict(mono="HF", era="2014&ndash;present", name="The Hall of Famer",
                 desc="Inducted in 2014 by Trish Stratus, and since then the division's favorite "
                      "returning legend: the first women's Rumble, Evolution, the 2022 ovation "
                      "match with Becky Lynch, tag gold at 47 in 2023 — and, in April 2026, a "
                      "public offer to lace up once more if the opponent is Iyo Sky."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="A one-way ticket to Mexico City to the Hall of Fame, with a broken neck and a "
             "punk band in the middle.",
        rows=[
            dict(year="1998", title="Debuts in Mexico",
                 desc="Self-financed training trips to Mexico after discovering lucha libre; "
                      "debuts as Angelica, with ECW appearances following in 1999."),
            dict(year="2000", title="Team Xtreme, and a title in six months",
                 desc="Debuts with the WWF in February, pairs with the Hardy Boyz, and beats "
                      "Stephanie McMahon-Helmsley for the Women's Championship on the August 21 "
                      "Raw with The Rock as referee."),
            dict(year="2002", title="The broken neck",
                 desc="Fractures her neck filming a stunt for the TV series Dark Angel; out "
                      "roughly a year and a half at the height of her popularity."),
            dict(year="2003", title="The cage first",
                 desc="Returns and wrestles Victoria in the first women's steel cage match in "
                      "Raw history on November 24."),
            dict(year="2004", title="The Raw main event",
                 desc="Beats Trish Stratus on December 6 in the first women's match to main "
                      "event Raw, winning her second Women's Championship."),
            dict(year="2006", title="Two titles, and a heel's goodbye",
                 desc="Wins the title in August and again at Cyber Sunday in November amid the "
                      "Rated-R storyline, then retires at Survivor Series on November 26, "
                      "dropping the belt to Mickie James. The Luchagors' debut album lands the "
                      "following September."),
            dict(year="2014", title="Hall of Fame",
                 desc="Inducted by Trish Stratus — the rivalry formally recast as a "
                      "partnership."),
            dict(year="2018", title="The Rumble and Evolution",
                 desc="Enters the first women's Royal Rumble on January 28, and wins the "
                      "Evolution tag alongside Trish on October 28."),
            dict(year="2022", title="The ovation match",
                 desc="A surprise Rumble entry, then a Raw Women's Championship challenge to "
                      "Becky Lynch at Elimination Chamber on February 19 — a loss received "
                      "with a standing ovation."),
            dict(year="2023", title="Champion again at 47",
                 desc="Wins the Women's Tag Team Championship with Becky Lynch on February 27 "
                      "and the WrestleMania 39 six-woman on April 1 — her last match — before "
                      "the backstage-attack angle writes her out on April 10."),
            dict(year="2026", title="Legend at large",
                 desc="Talks legacy on the No Holds Barred podcast in February; names Iyo Sky "
                      "as her dream comeback opponent on Busted Open in April; booked for "
                      "Evansville's Raptor Con in September. No match is scheduled."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who she went to war with.",
        cards=[
            dict(name="Trish Stratus", slug="trish-stratus",
                 desc="The rivalry that built the division's ceiling: 2000 valet brawls, the "
                      "December 6, 2004 Raw main event Lita won, the New Year's Revolution "
                      "rematch where her knee gave out, and Trish's 2006 retirement match in "
                      "Toronto, which Lita lost. Then the reversal — Trish inducted her into "
                      "the Hall of Fame in 2014, they won Evolution as partners, and the 2023 "
                      "angle that ended Lita's run was built on Trish turning heel. Twenty-six "
                      "years, and the story still is not over."),
            dict(name="Mickie James",
                 desc="The opponent on both ends of her final act: Lita beat James for the "
                      "title twice in 2006 — August, and Cyber Sunday in November — and James "
                      "took the belt back at Survivor Series in Lita's retirement match, the "
                      "crowd gleefully waving her out. They met once more on opposite sides at "
                      "Evolution 2018."),
            dict(name="Victoria",
                 desc="The workhorse rivalry of the comeback-from-the-broken-neck era, "
                      "producing the first women's steel cage match in Raw history on November "
                      "24, 2003 — which Victoria won, a detail this page keeps because the "
                      "milestone mattered more than the result."),
            dict(name="Becky Lynch", slug="becky-lynch",
                 desc="Idol and inheritor: Lynch has been explicit that Lita is a foundational "
                      "influence, and their 2022 Elimination Chamber title match doubled as a "
                      "torch-passing ceremony with an ovation for the loser. A year later they "
                      "were tag champions together. If the Iyo Sky comeback ever happens, it "
                      "will be because this alliance proved she could still go."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Music",
        lead="The only Hall of Famer in this database with a punk discography.",
        rows=[
            dict(when="2006&ndash;", title="The Luchagors", kind="Music",
                 desc="Her Atlanta punk band, fronted by Lita, with a self-titled debut album "
                      "released September 11, 2007 — started in the immediate afterlife of the "
                      "2006 retirement."),
            dict(when="2002", title="Dark Angel", kind="TV",
                 desc="The stunt-double work on the Fox series where she fractured her neck — "
                      "the injury that reshaped the middle of her career. Listed because it "
                      "changed the record more than most matches did."),
            dict(when="2014&ndash;", title="WWE legend programming", kind="TV",
                 desc="Hall of Fame 2014, recurring appearances across WWE documentary and "
                      "countdown programming, and the modern podcast circuit — No Holds Barred "
                      "in February 2026, Busted Open in April 2026 alongside Trish Stratus and "
                      "Kaitlyn."),
            dict(when="2017&ndash;", title="WWE 2K", kind="Game",
                 desc="A recurring playable legend in the WWE 2K series."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The firsts are the record &mdash; she collected television milestones the way "
             "others collect belts.",
        stats=[
            ("1st", "Women's Raw main event"),
            ("1st", "Women's cage match on Raw"),
            ("4",   "Women's title reigns"),
        ],
        rows=[
            dict(name="Half of the first women's match to main event Raw",
                 sub="December 6, 2004, against Trish Stratus — and Lita won it, taking her "
                     "second Women's Championship. The milestone is shared with Stratus the "
                     "way all match milestones are; the victory is not."),
            dict(name="Half of the first women's steel cage match in Raw history",
                 sub="November 24, 2003, against Victoria — a match she lost, printed here "
                     "with the result attached."),
            dict(name="Four WWF/WWE Women's Championship reigns, 2000-2006",
                 sub="Won from Stephanie McMahon-Helmsley, Trish Stratus, and Mickie James "
                     "twice. The first came within six months of her television debut."),
            dict(name="A title seventeen years after her previous one",
                 sub="The Women's Tag Team Championship with Becky Lynch, February 27, 2023, "
                     "at age 47 — seventeen years after her fourth Women's Championship "
                     "reign ended in November 2006. Believed to be among the longest gaps "
                     "between championships for any woman in company history; no source "
                     "formalises the record, so it is stated as a gap, not a title."),
            dict(name="Hall of Fame, Class of 2014",
                 sub="Inducted by Trish Stratus — the two anchor rivalries of the era "
                     "formally reconciled on stage."),
            dict(name="Part of the first women's Royal Rumble, 2018",
                 sub="Twelve years after retiring — one of the returns that established the "
                     "match's legend-entrant tradition alongside Trish Stratus's No. 30 "
                     "entry."),
            dict(name="The template claim",
                 sub="Routinely cited — including by Becky Lynch — as the foundational "
                     "influence for the high-flying, alternative-presentation generation "
                     "that followed. Printed as attributed influence, not as a "
                     "measurable."),
        ],
        footnote=("No career win-loss total appears anywhere on this page; none was verified, "
                  "and the Mexico/ECW record is undocumented in the sources used. One source "
                  "correction is logged in the module docstring: an automated Wikipedia read "
                  "returned an impossible date for the fourth title reign, and the verified "
                  "November 5, 2006 Cyber Sunday date is published instead."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="X / Twitter", v="@AmyDumas", href="https://x.com/AmyDumas"),
        dict(k="Instagram", v="@machetegirl", href="https://www.instagram.com/machetegirl/"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Lita_(wrestler)"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/lita"),
        dict(k="ITR Wrestling", v="Ready to return — naming Iyo Sky, April 2026",
             href="https://itrwrestling.com/news/lita-ready-for-wwe-return-to-face-7-time-champion/"),
        dict(k="411Mania", v="On legacy and following the product, February 2026",
             href="https://411mania.com/wrestling/lita-if-she-follows-wwe-product-legacy-more/"),
        dict(k="WKDQ", v="Evansville Raptor Con appearance, September 2026",
             href="https://wkdq.com/wwe-lita-evansville-raptor-con/"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/lita.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Lita still wrestling, and will she return?",
            a="She has not wrestled since the WrestleMania 39 six-woman tag on <b>April 1, "
              "2023</b>, but she has publicly left the door open: on the Busted Open podcast in "
              "April 2026 &mdash; appearing alongside Trish Stratus and Kaitlyn &mdash; she "
              "said she is ready for a comeback and named <b>Iyo Sky</b> as the opponent, a "
              "singles match the two have never had despite crossing paths in the 2023 tag "
              "division. As of August 31, 2026 no match is scheduled; her calendar is "
              "conventions and podcasts, including Evansville's Raptor Con on September "
              "12&ndash;13.",
            q_ld="Is Lita still wrestling, and will she return to WWE?",
            a_ld="Lita has not wrestled since the WrestleMania 39 six-woman tag match on April "
                 "1, 2023. In April 2026, on the Busted Open podcast, she said she is ready "
                 "for a WWE comeback and named Iyo Sky as the opponent she wants, a singles "
                 "match they have never had. As of August 31, 2026 no match has been "
                 "scheduled, and her current appearances are conventions and podcasts."),
        dict(
            q="What was Lita's last match — and was it the tag title loss?",
            a="No, and the distinction is worth keeping. Her last match is the <b>WrestleMania "
              "39 Night 1 six-woman tag on April 1, 2023</b>, won with Becky Lynch and Trish "
              "Stratus over Damage CTRL. The tag titles she held with Lynch were lost on the "
              "<b>April 10, 2023 Raw</b> to Liv Morgan and Raquel Rodriguez &mdash; a match "
              "Lita was not in, having been taken out backstage in the angle that set up "
              "Trish Stratus's heel turn. So her reign outlasted her last bell by nine days, "
              "and she left television as a champion who never lost the belts in the ring.",
            q_ld="What was Lita's last match?",
            a_ld="Lita's last match was the WrestleMania 39 Night 1 six-woman tag on April 1, "
                 "2023, which she won alongside Becky Lynch and Trish Stratus against Damage "
                 "CTRL. She was not in the April 10, 2023 match where she and Lynch lost the "
                 "WWE Women's Tag Team Championship to Liv Morgan and Raquel Rodriguez; she "
                 "had been written off television via a backstage attack angle beforehand."),
        dict(
            q="How many championships did Lita win?",
            a="Five in WWE: <b>four WWF/WWE Women's Championship reigns</b> &mdash; 2000 (from "
              "Stephanie McMahon-Helmsley, with The Rock refereeing), 2004 (from Trish Stratus "
              "in the first women's Raw main event), and twice from Mickie James in 2006 "
              "&mdash; plus the <b>WWE Women's Tag Team Championship</b> with Becky Lynch in "
              "2023, won at 47, seventeen years after her previous title. Her Mexico and ECW "
              "years produced no documented championships in the sources used for this page.",
            q_ld="How many championships did Lita win in WWE?",
            a_ld="Lita won five championships in WWE: four WWF/WWE Women's Championship reigns "
                 "(2000, 2004, and twice in 2006) and one WWE Women's Tag Team Championship "
                 "reign with Becky Lynch in 2023, won seventeen years after her fourth "
                 "Women's Championship reign ended."),
        dict(
            q="Why did Lita retire in 2006?",
            a="She chose to leave &mdash; burnout with the character's direction and life on "
              "the road, in the middle of the Rated-R storyline that had turned real-life "
              "tabloid material into television and made her the most jeered performer in the "
              "company. WWE booked the exit as a heel's comeuppance: she dropped the title to "
              "Mickie James at Survivor Series on November 26, 2006 and was mocked out of the "
              "arena. The two decades since &mdash; the Hall of Fame, Evolution, the 2022 "
              "ovation, the 2023 title &mdash; have functioned as the farewell the original "
              "never was.",
            q_ld="Why did Lita retire from WWE in 2006?",
            a_ld="Lita chose to leave WWE in 2006, citing burnout with the direction of her "
                 "character and life on the road during the Rated-R storyline era. Her "
                 "retirement match was a loss to Mickie James at Survivor Series on November "
                 "26, 2006, staged as a heel's send-off. Her later returns, Hall of Fame "
                 "induction and 2023 tag championship served as the proper farewell."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Amy Christine Dumas"),
        dict(label="Born", value="April 14, 1975", sub="Fort Lauderdale, Florida &middot; age 51"),
        dict(label="Billed from", value="Sanford, North Carolina", sub="per WWE.com"),
        dict(label="Height", value="5&#8242;6&#8243;", sub="168 cm"),
        dict(label="Weight", value="135 lb", sub="61 kg &middot; as historically billed"),
        dict(label="Debut", value="1998", sub="Mexico, as Angelica; ECW in 1999 as Miss Congeniality"),
        dict(label="WWF debut", value="February 2000", sub="first as Essa Rios' valet"),
        dict(label="Trained by", value="Dory Funk Jr. &middot; Ricky Santana &middot; Kevin Quinn "
                                       "&middot; El Dandy"),
        dict(label="Retired", value="November 26, 2006", sub="Survivor Series &mdash; returns since"),
        dict(label="Last match", value="April 1, 2023",
             sub="W, WrestleMania 39 six-woman tag, with Becky Lynch & Trish Stratus"),
        dict(label="Finishers", value="Moonsault &middot; Litacanrana &middot; Twist of Fate"),
        dict(label="Hall of Fame", value="Class of 2014", sub="inducted by Trish Stratus"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1975-04-14",
    bornplace="Fort Lauderdale, Florida, United States",
    nationality="United States",
    height_cm=168,
    weight_kg=61,
    ld=dict(
        alternateName=["Amy Christine Dumas", "Amy Dumas", "Angelica", "Miss Congeniality",
                       "The Extreme Diva"],
        award=["WWF/WWE Women's Championship (4 reigns, 2000-2006)",
               "WWE Women's Tag Team Championship (1 reign, with Becky Lynch, 2023)",
               "WWE Hall of Fame (Class of 2014)",
               "First women's match to main event Raw (December 6, 2004, winner)",
               "First women's steel cage match in Raw history (November 24, 2003)"],
        knowsAbout=["Professional wrestling", "WWE", "Lucha libre", "Women's professional wrestling",
                    "Punk rock", "High-flying wrestling"],
        description="Lita, born Amy Christine Dumas, is an American professional wrestler and 2014 "
                    "WWE Hall of Famer. A four-time WWF/WWE Women's Champion between 2000 and "
                    "2006, she won the first women's match to main event Raw, competed in the "
                    "first women's steel cage match in Raw history, and defined the high-flying "
                    "style of her generation as part of Team Xtreme with the Hardy Boyz. She won "
                    "the WWE Women's Tag Team Championship with Becky Lynch in 2023 at age 47, "
                    "and her last match was the WrestleMania 39 six-woman tag on April 1, 2023.",
        sameAs=["https://x.com/AmyDumas",
                "https://www.instagram.com/machetegirl/",
                "https://en.wikipedia.org/wiki/Lita_(wrestler)",
                "https://www.wwe.com/superstars/lita"],
    ),
)
