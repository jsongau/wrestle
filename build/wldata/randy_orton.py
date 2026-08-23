# -*- coding: utf-8 -*-
"""Randy Orton - dossier data.

Source: /tmp/research/randy-orton.md (web-verified, compiled Aug 23 2026). There is
no previous /wrestlers/randy-orton/ page to harvest, so every row below comes from
the research file and nothing is carried over from an older ledger.

Deliberate omissions, each for a stated reason:
  * No Instagram link. instagram.com/randyorton and instagram.com/official_randyorton
    both surface as apparently legitimate; the research pass could not establish which
    is official, so neither is published and the handle is absent from sameAs.
  * No WrestleMania headliner count. Wikipedia says three, but that figure predates
    WrestleMania 42, which he headlined on April 18, 2026. Four is likely and no
    source states it, so no number is asserted.
  * No signature-match ratings. No star-rating source for any Orton match could be
    verified in this pass, so the section carries the explanation instead of numbers.
  * No career win-loss total, and no tag-title day counts from WrestleIndex, which
    totals him at 17 reigns while omitting both RK-Bro reigns and the SmackDown Tag
    Team reign. It is used here only for world-title dates and day counts.
"""

# ----------------------------------------------------------------- record rows
# Ten bouts. Every one has a day-precise date AND a named opponent in the research
# file. Reigns whose deciding opponent is not named in a verified source are carried
# in Championships instead of guessed at here.
ROWS = [
    dict(result="W", date="2004-08-15", promo="WWE", landmark=True,
         event="SummerSlam", opponent="Chris Benoit",
         stip="Singles — world champion at 24, the youngest in WWE history",
         title="World Heavyweight Championship"),
    dict(result="L", date="2004-09-12", promo="WWE", landmark=True,
         event="Unforgiven", opponent="Triple H", opponent_html=True,
         stip="Singles — ends the 28-day reign, a month after Evolution ejected him",
         title="World Heavyweight Championship"),
    dict(result="W", date="2007-10-07", promo="WWE", landmark=True,
         event="No Mercy", opponent="No match — the vacant title was awarded by Vince McMahon",
         stip="Awarded, then lost the same night — WWE counts this as a reign of under a day",
         title="WWE Championship"),
    dict(result="L", date="2007-10-07", promo="WWE",
         event="No Mercy", opponent="Triple H", opponent_html=True,
         stip="Impromptu singles, the same night he was awarded the belt",
         title="WWE Championship"),
    dict(result="W", date="2007-10-07", promo="WWE", landmark=True,
         event="No Mercy", opponent="Triple H", opponent_html=True,
         stip="Last Man Standing — the second counted reign of one calendar date; 203 days",
         title="WWE Championship"),
    dict(result="W", date="2013-08-18", promo="WWE", landmark=True,
         event="SummerSlam", opponent="Daniel Bryan",
         stip="Money in the Bank cash-in, moments after Triple H attacked Bryan",
         title="WWE Championship"),
    dict(result="W", date="2013-12-15", promo="WWE", landmark=True,
         event="TLC", opponent="John Cena", opponent_html=True,
         stip="TLC match — unifies the two world titles and retires the World Heavyweight Championship",
         title="WWE & World Heavyweight Championships"),
    dict(result="L", date="2014-04-06", promo="WWE", type="tag",
         event="WrestleMania XXX", opponent="Daniel Bryan & Batista",
         stip="Triple threat — Bryan wins the title; ends a 161-day reign",
         title="WWE World Heavyweight Championship"),
    dict(result="W", date="2017-04-02", promo="WWE", landmark=True,
         event="WrestleMania 33", opponent="Bray Wyatt",
         stip="Singles — a 49-day reign, his ninth WWE Championship",
         title="WWE Championship"),
    dict(result="L", date="2026-04-18", promo="WWE", landmark=True,
         event="WrestleMania 42 Night 1", opponent="Cody Rhodes", opponent_html=True,
         stip="Singles — Pat McAfee as guest referee; Orton punts Rhodes after the bell",
         title="Undisputed WWE Championship"),
]

for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Triple H": "triple-h", "John Cena": "john-cena", "Cody Rhodes": "cody-rhodes"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="randy-orton",
    name="Randy Orton",
    realname="Randy Orton",
    epithet="The Viper",
    hook="Record & Titles",

    meta_desc=("Randy Orton, The Viper, is a 14-time world champion — 10 WWE Championship reigns plus 4 "
               "World Heavyweight Championship reigns — and the youngest world champion in WWE history at "
               "24. Full record, titles, stables, records and the 13/14/15 count explained."),
    og_desc=("The Viper: 14 world titles counted the way WWE and Wikipedia both count them, the youngest "
             "world champion in WWE history at 24, two Royal Rumbles, Evolution to the Legacy to 2026."),
    tw_desc=("The Viper: 14 world titles, the youngest world champion in WWE history at 24, and the "
             "13/14/15 counting dispute settled."),

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2000",
    height_imp="6&#8242;5&#8243;",
    weight_lb="275",
    world_titles="14",
    vitals_tagline="Apex Predator",
    support_note="Merch &middot; Games &middot; Data",
    x_url="https://x.com/RandyOrton",
    # ig_url deliberately omitted - the official handle is unresolved. See docstring.
    sp_items=[
        dict(ic="RO", title="Viper Merch", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="In the series across effectively his whole career",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="WI", title="WrestleIndex", sub="Per-reign dates and day counts",
             tag="Data", href="https://wrestleindex.com/wwe/randy-orton/"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/randy-orton"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Legend Killer &middot; The Viper &middot; The Apex Predator",
    hero_tag="Third generation, St. Louis &middot; <em>MMWA&ndash;SICW &middot; WWE &middot; "
             "2000&ndash;present</em>",
    now_label="NOW",
    now_bold="Active heel on SmackDown, no championship",
    now_tail=" &middot; back from a post-WrestleMania absence to cost Cody Rhodes the Undisputed WWE "
             "Championship at SummerSlam, and booked against him at Sunday Night&rsquo;s Main Event on "
             "September 6 in Atlanta",
    hstats=[
        dict(value="14",  x=True,  label="World Titles"),
        dict(value="24",  x=False, label="Age at First World Title"),
        dict(value="2",   x=True,  label="Royal Rumble Wins"),
        dict(value="210", x=False, label="Day IC Reign"),
    ],
    ghost_link="From Evolution’s rookie to a fourteenth world title",
    vlabel="Est. 2000 &middot; St. Louis, MO",
    mono="RO",

    # ---------------------------------------------------------------- 01 overview
    # index into overview of the correction paragraph -> the framed
    # "Setting one thing straight" callout (aside.corr) on the page
    correction=1,
    overview=[
        "<b>Randy Orton</b> is the wrestler whose significance is measurable rather than rhetorical. He "
        "holds fourteen world championships across the WWE Championship and World Heavyweight "
        "Championship lineages, a total behind only John Cena&rsquo;s seventeen and Ric Flair&rsquo;s "
        "sixteen and level with Triple H. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">14</span>'
        '<span class="pull-cap">world championships &mdash; behind only John Cena&rsquo;s 17 and Ric Flair&rsquo;s 16</span></span>'
        "He won the first of them at 24, which is still the youngest in "
        "WWE history, and he was still headlining WrestleMania twenty-two years later &mdash; Night 1 of "
        "WrestleMania 42 in April 2026. He has more pay-per-view matches than any other male wrestler in "
        "WWE, a record of durability rather than of any single peak, and the RKO is one of the very few "
        "wrestling moves with recognition outside the wrestling audience.",

        "The number is where the record gets mangled, and the &ldquo;13 / 14 / 15&rdquo; spread has three "
        "different causes of which only one is a real dispute. The count is <b>14</b>: WWE.com and "
        "Wikipedia state it independently and break it down identically, <b>10 WWE Championship reigns "
        "plus 4 World Heavyweight Championship reigns</b>. The <b>15</b> is not a count at all &mdash; it "
        "is the title he is chasing, written into the storyline. Every traceable &ldquo;15&rdquo; headline "
        "is prospective, and on the August 21, 2026 SmackDown he said on camera that he is going to "
        "&ldquo;get number 15.&rdquo; The <b>13</b> is legitimate: at TLC on December 15, 2013 he beat "
        "John Cena to unify the titles, and WWE counts the World Heavyweight half of that as a separate "
        "fourth reign lasting <b>about one minute</b> before he retired the belt in the same match. "
        "TheSportster says it outright &mdash; &ldquo;for some reason, WWE decided to count this title "
        "reign.&rdquo; Drop it and you get 13. There is a second asterisk almost nobody raises: on "
        "<b>October 7, 2007</b> he was awarded the vacant WWE Championship by Vince McMahon, lost it to "
        "Triple H in an impromptu match the same night and won it back later that night in a Last Man "
        "Standing match &mdash; <b>two counted reigns on one calendar date</b>. Merge those and you also "
        "get 13, by a different route.",

        "The part usually gotten backwards is the lineage split, which causes none of this. The WWE "
        "Championship and the 2002&ndash;2013 World Heavyweight Championship were genuinely separate "
        "titles with separate lineages, so counting them separately is correct rather than "
        "double-counting. When they were unified on December 15, 2013 the belt was renamed the WWE World "
        "Heavyweight Championship but, per Wikipedia, <i>retained the lineage of the WWE Championship</i> "
        "&mdash; which is why his October 27, 2013 to April 6, 2014 reign spans the rename and counts "
        "once, not twice. The modern World Heavyweight Championship introduced in 2023 is a third, "
        "different title, and Orton has never held it. So: 14 is correct and officially supported, 13 is "
        "a reasoned minority position that refuses to count a one-minute ceremonial reign, and 15 is "
        "simply wrong.",

        '<span class="pull" aria-hidden="true"><span class="pull-fig pull-fig--sm">3RD&nbsp;GEN</span>'
        '<span class="pull-cap">grandfather Bob Orton Sr., father &ldquo;Cowboy&rdquo; Bob Orton Jr., uncle Barry Orton</span></span>'
        "He is third generation &mdash; grandfather Bob Orton Sr., father &ldquo;Cowboy&rdquo; Bob Orton "
        "Jr., uncle Barry Orton &mdash; and his father trained him, alongside the staff of the "
        "Mid-Missouri Wrestling Alliance&ndash;Southern Illinois Conference Wrestling promotion in St. "
        "Louis, where he debuted in 2000. He reached the WWE main roster in 2002 and the run that made him "
        "began in January 2003 with Evolution, the Triple H / Ric Flair / Batista group built explicitly "
        "as wrestling&rsquo;s past, present and future. By December 2003 Evolution held every major Raw "
        "championship, Orton&rsquo;s share being a 210-day Intercontinental Championship reign, then the "
        "longest in seven years. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">24</span>'
        '<span class="pull-cap">his age winning the World Heavyweight title at SummerSlam 2004 &mdash; still WWE&rsquo;s youngest world champion</span></span>'
        "He beat Chris Benoit for the World Heavyweight Championship at SummerSlam "
        "on August 15, 2004 and was ejected from the group the next night. What followed was thirteen more "
        "world titles, two Royal Rumble wins in 2009 and 2017, a Money in the Bank cash-in at SummerSlam "
        "2013, and three more stables. As of August 2026 he is a part-time SmackDown heel who turned on "
        "Cody Rhodes in March, won the Elimination Chamber, lost the WrestleMania 42 main event and "
        "punted Rhodes afterward, then returned at SummerSlam on August 1 to hand CM Punk the win over "
        "him. He has not held a world title since November 16, 2020.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full ledger",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("14&times;", "World titles"),
            ("10&times;", "WWE Championship"),
            ("4&times;",  "World Heavyweight"),
            ("24",        "Age at first world title"),
            ("2&times;",  "Royal Rumble wins"),
            ("17th",      "Triple Crown"),
        ],
        lead=("Ten bouts &mdash; every one with both a day-precise date and a named opponent in the "
              "sources. This is a highlight subset, not a career count: no career win&ndash;loss total is "
              "published here because none was verified, and reigns whose deciding opponent is not named "
              "by a reliable source are carried in Championships below rather than guessed at in the "
              "table. Note the three rows dated October 7, 2007 &mdash; that one night is where two of his "
              "fourteen reigns come from. Filter by match type, tap any column header to sort, and turn "
              "spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("Intentionally empty. Every other section on this page cites a source; no star-rating "
                    "source &mdash; Meltzer, Cagematch or otherwise &mdash; could be verified for a single "
                    "Randy Orton match in the research pass behind this file, and inventing ratings for a "
                    "career this long would be the easiest and worst thing on the page. The matches that "
                    "actually decided something are in The Record above, and the acclaim that <i>is</i> "
                    "documented &mdash; PWI Wrestler of the Year in 2009 and 2010, PWI Feud of the Year "
                    "2009, and a Wrestling Observer Worst Feud of the Year in 2017 &mdash; is in Records "
                    "&amp; Feats below."),
    signature=[],

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("14&times;",  "World title reigns"),
            ("10 &plus; 4", "WWE + World Heavyweight"),
            ("17th",       "Triple Crown"),
            ("18th",       "Grand Slam"),
        ],
        lead=("The arithmetic, in full: <b>10 WWE Championship reigns + 4 World Heavyweight Championship "
              "reigns = 14</b>. WWE.com and Wikipedia agree on every count below. Two of the fourteen are "
              "the asterisks that produce the &ldquo;13&rdquo; figure &mdash; a one-minute reign on "
              "December 15, 2013 and a doubled night on October 7, 2007 &mdash; and both are marked. "
              "Per-reign dates and day counts are WrestleIndex&rsquo;s, which is reliable for world titles "
              "and demonstrably incomplete on tag titles."),
        rows=[
            dict(ic="W", name="WWE Championship", count="10",
                 sub="Oct 7, 2007 &mdash; awarded by Vince McMahon at No Mercy, lost the same night, "
                     "<b>under a day</b> &middot; Oct 7, 2007&ndash;Apr 27, 2008 &mdash; won back from "
                     "Triple H in a Last Man Standing match the same night, 203 days &middot; "
                     "Apr 26&ndash;Jun 7, 2009, 42 days &middot; Jun 15&ndash;Sep 13, 2009, 90 days "
                     "&middot; Oct 4&ndash;25, 2009, 21 days &middot; Sep 19&ndash;Nov 22, 2010, 64 days "
                     "&middot; Aug 18&ndash;Sep 15, 2013, 28 days, the Money in the Bank cash-in &middot; "
                     "Oct 27, 2013&ndash;Apr 6, 2014, 161 days &mdash; this reign spans the December 15 "
                     "unification and the rename to WWE World Heavyweight Championship and counts "
                     "<b>once</b>, because the unified belt kept the WWE Championship lineage &middot; "
                     "Apr 2&ndash;May 21, 2017, 49 days &middot; Oct 25&ndash;Nov 16, 2020, 22 days "
                     "&mdash; his most recent world championship. WrestleIndex files the lineage under its "
                     "current name, Undisputed WWE Championship; TheSportster describes the 2020 reign as "
                     "running &ldquo;SummerSlam through Survivor Series,&rdquo; which is imprecise and is "
                     "flagged here as the weaker source."),
            dict(ic="H", name="World Heavyweight Championship (2002-2013)", count="4",
                 sub="Aug 15&ndash;Sep 12, 2004 &middot; def. Chris Benoit at SummerSlam at 24 years old "
                     "&mdash; the youngest world champion in WWE history &mdash; and lost it to Triple H "
                     "at Unforgiven, 28 days &middot; May 6&ndash;Jul 17, 2011, 72 days &middot; "
                     "Aug 14&ndash;Sep 18, 2011, 35 days &middot; Dec 15, 2013 &mdash; won from John Cena "
                     "at TLC and <b>retired in the same match</b> on unification, a reign of about one "
                     "minute that WWE counts and that TheSportster openly questions. It also makes him the "
                     "final World Heavyweight Champion of that lineage. The modern World Heavyweight "
                     "Championship introduced in 2023 is a different title and he has never held it."),
            dict(ic="I", name="WWE Intercontinental Championship", count="1",
                 sub="Dec 14, 2003&ndash;Jul 11, 2004 &middot; 210 days &mdash; the longest reign with "
                     "that title in seven years at the time, and Evolution&rsquo;s share of the December "
                     "2003 sweep of every major Raw championship"),
            dict(ic="S", name="WWE United States Championship", count="1",
                 sub="Mar 11&ndash;Apr 8, 2018 &middot; won at Fastlane, lost at WrestleMania 34 &middot; "
                     "28 days &middot; the reign that completed the Grand Slam"),
            dict(ic="R", name="Raw Tag Team Championship", count="2",
                 sub="2021&ndash;22 with Matt Riddle as RK-Bro &middot; Aug 21, 2021 (SummerSlam) to "
                     "Jan 10, 2022, 142 days &middot; Mar 7 to May 20, 2022, 74 days &middot; both reigns "
                     "are on WWE.com and Wikipedia and <b>both are missing from WrestleIndex</b>, which is "
                     "why its 17-reign total runs low"),
            dict(ic="T", name="World Tag Team Championship", count="1",
                 sub="Nov 13, 2006&ndash;Jan 29, 2007 &middot; with Edge, as Rated-RKO &middot; 77 days"),
            dict(ic="D", name="SmackDown Tag Team Championship", count="1",
                 sub="2017 &middot; with the Wyatt Family under the Freebird Rule &middot; exact dates and "
                     "reign length not verified, and also missing from WrestleIndex &mdash; listed because "
                     "WWE.com and Wikipedia both credit it"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Six groups in twenty-three years &mdash; two he was the future of, two he led, one that was "
             "a comedy act with 216 days of tag titles, and one he joined in order to betray.",
        cards=[
            dict(era="WWE &middot; 2003&ndash;05, reunions 2007 and 2014",
                 name="Evolution",
                 members="Triple H, Ric Flair, Randy Orton, Batista",
                 desc="Formed January 20, 2003 when Orton joined the other three in attacking Scott "
                      "Steiner, and conceived as wrestling's past (Flair), present (Triple H) and future "
                      "(Orton and Batista). By December 2003 the group held every major Raw championship, "
                      "Orton's share being the Intercontinental Championship. Across the run: five World "
                      "Heavyweight Championships (Triple H four, Orton one), two World Tag Team "
                      "Championships, one Intercontinental Championship and Batista's 2005 Royal Rumble "
                      "win. Orton was ejected on August 16, 2004, the night after winning the world title "
                      "at SummerSlam, for refusing Triple H's demand to hand over the belt and spitting in "
                      "his face; Triple H took the title back at Unforgiven on September 12."),
            dict(era="WWE &middot; 2008&ndash;10",
                 name="The Legacy",
                 members="Randy Orton, Cody Rhodes, Ted DiBiase Jr., briefly Manu and Sim Snuka",
                 desc="Orton's own group, organised around multigenerational lineage — Orton with a "
                      "father, uncle and grandfather in the business, DiBiase with Ted DiBiase Sr., Rhodes "
                      "with Dusty Rhodes. Rhodes and DiBiase had first teamed as Priceless in June 2008. "
                      "The stable underwrote Orton's dominant 2009: the Royal Rumble win and three "
                      "separate WWE Championship reigns, plus two World Tag Team Championships for Rhodes "
                      "and DiBiase. It fractured when Rhodes and DiBiase turned on each other in the "
                      "WrestleMania XXVI triple threat against Orton, and the 2010 draft split them across "
                      "brands."),
            dict(era="WWE &middot; 2013&ndash;16, brief 2018 reunion",
                 name="The Authority",
                 members="Triple H, Stephanie McMahon, Randy Orton, Seth Rollins, Kane and others",
                 desc="The on-screen power couple controlling WWE operations, with Orton as its hand-picked "
                      "WWE Champion and designated “Face of the WWE” from August 2013 to November 2014. He "
                      "became a founding member by cashing in Money in the Bank at SummerSlam 2013 "
                      "immediately after Triple H attacked Daniel Bryan. The group's function was "
                      "authority-figure interference in title matches and coercion of other wrestlers. "
                      "Orton left in February 2015 out of storyline frustration at Seth Rollins' rise, "
                      "refusing a tag from Rollins mid-match and later RKO-ing him."),
            dict(era="WWE &middot; April 2021 &ndash; September 2023",
                 name="RK-Bro",
                 members="Randy Orton, Matt Riddle",
                 desc="Formed April 19, 2021 when Riddle interrupted an Orton backstage interview to "
                      "propose the team. A comedy-inflected odd-couple act that was also genuinely "
                      "successful: two Raw Tag Team Championship reigns totalling 216 days, and a No. 6 "
                      "placing in PWI's 2022 Tag Team 100. The team effectively ended with Orton's May "
                      "2022 back injury, which kept him out for well over a year, and was formally "
                      "finished when Riddle was released by WWE in September 2023."),
            dict(era="WWE &middot; 2006&ndash;07",
                 name="Rated-RKO",
                 members="Randy Orton, Edge",
                 desc="A two-man heel alliance with one World Tag Team Championship reign, November 13, "
                      "2006 to January 29, 2007 — 77 days."),
            dict(era="WWE &middot; 2016&ndash;17",
                 name="The Wyatt Family",
                 members="Bray Wyatt, Luke Harper, Randy Orton",
                 desc="Orton aligned with Wyatt and Harper and held the SmackDown Tag Team Championship "
                      "with them under the Freebird Rule before turning on Wyatt. The feud that came out "
                      "of it ran through WrestleMania 33 and was voted Worst Feud of the Year for 2017 by "
                      "the Wrestling Observer Newsletter."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One wrestler, three characters, and a fourth that no source has bothered to name.",
        cards=[
            dict(mono="LK", era="WWE &middot; 2003&ndash;06", name="The Legend Killer",
                 desc="An arrogant young heel whose gimmick was attacking and disrespecting retired and "
                      "veteran wrestlers in order to establish himself. It ran through the Evolution years "
                      "and produced his first world title. Both TheSportster and GiveMeSport still argue "
                      "it is his best character."),
            dict(mono="VP", era="WWE &middot; 2008&ndash;13 core period", name="The Viper",
                 desc="The pivot that defined him. Where the Legend Killer was loud and cocky, the Viper "
                      "was slowed down, methodical and unstable — the deliberate stalking, the pre-RKO "
                      "mat-pound, the punt kick as a character-ending weapon. It anchored The Legacy and "
                      "the 2009 peak, and the name has outlived the era as a permanent nickname."),
            dict(mono="AP", era="WWE &middot; roughly 2013 onward", name="The Apex Predator",
                 desc="An evolution rather than a break: the Viper's psychology carried into main-event "
                      "and then elder-statesman status, through the Authority run and the 2020 return to a "
                      "punt-kick-driven, legacy-obsessed heel. WWE.com uses “The Viper” and “Apex "
                      "Predator” together as his current nicknames."),
            dict(mono="26", era="WWE &middot; March 2026 &ndash; present", name="The current heel run",
                 desc="TheSmackDownHotel dates the turn to March 2026, when he assaulted Cody Rhodes. The "
                      "stated motivation is a fifteenth world championship, and since SummerSlam 2026 he "
                      "has been working in concert with CM Punk against Rhodes. Whether this is a named "
                      "persona era or simply a heel turn inside the Apex Predator character is not "
                      "verified — no source gives it a name, so none is invented here."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="St. Louis to Evolution to a twenty-third year still in the main event.",
        rows=[
            dict(year="2000", title="Debuts in St. Louis",
                 desc="Trained by his father, Bob Orton Jr., he debuts for the Mid-Missouri Wrestling "
                      "Alliance–Southern Illinois Conference Wrestling. He is third generation: grandfather "
                      "Bob Orton Sr., father Bob Orton Jr., uncle Barry Orton. (Wikipedia)"),
            dict(year="2002", title="Reaches the WWE main roster",
                 desc="Signs with WWE and moves up in 2002. (Wikipedia)"),
            dict(year="2003", title="Joins Evolution",
                 desc="On January 20 he aligns with Triple H, Ric Flair and Batista, and in December takes "
                      "the Intercontinental Championship for a 210-day reign — the longest with that title "
                      "in seven years at the time. (Wikipedia)"),
            dict(year="2004", title="Youngest world champion in WWE history",
                 desc="Beats Chris Benoit at SummerSlam on August 15 for the World Heavyweight "
                      "Championship at 24, and is ejected from Evolution the following night for refusing "
                      "to hand the belt to Triple H. (Wikipedia, WWE.com)"),
            dict(year="2007", title="Wins the WWE Championship twice in one night",
                 desc="At No Mercy on October 7 he is awarded the vacant title by Vince McMahon, loses it "
                      "to Triple H in an impromptu match, then wins it back from Triple H in a Last Man "
                      "Standing match — the two reigns WWE counts separately. (WrestleIndex, WWE.com)"),
            dict(year="2009", title="Peak heel year with The Legacy",
                 desc="Wins the Royal Rumble and holds the WWE Championship three separate times while "
                      "leading Cody Rhodes and Ted DiBiase Jr. PWI names him Wrestler of the Year and his "
                      "programme with Triple H Feud of the Year. (Wikipedia)"),
            dict(year="2013", title="Cashes in, then unifies the world titles",
                 desc="Cashes Money in the Bank on Daniel Bryan at SummerSlam on August 18, then on "
                      "December 15 at TLC beats John Cena to unify the WWE and World Heavyweight "
                      "Championships — retiring the latter and becoming its final champion. (Wikipedia)"),
            dict(year="2017", title="Second Royal Rumble and a WrestleMania title win",
                 desc="Wins the Rumble, then beats Bray Wyatt at WrestleMania 33 on April 2 for a 49-day "
                      "WWE Championship reign. (WrestleIndex, Wikipedia)"),
            dict(year="2021", title="RK-Bro",
                 desc="Teams with Matt Riddle from April 19 and wins the Raw Tag Team Championship at "
                      "SummerSlam on August 21; a second reign follows in 2022 before a back injury ends "
                      "the act. (Wikipedia)"),
            dict(year="2026", title="Heel turn, Elimination Chamber win, WrestleMania main event",
                 desc="Turns on Cody Rhodes in March, wins the men's Elimination Chamber to earn the title "
                      "shot, and headlines WrestleMania 42 Night 1 on April 18 — losing to Rhodes in a "
                      "match refereed by Pat McAfee, then punting him after the bell. (Wrestling Inc., "
                      "ESPN, Fox News)"),
            dict(year="2026", title="SummerSlam return costs Rhodes the title",
                 desc="Returns on August 1 at SummerSlam Night 1 to RKO Rhodes with the referee down, "
                      "handing CM Punk the Undisputed WWE Championship win, and is booked against Rhodes "
                      "for Sunday Night's Main Event on September 6 in Atlanta. (Forbes, Bleacher Report, "
                      "Fightful)"),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with, including the one that won an award nobody wants.",
        cards=[
            dict(name="Triple H", slug="triple-h",
                 desc="Peaked twice. The first run began the night after SummerSlam 2004, when Evolution "
                      "ejected Orton and converted him into a babyface challenger, and ran through "
                      "Unforgiven on September 12, 2004, where Triple H took the World Heavyweight "
                      "Championship back. It mattered because it was the intended coronation of Orton as "
                      "the company's next top star and it visibly did not take — the stalled babyface run "
                      "is exactly what forced the rebuild into the Viper. The 2009 rematch cycle, built on "
                      "The Legacy attacking the McMahon family on screen, was named PWI Feud of the Year."),
            dict(name="John Cena", slug="john-cena",
                 desc="The defining main-event pairing of his prime, spanning No Mercy 2007 through the "
                      "TLC unification match on December 15, 2013. It mattered structurally rather than "
                      "emotionally: Cena was the immovable babyface and Orton the heel constant tested "
                      "against him for the better part of a decade, and the feud's endpoint is literally "
                      "the moment WWE collapsed two world championships into one."),
            dict(name="The Legacy",
                 desc="His own stable turned on him and he beat both of them in the WrestleMania XXVI "
                      "triple threat, where Cody Rhodes and Ted DiBiase Jr. also turned on each other. It "
                      "mattered because it completed his babyface turn without a character rewrite — the "
                      "Viper stayed the Viper and the audience simply moved."),
            dict(name="Bray Wyatt",
                 desc="Ran from Orton's infiltration of the Wyatt Family through WrestleMania 33, and is "
                      "here as a cautionary case: the Wrestling Observer Newsletter voted it Worst Feud of "
                      "the Year for 2017. A wrestler with Orton's record collecting that award is part of "
                      "the career record, not a footnote to be quietly dropped."),
            dict(name="Seth Rollins", slug="seth-rollins",
                 desc="Peaked at WrestleMania 31, after Orton walked out of The Authority in February 2015 "
                      "by refusing a tag from Rollins mid-match and then RKO-ing him. It mattered as the "
                      "cleanest use of Orton as a veteran gatekeeper validating a rising main-eventer, a "
                      "role he has occupied repeatedly since."),
            dict(name="Cody Rhodes", slug="cody-rhodes",
                 desc="The current and most consequential late-career feud. Orton turned heel on Rhodes in "
                      "March 2026, won the Elimination Chamber, and lost the WrestleMania 42 Night 1 main "
                      "event on April 18 with Pat McAfee as guest referee, punting Rhodes afterward. He "
                      "returned on August 1 at SummerSlam to cost Rhodes the Undisputed WWE Championship "
                      "against CM Punk. It works because it inverts The Legacy: Orton once led Rhodes as a "
                      "protégé and is now the obstacle to his championship run, with a fifteenth world "
                      "title as the stated aim."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Beyond the ring &mdash; a short section, because most of what circulates could not be "
             "verified.",
        rows=[
            dict(when="2013", title="12 Rounds 2: Reloaded", kind="Film",
                 desc="WWE Studios, directed by Roel Reiné, with Orton in the lead. Confirmed by WWE.com's "
                      "own studios page and by Wikipedia's article on the film — the only Orton film credit "
                      "verified to two sources in this pass."),
            dict(when="2011", title="That's What I Am", kind="Film",
                 desc="A WWE Studios release listed in general filmography coverage. His role and its "
                      "prominence are not verified — IMDb blocks automated fetching and no second source "
                      "could confirm the details, so nothing further is claimed. Other WWE Studios credits "
                      "reported by aggregators were likewise not verified."),
            dict(when="2002&ndash;", title="WWE television and mainstream press", kind="TV",
                 desc="Continuously on WWE programming since 2002 across Raw, SmackDown and NXT. A CBS "
                      "News New York segment, “WWE star Randy Orton on the couch,” is a documented "
                      "mainstream appearance. Broader scripted-television guest credits are not verified."),
            dict(when="Series", title="WWE SmackDown vs. Raw, WWE 2K", kind="Game",
                 desc="Featured in the WWE video game series across effectively his entire career. Specific "
                      "cover-athlete years were not verified to a reliable source and are not listed. No "
                      "autobiography is verified, and while WWE has produced career retrospective and DVD "
                      "content on him, no specific title, release date or standalone documentary feature "
                      "could be confirmed — treat as unverified rather than nonexistent."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated the way the sources actually state them &mdash; and the arithmetic "
             "behind the number people keep getting wrong.",
        stats=[
            ("14",  "World championships"),
            ("24",  "Age at his first"),
            ("210", "Day IC reign"),
        ],
        rows=[
            dict(name="14 world championships — 10 WWE Championship plus 4 World Heavyweight",
                 sub="WWE.com and Wikipedia state the figure independently and break it down identically. "
                     "It is the third-most in WWE history, behind John Cena's 17 and Ric Flair's 16 and "
                     "level with Triple H."),
            dict(name="The '15' is a target, not a count",
                 sub="Every traceable '15' headline is prospective — Sportskeeda's 'massive step towards "
                     "15th World Championship,' SI's and SEScoops' pieces on what a 15th would mean to "
                     "him — and WWE wrote it into the storyline: on the August 21, 2026 SmackDown he said "
                     "he is going to 'get number 15.' Aggregators are reading a title he is chasing as a "
                     "title he has. He has not won a world championship since November 16, 2020."),
            dict(name="The '13' is the one-minute reign on December 15, 2013",
                 sub="At TLC he beat John Cena in a match that unified the World Heavyweight Championship "
                     "with the WWE Championship, and WWE counts the World Heavyweight half as a separate "
                     "fourth reign that began and ended inside the same match — Wikipedia puts it at about "
                     "one minute, retired immediately upon winning. TheSportster: 'for some reason, WWE "
                     "decided to count this title reign for Orton.' Drop it and the total is 13, which is "
                     "a defensible objection to WWE's bookkeeping rather than an error."),
            dict(name="The second asterisk: two counted reigns on one night, October 7, 2007",
                 sub="At No Mercy he was awarded the vacated WWE Championship by Vince McMahon, lost it to "
                     "Triple H in an impromptu match the same night, and won it back from Triple H later "
                     "the same night in a Last Man Standing match. WWE and WrestleIndex both count two "
                     "reigns on that date, at 'less than 1 day' and 203 days. WWE's own classics title "
                     "history does not clearly separate them in its displayed date range, which is why "
                     "some databases merge them — and merging them also yields 13, by a different route."),
            dict(name="The lineage split causes none of the confusion",
                 sub="This is the part usually gotten backwards. The WWE Championship and the 2002-2013 "
                     "World Heavyweight Championship were genuinely separate titles with separate "
                     "lineages, so counting them separately is correct rather than double-counting. On "
                     "unification the belt was renamed but retained the WWE Championship lineage, so his "
                     "October 27, 2013 to April 6, 2014 reign spans the rename and counts once. The World "
                     "Heavyweight Championship introduced in 2023 is a third title he has never held."),
            dict(name="Youngest world champion in WWE history, at 24",
                 sub="Beat Chris Benoit for the World Heavyweight Championship at SummerSlam on August 15, "
                     "2004. Stated by both WWE.com and Wikipedia, and still standing as of August 2026. "
                     "Orton has said publicly that he does not expect it to be broken."),
            dict(name="Final World Heavyweight Champion of the 2002-2013 lineage",
                 sub="December 15, 2013 — he won the title and retired it in the same match."),
            dict(name="Most pay-per-view matches by a male WWE wrestler",
                 sub="Per Wikipedia, which phrases it as a record held 'since 2021' — that is a dating of "
                     "when he took the record, not a cutoff. The precise match total is not verified and "
                     "is not published here."),
            dict(name="Two Royal Rumble wins, a Money in the Bank and two Elimination Chambers",
                 sub="Royal Rumble 2009 and 2017; Money in the Bank 2013, cashed in at SummerSlam on "
                     "August 18, 2013; Elimination Chamber wins in 2014 and 2026, the second of which "
                     "earned the WrestleMania 42 title shot. He is the 17th Triple Crown Champion and the "
                     "18th Grand Slam Champion."),
            dict(name="210-day Intercontinental Championship reign",
                 sub="December 14, 2003 to July 11, 2004 — the longest reign with that title in seven "
                     "years at the time, and Evolution's share of a December 2003 sweep in which the group "
                     "held every major championship on Raw."),
            dict(name="PWI No. 1 in 2008, Wrestler of the Year in 2009 and 2010",
                 sub="Also PWI Most Hated Wrestler in 2007 and 2009, Most Improved Wrestler in 2004, and "
                     "Feud of the Year 2009 for the Triple H programme."),
            dict(name="Wrestling Observer Newsletter Worst Feud of the Year, 2017",
                 sub="For the Bray Wyatt programme. Published here rather than omitted: a career this long "
                     "includes the awards nobody wants."),
        ],
        footnote=("Four things are deliberately absent. No WrestleMania headliner count: Wikipedia says "
                  "three, but that predates WrestleMania 42, which he headlined on April 18, 2026, so four "
                  "is likely and unsourced. No Instagram link: instagram.com/randyorton and "
                  "instagram.com/official_randyorton both appear legitimate and neither could be confirmed "
                  "as official, so the handle is omitted rather than guessed. No attendance or "
                  "television-ratings record: none specific to Orton was verified. And no career "
                  "win-loss total: WrestleIndex totals him at 17 title reigns while omitting both RK-Bro "
                  "reigns and the SmackDown Tag Team reign, so it is used here only for world-title dates "
                  "and day counts.")
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="X / Twitter", v="@RandyOrton", href="https://x.com/RandyOrton"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/randy-orton"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Randy_Orton"),
        dict(k="WrestleIndex", v="Per-reign dates and day counts",
             href="https://wrestleindex.com/wwe/randy-orton/"),
        dict(k="Wikipedia", v="World Heavyweight Championship, 2002–2013",
             href="https://en.wikipedia.org/wiki/World_Heavyweight_Championship_(WWE,_2002%E2%80%932013)"),
        dict(k="TheSportster", v="His 14 world title reigns, ranked",
             href="https://www.thesportster.com/wrestling/randy-orton-14-wwe-world-title-reigns-ranked/"),
        dict(k="PWMania", v="SmackDown, August 21, 2026 — the “number 15” promo",
             href="https://www.pwmania.com/wwe-smackdown-results-august-21-2026"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/randy-orton.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="How many world titles has Randy Orton won?",
            a="<b>Fourteen</b> &mdash; ten WWE Championships and four World Heavyweight Championships. "
              "WWE.com and Wikipedia state the figure independently and break it down the same way, so "
              "there is no source conflict on the headline number. It is the third-most in WWE history, "
              "behind John Cena&rsquo;s seventeen and Ric Flair&rsquo;s sixteen and level with Triple H. "
              "He has not won one since November 16, 2020.",
            q_ld="How many world titles has Randy Orton won?",
            a_ld="Randy Orton has won 14 world championships: ten WWE Championship reigns and four World "
                 "Heavyweight Championship reigns. WWE.com and Wikipedia state the figure independently "
                 "and break it down identically, so there is no conflict on the headline number. It is the "
                 "third-most in WWE history, behind John Cena with 17 and Ric Flair with 16, and level "
                 "with Triple H. Randy Orton has not won a world championship since November 16, 2020."),
        dict(
            q="Why do some sources say Randy Orton is a 13-time or 15-time world champion?",
            a="Three different causes, and only one is a real dispute. The <b>15</b> is not a count at all "
              "&mdash; it is the title he is chasing on television; on the August 21, 2026 SmackDown he "
              "said he is going to &ldquo;get number 15,&rdquo; and aggregators keep reading that as a "
              "title he already has. The <b>13</b> is legitimate: WWE counts his December 15, 2013 TLC win "
              "as a separate fourth World Heavyweight Championship reign lasting about <b>one minute</b> "
              "before he retired the belt on unification, and TheSportster says outright that &ldquo;for "
              "some reason, WWE decided to count this.&rdquo; Drop that reign and you get 13. A second "
              "asterisk nobody raises does the same thing: on <b>October 7, 2007</b> he was awarded the "
              "vacant WWE Championship, lost it to Triple H and won it back the same night, and WWE counts "
              "that as two reigns on one date.",
            q_ld="Why do some sources say Randy Orton is a 13-time or 15-time world champion?",
            a_ld="Three separate causes, only one of which is a genuine dispute. The figure 15 is not a "
                 "count but a target: on the August 21, 2026 episode of SmackDown Randy Orton said on "
                 "camera that he is going to get number 15, and that storyline goal is being misread as a "
                 "title he already holds. The figure 13 is legitimate: WWE counts his December 15, 2013 "
                 "TLC win over John Cena as a separate fourth World Heavyweight Championship reign that "
                 "lasted about one minute before he retired the title on unification, and TheSportster "
                 "notes that for some reason WWE decided to count it. A second asterisk produces the same "
                 "result: on October 7, 2007 Randy Orton was awarded the vacant WWE Championship by Vince "
                 "McMahon, lost it to Triple H the same night and won it back the same night in a Last Man "
                 "Standing match, and WWE counts those as two separate reigns on one calendar date."),
        dict(
            q="Doesn&rsquo;t the WWE and World Heavyweight title split double-count his reigns?",
            a="No &mdash; this is the part most often gotten backwards. The WWE Championship and the "
              "2002&ndash;2013 World Heavyweight Championship were two genuinely separate titles with "
              "separate lineages, so counting them separately is correct. When they were unified on "
              "December 15, 2013 the belt was renamed but <i>retained the WWE Championship lineage</i>, "
              "which is why his October 27, 2013 to April 6, 2014 reign spans the rename and counts once "
              "rather than twice. The World Heavyweight Championship introduced in 2023 is a third, "
              "different title, and Orton has never held it.",
            q_ld="Does the WWE Championship and World Heavyweight Championship split double-count Randy "
                 "Orton's reigns?",
            a_ld="No. The WWE Championship and the World Heavyweight Championship of 2002 to 2013 were two "
                 "genuinely separate titles with separate lineages, so counting them separately is correct "
                 "rather than double-counting. When they were unified on December 15, 2013 the belt was "
                 "renamed the WWE World Heavyweight Championship but retained the lineage of the WWE "
                 "Championship, so Randy Orton's reign from October 27, 2013 to April 6, 2014 spans the "
                 "rename and counts once. The World Heavyweight Championship introduced in 2023 is a "
                 "different title that Randy Orton has never held."),
        dict(
            q="Is Randy Orton really the youngest world champion in WWE history?",
            a="Yes. He was 24 when he beat Chris Benoit for the World Heavyweight Championship at "
              "SummerSlam on August 15, 2004. WWE.com and Wikipedia both state it and the record still "
              "stands as of August 2026; Orton has said publicly that he does not expect it to be broken. "
              "Evolution ejected him the following night, and Triple H took the title back at Unforgiven "
              "28 days later.",
            q_ld="Is Randy Orton the youngest world champion in WWE history?",
            a_ld="Yes. Randy Orton was 24 years old when he beat Chris Benoit for the World Heavyweight "
                 "Championship at SummerSlam on August 15, 2004. WWE.com and Wikipedia both state it, and "
                 "the record still stands as of August 2026. Evolution ejected him the following night and "
                 "Triple H took the title back at Unforgiven 28 days later."),
        dict(
            q="Why did Randy Orton turn on Cody Rhodes?",
            a="In storyline, the turn happened in March 2026 and is driven by his pursuit of a fifteenth "
              "world championship &mdash; Rhodes was the champion in the way. Orton won the Elimination "
              "Chamber, then lost the WrestleMania 42 Night 1 main event to Rhodes on April 18, 2026 in a "
              "match refereed by Pat McAfee, and punted him after the bell. He returned at SummerSlam on "
              "August 1 to cost Rhodes the Undisputed WWE Championship against CM Punk. The irony the "
              "angle trades on is real: Rhodes was Orton&rsquo;s prot&eacute;g&eacute; in The Legacy from "
              "2008 to 2010.",
            q_ld="Why did Randy Orton turn on Cody Rhodes?",
            a_ld="In storyline terms, Randy Orton turned on Cody Rhodes in March 2026 in pursuit of a "
                 "fifteenth world championship, with Rhodes as the champion standing in the way. Orton won "
                 "the Elimination Chamber, then lost the WrestleMania 42 Night 1 main event to Rhodes on "
                 "April 18, 2026 in a match refereed by Pat McAfee and punted him after the bell. He "
                 "returned at SummerSlam on August 1, 2026 to cost Rhodes the Undisputed WWE Championship "
                 "against CM Punk. Cody Rhodes had been Randy Orton's protege in The Legacy from 2008 to "
                 "2010."),
        dict(
            q="What happened to RK-Bro, and when does Orton wrestle next?",
            a="RK-Bro ran from April 2021 and won the Raw Tag Team Championship twice, for 142 days and 74 "
              "days. It stopped when Orton suffered a back injury in May 2022 that kept him out for well "
              "over a year, and it formally ended when Matt Riddle was released by WWE in September 2023. "
              "His next announced match is Cody Rhodes vs. Randy Orton at WWE Sunday Night&rsquo;s Main "
              "Event on <b>September 6, 2026</b> in Atlanta, Rhodes&rsquo; billed hometown; SmackDown "
              "general manager Nick Aldis has banned physical contact between them until then.",
            q_ld="What happened to RK-Bro, and when is Randy Orton's next match?",
            a_ld="RK-Bro, the team of Randy Orton and Matt Riddle, ran from April 2021 and won the Raw Tag "
                 "Team Championship twice, for 142 days and 74 days. It stopped when Randy Orton suffered "
                 "a back injury in May 2022 that kept him out for well over a year, and formally ended "
                 "when Matt Riddle was released by WWE in September 2023. Randy Orton's next announced "
                 "match is against Cody Rhodes at WWE Sunday Night's Main Event on September 6, 2026 in "
                 "Atlanta, Georgia. SmackDown general manager Nick Aldis has banned physical contact "
                 "between them until the event."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Born", value="April 1, 1980", sub="Knoxville, Tennessee"),
        dict(label="Billed from", value="St. Louis, Missouri"),
        dict(label="Height", value="6&#8242;5&#8243;", sub="196 cm"),
        dict(label="Weight", value="275 lb", sub="125 kg (billed) &middot; not cross-checked against Wikipedia"),
        dict(label="Family", value="Third generation",
             sub="Bob Orton Sr. &middot; &ldquo;Cowboy&rdquo; Bob Orton Jr. &middot; Barry Orton"),
        dict(label="Trained by", value="Bob Orton Jr.", sub="with MMWA&ndash;SICW staff, St. Louis"),
        dict(label="Debut", value="2000", sub="MMWA&ndash;SICW &middot; WWE main roster 2002"),
        dict(label="Finisher", value="RKO", sub="jumping cutter, out of nowhere"),
        dict(label="Signatures", value="Punt kick to the head &middot; elevated rope-hung DDT"),
        dict(label="Brand", value="SmackDown", sub="part-time"),
        dict(label="World titles", value="14", sub="10 WWE Championship &middot; 4 World Heavyweight"),
        dict(label="Also known as", value="The Legend Killer &middot; The Viper &middot; The Apex Predator"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1980-04-01",
    bornplace="Knoxville, Tennessee, United States",
    nationality="United States",
    height_cm=196,
    weight_kg=125,
    ld=dict(
        alternateName=["The Viper", "The Legend Killer", "The Apex Predator"],
        award=["WWE Championship (10 reigns)",
               "World Heavyweight Championship, 2002-2013 lineage (4 reigns, including the final reign)",
               "Youngest world champion in WWE history, at age 24",
               "WWE Intercontinental Championship (1 reign, 210 days)",
               "WWE United States Championship (1 reign)",
               "Raw Tag Team Championship (2 reigns, with Matt Riddle as RK-Bro)",
               "World Tag Team Championship (1 reign, with Edge as Rated-RKO)",
               "SmackDown Tag Team Championship (1 reign, with the Wyatt Family)",
               "Royal Rumble winner (2009, 2017)",
               "Money in the Bank winner (2013)",
               "Elimination Chamber winner (2014, 2026)",
               "17th WWE Triple Crown Champion",
               "18th WWE Grand Slam Champion",
               "Pro Wrestling Illustrated 500 number one (2008)",
               "Pro Wrestling Illustrated Wrestler of the Year (2009, 2010)",
               "Pro Wrestling Illustrated Feud of the Year (2009, with Triple H)"],
        knowsAbout=["Professional wrestling", "WWE", "Championship wrestling", "Evolution",
                    "The Legacy", "The Authority", "Orton wrestling family"],
        description="Randy Orton is an American professional wrestler signed to WWE and a "
                    "third-generation wrestler, the son of Bob Orton Jr. He is a 14-time world champion, "
                    "with ten WWE Championship reigns and four World Heavyweight Championship reigns, a "
                    "total behind only John Cena and Ric Flair and level with Triple H. He became the "
                    "youngest world champion in WWE history at 24 by beating Chris Benoit at SummerSlam on "
                    "August 15, 2004, won the Royal Rumble in 2009 and 2017, unified the WWE and World "
                    "Heavyweight Championships by beating John Cena at TLC on December 15, 2013, and has "
                    "wrestled more pay-per-view matches than any other male WWE wrestler. He debuted in "
                    "St. Louis in 2000 and reached the WWE main roster in 2002.",
        sameAs=["https://x.com/RandyOrton",
                "https://en.wikipedia.org/wiki/Randy_Orton",
                "https://www.wwe.com/superstars/randy-orton"],
    ),
)
