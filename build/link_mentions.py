#!/usr/bin/env python3
"""link_mentions.py - link the FIRST plain-text mention of a wrestler on a page.

    WL_ROOT="$PWD" python3 build/link_mentions.py <slug> <page> [<page> ...]

Only touches visible text inside the page body, after the shared header and before
the shared footer. Never links inside an existing <a>, a heading (h1-h3), <script>,
<style>, <title>, <button> or an attribute. One link per page per wrestler, and only
if the page does not already link that wrestler. Idempotent.
"""
import html, importlib.util, os, re, sys

ROOT = os.environ.get("WL_ROOT", os.getcwd())
spec = importlib.util.spec_from_file_location("bd", os.path.join(ROOT, "build", "build_dossier.py"))
bd = importlib.util.module_from_spec(spec); spec.loader.exec_module(bd)
bd._name_index()

def names_for(slug):
    return sorted([n for n, s in bd._NAME_MAP.items() if s == slug], key=len, reverse=True)

SKIP_OPEN = re.compile(r"<(a|h1|h2|h3|script|style|title|button|summary)\b", re.I)

def link_first(page, slug):
    s = open(page, encoding="utf-8").read()
    href = 'href="/wrestlers/%s/"' % slug
    start = s.find("</header>", s.find('<header class="site-header nav7"')) + 9
    end = s.rfind('<footer')
    if end < start: end = len(s)
    body = s[start:end]
    # already linked in the page body?
    if href in body:
        return "already linked"
    names = names_for(slug)
    if not names:
        return "no name"
    rx = re.compile(r"(?<![\w-])(%s)(?![\w-])" % "|".join(re.escape(html.escape(n, quote=False)) for n in names))
    out, i, depth_stack = [], 0, []
    for m in re.finditer(r"<[^>]+>", body):
        text = body[i:m.start()]
        if not depth_stack:
            mm = rx.search(text)
            if mm:
                new_text = text[:mm.start()] + '<a href="/wrestlers/%s/">%s</a>' % (slug, mm.group(1)) + text[mm.end():]
                s2 = s[:start] + body[:i] + new_text + body[m.start():] + s[end:]
                open(page, "w", encoding="utf-8").write(s2)
                return "linked %r" % mm.group(1)
        tag = m.group(0)
        o = SKIP_OPEN.match(tag)
        if o and not tag.endswith("/>"):
            depth_stack.append(o.group(1).lower())
        elif depth_stack and re.match(r"</%s\s*>" % depth_stack[-1], tag, re.I):
            depth_stack.pop()
        i = m.end()
    return "no plain mention"

if __name__ == "__main__":
    slug = sys.argv[1]
    for p in sys.argv[2:]:
        print("  %-55s %s" % (p, link_first(os.path.join(ROOT, p), slug)))
