# -*- coding: utf-8 -*-
"""Bayley - dossier data.

Compiled August 31, 2026. Sources are the web pages opened for this build (F4W,
Khel Now, TWNP-News, Pro Wrestling Dot Net, On3, WWE.com) plus verified career
history. Her employment status is the sharpest live question in the file and is
printed as the open question it is: written off television on July 18, 2026,
contract reports conflicting (Q4 2026 vs. January 2027), an Observer suggestion
she may have quietly re-signed, and no confirmation from either side.

Deliberate omissions:
  * No career win-loss total — none verified.
  * Her 2026 Royal Rumble participation could not be confirmed either way, so the
    Rumble is absent from the 2026 rows rather than guessed at.
  * The identity of her WrestleMania 41 backstage attacker was never resolved on
    television in any source consulted; nothing is asserted about it.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2015-08-22", promo="WWE", landmark=True,
         event="NXT TakeOver: Brooklyn", opponent="Sasha Banks", opponent_html=True,
         stip="Singles — the match that made the women's revolution undeniable",
         title="NXT Women's Championship"),
    dict(result="W", date="2015-10-07", promo="WWE", landmark=True,
         event="NXT TakeOver: Respect", opponent="Sasha Banks", opponent_html=True,
         stip="30-minute Iron Man main event — the first women's Iron Man match in WWE and "
              "the first women's main event of a TakeOver",
         title="NXT Women's Championship"),
    dict(result="L", date="2016-04-01", promo="WWE",
         event="NXT TakeOver: Dallas", opponent="Asuka",
         stip="Singles — the 223-day NXT reign ends", title="NXT Women's Championship"),
    dict(result="W", date="2017-02-13", promo="WWE", landmark=True,
         event="Raw", opponent="Charlotte Flair",
         stip="Singles — her first main-roster world title", title="WWE Raw Women's Championship"),
    dict(result="W", date="2019-02-17", promo="WWE", type="tag", landmark=True,
         event="Elimination Chamber", opponent="Five other teams",
         stip="Tag team Elimination Chamber, with Sasha Banks — the inaugural champions",
         title="WWE Women's Tag Team Championship"),
    dict(result="W", date="2019-05-19", promo="WWE", landmark=True,
         event="Money in the Bank", opponent="Charlotte Flair",
         stip="Cash-in the same night she won the briefcase — recognised as the first "
              "Women's Grand Slam Champion",
         title="WWE SmackDown Women's Championship"),
    dict(result="L", date="2020-10-25", promo="WWE", landmark=True,
         event="Hell in a Cell", opponent="Sasha Banks", opponent_html=True,
         stip="Hell in a Cell — the 380-day reign ends", title="WWE SmackDown Women's Championship"),
    dict(result="W", date="2024-01-27", promo="WWE", type="tag", landmark=True,
         event="Royal Rumble", opponent="The 2024 women's Rumble field",
         stip="Won from No. 3, lasting over an hour", title=""),
    dict(result="W", date="2024-04-07", promo="WWE", landmark=True,
         event="WrestleMania XL Night 2", opponent="Iyo Sky",
         stip="Singles — the Damage CTRL payoff", title="WWE Women's Championship"),
    dict(result="L", date="2024-08-03", promo="WWE",
         event="SummerSlam — Cleveland", opponent="Nia Jax",
         stip="Singles — the 118-day reign ends", title="WWE Women's Championship"),
    dict(result="L", date="2026-04-18", promo="WWE", type="tag",
         event="WrestleMania 42 Night 1 — Las Vegas", opponent="Three other teams",
         stip="Fatal four-way with Lyra Valkyria — Brie Bella & a returning Paige win; "
              "Bayley left the building visibly angry",
         title="WWE Women's Tag Team Championship"),
    dict(result="L", date="2026-07-18", promo="WWE", landmark=True,
         event="Saturday Night's Main Event — New York", opponent="Lyra Valkyria",
         stip="Bulldog Choke, then a post-match attack on the steel steps that wrote her off "
              "television — her last televised match to date",
         title=""),
]

# opponent_html rows carry a real <a>, so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Sasha Banks": "mercedes-mone"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="bayley",
    name="Bayley",
    realname="Pamela Rose Martinez",
    epithet="The Role Model",
    hook="Record & Titles",

    meta_desc=("Bayley, The Role Model, is a four-time world champion, the first Women's Grand Slam "
               "Champion and the 2024 Royal Rumble winner — currently off WWE television with her "
               "contract status unresolved. Full record, titles, factions, records and career."),
    og_desc=("The Role Model: 4 world title reigns, a 380-day SmackDown reign, the 2024 Royal Rumble, "
             "and the first Women's Grand Slam. Off TV since July 18, 2026 — status unresolved."),
    tw_desc="The Role Model: 4 world titles, the 2024 Rumble, the first Women's Grand Slam — and an open question.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2008",
    height_imp="5&#8242;6&#8243;",
    weight_lb="119",
    world_titles="4",
    vitals_tagline="The Role Model",
    support_note="Merch &middot; Games &middot; Read",
    x_url="https://x.com/itsBayleyWWE",
    ig_url="https://www.instagram.com/itsmebayley/",
    sp_items=[
        dict(ic="BA", title="Bayley Merch", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable in 2K17 through 2K26",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="NXT", title="The NXT Years", sub="Brooklyn & the Iron Man match",
             tag="Watch", href="https://www.wwe.com/shows/wwenxt"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/bayley"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Hugger &middot; The Golden Role Model &middot; Damage CTRL's founder",
    hero_tag="San Jose, California &middot; <em>Independents &middot; NXT &middot; WWE &middot; "
             "2008&ndash;present</em>",
    now_label="NOW",
    now_bold="Off WWE television, future unresolved",
    now_tail=" &middot; written off by Lyra Valkyria on July 18, 2026; contract reports conflict, and "
             "the Observer suggests she may have quietly re-signed",
    hstats=[
        dict(value="4",   x=True,  label="World Titles"),
        dict(value="380", x=False, label="Day Title Reign"),
        dict(value="2024", x=False, label="Royal Rumble Winner"),
        dict(value="1st", x=False, label="Women's Grand Slam"),
    ],
    ghost_link="From the hugger to the open question",
    vlabel="Est. 2008 &middot; San Jose, California",
    mono="BA",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Bayley</b> has spent a decade being the connective tissue of WWE's women's division "
        "&mdash; the fourth Horsewoman, the other half of the matches that made the revolution, the "
        "founder of its dominant faction, and the first woman to complete the Grand Slam &mdash; and "
        "as this page is compiled she is the division's biggest open question. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">380</span>'
        '<span class="pull-cap">days in her second SmackDown Women&rsquo;s Championship reign, 2019&ndash;20 &mdash; the longest of her four world title reigns</span></span>'
        "The verified record: four main-roster world championship reigns &mdash; one Raw, two "
        "SmackDown, one WWE Women's &mdash; plus an NXT Women's Championship, the inaugural WWE "
        "Women's Tag Team Championship with Sasha Banks, the 2024 Royal Rumble from the No. 3 spot, "
        "and recognition as the <b>first Women's Grand Slam Champion</b>.",

        "The line circulating in August 2026 is that &ldquo;Bayley is done with WWE.&rdquo; Nothing "
        "verifies it, and the sourced version is messier and more interesting. Lyra Valkyria beat her "
        "at Saturday Night's Main Event on <b>July 18, 2026</b> with the Bulldog Choke, then reapplied "
        "it on the steel steps in an angle built to write her off television; on Raw, Valkyria claimed "
        "she &ldquo;ran Bayley outta here.&rdquo; The contract reporting does not even agree with "
        "itself: F4W placed the expiry around <b>Q4 2026</b>, while later reports cited by Khel Now "
        "stretch it to <b>January 2027</b>. Since then Bayley has worked untelevised WWE live events "
        "in Stockton and Bakersfield, WWE kept referencing her on the August 24 Raw, and Dave Meltzer "
        "reasoned on Observer Radio that the company would hardly keep doing that if she were "
        "definitely gone &mdash; while AEW interest was reported by Wrestling Inc. and Mercedes Mone "
        "teased her on social media. Every one of those facts is real; no conclusion is. This page "
        "publishes the question, not an answer.",

        "She was born Pamela Rose Martinez on June 15, 1989 in San Jose, debuted on the California "
        "independents in 2008 as Davina Rose, and signed with WWE in December 2012. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">2015</span>'
        '<span class="pull-cap">the year of Brooklyn and the Iron Man match &mdash; the two Sasha Banks bouts that made the division main-event material</span></span>'
        "As the hugging underdog she beat Sasha Banks at TakeOver: Brooklyn on August 22, 2015 for the "
        "NXT Women's Championship, then won the 30-minute Iron Man rematch at TakeOver: Respect "
        "&mdash; the first women's Iron Man match in WWE and the first women's main event of a "
        "TakeOver. The main-roster version took longer to land: a Raw Women's Championship from "
        "Charlotte Flair in February 2017, then a slide into catchphrase purgatory, then the 2019 "
        "reinvention &mdash; inaugural tag champion with Banks in February, Money in the Bank winner "
        "and same-night cash-in champion in May, and, after the crowd finally turned, the 2019 heel "
        "run that produced the 380-day SmackDown reign she is still best remembered for.",

        "The last four years split into a triumph and a fade. She founded <b>Damage CTRL</b> at "
        "SummerSlam 2022 with Dakota Kai and Iyo Sky, got thrown out of her own faction in early 2024, "
        "and turned the ejection into the best babyface run of her career: the Royal Rumble win on "
        "January 27, 2024, and the WWE Women's Championship from Iyo Sky at WrestleMania XL Night 2. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">118</span>'
        '<span class="pull-cap">days as WWE Women&rsquo;s Champion in 2024, ended by Nia Jax at SummerSlam &mdash; her last title reign to date</span></span>'
        "Since Nia Jax took the title at SummerSlam 2024 the arc has bent downward: pulled from "
        "WrestleMania 41 after a backstage attack that was never explained on-screen, repackaged as "
        "Lyra Valkyria's mentor through the &ldquo;Role Model&rdquo; year, on the losing end of the "
        "WrestleMania 42 tag title four-way won by Brie Bella and a returning Paige &mdash; after "
        "which she reportedly stormed out of the building &mdash; and finally choked out at Saturday "
        "Night's Main Event in July 2026 by the protege who decided the mentor was dead weight. "
        "Whether that was a farewell or a setup is the thing nobody &mdash; possibly including WWE "
        "&mdash; can currently say.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Highlight set",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("4&times;", "World titles"),
            ("380",      "Day SmackDown reign"),
            ("2024",     "Royal Rumble winner"),
            ("1st",      "Women's Grand Slam"),
            ("1",        "NXT Women's reign"),
            ("1",        "Tag title reign"),
        ],
        lead=("Twelve documented bouts &mdash; a highlight subset, not a career count, and no career "
              "win&ndash;loss total is published because none was verified. The rows run from "
              "Brooklyn 2015 to the July 18, 2026 Saturday Night's Main Event loss that currently "
              "stands as her last televised match. Her 2026 Royal Rumble participation could not be "
              "confirmed either way and is omitted rather than guessed. Filter by match type, tap any "
              "column header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("Four bouts the reputation rests on. The ratings are this dossier's own editorial "
                    "grades, not Wrestling Observer figures &mdash; no Meltzer ratings were verified "
                    "in this pass and none are quoted."),
    signature=[
        dict(rating="4.5", event="NXT TakeOver: Brooklyn 2015", opponent="Sasha Banks",
             stip="NXT Women's Championship — the division's proof of concept"),
        dict(rating="4.5", event="NXT TakeOver: Respect 2015", opponent="Sasha Banks",
             stip="30-minute Iron Man main event — NXT Women's Championship"),
        dict(rating="4.0", event="WrestleMania XL Night 2", opponent="Iyo Sky",
             stip="WWE Women's Championship — the Damage CTRL story pays off"),
        dict(rating="3.5", event="Hell in a Cell 2020", opponent="Sasha Banks",
             stip="Hell in a Cell — the Boss 'n' Hug breakup blowoff"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("4&times;", "World title reigns"),
            ("380",      "Longest reign (days)"),
            ("1st",      "Women's Grand Slam"),
            ("0",        "Titles since Aug 2024"),
        ],
        lead=("Four world championship reigns across three lineages, plus the NXT and inaugural tag "
              "titles. She has held nothing since SummerSlam 2024, which is part of why the 2026 "
              "contract story reads the way it does."),
        rows=[
            dict(ic="S", name="SmackDown Women's Championship", count="2",
                 sub="2019, won by Money in the Bank cash-in on Charlotte Flair the night she won the "
                     "briefcase, May 19 &middot; 2019&ndash;20, regained October 11, 2019 in the "
                     "heel-turn era and held <b>380 days</b> until Sasha Banks beat her inside Hell in "
                     "a Cell on October 25, 2020 &mdash; the longest reign in the title's history at "
                     "the time"),
            dict(ic="W", name="WWE Women's Championship", count="1",
                 sub="2024 &middot; won from Iyo Sky at WrestleMania XL Night 2 on April 7 &middot; "
                     "118 days, ended by Nia Jax at SummerSlam on August 3"),
            dict(ic="R", name="Raw Women's Championship", count="1",
                 sub="2017 &middot; won from Charlotte Flair on the February 13 Raw &middot; lost to "
                     "Alexa Bliss at Payback on April 30"),
            dict(ic="T", name="WWE Women's Tag Team Championship", count="1",
                 sub="2019 &middot; inaugural champions with Sasha Banks, won in the tag team "
                     "Elimination Chamber on February 17 &middot; a 2020 second reign as a duo is "
                     "widely listed for Banks' side of the team and was not independently verified "
                     "for this page's count, so only the inaugural reign is claimed here"),
            dict(ic="N", name="NXT Women's Championship", count="1",
                 sub="2015&ndash;16 &middot; won from Sasha Banks at TakeOver: Brooklyn on August 22, "
                     "2015, lost to Asuka at TakeOver: Dallas on April 1, 2016 &middot; 223 days"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="A press label, a tag team, the faction she founded and was thrown out of, and a "
             "mentorship that ended on the steel steps.",
        cards=[
            dict(era="NXT &middot; 2013&ndash;15 &middot; press framing, not a booked unit",
                 name="The Four Horsewomen",
                 members="Bayley, Sasha Banks, Charlotte Flair, Becky Lynch",
                 desc="Never an on-screen alliance — a media and fan label for the four who came up "
                      "through NXT together, which WWE used editorially but never booked as a group. "
                      "Bayley was the last of the four to reach the main roster and, by the "
                      "underdog logic of the era, the emotional centre of it. In August 2026 she was "
                      "still invoking it: TWNP reported her floating a Horsewomen tag match that "
                      "would have to wait until, in her words, Sasha Banks comes back to WWE."),
            dict(era="WWE &middot; 2016&ndash;20",
                 name="The Boss 'n' Hug Connection",
                 members="Bayley, Sasha Banks",
                 desc="Best friends, inaugural WWE Women's Tag Team Champions at Elimination Chamber "
                      "2019, and then the long turn: Bayley's 2019 heel run set up the betrayal arc "
                      "that ended with Banks beating her inside Hell in a Cell in October 2020. The "
                      "friendship is the single longest-running story of her career."),
            dict(era="WWE &middot; 2022&ndash;24",
                 name="Damage CTRL",
                 members="Bayley (founder), Iyo Sky, Dakota Kai; later Asuka, Kairi Sane",
                 desc="Founded on her return at SummerSlam 2022 after a year out with a torn ACL. The "
                      "faction won everything around her while she stayed titleless, and in early "
                      "2024 it ejected her — the betrayal that powered her Royal Rumble win and the "
                      "WrestleMania XL title victory over Iyo Sky, the member who had eclipsed her."),
            dict(era="WWE &middot; 2025&ndash;26",
                 name="Bayley & Lyra Valkyria",
                 members="Bayley, Lyra Valkyria",
                 desc="The mentorship that gave the Role Model name its literal meaning — a year of "
                      "teaming that peaked with a WrestleMania 42 tag title four-way and collapsed "
                      "immediately after it: Valkyria turned on her following a loss to champions "
                      "Brie Bella and Paige, accused her of holding her back, and choked her out at "
                      "Saturday Night's Main Event on July 18, 2026. That angle is, as of today, the "
                      "last thing Bayley did on WWE television."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One person, played at different volumes &mdash; the hugger, the heel who cut the hair "
             "off the hugger, and the Role Model who took the name literally.",
        cards=[
            dict(mono="DR", era="Independents &middot; 2008&ndash;12", name="Davina Rose",
                 desc="The California independent years, starting at eighteen around Big Time "
                      "Wrestling in the Bay Area. Four years of anonymity that the WWE character "
                      "quietly drew on: the superfan who made it."),
            dict(mono="HG", era="NXT & WWE &middot; 2013&ndash;19", name="The Hugger",
                 desc="Side ponytail, tube men, hugs. Easy to parody and impossible to replicate — "
                      "the most purely loved babyface act of the NXT era, and the one that beat "
                      "Sasha Banks in Brooklyn. On the main roster the same act slowly curdled into "
                      "catchphrase filler, which is what made what came next work."),
            dict(mono="RM", era="WWE &middot; 2019&ndash;21", name="The Golden Role Model",
                 desc="The 2019 heel turn: hair cut on camera, tube men murdered, and the best run "
                      "of her career — the 380-day SmackDown reign, both belts at once with Banks as "
                      "tag champion, and a genuine claim to being 2020's wrestler of the year before "
                      "a torn ACL in July 2021 stopped everything."),
            dict(mono="DC", era="WWE &middot; 2022&ndash;26", name="Role Model, literal edition",
                 desc="Damage CTRL founder, then Damage CTRL exile, then 2024 Rumble winner and WWE "
                      "Women's Champion, then actual role model to Lyra Valkyria — a mentorship that "
                      "ended with the student choking the teacher out on the steel steps in July "
                      "2026. Whether the character has a next chapter is currently a contract "
                      "question, not a creative one."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="San Jose to Brooklyn to an unresolved August.",
        rows=[
            dict(year="2008", title="Debuts as Davina Rose",
                 desc="Starts on the California independents at eighteen; WWE signs her in December "
                      "2012 and she becomes Bayley in NXT."),
            dict(year="2015", title="Brooklyn and the Iron Man match",
                 desc="Beats Sasha Banks at TakeOver: Brooklyn on August 22 for the NXT Women's "
                      "Championship, then wins the 30-minute Iron Man rematch at TakeOver: Respect "
                      "on October 7 — the first women's main event of a TakeOver."),
            dict(year="2016", title="The reign ends; the main roster begins",
                 desc="Asuka takes the NXT title at TakeOver: Dallas on April 1 after 223 days. "
                      "Bayley debuts on Raw that summer."),
            dict(year="2017", title="First main-roster world title",
                 desc="Beats Charlotte Flair on the February 13 Raw for the Raw Women's Championship; "
                      "loses it to Alexa Bliss at Payback."),
            dict(year="2019", title="Grand Slam year",
                 desc="Inaugural Women's Tag Team Champion with Banks in the Elimination Chamber on "
                      "February 17; wins Money in the Bank on May 19 and cashes in the same night on "
                      "Charlotte Flair, completing the first Women's Grand Slam; turns heel in "
                      "October and starts the 380-day reign."),
            dict(year="2020", title="The 380 days end",
                 desc="Sasha Banks beats her inside Hell in a Cell on October 25, ending the longest "
                      "SmackDown Women's Championship reign to that point."),
            dict(year="2021", title="The ACL year",
                 desc="Tears an ACL in training in July, days before a planned return program — out "
                      "roughly a year."),
            dict(year="2022", title="Founds Damage CTRL",
                 desc="Returns at SummerSlam on July 30 with Dakota Kai and Iyo Sky. The faction "
                      "dominates the division while she stays titleless."),
            dict(year="2024", title="Rumble, WrestleMania, and the slide",
                 desc="Thrown out of Damage CTRL, wins the Royal Rumble on January 27 from No. 3, "
                      "beats Iyo Sky for the WWE Women's Championship at WrestleMania XL Night 2 on "
                      "April 7, and loses it to Nia Jax at SummerSlam on August 3 after 118 days."),
            dict(year="2025", title="Pulled from WrestleMania, repackaged as mentor",
                 desc="Removed from WrestleMania 41 after a backstage attack angle that was never "
                      "explained on-screen; returns mid-year and spends the rest of it mentoring "
                      "Lyra Valkyria."),
            dict(year="2026", title="The write-off",
                 desc="Loses the WrestleMania 42 tag title four-way with Valkyria on April 18 — won "
                      "by Brie Bella and a returning Paige — and reportedly storms out; Valkyria "
                      "turns on her, then chokes her out at Saturday Night's Main Event on July 18. "
                      "Off television since, with contract reports conflicting and house-show "
                      "appearances in Stockton and Bakersfield in August."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who she went to war with.",
        cards=[
            dict(name="Sasha Banks", slug="mercedes-mone",
                 desc="The career-defining series: Brooklyn 2015 and the Iron Man match made the "
                      "women's division a main-event act, the inaugural tag reign made them "
                      "champions together, and Hell in a Cell 2020 ended the friendship and the "
                      "380-day reign in one night. Now employed by different companies — which is "
                      "exactly why Mercedes Mone teasing her on social media in August 2026 read "
                      "as more than nostalgia."),
            dict(name="Iyo Sky",
                 desc="The Damage CTRL account: Bayley recruited her, Sky eclipsed her, the faction "
                      "chose Sky, and Bayley beat her for the WWE Women's Championship at "
                      "WrestleMania XL Night 2 — the cleanest revenge arc of her career, and the "
                      "last big thing she won."),
            dict(name="Lyra Valkyria",
                 desc="The live one. A year of mentorship, a WrestleMania 42 tag failure, and a turn: "
                      "Valkyria beat her with the Bulldog Choke at Saturday Night's Main Event on "
                      "July 18, 2026, reapplied it on the steps, and told Raw she'd run Bayley out "
                      "of the company — dialogue WWE kept feeding as late as the August 24 Raw. If "
                      "Bayley returns, this is the feud waiting for her."),
            dict(name="Charlotte Flair",
                 desc="The measuring stick: Bayley's first main-roster title came from her in "
                      "February 2017, and the Money in the Bank 2019 cash-in that made Bayley the "
                      "first Grand Slam champion came at her expense too. Flair won most of the "
                      "series; Bayley won the nights that counted."),
            dict(name="Nia Jax",
                 desc="The 2024 program that ended the last reign — Jax took the WWE Women's "
                      "Championship at SummerSlam in Cleveland — and, via Jax and Lash Legend's "
                      "title defense in the WrestleMania 42 four-way, indirectly the start of the "
                      "2026 unravelling too."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Thin by design &mdash; she is a wrestler's wrestler, and the verified list is short.",
        rows=[
            dict(when="2016&ndash;", title="WWE 2K", kind="Game",
                 desc="Playable from WWE 2K17 through WWE 2K26. She has never been a cover star."),
            dict(when="2015&ndash;", title="The NXT documentary era", kind="TV",
                 desc="A recurring presence in WWE's own long-form programming around the women's "
                      "revolution — the Brooklyn and Iron Man matches anchor most retellings of the "
                      "era. No scripted film or television role could be verified, so none is "
                      "listed."),
            dict(when="2020", title="\"Ding Dong, Hello!\"", kind="Segment",
                 desc="Her self-hosted heel talk show, remembered fondly enough that the catchphrase "
                      "outlived the set. Included here because it is the closest thing the resume "
                      "has to a media franchise, which is itself the point about the resume."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records that are actually hers &mdash; and the open question, stated as one.",
        stats=[
            ("1st", "Women's Grand Slam"),
            ("380", "Day SmackDown reign"),
            ("2024", "Royal Rumble winner"),
        ],
        rows=[
            dict(name="First Women's Grand Slam Champion",
                 sub="Completed on May 19, 2019, when the Money in the Bank cash-in gave her the "
                     "SmackDown Women's Championship to go with the Raw, NXT and Women's Tag Team "
                     "titles — the first woman to hold all four under WWE's then-definition. Later "
                     "Grand Slam claimants use later definitions; hers came first."),
            dict(name="380 days as SmackDown Women's Champion, 2019-20",
                 sub="October 11, 2019 to October 25, 2020 — the longest reign in that title's "
                     "history at the time, and still the number most attached to her name."),
            dict(name="2024 Royal Rumble winner from the No. 3 spot",
                 sub="January 27, 2024, lasting over an hour — the win that converted the Damage "
                     "CTRL ejection into the WrestleMania XL title victory over Iyo Sky."),
            dict(name="First women's main event of an NXT TakeOver — and the first women's Iron Man match in WWE",
                 sub="TakeOver: Respect, October 7, 2015, against Sasha Banks — 30 minutes, and "
                     "Bayley won the deciding fall. The milestone is shared with Banks the way all "
                     "match milestones are."),
            dict(name="Inaugural WWE Women's Tag Team Champion",
                 sub="With Sasha Banks, in the tag team Elimination Chamber on February 17, 2019."),
            dict(name="Four world championship reigns across three lineages",
                 sub="Raw (2017), SmackDown twice (2019, 2019-20) and the WWE Women's Championship "
                     "(2024) — plus the NXT Women's Championship, which WWE does not count as a "
                     "world title and neither does this page."),
            dict(name="The open question, August 2026",
                 sub="Written off television July 18, 2026. Contract expiry reported as Q4 2026 by "
                     "F4W and as late as January 2027 in reports cited by Khel Now — a live "
                     "conflict, printed as one. Working non-televised WWE live events in "
                     "California in August; referenced on the August 24 Raw; Observer speculation "
                     "that she may have quietly re-signed; reported AEW interest. Nothing is "
                     "confirmed in either direction."),
        ],
        footnote=("No career win-loss total, match count or aggregate rating appears anywhere on this "
                  "page; none was verified. Her 2026 Royal Rumble participation and the identity of "
                  "her WrestleMania 41 attacker are both unverified and both omitted rather than "
                  "guessed."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="X / Twitter", v="@itsBayleyWWE", href="https://x.com/itsBayleyWWE"),
        dict(k="Instagram", v="@itsmebayley", href="https://www.instagram.com/itsmebayley/"),
        dict(k="F4W", v="Contract speculation after the Valkyria angle",
             href="https://www.f4wonline.com/news/wwe/bayley-wwe-future-lyra-valkyria-raw/"),
        dict(k="Khel Now", v="The quiet re-signing report, August 26, 2026",
             href="https://khelnow.com/wwe/wwe-bayley-may-have-quietly-re-signed-202608"),
        dict(k="TWNP-News", v="Status update — house shows, Horsewomen tease",
             href="https://www.twnpnews.com/2026/07/bayley-returns-to-wwe/"),
        dict(k="WWE.com", v="Saturday Night's Main Event — Bayley vs. Lyra Valkyria",
             href="https://www.wwe.com/shows/snme/2026-07-18/bayley-vs-lyra-valkyria"),
        dict(k="Pro Wrestling Dot Net", v="WrestleMania 42 lineups",
             href="https://prowrestling.net/site/2026/04/18/wrestlemania-42-lineup-live-coverage-tonight-the-cards-for-both-nights-opening-matches-for-the-espn-and-espn2-simulcasts/"),
        dict(k="On3", v="WrestleMania 42 — the tag title four-way result",
             href="https://www.on3.com/pro/news/wwe-wrestlemania-42-night-1-results-brie-bella-and-returning-paige-saraya-win-womens-tag-titles/"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/bayley.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Has Bayley left WWE?",
            a="Unknown &mdash; and this page will not pretend otherwise. The facts: Lyra Valkyria "
              "beat her and attacked her at Saturday Night's Main Event on <b>July 18, 2026</b> in an "
              "angle built to write her off television, and she has not appeared on WWE TV since. Her "
              "contract expiry has been reported as <b>Q4 2026</b> (F4W) and as late as <b>January "
              "2027</b> (reports cited by Khel Now) &mdash; a live conflict. Against departure: she "
              "worked WWE live events in Stockton and Bakersfield in August, WWE kept referencing her "
              "on the August 24 Raw, and Dave Meltzer suggested on Observer Radio that she may have "
              "quietly re-signed. For it: reported AEW interest, and Mercedes Mone teasing her on "
              "social media. Nothing is confirmed either way as of August 31, 2026.",
            q_ld="Has Bayley left WWE?",
            a_ld="It is unconfirmed as of August 31, 2026. Bayley was written off WWE television on "
                 "July 18, 2026, when Lyra Valkyria defeated and attacked her at Saturday Night's Main "
                 "Event. Reports place her contract expiry between late 2026 and January 2027. She "
                 "has since worked non-televised WWE live events in Stockton and Bakersfield, "
                 "California, was referenced on the August 24, 2026 episode of Raw, and Dave Meltzer "
                 "has speculated she may have quietly re-signed, while AEW interest has also been "
                 "reported. Neither WWE nor Bayley has confirmed anything."),
        dict(
            q="Was Bayley really the first Women's Grand Slam Champion?",
            a="Yes, under the definition WWE used when it recognised her. When she cashed in Money in "
              "the Bank on Charlotte Flair on <b>May 19, 2019</b>, she became the first woman to have "
              "held the Raw, SmackDown, NXT and Women's Tag Team Championships. Later wrestlers are "
              "called Grand Slam champions under later definitions &mdash; the becky-lynch dossier on "
              "this site, for instance, records Becky Lynch as the <i>sixth</i> under the current "
              "table &mdash; but Bayley's came first, and WWE said so at the time.",
            q_ld="Was Bayley the first WWE Women's Grand Slam Champion?",
            a_ld="Yes. When Bayley cashed in her Money in the Bank contract on Charlotte Flair on May "
                 "19, 2019 to win the SmackDown Women's Championship, she became the first woman to "
                 "have held the Raw Women's, SmackDown Women's, NXT Women's and WWE Women's Tag Team "
                 "Championships, and WWE recognised her as the first Women's Grand Slam Champion. "
                 "Later Grand Slam designations use revised definitions."),
        dict(
            q="What happened between Bayley and Lyra Valkyria?",
            a="A year of mentorship that ended in a turn. They teamed through the Role Model year and "
              "into the WrestleMania 42 tag title four-way on April 18, 2026, which Brie Bella and a "
              "returning Paige won; after a subsequent loss to those champions, Valkyria attacked "
              "Bayley, said the mentorship had been holding her back, and &mdash; when Bayley got the "
              "match arranged through Adam Pearce &mdash; beat her with the Bulldog Choke at Saturday "
              "Night's Main Event on July 18, 2026, then reapplied it on the steel steps until Bayley "
              "foamed at the mouth. On Raw she claimed she &ldquo;ran Bayley outta here.&rdquo; That "
              "is where the story currently sits.",
            q_ld="What happened between Bayley and Lyra Valkyria?",
            a_ld="Bayley mentored and teamed with Lyra Valkyria for roughly a year, including a "
                 "WWE Women's Tag Team Championship fatal four-way at WrestleMania 42 on April 18, "
                 "2026, which Brie Bella and Paige won. Valkyria then turned on Bayley, accusing her "
                 "of holding her back, and defeated her with the Bulldog Choke at Saturday Night's "
                 "Main Event on July 18, 2026, attacking her on the steel steps afterwards. The angle "
                 "wrote Bayley off WWE television, and Valkyria has since claimed on Raw that she ran "
                 "Bayley out of the company."),
        dict(
            q="Why was Bayley pulled from WrestleMania 41?",
            a="On-screen, she was taken out by a backstage attack before her scheduled match in April "
              "2025, and her spot went to Lyra Valkyria's side of the story &mdash; the beginning of "
              "the thread that ran all the way to the 2026 turn. The attacker was never identified on "
              "television in any source consulted for this page, and no reporting verified a "
              "definitive behind-the-scenes explanation, so none is offered here.",
            q_ld="Why was Bayley removed from WrestleMania 41?",
            a_ld="Bayley was removed from WrestleMania 41 in April 2025 via an on-screen backstage "
                 "attack angle before her scheduled match. The attacker was never identified on WWE "
                 "television in the sources consulted for this page, and no verified behind-the-"
                 "scenes explanation has been published, so the question remains open."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Pamela Rose Martinez"),
        dict(label="Born", value="June 15, 1989", sub="San Jose, California &middot; age 37"),
        dict(label="Billed from", value="San Jose, California"),
        dict(label="Height", value="5&#8242;6&#8243;", sub="168 cm"),
        dict(label="Weight", value="119 lb", sub="54 kg &middot; as commonly listed; WWE.com lists no weight"),
        dict(label="Debut", value="2008", sub="California independents, as Davina Rose"),
        dict(label="WWE signing", value="December 2012", sub="NXT from 2013"),
        dict(label="Finishers", value="Rose Plant &middot; Bayley-to-Belly",
             sub="the suplex named the era; the Rose Plant carried the heel years"),
        dict(label="Last televised match", value="July 18, 2026",
             sub="L to Lyra Valkyria, Saturday Night's Main Event &mdash; written off after"),
        dict(label="Contract", value="Reported Q4 2026 &ndash; January 2027",
             sub="F4W vs. reports cited by Khel Now &mdash; unresolved, printed as a conflict"),
        dict(label="Brand", value="Raw", sub="as of her last appearances"),
        dict(label="Also known as",
             value="The Role Model &middot; The Hugger &middot; The Golden Role Model &middot; "
                   "Davina Rose"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1989-06-15",
    bornplace="San Jose, California, United States",
    nationality="United States",
    height_cm=168,
    weight_kg=54,
    ld=dict(
        alternateName=["Pamela Rose Martinez", "Davina Rose", "The Hugger", "The Golden Role Model",
                       "The Role Model"],
        award=["SmackDown Women's Championship (2 reigns, including 380 days in 2019-20)",
               "WWE Women's Championship (1 reign, 2024)",
               "Raw Women's Championship (1 reign, 2017)",
               "WWE Women's Tag Team Championship (inaugural champion, with Sasha Banks, 2019)",
               "NXT Women's Championship (1 reign, 223 days, 2015-16)",
               "Royal Rumble winner (2024)",
               "Money in the Bank winner (2019)",
               "First WWE Women's Grand Slam Champion (2019)"],
        knowsAbout=["Professional wrestling", "WWE", "NXT", "Women's professional wrestling",
                    "Championship wrestling", "Damage CTRL"],
        description="Bayley is an American professional wrestler known as The Role Model. A four-time "
                    "world champion in WWE, she was recognised as the first Women's Grand Slam "
                    "Champion in 2019, held the SmackDown Women's Championship for 380 days, won the "
                    "2024 Royal Rumble and the WWE Women's Championship at WrestleMania XL, and was "
                    "half of the 2015 NXT matches with Sasha Banks that defined the women's "
                    "revolution. As of August 31, 2026 she is off WWE television following a July "
                    "2026 angle with Lyra Valkyria, with her contract status publicly unresolved.",
        sameAs=["https://x.com/itsBayleyWWE",
                "https://www.instagram.com/itsmebayley/",
                "https://en.wikipedia.org/wiki/Bayley_(wrestler)",
                "https://www.wwe.com/superstars/bayley"],
    ),
)
