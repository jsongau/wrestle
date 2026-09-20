#!/usr/bin/env python3
"""add_week_0907.py - open the week of Sep 7 - Sep 13, 2026 (complete week).

    WL_ROOT="$PWD" python3 build/add_week_0907.py

Idempotent. Run AFTER fill_week_0831.py and BEFORE add_week_0914.py -
gallery weeks PREPEND, and WEEKS[0] drives the homepage This-Week block,
so oldest-first ordering leaves the newest week on top.

ASSEMBLY DECISIONS (three research agents, one lane each, Sep 20 assembly):
 - The week's lead is Sami Zayn winning the Undisputed WWE Title from CM
   Punk on the Sep 11 SmackDown at Arena CDMX (lead=True, mono="WWE Title").
   Verified against WWE.com's own results headline; ends Punk's 67-day
   reign. A later agent note placing the win at SNME Sep 13 was a
   hallucinated date and was overridden by the primary source.
 - ADDED beyond the agent lanes: Stephanie Vaquer beat Liv Morgan for the
   Women's World Title at a WWE live event in Chile on Sep 12 (POST
   Wrestling). It completes the arc the Sep 7 Raw row opens - Morgan
   retained on TV, then lost the belt five nights later off TV. Filed
   official=False from POST; a rare untelevised title change is exactly
   what the feed exists to record.
 - home=True budget (3-5): kept FIVE - Morgan (9/7), Nemeth (9/10),
   Zayn (9/11), Vaquer (9/12), the Andy Williams tribute (9/12). The
   Ospreay eliminator and the Kelani Jordan NXT rows arrived flagged
   home=True from agents and were DEMOTED to stay inside the cap.
 - Two agents returned htags as Python lists (["titles","rivalries"]);
   converted to the space-separated strings the rail filter expects.
   htags dropped entirely from demoted rows - htags ride with home=True.
 - The Butcher tribute row is anchored to the Sep 12 Collision show (in
   window), sourced to AEW's official recap; the death itself is filed in
   the 0831 week where it belongs.
 - Sep 11 SmackDown undercard (Green over Jax, Fenix over Saints, Bella
   over Paige) verified but not filed - six WWE rows already carry the
   week and the feed is a digest, not a results page.
 - All 7 video IDs oEmbed-verified: WWE (4), All Elite Wrestling (2 of 3
   AEW), TNA Wrestling (1). NXT tuples ride under the NXT promo key.
"""
import os

ROOT = os.environ.get("WL_ROOT", os.getcwd())

DISPATCH_BLOCK = '''
  # ================= WEEK OF SEPTEMBER 7 - SEPTEMBER 13, 2026 =================
  # Backfilled Sep 20. Zayn ends Punk's reign in Mexico City; Vaquer takes the
  # Women's World Title in Chile; AEW mourns The Butcher. See build/add_week_0907.py.

  # ---- WWE: Raw Sep 7 + SmackDown Sep 11 (Arena CDMX, Mexico City) ----
  dict(date="2026-09-11", promo="wwe", cat="title", official=True, who="Sami Zayn", lead=True, mono="WWE Title", home=True, htags="titles matches",
       hl="Sami Zayn stuns CM Punk to capture Undisputed WWE Championship in Mexico City",
       dek="Kevin Owens accidentally struck Punk with the belt and Zayn followed with a Helluva Kick to win the title at Arena CDMX, ending Punk's 67-day reign.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-09-11"),
  dict(date="2026-09-07", promo="wwe", cat="title", official=True, who="Liv Morgan", home=True, htags="titles rivalries",
       hl="Liv Morgan retains Women's World Title over Stephanie Vaquer with Judgment Day help",
       dek="Raquel Rodriguez and Roxanne Perez ran interference and Becky Lynch tried to even the odds, but Morgan struck Vaquer with the belt and hit Oblivion to retain on Raw.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-09-07"),
  dict(date="2026-09-12", promo="wwe", cat="title", official=False, who="Stephanie Vaquer", home=True, htags="titles",
       hl="Stephanie Vaquer beats Liv Morgan for Women's World Title at live event in Chile",
       dek="Five nights after falling to Morgan on Raw, Vaquer captured the Women's World Championship at a WWE live event in her native Chile, a rare title change away from television.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/09/12/stephanie-vaquer-wins-wwe-womens-world-championship-at-live-event-in-chile/"),
  dict(date="2026-09-07", promo="wwe", cat="return", official=True, who="Bayley",
       hl="Bayley makes shocking return during Money in the Bank qualifier on Raw",
       dek="Bayley pulled the referee out of the ring to cost Lyra Valkyria, allowing Sol Ruca to hit the Sol Snatcher and qualify for the Money in the Bank ladder match.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-09-07"),
  dict(date="2026-09-07", promo="wwe", cat="event", official=True, who="Bron Breakker",
       hl="Money in the Bank qualifiers begin as arson angle closes out Raw",
       dek="Bron Breakker speared Rey Mysterio to win a triple threat qualifier. Royce Keys, Bronco Nima and Lucien Price set The Usos car ablaze in an ominous warning.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-09-07"),
  dict(date="2026-09-08", promo="wwe", cat="business", official=True, who="WWE",
       hl="WWE announces eight new Raw and SmackDown dates across the United States",
       dek="The fall and winter run adds stops including Greenville, Fort Lauderdale, Raleigh, Wichita and Toledo from November 9 through December 7, with presale opening September 10.",
       src="WWE Corporate", url="https://corporate.wwe.com/about/news/2026/09-08-2026"),
  dict(date="2026-09-12", promo="wwe", cat="media", official=True, who="Cody Rhodes",
       hl="Cody Rhodes misses advertised Mexico City SmackDown, sit-down interview set",
       dek="Rhodes was advertised but did not appear following his Sunday Night's Main Event loss to Randy Orton. WWE announced a Michael Cole sit-down interview for the September 18 SmackDown in Corpus Christi.",
       src="TJRWrestling", url="https://tjrwrestling.net/news/cody-rhodes-immediate-wwe-future-confirmed/"),
  dict(date="2026-09-12", promo="wwe", cat="media", official=True, who="CM Punk",
       hl="CM Punk breaks silence on Instagram after losing WWE Title to Sami Zayn",
       dek="Punk posted to Instagram Stories that winners lose way more than losers do and vowed I will get MY title back, signing off BITW.",
       src="F4W Online", url="https://www.f4wonline.com/news/wwe/cm-punk-issues-statement-after-losing-wwe-title-to-sami-zayn/"),

  # ---- AEW: Rebel Heart Dynamite Sep 9 + Collision Sep 12 ----
  dict(date="2026-09-12", promo="aew", cat="passing", official=True, who="Andy Williams", home=True, htags="roster",
       hl="AEW honors Andy Williams as Daniel Garcia wins Butcher Battle Royale for charity",
       dek="Collision in Springfield opened with a 10-bell salute for The Butcher, dead at 48, with tributes from Brody King, Colt Cabana, Jeff Jarrett and a note from The Blade read by Tony Schiavone. Garcia last eliminated Josh Alexander to win the 12-man Butcher Battle Royale, earning 100,000 dollars for charity in Williams' memory and receiving his guitar.",
       src="All Elite Wrestling", url="https://www.allelitewrestling.com/post/aew-collision-results-september-12-2026"),
  dict(date="2026-09-09", promo="aew", cat="event", official=True, who="Will Ospreay",
       hl="Will Ospreay pins David Finlay in eliminator as Jon Moxley watches from commentary",
       dek="On the Rebel Heart edition of Dynamite from Akins Ford Arena in Athens, Georgia, world champion Ospreay countered a Finlay powerbomb and pinned him to keep his All Out date with Moxley intact. Andrade El Idolo retained the National Championship over The Beast Mortos, and the show opened with an In Memory Of graphic for Andy Williams plus a farewell ovation for Rebel.",
       src="WrestleView", url="https://www.wrestleview.com/top-story/392277-aew-dynamite-results-9-9-26-rebel-heart-dynamite-title-matches-return-of-the-waiting-room-and-more/"),
  dict(date="2026-09-09", promo="aew", cat="title", official=True, who="Swerve Strickland",
       hl="Swerve Strickland and New Level retain AEW World Trios titles on Rebel Heart Dynamite",
       dek="Strickland, Kofi and Austin Creed hit the Daybreak to put away Orange Cassidy, Kyle O'Reilly and Roderick Strong of the Conglomeration. Britt Baker also tapped out Hyan with the Lockjaw in six-woman action alongside new TBS champion Persephone and Hikaru Shida.",
       src="PWMania", url="https://www.pwmania.com/aew-dynamite-results-september-9-2026"),
  dict(date="2026-09-10", promo="aew", cat="media", official=False, who="Will Ospreay",
       hl="Ospreay clips drive AEW YouTube numbers after emotional Rebel Heart edition of Dynamite",
       dek="Eleven hours after upload, Rebel Heart Dynamite videos totaled 907k tracked views, with Ospreay-related clips at 252k, or 27.8 percent of all episode uploads. The top single video was Rebel handing Britt Baker her signature glove at 110k views.",
       src="F4W Online", url="https://www.f4wonline.com/news/aew/aew-dynamite-rebel-heart-youtube-metrics/"),
  dict(date="2026-09-12", promo="aew", cat="event", official=True, who="Jon Moxley",
       hl="Jon Moxley turns away Mike Bailey on Collision as Mercedes Mone watches from commentary",
       dek="Moxley hit the Death Rider near the 20-minute limit to win a Continental Title eliminator two weeks before challenging Ospreay at All Out. Women's world champion Mone sat in on commentary for Queen Aminata's win over Mina Shirakawa, PAC and The Dogs beat Bang Bang Gang, and AEW announced Blood and Guts for November 4 in Jacksonville.",
       src="Fightful", url="https://www.fightful.com/wrestling/aew-collision-results-9-12-2026-tribute-to-the-butcher-andy-williams/"),

  # ---- NXT Sep 8 / TNA Sep 10 / NJPW / RAF / industry ----
  dict(date="2026-09-10", promo="tna", cat="event", official=True, who="Nic Nemeth", home=True, htags="titles rivalries",
       hl="Nic Nemeth uses wrench to retain TNA World Title over Matt Hardy",
       dek="Nemeth beat Hardy in a No Disqualification main event in Brampton after Ryan Nemeth pulled the referee from the ring and a wrench shot set up the pin. Xia Brookside retained the Knockouts World Title over Gabby Forza with a belt shot behind the referee's back.",
       src="TNA Wrestling", url="https://tnawrestling.com/news/tna-thursday-night-impact-on-amc-results-september-10-2026"),
  dict(date="2026-09-08", promo="nxt", cat="event", official=False, who="Kelani Jordan",
       hl="Kelani Jordan retains NXT Women's Title as Waller challenger picture takes shape",
       dek="Jordan beat Jaida Parker and was attacked afterward by Wren Sinclair, who was suspended by Robert Stone; Jackson Drake also retained the North American Title over Tavion Heights. Tony D'Angelo, Mason Rook and Saquon Shugars won a six-man qualifier, setting next week's triple threat to name NXT Champion Grayson Waller's next challenger.",
       src="eWrestlingNews", url="https://www.ewrestlingnews.com/results/nxt-results/wwe-nxt-results-september-8-2026"),
  dict(date="2026-09-10", promo="tna", cat="event", official=True, who="Leon Slater",
       hl="Leon Slater found unconscious as Bound for Glory world title build turns violent",
       dek="Slater, who challenges Nemeth for the TNA World Title at Bound for Glory, was found laid out backstage before the main event, with the Nemeth brothers implicated. Frankie Kazarian accepted Moose's challenge for next week on the condition that Moose's entire TNA career is on the line.",
       src="TNA Wrestling", url="https://tnawrestling.com/news/tna-thursday-night-impact-on-amc-results-september-10-2026"),
  dict(date="2026-09-09", promo="njpw", cat="event", official=False, who="Hirooki Goto",
       hl="Goto and YOH beat Tsuji and Ishimori on Road to Destruction in Tokyo",
       dek="Hirooki Goto and YOH downed IWGP Heavyweight Champion Yota Tsuji and Taiji Ishimori in 13:30 at Korakuen Hall ahead of Goto's title challenge at Destruction in Kobe on September 27. Claudio Castagnoli also appeared on screen and accepted Shingo Takagi's challenge for the Kobe card.",
       src="Fightful", url="https://www.fightful.com/wrestling/njpw-road-to-destruction-results-9-9/"),
  dict(date="2026-09-08", promo="raf", cat="event", official=False, who="Khamzat Chimaev",
       hl="RAF 13 card finalized with Covington-Muhammad headliner and quick Chimaev return against Burns",
       dek="Real American Freestyle confirmed the full lineup for the Fox Nation card in Miami, topped by Colby Covington vs Belal Muhammad in a cruiserweight crossover bout. Khamzat Chimaev meets Gilbert Burns two weeks after beating Tyron Woodley at RAF Moscow, with Kennedy Blades vs Diana Avsaragova and Austin DeSanto vs Arsen Harutyunyan also set.",
       src="Sherdog", url="https://www.sherdog.com/news/news/RAF-13-full-card-confirmed-with-CovingtonMuhammad-ChimaevBurns-202730"),
  dict(date="2026-09-11", promo="industry", cat="media", official=False, who="Brandon Thurston",
       hl="TNA Impact on AMC drew 184,000 viewers for September 3 episode",
       dek="Per Wrestlenomics figures cited by Pro Wrestling Dot Net, the show did a 0.03 rating in 18-49 against college football competition. The counts exclude AMC+ and TNA+ streaming viewership.",
       src="Pro Wrestling Dot Net", url="https://prowrestling.net/site/2026/09/11/tna-impact-rating-9-3-how-did-the-final-show-fare-heading-into-labor-day-weekend/"),
  dict(date="2026-09-13", promo="industry", cat="media", official=False, who="Brandon Thurston",
       hl="NXT Heatwave fallout episode jumps to 768,000 viewers and 0.17 demo rating",
       dek="The September 1 NXT on The CW rose sharply from the prior week's 632,000 viewers and 0.09 demo, and topped the comparable 2025 episode's 654,000. ESPN Unlimited streaming figures are excluded from the counts.",
       src="Pro Wrestling Dot Net", url="https://prowrestling.net/site/2026/09/13/nxt-tv-rating-9-1-did-the-numbers-improve-for-the-nxt-heatwave-fallout-show/"),
  # =============== end week of September 7 - September 13, 2026 ===============
'''

GALLERY_BLOCK = '''  {"week":"2026-09-07","label":"Week of September 7, 2026","start":datetime.date(2026,9,7),"promos":{
     "WWE":[("xqJShWjSl54","2026-09-07","Raw \\u00b7 Liv Morgan vs. Stephanie Vaquer Women's World Title match"),("G4vd2W-87mI","2026-09-07","Raw \\u00b7 Bayley returns; Sol Ruca qualifies for Money in the Bank"),("lNlvNejNtDE","2026-09-11","SmackDown \\u00b7 Sami Zayn wins WWE Title in chaotic match against CM Punk"),("tjle7ArGJJ0","2026-09-11","SmackDown \\u00b7 Full highlights from Mexico City")],
     "AEW":[("BAyFq4bb3vg","2026-09-09","Dynamite \\u00b7 Will Ospreay defends against David Finlay in a world title eliminator at Rebel Heart"),("54zi-ZL557E","2026-09-12","Collision \\u00b7 The Butcher Battle Royale honors Andy Williams, won by Daniel Garcia"),("WGvgsrKVQq8","2026-09-12","Collision \\u00b7 Jon Moxley vs Speedball Mike Bailey in a Continental Title eliminator")],
     "NXT":[("wV2oAkgoySU","2026-09-08","NXT \\u00b7 Full highlights from the September 8 episode"),("irVQC190THI","2026-09-08","NXT \\u00b7 Kelani Jordan vs. Jaida Parker, NXT Women's Championship full match")],
     "TNA":[("bKPsplrBxHc","2026-09-10","iMPACT \\u00b7 Nic Nemeth vs. Matt Hardy, No DQ TNA World Title match")]
  }},
'''

def patch(path, anchor, block, marker):
    full = os.path.join(ROOT, path)
    s = open(full, encoding="utf-8").read()
    if marker in s:
        print("  already present, skipping:", path); return
    if anchor not in s:
        raise SystemExit("ANCHOR NOT FOUND in %s" % path)
    open(full, "w", encoding="utf-8").write(s.replace(anchor, anchor + block, 1))
    print("  inserted into", path)

patch("build/build_lorefeed.py", "DISPATCHES = [", DISPATCH_BLOCK, "WEEK OF SEPTEMBER 7 - SEPTEMBER 13, 2026")
patch("build/build_gallery.py", "WEEKS = [\n", GALLERY_BLOCK, '"week":"2026-09-07"')
print("done")
