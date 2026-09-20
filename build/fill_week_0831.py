#!/usr/bin/env python3
"""fill_week_0831.py - fill the week of Aug 31 - Sep 6, 2026 (Sep 2-6 backfill).

    WL_ROOT="$PWD" python3 build/fill_week_0831.py

Idempotent. add_week_0831.py OPENED this week with the Aug 31 Raw and the
Sep 1 fallout; the site then went unattended until Sep 20. This script fills
the rest of the week - Dynamite 9/2, iMPACT 9/3, SmackDown 9/4, Collision +
RAF Moscow 9/5, Sunday Night's Main Event and the NJPW weekend 9/5-9/6 - by
EXTENDING the existing 2026-08-31 gallery week in place and prepending the
new dispatches. Run BEFORE add_week_0907.py and add_week_0914.py.

ASSEMBLY DECISIONS (three research agents, one lane each, Sep 20 assembly):
 - home=True budget: the opener already carries FIVE home=True rows for this
   week, the cap. Every new row here ships home=False, including the SNME
   main event. The home rail takes the newest seven home rows site-wide, so
   after the 0907/0914 scripts run nothing from this week renders there
   anyway; the flag would be dead weight that breaks the 3-5 budget.
 - The SNME Orton-over-Rhodes row is still the week's lead (lead=True,
   mono="SNME") - lead and home are independent flags in the renderer.
 - SmackDown aired FRIDAY Sep 4, not Sep 5 as the gap brief guessed; all
   SmackDown rows and video tuples are dated 2026-09-04 per WWE.com.
 - Oba Femi vs Bron Breakker at SNME ended in a DQ WIN FOR FEMI when Bronson
   Reed returned with a chair - filed as Reed's return, not a Breakker win.
 - Andy "The Butcher" Williams: dated 2026-09-06 per TMZ/Wrestling Inc, and
   the dek describes the collapse without asserting which day it happened -
   Wrestling Inc's own copy is internally inconsistent about the day.
 - RAF Moscow: Snyder RETAINED (USA Wrestling + Wikipedia) - FloWrestling's
   "claims title" phrasing was the outlier and was not followed. The venue
   swap to Arena Mytishchi and the absent US stream are one media row.
 - Andrade finisher name (Destination Madrid vs The Message) and the MCMG
   opponents (Lethal Swirl vs The Swirl) are printed AS conflicts in the
   deks, per site policy: publish conflicts as conflicts.
 - ZERO gallery videos for TNA/NXT/RAF this week: NXT did not air in the
   Sep 2-6 window, TNA's hub points off-YouTube, and the only Chimaev-
   Woodley highlight belongs to a fan channel (oEmbed author "Olympic
   Wrestling", not RAF) - rejected. Zero verified beats one fake.
 - All 8 video IDs below oEmbed-verified: authors "WWE" (4) and
   "All Elite Wrestling" (4). Captions lead with SHOWNET show names;
   "Sunday Night's Main Event" maps to Peacock (added to SHOWNET today).
"""
import os

ROOT = os.environ.get("WL_ROOT", os.getcwd())

DISPATCH_BLOCK = '''
  # ============ WEEK OF AUGUST 31 - SEPTEMBER 6, 2026 - SEPT 2-6 FILL ============
  # Backfilled Sep 20 from the Sep 2-6 gap: Dynamite, iMPACT, SmackDown,
  # Collision, RAF Moscow, SNME, NJPW weekend. See build/fill_week_0831.py.

  # ---- WWE: SmackDown Sep 4 (Cleveland) + Sunday Night's Main Event Sep 6 (Atlanta) ----
  dict(date="2026-09-06", promo="wwe", cat="event", official=True, who="Randy Orton", lead=True, mono="SNME",
       hl="Randy Orton steals main event win over Cody Rhodes in Atlanta",
       dek="Orton low blows both Rhodes and the referee, then lands the RKO for the pin at State Farm Arena. Quavo opens the show with a live performance.",
       src="WWE.com", url="https://www.wwe.com/shows/snme/2026-09-06/results"),
  dict(date="2026-09-06", promo="wwe", cat="title", official=True, who="Trick Williams",
       hl="Trick Williams beats Baron Corbin to capture the United States Championship",
       dek="Lil Yachty survives a five minute Survive and Advance match to trigger the instant title shot. Williams counters End of Days and hits the Trick Shot to win.",
       src="WWE.com", url="https://www.wwe.com/shows/snme/2026-09-06/results"),
  dict(date="2026-09-06", promo="wwe", cat="return", official=True, who="Bronson Reed",
       hl="Bronson Reed returns and mauls Oba Femi to force disqualification finish",
       dek="Femi wins by DQ over Bron Breakker when Reed hits the ring with a steel chair. Reed follows with multiple Tsunamis as Breakker adds Super Spears.",
       src="WWE.com", url="https://www.wwe.com/shows/snme/2026-09-06/results"),
  dict(date="2026-09-04", promo="wwe", cat="event", official=True, who="CM Punk",
       hl="CM Punk survives Gargano and Zayn chaos to retain Undisputed WWE Title",
       dek="Punk pins Johnny Gargano with the GTS amid interference from Zayn, Owens, Gunther, Balor and LeRae. He then challenges Sami Zayn for Mexico City.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-09-04"),
  dict(date="2026-09-04", promo="wwe", cat="roster", official=True, who="Chelsea Green",
       hl="Chelsea Green cleared to return but must wear protective facemask",
       dek="Green is cleared from the orbital fracture suffered August 7, with a mandatory mask per WWE medical. She defends the Women's Title against Nia Jax next week in Mexico City.",
       src="WrestleZone", url="https://www.wrestlezone.com/news/1661119-chelsea-green-cleared-wwe-smackdown-catch-mask"),
  dict(date="2026-09-04", promo="wwe", cat="roster", official=True, who="Kyoki",
       hl="Kyoki makes SmackDown debut teaming with Shinsuke Nakamura as Bakusai",
       dek="The new duo beats The Miz and Kit Wilson in their first outing. Kyoki finishes with a Reverse Stunner.",
       src="WWE.com", url="https://www.wwe.com/shows/smackdown/2026-09-04"),

  # ---- AEW: Dynamite Sep 2 (Allen, TX) + Collision Sep 5 ----
  dict(date="2026-09-02", promo="aew", cat="title", official=True, who="Swerve Strickland",
       hl="Swerve Strickland and The New Level retain AEW World Trios Titles over The Rascalz",
       dek="Swerve hits the House Call on Dezmond Xavier and Kofi scores the pin at about 13 minutes on Dynamite in Allen, Texas.",
       src="Fightful", url="https://www.fightful.com/wrestling/aew-dynamite-results-9-2-2026-swerve-strickland-new-level-vs-rascalz-will-ospreay-mercedes-mone-more/"),
  dict(date="2026-09-02", promo="aew", cat="event", official=True, who="Mercedes Mone",
       hl="Thekla interrupts Mercedes Mone championship celebration and calls for a title match",
       dek="Mone, showing facial damage from the Willow Nightingale match, touts a fourth major title across different companies before Thekla crashes the party from the upper deck with a challenge.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/09/02/aew-dynamite-report-september-2-2026-allen-tex-at-credit-union-of-texas-event-center-aired-on-tbs-hbo-max-report-by-wade-keller-pwtorch-editor-commentators-excalibur-tony-schiavone/"),
  dict(date="2026-09-02", promo="aew", cat="event", official=True, who="Jon Moxley",
       hl="Jon Moxley challenges Will Ospreay for the AEW World Championship at All Out",
       dek="Moxley chokes out AR Fox with the Death Rider submission in a Continental eliminator, and the Ospreay title match is set for All Out on September 26 in Chicago.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/09/02/aew-dynamite-report-september-2-2026-allen-tex-at-credit-union-of-texas-event-center-aired-on-tbs-hbo-max-report-by-wade-keller-pwtorch-editor-commentators-excalibur-tony-schiavone/"),
  dict(date="2026-09-05", promo="aew", cat="title", official=True, who="Andrade El Idolo",
       hl="Andrade El Idolo turns back Gabe Kidd to keep the AEW National Championship",
       dek="Andrade retains on Collision and vows weekly defenses; Wrestling Inc calls the finisher the Destination Madrid while PWMania calls it The Message.",
       src="Wrestling Inc", url="https://www.wrestlinginc.com/2251732/aew-collision-september-5-2026-results/"),
  dict(date="2026-09-05", promo="aew", cat="roster", official=True, who="Motor City Machine Guns",
       hl="Motor City Machine Guns take their first AEW in-ring win on Saturday Collision",
       dek="Chris Sabin and Alex Shelley finish with Skull and Bones in their AEW in-ring debut; Wrestling Inc lists the opponents as Jay Lethal's Lethal Swirl while PWMania lists The Swirl's Blake Christian and Lee Johnson.",
       src="Wrestling Inc", url="https://www.wrestlinginc.com/2251732/aew-collision-september-5-2026-results/"),
  dict(date="2026-09-05", promo="aew", cat="media", official=False, who="AEW",
       hl="AEW Dynamite viewership ticks up to 796,000 viewers for post All In episode",
       dek="The September 2 Dynamite drew 796,000 viewers with a 0.21 in P18-49, up from 792,000 and 0.18 the prior week per Ringside News.",
       src="Ringside News", url="https://www.ringsidenews.com/aew-dynamite-viewership-sees-slight-increase-september-2-2026"),

  # ---- RAF Moscow Sep 5 / TNA Sep 3 / NJPW weekend / industry ----
  dict(date="2026-09-05", promo="raf", cat="event", official=True, who="Khamzat Chimaev",
       hl="Chimaev pins Woodley in 94 seconds as RAF Moscow card goes ahead",
       dek="Khamzat Chimaev scored push-out points, reversed a single-leg and pinned Tyron Woodley at 1:34 of the catchweight main event. Abdulrashid Sadulaev edged Zac Braunagel 8-6 and Jordan Burroughs teched Magomed Kurbanaliev 10-0.",
       src="MiddleEasy", url="https://middleeasy.com/mma-news/khamzat-chimaev-tyron-woodley-raf-moscow-pin-highlights"),
  dict(date="2026-09-05", promo="raf", cat="title", official=True, who="Kyle Snyder",
       hl="Snyder, Dake and Blades all retain RAF titles on Moscow card",
       dek="Kyle Snyder beat Akhmed Tazhudinov 11-5 to keep the light heavyweight title, his second win over Tazhudinov. Kyle Dake edged Mahamedkhabib Kadzimahamedau 7-6 in his cruiserweight defense and Kennedy Blades teched Vusala Parfianovich 10-0.",
       src="USA Wrestling", url="https://www.themat.com/news/2026/september/05/snyder-dake-blades-defend-titles-americans-roll-at-raf-moscow"),
  dict(date="2026-09-03", promo="raf", cat="media", official=True, who="Real American Freestyle",
       hl="RAF Moscow swaps venues two days out as Fox Nation declines to stream card",
       dek="RAF moved the card from VTB Arena, run by a subsidiary of sanctioned VTB Bank, to Arena Mytishchi to sidestep U.S. sanctions exposure. Fox Nation had declined to stream the event, and it ultimately aired with no U.S. streaming option.",
       src="Yahoo Sports", url="https://sports.yahoo.com/articles/sanctions-avoided-raf-moscow-abruptly-210000851.html"),
  dict(date="2026-09-03", promo="tna", cat="event", official=True, who="Matt Hardy",
       hl="Agent Zero wrecks Miguel vs Hotch as Hardy and Nemeth war escalates on iMPACT",
       dek="Trey Miguel vs Jason Hotch ended in a 19-minute no contest when Agent Zero attacked both men in Brampton. Matt Hardy blamed the Nemeths for the attack on Jeff, and Santino booked Hardy vs Nic Nemeth in a no-DQ match. Dutch beat BDE and KC Navarro won an X Division scramble qualifier.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/09/03/tna-impact-tv-results-9-3-hotch-vs-miguel-hartwell-hudson-vs-brookside-serrano-bde-vs-dutch/"),
  dict(date="2026-09-05", promo="njpw", cat="event", official=True, who="Shingo Takagi",
       hl="Takagi and Cobb topple United Empire as Road to Destruction opens in Tochigi",
       dek="Shingo Takagi and Jeff Cobb beat United Empire with the Burning Dragon at Light Cube Utsunomiya before 903 fans. NEVER Openweight champion Aaron Wolf tapped Hartley Jackson in six-man action and Chaos took the eight-man main event.",
       src="PWMania", url="https://www.pwmania.com/njpw-road-to-destruction-night-1-results-september-5-2026"),
  dict(date="2026-09-06", promo="njpw", cat="event", official=True, who="Yuji Nagata",
       hl="Nagata and Most Violent Players win Blue Justice XIX main event in Togane",
       dek="Yuji Nagata teamed with Togi Makabe and Toru Yano to beat Unbound Company in 15:24 before 1,258 fans at Togane Arena. Jeff Cobb pinned Zane Jay with the Tour of the Islands and House of Torture took the six-man tag.",
       src="PWMania", url="https://www.pwmania.com/njpw-blue-justice-xix-results-september-6-2026"),
  dict(date="2026-09-06", promo="industry", cat="passing", official=True, who="Andy Williams",
       hl="Andy The Butcher Williams, Every Time I Die guitarist and AEW alum, dies at 48",
       dek="Williams suffered a medical emergency and collapsed after a Butcher and Blade tag match with Braxton Sutter at an Enjoy Wrestling event in Millvale, Pennsylvania; he received CPR at ringside and the show was canceled. He co-founded Every Time I Die in 1998 and debuted in AEW in 2019.",
       src="Wrestling Inc", url="https://www.wrestlinginc.com/2251808/butcher-andy-williams-dead-aew-star-age-48/"),
  # ============ end Sept 2-6 fill, week of August 31 - September 6, 2026 ============
'''

WWE_TUPLES = ''',("x1HDr0olLQM","2026-09-04","SmackDown \\u00b7 Full SmackDown highlights: Sept. 4, 2026"),("pv64CXrsrMo","2026-09-04","SmackDown \\u00b7 FULL MATCH: CM Punk vs. Johnny Gargano for the WWE Title"),("03j8KkW7r1w","2026-09-06","Sunday Night's Main Event \\u00b7 Full show highlights from State Farm Arena in Atlanta"),("bzR8FA4nPl4","2026-09-06","Sunday Night's Main Event \\u00b7 Cody Rhodes vs. Randy Orton main event highlights")'''

AEW_TUPLES = ''',("VUGjamw-kQM","2026-09-02","Dynamite \\u00b7 Jon Moxley vs AR Fox match highlights"),("XPZrndkFTi0","2026-09-02","Dynamite \\u00b7 Austin Creed and Kofi's first match on Dynamite"),("cAOPO1nRYFk","2026-09-02","Dynamite \\u00b7 Cope calls for chairs, tables and ladders for the Tag Team Titles at All Out"),("DTt20FexAik","2026-09-05","Collision \\u00b7 Andrade El Idolo vs Gabe Kidd for the AEW National Championship")'''

def patch(path, anchor, block, marker):
    full = os.path.join(ROOT, path)
    s = open(full, encoding="utf-8").read()
    if marker in s:
        print("  already present, skipping:", path); return
    if anchor not in s or s.count(anchor) != 1:
        raise SystemExit("ANCHOR NOT FOUND (or not unique) in %s: %r" % (path, anchor[:60]))
    open(full, "w", encoding="utf-8").write(s.replace(anchor, anchor + block, 1))
    print("  inserted into", path)

patch("build/build_lorefeed.py", "DISPATCHES = [", DISPATCH_BLOCK, "SEPT 2-6 FILL")
# EXTEND the existing 2026-08-31 gallery week in place: append tuples inside
# the WWE and AEW lists that add_week_0831.py created.
patch("build/build_gallery.py", 'Superman Punches LA Knight")', WWE_TUPLES, "x1HDr0olLQM")
patch("build/build_gallery.py", 'share a moment after Wembley")', AEW_TUPLES, "VUGjamw-kQM")
print("done")
