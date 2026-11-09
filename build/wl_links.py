#!/usr/bin/env python3
"""wl_links.py - the ONE internal-linking engine for every page family.

Every generator imports link_page() and runs it on a page before writing it; the
hand-authored pages get it from build/link_sitewide.py. All of them share the same
entity index (wrestlers, tag teams, titles, factions, events) built from disk by
build_dossier._name_index(), so a page added anywhere becomes a link target
everywhere on the next build. Rules (enforced by build_dossier.prose_autolink):
first plain-text mention only, one link per target per page, never the page's own
subject, never inside an existing link, heading, nav, script, form control or SVG.
Only the page body is touched: the shared header and footer are left alone.
"""
import importlib.util, os

ROOT = os.environ.get("WL_ROOT", os.getcwd())
_bd = None

def _engine():
    global _bd
    if _bd is None:
        spec = importlib.util.spec_from_file_location("wl_bd", os.path.join(ROOT, "build", "build_dossier.py"))
        _bd = importlib.util.module_from_spec(spec); spec.loader.exec_module(_bd)
    return _bd

def link_page(html, rel_path):
    """rel_path like 'events/backlash-2026/index.html' or '/lore-feed/2026-11-02/'."""
    bd = _engine()
    rel = rel_path.strip("/")
    if rel.endswith("index.html"):
        rel = rel[: -len("index.html")].strip("/")
    parts = rel.split("/")
    bd._SELF = parts[1] if (len(parts) == 2 and parts[0] == "wrestlers") else "/%s/" % rel
    h0 = html.find('<header class="site-header nav7"')
    start = html.find("</header>", h0) + 9 if h0 >= 0 else html.find("<body")
    end = html.rfind("<footer")
    if end < start:
        end = html.rfind("</body>")
    if start < 9 or end <= start:
        return html
    body = bd.prose_autolink([html[start:end]])[0]
    return html[:start] + body + html[end:]
