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
            if current_total < 36000.0:
                print("%s\t%s\t%f" %( current_hack,"below", current_total ))
            elif current_total > 82000.0:
                print("%s\t%s\t%f" %( current_hack,"above", current_total ))
            else:
                print("%s\t%s\t%f" %( current_hack,"average" ,current_total ))

        current_hack = hack
        current_num_trips = count
        current_total = total

if current_hack == hack:
    if current_total < 36000.0:
        print("%s\t%s\t%f" %( current_hack,"below", current_total ))
    elif current_total > 82000.0:
        print("%s\t%s\t%f" %( current_hack,"above", current_total ))
    else:
        print("%s\t%s\t%f" %( current_hack,"average" ,current_total ))