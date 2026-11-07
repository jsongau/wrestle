#!/usr/bin/env python3
"""add_week_1026.py - open the week of Oct 26 - Nov 1, 2026 (Halloween Havoc).

    WL_ROOT="$PWD" python3 build/add_week_1026.py

Idempotent. Inserts one block after `DISPATCHES = [` in build_lorefeed.py.

ASSEMBLY DECISIONS (researched Nov 7, 2026):
 - LEAD: NXT Halloween Havoc (Sat Oct 31, PC Orlando). Grayson Waller ret. the
   NXT Title over Tony D'Angelo; Kelani Jordan ret. the Women's Title; CM Punk
   called Waller out and will challenge for the NXT Title. (Fightful)
 - AEW Fright Night Dynamite (Oct 28, St. Louis): Queen Aminata beat Persephone
   for the TBS Title (TITLE CHANGE); Darby ret. TNT; MCMG lead FTR 2-1; Blood &
   Guts set for the next Dynamite; Full Gear (Nov 14) build. (WrestlingInc)
 - SmackDown Oct 30 (Charleston): Sami Zayn ret. the Undisputed WWE Title over
   Trick Williams (restarted No-DQ, belt shot); Crown Jewel card set - Reigns vs
   Zayn (champ vs champ), Cody vs Orton (Last Man Standing), Chelsea Green vs Liv
   Morgan; Finn Balor's Demon laid out Gunther. (WWE.com/Sacnilk)
 - Raw Oct 26 (Fresno): Zayn ret. over Je'Von Evans; Penta teased an MITB
   cash-in; Becky beat Liv Morgan by DQ (Morgan retained); Stratton's cash-in
   thwarted. (WWE.com/Khel Now). John Cena return rumor = single-source ->
   OMITTED.
 - home=True budget: FOUR (Waller lead, Aminata, Zayn, Balor). No gallery block.
"""
import os

ROOT = os.environ.get("WL_ROOT", os.getcwd())

DISPATCH_BLOCK = '''
  # ================= WEEK OF OCTOBER 26 - NOVEMBER 1, 2026 (Halloween Havoc) =================
  # Assembled Nov 7. Halloween Havoc headlines; Aminata wins the TBS title; Zayn
  # keeps the Undisputed Title and the Crown Jewel card locks in; the Demon
  # returns. See build/add_week_1026.py.

  # ---- WWE NXT Halloween Havoc (Oct 31, Orlando) ----
  dict(date="2026-10-31", promo="nxt", cat="title", official=True, who="Grayson Waller", lead=True, mono="Halloween Havoc", home=True, htags="titles rivalries",
       hl="Grayson Waller survives Halloween Havoc as CM Punk sets his sights on the NXT Title",
       dek="Grayson Waller retained the NXT Championship over Tony D'Angelo at Halloween Havoc in Orlando, and Kelani Jordan kept the Women's Title, before CM Punk appeared to call Waller out and promise a challenge for the gold. Danhausen hosted the Halloween special.",
       src="Fightful", url="https://www.fightful.com/wrestling/wwe-nxt-halloween-havoc-results-10-31-2026-danhausen-hosts-grayson-waller-kelani-jordan-zilla-fatu-more/"),

  # ---- AEW Fright Night Dynamite (Oct 28, St. Louis) ----
  dict(date="2026-10-28", promo="aew", cat="title", official=True, who="Queen Aminata", home=True, htags="titles",
       hl="Queen Aminata dethrones Persephone for the AEW TBS Championship",
       dek="On Fright Night Dynamite, Queen Aminata pinned Persephone with a running knee to win the TBS Championship, overcoming a belt shot from Britt Baker. Darby Allin also retained the TNT Title over Josh Alexander.",
       src="WrestlingInc", url="https://www.wrestlinginc.com/2297881/aew-fright-night-dynamite-october-28-2026-results/"),

  # ---- WWE SmackDown Oct 30 (Charleston) ----
  dict(date="2026-10-30", promo="wwe", cat="title", official=True, who="Sami Zayn", home=True, htags="titles rivalries",
       hl="Sami Zayn keeps the Undisputed WWE Title over Trick Williams as Crown Jewel locks in",
       dek="In a restarted No Disqualification match, Sami Zayn retained the Undisputed WWE Championship over Trick Williams with a title-belt shot. The Crown Jewel card took shape with Zayn vs. Roman Reigns, Cody Rhodes vs. Randy Orton in a Last Man Standing match, and Chelsea Green vs. Liv Morgan.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-10-30"),
  dict(date="2026-10-30", promo="wwe", cat="return", official=True, who="Finn Balor", home=True, htags="rivalries",
       hl="The Demon returns as Finn Balor lays out Gunther on SmackDown",
       dek="After Gunther attacked Danhausen, Finn Balor appeared as The Demon and drove Gunther through the announce table with a Coup de Grace off a ladder, with reports of a possible clash between them at Crown Jewel.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-10-30"),

  # ---- AEW Fright Night Dynamite build ----
  dict(date="2026-10-28", promo="aew", cat="event", official=True, who="Jon Moxley",
       hl="Blood and Guts is set as AEW builds toward Full Gear",
       dek="A Blood and Guts match was set between Team Allin and the Don Callis Family, and Jon Moxley challenged The Cut to an Anarchy in the Arena match at Full Gear on November 14. The Motor City Machine Guns also moved ahead of FTR in their best-of-five series.",
       src="WrestlingInc", url="https://www.wrestlinginc.com/2297881/aew-fright-night-dynamite-october-28-2026-results/"),

  # ---- WWE Raw Oct 26 (Fresno) ----
  dict(date="2026-10-26", promo="wwe", cat="event", official=True, who="Penta",
       hl="Penta teases his cash-in as Sami Zayn turns back Je'Von Evans on Raw",
       dek="Sami Zayn retained the Undisputed WWE Title over Je'Von Evans in Fresno when Penta appeared to tease a Money in the Bank cash-in and Bron Breakker intervened. Becky Lynch beat Liv Morgan by disqualification, with Morgan keeping the Women's World Title, and Tiffany Stratton's own cash-in attempt was thwarted.",
       src="WWE.com", url="https://www.wwe.com/shows/raw/2026-10-26"),
  # =============== end week of October 26 - November 1, 2026 ===============
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

patch("build/build_lorefeed.py", "DISPATCHES = [", DISPATCH_BLOCK, "WEEK OF OCTOBER 26 - NOVEMBER 1, 2026")
print("done")
