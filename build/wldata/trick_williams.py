# -*- coding: utf-8 -*-
"""Trick Williams - dossier data.

Compiled November 9, 2026 from data/trick-williams.md, which carries a URL for every
claim (Wikipedia, WWE.com, gamecocksonline.com, cfbstats, Fox News, Fightful,
Wrestling Inc., F4W, Bleacher Report, Post Wrestling, Sacnilk, Heavy, Solowrestling).
Every record row has a day-precision date stated in one of those sources.

Replaces a thin ~363-word page. Harvested claims checked and corrected:
  * "Winner Take All vs Oba Femi, September 23, 2025" was printed with no result.
    It was a no contest; neither title changed hands. The row is NC.
  * The old page said nothing of the second US title reign (September 6, 2026).

Deliberate omissions:
  * No Signature section. No Wrestling Observer or Cagematch star rating was
    verified for any of his matches, and this dossier does not invent grades.
  * No walk-out theme band. The chant ("Whoop That Trick") is well sourced, but
    the entrance track's title and artist are not: one Sportskeeda widget names
    "Locked In" by Def Rebel, nothing official confirms it, and a March 2026
    interview implies the main-roster theme is newer. A guessed track is worse
    than none.
  * No Right Now (pulse) section: no X post was verified quote-for-quote.
  * Slot 5 is "before" (football) rather than factions. The Trick Melo Gang and the
    Trick-Yachty Gang are covered in Personas, Career and Rivalries instead.
  * No career win-loss total. record.total is the honest row count.
  * Status "US Champion as of November 9, 2026" rests on no reported title change
    through the November 6 SmackDown and the November 7 Crown Jewel card.
"""

import html as _h

_SLUG = {
    "Oba Femi": "oba-femi",
    "Dominik Mysterio": "dominik-mysterio",
    "Sami Zayn": "sami-zayn",
    "Randy Orton": "randy-orton",
    "Damian Priest": "damian-priest",
    "Penta": "penta",
    "CM Punk": "cm-punk",
    "Kevin Owens": "kevin-owens",
    "Bron Breakker": "bron-breakker",
    "Cody Rhodes": "cody-rhodes",
}

def _opp(*names, sep=" & "):
    """Opponent cell: link names that have a page on disk, escape the rest."""
    out = []
    for n in names:
        if n in _SLUG:
            out.append('<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_SLUG[n], _h.escape(n)))
        else:
            out.append(_h.escape(n))
    return sep.join(out)

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="L", date="2020-01-31", promo="IND",
         event="CZW, Philadelphia", opponent=_opp("D. J. Hyde"),
         stip="Singles, his first recorded match", title=""),
    dict(result="W", date="2023-09-30", promo="WWE", landmark=True,
         event="NXT No Mercy", opponent=_opp("Dominik Mysterio"),
         stip="Singles, Dragon Lee as special referee. First title",
         title="NXT North American Championship"),
    dict(result="L", date="2023-10-03", promo="WWE",
         event="NXT", opponent=_opp("Dominik Mysterio"),
         stip="Singles, Judgment Day interference. The 3-day reign ends",
         title="NXT North American Championship"),
    dict(result="W", date="2023-12-09", promo="WWE", type="tag", landmark=True,
         event="NXT Deadline", opponent=_opp("The Men's Iron Survivor Challenge field"),
         stip="Iron Survivor Challenge, earns an NXT title shot", title=""),
    dict(result="L", date="2024-02-04", promo="WWE", type="tag",
         event="NXT Vengeance Day", opponent=_opp("The opposing finalists"),
         stip="Dusty Rhodes Tag Team Classic final, with Carmelo Hayes, who attacks him after",
         title=""),
    dict(result="W", date="2024-04-06", promo="WWE", landmark=True,
         event="NXT Stand & Deliver, Philadelphia", opponent=_opp("Carmelo Hayes"),
         stip="Singles, the grudge match after the betrayal", title=""),
    dict(result="W", date="2024-04-16", promo="WWE",
         event="NXT", opponent=_opp("Carmelo Hayes"),
         stip="Steel cage, ends the feud", title=""),
    dict(result="W", date="2024-04-23", promo="WWE", landmark=True,
         event="NXT Spring Breakin'", opponent=_opp("Ilja Dragunov"),
         stip="Singles, Williams had to leave NXT if he lost", title="NXT Championship"),
    dict(result="W", date="2024-06-09", promo="WWE",
         event="NXT Battleground", opponent=_opp("Ethan Page"),
         stip="Singles, first defense", title="NXT Championship"),
    dict(result="L", date="2024-07-07", promo="WWE", type="tag",
         event="NXT Heatwave", opponent=_opp("Ethan Page", "Je'Von Evans", "Shawn Spears", sep=", "),
         stip="Fatal four-way, Page pins him. The 75-day reign ends", title="NXT Championship"),
    dict(result="W", date="2024-10-01", promo="WWE", landmark=True,
         event="NXT, CW premiere, Chicago", opponent=_opp("Ethan Page"),
         stip="Singles, CM Punk as special referee", title="NXT Championship"),
    dict(result="W", date="2024-10-27", promo="WWE",
         event="NXT Halloween Havoc", opponent=_opp("Ethan Page"),
         stip="Devil's Playground", title="NXT Championship"),
    dict(result="W", date="2024-12-07", promo="WWE",
         event="NXT Deadline", opponent=_opp("Ridge Holland"),
         stip="Singles", title="NXT Championship"),
    dict(result="L", date="2025-01-07", promo="WWE", type="tag", landmark=True,
         event="NXT New Year's Evil", opponent=_opp("Oba Femi", "Eddy Thorpe"),
         stip="Triple threat, Femi wins. The 98-day reign ends", title="NXT Championship"),
    dict(result="L", date="2025-04-19", promo="WWE", type="tag",
         event="NXT Stand & Deliver", opponent=_opp("Oba Femi", "Je'Von Evans"),
         stip="Triple threat, Femi retains", title="NXT Championship"),
    dict(result="W", date="2025-05-25", promo="WWE", landmark=True,
         event="NXT Battleground", opponent=_opp("Joe Hendry"),
         stip="Singles. First WWE-contracted wrestler to win a TNA title",
         title="TNA World Championship"),
    dict(result="W", date="2025-06-03", promo="WWE",
         event="NXT", opponent=_opp("Mike Santana"),
         stip="Singles, AJ Francis and KC Navarro interfere", title="TNA World Championship"),
    dict(result="W", date="2025-06-06", promo="TNA",
         event="TNA Against All Odds", opponent=_opp("Elijah"),
         stip="Singles", title="TNA World Championship"),
    dict(result="W", date="2025-07-20", promo="TNA", type="tag",
         event="TNA Slammiversary", opponent=_opp("Joe Hendry", "AJ Francis", "Mike Santana", sep=", "),
         stip="Four-way", title="TNA World Championship"),
    dict(result="W", date="2025-08-15", promo="TNA",
         event="TNA Emergence", opponent=_opp("Moose"),
         stip="Singles", title="TNA World Championship"),
    dict(result="L", date="2025-08-19", promo="WWE",
         event="NXT", opponent=_opp("Je'Von Evans"),
         stip="No. 1 contender match, Santana interferes", title=""),
    dict(result="NC", date="2025-09-23", promo="WWE",
         event="NXT", opponent=_opp("Oba Femi"),
         stip="Winner Take All, champion vs. champion. Ends in a no contest and a TNA vs. NXT brawl",
         title="NXT & TNA World Championships"),
    dict(result="L", date="2025-10-12", promo="TNA", landmark=True,
         event="TNA Bound for Glory", opponent=_opp("Mike Santana"),
         stip="Singles, main event. The 140-day reign ends", title="TNA World Championship"),
    dict(result="L", date="2025-10-25", promo="WWE",
         event="NXT Halloween Havoc", opponent=_opp("Ricky Saints"),
         stip="Singles", title="NXT Championship"),
    dict(result="L", date="2025-11-11", promo="WWE",
         event="NXT", opponent=_opp("Ricky Saints"),
         stip="Last Man Standing", title=""),
    dict(result="W", date="2026-01-09", promo="WWE", landmark=True,
         event="SmackDown", opponent=_opp("Rey Fenix"),
         stip="Singles, main-roster debut", title=""),
    dict(result="W", date="2026-01-16", promo="WWE",
         event="SmackDown", opponent=_opp("Matt Cardona"),
         stip="Saturday Night's Main Event qualifier", title=""),
    dict(result="L", date="2026-01-31", promo="WWE", type="tag",
         event="Royal Rumble", opponent=_opp("The 2026 men's Rumble field"),
         stip="Entered No. 10, eliminated Mr. Iguana and Chad Gable; eliminated by Cody Rhodes",
         title=""),
    dict(result="W", date="2026-02-20", promo="WWE", type="tag",
         event="SmackDown", opponent=_opp("Carmelo Hayes", "Damian Priest"),
         stip="Triple threat, Elimination Chamber qualifier", title=""),
    dict(result="L", date="2026-02-28", promo="WWE", type="tag",
         event="Elimination Chamber", opponent=_opp("Randy Orton", "Cody Rhodes", "LA Knight",
                                                    "Je'Von Evans", "Logan Paul", sep=", "),
         stip="Elimination Chamber, eliminated by Logan Paul; Orton wins", title=""),
    dict(result="W", date="2026-04-19", promo="WWE", landmark=True,
         event="WrestleMania 42 Night 2, Las Vegas", opponent=_opp("Sami Zayn"),
         stip="Singles, Trick Shot counters the Helluva Kick. His WrestleMania debut",
         title="WWE United States Championship"),
    dict(result="W", date="2026-05-09", promo="WWE",
         event="Backlash", opponent=_opp("Sami Zayn"),
         stip="Singles, WrestleMania rematch", title="WWE United States Championship"),
    dict(result="W", date="2026-06-27", promo="WWE",
         event="Night of Champions", opponent=_opp("Ricky Saints"),
         stip="Singles", title="WWE United States Championship"),
    dict(result="L", date="2026-08-02", promo="WWE", landmark=True,
         event="SummerSlam Night 2, Minneapolis", opponent=_opp("Baron Corbin"),
         stip="Singles, Corbin uses the belt, then End of Days. The 105-day reign ends",
         title="WWE United States Championship"),
    dict(result="W", date="2026-09-06", promo="WWE", landmark=True,
         event="Sunday Night's Main Event", opponent=_opp("Baron Corbin"),
         stip="Singles, Trick Shot. Second reign begins", title="WWE United States Championship"),
    dict(result="W", date="2026-09-18", promo="WWE", type="tag",
         event="SmackDown", opponent=_opp("Randy Orton", "Rey Fenix"),
         stip="Triple threat, Money in the Bank qualifier", title=""),
    dict(result="L", date="2026-10-10", promo="WWE", type="tag",
         event="Money in the Bank", opponent=_opp("Penta", "CM Punk", "Kevin Owens", "Bron Breakker",
                                                  "Je'Von Evans", sep=", "),
         stip="Six-man ladder match, Penta wins", title=""),
    dict(result="W", date="2026-10-16", promo="WWE",
         event="SmackDown", opponent=_opp("Johnny Gargano"),
         stip="Non-title, Trick Shot then Book End", title=""),
    dict(result="L", date="2026-10-30", promo="WWE", landmark=True,
         event="SmackDown, Charleston", opponent=_opp("Sami Zayn"),
         stip="DQ restarted as No Disqualification; Zayn wins with a low blow and a belt shot",
         title="Undisputed WWE Championship"),
]
for _r in ROWS:
    _r["opponent_html"] = True

DATA = dict(
    slug="trick-williams",
    name="Trick Williams",
    realname="Matrick Mondre Belton",
    epithet="Whoop That Trick",
    hook="Titles, Record & Career",
    art="trick-williams",

    meta_desc=("Trick Williams went from South Carolina walk-on receiver to Carmelo Hayes's hype "
               "man to two-time NXT Champion, TNA World Champion and two-time WWE United States "
               "Champion. Full record, titles, career timeline and FAQ."),
    og_desc=("Two NXT Championships, a 140-day TNA World Championship reign, the US title in "
             "his WrestleMania debut, and a second US reign as of November 2026."),
    tw_desc="Trick Williams: walk-on receiver, hype man, NXT Champion twice, TNA World Champion, US Champion.",

    # ---------------------------------------------------------------- identity bar
    debut_label="DEBUT",
    debut_year="2021",
    height_imp="6&#8242;5&#8243;",
    weight_lb="250",
    world_titles="1",
    vitals_tagline="Whoop That Trick",
    support_note="Merch &middot; Music &middot; Watch",
    x_url="https://x.com/_trickwilliams",
    ig_url="https://www.instagram.com/trickwilliams_wwe/",
    sp_items=[
        dict(ic="TW", title="Trick Williams Merch", sub="Official gear · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable since WWE 2K23, including WWE 2K26",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/trick-williams"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Two-time NXT Champion &middot; TNA World Champion &middot; the walk-on who became the hype man who became the act",
    hero_tag="Columbia, South Carolina &middot; <em>NXT &middot; TNA &middot; SmackDown &middot; 2021&ndash;present</em>",
    now_label="NOW",
    now_bold="WWE United States Champion",
    now_tail=(" &middot; second reign, won from Baron Corbin on September 6, 2026; lost an "
              "Undisputed WWE Championship challenge to Sami Zayn on October 30 &middot; as of "
              "November 9, 2026"),
    hstats=[
        dict(value="2",   x=True,  label="NXT Titles"),
        dict(value="2",   x=True,  label="US Titles"),
        dict(value="140", x=False, label="Day TNA World Reign"),
        dict(value="105", x=False, label="Day First US Reign"),
    ],
    ghost_link="From a South Carolina walk-on to the WrestleMania stage in five years",
    vlabel="Debut 2021 &middot; Columbia, South Carolina",
    mono="TW",

    # ---------------------------------------------------------------- 01 overview
    correction=2,
    overview=[
        "<b>Trick Williams</b> came to WWE as somebody else's sidekick. He debuted on NXT on "
        "September 14, 2021 as Carmelo Hayes's friend and hype man, and five years later he is "
        "the <b>WWE United States Champion</b> on SmackDown. In between he won the NXT North "
        "American Championship, the NXT Championship twice, and the TNA World Championship, "
        "which no WWE-contracted wrestler had won before him. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">2&times;</span>'
        '<span class="pull-cap">NXT Championship reigns, 2024&ndash;25: 75 days, then 98</span></span>'
        "The crowd built the character with him. Booker T started ad-libbing &ldquo;Whoop that "
        "Trick&rdquo; on commentary, a line from Al Kapone's song in the 2005 film Hustle &amp; "
        "Flow. Fans picked it up and never stopped. Williams says it was organic, and it followed "
        "him to the main roster.",

        "Before wrestling he was a football player. He caught four passes as a wide receiver at "
        "Hampton University in 2012, then walked on at the University of South Carolina, where "
        "he caught 11 passes for 121 yards in 2015 and was named the team's Spring Outstanding "
        "Walk-on on offense. He went undrafted in 2017, tried out at a Philadelphia Eagles rookie "
        "minicamp in May 2018, took a WWE tryout that December, and trained at CZW in "
        "Philadelphia and KnokX in Los Angeles. WWE signed him on February 24, 2021. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">140</span>'
        '<span class="pull-cap">days as TNA World Champion, May 25 to October 12, 2025</span></span>'
        "The TNA reign is the strangest line on the resume. He beat Joe Hendry for the TNA World "
        "Championship at NXT Battleground on May 25, 2025, defended it on NXT and on TNA shows "
        "including Slammiversary, and lost it to Mike Santana in the Bound for Glory main event "
        "on October 12, 2025, after 140 days.",

        "One record needs its counting rule. His WWE.com profile lists two NXT Championships, "
        "and fans often call him a three-time world champion. WWE does not class the NXT "
        "Championship as a world title, so this dossier counts one world title: TNA. A second "
        "correction concerns the night he and NXT Champion Oba Femi met in a Winner Take All "
        "match on September 23, 2025. It is sometimes listed as if it had a winner. It ended in "
        "a no contest after Williams slapped Mike Santana at ringside, and neither title moved.",

        "The main-roster run started with a walkout. He declared himself a free agent on "
        "SmackDown on December 26, 2025, signed with the brand a week later, and beat Rey Fenix "
        "in his debut on January 9, 2026. He entered the Royal Rumble at No. 10, reached the "
        "Elimination Chamber, and in April teamed up with rapper Lil Yachty and turned face. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig pull-fig--sm">WM42</span>'
        '<span class="pull-cap">his WrestleMania debut, April 19, 2026: beat Sami Zayn for the US title</span></span>'
        "At WrestleMania 42 in Las Vegas on April 19, 2026, in his first WrestleMania match, he "
        "beat Sami Zayn for the United States Championship by countering the Helluva Kick with "
        "the Trick Shot. Baron Corbin took the title at SummerSlam on August 2 after 105 days. "
        "Williams won it back on September 6 at Sunday Night's Main Event. On October 30 he "
        "challenged Zayn, now the Undisputed WWE Champion, and lost after a low blow and a belt "
        "shot. As of November 9, 2026 he is still the US Champion.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Highlight set",
        promo_order=["WWE", "TNA", "IND"],
        promo_labels={"WWE": "WWE / NXT", "TNA": "TNA", "IND": "Indie"},
        stats=[
            ("2&times;", "NXT titles"),
            ("2&times;", "US titles"),
            ("1",        "TNA world title"),
            ("1",        "NA title"),
            ("140",      "Day TNA reign"),
            ("2026",     "WrestleMania debut"),
        ],
        lead=("Every title change, every title defense on a premium event we could date, and the "
              "TV milestones from his first recorded match in 2020 to October 30, 2026. This is a "
              "highlight set, not a career count, and no career win&ndash;loss total is published "
              "because none was verified. NXT matches are filed under WWE. Filter by match type, "
              "tap any column header to sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("2&times;", "WWE United States"),
            ("2&times;", "NXT Championship"),
            ("1",        "TNA World"),
            ("1",        "NXT North American"),
        ],
        lead=("Six reigns across four championships in three years, plus the 2023 Iron Survivor "
              "Challenge. Only the TNA title counts as a world title by its promotion's own "
              "rules."),
        rows=[
            dict(ic="US", name="WWE United States Championship", count="2",
                 sub="2026, won from Sami Zayn at WrestleMania 42 Night 2 in Las Vegas on April 19; "
                     "retained against Zayn at Backlash on May 9 and Ricky Saints at Night of "
                     "Champions on June 27; lost to Baron Corbin at SummerSlam in Minneapolis on "
                     "August 2 after <b>105 days</b> &middot; 2026, regained from Corbin at "
                     "Sunday Night's Main Event on September 6; <b>current as of November 9, "
                     "2026</b>"),
            dict(ic="N", name="NXT Championship", count="2",
                 sub="2024, won from Ilja Dragunov at Spring Breakin' on April 23 with his NXT "
                     "career on the line; lost to Ethan Page in a fatal four-way at Heatwave on "
                     "July 7 after 75 days &middot; 2024&ndash;25, regained from Page on NXT's "
                     "CW premiere in Chicago on October 1 with CM Punk refereeing; lost to Oba "
                     "Femi in a triple threat at New Year's Evil on January 7, 2025 after 98 "
                     "days. WWE does not class this title as a world championship"),
            dict(ic="T", name="TNA World Championship", count="1",
                 sub="2025, won from Joe Hendry at NXT Battleground on May 25, the first "
                     "WWE-contracted wrestler to win a TNA title; defended against Mike Santana, "
                     "Elijah, a Slammiversary four-way and Moose; lost to Santana at Bound for "
                     "Glory on October 12 after <b>140 days</b>"),
            dict(ic="NA", name="NXT North American Championship", count="1",
                 sub="2023, won from Dominik Mysterio at No Mercy on September 30; lost back to "
                     "Mysterio on October 3 after Judgment Day interference. Three days, the "
                     "shortest reign in the title's history"),
        ],
    ),

    # ---------------------------------------------------------------- 05 before
    slot5=dict(
        id="before",
        h2="Before WWE",
        lead="A wide receiver first. The wrestling started at 25.",
        cards=[
            dict(era="Hampton &middot; 2012&ndash;13",
                 name="Hampton Pirates",
                 members="Wide receiver, scholarship player",
                 desc="Six games and one start as a freshman in 2012, with four catches for 33 "
                      "yards, including a 20-yard catch at Florida A&M. He was on the 2013 roster "
                      "but did not play; Wikipedia attributes the lost season to a pulled "
                      "hamstring."),
            dict(era="South Carolina &middot; 2014&ndash;16",
                 name="South Carolina Gamecocks",
                 members="Walk-on wide receiver, No. 15",
                 desc="Walked on in his hometown in spring 2014 and sat out the fall under "
                      "transfer rules. In 2015 he played every game, started five, caught 11 "
                      "passes for 121 yards and won the team's Spring Outstanding Walk-on award "
                      "on offense. In 2016 he played nine games, mostly on special teams, and "
                      "made the SEC Fall Academic Honor Roll. Graduated in December 2016."),
            dict(era="2017&ndash;18",
                 name="The NFL door",
                 members="Undrafted; Philadelphia Eagles tryout",
                 desc="Undrafted in 2017. He attended a Philadelphia Eagles rookie minicamp on a "
                      "tryout basis in May 2018. That December he took a WWE tryout instead."),
            dict(era="2019&ndash;21",
                 name="CZW and KnokX",
                 members="Training in Philadelphia, then Los Angeles",
                 desc="Trained with CZW in Philadelphia, where his first recorded match was a "
                      "loss to D. J. Hyde on January 31, 2020, then moved to KnokX in Los "
                      "Angeles. He built a Dolemite-inspired character, Sweet Daddy Trick, named "
                      "after his uncle's nickname. WWE signed him on February 24, 2021."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One name the whole way. Four different jobs inside it.",
        cards=[
            dict(mono="TM", era="NXT &middot; 2021&ndash;23", name="The hype man",
                 desc="Carmelo Hayes's friend and second in the Trick Melo Gang, introduced by "
                      "attacking Duke Hudson on September 14, 2021. A heel act until Bron "
                      "Breakker attacked them on April 4, 2023 and the pair turned face."),
            dict(mono="WT", era="NXT &middot; 2023&ndash;25", name="Whoop That Trick",
                 desc="The solo run. An amicable split on August 1, 2023, the North American "
                      "title, the Iron Survivor win, Hayes's betrayal at Vengeance Day 2024, and "
                      "two NXT Championship reigns, with the crowd chanting Booker T's ad-lib at "
                      "every entrance."),
            dict(mono="TC", era="NXT and TNA &middot; 2025", name="The crossover heel",
                 desc="Insulted and attacked Joe Hendry at TNA Rebellion on April 27, 2025, took "
                      "his TNA World Championship a month later, and defended it across both "
                      "promotions with AJ Francis and KC Navarro in his corner."),
            dict(mono="TY", era="SmackDown &middot; 2026&ndash;present", name="The champion with a rapper",
                 desc="Free agent in December 2025, SmackDown in January 2026, and a face turn "
                      "in April alongside Lil Yachty as the Trick-Yachty Gang. He ended the "
                      "weekly US title open challenges because he wants that belt treated as the "
                      "top prize on the show."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Walk-on, tryout, hype man, champion of three promotions' belts.",
        rows=[
            dict(year="2015", title="South Carolina",
                 desc="Plays every game for the Gamecocks as a walk-on wide receiver: 11 catches, "
                      "121 yards, five starts."),
            dict(year="2018", title="Two tryouts",
                 desc="Philadelphia Eagles rookie minicamp in May, WWE tryout in December."),
            dict(year="2020", title="First recorded match",
                 desc="Loses to D. J. Hyde at CZW in Philadelphia on January 31."),
            dict(year="2021", title="Signed, then on TV",
                 desc="Signs with WWE on February 24 and debuts on NXT on September 14 as "
                      "Carmelo Hayes's friend. The Trick Melo Gang begins."),
            dict(year="2023", title="Out on his own",
                 desc="Turns face with Hayes in April, splits amicably on August 1, wins the "
                      "North American title from Dominik Mysterio at No Mercy on September 30 "
                      "and loses it three days later, then wins the Iron Survivor Challenge on "
                      "December 9."),
            dict(year="2024", title="Betrayed, then champion twice",
                 desc="Hayes hits him with a chair after the Dusty Rhodes Tag Team Classic final "
                      "on February 4. Williams beats him at Stand & Deliver on April 6 and in a "
                      "cage on April 16, wins the NXT Championship from Ilja Dragunov on April "
                      "23, loses it to Ethan Page on July 7, and wins it back on October 1."),
            dict(year="2025", title="The TNA World Champion",
                 desc="Loses the NXT title to Oba Femi on January 7. Wins the TNA World "
                      "Championship from Joe Hendry on May 25 and holds it 140 days until Mike "
                      "Santana beats him at Bound for Glory on October 12. Declares himself a "
                      "free agent on SmackDown on December 26."),
            dict(year="2026", title="SmackDown and the US title",
                 desc="Debuts with a win over Rey Fenix on January 9, beats Sami Zayn for the "
                      "US title at WrestleMania 42 on April 19, marries Lash Legend on June 20, "
                      "loses the belt to Baron Corbin at SummerSlam on August 2 and regains it on "
                      "September 6. Falls short in the Money in the Bank ladder match on October "
                      "10 and against Zayn for the Undisputed WWE Championship on October 30."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went through.",
        cards=[
            dict(name="Carmelo Hayes",
                 desc="Best friend, partner, then the man who hit him with a chair at Vengeance "
                      "Day on February 4, 2024 and admitted two days later that he had also "
                      "ordered the October 2023 backstage attack. Williams won the Stand & "
                      "Deliver singles match on April 6 and the cage match ten days later. They "
                      "crossed again on SmackDown in an Elimination Chamber qualifier in February "
                      "2026, which Williams won."),
            dict(name="Oba Femi", slug="oba-femi",
                 desc="The wall at the top of NXT. Femi took the NXT Championship from him in a "
                      "triple threat on January 7, 2025, beat him again at Stand & Deliver that "
                      "April, and met him champion against champion in a Winner Take All match "
                      "on September 23, 2025 that ended in a no contest."),
            dict(name="Ethan Page",
                 desc="The NXT title trade of 2024: Williams beat him at Battleground, lost the "
                      "belt to him in a Heatwave four-way, took it back on the CW premiere with "
                      "CM Punk refereeing, and retained in a Devil's Playground match at "
                      "Halloween Havoc."),
            dict(name="Joe Hendry & Mike Santana",
                 desc="The TNA chapter. Williams invaded TNA to attack Hendry, took his world "
                      "title at NXT Battleground, and beat both men in the Slammiversary four-way. "
                      "Santana kept coming, cost him an NXT No. 1 contender match in August, and "
                      "ended the reign at Bound for Glory."),
            dict(name="Sami Zayn", slug="sami-zayn",
                 desc="Williams took the US title from him at WrestleMania 42 and beat him again "
                      "at Backlash. By October Zayn was the Undisputed WWE Champion, and he kept "
                      "that title against Williams on October 30 with a low blow and a belt shot."),
            dict(name="Baron Corbin",
                 desc="Back in WWE in July 2026, Corbin took the US title at SummerSlam with the "
                      "belt and End of Days. Williams won it back from him at Sunday Night's Main "
                      "Event five weeks later."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Music",
        lead="He records his own songs, and the crowd wrote his best-known line.",
        rows=[
            dict(when="2023&ndash;", title="Singles", kind="Music",
                 desc="\"Good Lookin' Wrassla\" (2023), \"The Realest\", \"Game Over\" and "
                      "\"Tricky Whoopin'\" (2024), \"Pronto\" featuring Kevo, \"Average Joe\" and "
                      "\"Mike Who?\" (2025), and \"Gingerbread Man\" featuring Lil Yachty (2026)."),
            dict(when="NXT&ndash;", title="\"Whoop That Trick\"", kind="Chant",
                 desc="Started from Booker T's ad-libs on NXT commentary, borrowed from Al "
                      "Kapone's song in Hustle & Flow. Kapone later reached out to him on "
                      "Instagram. His entrance theme itself is an instrumental WWE built from his "
                      "pitch of Baby Keem and Kendrick Lamar's \"Family Ties\"."),
            dict(when="2023&ndash;", title="WWE 2K", kind="Game",
                 desc="DLC in WWE 2K23, then on the roster in WWE 2K24, 2K25 and 2K26."),
            dict(when="TV", title="All American", kind="Screen",
                 desc="An extra in season 3, then a guest role as Eddie Blair in the season 7 "
                      "finale."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, with the rules that make them true.",
        stats=[
            ("1st", "WWE talent with a TNA title"),
            ("3",   "Day NA reign, a record low"),
            ("10",  "Rumble entry number, 2026"),
        ],
        rows=[
            dict(name="First WWE-contracted wrestler to win a TNA championship",
                 sub="May 25, 2025, over Joe Hendry at NXT Battleground. WWE.com phrases it as "
                     "the first active WWE Superstar to win the TNA World Title."),
            dict(name="US Champion in his WrestleMania debut",
                 sub="WrestleMania 42 Night 2, April 19, 2026, against Sami Zayn in Las Vegas."),
            dict(name="Two NXT Championship reigns in one calendar year",
                 sub="April 23 to July 7, 2024 (75 days) and October 1, 2024 to January 7, 2025 "
                     "(98 days)."),
            dict(name="Shortest NXT North American Championship reign",
                 sub="Three days, September 30 to October 3, 2023, both ends against Dominik "
                     "Mysterio."),
            dict(name="2023 Men's Iron Survivor Challenge winner",
                 sub="NXT Deadline, December 9, 2023."),
            dict(name="Champion in WWE and TNA within twelve months of each other",
                 sub="TNA World Champion until October 12, 2025; WWE United States Champion from "
                     "April 19, 2026."),
        ],
        footnote=("No career win-loss total appears on this page; none was verified. World titles "
                  "are counted as one because WWE does not class the NXT Championship as a world "
                  "title. Current-champion status is as of November 9, 2026."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="X / Twitter", v="@_trickwilliams", href="https://x.com/_trickwilliams"),
        dict(k="Instagram", v="@trickwilliams_wwe", href="https://www.instagram.com/trickwilliams_wwe/"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/trick-williams"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Trick_Williams"),
        dict(k="Gamecocks", v="South Carolina football bio",
             href="https://gamecocksonline.com/sports/football/roster/player/matrick-belton/"),
        dict(k="Fox News", v="WrestleMania 42 US title win",
             href="https://www.foxnews.com/sports/trick-williams-wins-united-states-championship-wrestlemania-debut"),
        dict(k="Fightful", v="US title regained, September 6, 2026",
             href="https://www.fightful.com/wrestling-news/trick-williams-wins-united-states-title-at-sunday-nights-main-event/"),
        dict(k="Wrestling Inc.", v="TNA World Championship win",
             href="https://www.wrestlinginc.com/1869092/trick-williams-defeats-joe-hendry-wins-tna-world-championship-wwe-nxt-battleground"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/trick-williams.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Trick Williams the current United States Champion?",
            a="Yes, as of November 9, 2026. He won the title back from Baron Corbin at Sunday "
              "Night's Main Event on <b>September 6, 2026</b>, his second reign. His first ran "
              "105 days, from WrestleMania 42 on April 19 to SummerSlam on August 2.",
            q_ld="Is Trick Williams the current WWE United States Champion?",
            a_ld="As of November 9, 2026, Trick Williams is the WWE United States Champion. He won "
                 "the title for the second time by beating Baron Corbin at Sunday Night's Main "
                 "Event on September 6, 2026. His first reign lasted 105 days, from WrestleMania 42 "
                 "on April 19, 2026 to SummerSlam on August 2, 2026."),
        dict(
            q="How many times has Trick Williams been NXT Champion?",
            a="Twice. He beat Ilja Dragunov on April 23, 2024 and lost to Ethan Page on July 7 "
              "(75 days). He beat Page on October 1, 2024 and lost to Oba Femi on January 7, 2025 "
              "(98 days).",
            q_ld="How many times has Trick Williams been NXT Champion?",
            a_ld="Trick Williams has been NXT Champion twice. He won the title from Ilja Dragunov "
                 "on April 23, 2024 and lost it to Ethan Page on July 7, 2024 after 75 days. He "
                 "regained it from Page on October 1, 2024 and lost it to Oba Femi on January 7, "
                 "2025 after 98 days."),
        dict(
            q="Was Trick Williams TNA World Champion?",
            a="Yes. He beat Joe Hendry for the TNA World Championship at NXT Battleground on "
              "<b>May 25, 2025</b>, the first WWE-contracted wrestler to win a TNA title. He lost "
              "it to Mike Santana at Bound for Glory on October 12, 2025, after 140 days.",
            q_ld="Was Trick Williams the TNA World Champion?",
            a_ld="Yes. Trick Williams won the TNA World Championship from Joe Hendry at NXT "
                 "Battleground on May 25, 2025, becoming the first WWE-contracted wrestler to win "
                 "a TNA championship. He held it for 140 days before losing to Mike Santana at "
                 "TNA Bound for Glory on October 12, 2025."),
        dict(
            q="Why did Trick Williams and Carmelo Hayes split up?",
            a="Twice over. Williams ended the Trick Melo Gang amicably on August 1, 2023 to chase "
              "his own titles. They reunited for the Dusty Rhodes Tag Team Classic, and after "
              "losing the final at Vengeance Day on February 4, 2024, Hayes hit him with a chair. "
              "Two days later Hayes admitted he was behind the October 2023 backstage attack too. "
              "Williams beat him at Stand & Deliver on April 6, 2024.",
            q_ld="Why did Trick Williams and Carmelo Hayes split up?",
            a_ld="Trick Williams first ended his partnership with Carmelo Hayes amicably on "
                 "August 1, 2023. They reunited for the Dusty Rhodes Tag Team Classic in early "
                 "2024, but after losing the final at NXT Vengeance Day on February 4, 2024, Hayes "
                 "attacked Williams with a steel chair and admitted he had ordered an October 2023 "
                 "attack on him. Williams beat Hayes at NXT Stand & Deliver on April 6, 2024."),
        dict(
            q="Did Trick Williams play college football?",
            a="Yes, as a wide receiver. He played at Hampton in 2012, then walked on at South "
              "Carolina, where he caught <b>11 passes for 121 yards</b> in 2015. He went undrafted "
              "in 2017 and had a Philadelphia Eagles minicamp tryout in May 2018.",
            q_ld="Did Trick Williams play college football?",
            a_ld="Yes. Trick Williams, whose real name is Matrick Belton, played wide receiver at "
                 "Hampton University in 2012 and then walked on at the University of South "
                 "Carolina, where he caught 11 passes for 121 yards in 2015. He went undrafted in "
                 "2017 and attended a Philadelphia Eagles rookie minicamp on a tryout in May 2018."),
        dict(
            q="Where does the \"Whoop That Trick\" chant come from?",
            a="From Al Kapone's song in the 2005 film Hustle &amp; Flow, by way of Booker T, who "
              "started ad-libbing the line on NXT commentary. Fans took it from there. His actual "
              "entrance theme is an instrumental; the words come from the crowd.",
            q_ld="Where does the Whoop That Trick chant come from?",
            a_ld="The Whoop That Trick chant comes from Al Kapone's song in the 2005 film Hustle "
                 "and Flow. Booker T began ad-libbing the phrase on NXT commentary during Trick "
                 "Williams's entrances, and fans adopted it. Trick Williams's entrance theme is an "
                 "instrumental, so the words come from the crowd."),
        dict(
            q="What happened in the Winner Take All match with Oba Femi?",
            a="Nothing changed hands. On September 23, 2025, NXT Champion Oba Femi faced TNA World "
              "Champion Williams on NXT with both belts at stake. It ended in a <b>no contest</b> "
              "after Williams slapped Mike Santana at ringside and the TNA and NXT rosters "
              "brawled.",
            q_ld="What happened in the Trick Williams vs. Oba Femi Winner Take All match?",
            a_ld="On September 23, 2025, NXT Champion Oba Femi faced TNA World Champion Trick "
                 "Williams on NXT in a Winner Take All match. It ended in a no contest after "
                 "Williams slapped Mike Santana at ringside and a brawl broke out between TNA and "
                 "NXT wrestlers. Neither title changed hands."),
        dict(
            q="When did Trick Williams join the main roster?",
            a="He declared himself a free agent on SmackDown on December 26, 2025, announced on "
              "January 2, 2026 that he had signed with SmackDown, and beat Rey Fenix in his debut "
              "match on <b>January 9, 2026</b>.",
            q_ld="When did Trick Williams join the WWE main roster?",
            a_ld="Trick Williams declared himself a free agent on SmackDown on December 26, 2025, "
                 "announced he had signed with SmackDown on January 2, 2026, and won his main "
                 "roster debut match against Rey Fenix on January 9, 2026."),
        dict(
            q="Who is Trick Williams married to?",
            a="WWE wrestler Lash Legend. They married on June 20, 2026 in Port Antonio, Jamaica.",
            q_ld="Who is Trick Williams married to?",
            a_ld="Trick Williams is married to WWE wrestler Lash Legend. They married on June 20, "
                 "2026 in Port Antonio, Jamaica."),
        dict(
            q="Is Trick Williams a world champion?",
            a="Once, by the strict count. The TNA World Championship is a world title. His two "
              "NXT Championships are not, because WWE does not class the NXT title as a world "
              "championship. He challenged Sami Zayn for the Undisputed WWE Championship on "
              "October 30, 2026 and lost.",
            q_ld="Is Trick Williams a world champion?",
            a_ld="Trick Williams has held one world championship, the TNA World Championship, from "
                 "May to October 2025. His two NXT Championship reigns are not counted as world "
                 "title reigns because WWE does not class the NXT Championship as a world title. "
                 "He lost a challenge for the Undisputed WWE Championship to Sami Zayn on October "
                 "30, 2026."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Matrick Mondre Belton"),
        dict(label="Born", value="May 26, 1994", sub="Columbia, South Carolina &middot; age 32"),
        dict(label="Billed from", value="Columbia, S.C."),
        dict(label="Height", value="6&#8242;5&#8243;",
             sub="196 cm, billed &middot; South Carolina listed him 6&#8242;3&#8243; as a receiver"),
        dict(label="Weight", value="250 lb", sub="113 kg, billed"),
        dict(label="College", value="Hampton &middot; South Carolina",
             sub="wide receiver, 2012&ndash;16; walk-on at South Carolina"),
        dict(label="Signed", value="February 24, 2021", sub="after a December 2018 WWE tryout"),
        dict(label="NXT debut", value="September 14, 2021", sub="beside Carmelo Hayes"),
        dict(label="Main roster", value="January 9, 2026", sub="SmackDown, W over Rey Fenix"),
        dict(label="Finisher", value="Trick Shot", sub="running knee &middot; also the Trick Kick"),
        dict(label="Current title", value="WWE United States",
             sub="second reign since September 6, 2026 &middot; as of November 9"),
        dict(label="Also known as", value="Sweet Daddy Trick (pre-WWE) &middot; Trick Melo Gang"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1994-05-26",
    bornplace="Columbia, South Carolina, U.S.",
    nationality="United States",
    alumni="University of South Carolina",
    height_cm=196,
    weight_kg=113,
    ld=dict(
        alternateName=["Matrick Mondre Belton", "Matrick Belton", "Sweet Daddy Trick"],
        award=["WWE United States Championship (2 reigns, 2026)",
               "NXT Championship (2 reigns, 2024-2025)",
               "TNA World Championship (1 reign, 2025)",
               "NXT North American Championship (1 reign, 2023)",
               "NXT Men's Iron Survivor Challenge winner (2023)"],
        knowsAbout=["Professional wrestling", "WWE", "NXT", "TNA Wrestling", "American football"],
        description="Trick Williams is an American professional wrestler signed to WWE on the "
                    "SmackDown brand. A former wide receiver at Hampton University and the "
                    "University of South Carolina, he debuted on NXT in 2021 alongside Carmelo "
                    "Hayes, became a two-time NXT Champion, won the NXT North American "
                    "Championship, and held the TNA World Championship for 140 days in 2025 as "
                    "the first WWE-contracted wrestler to win a TNA title. He won the WWE United "
                    "States Championship at WrestleMania 42 in April 2026 and regained it in "
                    "September 2026.",
        sameAs=["https://x.com/_trickwilliams",
                "https://www.instagram.com/trickwilliams_wwe/",
                "https://en.wikipedia.org/wiki/Trick_Williams",
                "https://www.wwe.com/superstars/trick-williams"],
    ),
)
