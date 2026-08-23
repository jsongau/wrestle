# -*- coding: utf-8 -*-
"""Bianca Belair - dossier data.

Sources: /tmp/research/bianca-belair.md (web-verified, compiled Aug 23 2026) and the
harvested match/signature/tape data from the previous /wrestlers/bianca-belair/ page.

Three things deliberately NOT published here, because the research file could not
support them:
  * No trainer. No source names an individual trainer, so the "Trained by" tape row
    is replaced by a "Developed at" row that says so out loud.
  * No career win-loss total. The old page's "74-28" headline is flagged by the
    harvester as inconsistent with its own sparkline (69 marks / 10 losses), and the
    same page's title list credits her with an NXT Women's Championship reign she
    never had. Only the dated bouts are carried over.
  * No "Team B.A.D. & Blonde" era. She was never in that group - see slot5.

Two harvested rows were dropped: the undated "Asuka, Raw 2022, title vs. career"
row (no day-precision date, and no such match appears in the research), and the
"IYO SKY, Money in the Bank 2023, May 27 2023" row, which conflates two different
nights - May 27, 2023 is Night of Champions, where Asuka ended the record reign,
and the Sky cash-in was SummerSlam, August 5, 2023. Both are restored below at the
dates the research dossier gives.
"""

# ----------------------------------------------------------------- record rows
# 7 dated bouts. Five are corroborated by the research dossier; the WrestleMania 36
# row is carried over from the previous page and is flagged in the lead.
ROWS = [
    dict(result="L", date="2020-04-05", promo="WWE",
         event="WrestleMania 36", opponent="Charlotte Flair",
         stip="Singles — carried over from the previous page's ledger", title=""),
    dict(result="W", date="2021-01-31", promo="WWE", type="tag", landmark=True,
         event="Royal Rumble", opponent="The 2021 women's Royal Rumble field",
         stip="Royal Rumble match — entered No. 3, lasted more than 56 minutes, last eliminated Rhea Ripley",
         title=""),
    dict(result="W", date="2021-04-10", promo="WWE", landmark=True,
         event="WrestleMania 37 Night 1 — Raymond James Stadium", opponent="Sasha Banks",
         stip="Singles — 17:15; first WrestleMania main event between two Black wrestlers",
         title="SmackDown Women's Championship"),
    dict(result="L", date="2021-08-21", promo="WWE", landmark=True,
         event="SummerSlam", opponent="Becky Lynch", opponent_html=True,
         stip="Singles — 26 seconds; ends a 133-day reign",
         title="SmackDown Women's Championship"),
    dict(result="W", date="2022-04-02", promo="WWE", landmark=True,
         event="WrestleMania 38", opponent="Becky Lynch", opponent_html=True,
         stip="Singles — the 419/420-day reign begins", title="Raw Women's Championship"),
    dict(result="L", date="2023-05-27", promo="WWE", landmark=True,
         event="Night of Champions", opponent="Asuka",
         stip="Singles — ends the longest reign in the title's history",
         title="WWE Women's Championship"),
    dict(result="L", date="2023-08-05", promo="WWE",
         event="SummerSlam", opponent="IYO SKY",
         stip="Cash-in — she had won the title earlier the same night",
         title="WWE Women's Championship"),
]

for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Becky Lynch": "becky-lynch"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="bianca-belair",
    name="Bianca Belair",
    realname="Bianca Nicole Crawford",
    epithet="The EST of WWE",
    hook="Record & Titles",

    meta_desc=("Bianca Belair, The EST of WWE, holds the longest single reign in Raw Women's "
               "Championship history at 419 days by WWE's count and 420 by Wikipedia's. Full record, "
               "titles, track career, records and the reign-length dispute explained."),
    og_desc=("The EST of WWE: a 419/420-day record reign, the 2021 Royal Rumble from No. 3, and the "
             "first WrestleMania main event between two Black wrestlers. Full record and career."),
    tw_desc=("The EST of WWE: a 419/420-day record reign, a Royal Rumble win from No. 3, and a "
             "WrestleMania main event that made history."),

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2016",
    height_imp="5&#8242;7&#8243;",
    weight_lb="155",
    world_titles="3",
    vitals_tagline="The EST",
    support_note="Merch &middot; Games &middot; Read",
    x_url="https://x.com/BiancaBelairWWE",
    ig_url="https://www.instagram.com/biancabelairwwe/",
    sp_items=[
        dict(ic="BB", title="EST Merch", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="In the series · installments not verified",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="MS", title="MileSplit Retrospective", sub="Her hurdling career, in full",
             tag="Read",
             href="https://www.milesplit.com/articles/450910/bianca-belair-wwe-legend-all-time-great-tennessee-hurdler"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/bianca-belair"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The EST of NXT &middot; The EST of WWE &middot; Four-time Tennessee state hurdles champion",
    hero_tag="Knoxville, Tennessee &middot; <em>WWE Performance Center &middot; NXT &middot; "
             "WWE &middot; 2016&ndash;present</em>",
    now_label="NOW",
    now_bold="Inactive, not competing, no championship",
    now_tail=" &middot; fourteen months out with a finger injury from WrestleMania 41, then a "
             "WrestleMania 42 return to announce her pregnancy rather than to wrestle &mdash; no "
             "announced return date",
    hstats=[
        dict(value="419",  x=False, label="Day Record Reign"),
        dict(value="3",    x=True,  label="Women's Titles"),
        dict(value="772",  x=False, label="Days as Champion"),
        dict(value="1",    x=True,  label="Royal Rumble Win"),
    ],
    ghost_link="From four state hurdles titles to the record reign",
    vlabel="Est. 2016 &middot; Knoxville, TN",
    mono="BB",

    # ---------------------------------------------------------------- 01 overview
    # index into overview of the correction paragraph -> the framed
    # "Setting one thing straight" callout (aside.corr) on the page
    correction=1,
    overview=[
        "<b>Bianca Belair</b> is the rare main-event wrestler whose case rests almost entirely on "
        "documented numbers rather than argument. She holds the longest single continuous reign in the "
        "history of the Raw Women&rsquo;s Championship lineage &mdash; 419 days by WWE&rsquo;s count, 420 "
        "by Wikipedia&rsquo;s and WrestleIndex&rsquo;s &mdash; and she is one of only two women ever to "
        "hold that title for a continuous year or more. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">419</span>'
        '<span class="pull-cap">days as Raw Women&rsquo;s Champion &mdash; the longest single reign in the lineage&rsquo;s history (Wikipedia counts 420)</span></span>'
        "She won the 2021 Royal Rumble from the No. 3 "
        "entry position after more than 56 minutes, main-evented Night 1 of WrestleMania 37 against "
        "Sasha Banks in the first WrestleMania main event contested between two Black wrestlers, and is "
        "the ninth Women&rsquo;s Triple Crown Champion. She had never wrestled a match before she was 27.",

        "The superlative that travels with her is where the record gets misstated, and it goes wrong in "
        "three separate ways. Wrestling Inc.&rsquo;s own report on the record-break said she became "
        "&ldquo;the longest-reigning women&rsquo;s champion of the entire modern era.&rdquo; That is "
        "<b>false</b>: Asuka held the NXT Women&rsquo;s Championship from April 1, 2016 to August 24, 2017 "
        "&mdash; <b>510 days</b>, which WWE itself recognises as <b>522</b> because of NXT&rsquo;s tape "
        "delay &mdash; roughly a hundred days longer than Belair&rsquo;s, and unambiguously modern era. "
        "Second, &ldquo;longest-reigning&rdquo; is ambiguous and each reading has a different holder: "
        "Belair owns the longest <i>single continuous</i> reign, while <b>Becky Lynch</b> owns the most "
        "<i>total accumulated days</i> with that title &mdash; 535 by Wikipedia&rsquo;s count, 559 by "
        "WWE&rsquo;s &mdash; and WWE published its own article headlined on Lynch&rsquo;s record. Both "
        "records live on wwe.com under near-identical language. Third, the day count itself is disputed "
        "by exactly one day: WWE.com says 419, Wikipedia and WrestleIndex say 420, and Wikipedia states "
        "outright that its 420 is &ldquo;recognized by WWE as 419 days.&rdquo; The accurate claim is "
        "narrower and still enormous &mdash; the longest single reign in that lineage&rsquo;s history.",

        "She was born Bianca Nicole Crawford on April 9, 1989 in Knoxville, Tennessee, and came to "
        "wrestling from track and field. At Austin East High School she was a four-time Tennessee state "
        "champion in the hurdles with bests of 13.57 in the 100m and 41.97 in the 300m &mdash; marks that "
        "rank second all-time in Tennessee prep history in both events &mdash; and placed third in the "
        "100m hurdles at Nike Outdoor Nationals as a senior. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">4&times;</span>'
        '<span class="pull-cap">Tennessee state hurdles champion at Austin East &mdash; marks second all-time in state prep history</span></span>'
        "College was less linear: South Carolina, then "
        "Texas A&amp;M, then a walk-on spot at Tennessee in 2013, where she ran a wind-legal 13.38 and "
        "qualified for the NCAA East Regional. Wikipedia records All-SEC and All-American honours; "
        "MileSplit&rsquo;s account of the same career emphasises that she never matched her prep marks in "
        "college and does not mention All-American status, so that one honour is single-sourced and "
        "flagged here rather than stated flat. She signed with the WWE Performance Center on April 12, 2016.",

        "The wrestling career itself is compact and steep. NXT live-event debut June 25, 2016; in-ring "
        "debut September 29, 2016; television debut under the ring name on May 3, 2017; main-roster call-up "
        "in April 2020. Then the run: the Rumble on January 31, 2021, the SmackDown Women&rsquo;s "
        "Championship in the WrestleMania 37 main event on April 10, a 133-day reign ended by a returning "
        "Becky Lynch at SummerSlam in 26 seconds, the record Raw Women&rsquo;s Championship reign from "
        "WrestleMania 38 on April 2, 2022 to Night of Champions on May 27, 2023, a WWE Women&rsquo;s "
        "Championship reign in August 2023 that lasted under a day, and two Women&rsquo;s Tag Team "
        "Championship reigns with Jade Cargill, the second finished alongside Naomi. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">772</span>'
        '<span class="pull-cap">days as champion across five reigns and three titles, per WrestleIndex</span></span>'
        "WrestleIndex totals "
        "her at 772 days as champion across five reigns and three titles. She has not competed since "
        "WrestleMania 41 in April 2025, where she broke a finger at the joint taking a triple German "
        "suplex; she returned at WrestleMania 42 on April 18, 2026 to announce, on air and in her own "
        "words, that she is expecting, and is listed inactive with no announced return date.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full ledger",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("419&ndash;420", "Day record reign"),
            ("5&times;",      "Title reigns"),
            ("3",             "Championships"),
            ("772",           "Days as champion"),
            ("1&times;",      "Royal Rumble"),
            ("9th",           "Women's Triple Crown"),
        ],
        lead=("Seven dated bouts &mdash; the title changes, the Rumble and the WrestleMania main event. "
              "This is a highlight subset, not a complete career count. No career win&ndash;loss record is "
              "published here: the previous version of this page headlined 74&ndash;28 over a graphic that "
              "actually plotted 69 bouts and 10 losses, and no source in the research file corroborates "
              "either figure. Five rows are corroborated by the research dossier; the WrestleMania 36 row "
              "is carried over from that older ledger and is not. Filter by match type, tap any column "
              "header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("Three matches, singled out between them by the previous ledger and the research file. The "
                    "ratings are carried over as published &mdash; no named outlet could be attached to "
                    "them in the research pass, and the WrestleMania 41 five-star figure is noted by "
                    "Wikipedia without an identified issuing publication."),
    signature=[
        dict(rating="5.0", event="WrestleMania 37 Night 1", opponent="Sasha Banks",
             stip="SmackDown Women's Championship — 17:15, and the first WrestleMania main event between two Black wrestlers"),
        dict(rating="5.0", event="WrestleMania 41", opponent="Jade Cargill",
             stip="Women's World Championship triple threat — rating per Wikipedia, issuing outlet unverified"),
        dict(rating="4.5", event="WrestleMania 38", opponent="Becky Lynch",
             stip="Raw Women's Championship — the record reign begins", url="/wrestlers/becky-lynch/"),
    ],
    signature_count_word="three",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("5&times;", "Title reigns"),
            ("3",        "Championships"),
            ("772",      "Total days as champion"),
            ("9th",      "Women's Triple Crown"),
        ],
        lead=("Five reigns across three championships, 772 total days as champion per WrestleIndex. Where "
              "WWE.com and Wikipedia disagree &mdash; and on the tag titles they do &mdash; both counts are "
              "shown with the reason."),
        rows=[
            dict(ic="R", name="Raw Women's Championship / WWE Women's Championship", count="2",
                 sub="2022&ndash;23 &middot; won at WrestleMania 38 on April 2, 2022, lost to Asuka at "
                     "Night of Champions on May 27, 2023 &middot; <b>419 days (WWE.com) / 420 days "
                     "(Wikipedia, WrestleIndex)</b> &mdash; the longest single continuous reign in the "
                     "title&rsquo;s history &middot; 2023 &middot; won at SummerSlam on August 5 and lost "
                     "it the same night, under a day &middot; the lineage was renamed from Raw Women&rsquo;s "
                     "Championship to WWE Women&rsquo;s Championship in 2023, which is why Wikipedia files "
                     "both reigns under the newer name &mdash; same belt, different branding"),
            dict(ic="S", name="SmackDown Women's Championship", count="1",
                 sub="2021 &middot; def. Sasha Banks in the WrestleMania 37 Night 1 main event on April 10 "
                     "&middot; lost to a returning Becky Lynch at SummerSlam on August 21 in 26 seconds "
                     "&middot; 133 days &middot; WrestleIndex files this reign under the label "
                     "&ldquo;Women&rsquo;s World Championship,&rdquo; which is a database artifact &mdash; "
                     "Wikipedia and WWE.com both identify it correctly"),
            dict(ic="T", name="WWE Women's Tag Team Championship", count="2",
                 sub="2024 &middot; May 4 to June 15, 42 days, with Jade Cargill &middot; 2024&ndash;25 "
                     "&middot; August 31 to February 24, 177 days, begun with Cargill and finished with "
                     "Naomi after Cargill was written off television &middot; <b>source conflict:</b> "
                     "WWE.com&rsquo;s profile credits one tag reign, Wikipedia and WrestleIndex both give "
                     "two with dates &mdash; two is the better-supported figure, but the disagreement with "
                     "WWE&rsquo;s own site is real &middot; the deciding events for both changes are not "
                     "verified in the research file"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Belair has spent nearly her entire career as a singles act. There are two real group "
             "associations, one of them not a membership at all &mdash; and one widely repeated stable "
             "credit that is chronologically impossible.",
        cards=[
            dict(era="WWE &middot; 2024&ndash;25",
                 name="Belair & Jade Cargill",
                 members="Bianca Belair, Jade Cargill, later Naomi",
                 desc="Not a named stable, but the most substantial group act of her career: two Women's "
                      "Tag Team Championship reigns across 2024 and 2025, and a No. 1 placing for the pair "
                      "in PWI's Tag Team 100 for 2024. Naomi replaced Cargill as co-champion during the "
                      "second reign after Cargill was written off television; the date of that switch is "
                      "not verified. The partnership later converted into a singles feud that peaked around "
                      "WrestleMania 41."),
            dict(era="WWE &middot; association, not membership",
                 name="The Street Profits",
                 members="Montez Ford, Angelo Dawkins — Belair adjacent by marriage",
                 desc="Belair married Montez Ford in June 2018, and the connection to the Street Profits "
                      "runs through that rather than through the roster sheet. She has been asked "
                      "repeatedly in interviews about joining the group, and Bobby Lashley was asked on "
                      "record whether she could join during their alliance — the framing of that coverage "
                      "is itself the confirmation that she was never a member. She has said publicly that "
                      "she made in-ring gear for the team."),
            dict(era="Correction &middot; the group she was never in",
                 name="Team B.A.D. & Blonde",
                 members="Naomi, Sasha Banks, Tamina, Lana, Emma, Summer Rae — not Bianca Belair",
                 desc="Belair is regularly credited with a “Team B.A.D. & Blonde era.” She was "
                      "never in it. Team B.A.D. was Naomi, Sasha Banks and Tamina, active May 2015 to May "
                      "2016; “Team B.A.D. & Blonde” was a one-off expanded alliance adding Lana, "
                      "Emma and Summer Rae for a single match against Team Total Divas at WrestleMania 32 "
                      "in April 2016. Wikipedia's article on the group lists Belair in neither incarnation, "
                      "and the dates rule it out anyway: she signed with the WWE Performance Center on "
                      "April 12, 2016 and did not appear even at an NXT live event until June 25, 2016 — "
                      "after that WrestleMania match had already happened."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One character for an entire televised career &mdash; unusual for a decade in the company, "
             "and the reason this section is short rather than padded.",
        cards=[
            dict(mono="EST", era="NXT &amp; WWE &middot; 2017&ndash;present", name="The EST",
                 desc="A superlative construction: the fastest, the strongest, the quickest, the roughest "
                      "and the toughest — the -est of everything. Billed as “The EST of NXT” in "
                      "developmental and “The EST of WWE” on the main roster; the only thing that "
                      "changed was the noun. The physical signature is the braided ponytail, used as both "
                      "a visual identifier and an in-storyline weapon. No name change, no gimmick reset, no "
                      "repackaging."),
            dict(mono="TURN", era="NXT &rarr; main roster &middot; c. 2018&ndash;2020",
                 name="Heel EST to babyface EST",
                 desc="The alignment flipped and the character did not. The same boastful superlatives that "
                      "read as arrogance in NXT read as confidence once she was on the main roster from "
                      "2020. The exact turn date is not verified in any source in the research file, so no "
                      "date is asserted here."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Knoxville hurdles to the record reign, in eleven steps.",
        rows=[
            dict(year="2007", title="Leaves Austin East as one of Tennessee's best-ever prep hurdlers",
                 desc="Four-time Tennessee state champion in the hurdles, ranked second all-time in state "
                      "prep history in both the 100m and the 300m, with bests of 13.57 and 41.97. Third in "
                      "the 100m hurdles and sixth in the 400m hurdles at Nike Outdoor Nationals as a "
                      "senior. (MileSplit)"),
            dict(year="2013", title="Walks on at Tennessee and reaches the NCAA East Regional",
                 desc="After stops at South Carolina and Texas A&M, she runs a wind-legal 13.38 in the 100m "
                      "hurdles and qualifies for regionals. Two-time SEC academic honor roll. Wikipedia "
                      "adds All-SEC and All-American honours and notes a career interrupted by intercostal "
                      "chondritis; the All-American credit is single-sourced. (MileSplit, Wikipedia)"),
            dict(year="2016", title="Signs with WWE having never wrestled",
                 desc="Joins the WWE Performance Center on April 12 at 27 years old and makes her first NXT "
                      "live-event appearance on June 25; in-ring debut September 29. (Wikipedia)"),
            dict(year="2017", title="Television debut as Bianca Belair",
                 desc="First NXT television appearance under the ring name on May 3. (Wikipedia)"),
            dict(year="2020", title="Main-roster call-up",
                 desc="Moves up from NXT in April 2020. (Wikipedia)"),
            dict(year="2021", title="Wins the Royal Rumble from No. 3",
                 desc="On January 31 she enters third, lasts more than 56 minutes — reported by Cageside "
                      "Seats as a women's Rumble record at the time — and last eliminates Rhea Ripley. She "
                      "is the second Black wrestler to win a Royal Rumble, after The Rock. Her exact time "
                      "and elimination count are not specified in the verified sources."),
            dict(year="2021", title="Main-events WrestleMania 37",
                 desc="On April 10 she beats Sasha Banks in 17:15 for the SmackDown Women's Championship in "
                      "the Night 1 main event — the first WrestleMania main event contested between two "
                      "Black wrestlers, and only the second time women headlined the show. (Wikipedia)"),
            dict(year="2021", title="Loses the title in 26 seconds",
                 desc="Becky Lynch returns at SummerSlam on August 21 and beats her in 26 seconds, ending a "
                      "133-day reign. Daily DDT named it a headscratching moment of the year, and Lynch has "
                      "since spoken publicly about the finish. (Forbes, WrestleIndex)"),
            dict(year="2022", title="Begins the record reign",
                 desc="Wins the Raw Women's Championship at WrestleMania 38 on April 2 and holds it until "
                      "May 27, 2023 — 419 days by WWE's count, 420 by Wikipedia's and WrestleIndex's, "
                      "passing Becky Lynch's single-reign record along the way. (WrestleIndex, WWE.com)"),
            dict(year="2024", title="Tag team run with Jade Cargill",
                 desc="Two Women's Tag Team Championship reigns across 2024–25; PWI ranks the pair No. 1 in "
                      "its Tag Team 100 for 2024. (WrestleIndex, Wikipedia)"),
            dict(year="2025", title="Injured at WrestleMania 41",
                 desc="Breaks a finger at the joint taking a triple German suplex in a Women's World "
                      "Championship triple threat. The injury proves far worse than the four to six weeks "
                      "first expected and keeps her out roughly a year. Her last on-screen appearance "
                      "before WrestleMania 42 was as guest referee at WWE Evolution in July 2025. (SI)"),
            dict(year="2026", title="Returns at WrestleMania 42 and announces her pregnancy",
                 desc="On April 18 she appears on Night 1 — not to wrestle — and announces on air that she "
                      "is expecting, with host John Cena adjusting the announced attendance from 50,816 to "
                      "50,817. She has not competed since and has no announced return date. (WWE.com, "
                      "Forbes, Fox News, Yahoo Sports)"),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Six programmes, four of which produced a championship change.",
        cards=[
            dict(name="Sasha Banks",
                 desc="Peaked at the WrestleMania 37 Night 1 main event on April 10, 2021, a 17:15 match "
                      "Belair won for the SmackDown Women's Championship. It mattered structurally as much "
                      "as narratively: the first WrestleMania headlined by two Black wrestlers and only the "
                      "second headlined by women, after WrestleMania 35. It was also Belair's first "
                      "championship of any kind — Rumble win to Mania title win is the cleanest star-making "
                      "arc WWE has run for a woman in the modern era."),
            dict(name="Becky Lynch", slug="becky-lynch",
                 desc="Peaked twice, in opposite directions. Lynch returned from maternity absence at "
                      "SummerSlam on August 21, 2021 and took the SmackDown Women's Championship in 26 "
                      "seconds — a finish that landed badly enough to become a talking point Lynch herself "
                      "has revisited. The rivalry then ran long, and Belair beat her for the Raw Women's "
                      "Championship at WrestleMania 38 to start the record reign."),
            dict(name="Asuka",
                 desc="Peaked at Night of Champions on May 27, 2023, where Asuka ended the 419/420-day "
                      "reign. It matters as the bookend to the longest single title reign in that "
                      "championship's history — the reign is the record, and this is the match that stopped "
                      "it. Asuka is also the holder of the NXT reign that disproves the wider "
                      "“modern era” claim made on Belair's behalf."),
            dict(name="IYO SKY",
                 desc="Peaked at SummerSlam on August 5, 2023, when Belair won the WWE Women's Championship "
                      "and lost it the same night to Sky. It produced the shortest reign of her career, "
                      "under a single day, immediately after her longest. The cash-in detail is general "
                      "knowledge of the event rather than separately verified; what WrestleIndex confirms "
                      "is the same-night win and loss."),
            dict(name="Jade Cargill",
                 desc="Peaked around WrestleMania 41 in April 2025. It converted her most successful tag "
                      "partnership into a singles feud, and it produced the match in which Belair broke her "
                      "finger — the injury that cost her roughly a year and, as of August 2026, still "
                      "defines her status."),
            dict(name="Bayley",
                 desc="WWE.com's own profile names Bayley among her defining rivalries, alongside IYO SKY, "
                      "Asuka and Becky Lynch. Listed here because WWE lists it, and flagged because no peak "
                      "event or date for it could be pinned down in the research pass."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Beyond the ring.",
        rows=[
            dict(when="2024", title="Love & WWE: Bianca & Montez", kind="TV",
                 desc="Hulu reality series, premiered February 2, 2024 — eight episodes, one season, "
                      "following Belair and Montez Ford in the build to WrestleMania 39. Filming began at "
                      "the 2023 Royal Rumble and ran roughly six months. (Wikipedia)"),
            dict(when="2021&ndash;22", title="ESPY Award and Sports Illustrated", kind="Awards",
                 desc="Won an ESPY in 2021 — the specific category is not verified. Sports Illustrated "
                      "ranked her No. 3 among top wrestlers in both 2021 and 2022. (Wikipedia)"),
            dict(when="Ongoing", title="MileSplit, Andscape, Essence, Fox News", kind="Press",
                 desc="MileSplit's retrospective on her hurdling career is the single best source for her "
                      "athletic marks. Andscape covered the historical significance of the WrestleMania 37 "
                      "main event; Essence has interviewed her on her career; Fox News, Forbes and Yahoo "
                      "Sports covered the WrestleMania 42 announcement, and Fox News also covered her "
                      "public request that fans stop following her from venues after a safety incident."),
            dict(when="Series", title="WWE 2K", kind="Game",
                 desc="She appears in the WWE 2K series. Specific installments, cover appearances and "
                      "release years were not verified in this research pass and are not listed rather than "
                      "guessed. No autobiography and no standalone documentary feature is verified either — "
                      "treat both as unverified rather than as nonexistent."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated the way the sources actually state them &mdash; including the two that "
             "are usually stated wrong.",
        stats=[
            ("419&ndash;420", "Day record reign"),
            ("772",           "Total days as champion"),
            ("56+",           "Minutes in the 2021 Rumble"),
        ],
        rows=[
            dict(name="Longest single continuous reign in the Raw Women's Championship lineage",
                 sub="April 2, 2022 to May 27, 2023. 419 days per WWE.com, 420 per Wikipedia and "
                     "WrestleIndex — an ordinary inclusive/exclusive counting difference, with Wikipedia "
                     "stating outright that its figure is 'recognized by WWE as 419 days.' Both are "
                     "correct per source; neither should be published alone."),
            dict(name="NOT the longest women's reign of the modern era",
                 sub="Asuka held the NXT Women's Championship from April 1, 2016 to August 24, 2017 — 510 "
                     "days, officially recognised by WWE as 522 because of NXT's tape delay. That is "
                     "roughly a hundred days longer than Belair's and squarely inside the modern era, so "
                     "Wrestling Inc.'s 'longest-reigning women's champion of the entire modern era' framing "
                     "is false. Belair's record belongs to one title lineage, not to the company."),
            dict(name="Longest single reign, not most total days — Becky Lynch holds that one",
                 sub="Wikipedia gives Lynch 535 combined days with the title across two reigns, recognised "
                     "by WWE as 559, and WWE published an article headlined 'Becky Lynch racks up most "
                     "total days as Raw Women's Champion in history,' noting she passed Alexa Bliss during "
                     "her 397th day. Both records sit on wwe.com under near-identical wording, which is "
                     "the whole reason the claim keeps travelling wrong."),
            dict(name="One of only two women to hold the title a continuous year or more",
                 sub="Wikipedia states plainly that only Becky Lynch and Bianca Belair have held it for a "
                     "continuous reign of 365 days or more."),
            dict(name="First WrestleMania main event contested between two Black wrestlers",
                 sub="WrestleMania 37 Night 1, April 10, 2021, Raymond James Stadium, Tampa — Belair beat "
                     "Sasha Banks in 17:15 for the SmackDown Women's Championship. It was also only the "
                     "second time women headlined WrestleMania, after WrestleMania 35 in 2019."),
            dict(name="WrestleMania 37 attendance is disputed by about 30 percent",
                 sub="Wikipedia's WrestleMania 37 article reports an officially claimed attendance of "
                     "25,675 while disputed records put the actual figure at 17,946 — a gap of roughly "
                     "7,700. The event ran under reduced-capacity conditions. Both figures are published "
                     "here with attribution; neither stands alone. The 50,816 given on air for "
                     "WrestleMania 42 is likewise a WWE announced figure, not an audited one."),
            dict(name="2021 Royal Rumble winner from the No. 3 entry",
                 sub="January 31, 2021. More than 56 minutes in the match, reported by Cageside Seats as a "
                     "women's Rumble record at the time, and Rhea Ripley eliminated last. Her exact time "
                     "and total elimination count are not specified in any source verified for this file. "
                     "She is the second Black wrestler to win a Royal Rumble, after The Rock."),
            dict(name="9th Women's Triple Crown Champion",
                 sub="Per Wikipedia. WrestleIndex totals her at 772 days as champion across five reigns and "
                     "three championships."),
            dict(name="First woman to win an Elimination Chamber match twice",
                 sub="Per Wikipedia. The years are not stated in the research file and are not guessed here."),
            dict(name="Second all-time in Tennessee prep history in both hurdle events",
                 sub="13.57 in the 100m hurdles and 41.97 in the 300m, set at Austin East High School in "
                     "Knoxville, alongside four state titles. At Tennessee she ran a wind-legal 13.38 and "
                     "qualified for the NCAA East Regional in 2013. Wikipedia records All-SEC and "
                     "All-American honours; MileSplit's account of the same career stresses that she "
                     "underperformed her prep marks in college and never mentions All-American status, so "
                     "that credit is single-sourced to Wikipedia."),
            dict(name="PWI No. 1 twice, in two different lists",
                 sub="No. 1 in the PWI Women's 150 for 2021, and No. 1 with Jade Cargill in the PWI Tag "
                     "Team 100 for 2024. PWI also named her Female Wrestler of the Year for 2022."),
            dict(name="Longest-reigning Black world champion in WWE, male or female",
                 sub="Stated by Wikipedia. The comparison set behind it was not independently verified, so "
                     "this is published as single-sourced."),
        ],
        footnote=("No Wrestling Observer Newsletter award is claimed for Belair: none was found in this "
                  "research pass, which is absence of evidence rather than evidence of absence. No "
                  "television-ratings record specific to her was verified either. Her brand is listed as "
                  "SmackDown because that is her last confirmed designation — Wikipedia records the move "
                  "at the 2023 Draft and TheSmackDownHotel still lists it in 2026, but no 2024 or 2025 "
                  "draft movement could be confirmed or ruled out."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Instagram", v="@biancabelairwwe", href="https://www.instagram.com/biancabelairwwe/"),
        dict(k="X / Twitter", v="@BiancaBelairWWE", href="https://x.com/BiancaBelairWWE"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/bianca-belair"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Bianca_Belair"),
        dict(k="MileSplit", v="The hurdling career, in full",
             href="https://www.milesplit.com/articles/450910/bianca-belair-wwe-legend-all-time-great-tennessee-hurdler"),
        dict(k="WrestleIndex", v="Per-reign dates and day counts",
             href="https://wrestleindex.com/wwe/bianca-belair/"),
        dict(k="WWE.com", v="Becky Lynch's most-total-days record",
             href="https://www.wwe.com/shows/raw/article/becky-lynch-total-days-raw-womens-champion"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/bianca-belair.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Bianca Belair still with WWE, and why hasn&rsquo;t she wrestled?",
            a="Yes, she is still with WWE. She has not competed since WrestleMania 41 in April 2025, where "
              "she broke a finger at the joint taking a triple German suplex &mdash; an injury that healed "
              "far more slowly than the four-to-six weeks originally expected and kept her out roughly a "
              "year. She returned on screen at WrestleMania 42 on April 18, 2026 to announce, herself and "
              "on air, that she is expecting. She is listed as inactive with no announced return date and "
              "no next match.",
            q_ld="Is Bianca Belair still with WWE, and why hasn't she wrestled?",
            a_ld="Yes. Bianca Belair is still with WWE. She has not competed since WrestleMania 41 in April "
                 "2025, where she broke a finger at the joint taking a triple German suplex, an injury that "
                 "healed far more slowly than the four to six weeks originally expected and kept her out "
                 "roughly a year. Bianca Belair returned on screen at WrestleMania 42 on April 18, 2026 to "
                 "announce on air that she is expecting, and she is listed as inactive with no announced "
                 "return date."),
        dict(
            q="Is Bianca Belair the longest-reigning women&rsquo;s champion of the modern era?",
            a="No, and the claim fails twice. Asuka held the NXT Women&rsquo;s Championship from April 1, "
              "2016 to August 24, 2017 &mdash; <b>510 days</b>, which WWE officially recognises as "
              "<b>522</b> because of NXT&rsquo;s tape delay &mdash; roughly a hundred days longer than "
              "Belair&rsquo;s reign, and unmistakably modern era. And &ldquo;longest-reigning&rdquo; is "
              "ambiguous even within the one title: Belair owns the longest single continuous reign, while "
              "<b>Becky Lynch</b> owns the most total accumulated days at 535 (Wikipedia) or 559 (WWE). "
              "What is true is narrower &mdash; Belair holds the longest single continuous reign in the Raw "
              "Women&rsquo;s Championship lineage.",
            q_ld="Is Bianca Belair the longest-reigning women's champion of the modern era?",
            a_ld="No. Asuka held the NXT Women's Championship from April 1, 2016 to August 24, 2017, a "
                 "reign of 510 days that WWE officially recognises as 522 days because of NXT's tape delay, "
                 "which is roughly a hundred days longer than Bianca Belair's reign and squarely within the "
                 "modern era. The phrase longest-reigning is also ambiguous: Bianca Belair holds the "
                 "longest single continuous reign in the Raw Women's Championship lineage, while Becky "
                 "Lynch holds the record for most total accumulated days with that title, 535 by "
                 "Wikipedia's count and 559 by WWE's."),
        dict(
            q="How long was Bianca Belair&rsquo;s Raw Women&rsquo;s Championship reign?",
            a="419 days according to WWE.com, 420 according to Wikipedia and WrestleIndex &mdash; April 2, "
              "2022 to May 27, 2023, from WrestleMania 38 to Night of Champions, where Asuka ended it. It "
              "is the longest single continuous reign in that title&rsquo;s history. The one-day gap is an "
              "ordinary inclusive/exclusive counting difference; Wikipedia says outright that its 420 is "
              "&ldquo;recognized by WWE as 419 days.&rdquo; Note also that the title was renamed the WWE "
              "Women&rsquo;s Championship mid-lineage in 2023 &mdash; same belt, different branding.",
            q_ld="How long was Bianca Belair's Raw Women's Championship reign?",
            a_ld="Bianca Belair's reign ran from April 2, 2022 to May 27, 2023, from WrestleMania 38 until "
                 "Asuka beat her at Night of Champions. WWE.com counts it as 419 days and Wikipedia and "
                 "WrestleIndex count it as 420, an inclusive versus exclusive counting difference that "
                 "Wikipedia describes as recognized by WWE as 419 days. It is the longest single continuous "
                 "reign in that title's history. The championship was renamed the WWE Women's Championship "
                 "mid-lineage in 2023."),
        dict(
            q="Was Bianca Belair the first woman to main-event WrestleMania?",
            a="No. Becky Lynch, Ronda Rousey and Charlotte Flair headlined WrestleMania 35 in 2019. "
              "Belair&rsquo;s WrestleMania 37 Night 1 main event against Sasha Banks on April 10, 2021 was "
              "the second time women headlined the show &mdash; but it was the first WrestleMania main "
              "event contested between two Black wrestlers.",
            q_ld="Was Bianca Belair the first woman to main-event WrestleMania?",
            a_ld="No. Becky Lynch, Ronda Rousey and Charlotte Flair headlined WrestleMania 35 in 2019. "
                 "Bianca Belair's WrestleMania 37 Night 1 main event against Sasha Banks on April 10, 2021 "
                 "was the second time women headlined WrestleMania, and it was the first WrestleMania main "
                 "event contested between two Black wrestlers."),
        dict(
            q="What is Bianca Belair&rsquo;s finisher?",
            a="The K.O.D., or Kiss of Death, which she has used since her 2016 debut. Descriptions differ "
              "by source: Wikipedia calls it a torture rack into an Argentine facebuster, while "
              "TheSmackDownHotel describes it as a sitout burning hammer. Both are describing the same "
              "move &mdash; the discrepancy is in technical naming, not in what happens. Her other "
              "signature is the braided ponytail, used as a literal weapon.",
            q_ld="What is Bianca Belair's finisher?",
            a_ld="Bianca Belair's finisher is the K.O.D., short for Kiss of Death, which she has used since "
                 "her 2016 debut. Sources describe it differently: Wikipedia calls it a torture rack into "
                 "an Argentine facebuster, while TheSmackDownHotel describes it as a sitout burning hammer. "
                 "Both describe the same move, and the discrepancy is one of technical naming. Her other "
                 "signature is the braided ponytail, used as an in-storyline weapon."),
        dict(
            q="What was Bianca Belair&rsquo;s track career before wrestling?",
            a="She was a hurdler. At Austin East High School in Knoxville she won four Tennessee state "
              "titles and ranks second all-time in Tennessee prep history in both the 100m hurdles (13.57) "
              "and the 300m hurdles (41.97), and placed third in the 100m hurdles at Nike Outdoor "
              "Nationals as a senior. She then ran at South Carolina, Texas A&amp;M and Tennessee, where "
              "she walked on in 2013, ran a wind-legal 13.38 and qualified for the NCAA East Regional. "
              "Wikipedia also credits her as an All-American; MileSplit&rsquo;s account of the same career "
              "does not, so that honour is single-sourced. She had never wrestled a match before signing "
              "with WWE at 27.",
            q_ld="What was Bianca Belair's track career before wrestling?",
            a_ld="Bianca Belair was a hurdler. At Austin East High School in Knoxville, Tennessee she won "
                 "four state titles and ranks second all-time in Tennessee high school history in both the "
                 "100m hurdles at 13.57 and the 300m hurdles at 41.97, and she placed third in the 100m "
                 "hurdles at Nike Outdoor Nationals as a senior. She then ran at South Carolina, Texas A&M "
                 "and Tennessee, where she walked on in 2013, ran a wind-legal 13.38 and qualified for the "
                 "NCAA East Regional. Wikipedia also credits her with All-American status, but MileSplit's "
                 "account of the same career does not mention it, so that honour is single-sourced. Bianca "
                 "Belair had never wrestled a match before signing with WWE at 27."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Bianca Nicole Crawford", sub="n&eacute;e Blair"),
        dict(label="Born", value="April 9, 1989", sub="Knoxville, Tennessee"),
        dict(label="Billed from", value="Knoxville, Tennessee"),
        dict(label="Height", value="5&#8242;7&#8243;", sub="170 cm"),
        dict(label="Weight", value="155 lb", sub="70 kg (billed) &middot; single-sourced; WWE.com lists no weight"),
        dict(label="Developed at", value="WWE Performance Center",
             sub="signed April 12, 2016 &middot; no source names an individual trainer, so none is listed"),
        dict(label="Debut", value="June 25, 2016", sub="NXT live event &middot; in-ring debut September 29, 2016"),
        dict(label="TV debut", value="May 3, 2017", sub="NXT, as Bianca Belair"),
        dict(label="Main roster", value="April 2020"),
        dict(label="Finisher", value="K.O.D. &mdash; Kiss of Death",
             sub="torture rack into an Argentine facebuster (Wikipedia) or a sitout burning hammer (TheSmackDownHotel)"),
        dict(label="Signatures", value="Braided ponytail whip &middot; handspring moonsault &middot; power offense"),
        dict(label="Brand", value="SmackDown", sub="last confirmed designation, 2023 Draft"),
        dict(label="Also known as", value="The EST &middot; The EST of NXT &middot; The EST of WWE"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1989-04-09",
    bornplace="Knoxville, Tennessee, United States",
    nationality="United States",
    alumni="University of Tennessee",
    height_cm=170,
    weight_kg=70,
    ld=dict(
        alternateName=["Bianca Nicole Crawford", "The EST", "The EST of WWE", "The EST of NXT"],
        award=["Raw Women's Championship / WWE Women's Championship (2 reigns, including a record "
               "419-day single reign, counted as 420 days by Wikipedia and WrestleIndex)",
               "SmackDown Women's Championship (1 reign, 133 days)",
               "WWE Women's Tag Team Championship (2 reigns, with Jade Cargill and Naomi)",
               "Royal Rumble winner (2021, from the No. 3 entry position)",
               "9th WWE Women's Triple Crown Champion",
               "First woman to win an Elimination Chamber match twice",
               "Pro Wrestling Illustrated Women's 150 number one (2021)",
               "Pro Wrestling Illustrated Tag Team 100 number one with Jade Cargill (2024)",
               "Pro Wrestling Illustrated Female Wrestler of the Year (2022)",
               "ESPY Award (2021)",
               "Four-time Tennessee high school state champion in the hurdles"],
        knowsAbout=["Professional wrestling", "WWE", "Championship wrestling",
                    "Track and field", "Hurdling", "Strength and power wrestling"],
        description="Bianca Belair is an American professional wrestler signed to WWE. She holds the "
                    "longest single continuous reign in the history of the Raw Women's Championship "
                    "lineage, from April 2, 2022 to May 27, 2023, counted as 419 days by WWE.com and 420 "
                    "by Wikipedia and WrestleIndex. She won the 2021 Royal Rumble from the No. 3 entry "
                    "position, main-evented Night 1 of WrestleMania 37 against Sasha Banks in the first "
                    "WrestleMania main event contested between two Black wrestlers, and is the ninth "
                    "Women's Triple Crown Champion. A four-time Tennessee state champion hurdler who ran "
                    "at South Carolina, Texas A&M and Tennessee, she signed with the WWE Performance "
                    "Center in 2016 having never wrestled. She has been inactive since April 2025.",
        sameAs=["https://x.com/BiancaBelairWWE",
                "https://www.instagram.com/biancabelairwwe/",
                "https://en.wikipedia.org/wiki/Bianca_Belair",
                "https://www.wwe.com/superstars/bianca-belair"],
    ),
)
