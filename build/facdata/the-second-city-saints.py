# -*- coding: utf-8 -*-
"""The Second City Saints (Ring of Honor, 2003-2005).

Sourcing notes, because this subject has more conflicting records than the two
WWE stables put together:

  * FORMATION. Three independent Wikipedia articles (Second City Saints infobox,
    Ace Steel, Colt Cabana) put the trio's formation at the ROH Night of
    Champions card on March 22, 2003. Wrestle Lore's own CM Punk dossier
    currently dates the group "2002-05"; that is flagged on the page rather than
    quietly overwritten here.
  * THE FORMATION MATCH RESULT. Wikipedia's CM Punk article says Cabana's turn
    "allow[ed] Punk and Steel to win the match". Two independent records of the
    card - thehistoryofwwe.com's ROH 2003 results and a contemporaneous
    match-by-match recap - both have Raven and Cabana WINNING, with Raven
    pinning Ace Steel, and Cabana turning after the bell. The page follows the
    two results archives and says so.
  * THE TAG TITLE REIGNS. thehistoryofwwe.com labels the May 15, 2004 Lexington
    card "Round Robin Challenge II"; Wikipedia, 411Mania and the event
    databases call it "Round Robin Challenge III". Same card, three title
    changes in one night. The page uses III and notes the other label.
  * THE 2011 REUNION. The Second City Saints article calls Money in the Bank
    2011 an "unofficial reunion". The Money in the Bank (2011) article places
    Cabana and Steel with Punk in TMZ photographs on the streets of Chicago
    after the show, not at ringside. Stated as what it is.
"""

DATA = dict(
    slug="the-second-city-saints",
    name="The Second City Saints",
    alternate_names=["Second City Saints", "The Saints"],
    promotion_full="Ring of Honor",
    brand="ROH &middot; 2003&ndash;2005",
    h1_a="The Second City",
    h1_b="Saints",
    founded_iso="2003-03-22",
    dissolved_iso="2005-08-13",
    founding_location="Philadelphia, Pennsylvania",

    title="The Second City Saints: CM Punk, Colt Cabana and Ace Steel in ROH | Wrestle Lore",
    meta_desc=("The Second City Saints, CM Punk's Ring of Honor trio with Colt Cabana and Ace Steel, "
               "March 22 2003 to August 2005. Members, the Raven feud, two ROH Tag Team title "
               "reigns, the Summer of Punk, and the records that disagree."),
    og_title="The Second City Saints (ROH, 2003-2005)",
    og_desc=("Three men from Chicago, a dog collar match with Raven, two tag title reigns and the "
             "Summer of Punk. The stable that built CM Punk before WWE ever saw him."),
    tw_desc=("Punk, Cabana, Ace Steel. Raven, the Briscoes, the Pepsi Plunge and a farewell match "
             "in Chicago Ridge. The full ROH file."),
    ld_page_name="The Second City Saints: members, timeline and championships",
    ld_description=("Professional wrestling stable in Ring of Honor comprising CM Punk, Colt Cabana "
                    "and Ace Steel, active from March 22, 2003 until CM Punk left for World "
                    "Wrestling Entertainment in August 2005."),
    ld_knows=["Professional wrestling", "Ring of Honor", "CM Punk", "Chicago"],

    chips=[
        dict(html="<b>Ring of Honor</b>", gold=False),
        dict(html="<b>Mar&nbsp;22, 2003</b> &ndash; <b>Aug&nbsp;2005</b>", gold=True),
        dict(html="<b>5</b> members and valets", gold=False),
        dict(html="<b>3</b> championship reigns", gold=False),
    ],
    lede=("Three men from Chicago &mdash; the Second City &mdash; who spent two and a half years "
          "making Ring of Honor's Saturday nights matter. A dog collar match with Raven, two tag "
          "title reigns won and lost against the Briscoes, and a farewell in Chicago Ridge that "
          "sent CM Punk to WWE as ROH's reigning-then-dethroned World Champion."),

    tape=[
        dict(label="Promotion", value="Ring of Honor"),
        dict(label="Formed", value="Mar 22, 2003",
             sub="ROH Night of Champions, Philadelphia. Corroborated by the Ace Steel and Colt Cabana articles."),
        dict(label="Members", value="3 (plus 2 valets)"),
        dict(label="Named for", value="Chicago",
             sub="All three men were from Chicago, the Second City."),
        dict(label="Tag reigns", value="2",
             sub="ROH Tag Team Championship, Apr 24 2004 and May 15 2004, both won from the Briscoes."),
        dict(label="World title", value="1",
             sub="CM Punk, Jun 18 &ndash; Aug 12, 2005. The Summer of Punk."),
        dict(label="Ended", value="Aug 13, 2005",
             sub="Punk's final ROH match, a 2-out-of-3 falls loss to Colt Cabana in Chicago Ridge."),
        dict(label="Biggest rival", value="Raven"),
    ],

    overview_lead="Chicago's team, and the two years that made CM Punk a name worth signing.",
    stats=[("29", "months active"), ("3", "core members"), ("3", "title reigns"),
           ("2", "ROH tag reigns"), ("55", "days ROH World Champ")],
    overview=[
        "The Second City Saints were a Ring of Honor stable made up of <b>CM Punk</b>, "
        "<b>Colt Cabana</b> and <b>Ace Steel</b> &mdash; Punk's and Cabana's trainer, and the third "
        "Chicagoan in the group, which is where the name comes from. They formed on "
        "<b>March 22, 2003</b> at ROH's Night of Champions in Philadelphia and effectively ended in "
        "August 2005 when Punk left for WWE. Two valets worked with them: <b>Lucy</b>, and "
        "<b>Traci Brooks</b>, who joined on <b>January 10, 2004</b>.",

        "The group existed to give Punk's straight edge character an opposite number and a home. "
        "ROH in 2003 was a small company selling itself on wrestling quality and long-form "
        "storytelling, and Punk's feud with <b>Raven</b> &mdash; the sober zealot against the "
        "addict, a rivalry Punk rooted publicly in his own alcoholic father &mdash; was one of the "
        "first things it told a story with. The Saints were formed out of that feud, in the most "
        "literal way: Cabana had been Raven's ally, and turned on him.",

        "What it changed was the shape of Punk's career and, arguably, the shape of the American "
        "independent scene. The Saints gave him a tag run to learn in &mdash; two ROH Tag Team "
        "Championship reigns with Cabana across the summer of 2004, both won from the Briscoe "
        "Brothers &mdash; and then a platform for the angle that made him famous. In June 2005, "
        "having already signed with WWE, Punk beat <b>Austin Aries</b> for the ROH World "
        "Championship and spent the summer threatening to take the belt with him. ROH called it the "
        "<b>Summer of Punk</b>, and it is still the template every promotion reaches for when a "
        "champion is about to leave.",

        "It ended in Chicago Ridge on <b>August 13, 2005</b>, the night after Punk dropped the title, "
        "with Cabana beating him two falls to one in a best-of-three at a show called Punk: The "
        "Final Chapter. The Saints were never formally broken up; the man they were built around "
        "simply left, and the other two went their own way.",
    ],

    members_lead=("Three wrestlers and two valets. Wikipedia's member list is the three; the valets "
                  "are recorded in the article body and are included here for completeness."),
    members_note=("Punk and Cabana were both trained by Ace Steel, which is why the stable reads "
                  "like a gym rather than an alliance."),
    members=[
        dict(name="CM Punk", slug="cm-punk", ld_role="Member and leader",
             dates="Mar 22, 2003 &ndash; Aug 13, 2005",
             start_iso="2003-03-22", end_iso="2005-08-13",
             role="Leader &middot; ROH World Champion",
             note=("The straight edge half of the Raven feud and the reason the group existed. Two "
                   "ROH Tag Team Championship reigns with Cabana, then the ROH World Championship "
                   "from June 18 to August 12, 2005 &mdash; the Summer of Punk.")),
        dict(name="Colt Cabana", ld_role="Member",
             dates="Mar 22, 2003 &ndash; 2005",
             start_iso="2003-03-22", end_iso="2005-08-13",
             role="Member &middot; two-time ROH Tag Team Champion",
             sameAs=["https://en.wikipedia.org/wiki/Colt_Cabana"],
             note=("Started as Punk's rival and as Raven's ally, then turned on Raven on March 22, "
                   "2003 and joined them. Punk's tag partner for both ROH Tag Team Championship "
                   "reigns, and his opponent in Punk's last ROH match.")),
        dict(name="Ace Steel", ld_role="Member",
             dates="Mar 22, 2003 &ndash; 2005",
             start_iso="2003-03-22", end_iso="2005-08-13",
             role="Member &middot; trainer to the other two",
             sameAs=["https://en.wikipedia.org/wiki/Ace_Steel"],
             note=("Trained both Punk and Cabana. He was the man Raven pinned in the tag match that "
                   "created the group. Released from a WWE developmental contract on February 4, "
                   "2008, and later a coach in both WWE and AEW.")),
        dict(name="Lucy", ld_role="Valet",
             dates="2003 &ndash; 2004",
             start_iso="2003-03-22",
             role="Valet &middot; manager",
             note=("Worked with the group as its valet. An angle in which she was assaulted set up "
                   "the Saints' war with The Prophecy, which came to a head at Final Battle 2003.")),
        dict(name="Traci Brooks", ld_role="Valet",
             dates="From Jan 10, 2004",
             start_iso="2004-01-10",
             role="Valet &middot; manager",
             note=("Joined the Second City Saints as the group's newest valet at The Battle Lines "
                   "Are Drawn on January 10, 2004.")),
    ],

    timeline_lead=("Ring of Honor ran house shows, not weekly television, so the beats are events "
                   "rather than episodes. Dates and match times below come from ROH results "
                   "archives."),
    timeline=[
        dict(when="Mar 15, 2003", title="Punk vs Raven begins",
             desc="At Expect The Unexpected in Cambridge, Massachusetts, Punk beats the debuting "
                  "Raven by submission with a hammerlock legsweep in a Raven's Rules match at 28:52. "
                  "The feud is built on Punk's straight edge lifestyle against Raven's addiction."),
        dict(when="Mar 22, 2003", title="Formation &middot; Night of Champions",
             desc="In Philadelphia, Raven and Colt Cabana beat Punk and Ace Steel in a Raven's Rules "
                  "match, Raven pinning Steel. After the bell Cabana turns on Raven and sides with "
                  "Punk and Steel. Three men from Chicago: the Second City Saints."),
        dict(when="Jun 14, 2003", title="Night of the Grudges",
             desc="Raven returns to ROH after a three-month absence and teams with B.J. Whitmer "
                  "against Punk and Cabana in a no-disqualification match in Cambridge. Cabana pins "
                  "Whitmer with the Colt .45 at 16:50."),
        dict(when="Jul 19, 2003", title="Death Before Dishonor &middot; dog collar",
             desc="At the Rex Plex in Elizabeth, New Jersey, Punk pins Raven in a dog collar match "
                  "at 18:22 after Cabana interferes behind the downed referee. The most violent "
                  "night of the feud."),
        dict(when="Nov 28, 2003", title="The Conclusion &middot; steel cage",
             desc="In Fairfield, Connecticut, Punk beats Raven in a steel cage match at 17:06 by "
                  "escaping the cage, settling the rivalry."),
        dict(when="Dec 27, 2003", title="Final Battle 2003 &middot; The Prophecy",
             desc="With Raven gone, the Saints turn on The Prophecy, attacking them at Final Battle "
                  "in Philadelphia while investigating an assault on the group's valet Lucy."),
        dict(when="Jan 10, 2004", title="Traci Brooks joins",
             desc="At The Battle Lines Are Drawn, Traci Brooks joins the Second City Saints as the "
                  "group's newest valet."),
        dict(when="Apr 24, 2004", title="First ROH Tag Team Championship",
             desc="At Reborn: Stage Two, at the Frontier Fieldhouse in Chicago Ridge, Illinois, Punk "
                  "and Cabana beat the Briscoe Brothers for the ROH Tag Team Championship, Punk "
                  "pinning Mark Briscoe with the Pepsi Plunge at 19:47. Won at home."),
        dict(when="May 15, 2004", title="Three title changes in one night",
             desc="At Round Robin Challenge III in Lexington, Massachusetts, Dan Maff and B.J. "
                  "Whitmer take the belts from Punk and Cabana at 7:05, the Briscoes take them from "
                  "Maff and Whitmer at 13:24, and Punk and Cabana take them back from the Briscoes "
                  "at 19:14, Cabana pinning Mark with a frog splash."),
        dict(when="Aug 7, 2004", title="Testing the Limit &middot; the reign ends",
             desc="In Philadelphia, Ricky Reyes and Rocky Romero &mdash; the Havana Pitbulls &mdash; "
                  "beat Punk and Cabana for the ROH Tag Team Championship, ending an 84-day second "
                  "reign."),
        dict(when="2004", title="Chicago's Elite",
             desc="Ring of Honor releases Chicago's Elite: The Best of the Second City Saints, the "
                  "compilation that fixed the group in the tape-trading memory of the era."),
        dict(when="Jun 18, 2005", title="Death Before Dishonor III &middot; the Summer of Punk",
             desc="In Morristown, New Jersey, having already signed with WWE, Punk pins ROH World "
                  "Champion Austin Aries with a Pepsi Plunge off the top at 30:29 to win the title. "
                  "He spends the summer promising to take the belt to WWE with him."),
        dict(when="Aug 12, 2005", title="Redemption &middot; the title goes",
             desc="In Dayton, Ohio, James Gibson beats Punk, Christopher Daniels and ROH Pure "
                  "Champion Samoa Joe in an elimination match at 50:41 to take the ROH World "
                  "Championship. Punk's reign ends at 55 days."),
        dict(when="Aug 13, 2005", title="Punk: The Final Chapter",
             desc="Back at Chicago Ridge, Illinois, Colt Cabana beats CM Punk two falls to one in a "
                  "best two-out-of-three falls match at 27:47. Punk's last ROH match before WWE, "
                  "against the man he formed the Saints with."),
    ],

    titles_lead=("Three reigns across two championships. Every one of them was won and lost inside "
                 "Ring of Honor."),
    titles_note=("The ROH World Championship is listed among the group's accomplishments by the "
                 "Second City Saints article, and the dates are not in dispute. Worth saying "
                 "plainly, though: by mid-2005 the Saints were a name more than a working unit, and "
                 "the Summer of Punk was a singles angle."),
    titles=[
        dict(ic="&#9819;", name="ROH Tag Team Championship &mdash; first reign",
             sub="<b>CM Punk &amp; Colt Cabana</b> &middot; won April 24, 2004 at Reborn: Stage Two, "
                 "Frontier Fieldhouse, Chicago Ridge, Illinois, beating the Briscoe Brothers (Punk "
                 "pinned Mark with the Pepsi Plunge at 19:47). Lost May 15, 2004 to Dan Maff and "
                 "B.J. Whitmer.",
             count="21", unit="days"),
        dict(ic="&#9819;", name="ROH Tag Team Championship &mdash; second reign",
             sub="<b>CM Punk &amp; Colt Cabana</b> &middot; regained the same night, May 15, 2004, "
                 "beating the Briscoe Brothers again (Cabana pinned Mark with a frog splash at "
                 "19:14). Lost August 7, 2004 at Testing the Limit in Philadelphia to Ricky Reyes "
                 "and Rocky Romero, the Havana Pitbulls.",
             count="84", unit="days"),
        dict(ic="&#9733;", name="ROH World Championship",
             sub="<b>CM Punk</b> &middot; won June 18, 2005 at Death Before Dishonor III in "
                 "Morristown, New Jersey, pinning Austin Aries at 30:29. Lost August 12, 2005 at "
                 "Redemption in Dayton, Ohio to James Gibson in a four-way elimination match also "
                 "involving Samoa Joe and Christopher Daniels, at 50:41.",
             count="55", unit="days"),
    ],

    moments_lead="Five nights, all of them on a Ring of Honor house show in front of a few hundred people.",
    moments=[
        dict(year="2003", kind="Expect the Unexpected", title="Punk beats the debuting Raven",
             desc="<b>March 15, 2003</b> &middot; Cambridge, Massachusetts &mdash; 28 minutes and 52 "
                  "seconds of a Raven's Rules match that opened the feud the Saints were born out "
                  "of. Punk wins by submission with a hammerlock legsweep."),
        dict(year="2003", kind="Night of Champions", title="Cabana turns, the Saints form",
             desc="<b>March 22, 2003</b> &middot; Philadelphia &mdash; Raven and Cabana beat Punk "
                  "and Ace Steel, Raven pinning Steel. Then Cabana turns on Raven after the bell "
                  "and walks out with the men he just beat. The founding moment."),
        dict(year="2003", kind="Death Before Dishonor", title="The dog collar match",
             desc="<b>July 19, 2003</b> &middot; Rex Plex, Elizabeth, New Jersey &mdash; Punk and "
                  "Raven chained together for 18:22, decided when Cabana interferes with the referee "
                  "down. The feud's most infamous night and one of ROH's early signature brawls."),
        dict(year="2004", kind="Reborn: Stage Two", title="Tag gold at the Frontier Fieldhouse",
             desc="<b>April 24, 2004</b> &middot; Chicago Ridge, Illinois &mdash; Punk pins Mark "
                  "Briscoe with the Pepsi Plunge at 19:47 to win the ROH Tag Team Championship with "
                  "Cabana, in front of the home crowd the group is named after."),
        dict(year="2005", kind="Death Before Dishonor III", title="The Summer of Punk begins",
             desc="<b>June 18, 2005</b> &middot; Morristown, New Jersey &mdash; Punk beats Austin "
                  "Aries for the ROH World Championship at 30:29, having already signed a WWE "
                  "contract, and starts the summer-long angle about walking out with the belt."),
    ],

    legacy_lead="What the Saints left in Chicago, in Ring of Honor, and in everyone who was in it.",
    legacy=[
        "The Second City Saints are the reason CM Punk arrived in WWE already formed. The character "
        "WWE eventually built the Straight Edge Society and The New Nexus around &mdash; the "
        "sanctimonious sober man who talks better than he is supposed to be allowed to &mdash; was "
        "written, tested and refined in Ring of Honor buildings holding a few hundred people, "
        "against Raven, between 2003 and 2005.",

        "The Summer of Punk is the group's other bequest, and it outgrew wrestling's memory of the "
        "Saints entirely. A champion who has signed elsewhere, refusing to drop the belt, is now a "
        "stock storyline; in 2005 it was startling enough that Punk was still being asked about it a "
        "decade later. The pipe bomb promo of <b>June 27, 2011</b> name-checks Ring of Honor "
        "directly &mdash; the WWE angle that made Punk a star was, in part, a callback to this one.",

        "The three members ended up scattered across the modern industry: one of the biggest draws "
        "of the 2010s, one of independent wrestling's most durable self-made careers and one of the "
        "most-travelled coaches in the business. For a stable that existed for twenty-nine months in "
        "front of small crowds, that is a considerable amount of downstream weather.",
    ],
    after=[
        dict(mono="P", era="WWE, Aug 2005", name="CM Punk",
             desc="Left ROH for WWE in August 2005. Won the WWE Championship at Money in the Bank on "
                  "July 17, 2011 and again at Survivor Series on November 20, 2011, holding it 434 "
                  "days."),
        dict(mono="C", era="WWE 2007&ndash;09, AEW 2020", name="Colt Cabana",
             desc="Signed with WWE on April 3, 2007, debuted on the main roster as Scotty Goldman on "
                  "August 15, 2008 and was released on February 20, 2009. Signed with AEW in "
                  "February 2020."),
        dict(mono="A", era="Trainer and coach", name="Ace Steel",
             desc="Released from WWE developmental on February 4, 2008. Signed as a WWE Performance "
                  "Center coach in November 2019, released January 5, 2022, then worked for AEW."),
        dict(mono="R", era="The opponent", name="Raven",
             desc="The rival the Saints were built out of. Punk beat him at Expect the Unexpected, "
                  "in a dog collar match at Death Before Dishonor and in a steel cage at The "
                  "Conclusion, all within 2003."),
    ],

    faq_lead="",
    faq=[
        dict(q="When did the Second City Saints form?",
             a="<b>March 22, 2003</b>, at Ring of Honor's Night of Champions in Philadelphia. Raven "
               "and Colt Cabana beat CM Punk and Ace Steel in a Raven's Rules match; after the bell "
               "Cabana turned on Raven and left with Punk and Steel. Wikipedia's infobox, the Ace "
               "Steel article and the Colt Cabana article all point at that card. "
               "<b>Note:</b> Wrestle Lore's own CM Punk dossier currently dates the group "
               "&ldquo;2002&ndash;05&rdquo;, which the sources do not support.",
             q_ld="When did the Second City Saints form?",
             a_ld="The Second City Saints formed on March 22, 2003 at Ring of Honor's Night of "
                  "Champions in Philadelphia, when Colt Cabana turned on Raven after a tag match "
                  "and aligned with CM Punk and Ace Steel."),
        dict(q="Who was in the Second City Saints?",
             a="Three wrestlers: <b>CM Punk</b>, <b>Colt Cabana</b> and <b>Ace Steel</b>, all from "
               "Chicago, which is where the name comes from &mdash; and Steel had trained the other "
               "two. Two valets worked with the group: <b>Lucy</b>, and <b>Traci Brooks</b>, who "
               "joined at The Battle Lines Are Drawn on January 10, 2004.",
             q_ld="Who was in the Second City Saints?",
             a_ld="The Second City Saints were CM Punk, Colt Cabana and Ace Steel, all from Chicago. "
                  "Ace Steel had trained both Punk and Cabana. Two valets worked with the group: "
                  "Lucy, and Traci Brooks, who joined on January 10, 2004."),
        dict(q="How many championships did the Second City Saints win?",
             a="Three reigns. Punk and Cabana won the <b>ROH Tag Team Championship</b> twice, on "
               "April 24, 2004 at Reborn: Stage Two and again on May 15, 2004 at Round Robin "
               "Challenge III &mdash; both times beating the Briscoe Brothers, and both reigns "
               "ending in defeat (21 days, then 84). Punk then held the <b>ROH World "
               "Championship</b> for 55 days, from June 18 to August 12, 2005.",
             q_ld="How many championships did the Second City Saints win?",
             a_ld="The Second City Saints held three championship reigns. CM Punk and Colt Cabana "
                  "won the ROH Tag Team Championship on April 24, 2004 and again on May 15, 2004, "
                  "holding it 21 and 84 days. CM Punk held the ROH World Championship for 55 days, "
                  "from June 18 to August 12, 2005."),
        dict(q="What was the Summer of Punk?",
             a="Ring of Honor's name for the 2005 storyline in which Punk, having already signed a "
               "WWE contract, won the <b>ROH World Championship</b> from Austin Aries on "
               "<b>June 18, 2005</b> and spent the summer threatening to take the belt to WWE with "
               "him. It ended on <b>August 12, 2005</b>, when James Gibson beat him, Samoa Joe and "
               "Christopher Daniels in a four-way elimination match at Redemption.",
             q_ld="What was the Summer of Punk?",
             a_ld="The Summer of Punk was Ring of Honor's 2005 storyline in which CM Punk, having "
                  "already signed with WWE, won the ROH World Championship from Austin Aries on "
                  "June 18, 2005 and threatened to take the title with him. It ended on August 12, "
                  "2005 when James Gibson won the title in a four-way elimination match."),
        dict(q="Did CM Punk really beat Raven in a dog collar match?",
             a="Yes. <b>July 19, 2003</b>, at Death Before Dishonor at the Rex Plex in Elizabeth, "
               "New Jersey. Punk pinned Raven at 18:22 after Cabana interfered while the referee was "
               "down. It was the third act of a feud that had already run through a Raven's Rules "
               "match in March and a tag match in June, and it was settled for good in a steel cage "
               "at The Conclusion on November 28, 2003.",
             q_ld="Did CM Punk beat Raven in a dog collar match?",
             a_ld="Yes. CM Punk pinned Raven in a dog collar match at Ring of Honor's Death Before "
                  "Dishonor on July 19, 2003 at the Rex Plex in Elizabeth, New Jersey, at 18:22, "
                  "after Colt Cabana interfered while the referee was down."),
        dict(q="How did the Second City Saints end?",
             a="They were never formally broken up. Punk left ROH for WWE in <b>August 2005</b>, "
               "wrestling his last match on <b>August 13, 2005</b> at Punk: The Final Chapter in "
               "Chicago Ridge &mdash; a best two-out-of-three falls match he lost 2-1 to Colt "
               "Cabana. With the man the stable was built around gone, it simply stopped.",
             q_ld="How did the Second City Saints end?",
             a_ld="The Second City Saints ended when CM Punk left Ring of Honor for WWE in August "
                  "2005. His final ROH match was on August 13, 2005 at Punk: The Final Chapter in "
                  "Chicago Ridge, Illinois, a best two-out-of-three falls match he lost 2-1 to Colt "
                  "Cabana. The group was never formally disbanded."),
    ],

    sources_lead="Every date and match time on this page traces to one of these.",
    sources_note=("Three genuine conflicts came up while building this page and none of them are "
                  "settled quietly. <b>One:</b> Wikipedia's CM Punk article says Cabana's turn let "
                  "Punk and Steel win the March 22, 2003 tag match; two independent results archives "
                  "have Raven and Cabana winning, with Raven pinning Ace Steel and the turn coming "
                  "after the bell &mdash; this page follows the archives. <b>Two:</b> "
                  "thehistoryofwwe.com labels the May 15, 2004 Lexington card &ldquo;Round Robin "
                  "Challenge II&rdquo;; Wikipedia, 411Mania and the event databases call it "
                  "&ldquo;Round Robin Challenge III&rdquo;. Same card. <b>Three:</b> the Second City "
                  "Saints article calls Money in the Bank 2011 an unofficial reunion; the Money in "
                  "the Bank (2011) article puts Cabana and Steel with Punk in TMZ photographs on the "
                  "streets of Chicago after the show, not at ringside."),
    sources=[
        dict(k="Wikipedia", v="The Second City Saints",
             href="https://en.wikipedia.org/wiki/The_Second_City_Saints"),
        dict(k="Wikipedia", v="CM Punk",
             href="https://en.wikipedia.org/wiki/CM_Punk"),
        dict(k="Wikipedia", v="Ace Steel",
             href="https://en.wikipedia.org/wiki/Ace_Steel"),
        dict(k="Wikipedia", v="Colt Cabana",
             href="https://en.wikipedia.org/wiki/Colt_Cabana"),
        dict(k="The History of WWE", v="ROH World Tag Team Title history",
             href="https://thehistoryofwwe.com/ring-of-honor-tag-team-title-history/"),
        dict(k="The History of WWE", v="Ring of Honor 2003 results",
             href="https://thehistoryofwwe.com/ring-of-honor-results-2003/"),
        dict(k="The History of WWE", v="Ring of Honor 2005 results",
             href="https://thehistoryofwwe.com/ring-of-honor-results-2005/"),
        dict(k="411Mania", v="ROH Round Robin Challenge III, May 15, 2004",
             href="https://411mania.com/wrestling/roh-round-robin-challenge-iii-may-15-2004-lexington-massachusetts/"),
    ],

    explore=[
        dict(href="/wrestlers/cm-punk/", kicker="Dossier", name="CM Punk",
             desc="The full record, from IWA Mid-South and Ring of Honor to the pipe bomb and back."),
        # Joe vs Punk II, October 16, 2004 at the Frontier Fieldhouse in Chicago
        # Ridge - a Saints-era ROH World Championship match that Wrestle Lore
        # already has a page for. Cross-link only; no new claim is made here,
        # and link_for()/href_for() drop it to nothing if the page ever moves.
        dict(href="/matches/samoa-joe-vs-cm-punk-roh-2004/", kicker="Match",
             name="Samoa Joe vs CM Punk", desc="ROH World Title Classic, 2004."),
        dict(href="/factions/straight-edge-society/", kicker="Next stable",
             name="The Straight Edge Society",
             desc="WWE, 2009&ndash;10. The Raven feud's argument, restaged with a congregation."),
        dict(href="/factions/the-new-nexus/", kicker="Next stable", name="The New Nexus",
             desc="WWE, 2011. Where the pipe bomb name-checked the promotion this page is about."),
        dict(href="/factions/", kicker="Index", name="All factions",
             desc="Every stable filed on Wrestle Lore."),
    ],

    hub_era="ROH &middot; 2003&ndash;05",
    hub_members="CM Punk, Colt Cabana, Ace Steel",
    hub_desc=("Three men from Chicago who made Ring of Honor's early Saturday nights matter: the "
              "Raven feud, two tag title reigns off the Briscoes, and the Summer of Punk."),
)
