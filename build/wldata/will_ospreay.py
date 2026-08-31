# -*- coding: utf-8 -*-
"""Will Ospreay - dossier data.

Sources: web research compiled August 31, 2026 - the day after Ospreay won the AEW World
Championship at All In: London. Every match row carries a day-precision date verified
against event coverage (POST Wrestling, Fightful, Wrestling Inc, AEW.com, Fox News) or
Wikipedia's championship tables. Nothing is invented; where two outlets disagree on a
detail (the finishing move at All In), the disagreement is printed rather than resolved.

Deliberate omissions:
  * No career win-loss total - no verified figure exists and none is fabricated.
  * No social links - handles were not verified in this pass.
  * No theme entry - no Spotify URL was verified.
  * His reported injury appearance at Forbidden Door 2025 is not given a match row: the
    only sourcing found was a single summary, and the surgery date (September 17, 2025)
    is the verified anchor instead.
"""

# ----------------------------------------------------------------- record rows
# A curated ledger of sixteen documented bouts, not a career count. NJPW dates are from
# Wikipedia's title and tournament tables; AEW dates from AEW.com's own championship
# history page and PPV results coverage.
ROWS = [
    dict(result="W", date="2016-06-07", promo="NJPW", landmark=True,
         event="Best of the Super Juniors 23 final", opponent="Ryusuke Taguchi",
         stip="Tournament final — youngest and first British winner", title=""),
    dict(result="W", date="2019-01-04", promo="NJPW",
         event="Wrestle Kingdom 13", opponent="Kota Ibushi",
         stip="Singles", title="NEVER Openweight Championship"),
    dict(result="W", date="2019-06-05", promo="NJPW", landmark=True,
         event="Best of the Super Juniors 26 final", opponent="Shingo Takagi",
         stip="Tournament final — 5.75 stars (Meltzer)", title=""),
    dict(result="W", date="2021-04-04", promo="NJPW", landmark=True,
         event="Sakura Genesis", opponent="Kota Ibushi",
         stip="Singles — first British holder; vacated after 32 days",
         title="IWGP World Heavyweight Championship"),
    dict(result="L", date="2023-01-04", promo="NJPW", landmark=True,
         event="Wrestle Kingdom 17", opponent="Kenny Omega", opponent_html=True,
         stip="Singles — 6.25 stars (Meltzer)", title="IWGP United States Championship"),
    dict(result="W", date="2023-06-25", promo="AEW",
         event="Forbidden Door", opponent="Kenny Omega", opponent_html=True,
         stip="Singles — regains the title", title="IWGP United States Championship"),
    dict(result="W", date="2023-08-27", promo="AEW",
         event="All In — Wembley", opponent="Chris Jericho",
         stip="Singles", title=""),
    dict(result="W", date="2024-04-21", promo="AEW", landmark=True,
         event="Dynasty", opponent="Bryan Danielson",
         stip="Singles — 6.5 stars (Meltzer), his highest ever in AEW", title=""),
    dict(result="W", date="2024-05-26", promo="AEW",
         event="Double or Nothing", opponent="Roderick Strong",
         stip="Singles — first reign begins", title="AEW International Championship"),
    dict(result="L", date="2024-06-30", promo="AEW",
         event="Forbidden Door", opponent="Swerve Strickland",
         stip="Singles — challenge", title="AEW World Championship"),
    dict(result="W", date="2024-08-25", promo="AEW", landmark=True,
         event="All In — Wembley", opponent="MJF", opponent_html=True,
         stip="Singles — regains the title at Wembley", title="AEW International Championship"),
    dict(result="L", date="2024-10-12", promo="AEW", type="tag",
         event="WrestleDream", opponent="Konosuke Takeshita & Ricochet",
         stip="Three-way — Takeshita wins the title", title="AEW International Championship"),
    dict(result="L", date="2024-12-28", promo="AEW",
         event="Worlds End", opponent="Kazuchika Okada", opponent_html=True,
         stip="Continental Classic final", title=""),
    dict(result="L", date="2025-05-25", promo="AEW",
         event="Double or Nothing", opponent="Hangman Adam Page",
         stip="Owen Hart Cup final", title=""),
    dict(result="L", date="2026-04-12", promo="AEW",
         event="Dynasty", opponent="Jon Moxley", opponent_html=True,
         stip="Singles — challenge, first match back from neck surgery era",
         title="AEW Continental Championship"),
    dict(result="W", date="2026-06-28", promo="AEW", landmark=True,
         event="Forbidden Door — San Jose", opponent="Swerve Strickland",
         stip="Owen Hart Cup final — earns the All In title shot", title=""),
    dict(result="W", date="2026-08-30", promo="AEW", landmark=True,
         event="All In: London — Wembley", opponent="Kenny Omega", opponent_html=True,
         stip="Singles — 34 minutes; first reign begins", title="AEW World Championship"),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Kenny Omega": "kenny-omega", "MJF": "mjf",
                 "Kazuchika Okada": "kazuchika-okada", "Jon Moxley": "jon-moxley"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="will-ospreay",
    name="Will Ospreay",
    realname="William Peter Charles Ospreay",
    epithet="The Aerial Assassin",
    hook="Record & Titles",

    meta_desc=("Will Ospreay won the AEW World Championship from Kenny Omega at All In: London on "
               "August 30, 2026 — his first reign. Full record, titles, factions, records and "
               "career, from BritWres to Wembley."),
    og_desc=("The Aerial Assassin: AEW World Champion as of August 30, 2026, former IWGP World "
             "Heavyweight Champion, two-time BOSJ winner and the most five-star-rated wrestler "
             "in Observer history."),
    tw_desc="The Aerial Assassin: AEW World Champion, crowned at Wembley on August 30, 2026.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2012",
    height_imp="6&#8242;1&#8243;",
    weight_lb="220",
    world_titles="2",
    vitals_tagline="The Aerial Assassin",
    support_note="Merch &middot; Watch &middot; Read",
    sp_items=[
        dict(ic="WO", title="AEW Shop", sub="Official tees · Shop AEW",
             tag="Shop", href="https://shop.aew.com/"),
        dict(ic="AEW", title="AEW Roster Profile", sub="AllEliteWrestling.com", tag="Visit",
             href="https://www.allelitewrestling.com/aew-roster"),
        dict(ic="NJ", title="NJPW", sub="United Empire · NJPW1972.com",
             tag="Visit", href="https://www.njpw1972.com/"),
        dict(ic="W", title="Wikipedia", sub="Full biography", tag="Read", charity=True,
             href="https://en.wikipedia.org/wiki/Will_Ospreay"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Aerial Assassin &middot; The Commonwealth Kingpin &middot; The Billy GOAT",
    hero_tag="London, England &middot; <em>BritWres &middot; RevPro &middot; NJPW &middot; AEW &middot; "
             "2012&ndash;present</em>",
    now_label="NOW",
    now_bold="AEW World Champion — first reign",
    now_tail=" &middot; beat Kenny Omega in 34 minutes at All In: London, Wembley Stadium, August 30, 2026",
    hstats=[
        dict(value="54",  x=False, label="Five-Star Matches"),
        dict(value="6.5", x=False, label="Highest Meltzer Rating"),
        dict(value="919", x=False, label="Day RevPro Reign"),
        dict(value="2",   x=True,  label="BOSJ Wins"),
    ],
    ghost_link="From a 2012 BritWres debut to the AEW World Championship at Wembley",
    vlabel="Est. 2012 &middot; London, England",
    mono="WO",

    # ---------------------------------------------------------------- 01 overview
    correction=2,
    overview=[
        "<b>Will Ospreay</b> is the AEW World Champion, and he has been for one day. He beat Kenny "
        "Omega in the main event of All In: London at Wembley Stadium on August 30, 2026, in front of a "
        "reported 40,000-plus crowd in his home country, after 34 minutes. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">1st</span>'
        '<span class="pull-cap">AEW World Championship reign &mdash; won from Kenny Omega at Wembley on August 30, 2026</span></span>'
        "It is his first AEW World Championship reign, two years after he failed in his first "
        "challenge against Swerve Strickland at Forbidden Door 2024, and it caps the strangest year of "
        "his career: double-fusion neck surgery in September 2025, a return in March 2026, a stint "
        "inside Jon Moxley&rsquo;s Death Riders that he ended by handing his patch back, and an Owen "
        "Hart Cup win over Swerve on June 28 that earned the Wembley shot. One sourcing note on the "
        "finish: POST Wrestling logs a final Hidden Blade after Omega survived a Storm Breaker; "
        "Wrestling Inc&rsquo;s recap credits the Storm Breaker itself. The result is not in dispute.",

        "The resume behind the moment is mostly a New Japan resume. He is a two-time Best of the Super "
        "Juniors winner (2016, the youngest and first British winner ever; 2019, beating Shingo Takagi "
        "in a final Dave Meltzer rated 5.75 stars), a three-time IWGP Junior Heavyweight Champion, a "
        "former NEVER Openweight Champion, and the first British IWGP World Heavyweight Champion, "
        "beating Kota Ibushi at Sakura Genesis on April 4, 2021. He was also the final IWGP United "
        "States Champion of note in the belt&rsquo;s last era, trading it with Kenny Omega across "
        "Wrestle Kingdom 17 and Forbidden Door 2023 before the title was folded away. At home he held "
        "the RevPro British Heavyweight Championship for <b>919 days</b> (February 14, 2020 to August "
        "21, 2022). By Wikipedia&rsquo;s count he has <b>54</b> matches rated five stars or higher by "
        "the Wrestling Observer&rsquo;s Dave Meltzer &mdash; the most of any wrestler ever &mdash; "
        "with a personal peak of 6.5 for the Bryan Danielson match at AEW Dynasty on April 21, 2024.",

        "One thing worth stating precisely, because most retellings blur it: Ospreay has held two "
        "world championships, and he never lost the first one. His IWGP World Heavyweight reign ended "
        "after 32 days when he <b>vacated</b> the title on May 20, 2021 with a neck injury &mdash; no "
        "one beat him for it. The neck is the recurring villain of the career: the same joint forced "
        "the double-fusion surgery of September 17, 2025, announced after his Owen Hart Cup final loss "
        "to Hangman Page that May. He has also never won the G1 Climax, a gap frequently assumed "
        "filled &mdash; he lost the 2022 final to Kazuchika Okada and the 2023 final to Tetsuya Naito. "
        "The record he actually holds is the ratings one, and the two Owen Hart Cups &mdash; no, one: "
        "he lost the 2025 final and won the 2026 tournament. Precision matters on this page.",

        "The 2026 arc is the one the reign is built on. Cleared on February 25 after five months out, "
        "he returned at Revolution on March 15, storming the ring after Jon Moxley&rsquo;s Continental "
        "Championship defense and fighting off the Death Riders. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">919</span>'
        '<span class="pull-cap">days as RevPro British Heavyweight Champion &mdash; the longest reign in the title&rsquo;s history</span></span>'
        "He challenged Moxley at Dynasty on April 12 and lost, then did the thing nobody expected: he "
        "accepted Moxley&rsquo;s offer and joined the Death Riders on the July 1 Dynamite. The "
        "membership lasted four weeks. He won the Owen Hart Cup with the Death Riders at ringside, "
        "helped Kenny Omega beat MJF for the AEW World Championship at Beach Break on July 8 by "
        "stripping MJF of the Dynamite Diamond Ring, and then refused Moxley&rsquo;s order to "
        "suffocate Omega with a plastic bag at Redemption on July 26 &mdash; tearing the bag apart and "
        "fighting his own unit off. On the July 29 Dynamite he returned his patch: &ldquo;You "
        "don&rsquo;t get to pull the trigger for me. I am out.&rdquo; A month later he walked into "
        "Wembley with United Empire allies Francesco Akira, HENARE and Callum Newman at his side and "
        "took the title from the man he had saved.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["AEW", "NJPW"],
        promo_labels={"AEW": "AEW", "NJPW": "NJPW"},
        stats=[
            ("1",    "AEW World reign, current"),
            ("54",   "Five-star matches"),
            ("6.5",  "Meltzer peak (Danielson)"),
            ("2&times;", "Best of the Super Juniors"),
            ("919",  "Day RevPro reign"),
            ("32",   "Day IWGP World reign"),
        ],
        lead=("Seventeen years condensed to sixteen documented bouts &mdash; the tournament finals, "
              "the title changes and the Wembley nights. This is a curated ledger, not a career "
              "count, and no win&ndash;loss total is published because none could be verified. NJPW "
              "dates come from Wikipedia&rsquo;s championship tables; AEW dates from AEW.com&rsquo;s "
              "own International Championship history and event coverage. Filter by match type, tap "
              "any column header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the ratings reputation rests on. Wikipedia credits him with 54 "
                    "matches at five stars or better from Dave Meltzer, the most ever; these three "
                    "carry the ratings most often cited, reported here as published rather than "
                    "re-verified against Observer archives."),
    signature=[
        dict(rating="6.5", event="Dynasty 2024", opponent="Bryan Danielson",
             stip="Confirmed at 6.5 stars in the Observer — among the highest ratings ever given"),
        dict(rating="6.25", event="Wrestle Kingdom 17", opponent="Kenny Omega",
             stip="IWGP United States Championship — Omega wins"),
        dict(rating="5.75", event="Best of the Super Juniors 26 final", opponent="Shingo Takagi",
             stip="The 2019 final that made the heavyweight move inevitable"),
    ],
    signature_count_word="three",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("1",   "AEW World reign"),
            ("2&times;", "AEW International"),
            ("1",   "IWGP World reign"),
            ("919", "Day RevPro reign"),
        ],
        lead=("Two world championships on two continents, plus the junior-division haul that built "
              "the name. Independent reign dates not listed here were not verified in this pass and "
              "are not invented."),
        rows=[
            dict(ic="A", name="AEW World Championship", count="1",
                 sub="August 30, 2026 &ndash; present &middot; def. Kenny Omega at All In: London, "
                     "Wembley Stadium &middot; his first reign, won in his home country"),
            dict(ic="I", name="AEW International Championship", count="2",
                 sub="May 26 &ndash; July 17, 2024 (def. Roderick Strong at Double or Nothing, lost "
                     "to MJF on Dynamite 250) &middot; August 25 &ndash; October 12, 2024 (def. MJF "
                     "at All In: London, lost to Konosuke Takeshita in a three-way at WrestleDream)"),
            dict(ic="W", name="IWGP World Heavyweight Championship", count="1",
                 sub="April 4 &ndash; May 20, 2021 &middot; def. Kota Ibushi at Sakura Genesis "
                     "&middot; first British holder &middot; vacated with a neck injury after 32 "
                     "days, never lost in the ring"),
            dict(ic="U", name="IWGP United States Championship", count="2",
                 sub="June 12, 2022 &ndash; January 4, 2023 (206 days, lost to Kenny Omega at "
                     "Wrestle Kingdom 17) &middot; June 25 &ndash; December 2023 (regained from "
                     "Omega at Forbidden Door; the title was then folded into the new IWGP Global "
                     "Championship, leaving him the last champion of its main line)"),
            dict(ic="J", name="IWGP Junior Heavyweight Championship", count="3",
                 sub="2017&ndash;2020 &middot; first British holder &middot; twice ended by Hiromu "
                     "Takahashi, including at Wrestle Kingdom 14"),
            dict(ic="N", name="NEVER Openweight Championship", count="1",
                 sub="January 4 &ndash; April 6, 2019 &middot; def. Kota Ibushi at Wrestle Kingdom 13"),
            dict(ic="R", name="RevPro British Heavyweight Championship", count="1",
                 sub="February 14, 2020 &ndash; August 21, 2022 &middot; def. Zack Sabre Jr., lost "
                     "to Ricky Knight Jr. &middot; <b>919 days</b>, the longest reign in the "
                     "title&rsquo;s history"),
            dict(ic="6", name="NEVER Openweight 6-Man Tag Team Championship", count="1",
                 sub="Won May 4, 2026 at Wrestling Dontaku with Great-O-Khan and HENARE &middot; "
                     "status as of August 31, 2026 not re-verified"),
            dict(ic="P", name="PROGRESS World Championship", count="1",
                 sub="2015 &middot; reign dates not verified in this pass"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="The empire he built, and the one he rented a room in for four weeks of 2026.",
        cards=[
            dict(era="NJPW &middot; 2020&ndash;present",
                 name="United Empire",
                 members="Will Ospreay (founder), Great-O-Khan, Jeff Cobb, HENARE, Francesco Akira, "
                         "TJP, Callum Newman, others across eras",
                 desc="Founded when Ospreay turned on Kazuchika Okada in October 2020, and the vehicle "
                      "for his entire heavyweight run in Japan. He stayed affiliated even after going "
                      "to AEW full-time, returning at Sakura Genesis in April 2026 and winning NEVER "
                      "six-man gold with O-Khan and HENARE that May. Akira, HENARE and Callum Newman "
                      "walked him to the ring at All In: London on August 30, 2026."),
            dict(era="AEW &middot; July 2026",
                 name="Death Riders",
                 members="Jon Moxley, Claudio Castagnoli, Wheeler Yuta, Marina Shafir, PAC, Daniel "
                         "Garcia &mdash; and, from July 1 to July 29, 2026, Ospreay",
                 desc="The strangest month of the career. Ospreay fought the Death Riders on his March "
                      "return, lost to Moxley at Dynasty, then accepted membership on the July 1 "
                      "Dynamite. The end came fast: ordered to suffocate Kenny Omega with a plastic "
                      "bag at Redemption on July 26, he refused, fought the group off, and handed his "
                      "patch back to Moxley on the July 29 Dynamite — “You don't get to pull the "
                      "trigger for me. I am out.” Moxley, unusually, let him leave."),
            dict(era="AEW &middot; 2024&ndash;present",
                 name="The Wembley act",
                 members="Ospreay, largely alone",
                 desc="Not a faction — the AEW singles run itself. He arrived full-time in 2024 as a "
                      "babyface built on match quality, main-evented both recent Wembley All Ins from "
                      "the mid-card up, and has said the Death Riders detour gave the character an "
                      "edge it lacked. The world title run that starts now is the payoff on all of it."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One name almost the whole way &mdash; the evolution has been in style, not branding: "
             "<b>Dark Britannico</b> (2012) &rarr; <b>The Aerial Assassin</b> (2013&ndash;2020) "
             "&rarr; <b>The Commonwealth Kingpin</b> (2020&ndash;2024) &rarr; <b>The Billy GOAT / "
             "AEW World Champion</b> (2024&ndash;present).",
        cards=[
            dict(mono="DB", era="BritWres &middot; 2012", name="Dark Britannico",
                 desc="The debut gimmick, April 1, 2012, on the British independents out of the London "
                      "School of Lucha Libre. It did not last; the flying did."),
            dict(mono="AA", era="Independents &amp; NJPW juniors &middot; 2013&ndash;2020",
                 name="The Aerial Assassin",
                 desc="The high-flying identity that won two Best of the Super Juniors and three IWGP "
                      "Junior Heavyweight Championships, and that critics of the style argued about "
                      "in public — a 2016 BOSJ match with Ricochet became wrestling's biggest "
                      "style-wars flashpoint of the decade."),
            dict(mono="CK", era="NJPW heavyweight &middot; 2020&ndash;2024", name="The Commonwealth Kingpin",
                 desc="The heel heavyweight who founded United Empire, added mass, swapped the "
                      "Os-Cutter's primacy for the Hidden Blade and Storm Breaker, and took the IWGP "
                      "World Heavyweight Championship in April 2021."),
            dict(mono="BG", era="AEW &middot; 2024&ndash;present", name="The Billy GOAT",
                 desc="The AEW-era self-description — the ratings record made literal. Rebuilt as a "
                      "babyface, detoured through the Death Riders in 2026, and crowned AEW World "
                      "Champion at Wembley on August 30, 2026."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="From an April Fools' Day debut to the AEW World Championship at Wembley.",
        rows=[
            dict(year="2012", title="Debut",
                 desc="Debuts April 1, 2012 on the British scene as Dark Britannico, trained at the "
                      "London School of Lucha Libre."),
            dict(year="2016", title="Wins Best of the Super Juniors at 23",
                 desc="Beats Ryusuke Taguchi in the June 7 final — the youngest winner and the first "
                      "British one."),
            dict(year="2019", title="Second BOSJ, NEVER title, junior-to-heavyweight pivot",
                 desc="Beats Kota Ibushi for the NEVER Openweight title at Wrestle Kingdom 13 on "
                      "January 4, then wins the June 5 BOSJ final over Shingo Takagi at 5.75 stars."),
            dict(year="2021", title="IWGP World Heavyweight Champion, then a vacated belt",
                 desc="Beats Ibushi at Sakura Genesis on April 4 to become the first British champion; "
                      "vacates on May 20 with a neck injury after 32 days."),
            dict(year="2023", title="The Omega series",
                 desc="Loses to Kenny Omega at Wrestle Kingdom 17 on January 4 (6.25 stars), regains "
                      "the IWGP US title from him at Forbidden Door on June 25, and beats Chris "
                      "Jericho at the first Wembley All In on August 27."),
            dict(year="2024", title="Full-time AEW, the Danielson match, two International reigns",
                 desc="The 6.5-star Bryan Danielson match at Dynasty on April 21; International "
                      "Championship wins at Double or Nothing (May 26) and All In: London (August "
                      "25); losses to Swerve at Forbidden Door and to Okada in the Continental "
                      "Classic final at Worlds End."),
            dict(year="2025", title="The neck again",
                 desc="Loses the Owen Hart Cup final to Hangman Page on May 25, then undergoes "
                      "double-fusion neck surgery on September 17. Out for the rest of the year."),
            dict(year="2026", title="Return, Death Riders, and the AEW World Championship",
                 desc="Cleared February 25; returns at Revolution March 15; joins the Death Riders "
                      "July 1 and quits July 29 after refusing to suffocate Kenny Omega; wins the "
                      "Owen Hart Cup over Swerve Strickland at Forbidden Door June 28; beats Omega "
                      "for the AEW World Championship at All In: London on August 30."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Kenny Omega", slug="kenny-omega",
                 desc="The defining rivalry, now with a championship on it. Omega won at Wrestle "
                      "Kingdom 17 on January 4, 2023 at 6.25 stars; Ospreay took the IWGP US title "
                      "back at Forbidden Door that June. In 2026 the story inverted — Ospreay saved "
                      "Omega from his own faction at Redemption, then beat him for the AEW World "
                      "Championship at Wembley on August 30. Omega handed him the belt afterward."),
            dict(name="Jon Moxley", slug="jon-moxley",
                 desc="Enemy, then employer, then enemy again inside five months of 2026. Ospreay "
                      "returned from surgery attacking Moxley's Death Riders in March, lost a "
                      "Continental Championship challenge to him at Dynasty on April 12, joined the "
                      "group on July 1, and walked out on July 29 when Moxley ordered him to "
                      "suffocate Kenny Omega with a plastic bag."),
            dict(name="Kazuchika Okada", slug="kazuchika-okada",
                 desc="The man he turned on to found United Empire in October 2020, and a recurring "
                      "ceiling: Okada beat him in the G1 Climax 32 final in 2022 and again in the "
                      "Continental Classic final at Worlds End on December 28, 2024."),
            dict(name="Swerve Strickland",
                 desc="Beat Ospreay's first AEW World Championship challenge at Forbidden Door on "
                      "June 30, 2024; Ospreay returned the favor where it counted, beating him in "
                      "the Owen Hart Cup final on June 28, 2026 to earn the Wembley title shot."),
            dict(name="Bryan Danielson",
                 desc="One match, and it is the rating on his tombstone: Dynasty, April 21, 2024, "
                      "confirmed by Dave Meltzer at 6.5 stars — among the highest marks the Observer "
                      "has ever printed."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Profile",
        lead="Thin by design &mdash; the verified list is short, and nothing is added to pad it.",
        rows=[
            dict(when="2024&ndash;", title="On-record interviews", kind="Interviews",
                 desc="His neurodivergence (dyslexia and an ADHD diagnosis, per Wikipedia), his "
                      "reasons for choosing AEW over WWE — staying near his family in England — and, "
                      "in 2026, his own account of the neck-surgery timeline (POST Wrestling, March "
                      "16, 2026) are all documented in his own words."),
            dict(when="2025&ndash;", title="Alex Windsor", kind="Personal",
                 desc="Engaged to wrestler Alex Windsor since June 2025, per Wikipedia — who won the "
                      "AEW Women's World Tag Team Championship on the same August 30, 2026 Wembley "
                      "card where he won the world title."),
            dict(when="2026", title="The Death Riders arc as television", kind="Storyline",
                 desc="He has said in interviews (F4W/Wrestling Observer) that the Death Riders "
                      "storyline “gave my character an edge.” No film roles, autobiography or "
                      "documentary series could be verified, so none are listed."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated the way the sources actually state them.",
        stats=[
            ("54",  "Five-star matches"),
            ("6.5", "Meltzer peak"),
            ("919", "Day RevPro reign"),
        ],
        rows=[
            dict(name="AEW World Champion, August 30, 2026",
                 sub="Beat Kenny Omega in 34 minutes in the All In: London main event at Wembley — "
                     "his first reign, in his home country, one day old as this page is written."),
            dict(name="Most five-star matches in Wrestling Observer history: 54",
                 sub="Wikipedia's count of matches Dave Meltzer has rated five stars or higher. "
                     "Single-sourced to that tally, so treat the precise figure as reported; the "
                     "record itself is not in dispute."),
            dict(name="A confirmed 6.5-star match",
                 sub="vs. Bryan Danielson, AEW Dynasty, April 21, 2024 — confirmed in the Observer "
                     "at 6.5, among the highest ratings ever issued. He also had two five-star "
                     "matches on one night at Worlds End 2024, per Wikipedia only the fifth wrestler "
                     "to do it."),
            dict(name="First British IWGP World Heavyweight Champion",
                 sub="Sakura Genesis, April 4, 2021, beating Kota Ibushi. The reign ended by "
                     "vacation, not defeat, after 32 days — the neck injury that has shadowed the "
                     "whole career."),
            dict(name="Two-time Best of the Super Juniors winner (2016, 2019)",
                 sub="The 2016 win made him the youngest and first British winner; the 2019 final "
                     "against Shingo Takagi went 5.75 stars."),
            dict(name="919 days as RevPro British Heavyweight Champion",
                 sub="February 14, 2020 to August 21, 2022 — the longest reign in the title's "
                     "history, spanning the pandemic era."),
            dict(name="2026 Owen Hart Cup winner",
                 sub="Beat Swerve Strickland in the final at Forbidden Door on June 28, 2026, with a "
                     "Paradigm Shift, a Death Rider and a Tiger Driver — Death Riders-era offense, "
                     "two days before he officially joined them. It earned the All In title match."),
            dict(name="Never a G1 Climax winner",
                 sub="Worth stating because it is commonly assumed otherwise: he lost the 2022 final "
                     "to Kazuchika Okada and the 2023 final to Tetsuya Naito."),
            dict(name="Double-fusion neck surgery to world champion in under a year",
                 sub="Surgery September 17, 2025; cleared February 25, 2026; returned March 15; "
                     "champion August 30 — a 347-day round trip, computed from those verified dates."),
        ],
        footnote=("Deliberately absent: any career win-loss total (none verified), social handles "
                  "(not verified this pass), and a match row for the reported Forbidden Door 2025 "
                  "injury appearance, which was single-sourced. The 54 five-star count is "
                  "Wikipedia's figure."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="POST Wrestling", v="All In: London 2026 — Ospreay takes the title",
             href="https://www.postwrestling.com/2026/08/30/aew-all-in-london-2026-results-will-ospreay-takes-aew-world-title-off-rival-kenny-omega-at-wembley-stadium/"),
        dict(k="Fightful", v="All In 2026 full results",
             href="https://www.fightful.com/wrestling/aew-all-in-results-8-30-2026-kenny-omega-vs-will-ospreay-willow-nightingale-vs-mercedes-mone-more/"),
        dict(k="Wikipedia", v="Full biography",
             href="https://en.wikipedia.org/wiki/Will_Ospreay"),
        dict(k="POST Wrestling", v="Ospreay's own surgery-to-clearance timeline",
             href="https://www.postwrestling.com/2026/03/16/will-ospreay-shares-timeline-from-neck-surgery-to-clearance/"),
        dict(k="WrestleZone", v="Ospreay hands back the Death Riders patch",
             href="https://www.wrestlezone.com/news/1654755-will-ospreay-death-riders-badge-jon-moxley-aew-dynamite"),
        dict(k="Fox News", v="Owen Hart Cup win at Forbidden Door",
             href="https://www.foxnews.com/sports/ospreay-wins-owen-hart-mens-tournament-aew-forbidden-door-punches-ticket-title-shot"),
        dict(k="AEW", v="International Championship history",
             href="https://www.allelitewrestling.com/aew-international-championship-history"),
        dict(k="Web Is Jericho", v="The 6.5-star Danielson rating, confirmed",
             href="https://www.webisjericho.com/dave-meltzers-star-rating-for-will-ospreay-vs-bryan-danielson-has-been-confirmed/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Will Ospreay the AEW World Champion?",
            a="Yes. He beat Kenny Omega in the main event of All In: London at Wembley Stadium on "
              "August 30, 2026 &mdash; a 34-minute match &mdash; for his first AEW World Championship "
              "reign. He entered with United Empire allies Francesco Akira, HENARE and Callum Newman, "
              "and Omega handed him the belt afterward. It is his second world championship overall, "
              "after the IWGP World Heavyweight title in 2021.",
            q_ld="Is Will Ospreay the AEW World Champion?",
            a_ld="Yes. Will Ospreay defeated Kenny Omega in the main event of AEW All In: London at "
                 "Wembley Stadium on August 30, 2026 to win the AEW World Championship. It is his "
                 "first AEW World Championship reign and his second world title overall, after the "
                 "IWGP World Heavyweight Championship he won in April 2021."),
        dict(
            q="Did Ospreay lose the IWGP World Heavyweight Championship?",
            a="No &mdash; he never lost it in a match. He beat Kota Ibushi for it at Sakura Genesis "
              "on April 4, 2021, becoming the first British holder, and <b>vacated</b> it on May 20, "
              "2021 with a neck injury, 32 days in. The same neck required double-fusion surgery on "
              "September 17, 2025; he was cleared on February 25, 2026 and returned at Revolution on "
              "March 15.",
            q_ld="Did Will Ospreay ever lose the IWGP World Heavyweight Championship?",
            a_ld="No. Will Ospreay won the IWGP World Heavyweight Championship from Kota Ibushi at "
                 "Sakura Genesis on April 4, 2021 and vacated it on May 20, 2021 because of a neck "
                 "injury, after 32 days. He was never defeated for the title. The same neck later "
                 "required double-fusion surgery in September 2025."),
        dict(
            q="Was Ospreay really in the Death Riders?",
            a="For four weeks. He officially joined Jon Moxley&rsquo;s faction on the July 1, 2026 "
              "Dynamite &mdash; months after returning from surgery specifically to fight them "
              "&mdash; and quit on the July 29 Dynamite, handing his patch back after refusing "
              "Moxley&rsquo;s order at Redemption (July 26) to suffocate Kenny Omega with a plastic "
              "bag. The Death Riders were at ringside when he won the Owen Hart Cup final on June 28, "
              "and he used a Paradigm Shift and a Death Rider in that match.",
            q_ld="Was Will Ospreay a member of the Death Riders?",
            a_ld="Yes, briefly. Will Ospreay officially joined Jon Moxley's Death Riders on the July "
                 "1, 2026 episode of AEW Dynamite and left on the July 29, 2026 episode, handing his "
                 "faction patch back to Moxley. He quit after refusing Moxley's order at AEW "
                 "Redemption on July 26, 2026 to suffocate AEW World Champion Kenny Omega with a "
                 "plastic bag."),
        dict(
            q="Does Ospreay hold the record for five-star matches?",
            a="Yes, per Wikipedia&rsquo;s running tally: <b>54</b> matches rated five stars or "
              "higher by Dave Meltzer, the most of any wrestler in Observer history. His personal "
              "peak is the confirmed 6.5 for Bryan Danielson at Dynasty, April 21, 2024. Treat the "
              "precise count as reported rather than independently audited &mdash; but the record "
              "itself is not seriously contested.",
            q_ld="Does Will Ospreay hold the record for the most five-star matches?",
            a_ld="Yes. According to Wikipedia's tally, Will Ospreay has 54 matches rated five stars "
                 "or higher by Dave Meltzer of the Wrestling Observer Newsletter, the most of any "
                 "wrestler in history. His highest single rating is a confirmed 6.5 stars for his "
                 "match against Bryan Danielson at AEW Dynasty on April 21, 2024."),
        dict(
            q="Has Ospreay ever won the G1 Climax?",
            a="No. He reached two finals and lost both &mdash; to Kazuchika Okada in 2022 and "
              "Tetsuya Naito in 2023. His tournament wins are the Best of the Super Juniors (2016, "
              "2019), the 2021 New Japan Cup, and the 2026 Owen Hart Cup, which earned the Wembley "
              "title match.",
            q_ld="Has Will Ospreay ever won the G1 Climax?",
            a_ld="No. Will Ospreay has never won the G1 Climax; he lost the 2022 final to Kazuchika "
                 "Okada and the 2023 final to Tetsuya Naito. His major tournament wins are the Best "
                 "of the Super Juniors in 2016 and 2019, the New Japan Cup in 2021, and the Owen "
                 "Hart Cup in 2026."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="William Peter Charles Ospreay"),
        dict(label="Born", value="May 7, 1993", sub="London, England &middot; age 33"),
        dict(label="Billed from", value="London, England"),
        dict(label="Height", value="6&#8242;1&#8243;", sub="185 cm"),
        dict(label="Weight", value="220 lb", sub="100 kg (billed)"),
        dict(label="Debut", value="April 1, 2012", sub="British independents, as Dark Britannico"),
        dict(label="Trained by", value="London School of Lucha Libre"),
        dict(label="Signature", value="Hidden Blade &middot; Storm Breaker &middot; Os-Cutter "
                                      "&middot; Tiger Driver &rsquo;91",
             sub="The Os-Cutter defined the junior years; the Hidden Blade ends matches now"),
        dict(label="Current title", value="AEW World Championship",
             sub="Won August 30, 2026 at All In: London &mdash; first reign"),
        dict(label="Family", value="Engaged to Alex Windsor",
             sub="Since June 2025 per Wikipedia; she won AEW women&rsquo;s tag gold on the same "
                 "Wembley card"),
        dict(label="Also known as",
             value="The Aerial Assassin &middot; The Commonwealth Kingpin &middot; The Billy GOAT"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1993-05-07",
    bornplace="London, England",
    nationality="United Kingdom",
    height_cm=185,
    weight_kg=100,
    ld=dict(
        alternateName=["William Peter Charles Ospreay", "The Aerial Assassin",
                       "The Commonwealth Kingpin", "The Billy GOAT"],
        award=["AEW World Championship (1 reign, current, won August 30, 2026)",
               "IWGP World Heavyweight Championship (1 reign, 2021, first British holder)",
               "AEW International Championship (2 reigns)",
               "IWGP United States Championship (2 reigns)",
               "IWGP Junior Heavyweight Championship (3 reigns)",
               "NEVER Openweight Championship (1 reign)",
               "RevPro British Heavyweight Championship (1 reign, 919 days)",
               "Best of the Super Juniors winner (2016, 2019)",
               "New Japan Cup winner (2021)",
               "Owen Hart Cup winner (2026)",
               "Most five-star-rated matches in Wrestling Observer history (54)"],
        knowsAbout=["Professional wrestling", "High-flying wrestling", "New Japan Pro-Wrestling",
                    "All Elite Wrestling", "United Empire", "Revolution Pro Wrestling",
                    "British wrestling"],
        description="Will Ospreay is an English professional wrestler and the current AEW World "
                    "Champion, having defeated Kenny Omega at All In: London at Wembley Stadium on "
                    "August 30, 2026. A two-time Best of the Super Juniors winner and former IWGP "
                    "World Heavyweight Champion, he holds the record for the most matches rated "
                    "five stars or higher by the Wrestling Observer's Dave Meltzer, with a "
                    "confirmed 6.5-star match against Bryan Danielson in 2024.",
        sameAs=["https://en.wikipedia.org/wiki/Will_Ospreay",
                "https://www.allelitewrestling.com/aew-roster"],
    ),
)
