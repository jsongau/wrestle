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
 dict(slug="raf-12", name="RAF 12", date="2026-08-22", venue="Rocket Arena", city="Cleveland, OH",
      stream="Fox Nation", tag="Dvalishvili vs. Cejudo 2", upcoming=True,
      src="Real American Freestyle", url="https://www.realamericanfreestyle.com/events/raf12",
      note="RAF's one year anniversary card, back in the city where the league debuted.",
      bouts=[
        ("Lightweight","Merab Dvalishvili","Henry Cejudo",None,None,"Crossover Lightweight Championship",None),
        ("Cruiserweight","Jordan Burroughs","Sean Brady",None,None,None,None),
        ("Heavyweight","Gable Steveson","Anthony Cassioppi",None,None,None,None),
        ("Middleweight","Evan Wick","Jason Nolf",None,None,"Middleweight Championship",None),
        ("Welterweight","David Carr","Tajmuraz Salkazanov",None,None,"Welterweight Championship",None),
        ("Light Heavyweight","Bo Nickal","Max McEnelly",None,None,None,None),
        ("Women's Catchweight","Kennedy Blades","Reese Larramendy",None,None,None,None),
        ("Cruiserweight","Tyron Woodley","Joaquin Buckley",None,None,None,None),
        ("Featherweight","Vladimer Khinchegashvili","Jesse Mendez",None,None,None,None),
        ("Featherweight","Johnni DiJulius","Asu Almabayev",None,None,None,None),
        ("Middleweight","Mahamedkhabib Kadzimahamedau","Will Lewan",None,None,None,None),
        ("Bantamweight","Masanosuke Ono","Ben Davino",None,None,None,None),
      ]),
 dict(slug="raf-11", name="RAF 11", date="2026-07-18", venue="UW-Milwaukee Panther Arena", city="Milwaukee, WI",
      stream="Fox Nation", tag="Tsarukyan vs. Covington",
      src="USA Wrestling", url="https://www.themat.com/news/2026/july/21/ben-askren-concludes-historic-wrestling-career-adeline-gray-and-trent-hidlay-pick-up-victories-at-raf11",
      note="Ben Askren closed his career here, leaving his boots on the mat after a comeback from a double lung transplant.",
      bouts=[
        ("Cruiserweight","Arman Tsarukyan","Colby Covington","Colby Covington","dec 5-3","Crossover Cruiserweight Championship",True),
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
      note="A post-match brawl between Tsarukyan and Poullas set up the RAF 07 rematch.",
      bouts=[
        ("Lightweight","Henry Cejudo","Urijah Faber","Henry Cejudo","tech fall 11-0",None,False),
        ("Middleweight","Arman Tsarukyan","Georgio Poullas","Arman Tsarukyan","dec 5-3",None,False),
        ("Middleweight","Aljamain Sterling","Benson Henderson","Aljamain Sterling","tech fall",None,False),
        ("Welterweight","David Carr","Bubba Jenkins","David Carr","tech fall 13-2","Welterweight Championship",False),
        ("Featherweight","Andrew Alirez","Bryce Meredith","Andrew Alirez","tech fall 13-2",None,False),
        ("Light Heavyweight","Givi Matcharashvili","Stephen Buchanan","Givi Matcharashvili","dec 3-3 on criteria",None,False),
        ("Women's Strawweight","Lucia Yepez","Everest Leydecker","Lucia Yepez","dec 10-3",None,False),
        ("Middleweight","Tajmuraz Salkazanov","Keegan O'Toole","Tajmuraz Salkazanov","dec 9-0",None,False),
        ("Middleweight","Evan Wick","Mahamedkhabib Kadzimahamedau","Evan Wick","tech fall 13-2",None,False),
        ("Cruiserweight","Zahid Valencia","Mahmoud Fawzy Sebie","Zahid Valencia","tech fall 10-0",None,False),
        ("Welterweight","Keelon Jimison","Clay Guida","Keelon Jimison","tech fall",None,False),
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
 dict(slug="arman-tsarukyan", name="Arman Tsarukyan", nick="Ahalkalakets",
      tagline="The UFC lightweight who wrestles for real",
      bornplace="Akhalkalaki, Georgia", nationality="Armenian", dob="1996-10-11",
      height="5 ft 7 in", reach="72.5 in", division="Lightweight", team="American Top Team",
      coach="Marcos da Matta", division_raf="Middleweight",
      stats=[("23-3","Pro MMA record"),("10-2","UFC record"),("7-1","RAF record"),("#2","UFC lightweight")],
      now="Ranked number two at lightweight. Faces Mauricio Ruffy at UFC 331 on September 19.",
      bio=[
        "Arman Tsarukyan is the clearest example of what Real American Freestyle was built to do. He is a top two UFC lightweight who spends the gaps between fights wrestling actual freestyle matches, and he has been the most active crossover athlete on the RAF roster since January 2026.",
        "He was born in Akhalkalaki, Georgia, to an Armenian family, and played junior ice hockey for six years before choosing combat sport at seventeen. He turned professional in MMA in 2015 and arrived in the UFC in 2019 on short notice, losing a Fight of the Night decision to Islam Makhachev on debut. He has lost once since.",
        "His RAF run has been lopsided. Seven of his first eight matches were wins, five of them technical falls, which in freestyle means a ten point lead ends the match early. The exception is the one that mattered most: Colby Covington beat him 5-2 at RAF 11 for the inaugural Crossover Championship, handing him his first RAF loss.",
        "He is also the reason RAF got its first genuine pull apart brawl. After beating Georgio Poullas at RAF 06 he shoved and punched him, and both corners spilled onto the mat.",
      ],
      correction=("A note on the record. Tsarukyan and Islam Makhachev have fought once, in 2019, and Makhachev won. "
                  "A second fight was booked for the lightweight title at UFC 311 in January 2025 and Tsarukyan withdrew the day before with a back injury. "
                  "It is often written up as a series. It is not one."),
      raf=[  # (event slug, date, opponent, win?, method, note)
        ("raf-14","2026-10-03","Dillon Danis",None,"Crossover middleweight title","Announced"),
        ("raf-11","2026-07-18","Colby Covington",False,"dec 2-5","Crossover Championship"),
        ("raf-georgia","2026-07-11","Kuat Khamitov",True,"tech fall 11-0",""),
        ("raf-10","2026-06-13","Tony Ferguson",True,"tech fall 10-0",""),
        ("raf-09","2026-05-30","Keelon Jimison",True,"tech fall 16-5",""),
        ("raf-08","2026-04-18","Urijah Faber",True,"tech fall 13-1",""),
        ("raf-07","2026-03-28","Georgio Poullas",True,"dec 9-3","Rematch"),
        ("raf-06","2026-02-28","Georgio Poullas",True,"dec 5-3","Brawl after the bell"),
        ("raf-05","2026-01-10","Lance Palmer",True,"tech fall 10-0",""),
      ],
      ufc=[  # (date, opponent, win?, method, rd, time, event)
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
      grappling="Submission grappling record of 4-0-1, including a technical decision over Benson Henderson and a fifth round rear naked choke on Patricky Freire at ADXC 10 in May 2025.",
      background=("His wrestling background is real but thinner than the reputation suggests, and it is worth being exact about it. "
                  "He holds Master of Sport rank in freestyle wrestling and a second in mixed martial arts. No world, European or national "
                  "championship medal appears in any published record. Armenian coverage has framed a European Championship run as something "
                  "he could still do, not something he has done."),
      srcs=[("UFC.com","https://www.ufc.com/athlete/arman-tsarukyan"),
            ("Wikipedia","https://en.wikipedia.org/wiki/Arman_Tsarukyan"),
            ("Sherdog","https://www.sherdog.com/fighter/Arman-Tsarukyan-213913"),
            ("RAF athlete page","https://www.realamericanfreestyle.com/athletes/arman-tsarukyan")]),
]
EVENT_BY_SLUG = {e["slug"]: e for e in EVENTS}

def _age(dob):
    d = d2(dob)
    return TODAY.year - d.year - ((TODAY.month, TODAY.day) < (d.month, d.day))

def athlete_page(a):
    title = "%s: RAF Record, UFC Record and Bio | Wrestle Lore" % a["name"]
    desc = ("%s, the UFC lightweight who competes in Real American Freestyle. Complete RAF record, "
            "every UFC fight, and how the two careers run alongside each other." % a["name"])
    canonical = "%s/promotions/raf/athletes/%s/" % (BASE, a["slug"])

    stats = "".join('<div><b>%s</b>%s</div>' % (esc(v), esc(l)) for v, l in a["stats"])

    rrows = []
    for slug, date, opp, win, method, note in a["raf"]:
        ev = EVENT_BY_SLUG.get(slug)
        evcell = ('<a href="/promotions/raf/%s/">%s</a>' % (slug, esc(ev["name"]))) if ev else esc(slug.upper().replace("-", " "))
        if win is None:
            res = '<span class="raf-tbd">Announced</span>'
        else:
            res = '<span class="raf-n is-win">Win</span>' if win else '<span class="raf-res-l">Loss</span>'
        rrows.append('<tr><td class="raf-wc">%s</td><td>%s</td><td class="raf-vs"><span class="raf-n">%s</span>%s</td>'
                     '<td class="raf-res">%s</td><td class="raf-res">%s</td></tr>'
                     % (pretty(date), evcell, esc(opp),
                        ('<span class="raf-belt">%s</span>' % esc(note)) if note else "", res, esc(method)))

    urows = []
    for date, opp, win, method, rd, tm, event in a["ufc"]:
        urows.append('<tr><td class="raf-wc">%s</td><td class="raf-vs"><span class="raf-n%s">%s</span></td>'
                     '<td class="raf-res">%s</td><td class="raf-res">%s</td><td class="raf-res">%s</td>'
                     '<td class="raf-wc">%s</td></tr>'
                     % (pretty(date), " is-win" if win else "", esc(opp),
                        '<span class="raf-n is-win">Win</span>' if win else '<span class="raf-res-l">Loss</span>',
                        esc(method), "R%s %s" % (esc(rd), esc(tm)), esc(event)))

    srcs = " ".join('<a href="%s" target="_blank" rel="noopener">%s</a>' % (esc(u), esc(n)) for n, u in a["srcs"])

    jsonld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Person",'
      '"name":"%s","alternateName":"%s","birthDate":"%s","birthPlace":{"@type":"Place","name":"%s"},'
      '"nationality":"%s","jobTitle":"Mixed martial artist and freestyle wrestler","url":"%s",'
      '"affiliation":[{"@type":"SportsOrganization","name":"Real American Freestyle"},'
      '{"@type":"SportsOrganization","name":"Ultimate Fighting Championship"}],"sameAs":[%s]}</script>\n'
      '<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
      '{"@type":"ListItem","position":1,"name":"Home","item":"%s/"},'
      '{"@type":"ListItem","position":2,"name":"Promotions","item":"%s/promotions/"},'
      '{"@type":"ListItem","position":3,"name":"RAF","item":"%s/promotions/raf/"},'
      '{"@type":"ListItem","position":4,"name":"%s","item":"%s"}]}</script>\n'
      % (esc(a["name"]), esc(a["nick"]), a["dob"], esc(a["bornplace"]), esc(a["nationality"]), canonical,
         ",".join('"%s"' % u for _, u in a["srcs"]), BASE, BASE, BASE, esc(a["name"]), canonical))

    bio = "".join('<p class="raf-p">%s</p>' % esc(x) for x in a["bio"])

    main = ('<div class="raf raf--athlete">'
      '<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li>'
      '<li><a href="/promotions/">Promotions</a></li><li><a href="/promotions/raf/">RAF</a></li>'
      '<li aria-current="page">%s</li></ol></nav>'
      '<div class="raf-hero">'
      '<p class="raf-kicker"><span class="raf-mark">RAF</span>%s</p>'
      '<h1 class="raf-h1">%s</h1><p class="raf-tag">%s</p>'
      '<div class="raf-meta">'
      '<span><b>Born</b>%s, %s</span><span><b>Age</b>%d</span><span><b>Height</b>%s</span>'
      '<span><b>Reach</b>%s</span><span><b>UFC division</b>%s</span><span><b>RAF division</b>%s</span>'
      '<span><b>Team</b>%s</span></div></div>'
      '<div class="raf-now">%s</div>'
      '<div class="raf-stats raf-stats--ath">%s</div>'
      '<h2 class="raf-h2">Overview</h2>%s'
      '<div class="raf-correct"><b>Setting one thing straight</b><p>%s</p></div>'
      '<h2 class="raf-h2">RAF record</h2>'
      '<p class="raf-sub">%s in Real American Freestyle. Every match links to the full card.</p>'
      '<div class="raf-tw"><table class="raf-card"><thead><tr><th>Date</th><th>Event</th><th>Opponent</th>'
      '<th>Result</th><th>Method</th></tr></thead><tbody>%s</tbody></table></div>'
      '<h2 class="raf-h2">UFC record</h2>'
      '<p class="raf-sub">%s in the UFC, %s as a professional. Debut April 2019.</p>'
      '<div class="raf-tw"><table class="raf-card"><thead><tr><th>Date</th><th>Opponent</th><th>Result</th>'
      '<th>Method</th><th>Round</th><th>Event</th></tr></thead><tbody>%s</tbody></table></div>'
      '<h2 class="raf-h2">Wrestling and grappling background</h2>'
      '<p class="raf-p">%s</p><p class="raf-p">%s</p>'
      '<div class="raf-watch"><b>Sources</b><p>Every figure on this page traces to a published record. '
      'Where sources disagree, the disagreement is stated rather than smoothed over.</p>%s</div>'
      '<div class="raf-nav"><a class="link-more" href="/promotions/raf/">All RAF events</a>'
      '<a class="link-more" href="/promotions/raf/raf-11/">His RAF title match</a></div>'
      '<p class="raf-colophon">Wrestle Lore is an independent, fan made project and is not affiliated with Real American '
      'Freestyle, the UFC, WWE, TKO Group Holdings, AEW, TNA or NJPW.</p>'
      '</div>'
      % (esc(a["name"]), esc(a["tagline"]), esc(a["name"]), esc(a["nick"]),
         esc(a["bornplace"]), esc(a["nationality"]), _age(a["dob"]), esc(a["height"]), esc(a["reach"]),
         esc(a["division"]), esc(a["division_raf"]), esc(a["team"]),
         esc(a["now"]), stats, bio, esc(a["correction"]),
         a["stats"][2][0], "".join(rrows), a["stats"][1][0], a["stats"][0][0], "".join(urows),
         esc(a["background"]), esc(a["grappling"]), srcs))
    return shell(title, desc, canonical, main, extra_head=jsonld)

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
        acell = '<span class="raf-n">%s</span>' % esc(a)
        bcell = '<span class="raf-n">%s</span>' % esc(bb)
    else:
        loser = bb if win == a else a
        acell = '<span class="raf-n is-win">%s</span>' % esc(win)
        bcell = '<span class="raf-n">%s</span>' % esc(loser)
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
      'Founded by Hulk Hogan and Eric Bischoff in 2025. Thirteen events in, every one of them here.</p>'
      '</div>'
      '<div class="raf-stats raf-stats--hub"><div><b>%d</b>events</div><div><b>%d</b>bouts on record</div>'
      '<div><b>13</b>championships</div><div><b>Fox Nation</b>exclusive stream</div></div>'
      '<h2 class="raf-h2">Every event</h2>'
      '<div class="raf-evs">%s</div>'
      '<h2 class="raf-h2">Current champions</h2>'
      '<div class="raf-tw"><table class="raf-card"><thead><tr><th>Division</th><th>Champion</th><th>Notes</th></tr></thead>'
      '<tbody>%s</tbody></table></div>'
      '<h2 class="raf-h2">Athlete files</h2>'
      '<p class="raf-sub">Crossover competitors with a record in more than one sport.</p>'
      '<div class="raf-evs">%s</div>'
      '<h2 class="raf-h2">Questions fans actually ask</h2>%s'
      '<p class="raf-colophon">Wrestle Lore is an independent, fan made project and is not affiliated with Real American Freestyle, '
      'WWE, TKO Group Holdings, AEW, TNA or NJPW. Results are filed from USA Wrestling, FloWrestling and Real American Freestyle, and every '
      'video is embedded from an official channel.</p>'
      '</div>'
      % (len(EVENTS), sum(len(e["bouts"]) for e in EVENTS), "".join(rows), champ,
         "".join('<a class="raf-ev" href="/promotions/raf/athletes/%s/">'
                 '<span class="raf-ev__n">%s</span><span class="raf-ev__t">%s</span>'
                 '<span class="raf-ev__v">%s</span><span class="raf-ev__c">Full record</span></a>'
                 % (a["slug"], esc(a["name"]), esc(a["tagline"]),
                    " and ".join(x[0] for x in a["stats"][:3])) for a in ATHLETES),
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
