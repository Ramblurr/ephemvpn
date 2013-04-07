import datetime
import time

#
# From the django project
# https://github.com/django/django/blob/4a103086d5c67fa4fcc53c106c9fdf644c742dd8/django/utils/timesince.py
# Copyright (c) Django Software Foundation and individual contributors.
# All rights reserved.

def ungettext(a,b,count):
    if count:
        return b
    return a

def ugettext(a):
    return a

def timesince(d, now=None, reversed=False):
    """
Takes two datetime objects and returns the time between d and now
as a nicely formatted string, e.g. "10 minutes". If d occurs after now,
then "0 minutes" is returned.

Units used are years, months, weeks, days, hours, and minutes.
Seconds and microseconds are ignored. Up to two adjacent units will be
displayed. For example, "2 weeks, 3 days" and "1 year, 3 months" are
possible outputs, but "2 weeks, 3 hours" and "1 year, 5 days" are not.

Adapted from http://blog.natbat.co.uk/archive/2003/Jun/14/time_since
"""
    chunks = (
      (60 * 60 * 24 * 365, lambda n: ungettext('year', 'years', n)),
      (60 * 60 * 24 * 30, lambda n: ungettext('month', 'months', n)),
      (60 * 60 * 24 * 7, lambda n : ungettext('week', 'weeks', n)),
      (60 * 60 * 24, lambda n : ungettext('day', 'days', n)),
      (60 * 60, lambda n: ungettext('hour', 'hours', n)),
      (60, lambda n: ungettext('minute', 'minutes', n))
    )
    # Convert datetime.date to datetime.datetime for comparison.
    if not isinstance(d, datetime.datetime):
        d = datetime.datetime(d.year, d.month, d.day)
    if now and not isinstance(now, datetime.datetime):
        now = datetime.datetime(now.year, now.month, now.day)

    if not now:
        now = datetime.datetime.now(None)

    delta = (d - now) if reversed else (now - d)
    # ignore microseconds
    since = delta.days * 24 * 60 * 60 + delta.seconds
    if since <= 0:
        # d is in the future compared to now, stop processing.
        return '0 ' + ugettext('minutes')
    for i, (seconds, name) in enumerate(chunks):
        count = since // seconds
        if count != 0:
            break
    s = ugettext('%(number)d %(type)s') % {'number': count, 'type': name(count)}
    if i + 1 < len(chunks):
        # Now get the second item
        seconds2, name2 = chunks[i + 1]
        count2 = (since - (seconds * count)) // seconds2
        if count2 != 0:
            s += ugettext(', %(number)d %(type)s') % {'number': count2, 'type': name2(count2)}
    return s

def timeuntil(d, now=None):
    """
Like timesince, but returns a string measuring the time until
the given time.
"""
    return timesince(d, now, reversed=True)


def readable_delta(from_dt, time_s):
    dt = datetime.datetime.fromtimestamp(time.mktime(time_s)+2) # add 2 to count for compute delay
    return timeuntil(dt, from_dt)
