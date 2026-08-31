# -*- coding: utf-8 -*-
"""Sting - dossier data.

Sources: web-verified August 31, 2026 - Wikipedia (main biography plus the Starrcade 1997,
Bound for Glory 2006, Bash at the Beach 1996 and Revolution 2024 event pages) and POST
Wrestling's report on his August 30, 2026 All In: London appearance. Every match row carries
a day-precision date from those sources or the canonical, multiply-documented date of a
major card.

Deliberate omissions:
  * No career win-loss total - none is verifiable across NWA/WCW, TNA, WWE and AEW.
  * His TNA World Championship reigns (four) are summarized without individual dates, which
    were not verified in this pass; only the 2006 NWA title win carries a dated row.
  * The August 30, 2026 All In appearance was a run-in, not a match, so it appears in prose
    and the timeline but not in the record table.
"""

# ----------------------------------------------------------------- record rows
# Twelve documented bouts - the Clash I draw that made him, the Flair bookends, Starrcade '97,
# the WWE cameo years, and the AEW run he left undefeated.
ROWS = [
    dict(result="D", date="1988-03-27", promo="WCW", landmark=True,
         event="Clash of the Champions I — Greensboro", opponent="Ric Flair", opponent_html=True,
         stip="45-minute time-limit draw — the night he arrived", title="NWA World Heavyweight Championship"),
    dict(result="W", date="1990-07-07", promo="WCW", landmark=True,
         event="Great American Bash — Baltimore", opponent="Ric Flair", opponent_html=True,
         stip="Singles — first world championship", title="NWA World Heavyweight Championship"),
    dict(result="W", date="1992-02-29", promo="WCW",
         event="SuperBrawl II — Milwaukee", opponent="Lex Luger",
         stip="Singles — second world title", title="WCW World Heavyweight Championship"),
    dict(result="W", date="1997-12-28", promo="WCW", landmark=True,
         event="Starrcade — Washington, D.C.", opponent="Hollywood Hogan", opponent_html=True,
         stip="Singles — the disputed count, restarted by Bret Hart", title="WCW World Heavyweight Championship"),
    dict(result="W", date="2001-03-26", promo="WCW", landmark=True,
         event="The final Monday Nitro — Panama City", opponent="Ric Flair", opponent_html=True,
         stip="Singles — the last match in WCW history, ending in an embrace", title=""),
    dict(result="W", date="2006-10-22", promo="TNA", landmark=True,
         event="Bound for Glory — Plymouth Township", opponent="Jeff Jarrett",
         stip="Title vs career", title="NWA World Heavyweight Championship"),
    dict(result="L", date="2015-03-29", promo="WWE", landmark=True,
         event="WrestleMania 31 — Levi's Stadium", opponent="Triple H",
         stip="Singles — his WWE in-ring debut, at 55", title=""),
    dict(result="L", date="2015-09-20", promo="WWE",
         event="Night of Champions", opponent="Seth Rollins",
         stip="Singles — his last WWE match; the neck injury", title="WWE World Heavyweight Championship"),
    dict(result="W", date="2021-03-07", promo="AEW", landmark=True, type="tag",
         event="Revolution", opponent="Brian Cage & Ricky Starks",
         stip="Cinematic street fight with Darby Allin — first match in over five years", title=""),
    dict(result="W", date="2024-02-07", promo="AEW", type="tag",
         event="Dynamite", opponent="Ricky Starks & Big Bill",
         stip="Tag with Darby Allin — a champion at 64", title="AEW World Tag Team Championship"),
    dict(result="W", date="2024-03-03", promo="AEW", landmark=True, type="tag",
         event="Revolution — Greensboro", opponent="The Young Bucks",
         stip="Retirement match — tornado tag, Ric Flair in the corner", title="AEW World Tag Team Championship"),
]

# opponent_html rows carry a real <a> so the escaping path is not used on them
for _r in ROWS:
    if _r.pop("opponent_html", False):
        _slug = {"Ric Flair": "ric-flair", "Hollywood Hogan": "hulk-hogan"}[_r["opponent"]]
        _r["opponent"] = '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_slug, _r["opponent"])
        _r["opponent_html"] = True

DATA = dict(
    slug="sting",
    name="Sting",
    realname="Steve Borden",
    epithet="The Icon",
    hook="Record & Legacy",

    meta_desc=("Sting, the Icon and the franchise of WCW, won six WCW World titles, headlined "
               "Starrcade 1997, and retired undefeated in AEW in March 2024 — with a bat-swinging "
               "return at All In: London in August 2026. Full record, titles and career."),
    og_desc=("The Icon: the 45-minute Clash draw that made him, six WCW World Championships, "
             "eighteen months in the rafters before Starrcade 1997, world titles in three "
             "companies, and a retirement at 64 as an undefeated AEW tag champion."),
    tw_desc="Sting: WCW's franchise, world champion in three companies, retired undefeated in AEW.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1985",
    height_imp="6&#8242;2&#8243;",
    weight_lb="250",
    world_titles="6",
    vitals_tagline="It's showtime, folks",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="ST", title="AEW Shop", sub="Official merchandise · Shop AEW",
             tag="Shop", href="https://www.shopaew.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable legend; 2K15 pre-order headliner",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="AEW", title="All Elite Wrestling", sub="AEW.com", tag="Visit", charity=True,
             href="https://www.allelitewrestling.com/"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Icon &middot; The Franchise of WCW &middot; The Stinger",
    hero_tag="Omaha, Nebraska &middot; <em>UWF &middot; NWA/WCW &middot; TNA &middot; WWE &middot; AEW &middot; 1985&ndash;2024</em>",
    now_label="NOW",
    now_bold="Retired &mdash; last match March 3, 2024",
    now_tail=" &middot; went out an undefeated AEW tag champion at 64 &mdash; and returned for one "
             "night at All In: London on August 30, 2026, clearing the ring with the bat as Darby "
             "Allin won back the TNT Championship",
    hstats=[
        dict(value="6",    x=False, label="WCW World Titles"),
        dict(value="4",    x=False, label="TNA World Titles"),
        dict(value="2016", x=True,  label="WWE Hall of Fame"),
        dict(value="0",    x=False, label="AEW Losses"),
    ],
    ghost_link="From the rafters of Nitro to a Wembley run-in at 67",
    vlabel="Est. 1985 &middot; Omaha, Nebraska",
    mono="ST",

    # ---------------------------------------------------------------- 01 overview
    correction=2,
    overview=[
        "<b>Sting</b> is the most loyal main-eventer wrestling has produced &mdash; the one "
        "megastar of the Monday Night War who never worked for Vince McMahon while the war was on. "
        "Born Steve Borden in Omaha on March 20, 1959, trained by Red Bastien and Rick Bassman and "
        "debuting November 25, 1985 alongside the future Ultimate Warrior in a bodybuilders' tag "
        "act, he became a star in one night: March 27, 1988, the first Clash of the Champions, "
        "where an unproven face-painted kid took NWA champion Ric Flair to a 45-minute draw on "
        "free television opposite WrestleMania IV. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">45</span>'
        '<span class="pull-cap">minutes with Ric Flair at Clash of the Champions I &mdash; the draw that made him, on the same night as WrestleMania IV</span></span>'
        "He won his first world title from Flair at the Great American Bash on July 7, 1990, his "
        "sixth and last WCW World Championship in 1999, and world championships in three companies "
        "&mdash; the only man to hold NWA, WCW and TNA world titles. He retired at 64, undefeated "
        "across a four-year AEW run, as one half of the AEW World Tag Team Champions.",

        "The middle of the story is the best long con in wrestling. When the nWo swallowed WCW in "
        "1996, the company's loudest hero went silent: for roughly eighteen months Sting did not "
        "wrestle, repainted the surfer colors into the white-and-black &ldquo;Crow&rdquo; face, and "
        "watched from the rafters with a baseball bat. The payoff &mdash; Starrcade, December 28, "
        "1997, against Hollywood Hogan &mdash; drew the biggest business in WCW history and then "
        "fumbled the ending: referee Nick Patrick counted Hogan's pin at normal speed when the "
        "story demanded a fast count, Bret Hart forced a restart, Sting won by Scorpion Deathlock, "
        "and the championship ended up vacated and rerun at SuperBrawl VIII. The angle remains the "
        "high-water mark of slow-burn booking; the finish remains the cautionary tale about "
        "executing it.",

        "One framing correction this page insists on: Sting was never a WWE guy who arrived late "
        "&mdash; he was the other side's franchise, and the WWE chapter was two matches long. He "
        "stayed with WCW to the literal last match in company history, beating Flair on the final "
        "Nitro on March 26, 2001, then spent a decade as TNA's biggest name, winning the NWA title "
        "in the title-vs-career match against Jeff Jarrett at Bound for Glory on October 22, 2006 "
        "and four TNA World Championships. When he finally appeared in WWE &mdash; Survivor Series "
        "2014, at 55 &mdash; it was as a visiting monument. He lost his WWE in-ring debut to "
        "Triple H at WrestleMania 31 on March 29, 2015 and lost a WWE World Heavyweight "
        "Championship match to Seth Rollins at Night of Champions on September 20, 2015, where a "
        "buckle-bomb neck injury forced what everyone assumed was the end; he went into the WWE "
        "Hall of Fame in 2016 announcing a retirement.",

        "AEW un-retired him and, for once, the epilogue improved the book. He debuted at Winter Is "
        "Coming in December 2020, wrestled his first match in over five years at Revolution on "
        "March 7, 2021 &mdash; a cinematic street fight alongside Darby Allin &mdash; and spent "
        "three years as Allin's tag partner and protector. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">0</span>'
        '<span class="pull-cap">losses in AEW &mdash; he retired as a reigning tag team champion at 64</span></span>'
        "He and Allin won the AEW World Tag Team Championship on the February 7, 2024 Dynamite, "
        "and the retirement match &mdash; Revolution, March 3, 2024, in Greensboro, a tornado tag "
        "against the Young Bucks with Ric Flair in the corner &mdash; ended with a Scorpion "
        "Deathlock submission, the titles retained, and an undefeated AEW record sealed. The coda "
        "came a year and a half later: at All In: London on August 30, 2026, with Allin tied up by "
        "interference in a falls-count-anywhere TNT Championship match, Sting hit the ring at 67 "
        "and cleared it with the bat &mdash; his son Steven Borden diving off a ladder in the same "
        "sequence &mdash; and Allin won the title back. An appearance, not a match: the in-ring "
        "record still ends March 3, 2024.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WCW", "TNA", "WWE", "AEW"],
        promo_labels={"WCW": "NWA/WCW", "TNA": "TNA", "WWE": "WWE", "AEW": "AEW"},
        stats=[
            ("6&times;", "WCW World Champion"),
            ("4&times;", "TNA World Champion"),
            ("1",        "NWA title in TNA"),
            ("45:00",    "The Clash I draw"),
            ("0",        "AEW losses"),
            ("2016",     "WWE Hall of Fame"),
        ],
        lead=("Eleven documented bouts &mdash; the Clash draw, the Flair bookends eleven years "
              "apart, Starrcade '97, both WWE matches, and the AEW farewell run. A curated ledger, "
              "not a career count: no verified win&ndash;loss total exists across four decades and "
              "four companies, and none is published. His four TNA World Championship reigns are "
              "summarized in the titles section without dated rows, because the individual dates "
              "were not verified in this pass. Filter by match type, tap any column header to "
              "sort, and turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the reputation rests on. No Dave Meltzer star rating could be "
                    "verified for these in this pass, so none is shown &mdash; the dashes are "
                    "honesty, not modesty."),
    signature=[
        dict(rating="&mdash;", event="Clash of the Champions I — Greensboro", opponent="Ric Flair",
             stip="NWA World title — the 45-minute draw that made him a main-eventer overnight"),
        dict(rating="&mdash;", event="Great American Bash 1990", opponent="Ric Flair",
             stip="NWA World title — the crowning"),
        dict(rating="&mdash;", event="Starrcade 1997", opponent="Hollywood Hogan",
             stip="WCW World title — eighteen months of rafters, one botched count"),
        dict(rating="&mdash;", event="Revolution 2024 — Greensboro", opponent="The Young Bucks",
             stip="AEW World Tag Team titles — the retirement match, won"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("6&times;", "WCW World Heavyweight"),
            ("4&times;", "TNA World Heavyweight"),
            ("2&times;", "NWA World (incl. 2006)"),
            ("1",        "AEW World Tag Team"),
        ],
        lead=("World championships in three companies &mdash; a distinction no one else holds "
              "&mdash; plus the AEW tag title he retired holding. The counts follow Wikipedia's "
              "summary; individual reign dates beyond the dated rows below were not verified in "
              "this pass and are not invented."),
        rows=[
            dict(ic="C", name="WCW World Heavyweight Championship", count="6",
                 sub="First won July 7, 1990 from Ric Flair at the Great American Bash (as the NWA "
                     "World title, the lineage WCW's belt continued); the Starrcade 1997 win over "
                     "Hollywood Hogan was vacated amid the count controversy and regained at "
                     "SuperBrawl VIII; sixth reign came in 1999"),
            dict(ic="T", name="TNA World Heavyweight Championship", count="4",
                 sub="The company&rsquo;s flagship title, held four times across 2007&ndash;2011 "
                     "&middot; individual reign dates not verified in this pass"),
            dict(ic="N", name="NWA World Heavyweight Championship (TNA era)", count="1",
                 sub="Won from Jeff Jarrett at Bound for Glory, October 22, 2006, title vs career "
                     "&mdash; making him the only man with NWA, WCW and TNA world championships"),
            dict(ic="A", name="AEW World Tag Team Championship", count="1",
                 sub="Won with Darby Allin from Ricky Starks and Big Bill on the February 7, 2024 "
                     "Dynamite, at 64; retained against the Young Bucks in the March 3, 2024 "
                     "retirement match and retired as champion"),
            dict(ic="I", name="WCW International World Heavyweight Championship", count="2",
                 sub="The &ldquo;big gold belt&rdquo; spinoff title of 1993&ndash;94 &middot; reign "
                     "dates not verified in this pass"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Alliances",
        lead="Mostly a loner by design &mdash; the bat, the rafters &mdash; but three alliances "
             "frame the career.",
        cards=[
            dict(era="WCW &middot; 1998",
                 name="nWo Wolfpac",
                 members="Sting, Kevin Nash, Randy Savage, Lex Luger, Konnan",
                 desc="After eighteen months of fighting the nWo alone, he joined its red-and-black "
                      "splinter — face paint recolored to match. A strange chapter for the "
                      "company's designated conscience, and short-lived; the black-and-white Crow "
                      "look returned within the year."),
            dict(era="TNA &middot; 2008&ndash;2009",
                 name="The Main Event Mafia",
                 members="Sting, Kurt Angle, Kevin Nash, Booker T, Scott Steiner",
                 desc="The veterans' heel faction of world champions, formed while he held the TNA "
                      "World title — the rare extended heel run of his career, played as wounded "
                      "pride rather than villainy."),
            dict(era="AEW &middot; 2020&ndash;2024",
                 name="Sting &amp; Darby Allin",
                 members="Sting, Darby Allin",
                 desc="Not a faction — a succession. The face-painted daredevil half his age drew "
                      "him back to the ring; they went unbeaten as a team, took the AEW World Tag "
                      "Team titles on February 7, 2024, and retired him as champion a month later. "
                      "The August 30, 2026 All In run-in — bat in hand, his son Steven diving off "
                      "a ladder — was this alliance's encore."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Two faces, painted over one man: <b>Surfer Sting</b> (1985&ndash;1996) &rarr; "
             "<b>Crow Sting</b> (1996&ndash;present), with a Joker-inflected detour in TNA. The "
             "silence was as deliberate as the paint.",
        cards=[
            dict(mono="PT", era="California &amp; UWF &middot; 1985&ndash;1987", name="Power Team USA to the Blade Runners",
                 desc="A bodybuilder recruited by Rick Bassman alongside Jim Hellwig — the future "
                      "Ultimate Warrior — then half of the Blade Runners tag act in Bill Watts' "
                      "UWF. Hellwig left; Borden stayed, kept the name Sting, and learned to "
                      "work."),
            dict(mono="SS", era="NWA/WCW &middot; 1987&ndash;1996", name="Surfer Sting",
                 desc="Neon paint, flat-top, pointed to the rafters — the promotion's homegrown "
                      "answer to Hulk Hogan without the defection. The Clash I draw with Flair, "
                      "the 1990 title win and five more world reigns belong to this face."),
            dict(mono="CS", era="WCW &middot; 1996&ndash;2001", name="Crow Sting",
                 desc="Inspired directly by the 1994 film The Crow: white face, black trench coat, "
                      "baseball bat, and eighteen months without a word while the nWo ran the "
                      "company. The most successful character reinvention of the era, paid off "
                      "and half-squandered at Starrcade 1997."),
            dict(mono="JS", era="TNA &amp; after &middot; 2011&ndash;2024", name="Joker Sting, then the Icon",
                 desc="TNA's unhinged, grinning variant borrowed from Heath Ledger's Joker gave "
                      "the character a third act; WWE and AEW got the composed elder version. The "
                      "AEW farewell run played every face he ever wore back to the crowd, "
                      "including one last rafters entrance."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="From a Gold's Gym recruitment to a Wembley run-in, four decades later.",
        rows=[
            dict(year="1985", title="Debut",
                 desc="Debuts November 25, 1985, trained by Red Bastien and Rick Bassman, "
                      "alongside Jim Hellwig — the future Ultimate Warrior — in Power Team USA."),
            dict(year="1988", title="Made in 45 minutes",
                 desc="Draws NWA champion Ric Flair at the first Clash of the Champions on March "
                      "27, live on TBS against WrestleMania IV. An audition becomes a coronation."),
            dict(year="1990", title="First world championship",
                 desc="Beats Flair for the NWA World title at the Great American Bash on July 7."),
            dict(year="1996", title="Into the rafters",
                 desc="Falsely accused of joining the nWo, he goes silent, adopts the Crow look, "
                      "and spends about eighteen months watching Nitro from the ceiling with a "
                      "bat."),
            dict(year="1997", title="Starrcade",
                 desc="Beats Hollywood Hogan on December 28 in WCW's biggest-ever main event — "
                      "through a restart forced by Bret Hart after the infamous ordinary-speed "
                      "'fast count.' The title is vacated and regained at SuperBrawl VIII."),
            dict(year="2001", title="The last match in WCW history",
                 desc="Beats Ric Flair on the final Nitro, March 26 — the two embrace, and the "
                      "company ends. He declines to go to the buyer."),
            dict(year="2006", title="Vindicated in TNA",
                 desc="Wins the NWA World title from Jeff Jarrett, title vs career, at Bound for "
                      "Glory on October 22 — then four TNA World Championship reigns through "
                      "2011."),
            dict(year="2014", title="WWE, finally",
                 desc="Appears at Survivor Series on November 23, at 55 — the first time he has "
                      "ever stood in a WWE ring."),
            dict(year="2015", title="Two matches and a broken neck",
                 desc="Loses his in-ring WWE debut to Triple H at WrestleMania 31 on March 29, "
                      "and a title match to Seth Rollins at Night of Champions on September 20, "
                      "where a buckle bomb injures his neck. Hall of Fame and a retirement "
                      "announcement follow in 2016."),
            dict(year="2020", title="AEW un-retires him",
                 desc="Debuts at Winter Is Coming on December 2; at Revolution on March 7, 2021 "
                      "he wrestles his first match in over five years, a cinematic street fight "
                      "with Darby Allin against Team Taz."),
            dict(year="2024", title="Out undefeated, and a champion",
                 desc="Wins the AEW World Tag Team titles with Allin on the February 7 Dynamite, "
                      "then retains them in the retirement match against the Young Bucks at "
                      "Revolution on March 3, in Greensboro, with Flair in the corner. Undefeated "
                      "in AEW, out at 64."),
            dict(year="2026", title="One more swing of the bat",
                 desc="At All In: London on August 30, he storms the ring at 67 to clear the "
                      "interference from Darby Allin's falls-count-anywhere TNT title match — his "
                      "son Steven Borden joins in — and Allin leaves champion. An appearance, not "
                      "a comeback."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Ric Flair", slug="ric-flair",
                 desc="The career-long axis: the 1988 Clash draw that made him, the 1990 Great "
                      "American Bash title change, and the final Nitro on March 26, 2001, when "
                      "WCW's last match ended with the two embracing. Flair stood in his corner "
                      "at the 2024 retirement match — the rivalry literally opened and closed the "
                      "career."),
            dict(name="Hollywood Hogan", slug="hulk-hogan",
                 desc="Eighteen months of silence in the rafters against the nWo's frontman, paid "
                      "off at Starrcade on December 28, 1997 — the biggest gate in WCW history "
                      "and the most litigated finish of the era. Sting also beat Hogan at TNA's "
                      "Bound for Glory in 2011, in what became Hogan's last singles match."),
            dict(name="The nWo",
                 desc="Less a rivalry with a man than with an occupation. The faction's takeover "
                      "turned WCW's brightest act into a silent vigilante, and the imagery it "
                      "produced — the bat, the trench coat, the descent from the ceiling — "
                      "outlived every member of the group."),
            dict(name="Jeff Jarrett",
                 desc="TNA's founding champion and authority heel, against whom Sting's arrival "
                      "legitimized the young company — settled title vs career at Bound for "
                      "Glory on October 22, 2006, with Sting taking the NWA World title."),
            dict(name="Seth Rollins",
                 desc="One match, with consequences: Night of Champions, September 20, 2015, for "
                      "the WWE World Heavyweight Championship. A buckle bomb compressed his neck "
                      "mid-match, he finished it anyway, and the injury ended the WWE chapter and "
                      "&mdash; everyone believed &mdash; the career."),
            dict(name="The Young Bucks",
                 desc="The final program: the Bucks turned on the AEW establishment, put Sting "
                      "and Allin's tag titles in their sights, and lost the tornado tag at "
                      "Revolution on March 3, 2024 — Matthew Jackson tapping to the Scorpion "
                      "Deathlock in Sting's last match."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Legacy",
        lead="Sparser than his stature suggests — he mostly let the character do the talking, "
             "often literally silently.",
        rows=[
            dict(when="1994&ndash;", title="The Crow (influence)", kind="Persona",
                 desc="The 1996 reinvention is directly modeled on the Brandon Lee film — the "
                      "rare case of a movie aesthetic becoming a wrestling character bigger than "
                      "the movie's own sequels."),
            dict(when="2014", title="WWE 2K15", kind="Game",
                 desc="His WWE video-game debut, as the pre-order headliner — before he had ever "
                      "wrestled a WWE match. Playable across the 2K series since."),
            dict(when="2016", title="WWE Hall of Fame", kind="Honor",
                 desc="Inducted April 2, 2016, using the ceremony to announce his (first) "
                      "retirement."),
            dict(when="2021&ndash;2024", title="&ldquo;Seek &amp; Destroy&rdquo;", kind="Music",
                 desc="Entered to Metallica in AEW — one of the few licensed-music entrances in "
                      "the company, and the sound of the farewell run."),
            dict(when="2004&ndash;", title="Faith ministry &amp; Moment of Truth", kind="Life",
                 desc="A born-again Christian since 1998, he has spoken openly about addiction "
                      "and recovery; the 2004 film Sting: Moment of Truth dramatized it."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records and the framing the sources support.",
        stats=[
            ("3",  "Companies' world titles"),
            ("6",  "WCW World reigns"),
            ("0",  "AEW losses"),
        ],
        rows=[
            dict(name="The only man to win NWA, WCW and TNA world championships",
                 sub="Six WCW World Heavyweight reigns, the 2006 NWA World title won at Bound for "
                     "Glory, and four TNA World Heavyweight reigns — per Wikipedia's summary of "
                     "his title history."),
            dict(name="Retired undefeated in AEW, as a champion",
                 sub="Every match of the 2020-2024 AEW run was a win, and the last one — March 3, "
                     "2024, at Revolution in Greensboro — was a successful AEW World Tag Team "
                     "Championship defense with Darby Allin against the Young Bucks. He was 64."),
            dict(name="Never wrestled for the WWF/WWE while WCW existed",
                 sub="The defining loyalty in the industry's defining war. He stayed through the "
                     "final Nitro on March 26, 2001 — winning the last match in WCW history — and "
                     "did not appear in a WWE ring until Survivor Series 2014, at 55."),
            dict(name="The Clash I draw, opposite WrestleMania IV",
                 sub="March 27, 1988: 45 minutes with NWA champion Ric Flair, free on TBS, "
                     "counter-programmed against WrestleMania IV — the single best-leveraged "
                     "star-making match of the era."),
            dict(name="Starrcade 1997 drew WCW's biggest business",
                 sub="The Hogan match on December 28, 1997 headlined the company's most successful "
                     "pay-per-view — the payoff of an eighteen-month tease conducted without "
                     "speaking. The botched count and vacated title that followed are inseparable "
                     "from the achievement."),
            dict(name="A champion at 64",
                 sub="The AEW World Tag Team Championship win with Darby Allin on February 7, "
                     "2024 made him one of the oldest champions in major-promotion history — and "
                     "he never lost the belts; he retired holding them."),
            dict(name="The 2026 All In return",
                 sub="August 30, 2026, Wembley Stadium: two and a half years into retirement, at "
                     "67, he cleared the ring with the bat during Darby Allin's TNT Championship "
                     "win over Kevin Knight — with his son Steven Borden diving off a ladder in "
                     "the same rescue (POST Wrestling). An appearance, not a match; the record "
                     "stands closed."),
        ],
        footnote=("No career win-loss total is published — none can be verified across NWA/WCW, "
                  "TNA, WWE and AEW. TNA-era reign dates beyond Bound for Glory 2006 were not "
                  "verified in this pass and are stated as counts only. And the AEW undefeated "
                  "streak is stated without a matches number, because the exact count was not "
                  "verified here; 'every AEW match a win' is the claim the sources support."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Sting_(wrestler)"),
        dict(k="Wikipedia", v="Revolution 2024 — the retirement match",
             href="https://en.wikipedia.org/wiki/Revolution_(2024)"),
        dict(k="POST Wrestling", v="All In 2026: the bat comes out for Darby Allin",
             href="https://www.postwrestling.com/2026/08/30/darby-allin-with-help-from-sting-takes-tnt-title-off-kevin-knight-at-aew-all-in-2026/"),
        dict(k="Wikipedia", v="Starrcade 1997 — the disputed finish",
             href="https://en.wikipedia.org/wiki/Starrcade_(1997)"),
        dict(k="Wikipedia", v="Bound for Glory 2006 — title vs career",
             href="https://en.wikipedia.org/wiki/Bound_for_Glory_(2006)"),
        dict(k="Wikipedia", v="Bash at the Beach 1996 — the night the nWo formed around him",
             href="https://en.wikipedia.org/wiki/Bash_at_the_Beach_(1996)"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Sting retired &mdash; and what was that at All In: London?",
            a="He is retired. His last match was the winning tornado-tag title defense with Darby "
              "Allin against the Young Bucks at AEW Revolution on <b>March 3, 2024</b>, after "
              "which he retired undefeated in AEW and still champion, at 64. What happened at All "
              "In: London on <b>August 30, 2026</b> was a run-in, not a match: with Allin's "
              "falls-count-anywhere TNT Championship match against Kevin Knight overrun by "
              "interference, Sting hit the ring with the bat and cleared it &mdash; his son "
              "Steven Borden dove off a ladder in the same rescue &mdash; and Allin won the "
              "title. The in-ring record remains closed.",
            q_ld="Is Sting retired, and what did he do at AEW All In: London in August 2026?",
            a_ld="Sting is retired from wrestling. His final match was on March 3, 2024 at AEW "
                 "Revolution, where he and Darby Allin retained the AEW World Tag Team "
                 "Championship against the Young Bucks; he retired undefeated in AEW at age 64. "
                 "On August 30, 2026, at AEW All In: London at Wembley Stadium, he made a "
                 "one-night surprise return — not a match — using his baseball bat to clear "
                 "interference during Darby Allin's falls-count-anywhere TNT Championship match "
                 "against Kevin Knight, which Allin won. Sting's son Steven Borden also assisted."),
        dict(
            q="How many world titles did Sting win?",
            a="Eleven across three companies, by Wikipedia's summary: <b>six WCW World "
              "Heavyweight Championships</b> (the first won from Ric Flair at the Great American "
              "Bash on July 7, 1990, under the NWA lineage), <b>one NWA World Championship</b> in "
              "TNA (from Jeff Jarrett, title vs career, at Bound for Glory on October 22, 2006) "
              "and <b>four TNA World Heavyweight Championships</b>. He is the only man to hold "
              "NWA, WCW and TNA world titles. He never won a WWE championship &mdash; he had "
              "only two WWE matches, and lost both.",
            q_ld="How many world championships did Sting win?",
            a_ld="Sting won eleven world championships across three companies: six WCW World "
                 "Heavyweight Championships, one NWA World Heavyweight Championship won in TNA "
                 "from Jeff Jarrett at Bound for Glory on October 22, 2006, and four TNA World "
                 "Heavyweight Championships. He is the only wrestler to win NWA, WCW and TNA "
                 "world titles. He never held a WWE championship, losing both of the WWE matches "
                 "he wrestled in 2015."),
        dict(
            q="What actually happened at Starrcade 1997?",
            a="The angle of the decade met the finish of a lifetime, in the bad sense. After "
              "eighteen months of Sting haunting the rafters, he met Hollywood Hogan for the WCW "
              "title on December 28, 1997. The planned story was a Montreal-style fast count on "
              "Sting that Bret Hart would overturn &mdash; but referee Nick Patrick's count came "
              "in at ordinary speed. Hart forced the restart anyway, Sting won with the Scorpion "
              "Deathlock, and the championship was later vacated and settled at SuperBrawl VIII, "
              "which Sting won. Biggest business in company history; most second-guessed finish "
              "in company history.",
            q_ld="What happened in the Sting versus Hollywood Hogan match at Starrcade 1997?",
            a_ld="At Starrcade on December 28, 1997, Sting faced Hollywood Hogan for the WCW World "
                 "Heavyweight Championship after an eighteen-month buildup. Referee Nick Patrick "
                 "counted a Hogan pinfall that was scripted to be a fast count but was delivered "
                 "at normal speed; Bret Hart then restarted the match, and Sting won by Scorpion "
                 "Deathlock. Because of the controversy the title was later vacated, and Sting "
                 "won it back at SuperBrawl VIII in February 1998. The event drew the largest "
                 "business in WCW history."),
        dict(
            q="Why did Sting never go to WWF during the Monday Night War?",
            a="Loyalty, deliberately chosen and repeatedly re-chosen &mdash; he re-signed with "
              "WCW at every point when jumping would have been the obvious move, and he has said "
              "he did not trust how the WWF machine would handle the character. The result is "
              "unique: the biggest star of the war's losing side never appeared for the winner "
              "until Survivor Series 2014, thirteen years after WCW died &mdash; and by then the "
              "abstention itself had become the legend.",
            q_ld="Why did Sting never wrestle for WWF during the Monday Night War?",
            a_ld="Sting chose to remain with WCW for the entirety of the Monday Night War, "
                 "re-signing rather than jumping to the WWF, and he has said he doubted the WWF "
                 "would present his character well. He wrestled in the last match in WCW history "
                 "on the final Nitro on March 26, 2001, and did not appear in a WWE ring until "
                 "Survivor Series on November 23, 2014, thirteen years after WCW closed."),
        dict(
            q="What ended Sting&rsquo;s WWE run in 2015?",
            a="A neck injury in his second and final WWE match. Challenging Seth Rollins for the "
              "WWE World Heavyweight Championship at Night of Champions on September 20, 2015, "
              "he took a buckle bomb that compressed his neck; he finished the match but the "
              "damage &mdash; at 56 &mdash; was enough that he announced his retirement at his "
              "2016 Hall of Fame induction. The AEW years later proved the retirement premature "
              "by exactly one glorious epilogue.",
            q_ld="What injury ended Sting's WWE career in 2015?",
            a_ld="Sting suffered a neck injury during his WWE World Heavyweight Championship "
                 "match against Seth Rollins at Night of Champions on September 20, 2015, when a "
                 "buckle bomb compressed his neck. He completed the match but never wrestled in "
                 "WWE again, and he announced his retirement at his WWE Hall of Fame induction "
                 "in April 2016. He later returned to wrestling with AEW from 2020 to 2024."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Steve Borden"),
        dict(label="Born", value="March 20, 1959", sub="Omaha, Nebraska &middot; age 67"),
        dict(label="Billed from", value="Venice Beach, California"),
        dict(label="Height", value="6&#8242;2&#8243;", sub="188 cm"),
        dict(label="Weight", value="250 lb", sub="113 kg (billed)"),
        dict(label="Debut", value="November 25, 1985", sub="via Power Team USA, with Jim Hellwig"),
        dict(label="Trained by", value="Red Bastien &amp; Rick Bassman"),
        dict(label="Last match", value="March 3, 2024",
             sub="Revolution, Greensboro &mdash; won, retaining the AEW tag titles at 64"),
        dict(label="Ring names", value="Flash Borden &rarr; Blade Runner Sting &rarr; Sting"),
        dict(label="Signature", value="Scorpion Deathlock &middot; Scorpion Death Drop &middot; Stinger Splash",
             sub="and the baseball bat, which is not a move but might as well be"),
        dict(label="Entrance theme", value="&ldquo;Seek &amp; Destroy&rdquo;",
             sub="Metallica, in AEW"),
        dict(label="Hall of Fame", value="WWE, 2016",
             sub="announced his first retirement from the podium"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1959-03-20",
    bornplace="Omaha, Nebraska",
    nationality="United States",
    height_cm=188,
    weight_kg=113,
    ld=dict(
        alternateName=["Steve Borden", "The Icon", "The Stinger", "The Franchise of WCW",
                       "Flash Borden"],
        award=["WCW World Heavyweight Championship (6 reigns)",
               "TNA World Heavyweight Championship (4 reigns)",
               "NWA World Heavyweight Championship (won 2006, in TNA)",
               "WCW International World Heavyweight Championship (2 reigns)",
               "AEW World Tag Team Championship (1 reign, with Darby Allin, retired as champion)",
               "WWE Hall of Fame (2016)"],
        knowsAbout=["Professional wrestling", "WCW", "New World Order", "TNA", "AEW",
                    "Monday Night War", "Starrcade"],
        description="Sting, born Steve Borden in Omaha, Nebraska, is an American retired "
                    "professional wrestler and the only man to win NWA, WCW and TNA world "
                    "championships — six WCW World Heavyweight titles among them. The face of WCW "
                    "throughout the Monday Night War, he headlined Starrcade 1997 against "
                    "Hollywood Hogan after an eighteen-month silent vigil, won the last match in "
                    "WCW history on the final Nitro in 2001, and retired on March 3, 2024 at AEW "
                    "Revolution, undefeated in AEW and a reigning tag team champion with Darby "
                    "Allin at 64. He made a one-night return appearance at All In: London on "
                    "August 30, 2026.",
        sameAs=["https://en.wikipedia.org/wiki/Sting_(wrestler)",
                "https://www.allelitewrestling.com/"],
    ),
)
