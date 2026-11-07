#!/usr/bin/env python3
"""add_week_1102.py - open the current week, Nov 2 - Nov 6, 2026 (Crown Jewel go-home).

    WL_ROOT="$PWD" python3 build/add_week_1102.py

Idempotent. Inserts one block after `DISPATCHES = [` in build_lorefeed.py.

ASSEMBLY DECISIONS (researched Nov 7, 2026 - the current week):
 - LEAD: John Cena returned to Raw in Brooklyn (Nov 2) and launched the John Cena
   Classic (Dec 14), naming Cody Rhodes the first invitee. (Fightful + WrestlingInc)
 - Raw Nov 2 (Barclays): Ethan Page beat Chad Gable for the Intercontinental Title
   (TITLE CHANGE); Reigns/Zayn final build; Solo Sikoa beat Royce Keys by DQ.
 - AEW Dynamite Blood & Guts (Nov 4): the Don Callis Family beat Team Allin (Copeland
   surrendered); a Women's Blood & Guts also took place (Statlander's team won).
   NOTE: an "O'Reilly taps Moxley" result circulating was the 2025 show - NOT used.
 - NXT Nov 4: Grayson Waller retained the NXT Title over CM Punk (Kevin Owens
   distraction); Moreno & Dar won the Dusty Rhodes Tag Team Classic final.
 - SmackDown Nov 6 (Brooklyn, taped): Kevin Owens beat CM Punk, No Holds Barred
   (single-source taping report -> flagged, non-home).
 - Crown Jewel PREVIEW (Nov 7, Riyadh): Reigns vs Zayn (champ vs champ), Cody vs
   Orton (Last Man Standing) - event has NOT happened yet, filed as a preview.
 - TNA iMPACT Oct 22/29 and Nov 5 not cleanly sourced -> omitted rather than guessed
   (known gap; TNA coverage current through Oct 15 + Bound for Glory).
 - home=True budget: FIVE (Cena lead, Page/IC, Blood & Guts, NXT, Crown Jewel).
 - No gallery block here.
"""
import os

ROOT = os.environ.get("WL_ROOT", os.getcwd())

DISPATCH_BLOCK = '''
  # ================= WEEK OF NOVEMBER 2 - NOVEMBER 6, 2026 (Crown Jewel go-home) =================
  # Assembled Nov 7 (current week). Cena returns in Brooklyn; Ethan Page takes the
  # IC title; Blood & Guts; Waller turns back CM Punk; Crown Jewel looms tonight.
  # See build/add_week_1102.py.

  # ---- WWE Raw Nov 2 (Brooklyn) ----
  dict(date="2026-11-02", promo="wwe", cat="media", official=True, who="John Cena", lead=True, mono="Cena Returns", home=True, htags="roster",
       hl="John Cena returns to Raw in Brooklyn and launches the John Cena Classic",
       dek="John Cena appeared at Barclays Center to unveil the John Cena Classic, a December 14 event, naming Cody Rhodes the first invitee and promising to scout talent at Survivor Series: WarGames. The go-home Raw also ended with Sami Zayn leveling Roman Reigns with a Helluva Kick before Crown Jewel.",
       src="Fightful", url="https://www.fightful.com/wrestling/wwe-raw-results-11-2-2026-solo-sikoa-vs-royce-keys-john-cena-roman-reigns-more/"),
  dict(date="2026-11-02", promo="wwe", cat="title", official=True, who="Ethan Page", home=True, htags="titles",
       hl="Ethan Page dethrones Chad Gable for the Intercontinental Championship on Raw",
       dek="Ethan Page beat Chad Gable in Brooklyn to win the Intercontinental Championship, ending Gable's reign after weeks of attacks alongside Big Cass.",
       src="WrestlingInc", url="https://www.wrestlinginc.com/2303334/wwe-raw-november-2-2026-results/"),

  # ---- AEW Dynamite: Blood & Guts (Nov 4) ----
  dict(date="2026-11-04", promo="aew", cat="event", official=True, who="Don Callis Family", home=True, htags="matches rivalries",
       hl="The Don Callis Family wins Blood and Guts as Adam Copeland surrenders",
       dek="In the men's Blood and Guts, the Don Callis Family beat Team Allin when Adam Copeland surrendered while chained to the cage with Kyle Fletcher holding a screwdriver to Will Ospreay's throat. Earlier, Kris Statlander's team won the women's Blood and Guts.",
       src="WrestlingInc", url="https://www.wrestlinginc.com/2307145/aew-dynamite-november-4-2026-results/"),

  # ---- WWE NXT Nov 4 ----
  dict(date="2026-11-04", promo="nxt", cat="title", official=True, who="Grayson Waller", home=True, htags="titles",
       hl="Grayson Waller turns back CM Punk as Moreno and Dar win the Dusty Classic",
       dek="Grayson Waller retained the NXT Championship over CM Punk after a Kevin Owens distraction let him roll Punk up with the tights. Romeo Moreno and Noam Dar won the Dusty Rhodes Tag Team Classic final, with Cody Rhodes presenting the cup.",
       src="WWE.com", url="https://www.wwe.com/shows/wwenxt/2026-11-4"),

  # ---- WWE Crown Jewel PREVIEW (Nov 7, Riyadh) ----
  dict(date="2026-11-06", promo="wwe", cat="event", official=True, who="Roman Reigns", home=True, htags="rivalries",
       hl="Crown Jewel descends on Riyadh with Reigns vs. Zayn and Cody vs. Orton",
       dek="WWE Crown Jewel emanates from Riyadh on November 7 in a champion-versus-champion main event, World Heavyweight Champion Roman Reigns against Undisputed WWE Champion Sami Zayn, with Cody Rhodes meeting Randy Orton in a Last Man Standing match. (Preview - the event had not taken place at publication.)",
       src="WWE.com", url="https://www.wwe.com/shows/wwe-crown-jewel/crown-jewel-2026"),

  # ---- WWE SmackDown Nov 6 (Brooklyn, taped) ----
  dict(date="2026-11-06", promo="wwe", cat="event", official=True, who="Kevin Owens",
       hl="Kevin Owens beats CM Punk in a No Holds Barred war in Brooklyn",
       dek="On a SmackDown taped at Barclays Center, Kevin Owens beat CM Punk in a No Holds Barred match, driving him through the announce table, as the Baddies and Fatal Influence teased a WarGames collision.",
       src="Sacnilk", url="https://www.sacnilk.com/news/wwe-smackdown-spoilers-november-6-2026-taped-results-winners"),
  # =============== end week of November 2 - November 6, 2026 ===============
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

patch("build/build_lorefeed.py", "DISPATCHES = [", DISPATCH_BLOCK, "WEEK OF NOVEMBER 2 - NOVEMBER 6, 2026")
print("done")
