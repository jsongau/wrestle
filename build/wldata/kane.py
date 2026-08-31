# -*- coding: utf-8 -*-
"""Kane - dossier data.

Sources: web-verified August 31, 2026 - Wikipedia (Kane (wrestler); 2026 Knox County,
Tennessee mayoral election), WVLT Knoxville (August 2026 election results), ITR Wrestling's
Kane biography, and Wrestling Inc (2021 Royal Rumble payout donation). Record-row dates are
day-precision and verified.

Deliberate omissions:
  * No career win-loss total - none is reliably published, so none is invented.
  * No theme entry - the fire and organ are famous, but no Spotify track URL was verified
    in this pass, so the block is omitted per house rule.
  * One source (ITR) dates his mayoralty from May 1, 2018; that is the primary-win date
    area, not the swearing-in. He won the general election in August 2018 and took office
    that September, and this page uses the latter framing.
  * The individual dates of all twelve tag team championship reigns were not re-verified
    and are summarized rather than enumerated.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="1997-11-09", promo="WWE", landmark=True,
         event="Survivor Series — Montreal", opponent="Mankind",
         stip="Singles — first match as Kane, five weeks after the Badd Blood debut", title=""),
    dict(result="L", date="1998-03-29", promo="WWE", landmark=True,
         event="WrestleMania XIV — Boston", opponent="The Undertaker", opponent_html=True,
         stip="Singles — takes three Tombstones; sits up anyway", title=""),
    dict(result="L", date="1998-04-26", promo="WWE",
         event="Unforgiven — Greensboro", opponent="The Undertaker", opponent_html=True,
         stip="The first Inferno match — loses when his arm catches fire", title=""),
    dict(result="W", date="1998-06-28", promo="WWE", landmark=True,
         event="King of the Ring — Pittsburgh", opponent="Stone Cold Steve Austin", opponent_html=True,
         stip="First Blood match — wins the WWF Championship", title="WWF Championship"),
    dict(result="L", date="1998-06-29", promo="WWE", landmark=True,
         event="Raw — Cleveland", opponent="Stone Cold Steve Austin", opponent_html=True,
         stip="Singles — the title goes back after roughly 24 hours", title="WWF Championship"),
    dict(result="W", date="2001-05-20", promo="WWE",
         event="Judgment Day", opponent="Triple H",
         stip="Chain match — second Intercontinental reign", title="WWF Intercontinental Championship"),
    dict(result="L", date="2003-06-23", promo="WWE", landmark=True,
         event="Raw — Madison Square Garden", opponent="Triple H",
         stip="Title vs. mask — loses, and unmasks after six years", title=""),
    dict(result="L", date="2004-03-14", promo="WWE",
         event="WrestleMania XX — Madison Square Garden", opponent="The Undertaker", opponent_html=True,
         stip="Singles — the Deadman returns; the brothers' last Mania match", title=""),
    dict(result="W", date="2008-03-30", promo="WWE", landmark=True,
         event="WrestleMania XXIV — Orlando", opponent="Chavo Guerrero",
         stip="Singles — wins in 11 seconds, an all-time Mania record", title="ECW Championship"),
    dict(result="W", date="2010-07-18", promo="WWE", landmark=True,
         event="Money in the Bank — Kansas City", opponent="Rey Mysterio",
         stip="Cash-in the same night he won the briefcase — first world title in 12 years",
         title="World Heavyweight Championship"),
    dict(result="W", date="2012-09-16", promo="WWE", type="tag",
         event="Night of Champions — Boston", opponent="Kofi Kingston & R-Truth",
         stip="Team Hell No, with Daniel Bryan — tag titles held 245 days",
         title="WWE Tag Team Championship"),
    dict(result="L", date="2018-11-02", promo="WWE", type="tag",
         event="Crown Jewel — Riyadh", opponent="D-Generation X",
         stip="Brothers of Destruction vs. Michaels & Triple H — a sitting mayor in the match", title=""),
    dict(result="L", date="2021-01-31", promo="WWE", landmark=True, type="tag",
         event="Royal Rumble match — St. Petersburg", opponent="The 2021 Royal Rumble field",
         stip="Enters No. 18, eliminates two, out to Damian Priest — his last match; "
              "donated the payday to a scholarship fund", title=""),
]

for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"The Undertaker": "the-undertaker",
                 "Stone Cold Steve Austin": "stone-cold-steve-austin"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="kane",
    name="Kane",
    realname="Glenn Thomas Jacobs",
    epithet="The Big Red Machine",
    hook="Record & Titles",

    meta_desc=("Kane won the WWF, ECW and World Heavyweight Championships, twelve tag team "
               "titles, and then two terms as Mayor of Knox County, Tennessee - an office his "
               "term limits end in September 2026. Full record and titles."),
    og_desc=("The Big Red Machine: a Hell in a Cell debut, a 24-hour WWF title reign, three "
             "world championships across three belts, and eight years as an elected mayor."),
    tw_desc="3 world titles, 12 tag reigns, 1 mask, 2 terms as Knox County mayor.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1992",
    height_imp="7&#8242;0&#8243;",
    weight_lb="323",
    world_titles="3",
    vitals_tagline="The devil's favorite demon",
    support_note="Merch &middot; Games &middot; Civic",
    sp_items=[
        dict(ic="KN", title="WWE Shop", sub="Official Kane merch · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable legend in the 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="KC", title="Knox County Mayor's Office", sub="The other career, 2018-2026",
             tag="Visit", href="https://knoxcounty.org/mayor/"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/kane"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Big Red Machine &middot; The Devil's Favorite Demon &middot; Mayor Glenn Jacobs",
    hero_tag="Knoxville, Tennessee &middot; <em>SMW &middot; USWA &middot; WWF/WWE &middot; 1992&ndash;2021 &middot; City-County Building &middot; 2018&ndash;2026</em>",
    now_label="NOW",
    now_bold="Mayor of Knox County, Tennessee &mdash; in his final days in office",
    now_tail=" &middot; term-limited after two terms; Betsy Henderson won the August 6, 2026 "
             "election to succeed him, and his second term ends at the start of September 2026",
    hstats=[
        dict(value="3",  x=True,  label="World Titles"),
        dict(value="12", x=True,  label="Tag Team Reigns"),
        dict(value="2",  x=True,  label="Terms as Mayor"),
        dict(value="1",  x=False, label="Day First Title Reign"),
    ],
    ghost_link="From ripping the door off the first Cell to eight years of county budgets",
    vlabel="Est. 1992 &middot; billed from Hell",
    mono="KN",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Kane</b> is the most durable monster character wrestling has produced and the only "
        "WWE world champion to be elected to major public office. Glenn Jacobs played The "
        "Undertaker&rsquo;s scarred half-brother from 1997 to 2021 &mdash; masked, unmasked, "
        "re-masked &mdash; and won a world championship under three different belts: the WWF "
        "Championship from Steve Austin in a First Blood match at King of the Ring on June 28, "
        "1998, the ECW Championship in eleven seconds at WrestleMania XXIV on March 30, 2008, "
        "and the World Heavyweight Championship on July 18, 2010, cashing in the Money in the "
        "Bank briefcase he had won earlier the same night. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">12</span>'
        '<span class="pull-cap">tag team championship reigns with seven different partners, his brother included</span></span>'
        "Around the singles gold sit twelve "
        "tag team reigns with seven partners &mdash; Mankind, X-Pac, The Undertaker, The "
        "Hurricane, Big Show, Rob Van Dam and Daniel Bryan &mdash; the last of them the Team "
        "Hell No run of 2012&ndash;13 that turned an anger-management skit into a 245-day "
        "title reign.",

        "One correction to the standard telling: his debut was not a match. At Badd Blood on "
        "October 5, 1997, Kane arrived mid&ndash;Hell in a Cell, tore the door off the "
        "structure, Tombstoned The Undertaker and cost him the match against Shawn Michaels "
        "&mdash; but he was an interference, not a participant. His first <b>match</b> came "
        "five weeks later, beating Mankind at Survivor Series in Montreal on November 9, 1997 "
        "&mdash; the same night as the Screwjob, which is why almost nobody remembers it. The "
        "other half-remembered fact is his first title reign&rsquo;s length: he won the WWF "
        "Championship on June 28, 1998 and lost it back to Austin on Raw the following night "
        "&mdash; roughly 24 hours, one of the shortest world reigns ever, and twelve years "
        "passed before the 2010 cash-in gave him a second.",

        "The character&rsquo;s history bends around the mask. Six years masked and mute-ish, "
        "then the title-versus-mask loss to Triple H on the June 23, 2003 Raw in Madison "
        "Square Garden that unmasked him into his most violent era &mdash; the era of "
        "tombstoning officials and setting commentators on fire &mdash; then the surprise "
        "re-masking in December 2011. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">11</span>'
        '<span class="pull-cap">seconds to win the ECW Championship at WrestleMania XXIV &mdash; still a WrestleMania record</span></span>'
        "Through every iteration he was the company&rsquo;s "
        "load-bearing wall: by most counts its all-time pay-per-view appearance leader, "
        "always available, always credible, never quite the top guy. The Undertaker pairing "
        "&mdash; enemies at WrestleManias XIV and XX, partners as the Brothers of Destruction "
        "&mdash; ran, on and off, for twenty-one years, closing with a tag loss to "
        "D-Generation X at Crown Jewel on November 2, 2018, by which time Jacobs was already "
        "a sitting mayor.",

        "Because that is the third act: Glenn Jacobs, libertarian-leaning Republican, was "
        "elected Mayor of Knox County, Tennessee in August 2018, took office that September, "
        "and was re-elected in August 2022. He wrestled twice while in office &mdash; Crown "
        "Jewel 2018 and the 2021 Royal Rumble on January 31, 2021, his final match, entering "
        "at No. 18, eliminating Ricochet and Dolph Ziggler, going out to Damian Priest, and "
        "donating the payday to a technical-college scholarship fund (Wrestling Inc). He was "
        "inducted into the Hall of Fame in 2021 while in office. Knox County limits mayors "
        "to two terms, so the 2026 race ran without him: Betsy Henderson won the general "
        "election on August 6, 2026 (WVLT), and as of this page&rsquo;s writing &mdash; the "
        "end of August 2026 &mdash; Jacobs is serving his final days, having discussed but "
        "not announced what comes next. No WWE return is scheduled; a retirement-match "
        "rumor cycle in 2025&ndash;26 produced nothing bookable.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWF/WWE"},
        stats=[
            ("1&times;", "WWF Championship"),
            ("1&times;", "ECW Championship"),
            ("1&times;", "World Heavyweight"),
            ("12&times;", "Tag team reigns"),
            ("2&times;", "Intercontinental"),
            ("2021",     "Hall of Fame"),
        ],
        lead=("Thirteen documented bouts &mdash; the real debut, all three world title wins, the "
              "24-hour reign's loss, the unmasking, and the Royal Rumble farewell of a sitting "
              "mayor. A curated ledger, not a career count; no career win&ndash;loss total is "
              "published because none is reliably sourced. His pre-Kane WWF runs as Isaac "
              "Yankem and the fake Diesel are summarized in Personas below. Filter by match "
              "type, tap any column header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the reputation rests on - a monster's resume runs on moments "
                    "more than star ratings, and his best-remembered bouts are stipulation "
                    "landmarks. Ratings, where shown, are Observer figures as commonly "
                    "reported."),
    signature=[
        dict(rating="4.0", event="WrestleMania XIV — Boston", opponent="The Undertaker",
             stip="The brothers' first match — three Tombstones to keep him down"),
        dict(rating="3.5", event="King of the Ring 1998 — Pittsburgh", opponent="Stone Cold Steve Austin",
             stip="First Blood — the WWF Championship win"),
        dict(rating="4.0", event="Money in the Bank 2010 — Kansas City", opponent="The SmackDown ladder match field",
             stip="Briefcase and world title in one night"),
        dict(rating="3.5", event="Unforgiven 1998 — Greensboro", opponent="The Undertaker",
             stip="The first Inferno match"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("3",  "World titles, 3 belts"),
            ("12&times;", "Tag team reigns"),
            ("2&times;", "Intercontinental"),
            ("2010", "Money in the Bank"),
        ],
        lead=("Three world championships under three different belts &mdash; a distinction few "
              "share &mdash; plus the busiest tag portfolio of his generation. The twelve tag "
              "reigns are summarized rather than enumerated; their individual dates were not "
              "re-verified in this pass."),
        rows=[
            dict(ic="W", name="WWF Championship", count="1",
                 sub="June 28, 1998, def. Stone Cold Steve Austin in a First Blood match at "
                     "King of the Ring; lost back to Austin on Raw the next night &mdash; a "
                     "reign of roughly 24 hours"),
            dict(ic="E", name="ECW Championship", count="1",
                 sub="March 30, 2008, def. Chavo Guerrero in 11 seconds at WrestleMania XXIV "
                     "&mdash; still the fastest WrestleMania match; lost to Mark Henry at "
                     "Night of Champions that June"),
            dict(ic="H", name="World Heavyweight Championship", count="1",
                 sub="July 18, 2010 &mdash; won the SmackDown Money in the Bank ladder match "
                     "and cashed in on Rey Mysterio the same night; held it into the "
                     "December TLC four-way that Edge won"),
            dict(ic="I", name="WWF/WWE Intercontinental Championship", count="2",
                 sub="Including the chain-match win over Triple H at Judgment Day, May 20, "
                     "2001 &mdash; the reigns that kept the monster credible between world "
                     "title programs"),
            dict(ic="T", name="Tag team championships", count="12",
                 sub="With seven partners &mdash; Mankind, X-Pac, The Undertaker, The "
                     "Hurricane, Big Show, Rob Van Dam and Daniel Bryan &mdash; spanning the "
                     "WWF, World, WCW and WWE tag titles; the Team Hell No reign with Bryan "
                     "ran 245 days across 2012-13"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Every alliance was an odd couple — the monster works best against a foil.",
        cards=[
            dict(era="WWF/WWE &middot; 1997&ndash;2018, intermittently",
                 name="The Brothers of Destruction",
                 members="Kane &amp; The Undertaker",
                 desc="Enemies first — WrestleMania XIV, the first Inferno match, WrestleMania "
                      "XX — and partners repeatedly in between, with tag title reigns "
                      "including a WCW Tag Championship during the Invasion. The double act "
                      "closed at Crown Jewel on November 2, 2018 against D-Generation X. In "
                      "reality Jacobs and Mark Calaway are close friends and unrelated."),
            dict(era="WWE &middot; 2012&ndash;2013",
                 name="Team Hell No",
                 members="Kane &amp; Daniel Bryan, with Dr. Shelby",
                 desc="The anger-management storyline that accidentally produced the best "
                      "comedy of the era and a legitimate 245-day WWE Tag Team Championship "
                      "reign, won at Night of Champions on September 16, 2012 and lost to "
                      "The Shield in May 2013. Hug it out."),
            dict(era="WWE &middot; 2013&ndash;2015",
                 name="The Authority's Director of Operations",
                 members="Corporate Kane, in a suit",
                 desc="The late-career reinvention: the demon in business attire, enforcing "
                      "for Triple H and Stephanie McMahon while occasionally reverting to "
                      "the mask mid-show. In hindsight, a dress rehearsal for actual "
                      "public administration."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Wrestling's best case study in gimmick salvage: three failed characters, then "
             "one that lasted 24 years &mdash; <b>Unabomb</b> &rarr; <b>Isaac Yankem, DDS</b> "
             "&rarr; <b>the fake Diesel</b> &rarr; <b>Kane</b> &rarr; <b>Mayor Glenn Jacobs</b>.",
        cards=[
            dict(mono="UB", era="Smoky Mountain &middot; 1993&ndash;1995", name="Unabomb",
                 desc="The pre-WWF monster run in Jim Cornette's territory, including tag "
                      "success with Al Snow — where the size finally met competent booking."),
            dict(mono="DDS", era="WWF &middot; 1995&ndash;1996", name="Isaac Yankem, DDS",
                 desc="Jerry Lawler's evil dentist, introduced to feud with Bret Hart. As "
                      "bad as it sounds; Jacobs played it gamely and survived it, which "
                      "was the real audition."),
            dict(mono="FD", era="WWF &middot; 1996", name="The fake Diesel",
                 desc="Wheeled out as an ersatz Kevin Nash after Nash left for WCW. The "
                      "second dead-end gimmick in two years — and the reason the Kane "
                      "reveal needed a mask."),
            dict(mono="KN", era="WWF/WWE &middot; 1997&ndash;2021", name="Kane",
                 desc="The Undertaker's burned, presumed-dead half-brother, built through "
                      "months of Paul Bearer promos before the Badd Blood door-rip. Masked "
                      "until June 2003, unmasked and nastier after, re-masked from December "
                      "2011. The rare monster gimmick that aged into an institution."),
            dict(mono="GJ", era="Tennessee &middot; 2018&ndash;2026", name="Mayor Glenn Jacobs",
                 desc="Two-term Republican Mayor of Knox County — elected August 2018, "
                      "re-elected August 2022, term-limited out with his tenure ending at "
                      "the start of September 2026. Wrestled twice while in office and "
                      "donated the 2021 Rumble payday to a scholarship fund."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Three dead gimmicks to a 24-year monster to a county executive.",
        rows=[
            dict(year="1992", title="Debut",
                 desc="Breaks in on the independents after college basketball and football; "
                      "Smoky Mountain and USWA runs follow."),
            dict(year="1995", title="First WWF run, wrong gimmicks",
                 desc="Debuts as Isaac Yankem, DDS against Bret Hart's circle; the fake "
                      "Diesel follows in 1996. Neither works, by design flaws not his."),
            dict(year="1997", title="Kane arrives",
                 desc="Rips the door off the first Hell in a Cell at Badd Blood on October "
                      "5 and Tombstones The Undertaker; first match November 9, beating "
                      "Mankind at Survivor Series."),
            dict(year="1998", title="WWF Champion for a day",
                 desc="Beats Austin in the First Blood match at King of the Ring on June "
                      "28; loses the rematch on Raw the next night. Also survives the "
                      "first Inferno match that April."),
            dict(year="2003", title="Unmasked",
                 desc="Loses title-versus-mask to Triple H on the June 23 Raw and enters "
                      "his most feared era — the Shane McMahon feud, the ring-post fire, "
                      "the Tombstone on an official."),
            dict(year="2008", title="ECW Champion in 11 seconds",
                 desc="Beats Chavo Guerrero at WrestleMania XXIV on March 30 in the "
                      "fastest match in WrestleMania history."),
            dict(year="2010", title="The perfect night",
                 desc="Wins the SmackDown Money in the Bank ladder match on July 18 and "
                      "cashes in on Rey Mysterio hours later — World Heavyweight Champion "
                      "twelve years after his first world title."),
            dict(year="2012", title="Team Hell No",
                 desc="Anger management with Daniel Bryan becomes a 245-day tag title "
                      "reign from September 16, 2012, and the character's warmest year."),
            dict(year="2018", title="Elected mayor",
                 desc="Wins the Knox County mayoralty in August 2018 and takes office in "
                      "September; wrestles Crown Jewel that November as a sitting mayor."),
            dict(year="2021", title="Last match, and the Hall",
                 desc="Enters the Royal Rumble on January 31, 2021 — eliminated by Damian "
                      "Priest, payday donated to a TCAT scholarship fund — and is "
                      "inducted into the Hall of Fame that April."),
            dict(year="2022", title="Re-elected",
                 desc="Wins a second term in August 2022 by a narrower margin than 2018."),
            dict(year="2026", title="Term-limited out",
                 desc="Barred from a third term; Betsy Henderson wins the August 6, 2026 "
                      "election to succeed him, and his tenure ends at the start of "
                      "September 2026 with his next act — politics or otherwise — "
                      "discussed but unannounced."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="The Undertaker", slug="the-undertaker",
                 desc="The reason the character exists: the storyline half-brother he "
                      "debuted by betraying at the first Hell in a Cell on October 5, "
                      "1997. WrestleMania XIV, the first Inferno match, WrestleMania XX, "
                      "Buried Alive matches, and long stretches as tag partners — no "
                      "pairing in company history sustained a story longer, and it ended "
                      "as a team, at Crown Jewel 2018."),
            dict(name="Stone Cold Steve Austin", slug="stone-cold-steve-austin",
                 desc="The 1998 program that gave Kane his only WWF Championship — the "
                      "First Blood win at King of the Ring on June 28, 1998, taken back "
                      "by Austin on Raw a night later. Their summer of stretcher matches "
                      "and swerves kept the monster in the main event through the "
                      "company's hottest year."),
            dict(name="Triple H",
                 desc="Two poles of the career: the chain-match Intercontinental win at "
                      "Judgment Day 2001, and the title-versus-mask Raw match on June 23, "
                      "2003 that stripped the character to its scars and relaunched him "
                      "as an unmasked terror."),
            dict(name="Daniel Bryan",
                 desc="Opponent turned court-ordered tag partner. The Team Hell No run — "
                      "champions for 245 days from September 2012 — proved the monster "
                      "could carry comedy without dying of it, and Bryan has credited "
                      "Jacobs as the best influence of his WWE run."),
            dict(name="Shane McMahon",
                 desc="The 2003 unmasked era's centrepiece — the ring-post fire spot, "
                      "the Last Man Standing and ambulance matches — the stretch that "
                      "made the unmasking stick."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Politics",
        lead="The only entry on this site whose second career involves a budget office.",
        rows=[
            dict(when="2006", title="See No Evil", kind="Film",
                 desc="WWE Studios horror lead as Jacob Goodnight; a 2014 sequel "
                      "followed — the company's most sustained film push for a "
                      "then-active wrestler."),
            dict(when="2018&ndash;2026", title="Mayor of Knox County", kind="Politics",
                 desc="Two terms running Tennessee's third-largest county: elected "
                      "August 2018, re-elected August 2022, term-limited out with his "
                      "tenure ending at the start of September 2026. Betsy Henderson "
                      "won the August 6, 2026 election to succeed him."),
            dict(when="2021", title="WWE Hall of Fame", kind="Honor",
                 desc="Inducted in the class of 2021 — a sitting mayor accepting as a "
                      "fire-summoning demon, a sentence only wrestling produces."),
            dict(when="2019&ndash;", title="Cameo weeks", kind="TV",
                 desc="Occasional one-night WWE returns while in office — including a "
                      "brief 24/7 Championship moment in 2019 — always played for the "
                      "pop, never a program."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records and the singular facts.",
        stats=[
            ("11",  "Seconds — fastest Mania match"),
            ("3",   "Belts worth of world titles"),
            ("2",   "Terms as mayor"),
        ],
        rows=[
            dict(name="Fastest match in WrestleMania history",
                 sub="11 seconds to beat Chavo Guerrero for the ECW Championship at "
                     "WrestleMania XXIV on March 30, 2008 — still unbeaten as of 2026."),
            dict(name="World champion under three different belts",
                 sub="WWF Championship (1998), ECW Championship (2008), World Heavyweight "
                     "Championship (2010) — twelve years between the first and second."),
            dict(name="Same-night Money in the Bank cash-in",
                 sub="July 18, 2010: won the SmackDown ladder match and cashed in on Rey "
                     "Mysterio hours later — the first same-night cash-in at the "
                     "briefcase's own pay-per-view."),
            dict(name="The only WWE world champion elected to major public office",
                 sub="Mayor of Knox County, Tennessee, 2018-2026 — roughly 480,000 "
                     "constituents; he wrestled Crown Jewel 2018 and the 2021 Royal "
                     "Rumble while holding the office."),
            dict(name="Pay-per-view ubiquity",
                 sub="Routinely cited as WWE's all-time leader in pay-per-view "
                     "appearances; WWE has used the claim itself, though no official "
                     "audited count exists, so it is reported here as the consensus "
                     "shorthand it is."),
            dict(name="A 24-hour first world title",
                 sub="June 28-29, 1998 — among the shortest WWF Championship reigns "
                     "ever, and by his own telling his favorite trivia answer."),
        ],
        footnote=("No career win-loss total is published; none is reliably sourced. One "
                  "circulating error is corrected silently throughout: his mayoralty is "
                  "sometimes dated from May 2018 (the primary), but he won the general "
                  "election in August 2018 and took office that September. The twelve "
                  "tag reigns are summarized, not enumerated - their individual dates "
                  "were not re-verified in this pass."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography",
             href="https://en.wikipedia.org/wiki/Kane_(wrestler)"),
        dict(k="Wikipedia", v="2026 Knox County mayoral election — the term-limited exit",
             href="https://en.wikipedia.org/wiki/2026_Knox_County,_Tennessee_mayoral_election"),
        dict(k="WVLT Knoxville", v="August 2026 election results — Henderson wins",
             href="https://www.wvlt.tv/2026/08/07/knox-county-election-results-raise-question-shifting-political-landscape/"),
        dict(k="ITR Wrestling", v="Career biography and title counts",
             href="https://itrwrestling.com/bio/kane/"),
        dict(k="Wrestling Inc", v="2021 Royal Rumble — the donated payday",
             href="https://www.wrestlinginc.com/news/2021/02/kane-to-donate-his-wwe-royal-rumble-pay/"),
        dict(k="WWE.com", v="Official profile",
             href="https://www.wwe.com/superstars/kane"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Kane still the Mayor of Knox County in 2026?",
            a="Barely &mdash; he is in his final days in office. Glenn Jacobs was elected in "
              "August 2018, re-elected in August 2022, and Knox County limits its mayors to "
              "two terms, so he could not run in 2026. Betsy Henderson won the general "
              "election on August 6, 2026 to succeed him, and his tenure ends at the start "
              "of September 2026. He has discussed a political future beyond the "
              "mayoralty without announcing anything specific.",
            q_ld="Is Kane still the Mayor of Knox County, Tennessee in 2026?",
            a_ld="As of late August 2026, Glenn Jacobs is serving the final days of his "
                 "second and last term as Mayor of Knox County, Tennessee. He was elected "
                 "in August 2018 and re-elected in August 2022, and term limits barred him "
                 "from running again. Betsy Henderson won the August 6, 2026 general "
                 "election to succeed him, with the new term beginning at the start of "
                 "September 2026."),
        dict(
            q="When was Kane&rsquo;s last match?",
            a="January 31, 2021 &mdash; the men&rsquo;s Royal Rumble match. He entered at "
              "No. 18, eliminated Ricochet and Dolph Ziggler, and was eliminated by Damian "
              "Priest after about a minute and fifty seconds, then donated his payday to a "
              "Knox County technical-college scholarship fund. He was a sitting mayor at "
              "the time, as he had been for his previous match, the Crown Jewel 2018 tag "
              "with The Undertaker. Retirement-match rumors have circulated since 2025 "
              "but nothing has been scheduled.",
            q_ld="When was Kane's last match?",
            a_ld="Kane's last match was the men's Royal Rumble match on January 31, 2021. "
                 "He entered at No. 18, eliminated Ricochet and Dolph Ziggler, and was "
                 "eliminated by Damian Priest. He donated his earnings from the match to "
                 "a technical-college scholarship fund in Knox County, Tennessee, where "
                 "he was the sitting mayor. He has not wrestled since."),
        dict(
            q="How many world titles did Kane win, and why is the first reign famous?",
            a="Three, under three different belts: the WWF Championship, won from Steve "
              "Austin in a First Blood match at King of the Ring on June 28, 1998; the "
              "ECW Championship, won in 11 seconds at WrestleMania XXIV on March 30, "
              "2008; and the World Heavyweight Championship, won on July 18, 2010 by "
              "cashing in the Money in the Bank briefcase he had won earlier that night. "
              "The first is famous for its length &mdash; he lost it back to Austin on "
              "Raw the next night, roughly 24 hours later, one of the shortest world "
              "title reigns in company history.",
            q_ld="How many world championships did Kane win?",
            a_ld="Kane won three world championships, each under a different title: the "
                 "WWF Championship on June 28, 1998, which he lost back to Steve Austin "
                 "the next night after roughly 24 hours; the ECW Championship, won in 11 "
                 "seconds at WrestleMania XXIV on March 30, 2008; and the World "
                 "Heavyweight Championship, won on July 18, 2010 by cashing in his Money "
                 "in the Bank contract on Rey Mysterio the same night he won it."),
        dict(
            q="Was Kane really The Undertaker&rsquo;s brother, and when did he debut?",
            a="In storyline he was the half-brother, horribly burned in a childhood "
              "funeral-home fire; in reality Glenn Jacobs and Mark Calaway are unrelated "
              "friends. He debuted at Badd Blood on October 5, 1997 by ripping the door "
              "off the first Hell in a Cell and Tombstoning The Undertaker &mdash; an "
              "interference, not a match. His first actual match was a win over Mankind "
              "at Survivor Series on November 9, 1997, overshadowed forever by the "
              "Montreal Screwjob happening later that card.",
            q_ld="When did Kane debut and was he really The Undertaker's brother?",
            a_ld="Kane debuted on October 5, 1997 at Badd Blood: In Your House, "
                 "interfering in the first Hell in a Cell match and attacking The "
                 "Undertaker; his first actual match was a win over Mankind at Survivor "
                 "Series on November 9, 1997. He was The Undertaker's half-brother only "
                 "in storyline; in reality Glenn Jacobs and Mark Calaway are unrelated "
                 "and are longtime friends."),
        dict(
            q="Why did Kane lose the mask, and when did it come back?",
            a="He put the mask on the line against his World Heavyweight Championship "
              "shot at Triple H on the June 23, 2003 Raw in Madison Square Garden, lost, "
              "and unmasked &mdash; launching the darkest version of the character. The "
              "mask returned in December 2011, and he wrestled masked for the remainder "
              "of the character&rsquo;s run, corporate-suit interludes aside.",
            q_ld="Why did Kane unmask in 2003 and when did the mask return?",
            a_ld="Kane unmasked on the June 23, 2003 episode of Raw after losing a match "
                 "against Triple H in which his mask was staked against a World "
                 "Heavyweight Championship opportunity. He wrestled unmasked until "
                 "December 2011, when the mask returned, and he kept it for the rest of "
                 "his career."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Glenn Thomas Jacobs"),
        dict(label="Born", value="April 26, 1967",
             sub="Torrejon de Ardoz, Spain, on a US Air Force base &middot; age 59"),
        dict(label="Billed from", value="Hell", sub="resident of Knox County, Tennessee"),
        dict(label="Height", value="7&#8242;0&#8243;", sub="213 cm (billed)"),
        dict(label="Weight", value="323 lb", sub="147 kg (billed)"),
        dict(label="Debut", value="1992", sub="as Kane: October 5, 1997, Badd Blood"),
        dict(label="Last match", value="January 31, 2021",
             sub="Royal Rumble match, eliminated by Damian Priest &mdash; payday donated"),
        dict(label="Ring names",
             value="Unabomb &rarr; Isaac Yankem, DDS &rarr; fake Diesel &rarr; Kane",
             sub="masked 1997&ndash;2003 and 2011&ndash;2021"),
        dict(label="Signature", value="Chokeslam &middot; Tombstone Piledriver &middot; "
                                      "flying clothesline &middot; the ring-post fire"),
        dict(label="Hall of Fame", value="2021", sub="inducted while a sitting mayor"),
        dict(label="Office", value="Mayor of Knox County, Tennessee",
             sub="2018&ndash;2026, two terms, term-limited; succeeded by Betsy Henderson"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1967-04-26",
    bornplace="Torrejon de Ardoz, Spain",
    nationality="United States",
    height_cm=213,
    weight_kg=147,
    ld=dict(
        alternateName=["Glenn Jacobs", "Glenn Thomas Jacobs", "The Big Red Machine",
                       "The Devil's Favorite Demon", "Isaac Yankem DDS", "Unabomb",
                       "Mayor Glenn Jacobs"],
        award=["WWF Championship (1 reign)",
               "ECW Championship (1 reign)",
               "World Heavyweight Championship (1 reign)",
               "WWF/WWE Intercontinental Championship (2 reigns)",
               "Tag team championships (12 reigns, seven partners)",
               "Money in the Bank (2010)",
               "WWE Hall of Fame (2021)",
               "Mayor of Knox County, Tennessee (2018-2026)"],
        knowsAbout=["Professional wrestling", "WWE", "Local government", "Knox County, Tennessee",
                    "Libertarian politics", "The Brothers of Destruction"],
        description="Kane, the ring name of Glenn Thomas Jacobs, is a retired American "
                    "professional wrestler and politician. Debuting at the first Hell in a "
                    "Cell match in October 1997 as The Undertaker's storyline half-brother, "
                    "he won world championships under three different belts - WWF (1998), "
                    "ECW (2008) and World Heavyweight (2010) - plus twelve tag team titles. "
                    "He served two terms as Mayor of Knox County, Tennessee from 2018 to "
                    "2026, wrestled his final match in the 2021 Royal Rumble while in "
                    "office, and entered the WWE Hall of Fame in 2021.",
        sameAs=["https://en.wikipedia.org/wiki/Kane_(wrestler)",
                "https://www.wwe.com/superstars/kane",
                "https://knoxcounty.org/mayor/"],
    ),
)
