#!/usr/bin/python

import sys

current_key = None
current_num_trips = 0


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    longi, lati , count = line.strip().split("\t")
    key = (longi,lati)

    try:
        count = int(count)
    except ValueError:
        continue

    if key == current_key:
        current_num_trips += count
    else:
        if current_key:
            # output goes to STDOUT (stream data that the program writes)
            print("%s\t%f" %( current_key, current_num_trips ))
        current_key = key
        current_num_trips = count

if current_key == key:
    print('%s\t%f' % (current_key, current_num_trips))