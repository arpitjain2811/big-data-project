#!/usr/bin/python

import sys

current_hack = None
current_num_trips = 0
current_total = 0.0
current_tip = 0.0
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    hack, num_trips, total, tip = line.strip().split("\t")
    try:
        num_trips = int(num_trips)
        total = float(total)
        tip = float(tip)
    except ValueError:
        continue

    if hack == current_hack:
        current_num_trips += num_trips
        current_total += total
        current_tip += tip
    else:
        if current_hack:
            # output goes to STDOUT (stream data that the program writes)
            print("%s\t%d" %( current_hack,current_num_trips,current_total,current_total/current_num_trips,current_tip,current_tip/current_num_trips ))
        current_hack = hack
        current_num_trips = num_trips
        current_total = total
        current_tip = tip

if current_hack == hack:
    print("%s\t%d" %( current_hack,current_num_trips,current_total,current_total/current_num_trips,current_tip,current_tip/current_num_trips ))
