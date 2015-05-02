#!/usr/bin/python

import sys

current_hack = None
current_num_trips = 0
current_total = 0.0


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    hack, total , count = line.strip().split("\t")

    try:
        total = float(total)
        count = int(count)
    except ValueError:
        continue

    if hack == current_hack:
        current_total += total
        current_num_trips += count
    else:
        if current_hack:
            # output goes to STDOUT (stream data that the program writes)
            print("%s\t%f" %( current_hack, current_total ))
        current_hack = hack
        current_num_trips = count
        current_total = total

if current_hack == hack:
    print('%s\t%f' % (current_hack, current_total))