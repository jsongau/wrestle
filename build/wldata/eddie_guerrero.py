# -*- coding: utf-8 -*-
"""Eddie Guerrero - dossier data. MEMORIAL MODULE.

Eddie Guerrero died on November 13, 2005. Nothing on this page frames him as active;
the "now" fields carry legacy, and the tone follows the site's standard for legends
who have passed - factual and warm, no mawkishness.

Sources: web-verified August 31, 2026 (Wikipedia, Slam Wrestling, Sports Illustrated,
Wikipedia's No Way Out 2004 and WWE Hall of Fame 2006 pages). Every match row carries
a day-precision date confirmed in those sources.

Deliberate omissions:
  * No career win-loss total - none exists in a verified form.
  * No Meltzer star ratings in the signature block - not verified in this pass, so
    the column is published blank rather than guessed at.
  * His final match is dated to the November 11, 2005 SmackDown broadcast, as
    Wikipedia dates it; the episode was taped earlier that week, and the taping date
    was not separately verified, so only the broadcast date is published.
"""

# ----------------------------------------------------------------- record rows
# 15 documented bouts across AAA, ECW, WCW and WWE - the title changes, the two
# canonical Rey Mysterio matches, and the last one.
ROWS = [
    dict(result="L", date="1994-11-06", promo="AAA", landmark=True, type="tag",
         event="When Worlds Collide — Los Angeles", opponent="El Hijo del Santo & Octagon",
         stip="Hair vs. mask — with Art Barr, as La Pareja del Terror", title=""),
    dict(result="W", date="1995-04-08", promo="ECW",
         event="Three Way Dance — Philadelphia", opponent="2 Cold Scorpio",
         stip="Singles — first US singles gold", title="ECW World Television Championship"),
    dict(result="W", date="1996-12-29", promo="WCW", landmark=True,
         event="Starrcade", opponent="Diamond Dallas Page",
         stip="Tournament final", title="WCW United States Heavyweight Championship"),
    dict(result="W", date="1997-09-14", promo="WCW",
         event="Fall Brawl", opponent="Chris Jericho",
         stip="Singles", title="WCW Cruiserweight Championship"),
    dict(result="L", date="1997-10-26", promo="WCW", landmark=True,
         event="Halloween Havoc — Las Vegas", opponent="Rey Mysterio Jr.",
         stip="Title vs. mask — the canonical cruiserweight match",
         title="WCW Cruiserweight Championship"),
    dict(result="W", date="2000-04-03", promo="WWE",
         event="Raw", opponent="Chris Jericho",
         stip="Singles — Latino Heat and Mamacita arrive", title="WWF European Championship"),
    dict(result="W", date="2002-04-21", promo="WWE",
         event="Backlash", opponent="Rob Van Dam",
         stip="Singles — three weeks into the second WWE run",
         title="WWE Intercontinental Championship"),
    dict(result="W", date="2002-11-17", promo="WWE", type="tag",
         event="Survivor Series — New York", opponent="Edge & Rey Mysterio; Kurt Angle & Chris Benoit",
         stip="Triple threat elimination — Los Guerreros, with Chavo",
         title="WWE Tag Team Championship"),
    dict(result="W", date="2003-07-27", promo="WWE",
         event="Vengeance", opponent="Chris Benoit",
         stip="Tournament final for the revived title", title="WWE United States Championship"),
    dict(result="W", date="2004-02-15", promo="WWE", landmark=True,
         event="No Way Out — Daly City", opponent="Brock Lesnar",
         stip="Singles — frog splash after a Goldberg spear; the summit", title="WWE Championship"),
    dict(result="W", date="2004-03-14", promo="WWE", landmark=True,
         event="WrestleMania XX — Madison Square Garden", opponent="Kurt Angle",
         stip="Singles — retains by untying his boot to slip the ankle lock", title="WWE Championship"),
    dict(result="L", date="2004-06-27", promo="WWE",
         event="The Great American Bash", opponent="JBL",
         stip="Texas bullrope match — the reign ends on a contested finish", title="WWE Championship"),
    dict(result="W", date="2005-02-20", promo="WWE", type="tag",
         event="No Way Out", opponent="The Basham Brothers",
         stip="Tag — with Rey Mysterio", title="WWE Tag Team Championship"),
    dict(result="L", date="2005-08-21", promo="WWE", landmark=True,
         event="SummerSlam", opponent="Rey Mysterio",
         stip="Ladder match — custody of Dominik hung above the ring", title=""),
    dict(result="W", date="2005-11-11", promo="WWE", landmark=True,
         event="SmackDown", opponent="Mr. Kennedy",
         stip="Singles — his final match, two days before his death", title=""),
]

DATA = dict(
    slug="eddie-guerrero",
    name="Eddie Guerrero",
    realname="Eduardo Gory Guerrero Llanes",
    epithet="Latino Heat",
    hook="Legacy & Titles",

    meta_desc=("Eddie Guerrero, Latino Heat, beat Brock Lesnar for the WWE Championship in 2004 and "
               "died on November 13, 2005 at 38. WWE Hall of Fame Class of 2006. Full record, "
               "titles, the Guerrero dynasty and a legacy still visible on every WWE show."),
    og_desc=("Latino Heat: from the Guerrero dynasty of El Paso through ECW, WCW and the 2004 WWE "
             "Championship, to a Hall of Fame legacy carried on by Rey, Chavo and Dominik. "
             "1967-2005."),
    tw_desc="Eddie Guerrero, 1967-2005: WWE Champion, Hall of Famer, the standard for making every second count.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1986",
    height_imp="5&#8242;8&#8243;",
    weight_lb="220",
    world_titles="1",
    vitals_tagline="I lie, I cheat, I steal",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="EG", title="WWE Shop", sub="Legends tees · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="A playable legend across the 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="PT", title="The Players' Tribune", sub="Rey Mysterio's 2025 letter to Eddie",
             tag="Read", href="https://www.theplayerstribune.com/"),
        dict(ic="W", title="Wikipedia", sub="Full biography", tag="Read", charity=True,
             href="https://en.wikipedia.org/wiki/Eddie_Guerrero"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Latino Heat &middot; Black Tiger &middot; Los Guerreros &middot; Viva La Raza",
    hero_tag="El Paso, Texas &middot; <em>CMLL &middot; AAA &middot; NJPW &middot; ECW &middot; WCW "
             "&middot; WWE &middot; 1986&ndash;2005</em>",
    now_label="LEGACY",
    now_bold="WWE Hall of Fame, Class of 2006",
    now_tail=(" &middot; died November 13, 2005, at 38 &middot; twenty years on, the frog splash, "
              "the Three Amigos and the lying-cheating-stealing playbook are still all over WWE "
              "television, most visibly in Rey and Dominik Mysterio's work"),
    hstats=[
        dict(value="1",  x=False, label="WWE Championship"),
        dict(value="4",  x=False, label="WWE Tag Reigns"),
        dict(value="2006", x=False, label="Hall of Fame"),
        dict(value="38", x=True,  label="Years, 1967-2005"),
    ],
    ghost_link="From the Guerrero dynasty of El Paso to the top of WrestleMania XX",
    vlabel="1967&ndash;2005 &middot; El Paso, Texas",
    mono="EG",

    # ---------------------------------------------------------------- 01 overview
    correction=2,
    overview=[
        "<b>Eddie Guerrero</b> beat Brock Lesnar for the WWE Championship at No Way Out on February "
        "15, 2004 &mdash; a 5&#8242;8&#8243; second-generation luchador pinning a 295-pound former "
        "NCAA champion with a frog splash &mdash; and for the twenty months between that night and "
        "his death on November 13, 2005, he was the best all-around performer in the company. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">2004</span>'
        '<span class="pull-cap">WWE Champion &mdash; the frog splash on Brock Lesnar at No Way Out, February 15</span></span>'
        "He was the youngest son of the Guerrero wrestling dynasty of El Paso &mdash; Gory "
        "Guerrero&rsquo;s boy, brother to Chavo Sr., Mando and Hector, uncle to Chavo Jr. &mdash; "
        "and he worked everywhere that mattered: CMLL and AAA in Mexico, New Japan as the second "
        "Black Tiger, ECW, WCW, and finally WWE, where the character built from his real flaws "
        "&mdash; the liar, the cheat, the thief you loved anyway &mdash; became one of the most "
        "durable acts the company has produced.",

        "The resume is deeper than the one title. He and Art Barr headlined AAA&rsquo;s When Worlds "
        "Collide in Los Angeles on November 6, 1994, losing their hair to El Hijo del Santo and "
        "Octagon in the match that showed American promoters what lucha libre could draw. He won "
        "the ECW World Television Championship twice in 1995, and his farewell series with Dean "
        "Malenko is part of ECW legend. In WCW he took the United States Championship at Starrcade "
        "1996 and the Cruiserweight Championship twice, and his title-versus-mask loss to Rey "
        "Mysterio Jr. at Halloween Havoc on October 26, 1997 is still the standard answer to "
        "&ldquo;best cruiserweight match ever televised in America.&rdquo; In WWE he won the "
        "European, Intercontinental and United States Championships, four WWE Tag Team Championship "
        "reigns &mdash; two with Chavo as Los Guerreros, one each with Tajiri and Rey Mysterio "
        "&mdash; and the WWE Championship he defended against Kurt Angle at WrestleMania XX by "
        "untying his own boot to escape the ankle lock.",

        "One framing needs correcting, gently: Eddie did not main-event WrestleMania XX, and the "
        "famous image from that night is not from his match. He retained the WWE Championship "
        "against Kurt Angle earlier on the card on March 14, 2004; the main event was Chris "
        "Benoit&rsquo;s, and the closing scene &mdash; Eddie and Benoit embracing in the confetti "
        "at Madison Square Garden, two friends who had driven the roads together holding both world "
        "titles &mdash; came after it. The moment is remembered as the era&rsquo;s emotional peak, "
        "and it is also remembered differently now than it was then; this page states the facts and "
        "leaves them there. Eddie&rsquo;s reign ended against JBL in a Texas bullrope match at The "
        "Great American Bash on June 27, 2004, on a finish contested enough that it needed a "
        "restart decision, and he never held a world title again &mdash; his last shot was against "
        "Batista at No Mercy on October 9, 2005, his 38th birthday.",

        "He died in his Minneapolis hotel room on November 13, 2005, found by Chavo, of acute "
        "heart failure linked to cardiovascular disease &mdash; two days after beating Mr. Kennedy "
        "on the November 11 SmackDown, and roughly four years into a sobriety he spoke about "
        "constantly; he had been public about the addictions that got him fired from WWE in 2001 "
        "and about the recovery that brought him back. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">20</span>'
        '<span class="pull-cap">years of tributes &mdash; and the frog splash still wins matches on WWE television</span></span>'
        "WWE aired tribute shows on November 14 and 18, and inducted him into the Hall of Fame on "
        "April 1, 2006, with Chris Benoit, Rey Mysterio and Chavo handling the induction. The "
        "legacy is not archival; it is on television weekly. Rey Mysterio dedicated his 2006 world "
        "title win to him and, on the 20th anniversary in November 2025, published a letter to "
        "Eddie at The Players&rsquo; Tribune. Chavo carried the family name across every major "
        "promotion. And Dominik Mysterio &mdash; the boy from the 2005 custody storyline &mdash; "
        "built his heel career explicitly on Eddie&rsquo;s playbook, down to winning at SummerSlam "
        "2025 with a faked chair shot, a loose boot and a frog splash.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["AAA", "ECW", "WCW", "WWE"],
        promo_labels={"AAA": "AAA", "ECW": "ECW", "WCW": "WCW", "WWE": "WWE"},
        stats=[
            ("1",        "WWE Championship"),
            ("4",        "WWE tag reigns"),
            ("2&times;", "WCW Cruiserweight"),
            ("2&times;", "ECW Television"),
            ("2",        "US titles (WCW & WWE)"),
            ("1996",     "Best of the Super Juniors"),
        ],
        lead=("Fifteen documented bouts across four promotions and eleven years &mdash; the title "
              "changes, the two canonical Rey Mysterio matches, and the final SmackDown win over "
              "Mr. Kennedy. A curated ledger, not a career count; no career win&ndash;loss total is "
              "published because no verified one exists. His Mexico and Japan records are "
              "represented by the When Worlds Collide match only, because those are the rows this "
              "pass could date to the day. Filter by match type, tap any column header to sort, and "
              "turn spoilers on to reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The bouts the reputation rests on. Star ratings are deliberately not "
                    "published: Observer figures for these matches were not verified in this pass, "
                    "and this page does not guess at numbers."),
    signature=[
        dict(rating="&mdash;", event="Halloween Havoc 1997", opponent="Rey Mysterio Jr.",
             stip="WCW Cruiserweight Championship vs. mask"),
        dict(rating="&mdash;", event="When Worlds Collide 1994", opponent="El Hijo del Santo & Octagon",
             stip="Hair vs. mask, with Art Barr — AAA's American breakthrough"),
        dict(rating="&mdash;", event="No Way Out 2004", opponent="Brock Lesnar",
             stip="WWE Championship — the summit"),
        dict(rating="&mdash;", event="WrestleMania XX", opponent="Kurt Angle",
             stip="WWE Championship — the untied boot"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("1", "WWE Championship"),
            ("4", "WWE tag reigns"),
            ("2&times;", "WCW Cruiserweight"),
            ("5", "Promotions with gold"),
        ],
        lead=("Championships in AAA, ECW, WCW and WWE, spread across every weight class he was "
              "allowed into. Independent and Mexican reign dates beyond those stated were not "
              "verified in this pass and are not invented here."),
        rows=[
            dict(ic="C", name="WWE Championship", count="1",
                 sub="February 15, 2004 &ndash; June 27, 2004 &middot; won from Brock Lesnar at No "
                     "Way Out, retained against Kurt Angle at WrestleMania XX, lost to JBL in a "
                     "Texas bullrope match at The Great American Bash &middot; the first "
                     "Mexican-American WWE Champion, a framing WWE itself uses"),
            dict(ic="T", name="WWE Tag Team Championship", count="4",
                 sub="Two reigns as Los Guerreros with Chavo (from Survivor Series 2002), one with "
                     "Tajiri (Judgment Day 2003 ladder match), one with Rey Mysterio (No Way Out "
                     "2005)"),
            dict(ic="U", name="WWE United States Championship", count="1",
                 sub="July 27, 2003, beating Chris Benoit in the tournament final at Vengeance to "
                     "become the revived title&rsquo;s first champion"),
            dict(ic="I", name="WWE Intercontinental Championship", count="2",
                 sub="September 2000, and again at Backlash on April 21, 2002 from Rob Van Dam, "
                     "three weeks after his return"),
            dict(ic="E", name="WWF European Championship", count="1",
                 sub="April 3, 2000, from Chris Jericho on Raw &mdash; the night Latino Heat and "
                     "Mamacita entered the vocabulary"),
            dict(ic="X", name="WCW United States Heavyweight Championship", count="1",
                 sub="Starrcade, December 29, 1996, over Diamond Dallas Page in the tournament final"),
            dict(ic="V", name="WCW Cruiserweight Championship", count="2",
                 sub="Fall Brawl 1997 from Chris Jericho; regained November 10, 1997 from Rey "
                     "Mysterio Jr., two weeks after losing the Halloween Havoc mask match"),
            dict(ic="D", name="ECW World Television Championship", count="2",
                 sub="April 8, 1995 from 2 Cold Scorpio, and again that July &mdash; his ECW run "
                     "lasted barely five months and is still talked about"),
            dict(ic="A", name="AAA World Tag Team Championship", count="1",
                 sub="With Art Barr, 1994, as La Pareja del Terror &mdash; the most hated team in "
                     "Mexico, by design"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="Family first, always &mdash; even the groups that were not family were about family.",
        cards=[
            dict(era="AAA &middot; 1992&ndash;1994",
                 name="La Pareja del Terror / Los Gringos Locos",
                 members="Eddie Guerrero, Art Barr (with Konnan, Chicano Power and others in the "
                         "wider Gringos Locos unit)",
                 desc="The great heel act of early-90s Mexico: a Mexican-American and a gringo "
                      "playing anti-Mexico villains so effectively that the hair-vs-mask loss to El "
                      "Hijo del Santo and Octagon headlined When Worlds Collide on November 6, "
                      "1994. Barr died three weeks after that match; Eddie carried the frog splash "
                      "for the rest of his career in tribute."),
            dict(era="WCW &middot; 1998&ndash;1999",
                 name="Latino World Order",
                 members="Eddie Guerrero, and most of WCW's Latino roster",
                 desc="Founded in October 1998 as an nWo parody with a real grievance under it — "
                      "Eddie's on-screen complaint about WCW wasting its Latino talent was barely a "
                      "work. Short-lived, dissolved around his 1999 car-accident recovery, and "
                      "affectionately revived by WWE storylines decades later."),
            dict(era="WWE &middot; 2000, and 2002&ndash;2004",
                 name="The Radicalz, then Los Guerreros",
                 members="Eddie Guerrero, Chris Benoit, Dean Malenko, Perry Saturn; later Eddie & "
                         "Chavo Guerrero",
                 desc="The Radicalz jumped from WCW together on January 31, 2000 and changed the "
                      "in-ring standard of the main roster on arrival. Los Guerreros, with Chavo "
                      "from 2002, turned the family shtick into gold — 'We lie, we cheat, we "
                      "steal' started as a heel mission statement and became a babyface anthem, "
                      "which tells you everything about how the audience took to him."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="Four masks and names before the world knew his face: <b>Mascara Magica</b> (CMLL) "
             "&rarr; <b>Black Tiger II</b> (NJPW) &rarr; <b>Eddie Guerrero</b> everywhere else "
             "&mdash; and finally <b>Latino Heat</b>, the persona that was mostly just him, turned "
             "up.",
        cards=[
            dict(mono="MM", era="CMLL &middot; late 1980s&ndash;1992", name="Mascara Magica",
                 desc="The masked name in Mexico City, tagging with El Hijo del Santo as La Pareja "
                      "Atomica — the respectful lucha apprenticeship before the heel turn that made "
                      "him."),
            dict(mono="BT", era="NJPW &middot; 1992&ndash;1998", name="Black Tiger II",
                 desc="The second man under the Black Tiger hood, working New Japan's junior "
                      "division against Jushin Thunder Liger, Wild Pegasus and the class of the "
                      "era. He won the 1996 Best of the Super Juniors under it."),
            dict(mono="LH", era="WWE &middot; 2000&ndash;2005", name="Latino Heat",
                 desc="Charming, jealous, larcenous — the character born in the Chyna storyline and "
                      "perfected on SmackDown: lowriders, the Three Amigos, lie-cheat-steal "
                      "finishes where the referee never saw a thing. WWE's shorthand for a whole "
                      "style of babyface cheating is still, functionally, 'doing an Eddie.'"),
            dict(mono="VLR", era="2004&ndash;2005", name="Viva La Raza",
                 desc="The championship-era Eddie: the same act with the weight of representation "
                      "on it. He talked openly about sobriety, faith and family, and the "
                      "El Paso-to-title-belt arc — told in his autobiography Cheating Death, "
                      "Stealing Life — is why the reign meant more than its 112 days."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Gory Guerrero's youngest son to WWE Champion, in nineteen working years.",
        rows=[
            dict(year="1986", title="Debut in the family business",
                 desc="Trained by his father Gory Guerrero and his brothers, debuts in Mexico while "
                      "still studying at New Mexico Highlands University."),
            dict(year="1994", title="When Worlds Collide",
                 desc="Headlines AAA's Los Angeles breakthrough show on November 6 with Art Barr, "
                      "losing hair to El Hijo del Santo and Octagon. Barr dies weeks later; Eddie "
                      "adopts the frog splash permanently."),
            dict(year="1995", title="ECW, then WCW",
                 desc="Two ECW Television Championship reigns and the Malenko series in five "
                      "months; WCW signs him before the year is out."),
            dict(year="1997", title="The Halloween Havoc match",
                 desc="Drops the Cruiserweight Championship to Rey Mysterio Jr. in the "
                      "title-vs-mask match on October 26 — the match a generation of smaller "
                      "wrestlers points to."),
            dict(year="1999", title="The car accident",
                 desc="Falls asleep at the wheel on New Year's Day and nearly dies. The painkiller "
                      "addiction that follows shapes the next four years."),
            dict(year="2000", title="The Radicalz jump",
                 desc="Arrives in WWF on January 31 with Benoit, Malenko and Saturn; wins the "
                      "European and Intercontinental titles and becomes Latino Heat."),
            dict(year="2001", title="Fired",
                 desc="Released on November 12, 2001 amid addiction problems — the low point he "
                      "spoke about openly for the rest of his life."),
            dict(year="2002", title="The comeback",
                 desc="Returns clean on April 1, wins the Intercontinental Championship from Rob "
                      "Van Dam at Backlash within three weeks, then builds Los Guerreros with "
                      "Chavo."),
            dict(year="2004", title="The top of the mountain",
                 desc="Beats Brock Lesnar for the WWE Championship at No Way Out on February 15, "
                      "retains against Kurt Angle at WrestleMania XX on March 14, and shares the "
                      "confetti with Chris Benoit. Loses the title to JBL on June 27."),
            dict(year="2005", title="The Rey feud, and the end",
                 desc="The custody-of-Dominik storyline peaks in the SummerSlam ladder match on "
                      "August 21; a face turn and a last title shot against Batista follow. He "
                      "beats Mr. Kennedy on the November 11 SmackDown and dies in Minneapolis on "
                      "November 13, at 38."),
            dict(year="2006", title="Hall of Fame",
                 desc="Inducted April 1, 2006 by Chris Benoit, Rey Mysterio and Chavo. Rey "
                      "dedicates his WrestleMania 22 world title win to him."),
            dict(year="2025", title="Twenty years on",
                 desc="Rey Mysterio publishes a letter to Eddie at The Players' Tribune on November "
                      "13, 2025; Dominik Mysterio's whole championship act — down to a SummerSlam "
                      "win built on a faked chair shot and a frog splash — runs on Eddie's "
                      "playbook."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with &mdash; and in this career, war and love kept trading places.",
        cards=[
            dict(name="Rey Mysterio", slug="rey-mysterio",
                 desc="The defining opposite number, twice. Halloween Havoc 1997 was the perfect "
                      "athletic version; the 2005 feud — built on the claim that Eddie, not Rey, "
                      "was Dominik's biological father, with custody hung above a SummerSlam ladder "
                      "on August 21, 2005 — was the ugly soap-opera version, and Eddie played the "
                      "villain of it brilliantly. Rey has spent twenty years honouring him for "
                      "both."),
            dict(name="Brock Lesnar",
                 desc="One night, February 15, 2004, and the most-cited underdog title win of its "
                      "era: the Goldberg spear, the DDT, the frog splash, and a champion who "
                      "wept with the belt because everyone watching knew what the road there had "
                      "been."),
            dict(name="Kurt Angle",
                 desc="The technician-versus-trickster pairing. The WrestleMania XX defense on "
                      "March 14, 2004, won by untying his own boot to slide out of the ankle lock, "
                      "is the single cleanest expression of the character ever filmed. Angle has "
                      "called him one of the greatest of all time."),
            dict(name="JBL",
                 desc="The 2004 feud that ended the reign — a bloody Judgment Day match and the "
                      "Texas bullrope finish at The Great American Bash on June 27 that took the "
                      "title on a reversed-decision technicality. The blood loss at Judgment Day "
                      "remains one of the era's most infamous images."),
            dict(name="Chris Benoit",
                 desc="Friend, travel partner, Radicalz co-founder, and the other half of the "
                      "WrestleMania XX confetti scene on March 14, 2004 — an image the industry "
                      "now views through everything learned in 2007. Their 2003 United States "
                      "Championship tournament final at Vengeance was the on-screen version of a "
                      "twenty-year friendly argument."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Memory",
        lead="The record of him &mdash; what he made, and what has been made about him.",
        rows=[
            dict(when="2005", title="Cheating Death, Stealing Life: The Eddie Guerrero Story", kind="Book",
                 desc="His autobiography, published months before his death — unusually frank about "
                      "addiction, the 1999 car accident, the firing and the recovery."),
            dict(when="2004", title="Viva La Raza: The Legacy of Eddie Guerrero", kind="Video",
                 desc="WWE's career retrospective DVD set, built around the title win."),
            dict(when="2005&ndash;", title="Tribute shows and anniversaries", kind="Television",
                 desc="Raw on November 14 and SmackDown on November 18, 2005 were full tribute "
                      "episodes. Every November since brings on-air acknowledgments, and the 20th "
                      "anniversary in 2025 brought a wave of them, led by Rey Mysterio's Players' "
                      "Tribune letter."),
            dict(when="2004&ndash;", title="WWE 2K series", kind="Game",
                 desc="A recurring playable legend in WWE's games, frog splash and lowrider "
                      "entrance included."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The marks he left, stated plainly.",
        stats=[
            ("1",    "WWE Championship"),
            ("2006", "Hall of Fame"),
            ("4",    "Promotions with major gold"),
        ],
        rows=[
            dict(name="WWE Champion, February 15 to June 27, 2004",
                 sub="Won from Brock Lesnar at No Way Out with a frog splash after a Goldberg "
                     "spear; retained against Kurt Angle at WrestleMania XX; lost to JBL in a "
                     "Texas bullrope match. WWE frames him as the first Mexican-American WWE "
                     "Champion."),
            dict(name="WWE Hall of Fame, Class of 2006",
                 sub="Inducted April 1, 2006 in Rosemont, alongside Bret Hart's class, by Chris "
                     "Benoit, Rey Mysterio and Chavo Guerrero — the first posthumous induction of "
                     "the modern annual ceremony era. Also honoured by AAA's hall, the Hardcore "
                     "Hall of Fame and the Wrestling Observer Newsletter Hall of Fame."),
            dict(name="Champion in AAA, ECW, WCW and WWE",
                 sub="Tag gold in Mexico with Art Barr, two ECW Television reigns, the WCW United "
                     "States and Cruiserweight titles, and eleven championships in WWF/WWE across "
                     "two runs."),
            dict(name="Best of the Super Juniors winner, 1996",
                 sub="As Black Tiger II in New Japan — part of the junior heavyweight class that "
                     "reshaped two continents' idea of what smaller wrestlers could headline."),
            dict(name="The Halloween Havoc standard",
                 sub="The October 26, 1997 title-vs-mask match with Rey Mysterio Jr. is still the "
                     "reference point for televised cruiserweight wrestling in America."),
            dict(name="A playbook still in weekly use",
                 sub="The frog splash, the Three Amigos, and the fake-the-foul chair spot are "
                     "living moves in WWE — Dominik Mysterio retained the Intercontinental "
                     "Championship at SummerSlam 2025 with a match built entirely of Eddie "
                     "references, boot escape and frog splash included."),
        ],
        footnote=("Deliberately absent: a career win-loss total, star ratings, and any invented "
                  "precision about his Mexico and Japan reigns — dates this pass could not verify "
                  "to the day are described in prose rather than tabulated. His final match is "
                  "dated to the November 11, 2005 broadcast, with the taping-date caveat noted in "
                  "the module header."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Eddie_Guerrero"),
        dict(k="Wikipedia", v="No Way Out 2004 — the title win",
             href="https://en.wikipedia.org/wiki/No_Way_Out_(2004)"),
        dict(k="Wikipedia", v="WWE Hall of Fame Class of 2006",
             href="https://en.wikipedia.org/wiki/WWE_Hall_of_Fame_(2006)"),
        dict(k="Slam Wrestling", v="Rey Mysterio honours Eddie, 20 years on (Nov 13, 2025)",
             href="https://slamwrestling.net/news/rey-mysterio-honours-eddie-guerrero/"),
        dict(k="Sports Illustrated", v="Dominik's Eddie-tribute win at SummerSlam 2025",
             href="https://www.si.com/fannation/wrestling/wwe/dominik-mysterio-retains-wwe-ic-championship-at-wwe-summerslam-2025"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="How did Eddie Guerrero die?",
            a="He was found unconscious by his nephew Chavo in his Minneapolis hotel room on the "
              "morning of November 13, 2005, and could not be revived. The cause was acute heart "
              "failure resulting from underlying cardiovascular disease; his widow Vickie has said "
              "the years of earlier substance abuse contributed to the heart condition, even "
              "though he had been publicly, proudly sober for roughly four years. He was 38, and "
              "had wrestled &mdash; and won &mdash; on SmackDown two days earlier.",
            q_ld="How did Eddie Guerrero die?",
            a_ld="Eddie Guerrero died on November 13, 2005, in Minneapolis, Minnesota, where he "
                 "was found unconscious in his hotel room by his nephew Chavo Guerrero. The cause "
                 "of death was acute heart failure due to underlying atherosclerotic "
                 "cardiovascular disease. He was 38 years old and had wrestled his final match, a "
                 "win over Mr. Kennedy, on the SmackDown broadcast of November 11, 2005."),
        dict(
            q="Was Eddie Guerrero WWE Champion, and for how long?",
            a="Yes, once &mdash; from February 15, 2004, when he pinned Brock Lesnar at No Way Out "
              "with a frog splash after Goldberg&rsquo;s interference, to June 27, 2004, when JBL "
              "took the title in a Texas bullrope match at The Great American Bash. In between he "
              "retained against Kurt Angle at WrestleMania XX by untying his boot to escape the "
              "ankle lock &mdash; the most Eddie finish imaginable. WWE frames him as the first "
              "Mexican-American WWE Champion.",
            q_ld="Was Eddie Guerrero ever WWE Champion?",
            a_ld="Yes. Eddie Guerrero held the WWE Championship once, from February 15, 2004, when "
                 "he defeated Brock Lesnar at No Way Out, until June 27, 2004, when he lost it to "
                 "JBL in a Texas bullrope match at The Great American Bash. During the reign he "
                 "retained the title against Kurt Angle at WrestleMania XX. WWE recognises him as "
                 "the first Mexican-American WWE Champion."),
        dict(
            q="Is Eddie Guerrero in the WWE Hall of Fame?",
            a="Yes &mdash; Class of 2006, inducted on April 1, 2006 in Rosemont, Illinois, the "
              "night before WrestleMania 22, in the same class as Bret Hart. Chris Benoit, Rey "
              "Mysterio and Chavo Guerrero handled the induction. He is also in the Wrestling "
              "Observer Newsletter Hall of Fame, AAA&rsquo;s hall, and the Hardcore Hall of Fame.",
            q_ld="Is Eddie Guerrero in the WWE Hall of Fame?",
            a_ld="Yes. Eddie Guerrero was inducted into the WWE Hall of Fame as part of the Class "
                 "of 2006, at the ceremony on April 1, 2006 in Rosemont, Illinois. He was inducted "
                 "by Chris Benoit, Rey Mysterio and Chavo Guerrero. He is also a member of the "
                 "Wrestling Observer Newsletter Hall of Fame and AAA's hall of fame."),
        dict(
            q="Why does Dominik Mysterio use the frog splash?",
            a="As a living tribute-slash-inheritance. Dominik is the child at the centre of the "
              "2005 Eddie&ndash;Rey custody storyline, and his modern heel act leans into the idea "
              "that he is &ldquo;Eddie&rsquo;s boy&rdquo; in spirit: frog splash finisher, "
              "lie-cheat-steal tactics, and a SummerSlam 2025 Intercontinental title defense "
              "against AJ Styles built almost entirely of Eddie spots &mdash; the faked chair "
              "shot, a loose-boot escape echoing WrestleMania XX, then the frog splash. Rey wrote "
              "in his 2025 anniversary letter that Eddie would have loved what Dominik has become "
              "in the ring.",
            q_ld="Why does Dominik Mysterio use Eddie Guerrero's frog splash?",
            a_ld="Dominik Mysterio uses the frog splash as a tribute to Eddie Guerrero, who was at "
                 "the centre of the 2005 WWE custody storyline involving Dominik as a child. "
                 "Dominik's heel character draws directly on Guerrero's lie-cheat-steal style; at "
                 "SummerSlam 2025 he retained the Intercontinental Championship against AJ Styles "
                 "with a match full of Guerrero references, including a faked chair shot and a "
                 "frog splash. Eddie himself adopted the frog splash in tribute to his late tag "
                 "team partner Art Barr."),
        dict(
            q="What was Eddie Guerrero&rsquo;s last match?",
            a="A win over Mr. Kennedy on the SmackDown broadcast of November 11, 2005 &mdash; two "
              "days before his death. The episode was taped earlier that week, as SmackDown was; "
              "this page publishes the broadcast date and notes the caveat rather than guessing "
              "at the taping date. His last pay-per-view match was the World Heavyweight "
              "Championship challenge against Batista at No Mercy on October 9, 2005, his 38th "
              "birthday.",
            q_ld="What was Eddie Guerrero's last match?",
            a_ld="Eddie Guerrero's final match was a victory over Mr. Kennedy on the SmackDown "
                 "episode broadcast on November 11, 2005, two days before his death on November "
                 "13. His final pay-per-view match was a World Heavyweight Championship challenge "
                 "against Batista at No Mercy on October 9, 2005, which was also his 38th "
                 "birthday."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Eduardo Gory Guerrero Llanes"),
        dict(label="Born", value="October 9, 1967", sub="El Paso, Texas"),
        dict(label="Died", value="November 13, 2005",
             sub="Minneapolis, Minnesota &middot; acute heart failure &middot; age 38"),
        dict(label="Billed from", value="El Paso, Texas"),
        dict(label="Height", value="5&#8242;8&#8243;", sub="173 cm"),
        dict(label="Weight", value="220 lb", sub="100 kg (billed)"),
        dict(label="Debut", value="1986", sub="Mexico, in the family promotion territory"),
        dict(label="Trained by", value="Gory Guerrero",
             sub="his father, alongside brothers Chavo Sr., Mando and Hector"),
        dict(label="Family", value="The Guerrero dynasty",
             sub="son of Gory &middot; uncle of Chavo Jr. &middot; married to Vickie Guerrero "
                 "&middot; father of Shaul, Sherilyn and Kaylie"),
        dict(label="Signature", value="Frog splash &middot; Three Amigos &middot; Lasso from El Paso",
             sub="the frog splash carried in tribute to Art Barr"),
        dict(label="Catchphrases", value="I lie, I cheat, I steal &middot; Viva La Raza"),
        dict(label="Hall of Fame", value="WWE Class of 2006",
             sub="inducted April 1, 2006 by Chris Benoit, Rey Mysterio and Chavo Guerrero"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1967-10-09",
    bornplace="El Paso, Texas, United States",
    nationality="United States",
    height_cm=173,
    weight_kg=100,
    ld=dict(
        alternateName=["Eduardo Gory Guerrero Llanes", "Latino Heat", "Black Tiger",
                       "Mascara Magica", "Eddy Guerrero"],
        award=["WWE Championship (1 reign, 2004)",
               "WWE Tag Team Championship (4 reigns)",
               "WWE United States Championship (1 reign)",
               "WWE Intercontinental Championship (2 reigns)",
               "WWF European Championship (1 reign)",
               "WCW United States Heavyweight Championship (1 reign)",
               "WCW Cruiserweight Championship (2 reigns)",
               "ECW World Television Championship (2 reigns)",
               "AAA World Tag Team Championship (1 reign, with Art Barr)",
               "Best of the Super Juniors winner (1996)",
               "WWE Hall of Fame (Class of 2006)",
               "Wrestling Observer Newsletter Hall of Fame"],
        knowsAbout=["Professional wrestling", "Lucha libre", "WWE", "WCW", "ECW", "AAA",
                    "New Japan Pro-Wrestling", "The Guerrero wrestling family"],
        description="Eddie Guerrero, born Eduardo Gory Guerrero Llanes in El Paso, Texas, was a "
                    "Mexican-American professional wrestler from the Guerrero dynasty. He held "
                    "championships in AAA, ECW, WCW and WWE, winning the WWE Championship from "
                    "Brock Lesnar at No Way Out on February 15, 2004 and defending it at "
                    "WrestleMania XX. He died of acute heart failure on November 13, 2005, at age "
                    "38, and was inducted into the WWE Hall of Fame in 2006. His frog splash and "
                    "lie-cheat-steal style remain touchstones in WWE, carried on by Rey and "
                    "Dominik Mysterio and Chavo Guerrero.",
        sameAs=["https://en.wikipedia.org/wiki/Eddie_Guerrero"],
    ),
)
