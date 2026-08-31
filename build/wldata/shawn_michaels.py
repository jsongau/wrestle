# -*- coding: utf-8 -*-
"""Shawn Michaels - dossier data.

Sources: web-verified August 31, 2026 - Wikipedia (Shawn Michaels), CBS Sports (September
2022 promotion to Senior Vice President of Talent Development Creative), WWE.com (WWE LFG
season two, which lists him among the coaches), F4WOnline (September 2025, on running NXT)
and SEScoops (2026, on NXT's build-stars-to-lose-them model). Record-row dates are all
day-precision and verified.

Deliberate omissions:
  * No career win-loss total - none is reliably published, so none is invented.
  * No theme entry - "Sexy Boy" is inseparable from him, but no Spotify track URL was
    verified in this pass, so the block is omitted per house rule.
  * Tag reign endpoint dates were not re-verified to the day and are stated loosely.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="1995-01-22", promo="WWE", landmark=True, type="tag",
         event="Royal Rumble match — Tampa", opponent="The 1995 Royal Rumble field",
         stip="Enters No. 1, wins — the first man to do it from the first spot", title=""),
    dict(result="W", date="1996-01-21", promo="WWE", type="tag",
         event="Royal Rumble match — Fresno", opponent="The 1996 Royal Rumble field",
         stip="Back-to-back Rumble wins", title=""),
    dict(result="W", date="1996-03-31", promo="WWE", landmark=True,
         event="WrestleMania XII — Anaheim", opponent="Bret Hart", opponent_html=True,
         stip="60-minute Iron Man match, won in overtime — first WWF Championship",
         title="WWF Championship"),
    dict(result="L", date="1996-11-17", promo="WWE",
         event="Survivor Series — Madison Square Garden", opponent="Sycho Sid",
         stip="Singles — the title goes, the crowd cheers Sid", title="WWF Championship"),
    dict(result="W", date="1997-01-19", promo="WWE",
         event="Royal Rumble — San Antonio", opponent="Sycho Sid",
         stip="Singles — regains the title in the Alamodome, his hometown",
         title="WWF Championship"),
    dict(result="W", date="1997-10-05", promo="WWE", landmark=True,
         event="Badd Blood: In Your House — St. Louis", opponent="The Undertaker", opponent_html=True,
         stip="The first Hell in a Cell — wins after the debuting Kane intervenes", title=""),
    dict(result="W", date="1997-11-09", promo="WWE", landmark=True,
         event="Survivor Series — Montreal", opponent="Bret Hart", opponent_html=True,
         stip="The Montreal Screwjob — the bell rings, the title changes",
         title="WWF Championship"),
    dict(result="L", date="1998-03-29", promo="WWE", landmark=True,
         event="WrestleMania XIV — Boston", opponent="Stone Cold Steve Austin", opponent_html=True,
         stip="Singles — wrestles on a broken back, then vanishes for four years",
         title="WWF Championship"),
    dict(result="W", date="2002-08-25", promo="WWE", landmark=True,
         event="SummerSlam — Uniondale", opponent="Triple H",
         stip="Unsanctioned street fight — the comeback, four years after the back gave out",
         title=""),
    dict(result="W", date="2002-11-17", promo="WWE", landmark=True, type="tag",
         event="Survivor Series — Madison Square Garden",
         opponent="Triple H, Chris Jericho, Booker T, Kane & Rob Van Dam",
         stip="The first Elimination Chamber — his fourth and final world title",
         title="World Heavyweight Championship"),
    dict(result="L", date="2009-04-05", promo="WWE", landmark=True,
         event="WrestleMania 25 — Houston", opponent="The Undertaker", opponent_html=True,
         stip="Singles — the Streak match most polls call the best ever", title=""),
    dict(result="L", date="2010-03-28", promo="WWE", landmark=True,
         event="WrestleMania XXVI — Glendale", opponent="The Undertaker", opponent_html=True,
         stip="Streak vs. career, no disqualification — the retirement match", title=""),
    dict(result="W", date="2018-11-02", promo="WWE", type="tag",
         event="Crown Jewel — Riyadh", opponent="The Undertaker & Kane",
         stip="D-Generation X reunion with Triple H — his actual last match", title=""),
]

for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Bret Hart": "bret-hart", "The Undertaker": "the-undertaker",
                 "Stone Cold Steve Austin": "stone-cold-steve-austin"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="shawn-michaels",
    name="Shawn Michaels",
    realname="Michael Shawn Hickenbottom",
    epithet="The Heartbreak Kid",
    hook="Record & Titles",

    meta_desc=("Shawn Michaels won four world championships, both ends of the Montreal Screwjob "
               "story, and the nickname Mr. WrestleMania - then a second career running NXT "
               "creative as WWE's SVP of Talent Development Creative. Full record and titles."),
    og_desc=("The Heartbreak Kid: the Iron Man match, the first Hell in a Cell, the first "
             "Elimination Chamber, Montreal, two retirements - and a 2026 day job running NXT."),
    tw_desc="Mr. WrestleMania: 4 world titles, 2 careers, and NXT's creative desk since 2021.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1984",
    height_imp="6&#8242;1&#8243;",
    weight_lb="225",
    world_titles="4",
    vitals_tagline="The showstopper",
    support_note="Merch &middot; Games &middot; Watch",
    sp_items=[
        dict(ic="HBK", title="WWE Shop", sub="Official HBK and DX merch · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable legend in the 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="NXT", title="WWE NXT", sub="The brand he runs, Tuesdays",
             tag="Watch", href="https://www.wwe.com/shows/wwenxt"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/shawn-michaels"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Heartbreak Kid &middot; The Showstopper &middot; Mr. WrestleMania",
    hero_tag="San Antonio, Texas &middot; <em>Mid-South &middot; AWA &middot; WWF/WWE &middot; 1984&ndash;2010, 2018</em>",
    now_label="NOW",
    now_bold="WWE Senior VP of Talent Development Creative",
    now_tail=" &middot; running NXT&rsquo;s creative and coaching WWE LFG &mdash; &ldquo;none of "
             "it feels like work for me,&rdquo; he said in September 2025",
    hstats=[
        dict(value="4",   x=True,  label="World Titles"),
        dict(value="2",   x=True,  label="Royal Rumbles"),
        dict(value="1st", x=False, label="Grand Slam Champion"),
        dict(value="60",  x=False, label="Iron Man Minutes"),
    ],
    ghost_link="From the Rockers' hot tags to the desk that decides what NXT is",
    vlabel="Est. 1984 &middot; San Antonio, Texas",
    mono="HBK",

    # ---------------------------------------------------------------- 01 overview
    correction=2,
    overview=[
        "<b>Shawn Michaels</b> is the consensus pick for the best in-ring performer WWE ever "
        "produced, and unusually for that kind of claim, the resume argues it match by match: the "
        "60-minute Iron Man match that won him his first WWF Championship at WrestleMania XII on "
        "March 31, 1996, the first Hell in a Cell at Badd Blood on October 5, 1997, the first "
        "Elimination Chamber &mdash; which he won for his final world title at Survivor Series on "
        "November 17, 2002 &mdash; and the two WrestleMania matches against The Undertaker in 2009 "
        "and 2010 that end most greatest-match polls. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">1st</span>'
        '<span class="pull-cap">Grand Slam Champion in WWF history, completed September 20, 1997</span></span>'
        "He won four world championships &mdash; three WWF, one World Heavyweight &mdash; two "
        "Royal Rumbles back to back in 1995 and 1996, and became the company&rsquo;s first Grand "
        "Slam Champion when he added the European title on September 20, 1997. The nickname Mr. "
        "WrestleMania is not a marketing line; it is an observation about where his best matches "
        "happened.",

        "He is also half of the most infamous real moment in wrestling history. At Survivor "
        "Series in Montreal on November 9, 1997, with Bret Hart leaving for WCW and refusing to "
        "drop the title in Canada, Vince McMahon had the bell rung while Michaels held Hart in "
        "his own Sharpshooter &mdash; a finish Hart had not agreed to. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">1997</span>'
        '<span class="pull-cap">Montreal &mdash; the screwjob that ended an era and a friendship, undone only in 2010</span></span>'
        "Michaels denied involvement for years and later admitted he knew. The two men did not "
        "speak for over a decade; the reconciliation, on the January 4, 2010 Raw, was as watched "
        "as the crime. Four months after Montreal came the other career-defining moment: he "
        "wrestled WrestleMania XIV on March 29, 1998 with a back broken in a casket-match bump "
        "(two herniated discs, one crushed), dropped the title to Steve Austin, and disappeared "
        "&mdash; everyone, including him, assumed for good.",

        "Which is why his record needs one correction: the retirement match against The "
        "Undertaker at WrestleMania XXVI on March 28, 2010 &mdash; career against Streak, and "
        "the career lost &mdash; was not his last match. Eight years later he came back exactly "
        "once, teaming with Triple H as D-Generation X to beat The Undertaker and Kane at Crown "
        "Jewel in Riyadh on November 2, 2018. He has called the one-off a mistake he does not "
        "regret getting out of his system, and nothing since suggests another. The 2010 "
        "retirement remains the true career endpoint; 2018 is a footnote, but it is the "
        "footnote the record books have to print. His first retirement, 1998 to 2002, was "
        "undone more gloriously: the unsanctioned SummerSlam 2002 match against Triple H, won "
        "on August 25, 2002, opened an eight-year second career many rate above the first.",

        "Since 2010 the second act has become a genuine executive career. He joined NXT as a "
        "coach in 2016, took over the brand&rsquo;s creative when Triple H fell ill in 2021, "
        "and was formally promoted to Senior Vice President of Talent Development Creative on "
        "September 7, 2022 (CBS Sports). In 2026 he still runs NXT&rsquo;s creative day to day "
        "&mdash; he told F4WOnline in September 2025 that &ldquo;none of it feels like work for "
        "me&rdquo; &mdash; and has articulated the brand&rsquo;s odd mandate as building stars "
        "in order to lose them to Raw and SmackDown (SEScoops). He also coaches on A&amp;E&rsquo;s "
        "WWE LFG alongside The Undertaker, Booker T and Michelle McCool. He went into the Hall "
        "of Fame twice: 2011 as an individual, 2019 with D-Generation X. He is 61.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWF/WWE"},
        stats=[
            ("3&times;", "WWF Championship"),
            ("1&times;", "World Heavyweight"),
            ("2&times;", "Royal Rumble wins"),
            ("1st",      "Grand Slam Champion"),
            ("3&times;", "Intercontinental"),
            ("2&times;", "Hall of Fame"),
        ],
        lead=("Thirteen documented bouts &mdash; both Rumble wins, all four world title changes in "
              "and out, Montreal, both retirements and the 2018 coda. A curated ledger, not a "
              "career count; no career win&ndash;loss total is published because none is reliably "
              "sourced. Filter by match type, tap any column header to sort, and turn spoilers on "
              "to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the reputation rests on. Ratings are Wrestling Observer figures "
                    "as commonly reported, not re-verified against Observer archives; the "
                    "WrestleMania 25 match swept most match-of-the-year voting in 2009."),
    signature=[
        dict(rating="5.0", event="WrestleMania 25 — Houston", opponent="The Undertaker",
             stip="Singles — the Streak at 17-0"),
        dict(rating="4.75", event="WrestleMania XXVI — Glendale", opponent="The Undertaker",
             stip="Streak vs. career — his retirement match"),
        dict(rating="4.75", event="WrestleMania XIX — Seattle", opponent="Chris Jericho",
             stip="Singles — the comeback validated"),
        dict(rating="4.5", event="WrestleMania XII — Anaheim", opponent="Bret Hart",
             stip="60-minute Iron Man match for the WWF Championship"),
        dict(rating="4.5", event="WrestleMania X — Madison Square Garden", opponent="Razor Ramon",
             stip="Ladder match — the template for every ladder match since"),
    ],
    signature_count_word="five",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("3&times;", "WWF Championship"),
            ("1&times;", "World Heavyweight"),
            ("3&times;", "Intercontinental"),
            ("5&times;", "Tag team reigns"),
        ],
        lead=("Four world championships and the first Grand Slam resume in company history, "
              "completed in 1997 before the concept had a name. Tag reign endpoint dates were "
              "not re-verified to the day in this pass and are stated loosely rather than "
              "guessed."),
        rows=[
            dict(ic="W", name="WWF Championship", count="3",
                 sub="Won in the WrestleMania XII Iron Man match, March 31, 1996 (def. Bret Hart "
                     "in overtime); regained from Sycho Sid at the Royal Rumble, January 19, "
                     "1997, in his hometown Alamodome; won a third time from Hart in Montreal, "
                     "November 9, 1997 &mdash; the Screwjob &mdash; and dropped to Steve Austin "
                     "at WrestleMania XIV, March 29, 1998"),
            dict(ic="H", name="World Heavyweight Championship", count="1",
                 sub="Won the first Elimination Chamber at Survivor Series, November 17, 2002, "
                     "at Madison Square Garden &mdash; his only title of the comeback era, lost "
                     "back to Triple H at Armageddon the next month"),
            dict(ic="I", name="WWF Intercontinental Championship", count="3",
                 sub="First won from the British Bulldog in October 1992; the third reign, from "
                     "Jeff Jarrett in July 1995, set up the ladder-match era the belt is still "
                     "associated with him for"),
            dict(ic="E", name="WWF European Championship", count="1",
                 sub="Won from the British Bulldog on September 20, 1997 in Birmingham, England "
                     "&mdash; the win that made him the first Grand Slam Champion; surrendered "
                     "by lying down for Triple H that December"),
            dict(ic="T", name="Tag team championships", count="5",
                 sub="Two WWF Tag reigns with Diesel (1994-95), one with Stone Cold Steve "
                     "Austin (1997), one World Tag reign with John Cena (2007), and the "
                     "Unified Tag titles with Triple H as D-Generation X (2009)"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Three units, each of which changed the shape of the company's television.",
        cards=[
            dict(era="AWA/WWF &middot; 1985&ndash;1992",
                 name="The Rockers",
                 members="Shawn Michaels &amp; Marty Jannetty",
                 desc="The high-flying tag act that imported the fast southern style to national "
                      "TV. Never officially WWF Tag champions — a 1990 title change was voided "
                      "on a technicality — and dissolved when Michaels superkicked Jannetty "
                      "through the Barber Shop window in January 1992, still the reference "
                      "point for every tag-team betrayal since."),
            dict(era="WWF &middot; 1997&ndash;1998",
                 name="D-Generation X, the original",
                 members="Michaels, Triple H, Chyna, Rick Rude",
                 desc="The smirking, curfew-breaking unit that defined the Attitude Era's tone a "
                      "year before the era had a name. Michaels fronted it for six months before "
                      "his back forced him out at WrestleMania XIV; Triple H inherited it. "
                      "Inducted into the Hall of Fame as a group in 2019."),
            dict(era="WWE &middot; 2006&ndash;2010, 2018",
                 name="D-Generation X, the reunion",
                 members="Michaels &amp; Triple H",
                 desc="The comeback-era two-man version: Unified Tag Team Champions in 2009 by "
                      "beating Jeri-Show, and the vehicle for his actual final match, the Crown "
                      "Jewel 2018 tag against The Undertaker and Kane."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One ring name almost the whole way &mdash; the reinventions happened inside it: "
             "<b>The Rockers&rsquo; hot tag</b> &rarr; <b>The Heartbreak Kid</b> &rarr; <b>the "
             "born-again cowboy of the comeback</b>. The initials outlasted every era.",
        cards=[
            dict(mono="R", era="AWA/WWF &middot; 1985&ndash;1992", name="Rocker",
                 desc="The babyface half of a team built on speed and double-teams — the "
                      "apprenticeship where he learned everything except restraint."),
            dict(mono="HBK", era="WWF &middot; 1992&ndash;1998", name="The Heartbreak Kid",
                 desc="The mirror-gazing heel turned crowd favourite — 'Sexy Boy', the zebra "
                      "chaps, the kip-up, Sweet Chin Music. Vain, brilliant and by his own later "
                      "admission chemically unbearable backstage. Everything before the broken "
                      "back."),
            dict(mono="HBK2", era="WWE &middot; 2002&ndash;2010", name="The comeback HBK",
                 desc="Returned sober and openly devout after four years gone. The same "
                      "showstopper instincts with the recklessness sanded into judgment — most "
                      "critics rate 2002-2010 as the better half of the career, which almost "
                      "never happens after a spinal injury."),
            dict(mono="SVP", era="WWE &middot; 2016&ndash;present", name="The executive",
                 desc="Coach, then showrunner: NXT's creative lead since 2021, Senior Vice "
                      "President of Talent Development Creative since September 2022, and a "
                      "coach on WWE LFG. The gimmick now is a headset."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="A 1984 debut at nineteen to the desk that decides what NXT is.",
        rows=[
            dict(year="1984", title="Debut at nineteen",
                 desc="First match October 16, 1984 in Mid-South, trained by Jose Lothario. The "
                      "Rockers form in the AWA the following year."),
            dict(year="1992", title="The Barber Shop window",
                 desc="Superkicks Marty Jannetty through Brutus Beefcake's talk-show set in "
                      "January and becomes the Heartbreak Kid; first Intercontinental title in "
                      "October."),
            dict(year="1995-96", title="Back-to-back Rumbles, then the boyhood dream",
                 desc="Wins the 1995 Rumble from the No. 1 spot and the 1996 Rumble outright, "
                      "then beats Bret Hart in the WrestleMania XII Iron Man match on March 31, "
                      "1996 for his first WWF Championship."),
            dict(year="1997", title="Grand Slam, the first Cell, Montreal",
                 desc="Completes the first Grand Slam on September 20, wins the first Hell in a "
                      "Cell on October 5, and holds the ring in Montreal on November 9 when the "
                      "bell rings early on Bret Hart."),
            dict(year="1998", title="The back breaks",
                 desc="Herniates two discs and crushes another in a casket match at the 1998 "
                      "Royal Rumble, wrestles WrestleMania XIV anyway on March 29, loses the "
                      "title to Austin, and retires at 32."),
            dict(year="2002", title="The comeback",
                 desc="Returns after four years and beats Triple H in an unsanctioned SummerSlam "
                      "match on August 25; wins the World Heavyweight Championship in the first "
                      "Elimination Chamber on November 17."),
            dict(year="2009", title="The Undertaker matches begin",
                 desc="Loses to The Undertaker at WrestleMania 25 on April 5, 2009 in the match "
                      "both men call their best."),
            dict(year="2010", title="Career vs. Streak",
                 desc="Puts his career against the Streak in the rematch at WrestleMania XXVI on "
                      "March 28, 2010, loses, and retires to a 20-minute farewell the next "
                      "night. Hall of Fame, 2011."),
            dict(year="2016", title="To NXT",
                 desc="Joins the Performance Center as a coach and finds, by his own account, "
                      "the job that fits."),
            dict(year="2018", title="The Saudi one-off",
                 desc="Comes back for one night at Crown Jewel on November 2 — DX beats the "
                      "Brothers of Destruction — making it, technically, his final match. DX "
                      "Hall of Fame induction follows in 2019."),
            dict(year="2021-22", title="Running NXT",
                 desc="Takes over NXT creative during Triple H's health absence in 2021; "
                      "formally promoted to Senior Vice President of Talent Development "
                      "Creative on September 7, 2022."),
            dict(year="2025-26", title="The executive era in full",
                 desc="Runs NXT week to week, coaches two seasons of WWE LFG on A&E, and "
                      "spends interviews defending the brand's mandate of building stars in "
                      "order to lose them."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Bret Hart", slug="bret-hart",
                 desc="The defining rivalry, because so much of it was real: the Iron Man match "
                      "at WrestleMania XII, two years of escalating backstage contempt, and "
                      "Montreal on November 9, 1997, where the worked fight became an actual "
                      "double-cross. Michaels spent years denying he knew and eventually "
                      "admitted he did. The on-air reconciliation on January 4, 2010 — a "
                      "handshake and a hug in the ring — closed wrestling's longest-running "
                      "genuine feud."),
            dict(name="The Undertaker", slug="the-undertaker",
                 desc="The first Hell in a Cell in 1997, the 2007 Royal Rumble final pairing, "
                      "and then the two WrestleMania matches — 25 in 2009, XXVI in 2010 — that "
                      "sit at the top of most all-time lists. Michaels lost both, the second "
                      "for his career, and has said losing them was the proudest work he ever "
                      "did."),
            dict(name="Triple H",
                 desc="Best friend, DX co-founder, and the opponent of his comeback: the "
                      "unsanctioned SummerSlam 2002 street fight, a three-stages-of-hell match, "
                      "and the long 2004 triangle with Chris Benoit. Now, as WWE's head of "
                      "creative, also his boss."),
            dict(name="Stone Cold Steve Austin", slug="stone-cold-steve-austin",
                 desc="One match, maximum weight: WrestleMania XIV, March 29, 1998. Michaels "
                      "could barely walk, Mike Tyson counted the fall, and the company's "
                      "future changed hands in one Stunner."),
            dict(name="Razor Ramon",
                 desc="The WrestleMania X ladder match on March 20, 1994 — two men, two "
                      "belts hanging, and the blueprint for thirty years of ladder matches "
                      "since. They ran it back at SummerSlam 1995."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Backstage",
        lead="The current media footprint is the job itself — NXT is his show.",
        rows=[
            dict(when="2021&ndash;", title="WWE NXT", kind="Executive",
                 desc="Creative lead for the brand — on camera rarely, in charge weekly. His "
                      "promotion to Senior Vice President of Talent Development Creative was "
                      "announced September 7, 2022."),
            dict(when="2025&ndash;2026", title="WWE LFG", kind="TV",
                 desc="Coach on A&E's competition series across its first two seasons, "
                      "alongside The Undertaker, Booker T, Michelle McCool and Bubba Ray "
                      "Dudley."),
            dict(when="2005", title="Heartbreak & Triumph", kind="Book",
                 desc="Autobiography covering the Rockers, the 1990s and the born-again "
                      "comeback; a WWE-produced DVD set of the same name followed."),
            dict(when="2010", title="Shawn Michaels: My Journey", kind="Documentary",
                 desc="WWE's retirement-year retrospective; he has since been a fixture of "
                      "every Montreal documentary the company has made."),
            dict(when="2016&ndash;", title="The Resurrection of Gavin Stone", kind="Film",
                 desc="A WWE Studios faith-based drama he headlined — his one leading film "
                      "role, released January 2017."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The firsts, which is the real shape of the resume.",
        stats=[
            ("1st", "Grand Slam Champion"),
            ("1st", "Hell in a Cell win"),
            ("1st", "Elimination Chamber win"),
        ],
        rows=[
            dict(name="First Grand Slam Champion in WWF history",
                 sub="Completed September 20, 1997 with the European Championship in "
                     "Birmingham — WWF, Intercontinental, Tag and European titles all held."),
            dict(name="Won the first Hell in a Cell and the first Elimination Chamber",
                 sub="Badd Blood, October 5, 1997, over The Undertaker; Survivor Series, "
                     "November 17, 2002, over five men for the World Heavyweight Championship "
                     "— the only man to win both stipulations at their debut."),
            dict(name="First man to win the Royal Rumble from the No. 1 spot",
                 sub="1995, lasting the whole match; he won again in 1996, the first "
                     "back-to-back Rumble winner."),
            dict(name="Mr. WrestleMania",
                 sub="Eleven Wrestling Observer or PWI match-of-the-year-calibre WrestleMania "
                     "bouts is the shorthand claim; what is verifiable is the run itself — "
                     "the X ladder match, XII Iron Man, XIV, XIX, XX, 25 and XXVI all sit in "
                     "canonical best-of lists."),
            dict(name="Two Hall of Fame rings",
                 sub="2011 as an individual — inducted the same night his friend Triple H "
                     "presented — and 2019 with D-Generation X."),
            dict(name="Two retirements, one asterisk",
                 sub="Retired 1998-2002 with the broken back; retired again March 28, 2010 "
                     "after the Undertaker match; broke the second retirement exactly once, "
                     "at Crown Jewel on November 2, 2018."),
        ],
        footnote=("No career win-loss total is published; none is reliably sourced. The "
                  "five-star folklore around his catalogue is heavier than the verified "
                  "Observer record - ratings above are as commonly reported. No Spotify theme "
                  "block for Sexy Boy: no track URL was verified in this pass."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography",
             href="https://en.wikipedia.org/wiki/Shawn_Michaels"),
        dict(k="CBS Sports", v="Promotion to SVP of Talent Development Creative",
             href="https://www.cbssports.com/wwe/news/shawn-michaels-promoted-to-wwe-senior-vice-president-of-talent-development-creative"),
        dict(k="WWE.com", v="WWE LFG season two — coaching roster",
             href="https://www.wwe.com/article/ae-and-wwe-to-premiere-wwe-lfg-season-2-in-june"),
        dict(k="F4WOnline", v="On running NXT: 'a role I love' (September 2025)",
             href="https://www.f4wonline.com/news/nxt/shawn-michaels-running-wwe-nxt-its-a-role-i-love/"),
        dict(k="SEScoops", v="On NXT building stars in order to lose them",
             href="https://www.sescoops.com/article/shawn-michaels-nxt-is-the-only-brand-that-builds-stars-in-order-to-lose-them"),
        dict(k="WWE.com", v="Official profile",
             href="https://www.wwe.com/superstars/shawn-michaels"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="What is Shawn Michaels&rsquo; role in WWE in 2026?",
            a="He is WWE&rsquo;s Senior Vice President of Talent Development Creative &mdash; in "
              "practice, the man who runs NXT. He joined NXT as a coach in 2016, took over the "
              "brand&rsquo;s creative during Triple H&rsquo;s 2021 health absence, and was "
              "formally promoted on September 7, 2022. In 2025&ndash;26 he has also coached on "
              "A&amp;E&rsquo;s WWE LFG. He describes the job as the one that fits: &ldquo;none "
              "of it feels like work for me.&rdquo;",
            q_ld="What is Shawn Michaels' role in WWE in 2026?",
            a_ld="In 2026 Shawn Michaels is WWE's Senior Vice President of Talent Development "
                 "Creative, the executive who runs the NXT brand's creative direction. He joined "
                 "NXT as a coach in 2016, took over its creative in 2021, was formally promoted "
                 "on September 7, 2022, and also coaches on the A&E competition series WWE LFG."),
        dict(
            q="What was Shawn Michaels&rsquo; last match &mdash; WrestleMania XXVI or Crown Jewel?",
            a="Crown Jewel, November 2, 2018 &mdash; a D-Generation X tag with Triple H against "
              "The Undertaker and Kane in Riyadh, which DX won. His <b>retirement match</b> was "
              "WrestleMania XXVI on March 28, 2010, where he lost his career to The "
              "Undertaker&rsquo;s Streak, and that retirement held for eight years before the "
              "single Saudi one-off. He has not wrestled since 2018 and treats 2010 as the real "
              "ending; the record books have to list both.",
            q_ld="What was Shawn Michaels' last match?",
            a_ld="Shawn Michaels' last match was a tag team match at Crown Jewel on November 2, "
                 "2018, where he and Triple H, as D-Generation X, defeated The Undertaker and "
                 "Kane. His retirement match was at WrestleMania XXVI on March 28, 2010, a loss "
                 "to The Undertaker with his career on the line, and the 2018 bout was a single "
                 "one-off return eight years later."),
        dict(
            q="What really happened in the Montreal Screwjob?",
            a="At Survivor Series on November 9, 1997, Bret Hart &mdash; leaving for WCW and "
              "unwilling to lose the WWF Championship in Canada &mdash; was double-crossed: as "
              "Michaels held Hart in Hart&rsquo;s own Sharpshooter, Vince McMahon ordered the "
              "bell rung as if Hart had submitted. He had not, and no such finish was agreed. "
              "Michaels denied advance knowledge for years before admitting he was in on it. "
              "Hart and Michaels reconciled on the January 4, 2010 episode of Raw.",
            q_ld="What happened in the Montreal Screwjob between Shawn Michaels and Bret Hart?",
            a_ld="At Survivor Series in Montreal on November 9, 1997, Vince McMahon ordered the "
                 "bell rung while Shawn Michaels held Bret Hart in the Sharpshooter, awarding "
                 "Michaels the WWF Championship even though Hart had not submitted and had not "
                 "agreed to the finish. Hart was leaving for WCW and had declined to lose the "
                 "title in Canada. Michaels later admitted he knew about the plan in advance; "
                 "the two reconciled publicly in January 2010."),
        dict(
            q="How many world titles did Shawn Michaels win?",
            a="Four &mdash; three WWF Championships (WrestleMania XII in 1996, the 1997 Royal "
              "Rumble, and Survivor Series 1997 in Montreal) and one World Heavyweight "
              "Championship, won in the first Elimination Chamber at Survivor Series 2002. He "
              "never won a world title again across the final eight years of his career, which "
              "he has said was fine by him: the second career was built on matches, not belts.",
            q_ld="How many world championships did Shawn Michaels win?",
            a_ld="Shawn Michaels won four world championships: three WWF Championships, won at "
                 "WrestleMania XII on March 31, 1996, at the Royal Rumble on January 19, 1997, "
                 "and at Survivor Series on November 9, 1997, plus one World Heavyweight "
                 "Championship, won in the first Elimination Chamber match at Survivor Series "
                 "on November 17, 2002."),
        dict(
            q="Why did Shawn Michaels retire the first time, in 1998?",
            a="A casket-match bump at the 1998 Royal Rumble &mdash; his lower back struck the "
              "edge of the casket &mdash; herniated two discs and crushed a third. He wrestled "
              "one more match on it, dropping the WWF Championship to Steve Austin at "
              "WrestleMania XIV on March 29, 1998, then was gone for four and a half years. "
              "Spinal fusion surgery and, by his account, getting sober and finding faith made "
              "the 2002 comeback possible.",
            q_ld="Why did Shawn Michaels retire in 1998?",
            a_ld="Shawn Michaels retired in 1998 because of a severe back injury suffered in a "
                 "casket match at the Royal Rumble in January 1998, which herniated two discs "
                 "and crushed a third. He wrestled one final match at WrestleMania XIV on March "
                 "29, 1998, losing the WWF Championship to Steve Austin, then was out of the "
                 "ring for over four years before returning in August 2002."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Michael Shawn Hickenbottom"),
        dict(label="Born", value="July 22, 1965", sub="Chandler, Arizona &middot; raised in San Antonio &middot; age 61"),
        dict(label="Billed from", value="San Antonio, Texas"),
        dict(label="Height", value="6&#8242;1&#8243;", sub="185 cm"),
        dict(label="Weight", value="225 lb", sub="102 kg (billed)"),
        dict(label="Debut", value="October 16, 1984", sub="Mid-South &middot; trained by Jose Lothario"),
        dict(label="Retirement match", value="March 28, 2010",
             sub="vs. The Undertaker, WrestleMania XXVI &mdash; one Crown Jewel tag followed in 2018"),
        dict(label="Ring names", value="Shawn Michaels, throughout",
             sub="The Heartbreak Kid &middot; HBK &middot; The Showstopper &middot; Mr. WrestleMania"),
        dict(label="Signature", value="Sweet Chin Music &middot; flying elbow drop &middot; kip-up",
             sub="the superkick tune-up stomp is its own crowd cue"),
        dict(label="Hall of Fame", value="2011 &amp; 2019",
             sub="individual, then with D-Generation X"),
        dict(label="Now", value="SVP, Talent Development Creative",
             sub="runs NXT creative; WWE LFG coach"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1965-07-22",
    bornplace="Chandler, Arizona, United States",
    nationality="United States",
    height_cm=185,
    weight_kg=102,
    ld=dict(
        alternateName=["Michael Shawn Hickenbottom", "HBK", "The Heartbreak Kid",
                       "The Showstopper", "Mr. WrestleMania"],
        award=["WWF Championship (3 reigns)",
               "World Heavyweight Championship (1 reign)",
               "WWF Intercontinental Championship (3 reigns)",
               "WWF European Championship (1 reign)",
               "WWF/WWE tag team championships (5 reigns)",
               "Royal Rumble winner (1995, 1996)",
               "First WWF Grand Slam Champion (1997)",
               "WWE Hall of Fame (2011; 2019 with D-Generation X)"],
        knowsAbout=["Professional wrestling", "WWE", "NXT", "Talent development",
                    "D-Generation X", "WrestleMania"],
        description="Shawn Michaels, born Michael Shawn Hickenbottom, is a retired American "
                    "professional wrestler and WWE executive. He won four world championships, "
                    "two Royal Rumbles, and became the WWF's first Grand Slam Champion in 1997; "
                    "his matches at WrestleMania XII, 25 and XXVI are regularly ranked among the "
                    "best ever. Retired in-ring since 2010 apart from a single 2018 match, he "
                    "has run NXT's creative since 2021 as WWE's Senior Vice President of Talent "
                    "Development Creative.",
        sameAs=["https://en.wikipedia.org/wiki/Shawn_Michaels",
                "https://www.wwe.com/superstars/shawn-michaels"],
    ),
)
