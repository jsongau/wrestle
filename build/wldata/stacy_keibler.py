# -*- coding: utf-8 -*-
"""Stacy Keibler - dossier data.

Compiled November 9, 2026 from data/stacy-keibler.md, which carries a source URL
on every claim. New page: there was no earlier /wrestlers/stacy-keibler/ to harvest.

She was a valet and manager first and a wrestler second, so the record is a
verified sample: every PPV match she wrestled plus the notable TV bouts that two
sources agree on (Cagematch's 74-match log, cross-checked against Wikipedia event
articles and thehistoryofwwe.com Raw results). House shows are left out.

Deliberate omissions:
  * No Signature section. No Observer or Cagematch star rating exists for any of
    her matches, and this site never invents one.
  * No social links (x_url / ig_url): none were verified in this pass.
  * No pulse section: she is retired and there is no verified current feed.
  * No win-loss total. record.total is the honest row count.
  * No Spotify player: no verified track id for the Kid Rock "Legs" cover, so the
    walk-out band ships with links only.
Disputes are flagged in the .md with the flag symbol and printed on the page where
they matter (Babe of the Year year, two 2002 title-match claims, debut match, last
match date, weight).
"""

_SLUGS = {
    "Trish Stratus": "trish-stratus", "Lita": "lita", "Chris Jericho": "chris-jericho",
    "Christian": "christian", "Matt Hardy": "matt-hardy", "Jeff Hardy": "jeff-hardy",
}

def _a(name):
    return '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_SLUGS[name], name)

# ----------------------------------------------------------------- record rows
ROWS = [
    # ---------------- WCW 2000
    dict(result="W", date="2000-06-05", promo="WCW", type="tag",
         event="Nitro", opponent="Kimberly & Mike Awesome",
         stip="Mixed tag with Diamond Dallas Page, her first logged match", title=""),
    dict(result="L", date="2000-07-09", promo="WCW", landmark=True,
         event="Bash at the Beach", opponent="Daffney",
         stip="Wedding Gown match, the first in WCW, with David Flair in her corner", title=""),
    dict(result="L", date="2000-07-24", promo="WCW", type="tag",
         event="Nitro", opponent="Lt. Loco & Major Gunns",
         stip="Mixed tag with David Flair", title=""),
    dict(result="W", date="2000-07-31", promo="WCW",
         event="Nitro", opponent="Major Gunns", stip="Hardcore match", title=""),
    dict(result="W", date="2000-08-08", promo="WCW", type="tag",
         event="Thunder", opponent="Major Gunns & Sgt. A-WOL",
         stip="Mixed tag tables match with David Flair", title=""),
    dict(result="L", date="2000-08-13", promo="WCW", landmark=True,
         event="New Blood Rising", opponent="Major Gunns",
         stip="Mud match, the finish that set up the false pregnancy angle", title=""),
    # ---------------- WWF 2001
    dict(result="L", date="2001-07-22", promo="WWE", type="tag", landmark=True,
         event="Invasion", opponent=_a("Lita") + " & " + _a("Trish Stratus"), opponent_html=True,
         stip="First tag team bra and panties match, with Torrie Wilson; Mick Foley referees", title=""),
    dict(result="W", date="2001-08-06", promo="WWE", type="tag",
         event="Raw", opponent="Jacqueline", stip="Two-on-one handicap with Torrie Wilson", title=""),
    dict(result="L", date="2001-08-20", promo="WWE", type="tag",
         event="Raw", opponent="Jacqueline, Lita & Molly Holly",
         stip="Six-woman tag with Ivory and Torrie Wilson", title=""),
    dict(result="W", date="2001-10-01", promo="WWE", type="tag",
         event="Raw", opponent="Tajiri & Torrie Wilson",
         stip="Mixed tag with Tazz; she pinned Torrie", title=""),
    dict(result="L", date="2001-10-21", promo="WWE", landmark=True,
         event="No Mercy", opponent="Torrie Wilson",
         stip="The first lingerie match in WWF history", title=""),
    dict(result="L", date="2001-10-29", promo="WWE",
         event="Raw", opponent=_a("Lita"), opponent_html=True, stip="Singles", title=""),
    dict(result="W", date="2001-10-30", promo="WWE", type="tag",
         event="SmackDown", opponent=_a("Lita") + " & the Hardy Boyz", opponent_html=True,
         stip="Six-person tag with the Dudley Boyz (taping date)", title=""),
    dict(result="L", date="2001-11-03", promo="WWE", type="tag",
         event="Rebellion", opponent=_a("Lita") + " & Torrie Wilson", opponent_html=True,
         stip="Tag with Mighty Molly; Trish Stratus referees", title=""),
    dict(result="L", date="2001-11-05", promo="WWE", type="tag",
         event="Raw", opponent="The APA & Jacqueline",
         stip="Tables match with the Dudley Boyz", title=""),
    dict(result="L", date="2001-11-20", promo="WWE",
         event="SmackDown", opponent=_a("Trish Stratus"), opponent_html=True,
         stip="Gravy bowl match (taping date)", title="WWF Women's Championship"),
    dict(result="L", date="2001-11-26", promo="WWE", landmark=True,
         event="Raw", opponent=_a("Trish Stratus"), opponent_html=True,
         stip="Bra and panties match", title="WWF Women's Championship"),
    dict(result="L", date="2001-12-24", promo="WWE",
         event="Raw", opponent="Torrie Wilson", stip="Eggnog match, taped December 21", title=""),
    # ---------------- WWE 2002
    dict(result="W", date="2002-02-11", promo="WWE",
         event="Raw", opponent="Torrie Wilson", stip="Bikini match", title=""),
    dict(result="W", date="2002-03-11", promo="WWE", type="tag",
         event="Raw", opponent=_a("Lita") + " & " + _a("Trish Stratus"), opponent_html=True,
         stip="Tag with Jazz", title=""),
    dict(result="L", date="2002-05-19", promo="WWE", landmark=True,
         event="Judgment Day", opponent=_a("Trish Stratus"), opponent_html=True,
         stip="Her only singles title match on pay-per-view", title="WWE Women's Championship"),
    dict(result="L", date="2002-07-02", promo="WWE",
         event="SmackDown", opponent="Torrie Wilson",
         stip="Bra and panties match (taping date)", title=""),
    dict(result="L", date="2002-08-19", promo="WWE",
         event="Raw", opponent=_a("Trish Stratus"), opponent_html=True,
         stip="Bra and panties mud match, her first Raw match after the move from SmackDown", title=""),
    dict(result="L", date="2002-09-02", promo="WWE",
         event="Raw", opponent="Terri Runnels",
         stip="Lingerie pillow fight; Jerry Lawler referees", title=""),
    dict(result="L", date="2002-09-09", promo="WWE", type="tag",
         event="Raw", opponent=_a("Trish Stratus") + " & Terri Runnels", opponent_html=True,
         stip="Tag with Victoria", title=""),
    dict(result="L", date="2002-10-07", promo="WWE",
         event="Raw", opponent=_a("Trish Stratus"), opponent_html=True,
         stip="Bra and panties, paddle stipulation; sources split on whether the title was on the line",
         title=""),
    dict(result="L", date="2002-11-18", promo="WWE",
         event="Raw", opponent="Victoria",
         stip="Singles; sources split on whether Victoria's title was on the line", title=""),
    # ---------------- WWE 2003
    dict(result="W", date="2003-02-24", promo="WWE", type="tag",
         event="Raw", opponent=_a("Chris Jericho") + " & " + _a("Christian"), opponent_html=True,
         stip="Mixed tag with Test, won by disqualification", title=""),
    dict(result="L", date="2003-06-30", promo="WWE", type="tag",
         event="Raw", opponent=_a("Chris Jericho") + " & Test", opponent_html=True,
         stip="Tag with Scott Steiner, restarted as no disqualification", title=""),
    dict(result="L", date="2003-08-11", promo="WWE", type="tag",
         event="Raw", opponent="Rico & Miss Jackie",
         stip="Mixed tag with Scott Steiner", title=""),
    dict(result="W", date="2003-09-01", promo="WWE", type="tag",
         event="Raw", opponent="Steven Richards & Victoria",
         stip="No-disqualification mixed tag with Test; she pinned Victoria", title=""),
    # ---------------- WWE 2004
    dict(result="L", date="2004-03-14", promo="WWE", type="tag", landmark=True,
         event="WrestleMania XX", opponent="Sable & Torrie Wilson",
         stip="Playboy Evening Gown match with Miss Jackie, Madison Square Garden", title=""),
    dict(result="NC", date="2004-03-15", promo="WWE",
         event="Raw", opponent="Miss Jackie",
         stip="Stopped when Mr. McMahon interrupted with the draft announcement", title=""),
    dict(result="L", date="2004-04-05", promo="WWE", type="tag",
         event="Raw", opponent="Lita, Trish Stratus, Gail Kim, Jazz, Molly Holly & Nidia",
         stip="Battle royal for a Women's Championship shot, won by Lita", title=""),
    dict(result="L", date="2004-05-10", promo="WWE", type="tag",
         event="Raw", opponent="Gail Kim, Jazz & Molly Holly",
         stip="Six-woman tag with Nidia and Victoria", title=""),
    dict(result="L", date="2004-06-14", promo="WWE", type="tag",
         event="Raw", opponent="Gail Kim & Molly Holly",
         stip="Tag with Nidia; she submitted to Gail Kim", title=""),
    dict(result="W", date="2004-08-09", promo="WWE", type="tag",
         event="Raw", opponent="Molly Holly, Gail Kim & Jazz",
         stip="Six-woman tag with Victoria and Nidia", title=""),
    dict(result="W", date="2004-09-13", promo="WWE", type="tag",
         event="Raw", opponent=_a("Trish Stratus") + ", Gail Kim & Molly Holly", opponent_html=True,
         stip="Six-woman tag with Victoria and Nidia", title=""),
    dict(result="W", date="2004-09-20", promo="WWE", type="tag",
         event="Raw", opponent=_a("Trish Stratus") + " & Molly Holly", opponent_html=True,
         stip="Tag with Victoria; she pinned Molly with a backslide", title=""),
    dict(result="W", date="2004-10-04", promo="WWE", landmark=True,
         event="Raw", opponent="Molly Holly",
         stip="Singles win by roll-up, Madison Square Garden, a week before her title shot", title=""),
    dict(result="L", date="2004-10-11", promo="WWE", landmark=True,
         event="Raw", opponent=_a("Trish Stratus"), opponent_html=True,
         stip="Singles in Manchester, England; Trish went after her injured leg",
         title="WWE Women's Championship"),
    dict(result="W", date="2004-10-18", promo="WWE", type="tag",
         event="Raw", opponent=_a("Trish Stratus") + ", Molly Holly & Gail Kim", opponent_html=True,
         stip="Six-woman tag with Victoria and Nidia", title=""),
    dict(result="L", date="2004-10-19", promo="WWE", type="tag", landmark=True,
         event="Taboo Tuesday", opponent=_a("Trish Stratus") + " and five others", opponent_html=True,
         stip="Fulfill Your Fantasy battle royal; eliminated second-to-last, by Molly Holly",
         title="WWE Women's Championship"),
    dict(result="L", date="2004-11-15", promo="WWE",
         event="Raw", opponent="Christy Hemme", stip="Lingerie pillow fight", title=""),
    # ---------------- WWE 2005
    dict(result="L", date="2005-08-08", promo="WWE", type="tag",
         event="Raw", opponent="The Heart Throbs & Victoria",
         stip="Mixed six-person tag as Super Stacy, with The Hurricane and Rosey", title=""),
    dict(result="L", date="2005-08-15", promo="WWE",
         event="Sunday Night Heat", opponent="Victoria", stip="Singles", title=""),
    dict(result="L", date="2005-10-25", promo="WWE", landmark=True,
         event="Velocity", opponent="Jillian Hall",
         stip="Her last match, on SmackDown's B-show (Cagematch taping date)", title=""),
]

DATA = dict(
    slug="stacy-keibler",
    name="Stacy Keibler",
    realname="Stacy Ann-Marie Keibler",
    epithet="The Legs of WWE",
    hook="WCW, WWE & Hall of Fame",
    art="stacy-keibler",

    meta_desc=("Stacy Keibler went from Nitro Girl to Miss Hancock in WCW, managed the Dudley Boyz, "
               "Test and Scott Steiner in WWE, finished third on Dancing with the Stars and entered "
               "the WWE Hall of Fame in 2023. Verified record, career and FAQ."),
    og_desc=("Nitro Girl, Miss Hancock, Duchess of Dudleyville, Super Stacy. Then Dancing with the "
             "Stars, Hollywood and the 2023 WWE Hall of Fame."),
    tw_desc="Stacy Keibler: WCW's Miss Hancock, WWE's Duchess of Dudleyville, Hall of Fame 2023.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1999",
    height_imp="5&#8242;11&#8243;",
    weight_lb="136",
    vitals_tagline="Duchess of Dudleyville",
    support_note="Profile &middot; Games &middot; Watch",
    sp_items=[
        dict(ic="WWE", title="Official Profile", sub="WWE.com Hall of Fame page", tag="Visit",
             href="https://www.wwe.com/superstars/stacykeibler"),
        dict(ic="HOF", title="Hall of Fame 2023", sub="WWE.com induction story", tag="Read",
             href="https://www.wwe.com/shows/wwe-hall-of-fame/class-of-2023/article/wwe-hall-of-fame-class-of-2023-immortalized-forever"),
        dict(ic="2K", title="WWE 2K26", sub="Playable, with Legs as her entrance music", tag="Play",
             href="https://wwe.2k.com/"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Nitro Girl &middot; Miss Hancock &middot; Duchess of Dudleyville &middot; Hall of Fame 2023",
    hero_tag="Baltimore, Maryland &middot; <em>WCW 1999&ndash;2001 &middot; WWF/WWE 2001&ndash;2006</em>",
    now_label="NOW",
    now_bold="Hall of Famer, retired since 2006",
    now_tail=(" &middot; inducted March 31, 2023 by Mick Foley and Torrie Wilson; playable in WWE 2K26. "
              "No WWE return has been announced."),
    hstats=[
        dict(value="2023", x=False, label="Hall of Fame Class"),
        dict(value="1999", x=False, label="Nitro Girl Search Win"),
        dict(value="30",   x=False, label="Perfect DWTS Score"),
        dict(value="3",    x=False, label="Place, DWTS Season 2"),
    ],
    ghost_link="From a fan-vote dance contest to the Hall of Fame",
    vlabel="Est. 1999 &middot; Baltimore, Maryland",
    mono="SK",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Stacy Keibler</b> got into wrestling through a dance contest. In November 1999 she won "
        "WCW's fan-voted Nitro Girl Search out of 300 entrants and joined the troupe as Skye. Within "
        "months WCW turned her into <b>Miss Hancock</b>, a business-suit heel valet who danced on "
        "tables. When the WWF bought WCW in 2001 it bought her contract too, and she spent the next "
        "five years as one of the most visible women on Raw and SmackDown. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">2023</span>'
        '<span class="pull-cap">her WWE Hall of Fame class, inducted by Mick Foley and Torrie Wilson</span></span>'
        "She managed the Dudley Boyz as the Duchess of Dudleyville, worked as Mr. McMahon's "
        "assistant, managed Test and then Scott Steiner, and wrestled at WrestleMania XX. In 2006 she "
        "finished third on Dancing with the Stars, left WWE that July and built a TV career. WWE "
        "inducted her into its Hall of Fame on March 31, 2023.",

        "Two things get repeated about her that the record does not support. First, she never held "
        "a championship. She challenged for the Women's title in November 2001, at Judgment Day "
        "2002, on Raw in October 2004 and in the Taboo Tuesday 2004 battle royal, and Trish Stratus "
        "beat her every time. Second, she did not win Dancing with the Stars. She finished third in "
        "season 2, behind Drew Lachey and Jerry Rice, though she earned the season's first perfect "
        "score. Her Hall of Fame case was never about titles. WWE's own announcement rests it on "
        "her time as a manager and a fan favorite who crossed into mainstream TV.",

        "She was born Stacy Ann-Marie Keibler on October 14, 1979 in Rosedale, Maryland, took dance "
        "from age three and cheered for the Baltimore Ravens at 18. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig pull-fig--sm">2001</span>'
        '<span class="pull-cap">the first tag team bra and panties match, Invasion, July 22, with Torrie Wilson</span></span>'
        "Her WCW year was all angles: a feud with Daffney over David Flair, WCW's first Wedding Gown "
        "match at Bash at the Beach 2000, and a false pregnancy story that ended with her off TV. "
        "In the WWF she started as an Alliance heel alongside Torrie Wilson. The two lost the first "
        "tag team bra and panties match to Lita and Trish Stratus at Invasion, then split, and "
        "Wilson beat her in the first lingerie match at No Mercy 2001.",

        "Her role kept changing. She held the cage key for the Dudleys at Survivor Series 2001 and "
        "went through a table for them in March 2002. Test and Steiner fought over her contract at "
        "Bad Blood and Unforgiven 2003. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">3rd</span>'
        '<span class="pull-cap">her finish on Dancing with the Stars season 2, 2006</span></span>'
        "Randy Orton dated her on screen and then hit her with an RKO in March 2005 to turn heel. "
        "Her last run was as Super Stacy, sidekick to The Hurricane and Rosey, and her last match "
        "was a loss to Jillian Hall on Velocity in October 2005. After Dancing with the Stars she "
        "acted in What About Brian, Chuck, Psych and How I Met Your Mother. She returned to WWE to "
        "induct Torrie Wilson in 2019, was inducted herself in 2023, and is playable in WWE 2K26.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Verified sample",
        promo_order=["WCW", "WWE"],
        promo_labels={"WCW": "WCW", "WWE": "WWF/WWE"},
        stats=[
            ("47",   "Bouts in this sample"),
            ("74",   "Matches Cagematch logs"),
            ("0",    "Championships"),
            ("4",    "PPV title challenges lost"),
            ("2000", "First logged match"),
            ("2005", "Last match"),
        ],
        lead=("This table is a verified sample, not her full record. She was a valet and manager "
              "first, so most of her TV time came at ringside. Listed here: every pay-per-view match "
              "she wrestled and the TV bouts that Cagematch and a second source agree on. Cagematch "
              "logs 74 matches in all, 2000 to 2005; house shows are left out. No win-loss total is "
              "published. Two 2002 rows carry a dispute over whether a title was on the line, and "
              "they are listed without one. Turn spoilers on to see results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("0",    "Championships"),
            ("2023", "Hall of Fame"),
            ("1999", "Nitro Girl Search"),
            ("3rd",  "Dancing with the Stars"),
        ],
        lead=("No belts. Her honors are the Hall of Fame, a contest win that started it all, and a "
              "network TV result that made her famous outside wrestling."),
        rows=[
            dict(ic="W", name="Women's Championship: challenged, never won", count="0",
                 sub="Lost to Trish Stratus on SmackDown and Raw in November 2001, at Judgment Day on "
                     "May 19, 2002, on Raw in Manchester on October 11, 2004, and in the Taboo Tuesday "
                     "battle royal on October 19, 2004"),
            dict(ic="H", name="WWE Hall of Fame, Class of 2023", count="&mdash;",
                 sub="Inducted March 31, 2023 at Crypto.com Arena, Los Angeles, by Mick Foley and "
                     "Torrie Wilson, alongside Rey Mysterio, The Great Muta and Andy Kaufman"),
            dict(ic="N", name="WCW Nitro Girl Search winner", count="&mdash;",
                 sub="Announced on Nitro, November 8, 1999: most fan votes among eight finalists, a "
                     "spot in the troupe and $10,000. WWE.com's Hall of Fame story dates the contest "
                     "to 2000; the broadcast date is 1999"),
            dict(ic="B", name="WWE Babe of the Year", count="&mdash;",
                 sub="WWE.com lists 2005; Wikipedia's Hall of Fame article lists 2004. The year is "
                     "printed as a dispute until a primary source settles it"),
        ],
    ),

    # ---------------------------------------------------------------- 05 before
    slot5=dict(
        id="before",
        lead="WCW, 1999 to 2001. Three roles in under two years.",
        cards=[
            dict(era="Baltimore &middot; 1997&ndash;99",
                 name="Ravens cheerleader",
                 members="Stacy Keibler",
                 desc="Dance training from age three and a spot on the Baltimore Ravens cheer squad at "
                      "18. That background won her the Nitro Girl Search and gave her the dance "
                      "routines she used for years."),
            dict(era="WCW &middot; 1999&ndash;2000",
                 name="Skye, Nitro Girl",
                 members="The Nitro Girls troupe",
                 desc="Won WCW's nationwide fan-vote contest on Nitro on November 8, 1999, out of 300 "
                      "entrants, and danced weekly as Skye until the troupe wound down in early 2000."),
            dict(era="WCW &middot; 2000",
                 name="Miss Hancock",
                 members="Standards and Practices; David Flair",
                 desc="A heel valet in a business suit who stripped down to table-dance. She first "
                      "managed the tag team Standards and Practices, then took David Flair from "
                      "Daffney. That feud gave her WCW's first Wedding Gown match at Bash at the "
                      "Beach 2000 and a mud match loss to Major Gunns at New Blood Rising."),
            dict(era="WCW &middot; 2001",
                 name="Stacy Keibler, manager",
                 members="Shawn Stasiak",
                 desc="After the false pregnancy angle took her off TV, she came back under her own "
                      "name and managed Shawn Stasiak against Bam Bam Bigelow. When WCW was sold "
                      "in 2001, the WWF bought her contract."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Five characters in six years. Most were someone's manager.",
        cards=[
            dict(mono="MH", era="WCW &middot; 2000", name="Miss Hancock",
                 desc="The table-dancing heel valet. WWE.com and the Bash at the Beach card spell it "
                      "Ms. Hancock; Cagematch spells it Miss. Same character."),
            dict(mono="AL", era="WWF &middot; 2001", name="Alliance mean girl",
                 desc="Debuted on SmackDown on June 14, 2001, then joined The Alliance with Torrie "
                      "Wilson as a heel pair who mocked everyone."),
            dict(mono="DD", era="WWF &middot; 2001&ndash;02", name="Duchess of Dudleyville",
                 desc="Manager of the Dudley Boyz through the tag title unification at Survivor "
                      "Series 2001. It ended when they powerbombed her through a table on Raw in "
                      "March 2002."),
            dict(mono="MG", era="WWE &middot; 2002&ndash;03", name="Manager for hire",
                 desc="Mr. McMahon's assistant on SmackDown, then Test's manager on Raw, then the "
                      "prize in a Test and Scott Steiner feud. Mick Foley fired both men on December "
                      "1, 2003."),
            dict(mono="SS", era="WWE &middot; 2005", name="Super Stacy",
                 desc="Superhero sidekick to The Hurricane and Rosey after Randy Orton's RKO ended "
                      "their on-screen romance. Her last character before she left wrestling."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Dance contest to Hall of Fame in twenty-four years, with the wrestling packed into six.",
        rows=[
            dict(year="1999", title="Wins the Nitro Girl Search",
                 desc="Announced on Nitro on November 8, 1999. She dances for WCW as Skye."),
            dict(year="2000", title="Miss Hancock",
                 desc="Becomes a heel valet, feuds with Daffney over David Flair, and loses WCW's "
                      "first Wedding Gown match at Bash at the Beach on July 9."),
            dict(year="2001", title="WWF debut and Invasion",
                 desc="Debuts on SmackDown on June 14 after the WCW sale. Loses the first tag team "
                      "bra and panties match at Invasion on July 22 and the first lingerie match at "
                      "No Mercy on October 21. Takes over as the Dudleys' manager in October."),
            dict(year="2002", title="WrestleMania X8 and Judgment Day",
                 desc="WrestleMania debut at ringside for the Dudleys, then a Women's Championship "
                      "loss to Trish Stratus at Judgment Day on May 19. Works as Mr. McMahon's "
                      "assistant, moves to Raw on August 12 and pairs with Test."),
            dict(year="2003", title="Test against Steiner",
                 desc="Scott Steiner wins her services at Bad Blood on June 15; Test wins them back "
                      "at Unforgiven on September 21. Mick Foley fires both men on December 1."),
            dict(year="2004", title="WrestleMania XX and a title shot",
                 desc="Loses the Playboy Evening Gown match at Madison Square Garden on March 14. "
                      "Loses a Women's Championship match to Trish Stratus in Manchester on October "
                      "11 and the Taboo Tuesday battle royal eight days later."),
            dict(year="2005", title="The RKO and Super Stacy",
                 desc="Randy Orton hits her with an RKO on Raw on March 21. She joins The Hurricane "
                      "and Rosey as Super Stacy, moves to SmackDown in August, and wrestles her last "
                      "match on Velocity in October."),
            dict(year="2006", title="Dancing with the Stars, then out",
                 desc="Finishes third on season 2 with Tony Dovolani on February 26. Announces on "
                      "July 21 that her WWE contract has ended and that she has a Touchstone TV "
                      "development deal."),
            dict(year="2007", title="Acting",
                 desc="What About Brian and George Lopez in 2007, then October Road and Samurai "
                      "Girl, followed by Chuck, Psych and How I Met Your Mother from 2010."),
            dict(year="2013", title="Host",
                 desc="Hosts Lifetime's Supermarket Superstar. Marries Jared Pobre on March 8, "
                      "2014."),
            dict(year="2019", title="Inducts Torrie Wilson",
                 desc="Returns to WWE on April 6 to induct her old partner and rival into the Hall "
                      "of Fame."),
            dict(year="2023", title="Hall of Fame",
                 desc="Inducted on March 31 in Los Angeles by Mick Foley and Torrie Wilson."),
            dict(year="2026", title="WWE 2K26",
                 desc="Playable in WWE 2K26, with the Kid Rock cover of Legs back as her entrance "
                      "music."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Partners, rivals and the women who kept beating her for the title.",
        cards=[
            dict(name="Torrie Wilson",
                 desc="Alliance partner in 2001, then her main rival after Wilson's Tajiri romance "
                      "made Wilson a fan favorite. Wilson won the No Mercy lingerie match and most of their "
                      "2002 bra and panties series. They stayed close friends, roomed together in "
                      "Los Angeles, and each inducted the other into the Hall of Fame, in 2019 and "
                      "2023."),
            dict(name="Trish Stratus", slug="trish-stratus",
                 desc="The champion in every Women's Championship match Stacy had: SmackDown and Raw "
                      "in November 2001, Judgment Day 2002, Raw on October 11, 2004, and Taboo "
                      "Tuesday 2004. Trish won them all."),
            dict(name="Lita", slug="lita",
                 desc="Across the ring at Invasion 2001, the first big women's match Stacy had in the "
                      "WWF, and a regular singles and tag opponent through 2001 and 2002."),
            dict(name="Daffney",
                 desc="Her WCW rival over David Flair in 2000. Daffney beat her in WCW's first "
                      "Wedding Gown match at Bash at the Beach."),
            dict(name="Molly Holly",
                 desc="The 2004 Raw opponent she beat most often, including a singles win at Madison "
                      "Square Garden on October 4, a week before her last title shot. Holly also "
                      "eliminated her from the Taboo Tuesday battle royal."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Gaming",
        lead="The wrestling run lasted six years. The TV career that followed has run longer.",
        rows=[
            dict(when="2005&ndash;06", title="Punk'd and Stuff magazine", kind="TV",
                 desc="Appearances on Punk'd while still with WWE, plus Stuff covers in June 2005 "
                      "and March 2006 and a stint as the magazine's fitness editor."),
            dict(when="2006", title="Dancing with the Stars, season 2", kind="TV",
                 desc="Third place with Tony Dovolani. A perfect 30 for her week 5 samba, the "
                      "season's first, and Bruno Tonioli's nickname, the Weapon of Mass Seduction."),
            dict(when="2007&ndash;08", title="What About Brian, October Road, Samurai Girl", kind="Screen",
                 desc="Recurring and guest roles on network TV, plus the 2007 film The Comebacks."),
            dict(when="2010&ndash;14", title="Chuck, Psych, How I Met Your Mother", kind="Screen",
                 desc="Her best-known acting run. She played Karina on How I Met Your Mother in 2010 "
                      "and 2014."),
            dict(when="2013", title="Supermarket Superstar", kind="Host",
                 desc="Host of the Lifetime food-pitch competition for its ten-episode run."),
            dict(when="2004", title="Why Can't We Just Dance?", kind="Music",
                 desc="Her track on the WWE Originals album, produced by WWE composer Jim Johnston."),
            dict(when="2000&ndash;2026", title="Video games", kind="Game",
                 desc="WCW Backstage Assault as Miss Hancock in 2000, then WWE titles from "
                      "WrestleMania X8 through WWE 2K26, which brought back her Legs entrance "
                      "music."),
            dict(when="Today", title="Caldera + Lab", kind="Business",
                 desc="A men's skincare brand she co-founded with her husband, Jared Pobre."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="Firsts and honors, with the counting rules that make them true.",
        stats=[
            ("300",  "Nitro Girl Search entrants"),
            ("30",   "Perfect DWTS score"),
            ("5",    "Maxim Hot 100 rank, 2006"),
        ],
        rows=[
            dict(name="Won WCW's Nitro Girl Search",
                 sub="Most fan votes among eight finalists from 300 entrants, announced on Nitro "
                     "November 8, 1999, with a $10,000 prize."),
            dict(name="WCW's first Wedding Gown match",
                 sub="Bash at the Beach, July 9, 2000, against Daffney. She lost."),
            dict(name="The first tag team bra and panties match",
                 sub="Invasion, July 22, 2001, with Torrie Wilson against Lita and Trish Stratus, "
                     "refereed by Mick Foley. She lost."),
            dict(name="The first lingerie match in WWF history",
                 sub="No Mercy, October 21, 2001, against Torrie Wilson. She lost."),
            dict(name="WrestleMania match at Madison Square Garden",
                 sub="WrestleMania XX, March 14, 2004, the Playboy Evening Gown tag with Miss Jackie "
                     "against Sable and Torrie Wilson."),
            dict(name="The first perfect score of Dancing with the Stars season 2",
                 sub="A 30 for the week 5 samba, per WWE.com, on the way to third place."),
            dict(name="WWE Hall of Fame, Class of 2023",
                 sub="Inducted by Mick Foley and Torrie Wilson on March 31, 2023, four years after "
                     "she inducted Wilson."),
        ],
        footnote=("No win-loss total appears on this page because none is verified. Cagematch logs "
                  "74 matches; the table shows 47 of them. Her billed weight differs by source "
                  "(136 lb on Wikipedia, 134 lb on Cagematch)."),
    ),

    # ---------------------------------------------------------------- walk-out
    theme=dict(
        kicker="Entrance theme",
        since="WWF Forceable Entry &middot; 2002",
        track="Legs",
        artist="Kid Rock",
        meta="ZZ Top cover &middot; WWF Forceable Entry &middot; March 26, 2002 &middot; 4:53",
        note=("Kid Rock's cover of the ZZ Top hit sits second on WWF Forceable Entry, right after "
              "Triple H's theme, and it is credited there to Stacy Keibler. The song choice "
              "matched the nickname, The Legs of WWE. WWE 2K26 brought the track back as her "
              "entrance music in March 2026."),
        source_label="Links only &middot; no player",
        links=[
            dict(svc="Wikipedia", sub="Forceable Entry track list",
                 href="https://en.wikipedia.org/wiki/WWF_Forceable_Entry"),
            dict(svc="YouTube", sub="Search the track",
                 href="https://www.youtube.com/results?search_query=Kid+Rock+Legs+Stacy+Keibler+theme"),
            dict(svc="Nu Metal Agenda", sub="Back in WWE 2K26",
                 href="https://numetalagenda.com/news/story/stacy-keibler-has-her-kid-rock-cover-of-legs-in-wwe-2k26-2/"),
        ],
        foot=('Sources: <a href="https://en.wikipedia.org/wiki/WWF_Forceable_Entry" target="_blank" '
              'rel="noopener">Wikipedia, WWF Forceable Entry</a>, '
              '<a href="https://numetalagenda.com/news/story/stacy-keibler-has-her-kid-rock-cover-of-legs-in-wwe-2k26-2/" '
              'target="_blank" rel="noopener">Nu Metal Agenda</a>.'),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/stacykeibler"),
        dict(k="WWE.com", v="Hall of Fame 2023 announcement",
             href="https://www.wwe.com/shows/wwe-hall-of-fame/article/stacy-keibler-announced-for-wwe-hall-of-fame-class-of-2023"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Stacy_Keibler"),
        dict(k="Cagematch", v="74-match log", href="https://www.cagematch.net/?id=2&nr=606&page=4"),
        dict(k="Wikipedia", v="Dancing with the Stars, season 2",
             href="https://en.wikipedia.org/wiki/Dancing_with_the_Stars_(American_season_2)"),
        dict(k="Wrestling Inc", v="2006: her WWE contract ends",
             href="https://www.wrestlinginc.com/news/2006/07/stacy-keibler-comments-on-wwe-departure-492786"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/stacy-keibler.md"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Is Stacy Keibler in the WWE Hall of Fame?",
            a="Yes. She went in with the <b>Class of 2023</b>, inducted by Mick Foley and Torrie "
              "Wilson on March 31, 2023 at Crypto.com Arena in Los Angeles. Rey Mysterio, The Great "
              "Muta and Andy Kaufman were in the same class.",
            q_ld="Is Stacy Keibler in the WWE Hall of Fame?",
            a_ld="Yes. Stacy Keibler was inducted into the WWE Hall of Fame as part of the Class of "
                 "2023 by Mick Foley and Torrie Wilson on March 31, 2023 at Crypto.com Arena in Los "
                 "Angeles."),
        dict(
            q="Did Stacy Keibler ever win a championship?",
            a="No. She never held a title in WCW or WWE. She challenged Trish Stratus for the "
              "Women's Championship in November 2001, at Judgment Day on May 19, 2002, on Raw on "
              "October 11, 2004, and in the Taboo Tuesday battle royal on October 19, 2004, and "
              "lost each time.",
            q_ld="Did Stacy Keibler ever win a championship in WWE or WCW?",
            a_ld="No. Stacy Keibler never won a championship in WCW or WWE. She lost Women's "
                 "Championship challenges to Trish Stratus in November 2001, at Judgment Day 2002, "
                 "on Raw on October 11, 2004, and in the Taboo Tuesday 2004 battle royal."),
        dict(
            q="What was Stacy Keibler's name in WCW?",
            a="Two names. She joined as <b>Skye</b> after winning the Nitro Girl Search on November "
              "8, 1999, then became <b>Miss Hancock</b> in 2000, a heel valet for Standards and "
              "Practices and later David Flair. In 2001 she worked under her own name as Shawn "
              "Stasiak's manager.",
            q_ld="What was Stacy Keibler's ring name in WCW?",
            a_ld="Stacy Keibler was Skye of the Nitro Girls after winning WCW's Nitro Girl Search in "
                 "November 1999, then Miss Hancock, a valet for Standards and Practices and David "
                 "Flair, in 2000. In 2001 she used her real name while managing Shawn Stasiak."),
        dict(
            q="Who did Stacy Keibler manage in WWE?",
            a="The Dudley Boyz as the Duchess of Dudleyville from October 2001, then Test from "
              "late 2002, then Scott Steiner after he won her services at Bad Blood 2003. Test won "
              "her back at Unforgiven 2003. In 2005 she was Super Stacy alongside "
              '<a href="/wrestlers/the-hurricane/">The Hurricane</a> and Rosey.',
            q_ld="Who did Stacy Keibler manage in WWE?",
            a_ld="Stacy Keibler managed the Dudley Boyz as the Duchess of Dudleyville from October "
                 "2001, then Test, then Scott Steiner after Bad Blood 2003, and Test again after "
                 "Unforgiven 2003. In 2005 she teamed with The Hurricane and Rosey as Super Stacy."),
        dict(
            q="How did Stacy Keibler do on Dancing with the Stars?",
            a="She finished <b>third</b> in season 2 with Tony Dovolani, behind Drew Lachey and "
              "Jerry Rice, in the finale on February 26, 2006. Her week 5 samba got a perfect 30, "
              "which WWE.com calls the season's first perfect score.",
            q_ld="How did Stacy Keibler do on Dancing with the Stars?",
            a_ld="Stacy Keibler finished third on season 2 of Dancing with the Stars in 2006, "
                 "partnered with Tony Dovolani, behind winner Drew Lachey and runner-up Jerry Rice. "
                 "She scored a perfect 30 for her week 5 samba."),
        dict(
            q="When did Stacy Keibler leave WWE?",
            a="In July 2006. She took time off for Dancing with the Stars, and on July 21, 2006 she "
              "posted that her WWE contract &ldquo;has come to an end&rdquo; and that she had signed "
              "a development deal with Touchstone TV.",
            q_ld="When did Stacy Keibler leave WWE?",
            a_ld="Stacy Keibler left WWE in July 2006. On July 21, 2006 she announced that her WWE "
                 "contract had ended and that she had signed a development deal with Touchstone TV "
                 "to pursue acting."),
        dict(
            q="What was Stacy Keibler's last match?",
            a="A loss to Jillian Hall on <b>Velocity</b>, which Cagematch dates to October 25, "
              "2005. Her last match on a pay-per-view was the Taboo Tuesday battle royal on October "
              "19, 2004.",
            q_ld="What was Stacy Keibler's last wrestling match?",
            a_ld="Stacy Keibler's last match was a loss to Jillian Hall on WWE Velocity, dated "
                 "October 25, 2005 by Cagematch. Her last pay-per-view match was the women's battle "
                 "royal at Taboo Tuesday on October 19, 2004."),
        dict(
            q="What was Stacy Keibler's entrance theme?",
            a="<b>Legs</b>, Kid Rock's cover of the ZZ Top song, released on the WWF Forceable "
              "Entry album on March 26, 2002. WWE 2K26 brought it back as her entrance music.",
            q_ld="What was Stacy Keibler's entrance theme?",
            a_ld="Stacy Keibler's entrance theme was Legs, a Kid Rock cover of the ZZ Top song, "
                 "released on the WWF Forceable Entry album in 2002. It is also her entrance music "
                 "in WWE 2K26."),
        dict(
            q="Who is Stacy Keibler married to?",
            a="Jared Pobre. They married in Mexico on March 8, 2014, have three children, and "
              "co-founded the men's skincare brand Caldera + Lab. Before that she dated actor "
              "George Clooney from 2011 to 2013.",
            q_ld="Who is Stacy Keibler married to?",
            a_ld="Stacy Keibler has been married to Jared Pobre since March 8, 2014. They have "
                 "three children and co-founded the men's skincare brand Caldera + Lab."),
        dict(
            q="Is Stacy Keibler coming back to WWE?",
            a="Nothing is announced. She has not wrestled since 2005. Her WWE appearances since "
              "leaving were Tough Enough in 2011, inducting Torrie Wilson in 2019 and her own Hall "
              "of Fame induction in 2023. As of November 9, 2026 her current WWE presence is as a "
              "playable legend in WWE 2K26.",
            q_ld="Is Stacy Keibler returning to WWE in 2026?",
            a_ld="No return has been announced as of November 9, 2026. Stacy Keibler has not "
                 "wrestled since 2005. Her later WWE appearances were Tough Enough in 2011, "
                 "inducting Torrie Wilson into the Hall of Fame in 2019, and her own induction in "
                 "2023. She is playable in WWE 2K26."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Stacy Ann-Marie Keibler"),
        dict(label="Born", value="October 14, 1979",
             sub="Rosedale, Maryland &middot; Cagematch says Baltimore"),
        dict(label="Billed from", value="Baltimore, Maryland"),
        dict(label="Height", value="5&#8242;11&#8243;", sub="180 cm &middot; WWE.com and Cagematch agree"),
        dict(label="Weight", value="136 lb", sub="62 kg billed &middot; Cagematch lists 134 lb"),
        dict(label="WCW start", value="November 8, 1999", sub="won the Nitro Girl Search on Nitro"),
        dict(label="WWF debut", value="June 14, 2001", sub="SmackDown, after the WCW sale"),
        dict(label="Last match", value="October 2005",
             sub="L to Jillian Hall, Velocity &middot; Cagematch date October 25"),
        dict(label="Left WWE", value="July 2006", sub="contract ended; Touchstone TV deal"),
        dict(label="Signature move", value="Roundhouse kick", sub="per WWE.com"),
        dict(label="Hall of Fame", value="Class of 2023", sub="inducted by Mick Foley and Torrie Wilson"),
        dict(label="Also known as", value="Skye &middot; Miss Hancock &middot; Super Stacy"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1979-10-14",
    bornplace="Rosedale, Maryland, United States",
    nationality="United States",
    height_cm=180,
    weight_kg=62,
    ld=dict(
        alternateName=["Stacy Ann-Marie Keibler", "Skye", "Miss Hancock", "Super Stacy",
                       "The Duchess of Dudleyville", "The Legs of WWE"],
        award=["WWE Hall of Fame (Class of 2023)",
               "WCW Nitro Girl Search winner (1999)",
               "Dancing with the Stars season 2, third place (2006)"],
        knowsAbout=["Professional wrestling", "WWE", "WCW", "Wrestling valets and managers",
                    "Dance", "Television acting"],
        description="Stacy Keibler is an American former professional wrestling valet and wrestler, "
                    "actress and model. She won WCW's Nitro Girl Search in 1999, worked in WCW as "
                    "Skye and Miss Hancock, and spent 2001 to 2006 in WWF/WWE managing the Dudley "
                    "Boyz, Test and Scott Steiner and challenging for the Women's Championship. She "
                    "finished third on Dancing with the Stars season 2 in 2006 and was inducted into "
                    "the WWE Hall of Fame in 2023.",
        sameAs=["https://en.wikipedia.org/wiki/Stacy_Keibler",
                "https://www.wwe.com/superstars/stacykeibler",
                "https://www.cagematch.net/?id=2&nr=606"],
    ),
)
