# -*- coding: utf-8 -*-
"""Goldberg - dossier data.

Sources: web-verified August 31, 2026 - Wikipedia (main biography plus the Starrcade 1998 and
Survivor Series 2016 event pages), Bleacher Report's report on the July 12, 2025 retirement
match and Sports Illustrated on the injury he took in it. Every match row carries a
day-precision date from those sources or the canonical, multiply-documented date of a major
card.

Deliberate omissions:
  * The streak is published as what it was: a billed 173-0, announced as 174-0 at Starrcade
    1998, with the real count acknowledged as lower and no substitute figure invented.
  * No career win-loss total beyond that framing.
  * WCW World Tag Team reign with Bret Hart is dated to the month only; the day was not
    verified in this pass.
"""

# ----------------------------------------------------------------- record rows
# Sixteen documented bouts - the debut, the streak's peaks and its taser-assisted end, both
# WWE runs, and the July 2025 retirement match against Gunther.
ROWS = [
    dict(result="W", date="1997-09-22", promo="WCW", landmark=True,
         event="Monday Nitro", opponent="Hugh Morrus",
         stip="Singles — televised debut; the streak begins", title=""),
    dict(result="W", date="1998-04-20", promo="WCW",
         event="Monday Nitro", opponent="Raven",
         stip="Raven's Rules — first championship", title="WCW United States Championship"),
    dict(result="W", date="1998-07-06", promo="WCW", landmark=True,
         event="Monday Nitro — Georgia Dome", opponent="Hollywood Hogan", opponent_html=True,
         stip="Singles — the title win, before 40,000-plus, on free TV", title="WCW World Heavyweight Championship"),
    dict(result="W", date="1998-10-25", promo="WCW", landmark=True,
         event="Halloween Havoc — Las Vegas", opponent="Diamond Dallas Page",
         stip="Singles — the streak's best match", title="WCW World Heavyweight Championship"),
    dict(result="L", date="1998-12-27", promo="WCW", landmark=True,
         event="Starrcade — Washington, D.C.", opponent="Kevin Nash",
         stip="Singles — Scott Hall's taser ends the streak at a billed 173-0", title="WCW World Heavyweight Championship"),
    dict(result="W", date="2003-09-21", promo="WWE", landmark=True,
         event="Unforgiven", opponent="Triple H",
         stip="Title vs career — his first WWE championship", title="World Heavyweight Championship"),
    dict(result="W", date="2004-03-14", promo="WWE", landmark=True,
         event="WrestleMania XX — Madison Square Garden", opponent="Brock Lesnar",
         stip="Singles — Steve Austin as referee; both men leaving, and the Garden knew it", title=""),
    dict(result="W", date="2016-11-20", promo="WWE", landmark=True,
         event="Survivor Series — Toronto", opponent="Brock Lesnar",
         stip="Singles — 1 minute 26 seconds, twelve years after his last match", title=""),
    dict(result="W", date="2017-03-05", promo="WWE",
         event="Fastlane", opponent="Kevin Owens",
         stip="Singles — the title in 22 seconds", title="WWE Universal Championship"),
    dict(result="L", date="2017-04-02", promo="WWE", landmark=True,
         event="WrestleMania 33 — Orlando", opponent="Brock Lesnar",
         stip="Singles — the trilogy ends; the reign ends at 28 days", title="WWE Universal Championship"),
    dict(result="W", date="2020-02-27", promo="WWE",
         event="Super ShowDown — Riyadh", opponent="&ldquo;The Fiend&rdquo; Bray Wyatt",
         stip="Singles — second Universal Championship, at 53", title="WWE Universal Championship"),
    dict(result="L", date="2020-04-04", promo="WWE",
         event="WrestleMania 36 Night 1", opponent="Braun Strowman",
         stip="Singles — the no-crowd WrestleMania", title="WWE Universal Championship"),
    dict(result="L", date="2021-08-21", promo="WWE",
         event="SummerSlam — Las Vegas", opponent="Bobby Lashley",
         stip="Singles — stopped when his knee gave out", title="WWE Championship"),
    dict(result="W", date="2021-10-21", promo="WWE",
         event="Crown Jewel — Riyadh", opponent="Bobby Lashley",
         stip="No Holds Barred — the receipt", title=""),
    dict(result="L", date="2022-02-19", promo="WWE",
         event="Elimination Chamber — Jeddah", opponent="Roman Reigns",
         stip="Singles — challenge", title="WWE Universal Championship"),
    dict(result="L", date="2025-07-12", promo="WWE", landmark=True,
         event="Saturday Night's Main Event XL — Atlanta", opponent="Gunther",
         stip="His retirement match, at 58 — out by technical submission", title="World Heavyweight Championship"),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Hollywood Hogan": "hulk-hogan"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="goldberg",
    name="Goldberg",
    realname="William Scott Goldberg",
    epithet="Who's Next?",
    hook="Record & Titles",

    meta_desc=("Goldberg rode a billed 173-0 streak to the WCW World Championship, won four world "
               "titles across WCW and WWE, and retired July 12, 2025 against Gunther at 58. Full "
               "record, the streak examined, titles and career."),
    og_desc=("Who's Next: the billed 173-0 streak, the Georgia Dome title win over Hollywood "
             "Hogan on free TV, 1:26 over Brock Lesnar twelve years later, and a retirement "
             "match against Gunther in July 2025 that ended with a broken hand and a cut-short "
             "goodbye."),
    tw_desc="Goldberg: the 173-0 streak (as billed), four world titles, retired July 2025.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1997",
    height_imp="6&#8242;4&#8243;",
    weight_lb="285",
    world_titles="4",
    vitals_tagline="Who's next?",
    support_note="Merch &middot; Games &middot; Listen",
    sp_items=[
        dict(ic="GB", title="WWE Shop", sub="Official merchandise · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable legend across the 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="WWE", title="Superstar Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/goldberg"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Da Man &middot; The Streak &middot; Spear, Jackhammer, next",
    hero_tag="Tulsa, Oklahoma &middot; <em>NFL &middot; WCW &middot; WWE &middot; 1997&ndash;2025</em>",
    now_label="NOW",
    now_bold="Retired &mdash; last match July 12, 2025",
    now_tail=" &middot; lost a World Heavyweight Championship challenge to Gunther at Saturday "
             "Night's Main Event in Atlanta at 58, broke his hand in the match, and had the "
             "farewell speech cut short by the broadcast clock",
    hstats=[
        dict(value="173", x=True,  label="The Billed Streak"),
        dict(value="4",   x=False, label="World Titles"),
        dict(value="1:26", x=False, label="Lesnar, 2016"),
        dict(value="2018", x=False, label="Hall of Fame"),
    ],
    ghost_link="From the Falcons' defensive line to a Georgia Dome title win",
    vlabel="Est. 1997 &middot; Tulsa, Oklahoma",
    mono="GB",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Goldberg</b> is the fastest star ever made. A defensive tackle out of the University "
        "of Georgia who played for the Los Angeles Rams and Atlanta Falcons before injuries ended "
        "the football career, William Scott Goldberg debuted on the September 22, 1997 Nitro "
        "against Hugh Morrus with no entrance music, no story and no name graphic worth reading "
        "&mdash; and inside ten months he was WCW World Heavyweight Champion, taking the title "
        "from Hollywood Hogan in front of 40,000-plus at the Georgia Dome on July 6, 1998, on "
        "free television. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">173</span>'
        '<span class="pull-cap">and 0 &mdash; the billed streak. The real count was lower, and WCW knew it</span></span>'
        "The engine was the streak: win after win, most of them under three minutes, spear, "
        "Jackhammer, &ldquo;Who's next?&rdquo; He won four world championships &mdash; one WCW, "
        "one WWE World Heavyweight, two WWE Universal &mdash; across a career that kept restarting "
        "itself, and he wrestled his retirement match on July 12, 2025, at 58, against Gunther in "
        "his adopted hometown of Atlanta.",

        "About that number: <b>173-0 was a marketing figure, not an audit</b>. WCW padded the "
        "count as it went &mdash; wins were added to the tally that never happened, and the "
        "on-screen total jumped when the booking needed it to; the ring announcer at Starrcade "
        "1998 introduced him as 174-0. Wikipedia states plainly that the actual number of "
        "consecutive wins was significantly lower, and no source agrees on a precise real figure, "
        "so this page does not publish one. What matters is that the billed streak was the "
        "hottest act in the company either way &mdash; and that it ended for real at Starrcade on "
        "December 27, 1998, when Scott Hall jolted him with a taser and Kevin Nash hit the "
        "Jackknife: billed 173-0 became 173-1, and neither the character nor WCW was ever quite "
        "as hot again.",

        "The WWE chapters were shorter and stranger. The 2003-04 run produced a World Heavyweight "
        "Championship win over Triple H at Unforgiven on September 21, 2003, and ended at "
        "WrestleMania XX on March 14, 2004 in the infamous Madison Square Garden match with Brock "
        "Lesnar &mdash; both men known to be leaving, the crowd booing everything except guest "
        "referee Steve Austin, Goldberg winning almost as an afterthought. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">1:26</span>'
        '<span class="pull-cap">to beat Brock Lesnar at Survivor Series 2016, twelve years after his previous match</span></span>'
        "Then the return nobody priced correctly: at Survivor Series in Toronto on November 20, "
        "2016, aged 49 and twelve years retired, he squashed Lesnar in one minute and 26 seconds "
        "&mdash; the most effective comeback match of the modern era. He took the Universal "
        "Championship from Kevin Owens in 22 seconds at Fastlane on March 5, 2017, dropped it to "
        "Lesnar at WrestleMania 33, and won it again at 53 from &ldquo;The Fiend&rdquo; Bray "
        "Wyatt at Super ShowDown in Riyadh on February 27, 2020 &mdash; a change that remains "
        "one of the most argued-over booking calls of its era. Late-career losses to Roman "
        "Reigns and a split with Bobby Lashley wound the clock down.",

        "The ending was orderly, which for him counts as novel. He announced 2025 as the finish, "
        "and WWE staged it at Saturday Night's Main Event XL in Atlanta on July 12, 2025: a "
        "World Heavyweight Championship match against the reigning Gunther, lost by technical "
        "submission in about fifteen minutes &mdash; the second-longest match of his career, per "
        "his own telling. He broke his hand somewhere in it, praised Gunther afterward, and had "
        "his in-ring farewell speech clipped by the broadcast window, which he groused about and "
        "then let go, thanking Triple H for the send-off. A Hall of Famer since 2018, he has "
        "spent retirement where he spent the career's gaps: with cars and his family, on his "
        "CarCast podcast. The record here closes at four world titles, one immortal squash "
        "comeback, and the most profitable unverifiable number in wrestling history.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WCW", "WWE"],
        promo_labels={"WCW": "WCW", "WWE": "WWE"},
        stats=[
            ("173&ndash;0", "The billed streak"),
            ("4",        "World title reigns"),
            ("1:26",     "Lesnar, 2016"),
            ("22s",      "Owens, 2017"),
            ("2018",     "Hall of Fame"),
            ("58",       "Age at final bell"),
        ],
        lead=("Sixteen documented bouts &mdash; the debut, the Georgia Dome, the streak's best "
              "night and its taser-assisted last one, both WWE runs and the Atlanta farewell. A "
              "curated ledger, not a career count &mdash; and deliberately not a streak audit: "
              "the 173-0 was billed, padded and ultimately unverifiable, so this table carries "
              "milestones rather than a running tally. Filter by match type, tap any column "
              "header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the reputation rests on. His art was compression — the canon "
                    "matches are mostly short, and no verifiable Dave Meltzer rating attaches to "
                    "any of them, so none is shown."),
    signature=[
        dict(rating="&mdash;", event="Halloween Havoc 1998 — Las Vegas", opponent="Diamond Dallas Page",
             stip="WCW World title — the streak's one great long match"),
        dict(rating="&mdash;", event="Monday Nitro, July 6, 1998", opponent="Hollywood Hogan",
             stip="WCW World title — the Georgia Dome coronation, given away free"),
        dict(rating="&mdash;", event="Survivor Series 2016 — Toronto", opponent="Brock Lesnar",
             stip="1:26 — the perfect comeback squash"),
        dict(rating="&mdash;", event="Saturday Night's Main Event XL", opponent="Gunther",
             stip="World Heavyweight title — the retirement match, lost standing up"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("1", "WCW World Heavyweight"),
            ("1", "World Heavyweight (WWE)"),
            ("2", "WWE Universal"),
            ("1", "WCW United States"),
        ],
        lead=("Four world championships across two companies, a US title won six months into the "
              "career, and a tag reign with Bret Hart most bios forget. Reign lengths are short "
              "throughout &mdash; the act was the chase, not the defense."),
        rows=[
            dict(ic="C", name="WCW World Heavyweight Championship", count="1",
                 sub="July 6, 1998 &ndash; December 27, 1998 &middot; def. Hollywood Hogan at the "
                     "Georgia Dome on Nitro, lost to Kevin Nash at Starrcade via Scott Hall&rsquo;s "
                     "taser &middot; 174 days, entirely inside the streak"),
            dict(ic="U", name="WCW United States Championship", count="1",
                 sub="Won from Raven on the April 20, 1998 Nitro &mdash; his first championship, "
                     "seven months after debut &mdash; and vacated when he won the World title"),
            dict(ic="W", name="World Heavyweight Championship (WWE)", count="1",
                 sub="September 21, 2003 &ndash; December 14, 2003 &middot; won from Triple H at "
                     "Unforgiven, title vs career; lost in the Armageddon triple threat &middot; "
                     "his July 2025 farewell was a failed challenge for the title&rsquo;s current "
                     "incarnation, not a reign"),
            dict(ic="V", name="WWE Universal Championship", count="2",
                 sub="March 5 &ndash; April 2, 2017 &middot; won from Kevin Owens at Fastlane in 22 "
                     "seconds, lost to Brock Lesnar at WrestleMania 33 &middot; February 27 &ndash; "
                     "April 4, 2020 &middot; won from &ldquo;The Fiend&rdquo; Bray Wyatt at Super "
                     "ShowDown at 53, lost to Braun Strowman at WrestleMania 36"),
            dict(ic="T", name="WCW World Tag Team Championship", count="1",
                 sub="With Bret Hart, December 1999 &middot; the day-precision date was not "
                     "verified in this pass and is not invented"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Alliances",
        lead="The act was engineered to need nobody &mdash; which is why the exceptions are "
             "instructive.",
        cards=[
            dict(era="WCW &middot; 1997&ndash;1998",
                 name="The streak, alone by design",
                 members="Goldberg, and a security escort",
                 desc="No manager, no faction, no promos to speak of — the entrance from the "
                      "locker room flanked by security was the whole presentation. WCW built the "
                      "one act the nWo era could not absorb: a man with no allegiances to "
                      "betray."),
            dict(era="WCW &middot; 1999",
                 name="Goldberg &amp; Bret Hart",
                 members="Goldberg, Bret Hart",
                 desc="Brief tag champions together in December 1999 amid the company's terminal "
                      "chaos — and permanently linked by darker history: Goldberg's mistimed kick "
                      "at Starrcade 1999 concussed Hart and forced his retirement, a consequence "
                      "both men have discussed with unusual candor since."),
            dict(era="WCW &middot; 2000",
                 name="The New Blood heel turn",
                 members="Goldberg, under Russo-Bischoff booking",
                 desc="The 2000 relaunch turned him heel and aligned him with the New Blood "
                      "faction. Merchandise sales and crowd reactions collapsed; the experiment "
                      "was reversed within months and stands as the canonical proof that some "
                      "acts only work pointed one way."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One gimmick, maintained for 28 years: himself, at maximum velocity. The variations "
             "are eras, not characters.",
        cards=[
            dict(mono="NFL", era="Before &middot; 1990&ndash;1995", name="Bill Goldberg, defensive tackle",
                 desc="University of Georgia, then the Rams and the Atlanta Falcons, with a World "
                      "Bowl II title in the World League. A torn abdomen ended it; powerlifting "
                      "and a WCW Power Plant invitation followed. The football explosiveness — "
                      "the three-point-stance spear — became the entire in-ring language."),
            dict(mono="ST", era="WCW &middot; 1997&ndash;1998", name="The Streak",
                 desc="Debuted September 22, 1997 with no music and barely a name. The squash-win "
                      "conveyor, the security-flanked walk, the pyro snort — inside a year it was "
                      "the biggest babyface act in the company and the only organic star WCW ever "
                      "made."),
            dict(mono="MO", era="WCW &amp; WWE &middot; 1999&ndash;2004", name="The chased man",
                 desc="After Starrcade 1998 the invincibility was gone and the booking never found "
                      "a second gear — the heel turn flopped, the WWE 2003 run peaked at "
                      "Unforgiven and curdled by WrestleMania XX, where the Garden booed two "
                      "departing men out of the building."),
            dict(mono="LG", era="WWE &middot; 2016&ndash;2025", name="The legend in the chute",
                 desc="The 2016-2025 part-timer: 1:26 over Lesnar, 22 seconds over Owens, a "
                      "Universal title at 53, and a retirement match at 58 he lost by technical "
                      "submission, on his feet, to Gunther — the version of the act that finally "
                      "got to end on purpose."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="The Power Plant to the Georgia Dome in ten months; everything after was epilogue "
             "management.",
        rows=[
            dict(year="1995", title="Football ends",
                 desc="A torn abdominal muscle finishes the NFL career after stints with the Rams "
                      "and Falcons; he drifts into powerlifting and the WCW Power Plant."),
            dict(year="1997", title="Debut, and the streak begins",
                 desc="Beats Hugh Morrus on the September 22 Nitro, unannounced. The wins stack "
                      "up in squash after squash."),
            dict(year="1998", title="US title, World title, 40,000 people",
                 desc="Takes the US title from Raven on April 20 and the WCW World Heavyweight "
                      "Championship from Hollywood Hogan at the Georgia Dome on July 6, on free "
                      "TV. Beats DDP in the streak's best match at Halloween Havoc on October "
                      "25. On December 27, Scott Hall's taser and Kevin Nash's Jackknife end the "
                      "billed 173-0 at Starrcade."),
            dict(year="1999", title="The Hart kick",
                 desc="A mistimed thrust kick at Starrcade concusses Bret Hart, ending Hart's "
                      "career; they had been tag champions together weeks earlier. The two later "
                      "reconciled publicly."),
            dict(year="2000", title="The heel turn that wasn't",
                 desc="The New Blood angle turns him heel; the audience declines to cooperate, "
                      "and the turn is reversed. An arm injury from a limousine-window stunt "
                      "costs him months."),
            dict(year="2003", title="WWE, round one",
                 desc="Debuts the night after WrestleMania XIX, wins the World Heavyweight "
                      "Championship from Triple H at Unforgiven on September 21, loses it in the "
                      "December Armageddon triple threat."),
            dict(year="2004", title="The Garden turns on everyone",
                 desc="Beats Brock Lesnar at WrestleMania XX on March 14 with Steve Austin "
                      "refereeing, both men leaving and the crowd jeering the whole thing. He is "
                      "gone for twelve years."),
            dict(year="2016", title="1:26",
                 desc="Returns at 49 and squashes Lesnar at Survivor Series in Toronto on "
                      "November 20 in one minute, 26 seconds — the comeback as thunderclap."),
            dict(year="2017", title="Universal Champion, then WrestleMania",
                 desc="Wins the Universal title from Kevin Owens in 22 seconds at Fastlane on "
                      "March 5; Lesnar takes it at WrestleMania 33 on April 2. Hall of Fame "
                      "induction follows in 2018."),
            dict(year="2020", title="Champion again at 53",
                 desc="Beats 'The Fiend' Bray Wyatt at Super ShowDown in Riyadh on February 27 "
                      "for a second Universal Championship — among the most disputed booking "
                      "decisions of the era — and drops it to Braun Strowman at the crowdless "
                      "WrestleMania 36."),
            dict(year="2022", title="The Reigns match",
                 desc="Loses the Universal Championship challenge to Roman Reigns at Elimination "
                      "Chamber in Jeddah on February 19 — the last match before the long runway "
                      "to retirement."),
            dict(year="2025", title="The retirement match",
                 desc="July 12, Saturday Night's Main Event XL in Atlanta: loses a World "
                      "Heavyweight Championship match to Gunther by technical submission at 58, "
                      "breaking his hand along the way. The farewell speech is cut short by the "
                      "broadcast window; he thanks Triple H anyway."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Hollywood Hogan", slug="hulk-hogan",
                 desc="One match that mattered more than most rivalries: July 6, 1998, Nitro at "
                      "the Georgia Dome, Hogan putting the twenty-month rookie over clean in "
                      "front of 40,000-plus for the WCW World Heavyweight Championship. WCW gave "
                      "away its biggest possible pay-per-view main event on free television and "
                      "got its biggest pop of the war for it."),
            dict(name="Diamond Dallas Page",
                 desc="Halloween Havoc, October 25, 1998 — the one streak match built as an "
                      "actual contest, against the company's other self-made star. Widely "
                      "considered the best match of his career and proof the act could go ten "
                      "hard minutes when the dance partner was right."),
            dict(name="Kevin Nash",
                 desc="The man on the other end of the streak's end at Starrcade, December 27, "
                      "1998 — with Scott Hall's taser doing the arguing. The finish is the "
                      "textbook case study in cashing out an unbeaten run: the number stopped "
                      "mattering, and so, gradually, did the character."),
            dict(name="Brock Lesnar",
                 desc="A trilogy with a twelve-year intermission: the booed WrestleMania XX "
                      "match of March 14, 2004 between two departing men, the 1:26 demolition at "
                      "Survivor Series 2016 that redeemed it, and the WrestleMania 33 decider "
                      "Lesnar won on April 2, 2017 — the rare Goldberg program with a real arc."),
            dict(name="&ldquo;The Fiend&rdquo; Bray Wyatt",
                 desc="Super ShowDown in Riyadh, February 27, 2020: Goldberg, 53, took the "
                      "Universal Championship from the hottest character act in the company. The "
                      "backlash was immediate and durable — it remains the win argued about most "
                      "in his ledger, cited whenever part-time legends beat full-time acts."),
            dict(name="Gunther",
                 desc="The ending: Saturday Night's Main Event XL in Atlanta, July 12, 2025, a "
                      "World Heavyweight Championship match Gunther won by putting him to sleep "
                      "in the middle of the ring. Goldberg called Gunther unbelievable "
                      "afterward; Gunther stayed backstage nearly an hour to talk with his "
                      "family. Losses do not come more respectful."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; After",
        lead="A modest media career for a man whose entrance was the best television WCW ever "
             "produced. Verified entries only.",
        rows=[
            dict(when="1999", title="Universal Soldier: The Return", kind="Film",
                 desc="The first film role of the action-movie sideline that followed the WCW "
                      "peak."),
            dict(when="2005", title="Santa's Slay &amp; The Longest Yard", kind="Film",
                 desc="The homicidal-Santa cult comedy and the Adam Sandler remake's prison "
                      "yard — the two roles people actually remember."),
            dict(when="2013&ndash;", title="CarCast", kind="Podcast",
                 desc="The automotive podcast where, in July 2025, he disclosed the broken hand "
                      "from the Gunther match — his main public channel in retirement, "
                      "reflecting a garage habit as documented as the career."),
            dict(when="2016&ndash;", title="WWE 2K series", kind="Game",
                 desc="Cover star of WWE 2K17 and a playable legend since — the comeback was "
                      "literally announced through a video-game marketing campaign."),
            dict(when="2018", title="WWE Hall of Fame", kind="Honor",
                 desc="Headlined the class of 2018, inducted by Paul Heyman."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, with the billed and the real kept separate &mdash; which, for this "
             "career, is the whole job.",
        stats=[
            ("173&ndash;1", "The streak, as billed"),
            ("4",       "World title reigns"),
            ("1:26",    "The Lesnar squash"),
        ],
        rows=[
            dict(name="The streak: billed 173-0, announced 174-0, really something lower",
                 sub="WCW inflated the running total on screen as the angle demanded — Wikipedia "
                     "notes the actual count of consecutive wins was significantly lower, and the "
                     "Starrcade ring introduction said 174-0 the night it ended. No corrected "
                     "figure is published here because no reliable one exists. As a piece of "
                     "booking, the padding worked; as arithmetic, it never happened."),
            dict(name="WCW World Heavyweight Champion ten months after his debut",
                 sub="September 22, 1997 debut; July 6, 1998 title win over Hollywood Hogan at "
                     "the Georgia Dome, on free television, before 40,000-plus — the fastest "
                     "ascent to a world title of the television era, and WCW's last great "
                     "self-made act."),
            dict(name="Four world championships across WCW and WWE",
                 sub="WCW World Heavyweight (1998, 174 days), World Heavyweight (2003), and two "
                     "Universal Championships (2017, 2020) — the second won at age 53."),
            dict(name="Beat Brock Lesnar in 1 minute 26 seconds, twelve years after his last match",
                 sub="Survivor Series, Toronto, November 20, 2016 — two spears and a Jackhammer. "
                     "The follow-up at Fastlane took the Universal title from Kevin Owens in 22 "
                     "seconds. No comeback in the modern era has been executed more efficiently."),
            dict(name="A world champion in three different decades",
                 sub="1998, 2003, 2017 and 2020 — the reigns bracket a 22-year span of the "
                     "main-event picture."),
            dict(name="The retirement match, July 12, 2025",
                 sub="Lost to Gunther by technical submission at Saturday Night's Main Event XL "
                     "in Atlanta, at 58 — about fifteen minutes, which he has called the "
                     "second-longest match of his career, wrestled with a hand he broke somewhere "
                     "in it (Sports Illustrated). The farewell speech was cut short by the "
                     "broadcast clock."),
            dict(name="WWE Hall of Fame, class of 2018",
                 sub="Inducted by Paul Heyman, seven years before the final match — one of the "
                     "few men to headline a Hall of Fame class and then wrestle for another "
                     "seven years."),
        ],
        footnote=("The one number this page refuses to publish is a 'real' streak figure: the "
                  "padding is documented, the true count is not, and replacing one unverifiable "
                  "number with another would repeat the original sin. The tag title with Bret "
                  "Hart is dated to December 1999 at month precision for the same reason."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography",
             href="https://en.wikipedia.org/wiki/Goldberg_(wrestler)"),
        dict(k="Bleacher Report", v="The retirement match: Gunther retains in Atlanta",
             href="https://bleacherreport.com/articles/25210696-goldberg-loses-gunther-wwe-saturday-nights-main-event-ahead-retirement"),
        dict(k="Sports Illustrated", v="He broke his hand in the retirement match",
             href="https://www.si.com/fannation/wrestling/wwe/goldberg-reveals-he-suffered-major-injury-during-retirement-match-at-wwe-saturday-nights-main-event"),
        dict(k="Wikipedia", v="Starrcade 1998 — the streak ends by taser",
             href="https://en.wikipedia.org/wiki/Starrcade_(1998)"),
        dict(k="Wikipedia", v="Survivor Series 2016 — 1:26 in Toronto",
             href="https://en.wikipedia.org/wiki/Survivor_Series_(2016)"),
        dict(k="WWE.com", v="Superstar profile", href="https://www.wwe.com/superstars/goldberg"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Was Goldberg really 173-0?",
            a="No &mdash; and yes, depending on which ledger you accept. <b>173-0 was the billed "
              "figure</b>: WCW openly padded the on-screen total, adding wins that never took "
              "place when the angle called for a rounder number, and the ring announcer at "
              "Starrcade 1998 introduced him at 174-0. The real count of consecutive wins was "
              "significantly lower, and no reliable corrected figure exists, so this page does "
              "not invent one. The loss, at least, is precise: December 27, 1998, to Kevin Nash, "
              "after Scott Hall's taser.",
            q_ld="Was Goldberg's undefeated streak really 173-0?",
            a_ld="No. The 173-0 streak was a billed figure that WCW inflated on screen, adding "
                 "wins that never occurred, and he was announced as 174-0 at Starrcade 1998. The "
                 "actual number of consecutive wins was significantly lower, though no reliable "
                 "corrected count exists. The streak genuinely ended at Starrcade on December 27, "
                 "1998, when Kevin Nash defeated him after Scott Hall shocked him with a taser."),
        dict(
            q="Did Goldberg&rsquo;s retirement match actually happen?",
            a="Yes. After announcing 2025 as the end, he wrestled his final match on <b>July 12, "
              "2025</b> at Saturday Night's Main Event XL in Atlanta &mdash; a World Heavyweight "
              "Championship challenge to Gunther, lost by technical submission when he faded in "
              "a sleeper in the middle of the ring, at 58. It ran about fifteen minutes, the "
              "second-longest match of his career by his own account; he broke his hand during "
              "it, and his in-ring farewell speech was cut short by the broadcast window, for "
              "which he later thanked Triple H anyway. He has stayed retired since.",
            q_ld="Did Goldberg's retirement match take place, and what happened?",
            a_ld="Yes. Goldberg wrestled his retirement match on July 12, 2025 at WWE Saturday "
                 "Night's Main Event XL in Atlanta, challenging Gunther for the World Heavyweight "
                 "Championship at age 58. Gunther won by technical submission with a sleeper "
                 "hold. The match lasted about fifteen minutes, Goldberg broke his hand during "
                 "it, and his farewell speech was cut short due to broadcast time constraints. "
                 "He has remained retired since."),
        dict(
            q="How many world titles did Goldberg win?",
            a="Four: the WCW World Heavyweight Championship (July 6 to December 27, 1998, won "
              "from Hollywood Hogan at the Georgia Dome), WWE's World Heavyweight Championship "
              "(September to December 2003, won from Triple H at Unforgiven), and two Universal "
              "Championships &mdash; the 2017 reign won from Kevin Owens in 22 seconds and lost "
              "to Brock Lesnar at WrestleMania 33, and the 2020 reign won from &ldquo;The "
              "Fiend&rdquo; at 53 and lost to Braun Strowman at WrestleMania 36.",
            q_ld="How many world championships did Goldberg win?",
            a_ld="Goldberg won four world championships: the WCW World Heavyweight Championship "
                 "in 1998, WWE's World Heavyweight Championship in 2003, and the WWE Universal "
                 "Championship twice, in 2017 and 2020. His first came from Hollywood Hogan at "
                 "the Georgia Dome on July 6, 1998, and his last from Bray Wyatt at Super "
                 "ShowDown on February 27, 2020, when he was 53."),
        dict(
            q="Why is the Survivor Series 2016 match such a big deal?",
            a="Because it should not have worked and instead became the model. Goldberg was 49 "
              "and had not wrestled since the booed WrestleMania XX match twelve years earlier; "
              "Lesnar was the most protected monster in the company. On November 20, 2016 in "
              "Toronto, Goldberg won in <b>1 minute 26 seconds</b> &mdash; two spears, a "
              "Jackhammer &mdash; and the crowd treated it as a miracle rather than a robbery. "
              "It rehabilitated his legacy, set up the Fastlane and WrestleMania 33 title "
              "matches, and remains the reference point for how to book a returning legend "
              "without exposing him.",
            q_ld="Why is Goldberg's Survivor Series 2016 match against Brock Lesnar significant?",
            a_ld="At Survivor Series on November 20, 2016 in Toronto, Goldberg defeated Brock "
                 "Lesnar in 1 minute and 26 seconds with two spears and a Jackhammer, in his "
                 "first match in twelve years, at age 49. The result redeemed their poorly "
                 "received WrestleMania XX match of 2004, led to Goldberg winning the Universal "
                 "Championship at Fastlane in March 2017, and is widely cited as the model for "
                 "booking a returning legend."),
        dict(
            q="What happened between Goldberg and Bret Hart?",
            a="The worst accident of his career. At Starrcade on December 19, 1999 &mdash; weeks "
              "after the two had held the WCW tag titles together &mdash; a mistimed thrust "
              "kick concussed Hart, and post-concussion syndrome forced Hart's retirement. "
              "Goldberg has called it his greatest regret; Hart was publicly bitter for years "
              "and the two later reconciled, with Hart even appearing at his 2018 Hall of Fame "
              "induction year. It is the counterweight every honest account of the stiff, "
              "high-impact style has to carry.",
            q_ld="What happened between Goldberg and Bret Hart?",
            a_ld="At WCW's Starrcade in December 1999, a mistimed thrust kick from Goldberg "
                 "concussed Bret Hart during their match, shortly after the two had been WCW "
                 "World Tag Team Champions together. The resulting post-concussion syndrome "
                 "ended Hart's in-ring career. Goldberg has repeatedly called it his greatest "
                 "regret, and the two men later reconciled publicly."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="William Scott Goldberg"),
        dict(label="Born", value="December 27, 1966", sub="Tulsa, Oklahoma &middot; age 59"),
        dict(label="Billed from", value="Atlanta, Georgia",
             sub="the adopted hometown &mdash; site of the Georgia Dome win and the farewell"),
        dict(label="Height", value="6&#8242;4&#8243;", sub="193 cm"),
        dict(label="Weight", value="285 lb", sub="129 kg (billed)"),
        dict(label="Debut", value="September 22, 1997", sub="Monday Nitro, vs Hugh Morrus"),
        dict(label="Trained at", value="The WCW Power Plant"),
        dict(label="Before wrestling", value="NFL defensive tackle",
             sub="Georgia Bulldogs &middot; Rams &middot; Falcons &middot; World Bowl II champion, 1992"),
        dict(label="Last match", value="July 12, 2025",
             sub="Saturday Night&rsquo;s Main Event XL, Atlanta &mdash; lost to Gunther at 58"),
        dict(label="Signature", value="Spear &middot; Jackhammer",
             sub="two moves, which was the point"),
        dict(label="Catchphrase", value="Who&rsquo;s next?"),
        dict(label="Hall of Fame", value="2018", sub="inducted by Paul Heyman"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1966-12-27",
    bornplace="Tulsa, Oklahoma",
    nationality="United States",
    height_cm=193,
    weight_kg=129,
    ld=dict(
        alternateName=["William Scott Goldberg", "Bill Goldberg", "Da Man"],
        award=["WCW World Heavyweight Championship (1 reign, 174 days, 1998)",
               "World Heavyweight Championship (1 reign, 2003)",
               "WWE Universal Championship (2 reigns, 2017 and 2020)",
               "WCW United States Championship (1 reign, 1998)",
               "WCW World Tag Team Championship (1 reign, with Bret Hart, 1999)",
               "WWE Hall of Fame (2018)"],
        knowsAbout=["Professional wrestling", "WCW", "WWE", "The Streak", "NFL football",
                    "Monday Nitro"],
        description="Goldberg, born William Scott Goldberg in Tulsa, Oklahoma, is an American "
                    "retired professional wrestler and former NFL defensive tackle. Riding a "
                    "billed 173-0 undefeated streak, he won the WCW World Heavyweight "
                    "Championship from Hollywood Hogan at the Georgia Dome on July 6, 1998, ten "
                    "months after his debut. He won four world championships across WCW and WWE, "
                    "beat Brock Lesnar in 1 minute 26 seconds at Survivor Series 2016 after a "
                    "twelve-year absence, was inducted into the WWE Hall of Fame in 2018, and "
                    "wrestled his retirement match on July 12, 2025, losing to Gunther at "
                    "Saturday Night's Main Event in Atlanta at age 58.",
        sameAs=["https://en.wikipedia.org/wiki/Goldberg_(wrestler)",
                "https://www.wwe.com/superstars/goldberg"],
    ),
)
