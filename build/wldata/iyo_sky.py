# -*- coding: utf-8 -*-
"""Iyo Sky - dossier data.

Sources: web research compiled August 31, 2026 - Wikipedia, Yahoo Sports, POST
Wrestling, F4W/WON, Fightful, TheSmackDownHotel and WWE.com show pages, all opened
during this pass. Every match row carries a day-precision date from one of those
sources. Stardom-era rows are limited to reign endpoints Wikipedia dates precisely;
opponents are only listed where verified, so several famous Stardom bouts are absent
rather than half-remembered.

Deliberate omissions:
  * No career win-loss total - none was verified.
  * No social links - handles were not verified in this pass.
  * Her exact birthplace within Japan is not published here because sources give
    only "Japan"; nothing more precise is invented.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="L", date="2016-07-24", promo="STARDOM",
         event="Stardom, Korakuen Hall", opponent="Toni Storm",
         stip="Singles - ends her run as inaugural champion after three defences",
         title="SWA World Championship"),
    dict(result="L", date="2018-10-28", promo="WWE", landmark=True,
         event="Evolution", opponent="Toni Storm",
         stip="Mae Young Classic 2018 final, as Io Shirai", title=""),
    dict(result="W", date="2020-06-07", promo="WWE", landmark=True,
         event="NXT TakeOver: In Your House", opponent="Charlotte Flair & Rhea Ripley",
         stip="Triple threat - wins the title from Flair",
         title="NXT Women's Championship"),
    dict(result="L", date="2021-04-07", promo="WWE", landmark=True,
         event="NXT TakeOver: Stand & Deliver", opponent="Raquel Gonzalez",
         stip="Singles - the 304-day reign ends", title="NXT Women's Championship"),
    dict(result="W", date="2022-09-12", promo="WWE", type="tag",
         event="Raw", opponent="Raquel Rodriguez & Aliyah",
         stip="With Dakota Kai - Damage CTRL's first gold",
         title="WWE Women's Tag Team Championship"),
    dict(result="W", date="2023-07-01", promo="WWE", type="tag", landmark=True,
         event="Money in the Bank - London", opponent="The 2023 women's ladder match field",
         stip="Wins the briefcase", title=""),
    dict(result="W", date="2023-08-05", promo="WWE", landmark=True,
         event="SummerSlam - Detroit", opponent="Bianca Belair",
         stip="Money in the Bank cash-in - first main-roster world title",
         title="WWE Women's Championship"),
    dict(result="L", date="2024-04-07", promo="WWE", landmark=True,
         event="WrestleMania XL Night 2", opponent="Bayley",
         stip="Singles - the 246-day reign ends", title="WWE Women's Championship"),
    dict(result="W", date="2025-03-03", promo="WWE", landmark=True,
         event="Raw", opponent="Rhea Ripley",
         stip="Singles - second main-roster world title", title="Women's World Championship"),
    dict(result="W", date="2025-04-20", promo="WWE", landmark=True,
         event="WrestleMania 41 Night 2", opponent="Rhea Ripley & Bianca Belair",
         stip="Triple threat - the first women's match in WWE rated five stars by Dave Meltzer",
         title="Women's World Championship"),
    dict(result="L", date="2025-07-13", promo="WWE", landmark=True,
         event="Evolution", opponent="Naomi",
         stip="Money in the Bank cash-in - the 132-day reign ends",
         title="Women's World Championship"),
    dict(result="W", date="2026-01-05", promo="WWE", type="tag",
         event="Raw - New York", opponent="The Kabuki Warriors",
         stip="With Rhea Ripley, as RHIYO", title="WWE Women's Tag Team Championship"),
    dict(result="L", date="2026-02-27", promo="WWE", type="tag",
         event="SmackDown - Louisville", opponent="The Irresistible Forces",
         stip="With Rhea Ripley - the 53-day reign ends",
         title="WWE Women's Tag Team Championship"),
    dict(result="W", date="2026-06-27", promo="WWE", landmark=True,
         event="Night of Champions - Riyadh", opponent="Liv Morgan",
         stip="Queen of the Ring final - Spanish Fly and Over the Moonsault", title=""),
    dict(result="L", date="2026-08-01", promo="WWE", landmark=True,
         event="SummerSlam Night 1 - Minneapolis", opponent="Liv Morgan",
         stip="Singles - challenge; hurt her knee mid-match, pinned at 13:35",
         title="Women's World Championship"),
    dict(result="W", date="2026-08-10", promo="WWE", type="tag",
         event="Raw", opponent="Raquel Rodriguez & Roxanne Perez",
         stip="With Sol Ruca, against The Judgment Day", title=""),
]

DATA = dict(
    slug="iyo-sky",
    name="Iyo Sky",
    realname="Masami Odate",
    epithet="The Genius of the Sky",
    hook="Record & Titles",

    meta_desc=("Iyo Sky, The Genius of the Sky, is a two-time WWE world champion, a two-time World of "
               "Stardom Champion, the 2026 Queen of the Ring, and half of the first five-star women's "
               "match in WWE history. Full record, titles, factions and career."),
    og_desc=("The Genius of the Sky: world titles on two continents, the first five-star women's match "
             "in WWE history, and the 2026 Queen of the Ring crown. Full record, titles and career."),
    tw_desc="The Genius of the Sky: WWE and Stardom world titles, and WWE's first women's five-star match.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2007",
    height_imp="5&#8242;1&#8243;",
    weight_lb="119",
    world_titles="2",
    vitals_tagline="The Genius of the Sky",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="IS", title="Iyo Sky Merch", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable in the current 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="SD", title="Stardom", sub="The promotion she was Ace of, 2011-2018",
             tag="Visit", href="https://en.wikipedia.org/wiki/World_Wonder_Ring_Stardom"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/iyo-sky"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Io Shirai &middot; The Ace of Stardom &middot; Damage CTRL &middot; RHIYO",
    hero_tag="Japan &middot; <em>Stardom &middot; NXT &middot; WWE &middot; 2007&ndash;present</em>",
    now_label="NOW",
    now_bold="Raw, no championship",
    now_tail=" &middot; came up short against Liv Morgan at SummerSlam on a hurt knee, and has since "
             "taken Sol Ruca's side against The Judgment Day",
    hstats=[
        dict(value="2",    x=True,  label="WWE World Titles"),
        dict(value="246",  x=False, label="Day WWE Women's Reign"),
        dict(value="5.0",  x=False, label="First WWE women's 5-star"),
        dict(value="2026", x=False, label="Queen of the Ring"),
    ],
    ghost_link="From a Team Makehen trainee in 2007 to world champion on two continents",
    vlabel="Est. 2007 &middot; Japan",
    mono="IS",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Iyo Sky</b> is the rare wrestler whose Japanese career and American career would each, on "
        "their own, justify a page like this. In Stardom she was the promotion's Ace: a two-time World "
        "of Stardom Champion whose second reign ran eighteen months with a record fourteen defences, "
        "the first wrestler to complete Stardom's Grand Slam, and Tokyo Sports' Joshi Wrestler of the "
        "Year three years running, 2015 through 2017. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">5.0</span>'
        '<span class="pull-cap">stars from Dave Meltzer for the WrestleMania 41 triple threat &mdash; the first women&rsquo;s match in WWE to receive the rating</span></span>'
        "In WWE she has held world titles on both "
        "current lineages &mdash; the WWE Women's Championship for 246 days from a SummerSlam 2023 "
        "cash-in, and the Women's World Championship for 132 days in 2025 &mdash; and her WrestleMania "
        "41 triple threat with Rhea Ripley and Bianca Belair became the first women's match in WWE "
        "history rated five stars by Dave Meltzer. She is the 2026 Queen of the Ring.",

        "Two precision points the retellings blur. First, the five-star WrestleMania 41 match was a "
        "<b>triple threat she won as champion</b> &mdash; the milestone is hers, Ripley's and "
        "Belair's together, and she left with the title she entered with. Second, neither of her WWE "
        "world reigns ended in a straight defeat: the first ended at WrestleMania XL against Bayley "
        "after 246 days, a clean loss, but the second ended at Evolution on July 13, 2025 when "
        "<b>Naomi cashed in Money in the Bank</b> &mdash; the same mechanism Sky herself had used to "
        "win her first title from Bianca Belair at SummerSlam 2023. The briefcase gave her one world "
        "championship and took another away, which is as neat a summary of WWE cause-and-effect as "
        "exists.",

        "She was born Masami Odate on May 8, 1990, debuted on March 4, 2007 at sixteen while still in "
        "high school, trained by Tomohiko Hashimoto, and wrestled Mexico from 2010 under names "
        "including Viva Kasai before Stardom made her Io Shirai. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">14</span>'
        '<span class="pull-cap">defences in her second World of Stardom reign, December 2015 to June 2017 &mdash; the record</span></span>'
        "WWE signed her out of the 2018 Mae Young Classic, where she lost the final to Toni Storm at "
        "Evolution; as Io Shirai she held the NXT Women's Championship for 304 days from June 7, 2020. "
        "The renaming to Iyo Sky came with the July 2022 main-roster call-up and the founding of "
        "<b>Damage CTRL</b> with Bayley and Dakota Kai at SummerSlam 2022 &mdash; the faction that "
        "carried her through two tag title reigns, the 2023 briefcase, and the championship run that "
        "made the American half of the career undeniable.",

        "The 2026 shape: RHIYO &mdash; the tag team with Rhea Ripley &mdash; won the Women's Tag Team "
        "Championship on the January 5 Raw and lost it to The Irresistible Forces after 53 days, "
        "dissolving when Ripley moved to SmackDown after WrestleMania 42, where Sky helped Ripley win "
        "the WWE Women's Championship from Jade Cargill. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">2026</span>'
        '<span class="pull-cap">Queen of the Ring &mdash; won June 27 in Riyadh by pinning the Women&rsquo;s World Champion, Liv Morgan</span></span>'
        "She won the Queen of the Ring final over Liv Morgan at Night of Champions on June 27 and "
        "chose Morgan's Women's World Championship for SummerSlam. The challenge failed on August 1 "
        "&mdash; she hurt her own knee driving Morgan into the ring post, absorbed interference from "
        "Roxanne Perez and Raquel Rodriguez, and was pinned at 13:35 &mdash; and she has answered it "
        "by siding with Sol Ruca against The Judgment Day, winning a tag match with Ruca over Perez "
        "and Rodriguez on the August 10 Raw. That is where she stands as of August 31, 2026: on Raw, "
        "unbelted, and still the division's measuring stick.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Highlight set",
        promo_order=["STARDOM", "WWE"],
        promo_labels={"STARDOM": "Stardom", "WWE": "WWE"},
        stats=[
            ("2&times;",  "WWE world titles"),
            ("2&times;",  "World of Stardom"),
            ("304",       "Day NXT reign"),
            ("246",       "Day WWE Women's reign"),
            ("3&times;",  "WWE Women's Tag"),
            ("2026",      "Queen of the Ring"),
        ],
        lead=("Sixteen documented bouts - a highlight subset, not a career count, and deliberately "
              "light on the Stardom years: only bouts with verified day-precision dates and opponents "
              "are listed, which excludes most of the runs that made her the Ace. No career win-loss "
              "total is published because none was verified. Filter by match type, tap any column "
              "header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The one verified rating, and two bouts chosen for weight rather than stars - no "
                    "unverified ratings are printed."),
    signature=[
        dict(rating="5.0", event="WrestleMania 41 Night 2", opponent="Rhea Ripley & Bianca Belair",
             stip="Women's World Championship triple threat — the first five-star women's match in WWE"),
        dict(rating="—", event="SummerSlam 2026 Night 1", opponent="Liv Morgan",
             stip="Women's World Championship — fought through her own knee injury; Forbes called it an instant classic"),
        dict(rating="—", event="Evolution 2018", opponent="Toni Storm",
             stip="Mae Young Classic final — the match that closed her signing"),
    ],
    signature_count_word="three",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("2&times;", "WWE world reigns"),
            ("2&times;", "World of Stardom"),
            ("7th",      "WWE Women's Grand Slam"),
            ("2",        "Countries with a Grand Slam"),
        ],
        lead=("A championship record split across two continents - the first wrestler to complete a "
              "Grand Slam in both Japan and the United States. Stardom reign counts are Wikipedia's; "
              "individual Stardom reign dates beyond those shown were not re-verified in this pass."),
        rows=[
            dict(ic="W", name="WWE Women's Championship", count="1",
                 sub="August 5, 2023 &ndash; April 7, 2024 &middot; won by Money in the Bank cash-in "
                     "on Bianca Belair at SummerSlam, lost to Bayley at WrestleMania XL &middot; "
                     "<b>246 days</b>, with defences against Zelina Vega, Asuka, Charlotte Flair and "
                     "Belair"),
            dict(ic="V", name="Women's World Championship", count="1",
                 sub="March 3 &ndash; July 13, 2025 &middot; won from Rhea Ripley on Raw, retained in "
                     "the five-star WrestleMania 41 triple threat, lost at Evolution when Naomi cashed "
                     "in Money in the Bank &middot; <b>132 days</b>"),
            dict(ic="N", name="NXT Women's Championship", count="1",
                 sub="June 7, 2020 &ndash; April 7, 2021, as Io Shirai &middot; <b>304 days</b> "
                     "&middot; won from Charlotte Flair in a triple threat also involving Rhea Ripley, "
                     "lost to Raquel Gonzalez"),
            dict(ic="T", name="WWE Women's Tag Team Championship", count="3",
                 sub="Twice with Dakota Kai in 2022&ndash;23 (48 and 114 days) &middot; once with Rhea "
                     "Ripley as RHIYO, January 5 &ndash; February 27, 2026, <b>53 days</b>"),
            dict(ic="X", name="NXT Women's Tag Team Championship", count="1",
                 sub="With Zoey Stark, July 6 &ndash; October 26, 2021 &middot; 111 days"),
            dict(ic="S", name="World of Stardom Championship", count="2",
                 sub="2013&ndash;14 (468 days, 10 defences) and December 23, 2015 &ndash; June 21, "
                     "2017 &mdash; an eighteen-month reign with a record <b>14 defences</b>"),
            dict(ic="D", name="Wonder of Stardom Championship", count="2",
                 sub="Including a 2017&ndash;18 reign with a record 12 defences &middot; part of the "
                     "first Stardom Grand Slam ever completed"),
            dict(ic="A", name="Artist of Stardom Championship", count="6",
                 sub="Stardom&rsquo;s trios title &middot; individual reign dates not verified in this "
                     "pass"),
            dict(ic="G", name="SWA World Championship and others", count="3",
                 sub="Inaugural SWA World Champion (lost to Toni Storm, July 24, 2016, after three "
                     "defences) &middot; Goddesses of Stardom and High Speed Championships, one reign "
                     "each"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="The Stardom unit she led, the WWE faction that defined her call-up, and the tag team "
             "that did not survive a brand split.",
        cards=[
            dict(era="Stardom &middot; 2016&ndash;2018",
                 name="Queen's Quest",
                 members="Io Shirai, leading",
                 desc="The Stardom stable she fronted through the back half of her Ace run - the "
                      "banner under which the record-setting second World of Stardom reign happened."),
            dict(era="WWE &middot; 2022&ndash;2025",
                 name="Damage CTRL",
                 members="Bayley, Iyo Sky, Dakota Kai; later Asuka and Kairi Sane",
                 desc="Formed at SummerSlam on July 30, 2022 - the vehicle for her entire first "
                      "main-roster act. It produced two tag title reigns with Kai, covered the 2023 "
                      "briefcase win and the 246-day WWE Women's Championship reign, turned face in "
                      "July 2024, and dissolved in May 2025 after Dakota Kai's release."),
            dict(era="WWE &middot; 2025&ndash;2026",
                 name="RHIYO",
                 members="Iyo Sky, Rhea Ripley",
                 desc="Formed October 11, 2025 out of a rivalry that kept resolving into respect. "
                      "Women's Tag Team Champions from January 5 to February 27, 2026 - 53 days - and "
                      "finished when Ripley moved to SmackDown after WrestleMania 42, where Sky "
                      "helped her win the WWE Women's Championship from Jade Cargill."),
            dict(era="WWE &middot; 2026&ndash;present",
                 name="With Sol Ruca, against The Judgment Day",
                 members="Iyo Sky, Sol Ruca",
                 desc="Not a named unit - an alliance formed after SummerSlam 2026, answering the "
                      "Judgment Day interference that shaped her title loss. She and Ruca beat Raquel "
                      "Rodriguez and Roxanne Perez on the August 10 Raw, and she was in Ruca's corner "
                      "again on August 24."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Half a dozen masks and names on the way up, and two that mattered: <b>Io Shirai</b> "
             "(Stardom and NXT) &rarr; <b>Iyo Sky</b> (WWE, 2022&ndash;present).",
        cards=[
            dict(mono="MX", era="Mexico &middot; 2010&ndash;2015", name="Viva Kasai and others",
                 desc="The lucha apprenticeship, worked under several names including Viva Kasai and "
                      "Oyuki, with a hair-vs-mask apuestas win in November 2011. It is where the "
                      "high-wire style was finished."),
            dict(mono="IO", era="Stardom &amp; NXT &middot; 2011&ndash;2022", name="Io Shirai",
                 desc="The Ace of Stardom and, from 2018, NXT's self-styled Evil Genius. Two World of "
                      "Stardom reigns, three straight Tokyo Sports awards, a 304-day NXT Women's "
                      "Championship reign, and a heel turn in June 2019 that gave the character its "
                      "edge."),
            dict(mono="IS", era="WWE &middot; 2022&ndash;present", name="Iyo Sky",
                 desc="The renaming came with the July 2022 call-up and Damage CTRL. The Genius of "
                      "the Sky is the same wrestler with the villainy made optional - since the 2024 "
                      "face turn she has been booked as the division's purest in-ring standard, the "
                      "one five-star matches and Queen of the Ring crowns get measured against."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Sixteen-year-old trainee to the first Grand Slam on two continents.",
        rows=[
            dict(year="2007", title="Debut at sixteen",
                 desc="Debuts March 4, 2007 while still in high school, trained by Tomohiko "
                      "Hashimoto. Her sister Mio Shirai also wrestled."),
            dict(year="2013", title="First World of Stardom Championship",
                 desc="Wins Stardom's top title on April 29, 2013 and holds it 468 days with ten "
                      "defences."),
            dict(year="2015", title="The Ace years begin",
                 desc="Starts the second World of Stardom reign on December 23, 2015 - eighteen "
                      "months and a record fourteen defences - and opens a run of three straight "
                      "Tokyo Sports Joshi Wrestler of the Year awards."),
            dict(year="2018", title="Mae Young Classic and WWE",
                 desc="Signs with WWE, reaches the Mae Young Classic final and loses it to Toni Storm "
                      "at Evolution on October 28. Debuts for NXT that November as Io Shirai."),
            dict(year="2020", title="NXT Women's Champion",
                 desc="Wins the title from Charlotte Flair in a triple threat with Rhea Ripley at "
                      "TakeOver: In Your House on June 7 and holds it 304 days."),
            dict(year="2022", title="Iyo Sky and Damage CTRL",
                 desc="Renamed on the main-roster call-up; founds Damage CTRL with Bayley and Dakota "
                      "Kai at SummerSlam on July 30, and wins tag gold with Kai that September."),
            dict(year="2023", title="Briefcase, then champion",
                 desc="Wins Money in the Bank in London on July 1 and cashes in on Bianca Belair at "
                      "SummerSlam on August 5 for the WWE Women's Championship."),
            dict(year="2024", title="The 246 days end",
                 desc="Loses the title to Bayley at WrestleMania XL on April 7 after 246 days."),
            dict(year="2025", title="A second world title and the five-star first",
                 desc="Beats Rhea Ripley for the Women's World Championship on the March 3 Raw, "
                      "retains in the WrestleMania 41 triple threat Meltzer rated five stars - a "
                      "first for women's wrestling in WWE - and loses the title at Evolution on July "
                      "13 to Naomi's cash-in. Forms RHIYO with Ripley on October 11."),
            dict(year="2026", title="Tag gold, the Queen's crown, and a knee",
                 desc="Wins the tag titles with Ripley on January 5 and loses them February 27; helps "
                      "Ripley win the WWE Women's Championship at WrestleMania 42; wins Queen of the "
                      "Ring over Liv Morgan on June 27 in Riyadh; loses the SummerSlam title match to "
                      "Morgan on August 1 after hurting her knee; sides with Sol Ruca against The "
                      "Judgment Day in August."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who she went to war with.",
        cards=[
            dict(name="Rhea Ripley",
                 desc="The defining relationship of her 2024-26: title matches in March 2025, a "
                      "double-DQ, the five-star WrestleMania 41 triple threat, and then a tag team - "
                      "RHIYO - built out of mutual respect that won gold in January 2026. She repaid "
                      "the account at WrestleMania 42 by helping Ripley beat Jade Cargill for the WWE "
                      "Women's Championship."),
            dict(name="Liv Morgan", slug="liv-morgan",
                 desc="The 2026 rivalry: Sky pinned the champion clean in the Queen of the Ring final "
                      "on June 27 in Riyadh, then lost the SummerSlam title match on August 1 with a "
                      "hurt knee and The Judgment Day working the margins - Morgan had also cracked "
                      "her in the head with the belt on the July Raw that set the match up. The clean "
                      "tournament pin is the fact Sky's next challenge will be built on."),
            dict(name="Bayley",
                 desc="Faction leader, then the loss that mattered most: Bayley turned on Damage CTRL "
                      "and took the WWE Women's Championship from her at WrestleMania XL on April 7, "
                      "2024, ending the 246-day reign - the only time Sky has dropped a world title "
                      "by pinfall in a straight singles match."),
            dict(name="Toni Storm",
                 desc="The recurring early rival on two continents: Storm ended her inaugural SWA "
                      "World Championship reign in July 2016 and beat her in the Mae Young Classic "
                      "final at Evolution in October 2018 - the match WWE signed her off the back of."),
            dict(name="Naomi",
                 desc="The cash-in. Naomi took the Women's World Championship at Evolution on July 13, "
                      "2025 with the same briefcase mechanism Sky had used on Bianca Belair two years "
                      "earlier - a loss with no rematch, because the title picture moved on without "
                      "either of them."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Thin by design - the verified list is short, and nothing is added to pad it.",
        rows=[
            dict(when="2022&ndash;", title="WWE 2K", kind="Game",
                 desc="A playable fixture of the current WWE 2K series. Her exact debut entry - and "
                      "whether early appearances were billed as Io Shirai - was not verified in this "
                      "pass, so no year is claimed."),
            dict(when="2018", title="Mae Young Classic", kind="TV",
                 desc="Her WWE introduction was itself a television product: the 2018 tournament run "
                      "ended in the final at Evolution, WWE's first all-women pay-per-view."),
            dict(when="2015&ndash;2017", title="Tokyo Sports awards", kind="Press",
                 desc="Three consecutive Joshi Wrestler of the Year awards - the Japanese sports-press "
                      "record of the Ace years. No memoir, documentary or scripted role could be "
                      "verified, so none is listed."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated the way the sources state them - with the shared milestones marked "
             "as shared.",
        stats=[
            ("5.0", "First WWE women's five-star"),
            ("246", "Day WWE Women's reign"),
            ("14",  "Defences, second Stardom reign"),
        ],
        rows=[
            dict(name="First five-star women's match in WWE history",
                 sub="The WrestleMania 41 Night 2 triple threat with Rhea Ripley and Bianca Belair, "
                     "April 20, 2025, per Dave Meltzer's rating as reported by Wikipedia. She won it "
                     "as champion. The milestone belongs to all three women; the victory is hers."),
            dict(name="First wrestler with a Grand Slam in both Japan and the United States",
                 sub="Stardom's first-ever Grand Slam, completed across its four championships, plus "
                     "WWE's - Wikipedia lists her as the seventh WWE Women's Grand Slam and tenth "
                     "Women's Triple Crown champion."),
            dict(name="World champion on both WWE lineages",
                 sub="WWE Women's Championship, 246 days (August 5, 2023 - April 7, 2024); Women's "
                     "World Championship, 132 days (March 3 - July 13, 2025). One won by cash-in, one "
                     "lost to a cash-in."),
            dict(name="Record 14 defences of the World of Stardom Championship",
                 sub="Second reign, December 23, 2015 to June 21, 2017 - roughly eighteen months as "
                     "the Ace of Stardom, after a first reign of 468 days."),
            dict(name="2026 Queen of the Ring",
                 sub="Won June 27, 2026 at Night of Champions in Riyadh by pinning Women's World "
                     "Champion Liv Morgan - a champion pinned clean in a non-title final, which is "
                     "why the SummerSlam challenge followed automatically."),
            dict(name="Royal Rumble 2025 iron woman - for a few hours",
                 sub="Entered No. 1 and lasted 1:06:45, breaking the women's longevity record - which "
                     "was itself surpassed later the same night, per Wikipedia. Stated here with the "
                     "caveat most retellings drop."),
            dict(name="Tokyo Sports Joshi Wrestler of the Year, three straight",
                 sub="2015, 2016 and 2017 - the run no other wrestler of her generation matched."),
        ],
        footnote=("No career win-loss total is published - none was verified. Her billed height and "
                  "weight (5'1\", 119 lb) are long-standing billing figures; WWE.com's profile was "
                  "not harvested for vitals in this pass. Sources give her birthplace only as Japan, "
                  "so nothing more precise appears here."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Iyo_Sky"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/iyo-sky"),
        dict(k="Yahoo Sports", v="Queen of the Ring win at Night of Champions 2026",
             href="https://sports.yahoo.com/articles/iyo-sky-wins-wwe-queen-181457889.html"),
        dict(k="POST Wrestling", v="SummerSlam 2026 - the Liv Morgan title match",
             href="https://www.postwrestling.com/2026/08/01/liv-morgan-retains-womens-world-championship-against-iyo-sky-at-summerslam/"),
        dict(k="F4W/WON", v="The July 2026 belt-shot incident on Raw",
             href="https://www.f4wonline.com/news/wwe/iyo-sky-image-wwe-raw-injury-liv-morgan/"),
        dict(k="Fightful", v="Raw results, August 24, 2026",
             href="https://www.fightful.com/wrestling/wwe-raw-results-8-24-2026-stephanie-vaquer-vs-roxanne-perez-solo-sikoa-penta-rey-fenix-more/"),
        dict(k="SmackDown Hotel", v="Women's Tag Team title history - the RHIYO reign",
             href="https://www.thesmackdownhotel.com/title-history/wwe/wwe-women-s-tag-team-championship"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Why did Io Shirai become Iyo Sky?",
            a="WWE renamed her on the main-roster call-up in July 2022, when she debuted at SummerSlam "
              "as a founding member of Damage CTRL. &ldquo;Io Shirai&rdquo; was the Stardom ring name "
              "she had carried since 2011 and kept through four years of NXT &mdash; the new spelling "
              "kept the sound of her name while giving WWE a mark it owned. She was born Masami "
              "Odate; neither name is her legal one.",
            q_ld="Why did Io Shirai change her name to Iyo Sky?",
            a_ld="WWE renamed Io Shirai as Iyo Sky in July 2022 when she moved from NXT to the main "
                 "roster and founded Damage CTRL at SummerSlam with Bayley and Dakota Kai. Io Shirai "
                 "was her ring name in Stardom from 2011 and in NXT from 2018. She was born Masami "
                 "Odate, so both names are ring names."),
        dict(
            q="Was Iyo Sky in the first five-star women's match in WWE history?",
            a="Yes &mdash; and she <b>won</b> it, as champion. The WrestleMania 41 Night 2 triple "
              "threat on April 20, 2025, against Rhea Ripley and Bianca Belair for the Women's World "
              "Championship, was the first women's match in WWE rated five stars by Dave Meltzer, per "
              "Wikipedia. The milestone is shared by all three women; the result is not.",
            q_ld="Was Iyo Sky in the first five-star women's match in WWE history?",
            a_ld="Yes. The WrestleMania 41 Night 2 triple threat on April 20, 2025, in which Iyo Sky "
                 "retained the Women's World Championship against Rhea Ripley and Bianca Belair, was "
                 "the first women's match in WWE history rated five stars by Dave Meltzer, according "
                 "to Wikipedia. Sky won the match and retained her title."),
        dict(
            q="Is Iyo Sky a champion right now, and what happened at SummerSlam?",
            a="No. As of August 31, 2026 she holds no title. She earned a Women's World Championship "
              "match by pinning champion Liv Morgan in the Queen of the Ring final on June 27, but "
              "lost the SummerSlam Night 1 match on August 1 at 13:35 &mdash; she hurt her own knee "
              "driving Morgan into the ring post with a meteora, took interference from Roxanne Perez "
              "and Raquel Rodriguez, and was pinned after a Codebreaker and Ob-Liv-ion. Since then "
              "she has allied with Sol Ruca against The Judgment Day on Raw.",
            q_ld="Is Iyo Sky a champion right now?",
            a_ld="No. As of August 31, 2026 Iyo Sky holds no championship. She challenged Liv Morgan "
                 "for the Women's World Championship at SummerSlam on August 1, 2026 and lost after "
                 "hurting her knee mid-match and absorbing interference from The Judgment Day's "
                 "Roxanne Perez and Raquel Rodriguez. She has since allied with Sol Ruca against The "
                 "Judgment Day on Raw."),
        dict(
            q="What did Iyo Sky accomplish in Japan?",
            a="She was the Ace of Stardom: two World of Stardom Championship reigns &mdash; 468 days "
              "with ten defences, then eighteen months from December 2015 with a record fourteen "
              "&mdash; two Wonder of Stardom reigns including one with a record twelve defences, six "
              "Artist of Stardom trios titles, the inaugural SWA World Championship, the 2014 5STAR "
              "Grand Prix, the first Stardom Grand Slam ever completed, and Tokyo Sports&rsquo; Joshi "
              "Wrestler of the Year in 2015, 2016 and 2017.",
            q_ld="What did Iyo Sky accomplish in Stardom in Japan?",
            a_ld="As Io Shirai, Iyo Sky was the Ace of Stardom. She held the World of Stardom "
                 "Championship twice, including an eighteen-month reign from December 2015 to June "
                 "2017 with a record fourteen defences, held the Wonder of Stardom Championship "
                 "twice, won the Artist of Stardom trios title six times, was the inaugural SWA World "
                 "Champion, won the 2014 5STAR Grand Prix, completed the first Stardom Grand Slam, "
                 "and won Tokyo Sports' Joshi Wrestler of the Year award in 2015, 2016 and 2017."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Masami Odate"),
        dict(label="Born", value="May 8, 1990", sub="Japan &middot; age 36 &middot; exact city not "
                                                    "verified"),
        dict(label="Height", value="5&#8242;1&#8243;", sub="155 cm (billed)"),
        dict(label="Weight", value="119 lb", sub="54 kg (billed)"),
        dict(label="Debut", value="March 4, 2007", sub="at sixteen, while still in high school"),
        dict(label="Trained by", value="Tomohiko Hashimoto", sub="Team Makehen"),
        dict(label="WWE debut", value="August 8, 2018", sub="Mae Young Classic &middot; NXT from "
                                                            "November 2018"),
        dict(label="Finishers", value="Over the Moonsault &middot; Moonsault",
             sub="with the Spanish Fly among the set-ups"),
        dict(label="Family", value="Mio Shirai", sub="sister, retired wrestler"),
        dict(label="Brand", value="Raw"),
        dict(label="Also known as",
             value="Io Shirai &middot; The Genius of the Sky &middot; Viva Kasai &middot; Oyuki"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1990-05-08",
    bornplace="Japan",
    nationality="Japan",
    height_cm=155,
    weight_kg=54,
    ld=dict(
        alternateName=["Masami Odate", "Io Shirai", "The Genius of the Sky", "Viva Kasai", "Oyuki"],
        award=["WWE Women's Championship (1 reign, 246 days)",
               "Women's World Championship (1 reign, 132 days)",
               "NXT Women's Championship (1 reign, 304 days)",
               "WWE Women's Tag Team Championship (3 reigns)",
               "NXT Women's Tag Team Championship (1 reign)",
               "World of Stardom Championship (2 reigns, record 14 defences in the second)",
               "Wonder of Stardom Championship (2 reigns)",
               "Artist of Stardom Championship (6 reigns)",
               "SWA World Championship (inaugural champion)",
               "Goddesses of Stardom Championship (1 reign)",
               "High Speed Championship (1 reign)",
               "Queen of the Ring (2026)",
               "5STAR Grand Prix winner (2014)",
               "Tokyo Sports Joshi Wrestler of the Year (2015, 2016, 2017)"],
        knowsAbout=["Professional wrestling", "Joshi puroresu", "Stardom", "WWE", "Damage CTRL",
                    "High-flying wrestling", "Lucha libre"],
        description="Iyo Sky, born Masami Odate and known in Japan as Io Shirai, is a Japanese "
                    "professional wrestler signed to WWE. The former Ace of Stardom held the World of "
                    "Stardom Championship twice, including an eighteen-month reign with a record "
                    "fourteen defences. In WWE she has held the WWE Women's Championship for 246 days "
                    "and the Women's World Championship for 132 days, won the 2026 Queen of the Ring, "
                    "and retained her title in the WrestleMania 41 triple threat that became the "
                    "first women's match in WWE history rated five stars by Dave Meltzer.",
        sameAs=["https://en.wikipedia.org/wiki/Iyo_Sky",
                "https://www.wwe.com/superstars/iyo-sky"],
    ),
)
