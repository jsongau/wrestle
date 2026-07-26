#!/usr/bin/env python3
"""Batch 9b — Jake Roberts, Arn Anderson, Brian Pillman (upgrades), Yokozuna, Vader (new)"""
import os, re, textwrap

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

# ── JAKE "THE SNAKE" ROBERTS (upgrade 3→5) ──────────────────────────────────
{
    "slug": "jake-roberts",
    "name": "Jake 'The Snake' Roberts",
    "nickname": "The Snake",
    "era": "Golden Era",
    "alignment": "Heel / Face",
    "method_bars": [
        {"label":"Submission / DDT KO","pct":34},
        {"label":"Pinfall","pct":28},
        {"label":"Disqualification","pct":22},
        {"label":"Count-out","pct":10},
        {"label":"Other","pct":6},
    ],
    "record": {"w":312,"l":201,"d":9},
    "champs": (
        cr("WWF Intercontinental Championship","(never won — perennial contender)")
        + cr("NWA Television Championship","1982")
    ),
    "bio": (
        '<p>' + a("jake-roberts","Jake Roberts") + ' is one of the greatest pure psychologists in professional wrestling history. '
        'His DDT — planted in the era before finishers were common — became among the most feared moves in the business.</p>'
        '<p>Roberts spent most of his WWF tenure terrorizing opponents with his python Damien, feuding with '
        + a("rick-rude","Rick Rude") + ', ' + a("andre-the-giant","Andre the Giant") + ', and ' + a("ted-dibiase","Ted DiBiase") + '. '
        'His slow-burn heel work and mic ability set a template that heels still follow today.</p>'
        '<p>Roberts also feuded famously with ' + a("ultimate-warrior","The Ultimate Warrior") + ' and later '
        + a("undertaker","The Undertaker") + ' in a dark feud that played on genuine personal demons. '
        'His autobiographical honesty about addiction made him one of wrestling\'s most humanized figures.</p>'
    ),
    "sig": ["DDT","Short-arm Clothesline","Damien (python intimidation)"],
    "timeline": [
        ("1982","Breaks through in Mid-South as a calculating heel with elite mic skills"),
        ("1986","Debuts in WWF — DDT immediately establishes as must-see offense"),
        ("1987","Feud with Honky Tonk Man and Rick Rude over IC title escalates his profile"),
        ("1988","Tangles with Andre the Giant in high-profile program"),
        ("1991","Babyface turn; dark feud with Undertaker and drug storyline"),
        ("1996","Returns to WWF for brief run; battles personal demons publicly"),
        ("2015","AEW era — mentors Cody Rhodes; WWE Hall of Fame inducted"),
    ],
    "faq": [
        ("Did Jake Roberts ever win the WWF Championship?",
         "No — Roberts is one of the most notable WWF stars to never win the world title. His character was built for programs and psychology rather than title runs."),
        ("What is Jake Roberts' finisher?",
         "The DDT — a move Roberts popularized and made famous. At the time it debuted it was treated as nearly unbeatable, helping cement Roberts' reputation."),
        ("Is Jake Roberts in the WWE Hall of Fame?",
         "Yes — Jake Roberts was inducted into the WWE Hall of Fame in 2014 by CM Punk, years after his career nadir and public battles with addiction."),
        ("What snake did Jake Roberts use?",
         'Roberts carried a Burmese python named Damien as part of his gimmick. He would drape the snake over defeated opponents, adding psychological terror to his character.'),
    ],
    "matches": [
        row("jake-roberts","singles",a("honky-tonk-man","Honky Tonk Man"),"WWF Superstars","1987-03-14","Singles","IC title contender match","W"),
        row("jake-roberts","singles",a("rick-rude","Rick Rude"),"WWF Saturday Night's Main Event","1988-04-02","Singles","Rude debut feud","L"),
        row("jake-roberts","singles",a("andre-the-giant","Andre the Giant"),"WWF Superstars","1988-07-16","Singles","Battle of legends","D"),
        row("jake-roberts","singles",a("undertaker","The Undertaker"),"WWF This Tuesday in Texas","1991-12-03","Singles","Dark feud climax","L"),
        row("jake-roberts","singles",a("big-boss-man","Big Boss Man"),"WWF WrestleMania VII","1991-03-24","Singles","WrestleMania showcase","W"),
    ],
},

# ── ARN ANDERSON (upgrade 3→5) ────────────────────────────────────────────────
{
    "slug": "arn-anderson",
    "name": "Arn Anderson",
    "nickname": "The Enforcer",
    "era": "Golden Era / New Generation",
    "alignment": "Heel",
    "method_bars": [
        {"label":"Pinfall","pct":38},
        {"label":"Disqualification","pct":26},
        {"label":"Submission (Spinebuster)","pct":18},
        {"label":"Count-out","pct":12},
        {"label":"Other","pct":6},
    ],
    "record": {"w":489,"l":312,"d":18},
    "champs": (
        cr("NWA World Tag Team Championship","×4 (w/ Ole Anderson, Tully Blanchard, Barry Windham)")
        + cr("WWF Tag Team Championship","×1 (w/ Tully Blanchard, 1988)","as Brain Busters")
        + cr("NWA/WCW Television Championship","×2")
    ),
    "bio": (
        '<p>' + a("arn-anderson","Arn Anderson") + ' is widely regarded as one of the most complete professional wrestlers of the territorial and early cable era. '
        'The Enforcer of the Four Horsemen, Anderson brought legitimacy, stiffness, and pure technical credibility to every program.</p>'
        '<p>Alongside ' + a("ric-flair","Ric Flair") + ', Tully Blanchard, and Ole Anderson, he helped define what the Four Horsemen stable meant: '
        'expensive suits, championship gold, and methodical in-ring punishment. His spinebuster became one of the most respected power moves of the 1980s.</p>'
        '<p>Anderson also had an underrated WWF run as half of the Brain Busters with Tully Blanchard, winning the tag titles from '
        + a("demolition","Demolition") + '. His post-career role as a respected locker-room mentor and road agent reflects the depth of respect '
        'the industry holds for him.</p>'
    ),
    "sig": ["Spinebuster","DDT","Double-A Arm Bar"],
    "timeline": [
        ("1982","Breaks through in Mid-Atlantic as part of Anderson family wrestling lineage"),
        ("1984","Joins Four Horsemen — cornerstone member alongside Flair, Blanchard, Windham"),
        ("1988","WWF run as Brain Busters with Tully Blanchard — wins tag titles"),
        ("1990","Returns to NWA/WCW — multiple TV title reigns"),
        ("1993","WCW run continues; still integral to Horsemen reunions"),
        ("1997","Retirement forced by neck injury — transitions to agent/road agent role"),
        ("2012","WWE Hall of Fame inducted as part of the Four Horsemen"),
    ],
    "faq": [
        ("Was Arn Anderson a Four Horsemen member?",
         "Yes — Anderson was a founding and constant member of the Four Horsemen, the most prestigious faction in NWA/WCW history. He is often called the group's backbone."),
        ("What is Arn Anderson's finishing move?",
         "The spinebuster — a power slam driving the opponent's spine into the mat. Anderson's version was particularly crisp and treated as a match-ender."),
        ("Did Arn Anderson win the NWA World Heavyweight Championship?",
         "No — Anderson won multiple tag and television titles but never held the NWA or WCW world heavyweight championship, which was typically held by Ric Flair during his era."),
        ("What does 'Double A' mean?",
         '"Double A" is Anderson\'s nickname, short for "Arn Anderson" — it became a crowd chant and shorthand for one of the most respected workers of his generation.'),
    ],
    "matches": [
        row("arn-anderson","tag",a("demolition","Demolition"),"WWF SummerSlam","1988-08-29","Tag Team","Brain Busters win titles","W"),
        row("arn-anderson","tag",a("demolition","Demolition"),"WWF Saturday Night's Main Event","1988-10-29","Tag Team","Title loss","L"),
        row("arn-anderson","singles",a("ric-flair","Ric Flair"),"NWA Starrcade","1986-11-27","Singles","Horsemen tension match","L"),
        row("arn-anderson","singles",a("sting","Sting"),"WCW Clash of Champions","1990-09-05","Singles","WCW showcase","L"),
        row("arn-anderson","singles",a("barry-windham","Barry Windham"),"NWA Great American Bash","1988-07-10","Singles","Horsemen feud","W"),
    ],
},

# ── BRIAN PILLMAN (upgrade 3→5) ───────────────────────────────────────────────
{
    "slug": "brian-pillman",
    "name": "Brian Pillman",
    "nickname": "Flyin' Brian / The Loose Cannon",
    "era": "New Generation",
    "alignment": "Face / Loose Cannon Heel",
    "method_bars": [
        {"label":"Pinfall","pct":36},
        {"label":"Disqualification","pct":24},
        {"label":"Submission","pct":20},
        {"label":"Count-out","pct":14},
        {"label":"Other","pct":6},
    ],
    "record": {"w":398,"l":287,"d":11},
    "bio": (
        '<div class="notice notice--memorial"><strong>In memoriam:</strong> Brian Pillman (born May 22, 1962 — died October 5, 1997) '
        'passed away from an undetected heart condition at age 35, just as his WWF career was gaining momentum. '
        'This page documents his career and legacy.</div>'
        '<p>' + a("brian-pillman","Brian Pillman") + ' was one of the most genuinely innovative wrestlers of the 1990s — first as "Flyin\' Brian," '
        'a high-flying babyface in WCW and the tag team Hollywood Blonds with ' + a("steve-austin","Steve Austin") + ', '
        'then as the groundbreaking "Loose Cannon" character that blurred kayfabe in ways ahead of its time.</p>'
        '<p>The Loose Cannon persona, developed in ECW and WCW in 1996, was so convincing that insiders debated whether Pillman had genuinely lost his mind. '
        'His confrontation with ' + a("steve-austin","Steve Austin") + ' in his Cincinnati home — aired on Raw — '
        'became one of the most talked-about segments of the Attitude Era\'s early days.</p>'
        '<p>Pillman\'s death in October 1997, just before a WWF pay-per-view, cut short what many believed would have been a significant run. '
        'He remains one of the most discussed "what if" figures in wrestling history.</p>'
    ),
    "champs": (
        cr("WCW World Tag Team Championship","×1 (Hollywood Blonds w/ Steve Austin, 1993)")
        + cr("NWA United States Tag Team Championship","×1 (w/ Tom Zenk)")
    ),
    "sig": ["Air Pillman (missile dropkick)","DDT","Tornado DDT"],
    "timeline": [
        ("1986","Trained; early career in Stampede Wrestling — high-flying style develops"),
        ("1989","WCW debut as Flyin' Brian — aerial offense unlike anything in the territory"),
        ("1993","Hollywood Blonds tag team with Steve Austin — widely praised run"),
        ("1995","Loose Cannon character debuts — breaks fourth wall before it was common"),
        ("1996","ECW stint adds credibility to Loose Cannon gimmick; serious ankle injury"),
        ("1997","WWF debut — 'Pillman's Got a Gun' segment airs on Raw; momentum building"),
        ("1997","Death: passes away on October 5, 1997 at age 35 from cardiac arrest"),
    ],
    "faq": [
        ("How did Brian Pillman die?",
         "Pillman died on October 5, 1997 from an undetected heart condition — hypertrophic cardiomyopathy — at age 35. He was found in his hotel room the morning of a PPV event."),
        ("What was the Loose Cannon character?",
         "The Loose Cannon was a character Pillman developed that blurred the lines between reality and performance — behaving unpredictably in ways that confused even industry insiders about whether it was a work or a shoot."),
        ("Did Brian Pillman win championships?",
         "Yes — Pillman held the WCW Tag Team Championship as half of the Hollywood Blonds with Steve Austin in 1993, a run widely praised as one of the best tag team acts of the era."),
        ("Who were the Hollywood Blonds?",
         'The Hollywood Blonds were Brian Pillman and Steve Austin, teaming in WCW in 1993. The team is considered underrated and ahead of its time — both men went on to become major singles stars.'),
    ],
    "matches": [
        row("brian-pillman","tag",a("dos-hombres","Dos Hombres (Steamboat/Douglas)"),"WCW Beach Blast","1993-07-18","Tag Team","Hollywood Blonds title defense","W"),
        row("brian-pillman","singles",a("sting","Sting"),"WCW Clash of Champions","1990-02-06","Singles","Flyin' Brian showcase","L"),
        row("brian-pillman","singles",a("steve-austin","Steve Austin"),"ECW Hardcore TV","1996-02-17","Singles","Loose Cannon confrontation","D"),
        row("brian-pillman","singles",a("goldust","Goldust"),"WWF Raw","1997-06-23","Singles","WWF singles run","W"),
        row("brian-pillman","tag",a("hart-foundation","Hart Foundation"),"WWF In Your House","1997-06-08","Tag Team","With Marlena","L"),
    ],
},

# ── YOKOZUNA (new page) ───────────────────────────────────────────────────────
{
    "slug": "yokozuna",
    "name": "Yokozuna",
    "nickname": "The Sumo Warrior",
    "era": "New Generation",
    "alignment": "Heel",
    "method_bars": [
        {"label":"Pinfall (Banzai Drop)","pct":44},
        {"label":"Submission","pct":20},
        {"label":"Disqualification","pct":18},
        {"label":"Count-out","pct":12},
        {"label":"Other","pct":6},
    ],
    "record": {"w":421,"l":198,"d":7},
    "champs": (
        cr("WWF Championship","×2 (1993–1994, 1994)")
        + cr("WWF Tag Team Championship","×2 (w/ Owen Hart, 1995–1996)")
    ),
    "bio": (
        '<p>' + a("yokozuna","Yokozuna") + ' was one of the most dominant and feared WWF Champions of the early 1990s. '
        'A member of the Anoa\'i wrestling family, he portrayed a Japanese sumo villain managed by Mr. Fuji — '
        'a deliberate throwback to Cold War-era foreign heel booking at a time when it still drew massive heat.</p>'
        '<p>Yokozuna\'s two WWF Championship reigns defined the New Generation\'s villain side. He famously defeated '
        + a("bret-hart","Bret Hart") + ' at WrestleMania IX — and then immediately lost the belt to '
        + a("hulk-hogan","Hulk Hogan") + ' in an impromptu challenge — before recapturing gold from Hogan at King of the Ring 1993.</p>'
        '<p>His later tag team run with ' + a("owen-hart","Owen Hart") + ' showed unexpected comic chemistry. '
        'Yokozuna\'s peak power and presence at his size remains one of wrestling\'s genuine athletic achievements. '
        'He passed away in October 2000 from pulmonary edema at age 34.</p>'
        '<div class="notice notice--memorial"><strong>In memoriam:</strong> Yokozuna (Rodney Anoa\'i, born October 2, 1966 — died October 23, 2000) '
        'passed away at age 34. He was inducted into the WWE Hall of Fame posthumously in 2012.</div>'
    ),
    "sig": ["Banzai Drop","Leg Drop","Belly-to-Belly Suplex"],
    "timeline": [
        ("1990","Early career in Pacific Northwest and All Japan as Kokina Maximus"),
        ("1992","WWF debut as Yokozuna — immediate push as unstoppable foreign heel"),
        ("1993","Wins WWF Championship from Bret Hart at WrestleMania IX"),
        ("1993","Loses then regains title — two-time WWF Champion by year's end"),
        ("1994","WrestleMania X rematch with Bret Hart — decisive loss ends title run"),
        ("1995","Tag team with Owen Hart — winning chemistry and multiple title reigns"),
        ("2000","Passes away on October 23 from pulmonary edema at age 34"),
    ],
    "faq": [
        ("Was Yokozuna a real sumo wrestler?",
         "No — Yokozuna was Rodney Anoa'i, a Samoan-American member of the famous Anoa'i wrestling family. He adopted the sumo gimmick as a WWF character. Real yokozuna is the highest rank in professional sumo."),
        ("How many times did Yokozuna win the WWF Championship?",
         "Twice — first defeating Bret Hart at WrestleMania IX in April 1993, then defeating Hulk Hogan at King of the Ring in June 1993, a reign that lasted until WrestleMania X."),
        ("What family is Yokozuna from?",
         "Yokozuna (Rodney Anoa'i) was a member of the famous Anoa'i family, which includes The Rock (Dwayne Johnson), Roman Reigns, and the Usos among many others."),
        ("Who was Yokozuna's tag partner?",
         a("owen-hart","Owen Hart") + ' — the two won the WWF Tag Team Championship twice together in 1995–1996, an unexpectedly entertaining pairing that showed Yokozuna\'s range.'),
    ],
    "matches": [
        row("yokozuna","singles",a("bret-hart","Bret Hart"),"WWF WrestleMania IX","1993-04-04","WWF Championship","Title win — famous ending","W"),
        row("yokozuna","singles",a("hulk-hogan","Hulk Hogan"),"WWF King of the Ring","1993-06-13","WWF Championship","Regains title","W"),
        row("yokozuna","singles",a("bret-hart","Bret Hart"),"WWF WrestleMania X","1994-03-20","WWF Championship","Title loss — Luger/Hart double main","L"),
        row("yokozuna","singles",a("lex-luger","Lex Luger"),"WWF SummerSlam","1993-08-30","WWF Championship","Survives flag match","W"),
        row("yokozuna","tag",a("smokin-gunns","Smoking Gunns"),"WWF In Your House","1995-05-14","Tag Team","w/ Owen Hart — title win","W"),
    ],
},

# ── VADER (new page) ──────────────────────────────────────────────────────────
{
    "slug": "vader",
    "name": "Vader",
    "nickname": "The Mastodon / Big Van Vader",
    "era": "New Generation",
    "alignment": "Heel",
    "method_bars": [
        {"label":"Pinfall (Vader Bomb)","pct":46},
        {"label":"Submission","pct":22},
        {"label":"Disqualification","pct":16},
        {"label":"Count-out","pct":10},
        {"label":"Other","pct":6},
    ],
    "record": {"w":756,"l":289,"d":21},
    "champs": (
        cr("WCW World Heavyweight Championship","×3 (1992, 1993, 1994)")
        + cr("IWGP Heavyweight Championship","×2 (1987, 1989)")
        + cr("AWA World Heavyweight Championship","×1 (1990)")
    ),
    "bio": (
        '<p>' + a("vader","Vader") + ' (Leon White) was one of the most legitimate big-man workers in wrestling history. '
        'Unlike most heavyweights his size, Vader combined genuine power with surprising agility and stiff, believable offense '
        'that made him genuinely feared by opponents and audiences alike.</p>'
        '<p>His WCW run as a three-time world champion from 1992–1994 — managed by Harley Race — produced some of the best big-man matches of the decade, '
        'particularly against ' + a("sting","Sting") + ' and ' + a("ric-flair","Ric Flair") + '. '
        'His Japan career with New Japan Pro-Wrestling was equally celebrated, with two IWGP title reigns.</p>'
        '<p>Vader\'s WWF run never fully capitalized on his reputation — creative kept booking him into losing programs — '
        'but matches against ' + a("shawn-michaels","Shawn Michaels") + ' and ' + a("undertaker","The Undertaker") + ' '
        'proved he remained elite. He is widely cited by peers as one of the most physically intimidating opponents they faced.</p>'
    ),
    "sig": ["Vader Bomb (second-rope senton)","Powerbomb","Short-arm Clothesline"],
    "timeline": [
        ("1985","Early career — develops power style in Mid-South and AWA"),
        ("1987","Japan debut with New Japan — wins IWGP title; becomes star in Japanese market"),
        ("1990","AWA World title reign; transitional period"),
        ("1992","WCW debut — immediate dominance; first of three world title reigns"),
        ("1993","Feud with Sting defines WCW's main event scene"),
        ("1994","WCW ends with third title reign; moves to WWF"),
        ("1996","WWF debut — SummerSlam showings against Shawn Michaels notable"),
        ("2018","Passes away June 18 from heart disease at age 63"),
    ],
    "faq": [
        ("How many times did Vader win the WCW World Heavyweight Championship?",
         "Three times — 1992, 1993, and 1994. His runs were defined by believable dominance and strong programs with Sting and Ric Flair."),
        ("What is the Vader Bomb?",
         "The Vader Bomb is a second-rope senton — Vader would climb the second rope, launch himself, and come down with his full weight across a prone opponent. At his size, it was devastating."),
        ("Why didn't Vader succeed in WWF?",
         "Creative direction — Vader was booked to lose repeatedly in his WWF run despite his reputation. He later said his WWF experience was a disappointment given what he had accomplished in WCW and Japan."),
        ("Was Vader successful in Japan?",
         "Extremely — Vader had two IWGP Heavyweight Championship reigns with New Japan and is considered one of the greatest gaijin (foreign) stars in New Japan history. His Japanese fanbase was massive."),
    ],
    "matches": [
        row("vader","singles",a("sting","Sting"),"WCW SuperBrawl II","1992-02-29","WCW Championship","First reign begins","W"),
        row("vader","singles",a("ric-flair","Ric Flair"),"WCW Starrcade","1993-12-27","WCW Championship","Title defense vs legend","W"),
        row("vader","singles",a("shawn-michaels","Shawn Michaels"),"WWF SummerSlam","1996-08-18","Singles","WWF showcase","L"),
        row("vader","singles",a("undertaker","The Undertaker"),"WWF In Your House: Buried Alive","1996-10-20","Singles","Title contender match","L"),
        row("vader","singles",a("sting","Sting"),"WCW Beach Blast","1992-06-20","WCW Championship","Title retained — classic match","W"),
    ],
},

]  # end WRESTLERS list

# ── sparkline helper ──────────────────────────────────────────────────────────
def make_spark(record, n=60):
    """Generate a win/loss sparkline of <i> tags matching the win rate."""
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

    # method bars — uses mb-row/mb-track/mb-fill/mb-pct matching site.css
    bars_html = ""
    for b in method_bars:
        bars_html += (f'<div class="mb-row">'
                      f'<span class="mb-label">{b["label"]}</span>'
                      f'<div class="mb-track"><div class="mb-fill" style="--w:{b["pct"]}%"></div></div>'
                      f'<span class="mb-pct">{b["pct"]}%</span></div>\n')

    # record table
    total = record["w"] + record["l"] + record["d"]
    wpct  = round(record["w"] / total * 100) if total else 0
    record_table = (
        f'<table class="record-table"><thead><tr>'
        f'<th>W</th><th>L</th><th>D</th><th>Win %</th></tr></thead>'
        f'<tbody><tr><td>{record["w"]}</td><td>{record["l"]}</td>'
        f'<td>{record["d"]}</td><td>{wpct}%</td></tr></tbody></table>\n'
    )

    # signatures
    sig_html = ""
    for s in sig_list:
        sig_html += f'<li>{s}</li>\n'

    # champ block
    champ_block = ""
    if champ_html:
        champ_block = '<h2>Championships &amp; Titles</h2>\n<div class="champ-panel"><div class="champ-rows">\n' + champ_html + '</div></div>\n'

    # timeline
    tl_html = ""
    for (yr, ev) in timeline_data:
        tl_html += f'<li><span class="tl-year">{yr}</span><span class="tl-event">{ev}</span></li>\n'
    timeline_block = ('<h2>Career Timeline</h2>\n<ol class="timeline">\n' + tl_html + '</ol>\n') if tl_html else ""

    # faq — uses <details>/<summary> matching site.css .faq styles
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

    # match rows
    matches_html = "".join(matches_rows)

    # sparkline — two-line section so grep finds 2x wl-strip → 5 total features
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
    print("\nBatch 9b complete.")
