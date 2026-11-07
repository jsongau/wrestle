#!/usr/bin/env python3
"""add_week_1005.py - open the week of Oct 5 - Oct 11, 2026.

A DOUBLE-PLE week: WWE Money in the Bank (Sat Oct 10, New Orleans) and
TNA Bound for Glory (Sun Oct 11, Tampa).

    WL_ROOT="$PWD" python3 build/add_week_1005.py

Idempotent. Inserts one block after `DISPATCHES = [` in build_lorefeed.py.

ASSEMBLY DECISIONS (researched Nov 7, 2026):
 - LEAD: Penta wins the men's Money in the Bank ladder match. Verified across
   WrestlingInc live blog + Sacnilk + Khel Now.
 - MITB (Oct 10, Smoothie King Center): Reigns ret. World Heavyweight Title over
   LA Knight; Liv Morgan beat champ Vaquer + Becky to WIN the Women's World
   Title; Tiffany Stratton won the women's briefcase. No cash-ins.
 - BFG (Oct 11, Yuengling Center, Tampa): Leon Slater beat Nic Nemeth to win the
   TNA World Title (youngest ever, via Option C); Amazing Red won the vacant
   X-Division Title in a 7-way, hours after his HOF induction; Jason Hotch won
   the International Title 4-way over Ali; Indi Hartwell won the Knockouts World
   Title over Xia Brookside (Mickie James ref); Serrano & Baszler won the
   Knockouts Tag Titles; Syx beat the Hardys (Falls Count Anywhere, Erick
   Redbeard helped). Verified: WrestlingInc + Wikipedia + ChaseYourSport.
 - SmackDown Oct 9: Bliss & Paxley won the Women's Tag Titles (Bliss subbing for
   injured Charlotte Flair). Raw Oct 5: Vaquer interference made MITB women's a
   triple threat; Reigns/Knight face-off.
 - home=True budget: FIVE (Penta lead, Liv, Bliss, Slater, Amazing Red).
 - No gallery block here; verified-video pass handled separately.
"""
import os

ROOT = os.environ.get("WL_ROOT", os.getcwd())

DISPATCH_BLOCK = '''
  # ================= WEEK OF OCTOBER 5 - OCTOBER 11, 2026 (MITB + Bound for Glory) =================
  # Assembled Nov 7. Double-PLE week. Penta + Stratton win briefcases; Liv Morgan
  # dethrones Vaquer; Reigns ret.; Bliss/Paxley win tag gold; and at Bound for
  # Glory Leon Slater becomes the youngest TNA World Champ with four more title
  # changes. See build/add_week_1005.py.

  # ---- WWE Money in the Bank (Oct 10, New Orleans) ----
  dict(date="2026-10-10", promo="wwe", cat="event", official=True, who="Penta", lead=True, mono="Money in the Bank", home=True, htags="matches",
       hl="Penta climbs to win the men's Money in the Bank briefcase in New Orleans",
       dek="At Money in the Bank, Penta won the men's ladder match over Bron Breakker, CM Punk, Kevin Owens, Trick Williams and Je'Von Evans, hitting Breakker with a Mexican Destroyer onto a bridged ladder before pulling down the briefcase. Breakker had earlier speared Evans through an ambulance.",
       src="WrestlingInc", url="https://www.wrestlinginc.com/2281848/wwe-money-in-the-bank-2026-results/"),
  dict(date="2026-10-10", promo="wwe", cat="title", official=True, who="Liv Morgan", home=True, htags="titles rivalries",
       hl="Liv Morgan dethrones Stephanie Vaquer for the Women's World Championship",
       dek="In a triple threat at Money in the Bank, Liv Morgan pinned champion Stephanie Vaquer with Oblivion, after Vaquer sent Becky Lynch into a table, to capture the Women's World Championship.",
       src="WrestlingInc", url="https://www.wrestlinginc.com/2281848/wwe-money-in-the-bank-2026-results/"),
  dict(date="2026-10-10", promo="wwe", cat="event", official=True, who="Tiffany Stratton",
       hl="Tiffany Stratton wins the women's Money in the Bank ladder match",
       dek="Stratton outlasted Sol Ruca, Lola Vice, Jacy Jayne, Roxanne Perez and Lash Legend, using the briefcase to knock Legend off a ladder before unclipping it to earn a guaranteed title shot.",
       src="WrestlingInc", url="https://www.wrestlinginc.com/2281848/wwe-money-in-the-bank-2026-results/"),
  dict(date="2026-10-10", promo="wwe", cat="title", official=True, who="Roman Reigns",
       hl="Roman Reigns turns back LA Knight to keep the World Heavyweight Title",
       dek="Reigns beat LA Knight with a Spear to retain the World Heavyweight Championship. Afterward 946 confronted Reigns, and The Usos and Solo Sikoa brawled with the group.",
       src="WrestlingInc", url="https://www.wrestlinginc.com/2281848/wwe-money-in-the-bank-2026-results/"),

  # ---- WWE SmackDown Oct 9 (Lafayette) ----
  dict(date="2026-10-09", promo="wwe", cat="title", official=True, who="Alexa Bliss", home=True, htags="titles",
       hl="Alexa Bliss and Tatum Paxley capture the Women's Tag Team Titles on SmackDown",
       dek="Standing in for an injured Charlotte Flair, Bliss teamed with Tatum Paxley to beat Fatal Influence (Fallon Henley and Lainey Reid) in Lafayette, with Paxley landing Cemetery Drive on Henley. It is Bliss's fifth women's tag title reign.",
       src="Sacnilk", url="https://www.sacnilk.com/news/new-champions-crowned-on-wwe-smackdown-october-9-2026"),

  # ---- WWE Raw Oct 5 (St. Louis) ----
  dict(date="2026-10-05", promo="wwe", cat="event", official=True, who="Stephanie Vaquer",
       hl="Vaquer's interference turns the Women's World Title into a Money in the Bank triple threat",
       dek="On Raw in St. Louis, Becky Lynch vs. Liv Morgan broke down when champion Stephanie Vaquer interfered, and Adam Pearce added both challengers to make it a triple threat at Money in the Bank. Roman Reigns and LA Knight came face to face ahead of their title match.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-10-05/results"),

  # ---- TNA Bound for Glory (Oct 11, Tampa) ----
  dict(date="2026-10-11", promo="tna", cat="title", official=True, who="Leon Slater", home=True, htags="titles matches",
       hl="Leon Slater becomes the youngest TNA World Champion at Bound for Glory",
       dek="Having given up the X-Division Title to invoke Option C, Leon Slater beat Nic Nemeth with a Swanton 450 in Tampa to win the TNA World Championship and become the youngest champion in company history.",
       src="WrestlingInc", url="https://www.wrestlinginc.com/2283301/tna-bound-for-glory-2026-results/"),
  dict(date="2026-10-11", promo="tna", cat="title", official=True, who="Amazing Red", home=True, htags="titles",
       hl="Amazing Red wins the vacant X-Division Title hours after his Hall of Fame induction",
       dek="Inducted into the TNA Hall of Fame on the pre-show, Amazing Red then won a seven-way scramble for the vacant X-Division Championship, pinning KC Navarro with a Code Red.",
       src="WrestlingInc", url="https://www.wrestlinginc.com/2283301/tna-bound-for-glory-2026-results/"),
  dict(date="2026-10-11", promo="tna", cat="title", official=True, who="Jason Hotch",
       hl="Jason Hotch pins Mustafa Ali to take the TNA International Title",
       dek="In a fatal four-way, Jason Hotch rolled up champion Mustafa Ali to win the International Championship, with John Skyler and Special Agent Zero also in the match after the Order 4 breakup.",
       src="WrestlingInc", url="https://www.wrestlinginc.com/2283301/tna-bound-for-glory-2026-results/"),
  dict(date="2026-10-11", promo="tna", cat="title", official=True, who="Indi Hartwell",
       hl="Indi Hartwell dethrones Xia Brookside for the Knockouts World Title",
       dek="With Mickie James as special guest referee, Indi Hartwell beat champion Xia Brookside with a Nelson slam to win the Knockouts World Championship at Bound for Glory.",
       src="WrestlingInc", url="https://www.wrestlinginc.com/2283301/tna-bound-for-glory-2026-results/"),
  dict(date="2026-10-11", promo="tna", cat="event", official=True, who="Syx",
       hl="Syx beat the Hardys in a Falls Count Anywhere war as Erick Redbeard appears",
       dek="Joseph Sawyer and Samuel Shaw of Syx beat Matt and Jeff Hardy in a Falls Count Anywhere match, with Erick Redbeard appearing mid-match to help the faction. Frankie Kazarian had earlier won the Call Your Shot Gauntlet.",
       src="WrestlingInc", url="https://www.wrestlinginc.com/2283301/tna-bound-for-glory-2026-results/"),
  # =============== end week of October 5 - October 11, 2026 ===============
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

patch("build/build_lorefeed.py", "DISPATCHES = [", DISPATCH_BLOCK, "WEEK OF OCTOBER 5 - OCTOBER 11, 2026")
print("done")
