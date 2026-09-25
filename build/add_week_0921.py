#!/usr/bin/env python3
"""add_week_0921.py - open the week of Sep 21 - Sep 25, 2026 (through Sep 25 AM).

    WL_ROOT="$PWD" python3 build/add_week_0921.py

Idempotent. Gallery weeks PREPEND, so this leaves 2026-09-21 as WEEKS[0] and
the homepage This-Week block regenerates from it.

ASSEMBLY DECISIONS (Sep 25, 2026):
 - Lead: 946 kidnaps Solo Sikoa on Raw 9/21 in San Antonio - the faction
   threw Sikoa into an SUV and drove off while The Bloodline watched. Penta
   replaced Sikoa in the MITB qualifier and won. Confirmed by WrestleView
   and Fightful recaps, Yahoo Sports standalone.
 - SmackDown 9/25 airs TONIGHT; results not yet available. Only the
   announced card (Punk vs Gunther vs Balor MITB qualifier, Williams vs
   Corbin steel cage US title, Charlotte vs Giulia vs Lash Legend) is noted
   as a preview dispatch - NO invented results.
 - AEW ran a combined Dynamite+Collision on 9/23 as the All Out go-home
   show. Mike Bailey joined United Empire (official AEW announcement).
   Persephone retained TBS, Swerve & New Level retained Trios.
 - NXT 9/22 launched the Dusty Rhodes Tag Team Classic with two first-round
   matches. Grayson Waller and Mason Rook traded promos for their title
   feud.
 - TNA iMPACT 9/24: Syx faction revealed as Joseph Sawyer & Samuel Shaw.
   Mustafa Ali retained International title in a triple threat. Ryan
   Nemeth qualified for BFG.
 - WWE-Rumble partnership announced 9/24: Main Event moves to Rumble.com
   starting October 14.
 - Worlds Collide (Sep 26) and AEW All Out (Sep 27) full cards locked but
   the events have NOT happened yet - filed as previews.
 - home=True budget: FIVE (Sikoa, Oba Femi, Dusty Classic, Bailey, Syx).
   htags only with home=True. All htags from {matches,titles,rivalries,roster}.
 - All 8 video IDs oEmbed-verified: WWE (4), All Elite Wrestling (3),
   TNA Wrestling (1). No RAF episode this week (last was RAF 13 on 9/18).
"""
import os

ROOT = os.environ.get("WL_ROOT", os.getcwd())

DISPATCH_BLOCK = '''
  # ================= WEEK OF SEPTEMBER 21 - SEPTEMBER 25, 2026 (in progress) =================
  # Assembled Sep 25. 946 kidnaps Sikoa on Raw; Penta replaces him and qualifies
  # for MITB; Dusty Classic begins on NXT; AEW All Out go-home. SmackDown 9/25
  # airs tonight - preview card only, no results. See build/add_week_0921.py.

  # ---- WWE: Raw Sep 21 (San Antonio) ----
  dict(date="2026-09-21", promo="wwe", cat="event", official=True, who="Solo Sikoa", lead=True, mono="946 Strikes", home=True, htags="matches rivalries",
       hl="946 ambushes and kidnaps Solo Sikoa from Raw in San Antonio",
       dek="The faction 946 attacked Solo Sikoa backstage before his MITB qualifying match, threw him into an SUV and sped away. The Usos and Jacob Fatu pursued but could not intervene. Penta was inserted as Sikoa\\u2019s replacement and won the triple threat to qualify for Money in the Bank.",
       src="Yahoo Sports", url="https://sports.yahoo.com/articles/solo-sikoa-attacked-kidnapped-946-021209655.html"),
  dict(date="2026-09-21", promo="wwe", cat="event", official=True, who="Penta",
       hl="Penta wins MITB qualifier after replacing kidnapped Solo Sikoa on Raw",
       dek="Penta beat Dominik Mysterio and Dragon Lee in a triple threat after being inserted into the match following Sikoa\\u2019s abduction by 946. Penta earlier confronted Judgment Day, calling Mysterio the king of the pendejos.",
       src="WrestleView", url="https://www.wrestleview.com/wwe-raw-results/392979-live-wwe-raw-results-september-21-2026-san-antonio/"),
  dict(date="2026-09-21", promo="wwe", cat="event", official=True, who="Roxanne Perez",
       hl="Roxanne Perez qualifies for Women\\u2019s Money in the Bank on Raw",
       dek="Perez pinned IYO SKY and La Catalina in a triple threat to earn her spot in the women\\u2019s MITB ladder match on October 10 in New Orleans.",
       src="Fightful", url="https://www.fightful.com/wrestling/wwe-raw-results-9-21-2026-mitb-qualifiers-bayley-vs-lyra-valkyria-penta-la-knight-more/"),
  dict(date="2026-09-21", promo="wwe", cat="media", official=True, who="Liv Morgan",
       hl="Liv Morgan calls her title loss the Santiago Screwjob as Becky Lynch takes credit",
       dek="Morgan said she was robbed of the Women\\u2019s World Championship on Raw and labelled the September 12 Chile live event the Santiago Screwjob. Becky Lynch claimed responsibility and demanded first dibs at a title match against new champion Stephanie Vaquer.",
       src="WrestleView", url="https://www.wrestleview.com/wwe-raw-results/392979-live-wwe-raw-results-september-21-2026-san-antonio/"),
  dict(date="2026-09-21", promo="wwe", cat="media", official=True, who="LA Knight",
       hl="LA Knight vows to take Roman Reigns\\u2019 World Heavyweight Championship",
       dek="Knight cut a promo on Raw noting that Reigns has had no Bloodline interference recently and claiming he is the most self-made fighter in the game. He challenged Reigns for the World Heavyweight Title.",
       src="WrestleView", url="https://www.wrestleview.com/wwe-raw-results/392979-live-wwe-raw-results-september-21-2026-san-antonio/"),
  dict(date="2026-09-21", promo="wwe", cat="return", official=True, who="Oba Femi", home=True, htags="roster rivalries",
       hl="Oba Femi returns to Raw and attacks Bron Breakker after DQ finish",
       dek="After Je\\u2019Von Evans beat Bron Breakker by disqualification when The Vision interfered, Oba Femi made a surprise return and laid out Breakker. The attack signals a feud between the two powerhouses.",
       src="Fightful", url="https://www.fightful.com/wrestling/wwe-raw-results-9-21-2026-mitb-qualifiers-bayley-vs-lyra-valkyria-penta-la-knight-more/"),

  # ---- NXT Sep 22 (The CW) ----
  dict(date="2026-09-22", promo="nxt", cat="event", official=True, who="Creed Brothers", home=True, htags="matches",
       hl="Dusty Rhodes Tag Team Classic kicks off on NXT with two first-round wins",
       dek="The Creed Brothers beat Jax Presley and Harley Riggins while Romeo Moreno and Noam Dar upset Los Americanos to advance to the quarterfinals. Robert Stone announced the tournament\\u2019s return last week.",
       src="PW Torch", url="https://www.pwtorch.com/site/2026/09/23/nxt-tv-results-9-22-dusty-rhodes-tag-team-classic-legacy-zilla-fatu-ek-prosper-vs-birthright-kali-armstrong-vs-skylar-raye/"),
  dict(date="2026-09-22", promo="nxt", cat="media", official=True, who="Grayson Waller",
       hl="Grayson Waller and Mason Rook trade words as NXT Title feud heats up",
       dek="NXT Champion Waller and challenger Rook had a heated war of words, with Rook declaring himself the best big man in the game. Thea Hail earned a future title match by teaming with La Catalina to beat Zaria and Kelani Jordan.",
       src="WWE.com", url="https://www.wwe.com/shows/wwenxt/2026-09-22"),

  # ---- AEW: Dynamite + Collision Sep 23 (Indianapolis) ----
  dict(date="2026-09-23", promo="aew", cat="signing", official=True, who="Mike Bailey", home=True, htags="roster",
       hl="Speedball Mike Bailey joins Will Ospreay\\u2019s United Empire on Dynamite",
       dek="Bailey officially debuted as a member of the United Empire alongside AEW World Champion Will Ospreay on the All Out go-home show. AEW confirmed Bailey\\u2019s signing earlier in the week.",
       src="Fightful", url="https://www.fightful.com/wrestling/speedball-mike-bailey-joins-united-empire-on-aew-dynamite/"),
  dict(date="2026-09-23", promo="aew", cat="title", official=True, who="Persephone",
       hl="Persephone retains TBS Championship over Hyan and issues All Out open challenge",
       dek="The TBS Champion used an underhanded finish to beat Hyan on the Dynamite portion of the combined show, then announced a TBS Title open challenge for All Out on September 27.",
       src="AEW", url="https://www.allelitewrestling.com/post/aew-dynamite-collision-results-september-23-2026"),
  dict(date="2026-09-23", promo="aew", cat="title", official=True, who="Swerve Strickland",
       hl="Swerve and The New Level retain AEW World Trios Titles ahead of All Out",
       dek="Swerve Strickland and The New Level defended the World Trios Championship against The Demand on Dynamite. Their All Out opponents, The Good The Bad and The Ugly, were confirmed for the pay-per-view.",
       src="Fightful", url="https://www.fightful.com/wrestling/aew-dynamite-results-9-23-2026-persephone-vs-hyan-swerve-new-level-vs-demand-will-ospreay-more/"),
  dict(date="2026-09-23", promo="aew", cat="event", official=True, who="Will Ospreay",
       hl="Will Ospreay and Jon Moxley come face to face in final All Out build",
       dek="The AEW World Champion and his challenger closed the combined Dynamite-Collision show with a confrontation in Indianapolis. Ospreay defends against Moxley at All Out on Saturday, September 27 in Chicago.",
       src="AEW", url="https://www.allelitewrestling.com/post/aew-dynamite-collision-results-september-23-2026"),

  # ---- TNA iMPACT Sep 24 (San Antonio) ----
  dict(date="2026-09-24", promo="tna", cat="event", official=True, who="Syx", home=True, htags="rivalries",
       hl="Mystery faction Syx revealed as Joseph Sawyer and Samuel Shaw on iMPACT",
       dek="After weeks of ambushing wrestlers, the attackers of The Hardy Brothers unmasked as Joseph Sawyer and Samuel Shaw, forming the faction Syx. The Hardys challenged Sawyer and Shaw to a match next week.",
       src="TNA Wrestling", url="https://tnawrestling.com/news/tna-thursday-night-impact-on-amc-live-results-september-24-2026"),
  dict(date="2026-09-24", promo="tna", cat="title", official=True, who="Mustafa Ali",
       hl="Mustafa Ali retains TNA International Title in controversial triple threat",
       dek="Ali struck Trey Miguel with the championship belt and rolled him up to retain the International Championship in a triple threat that also featured Jason Hotch. Tasha Steelz assisted Ali during the finish.",
       src="TNA Wrestling", url="https://tnawrestling.com/news/tna-thursday-night-impact-on-amc-live-results-september-24-2026"),
  dict(date="2026-09-24", promo="tna", cat="event", official=True, who="Ryan Nemeth",
       hl="Ryan Nemeth qualifies for Bound for Glory X-Division Championship match",
       dek="Nemeth beat KJ Orso with the Hollywood Ending to secure his spot in the X-Division title match at Bound for Glory. Order 4 fractured as Mila Moore and John Skyler quit the faction after Ali discovered their relationship.",
       src="Ringside News", url="https://www.ringsidenews.com/tna-impact-results-highlights-key-moments-september-24-2026"),

  # ---- Industry / Business ----
  dict(date="2026-09-24", promo="industry", cat="business", official=True, who="WWE",
       hl="WWE Main Event moves to Rumble streaming platform starting October 14",
       dek="WWE and Rumble announced a long-term partnership to stream Main Event every Wednesday at 8 PM ET on Rumble.com and its apps, replacing its previous Peacock home. The move adds another distribution channel for weekly WWE content.",
       src="WWE Corporate", url="https://corporate.wwe.com/about/news/2026/09-24-2026-0"),
  dict(date="2026-09-25", promo="wwe", cat="event", official=True, who="CM Punk",
       hl="SmackDown tonight: CM Punk vs. Gunther vs. Finn Balor in MITB qualifier",
       dek="Tonight\\u2019s SmackDown in Indianapolis features a triple threat to fill the last men\\u2019s MITB spot, plus Trick Williams defends the United States Title against Baron Corbin in a steel cage and Charlotte Flair battles Giulia and Lash Legend for a women\\u2019s ladder match spot.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-09-25"),
  # =============== end week of September 21 - September 25, 2026 ===============
'''

GALLERY_BLOCK = '''  {"week":"2026-09-21","label":"Week of September 21, 2026","start":datetime.date(2026,9,21),"promos":{
     "WWE":[("Eod0YsUxGwQ","2026-09-21","Raw \\u00b7 Penta fights off The Judgment Day in Raw highlights from San Antonio"),("Rkr6Yw1WOrI","2026-09-21","Raw \\u00b7 Penta qualifies for Money in the Bank after Solo Sikoa\\u2019s abduction")],
     "AEW":[("ETANjtz_Rmg","2026-09-23","Dynamite \\u00b7 Persephone vs Hyan for the TBS Championship match highlights"),("4DrtpslLWTk","2026-09-23","Dynamite \\u00b7 Jon Moxley vs Dezmond Xavier match highlights"),("n682IQt55s4","2026-09-23","Dynamite \\u00b7 Cage and Cope, FTR and The Young Bucks preview All Out")],
     "NXT":[("jh8GHTPNcFE","2026-09-22","NXT \\u00b7 Full highlights from the Dusty Classic premiere on The CW"),("4Quvhy8Oo7M","2026-09-22","NXT \\u00b7 Top 10 NXT moments from the Dusty Classic episode")],
     "TNA":[("rWAbJEEBDhM","2026-09-24","iMPACT \\u00b7 Mustafa Ali defends International Title in a triple threat classic")]
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

patch("build/build_lorefeed.py", "DISPATCHES = [", DISPATCH_BLOCK, "WEEK OF SEPTEMBER 21 - SEPTEMBER 25, 2026")
patch("build/build_gallery.py", "WEEKS = [\n", GALLERY_BLOCK, '"week":"2026-09-21"')
print("done")
