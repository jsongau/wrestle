#!/usr/bin/env python3
"""add_week_1019.py - open the week of Oct 19 - Oct 25, 2026 (Crown Jewel build).

    WL_ROOT="$PWD" python3 build/add_week_1019.py

Idempotent. Inserts one block after `DISPATCHES = [` in build_lorefeed.py.

ASSEMBLY DECISIONS (researched Nov 7, 2026):
 - No PLE this week; Crown Jewel is Nov 7 in Riyadh. Lead is the Crown Jewel
   card forming, anchored by Cody Rhodes vs Randy Orton (Last Man Standing).
 - SmackDown Oct 23 (Ontario, CA): Michin & B-Fab beat Bliss & Paxley for the
   Women's Tag Titles (TITLE CHANGE); Chelsea Green ret. WWE Women's Title over
   Roxanne Perez; Cody vs Orton Last Man Standing set for Crown Jewel; Sami
   Zayn vs Trick Williams (Undisputed) set for Oct 30; Stratton teased an MITB
   cash-in on Liv Morgan.
 - Raw Oct 19 (San Diego): Reigns returned to aid The Bloodline vs 946 (Carmelo
   Hayes now in 946); Reigns and Undisputed champ Sami Zayn traded words over
   Crown Jewel; Gable ret. IC in a triple threat; Penta beat Bron Breakker.
 - Dynamite Oct 21 (Coral Gables): Ilja Dragunov beat Mike Bailey in his AEW
   in-ring debut; a Blood & Guts challenge was issued; Swerve demanded a Trios
   rematch as AEW builds to Full Gear (Nov 14, per WrestlingInc).
 - home=True budget: FOUR (Cody/Orton lead, Michin/B-Fab, Reigns/Raw, Dragunov).
 - No gallery block here.
"""
import os

ROOT = os.environ.get("WL_ROOT", os.getcwd())

DISPATCH_BLOCK = '''
  # ================= WEEK OF OCTOBER 19 - OCTOBER 25, 2026 (Crown Jewel build) =================
  # Assembled Nov 7. Crown Jewel card forms (Cody vs Orton Last Man Standing);
  # Michin & B-Fab win the women's tag titles; Reigns returns on Raw; Ilja
  # Dragunov wins his AEW in-ring debut. See build/add_week_1019.py.

  # ---- WWE SmackDown Oct 23 (Ontario, CA) ----
  dict(date="2026-10-23", promo="wwe", cat="event", official=True, who="Cody Rhodes", lead=True, mono="Crown Jewel", home=True, htags="rivalries",
       hl="Cody Rhodes and Randy Orton sign a Last Man Standing match for Crown Jewel",
       dek="On SmackDown, GM Nick Aldis booked Cody Rhodes against Randy Orton at Crown Jewel in Riyadh on November 7, and Rhodes insisted on Last Man Standing rules as the former partners' feud turned personal.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-10-23/results"),
  dict(date="2026-10-23", promo="wwe", cat="title", official=True, who="Michin", home=True, htags="titles",
       hl="Michin and B-Fab capture the Women's Tag Team Titles on SmackDown",
       dek="Jade Cargill struck Tatum Paxley from ringside, and Michin pinned her with a Styles Clash as Michin and B-Fab beat Alexa Bliss and Paxley for the Women's Tag Team Championship.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-10-23/results"),
  dict(date="2026-10-23", promo="wwe", cat="title", official=True, who="Chelsea Green",
       hl="Chelsea Green turns back Roxanne Perez as Stratton stalks a cash-in",
       dek="Chelsea Green retained the WWE Women's Championship against Roxanne Perez, and Tiffany Stratton nearly cashed in her Money in the Bank contract on Liv Morgan before Morgan escaped.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-10-23/results"),

  # ---- WWE Raw Oct 19 (San Diego) ----
  dict(date="2026-10-19", promo="wwe", cat="event", official=True, who="Roman Reigns", home=True, htags="rivalries",
       hl="Roman Reigns returns on Raw to stand with The Bloodline against 946",
       dek="Reigns made a surprise return to help The Usos and Solo Sikoa clear out 946, now bolstered by Carmelo Hayes, and traded words with Undisputed WWE Champion Sami Zayn over which title matters most ahead of Crown Jewel. Chad Gable retained the Intercontinental Title in a triple threat.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-10-19"),

  # ---- AEW Dynamite Oct 21 (Coral Gables) ----
  dict(date="2026-10-21", promo="aew", cat="event", official=True, who="Ilja Dragunov", home=True, htags="rivalries",
       hl="Ilja Dragunov wins his AEW in-ring debut over Mike Bailey",
       dek="Days after arriving at WrestleDream, Ilja Dragunov beat Speedball Mike Bailey with an H-Bomb on Dynamite. Later, Darby Allin, Steven Borden, The Young Bucks, Will Ospreay and Adam Copeland issued a Blood and Guts challenge to the Don Callis Family.",
       src="WrestlingInc", url="https://www.wrestlinginc.com/2292521/aew-dynamite-october-21-2026-results/"),
  dict(date="2026-10-21", promo="aew", cat="event", official=True, who="Swerve Strickland",
       hl="Swerve Strickland demands a Trios rematch as AEW builds to Full Gear",
       dek="Swerve Strickland pushed for a World Trios Championship rematch against Adam Page, Brody King and Bandido, calling for a Texas Death Match, as AEW set its sights on Full Gear.",
       src="WrestlingInc", url="https://www.wrestlinginc.com/2292521/aew-dynamite-october-21-2026-results/"),
  # =============== end week of October 19 - October 25, 2026 ===============
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

patch("build/build_lorefeed.py", "DISPATCHES = [", DISPATCH_BLOCK, "WEEK OF OCTOBER 19 - OCTOBER 25, 2026")
print("done")
