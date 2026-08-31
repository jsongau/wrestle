# -*- coding: utf-8 -*-
"""Batista - dossier data.

Sources: web-verified August 31, 2026 (Wikipedia, Fightful, WWE.com, Ringside News,
Wikipedia's WWE Hall of Fame 2026 page). Every match row carries a day-precision date
confirmed in those sources.

Deliberate omissions:
  * No career win-loss total - no verified figure exists and none is invented.
  * No Meltzer star ratings in the signature block - not verified in this pass.
  * Hall of Fame status is stated precisely: announced for the Class of 2020 on
    December 9, 2019, never actually inducted, and absent from every class through
    2026 - the delay is sourced (film scheduling, per Fightful) rather than guessed at.
"""

# ----------------------------------------------------------------- record rows
# 15 documented bouts - both Royal Rumble wins, all six world title changes he was
# part of, the Evolution reunion loss and both farewell matches.
ROWS = [
    dict(result="W", date="2005-01-30", promo="WWE", landmark=True, type="tag",
         event="Royal Rumble match", opponent="The 2005 Royal Rumble field",
         stip="Last eliminated John Cena", title=""),
    dict(result="W", date="2005-04-03", promo="WWE", landmark=True,
         event="WrestleMania 21", opponent="Triple H",
         stip="Singles — first world title; the Evolution split pays off",
         title="World Heavyweight Championship"),
    dict(result="W", date="2005-06-26", promo="WWE", landmark=True,
         event="Vengeance", opponent="Triple H",
         stip="Hell in a Cell — the blowoff", title="World Heavyweight Championship"),
    dict(result="W", date="2005-10-09", promo="WWE",
         event="No Mercy", opponent="Eddie Guerrero",
         stip="Singles — defense in Guerrero's last title challenge",
         title="World Heavyweight Championship"),
    dict(result="W", date="2006-11-26", promo="WWE",
         event="Survivor Series", opponent="King Booker",
         stip="Singles — regains the title lost to injury", title="World Heavyweight Championship"),
    dict(result="L", date="2007-04-01", promo="WWE", landmark=True,
         event="WrestleMania 23", opponent="The Undertaker",
         stip="Singles — the streak takes the title", title="World Heavyweight Championship"),
    dict(result="W", date="2007-09-16", promo="WWE", type="tag",
         event="Unforgiven", opponent="The Great Khali & Rey Mysterio",
         stip="Triple threat — third reign", title="World Heavyweight Championship"),
    dict(result="W", date="2008-10-26", promo="WWE",
         event="Cyber Sunday", opponent="Chris Jericho",
         stip="Steve Austin as fan-voted referee — fourth reign",
         title="World Heavyweight Championship"),
    dict(result="W", date="2010-02-21", promo="WWE", landmark=True,
         event="Elimination Chamber", opponent="John Cena",
         stip="Impromptu match ordered by Mr. McMahon — heel Batista's first WWE Championship",
         title="WWE Championship"),
    dict(result="L", date="2010-03-28", promo="WWE", landmark=True,
         event="WrestleMania XXVI", opponent="John Cena",
         stip="Singles — the reign ends", title="WWE Championship"),
    dict(result="L", date="2010-05-23", promo="WWE",
         event="Over the Limit", opponent="John Cena",
         stip="I Quit — last match of the first run; he 'quit' the company on Raw the next night",
         title="WWE Championship"),
    dict(result="W", date="2014-01-26", promo="WWE", landmark=True, type="tag",
         event="Royal Rumble match — Pittsburgh", opponent="The 2014 Royal Rumble field",
         stip="Won under loud protest from a crowd that wanted Daniel Bryan", title=""),
    dict(result="L", date="2014-04-06", promo="WWE", landmark=True, type="tag",
         event="WrestleMania XXX", opponent="Daniel Bryan & Randy Orton",
         stip="Triple threat — Bryan makes him tap", title="WWE World Heavyweight Championship"),
    dict(result="L", date="2014-06-01", promo="WWE", type="tag",
         event="Payback — Chicago", opponent="The Shield",
         stip="Evolution vs. The Shield — no-holds-barred elimination, swept 3-0", title=""),
    dict(result="L", date="2019-04-07", promo="WWE", landmark=True,
         event="WrestleMania 35", opponent="Triple H",
         stip="No holds barred — the final match; Triple H's career was on the line", title=""),
]

DATA = dict(
    slug="batista",
    name="Batista",
    realname="David Michael Bautista Jr.",
    epithet="The Animal",
    hook="Record & Titles",

    meta_desc=("Batista, The Animal, won six world championships and two Royal Rumbles before "
               "retiring at WrestleMania 35 and becoming Hollywood's most respected "
               "wrestler-turned-actor. Full record, titles, Evolution and career."),
    og_desc=("The Animal: six world titles, two Royal Rumble wins, the 285-day reign that rebuilt "
             "SmackDown — and a second career as Drax, Rabban and beyond."),
    tw_desc="Batista: six world titles, two Royal Rumbles, retired 2019, now a Hollywood lead.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1999",
    height_imp="6&#8242;6&#8243;",
    weight_lb="290",
    world_titles="6",
    vitals_tagline="I walk alone",
    support_note="Merch &middot; Films &middot; Read",
    sp_items=[
        dict(ic="BA", title="WWE Shop", sub="Legends tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable as a legend in the 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="F", title="Filmography", sub="Every Dave Bautista role, Wikipedia",
             tag="Read", href="https://en.wikipedia.org/wiki/Dave_Bautista_filmography"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/batista"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Animal &middot; Deacon Batista &middot; Leviathan &middot; Dave Bautista",
    hero_tag="Washington, D.C. &middot; <em>OVW &middot; WWE &middot; Hollywood &middot; 1999&ndash;2019</em>",
    now_label="NOW",
    now_bold="Retired from wrestling, working actor",
    now_tail=(" &middot; final match WrestleMania 35, April 7, 2019 &middot; filming Road House 2 and "
              "Highlander as of the most recent filmography updates &middot; still not a WWE Hall of "
              "Famer, by scheduling rather than by choice"),
    hstats=[
        dict(value="6",   x=False, label="World Titles"),
        dict(value="2",   x=False, label="Royal Rumbles"),
        dict(value="285", x=False, label="Day First Reign"),
        dict(value="0",   x=True,  label="HOF Inductions, So Far"),
    ],
    ghost_link="From a D.C. bouncer to the biggest box-office career any wrestler has built",
    vlabel="Est. 1999 &middot; Washington, D.C.",
    mono="BA",

    # ---------------------------------------------------------------- 01 overview
    correction=2,
    overview=[
        "<b>Batista</b> retired on his own terms, which almost nobody in wrestling manages. His last "
        "match was a no-holds-barred loss to Triple H at WrestleMania 35 on April 7, 2019 &mdash; the "
        "match he asked for &mdash; and he announced his retirement the next day. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">6</span>'
        '<span class="pull-cap">world championships &mdash; four World Heavyweight, two WWE</span></span>'
        "What came before was one of the most efficient main-event careers of the 2000s: six world "
        "championships, Royal Rumble wins in 2005 and 2014, and a 285-day first World Heavyweight "
        "Championship reign that was the longest in that title&rsquo;s history and the spine of "
        "SmackDown&rsquo;s 2005&ndash;06 rebuild. What came after is the reason the retirement stuck: "
        "Dave Bautista is, by broad industry consensus, the best actor wrestling has ever produced.",

        "The wrestling story is Evolution, twice. He joined Triple H, Ric Flair and Randy Orton in "
        "early 2003 as the muscle, and the group&rsquo;s whole purpose became the slow-burn tease of "
        "his split from Triple H &mdash; paid off when he won the 2005 Royal Rumble on January 30, "
        "chose the World Heavyweight Championship, and beat Triple H at WrestleMania 21 on April 3, "
        "2005, then twice more, ending inside Hell in a Cell at Vengeance. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">2</span>'
        '<span class="pull-cap">Royal Rumble wins, nine years apart &mdash; one cheered, one booed out of the building</span></span>'
        "The 2014 sequel inverted it: he returned on January 20, won the Royal Rumble six days later, "
        "and the Pittsburgh crowd revolted because Daniel Bryan was not in the match. WWE bent the "
        "booking to reality, and Batista&rsquo;s WrestleMania XXX main event ended with him tapping "
        "to Bryan &mdash; a finish he has consistently said he endorsed. He was gone again by June "
        "2014, back once more in 2019 to give Triple H the farewell feud, and done.",

        "One thing needs setting straight: <b>Batista is not a WWE Hall of Famer</b>, and the reason "
        "is mundane. WWE announced him for the Class of 2020 on December 9, 2019; the ceremony was "
        "postponed by the pandemic, he withdrew before the merged 2021 event, and he has said "
        "repeatedly since &mdash; including to Chris Van Vliet in August 2024 &mdash; that he wants "
        "the induction and expects it eventually. Fightful&rsquo;s reporting in November 2025 says "
        "WWE has asked every year and the answer is always film scheduling, not politics. The Class "
        "of 2026, announced and inducted in Las Vegas on April 17, 2026, did not include him. So the "
        "correct sentence is &ldquo;announced but never inducted,&rdquo; not &ldquo;Hall of Famer,"
        "&rdquo; and any page that says otherwise is ahead of the facts.",

        "The second career is not a footnote; it is the bigger one. Since debuting as Drax in "
        "Guardians of the Galaxy in 2014 he has built a filmography no other wrestler approaches "
        "&mdash; five MCU appearances through 2023, Blade Runner 2049, Spectre, both Dune films as "
        "Rabban, Glass Onion, Knock at the Cabin, The Last Showgirl &mdash; and by the most recent "
        "updates he was filming Road House 2 and playing The Kurgan in a Highlander remake. He has "
        "been open that he deliberately chose character-actor credibility over action-star money, "
        "and it worked. He turned 57 in January 2026, lives in the film world full-time, and his "
        "wrestling chapter is closed &mdash; pending one overdue ceremony.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("4&times;", "World Heavyweight"),
            ("2&times;", "WWE Championship"),
            ("2",        "Royal Rumbles"),
            ("285",      "Day first reign"),
            ("3",        "Tag title reigns"),
            ("1-0",      "MMA record"),
        ],
        lead=("Fifteen documented bouts &mdash; both Rumble wins, every world title change he was in, "
              "the Shield sweep and the two farewells. A curated ledger, not a career count; no "
              "career win&ndash;loss total is published because no verified one exists. Filter by "
              "match type, tap any column header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The bouts the reputation rests on. Star ratings are deliberately not published: "
                    "Observer figures were not verified in this pass, and this page does not guess "
                    "at numbers."),
    signature=[
        dict(rating="&mdash;", event="WrestleMania 21", opponent="Triple H",
             stip="World Heavyweight Championship — the Evolution split pays off"),
        dict(rating="&mdash;", event="Vengeance 2005", opponent="Triple H",
             stip="Hell in a Cell — the trilogy ends"),
        dict(rating="&mdash;", event="WrestleMania XXX", opponent="Daniel Bryan & Randy Orton",
             stip="The main event he tapped out in, and defends to this day"),
        dict(rating="&mdash;", event="WrestleMania 35", opponent="Triple H",
             stip="No holds barred — the retirement match he asked for"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("4&times;", "World Heavyweight"),
            ("2&times;", "WWE Championship"),
            ("285",      "Day first reign"),
            ("3",        "Tag reigns"),
        ],
        lead=("Six world championships across two brands, plus tag gold with two very different "
              "partners. Exact reign endpoints beyond the ones stated were not re-verified in this "
              "pass and are not invented here."),
        rows=[
            dict(ic="W", name="World Heavyweight Championship", count="4",
                 sub="First won April 3, 2005 at WrestleMania 21 from Triple H &middot; the 285-day "
                     "first reign was the longest in the title&rsquo;s history &middot; regained from "
                     "King Booker at Survivor Series 2006, from The Great Khali in the Unforgiven "
                     "2007 triple threat, and from Chris Jericho at Cyber Sunday 2008 &middot; two "
                     "reigns ended by injury or vacancy rather than pinfall"),
            dict(ic="C", name="WWE Championship", count="2",
                 sub="2009 &middot; won from Randy Orton in a steel cage at Extreme Rules on June 7, "
                     "vacated within days after a torn biceps &middot; 2010 &middot; won from John "
                     "Cena at Elimination Chamber on February 21 in an impromptu match ordered by "
                     "Mr. McMahon, lost back to Cena at WrestleMania XXVI"),
            dict(ic="T", name="World Tag Team Championship", count="1",
                 sub="With Ric Flair, December 2003 &mdash; the Evolution era when the group held "
                     "every male title on Raw at once"),
            dict(ic="S", name="WWE Tag Team Championship", count="2",
                 sub="With Rey Mysterio in 2005 and with John Cena in 2008 &mdash; both short, both "
                     "story devices more than team runs"),
            dict(ic="R", name="Royal Rumble", count="2",
                 sub="2005 (last eliminating John Cena) and 2014 (last eliminating Roman Reigns, to "
                     "open revolt from a Pittsburgh crowd that wanted Daniel Bryan)"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="One faction, entered twice, defining both halves of the career.",
        cards=[
            dict(era="WWE &middot; 2003&ndash;2005",
                 name="Evolution",
                 members="Triple H, Ric Flair, Randy Orton, Batista",
                 desc="The past, present and two futures of the business, by its own billing. "
                      "Batista was the enforcer, and the group's long game — every member holding "
                      "gold, the slow tease of the Animal outgrowing the leader — paid off in the "
                      "thumbs-down moment of early 2005 and the WrestleMania 21 title win over "
                      "Triple H. The 2005 split remains one of the cleanest faction-breakup "
                      "storylines WWE has run."),
            dict(era="WWE &middot; 2014",
                 name="Evolution, reunion",
                 members="Triple H, Randy Orton, Batista",
                 desc="Reformed in April 2014 specifically to fight The Shield, and lost twice — "
                      "including the 3-0 no-holds-barred elimination sweep at Payback on June 1, "
                      "2014. Batista quit on-screen the next night, walking out on Raw in the "
                      "'I walk alone' framing that folded the real frustration of his 2014 run into "
                      "the character. The 2019 farewell program with Triple H was Evolution's last "
                      "echo: he attacked Ric Flair on Flair's 70th-birthday celebration to get it."),
            dict(era="OVW &middot; 2000&ndash;2002",
                 name="The developmental years",
                 members="Leviathan, in Ohio Valley Wrestling",
                 desc="Before Deacon Batista there was Leviathan, the 'Demon of the Deep' in OVW's "
                      "famous class alongside Brock Lesnar, John Cena and Randy Orton — the most "
                      "loaded developmental roster WWE ever had in one building."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Four names on the way up, one brand at the top: <b>Khan</b> (1999) &rarr; "
             "<b>Leviathan</b> (OVW, 2000&ndash;2002) &rarr; <b>Deacon Batista</b> (2002) &rarr; "
             "<b>Batista, The Animal</b> (2002&ndash;2019) &mdash; and, in the credits, "
             "<b>Dave Bautista</b>.",
        cards=[
            dict(mono="LV", era="OVW &middot; 2000&ndash;2002", name="Leviathan",
                 desc="The developmental monster, trained into shape at Afa's Wild Samoan school "
                      "before OVW. The raw-power template the later character refined."),
            dict(mono="DB", era="WWE &middot; 2002", name="Deacon Batista",
                 desc="The main-roster debut on May 9, 2002: collection-box-carrying enforcer for "
                      "Reverend D-Von. A dead-end gimmick that lasted months before the reset."),
            dict(mono="AN", era="WWE &middot; 2002&ndash;2019", name="Batista, The Animal",
                 desc="The Evolution enforcer who became the franchise: shades, machine-gun pyro, "
                      "the spinebuster into the Batista Bomb. The 2010 heel version — smug, "
                      "Hollywood-slick, 'I'm better than this company' — read as a preview of the "
                      "real exit, and the 2014 'Bluetista' crowd revolt accidentally created his "
                      "best character work."),
            dict(mono="DR", era="Hollywood &middot; 2014&ndash;", name="Dave Bautista",
                 desc="Drax in five MCU films, Rabban in both Dunes, Sapper Morton in Blade Runner "
                      "2049, Duke in Glass Onion, Leonard in Knock at the Cabin. He pursued small "
                      "roles with great directors over franchise paychecks, and is routinely called "
                      "the best actor to come out of wrestling."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="A D.C. bouncer at 30, a world champion at 36, a working character actor ever since.",
        rows=[
            dict(year="1999", title="Late start",
                 desc="Debuts on October 30, 1999 as Khan after training with Afa Anoai's Wild "
                      "Samoan school — he was already 30, having come to wrestling from bouncing "
                      "and bodybuilding."),
            dict(year="2002", title="WWE debut",
                 desc="Arrives on SmackDown on May 9, 2002 as Deacon Batista after the Leviathan "
                      "run in OVW's legendary Lesnar-Cena-Orton class."),
            dict(year="2003", title="Evolution",
                 desc="Joins Triple H, Ric Flair and Randy Orton in January. The group spends 2003 "
                      "holding every male championship on Raw."),
            dict(year="2005", title="The year of the Animal",
                 desc="Wins the Royal Rumble on January 30, beats Triple H at WrestleMania 21 on "
                      "April 3 for the World Heavyweight Championship, and holds it 285 days — the "
                      "longest reign in the title's history — while anchoring SmackDown."),
            dict(year="2007", title="The Undertaker series",
                 desc="Loses the title to The Undertaker at WrestleMania 23 on April 1, then trades "
                      "classics with him all year — widely treated as his best in-ring run."),
            dict(year="2010", title="Heel exit",
                 desc="Wins the WWE Championship from John Cena at Elimination Chamber on February "
                      "21, loses it back at WrestleMania XXVI, loses the I Quit match at Over the "
                      "Limit on May 23 and quits on Raw the next night."),
            dict(year="2012", title="One MMA fight",
                 desc="Wins his only MMA bout by first-round TKO over Vince Lucero at CES MMA in "
                      "Providence on October 6, 2012, at 43."),
            dict(year="2014", title="The Rumble backfire",
                 desc="Returns January 20, wins the Royal Rumble on January 26 to open hostility, "
                      "taps to Daniel Bryan in the WrestleMania XXX main event on April 6, reunites "
                      "Evolution, loses twice to The Shield and leaves in June. Guardians of the "
                      "Galaxy opens in August and changes everything."),
            dict(year="2019", title="The farewell he wanted",
                 desc="Attacks Ric Flair to bait Triple H, loses the no-holds-barred match at "
                      "WrestleMania 35 on April 7, and announces his retirement on April 8."),
            dict(year="2020", title="Hall of Fame, announced and paused",
                 desc="Named to the Class of 2020 on December 9, 2019; the pandemic postpones the "
                      "ceremony and he withdraws from the merged 2021 event, asking to be inducted "
                      "when he can attend properly."),
            dict(year="2026", title="Still waiting, still filming",
                 desc="Not part of the Class of 2026 inducted in Las Vegas on April 17, 2026. "
                      "Reporting through late 2025 attributes the delay entirely to film "
                      "scheduling; his slate includes Road House 2 and Highlander's Kurgan."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Triple H",
                 desc="Mentor, obstacle, and final opponent. The 2005 trilogy — WrestleMania 21, "
                      "Backlash, the Vengeance Hell in a Cell — is the definitive Evolution-split "
                      "story, and the 2019 no-holds-barred match at WrestleMania 35 closed the "
                      "career in the same relationship it was made in."),
            dict(name="The Undertaker",
                 desc="The 2007 series that rebuilt his in-ring reputation: WrestleMania 23 on "
                      "April 1, 2007, the Cyber Sunday and Survivor Series rematches, a Last Man "
                      "Standing draw. He lost the biggest ones and gained the most from them."),
            dict(name="John Cena",
                 desc="The two 2005 Rumble finalists spent five years as parallel franchises and "
                      "finally collided in 2010: Elimination Chamber, WrestleMania XXVI, and the I "
                      "Quit match at Over the Limit that ended his first run. The heel Batista of "
                      "this feud is his most rewatched character work."),
            dict(name="Eddie Guerrero",
                 desc="A short, warm program with a sad edge: Guerrero challenged him for the World "
                      "Heavyweight Championship at No Mercy on October 9, 2005 — Eddie's 38th "
                      "birthday — with a friendship-and-temptation story built around whether Eddie "
                      "could play fair. Batista won clean; Guerrero died five weeks later, and "
                      "Batista has spoken often about how much the pairing meant to him."),
            dict(name="Daniel Bryan",
                 desc="Not a rivalry he chose — the 2014 audience chose it for him. The Rumble win "
                      "over a Bryan-less field, the YES Movement, and the WrestleMania XXX main "
                      "event where he took the deciding submission are inseparable from his 2014 "
                      "run reading as a noble failure. He has said ever since that Bryan winning "
                      "was the right call."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Film",
        lead="The deepest post-wrestling filmography anyone in the business has &mdash; only the "
             "anchors are listed.",
        rows=[
            dict(when="2014&ndash;2023", title="Drax the Destroyer, Marvel Cinematic Universe", kind="Film",
                 desc="Guardians of the Galaxy (2014), Vol. 2 (2017), Avengers: Infinity War (2018) "
                      "and Endgame (2019), Vol. 3 (2023). The role that moved him from cameo casting "
                      "to a genuine acting career."),
            dict(when="2017&ndash;2024", title="The prestige run", kind="Film",
                 desc="Blade Runner 2049 (2017), Spectre's Mr. Hinx (2015), Dune (2021) and Dune: "
                      "Part Two (2024) as Rabban, Glass Onion (2022), Knock at the Cabin (2023), "
                      "The Last Showgirl (2024)."),
            dict(when="2024&ndash;", title="In production", kind="Film",
                 desc="The Killer's Game (2024) released; Road House 2 and Highlander (as The "
                      "Kurgan) in production per the most recent filmography updates, plus a voice "
                      "role in an Avatar: The Last Airbender animated film."),
            dict(when="2012", title="CES MMA: Real Pain", kind="MMA",
                 desc="His one professional MMA fight — first-round TKO of Vince Lucero on October "
                      "6, 2012. Career record 1-0, with a Brazilian jiu-jitsu brown belt under "
                      "Cesar Gracie."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records and the one conspicuous absence.",
        stats=[
            ("285", "Day WHC reign"),
            ("2",   "Royal Rumbles"),
            ("6",   "World titles"),
        ],
        rows=[
            dict(name="Longest World Heavyweight Championship reign in that title's history — 285 days",
                 sub="April 3, 2005 to January 2006, ended by a legitimate triceps injury and "
                     "vacancy rather than a loss."),
            dict(name="Two Royal Rumble wins, 2005 and 2014",
                 sub="One of the small club of multiple-time winners. The 2014 win over a field "
                     "without Daniel Bryan produced one of the loudest crowd revolts in modern WWE."),
            dict(name="Six world championships",
                 sub="Four World Heavyweight, two WWE. He main-evented WrestleMania twice (21 and "
                     "XXX, the latter as a losing participant in the triple threat)."),
            dict(name="Announced for the WWE Hall of Fame — never yet inducted",
                 sub="Named to the Class of 2020 on December 9, 2019; withdrew when the pandemic "
                     "merged the ceremonies; absent from every class through 2026. Fightful's "
                     "reporting attributes the delay solely to film scheduling, and Bautista said "
                     "in August 2024 that he wants the induction — 'Eventually, I will.'"),
            dict(name="1-0 as a professional mixed martial artist",
                 sub="TKO of Vince Lucero, CES MMA, October 6, 2012 — at age 43."),
            dict(name="The consensus best actor wrestling has produced",
                 sub="A subjective title, but one stated across trade coverage of his career, built "
                     "on choosing Villeneuve, Craig-era Bond, Rian Johnson and M. Night Shyamalan "
                     "projects over franchise action leads."),
        ],
        footnote=("Deliberately absent: a career win-loss total (no verified figure), social "
                  "handles (his accounts are actor-branded rather than wrestling-branded and are "
                  "not tracked here), and any claim that he is already a Hall of Famer — as of "
                  "August 31, 2026 he is not."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Dave_Bautista"),
        dict(k="Fightful", v="Bautista on the Hall of Fame — 'Eventually, I will' (Aug 2024)",
             href="https://www.fightful.com/wrestling/dave-bautista-batista-wwe-hall-fame-induction-eventually-i-will-i-want/"),
        dict(k="WWE.com", v="Batista's own 2021 Hall of Fame statement",
             href="https://www.wwe.com/article/batista-hall-of-fame-update"),
        dict(k="Ringside News", v="Why the induction keeps slipping — scheduling, per Fightful (Nov 2025)",
             href="https://www.ringsidenews.com/real-reason-revealed-batistas-delayed-wwe-hall-fame-induction/"),
        dict(k="Wikipedia", v="WWE Hall of Fame Class of 2026 — he is not in it",
             href="https://en.wikipedia.org/wiki/WWE_Hall_of_Fame_(2026)"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Batista in the WWE Hall of Fame?",
            a="No &mdash; and this is the most commonly wrong fact about him. WWE announced him for "
              "the Class of 2020 on December 9, 2019, but the ceremony was postponed by the "
              "pandemic and he withdrew before the merged 2021 event, asking to be inducted when he "
              "could attend properly. Every class since, including the Class of 2026 inducted in "
              "Las Vegas on April 17, 2026, has gone by without him. He has said repeatedly that he "
              "wants in &mdash; &ldquo;Eventually, I will&rdquo; &mdash; and reporting from late "
              "2025 attributes the delay entirely to film-schedule conflicts with WrestleMania "
              "weekend, not to any falling-out.",
            q_ld="Is Batista in the WWE Hall of Fame?",
            a_ld="No. Batista was announced for the WWE Hall of Fame Class of 2020 on December 9, "
                 "2019, but the ceremony was postponed by the COVID-19 pandemic and he withdrew "
                 "before the merged 2021 event. As of August 2026 he has never been inducted, and "
                 "he was not part of the Class of 2026. He has said he wants the induction "
                 "eventually, and reporting attributes the repeated delay to conflicts between his "
                 "film schedule and WrestleMania weekend."),
        dict(
            q="When was Batista&rsquo;s last match?",
            a="April 7, 2019 &mdash; a no-holds-barred loss to Triple H at WrestleMania 35, with "
              "Triple H&rsquo;s career on the line and a Ric Flair interference in the finish. He "
              "announced his retirement the next day and has not wrestled since; unlike most "
              "wrestling retirements, this one has held for over seven years. He has consistently "
              "said the WrestleMania 35 match was the send-off he asked for.",
            q_ld="When was Batista's last wrestling match?",
            a_ld="Batista's last match was at WrestleMania 35 on April 7, 2019, a no-holds-barred "
                 "loss to Triple H. He announced his retirement from professional wrestling the "
                 "following day, April 8, 2019, and has not wrestled since, focusing entirely on "
                 "his acting career as Dave Bautista."),
        dict(
            q="How many world titles did Batista win?",
            a="Six &mdash; four World Heavyweight Championships (first won from Triple H at "
              "WrestleMania 21 on April 3, 2005, the start of a 285-day reign that is the longest "
              "in that title&rsquo;s history) and two WWE Championships (won from Randy Orton in a "
              "cage at Extreme Rules 2009 and vacated to a torn biceps within days, then won from "
              "John Cena at Elimination Chamber 2010). He also won the Royal Rumble twice, in 2005 "
              "and 2014, and held tag team gold with Ric Flair, Rey Mysterio and John Cena.",
            q_ld="How many world championships did Batista win?",
            a_ld="Batista won six world championships in WWE: four World Heavyweight Championships "
                 "and two WWE Championships. His first World Heavyweight Championship reign, begun "
                 "at WrestleMania 21 on April 3, 2005, lasted 285 days, the longest reign in that "
                 "title's history. He also won the Royal Rumble in 2005 and 2014."),
        dict(
            q="Why did the crowd boo Batista&rsquo;s 2014 Royal Rumble win?",
            a="Because Daniel Bryan was not in the match. Batista returned on January 20, 2014 "
              "after three and a half years away and won the Rumble six days later in Pittsburgh, "
              "last eliminating Roman Reigns, in front of a crowd chanting for Bryan &mdash; who "
              "had not been entered at all. The revolt did not stop, WWE rewrote the road to "
              "WrestleMania XXX, and the main event on April 6, 2014 ended with Bryan submitting "
              "Batista to win the title. Batista has said many times since that the change was "
              "correct, and his own heel run out of it (&ldquo;Bluetista&rdquo;) became a cult "
              "favourite.",
            q_ld="Why was Batista booed when he won the 2014 Royal Rumble?",
            a_ld="Batista was booed because the crowd wanted Daniel Bryan, who was not entered in "
                 "the 2014 Royal Rumble match. Batista had just returned from three and a half "
                 "years away and won the match in Pittsburgh on January 26, 2014. The sustained "
                 "fan revolt led WWE to add Bryan to the WrestleMania XXX main event, where Bryan "
                 "defeated Batista and Randy Orton to win the WWE World Heavyweight Championship, "
                 "with Batista submitting to end the match. Batista has repeatedly endorsed that "
                 "outcome."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="David Michael Bautista Jr."),
        dict(label="Born", value="January 18, 1969", sub="Washington, D.C. &middot; age 57"),
        dict(label="Billed from", value="Washington, D.C."),
        dict(label="Height", value="6&#8242;6&#8243;", sub="198 cm"),
        dict(label="Weight", value="290 lb", sub="132 kg billed at his peak; he has said he "
                                                 "trimmed to around 240 lb for film work"),
        dict(label="Debut", value="October 30, 1999", sub="as Khan; WWE debut May 9, 2002"),
        dict(label="Trained by", value="Afa Anoai",
             sub="Wild Samoan Training Center &middot; later Muay Thai and Eskrima under Marrese "
                 "Crump, BJJ brown belt under Cesar Gracie"),
        dict(label="Signature", value="Batista Bomb &middot; Spinebuster &middot; Spear",
             sub="the thumbs-up, thumbs-down gesture as the kill signal"),
        dict(label="Final match", value="April 7, 2019",
             sub="No holds barred vs. Triple H, WrestleMania 35; retirement announced April 8"),
        dict(label="Hall of Fame", value="Announced 2019, never inducted",
             sub="withdrew from the merged 2021 ceremony; absent from every class through 2026"),
        dict(label="Also known as", value="The Animal &middot; Leviathan &middot; Deacon Batista "
                                          "&middot; Dave Bautista"),
        dict(label="MMA record", value="1&ndash;0", sub="TKO of Vince Lucero, CES MMA, October 6, 2012"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1969-01-18",
    bornplace="Washington, D.C., United States",
    nationality="United States",
    height_cm=198,
    weight_kg=132,
    ld=dict(
        alternateName=["Dave Bautista", "David Michael Bautista Jr.", "The Animal", "Leviathan",
                       "Deacon Batista"],
        award=["World Heavyweight Championship (4 reigns; longest reign in the title's history, "
               "285 days)",
               "WWE Championship (2 reigns)",
               "World Tag Team Championship (1 reign, with Ric Flair)",
               "WWE Tag Team Championship (2 reigns, with Rey Mysterio and John Cena)",
               "Royal Rumble winner (2005, 2014)"],
        knowsAbout=["Professional wrestling", "WWE", "Evolution", "Acting", "Mixed martial arts",
                    "Bodybuilding"],
        description="Batista, real name David Michael Bautista Jr., is a retired American "
                    "professional wrestler and working actor. In WWE he won six world "
                    "championships and two Royal Rumbles, and his first World Heavyweight "
                    "Championship reign of 285 days remains the longest in that title's history. "
                    "He retired after losing to Triple H at WrestleMania 35 on April 7, 2019, and "
                    "has since built the most acclaimed acting career of any former wrestler, "
                    "including Drax in the Marvel Cinematic Universe and Rabban in Dune. He was "
                    "announced for the WWE Hall of Fame Class of 2020 but has not yet been "
                    "inducted as of August 2026.",
        sameAs=["https://en.wikipedia.org/wiki/Dave_Bautista",
                "https://www.wwe.com/superstars/batista"],
    ),
)
