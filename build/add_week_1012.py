#!/usr/bin/env python3
"""add_week_1012.py - open the week of Oct 12 - Oct 18, 2026 (AEW WrestleDream).

    WL_ROOT="$PWD" python3 build/add_week_1012.py

Idempotent. Inserts one block after `DISPATCHES = [` in build_lorefeed.py.

ASSEMBLY DECISIONS (researched Nov 7, 2026):
 - LEAD: Will Ospreay retains the AEW World Title in the first-ever Clockwork
   Carnage match at WrestleDream (Oct 17, Addition Financial Arena, Orlando).
   Verified: Fightful full card + WrestlingInc.
 - WrestleDream: Hangman Page, Bandido & Brody King beat Swerve & New Level for
   the World Trios Titles (2/3 falls) - TITLE CHANGE; Mercedes Mone ret. the
   Women's World Title over Thekla; Young Bucks ret. tag titles; Andrade ret.
   National; Persephone ret. TBS; Moxley ret. Continental; Ilja Dragunov made
   his AEW debut (ALL ELITE), continuing from his August WWE exit.
 - Raw Oct 12 (Bossier City): Carmelo Hayes joined 946 and the group attacked
   The Bloodline; Chad Gable ret. the Intercontinental Title over Rey Fenix.
 - Dynamite Oct 14 (Cleveland): Clockwork Carnage qualifiers set; Adam Copeland
   announced he will retire in 2027.
 - SmackDown Oct 16 (Sacramento): Cody Rhodes beat Baron Corbin by DQ when Randy
   Orton interfered; Orton then drove Cody into the steel steps.
 - iMPACT Oct 15 (San Antonio): Trey Miguel won a five-way ladder match to earn
   a TNA World Title shot vs new champ Leon Slater at Destination X (Nov 15).
 - home=True budget: FIVE (Ospreay lead, Hangman/Trios, Ilja, Carmelo/946,
   Cody/Orton). No gallery block here.
"""
import os

ROOT = os.environ.get("WL_ROOT", os.getcwd())

DISPATCH_BLOCK = '''
  # ================= WEEK OF OCTOBER 12 - OCTOBER 18, 2026 (WrestleDream) =================
  # Assembled Nov 7. Ospreay wins the first Clockwork Carnage; Hangman's side takes
  # the Trios titles; Ilja Dragunov debuts in AEW; Carmelo Hayes joins 946; the
  # Cody-Orton feud reignites. See build/add_week_1012.py.

  # ---- AEW WrestleDream (Oct 17, Orlando) ----
  dict(date="2026-10-17", promo="aew", cat="title", official=True, who="Will Ospreay", lead=True, mono="WrestleDream", home=True, htags="titles matches",
       hl="Will Ospreay survives the first-ever Clockwork Carnage to keep the AEW World Title",
       dek="In the WrestleDream main event in Orlando, Ospreay retained the AEW World Championship in the inaugural Clockwork Carnage match against Samoa Joe, Adam Copeland, Konosuke Takeshita, Kazuchika Okada, Ricochet, Mike Bailey and Darby Allin.",
       src="Fightful", url="https://www.fightful.com/wrestling/aew-wrestledream-results-10-17-2026-mercedes-mone-vs-thekla-clockwork-carnage-more/"),
  dict(date="2026-10-17", promo="aew", cat="title", official=True, who="Hangman Page", home=True, htags="titles",
       hl="Hangman Page, Bandido and Brody King win the AEW World Trios Titles",
       dek="In a two-out-of-three-falls match at WrestleDream, Hangman Page, Bandido and Brody King dethroned Swerve Strickland and New Level (Kofi Kingston and Austin Creed) for the World Trios Championship.",
       src="Fightful", url="https://www.fightful.com/wrestling/aew-wrestledream-results-10-17-2026-mercedes-mone-vs-thekla-clockwork-carnage-more/"),
  dict(date="2026-10-17", promo="aew", cat="title", official=True, who="Mercedes Mone",
       hl="Mercedes Mone turns back Thekla to retain the AEW Women's World Title",
       dek="Mercedes Mone beat Thekla at WrestleDream to keep the Women's World Championship in the match Thekla earned by winning the All Out number one contender bout.",
       src="Fightful", url="https://www.fightful.com/wrestling/aew-wrestledream-results-10-17-2026-mercedes-mone-vs-thekla-clockwork-carnage-more/"),
  dict(date="2026-10-17", promo="aew", cat="signing", official=True, who="Ilja Dragunov", home=True, htags="roster",
       hl="Ilja Dragunov debuts at WrestleDream and is All Elite",
       dek="Ilja Dragunov made a surprise AEW debut at WrestleDream, months after his WWE exit, and was announced as All Elite.",
       src="Fightful", url="https://www.fightful.com/wrestling/aew-wrestledream-results-10-17-2026-mercedes-mone-vs-thekla-clockwork-carnage-more/"),

  # ---- WWE Raw Oct 12 (Bossier City) ----
  dict(date="2026-10-12", promo="wwe", cat="event", official=True, who="Carmelo Hayes", home=True, htags="rivalries",
       hl="Carmelo Hayes joins 946 as the faction ambushes The Bloodline on Raw",
       dek="The six-man between The Bloodline (Solo Sikoa and The Usos) and 946 ended in chaos when Carmelo Hayes revealed himself as the newest member of 946, and the group closed the show standing tall over The Bloodline.",
       src="Fightful", url="https://www.fightful.com/wrestling/wwe-raw-results-10-12-2026-the-bloodline-vs-946-chad-gable-vs-rey-fenix-liv-morgan-more/"),
  dict(date="2026-10-12", promo="wwe", cat="title", official=True, who="Chad Gable",
       hl="Chad Gable turns back Rey Fenix to keep the Intercontinental Title",
       dek="Chad Gable retained the Intercontinental Championship against Rey Fenix on Raw, with Ethan Page attacking Fenix backstage beforehand.",
       src="Fightful", url="https://www.fightful.com/wrestling/wwe-raw-results-10-12-2026-the-bloodline-vs-946-chad-gable-vs-rey-fenix-liv-morgan-more/"),

  # ---- AEW Dynamite Oct 14 (Cleveland) ----
  dict(date="2026-10-14", promo="aew", cat="retirement", official=True, who="Adam Copeland",
       hl="Adam Copeland announces he will retire in 2027",
       dek="On Dynamite, Adam Copeland said he will retire in 2027 and blamed Christian Cage for breaking his ribs, before the Don Callis Family attacked him. The night also set the Clockwork Carnage field with qualifier wins for Ricochet, Takeshita and Copeland.",
       src="Fightful", url="https://www.fightful.com/wrestling/aew-dynamite-results-10-14-2026-will-ospreay-andrade-in-tag-action-clockwork-carnage-qualifiers-mercedes-mone-dani-luna-more/"),

  # ---- WWE SmackDown Oct 16 (Sacramento) ----
  dict(date="2026-10-16", promo="wwe", cat="event", official=True, who="Cody Rhodes", home=True, htags="rivalries",
       hl="Randy Orton costs Cody Rhodes again as their feud boils over on SmackDown",
       dek="Cody Rhodes beat Baron Corbin by disqualification in Sacramento when Randy Orton interfered, and Orton then drove Cody into the steel steps as the former partners' rivalry intensified.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-10-16/results"),

  # ---- TNA iMPACT Oct 15 (San Antonio) ----
  dict(date="2026-10-15", promo="tna", cat="event", official=True, who="Trey Miguel",
       hl="Trey Miguel wins a ladder match to earn a shot at champion Leon Slater",
       dek="Trey Miguel won a five-way ladder match on iMPACT to become number one contender to new TNA World Champion Leon Slater, with the title match set for Destination X on November 15.",
       src="WrestlingInc", url="https://www.wrestlinginc.com/2287262/tna-thursday-night-impact-october-15-2026-results/"),
  # =============== end week of October 12 - October 18, 2026 ===============
'''

def patch(path, anchor, block, marker):
    full = os.path.join(ROOT, path)
    s = open(full, encoding="utf-8").read()
    if marker in s:
        print("  already present, skipping:", marker); return
    if anchor not in s:
        raise SystemExit("ANCHOR NOT FOUND in %s" % path)
    open(full, "w", encoding="utf-8").write(s.replace(anchor, anchor + block, 1))
    print("  inserted:", marker)

patch("build/build_lorefeed.py", "DISPATCHES = [", DISPATCH_BLOCK, "WEEK OF OCTOBER 12 - OCTOBER 18, 2026")
print("done")
