#!/usr/bin/python

import sys

current_hack = None
current_num_trips = 0
current_tip = 0.0


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    hack, tip , count = line.strip().split("\t")

    try:
        tip = float(tip)
        count = int(count)
    except ValueError:
        continue

    if hack == current_hack:
        current_tip += tip
        current_num_trips += count
    else:
        if current_hack:
            # output goes to STDOUT (stream data that the program writes)
            print("%s\t%f" %( current_hack, current_tip/current_num_trips ))
        current_hack = hack
        current_num_trips = count
        current_tip = tip

if current_hack == hack:
    print('%s\t%f' % (current_hack, current_tip/current_num_trips))