#!/usr/bin/env python3
"""Real American Freestyle generator — the RAF section of Wrestle Lore.
ONE source (EVENTS + CLIPS) emits, all in sync:
  /promotions/raf/                 -> the RAF hub: what it is, champions, every event
  /promotions/raf/<slug>/          -> one page per event (full card, results, video, schema)
  css/site.css                     -> the .raf-* styles (idempotent block, scoped under .raf)
  sitemap.xml                      -> +RAF URLs
Then run `python3 build/apply_shell.py` to stamp nav + footer.
To add an event: append ONE dict to EVENTS, rerun this, then apply_shell.py.
ROOT overridable: WL_ROOT=/path python3 build/build_raf.py
EVERY result here is sourced. Every clip id is oEmbed-verified against the official channel.
"""
import os, re, datetime, html as _html

ROOT = os.environ.get("WL_ROOT", "/root/wwe")
BASE = "https://wrestlelore.com"
TODAY = datetime.date.fromisoformat(os.environ["WL_TODAY"]) if os.environ.get("WL_TODAY") else datetime.date.today()

def esc(s): return _html.escape(str(s), quote=True) if s is not None else ""

# ------------------------------------------------------------------ EVENTS
# bout: (wc, a, b, winner, method, title, change)  winner=None => not yet wrestled
EVENTS = [
 dict(slug="raf-14", name="RAF 14", date="2026-10-03", venue="Fontainebleau Las Vegas", city="Las Vegas, NV",
      stream="Fox Nation", tag="Tsarukyan vs. Danis", upcoming=True,
      src="Real American Freestyle", url="https://www.realamericanfreestyle.com/events/raf14",
      note="RAF's Las Vegas debut, and three of the four announced bouts carry a championship. "
           "Tsarukyan defends a wrestling title two weeks after a UFC fight.",
      bouts=[
        ("Middleweight","Arman Tsarukyan","Dillon Danis",None,None,"Middleweight Crossover Championship",None),
        ("Women's Strawweight","Lucia Yepez","Sarah Hildebrandt",None,None,"Women's Strawweight Championship",None),
        ("Lightweight","Jordan Oliver","Ridge Lovett",None,None,"Lightweight Championship",None),
        ("Cruiserweight","Alexander Shlemenko","Michael Page",None,None,None,None),
      ]),
 dict(slug="raf-13", name="RAF 13", date="2026-09-19", venue="Watsco Center", city="Coral Gables, FL",
      stream="Fox Nation", tag="Covington vs. Muhammad", upcoming=True,
      src="Real American Freestyle", url="https://www.realamericanfreestyle.com/events/raf13",
      note="A double title card in Covington's home market, built on a grudge that started at the RAF 11 press conference.",
      bouts=[
        ("Cruiserweight","Colby Covington","Belal Muhammad",None,None,"Cruiserweight Crossover Championship",None),
        ("Catchweight","Real Tarzan","Larry Wheels",None,None,None,None),
        ("Heavyweight","Wyatt Hendrickson","Greg Kerkvliet",None,None,"Heavyweight Championship",None),
        ("Catchweight","Luke Rockhold","Joe Pyfer",None,None,None,None),
        ("Welterweight","Michael Caliendo","Timur Bizhoev",None,None,None,None),
        ("Lightweight","Haji Aliyev","Jacori Teemer",None,None,None,None),
        ("Cruiserweight","Georgios Kougioumtsidis","Chance Marsteller",None,None,None,None),
      ]),
 dict(slug="raf-12", name="RAF 12", date="2026-08-22", venue="Rocket Arena", city="Cleveland, OH",
      stream="Fox Nation", tag="Dvalishvili vs. Cejudo 2", upcoming=True,
      src="Real American Freestyle", url="https://www.realamericanfreestyle.com/events/raf12",
      note="RAF's one year anniversary card, back in the city where the league debuted. Covington vs. Muhammad was originally the main event and moved to RAF 13, and Dvalishvili vs. Cejudo replaced it. Kennedy Blades defends against Diana Avsaragova, not Reese Larramendy as first announced.",
      bouts=[
        ("Lightweight","Merab Dvalishvili","Henry Cejudo",None,None,"Lightweight Crossover Championship, inaugural",None),
        ("Catchweight","Jordan Burroughs","Sean Brady",None,None,None,None),
        ("Heavyweight","Gable Steveson","Anthony Cassioppi",None,None,None,None),
        ("Middleweight","Evan Wick","Jason Nolf",None,None,"Middleweight Championship, vacant",None),
        ("Welterweight","David Carr","Tajmuraz Salkazanov",None,None,"Welterweight Championship",None),
        ("Catchweight","Bo Nickal","Max McEnelly",None,None,None,None),
        ("Women's Middleweight","Kennedy Blades","Diana Avsaragova",None,None,"Women's Middleweight Championship",None),
        ("Cruiserweight","Tyron Woodley","Joaquin Buckley",None,None,None,None),
        ("Featherweight","Vladimer Khinchegashvili","Jesse Mendez",None,None,None,None),
        ("Featherweight","Johnni DiJulius","Asu Almabayev",None,None,None,None),
        ("Middleweight","Mahamedkhabib Kadzimahamedau","Will Lewan",None,None,None,None),
        ("Bantamweight","Masanosuke Ono","Ben Davino",None,None,None,None),
      ]),
 dict(slug="raf-11", name="RAF 11", date="2026-07-18", venue="UW-Milwaukee Panther Arena", city="Milwaukee, WI",
      stream="Fox Nation", tag="Tsarukyan vs. Covington",
      src="USA Wrestling", url="https://www.themat.com/news/2026/july/21/ben-askren-concludes-historic-wrestling-career-adeline-gray-and-trent-hidlay-pick-up-victories-at-raf11",
      note="Ben Askren closed his career here, leaving his boots on the mat after a comeback from a double lung transplant. The main event score is filed as 5-3, which is what RAF's own recap and most of the press ran. RAF's event scoreboard and USA Wrestling both published 5-2, which was the score at the end of the second period.",
      bouts=[
        ("Cruiserweight","Arman Tsarukyan","Colby Covington","Colby Covington","dec 5-3","Cruiserweight Crossover Championship",True),
        ("Cruiserweight","Ben Askren","Belal Muhammad","Belal Muhammad","dec 6-3",None,False),
        ("Catchweight","Clay Guida","Frankie Edgar","Frankie Edgar","dec 9-1",None,False),
        ("Middleweight","Keegan O'Toole","Christopher Minto","Keegan O'Toole","dec 14-9",None,False),
        ("Women's Cruiserweight","Adeline Gray","Skylar Grote","Adeline Gray","dec 5-2",None,False),
        ("Bantamweight","Arsen Harutyunyan","Ben Davino","Arsen Harutyunyan","dec 6-5",None,False),
        ("Light Heavyweight","Trent Hidlay","Magomedkhan Magomedov","Trent Hidlay","tech fall 10-0",None,False),
        ("Cruiserweight","Aeoden Sinclair","Magomed Ramazanov","Magomed Ramazanov","dec 6-3",None,False),
        ("Light Heavyweight","Pat Downey","Zac Braunagel","Zac Braunagel","tech fall 12-2",None,False),
        ("Heavyweight","Anthony Cassioppi","Mostafa Elders","Anthony Cassioppi","dec 6-2",None,False),
        ("Welterweight","Michael Caliendo","Mirzo Khayitov","Michael Caliendo","dec 9-2",None,False),
        ("Women's Strawweight","Lucia Yepez","Felicity Taylor","Lucia Yepez","tech fall 10-0","Women's Strawweight Championship",False),
      ]),
 dict(slug="raf-georgia", name="RAF Georgia", date="2026-07-11", venue="Tbilisi Arena", city="Tbilisi, Georgia",
      stream="Fox Nation", tag="Dvalishvili vs. Cejudo",
      src="USA Wrestling", url="https://www.themat.com/news/2026/july/11/snyder-pins-sadulaev-dake-and-maroulis-also-retain-belts-at-raf-georgia",
      note="RAF's first card outside the United States, in Dvalishvili's home country.",
      bouts=[
        ("Lightweight","Merab Dvalishvili","Henry Cejudo","Merab Dvalishvili","dec 11-8",None,False),
        ("Light Heavyweight","Kyle Snyder","Abdulrashid Sadulaev","Kyle Snyder","fall 4:25","Light Heavyweight Championship",False),
        ("Middleweight","Arman Tsarukyan","Kuat Khamitov","Arman Tsarukyan","tech fall 11-0",None,False),
        ("Cruiserweight","Kyle Dake","Vladimeri Gamkrelidze","Kyle Dake","dec 2-0","Cruiserweight Championship",False),
        ("Heavyweight","Geno Petriashvili","Jake Varner","Geno Petriashvili","tech fall 10-0",None,False),
        ("Women's Bantamweight","Helen Maroulis","Anhelina Lysak","Helen Maroulis","dec 8-2","Women's Bantamweight Championship",False),
        ("Heavyweight","Zach Elam","Givi Matcharashvili","Givi Matcharashvili","dec 7-3",None,False),
        ("Featherweight","Vladimer Khinchegashvili","Conor Beebe","Vladimer Khinchegashvili","tech fall 11-0",None,False),
        ("Women's Bantamweight","Anastasia Nichita","Sangeeta Phogat","Anastasia Nichita","dec 7-6",None,False),
        ("Lightweight","Ernazar Akmataliev","Zain Retherford","Ernazar Akmataliev","dec 3-3 on criteria",None,False),
        ("Catchweight","Jarrett Jacques","Razambek Zhamalov","Razambek Zhamalov","dec 3-2",None,False),
        ("Featherweight","Brock Hardy","Alibeg Alibegov","Brock Hardy","tech fall 13-2",None,False),
      ]),
 dict(slug="raf-10", name="RAF 10", date="2026-06-13", venue="Chaifetz Arena", city="St. Louis, MO",
      stream="Fox Nation", tag="Chimaev vs. Danis",
      src="USA Wrestling", url="https://www.themat.com/news/2026/june/15/austin-desanto-defends-bantamweight-title-aaron-pico-keegan-o-toole-and-andrew-alirez-earn-statement-victories-at-raf-10",
      note="Khamzat Chimaev's freestyle debut lasted 41 seconds and ended in a brawl.",
      bouts=[
        ("Catchweight","Khamzat Chimaev","Dillon Danis","Khamzat Chimaev","fall 0:41",None,False),
        ("Middleweight","Arman Tsarukyan","Tony Ferguson","Arman Tsarukyan","tech fall 10-0",None,False),
        ("Lightweight","Aaron Pico","Lance Palmer","Aaron Pico","tech fall 12-1",None,False),
        ("Women's Strawweight","Lucia Yepez","Kendra Ryan","Lucia Yepez","tech fall 11-1","Women's Strawweight Championship",True),
        ("Bantamweight","Austin DeSanto","Reineri Ortega","Austin DeSanto","dec 2-1","Bantamweight Championship",False),
        ("Light Heavyweight","Rizabek Aitmukhan","Hayden Zillmer","Rizabek Aitmukhan","dec 6-4",None,False),
        ("Lightweight","Sebastian Rivera","Haji Aliyev","Sebastian Rivera","dec 9-5",None,False),
        ("Middleweight","Keegan O'Toole","Bekzod Abdurakhmonov","Keegan O'Toole","dec 10-6",None,False),
        ("Featherweight","Andrew Alirez","Jaydin Eierman","Andrew Alirez","dec 5-3",None,False),
        ("Heavyweight","Shamil Sharipov","Yonger Bastida","Shamil Sharipov","dec 5-3",None,False),
        ("Bantamweight","Arsen Harutyunyan","Caleb Smith","Arsen Harutyunyan","tech fall 14-4",None,False),
      ]),
 dict(slug="raf-09", name="RAF 09", date="2026-05-30", venue="College Park Center", city="Arlington, TX",
      stream="Fox Nation", tag="Steveson vs. Romanov",
      src="USA Wrestling", url="https://www.themat.com/news/2026/may/31/steveson-dominates-in-raf-09-main-event-snyder-woods-earn-title-belts",
      note="Gable Steveson's first freestyle match since 2023, and his RAF debut.",
      bouts=[
        ("Heavyweight","Gable Steveson","Alexandr Romanov","Gable Steveson","tech fall 10-0",None,False),
        ("Catchweight","Colby Covington","Chris Weidman","Colby Covington","dec 5-4",None,False),
        ("Light Heavyweight","Kyle Snyder","Givi Matcharashvili","Kyle Snyder","tech fall 10-0","Light Heavyweight Championship",False),
        ("Lightweight","Merab Dvalishvili","Frankie Edgar","Merab Dvalishvili","tech fall 12-1",None,False),
        ("Featherweight","Real Woods","Ibragim Ilyasov","Real Woods","fall 2:11","Featherweight Championship",True),
        ("Middleweight","Jason Nolf","Christopher Minto","Jason Nolf","dec 10-5",None,False),
        ("Middleweight","Arman Tsarukyan","Keelon Jimison","Arman Tsarukyan","tech fall 16-5",None,False),
        ("Cruiserweight","Parker Keckeisen","Georgios Kougioumtsidis","Parker Keckeisen","dec 8-5",None,False),
        ("Lightweight","Zain Retherford","Antrell Taylor","Zain Retherford","dec 8-0",None,False),
        ("Lightweight","Ridge Lovett","Bajrang Punia","Ridge Lovett","dec 13-8",None,False),
        ("Women's Catchweight","Lucia Yepez","Cameron Guerin","Lucia Yepez","tech fall 10-0",None,False),
      ]),
 dict(slug="raf-08", name="RAF 08", date="2026-04-18", venue="Liacouras Center", city="Philadelphia, PA",
      stream="Fox Nation", tag="Tsarukyan vs. Faber",
      src="USA Wrestling", url="https://www.themat.com/news/2026/april/19/maroulis-snyder-retain-belts-valencia-woods-notch-wins-at-raf-08",
      note="Khamzat Chimaev's signing was announced on the broadcast.",
      bouts=[
        ("Middleweight","Arman Tsarukyan","Urijah Faber","Arman Tsarukyan","tech fall 13-1",None,False),
        ("Light Heavyweight","Kyle Snyder","Rizabek Aitmukhan","Kyle Snyder","dec 12-6","Light Heavyweight Championship",False),
        ("Women's Bantamweight","Helen Maroulis","Alexis Janiak","Helen Maroulis","tech fall 10-0","Women's Bantamweight Championship",False),
        ("Heavyweight","Shamil Sharipov","Anthony Cassioppi","Shamil Sharipov","fall 1:45",None,False),
        ("Cruiserweight","Zahid Valencia","Aeoden Sinclair","Zahid Valencia","dec 8-2",None,False),
        ("Featherweight","Real Woods","Anthony Ashnault","Real Woods","dec 7-2",None,False),
        ("Middleweight","Jason Nolf","Joey Blaze","Jason Nolf","dec 11-2",None,False),
        ("Featherweight","Vladimer Khinchegashvili","Johnni DiJulius","Vladimer Khinchegashvili","dec 8-5",None,False),
        ("Lightweight","Lance Palmer","Cayden Henschel","Lance Palmer","dec 3-2",None,False),
        ("Featherweight","Jordan Oliver","Mike Van Brill","Jordan Oliver","dec 5-0",None,False),
        ("Bantamweight","Lucas Byrd","Darian Cruz","Lucas Byrd","dec 2-2 on criteria",None,False),
      ]),
 dict(slug="raf-07", name="RAF 07", date="2026-03-28", venue="Yuengling Center", city="Tampa, FL",
      stream="Fox Nation", tag="Tsarukyan vs. Poullas 2",
      src="USA Wrestling", url="https://www.themat.com/news/2026/march/29/snyder-edges-tazhudinov-in-battle-of-olympic-champions-at-raf-07-dake-blades-hendrickson-retain-belts",
      note="A high school senior, Bo Bassett, beat a 2016 Olympic champion on this card.",
      bouts=[
        ("Middleweight","Arman Tsarukyan","Georgio Poullas","Arman Tsarukyan","dec 9-3",None,False),
        ("Cruiserweight","Colby Covington","Dillon Danis","Colby Covington","tech fall 14-4",None,False),
        ("Cruiserweight","Kyle Dake","Parker Keckeisen","Kyle Dake","dec 7-1","Cruiserweight Championship",False),
        ("Light Heavyweight","Kyle Snyder","Akhmed Tazhudinov","Kyle Snyder","dec 3-3 on criteria","Light Heavyweight Championship",True),
        ("Women's Middleweight","Kennedy Blades","Milana Dudieva","Kennedy Blades","tech fall 11-0","Women's Middleweight Championship",False),
        ("Heavyweight","Wyatt Hendrickson","Trent Hillger","Wyatt Hendrickson","dec 6-2","Heavyweight Championship",False),
        ("Featherweight","Johnni DiJulius","Conor Beebe","Johnni DiJulius","dec 9-6",None,False),
        ("Light Heavyweight","Trent Hidlay","Pat Downey","Trent Hidlay","tech fall 12-0",None,False),
        ("Middleweight","Jason Nolf","David Mistulov","Jason Nolf","tech fall 10-0",None,False),
        ("Cruiserweight","Aeoden Sinclair","Khidir Saipudinov","Aeoden Sinclair","dec 9-4",None,False),
        ("Featherweight","Bo Bassett","Vladimer Khinchegashvili","Bo Bassett","tech fall 13-3",None,False),
      ]),
 dict(slug="raf-06", name="RAF 06", date="2026-02-28", venue="Mullett Arena", city="Tempe, AZ",
      stream="Fox Nation", tag="Cejudo vs. Faber",
      src="USA Wrestling", url="https://www.themat.com/news/2026/march/02/olympic-champ-cejudo-returns-carr-defends-belt-at-raf-06",
      note="A post-match brawl between Tsarukyan and Poullas set up the RAF 07 rematch. The score of that match is filed as disputed: RAF published 5-4, most press reported 5-3, MMA Mania had 6-4 and USA Wrestling had 5-2.",
      bouts=[
        ("Lightweight","Henry Cejudo","Urijah Faber","Henry Cejudo","tech fall 11-0",None,False),
        ("Middleweight","Arman Tsarukyan","Georgio Poullas","Arman Tsarukyan","decision, score disputed",None,False),
        ("Middleweight","Aljamain Sterling","Benson Henderson","Aljamain Sterling","tech fall",None,False),
        ("Welterweight","David Carr","Bubba Jenkins","David Carr","tech fall 13-2","Welterweight Championship",False),
        ("Featherweight","Andrew Alirez","Bryce Meredith","Andrew Alirez","tech fall 13-2",None,False),
        ("Light Heavyweight","Givi Matcharashvili","Stephen Buchanan","Givi Matcharashvili","dec 3-3 on criteria",None,False),
        ("Women's Strawweight","Lucia Yepez","Everest Leydecker","Lucia Yepez","dec 10-3",None,False),
        ("Middleweight","Tajmuraz Salkazanov","Keegan O'Toole","Tajmuraz Salkazanov","dec 9-0",None,False),
        ("Middleweight","Evan Wick","Mahamedkhabib Kadzimahamedau","Evan Wick","tech fall 13-2",None,False),
        ("Cruiserweight","Zahid Valencia","Mahmoud Fawzy Sebie","Zahid Valencia","tech fall 10-0",None,False),
        ("Welterweight","Keelon Jimison","Clay Guida","Keelon Jimison","tech fall 13-2",None,False),
        ("Featherweight","Jordan Oliver","Beau Bartlett","Jordan Oliver","dec 5-3",None,False),
      ]),
 dict(slug="raf-05", name="RAF 05", date="2026-01-10", venue="Amerant Bank Arena", city="Sunrise, FL",
      stream="Fox Nation", tag="Covington vs. Rockhold",
      src="USA Wrestling", url="https://www.themat.com/news/2026/january/11/dake-outlasts-kadzimahamedau-to-retain-cruiserweight-title-at-raf05",
      note="Fox Nation's highest single day of subscriber sign-ups in more than a year.",
      bouts=[
        ("Cruiserweight","Colby Covington","Luke Rockhold","Colby Covington","tech fall 12-0",None,False),
        ("Cruiserweight","Kyle Dake","Mahamedkhabib Kadzimahamedau","Kyle Dake","dec 10-7","Cruiserweight Championship",False),
        ("Lightweight","Arman Tsarukyan","Lance Palmer","Arman Tsarukyan","tech fall 10-0",None,False),
        ("Featherweight","Jordan Oliver","Real Woods","Jordan Oliver","dec 3-3 on criteria",None,False),
        ("Light Heavyweight","Stephen Buchanan","Yoel Romero","Stephen Buchanan","tech fall 10-0",None,False),
        ("Cruiserweight","Zahid Valencia","Nate Jackson","Zahid Valencia","dec 4-0",None,False),
        ("Bantamweight","Austin DeSanto","Nathan Tomasello","Austin DeSanto","tech fall 11-1","Bantamweight Championship",True),
        ("Featherweight","Bo Bassett","Cayden Henschel","Bo Bassett","tech fall 14-4",None,False),
        ("Heavyweight","Mostafa Elders","Steve Mocco","Mostafa Elders","dec 6-1",None,False),
        ("Featherweight","Johnni DiJulius","Pat Lugo","Johnni DiJulius","tech fall 11-0",None,False),
        ("Open","Georgio Poullas","Keelon Jimison","Georgio Poullas","tech fall 11-1",None,False),
      ]),
 dict(slug="raf-04", name="RAF 04", date="2025-12-20", venue="Fishers Event Center", city="Fishers, IN",
      stream="Fox Nation", tag="Hendrickson vs. Parris",
      src="USA Wrestling", url="https://www.themat.com/news/2025/december/21/hendrickson-tops-parris-blades-carr-defend-titles-hamiti-romero-earn-belts-at-raf-04",
      note="Three championships were decided on a nine bout card.",
      bouts=[
        ("Heavyweight","Wyatt Hendrickson","Mason Parris","Wyatt Hendrickson","tech fall 13-2","Heavyweight Championship",False),
        ("Light Heavyweight","Yoel Romero","Pat Downey","Yoel Romero","tech fall 10-0","Interim Light Heavyweight Championship",True),
        ("Catchweight","David Carr","Belal Muhammad","David Carr","tech fall 10-0","Welterweight Championship",False),
        ("Women's Middleweight","Kennedy Blades","Alara Boyd","Kennedy Blades","tech fall 10-0","Women's Middleweight Championship",False),
        ("Cruiserweight","Mahamedkhabib Kadzimahamedau","Dustin Plott","Mahamedkhabib Kadzimahamedau","dec 11-7",None,False),
        ("Middleweight","Dean Hamiti","Evan Wick","Dean Hamiti","fall","Middleweight Championship",True),
        ("Cruiserweight","Parker Keckeisen","Zahid Valencia","Parker Keckeisen","dec 10-2",None,False),
        ("Light Heavyweight","Trent Hidlay","Jacob Cardenas","Trent Hidlay","dec 5-3",None,False),
        ("Welterweight","Jason Nolf","Andy Varela","Jason Nolf","tech fall 10-0",None,False),
      ]),
 dict(slug="raf-03", name="RAF 03", date="2025-11-29", venue="Wintrust Arena", city="Chicago, IL",
      stream="Fox Nation", tag="Mendes vs. Chandler",
      src="USA Wrestling", url="https://www.themat.com/news/2025/november/30/blades-oliver-earn-championship-belts-lee-upset-at-raf-03-in-chicago",
      note="RAF's first high school competitor, Bo Bassett, won by fall in a minute.",
      bouts=[
        ("Middleweight","Michael Chandler","Chad Mendes","Michael Chandler","dec 4-1",None,False),
        ("Women's Featherweight","Kennedy Blades","Alejandra Rivera","Kennedy Blades","tech fall 11-0","Women's Featherweight Championship",True),
        ("Heavyweight","Akhmed Tazhudinov","Anthony Cassioppi","Akhmed Tazhudinov","fall 3:39",None,False),
        ("Bantamweight","Andrii Yatsenko","Spencer Lee","Andrii Yatsenko","fall 5:59",None,False),
        ("Lightweight","Austin Gomez","Austin O'Connor","Austin Gomez","dec 9-1",None,False),
        ("Featherweight","Jordan Oliver","Real Woods","Jordan Oliver","dec 2-2 on criteria","Featherweight Championship",True),
        ("Catchweight","Cayden Henschel","Clay Guida","Cayden Henschel","tech fall 11-0",None,False),
        ("Light Heavyweight","Pat Downey","Joaquin Buckley","Pat Downey","tech fall 12-0",None,False),
        ("Women's Featherweight","Alexis Gomez","Bella Mir","Alexis Gomez","dec 7-3",None,False),
        ("Featherweight","Bo Bassett","Darrion Caldwell","Bo Bassett","fall 1:00",None,False),
      ]),
 dict(slug="raf-02", name="RAF 02", date="2025-10-25", venue="Bryce Jordan Center", city="State College, PA",
      stream="Fox Nation", tag="Dake vs. Makoev",
      src="USA Wrestling", url="https://www.themat.com/news/2025/october/26/olympic-champions-maroulis-varner-among-raf-02-winners-at-penn-state",
      note="Jake Varner wrestled his first match since 2018.",
      bouts=[
        ("Cruiserweight","Kyle Dake","Boris Makoev","Kyle Dake","dec 7-1","Cruiserweight Championship",False),
        ("Women's Bantamweight","Helen Maroulis","Samantha Stewart","Helen Maroulis","dec 6-0","Women's Bantamweight Championship",True),
        ("Bantamweight","Nathan Tomasello","Matt Ramos","Nathan Tomasello","dec 5-3","Bantamweight Championship",False),
        ("Welterweight","David Carr","Amr Hussein","David Carr","tech fall 18-6","Welterweight Championship",True),
        ("Heavyweight","Jake Varner","Patrick Downey","Jake Varner","dec 5-1",None,False),
        ("Cruiserweight","Nate Jackson","Carter Starocci","Nate Jackson","dec 7-2",None,False),
        ("Open","Cayden Henschel","Keelon Jimison","Cayden Henschel","tech fall 11-1",None,False),
        ("Heavyweight","Mason Parris","Alexandr Romanov","Mason Parris","tech fall 11-0",None,False),
        ("Welterweight","Tajmuraz Salkazanov","James Green","Tajmuraz Salkazanov","dec 4-4 on criteria",None,False),
        ("Bantamweight","Austin DeSanto","Nico Megaludis","Austin DeSanto","tech fall 10-0",None,False),
      ]),
 dict(slug="raf-01", name="RAF 01", date="2025-08-30", venue="Wolstein Center", city="Cleveland, OH",
      stream="Fox Nation", tag="Hendrickson vs. Elders", debut=True,
      src="USA Wrestling", url="https://www.themat.com/news/2025/august/30/2025-world-team-members-woods-hendrickson-olympic-champion-hildebrandt-shine-in-raf-01-in-cleveland",
      note="The league's first card, opening with a tribute to Hulk Hogan, who died seven weeks earlier. Eight championships were decided in one night.",
      bouts=[
        ("Heavyweight","Wyatt Hendrickson","Mostafa Elders","Wyatt Hendrickson","tech fall 14-1","Heavyweight Championship",True),
        ("Light Heavyweight","Bo Nickal","Jacob Cardenas","Bo Nickal","dec 6-4","Light Heavyweight Championship",True),
        ("Women's Middleweight","Alejandra Rivera","Holly Holm","Alejandra Rivera","dec 9-7",None,False),
        ("Cruiserweight","Kyle Dake","Dean Hamiti","Kyle Dake","tech fall 11-0","Cruiserweight Championship",True),
        ("Featherweight","Real Woods","Darrion Caldwell","Real Woods","fall 3:29","Featherweight Championship",True),
        ("Women's Strawweight","Sarah Hildebrandt","Zeltzin Hernandez","Sarah Hildebrandt","tech fall 11-0","Women's Strawweight Championship",True),
        ("Middleweight","Evan Wick","Jason Nolf","Evan Wick","dec 10-8","Middleweight Championship",True),
        ("Lightweight","Austin Gomez","Lance Palmer","Austin Gomez","tech fall 11-0",None,False),
        ("Lightweight","Yianni Diakomihalis","Bajrang Punia","Yianni Diakomihalis","dec 5-1","Lightweight Championship",True),
        ("Bantamweight","Nathan Tomasello","Matt Ramos","Nathan Tomasello","dec 4-3","Bantamweight Championship",True),
      ]),
]

# ------------------------------------------------------------------ CLIPS
# every id oEmbed-verified: author_name is "Real American Freestyle Wrestling" or "Fox Nation"
CLIPS = {
 "raf-12":[("XYVMMGxHjIo","Live anniversary show from Cleveland")],
 "raf-11":[("uLSj7bv8mMQ","Live main card from Milwaukee"),("-l1jyB1k3Fo","Opening matches"),
           ("injIWpjSTP4","Inside match day")],
 "raf-georgia":[("qGYemvUYAac","Full show from Tbilisi"),("_4xneZSiDC0","Full broadcast episode"),
                ("FdAHq4V_DhE","Opening matches"),("6iI2OHmk4tg","Countdown to the main event")],
 "raf-10":[("lT35eurg7xY","Live show from St. Louis"),("VFQ-uqvwnjQ","Full broadcast episode"),
           ("Cq11eTX4xM4","Chimaev against Danis"),("X20SteWU4cs","Tsarukyan against Ferguson"),
           ("sNHBvdXyC0o","Opening matches"),("sM0c6Zxv2mg","Final press conference")],
 "raf-09":[("1cXidkYgcV0","Full broadcast episode"),("fJdK_sR947o","Steveson against Romanov, full match"),
           ("iel5Gtqdcec","Covington against Weidman, full match"),("8QnO_VxFlRE","Dvalishvili against Edgar"),
           ("210JbqJor5c","Opening matches")],
 "raf-08":[("YWt0fVCMSlk","Full replay"),("Dm-YNf3bnhw","Press conference"),
           ("fql7qFsLbpg","Opening match"),("PcMJAEuY-B8","Final press conference")],
 "raf-07":[("P7o1OXJDUtg","Full broadcast episode"),("OKldfg8wJfc","Dake against Keckeisen for the title")],
 "raf-06":[("E4CYMvb2XyA","Full event replay"),("-nvm6RbsTys","Full broadcast episode"),
           ("-yaPPY2RBPA","Cejudo against Faber in the main event"),("T15TGXKPSTc","Sterling against Henderson")],
 "raf-05":[("Bldm2vim5Pg","Full event from Sunrise"),("cZZJRO5d_TI","Covington against Rockhold")],
 "raf-04":[("5EJ9SPLSPG4","Full event with three title matches"),("HWtrezKgvSE","Hendrickson against Parris for the title")],
 "raf-03":[("15qqJDW-HhE","Full event with two title matches"),("ZqmJRhWdppA","Full broadcast episode"),
           ("wZJZwau41gM","Chandler against Mendes in the main event")],
 "raf-02":[("fuI-Fn4P-Hc","Full broadcast episode"),("J6rMrJVqFzI","Maroulis against Stewart for the title"),
           ("2NDu6DV8FZU","Dake against Makoev for the title")],
 "raf-01":[("m4pfB4YVmWE","Full event from the league debut"),("40HHz134UWc","Full broadcast episode"),
           ("MhVJdpKbK3w","Dake against Hamiti, highlights")],
}

CHAMPIONS = [
 ("Heavyweight","Wyatt Hendrickson","2025 NCAA champion, active duty U.S. Air Force"),
 ("Light Heavyweight","Kyle Snyder","2016 Olympic champion, three time World champion"),
 ("Cruiserweight","Kyle Dake","Four time World champion, two time Olympic bronze medallist"),
 ("Crossover Cruiserweight","Colby Covington","Former UFC welterweight title challenger"),
 ("Welterweight","David Carr","Two time NCAA champion, 2025 U.S. World Team"),
 ("Middleweight","Vacant","Last held by Dean Hamiti"),
 ("Lightweight","Vacant","Last held by Yianni Diakomihalis"),
 ("Featherweight","Real Woods","2025 World bronze medallist"),
 ("Bantamweight","Austin DeSanto","Took the belt from Nathan Tomasello at RAF 05"),
 ("Women's Middleweight","Kennedy Blades","2024 Olympic silver medallist"),
 ("Women's Bantamweight","Helen Maroulis","2016 Olympic champion, four time World champion"),
 ("Women's Strawweight","Lucia Yepez","Won the belt at RAF 10, defended at RAF 11"),
 ("Women's Cruiserweight","Vacant","Division opened at RAF 11"),
]

MON = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
def d2(s): return datetime.date.fromisoformat(s)
def pretty(s):
    d = d2(s); return "%s %d, %d" % (MON[d.month-1], d.day, d.year)
def longdate(s):
    d = d2(s); return d.strftime("%B %-d, %Y")

for e in EVENTS:
    e["_dt"] = d2(e["date"])
EVENTS.sort(key=lambda e: e["_dt"], reverse=True)


# ------------------------------------------------------------------ ATHLETES
# Profiles for RAF competitors who are NOT pro wrestlers, so they stay out of
# the /wrestlers/ roster namespace (its A-Z, counts and search index).
ATHLETES = [
 dict(slug="arman-tsarukyan", name="Arman Tsarukyan", realname="Arman Nairovich Tsarukyan",
      nick="Ahalkalakets", initials="AT", debut_year="2015",
      tagline="The UFC lightweight who wrestles for real",
      kick="Ahalkalakets \u00b7 Master of Sport, freestyle wrestling",
      the="Real American Freestyle",
      hero_tag='Crossover Cruiserweight \u00b7 <em>UFC \u00b7 RAF \u00b7 ADXC</em>',
      now_b="No. 2 UFC lightweight",
      now_rest="facing Mauricio Ruffy at UFC 331 on September 19",
      bornplace="Akhalkalaki, Georgia", nationality="Armenian", dob="1996-10-11",
      height="5 ft 7 in", reach="72.5 in", division="Lightweight", division_raf="Middleweight",
      team="American Top Team", coach="Marcos da Matta",
      stats=[("23-3","Pro MMA"),("10-2","In the UFC"),("7-1","In RAF"),("No. 2","Lightweight rank")],
      rafstats=[("7-1","RAF record"),("5","Tech falls"),("1","Title match"),("9","Matches booked")],
      ufcstats=[("23-3","Pro record"),("10-2","UFC record"),("9","KO or TKO"),("6","Submissions"),("4","Performance bonuses")],
      bio=[
        "Arman Tsarukyan is the clearest example of what Real American Freestyle was built to do. He is a top two UFC lightweight who spends the gaps between fights wrestling actual freestyle matches, and since January 2026 he has been the most active crossover athlete on the RAF roster.",
        "He was born in Akhalkalaki, Georgia, to an Armenian family, and played junior ice hockey for six years, including with the youth side of HC Amur, before choosing combat sport at seventeen. He turned professional in MMA in 2015 and arrived in the UFC in April 2019 on short notice, losing a Fight of the Night decision to Islam Makhachev on debut. He has lost once in the octagon since.",
        "His RAF run has been lopsided. Seven of his first eight matches were wins and five of those were technical falls. The exception is the one that mattered most: Colby Covington beat him 5-3 at RAF 11 for the inaugural Cruiserweight Crossover Championship, handing him his first RAF loss and taking the belt he had called for.",
        "He is also the reason RAF got its first genuine pull apart brawl. After beating Georgio Poullas at RAF 06 in Tempe he shoved and punched him, both corners spilled onto the mat, and the fighting carried into the crowd.",
      ],
      correction=("Tsarukyan and Islam Makhachev have fought once, in April 2019, and Makhachev won a unanimous decision. "
                  "A second fight was booked for the lightweight title at UFC 311 in January 2025 and Tsarukyan withdrew the day before with a back injury from the weight cut. "
                  "It gets written up as a two fight series constantly. It is not one. He has contested zero UFC title fights: one booked and withdrawn from, one declined in 2024, and one eliminator won at UFC 300."),
      social=[("X","https://x.com/ArmanUfc",'<svg viewBox="0 0 24 24" style="fill:currentColor"><path d="M18.9 2H22l-7.6 8.7L23.3 22h-6.9l-5.4-7-6.2 7H1.7l8.1-9.3L1 2h7.1l4.9 6.4L18.9 2Zm-2.4 18h1.9L7.6 3.9H5.6L16.5 20Z"/></svg>'),
              ("Instagram","https://www.instagram.com/arman_tsarukyan_/",'<svg viewBox="0 0 24 24" style="fill:currentColor"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.3 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.3 1.8-.4 2.2a3.8 3.8 0 0 1-.9 1.4 3.8 3.8 0 0 1-1.4.9c-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.3-2.2-.4a3.8 3.8 0 0 1-1.4-.9 3.8 3.8 0 0 1-.9-1.4c-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.3-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2Zm0 3.6A6.2 6.2 0 1 0 12 18.2 6.2 6.2 0 0 0 12 5.8Zm0 10.2A4 4 0 1 1 12 8a4 4 0 0 1 0 8Zm6.4-10.5a1.44 1.44 0 1 1-1.44-1.44 1.44 1.44 0 0 1 1.44 1.44Z"/></svg>')],
      watch=[("RAF","Real American Freestyle","Every RAF card on Fox Nation","Watch","https://nation.foxnews.com/real-american-freestyle-nation/"),
             ("UFC","UFC athlete profile","Official record and rankings","Visit","https://www.ufc.com/athlete/arman-tsarukyan"),
             ("RAF","His RAF athlete file","Match by match on RAF.com","Visit","https://www.realamericanfreestyle.com/athletes/arman-tsarukyan")],
      tape=[("Real name","Arman Nairovich Tsarukyan"),("Born","October 11, 1996"),("Birthplace","Akhalkalaki, Georgia"),
            ("Nationality","Armenian"),("Height","5 ft 7 in"),("Reach","72.5 in"),("Stance","Orthodox"),
            ("UFC division","Lightweight, 155 lb"),("RAF division","Middleweight"),("Team","American Top Team"),
            ("Head coach","Marcos da Matta"),("Pro MMA debut","September 2015"),("UFC debut","April 20, 2019"),
            ("RAF debut","January 10, 2026")],
      raf=[
        ("raf-14","2026-10-03","Dillon Danis",None,"Middleweight Crossover Championship","Announced"),
        ("raf-11","2026-07-18","Colby Covington",False,"dec 3-5","Cruiserweight Crossover Championship"),
        ("raf-georgia","2026-07-11","Kuat Khamitov",True,"tech fall 11-0",""),
        ("raf-10","2026-06-13","Tony Ferguson",True,"tech fall 10-0",""),
        ("raf-09","2026-05-30","Keelon Jimison",True,"tech fall 16-5",""),
        ("raf-08","2026-04-18","Urijah Faber",True,"tech fall 13-1",""),
        ("raf-07","2026-03-28","Georgio Poullas",True,"dec 9-3","Rematch"),
        ("raf-06","2026-02-28","Georgio Poullas",True,"decision, score disputed","Brawl after the bell"),
        ("raf-05","2026-01-10","Lance Palmer",True,"tech fall 10-0","RAF debut"),
      ],
      ufc=[
        ("2025-11-22","Dan Hooker",True,"Submission, arm triangle","2","3:34","UFC Fight Night: Tsarukyan vs. Hooker"),
        ("2024-04-13","Charles Oliveira",True,"Decision, split","3","5:00","UFC 300"),
        ("2023-12-02","Beneil Dariush",True,"KO, knee and punches","1","1:04","UFC on ESPN: Dariush vs. Tsarukyan"),
        ("2023-06-17","Joaquim Silva",True,"TKO, punches","3","3:25","UFC on ESPN 47"),
        ("2022-12-17","Damir Ismagulov",True,"Decision, unanimous","3","5:00","UFC Fight Night 216"),
        ("2022-06-25","Mateusz Gamrot",False,"Decision, unanimous","5","5:00","UFC on ESPN: Tsarukyan vs. Gamrot"),
        ("2022-02-26","Joel Alvarez",True,"TKO, punches","2","1:57","UFC Fight Night 202"),
        ("2021-09-18","Christos Giagos",True,"TKO, punches","1","2:09","UFC Fight Night 192"),
        ("2021-01-23","Matt Frevola",True,"Decision, unanimous","3","5:00","UFC 257"),
        ("2020-07-19","Davi Ramos",True,"Decision, unanimous","3","5:00","UFC Fight Night: Figueiredo vs. Benavidez 2"),
        ("2019-07-27","Olivier Aubin-Mercier",True,"Decision, unanimous","3","5:00","UFC 240"),
        ("2019-04-20","Islam Makhachev",False,"Decision, unanimous","3","5:00","UFC Fight Night 149"),
      ],
      rivalries=[
        ("Colby Covington","RAF 11, Crossover Championship",
         "Tsarukyan called Covington out from the mat at RAF 08 and Covington accepted. Three months later Covington beat him 5-2 in Milwaukee for the inaugural Crossover Championship, handing him his only RAF loss."),
        ("Georgio Poullas","RAF 06 and RAF 07",
         "The one that turned personal. Tsarukyan won a decision in Tempe that four outlets published four different ways, then attacked Poullas after the bell, triggering a mat wide brawl with both corners and fights in the crowd. He won the Tampa rematch 9-3."),
        ("Islam Makhachev","UFC Fight Night 149, 2019",
         "Makhachev won their only meeting by unanimous decision in Saint Petersburg, a Fight of the Night that was Tsarukyan's octagon debut on short notice. The rematch has been booked twice and has never happened."),
        ("Dillon Danis","RAF 14, October 3",
         "Announced for the inaugural Middleweight Crossover Championship at Fontainebleau Las Vegas. Danis was pinned in 41 seconds by Khamzat Chimaev at RAF 10."),
      ],
      faq=[
        ("Is Arman Tsarukyan a professional wrestler?",
         "No. He is a mixed martial artist who competes in freestyle wrestling. RAF matches are real competition scored under freestyle rules, not worked pro wrestling matches."),
        ("What is his RAF record?",
         "Seven wins and one loss across eight completed matches, with five of the wins by technical fall. The loss is to Colby Covington at RAF 11 in the Cruiserweight Crossover Championship match."),
        ("Has he fought Islam Makhachev twice?",
         "No. They fought once, in April 2019, and Makhachev won by unanimous decision. A title rematch was booked for UFC 311 in January 2025 and Tsarukyan pulled out the day before with a back injury."),
        ("Did he win an Olympic or World wrestling medal?",
         "No. He holds Master of Sport rank in freestyle wrestling and a second in mixed martial arts, but no world, European or national championship medal appears in any published record."),
        ("Who does he face next?",
         "Mauricio Ruffy at UFC 331 on September 19, 2026, and Dillon Danis at RAF 14 on October 3, 2026."),
      ],
      grappling=("His submission grappling record is 4-0-1, including a technical decision over Benson Henderson by arm triangle "
                 "and a fifth round rear naked choke on former Bellator champion Patricky Freire at ADXC 10 in May 2025."),
      background=("His wrestling background is real but thinner than the reputation suggests, and it is worth being exact about it. "
                  "He holds Master of Sport rank in freestyle wrestling and a second in mixed martial arts. No world, European or national "
                  "championship medal appears in any published record, and Armenian coverage has framed a European Championship run as "
                  "something he could still do rather than something he has done. What is documented is a wrestling base built alongside six "
                  "years of junior ice hockey, and a takedown game that has carried into both sports."),
      srcs=[("UFC.com","https://www.ufc.com/athlete/arman-tsarukyan"),
            ("Wikipedia","https://en.wikipedia.org/wiki/Arman_Tsarukyan"),
            ("Sherdog","https://www.sherdog.com/fighter/Arman-Tsarukyan-213913"),
            ("RAF athlete file","https://www.realamericanfreestyle.com/athletes/arman-tsarukyan")]),
]

# ---- Athlete files beyond Tsarukyan: everyone he has faced or is booked against in RAF,
# ---- plus crossover fighters the rest of the RAF data already names (see Woodley, below).
S_X = '<svg viewBox="0 0 24 24" style="fill:currentColor"><path d="M18.9 2H22l-7.6 8.7L23.3 22h-6.9l-5.4-7-6.2 7H1.7l8.1-9.3L1 2h7.1l4.9 6.4L18.9 2Zm-2.4 18h1.9L7.6 3.9H5.6L16.5 20Z"/></svg>'
S_IG = '<svg viewBox="0 0 24 24" style="fill:currentColor"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.3 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.3 1.8-.4 2.2a3.8 3.8 0 0 1-.9 1.4 3.8 3.8 0 0 1-1.4.9c-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.3-2.2-.4a3.8 3.8 0 0 1-1.4-.9 3.8 3.8 0 0 1-.9-1.4c-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.3-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2Zm0 3.6A6.2 6.2 0 1 0 12 18.2 6.2 6.2 0 0 0 12 5.8Zm0 10.2A4 4 0 1 1 12 8a4 4 0 0 1 0 8Zm6.4-10.5a1.44 1.44 0 1 1-1.44-1.44 1.44 1.44 0 0 1 1.44 1.44Z"/></svg>'
W_RAF = ("RAF","Real American Freestyle","Every RAF card on Fox Nation","Watch","https://nation.foxnews.com/real-american-freestyle-nation/")

OPPONENTS = [
 dict(slug="colby-covington", name="Colby Covington", realname="Colby Ray Covington", nick="Chaos",
      initials="CC", debut_year="2012", tagline="The inaugural Crossover Champion",
      kick="Chaos · NCAA All American, Oregon State", the="Real American Freestyle",
      hero_tag='Crossover Champion · <em>RAF · UFC</em>',
      now_b="RAF Crossover Champion", now_rest="defends against Belal Muhammad at RAF 13 on September 19",
      bornplace="Clovis, California", nationality="American", dob="1988-02-22",
      height="5 ft 11 in", reach="72 in", team="MMA Masters",
      stats=[("4-0","In RAF"),("17-5","Pro MMA"),("12-5","In the UFC"),("2011","NCAA All American")],
      rafstats=[("4-0","RAF record"),("1","Championship"),("36-11","Points for and against"),("4","Matches")],
      bio=["Colby Covington is the only man to beat Arman Tsarukyan in Real American Freestyle, and he did it for a belt. He took the inaugural Cruiserweight Crossover Championship 5-3 at RAF 11 in Milwaukee, in a match he had spent months talking his way into.",
           "The wrestling behind the persona is real. He was a 2011 NCAA Division I All American at Oregon State, placing fifth at 174 pounds, and before that went 34-0 as a junior college national champion at Iowa Central. Oregon State's own record books list him as the third All American of the Jim Zalesky era.",
           "He is 4-0 in RAF with wins over Luke Rockhold, Dillon Danis, Chris Weidman and Tsarukyan, and the margins tell a story: he shut Rockhold out 12-0 on debut, then beat Weidman and Tsarukyan by a combined 10-7.",
           "He retired from MMA in May 2026 after being left off a card he badly wanted, ending a UFC run that included an interim welterweight title and two losses to Kamaru Usman."],
      correction=("He is an investor in RAF while competing in it. Co-founder Chad Bronstein has said on the record that the investment buys him no matchmaking control, "
                  "overruling Covington publicly when he wanted a different opponent than Belal Muhammad."),
      social=[("X","https://x.com/ColbyCovMMA",S_X),("Instagram","https://www.instagram.com/colbycovmma/",S_IG)],
      watch=[W_RAF,("UFC","UFC athlete profile","Full MMA record","Visit","https://www.ufc.com/athlete/colby-covington"),
             ("RAF","His RAF athlete file","Match by match","Visit","https://www.realamericanfreestyle.com/athletes/colby-covington")],
      tape=[("Real name","Colby Ray Covington"),("Born","February 22, 1988"),("Birthplace","Clovis, California"),
            ("Nationality","American"),("Height","5 ft 11 in"),("Reach","72 in"),("RAF division","Cruiserweight, crossover"),
            ("MMA division","Welterweight"),("Team","MMA Masters, Miami"),("College","Oregon State"),
            ("NCAA best","5th at 174 lb, 2011"),("UFC debut","August 23, 2014"),("RAF debut","January 10, 2026")],
      raf=[("raf-13","2026-09-19","Belal Muhammad",None,"Cruiserweight Crossover Championship","Announced"),
           ("raf-11","2026-07-18","Arman Tsarukyan",True,"dec 5-3","Won the inaugural title"),
           ("raf-09","2026-05-30","Chris Weidman",True,"dec 5-4",""),
           ("raf-07","2026-03-28","Dillon Danis",True,"tech fall 14-4",""),
           ("raf-05","2026-01-10","Luke Rockhold",True,"tech fall 12-0","RAF debut")],
      alt_title="Selected UFC record", alt_lead="12-5 in the UFC and 17-5 as a professional, including the interim welterweight title in 2018.",
      alt=[("2024-12-14","Joaquin Buckley",False,"TKO, doctor stoppage","3","4:42","UFC on ESPN 63"),
           ("2023-12-16","Leon Edwards",False,"Decision, unanimous","5","5:00","UFC 296"),
           ("2022-03-05","Jorge Masvidal",True,"Decision, unanimous","5","5:00","UFC 272"),
           ("2021-11-06","Kamaru Usman",False,"Decision, unanimous","5","5:00","UFC 268"),
           ("2020-09-19","Tyron Woodley",True,"TKO, rib injury","5","1:19","UFC Fight Night 178"),
           ("2019-12-14","Kamaru Usman",False,"TKO, punches","5","4:10","UFC 245"),
           ("2019-08-03","Robbie Lawler",True,"Decision, unanimous","5","5:00","UFC on ESPN 5"),
           ("2018-06-09","Rafael dos Anjos",True,"Decision, unanimous","5","5:00","UFC 225, interim title")],
      background=("His college record is the part people skip. He was a two time Pac-10 champion at Oregon State and an NCAA Division I All American in 2011, "
                  "finishing fifth at 174 pounds after beating Christopher Henrich 3-2 in the placing match. Before Corvallis he went 34-0 and won an NJCAA national "
                  "title at 165 pounds for Iowa Central, and before that took an Oregon state title at Thurston High School with a 118-34 career record. RAF files his division three different ways: his athlete page says catchweight, the champions page says crossover cruiserweight, and the RAF 11 bout itself was contested at cruiserweight, which is what USA Wrestling logged."),
      rivalries=[("Arman Tsarukyan","RAF 11, Crossover Championship",
                  "Covington's objection was conduct, not skill. He pointed at Tsarukyan throwing Urijah Faber off the stage at RAF 08 and said it was not how the wrestling world behaves. He then beat him 5-3 for the belt."),
                 ("Belal Muhammad","RAF 13, September 19",
                  "The two nearly came to blows at the RAF 11 post-event press conference. Covington wanted a Kamaru Usman trilogy instead; RAF's founders made the Muhammad match anyway."),
                 ("Kamaru Usman","UFC 245 and UFC 268",
                  "Two welterweight title fights, two losses, the first by fifth round TKO and the second on the cards.")],
      faq=[("Did Colby Covington really wrestle in college?","Yes. He was a 2011 NCAA Division I All American at Oregon State, placing fifth at 174 pounds, and a junior college national champion at Iowa Central with a 34-0 season."),
           ("What is his RAF record?","4-0, with wins over Luke Rockhold, Dillon Danis, Chris Weidman and Arman Tsarukyan."),
           ("Is he still fighting in the UFC?","No. He notified the UFC of his retirement in May 2026."),
           ("What is the Crossover Championship?","A family of RAF belts contested by crossover athletes from other combat sports rather than career wrestlers, split by weight class. Covington won the inaugural Cruiserweight Crossover Championship by beating Tsarukyan at RAF 11. Tsarukyan meets Dillon Danis for the inaugural Middleweight Crossover Championship at RAF 14.")],
      srcs=[("UFC.com","https://www.ufc.com/athlete/colby-covington"),("Wikipedia","https://en.wikipedia.org/wiki/Colby_Covington"),
            ("Oregon State Athletics","https://osubeavers.com/sports/wrestling/roster/colby-covington/1640"),
            ("RAF athlete file","https://www.realamericanfreestyle.com/athletes/colby-covington")]),

 dict(slug="dillon-danis", name="Dillon Danis", nick="El Jefe", initials="DD", debut_year="2018",
      tagline="The black belt who keeps turning up in brawls",
      kick="El Jefe · Marcelo Garcia black belt", the="Real American Freestyle",
      hero_tag='Cruiserweight · <em>RAF · BJJ · Bellator</em>',
      now_b="0-2 in RAF", now_rest="faces Arman Tsarukyan at RAF 14 on October 3",
      bornplace="Parsippany-Troy Hills, New Jersey", nationality="American", dob="1993-08-22",
      height="6 ft 0 in", reach="Not published", team="SBG Ireland",
      stats=[("0-2","In RAF"),("2-0","Pro MMA"),("2015","BJJ black belt"),("2016","Pan No-Gi champion")],
      rafstats=[("0-2","RAF record"),("4","Points scored"),("24","Points conceded"),("1","Brawl")],
      bio=["Dillon Danis is a genuine Marcelo Garcia black belt with one of the thinnest competitive records in combat sports, and he has now brought both of those facts to freestyle wrestling.",
           "He is 0-2 in RAF. Colby Covington beat him 14-4 at RAF 07, and Khamzat Chimaev ended their RAF 10 main event inside a minute, after which Danis kicked out at him and both camps stormed the mat.",
           "The grappling credentials are real and worth stating plainly: black belt from Marcelo Garcia in April 2015, an IBJJF Pan No-Gi title at black belt in 2016, and a 0-0 draw with Gordon Ryan at ADCC 2017 that went against him on a referee decision.",
           "He faces Arman Tsarukyan at RAF 14 in Las Vegas on October 3, which puts him across from the man Covington beat for the Crossover Championship."],
      correction=("His professional MMA record is two fights, both first round submissions in Bellator, seven years apart from anything else. "
                  "A 2025 Misfits win over Warren Spencer is logged by Sherdog as an exhibition and by Wikipedia inside the record, which is why you will see both 2-0 and 3-0 published."),
      social=[("X","https://x.com/dillondanis",S_X),("Instagram","https://www.instagram.com/dillondanis/",S_IG)],
      watch=[W_RAF,("RAF","His RAF athlete file","Match by match","Visit","https://www.realamericanfreestyle.com/athletes/dillon-danis"),
             ("BJJ","BJJ Heroes profile","Grappling lineage and titles","Visit","https://www.bjjheroes.com/bjj-fighters/dillon-danis")],
      tape=[("Born","August 22, 1993"),("Birthplace","Parsippany-Troy Hills, New Jersey"),("Nationality","American"),
            ("Height","6 ft 0 in"),("RAF division","Cruiserweight"),("MMA team","SBG Ireland"),("BJJ team","Alliance"),
            ("Black belt","April 13, 2015, from Marcelo Garcia"),("Pro MMA","2-0"),("RAF debut","March 28, 2026")],
      raf=[("raf-14","2026-10-03","Arman Tsarukyan",None,"Middleweight Crossover Championship","Announced"),
           ("raf-10","2026-06-13","Khamzat Chimaev",False,"fall 0:41","Brawl after the bell"),
           ("raf-07","2026-03-28","Colby Covington",False,"tech fall 4-14","RAF debut")],
      background=("The grappling is the credential. His lineage runs Maeda to Carlos Gracie to Helio Gracie to Rolls Gracie to Romero Cavalcanti to Fabio Gurgel to "
                  "Marcelo Garcia, who promoted him to black belt on April 13, 2015. At black belt he won the IBJJF Pan No-Gi in 2016 plus New York Spring and Boca "
                  "Raton Opens. At ADCC 2017 he drew Gordon Ryan 0-0 in the first round and lost on referee decision, then submitted Yukiyasu Ozawa in the absolute."),
      rivalries=[("Khamzat Chimaev","RAF 10, June 13",
                  "Chimaev finished it in 41 seconds. Danis kicked out at him afterward, Chimaev kicked back, and both camps flooded the mat in RAF's second major brawl. RAF declined to ban him."),
                 ("Colby Covington","RAF 07, March 28",
                  "Danis out-attempted him on takedowns four to two and still lost 14-4, the pattern of his RAF run so far."),
                 ("Logan Paul","Misfits Boxing, October 2023",
                  "Lost by disqualification in round six for attempting a guillotine and then punching security as the ring filled.")],
      faq=[("Is Dillon Danis actually a good grappler?","Yes. He is a legitimate Marcelo Garcia black belt with an IBJJF Pan No-Gi title, and he drew Gordon Ryan at ADCC 2017."),
           ("What is his RAF record?","0-2, losing to Colby Covington at RAF 07 and Khamzat Chimaev at RAF 10."),
           ("How many professional MMA fights has he had?","Two sanctioned bouts, both first round submissions in Bellator. A 2025 Misfits win is logged as an exhibition by Sherdog."),
           ("Is he banned from the UFC?","Yes. Dana White said in November 2025 that Danis would never attend a UFC event again after a cageside brawl at UFC 322.")],
      srcs=[("Wikipedia","https://en.wikipedia.org/wiki/Dillon_Danis"),("Sherdog","https://www.sherdog.com/fighter/Dillon-Danis-247811"),
            ("BJJ Heroes","https://www.bjjheroes.com/bjj-fighters/dillon-danis"),
            ("RAF athlete file","https://www.realamericanfreestyle.com/athletes/dillon-danis")]),

 dict(slug="tony-ferguson", name="Tony Ferguson", realname="Anthony Armand Ferguson Padilla", nick="El Cucuy",
      initials="TF", debut_year="2008", tagline="The interim champion who came back to the mat",
      kick="El Cucuy · NCWA national champion", the="Real American Freestyle",
      hero_tag='Middleweight · <em>RAF · UFC · Misfits</em>',
      now_b="Misfits middleweight boxing champion", now_rest="0-1 in RAF after RAF 10",
      bornplace="Oxnard, California", nationality="American", dob="1984-02-12",
      height="5 ft 11 in", reach="76.5 in", team="Reign Training Center",
      stats=[("0-1","In RAF"),("25-11","Pro MMA"),("12","Fight win streak"),("2006","NCWA champion")],
      rafstats=[("0-1","RAF record"),("0","Points scored"),("10","Points conceded"),("1","Match")],
      bio=["Tony Ferguson built one of the great runs in UFC lightweight history and then one of its worst collapses, and at 42 he turned up on a wrestling mat to start again.",
           "The run was twelve straight UFC wins with nine finishes, tied for the second longest lightweight streak in company history alongside Khabib Nurmagomedov, and capped by an interim title over Kevin Lee at UFC 216. The collapse was eight consecutive losses, the longest losing streak the UFC has recorded.",
           "He signed with RAF in April 2026 and met Arman Tsarukyan in the RAF 10 co-main event in St. Louis. Tsarukyan led 6-0 off a first period toss and ended it 10-0 early in the second.",
           "His wrestling coach from Grand Valley State, Dave Mills, cornered him that night. Mills had once covered Ferguson's tuition shortfall on a promissory note."],
      correction=("His 2006 national title was NCWA, the National Collegiate Wrestling Association, not NCAA. It is a real national championship in a separate collegiate "
                  "association, and it is routinely miswritten as an NCAA credential."),
      social=[("X","https://x.com/TonyFergusonXT",S_X),("Instagram","https://www.instagram.com/tonyfergusonxt/",S_IG)],
      watch=[W_RAF,("UFC","UFC athlete profile","Full MMA record","Visit","https://www.ufc.com/athlete/tony-ferguson"),
             ("RAF","His RAF athlete file","Match by match","Visit","https://www.realamericanfreestyle.com/athletes/tony-ferguson")],
      tape=[("Real name","Anthony Armand Ferguson Padilla"),("Born","February 12, 1984"),("Birthplace","Oxnard, California"),
            ("Nationality","American"),("Height","5 ft 11 in"),("Reach","76.5 in"),("RAF division","Middleweight"),
            ("College","Grand Valley State"),("NCWA title","165 lb, 2006"),("UFC honour","Interim lightweight champion, 2017"),
            ("RAF debut","June 13, 2026")],
      raf=[("raf-10","2026-06-13","Arman Tsarukyan",False,"tech fall 0-10","RAF debut")],
      alt_title="Selected UFC record", alt_lead="Twelve straight wins, then eight straight losses. Both are UFC records or near them.",
      alt=[("2024-08-03","Michael Chiesa",False,"Submission, rear naked choke","1","","UFC on ABC 7"),
           ("2023-12-16","Paddy Pimblett",False,"Decision, unanimous","3","5:00","UFC 296"),
           ("2022-09-10","Nate Diaz",False,"Submission, guillotine","4","","UFC 279"),
           ("2022-05-07","Michael Chandler",False,"KO, front kick","2","","UFC 274"),
           ("2020-12-12","Charles Oliveira",False,"Decision, unanimous","3","5:00","UFC 256"),
           ("2020-05-09","Justin Gaethje",False,"TKO, punches","5","","UFC 249, interim title"),
           ("2019-06-08","Donald Cerrone",True,"TKO, doctor stoppage","2","","UFC 238"),
           ("2018-10-06","Anthony Pettis",True,"TKO, corner stoppage","2","","UFC 229"),
           ("2017-10-07","Kevin Lee",True,"Submission, triangle","3","","UFC 216, interim title")],
      background=("He wrestled at Grand Valley State after stops at Central Michigan and Muskegon Community College, captained the team, and won the NCWA national title "
                  "at 165 pounds in 2006. At Muskegon Catholic Central he was a three time All State wrestler, a 2002 state champion at 152 pounds, and a starting "
                  "defensive back on a state championship football team."),
      rivalries=[("Arman Tsarukyan","RAF 10, June 13",
                  "RAF billed it as pressure against pressure and a clash of wrestling eras. Tsarukyan tossed him for six in the first period and finished it 10-0 in the second."),
                 ("Khabib Nurmagomedov","Booked and never fought",
                  "The most famous fight that never happened. The two are tied for the second longest win streak in UFC lightweight history."),
                 ("Justin Gaethje","UFC 249, May 2020",
                  "The interim title fight that ended the twelve fight run and began the eight loss slide.")],
      faq=[("Did Tony Ferguson wrestle in college?","Yes, at Grand Valley State, where he captained the team and won the 2006 NCWA national title at 165 pounds. That is NCWA, not NCAA."),
           ("What is his RAF record?","0-1. He lost to Arman Tsarukyan by technical fall at RAF 10 in June 2026."),
           ("Has he retired from MMA?","No announcement has been published. He left the UFC in January 2025 and has since boxed for Misfits and wrestled for RAF."),
           ("What is his UFC losing streak?","Eight consecutive losses, the longest in UFC history, passing B.J. Penn with the Michael Chiesa defeat in August 2024.")],
      srcs=[("UFC.com","https://www.ufc.com/athlete/tony-ferguson"),("Wikipedia","https://en.wikipedia.org/wiki/Tony_Ferguson"),
            ("Sherdog","https://www.sherdog.com/fighter/Tony-Ferguson-31239"),
            ("RAF athlete file","https://www.realamericanfreestyle.com/athletes/tony-ferguson")]),

 dict(slug="urijah-faber", name="Urijah Faber", realname="Urijah Christopher Faber", nick="The California Kid",
      initials="UF", debut_year="2003", tagline="The Hall of Famer who took the throw",
      kick="The California Kid · UFC Hall of Fame, 2017", the="Real American Freestyle",
      hero_tag='Middleweight · <em>RAF · UFC · WEC</em>',
      now_b="UFC Hall of Famer", now_rest="0-2 in RAF after RAF 06 and RAF 08",
      bornplace="Isla Vista, California", nationality="American", dob="1979-05-14",
      height="5 ft 6 in", reach="67 in", team="Team Alpha Male",
      stats=[("0-2","In RAF"),("35-11","Pro MMA"),("2017","UFC Hall of Fame"),("5","WEC title defences")],
      rafstats=[("0-2","RAF record"),("1","Points scored"),("24","Points conceded"),("2","Main events")],
      bio=["Urijah Faber is in the UFC Hall of Fame, founded the gym that produced two UFC champions, and at 46 he took a RAF main event and got thrown off the stage.",
           "He was the WEC featherweight champion with five successful defences, held King of the Cage and Gladiator Challenge belts, and went into the Hall of Fame's modern wing in 2017 as the first bantamweight or featherweight inducted.",
           "His RAF run is 0-2. Henry Cejudo shut him out 11-0 at RAF 06 in Tempe, then Arman Tsarukyan beat him 13-1 at RAF 08 in Philadelphia, in a match elevated to the main event when Cejudo withdrew injured.",
           "That RAF 08 match is the one people remember, and not for the score."],
      correction=("At RAF 08, Tsarukyan hit a single leg and drove Faber completely off the raised stage onto the floor beside the announce desk. Each wrestler was awarded "
                  "a point for it and neither was hurt. Faber's response on Instagram: he has all the makings of a champion except self control."),
      social=[("X","https://x.com/UrijahFaber",S_X),("Instagram","https://www.instagram.com/urijahfaber/",S_IG)],
      watch=[W_RAF,("UFC","UFC athlete profile","Full MMA record","Visit","https://www.ufc.com/athlete/urijah-faber"),
             ("RAF","His RAF athlete file","Match by match","Visit","https://www.realamericanfreestyle.com/athletes/urijah-faber")],
      tape=[("Real name","Urijah Christopher Faber"),("Born","May 14, 1979"),("Birthplace","Isla Vista, California"),
            ("Nationality","American"),("Height","5 ft 6 in"),("Reach","67 in"),("RAF division","Middleweight, 175 lb"),
            ("College","UC Davis"),("NCAA","Qualifier 2001 and 2002"),("Career wins","92, a UC Davis record"),
            ("Hall of Fame","UFC, class of 2017"),("RAF debut","February 28, 2026")],
      raf=[("raf-08","2026-04-18","Arman Tsarukyan",False,"tech fall 1-13","Main event"),
           ("raf-06","2026-02-28","Henry Cejudo",False,"tech fall 0-11","Main event, RAF debut")],
      background=("He wrestled at UC Davis from 2000 to 2003, qualified for the NCAA Division I Championships in 2001 and 2002, and still holds the programme's all time "
                  "records for career wins with 92 and dual wins with 42. In 2002 at 133 pounds he went 31-10 and lost in the fourth round of wrestlebacks, one match short "
                  "of becoming UC Davis's first ever wrestling All American."),
      rivalries=[("Arman Tsarukyan","RAF 08, April 18",
                  "The single leg that carried Faber off the stage and onto the floor. Faber called him a spoiled kid for life and said he had every making of a champion except self control."),
                 ("Henry Cejudo","RAF 06, February 28",
                  "Cejudo shut him out 11-0 in Arizona, leading 3-0 after one period and 7-0 after two, then called out Merab Dvalishvili."),
                 ("Dominick Cruz","UFC and WEC",
                  "Faber won the first meeting and lost the next two, the defining trilogy of the lighter weight classes in that era.")],
      faq=[("Why is Urijah Faber in RAF?","He has said the wrestling community competed for years without pay and that RAF is a real professional route for wrestlers to make a career."),
           ("What is his RAF record?","0-2, losing to Henry Cejudo at RAF 06 and Arman Tsarukyan at RAF 08."),
           ("What happened at RAF 08?","Tsarukyan drove him off the raised stage onto the floor on a single leg. Both men were awarded a point and neither was injured."),
           ("Is he a UFC Hall of Famer?","Yes, class of 2017, modern wing, the first fighter from the bantamweight or featherweight divisions inducted.")],
      srcs=[("UFC.com","https://www.ufc.com/athlete/urijah-faber"),("Wikipedia","https://en.wikipedia.org/wiki/Urijah_Faber"),
            ("USA Wrestling","https://www.themat.com/news/2017/april/09/wrestler-urijah-faber-to-be-inducted-into-ufc-hall-of-fame"),
            ("RAF athlete file","https://www.realamericanfreestyle.com/athletes/urijah-faber")]),

 dict(slug="lance-palmer", name="Lance Palmer", nick="The Party", initials="LP", debut_year="2011",
      tagline="Four time All American, two time PFL champion",
      kick="The Party · Four time NCAA All American, Ohio State", the="Real American Freestyle",
      hero_tag='Lightweight · <em>RAF · PFL · WSOF</em>',
      now_b="RAF Head of Talent Development", now_rest="1-3 as an RAF competitor",
      bornplace="Cleveland, Ohio", nationality="American", dob="1987-02-07",
      height="5 ft 6 in", reach="69 in", team="Nick Catone MMA",
      stats=[("1-3","In RAF"),("23-8","Pro MMA"),("4x","NCAA All American"),("2","PFL titles")],
      rafstats=[("1-3","RAF record"),("4","Matches"),("1","Win, over Cayden Henschel"),("2021","Ohio State Hall of Fame")],
      bio=["Lance Palmer has the deepest wrestling resume of anyone Arman Tsarukyan has faced in RAF, and it did not help him for very long.",
           "He is one of only eight four time NCAA All Americans in Ohio State history, placing fourth as a true freshman in 2007, eighth in 2008, fourth in 2009 and second in 2010, when he also won the Big Ten title at 149 pounds and was named the conference tournament's most outstanding wrestler. He went into the Ohio State Athletics Hall of Fame in 2021.",
           "In MMA he won back to back Professional Fighters League season championships in 2018 and 2019, a million dollars each, after two runs as WSOF featherweight champion.",
           "Tsarukyan's RAF debut came against him at RAF 05 and lasted one period: an immediate takedown for four, then another with a turn, and a 10-0 technical fall."],
      correction=("He is not only a competitor. Palmer has been RAF's Head of Talent Development since 2025, which makes him one of the few people who both books the "
                  "roster and loses to it."),
      social=[("X","https://x.com/LancePalmerMMA",S_X),("Instagram","https://www.instagram.com/lancepalmer/",S_IG)],
      watch=[W_RAF,("RAF","His RAF athlete file","Match by match","Visit","https://www.realamericanfreestyle.com/athletes/lance-palmer"),
             ("OSU","Ohio State Hall of Fame","His college record","Visit","https://ohiostatebuckeyes.com/honors/hall-of-fame-inductees/lance-palmer/325")],
      tape=[("Born","February 7, 1987"),("Birthplace","Cleveland, Ohio"),("Nationality","American"),
            ("Height","5 ft 6 in"),("Reach","69 in"),("RAF division","Lightweight"),("MMA division","Featherweight"),
            ("College","Ohio State, 2007 to 2010"),("NCAA","All American four times at 149 lb"),
            ("Big Ten","Champion, 2010"),("College record","121-33"),("RAF role","Head of Talent Development")],
      raf=[("raf-10","2026-06-13","Aaron Pico",False,"tech fall 1-12",""),
           ("raf-08","2026-04-18","Cayden Henschel",True,"dec 3-2",""),
           ("raf-05","2026-01-10","Arman Tsarukyan",False,"tech fall 0-10",""),
           ("raf-01","2025-08-30","Austin Gomez",False,"tech fall 0-11","RAF debut")],
      background=("Four NCAA All American finishes at 149 pounds for Ohio State, in 2007, 2008, 2009 and 2010, one of only eight wrestlers in programme history to do it. "
                  "He was Big Ten champion and the tournament's most outstanding wrestler in 2010, team captain that year, and finished 121-33 in college. Before that he "
                  "won four Ohio state titles at St. Edward High School with a 150-6 record and an NHSCA senior national title."),
      rivalries=[("Arman Tsarukyan","RAF 05, January 10",
                  "Tsarukyan's RAF debut. Two takedowns and a turn inside the first period for a 10-0 technical fall, celebrated with the Armenian flag."),
                 ("Aaron Pico","RAF 10, June 13",
                  "Pico's wrestling comeback came at Palmer's expense, a 12-1 technical fall in St. Louis."),
                 ("Cayden Henschel","RAF 08, April 18",
                  "His only RAF win to date, a 3-2 decision in Philadelphia.")],
      faq=[("How good a wrestler was Lance Palmer?","One of eight four time NCAA All Americans in Ohio State history, a 2010 Big Ten champion, and an Ohio State Athletics Hall of Famer."),
           ("What is his RAF record?","1-3, with the win over Cayden Henschel at RAF 08."),
           ("What did he win in the PFL?","Back to back season championships in 2018 and 2019, worth a million dollars each."),
           ("Does he work for RAF?","Yes. He has been RAF's Head of Talent Development since 2025 while still competing.")],
      srcs=[("Ohio State Athletics","https://ohiostatebuckeyes.com/honors/hall-of-fame-inductees/lance-palmer/325"),
            ("Wikipedia","https://en.wikipedia.org/wiki/Lance_Palmer"),("Sherdog","https://www.sherdog.com/fighter/Lance-Palmer-80836"),
            ("RAF athlete file","https://www.realamericanfreestyle.com/athletes/lance-palmer")]),

 dict(slug="georgio-poullas", name="Georgio Poullas", initials="GP", debut_year="2026",
      nick="Canfield", tagline="The street wrestler who cashed the biggest purse",
      kick="Canfield, Ohio · Division I at Cleveland State and Rider", the="Real American Freestyle",
      hero_tag='Middleweight · <em>RAF</em>',
      now_b="1-2 in RAF", now_rest="no bout booked since RAF 07",
      bornplace="Canfield, Ohio", nationality="American", dob="1998-04-21",
      height="Not published", reach="Not published", team="Not published",
      stats=[("1-2","In RAF"),("176-15","High school record"),("2016","Ohio state champion"),("3","RAF matches")],
      rafstats=[("1-2","RAF record"),("1","Technical fall win"),("2","Losses to Tsarukyan"),("1","Post-match brawl")],
      bio=["Georgio Poullas came to Real American Freestyle from the internet, not from a national team, and ended up in the promotion's most notorious moment.",
           "He wrestled Division I at Cleveland State and then Rider without a published national placing, coached at his old high school, moved to Los Angeles and built a following on fitness content and a street challenge series offering strangers a thousand dollars to take him down.",
           "RAF signed him and he beat Keelon Jimison by technical fall at RAF 05. Then came Arman Tsarukyan twice: a contested points decision at RAF 06 that ended with Tsarukyan tackling and punching him after the whistle, and a 9-3 rematch loss at RAF 07.",
           "The rematch carried what a Creators Inc. executive called the largest purse ever paid for a competitive wrestling match, close to seven figures for six minutes."],
      correction=("Four different scores have been published for the RAF 06 decision. RAF's own pages say 5-4, most of the press says 5-3, MMA Mania says 6-4 and USA Wrestling "
                  "says 5-2. Every source agrees Tsarukyan won on points in the third period. This page does not pick one."),
      social=[("Instagram","https://www.instagram.com/georgiopoullas/",S_IG)],
      watch=[W_RAF,("RAF","His RAF athlete file","Match by match","Visit","https://www.realamericanfreestyle.com/athletes/georgio-poullas")],
      tape=[("Born","April 21, 1998"),("Birthplace","Canfield, Ohio"),("Nationality","American"),
            ("RAF division","Middleweight"),("High school","Canfield, Ohio"),("State title","152 lb, 2016"),
            ("High school record","176-15"),("College","Cleveland State, then Rider"),("RAF debut","January 10, 2026")],
      raf=[("raf-07","2026-03-28","Arman Tsarukyan",False,"dec 3-9","Rematch"),
           ("raf-06","2026-02-28","Arman Tsarukyan",False,"decision, score disputed","Brawl after the bell"),
           ("raf-05","2026-01-10","Keelon Jimison",True,"tech fall 12-1","RAF debut")],
      background=("He was a 2016 Ohio state champion at 152 pounds, the first Canfield state title in seventeen years, and a state runner up in 2017, finishing 176-15 across "
                  "his career. He wrestled Division I at Cleveland State from 2017 to 2019 and at Rider in 2019 and 2020. No NCAA placing or All America honour is published "
                  "for him, and no freestyle national placing either. What he built instead was an audience."),
      rivalries=[("Arman Tsarukyan","RAF 06 and RAF 07",
                  "Two matches, one brawl, and a great deal of talking. Poullas called the post-whistle tackle a coward move and said he would be ready if it happened again. It did not; Tsarukyan won the rematch 9-3."),
                 ("Keelon Jimison","RAF 05, January 10",
                  "His only RAF win, a first period technical fall inside a minute and a half.")],
      faq=[("Who is Georgio Poullas?","An Ohio wrestler who competed at Cleveland State and Rider, built a following through fitness content and a street wrestling challenge series, and signed with RAF in 2026."),
           ("What is his RAF record?","1-2. He beat Keelon Jimison at RAF 05 and lost to Arman Tsarukyan at RAF 06 and RAF 07."),
           ("What happened in the RAF 06 brawl?","Tsarukyan tackled and punched him after the final whistle. Both corners flooded the mat and the fighting spilled into the crowd. No discipline against either man was ever reported."),
           ("What was the RAF 06 score?","It depends who you ask. RAF says 5-4, most outlets say 5-3, MMA Mania says 6-4 and USA Wrestling says 5-2. All agree Tsarukyan won.")],
      srcs=[("Wikipedia","https://en.wikipedia.org/wiki/Georgio_Poullas"),
            ("RAF athlete file","https://www.realamericanfreestyle.com/athletes/georgio-poullas"),
            ("Tribune Chronicle","https://www.tribtoday.com/sports/local-sports/2026/02/poullas-finds-new-avenue-to-continue-wrestling/")]),

 dict(slug="keelon-jimison", name="Keelon Jimison", nick="Mugzy", initials="KJ", debut_year="2025",
      tagline="The comeback story with no college behind it",
      kick="Mugzy · Kansas City, Missouri", the="Real American Freestyle",
      hero_tag='Welterweight · <em>RAF</em>',
      now_b="1-3 in RAF", now_rest="no bout booked since RAF 09",
      bornplace="Kansas City, Missouri", nationality="American", dob=None,
      height="Not published", reach="Not published", team="Not published",
      stats=[("1-3","In RAF"),("4","RAF matches"),("1","Win, over Clay Guida"),("0","College wrestling")],
      rafstats=[("1-3","RAF record"),("1","Technical fall win"),("2","Open weight bouts"),("4","Matches")],
      bio=["Keelon Jimison, who competes as Mugzy, is the RAF athlete with the least conventional background on the roster and one of the better stories.",
           "He never wrestled in college and did not place in high school. He built an audience of close to a million followers wrestling fans who invited him, produced an instructional series on the ankle pick, and RAF signed him off that.",
           "He is 1-3 in RAF. The win is the one that matters to him: a technical fall over UFC veteran Clay Guida at RAF 06, after which he talked about jail, selling drugs and not quitting on himself.",
           "Arman Tsarukyan tech falled him 16-5 at RAF 09, though not before Jimison hit a four point throw to cut a 5-0 hole to 5-4."],
      correction=("His official RAF page lists three matches and a 1-0-2 record. It omits his RAF 02 loss to Cayden Henschel, which RAF itself recapped and which FloWrestling "
                  "and InterMat both carry. His actual record is 1-3 across four matches."),
      social=[("Instagram","https://www.instagram.com/mugzy_bulljunk/",S_IG)],
      watch=[W_RAF,("RAF","His RAF athlete file","Match by match","Visit","https://www.realamericanfreestyle.com/athletes/mugzy")],
      tape=[("Nickname","Mugzy"),("Hometown","Kansas City, Missouri"),("Nationality","American"),
            ("RAF division","Welterweight"),("College wrestling","None"),("RAF debut","October 25, 2025"),
            ("RAF matches","4"),("Notable win","Clay Guida, RAF 06")],
      raf=[("raf-09","2026-05-30","Arman Tsarukyan",False,"tech fall 5-16",""),
           ("raf-06","2026-02-28","Clay Guida",True,"tech fall 13-2",""),
           ("raf-05","2026-01-10","Georgio Poullas",False,"tech fall 1-12","Open weight"),
           ("raf-02","2025-10-25","Cayden Henschel",False,"tech fall 1-11","Open weight, RAF debut")],
      background=("There is no college wrestling record and no national placing, and he says so himself. He did not place in high school and never went to college. What he "
                  "has instead is an audience built on wrestling members of the public who invited him, and an instructional series on the ankle pick. He has spoken publicly "
                  "about jail time, substance abuse and rebuilding, which is the frame RAF has used for him."),
      rivalries=[("Arman Tsarukyan","RAF 09, May 30",
                  "Down 5-0, Jimison hit a four point throw to make it 5-4 before Tsarukyan pulled away to a 16-5 technical fall. Tsarukyan gave him a shout out afterward."),
                 ("Clay Guida","RAF 06, February 28",
                  "His RAF win, a second period technical fall over a UFC veteran, and the match that produced his comeback interview."),
                 ("Georgio Poullas","RAF 05, January 10",
                  "A technical fall loss inside the first period, in an open weight bout.")],
      faq=[("Did Keelon Jimison wrestle in college?","No. He has said publicly that he never attended college and did not place in high school wrestling."),
           ("What is his RAF record?","1-3 across four matches. His official RAF page shows only three and omits the RAF 02 loss."),
           ("Why is he called Mugzy?","It is the name he competes and posts under, sometimes billed as Mugzy BullJunk."),
           ("What is his best RAF win?","A technical fall over UFC veteran Clay Guida at RAF 06 in February 2026.")],
      srcs=[("RAF athlete file","https://www.realamericanfreestyle.com/athletes/mugzy"),
            ("USA Wrestling","https://www.themat.com/news/2026/march/02/olympic-champ-cejudo-returns-carr-defends-belt-at-raf-06"),
            ("FloWrestling","https://www.flowrestling.org/articles/14671206-results-from-real-american-freestyle-02")]),

 dict(slug="kuat-khamitov", name="Kuat Khamitov", nick="Naiman", initials="KK", debut_year="2008",
      tagline="Kazakhstan's crossover star",
      kick="Naiman · Alash Pride", the="Real American Freestyle",
      hero_tag='Middleweight · <em>RAF · ACA · Boxing</em>',
      now_b="Vice President, Almaty Region Wrestling Federation", now_rest="appointed August 15, 2026",
      bornplace="Yntaly, Almaty Region, Kazakhstan", nationality="Kazakh", dob="1988-02-22",
      height="5 ft 8 in", reach="70 in", team="Alash Pride",
      stats=[("0-1","In RAF"),("25-9-1","Pro MMA"),("2","WBK titles"),("1","Pro boxing win")],
      rafstats=[("0-1","RAF record"),("0","Points scored"),("11","Points conceded"),("4","Takedowns conceded")],
      bio=["Kuat Khamitov is one of the biggest crossover names in Kazakh combat sport, a fighter, boxer, film actor and now a wrestling federation executive, and RAF brought him to Tbilisi to meet Arman Tsarukyan.",
           "He fights out of Alash Pride and has spent his career across Fight Nights Global, ACA, RCC and regional Kazakh promotions, holding two WBK world titles at lightweight and welterweight.",
           "In September 2024 he made his professional boxing debut in Almaty and won the WBC Allstars belt over six rounds.",
           "His single RAF appearance came at RAF Georgia in July 2026. He got in on single legs repeatedly and Tsarukyan peeled off and reversed each one, taking it 11-0 with 54 seconds left."],
      correction=("His published MMA record varies by source: Sherdog has 25-9-1 with a bout by bout history, Kazakh outlets report 28-8-2, and Tapology has a stale 26-7-2. "
                  "RAF's own page also lists his age as 28 where four MMA databases give a 1988 birth date, which would make him 38."),
      social=[("Instagram","https://www.instagram.com/kuat_khamitov/",S_IG)],
      watch=[W_RAF,("RAF","His RAF athlete file","Match by match","Visit","https://www.realamericanfreestyle.com/athletes/kuat-khamitov"),
             ("MMA","Sherdog record","Bout by bout history","Visit","https://www.sherdog.com/fighter/Kuat-Khamitov-86936")],
      tape=[("Born","February 22, 1988"),("Birthplace","Yntaly, Almaty Region, Kazakhstan"),("Nationality","Kazakh"),
            ("Height","5 ft 8 in"),("Reach","70 in"),("Stance","Southpaw"),("RAF division","Middleweight"),
            ("MMA division","Welterweight"),("Team","Alash Pride"),("Titles","WBK lightweight and welterweight"),
            ("Boxing","1-0, WBC Allstars belt"),("RAF debut","July 11, 2026")],
      raf=[("raf-georgia","2026-07-11","Arman Tsarukyan",False,"tech fall 0-11","RAF debut")],
      alt_title="Recent MMA record", alt_lead="Sherdog logs 25-9-1 with a bout by bout history running to February 2026.",
      alt=[("2026-02-14","Alan Silva",True,"Decision","3","","GFC 36"),
           ("2025-10-23","Anatoliy Boyko",True,"Decision","3","","ACA 194"),
           ("2024-05-11","Alexander Shlemenko",False,"Decision","3","","RCC 19"),
           ("2023-03-01","Bobur Abdulazizov",True,"Submission, guillotine","1","","MFC 4"),
           ("2022-09-01","Vasily Babintsev",True,"Submission","1","","MFC 3"),
           ("2021-09-01","Marif Piraev",False,"Decision, split","3","","AMC Fight Nights 104")],
      background=("He began wrestling at five and came up through Kazakhstan's wrestling system before turning to mixed martial arts around 2008, and his style is built on "
                  "takedowns and positional control. No specific freestyle, sambo or judo title or rank is published for him anywhere. In August 2026 he was appointed Vice "
                  "President of the Wrestling Federation of Almaty Region, an administrative post rather than a competitive credential."),
      rivalries=[("Arman Tsarukyan","RAF Georgia, July 11",
                  "A homecoming for Tsarukyan, who was born in Akhalkalaki, Georgia. Khamitov kept getting to single legs and kept getting peeled off, and it ended 11-0."),
                 ("Alexander Shlemenko","RCC 19, May 2024",
                  "A decision loss to the long time Bellator middleweight champion.")],
      faq=[("Who is Kuat Khamitov?","A Kazakh mixed martial artist and boxer from the Almaty region who fights out of Alash Pride, and a media figure in Kazakhstan."),
           ("What is his RAF record?","0-1. He lost to Arman Tsarukyan by technical fall at RAF Georgia in July 2026."),
           ("What is his MMA record?","Sources disagree. Sherdog says 25-9-1, Kazakh outlets say 28-8-2, and Tapology has an older 26-7-2."),
           ("Does he box?","Yes. He debuted professionally in September 2024 in Almaty and won the WBC Allstars belt over six rounds.")],
      srcs=[("Sherdog","https://www.sherdog.com/fighter/Kuat-Khamitov-86936"),
            ("RAF athlete file","https://www.realamericanfreestyle.com/athletes/kuat-khamitov"),
            ("Tapology","https://www.tapology.com/fightcenter/fighters/27721-kuat-khamitov")]),

 # Woodley is NOT a Tsarukyan opponent. He files here because he is on the RAF 12 card
 # and sits inside Colby Covington's UFC record above, so athlete_link() already reaches
 # for him from two places. He is a mixed martial artist, so he stays out of /wrestlers/.
 dict(slug="tyron-woodley", name="Tyron Woodley", nick="The Chosen One", initials="TW",
      debut_year="2009", tagline="The welterweight champion who went back to the mat",
      kick="The Chosen One · Two time NCAA All American, Missouri", the="Real American Freestyle",
      hero_tag='Cruiserweight · <em>RAF · UFC · Boxing</em>',
      now_b="1-0 in RAF", now_rest="meets Khamzat Chimaev at RAF Moscow on September 5",
      bornplace="Ferguson, Missouri", nationality="American", dob="1982-04-07",
      height="5 ft 9 in", reach="74 in", team="ATT Evolution",
      stats=[("19-7-1","Pro MMA"),("9-6-1","In the UFC"),("1-0","In RAF"),("2x","NCAA All American")],
      rafstats=[("1-0","RAF record"),("14-8","Debut win"),("13","Unanswered points"),("2","Matches booked")],
      bio=["Tyron Woodley held the UFC welterweight championship for 945 days and defended it three times, and at 44 he has taken the wrestling that built all of it back to an actual wrestling mat.",
           "The wrestling came first and it was serious. He went 48-0 as a senior at McCluer High School in Florissant, Missouri and won the Class 4A state title at 160 pounds in 2000. At the University of Missouri he finished 110-38, became the first Big 12 champion in the programme's history in 2003, and earned All America honours twice, eighth at 165 pounds in 2003 and seventh in 2005.",
           "He turned professional in mixed martial arts in February 2009, went 10-1 across Strikeforce and the regional circuit, and knocked out Robbie Lawler in 2:12 at UFC 201 in July 2016 for the welterweight belt. He lost it to Kamaru Usman at UFC 235 in March 2019 and never won again in the octagon, dropping his last four to Usman, Gilbert Burns, Colby Covington and Vicente Luque.",
           "Boxing did not go better: two losses to Jake Paul in 2021, the second by sixth round knockout, and a second round stoppage by a 50 year old Anderson Silva in December 2025, leaving him 0-3. Then RAF put him on its anniversary card in Cleveland against Joaquin Buckley. He went 8-1 down in the first period, a point from losing by technical superiority, scored thirteen unanswered and won 14-8. It was his first competitive win of any kind since Darren Till in 2018."],
      correction=("UFC.com bills his reign as four title defences and lists Stephen Thompson twice. Three of the four were wins. "
                  "The fourth, UFC 205 in November 2016, was a majority draw: Woodley kept the belt because a champion keeps the belt on a draw, "
                  "but he did not beat Thompson that night, which is exactly why the rematch was ordered. Wikipedia's summary repeats the four and "
                  "Sports Illustrated headlined the draw as a successful defence. The three real defences are UFC 209, UFC 214 and UFC 228."),
      social=[("X","https://x.com/TWooodley",S_X),("Instagram","https://www.instagram.com/twooodley/",S_IG)],
      watch=[W_RAF,("UFC","UFC athlete profile","Full MMA record","Visit","https://www.ufc.com/athlete/tyron-woodley"),
             ("RAF","His RAF athlete file","Match by match","Visit","https://www.realamericanfreestyle.com/athletes/tyron-woodley")],
      tape=[("Born","April 7, 1982"),("Birthplace","Ferguson, Missouri"),("Nationality","American"),
            ("Height","5 ft 9 in"),("Reach","74 in"),("Stance","Orthodox"),
            ("RAF division","Cruiserweight"),("MMA division","Welterweight"),("Team","ATT Evolution"),
            ("High school","McCluer, Florissant, Missouri"),("State title","160 lb, Class 4A, 2000"),
            ("College","Missouri"),("College record","110-38"),("Big 12 title","165 lb, 2003"),
            ("NCAA best","7th at 165 lb, 2005"),("Pro MMA debut","February 7, 2009"),
            ("UFC debut","February 2, 2013"),("UFC title reign","July 30, 2016 to March 2, 2019"),
            ("Pro boxing","0-3"),("RAF debut","August 22, 2026")],
      raf=[("raf-moscow","2026-09-05","Khamzat Chimaev",None,"Catchweight, main event","Announced"),
           ("raf-12","2026-08-22","Joaquin Buckley",True,"dec 14-8","RAF debut")],
      alt_title="UFC record, decided bouts",
      alt_lead=("9-6-1 across sixteen UFC bouts between 2013 and 2021. The fifteen decided bouts are below. The sixteenth, "
                "Stephen Thompson at UFC 205 on November 12, 2016, was a majority draw he left still holding the belt."),
      altstats=[("19-7-1","Pro record"),("9-6-1","UFC record"),("3","Title defences"),("945","Days as champion"),("0-3","Pro boxing")],
      alt=[("2021-03-27","Vicente Luque",False,"Submission, D'Arce choke","1","3:56","UFC 260"),
           ("2020-09-19","Colby Covington",False,"TKO, rib injury","5","1:19","UFC Fight Night 178"),
           ("2020-05-30","Gilbert Burns",False,"Decision, unanimous","5","5:00","UFC on ESPN: Woodley vs. Burns"),
           ("2019-03-02","Kamaru Usman",False,"Decision, unanimous","5","5:00","UFC 235"),
           ("2018-09-08","Darren Till",True,"Submission, D'Arce choke","2","4:19","UFC 228, title defence"),
           ("2017-07-29","Demian Maia",True,"Decision, unanimous","5","5:00","UFC 214, title defence"),
           ("2017-03-04","Stephen Thompson",True,"Decision, majority","5","5:00","UFC 209, title defence"),
           ("2016-07-30","Robbie Lawler",True,"KO, punches","1","2:12","UFC 201, won the title"),
           ("2015-01-31","Kelvin Gastelum",True,"Decision, split","3","5:00","UFC 183"),
           ("2014-08-23","Dong Hyun Kim",True,"TKO, punches","1","1:01","UFC Fight Night 48"),
           ("2014-06-14","Rory MacDonald",False,"Decision, unanimous","3","5:00","UFC 174"),
           ("2014-03-15","Carlos Condit",True,"TKO, knee injury","2","2:00","UFC 171"),
           ("2013-11-16","Josh Koscheck",True,"KO, punches","1","4:38","UFC 167"),
           ("2013-06-15","Jake Shields",False,"Decision, split","3","5:00","UFC 161"),
           ("2013-02-02","Jay Hieron",True,"KO, punches","1","0:36","UFC 156, UFC debut")],
      background=("The wrestling is the deepest credential on this page, and it is worth being exact about it. He was an all state pick in 1999 and 2000 "
                  "at McCluer High School in Florissant, went 48-0 as a senior, and took Missouri's Class 4A title at 160 pounds with a 3-1 decision over "
                  "Adam Stern, the most wins of any Missouri state champion that year and only the third state title in his school's history. At the "
                  "University of Missouri he wrestled four years at 165 pounds, finished 110-38, and in 2003 beat Iowa State's Nick Passolano 5-1 in "
                  "overtime to become the first Big 12 champion the Missouri programme ever had. He was an NCAA Division I All American twice, eighth in "
                  "2003 and seventh in 2005, and graduated that year in agricultural economics. What is not there matters too: no NCAA title, no Olympic "
                  "or senior world medal, and no senior freestyle national title is published for him. The closest are a 2006 University freestyle national "
                  "runner up finish and a Real Pro Wrestling regional championship the same year. Missouri put him in its athletics hall of fame in 2019."),
      rivalries=[("Colby Covington","UFC Fight Night 178, September 2020",
                  "Five rounds, and the finish is still argued over. Woodley's rib gave out at 1:19 of the fifth and the bout was waved off as a TKO by injury, "
                  "which Covington has always framed as a quit. Covington holds RAF's Cruiserweight Crossover Championship on the same roster Woodley just joined."),
                 ("Stephen Thompson","UFC 205 and UFC 209",
                  "Ten rounds over four months for the belt: a majority draw in New York in November 2016, then a majority decision in Las Vegas in March 2017. "
                  "Neither was popular, and the first is the reason his defence count is misreported to this day."),
                 ("Joaquin Buckley","RAF 12, August 22",
                  "His RAF debut and his first competitive win since 2018. Buckley led 8-1 inside the first period, one point from ending it by technical superiority, "
                  "and Woodley answered with thirteen straight to win 14-8."),
                 ("Khamzat Chimaev","RAF Moscow, September 5",
                  "Announced as the catchweight main event of RAF's first card in Russia, two weeks after Cleveland. Chimaev pinned Dillon Danis in 41 seconds "
                  "on his own RAF debut at RAF 10.")],
      faq=[("Is Tyron Woodley a professional wrestler?",
            "No. He is a former UFC welterweight champion competing in freestyle wrestling for RAF. RAF matches are real competition scored under freestyle rules, not worked pro wrestling matches. He wrestled at Missouri long before he ever fought."),
           ("How many times did he defend the UFC welterweight title?",
            "Three: Stephen Thompson at UFC 209, Demian Maia at UFC 214 and Darren Till at UFC 228. UFC.com says four because it counts the UFC 205 majority draw with Thompson, which he did not win."),
           ("What is his RAF record?",
            "1-0. He beat Joaquin Buckley 14-8 at RAF 12 in Cleveland on August 22, 2026, after trailing 8-1 in the first period."),
           ("Was he an NCAA champion?",
            "No. He was an NCAA Division I All American twice at Missouri, eighth at 165 pounds in 2003 and seventh in 2005, and the first Big 12 champion in Missouri history. He never won a national title."),
           ("What is his professional boxing record?",
            "0-3. He lost twice to Jake Paul in 2021 and was stopped in the second round by Anderson Silva in December 2025."),
           ("Who does he face next?",
            "Khamzat Chimaev at RAF Moscow on September 5, 2026, in a catchweight main event.")],
      srcs=[("UFC.com","https://www.ufc.com/athlete/tyron-woodley"),
            ("Wikipedia","https://en.wikipedia.org/wiki/Tyron_Woodley"),
            ("Sherdog","https://www.sherdog.com/fighter/Tyron-Woodley-42605"),
            ("Missouri Athletics","https://mutigers.com/news/2019/11/14/mizzou-hall-of-fame-feature-tyron-woodley"),
            ("RAF athlete file","https://www.realamericanfreestyle.com/athletes/tyron-woodley")]),
]

ATHLETES = ATHLETES + OPPONENTS
# Tsarukyan is the anchor of this set, so he leads; everyone he has met sorts by name.
ATHLETES = ATHLETES[:1] + sorted(ATHLETES[1:], key=lambda x: x["name"].split()[-1])
ATHLETE_BY_NAME = {a["name"]: a["slug"] for a in ATHLETES}

EVENT_BY_SLUG = {e["slug"]: e for e in EVENTS}

def _age(dob):
    d = d2(dob)
    return TODAY.year - d.year - ((TODAY.month, TODAY.day) < (d.month, d.day))

# Page-local CSS, mirroring how /wrestlers/ profiles ship theirs in an inline <style>.
# These classes exist in NEITHER site.css NOR profile.css. Verbatim from the cm-punk page
# so this profile renders identically. Scoped under .wl-dossier exactly as there.
PROFILE_CSS = """
.wl-dossier .sec-lead{font-family:'Inter',system-ui,sans-serif;color:rgba(244,245,247,.62);font-size:15px;line-height:1.55;max-width:74ch;margin:-4px 0 22px}
.wl-dossier .sec-body{font-family:'Inter',system-ui,sans-serif;color:rgba(244,245,247,.82);font-size:16px;line-height:1.7;max-width:72ch;margin:0 0 14px}
.wl-dossier .rec2-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(96px,1fr));gap:10px;margin:2px 0 16px}
.wl-dossier .rec2-stat{background:#12141a;border:1px solid rgba(255,255,255,.06);border-radius:10px;padding:11px 13px}
.wl-dossier .rec2-stat b{display:block;font-family:'Anton',sans-serif;font-size:22px;color:#f4f5f7;letter-spacing:.01em}
.wl-dossier .rec2-stat span{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.06em;text-transform:uppercase;color:#8a8f98}
.wl-dossier .rec2-scroll{max-height:366px;overflow-y:auto;overflow-x:auto;border:1px solid rgba(255,255,255,.08);border-radius:12px;scrollbar-width:thin;scrollbar-color:#d4af37 transparent;background:linear-gradient(90deg,#0f1116 30%,rgba(15,17,22,0)) 0 0/28px 100% no-repeat,linear-gradient(90deg,rgba(15,17,22,0),#0f1116 70%) 100% 0/28px 100% no-repeat,radial-gradient(farthest-side at 0 50%,rgba(212,175,55,.28),transparent) 0 0/14px 100% no-repeat,radial-gradient(farthest-side at 100% 50%,rgba(212,175,55,.28),transparent) 100% 0/14px 100% no-repeat;background-attachment:local,local,scroll,scroll}
.wl-dossier .rec2-scroll::-webkit-scrollbar{width:9px;height:9px}
.wl-dossier .rec2-scroll::-webkit-scrollbar-thumb{background:rgba(212,175,55,.5);border-radius:9px}
.wl-dossier .rec2-table{width:100%;border-collapse:collapse;font-family:'Inter',sans-serif;font-size:12.5px;min-width:760px}
.wl-dossier .rec2-table thead th{position:sticky;top:0;z-index:2;background:#0f1116;text-align:left;padding:10px 12px;font-family:'JetBrains Mono',monospace;font-size:9.5px;letter-spacing:.06em;text-transform:uppercase;color:#8a8f98;border-bottom:1px solid rgba(212,175,55,.28);white-space:nowrap}
.wl-dossier .rec2-table td{padding:9px 12px;border-bottom:1px solid rgba(255,255,255,.045);vertical-align:top;color:rgba(244,245,247,.82)}
.wl-dossier .rec2-table tbody tr:nth-child(even){background:rgba(255,255,255,.015)}
.wl-dossier .rec2-table tbody tr:hover{background:rgba(212,175,55,.06)}
.wl-dossier .rec2-table td.dim{color:rgba(244,245,247,.5)}
.wl-dossier .rec2-table th:first-child,.wl-dossier .rec2-table td:first-child{min-width:88px}
.wl-dossier .rec2-date{font-family:'JetBrains Mono',monospace;font-size:11px;white-space:nowrap}
.wl-dossier .rec2-per{font-size:11.5px;color:rgba(244,245,247,.62);white-space:nowrap}
.wl-dossier .rec2-ev{font-weight:500;color:#f4f5f7;min-width:150px}
.wl-dossier .rec2-opp{color:rgba(244,245,247,.8)}
.wl-dossier .rec2-count{font-family:'JetBrains Mono',monospace;font-size:11px;color:#8a8f98;margin:11px 0 0}
.wl-dossier .rec2-count b{color:#f2cc4b}
.wl-dossier .opp-link{color:inherit;text-decoration:none;border-bottom:1px solid rgba(212,175,55,.28);transition:color .12s,border-color .12s}
.wl-dossier .opp-link:hover{color:#f2cc4b;border-bottom-color:#f2cc4b}
.wl-dossier .opp-link:focus-visible{outline:2px solid #d4af37;outline-offset:2px;border-radius:2px}
.wl-dossier .rw{display:inline-grid;place-items:center;width:22px;height:22px;border-radius:6px;font-family:'Anton',sans-serif;font-size:12px}
.wl-dossier .rw-w{background:rgba(37,181,110,.16);color:#4ce39a;border:1px solid rgba(37,181,110,.44)}
.wl-dossier .rw-l{background:rgba(225,29,42,.14);color:#ff6b73;border:1px solid rgba(225,29,42,.34)}
.wl-dossier .rw-d{background:rgba(255,255,255,.08);color:#cfd2d8;border:1px solid rgba(255,255,255,.16)}
.wl-dossier .pchip{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.04em;text-transform:uppercase;padding:3px 7px;border-radius:5px;background:rgba(255,255,255,.06);color:#a7abb2;white-space:nowrap}
.wl-dossier .pchip-raf{background:rgba(46,95,163,.2);color:#8fb0ff}
.wl-dossier .pchip-ufc{background:rgba(225,29,42,.14);color:#ff8a90}
.wl-dossier .pchip-belt{background:rgba(212,175,55,.14);color:#f2cc4b}
.wl-dossier .faq2-list{display:flex;flex-direction:column;gap:8px}
.wl-dossier .faq2-item{background:#12141a;border:1px solid rgba(255,255,255,.07);border-radius:11px;overflow:hidden}
.wl-dossier .faq2-item[open]{border-color:rgba(212,175,55,.28)}
.wl-dossier .faq2-q{list-style:none;cursor:pointer;display:flex;align-items:center;justify-content:space-between;gap:14px;padding:14px 16px;font-family:'Oswald',sans-serif;font-weight:600;text-transform:uppercase;letter-spacing:.02em;font-size:14px;color:#f4f5f7}
.wl-dossier .faq2-q::-webkit-details-marker{display:none}
.wl-dossier .faq2-ic{flex:none;position:relative;width:14px;height:14px}
.wl-dossier .faq2-ic:before,.wl-dossier .faq2-ic:after{content:"";position:absolute;background:#d4af37;transition:transform .2s}
.wl-dossier .faq2-ic:before{left:0;top:6px;width:14px;height:2px}
.wl-dossier .faq2-ic:after{left:6px;top:0;width:2px;height:14px}
.wl-dossier .faq2-item[open] .faq2-ic:after{transform:scaleY(0)}
.wl-dossier .faq2-a{font-family:'Inter',sans-serif;font-size:13.5px;line-height:1.6;color:rgba(244,245,247,.66);margin:0;padding:0 16px 15px}
.wl-dossier .fac-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:14px}
.wl-dossier .fac-card{background:linear-gradient(180deg,#14161d,#0f1116);border:1px solid rgba(255,255,255,.08);border-radius:13px;padding:18px;min-width:0}
.wl-dossier .fac-era{font-family:'JetBrains Mono',monospace;font-size:9.5px;letter-spacing:.06em;text-transform:uppercase;color:#8a8f98;margin-bottom:7px;display:block}
.wl-dossier .fac-name{font-family:'Anton',sans-serif;text-transform:uppercase;font-size:20px;color:#f4f5f7;margin:0 0 9px;line-height:1.05}
.wl-dossier .fac-desc{font-family:'Inter',sans-serif;font-size:13px;line-height:1.5;color:rgba(244,245,247,.6);margin:0}
.wl-dossier .corr{background:#12141a;border:1px solid rgba(212,175,55,.26);border-left:3px solid #d4af37;border-radius:12px;padding:15px 19px;margin:6px 0 0}
.wl-dossier .corr b{display:block;font-family:'JetBrains Mono',monospace;font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:#f2cc4b;margin-bottom:8px}
.wl-dossier .corr p{margin:0;font-family:'Inter',sans-serif;font-size:13.5px;line-height:1.6;color:rgba(244,245,247,.72);max-width:74ch}
.wl-dossier .srcs{display:flex;flex-direction:column;gap:7px;margin-top:4px}
.wl-dossier .srcs a{font-family:'JetBrains Mono',monospace;font-size:10.5px;letter-spacing:.05em;text-transform:uppercase;color:#d4af37;text-decoration:none;border-bottom:1px solid rgba(212,175,55,.24);padding-bottom:5px}
.wl-dossier .srcs a:hover{color:#f2cc4b}
@media(max-width:640px){
.wl-dossier .rec2-table{min-width:640px;font-size:12px}
.wl-dossier .rec2-table thead th{padding:9px 10px}
.wl-dossier .rec2-table td{padding:8px 10px}
.wl-dossier .rec2-date{font-size:10.5px}
.wl-dossier .rec2-ev{min-width:130px}
.wl-dossier .rec2-stats{grid-template-columns:repeat(2,1fr)}
.wl-dossier .sec-lead{font-size:14px}
.wl-dossier .fac-grid{grid-template-columns:1fr}
}
"""

def profile_shell(title, desc, canonical, body, extra_head=""):
    """The /wrestlers/ profile template. profile.css scopes ~432 rules under .wl-dossier,
    and the profiles ship a further page-local <style> block for components that live in
    neither stylesheet (.rec2-*, .rw, .pchip, .faq2-*, .sec-lead). Both are required."""
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
      '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
      '<title>%s</title>\n<meta name="description" content="%s">\n<link rel="canonical" href="%s">\n'
      '<meta name="robots" content="index,follow">\n'
      '<meta property="og:type" content="profile">\n<meta property="og:title" content="%s">\n'
      '<meta property="og:description" content="%s">\n<meta property="og:url" content="%s">\n'
      '<meta property="og:site_name" content="Wrestle Lore">\n%s'
      '<link rel="stylesheet" href="/css/site.css">\n'
      '<link rel="stylesheet" href="/css/profile.css">\n'
      '<style>%s</style>\n</head>\n<body>\n'
      '<header class="site-header nav7"></header>\n%s\n'
      '<footer class="site-footer site-footer--fat"></footer>\n'
      '<script src="/js/main.js" defer></script>\n<script src="/js/search-index.js" defer></script>\n'
      '<script src="/js/nav.js" defer></script>\n<script src="/js/engage.js" defer></script>\n'
      '<script src="/js/profile.js" defer></script>\n</body>\n</html>\n'
      % (esc(title), esc(desc), canonical, esc(title), esc(desc), canonical, extra_head,
         PROFILE_CSS.strip("\n"), body))

SECS_HEAD = [("overview","Overview"),("record","RAF Record")]
SECS_TAIL = [("background","Background"),("rivalries","Rivalries"),("faq","FAQ")]

def alt_of(a):
    """Every athlete file carries a RAF record. Most also carry a second combat record
    from the sport they are known for. Arman's key is `ufc` for historical reasons;
    the opponents use the generic `alt`. Normalise both here so athlete_page has one shape."""
    rows = a.get("alt") or a.get("ufc")
    if not rows: return None
    title = a.get("alt_title") or "UFC Record"
    return dict(rows=rows, title=title,
                nav=("UFC Record" if "UFC" in title else "MMA Record"),
                stats=a.get("altstats") or a.get("ufcstats"),
                lead=a.get("alt_lead"))

def secs_for(a):
    alt = alt_of(a)
    return SECS_HEAD + ([("mma", alt["nav"])] if alt else []) + SECS_TAIL

def athlete_link(name, self_slug=None):
    """Cross-link an opponent name to their own athlete file when we have one.
    This is what makes the RAF athlete set a connected graph rather than nine orphans."""
    s = ATHLETE_BY_NAME.get(name)
    if not s or s == self_slug: return esc(name)
    return '<a class="opp-link" href="/promotions/raf/athletes/%s/">%s</a>' % (s, esc(name))

def _pub(v):
    return v and str(v).strip() and str(v).strip().lower() != "not published"

def athlete_page(a):
    alt = alt_of(a)
    name = a["name"]; me = a["slug"]
    if alt:
        title = "%s: RAF Record, %s and Profile | Wrestle Lore" % (name, alt["nav"])
    else:
        title = "%s: RAF Record and Full Profile | Wrestle Lore" % name
    tl = a["tagline"]
    desc = ("%s, %s. Complete Real American Freestyle record, every match dated, linked to its "
            "card and sourced, plus the background behind it." % (name, tl[0].lower() + tl[1:]))
    canonical = "%s/promotions/raf/athletes/%s/" % (BASE, a["slug"])
    num = lambda i: '<span class="n">%02d</span>' % i

    secs = secs_for(a)
    subnav = ('<nav class="subnav" aria-label="Profile sections"><ul>%s</ul>'
              '<span class="subnav-ind" aria-hidden="true"></span></nav>'
              % "".join('<li><a href="#%s">%s</a></li>' % (i, l) for i, l in secs))

    seg = ["EST.&nbsp;%s" % a["debut_year"]]
    if _pub(a.get("height")): seg.append(a["height"].replace(" ", "&nbsp;"))
    if _pub(a.get("reach")):  seg.append("%s REACH" % a["reach"].replace(" ", "&nbsp;"))
    seg.append(a.get("vitals_rec") or
               ("%s %s" % (a["stats"][0][0],
                           a["stats"][0][1].upper().replace("IN THE ", "").replace("IN ", ""))))
    vitals = (" <i>&middot;</i> ".join(seg) +
              " <i>&middot;</i> <b>&#10216;&nbsp;%s&nbsp;&#10217;</b>" % esc(a["nick"].upper()))

    idn = ('<div class="idn" id="idn"><div class="idn-in">'
      '<nav class="idn-crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">&rsaquo;</span>'
      '<a href="/promotions/raf/">RAF</a><span class="sep">&rsaquo;</span><span class="cur">%s</span></nav>'
      '<div class="idn-plate"><span class="idn-eye">%s</span><b class="idn-name">%s</b>'
      '<span class="idn-dia">&#9670;</span><span class="idn-vitals">%s</span><span class="idn-sep"></span>'
      '<div class="idn-soc">%s</div>'
      '<div class="idn-supwrap"><button class="idn-support js-idn" aria-expanded="false">Watch <span class="chev">&#8964;</span></button>'
      '<div class="idn-panel" id="idnPanel"><div class="sp-head"><span class="sp-k">Where to watch %s</span>'
      '<span class="sp-note">%s</span></div>%s</div></div></div>'
      '<div class="idn-rightspace" aria-hidden="true"></div></div></div>'
      % (esc(name.split()[-1]), esc(a["tagline"]), esc(name.upper()), vitals,
         "".join('<a href="%s" target="_blank" rel="noopener" aria-label="%s">%s</a>' % (esc(u), esc(lbl), ic)
                 for lbl, u, ic in a["social"]),
         esc(name.split()[0]),
         esc(" &middot; ".join(dict.fromkeys(x[0] for x in a["watch"]))).replace("&amp;", "&"),
         "".join('<a class="sp-item" href="%s" target="_blank" rel="noopener"><span class="sp-ic">%s</span>'
                 '<span class="sp-txt"><b>%s</b><span>%s</span></span><span class="sp-tag">%s</span></a>'
                 % (esc(u), esc(ic), esc(t), esc(sub), esc(tag)) for ic, t, sub, tag, u in a["watch"])))

    hstats = "".join('<div class="hstat"><b><span class="num">%s</span></b><span>%s</span></div>'
                     % (esc(v), esc(l)) for v, l in a["stats"])
    ghost = ('<a class="ghost-link" href="#mma">And the %s alongside it</a>' % esc(alt["nav"].lower())) if alt \
            else '<a class="ghost-link" href="#background">And the wrestling behind it</a>'
    hero = ('<header class="hero" id="top"><div class="wrap"><div>'
      '<div class="hero-kick">%s</div><h1><span class="the">%s</span>%s</h1>'
      '<p class="hero-tag">%s</p>'
      '<div class="hero-now"><span>NOW</span><b>%s</b> &middot; %s</div>'
      '<div class="hero-stats">%s</div>'
      '<div class="hero-cta-row"><button class="discover" type="button" data-scroll="#record">Explore the full record'
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="m6 9 6 6 6-6"/></svg></button>'
      '%s</div></div>'
      '<figure class="portrait" aria-label="%s key art"><span class="slot">PHOTO SLOT</span>'
      '<span class="vlabel">Est. %s &middot; %s</span>'
      '<svg class="crown" viewBox="0 0 64 54" aria-hidden="true"><path d="M6 46 L2 14 L18 26 L32 6 L46 26 L62 14 L58 46 Z"/></svg>'
      '<span class="mono" aria-hidden="true">%s</span>'
      '<figcaption class="cap"><span class="r">Roster File &middot; %s</span><span class="n">%s</span></figcaption>'
      '</figure></div></header>'
      % (a["kick"], esc(a["the"]), esc(name), a["hero_tag"], esc(a["now_b"]), esc(a["now_rest"]),
         hstats, ghost, esc(name), a["debut_year"], esc(a["bornplace"]), esc(a["initials"]),
         esc(a["tagline"]), esc(a.get("realname") or name)))

    tiles = lambda rows: '<div class="rec2-stats">%s</div>' % "".join(
        '<div class="rec2-stat"><b>%s</b><span>%s</span></div>' % (esc(v), esc(l)) for v, l in rows)

    sec1 = ('<section class="sec reveal" id="overview"><div class="sec-h">%s<h2>Overview</h2></div>'
            '<p class="sec-lead">%s</p>%s'
            '<div class="corr"><b>Setting one thing straight</b><p>%s</p></div></section>'
            % (num(1), esc(a["bio"][0]),
               "".join('<p class="sec-body">%s</p>' % esc(x) for x in a["bio"][1:]), esc(a["correction"])))

    rrows = []
    for slug, date, opp, win, method, note in a["raf"]:
        ev = EVENT_BY_SLUG.get(slug)
        evc = ('<a class="opp-link" href="/promotions/raf/%s/">%s</a>' % (slug, esc(ev["name"]))) if ev \
              else esc(slug.upper().replace("-", " "))
        badge = ('<span class="rw rw-w">W</span>' if win else '<span class="rw rw-l">L</span>') \
                if win is not None else '<span class="rw rw-d">&ndash;</span>'
        chip = '<span class="pchip pchip-belt">%s</span>' % esc(note) if note else ""
        rrows.append('<tr><td class="rec2-date">%s</td><td class="rec2-ev">%s %s</td>'
                     '<td class="rec2-opp">%s</td><td>%s</td><td class="dim">%s</td></tr>'
                     % (pretty(date), evc, chip, athlete_link(opp, me), badge, esc(method)))
    done = len([x for x in a["raf"] if x[3] is not None])
    upc = len(a["raf"]) - done
    sec2 = ('<section class="sec reveal" id="record"><div class="sec-h">%s<h2>RAF Record</h2></div>%s'
            '<p class="sec-lead">%s across %d completed %s, every one linked to its full card. A tech fall means '
            'a ten point lead ended it early, freestyle wrestling&rsquo;s version of a squash.</p>'
            '<div class="rec2-scroll"><table class="rec2-table"><thead><tr><th>Date</th><th>Event</th>'
            '<th>Opponent</th><th>Result</th><th>Method</th></tr></thead><tbody>%s</tbody></table></div>'
            '<p class="rec2-count"><b>%d</b> %s on record, <b>%d</b> announced</p></section>'
            % (num(2), tiles(a["rafstats"]), a["rafstats"][0][0], done,
               "match" if done == 1 else "matches", "".join(rrows),
               done, "match" if done == 1 else "matches", upc))

    secs_html = [sec1, sec2]
    n = 3
    if alt:
        urows = []
        for date, opp, win, method, rd, tm, event in alt["rows"]:
            per = ('<td class="rec2-per">R%s %s</td>' % (esc(rd), esc(tm))) if rd else '<td class="rec2-per">&ndash;</td>'
            urows.append('<tr><td class="rec2-date">%s</td><td class="rec2-opp">%s</td>'
                         '<td>%s</td><td class="dim">%s</td>%s'
                         '<td class="rec2-ev">%s</td></tr>'
                         % (pretty(date), athlete_link(opp, me),
                            '<span class="rw rw-w">W</span>' if win else '<span class="rw rw-l">L</span>',
                            esc(method), per, esc(event)))
        lead = alt["lead"] or ("%s in the UFC and %s as a professional. He debuted in April 2019 on short notice."
                               % (a["stats"][1][0], a["stats"][0][0]))
        secs_html.append(
            '<section class="sec reveal" id="mma"><div class="sec-h">%s<h2>%s</h2></div>%s'
            '<p class="sec-lead">%s</p>'
            '<div class="rec2-scroll"><table class="rec2-table"><thead><tr><th>Date</th><th>Opponent</th>'
            '<th>Result</th><th>Method</th><th>Round</th><th>Event</th></tr></thead><tbody>%s</tbody></table></div>'
            '<p class="rec2-count"><b>%d</b> %s listed</p></section>'
            % (num(n), esc(alt["title"]), tiles(alt["stats"]) if alt["stats"] else "",
               esc(lead), "".join(urows), len(alt["rows"]),
               "bout" if len(alt["rows"]) == 1 else "bouts"))
        n += 1

    bg = '<p class="sec-body">%s</p>' % esc(a["background"])
    if a.get("grappling"): bg += '<p class="sec-body">%s</p>' % esc(a["grappling"])
    secs_html.append('<section class="sec reveal" id="background"><div class="sec-h">%s<h2>Background</h2></div>%s</section>'
                     % (num(n), bg)); n += 1

    secs_html.append('<section class="sec reveal" id="rivalries"><div class="sec-h">%s<h2>Rivalries</h2></div>'
            '<div class="fac-grid">%s</div></section>'
            % (num(n), "".join('<div class="fac-card"><span class="fac-era">%s</span>'
                               '<h3 class="fac-name">%s</h3><p class="fac-desc">%s</p></div>'
                               % (esc(k), athlete_link(t, me), esc(d)) for t, k, d in a["rivalries"]))); n += 1

    secs_html.append('<section class="sec reveal" id="faq"><div class="sec-h">%s<h2>FAQ</h2></div>'
            '<div class="faq2-list">%s</div></section>'
            % (num(n), "".join('<details class="faq2-item"><summary class="faq2-q">%s'
                               '<span class="faq2-ic" aria-hidden="true"></span></summary>'
                               '<p class="faq2-a">%s</p></details>' % (esc(q), esc(ans)) for q, ans in a["faq"])))

    # Everyone else in the RAF athlete set, so no profile is a dead end for a crawler.
    others = [o for o in ATHLETES if o["slug"] != me]
    also = ('<section class="card" aria-labelledby="also-h"><h2 id="also-h" class="kick">Other RAF athlete files</h2>'
            '<div class="srcs">%s</div></section>'
            % "".join('<a href="/promotions/raf/athletes/%s/">%s</a>' % (o["slug"], esc(o["name"])) for o in others))

    rail = ('<aside class="rail" aria-label="Quick facts">'
      '<section class="card tott" aria-labelledby="tott-h"><h2 id="tott-h" class="kick">Tale of the Tape</h2><dl>%s</dl></section>'
      '%s'
      '<section class="card" aria-labelledby="src-h"><h2 id="src-h" class="kick">Sources</h2>'
      '<div class="srcs">%s</div></section></aside>'
      % ("".join('<div class="row"><dt>%s</dt><dd>%s</dd></div>' % (esc(k), esc(v)) for k, v in a["tape"]),
         also,
         "".join('<a href="%s" target="_blank" rel="noopener">%s</a>' % (esc(u), esc(nm)) for nm, u in a["srcs"])))

    q2 = lambda t: esc(t).replace('"', '\\"')
    faq_ld = ",".join('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
                      % (q2(q), q2(ans)) for q, ans in a["faq"])
    bits = ['"name":"%s"' % esc(name), '"alternateName":"%s"' % esc(a["nick"])]
    if a.get("dob"): bits.append('"birthDate":"%s"' % a["dob"])
    bits.append('"birthPlace":{"@type":"Place","name":"%s"}' % esc(a["bornplace"]))
    bits.append('"nationality":"%s"' % esc(a["nationality"]))
    if _pub(a.get("height")): bits.append('"height":"%s"' % esc(a["height"]))
    bits.append('"jobTitle":"Freestyle wrestler"' if not alt else
                '"jobTitle":"Mixed martial artist and freestyle wrestler"')
    bits.append('"url":"%s"' % canonical)
    bits.append('"affiliation":[{"@type":"SportsOrganization","name":"Real American Freestyle"}]')
    bits.append('"sameAs":[%s]' % ",".join('"%s"' % u for _, u in a["srcs"]))
    jsonld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Person",%s}</script>\n'
      '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s]}</script>\n'
      '<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
      '{"@type":"ListItem","position":1,"name":"Home","item":"%s/"},'
      '{"@type":"ListItem","position":2,"name":"Promotions","item":"%s/promotions/"},'
      '{"@type":"ListItem","position":3,"name":"RAF","item":"%s/promotions/raf/"},'
      '{"@type":"ListItem","position":4,"name":"%s","item":"%s"}]}</script>\n'
      % (",".join(bits), faq_ld, BASE, BASE, BASE, esc(name), canonical))

    body = ('<div class="wl-dossier bar-glass" id="main">%s%s%s'
            '<div class="layout"><main class="profile-main">%s</main>%s</div></div>'
            % (subnav, idn, hero, "".join(secs_html), rail))
    return profile_shell(title, desc, canonical, body, extra_head=jsonld)

# ------------------------------------------------------------------ RENDER
FOXNATION = "https://nation.foxnews.com/real-american-freestyle-nation/"
def yt(vid, label, ev):
    """Same facade contract as build_gallery.facade_card so js/media.js adopts it
    and opens the shared theater player. Do not invent a second facade shape."""
    ttl = "%s, %s" % (label, longdate(ev["date"]))
    return ('<article class="vcard raf-vcard">'
            '<div class="yt" data-yt-id="%s" data-yt-title="%s" data-yt-creator="Real American Freestyle" '
            'data-yt-service="Fox Nation" data-yt-service-url="%s">'
            '<a class="yt__link" href="https://www.youtube.com/watch?v=%s" target="_blank" rel="noopener">%s</a></div>'
            '<div class="vcard__body"><span class="telemetry"><b>%s</b></span>'
            '<h3 class="vcard__title">%s</h3></div></article>'
            % (esc(vid), esc(ttl), FOXNATION, esc(vid), esc(label), esc(ev["name"]), esc(label)))

def bout_row(b, upcoming):
    wc, a, bb, win, method, title, change = b
    if upcoming or not win:
        res = '<span class="raf-tbd">Not yet wrestled</span>'
        acell = '<span class="raf-n">%s</span>' % athlete_link(a)
        bcell = '<span class="raf-n">%s</span>' % athlete_link(bb)
    else:
        loser = bb if win == a else a
        acell = '<span class="raf-n is-win">%s</span>' % athlete_link(win)
        bcell = '<span class="raf-n">%s</span>' % athlete_link(loser)
        res = esc(method or "")
    tl = ""
    if title:
        cls = "raf-belt is-change" if change else "raf-belt"
        tl = '<span class="%s">%s%s</span>' % (cls, esc(title), " · new champion" if change else "")
    return ('<tr><td class="raf-wc">%s</td><td class="raf-vs">%s<span class="raf-d">def.</span>%s%s</td>'
            '<td class="raf-res">%s</td></tr>'
            % (esc(wc), acell, bcell, tl, res)) if (win and not upcoming) else (
           '<tr><td class="raf-wc">%s</td><td class="raf-vs">%s<span class="raf-d">vs.</span>%s%s</td>'
           '<td class="raf-res">%s</td></tr>' % (esc(wc), acell, bcell, tl, res))

def event_page(e, older, newer):
    slug = e["slug"]; up = e.get("upcoming")
    title = "%s Results: Full Card, %s | Wrestle Lore" % (e["name"], pretty(e["date"]))
    if up: title = "%s: Full Card and How to Watch, %s | Wrestle Lore" % (e["name"], pretty(e["date"]))
    desc = ("%s from %s in %s on %s. Every bout on the card, %s, sourced and dated."
            % (e["name"], e["venue"], e["city"], longdate(e["date"]),
               "with the announced lineup" if up else "with full results"))
    canonical = "%s/promotions/raf/%s/" % (BASE, slug)
    clips = CLIPS.get(slug, [])
    titles_on_line = [b for b in e["bouts"] if b[5]]
    changes = [b for b in e["bouts"] if b[6]]

    nav = []
    if newer: nav.append('<a class="link-more" href="/promotions/raf/%s/">Newer event</a>' % newer["slug"])
    nav.append('<a class="link-more" href="/promotions/raf/">All RAF events</a>')
    if older: nav.append('<a class="link-more" href="/promotions/raf/%s/">Older event</a>' % older["slug"])

    li = []
    for i, b in enumerate(e["bouts"], 1):
        li.append('{"@type":"ListItem","position":%d,"name":"%s vs. %s"}' % (i, esc(b[1]).replace('"','\\"'), esc(b[2]).replace('"','\\"')))
    jsonld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"SportsEvent",'
      '"name":"%s","startDate":"%s","eventStatus":"https://schema.org/EventScheduled",'
      '"eventAttendanceMode":"https://schema.org/OfflineEventAttendanceMode",'
      '"location":{"@type":"Place","name":"%s","address":"%s"},'
      '"organizer":{"@type":"SportsOrganization","name":"Real American Freestyle","url":"https://www.realamericanfreestyle.com/"},'
      '"url":"%s","description":"%s",'
      '"subEvent":{"@type":"ItemList","numberOfItems":%d,"itemListElement":[%s]}}</script>\n'
      '<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
      '{"@type":"ListItem","position":1,"name":"Home","item":"%s/"},'
      '{"@type":"ListItem","position":2,"name":"Promotions","item":"%s/promotions/"},'
      '{"@type":"ListItem","position":3,"name":"RAF","item":"%s/promotions/raf/"},'
      '{"@type":"ListItem","position":4,"name":"%s","item":"%s"}]}</script>\n'
      % (esc(e["name"]), e["date"], esc(e["venue"]), esc(e["city"]), canonical, esc(desc),
         len(e["bouts"]), ",".join(li), BASE, BASE, BASE, esc(e["name"]), canonical))

    hero = ('<div class="raf-hero">'
      '<p class="raf-kicker"><span class="raf-mark">RAF</span>%s</p>'
      '<h1 class="raf-h1">%s</h1>'
      '<p class="raf-tag">%s</p>'
      '<div class="raf-meta">'
      '<span><b>Date</b>%s</span><span><b>Venue</b>%s</span>'
      '<span><b>City</b>%s</span><span><b>Stream</b>%s</span></div>'
      '</div>' % ("Upcoming" if up else "Results",
                  esc(e["name"]), esc(e.get("tag","")),
                  longdate(e["date"]), esc(e["venue"]), esc(e["city"]), esc(e["stream"])))

    intro = '<p class="raf-note">%s</p>' % esc(e["note"]) if e.get("note") else ""

    stat = ('<div class="raf-stats"><div><b>%d</b>bouts</div><div><b>%d</b>title matches</div>'
            '<div><b>%d</b>%s</div></div>'
            % (len(e["bouts"]), len(titles_on_line), len(changes),
               "titles changed hands" if not up else "belts on the line"))

    rows = "".join(bout_row(b, up) for b in e["bouts"])
    card = ('<h2 class="raf-h2">%s</h2><div class="raf-tw"><table class="raf-card">'
            '<thead><tr><th>Division</th><th>Bout</th><th>Result</th></tr></thead>'
            '<tbody>%s</tbody></table></div>'
            % ("The card" if up else "Full results", rows))

    vid = ""
    if clips:
        vid = ('<h2 class="raf-h2">Watch</h2><p class="raf-sub">Official video from Real American Freestyle and Fox Nation.</p>'
               '<div class="raf-clips">%s</div>' % "".join(yt(v, l, e) for v, l in clips))

    watch = ('<div class="raf-watch"><b>Where to watch</b>'
             '<p>RAF streams exclusively on Fox Nation in the United States. It is a subscription, not a pay per view. '
             'The official RAF channel also posts full events on YouTube.</p>'
             '<a class="raf-cta" href="https://nation.foxnews.com/real-american-freestyle-nation/" target="_blank" rel="noopener">Fox Nation</a>'
             '<a class="raf-cta raf-cta--ghost" href="%s" target="_blank" rel="noopener">Source: %s</a></div>'
             % (esc(e["url"]), esc(e["src"])))

    main = ('<div class="raf">'
      '<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li>'
      '<li><a href="/promotions/">Promotions</a></li><li><a href="/promotions/raf/">RAF</a></li>'
      '<li aria-current="page">%s</li></ol></nav>'
      '%s%s%s%s%s%s'
      '<div class="raf-nav">%s</div></div>'
      % (esc(e["name"]), hero, intro, stat, card, vid, watch, " ".join(nav)))
    return shell(title, desc, canonical, main, extra_head=jsonld)

def hub_page():
    title = "Real American Freestyle (RAF): Every Event, Result and Champion | Wrestle Lore"
    desc = ("Real American Freestyle explained for wrestling fans. Every RAF card from RAF 01 to RAF 12, "
            "full results, current champions, and where to watch.")
    canonical = "%s/promotions/raf/" % BASE

    rows = []
    for e in EVENTS:
        up = e.get("upcoming")
        rows.append('<a class="raf-ev%s" href="/promotions/raf/%s/">'
          '<span class="raf-ev__n">%s</span>'
          '<span class="raf-ev__t">%s</span>'
          '<span class="raf-ev__d">%s</span>'
          '<span class="raf-ev__v">%s, %s</span>'
          '<span class="raf-ev__c">%s</span></a>'
          % (" is-up" if up else "", esc(e["slug"]), esc(e["name"]), esc(e.get("tag","")),
             pretty(e["date"]), esc(e["venue"]), esc(e["city"]),
             "Upcoming" if up else "%d bouts" % len(e["bouts"])))

    champ = "".join('<tr><td>%s</td><td class="%s">%s</td><td>%s</td></tr>'
                    % (esc(d), "raf-vac" if c == "Vacant" else "raf-n is-win", esc(c), esc(n))
                    for d, c, n in CHAMPIONS)

    faq = [
      ("What is Real American Freestyle?",
       "A freestyle wrestling league founded in 2025 by Chad Bronstein, Izzy Martinez, Eric Bischoff and Hulk Hogan. "
       "The matches are real freestyle wrestling with real scores, presented with pro wrestling stagecraft. Hogan died in July 2025, "
       "seven weeks before the first card, which opened with a tribute to him."),
      ("Is RAF scripted like WWE?",
       "No. RAF is unscripted competition scored under freestyle rules. What it borrows from pro wrestling is presentation: "
       "entrances, championships, rivalries and commentary."),
      ("How does freestyle scoring work?",
       "Points come from takedowns, exposure and pushouts. A wrestler who leads by ten points wins immediately by technical superiority, "
       "which appears in results as a tech fall. A pin still ends the match instantly, exactly as it does in pro wrestling."),
      ("Where can I watch RAF?",
       "Fox Nation carries every event exclusively in the United States on a subscription, not a pay per view. "
       "The official RAF YouTube channel also posts full events worldwide."),
      ("Do WWE or UFC wrestlers compete in RAF?",
       "UFC fighters compete regularly, including Colby Covington, Khamzat Chimaev, Merab Dvalishvili and Henry Cejudo, and there is a "
       "separate Crossover Championship for them. Gable Steveson, a former WWE Superstar and Olympic gold medallist, also competes."),
    ]
    faq_html = "".join('<details class="raf-faq"><summary>%s</summary><p>%s</p></details>' % (esc(q), esc(a)) for q, a in faq)
    faq_ld = ",".join('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
                      % (esc(q).replace('"','\\"'), esc(a).replace('"','\\"')) for q, a in faq)

    jsonld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"SportsOrganization",'
      '"name":"Real American Freestyle","alternateName":"RAF","sport":"Freestyle wrestling","foundingDate":"2025",'
      '"url":"https://www.realamericanfreestyle.com/","sameAs":["https://en.wikipedia.org/wiki/Real_American_Freestyle",'
      '"https://www.youtube.com/@RAFwrestling"]}</script>\n'
      '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s]}</script>\n'
      '<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
      '{"@type":"ListItem","position":1,"name":"Home","item":"%s/"},'
      '{"@type":"ListItem","position":2,"name":"Promotions","item":"%s/promotions/"},'
      '{"@type":"ListItem","position":3,"name":"RAF","item":"%s"}]}</script>\n' % (faq_ld, BASE, BASE, canonical))

    main = ('<div class="raf raf--hub">'
      '<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li>'
      '<li><a href="/promotions/">Promotions</a></li><li aria-current="page">RAF</li></ol></nav>'
      '<div class="raf-hero raf-hero--hub">'
      '<p class="raf-kicker"><span class="raf-mark">RAF</span>Real American Freestyle</p>'
      '<h1 class="raf-h1">Real wrestling, run like pro wrestling</h1>'
      '<p class="raf-lede">Olympic champions, NCAA champions and UFC fighters wrestling for real, on a card built like a wrestling show. '
      'Founded by Hulk Hogan and Eric Bischoff in 2025. %d cards wrestled, %d announced, every one of them here.</p>'
      '</div>'
      '<div class="raf-stats raf-stats--hub"><div><b>%d</b>events</div><div><b>%d</b>bouts on record</div>'
      '<div><b>13</b>championships</div><div><b>Fox Nation</b>exclusive stream</div></div>'
      '<h2 class="raf-h2">Every event</h2>'
      '<div class="raf-evs">%s</div>'
      '<h2 class="raf-h2">Current champions</h2>'
      '<div class="raf-tw"><table class="raf-card"><thead><tr><th>Division</th><th>Champion</th><th>Notes</th></tr></thead>'
      '<tbody>%s</tbody></table></div>'
      '<h2 class="raf-h2">Athlete files</h2>'
      '<p class="raf-sub">Tsarukyan, everyone he has met on an RAF mat, and the other crossover fighters this section already tracks. Each file carries the full RAF record with every match linked to its card.</p>'
      '<div class="raf-evs">%s</div>'
      '<h2 class="raf-h2">Questions fans actually ask</h2>%s'
      '<p class="raf-colophon">Wrestle Lore is an independent, fan made project and is not affiliated with Real American Freestyle, '
      'WWE, TKO Group Holdings, AEW, TNA or NJPW. Results are filed from USA Wrestling, FloWrestling and Real American Freestyle, and every '
      'video is embedded from an official channel.</p>'
      '</div>'
      % (len([e for e in EVENTS if not e.get("upcoming")]), len([e for e in EVENTS if e.get("upcoming")]),
         len(EVENTS), sum(len(e["bouts"]) for e in EVENTS), "".join(rows), champ,
         "".join('<a class="raf-ev" href="/promotions/raf/athletes/%s/">'
                 '<span class="raf-ev__n">%s</span><span class="raf-ev__t">%s</span>'
                 '<span class="raf-ev__v">%s</span><span class="raf-ev__c">Full record</span></a>'
                 % (a["slug"], esc(a["name"]), esc(a["tagline"]),
                    "%s in RAF" % a["rafstats"][0][0]) for a in ATHLETES),
         faq_html))
    return shell(title, desc, canonical, main, extra_head=jsonld)

# ------------------------------------------------------------------ SHELL
def shell(title, desc, canonical, main, extra_head="", profile_css=False):
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
      '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
      '<title>%s</title>\n<meta name="description" content="%s">\n<link rel="canonical" href="%s">\n'
      '<meta name="robots" content="index,follow">\n'
      '<meta property="og:type" content="website">\n<meta property="og:title" content="%s">\n'
      '<meta property="og:description" content="%s">\n<meta property="og:url" content="%s">\n'
      '<meta property="og:site_name" content="Wrestle Lore">\n%s'
      '<link rel="stylesheet" href="/css/site.css">\n'
      '%s</head>\n<body>\n'
      '<header class="site-header nav7"></header>\n<main id="main">\n%s\n</main>\n'
      '<footer class="site-footer site-footer--fat"></footer>\n'
      '<script src="/js/main.js" defer></script>\n<script src="/js/nav.js" defer></script>\n'
      '<script src="/js/media.js" defer></script>\n</body>\n</html>\n'
      % (esc(title), esc(desc), canonical, esc(title), esc(desc), canonical, extra_head,
         '<link rel="stylesheet" href="/css/profile.css">\n' if profile_css else "", main))

# ------------------------------------------------------------------ CSS
RAF_CSS = """
/* ==== RAF (generated by build/build_raf.py — do not hand-edit) ==== */
:root{--c-raf:#2E5FA3;--c-raf-b:#5B93D6;--raf:#2E5FA3}
.raf{max-width:1180px;margin:0 auto;padding:0 clamp(16px,3vw,32px) 96px}
.raf .raf-hero{padding:26px 0 22px;border-bottom:1px solid var(--c-line)}
.raf-kicker{display:flex;align-items:center;gap:12px;font:600 12px/1 var(--f-mono,monospace);
  letter-spacing:.16em;text-transform:uppercase;color:var(--c-gold);margin:0 0 14px}
.raf-mark{display:inline-block;background:var(--c-raf);color:#fff;padding:5px 9px;letter-spacing:.14em;font-weight:800}
.raf-h1{font-family:var(--f-display,inherit);font-size:clamp(38px,7vw,74px);line-height:.96;margin:0 0 10px;letter-spacing:-.02em}
.raf-tag{font-size:19px;color:var(--c-gold);margin:0 0 18px;letter-spacing:.02em}
.raf-lede{font-size:19px;line-height:1.6;color:var(--c-ink-2,#b9c2cb);max-width:62ch;margin:0}
.raf-meta{display:flex;flex-wrap:wrap;gap:26px}
.raf-meta span{display:flex;flex-direction:column;gap:4px;font-size:15px}
.raf-meta b{font:600 10.5px/1 var(--f-mono,monospace);letter-spacing:.14em;text-transform:uppercase;color:var(--c-ink-3,#8892a0)}
.raf-note{font-size:17px;line-height:1.6;color:var(--c-ink-2,#b9c2cb);max-width:66ch;margin:22px 0 0;
  border-left:3px solid var(--c-raf);padding-left:16px}
.raf-stats{display:flex;flex-wrap:wrap;gap:1px;background:var(--c-line);border:1px solid var(--c-line);margin:26px 0 0}
.raf-stats div{flex:1 1 150px;background:var(--c-bg);padding:14px 16px;display:flex;flex-direction:column;gap:5px;
  font:500 11px/1.3 var(--f-mono,monospace);letter-spacing:.11em;text-transform:uppercase;color:var(--c-ink-3,#8892a0)}
.raf-stats b{font-family:var(--f-display,inherit);font-size:27px;letter-spacing:-.01em;color:var(--c-gold);text-transform:none}
.raf-h2{font-family:var(--f-display,inherit);font-size:clamp(24px,3.4vw,34px);margin:46px 0 6px;letter-spacing:-.015em}
.raf-sub{font-size:15px;color:var(--c-ink-3,#8892a0);margin:0 0 16px}
.raf-tw{overflow-x:auto;border:1px solid var(--c-line);margin:18px 0 0}
table.raf-card{border-collapse:collapse;width:100%;min-width:640px;font-size:15px}
table.raf-card th{font:600 10.5px/1 var(--f-mono,monospace);letter-spacing:.12em;text-transform:uppercase;
  color:var(--c-ink-3,#8892a0);text-align:left;padding:13px 16px;border-bottom:1px solid var(--c-line);white-space:nowrap}
table.raf-card td{padding:13px 16px;border-bottom:1px solid var(--c-line-soft,rgba(255,255,255,.06));vertical-align:top}
table.raf-card tbody tr:last-child td{border-bottom:none}
.raf-wc{font:500 12px/1.4 var(--f-mono,monospace);letter-spacing:.06em;color:var(--c-ink-3,#8892a0);white-space:nowrap}
.raf-vs{line-height:1.7}
.raf-n{font-weight:600}
.raf-n.is-win{color:var(--c-gold)}
.raf-d{display:inline-block;margin:0 9px;font:500 11px/1 var(--f-mono,monospace);
  letter-spacing:.1em;text-transform:uppercase;color:var(--c-ink-3,#8892a0)}
.raf-belt{display:block;margin-top:6px;font:600 10.5px/1.4 var(--f-mono,monospace);letter-spacing:.1em;
  text-transform:uppercase;color:var(--c-raf-b)}
.raf-belt.is-change{color:var(--c-gold)}
.raf-res{font:500 13.5px/1.5 var(--f-mono,monospace);white-space:nowrap;color:var(--c-ink-2,#b9c2cb)}
.raf-tbd{color:var(--c-ink-3,#8892a0);font-style:italic}
.raf-vac{color:var(--c-ink-3,#8892a0);font-style:italic}
.raf-clips{display:grid;grid-template-columns:repeat(auto-fill,minmax(258px,1fr));gap:16px;margin-top:6px}
.raf-vcard{min-width:0}
.raf-watch{margin-top:44px;border:1px solid var(--c-line);border-top:3px solid var(--c-raf);padding:22px 24px}
.raf-watch b{display:block;font:600 10.5px/1 var(--f-mono,monospace);letter-spacing:.14em;
  text-transform:uppercase;color:var(--c-gold);margin-bottom:10px}
.raf-watch p{margin:0 0 16px;max-width:64ch;font-size:15.5px;line-height:1.6;color:var(--c-ink-2,#b9c2cb)}
.raf-cta{display:inline-block;margin:0 10px 0 0;padding:10px 18px;border:1px solid var(--c-raf-b);
  color:var(--c-raf-b);font:600 12px/1 var(--f-mono,monospace);letter-spacing:.1em;text-transform:uppercase;text-decoration:none}
.raf-cta:hover{background:var(--c-raf);border-color:var(--c-raf);color:#fff}
.raf-cta--ghost{border-color:var(--c-line);color:var(--c-ink-3,#8892a0)}
.raf-nav{display:flex;flex-wrap:wrap;gap:20px;margin-top:40px;padding-top:22px;border-top:1px solid var(--c-line)}
.raf-evs{display:grid;grid-template-columns:repeat(auto-fill,minmax(268px,1fr));gap:1px;
  background:var(--c-line);border:1px solid var(--c-line);margin-top:18px}
.raf-ev{display:flex;flex-direction:column;gap:5px;background:var(--c-bg);padding:18px 20px;text-decoration:none;
  transition:background .16s ease}
.raf-ev:hover{background:var(--c-bg-2,rgba(255,255,255,.04))}
.raf-ev.is-up{border-left:3px solid var(--c-gold)}
.raf-ev__n{font-family:var(--f-display,inherit);font-size:23px;letter-spacing:-.01em;color:var(--c-ink,#e8edf1)}
.raf-ev__t{font-size:15px;color:var(--c-gold)}
.raf-ev__d{font:500 11.5px/1 var(--f-mono,monospace);letter-spacing:.1em;text-transform:uppercase;color:var(--c-ink-3,#8892a0);margin-top:3px}
.raf-ev__v{font-size:13.5px;color:var(--c-ink-3,#8892a0)}
.raf-ev__c{font:600 10.5px/1 var(--f-mono,monospace);letter-spacing:.12em;text-transform:uppercase;color:var(--c-raf-b);margin-top:4px}
.raf-faq{border:1px solid var(--c-line);margin-bottom:8px;background:var(--c-bg)}
.raf-faq summary{cursor:pointer;padding:15px 18px;font-weight:600;font-size:16.5px;list-style:none}
.raf-faq summary::-webkit-details-marker{display:none}
.raf-faq summary::after{content:"+";float:right;color:var(--c-raf-b);font-weight:400}
.raf-faq[open] summary::after{content:"\\2013"}
.raf-faq p{margin:0;padding:0 18px 17px;font-size:15.5px;line-height:1.65;color:var(--c-ink-2,#b9c2cb);max-width:70ch}
.chip--raf{background:rgba(46,95,163,.16);color:var(--c-raf-b);border-color:rgba(46,95,163,.5)}
.raf-now{margin:22px 0 0;padding:12px 18px;border:1px solid var(--c-gold-dim,rgba(212,175,55,.4));font:600 12.5px/1.5 var(--f-mono,monospace);letter-spacing:.06em;color:var(--c-gold);display:inline-block}
.raf-p{font-size:16.5px;line-height:1.72;color:var(--c-ink-2,#b9c2cb);max-width:70ch;margin:0 0 15px}
.raf-correct{margin:26px 0 0;border-left:3px solid var(--c-raf-b);padding:16px 20px;background:var(--c-bg-2,rgba(255,255,255,.03))}
.raf-correct b{display:block;font:600 10.5px/1 var(--f-mono,monospace);letter-spacing:.14em;text-transform:uppercase;color:var(--c-raf-b);margin-bottom:9px}
.raf-correct p{margin:0;font-size:15.5px;line-height:1.65;color:var(--c-ink-2,#b9c2cb);max-width:72ch}
.raf-res-l{font-weight:600;color:var(--c-loss,#c4574d)}
.raf-stats--ath{margin:24px 0 0}
.raf-stats--ath b{color:var(--c-raf-b)}
.rec2-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(96px,1fr));gap:10px;margin:2px 0 18px}
.rec2-stat{background:#12141a;border:1px solid rgba(255,255,255,.06);border-radius:10px;padding:11px 13px;display:flex;flex-direction:column;gap:3px}
.rec2-stat b{font-family:var(--f-display,inherit);font-size:22px;line-height:1;color:var(--c-gold);letter-spacing:-.01em}
.rec2-stat span{font:500 10.5px/1.3 var(--f-mono,monospace);letter-spacing:.1em;text-transform:uppercase;color:var(--c-ink-3,#8892a0)}
@media (max-width:640px){.rec2-stats{grid-template-columns:repeat(2,1fr)}}
.raf-colophon{margin-top:52px;padding-top:20px;border-top:1px solid var(--c-line);
  font-size:13px;line-height:1.7;color:var(--c-ink-3,#8892a0);max-width:82ch}
@media (max-width:640px){
  .raf-meta{gap:16px}
  .raf-clips{grid-template-columns:1fr 1fr}
}
/* ==== /RAF ==== */
"""

def inject_css():
    p = os.path.join(ROOT, "css", "site.css")
    css = open(p, encoding="utf-8").read()
    blk = RAF_CSS.strip("\n")
    pat = re.compile(r"/\* ==== RAF \(generated.*?/\* ==== /RAF ==== \*/", re.S)
    new = pat.sub(lambda m: blk, css) if pat.search(css) else css.rstrip() + "\n\n" + blk + "\n"
    if new != css:
        open(p, "w", encoding="utf-8").write(new); print("css/site.css: RAF block written")
    else:
        print("css/site.css: RAF block already current")

def write(rel, htmlstr):
    p = os.path.join(ROOT, rel.lstrip("/"))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    old = open(p, encoding="utf-8").read() if os.path.exists(p) else None
    if old != htmlstr:
        open(p, "w", encoding="utf-8").write(htmlstr)

def update_sitemap():
    p = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(p): return
    xml = open(p, encoding="utf-8").read()
    urls = ["%s/promotions/raf/" % BASE] + ["%s/promotions/raf/%s/" % (BASE, e["slug"]) for e in EVENTS]\
           + ["%s/promotions/raf/athletes/%s/" % (BASE, a["slug"]) for a in ATHLETES]
    add = [u for u in urls if u not in xml]
    if not add:
        print("sitemap: RAF urls already present"); return
    today = TODAY.isoformat()
    blk = "".join('<url><loc>%s</loc><lastmod>%s</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>\n' % (u, today) for u in add)
    xml = xml.replace("</urlset>", blk + "</urlset>")
    open(p, "w", encoding="utf-8").write(xml)
    print("sitemap +%d RAF urls" % len(add))

def patch_promotions_index():
    """RAF gets two entry points, and neither one widens the top-level nav.

    1. components/meganav.html  -> the .bcard grid inside the Promotions mega menu.
       That grid is stamped into every page's <header> by apply_shell.py, so it MUST be
       edited at the component. An earlier version edited promotions/index.html directly
       and apply_shell silently reverted it on the next run.
    2. promotions/index.html    -> the .card list in <main>, the actual directory page.
    """
    # ---- 1. the mega menu component
    p = os.path.join(ROOT, "components", "meganav.html")
    if os.path.exists(p):
        nav = open(p, encoding="utf-8").read()
        if 'href="/promotions/raf/"' in nav:
            print("meganav: RAF card already present")
        else:
            cards = list(re.finditer(r'<a class="dk bcard"[^>]*>.*?</a>', nav, re.S))
            if cards:
                card = ('\n              <a class="dk bcard" href="/promotions/raf/" style="--pc:var(--raf)">\n'
                        '              <span class="klbl">EST. 2025 // REAL COMPETITION</span>\n'
                        '              <div class="bnm">RAF</div>\n'
                        '              <span class="bys">OLYMPIC AND NCAA CHAMPIONS, FOR REAL</span>\n'
                        '              <span class="stream">LIVE ON FOX NATION</span>\n'
                        '            </a>')
                e = cards[-1].end()
                open(p, "w", encoding="utf-8").write(nav[:e] + card + nav[e:])
                print("meganav: RAF card added to the Promotions menu (%d cards there now)" % (len(cards)+1))
            else:
                print("WARN: no .bcard grid in components/meganav.html")

    # ---- 2. the /promotions/ directory page body
    p = os.path.join(ROOT, "promotions", "index.html")
    if not os.path.exists(p):
        print("WARN: promotions/index.html not found"); return
    html = open(p, encoding="utf-8").read()
    mn, ftr = html.find("<main"), html.find("<footer")
    if mn < 0 or ftr < 0: 
        print("WARN: promotions/index.html has no <main>"); return
    body = html[mn:ftr]
    if 'href="/promotions/raf/"' in body:
        print("promotions page: RAF card already present"); return
    cards = list(re.finditer(r'<a class="card" href="/promotions/[a-z]+/"[^>]*>.*?</a>', body, re.S))
    if not cards:
        print("WARN: no .card list in promotions/index.html <main>"); return
    card = ('<a class="card" href="/promotions/raf/" style="text-decoration:none;color:inherit">'
            '<div class="card__body stack"><span class="chip chip--raf">RAF</span>'
            '<h3 style="font-size:var(--fs-500)">Real American Freestyle</h3>'
            '<p class="muted">Real freestyle wrestling run like a wrestling show. '
            'Olympic and NCAA champions against UFC fighters, founded by Hogan and Bischoff.</p>'
            '</div></a>')
    e = mn + cards[-1].end()
    html = html[:e] + card + html[e:]
    # adding a card breaks the lede's count; fix the sentence in the same pass
    old_lede = ("Wrestle Lore covers the five promotions that defined modern professional wrestling "
                "(1997&ndash;present):")
    for variant in (old_lede, old_lede.replace("&ndash;", "\u2013"), old_lede.replace("&ndash;", "-")):
        if variant in html:
            html = html.replace(variant, variant.replace("the five promotions that defined modern professional wrestling",
                                                         "the promotions that defined modern professional wrestling"), 1)
            print("promotions page: lede count corrected")
            break
    open(p, "w", encoding="utf-8").write(html)
    print("promotions page: RAF card added to the directory (after %d cards)" % len(cards))

if __name__ == "__main__":
    inject_css()
    n = 0
    for i, e in enumerate(EVENTS):
        newer = EVENTS[i-1] if i > 0 else None
        older = EVENTS[i+1] if i < len(EVENTS)-1 else None
        write("/promotions/raf/%s/index.html" % e["slug"], event_page(e, older, newer)); n += 1
    write("/promotions/raf/index.html", hub_page())
    for a in ATHLETES:
        write("/promotions/raf/athletes/%s/index.html" % a["slug"], athlete_page(a))
    patch_promotions_index()
    update_sitemap()
    print("done: RAF hub + %d event pages (%d bouts, %d clips) ROOT=%s"
          % (n, sum(len(e["bouts"]) for e in EVENTS), sum(len(v) for v in CLIPS.values()), ROOT))
    print("now run: python3 build/apply_shell.py")
