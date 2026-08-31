# -*- coding: utf-8 -*-
"""Tiffany Stratton - dossier data.

Sources: web research compiled August 31, 2026 - Wikipedia, TheSmackDownHotel,
Sports Illustrated, TJR Wrestling, Bleacher Report, Wrestling Inc and WWE.com show
pages, all opened during this pass. Every match row carries a day-precision date
from one of those sources.

Deliberate omissions:
  * No career win-loss total - none was verified.
  * No social links - handles were not verified in this pass.
  * The WWE Women's Championship reign length is printed as a live conflict:
    Wikipedia counts 302 days, Sports Illustrated's report of the losing night says
    301. Both are published; neither is silently adopted.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2023-05-28", promo="WWE", landmark=True,
         event="NXT Battleground", opponent="Lyra Valkyria",
         stip="Tournament final for the vacant title - champion in year two of her career",
         title="NXT Women's Championship"),
    dict(result="L", date="2023-09-12", promo="WWE", landmark=True,
         event="NXT - Orlando", opponent="Becky Lynch",
         stip="Singles - the 107-day reign ends", title="NXT Women's Championship"),
    dict(result="W", date="2024-07-06", promo="WWE", type="tag", landmark=True,
         event="Money in the Bank - Toronto", opponent="The 2024 women's ladder match field",
         stip="Wins the briefcase", title=""),
    dict(result="W", date="2025-01-03", promo="WWE", landmark=True,
         event="SmackDown", opponent="Nia Jax",
         stip="Money in the Bank cash-in - first world title",
         title="WWE Women's Championship"),
    dict(result="W", date="2025-04-19", promo="WWE", landmark=True,
         event="WrestleMania 41 Night 1", opponent="Charlotte Flair",
         stip="Singles - retains over the 14-time champion in her first WrestleMania title match",
         title="WWE Women's Championship"),
    dict(result="W", date="2025-06-27", promo="WWE",
         event="SmackDown", opponent="Nia Jax",
         stip="Last Woman Standing - retains", title="WWE Women's Championship"),
    dict(result="W", date="2025-07-13", promo="WWE",
         event="Evolution", opponent="Trish Stratus",
         stip="Singles - retains over the Hall of Famer", title="WWE Women's Championship"),
    dict(result="W", date="2025-08-02", promo="WWE",
         event="SummerSlam Night 1", opponent="Jade Cargill",
         stip="Singles - retains over the Queen of the Ring", title="WWE Women's Championship"),
    dict(result="L", date="2025-10-11", promo="WWE",
         event="Crown Jewel - Perth", opponent="Stephanie Vaquer",
         stip="Champion vs. champion", title="WWE Women's Crown Jewel Championship"),
    dict(result="L", date="2025-11-01", promo="WWE", landmark=True,
         event="Saturday Night's Main Event XLI - Salt Lake City", opponent="Jade Cargill",
         stip="Singles - the 301- or 302-day reign ends on a worked-over knee",
         title="WWE Women's Championship"),
    dict(result="L", date="2026-01-31", promo="WWE", type="tag",
         event="Royal Rumble match - Riyadh", opponent="The 2026 women's Royal Rumble field",
         stip="Runner-up - last eliminated, by winner Liv Morgan", title=""),
    dict(result="L", date="2026-02-28", promo="WWE", type="tag",
         event="Elimination Chamber", opponent="The 2026 women's Chamber field",
         stip="Final competitor eliminated, by Rhea Ripley", title=""),
    dict(result="W", date="2026-04-24", promo="WWE", landmark=True,
         event="SmackDown", opponent="Giulia",
         stip="Singles - first woman to add this belt to a world and NXT title",
         title="WWE Women's United States Championship"),
    dict(result="L", date="2026-08-02", promo="WWE", type="tag",
         event="SummerSlam Night 2", opponent="Chelsea Green, Charlotte Flair, Jade Cargill, Lash Legend",
         stip="Five-way ladder match - Green won", title="Interim WWE Women's Championship"),
    dict(result="L", date="2026-08-14", promo="WWE", landmark=True,
         event="SmackDown", opponent="Jacy Jayne",
         stip="Singles - Rolling Encore ends the 112-day reign",
         title="WWE Women's United States Championship"),
    dict(result="L", date="2026-08-28", promo="WWE", type="tag",
         event="SmackDown", opponent="The Irresistible Forces",
         stip="With Chelsea Green - Nia Jax wins with an inside cradle", title=""),
]

DATA = dict(
    slug="tiffany-stratton",
    name="Tiffany Stratton",
    realname="Jessica Lynn Woynilko",
    epithet="The Buff Barbie",
    hook="Record & Titles",

    meta_desc=("Tiffany Stratton, The Buff Barbie, held the WWE Women's Championship for over 300 "
               "days from a Money in the Bank cash-in, plus NXT and Women's United States gold. Full "
               "record, titles, factions and career."),
    og_desc=("The Buff Barbie: a 300-plus-day WWE Women's Championship reign, the 2024 briefcase, "
             "NXT and US titles - all before turning 28. Full record, titles and career."),
    tw_desc="The Buff Barbie: 300+ days as WWE Women's Champion, plus NXT and Women's US gold.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2021",
    height_imp="5&#8242;7&#8243;",
    weight_lb="143",
    world_titles="1",
    vitals_tagline="It's Tiffy Time",
    support_note="Merch &middot; Games &middot; Watch",
    sp_items=[
        dict(ic="TS", title="Tiffany Stratton Merch", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable in the current 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="SD", title="SmackDown", sub="Fridays - her home show",
             tag="Watch", href="https://www.wwe.com/shows/smackdown"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/tiffany-stratton"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Tiffy Time &middot; The Center of the Universe &middot; ex-elite trampolinist",
    hero_tag="Prior Lake, Minnesota &middot; <em>NXT &middot; WWE &middot; 2021&ndash;present</em>",
    now_label="NOW",
    now_bold="SmackDown, no championship",
    now_tail=" &middot; dropped the Women's US title to Jacy Jayne on August 14 and is fighting The "
             "Irresistible Forces and Fatal Influence alongside interim champion Chelsea Green",
    hstats=[
        dict(value="302",  x=False, label="Day Title Reign (or 301)"),
        dict(value="1",    x=True,  label="World Title"),
        dict(value="2024", x=False, label="Miss Money in the Bank"),
        dict(value="112",  x=False, label="Day US Title Reign"),
    ],
    ghost_link="From elite trampolining to a 300-day world title reign in under four years",
    vlabel="Est. 2021 &middot; Prior Lake, Minnesota",
    mono="TS",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Tiffany Stratton</b> compressed a decade of career into four years. Signed August 30, "
        "2021 with no wrestling background beyond elite trampoline gymnastics, she was NXT Women's "
        "Champion inside two years, Miss Money in the Bank inside three, and WWE Women's Champion "
        "inside three and a half &mdash; a reign that ran more than <b>300 days</b> across all of "
        "2025 and beat back Nia Jax, Charlotte Flair at WrestleMania, Trish Stratus and Jade Cargill. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">302</span>'
        '<span class="pull-cap">days as WWE Women&rsquo;s Champion per Wikipedia &mdash; Sports Illustrated counts 301; both endpoints are January 3 and November 1, 2025</span></span>'
        "In April 2026 she added the Women's United States Championship, becoming the first woman to "
        "put that belt next to world and NXT gold. As of August 31, 2026 she holds nothing &mdash; "
        "and the story of her year is how quickly the division she ruled turned into a gauntlet.",

        "Her defining number needs a flag. Wikipedia counts the WWE Women's Championship reign at "
        "<b>302 days</b>; Sports Illustrated's report of the night she lost counted <b>301</b>. Both "
        "agree on the endpoints &mdash; the cash-in on Nia Jax on the January 3, 2025 SmackDown, and "
        "the loss to Jade Cargill at Saturday Night's Main Event XLI on November 1, 2025 &mdash; and "
        "the day-count arithmetic between those dates gives 302, so the discrepancy is a counting "
        "convention, not a factual dispute. Both figures are printed here rather than one being "
        "silently adopted. Either way it was the longest women's reign in the company at the time it "
        "ended, and it ended on a knee that Cargill had softened up with a backstage attack the week "
        "before &mdash; the heel turn that ran through WrestleMania 42 season.",

        "She was born Jessica Lynn Woynilko on May 1, 1999 in Prior Lake, Minnesota, and was an "
        "elite-level trampoline gymnast until an undiagnosed stress fracture ended that career in "
        "2017. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig pull-fig--sm">2021</span>'
        '<span class="pull-cap">the year she first wrestled &mdash; trained by Greg Gagne before WWE signed her that August</span></span>'
        "Trained by Greg Gagne, she signed in August 2021, debuted on 205 Live that November, and "
        "worked NXT as a rich-girl heel built on Paris Hilton and Sharpay Evans references &mdash; "
        "with the gymnastics repurposed into the Prettiest Moonsault Ever, the finisher that still "
        "closes her matches. She beat Lyra Valkyria in a tournament final at NXT Battleground on May "
        "28, 2023 for the vacant NXT Women's Championship, held it 107 days, and lost it to a "
        "main-roster raider: Becky Lynch, on the September 12, 2023 NXT.",

        "2026 has been the hard year. She entered the Royal Rumble and finished runner-up, last "
        "eliminated by winner Liv Morgan; she was the final woman eliminated from the Elimination "
        "Chamber, by Rhea Ripley; and her consolation run with the Women's United States Championship "
        "&mdash; won from Giulia on the April 24 SmackDown &mdash; ended at 112 days on August 14, "
        "when Fatal Influence's Jacy Jayne pinned her with the Rolling Encore while Stratton was "
        "distracted trying to protect Chelsea Green. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">112</span>'
        '<span class="pull-cap">days as Women&rsquo;s United States Champion, April 24 to August 14, 2026 &mdash; the first woman to hold US, world and NXT titles</span></span>'
        "She lost the SummerSlam interim-title ladder match on August 2 &mdash; created because "
        "champion Rhea Ripley's knee surgery froze the WWE Women's Championship &mdash; and has "
        "spent August tag-partnered with interim champion Chelsea Green against Nia Jax and Lash "
        "Legend's Irresistible Forces, dropping decisions to Lash Legend on August 21 and to the "
        "Forces on August 28. She is title-less, face, popular, and plainly being rebuilt toward "
        "another shot.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Highlight set",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("302",      "Day title reign (or 301)"),
            ("1&times;", "WWE Women's Championship"),
            ("1&times;", "NXT Women's Championship"),
            ("1&times;", "Women's US Championship"),
            ("2024",     "Money in the Bank"),
            ("2nd",      "2026 Rumble - runner-up"),
        ],
        lead=("Sixteen documented bouts - a highlight subset, not a career count, and heavier on "
              "2025-26 than any page like this usually is, because that is where the career has "
              "happened. No career win-loss total is published because none was verified. The "
              "November 1, 2025 row carries the reign-length conflict on its face: 302 days per "
              "Wikipedia, 301 per Sports Illustrated. Filter by match type, tap any column header to "
              "sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("Three bouts that define the run so far. No star ratings are printed because "
                    "none were verified in this pass."),
    signature=[
        dict(rating="—", event="WrestleMania 41 Night 1", opponent="Charlotte Flair",
             stip="WWE Women's Championship — retained over the 14-time world champion"),
        dict(rating="—", event="SmackDown, January 3, 2025", opponent="Nia Jax",
             stip="Money in the Bank cash-in — the start of the 300-day reign"),
        dict(rating="—", event="Evolution 2025", opponent="Trish Stratus",
             stip="WWE Women's Championship — champion vs. Hall of Famer at the all-women PLE"),
    ],
    signature_count_word="three",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("1&times;", "WWE Women's Championship"),
            ("302",      "Days held (301 per SI)"),
            ("1st",      "Woman with US + world + NXT"),
            ("2024",     "Miss Money in the Bank"),
        ],
        lead=("Three championships and a briefcase in a career that only started in 2021 - every one "
              "of them won on SmackDown or NXT television rather than at a stadium show, which is its "
              "own kind of statement about how WWE has used her."),
        rows=[
            dict(ic="W", name="WWE Women's Championship", count="1",
                 sub="January 3 &ndash; November 1, 2025 &middot; won by Money in the Bank cash-in on "
                     "Nia Jax on SmackDown, lost to Jade Cargill at Saturday Night&rsquo;s Main Event "
                     "XLI &middot; <b>302 days per Wikipedia, 301 per Sports Illustrated</b> &middot; "
                     "defences included Bayley, Nia Jax three times, Charlotte Flair at WrestleMania "
                     "41, Trish Stratus at Evolution and Jade Cargill at SummerSlam"),
            dict(ic="U", name="WWE Women's United States Championship", count="1",
                 sub="April 24 &ndash; August 14, 2026 &middot; won from Giulia on SmackDown, lost to "
                     "Jacy Jayne on SmackDown &middot; <b>112 days</b> &middot; defences against "
                     "Kiana James (May 8) and Lash Legend (May 22) &middot; the first woman to hold "
                     "this belt alongside prior world and NXT titles"),
            dict(ic="N", name="NXT Women's Championship", count="1",
                 sub="May 28 &ndash; September 12, 2023 &middot; won the vacant title over Lyra "
                     "Valkyria in a tournament final at NXT Battleground, lost to Becky Lynch in "
                     "Orlando &middot; <b>107 days</b>, in her second year as a wrestler"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Alliances",
        lead="She has never been in a booked stable - her career is singles all the way down, which "
             "makes the current tag alliance the outlier worth explaining.",
        cards=[
            dict(era="NXT &amp; WWE &middot; 2021&ndash;2025 &middot; no faction",
                 name="The solo act",
                 members="Tiffany Stratton",
                 desc="From 205 Live through the entire 300-day championship reign she worked without "
                      "a unit, a manager or a regular partner - unusual for a champion in this era, "
                      "and the reason her title defences were booked as her against the field."),
            dict(era="WWE &middot; 2026 &middot; alliance, not a stable",
                 name="With Chelsea Green",
                 members="Tiffany Stratton, Chelsea Green",
                 desc="Forged in the interim-title era: Green won the SummerSlam ladder match "
                      "Stratton was in, then saved her from a post-match beating by The Irresistible "
                      "Forces with a kendo stick on the August 21 SmackDown. They have since tagged "
                      "against the Forces - losing on August 28 - and Stratton's attempt to protect "
                      "Green mid-match on August 14 is what cost her the US title to Jacy Jayne. An "
                      "alliance of circumstance against two heel units, Fatal Influence and The "
                      "Irresistible Forces, that outnumber either of them."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One name, one gimmick, tuned twice.",
        cards=[
            dict(mono="DG", era="NXT &middot; 2021&ndash;2023", name="The daddy's girl",
                 desc="The debut character: a wealthy, spoiled gymnast built openly on Paris Hilton "
                      "and Sharpay Evans references, with the trampoline pedigree doing the athletic "
                      "heavy lifting. It won the NXT Women's Championship in year two."),
            dict(mono="BB", era="WWE &middot; 2023&ndash;2025", name="The Buff Barbie",
                 desc="The main-roster refinement - same vanity, more menace, and the catchphrase "
                      "economy of Tiffy Time. The 2024 briefcase and the January 2025 cash-in were "
                      "both executed in this register, as a heel the crowd increasingly refused to "
                      "boo."),
            dict(mono="FC", era="WWE &middot; 2025&ndash;present", name="The fan favourite",
                 desc="Turned face in early 2025 after Charlotte Flair's post-Rumble attack, and "
                      "carried the WWE Women's Championship as SmackDown's ace babyface for the rest "
                      "of the reign. The 2026 version is the same character with the gold stripped "
                      "away - which WWE is visibly using as the setup for the next chase."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Trampoline to the top of SmackDown in four years flat.",
        rows=[
            dict(year="2017", title="Gymnastics ends",
                 desc="An undiagnosed stress fracture in her foot ends an elite trampoline career; "
                      "her parents point her toward wrestling and Greg Gagne trains her."),
            dict(year="2021", title="Signs with WWE",
                 desc="Signs August 30, 2021; debuts on 205 Live that November 16 and on NXT "
                      "television December 28."),
            dict(year="2023", title="NXT Women's Champion",
                 desc="Beats Lyra Valkyria in a tournament final at NXT Battleground on May 28 for "
                      "the vacant title; loses it to Becky Lynch on September 12 after 107 days."),
            dict(year="2024", title="Miss Money in the Bank",
                 desc="Wins the women's ladder match in Toronto on July 6 and carries the briefcase "
                      "to the main roster's front rank."),
            dict(year="2025", title="The 300-day reign",
                 desc="Cashes in on Nia Jax on the January 3 SmackDown, turns face within weeks, and "
                      "retains against Bayley, Jax repeatedly, Charlotte Flair at WrestleMania 41, "
                      "Trish Stratus at Evolution and Jade Cargill at SummerSlam. Cargill turns heel, "
                      "attacks her on October 24, and takes the title at Saturday Night's Main Event "
                      "on November 1."),
            dict(year="2026", title="Near-misses, a US title, and a rebuild",
                 desc="Royal Rumble runner-up on January 31, last woman out of the Elimination "
                      "Chamber on February 28; wins the Women's US Championship from Giulia on April "
                      "24 and holds it 112 days; loses the SummerSlam interim-title ladder match on "
                      "August 2 and the US title to Jacy Jayne on August 14; allies with Chelsea "
                      "Green against The Irresistible Forces and Fatal Influence through late "
                      "August."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who she went to war with.",
        cards=[
            dict(name="Nia Jax",
                 desc="The load-bearing rivalry of the reign: Stratton cashed in on her, then beat "
                      "her by DQ in February, clean in May, and in a Last Woman Standing match on "
                      "June 27, 2025. Jax has kept the receipts - The Irresistible Forces' beatdowns "
                      "in August 2026, including the pre-match attack that softened Stratton up for "
                      "the Jacy Jayne title loss, are the same feud carried on by a tag team."),
            dict(name="Jade Cargill", slug="jade-cargill",
                 desc="The rivalry that book-ended the reign. Stratton beat her clean at SummerSlam "
                      "on August 2, 2025; Cargill turned heel, attacked her backstage on October 24, "
                      "and took the championship at Saturday Night's Main Event on November 1, "
                      "working the injured knee the whole match. They met again in the SummerSlam "
                      "2026 ladder match, where Cargill was one of the four she didn't beat."),
            dict(name="Charlotte Flair", slug="charlotte-flair",
                 desc="The torch-passing match: WrestleMania 41 Night 1, April 19, 2025, Stratton "
                      "retaining over the 14-time world champion in her first WrestleMania title "
                      "defence - the result that legitimised the reign. Flair's post-Rumble attack "
                      "that February is also what turned Stratton face."),
            dict(name="Becky Lynch", slug="becky-lynch",
                 desc="Brief and formative: Lynch came down from the main roster and took the NXT "
                      "Women's Championship from her on September 12, 2023 - a loss to a legend that "
                      "did more for Stratton's standing than most wins. They have not run it back "
                      "with the roles reversed."),
            dict(name="Fatal Influence",
                 desc="The current problem: Jacy Jayne took the US title from her on August 14, 2026 "
                      "with the Rolling Encore while Fallon Henley and the unit worked the numbers, "
                      "and the same group holds the Women's Tag Team Championship. Stratton's August "
                      "has been spent fighting a two-front war against them and The Irresistible "
                      "Forces with only Chelsea Green alongside."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Thin by design - the career is four years old and the verified list is short.",
        rows=[
            dict(when="2024&ndash;", title="WWE 2K", kind="Game",
                 desc="A playable fixture of the current WWE 2K series. Her exact debut entry was "
                      "not verified in this pass, so no year is claimed for it."),
            dict(when="2024", title="Tiffy Time, by def rebel", kind="Music",
                 desc="Her entrance theme since February 2024, per TheSmackDownHotel - the "
                      "catchphrase set to music."),
            dict(when="2016&ndash;2017", title="Elite trampoline gymnastics", kind="Sport",
                 desc="Competed at elite level before the 2017 foot injury - the background the "
                      "Prettiest Moonsault Ever converts into offense. No film, television or book "
                      "credits could be verified, so none are listed."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated the way the sources state them - including the one-day counting "
             "conflict at the centre of her resume.",
        stats=[
            ("302", "Days as champion (or 301)"),
            ("112", "Days as US Champion"),
            ("4",   "Years, debut to all of it"),
        ],
        rows=[
            dict(name="A 300-plus-day WWE Women's Championship reign",
                 sub="January 3 to November 1, 2025 - 302 days by Wikipedia's count and by plain "
                     "date arithmetic, 301 by Sports Illustrated's report of the losing night. The "
                     "endpoints are not in dispute; the convention is. Both figures are printed."),
            dict(name="Cash-in champion who kept the belt",
                 sub="Her Money in the Bank cash-in - on Nia Jax, mid-SmackDown, January 3, 2025 - "
                     "opened a reign that ran ten months, against the pattern of briefcase reigns "
                     "measured in weeks."),
            dict(name="First woman to hold the Women's US title after world and NXT gold",
                 sub="Won from Giulia on April 24, 2026, 112 days. Athlon Sports framed the win as "
                     "historic on those grounds; the precise first-woman phrasing is theirs."),
            dict(name="Retained over Charlotte Flair at WrestleMania 41",
                 sub="April 19, 2025, Night 1 - a fourth-year wrestler beating the 14-time world "
                     "champion in her first WrestleMania championship match."),
            dict(name="2026 Royal Rumble runner-up",
                 sub="Last woman eliminated on January 31, 2026, by winner Liv Morgan - followed a "
                     "month later by being the last eliminated from the Elimination Chamber, by Rhea "
                     "Ripley. The two near-misses define her 2026 as sharply as the titles defined "
                     "her 2025."),
            dict(name="NXT Women's Champion in year two of her career",
                 sub="May 28, 2023, roughly eighteen months after her first televised match - among "
                     "the fastest championship arcs of the modern developmental system."),
        ],
        footnote=("No career win-loss total is published - none was verified. Social handles are "
                  "omitted as unverified. Billed height and weight (5'7\", 143 lb) are "
                  "TheSmackDownHotel's figures. Her PWI Women's 250 ranking of No. 4 in 2025 is "
                  "Wikipedia's; no 2026 list placement was available as of August 31, 2026."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Tiffany_Stratton"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/tiffany-stratton"),
        dict(k="SmackDown Hotel", v="Profile and vitals",
             href="https://www.thesmackdownhotel.com/wrestlers/tiffany-stratton"),
        dict(k="Sports Illustrated", v="The November 1, 2025 title loss to Jade Cargill",
             href="https://www.si.com/fannation/wrestling/wwe/jade-cargill-dominates-tiffany-stratton-to-win-wwe-women-championship"),
        dict(k="TJR Wrestling", v="The August 14, 2026 US title loss to Jacy Jayne",
             href="https://tjrwrestling.net/news/breaking-tiffany-strattons-wwe-womens-u-s-title-reign-ends-on-smackdown/"),
        dict(k="Bleacher Report", v="SummerSlam 2026 interim-title ladder match",
             href="https://bleacherreport.com/articles/25460215-chelsea-green-wins-interim-wwe-womens-title-ladder-match-summerslam-after-ripleys-injury"),
        dict(k="WWE.com", v="SmackDown results, August 28, 2026",
             href="https://www.wwe.com/shows/smackdown/2026-08-28"),
        dict(k="Wrestling Inc", v="Chelsea Green injury and interim title status",
             href="https://www.wrestlinginc.com/2237183/wwe-chelsea-green-title-status-injury/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Tiffany Stratton a champion right now?",
            a="No. As of August 31, 2026 she holds nothing. She lost the WWE Women's United States "
              "Championship to <b>Jacy Jayne</b> on the August 14 SmackDown after 112 days, having "
              "already lost the SummerSlam five-way ladder match for the interim WWE Women's "
              "Championship on August 2, which Chelsea Green won. She is on SmackDown, allied with "
              "Green against The Irresistible Forces and Fatal Influence &mdash; and on the wrong "
              "end of the August results, dropping falls to Lash Legend on August 21 and the Forces "
              "on August 28.",
            q_ld="Is Tiffany Stratton a champion right now?",
            a_ld="No. As of August 31, 2026 Tiffany Stratton holds no championship. She lost the WWE "
                 "Women's United States Championship to Jacy Jayne on the August 14, 2026 SmackDown "
                 "after 112 days, and earlier lost the SummerSlam five-way ladder match for the "
                 "interim WWE Women's Championship, won by Chelsea Green on August 2, 2026. She is "
                 "allied with Chelsea Green against The Irresistible Forces and Fatal Influence on "
                 "SmackDown."),
        dict(
            q="How long was Tiffany Stratton WWE Women's Champion - 301 or 302 days?",
            a="Both numbers are in print. The endpoints are agreed everywhere: she cashed in Money "
              "in the Bank on Nia Jax on the <b>January 3, 2025</b> SmackDown and lost to Jade "
              "Cargill at Saturday Night's Main Event XLI on <b>November 1, 2025</b>. Wikipedia "
              "counts that as <b>302 days</b>, which matches plain date arithmetic; Sports "
              "Illustrated's report of the losing night said <b>301</b>. It is a counting "
              "convention, not a factual dispute, and this page prints both rather than adopting "
              "one.",
            q_ld="How long was Tiffany Stratton's WWE Women's Championship reign?",
            a_ld="Tiffany Stratton held the WWE Women's Championship from January 3, 2025, when she "
                 "cashed in her Money in the Bank contract on Nia Jax on SmackDown, until November "
                 "1, 2025, when Jade Cargill beat her at Saturday Night's Main Event XLI. Wikipedia "
                 "counts the reign at 302 days, which matches the date arithmetic, while Sports "
                 "Illustrated counted 301 days. The endpoints are not in dispute."),
        dict(
            q="Why is there an interim WWE Women's Championship, and where does Stratton fit?",
            a="Because champion <b>Rhea Ripley</b> tore a meniscus and had knee surgery, and could "
              "not be cleared for SummerSlam. WWE put an interim title on the line in a five-way "
              "ladder match on Night 2, August 2, 2026 &mdash; Stratton, Chelsea Green, Charlotte "
              "Flair, Jade Cargill and Lash Legend &mdash; which Green won; Green then broke an "
              "orbital bone within weeks but kept the belt. The interim champion is expected to "
              "face Ripley in a unification match; Ripley is projected back around the Royal "
              "Rumble. Stratton qualified for the ladder match by beating Jacy Jayne &mdash; the "
              "woman who then took her US title twelve days later.",
            q_ld="Why does WWE have an interim Women's Championship in 2026?",
            a_ld="WWE created an interim WWE Women's Championship because champion Rhea Ripley tore "
                 "her meniscus and had knee surgery, leaving her unable to compete at SummerSlam "
                 "2026. Chelsea Green won the interim title in a five-way ladder match over Tiffany "
                 "Stratton, Charlotte Flair, Jade Cargill and Lash Legend on August 2, 2026, and is "
                 "expected to face Ripley in a unification match when Ripley returns, projected "
                 "around the 2027 Royal Rumble."),
        dict(
            q="What is Tiffany Stratton's background before wrestling?",
            a="Elite trampoline gymnastics. Born Jessica Lynn Woynilko in Prior Lake, Minnesota on "
              "May 1, 1999, she competed at elite level until an undiagnosed stress fracture in her "
              "foot ended the gymnastics career in 2017. Her parents steered her to wrestling, Greg "
              "Gagne trained her, and WWE signed her on August 30, 2021 &mdash; the Prettiest "
              "Moonsault Ever is the gymnastics converted directly into a finisher.",
            q_ld="What was Tiffany Stratton's athletic background before WWE?",
            a_ld="Tiffany Stratton, born Jessica Lynn Woynilko on May 1, 1999 in Prior Lake, "
                 "Minnesota, was an elite-level trampoline gymnast until an undiagnosed stress "
                 "fracture in her foot ended that career in 2017. She was trained for wrestling by "
                 "Greg Gagne and signed with WWE on August 30, 2021. Her finisher, the Prettiest "
                 "Moonsault Ever, draws directly on her gymnastics background."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Jessica Lynn Woynilko"),
        dict(label="Born", value="May 1, 1999", sub="Prior Lake, Minnesota &middot; age 27"),
        dict(label="Billed from", value="Prior Lake, Minnesota"),
        dict(label="Height", value="5&#8242;7&#8243;", sub="170 cm"),
        dict(label="Weight", value="143 lb", sub="65 kg per SmackDown Hotel"),
        dict(label="Signed", value="August 30, 2021",
             sub="205 Live debut November 16; NXT TV from December 28"),
        dict(label="Trained by", value="Greg Gagne", sub="then the WWE Performance Center system"),
        dict(label="Background", value="Elite trampoline gymnastics", sub="ended by injury, 2017"),
        dict(label="Finisher", value="Prettiest Moonsault Ever",
             sub="rope-assisted double-jump moonsault"),
        dict(label="Theme", value="Tiffy Time", sub="by def rebel, since February 2024"),
        dict(label="Brand", value="SmackDown"),
        dict(label="Also known as", value="The Buff Barbie &middot; The Center of the Universe"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1999-05-01",
    bornplace="Prior Lake, Minnesota, United States",
    nationality="United States",
    height_cm=170,
    weight_kg=65,
    ld=dict(
        alternateName=["Jessica Lynn Woynilko", "The Buff Barbie", "The Center of the Universe"],
        award=["WWE Women's Championship (1 reign, 302 days per Wikipedia, 301 per Sports Illustrated)",
               "WWE Women's United States Championship (1 reign, 112 days)",
               "NXT Women's Championship (1 reign, 107 days)",
               "Women's Money in the Bank winner (2024)",
               "Women's Royal Rumble runner-up (2026)",
               "Pro Wrestling Illustrated Women's 250 No. 4 (2025)"],
        knowsAbout=["Professional wrestling", "WWE", "Women's professional wrestling",
                    "Trampoline gymnastics", "Championship wrestling"],
        description="Tiffany Stratton, born Jessica Lynn Woynilko, is an American professional "
                    "wrestler signed to WWE. A former elite trampoline gymnast trained by Greg "
                    "Gagne, she won the NXT Women's Championship in 2023, the women's Money in the "
                    "Bank ladder match in 2024, and the WWE Women's Championship by cash-in on "
                    "January 3, 2025, holding it just over 300 days with defences against Charlotte "
                    "Flair, Trish Stratus, Nia Jax and Jade Cargill. In 2026 she held the WWE "
                    "Women's United States Championship for 112 days and finished runner-up in the "
                    "Royal Rumble.",
        sameAs=["https://en.wikipedia.org/wiki/Tiffany_Stratton",
                "https://www.wwe.com/superstars/tiffany-stratton"],
    ),
)
