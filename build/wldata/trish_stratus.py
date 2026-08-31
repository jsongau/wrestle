# -*- coding: utf-8 -*-
"""Trish Stratus - dossier data.

Compiled August 31, 2026. Sources are the web pages opened for this build
(Wikipedia, WWE.com's Evolution 2025 match page, WWE.com profile, Sports
Illustrated, ClutchPoints) plus verified career history. She is a legend, not
an active wrestler: the "now" fields describe her actual current standing —
last match July 13, 2025, a stated desire for one more "finale moment," and a
2026 European-tour tease that produced nothing — and invent no activity.

Deliberate omissions:
  * No career win-loss total — none verified.
  * Her height is published as a conflict: WWE.com says 5'5", Wikipedia-derived
    listings commonly say 5'4". Both are printed; neither is adopted silently.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2001-11-18", promo="WWE", type="tag", landmark=True,
         event="Survivor Series", opponent="Jazz, Jacqueline, Ivory, Lita & Molly Holly",
         stip="Six-pack challenge for the vacant title — the first of a record seven",
         title="WWF Women's Championship"),
    dict(result="W", date="2003-03-30", promo="WWE", type="tag", landmark=True,
         event="WrestleMania XIX", opponent="Victoria & Jazz",
         stip="Triple threat — her only WrestleMania title win",
         title="WWE Women's Championship"),
    dict(result="W", date="2004-06-13", promo="WWE", type="tag",
         event="Bad Blood", opponent="Lita, Victoria & Gail Kim",
         stip="Fatal four-way — the fifth reign, as the division's top heel",
         title="WWE Women's Championship"),
    dict(result="L", date="2004-12-06", promo="WWE", landmark=True,
         event="Raw", opponent="Lita", opponent_html=True,
         stip="The first women's match to main event Raw",
         title="WWE Women's Championship"),
    dict(result="W", date="2005-01-09", promo="WWE",
         event="New Year's Revolution", opponent="Lita", opponent_html=True,
         stip="Singles — regains the title; the 448-day sixth reign begins",
         title="WWE Women's Championship"),
    dict(result="L", date="2006-04-02", promo="WWE", landmark=True,
         event="WrestleMania 22", opponent="Mickie James",
         stip="Singles — the 448-day reign ends", title="WWE Women's Championship"),
    dict(result="W", date="2006-09-17", promo="WWE", landmark=True,
         event="Unforgiven — Toronto", opponent="Lita", opponent_html=True,
         stip="Retirement match in her hometown — wins a seventh title and leaves as champion",
         title="WWE Women's Championship"),
    dict(result="W", date="2011-04-03", promo="WWE", type="tag",
         event="WrestleMania XXVII", opponent="Dolph Ziggler & LayCool",
         stip="Six-person mixed tag, with John Morrison & Snooki", title=""),
    dict(result="L", date="2018-01-28", promo="WWE", type="tag", landmark=True,
         event="Royal Rumble", opponent="The first women's Royal Rumble field",
         stip="Entered No. 30 and eliminated three", title=""),
    dict(result="W", date="2018-10-28", promo="WWE", type="tag", landmark=True,
         event="Evolution", opponent="Mickie James & Alicia Fox",
         stip="With Lita, at WWE's first all-women pay-per-view", title=""),
    dict(result="L", date="2019-08-11", promo="WWE", landmark=True,
         event="SummerSlam — Toronto", opponent="Charlotte Flair",
         stip="Singles — billed at the time as her last match; she tapped to the Figure Eight",
         title=""),
    dict(result="W", date="2023-04-01", promo="WWE", type="tag",
         event="WrestleMania 39 Night 1", opponent="Damage CTRL",
         stip="Six-woman tag with Becky Lynch & Lita", title=""),
    dict(result="W", date="2023-05-27", promo="WWE",
         event="Night of Champions — Jeddah", opponent="Becky Lynch", opponent_html=True,
         stip="Singles — with an assist from protege Zoey Stark", title=""),
    dict(result="L", date="2023-09-02", promo="WWE",
         event="Payback", opponent="Becky Lynch", opponent_html=True,
         stip="Steel cage — her first cage match, at 47", title=""),
    dict(result="L", date="2025-02-01", promo="WWE", type="tag",
         event="Royal Rumble", opponent="The 2025 women's Rumble field",
         stip="Entered No. 25, eliminated by Nia Jax", title=""),
    dict(result="W", date="2025-03-01", promo="WWE", type="tag",
         event="Elimination Chamber — Toronto", opponent="Nia Jax & Candice LeRae",
         stip="Tag, with Tiffany Stratton — a hometown win in the 25th-anniversary year", title=""),
    dict(result="L", date="2025-07-13", promo="WWE", landmark=True,
         event="Evolution", opponent="Tiffany Stratton",
         stip="Singles — a WWE Women's Championship challenge at 49; her most recent match",
         title="WWE Women's Championship"),
]

# opponent_html rows carry a real <a>, so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Lita": "lita", "Becky Lynch": "becky-lynch"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="trish-stratus",
    name="Trish Stratus",
    realname="Patricia Anne Stratigeas",
    epithet="The Diva of the Decade",
    hook="Record & Titles",

    meta_desc=("Trish Stratus won a record seven WWE Women's Championships, held one of them for "
               "448 days, and retired as champion in her hometown — then kept coming back for two "
               "more decades. Full record, titles, factions, records and career."),
    og_desc=("The Diva of the Decade: 7 Women's Championship reigns, a 448-day reign, a hometown "
             "retirement as champion in 2006, and comebacks in four different decades of life."),
    tw_desc="Trish Stratus: 7 Women's titles, 448 days as champion, retired on top — and never quite gone.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2000",
    height_imp="5&#8242;4&#8243;",
    weight_lb="125",
    world_titles="7",
    vitals_tagline="100% Stratusfaction",
    support_note="Merch &middot; Yoga &middot; Watch",
    x_url="https://x.com/trishstratuscom",
    ig_url="https://www.instagram.com/trishstratuscom/",
    sp_items=[
        dict(ic="TS", title="Trish Stratus Merch", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="SY", title="Stratusphere", sub="Her yoga and fitness brand",
             tag="Visit", href="https://trishstratus.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable legend, including WWE 2K26",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/trish-stratus"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Seven-time champion &middot; Hall of Fame 2013 &middot; the fitness model who learned to be the best",
    hero_tag="Toronto, Ontario, Canada &middot; <em>WWF/WWE &middot; 2000&ndash;2006 &middot; and "
             "returns ever since</em>",
    now_label="NOW",
    now_bold="Legend — last match July 13, 2025",
    now_tail=" &middot; lost a WWE Women's Championship challenge to Tiffany Stratton at Evolution at "
             "49; says she wants one more &ldquo;finale moment,&rdquo; and teased the 2026 European "
             "tour without taking it",
    hstats=[
        dict(value="7",   x=True,  label="Women's Titles"),
        dict(value="448", x=False, label="Day Title Reign"),
        dict(value="2013", x=False, label="Hall of Fame Class"),
        dict(value="49",  x=False, label="Age at Last Title Match"),
    ],
    ghost_link="From fitness model to the standard everyone since is measured against",
    vlabel="Est. 2000 &middot; Toronto, Ontario",
    mono="TS",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Trish Stratus</b> is the transformation story the rest of women's wrestling still gets "
        "measured against: hired in 2000 as a fitness model to stand at ringside, retired in 2006 as "
        "a <b>seven-time WWE Women's Champion</b> who left the company holding the belt, having won "
        "it in her retirement match in her hometown. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">7</span>'
        '<span class="pull-cap">WWE Women&rsquo;s Championship reigns, 2001&ndash;2006 &mdash; a record in that title&rsquo;s history</span></span>'
        "The concrete record: seven reigns with the WWF/WWE Women's Championship between Survivor "
        "Series 2001 and Unforgiven 2006, a 448-day sixth reign, a Hardcore Championship for "
        "twenty-four hours of 2002, the 2013 Hall of Fame, three straight WWE Babe of the Year "
        "awards, the company's own Diva of the Decade designation &mdash; and then two decades of "
        "returns, the most recent a WWE Women's Championship match against Tiffany Stratton at "
        "Evolution on July 13, 2025, at age 49.",

        "Two claims travel with her name and both need calibrating. The first is &ldquo;greatest "
        "women's wrestler of all time,&rdquo; which even WWE.com hedges as &ldquo;perhaps.&rdquo; "
        "What the record supports without argument is narrower and still singular: the most reigns "
        "in the history of the original Women's Championship, and, per Wikipedia's accounting, a "
        "448-day reign &mdash; January 9, 2005 to April 2, 2006 &mdash; that stands as <b>the "
        "longest reign of any women's world champion in the 21st century</b>. Note the counting "
        "rules doing the work there: it excludes Asuka's 510-day NXT reign because WWE does not "
        "class the NXT title as a world championship, and Becky Lynch's 398 and Bianca Belair's 420 "
        "fall short of it. The second claim is that her seven reigns are &ldquo;the record for a "
        "single woman in WWE.&rdquo; They are the record <i>for that title</i>. Becky Lynch also "
        "has seven world reigns across two modern lineages, and Charlotte Flair has more across "
        "several; the honest sentence is that Trish's seven came in one championship's lineage, in "
        "five years, in a division she had to help build first.",

        "She was born Patricia Anne Stratigeas on December 18, 1975 in Toronto, was training at "
        "Sully's Gym under Ron Hutchison when WWF signed her in November 1999, and debuted on March "
        "19, 2000 as the valet for T&amp;A. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig pull-fig--sm">2004</span>'
        '<span class="pull-cap">the year of the first women&rsquo;s Raw main event &mdash; Trish vs. Lita, December 6, for the title Lita took that night</span></span>'
        "The early years were storyline chum &mdash; the Mr. McMahon angle, the &ldquo;bark like a "
        "dog&rdquo; segment &mdash; and her answer was to become, by consensus of the locker room "
        "and the tape, a genuinely great wrestler: the 2001 six-pack challenge title win, the "
        "WrestleMania XIX triple threat, the 2004&ndash;05 heel run opposite Lita that produced the "
        "first women's main event in Raw history on December 6, 2004, and the Mickie James "
        "obsessed-fan saga that peaked at WrestleMania 22. When she retired at Unforgiven on "
        "September 17, 2006, beating Lita with the Sharpshooter in a Toronto building screaming "
        "&ldquo;thank you Trish,&rdquo; it was the rare wrestling goodbye executed exactly right.",

        "Except she has never entirely stayed gone, and the returns have their own resume: the "
        "WrestleMania XXVII mixed tag in 2011, the No. 30 spot in the first women's Royal Rumble in "
        "2018, the Evolution tag with Lita at WWE's first all-women pay-per-view, a hometown "
        "SummerSlam singles match against Charlotte Flair in 2019, and the 2023 run against Becky "
        "Lynch that gave her a first-ever steel cage match at 47. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">49</span>'
        '<span class="pull-cap">her age challenging Tiffany Stratton for the WWE Women&rsquo;s Championship at Evolution 2025 &mdash; her most recent match</span></span>'
        "Her 25th-anniversary year, 2025, was practically a farewell tour that refused to announce "
        "itself: the Royal Rumble at No. 25, an Elimination Chamber tag win in Toronto alongside "
        "Tiffany Stratton, and then the Evolution title match against the same Stratton that "
        "July, which she lost cleanly. Since then: a stated desire for &ldquo;a bit of a finale "
        "moment&rdquo; (Sports Illustrated, March 2026), delayed in part by her mother's illness "
        "and passing; WrestleMania 42 week festivities in Las Vegas; and a June 2026 social-media "
        "tease about &ldquo;dusting off this ring rust&rdquo; ahead of WWE's European tour that, as "
        "of August 31, 2026, led nowhere. No match is booked. The closure she keeps talking about "
        "is still out there.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Highlight set",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("7&times;", "Women's titles"),
            ("448",      "Day sixth reign"),
            ("1",        "Hardcore title"),
            ("2013",     "Hall of Fame"),
            ("3&times;", "Babe of the Year"),
            ("2025",     "Most recent match"),
        ],
        lead=("Seventeen documented bouts spanning twenty-four years &mdash; a highlight subset, not "
              "a career count, and no career win&ndash;loss total is published because none was "
              "verified. The 2000&ndash;06 rows are the spine of the original run; everything after "
              "2011 is a return, which is itself the story: no women's wrestler of her generation "
              "has come back this often, this credibly, for this long. Filter by match type, tap "
              "any column header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("Four bouts the reputation rests on. The ratings are this dossier's own "
                    "editorial grades, not Wrestling Observer figures &mdash; no Meltzer ratings "
                    "were verified in this pass and none are quoted."),
    signature=[
        dict(rating="4.0", event="Raw, December 6, 2004", opponent="Lita",
             stip="The first women's main event in Raw history — WWE Women's Championship"),
        dict(rating="4.0", event="WrestleMania 22", opponent="Mickie James",
             stip="The obsessed-fan payoff — WWE Women's Championship"),
        dict(rating="3.5", event="Unforgiven 2006", opponent="Lita",
             stip="Retirement match, Toronto — wins the title with the Sharpshooter and leaves"),
        dict(rating="3.5", event="Evolution 2025", opponent="Tiffany Stratton",
             stip="WWE Women's Championship challenge at 49 — Stratus vs. Stratton, finally"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("7&times;", "Women's title reigns"),
            ("448",      "Longest reign (days)"),
            ("1",        "Hardcore title"),
            ("2013",     "Hall of Fame"),
        ],
        lead=("Seven reigns with one championship, which is the cleanest version of a record like "
              "this that exists: no renamed lineages, no counting disputes — one belt, seven "
              "times, in five years."),
        rows=[
            dict(ic="W", name="WWF/WWE Women's Championship", count="7",
                 sub="2001, won in the Survivor Series six-pack challenge on November 18 &mdash; "
                     "lost to Jazz in February 2002 &middot; 2002, regained May 12 &mdash; lost to "
                     "Molly Holly at King of the Ring &middot; 2002, regained at Unforgiven "
                     "September 22 &mdash; lost to Victoria at Survivor Series &middot; 2003, won "
                     "the WrestleMania XIX triple threat over Victoria and Jazz on March 30 "
                     "&mdash; lost to Jazz at Backlash &middot; 2004, won the Bad Blood four-way "
                     "on June 13 &mdash; lost to Lita in the December 6 Raw main event &middot; "
                     "2005&ndash;06, regained at New Year's Revolution on January 9 &mdash; "
                     "<b>448 days</b>, lost to Mickie James at WrestleMania 22 &middot; 2006, won "
                     "her retirement match against Lita at Unforgiven on September 17 and left as "
                     "champion; the title was subsequently vacated"),
            dict(ic="H", name="WWE Hardcore Championship", count="1",
                 sub="May 6, 2002 &middot; pinned Crash Holly under the 24/7 rule and lost it back "
                     "to Steven Richards &mdash; a one-day footnote she has joked about ever "
                     "since"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="She mostly worked alone, which was the point &mdash; but three alliances shaped the "
             "arc.",
        cards=[
            dict(era="WWF &middot; 2000&ndash;01",
                 name="T&A",
                 members="Test, Albert; Trish Stratus as manager",
                 desc="The entry point: a fitness model managing two mid-card powerhouses, feuding "
                      "with the Hardys and Lita. It is remembered mainly for starting both halves "
                      "of the Trish-Lita rivalry, the most important professional relationship "
                      "either woman had."),
            dict(era="WWE &middot; 2018&ndash;2023",
                 name="Team Bestie",
                 members="Trish Stratus, Lita",
                 desc="The late-career alliance, formalised at Evolution 2018 and revived through "
                      "the 2023 run alongside Becky Lynch — including the WrestleMania 39 "
                      "six-woman win over Damage CTRL. It ended in kayfabe when Trish turned on "
                      "Becky in 2023; off-screen the two remain each other's Hall of Fame "
                      "inductors and podcast co-guests."),
            dict(era="WWE &middot; 2023",
                 name="Trish & Zoey Stark",
                 members="Trish Stratus, Zoey Stark",
                 desc="The heel finale of the 2023 run: Stark as enforcer-protege through the "
                      "Becky Lynch feud, including the Night of Champions assist. The mentorship "
                      "framing — the legend manufacturing a successor — was the last fully new "
                      "story Trish has told in a WWE ring."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One name throughout &mdash; the person underneath it changed three times.",
        cards=[
            dict(mono="FM", era="Pre-WWF &middot; 1998&ndash;2000", name="The fitness model",
                 desc="Muscle magazine covers and a kinesiology-minded gym rat from Toronto, "
                      "signed off a Sully's Gym recommendation in November 1999. WWE hired a "
                      "look; it accidentally hired a worker."),
            dict(mono="VA", era="WWF &middot; 2000&ndash;01", name="The valet years",
                 desc="T&A's manager, the Mr. McMahon storyline, and the segments the company "
                      "later apologised for by pushing her. The 2001 pivot — training seriously, "
                      "taking the division seriously — is the hinge of the whole career."),
            dict(mono="CH", era="WWE &middot; 2001&ndash;06", name="The champion",
                 desc="Seven title reigns, the Chick Kick and Stratusfaction, the Lita and Mickie "
                      "James rivalries, and the retirement executed on her own terms: winning the "
                      "belt in her hometown and handing the division to the next era. The "
                      "2004-05 heel run — vain, vicious, brilliant — is widely her best work."),
            dict(mono="LG", era="WWE &middot; 2011&ndash;present", name="The legend who keeps lacing up",
                 desc="Hall of Fame 2013, and a return in every era since: the first women's "
                      "Rumble, Evolution, SummerSlam 2019, the 2023 Becky Lynch heel run at 47, "
                      "and the Evolution 2025 title challenge at 49. She calls the missing piece "
                      "a \"finale moment\"; it has not happened yet."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Ringside prop to retired-as-champion in six years &mdash; then twenty years of "
             "encores.",
        rows=[
            dict(year="2000", title="Debuts as T&A's manager",
                 desc="First appearance March 19, 2000 on Sunday Night Heat, after signing in "
                      "November 1999 and training under Ron Hutchison at Sully's Gym in Toronto."),
            dict(year="2001", title="First championship",
                 desc="Wins the vacant WWF Women's Championship in the Survivor Series six-pack "
                      "challenge on November 18 — the first of seven."),
            dict(year="2003", title="WrestleMania XIX",
                 desc="Beats Victoria and Jazz in the triple threat on March 30 — her only "
                      "WrestleMania title win, in the year of her third Babe of the Year award "
                      "and the Diva of the Decade designation."),
            dict(year="2004", title="The heel turn and the Raw main event",
                 desc="Turns on Chris Jericho at WrestleMania XX, rules the division as a heel, "
                      "and drops the title to Lita on December 6 in the first women's match to "
                      "main event Raw."),
            dict(year="2005", title="The 448 days begin",
                 desc="Regains the title from Lita at New Year's Revolution on January 9 and "
                      "holds it through the entire year — the longest women's world title reign "
                      "of the 21st century, per Wikipedia's accounting."),
            dict(year="2006", title="Retires as champion",
                 desc="Loses the belt to Mickie James at WrestleMania 22, then wins her "
                      "retirement match against Lita at Unforgiven in Toronto on September 17, "
                      "taking the title with the Sharpshooter and vacating it by leaving."),
            dict(year="2013", title="Hall of Fame",
                 desc="Inducted by Stephanie McMahon — at the time the youngest inductee in the "
                      "Hall's history."),
            dict(year="2018", title="The Rumble and Evolution",
                 desc="Enters the first women's Royal Rumble at No. 30 on January 28, then teams "
                      "with Lita to win at Evolution, WWE's first all-women pay-per-view, on "
                      "October 28."),
            dict(year="2019", title="SummerSlam in Toronto",
                 desc="Loses to Charlotte Flair on August 11 in a hometown match billed as her "
                      "last. It wasn't."),
            dict(year="2023", title="The Becky Lynch trilogy at 47",
                 desc="Wins the WrestleMania 39 six-woman with Becky Lynch and Lita, turns heel, "
                      "beats Lynch at Night of Champions with Zoey Stark's help, and loses the "
                      "steel cage blowoff at Payback — her first cage match ever."),
            dict(year="2025", title="The silver-anniversary run",
                 desc="Royal Rumble at No. 25, an Elimination Chamber tag win with Tiffany "
                      "Stratton in Toronto on March 1, and the Evolution title challenge against "
                      "Stratton on July 13 — her most recent match, at 49."),
            dict(year="2026", title="The tease",
                 desc="Tells Sports Illustrated in March she wants a \"finale moment,\" delayed "
                      "by her mother's illness and passing; appears at WrestleMania 42 week; and "
                      "in June publicly flirts with WWE's European tour — \"why do I suddenly "
                      "feel like dusting off this ring rust?\" — without wrestling on it."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who she went to war with.",
        cards=[
            dict(name="Lita", slug="lita",
                 desc="The defining rivalry of the era and arguably of women's wrestling's "
                      "pre-revolution history: valet-era brawls in 2000, the first women's Raw "
                      "main event on December 6, 2004 — which Lita won — the New Year's "
                      "Revolution rematch, and the Unforgiven 2006 retirement match Trish won in "
                      "Toronto. Then the second act: partners at Evolution 2018 and WrestleMania "
                      "39, and Hall of Fame inductor for her in 2014. Opponent, foil, best "
                      "friend — in that order."),
            dict(name="Mickie James",
                 desc="The obsessed-superfan storyline of 2005-06, the best long-form character "
                      "work of the division's first golden age, peaking with James taking the "
                      "title at WrestleMania 22 and ending Trish's 448-day reign. They ran it "
                      "back once more at Evolution 2018, on opposite sides of the tag."),
            dict(name="Becky Lynch", slug="becky-lynch",
                 desc="The 2023 return feud — Legend vs. The Man — built on Trish turning heel "
                      "against the woman who grew up on her matches. She beat Lynch at Night of "
                      "Champions with Zoey Stark's interference and lost the Payback steel cage "
                      "match, taking her first-ever cage bump at 47. It is the modern era's "
                      "proof that she never became a nostalgia act: she worked it as a full-time "
                      "heel."),
            dict(name="Victoria & Jazz",
                 desc="The all-wrestler wing of the early-2000s division: Jazz took her first "
                      "title, Victoria took her third, and the WrestleMania XIX triple threat "
                      "against both is her signature championship win. These were the feuds that "
                      "established the belt as a wrestling prize rather than a prop."),
            dict(name="Tiffany Stratton",
                 desc="The generational rhyme — Stratus vs. Stratton, a pairing the names alone "
                      "demanded. Partners at Elimination Chamber 2025 in Toronto, then champion "
                      "and challenger at Evolution on July 13, 2025, where Stratton retained "
                      "the WWE Women's Championship cleanly. If the \"finale moment\" ever "
                      "happens, this thread is the obvious one to pull."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Business",
        lead="The rare wrestling crossover who built her second act on wellness rather than "
             "Hollywood.",
        rows=[
            dict(when="2008&ndash;", title="Stratusphere", kind="Business",
                 desc="Her yoga and fitness brand, anchored by the Stratusphere Yoga studio she "
                      "opened in the Toronto area in 2008 — the longest-running business venture "
                      "of any woman from her wrestling generation."),
            dict(when="2011&ndash;19", title="Film and television", kind="Screen",
                 desc="Canadian film and TV work including the action film Bounty Hunters "
                      "(2011) and a run of hosting and reality appearances in Canada. No "
                      "current scripted project is verified, so none is listed."),
            dict(when="2013&ndash;", title="WWE legend programming", kind="TV",
                 desc="Hall of Fame 2013, recurring documentary and countdown appearances, and "
                      "a regular presence in WWE's anniversary programming — most recently "
                      "around her own 25th anniversary in 2025 and the \"everyone's first "
                      "crush\" signing tour that followed."),
            dict(when="2016&ndash;", title="WWE 2K", kind="Game",
                 desc="A playable legend across the modern WWE 2K series, including WWE 2K26."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, with the counting rules that make them true.",
        stats=[
            ("7",   "Women's title reigns"),
            ("448", "Day reign, 2005-06"),
            ("30",  "Rumble entry number, 2018"),
        ],
        rows=[
            dict(name="Seven WWF/WWE Women's Championship reigns — the record for that title",
                 sub="November 18, 2001 to September 17, 2006. The record is specific to the "
                     "original Women's Championship lineage, retired in 2010; modern multi-"
                     "lineage counts (Becky Lynch's seven, Charlotte Flair's more) are a "
                     "different measurement, not a broken record."),
            dict(name="A 448-day reign — the longest women's world title reign of the 21st century",
                 sub="January 9, 2005 to April 2, 2006, per Wikipedia's accounting. The claim "
                     "survives Bianca Belair's 420 and Becky Lynch's 398-399; it excludes "
                     "Asuka's 510-day NXT reign only because WWE does not class the NXT Women's "
                     "Championship as a world title."),
            dict(name="Retired as champion, in her hometown, in her retirement match",
                 sub="Unforgiven, September 17, 2006, beating Lita with the Sharpshooter in "
                     "Toronto. Almost no one in wrestling history has been given — or earned — "
                     "that exact exit."),
            dict(name="First women's main event in Raw history",
                 sub="December 6, 2004, against Lita, with the Women's Championship on the line. "
                     "She lost it, which the milestone retellings often skip — the night "
                     "belonged to both women."),
            dict(name="No. 30 in the first women's Royal Rumble",
                 sub="January 28, 2018 — the anchor-leg spot in the most stacked surprise-entrant "
                     "field the women's division has had, with three eliminations."),
            dict(name="Hall of Fame, 2013 — then the youngest inductee ever",
                 sub="Inducted by Stephanie McMahon at 37, seven years after retiring."),
            dict(name="Babe of the Year three times, Diva of the Decade, and PWI Woman of the Year four times",
                 sub="WWE's own awards 2001-03 plus the 2003 Diva of the Decade designation; Pro "
                     "Wrestling Illustrated's Woman of the Year in 2002, 2003, 2005 and 2006."),
            dict(name="A championship match in her fifth decade",
                 sub="Evolution, July 13, 2025: a clean, competitive WWE Women's Championship "
                     "challenge against Tiffany Stratton at 49, twenty-five years after her "
                     "debut. Whatever the \"finale moment\" turns out to be, the bar for it is "
                     "already set."),
        ],
        footnote=("No career win-loss total appears anywhere on this page; none was verified. Her "
                  "height is a live conflict — WWE.com says 5'5\", most independent listings say "
                  "5'4\" — and both are printed in the tape rather than resolved."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="X / Twitter", v="@trishstratuscom", href="https://x.com/trishstratuscom"),
        dict(k="Instagram", v="@trishstratuscom", href="https://www.instagram.com/trishstratuscom/"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Trish_Stratus"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/trish-stratus"),
        dict(k="WWE.com", v="Evolution 2025 — Stratton vs. Stratus",
             href="https://www.wwe.com/shows/wweevolution/2025/tiffany-stratton-trish-stratus"),
        dict(k="Sports Illustrated", v="On the 25th anniversary and a \"finale moment\"",
             href="https://www.si.com/fannation/wrestling/wwe/trish-stratus-discusses-a-potential-return-to-wwe-following-25-year-anniversary"),
        dict(k="ClutchPoints", v="The 2026 European tour tease",
             href="https://clutchpoints.com/wwe/wwe-news-is-trish-stratus-teasing-return-2026-european-tour"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/trish-stratus.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Trish Stratus still wrestling?",
            a="Not actively, and nothing is booked. Her most recent match was the WWE Women's "
              "Championship challenge against Tiffany Stratton at Evolution on <b>July 13, "
              "2025</b>, at 49, which she lost. Since then she has told Sports Illustrated she "
              "wants &ldquo;a bit of a finale moment&rdquo; &mdash; plans she said were "
              "disrupted by her mother's illness and passing &mdash; appeared during "
              "WrestleMania 42 week in Las Vegas, and in June 2026 publicly teased WWE's "
              "European tour (&ldquo;why do I suddenly feel like dusting off this ring "
              "rust?&rdquo;) without wrestling on it. As of August 31, 2026 there is no "
              "announced match.",
            q_ld="Is Trish Stratus still wrestling in 2026?",
            a_ld="Trish Stratus is not actively wrestling as of August 31, 2026. Her most recent "
                 "match was a WWE Women's Championship challenge against Tiffany Stratton at "
                 "Evolution on July 13, 2025, which she lost at age 49. She has said she wants "
                 "a finale moment to close her career, and in June 2026 she teased a return "
                 "around WWE's European tour on social media, but no match has been announced."),
        dict(
            q="Does Trish Stratus hold the record for most WWE Women's Championship reigns?",
            a="For the original title, yes: <b>seven reigns</b> with the WWF/WWE Women's "
              "Championship between 2001 and 2006, the most in that championship's history "
              "before it was retired in 2010. The claim needs its boundary: Becky Lynch also "
              "has seven world title reigns across the two modern renamed lineages, and "
              "Charlotte Flair has more across several. Nobody has broken Trish's record, "
              "because nobody can &mdash; the title it applies to no longer exists. Different "
              "belts, different ledgers.",
            q_ld="Does Trish Stratus hold the record for most WWE Women's Championship reigns?",
            a_ld="Trish Stratus holds the record for the original WWF/WWE Women's Championship "
                 "with seven reigns between 2001 and 2006, the most in that title's history "
                 "before it was retired in 2010. Modern wrestlers such as Becky Lynch and "
                 "Charlotte Flair have comparable or higher world title reign counts, but "
                 "those are in different, renamed championship lineages, so Trish's record "
                 "stands unbroken for the title it applies to."),
        dict(
            q="Was Trish Stratus's 448-day reign really the longest of the modern era?",
            a="Wikipedia states it as <b>the longest reign of any women's world champion in the "
              "21st century</b>: January 9, 2005 to April 2, 2006, ended by Mickie James at "
              "WrestleMania 22. The counting rules matter. Bianca Belair's 420 days and Becky "
              "Lynch's 398&ndash;399 fall short of it; Asuka's 510-day NXT Women's Championship "
              "reign exceeds it in days but is excluded because WWE does not class the NXT "
              "title as a world championship. State the claim with that asterisk and it "
              "holds.",
            q_ld="Was Trish Stratus's 448-day title reign the longest women's reign of the modern era?",
            a_ld="Trish Stratus held the WWE Women's Championship for 448 days from January 9, "
                 "2005 to April 2, 2006, which Wikipedia describes as the longest reign of any "
                 "women's world champion in the 21st century. Bianca Belair's 420-day and "
                 "Becky Lynch's 398-day reigns fall short of it, while Asuka's 510-day NXT "
                 "Women's Championship reign is longer in days but is not counted as a world "
                 "championship reign by WWE."),
        dict(
            q="Did Trish Stratus really retire as champion?",
            a="Yes &mdash; the cleanest exit in the division's history. She beat Lita at "
              "Unforgiven on <b>September 17, 2006</b> in Toronto, her hometown, in her "
              "announced retirement match, winning her seventh WWE Women's Championship with "
              "the Sharpshooter &mdash; a one-night tribute to fellow Canadian Bret Hart. She "
              "left with the belt, which was subsequently vacated. Her later matches &mdash; "
              "2011, 2018, 2019, 2023, 2025 &mdash; are returns, not a resumption: she has "
              "never come back full-time.",
            q_ld="Did Trish Stratus retire as WWE Women's Champion?",
            a_ld="Yes. Trish Stratus won her seventh WWE Women's Championship in her retirement "
                 "match, defeating Lita at Unforgiven on September 17, 2006 in her hometown of "
                 "Toronto, using the Sharpshooter. She retired as champion and the title was "
                 "subsequently vacated. Her matches since — in 2011, 2018, 2019, 2023 and 2025 "
                 "— have been one-off returns rather than a full-time comeback."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Patricia Anne Stratigeas",
             sub="Patricia Fisico since her 2006 marriage"),
        dict(label="Born", value="December 18, 1975", sub="Toronto, Ontario, Canada &middot; age 50"),
        dict(label="Billed from", value="Toronto, Ontario, Canada"),
        dict(label="Height", value="5&#8242;4&#8243;",
             sub="163 cm &middot; WWE.com lists 5&#8242;5&#8243; &mdash; a standing conflict"),
        dict(label="Weight", value="125 lb", sub="57 kg &middot; as historically billed"),
        dict(label="Debut", value="March 19, 2000", sub="Sunday Night Heat, as T&A's valet"),
        dict(label="Signed", value="November 1999",
             sub="trained by Ron Hutchison at Sully's Gym, Toronto"),
        dict(label="Retired", value="September 17, 2006", sub="as champion &mdash; returns since"),
        dict(label="Last match", value="July 13, 2025",
             sub="L to Tiffany Stratton, Evolution, WWE Women's Championship"),
        dict(label="Finishers", value="Stratusfaction &middot; Chick Kick",
             sub="plus the Sharpshooter, borrowed for the retirement match"),
        dict(label="Hall of Fame", value="Class of 2013", sub="inducted by Stephanie McMahon"),
        dict(label="Also known as",
             value="The Diva of the Decade &middot; 100% Stratusfaction Guaranteed"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1975-12-18",
    bornplace="Toronto, Ontario, Canada",
    nationality="Canada",
    height_cm=163,
    weight_kg=57,
    ld=dict(
        alternateName=["Patricia Anne Stratigeas", "Patricia Fisico", "The Diva of the Decade"],
        award=["WWF/WWE Women's Championship (7 reigns, the record for that title, 2001-2006)",
               "WWE Hardcore Championship (1 reign, 2002)",
               "WWE Hall of Fame (Class of 2013)",
               "WWE Babe of the Year (2001, 2002, 2003)",
               "WWE Diva of the Decade (2003)",
               "Pro Wrestling Illustrated Woman of the Year (2002, 2003, 2005, 2006)",
               "448-day WWE Women's Championship reign (2005-2006)"],
        knowsAbout=["Professional wrestling", "WWE", "Women's professional wrestling",
                    "Fitness", "Yoga", "Championship wrestling"],
        description="Trish Stratus is a Canadian professional wrestler, a record seven-time "
                    "WWF/WWE Women's Champion and a 2013 WWE Hall of Famer. Debuting in 2000 as "
                    "a fitness model turned valet, she became the defining women's wrestler of "
                    "her era, holding the Women's Championship for 448 days in 2005-06 and "
                    "retiring as champion in her hometown of Toronto at Unforgiven 2006. She has "
                    "returned across every era since, most recently challenging Tiffany Stratton "
                    "for the WWE Women's Championship at Evolution on July 13, 2025 at age 49.",
        sameAs=["https://x.com/trishstratuscom",
                "https://www.instagram.com/trishstratuscom/",
                "https://en.wikipedia.org/wiki/Trish_Stratus",
                "https://www.wwe.com/superstars/trish-stratus"],
    ),
)
