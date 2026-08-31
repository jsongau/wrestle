# -*- coding: utf-8 -*-
"""Randy Savage - dossier data.

Sources: web-verified August 31, 2026 - Wikipedia (main biography plus the WrestleMania III,
WrestleMania IV, Bash at the Beach 1996 and Spring Stampede 1998 event pages). Every match row
carries a day-precision date that appears in those sources.

Memorial page: Savage died May 20, 2011. All present-tense framing is confined to legacy; no
activity is implied anywhere.

Deliberate omissions:
  * No career win-loss total - none is verifiable across four decades and is not estimated.
  * The ICW World Heavyweight Championship reigns from his family's Kentucky promotion are
    listed without dates, which could not be verified in this pass.
  * No social links: none existed in his lifetime that can be authenticated.
"""

# ----------------------------------------------------------------- record rows
# Fifteen documented bouts - the Steamboat match that set the workrate standard, the one-night
# tournament, both halves of the Hogan arc, the four WCW title wins and the 2004 TNA farewell.
ROWS = [
    dict(result="W", date="1986-02-08", promo="WWE",
         event="Boston Garden", opponent="Tito Santana",
         stip="Singles — wins with a foreign object", title="WWF Intercontinental Championship"),
    dict(result="L", date="1987-03-29", promo="WWE", landmark=True,
         event="WrestleMania III — Pontiac Silverdome", opponent="Ricky Steamboat",
         stip="Singles — 1987 Match of the Year, PWI and the Observer", title="WWF Intercontinental Championship"),
    dict(result="W", date="1988-03-27", promo="WWE", landmark=True,
         event="WrestleMania IV — Atlantic City", opponent="Ted DiBiase",
         stip="Tournament final — his fourth win of the night", title="WWF Championship"),
    dict(result="W", date="1988-08-29", promo="WWE", type="tag",
         event="SummerSlam — Madison Square Garden", opponent="Ted DiBiase & Andre the Giant",
         stip="The Mega Powers vs The Mega Bucks, with Hulk Hogan", title=""),
    dict(result="L", date="1989-04-02", promo="WWE", landmark=True,
         event="WrestleMania V", opponent="Hulk Hogan", opponent_html=True,
         stip="The Mega Powers explode", title="WWF Championship"),
    dict(result="L", date="1991-03-24", promo="WWE", landmark=True,
         event="WrestleMania VII", opponent="The Ultimate Warrior",
         stip="Career vs career — reunited with Miss Elizabeth after the bell", title=""),
    dict(result="W", date="1991-12-03", promo="WWE",
         event="This Tuesday in Texas", opponent="Jake Roberts",
         stip="Singles — payoff to the cobra-bite angle that reinstated him", title=""),
    dict(result="W", date="1992-04-05", promo="WWE", landmark=True,
         event="WrestleMania VIII — Hoosier Dome", opponent="Ric Flair", opponent_html=True,
         stip="Singles — second WWF Championship", title="WWF Championship"),
    dict(result="L", date="1992-09-01", promo="WWE",
         event="Prime Time Wrestling taping — Hershey", opponent="Ric Flair", opponent_html=True,
         stip="Singles — aired September 14; the reign ends", title="WWF Championship"),
    dict(result="W", date="1995-11-26", promo="WCW", landmark=True, type="tag",
         event="World War 3 — Norfolk", opponent="The 60-man World War 3 field",
         stip="Three-ring battle royal for the vacant title", title="WCW World Heavyweight Championship"),
    dict(result="W", date="1996-01-22", promo="WCW",
         event="Monday Nitro", opponent="Ric Flair", opponent_html=True,
         stip="Singles — second WCW title", title="WCW World Heavyweight Championship"),
    dict(result="NC", date="1996-07-07", promo="WCW", landmark=True, type="tag",
         event="Bash at the Beach — Daytona Beach", opponent="The Outsiders & Hulk Hogan",
         stip="Hostile takeover match — takes the legdrops that announce the nWo", title=""),
    dict(result="W", date="1998-04-19", promo="WCW", landmark=True,
         event="Spring Stampede — Denver", opponent="Sting", opponent_html=True,
         stip="No disqualification — third WCW title", title="WCW World Heavyweight Championship"),
    dict(result="W", date="1999-07-11", promo="WCW",
         event="Bash at the Beach", opponent="Kevin Nash",
         stip="Tag rules put the title on the line — fourth and final WCW reign", title="WCW World Heavyweight Championship"),
    dict(result="W", date="2004-12-05", promo="TNA", landmark=True, type="tag",
         event="Turning Point — Orlando", opponent="Jeff Jarrett, Kevin Nash & Scott Hall",
         stip="Six-man tag with AJ Styles & Jeff Hardy — his final match", title=""),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Hulk Hogan": "hulk-hogan", "Ric Flair": "ric-flair", "Sting": "sting"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="randy-savage",
    name="Randy Savage",
    realname="Randy Mario Poffo",
    epithet="Macho Man",
    hook="Record & Legacy",

    meta_desc=("Randy 'Macho Man' Savage won two WWF Championships and four WCW World titles, and "
               "his WrestleMania III match with Ricky Steamboat set the standard for a generation. "
               "He died May 20, 2011. Full record, titles and career."),
    og_desc=("The Macho Man: a 414-day Intercontinental reign, four tournament wins in one night at "
             "WrestleMania IV, six world championships across WWF and WCW, and the voice and wardrobe "
             "nobody has stopped imitating since. 1952-2011."),
    tw_desc="Randy Savage, 1952-2011: six world titles, the Steamboat match, and the Mega Powers.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1973",
    height_imp="6&#8242;2&#8243;",
    weight_lb="237",
    world_titles="6",
    vitals_tagline="Oooh yeah, dig it",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="MM", title="WWE Shop", sub="Legacy merchandise · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable legend across the 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="WWE", title="Alumni Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/randy-savage"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Macho Man &middot; Macho King &middot; The Tower of Power",
    hero_tag="Columbus, Ohio &middot; <em>ICW &middot; Memphis &middot; WWF &middot; WCW &middot; TNA &middot; 1973&ndash;2004</em>",
    now_label="1952&ndash;2011",
    now_bold="Died May 20, 2011, at 58",
    now_tail=" &middot; heart disease at the wheel near Seminole, Florida &middot; inducted into the "
             "WWE Hall of Fame in 2015, accepted by his brother Lanny Poffo",
    hstats=[
        dict(value="2",   x=False, label="WWF Championships"),
        dict(value="4",   x=False, label="WCW World Titles"),
        dict(value="414", x=False, label="Day IC Reign"),
        dict(value="2015", x=True, label="Hall of Fame"),
    ],
    ghost_link="From his father's Kentucky promotion to the Silverdome",
    vlabel="Est. 1973 &middot; Columbus, Ohio",
    mono="MM",

    # ---------------------------------------------------------------- 01 overview
    correction=3,
    overview=[
        "<b>Randy Savage</b> was the best all-around performer of the WWF's 1980s boom &mdash; the "
        "one headliner of that era whose matches hold up on tape, whose promos created a whole "
        "dialect, and whose look (sequined robes, mirrored shades, cowboy hat) is still shorthand "
        "for professional wrestling itself. Born Randy Mario Poffo in Columbus, Ohio on November 15, "
        "1952, he was a minor-league baseball catcher before he was a wrestler, and he debuted in "
        "1973, working for his father Angelo Poffo's outlaw ICW promotion before Memphis and, in "
        "1985, the WWF. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">414</span>'
        '<span class="pull-cap">days as Intercontinental Champion, February 8, 1986 to March 29, 1987 &mdash; the belt&rsquo;s credibility era</span></span>'
        "He won six world championships &mdash; two WWF, four WCW &mdash; an Intercontinental title "
        "he held 414 days, and the 1987 King of the Ring tournament, and he did it all with Miss "
        "Elizabeth at ringside, the first valet act in company history that the audience treated as "
        "a love story rather than a prop.",

        "Two matches carry the reputation. At WrestleMania III on March 29, 1987 he dropped the "
        "Intercontinental Championship to Ricky Steamboat in front of the Silverdome crowd &mdash; "
        "a match built move-for-move in advance, against the improvisational habits of the era, and "
        "named 1987 Match of the Year by both Pro Wrestling Illustrated and the Wrestling Observer "
        "Newsletter. Steamboat has called it the moment that defined him; it is routinely ranked "
        "among the greatest matches ever, and it made workrate a main-event virtue in a company "
        "that had not prized it. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">4</span>'
        '<span class="pull-cap">wins in one night to take the vacant WWF Championship at WrestleMania IV</span></span>'
        "A year later, on March 27, 1988 in Atlantic City, he won the vacant WWF Championship by "
        "beating Butch Reed, Greg Valentine, One Man Gang and finally Ted DiBiase &mdash; four "
        "matches in one night, the only man to win the title that way, with Hulk Hogan neutralizing "
        "Andre the Giant in the final. The Mega Powers partnership that night produced, and its "
        "jealousy-fueled collapse, is the template heel turn: Savage dropped the title to Hogan in "
        "the WrestleMania V main event on April 2, 1989.",

        "The second half of the career keeps being underrated because the first half is so bright. "
        "The retirement match loss to The Ultimate Warrior at WrestleMania VII on March 24, 1991 "
        "&mdash; career versus career, ending with the on-camera reunion with Miss Elizabeth &mdash; "
        "is arguably the best story WWF told in that decade; the retirement itself lasted eight "
        "months, undone by the Jake Roberts cobra-bite angle. He beat Ric Flair for a second WWF "
        "Championship at WrestleMania VIII on April 5, 1992, in a feud built on Flair's fabricated "
        "claim to Elizabeth, and lost it back at a Prime Time Wrestling taping in Hershey on "
        "September 1, 1992. In WCW from December 1994, he won the World Heavyweight Championship "
        "four times &mdash; the 60-man World War 3 battle royal on November 26, 1995, from Flair on "
        "the January 22, 1996 Nitro, from Sting at Spring Stampede on April 19, 1998, and from Kevin "
        "Nash at Bash at the Beach on July 11, 1999 &mdash; and he was the man taking the legdrops "
        "at Bash at the Beach 1996 when Hogan turned and the nWo was born. His final match was a "
        "winning six-man tag for TNA at Turning Point on December 5, 2004, at 52.",

        "About the death, one correction worth making: he did not die in a car crash, exactly. On "
        "the morning of May 20, 2011, driving near Seminole, Florida with his second wife Lynn, he "
        "lost consciousness at the wheel and the vehicle left the road; the medical examiner found "
        "he had suffered sudden cardiac death from atherosclerotic heart disease &mdash; an enlarged "
        "heart and advanced coronary artery disease he had no diagnosis for &mdash; and the crash "
        "injuries themselves were minor. He was 58. WWE inducted him into the Hall of Fame in 2015, "
        "with Hulk Hogan &mdash; estranged from him for most of the 2000s &mdash; delivering the "
        "induction and his brother Lanny Poffo accepting with a poem, and a statue of him went up "
        "at that year's WrestleMania Axxess. The catchphrases, the Slim Jim ads, the &ldquo;Macho "
        "Man&rdquo; of it all have outlived him so thoroughly that the sharpest in-ring worker of "
        "his generation is now remembered first as a voice. Both memories are accurate.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE", "WCW", "TNA"],
        promo_labels={"WWE": "WWF/WWE", "WCW": "WCW", "TNA": "TNA"},
        stats=[
            ("2&times;", "WWF Champion"),
            ("4&times;", "WCW World Champion"),
            ("414",      "Day IC reign"),
            ("4",        "Wins in one night, WM IV"),
            ("1987",     "MOTY vs Steamboat"),
            ("1",        "King of the Ring"),
        ],
        lead=("Fifteen documented bouts &mdash; the Steamboat masterpiece, the one-night tournament, "
              "the Mega Powers arc from formation to explosion, all four WCW title wins and the 2004 "
              "TNA six-man that closed the career. A curated ledger, not a career count: no verified "
              "win&ndash;loss total exists across ICW, Memphis, WWF, WCW and TNA, and none is "
              "published. The September 1992 Flair row is dated to the Hershey taping; it aired "
              "September 14. Filter by match type, tap any column header to sort, and turn spoilers "
              "on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the reputation rests on. Only the first has a verifiable Dave "
                    "Meltzer rating &mdash; where the rating column shows a dash, none is claimed "
                    "rather than one invented."),
    signature=[
        dict(rating="5.0", event="WrestleMania III — Pontiac Silverdome", opponent="Ricky Steamboat",
             stip="Intercontinental Championship — 1987 Match of the Year, PWI and Observer"),
        dict(rating="&mdash;", event="WrestleMania IV — Atlantic City", opponent="Ted DiBiase",
             stip="Tournament final — fourth win of the night for the vacant WWF Championship"),
        dict(rating="&mdash;", event="WrestleMania VII", opponent="The Ultimate Warrior",
             stip="Career vs career — the Elizabeth reunion"),
        dict(rating="&mdash;", event="WrestleMania VIII — Hoosier Dome", opponent="Ric Flair",
             stip="WWF Championship — the feud over Elizabeth's honor"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("2&times;", "WWF Championship"),
            ("4&times;", "WCW World Heavyweight"),
            ("414",      "Day IC reign"),
            ("1",        "King of the Ring"),
        ],
        lead=("Six world championships and the Intercontinental reign that made the workrate belt "
              "mean something. The early-career titles from his family's ICW promotion are listed "
              "without dates rather than guessed at."),
        rows=[
            dict(ic="W", name="WWF Championship", count="2",
                 sub="March 27, 1988 &ndash; April 2, 1989 &middot; won the vacant title through the "
                     "WrestleMania IV tournament, lost to Hulk Hogan at WrestleMania V &middot; "
                     "regained from Ric Flair at WrestleMania VIII, April 5, 1992, lost back to Flair "
                     "at the September 1, 1992 Hershey taping"),
            dict(ic="I", name="WWF Intercontinental Championship", count="1",
                 sub="February 8, 1986 &ndash; March 29, 1987 &middot; def. Tito Santana at the Boston "
                     "Garden, lost to Ricky Steamboat at WrestleMania III &middot; <b>414 days</b>, "
                     "and the definitive run with the belt of that era"),
            dict(ic="C", name="WCW World Heavyweight Championship", count="4",
                 sub="November 26, 1995 (World War 3 battle royal) &middot; January 22, 1996 (def. "
                     "Ric Flair, Nitro) &middot; April 19, 1998 (def. Sting, Spring Stampede) &middot; "
                     "July 11, 1999 (def. Kevin Nash, Bash at the Beach)"),
            dict(ic="K", name="King of the Ring", count="1",
                 sub="Won the 1987 tournament, the pre-pay-per-view edition &mdash; the crown became "
                     "the Macho King act two years later"),
            dict(ic="X", name="ICW World Heavyweight Championship", count="3",
                 sub="His father Angelo Poffo&rsquo;s Kentucky outlaw promotion &middot; reign dates "
                     "not verified in this pass"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Alliances",
        lead="He worked best alone with one person at ringside &mdash; but three alliances shaped "
             "the career.",
        cards=[
            dict(era="WWF &middot; 1987&ndash;1989",
                 name="The Mega Powers",
                 members="Randy Savage, Hulk Hogan, Miss Elizabeth",
                 desc="Formed when Elizabeth brought Hogan to ringside during the WrestleMania IV "
                      "final; they headlined SummerSlam 1988 against DiBiase and Andre. The collapse "
                      "— Savage's on-screen jealousy over Elizabeth, the slap heard on The Main "
                      "Event in February 1989 — built to the WrestleMania V main event, where Hogan "
                      "took his title. It remains the reference implementation of the "
                      "partner-turned-rival program."),
            dict(era="WCW &middot; 1997&ndash;1998",
                 name="nWo / nWo Wolfpac",
                 members="Savage, Hogan, Hall, Nash and the rotating roster",
                 desc="The man the nWo was announced upon — flattened by three Hogan legdrops at "
                      "Bash at the Beach 1996 — eventually joined it, then sided with the red-and-"
                      "black Wolfpac splinter in 1998. His Spring Stampede 1998 title win came in "
                      "the middle of the split, with Wolfpac and Hollywood factions interfering in "
                      "opposite directions."),
            dict(era="WCW &middot; 1999",
                 name="Team Madness",
                 members="Savage, Gorgeous George, Madusa, Miss Madness",
                 desc="The final reinvention: pinstripes, an entourage, and the July 11, 1999 title "
                      "win over Kevin Nash. The reign lasted one day — Hogan took the belt the next "
                      "night on Nitro — and the act dissolved within months, effectively ending his "
                      "full-time career."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One voice, several crowns: <b>The Spider</b> (early 1970s) &rarr; <b>Macho Man</b> "
             "(1985&ndash;1989) &rarr; <b>Macho King</b> (1989&ndash;1991) &rarr; the WCW years "
             "(1994&ndash;2000). The name Savage was a Memphis invention; the wardrobe was his own.",
        cards=[
            dict(mono="SP", era="ICW &amp; territories &middot; 1973&ndash;1985", name="The Spider / Randy Savage",
                 desc="A former minor-league catcher in the Cardinals and Reds organizations, he "
                      "worked masked as The Spider early on and took the Savage name in Memphis, "
                      "where his family's outlaw ICW promotion had made the Poffos personae non "
                      "gratae with the establishment. The chip on the shoulder never left the act."),
            dict(mono="MM", era="WWF &middot; 1985&ndash;1989", name="Macho Man",
                 desc="The paranoid, explosive heel-then-hero with Miss Elizabeth at ringside — the "
                      "raspy growl, the pointed finger, the top-rope elbow. The 414-day "
                      "Intercontinental reign and the Steamboat match made him the company's "
                      "credibility; the tournament win at WrestleMania IV made him its champion."),
            dict(mono="MK", era="WWF &middot; 1989&ndash;1991", name="Macho King",
                 desc="Crowned after beating Jim Duggan for the King of the Ring lineage crown, with "
                      "Sensational Sherri replacing Elizabeth. The act ended at WrestleMania VII — "
                      "career lost to the Ultimate Warrior, Sherri turning on him, and Elizabeth "
                      "coming out of the crowd for the reunion that made grown men cry on camera."),
            dict(mono="WC", era="WCW &middot; 1994&ndash;2000", name="The WCW Savage",
                 desc="Four world titles, the nWo and Wolfpac detours, and the Team Madness finale. "
                      "Increasingly a nostalgia headliner, but the World War 3 win, two Flair "
                      "programs and the Spring Stampede 1998 title change kept him in every main "
                      "event picture the company drew until injuries ended the run."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="From minor-league dugouts to the Silverdome, and out through Orlando in 2004.",
        rows=[
            dict(year="1973", title="Debut, via baseball",
                 desc="Debuts during the off-season of a minor-league catching career in the "
                      "Cardinals and Reds systems; works his family's ICW promotion and the Memphis "
                      "territory through the early 1980s."),
            dict(year="1985", title="Signs with the WWF",
                 desc="Arrives as the hottest free agent in the territories, with every heel manager "
                      "on television bidding for him; he chooses the unknown Miss Elizabeth "
                      "instead."),
            dict(year="1986", title="Intercontinental Champion",
                 desc="Beats Tito Santana at the Boston Garden on February 8. The 414-day reign "
                      "defines the belt for the era."),
            dict(year="1987", title="The Steamboat match",
                 desc="Drops the title to Ricky Steamboat at WrestleMania III on March 29 — 1987 "
                      "Match of the Year in PWI and the Observer, and the match that made workrate "
                      "a WWF main-event virtue. Wins the King of the Ring tournament that "
                      "September."),
            dict(year="1988", title="WWF Champion in one night",
                 desc="Wins four matches at WrestleMania IV on March 27, beating Ted DiBiase in the "
                      "final for the vacant title. The Mega Powers form the same night."),
            dict(year="1989", title="The Mega Powers explode",
                 desc="Turns on Hogan over Miss Elizabeth in February; loses the title to him in "
                      "the WrestleMania V main event on April 2."),
            dict(year="1991", title="Retired, unretired",
                 desc="Loses the career-vs-career match to the Ultimate Warrior at WrestleMania VII "
                      "on March 24 — then Jake Roberts' king cobra bites him on television, and the "
                      "public demand for the payoff forces his reinstatement by November."),
            dict(year="1992", title="Champion again, against Flair",
                 desc="Beats Ric Flair at WrestleMania VIII on April 5 for a second WWF Championship, "
                      "in the feud over Flair's doctored photos of Elizabeth; drops it back to Flair "
                      "at the September 1 Hershey taping."),
            dict(year="1994", title="To WCW",
                 desc="Debuts in December 1994, reuniting with Hogan on the other channel."),
            dict(year="1995", title="WCW Champion",
                 desc="Wins the 60-man World War 3 battle royal on November 26 for the vacant title; "
                      "adds a second from Flair on Nitro on January 22, 1996."),
            dict(year="1996", title="Ground zero for the nWo",
                 desc="Takes the three legdrops from the turning Hogan at Bash at the Beach on July "
                      "7 — the single most consequential angle of the decade lands on him."),
            dict(year="1998", title="Third and fourth reigns",
                 desc="Beats Sting at Spring Stampede on April 19, 1998, and Kevin Nash at Bash at "
                      "the Beach on July 11, 1999 — each reign measured in days, as the company "
                      "spiraled."),
            dict(year="2004", title="The final match",
                 desc="Returns at 52 for TNA and wins the Turning Point six-man on December 5 with "
                      "AJ Styles and Jeff Hardy against Jarrett, Nash and Hall. He never wrestles "
                      "again."),
            dict(year="2011", title="Death, and the delayed flowers",
                 desc="Dies May 20, 2011 of sudden cardiac death at the wheel near Seminole, "
                      "Florida, at 58. WWE inducts him into the Hall of Fame in 2015 — Hogan "
                      "inducting, Lanny Poffo accepting."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Ricky Steamboat",
                 desc="The crushed-larynx angle — Savage driving the ring bell off the top rope onto "
                      "Steamboat's throat in late 1986 — built to WrestleMania III on March 29, "
                      "1987, a match the two rehearsed move by move against every custom of the "
                      "day. It won every Match of the Year award going, and it is the match that "
                      "made both men permanent."),
            dict(name="Hulk Hogan", slug="hulk-hogan",
                 desc="Partner, then enemy, then colleague, then enemy again — the Mega Powers "
                      "explosion at WrestleMania V on April 2, 1989 was the biggest match the WWF "
                      "could book, and the Bash at the Beach 1996 legdrops put Savage under the "
                      "nWo's founding image. Off screen the friendship fractured for most of the "
                      "2000s; Hogan delivering his 2015 Hall of Fame induction was the public "
                      "reconciliation, four years too late for Savage to see it."),
            dict(name="Ric Flair", slug="ric-flair",
                 desc="Two companies, two eras. In the WWF, Flair's fabricated claim that Elizabeth "
                      "had been &ldquo;his&rdquo; first fueled WrestleMania VIII on April 5, 1992, "
                      "where Savage took the title; Flair took it back that September. In WCW they "
                      "traded the World Heavyweight Championship in 1995-96 and worked a bitter "
                      "1995-96 program that ran through Nitro's first year."),
            dict(name="The Ultimate Warrior",
                 desc="Career versus career at WrestleMania VII on March 24, 1991 — five elbow "
                      "drops could not keep Warrior down, and the loss ended the Macho King. What "
                      "followed, Sherri's attack and Elizabeth's rescue from the front row, is the "
                      "most replayed non-finish moment in early WrestleMania history."),
            dict(name="Jake Roberts",
                 desc="The angle that unretired him: Roberts, refused a wedding invitation, ambushed "
                      "the Savages at their on-screen reception and later had his devenomized king "
                      "cobra bite Savage's arm on television — footage stations cut around. The "
                      "payoff win came at This Tuesday in Texas on December 3, 1991."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Voice",
        lead="The voice did as much work as the elbow. Verified entries only.",
        rows=[
            dict(when="1990s", title="Slim Jim", kind="Ads",
                 desc="&ldquo;Snap into a Slim Jim!&rdquo; — the spokesman run that kept him on "
                      "television between falls and made him a celebrity to people who never "
                      "watched wrestling."),
            dict(when="2002", title="Spider-Man", kind="Film",
                 desc="Bonesaw McGraw, the cage-match wrestler who mauls Tobey Maguire's Peter "
                      "Parker — a rare mainstream film role played entirely within his own act."),
            dict(when="2003", title="Be a Man", kind="Album",
                 desc="A rap album released October 7, 2003, including a diss track aimed at Hulk "
                      "Hogan. Reviewed about as well as you would expect; collected ever since."),
            dict(when="1985&ndash;", title="&ldquo;Pomp and Circumstance&rdquo;", kind="Music",
                 desc="Elgar's graduation processional as an entrance theme — one of the era's "
                      "great incongruities, and permanently his."),
            dict(when="2015", title="WWE Hall of Fame &amp; A&amp;E biography", kind="Legacy",
                 desc="The 2015 induction, a WrestleMania Axxess statue the same year, and a later "
                      "A&amp;E Biography episode anchor the posthumous canon."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, and the framing the sources actually support.",
        stats=[
            ("6",   "World title reigns"),
            ("414", "Days as IC Champion"),
            ("4",   "Wins in one night, WM IV"),
        ],
        rows=[
            dict(name="Six world championships across WWF and WCW",
                 sub="Two WWF Championships (1988, 1992) and four WCW World Heavyweight Championships "
                     "(1995, 1996, 1998, 1999)."),
            dict(name="Only man to win the WWF Championship via a one-night tournament",
                 sub="Four wins at WrestleMania IV on March 27, 1988 — Butch Reed, Greg Valentine, "
                     "One Man Gang, Ted DiBiase — for the vacant title. The 14-man bracket has never "
                     "been rerun for the top title."),
            dict(name="414 days as Intercontinental Champion",
                 sub="February 8, 1986 to March 29, 1987. The reign ended in the Steamboat match, "
                     "which is the rare title loss that raised the loser's standing."),
            dict(name="1987 Match of the Year, twice over",
                 sub="The WrestleMania III Steamboat match took the award from both Pro Wrestling "
                     "Illustrated and the Wrestling Observer Newsletter, and appears near the top of "
                     "essentially every greatest-matches list compiled since."),
            dict(name="King of the Ring, 1987",
                 sub="Won the tournament in its pre-pay-per-view era; the crown became the Macho "
                     "King character in 1989."),
            dict(name="The nWo was announced on his chest",
                 sub="He took the three Hogan legdrops at Bash at the Beach on July 7, 1996 — the "
                     "most consequential heel turn in the business's history required a victim the "
                     "audience loved, and it was him."),
            dict(name="WWE Hall of Fame, 2015",
                 sub="Inducted posthumously by Hulk Hogan, accepted by Lanny Poffo with a poem. The "
                     "long wait — four years after his death, fourteen after his last WWE "
                     "appearance — was itself a running story."),
            dict(name="A career on two clocks",
                 sub="A professional baseball career (Cardinals and Reds farm systems, 1971-1974) "
                     "before the wrestling one; he taught himself to throw left-handed after a "
                     "collision injured his right shoulder. The obsessiveness became the wrestling "
                     "style."),
        ],
        footnote=("No career win-loss total is published: none can be verified across ICW, Memphis, "
                  "the WWF, WCW and TNA. The ICW World Heavyweight reigns are listed without dates "
                  "for the same reason. His fourth WCW reign is dated July 11, 1999 per Wikipedia; "
                  "it ended the following night on Nitro, which is stated in prose rather than "
                  "given its own row because the loss's own details were not verified in this "
                  "pass."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Randy_Savage"),
        dict(k="Wikipedia", v="WrestleMania III — the Steamboat match",
             href="https://en.wikipedia.org/wiki/WrestleMania_III"),
        dict(k="Wikipedia", v="WrestleMania IV — the one-night tournament",
             href="https://en.wikipedia.org/wiki/WrestleMania_IV"),
        dict(k="Wikipedia", v="Bash at the Beach 1996 — the nWo turn lands on him",
             href="https://en.wikipedia.org/wiki/Bash_at_the_Beach_(1996)"),
        dict(k="Wikipedia", v="Spring Stampede 1998 — third WCW title",
             href="https://en.wikipedia.org/wiki/Spring_Stampede_(1998)"),
        dict(k="WWE.com", v="Alumni profile", href="https://www.wwe.com/superstars/randy-savage"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="How did Randy Savage die?",
            a="On the morning of May 20, 2011, driving near Seminole, Florida, he lost consciousness "
              "at the wheel and his vehicle left the road. The medical examiner found he had "
              "suffered sudden cardiac death from <b>atherosclerotic heart disease</b> &mdash; an "
              "enlarged heart and advanced coronary artery disease &mdash; and that the crash "
              "injuries were minor: the heart failed first, not the driving. His wife Lynn, in the "
              "passenger seat, survived. He was 58.",
            q_ld="How did Randy Savage die?",
            a_ld="Randy Savage died on May 20, 2011, at age 58, while driving near Seminole, "
                 "Florida. He suffered sudden cardiac death from atherosclerotic heart disease, "
                 "with an enlarged heart and advanced coronary artery disease, lost consciousness "
                 "at the wheel, and the vehicle left the road. The medical examiner determined the "
                 "crash injuries were minor and the heart condition was the cause of death. His "
                 "wife Lynn, a passenger, survived."),
        dict(
            q="How many world titles did Randy Savage win?",
            a="Six: two WWF Championships and four WCW World Heavyweight Championships. The first "
              "came through the WrestleMania IV tournament on March 27, 1988 &mdash; four wins in "
              "one night for the vacant title &mdash; and the second from Ric Flair at WrestleMania "
              "VIII on April 5, 1992. The WCW four: the World War 3 battle royal (November 26, "
              "1995), Flair on Nitro (January 22, 1996), Sting at Spring Stampede (April 19, 1998) "
              "and Kevin Nash at Bash at the Beach (July 11, 1999). He also held the "
              "Intercontinental Championship for 414 days and won the 1987 King of the Ring.",
            q_ld="How many world championships did Randy Savage win?",
            a_ld="Randy Savage won six world championships: two WWF Championships and four WCW World "
                 "Heavyweight Championships. He won his first WWF Championship through a one-night, "
                 "four-match tournament at WrestleMania IV on March 27, 1988, and his second from "
                 "Ric Flair at WrestleMania VIII on April 5, 1992. His WCW titles came on November "
                 "26, 1995, January 22, 1996, April 19, 1998 and July 11, 1999. He also held the "
                 "Intercontinental Championship for 414 days."),
        dict(
            q="Is the Steamboat match really that good?",
            a="It holds up. WrestleMania III, March 29, 1987: he dropped the Intercontinental "
              "Championship to Ricky Steamboat in a match the two of them had planned essentially "
              "move for move, against the ad-libbed norms of the era. It won 1987 Match of the Year "
              "from both PWI and the Wrestling Observer, Steamboat calls it the match that defined "
              "him, and generations of wrestlers &mdash; from the two men's own testimony to "
              "decades of best-ever lists &mdash; cite it as the one that taught them structure. On "
              "a card remembered for Hogan slamming Andre, it is the match the workers remember.",
            q_ld="Is Randy Savage versus Ricky Steamboat at WrestleMania III considered a great match?",
            a_ld="Yes. Randy Savage lost the Intercontinental Championship to Ricky Steamboat at "
                 "WrestleMania III on March 29, 1987, in a match the two planned in unusual detail "
                 "beforehand. It won 1987 Match of the Year honors from both Pro Wrestling "
                 "Illustrated and the Wrestling Observer Newsletter, and it is regularly ranked "
                 "among the greatest professional wrestling matches ever."),
        dict(
            q="What was Randy Savage&rsquo;s last match?",
            a="A win, at 52: the TNA Turning Point six-man on <b>December 5, 2004</b>, teaming with "
              "AJ Styles and Jeff Hardy against Jeff Jarrett, Kevin Nash and Scott Hall. His WWF "
              "retirement match &mdash; the WrestleMania VII career-vs-career loss to the Ultimate "
              "Warrior on March 24, 1991 &mdash; famously did not stick; the 2004 one did.",
            q_ld="What was Randy Savage's last match?",
            a_ld="Randy Savage's final match was at TNA Turning Point on December 5, 2004, when he "
                 "teamed with AJ Styles and Jeff Hardy to defeat Jeff Jarrett, Kevin Nash and Scott "
                 "Hall. He was 52. His earlier retirement match, a career-versus-career loss to The "
                 "Ultimate Warrior at WrestleMania VII on March 24, 1991, was reversed by "
                 "reinstatement later in 1991."),
        dict(
            q="Why did Savage and Miss Elizabeth matter so much?",
            a="Because the WWF had never presented a valet as a person before. Elizabeth Hulette "
              "&mdash; his real-life wife from 1984 to 1992 &mdash; stood at ringside not as a prop "
              "but as the story: his on-screen jealousy over her broke up the Mega Powers, Flair's "
              "invented history with her fueled WrestleMania VIII, and her walk from the crowd to "
              "the ring after his WrestleMania VII retirement loss is one of the form&rsquo;s "
              "genuinely moving moments. She died in 2003; he died in 2011; the act remains the "
              "standard every on-screen wrestling couple is measured against.",
            q_ld="Why were Randy Savage and Miss Elizabeth significant as an on-screen pairing?",
            a_ld="Randy Savage and Miss Elizabeth, his real-life wife from 1984 to 1992, formed the "
                 "first WWF valet act treated as a genuine love story. The jealousy storyline "
                 "between them broke up the Mega Powers in 1989, Ric Flair's fabricated claims "
                 "about Elizabeth drove the WrestleMania VIII program in 1992, and their reunion "
                 "after Savage's retirement loss at WrestleMania VII in 1991 is one of wrestling's "
                 "most celebrated emotional moments. Elizabeth died in 2003."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Randy Mario Poffo"),
        dict(label="Born", value="November 15, 1952", sub="Columbus, Ohio"),
        dict(label="Died", value="May 20, 2011",
             sub="near Seminole, Florida &middot; sudden cardiac death &middot; age 58"),
        dict(label="Billed from", value="Sarasota, Florida"),
        dict(label="Height", value="6&#8242;2&#8243;", sub="188 cm"),
        dict(label="Weight", value="237 lb", sub="108 kg (billed)"),
        dict(label="Debut", value="1973", sub="off-seasons of a minor-league baseball career"),
        dict(label="Trained by", value="Angelo Poffo (father)",
             sub="Wikipedia also credits Terry &ldquo;The Goose&rdquo; Stephens"),
        dict(label="Family", value="Son of Angelo Poffo, brother of Lanny Poffo",
             sub="married to Elizabeth Hulette &mdash; Miss Elizabeth &mdash; 1984&ndash;1992"),
        dict(label="Ring names", value="The Spider &rarr; Randy Savage",
             sub="Macho Man &middot; Macho King, 1989&ndash;1991"),
        dict(label="Signature", value="Diving elbow drop &middot; Double axe handle",
             sub="the elbow is the most imitated finisher of its era"),
        dict(label="Entrance theme", value="&ldquo;Pomp and Circumstance&rdquo;", sub="Elgar"),
        dict(label="Hall of Fame", value="2015",
             sub="inducted by Hulk Hogan, accepted by Lanny Poffo"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1952-11-15",
    bornplace="Columbus, Ohio",
    nationality="United States",
    height_cm=188,
    weight_kg=108,
    ld=dict(
        alternateName=["Randy Mario Poffo", "Macho Man Randy Savage", "The Macho Man",
                       "Macho King", "The Spider"],
        deathDate="2011-05-20",
        deathPlace="Seminole, Florida",
        award=["WWF Championship (2 reigns)",
               "WCW World Heavyweight Championship (4 reigns)",
               "WWF Intercontinental Championship (1 reign, 414 days)",
               "WWF King of the Ring (1987)",
               "PWI and Wrestling Observer Match of the Year (1987, vs Ricky Steamboat)",
               "WWE Hall of Fame (2015)"],
        knowsAbout=["Professional wrestling", "The Mega Powers", "WWF", "WCW", "WrestleMania",
                    "Intercontinental Championship"],
        description="Randy Savage, born Randy Mario Poffo in Columbus, Ohio, was an American "
                    "professional wrestler known as the Macho Man. He won two WWF Championships — "
                    "the first through a four-match, one-night tournament at WrestleMania IV in "
                    "1988 — and four WCW World Heavyweight Championships, held the Intercontinental "
                    "Championship for 414 days, and his WrestleMania III match against Ricky "
                    "Steamboat won 1987 Match of the Year from Pro Wrestling Illustrated and the "
                    "Wrestling Observer Newsletter. He died of heart disease on May 20, 2011, at "
                    "age 58, and was inducted into the WWE Hall of Fame in 2015.",
        sameAs=["https://en.wikipedia.org/wiki/Randy_Savage",
                "https://www.wwe.com/superstars/randy-savage"],
    ),
)
