# -*- coding: utf-8 -*-
"""Bron Breakker - dossier data.

Sources: web research compiled August 31, 2026 - Wikipedia (Bron Breakker, The Vision),
WWE.com (official profile, Raw and Sunday Night's Main Event previews), Wrestling Inc.
(Raw results, August 24, 2026), GiveMeSport (Royal Rumble masked-man report), Last Word
on Sports. Every match row carries a day-precision date stated in one of those sources.

Deliberate omissions and flags:
  * No career win-loss total: no source publishes a verified one.
  * No social links: no handle could be verified as official in this pass.
  * WWE.com's profile still lists him as the reigning World Tag Team Champion; he and
    Austin Theory lost the titles to the Street Profits on the June 22, 2026 Raw. The
    page flags the lag rather than repeating it.
  * Height and weight conflict: WWE bills 6'0" and 250 lb; Wikipedia gives 5'10" and
    223 lb. The billed figures are used and the conflict is printed.
  * The identity of the masked man who caused his 2026 Royal Rumble elimination has
    never been confirmed on WWE programming. A High Spots Podcast report (via
    GiveMeSport) named Grayson Waller as a stand-in dressed to resemble Seth Rollins.
    Reported, not asserted.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2021-09-14", promo="WWE", landmark=True,
         event="NXT 2.0 premiere", opponent="LA Knight",
         stip="Singles — televised debut", title=""),
    dict(result="W", date="2022-01-04", promo="WWE", landmark=True,
         event="NXT New Year's Evil", opponent="Tommaso Ciampa",
         stip="Singles — first NXT Championship", title="NXT Championship"),
    dict(result="L", date="2022-03-08", promo="WWE", type="tag",
         event="NXT Roadblock", opponent="Dolph Ziggler & Tommaso Ciampa",
         stip="Triple threat — Ziggler pins Ciampa to take the title",
         title="NXT Championship"),
    dict(result="W", date="2022-04-04", promo="WWE", landmark=True,
         event="Raw", opponent="Dolph Ziggler",
         stip="Singles — regains the title on the main-roster show",
         title="NXT Championship"),
    dict(result="W", date="2022-09-04", promo="WWE", landmark=True,
         event="NXT Worlds Collide", opponent="Tyler Bate",
         stip="Winner-takes-all — unifies the NXT and NXT UK Championships",
         title="NXT Championship"),
    dict(result="L", date="2023-04-01", promo="WWE", landmark=True,
         event="NXT Stand & Deliver", opponent="Carmelo Hayes",
         stip="Singles — the 362-day reign ends", title="NXT Championship"),
    dict(result="W", date="2024-08-03", promo="WWE", landmark=True,
         event="SummerSlam — Cleveland", opponent="Sami Zayn",
         stip="Singles — first main-roster title", title="WWE Intercontinental Championship"),
    dict(result="L", date="2024-09-23", promo="WWE",
         event="Raw", opponent="Jey Uso",
         stip="Singles — 51-day reign ends", title="WWE Intercontinental Championship"),
    dict(result="W", date="2024-10-21", promo="WWE",
         event="Raw", opponent="Jey Uso",
         stip="Singles — regains the title amid Bloodline interference",
         title="WWE Intercontinental Championship"),
    dict(result="L", date="2025-04-20", promo="WWE", type="tag", landmark=True,
         event="WrestleMania 41 Night 2", opponent="Dominik Mysterio, Penta & Finn Balor",
         stip="Fatal four-way — Mysterio takes the title; the 181-day reign ends",
         title="WWE Intercontinental Championship"),
    dict(result="W", date="2025-09-20", promo="WWE", type="tag",
         event="Wrestlepalooza — Indianapolis", opponent="The Usos",
         stip="Tag — with Bronson Reed", title=""),
    dict(result="W", date="2025-11-29", promo="WWE", type="tag", landmark=True,
         event="Survivor Series: WarGames", opponent="CM Punk, Cody Rhodes, Roman Reigns & The Usos",
         stip="WarGames — pins Punk after interference from a hooded Austin Theory", title=""),
    dict(result="L", date="2026-01-05", promo="WWE",
         event="Raw — Netflix anniversary show", opponent="CM Punk",
         stip="Singles — challenge", title="World Heavyweight Championship"),
    dict(result="L", date="2026-01-31", promo="WWE", type="tag",
         event="Royal Rumble match — Riyadh", opponent="The 2026 Royal Rumble field",
         stip="Blindsided by a masked man on the ramp; eliminated by Oba Femi in seconds",
         title=""),
    dict(result="W", date="2026-05-09", promo="WWE", landmark=True,
         event="Backlash", opponent="Seth Rollins",
         stip="Singles — beats the man who built The Vision", title=""),
    dict(result="L", date="2026-06-22", promo="WWE", type="tag",
         event="Raw", opponent="The Street Profits",
         stip="Tag — with Austin Theory; Joe Hendry and Seth Rollins interfere",
         title="World Tag Team Championship"),
    dict(result="L", date="2026-06-27", promo="WWE", landmark=True,
         event="Night of Champions — Riyadh", opponent="Seth Rollins",
         stip="Steel cage — Rollins ends the feud", title=""),
]

DATA = dict(
    slug="bron-breakker",
    name="Bron Breakker",
    realname="Bronson Rechsteiner",
    epithet="The Dog",
    hook="Record & Titles",

    meta_desc=("Bron Breakker, son of Rick Steiner, is a two-time NXT Champion and two-time "
               "Intercontinental Champion who faces Oba Femi at Sunday Night's Main Event. Full "
               "record, titles, factions, records and career."),
    og_desc=("The Dog: two NXT Championship reigns including 362 days, two Intercontinental "
             "reigns, The Vision, and a September 6 showdown with Oba Femi over which of them "
             "is WWE's future."),
    tw_desc="Two NXT titles, two Intercontinental titles, The Vision — and Oba Femi on September 6.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2020",
    height_imp="6&#8242;0&#8243;",
    weight_lb="250",
    world_titles="0",
    vitals_tagline="Steiner blood",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="BB", title="WWE Shop", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable in 2K23 through 2K26",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="NFL", title="Madden NFL 21", sub="As a Baltimore Ravens fullback",
             tag="Play", href="https://www.ea.com/games/madden-nfl"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/bron-breakker"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Second-generation Steiner &middot; The Dog of NXT &middot; The Big Bad Booty Nephew",
    hero_tag="Woodstock, Georgia &middot; <em>NXT &middot; WWE &middot; 2020&ndash;present</em>",
    now_label="NOW",
    now_bold="Raw, no championship",
    now_tail=" &middot; signed to face Oba Femi at Sunday Night&rsquo;s Main Event on September 6 "
             "after the August 24 contract-signing brawl",
    hstats=[
        dict(value="2",   x=True,  label="NXT Titles"),
        dict(value="362", x=False, label="Day NXT Reign"),
        dict(value="2",   x=True,  label="IC Titles"),
        dict(value="2022", x=False, label="WON Rookie of the Year"),
    ],
    ghost_link="From Kennesaw State fullback to the man who exiled Seth Rollins",
    vlabel="Est. 2020 &middot; Woodstock, Georgia",
    mono="BB",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Bron Breakker</b> is the fastest-moving second-generation act of his era, and the "
        "collision he is walking into is the reason this page exists in its current form. He is "
        "the son of Rick Steiner and the nephew of Scott Steiner, a former Kennesaw State running "
        "back and Baltimore Ravens fullback who had his first professional match in October 2020 "
        "and held the NXT Championship fourteen months later. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">362</span>'
        '<span class="pull-cap">days in his second NXT Championship reign, ended by Carmelo Hayes at Stand &amp; Deliver 2023</span></span>'
        "He is a two-time NXT Champion, a two-time Intercontinental Champion, a Dusty Rhodes Tag "
        "Team Classic winner, the Wrestling Observer Newsletter&rsquo;s 2022 Rookie of the Year "
        "&mdash; and, as of August 31, 2026, a man with no championship and one match booked: "
        "Oba Femi, Sunday Night&rsquo;s Main Event, September 6, over the explicit question of "
        "which of them is WWE&rsquo;s future.",

        "Two things the record needs set straight. First, WWE.com&rsquo;s own profile still lists "
        "him as the reigning World Tag Team Champion; he is not. He and Austin Theory lost the "
        "titles to the Street Profits on the June 22, 2026 Raw, with Joe Hendry and Seth Rollins "
        "interfering, and the July 6 rematch did not bring them back. The reign itself needs a "
        "footnote too: the 84 days usually quoted belong to the championship run Logan Paul and "
        "Theory started on March 30, 2026 &mdash; Breakker was only added on May 25, under the "
        "Freebird Rule, after Paul tore a tricep, so his own recognised share of it is 28 days. "
        "Second, his listed size depends on who is doing the listing: WWE bills 6&#8242;0&#8243; "
        "and 250 pounds, Wikipedia records 5&#8242;10&#8243; and 223. The billed figures are used "
        "on this page and the gap is printed rather than papered over.",

        "The rise was nearly vertical. He debuted on the September 14, 2021 NXT 2.0 premiere "
        "against LA Knight, beat Tommaso Ciampa for the NXT Championship at New Year&rsquo;s Evil "
        "on January 4, 2022, lost it in a March triple threat without being pinned, and took it "
        "back from Dolph Ziggler on the April 4, 2022 Raw. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">2</span>'
        '<span class="pull-cap">Intercontinental Championship reigns &mdash; 51 days from SummerSlam 2024, then 181 more from October</span></span>'
        "The second reign ran 362 days and unified the NXT and NXT UK titles over Tyler Bate at "
        "Worlds Collide on September 4, 2022, before Carmelo Hayes ended it at Stand &amp; "
        "Deliver on April 1, 2023. On the main roster he won the Intercontinental Championship "
        "from Sami Zayn at SummerSlam on August 3, 2024 &mdash; the same Cleveland night Gunther "
        "won his first world title &mdash; traded it with Jey Uso that autumn, and held it 181 "
        "days until Dominik Mysterio took it in a fatal four-way at WrestleMania 41 Night 2 on "
        "April 20, 2025.",

        "Then came The Vision, and the war that followed it. He joined Seth Rollins&rsquo; "
        "Paul Heyman-managed faction in the weeks after WrestleMania 41, pinned CM Punk in the "
        "November 29, 2025 WarGames match, and in October 2025 turned on Rollins and exiled him "
        "from the group with a spear &mdash; WWE.com&rsquo;s profile now tells that part itself. "
        "2026 has been a ledger of near-misses: a failed World Heavyweight Championship challenge "
        "against Punk on the January 5 Raw; a Royal Rumble that ended in seconds on January 31, "
        "when a masked man blindsided him on the ramp and Oba Femi threw him out &mdash; a report "
        "relayed by GiveMeSport named Grayson Waller as the masked man, dressed to resemble "
        "Rollins, and WWE has never confirmed it on screen; a win over Rollins at Backlash on May "
        "9; the tag title loss on June 22; and the steel cage defeat to Rollins at Night of "
        "Champions on June 27 that ended the feud. Since August 10, when Femi shut down a Vision "
        "beatdown and confronted him, everything has pointed at September 6. At the August 24 "
        "contract signing he blindsided Femi, watched Femi put Theory through a table, and told "
        "him he would live in his shadow. Femi signed anyway.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE"],
        promo_labels={"WWE": "WWE"},
        stats=[
            ("2&times;", "NXT Championship"),
            ("362",      "Day NXT reign"),
            ("2&times;", "Intercontinental"),
            ("1",        "Dusty Classic"),
            ("2022",     "WON Rookie of the Year"),
            ("28",       "Recognised tag-title days"),
        ],
        lead=("Seventeen documented bouts &mdash; the NXT title changes, the Intercontinental "
              "trades with Jey Uso, and the full 2026 arc from the Punk challenge to the Rollins "
              "cage match. This is a curated ledger, not a career count, and no win&ndash;loss "
              "total is published because no source verifies one. The Royal Rumble row carries "
              "the masked-man caveat: the attacker&rsquo;s identity has been reported (Grayson "
              "Waller, per a High Spots Podcast report relayed by GiveMeSport) but never "
              "confirmed on WWE programming. Filter by match type, tap any column header to "
              "sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("No list is published here. No Wrestling Observer star ratings for his "
                    "matches could be verified in this research pass, and this page does not "
                    "assign its own. The bouts most often cited as his best &mdash; the Zayn "
                    "match at SummerSlam 2024, the WarGames matches of 2024 and 2025, the "
                    "Rollins series of 2026 &mdash; are all in the record table above with "
                    "dates and outcomes."),
    signature_count_word="none",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("2&times;", "NXT Championship"),
            ("2&times;", "Intercontinental"),
            ("1",        "NXT Tag reign"),
            ("28",       "World Tag days recognised"),
        ],
        lead=("Six championship reigns across five years, none of them a world title yet &mdash; "
              "his two world-title matches, against Seth Rollins in 2023 and CM Punk in 2026, "
              "were both losses. The World Tag Team Championship entry carries the Freebird Rule "
              "asterisk in full."),
        rows=[
            dict(ic="N", name="NXT Championship", count="2",
                 sub="2022 &middot; def. Tommaso Ciampa at New Year&rsquo;s Evil on January 4, "
                     "lost in the March 8 Roadblock triple threat without being pinned &mdash; 63 "
                     "days &middot; 2022&ndash;23 &middot; def. Dolph Ziggler on the April 4 Raw, "
                     "lost to Carmelo Hayes at Stand &amp; Deliver on April 1, 2023 &mdash; "
                     "<b>362 days</b>, absorbing the NXT UK Championship from Tyler Bate at "
                     "Worlds Collide along the way"),
            dict(ic="I", name="WWE Intercontinental Championship", count="2",
                 sub="2024 &middot; def. Sami Zayn at SummerSlam on August 3, lost to Jey Uso on "
                     "the September 23 Raw &mdash; 51 days &middot; 2024&ndash;25 &middot; "
                     "regained from Uso on the October 21 Raw, lost to Dominik Mysterio in the "
                     "WrestleMania 41 Night 2 fatal four-way on April 20, 2025 &mdash; <b>181 "
                     "days</b>"),
            dict(ic="T", name="World Tag Team Championship", count="1",
                 sub="2026 &middot; recognised as champion with Austin Theory from <b>May 25</b> "
                     "under the Freebird Rule, after Logan Paul &mdash; who had won the titles "
                     "with Theory from The Usos in a Street Fight on March 30 &mdash; tore a "
                     "tricep &middot; lost to the Street Profits on the June 22 Raw &middot; the "
                     "84 days Wikipedia logs belong to the reign as a whole; Breakker&rsquo;s own "
                     "recognised share is 28"),
            dict(ic="D", name="NXT Tag Team Championship", count="1",
                 sub="2024 &middot; with Baron Corbin, after winning the Dusty Rhodes Tag Team "
                     "Classic &middot; retained against Axiom &amp; Nathan Frazer at Stand &amp; "
                     "Deliver, lost the rematch on the April 9, 2024 NXT &mdash; his final NXT "
                     "match &middot; Wikipedia dates the win to January 2024; the exact change "
                     "date was not verified in this pass"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="One tag team with a name, and one faction he joined, inherited and now fronts.",
        cards=[
            dict(era="NXT &middot; 2023&ndash;24",
                 name="The Wolf Dogs",
                 members="Bron Breakker, Baron Corbin",
                 desc="The odd-couple pairing that carried his last NXT stretch: they won the "
                      "2024 Dusty Rhodes Tag Team Classic and the NXT Tag Team Championship, and "
                      "the April 9, 2024 rematch loss to Axiom and Nathan Frazer was the last "
                      "match Breakker wrestled in NXT before the main-roster draft."),
            dict(era="WWE &middot; 2025 &middot; the Rollins era",
                 name="The Vision, under Seth Rollins",
                 members="Seth Rollins, Paul Heyman, Bron Breakker, Bronson Reed; Logan Paul and "
                         "Austin Theory joined after Survivor Series 2025",
                 desc="Formed in the weeks after WrestleMania 41, when Rollins and Heyman turned "
                      "on CM Punk and Roman Reigns. Breakker was the faction's enforcer through "
                      "2025: the Wrestlepalooza tag win over The Usos with Bronson Reed on "
                      "September 20, and the WarGames win on November 29, where he pinned Punk "
                      "after a hooded Austin Theory interfered. Becky Lynch's reported "
                      "association with the group is covered on her page; Wikipedia's member "
                      "table does not include her."),
            dict(era="WWE &middot; October 2025&ndash;present &middot; the Breakker era",
                 name="The Vision, under Bron Breakker",
                 members="Bron Breakker, Bronson Reed, Austin Theory, Paul Heyman",
                 desc="In October 2025 Breakker turned on Rollins and exiled him from the faction "
                      "with a spear — a version of events WWE.com's own profile now leads with. "
                      "The takeover bought him a war he eventually lost: Rollins beat him in the "
                      "Night of Champions steel cage on June 27, 2026, after Breakker had won at "
                      "Backlash on May 9. The group remains intact around him — it was a Vision "
                      "beatdown that Oba Femi interrupted on the August 10 Raw, and Theory who "
                      "went through a table at the August 24 contract signing. Heyman's position "
                      "is the open question: he brokered the Femi match with Adam Pearce, and has "
                      "been conspicuously respectful of the opponent."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One ring name, several designations &mdash; the gimmick has always been the "
             "bloodline and the output, not a costume.",
        cards=[
            dict(mono="FB", era="Football &middot; 2016&ndash;2020", name="Bronson Rechsteiner",
                 desc="Kennesaw State running back and fullback, then an undrafted free agent "
                      "with the Baltimore Ravens in 2020, released that August. He appears in "
                      "Madden NFL 21 as a Raven — almost certainly the only man on the roster "
                      "with that particular credit."),
            dict(mono="BB", era="NXT &middot; 2021&ndash;24", name="Bron Breakker",
                 desc="WWE renamed him on arrival — the Steiner surname stayed off screen, the "
                      "Steiner offence did not. The gorilla press powerslam, the spear and his "
                      "uncle's Steiner Recliner all survived the rebrand. Vic Joseph once "
                      "introduced him on NXT commentary as \"the Big Bad Booty Nephew,\" a nod "
                      "to Scott Steiner that stuck as a fan nickname; Breakker's own preferred "
                      "designation, coined on the road to NXT Deadline, was \"the Dog of NXT.\""),
            dict(mono="EN", era="WWE &middot; 2024&ndash;25", name="The Vision's enforcer",
                 desc="The main-roster heel run: Intercontinental Champion twice, then the "
                      "attack-dog of Seth Rollins' faction, booked as the man who hits harder "
                      "than the plan requires. The WarGames pin on CM Punk was the peak of the "
                      "role."),
            dict(mono="LD", era="WWE &middot; 2025&ndash;present", name="Leader of The Vision",
                 desc="Since exiling Rollins in October 2025 he has fronted the group himself — "
                      "WWE.com calls him an unpredictable force, which is the polite version of "
                      "a man who speared his own faction leader. The Oba Femi program is the "
                      "first time the character has been asked to defend the premise that he, "
                      "and not somebody newer, is the future."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="From the Ravens' practice squad to a September 6 answer to the only question that "
             "matters to him.",
        rows=[
            dict(year="2020", title="Football ends, wrestling begins",
                 desc="Released by the Baltimore Ravens in August; debuts at WrestleJam 8 in "
                      "Ringgold, Georgia on October 8, beating Jamie Hall."),
            dict(year="2021", title="Signs with WWE; NXT 2.0 debut",
                 desc="Signs a developmental deal in February; debuts on the September 14 NXT "
                      "2.0 premiere against LA Knight."),
            dict(year="2022", title="Two NXT Championship reigns",
                 desc="Beats Tommaso Ciampa at New Year's Evil on January 4; loses the title in "
                      "a March triple threat without being pinned; regains it from Dolph Ziggler "
                      "on the April 4 Raw and unifies it with the NXT UK title over Tyler Bate "
                      "at Worlds Collide on September 4. Named WON Rookie of the Year."),
            dict(year="2023", title="The 362-day reign ends",
                 desc="Carmelo Hayes beats him at Stand & Deliver on April 1. He challenges Seth "
                      "Rollins for the World Heavyweight Championship at NXT Gold Rush on June "
                      "20 and loses — a detail the 2026 feud never mentioned."),
            dict(year="2024", title="Dusty Classic, call-up, Intercontinental gold",
                 desc="Wins the Dusty Rhodes Tag Team Classic and NXT tag titles with Baron "
                      "Corbin; moves to Raw; beats Sami Zayn for the Intercontinental "
                      "Championship at SummerSlam on August 3, loses it to Jey Uso in September "
                      "and takes it back on October 21."),
            dict(year="2025", title="WrestleMania loss, The Vision, WarGames",
                 desc="Dominik Mysterio takes the IC title in the WrestleMania 41 fatal four-way "
                      "on April 20. Breakker joins Seth Rollins' new faction, turns on him in "
                      "October and exiles him, and pins CM Punk in WarGames on November 29."),
            dict(year="2026", title="Near-misses, a cage loss, and Oba Femi",
                 desc="Fails to take the World Heavyweight title from Punk on January 5; lasts "
                      "seconds in the Royal Rumble after a masked-man attack, thrown out by Oba "
                      "Femi; costs Rollins his WrestleMania 42 match with a spear; beats Rollins "
                      "at Backlash on May 9 and loses the steel cage at Night of Champions on "
                      "June 27; loses the tag titles on June 22; signs for Femi at Sunday "
                      "Night's Main Event, September 6."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Seth Rollins",
                 desc="The defining feud of the main-roster run so far, and it ran in both "
                      "directions: Rollins recruited him into The Vision in 2025, Breakker "
                      "exiled Rollins from it with a spear in October, and 2026 settled it in "
                      "instalments — Breakker's interference cost Rollins against Gunther at "
                      "WrestleMania 42 Night 1 on April 18, Breakker won Backlash on May 9, and "
                      "Rollins won the steel cage at Night of Champions on June 27 to close the "
                      "book. Rollins also helped take the tag titles off him five days before "
                      "the cage match."),
            dict(name="Jey Uso", slug="jey-uso",
                 desc="The Intercontinental trade of autumn 2024 — Uso took the title on the "
                      "September 23 Raw, Breakker took it back on October 21 with the Bloodline "
                      "involved. It mattered because the second reign, at 181 days, is the one "
                      "his main-roster credibility is built on."),
            dict(name="CM Punk", slug="cm-punk",
                 desc="Breakker pinned Punk in the November 29, 2025 WarGames match — with a "
                      "hooded Austin Theory's help — and then failed to take Punk's World "
                      "Heavyweight Championship on the January 5, 2026 Raw. The pattern of the "
                      "whole 2026 ledger in miniature: he can hurt the top of the card, and has "
                      "not yet beaten it when it counts."),
            dict(name="Carmelo Hayes",
                 desc="The man who ended the 362-day NXT reign at Stand & Deliver on April 1, "
                      "2023, in the match most NXT-era retrospectives treat as the changing of "
                      "the guard."),
            dict(name="Oba Femi",
                 desc="The live one, and it started before either man acknowledged it: Femi "
                      "threw a just-ambushed Breakker out of the 2026 Royal Rumble in seconds. "
                      "It became a program on the August 10 Raw, when Femi shut down a Vision "
                      "beatdown; Paul Heyman and Adam Pearce turned the stare-downs into a match "
                      "on August 17; and the August 24 contract signing ended with Austin Theory "
                      "through a table and Femi promising Breakker would spend September 6 "
                      "running. The stated stakes — which man is WWE's future — are for once the "
                      "actual stakes."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="Short list, one genuinely unusual entry.",
        rows=[
            dict(when="2020", title="Madden NFL 21", kind="Game",
                 desc="Appears as a Baltimore Ravens fullback — the football career preserved in "
                      "a video game before the wrestling one began."),
            dict(when="2023&ndash;", title="WWE 2K", kind="Game",
                 desc="Playable in WWE 2K23, 2K24, 2K25 and 2K26."),
            dict(when="2025", title="Intuit commercial", kind="TV",
                 desc="A national ad spot, per Wikipedia — his only non-WWE screen credit to "
                      "date. No documentary, film or scripted role could be verified, so none "
                      "is listed."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records and the asterisks, including two his own employer's website gets "
             "wrong.",
        stats=[
            ("362", "Day NXT reign"),
            ("181", "Day IC reign"),
            ("14",  "Months, debut to NXT title"),
        ],
        rows=[
            dict(name="NXT Champion fourteen months after his first match",
                 sub="First match October 8, 2020; NXT Championship January 4, 2022. The second "
                     "reign ran 362 days and unified the NXT UK title into the NXT Championship "
                     "at Worlds Collide."),
            dict(name="Wrestling Observer Newsletter Rookie of the Year, 2022",
                 sub="Plus a No. 6 ranking on both ESPN's and PWI's 2023 lists of the best "
                     "wrestlers under 30, per Wikipedia."),
            dict(name="Two-time Intercontinental Champion at 27",
                 sub="51 days from SummerSlam 2024, then 181 days from October 21, 2024 to "
                     "WrestleMania 41. Both reigns ended against members of the Bloodline-Judgment "
                     "Day axis — Jey Uso, then Dominik Mysterio."),
            dict(name="Pinned CM Punk in WarGames",
                 sub="November 29, 2025, for the Breakker-Reed-Paul-McIntyre-Lesnar team, after "
                     "interference from a hooded figure later revealed as Austin Theory."),
            dict(name="World Tag Team Champion for 28 recognised days",
                 sub="Added via the Freebird Rule on May 25, 2026 after Logan Paul's tricep "
                     "injury; lost with Austin Theory to the Street Profits on June 22. The "
                     "84-day figure in circulation is the length of the Paul-Theory reign as a "
                     "whole, not of Breakker's share — and WWE.com's profile still lists him as "
                     "champion, which he has not been since June."),
            dict(name="Eliminated from the 2026 Royal Rumble in seconds",
                 sub="Blindsided by a masked man on the ramp, then thrown out by Oba Femi almost "
                     "immediately — the seed of the September 6 match. The masked man has never "
                     "been identified on WWE television; a High Spots Podcast report relayed by "
                     "GiveMeSport named Grayson Waller, dressed to resemble Seth Rollins. This "
                     "page reports the report."),
            dict(name="A 0-2 record in world championship matches",
                 sub="Seth Rollins at NXT Gold Rush on June 20, 2023, and CM Punk on the January "
                     "5, 2026 Raw. Worth stating plainly because the Oba Femi program is "
                     "explicitly about who gets there first."),
        ],
        footnote=("Deliberately absent: a career win-loss record, which no source verifies; "
                  "social handles, which could not be confirmed as official; and any Wrestling "
                  "Observer star ratings, none of which were verified for his matches in this "
                  "pass. WWE.com's stale tag-champion listing and the 6'0\"/250 vs 5'10\"/223 "
                  "size conflict are printed above rather than resolved."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/bron-breakker"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Bron_Breakker"),
        dict(k="Wikipedia", v="The Vision — faction history",
             href="https://en.wikipedia.org/wiki/The_Vision_(professional_wrestling)"),
        dict(k="Wrestling Inc.", v="Raw results, August 24, 2026 — the contract signing",
             href="https://www.wrestlinginc.com/2243203/wwe-raw-august-24-stephanie-vaquer-roxanne-perez-contract-signing-more/"),
        dict(k="WWE.com", v="Sunday Night's Main Event preview — Femi vs. Breakker",
             href="https://www.wwe.com/shows/snme/2026-09-06/oba-femi-vs-bron-breakker"),
        dict(k="GiveMeSport", v="The Royal Rumble masked-man report",
             href="https://www.givemesport.com/bron-breakker-royal-rumble-attacker-identity-revealed-wwe/"),
        dict(k="Last Word on Sports", v="Femi vs. Breakker — the stakes",
             href="https://lastwordonsports.com/prowrestling/2026/08/16/oba-femi-vs-bron-breakker-who-can-afford-to-lose/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="When does Bron Breakker face Oba Femi, and how was the match made?",
            a="Sunday Night&rsquo;s Main Event on <b>September 6, 2026</b>, their first "
              "singles match. Femi stopped a Vision beatdown and confronted Breakker on the "
              "August 10 Raw; Paul Heyman stepped between them on August 17 and, with Raw "
              "general manager Adam Pearce, arranged the match; and the August 24 contract "
              "signing collapsed into a brawl &mdash; Breakker blindsided Femi, Femi put Austin "
              "Theory through a ringside table and signed the contract himself. The prior "
              "history is thin but pointed: Femi eliminated a just-ambushed Breakker from the "
              "Royal Rumble in seconds on January 31.",
            q_ld="When does Bron Breakker face Oba Femi?",
            a_ld="Bron Breakker faces Oba Femi at WWE Sunday Night's Main Event on September 6, "
                 "2026, in their first singles match. The match was arranged by Paul Heyman and "
                 "Raw general manager Adam Pearce after confrontations on the August 10 and "
                 "August 17, 2026 episodes of Raw, and the August 24 contract signing ended in "
                 "a brawl in which Oba Femi put Austin Theory through a table and signed the "
                 "contract. Femi had eliminated Breakker from the 2026 Royal Rumble in seconds "
                 "on January 31, 2026, after a masked man attacked Breakker."),
        dict(
            q="Is Bron Breakker a champion right now?",
            a="No, as of August 31, 2026 &mdash; and this needs saying because WWE.com&rsquo;s "
              "own profile still lists him as World Tag Team Champion. He and Austin Theory "
              "lost those titles to the Street Profits on the <b>June 22, 2026</b> Raw, and the "
              "July 6 rematch failed. His last singles title was the Intercontinental "
              "Championship, lost at WrestleMania 41 on April 20, 2025. He has never held a "
              "world championship: his two world title matches, against Seth Rollins in 2023 "
              "and CM Punk in January 2026, were both losses.",
            q_ld="Is Bron Breakker a champion right now?",
            a_ld="No. As of August 31, 2026 Bron Breakker holds no championship, although "
                 "WWE.com's profile still lists him as World Tag Team Champion. He and Austin "
                 "Theory lost the World Tag Team Championship to the Street Profits on the June "
                 "22, 2026 episode of Raw. His most recent singles title was the WWE "
                 "Intercontinental Championship, which he lost at WrestleMania 41 on April 20, "
                 "2025, and he has never held a world championship."),
        dict(
            q="Who attacked Bron Breakker at the 2026 Royal Rumble?",
            a="Officially, nobody knows &mdash; WWE has never confirmed the masked man&rsquo;s "
              "identity on television. A High Spots Podcast report relayed by GiveMeSport "
              "named <b>Grayson Waller</b>, brought in from NXT and dressed to resemble Seth "
              "Rollins. What is on the record: the masked man blindsided Breakker on the ramp "
              "on January 31, 2026, and Oba Femi eliminated him within seconds of his entering "
              "the ring. The Rollins feud that consumed his spring &mdash; Backlash, the Night "
              "of Champions cage &mdash; grew directly out of that night.",
            q_ld="Who was the masked man who attacked Bron Breakker at the 2026 Royal Rumble?",
            a_ld="WWE has never confirmed the masked man's identity on television. A High Spots "
                 "Podcast report relayed by GiveMeSport identified Grayson Waller as the "
                 "attacker, reportedly dressed to resemble Seth Rollins. The masked man "
                 "blindsided Bron Breakker on the entrance ramp at the Royal Rumble on January "
                 "31, 2026, and Oba Femi eliminated Breakker within seconds."),
        dict(
            q="Is Bron Breakker related to the Steiner Brothers?",
            a="Yes &mdash; directly. He was born Bronson Rechsteiner, son of <b>Rick "
              "Steiner</b> and nephew of <b>Scott Steiner</b>; Rechsteiner is the family's "
              "actual surname. The inheritance is visible in the move set &mdash; the gorilla "
              "press powerslam and the Steiner Recliner both come from the family playbook "
              "&mdash; and in the nickname commentary hung on him in NXT: &ldquo;the Big Bad "
              "Booty Nephew,&rdquo; after his uncle&rsquo;s Big Bad Booty Daddy.",
            q_ld="Is Bron Breakker related to the Steiner Brothers?",
            a_ld="Yes. Bron Breakker was born Bronson Rechsteiner and is the son of Rick "
                 "Steiner and the nephew of Scott Steiner of the Steiner Brothers. His move "
                 "set includes the gorilla press powerslam and the Steiner Recliner, both "
                 "inherited from the family, and NXT commentary once nicknamed him the Big Bad "
                 "Booty Nephew after Scott Steiner's Big Bad Booty Daddy persona."),
        dict(
            q="Did Bron Breakker really play in the NFL?",
            a="He got as far as an NFL roster, which is further than almost anyone: he signed "
              "with the <b>Baltimore Ravens</b> as an undrafted free agent fullback in April "
              "2020 after a running back career at Kennesaw State, and was released that "
              "August without appearing in a regular-season game. He is in <b>Madden NFL "
              "21</b> as a Raven, and his first wrestling match came two months after his "
              "release, on October 8, 2020.",
            q_ld="Did Bron Breakker play in the NFL?",
            a_ld="Bron Breakker signed with the Baltimore Ravens as an undrafted free agent "
                 "fullback in April 2020, after playing running back at Kennesaw State "
                 "University, and was released in August 2020 without playing a regular-season "
                 "game. He appears in Madden NFL 21 as a Ravens player. His first professional "
                 "wrestling match took place on October 8, 2020, two months after his release."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Bronson Rechsteiner"),
        dict(label="Born", value="October 24, 1997", sub="Woodstock, Georgia &middot; age 28"),
        dict(label="Billed from", value="Atlanta, Georgia", sub="per WWE.com"),
        dict(label="Height", value="6&#8242;0&#8243;",
             sub="billed &middot; Wikipedia lists 5&#8242;10&#8243; / 178 cm"),
        dict(label="Weight", value="250 lb", sub="billed &middot; Wikipedia lists 223 lb / 101 kg"),
        dict(label="Debut", value="October 8, 2020", sub="WrestleJam 8, Ringgold, Georgia"),
        dict(label="Trained at", value="WWE Performance Center", sub="signed February 2021"),
        dict(label="Family", value="Son of Rick Steiner &middot; nephew of Scott Steiner",
             sub="born Rechsteiner &mdash; the Steiners&rsquo; legal surname"),
        dict(label="Signature", value="Spear &middot; Gorilla press powerslam &middot; Steiner "
                                      "Recliner",
             sub="the Recliner inherited from his uncle"),
        dict(label="Brand", value="Raw"),
        dict(label="Faction", value="The Vision", sub="leader since October 2025"),
        dict(label="Also known as",
             value="The Dog of NXT &middot; The Big Bad Booty Nephew"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1997-10-24",
    bornplace="Woodstock, Georgia",
    nationality="United States",
    alumni="Kennesaw State University",
    height_cm=183,
    weight_kg=113,
    ld=dict(
        alternateName=["Bronson Rechsteiner", "The Dog of NXT", "The Big Bad Booty Nephew"],
        award=["NXT Championship (2 reigns, including 362 days)",
               "WWE Intercontinental Championship (2 reigns)",
               "World Tag Team Championship (1 reign, with Austin Theory, via the Freebird Rule)",
               "NXT Tag Team Championship (1 reign, with Baron Corbin)",
               "Dusty Rhodes Tag Team Classic (2024)",
               "Wrestling Observer Newsletter Rookie of the Year (2022)"],
        knowsAbout=["Professional wrestling", "WWE", "NXT", "The Vision", "American football",
                    "Championship wrestling"],
        description="Bron Breakker, born Bronson Rechsteiner, is an American professional "
                    "wrestler signed to WWE's Raw brand. The son of Rick Steiner and nephew of "
                    "Scott Steiner, he is a two-time NXT Champion — including a 362-day reign "
                    "that unified the NXT and NXT UK Championships — a two-time Intercontinental "
                    "Champion, a Dusty Rhodes Tag Team Classic winner and the Wrestling Observer "
                    "Newsletter's 2022 Rookie of the Year. A former Kennesaw State running back "
                    "and Baltimore Ravens fullback, he leads The Vision faction and faces Oba "
                    "Femi at Sunday Night's Main Event on September 6, 2026.",
        sameAs=["https://en.wikipedia.org/wiki/Bron_Breakker",
                "https://www.wwe.com/superstars/bron-breakker"],
    ),
)
