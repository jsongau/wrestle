# -*- coding: utf-8 -*-
"""Becky Lynch - dossier data.

Sources: /tmp/research/becky-lynch.md (web-verified, compiled Aug 23 2026) and the
match / signature / tape data harvested from the previous /wrestlers/becky-lynch/ page.
Nothing here is invented. Where the two disagree, or where the research file records a
live conflict between publishers, the conflict is printed on the page rather than
silently resolved. Career win-loss totals are NOT published: the old page carried a
"79-35" headline that the harvester flags as inconsistent with its own sparkline and
with its own seven-row match table, and the research file verifies no career count.
"""

# ----------------------------------------------------------------- record rows
# All seven bouts are carried from the existing page. No match has been added.
# Escaped fields (event / opponent / stip / title) use literal punctuation, because
# the generator HTML-escapes them; entities are used only in raw-HTML fields.
ROWS = [
    dict(result="W", date="2018-10-28", promo="WWE", landmark=True,
         event="Evolution", opponent="Charlotte Flair",
         stip="Last Woman Standing — WWE's own 2018 Match of the Year",
         title="SmackDown Women's Championship"),
    dict(result="W", date="2019-02-17", promo="WWE",
         event="Elimination Chamber", opponent="Bayley",
         stip="Singles", title="SmackDown Women's Championship"),
    dict(result="W", date="2019-04-07", promo="WWE", type="tag", landmark=True,
         event="WrestleMania 35", opponent="Ronda Rousey & Charlotte Flair",
         stip="Winner Takes All triple threat — first women's match to main event WrestleMania; "
              "title tables date the changes April 8",
         title="Raw & SmackDown Women's Championships"),
    dict(result="W", date="2019-05-19", promo="WWE", landmark=True,
         event="Money in the Bank", opponent="Sasha Banks",
         stip="Singles — retains on the night the 41-to-42-day Two Belts run ends",
         title="Raw Women's Championship"),
    dict(result="W", date="2019-10-06", promo="WWE",
         event="Hell in a Cell", opponent="Sasha Banks",
         stip="Hell in a Cell — the previous dossier also recorded this opponent as Charlotte Flair; "
              "unresolved",
         title="Raw Women's Championship"),
    dict(result="L", date="2022-04-02", promo="WWE", landmark=True,
         event="WrestleMania 38", opponent="Bianca Belair", opponent_html=True,
         stip="Singles — ends the 162-day second reign",
         title="Raw Women's Championship"),
    dict(result="W", date="2023-09-02", promo="WWE",
         event="Payback", opponent="Trish Stratus",
         stip="Singles — Legend vs. The Man", title=""),
]

# opponent_html rows carry a real <a>, so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Bianca Belair": "bianca-belair"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="becky-lynch",
    name="Becky Lynch",
    realname="Rebecca Quin",
    epithet="The Man",
    hook="Record & Titles",

    meta_desc=("Becky Lynch, The Man, is a seven-time world champion, the inaugural SmackDown Women's "
               "Champion and the only three-time Women's Intercontinental Champion. Full record, titles, "
               "factions, records and career."),
    og_desc=("The Man: 7 world title reigns, the 2019 Royal Rumble, and both the longest and the shortest "
             "Women's Intercontinental Championship reigns. Full record, titles, factions and career."),
    tw_desc="The Man: 7 world titles, the 2019 Royal Rumble, and both ends of the Women's IC reign record.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2002",
    height_imp="5&#8242;6&#8243;",
    weight_lb="135",
    world_titles="7",
    vitals_tagline="The Man",
    support_note="Merch &middot; Books &middot; Watch",
    x_url="https://x.com/BeckyLynchWWE",
    ig_url="https://www.instagram.com/beckylynchwwe/",
    sp_items=[
        dict(ic="BL", title="Becky Lynch Merch", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Cover athlete, WWE 2K20",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="ST", title="Star Trek: Starfleet Academy", sub="Lieutenant Ya · 2026",
             tag="Watch", href="https://en.wikipedia.org/wiki/Star_Trek:_Starfleet_Academy"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/becky-lynch"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Irish Lass Kicker &middot; Becky Two Belts &middot; Big Time Becks",
    hero_tag="Limerick, Ireland &middot; <em>Independents &middot; NXT &middot; WWE &middot; "
             "2002&ndash;present</em>",
    now_label="NOW",
    now_bold="Back on Raw, no title, no match signed",
    now_tail=" &middot; returned August 3, 2026 to chase Liv Morgan&rsquo;s Women&rsquo;s World Championship",
    hstats=[
        dict(value="7",   x=True,  label="World Titles"),
        dict(value="398", x=False, label="Day Title Reign"),
        dict(value="163", x=False, label="Day Record IC Reign"),
        dict(value="3",   x=True,  label="Women's IC Reigns"),
    ],
    ghost_link="From Rebecca Knox to The Man",
    vlabel="Est. 2002 &middot; Limerick, Ireland",
    mono="BL",

    # ---------------------------------------------------------------- 01 overview
    # index into overview of the correction paragraph -> the framed
    # "Setting one thing straight" callout (aside.corr) on the page
    correction=1,
    overview=[
        "<b>Becky Lynch</b> is the clearest modern case of a wrestler rewriting her own ceiling in public. "
        "In the summer of 2018 she was a mid-card babyface WWE kept losing with; by April 2019 she closed "
        "WrestleMania holding two world championships, and by the end of that year she had led WWE "
        "merchandise sales and become the first woman ever named <i>Pro Wrestling Illustrated</i>&rsquo;s "
        "Most Popular Wrestler of the Year. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">7</span>'
        '<span class="pull-cap">world title reigns across two lineages &mdash; alongside the 2019 Royal Rumble and the inaugural SmackDown Women&rsquo;s Championship</span></span>'
        "The concrete record underneath the story: seven world title "
        "reigns across two lineages, the inaugural SmackDown Women&rsquo;s Championship, the 2019 Royal "
        "Rumble, an NXT Women&rsquo;s Championship, two Women&rsquo;s Tag Team Championship reigns, and "
        "both the longest and the shortest reigns in the history of the Women&rsquo;s Intercontinental "
        "Championship &mdash; 163 days and 43 days, held by the same person.",

        "The line that travels with her name fails three ways, and the accurate version is still enormous. "
        "First, the WrestleMania 35 main event was a <b>triple threat</b> &mdash; Lynch, Ronda Rousey and "
        "Charlotte Flair &mdash; so the milestone Wikipedia actually states is about the <i>match</i>: the "
        "first women&rsquo;s match to main event WrestleMania. Flair and Rousey are &ldquo;the first woman "
        "to main event WrestleMania&rdquo; exactly as much as Lynch is. Second, it was <b>not</b> the first "
        "women&rsquo;s match to main event a WWE pay-per-view at all: Sasha Banks vs. Charlotte Flair closed "
        "Hell in a Cell on <b>October 30, 2016</b> at TD Garden, two and a half years earlier. The "
        "WrestleMania 35 first is specific to WrestleMania. Third, &ldquo;Becky Two Belts&rdquo; is "
        "remembered as an era and lasted <b>41&ndash;42 days</b>: she dropped the SmackDown Women&rsquo;s "
        "Championship back to Flair at Money in the Bank on <b>May 19, 2019</b>, about six weeks later. What "
        "is uniquely hers from that night is narrower and better: she is the <b>first person to win both "
        "world titles in a single match</b>, and she handed Ronda Rousey her <b>first pinfall loss</b>, "
        "countering the Piper&rsquo;s Pit into a crucifix pin.",

        "She was born Rebecca Quin on January 30, 1987 in Limerick and debuted on November 11, 2002 at "
        "fifteen, trained by Fergal Devitt &mdash; later Finn B&aacute;lor &mdash; and Paul Tracey, with "
        "further training at NWA UK Hammerlock. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig pull-fig--sm">AGE&nbsp;15</span>'
        '<span class="pull-cap">her age at her November 11, 2002 debut, trained by Fergal Devitt &mdash; later Finn B&aacute;lor</span></span>'
        "As <b>Rebecca Knox</b> she worked the European and North "
        "American independents, winning the inaugural ECCW SuperGirls Championship in 2005 and the World "
        "Queens of Chaos Championship, and briefly worked as Komeera. A head injury took roughly six years "
        "out of her career; she was an Aer Lingus flight attendant, took a degree from Dublin Institute of "
        "Technology and studied at the Gaiety School of Acting before signing with WWE in April 2013. She "
        "came up through NXT as one of the four the press christened the Four Horsewomen, won the inaugural "
        "SmackDown Women&rsquo;s Championship on September 11, 2016, and then spent two years as the "
        "sympathetic underdog &mdash; until Flair was inserted into her SummerSlam 2018 title match, Lynch "
        "attacked her, the crowd sided with the attacker, and WWE let the reaction dictate the character.",

        "The years since have been a series of reinventions. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">162</span>'
        '<span class="pull-cap">days as Raw Women&rsquo;s Champion after the SummerSlam 2021 return &mdash; won in roughly 26 seconds</span></span>'
        "She returned at SummerSlam 2021 as &ldquo;Big "
        "Time Becks,&rdquo; beat Bianca Belair in roughly 26 seconds and took the Raw Women&rsquo;s "
        "Championship that October for 162 days; she won the Women&rsquo;s Tag Team Championship with Lita "
        "in 2023 and the NXT Women&rsquo;s Championship from Tiffany Stratton that September; she won the "
        "2024 Elimination Chamber and the vacant Women&rsquo;s World Championship on April 22, 2024 for 33 "
        "days, and published a memoir that took the Wrestling Observer&rsquo;s Best Pro Wrestling Book "
        "award. In 2025 she returned at WrestleMania 41 to win tag gold with Lyra Valkyria, turned on her a "
        "day later, and built the Women&rsquo;s Intercontinental Championship into her belt across three "
        "reigns. She lost it to Sol Ruca at Clash in Italy on May 31, 2026, went off television for the "
        "summer &mdash; her exact final match of that run is not verified by any source in this file &mdash; "
        "and came back on the August 3, 2026 Raw to confront Women&rsquo;s World Champion Liv Morgan "
        "alongside Stephanie Vaquer. No match has been signed.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Highlight set",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("7&times;",  "World titles"),
            ("5&times;",  "SmackDown / Women's World"),
            ("2&times;",  "Raw / WWE Women's"),
            ("3&times;",  "Women's Intercontinental"),
            ("398",       "Longest reign (days)"),
            ("2019",      "Royal Rumble winner"),
        ],
        lead=("Seven bouts &mdash; a highlight subset, not a career count. These are the rows carried over "
              "from the previous Becky Lynch dossier; the research file compiled for this rebuild verifies "
              "title changes, dates and reign lengths but not a full match ledger, so no career "
              "win&ndash;loss total is published here rather than guessed. Two live conflicts are printed "
              "in the rows themselves: WrestleMania 35 is dated April 7, 2019 by Wikipedia&rsquo;s event "
              "article and April 8 by the title-change tables, and the October 6, 2019 Hell in a Cell "
              "opponent was recorded two different ways on the old page. Filter by match type, tap any "
              "column header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The three bouts the previous dossier singled out, with its ratings as published. One "
                    "caution carried forward: that page described the Hell in a Cell bout as the first "
                    "women&rsquo;s Hell in a Cell match, which is wrong &mdash; that was Sasha Banks vs. "
                    "Charlotte Flair on October 30, 2016 &mdash; and it named two different opponents for "
                    "the 2019 match."),
    signature=[
        dict(rating="5.0", event="WrestleMania 35", opponent="Ronda Rousey & Charlotte Flair",
             stip="Winner Takes All triple threat — both world titles"),
        dict(rating="4.5", event="Hell in a Cell 2019", opponent="Sasha Banks",
             stip="Hell in a Cell — Raw Women's Championship"),
        dict(rating="4.0", event="Evolution 2018", opponent="Charlotte Flair",
             stip="Last Woman Standing — SmackDown Women's Championship"),
    ],
    signature_count_word="three",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("7&times;",     "World title reigns"),
            ("163",          "Longest IC reign (days)"),
            ("6th",          "Women's Grand Slam"),
            ("6th / 8th",    "Triple Crown — disputed"),
        ],
        lead=("Seven world title reigns across two lineages that were each renamed mid-stream, which is "
              "where almost every miscount of her career comes from. Reign lengths are given as the "
              "published title-history tables give them; where publishers disagree, both figures appear."),
        rows=[
            dict(ic="W", name="Women's World Championship / SmackDown Women's Championship", count="5",
                 sub="Created August 23, 2016 as the SmackDown Women&rsquo;s Championship, renamed the "
                     "Women&rsquo;s World Championship on June 12, 2023 &middot; 2016, <b>inaugural "
                     "champion</b> at Backlash, 84 days &middot; 2018, def. Charlotte Flair at Hell in a "
                     "Cell, 91 days &middot; 2019, WrestleMania 35, <b>41 days</b> (SmackDown Hotel) or "
                     "<b>42</b> (Khel Now) &middot; 2021, def. Bianca Belair at SummerSlam, 62 days "
                     "&middot; 2024, won the vacant title in a battle royal, 33 days"),
            dict(ic="R", name="WWE Women's Championship / Raw Women's Championship", count="2",
                 sub="Established April 3, 2016 at WrestleMania 32, renamed Raw Women&rsquo;s Championship "
                     "in September 2016, reverted June 9, 2023 &middot; 2019&ndash;20, <b>398 days</b> "
                     "(SmackDown Hotel) or <b>399</b> (Khel Now), relinquished on May 10, 2020 rather than "
                     "lost &mdash; Khel Now&rsquo;s claim that it ended at WrestleMania 36 is wrong "
                     "&middot; 2021&ndash;22, 162 days, ended by Bianca Belair &middot; <b>Flagged:</b> "
                     "Wikipedia&rsquo;s article on this title gives her combined total as &ldquo;535 days "
                     "(559 per WWE)&rdquo;, but the per-reign figures sum to 560 and 535 reconciles with "
                     "nothing found &mdash; not adopted here"),
            dict(ic="I", name="WWE Women's Intercontinental Championship", count="3",
                 sub="Most reigns of anyone &middot; 2025, won at Money in the Bank on June 7, <b>163 days "
                     "&mdash; the longest in the title&rsquo;s history</b>, ended November 17, 2025 by "
                     "<b>Maxxine Dupri</b> (SmackDown Hotel&rsquo;s table and a Sports Illustrated "
                     "headline; two automated reads of Wikipedia returned two different, both wrong, "
                     "champions for that date) &middot; 2026, won on the January 5 Raw, 54 days &middot; "
                     "2026, won at WrestleMania 42 on April 18, <b>43 days &mdash; the shortest in the "
                     "title&rsquo;s history</b>, lost to Sol Ruca at Clash in Italy"),
            dict(ic="T", name="WWE Women's Tag Team Championship", count="2",
                 sub="2023, with Lita, won on the February 27 Raw &mdash; <b>42 days</b> (SmackDown Hotel) "
                     "or <b>41</b> (Khel Now) &middot; 2025, with Lyra Valkyria, won at WrestleMania 41 on "
                     "April 20 &mdash; <b>1 day</b>, the shortest reign in the title&rsquo;s history, "
                     "logged by WWE as less than a day; Lynch turned on Valkyria as it ended"),
            dict(ic="N", name="NXT Women's Championship", count="1",
                 sub="2023 &middot; def. Tiffany Stratton on the September 12 NXT in Orlando &middot; 42 "
                     "days &middot; lost to Lyra Valkyria on October 24, 2023"),
            dict(ic="E", name="NWA ECCW SuperGirls Championship", count="1",
                 sub="2005 &middot; inaugural champion, as Rebecca Knox &middot; reign dates not verified"),
            dict(ic="Q", name="World Queens of Chaos Championship", count="1",
                 sub="Independent-era reign, as Rebecca Knox &middot; date not verified"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Two booked stables, one press label that was never a stable at all, and one membership the "
             "sources do not agree on.",
        cards=[
            dict(era="NXT &middot; 2013&ndash;15 &middot; press framing, not a booked unit",
                 name="The Four Horsewomen",
                 members="Becky Lynch, Charlotte Flair, Sasha Banks, Bayley",
                 desc="The legitimate framing, with one important caveat: this was never an on-screen "
                      "alliance. The four were never booked as a unit. The name was applied by media and "
                      "fans — WWE used it editorially, in its own NXT roundtable feature — and it "
                      "deliberately echoes Ric Flair's Four Horsemen as a nod to Charlotte's lineage. "
                      "Wikipedia does not list it among Lynch's factions at all. What it describes is real: "
                      "four women who came up through NXT together between 2013 and 2015 and moved to the "
                      "main roster in 2015, after which the women's division was rebuilt around them."),
            dict(era="NXT &middot; 2014&ndash;15",
                 name="Team B.A.E.",
                 members="Sasha Banks, Becky Lynch",
                 desc="\"Best At Everything\" — Lynch as Sasha Banks' NXT lackey. The pairing that "
                      "established her early alignment and carried into her main-roster arrival."),
            dict(era="WWE &middot; 2015",
                 name="Team PCB",
                 members="Paige, Charlotte Flair, Becky Lynch",
                 desc="Formed during the 2015 \"Divas Revolution\" three-way faction war against Team "
                      "B.A.D. and Team Bella; the name was a retitle after an earlier one was dropped. The "
                      "feud won the Wrestling Observer Newsletter's Worst Feud of the Year award for 2015, "
                      "which is the honest verdict on it."),
            dict(era="WWE &middot; 2025&ndash;26 &middot; membership disputed",
                 name="The Vision",
                 members="Seth Rollins, Paul Heyman, Bron Breakker, Bronson Reed, Logan Paul, Austin Theory "
                         "— and, disputed, Becky Lynch",
                 desc="Include with the flag attached. Multiple outlets reported Lynch aligning with "
                      "Rollins' Heyman-managed faction after helping him retain the World Heavyweight "
                      "Championship at Clash in Paris in late August 2025, and Pro Wrestling Fandom lists "
                      "her as a member. Wikipedia's article on The Vision does not list her in its member "
                      "table. That is an open conflict between publishers, not a settled fact, and it is "
                      "published here as one."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Four characters that matter, out of a run that started in 2002 &mdash; and one accidental "
             "turn that produced the biggest act in the division.",
        cards=[
            dict(mono="RK", era="Independents &middot; 2002&ndash;13", name="Rebecca Knox",
                 desc="The independent-circuit run across Europe and North America, begun at fifteen. "
                      "Finishers of the era were Hard Knox, a leg-hook sitout suplex slam, and the "
                      "Bexploder. She won the inaugural ECCW SuperGirls Championship in 2005 and briefly "
                      "worked under the name Komeera in 2004, before a head injury took roughly six years "
                      "out of her career."),
            dict(mono="LK", era="WWE &middot; 2016&ndash;18", name="The Irish Lass Kicker",
                 desc="The steampunk-goggles main-roster babyface and inaugural SmackDown Women's "
                      "Champion. Sympathetic underdog framing — the version of the character WWE kept "
                      "losing with, and the reason the 2018 turn landed as hard as it did. The Dis-arm-her "
                      "had replaced the Four-Leg Clover as her finish on July 1, 2014."),
            dict(mono="TM", era="WWE &middot; 2018&ndash;20, 2021/22&ndash;present", name="The Man",
                 desc="Charlotte Flair was inserted into her SummerSlam 2018 title match; Lynch attacked "
                      "her afterwards, the crowd cheered the attacker, and WWE rewrote the character "
                      "around the reaction. The Man-handle Slam was added as a second finisher on January "
                      "1, 2019. Wikipedia dates the nickname 2018–2020 and 2021–present; SmackDown Hotel "
                      "dates the second stint from 2022 — a minor conflict, unresolved."),
            dict(mono="BT", era="WWE &middot; 2021&ndash;22", name="Big Time Becks",
                 desc="The heel reinvention on returning at SummerSlam 2021: Hollywood-styled, arrogant, "
                      "wealth-flaunting, and introduced by beating Bianca Belair in roughly 26 seconds. It "
                      "ran to WrestleMania 38, where Belair took the Raw Women's Championship back and "
                      "closed the loop."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Limerick to the main event, with six years missing in the middle.",
        rows=[
            dict(year="2002", title="Debuts at fifteen",
                 desc="Debuts November 11, 2002 as Rebecca Knox, trained by Fergal Devitt — later Finn "
                      "Bálor — and Paul Tracey, with further training at NWA UK Hammerlock."),
            dict(year="2005", title="Inaugural independent champion",
                 desc="Wins the first ECCW SuperGirls Championship and later the World Queens of Chaos "
                      "Championship. A head injury then keeps her out of wrestling for roughly six years, "
                      "spent as an Aer Lingus flight attendant and at the Gaiety School of Acting."),
            dict(year="2013", title="Signs with WWE",
                 desc="Joins in April 2013 and debuts as Becky Lynch on August 29, 2013 in NXT, on an "
                      "Irish-dancing entrance and the Four-Leg Clover."),
            dict(year="2016", title="Inaugural SmackDown Women's Champion",
                 desc="Wins the new title on September 11, 2016 at Backlash and holds it 84 days."),
            dict(year="2018", title="The turn",
                 desc="Attacks Charlotte Flair after SummerSlam; the crowd sides with her and WWE rewrites "
                      "the character as The Man. Takes Wrestling Observer Women's Wrestling MVP and PWI "
                      "Woman of the Year, and WWE's own 2018 Match of the Year for Evolution."),
            dict(year="2019", title="Royal Rumble, then the WrestleMania main event",
                 desc="Wins the women's Royal Rumble, then beats Ronda Rousey and Charlotte Flair in the "
                      "WrestleMania 35 triple threat on April 7 to hold both world titles. Leads WWE "
                      "merchandise sales, tops the PWI Women's 100 and becomes the first woman named PWI "
                      "Most Popular Wrestler of the Year."),
            dict(year="2021", title="Return and heel turn",
                 desc="Returns at SummerSlam, beats Bianca Belair for the SmackDown Women's Championship, "
                      "becomes Big Time Becks and takes the Raw Women's Championship in October."),
            dict(year="2023", title="NXT champion and tag champion",
                 desc="Wins the Women's Tag Team Championship with Lita in February; takes the NXT Women's "
                      "Championship from Tiffany Stratton on September 12 and holds it 42 days."),
            dict(year="2024", title="Seventh world title, and a book award",
                 desc="Wins the Elimination Chamber, then the vacant Women's World Championship on April "
                      "22 for 33 days. Publishes Becky Lynch: The Man: Not Your Average Average Girl, "
                      "which wins the Wrestling Observer's Best Pro Wrestling Book award for 2024."),
            dict(year="2025", title="Returns, turns, and builds a new belt",
                 desc="Returns at WrestleMania 41 to win the tag titles with Lyra Valkyria, then turns on "
                      "her a day later; wins the Women's Intercontinental Championship at Money in the "
                      "Bank on June 7 and holds it a record 163 days."),
            dict(year="2026", title="A third IC reign, then a summer away",
                 desc="Regains the IC title on the January 5 Raw and again at WrestleMania 42; loses it to "
                      "Sol Ruca on May 31; goes off television for the summer, with no verified final "
                      "match; returns August 3 to challenge Liv Morgan."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who she went to war with.",
        cards=[
            dict(name="Charlotte Flair",
                 desc="The spine of the whole career: friends in Team PCB, then the SummerSlam 2018 turn, "
                      "then the Last Woman Standing match at Evolution on October 28, 2018 that WWE named "
                      "its Match of the Year, then the WrestleMania 35 triple threat, then Money in the "
                      "Bank on May 19, 2019, where Flair took the SmackDown title back and ended the Two "
                      "Belts run. It mattered because the Flair rivalry is what converted crowd "
                      "frustration with Lynch's booking into the loudest reaction in the company."),
            dict(name="Ronda Rousey",
                 desc="One peak, and it is the biggest night of both careers. At WrestleMania 35 Lynch "
                      "pinned Rousey to win both world titles, handing Rousey her first pinfall loss. WWE "
                      "had built 2018 around Rousey as the crossover star and the audience picked Lynch "
                      "instead — CBS Sports named Lynch's attack on Rousey its 2018 Best Moment of the "
                      "Year. The much-repeated complaint that Rousey's shoulders were not down is a "
                      "kayfabe talking point WWE's own commentary seeded that night; no source verifies it "
                      "and no title change was ever reviewed."),
            dict(name="Asuka",
                 desc="The counterweight to the Flair feud: Asuka took the SmackDown Women's Championship "
                      "from Lynch in the three-way TLC match on December 16, 2018 that CBS Sports named "
                      "its 2018 WWE Match of the Year, and the two ran it back through 2019 to 2022. Asuka "
                      "is the opponent Lynch consistently could not put away cleanly."),
            dict(name="Bianca Belair", slug="bianca-belair",
                 desc="The bookends of the Big Time Becks run. Lynch returned at SummerSlam on August 21, "
                      "2021 and beat Belair in roughly 26 seconds for the SmackDown Women's Championship, "
                      "a finish designed to make the returning heel intolerable; Belair took the Raw "
                      "Women's Championship back at WrestleMania 38 on April 2, 2022, ending Lynch's "
                      "162-day reign."),
            dict(name="Lyra Valkyria",
                 desc="Valkyria beat Lynch for the NXT Women's Championship in October 2023, then "
                      "partnered with her to win the Women's Tag Team Championship at WrestleMania 41 in "
                      "April 2025 — a reign that lasted one day before Lynch turned on her. The feud that "
                      "followed produced Lynch's record 163-day Women's Intercontinental Championship "
                      "reign, including a No DQ match at SummerSlam 2025. It is the program that made that "
                      "title matter."),
            dict(name="Liv Morgan",
                 desc="Morgan took the Women's World Championship from Lynch on May 25, 2024 at King and "
                      "Queen of the Ring, ending the 33-day reign. It restarted on August 3, 2026, when "
                      "Lynch returned to confront Morgan over infrequent defenses — calling her a "
                      "\"glorified valet\" — with Stephanie Vaquer laying claim to the same title shot. On "
                      "the August 17 Raw, Lynch threw Morgan into the barricade. This is her live "
                      "storyline."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Beyond the ring.",
        rows=[
            dict(when="2024", title="Becky Lynch: The Man: Not Your Average Average Girl", kind="Book",
                 desc="Her memoir, published by Gallery Books in 2024. It won the Wrestling Observer "
                      "Newsletter's Best Pro Wrestling Book award for 2024. A New York Times bestseller "
                      "claim also circulates; it came back from only one automated read in the research "
                      "for this file and is single-sourced, so it is reported here as unconfirmed rather "
                      "than stated."),
            dict(when="2026", title="Star Trek: Starfleet Academy", kind="TV",
                 desc="Plays Lieutenant Ya across two episodes — her most substantial scripted television "
                      "role to date."),
            dict(when="2018&ndash;2025", title="The Marine 6, Rumble, Happy Gilmore 2", kind="Film",
                 desc="Maddy Hayes in The Marine 6: Close Quarters (2018), her film debut; the voice of "
                      "Axehammer in Rumble (2021); Flex in Happy Gilmore 2 (2025). She also worked as a "
                      "stunt double on one episode of Vikings in 2013."),
            dict(when="2020&ndash;2023", title="Billions, Young Rock, Weakest Link", kind="TV",
                 desc="Scripted and unscripted appearances across a decade: Billions (2020), Cyndi Lauper "
                      "in two episodes of Young Rock (2022–23), WWE Rivals (2022), Biography: WWE Legends "
                      "(2023), and a run of game-show and talk-show spots including Weakest Link, "
                      "Celebrity Family Feud, The Kelly Clarkson Show and Celebrity Jeopardy! in 2023."),
            dict(when="2016&ndash;", title="WWE 2K and crossovers", kind="Game",
                 desc="Playable from WWE 2K17 through WWE 2K26, and the cover athlete for WWE 2K20. "
                      "Crossover appearances in Brawlhalla (2019), The King of Fighters All Star (2019), "
                      "Rainbow Six Siege (2023) and Fortnite (2023). She has also hosted on WWE's "
                      "UpUpDownDown web series since 2018 as \"Soulless Senpai.\""),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records that are actually hers, stated the way the sources state them &mdash; with the "
             "numbers publishers disagree on printed as disagreements.",
        stats=[
            ("163",        "Day IC reign — the longest"),
            ("43",         "Day IC reign — the shortest"),
            ("41&ndash;42", "Days as Becky Two Belts"),
        ],
        rows=[
            dict(name="First person to win both world titles in a single match",
                 sub="WrestleMania 35, the Winner Takes All triple threat for the Raw and SmackDown "
                     "Women's Championships. This one is hers alone, and it is the strongest claim from "
                     "that night."),
            dict(name="Handed Ronda Rousey her first pinfall loss",
                 sub="Same match, countering the Piper's Pit into a crucifix pin. Also hers alone."),
            dict(name="Part of the first women's match to main event WrestleMania — shared three ways",
                 sub="Wikipedia's phrasings are \"the first-ever women's main event match in WrestleMania "
                     "history\" and \"the first-ever women's match to main event WrestleMania\" — both "
                     "describe the match, not a person. It was a triple threat, so Charlotte Flair and "
                     "Ronda Rousey hold the milestone equally. And it was not the first women's match to "
                     "main event a WWE PPV: Sasha Banks vs. Charlotte Flair closed Hell in a Cell on "
                     "October 30, 2016."),
            dict(name="Becky Two Belts lasted 41 to 42 days",
                 sub="WrestleMania 35 to Money in the Bank on May 19, 2019, when Charlotte Flair regained "
                     "the SmackDown Women's Championship. SmackDown Hotel dates the reign April 8 to May "
                     "19 and counts 41 days; Khel Now counts 42. About six weeks either way. She kept the "
                     "Raw title for roughly another year."),
            dict(name="Both the longest and the shortest Women's Intercontinental Championship reigns",
                 sub="163 days from June 7 to November 17, 2025, and 43 days from April 18 to May 31, "
                     "2026. She also holds the most reigns with the title, at three — WWE.com lists it as "
                     "\"3; most-ever.\""),
            dict(name="Shortest Women's Tag Team Championship reign",
                 sub="One day with Lyra Valkyria from WrestleMania 41 on April 20, 2025, logged by WWE as "
                     "less than a day. Lynch turned on Valkyria as it ended."),
            dict(name="398 days in the Raw / WWE Women's Championship lineage, 2019–20",
                 sub="SmackDown Hotel says 398; Khel Now says 399 and adds that she lost at WrestleMania "
                     "36, which is wrong — she defended successfully there and relinquished the title on "
                     "May 10, 2020. The one-day gap traces to WrestleMania 35 being dated April 7 by "
                     "Wikipedia's event article and April 8 by the title-change tables."),
            dict(name="Seven world championships, and a Triple Crown ordinal nobody agrees on",
                 sub="Five reigns in the SmackDown / Women's World lineage and two in the Raw / WWE "
                     "Women's lineage. Wikipedia and Pro Wrestling Fandom both call her the sixth Women's "
                     "Grand Slam Champion; on the Triple Crown, Wikipedia says sixth and Pro Wrestling "
                     "Fandom says eighth. Unresolved, so both are published."),
            dict(name="2019 Royal Rumble winner and 2024 Elimination Chamber winner",
                 sub="The 2019 Rumble win is what set up the WrestleMania 35 main event; the 2024 Chamber "
                     "win preceded her seventh world title."),
            dict(name="First woman named PWI Most Popular Wrestler of the Year",
                 sub="2019, alongside topping the PWI Women's 100 that year and leading WWE merchandise "
                     "sales. PWI Woman of the Year in 2018 and 2019; Wrestling Observer Women's Wrestling "
                     "MVP in 2018 and 2019; Sports Illustrated Women's Wrestler of the Year in 2018 and "
                     "2019, and 20th on its Greatest WWE Wrestlers of All Time list. Her 2025 and 2026 PWI "
                     "placings are not verified."),
            dict(name="WrestleMania 35 drew somewhere between 63,000 and 82,265",
                 sub="WWE announced 82,265 at MetLife Stadium; the Wrestling Observer reported 63,000 paid "
                     "and estimated 68,000 to 70,000 including comps at a legitimate sellout. The same gap "
                     "between announced and counted recurs elsewhere in this era: at Royal Rumble 2023, "
                     "WWE announced 51,338 while Wrestlenomics reported 42,928 scanned. Announced gates "
                     "are marketing figures, not turnstile counts."),
        ],
        footnote=("Cagematch was excluded from the research for this page, so no career win-loss total, "
                  "match count or aggregate rating appears anywhere on it. Two source problems are worth "
                  "keeping in view: Wikipedia was actively unreliable on the Women's Intercontinental "
                  "Championship, returning two different and both incorrect champions across two reads of "
                  "the November 17, 2025 title change (it was Maxxine Dupri), and its WWE Women's "
                  "Championship article's combined figure of \"535 days (559 per WWE)\" reconciles with no "
                  "per-reign numbers found — the reigns sum to 560. Both are printed on this page as "
                  "conflicts rather than adopted."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Instagram", v="@beckylynchwwe", href="https://www.instagram.com/beckylynchwwe/"),
        dict(k="X / Twitter", v="@BeckyLynchWWE", href="https://x.com/BeckyLynchWWE"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/becky-lynch"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Becky_Lynch"),
        dict(k="WrestleMania 35", v="The main event, as written",
             href="https://en.wikipedia.org/wiki/WrestleMania_35"),
        dict(k="Hell in a Cell 2016", v="The actual first women's PPV main event",
             href="https://en.wikipedia.org/wiki/Hell_in_a_Cell_(2016)"),
        dict(k="SmackDown Hotel", v="Women's Intercontinental title history",
             href="https://www.thesmackdownhotel.com/title-history/wwe/wwe-womens-intercontinental-championship"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/becky-lynch.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Was Becky Lynch the first woman to main event WrestleMania?",
            a="Not on her own, and the wider version of the claim is simply wrong. The WrestleMania 35 main "
              "event on April 7, 2019 was a <b>triple threat</b> &mdash; Lynch, Ronda Rousey and Charlotte "
              "Flair &mdash; so the milestone Wikipedia records is about the match: <i>the first-ever "
              "women&rsquo;s match to main event WrestleMania</i>. Flair and Rousey share it equally. It "
              "was also <b>not</b> the first women&rsquo;s match to main event a WWE pay-per-view: Sasha "
              "Banks vs. Charlotte Flair closed Hell in a Cell on <b>October 30, 2016</b> at TD Garden, two "
              "and a half years earlier. What is uniquely Lynch&rsquo;s from that night: she is the first "
              "person to win both world titles in a single match, and she gave Ronda Rousey her first "
              "pinfall loss.",
            q_ld="Was Becky Lynch the first woman to main event WrestleMania?",
            a_ld="Not alone. The WrestleMania 35 main event on April 7, 2019 was a triple threat between "
                 "Becky Lynch, Ronda Rousey and Charlotte Flair, so the accurate milestone is that it was "
                 "the first women's match to main event WrestleMania, shared equally by all three. It was "
                 "also not the first women's match to main event a WWE pay-per-view: Sasha Banks versus "
                 "Charlotte Flair closed Hell in a Cell on October 30, 2016. What is uniquely Becky "
                 "Lynch's is that she became the first person to win both world titles in a single match "
                 "and handed Ronda Rousey her first pinfall loss."),
        dict(
            q="How long was Becky Lynch &ldquo;Becky Two Belts&rdquo;?",
            a="About six weeks &mdash; <b>41 or 42 days</b>, depending on the source, not the year it is "
              "usually remembered as. She won both titles at WrestleMania 35 and dropped the SmackDown "
              "Women&rsquo;s Championship back to Charlotte Flair at Money in the Bank on <b>May 19, "
              "2019</b>. SmackDown Hotel dates the reign April 8 to May 19 and counts 41 days; Khel Now "
              "counts 42. The single-day gap comes from WrestleMania 35 being dated April 7 by "
              "Wikipedia&rsquo;s event article and April 8 by the title-change tables. She kept the Raw "
              "Women&rsquo;s Championship for roughly another year.",
            q_ld="How long was Becky Lynch a double champion as Becky Two Belts?",
            a_ld="About six weeks: 41 or 42 days, not a year. Becky Lynch won both the Raw and SmackDown "
                 "Women's Championships at WrestleMania 35 and lost the SmackDown Women's Championship "
                 "back to Charlotte Flair at Money in the Bank on May 19, 2019. SmackDown Hotel dates the "
                 "reign April 8 to May 19 and counts 41 days, while Khel Now counts 42; the one-day gap "
                 "comes from WrestleMania 35 being dated April 7 by Wikipedia's event article and April 8 "
                 "by the title-change tables. Becky Lynch kept the Raw Women's Championship for roughly "
                 "another year."),
        dict(
            q="How many world championships has Becky Lynch won?",
            a="Seven: five in the SmackDown Women&rsquo;s / Women&rsquo;s World Championship lineage, "
              "including the inaugural reign in 2016, and two in the Raw Women&rsquo;s / WWE Women&rsquo;s "
              "Championship lineage. Both lineages were renamed mid-stream, which is where nearly every "
              "miscount comes from &mdash; sources that treat the renamed belts as four separate titles "
              "inflate or deflate the number. She is also a three-time Women&rsquo;s Intercontinental "
              "Champion, a one-time NXT Women&rsquo;s Champion and a two-time Women&rsquo;s Tag Team "
              "Champion.",
            q_ld="How many world championships has Becky Lynch won?",
            a_ld="Becky Lynch has seven world title reigns: five in the SmackDown Women's Championship and "
                 "Women's World Championship lineage, including the inaugural reign in 2016, and two in "
                 "the Raw Women's Championship and WWE Women's Championship lineage. Both lineages were "
                 "renamed mid-stream, which is the source of most miscounts. Becky Lynch is also a "
                 "three-time WWE Women's Intercontinental Champion, a one-time NXT Women's Champion and a "
                 "two-time WWE Women's Tag Team Champion."),
        dict(
            q="Is Becky Lynch a champion right now, and where is she?",
            a="No. She lost the WWE Women&rsquo;s Intercontinental Championship to Sol Ruca at Clash in "
              "Italy on <b>May 31, 2026</b>, ending her third reign at 43 days; that title has since "
              "passed to Raquel Rodriguez. Lynch is on <b>Raw</b>. She was off television through the "
              "summer of 2026 &mdash; her exact final match of that run is not verified &mdash; and "
              "returned on the <b>August 3, 2026</b> Raw to confront Women&rsquo;s World Champion Liv "
              "Morgan alongside Stephanie Vaquer. No match has been signed.",
            q_ld="Is Becky Lynch a champion right now?",
            a_ld="No. Becky Lynch lost the WWE Women's Intercontinental Championship to Sol Ruca at Clash "
                 "in Italy on May 31, 2026, ending her third reign at 43 days, and that title has since "
                 "passed to Raquel Rodriguez. Becky Lynch is on Raw. She was off WWE television through "
                 "the summer of 2026 and returned on the August 3, 2026 episode of Raw to confront "
                 "Women's World Champion Liv Morgan alongside Stephanie Vaquer. No match has been "
                 "announced."),
        dict(
            q="Was the Four Horsewomen a real stable?",
            a="No &mdash; and this is worth separating carefully, because the framing itself is "
              "legitimate. Lynch, Charlotte Flair, Sasha Banks and Bayley were never booked as an "
              "on-screen unit. The name is a media and fan label for the four women who came up through "
              "NXT together between 2013 and 2015, playing off Ric Flair&rsquo;s Four Horsemen as a nod to "
              "Charlotte&rsquo;s lineage; WWE used it editorially in its own NXT roundtable feature, and "
              "Wikipedia does not list it among Lynch&rsquo;s factions at all. Her actual booked groups "
              "were Team B.A.E. and Team PCB &mdash; plus The Vision, which is disputed.",
            q_ld="Was the Four Horsewomen a real WWE stable?",
            a_ld="No. Becky Lynch, Charlotte Flair, Sasha Banks and Bayley were never booked as an "
                 "on-screen faction. The Four Horsewomen is a media and fan label for the four women who "
                 "came up through NXT together between 2013 and 2015, echoing Ric Flair's Four Horsemen "
                 "as a nod to Charlotte Flair's lineage. WWE used the name editorially in its own NXT "
                 "roundtable feature, and Wikipedia does not list it among Becky Lynch's factions. Her "
                 "actual booked groups were Team B.A.E. and Team PCB, plus The Vision, whose membership "
                 "is disputed."),
        dict(
            q="Is Becky Lynch a member of The Vision?",
            a="Reported, but not settled. Multiple news outlets reported her aligning with Seth "
              "Rollins&rsquo; Paul Heyman-managed faction after she helped him retain the World "
              "Heavyweight Championship at Clash in Paris in late August 2025, and Pro Wrestling Fandom "
              "lists her as a member. <b>Wikipedia&rsquo;s article on The Vision does not list her in its "
              "member table.</b> That is a live disagreement between publishers rather than a fact this "
              "page can confirm, so it is published with the flag attached rather than asserted.",
            q_ld="Is Becky Lynch a member of The Vision?",
            a_ld="It is reported but not settled. Multiple news outlets reported Becky Lynch aligning "
                 "with Seth Rollins' Paul Heyman-managed faction The Vision after she helped Rollins "
                 "retain the World Heavyweight Championship at Clash in Paris in late August 2025, and "
                 "Pro Wrestling Fandom lists her as a member. However, Wikipedia's article on The Vision "
                 "does not list Becky Lynch in its member table, so the membership is presented here as a "
                 "documented conflict rather than a confirmed fact."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Rebecca Quin", sub="Wikipedia and SmackDown Hotel agree"),
        dict(label="Born", value="January 30, 1987", sub="Limerick, Republic of Ireland"),
        dict(label="Billed from", value="Dublin, Ireland",
             sub="per WWE.com &mdash; her birthplace is Limerick"),
        dict(label="Height", value="5&#8242;6&#8243;", sub="168 cm"),
        dict(label="Weight", value="135 lb", sub="61 kg &middot; WWE.com lists no weight"),
        dict(label="Debut", value="November 11, 2002", sub="at fifteen, as Rebecca Knox"),
        dict(label="WWE debut", value="August 29, 2013", sub="NXT, after signing in April 2013"),
        dict(label="Trained by", value="Fergal Devitt &middot; Paul Tracey",
             sub="NWA UK Hammerlock"),
        dict(label="Finishers", value="Dis-arm-her &middot; Man-handle Slam",
             sub="from July 1, 2014 and January 1, 2019 &middot; Wikipedia spells it Manhandle Slam"),
        dict(label="Earlier finishers", value="Hard Knox &middot; Bexploder &middot; Four-Leg Clover"),
        dict(label="Brand", value="Raw"),
        dict(label="Also known as",
             value="The Man &middot; The Irish Lass Kicker &middot; Becky Two Belts &middot; Big Time "
                   "Becks &middot; Rebecca Knox"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1987-01-30",
    bornplace="Limerick, Republic of Ireland",
    nationality="Ireland",
    alumni="Dublin Institute of Technology",
    height_cm=168,
    weight_kg=61,
    ld=dict(
        alternateName=["Rebecca Quin", "The Man", "The Irish Lass Kicker", "Becky Two Belts",
                       "Big Time Becks", "Rebecca Knox", "Komeera"],
        award=["SmackDown Women's Championship / Women's World Championship (5 reigns, inaugural champion)",
               "Raw Women's Championship / WWE Women's Championship (2 reigns)",
               "WWE Women's Intercontinental Championship (3 reigns, the most of anyone, including both "
               "the longest reign at 163 days and the shortest at 43 days)",
               "NXT Women's Championship (1 reign)",
               "WWE Women's Tag Team Championship (2 reigns, with Lita and with Lyra Valkyria)",
               "NWA ECCW SuperGirls Championship (1 reign, inaugural champion)",
               "World Queens of Chaos Championship (1 reign)",
               "Royal Rumble winner (2019)",
               "Elimination Chamber winner (2024)",
               "WWE Women's Grand Slam Champion (sixth)",
               "WWE Women's Triple Crown Champion (sixth per Wikipedia, eighth per Pro Wrestling Fandom)",
               "Pro Wrestling Illustrated Most Popular Wrestler of the Year (2019, the first woman)",
               "Pro Wrestling Illustrated Woman of the Year (2018, 2019)",
               "Pro Wrestling Illustrated Women's 100 number one (2019)",
               "Wrestling Observer Newsletter Women's Wrestling MVP (2018, 2019)",
               "Wrestling Observer Newsletter Best Pro Wrestling Book (2024)",
               "WWE Female Superstar of the Year (2018, 2019)",
               "Sports Illustrated Women's Wrestler of the Year (2018, 2019)"],
        knowsAbout=["Professional wrestling", "WWE", "Women's professional wrestling",
                    "Championship wrestling", "Submission grappling", "Irish professional wrestling"],
        description="Becky Lynch is an Irish professional wrestler signed to WWE, known as The Man. A "
                    "seven-time world champion, she was the inaugural SmackDown Women's Champion in 2016, "
                    "won the 2019 Royal Rumble, and competed in the first women's match to main event "
                    "WrestleMania — a triple threat at WrestleMania 35 shared with Charlotte Flair and "
                    "Ronda Rousey — where she became the first person to win both world titles in a single "
                    "match and handed Ronda Rousey her first pinfall loss. She holds both the longest and "
                    "the shortest reigns in the history of the WWE Women's Intercontinental Championship, "
                    "at 163 and 43 days, and the most reigns with it. Born Rebecca Quin in Limerick, she "
                    "debuted in 2002 as Rebecca Knox and signed with WWE in 2013.",
        sameAs=["https://x.com/BeckyLynchWWE",
                "https://www.instagram.com/beckylynchwwe/",
                "https://en.wikipedia.org/wiki/Becky_Lynch",
                "https://www.wwe.com/superstars/becky-lynch"],
    ),
)
