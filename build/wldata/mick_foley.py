# -*- coding: utf-8 -*-
"""Mick Foley - dossier data.

Sources: web-verified August 31, 2026 (Wikipedia, POST Wrestling, PWMania, TPWW, SI).
Every match row carries a day-precision date. The Halftime Heat row uses the air date
(January 31, 1999, during the Super Bowl halftime); the first title win uses the
taping date (December 29, 1998) with the January 4, 1999 air date flagged in the
prose, because the air date is the one attached to the famous "that'll put butts in
seats" moment and both float around the sources.

Deliberate omissions:
  * No career win-loss total - no verified figure exists across WWF, WCW, ECW, TNA,
    Japan and the independents, and none is invented.
  * No social links - handles were not verified in this pass.
  * No Observer star ratings in the signature block - none were verified against
    archives, so the matches are listed without numbers rather than with guesses.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="L", date="1998-06-28", promo="WWE", landmark=True,
         event="King of the Ring — Pittsburgh", opponent="The Undertaker",
         stip="Hell in a Cell — thrown off the 16-foot cell through the announce table, then through the roof", title=""),
    dict(result="W", date="1998-12-29", promo="WWE", landmark=True,
         event="Raw — Worcester (aired January 4, 1999)", opponent="The Rock",
         stip="Singles — first WWF Championship, via Mandible Claw", title="WWF Championship"),
    dict(result="L", date="1999-01-31", promo="WWE", landmark=True,
         event="Royal Rumble — Anaheim", opponent="The Rock",
         stip="I Quit match — eleven unprotected chair shots", title="WWF Championship"),
    dict(result="W", date="1999-01-31", promo="WWE",
         event="Halftime Heat", opponent="The Rock",
         stip="Empty arena match, aired during the Super Bowl halftime — pinned with a forklift", title="WWF Championship"),
    dict(result="W", date="1999-08-22", promo="WWE", landmark=True, type="tag",
         event="SummerSlam — Minneapolis", opponent="Stone Cold Steve Austin & Triple H",
         stip="Triple threat — pinned Austin for a third WWF Championship", title="WWF Championship"),
    dict(result="L", date="2000-01-23", promo="WWE", landmark=True,
         event="Royal Rumble — Madison Square Garden", opponent="Triple H",
         stip="Street fight as Cactus Jack — thumbtacks and barbed wire", title="WWF Championship"),
    dict(result="L", date="2000-02-27", promo="WWE", landmark=True,
         event="No Way Out — Hartford", opponent="Triple H",
         stip="Hell in a Cell — career on the line; the retirement stipulation lands", title="WWF Championship"),
    dict(result="L", date="2000-04-02", promo="WWE", landmark=True, type="tag",
         event="WrestleMania 2000", opponent="Triple H, The Rock & Big Show",
         stip="Four-way main event — brought back one match after retiring; pinned by Triple H", title="WWF Championship"),
    dict(result="L", date="2004-04-18", promo="WWE", landmark=True,
         event="Backlash — Edmonton", opponent="Randy Orton",
         stip="Hardcore rules as Cactus Jack — thumbtacks; Orton retains", title="WWF Intercontinental Championship"),
    dict(result="L", date="2006-04-02", promo="WWE", landmark=True,
         event="WrestleMania 22 — Chicago", opponent="Edge",
         stip="Hardcore match — speared through a flaming table", title=""),
    dict(result="W", date="2006-06-11", promo="WWE", type="tag",
         event="ECW One Night Stand — New York", opponent="Terry Funk, Tommy Dreamer & Beulah",
         stip="Six-person hardcore tag, with Edge & Lita", title=""),
    dict(result="W", date="2009-04-19", promo="TNA", landmark=True,
         event="TNA Lockdown — Philadelphia", opponent="Sting",
         stip="Steel cage — a world title again at 43", title="TNA World Heavyweight Championship"),
    dict(result="L", date="2012-01-29", promo="WWE", type="tag",
         event="Royal Rumble — St. Louis", opponent="The 2012 Royal Rumble field",
         stip="30-man Royal Rumble match — his last match to date", title=""),
]

DATA = dict(
    slug="mick-foley",
    name="Mick Foley",
    realname="Michael Francis Foley",
    epithet="The Hardcore Legend",
    hook="Record & Titles",

    meta_desc=("Mick Foley - Cactus Jack, Mankind and Dude Love - is a three-time WWF Champion, "
               "the first Hardcore Champion, and the man thrown off the Hell in a Cell in 1998. "
               "Full record, titles, personas and career."),
    og_desc=("The Hardcore Legend: three WWF Championships across three personas, eight tag team "
             "reigns, the 1998 Hell in a Cell, and a number-one New York Times bestseller."),
    tw_desc="Three faces, three WWF Championships, one ear, and the most famous fall in wrestling.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1986",
    height_imp="6&#8242;2&#8243;",
    weight_lb="287",
    world_titles="4",
    vitals_tagline="Bang bang!",
    support_note="Merch &middot; Books &middot; Read",
    sp_items=[
        dict(ic="MF", title="RealMickFoley.com", sub="Official site · tour dates & books",
             tag="Visit", href="https://www.realmickfoley.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable as a legend across the 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="WWE", title="WWE Shop", sub="Mankind & Cactus Jack merch",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="RN", title="RAINN", sub="The charity Foley has raised money for over many years",
             tag="Give", charity=True, href="https://www.rainn.org/"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Cactus Jack &middot; Mankind &middot; Dude Love",
    hero_tag="Long Island, New York &middot; <em>CWA &middot; WCW &middot; ECW &middot; WWF &middot; TNA &middot; 1986&ndash;2012</em>",
    now_label="NOW",
    now_bold="Retired since 2012",
    now_tail=" &middot; turned 61 in June 2026, appeared for AEW at Double or Nothing in May, and says one last match is possible &ldquo;if the stars align&rdquo;",
    hstats=[
        dict(value="3", x=True, label="WWF Championships"),
        dict(value="8", x=True, label="WWF Tag Titles"),
        dict(value="16", x=False, label="Foot Fall, Twice"),
        dict(value="1", x=False, label="NYT No. 1 Bestseller"),
    ],
    ghost_link="From a Clarksburg armory in 1986 to the top of the Cell",
    vlabel="Est. 1986 &middot; Long Island, NY",
    mono="MF",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Mick Foley</b> is the only man to win the WWF Championship as three different people. "
        "Cactus Jack, Mankind and Dude Love were not costumes but full characters with separate "
        "histories, and all three entered the 1998 Royal Rumble as separate entrants. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">3</span>'
        '<span class="pull-cap">WWF Championship reigns &mdash; every one of them won as Mankind, every one against The Rock&rsquo;s corner of the card</span></span>'
        "He is a three-time WWF Champion, an eight-time WWF Tag Team Champion with five different "
        "partners, the first-ever WWF Hardcore Champion, a TNA World Heavyweight Champion at 43, "
        "and a 2013 WWE Hall of Famer. He is also, by common consent, the man who paid the most "
        "for all of it: an ear lost in Munich, a body held together by a replaced hip and rebuilt "
        "knees, and the two falls from the June 28, 1998 Hell in a Cell that remain the most "
        "replayed bumps in the industry&rsquo;s history.",

        "The famous line about his title win &mdash; &ldquo;January 4, 1999, the night that changed "
        "the Monday Night War&rdquo; &mdash; needs one correction: the match did not happen that "
        "night. Foley beat The Rock for the WWF Championship at a Raw <b>taping on December 29, "
        "1998</b> in Worcester, Massachusetts; the episode <b>aired January 4, 1999</b>, the night "
        "WCW commentator Tony Schiavone gave away the result on live television &mdash; &ldquo;that&rsquo;ll "
        "put butts in seats&rdquo; &mdash; and hundreds of thousands of viewers changed the channel to "
        "watch it happen. Both dates are real; they belong to different things. This page dates the "
        "match to the taping and the moment to the broadcast.",

        "The career before the fame is the reason the fame stuck. He debuted on June 23, 1986 in "
        "Clarksburg, West Virginia, trained by Dominic DeNucci, and spent a decade as Cactus Jack "
        "in the territories, WCW and ECW &mdash; losing his right ear in a March 16, 1994 match "
        "against Big Van Vader in Munich and finishing the match anyway. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">16</span>'
        '<span class="pull-cap">feet from the top of the Cell through the announce table on June 28, 1998 &mdash; and he climbed back up</span></span>'
        "WWF signed him in 1996 as Mankind, a scarred recluse who squealed and pulled his own hair, "
        "and he beat The Undertaker clean in his pay-per-view debut. Two years later the same "
        "opponent threw him off the roof of the Cell, and the second, unplanned fall &mdash; through "
        "a breaking panel to the mat, a chair landing on his face &mdash; is the one the wrestlers "
        "themselves still describe with disbelief. He retired in 2000, un-retired for stretches in "
        "2004&ndash;2012, and wrestled his final match in the 2012 Royal Rumble.",

        "The 2026 story is that the door is not quite closed. Foley lost roughly 100 pounds, had "
        "planned a final deathmatch for his 60th birthday in 2025 and scrapped it after dizzy spells "
        "traced to a training concussion, then made his first AEW appearance at Double or Nothing "
        "on May 24, 2026 in Queens, in a segment with MJF &mdash; the same MJF who had once pitched "
        "him six weeks of television for a farewell match. In June 2026 he told Ariel Helwani "
        "&ldquo;I think I have one last good match in me &mdash; all the stars would have to "
        "align,&rdquo; named Darby Allin his dream opponent, and set two conditions: thirty more "
        "pounds, and no trauma to the head. As of August 31, 2026 no match is announced, and this "
        "page treats him as what he is &mdash; retired since January 29, 2012, with an asterisk he "
        "put there himself.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE", "TNA"],
        promo_labels={"WWE": "WWF/WWE", "TNA": "TNA"},
        stats=[
            ("3&times;", "WWF Champion"),
            ("8&times;", "WWF Tag Champion"),
            ("1st", "Hardcore Champion"),
            ("2", "Falls from the Cell"),
            ("1&times;", "TNA World Champion"),
            ("2013", "Hall of Fame"),
        ],
        lead=("Thirteen documented bouts &mdash; the Cell, the three title changes, both retirements "
              "and the TNA championship. This is a curated ledger, not a career count; no career "
              "win&ndash;loss total exists across five promotions and none is invented here. Television "
              "tapings mean two dates need flagging: the first title win is dated to its December 29, "
              "1998 taping (aired January 4, 1999), and Halftime Heat is dated to its Super Bowl "
              "halftime broadcast. Filter by match type, tap any column header to sort, and turn "
              "spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the reputation rests on. No Wrestling Observer star ratings are "
                    "published here &mdash; none were verified against archives in this pass, and the "
                    "point of these four was never the snowflakes."),
    signature=[
        dict(rating="—", event="King of the Ring 1998", opponent="The Undertaker",
             stip="Hell in a Cell — the two falls"),
        dict(rating="—", event="Royal Rumble 2000", opponent="Triple H",
             stip="Street fight — the match Triple H credits with making him"),
        dict(rating="—", event="Raw, December 29, 1998 (aired January 4, 1999)", opponent="The Rock",
             stip="The title win that turned the Monday Night War"),
        dict(rating="—", event="WrestleMania 22", opponent="Edge",
             stip="Hardcore match — the flaming table, on Foley's own terms"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("3&times;", "WWF Championship"),
            ("8&times;", "WWF Tag Team"),
            ("1st", "Hardcore Champion"),
            ("4", "Promotions with gold"),
        ],
        lead=("Championships in the WWF, WCW, ECW and TNA. Exact dates for the eight tag reigns and "
              "the early territory titles were not all verified in this pass and are not invented; "
              "partners and years are listed as the sources state them."),
        rows=[
            dict(ic="W", name="WWF Championship", count="3",
                 sub="Def. The Rock at the December 29, 1998 Raw taping (aired January 4, 1999); "
                     "def. The Rock in the Halftime Heat empty arena match, aired January 31, 1999; "
                     "def. Austin and Triple H in the SummerSlam triple threat, August 22, 1999 &mdash; "
                     "all three as Mankind"),
            dict(ic="T", name="WWF Tag Team Championship", count="8",
                 sub="Five partners: Stone Cold Steve Austin (1997), Chainsaw Charlie at WrestleMania "
                     "XIV, Kane twice (1998), The Rock three times as the Rock &rsquo;n&rsquo; Sock "
                     "Connection (1999), and Al Snow (1999)"),
            dict(ic="H", name="WWF Hardcore Championship", count="1",
                 sub="The first champion &mdash; handed the belt in November 1998 as the division&rsquo;s "
                     "founding act"),
            dict(ic="N", name="TNA World Heavyweight Championship", count="1",
                 sub="Def. Sting in a steel cage at Lockdown, April 19, 2009 &mdash; a world champion "
                     "again at 43"),
            dict(ic="L", name="TNA Legends Championship", count="1",
                 sub="2009 &mdash; reign dates not verified in this pass"),
            dict(ic="E", name="ECW World Tag Team Championship", count="2",
                 sub="Both with Mikey Whipwreck, the rookie he was helping train"),
            dict(ic="C", name="WCW World Tag Team Championship", count="1",
                 sub="With Kevin Sullivan, won at Slamboree 1994 &mdash; the same year as the Vader "
                     "ear match"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Foley mostly worked alone &mdash; the units that mattered were a joke that got over, "
             "and a gimmick that became a census entry.",
        cards=[
            dict(era="WWF &middot; 1999&ndash;2000",
                 name="The Rock 'n' Sock Connection",
                 members="Mankind, The Rock",
                 desc="A comedy team of the company's most protected star and its least protected "
                      "one, and three tag title reigns anyway. Its centerpiece, the September 27, "
                      "1999 &ldquo;This is Your Life&rdquo; segment, drew one of the highest-rated "
                      "quarter hours in Raw history. The friendship was one-sided on screen and "
                      "the joke was always on Foley, which is why it worked."),
            dict(era="WWF &middot; 1998",
                 name="The Three Faces of Foley",
                 members="Cactus Jack, Mankind, Dude Love",
                 desc="Not a faction — one man booked as three. Dude Love was the teenage backyard "
                      "fantasy, Cactus Jack the scarred brawler, Mankind the broken recluse; all "
                      "three entered the 1998 Royal Rumble separately, and Vince McMahon cycled "
                      "through them on television as Foley kept failing to please him. No one else "
                      "has had a character split treated as continuity rather than a retcon."),
            dict(era="WWF/WWE &middot; 2000&ndash;2016",
                 name="The authority years",
                 members="Commissioner Foley, GM Foley",
                 desc="Commissioner from 2000, the referee and foil through the McMahon-Helmsley "
                      "era, SmackDown and Raw general manager in later spells (Raw GM 2016-17). "
                      "The flannel-and-clipboard version of Foley kept him on television for two "
                      "decades after the retirement match."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Three characters with separate move sets and separate wardrobes, plus the two "
             "post-ring identities that outlasted them all: <b>Cactus Jack</b> (1986&ndash;) &rarr; "
             "<b>Mankind</b> (1996&ndash;) &rarr; <b>Dude Love</b> (1997&ndash;) &rarr; author &rarr; "
             "one-last-match elder statesman.",
        cards=[
            dict(mono="CJ", era="Territories, WCW, ECW, WWF &middot; 1986&ndash;2012", name="Cactus Jack",
                 desc="The original: a wild-eyed brawler billed from Truth or Consequences, New "
                      "Mexico, built on the Cactus Elbow off the apron and a total disregard for "
                      "landing. This is the persona that lost the ear to Vader in Munich in 1994, "
                      "headlined ECW, and came back whenever the WWF needed a match to feel "
                      "dangerous — the Rumble 2000 street fight above all."),
            dict(mono="MK", era="WWF &middot; 1996&ndash;2000", name="Mankind",
                 desc="Debuted April 1, 1996 as a squealing recluse in a leather mask, then evolved "
                      "into the sweatpants-and-sock everyman who won all three WWF Championships. "
                      "Mr. Socko, the Mandible Claw, and the crowd's total emotional investment — "
                      "the Cell fall happened to Mankind, and so did the title win that answered it."),
            dict(mono="DL", era="WWF &middot; 1997&ndash;1998", name="Dude Love",
                 desc="The tie-dyed ladies' man Foley invented as a teenager and finally got to "
                      "play at 31. Tag champion with Steve Austin in 1997, corporate stooge for "
                      "Vince McMahon in 1998, and the deliberately worst wrestler of the three."),
            dict(mono="AU", era="1999&ndash;present", name="The author",
                 desc="Have a Nice Day! (1999), written longhand, hit number one on the New York "
                      "Times bestseller list and rewrote what a wrestling book could be. Foley Is "
                      "Good (2001) went to number one as well, followed by The Hardcore Diaries, "
                      "Countdown to Lockdown, novels and children's books."),
            dict(mono="61", era="2012&ndash;present", name="The elder statesman",
                 desc="Hall of Fame 2013, spoken-word tours, the Foley Is Pod podcast, a sincere "
                      "second life as a professional Santa Claus — and, in 2026, a 100-pounds-"
                      "lighter 61-year-old telling Ariel Helwani the last match might still "
                      "happen."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="A Clarksburg armory in 1986 to the top of the Cell, and a longer goodbye than anyone's.",
        rows=[
            dict(year="1986", title="Debut",
                 desc="June 23, 1986 in Clarksburg, West Virginia, trained by Dominic DeNucci — "
                      "having commuted from Long Island to Freedom, Pennsylvania for training."),
            dict(year="1994", title="Loses an ear in Munich",
                 desc="March 16, 1994, against Big Van Vader in WCW — the ear is torn off in the "
                      "ropes and Foley finishes the match. Wins WCW tag gold with Kevin Sullivan "
                      "at Slamboree the same year."),
            dict(year="1996", title="Mankind debuts in the WWF",
                 desc="April 1, 1996, and beats The Undertaker at King of the Ring two months "
                      "later — the start of wrestling's strangest main-event push."),
            dict(year="1998", title="The Cell",
                 desc="June 28, 1998: thrown 16 feet off the roof of the Cell through the announce "
                      "table, then chokeslammed through the roof itself. First Hardcore Champion by "
                      "November."),
            dict(year="1999", title="Three WWF Championships",
                 desc="Wins the title at the December 29, 1998 taping (aired January 4, 1999), in "
                      "the Halftime Heat empty arena match, and in the SummerSlam triple threat. "
                      "Have a Nice Day! hits number one on the New York Times list."),
            dict(year="2000", title="Retirement, twice",
                 desc="Loses the career-versus-title Cell match to Triple H at No Way Out on "
                      "February 27; comes back six weeks later for the WrestleMania 2000 four-way "
                      "at Linda McMahon's request, loses, and stays gone for four years."),
            dict(year="2004", title="Cactus Jack returns",
                 desc="The Backlash hardcore match with Randy Orton on April 18 — thumbtacks, and a "
                      "star-making loss he chose to take."),
            dict(year="2006", title="The Edge program",
                 desc="Speared through a flaming table at WrestleMania 22 on April 2; wins the "
                      "ECW One Night Stand six-person tag with Edge and Lita on June 11."),
            dict(year="2009", title="TNA World Champion at 43",
                 desc="Beats Sting in the Lockdown cage on April 19, 2009."),
            dict(year="2012", title="The last match",
                 desc="The Royal Rumble match, January 29, 2012. Hall of Fame the following year."),
            dict(year="2026", title="The asterisk",
                 desc="AEW appearance at Double or Nothing on May 24 with MJF; tells Ariel Helwani "
                      "in June that one last good match is possible if the stars align, names Darby "
                      "Allin the dream opponent, and keeps touring and podcasting in the meantime."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="The Undertaker",
                 desc="The 1996 series made Mankind a main-eventer — he beat The Undertaker clean "
                      "at King of the Ring 1996 in his pay-per-view debut — and the 1998 Hell in a "
                      "Cell made both men permanent. Two falls, one match, and the single most "
                      "replayed piece of footage the company owns."),
            dict(name="The Rock",
                 desc="The championship trilogy of early 1999 — the taped title win that turned the "
                      "ratings war, the I Quit match with its eleven chair shots, the empty-arena "
                      "Halftime Heat — and then, in the same calendar year, the Rock 'n' Sock "
                      "Connection. No feud has ever pivoted from that much violence to that much "
                      "comedy that fast."),
            dict(name="Triple H",
                 desc="The Royal Rumble 2000 street fight is the match Triple H has repeatedly "
                      "called the one that made him, and the No Way Out Cell rematch a month later "
                      "ended Foley's full-time career on the stipulation he asked for. Foley's "
                      "job in both was to lose in a way that transferred everything he had."),
            dict(name="Randy Orton",
                 desc="Backlash 2004: the semi-retired legend versus the Legend Killer, hardcore "
                      "rules, thumbtacks. Foley lost on purpose and on principle — he has said the "
                      "match existed to make Orton, and it did."),
            dict(name="Edge",
                 desc="WrestleMania 22, hardcore rules, and the flaming-table spear that Foley "
                      "engineered to give himself the WrestleMania moment he felt he never had. "
                      "Edge has credited the match with legitimising him as a main-eventer; the "
                      "ECW One Night Stand six-person that June put them on the same side."),
            dict(name="Vader",
                 desc="The WCW series that established what a Cactus Jack match cost: the "
                      "powerbomb on concrete that gave him a concussion in 1993, and the Munich "
                      "match of March 16, 1994 that took his right ear."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Books",
        lead="The rare wrestler whose second career is genuinely literary.",
        rows=[
            dict(when="1999", title="Have a Nice Day! A Tale of Blood and Sweatsocks", kind="Book",
                 desc="Written longhand, number one on the New York Times bestseller list — the "
                      "book that created the wrestler-memoir genre."),
            dict(when="2001&ndash;2010", title="Foley Is Good, The Hardcore Diaries, Countdown to Lockdown", kind="Books",
                 desc="Foley Is Good also reached number one. Later shelves include novels "
                      "(Tietam Brown) and children's Christmas books."),
            dict(when="2022&ndash;", title="Foley Is Pod", kind="Podcast",
                 desc="Weekly memoir-by-installments podcast, alongside a continuing live "
                      "spoken-word tour."),
            dict(when="2014", title="I Am Santa Claus", kind="Documentary",
                 desc="Foley, a lifelong Christmas obsessive, features in and executive-produced "
                      "the documentary about professional Santas."),
            dict(when="2013", title="WWE Hall of Fame, Class of 2013", kind="Honor",
                 desc="Inducted by Terry Funk. Playable as a legend across WWE 2K entries."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records and the receipts — stated the way the sources state them.",
        stats=[
            ("3", "WWF Championships"),
            ("16", "Feet, Cell to table"),
            ("1st", "Hardcore Champion"),
        ],
        rows=[
            dict(name="Three WWF Championships as three-persona headliner",
                 sub="All three won as Mankind in 1998-99, but the three-character history is the "
                     "feat: no other WWF/WWE Champion has had two other full personas in the same "
                     "company's canon."),
            dict(name="The Hell in a Cell falls, June 28, 1998",
                 sub="Thrown 16 feet from the roof through the announce table; then, unplanned, "
                     "chokeslammed through the cell roof to the mat. He finished the match."),
            dict(name="First WWF Hardcore Champion",
                 sub="Awarded the belt in November 1998; the division was effectively built around "
                     "his tolerance."),
            dict(name="Eight WWF Tag Team Championships with five partners",
                 sub="Austin, Chainsaw Charlie (Terry Funk), Kane, The Rock and Al Snow — the Rock "
                     "'n' Sock Connection accounts for three."),
            dict(name="The ratings turn of January 4, 1999",
                 sub="Tony Schiavone mocked the taped title win on Nitro — &ldquo;that'll put butts "
                     "in seats&rdquo; — and viewers switched to Raw in the hundreds of thousands to "
                     "watch Foley win. Routinely cited as the Monday Night War's hinge moment."),
            dict(name="This is Your Life, September 27, 1999",
                 sub="The Rock 'n' Sock segment drew one of the highest-rated quarter hours in Raw "
                     "history."),
            dict(name="TNA World Heavyweight Champion at 43",
                 sub="Beat Sting in the Lockdown cage on April 19, 2009."),
            dict(name="Number one New York Times bestseller, twice",
                 sub="Have a Nice Day! (1999) and Foley Is Good (2001), both written without a "
                     "ghostwriter."),
            dict(name="An ear left in Munich",
                 sub="March 16, 1994, against Vader — torn off in the ropes; the match continued."),
            dict(name="The 2026 one-last-match file",
                 sub="Lost roughly 100 pounds; scrapped a planned 60th-birthday deathmatch in 2025 "
                     "after a training concussion; appeared at AEW Double or Nothing on May 24, "
                     "2026; told Ariel Helwani in June 2026 the stars would all have to align, and "
                     "named Darby Allin the dream opponent. Nothing is announced."),
        ],
        footnote=("Two things are deliberately absent. No career win-loss record — none exists "
                  "across the WWF, WCW, ECW, TNA, Japan and the independents, and the honest "
                  "answer is that Foley lost most of the matches that made him famous. And no "
                  "Observer star ratings — none were verified in this pass, and his case never "
                  "rested on them."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Mick_Foley"),
        dict(k="POST Wrestling", v="&ldquo;One last good match&rdquo; &mdash; the Helwani interview, June 2026",
             href="https://www.postwrestling.com/2026/06/02/mick-foley-i-think-i-have-one-last-good-match-in-me-all-the-stars-would-have-to-align/"),
        dict(k="PWMania", v="Health update at 60 &mdash; Cauliflower Alley Club, September 2025",
             href="https://www.pwmania.com/mick-foley-provides-positive-health-update-at-age-60"),
        dict(k="TPWW", v="AEW match update and the Darby Allin answer, June 2026",
             href="https://www.tpww.net/2026/06/mick-foley-provides-update-on-him-potentially-wrestling-a-match-in-aew-his-choice-of-opponent/"),
        dict(k="Sports Illustrated", v="The scrapped MJF farewell match",
             href="https://www.si.com/fannation/wrestling/wrestling-news/mick-foley-reveals-almost-match-against-mjf"),
        dict(k="Official site", v="RealMickFoley.com", href="https://www.realmickfoley.com/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Did Mick Foley really fall off the Hell in a Cell?",
            a="Twice, in the same match &mdash; June 28, 1998, against The Undertaker at King of the "
              "Ring. The first fall, off the roof through the Spanish announce table, was planned; "
              "the figure attached to it in the sources is <b>16 feet</b>, not the twenty-plus that "
              "circulates. The second was not planned: the cell panel broke under a chokeslam and he "
              "fell through to the mat with the chair landing on his face. He finished the match, "
              "which is the part every retelling agrees on.",
            q_ld="Did Mick Foley really fall off the Hell in a Cell?",
            a_ld="Yes, twice in the same match, on June 28, 1998 against The Undertaker at WWF King "
                 "of the Ring. The first fall was planned: he was thrown 16 feet from the roof of "
                 "the cell through the Spanish announce table. The second was not planned: the cell "
                 "panel broke under a chokeslam and Foley fell through the roof to the mat. He "
                 "finished the match."),
        dict(
            q="How many world titles did Mick Foley win?",
            a="Four: three WWF Championships, all won as Mankind &mdash; the taped December 29, 1998 "
              "Raw win over The Rock (aired January 4, 1999), the Halftime Heat empty arena rematch, "
              "and the SummerSlam 1999 triple threat where he pinned Steve Austin &mdash; plus the "
              "TNA World Heavyweight Championship, won from Sting in a cage at Lockdown on April 19, "
              "2009, when he was 43.",
            q_ld="How many world championships did Mick Foley win?",
            a_ld="Four. Mick Foley won the WWF Championship three times as Mankind: at a Raw taping "
                 "on December 29, 1998 that aired January 4, 1999, in the Halftime Heat empty arena "
                 "match against The Rock, and in the SummerSlam 1999 triple threat. He also won the "
                 "TNA World Heavyweight Championship from Sting at Lockdown on April 19, 2009."),
        dict(
            q="Is Mick Foley retired, and will he wrestle again?",
            a="His last match was the Royal Rumble on January 29, 2012, and he is retired as of "
              "August 31, 2026 &mdash; but he has reopened the question himself. After losing "
              "roughly 100 pounds he told Ariel Helwani in June 2026, &ldquo;I think I have one last "
              "good match in me. All the stars would have to align,&rdquo; named <b>Darby Allin</b> "
              "his dream opponent, and appeared for AEW at Double or Nothing on May 24, 2026 in a "
              "segment with MJF. A planned 60th-birthday deathmatch in 2025 was scrapped after a "
              "training concussion, and any future match, he says, must avoid trauma to the head. "
              "Nothing is announced.",
            q_ld="Is Mick Foley retired, and will he wrestle again?",
            a_ld="Mick Foley's last match was the Royal Rumble on January 29, 2012, and he remains "
                 "retired as of August 31, 2026. He has said a return is possible: after losing "
                 "roughly 100 pounds, he told Ariel Helwani in June 2026 that he has one last good "
                 "match in him if the stars align, named Darby Allin his dream opponent, and "
                 "appeared for AEW at Double or Nothing on May 24, 2026. A planned deathmatch for "
                 "his 60th birthday in 2025 was cancelled after a concussion suffered in training. "
                 "No match is announced."),
        dict(
            q="What are the three faces of Foley?",
            a="<b>Cactus Jack</b> (1986 onward), the brawler from Truth or Consequences, New Mexico; "
              "<b>Mankind</b> (from April 1, 1996), the masked recluse who became the sweatpants "
              "everyman and won all three WWF titles; and <b>Dude Love</b> (from 1997), the tie-dyed "
              "character Foley invented as a teenager. All three entered the 1998 Royal Rumble as "
              "separate entrants &mdash; the only time one wrestler has taken three spots in the "
              "match as three people.",
            q_ld="What are the three faces of Mick Foley?",
            a_ld="Mick Foley wrestled as three distinct characters: Cactus Jack, a brawler billed "
                 "from Truth or Consequences, New Mexico; Mankind, the masked recluse who debuted "
                 "on April 1, 1996 and won all three of his WWF Championships; and Dude Love, a "
                 "tie-dyed character he invented as a teenager. All three entered the 1998 Royal "
                 "Rumble as separate entrants."),
        dict(
            q="Did Foley really lose an ear in a match?",
            a="Yes. On March 16, 1994, in a WCW match against Big Van Vader in Munich, his right ear "
              "was torn off in the ring ropes. He finished the match. The ear could not be "
              "reattached, and the story &mdash; told at length in Have a Nice Day! &mdash; is the "
              "shorthand for what the pre-WWF decade cost him.",
            q_ld="Did Mick Foley really lose an ear in a match?",
            a_ld="Yes. On March 16, 1994, during a WCW match against Big Van Vader in Munich, "
                 "Germany, Mick Foley's right ear was torn off in the ring ropes. He finished the "
                 "match, and the ear could not be reattached."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Michael Francis Foley"),
        dict(label="Born", value="June 7, 1965",
             sub="Bloomington, Indiana; raised in East Setauket, Long Island &middot; age 61"),
        dict(label="Billed from", value="Long Island, NY / Truth or Consequences, NM",
             sub="the latter as Cactus Jack"),
        dict(label="Height", value="6&#8242;2&#8243;", sub="188 cm"),
        dict(label="Weight", value="287 lb", sub="130 kg billed in his prime &mdash; roughly 100 lb lighter in 2026"),
        dict(label="Debut", value="June 23, 1986", sub="Clarksburg, West Virginia"),
        dict(label="Trained by", value="Dominic DeNucci"),
        dict(label="Ring names", value="Cactus Jack &rarr; Mankind &rarr; Dude Love &rarr; Mick Foley",
             sub="all three characters entered the 1998 Royal Rumble separately"),
        dict(label="Signature", value="Mandible Claw / Mr. Socko &middot; Double-arm DDT &middot; "
                                      "Cactus Elbow"),
        dict(label="Last match", value="January 29, 2012", sub="Royal Rumble match"),
        dict(label="Hall of Fame", value="2013", sub="inducted by Terry Funk"),
        dict(label="Also known as", value="The Hardcore Legend &middot; Mrs. Foley&rsquo;s Baby Boy"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1965-06-07",
    bornplace="Bloomington, Indiana",
    nationality="United States",
    height_cm=188,
    weight_kg=130,
    ld=dict(
        alternateName=["Michael Francis Foley", "Cactus Jack", "Mankind", "Dude Love",
                       "The Hardcore Legend"],
        award=["WWF Championship (3 reigns)",
               "WWF Tag Team Championship (8 reigns)",
               "WWF Hardcore Championship (first champion)",
               "TNA World Heavyweight Championship (1 reign)",
               "TNA Legends Championship (1 reign)",
               "ECW World Tag Team Championship (2 reigns)",
               "WCW World Tag Team Championship (1 reign)",
               "WWE Hall of Fame (2013)"],
        knowsAbout=["Professional wrestling", "Hardcore wrestling", "WWE", "ECW", "WCW", "TNA",
                    "Memoir writing"],
        description="Mick Foley, born Michael Francis Foley, is a retired American professional "
                    "wrestler and author who competed as Cactus Jack, Mankind and Dude Love. He won "
                    "the WWF Championship three times, held eight WWF Tag Team Championships, was "
                    "the first WWF Hardcore Champion, won the TNA World Heavyweight Championship in "
                    "2009, and survived the famous 1998 Hell in a Cell match against The Undertaker. "
                    "His autobiography Have a Nice Day! reached number one on the New York Times "
                    "bestseller list. He was inducted into the WWE Hall of Fame in 2013 and last "
                    "wrestled in the 2012 Royal Rumble.",
        sameAs=["https://en.wikipedia.org/wiki/Mick_Foley",
                "https://www.realmickfoley.com/"],
    ),
)
