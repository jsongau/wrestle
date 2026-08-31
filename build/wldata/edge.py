# -*- coding: utf-8 -*-
"""Edge / Adam Copeland - dossier data.

Sources: web-verified August 31, 2026 (Wikipedia; Wrestling Inc on Double or Nothing
2026 and All In: London 2026; Wikipedia's AEW Revolution 2025 and TNT Championship
pages; contemporaneous coverage of the 2024 tibia injury and the 2025 FTR turn).
Every match row carries a day-precision date.

Deliberate omissions:
  * No career win-loss total - none verified, none invented.
  * No social links - handles were not verified in this pass.
  * No Observer star ratings in the signature block - none verified in this pass.
  * The exact length of the first (December 30, 2023) TNT reign is given as the
    sources give it - about three and a half minutes - rather than to the second.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2000-04-02", promo="WWE", landmark=True, type="tag",
         event="WrestleMania 2000", opponent="The Hardy Boyz & The Dudley Boyz",
         stip="Triangle ladder match, with Christian — first WWF Tag Team Championship", title="WWF Tag Team Championship"),
    dict(result="W", date="2001-04-01", promo="WWE", landmark=True, type="tag",
         event="WrestleMania X-Seven", opponent="The Hardy Boyz & The Dudley Boyz",
         stip="TLC II, with Christian — the mid-air spear on Jeff Hardy", title="WWF Tag Team Championship"),
    dict(result="W", date="2005-04-03", promo="WWE", landmark=True, type="tag",
         event="WrestleMania 21 — Los Angeles", opponent="The Money in the Bank field",
         stip="Wins the first Money in the Bank ladder match ever held", title=""),
    dict(result="W", date="2006-01-08", promo="WWE", landmark=True,
         event="New Year's Revolution", opponent="John Cena",
         stip="The first Money in the Bank cash-in — first WWE Championship", title="WWE Championship"),
    dict(result="L", date="2008-03-30", promo="WWE",
         event="WrestleMania XXIV — Orlando", opponent="The Undertaker",
         stip="Singles — the streak match, main event", title="World Heavyweight Championship"),
    dict(result="W", date="2011-04-03", promo="WWE", landmark=True,
         event="WrestleMania XXVII — Atlanta", opponent="Alberto Del Rio",
         stip="Singles — his last match before nine years of forced retirement", title="World Heavyweight Championship"),
    dict(result="W", date="2020-04-05", promo="WWE", landmark=True,
         event="WrestleMania 36 Night 2", opponent="Randy Orton",
         stip="Last Man Standing — first match back after 3,285 days", title=""),
    dict(result="W", date="2021-01-31", promo="WWE", landmark=True, type="tag",
         event="Royal Rumble", opponent="The 2021 Royal Rumble field",
         stip="Wins from No. 1 — his second Rumble win, eleven years after the first", title=""),
    dict(result="L", date="2021-04-11", promo="WWE", type="tag",
         event="WrestleMania 37 Night 2", opponent="Roman Reigns & Daniel Bryan",
         stip="Triple threat main event — Reigns pins both challengers", title="WWE Universal Championship"),
    dict(result="W", date="2023-08-18", promo="WWE", landmark=True,
         event="SmackDown — Toronto", opponent="Sheamus",
         stip="Singles — his final WWE match, 25 years after his debut", title=""),
    dict(result="W", date="2023-12-30", promo="AEW",
         event="Worlds End", opponent="Christian Cage",
         stip="No disqualification — wins the TNT Championship", title="AEW TNT Championship"),
    dict(result="L", date="2023-12-30", promo="AEW",
         event="Worlds End", opponent="Christian Cage",
         stip="Immediate rematch the same night — the belt goes straight back after about three and a half minutes", title="AEW TNT Championship"),
    dict(result="W", date="2024-03-20", promo="AEW", landmark=True,
         event="Dynamite — Toronto", opponent="Christian Cage",
         stip="I Quit match — a second TNT Championship, at home", title="AEW TNT Championship"),
    dict(result="W", date="2024-05-26", promo="AEW", landmark=True,
         event="Double or Nothing — Las Vegas", opponent="Malakai Black",
         stip="Barbed-wire steel cage — retains, but fractures his tibia diving off the cage; stripped of the title days later", title="AEW TNT Championship"),
    dict(result="L", date="2025-03-09", promo="AEW", type="tag",
         event="Revolution — Los Angeles", opponent="Jon Moxley & Christian Cage",
         stip="World title match turned three-way by Christian's Casino Gauntlet cash-in — Moxley retains", title="AEW World Championship"),
    dict(result="W", date="2025-08-24", promo="AEW", type="tag",
         event="Forbidden Door — London", opponent="Killswitch & Kip Sabian",
         stip="First match as a reunited team with Christian Cage", title=""),
    dict(result="W", date="2025-09-20", promo="AEW", type="tag",
         event="All Out — Toronto", opponent="FTR",
         stip="Tag — the payback for the Dynasty betrayal, in Copeland's home city", title=""),
    dict(result="W", date="2026-05-24", promo="AEW", landmark=True, type="tag",
         event="Double or Nothing — Queens", opponent="FTR",
         stip="I Quit match, with Beth Phoenix run-in — Cage & Cope win the tag titles", title="AEW World Tag Team Championship"),
    dict(result="W", date="2026-08-30", promo="AEW", landmark=True, type="tag",
         event="All In: London — Wembley", opponent="The Young Bucks",
         stip="Tag — retained; stared down by three teams after the bell", title="AEW World Tag Team Championship"),
]

DATA = dict(
    slug="edge",
    name="Edge",
    realname="Adam Joseph Copeland",
    epithet="The Rated-R Superstar",
    hook="Record & Titles",

    meta_desc=("Edge - Adam 'Cope' Copeland - won 11 world championships in WWE, 31 titles in all, "
               "and now holds the AEW World Tag Team Championship with Christian Cage. Full record, "
               "titles, factions, records and career."),
    og_desc=("The Rated-R Superstar: 11 WWE world titles, 31 WWE championships, two Royal Rumble "
             "wins, a nine-year retirement he came back from, and a current AEW tag title reign "
             "alongside Christian Cage."),
    tw_desc="11 world titles, two Royal Rumbles, one impossible comeback - and AEW tag gold at 52.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1992",
    height_imp="6&#8242;5&#8243;",
    weight_lb="241",
    world_titles="11",
    vitals_tagline="You think you know me",
    support_note="Merch &middot; Games &middot; Watch",
    sp_items=[
        dict(ic="AEW", title="AEW Shop", sub="Official Cope merch",
             tag="Shop", href="https://www.shopaew.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable as a legend across the 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="TV", title="All Elite Wrestling", sub="Dynamite & Collision — where he wrestles now",
             tag="Watch", href="https://www.allelitewrestling.com/"),
        dict(ic="HOF", title="WWE Hall of Fame Profile", sub="WWE.com — Class of 2012", charity=True,
             tag="Visit", href="https://www.wwe.com/superstars/edge"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Adam &ldquo;Cope&rdquo; Copeland &middot; The Ultimate Opportunist",
    hero_tag="Orangeville, Ontario &middot; <em>WWF/WWE &middot; AEW &middot; 1992&ndash;present</em>",
    now_label="NOW",
    now_bold="AEW World Tag Team Champion",
    now_tail=" &middot; one half of Cage &amp; Cope with Christian Cage &mdash; retained against the Young Bucks at All In: London on August 30, 2026",
    hstats=[
        dict(value="11", x=True, label="WWE World Titles"),
        dict(value="31", x=False, label="WWE Championships"),
        dict(value="2",  x=True,  label="Royal Rumble Wins"),
        dict(value="9",  x=False, label="Years Retired, Undone"),
    ],
    ghost_link="From an essay-contest tryout to eleven world championships",
    vlabel="Est. 1992 &middot; Orangeville, ON",
    mono="ED",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Edge</b> &mdash; Adam Copeland, and in AEW simply <b>Cope</b> &mdash; has the strangest "
        "shape of any great career: superstardom, a spinal diagnosis that ended it at 37, nine years "
        "of retirement, and then a second career longer and stranger than most wrestlers&rsquo; "
        "first. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">11</span>'
        '<span class="pull-cap">world championship reigns in WWE &mdash; four WWE Championships and a record seven World Heavyweight Championships</span></span>'
        "He won eleven world championships in WWE &mdash; four WWE Championships and a "
        "record seven World Heavyweight Championships &mdash; among <b>31 total WWE titles</b>, the "
        "most of anyone in that company&rsquo;s history. He won the first Money in the Bank match "
        "ever held and executed the first cash-in. He won Royal Rumbles eleven years apart. And as "
        "of August 31, 2026 he is an AEW World Tag Team Champion at 52, alongside the same partner "
        "he won his first title with at 26: Christian.",

        "One number needs untangling, because even the sources trip on it. Edge is frequently "
        "credited with winning the tag titles &ldquo;a record 12 times with Christian.&rdquo; The "
        "12 is real but it is not theirs together: Edge holds <b>12 World Tag Team Championship "
        "reigns in total</b> &mdash; seven with Christian, plus reigns with Chris Benoit, Hulk "
        "Hogan, Randy Orton and Chris Jericho &mdash; and two WWE Tag Team Championship reigns "
        "(with Rey Mysterio in 2002, and with Jericho in 2009) on top. Fourteen WWE tag reigns, "
        "seven of them with Christian. The arithmetic that gets him to 31 championships: 4 WWE "
        "titles + 7 World Heavyweight + 5 Intercontinental + 1 United States + 12 World Tag + 2 WWE "
        "Tag. The AEW titles &mdash; two TNT Championships and the current World Tag Team "
        "Championship &mdash; sit outside that count.",

        "The first career ran June 22, 1998 (his televised WWF debut) to April 3, 2011: the ladder "
        "and TLC wars with Christian, the Hardys and the Dudleys; King of the Ring 2001; the "
        "Rated-R Superstar heel run that started with the live sex celebration and ended with him "
        "as the best villain of his era; the WrestleMania XXIV main event against The Undertaker. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">3,285</span>'
        '<span class="pull-cap">days between the WrestleMania XXVII farewell and the Royal Rumble 2020 return &mdash; a retirement diagnosed as permanent</span></span>'
        "Then an MRI found cervical spinal stenosis, and on April 11, 2011 he retired on Raw as "
        "reigning World Heavyweight Champion, days after beating Alberto Del Rio at WrestleMania "
        "XXVII. Hall of Fame, 2012, inducted by Christian. The comeback nobody planned for came at "
        "the Royal Rumble on January 26, 2020; he beat Randy Orton in a Last Man Standing match at "
        "WrestleMania 36, won the 2021 Rumble from the No. 1 spot, main-evented WrestleMania 37 "
        "against Roman Reigns and Daniel Bryan, and founded The Judgment Day &mdash; the faction "
        "that promptly threw him out and became WWE&rsquo;s top act without him.",

        "The AEW chapter began at WrestleDream on October 1, 2023, six weeks after his final WWE "
        "match &mdash; a win over Sheamus in Toronto on August 18, 2023. Since then: two TNT "
        "Championships, both involving Christian Cage on the other side; a fractured tibia from the "
        "top of a barbed-wire cage at Double or Nothing 2024 that cost him the belt and eight "
        "months; a world title challenge against Jon Moxley at Revolution 2025 that Christian&rsquo;s "
        "cash-in turned into a three-way; and FTR&rsquo;s betrayal at Dynasty 2025, which finally "
        "pushed the two old rivals onto the same side. Cage &amp; Cope beat FTR in an I Quit match "
        "at Double or Nothing on May 24, 2026 &mdash; Beth Phoenix, Copeland&rsquo;s wife, punching "
        "Dax Harwood down the ramp on the way &mdash; to win the AEW World Tag Team Championship, "
        "and retained against the Young Bucks at All In: London on August 30, 2026, where the Motor "
        "City Machine Guns, FTR and New Level all appeared for the staredown that maps out what "
        "comes next.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE", "AEW"],
        promo_labels={"WWE": "WWF/WWE", "AEW": "AEW"},
        stats=[
            ("11&times;", "WWE world champion"),
            ("31", "WWE championships"),
            ("2&times;", "Royal Rumble winner"),
            ("1st", "Money in the Bank"),
            ("2&times;", "TNT Champion"),
            ("1&times;", "AEW Tag Champion"),
        ],
        lead=("Nineteen documented bouts &mdash; the ladder era, the first cash-in, both "
              "retirement-adjacent matches, the comeback, and the full AEW arc through All In: "
              "London. This is a curated ledger, not a career count; no career win&ndash;loss total "
              "exists across 34 years and none is invented. The two Worlds End rows are the same "
              "night: he won the TNT title and lost it back to Christian Cage inside the same show. "
              "Filter by match type, tap any column header to sort, and turn spoilers on to reveal "
              "results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the reputation rests on. No Observer star ratings are published "
                    "here &mdash; none were verified against archives in this pass."),
    signature=[
        dict(rating="—", event="WrestleMania X-Seven", opponent="The Hardy Boyz & The Dudley Boyz",
             stip="TLC II — the mid-air spear that follows him everywhere"),
        dict(rating="—", event="New Year's Revolution 2006", opponent="John Cena",
             stip="The first Money in the Bank cash-in — the template every cash-in since has copied"),
        dict(rating="—", event="WrestleMania 36 Night 2", opponent="Randy Orton",
             stip="Last Man Standing — first match after nine years retired"),
        dict(rating="—", event="Double or Nothing 2026", opponent="FTR",
             stip="I Quit — the tag title win with Christian Cage and Beth Phoenix"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("11&times;", "WWE world titles"),
            ("7&times;", "World Heavyweight (record)"),
            ("14&times;", "WWE tag reigns"),
            ("31", "WWE titles in all"),
        ],
        lead=("Thirty-one championships in WWE &mdash; the most in that company&rsquo;s history "
              "&mdash; plus the AEW gold of the second career. Individual reign dates for the "
              "midcard and tag runs are not itemised here; the counts are the load-bearing part."),
        rows=[
            dict(ic="W", name="World Heavyweight Championship", count="7",
                 sub="The record for that title. The last reign ended the strangest way a reign can: "
                     "relinquished undefeated on April 15, 2011, because his neck retired him first"),
            dict(ic="E", name="WWE Championship", count="4",
                 sub="The first via the first Money in the Bank cash-in on John Cena at New "
                     "Year&rsquo;s Revolution, January 8, 2006"),
            dict(ic="T", name="AEW World Tag Team Championship", count="1",
                 sub="Current. With Christian Cage as Cage &amp; Cope &mdash; def. FTR in an I Quit "
                     "match at Double or Nothing, May 24, 2026; retained against the Young Bucks at "
                     "All In: London, August 30, 2026"),
            dict(ic="N", name="AEW TNT Championship", count="2",
                 sub="Def. Christian Cage at Worlds End, December 30, 2023, for roughly three and a "
                     "half minutes; def. Christian again in an I Quit match on the March 20, 2024 "
                     "Dynamite in Toronto &mdash; stripped that May after fracturing his tibia at "
                     "Double or Nothing"),
            dict(ic="G", name="World Tag Team Championship", count="12",
                 sub="Seven with Christian &mdash; the ladder-and-TLC era &mdash; plus reigns with "
                     "Chris Benoit, Hulk Hogan, Randy Orton and Chris Jericho"),
            dict(ic="TT", name="WWE Tag Team Championship", count="2",
                 sub="With Rey Mysterio (2002) and with Chris Jericho (2009)"),
            dict(ic="I", name="WWE Intercontinental Championship", count="5",
                 sub="Five reigns between 1999 and 2011 &mdash; part of the 31-title total"),
            dict(ic="U", name="WWE United States Championship", count="1",
                 sub="The single reign that completes his Grand Slam"),
            dict(ic="K", name="King of the Ring &middot; Money in the Bank &middot; Royal Rumbles",
                 count="4",
                 sub="King of the Ring 2001; the first Money in the Bank ladder match at "
                     "WrestleMania 21, April 3, 2005; Royal Rumble wins in 2010 and 2021 &mdash; the "
                     "2021 win from the No. 1 spot"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Four units across four eras &mdash; and the two that mattered most both had Christian "
             "in them.",
        cards=[
            dict(era="WWF &middot; 1998&ndash;1999",
                 name="The Brood",
                 members="Gangrel, Edge, Christian",
                 desc="The vampire-adjacent trio that introduced both Canadians: rising through the "
                      "ring in a circle of fire, dumping 'bloodbaths' on enemies. A gimmick with a "
                      "shelf life, but the entrance remains one of the most-referenced of the era, "
                      "and it welded Edge and Christian together on screen as they already were off "
                      "it."),
            dict(era="WWF/WWE &middot; 1998&ndash;2001",
                 name="Edge & Christian",
                 members="Edge, Christian",
                 desc="Seven tag title reigns, the five-second pose, kazoos, and the ladder/TLC "
                      "trilogy with the Hardys and Dudleys that redefined what tag wrestling could "
                      "draw. They split in 2001 when Edge won King of the Ring and Christian turned "
                      "on him — the first of a quarter-century of breakups and reunions."),
            dict(era="WWE &middot; 2022",
                 name="The Judgment Day",
                 members="Edge (founder), Damian Priest, Rhea Ripley",
                 desc="Founded by Edge in April 2022 as a cult-of-personality heel stable; by June "
                      "the members had voted him out, with Finn Balor taking his place. The faction "
                      "became WWE's dominant act for years — built on a foundation he laid and was "
                      "evicted from."),
            dict(era="AEW &middot; 2025&ndash;present",
                 name="Cage & Cope",
                 members="Christian Cage, Cope, with Beth Phoenix in their corner",
                 desc="The reunion nobody in the story wanted until FTR forced it: after the "
                      "Dynasty 2025 betrayal, Christian — Copeland's tormentor through 2023-24 — "
                      "became his partner again at Forbidden Door on August 24, 2025. AEW World "
                      "Tag Team Champions since Double or Nothing 2026, with Copeland's wife Beth "
                      "Phoenix as the equaliser at ringside."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One man, three billing names and a quarter century of recalibration: <b>Sexton "
             "Hardcastle</b> (independents) &rarr; <b>Edge</b> (1998&ndash;2023) &rarr; <b>Adam "
             "Copeland / Cope</b> (AEW, 2023&ndash;present). WWE owns the name Edge; he took his "
             "own to AEW.",
        cards=[
            dict(mono="SH", era="Independents &middot; 1992&ndash;1998", name="Sexton Hardcastle",
                 desc="The Ontario independent scene name, alongside Christian as 'Suicide "
                      "Blondes.' He broke in by winning a Toronto newspaper essay contest for free "
                      "training with Sweet Daddy Siki and Ron Hutchison at 17."),
            dict(mono="BR", era="WWF &middot; 1998&ndash;2000", name="The brooding loner",
                 desc="Debuted June 22, 1998 as a mute, trench-coated mystery who entered through "
                      "the crowd — then found his actual gift, comedy, when the Brood dissolved "
                      "into Edge & Christian's five-second poses."),
            dict(mono="RR", era="WWE &middot; 2004&ndash;2011", name="The Rated-R Superstar",
                 desc="The defining persona: an opportunistic, gleefully hateable heel built on the "
                      "live sex celebration with Lita, the first Money in the Bank cash-in, and a "
                      "genius for winning titles in ways that felt like theft. 'The Ultimate "
                      "Opportunist' was an insult he adopted as a title."),
            dict(mono="GM", era="WWE &middot; 2020&ndash;2023", name="The grizzled comeback",
                 desc="The 2020-23 version wrestled as a man borrowing time: Last Man Standing "
                      "wars with Orton, the 2021 Rumble from No. 1, the Judgment Day founding and "
                      "eviction, and a farewell lap that ended where he started, in Toronto."),
            dict(mono="CO", era="AEW &middot; 2023&ndash;present", name="Cope",
                 desc="Billed under his real name — then just Cope — since WrestleDream 2023. The "
                      "Cope Open challenge series, two TNT titles, a broken tibia off a cage top "
                      "at 50, and now one half of Cage & Cope. The persona is mostly just Adam "
                      "Copeland: a lifer who cannot stop."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="An essay contest in Toronto to a Wembley title defence 34 years later.",
        rows=[
            dict(year="1992", title="Debut",
                 desc="First match in Toronto in 1992, after winning free training from Sweet "
                      "Daddy Siki and Ron Hutchison in a newspaper essay contest at 17."),
            dict(year="1998", title="WWF debut",
                 desc="Televised debut June 22, 1998 on Raw against Jose Estrada Jr.; the Brood, "
                      "then Edge & Christian follow."),
            dict(year="2000", title="The ladder era begins",
                 desc="First tag titles in the WrestleMania 2000 triangle ladder match on April 2; "
                      "TLC II at WrestleMania X-Seven a year later."),
            dict(year="2001", title="King of the Ring, and the split",
                 desc="Wins the 2001 tournament; Christian turns on him, and the singles career "
                      "starts."),
            dict(year="2005", title="Mr. Money in the Bank",
                 desc="Wins the first Money in the Bank ladder match at WrestleMania 21 on April "
                      "3, 2005 — then holds the case for nine months."),
            dict(year="2006", title="The first cash-in",
                 desc="Cashes in on a bloodied John Cena at New Year's Revolution on January 8, "
                      "2006 for his first WWE Championship, inventing the move every holder since "
                      "has copied."),
            dict(year="2008", title="Champion era",
                 desc="La Familia, three world title reigns in a year, and the WrestleMania XXIV "
                      "main event against The Undertaker's streak on March 30."),
            dict(year="2011", title="Retired by his own spine",
                 desc="Retains over Del Rio at WrestleMania XXVII on April 3; an MRI finds "
                      "cervical spinal stenosis; he announces retirement on the April 11 Raw and "
                      "vacates the World Heavyweight Championship. Hall of Fame, 2012."),
            dict(year="2020", title="The comeback",
                 desc="Returns at the Royal Rumble on January 26, 2020, nine years after doctors "
                      "said never; beats Orton in a Last Man Standing match at WrestleMania 36."),
            dict(year="2021", title="Rumble to main event",
                 desc="Wins the Royal Rumble from No. 1 on January 31; main-events WrestleMania 37 "
                      "against Reigns and Bryan."),
            dict(year="2023", title="Toronto goodbye, AEW hello",
                 desc="Final WWE match August 18 in Toronto, beating Sheamus; debuts in AEW at "
                      "WrestleDream on October 1."),
            dict(year="2024", title="TNT gold and a broken leg",
                 desc="Beats Christian in the I Quit match on March 20 in Toronto; retains against "
                      "Malakai Black in the barbed-wire cage at Double or Nothing on May 26 but "
                      "fractures his tibia coming off the top of it, and is stripped of the title."),
            dict(year="2025", title="Moxley, betrayal, reunion",
                 desc="Loses the three-way world title match at Revolution on March 9; FTR turn on "
                      "him at Dynasty; he and Christian Cage reunite at Forbidden Door on August "
                      "24 and beat FTR at All Out in Toronto on September 20."),
            dict(year="2026", title="Tag champions again, 26 years on",
                 desc="Cage & Cope take the AEW World Tag Team Championship from FTR in the "
                      "Double or Nothing I Quit match on May 24 and retain against the Young Bucks "
                      "at All In: London on August 30."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Christian Cage",
                 desc="Childhood best friend, seven-time tag partner, 2001 betrayer, 2012 Hall of "
                      "Fame inductor, 2023-24 AEW tormentor, and current tag partner again. Their "
                      "three TNT title matches — Worlds End 2023 twice in one night, then the "
                      "Toronto I Quit match — were the meanest wrestling either has done, which is "
                      "exactly why the 2025 reunion landed. No relationship in wrestling has been "
                      "mined this long or this well."),
            dict(name="Randy Orton",
                 desc="Rated-RKO partners turned career-long opposites. Orton was the opponent for "
                      "the 2020 comeback — the WrestleMania 36 Last Man Standing match and the "
                      "vicious 'greatest wrestling match ever' Backlash follow-up — and the man "
                      "Edge last eliminated to win the 2021 Rumble... the 2010 one having ended "
                      "the same way."),
            dict(name="John Cena",
                 desc="The definitive Edge victim: the first cash-in at New Year's Revolution "
                      "2006, the TLC wars, the Unforgiven 2006 title change in Toronto. Edge's "
                      "heel peak exists in opposition to Cena's face peak."),
            dict(name="The Undertaker",
                 desc="The 2008 program — champion versus streak at WrestleMania XXIV, then the "
                      "SummerSlam Hell in a Cell — was the elevation ceremony: Edge main-evented "
                      "WrestleMania against the most protected act in the company and took the "
                      "chokeslam through the ring for his trouble."),
            dict(name="FTR",
                 desc="Allies against the Death Riders through early 2025 until they beat him "
                      "down at Dynasty in April — the turn that put him on a stretcher and "
                      "created Cage & Cope. Beaten at All Out 2025, beaten again in the I Quit "
                      "title match at Double or Nothing 2026 where Dax Harwood threatened his "
                      "family and Beth Phoenix answered personally — and back in the frame after "
                      "the All In: London staredown."),
            dict(name="Mick Foley",
                 desc="One match, permanent consequences: the WrestleMania 22 hardcore match, "
                      "April 2, 2006, ending with Edge spearing Foley through a flaming table. "
                      "Edge has said it legitimised him as a main-eventer; Foley designed it to "
                      "do exactly that."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Acting",
        lead="The rare wrestler with a real second-screen career, kept to the verified list.",
        rows=[
            dict(when="2004", title="Adam Copeland on Edge", kind="Book",
                 desc="The autobiography, written during an injury layoff in the WWE years."),
            dict(when="2016&ndash;2020", title="Vikings", kind="TV",
                 desc="Recurring role as Kjetill Flatnose across the History drama's later "
                      "seasons — the credit that made the acting career real."),
            dict(when="2023&ndash;", title="Percy Jackson and the Olympians", kind="TV",
                 desc="Plays the war god Ares in the Disney+ series."),
            dict(when="2022&ndash;", title="WWE 2K / AEW games", kind="Games",
                 desc="Playable in WWE 2K entries as Edge and in AEW's roster as Cope."),
            dict(when="2012", title="WWE Hall of Fame", kind="Honor",
                 desc="Class of 2012, inducted by Christian — at the time the youngest headline "
                      "inductee of the modern era, because retirement came at 37."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, and the asterisks the retellings drop.",
        stats=[
            ("31", "WWE championships"),
            ("7", "World Heavyweight reigns"),
            ("3,285", "Days retired"),
        ],
        rows=[
            dict(name="31 championships in WWE — the most in company history",
                 sub="4 WWE Championships + 7 World Heavyweight + 5 Intercontinental + 1 United "
                     "States + 12 World Tag Team + 2 WWE Tag Team. The AEW titles sit outside this "
                     "count."),
            dict(name="Record seven World Heavyweight Championship reigns",
                 sub="No one else reached seven with that title before it was retired in 2013. The "
                     "last reign was surrendered, not lost — vacated April 15, 2011 upon "
                     "retirement."),
            dict(name="First Money in the Bank winner and first cash-in",
                 sub="Won the inaugural ladder match at WrestleMania 21 on April 3, 2005; cashed "
                     "in on John Cena at New Year's Revolution on January 8, 2006. Every cash-in "
                     "since is quoting him."),
            dict(name="Two Royal Rumble wins, eleven years apart",
                 sub="2010 and 2021 — the 2021 win from the No. 1 spot, at age 47, one year into "
                     "a comeback from a nine-year retirement. Only a handful of men have won "
                     "multiple Rumbles; none with that gap."),
            dict(name="The comeback itself",
                 sub="Diagnosed with cervical spinal stenosis and retired April 11, 2011; cleared "
                     "and returned January 26, 2020 — 3,285 days later — and then wrestled for "
                     "another six-plus years and counting."),
            dict(name="Grand Slam Champion",
                 sub="World, Intercontinental, United States and tag titles — the full WWE set."),
            dict(name="Tag team champion 26 years apart, with the same partner",
                 sub="First tag titles with Christian at WrestleMania 2000 on April 2, 2000; AEW "
                     "World Tag Team Champions with Christian Cage since May 24, 2026. Both were "
                     "won in ladder-adjacent violence — a triangle ladder match then, an I Quit "
                     "match now."),
            dict(name="The barbed-wire cage dive at 50",
                 sub="Double or Nothing, May 26, 2024: retained the TNT title against Malakai "
                     "Black, dove off the top of the cage, and fractured his tibia on landing — "
                     "stripped of the title days later, out roughly eight months."),
            dict(name="King of the Ring 2001",
                 sub="The tournament win that launched the singles run, the same summer the "
                     "Christian split did."),
        ],
        footnote=("Deliberately absent: any career win-loss total (none verified across 34 years), "
                  "social handles (not verified in this pass), and Observer ratings (not checked "
                  "against archives). The 11 world titles are WWE-only — AEW has not put a world "
                  "championship on him, a fact his Revolution 2025 challenge left intact."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Adam_Copeland"),
        dict(k="Wrestling Inc", v="Double or Nothing 2026 &mdash; Cage &amp; Cope win the tag titles",
             href="https://www.wrestlinginc.com/2180296/aew-double-or-nothing-2026-cope-cage-adam-copeland-christian-ftr-dax-harwood-cash-wheeler-new-champs-i-quit/"),
        dict(k="Wrestling Inc", v="All In: London 2026 &mdash; retained over the Young Bucks",
             href="https://www.wrestlinginc.com/2247132/aew-all-in-london-2026-cope-cage-young-bucks-defeat-facing-down-rivals/"),
        dict(k="Wikipedia", v="AEW Revolution 2025 &mdash; the Moxley three-way",
             href="https://en.wikipedia.org/wiki/AEW_Revolution_(2025)"),
        dict(k="Wikipedia", v="AEW TNT Championship reign history",
             href="https://en.wikipedia.org/wiki/AEW_TNT_Championship"),
        dict(k="POST Wrestling", v="Forbidden Door 2025 &mdash; the reunion&rsquo;s first match",
             href="https://www.postwrestling.com/2025/08/24/aew-forbidden-door-adam-copeland-christian-cage-take-down-killswitch-kip-sabian-in-tag-action/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Why did Edge retire in 2011, and how did he come back?",
            a="An MRI in the spring of 2011 found <b>cervical spinal stenosis</b> &mdash; a "
              "narrowing of the spinal canal &mdash; and doctors refused to clear him, citing risk "
              "of paralysis. He announced retirement on the April 11, 2011 Raw as reigning World "
              "Heavyweight Champion, days after beating Alberto Del Rio at WrestleMania XXVII, and "
              "vacated the title on April 15. Nine years of medical advances and re-evaluation "
              "later, he was cleared, and returned in the 2020 Royal Rumble on January 26 &mdash; "
              "3,285 days after his last match. He has wrestled ever since, in WWE until 2023 and "
              "AEW from October 2023.",
            q_ld="Why did Edge retire in 2011, and how did he come back?",
            a_ld="Edge retired in April 2011 after an MRI revealed cervical spinal stenosis, a "
                 "narrowing of the spinal canal, and doctors refused to clear him to wrestle due "
                 "to the risk of paralysis. He announced his retirement on April 11, 2011 as "
                 "reigning World Heavyweight Champion and vacated the title. After being medically "
                 "cleared following years of re-evaluation, he returned at the Royal Rumble on "
                 "January 26, 2020, nine years later, and has wrestled since — in WWE until 2023 "
                 "and in AEW since October 2023."),
        dict(
            q="How many world titles has Edge won &mdash; and does AEW change the number?",
            a="Eleven, all in WWE: four WWE Championships and a record seven World Heavyweight "
              "Championships. AEW does not change it &mdash; his AEW titles are two TNT "
              "Championships and the current World Tag Team Championship, and his one AEW World "
              "Championship match (Revolution, March 9, 2025, against Jon Moxley, turned into a "
              "three-way by Christian Cage&rsquo;s cash-in) was a loss. His overall WWE total is 31 "
              "championships, the most in that company&rsquo;s history.",
            q_ld="How many world championships has Edge won?",
            a_ld="Eleven, all in WWE: four WWE Championships and a record seven World Heavyweight "
                 "Championships. His AEW titles — two TNT Championships and the AEW World Tag Team "
                 "Championship he currently holds with Christian Cage — are not world titles, and "
                 "his one AEW World Championship match, at Revolution on March 9, 2025, was a "
                 "loss. He won 31 championships in WWE overall, the most in that company's "
                 "history."),
        dict(
            q="What is Edge&rsquo;s status right now?",
            a="As of August 31, 2026 he is one half of the reigning <b>AEW World Tag Team "
              "Champions</b> with Christian Cage, as Cage &amp; Cope. They took the titles from FTR "
              "in an I Quit match at Double or Nothing on May 24, 2026 &mdash; with Beth Phoenix "
              "intervening on her husband&rsquo;s behalf &mdash; and retained against the Young "
              "Bucks at All In: London on August 30, 2026. After that defence the Motor City "
              "Machine Guns, FTR and New Level all confronted the champions, so the queue is "
              "formed. He turns 53 in October and wrestles as Cope, under his real surname&rsquo;s "
              "shorthand, because WWE owns the name Edge.",
            q_ld="What is Edge's status in AEW right now?",
            a_ld="As of August 31, 2026, Adam Copeland, billed as Cope, is one half of the "
                 "reigning AEW World Tag Team Champions with Christian Cage, as the team Cage and "
                 "Cope. They won the titles from FTR in an I Quit match at Double or Nothing on "
                 "May 24, 2026 and retained them against the Young Bucks at All In: London on "
                 "August 30, 2026, after which the Motor City Machine Guns, FTR and New Level all "
                 "confronted them as potential challengers."),
        dict(
            q="Why is he called Cope in AEW?",
            a="Because WWE owns the trademark on &ldquo;Edge.&rdquo; He debuted in AEW at "
              "WrestleDream on October 1, 2023 under his real name, Adam Copeland, and the billing "
              "has since compressed to <b>Cope</b> &mdash; which also names his open-challenge "
              "series, the Cope Open. The Rated-R iconography travelled with him even though the "
              "name could not.",
            q_ld="Why is Edge called Cope in AEW?",
            a_ld="WWE owns the trademark on the ring name Edge, so when Adam Copeland debuted in "
                 "AEW at WrestleDream on October 1, 2023 he was billed under his real name, which "
                 "has since been shortened to Cope. His open-challenge series in AEW was called "
                 "the Cope Open."),
        dict(
            q="What happened between Edge and FTR?",
            a="They were allies first &mdash; FTR stood with him against Jon Moxley&rsquo;s Death "
              "Riders through early 2025. After his world title loss at Revolution, FTR beat him "
              "down at Dynasty in April 2025, putting him out on a stretcher. The answer was the "
              "reunion with Christian Cage: wins over FTR at All Out in Toronto on September 20, "
              "2025 and again &mdash; for FTR&rsquo;s tag titles &mdash; in the Double or Nothing "
              "I Quit match on May 24, 2026, where Dax Harwood invoked Copeland&rsquo;s daughters "
              "and Beth Phoenix personally delivered the receipts. FTR reappeared in the "
              "challengers&rsquo; staredown at All In: London, so it is not over.",
            q_ld="What happened between Edge and FTR in AEW?",
            a_ld="FTR were Adam Copeland's allies against the Death Riders until April 2025, when "
                 "they attacked him after AEW Dynasty, leaving him stretchered out. Copeland "
                 "reunited with Christian Cage in response; the pair beat FTR at All Out on "
                 "September 20, 2025 and took the AEW World Tag Team Championship from them in an "
                 "I Quit match at Double or Nothing on May 24, 2026, with Beth Phoenix "
                 "intervening. FTR appeared among the challengers confronting the champions at "
                 "All In: London on August 30, 2026."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Adam Joseph Copeland"),
        dict(label="Born", value="October 30, 1973",
             sub="Orangeville, Ontario, Canada &middot; age 52"),
        dict(label="Billed from", value="Toronto, Ontario"),
        dict(label="Height", value="6&#8242;5&#8243;", sub="196 cm"),
        dict(label="Weight", value="241 lb", sub="109 kg (billed)"),
        dict(label="Debut", value="1992", sub="Toronto, as a 19-year-old; WWF televised debut June 22, 1998"),
        dict(label="Trained by", value="Sweet Daddy Siki &amp; Ron Hutchison",
             sub="training won through a Toronto newspaper essay contest at 17"),
        dict(label="Ring names", value="Sexton Hardcastle &rarr; Edge &rarr; Adam Copeland / Cope",
             sub="1992&ndash;98 &middot; 1998&ndash;2023 &middot; 2023&ndash;present &mdash; WWE owns "
                 "&ldquo;Edge,&rdquo; so AEW bills him by his own name"),
        dict(label="Signature", value="Spear &middot; Killswitch/Impaler DDT &middot; crossface",
             sub="the spear delivered from everywhere, including mid-air at TLC II"),
        dict(label="Family", value="Married to Beth Phoenix",
             sub="WWE Hall of Famer, now a recurring presence in his AEW corner; two daughters"),
        dict(label="Brand", value="AEW", sub="World Tag Team Champion with Christian Cage since May 24, 2026"),
        dict(label="Also known as", value="The Rated-R Superstar &middot; The Ultimate Opportunist &middot; Cope"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1973-10-30",
    bornplace="Orangeville, Ontario, Canada",
    nationality="Canada",
    height_cm=196,
    weight_kg=109,
    ld=dict(
        alternateName=["Adam Joseph Copeland", "Adam Copeland", "Cope", "Sexton Hardcastle",
                       "The Rated-R Superstar", "The Ultimate Opportunist"],
        award=["WWE Championship (4 reigns)",
               "World Heavyweight Championship (record 7 reigns)",
               "WWF/World Tag Team Championship (12 reigns)",
               "WWE Tag Team Championship (2 reigns)",
               "WWE Intercontinental Championship (5 reigns)",
               "WWE United States Championship (1 reign)",
               "AEW World Tag Team Championship (1 reign, current, with Christian Cage)",
               "AEW TNT Championship (2 reigns)",
               "Royal Rumble winner (2010, 2021)",
               "First Money in the Bank winner (2005)",
               "King of the Ring (2001)",
               "WWE Hall of Fame (2012)"],
        knowsAbout=["Professional wrestling", "WWE", "AEW", "Tag team wrestling", "Ladder matches",
                    "Acting"],
        description="Edge, born Adam Joseph Copeland in Orangeville, Ontario, is a Canadian "
                    "professional wrestler and actor. In WWE he won 31 championships, the most in "
                    "company history, including 11 world titles - four WWE Championships and a "
                    "record seven World Heavyweight Championships - two Royal Rumbles, and the "
                    "first Money in the Bank match. Forced to retire in 2011 with cervical spinal "
                    "stenosis, he returned nine years later in 2020. Since 2023 he has wrestled in "
                    "AEW as Cope, winning the TNT Championship twice and, with Christian Cage as "
                    "Cage & Cope, the AEW World Tag Team Championship, which the pair hold as of "
                    "August 2026.",
        sameAs=["https://en.wikipedia.org/wiki/Adam_Copeland",
                "https://www.wwe.com/superstars/edge"],
    ),
)
