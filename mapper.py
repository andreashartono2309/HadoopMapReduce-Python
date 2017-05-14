#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 5:
        page, date, pageview, activeserver, inactiveserver = data
        print "{0}\t{1}".format(page, pageview)

