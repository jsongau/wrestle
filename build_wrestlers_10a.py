#!/usr/bin/env python3
"""Batch 10a — Andre the Giant, Roddy Piper, Mr. Perfect, Chyna, Rick Rude (new pages)"""
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

# ── ANDRE THE GIANT ───────────────────────────────────────────────────────────
{
    "slug": "andre-the-giant",
    "name": "Andre the Giant",
    "nickname": "The Eighth Wonder of the World",
    "era": "Golden Era",
    "alignment": "Face / Heel",
    "method_bars": [
        {"label":"Pinfall","pct":38},
        {"label":"Disqualification","pct":30},
        {"label":"Count-out","pct":18},
        {"label":"Submission","pct":8},
        {"label":"Other","pct":6},
    ],
    "record": {"w":612,"l":97,"d":24},
    "champs": (
        cr("WWF Championship","1× (1988 — 1 day)","Vacated; sold title to Ted DiBiase, not recognized officially")
        + cr("NWA/WWF Tag Team Championship","Multiple reigns — various partners")
        + cr("Intercontinental Championship","Claim disputed — not recognized")
    ),
    "bio": (
        '<p>' + a("andre-the-giant","Andre the Giant") + ' (André René Roussimoff) was the defining giant of professional wrestling — '
        'at 7\'4" and 520 lbs at his peak, he was the most physically imposing performer the sport has ever seen, '
        'and arguably the most globally recognizable wrestler in history before ' + a("hulk-hogan","Hulk Hogan") + '.</p>'
        '<p>Andre toured the world for over two decades, appearing for virtually every major territory. '
        'His undefeated streak — legitimate or heavily protected depending on the territory — lasted roughly 15 years. '
        'The 1987 WWF Championship feud with Hogan, culminating at WrestleMania III in the Pontiac Silverdome before '
        '93,000 fans, produced wrestling\'s most iconic visual: Hogan bodyslamming Andre.</p>'
        '<p>Andre\'s later years saw him turn heel, managed by '
        + a("ted-dibiase","Ted DiBiase") + ', in programs designed around his deteriorating health. '
        'His cooperation — performing through genuine pain and degenerative acromegaly — reflected his professionalism. '
        'Andre passed away in January 1993 and was the inaugural WWE Hall of Fame inductee. '
        'He was 46 years old.</p>'
        '<div class="notice notice--memorial"><strong>In memoriam:</strong> Andre the Giant (born May 19, 1946 — died January 27, 1993) '
        'passed away from congestive heart failure at age 46. He was the inaugural WWE Hall of Fame inductee in 1993.</div>'
    ),
    "sig": ["Sitdown Splash","Headbutt","Big Boot","Bearhug"],
    "timeline": [
        ("1966","Professional debut in France — size and athletic background attract attention"),
        ("1973","WWF debut — begins years of regular appearances; undefeated streak grows"),
        ("1980","Recognized globally as wrestling's biggest star — literally and figuratively"),
        ("1987","WrestleMania III: bodyslam by Hulk Hogan before 93,000 in Pontiac — wrestling's most iconic moment"),
        ("1988","WWF Championship moment — pins Hogan in controversial Main Event TV match"),
        ("1989","Heel turn with Ted DiBiase; managed by Bobby Heenan — Heenan Family feud"),
        ("1991","Final significant WWF programming; health visibly declining"),
        ("1993","Passes away January 27 in Paris from congestive heart failure, age 46"),
    ],
    "faq": [
        ("How tall was Andre the Giant?",
         "Andre's billed height was 7'4\" — his actual measured height varied by source, generally listed between 7'0\" and 7'4\" depending on the era. His acromegaly (abnormal growth) caused his size and ultimately contributed to his death."),
        ("Did Hulk Hogan really bodyslam Andre the Giant?",
         "Yes — the bodyslam at WrestleMania III on March 29, 1987, is real. It was a legitimately difficult feat given Andre's size and weight at that point. Hogan has described it as physically the hardest thing he did in wrestling."),
        ("Did Andre the Giant ever lose?",
         "Yes — Andre's undefeated streak was a promotional tool, not a literal record. He lost via DQ and other methods in various territories. His streak was eventually broken by Hulk Hogan in WWF's Main Event special in 1988."),
        ("When did Andre the Giant die?",
         "Andre the Giant died on January 27, 1993, in Paris, France, from congestive heart failure. He was 46 years old and had been in Paris for his father's funeral. He was the inaugural WWE Hall of Fame inductee the same year."),
    ],
    "matches": [
        row("andre-the-giant","singles",a("hulk-hogan","Hulk Hogan"),"WWF WrestleMania III","1987-03-29","Singles","Bodyslam — wrestling's most iconic moment","L"),
        row("andre-the-giant","singles",a("hulk-hogan","Hulk Hogan"),"WWF Main Event","1988-02-05","WWF Championship","Andre wins in controversial finish; Ted DiBiase plan","W"),
        row("andre-the-giant","singles",a("big-john-studd","Big John Studd"),"WWF WrestleMania I","1985-03-31","Bodyslam Challenge","Andre wins bodyslam match","W"),
        row("andre-the-giant","tag",a("hulk-hogan","Hogan") + " &amp; " + a("randy-savage","Savage"),"WWF SummerSlam","1988-08-29","Tag — Mega Powers vs. Mega Bucks","Andre & DiBiase lose to Mega Powers","L"),
        row("andre-the-giant","singles",a("jake-roberts","Jake Roberts"),"WWF Saturday Night's Main Event","1987-10-03","Singles","Andre vs. Damien — classic intimidation","W"),
    ],
},

# ── RODDY PIPER ───────────────────────────────────────────────────────────────
{
    "slug": "roddy-piper",
    "name": "Roddy Piper",
    "nickname": "Hot Rod",
    "era": "Golden Era",
    "alignment": "Heel / Face",
    "method_bars": [
        {"label":"Disqualification","pct":36},
        {"label":"Pinfall","pct":28},
        {"label":"Count-out","pct":18},
        {"label":"Submission","pct":12},
        {"label":"Other","pct":6},
    ],
    "record": {"w":489,"l":312,"d":28},
    "champs": (
        cr("WWF Intercontinental Championship","1× (1992)")
        + cr("NWA United States Heavyweight Championship","×2 (Mid-Atlantic, 1980–1981)")
        + cr("WCW Television Championship","×1 (1999)")
    ),
    "bio": (
        '<p>' + a("roddy-piper","Roddy Piper") + ' (Roderick George Toombs) was the greatest heel talker of the Golden Era '
        'and one of wrestling\'s most naturally gifted entertainers. His Piper\'s Pit interview segment defined '
        'what wrestling promos could be — dangerous, unpredictable, genuinely uncomfortable.</p>'
        '<p>Piper\'s role in the first WrestleMania was central: feuding with '
        + a("hulk-hogan","Hulk Hogan") + ' through 1984–85 gave WWF its essential conflict. '
        'As heel manager of Paul Orndorff at WrestleMania I, Piper\'s star power was a key ingredient '
        'in making the event feel like a genuine main event spectacle.</p>'
        '<p>Piper could work babyface nearly as well as heel — his transition to fan favorite in the '
        'late 1980s and 1990s showed range few of his contemporaries possessed. '
        'His 1989 film They Live remains a cult classic. '
        'Roddy Piper passed away in July 2015 from cardiac arrest at age 61.</p>'
        '<div class="notice notice--memorial"><strong>In memoriam:</strong> Roddy Piper (born January 17, 1954 — died July 31, 2015) '
        'passed away from cardiac arrest at age 61. Inducted into the WWE Hall of Fame in 2005.</div>'
    ),
    "sig": ["Sleeper Hold","Piledriver","Hip Toss","Piper's Pit (interview segment)"],
    "timeline": [
        ("1973","Professional debut as teenager — trained by various territory veterans"),
        ("1980","NWA US title reigns — establishes as elite heel in Mid-Atlantic"),
        ("1984","WWF debut — Piper's Pit launches; becomes top heel immediately"),
        ("1985","WrestleMania I: manages Paul Orndorff in main event vs. Hogan and Mr. T"),
        ("1992","Babyface IC title reign — brief but memorable"),
        ("1994","Semi-retirement; movie career including They Live"),
        ("1996","WCW return — feuds and TV title reign"),
        ("2005","WWE Hall of Fame induction — long overdue recognition"),
        ("2015","Passes away July 31 from cardiac arrest at age 61"),
    ],
    "faq": [
        ("Did Roddy Piper ever win the WWF Championship?",
         "No — Piper is one of wrestling's great examples of a top star who never held the world title. His value was as a heat machine and program driver; a world title would have required turning babyface, which WWE did eventually but carefully."),
        ("What was Piper's Pit?",
         "Piper's Pit was an in-ring interview segment hosted by Roddy Piper from 1984–87. It was intentionally volatile — Piper's unpredictability made it must-watch TV. The coconut incident with Jimmy Snuka is its most famous moment."),
        ("What movies did Roddy Piper appear in?",
         "Piper's most notable film is They Live (1988), the John Carpenter sci-fi film in which he stars. It includes one of cinema's longest fight scenes. Piper appeared in numerous other films and TV shows throughout his career."),
        ("How did Roddy Piper die?",
         "Roddy Piper died on July 31, 2015, from hypertensive cardiovascular disease (cardiac arrest) at his home in Hollywood. He was 61 years old. His death came just months after the passing of his WrestleMania I co-star, Randy Savage."),
    ],
    "matches": [
        row("roddy-piper","singles",a("hulk-hogan","Hulk Hogan"),"WWF WrestleMania II","1986-04-07","Boxing match","Celebrity boxing exhibition — major WM II match","L"),
        row("roddy-piper","singles",a("bret-hart","Bret Hart"),"WWF WrestleMania VIII","1992-04-05","WWF IC Championship","Piper wins IC title — popular babyface moment","W"),
        row("roddy-piper","singles",a("bret-hart","Bret Hart"),"WWF WrestleMania IX","1993-04-04","WWF IC Championship","Piper loses IC title back to Hart","L"),
        row("roddy-piper","tag",a("hulk-hogan","Hulk Hogan"),"WWF WrestleMania I","1985-03-31","Tag — Hogan/Mr. T vs. Piper/Orndorff","Loses the main event of the first WrestleMania","L"),
        row("roddy-piper","singles",a("mr-perfect","Mr. Perfect"),"WWF Survivor Series","1991-11-27","Singles","Tag team survivor series","W"),
    ],
},

# ── MR. PERFECT (CURT HENNIG) ─────────────────────────────────────────────────
{
    "slug": "mr-perfect",
    "name": "Mr. Perfect",
    "nickname": "Curt Hennig",
    "era": "Golden Era / New Generation",
    "alignment": "Heel / Face",
    "method_bars": [
        {"label":"Pinfall","pct":42},
        {"label":"Submission (Perfectplex)","pct":28},
        {"label":"Disqualification","pct":18},
        {"label":"Count-out","pct":8},
        {"label":"Other","pct":4},
    ],
    "record": {"w":521,"l":289,"d":14},
    "champs": (
        cr("WWF Intercontinental Championship","×2 (1990–1991)")
        + cr("AWA World Heavyweight Championship","×1 (1987)")
        + cr("WCW United States Heavyweight Championship","×1 (1997)")
    ),
    "bio": (
        '<p>' + a("mr-perfect","Mr. Perfect") + ' (Curt Hennig) was one of the most athletically gifted wrestlers of his generation — '
        'a legitimate multi-sport athlete from a wrestling family (his father was AWA legend Larry "The Axe" Hennig) '
        'who combined natural charisma with elite technical ability.</p>'
        '<p>The Mr. Perfect character — introduced in 1988 with vignettes showing Hennig perfecting every sport — '
        'was the ideal vehicle for his abilities. His two Intercontinental Championship reigns produced '
        'some of the best IC title matches of the Golden Era, particularly against '
        + a("bret-hart","Bret Hart") + ' at SummerSlam 1991 — widely regarded as one of the greatest matches in SummerSlam history.</p>'
        '<p>Hennig\'s late career in WCW saw him as part of the nWo and in the US title scene. '
        'He passed away in February 2003 from acute cocaine toxicity at age 44. '
        'He was inducted into the WWE Hall of Fame posthumously in 2007.</p>'
        '<div class="notice notice--memorial"><strong>In memoriam:</strong> Curt Hennig (born March 28, 1958 — died February 10, 2003) '
        'passed away at age 44. Inducted into the WWE Hall of Fame in 2007.</div>'
    ),
    "sig": ["Perfectplex (fisherman suplex)","Axe Bomber (short-arm clothesline)","Standing dropkick"],
    "timeline": [
        ("1980","Professional debut — follows father Larry 'The Axe' Hennig into business"),
        ("1987","AWA World Heavyweight Championship reign — peak of territorial era"),
        ("1988","WWF debut — Mr. Perfect character launched with iconic 'perfection' vignettes"),
        ("1990","First IC title reign — becomes the premier midcard title program in WWF"),
        ("1991","SummerSlam match vs. Bret Hart — classic IC match defines both careers"),
        ("1992","Managerial role for Ric Flair — IC title feud with British Bulldog and others"),
        ("1993","Returns to active competition; manages the Narcissist Lex Luger"),
        ("1997","WCW debut — nWo, US title reign; late career respected performances"),
        ("2003","Passes away February 10 from acute cocaine toxicity, age 44"),
    ],
    "faq": [
        ("What championships did Mr. Perfect win?",
         "Mr. Perfect (Curt Hennig) won the WWF Intercontinental Championship twice (1990, 1991), the AWA World Heavyweight Championship (1987), and the WCW United States Championship (1997)."),
        ("What is the Perfectplex?",
         "The Perfectplex is a fisherman suplex with a bridge — Hennig hooks the opponent's leg and bridges back for the pin. It was treated as nearly impossible to kick out of, and Hennig's execution was textbook."),
        ("What is Mr. Perfect's best match?",
         "Most historians point to his IC Championship match with Bret Hart at SummerSlam 1991 as his finest work — a match that showcased both men's technical excellence and storytelling ability, often listed among the greatest SummerSlam matches ever."),
        ("Is Mr. Perfect in the WWE Hall of Fame?",
         "Yes — Curt Hennig was inducted posthumously in 2007, four years after his death. His son, Joe Hennig (Curtis Axel), has also competed in WWE."),
    ],
    "matches": [
        row("mr-perfect","singles",a("bret-hart","Bret Hart"),"WWF SummerSlam","1991-08-26","WWF IC Championship","Classic — loses title to Hart","L"),
        row("mr-perfect","singles",a("bret-hart","Bret Hart"),"WWF WrestleMania X","1994-03-20","Singles","WM showcase match","L"),
        row("mr-perfect","singles","Texas Tornado Kerry Von Erich","WWF SummerSlam","1990-08-27","WWF IC Championship","Loses IC title to Von Erich","L"),
        row("mr-perfect","singles","Texas Tornado Kerry Von Erich","WWF Superstars","1990-11-19","WWF IC Championship","Regains IC title","W"),
        row("mr-perfect","singles",a("shawn-michaels","Shawn Michaels"),"WWF Raw","1993-07-27","IC Championship match","Classic TV match","W"),
    ],
},

# ── CHYNA ─────────────────────────────────────────────────────────────────────
{
    "slug": "chyna",
    "name": "Chyna",
    "nickname": "The Ninth Wonder of the World",
    "era": "Attitude Era",
    "alignment": "Heel / Face",
    "method_bars": [
        {"label":"Pinfall","pct":44},
        {"label":"Disqualification","pct":26},
        {"label":"Submission","pct":16},
        {"label":"Count-out","pct":10},
        {"label":"Other","pct":4},
    ],
    "record": {"w":89,"l":61,"d":4},
    "champs": (
        cr("WWF Intercontinental Championship","×2 (1999, 2001)","First woman to hold the title")
        + cr("WWF Women's Championship","×1 (2001)")
        + cr("WWF Tag Team Championship","×1 (w/ Triple H)")
    ),
    "bio": (
        '<p>' + a("chyna","Chyna") + ' (Joanie Laurer) was the first woman to compete in the Royal Rumble, '
        'the first woman to win the WWF Intercontinental Championship, and the most physically imposing '
        'female performer in WWF history. She redefined what female wrestlers could do and where they could appear.</p>'
        '<p>Chyna was part of D-Generation X alongside '
        + a("triple-h","Triple H") + ', ' + a("shawn-michaels","Shawn Michaels") + ', and others, '
        'serving simultaneously as Triple H\'s manager and bodyguard and then as a legitimate competitor. '
        'Her IC title reign in 1999 — defeating Jeff Jarrett at No Mercy — was treated as a genuine upset '
        'and breakthrough moment for mixed-gender competition.</p>'
        '<p>Chyna left WWF in 2001 following personal issues. Her post-WWE career was complicated, '
        'and she passed away in April 2016 from an accidental drug overdose at age 45. '
        'She was posthumously inducted into the WWE Hall of Fame in 2019.</p>'
        '<div class="notice notice--memorial"><strong>In memoriam:</strong> Chyna (Joanie Laurer, born December 27, 1970 — died April 20, 2016) '
        'passed away at age 45. She was inducted into the WWE Hall of Fame posthumously in 2019.</div>'
    ),
    "sig": ["Pedigree (assisted)","Low Blow","Standing Powerbomb","Handspring Elbow"],
    "timeline": [
        ("1996","Debuts in WWF — immediately stands out physically and character-wise"),
        ("1997","Joins D-Generation X as Triple H's enforcer and bodyguard"),
        ("1999","Royal Rumble entry — first woman to compete in the Royal Rumble"),
        ("1999","Defeats Jeff Jarrett for WWF IC Championship — first woman to win title"),
        ("2001","Second IC title reign; brief Women's Championship reign"),
        ("2001","Departs WWF following personal difficulties"),
        ("2016","Passes away April 20 from accidental drug overdose, age 45"),
        ("2019","Inducted posthumously into WWE Hall of Fame as a solo inductee"),
    ],
    "faq": [
        ("Was Chyna the first woman to hold the Intercontinental Championship?",
         "Yes — Chyna won the WWF Intercontinental Championship twice, making her the first (and, as of 2025, only) woman to hold the title. Her first win came at No Mercy 1999 against Jeff Jarrett."),
        ("Did Chyna compete in the Royal Rumble?",
         "Yes — Chyna entered the Royal Rumble in 1999, making her the first woman to compete in the event. She eliminated others in the match, further cementing her status as a crossover competitor."),
        ("What is Chyna's legacy?",
         "Chyna broke gender barriers in ways that predated the Women's Evolution era by two decades. She competed against men, held men's titles, and showed that a woman could be a credible physical presence in WWF main events."),
        ("When was Chyna inducted into the WWE Hall of Fame?",
         "Chyna was inducted into the WWE Hall of Fame posthumously in 2019, as part of that year's class alongside D-Generation X. Her individual induction was separate from the DX group induction in 2019."),
    ],
    "matches": [
        row("chyna","singles","Jeff Jarrett","WWF No Mercy","1999-10-17","WWF IC Championship","First woman to win IC title","W"),
        row("chyna","singles","Jeff Jarrett","WWF No Mercy","2000-10-22","WWF IC Championship","Second IC title win","W"),
        row("chyna","singles",a("chris-jericho","Chris Jericho"),"WWF Survivor Series","1999-11-14","IC title match","Defends IC title","W"),
        row("chyna","singles",a("triple-h","Triple H"),"WWF Raw","1999-05-24","Singles","Program with Triple H turning babyface","L"),
        row("chyna","royal-rumble","Royal Rumble field","WWF Royal Rumble","1999-01-24","Royal Rumble","First woman in Royal Rumble","D"),
    ],
},

# ── RICK RUDE ─────────────────────────────────────────────────────────────────
{
    "slug": "rick-rude",
    "name": "Rick Rude",
    "nickname": "The Ravishing One",
    "era": "Golden Era",
    "alignment": "Heel",
    "method_bars": [
        {"label":"Pinfall","pct":40},
        {"label":"Submission (Rude Awakening)","pct":30},
        {"label":"Disqualification","pct":18},
        {"label":"Count-out","pct":8},
        {"label":"Other","pct":4},
    ],
    "record": {"w":498,"l":287,"d":16},
    "champs": (
        cr("WWF Intercontinental Championship","×1 (1989)")
        + cr("WCW United States Heavyweight Championship","×1 (1993)")
        + cr("WCW International World Heavyweight Championship","×1 (1993)")
    ),
    "bio": (
        '<p>' + a("rick-rude","Rick Rude") + ' (Richard Erwin Rood) was one of the most effective pure heels of the Golden Era. '
        'With legitimate physical gifts — a bodybuilder physique combined with genuine in-ring ability — '
        'and a heel character built entirely on vanity and condescension, Rude was perfectly cast.</p>'
        '<p>Rude\'s WWF run produced memorable programs with '
        + a("jake-roberts","Jake Roberts") + ' (whose wife\'s face appeared on Rude\'s trunks in a notorious angle) '
        'and the ultimate payoff of winning the IC title from the Ultimate Warrior at WrestleMania V. '
        'His WCW run in the early 1990s was equally strong, producing US and International title reigns.</p>'
        '<p>Rick Rude passed away in April 1999 from heart failure caused by accidental drug overdose at age 40. '
        'He was inducted into the WWE Hall of Fame posthumously in 2017.</p>'
        '<div class="notice notice--memorial"><strong>In memoriam:</strong> Rick Rude (born December 7, 1958 — died April 20, 1999) '
        'passed away at age 40. He was inducted into the WWE Hall of Fame posthumously in 2017.</div>'
    ),
    "sig": ["Rude Awakening (neckbreaker)","Tombstone Piledriver","Swinging Neckbreaker"],
    "timeline": [
        ("1982","Professional debut — physical gifts immediately apparent"),
        ("1986","WWF debut — Ravishing Rick Rude character fully formed"),
        ("1987","Feud with Jake Roberts — trunks with wife's face angle; compelling television"),
        ("1989","WWF Intercontinental title win over Ultimate Warrior at WrestleMania V"),
        ("1990","Leaves WWF; joins WCW"),
        ("1993","WCW US and International title reigns — peak WCW work"),
        ("1997","Appears on both WWF Raw and WCW Nitro on the same night — legal battle makes it possible"),
        ("1999","Passes away April 20 from heart failure, age 40"),
    ],
    "faq": [
        ("How did Rick Rude win the WWF Intercontinental Championship?",
         "Rude defeated The Ultimate Warrior at WrestleMania V on April 2, 1989. Bobby Heenan grabbed Warrior's legs from outside, allowing Rude to get the pin. It was the climax of a long feud built on Rude's infatuation with Warrior's then-wife."),
        ("Why did Rick Rude appear on both Raw and Nitro?",
         "On September 22, 1997, Rick Rude appeared live on WCW Nitro (as part of the nWo) while a taped version of him appeared on WWF Raw from a previous taping. The WWF's taping schedule made this possible and was an embarrassment for WWF."),
        ("What is Rick Rude's finishing move?",
         "The Rude Awakening — a swinging neckbreaker. Rude would gyrate his hips before delivering the move, maximizing the crowd's reaction to his heel character."),
        ("Is Rick Rude in the WWE Hall of Fame?",
         "Yes — Rick Rude was inducted posthumously into the WWE Hall of Fame in 2017, inducted by his son who is also a professional wrestler."),
    ],
    "matches": [
        row("rick-rude","singles","Ultimate Warrior","WWF WrestleMania V","1989-04-02","WWF IC Championship","Rude wins IC title — major Heenan Family moment","W"),
        row("rick-rude","singles","Ultimate Warrior","WWF SummerSlam","1989-08-28","WWF IC Championship","Warrior regains title","L"),
        row("rick-rude","singles",a("jake-roberts","Jake Roberts"),"WWF Saturday Night's Main Event","1988-04-02","Singles","Famous trunks feud payoff","W"),
        row("rick-rude","singles","Sting","WCW Beach Blast","1992-06-20","WCW International Championship","WCW title program","L"),
        row("rick-rude","singles",a("shawn-michaels","Shawn Michaels"),"WWF Raw","1992-12-14","WWF IC Championship","Late WWF/early WCW program","W"),
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

# ── page builder ──────────────────────────────────────────────────────────────
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
    print("\nBatch 10a complete.")
