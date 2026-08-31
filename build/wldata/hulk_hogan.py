# -*- coding: utf-8 -*-
"""Hulk Hogan - dossier data.

Sources: web-verified August 31, 2026 - Wikipedia (main biography plus the WrestleMania III,
Bash at the Beach 1994, Bash at the Beach 1996 and Starrcade 1997 event pages) and NBC News's
report on the medical examiner's findings. Every match row carries a day-precision date that
appears in one of those sources or is the canonical, multiply-documented date of a major card.

Deliberate omissions:
  * No career win-loss total. None is verifiable across a 35-year career spanning six
    promotions, and nothing is published rather than an estimate.
  * No social links. His accounts are now memorial pages run by the estate; the module links
    the official WWE alumni profile instead.
  * The WrestleMania III attendance of 93,173 is published only as the billed figure, with
    the disputed real number (about 78,000 per retrospective analyses) stated alongside it.
"""

# ----------------------------------------------------------------- record rows
# Nineteen documented bouts from debut-era stardom to the January 2012 UK tour. Dates for
# the major cards are canonical; the two 2012 rows' framing follows contemporary TNA tour
# coverage of the Manchester show as his final match.
ROWS = [
    dict(result="W", date="1984-01-23", promo="WWE", landmark=True,
         event="Madison Square Garden", opponent="The Iron Sheik",
         stip="Singles — Hulkamania begins", title="WWF Championship"),
    dict(result="W", date="1985-03-31", promo="WWE", landmark=True, type="tag",
         event="WrestleMania I", opponent="Roddy Piper & Paul Orndorff",
         stip="Tag — with Mr. T; Muhammad Ali as enforcer", title=""),
    dict(result="W", date="1987-03-29", promo="WWE", landmark=True,
         event="WrestleMania III — Pontiac Silverdome", opponent="Andre the Giant",
         stip="Singles — the bodyslam", title="WWF Championship"),
    dict(result="L", date="1988-02-05", promo="WWE", landmark=True,
         event="The Main Event", opponent="Andre the Giant",
         stip="Singles — twin-referee finish ends the 1,474-day reign", title="WWF Championship"),
    dict(result="W", date="1989-04-02", promo="WWE", landmark=True,
         event="WrestleMania V", opponent="Randy Savage", opponent_html=True,
         stip="The Mega Powers explode", title="WWF Championship"),
    dict(result="L", date="1990-04-01", promo="WWE", landmark=True,
         event="WrestleMania VI — SkyDome", opponent="The Ultimate Warrior",
         stip="Title vs title — pinned clean", title="WWF Championship"),
    dict(result="W", date="1991-03-24", promo="WWE",
         event="WrestleMania VII", opponent="Sgt. Slaughter",
         stip="Singles — third WWF title", title="WWF Championship"),
    dict(result="W", date="1993-04-04", promo="WWE",
         event="WrestleMania IX", opponent="Yokozuna",
         stip="Impromptu challenge — fifth WWF title", title="WWF Championship"),
    dict(result="W", date="1994-07-17", promo="WCW", landmark=True,
         event="Bash at the Beach — Orlando", opponent="Ric Flair", opponent_html=True,
         stip="Singles — wins the title in his first WCW match", title="WCW World Heavyweight Championship"),
    dict(result="NC", date="1996-07-07", promo="WCW", landmark=True, type="tag",
         event="Bash at the Beach — Daytona Beach", opponent="Randy Savage, Sting & Lex Luger",
         stip="Hostile takeover match — revealed as the nWo's third man", title=""),
    dict(result="W", date="1996-08-10", promo="WCW",
         event="Hog Wild — Sturgis", opponent="The Giant",
         stip="Singles — first title as Hollywood Hogan", title="WCW World Heavyweight Championship"),
    dict(result="L", date="1997-12-28", promo="WCW", landmark=True,
         event="Starrcade — Washington, D.C.", opponent="Sting", opponent_html=True,
         stip="Singles — the disputed count, restarted by Bret Hart", title="WCW World Heavyweight Championship"),
    dict(result="L", date="1998-07-06", promo="WCW", landmark=True,
         event="Monday Nitro — Georgia Dome", opponent="Goldberg", opponent_html=True,
         stip="Singles — Goldberg's title win before 40,000-plus", title="WCW World Heavyweight Championship"),
    dict(result="L", date="2002-03-17", promo="WWE", landmark=True,
         event="WrestleMania X8 — Toronto", opponent="The Rock",
         stip="Icon vs Icon — the crowd turns him face mid-match", title=""),
    dict(result="W", date="2002-04-21", promo="WWE", landmark=True,
         event="Backlash", opponent="Triple H",
         stip="Singles — sixth and final WWE title, eighteen years after the first", title="WWE Undisputed Championship"),
    dict(result="W", date="2005-08-21", promo="WWE",
         event="SummerSlam", opponent="Shawn Michaels",
         stip="Legend vs Showstopper", title=""),
    dict(result="W", date="2006-08-20", promo="WWE",
         event="SummerSlam", opponent="Randy Orton",
         stip="Singles — his last WWE match", title=""),
    dict(result="L", date="2011-10-16", promo="TNA", landmark=True,
         event="Bound for Glory — Philadelphia", opponent="Sting", opponent_html=True,
         stip="No disqualification — his last singles match", title=""),
    dict(result="W", date="2012-01-27", promo="TNA", type="tag",
         event="Impact Wrestling UK tour — Manchester", opponent="Bobby Roode, Bully Ray & Kurt Angle",
         stip="Six-man tag with Sting & James Storm — his final match", title=""),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Randy Savage": "randy-savage", "Ric Flair": "ric-flair",
                 "Sting": "sting", "Goldberg": "goldberg"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="hulk-hogan",
    name="Hulk Hogan",
    realname="Terry Gene Bollea",
    epithet="The Immortal",
    hook="Record & Legacy",

    meta_desc=("Hulk Hogan, the face of 1980s wrestling and the nWo's Hollywood Hogan, won six WWF/WWE "
               "and six WCW world championships and died July 24, 2025 at 71. Full record, titles, "
               "personas and career."),
    og_desc=("The Immortal: twelve world championships across WWF and WCW, the bodyslam of Andre the "
             "Giant before a billed 93,173, the nWo heel turn that changed the business — and a death "
             "in July 2025 that closed the book on wrestling's biggest star."),
    tw_desc="Hulk Hogan, 1953-2025: 12 world titles, WrestleMania I through X8, and the nWo.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1977",
    height_imp="6&#8242;7&#8243;",
    weight_lb="302",
    world_titles="12",
    vitals_tagline="Whatcha gonna do, brother?",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="HH", title="WWE Shop", sub="Legacy merchandise · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable legend across the 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="WWE", title="Alumni Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/hulk-hogan"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Hulkamania &middot; Hollywood Hogan &middot; The Hulkster",
    hero_tag="Augusta, Georgia &middot; <em>CWF &middot; AWA &middot; NJPW &middot; WWF &middot; WCW &middot; TNA &middot; 1977&ndash;2012</em>",
    now_label="1953&ndash;2025",
    now_bold="Died July 24, 2025, at 71",
    now_tail=" &middot; cardiac arrest at his Clearwater, Florida home; the medical examiner ruled "
             "acute myocardial infarction, with atrial fibrillation and chronic lymphocytic leukemia "
             "noted as contributing",
    hstats=[
        dict(value="6",    x=False, label="WWF/WWE Titles"),
        dict(value="6",    x=False, label="WCW Titles"),
        dict(value="2",    x=True,  label="HOF Inductions"),
        dict(value="1,474", x=False, label="Day First Reign"),
    ],
    ghost_link="From the Florida territory to the Pontiac Silverdome",
    vlabel="Est. 1977 &middot; Augusta, Georgia",
    mono="HH",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Hulk Hogan</b> was the biggest star professional wrestling has produced, and for two "
        "separate decades he was also its main event. Born Terry Gene Bollea in Augusta, Georgia on "
        "August 11, 1953, he debuted on August 10, 1977 in Fort Myers, Florida, trained by Hiro "
        "Matsuda, and became the engine of the WWF's national expansion the night he beat The Iron "
        "Sheik at Madison Square Garden on January 23, 1984. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">1,474</span>'
        '<span class="pull-cap">days in his first WWF Championship reign, January 23, 1984 to February 5, 1988</span></span>'
        "That first reign ran 1,474 days, through the first three WrestleManias, and the era it named "
        "&mdash; Hulkamania &mdash; is shorthand for the whole 1980s boom. He won the WWF Championship "
        "six times and the WCW World Heavyweight Championship six times, headlined the first nine "
        "WrestleManias in one role or another, and in 1996 did the thing almost no star of his size "
        "has ever done: he turned heel, became Hollywood Hogan, and founded the New World Order, the "
        "angle that powered WCW past the WWF for 83 consecutive weeks of Monday-night ratings. He "
        "died on July 24, 2025, at 71.",

        "The number every retrospective reaches for is <b>93,173</b> &mdash; the crowd at the Pontiac "
        "Silverdome on March 29, 1987, when he bodyslammed the 520-pound Andre the Giant at "
        "WrestleMania III. That figure is real only as a billed number: it is the attendance the WWF "
        "announced, and retrospective analyses put the actual gate near 78,000. The slam itself also "
        "carries a myth &mdash; that Andre had never been slammed before &mdash; which is false; Hogan "
        "himself had slammed him in 1980. What is true is enough: the match drew what was then the "
        "largest crowd in the company's history, the pinfall was Andre's first meaningful defeat in a "
        "WWF ring in fifteen years of booking, and the image became the single most replayed frame in "
        "the company's library. This page publishes the billed figure as a billed figure and flags "
        "the dispute, because the sources themselves do.",

        "The second act should not have worked. He left for WCW in 1994, beat Ric Flair for the WCW "
        "World Heavyweight Championship in his first match there &mdash; Bash at the Beach, July 17, "
        "1994 &mdash; and by 1996 the red-and-yellow act was dying in front of hostile crowds. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">83</span>'
        '<span class="pull-cap">consecutive weeks WCW Nitro beat Raw in the ratings during the nWo era he ignited</span></span>'
        "At Bash at the Beach on July 7, 1996 he walked out as the mystery third man alongside Scott "
        "Hall and Kevin Nash, dropped three legdrops on Randy Savage, and told the crowd to call it "
        "&ldquo;the new world order of wrestling.&rdquo; Hollywood Hogan held the WCW title through "
        "the hottest stretch in the company's history, lost it to Sting in the disputed Starrcade "
        "1997 finish and to Goldberg in front of 40,000-plus at the Georgia Dome on July 6, 1998, and "
        "came back to WWE in 2002 to be turned face by 68,000 Toronto fans mid-match against The Rock "
        "at WrestleMania X8. A month later he took the Undisputed Championship from Triple H at "
        "Backlash &mdash; his sixth WWE title, eighteen years after his first. His last WWE match was "
        "a win over Randy Orton at SummerSlam 2006; his actual final match was a six-man tag on "
        "TNA's UK tour in Manchester on January 27, 2012.",

        "The last decade complicated the legend and then ended it. In July 2015 WWE terminated his "
        "contract and scrubbed him from its website after leaked recordings caught him using racial "
        "slurs; he apologized, won a headline-making privacy suit against Gawker, and was reinstated "
        "to the Hall of Fame in July 2018. His final WWE appearance was on Raw's Netflix debut on "
        "January 6, 2025, promoting his Real American Beer brand, and he was audibly booed. He died "
        "on the morning of July 24, 2025 after a cardiac-arrest call to his Clearwater home; the "
        "Pinellas County medical examiner ruled the cause acute myocardial infarction &mdash; a heart "
        "attack &mdash; with a history of atrial fibrillation and chronic lymphocytic leukemia noted, "
        "and the manner of death natural. He was a WWE Hall of Famer twice over, inducted "
        "individually by Sylvester Stallone in 2005 and again with the nWo in 2020.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE", "WCW", "TNA"],
        promo_labels={"WWE": "WWF/WWE", "WCW": "WCW", "TNA": "TNA"},
        stats=[
            ("6&times;",  "WWF/WWE Champion"),
            ("6&times;",  "WCW World Champion"),
            ("1,474",     "Day first reign"),
            ("2&times;",  "Royal Rumble winner"),
            ("9",         "WrestleMania main events"),
            ("2&times;",  "Hall of Fame"),
        ],
        lead=("Nineteen documented bouts across four decades &mdash; the MSG title win that started "
              "Hulkamania, the Silverdome slam, both halves of the WCW arc, and the quiet TNA six-man "
              "in Manchester that actually closed the career. This is a curated ledger, not a career "
              "count: no win&ndash;loss total exists that could be verified across six promotions and "
              "35 years, so none is published. Filter by match type, tap any column header to sort, "
              "and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the reputation rests on. Hogan's canon was built on spectacle and "
                    "story rather than workrate, and no Dave Meltzer star rating could be verified "
                    "for any of them in this pass &mdash; where the rating column shows a dash, none "
                    "is claimed."),
    signature=[
        dict(rating="&mdash;", event="WrestleMania III — Pontiac Silverdome", opponent="Andre the Giant",
             stip="WWF Championship — the bodyslam, before a billed 93,173"),
        dict(rating="&mdash;", event="WrestleMania VI — SkyDome", opponent="The Ultimate Warrior",
             stip="Title vs title — the clean job that passed the torch, briefly"),
        dict(rating="&mdash;", event="Bash at the Beach 1996", opponent="Randy Savage, Sting & Lex Luger",
             stip="The heel turn — three legdrops on Savage and the birth of the nWo"),
        dict(rating="&mdash;", event="WrestleMania X8 — Toronto", opponent="The Rock",
             stip="Icon vs Icon — the crowd rewrites the match in real time"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("6&times;", "WWF/WWE Championship"),
            ("6&times;", "WCW World Heavyweight"),
            ("2&times;", "Royal Rumble winner"),
            ("2&times;", "WWE Hall of Fame"),
        ],
        lead=("Twelve world championship reigns split evenly between the two companies whose wars "
              "defined his career &mdash; and almost nothing else, because he almost never worked "
              "the midcard. He never held the Intercontinental, United States or a WWE tag team "
              "championship."),
        rows=[
            dict(ic="W", name="WWF/WWE Championship", count="6",
                 sub="First won January 23, 1984 from The Iron Sheik at Madison Square Garden; the "
                     "1,474-day first reign is the second-longest in the title&rsquo;s history, behind "
                     "only Bruno Sammartino&rsquo;s first. Sixth and final reign won from Triple H at "
                     "Backlash, April 21, 2002, as the Undisputed Championship"),
            dict(ic="C", name="WCW World Heavyweight Championship", count="6",
                 sub="First won July 17, 1994 from Ric Flair at Bash at the Beach, in his first WCW "
                     "match; held through most of the nWo's peak; lost to Goldberg on the July 6, 1998 "
                     "Nitro at the Georgia Dome"),
            dict(ic="R", name="Royal Rumble", count="2",
                 sub="Back-to-back winner, 1990 and 1991 &mdash; the first man to win consecutive "
                     "Rumbles"),
            dict(ic="I", name="IWGP League, New Japan", count="1",
                 sub="Won the inaugural 1983 IWGP League tournament on June 2, 1983, knocking out "
                     "Antonio Inoki in the final with the Axe Bomber"),
            dict(ic="H", name="WWE Hall of Fame", count="2",
                 sub="Inducted individually in 2005 by Sylvester Stallone, and again in 2020 as a "
                     "member of the nWo. Removed from the Hall of Fame listings in July 2015 and "
                     "reinstated in July 2018"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Three alliances that mattered &mdash; one that made the 1980s, one that made the 1990s, "
             "and one that made nobody's highlight reel.",
        cards=[
            dict(era="WWF &middot; 1988&ndash;1989",
                 name="The Mega Powers",
                 members="Hulk Hogan, Randy Savage, Miss Elizabeth",
                 desc="The superteam with Randy Savage that main-evented WrestleMania IV and "
                      "SummerSlam 1988, then detonated on live television when Savage turned on him "
                      "over Miss Elizabeth in February 1989. The explosion was the WrestleMania V "
                      "main event on April 2, 1989 — Hogan won the WWF Championship in it — and it "
                      "remains the template for every allies-to-enemies program since."),
            dict(era="WCW &middot; 1996&ndash;1999",
                 name="New World Order",
                 members="Hollywood Hogan, Scott Hall, Kevin Nash, and eventually dozens more",
                 desc="Founded on July 7, 1996 at Bash at the Beach when Hogan revealed himself as "
                      "the Outsiders' third man and legdropped Randy Savage. As nWo Hollywood he was "
                      "its centerpiece through the era when Nitro beat Raw 83 weeks running. The "
                      "faction splintered into Hollywood and Wolfpac halves in 1998 and reformed "
                      "repeatedly with diminishing returns; the original three went into the WWE "
                      "Hall of Fame together in 2020."),
            dict(era="TNA &middot; 2010&ndash;2011",
                 name="Immortal",
                 members="Hulk Hogan, Eric Bischoff, Jeff Jarrett, Jeff Hardy and others",
                 desc="The heel authority faction of his TNA run as on-screen boss, formed at Bound "
                      "for Glory 2010. It ended with his face turn after losing to Sting at Bound "
                      "for Glory 2011 — the last singles match of his career."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One man, two eras, and the rare heel turn that created a second career: <b>Terry "
             "Boulder</b> (1977&ndash;1979) &rarr; <b>Hulk Hogan</b> (1979&ndash;1996) &rarr; "
             "<b>Hollywood Hogan</b> (1996&ndash;2002) &rarr; the red-and-yellow again "
             "(2002&ndash;2012).",
        cards=[
            dict(mono="TB", era="Florida &amp; Alabama &middot; 1977&ndash;1979", name="Terry Boulder",
                 desc="The territory name, worked alongside a storyline brother, with a stint as "
                      "Sterling Golden. Lou Ferrigno comparisons on a Memphis talk show got him the "
                      "Hulk name; Vince McMahon Sr. added the Irish-sounding Hogan."),
            dict(mono="HH", era="AWA, NJPW &amp; WWF &middot; 1979&ndash;1996", name="Hulk Hogan",
                 desc="Say your prayers, take your vitamins. The all-American superhero whose act — "
                      "the shirt tear, the big boot, the legdrop, the hulk-up — carried the WWF's "
                      "national expansion, the first nine WrestleManias and the Rock 'n' Wrestling "
                      "crossover. In Japan, working a heavier style, he won the inaugural IWGP League "
                      "in 1983 by knocking out Antonio Inoki."),
            dict(mono="HW", era="WCW &middot; 1996&ndash;2002", name="Hollywood Hogan",
                 desc="The black-and-white heel — spray-painted belt, feathered boa, air guitar on "
                      "the title. The turn at Bash at the Beach 1996 is the most consequential in "
                      "the industry's history: it made the nWo, made Nitro, and made a generation "
                      "take a fictional business half-seriously again."),
            dict(mono="RY", era="WWE &amp; TNA &middot; 2002&ndash;2012", name="The Immortal",
                 desc="The nostalgia act, embraced rather than resisted — turned face by the Toronto "
                      "crowd at WrestleMania X8, a sixth WWE title at Backlash 2002, SummerSlam wins "
                      "over Shawn Michaels and Randy Orton, then the TNA years as on-screen boss. "
                      "Includes the brief masked Mr. America footnote in 2003."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Fort Myers, 1977, to a Manchester six-man in 2012 — and the headlines that outlived the career.",
        rows=[
            dict(year="1977", title="Debut in Florida",
                 desc="Debuts August 10, 1977 in Fort Myers, trained by Hiro Matsuda, who broke his "
                      "leg in an early session to test him."),
            dict(year="1984", title="Hulkamania begins",
                 desc="Beats The Iron Sheik for the WWF Championship at Madison Square Garden on "
                      "January 23. The reign runs 1,474 days and underwrites the national expansion."),
            dict(year="1987", title="The slam at the Silverdome",
                 desc="Bodyslams and pins Andre the Giant at WrestleMania III on March 29 before a "
                      "billed 93,173, the defining image of the boom."),
            dict(year="1988", title="The reign ends; the Mega Powers form",
                 desc="Drops the title to Andre on The Main Event, February 5, via the twin-Hebner "
                      "screwjob. Forms the Mega Powers with Randy Savage, whose WrestleMania IV "
                      "tournament win he assists."),
            dict(year="1989", title="Mega Powers explode",
                 desc="Beats Savage for the WWF Championship in the WrestleMania V main event on "
                      "April 2."),
            dict(year="1990", title="Passing the torch, briefly",
                 desc="Loses clean to The Ultimate Warrior, title versus title, at WrestleMania VI on "
                      "April 1 — then is champion again within a year, beating Sgt. Slaughter at "
                      "WrestleMania VII."),
            dict(year="1994", title="To WCW",
                 desc="Beats Ric Flair for the WCW World Heavyweight Championship at Bash at the "
                      "Beach on July 17, in his first match with the company."),
            dict(year="1996", title="The heel turn",
                 desc="Reveals himself as the nWo's third man at Bash at the Beach on July 7. "
                      "Hollywood Hogan and the nWo power WCW to 83 straight weekly ratings wins over "
                      "the WWF."),
            dict(year="1998", title="Goldberg and the long slide",
                 desc="Drops the WCW title to Goldberg before 40,000-plus at the Georgia Dome on the "
                      "July 6 Nitro — after the Starrcade 1997 finish against Sting had already "
                      "curdled the nWo's peak."),
            dict(year="2002", title="Toronto turns him face",
                 desc="Loses to The Rock at WrestleMania X8 on March 17 as the crowd cheers him into "
                      "a babyface turn mid-match, then beats Triple H at Backlash on April 21 for a "
                      "sixth WWE title."),
            dict(year="2006", title="Last WWE match",
                 desc="Beats Randy Orton at SummerSlam on August 20. The 2005 Hall of Fame induction "
                      "by Sylvester Stallone had already framed the send-off."),
            dict(year="2012", title="The actual final match",
                 desc="After the TNA years as on-screen boss and a Bound for Glory loss to Sting in "
                      "October 2011, he wrestles his last match on January 27, 2012 in Manchester, "
                      "England — a winning six-man tag with Sting and James Storm."),
            dict(year="2015", title="Terminated, then reinstated",
                 desc="WWE terminates his contract in July 2015 over leaked recordings of racial "
                      "slurs and removes him from its website; he is reinstated to the Hall of Fame "
                      "in July 2018 after public apologies."),
            dict(year="2025", title="Death at 71",
                 desc="Dies July 24, 2025 after cardiac arrest at his Clearwater, Florida home. The "
                      "medical examiner rules acute myocardial infarction, natural causes, with "
                      "atrial fibrillation and chronic lymphocytic leukemia contributing. His last "
                      "WWE appearance was Raw's Netflix debut on January 6, 2025."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Andre the Giant",
                 desc="Friend, mentor figure, then the immovable object of WrestleMania III — the "
                      "slam and pinfall on March 29, 1987 made Hogan the industry's permanent "
                      "headline. Andre took the title back on The Main Event on February 5, 1988 via "
                      "the twin-referee screwjob and sold it to Ted DiBiase, the angle that forced "
                      "the WrestleMania IV tournament."),
            dict(name="Randy Savage", slug="randy-savage",
                 desc="The whole arc of late-80s WWF: allies as the Mega Powers, enemies by "
                      "WrestleMania V, where Hogan took Savage's title on April 2, 1989. Seven years "
                      "later the two were the axis of the nWo angle from the other side — the three "
                      "legdrops Hogan dropped on Savage at Bash at the Beach 1996 are the turn "
                      "itself."),
            dict(name="The Ultimate Warrior",
                 desc="Title versus title at WrestleMania VI, April 1, 1990, in the SkyDome — the "
                      "rare Hogan clean loss, given to the man positioned as his successor. The "
                      "sequel, WCW's Halloween Havoc 1998 rematch, is remembered as one of the worst "
                      "high-profile matches ever, which is its own kind of bookend."),
            dict(name="Ric Flair", slug="ric-flair",
                 desc="The dream match the WWF never ran at WrestleMania: they finally settled it in "
                      "WCW, where Hogan beat Flair for the title at Bash at the Beach 1994 in his "
                      "first match with the company, and the two traded it through 1994-95 and again "
                      "in 1999. The rivalry is the bridge between the two eras of the business each "
                      "man owned."),
            dict(name="Sting", slug="sting",
                 desc="Eighteen months of Sting in the rafters pointing a bat at the nWo built to "
                      "Starrcade, December 28, 1997 — the biggest gate in WCW history and a finish "
                      "so bungled it damaged both men. Sting also ended Hogan's singles career, "
                      "beating him at TNA's Bound for Glory on October 16, 2011."),
            dict(name="Goldberg", slug="goldberg",
                 desc="One night rather than a program: July 6, 1998, Nitro at the Georgia Dome, "
                      "Hogan put the streaking Goldberg over clean in front of 40,000-plus — the "
                      "biggest single unselfish call of his WCW run, given away on free television."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Business",
        lead="The most heavily merchandised and cross-promoted wrestler of his century — trimmed here "
             "to the entries that are verifiable and mattered.",
        rows=[
            dict(when="1982", title="Rocky III", kind="Film",
                 desc="Thunderlips, opposite Sylvester Stallone — the role that made Vince McMahon "
                      "Sr. briefly fire him and made his national profile. Stallone inducted him "
                      "into the Hall of Fame 23 years later."),
            dict(when="1989", title="No Holds Barred", kind="Film",
                 desc="The WWF-produced vehicle, followed by a run of family films (Suburban "
                      "Commando, Mr. Nanny) and the syndicated series Thunder in Paradise."),
            dict(when="1985&ndash;", title="Rock 'n' Wrestling &amp; Real American", kind="Music/TV",
                 desc="The Saturday-morning cartoon bearing his likeness, and Rick Derringer's "
                      "&ldquo;Real American&rdquo; — the entrance theme that became shorthand for "
                      "the character and was later licensed for his beer brand."),
            dict(when="2005&ndash;2007", title="Hogan Knows Best", kind="TV",
                 desc="The VH1 family reality series, the center of his celebrity in the 2000s."),
            dict(when="2016", title="Bollea v. Gawker", kind="Court",
                 desc="The privacy suit over a leaked tape, funded in part by Peter Thiel, that won "
                      "a nine-figure judgment and bankrupted Gawker Media — a landmark case beyond "
                      "wrestling."),
            dict(when="2024&ndash;", title="Real American Beer", kind="Business",
                 desc="The brand he promoted in his final public appearances, including Raw's "
                      "Netflix debut on January 6, 2025."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records and the caveats, stated the way the sources state them.",
        stats=[
            ("12",    "World title reigns"),
            ("1,474", "Days, first WWF reign"),
            ("83",    "Weeks of Nitro wins"),
        ],
        rows=[
            dict(name="Twelve world championship reigns across WWF/WWE and WCW",
                 sub="Six WWF/WWE Championships — 1984, 1989, two in 1991, 1993 and 2002, as WWE "
                     "counts them — and six WCW World Heavyweight Championships. The split is "
                     "even, which is itself the career in one number: he was the biggest star in both "
                     "companies of the Monday Night War."),
            dict(name="1,474 days as WWF Champion in a single reign",
                 sub="January 23, 1984 to February 5, 1988 — the longest reign of wrestling's "
                     "national-television era and second all-time behind Bruno Sammartino's first."),
            dict(name="Back-to-back Royal Rumble wins, 1990 and 1991",
                 sub="The first man to win two Rumbles, and the only one to win consecutive editions "
                     "until Shawn Michaels in 1995-96."),
            dict(name="Headlined WrestleMania I through IX",
                 sub="Main-evented or co-main-evented the first nine WrestleManias — wrestling in "
                     "eight and inserting himself into the WrestleMania IX finish to win the title "
                     "in an impromptu match."),
            dict(name="The billed 93,173 at WrestleMania III",
                 sub="The WWF's announced Silverdome attendance for the Andre match on March 29, "
                     "1987; retrospective analyses put the real figure around 78,000. Published here "
                     "as what it is: the billed number."),
            dict(name="Founded the nWo — and the 83-week streak followed",
                 sub="The July 7, 1996 turn created the angle that carried WCW Nitro past Raw for 83 "
                     "consecutive weeks of head-to-head ratings. The streak belongs to the company; "
                     "the turn belongs to him."),
            dict(name="Inaugural IWGP League winner, 1983",
                 sub="Knocked out Antonio Inoki with the Axe Bomber in the final on June 2, 1983 in "
                     "Tokyo — a real shock finish in New Japan's biggest tournament, part of a "
                     "parallel Japanese career most American retrospectives skip."),
            dict(name="Two WWE Hall of Fame inductions",
                 sub="2005 individually, inducted by Sylvester Stallone; 2020 with the nWo. Both "
                     "listings were interrupted by his 2015-2018 removal from the Hall following "
                     "the leaked-recordings scandal."),
            dict(name="The 2015 termination and 2018 reinstatement",
                 sub="Not a feat, but part of any honest ledger: WWE cut ties in July 2015 after "
                     "recordings of him using racial slurs surfaced, and reinstated him in July "
                     "2018 after his public apologies. The episode permanently divided how the "
                     "audience received him, visible as late as the boos on Raw's Netflix debut in "
                     "January 2025."),
        ],
        footnote=("Bookkeeping note: his six WWF/WWE reigns are 1984 (Iron Sheik), 1989 (Savage), "
                  "1991 (Slaughter at WrestleMania VII), a brief fourth reign in December 1991 that "
                  "was vacated within days, 1993 (Yokozuna at WrestleMania IX) and 2002 (Triple H "
                  "at Backlash) — WWE's count of six total is the one published here. No career "
                  "win-loss total is published anywhere on this page: none exists that can be "
                  "verified."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Hulk_Hogan"),
        dict(k="NBC News", v="Medical examiner: heart attack, natural causes",
             href="https://www.nbcnews.com/news/us-news/hulk-hogan-71-died-heart-attack-rcna222256"),
        dict(k="Wikipedia", v="WrestleMania III — the Silverdome card",
             href="https://en.wikipedia.org/wiki/WrestleMania_III"),
        dict(k="Wikipedia", v="Bash at the Beach 1994 — first WCW match and title",
             href="https://en.wikipedia.org/wiki/Bash_at_the_Beach_(1994)"),
        dict(k="Wikipedia", v="Bash at the Beach 1996 — the nWo turn",
             href="https://en.wikipedia.org/wiki/Bash_at_the_Beach_(1996)"),
        dict(k="Wikipedia", v="Starrcade 1997 — the disputed finish with Sting",
             href="https://en.wikipedia.org/wiki/Starrcade_(1997)"),
        dict(k="WWE.com", v="Alumni profile", href="https://www.wwe.com/superstars/hulk-hogan"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="How did Hulk Hogan die?",
            a="He died on the morning of July 24, 2025, at 71, after emergency crews responded to a "
              "cardiac-arrest call at his Clearwater, Florida home. The Pinellas County medical "
              "examiner ruled the cause <b>acute myocardial infarction</b> &mdash; a heart attack "
              "&mdash; and the manner of death natural, noting a history of atrial fibrillation and "
              "chronic lymphocytic leukemia as contributing conditions. His final WWE appearance had "
              "come six months earlier, on Raw&rsquo;s Netflix debut on January 6, 2025.",
            q_ld="How did Hulk Hogan die?",
            a_ld="Hulk Hogan died on July 24, 2025, at age 71, after emergency responders answered a "
                 "cardiac arrest call at his home in Clearwater, Florida. The medical examiner ruled "
                 "the cause of death acute myocardial infarction, a heart attack, and classified the "
                 "manner of death as natural, noting a history of atrial fibrillation and chronic "
                 "lymphocytic leukemia as contributing conditions. His final WWE appearance was on "
                 "the Netflix debut episode of Raw on January 6, 2025."),
        dict(
            q="How many world titles did Hulk Hogan win?",
            a="Twelve: six WWF/WWE Championships and six WCW World Heavyweight Championships. The "
              "first came from The Iron Sheik at Madison Square Garden on January 23, 1984 and ran "
              "1,474 days; the last came from Triple H at Backlash on April 21, 2002, as the "
              "Undisputed Championship &mdash; eighteen years after the first. He also won the Royal "
              "Rumble back to back in 1990 and 1991 and never held a WWE midcard or tag title.",
            q_ld="How many world championships did Hulk Hogan win?",
            a_ld="Hulk Hogan won twelve world championships: six WWF/WWE Championships and six WCW "
                 "World Heavyweight Championships. His first WWF Championship, won from The Iron "
                 "Sheik on January 23, 1984, lasted 1,474 days. His final world title win came "
                 "against Triple H at Backlash on April 21, 2002, when he won the WWE Undisputed "
                 "Championship. He also won the Royal Rumble in 1990 and 1991."),
        dict(
            q="Did 93,173 people really watch him slam Andre the Giant?",
            a="That is the billed figure. The WWF announced 93,173 at the Pontiac Silverdome for "
              "WrestleMania III on March 29, 1987, and retrospective analyses put the actual "
              "attendance around <b>78,000</b>. Either number was the largest crowd in company "
              "history at the time. The related myth &mdash; that Andre had never been slammed "
              "before that night &mdash; is also false; Hogan himself had slammed him years earlier. "
              "The match&rsquo;s standing does not depend on either exaggeration.",
            q_ld="Did 93,173 people really attend WrestleMania III to watch Hulk Hogan slam Andre the Giant?",
            a_ld="93,173 was the attendance the WWF announced for WrestleMania III at the Pontiac "
                 "Silverdome on March 29, 1987, where Hulk Hogan bodyslammed and pinned Andre the "
                 "Giant. Retrospective analyses estimate the actual attendance was closer to 78,000. "
                 "The claim that Andre the Giant had never been bodyslammed before that match is "
                 "also inaccurate, as Hogan himself had slammed him in earlier matches."),
        dict(
            q="What was Hulk Hogan&rsquo;s last match?",
            a="A six-man tag on TNA&rsquo;s UK tour in Manchester, England on <b>January 27, 2012</b>: "
              "Hogan, Sting and James Storm beat Bobby Roode, Bully Ray and Kurt Angle. His last "
              "singles match was the loss to Sting at Bound for Glory on October 16, 2011, and his "
              "last WWE match was the SummerSlam win over Randy Orton on August 20, 2006. He was 58 "
              "when he wrestled for the final time.",
            q_ld="What was Hulk Hogan's last match?",
            a_ld="Hulk Hogan's final match was a six-man tag team match on TNA's United Kingdom tour "
                 "in Manchester, England on January 27, 2012, in which Hogan, Sting and James Storm "
                 "defeated Bobby Roode, Bully Ray and Kurt Angle. His final singles match was a loss "
                 "to Sting at TNA Bound for Glory on October 16, 2011, and his final WWE match was a "
                 "victory over Randy Orton at SummerSlam on August 20, 2006."),
        dict(
            q="Why was Hogan removed from the WWE Hall of Fame in 2015?",
            a="In July 2015, recordings surfaced of Hogan using racial slurs, made years earlier and "
              "published alongside the Gawker tape litigation. WWE terminated his contract, removed "
              "his merchandise and scrubbed his Hall of Fame listing. He apologized publicly and was "
              "reinstated on July 15, 2018, later appearing at company events through his final Raw "
              "appearance in January 2025 &mdash; where a portion of the crowd booed him, a measure "
              "of how permanently the episode divided his audience.",
            q_ld="Why was Hulk Hogan removed from the WWE Hall of Fame in 2015?",
            a_ld="WWE terminated Hulk Hogan's contract and removed his Hall of Fame listing in July "
                 "2015 after recordings surfaced of him using racial slurs. Hogan apologized "
                 "publicly, and WWE reinstated him to the Hall of Fame on July 15, 2018. He "
                 "continued to make occasional WWE appearances afterward, the last being the "
                 "Netflix debut of Raw on January 6, 2025, where parts of the crowd booed him."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Terry Gene Bollea"),
        dict(label="Born", value="August 11, 1953", sub="Augusta, Georgia"),
        dict(label="Died", value="July 24, 2025",
             sub="Clearwater, Florida &middot; heart attack, ruled natural &middot; age 71"),
        dict(label="Billed from", value="Venice Beach, California",
             sub="earlier Hollywood, California, as Hollywood Hogan"),
        dict(label="Height", value="6&#8242;7&#8243;", sub="201 cm"),
        dict(label="Weight", value="302 lb", sub="137 kg (billed)"),
        dict(label="Debut", value="August 10, 1977", sub="Fort Myers, Florida"),
        dict(label="Trained by", value="Hiro Matsuda"),
        dict(label="Ring names",
             value="Terry Boulder &rarr; Sterling Golden &rarr; Hulk Hogan &rarr; Hollywood Hogan",
             sub="plus the masked Mr. America footnote, 2003"),
        dict(label="Signature", value="Running legdrop &middot; Big boot &middot; The hulk-up",
             sub="Axe Bomber in Japan"),
        dict(label="Entrance theme", value="&ldquo;Real American&rdquo;",
             sub="Rick Derringer &middot; &ldquo;Voodoo Child&rdquo; as Hollywood Hogan in WCW"),
        dict(label="Hall of Fame", value="2005 &middot; 2020 (nWo)",
             sub="removed July 2015, reinstated July 2018"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1953-08-11",
    bornplace="Augusta, Georgia",
    nationality="United States",
    height_cm=201,
    weight_kg=137,
    ld=dict(
        alternateName=["Terry Gene Bollea", "Hollywood Hogan", "Terry Boulder", "Sterling Golden",
                       "The Hulkster", "The Immortal", "Mr. America"],
        deathDate="2025-07-24",
        deathPlace="Clearwater, Florida",
        award=["WWF/WWE Championship (6 reigns; first reign a 1,474-day run, 1984-1988)",
               "WCW World Heavyweight Championship (6 reigns)",
               "Royal Rumble winner (1990, 1991)",
               "IWGP League tournament winner (1983)",
               "WWE Hall of Fame (2005, individually; 2020, with the nWo)"],
        knowsAbout=["Professional wrestling", "Hulkamania", "New World Order", "WWF", "WCW", "TNA",
                    "WrestleMania"],
        description="Hulk Hogan, born Terry Gene Bollea in Augusta, Georgia, was an American "
                    "professional wrestler and the biggest star of wrestling's 1980s boom. He won "
                    "the WWF/WWE Championship six times, beginning with a 1,474-day reign started "
                    "on January 23, 1984, bodyslammed Andre the Giant before a billed 93,173 fans "
                    "at WrestleMania III, and won the WCW World Heavyweight Championship six times "
                    "after turning heel in 1996 to found the New World Order as Hollywood Hogan. He "
                    "wrestled his final match in January 2012 and died of a heart attack on July "
                    "24, 2025, at age 71.",
        sameAs=["https://en.wikipedia.org/wiki/Hulk_Hogan",
                "https://www.wwe.com/superstars/hulk-hogan"],
    ),
)
