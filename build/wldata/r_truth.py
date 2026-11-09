# -*- coding: utf-8 -*-
"""R-Truth - dossier data.

Compiled November 9, 2026 from data/r-truth.md, which carries a URL for every
claim (Wikipedia's R-Truth, K-Kwik, 24/7 champions and TNA tag champions pages,
WWE.com profile, results and title history, Wrestling Inc, Fightful, POST
Wrestling, CBS Sports, Sports Illustrated, PWInsider, ClutchPoints/Yahoo,
WrestleTalk, TheSmackDownHotel). Built from the .md, not from memory.

Harvested from the old 186-word page: the March 20, 2026 tag title win with
Damian Priest and the real name, both verified. The old page still called him
the current champion; that reign ended August 14, 2026 and is corrected here.

Status as of November 9, 2026 (searched, not assumed): out of action with an
undisclosed injury since a referee stoppage against Damian Priest on the
October 16, 2026 SmackDown. He posted from hospital on October 19 that he was
OK and would be back. No return date is announced.

Deliberate omissions:
  * No Signature section. No star rating for any R-Truth match was verified in
    this pass, and this dossier does not invent editorial grades. The section
    is omitted and the numbering closes up (the generator handles it).
  * No live X pulse. Only one post was verified (October 19, 2026), which is
    quoted in the FAQ and the career timeline instead.
  * No Instagram link: no handle was verified. X (@RonKillings) is verified via
    the post Fightful embedded on October 19, 2026.
  * No Spotify player: no track id was verified for "What's Up?". The walk-out
    band ships listen links only, which is the band's designed fallback.
  * No career win-loss total. None was verified; record.total is the row count.
  * Rows without a sourced opponent (the vacant NWA tag title win in 2003, the
    2018 Mixed Match Challenge final, the last 24/7 reign) live in the titles
    and feats sections rather than as record rows with a guessed opponent.
"""

_LINK = {
    "AJ Styles": "aj-styles", "John Cena": "john-cena", "Damian Priest": "damian-priest",
    "Gunther": "gunther", "Samoa Joe": "samoa-joe", "Shinsuke Nakamura": "shinsuke-nakamura",
    "Finn Balor": "finn-balor", "Kane": "kane", "Daniel Bryan": "daniel-bryan",
    "Sting": "sting", "Kurt Angle": "kurt-angle", "The Rock": "the-rock",
    "Big Show": "big-show",
}

def _a(name):
    return '<a class="opp-link" href="/wrestlers/%s/">%s</a>' % (_LINK[name], name)

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="1999-11-06", promo="IND", landmark=True,
         event="NWA Wildside", opponent=_a("AJ Styles"), opponent_html=True,
         stip="Singles, as K-Krush. His first championship",
         title="NWA Wildside Television Championship"),
    dict(result="W", date="2001-02-03", promo="WWF",
         event="WWF, under the 24/7 rule", opponent="Raven",
         stip="Hardcore title win, lost to Crash Holly the same night",
         title="WWF Hardcore Championship"),
    dict(result="W", date="2002-08-07", promo="TNA", landmark=True,
         event="NWA-TNA Weekly PPV #8, Nashville", opponent="Ken Shamrock",
         stip="Singles, won with an Ace Crusher. First NWA world title",
         title="NWA World Heavyweight Championship"),
    dict(result="L", date="2002-11-20", promo="TNA",
         event="NWA-TNA Weekly PPV #22, Nashville", opponent="Jeff Jarrett",
         stip="Singles. A masked man's guitar shot ends the 105-day reign",
         title="NWA World Heavyweight Championship"),
    dict(result="W", date="2004-05-19", promo="TNA", type="tag", landmark=True,
         event="NWA-TNA Weekly PPV #95, Nashville",
         opponent="%s, Chris Harris & Raven" % _a("AJ Styles"), opponent_html=True,
         stip="Four-way. Second NWA world title, won with a diving axe kick",
         title="NWA World Heavyweight Championship"),
    dict(result="L", date="2004-06-02", promo="TNA", type="tag",
         event="NWA-TNA Weekly PPV #97, Nashville",
         opponent="Jeff Jarrett, %s, Chris Harris & Raven" % _a("AJ Styles"), opponent_html=True,
         stip="King of the Mountain. Jarrett takes the title back",
         title="NWA World Heavyweight Championship"),
    dict(result="W", date="2007-09-09", promo="TNA", type="tag",
         event="No Surrender, Orlando",
         opponent="%s & %s" % (_a("Kurt Angle"), _a("Sting")), opponent_html=True,
         stip="Team Pacman, with Adam \"Pacman\" Jones. Jones pins Sting",
         title="TNA World Tag Team Championship"),
    dict(result="L", date="2007-10-14", promo="TNA", type="tag",
         event="Bound for Glory, Duluth", opponent="AJ Styles & Tomko",
         stip="With Consequences Creed standing in for Jones",
         title="TNA World Tag Team Championship"),
    dict(result="W", date="2008-08-29", promo="WWE", landmark=True,
         event="SmackDown", opponent="Kenny Dykstra",
         stip="The R-Truth debut match, seven years after the WWF let him go", title=""),
    dict(result="W", date="2009-10-25", promo="WWE", type="tag",
         event="Bragging Rights", opponent="Team Raw",
         stip="Seven-on-seven, Team SmackDown wins the trophy", title=""),
    dict(result="L", date="2010-03-28", promo="WWE", type="tag",
         event="WrestleMania XXVI", opponent=_a("Big Show") + " & The Miz", opponent_html=True,
         stip="With John Morrison, against ShoMiz",
         title="Unified WWE Tag Team Championship"),
    dict(result="W", date="2010-05-24", promo="WWE", landmark=True,
         event="Raw", opponent="The Miz",
         stip="For the vacant title. His first WWE singles championship",
         title="WWE United States Championship"),
    dict(result="L", date="2010-06-14", promo="WWE", type="tag",
         event="Raw", opponent="The Miz and two others",
         stip="Fatal four-way. The reign ends at 20 days",
         title="WWE United States Championship"),
    dict(result="L", date="2011-06-19", promo="WWE", landmark=True,
         event="Capitol Punishment", opponent=_a("John Cena"), opponent_html=True,
         stip="Singles. The paranoid heel's only WWE Championship match",
         title="WWE Championship"),
    dict(result="L", date="2011-11-20", promo="WWE", type="tag", landmark=True,
         event="Survivor Series", opponent="%s & %s" % (_a("John Cena"), _a("The Rock")),
         opponent_html=True,
         stip="Main event, as Awesome Truth with The Miz", title=""),
    dict(result="W", date="2012-04-30", promo="WWE", type="tag", landmark=True,
         event="Raw SuperShow", opponent="Primo & Epico",
         stip="With Kofi Kingston", title="WWE Tag Team Championship"),
    dict(result="L", date="2012-09-16", promo="WWE", type="tag",
         event="Night of Champions, Boston",
         opponent="%s & %s" % (_a("Kane"), _a("Daniel Bryan")), opponent_html=True,
         stip="With Kofi Kingston. Kane pins Kingston", title="WWE Tag Team Championship"),
    dict(result="L", date="2015-03-29", promo="WWE", type="tag",
         event="WrestleMania 31", opponent="The Intercontinental ladder field",
         stip="Seven-man ladder match", title="WWE Intercontinental Championship"),
    dict(result="W", date="2016-06-19", promo="WWE", type="tag",
         event="Money in the Bank", opponent="Breezango",
         stip="Golden Truth, with Goldust", title=""),
    dict(result="W", date="2019-01-29", promo="WWE", landmark=True,
         event="SmackDown", opponent=_a("Shinsuke Nakamura"), opponent_html=True,
         stip="Singles, a roll-up. Second US title",
         title="WWE United States Championship"),
    dict(result="L", date="2019-03-05", promo="WWE", type="tag",
         event="SmackDown", opponent=_a("Samoa Joe") + " and two others", opponent_html=True,
         stip="Fatal four-way. The reign ends at 35 days",
         title="WWE United States Championship"),
    dict(result="W", date="2019-05-20", promo="WWE", landmark=True,
         event="Raw, Albany", opponent="Robert Roode",
         stip="A parking-lot pin. The first of 54 reigns",
         title="WWE 24/7 Championship"),
    dict(result="W", date="2019-06-02", promo="WWE",
         event="Golf course", opponent="Jinder Mahal",
         stip="24/7 rules, on the course", title="WWE 24/7 Championship"),
    dict(result="W", date="2019-06-20", promo="WWE",
         event="Drake Maverick's wedding, Orlando", opponent="Drake Maverick",
         stip="Pinned the groom as the couple walked out", title="WWE 24/7 Championship"),
    dict(result="W", date="2023-12-18", promo="WWE",
         event="Raw", opponent="JD McDonagh",
         stip="Loser Leaves Judgment Day, Miracle on 34th Street Fight", title=""),
    dict(result="W", date="2024-04-06", promo="WWE", type="tag", landmark=True,
         event="WrestleMania XL Night 1", opponent="Five other teams",
         stip="Six-pack ladder match with The Miz. His first WrestleMania win",
         title="Raw Tag Team Championship"),
    dict(result="L", date="2024-06-24", promo="WWE", type="tag",
         event="Raw", opponent=_a("Finn Balor") + " & JD McDonagh", opponent_html=True,
         stip="With The Miz. The reign ends at 79 days",
         title="World Tag Team Championship"),
    dict(result="L", date="2025-05-24", promo="WWE", landmark=True,
         event="Saturday Night's Main Event, Tampa", opponent=_a("John Cena"), opponent_html=True,
         stip="Non-title. His childhood hero hits the AA, then the belt", title=""),
    dict(result="W", date="2025-06-20", promo="WWE",
         event="SmackDown", opponent=_a("John Cena"), opponent_html=True,
         stip="Disqualification, after Cena hits him with the title", title=""),
    dict(result="L", date="2025-12-29", promo="WWE",
         event="Raw", opponent=_a("Gunther"), opponent_html=True,
         stip="Taps to a sleeper, two weeks after Gunther retired Cena", title=""),
    dict(result="W", date="2026-03-20", promo="WWE", type="tag", landmark=True,
         event="SmackDown", opponent="Tama Tonga & JC Mateo",
         stip="With Damian Priest. Truth pins Mateo with an Attitude Adjustment",
         title="WWE Tag Team Championship"),
    dict(result="W", date="2026-04-17", promo="WWE", type="tag",
         event="SmackDown", opponent="Kofi Kingston & Grayson Waller",
         stip="With Damian Priest, on the go-home show before WrestleMania 42",
         title="WWE Tag Team Championship"),
    dict(result="L", date="2026-08-14", promo="WWE", type="tag",
         event="SmackDown, Boston", opponent="The MFTs and the War Raiders",
         stip="Triple threat. The 147-day reign ends", title="WWE Tag Team Championship"),
    dict(result="L", date="2026-08-21", promo="WWE", type="tag",
         event="SmackDown", opponent="Tama Tonga & Talla Tonga",
         stip="Rematch with Priest. The Tongas finish Truth with the Red Cross",
         title="WWE Tag Team Championship"),
    dict(result="L", date="2026-09-11", promo="WWE", type="tag", landmark=True,
         event="SmackDown", opponent="Erik & Ivar (War Raiders)",
         stip="With Priest, who turns on him with South of Heaven afterward",
         title="AAA World Tag Team Championship"),
    dict(result="L", date="2026-10-16", promo="WWE", landmark=True,
         event="SmackDown", opponent=_a("Damian Priest"), opponent_html=True,
         stip="Referee stoppage after Truth is hurt on a top-rope dropkick. His most recent match",
         title=""),
]

# html-flagged opponents are emitted raw, so their ampersands must be entities
for _r in ROWS:
    if _r.get("opponent_html"):
        _r["opponent"] = _r["opponent"].replace(" & ", " &amp; ")

DATA = dict(
    slug="r-truth",
    name="R-Truth",
    realname="Ronnie Aaron Killings",
    epithet="The Truth",
    hook="Record & Titles",
    art="r-truth",

    meta_desc=("R-Truth (Ron Killings): two-time NWA World Heavyweight Champion in TNA, 54-time "
               "WWE 24/7 Champion, US and tag champion, and WWE Tag Team Champion with Damian "
               "Priest at 54. Full record, titles, the 2025 release saga and his 2026 status."),
    og_desc=("Two NWA world titles in TNA, 54 reigns as 24/7 Champion, tag gold at 52 and 54, a "
             "June 2025 release that lasted six days, and a 2026 betrayal by Damian Priest."),
    tw_desc="R-Truth: 2x NWA World Champion, 54x 24/7 Champion, tag champ at 54. What's up.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1999",
    height_imp="6&#8242;2&#8243;",
    weight_lb="220",
    world_titles="2",
    vitals_tagline="What's up",
    support_note="Merch &middot; Music &middot; Watch",
    x_url="https://x.com/RonKillings",
    sp_items=[
        dict(ic="RT", title="R-Truth Merch", sub="Official gear · WWE Shop",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="2K", title="WWE 2K", sub="Playable in the WWE games since 2002",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="WWE", title="Official Profile", sub="WWE.com", tag="Visit", charity=True,
             href="https://www.wwe.com/superstars/r-truth"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Two-time NWA World Champion &middot; 54-time 24/7 Champion &middot; tag champion at 54",
    hero_tag="Charlotte, North Carolina &middot; <em>WWF 2000&ndash;01 &middot; NWA-TNA 2002&ndash;07 "
             "&middot; WWE 2008&ndash;present</em>",
    now_label="NOW",
    now_bold="Injured, SmackDown",
    now_tail=(" &middot; hurt in a referee stoppage against Damian Priest on October 16, 2026; "
              "posted from hospital on October 19 that he is OK and will be back. No return date "
              "announced as of November 9, 2026"),
    hstats=[
        dict(value="54", x=True,  label="24/7 Title Reigns"),
        dict(value="2",  x=True,  label="NWA World Titles"),
        dict(value="3",  x=True,  label="WWE Tag Title Reigns"),
        dict(value="2",  x=True,  label="US Title Reigns"),
    ],
    ghost_link="From a Charlotte prison cell to world champion to the funniest man on the roster",
    vlabel="Est. 1999 &middot; Charlotte, North Carolina",
    mono="RT",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>R-Truth</b> has the strangest resume on the WWE roster. Before he was the man who chased "
        "a 24/7 belt across parking lots, golf courses and a wedding, he was <b>Ron &ldquo;The "
        "Truth&rdquo; Killings, two-time NWA World Heavyweight Champion</b>, beating Ken Shamrock for "
        "the title on August 7, 2002 in NWA-TNA&rsquo;s first year. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">54</span>'
        '<span class="pull-cap">reigns as WWE 24/7 Champion, 2019&ndash;2022. The next-best count is 15</span></span>'
        "The rest of the ledger is long and real: two Hardcore reigns in 2001 as K-Kwik, two United "
        "States Championships, tag titles with Kofi Kingston in 2012, The Miz at WrestleMania XL in "
        "2024 and <a href=\"/wrestlers/damian-priest/\">Damian Priest</a> in 2026, and a WWE "
        "Championship match against <a href=\"/wrestlers/john-cena/\">John Cena</a> at Capitol "
        "Punishment in 2011.",

        "Two things people get wrong about him. First, he was not released in June 2025 in the "
        "usual sense. He posted &ldquo;I just got released from WWE&rdquo; on June 1, but Fightful "
        "reported that WWE was letting his contract lapse rather than cutting it. Six days later he "
        "was back, costing Cena and Logan Paul at Money in the Bank. Second, the 24/7 count depends "
        "on who is counting. WWE.com&rsquo;s profile says 54. Wikipedia&rsquo;s champions list says "
        "54 overall and 53 recognized by WWE. Either number is a record no one is close to, and the "
        "title was retired in November 2022, so no one ever will be.",

        "He was born Ronnie Aaron Killings in Charlotte, North Carolina on January 19, 1972. He "
        "turned down college scholarships to chase music, sold drugs to pay for it, was arrested four "
        "times and served 13 months. Wrestling came after. He trained under George South and others, "
        "won the NWA Wildside TV title from <a href=\"/wrestlers/aj-styles/\">AJ Styles</a> in 1999, "
        "and reached the WWF as K-Kwik, Road Dogg&rsquo;s rapping partner, in November 2000. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig pull-fig--sm">2002</span>'
        '<span class="pull-cap">the year he won the NWA World Heavyweight Championship, a title he calls proof he was the first Black man to hold it</span></span>'
        "Released in 2001, he became a main-event act in NWA-TNA: two NWA world titles, the 3 Live "
        "Kru with Konnan and B.G. James, and TNA tag gold with NFL cornerback Adam &ldquo;Pacman&rdquo; "
        "Jones in 2007. WWE brought him back as R-Truth on August 29, 2008.",

        "The second WWE run has lasted 18 years and three characters. The rapping babyface of "
        "2008&ndash;10. The paranoid &ldquo;Little Jimmy&rdquo; heel of 2011, who got a world title "
        "match and a Survivor Series main event. Then the comedy act that took over the back half of "
        "his career and made him one of WWE&rsquo;s most popular performers. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">147</span>'
        '<span class="pull-cap">days as WWE Tag Team Champion with Damian Priest in 2026, won at 54</span></span>'
        "2025 was the wildest year of it: a feud with his childhood hero Cena, the non-renewal, the "
        "return, a haircut on Raw that announced &ldquo;Ron Killings,&rdquo; and a quiet slide back "
        "to R-Truth within two months. In 2026 he and Priest won the WWE Tag Team Championship on "
        "March 20 and held it 147 days. Priest turned on him on September 11. Their singles match on "
        "October 16 was stopped when Truth was hurt on a top-rope dropkick. As of November 9, 2026 he "
        "has not wrestled since, and says he will be back.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Highlight set",
        promo_order=["IND", "WWF", "TNA", "WWE"],
        promo_labels={"IND": "Indie", "WWF": "WWF", "TNA": "NWA-TNA", "WWE": "WWE"},
        stats=[
            ("2&times;",  "NWA World titles"),
            ("54&times;", "24/7 titles"),
            ("2&times;",  "US titles"),
            ("3&times;",  "WWE tag titles"),
            ("2&times;",  "Hardcore titles"),
            ("2026",      "Most recent match"),
        ],
        lead=("Thirty-six documented bouts across 27 years, from the NWA Wildside TV title in 1999 "
              "to the October 2026 referee stoppage against Damian Priest. This is a highlight set, "
              "not a career count. No career win&ndash;loss total is published because none was "
              "verified. Most 24/7 title changes were not matches in any normal sense, so only three "
              "representative ones are listed. Filter by promotion or match type, sort any column, "
              "and turn spoilers on to see results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 titles
    titles=dict(
        stats=[
            ("2&times;",  "NWA World Heavyweight"),
            ("54&times;", "WWE 24/7"),
            ("2&times;",  "WWE United States"),
            ("147",       "Days, 2026 tag reign"),
        ],
        lead=("Gold in four promotions over 27 years. The world titles came in NWA-TNA. The "
              "volume came in WWE, where he holds a 24/7 record that cannot be broken because the "
              "belt is retired."),
        rows=[
            dict(ic="W", name="NWA World Heavyweight Championship", count="2",
                 sub="August 7, 2002, beat Ken Shamrock on NWA-TNA weekly PPV #8 in Nashville; lost "
                     "to Jeff Jarrett on November 20, 2002 after a masked man&rsquo;s guitar shot "
                     "&middot; May 19, 2004, won a four-way over AJ Styles, Chris Harris and Raven; "
                     "lost to Jarrett in a King of the Mountain match on June 2, 2004"),
            dict(ic="24", name="WWE 24/7 Championship", count="54",
                 sub="First reign May 20, 2019, pinning Robert Roode in a Raw parking lot in Albany "
                     "&middot; last reign June 20, 2022 on Main Event in Lincoln, Nebraska &middot; "
                     "WWE.com counts 54; Wikipedia lists 54 with 53 recognized by WWE &middot; the "
                     "title was retired after Raw on November 7, 2022"),
            dict(ic="US", name="WWE United States Championship", count="2",
                 sub="May 24, 2010, won the vacant title from The Miz on Raw; lost to Miz in a "
                     "fatal four-way June 14 (20 days) &middot; January 29, 2019, beat Shinsuke "
                     "Nakamura on SmackDown; lost to Samoa Joe in a fatal four-way March 5 (35 days)"),
            dict(ic="T", name="WWE / World Tag Team Championship", count="3",
                 sub="With Kofi Kingston, April 30 to September 16, 2012 &middot; with The Miz, "
                     "won the Raw Tag Team title in the WrestleMania XL ladder match on April 6, "
                     "2024, renamed World Tag Team Championship that month, lost June 24 (79 days) "
                     "&middot; with Damian Priest, March 20 to August 14, 2026 (147 days)"),
            dict(ic="H", name="WWF Hardcore Championship", count="2",
                 sub="February 3 and 4, 2001, as K-Kwik. Both times he beat Raven and lost the "
                     "belt to Crash Holly within hours under the 24/7 rule"),
            dict(ic="N", name="NWA World Tag Team Championship", count="1",
                 sub="With the 3 Live Kru, won the vacant title November 26, 2003 and held it "
                     "under the Freebird rule until January 28, 2004 &middot; Wikipedia&rsquo;s "
                     "infobox credits a second reign in late 2004; its body credits that win to "
                     "Konnan and James, so one is counted here"),
            dict(ic="T", name="TNA World Tag Team Championship", count="1",
                 sub="With Adam &ldquo;Pacman&rdquo; Jones, beat Kurt Angle and Sting at No "
                     "Surrender on September 9, 2007; lost at Bound for Glory on October 14 with "
                     "Consequences Creed filling in for Jones (35 days)"),
            dict(ic="R", name="Regional and developmental titles", count="3",
                 sub="NWA Wildside Television Championship, November 6, 1999, over AJ Styles "
                     "&middot; MCW Southern Heavyweight Championship twice in 2000, in WWF&rsquo;s "
                     "Memphis developmental system"),
        ],
    ),

    # ---------------------------------------------------------------- 04 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="A career of partnerships, most of which ended with somebody turning on him.",
        cards=[
            dict(era="NWA-TNA &middot; 2003&ndash;05",
                 name="3 Live Kru",
                 members="Ron Killings, Konnan, B.G. James",
                 desc="Formed in July 2003. Won the vacant NWA World Tag Team titles on November "
                      "26, 2003 and defended them under the Freebird rule. It ended when Konnan "
                      "turned on the others in December 2005."),
            dict(era="NWA-TNA &middot; 2007",
                 name="Team Pacman",
                 members="Ron Killings, Adam \"Pacman\" Jones",
                 desc="The NFL cornerback and the former world champion beat Kurt Angle and Sting "
                      "for the TNA tag titles at No Surrender 2007. Jones could not always "
                      "appear, so Consequences Creed defended in his place and lost them at Bound "
                      "for Glory."),
            dict(era="WWE &middot; 2011, 2024",
                 name="Awesome Truth",
                 members="R-Truth, The Miz",
                 desc="Debuted as heels on August 22, 2011, got fired by Triple H, rehired, and "
                      "main-evented Survivor Series against Cena and The Rock. Miz broke it up the "
                      "next night. The 2024 reunion won the Raw tag titles at WrestleMania XL, and "
                      "Miz walked out on him again on September 30, 2024."),
            dict(era="WWE &middot; 2016&ndash;17",
                 name="Golden Truth",
                 members="R-Truth, Goldust",
                 desc="A comedy tag team built on two veterans who should not have worked "
                      "together and did. Beat Breezango at Money in the Bank 2016, and had its "
                      "own remix of \"What's Up?\"."),
            dict(era="WWE &middot; 2023",
                 name="The Judgment Day (self-appointed)",
                 members="R-Truth, uninvited",
                 desc="After his Survivor Series return he decided he was a member. The group "
                      "attacked him on December 11, 2023, and a week later he beat JD McDonagh in "
                      "a Loser Leaves Judgment Day street fight."),
            dict(era="WWE &middot; 2026",
                 name="Wepa Up",
                 members="R-Truth, Damian Priest",
                 desc="Named on WWE Shop merch for Priest's \"Wepa\" and Truth's \"What's up?\". "
                      "Won the WWE Tag Team Championship on March 20, 2026 and held it 147 days. "
                      "Priest ended it with South of Heaven on September 11, 2026."),
        ],
    ),

    # ---------------------------------------------------------------- 05 personas
    personas=dict(
        lead="Six names in 27 years. Every one of them raps.",
        cards=[
            dict(mono="KK", era="WWF &middot; 2000&ndash;01", name="K-Kwik",
                 desc="Road Dogg's rapping partner, debuting on Raw is War on November 13, 2000. "
                      "Two Hardcore title reigns in February 2001, then released that August."),
            dict(mono="TR", era="NWA-TNA &middot; 2002&ndash;07", name="Ron \"The Truth\" Killings",
                 desc="The serious version. Two NWA World Heavyweight titles, the 3 Live Kru, and "
                      "\"Toma\" by Pitbull as his walk-out. This is the run his own song \"Legacy\" "
                      "is about."),
            dict(mono="RT", era="WWE &middot; 2008&ndash;10", name="R-Truth",
                 desc="Returned on SmackDown on August 29, 2008, rapping \"What's Up?\" to the "
                      "ring. A popular babyface who won the US title in 2010."),
            dict(mono="LJ", era="WWE &middot; 2011", name="The paranoid heel",
                 desc="Convinced the world was lying to him, talking to the invisible \"Little "
                      "Jimmy\". Got a WWE Championship match against Cena and a Survivor Series "
                      "main event. Many fans still rate it his best character work."),
            dict(mono="24", era="WWE &middot; 2015&ndash;2025", name="The comedy legend",
                 desc="The confused, joyful R-Truth who thinks he is someone else and never "
                      "stops trying. Carried the 24/7 Championship for three years and became one "
                      "of WWE's most popular acts."),
            dict(mono="RK", era="WWE &middot; June 2025", name="Ron Killings",
                 desc="Back from the non-renewal, he cut off his hair on Raw on June 9, 2025 and "
                      "said the Truth had set Ron Killings free. Within two months he was R-Truth "
                      "again. He later called Ron Killings \"the cavalry\" and \"a selfish move\"."),
        ],
    ),

    # ---------------------------------------------------------------- 06 career
    career=dict(
        lead="Prison, music, the WWF, a world title in TNA, and an 18-year second act.",
        rows=[
            dict(year="1999", title="K-Krush, and a first title",
                 desc="Wins the NWA Wildside Television Championship from AJ Styles on November 6, "
                      "and signs a WWF developmental deal."),
            dict(year="2000", title="K-Kwik reaches Raw",
                 desc="Twice MCW Southern Heavyweight Champion in Memphis, then debuts on Raw is "
                      "War on November 13 alongside Road Dogg."),
            dict(year="2001", title="Hardcore, and released",
                 desc="Wins the Hardcore title from Raven on February 3 and 4, loses it to Crash "
                      "Holly both times within hours, and is released in August."),
            dict(year="2002", title="NWA World Heavyweight Champion",
                 desc="Signs with NWA-TNA in June and beats Ken Shamrock for the NWA world title "
                      "on August 7 in Nashville. Jeff Jarrett takes it on November 20."),
            dict(year="2003", title="The 3 Live Kru",
                 desc="Forms the Kru with Konnan and B.G. James in July. They win the vacant NWA "
                      "World Tag Team titles on November 26."),
            dict(year="2004", title="Second world title",
                 desc="Wins a four-way over AJ Styles, Chris Harris and Raven on May 19. Jarrett "
                      "regains it in a King of the Mountain match on June 2."),
            dict(year="2007", title="Team Pacman, then out",
                 desc="Wins the TNA tag titles with Adam \"Pacman\" Jones at No Surrender on "
                      "September 9, loses them October 14, and leaves TNA in December."),
            dict(year="2008", title="R-Truth arrives",
                 desc="Returns to WWE on SmackDown on August 29 and beats Kenny Dykstra."),
            dict(year="2010", title="First US title",
                 desc="Loses with John Morrison at WrestleMania XXVI, then wins the vacant US "
                      "title from The Miz on May 24."),
            dict(year="2011", title="The heel turn",
                 desc="Turns on John Morrison, challenges Cena for the WWE Championship at Capitol "
                      "Punishment on June 19, and main-events Survivor Series with The Miz."),
            dict(year="2012", title="Tag champion with Kofi",
                 desc="Wins the WWE Tag Team titles with Kofi Kingston on April 30 and holds them "
                      "until Night of Champions on September 16."),
            dict(year="2019", title="The 24/7 era begins",
                 desc="Wins a second US title on January 29, then the 24/7 title on May 20. Over "
                      "the next three years he wins it 54 times."),
            dict(year="2023", title="Judgment Day, uninvited",
                 desc="Returns at Survivor Series on November 25 and declares himself a member. "
                      "Beats JD McDonagh in a Loser Leaves Judgment Day match on December 18."),
            dict(year="2024", title="WrestleMania gold at 52",
                 desc="Wins the Raw tag titles with The Miz in the WrestleMania XL ladder match on "
                      "April 6. Loses them June 24. Miz walks out on him September 30."),
            dict(year="2025", title="Cena, the release, and Ron Killings",
                 desc="Loses to John Cena at Saturday Night's Main Event on May 24. Announces his "
                      "release on June 1, returns at Money in the Bank on June 7, and cuts his hair "
                      "on Raw as Ron Killings on June 9. Back to R-Truth by late summer. Releases "
                      "The White Album, a No. 10 Billboard country record."),
            dict(year="2026", title="Wepa Up, then betrayal",
                 desc="Wins the WWE Tag Team Championship with Damian Priest on March 20 and loses "
                      "it August 14. Priest turns on him September 11. Their October 16 match is "
                      "stopped when Truth is hurt. He says he will be back."),
        ],
    ),

    # ---------------------------------------------------------------- 07 rivalries
    rivalries=dict(
        lead="Who he went to war with, and who turned on him.",
        cards=[
            dict(name="John Cena", slug="john-cena",
                 desc="Two feuds 14 years apart. In 2011 the paranoid heel challenged Cena for the "
                      "WWE Championship at Capitol Punishment and lost. In 2025 Truth called Cena "
                      "his childhood hero, got put through a table at the Backlash press "
                      "conference, lost at Saturday Night's Main Event on May 24, and returned "
                      "from his non-renewal to cost Cena at Money in the Bank."),
            dict(name="Damian Priest", slug="damian-priest",
                 desc="Partner, then attacker. They won the WWE Tag Team Championship on March "
                      "20, 2026 and held it 147 days. After losing an AAA tag title shot on "
                      "September 11, Priest hit him with South of Heaven. Their October 16 match "
                      "ended in a referee stoppage, and Truth says Priest \"tried to kill me\"."),
            dict(name="The Miz",
                 desc="The partner who keeps leaving. Awesome Truth main-evented Survivor Series "
                      "2011 and split the next night. The 2024 reunion won tag gold at WrestleMania "
                      "XL, and Miz walked out on him again that September."),
            dict(name="Jeff Jarrett",
                 desc="The man who took both of his NWA world titles: November 20, 2002, with a "
                      "masked man's guitar shot, and June 2, 2004, in a King of the Mountain "
                      "match. Jarrett was the TNA founder and its top champion of that era."),
            dict(name="The 24/7 field",
                 desc="Jinder Mahal on a golf course and a plane, Drake Maverick at his own "
                      "wedding, Robert Roode in a parking lot, Bad Bunny with a trade. The 24/7 "
                      "title was a three-year running bit, and Truth was the center of it."),
            dict(name="Gunther", slug="gunther",
                 desc="After Gunther made John Cena tap in Cena's last match on December 13, "
                      "2025, Truth stepped up to avenge his hero on Raw two weeks later and tapped "
                      "to the sleeper too."),
        ],
    ),

    # ---------------------------------------------------------------- 08 media
    media=dict(
        h2="Music &amp; Media",
        lead="A rapper first. He turned down college scholarships for music before wrestling.",
        rows=[
            dict(when="2003&ndash;", title="Albums", kind="Music",
                 desc="Invinceable (2003), Killingit (2016), Legacy (2021) and The White Album "
                      "(August 2025), a country record that reached No. 10 on Billboard's Country "
                      "Albums chart."),
            dict(when="2008&ndash;", title="\"What's Up?\"", kind="Theme",
                 desc="His own entrance theme, released on Voices: WWE The Music, Vol. 9. In June "
                      "2025 he turned down Metro Boomin's offer to produce a new one."),
            dict(when="2011", title="\"Little Jimmy\"", kind="TV",
                 desc="The June 6, 2011 Raw song segment that became the catchphrase of his heel "
                      "run and the name of his finisher."),
            dict(when="2003&ndash;18", title="Film", kind="Screen",
                 desc="Head of State (2003), The Wrestler (2008), Break Dance Revolution (2016) "
                      "and Blood Brother (2018)."),
            dict(when="2002&ndash;", title="WWE video games", kind="Game",
                 desc="Playable in WWE's games from 2002 through the 2026 edition."),
        ],
    ),

    # ---------------------------------------------------------------- 09 feats
    slot10=dict(
        id="feats",
        lead="The records, with the counting rules that make them true.",
        stats=[
            ("54", "24/7 title reigns"),
            ("15", "Next-best 24/7 count"),
            ("54", "Age at his last tag title win"),
        ],
        rows=[
            dict(name="54 reigns as WWE 24/7 Champion, the record for that title",
                 sub="May 20, 2019 to June 20, 2022. WWE.com counts 54. Wikipedia lists 54 with "
                     "53 recognized by WWE. Akira Tozawa and Dana Brooke are next with 15 each. "
                     "The title was retired in November 2022, so the record is closed."),
            dict(name="Two NWA World Heavyweight Championships",
                 sub="August 7, 2002 over Ken Shamrock and May 19, 2004 in a four-way, both in "
                     "NWA-TNA. He says he was the first Black man to hold the title. That is his "
                     "own claim, repeated by Cultaholic, and this page attributes it to him."),
            dict(name="The only wrestler to hold both the Hardcore and 24/7 titles",
                 sub="Two Hardcore reigns as K-Kwik in February 2001, and the 24/7 title from May "
                     "20, 2019. The two belts shared the same anytime-anywhere rule, 18 years "
                     "apart."),
            dict(name="Tag team gold at 52 and 54",
                 sub="The Raw Tag Team Championship with The Miz at WrestleMania XL in 2024, and "
                     "the WWE Tag Team Championship with Damian Priest in 2026, held 147 days."),
            dict(name="A first WrestleMania win, 16 years after his WWE return",
                 sub="WrestleMania XL Night 1, April 6, 2024, in a six-pack ladder match. His "
                     "earlier WrestleMania matches, from XXVI in 2010 on, were losses."),
            dict(name="A release that lasted six days",
                 sub="He announced it on June 1, 2025. Fightful reported a non-renewal, not a "
                     "cut. He was back on June 7 at Money in the Bank."),
            dict(name="A top-10 Billboard album during an active WWE run",
                 sub="The White Album, released August 7, 2025, reached No. 10 on Billboard's "
                     "Country Albums chart."),
        ],
        footnote=("No career win-loss total appears on this page; none was verified. The 2026 "
                  "tag reign is 147 days by date; Wrestling Inc printed 148."),
    ),

    # ---------------------------------------------------------------- 10 reference
    reference=[
        dict(k="X / Twitter", v="@RonKillings", href="https://x.com/RonKillings"),
        dict(k="WWE.com", v="Official profile", href="https://www.wwe.com/superstars/r-truth"),
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/R-Truth"),
        dict(k="Wikipedia", v="List of WWE 24/7 Champions",
             href="https://en.wikipedia.org/wiki/List_of_WWE_24/7_Champions"),
        dict(k="WWE.com", v="US Championship title history",
             href="https://www.wwe.com/classics/titlehistory/unitedstates"),
        dict(k="Wrestling Inc", v="March 20, 2026: Priest & Truth win the tag titles",
             href="https://www.wrestlinginc.com/2128495/wwe-smackdown-damian-priest-r-truth-mfts-tag-team-championship"),
        dict(k="Fightful", v="September 11, 2026: Priest turns on Truth",
             href="https://www.fightful.com/?p=327922"),
        dict(k="WWE.com", v="October 16, 2026 SmackDown results",
             href="https://www.wwe.com/shows/smackdown/2026-10-16/results"),
        dict(k="POST Wrestling", v="June 1, 2025: the non-renewal",
             href="https://www.postwrestling.com/?p=116644"),
        dict(k="CBS Sports", v="Truth on dropping Ron Killings",
             href="https://www.cbssports.com/wwe/news/r-truth-defends-wwe-dropping-his-ron-killings-persona-it-was-a-selfish-move/"),
        dict(k="Research Dossier", v="Full career data (.md)", href="/data/r-truth.md"),
    ],

    # ---------------------------------------------------------------- 11 faq
    faq=[
        dict(
            q="Is R-Truth still in WWE?",
            a="Yes. He is on SmackDown but <b>out injured</b> as of November 9, 2026. His match "
              "with Damian Priest on October 16, 2026 was stopped by the referee after he was hurt "
              "on a top-rope dropkick. On October 19 he posted from hospital: &ldquo;I AM OK&rdquo; "
              "and &ldquo;I&rsquo;ll be back.&rdquo; No return date has been announced.",
            q_ld="Is R-Truth still in WWE in 2026?",
            a_ld="Yes. R-Truth is on the WWE SmackDown roster but has been out injured since his "
                 "October 16, 2026 match against Damian Priest was stopped by the referee. He "
                 "posted on October 19, 2026 that he was OK and would be back. As of November 9, "
                 "2026, no return date had been announced."),
        dict(
            q="Did WWE release R-Truth in 2025?",
            a="Not in the usual sense. On June 1, 2025 he posted &ldquo;I just got released from "
              "WWE,&rdquo; but Fightful reported WWE was letting his contract expire rather than "
              "cutting it. After a week of backlash from fans and wrestlers he returned at Money in "
              "the Bank on June 7, 2025, costing John Cena and Logan Paul their tag match against "
              "Cody Rhodes and Jey Uso.",
            q_ld="Did WWE release R-Truth in 2025?",
            a_ld="R-Truth announced on June 1, 2025 that WWE had released him. Reports said WWE was "
                 "allowing his contract to expire rather than terminating it. He returned six days "
                 "later at Money in the Bank on June 7, 2025, helping Cody Rhodes and Jey Uso beat "
                 "John Cena and Logan Paul."),
        dict(
            q="Why did R-Truth change his name to Ron Killings?",
            a="After his return he cut off his hair on Raw on June 9, 2025 and said the Truth had "
              "set Ron Killings free. Dave Meltzer reported he asked for the name in his new deal "
              "so he could keep using it after WWE. Fightful reported he wanted a more serious run. "
              "Within two months he was back to the R-Truth character. He later told CBS Sports "
              "Ron Killings was &ldquo;the cavalry&rdquo; and &ldquo;a selfish move.&rdquo;",
            q_ld="Why did R-Truth change his name to Ron Killings?",
            a_ld="R-Truth began using his real name, Ron Killings, after returning to WWE in June "
                 "2025. Reports said he requested the name in his new contract so he could keep "
                 "using it after WWE, and that he wanted a more serious run. He returned to the "
                 "R-Truth comedy character within about two months."),
        dict(
            q="How many times did R-Truth win the 24/7 Championship?",
            a="<b>54</b>, per WWE.com. Wikipedia&rsquo;s champions list counts 54 overall with 53 "
              "recognized by WWE. The first was May 20, 2019, pinning Robert Roode in a parking "
              "lot. The last was June 20, 2022. Nobody else reached 16. The title was retired in "
              "November 2022.",
            q_ld="How many times did R-Truth win the WWE 24/7 Championship?",
            a_ld="R-Truth won the WWE 24/7 Championship 54 times according to WWE.com, the record "
                 "for the title. Some lists recognize 53. His first reign began May 20, 2019 and "
                 "his last on June 20, 2022. The title was retired in November 2022."),
        dict(
            q="Was R-Truth a world champion?",
            a="Yes, in NWA-TNA. As Ron &ldquo;The Truth&rdquo; Killings he won the <b>NWA World "
              "Heavyweight Championship twice</b>: from Ken Shamrock on August 7, 2002, and in a "
              "four-way over AJ Styles, Chris Harris and Raven on May 19, 2004. Jeff Jarrett ended "
              "both reigns. In WWE his only world title match was against John Cena at Capitol "
              "Punishment in 2011.",
            q_ld="Was R-Truth ever a world champion?",
            a_ld="Yes. Ron Killings, now known as R-Truth, won the NWA World Heavyweight "
                 "Championship twice in NWA-TNA, on August 7, 2002 against Ken Shamrock and on May "
                 "19, 2004 in a four-way match. He has not won a world title in WWE."),
        dict(
            q="Who did R-Truth win tag team titles with?",
            a="Five partners across three promotions: the 3 Live Kru (Konnan and B.G. James) for "
              "the NWA tag titles in 2003, Adam &ldquo;Pacman&rdquo; Jones for the TNA tag titles in "
              "2007, Kofi Kingston in 2012, The Miz at WrestleMania XL in 2024, and Damian Priest "
              "from March 20 to August 14, 2026.",
            q_ld="Who has R-Truth won tag team championships with?",
            a_ld="R-Truth has won tag team titles with Konnan and B.G. James (NWA, 2003), Adam "
                 "Pacman Jones (TNA, 2007), Kofi Kingston (WWE, 2012), The Miz (WrestleMania XL, "
                 "2024) and Damian Priest (WWE Tag Team Championship, March to August 2026)."),
        dict(
            q="Why did Damian Priest turn on R-Truth?",
            a="On the September 11, 2026 SmackDown they lost an AAA World Tag Team Championship "
              "match to the War Raiders. Priest hugged Truth, put a sombrero on him, then hit him "
              "with a clothesline and South of Heaven. On the October 30 SmackDown Priest said "
              "Truth had been dragging him down.",
            q_ld="Why did Damian Priest turn on R-Truth?",
            a_ld="Damian Priest attacked R-Truth after they lost an AAA World Tag Team Championship "
                 "match to the War Raiders on the September 11, 2026 episode of SmackDown. Priest "
                 "later said R-Truth had been dragging him down."),
        dict(
            q="What is R-Truth's real name and how old is he?",
            a="Ronnie Aaron Killings, born January 19, 1972 in Charlotte, North Carolina. He is "
              "54. One wrestling database gives his birthplace as Williamsburg, South Carolina; "
              "Wikipedia says Charlotte, which WWE also bills as his hometown.",
            q_ld="What is R-Truth's real name?",
            a_ld="R-Truth's real name is Ronnie Aaron Killings. He was born on January 19, 1972 in "
                 "Charlotte, North Carolina, and was 54 years old in November 2026."),
        dict(
            q="What is R-Truth's entrance theme?",
            a="&ldquo;What&rsquo;s Up?&rdquo;, which he performs himself. It has been his WWE theme "
              "since 2008, apart from short swaps in 2010 and 2011, and appears on Voices: WWE The "
              "Music, Vol. 9. In June 2025 he declined Metro Boomin&rsquo;s offer of a new theme: "
              "&ldquo;What&rsquo;s up ain&rsquo;t broken, I wanna keep it.&rdquo;",
            q_ld="What is R-Truth's entrance theme song?",
            a_ld="R-Truth's entrance theme is \"What's Up?\", which he performs himself. He has used "
                 "it in WWE since 2008, and it appears on the album Voices: WWE The Music, Vol. 9. "
                 "In 2025 he turned down an offer from producer Metro Boomin to make a new theme."),
    ],

    # ---------------------------------------------------------------- walk-out
    theme={
        "kicker": "Entrance theme",
        "since": "since SmackDown, 2008",
        "track": "What's Up?",
        "artist": "R-Truth",
        "meta": "Voices: WWE The Music, Vol. 9 &middot; performed by Ron Killings",
        "note": ("He raps his own entrance, and the crowd raps the hook back at him. When Metro "
                 "Boomin offered to produce a new theme in June 2025, right after the Ron Killings "
                 "rebrand, he said no: &ldquo;What&rsquo;s up ain&rsquo;t broken, I wanna keep "
                 "it.&rdquo; The phrase also named his finisher and, in 2026, half of his tag team."),
        "source_label": "Listen &middot; links",
        "links": [
            {"svc": "WWE.com", "sub": "Voices: WWE The Music, Vol. 9 · track 6",
             "href": "https://www.wwe.com/subscriptions/wwetunes/3242484/musicvol9"},
            {"svc": "Apple Music", "sub": "Search: R-Truth What's Up",
             "href": "https://music.apple.com/us/search?term=R-Truth%20What%27s%20Up"},
            {"svc": "YouTube", "sub": "Search: R-Truth theme",
             "href": "https://www.youtube.com/results?search_query=R-Truth+What%27s+Up+theme"},
        ],
        "lineage": [
            {"date": "2000", "title": "Rowdy", "who": "Ron Killings &middot; WWF, as K-Kwik"},
            {"date": "2002", "title": "Toma", "who": "Pitbull &middot; NWA-TNA"},
            {"date": "2008", "title": "What's Up?", "who": "R-Truth &middot; WWE", "now": True},
            {"date": "2011", "title": "Awesome Truth", "who": "with Jim Johnston &middot; with The Miz"},
            {"date": "2016", "title": "What's Up? (Golden Truth Remix)", "who": "with Goldust"},
        ],
        "foot": ('Sources: <a href="https://www.wwe.com/subscriptions/wwetunes/3242484/musicvol9" '
                 'target="_blank" rel="noopener">WWE.com</a>, '
                 '<a href="https://www.fightful.com/?p=232643" target="_blank" rel="noopener">Fightful</a>, '
                 '<a href="https://thesmackdownhotel.com/wrestlers/r-truth" target="_blank" '
                 'rel="noopener">TheSmackDownHotel</a> (lineage). No Spotify track id was verified, '
                 'so no player is embedded.'),
    },

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Ronnie Aaron Killings", sub="ring name Ron Killings, 2002&ndash;07 and 2025"),
        dict(label="Born", value="January 19, 1972",
             sub="Charlotte, North Carolina &middot; age 54 &middot; one database says Williamsburg, S.C."),
        dict(label="Billed from", value="Charlotte, North Carolina"),
        dict(label="Height", value="6&#8242;2&#8243;", sub="188 cm &middot; WWE.com"),
        dict(label="Weight", value="220 lb", sub="100 kg &middot; WWE.com; billed 235 lb before 2011"),
        dict(label="Debut", value="1999", sub="NWA Wildside as K-Krush; managed in PWF from 1997"),
        dict(label="WWE return", value="August 29, 2008", sub="SmackDown, def. Kenny Dykstra"),
        dict(label="Trained by", value="George South &middot; Manny Fernandez",
             sub="plus Chris Hamrick and Italian Stallion"),
        dict(label="Finisher", value="Lie Detector", sub="WWE.com&rsquo;s listed signature move"),
        dict(label="Last match", value="October 16, 2026",
             sub="L to Damian Priest by referee stoppage, SmackDown"),
        dict(label="Status", value="Injured, SmackDown", sub="no return date as of November 9, 2026"),
        dict(label="Also known as", value="K-Kwik &middot; K-Krush &middot; Ron Killings"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1972-01-19",
    bornplace="Charlotte, North Carolina, United States",
    nationality="United States",
    height_cm=188,
    weight_kg=100,
    ld=dict(
        alternateName=["Ron Killings", "Ronnie Aaron Killings", "K-Kwik", "K-Krush",
                       "Ron \"The Truth\" Killings"],
        award=["NWA World Heavyweight Championship (2 reigns, 2002 and 2004)",
               "WWE 24/7 Championship (54 reigns per WWE.com, 2019-2022)",
               "WWE United States Championship (2 reigns, 2010 and 2019)",
               "WWE Tag Team Championship (with Kofi Kingston, 2012; with Damian Priest, 2026)",
               "Raw / World Tag Team Championship (with The Miz, 2024)",
               "TNA World Tag Team Championship (with Adam Jones, 2007)",
               "NWA World Tag Team Championship (with 3 Live Kru, 2003)",
               "WWF Hardcore Championship (2 reigns, 2001)",
               "Mixed Match Challenge Season 2 winner (with Carmella, 2018)"],
        knowsAbout=["Professional wrestling", "WWE", "TNA Wrestling", "Hip hop music",
                    "Tag team wrestling"],
        description="R-Truth (Ronnie Aaron Killings) is an American professional wrestler and "
                    "rapper. As Ron Killings he won the NWA World Heavyweight Championship twice "
                    "in NWA-TNA, in 2002 and 2004. In WWE since 2008 he has won the United States "
                    "Championship twice, tag team titles with Kofi Kingston, The Miz and Damian "
                    "Priest, and a record 54 WWE 24/7 Championships. As of November 9, 2026 he is "
                    "on the SmackDown roster and out injured after an October 16, 2026 match.",
        sameAs=["https://x.com/RonKillings",
                "https://en.wikipedia.org/wiki/R-Truth",
                "https://www.wwe.com/superstars/r-truth"],
    ),
)
