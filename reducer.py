#!/usr/bin/python

import sys


pageviewTotals = {}

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.           
        continue

    pagename, pageview = data
    pageviewTotals.setdefault(pagename, 0)
    pageviewTotals[pagename] += float(pageview)

for pagename in pageviewTotals:
    print "{0}\t{1}".format(pagename,pageviewTotals[pagename])


