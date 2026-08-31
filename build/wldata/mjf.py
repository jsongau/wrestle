# -*- coding: utf-8 -*-
"""MJF - dossier data.

Sources: web research compiled August 31, 2026, the day after MJF came up empty in the
Casino Gauntlet at All In: London (Andrade won it). AEW title dates verified against
AEW.com's championship history and event coverage from POST Wrestling, Fightful,
Wrestling Inc, Fox News and Bleacher Report; CMLL dates against POST Wrestling's
reporting. Nothing is invented.

Deliberate omissions:
  * No career win-loss total - none verified.
  * The signature-matches section carries a single entry, because only one MJF match
    has a Meltzer rating that was verified in this pass; nothing is padded around it.
  * Dynamite Diamond Ring win years are not itemized - the sources consulted agree on
    the record count of six but not on the year-by-year list.
  * No social links and no theme entry - not verified in this pass.
"""

# ----------------------------------------------------------------- record rows
# Seventeen documented bouts. A curated ledger, not a career count.
ROWS = [
    dict(result="W", date="2020-02-29", promo="AEW",
         event="Revolution", opponent="Cody Rhodes",
         stip="Singles — the star-making grudge win", title=""),
    dict(result="W", date="2022-02-02", promo="AEW", landmark=True,
         event="Dynamite", opponent="CM Punk",
         stip="Singles — first man to beat Punk in his AEW run", title=""),
    dict(result="L", date="2022-03-06", promo="AEW",
         event="Revolution", opponent="CM Punk",
         stip="Dog collar match", title=""),
    dict(result="W", date="2022-11-19", promo="AEW", landmark=True,
         event="Full Gear", opponent="Jon Moxley", opponent_html=True,
         stip="Singles — youngest AEW World Champion; the 406-day reign begins",
         title="AEW World Championship"),
    dict(result="W", date="2023-03-05", promo="AEW", landmark=True,
         event="Revolution", opponent="Bryan Danielson",
         stip="60-minute Iron Man — won in overtime; 5.75 stars (Meltzer)",
         title="AEW World Championship"),
    dict(result="L", date="2023-12-30", promo="AEW", landmark=True,
         event="Worlds End", opponent="Samoa Joe",
         stip="Singles — the record 406-day reign ends", title="AEW World Championship"),
    dict(result="W", date="2024-07-17", promo="AEW",
         event="Dynamite 250", opponent="Will Ospreay", opponent_html=True,
         stip="Singles — rebrands the belt the 'American Championship'",
         title="AEW International Championship"),
    dict(result="L", date="2024-08-25", promo="AEW", landmark=True,
         event="All In — Wembley", opponent="Will Ospreay", opponent_html=True,
         stip="Singles — Ospreay takes the title back", title="AEW International Championship"),
    dict(result="W", date="2025-07-12", promo="AEW", type="tag", landmark=True,
         event="All In: Texas", opponent="The Casino Gauntlet field",
         stip="Casino Gauntlet — wins an anytime world title shot", title=""),
    dict(result="W", date="2025-08-01", promo="CMLL",
         event="Viernes Espectacular — Arena Mexico", opponent="Averno",
         stip="Singles — low blow and a half-crab", title="CMLL World Light Heavyweight Championship"),
    dict(result="L", date="2025-09-19", promo="CMLL", landmark=True,
         event="CMLL 92nd Aniversario", opponent="Mistico",
         stip="Title vs. mask — Mistico keeps the mask, takes the belt",
         title="CMLL World Light Heavyweight Championship"),
    dict(result="W", date="2025-12-27", promo="AEW", type="tag", landmark=True,
         event="Worlds End", opponent="Samoa Joe, Hangman Page & Swerve Strickland",
         stip="Four-way — cashed the gauntlet contract into the match; second reign",
         title="AEW World Championship"),
    dict(result="W", date="2026-04-12", promo="AEW",
         event="Dynasty", opponent="Kenny Omega", opponent_html=True,
         stip="Singles, near 40 minutes — retains with the Dynamite Diamond Ring",
         title="AEW World Championship"),
    dict(result="L", date="2026-04-15", promo="AEW", landmark=True,
         event="Dynamite: Spring BreakThru", opponent="Darby Allin",
         stip="Singles — beaten in just over two minutes, four Coffin Drops",
         title="AEW World Championship"),
    dict(result="W", date="2026-05-24", promo="AEW", landmark=True,
         event="Double or Nothing", opponent="Darby Allin",
         stip="Title vs. hair — third reign at age 30", title="AEW World Championship"),
    dict(result="L", date="2026-07-08", promo="AEW", landmark=True,
         event="Dynamite: Beach Break", opponent="Kenny Omega", opponent_html=True,
         stip="Singles — Ospreay strips the Diamond Ring; the 45-day reign ends",
         title="AEW World Championship"),
    dict(result="L", date="2026-08-30", promo="AEW", type="tag",
         event="All In: London — Wembley", opponent="The Casino Gauntlet field",
         stip="Casino Gauntlet — entered No. 2; Andrade wins", title=""),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Jon Moxley": "jon-moxley", "Will Ospreay": "will-ospreay",
                 "Kenny Omega": "kenny-omega"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="mjf",
    name="MJF",
    realname="Maxwell Tyler Friedman",
    epithet="The Salt of the Earth",
    hook="Record & Titles",

    meta_desc=("MJF, Maxwell Jacob Friedman, is a three-time AEW World Champion whose record "
               "406-day first reign remains the longest in the title's history. Full record, "
               "titles, factions, records and career, current through All In: London 2026."),
    og_desc=("The Salt of the Earth: three AEW World Championship reigns including the record "
             "406-day first one, the youngest champion in company history, six Dynamite Diamond "
             "Rings — and a lost Casino Gauntlet at Wembley."),
    tw_desc="The Salt of the Earth: 3x AEW World Champion, 406-day record reign, youngest ever.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2015",
    height_imp="5&#8242;11&#8243;",
    weight_lb="205",
    world_titles="3",
    vitals_tagline="Better than you, and you know it",
    support_note="Merch &middot; Watch &middot; Read",
    sp_items=[
        dict(ic="MJF", title="AEW Shop", sub="Official tees · Shop AEW",
             tag="Shop", href="https://shop.aew.com/"),
        dict(ic="AEW", title="AEW Roster Profile", sub="AllEliteWrestling.com", tag="Visit",
             href="https://www.allelitewrestling.com/aew-roster"),
        dict(ic="CM", title="Cagematch Profile", sub="Career database",
             tag="Visit", href="https://www.cagematch.net/en?id=2&nr=17012&gimmick=MJF"),
        dict(ic="W", title="Wikipedia", sub="Full biography", tag="Read", charity=True,
             href="https://en.wikipedia.org/wiki/MJF"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Salt of the Earth &middot; The Devil &middot; The Wolf of Wrestling",
    hero_tag="Plainview, New York &middot; <em>CZW &middot; MLW &middot; AEW &middot; CMLL "
             "&middot; 2015&ndash;present</em>",
    now_label="NOW",
    now_bold="No championship — lost the Casino Gauntlet at All In: London",
    now_tail=" &middot; entered No. 2 at Wembley on August 30, 2026; Andrade won the world title "
             "shot; the hair, at least, is safe",
    hstats=[
        dict(value="3",   x=True,  label="AEW World Titles"),
        dict(value="406", x=False, label="Day Record Reign"),
        dict(value="26",  x=False, label="Youngest AEW Champ, Age"),
        dict(value="6",   x=True,  label="Dynamite Diamond Rings"),
    ],
    ghost_link="From Long Island to the longest reign the AEW title has ever had",
    vlabel="Est. 2015 &middot; Plainview, New York",
    mono="MJF",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>MJF</b> is, for the moment, a man without a belt or a contract clause to hide behind. "
        "At All In: London on August 30, 2026 he entered the Casino Gauntlet at No. 2 and watched "
        "Andrade El Idolo pin Nick Wayne to take the world title shot he wanted; seven weeks "
        "earlier, on the July 8 Beach Break edition of Dynamite, Kenny Omega had taken the AEW "
        "World Championship from him after Will Ospreay stripped the Dynamite Diamond Ring off "
        "his hand mid-match. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">3</span>'
        '<span class="pull-cap">AEW World Championship reigns &mdash; 406 days, then 109, then 45</span></span>'
        "That ended his third reign at 45 days and, for the first time since 2019, left him "
        "without an obvious next grievance. He is 30 years old and has already held the AEW World "
        "Championship longer than anyone else ever has.",

        "The record needs stating precisely, because its usual phrasing has expired. The first "
        "reign &mdash; November 19, 2022, when he beat Jon Moxley at Full Gear with brass "
        "knuckles supplied by William Regal, to December 30, 2023, when Samoa Joe beat him at "
        "Worlds End &mdash; ran <b>406 days</b>, and it made him the youngest AEW World Champion "
        "ever at 26. For two years it was routinely called &ldquo;the longest reign in AEW "
        "history.&rdquo; It no longer is: Kazuchika Okada&rsquo;s Continental Championship reign "
        "reached 648 days in 2025. What the 406 remains is the longest reign in the <b>AEW World "
        "Championship&rsquo;s</b> history &mdash; a narrower and still unbroken record. The "
        "other two reigns bookend 2026: 109 days from the Worlds End 2025 four-way to "
        "Darby Allin&rsquo;s two-minute ambush on April 15, and 45 days from the title-vs-hair "
        "revenge win at Double or Nothing on May 24 to Beach Break.",

        "The mechanism of the second reign was pure MJF. He won the <b>Casino Gauntlet</b> at "
        "All In: Texas on July 12, 2025, banking a world title shot redeemable anytime, then sat "
        "on the contract for five months while detouring through Mexico &mdash; winning "
        "CMLL&rsquo;s World Light Heavyweight Championship from Averno at Arena Mexico on August "
        "1, 2025, defending it, unmasking Mistico, and finally losing the belt in a "
        "title-versus-mask match at the CMLL 92nd Aniversario on September 19. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">406</span>'
        '<span class="pull-cap">days as AEW World Champion, 2022&ndash;23 &mdash; still the longest reign in that title&rsquo;s history</span></span>'
        "In December he reappeared on the Holiday Bash Dynamite, executed the contract to "
        "convert Worlds End&rsquo;s scheduled title match into a four-way, and pinned his way "
        "past champion Samoa Joe, Hangman Page and Swerve Strickland on December 27, 2025. "
        "Nobody in AEW has monetized paperwork better.",

        "Underneath the scarf-and-grievance act sits the resume of a serious wrestler: the "
        "60-minute Iron Man match against Bryan Danielson at Revolution 2023, won in overtime at "
        "5.75 stars from Dave Meltzer; the first clean-era win over CM Punk in 2022; a record "
        "<b>six</b> Dynamite Diamond Ring wins, the jewelry that has doubled as a foreign object "
        "through every era of his act; and a near-40-minute war with Kenny Omega at Dynasty in "
        "April 2026 in which he became, per Wikipedia, only the second man ever to kick out of "
        "the One-Winged Angel &mdash; before winning with the ring anyway. Three days later, "
        "exhausted, he lost the title to Darby Allin in two minutes. Both halves of that week "
        "are the character in miniature.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["AEW", "CMLL"],
        promo_labels={"AEW": "AEW", "CMLL": "CMLL"},
        stats=[
            ("3&times;", "AEW World Champion"),
            ("406",  "Day record first reign"),
            ("26",   "Youngest champ, age"),
            ("6&times;", "Dynamite Diamond Ring"),
            ("1",    "Casino Gauntlet win"),
            ("1",    "CMLL title reign"),
        ],
        lead=("Seventeen documented bouts &mdash; all three world title reigns at both ends, the "
              "Punk and Danielson classics, the Mexico detour and both Casino Gauntlets. This "
              "is a curated ledger, not a career count, and no win&ndash;loss total is "
              "published because none could be verified. The pre-AEW CZW and MLW years are "
              "summarized in the titles section rather than given rows, because day-precision "
              "dates for them were not verified. Filter by match type, tap any column header "
              "to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("One entry, deliberately: only one MJF match carries a Meltzer rating that "
                    "was verified in this pass, and this page does not pad ratings it cannot "
                    "source. The Omega Dynasty match and the Punk dog collar bout belong on any "
                    "shortlist of his best; they are simply listed without stars elsewhere on "
                    "this page."),
    signature=[
        dict(rating="5.75", event="Revolution 2023", opponent="Bryan Danielson",
             stip="AEW World Championship — 60-minute Iron Man, won in overtime"),
    ],
    signature_count_word="one",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("3&times;", "AEW World reigns"),
            ("406", "Day record reign"),
            ("1",   "International reign"),
            ("1",   "CMLL Light Heavyweight"),
        ],
        lead=("Three AEW World Championship reigns and a short shelf of everything else — plus "
              "the ring that is not a championship but has decided several. Pre-AEW reign "
              "dates are summarized at the precision actually verified."),
        rows=[
            dict(ic="A", name="AEW World Championship", count="3",
                 sub="November 19, 2022 &ndash; December 30, 2023 &middot; def. Jon Moxley at "
                     "Full Gear, lost to Samoa Joe at Worlds End &middot; <b>406 days</b>, the "
                     "longest reign in the title&rsquo;s history, begun at 26 &mdash; the "
                     "youngest champion ever &middot; December 27, 2025 &ndash; April 15, 2026 "
                     "&middot; won the Worlds End four-way via his Casino Gauntlet contract, "
                     "lost to Darby Allin in two minutes &mdash; 109 days &middot; May 24 "
                     "&ndash; July 8, 2026 &middot; title vs. hair over Allin at Double or "
                     "Nothing, lost to Kenny Omega at Beach Break &mdash; 45 days"),
            dict(ic="I", name="AEW International Championship", count="1",
                 sub="July 17 &ndash; August 25, 2024 &middot; def. Will Ospreay on Dynamite "
                     "250, lost it back to Ospreay at All In: London &middot; 39 days, during "
                     "which he unofficially rebranded it the &ldquo;American "
                     "Championship&rdquo; with a custom stars-and-stripes plate"),
            dict(ic="C", name="CMLL World Light Heavyweight Championship", count="1",
                 sub="August 1 &ndash; September 19, 2025 &middot; def. Averno at Arena Mexico, "
                     "lost to Mistico in a title vs. mask match at the 92nd Aniversario &middot; "
                     "49 days, per Wikipedia&rsquo;s count"),
            dict(ic="R", name="ROH World Tag Team Championship", count="1",
                 sub="2023, with Adam Cole &mdash; the &ldquo;better than you bay bay&rdquo; "
                     "era&rsquo;s strangest artifact &middot; exact reign endpoints not "
                     "verified in this pass"),
            dict(ic="M", name="MLW World Middleweight Championship", count="1",
                 sub="Inaugural champion, late 2010s &middot; also an MLW World Tag Team "
                     "Championship with Richard Holliday &middot; dates not verified in this "
                     "pass"),
            dict(ic="Z", name="CZW World Heavyweight Championship", count="1",
                 sub="Plus the CZW Wired Championship, per Wikipedia &middot; dates not "
                     "verified in this pass"),
            dict(ic="D", name="Dynamite Diamond Ring", count="6",
                 sub="A record six wins of AEW&rsquo;s annual battle royal prize &mdash; not a "
                     "championship, but the ring has ended title matches, including the Omega "
                     "defense at Dynasty 2026 &middot; year-by-year list not verified, so not "
                     "printed"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="He works alone by temperament; every group he has joined ended as evidence for "
             "the prosecution.",
        cards=[
            dict(era="AEW &middot; 2019&ndash;2021",
                 name="The Inner Circle, then the coup",
                 members="Chris Jericho, MJF, Sammy Guevara, Jake Hager, Santana & Ortiz",
                 desc="Joined Jericho's group in 2020, spent a year measuring the drapes, and "
                      "split to form The Pinnacle in 2021 — beating the Inner Circle in the "
                      "first Blood & Guts match. The apprenticeship-then-betrayal template has "
                      "been his standard operating procedure since."),
            dict(era="AEW &middot; 2021&ndash;2022",
                 name="The Pinnacle",
                 members="MJF (leader), Wardlow, Shawn Spears, FTR, Tully Blanchard",
                 desc="His own faction, built as a mirror of Jericho's and dissolved by its own "
                      "logic: bodyguard Wardlow, treated as staff, walked out and beat him "
                      "clean at Double or Nothing 2022 after ten powerbombs."),
            dict(era="AEW &middot; 2025",
                 name="The Hurt Syndicate",
                 members="Bobby Lashley, Shelton Benjamin, MVP — and briefly MJF",
                 desc="Bought his way in during 2025 with a viciousness audition, and was voted "
                      "out on August 6, 2025, per Wikipedia — even a faction built on hurting "
                      "people found him excessive. The Casino Gauntlet contract and the Mexico "
                      "detour immediately followed."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One name, several masks, all of them him: <b>the Salt of the Earth</b> &rarr; "
             "<b>Max, the reluctant friend</b> &rarr; <b>the Devil</b> &rarr; <b>the "
             "contract-holder</b>. The constant is that the villainy is presented as honesty.",
        cards=[
            dict(mono="SE", era="AEW &middot; 2019&ndash;2023", name="The Salt of the Earth",
                 desc="The scarf, the Burberry, the better-than-you catechism — a throwback "
                      "heel built on promo craft rather than plunder, who turned on Cody "
                      "Rhodes in 2019 and won the world title with loaded knuckles in 2022."),
            dict(mono="MAX", era="AEW &middot; 2023", name="Max",
                 desc="The 2023 experiment: a babyface year built on the Adam Cole friendship "
                      "storyline, tag gold in ROH, and four pillars sentiment — ended by the "
                      "Devil angle that revealed the friendship's shelf life."),
            dict(mono="DV", era="AEW &middot; 2023&ndash;2024", name="The Devil",
                 desc="The masked-conspiracy arc that closed the 406-day reign, and the injury "
                      "hiatus after it. He returned at Double or Nothing on May 26, 2024, "
                      "announced he had re-signed with AEW, and attacked Adam Cole — order "
                      "restored."),
            dict(mono="CH", era="AEW &amp; CMLL &middot; 2025&ndash;2026", name="The contract-holder",
                 desc="The gauntlet-contract era: title shots as financial instruments, a CMLL "
                      "championship and an unmasking feud with Mistico in Mexico, a four-way "
                      "cash-in, a hair match won, and finally a reign ended when Will Ospreay "
                      "confiscated the jewelry."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Plainview, Long Island to three world titles by thirty.",
        rows=[
            dict(year="2015", title="Debut",
                 desc="February 15, 2015, trained by Brian Myers and Pat Buck at the Create A "
                      "Pro academy in Hicksville, New York."),
            dict(year="2019", title="Signs with AEW",
                 desc="Announced January 7, 2019 as one of the company's first signings; turns "
                      "on Cody Rhodes at Full Gear that November."),
            dict(year="2022", title="Punk, the ring, and the championship",
                 desc="First man to beat CM Punk in his AEW run on February 2; loses the dog "
                      "collar rematch at Revolution; beats Jon Moxley for the AEW World "
                      "Championship at Full Gear on November 19, at 26 the youngest champion "
                      "ever."),
            dict(year="2023", title="The 406-day reign",
                 desc="The 5.75-star Iron Man over Danielson at Revolution on March 5, the "
                      "Adam Cole double-life storyline, ROH tag gold — and the fall at Worlds "
                      "End on December 30 to Samoa Joe."),
            dict(year="2024", title="Return, re-signing, and the American Championship",
                 desc="Returns at Double or Nothing on May 26 having re-signed; takes the "
                      "International title off Will Ospreay on Dynamite 250 (July 17), "
                      "rebrands it, and loses it back at Wembley on August 25."),
            dict(year="2025", title="The Hurt Syndicate, the gauntlet, and Mexico",
                 desc="In and out of the Hurt Syndicate by August 6; wins the Casino Gauntlet "
                      "at All In: Texas on July 12; wins and loses CMLL's Light Heavyweight "
                      "title (August 1 to September 19, the Mistico mask match); cashes the "
                      "contract into the Worlds End four-way and wins the title on December "
                      "27."),
            dict(year="2026", title="Three reigns' worth of whiplash",
                 desc="Survives the One-Winged Angel to retain over Kenny Omega at Dynasty "
                      "(April 12), loses the title to Darby Allin in two minutes three days "
                      "later, wins it back in the title-vs-hair match at Double or Nothing "
                      "(May 24), loses it to Omega at Beach Break (July 8) after Ospreay "
                      "strips the Diamond Ring, and comes up empty in the Wembley Casino "
                      "Gauntlet on August 30."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Kenny Omega", slug="kenny-omega",
                 desc="The 2026 title rivalry. MJF kicked out of the One-Winged Angel at "
                      "Dynasty on April 12 — only the second man ever to, per Wikipedia — and "
                      "retained with the Dynamite Diamond Ring after nearly 40 minutes; Omega "
                      "took the title at Beach Break on July 8 once Will Ospreay had "
                      "confiscated the ring mid-match."),
            dict(name="CM Punk",
                 desc="The 2022 feud that produced his most replayed promo work — the pipe "
                      "bomb answered in kind. MJF won the first match on February 2, 2022, "
                      "Punk took the dog collar match at Revolution on March 6, and the "
                      "Larry-the-dog monologue in between remains a modern promo touchstone."),
            dict(name="Bryan Danielson",
                 desc="The 60-minute Iron Man at Revolution 2023, won in overtime at 5.75 "
                      "stars — the match that settled whether the loudmouth could actually "
                      "go for an hour. He could."),
            dict(name="Darby Allin",
                 desc="The 2026 humiliation loop: Allin squashed him in two minutes with four "
                      "Coffin Drops on April 15 to take the title; MJF answered at Double or "
                      "Nothing on May 24, keeping his hair and taking the belt back — his "
                      "third reign, at 30."),
            dict(name="Mistico",
                 desc="The Mexico chapter: MJF unmasked him at Grand Slam Mexico in June "
                      "2025, won CMLL gold off Averno that August, and put the title against "
                      "Mistico's mask at the 92nd Aniversario on September 19, 2025 — and "
                      "lost, in front of the happiest crowd of his career."),
            dict(name="Will Ospreay", slug="will-ospreay",
                 desc="Traded the International Championship with him across the summer of "
                      "2024 — Dynamite 250, then Wembley — and lost the world title in July "
                      "2026 substantially because Ospreay pulled the Dynamite Diamond Ring "
                      "off his finger."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Acting",
        lead="Short list, verified only.",
        rows=[
            dict(when="2025", title="Happy Gilmore 2", kind="Film",
                 desc="Feature-film appearance, per Wikipedia."),
            dict(when="2025&ndash;26", title="Violent Night 2", kind="Film",
                 desc="Second listed film credit, per Wikipedia."),
            dict(when="2022&ndash;", title="The promo archive", kind="Television",
                 desc="Wrestling Observer's Best on Interviews in 2021 and 2022 and Most "
                      "Charismatic three times — the talking is the media empire."),
            dict(when="2025", title="Marriage", kind="Personal",
                 desc="Married media personality Alicia Atout on September 5, 2025, per "
                      "Wikipedia."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated the way the sources actually state them — including the one "
             "that quietly expired.",
        stats=[
            ("406", "Day AEW World reign"),
            ("3",   "AEW World reigns"),
            ("26",  "Youngest champion, age"),
        ],
        rows=[
            dict(name="406 days as AEW World Champion — still the title's longest reign",
                 sub="November 19, 2022 to December 30, 2023. It is no longer 'the longest "
                     "reign in AEW history' — Okada's 648-day Continental run passed it in "
                     "2025 — but no AEW World Championship reign has approached it."),
            dict(name="Youngest AEW World Champion ever",
                 sub="26 years old at Full Gear 2022. He completed three reigns before "
                     "turning 31."),
            dict(name="Three AEW World Championship reigns by age 30",
                 sub="406 days, 109 days, 45 days — the second won by contract cash-in into "
                     "a four-way, the third in a title vs. hair match, per Fox News's "
                     "coverage of Double or Nothing 2026."),
            dict(name="A record six Dynamite Diamond Ring wins",
                 sub="The count is consistently reported as six; the year-by-year list is "
                     "not, so only the count is printed here."),
            dict(name="First man to beat CM Punk in his AEW run",
                 sub="February 2, 2022, on Dynamite — Punk's first singles loss since his "
                     "2014 return to wrestling."),
            dict(name="Second man ever to kick out of the One-Winged Angel",
                 sub="At Dynasty, April 12, 2026, per Wikipedia's accounting — Kota Ibushi "
                     "is the only other. MJF retained that night with the Diamond Ring."),
            dict(name="Casino Gauntlet winner, All In: Texas 2025",
                 sub="July 12, 2025 — the anytime title-shot contract he held for 168 days "
                     "before converting Worlds End into a four-way and winning it."),
            dict(name="CMLL World Light Heavyweight Champion",
                 sub="August 1 to September 19, 2025 — won from Averno at Arena Mexico, "
                     "lost to Mistico in a title vs. mask match at the 92nd Aniversario, "
                     "one of the biggest lucha matches of the year."),
            dict(name="The 2026 whiplash fortnight",
                 sub="Retained over Omega in a 40-minute epic on April 12; lost the title in "
                     "roughly two minutes to Darby Allin on April 15. No champion in AEW "
                     "history has had a stranger week, and this page will not pretend "
                     "otherwise."),
        ],
        footnote=("Deliberately absent: a career win-loss total (none verified); a "
                  "year-by-year Dynamite Diamond Ring list (sources conflict); pre-AEW reign "
                  "dates (not verified to day precision); and any Meltzer rating beyond the "
                  "single verified 5.75, per the signature section's note."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wrestling Inc", v="All In 2026 results — the Casino Gauntlet",
             href="https://www.wrestlinginc.com/2247073/aew-all-in-2026-results/"),
        dict(k="AEW", v="Dynamite: Beach Break results — the title changes hands",
             href="https://www.allelitewrestling.com/post/aew-dynamite-beach-break-results-july-8-2026"),
        dict(k="Wikipedia", v="Full biography",
             href="https://en.wikipedia.org/wiki/MJF"),
        dict(k="POST Wrestling", v="CMLL Light Heavyweight title win over Averno",
             href="https://www.postwrestling.com/2025/08/02/mjf-wins-cmll-world-light-heavyweight-title-defends-against-zandokan-jr-on-8-15/"),
        dict(k="Wrestling Inc", v="Darby Allin's title win, broken down",
             href="https://www.wrestlinginc.com/2154588/breaking-down-the-belts-darby-allin-aew-world-championship/"),
        dict(k="Wikipedia", v="List of AEW World Champions",
             href="https://en.wikipedia.org/wiki/List_of_AEW_World_Champions"),
        dict(k="AEW", v="International Championship history",
             href="https://www.allelitewrestling.com/aew-international-championship-history"),
        dict(k="Cagematch", v="Career database profile",
             href="https://www.cagematch.net/en?id=2&nr=17012&gimmick=MJF"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is MJF still AEW World Champion?",
            a="No. Kenny Omega beat him for the title on the Beach Break edition of Dynamite on "
              "<b>July 8, 2026</b>, ending his third reign at 45 days &mdash; a match turned "
              "when Will Ospreay pulled the Dynamite Diamond Ring off MJF&rsquo;s hand before "
              "it could be used. At All In: London on August 30, 2026 he tried to re-enter the "
              "title picture through the Casino Gauntlet and lost it to Andrade El Idolo.",
            q_ld="Is MJF still the AEW World Champion?",
            a_ld="No. MJF lost the AEW World Championship to Kenny Omega on the Beach Break "
                 "edition of AEW Dynamite on July 8, 2026, ending his third reign after 45 "
                 "days. Will Ospreay removed MJF's Dynamite Diamond Ring during the match, "
                 "preventing its use. MJF then failed to win the Casino Gauntlet at All In: "
                 "London on August 30, 2026, which Andrade El Idolo won."),
        dict(
            q="Does MJF still hold the longest reign in AEW history?",
            a="Only in the narrow sense &mdash; and the distinction matters. His 406-day first "
              "reign (November 19, 2022 to December 30, 2023) is still the longest in the "
              "<b>AEW World Championship&rsquo;s</b> history. But as a claim about all AEW "
              "titles it expired in 2025, when Kazuchika Okada&rsquo;s Continental "
              "Championship reign reached <b>648 days</b>. Pages still calling MJF&rsquo;s "
              "reign the longest in company history are out of date.",
            q_ld="Does MJF hold the longest championship reign in AEW history?",
            a_ld="No, only the longest AEW World Championship reign. MJF's first reign ran 406 "
                 "days from November 19, 2022 to December 30, 2023, which remains the record "
                 "for that title. However, Kazuchika Okada's AEW Continental Championship "
                 "reign of 648 days, ended in December 2025, is the longest championship "
                 "reign in AEW company history."),
        dict(
            q="How did MJF win his second AEW World Championship?",
            a="By contract. He won the Casino Gauntlet at All In: Texas on July 12, 2025, "
              "earning a world title shot redeemable anytime, then held it until the December "
              "2025 Holiday Bash Dynamite, where he cashed it in to be <b>added</b> to Worlds "
              "End&rsquo;s championship match &mdash; converting it into a four-way with "
              "champion Samoa Joe, Hangman Page and Swerve Strickland. He won it on December "
              "27, 2025. The reign lasted 109 days, ending in Darby Allin&rsquo;s two-minute "
              "upset on April 15, 2026.",
            q_ld="How did MJF win his second AEW World Championship?",
            a_ld="MJF won the Casino Gauntlet at All In: Texas on July 12, 2025, earning an "
                 "anytime AEW World Championship match, and in December 2025 cashed in the "
                 "contract to be added to the Worlds End title match, making it a four-way "
                 "with champion Samoa Joe, Hangman Page and Swerve Strickland. He won the "
                 "match on December 27, 2025, and held the title 109 days before losing to "
                 "Darby Allin on April 15, 2026."),
        dict(
            q="What happened between MJF and Mistico?",
            a="A genuine lucha feud, not a cameo. MJF unmasked Mistico at Grand Slam Mexico in "
              "June 2025, then beat Averno for the CMLL World Light Heavyweight Championship "
              "at Arena Mexico on August 1, 2025 &mdash; working as a pro-American heel with a "
              "translator &mdash; and defended against Zandokan Jr. before putting the title "
              "against Mistico&rsquo;s mask at the CMLL 92nd Aniversario on September 19. "
              "Mistico won; MJF left Mexico beltless and the crowd left delighted.",
            q_ld="What happened in the feud between MJF and Mistico in CMLL?",
            a_ld="MJF unmasked Mistico at AEW Grand Slam Mexico in June 2025, won the CMLL "
                 "World Light Heavyweight Championship from Averno at Arena Mexico on August "
                 "1, 2025, and defended it against Zandokan Jr. before facing Mistico in a "
                 "title versus mask match at the CMLL 92nd Aniversario on September 19, 2025. "
                 "Mistico won the match and the championship, keeping his mask."),
        dict(
            q="Did MJF really kick out of the One-Winged Angel?",
            a="Yes &mdash; at Dynasty on April 12, 2026, in the near-40-minute title defense "
              "against Kenny Omega. Per Wikipedia&rsquo;s accounting he is only the "
              "<b>second</b> man ever to do it, after Kota Ibushi. He won that match with the "
              "Dynamite Diamond Ring; the rematch at Beach Break on July 8, with the ring "
              "confiscated by Will Ospreay, went the other way.",
            q_ld="Did MJF kick out of Kenny Omega's One-Winged Angel?",
            a_ld="Yes. At AEW Dynasty on April 12, 2026, MJF kicked out of Kenny Omega's "
                 "One-Winged Angel during their AEW World Championship match, becoming per "
                 "Wikipedia only the second wrestler ever to do so after Kota Ibushi. MJF won "
                 "that match using the Dynamite Diamond Ring, but lost the July 8, 2026 "
                 "rematch after Will Ospreay removed the ring."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Maxwell Tyler Friedman",
             sub="&ldquo;Jacob&rdquo; belongs to the ring name only"),
        dict(label="Born", value="March 15, 1996", sub="Plainview, New York &middot; age 30"),
        dict(label="Billed from", value="Plainview, Long Island, New York"),
        dict(label="Height", value="5&#8242;11&#8243;", sub="180 cm, per Cagematch"),
        dict(label="Weight", value="205 lb", sub="93 kg, per Cagematch"),
        dict(label="Debut", value="February 15, 2015",
             sub="Create A Pro Wrestling Academy, Hicksville, New York"),
        dict(label="Trained by", value="Brian Myers &amp; Pat Buck"),
        dict(label="Signature", value="Heat Seeker piledriver &middot; Salt of the Earth "
                                      "armbar &middot; the Dynamite Diamond Ring",
             sub="The ring is a foreign object with a trophy case"),
        dict(label="Titles held", value="None as of August 31, 2026",
             sub="Third AEW World reign ended July 8, 2026"),
        dict(label="Family", value="Married to Alicia Atout", sub="September 5, 2025"),
        dict(label="Also known as",
             value="The Salt of the Earth &middot; The Devil &middot; The Wolf of Wrestling"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1996-03-15",
    bornplace="Plainview, New York, United States",
    nationality="United States",
    height_cm=180,
    weight_kg=93,
    ld=dict(
        alternateName=["Maxwell Jacob Friedman", "Maxwell Tyler Friedman",
                       "The Salt of the Earth", "The Devil", "The Wolf of Wrestling"],
        award=["AEW World Championship (3 reigns; record 406-day reign; youngest champion "
               "at 26)",
               "AEW International Championship (1 reign)",
               "CMLL World Light Heavyweight Championship (1 reign)",
               "ROH World Tag Team Championship (1 reign, with Adam Cole)",
               "MLW World Middleweight Championship (inaugural)",
               "CZW World Heavyweight Championship (1 reign)",
               "Dynamite Diamond Ring (record 6 wins)",
               "Casino Gauntlet winner (2025)"],
        knowsAbout=["Professional wrestling", "All Elite Wrestling", "CMLL", "Ring of Honor",
                    "Major League Wrestling", "Promo work"],
        description="MJF, born Maxwell Tyler Friedman in Plainview, New York, is an American "
                    "professional wrestler and three-time AEW World Champion. His first reign "
                    "of 406 days remains the longest in the title's history, begun at 26 as "
                    "the youngest champion ever. He lost the championship to Kenny Omega on "
                    "July 8, 2026 and was unsuccessful in the Casino Gauntlet at All In: "
                    "London on August 30, 2026.",
        sameAs=["https://en.wikipedia.org/wiki/MJF",
                "https://www.cagematch.net/en?id=2&nr=17012&gimmick=MJF"],
    ),
)
