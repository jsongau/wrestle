# -*- coding: utf-8 -*-
"""The Straight Edge Society (WWE, 2009-2010).

Sourcing notes for anyone editing this file:

  * Formation and dissolution dates come from the Wikipedia infobox
    (November 27, 2009 - September 3, 2010) and are corroborated by the
    article body: the November 27 SmackDown "conversion" of Festus into
    Luke Gallows, and the September 3 SmackDown where Punk hit Gallows
    with a GTS and walked out.
  * Serena's release date is the one real conflict on this subject. Her
    own article and the Pro Wrestling fandom entry both say August 20,
    2010; the Straight Edge Society article describes WWE.com announcing
    it during the August 27 SmackDown. Both are on the page, framed as
    what they are, rather than one being picked silently.
  * The group held NO championship. Punk's World Heavyweight title reign
    ended at Hell in a Cell on October 4, 2009, seven weeks before the
    stable existed. The Championships section is therefore dropped and
    the sections renumber. Do not "fix" this by back-dating the group.
  * Darren Young is NOT a member. He was Punk's NXT season-one rookie and
    backed out before the head-shaving initiation. He appears in the
    timeline only.
"""

DATA = dict(
    slug="straight-edge-society",
    name="The Straight Edge Society",
    alternate_names=["SES", "The Straight Edge Society"],
    promotion_full="World Wrestling Entertainment",
    brand="WWE &middot; 2009&ndash;2010",
    h1_a="The Straight Edge",
    h1_b="Society",
    founded_iso="2009-11-27",
    dissolved_iso="2010-09-03",
    founding_location="WWE SmackDown",

    title="The Straight Edge Society: CM Punk's WWE cult, 2009-2010 | Wrestle Lore",
    meta_desc=("The Straight Edge Society, CM Punk's WWE stable with Luke Gallows, Serena and "
               "Joey Mercury. Formed November 27, 2009, disbanded September 3, 2010: members, "
               "timeline, the Rey Mysterio hair-vs-mask feud, and why it never won a title."),
    og_title="The Straight Edge Society (WWE, 2009-2010)",
    og_desc=("CM Punk's congregation of sobriety: Luke Gallows, Serena and Joey Mercury, the "
             "shaved heads, and the Rey Mysterio feud that ended with Punk's own head on the floor."),
    tw_desc=("Punk, Gallows, Serena, Mercury. Ten months, four shaved heads, zero championships. "
             "The full file."),
    ld_page_name="The Straight Edge Society: members, timeline and legacy",
    ld_description=("Professional wrestling stable in WWE led by CM Punk from November 27, 2009 "
                    "to September 3, 2010, comprising Luke Gallows, Serena and Joey Mercury, "
                    "built around a villainous reading of the straight edge subculture."),
    ld_knows=["Professional wrestling", "Straight edge", "WWE SmackDown", "CM Punk"],

    # ---- hero ----
    chips=[
        dict(html="<b>WWE</b> &middot; SmackDown", gold=False),
        dict(html="<b>Nov&nbsp;27, 2009</b> &ndash; <b>Sep&nbsp;3, 2010</b>", gold=True),
        dict(html="<b>4</b> members", gold=False),
        dict(html="<b>0</b> championships", gold=False),
    ],
    lede=("A wrestling stable normally sells you a contract dispute or a bloodline. The Straight "
          "Edge Society sold you a religion. CM Punk spent ten months on SmackDown running a "
          "congregation of sobriety, shaving the heads of everyone who joined it, and losing "
          "almost every match that mattered &mdash; which is exactly why people still remember it."),

    # ---- rail ----
    tape=[
        dict(label="Promotion", value="WWE (SmackDown)"),
        dict(label="Active", value="Nov 27, 2009 &ndash; Sep 3, 2010",
             sub="Wikipedia infobox; the dates match the two SmackDown episodes the article describes."),
        dict(label="Leader", value='<a href="/wrestlers/cm-punk/">CM Punk</a>'),
        dict(label="Members", value="4"),
        dict(label="Titles won", value="None",
             sub="Punk's World Heavyweight reign ended Oct 4, 2009, seven weeks before the group formed."),
        dict(label="Heads shaved", value="2 on camera",
             sub="Serena, Jan 22, 2010. Punk himself, May 23, 2010 at Over the Limit."),
        dict(label="Signature", value="The conversion promo"),
        dict(label="Ended by", value="Big Show"),
    ],

    # ---- 01 overview ----
    overview_lead="What it was, why WWE ran it, and what it left behind.",
    stats=[("10", "months active"), ("4", "members"), ("0", "titles"),
           ("3", "PPVs vs Mysterio"), ("2", "heads shaved")],
    overview=[
        "The Straight Edge Society was a WWE stable led by <b>CM Punk</b> on SmackDown between "
        "<b>November 27, 2009</b> and <b>September 3, 2010</b>. Its members were Punk, "
        "<b>Luke Gallows</b>, <b>Serena</b> and <b>Joey Mercury</b>. The premise was a single "
        "inversion: Punk took straight edge &mdash; a real subculture built on abstaining from "
        "alcohol, tobacco and drugs, and one Punk genuinely lives &mdash; and played it as a cult, "
        "with himself as the saviour and the audience as the addicted.",

        "It existed because Punk's 2009 heel turn needed somewhere to go. He had spent that summer "
        "beating Jeff Hardy while lecturing a crowd that adored Hardy, and by the "
        "<b>August 28, 2009</b> SmackDown he had run Hardy out of the company in a loser-leaves-WWE "
        "steel cage match. The gimmick worked but had no engine: a man alone can only sermonise so "
        "long. The Society gave him converts. On the <b>November 27, 2009</b> SmackDown he "
        "&ldquo;cured&rdquo; the previously mute, comedic Festus and produced Luke Gallows, and the "
        "act suddenly had a before-and-after picture to point at.",

        "What it changed was the vocabulary of a heel stable. The Society did not recruit by "
        "contract or bloodline; it recruited by conversion, and the price of admission was your "
        "hair. Serena climbed the barricade on the <b>January 22, 2010</b> SmackDown and had her "
        "head shaved on camera as her initiation &mdash; a genuinely startling image on a 2010 WWE "
        "show. That ritual then became the currency of the group's one great feud, against "
        "<b>Rey Mysterio</b>, which escalated across three pay-per-views until Punk's own hair was "
        "on the table.",

        "The record is the strange part. The Straight Edge Society <b>never held a championship</b>. "
        "Punk's World Heavyweight title reign had ended at Hell in a Cell on "
        "<b>October 4, 2009</b>, seven weeks before the stable formed, and no member won a belt "
        "while wearing the X. It lost the WrestleMania match, lost the hair match, and was beaten "
        "three-on-one by Big Show at SummerSlam. Its whole value was in the imagery and the promos, "
        "which is why it is remembered warmly by people who could not name a single match it won.",
    ],

    # ---- 02 members ----
    members_lead="Four members in ten months. Every one of them had their hair on the line at some point.",
    members_note=("<b>Not a member:</b> Darren Young, Punk's rookie on the first season of NXT, agreed "
                  "to join and then changed his mind before the head-shaving. He is in the timeline "
                  "below, not in this list."),
    members=[
        dict(name="CM Punk", slug="cm-punk", ld_role="Leader and founder",
             dates="Nov 27, 2009 &ndash; Sep 3, 2010",
             start_iso="2009-11-27", end_iso="2010-09-03",
             role="Leader &middot; founder &middot; the voice",
             note=("Wrote and performed the entire premise. Held no championship for a single day of "
                   "the group's existence, and ended it himself by hitting Gallows with a Go To Sleep "
                   "and walking out on the September 3, 2010 SmackDown.")),
        dict(name="Luke Gallows", ld_role="Enforcer",
             dates="Nov 27, 2009 &ndash; Sep 24, 2010",
             start_iso="2009-11-27", end_iso="2010-09-24",
             role="Enforcer &middot; the first convert",
             sameAs=["https://en.wikipedia.org/wiki/Doc_Gallows"],
             note=("Repackaged from the comedy character Festus on the November 27, 2009 SmackDown, "
                   "which is the moment the stable dates from. He was the walking proof of the "
                   "gimmick. Released by WWE on November 19, 2010.")),
        dict(name="Serena", ld_role="Member",
             dates="Jan 22, 2010 &ndash; Aug 20, 2010",
             start_iso="2010-01-22", end_iso="2010-08-20",
             role="Member &middot; the initiation",
             sameAs=["https://en.wikipedia.org/wiki/Serena_Deeb"],
             note=("Came over the barricade on the January 22, 2010 SmackDown and had her head shaved "
                   "as her initiation. Released on August 20, 2010, reportedly for not living the "
                   "straight edge persona in public &mdash; a storyline undone by the storyline.")),
        dict(name="Joey Mercury", ld_role="Member",
             dates="Apr 25, 2010 &ndash; Sep 2010",
             start_iso="2010-04-25", end_iso="2010-09-03",
             role="Member &middot; the masked man",
             sameAs=["https://en.wikipedia.org/wiki/Joey_Mercury"],
             note=("A three-time WWE Tag Team Champion with MNM, working backstage by 2010. He "
                   "appeared hooded at Extreme Rules on April 25 to cost Rey Mysterio the match, and "
                   "was unmasked by Big Show on the July 23, 2010 SmackDown.")),
    ],

    # ---- 03 timeline ----
    timeline_lead=("Two prologue beats are included because the group is unreadable without them: "
                   "the heel turn that created the preacher, and the title loss that meant the "
                   "Society was never a champion's stable."),
    timeline=[
        dict(when="Aug 23, 2009", title="Prologue &middot; SummerSlam",
             desc="Punk regains the World Heavyweight Championship from Jeff Hardy in a TLC match, "
                  "then is attacked by The Undertaker. The sanctimonious straight edge heel is now "
                  "the top villain on SmackDown."),
        dict(when="Aug 28, 2009", title="Prologue &middot; Hardy leaves",
             desc="On SmackDown, Punk retains the World Heavyweight Championship in a "
                  "loser-leaves-WWE steel cage match and Jeff Hardy leaves the company."),
        dict(when="Oct 4, 2009", title="Prologue &middot; the belt goes",
             desc="At Hell in a Cell, Punk loses the World Heavyweight Championship to The "
                  "Undertaker. He will not hold a title again until 2011 &mdash; which is to say, "
                  "not once during the Straight Edge Society."),
        dict(when="Nov 27, 2009", title="Formation &middot; Festus becomes Luke Gallows",
             desc="On SmackDown, Punk &ldquo;transforms&rdquo; the previously unresponsive Festus "
                  "into the focused Luke Gallows. This is the date the stable is founded."),
        dict(when="Jan 22, 2010", title="Serena's initiation",
             desc="Serena, planted in the crowd, jumps the barricade to join. She agrees to have her "
                  "head shaved bald on camera as the price of admission."),
        dict(when="Jan 31, 2010", title="Recruiting from the Rumble",
             desc="Punk begins interrupting events to preach and recruit, starting at the Royal "
                  "Rumble, cutting sermons mid-match on his way to being eliminated."),
        dict(when="Feb 21, 2010", title="The Mysterio feud opens",
             desc="The Society begins its rivalry with Rey Mysterio at the Elimination Chamber "
                  "pay-per-view. It will run across three consecutive pay-per-views."),
        dict(when="Feb 23, 2010", title="The rookie who said no",
             desc="Punk is revealed as the mentor of NXT rookie Darren Young. Young agrees to join "
                  "the Society, then backs out before the head-shaving. He never becomes a member."),
        dict(when="Mar 28, 2010", title="WrestleMania XXVI",
             desc="Mysterio defeats Punk. The stipulation had been that Mysterio would join the "
                  "Straight Edge Society if he lost."),
        dict(when="Apr 25, 2010", title="Extreme Rules &middot; the fourth man",
             desc="Punk beats Mysterio with Punk's hair on the line, after interference from a "
                  "hooded, masked fourth member. The Society is now four."),
        dict(when="May 23, 2010", title="Over the Limit &middot; Punk is shaved",
             desc="The stipulations from the previous two pay-per-views are combined. Mysterio wins "
                  "after interference from Kane, and Punk's head is shaved. He spends the following "
                  "months hiding it under a mask and a hood."),
        dict(when="Jun 20, 2010", title="Fatal 4-Way",
             desc="Punk works a fatal four-way match at the Fatal 4-Way pay-per-view. The Society "
                  "stays close to the World Heavyweight title picture without ever closing on it."),
        dict(when="Jul 23, 2010", title="The mask comes off",
             desc="On SmackDown, the masked man wrestles and loses to Big Show, who then unmasks him "
                  "as Joey Mercury."),
        dict(when="Aug 15, 2010", title="SummerSlam &middot; three against one",
             desc="At the Staples Center in Los Angeles, Big Show beats all three of Punk, Gallows "
                  "and Mercury in a 3-on-1 handicap match, knocking out Gallows and chokeslamming "
                  "Mercury onto him for the pin."),
        dict(when="Aug 20, 2010", title="Serena released",
             desc="WWE releases Serena, reportedly for not living out the straight edge persona in "
                  "public. On the August 27 SmackDown, WWE.com's announcement is folded into the "
                  "show to write her out."),
        dict(when="Sep 3, 2010", title="Disbandment",
             desc="After losing a handicap match to Big Show, a visibly frustrated Punk hits Gallows "
                  "with a Go To Sleep and leaves the ring. This is the date the group ends."),
        dict(when="Sep 24, 2010", title="The last word",
             desc="Gallows confronts Punk on SmackDown, promising to celebrate his win with a beer. "
                  "Punk wins the match. Gallows is released on November 19, 2010."),
    ],

    # ---- 04 championships: deliberately absent. See the module docstring. ----
    titles=[],

    # ---- 05 moments ----
    moments_lead=("Five segments that carry the whole run. None of them is a title match, because "
                  "there were none to have."),
    moments=[
        dict(year="2009", kind="SmackDown", title="The conversion of Festus",
             desc="<b>November 27, 2009</b> &middot; SmackDown &mdash; Punk parades the mute, "
                  "grinning Festus in front of the crowd and returns him as Luke Gallows: shaved, "
                  "articulate, furious. The stable's founding document, performed as a faith "
                  "healing."),
        dict(year="2010", kind="SmackDown", title="Serena takes the clippers",
             desc="<b>January 22, 2010</b> &middot; SmackDown &mdash; a woman comes out of the "
                  "audience begging to be saved, and Punk shaves her head in the middle of the ring "
                  "as her initiation. The single most-remembered image the group produced."),
        dict(year="2010", kind="WrestleMania XXVI", title="Punk vs Rey Mysterio",
             desc="<b>March 28, 2010</b> &mdash; Mysterio wins, with the stipulation hanging over it "
                  "that a loss would have made him a member of the Society. The feud's opening "
                  "statement, and the first of three straight pay-per-views."),
        dict(year="2010", kind="Over the Limit", title="Hair against mask",
             desc="<b>May 23, 2010</b> &mdash; the stipulations from WrestleMania and Extreme Rules "
                  "are stacked into one match. Mysterio wins after Kane interferes, and Punk's own "
                  "head is shaved in front of the crowd he had been shaving others for."),
        dict(year="2010", kind="SummerSlam", title="Big Show, three on one",
             desc="<b>August 15, 2010</b> &middot; Staples Center, Los Angeles &mdash; Big Show "
                  "knocks out Gallows, chokeslams Mercury on top of him and pins him. Three members "
                  "of a stable beaten by one man is the beginning of its end."),
    ],

    # ---- 06 legacy ----
    legacy_lead="What ten months of losing bought.",
    legacy=[
        "The Straight Edge Society is the clearest evidence that a wrestling stable does not need to "
        "win to matter. It went 0-for-championships, lost its WrestleMania match, lost its hair "
        "match and was beaten three-on-one at SummerSlam, and it is still the run people cite when "
        "they argue that Punk was a main-event act long before WWE agreed. The Society is where he "
        "proved he could carry a segment with nothing but a microphone and a set of clippers.",

        "It also stress-tested the character that would make him famous. The <b>June 27, 2011</b> "
        "&ldquo;pipe bomb&rdquo; promo works because the audience had already spent two years "
        "watching Punk lecture them from a moral high ground; the Society is where that voice was "
        "built. Four months after the group ended he took over The Nexus, and seven months after "
        "that he was sitting cross-legged on the stage in Las Vegas.",

        "For everyone else it was a launchpad or an exit. Gallows was released, went to Japan and "
        "came back a Bullet Club founder-adjacent star. Serena was released mid-angle and rebuilt a "
        "career that ended up more decorated than the one WWE cut short. Mercury went back behind "
        "the curtain and returned four years later as one half of J&amp;J Security. The Society's "
        "real legacy is a set of careers it redirected.",
    ],
    after=[
        dict(mono="P", era="After September 2010", name="CM Punk",
             desc="Took over The Nexus on the January 3, 2011 Raw and renamed it The New Nexus. Won "
                  "the WWE Championship from John Cena at Money in the Bank on July 17, 2011."),
        dict(mono="G", era="Released Nov 19, 2010", name="Luke Gallows",
             desc="Left WWE, worked the independents and Japan, and in November 2013 was announced "
                  "for New Japan's World Tag League alongside Karl Anderson as part of Bullet Club."),
        dict(mono="S", era="Released Aug 20, 2010", name="Serena Deeb",
             desc="Won the NWA World Women's Championship on October 27, 2020, beating Thunder Rosa. "
                  "Signed with AEW in September 2020 and works there as a coach."),
        dict(mono="M", era="Back in 2014", name="Joey Mercury",
             desc="Returned to television on September 29, 2014 as one half of J&amp;J Security with "
                  "Jamie Noble, bodyguards to Seth Rollins, before going back to producing."),
    ],

    # ---- 07 faq ----
    faq_lead="",
    faq=[
        dict(q="When did the Straight Edge Society form and when did it break up?",
             a="The stable dates from the <b>November 27, 2009</b> episode of SmackDown, when CM "
               "Punk repackaged Festus as Luke Gallows, and ended on the <b>September 3, 2010</b> "
               "episode, when Punk hit Gallows with a Go To Sleep after a handicap loss to Big Show "
               "and walked out. Ten months, almost to the day.",
             q_ld="When did the Straight Edge Society form and when did it break up?",
             a_ld="The Straight Edge Society formed on the November 27, 2009 episode of WWE "
                  "SmackDown, when CM Punk repackaged Festus as Luke Gallows, and disbanded on the "
                  "September 3, 2010 episode, when Punk hit Gallows with a Go To Sleep after losing "
                  "a handicap match to Big Show."),
        dict(q="Who were the members of the Straight Edge Society?",
             a="Four: <b>CM Punk</b> as leader, <b>Luke Gallows</b> from the founding date, "
               "<b>Serena</b> from January 22, 2010, and <b>Joey Mercury</b>, who first appeared "
               "hooded at Extreme Rules on April 25, 2010 and was unmasked on July 23. Darren Young "
               "is often listed as a fifth; he was Punk's NXT rookie, agreed to join, and backed out "
               "before the head-shaving.",
             q_ld="Who were the members of the Straight Edge Society?",
             a_ld="The Straight Edge Society had four members: CM Punk as leader, Luke Gallows from "
                  "November 27, 2009, Serena from January 22, 2010, and Joey Mercury, who first "
                  "appeared masked on April 25, 2010 and was unmasked on July 23, 2010. Darren "
                  "Young was CM Punk's NXT rookie but never formally joined the group."),
        dict(q="Did the Straight Edge Society ever win a championship?",
             a="No. Not one, in ten months. Punk's World Heavyweight Championship reign ended at "
               "Hell in a Cell on <b>October 4, 2009</b>, seven weeks before the group existed, and "
               "neither Gallows, Serena nor Mercury held a title while in it. Every &ldquo;SES "
               "championship&rdquo; you see online is somebody counting Punk's 2009 reign that "
               "predates the stable.",
             q_ld="Did the Straight Edge Society ever win a championship?",
             a_ld="No. The Straight Edge Society never held a championship. CM Punk's World "
                  "Heavyweight Championship reign ended at Hell in a Cell on October 4, 2009, seven "
                  "weeks before the stable was formed on November 27, 2009, and no member won a "
                  "title during the group's existence."),
        dict(q="Why did Serena leave the Straight Edge Society?",
             a="She was released by WWE. Her own article and the Pro Wrestling fandom entry both give "
               "<b>August 20, 2010</b> as the release date, reportedly because she was not "
               "&ldquo;living out&rdquo; the straight edge persona in public. The Straight Edge "
               "Society article instead describes WWE.com announcing the release during the "
               "<b>August 27</b> SmackDown, which is when it was written into the show. Both dates "
               "are real; they describe different things.",
             q_ld="Why did Serena leave the Straight Edge Society?",
             a_ld="Serena was released by WWE on August 20, 2010, reportedly for not living out the "
                  "straight edge persona in public. The release was written into television on the "
                  "August 27, 2010 episode of SmackDown, when WWE.com's announcement was "
                  "acknowledged on the show, which is why some sources give the later date."),
        dict(q="Whose heads actually got shaved?",
             a="Two, on camera. <b>Serena</b> was shaved as her initiation on the January 22, 2010 "
               "SmackDown. <b>CM Punk</b> was shaved on <b>May 23, 2010</b> at Over the Limit, after "
               "losing a match to Rey Mysterio that combined the stipulations of their two previous "
               "pay-per-view matches &mdash; Punk's hair against Mysterio's mask. Punk spent the "
               "next several months wrestling in a mask and hood.",
             q_ld="Whose heads were shaved in the Straight Edge Society?",
             a_ld="Two heads were shaved on camera. Serena had her head shaved as her initiation on "
                  "the January 22, 2010 episode of SmackDown. CM Punk had his own head shaved on "
                  "May 23, 2010 at Over the Limit after losing to Rey Mysterio in a match combining "
                  "the stipulations of their two previous pay-per-view matches."),
        dict(q="How did the Straight Edge Society lead to The New Nexus?",
             a="Directly. Punk moved to Raw a few months after the Society folded, and on the "
               "<b>January 3, 2011</b> Raw he was revealed as the new leader of The Nexus, which was "
               "renamed The New Nexus. He brought the initiation ritual with him &mdash; the kendo "
               "stick test on the January 10 Raw is the Society's head-shaving idea with the "
               "religion filed off.",
             q_ld="How did the Straight Edge Society lead to The New Nexus?",
             a_ld="After the Straight Edge Society disbanded in September 2010, CM Punk moved to Raw "
                  "and was revealed as the new leader of The Nexus on the January 3, 2011 episode "
                  "of Raw. The group was renamed The New Nexus, and Punk carried over the "
                  "initiation-ritual device from the Straight Edge Society."),
    ],

    # ---- 08 sources ----
    sources_lead="Every date on this page traces to one of these.",
    sources_note=("Where two sources disagree &mdash; Serena's release date is the only case here "
                  "&mdash; both readings are stated on the page rather than one being chosen "
                  "quietly."),
    sources=[
        dict(k="Wikipedia", v="The Straight Edge Society",
             href="https://en.wikipedia.org/wiki/The_Straight_Edge_Society"),
        dict(k="Wikipedia", v="Serena Deeb",
             href="https://en.wikipedia.org/wiki/Serena_Deeb"),
        dict(k="Wikipedia", v="Doc Gallows",
             href="https://en.wikipedia.org/wiki/Doc_Gallows"),
        dict(k="Wikipedia", v="Joey Mercury",
             href="https://en.wikipedia.org/wiki/Joey_Mercury"),
        dict(k="Wikipedia", v="SummerSlam (2010)",
             href="https://en.wikipedia.org/wiki/SummerSlam_(2010)"),
        dict(k="Wikipedia", v="CM Punk",
             href="https://en.wikipedia.org/wiki/CM_Punk"),
        dict(k="Pro Wrestling Wiki", v="Serena Deeb",
             href="https://prowrestling.fandom.com/wiki/Serena_Deeb"),
    ],

    # ---- outbound cross-links ----
    explore=[
        dict(href="/wrestlers/cm-punk/", kicker="Dossier", name="CM Punk",
             desc="The full record: Chicago, Ring of Honor, the pipe bomb, the returns."),
        dict(href="/factions/the-new-nexus/", kicker="Next stable", name="The New Nexus",
             desc="Where Punk went four months later, and what he did with somebody else's army."),
        dict(href="/factions/the-second-city-saints/", kicker="First stable",
             name="The Second City Saints",
             desc="The Ring of Honor trio that made him, seven years earlier."),
        dict(href="/factions/", kicker="Index", name="All factions",
             desc="Every stable filed on Wrestle Lore."),
    ],

    # ---- hub card ----
    hub_era="WWE &middot; 2009&ndash;10",
    hub_members="CM Punk, Luke Gallows, Serena, Joey Mercury",
    hub_desc=("A cult of sobriety with Punk as its messiah, shaving heads and preaching the straight "
              "edge gospel across ten months of SmackDown &mdash; and never winning a title."),
)
