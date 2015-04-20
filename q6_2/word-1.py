#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    driver,date,hour = line.split(',')
    hour=float(hour)
    print '%.1f\t%s' % (hour, 1)
