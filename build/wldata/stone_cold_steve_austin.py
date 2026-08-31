# -*- coding: utf-8 -*-
"""Stone Cold Steve Austin - dossier data.

Sources: web-verified August 31, 2026 - Wikipedia (Stone Cold Steve Austin; WrestleMania 13;
WWE Hall of Fame (2025)), WWE.com's official profile, Newsweek (March 16, 2026, on him
skipping 3:16 Day for a desert race) and Slam Wrestling (February 10, 2026, WrestleMania 42
weekend booking). All record-row dates are day-precision and verified against those pages.

Deliberate omissions:
  * No career win-loss total - none is reliably published anywhere, and nothing is invented.
  * No theme entry - "I Won't Do What You Tell Me" and Disturbed's "Glass Shatters" are real,
    but no Spotify track URL was verified in this pass, so the block is omitted per house rule.
  * No social links - handles were not verified in this pass.
  * The wrestlelore pages for the earlier gimmicks (/wrestlers/stunning-steve-austin/ and
    /wrestlers/the-ringmaster/) cover the WCW and 1995-96 WWF runs; this dossier covers the
    Stone Cold persona and only points at those pages.
"""

# ----------------------------------------------------------------- record rows
# Twelve documented bouts - the 3:16 speech, the double turn, the neck break, four title
# wins at WrestleMania-level events, the 2003 farewell and the 2022 one-night return.
ROWS = [
    dict(result="W", date="1996-06-23", promo="WWE", landmark=True,
         event="King of the Ring 1996 — Milwaukee", opponent="Jake Roberts",
         stip="Tournament final — the Austin 3:16 speech", title=""),
    dict(result="L", date="1996-11-17", promo="WWE",
         event="Survivor Series — Madison Square Garden", opponent="Bret Hart", opponent_html=True,
         stip="Singles — Hart's return match", title=""),
    dict(result="W", date="1997-01-19", promo="WWE", type="tag",
         event="Royal Rumble match — San Antonio", opponent="The 1997 Royal Rumble field",
         stip="Wins after referees miss his elimination", title=""),
    dict(result="L", date="1997-03-23", promo="WWE", landmark=True,
         event="WrestleMania 13 — Rosemont", opponent="Bret Hart", opponent_html=True,
         stip="Submission match — passes out in the Sharpshooter; the double turn", title=""),
    dict(result="W", date="1997-08-03", promo="WWE", landmark=True,
         event="SummerSlam — East Rutherford", opponent="Owen Hart",
         stip="Singles — wins the title after the piledriver that broke his neck",
         title="WWF Intercontinental Championship"),
    dict(result="W", date="1998-03-29", promo="WWE", landmark=True,
         event="WrestleMania XIV — Boston", opponent="Shawn Michaels", opponent_html=True,
         stip="Singles — first WWF Championship; Mike Tyson counts the pin",
         title="WWF Championship"),
    dict(result="L", date="1998-06-28", promo="WWE",
         event="King of the Ring 1998", opponent="Kane", opponent_html=True,
         stip="First Blood match — regains the title the next night on Raw",
         title="WWF Championship"),
    dict(result="W", date="1999-03-28", promo="WWE", landmark=True,
         event="WrestleMania XV — Philadelphia", opponent="The Rock",
         stip="No disqualification — third WWF Championship", title="WWF Championship"),
    dict(result="W", date="2001-04-01", promo="WWE", landmark=True,
         event="WrestleMania X-Seven — Houston", opponent="The Rock",
         stip="No disqualification — wins with Vince McMahon's help; the heel turn",
         title="WWF Championship"),
    dict(result="L", date="2001-12-09", promo="WWE",
         event="Vengeance", opponent="Chris Jericho",
         stip="Unification tournament final — Jericho becomes Undisputed Champion",
         title="WWF Championship"),
    dict(result="L", date="2003-03-30", promo="WWE", landmark=True,
         event="WrestleMania XIX — Seattle", opponent="The Rock",
         stip="Singles — his last match for nineteen years", title=""),
    dict(result="W", date="2022-04-02", promo="WWE", landmark=True,
         event="WrestleMania 38 Night 1 — Arlington", opponent="Kevin Owens",
         stip="No holds barred — the actual last match, at 57", title=""),
]

for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Bret Hart": "bret-hart", "Shawn Michaels": "shawn-michaels",
                 "Kane": "kane"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="stone-cold-steve-austin",
    name="Stone Cold Steve Austin",
    realname="Steven James Anderson (later Steve Williams)",
    epithet="The Texas Rattlesnake",
    hook="Record & Titles",

    meta_desc=("Stone Cold Steve Austin won six WWF Championships, three Royal Rumbles and the "
               "1996 King of the Ring, and drew the biggest business in WWF history. Full record, "
               "titles, the 1997 double turn and the 2022 return."),
    og_desc=("The Texas Rattlesnake: six WWF Championships, three Royal Rumble wins, the WrestleMania "
             "13 double turn, and a last match that came nineteen years after the one everyone "
             "remembers as his last."),
    tw_desc="Six WWF titles, three Royal Rumbles, one broken neck, and a 2022 curtain call.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1989",
    height_imp="6&#8242;2&#8243;",
    weight_lb="252",
    world_titles="6",
    vitals_tagline="Austin 3:16",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="SC", title="WWE Shop", sub="Official 3:16 tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable legend in the 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="BS", title="El Segundo Brewing", sub="Broken Skull IPA collaboration",
             tag="Visit", href="https://www.elsegundobrewing.com/"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/stone-cold-steve-austin"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Texas Rattlesnake &middot; The Bionic Redneck &middot; formerly Stunning Steve",
    hero_tag="Victoria, Texas &middot; <em>USWA &middot; WCW &middot; ECW &middot; WWF/WWE &middot; 1989&ndash;2003, 2022</em>",
    now_label="NOW",
    now_bold="Retired &mdash; rancher, broadcaster and off-road racer",
    now_tail=" &middot; skipped 3:16 Day 2026 to prep a race truck for a 250-mile desert race; "
             "signed at WWE World over WrestleMania 42 weekend in Las Vegas",
    hstats=[
        dict(value="6",    x=True,  label="WWF Titles"),
        dict(value="3",    x=True,  label="Royal Rumbles"),
        dict(value="3:16", x=False, label="King of the Ring 1996"),
        dict(value="19",   x=False, label="Years Between Last Matches"),
    ],
    ghost_link="From a Dallas loading dock to the biggest draw the company ever had",
    vlabel="Est. 1989 &middot; Victoria, Texas",
    mono="SC",

    # ---------------------------------------------------------------- 01 overview
    correction=2,
    overview=[
        "<b>Stone Cold Steve Austin</b> is a six-time WWF Champion, a three-time Royal Rumble winner "
        "&mdash; the only man with three &mdash; and the wrestler most historians credit with turning "
        "the Monday Night War. He is a Texan brawler whose entire act was compressed into a single "
        "sentence at King of the Ring on June 23, 1996: he beat Jake Roberts in the tournament final "
        "and told him that &ldquo;Austin 3:16 says I just whipped your ass.&rdquo; "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">6&times;</span>'
        '<span class="pull-cap">WWF Champion between March 1998 and December 2001 &mdash; every reign inside four years</span></span>'
        "Within two years that sentence was the best-selling T-shirt in the business, and the company "
        "built its entire Attitude Era around him fighting his own boss. All six title reigns sit "
        "inside a four-year window, because the career itself was compressed: a broken neck in 1997, "
        "the top of the business by 1998, and out as a full-time wrestler by 2003 at 38.",

        "The making of him was a loss. At WrestleMania 13 on March 23, 1997, in Rosemont, Bret Hart "
        "trapped him in the Sharpshooter in a submission match and Austin, face covered in blood, "
        "passed out rather than quit. He went in the heel and came out the hero &mdash; the famous "
        "double turn &mdash; and in April 2025 WWE made that match the first induction in the Hall of "
        "Fame&rsquo;s new Immortal Moment category, with both men on stage in Las Vegas to accept it. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">1997</span>'
        '<span class="pull-cap">the double turn at WrestleMania 13, and the broken neck at SummerSlam &mdash; both in one year</span></span>'
        "Five months after Rosemont, Owen Hart&rsquo;s botched piledriver at SummerSlam on August 3, "
        "1997 bruised his spinal cord and left him temporarily paralysed in the ring; he still won the "
        "Intercontinental Championship that night, but the injury rewrote his style, shortened his "
        "career, and hangs over every list of what he might have done with a healthy neck.",

        "His last match is almost always given as WrestleMania XIX against The Rock on March 30, 2003, "
        "and for nineteen years that was true. It is not any more. At WrestleMania 38 on April 2, "
        "2022, at 57, he answered Kevin Owens&rsquo; talk-show challenge with a full no-holds-barred "
        "match &mdash; not a run-in, a match, which he won &mdash; and that is now the final bout on "
        "his record. The 2003 Seattle match remains the last of his full-time career and the end of "
        "the trilogy of WrestleMania main-card matches with The Rock (XV, X-Seven, XIX), all three of "
        "which he headlined and the first two of which he won; the 2022 match is a one-night coda. "
        "Any page that says he retired in 2003 and never wrestled again is out of date by one match.",

        "In 2026 he is a 61-year-old retiree who stays busy on his own terms. He spent years as "
        "cable&rsquo;s blue-collar everyman &mdash; the Broken Skull Challenge, Straight Up Steve "
        "Austin, the Broken Skull Sessions interview show, a long-running podcast &mdash; and his "
        "current obsession is off-road racing: he told interviewers in March 2026 that he was skipping "
        "WWE&rsquo;s 3:16 Day show in his hometown of San Antonio because he was in a Nevada garage "
        "getting a side-by-side ready for a 250-mile desert race (Newsweek). He still shows up when it "
        "counts &mdash; the 2025 Hall of Fame stage with Bret Hart, a WWE World signing over "
        "WrestleMania 42 weekend in Las Vegas in April 2026 &mdash; but he has stayed firm that the "
        "Owens match scratched the itch. He went into the Hall of Fame as an individual in 2009.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWF/WWE"},
        stats=[
            ("6&times;", "WWF Championship"),
            ("3&times;", "Royal Rumble wins"),
            ("2&times;", "Intercontinental"),
            ("4&times;", "Tag team titles"),
            ("1996",     "King of the Ring"),
            ("2009",     "Hall of Fame"),
        ],
        lead=("Twelve documented bouts &mdash; the 3:16 speech, the double turn, the neck break, the "
              "four biggest title wins, the Seattle farewell and the 2022 return. This is a curated "
              "ledger, not a career count, and no career win&ndash;loss total is published because no "
              "reliable one exists. His WCW and Ringmaster years are covered on their own pages. "
              "Filter by match type, tap any column header to sort, and turn spoilers on to reveal "
              "results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the reputation rests on. The WrestleMania 13 submission match is the "
                    "one WWE itself canonised in 2025 as the first Immortal Moment inductee; the "
                    "ratings shown are Wrestling Observer figures as commonly reported, not "
                    "re-verified against Observer archives."),
    signature=[
        dict(rating="5.0", event="WrestleMania 13 — Rosemont", opponent="Bret Hart",
             stip="Submission match — the double turn; Hall of Fame Immortal Moment, 2025"),
        dict(rating="4.5", event="WrestleMania X-Seven — Houston", opponent="The Rock",
             stip="WWF Championship — no disqualification; the heel turn"),
        dict(rating="4.5", event="Survivor Series 1996 — Madison Square Garden", opponent="Bret Hart",
             stip="Singles — the technical prequel to Rosemont"),
        dict(rating="4.0", event="WrestleMania XIV — Boston", opponent="Shawn Michaels",
             stip="WWF Championship — the era changes hands"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("6&times;", "WWF Championship"),
            ("2&times;", "Intercontinental"),
            ("4&times;", "WWF tag titles"),
            ("2&times;", "WCW titles held"),
        ],
        lead=("Every WWF Championship reign sits between WrestleMania XIV in March 1998 and Vengeance "
              "in December 2001 &mdash; the most compressed six-reign run any WWF/WWE Champion has "
              "had. He is a Triple Crown Champion. Exact endpoints for the tag reigns and the WCW "
              "belts were not re-verified in this pass and are stated loosely rather than guessed."),
        rows=[
            dict(ic="W", name="WWF Championship", count="6",
                 sub="March 29, 1998 (def. Shawn Michaels, WrestleMania XIV) through December 9, 2001 "
                     "(lost to Chris Jericho in the unification final at Vengeance) &middot; other "
                     "wins: June 29, 1998 Raw (Kane), WrestleMania XV (The Rock), June 28, 1999 Raw "
                     "(The Undertaker), WrestleMania X-Seven (The Rock), October 8, 2001 Raw (Kurt "
                     "Angle)"),
            dict(ic="I", name="WWF Intercontinental Championship", count="2",
                 sub="First won from Owen Hart at SummerSlam, August 3, 1997 &mdash; the night of the "
                     "broken neck; forfeited that autumn because of it, then regained from Owen at "
                     "Survivor Series, November 9, 1997"),
            dict(ic="T", name="WWF Tag Team Championship", count="4",
                 sub="With four different partners &mdash; Shawn Michaels and Dude Love in 1997, The "
                     "Undertaker in 1998, Triple H in 2001 &mdash; a running gag about a man who "
                     "could not keep a partner"),
            dict(ic="C", name="WCW United States &amp; Tag Team Championships", count="2+",
                 sub="As Stunning Steve Austin, 1991&ndash;1995, including two US reigns and a tag "
                     "reign with Brian Pillman as the Hollywood Blonds &mdash; covered in full on the "
                     "Stunning Steve Austin page"),
            dict(ic="M", name="Million Dollar Championship", count="1",
                 sub="Handed to him as The Ringmaster in 1996 &mdash; unrecognised by WWE title "
                     "history; the gimmick has its own page"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Alliances",
        lead="He was mostly a one-man act &mdash; the exceptions were short, and two of them are "
             "among the most replayed angles ever taped.",
        cards=[
            dict(era="WCW &middot; 1993&ndash;1994",
                 name="The Hollywood Blonds",
                 members="Stunning Steve Austin &amp; Brian Pillman",
                 desc="The tag team that first showed the personality — smug, quick, camera-mugging "
                      "heels who held the WCW tag titles for five months. WCW split them up early, "
                      "which Austin has called one of the company's dumbest calls, and the full run "
                      "lives on the Stunning Steve Austin page."),
            dict(era="WWF &middot; 1998&ndash;1999, 2001",
                 name="The war with the McMahons",
                 members="Austin against Vince McMahon's Corporation",
                 desc="Not a faction but the axis of the entire Attitude Era: the wage worker giving "
                      "the owner a Stunner every week. Beer trucks, cement trucks, a bedpan — the "
                      "feud drew the highest ratings in company history and made both men."),
            dict(era="WWF &middot; 2001",
                 name="The Alliance &amp; the Two-Man Power Trip",
                 members="Austin, Triple H; later the WCW/ECW Alliance",
                 desc="The heel experiment. After turning at WrestleMania X-Seven he held the WWF "
                      "title as Vince's ally, formed the Two-Man Power Trip with Triple H (tag "
                      "champions together in spring 2001), then led the Alliance in the Invasion "
                      "angle. Business sagged, and he has said turning heel in his home state was a "
                      "mistake he owns."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Four names to get to the one that mattered: <b>Stunning Steve Austin</b> (WCW, "
             "1991&ndash;1995) &rarr; <b>The Ringmaster</b> (WWF, 1995&ndash;1996) &rarr; <b>Stone "
             "Cold Steve Austin</b> (1996&ndash;present). The first two have their own wrestlelore "
             "pages; this one covers the persona that sold the shirts.",
        cards=[
            dict(mono="SSA", era="WCW &middot; 1991&ndash;1995", name="Stunning Steve Austin",
                 desc="Blond, arrogant, and by his own account going nowhere — a two-time US Champion "
                      "and half of the Hollywood Blonds, fired by WCW over the phone in 1995 while "
                      "injured. Covered in full at /wrestlers/stunning-steve-austin/."),
            dict(mono="RM", era="WWF &middot; 1995&ndash;1996", name="The Ringmaster",
                 desc="Ted DiBiase's hand-picked Million Dollar Champion, a gimmick with someone "
                      "else's voice. He hated it, and the company let him rename himself within "
                      "months. Covered at /wrestlers/the-ringmaster/."),
            dict(mono="SC", era="WWF/WWE &middot; 1996&ndash;present", name="Stone Cold",
                 desc="Shaved head, black trunks, no music cues wasted — the glass shattered and the "
                      "arena stood up. Built from a serial-killer documentary pitch and a cup of tea: "
                      "his English ex-wife telling him to drink it before it got stone cold. The "
                      "3:16 promo made the name scripture."),
            dict(mono="TR", era="Since 2003", name="The broadcaster and pitchman",
                 desc="Podcasts, reality shows, the Broken Skull Sessions interview chair, beer and "
                      "whiskey brands, and now off-road racing — the persona intact, the language "
                      "unchanged, no wrestling required."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="A Dallas wrestling school in 1989 to the biggest box-office run the WWF ever had.",
        rows=[
            dict(year="1989", title="Debut in Texas",
                 desc="Trained by Chris Adams at the Dallas Sportatorium school; early work in USWA "
                      "as Steve Austin, the surname chosen to avoid clashing with Steve Williams."),
            dict(year="1991", title="WCW, as Stunning Steve",
                 desc="TV Champion within months, two US title reigns, the Hollywood Blonds with "
                      "Brian Pillman — then fired by phone in 1995."),
            dict(year="1996", title="Austin 3:16",
                 desc="Wins King of the Ring on June 23, 1996 and cuts the promo on Jake Roberts "
                      "that names the era. The Ringmaster is dead within the year."),
            dict(year="1997", title="The double turn and the broken neck",
                 desc="Passes out rather than submits to Bret Hart at WrestleMania 13 on March 23; "
                      "Owen Hart's piledriver bruises his spinal cord at SummerSlam on August 3. He "
                      "leaves 1997 the most popular man in the company."),
            dict(year="1998", title="First WWF Championship",
                 desc="Beats Shawn Michaels at WrestleMania XIV on March 29 with Mike Tyson as "
                      "enforcer. The McMahon feud begins in earnest; Raw finally beats Nitro."),
            dict(year="1999", title="The trilogy begins",
                 desc="Beats The Rock at WrestleMania XV on March 28 — the first of three "
                      "consecutive odd-year WrestleMania headline matches between them."),
            dict(year="2000", title="A year lost to the neck",
                 desc="Spinal surgery in January 2000 costs him most of the year; the Rikishi "
                      "hit-and-run angle explains the absence."),
            dict(year="2001", title="The heel turn",
                 desc="Wins his third Royal Rumble, then shakes Vince McMahon's hand to beat The "
                      "Rock at WrestleMania X-Seven on April 1. Two more title reigns follow; "
                      "Jericho unifies the belts over him in December."),
            dict(year="2003", title="The Seattle farewell",
                 desc="Loses to The Rock at WrestleMania XIX on March 30 in what stands for nineteen "
                      "years as his last match. Neck and health end the full-time career at 38."),
            dict(year="2009", title="Hall of Fame",
                 desc="Inducted as an individual, the year before headlining-era peers followed. "
                      "Television and podcasting fill the next decade."),
            dict(year="2022", title="One more at 57",
                 desc="Beats Kevin Owens in a no-holds-barred match at WrestleMania 38 Night 1 on "
                      "April 2, 2022 — the true final match."),
            dict(year="2025-26", title="Legacy laps",
                 desc="On stage with Bret Hart on April 18, 2025 as WrestleMania 13 becomes the "
                      "first Immortal Moment inductee; skips 3:16 Day 2026 for desert-race prep; "
                      "signs at WWE World during WrestleMania 42 weekend in Las Vegas."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Bret Hart", slug="bret-hart",
                 desc="The rivalry that built him. Hart beat him at Survivor Series 1996 and again "
                      "at WrestleMania 13 on March 23, 1997, and the second loss made Austin's "
                      "career: bloody, unconscious, never quitting. The double turn is the textbook "
                      "example of the form, and in 2025 WWE inducted the match itself into the Hall "
                      "of Fame. The two men, enemies on tape and friends off it, accepted together."),
            dict(name="Vince McMahon",
                 desc="The boss. From late 1997 through 1999 the weekly question of whether Austin "
                      "would keep his job or Stunner his employer carried the highest-rated "
                      "wrestling television ever made. Every authority figure feud since is a "
                      "photocopy of it."),
            dict(name="The Rock",
                 desc="Three WrestleMania headline matches — XV, X-Seven, XIX — the only pair to "
                      "headline three. Austin won the first two; the Rock won the last, in Austin's "
                      "final full-time match on March 30, 2003, a result Austin has said he was at "
                      "peace with giving him."),
            dict(name="Owen Hart",
                 desc="The rivalry with the physical cost: the SummerSlam 1997 piledriver that "
                      "bruised his spinal cord. Austin won the Intercontinental title that night "
                      "and beat Owen again for it at Survivor Series, but the neck was never the "
                      "same, and the injury shortened everything that followed."),
            dict(name="Shawn Michaels", slug="shawn-michaels",
                 desc="One match that mattered more than a feud: WrestleMania XIV, March 29, 1998, "
                      "Michaels wrestling on a destroyed back, Tyson at ringside, and the belt — "
                      "and the company — handed to Austin."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Business",
        lead="The busiest post-ring media career of his generation, all of it in his own voice.",
        rows=[
            dict(when="2013&ndash;", title="The Steve Austin Show / podcasting", kind="Podcast",
                 desc="One of the first major wrestler podcasts, running in various forms across "
                      "PodcastOne and other platforms for over a decade."),
            dict(when="2014&ndash;2017", title="Broken Skull Challenge", kind="TV",
                 desc="CMT obstacle-course competition on his Texas ranch property, four seasons."),
            dict(when="2019&ndash;2022", title="Broken Skull Sessions", kind="TV",
                 desc="Long-form sit-down interview show on the WWE Network and Peacock — The "
                      "Undertaker was the first guest, the night after his final farewell."),
            dict(when="2023", title="Stone Cold Takes on America", kind="TV",
                 desc="A&E road-trip series; the same network's Biography: WWE Legends episode "
                      "covers his career."),
            dict(when="2026", title="Off-road racing", kind="Sport",
                 desc="His stated 2026 priority: building and racing a side-by-side in desert "
                      "events, which he cited when passing on WWE's 3:16 Day show in San Antonio "
                      "in March 2026 (Newsweek)."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records and the numbers, stated the way the sources state them.",
        stats=[
            ("3",    "Royal Rumble wins"),
            ("3",    "Rock WrestleMania headliners"),
            ("2025", "Immortal Moment induction"),
        ],
        rows=[
            dict(name="Only three-time Royal Rumble winner",
                 sub="1997, 1998 and 2001 — still unmatched as of the 2026 Rumble. The 1997 win "
                     "came after referees missed his elimination, a finish WWE played straight."),
            dict(name="Six WWF Championship reigns in under four years",
                 sub="March 29, 1998 to December 9, 2001. Nobody has packed six world reigns into "
                     "a tighter window in company history."),
            dict(name="First Immortal Moment inductee, WWE Hall of Fame 2025",
                 sub="The WrestleMania 13 submission match against Bret Hart was inducted April 18, "
                     "2025 at the Fontainebleau Las Vegas, accepted by both men — the first match, "
                     "rather than person, WWE has enshrined."),
            dict(name="Headlined three WrestleManias against The Rock",
                 sub="XV (1999), X-Seven (2001) and XIX (2003) — the only opponent pairing with "
                     "three WrestleMania headline matches."),
            dict(name="The merchandise benchmark",
                 sub="Austin 3:16 is routinely described as the best-selling T-shirt in wrestling "
                     "history; exact sales figures have never been published, so the claim is "
                     "reported here as the industry consensus it is rather than a number."),
            dict(name="A last match nineteen years after the farewell",
                 sub="WrestleMania XIX, March 30, 2003, then WrestleMania 38, April 2, 2022 — a "
                     "no-holds-barred win over Kevin Owens at 57 in front of his home-state crowd "
                     "in Arlington."),
        ],
        footnote=("Two things are deliberately absent. No career win-loss total, because no reliable "
                  "one exists in any source consulted. No Spotify theme block: the entrance themes "
                  "are famous, but no track URL was verified in this pass, and house rules say omit "
                  "rather than guess."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography",
             href="https://en.wikipedia.org/wiki/Stone_Cold_Steve_Austin"),
        dict(k="WWE.com", v="Official profile",
             href="https://www.wwe.com/superstars/stone-cold-steve-austin"),
        dict(k="Wikipedia", v="WrestleMania 13 — the double turn",
             href="https://en.wikipedia.org/wiki/WrestleMania_13"),
        dict(k="Wikipedia", v="WWE Hall of Fame (2025) — Immortal Moment induction",
             href="https://en.wikipedia.org/wiki/WWE_Hall_of_Fame_(2025)"),
        dict(k="Newsweek", v="Skipping 3:16 Day 2026 for a desert race",
             href="https://www.newsweek.com/sports/wrestling/stone-cold-steve-austin-addresses-status-for-316-day-wwe-raw-11683787"),
        dict(k="Slam Wrestling", v="WrestleMania 42 weekend WWE World appearance",
             href="https://slamwrestling.net/news/stone-cold-steve-austin-set-for-wrestlemania-42-appearance/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="When was Stone Cold Steve Austin&rsquo;s last match?",
            a="April 2, 2022 &mdash; a no-holds-barred win over Kevin Owens at WrestleMania 38 Night "
              "1 in Arlington, Texas, at age 57. The match everyone remembers as his last, the "
              "WrestleMania XIX loss to The Rock on March 30, 2003 in Seattle, was the end of his "
              "full-time career and stood as his final bout for nineteen years, but the Owens match "
              "now closes the record. He has repeatedly said since that it scratched the itch and he "
              "has no plans for another.",
            q_ld="When was Stone Cold Steve Austin's last match?",
            a_ld="Stone Cold Steve Austin's last match was on April 2, 2022, when he defeated Kevin "
                 "Owens in a no-holds-barred match at WrestleMania 38 Night 1 in Arlington, Texas, at "
                 "age 57. His previous match, a loss to The Rock at WrestleMania XIX on March 30, "
                 "2003 in Seattle, ended his full-time career and stood as his final bout for "
                 "nineteen years."),
        dict(
            q="How many times was Steve Austin WWF Champion?",
            a="Six &mdash; all between March 29, 1998 (beating Shawn Michaels at WrestleMania XIV) "
              "and December 9, 2001 (losing the unification final to Chris Jericho at Vengeance). "
              "The other wins came over Kane (June 29, 1998 Raw), The Rock (WrestleMania XV), The "
              "Undertaker (June 28, 1999 Raw), The Rock again (WrestleMania X-Seven) and Kurt Angle "
              "(October 8, 2001 Raw). He also won the Intercontinental Championship twice, four tag "
              "team championships, the 1996 King of the Ring, and a record three Royal Rumbles.",
            q_ld="How many times was Steve Austin WWF Champion?",
            a_ld="Steve Austin was WWF Champion six times, with every reign falling between March 29, "
                 "1998, when he beat Shawn Michaels at WrestleMania XIV, and December 9, 2001, when "
                 "he lost the unification final to Chris Jericho at Vengeance. He also held the "
                 "Intercontinental Championship twice, won four tag team championships, the 1996 King "
                 "of the Ring, and a record three Royal Rumble matches in 1997, 1998 and 2001."),
        dict(
            q="What happened at WrestleMania 13, and why does it matter so much?",
            a="On March 23, 1997, Bret Hart beat Austin in a submission match when Austin, bleeding "
              "heavily, passed out in the Sharpshooter rather than give up. Hart went in the fan "
              "favourite and left the villain; Austin went in the villain and left the biggest star "
              "in the company &mdash; the definitive double turn. In April 2025 WWE inducted the "
              "match itself into the Hall of Fame as the first entry in its Immortal Moment "
              "category, accepted by both men.",
            q_ld="What happened between Steve Austin and Bret Hart at WrestleMania 13?",
            a_ld="At WrestleMania 13 on March 23, 1997, Bret Hart defeated Steve Austin in a "
                 "submission match when Austin, bleeding heavily, passed out in the Sharpshooter "
                 "rather than submit. The match executed a double turn: Hart left as a villain and "
                 "Austin as the company's biggest hero. In April 2025 WWE inducted the match into "
                 "the Hall of Fame as the first Immortal Moment inductee."),
        dict(
            q="What is Steve Austin doing in 2026?",
            a="Living retired on his own schedule: ranch life, media work, and &mdash; his stated "
              "2026 priority &mdash; off-road racing. In March 2026 he passed on appearing at "
              "WWE&rsquo;s 3:16 Day Raw in San Antonio because he was preparing a side-by-side for "
              "a 250-mile desert race (Newsweek). He signed for fans at WWE World during "
              "WrestleMania 42 weekend in Las Vegas in April 2026, with no in-ring role. He is 61, "
              "and there is no indication of another match.",
            q_ld="What is Steve Austin doing in 2026?",
            a_ld="In 2026 Steve Austin is retired from wrestling and focused on off-road racing, "
                 "ranch life and media work. In March 2026 he skipped WWE's 3:16 Day Raw in San "
                 "Antonio to prepare a vehicle for a 250-mile desert race, and in April 2026 he "
                 "made a fan appearance at WWE World during WrestleMania 42 weekend in Las Vegas. "
                 "He is 61 and has given no indication he will wrestle again."),
        dict(
            q="Did the Owen Hart piledriver really break Austin&rsquo;s neck?",
            a="It caused a legitimate spinal injury &mdash; a bruised spinal cord with temporary "
              "paralysis, suffered at SummerSlam on August 3, 1997, on a botched sit-down "
              "piledriver. Austin still finished the match and won the Intercontinental "
              "Championship, but the injury required spinal surgery in early 2000, cost him most "
              "of that year, and is the main reason his full-time career ended at 38 in 2003.",
            q_ld="Did Owen Hart's piledriver really injure Steve Austin's neck?",
            a_ld="Yes. At SummerSlam on August 3, 1997, a botched sit-down piledriver from Owen "
                 "Hart bruised Steve Austin's spinal cord and left him temporarily paralysed in "
                 "the ring. Austin finished the match and won the Intercontinental Championship, "
                 "but the injury led to spinal surgery in early 2000 and was the main reason his "
                 "full-time career ended in 2003, when he was 38."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Steven James Anderson",
             sub="raised as Steve Williams; legally Steve Austin since 2007"),
        dict(label="Born", value="December 18, 1964", sub="Austin, Texas &middot; raised in Edna &middot; age 61"),
        dict(label="Billed from", value="Victoria, Texas"),
        dict(label="Height", value="6&#8242;2&#8243;", sub="188 cm"),
        dict(label="Weight", value="252 lb", sub="114 kg (billed)"),
        dict(label="Debut", value="1989", sub="Dallas, Texas &middot; trained by Chris Adams"),
        dict(label="Last match", value="April 2, 2022",
             sub="def. Kevin Owens, WrestleMania 38 Night 1 &mdash; nineteen years after the "
                 "WrestleMania XIX farewell"),
        dict(label="Ring names",
             value="Stunning Steve Austin &rarr; The Ringmaster &rarr; Stone Cold Steve Austin",
             sub="the first two have their own wrestlelore pages"),
        dict(label="Signature", value="Stone Cold Stunner &middot; Lou Thesz press &middot; "
                                      "Mudhole stomps"),
        dict(label="Hall of Fame", value="2009",
             sub="plus the WrestleMania 13 match as 2025&rsquo;s first Immortal Moment"),
        dict(label="Now", value="Retired &mdash; media and off-road racing",
             sub="skipped 3:16 Day 2026 for race prep; WWE World signing, WrestleMania 42 weekend"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1964-12-18",
    bornplace="Austin, Texas, United States",
    nationality="United States",
    height_cm=188,
    weight_kg=114,
    ld=dict(
        alternateName=["Steve Austin", "Steven James Anderson", "Steve Williams",
                       "Stunning Steve Austin", "The Ringmaster", "The Texas Rattlesnake",
                       "The Bionic Redneck"],
        award=["WWF Championship (6 reigns)",
               "WWF Intercontinental Championship (2 reigns)",
               "WWF Tag Team Championship (4 reigns)",
               "Royal Rumble winner (1997, 1998, 2001)",
               "King of the Ring (1996)",
               "WWE Hall of Fame (2009)",
               "WWE Hall of Fame Immortal Moment — WrestleMania 13 vs Bret Hart (2025)"],
        knowsAbout=["Professional wrestling", "WWF Attitude Era", "WWE", "WCW",
                    "Broadcasting", "Podcasting", "Off-road racing"],
        description="Stone Cold Steve Austin, born Steven James Anderson in Austin, Texas, is a "
                    "retired American professional wrestler and media personality. He won the WWF "
                    "Championship six times between 1998 and 2001, a record three Royal Rumbles, "
                    "the 1996 King of the Ring, and was the top drawing star of the WWF's Attitude "
                    "Era. His WrestleMania 13 submission match against Bret Hart became the first "
                    "Immortal Moment inducted into the WWE Hall of Fame in 2025. His final match "
                    "was a 2022 win over Kevin Owens at WrestleMania 38.",
        sameAs=["https://en.wikipedia.org/wiki/Stone_Cold_Steve_Austin",
                "https://www.wwe.com/superstars/stone-cold-steve-austin"],
    ),
)
