#!/usr/bin/env python3
"""add_week_0831.py - open the week of Aug 31 - Sep 6, 2026 (partial: through Sep 1).

    WL_ROOT="$PWD" python3 build/add_week_0831.py

Idempotent. The gallery hub says "updated nightly" and renders a this-week-so-
far state by design, so opening the week two days in is the intended use, not
a compromise. Re-run later scripts/sessions APPEND further days via new
insert scripts; this one only opens the week.

ASSEMBLY DECISIONS (three research agents, one lane each):
 - The All In attendance story arrived from BOTH the AEW and the industry
   agent. Kept the industry version - it carries the 2023/24/25 comparables -
   and dropped the duplicate. One fact, one row.
 - Two agent-supplied htags ("business", "signings") are not in the rail's
   filter vocabulary (matches|titles|rivalries|roster) and were corrected.
 - The "Full NXT Heatwave highlights" video was EXCLUDED: oEmbed verified the
   ID but could not pin the upload inside Aug 31-Sep 1, and Heatwave belongs
   to LAST week's page. A video filed to the wrong week is worse than a
   missing video.
"""
import os

ROOT = os.environ.get("WL_ROOT", os.getcwd())

DISPATCH_BLOCK = '''
  # ================= WEEK OF AUGUST 31 - SEPTEMBER 6, 2026 (in progress) =================
  # Opened Sep 1 with Raw and the All In / Heatwave fallout. Fills nightly.

  # ---- WWE: Raw Aug 31, Rocket Arena, Cleveland ----
  dict(date="2026-08-31", promo="wwe", cat="event", official=True, who="Penta", home=True, htags="matches titles",
       hl="Penta defeats Rey Fenix to win the World Title number one contender tournament",
       dek="Penta pinned his brother with a Mexican Destroyer and challenges Roman Reigns for the World Heavyweight Championship September 14 in Mexico City.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/08/31/wwe-raw-results-8-31-kellers-report-on-roman-reigns-appearance-raquel-vs-sol-ruca-for-ic-title-penta-vs-rey-fenix-in-tournament-final-chad-gable-speaks/"),
  dict(date="2026-08-31", promo="wwe", cat="event", official=True, who="Roman Reigns", home=True, htags="rivalries",
       hl="Roman Reigns flattens LA Knight as Royce Keys and OTM ambush The Usos",
       dek="Keys, Bronco Nima and Lucien Price destroyed The Usos in the parking garage and Solo Sikoa was attacked. Reigns closed the night by Superman Punching Knight.",
       src="WrestleView", url="https://www.wrestleview.com/wwe-raw-results/391685-wwe-raw-results-august-31-2026-cleveland/"),
  dict(date="2026-08-31", promo="wwe", cat="title", official=True, who="Raquel Rodriguez",
       hl="Raquel Rodriguez retains the Womens Intercontinental Title against Sol Ruca",
       dek="Rodriguez hit the Tejana Bomb for the pin after Lyra Valkyria's interference cost Ruca the match in Cleveland.",
       src="WrestleView", url="https://www.wrestleview.com/wwe-raw-results/391685-wwe-raw-results-august-31-2026-cleveland/"),
  dict(date="2026-08-31", promo="wwe", cat="event", official=True, who="Dragon Lee",
       hl="Dragon Lee beats Ethan Page to earn an Intercontinental Title shot at Chad Gable",
       dek="Lee hit Operation Dragon to win and challenges Gable on the September 14 Raw in Mexico City.",
       src="PWTorch", url="https://www.pwtorch.com/site/2026/08/31/wwe-raw-results-8-31-kellers-report-on-roman-reigns-appearance-raquel-vs-sol-ruca-for-ic-title-penta-vs-rey-fenix-in-tournament-final-chad-gable-speaks/"),
  dict(date="2026-08-31", promo="wwe", cat="media", official=True, who="Quavo",
       hl="Quavo confirmed on Raw to open Sunday Nights Main Event in hometown Atlanta",
       dek="The rapper debuts an unreleased song September 6 at the special headlined by Oba Femi vs Bron Breakker and Cody Rhodes vs Randy Orton.",
       src="Wrestling Inc.", url="https://www.wrestlinginc.com/2248266/quavo-wwe-sunday-nights-main-event-perform-live/"),
  dict(date="2026-09-01", promo="wwe", cat="media", official=False, who="John Cena",
       hl="John Cena says WWE has finalized plans for the John Cena Classic",
       dek="Speaking at FanExpo Canada, Cena said all details of the NXT versus main roster tournament announced at Backlash are set but staying secret for now.",
       src="Blog of Doom", url="https://www.blogofdoom.com/2026/09/01/morning-daily-news-update-september-1-2026-john-cena-says-wwe-has-finalised-plans-for-john-cena-classic/"),

  # ---- AEW: All In fallout ----
  dict(date="2026-09-01", promo="aew", cat="signing", official=False, who="New Level", home=True, htags="roster",
       hl="New Level say their AEW contracts became official less than 24 hours before All In",
       dek="Kofi and Austin Creed told the Ariel Helwani Show their deals only solidified less than a day before the Wembley debut where they won the World Trios Titles.",
       src="Fightful", url="https://www.fightful.com/wrestling-news/new-level-say-they-officially-signed-their-aew-contracts-less-than-24-hours-before-aew-all-in"),
  dict(date="2026-08-31", promo="aew", cat="return", official=False, who="Britt Baker",
       hl="Britt Baker's All In return reportedly came together hours before the show",
       dek="Fightful Select reports Baker did not travel with the roster and arrived in London Sunday morning, after multiple return overtures during her nearly two-year absence.",
       src="Fightful", url="https://www.fightful.com/wrestling-news/details-about-britt-bakers-return-to-aew"),
  dict(date="2026-08-31", promo="aew", cat="roster", official=False, who="Mercedes Mone",
       hl="Mercedes Mone reveals a broken nose suffered early in her All In title win",
       dek="The new AEW Womens World Champion says she broke her nose early in the Willow Nightingale match and needed stitches, posting a bloodied photo captioned Heavy is the crown.",
       src="WrestleTalk", url="https://wrestletalk.com/news/aew-mercedes-mone-all-in-comment/"),
  dict(date="2026-08-31", promo="aew", cat="media", official=True, who="Will Ospreay",
       hl="Ospreay keeps one of Kenny Omega's side plates on the AEW World Title",
       dek="AEW footage of the new champion's side plate installation shows Ospreay retaining one of Omega's plates as a tribute to his predecessor.",
       src="411Mania", url="https://411mania.com/wrestling/will-ospreay-decides-to-retain-one-of-kenny-omegas-side-plates-on-aew-world-title-all-in-2026-triumph/"),

  # ---- NXT / TNA / RAF / industry ----
  dict(date="2026-09-01", promo="nxt", cat="event", official=True, who="Kelani Jordan", home=True, htags="matches",
       hl="NXT runs its Heatwave fallout show with new champion Kelani Jordan set to appear",
       dek="The live Performance Center episode features Nikkita Lyons vs Thea Hail and fallout from Heatwave's five title changes.",
       src="Pro Wrestling Dot Net", url="https://prowrestling.net/site/2026/09/01/nxt-tv-preview-tonights-nxt-heatwave-fallout-show/"),
  dict(date="2026-09-01", promo="tna", cat="event", official=True, who="Nic Nemeth",
       hl="TNA announces back to back September shows at San Antonio's Boeing Center",
       dek="Thursday Night iMPACT airs live from San Antonio September 24 and 25, with the Hardys, Nic Nemeth, Mustafa Ali and Leon Slater advertised.",
       src="TNA Wrestling", url="https://tnawrestling.com/news/tna-wrestling-returns-to-san-antonio-texas-backtoback-nights-of-actionpacked-pro-wrestling"),
  dict(date="2026-09-01", promo="raf", cat="event", official=False, who="Khamzat Chimaev", home=True, htags="rivalries",
       hl="Chimaev calls out four UFC middleweights days before the RAF Moscow match with Woodley",
       dek="Posting I'm ready, the Moscow headliner named Strickland, Du Plessis, Imavov and Borralho on X, and Borralho answered. Chimaev wrestles Tyron Woodley September 5.",
       src="Sherdog", url="https://www.sherdog.com/news/news/Khamzat-Chimaev-names-4-UFC-targets-Caio-Borralho-answers-the-call-202602"),
  dict(date="2026-09-01", promo="industry", cat="business", official=False, who="Tony Khan",
       hl="Brent Council data shows 41,102 turnstile attendance for AEW All In at Wembley",
       dek="Local government figures show 46,987 distributed tickets against Tony Khan's claim of close to 50,000. The count trails All In London 2023's 72,265 and 2024's 46,476 but tops All In Texas 2025's 21,973.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/09/01/aew-all-in-2026-records-41102-turnstile-count-attendance-according-to-local-government-in-london/"),
  dict(date="2026-09-01", promo="industry", cat="media", official=False, who="WWE",
       hl="Raw's August 24 Netflix episode draws 2.5 million global views, seventh on the weekly chart",
       dek="The show slipped from the prior week's 2.7 million views and sixth place finish on Netflix's most viewed weekly shows list.",
       src="Pro Wrestling Dot Net", url="https://prowrestling.net/site/2026/09/01/wwe-raw-on-netflix-viewership-how-did-the-show-featuring-the-usos-vs-la-knight-and-solo-sikoa-perform/"),
  dict(date="2026-09-01", promo="industry", cat="retirement", official=False, who="Carmella",
       hl="Carmella confirms she is retired from pro wrestling on her own podcast",
       dek="Leah Van Dale said I can't wrestle anymore, I'm retired. She has not wrestled since 2023 after the birth of her first child and drop foot complications.",
       src="POST Wrestling", url="https://www.postwrestling.com/2026/09/01/carmella-confirms-pro-wrestling-retirement/"),
  # =============== end week of August 31 - September 6, 2026 ===============
'''

GALLERY_BLOCK = '''  {"week":"2026-08-31","label":"Week of August 31, 2026","start":datetime.date(2026,8,31),"promos":{
     "WWE":[("LU0-WUBQNvI","2026-08-31","Raw \\u00b7 Full show highlights"),("gwdABPJQsNs","2026-08-31","Raw \\u00b7 Penta vs. Rey Fenix, No. 1 Contender's Match"),("zbqhZfSAF2w","2026-08-31","Raw \\u00b7 Roman Reigns Superman Punches LA Knight")],
     "AEW":[("s2NfvFpUCX8","2026-08-31","All In \\u00b7 Ospreay and Omega share a moment after Wembley")]
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

patch("build/build_lorefeed.py", "DISPATCHES = [", DISPATCH_BLOCK, "WEEK OF AUGUST 31 - SEPTEMBER 6, 2026")
patch("build/build_gallery.py", "WEEKS = [\n", GALLERY_BLOCK, '"week":"2026-08-31"')
print("done")
