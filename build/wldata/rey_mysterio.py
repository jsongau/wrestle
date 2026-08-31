# -*- coding: utf-8 -*-
"""Rey Mysterio - dossier data.

Sources: web-verified August 31, 2026 (Wikipedia; Wrestling Inc and Wrestlezone on
the August 17, 2026 Intercontinental title match; Yahoo Sports on the WrestleMania 42
return and the Royal Rumble 2026 injury; Slam Wrestling; Fightful on the WrestleMania
42 ladder match; Sportskeeda's championship ledger). Every match row carries a
day-precision date.

Deliberate omissions:
  * No career win-loss total - none verified across 37 years, none invented.
  * The WCW Cruiserweight reign count conflicts across sources (five vs. six); the
    conflict is flagged in the titles section rather than silently resolved.
  * No social links - handles were not verified in this pass.
  * No Observer star ratings - none verified against archives in this pass.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2002-07-25", promo="WWE", landmark=True,
         event="SmackDown", opponent="Chavo Guerrero",
         stip="Singles — WWE debut, mask restored after three unmasked WCW years", title=""),
    dict(result="W", date="2006-01-29", promo="WWE", landmark=True, type="tag",
         event="Royal Rumble — Miami", opponent="The 2006 Royal Rumble field",
         stip="Entered No. 2, lasted 62 minutes, won — dedicated to Eddie Guerrero", title=""),
    dict(result="W", date="2006-04-02", promo="WWE", landmark=True, type="tag",
         event="WrestleMania 22 — Chicago", opponent="Kurt Angle & Randy Orton",
         stip="Triple threat — first World Heavyweight Championship, pinning Orton", title="World Heavyweight Championship"),
    dict(result="W", date="2009-04-05", promo="WWE",
         event="WrestleMania 25 — Houston", opponent="JBL",
         stip="Singles — wins the Intercontinental Championship in 21 seconds", title="WWE Intercontinental Championship"),
    dict(result="L", date="2009-06-07", promo="WWE",
         event="Extreme Rules — New Orleans", opponent="Chris Jericho",
         stip="No holds barred — Jericho takes the title and keeps grabbing at the mask", title="WWE Intercontinental Championship"),
    dict(result="W", date="2009-06-28", promo="WWE", landmark=True,
         event="The Bash — Sacramento", opponent="Chris Jericho",
         stip="Title vs. mask — unmasks Jericho mid-springboard and regains the title", title="WWE Intercontinental Championship"),
    dict(result="W", date="2010-06-20", promo="WWE", type="tag",
         event="Fatal 4-Way — Uniondale", opponent="Big Show, CM Punk & Jack Swagger",
         stip="Four-way — a second World Heavyweight Championship", title="World Heavyweight Championship"),
    dict(result="W", date="2011-07-25", promo="WWE", landmark=True,
         event="Raw — Hampton", opponent="The Miz",
         stip="Tournament final — wins the vacant WWE Championship", title="WWE Championship"),
    dict(result="L", date="2011-07-25", promo="WWE",
         event="Raw — Hampton", opponent="John Cena",
         stip="Singles, the same night — the shortest-lived of his world reigns", title="WWE Championship"),
    dict(result="W", date="2019-05-19", promo="WWE",
         event="Money in the Bank — Hartford", opponent="Samoa Joe",
         stip="Singles — a United States Championship at 44", title="WWE United States Championship"),
    dict(result="W", date="2021-05-16", promo="WWE", landmark=True, type="tag",
         event="WrestleMania Backlash", opponent="Dolph Ziggler & Robert Roode",
         stip="Tag, with Dominik — WWE's first father-and-son tag team champions", title="WWE SmackDown Tag Team Championship"),
    dict(result="W", date="2023-04-01", promo="WWE", landmark=True,
         event="WrestleMania 39 Night 1 — Los Angeles", opponent="Dominik Mysterio",
         stip="Singles — father versus son, two nights after his Hall of Fame induction", title=""),
    dict(result="L", date="2026-01-31", promo="WWE", type="tag",
         event="Royal Rumble — Riyadh", opponent="The 2026 Royal Rumble field",
         stip="Entered No. 4 on a bad knee, eliminated by Oba Femi at 2:43 — followed by months out", title=""),
    dict(result="L", date="2026-04-19", promo="WWE", landmark=True, type="tag",
         event="WrestleMania 42 Night 2 — Las Vegas", opponent="Penta, Je'Von Evans, Dragon Lee, JD McDonagh & Rusev",
         stip="Six-man ladder match — Penta retains; Mysterio, 51, feeds Rusev a West Coast Pop through a ladder", title="WWE Intercontinental Championship"),
    dict(result="L", date="2026-08-17", promo="WWE", landmark=True,
         event="Raw", opponent="Chad Gable",
         stip="Singles — Gable's first defense; a reversed roll-up out of duelling ankle locks", title="WWE Intercontinental Championship"),
]

DATA = dict(
    slug="rey-mysterio",
    name="Rey Mysterio",
    realname="Oscar Gutierrez Rubio",
    epithet="The Master of the 619",
    hook="Record & Titles",

    meta_desc=("Rey Mysterio - three world championships, the 2006 Royal Rumble, a Hall of Fame "
               "ring while still active, and an Intercontinental title challenge at 51 in August "
               "2026. Full record, titles, factions and career."),
    og_desc=("The Master of the 619: lucha libre's greatest export - three world titles, the 2006 "
             "Royal Rumble from No. 2, WWE's first father-son tag champions, and still wrestling "
             "title matches at 51 in 2026."),
    tw_desc="Three world titles, one mask, 37 years - and still challenging for gold at 51.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1989",
    height_imp="5&#8242;6&#8243;",
    weight_lb="175",
    world_titles="3",
    vitals_tagline="The biggest little man",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="RM", title="WWE Shop", sub="Masks, jerseys and the 619 line",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K22", sub="Cover star of the 2K22 edition",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="TV", title="WWE Raw", sub="Where he wrestles now",
             tag="Watch", href="https://www.wwe.com/"),
        dict(ic="HOF", title="Hall of Fame, Class of 2023", sub="Inducted while a full-time active wrestler",
             charity=True, tag="Visit", href="https://www.wwe.com/shows/wwehalloffame"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Rey Misterio Jr. &middot; lucha libre&rsquo;s greatest export",
    hero_tag="San Diego, California &middot; <em>AAA &middot; ECW &middot; WCW &middot; WWE &middot; 1989&ndash;present</em>",
    now_label="NOW",
    now_bold="Raw, active at 51",
    now_tail=" &middot; came up just short against Intercontinental Champion Chad Gable on August 17, 2026 &mdash; who called him &ldquo;a human being like no other&rdquo; afterward",
    hstats=[
        dict(value="3", x=True, label="World Titles"),
        dict(value="2006", x=False, label="Royal Rumble Win"),
        dict(value="619", x=False, label="The Signature"),
        dict(value="37", x=False, label="Years a Pro"),
    ],
    ghost_link="From a Tijuana ring at 14 to a title match at 51",
    vlabel="Est. 1989 &middot; San Diego, CA",
    mono="RM",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Rey Mysterio</b> is the argument, in one 5&#8242;6&#8243; person, that size was always "
        "a booking convention rather than a law. He debuted at <b>14</b>, on April 30, 1989, "
        "trained by his uncle Rey Misterio; he is still an active WWE wrestler at <b>51</b>, "
        "having wrestled a ladder match at WrestleMania 42 in April 2026 and an Intercontinental "
        "Championship match on the August 17, 2026 Raw. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">3</span>'
        '<span class="pull-cap">world championship reigns &mdash; two World Heavyweight, one WWE &mdash; every one of them won as the smallest man in the match</span></span>'
        "In between: three world championships, the "
        "2006 Royal Rumble, two Intercontinental and three United States Championships, WWE&rsquo;s "
        "21st Grand Slam, the first father-and-son tag team title reign in company history, and a "
        "2023 Hall of Fame induction he attended as a full-time active wrestler &mdash; then went "
        "out the next night and beat his own son at WrestleMania.",

        "One record needs its expiry date attached, because most retellings leave it off. His 2006 "
        "Royal Rumble run &mdash; entering at No. 2 and surviving <b>62 minutes</b> to win, "
        "dedicating it to Eddie Guerrero, who had died that November &mdash; set the record for the "
        "longest time spent in a single Rumble match. It stood for seventeen years, and then it "
        "fell: Gunther&rsquo;s 71 minutes 25 seconds in the 2023 match is the record now. What "
        "Mysterio keeps is the part no one can pass: the win itself, from the No. 2 position, as a "
        "cruiserweight, in the most sentimental Rumble ever booked &mdash; the springboard to his "
        "first World Heavyweight Championship over Kurt Angle and Randy Orton at WrestleMania 22 "
        "on April 2, 2006.",

        "The mask history is its own biography. As Rey Misterio Jr. he became AAA&rsquo;s teenage "
        "prodigy, then the engine of WCW&rsquo;s cruiserweight division from 1996 &mdash; and WCW, "
        "in one of wrestling&rsquo;s consensus mistakes, took the mask off him: he lost it in a "
        "hair-versus-mask tag match at SuperBrawl IX on February 21, 1999, against Kevin Nash and "
        "Scott Hall, and worked barefaced for three years. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">62</span>'
        '<span class="pull-cap">minutes in the 2006 Royal Rumble from the No. 2 spot &mdash; the iron-man record for seventeen years, and still the win</span></span>'
        "WWE restored it for his July 25, 2002 debut against Chavo Guerrero and has protected it "
        "since &mdash; most famously in the 2009 Chris Jericho feud, where Mysterio kept the mask "
        "and unmasked Jericho instead. The lucha inheritance became a dynasty question in the "
        "2020s: tag champion with his son Dominik in 2021, betrayed by him in 2022, and winner of "
        "the father-versus-son match at WrestleMania 39 on April 1, 2023, two nights after his "
        "Hall of Fame induction.",

        "The 2025&ndash;26 file is a run of bad luck met with unreasonable durability. A torn "
        "groin and adductor, suffered in a six-man tag on the April 18, 2025 SmackDown, scratched "
        "him from a planned WrestleMania 41 match against El Grande Americano the next night; he "
        "returned on the November 3, 2025 Raw. A knee injury on the January 26, 2026 Raw put his "
        "Royal Rumble spot in doubt; he went anyway, entered No. 4, and was eliminated by Oba Femi "
        "in under three minutes before another months-long absence WWE folded into the storyline. "
        "He came back for the WrestleMania 42 Intercontinental ladder match on April 19, 2026 "
        "&mdash; Penta retained &mdash; and on August 17, 2026, a week after champion Chad Gable "
        "offered him the shot, took Gable to a reversed roll-up out of duelling ankle locks on "
        "Raw. Gable&rsquo;s Instagram message afterward &mdash; &ldquo;Rey Mysterio is truly a "
        "human being like no other I&rsquo;ve ever met. All class&rdquo; &mdash; is the current "
        "state of the account: no championship, no retirement announced, and the whole roster "
        "treating a match with him as an honor. He turns 52 in December.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("3&times;", "World champion"),
            ("2006", "Royal Rumble winner"),
            ("21st", "WWE Grand Slam"),
            ("2023", "Hall of Fame, active"),
            ("5&times;", "Tag champion in WWE"),
            ("51", "Age, still active"),
        ],
        lead=("Fifteen documented WWE bouts &mdash; the debut, the Rumble, all three world title "
              "changes, the mask-versus-title answer to Jericho, the Dominik matches and the full "
              "2026 arc. This is a curated ledger, not a career count: the AAA, ECW and WCW years "
              "are summarised in the career section rather than rowed here, and no win&ndash;loss "
              "total is published because none is verified. The two July 25, 2011 rows are the "
              "same night &mdash; he won and lost the WWE Championship inside one Raw. Filter by "
              "match type, tap any column header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the reputation rests on. No Observer star ratings are published "
                    "here &mdash; none were verified against archives in this pass, and his case "
                    "was always the highlight reel, not the scorecard."),
    signature=[
        dict(rating="—", event="Royal Rumble 2006 — Miami", opponent="The Rumble field",
             stip="62 minutes from No. 2, the win, and the Eddie Guerrero dedication"),
        dict(rating="—", event="The Bash 2009 — Sacramento", opponent="Chris Jericho",
             stip="Title vs. mask — the unmasking counter, mid-springboard"),
        dict(rating="—", event="WrestleMania 22 — Chicago", opponent="Kurt Angle & Randy Orton",
             stip="The first world title, in the triple threat"),
        dict(rating="—", event="WrestleMania 39 Night 1", opponent="Dominik Mysterio",
             stip="Father versus son, two nights after his Hall of Fame induction"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("3&times;", "World title reigns"),
            ("21st", "Grand Slam Champion"),
            ("3&times;", "US Championship"),
            ("5 or 6", "WCW Cruiserweight — see note"),
        ],
        lead=("Championships across WWE and WCW, a Grand Slam, and one count this page refuses to "
              "settle: sources give his WCW Cruiserweight total as five or six, and the conflict is "
              "flagged rather than silently resolved."),
        rows=[
            dict(ic="H", name="World Heavyweight Championship", count="2",
                 sub="WrestleMania 22 triple threat over Kurt Angle and Randy Orton, April 2, 2006; "
                     "the Fatal 4-Way win of June 20, 2010"),
            dict(ic="W", name="WWE Championship", count="1",
                 sub="Won the vacant title in the tournament final over The Miz on the July 25, "
                     "2011 Raw &mdash; and lost it to John Cena the same night"),
            dict(ic="I", name="WWE Intercontinental Championship", count="2",
                 sub="From JBL in 21 seconds at WrestleMania 25, April 5, 2009; regained from Chris "
                     "Jericho in the title-vs-mask match at The Bash, June 28, 2009"),
            dict(ic="U", name="WWE United States Championship", count="3",
                 sub="From Samoa Joe at Money in the Bank, May 19, 2019; from AJ Styles in "
                     "November 2019; from Austin Theory on the August 11, 2023 SmackDown &mdash; "
                     "that last at age 48"),
            dict(ic="T", name="WWE Tag Team Championship", count="4",
                 sub="Four partners, all headline names: Edge (November 2002), Rob Van Dam "
                     "(December 2004), Eddie Guerrero (February 2005), Batista (December 2005)"),
            dict(ic="D", name="WWE SmackDown Tag Team Championship", count="1",
                 sub="With Dominik at WrestleMania Backlash, May 16, 2021 &mdash; WWE&rsquo;s first "
                     "father-and-son tag team champions"),
            dict(ic="C", name="WWE Cruiserweight Championship", count="3",
                 sub="Three reigns, 2003&ndash;04, as the division&rsquo;s standard-bearer"),
            dict(ic="X", name="WCW Cruiserweight Championship", count="5*",
                 sub="The asterisk is the point: most ledgers say five reigns, at least one says "
                     "six, and the conflict is published here rather than resolved. Three WCW World "
                     "Tag Team reigns sit alongside it, with partners including Billy Kidman and "
                     "Konnan"),
            dict(ic="G", name="Grand Slam &amp; Royal Rumble", count="&mdash;",
                 sub="WWE&rsquo;s 21st Grand Slam Champion; 2006 Royal Rumble winner from the No. 2 "
                     "position; Hall of Fame Class of 2023, inducted while active"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Two units that carried lucha libre into American main events, and the family act "
             "that turned into the best story of his late career.",
        cards=[
            dict(era="WCW 1998&ndash;99 &middot; WWE 2022&ndash;",
                 name="Latino World Order",
                 members="Eddie Guerrero (founder), Rey Mysterio; revived by Mysterio with Santos "
                         "Escobar, Cruz Del Toro, Joaquin Wilde, Zelina Vega",
                 desc="Eddie Guerrero's WCW faction, revived by Mysterio in WWE in 2022 as a "
                      "tribute with a working roster. The LWO gave the 2023-24 SmackDown midcard "
                      "its identity and made Mysterio the standing patron of WWE's lucha "
                      "generation — the same role the storyline keeps writing for him against "
                      "Penta, Dragon Lee and the rest."),
            dict(era="WCW &middot; 1999&ndash;2000",
                 name="Filthy Animals",
                 members="Rey Misterio Jr., Konnan, Billy Kidman, Eddie Guerrero",
                 desc="The unmasked years' crew — WCW's young, swaggering counter-culture unit, "
                      "and the context for his tag title runs with Kidman and Konnan."),
            dict(era="WWE &middot; 2002&ndash;2005",
                 name="The SmackDown Six era",
                 members="Rey Mysterio & Edge, vs. Angle & Benoit, Los Guerreros",
                 desc="Not a faction but the ensemble that rebuilt WWE tag wrestling: three teams, "
                      "one tournament, and Mysterio & Edge's November 2002 title win. The 2005 "
                      "series with Eddie Guerrero — friendship to feud, custody ladder match "
                      "included — grew directly out of it."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One character, five contexts &mdash; the mask is the persona, and losing it once is "
             "the hinge of the whole biography: <b>Colibri</b> &rarr; <b>Rey Misterio Jr.</b> "
             "&rarr; the unmasked WCW years &rarr; <b>Rey Mysterio, WWE</b> &rarr; the patriarch.",
        cards=[
            dict(mono="CO", era="Mexico &middot; 1989&ndash;1992", name="Colibri",
                 desc="The teenage prodigy — debuting at 14 under names including La Lagartija "
                      "Verde and Colibri, trained by his uncle Rey Misterio, before AAA made him "
                      "Rey Misterio Jr. in 1992."),
            dict(mono="JR", era="AAA, ECW, WCW &middot; 1992&ndash;1999", name="Rey Misterio Jr.",
                 desc="The high-flyer who translated lucha libre for American audiences — the 1995 "
                      "ECW run with Psicosis, then WCW from 1996, where the cruiserweight division "
                      "was effectively built on his matches with Guerrera, Malenko and Ultimo "
                      "Dragon."),
            dict(mono="UM", era="WCW &middot; 1999&ndash;2002", name="The unmasked years",
                 desc="Lost the mask in the hair-vs-mask tag at SuperBrawl IX, February 21, 1999, "
                      "to Kevin Nash and Scott Hall — a decision WCW itself came to regret and "
                      "lucha tradition never forgave. Three barefaced years followed."),
            dict(mono="RM", era="WWE &middot; 2002&ndash;present", name="Rey Mysterio",
                 desc="Mask restored, spelling anglicised, and the 619 installed as one of the "
                      "most over finishers in company history. The underdog formula never "
                      "changed; WWE finally put a world title on it in 2006."),
            dict(mono="PA", era="WWE &middot; 2018&ndash;present", name="The patriarch",
                 desc="The final form: LWO elder, Hall of Famer while active, father in "
                      "wrestling's best family feud, and the veteran whose opponents thank him "
                      "afterward — as Chad Gable did, publicly, in August 2026."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Tijuana at fourteen to a Raw title match at fifty-one.",
        rows=[
            dict(year="1989", title="Debut at 14",
                 desc="April 30, 1989, trained by his uncle Rey Misterio; AAA signs the teenager "
                      "by 1992."),
            dict(year="1996", title="The cruiserweight revolution",
                 desc="Arrives in WCW after an ECW run and turns the Cruiserweight Championship "
                      "into appointment television — five (or six; sources conflict) reigns."),
            dict(year="1999", title="The mask comes off",
                 desc="Loses the hair-vs-mask tag at SuperBrawl IX on February 21 to Nash and "
                      "Hall; wrestles unmasked until 2002."),
            dict(year="2002", title="WWE, mask restored",
                 desc="Debuts July 25, 2002 on SmackDown, beating Chavo Guerrero; the SmackDown "
                      "Six era and the Edge tag title win follow within months."),
            dict(year="2006", title="The Eddie year",
                 desc="Wins the Royal Rumble from No. 2 on January 29, 62 minutes, dedicated to "
                      "Eddie Guerrero; beats Angle and Orton at WrestleMania 22 on April 2 for the "
                      "World Heavyweight Championship."),
            dict(year="2009", title="Keeps the mask, takes the title",
                 desc="The Jericho feud: loses the IC title at Extreme Rules, wins the "
                      "title-vs-mask rematch at The Bash on June 28 by unmasking Jericho "
                      "mid-move."),
            dict(year="2011", title="WWE Champion for a night",
                 desc="Wins the vacant WWE Championship over The Miz on the July 25 Raw and loses "
                      "it to John Cena the same evening."),
            dict(year="2015", title="Departure",
                 desc="Leaves WWE in February 2015 for Lucha Underground, AAA and the "
                      "independents — the sabbatical that extended the career."),
            dict(year="2018", title="Return",
                 desc="Back in WWE, with Dominik increasingly part of the act; a third US title "
                      "run follows in 2019."),
            dict(year="2021", title="Father-and-son champions",
                 desc="First father-son tag team champions in WWE history, with Dominik, at "
                      "WrestleMania Backlash on May 16 — and wrestling's best betrayal storyline "
                      "when Dominik turns in 2022."),
            dict(year="2023", title="Hall of Fame Friday, WrestleMania Saturday",
                 desc="Inducted March 31 as an active wrestler; beats Dominik at WrestleMania 39 "
                      "the next night; wins a third US title from Austin Theory in August at 48."),
            dict(year="2025", title="The torn groin",
                 desc="Injured in a six-man on the April 18 SmackDown, scratched from the planned "
                      "WrestleMania 41 match with El Grande Americano; returns November 3 on Raw."),
            dict(year="2026", title="Still in the title picture at 51",
                 desc="Hurts a knee January 26, wrestles the Rumble anyway (out at 2:43 to Oba "
                      "Femi), misses months, returns for the WrestleMania 42 IC ladder match on "
                      "April 19, and pushes champion Chad Gable to a reversed roll-up on the "
                      "August 17 Raw."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Eddie Guerrero",
                 desc="Best friend, tag partner, and the opponent of his most personal feud — the "
                      "2005 series that escalated to a ladder match with custody papers hanging "
                      "above the ring. Guerrero's death in November 2005 reframed everything "
                      "after: the 2006 Rumble win, the world title, and years of tributes "
                      "including the LWO revival all carry the dedication."),
            dict(name="Dominik Mysterio",
                 desc="The son he tagged with to make WWE history in 2021 turned on him in 2022 "
                      "and became the company's most gleefully booed heel by calling him a "
                      "deadbeat. Rey won the father-versus-son match at WrestleMania 39 on April "
                      "1, 2023 — with Bad Bunny at ringside — in what both men's peers regard as "
                      "the best-built family feud of the era."),
            dict(name="Chris Jericho",
                 desc="The 2009 IC series built entirely on the mask: Jericho took the title at "
                      "Extreme Rules, kept clawing at the hood, and lost the title-versus-mask "
                      "stakes match at The Bash when Mysterio unmasked him in mid-air. Nobody has "
                      "used the mask's meaning better in an American ring."),
            dict(name="Kurt Angle",
                 desc="From the SmackDown Six tag wars of 2002 — Mysterio & Edge against Angle & "
                      "Benoit — to the WrestleMania 22 triple threat where Mysterio took Angle's "
                      "World Heavyweight Championship without Angle being pinned. The size gap "
                      "was the story; the chemistry was the point."),
            dict(name="Chad Gable",
                 desc="The 2026 program, and proof the underdog formula still runs: Gable, fresh "
                      "off winning the IC title in his hometown at SummerSlam, offered Mysterio a "
                      "shot and survived it by a reversed roll-up on the August 17 Raw — then "
                      "posted that Mysterio was 'a human being like no other.' The El Grande "
                      "Americano lucha-mockery saga that Gable originated in 2025 gives the "
                      "respect its edge."),
            dict(name="Psicosis and the cruiserweight class of '96",
                 desc="Psicosis, Juventud Guerrera, Ultimo Dragon, Dean Malenko — the ECW and WCW "
                      "opponents with whom he imported an entire style. The 1996-97 Cruiserweight "
                      "division is the reason every US promotion now has a high-flying division "
                      "at all."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Legacy",
        lead="The crossover items, kept to what was verified.",
        rows=[
            dict(when="2022", title="WWE 2K22 cover star", kind="Game",
                 desc="Cover athlete for the series' 20th-anniversary-of-Rey edition, with a "
                      "dedicated 2K Showcase mode retracing his career."),
            dict(when="2009", title="Rey Mysterio: Behind the Mask", kind="Book",
                 desc="The autobiography, covering Tijuana, WCW and the WWE ascent."),
            dict(when="2023", title="WWE Hall of Fame, Class of 2023", kind="Honor",
                 desc="Headlined the class while a full-time active wrestler — and won at "
                      "WrestleMania the following night."),
            dict(when="1989&ndash;", title="The mask itself", kind="Icon",
                 desc="The most merchandised object in WWE's modern history by any casual count "
                      "of an arena crowd — thousands of replica masks a night, for two decades."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, with expiry dates attached where they belong.",
        stats=[
            ("3", "World titles"),
            ("62:12", "2006 Rumble iron man"),
            ("14", "Age at debut"),
        ],
        rows=[
            dict(name="Royal Rumble 2006 — the win from No. 2",
                 sub="62 minutes in the match, the longest single-Rumble survival time until "
                     "Gunther's 71:25 in 2023 — a caveat most retellings drop. The win, dedicated "
                     "to Eddie Guerrero, still stands as the lowest-number victory of the modern "
                     "era alongside the No. 1 winners."),
            dict(name="Three world championships as a 5'6\" cruiserweight",
                 sub="World Heavyweight at WrestleMania 22 (April 2, 2006) and Fatal 4-Way (June "
                     "20, 2010); the WWE Championship on July 25, 2011, held for hours — the "
                     "point was never the length."),
            dict(name="WWE's first father-and-son tag team champions",
                 sub="With Dominik, at WrestleMania Backlash, May 16, 2021."),
            dict(name="Hall of Fame induction as an active wrestler",
                 sub="Class of 2023, inducted March 31, 2023 — then beat Dominik at WrestleMania "
                     "39 the next night, and has wrestled title matches in every year since, "
                     "including against Chad Gable on August 17, 2026 at age 51."),
            dict(name="WWE's 21st Grand Slam Champion",
                 sub="World, Intercontinental, United States and tag championships — completed "
                     "across the longest arc of any Grand Slam winner."),
            dict(name="The title-vs-mask defense, The Bash 2009",
                 sub="Put the mask against Jericho's Intercontinental title on June 28, 2009, and "
                     "won both ways — kept the hood, took the belt, and unmasked Jericho in the "
                     "finish."),
            dict(name="A 37-year career bridging five booms",
                 sub="AAA's early-90s golden age, ECW, WCW's cruiserweight revolution, WWE's "
                     "Ruthless Aggression and modern eras — no other active WWE wrestler predates "
                     "the Monday Night War."),
            dict(name="The 2026 durability file",
                 sub="Knee injury January 26; Rumble anyway on January 31; months out; a "
                     "WrestleMania 42 ladder match April 19 including a West Coast Pop on Rusev "
                     "through a ladder; and a 13-minute IC challenge on August 17 that the "
                     "champion publicly called an honor."),
        ],
        footnote=("Deliberately unresolved: the WCW Cruiserweight reign count (five in most "
                  "ledgers, six in at least one opened for this page) — flagged in the titles "
                  "section rather than silently picked. Deliberately absent: career win-loss "
                  "totals, social handles, and Observer ratings, none verified in this pass."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Rey_Mysterio"),
        dict(k="Wrestling Inc", v="The August 17, 2026 Intercontinental title match",
             href="https://www.wrestlinginc.com/2238831/wwe-raw-chad-gable-rey-mysterio-first-wwe-mens-intercontinental-title-defense/"),
        dict(k="Wrestlezone", v="Chad Gable&rsquo;s post-match message",
             href="https://www.wrestlezone.com/news/1658262-chad-gable-message-rey-mysterio-wwe-raw-title-match"),
        dict(k="Yahoo Sports", v="Return from injury and the WrestleMania 42 ladder match",
             href="https://sports.yahoo.com/articles/rey-mysterio-wwe-wrestlemania-match-115912958.html"),
        dict(k="Yahoo Sports", v="The Royal Rumble 2026 injury account",
             href="https://sports.yahoo.com/articles/wwe-claims-top-star-injured-154856198.html"),
        dict(k="Fightful", v="WrestleMania 42 &mdash; Penta retains the ladder match",
             href="https://www.fightful.com/wrestling/penta-wins-ladder-match-to-retain-wwe-intercontinental-title-at-wrestlemania-42/"),
        dict(k="Sportskeeda", v="Championship ledger",
             href="https://www.sportskeeda.com/wwe/rey-mysterio-championship-wins"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Rey Mysterio still wrestling in 2026?",
            a="Yes &mdash; a full-time active WWE wrestler on Raw at 51. In 2026 alone he has "
              "wrestled the Royal Rumble on January 31 (entering No. 4 on an injured knee), the "
              "WrestleMania 42 Intercontinental Championship ladder match on April 19, and a "
              "13-minute Intercontinental title match against Chad Gable on the August 17 Raw, "
              "which he lost to a reversed roll-up. No retirement has been announced. He turns 52 "
              "in December 2026.",
            q_ld="Is Rey Mysterio still an active wrestler in 2026?",
            a_ld="Yes. Rey Mysterio is an active WWE wrestler on Raw at age 51 as of August 2026. "
                 "In 2026 he has wrestled in the Royal Rumble on January 31, the Intercontinental "
                 "Championship ladder match at WrestleMania 42 on April 19, and an "
                 "Intercontinental Championship match against Chad Gable on the August 17 episode "
                 "of Raw, which Gable won. No retirement has been announced."),
        dict(
            q="How many world titles has Rey Mysterio won?",
            a="Three: the World Heavyweight Championship twice &mdash; the WrestleMania 22 triple "
              "threat over Kurt Angle and Randy Orton on April 2, 2006, and the Fatal 4-Way match "
              "of June 20, 2010 &mdash; and the WWE Championship once, won in a tournament final "
              "over The Miz on July 25, 2011 and lost to John Cena the same night. He is also "
              "WWE&rsquo;s 21st Grand Slam Champion, with Intercontinental, United States and tag "
              "titles filling out the set.",
            q_ld="How many world championships has Rey Mysterio won?",
            a_ld="Three. Rey Mysterio won the World Heavyweight Championship at WrestleMania 22 on "
                 "April 2, 2006 and again at Fatal 4-Way on June 20, 2010, and the WWE "
                 "Championship on July 25, 2011, which he lost to John Cena later the same night. "
                 "He is also WWE's 21st Grand Slam Champion."),
        dict(
            q="What happened between Rey Mysterio and Chad Gable?",
            a="Gable beat Penta for the Intercontinental Championship at SummerSlam in his "
              "hometown Minneapolis on August 2, 2026, then offered Mysterio a title shot &mdash; "
              "partly a respect angle, partly the long tail of the <b>El Grande Americano</b> "
              "story, the masked lucha-mocking character Gable originated in 2025 (a planned "
              "Mysterio match at WrestleMania 41 died with Rey&rsquo;s torn groin; Ludwig Kaiser "
              "later took over the mask). On the August 17 Raw, Gable won his first defense with "
              "a reversed roll-up out of duelling ankle locks, then posted that Mysterio is "
              "&ldquo;truly a human being like no other I&rsquo;ve ever met. All class.&rdquo;",
            q_ld="What happened between Rey Mysterio and Chad Gable in 2026?",
            a_ld="Chad Gable won the Intercontinental Championship from Penta at SummerSlam on "
                 "August 2, 2026, then offered Rey Mysterio a title match. On the August 17, 2026 "
                 "episode of Raw, Gable retained in his first defense, winning a 13-minute match "
                 "with a reversed roll-up while both men traded ankle lock attempts. Gable "
                 "afterward praised Mysterio publicly as 'a human being like no other.' The feud "
                 "traces loosely to the El Grande Americano storyline Gable originated in 2025, "
                 "when an injury cancelled a planned Mysterio match at WrestleMania 41."),
        dict(
            q="Why did Rey Mysterio wrestle without a mask in WCW but wear one in WWE?",
            a="WCW booked the mask off him: he lost a hair-versus-mask tag match at SuperBrawl IX "
              "on February 21, 1999, against Kevin Nash and Scott Hall, and wrestled barefaced for "
              "three years &mdash; a decision widely regarded, including inside WCW, as a waste of "
              "one of wrestling&rsquo;s most valuable images. When WWE signed him it restored the "
              "mask for his July 25, 2002 debut and has protected it since; in the lucha "
              "tradition a lost mask is lost forever, so the restoration remains a standing "
              "American exception to a Mexican rule.",
            q_ld="Why did Rey Mysterio lose his mask in WCW but wear it again in WWE?",
            a_ld="Rey Mysterio lost his mask in WCW in a hair-versus-mask tag match at SuperBrawl "
                 "IX on February 21, 1999, against Kevin Nash and Scott Hall, and wrestled "
                 "unmasked until 2002. When he signed with WWE, the company restored the mask for "
                 "his debut on July 25, 2002 and has protected it since, despite the lucha libre "
                 "tradition that a mask lost in a wager match is lost permanently."),
        dict(
            q="Does Rey Mysterio still hold the Royal Rumble longest-time record?",
            a="No &mdash; and the win matters more than the record did. His 62 minutes from the "
              "No. 2 spot in the 2006 Rumble was the longest single-match survival time for "
              "seventeen years, until Gunther&rsquo;s 71:25 in 2023. What no one has taken is the "
              "context: he won that Rumble, as a cruiserweight, months after Eddie Guerrero&rsquo;s "
              "death, and turned it into the World Heavyweight Championship at WrestleMania 22.",
            q_ld="Does Rey Mysterio still hold the Royal Rumble record for longest time in the match?",
            a_ld="No. Rey Mysterio's 62 minutes in the 2006 Royal Rumble, entering at No. 2 and "
                 "winning, was the record for the longest survival time in a single Royal Rumble "
                 "for seventeen years, until Gunther set the current record of 71 minutes 25 "
                 "seconds in 2023. Mysterio's 2006 victory itself still stands as one of the "
                 "lowest-entry-number wins in the match's history."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Oscar Gutierrez Rubio"),
        dict(label="Born", value="December 11, 1974",
             sub="Chula Vista, California &middot; age 51"),
        dict(label="Billed from", value="San Diego, California",
             sub="the 619 is San Diego&rsquo;s area code"),
        dict(label="Height", value="5&#8242;6&#8243;", sub="168 cm"),
        dict(label="Weight", value="175 lb", sub="79 kg (billed)"),
        dict(label="Debut", value="April 30, 1989", sub="at 14 years old"),
        dict(label="Trained by", value="Rey Misterio (his uncle)",
             sub="whose name he carried as Rey Misterio Jr."),
        dict(label="Ring names", value="Colibri &rarr; Rey Misterio Jr. &rarr; Rey Mysterio",
             sub="mask lost at WCW SuperBrawl IX, February 21, 1999; restored by WWE in 2002"),
        dict(label="Signature", value="619 &middot; West Coast Pop &middot; springboard everything",
             sub="the frog splash used as an Eddie Guerrero tribute"),
        dict(label="Family", value="Son Dominik Mysterio; daughter Aalyah",
             sub="first father-son tag champions in WWE history, 2021"),
        dict(label="Brand", value="Raw", sub="active roster, no championship as of August 31, 2026"),
        dict(label="Hall of Fame", value="2023", sub="inducted while a full-time active wrestler"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1974-12-11",
    bornplace="Chula Vista, California",
    nationality="United States",
    height_cm=168,
    weight_kg=79,
    ld=dict(
        alternateName=["Oscar Gutierrez Rubio", "Rey Misterio Jr.", "Colibri",
                       "The Master of the 619", "The Biggest Little Man"],
        award=["World Heavyweight Championship (2 reigns)",
               "WWE Championship (1 reign)",
               "WWE Intercontinental Championship (2 reigns)",
               "WWE United States Championship (3 reigns)",
               "WWE Tag Team Championship (4 reigns)",
               "WWE SmackDown Tag Team Championship (1 reign, with Dominik Mysterio)",
               "WWE Cruiserweight Championship (3 reigns)",
               "WCW Cruiserweight Championship (5 reigns by most counts)",
               "WCW World Tag Team Championship (3 reigns)",
               "Royal Rumble winner (2006)",
               "WWE Grand Slam Champion (21st)",
               "WWE Hall of Fame (2023)"],
        knowsAbout=["Professional wrestling", "Lucha libre", "WWE", "WCW", "AAA",
                    "Cruiserweight wrestling"],
        description="Rey Mysterio, born Oscar Gutierrez Rubio in Chula Vista, California, is an "
                    "American professional wrestler and the most successful luchador in WWE "
                    "history. He debuted in 1989 at age 14, drove WCW's cruiserweight division, "
                    "and in WWE won three world championships, the 2006 Royal Rumble from the No. "
                    "2 position, and titles completing the Grand Slam. With his son Dominik he "
                    "formed WWE's first father-and-son tag team champions in 2021, and he was "
                    "inducted into the WWE Hall of Fame in 2023 while still active. At 51 he "
                    "remains on the Raw roster, most recently challenging Chad Gable for the "
                    "Intercontinental Championship on August 17, 2026.",
        sameAs=["https://en.wikipedia.org/wiki/Rey_Mysterio",
                "https://www.wwe.com/"],
    ),
)
