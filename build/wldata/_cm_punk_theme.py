"""cm-punk's walk-out data — the source of truth for a HAND-SPLICED module.

/wrestlers/cm-punk/ is hand-authored, not generated, so build_dossier.py never
reads this file: load_all() skips any wldata module whose name starts with "_".
It lives here so the module on that page stays reproducible. To re-render it:

    import importlib.util, os
    os.environ["WL_ROOT"] = os.getcwd()
    def _m(n, p):
        s = importlib.util.spec_from_file_location(n, p)
        m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
    bd = _m("bd", "build/build_dossier.py")
    th = _m("th", "build/wldata/_cm_punk_theme.py")
    band = bd.theme_band({"theme": th.THEME})   # splice between </header> and .layout

Every fact below is sourced; see the "foot" line, which ships on the page.
  track / album / year / Grammy ... en.wikipedia.org/wiki/Cult_of_Personality_(song)
                                    grammy.com/awards/categories/hard-rock-performance/1990/
  spotify_id (Vivid, 4:54) ........ open.spotify.com oEmbed for the track URL
  July 25, 2011 Raw debut ......... ultimateclassicrock.com/cm-punk-cult-of-personality/
                                    cagesideseats.com 2011/7/26
  licensed master, contract demand  Punk on The Morning Mosh Pit, via WrestleZone
  WrestleMania 29 / 41 live band .. ultimateclassicrock.com ; bleacherreport.com 25188332
  This Fire Burns 2006-2011 ....... songfacts.com/facts/killswitch-engage/this-fire
  Miseria Cantare (ROH) ........... fightful.com (Punk's ROH intro, revived later)
  Malcolm X opening sample ........ faroutmagazine.co.uk story-behind-the-song
"""

THEME = {
  "kicker": "Entrance theme",
  "since": "since Raw, July&nbsp;25, 2011",
  "track": "Cult of Personality",
  "artist": "Living Colour",
  "meta": "Vivid &middot; 1988 &middot; 4:54 &middot; Grammy, Best Hard Rock Performance, 1990",
  "note": ("WWE writes its own entrance music and almost never rents anyone else&rsquo;s. Punk put the "
           "real Living Colour master on a list of contract demands he expected Vince McMahon to refuse; "
           "McMahon said yes to all of it. At WrestleMania 29 and again at 41, the band played it live "
           "on the ramp."),
  "cue": {
    "quote": "And during the few moments that we have left&hellip;",
    "src": ("Malcolm X, <i>Message to the Grass Roots</i> &mdash; the sample that opens the record, and "
            "the first thing the arena hears. Then the riff lands, and the building goes with it."),
  },
  "spotify_id": "5e3YOg6fIkP0wD5TyxcHOH",
  "source_label": "Player &middot; Spotify",
  "links": [
    {"svc": "Spotify", "sub": "Full track · Vivid, 1988",
     "href": "https://open.spotify.com/track/5e3YOg6fIkP0wD5TyxcHOH"},
    {"svc": "Apple Music", "sub": "Vivid · 2023 remaster",
     "href": "https://music.apple.com/us/album/vivid-2023-remaster/273290580"},
    {"svc": "YouTube", "sub": "Official video · LivingColourVEVO",
     "href": "https://www.youtube.com/watch?v=7xxgRUyzgs0"},
  ],
  "lineage": [
    {"date": "2005", "title": "Miseria Cantare", "who": "AFI &middot; Ring of Honor"},
    {"date": "2006", "title": "This Fire Burns", "who": "Killswitch Engage &middot; WWE"},
    {"date": "2011", "title": "Cult of Personality", "who": "Living Colour &middot; WWE, AEW", "now": True},
    {"date": "2023", "title": "2023 remaster", "who": "Survivor Series return"},
  ],
  "foot": ('Dated to Raw, July 25, 2011. Sources: '
           '<a href="https://www.grammy.com/awards/categories/hard-rock-performance/1990/" '
           'target="_blank" rel="noopener">Grammy.com</a>, '
           '<a href="https://ultimateclassicrock.com/cm-punk-cult-of-personality/" '
           'target="_blank" rel="noopener">Ultimate Classic Rock</a>, '
           '<a href="https://bleacherreport.com/articles/25188332-living-colour-plays-cult-personality-'
           'cm-punks-wwe-wrestlemania-41-entrance" target="_blank" rel="noopener">Bleacher Report</a>.'),
}
