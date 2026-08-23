# -*- coding: utf-8 -*-
"""Cody Rhodes - dossier data.

Sources: /tmp/research/cody-rhodes.md (web-verified, compiled Aug 23 2026) and the
harvested match/signature/tape data from the previous /wrestlers/cody-rhodes/ page.

Nothing here is invented. Two items the research explicitly flags as BAD EXTRACTIONS
are deliberately absent: the "Cody Rhodes - The Bloodline (2024-present)" stable line
(he has never been in The Bloodline) and the "14 day" first Undisputed WWE title reign
(the real figure is 378 days, SEScoops). The old page's "78-38" career headline is not
republished either - the harvester flags it as inconsistent with its own sparkline, and
Cagematch was JavaScript-gated for the research pass, so no career total is claimed.
"""

# ----------------------------------------------------------------- record rows
# Seven rows harvested from the existing page, plus rows whose dates are stated
# day-precise in the research dossier. Anything without a day-precise date (the two
# Intercontinental reigns, the ROH/NWA/IWGP loss dates, the 2024 Crown Jewel final,
# the second TNT reign) is described in the Championships section instead of being
# given a fabricated date here.
ROWS = [
    dict(result="W", date="2013-10-14", promo="WWE", type="tag", landmark=True,
         event="Raw", opponent="Seth Rollins & Roman Reigns",
         stip="No-DQ tag w/ Goldust — jobs on the line",
         title="WWE Tag Team Championship"),
    dict(result="W", date="2017-06-23", promo="ROH", landmark=True,
         event="Best in the World", opponent="Christopher Daniels",
         stip="Singles — first world championship of his career",
         title="ROH World Championship"),
    dict(result="W", date="2018-09-01", promo="NWA", landmark=True,
         event="All In — Sears Centre", opponent="Nick Aldis",
         stip="Singles — on the show he co-promoted",
         title="NWA Worlds Heavyweight Championship"),
    dict(result="W", date="2019-05-25", promo="AEW",
         event="Double or Nothing", opponent="Dustin Rhodes", opponent_html=True,
         stip="Singles — brother vs. brother, AEW's debut pay-per-view", title=""),
    dict(result="W", date="2020-05-23", promo="AEW", landmark=True,
         event="Double or Nothing", opponent="Lance Archer",
         stip="Tournament final — inaugural champion, belt presented by Mike Tyson",
         title="AEW TNT Championship"),
    dict(result="W", date="2021-12-25", promo="AEW",
         event="Rampage — Holiday Bash", opponent="Sammy Guevara",
         stip="Singles — third reign begins", title="AEW TNT Championship"),
    dict(result="L", date="2022-01-26", promo="AEW",
         event="Dynamite — Beach Break", opponent="Sammy Guevara",
         stip="Ladder match — his last AEW title match", title="AEW TNT Championship"),
    dict(result="W", date="2022-04-02", promo="WWE", landmark=True,
         event="WrestleMania 38 Night 1", opponent="Seth Rollins", opponent_html=True,
         stip="Singles — the surprise WWE return", title=""),
    dict(result="L", date="2022-04-08", promo="WWE",
         event="SmackDown", opponent="Roman Reigns", opponent_html=True,
         stip="Singles", title=""),
    dict(result="L", date="2022-06-05", promo="WWE", landmark=True,
         event="Hell in a Cell", opponent="Seth Rollins", opponent_html=True,
         stip="Hell in a Cell — worked it with a torn pectoral tendon", title=""),
    dict(result="W", date="2023-01-28", promo="WWE", type="tag", landmark=True,
         event="Royal Rumble", opponent="The 2023 Royal Rumble field",
         stip="Royal Rumble match — first of two straight", title=""),
    dict(result="L", date="2023-04-01", promo="WWE", landmark=True,
         event="WrestleMania 39", opponent="Roman Reigns", opponent_html=True,
         stip="Singles — Solo Sikoa interference",
         title="Undisputed WWE Universal Championship"),
    dict(result="W", date="2024-01-27", promo="WWE", type="tag", landmark=True,
         event="Royal Rumble", opponent="The 2024 Royal Rumble field",
         stip="Royal Rumble match — first back-to-back winner since 1998", title=""),
    dict(result="W", date="2024-04-07", promo="WWE", landmark=True,
         event="WrestleMania XL Night 2", opponent="Roman Reigns", opponent_html=True,
         stip="Bloodline Rules — ends a 1,316-day reign",
         title="Undisputed WWE Championship"),
    dict(result="L", date="2025-04-20", promo="WWE", landmark=True,
         event="WrestleMania 41 Night 2", opponent="John Cena", opponent_html=True,
         stip="Singles — ends the 378-day first reign",
         title="Undisputed WWE Championship"),
    dict(result="W", date="2025-08-03", promo="WWE", landmark=True,
         event="SummerSlam Night 2", opponent="John Cena", opponent_html=True,
         stip="Singles — second reign begins", title="Undisputed WWE Championship"),
    dict(result="L", date="2026-01-09", promo="WWE",
         event="SmackDown", opponent="Drew McIntyre",
         stip="Three Stages of Hell — ends a 159-day reign",
         title="Undisputed WWE Championship"),
    dict(result="W", date="2026-03-06", promo="WWE",
         event="SmackDown", opponent="Drew McIntyre",
         stip="Singles — third reign begins", title="Undisputed WWE Championship"),
    dict(result="W", date="2026-04-18", promo="WWE",
         event="WrestleMania 42 Night 1", opponent="Randy Orton",
         stip="Singles — defense against his old Legacy leader",
         title="Undisputed WWE Championship"),
    dict(result="W", date="2026-05-31", promo="WWE",
         event="Clash in Italy", opponent="Gunther",
         stip="Singles — defense", title="Undisputed WWE Championship"),
    dict(result="L", date="2026-06-27", promo="WWE", landmark=True,
         event="Night of Champions", opponent="Sami Zayn",
         stip="Triple threat also involving Gunther — ends a 113-day reign",
         title="Undisputed WWE Championship"),
    dict(result="L", date="2026-08-01", promo="WWE", landmark=True,
         event="SummerSlam Night 1 — U.S. Bank Stadium", opponent="CM Punk", opponent_html=True,
         stip="Singles — Randy Orton returns and hits the RKO",
         title="Undisputed WWE Championship"),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Roman Reigns": "roman-reigns", "Seth Rollins": "seth-rollins",
                 "John Cena": "john-cena", "CM Punk": "cm-punk",
                 "Dustin Rhodes": "dustin-rhodes"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

PULSE = dict(
 handle="CodyRhodes",
 lead=("What he is posting, as it happens. His X account is active and curated here from "
       "press-verified posts &mdash; every quote is verbatim, every card links the original "
       "post. His family life lives on Instagram; the Orton feud, notably, he has not "
       "posted about at all. Newest first."),
 foot=("Follow live: <a href=\"https://x.com/CodyRhodes\" target=\"_blank\" rel=\"noopener\">"
       "@CodyRhodes on X</a> &middot; curated by hand &middot; quotes verbatim from the linked posts "
       "&middot; no engagement counts shown because we refuse to fake them"),
 cards=[
  dict(x_url="https://x.com/CodyRhodes/status/2087977889421525411", date="Aug 13 &middot; 2026", wide=True,
       quote=("&ldquo;Bus broke down on the side of the road (still going to make the house show!) "
              "but while we pass the time&hellip; &#128165; Old school. Q/A &#128165; Use #CodyBus&rdquo;"),
       why=("A flat tire became an hour-long live Q&amp;A with fans from the roadside &mdash; the "
            "replies below are from that thread."),
       src="Wrestling Headlines",
       src_url="https://wrestlingheadlines.com/cody-rhodes-american-nightmare-tour-bus-breaks-down-rhodes-does-live-twitter-qa-to-pass-time/"),
  dict(x_url="https://x.com/CodyRhodes/status/2087311053109510352", date="Aug 11 &middot; 2026",
       quote=("&ldquo;Arik my friend no shade intended, but my outlook&hellip; Avery is 19. His Father "
              "was paying dues and making sacrifices throughout that young man&rsquo;s youth that some "
              "people may never understand&hellip; To simplify&hellip;he already set up the fn&rsquo; chairs&rdquo;"),
       why="Defending AJ Styles&rsquo; 19-year-old son against a paying-dues callout. The locker-room-leader voice, unprompted.",
       src="Fightful",
       src_url="https://www.fightful.com/wrestling/cody-rhodes-explains-how-avery-styles-already-set-up-the-fn-chairs/"),
  dict(x_url="https://x.com/CodyRhodes/status/2087985660569207180", date="Aug 13 &middot; 2026",
       quote=("&ldquo;The rest of the cast. Everybody loving and knowing the games! 10/16 &#128165; "
              "can&rsquo;t come soon enough!&rdquo;"),
       why="From the bus Q&amp;A: what excited him most about playing Guile in the Street Fighter film, in theaters October 16.",
       src="Wrestling Headlines",
       src_url="https://wrestlingheadlines.com/cody-rhodes-american-nightmare-tour-bus-breaks-down-rhodes-does-live-twitter-qa-to-pass-time/"),
  dict(x_url="https://x.com/CodyRhodes/status/2087986716581753006", date="Aug 13 &middot; 2026",
       quote="&ldquo;Tomorrow morning actually&hellip; &#128064; Brand new collection. First class.&rdquo;",
       why="Merch tease from the same thread; the collection dropped the next morning.",
       src="Wrestling Headlines",
       src_url="https://wrestlingheadlines.com/cody-rhodes-american-nightmare-tour-bus-breaks-down-rhodes-does-live-twitter-qa-to-pass-time/"),
  dict(x_url="https://x.com/CodyRhodes/status/2074214475851284791", date="Jul 6 &middot; 2026",
       quote="&#127942;&#127942;&#127942;&#127942;",
       why=("Four trophies, no words, posted hours before his booked title rematch on Raw &mdash; the match "
            "a Gunther attack took him out of. The fourth-reign reading is ours, not his; he never explained it."),
       src="SI",
       src_url="https://www.si.com/fannation/wrestling/wwe/wwe-raw-results-cody-rhodes-unable-to-compete-for-wwe-title"),
  dict(x_url="https://x.com/CodyRhodes/status/2030986108490637821", date="Mar 9 &middot; 2026",
       quote="&ldquo;Records can be broken (even your own) There&rsquo;s nothing like Mania&rdquo;",
       why="On course for his fourth straight WrestleMania main event, a record he already held.",
       src="Yahoo Sports",
       src_url="https://sports.yahoo.com/articles/cody-rhodes-reacts-4th-consecutive-160500987.html"),
 ])

DATA = dict(
 pulse=PULSE,
    slug="cody-rhodes",
    name="Cody Rhodes",
    realname="Cody Garrett Runnels",
    epithet="The American Nightmare",
    hook="Record & Titles",

    meta_desc=("Cody Rhodes, The American Nightmare, is a three-time Undisputed WWE Champion who ended "
               "Roman Reigns' 1,316-day reign at WrestleMania XL. He is not, per WWE's own title lineage, "
               "a Universal Champion. Full record, titles, factions and career."),
    og_desc=("The American Nightmare: 3 Undisputed WWE Championship reigns totalling 650 days, "
             "back-to-back Royal Rumbles, a record three TNT Championships — and the Universal "
             "Championship claim WWE.com contradicts on its own site."),
    tw_desc=("3 Undisputed WWE reigns, 650 days, back-to-back Royal Rumbles — and why the "
             "“Universal Champion” line on his WWE.com profile does not survive WWE's own records."),

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2006",
    height_imp="6&#8242;2&#8243;",
    weight_lb="222",
    world_titles="3",
    vitals_tagline="Finish the story",
    support_note="Merch &middot; Games &middot; Watch",
    x_url="https://x.com/codyrhodes",
    ig_url="https://www.instagram.com/americannightmarecody/",
    sp_items=[
        dict(ic="CR", title="American Nightmare Merch", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="WWE 2K24 cover athlete · 20 games",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="SF", title="Street Fighter", sub="Plays Guile · October 16, 2026",
             tag="Watch", href="https://en.wikipedia.org/wiki/Street_Fighter_(2026_film)"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/cody-rhodes"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The American Nightmare &middot; Son of the American Dream &middot; The Man Who Finished the Story",
    hero_tag="Rhodes Family &middot; <em>OVW &middot; ROH &middot; NWA &middot; AEW &middot; WWE &middot; 2006&ndash;present</em>",
    now_label="NOW",
    now_bold="Untitled — SmackDown",
    now_tail=" &middot; third reign ended June 27, 2026; faces Randy Orton at Sunday Night&rsquo;s Main Event, September 6",
    hstats=[
        dict(value="3",   x=True,  label="Undisputed WWE Reigns"),
        dict(value="650", x=False, label="Days as WWE Champion"),
        dict(value="2",   x=True,  label="Straight Royal Rumbles"),
        dict(value="3",   x=True,  label="TNT Championships"),
    ],
    ghost_link="From Stardust to finishing the story",
    vlabel="Est. 2006 &middot; Atlanta, GA",
    mono="CR",

    # ---------------------------------------------------------------- 01 overview
    # index into overview of the correction paragraph -> the framed
    # "Setting one thing straight" callout (aside.corr) on the page
    correction=1,
    overview=[
        "<b>Cody Rhodes</b> is the wrestler who left WWE as a mid-card comedy act, built a rival "
        "company, and came back to end the longest world title reign of the modern era &mdash; and the "
        "industry rearranged itself around that arc. "
        '<span class="pull pull--q" aria-hidden="true">'
        '<span class="pull-quote">He took a character WWE had discarded and turned it into the company&rsquo;s most bankable act &mdash; and he did it by leaving first.</span></span>'
        "He is the only person to have been an executive "
        "vice president of All Elite Wrestling and then the top babyface of WWE. Between 2023 and 2026 "
        "he won back-to-back Royal Rumbles, main-evented four consecutive WrestleManias, topped the "
        "PWI 500 in consecutive years, and took the Wrestling Observer Newsletter&rsquo;s Wrestler of "
        "the Year for 2024. The concrete claim is simpler than the mythology: he took a character WWE "
        "had discarded and turned it into the company&rsquo;s most bankable act, and he did it by "
        "leaving first.",

        "One correction belongs up front, because it is the reason his world title count is reported "
        "three different ways. <b>Cody Rhodes is not a Universal Champion &mdash; not per WWE&rsquo;s "
        "own title lineage.</b> At WrestleMania XL Night 2 on April 7, 2024 he beat Roman Reigns for "
        "what was then billed as the Undisputed WWE Universal Championship, and WWE immediately stopped "
        "treating the Universal Championship as a distinct title. It was <i>retired</i> rather than "
        "transferred: Fightful and Cageside Seats both reported in April 2025 that WWE.com&rsquo;s title "
        "page now lists the belt as retired with <b>Roman Reigns</b> as its final champion, and Rhodes "
        "absent from the lineage entirely. Yet WWE.com&rsquo;s Cody Rhodes Superstar profile still "
        "carries &ldquo;Universal Champion&rdquo; as a line item next to &ldquo;Undisputed WWE Champion "
        "(x3).&rdquo; WWE.com contradicts WWE.com, and that single unresolved line is what drives the "
        "spread across databases: <b>three</b> world reigns if the WrestleMania XL win counts once, "
        "<b>four</b> if it is double-counted as WWE and Universal, <b>five</b> once the ROH and NWA "
        "world titles from his time away are folded in. This page counts it once.",

        "He was born Cody Garrett Runnels on June 30, 1985, son of Dusty Rhodes and half-brother of "
        "Dustin Rhodes. He wrestled amateur at Lassiter High School in Marietta, Georgia, winning "
        "Georgia state championships in 2003 and 2004, and debuted on June 16, 2006 in Ohio Valley "
        "Wrestling. His first WWE title, the World Tag Team Championship with Hardcore Holly, came in "
        "December 2007; The Legacy with Randy Orton and Ted DiBiase Jr. followed from 2008 to 2010. "
        "Then came a decade of characters that never quite landed &mdash; &ldquo;Dashing&rdquo; Cody "
        "Rhodes, the masked &ldquo;Undashing&rdquo; run, Rhodes Scholars with Damien Sandow, The "
        "Brotherhood with Goldust, and finally Stardust, the face-painted cosmic gimmick he asked to be "
        "released from. WWE granted the release on May 21, 2016.",

        '<span class="pull" aria-hidden="true"><span class="pull-fig">10,000</span>'
        '<span class="pull-cap">seats at All In, the self-financed 2018 show he co-promoted &mdash; the proof of concept for AEW</span></span>'
        "The run that made him happened outside WWE. He worked as &ldquo;Cody,&rdquo; a mononym, "
        "because WWE owned the surname &mdash; a trademark he did not get back until November 2020. He "
        "joined Bullet Club and The Elite, took the ROH World Championship from Christopher Daniels on "
        "June 23, 2017, and beat Nick Aldis for the NWA Worlds Heavyweight Championship on September 1, "
        "2018 at All In, the self-financed 10,000-seat show he co-promoted with the Young Bucks and "
        "which became the proof-of-concept for AEW. As an AEW EVP he was the inaugural and record "
        "three-time TNT Champion, and never AEW World Champion &mdash; he wrote a stipulation barring "
        "himself from the title into his own storyline, a call he has since said was a mistake. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">650</span>'
        '<span class="pull-cap">days as Undisputed WWE Champion across three reigns after finishing the story</span></span>'
        "He left "
        "in February 2022, returned at WrestleMania 38, won the Rumble in 2023 and 2024, and finished "
        "the story on April 7, 2024. Three reigns and 650 days later he is untitled, on SmackDown, and "
        "back in a feud with Randy Orton that started in 2009.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE", "AEW", "ROH", "NWA"],
        promo_labels={"WWE": "WWE", "AEW": "AEW", "ROH": "ROH", "NWA": "NWA"},
        stats=[
            ("3&times;", "Undisputed WWE reigns"),
            ("650",      "Days as WWE Champion"),
            ("378",      "Longest reign (days)"),
            ("3&times;", "AEW TNT Championship"),
            ("2&times;", "Royal Rumble wins"),
            ("34th",     "Triple Crown"),
        ],
        lead=("Twenty-two documented bouts &mdash; every world title change, the WrestleMania main "
              "events and the nights that redirected the career. <b>This is a curated ledger, not a "
              "career count:</b> the 22 in the counter is the number of rows on this page, not the "
              "number of matches he has wrestled. Cagematch is JavaScript-gated and could not be read "
              "for this file, and the previous edition of this profile carried a &ldquo;78&ndash;38&rdquo; "
              "headline that did not agree with its own chart, so no career win&ndash;loss total is "
              "published here rather than guessed. Filter by match type, tap any column header to sort, "
              "and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The three matches carried over from this profile&rsquo;s previous edition. Treat the "
                    "star ratings as that page&rsquo;s editorial call rather than sourced figures &mdash; "
                    "no Meltzer or Cagematch rating for any Cody Rhodes match could be verified for this "
                    "file, and none is invented here."),
    signature=[
        dict(rating="5.0", event="WrestleMania XL Night 2", opponent="Roman Reigns",
             stip="Bloodline Rules — the story finished", url="/wrestlers/roman-reigns/"),
        dict(rating="4.0", event="WrestleMania 38 Night 1", opponent="Seth Rollins",
             stip="Singles — the surprise return", url="/wrestlers/seth-rollins/"),
        dict(rating="4.0", event="AEW Double or Nothing 2019", opponent="Dustin Rhodes",
             stip="Singles — brother vs. brother", url="/wrestlers/dustin-rhodes/"),
    ],
    signature_count_word="three",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("3&times;", "Undisputed WWE reigns"),
            ("0",        "Universal Championships"),
            ("3&times;", "TNT Championship (record)"),
            ("34th",     "Triple Crown"),
        ],
        lead=("Three Undisputed WWE Championship reigns, two world titles won outside WWE, and one "
              "championship he is credited with that WWE&rsquo;s own lineage does not give him. Where "
              "sources disagree &mdash; and on the tag titles they disagree badly &mdash; the "
              "disagreement is printed rather than resolved."),
        rows=[
            dict(ic="W", name="Undisputed WWE Championship", count="3",
                 sub="2024&ndash;25, <b>378 days</b> &mdash; def. Roman Reigns at WrestleMania XL Night 2, "
                     "April 7, 2024; lost to John Cena at WrestleMania 41, April 20, 2025 &middot; "
                     "2025&ndash;26, 159 days &mdash; def. Cena at SummerSlam, August 3, 2025; lost to "
                     "Drew McIntyre, January 9, 2026 &middot; 2026, 113 days &mdash; def. McIntyre on "
                     "SmackDown, March 6, 2026; lost to Sami Zayn in a triple threat at Night of "
                     "Champions, June 27, 2026 &middot; <b>650 days combined</b>"),
            dict(ic="U", name="Universal Championship — not credited", count="0",
                 sub="<b>WWE.com&rsquo;s Superstar profile lists him as a Universal Champion; "
                     "WWE.com&rsquo;s title history does not.</b> The WrestleMania XL win was for the "
                     "then-unified Undisputed WWE Universal Championship, after which WWE retired the "
                     "Universal Championship rather than passing it on. Fightful and Cageside Seats "
                     "reported in April 2025 that WWE lists the belt as retired with Roman Reigns as "
                     "final champion and Rhodes nowhere in the lineage. Counted here as zero, and as one "
                     "&mdash; not two &mdash; world reign for WrestleMania XL."),
            dict(ic="T", name="AEW TNT Championship", count="3",
                 sub="Inaugural champion &middot; def. Lance Archer at Double or Nothing, May 23, 2020, "
                     "belt presented by Mike Tyson &middot; a record three reigns per Wikipedia &middot; "
                     "third reign def. Sammy Guevara on the December 25, 2021 Rampage, lost back to him "
                     "in a January 26, 2022 ladder match &middot; the second reign&rsquo;s end date is "
                     "not verified, and this file&rsquo;s sources give conflicting dates for the "
                     "reign-one/reign-two changeover, so neither is published as a match row"),
            dict(ic="R", name="ROH World Championship", count="1",
                 sub="def. Christopher Daniels at Best in the World, June 23, 2017 &middot; loss date and "
                     "reign length not verified"),
            dict(ic="N", name="NWA Worlds Heavyweight Championship", count="1",
                 sub="def. Nick Aldis at All In, September 1, 2018 &mdash; on the 10,000-seat show he "
                     "co-promoted &middot; loss date and reign length not verified"),
            dict(ic="I", name="WWE Intercontinental Championship", count="2",
                 sub="2011&ndash;12 &middot; reign count confirmed by WWE.com and Wikipedia; exact win and "
                     "loss dates were not verified for this file, so no reign lengths are claimed"),
            dict(ic="J", name="IWGP United States Heavyweight Championship", count="1",
                 sub="2018 &middot; dates not verified"),
            dict(ic="G", name="WWE tag team championships", count="?",
                 sub="<b>The sources contradict each other, including within one page.</b> WWE.com&rsquo;s "
                     "Superstar profile lists World Tag Team Champion (x3), WWE Tag Team Champion, Raw Tag "
                     "Team Champion (x4) and SmackDown Tag Team Champion &mdash; while the bio text on that "
                     "same page says six tag championships in his 2007&ndash;16 run. Wikipedia lists two "
                     "World Tag Team Championship reigns (2007&ndash;08, with Hardcore Holly and Ted DiBiase "
                     "Jr.); prowrestling.fandom says three World Tag and three WWE Tag. The &ldquo;Raw Tag "
                     "Team Champion (x4)&rdquo; line matches no reign this file could identify. "
                     "<b>Best supported: two World Tag Team reigns in 2007&ndash;08</b>, plus one WWE Tag "
                     "Team Championship &mdash; taken with Goldust from Seth Rollins and Roman Reigns in a "
                     "No-DQ match on the October 14, 2013 Raw, the only reign independently verified here. "
                     "No single total is published because no defensible one exists yet."),
            dict(ic="S", name="ROH World Six-Man Tag Team Championship", count="1",
                 sub="2018, with the Young Bucks &middot; dates not verified"),
            dict(ic="O", name="OVW Heavyweight, Television, Southern Tag Team", count="1 / 1 / 2",
                 sub="Developmental, 2006&ndash;07 &middot; dates not verified (prowrestling.fandom)"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Six groups across twenty years &mdash; two of them second-generation bloodline acts, one of "
             "them a company.",
        cards=[
            dict(era="WWE &middot; 2008&ndash;2010",
                 name="The Legacy",
                 members="Randy Orton, Cody Rhodes, Ted DiBiase Jr., briefly Manu",
                 desc="A second-generation heel unit built explicitly on wrestling bloodlines — Orton’s, "
                      "Rhodes’, DiBiase’s. It functioned as Orton’s enforcement arm through his 2009 world "
                      "title run and ended when Rhodes and DiBiase turned on him; both got singles pushes "
                      "out of it. Rhodes’ 2026 feud with Orton runs directly off this history."),
            dict(era="WWE &middot; 2012&ndash;2013",
                 name="Team Rhodes Scholars",
                 members="Cody Rhodes, Damien Sandow",
                 desc="A comedy-tinged tag team built on the “intellectual” pairing. They won a tag team "
                      "tournament and challenged for the tag titles before Sandow turned on Rhodes."),
            dict(era="WWE &middot; 2013&ndash;2014",
                 name="The Brotherhood",
                 members="Cody Rhodes, Dustin Rhodes (Goldust)",
                 desc="Real brothers, booked as fired and fighting for their jobs against The Shield. They "
                      "beat Seth Rollins and Roman Reigns for the WWE Tag Team Championship on the October "
                      "14, 2013 Raw and won the 2013 Slammy for Tag Team of the Year."),
            dict(era="NJPW / ROH / independents &middot; 2016&ndash;2019",
                 name="Bullet Club / The Elite",
                 members="Cody, Kenny Omega, The Young Bucks, Marty Scurll, Hangman Page",
                 desc="The vehicle for his post-WWE reinvention across NJPW, ROH and the independents. This "
                      "group promoted All In on September 1, 2018 — the show that proved a non-WWE promotion "
                      "could sell a 10,000-seat building — and its core became AEW’s founding talent."),
            dict(era="AEW &middot; 2019&ndash;2022",
                 name="The AEW executive group",
                 members="Cody Rhodes, Kenny Omega, The Young Bucks, under Tony Khan",
                 desc="Rhodes as Executive Vice President: he booked, produced and wrestled. He was the "
                      "inaugural and record three-time TNT Champion and never AEW World Champion, because he "
                      "wrote a stipulation barring himself from challenging for that title into his own "
                      "storyline — a decision he has since publicly called a creative mistake."),
            dict(era="AEW &middot; 2019&ndash;2022",
                 name="The Nightmare Family",
                 members="Cody Rhodes, Dustin Rhodes, Arn Anderson, QT Marshall, Brandi Rhodes",
                 desc="A training-and-mentorship stable centred on the Nightmare Factory school rather than "
                      "on a title chase — the closest thing his AEW run had to a permanent home."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Six characters, one of which is just his actual biography.",
        cards=[
            dict(mono="CR", era="OVW / WWE &middot; 2006&ndash;2010", name="Cody Runnels",
                 desc="Developmental and early main roster. A straight second-generation babyface, then a "
                      "Legacy heel. First WWE title — the World Tag Team Championship with Hardcore Holly — "
                      "in December 2007."),
            dict(mono="DCR", era="WWE &middot; 2010&ndash;2011", name="“Dashing” Cody Rhodes",
                 desc="A narcissist obsessed with his own face who handed out grooming tips on WWE "
                      "television. The first character that got a reaction on its own terms."),
            dict(mono="UN", era="WWE &middot; 2011&ndash;2013", name="“Undashing” Cody Rhodes",
                 desc="Rey Mysterio breaks his nose in storyline; Rhodes comes back in a clear protective "
                      "mask, sullen and disfigured. He won his first Intercontinental Championship in this "
                      "run."),
            dict(mono="SD", era="WWE &middot; 2014&ndash;2016", name="Stardust",
                 desc="A face-painted cosmic villain, a deliberate echo of Goldust. Rhodes has said the "
                      "gimmick was creatively dead-ended; he requested and received his release on May 21, "
                      "2016."),
            dict(mono="AN", era="Independents / AEW &middot; 2016&ndash;2020", name="“Cody” — The American Nightmare",
                 desc="A mononym, because WWE held the “Rhodes” trademark until November 2020. Independent "
                      "main-eventer, ROH and NWA world champion, All In co-promoter, AEW co-founder and "
                      "executive vice president."),
            dict(mono="TAN", era="WWE &middot; 2022&ndash;present", name="Cody Rhodes, The American Nightmare",
                 desc="The WWE return at WrestleMania 38. The character is the legacy pursuit itself — "
                      "“finish the story,” his father’s unfinished business — unusual in that the gimmick "
                      "is a documented biographical fact rather than a fiction."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Marietta to OVW to a company of his own and back.",
        rows=[
            dict(year="2006", title="Turns pro",
                 desc="Debuts June 16, 2006 in Ohio Valley Wrestling as Cody Runnels, after Georgia state "
                      "amateur titles at Lassiter High School in 2003 and 2004."),
            dict(year="2007", title="First WWE championship",
                 desc="Wins the World Tag Team Championship with Hardcore Holly in December 2007."),
            dict(year="2008", title="The Legacy",
                 desc="Joins Randy Orton and Ted DiBiase Jr. in the second-generation heel stable that "
                      "carries Orton’s world title run."),
            dict(year="2016", title="Asks out of WWE",
                 desc="Released May 21, 2016 after the Stardust run, and begins working as “Cody” because "
                      "WWE owns the surname."),
            dict(year="2018", title="All In",
                 desc="Co-promotes the 10,000-seat independent show on September 1, 2018 and beats Nick "
                      "Aldis on it for the NWA Worlds Heavyweight Championship."),
            dict(year="2019", title="Co-founds AEW",
                 desc="AEW is unveiled January 1, 2019 with Rhodes as Executive Vice President; he wins the "
                      "inaugural TNT Championship on May 23, 2020."),
            dict(year="2022", title="Returns to WWE",
                 desc="Leaves AEW February 15, 2022 and returns at WrestleMania 38 on April 2, beating Seth "
                      "Rollins. Tears a pectoral tendon that June and works Hell in a Cell with it."),
            dict(year="2024", title="Finishes the story",
                 desc="After back-to-back Royal Rumble wins in 2023 and 2024, beats Roman Reigns at "
                      "WrestleMania XL on April 7, 2024, ending a 1,316-day reign."),
            dict(year="2025", title="Loses and regains the title",
                 desc="Loses to John Cena at WrestleMania 41 on April 20 after 378 days, wins King of the "
                      "Ring on June 28, and beats Cena back at SummerSlam on August 3."),
            dict(year="2026", title="Third reign, then out of the picture",
                 desc="Regains the belt from Drew McIntyre on March 6, loses it to Sami Zayn at Night of "
                      "Champions on June 27, and fails to take it from CM Punk at SummerSlam on August 1 "
                      "after Randy Orton’s returning RKO."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Roman Reigns", slug="roman-reigns",
                 desc="Two consecutive WrestleMania main events with opposite outcomes: a loss at "
                      "WrestleMania 39 in 2023 to Solo Sikoa’s interference, then the Bloodline Rules win at "
                      "WrestleMania XL on April 7, 2024 that ended the fourth-longest world title reign in "
                      "WWE history. Structured as a two-year story about whether the challenger could "
                      "survive the Bloodline, and the most consequential single result of the 2020s."),
            dict(name="Randy Orton",
                 desc="Peaked in the 2009–10 Legacy breakup and is live again in 2026. Orton was both "
                      "Rhodes’ storyline mentor and one of his real trainers, which gives the feud a "
                      "mentor-betrays-student spine WWE keeps returning to. Orton’s return RKO at SummerSlam "
                      "on August 1, 2026 cost Rhodes the Undisputed WWE Championship and set their September "
                      "6 match at Sunday Night’s Main Event."),
            dict(name="John Cena", slug="john-cena",
                 desc="Peaked at WrestleMania 41 and SummerSlam 2025. Cena beat Rhodes on April 20, 2025 to "
                      "win a record 17th world championship, ending the 378-day reign; Rhodes beat him back "
                      "on August 3. The pair bookended Cena’s final run, with Rhodes cast as the man handing "
                      "the company over and then taking it back."),
            dict(name="MJF",
                 desc="Peaked in AEW across 2019–20. The feud that made MJF a main-event heel: a slow "
                      "betrayal built around Rhodes’ vanity, culminating in a Full Gear stipulation match. "
                      "It is the best evidence that Rhodes’ AEW value was as much in what he built around "
                      "him as in his own matches."),
            dict(name="Seth Rollins", slug="seth-rollins",
                 desc="Peaked at WrestleMania 38. Rollins was the surprise opponent for the WWE return on "
                      "April 2, 2022, and they wrestled a three-match series that year, including the Hell "
                      "in a Cell match Rhodes worked with a torn pectoral tendon. The feud’s job was to "
                      "re-establish him as a main-event WWE act within weeks of leaving AEW, and it did."),
            dict(name="Drew McIntyre",
                 desc="Peaked January to March 2026. McIntyre took the Undisputed WWE Championship in a "
                      "Three Stages of Hell match on the January 9, 2026 SmackDown and lost it back on March "
                      "6 — a 56-day interruption that reads as the setup for Rhodes’ third reign rather than "
                      "a genuine transfer of the top spot."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Beyond the ring.",
        rows=[
            dict(when="2026", title="Street Fighter", kind="Film",
                 desc="Plays Guile in Paramount’s adaptation, out October 16, 2026, alongside Roman Reigns "
                      "as Akuma, Andrew Koji as Ryu, Noah Centineo as Ken, Callina Liang as Chun-Li, David "
                      "Dastmalchian as M. Bison, Jason Momoa as Blanka and 50 Cent as Balrog. He took "
                      "roughly a month away from television to film it."),
            dict(when="2023", title="American Nightmare: Becoming Cody Rhodes", kind="Documentary",
                 desc="Peacock original covering the AEW exit and the WWE return."),
            dict(when="2021&ndash;22", title="Rhodes to the Top", kind="TV",
                 desc="Reality series with Brandi Rhodes on TNT, produced during the AEW run. Sources give "
                      "the air year as either 2021 or 2022 and this file did not resolve it. He also served "
                      "as a judge on TBS’s Go-Big Show."),
            dict(when="2024", title="WWE 2K24", kind="Game",
                 desc="Cover athlete alongside Rhea Ripley and Bianca Belair. TheSmackDownHotel’s database "
                      "credits him with appearances in 20 wrestling games."),
            dict(when="2025&ndash;", title="What Do You Wanna Talk About?", kind="YouTube",
                 desc="His own interview channel, launched 2025. Subscriber and view counts are deliberately "
                      "not printed here — they move daily and any figure in a static page is wrong by the "
                      "time it is read. No authorised autobiography exists; the “biographies” listed on "
                      "retailers are unauthorised third-party titles."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The numbers behind the run, stated the way the sources actually state them.",
        stats=[
            ("650",   "Days as WWE Champion"),
            ("378",   "Longest single reign"),
            ("1,316", "Day reign he ended"),
        ],
        rows=[
            dict(name="Back-to-back Royal Rumble wins, 2023 and 2024",
                 sub="January 28, 2023 and January 27, 2024. The fourth man to win two consecutive Royal "
                     "Rumbles and the first since Steve Austin in 1997–98; the others are Hulk Hogan "
                     "(1990–91) and Shawn Michaels (1995–96)."),
            dict(name="378-day first Undisputed WWE Championship reign",
                 sub="April 7, 2024 to April 20, 2025 (SEScoops). Note that a read of Wikipedia during this "
                     "research returned “April 6 – April 20, 2024 (14 days),” which is wrong on both the "
                     "start date and the length — a bad extraction rather than a source disagreement. The "
                     "378-day figure is the one to use."),
            dict(name="650 combined days as Undisputed WWE Champion",
                 sub="378 + 159 + 113 across three reigns, calculated from SEScoops and Last Word on Pro "
                     "Wrestling. The third reign carried televised defenses against Randy Orton at "
                     "WrestleMania 42 Night 1 and Gunther at Clash in Italy."),
            dict(name="Ended a 1,316-day world title reign",
                 sub="Roman Reigns’ Universal Championship run, the fourth-longest world title reign in WWE "
                     "history and the longest since 1988, closed out at WrestleMania XL."),
            dict(name="PWI 500 number one in 2024 and 2025",
                 sub="Back-to-back. Sports Illustrated reported this made him only the fourth wrestler ever "
                     "to repeat at number one. The 2026 list had not been published as of August 23, 2026; "
                     "it normally appears in September."),
            dict(name="Wrestling Observer Newsletter Wrestler of the Year, 2024",
                 sub="Ahead of Will Ospreay, who took Most Outstanding Wrestler the same year."),
            dict(name="Record three-time AEW TNT Champion, and the title’s first",
                 sub="Inaugural champion on May 23, 2020, beating Lance Archer at Double or Nothing with "
                     "Mike Tyson presenting the belt. The first reign ran a near-weekly open challenge, "
                     "including defenses against wrestlers from outside AEW."),
            dict(name="All In, September 1, 2018",
                 sub="Co-promoted the first non-WWE, non-WCW North American show to sell roughly 10,000 "
                     "tickets in about two decades, and beat Nick Aldis on it for the NWA Worlds "
                     "Heavyweight Championship. It became the direct precursor to AEW."),
            dict(name="34th WWE Triple Crown Champion, 2025 King of the Ring, inaugural Crown Jewel Champion",
                 sub="King of the Ring won June 28, 2025; the inaugural Crown Jewel Championship won in 2024 "
                     "over Gunther."),
            dict(name="WrestleMania 42 attendance is disputed by about 8,900",
                 sub="Rhodes defended the title against Randy Orton on Night 1, April 18, 2026. WWE’s "
                     "corporate release claimed 106,072 across both nights; POST Wrestling’s tally of WWE’s "
                     "own nightly figures came to 106,071, one short; the Las Vegas Stadium Authority "
                     "reported 97,126 (47,093 + 50,033). All three measures agree the show was down 15–18% "
                     "on WrestleMania 41. SummerSlam 2026, where he worked the Night 1 title match, drew "
                     "68,052 across two nights at U.S. Bank Stadium."),
        ],
        footnote=("No Cagematch figures appear anywhere on this page: the site is JavaScript-gated and "
                  "returned only a redirect stub to every fetch made for this file. Total-title counts also "
                  "diverge by methodology — a read of Wikipedia gives 19 championships across all "
                  "promotions, TheSmackDownHotel gives 25 total and “5-time World Champion,” and the gap is "
                  "mostly tag titles plus the Universal Championship question. No PLE buyrate or viewership "
                  "figure is cited because none was verifiable for the Netflix and ESPN era."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Instagram", v="@americannightmarecody",
             href="https://www.instagram.com/americannightmarecody/"),
        dict(k="X / Twitter", v="@codyrhodes", href="https://x.com/codyrhodes"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/cody-rhodes"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Cody_Rhodes"),
        dict(k="Cageside Seats", v="WWE officially retires the Universal Championship",
             href="https://www.cagesideseats.com/wwe/2025/4/22/24413556/wwe-officially-retires-universal-championship-roman-reigns-cody-rhodes-john-cena"),
        dict(k="SEScoops", v="The 378-day reign ends at WrestleMania 41",
             href="https://www.sescoops.com/article/cody-rhodes-title-reign-ends-john-cena-wrestlemania-41"),
        dict(k="Last Word on Pro Wrestling", v="2026 Undisputed WWE Championship tracker",
             href="https://lastwordonsports.com/prowrestling/2026/01/22/who-is-the-wwe-undisputed-champion-2026/"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/cody-rhodes.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Cody Rhodes a Universal Champion?",
            a="Not according to WWE&rsquo;s own title lineage &mdash; and WWE.com disagrees with itself "
              "about it. He beat Roman Reigns at WrestleMania XL on April 7, 2024 for what was billed at "
              "the time as the Undisputed WWE Universal Championship, but WWE then <b>retired</b> the "
              "Universal Championship instead of transferring it. Fightful and Cageside Seats both "
              "reported in April 2025 that WWE.com&rsquo;s title history lists the belt as retired with "
              "Roman Reigns as its final champion and Rhodes absent from the lineage. Yet the "
              "&ldquo;Championship Highlights&rdquo; list on WWE.com&rsquo;s own Cody Rhodes profile still "
              "shows &ldquo;Universal Champion.&rdquo; That contradiction is why you will see his world "
              "title count reported as three, four or five depending on the database.",
            q_ld="Is Cody Rhodes a Universal Champion?",
            a_ld="No, not according to WWE's published title lineage. Cody Rhodes beat Roman Reigns at "
                 "WrestleMania XL on April 7, 2024 for what was then billed as the Undisputed WWE "
                 "Universal Championship, but WWE retired the Universal Championship rather than "
                 "transferring it. Fightful and Cageside Seats reported in April 2025 that WWE.com's title "
                 "history lists the Universal Championship as retired with Roman Reigns as its final "
                 "champion, with Cody Rhodes absent from that lineage. WWE.com's own Cody Rhodes Superstar "
                 "profile nonetheless still lists Universal Champion among his championship highlights, "
                 "and that internal contradiction is why his world title count is reported as three, four "
                 "or five across different databases."),
        dict(
            q="How many times has Cody Rhodes won the WWE Championship?",
            a="Three. April 7, 2024 from Roman Reigns, a 378-day reign; August 3, 2025 from John Cena, 159 "
              "days; and March 6, 2026 from Drew McIntyre, 113 days &mdash; 650 days combined. He is not "
              "champion now: Sami Zayn took the title from him in a triple threat at Night of Champions on "
              "June 27, 2026, and CM Punk has held it since July 6, 2026.",
            q_ld="How many times has Cody Rhodes won the WWE Championship?",
            a_ld="Cody Rhodes has held the Undisputed WWE Championship three times: from April 7, 2024, "
                 "won from Roman Reigns, a reign of 378 days; from August 3, 2025, won from John Cena, 159 "
                 "days; and from March 6, 2026, won from Drew McIntyre, 113 days. That is 650 days "
                 "combined. Cody Rhodes is not the champion as of August 2026 — Sami Zayn won the title "
                 "from him in a triple threat at Night of Champions on June 27, 2026, and CM Punk has held "
                 "it since July 6, 2026."),
        dict(
            q="Was Cody Rhodes ever AEW World Champion?",
            a="No. He was the inaugural and record three-time TNT Champion, but he never held AEW&rsquo;s "
              "top title. He built a stipulation into his own storyline barring himself from challenging "
              "for it &mdash; a call he has since said publicly was a mistake. Chris Jericho was "
              "AEW&rsquo;s first World Champion.",
            q_ld="Was Cody Rhodes ever the AEW World Champion?",
            a_ld="No. Cody Rhodes never held the AEW World Championship. He was the inaugural TNT Champion "
                 "and a record three-time holder of that title, but he wrote a stipulation into his own "
                 "storyline barring himself from challenging for the AEW World Championship, a decision he "
                 "has since publicly called a mistake. Chris Jericho was AEW's first World Champion."),
        dict(
            q="Why did Cody Rhodes leave WWE the first time?",
            a="He asked for his release and WWE granted it on May 21, 2016. The stated reason was "
              "creative: he had been playing Stardust since 2014 and could not get the character changed. "
              "He then worked under the single name &ldquo;Cody&rdquo; for four years because WWE held the "
              "trademark on &ldquo;Rhodes,&rdquo; which he did not regain until November 2020.",
            q_ld="Why did Cody Rhodes leave WWE in 2016?",
            a_ld="Cody Rhodes asked for his release and WWE granted it on May 21, 2016. The stated reason "
                 "was creative: he had played the Stardust character since 2014 and could not get it "
                 "changed. Cody Rhodes then worked under the single name Cody for four years because WWE "
                 "held the trademark on the name Rhodes, which he did not regain until November 2020."),
        dict(
            q="What does &ldquo;finish the story&rdquo; mean?",
            a="It refers to Dusty Rhodes never having held a WWE world championship &mdash; a three-time "
              "NWA Worlds Heavyweight Champion who was never given the top belt in the company his son now "
              "headlines. Cody&rsquo;s WrestleMania XL win on April 7, 2024 was booked as closing that gap. "
              "The emotional premise is real biography; the booking around it is storyline.",
            q_ld="What does finishing the story mean for Cody Rhodes?",
            a_ld="It refers to Dusty Rhodes, Cody Rhodes' father, never having held a WWE world "
                 "championship. Dusty Rhodes was a three-time NWA Worlds Heavyweight Champion but was "
                 "never given the top belt in WWE. Cody Rhodes' win over Roman Reigns at WrestleMania XL "
                 "on April 7, 2024 was booked as closing that gap. The emotional premise is real "
                 "biography; the booking built around it is storyline."),
        dict(
            q="Is Cody Rhodes leaving WWE for Hollywood?",
            a="No departure has been announced. He plays Guile in Paramount&rsquo;s <i>Street Fighter</i>, "
              "out October 16, 2026, and took roughly a month off television to shoot it. He is booked on "
              "WWE television through at least September 6, 2026, when he faces Randy Orton at Sunday "
              "Night&rsquo;s Main Event.",
            q_ld="Is Cody Rhodes leaving WWE for Hollywood?",
            a_ld="No. Cody Rhodes has not announced any departure from WWE. He plays Guile in Paramount's "
                 "Street Fighter, released October 16, 2026, and took roughly a month away from television "
                 "to film it. Cody Rhodes is booked on WWE television through at least September 6, 2026, "
                 "when he faces Randy Orton at Sunday Night's Main Event."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Cody Garrett Runnels"),
        dict(label="Born", value="June 30, 1985", sub="age 41"),
        dict(label="Birthplace", value="Disputed",
             sub="Charlotte, NC (Wikipedia) &middot; Marietta, GA (TheSmackDownHotel)"),
        dict(label="Billed from", value="Atlanta, Georgia",
             sub="also Charlotte, Marietta and &ldquo;The Fifth Dimension&rdquo;"),
        dict(label="Height", value="6&#8242;2&#8243;", sub="188 cm"),
        dict(label="Weight", value="222 lb", sub="101 kg &middot; 220 lb per TheSmackDownHotel"),
        dict(label="Debut", value="June 16, 2006", sub="Ohio Valley Wrestling"),
        dict(label="WWE return", value="April 2, 2022", sub="WrestleMania 38"),
        dict(label="Trained by",
             value="Al Snow &middot; Danny Davis &middot; Dusty Rhodes &middot; Dustin Rhodes &middot; "
                   "Randy Orton &middot; Ricky Morton &middot; Shawn Spears"),
        dict(label="Finishers", value="Cross Rhodes &middot; Cody Cutter",
             sub="also the figure-four leglock and Disaster Kick"),
        dict(label="Amateur", value="Georgia state champion, 2003 &amp; 2004", sub="Lassiter High School"),
        dict(label="Family", value="Son of Dusty Rhodes", sub="half-brother of Dustin Rhodes (Goldust)"),
        dict(label="Brand", value="SmackDown"),
        dict(label="Also known as",
             value="The American Nightmare &middot; Cody &middot; Cody Runnels &middot; Stardust "
                   "&middot; Fuego 2"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1985-06-30",
    bornplace="Charlotte, North Carolina, United States",
    nationality="United States",
    height_cm=188,
    weight_kg=101,
    ld=dict(
        alternateName=["Cody Garrett Runnels", "The American Nightmare", "Cody", "Cody Runnels",
                       "Stardust", "Dashing Cody Rhodes", "Fuego 2"],
        award=["Undisputed WWE Championship (3 reigns, 650 combined days)",
               "WWE Intercontinental Championship (2 reigns)",
               "AEW TNT Championship (record 3 reigns, inaugural champion)",
               "ROH World Championship (1 reign)",
               "NWA Worlds Heavyweight Championship (1 reign)",
               "IWGP United States Heavyweight Championship (1 reign)",
               "World Tag Team Championship (2 reigns, 2007–08)",
               "WWE Tag Team Championship (with Goldust, 2013)",
               "Royal Rumble winner (2023, 2024 — back-to-back)",
               "King of the Ring winner (2025)",
               "Crown Jewel Championship (2024, inaugural winner)",
               "WWE Triple Crown Champion (34th)",
               "Pro Wrestling Illustrated 500 number one (2024, 2025)",
               "Wrestling Observer Newsletter Wrestler of the Year (2024)"],
        knowsAbout=["Professional wrestling", "All Elite Wrestling", "The Legacy",
                    "Rhodes wrestling family", "WWE", "Championship wrestling",
                    "Wrestling promotion and booking"],
        description="Cody Rhodes is an American professional wrestler signed to WWE, the son of Dusty "
                    "Rhodes and a three-time Undisputed WWE Champion whose reigns total 650 days. He "
                    "ended Roman Reigns' 1,316-day world title reign at WrestleMania XL on April 7, 2024. "
                    "He is not credited as a Universal Champion in WWE's published title lineage: WWE "
                    "retired the Universal Championship after WrestleMania XL and recognises Roman Reigns "
                    "as its final holder. Rhodes left WWE in 2016, won the ROH World and NWA Worlds "
                    "Heavyweight Championships, co-promoted All In in 2018 and co-founded All Elite "
                    "Wrestling in 2019 as an executive vice president and record three-time TNT Champion, "
                    "then returned to WWE at WrestleMania 38 in 2022. He won the Royal Rumble in 2023 and "
                    "2024, topped the PWI 500 in 2024 and 2025, and was the Wrestling Observer "
                    "Newsletter's 2024 Wrestler of the Year.",
        sameAs=["https://x.com/codyrhodes",
                "https://www.instagram.com/americannightmarecody/",
                "https://en.wikipedia.org/wiki/Cody_Rhodes",
                "https://www.wwe.com/superstars/cody-rhodes"],
    ),
)
