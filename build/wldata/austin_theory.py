# -*- coding: utf-8 -*-
"""Austin Theory - dossier data.

Compiled November 9, 2026 from data/austin-theory.md, which carries a URL for every
claim. Sources opened for this build: Wikipedia (Austin Theory; A-Town Down Under;
2022 Money in the Bank), WWE.com (profile, 2019 signing release, WrestleMania 36 and
39 results, Survivor Series 2022 result, 2026 Royal Rumble stats), ESPN profile,
Fightful, Wrestling Inc., F4W, Fox Sports, Bleacher Report, PWInsider via Sports
Illustrated, Khel Now and Sacnilk (Crown Jewel 2026 results).

The old /wrestlers/austin-theory/ page (~210 words) was harvested and checked. It
was correct that Theory and Bron Breakker won the World Tag Team Championship on
Raw on July 6, 2026, but it called that his only reign. It was his second: he first
won the titles with Logan Paul on March 30, 2026. The pair also lost the belts at
Crown Jewel on November 7, 2026, which the old page predates.

Deliberate omissions and flags:
  * No Signature section. No Wrestling Observer or Cagematch rating was verified
    for any Theory match, and this dossier does not invent star ratings.
  * No walk-out band. No source verified the title of his entrance theme.
  * No career win-loss total. None is verified anywhere; record.total is the
    honest row count.
  * Slot 5 is "factions" (The Way, A-Town Down Under, The Vision). Pre-WWE work
    (WWA4, Evolve, WWN, FIP) is covered in the record, titles, career and personas.
  * "Youngest US Champion in WWE history" is ESPN's claim. The same ESPN profile
    misdates his first US title, so the claim is attributed, not adopted.
  * WWE.com's bio credits title success in Progress and CMLL. No such title is
    listed anywhere else, so none is printed.
  * The one-name "Theory" era ended in August 2022 per Wikipedia, at Clash at the
    Castle (September 3, 2022) per SEScoops. Both are noted; neither is adopted.
"""

_LINKS = {
    "John Cena": "john-cena", "Seth Rollins": "seth-rollins", "Bobby Lashley": "bobby-lashley",
    "Finn Balor": "finn-balor", "Rey Mysterio": "rey-mysterio", "Oba Femi": "oba-femi",
    "Penta": "penta", "LA Knight": "la-knight", "Brock Lesnar": "brock-lesnar",
    "Drew McIntyre": "drew-mcintyre", "Sami Zayn": "sami-zayn", "Sheamus": "sheamus",
    "Damian Priest": "damian-priest", "Cody Rhodes": "cody-rhodes", "Jey Uso": "jey-uso",
}

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="L", date="2016-04-29", promo="IND", type="tag",
         event="Glory Pro Wrestling", opponent="Mike Cobb & Poncho Arp",
         stip="Three-way, his professional debut", title=""),
    dict(result="W", date="2016-05-05", promo="IND", landmark=True,
         event="WWA4", opponent="AR Fox",
         stip="Singles, a week into his career, against his own trainer",
         title="WWA4 Heavyweight Championship"),
    dict(result="W", date="2017-02-24", promo="IND",
         event="Evolve 78", opponent="Darby Allin",
         stip="Singles, his Evolve debut", title=""),
    dict(result="W", date="2017-12-10", promo="IND",
         event="Evolve 97", opponent="Fred Yehi",
         stip="Singles", title="FIP World Heavyweight Championship"),
    dict(result="W", date="2018-04-06", promo="IND",
         event="WWN", opponent="Keith Lee",
         stip="Singles, first WWN title", title="WWN Championship"),
    dict(result="W", date="2018-12-15", promo="IND", type="tag", landmark=True,
         event="Evolve 117", opponent="Fabian Aichner & Roderick Strong",
         stip="Triple threat, takes the title from Aichner", title="Evolve Championship"),
    dict(result="W", date="2019-07-13", promo="IND", landmark=True,
         event="Evolve 131 (10th Anniversary)", opponent="JD Drake",
         stip="Winner takes all, holds Evolve and WWN gold at once",
         title="WWN Championship"),
    dict(result="L", date="2019-11-09", promo="IND",
         event="Evolve 139", opponent="Josh Briggs",
         stip="Singles, the Evolve reign ends after WWE signing", title="Evolve Championship"),
    dict(result="L", date="2019-12-25", promo="WWE", landmark=True,
         event="NXT (TV debut)", opponent="Roderick Strong",
         stip="Open challenge, his first televised WWE match",
         title="NXT North American Championship"),
    dict(result="L", date="2020-04-05", promo="WWE", type="tag",
         event="WrestleMania 36 Night 2", opponent="The Street Profits",
         stip="Tag, with Angel Garza, replacing Andrade", title="Raw Tag Team Championship"),
    dict(result="L", date="2020-09-08", promo="WWE",
         event="NXT Super Tuesday II", opponent="Bronson Reed",
         stip="Singles", title=""),
    dict(result="L", date="2021-11-22", promo="WWE", landmark=True,
         event="Raw", opponent="Big E",
         stip="Singles, the reward for stealing Vince McMahon's egg",
         title="WWE Championship"),
    dict(result="L", date="2022-01-29", promo="WWE", type="tag",
         event="Royal Rumble", opponent="The 2022 men's Rumble field",
         stip="Entered No. 3, eliminated by AJ Styles", title=""),
    dict(result="L", date="2022-02-19", promo="WWE", type="tag",
         event="Elimination Chamber", opponent="Brock Lesnar and the Chamber field",
         stip="Elimination Chamber, last man eliminated by Lesnar", title="WWE Championship"),
    dict(result="L", date="2022-04-03", promo="WWE",
         event="WrestleMania 38 Night 2", opponent="Pat McAfee",
         stip="Singles, then a Stone Cold Stunner afterward", title=""),
    dict(result="W", date="2022-04-18", promo="WWE", landmark=True,
         event="Raw", opponent="Finn Balor",
         stip="Singles, first WWE title at 24", title="United States Championship"),
    dict(result="W", date="2022-06-05", promo="WWE",
         event="Hell in a Cell", opponent="Mustafa Ali",
         stip="Singles, retains", title="United States Championship"),
    dict(result="L", date="2022-07-02", promo="WWE",
         event="Money in the Bank", opponent="Bobby Lashley",
         stip="Singles, taps to the Hurt Lock; 75-day reign ends",
         title="United States Championship"),
    dict(result="W", date="2022-07-02", promo="WWE", type="tag", landmark=True,
         event="Money in the Bank", opponent="Riddle, Seth Rollins, Drew McIntyre, Sami Zayn, Sheamus, Omos & Madcap Moss",
         stip="Ladder match as the unannounced eighth entrant, two hours after losing the US title",
         title="Money in the Bank contract"),
    dict(result="L", date="2022-11-07", promo="WWE",
         event="Raw", opponent="Seth Rollins",
         stip="Money in the Bank cash-in, Lashley pulled him out", title="United States Championship"),
    dict(result="W", date="2022-11-26", promo="WWE", type="tag", landmark=True,
         event="Survivor Series WarGames", opponent="Seth Rollins & Bobby Lashley",
         stip="Triple threat, second US title", title="United States Championship"),
    dict(result="W", date="2023-02-18", promo="WWE", type="tag",
         event="Elimination Chamber, Montreal", opponent="Seth Rollins, Bronson Reed, Damian Priest, Johnny Gargano & Montez Ford",
         stip="Elimination Chamber, retains with help from Logan Paul",
         title="United States Championship"),
    dict(result="W", date="2023-04-01", promo="WWE", landmark=True,
         event="WrestleMania 39 Night 1", opponent="John Cena",
         stip="Singles, opened the show; low blow and A-Town Down with the referee down",
         title="United States Championship"),
    dict(result="W", date="2023-05-06", promo="WWE", type="tag",
         event="Backlash", opponent="Bobby Lashley & Bronson Reed",
         stip="Triple threat, retains", title="United States Championship"),
    dict(result="L", date="2023-08-11", promo="WWE", landmark=True,
         event="SmackDown", opponent="Rey Mysterio",
         stip="Impromptu match, Mysterio replaced Santos Escobar; 258-day reign ends",
         title="United States Championship"),
    dict(result="L", date="2023-09-02", promo="WWE",
         event="Payback", opponent="Rey Mysterio",
         stip="Singles, rematch", title="United States Championship"),
    dict(result="L", date="2023-10-13", promo="WWE", type="tag",
         event="SmackDown", opponent="Cody Rhodes & Jey Uso",
         stip="Tag, with Grayson Waller", title="Undisputed WWE Tag Team Championship"),
    dict(result="W", date="2024-04-06", promo="WWE", type="tag", landmark=True,
         event="WrestleMania XL Night 1", opponent="Judgment Day, The New Day, #DIY, New Catch Republic, The Miz & R-Truth",
         stip="Six-pack ladder, with Waller, who pulled down the SmackDown belts",
         title="WWE Tag Team Championship"),
    dict(result="W", date="2024-05-03", promo="WWE", type="tag",
         event="SmackDown", opponent="The Street Profits",
         stip="Tag, first title defense", title="WWE Tag Team Championship"),
    dict(result="L", date="2024-07-05", promo="WWE", type="tag",
         event="SmackDown", opponent="#DIY",
         stip="Tag, the 90-day reign ends", title="WWE Tag Team Championship"),
    dict(result="L", date="2025-02-15", promo="WWE", type="tag",
         event="NXT Vengeance Day", opponent="Oba Femi & Grayson Waller",
         stip="Three-way, Femi pinned Waller after Waller hit Theory by mistake",
         title="NXT Championship"),
    dict(result="L", date="2026-01-31", promo="WWE", type="tag",
         event="Royal Rumble", opponent="The 2026 men's Rumble field",
         stip="Entered No. 15, eliminated La Parka, eliminated by LA Knight", title=""),
    dict(result="W", date="2026-03-30", promo="WWE", type="tag", landmark=True,
         event="Raw", opponent="The Usos",
         stip="Street Fight, with Logan Paul; brass knuckles finish",
         title="World Tag Team Championship"),
    dict(result="L", date="2026-04-18", promo="WWE", type="tag",
         event="WrestleMania 42 Night 1", opponent="LA Knight & The Usos",
         stip="Six-man, with Logan Paul & IShowSpeed; pinned after the BFT", title=""),
    dict(result="W", date="2026-05-23", promo="WWE", type="tag",
         event="Saturday Night's Main Event", opponent="The Street Profits",
         stip="Tag, with Paul; Heyman put Theory's foot on the rope",
         title="World Tag Team Championship"),
    dict(result="L", date="2026-06-22", promo="WWE", type="tag",
         event="Raw", opponent="The Street Profits",
         stip="Tag, with Bron Breakker for the injured Paul; Rollins hit Theory with the knuckles",
         title="World Tag Team Championship"),
    dict(result="W", date="2026-07-06", promo="WWE", type="tag", landmark=True,
         event="Raw", opponent="The Street Profits",
         stip="Tag, with Breakker; a Maxxine Dupri low blow set up the pin",
         title="World Tag Team Championship"),
    dict(result="L", date="2026-11-07", promo="WWE", type="tag", landmark=True,
         event="Crown Jewel, Riyadh", opponent="Penta & Je'Von Evans",
         stip="Tag, with Breakker; pinned after the Mexican Destroyer and OG Cutter",
         title="World Tag Team Championship"),
]

def _link(s):
    out, hit = s, False
    for name, slug in _LINKS.items():
        if name in out:
            out = out.replace(name, '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (slug, name))
            hit = True
    return out, hit

for _r in ROWS:
    _o, _hit = _link(_r["opponent"].replace("&", "&amp;"))
    if _hit:
        _r["opponent"] = _o
        _r["opponent_html"] = True

DATA = dict(
    slug="austin-theory",
    art="austin-theory",
    name="Austin Theory",
    realname="Austin Tyler White",
    epithet="The A-Town Kid",
    hook="Record, Titles & WrestleMania 39",

    meta_desc=("Austin Theory beat John Cena at WrestleMania 39, won Money in the Bank at 24, held "
               "the US Championship twice and has five tag and US title reigns. Full record, titles, "
               "factions and career, checked November 2026."),
    og_desc=("Evolve and WWN champion at 21, Mr. McMahon's protege, 2022 Money in the Bank winner, "
             "two-time US Champion, the man who beat John Cena at WrestleMania 39, and a two-time "
             "World Tag Team Champion in The Vision."),
    tw_desc="Austin Theory: two US titles, a WrestleMania win over John Cena, and three tag title reigns.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="2016",
    height_imp="6&#8242;1&#8243;",
    weight_lb="220",
    vitals_tagline="A-Town Down",
    support_note="Merch &middot; Games &middot; Watch",
    x_url="https://x.com/_Theory1",
    ig_url="https://www.instagram.com/austin_theory/",
    sp_items=[
        dict(ic="AT", title="WWE Shop", sub="Official tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable from WWE 2K22 to WWE 2K26",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/austin-theory"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Two-time US Champion &middot; Money in the Bank 2022 &middot; beat John Cena at WrestleMania 39",
    hero_tag="McDonough, Georgia &middot; <em>Evolve &amp; WWN &middot; WWE since 2019 &middot; Raw, The Vision</em>",
    now_label="NOW",
    now_bold="Raw · The Vision",
    now_tail=(" &middot; lost the World Tag Team Championship with Bron Breakker to Penta and "
              "Je&rsquo;Von Evans at Crown Jewel on November 7, 2026, ending a 124-day reign"),
    hstats=[
        dict(value="2",    x=True,  label="US Title Reigns"),
        dict(value="3",    x=True,  label="Tag Title Reigns"),
        dict(value="258",  x=False, label="Day US Title Reign"),
        dict(value="2022", x=False, label="Money in the Bank"),
    ],
    ghost_link="From a Georgia gym class to beating John Cena at WrestleMania",
    vlabel="Est. 2016 &middot; McDonough, Georgia",
    mono="AT",

    # ---------------------------------------------------------------- 01 overview
    correction=2,
    overview=[
        "<b>Austin Theory</b> got to every milestone early. He won his first championship a week "
        "into his career, held the Evolve and WWN titles at the same time at 21, and signed with "
        "WWE in August 2019 at 22. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig pull-fig--sm">24</span>'
        '<span class="pull-cap">his age when he won Money in the Bank on July 2, 2022, the youngest winner of the briefcase</span></span>'
        "By 24 he was Mr. McMahon's on-screen protege, a United States Champion, and the "
        "youngest Money in the Bank winner in WWE history. At 25 he beat John Cena at "
        "WrestleMania 39. The record since then reads like a man WWE keeps returning to: a "
        "WrestleMania XL tag title win with Grayson Waller, an injury and a quiet split in 2025, "
        "and a return under a mask that put him in Paul Heyman's group, The Vision.",

        "The core numbers are specific. He has held the <b>United States Championship twice</b>, "
        "for 75 days in 2022 and 258 days across 2022 and 2023. He has held the WWE Tag Team "
        "Championship once, with Waller, for 90 days. He has held the <b>World Tag Team "
        "Championship twice</b> in 2026, first with Logan Paul for 84 days and then with Bron "
        "Breakker for 124 days. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">5</span>'
        '<span class="pull-cap">WWE title reigns: two US Championships and three tag team championships</span></span>'
        "Add the 2022 Money in the Bank contract and the Evolve, WWN and FIP titles from the "
        "independent years, and that is a full shelf for a wrestler who turned 29 in August 2026.",

        "Two details about him get repeated wrong. The first is that he failed three Money in "
        "the Bank cash-ins. He ran out with the briefcase at SummerSlam and at Clash at the Castle "
        "in 2022, but neither became a match. The only official cash-in came on Raw on November "
        "7, 2022, against United States Champion Seth Rollins, and it failed when Bobby Lashley "
        "pulled him out of the ring. The second is the date of his first title. ESPN's profile "
        "says he first won the United States Championship at Survivor Series 2022. He first won "
        "it from Finn Balor on Raw on April 18, 2022, seven months earlier.",

        "The night that defines him is April 1, 2023. Theory opened WrestleMania 39 against "
        "John Cena, the wrestler he has called an influence, with his US title on the line. "
        "Cena made him tap to the STF while the referee was down. Theory hit a low blow and then "
        "A-Town Down for the pin. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig pull-fig--sm">WM39</span>'
        '<span class="pull-cap">Theory pinned John Cena on April 1, 2023, opening the show</span></span>'
        "As of November 9, 2026, he is on Raw as a member of The Vision. He and Breakker lost "
        "the World Tag Team Championship to Penta and Je'Von Evans at Crown Jewel in Riyadh on "
        "November 7, 2026, when Evans pinned him with the OG Cutter.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Highlight set",
        promo_order=["WWE", "IND"],
        promo_labels={"WWE": "WWE &amp; NXT", "IND": "Indies (Evolve, WWN)"},
        stats=[
            ("2&times;", "US titles"),
            ("3&times;", "Tag titles"),
            ("2022",     "Money in the Bank"),
            ("WM39",     "Beat John Cena"),
            ("2&times;", "WWN titles"),
            ("2016",     "Pro debut"),
        ],
        lead=("Thirty-eight documented bouts from his 2016 debut to Crown Jewel 2026. This is a "
              "highlight set, not a career count, and no career win&ndash;loss total is printed "
              "because none was verified. Every title change he was part of is here, along with "
              "his WWE debut, his WrestleMania matches, and the Money in the Bank night. Filter "
              "by promotion or match type, tap any column to sort, and turn spoilers on to see "
              "results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("2&times;", "US Championship reigns"),
            ("333",      "Days as US Champion"),
            ("3&times;", "WWE tag title reigns"),
            ("2022",     "Money in the Bank"),
        ],
        lead=("Five WWE title reigns and one briefcase, on top of the independent gold he "
              "collected between 18 and 21."),
        rows=[
            dict(ic="US", name="WWE United States Championship", count="2",
                 sub="Won from Finn Balor on Raw, April 18, 2022; lost to Bobby Lashley at Money "
                     "in the Bank, July 2, 2022 (75 days) &middot; won a triple threat over Seth "
                     "Rollins and Lashley at Survivor Series WarGames, November 26, 2022; beat "
                     "John Cena at WrestleMania 39; lost to Rey Mysterio on SmackDown, August 11, "
                     "2023 (<b>258 days</b>)"),
            dict(ic="WT", name="World Tag Team Championship", count="2",
                 sub="With Logan Paul: won a Street Fight over The Usos on Raw, March 30, 2026; "
                     "lost to The Street Profits on June 22, 2026 with Bron Breakker in for the "
                     "injured Paul (84 days) &middot; with Breakker: regained on Raw, July 6, "
                     "2026; lost to Penta and Je&rsquo;Von Evans at Crown Jewel, November 7, "
                     "2026 (124 days)"),
            dict(ic="TT", name="WWE Tag Team Championship", count="1",
                 sub="With Grayson Waller as A-Town Down Under: won the SmackDown belts in the "
                     "WrestleMania XL six-pack ladder match, April 6, 2024 (renamed the WWE Tag "
                     "Team Championship that month); lost to #DIY, July 5, 2024 (90 days)"),
            dict(ic="MB", name="Men's Money in the Bank", count="1",
                 sub="July 2, 2022, MGM Grand Garden Arena &middot; the unannounced eighth "
                     "entrant, youngest winner at 24 years 11 months &middot; official cash-in "
                     "failed against Seth Rollins on Raw, November 7, 2022"),
            dict(ic="EV", name="Evolve Championship", count="1",
                 sub="Won from Fabian Aichner in a triple threat with Roderick Strong at Evolve "
                     "117, December 15, 2018; lost to Josh Briggs at Evolve 139, November 9, 2019"),
            dict(ic="WN", name="WWN Championship", count="2",
                 sub="Won from Keith Lee, April 6, 2018; lost to Joey Janela, June 23, 2018 "
                     "&middot; won from JD Drake at Evolve&rsquo;s 10th Anniversary show, July "
                     "13, 2019"),
            dict(ic="FP", name="FIP World Heavyweight Championship", count="1",
                 sub="Won from Fred Yehi at Evolve 97, December 10, 2017; lost to Anthony Henry, "
                     "September 30, 2018"),
            dict(ic="GA", name="Georgia and regional titles", count="6",
                 sub="WWA4 Heavyweight (won from his trainer AR Fox, May 5, 2016) &middot; The "
                     "Crash Heavyweight (March 2 to May 4, 2019) &middot; MLA Global &middot; PWA "
                     "Heritage &middot; XWA Heavyweight, one reign each, per Wikipedia"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Three groups, each a step up the card.",
        cards=[
            dict(era="NXT &middot; 2020&ndash;21",
                 name="The Way",
                 members="Johnny Gargano, Candice LeRae, Indi Hartwell, Austin Theory",
                 desc="He helped Gargano win the North American Championship at TakeOver: "
                      "WarGames on December 6, 2020 and was revealed as a member three days later. "
                      "The Way was NXT's sitcom heel family, and Theory played the eager apprentice. "
                      "His last NXT match was a loss to Kyle O'Reilly on July 20, 2021."),
            dict(era="SmackDown &amp; Raw &middot; 2023&ndash;25",
                 name="A-Town Down Under",
                 members="Austin Theory, Grayson Waller",
                 desc="Atlanta and Australia, formed after the 2023 Draft. They won a March 2024 "
                      "tournament, then the SmackDown Tag Team Championship in the WrestleMania XL "
                      "six-pack ladder match on April 6, 2024, and held it 90 days until #DIY took "
                      "it on July 5. Waller quietly ended the team on Raw on July 21, 2025, "
                      "announcing that Theory was injured, and joined The New Day."),
            dict(era="Raw &middot; 2025&ndash;present",
                 name="The Vision",
                 members="Paul Heyman, Bron Breakker, Bronson Reed, Logan Paul, Austin Theory",
                 desc="Seth Rollins founded the group with Heyman in 2025 and was thrown out of it "
                      "in October, before Theory arrived. He joined under a hood, superkicking and stomping CM Punk to help The Vision "
                      "win the men's WarGames match on November 29, 2025. He unmasked on Raw on "
                      "December 15 with a shaved head. Heyman's group has given him two World Tag "
                      "Team Championships in 2026, and Maxxine Dupri sided with him in July."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One name, mostly. Five different jobs underneath it.",
        cards=[
            dict(mono="EV", era="Indies &middot; 2016&ndash;19", name="The prodigy",
                 desc="Trained by AR Fox at the WWA4 school in Atlanta. Debuted in April 2016, "
                      "won his first title in May, and by July 2019 held the Evolve and WWN titles "
                      "together, wrestling NXT names like Adam Cole and Johnny Gargano under the "
                      "WWE and Evolve partnership."),
            dict(mono="AP", era="NXT &middot; 2020&ndash;21", name="The apprentice",
                 desc="Gargano's protege in The Way, with a brief 2020 main-roster call-up that "
                      "included a WrestleMania 36 tag title match alongside Angel Garza."),
            dict(mono="TH", era="Raw &middot; 2021&ndash;22", name="Mr. McMahon's protege",
                 desc="Stole the Cleopatra's Egg, took selfies with opponents mid-match, lost to "
                      "Pat McAfee at WrestleMania 38 and ate a Stunner for it. Billed as just "
                      "Theory for part of 2022, the year he won the US title and the briefcase."),
            dict(mono="US", era="Raw &amp; SmackDown &middot; 2022&ndash;23", name="The champion heel",
                 desc="The 258-day US Champion who survived an Elimination Chamber, beat Edge on "
                      "Raw, and pinned John Cena at WrestleMania 39 with a low blow behind the "
                      "referee's back."),
            dict(mono="VI", era="Raw &middot; 2025&ndash;present", name="The masked man",
                 desc="After a 2025 injury took him off the active roster, he came back hooded at "
                      "WarGames, unmasked with a shaved head, and became The Vision's tag "
                      "specialist."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="A ten-year career with a title, a briefcase or a WrestleMania in almost every year.",
        rows=[
            dict(year="2016", title="Debut and first title",
                 desc="Debuts April 29 at Glory Pro Wrestling. Wins the WWA4 Heavyweight "
                      "Championship from his trainer AR Fox on May 5."),
            dict(year="2017", title="Evolve",
                 desc="Debuts for Evolve on February 24 at Evolve 78, beating Darby Allin. Wins "
                      "the FIP World Heavyweight Championship from Fred Yehi on December 10."),
            dict(year="2018", title="WWN and Evolve champion",
                 desc="Beats Keith Lee for the WWN Championship on April 6, then takes the Evolve "
                      "Championship from Fabian Aichner on December 15."),
            dict(year="2019", title="Signs with WWE",
                 desc="Wins the WWN title again on July 13 at Evolve's 10th Anniversary show. WWE "
                      "announces his signing on August 14. His NXT TV debut on December 25 is a "
                      "North American title loss to Roderick Strong."),
            dict(year="2020", title="WrestleMania 36 and The Way",
                 desc="Replaces Andrade next to Angel Garza in the Raw Tag title match at "
                      "WrestleMania 36 on April 5 and loses to The Street Profits. Back in NXT, "
                      "he joins The Way in December."),
            dict(year="2021", title="Raw and the egg",
                 desc="Drafted to Raw. On November 22 he is revealed as the man who took Vince "
                      "McMahon's Cleopatra's Egg and gets a WWE Championship match with Big E "
                      "that night, which he loses."),
            dict(year="2022", title="US title and Money in the Bank",
                 desc="Loses to Pat McAfee at WrestleMania 38. Beats Finn Balor for the US title "
                      "on April 18, loses it to Bobby Lashley on July 2, then wins Money in the Bank "
                      "the same night. His cash-in fails on November 7. He wins the US title back "
                      "at Survivor Series WarGames on November 26."),
            dict(year="2023", title="WrestleMania 39",
                 desc="Retains in the Elimination Chamber, then pins John Cena at WrestleMania 39 "
                      "on April 1. Rey Mysterio ends the 258-day reign on August 11. A-Town Down "
                      "Under debuts on September 1."),
            dict(year="2024", title="Tag champions",
                 desc="Wins the SmackDown Tag Team Championship with Grayson Waller in the "
                      "WrestleMania XL ladder match on April 6. Loses it to #DIY on July 5."),
            dict(year="2025", title="Injury, then the mask",
                 desc="Moves to Raw in January. Waller announces Theory is injured and splits "
                      "the team on July 21. He returns hooded at Survivor Series WarGames on "
                      "November 29 and unmasks on Raw on December 15."),
            dict(year="2026", title="Two tag title reigns",
                 desc="Wins the World Tag Team Championship with Logan Paul on March 30 and loses "
                      "at WrestleMania 42 in a non-title six-man. Drops the belts June 22, "
                      "regains them with Bron Breakker on July 6, and loses them to Penta and "
                      "Je'Von Evans at Crown Jewel on November 7."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="The people on the other side of his biggest nights.",
        cards=[
            dict(name="John Cena", slug="john-cena",
                 desc="The wrestler Theory grew up citing, and the win his WWE career is built on. "
                      "Theory opened WrestleMania 39 on April 1, 2023 by defending the US title "
                      "against Cena, survived a tap-out the referee did not see, and pinned him "
                      "after a low blow and A-Town Down."),
            dict(name="Seth Rollins", slug="seth-rollins",
                 desc="Briefly a 2020 ally, then a recurring obstacle. Rollins beat Theory's "
                      "official Money in the Bank cash-in on November 7, 2022, lost the US title "
                      "to him nineteen days later, and in June 2026 hit him with brass knuckles to "
                      "cost The Vision the World Tag Team Championship."),
            dict(name="Bobby Lashley", slug="bobby-lashley",
                 desc="Took the first US title from Theory with the Hurt Lock at Money in the Bank "
                      "2022, then wrecked his cash-in that November. Theory beat him in the "
                      "Survivor Series triple threat, a No DQ match on Raw in January 2023, and "
                      "the Backlash triple threat that May."),
            dict(name="Rey Mysterio", slug="rey-mysterio",
                 desc="Stepped in for an injured Santos Escobar on SmackDown on August 11, 2023 "
                      "and ended Theory's 258-day US title reign, then beat him again at Payback "
                      "on September 2."),
            dict(name="LA Knight and The Usos", slug="la-knight",
                 desc="The 2026 opponents. Theory and Logan Paul took the World Tag Team "
                      "Championship from The Usos on March 30 after IShowSpeed hit Knight with "
                      "brass knuckles. Knight pinned Theory with the BFT at WrestleMania 42 Night "
                      "1 on April 18, and eliminated him from the 2026 Royal Rumble."),
            dict(name="Penta and Je'Von Evans", slug="penta",
                 desc="The team that ended his second World Tag Team reign. Evans used The "
                      "Vision's own brass knuckles on Theory in a non-title win during the fall, "
                      "then pinned him with the OG Cutter at Crown Jewel on November 7, 2026."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="A wrestler first. The screen credits are small, and the games are steady.",
        rows=[
            dict(when="2016&ndash;17", title="Film extra work", kind="Screen",
                 desc="Extra in Neighbors 2: Sorority Rising (2016) and Spider-Man: Homecoming "
                      "(2017), plus a small role in Fist Fight, "
                      "per Wikipedia."),
            dict(when="2022&ndash;", title="WWE 2K", kind="Game",
                 desc="Playable in WWE 2K22, 2K23, 2K24, 2K25 and 2K26."),
            dict(when="2023&ndash;25", title="The Grayson Waller Effect", kind="TV",
                 desc="Waller's in-ring talk show, with Theory as the regular sidekick, including "
                      "the Elimination Chamber: Perth episode on February 24, 2024 that ended with "
                      "Cody Rhodes and Seth Rollins attacking him."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="What the record supports, with the counting rules attached.",
        stats=[
            ("24",  "Age at Money in the Bank"),
            ("333", "Days as US Champion"),
            ("5",   "WWE title reigns"),
        ],
        rows=[
            dict(name="Youngest Money in the Bank winner in WWE history",
                 sub="24 years and 11 months on July 2, 2022, ahead of Tiffany Stratton at 25. "
                     "He won it as an unannounced eighth entrant, two hours after losing his US "
                     "title in the same building."),
            dict(name="Pinned John Cena at WrestleMania",
                 sub="WrestleMania 39 Night 1, April 1, 2023, in the opening match, retaining the "
                     "United States Championship."),
            dict(name="Lost and won gold on the same night",
                 sub="Money in the Bank 2022: tapped to Bobby Lashley for the US title, then "
                     "climbed the ladder in the main event."),
            dict(name="Two-promotion double champion at 21",
                 sub="After July 13, 2019 he held the Evolve and WWN Championships at once, the "
                     "titles he still held when WWE announced his signing that August."),
            dict(name="First team crowned in the WrestleMania XL tag split",
                 sub="A-Town Down Under won the SmackDown belts first in the April 6, 2024 "
                     "six-pack ladder match, before The Miz and R-Truth took the Raw belts."),
            dict(name="Youngest United States Champion, per ESPN",
                 sub="ESPN's claim, from a profile that also misdates his first US title. It is "
                     "listed as ESPN's claim, not as a verified record."),
        ],
        footnote=("No career win-loss total appears on this page; none was verified. No match "
                  "star ratings appear either, because none was verified from the Wrestling "
                  "Observer or Cagematch."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="X / Twitter", v="@_Theory1", href="https://x.com/_Theory1"),
        dict(k="Instagram", v="@austin_theory", href="https://www.instagram.com/austin_theory/"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/austin-theory"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Austin_Theory"),
        dict(k="WWE.com", v="WrestleMania 39: Theory def. John Cena",
             href="https://www.wwe.com/index%2Ephp/shows/wrestlemania/austin-theory-vs-john-cena-results"),
        dict(k="WWE.com", v="2019 signing announcement",
             href="https://www.wwe.com/shows/wwenxt/article/austin-theory-santana-garrett-headline-wwe-performance-center-class"),
        dict(k="Khel Now", v="Crown Jewel 2026 tag title result",
             href="https://khelnow.com/wwe/wwe-crown-jewel-results-jevon-evans-and-penta-win-tag-team-championship-202611"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/austin-theory.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Austin Theory a champion right now?",
            a="No. He and Bron Breakker lost the World Tag Team Championship to Penta and "
              "Je&rsquo;Von Evans at Crown Jewel in Riyadh on <b>November 7, 2026</b>, ending a "
              "124-day reign. As of November 9, 2026 he is on Raw as a member of Paul Heyman&rsquo;s "
              "group, The Vision.",
            q_ld="Is Austin Theory a WWE champion in November 2026?",
            a_ld="No. Austin Theory and Bron Breakker lost the World Tag Team Championship to Penta "
                 "and Je'Von Evans at WWE Crown Jewel in Riyadh on November 7, 2026, ending a "
                 "124-day reign that began on Raw on July 6, 2026. As of November 9, 2026, Austin "
                 "Theory wrestles on Raw as a member of The Vision."),
        dict(
            q="Did Austin Theory beat John Cena at WrestleMania?",
            a="Yes. At WrestleMania 39 Night 1 on <b>April 1, 2023</b>, Theory retained the United "
              "States Championship against Cena in the opening match. Cena made him tap to the STF, "
              "but the referee was down. Theory hit a low blow and then A-Town Down for the pin.",
            q_ld="Did Austin Theory beat John Cena at WrestleMania 39?",
            a_ld="Yes. Austin Theory defeated John Cena at WrestleMania 39 Night 1 on April 1, 2023 "
                 "to retain the WWE United States Championship. Cena forced Theory to tap to the STF "
                 "while the referee was down, then Theory hit a low blow and his A-Town Down "
                 "finisher for the pinfall."),
        dict(
            q="How many times has Austin Theory been United States Champion?",
            a="Twice. He beat Finn Balor on Raw on April 18, 2022 and lost to Bobby Lashley at "
              "Money in the Bank on July 2, 2022, a 75-day reign. He won it back in a triple "
              "threat over Seth Rollins and Lashley at Survivor Series WarGames on November 26, "
              "2022 and held it <b>258 days</b>, until Rey Mysterio beat him on SmackDown on "
              "August 11, 2023.",
            q_ld="How many times has Austin Theory been WWE United States Champion?",
            a_ld="Austin Theory has been WWE United States Champion twice. His first reign ran "
                 "from April 18, 2022, when he beat Finn Balor on Raw, to July 2, 2022, when he "
                 "lost to Bobby Lashley at Money in the Bank, for 75 days. His second ran from "
                 "Survivor Series WarGames on November 26, 2022 to August 11, 2023, when Rey "
                 "Mysterio beat him on SmackDown, for 258 days."),
        dict(
            q="Did Austin Theory ever cash in Money in the Bank?",
            a="Once, officially, and it failed. He won the briefcase on July 2, 2022, at 24 the "
              "youngest winner ever. He ran out with it at SummerSlam and at Clash at the Castle, "
              "but neither became a match. On Raw on November 7, 2022 he cashed in on United "
              "States Champion Seth Rollins. Bobby Lashley pulled him from the ring, and Rollins "
              "pinned him with the Stomp.",
            q_ld="Did Austin Theory cash in his Money in the Bank contract?",
            a_ld="Austin Theory made one official Money in the Bank cash-in, on Raw on November 7, "
                 "2022, against United States Champion Seth Rollins, and lost after Bobby Lashley "
                 "pulled him out of the ring. Earlier attempts at SummerSlam and Clash at the "
                 "Castle in 2022 never became official matches. He had won the 2022 Money in the "
                 "Bank ladder match on July 2, 2022 at age 24, the youngest winner in WWE history."),
        dict(
            q="What happened to A-Town Down Under?",
            a="Theory and Grayson Waller won the SmackDown Tag Team Championship in the six-pack "
              "ladder match at WrestleMania XL on April 6, 2024 and lost it to #DIY on July 5, "
              "after 90 days. The team moved to Raw in January 2025. On Raw on July 21, 2025, "
              "Waller announced that Theory was injured, ended the team, and joined The New Day.",
            q_ld="What happened to A-Town Down Under, Austin Theory and Grayson Waller's tag team?",
            a_ld="A-Town Down Under, Austin Theory and Grayson Waller, won the SmackDown Tag Team "
                 "Championship at WrestleMania XL on April 6, 2024 and held it for 90 days until "
                 "losing to #DIY on July 5, 2024. The team ended on Raw on July 21, 2025, when "
                 "Waller announced Theory was injured and aligned with The New Day."),
        dict(
            q="Was Austin Theory the masked man who helped The Vision?",
            a="Yes. A hooded figure climbed into the men&rsquo;s WarGames match at Survivor Series "
              "on November 29, 2025 and hit CM Punk with a superkick and a curb stomp, setting up "
              "Bron Breakker&rsquo;s winning spear. On Raw on December 15, 2025, the masked man "
              "unmasked as Theory, with a newly shaved head. Paul Heyman inducted him into The "
              "Vision two weeks later.",
            q_ld="Was Austin Theory the masked man at Survivor Series WarGames 2025?",
            a_ld="Yes. Austin Theory was revealed on Raw on December 15, 2025 as the masked man who "
                 "attacked CM Punk during the men's WarGames match at Survivor Series on November "
                 "29, 2025, helping The Vision win. Paul Heyman then inducted him into The Vision."),
        dict(
            q="What is Austin Theory's real name and where is he from?",
            a="His real name is <b>Austin Tyler White</b>. He was born on August 2, 1997 in "
              "McDonough, Georgia, a suburb of Atlanta. WWE bills him from Atlanta.",
            q_ld="What is Austin Theory's real name?",
            a_ld="Austin Theory's real name is Austin Tyler White. He was born on August 2, 1997 in "
                 "McDonough, Georgia, and WWE bills him from Atlanta, Georgia."),
        dict(
            q="Where did Austin Theory wrestle before WWE?",
            a="Georgia independents first, then Evolve and the WWN family. He trained under AR Fox "
              "at the WWA4 school, debuted in April 2016, and beat Fox for the WWA4 title in May. "
              "He won the FIP World Heavyweight Championship in 2017, the WWN Championship twice, "
              "and the Evolve Championship in December 2018. WWE announced his signing on August "
              "14, 2019, while he held both the Evolve and WWN titles.",
            q_ld="Where did Austin Theory wrestle before WWE?",
            a_ld="Before WWE, Austin Theory trained under AR Fox at the WWA4 Wrestling School in "
                 "Georgia, debuted in 2016, and won titles in WWA4, FIP, WWN and Evolve. He was the "
                 "reigning Evolve and WWN Champion when WWE announced his signing on August 14, "
                 "2019."),
        dict(
            q="What is Austin Theory's finisher?",
            a="<b>A-Town Down</b>, the move WWE.com lists as his signature and the one he used to "
              "pin John Cena at WrestleMania 39. ESPN's 2022 profile called it the ATL, a spinning "
              "cutter.",
            q_ld="What is Austin Theory's finishing move?",
            a_ld="Austin Theory's finishing move is A-Town Down, which WWE.com lists as his "
                 "signature move. He used it to pin John Cena at WrestleMania 39. An earlier ESPN "
                 "profile described it as the ATL, a spinning cutter."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Austin Tyler White"),
        dict(label="Born", value="August 2, 1997", sub="McDonough, Georgia &middot; age 29"),
        dict(label="Billed from", value="Atlanta, Georgia",
             sub="WWE.com and ESPN; real hometown McDonough"),
        dict(label="Height", value="6&#8242;1&#8243;",
             sub="185 cm &middot; billed by ESPN; WWE.com lists none"),
        dict(label="Weight", value="220 lb", sub="100 kg &middot; WWE.com billing"),
        dict(label="Debut", value="April 29, 2016", sub="Glory Pro Wrestling, a three-way loss"),
        dict(label="Trained by", value="AR Fox", sub="WWA4 Wrestling School, then the WWE Performance Center"),
        dict(label="Signed", value="August 14, 2019", sub="WWE announcement, as Evolve and WWN Champion"),
        dict(label="Finisher", value="A-Town Down", sub="listed by WWE.com; ESPN called it the ATL"),
        dict(label="Brand", value="Raw &middot; The Vision", sub="as of November 9, 2026"),
        dict(label="Last match", value="November 7, 2026",
             sub="L with Bron Breakker to Penta &amp; Je&rsquo;Von Evans, Crown Jewel"),
        dict(label="Lifestyle", value="Straight edge", sub="per Wikipedia"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1997-08-02",
    bornplace="McDonough, Georgia, United States",
    nationality="United States",
    height_cm=185,
    weight_kg=100,
    ld=dict(
        alternateName=["Austin Tyler White", "Theory", "The A-Town Kid"],
        award=["WWE United States Championship (2 reigns, 2022-2023)",
               "World Tag Team Championship (2 reigns, 2026, with Logan Paul and Bron Breakker)",
               "WWE Tag Team Championship (1 reign, 2024, with Grayson Waller)",
               "Men's Money in the Bank (2022)",
               "Evolve Championship (1 reign)",
               "WWN Championship (2 reigns)",
               "FIP World Heavyweight Championship (1 reign)"],
        knowsAbout=["Professional wrestling", "WWE", "Tag team wrestling", "Evolve Wrestling"],
        description="Austin Theory is an American professional wrestler signed to WWE, where he "
                    "wrestles on Raw as a member of The Vision. A former Evolve and WWN Champion, "
                    "he won the 2022 Men's Money in the Bank ladder match at 24, held the United "
                    "States Championship twice, defeated John Cena at WrestleMania 39, won the WWE "
                    "Tag Team Championship with Grayson Waller at WrestleMania XL, and held the "
                    "World Tag Team Championship twice in 2026, with Logan Paul and then Bron "
                    "Breakker, until losing it at Crown Jewel on November 7, 2026.",
        sameAs=["https://x.com/_Theory1",
                "https://www.instagram.com/austin_theory/",
                "https://en.wikipedia.org/wiki/Austin_Theory",
                "https://www.wwe.com/superstars/austin-theory"],
    ),
)
