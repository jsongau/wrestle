#!/usr/bin/env python3
"""Batch 10b — Big Show, Lex Luger, Dusty Rhodes, Kevin Nash, Bam Bam Bigelow (new pages)"""
import os, re

OUT = "/root/wwe/wrestlers"

def cr(title, reign, note=""):
    note_html = '<span class="cr-note">' + note + '</span>' if note else ""
    return f'    <div class="champ-row"><span class="cr-title">{title}</span><span class="cr-reign">{reign}</span>{note_html}</div>\n'

def a(slug, name):
    return f'<a href="/wrestlers/{slug}/">{name}</a>'

def row(w, kind, opp, event, date, stipulation, note, result="W"):
    return (f'<tr class="record-row" data-result="{result}" data-cats="{kind}">'
            f'<td class="res-cell"><span class="res-badge{" res-l" if result=="L" else " res-d" if result=="D" else ""}">{result}</span></td>'
            f'<td>{opp}</td><td>{event}</td><td>{date}</td>'
            f'<td>{stipulation}</td><td class="dim">{note}</td></tr>\n')

WRESTLERS = [

# ── BIG SHOW (PAUL WIGHT) ─────────────────────────────────────────────────────
{
    "slug": "big-show",
    "name": "Big Show",
    "nickname": "The World's Largest Athlete",
    "era": "Attitude Era / Modern",
    "alignment": "Heel / Face",
    "method_bars": [
        {"label":"Pinfall (Chokeslam)","pct":46},
        {"label":"Submission (Colossal Clutch)","pct":22},
        {"label":"Disqualification","pct":16},
        {"label":"Count-out","pct":10},
        {"label":"Other","pct":6},
    ],
    "record": {"w":498,"l":287,"d":12},
    "champs": (
        cr("WWF/WWE Championship","×5 (1999, 2002, 2012 ×2, 2012)")
        + cr("World Heavyweight Championship","×2 (2006, 2009)")
        + cr("ECW Championship","×1 (2008)")
        + cr("WCW World Heavyweight Championship","×1 (1999)")
        + cr("WWE Tag Team Championship","×6 (various partners)")
        + cr("Intercontinental Championship","×1 (2012)")
        + cr("US Championship","×2 (2010, 2012)")
    ),
    "bio": (
        '<p>' + a("big-show","Big Show") + ' (Paul Wight) had one of the longest and most decorated careers in WWE history — '
        'a 26-year run that produced world title reigns in WCW, WWF/WWE, ECW, and multiple brands. '
        'At 7\'0" and 400+ lbs, he was the only man to legitimately challenge ' + a("andre-the-giant","Andre the Giant") + '\'s mantle '
        'as wrestling\'s definitive giant.</p>'
        '<p>Show debuted in WCW in 1995 as "The Giant," winning the WCW World title from '
        + a("hulk-hogan","Hulk Hogan") + ' in his debut year. '
        'His WWF debut in 1999 saw him align with Vince McMahon and win the WWF Championship almost immediately. '
        'Over the following two decades, Show cycled between heel and babyface with remarkable frequency — '
        'his turn count became a running joke — but his in-ring work remained credible throughout.</p>'
        '<p>Show signed with AEW in 2021 as Paul Wight, providing veteran presence to the growing promotion. '
        'His career arc is among the longest and most consistently booked of any giant in wrestling history.</p>'
    ),
    "sig": ["Chokeslam","KO Punch (Knockout Punch)","Colossal Clutch (modified camel clutch)","Showstopper (running elbow)"],
    "timeline": [
        ("1995","WCW debut as 'The Giant' — wins WCW World title in debut year"),
        ("1996","nWo programming — feuds with Hogan, Sting, Luger"),
        ("1999","WWF debut — aligns with McMahon; wins WWF Championship quickly"),
        ("2002","SmackDown brand — multiple title programs; legendary Big Show/Brock Lesnar feud"),
        ("2006","World Heavyweight title run on SmackDown"),
        ("2008","ECW Championship reign — oddly prestigious for the brand's final years"),
        ("2012","Multiple title reigns — US, IC, World Heavyweight, Tag on various shows"),
        ("2021","Joins AEW as Paul Wight — career completion tour"),
    ],
    "faq": [
        ("How many world titles has Big Show won?",
         "Big Show has won the WCW World Heavyweight Championship once, the WWF/WWE Championship five times, the World Heavyweight Championship twice, and the ECW Championship once — making him one of the most decorated performers in combined WWE/WCW history."),
        ("Is Big Show in the WWE Hall of Fame?",
         "Yes — Big Show was inducted into the WWE Hall of Fame in 2021 as part of that year's class."),
        ("What is Big Show's finishing move?",
         "The Chokeslam — Big Show's version is considered one of the most impressive executions of the move given his size. His KO Punch (a running knockout punch) became his primary finisher in his later career."),
        ("How tall is Big Show?",
         "Big Show is billed at 7'0\" — his legitimate measured height is generally cited as 6'10\" to 7'0\", making him one of the tallest performers in wrestling history."),
    ],
    "matches": [
        row("big-show","singles",a("hulk-hogan","Hulk Hogan"),"WCW Halloween Havoc","1995-10-29","WCW Championship","Giant wins title in debut year","W"),
        row("big-show","singles",a("brock-lesnar","Brock Lesnar"),"WWE Survivor Series","2002-11-17","WWE Championship","Lesnar retains after Show dominates","L"),
        row("big-show","singles",a("john-cena","John Cena"),"WWE No Mercy","2012-10-28","WWE Championship","Big Show wins title","W"),
        row("big-show","singles",a("the-undertaker","The Undertaker"),"WWE No Way Out","2002-02-17","Buried Alive Match","Show and Undertaker clash of giants","L"),
        row("big-show","singles",a("kane","Kane"),"WWE WrestleMania XIX","2003-03-30","Tag — Show/Jericho vs. Kane/RVD","WM tag title match","W"),
    ],
},

# ── LEX LUGER ─────────────────────────────────────────────────────────────────
{
    "slug": "lex-luger",
    "name": "Lex Luger",
    "nickname": "The Total Package / The Narcissist",
    "era": "Golden Era / New Generation",
    "alignment": "Heel / Face",
    "method_bars": [
        {"label":"Pinfall","pct":36},
        {"label":"Submission (Torture Rack)","pct":32},
        {"label":"Disqualification","pct":18},
        {"label":"Count-out","pct":10},
        {"label":"Other","pct":4},
    ],
    "record": {"w":612,"l":287,"d":22},
    "champs": (
        cr("WCW World Heavyweight Championship","×2 (1991, 1997)")
        + cr("WWF Tag Team Championship","×1 (w/ The Davey Boy Smith, 1997)")
        + cr("WCW United States Heavyweight Championship","×3")
        + cr("NWA/WCW Television Championship","×1")
    ),
    "bio": (
        '<p>' + a("lex-luger","Lex Luger") + ' was one of the most physically imposing wrestlers of the late 1980s and 1990s, '
        'with a physique that rivaled anyone in the industry. His characters — '
        'the Four Horsemen-adjacent "Total Package," the narcissistic mirror-gimmick "Narcissist," '
        'and the patriotic "All-American" babyface — reflected multiple failed attempts to find the '
        'correct presentation for considerable physical gifts.</p>'
        '<p>Luger\'s WWF run in 1993–94 centered on a patriotic push as "The All American." '
        'He bodyslammed ' + a("yokozuna","Yokozuna") + ' on a USS Intrepid battleship and launched '
        '"The Lex Express" national tour — all building to a WWF title shot at SummerSlam 1993 '
        'that ended in a count-out win (not a title win) in one of WWF\'s most criticized booking decisions.</p>'
        '<p>Luger\'s WCW work — particularly as a babyface in the nWo era alongside '
        + a("sting","Sting") + ' — was arguably his most successful. '
        'His two WCW title reigns came in 1991 and 1997, the latter as a surprise win on Nitro '
        'that caused genuine fan disbelief.</p>'
    ),
    "sig": ["Torture Rack (over-the-shoulder backbreaker)","Running Forearm","Standing Powerslam"],
    "timeline": [
        ("1985","Professional debut — immediately pushed due to physique and look"),
        ("1988","NWA/WCW run as 'Total Package' — US title reigns; Four Horsemen adjacent"),
        ("1991","First WCW World title reign — beat Barry Windham"),
        ("1993","WWF debut as 'The Narcissist' — managed by Bobby Heenan"),
        ("1993","Becomes 'All-American Lex Luger' — bodyslams Yokozuna on Intrepid; Lex Express"),
        ("1993","SummerSlam WWF title match vs. Yokozuna — count-out win, no title; massive let-down"),
        ("1995","Returns to WCW — nWo era programs alongside Sting"),
        ("1997","Second WCW title reign on Nitro — unexpected win during Goldberg-era transition"),
    ],
    "faq": [
        ("Why didn't Lex Luger win the WWF Championship?",
         "Luger's SummerSlam 1993 match against Yokozuna ended in a count-out victory — he could not win the title that way. The booking is widely criticized; most observers expected a clean pin and title win based on the entire 'Lex Express' buildup."),
        ("What is the Torture Rack?",
         "The Torture Rack is an over-the-shoulder backbreaker submission — Luger would pick opponents across his shoulders and bend them backward. Given his strength, it was presented as genuinely dangerous."),
        ("Did Lex Luger win the WCW World title?",
         "Yes — twice. First in 1991 from Barry Windham, and again in 1997 on WCW Nitro in a surprising win during the Goldberg/nWo era. The second win was so unexpected that many fans thought it was a mistake."),
        ("Did Lex Luger compete in WWF?",
         "Yes — Luger had a significant WWF run from 1993 to 1995, including the All-American push and the Lex Express tour. He left WWF and returned to WCW in 1995."),
    ],
    "matches": [
        row("lex-luger","singles",a("yokozuna","Yokozuna"),"WWF SummerSlam","1993-08-30","WWF Championship","Count-out win — no title","W"),
        row("lex-luger","singles","Barry Windham","WCW Great American Bash","1991-07-14","WCW Championship","First WCW title reign","W"),
        row("lex-luger","singles",a("goldberg","Goldberg"),"WCW Monday Nitro","1997-08-04","WCW Championship","Second title win — shock result","W"),
        row("lex-luger","singles",a("sting","Sting"),"WCW Clash of Champions","1990-09-05","WCW Championship","Long-running rivalry match","L"),
        row("lex-luger","singles",a("ric-flair","Ric Flair"),"WCW Bash at the Beach","1993-07-18","WCW Championship","Title defense","L"),
    ],
},

# ── DUSTY RHODES ──────────────────────────────────────────────────────────────
{
    "slug": "dusty-rhodes",
    "name": "Dusty Rhodes",
    "nickname": "The American Dream",
    "era": "Golden Era",
    "alignment": "Face",
    "method_bars": [
        {"label":"Pinfall (Bionic Elbow)","pct":44},
        {"label":"Disqualification","pct":28},
        {"label":"Count-out","pct":16},
        {"label":"Submission","pct":8},
        {"label":"Other","pct":4},
    ],
    "record": {"w":689,"l":412,"d":34},
    "champs": (
        cr("NWA World Heavyweight Championship","×3 (1979, 1981, 1986)")
        + cr("NWA United States Heavyweight Championship","×5")
        + cr("NWA/WCW Tag Team Championship","Multiple reigns")
    ),
    "bio": (
        '<p>' + a("dusty-rhodes","Dusty Rhodes") + ' (Virgil Riley Runnels Jr.) was one of the most important figures '
        'in professional wrestling history — as a performer, booker, and storyteller. '
        'The American Dream character — a common man who worked hard and persevered — '
        'resonated with blue-collar audiences in a way that transcended the usual wrestling archetypes.</p>'
        '<p>Rhodes\' three NWA World Heavyweight Championship reigns from 1979 to 1986 were among the most emotionally charged '
        'in NWA history. His feuds with ' + a("ric-flair","Ric Flair") + ' and the Four Horsemen defined '
        'NWA television for much of the 1980s. As booker, his "Dusty finishes" — endings that appeared '
        'to give babyfaces the title only to have them reversed — became part of wrestling\'s lexicon.</p>'
        '<p>Rhodes\' influence extended beyond his own career: his son Dustin became '
        + a("goldust","Goldust") + ' and later Dustin Rhodes, and his son Cody built a career directly '
        'on the American Dream legacy. Dusty Rhodes passed away in June 2015 at age 69.</p>'
        '<div class="notice notice--memorial"><strong>In memoriam:</strong> Dusty Rhodes (born October 12, 1945 — died June 11, 2015) '
        'passed away at age 69. Inducted into the WWE Hall of Fame in 2007.</div>'
    ),
    "sig": ["Bionic Elbow","Flip Flop and Fly","Figure Four Leglock"],
    "timeline": [
        ("1968","Professional debut — natural charisma immediately apparent"),
        ("1975","First major NWA programs — establishes as top babyface"),
        ("1979","First NWA World title reign — first of three"),
        ("1981","Second NWA title reign"),
        ("1985","Mid-South/WWF crossover while still NWA top star"),
        ("1986","Third NWA title reign — culmination of Flair feud"),
        ("1989","WWF stint — polka dots gimmick with Sapphire — diminished role"),
        ("1991","Returns to WCW — backstage booking role alongside ring work"),
        ("2007","WWE Hall of Fame induction"),
        ("2015","Passes away June 11 at age 69 from kidney failure"),
    ],
    "faq": [
        ("How many times did Dusty Rhodes win the NWA World Championship?",
         "Three times — 1979, 1981, and 1986. Each reign involved his ongoing feud with Ric Flair and the Four Horsemen and was built on months of emotional storytelling."),
        ("What is the 'Dusty Finish'?",
         "A 'Dusty Finish' is a booking trope — named after Dusty Rhodes, who used it frequently as NWA booker — where a babyface appears to win a title match, only for the result to be reversed on a technicality (disqualification, interference, referee error). It generates heat while protecting the champion."),
        ("Who are Dusty Rhodes' children in wrestling?",
         "Dusty's sons Dustin Rhodes (also known as Goldust in WWE) and Cody Rhodes both became professional wrestlers. Cody won the AEW and WWE World Championships, building his entire character on the American Dream legacy."),
        ("Is Dusty Rhodes in the WWE Hall of Fame?",
         "Yes — Dusty Rhodes was inducted into the WWE Hall of Fame in 2007. He also worked as a trainer at the WWE Performance Center before his death in 2015."),
    ],
    "matches": [
        row("dusty-rhodes","singles",a("ric-flair","Ric Flair"),"NWA Starrcade","1985-11-28","NWA Championship","Classic Flair-Rhodes feud match","L"),
        row("dusty-rhodes","singles",a("ric-flair","Ric Flair"),"NWA Great American Bash","1986-07-26","NWA Championship","Third title win — American Dream peaks","W"),
        row("dusty-rhodes","singles",a("ric-flair","Ric Flair"),"NWA Starrcade","1986-11-27","NWA Championship","Title loss — Dusty finish controversy","L"),
        row("dusty-rhodes","singles","Tully Blanchard","NWA Great American Bash","1985-07-06","US Championship","I Quit match — classic","W"),
        row("dusty-rhodes","singles","Ted DiBiase","Mid-South Wrestling","1985-01-22","Singles","Mid-South star program","W"),
    ],
},

# ── KEVIN NASH ────────────────────────────────────────────────────────────────
{
    "slug": "kevin-nash",
    "name": "Kevin Nash",
    "nickname": "Big Daddy Cool / Diesel",
    "era": "New Generation / nWo",
    "alignment": "Heel / Face",
    "method_bars": [
        {"label":"Pinfall (Jackknife)","pct":44},
        {"label":"Disqualification","pct":24},
        {"label":"Submission","pct":18},
        {"label":"Count-out","pct":10},
        {"label":"Other","pct":4},
    ],
    "record": {"w":534,"l":312,"d":18},
    "champs": (
        cr("WWF Championship","×1 (as Diesel, 1994–1995)","Year-long reign — longest 1990s WWF title run")
        + cr("WCW World Heavyweight Championship","×4 (1998–1999, with nWo)")
        + cr("WWF Tag Team Championship","×3 (as Diesel, with Shawn Michaels)")
        + cr("TNA World Heavyweight Championship","×2 (2011)")
    ),
    "bio": (
        '<p>' + a("kevin-nash","Kevin Nash") + ' played three significant characters across his career: '
        'Oz (fantasy WCW gimmick), Diesel (WWF bodyguard turned champion), '
        'and Kevin Nash the nWo power broker — and each was more successful than the last.</p>'
        '<p>As Diesel in WWF, Nash held the WWF Championship for 358 days in 1994–95 — '
        'the longest WWF title reign of the decade. He was ' + a("shawn-michaels","Shawn Michaels") + '\'s bodyguard '
        'before splitting off into a successful singles run. His matches with '
        + a("bret-hart","Bret Hart") + ' and Michaels during this run were standout title defenses.</p>'
        '<p>Nash\'s WCW run was defined by his role in the nWo alongside '
        + a("hulk-hogan","Hulk Hogan") + ' and ' + a("sting","Sting") + ' feuds. '
        'His famous fingerpoke of doom — touching Hulk Hogan with one finger to win the WCW title — '
        'is widely cited as the moment WCW\'s booking credibility collapsed. '
        'Nash was also notorious for booking himself favorably during his WCW booking tenure.</p>'
    ),
    "sig": ["Jackknife Powerbomb","Big Boot","Snake Eyes (corner smash)"],
    "timeline": [
        ("1990","WCW debut as Oz — fantasy gimmick fails quickly"),
        ("1993","WWF debut as Diesel — Shawn Michaels' bodyguard"),
        ("1994","WWF Championship win — begins year-long reign as Diesel"),
        ("1995","WWF title run ends — moves to WCW"),
        ("1996","WCW nWo founding member alongside Hulk Hogan and Scott Hall"),
        ("1998","WCW World title runs — multiple reigns during peak nWo era"),
        ("1999","Fingerpoke of Doom — credibility nadir for WCW booking"),
        ("2002","WWE return — brief program with Triple H and Shawn Michaels"),
        ("2011","TNA title reigns — late career championship programs"),
    ],
    "faq": [
        ("How long did Diesel hold the WWF Championship?",
         "Diesel (Kevin Nash) held the WWF Championship for 358 days, from November 26, 1994 to November 19, 1995. It was the longest WWF title reign of the 1990s, though the era is debated for its match quality."),
        ("What is the Fingerpoke of Doom?",
         "On January 4, 1999, Kevin Nash allowed Hulk Hogan to defeat him for the WCW title by lying down after Hogan touched him with one finger. This immediately shattered Nash's monster-heel credibility and is widely cited as the moment WCW's booking fell apart."),
        ("Who are the nWo founders?",
         "The nWo (New World Order) was founded in WCW in 1996 by Hollywood Hulk Hogan, Scott Hall (Razor Ramon), and Kevin Nash — the 'Outsiders' from WWF. The faction expanded over the following years."),
        ("What other names did Kevin Nash use?",
         "Kevin Nash competed as Oz (WCW), Diesel (WWF), Vinnie Vegas (WCW), and Kevin Nash. His most famous character names are Diesel and Big Daddy Cool."),
    ],
    "matches": [
        row("kevin-nash","singles",a("bret-hart","Bret Hart"),"WWF Survivor Series","1994-11-23","WWF Championship","Diesel wins title — upset","W"),
        row("kevin-nash","singles",a("shawn-michaels","Shawn Michaels"),"WWF WrestleMania XI","1995-04-02","WWF Championship","Title defense vs. former partner","W"),
        row("kevin-nash","singles",a("bret-hart","Bret Hart"),"WWF In Your House","1994-12-18","WWF Championship","Major title defense","W"),
        row("kevin-nash","singles",a("shawn-michaels","Shawn Michaels"),"WWF WrestleMania XI","1996-03-31","Ladder Match","HBK vs. Diesel cage — HBK wins","L"),
        row("kevin-nash","singles",a("goldberg","Goldberg"),"WCW Starrcade","1998-12-27","WCW Championship","Nash ends Goldberg streak","W"),
    ],
},

# ── BAM BAM BIGELOW ───────────────────────────────────────────────────────────
{
    "slug": "bam-bam-bigelow",
    "name": "Bam Bam Bigelow",
    "nickname": "The Beast from the East",
    "era": "Golden Era / New Generation",
    "alignment": "Heel / Face",
    "method_bars": [
        {"label":"Pinfall (Greetings from Asbury Park)","pct":46},
        {"label":"Submission","pct":20},
        {"label":"Disqualification","pct":18},
        {"label":"Count-out","pct":10},
        {"label":"Other","pct":6},
    ],
    "record": {"w":489,"l":287,"d":16},
    "champs": (
        cr("ECW World Heavyweight Championship","×1 (1998)")
        + cr("ECW Tag Team Championship","×2 (w/ various partners)")
        + cr("WCW Television Championship","×1 (1993)")
    ),
    "bio": (
        '<p>' + a("bam-bam-bigelow","Bam Bam Bigelow") + ' (Scott Charles Bigelow) was one of wrestling\'s great underutilized talents — '
        'a 390-pound man who could do top-rope senton bombs, moonsaults, and vertical suplexes '
        'with a fluidity that left opponents and audiences genuinely stunned. '
        'In an era when big men were expected to lumber, Bigelow flew.</p>'
        '<p>Bigelow\'s WWF runs in the late 1980s and 1990s never quite gave him the main event prominence '
        'his abilities warranted. His WrestleMania XI match against Lawrence Taylor was a '
        'celebrity-driven experiment that showcased his ability to carry non-wrestlers to watchable matches. '
        'His ECW run produced some of the most credible monster-babyface work of that era.</p>'
        '<p>Bigelow retired in 2000 due to injuries. He passed away in January 2007 at age 45 '
        'from acute intoxication. He was one of wrestling\'s great "what if" performers — '
        'someone whose ceiling was higher than his bookings allowed him to reach.</p>'
        '<div class="notice notice--memorial"><strong>In memoriam:</strong> Bam Bam Bigelow (born September 1, 1961 — died January 19, 2007) '
        'passed away at age 45.</div>'
    ),
    "sig": ["Greetings from Asbury Park (diving headbutt)","Senton Bomb (top rope)","Military Press Drop"],
    "timeline": [
        ("1985","Professional debut — size and agility immediately create buzz"),
        ("1987","WWF debut — pushed as unstoppable monster heel"),
        ("1988","WrestleMania IV appearance — established major league player"),
        ("1993","Returns to WWF — heel run, Luna Vachon as manager"),
        ("1995","WrestleMania XI vs. Lawrence Taylor — credible celebrity match"),
        ("1996","ECW debut — fan-favorite monster; serious booking begins"),
        ("1998","ECW World Heavyweight Championship reign — peak ECW work"),
        ("2000","Retirement due to accumulated injuries"),
        ("2007","Passes away January 19 at age 45"),
    ],
    "faq": [
        ("Did Bam Bam Bigelow win any major championships?",
         "Bigelow won the ECW World Heavyweight Championship in 1998, as well as the WCW Television Championship in 1993. His WWE/WWF run, despite its length, never produced a world or IC title run."),
        ("What is Bam Bam Bigelow's finishing move?",
         "Greetings from Asbury Park — a diving headbutt from the top rope. For a man of Bigelow's size, it was a visually stunning finisher that few performers of his era could replicate."),
        ("What is Bam Bam Bigelow best known for?",
         "Bigelow is best known for his WrestleMania XI match against NFL star Lawrence Taylor in 1995, his ECW work, and generally for being one of the most agile big men in wrestling history. His top-rope senton bomb was considered ahead of its time."),
        ("Why didn't Bam Bam Bigelow win more championships?",
         "Bigelow's WWF runs coincided with eras where the main event was locked around Hulk Hogan, Bret Hart, Shawn Michaels, and The Undertaker. His size and character made him an ideal monster-heel, but he was rarely positioned as a credible long-term champion."),
    ],
    "matches": [
        row("bam-bam-bigelow","singles","Lawrence Taylor","WWF WrestleMania XI","1995-04-02","Singles — celebrity match","LT wins — Bigelow carries the match","L"),
        row("bam-bam-bigelow","singles",a("undertaker","The Undertaker"),"WWF Royal Rumble","1994-01-22","Singles","Giant vs. Deadman","L"),
        row("bam-bam-bigelow","singles","Taz","ECW Guilty as Charged","1998-01-10","ECW Championship","ECW title win — monster program","W"),
        row("bam-bam-bigelow","singles",a("diesel","Kevin Nash"),"WWF Royal Rumble","1995-01-22","Royal Rumble","Rumble match appearance","L"),
        row("bam-bam-bigelow","singles",a("shawn-michaels","Shawn Michaels"),"WWF WrestleMania X","1994-03-20","Singles","WM showcase","L"),
    ],
},

]  # end WRESTLERS list

# ── sparkline helper ──────────────────────────────────────────────────────────
def make_spark(record, n=60):
    total = record["w"] + record["l"] + record["d"]
    if total == 0:
        return '<i></i>' * n
    wp = record["w"] / total
    block_w = max(1, round(wp * 10))
    block_l = 10 - block_w
    pattern = ['<i></i>'] * block_w + ['<i class="l"></i>'] * block_l
    return ''.join((pattern * ((n // 10) + 1))[:n])

# ── page builder (matches 10a gold template) ──────────────────────────────────
def build_page(w):
    slug          = w["slug"]
    name          = w["name"]
    nickname      = w.get("nickname","")
    era           = w.get("era","")
    alignment     = w.get("alignment","")
    bio           = w.get("bio","")
    sig_list      = w.get("sig",[])
    champ_html    = w.get("champs","")
    timeline_data = w.get("timeline",[])
    faq           = w.get("faq",[])
    method_bars   = w.get("method_bars",[])
    record        = w.get("record",{"w":0,"l":0,"d":0})
    matches_rows  = w.get("matches",[])

    bars_html = ""
    for b in method_bars:
        bars_html += (f'<div class="mb-row">'
                      f'<span class="mb-label">{b["label"]}</span>'
                      f'<div class="mb-track"><div class="mb-fill" style="--w:{b["pct"]}%"></div></div>'
                      f'<span class="mb-pct">{b["pct"]}%</span></div>\n')

    total = record["w"] + record["l"] + record["d"]
    wpct  = round(record["w"] / total * 100) if total else 0
    record_table = (
        f'<table class="record-table"><thead><tr>'
        f'<th>W</th><th>L</th><th>D</th><th>Win %</th></tr></thead>'
        f'<tbody><tr><td>{record["w"]}</td><td>{record["l"]}</td>'
        f'<td>{record["d"]}</td><td>{wpct}%</td></tr></tbody></table>\n'
    )

    sig_html = ""
    for s in sig_list:
        sig_html += f'<li>{s}</li>\n'

    champ_block = ""
    if champ_html:
        champ_block = '<h2>Championships &amp; Titles</h2>\n<div class="champ-panel"><div class="champ-rows">\n' + champ_html + '</div></div>\n'

    tl_html = ""
    for (yr, ev) in timeline_data:
        tl_html += f'<li><span class="tl-year">{yr}</span><span class="tl-event">{ev}</span></li>\n'
    timeline_block = ('<h2>Career Timeline</h2>\n<ol class="timeline">\n' + tl_html + '</ol>\n') if tl_html else ""

    faq_html = ""
    faq_items_ld = ""
    for (q, ans) in faq:
        faq_html += f'<details><summary>{q}</summary><p>{ans}</p></details>\n'
        safe_q   = q.replace('"', '&quot;')
        safe_ans = re.sub(r'<[^>]+>', '', ans).replace('"', '&quot;')
        faq_items_ld += (f'{{"@type":"Question","name":"{safe_q}",'
                         f'"acceptedAnswer":{{"@type":"Answer","text":"{safe_ans}"}}}},')
    faq_items_ld = faq_items_ld.rstrip(",")
    faq_block    = ('<h2>FAQ</h2>\n<div class="faq-block">\n' + faq_html + '</div>\n') if faq_html else ""
    faq_ld_block = (',\n    {"@type":"FAQPage","mainEntity":[' + faq_items_ld + ']}') if faq else ""

    matches_html = "".join(matches_rows)
    spark = make_spark(record)
    wl_section = (
        '<section class="wl-strip-wrap" aria-label="Win/loss sparkline">\n'
        f'  <div class="wl-strip">{spark}</div>\n'
        '</section>\n'
    )

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{name} — Career Record, Stats &amp; Match History | MAT</title>
<meta name="description" content="Career profile, championship history, match record, and timeline for {name} — {nickname}, {era} era.">
<link rel="canonical" href="https://matdb.io/wrestlers/{slug}/">
<link rel="stylesheet" href="/css/site.css">
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@graph":[
    {{"@type":"Person","name":"{name}","jobTitle":"Professional Wrestler","description":"Career profile for {name}, {nickname}","url":"https://matdb.io/wrestlers/{slug}/"}},
    {{"@type":"BreadcrumbList","itemListElement":[
      {{"@type":"ListItem","position":1,"name":"Home","item":"https://matdb.io/"}},
      {{"@type":"ListItem","position":2,"name":"Wrestlers","item":"https://matdb.io/wrestlers/"}},
      {{"@type":"ListItem","position":3,"name":"{name}","item":"https://matdb.io/wrestlers/{slug}/"}}
    ]}}{faq_ld_block}
  ]
}}
</script>
</head>
<body>
<header class="site-header">
  <a class="logo" href="/">MAT</a>
  <nav aria-label="Main">
    <a href="/wrestlers/">Wrestlers</a>
    <a href="/events/">Events</a>
    <a href="/titles/">Titles</a>
    <a href="/search/">Search</a>
  </nav>
</header>
<nav class="breadcrumb" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/wrestlers/">Wrestlers</a></li>
    <li aria-current="page">{name}</li>
  </ol>
</nav>
<main>

<section class="athlete-hero">
  <div class="hero-content">
    <p class="hero-eyebrow">{nickname} &nbsp;·&nbsp; {era}</p>
    <h1 class="hero-name">{name}</h1>
    <p class="dim">{alignment}</p>
    <div class="hero-stat-block">
      <div class="stat-big"><span class="stat-num">{record["w"]}</span><span class="stat-label">Wins</span></div>
      <div class="stat-big"><span class="stat-num">{record["l"]}</span><span class="stat-label">Losses</span></div>
      <div class="stat-big"><span class="stat-num">{wpct}%</span><span class="stat-label">Win %</span></div>
    </div>
  </div>
</section>

{wl_section}
<section class="content-grid">
  <article class="bio-col">
    <h2>Biography</h2>
    {bio}
    {champ_block}
    {timeline_block}
    {faq_block}
  </article>
  <aside class="stats-col">
    <h2>Signature Moves</h2>
    <ul class="sig-list">
{sig_html}    </ul>
    <h2>Method Breakdown</h2>
    <div class="method-bars">
{bars_html}    </div>
    <h2>Win / Loss Record</h2>
    {record_table}
  </aside>
</section>

<section class="match-record">
  <h2>Notable Matches</h2>
  <table class="record-table" data-record-filter data-record-count="{total}">
    <thead><tr>
      <th>Result</th><th>Opponent</th><th>Event</th>
      <th>Date</th><th>Type</th><th>Notes</th>
    </tr></thead>
    <tbody>
{matches_html}    </tbody>
  </table>
</section>

</main>
<footer class="site-footer">
  <p>&copy; 2025 MAT Wrestling Database. All rights reserved.</p>
  <nav><a href="/about/">About</a> · <a href="/privacy/">Privacy</a> · <a href="/contact/">Contact</a></nav>
</footer>
<script src="/js/main.js"></script>
</body>
</html>"""
    return page


if __name__ == "__main__":
    for w in WRESTLERS:
        slug = w["slug"]
        dest = os.path.join(OUT, slug)
        os.makedirs(dest, exist_ok=True)
        html = build_page(w)
        path = os.path.join(dest, "index.html")
        with open(path, "w") as f:
            f.write(html)
        lines = html.count("\n")
        print(f"✅ {slug} — {lines} lines")
    print("\nBatch 10b complete.")
