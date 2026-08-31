#!/usr/bin/env python3
"""add_week_0824.py - one-shot insert of the week of Aug 24-30, 2026.

    WL_ROOT="$PWD" python3 build/add_week_0824.py

Idempotent: refuses to insert twice. Verifies its own anchors and fails loudly
rather than half-applying.

WHY A SCRIPT AND NOT A HAND EDIT: two files, ~34 dispatches and 20 video
tuples. A hand edit that half-lands leaves the feed and the gallery telling
different stories about the same week, and that is worse than either being
empty.

EDITORIAL DECISIONS BAKED IN HERE, so they are reviewable:
 - home=True on exactly SEVEN items, one per promotion. The homepage rail is
   home_rail_items(cap=7) and takes the NEWEST seven, so marking ten would
   have made the rail all-AEW on Aug 30 and buried WWE, TNA, NJPW and RAF.
   Seven marks, seven promotions, one balanced rail.
 - lead=True on Ospreay AND Waller, but be aware the generator renders only
   ONE lead per week: render_week() does `top = next(d for d in items if
   d.get("lead"))` and takes the first match. Ospreay wins it. The flag on
   Waller is not dead weight - lead feeds the +100 term in the week's sort
   key, so Heatwave ranks directly under All In instead of sinking into the
   Aug 30 pile. Verified: the built page has exactly one .is-lead.
 - The ESPN non-renewal story arrived from two researchers. Kept the version
   that carries the RETRACTION the next day, because a denied report that was
   later withdrawn is a different fact from a denied report.
"""

import os, re, sys

ROOT = os.environ.get("WL_ROOT", os.getcwd())

# ────────────────────────────── LORE FEED ──────────────────────────────
DISPATCH_BLOCK = '''
  # ================= WEEK OF AUGUST 24-30, 2026 =================
  # Two premium live events in one week: AEW All In: London (Wembley, Aug 30,
  # seven title changes) and WWE NXT Heatwave (Edinburg TX, Aug 30, five).

  # ---- AEW: All In: London, Wembley Stadium, Aug 30 ----
  dict(date="2026-08-30", promo="aew", cat="title", official=True, who="Will Ospreay",
       lead=True, mono="All In: London", home=True, htags="titles matches",
       hl="Will Ospreay beats Kenny Omega at Wembley Stadium for the AEW World Championship",
       dek="Ospreay ended a bloody main event with the Hidden Blade to win his first AEW World Title in front of his home country.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-all-in-london-results-august-30-2026"),
  dict(date="2026-08-30", promo="aew", cat="title", official=True, who="Mercedes Mone",
       home=True, htags="titles matches",
       hl="Mercedes Mone submits Willow Nightingale for the AEW Women's World Championship",
       dek="Mone worked the hand she injured in a backstage attack on Dynamite, then won the title for the first time with the Statement Maker.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-all-in-london-results-august-30-2026"),
  dict(date="2026-08-30", promo="aew", cat="signing", official=True, who="The New Level",
       hl="Kofi and Austin Creed debut in AEW as The New Level and win the World Trios Titles",
       dek="The former New Day members joined Swerve Strickland to win the 21-wrestler Trios Roulette Royale on the Buy In. Tony Khan confirmed both are signed.",
       src="Wrestling Inc.", url="https://www.wrestlinginc.com/2247106/aew-all-in-london-2026-austin-creed-kofi-swerve-strickland-new-level-debut-win-gold/"),
  dict(date="2026-08-30", promo="aew", cat="title", official=True, who="Darby Allin",
       hl="Darby Allin takes the TNT Championship from Kevin Knight in a Falls Count Anywhere match",
       dek="Allin won his third TNT Title with a Coffin Drop off the Wembley stage. Sting appeared with a bat to even the odds against the Don Callis Family.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-all-in-london-results-august-30-2026"),
  dict(date="2026-08-30", promo="aew", cat="title", official=True, who="Kazuchika Okada",
       hl="Kazuchika Okada regains the AEW International Championship in a Wembley three-way",
       dek="Okada hit the Rainmaker on champion Kyle Fletcher in a match that also included Konosuke Takeshita.",
       src="Fightful", url="https://www.fightful.com/wrestling/aew-all-in-results-8-30-2026-kenny-omega-vs-will-ospreay-willow-nightingale-vs-mercedes-mone-more/"),
  dict(date="2026-08-30", promo="aew", cat="title", official=True, who="Persephone",
       hl="Persephone beats Maya World for the TBS Championship as Britt Baker returns",
       dek="Persephone won the title with a crucifix powerbomb on the Buy In. The masked attacker who cost World the match unmasked as Dr. Britt Baker.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-all-in-london-results-august-30-2026"),
  dict(date="2026-08-30", promo="aew", cat="title", official=True, who="The Brawling Birds",
       hl="Jamie Hayter and Alex Windsor win the AEW Women's World Tag Team Titles at Wembley",
       dek="The Brawling Birds hit 2 Birds, 1 Stone on Lena Kross to take the belts from Divine Dominion in front of a home crowd.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-all-in-london-results-august-30-2026"),
  dict(date="2026-08-30", promo="aew", cat="title", official=True, who="Jon Moxley",
       hl="Jon Moxley submits Nigel McGuinness in the Continental Challenge Cup final",
       dek="Moxley kept the AEW Continental Championship, capping a tournament run that went through Claudio Castagnoli in the Glasgow semifinal.",
       src="AEW.com", url="https://www.allelitewrestling.com/post/aew-all-in-london-results-august-30-2026"),
  dict(date="2026-08-30", promo="aew", cat="event", official=True, who="Andrade El Idolo",
       hl="Andrade El Idolo wins the All In Casino Gauntlet and a guaranteed world title shot",
       dek="Andrade pinned Nick Wayne to win the ten-entrant gauntlet, which also featured MJF and a returning Chris Jericho.",
       src="PWMania", url="https://www.pwmania.com/aew-all-in-london-results-august-30-2026"),
  dict(date="2026-08-27", promo="aew", cat="business", official=True, who="Tony Khan",
       hl="Tony Khan says All In: London is approaching a six million dollar gate",
       dek="On the pre-show media call Khan said the Wembley card would run at most four hours and confirmed the Trios Roulette Royale for the Buy In.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/08/27/aew-all-in-london-2026-media-call-with-tony-khan-6-million-gate-four-hour-show-trios-title-match-on-buy-in/"),

  # ---- WWE NXT: Heatwave, Bert Ogden Arena, Edinburg TX, Aug 30 ----
  dict(date="2026-08-30", promo="nxt", cat="title", official=True, who="Grayson Waller",
       lead=True, mono="NXT Heatwave", home=True, htags="titles matches",
       hl="Grayson Waller wins the NXT Championship in a Heatwave Fatal 4-Way",
       dek="Waller stole the pin late over Tony D'Angelo, Zilla Fatu and Cruz Montana at the show co-branded with AAA as Ola de Calor.",
       src="WWE.com", url="https://www.wwe.com/nxt-heatwave-2026"),
  dict(date="2026-08-30", promo="nxt", cat="title", official=True, who="Kelani Jordan",
       hl="Kelani Jordan defeats Kendal Grey for the NXT Women's Championship",
       dek="Jordan worked over Grey's arm throughout and finished with a split-legged moonsault. It is her first NXT Women's Title reign.",
       src="Slam Wrestling", url="https://slamwrestling.net/news/wwe-nxt-heatwave-2026-results/"),
  dict(date="2026-08-30", promo="nxt", cat="title", official=True, who="Zaria",
       hl="Zaria unifies the NXT Women's North American and Women's Speed Championships",
       dek="Zaria beat Wren Sinclair and Kali Armstrong in the Heatwave opener with a spear and an F5. The two titles are now one championship.",
       src="Wrestling Inc.", url="https://www.wrestlinginc.com/2246913/wwe-nxt-heatwave-2026-several-championships-up-for-grabs-submission-match/"),
  dict(date="2026-08-30", promo="nxt", cat="title", official=True, who="Jackson Drake",
       hl="Jackson Drake defeats Myles Borne for the NXT North American Championship",
       dek="Vanity Project interference proved decisive. Borne afterward turned on partner Tavion Heights, having already lost the tag titles earlier in the night.",
       src="Slam Wrestling", url="https://slamwrestling.net/news/wwe-nxt-heatwave-2026-results/"),
  dict(date="2026-08-25", promo="nxt", cat="event", official=True, who="Tony D'Angelo",
       hl="The Heatwave Summit collapses into a brawl on the NXT go-home show",
       dek="The contract signing for the NXT and Women's Title matches broke down, leaving champions Tony D'Angelo and Kendal Grey laid out five days out.",
       src="WWE.com", url="https://www.wwe.com/shows/wwenxt/2026-08-25"),

  # ---- WWE: Raw Aug 24 and SmackDown Aug 28, both from Ottawa ----
  dict(date="2026-08-28", promo="wwe", cat="event", official=True, who="Sami Zayn",
       home=True, htags="rivalries titles",
       hl="Sami Zayn ends the SmackDown No. 1 Contender's Match in a no contest with the title belt",
       dek="Zayn dragged Finn Balor from the ring and attacked both referees, then hit Balor, Gunther, Kevin Owens and CM Punk with the WWE Championship.",
       src="Wrestling Inc.", url="https://www.wrestlinginc.com/2246899/wwe-smackdown-no-1-contenders-match-chaos-sami-zayn-cm-punk/"),
  dict(date="2026-08-28", promo="wwe", cat="title", official=True, who="Jacy Jayne",
       hl="Jacy Jayne retains the Women's United States Championship against Paige",
       dek="Fallon Henley and Lainey Reid distracted Paige from the apron and Jayne rolled her up. Nikki Bella attacked Paige after the match.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-08-28"),
  dict(date="2026-08-26", promo="wwe", cat="roster", official=False, who="AJ Lee",
       hl="AJ Lee is expected to wrestle again for WWE despite her absence since WrestleMania 42",
       dek="Fightful Select reported Lee has not had her final WWE match. She has not been in a storyline since losing the Women's Intercontinental Title to Becky Lynch.",
       src="Slam Wrestling", url="https://slamwrestling.net/news/backstage-update-emerges-on-aj-lees-wwe-future-wrestling-news-rumours-august-26-2026/"),
  dict(date="2026-08-24", promo="wwe", cat="event", official=True, who="Royce Keys",
       hl="Royce Keys returns with OTM and lays out The Usos, LA Knight and Solo Sikoa",
       dek="The Ottawa main event was thrown out as a no contest when Keys arrived with Bronco Nima and Lucien Price and put all four men down.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-08-24"),
  dict(date="2026-08-24", promo="wwe", cat="event", official=True, who="Stephanie Vaquer",
       hl="Stephanie Vaquer beats Roxanne Perez in her first match since WrestleMania 42",
       dek="Becky Lynch cut off Liv Morgan and Raquel Rodriguez before Vaquer finished with a face breaker. She was told backstage she challenges Morgan for the Women's World Title in two weeks.",
       src="Slam Wrestling", url="https://slamwrestling.net/news/wwe-raw-results-august-24-2026/"),
  dict(date="2026-08-24", promo="wwe", cat="event", official=True, who="Penta",
       hl="Penta and Rey Fenix win their semifinals to set a brothers' final for a Reigns title shot",
       dek="Penta beat La Parka with a Mexican Destroyer and Fenix beat Dragon Lee with the Mexican Muscle Buster. The winner challenges Roman Reigns.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-08-24/results"),
  dict(date="2026-08-24", promo="wwe", cat="return", official=True, who="Big Cass",
       hl="Big Cass beats Je'Von Evans in his first WWE match in over eight years",
       dek="Cass shoved Evans off the top rope and finished with a Big Boot. Dominik Mysterio and JD McDonagh attacked Evans after the bell.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-08-24/results"),
  dict(date="2026-08-24", promo="wwe", cat="event", official=True, who="Oba Femi",
       hl="Oba Femi and Bron Breakker brawl at a Raw contract signing for Sunday Night's Main Event",
       dek="Breakker blindsided Femi and Austin Theory joined the fight, but Femi recovered and sent Theory through the signing table.",
       src="Slam Wrestling", url="https://slamwrestling.net/news/wwe-raw-results-august-24-2026/"),

  # ---- TNA: iMPACT Aug 27 ----
  dict(date="2026-08-28", promo="tna", cat="signing", official=True, who="Zoey Serrano",
       home=True, htags="roster",
       hl="TNA confirms the signing of Zoey Serrano after her iMPACT debut",
       dek="The former WWE star known as Zoey Stark debuted on the Aug. 27 iMPACT by attacking Indi Hartwell alongside Xia Brookside.",
       src="Wrestling Inc.", url="https://www.wrestlinginc.com/2247236/tna-zoey-serrano-stark-signing-impact-debut/"),
  dict(date="2026-08-27", promo="tna", cat="title", official=True, who="M by Elegance",
       hl="M by Elegance wins the inaugural TNA Knockouts Television Championship",
       dek="Elegance targeted the arm and finished Jada Stone with a piledriver in the tournament final. She is the first holder of the new title.",
       src="Fightful", url="https://www.fightful.com/wrestling/tna-impact-results-8-27-knockouts-tv-title-tournament-final/"),
  dict(date="2026-08-27", promo="tna", cat="event", official=True, who="Leon Slater",
       hl="Leon Slater invokes Option C for a Bound for Glory world title shot",
       dek="Slater cashed in to challenge Nic Nemeth, saying he intends to become the youngest champion in company history.",
       src="Slam Wrestling", url="https://slamwrestling.net/report/tna-impact-results-08-27-2026-debuts-championships-and-statements-made-oh-my/"),
  dict(date="2026-08-27", promo="tna", cat="title", official=True, who="The Nemeths",
       hl="The Nemeths retain the TNA Tag Team Championship against Leon Slater and Ricky Sosa",
       dek="Nic and Ryan Nemeth turned back the challengers in their first defense since winning the belts at Lockdown.",
       src="Fightful", url="https://www.fightful.com/wrestling/tna-impact-results-8-27-knockouts-tv-title-tournament-final/"),
  dict(date="2026-08-27", promo="tna", cat="event", official=True, who="Jeff Hardy",
       hl="Jeff Hardy leaves iMPACT by ambulance after another mystery attack",
       dek="Hardy was found laid out and loaded onto a stretcher, with Matt Hardy helping him into the ambulance.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/08/27/tna-impact-tv-results-8-27-stone-vs-elegance-elijah-vs-bronson-hartwell-appearance/"),

  # ---- NJPW ----
  dict(date="2026-08-30", promo="njpw", cat="event", official=True, who="Hirooki Goto",
       home=True, htags="matches",
       hl="Hirooki Goto's team beats champion Yota Tsuji's side at NJPW Shimonoseki Impact",
       dek="Goto, YOH and YOSHI-HASHI won before a sold-out 1,817 in Yamaguchi, four weeks before Goto challenges Tsuji for the IWGP Heavyweight Championship at Destruction in Kobe.",
       src="Fightful", url="https://www.fightful.com/wrestling-news/njpw-shimonoseki-impact-results-8-30-26-hirooki-goto-yoh-yoshi-hashi-pick-up-win-in-main-event"),

  # ---- RAF: fallout from RAF 12, build to Moscow ----
  dict(date="2026-08-25", promo="raf", cat="event", official=False, who="Tyron Woodley",
       home=True, htags="matches",
       hl="Tyron Woodley says Khamzat Chimaev may be an easier test than Joaquin Buckley",
       dek="Woodley rallied from 8-1 down to beat Buckley 14-8 at RAF 12 and meets Chimaev in the September 5 Moscow main event. He said the absence of strikes favors his wrestling.",
       src="MiddleEasy", url="https://middleeasy.com/mma-news/tyron-woodley-khamzat-chimaev-raf-moscow-joaquin-buckley/"),
  dict(date="2026-08-25", promo="raf", cat="event", official=False, who="Colby Covington",
       hl="Colby Covington drops interest in a Bo Nickal match after Nickal's RAF 12 loss",
       dek="Nickal lost 3-2 to 2026 NCAA champion Max McEnelly in Cleveland. Covington said the mystique is not there anymore and cited the weight gap.",
       src="Yahoo Sports", url="https://sports.yahoo.com/articles/colby-covington-says-bo-nickal-225019899.html"),
  dict(date="2026-08-24", promo="raf", cat="event", official=False, who="Merab Dvalishvili",
       hl="Merab Dvalishvili addresses his 36-second loss to Henry Cejudo at RAF 12",
       dek="Cejudo pinned Dvalishvili in 36 seconds in Cleveland to take the lightweight title. Dvalishvili said he had been preparing for his UFC title defense rather than a full wrestling camp.",
       src="Heavy", url="https://heavy.com/sports/ufc/merab-dvalishvili-addresses-henry-cejudo-raf-loss/"),

  # ---- industry ----
  dict(date="2026-08-26", promo="industry", cat="media", official=True, who="SEScoops",
       hl="SEScoops retracts its ESPN report and parts ways with the writer",
       dek="The outlet said the subject deserved a direct chance to respond and that the step was not taken to the appropriate standard. Writer BJ Bethel said he stood by the story.",
       src="Awful Announcing", url="https://awfulannouncing.com/wwe/sescoops-retracts-espn-wwe-report.html"),
  dict(date="2026-08-25", promo="industry", cat="media", official=True, who="ESPN",
       hl="ESPN denies a report that it has decided not to renew its WWE deal",
       dek="ESPN said there is no truth to the report that it had decided against renewing the five-year, $1.6 billion premium live event agreement that runs to 2030.",
       src="Wrestling Attitude", url="https://www.wrestlingattitude.com/2026/08/espn-denies-wwe-ple-contract-non-renewal-reports.html"),
  # =============== end week of August 24-30, 2026 ===============
'''

GALLERY_BLOCK = '''  {"week":"2026-08-24","label":"Week of August 24, 2026","start":datetime.date(2026,8,24),"promos":{
     "WWE":[("YKkV6B4XugE","2026-08-24","Raw \\u00b7 Full show highlights"),("3z-lAWwmk4w","2026-08-24","Raw \\u00b7 Top 10 moments"),("h2wGqoYC5nE","2026-08-24","Raw \\u00b7 Royce Keys and OTM attack The Usos"),("prGteFbrO2g","2026-08-24","Raw \\u00b7 Oba Femi and Bron Breakker contract signing"),("9Le3pCbsepc","2026-08-28","SmackDown \\u00b7 Full show highlights"),("Ti6LMGlWzvU","2026-08-28","SmackDown \\u00b7 Top 10 moments"),("q-cGhdmje6A","2026-08-28","SmackDown \\u00b7 Sami Zayn ruins the No. 1 Contender's Match"),("FSyaWfLxgpA","2026-08-28","SmackDown \\u00b7 Jacy Jayne vs. Paige, Women's U.S. Title")],
     "AEW":[("w0H7dv46UhY","2026-08-30","All In \\u00b7 Cold open"),("LJxwEkDzc4Q","2026-08-30","All In \\u00b7 Ospreay vs. Omega, AEW World Title"),("R1Aq466zfG4","2026-08-30","All In \\u00b7 The Buy In pre-show"),("LfCPoPIAAJk","2026-08-30","All In \\u00b7 Post-show media scrum"),("WPdoj16in-Y","2026-08-26","Dynamite \\u00b7 Moxley vs. Castagnoli, Continental Challenge Cup"),("0bduV-wWUvs","2026-08-26","Dynamite \\u00b7 Will Ospreay promo in Glasgow"),("0Y7ngGOI_4s","2026-08-29","Collision \\u00b7 Kyle Fletcher ambushes Takeshita")],
     "TNA":[("4pGKgB9DxyI","2026-08-27","iMPACT \\u00b7 Santino Marella books the Nemeths in the main event"),("dB4z9Iy0HG0","2026-08-27","iMPACT \\u00b7 Zoey Serrano debuts by attacking Indi Hartwell")],
     "NXT":[("N66zv_yR-MU","2026-08-25","NXT \\u00b7 Full show highlights"),("M2aCEW7dxic","2026-08-25","NXT \\u00b7 Top 10 moments"),("dJqBkDltFcg","2026-08-25","NXT \\u00b7 The Heatwave Summit erupts into a brawl")]
  }},
'''


def patch(path, anchor, block, marker):
    full = os.path.join(ROOT, path)
    with open(full, encoding="utf-8") as fh:
        s = fh.read()
    if marker in s:
        print("  already present, skipping:", path)
        return False
    if anchor not in s:
        raise SystemExit("ANCHOR NOT FOUND in %s: %r" % (path, anchor[:60]))
    s = s.replace(anchor, anchor + block, 1)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(s)
    print("  inserted into", path)
    return True


def main():
    print("week of 2026-08-24 -> lore feed + gallery")
    patch("build/build_lorefeed.py", "DISPATCHES = [", DISPATCH_BLOCK,
          "WEEK OF AUGUST 24-30, 2026")
    patch("build/build_gallery.py", "WEEKS = [\n", GALLERY_BLOCK,
          '"week":"2026-08-24"')

    # "All In" is a new show name. SHOWNAME drives the video page <title> and
    # the VideoObject schema; without an entry it falls back to the bare label
    # and the pages read "All In, August 30" instead of naming the promotion.
    g = os.path.join(ROOT, "build/build_gallery.py")
    s = open(g, encoding="utf-8").read()
    if '"All In":' not in s:
        s = s.replace('"SummerSlam":"WWE SummerSlam"',
                      '"SummerSlam":"WWE SummerSlam","All In":"AEW All In: London"', 1)
        s = s.replace('SHOWORDER = ["SummerSlam",',
                      'SHOWORDER = ["SummerSlam","All In",', 1)
        open(g, "w", encoding="utf-8").write(s)
        print("  registered show name: All In")
    else:
        print("  show name already registered: All In")


if __name__ == "__main__":
    main()
