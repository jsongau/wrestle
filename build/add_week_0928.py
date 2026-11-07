#!/usr/bin/env python3
"""add_week_0928.py - open the week of Sep 28 - Oct 4, 2026, and backfill the
Sep 26 PLE results (WWE x AAA Worlds Collide + AEW All Out).

    WL_ROOT="$PWD" python3 build/add_week_0928.py

Idempotent. Two insert blocks into build_lorefeed.py (both land after
`DISPATCHES = [`): a PLE backfill block (Sep 26 dates -> auto-group into the
Sep 21 lore week) and the Week-of-Sep-28 block. The generator sorts by date,
so insertion order does not matter.

ASSEMBLY DECISIONS (researched Nov 7, 2026):
 - LEAD: the passing of PAC (Benjamin Satterley), 40. Confirmed by AEW
   Sep 27; he had wrestled his final match at All Out in the Chicago area.
   Cause not stated -> NOT speculated. AEW's Sep 30 Dynamite was a tribute
   show (ten-bell salute, Moxley promo); TNA iMPACT and WWE Raw also paid
   tribute. cat="passing", handled respectfully.
 - PLE BACKFILL (Sep 26, both shows ran head-to-head in the Chicago area):
   * AEW All Out: Ospreay ret. World Title over Moxley (Hidden Blade);
     Young Bucks won the World Tag Titles in a three-team ladder match over
     champions Cage & Copeland (FTR involved); Thekla beat Willow to earn
     Mercedes Mone at WrestleDream Oct 17.
   * WWE x AAA Worlds Collide (taped Sep 26, aired on YouTube Sep 30):
     CM Punk/Rey Mysterio/El Grande Americano won the six-man main event;
     La Catalina ret. AAA Reina de Reinas over Roxanne Perez.
 - SmackDown Oct 2 verified via WWE.com + WrestlingInc: Owens won the last
   men's MITB qualifier (Orton derailed Cody); Stratton won the women's.
 - Collision Oct 3 (Fightful, opened): Moxley ret. Continental; AEW set a
   Clockwork Carnage World Title match for WrestleDream.
 - home=True budget: FIVE (PAC lead, Jaida Parker/946, Owens/MITB, Waller,
   Hardys). htags only on home items, from {matches,titles,rivalries,roster}.
 - No gallery block here; verified-video pass handled separately.
"""
import os

ROOT = os.environ.get("WL_ROOT", os.getcwd())

# ---- Sep 26 PLE backfill (auto-groups into the Sep 21 lore week) ----
BACKFILL_BLOCK = '''
  # ============ SEP 26 PLE BACKFILL - WORLDS COLLIDE / ALL OUT (groups into wk of Sep 21) ============
  # Both shows ran head-to-head Sat Sep 26 in the Chicago area. Added Nov 7. See build/add_week_0928.py.
  dict(date="2026-09-26", promo="aew", cat="title", official=True, who="Will Ospreay",
       hl="Will Ospreay pins Jon Moxley to retain the AEW World Championship at All Out",
       dek="In the All Out main event in the Chicago area, Ospreay survived heavy interference and a briefcase shot to beat Moxley with the Hidden Blade in his first defense since winning the title at All In. Moxley placed the belt on Ospreay's shoulder afterward in a show of respect.",
       src="WrestlingInc", url="https://www.wrestlinginc.com/2269727/aew-all-out-2026-several-titles-on-line-two-number-one-contenders-matches/"),
  dict(date="2026-09-26", promo="aew", cat="title", official=True, who="The Young Bucks",
       hl="The Young Bucks climb to capture the AEW World Tag Team Titles at All Out",
       dek="Matt and Nick Jackson pulled the belts down in a three-team ladder match to dethrone champions Christian Cage and Adam Copeland, with FTR also in the match.",
       src="WrestlingInc", url="https://www.wrestlinginc.com/2269727/aew-all-out-2026-several-titles-on-line-two-number-one-contenders-matches/"),
  dict(date="2026-09-26", promo="aew", cat="event", official=True, who="Thekla",
       hl="Thekla beats Willow Nightingale to earn a shot at Mercedes Mone",
       dek="Thekla won the Women's World Championship number one contender match and will challenge Mercedes Mone at WrestleDream on October 17. Mone appeared afterward to hold up the title.",
       src="WrestlingInc", url="https://www.wrestlinginc.com/2269727/aew-all-out-2026-several-titles-on-line-two-number-one-contenders-matches/"),
  dict(date="2026-09-26", promo="wwe", cat="event", official=True, who="CM Punk",
       hl="CM Punk, Rey Mysterio and El Grande Americano win the Worlds Collide main event",
       dek="At the WWE x AAA Worlds Collide show in the Chicago area, the trio beat Dominik Mysterio, JD McDonagh and Omos, with Punk landing the GTS on McDonagh. The card was taped September 26 and aired on WWE's YouTube channel on September 30.",
       src="WWE.com", url="https://www.wwe.com/shows/wwe-worlds-collide/2026"),
  dict(date="2026-09-26", promo="wwe", cat="title", official=True, who="La Catalina",
       hl="La Catalina retains the AAA Reina de Reinas Title over Roxanne Perez",
       dek="La Catalina countered Perez's Pop Rox to keep the championship at Worlds Collide. Perez attacked her after the bell and raised the title high.",
       src="WWE.com", url="https://www.wwe.com/shows/wwe-worlds-collide/2026"),
  # ============ end Sep 26 PLE backfill ============
'''

DISPATCH_BLOCK = '''
  # ================= WEEK OF SEPTEMBER 28 - OCTOBER 4, 2026 =================
  # Assembled Nov 7. Lead: the passing of PAC (Benjamin Satterley). MITB fields
  # set; Bloodline-946 war escalates; Dusty Classic rolls on; BFG build on TNA.
  # See build/add_week_0928.py.

  dict(date="2026-09-28", promo="aew", cat="passing", official=True, who="PAC", lead=True, mono="In Memoriam", home=True, htags="roster",
       hl="Wrestling mourns PAC, Benjamin Satterley, dead at 40",
       dek="AEW confirmed that Benjamin Satterley, the British star known as PAC and formerly Neville in WWE, had died at 40, a day after wrestling at All Out in the Chicago area. A cause was not given. AEW's September 30 Dynamite became a tribute show with a ten-bell salute and an emotional Jon Moxley promo, and TNA iMPACT and WWE honored him on their programs.",
       src="Cleveland 19", url="https://www.cleveland19.com/2026/09/28/aew-star-benjamin-pac-satterley-dead-40/"),

  # ---- WWE: Raw Sep 28 (Milwaukee) ----
  dict(date="2026-09-28", promo="wwe", cat="event", official=True, who="Jaida Parker", home=True, htags="rivalries",
       hl="Jaida Parker revealed as 946 as the faction war with The Bloodline explodes on Raw",
       dek="946 (Royce Keys, Bronco Nima and Lucien Price) escalated their war with The Bloodline in Milwaukee, and Jaida Parker was revealed as a member of the group, striking Jacob Fatu with a car during the chaos.",
       src="Fightful", url="https://www.fightful.com/wrestling/wwe-raw-results-9-28-2026-stephanie-vaquer-appears-bloodline-calls-out-946-more/"),
  dict(date="2026-09-28", promo="wwe", cat="media", official=True, who="Stephanie Vaquer",
       hl="Stephanie Vaquer books Liv Morgan vs. Becky Lynch to name her next challenger",
       dek="Women's World Champion Stephanie Vaquer announced that Liv Morgan and Becky Lynch would meet on Raw the following week, with the winner earning a shot at her title.",
       src="Fightful", url="https://www.fightful.com/wrestling/wwe-raw-results-9-28-2026-stephanie-vaquer-appears-bloodline-calls-out-946-more/"),

  # ---- WWE: SmackDown Oct 2 (Denver) ----
  dict(date="2026-10-02", promo="wwe", cat="event", official=True, who="Kevin Owens", home=True, htags="matches",
       hl="Kevin Owens and Tiffany Stratton win the final Money in the Bank qualifiers",
       dek="On SmackDown in Denver, Kevin Owens beat Cody Rhodes and Johnny Gargano for the last men's ladder spot after Randy Orton derailed Rhodes, while Tiffany Stratton won her triple threat to complete the women's field for Money in the Bank on October 10 in New Orleans.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-10-02/results"),

  # ---- NXT Sep 29 (Orlando) ----
  dict(date="2026-09-29", promo="nxt", cat="title", official=True, who="Grayson Waller", home=True, htags="titles",
       hl="Grayson Waller answers an open challenge as the Dusty Classic rolls on",
       dek="NXT Champion Grayson Waller beat EK Prosper in an open challenge in Orlando, while Fraxiom and the team of Mini Vikingo and Chazz Hall advanced in the Dusty Rhodes Tag Team Classic.",
       src="Fightful", url="https://www.fightful.com/wrestling/wwe-nxt-results-9-29-2026-grayson-waller-defends-the-nxt-title-dusty-cup-continues-more/"),

  # ---- AEW Collision Oct 3 (Highland Heights, KY) ----
  dict(date="2026-10-03", promo="aew", cat="title", official=True, who="Jon Moxley",
       hl="Jon Moxley retains the Continental Championship as WrestleDream takes shape",
       dek="Moxley beat Jake Doyle in a Continental Championship Eliminator on Collision, and AEW announced the World Championship will be defended in a Clockwork Carnage match at WrestleDream. Paul Wight and Nigel McGuinness paid tribute to PAC during the broadcast.",
       src="Fightful", url="https://www.fightful.com/wrestling/aew-collision-results-10-3-2026-kofi-vs-lee-moriarty-jon-moxley-death-riders-queen-aminata-more/"),

  # ---- TNA iMPACT Oct 1 (San Antonio) ----
  dict(date="2026-10-01", promo="tna", cat="event", official=True, who="The Hardys", home=True, htags="rivalries",
       hl="The Hardys and Syx sign a No-DQ Bound for Glory clash on iMPACT",
       dek="On an iMPACT dedicated to PAC, Joseph Sawyer and Samuel Shaw of Syx targeted the Hardys, and a No Disqualification, Falls Count Anywhere tag match was announced for Bound for Glory. A four-way for the International Title was also set for the pay-per-view.",
       src="Fightful", url="https://www.fightful.com/wrestling/tna-impact-results-10-1-syx-to-speak-leon-slater-competes/"),
  # =============== end week of September 28 - October 4, 2026 ===============
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

patch("build/build_lorefeed.py", "DISPATCHES = [", BACKFILL_BLOCK, "SEP 26 PLE BACKFILL")
patch("build/build_lorefeed.py", "DISPATCHES = [", DISPATCH_BLOCK, "WEEK OF SEPTEMBER 28 - OCTOBER 4, 2026")
print("done")
