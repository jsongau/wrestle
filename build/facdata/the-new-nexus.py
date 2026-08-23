# -*- coding: utf-8 -*-
"""The New Nexus (WWE, 2011).

Sourcing notes:

  * This is the CM Punk-led Nexus, not Wade Barrett's. Punk was revealed as
    leader on the January 3, 2011 Raw and the group was renamed to distance
    itself from Barrett.
  * The end date is genuinely contested inside a single source. Wikipedia's
    Nexus article says the WWE Championship "was finally held by the stable on
    their last night of existence" (Money in the Bank, July 17, 2011) and also
    says Otunga and McGillicutty "worked as a tag team with the New Nexus banner
    until August 1, 2011, and continued without the banner until August 22,
    2011, when the group disbanded". dissolved_iso uses the explicit
    disbandment date; the July reading is stated on the page and in the FAQ.
  * The WWE Championship entry in the Championships section is a judgement call
    that is spelled out rather than hidden: Punk won it on his last night with
    the group and walked out of the building with it.
"""

DATA = dict(
    slug="the-new-nexus",
    name="The New Nexus",
    alternate_names=["New Nexus", "The Nexus"],
    promotion_full="World Wrestling Entertainment",
    brand="WWE &middot; 2011",
    h1_a="The New",
    h1_b="Nexus",
    founded_iso="2011-01-03",
    dissolved_iso="2011-08-22",
    founding_location="WWE Raw",

    title="The New Nexus: CM Punk's WWE stable, 2011 | Wrestle Lore",
    meta_desc=("The New Nexus, the CM Punk-led version of The Nexus from January 3, 2011. Members, "
               "the kendo-stick initiation, the Randy Orton feud, the WWE Tag Team Championship "
               "reign, the pipe bomb, and the argument over when it actually ended."),
    og_title="The New Nexus (WWE, 2011)",
    og_desc=("CM Punk took someone else's invasion army, made them earn their armbands with kendo "
             "sticks, and used the last seven months of it to become the most talked-about man in "
             "wrestling."),
    tw_desc=("Punk, Otunga, McGillicutty, Harris, Ryan. Two championships, one pipe bomb, and a "
             "disbandment date nobody agrees on."),
    ld_page_name="The New Nexus: members, timeline and championships",
    ld_description=("Professional wrestling stable in WWE, the CM Punk-led continuation of The "
                    "Nexus, active from January 3, 2011 to August 22, 2011, comprising CM Punk, "
                    "David Otunga, Michael McGillicutty, Husky Harris and Mason Ryan."),
    ld_knows=["Professional wrestling", "WWE Raw", "The Nexus", "CM Punk"],

    chips=[
        dict(html="<b>WWE</b> &middot; Raw", gold=False),
        dict(html="<b>Jan&nbsp;3</b> &ndash; <b>Aug&nbsp;22, 2011</b>", gold=True),
        dict(html="<b>7</b> members", gold=False),
        dict(html="<b>2</b> championships", gold=False),
    ],
    lede=("Wade Barrett built The Nexus to invade WWE. CM Punk took it off him on the first Raw of "
          "2011, made the survivors beat each other with kendo sticks to keep their armbands, and "
          "spent seven months using someone else's army as the backdrop for his own exit. It ended "
          "with him walking out of a Chicago arena holding the WWE Championship."),

    tape=[
        dict(label="Promotion", value="WWE (Raw)"),
        dict(label="Active", value="Jan 3 &ndash; Aug 22, 2011",
             sub="Punk revealed as leader Jan 3; tag titles lost and group disbanded Aug 22."),
        dict(label="Leader", value='<a href="/wrestlers/cm-punk/">CM Punk</a>'),
        dict(label="Members", value="7",
             sub="Includes Gabriel and Slater, who lasted one week before leaving to form The Corre."),
        dict(label="Titles won", value="2",
             sub="WWE Tag Team Championship (Otunga &amp; McGillicutty) and the WWE Championship (Punk)."),
        dict(label="Predecessor", value="The Nexus"),
        dict(label="Splinter group", value="The Corre"),
        dict(label="Ended by", value="Air Boom"),
    ],

    overview_lead="A hostile takeover of a hostile takeover.",
    stats=[("7", "months active"), ("7", "members"), ("2", "titles"),
           ("91", "days tag champs"), ("1", "pipe bomb")],
    overview=[
        "The New Nexus was the second and final version of The Nexus, the WWE stable that had spent "
        "2010 as an invasion angle under <b>Wade Barrett</b>. On the <b>January 3, 2011</b> episode "
        "of Raw the group announced it was under &ldquo;new management&rdquo; and revealed "
        "<b>CM Punk</b> as its leader, a position he took after Barrett lost a number one "
        "contendership steel cage match involving Randy Orton and Sheamus &mdash; Punk teased "
        "helping Barrett escape the cage, then knocked him off it. Barrett was exiled and the group "
        "was renamed to put distance between itself and him.",

        "It existed because both halves of it needed rescuing. The Nexus had lost its central feud "
        "with John Cena and its threat had gone flat; Punk had come off the Straight Edge Society "
        "in September 2010 with no stable and no title. Handing Punk a ready-made crew solved both "
        "problems at once, and he immediately rewrote the group in his own image. On the "
        "<b>January 10, 2011</b> Raw he made the members prove loyalty by hitting each other with "
        "kendo sticks. <b>Justin Gabriel</b> and <b>Heath Slater</b> refused, walked, and joined "
        "Barrett and Ezekiel Jackson on SmackDown as <b>The Corre</b>. "
        "<b>Husky Harris</b>, <b>Michael McGillicutty</b> and <b>David Otunga</b> took the beating "
        "and stayed.",

        "What it changed, in the end, was Punk's career rather than WWE's landscape. The stable "
        "spent the spring being systematically dismantled by <b>Randy Orton</b>, who beat every "
        "member in turn and punted several of them off television, and who beat Punk himself at "
        "<b>WrestleMania XXVII</b> on April 3 and again in a Last Man Standing match at Extreme "
        "Rules on May 1. Losing that consistently to one man is usually the end of a group. Here it "
        "set up the alternative: if the Nexus could not get Punk over as a conqueror, his contract "
        "expiring could.",

        "On the <b>June 27, 2011</b> Raw, Punk sat cross-legged on the entrance stage and delivered "
        "the worked-shoot promo now universally called the <b>pipe bomb</b>, naming Ring of Honor "
        "and New Japan as places he might take the WWE Championship when his deal ran out. Three "
        "weeks later, at Money in the Bank in his home town, he beat John Cena for the title and "
        "left the building with it. The New Nexus is the only stable in WWE history whose defining "
        "moment is its leader quitting.",
    ],

    members_lead=("Seven men wore the armband under Punk. Two of them for exactly one week."),
    members_note=("Wade Barrett founded The Nexus and led it through 2010, but was exiled on "
                  "January 3, 2011 and never wore the New Nexus banner. He is not listed here."),
    members=[
        dict(name="CM Punk", slug="cm-punk", ld_role="Leader",
             dates="Jan 3 &ndash; Jul 17, 2011",
             start_iso="2011-01-03", end_iso="2011-07-17",
             role="Leader &middot; the takeover",
             note=("Took the group from Wade Barrett, imposed the kendo-stick initiation, and used "
                   "his last seven months under contract to build the pipe-bomb angle. Won the WWE "
                   "Championship on his final night with the stable.")),
        dict(name="David Otunga", ld_role="Member",
             dates="Jan 3 &ndash; Aug 22, 2011",
             start_iso="2011-01-03", end_iso="2011-08-22",
             role="Member &middot; WWE Tag Team Champion",
             sameAs=["https://en.wikipedia.org/wiki/David_Otunga"],
             note=("Passed Punk's initiation and stayed to the end. Won the WWE Tag Team "
                   "Championship with McGillicutty on the May 23, 2011 Raw and held it 91 days. A "
                   "Harvard Law graduate, which the commentary never stopped mentioning.")),
        dict(name="Michael McGillicutty", ld_role="Member",
             dates="Jan 3 &ndash; Aug 22, 2011",
             start_iso="2011-01-03", end_iso="2011-08-22",
             role="Member &middot; WWE Tag Team Champion",
             sameAs=["https://en.wikipedia.org/wiki/Curtis_Axel"],
             note=("Third-generation wrestler, son of Mr. Perfect. Held the WWE Tag Team "
                   "Championship with Otunga from May 23 to August 22, 2011 &mdash; the longest "
                   "single thing the New Nexus actually accomplished.")),
        dict(name="Husky Harris", ld_role="Member",
             dates="Jan 3 &ndash; Jan 31, 2011",
             start_iso="2011-01-03", end_iso="2011-01-31",
             role="Member &middot; written off in four weeks",
             sameAs=["https://en.wikipedia.org/wiki/Bray_Wyatt"],
             note=("Passed the kendo-stick initiation and was gone by the end of the month: Randy "
                   "Orton punted him on the January 31, 2011 Raw and he was sent back to "
                   "developmental. He returned in 2012 as Bray Wyatt.")),
        dict(name="Mason Ryan", ld_role="Member",
             dates="Jan 17 &ndash; Jun 27, 2011",
             start_iso="2011-01-17", end_iso="2011-06-27",
             role="Member &middot; the enforcer",
             note=("Joined on the January 17, 2011 Raw by attacking both Punk and John Cena during "
                   "their match, after which Punk handed him a Nexus armband. Left the group on the "
                   "June 27, 2011 Raw when an injury was announced.")),
        dict(name="Justin Gabriel", ld_role="Former member",
             dates="Jan 3 &ndash; Jan 10, 2011",
             start_iso="2011-01-03", end_iso="2011-01-10",
             role="Member &middot; one week",
             note=("Refused to hit his own stablemates with a kendo stick at Punk's initiation and "
                   "walked out the same night, joining Wade Barrett and Ezekiel Jackson on "
                   "SmackDown as The Corre.")),
        dict(name="Heath Slater", ld_role="Former member",
             dates="Jan 3 &ndash; Jan 10, 2011",
             start_iso="2011-01-03", end_iso="2011-01-10",
             role="Member &middot; one week",
             note=("Left alongside Gabriel for the same reason and on the same night. The Corre "
                   "would spend the spring feuding with the group they had just quit.")),
    ],

    timeline_lead="Seven months, start to finish, on Raw.",
    timeline=[
        dict(when="Jan 3, 2011", title="The takeover",
             desc="On Raw, The Nexus announces it is under &ldquo;new management&rdquo; and CM Punk "
                  "is revealed as leader. Punk had teased helping Wade Barrett escape a number one "
                  "contendership steel cage match, then knocked him off the cage. Barrett is exiled "
                  "and the group is renamed The New Nexus."),
        dict(when="Jan 10, 2011", title="The kendo stick initiation",
             desc="Punk orders the members to hit each other with kendo sticks to prove loyalty. "
                  "Justin Gabriel and Heath Slater refuse and leave, joining Barrett and Ezekiel "
                  "Jackson on SmackDown as The Corre. Husky Harris, Michael McGillicutty and David "
                  "Otunga take the beating and pass."),
        dict(when="Jan 17, 2011", title="Mason Ryan gets an armband",
             desc="Ryan interferes in Punk's match with John Cena, attacking both men. Punk hands "
                  "him a Nexus armband on the spot."),
        dict(when="Jan 30, 2011", title="Royal Rumble",
             desc="The New Nexus and The Corre are both in the 40-man Royal Rumble match. The New "
                  "Nexus costs Randy Orton his rematch clause for The Miz's WWE Championship, "
                  "starting the feud that will define the group's spring."),
        dict(when="Jan 31, 2011", title="Orton punts Husky Harris",
             desc="On Raw, Orton punts Harris in the head and writes him off television. Harris "
                  "returns to developmental; he will come back in 2012 as Bray Wyatt."),
        dict(when="Feb &ndash; Mar 2011", title="Orton clears the room",
             desc="Over the following weeks Orton beats every member of The New Nexus in turn, "
                  "causing several storyline injuries by punting them. By WrestleMania the leader "
                  "is nearly the only one left standing."),
        dict(when="Apr 3, 2011", title="WrestleMania XXVII",
             desc="Randy Orton defeats CM Punk. The group's biggest stage and its biggest loss."),
        dict(when="May 1, 2011", title="Extreme Rules",
             desc="Orton beats Punk again, this time in a Last Man Standing match, closing out the "
                  "feud with the New Nexus on the wrong end of it."),
        dict(when="May 23, 2011", title="Tag titles &middot; the one real win",
             desc="On Raw, with a distraction from The New Nexus, McGillicutty and Otunga beat Big "
                  "Show and Kane for the WWE Tag Team Championship."),
        dict(when="Jun 20, 2011", title="Power to the People",
             desc="Punk was to be named number one contender for Cena's WWE Championship; instead "
                  "he is put in a triple threat with Alberto Del Rio and Rey Mysterio under a "
                  "fan-voted falls-count-anywhere stipulation. Punk wins, then reveals his WWE "
                  "contract expires at Money in the Bank."),
        dict(when="Jun 27, 2011", title="The pipe bomb",
             desc="Mason Ryan's injury is announced and he leaves the group. The same night Punk "
                  "sits cross-legged on the stage and delivers the worked-shoot promo he called a "
                  "pipe bomb, explicitly naming Ring of Honor and New Japan Pro-Wrestling as places "
                  "he might take the title."),
        dict(when="Jul 17, 2011", title="Money in the Bank",
             desc="At the Allstate Arena in Rosemont, Illinois, Punk beats John Cena for the WWE "
                  "Championship, blows a kiss at Vince McMahon and leaves the building with the "
                  "belt. Some sources treat this as the night the New Nexus ends."),
        dict(when="Jul 25, 2011", title="A new champion is crowned",
             desc="With Punk gone, WWE runs a tournament on Raw. Rey Mysterio wins the WWE "
                  "Championship and loses it to John Cena the same night. Punk returns at the end "
                  "of the show, still holding the belt he left with."),
        dict(when="Aug 1, 2011", title="The banner comes down",
             desc="Otunga and McGillicutty stop working under the New Nexus name, continuing as a "
                  "tag team without it."),
        dict(when="Aug 22, 2011", title="Disbandment",
             desc="Otunga and McGillicutty lose the WWE Tag Team Championship to Kofi Kingston and "
                  "Evan Bourne, after 91 days. With the belts gone, the group is finished."),
    ],

    titles_lead="Two championships, both won in the group's last three months.",
    titles_note=("The WWE Championship is listed because Punk won it on his final night with the "
                 "stable and left the arena holding it, which is the reading the source takes: the "
                 "title was &ldquo;finally held by the stable on their last night of existence.&rdquo; "
                 "It was not defended for the group, and WWE crowned a new champion eight days "
                 "later. Count it or discount it &mdash; the dates are here either way."),
    titles=[
        dict(ic="&#9819;", name="WWE Tag Team Championship",
             sub="<b>Michael McGillicutty &amp; David Otunga</b> &middot; won May 23, 2011 on Raw, "
                 "beating Big Show and Kane after a New Nexus distraction. Lost August 22, 2011 to "
                 "Kofi Kingston and Evan Bourne (Air Boom). The only title the group ever defended.",
             count="91", unit="days"),
        dict(ic="&#9733;", name="WWE Championship",
             sub="<b>CM Punk</b> &middot; won July 17, 2011 at Money in the Bank, Allstate Arena, "
                 "Rosemont, Illinois, beating John Cena with Cena's job on the line. Punk left the "
                 "building with the belt as his contract expired; WWE crowned a new champion in a "
                 "tournament on the July 25 Raw.",
             count="8", unit="days as recognised"),
    ],

    moments_lead="Five nights that carry the run. Four of them are promos or angles, not matches.",
    moments=[
        # Moment titles are escaped (they may become links), so this one uses
        # literal typographic quotes rather than &ldquo;/&rdquo; entities.
        dict(year="2011", kind="Raw", title="“Under new management”",
             desc="<b>January 3, 2011</b> &middot; Raw &mdash; after months of teasing, The Nexus "
                  "reveals its new leader is the man who had just knocked Wade Barrett off a steel "
                  "cage. The invasion angle becomes a Punk vehicle in one segment."),
        dict(year="2011", kind="Raw", title="The kendo stick initiation",
             desc="<b>January 10, 2011</b> &middot; Raw &mdash; Punk makes the group beat each other "
                  "to keep their armbands. Gabriel and Slater refuse and leave to form The Corre; "
                  "Harris, McGillicutty and Otunga take it. The Straight Edge Society's "
                  "head-shaving ritual, reissued as violence."),
        dict(year="2011", kind="WrestleMania XXVII", title="Randy Orton beats CM Punk",
             desc="<b>April 3, 2011</b> &mdash; the New Nexus's WrestleMania match, and its loss. "
                  "Orton had spent three months punting the stable's members off television; here "
                  "he finished with the leader."),
        dict(year="2011", kind="Raw", title="The pipe bomb",
             desc="<b>June 27, 2011</b> &middot; Raw &mdash; Punk sits cross-legged on the stage and "
                  "delivers a worked-shoot promo about his expiring contract, naming Ring of Honor "
                  "and New Japan on WWE television. The most consequential promo of the era, cut "
                  "while nominally leading this stable."),
        # The sitemap advertises /matches/cm-punk-vs-cena-mitb-2011/, so the slug is
        # declared here. link_for() stats the filesystem: if that page ever lands the
        # title becomes a link with no edit here, and until then it stays plain text.
        dict(year="2011", kind="Money in the Bank", match_slug="cm-punk-vs-cena-mitb-2011",
             title="CM Punk beats John Cena in Chicago",
             desc="<b>July 17, 2011</b> &middot; Allstate Arena, Rosemont, Illinois &mdash; Punk "
                  "wins the WWE Championship in front of his home crowd, kicks Alberto Del Rio "
                  "before he can cash in, blows a kiss at Vince McMahon and disappears through the "
                  "crowd with the belt."),
    ],

    legacy_lead="A stable remembered for what one member did on the way out of it.",
    legacy=[
        "The New Nexus is the rare stable whose legacy runs entirely through its leader. As a group "
        "it lost its WrestleMania match, lost the rematch, lost most of its members to Randy Orton's "
        "punt, and won exactly one championship it could defend. What it did do was give CM Punk "
        "seven months of weekly television as the most visible man on Raw at precisely the moment "
        "his contract was running down &mdash; and that timing is the whole story.",

        "The pipe bomb on <b>June 27, 2011</b> and the Money in the Bank main event three weeks "
        "later reset Punk's standing permanently. He won the WWE Championship back at Survivor "
        "Series on <b>November 20, 2011</b> and held it for <b>434 days</b> until The Rock beat him "
        "at the Royal Rumble on January 27, 2013 &mdash; the tenth-longest world title reign in WWE "
        "history. None of that happens on that schedule without the runway the New Nexus provided.",

        "The supporting cast did better out of it than the group's record suggests. Husky Harris "
        "went back to developmental and returned as one of the most distinctive characters of the "
        "decade. McGillicutty was repackaged and put with Paul Heyman. Otunga became a broadcaster. "
        "The New Nexus was a bad stable that produced good careers.",
    ],
    after=[
        dict(mono="P", era="After July 2011", name="CM Punk",
             desc="Regained the WWE Championship at Survivor Series on November 20, 2011 and held it "
                  "434 days, losing to The Rock at the Royal Rumble on January 27, 2013."),
        dict(mono="H", era="Repackaged 2012", name="Husky Harris",
             desc="Punted off television on January 31, 2011 and returned to FCW. Repackaged as "
                  "Bray Wyatt in April 2012."),
        dict(mono="M", era="Repackaged 2013", name="Michael McGillicutty",
             desc="Became Curtis Axel on the May 20, 2013 Raw with Paul Heyman as manager, and won "
                  "the Intercontinental Championship at Payback on June 16, 2013."),
        dict(mono="O", era="Broadcast booth", name="David Otunga",
             desc="A Harvard Law graduate from 2006, he moved into WWE commentary from June 2016 "
                  "and was released on April 15, 2020."),
    ],

    faq_lead="",
    faq=[
        dict(q="What was the difference between The Nexus and The New Nexus?",
             a="Leadership. The Nexus was <b>Wade Barrett's</b> invasion group through 2010. On the "
               "<b>January 3, 2011</b> Raw, Barrett was exiled after CM Punk knocked him off a steel "
               "cage, Punk was revealed as the new leader, and the group was renamed The New Nexus "
               "specifically to distance itself from the old management. Same armbands, different "
               "religion.",
             q_ld="What was the difference between The Nexus and The New Nexus?",
             a_ld="The Nexus was Wade Barrett's invasion stable through 2010. On the January 3, 2011 "
                  "episode of Raw, Barrett was exiled and CM Punk was revealed as the new leader, "
                  "and the group was renamed The New Nexus to distance itself from Barrett."),
        dict(q="Who was in The New Nexus?",
             a="CM Punk led it. <b>David Otunga</b> and <b>Michael McGillicutty</b> lasted the whole "
               "run; <b>Husky Harris</b> passed the initiation and was written off by January 31; "
               "<b>Mason Ryan</b> joined on January 17 and left in June with an injury. "
               "<b>Justin Gabriel</b> and <b>Heath Slater</b> were members for exactly one week "
               "before refusing the initiation and leaving to form The Corre.",
             q_ld="Who was in The New Nexus?",
             a_ld="The New Nexus was led by CM Punk and included David Otunga, Michael McGillicutty, "
                  "Husky Harris and Mason Ryan. Justin Gabriel and Heath Slater were members for one "
                  "week, from January 3 to January 10, 2011, before leaving to form The Corre."),
        dict(q="What championships did The New Nexus win?",
             a="Two. <b>McGillicutty and Otunga</b> won the WWE Tag Team Championship on the "
               "<b>May 23, 2011</b> Raw from Big Show and Kane, and held it 91 days until Kofi "
               "Kingston and Evan Bourne took it on August 22. <b>CM Punk</b> won the WWE "
               "Championship at Money in the Bank on <b>July 17, 2011</b> &mdash; on his last night "
               "with the group, walking out of the building with the belt as his contract expired.",
             q_ld="What championships did The New Nexus win?",
             a_ld="The New Nexus won two championships. Michael McGillicutty and David Otunga won the "
                  "WWE Tag Team Championship on the May 23, 2011 episode of Raw and held it for 91 "
                  "days until August 22, 2011. CM Punk won the WWE Championship at Money in the Bank "
                  "on July 17, 2011, on his last night with the group."),
        dict(q="When did The New Nexus actually disband?",
             a="Sources disagree, and the same source disagrees with itself. One reading ends the "
               "group on <b>July 17, 2011</b>, the night Punk left with the WWE Championship &mdash; "
               "described as &ldquo;their last night of existence&rdquo;. The other follows Otunga "
               "and McGillicutty, who used the New Nexus banner until <b>August 1, 2011</b>, "
               "continued without it, and lost the tag titles on <b>August 22, 2011</b>, which is "
               "given as the disbandment. This page uses August 22 for the group and July 17 for "
               "Punk, because both are true of different things.",
             q_ld="When did The New Nexus disband?",
             a_ld="Sources give two dates. CM Punk left on July 17, 2011 after winning the WWE "
                  "Championship at Money in the Bank, which some accounts call the group's last "
                  "night. David Otunga and Michael McGillicutty used the New Nexus banner until "
                  "August 1, 2011 and the group is recorded as disbanding on August 22, 2011, when "
                  "they lost the WWE Tag Team Championship."),
        dict(q="Was the pipe bomb promo a New Nexus segment?",
             a="Technically yes, which is the joke. Punk delivered it on the <b>June 27, 2011</b> "
               "Raw, while still the leader of the stable, on the same night Mason Ryan's injury was "
               "announced and he left the group. The promo has nothing to do with the Nexus and "
               "everything to do with Punk's expiring contract &mdash; the stable was the furniture "
               "he happened to be standing in front of.",
             q_ld="Was the pipe bomb promo a New Nexus segment?",
             a_ld="CM Punk delivered the pipe bomb promo on the June 27, 2011 episode of Raw while "
                  "he was still the leader of The New Nexus, on the same night Mason Ryan left the "
                  "group with an injury. The promo concerned Punk's expiring WWE contract rather "
                  "than the stable itself."),
        dict(q="Why did Justin Gabriel and Heath Slater leave after one week?",
             a="Punk's initiation. On the <b>January 10, 2011</b> Raw he ordered the members to hit "
               "each other with kendo sticks to prove loyalty. Gabriel and Slater refused, left, and "
               "joined Wade Barrett and Ezekiel Jackson on SmackDown as <b>The Corre</b> &mdash; "
               "which promptly became one of The New Nexus's rivals.",
             q_ld="Why did Justin Gabriel and Heath Slater leave The New Nexus?",
             a_ld="On the January 10, 2011 episode of Raw, CM Punk ordered the members of The New "
                  "Nexus to hit each other with kendo sticks as an initiation. Justin Gabriel and "
                  "Heath Slater refused and left the group, joining Wade Barrett and Ezekiel Jackson "
                  "on SmackDown as The Corre."),
    ],

    sources_lead="Every date on this page traces to one of these.",
    sources_note=("The disbandment date is the one point where the sourcing genuinely pulls in two "
                  "directions; both readings are stated above rather than resolved silently."),
    sources=[
        dict(k="Wikipedia", v="The Nexus (professional wrestling)",
             href="https://en.wikipedia.org/wiki/The_Nexus_(professional_wrestling)"),
        dict(k="Wikipedia", v="Money in the Bank (2011)",
             href="https://en.wikipedia.org/wiki/Money_in_the_Bank_(2011)"),
        dict(k="Wikipedia", v="CM Punk",
             href="https://en.wikipedia.org/wiki/CM_Punk"),
        dict(k="Wikipedia", v="Curtis Axel",
             href="https://en.wikipedia.org/wiki/Curtis_Axel"),
        dict(k="Wikipedia", v="David Otunga",
             href="https://en.wikipedia.org/wiki/David_Otunga"),
        dict(k="Wikipedia", v="Bray Wyatt",
             href="https://en.wikipedia.org/wiki/Bray_Wyatt"),
    ],

    explore=[
        dict(href="/wrestlers/cm-punk/", kicker="Dossier", name="CM Punk",
             desc="The full record, including the 434-day title reign that started four months after "
                  "this group ended."),
        dict(href="/factions/straight-edge-society/", kicker="Previous stable",
             name="The Straight Edge Society",
             desc="The WWE cult Punk ran before this one, and where the initiation ritual came from."),
        dict(href="/factions/the-second-city-saints/", kicker="First stable",
             name="The Second City Saints",
             desc="Ring of Honor, 2003&ndash;05 &mdash; one of the two promotions Punk named in the "
                  "pipe bomb."),
        dict(href="/factions/", kicker="Index", name="All factions",
             desc="Every stable filed on Wrestle Lore."),
    ],

    hub_era="WWE &middot; 2011",
    hub_members="CM Punk, David Otunga, Michael McGillicutty, Husky Harris, Mason Ryan",
    hub_desc=("Punk seized Wade Barrett's invasion army, made the survivors earn their armbands with "
              "kendo sticks, and used its last night to walk out of Chicago with the WWE "
              "Championship."),
)
