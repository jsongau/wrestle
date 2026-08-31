# -*- coding: utf-8 -*-
"""Liv Morgan - dossier data.

Sources: web research compiled August 31, 2026 - Wikipedia, Fightful, POST Wrestling,
TheSmackDownHotel, Yahoo Sports and WWE.com show pages, all opened during this pass.
Every match row carries a day-precision date from one of those sources.

Deliberate omissions:
  * No career win-loss total - none was verified.
  * No social links - handles were not verified in this pass.
  * The 2023 tag title reigns with Raquel Rodriguez are dated from Wikipedia's reign
    table; the winning opponents for the first two were not verified and are not
    invented, so those two reigns appear in the titles section but not as match rows.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="L", date="2019-01-27", promo="WWE", type="tag",
         event="Royal Rumble", opponent="The 2019 women's Royal Rumble field",
         stip="Eliminated in 8 seconds - the record shortest women's Rumble appearance", title=""),
    dict(result="W", date="2020-08-30", promo="WWE", type="tag",
         event="Payback", opponent="The IIconics",
         stip="With Ruby Riott - The Riott Squad reunion", title=""),
    dict(result="W", date="2022-07-02", promo="WWE", type="tag", landmark=True,
         event="Money in the Bank - Las Vegas", opponent="The 2022 women's ladder match field",
         stip="Wins the briefcase", title=""),
    dict(result="W", date="2022-07-02", promo="WWE", landmark=True,
         event="Money in the Bank - Las Vegas", opponent="Ronda Rousey",
         stip="Cash-in the same night - first title of her career",
         title="SmackDown Women's Championship"),
    dict(result="W", date="2022-09-03", promo="WWE",
         event="Clash at the Castle - Cardiff", opponent="Shayna Baszler",
         stip="Singles - retains", title="SmackDown Women's Championship"),
    dict(result="L", date="2022-10-08", promo="WWE", landmark=True,
         event="Extreme Rules - Philadelphia", opponent="Ronda Rousey",
         stip="Extreme Rules - the 98-day reign ends", title="SmackDown Women's Championship"),
    dict(result="W", date="2024-05-25", promo="WWE", landmark=True,
         event="King and Queen of the Ring - Jeddah", opponent="Becky Lynch",
         stip="Singles - second world title, start of the 226-day reign",
         title="Women's World Championship"),
    dict(result="W", date="2024-08-03", promo="WWE", landmark=True,
         event="SummerSlam - Cleveland", opponent="Rhea Ripley",
         stip="Retains - Dominik Mysterio turns on Ripley", title="Women's World Championship"),
    dict(result="W", date="2024-11-02", promo="WWE", landmark=True,
         event="Crown Jewel - Riyadh", opponent="Nia Jax",
         stip="Champion vs. champion - inaugural winner",
         title="WWE Women's Crown Jewel Championship"),
    dict(result="L", date="2025-01-06", promo="WWE", landmark=True,
         event="Raw - Netflix premiere", opponent="Rhea Ripley",
         stip="Singles - the 226-day reign ends", title="Women's World Championship"),
    dict(result="W", date="2026-01-31", promo="WWE", type="tag", landmark=True,
         event="Royal Rumble match - Riyadh", opponent="The 2026 women's Royal Rumble field",
         stip="Wins from No. 14, last eliminating Tiffany Stratton", title=""),
    dict(result="W", date="2026-04-18", promo="WWE", landmark=True,
         event="WrestleMania 42 Night 1", opponent="Stephanie Vaquer",
         stip="Singles - takes the title back in about six minutes",
         title="Women's World Championship"),
    dict(result="L", date="2026-06-27", promo="WWE",
         event="Night of Champions - Riyadh", opponent="Iyo Sky",
         stip="Queen of the Ring final - non-title; pinned clean", title=""),
    dict(result="W", date="2026-08-01", promo="WWE", landmark=True,
         event="SummerSlam Night 1 - Minneapolis", opponent="Iyo Sky",
         stip="First televised defence of the reign - Codebreaker and Ob-Liv-ion at 13:35",
         title="Women's World Championship"),
]

DATA = dict(
    slug="liv-morgan",
    name="Liv Morgan",
    realname="Gionna Jene Daddio",
    epithet="Leader of The Judgment Day",
    hook="Record & Titles",

    meta_desc=("Liv Morgan is the reigning Women's World Champion, a three-time world champion in the "
               "same lineage, the 2026 Royal Rumble winner and the leader of The Judgment Day. Full "
               "record, titles, factions and career."),
    og_desc=("Women's World Champion, 2026 Royal Rumble winner, 2022 Money in the Bank winner, "
             "four-time tag champion with Raquel Rodriguez and leader of The Judgment Day."),
    tw_desc="Women's World Champion: 3 world reigns in one lineage, the 2026 Rumble, The Judgment Day.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2015",
    height_imp="5&#8242;3&#8243;",
    weight_lb="125",
    world_titles="3",
    vitals_tagline="Watch her",
    support_note="Merch &middot; Games &middot; Watch",
    sp_items=[
        dict(ic="LM", title="Liv Morgan Merch", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable in the current 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="JD", title="The Judgment Day", sub="The faction she leads on Raw",
             tag="Watch", href="https://www.wwe.com/shows/raw"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/liv-morgan"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Riott Squad &middot; The Revenge Tour &middot; The Judgment Day",
    hero_tag="Morristown, New Jersey &middot; <em>NXT &middot; WWE &middot; 2015&ndash;present</em>",
    now_label="NOW",
    now_bold="Women's World Champion",
    now_tail=" &middot; 135 days into the reign as of August 31, 2026, with Stephanie Vaquer "
             "challenging on the September 7 Raw and Becky Lynch circling the same title",
    hstats=[
        dict(value="3",    x=True,  label="World Title Reigns"),
        dict(value="2026", x=False, label="Royal Rumble Winner"),
        dict(value="226",  x=False, label="Day Longest Reign"),
        dict(value="4",    x=True,  label="Tag Titles with Raquel"),
    ],
    ghost_link="From planted fan at a 2015 TakeOver to champion booking her own challengers",
    vlabel="Est. 2015 &middot; Elmwood Park, New Jersey",
    mono="LM",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Liv Morgan</b> is the reigning Women's World Champion and, at this point, the argument "
        "that persistence is a wrestling style. She spent seven years as a plucky underdog the "
        "company never quite pulled the trigger on; since 2022 she has won a briefcase and cashed it "
        "in on Ronda Rousey the same night, run a 226-day reign as Women's World Champion, become the "
        "inaugural Women's Crown Jewel Champion, taken over <b>The Judgment Day</b>, and won the 2026 "
        "Royal Rumble. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">3</span>'
        '<span class="pull-cap">world title reigns, all in the same SmackDown Women&rsquo;s / Women&rsquo;s World lineage &mdash; 2022, 2024 and the current one</span></span>'
        "The current reign started at WrestleMania 42 on April 18, 2026, when she beat Stephanie "
        "Vaquer in about six minutes to take the title back, and it survived its first televised "
        "defence at SummerSlam on August 1 against Iyo Sky. Vaquer gets her rematch on the September "
        "7 Raw.",

        "Her title count reads two different ways in print, and both are defensible &mdash; so here "
        "is the arithmetic. Wikipedia's infobox and Fightful's current coverage call her a "
        "<b>two-time Women's World Champion</b>: 2024's 226-day reign, and the current one. "
        "TheSmackDownHotel calls her a <b>three-time champion</b>, because it counts her 2022 "
        "SmackDown Women's Championship reign in the same ledger &mdash; and that is the same belt: "
        "the SmackDown Women's Championship was renamed the Women's World Championship in June 2023. "
        "This page follows the lineage: <b>three world title reigns, one lineage</b> &mdash; 98 days "
        "in 2022, 226 days in 2024&ndash;25, and the current reign, 135 days old as of August 31, "
        "2026. Anyone calling her a two-time champion is counting the name; anyone saying three is "
        "counting the belt.",

        "She was born Gionna Jene Daddio on June 8, 1994 in Morristown, New Jersey, signed in 2014 "
        "with no wrestling background, and debuted in 2015 &mdash; first on camera as a planted "
        "&ldquo;fan&rdquo; at NXT TakeOver: Rival that February, then in the ring that November. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">8</span>'
        '<span class="pull-cap">seconds in the 2019 Royal Rumble &mdash; the record shortest women&rsquo;s Rumble appearance, from the years when she was the punchline</span></span>'
        "The Riott Squad years (2017&ndash;2021, twice) made her popular and won her nothing; the "
        "2019 Royal Rumble literally lasted eight seconds. The turn came at Money in the Bank on July "
        "2, 2022: briefcase and championship in one night, off Ronda Rousey. When Rousey took the "
        "title back at Extreme Rules that October, WWE had learned the audience would treat Morgan's "
        "losses as injustices &mdash; which is the engine everything since has run on.",

        "The 2024 &ldquo;Revenge Tour&rdquo; converted that goodwill into a heel act that worked "
        "better than the babyface one ever had: she beat Becky Lynch for the Women's World "
        "Championship at King and Queen of the Ring on May 25, 2024, took Dominik Mysterio and then "
        "the whole Judgment Day out from under Rhea Ripley, and held the title 226 days until Ripley "
        "beat her on Raw's Netflix premiere, January 6, 2025. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">226</span>'
        '<span class="pull-cap">days as Women&rsquo;s World Champion in 2024&ndash;25 &mdash; ended by Rhea Ripley on Raw&rsquo;s Netflix premiere</span></span>'
        "A dislocated shoulder on June 16, 2025 cost her five and a half months; she returned at "
        "Survivor Series: WarGames on November 29, won the Rumble from No. 14 on January 31, 2026 "
        "&mdash; last eliminating Tiffany Stratton &mdash; and beat Vaquer at WrestleMania 42. The "
        "reign's defining criticism is its defence rate: SummerSlam was the first televised defence "
        "in over a hundred days, Becky Lynch returned in August calling her a &ldquo;glorified "
        "valet,&rdquo; and Iyo Sky pinned her clean in the non-title Queen of the Ring final in June. "
        "The Judgment Day &mdash; Dominik Mysterio, Raquel Rodriguez, Roxanne Perez, JD McDonagh "
        "&mdash; remains her margin in every close match.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Highlight set",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("3&times;", "World titles, one lineage"),
            ("226",      "Longest reign (days)"),
            ("2026",     "Royal Rumble winner"),
            ("2022",     "Money in the Bank"),
            ("4&times;", "Women's Tag Team"),
            ("1st",      "Crown Jewel Champion"),
        ],
        lead=("Fourteen documented bouts - a highlight subset, not a career count, running from the "
              "8-second 2019 Rumble to the SummerSlam 2026 defence. No career win-loss total is "
              "published because none was verified. The two Money in the Bank rows are the same "
              "night, July 2, 2022 - the briefcase and the cash-in are listed separately because "
              "they were separate matches. Filter by match type, tap any column header to sort, and "
              "turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("Three bouts that define the run. No star ratings are printed because none were "
                    "verified in this pass."),
    signature=[
        dict(rating="—", event="Money in the Bank 2022", opponent="Ronda Rousey",
             stip="The same-night cash-in — briefcase to champion in one evening"),
        dict(rating="—", event="SummerSlam 2026 Night 1", opponent="Iyo Sky",
             stip="Women's World Championship — Forbes called it an instant classic"),
        dict(rating="—", event="WrestleMania 42 Night 1", opponent="Stephanie Vaquer",
             stip="Women's World Championship — the six-minute reclamation"),
    ],
    signature_count_word="three",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("3&times;", "World reigns, one lineage"),
            ("4&times;", "Tag reigns with Raquel"),
            ("1st",      "Crown Jewel Champion"),
            ("135",      "Days into the current reign"),
        ],
        lead=("Every championship she has ever held has come since July 2022, and every world reign "
              "sits in a single lineage that changed names mid-stream - which is where the two-time / "
              "three-time discrepancy in her coverage comes from. Both counts are printed here with "
              "their sources."),
        rows=[
            dict(ic="W", name="Women's World Championship / SmackDown Women's Championship", count="3",
                 sub="One lineage, renamed June 2023 &middot; 2022, cash-in on Ronda Rousey at Money "
                     "in the Bank, <b>98 days</b>, lost back to Rousey at Extreme Rules &middot; "
                     "2024&ndash;25, def. Becky Lynch at King and Queen of the Ring, <b>226 days</b>, "
                     "lost to Rhea Ripley on the Netflix premiere Raw &middot; 2026&ndash;present, "
                     "def. Stephanie Vaquer at WrestleMania 42, <b>135 days and counting</b> as of "
                     "August 31, 2026 &middot; Wikipedia and Fightful count the two reigns under the "
                     "current name; TheSmackDownHotel counts all three &mdash; same belt either way"),
            dict(ic="T", name="WWE Women's Tag Team Championship", count="4",
                 sub="All with Raquel Rodriguez &mdash; a record for one team &middot; 2023, 39 days, "
                     "vacated when Morgan injured a shoulder &middot; 2023, 16 days &middot; "
                     "2025, February 24 to WrestleMania 41 Night 2, lost to Lyra Valkyria &amp; Becky "
                     "Lynch &middot; 2025, regained on the post-WrestleMania Raw, ended June 16 at 70 "
                     "days when Morgan dislocated her shoulder and Roxanne Perez replaced her"),
            dict(ic="C", name="WWE Women's Crown Jewel Championship", count="1",
                 sub="Inaugural winner &middot; beat WWE Women's Champion Nia Jax, champion vs. "
                     "champion, at Crown Jewel in Riyadh on November 2, 2024"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Two runs with the squad that made her, and the villain faction she took over from the "
             "inside.",
        cards=[
            dict(era="WWE &middot; 2017&ndash;2019",
                 name="The Riott Squad",
                 members="Ruby Riott, Liv Morgan, Sarah Logan",
                 desc="Her main-roster debut vehicle from November 21, 2017 - a chaos-agent heel trio "
                      "that attacked Becky Lynch and Naomi on arrival. It got her on television every "
                      "week and won her nothing; it disbanded when she was drafted to SmackDown in "
                      "April 2019."),
            dict(era="WWE &middot; 2020&ndash;2021",
                 name="The Riott Squad, reunion",
                 members="Ruby Riott, Liv Morgan",
                 desc="Reformed August 3, 2020 as a duo, with a win over The IIconics at Payback on "
                      "August 30. It ended for good when WWE released Ruby Riott on June 2, 2021 - "
                      "the breakup that left Morgan to sink or swim as a singles act."),
            dict(era="WWE &middot; 2024&ndash;present",
                 name="The Judgment Day",
                 members="Liv Morgan, Dominik Mysterio, Raquel Rodriguez, Roxanne Perez, JD McDonagh",
                 desc="She joined on August 5, 2024, two days after beating Rhea Ripley at SummerSlam, "
                      "completing a hostile takeover that excommunicated Ripley and Damian Priest - "
                      "with Dominik Mysterio's on-screen defection to her side as the hinge. She has "
                      "run the group's women's wing since: Rodriguez as enforcer, Perez as protege, "
                      "and interference as a standing feature of her title defences, including "
                      "SummerSlam 2026."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One ring name since 2015 and three distinct acts inside it.",
        cards=[
            dict(mono="RS", era="WWE &middot; 2017&ndash;2021", name="The Riott Squad's heart",
                 desc="Blue tongue, hoodies, chaos - the sidekick years, twice over. Popular, "
                      "protected by nobody, and beaten in eight seconds at the 2019 Royal Rumble, "
                      "which became the stat her later career is measured against."),
            dict(mono="UD", era="WWE &middot; 2021&ndash;2023", name="The underdog who finally won",
                 desc="The long babyface chase that peaked at Money in the Bank 2022: briefcase and "
                      "title in one night off Ronda Rousey. The crowd treated every setback "
                      "afterwards as an injustice, which turned out to be the asset."),
            dict(mono="RT", era="WWE &middot; 2024&ndash;present", name="The Revenge Tour",
                 desc="The heel reinvention: petty, patient and structural. She did not just beat "
                      "Rhea Ripley - she took Ripley's boyfriend storyline, her faction and her "
                      "title, in that order, and has run The Judgment Day as champion-manager of her "
                      "own challengers since. Slammy voters made it official: 2025 Female Superstar "
                      "of the Year, and Villain of the Year with Dominik Mysterio."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Planted fan to champion in eleven years, with the middle spent as everyone's favourite "
             "near-miss.",
        rows=[
            dict(year="2015", title="Signed, planted, debuted",
                 desc="On camera at NXT TakeOver: Rival in February as a planted fan; in-ring debut "
                      "that November. Becomes Liv Morgan on December 2, 2015."),
            dict(year="2017", title="The Riott Squad arrives",
                 desc="Main-roster debut November 21, 2017 on SmackDown, attacking Becky Lynch and "
                      "Naomi alongside Ruby Riott and Sarah Logan."),
            dict(year="2019", title="Eight seconds",
                 desc="Sets the record for the shortest women's Royal Rumble appearance on January "
                      "27. The squad disbands in April; a reunion runs 2020-21 until Riott's "
                      "release."),
            dict(year="2022", title="Briefcase and belt in one night",
                 desc="Wins Money in the Bank on July 2 and cashes in on Ronda Rousey the same "
                      "night for the SmackDown Women's Championship - her first title. Rousey takes "
                      "it back at Extreme Rules on October 8 after 98 days."),
            dict(year="2024", title="The Revenge Tour",
                 desc="Beats Becky Lynch for the Women's World Championship on May 25 at King and "
                      "Queen of the Ring, beats Rhea Ripley at SummerSlam as Dominik Mysterio turns, "
                      "joins and takes over The Judgment Day on August 5, and adds the inaugural "
                      "Crown Jewel Championship on November 2."),
            dict(year="2025", title="The reign ends, then the shoulder",
                 desc="Loses the title to Ripley on the January 6 Netflix premiere Raw at 226 days. "
                      "Dislocates a shoulder on June 16 and misses five and a half months, returning "
                      "at Survivor Series: WarGames on November 29. Voted Slammy Female Superstar of "
                      "the Year."),
            dict(year="2026", title="Rumble, reclamation, and a stingy reign",
                 desc="Wins the Royal Rumble from No. 14 on January 31, last eliminating Tiffany "
                      "Stratton; beats Stephanie Vaquer for the title at WrestleMania 42 on April 18; "
                      "is pinned by Iyo Sky in the non-title Queen of the Ring final on June 27; "
                      "retains over Sky at SummerSlam on August 1 in her first televised defence. "
                      "Vaquer's rematch is set for the September 7 Raw."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who she went to war with.",
        cards=[
            dict(name="Rhea Ripley",
                 desc="The career-defining feud. Morgan blamed Ripley for the 2023 shoulder injury, "
                      "took her title shot, her faction and Dominik Mysterio through 2024, and beat "
                      "her at SummerSlam on August 3. Ripley answered by ending the 226-day reign on "
                      "Raw's Netflix premiere, January 6, 2025. It is the rivalry that turned Morgan "
                      "from sympathetic loser into the division's best-organised villain."),
            dict(name="Ronda Rousey",
                 desc="The making of her: briefcase cash-in and pinfall on July 2, 2022, a "
                      "controversial SummerSlam retention where she was pinned while tapping, and the "
                      "Extreme Rules loss that October that ended the first reign. Rousey is the "
                      "biggest name on her ledger and the reason the ledger exists."),
            dict(name="Iyo Sky", slug="iyo-sky",
                 desc="The 2026 threat from the wrestling side of the roster: Sky pinned her clean in "
                      "the Queen of the Ring final on June 27 in Riyadh, and took her to 13:35 at "
                      "SummerSlam before the Codebreaker and Ob-Liv-ion - with Roxanne Perez and "
                      "Raquel Rodriguez working the margins. The clean tournament loss is the "
                      "asterisk her reign carries."),
            dict(name="Stephanie Vaquer",
                 desc="The live programme. Morgan took the title from her in about six minutes at "
                      "WrestleMania 42 on April 18, 2026, and Vaquer earned the rematch for the "
                      "September 7 Raw in Birmingham, Alabama - declaring on August 24 that she will "
                      "not need Becky Lynch's help. It is only the second defence of a reign whose "
                      "defence rate is itself the story."),
            dict(name="Becky Lynch", slug="becky-lynch",
                 desc="Two eras of the same feud: Morgan beat her for the Women's World Championship "
                      "at King and Queen of the Ring on May 25, 2024, and Lynch returned on the "
                      "August 3, 2026 Raw to call her a glorified valet over the infrequent "
                      "defences - throwing her into the barricade on August 17. No match has been "
                      "signed, but Lynch is the queue behind Vaquer."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Thin by design - the verified list is short, and nothing is added to pad it.",
        rows=[
            dict(when="2017&ndash;", title="WWE 2K", kind="Game",
                 desc="A playable fixture of the modern WWE 2K series. Her exact debut entry was not "
                      "verified in this pass, so no year is claimed for it."),
            dict(when="2025", title="Slammy Awards", kind="TV",
                 desc="Female Superstar of the Year, plus Villain of the Year shared with Dominik "
                      "Mysterio - WWE's own year-end recognition of the Judgment Day act."),
            dict(when="2024&ndash;", title="WWE digital and Netflix era programming", kind="TV",
                 desc="A centrepiece of Raw's Netflix era - her 226-day reign ended on the January 6, "
                      "2025 premiere episode. No film role, memoir or documentary special could be "
                      "verified, so none is listed."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, stated with the counting method shown - her career is unusually easy to "
             "miscount and this page refuses to.",
        stats=[
            ("3",    "World reigns, one lineage"),
            ("2026", "Royal Rumble winner"),
            ("8",    "Seconds in the 2019 Rumble"),
        ],
        rows=[
            dict(name="Three world championship reigns in a single lineage",
                 sub="98 days in 2022 (as the SmackDown Women's Championship), 226 days in 2024-25 "
                     "and the current reign from April 18, 2026 (as the Women's World Championship - "
                     "same belt, renamed June 2023). Wikipedia and Fightful say two-time under the "
                     "current name; TheSmackDownHotel says three-time across the lineage. Both are "
                     "printed; the belt agrees with the bigger number."),
            dict(name="2026 Royal Rumble winner",
                 sub="January 31, 2026, from the No. 14 spot, last eliminating Tiffany Stratton - "
                     "two months and two days after returning from a five-and-a-half-month shoulder "
                     "injury."),
            dict(name="Briefcase and world title in one night",
                 sub="July 2, 2022: won the women's Money in the Bank ladder match, then cashed in "
                     "on Ronda Rousey the same evening. It was the first championship of any kind in "
                     "her career."),
            dict(name="Inaugural WWE Women's Crown Jewel Champion",
                 sub="Beat WWE Women's Champion Nia Jax, champion vs. champion, at Crown Jewel in "
                     "Riyadh on November 2, 2024."),
            dict(name="Record four Women's Tag Team Championship reigns as one team",
                 sub="All with Raquel Rodriguez, 2023-2025. Two of the four ended because of Morgan's "
                     "own shoulder injuries rather than a losing fall - vacated in May 2023, and "
                     "replaced by Roxanne Perez in June 2025."),
            dict(name="Shortest women's Royal Rumble appearance ever: 8 seconds",
                 sub="January 27, 2019. Printed here because she cites it herself - the floor the "
                     "2026 Rumble win is measured from."),
            dict(name="Slammy Female Superstar of the Year, 2025",
                 sub="Plus Villain of the Year, shared with Dominik Mysterio - despite missing "
                     "nearly half of 2025 injured."),
        ],
        footnote=("No career win-loss total is published - none was verified. Height is Wikipedia's "
                  "5'3\"; TheSmackDownHotel bills her at 5'5\" and 125 lb, and the weight here is "
                  "theirs. Social handles are omitted as unverified. The first two tag reigns' "
                  "winning opponents were not verified, so those reigns appear in the title table "
                  "but not the match ledger."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Liv_Morgan"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/liv-morgan"),
        dict(k="Fightful", v="Vaquer challenge set for the September 7 Raw",
             href="https://www.fightful.com/wrestling/wwe-raw-stephanie-vaquer-liv-morgan-324290/"),
        dict(k="POST Wrestling", v="SummerSlam 2026 - retaining over Iyo Sky",
             href="https://www.postwrestling.com/2026/08/01/liv-morgan-retains-womens-world-championship-against-iyo-sky-at-summerslam/"),
        dict(k="SmackDown Hotel", v="Profile - the three-reign count",
             href="https://www.thesmackdownhotel.com/wrestlers/liv-morgan"),
        dict(k="Yahoo Sports", v="WrestleMania 42 full results",
             href="https://sports.yahoo.com/articles/wrestlemania-42-full-winners-list-042619263.html"),
        dict(k="Fightful", v="Raw results, August 24, 2026",
             href="https://www.fightful.com/wrestling/wwe-raw-results-8-24-2026-stephanie-vaquer-vs-roxanne-perez-solo-sikoa-penta-rey-fenix-more/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Liv Morgan a champion right now?",
            a="Yes. She is the reigning <b>Women's World Champion</b>, 135 days into the reign as of "
              "August 31, 2026, having beaten Stephanie Vaquer at WrestleMania 42 on April 18. She "
              "retained against Iyo Sky at SummerSlam on August 1 in the reign's first televised "
              "defence, and defends against Vaquer on the September 7 Raw in Birmingham, Alabama. "
              "Becky Lynch, who returned August 3 calling her a &ldquo;glorified valet,&rdquo; is "
              "circling the same title.",
            q_ld="Is Liv Morgan a champion right now?",
            a_ld="Yes. As of August 31, 2026 Liv Morgan is the reigning WWE Women's World Champion. "
                 "She won the title from Stephanie Vaquer at WrestleMania 42 on April 18, 2026, "
                 "retained it against Iyo Sky at SummerSlam on August 1, 2026, and is scheduled to "
                 "defend it against Stephanie Vaquer on the September 7, 2026 episode of Raw."),
        dict(
            q="Is Liv Morgan a two-time or three-time world champion?",
            a="Both answers are in print, and they describe the same career. Wikipedia and Fightful "
              "say <b>two-time Women's World Champion</b> &mdash; 2024 and the current reign &mdash; "
              "counting reigns under the current name. TheSmackDownHotel says <b>three-time</b>, "
              "adding her 2022 SmackDown Women's Championship reign, and that is the same belt: the "
              "title was renamed the Women's World Championship in June 2023. Counted by lineage, "
              "she is a three-time world champion: 98 days, 226 days, and the current reign.",
            q_ld="Is Liv Morgan a two-time or three-time world champion?",
            a_ld="Both figures appear in print because the title was renamed. Liv Morgan has three "
                 "world championship reigns in one lineage: the SmackDown Women's Championship in "
                 "2022 for 98 days, and the Women's World Championship - the same belt, renamed in "
                 "June 2023 - in 2024-25 for 226 days and again from April 18, 2026. Sources that "
                 "say two-time are counting only the reigns under the current name."),
        dict(
            q="Who leads The Judgment Day, and how did Liv Morgan end up in it?",
            a="She does &mdash; the women's side outright, and in practice most of the rest. She "
              "joined on August 5, 2024, two days after beating Rhea Ripley at SummerSlam with "
              "Dominik Mysterio's help, and the group excommunicated Ripley and Damian Priest in the "
              "takeover. The 2026 roster around her: Dominik Mysterio, Raquel Rodriguez, Roxanne "
              "Perez and JD McDonagh. Rodriguez and Perez ran interference in her SummerSlam 2026 "
              "defence against Iyo Sky, which is the standing pattern of the reign.",
            q_ld="How did Liv Morgan become the leader of The Judgment Day?",
            a_ld="Liv Morgan joined The Judgment Day on August 5, 2024, two days after defeating Rhea "
                 "Ripley at SummerSlam with Dominik Mysterio turning to her side. The group then "
                 "excommunicated Rhea Ripley and Damian Priest, and Morgan has led its women's wing "
                 "since, alongside Dominik Mysterio, Raquel Rodriguez, Roxanne Perez and JD McDonagh. "
                 "Rodriguez and Perez interfered in her SummerSlam 2026 title defence against Iyo "
                 "Sky."),
        dict(
            q="Why is Liv Morgan's current reign criticised, and what happens September 7?",
            a="Defence rate. Between WrestleMania 42 on April 18 and SummerSlam on August 1 &mdash; "
              "105 days &mdash; she made no televised defence, a gap Becky Lynch turned into the "
              "&ldquo;glorified valet&rdquo; storyline on returning August 3. She was also pinned "
              "clean by Iyo Sky in the <i>non-title</i> Queen of the Ring final on June 27. The "
              "September 7 Raw defence against Stephanie Vaquer &mdash; announced August 24, after "
              "Vaquer beat Roxanne Perez &mdash; is only the reign's second, and Vaquer says she "
              "will not need Becky Lynch's help to take the title back.",
            q_ld="Why is Liv Morgan's 2026 title reign criticised?",
            a_ld="Because of its defence rate. Liv Morgan made no televised defence of the Women's "
                 "World Championship between winning it at WrestleMania 42 on April 18, 2026 and "
                 "SummerSlam on August 1, 2026, and she was pinned cleanly by Iyo Sky in the "
                 "non-title Queen of the Ring final on June 27. Becky Lynch returned on August 3 "
                 "calling her a glorified valet, and Stephanie Vaquer challenges her on the "
                 "September 7 Raw in only the second defence of the reign."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Gionna Jene Daddio"),
        dict(label="Born", value="June 8, 1994", sub="Morristown, New Jersey &middot; age 32"),
        dict(label="Billed from", value="Elmwood Park, New Jersey",
             sub="per Wikipedia &middot; SmackDown Hotel says Paramus"),
        dict(label="Height", value="5&#8242;3&#8243;",
             sub="160 cm per Wikipedia &middot; SmackDown Hotel bills 5&#8242;5&#8243;"),
        dict(label="Weight", value="125 lb", sub="57 kg per SmackDown Hotel"),
        dict(label="Debut", value="2015", sub="planted-fan cameo in February; in-ring from November"),
        dict(label="Trained by", value="WWE Performance Center"),
        dict(label="Finishers", value="Ob-Liv-ion &middot; Liv Kick (earlier)",
             sub="springboard reverse STO, since January 2020"),
        dict(label="Faction", value="The Judgment Day", sub="leader, since August 5, 2024"),
        dict(label="Brand", value="Raw"),
        dict(label="Title", value="Women's World Champion",
             sub="since April 18, 2026 &middot; 135 days as of August 31"),
        dict(label="Also known as", value="Marley (2015) &middot; The Riott Squad&rsquo;s Liv"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1994-06-08",
    bornplace="Morristown, New Jersey, United States",
    nationality="United States",
    height_cm=160,
    weight_kg=57,
    ld=dict(
        alternateName=["Gionna Jene Daddio", "Gionna Daddio", "Marley"],
        award=["Women's World Championship / SmackDown Women's Championship (3 reigns in the lineage)",
               "WWE Women's Tag Team Championship (4 reigns, with Raquel Rodriguez)",
               "WWE Women's Crown Jewel Championship (inaugural, 2024)",
               "Women's Money in the Bank winner (2022)",
               "Women's Royal Rumble winner (2026)",
               "Slammy Award for Female Superstar of the Year (2025)",
               "Slammy Award for Villain of the Year (2025, with Dominik Mysterio)"],
        knowsAbout=["Professional wrestling", "WWE", "Women's professional wrestling",
                    "The Judgment Day", "Championship wrestling"],
        description="Liv Morgan, born Gionna Jene Daddio, is an American professional wrestler "
                    "signed to WWE and the reigning Women's World Champion. She has three world "
                    "championship reigns in the SmackDown Women's / Women's World Championship "
                    "lineage, won the 2022 women's Money in the Bank ladder match and cashed it in "
                    "the same night on Ronda Rousey, won the 2026 women's Royal Rumble, is the "
                    "inaugural WWE Women's Crown Jewel Champion, a four-time Women's Tag Team "
                    "Champion with Raquel Rodriguez, and the leader of The Judgment Day.",
        sameAs=["https://en.wikipedia.org/wiki/Liv_Morgan",
                "https://www.wwe.com/superstars/liv-morgan"],
    ),
)
