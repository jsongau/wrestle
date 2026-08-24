#!/usr/bin/env python3
"""eventsdata.py - the ONE list of upcoming WWE premium live events.

Why this file exists, written down so nobody rebuilds the mistake:

Before this, "what is the next event" was stated in SIX places across two
files - the ticker strip, the production-truck vignette, the vignette's
countdown target, the floating widget's tab label, the widget body, and the
widget's own countdown target - each one a hand-typed copy. SummerSlam ran on
August 1-2 2026 and every one of those copies went on claiming it was next,
with a countdown frozen at 00/00/00/00, until a human noticed on August 24.

A fact stated in six places is a fact that will be wrong in five of them. This
module is the only place any of it is written down; build/patch_next_event.py
stamps it into the pages.

MAINTENANCE: when a show passes, you do not edit it out. `upcoming()` filters
by date, so the list self-advances. You only ever APPEND newly announced
shows, and you re-run the patcher.

Every entry carries `source` - the URL the date and venue were read from - so
a future session can re-verify rather than trust this file.
"""

# start: ISO 8601 with a real UTC offset, at the announced bell time.
#   Never a bare date: "2026-09-06" is midnight UTC, which is the evening of
#   Sep 5 in the US, and the countdown would hit zero a day early.
EVENTS = [
    {
        "slug":  "sunday-nights-main-event",
        "name":  "Sunday Night's Main Event",
        "short": "Sunday Night's Main Event",
        "start": "2026-09-06T20:00:00-04:00",
        "when":  "Sunday, Sep 6, 2026",
        "row":   "Sep 6",
        "venue": "State Farm Arena",
        "city":  "Atlanta, GA",
        "cityshort": "Atlanta",
        "nights": 1,
        "tickets": "https://www.ticketmaster.com/wwe-tickets/artist/807358",
        "source": "https://www.f4wonline.com/event-guides/wwe-2026-ple-list-ppv-schedule/",
    },
    {
        "slug":  "worlds-collide-2026",
        "name":  "WWE/AAA/NXT Worlds Collide",
        "short": "Worlds Collide",
        "start": "2026-09-26T19:30:00-05:00",
        "when":  "Saturday, Sep 26, 2026",
        "row":   "Sep 26",
        "venue": "Allstate Arena",
        "city":  "Rosemont, IL",
        "cityshort": "Rosemont",
        "nights": 1,
        "tickets": "https://www.ticketmaster.com/wweaaanxt-worlds-collide-rosemont-illinois-09-26-2026/event/040064EFEABD140C",
        "source": "https://rosemont.com/allstate/event/wwe-aaa-nxt-worlds-collide/",
    },
    {
        "slug":  "money-in-the-bank-2026",
        "name":  "Money in the Bank",
        "short": "Money in the Bank",
        "start": "2026-10-10T19:00:00-05:00",
        "when":  "Saturday, Oct 10, 2026",
        "row":   "Oct 10",
        "venue": "Smoothie King Center",
        "city":  "New Orleans, LA",
        "cityshort": "New Orleans",
        "nights": 1,
        "tickets": "https://www.ticketmaster.com/wwe-tickets/artist/807358",
        "source": "https://www.f4wonline.com/event-guides/wwe-2026-ple-list-ppv-schedule/",
    },
    {
        "slug":  "survivor-series-2026",
        "name":  "Survivor Series",
        "short": "Survivor Series",
        "start": "2026-11-28T19:00:00-06:00",
        "when":  "Saturday, Nov 28, 2026",
        "row":   "Nov 28",
        "venue": "Daikin Park",
        "city":  "Houston, TX",
        "cityshort": "Houston",
        "nights": 1,
        "tickets": "https://www.ticketmaster.com/wwe-tickets/artist/807358",
        "source": "https://www.f4wonline.com/event-guides/wwe-2026-ple-list-ppv-schedule/",
    },
]

import datetime as _dt


def _dtof(e):
    return _dt.datetime.fromisoformat(e["start"])


def upcoming(now=None):
    """Every event still in the future, soonest first.

    An event counts as upcoming until its bell time. A two-night show would
    want start-of-night-1 to end-of-night-2; none in the list are two-night,
    and inventing the window for a case that does not exist is how you get a
    bug the day one appears. Add `end` to the entry when that day comes.
    """
    now = now or _dt.datetime.now(_dt.timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=_dt.timezone.utc)
    return sorted([e for e in EVENTS if _dtof(e) > now], key=_dtof)


def next_event(now=None):
    up = upcoming(now)
    if not up:
        raise SystemExit(
            "eventsdata: every event in EVENTS is in the past.\n"
            "Nothing is being patched, because a homepage that says nothing "
            "is upcoming is better than one that lies about a show that "
            "already happened. Append the newly announced dates and re-run."
        )
    return up[0]


def also_on_sale(now=None, limit=3):
    return upcoming(now)[1:1 + limit]


if __name__ == "__main__":
    n = next_event()
    print("next:", n["name"], "-", n["when"], "-", n["venue"], n["city"])
    for e in also_on_sale():
        print("  also:", e["row"], e["short"], e["cityshort"])
