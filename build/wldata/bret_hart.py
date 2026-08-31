# -*- coding: utf-8 -*-
"""Bret Hart - dossier data.

Sources: web-verified August 31, 2026 - Wikipedia (Bret Hart; WrestleMania 13; List of WCW
United States Heavyweight Champions; WWE Hall of Fame (2025)), Slam Wrestling (August 2025
interview on the SummerSlam snub), PWMania (October 2025 appearance cancellations),
brethart.com and TPWW (August 2026 Maple Leaf Pro interview segment). Record-row dates are
day-precision and verified.

Deliberate omissions:
  * No career win-loss total - none is reliably published, so none is invented.
  * No theme entry - no Spotify track URL was verified in this pass, so omitted.
  * The exact endpoints of the two WCW World Heavyweight Championship reigns are murky in
    every source (vacated and reawarded around the December 1999 Goldberg matches, then
    stripped in January 2000); this page states the window rather than fake precision.
  * A reported skin-cancer diagnosis circulated in recent years but was not verified with
    a dated source in this pass and is not published here. The 2016 prostate cancer and
    2002 stroke are well documented and are.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="1991-08-26", promo="WWE", landmark=True,
         event="SummerSlam — Madison Square Garden", opponent="Mr. Perfect",
         stip="Singles — first singles title, submission win", title="WWF Intercontinental Championship"),
    dict(result="W", date="1992-04-05", promo="WWE",
         event="WrestleMania VIII — Indianapolis", opponent="Roddy Piper",
         stip="Singles — Piper's only clean pinfall loss in the WWF", title="WWF Intercontinental Championship"),
    dict(result="W", date="1992-10-12", promo="WWE", landmark=True,
         event="House show — Saskatoon", opponent="Ric Flair",
         stip="Singles — first WWF Championship, untelevised, in Saskatchewan", title="WWF Championship"),
    dict(result="L", date="1994-03-20", promo="WWE", landmark=True,
         event="WrestleMania X — Madison Square Garden", opponent="Owen Hart",
         stip="Singles — the opener; clean loss to his brother", title=""),
    dict(result="W", date="1994-03-20", promo="WWE",
         event="WrestleMania X — Madison Square Garden", opponent="Yokozuna",
         stip="Singles — second WWF title the same night", title="WWF Championship"),
    dict(result="L", date="1994-11-23", promo="WWE",
         event="Survivor Series — San Antonio", opponent="Bob Backlund",
         stip="Towel match — Owen tricks their mother into throwing it in", title="WWF Championship"),
    dict(result="W", date="1995-11-19", promo="WWE",
         event="Survivor Series — Landover", opponent="Diesel",
         stip="No disqualification — third WWF title", title="WWF Championship"),
    dict(result="L", date="1996-03-31", promo="WWE", landmark=True,
         event="WrestleMania XII — Anaheim", opponent="Shawn Michaels", opponent_html=True,
         stip="60-minute Iron Man match, lost in overtime", title="WWF Championship"),
    dict(result="W", date="1996-11-17", promo="WWE",
         event="Survivor Series — Madison Square Garden", opponent="Stone Cold Steve Austin", opponent_html=True,
         stip="Singles — the comeback match after seven months away", title=""),
    dict(result="W", date="1997-03-23", promo="WWE", landmark=True,
         event="WrestleMania 13 — Rosemont", opponent="Stone Cold Steve Austin", opponent_html=True,
         stip="Submission match — Austin passes out; the double turn", title=""),
    dict(result="W", date="1997-08-03", promo="WWE",
         event="SummerSlam — East Rutherford", opponent="The Undertaker", opponent_html=True,
         stip="Singles, Shawn Michaels as referee — fifth WWF title", title="WWF Championship"),
    dict(result="L", date="1997-11-09", promo="WWE", landmark=True,
         event="Survivor Series — Montreal", opponent="Shawn Michaels", opponent_html=True,
         stip="The Montreal Screwjob — bell rung on a finish he never agreed to",
         title="WWF Championship"),
    dict(result="W", date="1999-11-21", promo="WCW", landmark=True,
         event="WCW Mayhem — Toronto", opponent="Chris Benoit",
         stip="Tournament final — first WCW World Championship", title="WCW World Heavyweight Championship"),
    dict(result="W", date="1999-12-19", promo="WCW",
         event="Starrcade — Washington, D.C.", opponent="Goldberg",
         stip="Singles — the mule kick that caused the concussion that ended the career",
         title="WCW World Heavyweight Championship"),
    dict(result="W", date="2010-03-28", promo="WWE", landmark=True,
         event="WrestleMania XXVI — Glendale", opponent="Vince McMahon",
         stip="No holds barred — twelve years of Montreal settled with a chair", title=""),
]

for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Shawn Michaels": "shawn-michaels", "The Undertaker": "the-undertaker",
                 "Stone Cold Steve Austin": "stone-cold-steve-austin"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="bret-hart",
    name="Bret Hart",
    realname="Bret Sergeant Hart",
    epithet="The Hitman",
    hook="Record & Titles",

    meta_desc=("Bret Hart won five WWF Championships and two WCW World Championships, lost the "
               "Montreal Screwjob for real, and had his WrestleMania 13 classic inducted into the "
               "Hall of Fame in 2025. Full record, titles and the 2026 picture."),
    og_desc=("The Hitman: five WWF titles, two WCW titles, the Screwjob, the double turn, and a "
             "2025 Hall of Fame induction for a match he lost nothing by winning."),
    tw_desc="The best there is, was, ever will be: 5 WWF titles, 2 WCW titles, one Montreal.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1978",
    height_imp="6&#8242;0&#8243;",
    weight_lb="235",
    world_titles="7",
    vitals_tagline="The best there is, was, and ever will be",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="BH", title="BretHart.com", sub="Official site, news and appearances",
             tag="Visit", href="https://brethart.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable legend in the 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="WS", title="WWE Shop", sub="Official Hitman merch · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/bret-hart"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Hitman &middot; The Excellence of Execution &middot; the pink and black attack",
    hero_tag="Calgary, Alberta &middot; <em>Stampede &middot; WWF &middot; WCW &middot; 1978&ndash;2000</em>",
    now_label="NOW",
    now_bold="Retired in Calgary, at 69",
    now_tail=" &middot; still giving prickly, precise interviews &mdash; a 2026 Maple Leaf Pro "
             "sit-down, a 2025 Hall of Fame stage shared with Steve Austin, and no forgiveness "
             "spent on anyone he thinks earned none",
    hstats=[
        dict(value="5",    x=True,  label="WWF Titles"),
        dict(value="2",    x=True,  label="WCW World Titles"),
        dict(value="2",    x=True,  label="King of the Ring"),
        dict(value="1994", x=False, label="Rumble Co-Winner"),
    ],
    ghost_link="From the Hart family Dungeon to the sharpest technical resume of the 1990s",
    vlabel="Est. 1978 &middot; Calgary, Alberta",
    mono="BH",

    # ---------------------------------------------------------------- 01 overview
    correction=2,
    overview=[
        "<b>Bret Hart</b> billed himself the best there is, the best there was, and the best "
        "there ever will be, and built the closest thing wrestling has to a factual case for a "
        "boast: five WWF Championships, two WCW World Championships, two Intercontinental "
        "reigns, two King of the Ring wins (the 1991 tournament and the first pay-per-view "
        "edition in 1993), and a 1994 Royal Rumble co-win with Lex Luger. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">5</span>'
        '<span class="pull-cap">WWF Championship reigns between October 1992 and November 1997 &mdash; the company&rsquo;s 1990s axis</span></span>'
        "The eighth of Stu Hart&rsquo;s twelve children, he came out of the family&rsquo;s "
        "Calgary Dungeon and carried the WWF through its leanest commercial years on technical "
        "credibility: the first title won in an untelevised match in Saskatoon against Ric "
        "Flair on October 12, 1992, the last taken from him in Montreal by means outside the "
        "match entirely.",

        "Montreal is the fact everyone knows, and it is a fact, not an angle: at Survivor "
        "Series on November 9, 1997, leaving for WCW and having declined to drop the title in "
        "Canada, he was double-crossed when Vince McMahon had the bell rung while Shawn "
        "Michaels held him in his own Sharpshooter. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">1997</span>'
        '<span class="pull-cap">the Screwjob &mdash; the last time a major world title changed hands off-script</span></span>'
        "But the better summary of him is the year that preceded it: at WrestleMania 13 on "
        "March 23, 1997 he beat Steve Austin in a submission match in which Austin passed out "
        "rather than quit, executing wrestling&rsquo;s definitive double turn &mdash; Hart "
        "walked in the hero and out the heel, and made his opponent a megastar by beating him. "
        "In April 2025 WWE inducted that match into the Hall of Fame as the first entry in its "
        "Immortal Moment category, and Hart and Austin accepted together in Las Vegas &mdash; "
        "Hart&rsquo;s third induction, after 2006 individually and 2019 with the Hart "
        "Foundation.",

        "The end of the career is usually told wrong by one detail. The Goldberg mule kick "
        "that concussed him came at Starrcade on December 19, 1999 &mdash; a match Hart "
        "<b>won</b>, taking his second WCW World Championship reign into December &mdash; but "
        "it did not stop him that night. He kept wrestling into January 2000 while the "
        "post-concussion symptoms worsened, was stripped of the title that month, and did not "
        "formally retire until October 26, 2000. The concussion, and the stroke he suffered "
        "in a 2002 bicycle accident, define the aftermath; he has spent two decades saying, "
        "with characteristic lack of diplomacy, that Goldberg&rsquo;s carelessness took years "
        "of his career. Goldberg has apologised publicly; Hart has accepted the apology "
        "without ever quite accepting the kick.",

        "At 69 he lives in Calgary, recovered from the 2016 prostate cancer surgery he "
        "announced publicly, and remains wrestling&rsquo;s most quotable unfiltered elder. The "
        "2025&ndash;26 file: the Hall of Fame stage with Austin on April 18, 2025; an August "
        "2025 Slam Wrestling interview in which he noted WWE invited him to SummerSlam and "
        "then failed to seat him (&ldquo;I don&rsquo;t think they really fully appreciate "
        "me&rdquo;); a run of cancelled US signings in late 2025 that he attributed to "
        "commitments at home; and a sit-down interview aired on Maple Leaf Pro&rsquo;s TSN2 "
        "show in August 2026, praising young Canadian talent. He does not do nostalgia "
        "matches, does not soften old grievances, and shows no sign of starting either.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE", "WCW"],
        promo_labels={"WWE": "WWF/WWE", "WCW": "WCW"},
        stats=[
            ("5&times;", "WWF Championship"),
            ("2&times;", "WCW World Heavyweight"),
            ("2&times;", "Intercontinental"),
            ("2&times;", "King of the Ring"),
            ("2&times;", "WWF Tag titles"),
            ("3&times;", "Hall of Fame"),
        ],
        lead=("Fifteen documented bouts &mdash; all five WWF title changes in or out, both "
              "brothers' WrestleMania X matches, Montreal, the WCW crowning and the Starrcade "
              "match that ended everything in slow motion. A curated ledger, not a career "
              "count; no career win&ndash;loss total is published because none is reliably "
              "sourced. Filter by promotion or match type, tap any column header to sort, and "
              "turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the reputation rests on. WrestleMania 13 carries the official "
                    "canonisation now; the ratings shown are Wrestling Observer figures as "
                    "commonly reported rather than re-verified against archives."),
    signature=[
        dict(rating="5.0", event="WrestleMania 13 — Rosemont", opponent="Stone Cold Steve Austin",
             stip="Submission match — the double turn; Hall of Fame Immortal Moment, 2025"),
        dict(rating="5.0", event="In Your House: Canadian Stampede — Calgary", opponent="Ten-man tag, Hart Foundation vs. Austin's team",
             stip="The hottest crowd of the decade, in his hometown"),
        dict(rating="4.75", event="SummerSlam 1992 — Wembley", opponent="British Bulldog",
             stip="Intercontinental Championship — 80,000 for a brother-in-law feud"),
        dict(rating="4.5", event="WrestleMania X — Madison Square Garden", opponent="Owen Hart",
             stip="The opener — a clean loss that made his brother"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("5&times;", "WWF Championship"),
            ("2&times;", "WCW World Heavyweight"),
            ("4&times;", "WCW United States"),
            ("4&times;", "Tag reigns, both companies"),
        ],
        lead=("Seven world championships across the two companies, and a triple crown in each "
              "&mdash; the first man to manage both. The WCW World reign endpoints are the one "
              "genuinely messy patch in his title history and are stated as a window rather "
              "than fake dates."),
        rows=[
            dict(ic="W", name="WWF Championship", count="5",
                 sub="October 12, 1992, def. Ric Flair in Saskatoon, untelevised &middot; "
                     "WrestleMania X, def. Yokozuna &middot; Survivor Series 1995, def. Diesel "
                     "&middot; SummerSlam 1997, def. The Undertaker with Shawn Michaels as "
                     "referee &middot; final reign ended by the Screwjob, November 9, 1997"),
            dict(ic="C", name="WCW World Heavyweight Championship", count="2",
                 sub="Won the tournament final over Chris Benoit at Mayhem in Toronto, November "
                     "21, 1999; the reigns were vacated and reawarded around the December "
                     "Goldberg matches and stripped in January 2000 when the concussion was "
                     "diagnosed &mdash; sources disagree on exact endpoints, so none are "
                     "published here"),
            dict(ic="I", name="WWF Intercontinental Championship", count="2",
                 sub="Def. Mr. Perfect at SummerSlam, August 26, 1991; def. Roddy Piper at "
                     "WrestleMania VIII, April 5, 1992 &mdash; the reigns that made the belt a "
                     "main-event incubator"),
            dict(ic="U", name="WCW United States Heavyweight Championship", count="4",
                 sub="Four reigns across 1998&ndash;99, per the championship's own title "
                     "history &mdash; individual endpoints not re-verified in this pass"),
            dict(ic="T", name="Tag team championships", count="4",
                 sub="Two WWF Tag reigns with Jim Neidhart as the Hart Foundation (1987, 1990) "
                     "and a WCW Tag reign with Goldberg (December 1999); a fourth, with "
                     "different accounting, appears in some WCW listings and is flagged rather "
                     "than asserted"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="One family, twice over — the tag team that named it and the stable that "
             "weaponised it.",
        cards=[
            dict(era="WWF &middot; 1985&ndash;1991",
                 name="The Hart Foundation",
                 members="Bret Hart &amp; Jim Neidhart, with Jimmy Hart managing",
                 desc="The pink-and-black tag team — Bret the technician, Neidhart the anvil. "
                      "Two WWF Tag Team Championship reigns (1987, 1990), and the platform the "
                      "singles career launched from. Inducted into the Hall of Fame as a team "
                      "in 2019."),
            dict(era="WWF &middot; 1997",
                 name="The Hart Foundation, the stable",
                 members="Bret, Owen Hart, British Bulldog, Jim Neidhart, Brian Pillman",
                 desc="The great heel-in-America, hero-in-Canada experiment: an anti-American "
                      "family unit that turned every border crossing into a moral inversion. "
                      "Its peak, the Canadian Stampede ten-man tag in Calgary on July 6, 1997, "
                      "had maybe the loudest sustained crowd of the decade. Dissolved by "
                      "Montreal and by Owen's death two years later."),
            dict(era="WCW &middot; 1999",
                 name="With Goldberg, briefly",
                 members="Bret Hart &amp; Goldberg",
                 desc="Tag champions together on December 7, 1999 — twelve days before "
                      "Goldberg's thrust kick at Starrcade concussed him and started the end "
                      "of his career. The pairing is remembered entirely for its last two "
                      "minutes."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="No gimmick changes, ever &mdash; the same character for 22 years, adjusted only "
             "in framing: <b>the tag technician</b> &rarr; <b>the Hitman</b> &rarr; <b>the "
             "anti-American patriot</b> &rarr; <b>the wronged man</b>.",
        cards=[
            dict(mono="ST", era="Stampede/WWF &middot; 1978&ndash;1991", name="The technician",
                 desc="Dungeon-trained, second-generation, allergic to flash — the reputation "
                      "was built entirely on execution, which became the nickname."),
            dict(mono="HM", era="WWF &middot; 1991&ndash;1996", name="The Hitman",
                 desc="Pink and black, mirrored shades handed to a kid at ringside every "
                      "night, and the era's most trusted in-ring product. WWF Champion five "
                      "times over while the company shrank around him."),
            dict(mono="HF", era="WWF &middot; 1997", name="The border heel",
                 desc="The 1997 masterstroke: the same honest character, reframed — a villain "
                      "in American buildings and a folk hero everywhere else, often within "
                      "the same week. The most sophisticated heel run of its decade, cut off "
                      "by Montreal at its peak."),
            dict(mono="WM", era="WCW/after &middot; 1997&ndash;present", name="The wronged man",
                 desc="WCW never figured out what it had signed; the concussion ended the "
                      "in-ring story in 2000, and the decades since have been an extended "
                      "cross-examination of everyone involved — in his autobiography, in "
                      "documentaries, and in interviews that remain quotably unforgiving."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="The Dungeon to Montreal, and the long deposition after.",
        rows=[
            dict(year="1978", title="Debut in Stampede",
                 desc="Breaks in for his father Stu's Calgary promotion after amateur "
                      "credentials at Mount Royal College; WWF absorbs Stampede in 1984."),
            dict(year="1987", title="Hart Foundation tag champions",
                 desc="First WWF Tag Team Championship with Jim Neidhart; a second reign "
                      "follows in 1990."),
            dict(year="1991", title="Intercontinental Champion, King of the Ring",
                 desc="Beats Mr. Perfect at SummerSlam on August 26 for the IC title and wins "
                      "the 1991 King of the Ring tournament."),
            dict(year="1992", title="WWF Champion in Saskatoon",
                 desc="Beats Ric Flair on October 12, 1992 at an untelevised show — the "
                      "least glamorous world title win of the decade, which he has always "
                      "seemed to prefer."),
            dict(year="1994", title="Rumble co-winner, champion again",
                 desc="Co-wins the Royal Rumble with Lex Luger on January 22, loses clean to "
                      "Owen in the WrestleMania X opener on March 20, and beats Yokozuna for "
                      "the title the same night."),
            dict(year="1997", title="The double turn, the stable, the Screwjob",
                 desc="Beats Austin at WrestleMania 13 on March 23 and turns heel by winning; "
                      "leads the Hart Foundation stable through the year of the border war; "
                      "loses everything in Montreal on November 9."),
            dict(year="1999", title="WCW Champion, twice, briefly",
                 desc="Wins the tournament final over Benoit at Mayhem on November 21; the "
                      "Owen tribute match with Benoit on the October 4 Nitro is the one WCW "
                      "match of his anyone rewatches. Goldberg's kick lands December 19."),
            dict(year="2000", title="Stripped, then retired",
                 desc="Post-concussion syndrome forces the title's surrender in January and "
                      "formal retirement on October 26, 2000. A stroke follows in 2002; he "
                      "rehabilitates through the decade."),
            dict(year="2006", title="Hall of Fame, first pass",
                 desc="Inducted individually; declines to attend WrestleMania the next "
                      "night, in character to the last."),
            dict(year="2010", title="Peace with Michaels and McMahon",
                 desc="Shakes Shawn Michaels' hand on the January 4 Raw, then beats Vince "
                      "McMahon in a no-holds-barred match at WrestleMania XXVI on March 28 — "
                      "his last match."),
            dict(year="2016", title="Prostate cancer, beaten",
                 desc="Announces the diagnosis and successful surgery publicly, and adds "
                      "cancer advocacy to his stroke-recovery foundation work."),
            dict(year="2025-26", title="Canon and candour",
                 desc="Accepts the first Immortal Moment induction with Austin on April 18, "
                      "2025; gives the SummerSlam-snub interview that August; cancels late-"
                      "2025 signings citing commitments at home; sits for a Maple Leaf Pro "
                      "TSN2 interview aired August 2026."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with — in the ring and, uniquely, out of it.",
        cards=[
            dict(name="Shawn Michaels", slug="shawn-michaels",
                 desc="The Iron Man match at WrestleMania XII on March 31, 1996 — sixty "
                      "scoreless minutes, lost in overtime — then two years of genuine "
                      "backstage hatred, then Montreal on November 9, 1997: the bell rung on "
                      "a finish he never agreed to, McMahon's order, Michaels holding the "
                      "hold. Thirteen years of silence ended on the January 4, 2010 Raw with "
                      "a handshake both men have called sincere."),
            dict(name="Stone Cold Steve Austin", slug="stone-cold-steve-austin",
                 desc="Survivor Series 1996 and the WrestleMania 13 submission match — the "
                      "loss that wasn't a loss, the win that wasn't a win. Hart beat Austin "
                      "and made him; the double turn is taught as the form's perfect "
                      "execution, and WWE put the match itself in the Hall of Fame in 2025. "
                      "The two accepted side by side."),
            dict(name="Owen Hart",
                 desc="The best brother feud wrestling has produced: Owen's clean win in the "
                      "WrestleMania X opener on March 20, 1994, the cage match at SummerSlam "
                      "1994, and a reconciliation into the 1997 Hart Foundation. Owen's death "
                      "in May 1999 hangs over everything after; Bret's Nitro tribute match "
                      "with Chris Benoit that October is his WCW masterpiece."),
            dict(name="Vince McMahon",
                 desc="Employer, betrayer, and finally opponent. Montreal turned a contract "
                      "dispute into wrestling's most litigated real event — documented live "
                      "in the film Wrestling with Shadows — and the no-holds-barred win over "
                      "McMahon at WrestleMania XXVI on March 28, 2010 was less a match than "
                      "a public settlement."),
            dict(name="Goldberg",
                 desc="Twelve days after they won tag titles together, Goldberg's mule kick "
                      "at Starrcade on December 19, 1999 concussed him; Hart won the match "
                      "and lost the career. He has spent decades naming the kick as the end "
                      "of him — Goldberg has apologised; the interviews suggest the ledger "
                      "remains open."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; After",
        lead="The most documented grievance in wrestling, much of it in his own hand.",
        rows=[
            dict(when="1998", title="Hitman Hart: Wrestling with Shadows", kind="Film",
                 desc="The documentary crew that happened to be embedded during Montreal — "
                      "the Screwjob's primary source, including the locker-room aftermath."),
            dict(when="2007", title="Hitman: My Real Life in the Cartoon World of Wrestling", kind="Book",
                 desc="The autobiography, built from decades of audio diaries — widely "
                      "considered the best wrestling memoir written."),
            dict(when="2010&ndash;2011", title="WWE returns", kind="TV",
                 desc="Raw guest-host runs, the McMahon match, and a brief on-screen general "
                      "manager stint — the reconciliation era."),
            dict(when="2016&ndash;", title="Advocacy", kind="Charity",
                 desc="Stroke-recovery work through his foundation after the 2002 stroke, and "
                      "prostate cancer awareness after his 2016 surgery."),
            dict(when="2025&ndash;2026", title="Interviews", kind="Media",
                 desc="The August 2025 Slam Wrestling sit-down (the SummerSlam seat that "
                      "never materialised) and the August 2026 Maple Leaf Pro TSN2 segment "
                      "praising young Canadian wrestlers — still candid, still keeping "
                      "score."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records and the singular facts.",
        stats=[
            ("7",    "World titles, two companies"),
            ("2",    "King of the Ring wins"),
            ("2025", "Immortal Moment induction"),
        ],
        rows=[
            dict(name="Five WWF Championships in five years",
                 sub="October 12, 1992 to November 9, 1997 — the spine of the company's "
                     "mid-1990s. Only the Screwjob took the last one."),
            dict(name="Triple Crown in both WWF and WCW",
                 sub="World, Intercontinental and tag titles in the WWF; World, United States "
                     "and tag titles in WCW — the first man to complete both companies' "
                     "sets."),
            dict(name="Won the first King of the Ring pay-per-view",
                 sub="June 13, 1993, three tournament matches in one night, after already "
                     "winning the 1991 tournament edition."),
            dict(name="Royal Rumble 1994 co-winner",
                 sub="January 22, 1994, with Lex Luger — the only tie in Rumble history, "
                     "both men's feet ruled to have touched simultaneously."),
            dict(name="Three Hall of Fame inductions",
                 sub="2006 individually; 2019 with the Hart Foundation; April 18, 2025 as "
                     "half of the first Immortal Moment, the WrestleMania 13 submission "
                     "match, accepted on stage with Steve Austin."),
            dict(name="The last off-script world title change",
                 sub="Montreal, November 9, 1997 — no major world championship has changed "
                     "hands against a champion's will on a live broadcast since."),
        ],
        footnote=("No career win-loss total is published; none is reliably sourced. The WCW "
                  "World reign endpoints and the exact count of his WCW tag accounting vary "
                  "by source and are flagged in the titles table rather than smoothed over. "
                  "A skin-cancer report from recent years was not verified with a dated "
                  "source in this pass and is deliberately not repeated here."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography",
             href="https://en.wikipedia.org/wiki/Bret_Hart"),
        dict(k="Wikipedia", v="WrestleMania 13 — the double turn",
             href="https://en.wikipedia.org/wiki/WrestleMania_13"),
        dict(k="Wikipedia", v="WWE Hall of Fame (2025) — Immortal Moment induction",
             href="https://en.wikipedia.org/wiki/WWE_Hall_of_Fame_(2025)"),
        dict(k="Slam Wrestling", v="August 2025 interview — the SummerSlam snub",
             href="https://slamwrestling.net/interviews/bret-hart-on-wwes-summerslam-snub-early-career-influences-and-wrestlings-future/"),
        dict(k="PWMania", v="Late-2025 appearance cancellations and statement",
             href="https://www.pwmania.com/bret-hart-cancels-multiple-appearances-releases-statement-addressing-situation"),
        dict(k="BretHart.com", v="Official site — news and appearances",
             href="https://brethart.com/news/"),
        dict(k="Wikipedia", v="WCW United States Championship title history",
             href="https://en.wikipedia.org/wiki/List_of_WCW_United_States_Heavyweight_Champions"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="What actually happened in the Montreal Screwjob?",
            a="At Survivor Series on November 9, 1997, Bret Hart &mdash; WWF Champion, signed "
              "to WCW, and having exercised contractual creative control to decline losing in "
              "Canada &mdash; was double-crossed on live pay-per-view: Vince McMahon ordered "
              "the bell rung while Shawn Michaels held Hart in Hart&rsquo;s own Sharpshooter, "
              "though Hart had not submitted and no such finish was agreed. Hart spat on "
              "McMahon from the ring and punched him backstage; the documentary Wrestling "
              "with Shadows captured the night. It remains the last time a major world title "
              "changed hands off-script.",
            q_ld="What happened in the Montreal Screwjob?",
            a_ld="At Survivor Series in Montreal on November 9, 1997, WWF owner Vince McMahon "
                 "ordered the bell rung while Shawn Michaels held Bret Hart in the "
                 "Sharpshooter, awarding Michaels the WWF Championship even though Hart had "
                 "not submitted and had not agreed to that finish. Hart, who was leaving for "
                 "WCW, had declined to lose the title in Canada. The double-cross was real, "
                 "was captured in the documentary Wrestling with Shadows, and remains the "
                 "last off-script world title change in a major promotion."),
        dict(
            q="How many world titles did Bret Hart win?",
            a="Seven &mdash; five WWF Championships (first won from Ric Flair in Saskatoon on "
              "October 12, 1992; the others at WrestleMania X, Survivor Series 1995 and "
              "SummerSlam 1997, with the last reign ended by the Screwjob) and two WCW World "
              "Heavyweight Championships, the first won in a tournament final over Chris "
              "Benoit at Mayhem on November 21, 1999. The WCW reigns&rsquo; exact endpoints "
              "are genuinely murky &mdash; vacated, reawarded and finally stripped in January "
              "2000 when his concussion was diagnosed.",
            q_ld="How many world championships did Bret Hart win?",
            a_ld="Bret Hart won seven world championships: five WWF Championships between "
                 "October 12, 1992 and November 9, 1997, and two WCW World Heavyweight "
                 "Championships in late 1999, the first won by beating Chris Benoit in a "
                 "tournament final at WCW Mayhem on November 21, 1999. His second WCW reign "
                 "ended when the title was stripped in January 2000 after his concussion was "
                 "diagnosed."),
        dict(
            q="How did Bret Hart&rsquo;s career end?",
            a="A thrust kick from Goldberg at Starrcade on December 19, 1999 gave him a "
              "severe concussion &mdash; in a match Hart actually won. He wrestled on into "
              "January 2000 as post-concussion syndrome worsened, was stripped of the WCW "
              "title that month, and formally retired on October 26, 2000. A stroke from a "
              "2002 bicycle accident compounded the damage; he recovered most of his "
              "mobility and has spent the years since doing stroke-recovery and cancer "
              "advocacy. So the kick ended the career, but not on the night &mdash; the "
              "ending took ten months to become official.",
            q_ld="How did Bret Hart's career end?",
            a_ld="Bret Hart's career ended as a result of a severe concussion caused by a "
                 "kick from Goldberg at WCW Starrcade on December 19, 1999, in a match Hart "
                 "won. He continued wrestling into January 2000 while post-concussion "
                 "symptoms worsened, was stripped of the WCW World Heavyweight Championship "
                 "that month, and formally retired on October 26, 2000. He later suffered a "
                 "stroke in a 2002 bicycle accident and recovered through rehabilitation."),
        dict(
            q="What is Bret Hart doing in 2026?",
            a="Living in Calgary at 69, retired for a quarter century and busier as a voice "
              "than a presence: he accepted the WrestleMania 13 match&rsquo;s Hall of Fame "
              "induction with Steve Austin in April 2025, gave a candid August 2025 "
              "interview about WWE inviting him to SummerSlam and failing to seat him, "
              "cancelled a run of late-2025 US signings citing commitments at home, and sat "
              "for a Maple Leaf Pro interview aired on TSN2 in August 2026, praising young "
              "Canadian talent. He beat prostate cancer in 2016 and does not perform "
              "physically in any capacity.",
            q_ld="What is Bret Hart doing in 2026?",
            a_ld="In 2026 Bret Hart, aged 69, is retired and lives in Calgary. His recent "
                 "activity includes accepting the WWE Hall of Fame's first Immortal Moment "
                 "induction alongside Steve Austin in April 2025, a candid August 2025 "
                 "interview about being invited to SummerSlam without being given a seat, "
                 "cancelling several late-2025 autograph appearances for personal reasons, "
                 "and a sit-down interview aired on Maple Leaf Pro Wrestling's TSN2 show in "
                 "August 2026. He does not wrestle or perform physically."),
        dict(
            q="Did Bret Hart really turn heel by winning at WrestleMania 13?",
            a="Yes &mdash; that is the double turn. He beat Steve Austin legitimately by "
              "the match&rsquo;s rules on March 23, 1997, when Austin passed out in the "
              "Sharpshooter rather than submit, but Hart&rsquo;s refusal to release the "
              "hold and his post-match attack flipped the crowd: Austin left the hero, "
              "Hart left the villain. It is the cleanest example of both wrestlers "
              "swapping alignments inside one match, and WWE inducted the match itself "
              "into the Hall of Fame in 2025.",
            q_ld="Did Bret Hart turn heel by winning at WrestleMania 13?",
            a_ld="Yes. At WrestleMania 13 on March 23, 1997, Bret Hart beat Steve Austin "
                 "when Austin passed out in the Sharpshooter rather than submit, and Hart's "
                 "refusal to release the hold turned the crowd against him. Hart entered as "
                 "the fan favourite and left as the villain while Austin left as the hero — "
                 "the definitive double turn. WWE inducted the match into its Hall of Fame "
                 "as the first Immortal Moment in 2025."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Bret Sergeant Hart"),
        dict(label="Born", value="July 2, 1957", sub="Calgary, Alberta &middot; age 69"),
        dict(label="Billed from", value="Calgary, Alberta, Canada"),
        dict(label="Height", value="6&#8242;0&#8243;", sub="183 cm"),
        dict(label="Weight", value="235 lb", sub="107 kg (billed)"),
        dict(label="Debut", value="1978", sub="Stampede Wrestling &middot; the Hart family Dungeon"),
        dict(label="Last match", value="March 28, 2010",
             sub="def. Vince McMahon, no holds barred, WrestleMania XXVI"),
        dict(label="Family", value="Eighth of Stu and Helen Hart's twelve children",
             sub="brother of Owen Hart; the Dungeon's most famous graduate"),
        dict(label="Signature", value="Sharpshooter &middot; the Five Moves of Doom",
             sub="backbreaker, elbow from the second rope, Russian legsweep, bulldog, Sharpshooter"),
        dict(label="Hall of Fame", value="2006, 2019 &amp; 2025",
             sub="individual &middot; Hart Foundation &middot; WrestleMania 13 as an Immortal Moment"),
        dict(label="Health", value="Concussion 1999 &middot; stroke 2002 &middot; prostate cancer beaten 2016",
             sub="the reason there was never a nostalgia match"),
        dict(label="Now", value="Retired in Calgary", sub="interviews, advocacy, and a long memory"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1957-07-02",
    bornplace="Calgary, Alberta, Canada",
    nationality="Canada",
    height_cm=183,
    weight_kg=107,
    ld=dict(
        alternateName=["Bret Sergeant Hart", "The Hitman", "Bret 'The Hitman' Hart",
                       "The Excellence of Execution"],
        award=["WWF Championship (5 reigns)",
               "WCW World Heavyweight Championship (2 reigns)",
               "WWF Intercontinental Championship (2 reigns)",
               "WCW United States Heavyweight Championship (4 reigns)",
               "WWF Tag Team Championship (2 reigns, Hart Foundation)",
               "WCW World Tag Team Championship (1 reign, with Goldberg)",
               "King of the Ring (1991, 1993)",
               "Royal Rumble co-winner (1994)",
               "WWE Hall of Fame (2006; 2019 with the Hart Foundation; 2025 Immortal Moment)"],
        knowsAbout=["Professional wrestling", "WWF", "WCW", "Stampede Wrestling",
                    "The Hart wrestling family", "Stroke recovery advocacy"],
        description="Bret Hart, born July 2, 1957 in Calgary, is a retired Canadian professional "
                    "wrestler who won five WWF Championships and two WCW World Heavyweight "
                    "Championships. Known as the Hitman and the Excellence of Execution, he was "
                    "the victim of the 1997 Montreal Screwjob, retired in 2000 after a "
                    "concussion, and is a three-time WWE Hall of Fame inductee, most recently in "
                    "2025 when his WrestleMania 13 match with Steve Austin became the first "
                    "Immortal Moment inductee.",
        sameAs=["https://en.wikipedia.org/wiki/Bret_Hart",
                "https://brethart.com/",
                "https://www.wwe.com/superstars/bret-hart"],
    ),
)
