#!/usr/bin/env python3
"""add_week_0914.py - open the week of Sep 14 - Sep 20, 2026 (through Sep 20).

    WL_ROOT="$PWD" python3 build/add_week_0914.py

Idempotent. Run LAST of the three backfill scripts - gallery weeks PREPEND,
so this leaves 2026-09-14 as WEEKS[0] and the homepage This-Week block
regenerates from it. Sep 20 is assembly day: only what already happened is
filed, and no Raw 9/14 or NXT 9/15 ratings exist yet (Nielsen's September
methodology change delayed reporting) - none are invented.

ASSEMBLY DECISIONS (three research agents, one lane each, Sep 20 assembly):
 - Lead: Roman Reigns RETAINED over Penta on the Sep 14 Raw in Mexico City
   (spear, 22:25) - confirmed by TWO written sources, PWTorch and Pro
   Wrestling Dot Net. The YouTube video FkxdfCo5QyQ titled as Penta WINNING
   the title resolved via oEmbed to fan channel "NagraPidi" and its title
   claim is FALSE; it is rejected everywhere, and the two Raw tuples below
   are from the official WWE channel instead.
 - RAF 13 is dated 2026-09-18: Fightful, Wikipedia and Yahoo place it
   Friday Sep 18 at the Watsco Center in Miami; MiddleEasy's Sep 19 is
   publish-date drift and the gap brief's Sep 19 followed it. The
   Harutyunyan-over-DeSanto bantamweight title change is real and filed
   inside the dek.
 - home=True budget (3-5): kept FIVE - Reigns (9/14), Moxley Dynamite and
   the Mone medical pull (9/16), Covington RAF 13 (9/18), Zayn's first
   defense (9/18). The Mason Rook NXT contender row arrived flagged
   home=True and was DEMOTED to stay inside the cap.
 - Two agent rows carried htags as Python lists; converted to the
   space-separated strings the rail expects. htags dropped from the
   demoted row - htags ride with home=True.
 - The Dragunov-to-AEW row is a REPORT (Fightful Select via PWTorch) and
   ships official=False; the dek says the deal was not finalized.
 - Worlds Collide: Sep 26 at Allstate Arena (per the venue itself) - the
   Sep 12 date the gap brief warned about belongs to the 2025 show and
   appears nowhere here.
 - NJPW ran no cards in window; the one NJPW row is the Sep 20 full-card
   confirmation for Destruction in Kobe, published today, filed as what
   it is: an announcement, not a result.
 - All 9 video IDs oEmbed-verified: WWE (5), All Elite Wrestling (3),
   TNA Wrestling (1), Real American Freestyle Wrestling (1) - the first
   official-channel RAF video the gallery has carried.
"""
import os

ROOT = os.environ.get("WL_ROOT", os.getcwd())

DISPATCH_BLOCK = '''
  # ================= WEEK OF SEPTEMBER 14 - SEPTEMBER 20, 2026 (in progress) =================
  # Backfilled Sep 20, current through today. Reigns turns back Penta in Mexico
  # City; Zayn's first defense; RAF 13 in Miami. See build/add_week_0914.py.

  # ---- WWE: Raw Sep 14 (Arena CDMX) + SmackDown Sep 18 (Corpus Christi) ----
  dict(date="2026-09-14", promo="wwe", cat="title", official=True, who="Roman Reigns", lead=True, mono="World Title", home=True, htags="matches titles",
       hl="Roman Reigns spears Penta to retain World Heavyweight Title in Mexico City",
       dek="Reigns survives multiple Mexican Destroyers and pins Penta with a Superman Punch and spear at 22:25 before a devastated Arena CDMX crowd.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/09/14/wwe-raw-results-9-14-kellers-report-on-roman-reigns-vs-penta-for-the-world-title-gable-vs-lee-for-ic-title-mitb-qualifying-matches-more/"),
  dict(date="2026-09-18", promo="wwe", cat="title", official=True, who="Sami Zayn", home=True, htags="titles rivalries",
       hl="Sami Zayn retains WWE Title over Kevin Owens as CM Punk interferes on SmackDown",
       dek="In his first SmackDown as Undisputed WWE Champion, Zayn beats Owens after Punk strikes Owens with the title belt; Punk lays out both men to close the show.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/09/18/wwe-smackdown-results-9-18-kellers-report-on-sami-zayn-celebrating-his-wwe-title-win-mitb-qualifiers-cody-rhodes-addresses-orton/"),
  dict(date="2026-09-14", promo="wwe", cat="title", official=True, who="Chad Gable",
       hl="Chad Gable taps out Dragon Lee to keep Intercontinental Championship on Raw",
       dek="Gable counters a Styles Clash into a grapevined ankle lock and forces Lee to submit at 15:40, then raises his hand in a show of respect.",
       src="Wrestling Inc", url="https://www.wrestlinginc.com/2258569/wwe-raw-chad-gable-dragon-lee-mens-intercontinental-title-retains/"),
  dict(date="2026-09-14", promo="wwe", cat="event", official=True, who="Je'Von Evans",
       hl="Je'Von Evans and Lola Vice win Money in the Bank qualifiers on Raw",
       dek="Evans beats Austin Theory and Big Cass in a triple threat while Vice defeats Raquel Rodriguez and Kelani Jordan to reach the October 10 ladder matches in New Orleans.",
       src="Pro Wrestling Dot Net", url="https://prowrestling.net/site/2026/09/14/wwe-raw-results-9-14-powells-live-review-of-roman-reigns-vs-penta-for-the-world-heavyweight-championship-chad-gable-vs-dragon-lee-for-the-intercontinental-title-mitb-qualifiers/"),
  dict(date="2026-09-18", promo="wwe", cat="media", official=True, who="Cody Rhodes",
       hl="Cody Rhodes tells Michael Cole he will not repeat his mercy toward Randy Orton",
       dek="In a sit-down interview on SmackDown, Rhodes says he refuses to compromise himself to win but vows he will not make the same decision he made at Sunday Night's Main Event.",
       src="Pro Wrestling Dot Net", url="https://prowrestling.net/site/2026/09/18/wwe-smackdown-results-9-18-barnetts-live-review-of-new-wwe-champion-sami-zayns-appearance-michael-coles-interview-with-cody-rhodes-money-in-the-bank-qualifiers/"),
  dict(date="2026-09-18", promo="wwe", cat="event", official=True, who="Trick Williams",
       hl="Trick Williams and Jacy Jayne claim Money in the Bank spots on SmackDown",
       dek="Williams wins a triple threat over Randy Orton and Rey Fenix while Jayne pins Alexa Bliss in a three-way also involving Jade Cargill.",
       src="Fightful", url="https://www.fightful.com/wrestling/wwe-smackdown-results-9-18-2026-sami-zayn-appears-mitb-qualifiers-more/"),

  # ---- AEW: Dynamite Sep 16 (Norfolk) + Collision Sep 19 (Charleston) ----
  dict(date="2026-09-16", promo="aew", cat="event", official=True, who="Jon Moxley", home=True, htags="matches rivalries",
       hl="Death Riders lay out United Empire as Moxley trio wins Dynamite main event",
       dek="Jon Moxley, PAC and Gabe Kidd beat Will Ospreay, Andrade El Idolo and Francesco Akira in Norfolk, and the Death Riders and The Dogs beat down United Empire to close the show. Ospreay defends the AEW World Championship against Moxley at All Out in Chicago on September 26.",
       src="Fightful", url="https://www.fightful.com/wrestling-news/aew-dynamite-results-9-16-2026-united-empire-vs-death-riders-jamie-hayter-vs-lena-kross-more"),
  dict(date="2026-09-16", promo="aew", cat="roster", official=True, who="Mercedes Mone", home=True, htags="titles roster",
       hl="Mercedes Mone not medically cleared for All Out due to broken nose",
       dek="AEW announced the Women's World Champion, whose nose was broken by Willow Nightingale at All In, will miss All Out in Chicago. Nightingale faces Thekla at All Out with the winner challenging Mone at WrestleDream in Orlando this October.",
       src="SEScoops", url="https://www.sescoops.com/article/top-aew-champion-mercedes-mone-not-cleared-to-compete-at-all-out-2026"),
  dict(date="2026-09-14", promo="aew", cat="signing", official=False, who="Ilja Dragunov",
       hl="Ilja Dragunov reportedly set to sign with AEW after WWE exit",
       dek="Fightful Select reports the former WWE United States Champion is expected to sign with AEW barring unforeseen circumstances, after his WWE contract expired with no 90-day non-compete. The deal was not yet finalized as of the report.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/09/14/major-name-reportedly-expected-to-sign-with-aew/"),
  dict(date="2026-09-15", promo="aew", cat="media", official=True, who="All Elite Wrestling",
       hl="AEW announces Hulu Japan streaming deal for Dynamite, Collision and pay-per-views",
       dek="AEW and Hulu Japan jointly announced that Dynamite, Collision and live pay-per-view events will stream exclusively in Japan on Hulu Japan starting November 2026. New episodes will no longer be added to NJPW World.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/09/15/xaew-announces-that-dynamite-collision-and-ppvs-will-air-in-japan-on-hulu-japan/"),
  dict(date="2026-09-19", promo="aew", cat="title", official=True, who="Andrade El Idolo",
       hl="Andrade retains National Title on Collision and PAC issues All Out challenge",
       dek="Andrade El Idolo beat Daniel Garcia in Charleston to retain the AEW National Championship, after which PAC attacked him and challenged for the title at All Out. Darby Allin also retained the TNT Championship against Myron Reed.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/09/19/aew-collision-results-9-19-moxley-vs-zachary-wentz-darby-vs-myron-reed-for-the-tnt-title-thekla-vs-zayda-steel-andrade-vs-garcia-for-the-national-title/"),

  # ---- RAF 13 Sep 18 / NXT Sep 15 / TNA Sep 17 / NJPW / industry ----
  dict(date="2026-09-18", promo="raf", cat="event", official=True, who="Colby Covington", home=True, htags="matches",
       hl="Covington blanks Belal Muhammad 10-0 to retain RAF crossover crown at RAF 13",
       dek="Covington kept the Cruiserweight Crossover title with a 10-0 tech fall shutout in Miami. Khamzat Chimaev beat Gilbert Burns 15-4 and Joe Pyfer routed Luke Rockhold 14-3, while Arsen Harutyunyan took the bantamweight belt from Austin DeSanto 6-3.",
       src="Fightful", url="https://www.fightful.com/mma/raf-13-results-9-18-colby-covington-beats-belal-muhammad-khamzat-chimaev-wins/"),
  dict(date="2026-09-15", promo="nxt", cat="event", official=True, who="Mason Rook",
       hl="Mason Rook wins triple threat to earn NXT Title shot at Grayson Waller",
       dek="Rook beat Tony D'Angelo and Saquon Shugars to become number one contender. AAA champ La Catalina brawled with Kelani Jordan, and Robert Stone announced the return of the Dusty Tag Team Classic.",
       src="WWE.com", url="https://www.wwe.com/shows/wwenxt/2026-09-15"),
  dict(date="2026-09-17", promo="tna", cat="event", official=True, who="Moose",
       hl="Moose saves TNA career against Kazarian as Bound for Glory card takes shape",
       dek="Moose beat Frankie Kazarian in 16:54 with consecutive spears to keep his TNA job, then smashed a crown with a chair. Rich Swann pinned LJ Cleary to reach the X-Division title match at Bound for Glory, and Eddie Edwards challenged Ricky Sosa for the show.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/09/17/tna-impact-9-17-results-moose-saves-tna-career-rich-swann-advances-to-bound-for-glory/"),
  dict(date="2026-09-20", promo="njpw", cat="event", official=True, who="Yota Tsuji",
       hl="NJPW locks in full Destruction in Kobe card topped by Tsuji versus Goto",
       dek="Yota Tsuji defends the IWGP Heavyweight title against Hirooki Goto on September 27, with Gabe Kidd against Drilla Moloney for the Global belt and Konosuke Takeshita against Shun Skywalker for the TV title. G1 winner Ryohei Oiwa challenges the Kobe winner at King of Pro Wrestling on October 12.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/09/20/njpw-confirms-full-card-for-destruction-in-kobe/"),
  dict(date="2026-09-16", promo="industry", cat="business", official=False, who="CM Punk",
       hl="Allstate Arena advertises four matches for WWE and AAA Worlds Collide",
       dek="The Rosemont venue is promoting CM Punk, Rey Mysterio and El Grande Americano against Dominik Mysterio, JD McDonagh and Omos for September 26, plus Penta and Rey Fenix against Los Perros del Mal. Over 10,900 tickets are out for a show running opposite AEW All Out.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/09/16/allstate-arena-advertising-four-matches-for-wwe-worlds-collide/"),
  dict(date="2026-09-17", promo="industry", cat="roster", official=False, who="Flip Gordon",
       hl="Flip Gordon reenlists in Army National Guard while vowing ring return",
       dek="After 11 years as a pro, Gordon reenlisted in the Army National Guard and said his wrestling career continues, including a return to CMLL. The same update noted Chris Bey underwent his first stem cell therapy session in his neck injury recovery.",
       src="F4W/WON", url="https://www.f4wonline.com/news/daily-updates/daily-update-wwe-notes-flip-gordon-chris-bey/"),
  # =============== end week of September 14 - September 20, 2026 ===============
'''

GALLERY_BLOCK = '''  {"week":"2026-09-14","label":"Week of September 14, 2026","start":datetime.date(2026,9,14),"promos":{
     "WWE":[("t7m12y_xvr0","2026-09-14","Raw \\u00b7 Roman Reigns vs. Penta World Heavyweight Title match highlights from Mexico City"),("bXaM4W2nquo","2026-09-14","Raw \\u00b7 Penta reacts to his match against Roman Reigns in a WWE digital exclusive"),("qLCQyYed-dI","2026-09-18","SmackDown \\u00b7 Kevin Owens steps up to challenge new champion Sami Zayn for the WWE Title"),("efd8w7YrrR4","2026-09-18","SmackDown \\u00b7 CM Punk blasts Kevin Owens with the title as Sami Zayn retains the WWE Championship")],
     "AEW":[("3nVvKLNsxyU","2026-09-16","Dynamite \\u00b7 Will Ospreay fights off the Death Riders and The Dogs"),("kutouK73ozY","2026-09-19","Collision \\u00b7 PAC challenges Andrade El Idolo to a National Title match at All Out"),("AfAchQFBqlU","2026-09-19","Collision \\u00b7 Jon Moxley vs Zachary Wentz match highlights")],
     "NXT":[("TfC5onUse0w","2026-09-15","NXT \\u00b7 Tony D'Angelo vs. Saquon Shugars vs. Mason Rook triple threat highlights")],
     "TNA":[("PUXKEyMbXpQ","2026-09-17","iMPACT \\u00b7 Moose puts his TNA career on the line against Frankie Kazarian")],
     "RAF":[("IR3ZKkuwcoo","2026-09-18","RAF \\u00b7 Khamzat Chimaev vs. Gilbert Burns full highlights from RAF 13")]
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

patch("build/build_lorefeed.py", "DISPATCHES = [", DISPATCH_BLOCK, "WEEK OF SEPTEMBER 14 - SEPTEMBER 20, 2026")
patch("build/build_gallery.py", "WEEKS = [\n", GALLERY_BLOCK, '"week":"2026-09-14"')
print("done")
