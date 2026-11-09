# -*- coding: utf-8 -*-
"""Razor Ramon (Scott Hall) - dossier data.

Built from data/razor-ramon.md (compiled November 9, 2026). Every row carries a
day-precision date from a source listed there. The page title is Razor Ramon, but
it covers Scott Hall's whole career: Florida, the AWA, WCW's Diamond Studd, the WWF
Razor Ramon run, the Kliq, The Outsiders and the nWo, WWF 2002, TNA, and his final
match in 2016.

Memorial page: Hall died March 14, 2022. Present tense is confined to legacy.

Deliberate omissions:
  * No career win-loss total. None is verifiable (Cagematch is JS-gated). The old
    page's "1-5-0" record and finish-method percentages were fabricated and are gone.
  * No walk-out theme band. The Razor Ramon theme's title and a stable listening
    link could not be verified to the standard the band needs.
  * No social links: none can be authenticated for a subject who has died.
  * The May 19, 1996 Madison Square Garden match with Hunter Hearst Helmsley (the
    Curtain Call night) has no row: the result was not verified.
  * Diamond Studd debut date: Wikipedia says SuperBrawl I, but that card does not
    list him, so no debut row is given.
  * Brief premise corrected: "Starship Coyote" was a Florida / Crockett name, not
    an AWA one. In the AWA he was "Magnum" and then "Big" Scott Hall.
  * There is no /matches/ page for WrestleMania X or SummerSlam 1995 on disk, so
    those signature cards stay unlinked. (/matches/ and /rankings/ link to
    /matches/hbk-vs-razor-ramon-wrestlemania-x/ and
    /matches/hbk-vs-razor-ramon-summerslam-1995/, which do not exist.)
"""

ROWS = [
    # ------------------------------------------------------------ territories
    dict(result="W", date="1986-01-18", promo="IND", type="tag", landmark=True,
         event="AWA, Albuquerque", opponent="Jimmy Garvin & Steve Regal",
         stip="Tag with Curt Hennig, his first major championship", title="AWA World Tag Team Championship"),
    dict(result="L", date="1986-05-17", promo="IND", type="tag",
         event="AWA", opponent="Buddy Rose & Doug Somers",
         stip="Tag with Curt Hennig, lost by countout", title="AWA World Tag Team Championship"),
    dict(result="L", date="1989-07-09", promo="WCW",
         event="WCW television", opponent="The Great Muta",
         stip="Singles, his WCW TV debut as Scott Hall", title=""),
    # ------------------------------------------------------------ WWF 1992-1996
    dict(result="W", date="1992-08-08", promo="WWF", landmark=True,
         event="Superstars", opponent="Paul Van Dale",
         stip="Singles, Razor Ramon's TV debut, won with the crucifix powerbomb", title=""),
    dict(result="W", date="1993-04-04", promo="WWF",
         event="WrestleMania IX, Caesars Palace", opponent="Bob Backlund",
         stip="Singles, small package in 3:45", title=""),
    dict(result="W", date="1993-09-27", promo="WWF", landmark=True,
         event="Raw, New Haven", opponent="Rick Martel",
         stip="Battle royal final for the vacant title, first reign", title="WWF Intercontinental Championship"),
    dict(result="W", date="1994-03-20", promo="WWF", landmark=True,
         event="WrestleMania X, Madison Square Garden", opponent="Shawn Michaels",
         stip="Ladder match, both belts hung, unifies the title", title="WWF Intercontinental Championship"),
    dict(result="L", date="1994-04-13", promo="WWF",
         event="Superstars taping, Rochester", opponent="Diesel",
         stip="Singles, Michaels interferes, first reign ends", title="WWF Intercontinental Championship"),
    dict(result="W", date="1994-08-29", promo="WWF", landmark=True,
         event="SummerSlam, United Center", opponent="Diesel",
         stip="Singles, Walter Payton in his corner, second reign", title="WWF Intercontinental Championship"),
    dict(result="W", date="1994-11-23", promo="WWF", type="tag",
         event="Survivor Series, San Antonio", opponent="The Teamsters (Diesel, Shawn Michaels, Owen Hart, Jeff Jarrett, Jim Neidhart)",
         stip="5-on-5 elimination, captain of The Bad Guys and sole survivor", title=""),
    dict(result="L", date="1995-01-22", promo="WWF",
         event="Royal Rumble, Tampa", opponent="Jeff Jarrett",
         stip="Restarted after a countout, pinned on an injured knee", title="WWF Intercontinental Championship"),
    dict(result="W", date="1995-04-02", promo="WWF",
         event="WrestleMania XI, Hartford", opponent="Jeff Jarrett",
         stip="Singles, won by disqualification, title stays with Jarrett", title="WWF Intercontinental Championship"),
    dict(result="W", date="1995-05-19", promo="WWF",
         event="House show, Montreal", opponent="Jeff Jarrett",
         stip="Ladder match, first three-time champion", title="WWF Intercontinental Championship"),
    dict(result="L", date="1995-08-27", promo="WWF", landmark=True,
         event="SummerSlam, Pittsburgh", opponent="Shawn Michaels",
         stip="Ladder match rematch, 25:01", title="WWF Intercontinental Championship"),
    dict(result="W", date="1995-10-22", promo="WWF",
         event="In Your House 4, Winnipeg", opponent="Dean Douglas",
         stip="Surprise match minutes after Douglas won by forfeit, first four-time champion",
         title="WWF Intercontinental Championship"),
    dict(result="L", date="1996-01-21", promo="WWF",
         event="Royal Rumble, Fresno", opponent="Goldust",
         stip="Singles, fourth and final reign ends", title="WWF Intercontinental Championship"),
    # ------------------------------------------------------------ WCW 1996-2000
    dict(result="NC", date="1996-07-07", promo="WCW", landmark=True, type="tag",
         event="Bash at the Beach, Daytona Beach", opponent="Randy Savage, Sting & Lex Luger",
         stip="Six-man with Kevin Nash and the mystery partner, Hulk Hogan. The nWo is born",
         title=""),
    dict(result="W", date="1996-10-27", promo="WCW", landmark=True, type="tag",
         event="Halloween Havoc, Las Vegas", opponent="Harlem Heat (Booker T & Stevie Ray)",
         stip="Tag with Kevin Nash, first Outsiders reign", title="WCW World Tag Team Championship"),
    dict(result="L", date="1997-01-25", promo="WCW", type="tag",
         event="Souled Out, Cedar Rapids", opponent="The Steiner Brothers",
         stip="Tag with Nash, reversed on Nitro two days later", title="WCW World Tag Team Championship"),
    dict(result="L", date="1997-02-23", promo="WCW", type="tag",
         event="SuperBrawl VII, Daly City", opponent="Lex Luger & The Giant",
         stip="Tag with Nash, titles returned the next night", title="WCW World Tag Team Championship"),
    dict(result="L", date="1997-10-13", promo="WCW", type="tag",
         event="Nitro, Tampa", opponent="The Steiner Brothers",
         stip="Tag with Syxx in the injured Nash's place, 231-day reign ends", title="WCW World Tag Team Championship"),
    dict(result="W", date="1997-11-23", promo="WCW", landmark=True, type="tag",
         event="World War 3, Auburn Hills", opponent="59 others, last The Giant",
         stip="60-man three-ring battle royal for a world title shot", title=""),
    dict(result="W", date="1998-01-12", promo="WCW", type="tag",
         event="Nitro, Jacksonville", opponent="The Steiner Brothers",
         stip="Tag with Nash", title="WCW World Tag Team Championship"),
    dict(result="W", date="1998-02-22", promo="WCW", type="tag",
         event="SuperBrawl VIII, Daly City", opponent="The Steiner Brothers",
         stip="Tag with Nash, Scott Steiner turns on Rick", title="WCW World Tag Team Championship"),
    dict(result="L", date="1998-03-15", promo="WCW", landmark=True,
         event="Uncensored, Mobile", opponent="Sting",
         stip="His World War 3 title shot, pinned after the Scorpion Death Drop",
         title="WCW World Heavyweight Championship"),
    dict(result="L", date="1998-05-17", promo="WCW", type="tag",
         event="Slamboree, Worcester", opponent="Sting & The Giant",
         stip="Tag with Nash, Hall hits Nash with a belt and the team splits", title="WCW World Tag Team Championship"),
    dict(result="W", date="1998-07-20", promo="WCW", type="tag",
         event="Nitro, Salt Lake City", opponent="Sting & Kevin Nash",
         stip="Tag with The Giant", title="WCW World Tag Team Championship"),
    dict(result="L", date="1999-01-17", promo="WCW",
         event="Souled Out, Charleston", opponent="Goldberg",
         stip="Stun gun ladder match", title=""),
    dict(result="W", date="1999-02-21", promo="WCW", landmark=True,
         event="SuperBrawl IX, Oakland", opponent="Roddy Piper",
         stip="Singles, first United States title", title="WCW United States Heavyweight Championship"),
    dict(result="W", date="1999-02-21", promo="WCW", type="tag",
         event="SuperBrawl IX, Oakland", opponent="Konnan & Rey Mysterio",
         stip="Hair vs mask, with Nash, in for the injured Lex Luger. Mysterio unmasks", title=""),
    dict(result="W", date="1999-11-08", promo="WCW", type="tag",
         event="Nitro, Indianapolis", opponent="Goldberg, Bret Hart & Sid Vicious",
         stip="Four-way ladder match, second United States title", title="WCW United States Heavyweight Championship"),
    dict(result="W", date="1999-12-13", promo="WCW", type="tag",
         event="Nitro, New Orleans", opponent="Bret Hart & Goldberg",
         stip="Tag with Nash, seventh and final tag reign", title="WCW World Tag Team Championship"),
    dict(result="L", date="2000-02-20", promo="WCW", type="tag",
         event="SuperBrawl 2000, Daly City", opponent="Sid Vicious & Jeff Jarrett",
         stip="Three-way dance, Sid retains. His last WCW match", title="WCW World Heavyweight Championship"),
    # ------------------------------------------------------------ WWF 2002
    dict(result="W", date="2002-03-04", promo="WWF",
         event="Raw", opponent="Spike Dudley",
         stip="Singles, first WWF match since May 1996", title=""),
    dict(result="L", date="2002-03-17", promo="WWF", landmark=True,
         event="WrestleMania X8, SkyDome", opponent="Steve Austin",
         stip="Singles, Nash in his corner. His first WrestleMania loss", title=""),
    # ------------------------------------------------------------ TNA + final match
    dict(result="L", date="2004-12-05", promo="TNA", type="tag",
         event="Turning Point, Orlando", opponent="AJ Styles, Jeff Hardy & Randy Savage",
         stip="Six-man with Jeff Jarrett and Kevin Nash as the Kings of Wrestling", title=""),
    dict(result="L", date="2005-01-16", promo="TNA",
         event="Final Resolution, Orlando", opponent="Jeff Hardy",
         stip="Singles, Roddy Piper as special referee", title=""),
    dict(result="W", date="2010-05-04", promo="TNA", type="tag",
         event="Impact taping (aired May 13)", opponent="Matt Morgan",
         stip="Nash's Feast or Fired cash-in, Eric Young added under the Freebird rule",
         title="TNA World Tag Team Championship"),
    dict(result="W", date="2016-06-17", promo="IND", landmark=True,
         event="F1RST Wrestling, Des Moines", opponent="Chuck Taylor",
         stip="Singles, his final match", title="DDT Ironman Heavymetalweight Championship"),
]

DATA = dict(
    slug="razor-ramon",
    name="Razor Ramon",
    realname="Scott Oliver Hall",
    epithet="The Bad Guy",
    hook="Record & Legacy",
    art="razor-ramon",

    meta_desc=("Razor Ramon, Scott Hall: four-time Intercontinental Champion, winner of the "
               "WrestleMania X ladder match, nWo founder, seven-time WCW tag champion and "
               "two-time WWE Hall of Famer. Died March 14, 2022. Full record and career."),
    og_desc=("Scott Hall's whole career on one page: the Diamond Studd, Razor Ramon's four "
             "Intercontinental reigns and the WrestleMania X ladder match, The Outsiders, the "
             "nWo, and two WWE Hall of Fame inductions. 1958-2022."),
    tw_desc="Razor Ramon, Scott Hall, 1958-2022: the WrestleMania X ladder match, the Outsiders and the nWo.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1984",
    height_imp="6&#8242;7&#8243;",
    weight_lb="287",
    vitals_tagline="Say hello to the Bad Guy",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="RR", title="WWE Shop", sub="Legends merchandise · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable legend in the 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="WWE", title="Alumni Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/razor-ramon"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="The Bad Guy &middot; The Diamond Studd &middot; The Outsider",
    hero_tag="Billed from Miami &middot; <em>AWA &middot; WCW &middot; WWF &middot; nWo &middot; TNA &middot; 1984&ndash;2016</em>",
    now_label="1958&ndash;2022",
    now_bold="Died March 14, 2022, at 63",
    now_tail=(" &middot; complications after hip surgery, Marietta, Georgia &middot; WWE Hall of "
              "Fame 2014, and again with the nWo in 2020"),
    hstats=[
        dict(value="4",    x=True,  label="Intercontinental reigns"),
        dict(value="7",    x=True,  label="WCW World Tag reigns"),
        dict(value="434",  x=False, label="Days as IC Champion"),
        dict(value="2",    x=True,  label="Hall of Fame inductions"),
    ],
    ghost_link="From Florida in 1984 to Des Moines in 2016",
    vlabel="Est. 1984 &middot; St. Mary&rsquo;s County, Maryland",
    mono="RR",

    # ---------------------------------------------------------------- 01 overview
    correction=2,
    overview=[
        "<b>Scott Hall</b> wrestled under several names, and two of them changed the business. As "
        "<b>Razor Ramon</b>, a Miami tough guy built on Tony Montana from <i>Scarface</i>, he "
        "flicked a toothpick at the camera, said &ldquo;Hey, yo,&rdquo; and became the first "
        "man to hold the WWF Intercontinental Championship four times. As plain Scott Hall, he "
        "walked through a Nitro crowd on May 27, 1996 and started the invasion that became the "
        '<a href="/factions/nwo/">nWo</a>. Born October 20, 1958 in St. Mary&rsquo;s County, '
        "Maryland, he debuted in Florida in 1984, won the AWA World Tag Team Championship with "
        "Curt Hennig (Mr. Perfect) in 1986, and worked WCW as The Diamond Studd, managed by "
        "Diamond Dallas Page, before the WWF signed him in 1992.",

        "The Razor run lasted four years. He won the vacant Intercontinental title in a Raw "
        "battle royal in September 1993, and when Shawn Michaels claimed the belt was still his, "
        "WrestleMania X settled it: both belts hung above the ring at Madison Square Garden on "
        "March 20, 1994, and Razor climbed for both. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">434</span>'
        '<span class="pull-cap">days as Intercontinental Champion across four reigns, as WWE counts them</span></span>'
        "Dave Meltzer gave the match five stars, and both the Wrestling Observer and Pro "
        "Wrestling Illustrated named it the 1994 Match of the Year. He won the title back from "
        "Diesel at SummerSlam 1994, again from Jeff Jarrett in May 1995, and a fourth time from "
        "Dean Douglas in October 1995. WWE&rsquo;s title history credits him with 434 days as "
        "champion. Backstage he ran with Michaels, Kevin Nash, Sean Waltman and Triple H as the "
        "Kliq, and the Madison Square Garden Curtain Call on May 19, 1996 was his WWF exit.",

        "One correction, because the old version of this page got it backwards: Razor Ramon "
        "won the WrestleMania X ladder match. Michaels tangled himself in the ropes going for "
        "the belts, and Razor retrieved both to stay the undisputed champion. Michaels won the "
        "rematch, a ladder match at SummerSlam on August 27, 1995. The old page's Triple H "
        "rows from April 1996 and WrestleMania XII had no source and are gone, and so is its "
        "1-5-0 career record. Hall never held a world heavyweight title.",

        "In WCW, Hall and Nash were The Outsiders. At "
        '<a href="/matches/nwo-formation-bash-at-the-beach-1996/">Bash at the Beach on July 7, '
        "1996</a> their mystery partner turned out to be Hulk Hogan, and the match with Randy "
        "Savage, Sting and Lex Luger ended in a no contest and a new faction. The Outsiders won "
        "the WCW World Tag Team Championship six times, starting at Halloween Havoc on October 27, "
        "1996, and Hall added a seventh reign with The Giant. He won the 1997 World War 3 battle "
        "royal, two WCW United States titles and the Television title. At Starrcade 1998 his stun "
        "gun set up the end of Goldberg&rsquo;s streak.",

        "The later years were harder. He came back to the WWF with the nWo in 2002, lost to "
        "Steve Austin at WrestleMania X8, and was released that May. He worked TNA in 2002, "
        "2004&ndash;2005 and 2010, and his last match was in Des Moines on June 17, 2016. His "
        "fight with addiction was public; he moved into Diamond Dallas Page&rsquo;s Atlanta home "
        "during the recovery shown in <i>The Resurrection of Jake the Snake</i>. WWE inducted him "
        "into the Hall of Fame in 2014, Nash giving the speech, and Hall closed with &ldquo;bad "
        "times don&rsquo;t last, but bad guys do.&rdquo; He went in again with the nWo in the 2020 "
        "class. He died on March 14, 2022, at 63, after complications from hip-replacement "
        "surgery, at WellStar Kennestone Hospital in Marietta, Georgia.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWF", "WCW", "TNA", "IND"],
        promo_labels={"WWF": "WWF", "WCW": "WCW", "TNA": "TNA", "IND": "AWA and indies"},
        stats=[
            ("4&times;", "Intercontinental"),
            ("7&times;", "WCW World Tag"),
            ("2&times;", "WCW United States"),
            ("1&times;", "WCW Television"),
            ("5&#9733;", "WrestleMania X"),
            ("1997",     "World War 3 winner"),
        ],
        lead=("Thirty-nine documented bouts, from the 1986 AWA tag title with Curt Hennig to the "
              "2016 match that ended the career. Every Intercontinental title change, every WCW "
              "tag reign we could date to the night, the nWo&rsquo;s first match, and the 2002 "
              "WWF return. This is a curated ledger, not a career count: no "
              "verified win&ndash;loss total exists, and none is estimated. The first IC win and "
              "loss are dated to WWE&rsquo;s title history, which uses taping dates. Filter by "
              "promotion or match type, sort any column, and turn spoilers on to see results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the legacy rests on. Only WrestleMania X carries a verified Dave "
                    "Meltzer rating. A dash means no rating is claimed."),
    signature=[
        dict(rating="5.0", event="WrestleMania X, Madison Square Garden", opponent="Shawn Michaels",
             stip="Ladder match for the undisputed Intercontinental title, 1994 Match of the Year"),
        dict(rating="&mdash;", event="SummerSlam 1994, Chicago", opponent="Diesel",
             stip="Intercontinental title, Walter Payton in his corner"),
        dict(rating="&mdash;", event="SummerSlam 1995, Pittsburgh", opponent="Shawn Michaels",
             stip="The ladder match rematch, 25 minutes"),
        dict(rating="&mdash;", event="Bash at the Beach 1996, Daytona Beach",
             opponent="Randy Savage, Sting and Lex Luger",
             stip="The Outsiders reveal their third man, Hulk Hogan",
             url="/matches/nwo-formation-bash-at-the-beach-1996/"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("4&times;", "Intercontinental"),
            ("7&times;", "WCW World Tag"),
            ("2&times;", "WCW United States"),
            ("434",      "Days as IC Champion"),
        ],
        lead=("Never a world heavyweight champion, and one of the most decorated midcard and tag "
              "champions of the 1990s. Days are as the title histories count them."),
        rows=[
            dict(ic="I", name="WWF Intercontinental Championship", count="4",
                 sub="September 27, 1993, Raw battle royal over Rick Martel (197 days) &middot; "
                     "August 29, 1994, SummerSlam over Diesel (145) &middot; May 19, 1995, ladder "
                     "match over Jeff Jarrett in Montreal (2) &middot; October 22, 1995, In Your House 4 "
                     "over Dean Douglas (90) &middot; unified the belt at WrestleMania X &middot; "
                     "the first three-time and four-time champion"),
            dict(ic="T", name="WCW World Tag Team Championship", count="7",
                 sub="Six with Kevin Nash as The Outsiders, from Halloween Havoc on October 27, 1996 "
                     "to Nitro on December 13, 1999 (Syxx defended in Nash&rsquo;s place in 1997) "
                     "&middot; one with The Giant, July 20, 1998 &middot; 571 combined days"),
            dict(ic="U", name="WCW United States Heavyweight Championship", count="2",
                 sub="February 21, 1999, SuperBrawl IX over Roddy Piper &middot; November 8, 1999, "
                     "four-way ladder match on Nitro &middot; the second ended with a knee injury at "
                     "Starrcade on December 19, 1999"),
            dict(ic="V", name="WCW World Television Championship", count="1",
                 sub="November 21, 1999, Mayhem, after Rick Steiner forfeited &middot; abandoned "
                     "eight days later when Nash threw the belt in a trash can"),
            dict(ic="A", name="AWA World Tag Team Championship", count="1",
                 sub="With Curt Hennig &middot; January 18, 1986, Albuquerque, over Jimmy Garvin and "
                     "Steve Regal &middot; lost May 17, 1986"),
            dict(ic="N", name="TNA World Tag Team Championship", count="1",
                 sub="With Nash and Eric Young under the Freebird rule &middot; taped May 4, 2010 "
                     "&middot; stripped at the June 14, 2010 tapings"),
            dict(ic="P", name="WWC titles, Puerto Rico", count="2",
                 sub="Caribbean Heavyweight Championship (1991) and Universal Heavyweight "
                     "Championship (2007)"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        lead="Teams and groups across five promotions. The Outsiders and the nWo are the ones history kept.",
        cards=[
            dict(era="CWF &amp; Crockett &middot; c.1983&ndash;1985", name="American Starship",
                 members="Coyote (Scott Hall), Eagle (Dan Spivey)",
                 desc="His first act, a tag team in Championship Wrestling from Florida that also "
                      "worked Jim Crockett Promotions and Central States. Not an AWA team."),
            dict(era="WCW &middot; 1991&ndash;1992", name="The Diamond Mine",
                 members="The Diamond Studd, Diamond Dallas Page (manager), Oz",
                 desc="Page's stable, where Hall first teamed with the man then billed as Oz. That "
                      "was Kevin Nash, five years before The Outsiders."),
            dict(era="WWF &middot; 1994&ndash;1996", name="The Kliq",
                 members="Scott Hall, Kevin Nash, Shawn Michaels, Sean Waltman, Triple H",
                 desc="The backstage group of friends. The Curtain Call at Madison Square Garden on "
                      "May 19, 1996 broke kayfabe in front of a live crowd, and only Triple H was "
                      "punished, because Hall and Nash were already leaving."),
            dict(era="WCW &middot; 1996&ndash;2000", name="The Outsiders",
                 members="Scott Hall, Kevin Nash (Syxx as a stand-in in 1997)",
                 desc="Six WCW World Tag Team Championship reigns and PWI Tag Team of the Year for "
                      "1997. The team split at Slamboree 1998 and reunited in 1999."),
            dict(era="WCW &middot; 1996&ndash;1999 &middot; WWF 2002", name="nWo",
                 members="Hulk Hogan, Scott Hall, Kevin Nash, later many more",
                 desc="Founded at Bash at the Beach on July 7, 1996. Hall sided with nWo Hollywood "
                      "after Slamboree 1998, and the three founders brought the group to the WWF "
                      "in 2002. Inducted into the WWE Hall of Fame with the 2020 class."),
            dict(era="TNA &middot; 2004&ndash;2005 &middot; 2010", name="Kings of Wrestling and The Band",
                 members="Hall, Nash, Jeff Jarrett (2004); Hall, Nash, Waltman, Eric Young (2010)",
                 desc="Two late TNA reunions. The Band held the TNA World Tag Team Championship in "
                      "2010 until it was stripped that June."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead=("One career, four names. The Diamond Studd built the toothpick and the finisher, "
              "Razor Ramon made them famous, and Scott Hall used his own name to start an invasion."),
        cards=[
            dict(mono="SH", era="Florida &middot; AWA &middot; 1984&ndash;1989",
                 name="Starship Coyote / Big Scott Hall",
                 desc="American Starship's Coyote in Florida, then Magnum and Big Scott Hall in the "
                      "AWA, where he won the tag titles with Curt Hennig and challenged for the AWA "
                      "world title. New Japan, Germany and Puerto Rico filled the gaps."),
            dict(mono="DS", era="WCW &middot; 1991&ndash;1992", name="The Diamond Studd",
                 desc="The toothpick flick and Diamond Dallas Page as his manager. The "
                      "crucifix powerbomb was already the finish. He left WCW in May 1992 and the "
                      "WWF signed him that month."),
            dict(mono="RR", era="WWF &middot; 1992&ndash;1996", name="Razor Ramon",
                 desc="A heel modeled on Scarface who was captaining the fan favorites by "
                      "Survivor Series 1994. Four Intercontinental reigns, the WrestleMania X "
                      "ladder match, and a crucifix powerbomb finish named for the character."),
            dict(mono="HL", era="WCW &middot; 1996&ndash;2000 &middot; WWF 2002", name="Scott Hall",
                 desc="His real name and no gimmick. He walked out of the Nitro crowd on May "
                      "27, 1996, co-founded the nWo, won seven WCW tag titles, and kept the "
                      "crucifix powerbomb under a new name."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Florida to Madison Square Garden to Daytona Beach, and out through Des Moines in 2016.",
        rows=[
            dict(year="1984", title="Debut in Florida",
                 desc="Starts in Championship Wrestling from Florida as Coyote of American Starship "
                      "with Dan Spivey. Wikipedia dates the debut October 2, 1984."),
            dict(year="1986", title="AWA tag champion",
                 desc="Wins the AWA World Tag Team Championship with Curt Hennig on January 18 in "
                      "Albuquerque."),
            dict(year="1989", title="First WCW run",
                 desc="Debuts on WCW television on July 9, pinned by The Great Muta."),
            dict(year="1991", title="The Diamond Studd",
                 desc="Returns to WCW managed by Diamond Dallas Page, teaming with Oz, who is Kevin "
                      "Nash."),
            dict(year="1992", title="Razor Ramon arrives",
                 desc="Signs with the WWF and wins his TV debut on Superstars on August 8 with his "
                      "crucifix powerbomb."),
            dict(year="1993", title="Intercontinental Champion",
                 desc="Pins Bob Backlund at WrestleMania IX, then wins the vacant title in a Raw "
                      "battle royal final over Rick Martel."),
            dict(year="1994", title="The ladder match",
                 desc="Beats Shawn Michaels at WrestleMania X on March 20 to unify the title. Loses "
                      "it to Diesel, wins it back at SummerSlam, and is sole survivor at Survivor "
                      "Series."),
            dict(year="1995", title="Third and fourth reigns",
                 desc="Loses to Jeff Jarrett at the Royal Rumble, regains the belt in Montreal in "
                      "May, loses the SummerSlam ladder rematch to Michaels, and wins a fourth "
                      "title in Winnipeg in October."),
            dict(year="1996", title="The Outsider",
                 desc="Drops the title to Goldust in January, takes part in the Curtain Call on May "
                      "19, debuts on Nitro on May 27, and forms the nWo with Nash and Hogan at Bash "
                      "at the Beach on July 7."),
            dict(year="1997", title="Tag champion, World War 3 winner",
                 desc="The Outsiders hold the tag titles for 231 days in one stretch, Syxx filling in "
                      "for Nash. Hall wins the World War 3 battle royal on November 23."),
            dict(year="1998", title="Title shot and the split",
                 desc="Loses to Sting for the WCW World Heavyweight Championship at Uncensored, turns "
                      "on Nash at Slamboree, and stun-guns Goldberg at Starrcade."),
            dict(year="1999", title="Three titles in one year",
                 desc="Two United States title wins, the Television title at Mayhem, and a last tag "
                      "reign with Nash in December."),
            dict(year="2002", title="Back to the WWF",
                 desc="Returns with the nWo at No Way Out, loses to Steve Austin at WrestleMania X8, "
                      "and is released in May."),
            dict(year="2004", title="TNA",
                 desc="Teams with Nash and Jeff Jarrett as the Kings of Wrestling; loses to Jeff "
                      "Hardy at Final Resolution in January 2005."),
            dict(year="2010", title="One more tag title",
                 desc="Wins the TNA World Tag Team Championship with Nash and Eric Young, then is "
                      "stripped and released in June."),
            dict(year="2014", title="Hall of Fame",
                 desc="Inducted by Kevin Nash on April 5 in New Orleans."),
            dict(year="2016", title="Final match",
                 desc="Beats Chuck Taylor in Des Moines on June 17."),
            dict(year="2021", title="Hall of Fame, again",
                 desc="Inducted with the nWo as part of the 2020 class, in a ceremony delayed by the "
                      "pandemic and aired April 6, 2021."),
            dict(year="2022", title="Death",
                 desc="Dies March 14, 2022, at 63, in Marietta, Georgia, after complications from "
                      "hip-replacement surgery. WWE announces it at the start of that night's Raw."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="The men he fought, and the friend he fought most.",
        cards=[
            dict(name="Shawn Michaels",
                 desc="Friends off camera, rivals on it. WrestleMania X put both belts above the "
                      "ring and Razor got them. Michaels won the SummerSlam 1995 rematch."),
            dict(name="Kevin Nash",
                 desc="Took the Intercontinental title from him as Diesel in April 1994 and lost "
                      "it back at SummerSlam. Then the partner of his career, until Hall hit him "
                      "with a belt at Slamboree 1998."),
            dict(name="Jeff Jarrett",
                 desc="Three Intercontinental title changes in 1995, a WrestleMania XI win by "
                      "disqualification, and TNA matches against each other in 2002."),
            dict(name="Goldust",
                 desc="Ended Razor's fourth and last Intercontinental reign at the 1996 Royal "
                      "Rumble in Fresno on January 21."),
            dict(name="The Steiner Brothers",
                 desc="Traded the WCW World Tag Team Championship with The Outsiders through 1997 "
                      "and 1998, until Scott Steiner turned on Rick at SuperBrawl VIII."),
            dict(name="Goldberg",
                 desc="Hall's stun gun at Starrcade 1998 cost Goldberg the streak. Goldberg answered "
                      "in a stun gun ladder match at Souled Out 1999."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Legacy",
        lead="Verified entries only.",
        rows=[
            dict(when="1996", title="Wrestling Observer Best Gimmick", kind="Award",
                 desc="Observer readers voted the nWo the best gimmick of 1996."),
            dict(when="2011", title="E:60, Scott Hall", kind="TV",
                 desc="ESPN's E:60 profile, \"Scott Hall, a cautionary tale,\" aired "
                      "October 19, 2011."),
            dict(when="2014", title="WWE Hall of Fame speech", kind="Speech",
                 desc="Inducted by Kevin Nash. He closed with \"Hard work pays off, dreams come "
                      "true, bad times don't last, but bad guys do.\""),
            dict(when="2015", title="The Resurrection of Jake the Snake", kind="Film",
                 desc="Steve Yu's documentary, which premiered at Slamdance on January 23, 2015. "
                      "Hall joins Jake Roberts at Diamond Dallas Page's house during recovery."),
            dict(when="2016", title="WWE 2K17", kind="Game",
                 desc="Playable as a legend, as Scott Hall with Razor Ramon as an alternate."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, and the framing the sources support.",
        stats=[
            ("4",   "Intercontinental reigns"),
            ("7",   "WCW World Tag reigns"),
            ("2",   "WWE Hall of Fame inductions"),
        ],
        rows=[
            dict(name="First four-time Intercontinental Champion",
                 sub="His third reign in May 1995 made him the first three-time champion, and the "
                     "fourth in October 1995 the first four-time champion."),
            dict(name="WrestleMania X: five stars and Match of the Year",
                 sub="Dave Meltzer rated the March 20, 1994 ladder match five stars. Observer and PWI "
                     "readers both named it the 1994 Match of the Year."),
            dict(name="Seven WCW World Tag Team Championship reigns",
                 sub="Six with Kevin Nash and one with The Giant, between October 1996 and "
                     "December 1999."),
            dict(name="1997 World War 3 winner",
                 sub="Won the 60-man battle royal on November 23, 1997, last eliminating The Giant."),
            dict(name="Survivor Series 1994 sole survivor",
                 sub="Captained The Bad Guys and outlasted The Teamsters when all five were counted "
                     "out."),
            dict(name="Two WWE Hall of Fame inductions",
                 sub="Individually in 2014 and with the nWo in the 2020 class."),
            dict(name="PWI honors",
                 sub="Most Improved Wrestler 1992, and Tag Team of the Year 1997 with Nash."),
        ],
        footnote=("No career win-loss total is published: none can be verified across Florida, the "
                  "AWA, WCW, the WWF, TNA and the independents. The old version of this page "
                  "showed a 1-5-0 record with finish percentages; it had no source and was removed."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Scott Hall, full biography", href="https://en.wikipedia.org/wiki/Scott_Hall"),
        dict(k="WWE.com", v="Razor Ramon alumni profile", href="https://www.wwe.com/superstars/razor-ramon"),
        dict(k="WWE.com", v="Intercontinental title history", href="https://www.wwe.com/classics/titlehistory/intercontinental"),
        dict(k="Wikipedia", v="WrestleMania X, the ladder match", href="https://en.wikipedia.org/wiki/WrestleMania_X"),
        dict(k="Wikipedia", v="Bash at the Beach 1996, the nWo", href="https://en.wikipedia.org/wiki/Bash_at_the_Beach_(1996)"),
        dict(k="Wikipedia", v="WCW World Tag Team title history", href="https://en.wikipedia.org/wiki/List_of_WCW_World_Tag_Team_Champions"),
        dict(k="CBS Sports", v="Obituary, March 14, 2022", href="https://www.cbssports.com/wwe/news/wrestling-legend-scott-hall-dies-at-63-two-time-wwe-hall-of-famer-taken-off-life-support-after-heart-attacks"),
        dict(k="Wikipedia", v="WWE Hall of Fame", href="https://en.wikipedia.org/wiki/WWE_Hall_of_Fame"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="How did Scott Hall die?",
            a="He died on March 14, 2022, at 63, at WellStar Kennestone Hospital in Marietta, "
              "Georgia. He had broken his hip in a fall earlier that month. After hip-replacement "
              "surgery a blood clot came loose, he had three heart attacks on March 12, and his "
              "family took him off life support two days later. WWE announced his death at the "
              "start of that night's Raw.",
            q_ld="How did Scott Hall die?",
            a_ld="Scott Hall, who wrestled as Razor Ramon, died on March 14, 2022, at age 63, at "
                 "WellStar Kennestone Hospital in Marietta, Georgia. After hip-replacement surgery "
                 "following a fall, a blood clot led to three heart attacks on March 12, 2022, and "
                 "he was removed from life support on March 14."),
        dict(
            q="Who won the WrestleMania X ladder match?",
            a="Razor Ramon. On March 20, 1994 at Madison Square Garden, both Intercontinental belts "
              "hung above the ring. Shawn Michaels got caught in the ropes and Razor climbed down "
              "with both, staying the undisputed champion. Michaels won their SummerSlam 1995 "
              "ladder rematch.",
            q_ld="Who won the ladder match between Razor Ramon and Shawn Michaels at WrestleMania X?",
            a_ld="Razor Ramon won the ladder match at WrestleMania X on March 20, 1994, at Madison "
                 "Square Garden, retrieving both Intercontinental Championship belts to remain the "
                 "undisputed champion. Shawn Michaels won their ladder match rematch at SummerSlam "
                 "on August 27, 1995."),
        dict(
            q="How many times was Razor Ramon Intercontinental Champion?",
            a="Four, and he was the first wrestler to reach both three and four reigns. WWE dates "
              "them September 27, 1993, August 29, 1994, May 19, 1995 and October 22, 1995, for "
              "434 days in all.",
            q_ld="How many times was Razor Ramon Intercontinental Champion?",
            a_ld="Razor Ramon held the WWF Intercontinental Championship four times, the first "
                 "wrestler to do so. WWE dates the reigns from September 27, 1993, August 29, 1994, "
                 "May 19, 1995 and October 22, 1995, totaling 434 days."),
        dict(
            q="Was Scott Hall a founding member of the nWo?",
            a="Yes. Hall and Kevin Nash arrived in WCW as The Outsiders in 1996, and at Bash at the "
              "Beach on July 7, 1996 Hulk Hogan was revealed as their third man. Those three are "
              "the founders. WWE inducted the nWo, with Hall, into the Hall of Fame as part of the "
              "2020 class.",
            q_ld="Was Scott Hall a founding member of the nWo?",
            a_ld="Yes. Scott Hall, Kevin Nash and Hulk Hogan founded the nWo at WCW Bash at the "
                 "Beach on July 7, 1996, when Hogan was revealed as the partner of Hall and Nash, "
                 "known as The Outsiders. The nWo, including Hall, was inducted into the WWE Hall "
                 "of Fame as part of the 2020 class."),
        dict(
            q="How many WCW tag team titles did Scott Hall win?",
            a="Seven WCW World Tag Team Championships. Six came with Kevin Nash as The Outsiders, "
              "starting at Halloween Havoc on October 27, 1996, and one with The Giant on July 20, "
              "1998. During one 1997 reign Syxx defended in the injured Nash's place.",
            q_ld="How many WCW World Tag Team Championships did Scott Hall win?",
            a_ld="Scott Hall won the WCW World Tag Team Championship seven times: six with Kevin "
                 "Nash as The Outsiders, beginning at Halloween Havoc on October 27, 1996, and once "
                 "with The Giant on July 20, 1998."),
        dict(
            q="What was the Razor&rsquo;s Edge?",
            a="His finisher, a crucifix powerbomb: he lifted the opponent onto his shoulders with "
              "the arms spread and threw them down back first. In WCW he kept the move and renamed "
              "it for The Outsiders.",
            q_ld="What was Razor Ramon's finishing move?",
            a_ld="Razor Ramon's finishing move was the Razor's Edge, a crucifix powerbomb. As Scott "
                 "Hall in WCW the same move was called the Outsider's Edge."),
        dict(
            q="Was Razor Ramon really Cuban?",
            a="No. The character was built on Tony Montana from <i>Scarface</i>, and he was billed "
              "from Miami. Scott Hall was born in St. Mary&rsquo;s County, Maryland, on October 20, "
              "1958.",
            q_ld="Was Razor Ramon actually Cuban?",
            a_ld="No. Razor Ramon was a character inspired by Tony Montana from the film Scarface "
                 "and billed from Miami. Scott Hall was born on October 20, 1958, in St. Mary's "
                 "County, Maryland."),
        dict(
            q="Is Scott Hall in the WWE Hall of Fame?",
            a="Twice. Kevin Nash inducted him individually on April 5, 2014 in New Orleans. He went "
              "in again with the nWo, alongside Hulk Hogan, Nash and Sean Waltman, in the 2020 "
              "class, whose ceremony was delayed by the pandemic and aired April 6, 2021.",
            q_ld="Is Scott Hall in the WWE Hall of Fame?",
            a_ld="Yes, twice. Scott Hall was inducted individually on April 5, 2014, in New "
                 "Orleans, by Kevin Nash, and again as a member of the nWo with Hulk Hogan, Kevin "
                 "Nash and Sean Waltman in the 2020 class, whose ceremony aired April 6, 2021."),
        dict(
            q="What was the Kliq and the Curtain Call?",
            a="The Kliq was a backstage group of friends: Hall, Kevin Nash, Shawn Michaels, Sean "
              "Waltman and Triple H. On May 19, 1996, at the end of Hall and Nash's last WWF night "
              "at Madison Square Garden, four of them hugged in the ring in front of the crowd. "
              "Hall and Nash were already leaving for WCW, so Triple H took the punishment.",
            q_ld="What was the Kliq's Curtain Call?",
            a_ld="The Curtain Call happened on May 19, 1996, at Madison Square Garden, when Kliq "
                 "members Scott Hall, Kevin Nash, Shawn Michaels and Triple H embraced in the ring "
                 "after the show, breaking character in front of the live crowd. Hall and Nash were "
                 "leaving for WCW, so only Triple H was punished."),
        dict(
            q="Did Scott Hall ever win a world title?",
            a="No. His best shot came from winning the World War 3 battle royal on November 23, "
              "1997, which earned him a WCW World Heavyweight Championship match. Sting beat him at "
              "Uncensored on March 15, 1998.",
            q_ld="Did Scott Hall ever win a world heavyweight championship?",
            a_ld="No. Scott Hall never held a world heavyweight championship. He won the WCW World "
                 "War 3 battle royal on November 23, 1997, and lost the resulting WCW World "
                 "Heavyweight Championship match to Sting at Uncensored on March 15, 1998."),
        dict(
            q="Who was The Diamond Studd?",
            a="Scott Hall in WCW in 1991 and 1992, managed by Diamond Dallas Page in the Diamond "
              "Mine. The toothpick and the crucifix powerbomb started there. His partner Oz was "
              "Kevin Nash.",
            q_ld="Who was The Diamond Studd in WCW?",
            a_ld="The Diamond Studd was Scott Hall's WCW character in 1991 and 1992, managed by "
                 "Diamond Dallas Page. He later became Razor Ramon in the WWF."),
        dict(
            q="What was Scott Hall&rsquo;s last match?",
            a="A win over Chuck Taylor at F1RST Wrestling in Des Moines, Iowa, on June 17, 2016. "
              "His last WWF match came in May 2002, and his last WCW match was SuperBrawl 2000 on "
              "February 20.",
            q_ld="What was Scott Hall's last match?",
            a_ld="Scott Hall's final match was a win over Chuck Taylor at F1RST Wrestling in Des "
                 "Moines, Iowa, on June 17, 2016."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Scott Oliver Hall"),
        dict(label="Born", value="October 20, 1958", sub="St. Mary&rsquo;s County, Maryland"),
        dict(label="Died", value="March 14, 2022",
             sub="Marietta, Georgia &middot; complications after hip surgery &middot; age 63"),
        dict(label="Billed from", value="Miami, Florida"),
        dict(label="Height", value="6&#8242;7&#8243;", sub="201 cm (billed)"),
        dict(label="Weight", value="287 lb", sub="130 kg (billed)"),
        dict(label="Debut", value="1984", sub="October 2 per Wikipedia; Dan Spivey's page dates their team to 1983"),
        dict(label="Trained by", value="Hiro Matsuda", sub="also Florida training under Dusty Rhodes"),
        dict(label="Ring names", value="Coyote &middot; Diamond Studd &middot; Razor Ramon",
             sub="Magnum and Big Scott Hall in the AWA, Texas Scott in Germany"),
        dict(label="Finisher", value="Razor&rsquo;s Edge", sub="crucifix powerbomb &middot; the Outsider&rsquo;s Edge in WCW"),
        dict(label="Catchphrase", value="&ldquo;Say hello to the Bad Guy&rdquo;"),
        dict(label="Family", value="Children Cody and Cassidy", sub="Cody Hall also wrestles"),
        dict(label="Hall of Fame", value="2014 &middot; 2020",
             sub="individually, inducted by Kevin Nash &middot; then with the nWo"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1958-10-20",
    bornplace="St. Mary's County, Maryland",
    nationality="United States",
    height_cm=201,
    weight_kg=130,
    ld=dict(
        alternateName=["Scott Hall", "Scott Oliver Hall", "The Bad Guy", "The Diamond Studd",
                       "Starship Coyote", "The Outsider"],
        deathDate="2022-03-14",
        deathPlace="Marietta, Georgia",
        award=["WWF Intercontinental Championship (4 reigns)",
               "WCW World Tag Team Championship (7 reigns)",
               "WCW United States Heavyweight Championship (2 reigns)",
               "WCW World Television Championship (1 reign)",
               "AWA World Tag Team Championship (1 reign, with Curt Hennig)",
               "TNA World Tag Team Championship (1 reign)",
               "WCW World War 3 winner (1997)",
               "Wrestling Observer and PWI Match of the Year (1994, vs Shawn Michaels)",
               "WWE Hall of Fame (2014)",
               "WWE Hall of Fame (2020, as a member of the nWo)"],
        knowsAbout=["Professional wrestling", "Ladder match", "nWo", "The Outsiders", "WWF", "WCW",
                    "Intercontinental Championship"],
        description="Scott Hall was an American professional wrestler who performed as Razor "
                    "Ramon in the WWF from 1992 to 1996, winning the Intercontinental Championship "
                    "four times and defeating Shawn Michaels in the WrestleMania X ladder match, "
                    "the 1994 Match of the Year. In WCW he co-founded the nWo with Kevin Nash and "
                    "Hulk Hogan in 1996 and won the WCW World Tag Team Championship seven times. "
                    "He was inducted into the WWE Hall of Fame in 2014 and again with the nWo in "
                    "2020. He died on March 14, 2022, at age 63.",
        sameAs=["https://en.wikipedia.org/wiki/Scott_Hall",
                "https://www.wwe.com/superstars/razor-ramon"],
    ),
)
