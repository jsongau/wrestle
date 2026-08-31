# -*- coding: utf-8 -*-
"""Kurt Angle - dossier data.

Sources: web-verified August 31, 2026 (Wikipedia, POST Wrestling, TheMat.com/USA
Wrestling, Fightful). Every match row carries a day-precision date stated in those
sources or in the standard event record.

Deliberate omissions:
  * No career win-loss total - no verified figure exists across WWF/WWE and TNA and
    none is invented.
  * The WCW Championship reign during the 2001 Invasion is listed without an exact
    date - the air date was not verified in this pass.
  * No social links - handles were not verified in this pass.
  * No Observer star ratings in the signature block - none were verified against
    archives; the one award that is verified (PWI Match of the Year for WrestleMania
    21) is stated as an award, not a rating.
"""

# ----------------------------------------------------------------- record rows
ROWS = [
    dict(result="W", date="1999-11-14", promo="WWE", landmark=True,
         event="Survivor Series — Detroit", opponent="Shawn Stasiak",
         stip="Singles — televised debut, three years after the gold medal", title=""),
    dict(result="W", date="2000-10-22", promo="WWE", landmark=True,
         event="No Mercy — Albany", opponent="The Rock",
         stip="Singles — first WWF Championship, one year into his run", title="WWF Championship"),
    dict(result="W", date="2001-09-23", promo="WWE", landmark=True,
         event="Unforgiven — Pittsburgh", opponent="Stone Cold Steve Austin",
         stip="Singles — a second WWF Championship in his hometown", title="WWF Championship"),
    dict(result="W", date="2003-01-19", promo="WWE",
         event="Royal Rumble — Boston", opponent="Chris Benoit",
         stip="Singles — the technical match both men were measured by", title="WWE Championship"),
    dict(result="L", date="2003-03-30", promo="WWE", landmark=True,
         event="WrestleMania XIX — Seattle", opponent="Brock Lesnar",
         stip="Singles — wrestled with a broken neck; the botched Shooting Star Press finish", title="WWE Championship"),
    dict(result="W", date="2003-07-27", promo="WWE", type="tag",
         event="Vengeance — Denver", opponent="Brock Lesnar & Big Show",
         stip="Triple threat — a fourth and final WWE Championship", title="WWE Championship"),
    dict(result="W", date="2005-04-03", promo="WWE", landmark=True,
         event="WrestleMania 21 — Los Angeles", opponent="Shawn Michaels",
         stip="Singles — PWI Match of the Year", title=""),
    dict(result="L", date="2006-04-02", promo="WWE", landmark=True, type="tag",
         event="WrestleMania 22 — Chicago", opponent="Rey Mysterio & Randy Orton",
         stip="Triple threat — drops the World Heavyweight Championship to Mysterio without being pinned", title="World Heavyweight Championship"),
    dict(result="W", date="2006-11-19", promo="TNA", landmark=True,
         event="TNA Genesis", opponent="Samoa Joe",
         stip="Singles — ends Joe's undefeated streak in Angle's first TNA match", title=""),
    dict(result="W", date="2007-06-17", promo="TNA", landmark=True, type="tag",
         event="TNA Slammiversary", opponent="The King of the Mountain field",
         stip="King of the Mountain match — becomes the first TNA World Heavyweight Champion", title="TNA World Heavyweight Championship"),
    dict(result="L", date="2016-03-08", promo="TNA",
         event="Impact Wrestling", opponent="Bobby Lashley",
         stip="Singles — his TNA farewell match", title=""),
    dict(result="W", date="2017-10-22", promo="WWE", type="tag",
         event="TLC — Minneapolis", opponent="The Miz, Braun Strowman, Kane, Cesaro & Sheamus",
         stip="TLC handicap tag with Seth Rollins & Dean Ambrose — first WWE match in eleven years", title=""),
    dict(result="W", date="2018-04-08", promo="WWE", type="tag",
         event="WrestleMania 34 — New Orleans", opponent="Triple H & Stephanie McMahon",
         stip="Mixed tag with Ronda Rousey in her debut", title=""),
    dict(result="L", date="2019-04-07", promo="WWE", landmark=True,
         event="WrestleMania 35 — East Rutherford", opponent="Baron Corbin",
         stip="Farewell match — the retirement bout he has said he wishes had gone differently", title=""),
]

DATA = dict(
    slug="kurt-angle",
    name="Kurt Angle",
    realname="Kurt Steven Angle",
    epithet="The Olympic Hero",
    hook="Record & Titles",

    meta_desc=("Kurt Angle won Olympic gold in 1996 with a broken neck, then became a 13-time world "
               "champion across WWE and TNA. Full record, titles, factions, records and career."),
    og_desc=("The Olympic Hero: 1996 freestyle gold, four WWF/WWE Championships, six TNA World "
             "Championships, and the fastest rise from rookie to world champion of his era."),
    tw_desc="Olympic gold in 1996, a WWF Championship by 2000, thirteen world titles in all.",

    # ---------------------------------------------------------------- identity bar
    debut_label="EST.",
    debut_year="1998",
    height_imp="6&#8242;0&#8243;",
    weight_lb="220",
    world_titles="13",
    vitals_tagline="It&rsquo;s true, it&rsquo;s damn true",
    support_note="Merch &middot; Games &middot; Read",
    sp_items=[
        dict(ic="KA", title="WWE Alumni Profile", sub="WWE.com",
             tag="Visit", href="https://www.wwe.com/superstars/kurt-angle"),
        dict(ic="2K", title="WWE 2K", sub="Playable as a legend across the 2K series",
             tag="Play", href="https://wwe.2k.com/"),
        dict(ic="WWE", title="WWE Shop", sub="Olympic Hero merch",
             tag="Shop", href="https://shop.wwe.com/"),
        dict(ic="USA", title="USA Wrestling", sub="The women's freestyle program he fundraises for",
             tag="Give", charity=True, href="https://www.themat.com/"),
    ],

    # ---------------------------------------------------------------- hero
    hero_kick="Olympic gold medalist &middot; The Wrestling Machine &middot; the Three I&rsquo;s",
    hero_tag="Pittsburgh, Pennsylvania &middot; <em>1996 Olympics &middot; WWF/WWE &middot; TNA &middot; 1998&ndash;2019</em>",
    now_label="NOW",
    now_bold="Retired since WrestleMania 35",
    now_tail=" &middot; marked thirty years since the gold medal in July 2026, and spends his time on his family, his health and women&rsquo;s amateur wrestling",
    hstats=[
        dict(value="1996", x=False, label="Olympic Gold"),
        dict(value="13",   x=True,  label="World Titles"),
        dict(value="6",    x=True,  label="TNA World Titles"),
        dict(value="5",    x=False, label="Neck Surgeries"),
    ],
    ghost_link="From the Atlanta podium to the Pittsburgh ring",
    vlabel="Est. 1998 &middot; Pittsburgh, PA",
    mono="KA",

    # ---------------------------------------------------------------- 01 overview
    correction=1,
    overview=[
        "<b>Kurt Angle</b> is the only Olympic gold medalist to become a world champion in WWE, and "
        "the shorthand for his career is how little time the second half of that sentence took. He "
        "won freestyle gold in the 90&ndash;100 kg class at the 1996 Atlanta Games, made his "
        "televised WWF debut at Survivor Series on November 14, 1999, and beat The Rock for the WWF "
        "Championship at No Mercy on October 22, 2000 &mdash; champion inside his first year. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">13</span>'
        '<span class="pull-cap">world championship reigns across WWE and TNA &mdash; four WWF/WWE, one WCW, one World Heavyweight, six TNA, one IWGP</span></span>'
        "He is a thirteen-time world champion by Wikipedia&rsquo;s cross-promotion count, the 2000 "
        "King of the Ring, WWE&rsquo;s fifth Grand Slam champion and tenth Triple Crown winner, the "
        "first TNA World Heavyweight Champion, and a Hall of Famer in both companies &mdash; TNA in "
        "2013, WWE in 2017, inducted by John Cena.",

        "The line everyone knows &mdash; he &ldquo;won Olympic gold with a broken freakin&rsquo; "
        "neck&rdquo; &mdash; is true in substance and loose in timing, and the difference is worth "
        "stating. Angle fractured two cervical vertebrae, herniated two discs and pulled four "
        "muscles at the 1996 <b>Olympic Trials</b>, months before the Games. He competed in Atlanta "
        "while the injury healed, managing it rather than wrestling through a fresh break, and beat "
        "Abbas Jadidi in the final on July 31, 1996 by referees&rsquo; decision. The gimmick "
        "compressed the timeline; the medical file did not need the help. The neck it started with "
        "never really recovered: five neck surgeries and counting, by his own 2025 accounting.",

        "The WWE years, 1999&ndash;2006, are the most complete resume of his generation: title wins "
        "over The Rock and Steve Austin, the Royal Rumble 2003 match with Chris Benoit, the "
        "WrestleMania XIX main event against Brock Lesnar that he wrestled with a genuinely broken "
        "neck, and the WrestleMania 21 match with Shawn Michaels that took Pro Wrestling "
        "Illustrated&rsquo;s Match of the Year. "
        '<span class="pull" aria-hidden="true"><span class="pull-fig">6</span>'
        '<span class="pull-cap">TNA World Heavyweight Championship reigns &mdash; a record, starting with the title&rsquo;s creation in 2007</span></span>'
        "WWE released him at his own request in August 2006, citing health; TNA signed him within "
        "weeks, and he ended Samoa Joe&rsquo;s undefeated streak in his debut at Genesis on November "
        "19, 2006. He became the first TNA World Heavyweight Champion at Slammiversary on June 17, "
        "2007 and held the title a record six times, headlining the company for a decade before a "
        "farewell run in 2016.",

        "He returned to WWE in 2017 &mdash; Hall of Fame in the spring, Raw general manager by "
        "April, a ring return in the TLC main event that October &mdash; and retired at WrestleMania "
        "35 on April 7, 2019, losing to Baron Corbin in a farewell he has since said he wanted "
        "against a different opponent. The 2026 picture is a man doing the arithmetic on what the "
        "career cost: two knee replacements, two back surgeries, five neck operations, and his own "
        "June 2025 summary &mdash; &ldquo;I gave a lot to my sport and the business, but I&rsquo;m "
        "paying the price now.&rdquo; He calls himself semi-retired, marked the thirtieth "
        "anniversary of the gold medal on July 31, 2026, and has poured his competitive energy into "
        "fundraising for USA Wrestling&rsquo;s women&rsquo;s freestyle program while his "
        "eight-year-old daughter Nikoletta starts out in the sport &mdash; trained, at his "
        "insistence, by her uncle rather than by him.",
    ],

    # ---------------------------------------------------------------- 02 record
    record=dict(
        total=len(ROWS),
        full_label="Full record",
        promo_order=["WWE", "TNA"],
        promo_labels={"WWE": "WWF/WWE", "TNA": "TNA"},
        stats=[
            ("1996", "Olympic gold"),
            ("13&times;", "World champion"),
            ("4&times;", "WWF/WWE Champion"),
            ("6&times;", "TNA World Champion"),
            ("2000", "King of the Ring"),
            ("2", "Halls of Fame"),
        ],
        lead=("Fourteen documented bouts &mdash; the debut, the title wins, the broken-neck "
              "WrestleMania, both company farewells and the 2017 comeback. This is a curated ledger, "
              "not a career count, and no career win&ndash;loss total is published because no "
              "verified one exists. The WCW Championship win during the 2001 Invasion angle is "
              "absent as a row for the same reason: the exact air date was not verified in this "
              "pass. Filter by match type, tap any column header to sort, and turn spoilers on to "
              "reveal results."),
        rows=ROWS,
    ),

    # ---------------------------------------------------------------- 03 signature
    signature_lead=("The matches the reputation rests on. No Observer star ratings are published "
                    "here &mdash; none were verified against archives in this pass; the one verified "
                    "honor, PWI Match of the Year for WrestleMania 21, is listed as the award it "
                    "is."),
    signature=[
        dict(rating="—", event="WrestleMania 21 — Los Angeles", opponent="Shawn Michaels",
             stip="PWI Match of the Year 2005"),
        dict(rating="—", event="WrestleMania XIX — Seattle", opponent="Brock Lesnar",
             stip="Wrestled with a broken neck; the Shooting Star Press finish"),
        dict(rating="—", event="Royal Rumble 2003 — Boston", opponent="Chris Benoit",
             stip="WWE Championship — the technical benchmark of the era"),
        dict(rating="—", event="TNA Genesis 2006", opponent="Samoa Joe",
             stip="Ended Joe's undefeated streak in Angle's first TNA match"),
    ],
    signature_count_word="four",

    # ---------------------------------------------------------------- 04 titles
    titles=dict(
        stats=[
            ("13&times;", "World title reigns"),
            ("4&times;", "WWF/WWE Championship"),
            ("6&times;", "TNA World Championship"),
            ("5th", "WWE Grand Slam Champion"),
        ],
        lead=("Thirteen world championships across four sanctioning bodies, plus the midcard belts "
              "that made him WWE&rsquo;s fifth Grand Slam champion. Exact dates for the Invasion-era "
              "WCW reign and the 2000 Eurocontinental double were not verified in this pass and are "
              "given loosely rather than guessed."),
        rows=[
            dict(ic="W", name="WWF/WWE Championship", count="4",
                 sub="Def. The Rock at No Mercy, October 22, 2000; def. Steve Austin at Unforgiven "
                     "in Pittsburgh, September 23, 2001; a third reign in 2002; def. Lesnar and Big "
                     "Show in the Vengeance triple threat, July 27, 2003"),
            dict(ic="H", name="World Heavyweight Championship", count="1",
                 sub="Won the vacant title in a January 2006 SmackDown battle royal; lost it to Rey "
                     "Mysterio in the WrestleMania 22 triple threat on April 2, 2006 without being "
                     "pinned"),
            dict(ic="C", name="WCW Championship", count="1",
                 sub="Won from Booker T during the 2001 Invasion angle &mdash; exact air date not "
                     "verified in this pass"),
            dict(ic="T", name="TNA World Heavyweight Championship", count="6",
                 sub="The record. First champion, via King of the Mountain at Slammiversary, June "
                     "17, 2007; individual reign dates for the other five not itemised here"),
            dict(ic="I", name="IWGP Championship (Third Belt)", count="1",
                 sub="The 2007 offshoot lineage recognised by NJPW's partner promotions &mdash; the "
                     "reign that pushes cross-promotion counts to thirteen"),
            dict(ic="G", name="WWF Intercontinental &amp; European Championships", count="1 each",
                 sub="Held both simultaneously in early 2000 &mdash; the self-styled "
                     "&ldquo;Eurocontinental&rdquo; run &mdash; before dropping both at WrestleMania "
                     "2000 in a two-fall triple threat"),
            dict(ic="TT", name="WWE Tag Team Championship", count="1",
                 sub="With Chris Benoit, winning the tournament final over Edge & Rey Mysterio at No "
                     "Mercy, October 20, 2002 &mdash; the match that launched the SmackDown Six "
                     "tag division"),
            dict(ic="K", name="King of the Ring", count="2000",
                 sub="Won the tournament in his first full year; US Championship and Hardcore "
                     "Championship reigns also on the WWE ledger, completing the Grand Slam"),
        ],
    ),

    # ---------------------------------------------------------------- 05 factions
    slot5=dict(
        id="factions",
        h2="Factions",
        lead="A soloist by design &mdash; the units he did join existed to put his credentials at "
             "the center.",
        cards=[
            dict(era="WWE &middot; 2002&ndash;2003",
                 name="Team Angle",
                 members="Kurt Angle, Charlie Haas, Shelton Benjamin",
                 desc="Two decorated amateur wrestlers recruited as extensions of Angle's own "
                      "resume, complete with medals on their trunks. Haas and Benjamin took the "
                      "WWE Tag Team Championship as The World's Greatest Tag Team after Angle "
                      "dropped them, which rather proved the recruitment worked."),
            dict(era="TNA &middot; 2008&ndash;2009",
                 name="The Main Event Mafia",
                 members="Kurt Angle, Sting, Kevin Nash, Booker T, Scott Steiner",
                 desc="TNA's veterans-versus-originals faction, built on the conceit that every "
                      "member was a former world champion. Angle fronted it as 'the Godfather,' "
                      "and its war with the TNA Frontline was the company's central story through "
                      "2009."),
            dict(era="TNA &middot; 2007&ndash;2008",
                 name="The Angle Alliance",
                 members="Kurt Angle, Karen Angle, AJ Styles, Tomko",
                 desc="The champion's stable from his first TNA title runs — part protection "
                      "racket, part soap opera, with the on-screen marriage storyline doing as "
                      "much work as the wrestling."),
        ],
    ),

    # ---------------------------------------------------------------- 06 personas
    personas=dict(
        lead="One gimmick, played at different volumes for twenty years: the greatest amateur "
             "credentials in the business, weaponised. <b>Olympic Hero</b> &rarr; <b>Wrestling "
             "Machine</b> &rarr; <b>TNA founder-champion</b> &rarr; <b>GM</b> &rarr; retired "
             "ambassador.",
        cards=[
            dict(mono="OH", era="WWF/WWE &middot; 1999&ndash;2004", name="The Olympic Hero",
                 desc="The three I's — Intensity, Integrity, Intelligence — delivered with such "
                      "earnest smugness that crowds invented the 'you suck' chant to the beat of "
                      "his own theme. A milk truck, a tiny cowboy hat, and underneath it the best "
                      "pure wrestler in the company. The gimmick's genius was that the credentials "
                      "were real."),
            dict(mono="WM", era="WWE &middot; 2005&ndash;2006", name="The Wrestling Machine",
                 desc="The post-comedy version: shaved-down, short-form, snapping limbs on the "
                      "revived ECW brand. Born of a body that could no longer do long comedy "
                      "matches, and the last WWE persona before the 2006 release."),
            dict(mono="TN", era="TNA &middot; 2006&ndash;2016", name="The founding champion",
                 desc="TNA's biggest signing ever arrived as proof of concept and became its "
                      "first World Heavyweight Champion. Six reigns, the Main Event Mafia, and a "
                      "decade as the company's measuring stick — TNA Hall of Fame, 2013."),
            dict(mono="GM", era="WWE &middot; 2017&ndash;2019", name="The general manager",
                 desc="Raw GM from April 2017, the on-screen father figure of the Jason Jordan "
                      "storyline, and an in-ring farewell tour that ran from the TLC 2017 main "
                      "event to WrestleMania 35."),
            dict(mono="30", era="2019&ndash;present", name="The ambassador",
                 desc="Semi-retired by his own description: appearances, the thirty-year gold "
                      "medal anniversary in July 2026, fundraising for USA Wrestling's women's "
                      "freestyle program, and tournament weekends watching his daughter wrestle."),
        ],
    ),

    # ---------------------------------------------------------------- 07 career
    career=dict(
        lead="Atlanta 1996 to East Rutherford 2019 — the fastest rookie-to-champion arc of its era.",
        rows=[
            dict(year="1996", title="Olympic gold",
                 desc="Wins freestyle gold in the 90-100 kg class in Atlanta on July 31, beating "
                      "Abbas Jadidi by referees' decision, months after fracturing two vertebrae at "
                      "the Trials."),
            dict(year="1998", title="Signs with the WWF",
                 desc="First developmental match August 20, 1998; televised debut at Survivor "
                      "Series on November 14, 1999."),
            dict(year="2000", title="King of the Ring, then champion",
                 desc="Wins the 2000 King of the Ring, then beats The Rock at No Mercy on October "
                      "22 for the WWF Championship — champion within a year of debuting."),
            dict(year="2001", title="Hometown title win",
                 desc="Beats Steve Austin at Unforgiven in Pittsburgh on September 23; also holds "
                      "the WCW Championship during the Invasion."),
            dict(year="2003", title="The broken-neck main event",
                 desc="Retains against Benoit at the Royal Rumble on January 19, then drops the "
                      "title to Brock Lesnar at WrestleMania XIX on March 30 with a fractured "
                      "neck; regains it at Vengeance on July 27."),
            dict(year="2005", title="WrestleMania 21",
                 desc="Beats Shawn Michaels on April 3 — PWI Match of the Year."),
            dict(year="2006", title="Release and reinvention",
                 desc="Loses the World Heavyweight Championship to Rey Mysterio at WrestleMania 22 "
                      "on April 2; released at his own request in August over health concerns; "
                      "debuts in TNA and ends Samoa Joe's streak at Genesis on November 19."),
            dict(year="2007", title="First TNA World Heavyweight Champion",
                 desc="Wins King of the Mountain at Slammiversary on June 17 — the first of a "
                      "record six reigns."),
            dict(year="2013", title="TNA Hall of Fame",
                 desc="Inducted while still an active headliner; TNA farewell match follows on "
                      "March 8, 2016, against Bobby Lashley."),
            dict(year="2017", title="WWE Hall of Fame and the comeback",
                 desc="Inducted by John Cena; Raw general manager from April; returns to the ring "
                      "in the TLC main event on October 22."),
            dict(year="2019", title="The farewell",
                 desc="Loses to Baron Corbin at WrestleMania 35 on April 7 — the retirement match "
                      "he has said he wanted against John Cena instead."),
            dict(year="2026", title="Thirty years on",
                 desc="Marks the gold medal's 30th anniversary on July 31; semi-retired, "
                      "fundraising for women's amateur wrestling, managing a body with five neck "
                      "surgeries, two knee replacements and two back operations behind it."),
        ],
    ),

    # ---------------------------------------------------------------- 08 rivalries
    rivalries=dict(
        lead="Who he went to war with.",
        cards=[
            dict(name="Brock Lesnar",
                 desc="The next-generation monster against the shrinking-spine technician: the "
                      "WrestleMania XIX main event of March 30, 2003, wrestled on a neck Angle "
                      "knew was broken, ending with Lesnar's under-rotated Shooting Star Press. "
                      "The SummerSlam 2003 rematch and an Iron Man match followed. It is the "
                      "rivalry that defines both the peak and the price of the WWE years."),
            dict(name="Shawn Michaels",
                 desc="Built on a single question — Mr. WrestleMania against the Olympian who'd "
                      "never faced him — and paid off at WrestleMania 21 on April 3, 2005, with "
                      "Angle winning by ankle lock. PWI's Match of the Year; their Vengeance 2005 "
                      "rematch went the other way."),
            dict(name="Chris Benoit",
                 desc="The Royal Rumble 2003 title match is the purest expression of what both men "
                      "did: thirty minutes of escalating counter-wrestling that ended careers' "
                      "worth of 'best technical match' arguments. They were also tag champions "
                      "together, winning the 2002 tournament final over Edge & Rey Mysterio."),
            dict(name="Samoa Joe",
                 desc="TNA's marquee feud: the undefeated homegrown monster against the imported "
                      "legend. Angle took Joe's streak in his very first TNA match at Genesis on "
                      "November 19, 2006, and the series ran through Lockdown's cage and years of "
                      "title programs. It made TNA feel, briefly, like a real alternative."),
            dict(name="Rey Mysterio",
                 desc="Threaded through both careers: opponents in the 2002 SmackDown Six tag "
                      "division, then the WrestleMania 22 triple threat on April 2, 2006, where "
                      "Mysterio took Angle's World Heavyweight Championship without Angle being "
                      "pinned — a finish Angle has grumbled about, entertainingly, ever since."),
            dict(name="Eddie Guerrero",
                 desc="WrestleMania XX and the 2004 SmackDown main-event scene — the champion "
                      "cheating to survive against the wrestling machine. Their chemistry made "
                      "Guerrero's title reign feel earned, and Angle has called him one of the "
                      "best he ever worked."),
        ],
    ),

    # ---------------------------------------------------------------- 09 media
    media=dict(
        h2="Media &amp; Beyond",
        lead="Thin by choice — the verified list, without padding.",
        rows=[
            dict(when="2001", title="It's True, It's True", kind="Book",
                 desc="The autobiography, written at the peak of the Olympic Hero run."),
            dict(when="2011", title="Warrior", kind="Film",
                 desc="Plays the Russian MMA monster Koba in the Tom Hardy fight drama — his most "
                      "visible acting credit among a run of smaller film roles."),
            dict(when="2021&ndash;", title="The Kurt Angle Show", kind="Podcast",
                 desc="Week-by-week career retrospective podcast; also the venue for his frank "
                      "running commentary on his surgeries."),
            dict(when="2022&ndash;", title="WWE 2K", kind="Game",
                 desc="Playable as a legend across current WWE 2K entries."),
            dict(when="2025&ndash;", title="USA Wrestling fundraising", kind="Advocacy",
                 desc="Raising money for women's freestyle stipends and campus clubs, with the "
                      "stated goal of making Pennsylvania the top women's wrestling state "
                      "(TheMat.com, July 2025)."),
        ],
    ),

    # ---------------------------------------------------------------- 10 feats
    slot10=dict(
        id="feats",
        lead="The records, with the caveats the retellings drop.",
        stats=[
            ("1996", "Olympic gold"),
            ("13", "World title reigns"),
            ("~1yr", "Debut to WWF Champion"),
        ],
        rows=[
            dict(name="Olympic gold medal, freestyle wrestling, 1996",
                 sub="90-100 kg class, Atlanta, beating Abbas Jadidi in the July 31 final by "
                     "referees' decision. The broken neck — two fractured vertebrae, two herniated "
                     "discs — happened at the Trials months earlier; he competed at the Games while "
                     "it healed. Still the only Olympic gold medalist to headline WWE."),
            dict(name="WWF Champion within a year of his televised debut",
                 sub="Survivor Series, November 14, 1999 to No Mercy, October 22, 2000 — with King "
                     "of the Ring collected on the way. The fastest credential-stacking rookie year "
                     "in company history."),
            dict(name="Thirteen world championship reigns",
                 sub="Four WWF/WWE, one World Heavyweight, one WCW, six TNA, one IWGP (Third Belt) "
                     "— the cross-promotion count as Wikipedia tallies it. WWE's own materials "
                     "count only the six under its banner, which is why published totals vary."),
            dict(name="Fifth Grand Slam champion, tenth Triple Crown winner in WWE",
                 sub="World, Intercontinental, European, tag and more — the full set, including the "
                     "simultaneous IC-and-European 'Eurocontinental' spell of early 2000."),
            dict(name="First and six-time TNA World Heavyweight Champion",
                 sub="From the title's creation at Slammiversary 2007 — still the record for that "
                     "championship."),
            dict(name="The broken-neck WrestleMania XIX main event",
                 sub="March 30, 2003, against Brock Lesnar — wrestled on a neck that needed "
                     "surgery, ending with the botched Shooting Star Press that could have broken "
                     "Lesnar's. Angle had the title back by July."),
            dict(name="Two Halls of Fame",
                 sub="TNA in 2013, while active; WWE in 2017, inducted by John Cena."),
            dict(name="The medical bill",
                 sub="By his own 2025 accounting: five neck surgeries, two knee replacements, two "
                     "back operations, shoulder replacements pending — 'I gave a lot to my sport "
                     "and the business, but I'm paying the price now.'"),
        ],
        footnote=("Two counts are deliberately hedged. The thirteen world titles is Wikipedia's "
                  "cross-promotion figure — WWE materials recognise six, TNA six, and the IWGP "
                  "Third Belt reign is the disputed thirteenth. And no career win-loss record is "
                  "published, because no verified total exists."),
    ),

    # ---------------------------------------------------------------- 11 reference
    reference=[
        dict(k="Wikipedia", v="Full biography", href="https://en.wikipedia.org/wiki/Kurt_Angle"),
        dict(k="POST Wrestling", v="30th anniversary of the gold medal, July 2026",
             href="https://www.postwrestling.com/2026/07/31/kurt-angle-celebrates-30th-anniversary-of-his-olympic-gold-medal-victory/"),
        dict(k="POST Wrestling", v="&ldquo;I&rsquo;m paying the price now&rdquo; &mdash; health, June 2025",
             href="https://www.postwrestling.com/2025/06/27/kurt-angle-i-gave-a-lot-to-my-sport-and-the-business-but-im-paying-the-price-now/"),
        dict(k="USA Wrestling", v="The wrestling dad backing women&rsquo;s freestyle, July 2025",
             href="https://www.themat.com/news/2025/july/31/olympic-champion-and-wwe-star-kurt-angle-is-a-wrestling-dad-stepping-up-to-support-women-s-wrestling"),
        dict(k="Fightful", v="The neck-fusion file, 2023",
             href="https://www.fightful.com/wrestling/kurt-angle-says-neck-surgery-next-him-i-m-probably-going-have-fusion-next-year/"),
    ],

    # ---------------------------------------------------------------- 12 faq
    faq=[
        dict(
            q="Did Kurt Angle really win Olympic gold with a broken neck?",
            a="Yes, with one timing correction the gimmick always skipped: the break happened at the "
              "1996 Olympic <b>Trials</b>, months before the Games &mdash; two fractured cervical "
              "vertebrae, two herniated discs, four pulled muscles. He competed in Atlanta while the "
              "injury healed and beat Abbas Jadidi in the 90&ndash;100 kg freestyle final on July "
              "31, 1996 by referees&rsquo; decision. So: gold medal, genuinely broken neck, several "
              "months apart &mdash; which is barely less absurd than the catchphrase version.",
            q_ld="Did Kurt Angle really win his Olympic gold medal with a broken neck?",
            a_ld="Substantially yes, with one timing caveat. Kurt Angle fractured two cervical "
                 "vertebrae, herniated two discs and pulled four muscles at the 1996 Olympic "
                 "Trials, months before the Games. He competed at the Atlanta Olympics while the "
                 "injury was healing and won gold in the 90-100 kg freestyle class on July 31, "
                 "1996, defeating Abbas Jadidi in the final by referees' decision."),
        dict(
            q="How many world titles has Kurt Angle won?",
            a="Thirteen by the cross-promotion count: four WWF/WWE Championships, one World "
              "Heavyweight Championship, one WCW Championship (during the 2001 Invasion), a record "
              "six TNA World Heavyweight Championships, and one IWGP Championship of the 2007 "
              "&ldquo;Third Belt&rdquo; lineage. WWE&rsquo;s own materials count only the six reigns "
              "under its banner, which is why you will see different totals in different places.",
            q_ld="How many world championships has Kurt Angle won?",
            a_ld="Thirteen by the cross-promotion count: four WWF/WWE Championships, one World "
                 "Heavyweight Championship, one WCW Championship, six TNA World Heavyweight "
                 "Championships, which is the record for that title, and one IWGP Championship of "
                 "the Third Belt lineage. WWE's own materials count only the six reigns that "
                 "happened under its banner."),
        dict(
            q="Is Kurt Angle retired, and what is he doing in 2026?",
            a="Fully retired since losing to Baron Corbin at WrestleMania 35 on April 7, 2019, and "
              "he has been explicit that his body has no comeback in it: five neck surgeries, two "
              "knee replacements, two back operations, and shoulder work still pending. In 2026 he "
              "calls himself semi-retired in the working sense &mdash; appearances, his podcast "
              "archive, fundraising for USA Wrestling&rsquo;s women&rsquo;s freestyle program &mdash; "
              "and he marked the thirtieth anniversary of the gold medal on July 31, 2026. His "
              "daughter Nikoletta has started amateur wrestling; he refuses to be her coach so he "
              "can stay her dad.",
            q_ld="Is Kurt Angle retired, and what is he doing in 2026?",
            a_ld="Kurt Angle has been retired since losing to Baron Corbin at WrestleMania 35 on "
                 "April 7, 2019. As of 2026 he describes himself as semi-retired, making "
                 "appearances, fundraising for USA Wrestling's women's freestyle program, and "
                 "supporting his young daughter Nikoletta's start in amateur wrestling. He has had "
                 "five neck surgeries, two knee replacements and two back operations, and marked "
                 "the 30th anniversary of his Olympic gold medal on July 31, 2026."),
        dict(
            q="Why did Kurt Angle leave WWE for TNA in 2006?",
            a="WWE granted him a release in August 2006 over health concerns &mdash; the neck, the "
              "schedule, and by his own later admission the painkiller addiction he has since "
              "beaten. TNA signed him within weeks. The move gave TNA the biggest name it ever "
              "acquired and gave Angle another decade: the first TNA World Heavyweight Championship "
              "at Slammiversary on June 17, 2007, six reigns in all, and the 2013 TNA Hall of Fame "
              "before the 2017 WWE reconciliation.",
            q_ld="Why did Kurt Angle leave WWE for TNA in 2006?",
            a_ld="WWE released Kurt Angle at his own request in August 2006, citing health "
                 "concerns including his neck injuries; Angle later acknowledged painkiller "
                 "addiction during that period, which he has since overcome. He signed with TNA "
                 "weeks later, ended Samoa Joe's undefeated streak in his debut, became the first "
                 "TNA World Heavyweight Champion on June 17, 2007, and won that title a record six "
                 "times before returning to WWE in 2017."),
        dict(
            q="What was Kurt Angle&rsquo;s last match?",
            a="WrestleMania 35, April 7, 2019 &mdash; a loss to Baron Corbin in his announced "
              "farewell match. He has said repeatedly since that he wished the opponent had been "
              "John Cena, who had faced him in his 2002 televised debut match and inducted him into "
              "the Hall of Fame in 2017. WWE released him from his backstage role in the April 2020 "
              "budget cuts, and he has not wrestled since.",
            q_ld="What was Kurt Angle's last match?",
            a_ld="Kurt Angle's last match was at WrestleMania 35 on April 7, 2019, a loss to Baron "
                 "Corbin in his farewell match. He has said he wished the opponent had been John "
                 "Cena, whose first televised WWE match in 2002 was against Angle and who inducted "
                 "Angle into the WWE Hall of Fame in 2017."),
    ],

    # ---------------------------------------------------------------- rail
    tape=[
        dict(label="Real name", value="Kurt Steven Angle"),
        dict(label="Born", value="December 9, 1968",
             sub="Mt. Lebanon, Pennsylvania &middot; age 57"),
        dict(label="Billed from", value="Pittsburgh, Pennsylvania"),
        dict(label="Height", value="6&#8242;0&#8243;", sub="183 cm"),
        dict(label="Weight", value="220 lb", sub="100 kg (billed)"),
        dict(label="Debut", value="August 20, 1998",
             sub="developmental, vs. Tom Prichard; televised debut November 14, 1999 at Survivor Series"),
        dict(label="Trained by", value="WWF developmental system",
             sub="after a lifetime of amateur wrestling &mdash; 1995 world freestyle champion, 1996 Olympic gold"),
        dict(label="Signature", value="Angle Slam &middot; Ankle lock &middot; moonsault",
             sub="the ankle lock usually with the grapevine"),
        dict(label="Entrance theme", value="&ldquo;Medal&rdquo; by Jim Johnston",
             sub="the theme the &ldquo;you suck&rdquo; chant was built on"),
        dict(label="Last match", value="April 7, 2019", sub="WrestleMania 35, vs. Baron Corbin"),
        dict(label="Halls of Fame", value="TNA 2013 &middot; WWE 2017", sub="inducted by John Cena"),
        dict(label="Also known as", value="The Olympic Hero &middot; The Wrestling Machine"),
    ],

    # ---------------------------------------------------------------- JSON-LD
    born_iso="1968-12-09",
    bornplace="Mt. Lebanon, Pennsylvania",
    nationality="United States",
    height_cm=183,
    weight_kg=100,
    ld=dict(
        alternateName=["Kurt Steven Angle", "The Olympic Hero", "The Wrestling Machine"],
        award=["Olympic gold medal, freestyle wrestling 90-100 kg (1996)",
               "WWF/WWE Championship (4 reigns)",
               "World Heavyweight Championship (1 reign)",
               "WCW Championship (1 reign)",
               "TNA World Heavyweight Championship (record 6 reigns)",
               "IWGP Championship, Third Belt lineage (1 reign)",
               "WWE King of the Ring (2000)",
               "WWE Tag Team Championship (1 reign, with Chris Benoit)",
               "WWF Intercontinental Championship",
               "WWF European Championship",
               "TNA Hall of Fame (2013)",
               "WWE Hall of Fame (2017)"],
        knowsAbout=["Professional wrestling", "Freestyle wrestling", "Olympic Games", "WWE", "TNA",
                    "Amateur wrestling development"],
        description="Kurt Angle, born Kurt Steven Angle in Mt. Lebanon, Pennsylvania, is a retired "
                    "American professional wrestler and 1996 Olympic gold medalist in freestyle "
                    "wrestling. He won the WWF/WWE Championship four times, the World Heavyweight "
                    "and WCW Championships once each, and a record six TNA World Heavyweight "
                    "Championships as that title's first holder. He won King of the Ring in 2000, "
                    "became WWE's fifth Grand Slam champion, and was inducted into the TNA Hall of "
                    "Fame in 2013 and the WWE Hall of Fame in 2017. His farewell match was at "
                    "WrestleMania 35 on April 7, 2019.",
        sameAs=["https://en.wikipedia.org/wiki/Kurt_Angle",
                "https://www.wwe.com/superstars/kurt-angle"],
    ),
)
