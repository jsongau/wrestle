# -*- coding: utf-8 -*-
"""Nic Nemeth (Dolph Ziggler in WWE) - dossier data.

Compiled November 9, 2026 from data/nic-nemeth.md, which carries a source URL for
every claim (Wikipedia event and title-history pages, WWE.com, PWTorch, Fightful,
Wrestling Inc, POST Wrestling, PWInsider, Slam Wrestling, SI, CBS Sports, TNA).

The old page (about 267 words) was harvested and checked. It was wrong in the way
that matters most: it called him the reigning TNA World Champion and treated the
Slammiversary 2026 win as his only one. He is a two-time TNA World Champion (July
20, 2024 and June 28, 2026) and lost the title to Leon Slater at Bound for Glory on
October 11, 2026. As of the November 5, 2026 Impact he and Ryan Nemeth were TNA
World Tag Team Champions. Overview paragraph 1 is the correction.

Dolph Ziggler and Nic Nemeth are written as one career. The personas section runs
in order from Nick Nemeth in OVW to Nic Nemeth in TNA.

Deliberate omissions:
  * No career win-loss total. Cagematch is JavaScript-gated; none was verified.
  * No walk-out theme band. "Here to Show the World" (Downstait) is verified as his
    WWE theme, but no Spotify or streaming URL for the track was verified, and the
    band's fallback links must be real.
  * No star ratings on the signature cards. No Wrestling Observer or Cagematch
    figure was verified, so every card shows a dash rather than a number.
  * No social links. No account URL was verified in this pass.
  * No pulse section. No press-verified posts were collected.
"""


def _a(slug, name):
    return '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (slug, name)


# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="2006-04-03", promo="WWE", type="tag", landmark=True,
         event="Raw", opponent=_a("big-show", "Big Show") + " &amp; " + _a("kane", "Kane"),
         opponent_html=True,
         stip="Spirit Squad's Kenny and Mikey win it; all five members, Nicky included, are recognized champions under the Freebird Rule",
         title="World Tag Team Championship"),
    dict(result="W", date="2010-07-28", promo="WWE", landmark=True,
         event="SmackDown (aired Aug 6)", opponent="Kofi Kingston",
         stip="Singles; first Intercontinental title, 160 days", title="Intercontinental Championship"),
    dict(result="L", date="2011-02-15", promo="WWE", landmark=True,
         event="SmackDown (aired Feb 18)", opponent=_a("edge", "Edge"), opponent_html=True,
         stip="Awarded the vacant title by Vickie Guerrero, then lost it to Edge on the same taping",
         title="World Heavyweight Championship"),
    dict(result="W", date="2011-06-19", promo="WWE",
         event="Capitol Punishment", opponent="Kofi Kingston",
         stip="Singles; first United States title, 182 days", title="United States Championship"),
    dict(result="L", date="2011-12-18", promo="WWE",
         event="TLC", opponent="Zack Ryder",
         stip="Singles; the US title reign ends", title="United States Championship"),
    dict(result="W", date="2012-07-15", promo="WWE", type="tag", landmark=True,
         event="Money in the Bank", opponent="Christian, Cody Rhodes, Damien Sandow, Tensai, Santino Marella, Tyson Kidd & Sin Cara",
         stip="Eight-man ladder match for the World Heavyweight title contract", title=""),
    dict(result="W", date="2012-11-18", promo="WWE", type="tag", landmark=True,
         event="Survivor Series", opponent="Team Foley: " + _a("randy-orton", "Randy Orton") + ", Daniel Bryan, " + _a("kane", "Kane") + ", The Miz &amp; Kofi Kingston",
         opponent_html=True,
         stip="Elimination tag as captain; sole survivor after a superkick on Orton", title=""),
    dict(result="W", date="2013-04-08", promo="WWE", landmark=True,
         event="Raw (night after WrestleMania 29)", opponent="Alberto Del Rio",
         stip="Money in the Bank cash-in", title="World Heavyweight Championship"),
    dict(result="L", date="2013-06-16", promo="WWE",
         event="Payback", opponent="Alberto Del Rio",
         stip="Singles; worked weeks after a concussion; the reign ends at 69 days",
         title="World Heavyweight Championship"),
    dict(result="W", date="2014-08-17", promo="WWE",
         event="SummerSlam", opponent="The Miz",
         stip="Singles; second Intercontinental title", title="Intercontinental Championship"),
    dict(result="W", date="2014-11-23", promo="WWE", type="tag", landmark=True,
         event="Survivor Series",
         opponent="Team Authority: " + _a("seth-rollins", "Seth Rollins") + ", " + _a("kane", "Kane") + ", Luke Harper, Mark Henry &amp; Rusev",
         opponent_html=True,
         stip="Team Cena elimination match; last man standing after Sting's WWE debut, pins Rollins",
         title=""),
    dict(result="W", date="2014-12-14", promo="WWE",
         event="TLC (Cleveland)", opponent="Luke Harper",
         stip="Ladder match in his hometown; fourth Intercontinental title",
         title="Intercontinental Championship"),
    dict(result="L", date="2015-03-29", promo="WWE", type="tag",
         event="WrestleMania 31", opponent=_a("daniel-bryan", "Daniel Bryan") + ", Bad News Barrett, Dean Ambrose, Luke Harper, R-Truth &amp; Stardust",
         opponent_html=True,
         stip="Seven-man ladder match; the headbutt exchange atop the ladder, Bryan wins",
         title="Intercontinental Championship"),
    dict(result="L", date="2016-04-03", promo="WWE", type="tag",
         event="WrestleMania 32", opponent="Kevin Owens, Zack Ryder, Sami Zayn, The Miz, Sin Cara &amp; Stardust",
         stip="Seven-man ladder match won by Zack Ryder", title="Intercontinental Championship"),
    dict(result="L", date="2016-08-21", promo="WWE", landmark=True,
         event="SummerSlam", opponent="Dean Ambrose",
         stip="Singles; WWE World Championship challenge", title="WWE World Championship"),
    dict(result="W", date="2016-10-09", promo="WWE", landmark=True,
         event="No Mercy", opponent="The Miz",
         stip="Title vs. career; fifth Intercontinental title", title="Intercontinental Championship"),
    dict(result="W", date="2017-12-17", promo="WWE", type="tag",
         event="Clash of Champions", opponent="Baron Corbin &amp; Bobby Roode",
         stip="Triple threat; he left the belt in the ring two days later", title="United States Championship"),
    dict(result="L", date="2018-01-28", promo="WWE", type="tag",
         event="Royal Rumble", opponent="The 2018 men's Rumble field",
         stip="Surprise entrant No. 30", title=""),
    dict(result="W", date="2018-06-18", promo="WWE", landmark=True,
         event="Raw", opponent=_a("seth-rollins", "Seth Rollins"), opponent_html=True,
         stip="Singles; sixth Intercontinental title", title="Intercontinental Championship"),
    dict(result="L", date="2018-08-19", promo="WWE",
         event="SummerSlam", opponent=_a("seth-rollins", "Seth Rollins"), opponent_html=True,
         stip="Singles; the last of his six IC reigns ends", title="Intercontinental Championship"),
    dict(result="W", date="2018-09-03", promo="WWE", type="tag",
         event="Raw", opponent="The B-Team",
         stip="With Drew McIntyre, as the Dogs of War", title="Raw Tag Team Championship"),
    dict(result="L", date="2019-08-11", promo="WWE",
         event="SummerSlam", opponent=_a("goldberg", "Goldberg"), opponent_html=True,
         stip="Singles; a short loss", title=""),
    dict(result="W", date="2019-09-15", promo="WWE", type="tag",
         event="Clash of Champions", opponent=_a("seth-rollins", "Seth Rollins") + " &amp; Braun Strowman",
         opponent_html=True,
         stip="With Robert Roode", title="Raw Tag Team Championship"),
    dict(result="L", date="2020-04-05", promo="WWE",
         event="WrestleMania 36 Night 2", opponent="Otis",
         stip="Singles", title=""),
    dict(result="L", date="2020-07-19", promo="WWE",
         event="Extreme Rules", opponent=_a("drew-mcintyre", "Drew McIntyre"), opponent_html=True,
         stip="Singles; WWE Championship challenge", title="WWE Championship"),
    dict(result="W", date="2021-01-08", promo="WWE", type="tag",
         event="SmackDown", opponent="The Street Profits",
         stip="With Robert Roode", title="SmackDown Tag Team Championship"),
    dict(result="W", date="2022-03-08", promo="WWE", type="tag", landmark=True,
         event="NXT Roadblock", opponent=_a("bron-breakker", "Bron Breakker") + " &amp; Tommaso Ciampa",
         opponent_html=True,
         stip="Triple threat; superkick on Breakker after Roode pulled him out", title="NXT Championship"),
    dict(result="W", date="2022-04-02", promo="WWE",
         event="NXT Stand & Deliver", opponent=_a("bron-breakker", "Bron Breakker"), opponent_html=True,
         stip="Singles; retained with Roode's help", title="NXT Championship"),
    dict(result="L", date="2022-04-04", promo="WWE",
         event="Raw", opponent=_a("bron-breakker", "Bron Breakker"), opponent_html=True,
         stip="Singles; the 27-day reign ends", title="NXT Championship"),
    dict(result="W", date="2024-02-23", promo="NJPW", landmark=True,
         event="The New Beginning in Sapporo", opponent="David Finlay",
         stip="Singles; first title after leaving WWE", title="IWGP Global Heavyweight Championship"),
    dict(result="W", date="2024-04-27", promo="AAA", landmark=True,
         event="Triplemania XXXII (Monterrey)", opponent="Alberto El Patron",
         stip="Singles for the vacant title", title="AAA Mega Championship"),
    dict(result="W", date="2024-05-03", promo="NJPW",
         event="Wrestling Dontaku Night 1", opponent="Hiroshi Tanahashi",
         stip="Main event; first defense", title="IWGP Global Heavyweight Championship"),
    dict(result="L", date="2024-05-04", promo="NJPW",
         event="Wrestling Dontaku Night 2", opponent="David Finlay",
         stip="Singles; the 71-day reign ends", title="IWGP Global Heavyweight Championship"),
    dict(result="W", date="2024-07-20", promo="TNA", type="tag", landmark=True,
         event="Slammiversary (Montreal)", opponent="Moose, Josh Alexander, Steve Maclin, Frankie Kazarian &amp; Joe Hendry",
         stip="Six-way elimination; first TNA World title", title="TNA World Championship"),
    dict(result="L", date="2024-08-17", promo="AAA",
         event="Triplemania XXXII (Mexico City)", opponent="Alberto El Patron",
         stip="Singles; the Mega title reign ends", title="AAA Mega Championship"),
    dict(result="W", date="2024-08-30", promo="TNA",
         event="Emergence", opponent="Josh Alexander",
         stip="60-minute Iron Man match, won 3-2 with a fall in the closing seconds",
         title="TNA World Championship"),
    dict(result="W", date="2024-10-26", promo="TNA",
         event="Bound for Glory", opponent="Joe Hendry",
         stip="Singles; retained", title="TNA World Championship"),
    dict(result="L", date="2025-01-19", promo="TNA", landmark=True,
         event="Genesis", opponent="Joe Hendry",
         stip="Singles; the 183-day reign ends", title="TNA World Championship"),
    dict(result="W", date="2025-04-27", promo="TNA", type="tag",
         event="Rebellion", opponent=_a("matt-hardy", "Matt Hardy") + " &amp; " + _a("jeff-hardy", "Jeff Hardy"),
         opponent_html=True,
         stip="With Ryan Nemeth; first reign as The Nemeths", title="TNA World Tag Team Championship"),
    dict(result="L", date="2025-07-20", promo="TNA", type="tag",
         event="Slammiversary", opponent="The Hardys, The Rascalz &amp; First Class",
         stip="Four-way ladder match", title="TNA World Tag Team Championship"),
    dict(result="W", date="2025-10-12", promo="TNA", type="tag",
         event="Bound for Glory", opponent="The Call Your Shot Gauntlet field",
         stip="Declared co-winner with Frankie Kazarian after a double pin counted by two referees",
         title=""),
    dict(result="L", date="2025-11-17", promo="WWE", landmark=True,
         event="Raw", opponent=_a("solo-sikoa", "Solo Sikoa"), opponent_html=True,
         stip="Billed as Dolph Ziggler; first round of John Cena's Last Time Is Now tournament",
         title=""),
    dict(result="W", date="2026-06-28", promo="TNA", landmark=True,
         event="Slammiversary", opponent="Mike Santana",
         stip="Call Your Shot cash-in; second TNA World title", title="TNA World Championship"),
    dict(result="W", date="2026-08-23", promo="TNA", type="tag",
         event="Lockdown (Chicago)", opponent=_a("matt-hardy", "Matt Hardy") + " &amp; " + _a("jeff-hardy", "Jeff Hardy"),
         opponent_html=True,
         stip="Steel cage, with Ryan Nemeth; makes him a double champion", title="TNA World Tag Team Championship"),
    dict(result="W", date="2026-10-08", promo="TNA", type="tag",
         event="Impact", opponent=_a("matt-hardy", "Matt Hardy") + " &amp; " + _a("jeff-hardy", "Jeff Hardy"),
         opponent_html=True,
         stip="Lockdown rematch; Nic rolls up Jeff to retain", title="TNA World Tag Team Championship"),
    dict(result="L", date="2026-10-11", promo="TNA", landmark=True,
         event="Bound for Glory", opponent="Leon Slater",
         stip="Main event; the 105-day reign ends", title="TNA World Championship"),
    dict(result="W", date="2026-11-05", promo="TNA", type="tag",
         event="Impact", opponent="Leon Slater &amp; Amazing Red",
         stip="With Ryan Nemeth; Danger Zone on Red to retain", title="TNA World Tag Team Championship"),
]

# Plain-text opponents stay escaped by the generator. Rows with links carry
# opponent_html=True, and "&amp;" in plain rows must not be double-escaped, so
# any plain row containing an entity is flagged as HTML too (the text is static).
for _r in ROWS:
    if "&amp;" in _r["opponent"] or "<a " in _r["opponent"]:
        _r["opponent_html"] = True

DATA = dict(
    slug="nic-nemeth",
    name="Nic Nemeth",
    realname="Nicholas Theodore Nemeth",
    epithet="The Showoff",
    hook="Record & Titles",
    art="nic-nemeth",

    meta_desc=("Nic Nemeth, Dolph Ziggler in WWE: Spirit Squad, two World Heavyweight titles, the "
               "2013 cash-in, six Intercontinental titles, NXT Champion, then IWGP Global, AAA Mega "
               "and two TNA World titles. Record, titles, timeline and status."),
    og_desc=("Dolph Ziggler and Nic Nemeth, one career: 19 years in WWE, released in 2023, then "
             "champion in NJPW, AAA and TNA. Two-time TNA World Champion, now TNA tag champion."),
    tw_desc="Nic Nemeth, formerly Dolph Ziggler: two WHC reigns, six IC titles, two TNA World titles.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2004",
    height_imp="6&#8242;0&#8243;",
    weight_lb="213",
    world_titles="4",
    vitals_tagline="The Showstealer",
    support_note="Watch &middot; Play",
    sp_items=[
        dict(ic="TNA", title="TNA Wrestling", sub="His current promotion", tag="Visit",
             href="https://tnawrestling.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable through WWE 2K23", tag="Play",
             href="https://wwe.2k.com/"),
        dict(ic="W", title="Wikipedia", sub="Full biography", tag="Read", charity=True,
             href="https://en.wikipedia.org/wiki/Nic_Nemeth"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Dolph Ziggler in WWE &middot; Nic Nemeth since 2024 &middot; one career, two names",
    hero_tag="Cleveland, Ohio &middot; <em>WWE 2004&ndash;2023 &middot; NJPW, AAA and TNA since</em>",
    now_label="NOW",
    now_bold="TNA World Tag Team Champion, with Ryan Nemeth",
    now_tail=(" &middot; lost the TNA World Championship to Leon Slater at Bound for Glory on "
              "October 11, 2026, and retained the tag titles on the November 5 Impact"),
    hstats=[
        dict(value="4",  x=False, label="World Titles, WWE and TNA"),
        dict(value="6",  x=True,  label="Intercontinental Titles"),
        dict(value="19", x=False, label="Years in WWE"),
        dict(value="2",  x=True,  label="Survivor Series Sole Survivals"),
    ],
    ghost_link="From the Spirit Squad to two TNA World titles",
    vlabel="Est. 2004 &middot; Cleveland, Ohio",
    mono="NN",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Nic Nemeth</b> is the man WWE audiences knew for fifteen years as <b>Dolph "
        "Ziggler</b>. He was a three-time Mid-American Conference champion at Kent State, debuted in "
        "Ohio Valley Wrestling in 2004, and spent 2006 in a cheerleader costume as Nicky of the "
        "Spirit Squad. Then came Dolph Ziggler. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">6</span>'
        '<span class="pull-cap">Intercontinental Championship reigns, 2010&ndash;2018</span></span>'
        "The WWE record reads two World Heavyweight Championships, six Intercontinental titles, two "
        "United States titles, four tag team title reigns, the 2012 Money in the Bank briefcase, "
        "two Survivor Series sole survivals and a 27-day NXT Championship in 2022. WWE released "
        "him on September 21, 2023, after 19 years.",

        "The old version of this page said he won the TNA World Championship at Slammiversary on "
        "June 28, 2026, and still held it. Both halves need fixing. That night was his <b>second</b> "
        "TNA World title. The first came at Slammiversary on July 20, 2024, in a six-way "
        "elimination match in Montreal, and lasted 183 days until Joe Hendry beat him at Genesis. "
        "The second reign ended at 105 days, when <b>Leon Slater</b> beat him in the Bound for "
        "Glory main event on October 11, 2026. As of the November 5, 2026 Impact, the gold he holds "
        "is the TNA World Tag Team Championship, with his brother Ryan. One more counting rule: "
        "this page lists four world titles (two in WWE, two in TNA). The NXT Championship is not "
        "classed as a world title by WWE, and the AAA Mega and IWGP Global titles are counted "
        "separately below.",

        "The WWE peak came in two bursts. On July 15, 2012 he won the Money in the Bank ladder "
        "match in Phoenix. On April 8, 2013, the night after WrestleMania 29, he cashed it in on "
        "Alberto Del Rio in East Rutherford, New Jersey, and won the World Heavyweight "
        "Championship. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig pull-fig--sm">April 8, 2013</span>'
        '<span class="pull-cap">the Money in the Bank cash-in on Alberto Del Rio, the night after WrestleMania 29</span></span>'
        "A concussion followed within weeks. He lost the title back to Del Rio at Payback on June "
        "16, 2013, after 69 days. His first World Heavyweight reign, in February 2011, had lasted "
        "part of one SmackDown taping. The second burst was 2014: three Intercontinental titles "
        "and the Survivor Series main event in St. Louis, where Sting's WWE debut helped him pin "
        "Seth Rollins as the last man standing for Team Cena.",

        "After the release he worked everywhere at once. He beat David Finlay for NJPW's IWGP "
        "Global Heavyweight Championship on February 23, 2024 in Sapporo. He won the vacant AAA "
        "Mega Championship from Alberto El Patron on April 27, 2024 in Monterrey. He won the TNA "
        "World title on July 20, 2024. For a week in 2024 he held two of those belts at once, and "
        "for four weeks he held two others. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">105</span>'
        '<span class="pull-cap">days in his second TNA World Championship reign, June 28 to October 11, 2026</span></span>'
        "In TNA he turned heel with Ryan in March 2025, won the tag titles twice, re-signed in "
        "January 2026, and cashed in a Call Your Shot trophy on Mike Santana at Slammiversary 2026. "
        "He made one WWE appearance in between, on November 17, 2025, billed again as Dolph Ziggler "
        "in John Cena's Last Time Is Now tournament. He lost to Solo Sikoa. He has said WWE asked "
        "him back several times and he turned the other offers down.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Highlight set",
        promo_order=["WWE", "NJPW", "AAA", "TNA"],
        promo_labels={"WWE": "WWE", "NJPW": "NJPW", "AAA": "AAA", "TNA": "TNA"},
        stats=[
            ("2&times;", "World Heavyweight"),
            ("6&times;", "Intercontinental"),
            ("2&times;", "TNA World"),
            ("1",        "NXT title"),
            ("2012",     "Money in the Bank"),
            ("2026",     "Most recent title"),
        ],
        lead=("Forty-seven documented bouts from 2006 to November 5, 2026. This is a highlight set, "
              "not a career count, and no career win&ndash;loss total is printed because none was "
              "verified. Most of his title wins and losses are here, along with the premium events "
              "that framed them. The 2006 row is a Spirit Squad title win credited to all five members under "
              "the Freebird Rule. Filter by promotion or match type, tap a column header to sort, "
              "and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("Six nights that define the career. No Wrestling Observer or Cagematch rating "
                    "was verified for any of them, so each card shows a dash instead of a number."),
    signature=[
        dict(rating="&mdash;", event="Raw, April 8, 2013", opponent="Alberto Del Rio",
             stip="The Money in the Bank cash-in, the night after WrestleMania 29"),
        dict(rating="&mdash;", event="Survivor Series 2014", opponent="Team Authority",
             stip="Sole survivor for Team Cena, with Sting's WWE debut at the finish"),
        dict(rating="&mdash;", event="No Mercy 2016", opponent="The Miz",
             stip="Title vs. career for the Intercontinental Championship"),
        dict(rating="&mdash;", event="NXT Roadblock 2022", opponent="Bron Breakker & Tommaso Ciampa",
             stip="Triple threat for the NXT Championship"),
        dict(rating="&mdash;", event="Emergence 2024", opponent="Josh Alexander",
             stip="60-minute Iron Man match for the TNA World Championship, won 3-2"),
        dict(rating="&mdash;", event="Slammiversary 2026", opponent="Mike Santana",
             stip="Call Your Shot cash-in for a second TNA World title"),
    ],
    signature_count_word="six",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("4",        "World titles, WWE and TNA"),
            ("6&times;", "Intercontinental"),
            ("5",        "Promotions with a title"),
            ("2026",     "Current tag reign began"),
        ],
        lead=("Titles in WWE, NJPW, AAA and TNA, plus developmental gold in FCW. Day counts are the "
              "reign lengths published in title histories; where WWE recognizes a different figure "
              "because of tape delay, both are given."),
        rows=[
            dict(ic="W", name="World Heavyweight Championship (WWE)", count="2",
                 sub="February 15, 2011, SmackDown taping in San Diego: awarded the vacant title by "
                     "Vickie Guerrero and lost it to Edge the same night (WWE dates it February 18, "
                     "the air date) &middot; April 8, 2013, Raw: Money in the Bank cash-in on "
                     "Alberto Del Rio, lost to Del Rio at Payback on June 16 after <b>69 days</b>"),
            dict(ic="T", name="TNA World Championship", count="2",
                 sub="July 20, 2024, Slammiversary in Montreal, six-way elimination; lost to Joe "
                     "Hendry at Genesis on January 19, 2025 after <b>183 days</b> &middot; June 28, "
                     "2026, Slammiversary, Call Your Shot cash-in on Mike Santana; lost to Leon "
                     "Slater at Bound for Glory on October 11, 2026 after <b>105 days</b>"),
            dict(ic="IC", name="Intercontinental Championship", count="6",
                 sub="2010 from Kofi Kingston (160 days) &middot; SummerSlam 2014 from The Miz (35) "
                     "&middot; Raw, September 22, 2014 (56) &middot; TLC 2014 ladder match in "
                     "Cleveland (22) &middot; No Mercy 2016, title vs. career against The Miz (37) "
                     "&middot; Raw, June 18, 2018 from Seth Rollins, lost to Rollins at SummerSlam "
                     "(62)"),
            dict(ic="US", name="United States Championship", count="2",
                 sub="Capitol Punishment, June 19, 2011, from Kofi Kingston (182 days) &middot; "
                     "Clash of Champions, December 17, 2017, triple threat; he left the belt in the "
                     "ring two days later and it was declared vacant December 26"),
            dict(ic="NXT", name="NXT Championship", count="1",
                 sub="NXT Roadblock, March 8, 2022, triple threat over Bron Breakker and Tommaso "
                     "Ciampa; lost to Breakker on Raw, April 4, 2022 (27 days)"),
            dict(ic="G", name="IWGP Global Heavyweight Championship (NJPW)", count="1",
                 sub="The New Beginning in Sapporo, February 23, 2024, from David Finlay; beat "
                     "Hiroshi Tanahashi on May 3, lost to Finlay on May 4 (71 days)"),
            dict(ic="M", name="AAA Mega Championship", count="1",
                 sub="Triplemania XXXII Monterrey, April 27, 2024, vacant title over Alberto El "
                     "Patron; lost to El Patron at Triplemania XXXII Mexico City on August 17, 2024"),
            dict(ic="TT", name="TNA World Tag Team Championship", count="2",
                 sub="With Ryan Nemeth &middot; Rebellion, April 27, 2025, from The Hardys; lost "
                     "in a four-way ladder match at Slammiversary on July 20, 2025 &middot; "
                     "Lockdown, August 23, 2026, steel cage over The Hardys; <b>reigning as of "
                     "November 5, 2026</b>"),
            dict(ic="R", name="Raw Tag Team Championship", count="2",
                 sub="With Drew McIntyre, September 3 to October 22, 2018 &middot; with Robert "
                     "Roode, September 15 to October 14, 2019"),
            dict(ic="S", name="SmackDown Tag Team Championship", count="1",
                 sub="With Robert Roode, from The Street Profits on January 8, 2021; lost to Rey and "
                     "Dominik Mysterio at WrestleMania Backlash 2021"),
            dict(ic="WT", name="World Tag Team Championship", count="1",
                 sub="As Nicky of the Spirit Squad, April 3 to November 5, 2006 (216 days), all "
                     "five members recognized under the Freebird Rule; lost to Ric Flair and Roddy "
                     "Piper at Cyber Sunday"),
            dict(ic="$", name="Money in the Bank", count="1",
                 sub="July 15, 2012, Phoenix: the World Heavyweight contract ladder match"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Mostly a singles act, with five groups that marked the eras.",
        cards=[
            dict(era="WWE &middot; 2006",
                 name="Spirit Squad",
                 members="Kenny, Johnny, Mitch, Nicky, Mikey",
                 desc="Five male cheerleaders who debuted on Raw on January 23, 2006, won the World "
                      "Tag Team titles on April 3, and feuded with the reformed D-Generation X. "
                      "They lost the belts to Ric Flair and Roddy Piper at Cyber Sunday and "
                      "disbanded on Raw on November 27, 2006. Nicky was Nemeth."),
            dict(era="WWE &middot; 2010&ndash;2013",
                 name="With Vickie Guerrero and Big E",
                 members="Dolph Ziggler, Vickie Guerrero, Big E Langston",
                 desc="Vickie Guerrero handed him the vacant World Heavyweight title in 2011 and was "
                      "at ringside when he won Money in the Bank in 2012. Big E was his enforcer by "
                      "the 2013 title reign and was ejected from ringside at Payback."),
            dict(era="WWE &middot; 2018",
                 name="Dogs of War",
                 members="Dolph Ziggler, Drew McIntyre, Braun Strowman",
                 desc="Formed on Raw on September 3, 2018, the night Ziggler and McIntyre won the Raw "
                      "Tag Team titles from The B-Team. They lost them to Seth Rollins and Dean "
                      "Ambrose on October 22."),
            dict(era="WWE &middot; 2019&ndash;2022",
                 name="Ziggler and Roode",
                 members="Dolph Ziggler, Robert Roode",
                 desc="Raw Tag Team Champions in 2019 and SmackDown Tag Team Champions in 2021. "
                      "Roode was in his corner for the 2022 NXT Championship run and pulled Bron "
                      "Breakker out of the ring at Roadblock."),
            dict(era="TNA &middot; 2025&ndash;present",
                 name="The Nemeths",
                 members="Nic Nemeth, Ryan Nemeth",
                 desc="The brothers turned heel together at Sacrifice on March 14, 2025, attacking "
                      "Matt Hardy. They have held the TNA World Tag Team Championship twice, both "
                      "times taking it from The Hardys."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One career under two names. Dolph Ziggler and Nic Nemeth are the same wrestler.",
        cards=[
            dict(mono="NN", era="OVW &middot; 2004&ndash;2005", name="Nick Nemeth",
                 desc="Debuted in Ohio Valley Wrestling on November 3, 2004, under his own name, and "
                      "spent 2005 as the caddie for Chavo Guerrero's Kerwin White character until "
                      "the angle ended after Eddie Guerrero's death."),
            dict(mono="NY", era="WWE &middot; 2006", name="Nicky",
                 desc="The Spirit Squad cheerleader. A comedy gimmick, but it put him on Raw, made "
                      "him a World Tag Team Champion under the Freebird Rule, and put him in the "
                      "ring with D-Generation X."),
            dict(mono="DZ", era="WWE &middot; 2008&ndash;2023", name="Dolph Ziggler",
                 desc="Introduced on Raw on September 15, 2008. A bleached-blond, self-adoring heel "
                      "who sold big and stole shows, later a fan favorite from 2013. Every WWE title "
                      "on this page was won under this name."),
            dict(mono="NN", era="NJPW &middot; AAA &middot; TNA &middot; 2024&ndash;present", name="Nic Nemeth",
                 desc="After the September 2023 release he went back to his legal name and won "
                      "titles in NJPW, AAA and TNA within a year. WWE billed him as Dolph Ziggler "
                      "again for one Raw match on November 17, 2025."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Kent State to OVW to nineteen years in WWE, then four promotions in two years.",
        rows=[
            dict(year="2003", title="Kent State",
                 desc="Finishes with 121 career wins, then the school record, and three "
                      "Mid-American Conference titles at 165 lb. He had been accepted to Arizona "
                      "State's law school."),
            dict(year="2004", title="OVW debut",
                 desc="First match in Ohio Valley Wrestling on November 3, as Nick Nemeth."),
            dict(year="2006", title="Spirit Squad",
                 desc="Debuts on Raw on January 23 and becomes a World Tag Team Champion on April 3. "
                      "The group disbands on November 27 after the DX feud."),
            dict(year="2008", title="Dolph Ziggler",
                 desc="The new name debuts on Raw on September 15."),
            dict(year="2010", title="First Intercontinental title",
                 desc="Beats Kofi Kingston at a July 28 SmackDown taping and holds the title for 160 "
                      "days."),
            dict(year="2011", title="World champion for one taping",
                 desc="Awarded the vacant World Heavyweight title on February 15 and loses it to Edge "
                      "the same night. Wins the US title at Capitol Punishment on June 19."),
            dict(year="2012", title="Money in the Bank",
                 desc="Wins the World Heavyweight contract ladder match on July 15 in Phoenix, then "
                      "survives alone for his team at Survivor Series on November 18."),
            dict(year="2013", title="The cash-in",
                 desc="Cashes in on Alberto Del Rio on Raw, April 8, the night after WrestleMania 29. "
                      "A concussion follows, and Del Rio takes the title back at Payback on June 16."),
            dict(year="2014", title="Sole survivor again",
                 desc="Three Intercontinental title wins, and the last man standing for Team Cena at "
                      "Survivor Series on November 23, with Sting's debut at the finish."),
            dict(year="2016", title="Title vs. career",
                 desc="Loses to Dean Ambrose for the WWE World Championship at SummerSlam, then puts "
                      "his career on the line against The Miz at No Mercy on October 9 and wins the "
                      "Intercontinental title."),
            dict(year="2018", title="No. 30 and the sixth IC title",
                 desc="Surprise No. 30 in the Royal Rumble, a sixth Intercontinental title from Seth "
                      "Rollins on June 18, and Raw tag gold with Drew McIntyre on September 3."),
            dict(year="2019", title="Rumble final three",
                 desc="Lasts to the final three of the Rumble from No. 28, loses to Goldberg at "
                      "SummerSlam, and wins the Raw tag titles with Robert Roode."),
            dict(year="2020", title="WWE Championship challenge",
                 desc="Loses to Otis at WrestleMania 36 and challenges Drew McIntyre for the WWE "
                      "Championship at Extreme Rules on July 19."),
            dict(year="2022", title="NXT Champion",
                 desc="Wins the NXT Championship at Roadblock on March 8 and holds it 27 days, until "
                      "Bron Breakker takes it back on Raw."),
            dict(year="2023", title="Released",
                 desc="Goes undrafted, then is released on September 21 after 19 years with WWE."),
            dict(year="2024", title="Three promotions, three titles",
                 desc="Debuts in TNA at Hard To Kill on January 13. Wins the IWGP Global title on "
                      "February 23, the AAA Mega title on April 27 and the TNA World title on "
                      "July 20."),
            dict(year="2025", title="Heel turn and a WWE one-off",
                 desc="Loses the TNA title to Joe Hendry on January 19, turns heel with Ryan in "
                      "March, wins the tag titles in April, co-wins the Call Your Shot Gauntlet in "
                      "October, and loses to Solo Sikoa on Raw on November 17."),
            dict(year="2026", title="Double champion",
                 desc="Re-signs with TNA in January, cashes in for a second TNA World title on June "
                      "28, regains the tag titles in a cage on August 23, and loses the world title "
                      "to Leon Slater on October 11. Still a tag champion on November 5."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="The opponents his title history keeps returning to.",
        cards=[
            dict(name="The Miz",
                 desc="They traded the Intercontinental title in 2014 and met again at No Mercy 2016, "
                      "where Ziggler put his career up against the belt and won it. Miz took it back "
                      "on SmackDown's 900th episode 37 days later."),
            dict(name="Seth Rollins", slug="seth-rollins",
                 desc="Ziggler pinned Rollins to end Survivor Series 2014, took the Intercontinental "
                      "title from him on June 18, 2018, and lost it back at SummerSlam. They met "
                      "over the Raw tag titles in 2018 and 2019 as well."),
            dict(name="Kofi Kingston",
                 desc="The opponent for his first two singles titles: the Intercontinental title in "
                      "2010, which Kingston won back in January 2011, and the United States title "
                      "at Capitol Punishment 2011."),
            dict(name="Alberto Del Rio",
                 desc="The cash-in on April 8, 2013, and the Payback rematch on June 16, where Del "
                      "Rio targeted his concussed head and regained the title."),
            dict(name="Joe Hendry",
                 desc="Hendry was in the six-way where Nemeth first won the TNA title, lost to him at "
                      "Bound for Glory 2024, and beat him for the title at Genesis on January 19, "
                      "2025."),
            dict(name="The Hardys", slug="jeff-hardy",
                 desc="The Nemeths took the TNA World Tag Team titles from Matt and Jeff Hardy at "
                      "Rebellion 2025, lost them back at Slammiversary 2025, and won them again in "
                      "a cage at Lockdown 2026."),
            dict(name="Leon Slater",
                 desc="Slater cashed in his X Division title for a world title shot and beat Nemeth "
                      "in the Bound for Glory 2026 main event, billed as the youngest world champion "
                      "in TNA history. The Nemeths then beat Slater and Amazing Red on November 5."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Comedy",
        lead="Stand-up, reality TV, film and a run as Colonel Sanders.",
        rows=[
            dict(when="2010&ndash;", title="Stand-up comedy", kind="Comedy",
                 desc="Started doing stand-up around 2010, with his first Los Angeles set in 2013. "
                      "Competed on Roast Battle III in 2018 and headlined a tour after the 2019 "
                      "Royal Rumble."),
            dict(when="2014&ndash;17", title="Total Divas", kind="TV",
                 desc="A recurring cast member, alongside appearances on @midnight, Adam Ruins "
                      "Everything, Wild 'n Out, The Challenge and Miz & Mrs."),
            dict(when="2015&ndash;24", title="Film", kind="Screen",
                 desc="Me Him Her and Buddy Hutchins (2015), Countdown (2016), a voice role in The "
                      "Jetsons & WWE: Robo-WrestleMania! (2017), The Speed of Time (2020) and "
                      "Drugstore June (2024)."),
            dict(when="2016&ndash;17", title="KFC commercials", kind="Ads",
                 desc="Played Colonel Sanders in a run of KFC ads."),
            dict(when="2009&ndash;23", title="WWE video games", kind="Game",
                 desc="Playable from WWE SmackDown vs. Raw 2010 through WWE 2K23."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, with the dates that make them true.",
        stats=[
            ("2",   "Survivor Series sole survivals"),
            ("6",   "Intercontinental reigns"),
            ("121", "Kent State career wins"),
        ],
        rows=[
            dict(name="Two Survivor Series sole survivals",
                 sub="November 18, 2012 as captain of Team Ziggler, and November 23, 2014 for Team "
                     "Cena, the match that removed The Authority from power in the storyline."),
            dict(name="Six Intercontinental Championship reigns",
                 sub="Between July 2010 and August 2018, the longest at 160 days."),
            dict(name="Two belts at once, twice, in 2024",
                 sub="IWGP Global and AAA Mega from April 27 to May 4, 2024, then AAA Mega and TNA "
                     "World from July 20 to August 17, 2024. Computed from the published reign "
                     "dates."),
            dict(name="Won a 60-minute Iron Man match",
                 sub="Beat Josh Alexander 3-2 at Emergence on August 30, 2024, scoring the deciding "
                     "fall in the final seconds."),
            dict(name="TNA double champion",
                 sub="Held the TNA World and TNA World Tag Team titles together from August 23 to "
                     "October 11, 2026."),
            dict(name="Kent State wins record",
                 sub="121 career wins from 2000 to 2003, the school record until 2006, plus three "
                     "Mid-American Conference titles."),
            dict(name="Hall of Fame, Class of 2026",
                 sub="Named to the George Tragos/Lou Thesz Professional Wrestling Hall of Fame, "
                     "announced December 11, 2025."),
        ],
        footnote=("No career win-loss total appears on this page; none was verified. Height and "
                  "weight are WWE billings. The world-title count of four covers WWE and TNA only."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Nic_Nemeth"),
        dict(k="TNA Wrestling", v="Official site", href="https://tnawrestling.com/"),
        dict(k="WWE.com", v="Payback 2013, Ziggler vs. Del Rio",
             href="https://www.wwe.com/shows/wwepayback/2013/world-heavyweight-champion-dolph-ziggler-vs-alberto-del-rio"),
        dict(k="Wrestling Inc", v="Slammiversary 2026 title win",
             href="https://www.wrestlinginc.com/2203408/nic-nemeth-wins-2nd-tna-world-title-slammiversary-main-event/"),
        dict(k="Wrestling Inc", v="Bound for Glory 2026, Slater wins",
             href="https://wrestlinginc.com/2283341/leon-slater-wins-tna-world-title-bound-glory-main-event/"),
        dict(k="Wrestling Inc", v="November 5, 2026 tag title defense",
             href="https://www.wrestlinginc.com/2308799/tna-impact-nic-ryan-nemeth-amazing-red-leon-slater-retain-tag-title/"),
        dict(k="Slam Wrestling", v="On turning down WWE offers",
             href="https://slamwrestling.net/news/nic-nemeth-says-he-rejected-multiple-offers-to-return-to-wwe/"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/nic-nemeth.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Nic Nemeth the same wrestler as Dolph Ziggler?",
            a="Yes. Dolph Ziggler was his WWE ring name from September 2008 until his release in "
              "September 2023. Nicholas Theodore Nemeth is his legal name, and he has wrestled as "
              "<b>Nic Nemeth</b> in NJPW, AAA and TNA since 2024. WWE billed him as Dolph Ziggler "
              "once more for a Raw match on November 17, 2025.",
            q_ld="Is Nic Nemeth the same wrestler as Dolph Ziggler?",
            a_ld="Yes. Nic Nemeth, born Nicholas Theodore Nemeth, wrestled in WWE as Dolph Ziggler "
                 "from 2008 until his release in September 2023. Since 2024 he has competed under "
                 "his legal name in NJPW, AAA and TNA. WWE billed him as Dolph Ziggler again for "
                 "a one-off Raw match on November 17, 2025."),
        dict(
            q="Is Nic Nemeth still the TNA World Champion?",
            a="No. He won the title for the second time at Slammiversary on June 28, 2026, and lost "
              "it to <b>Leon Slater</b> in the Bound for Glory main event on October 11, 2026, after "
              "105 days. He is still a champion: he and his brother Ryan hold the TNA World Tag "
              "Team Championship, which they retained on the November 5, 2026 Impact.",
            q_ld="Is Nic Nemeth still the TNA World Champion?",
            a_ld="No. Nic Nemeth won his second TNA World Championship at Slammiversary on June 28, "
                 "2026 and lost it to Leon Slater at Bound for Glory on October 11, 2026, after 105 "
                 "days. As of the November 5, 2026 episode of TNA Impact, Nic Nemeth and his "
                 "brother Ryan Nemeth were the TNA World Tag Team Champions."),
        dict(
            q="How many times has Nic Nemeth been TNA World Champion?",
            a="Twice. The first reign began at Slammiversary on July 20, 2024 in Montreal, where he "
              "won a six-way elimination match, and ended at Genesis on January 19, 2025 against Joe "
              "Hendry (183 days). The second began on June 28, 2026 and ended on October 11, 2026 "
              "(105 days).",
            q_ld="How many times has Nic Nemeth been TNA World Champion?",
            a_ld="Nic Nemeth has been TNA World Champion twice. He won it at Slammiversary on July "
                 "20, 2024 and lost it to Joe Hendry at Genesis on January 19, 2025 after 183 days. "
                 "He won it again at Slammiversary on June 28, 2026 and lost it to Leon Slater at "
                 "Bound for Glory on October 11, 2026 after 105 days."),
        dict(
            q="How many world titles did Dolph Ziggler win in WWE?",
            a="Two, both the World Heavyweight Championship. The first, in February 2011, lasted "
              "part of one SmackDown taping before Edge won it back. The second came from the Money "
              "in the Bank cash-in on April 8, 2013 and lasted 69 days. His 2022 NXT Championship is "
              "not classed as a world title by WWE. Counting his two TNA World titles, the total is "
              "four.",
            q_ld="How many world championships did Dolph Ziggler win in WWE?",
            a_ld="Dolph Ziggler won the World Heavyweight Championship twice in WWE: briefly on "
                 "February 15, 2011, and from April 8 to June 16, 2013 after cashing in Money in "
                 "the Bank. He also held the NXT Championship in 2022, which WWE does not class as "
                 "a world title. As Nic Nemeth he later won the TNA World Championship twice."),
        dict(
            q="What happened with Dolph Ziggler's 2013 Money in the Bank cash-in?",
            a="He won the briefcase on July 15, 2012 in Phoenix and cashed it in on Alberto Del Rio "
              "on <b>April 8, 2013</b>, on the Raw after WrestleMania 29, to win the World "
              "Heavyweight Championship. He suffered a concussion soon after and lost the title back "
              "to Del Rio at Payback on June 16, 2013.",
            q_ld="When did Dolph Ziggler cash in Money in the Bank?",
            a_ld="Dolph Ziggler cashed in his Money in the Bank contract on Alberto Del Rio on the "
                 "April 8, 2013 episode of Raw, the night after WrestleMania 29, winning the World "
                 "Heavyweight Championship. He had won the briefcase on July 15, 2012. He lost the "
                 "title back to Del Rio at Payback on June 16, 2013, after 69 days."),
        dict(
            q="How many times was Dolph Ziggler Intercontinental Champion?",
            a="Six: 2010 (from Kofi Kingston), August 2014 (SummerSlam), September 2014 (Raw), "
              "December 2014 (TLC ladder match in Cleveland), October 2016 (No Mercy, title vs. "
              "career against The Miz) and June 2018 (from Seth Rollins).",
            q_ld="How many times was Dolph Ziggler Intercontinental Champion?",
            a_ld="Dolph Ziggler was Intercontinental Champion six times, between 2010 and 2018. His "
                 "reigns began in July 2010, August 2014, September 2014, December 2014, October "
                 "2016 and June 2018. The longest lasted 160 days."),
        dict(
            q="Was Dolph Ziggler in the Spirit Squad?",
            a="Yes. He was Nicky, one of the five cheerleaders who debuted on Raw on January 23, "
              "2006. The group won the World Tag Team Championship on April 3, 2006, with all five "
              "recognized as champions under the Freebird Rule, and disbanded in November 2006.",
            q_ld="Was Dolph Ziggler in the Spirit Squad?",
            a_ld="Yes. Before becoming Dolph Ziggler, Nic Nemeth was Nicky in the Spirit Squad, a "
                 "five-man cheerleader group that debuted on WWE Raw on January 23, 2006. The group "
                 "won the World Tag Team Championship on April 3, 2006 under the Freebird Rule and "
                 "disbanded in November 2006."),
        dict(
            q="Did Dolph Ziggler win the NXT Championship?",
            a="Yes, at NXT Roadblock on March 8, 2022, in a triple threat with champion Bron "
              "Breakker and Tommaso Ciampa. He retained against Breakker at Stand &amp; Deliver and "
              "lost to him on Raw on April 4, 2022, after 27 days.",
            q_ld="Did Dolph Ziggler win the NXT Championship?",
            a_ld="Yes. Dolph Ziggler won the NXT Championship at NXT Roadblock on March 8, 2022, "
                 "beating Bron Breakker and Tommaso Ciampa in a triple threat. He lost it to Bron "
                 "Breakker on Raw on April 4, 2022, after 27 days."),
        dict(
            q="When did WWE release Dolph Ziggler?",
            a="On <b>September 21, 2023</b>, after 19 years with the company. He had gone "
              "undrafted earlier that year. He then won titles in NJPW, AAA and TNA during 2024.",
            q_ld="When did WWE release Dolph Ziggler?",
            a_ld="WWE released Dolph Ziggler on September 21, 2023, ending a 19-year tenure. Working "
                 "as Nic Nemeth, he won the IWGP Global Heavyweight, AAA Mega and TNA World "
                 "championships in 2024."),
        dict(
            q="Has Nic Nemeth gone back to WWE?",
            a="Once. He returned as Dolph Ziggler on Raw on November 17, 2025, in John Cena's Last "
              "Time Is Now tournament, and lost to Solo Sikoa in the first round. He re-signed with "
              "TNA in January 2026 and told Slam Wrestling that WWE had asked him back several "
              "times and he had declined the other offers.",
            q_ld="Has Nic Nemeth returned to WWE?",
            a_ld="Nic Nemeth made one WWE appearance after his release, wrestling as Dolph Ziggler "
                 "on Raw on November 17, 2025 and losing to Solo Sikoa in the first round of John "
                 "Cena's Last Time Is Now tournament. He re-signed with TNA in January 2026 and "
                 "has said he turned down other WWE offers."),
        dict(
            q="Who is Ryan Nemeth?",
            a="His younger brother, also a professional wrestler. Together they are The Nemeths, "
              "two-time TNA World Tag Team Champions: April 27 to July 20, 2025, and again since "
              "Lockdown on August 23, 2026.",
            q_ld="Who is Ryan Nemeth?",
            a_ld="Ryan Nemeth is Nic Nemeth's younger brother and tag team partner. As The Nemeths "
                 "they have won the TNA World Tag Team Championship twice, first at Rebellion on "
                 "April 27, 2025 and again at Lockdown on August 23, 2026."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Nicholas Theodore Nemeth"),
        dict(label="Born", value="July 27, 1980", sub="Cleveland, Ohio &middot; age 46"),
        dict(label="Billed from", value="Hollywood, Florida", sub="WWE billing"),
        dict(label="Height", value="6&#8242;0&#8243;", sub="183 cm &middot; as billed"),
        dict(label="Weight", value="213 lb", sub="97 kg &middot; as billed; varied by era"),
        dict(label="College", value="Kent State University",
             sub="121 career wins, three MAC titles at 165 lb"),
        dict(label="Debut", value="November 3, 2004", sub="OVW, as Nick Nemeth"),
        dict(label="WWE release", value="September 21, 2023", sub="after 19 years"),
        dict(label="Promotion", value="TNA", sub="re-signed January 2026"),
        dict(label="Finishers", value="Zig Zag / Danger Zone &middot; superkick",
             sub="the Zig Zag was renamed the Danger Zone after WWE"),
        dict(label="WWE theme", value="&ldquo;Here to Show the World&rdquo;",
             sub="by Downstait, from November 2011"),
        dict(label="Also known as", value="Dolph Ziggler &middot; Nicky &middot; The Showoff"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1980-07-27",
    bornplace="Cleveland, Ohio, United States",
    nationality="United States",
    alumni="Kent State University",
    height_cm=183,
    weight_kg=97,
    ld=dict(
        alternateName=["Dolph Ziggler", "Nicholas Theodore Nemeth", "Nick Nemeth", "Nicky",
                       "The Showoff"],
        award=["World Heavyweight Championship, WWE (2 reigns, 2011 and 2013)",
               "TNA World Championship (2 reigns, 2024-2025 and 2026)",
               "WWE Intercontinental Championship (6 reigns)",
               "WWE United States Championship (2 reigns)",
               "NXT Championship (1 reign, 2022)",
               "IWGP Global Heavyweight Championship (1 reign, 2024)",
               "AAA Mega Championship (1 reign, 2024)",
               "TNA World Tag Team Championship (2 reigns, with Ryan Nemeth)",
               "WWE Raw Tag Team Championship (2 reigns)",
               "WWE SmackDown Tag Team Championship (1 reign)",
               "World Tag Team Championship (1 reign, Spirit Squad)",
               "Money in the Bank (2012)",
               "George Tragos/Lou Thesz Professional Wrestling Hall of Fame (Class of 2026)"],
        knowsAbout=["Professional wrestling", "WWE", "TNA Wrestling", "New Japan Pro-Wrestling",
                    "Amateur wrestling", "Stand-up comedy"],
        description="Nic Nemeth is an American professional wrestler who competed in WWE as Dolph "
                    "Ziggler from 2008 until his release in September 2023. In WWE he won the World "
                    "Heavyweight Championship twice, the Intercontinental Championship six times "
                    "and the NXT Championship, and won Money in the Bank in 2012. Since 2024 he has "
                    "won the IWGP Global Heavyweight, AAA Mega and TNA World championships, holding "
                    "the TNA World title twice. As of November 2026 he and his brother Ryan Nemeth "
                    "are TNA World Tag Team Champions.",
        sameAs=["https://en.wikipedia.org/wiki/Nic_Nemeth"],
    ),
)
