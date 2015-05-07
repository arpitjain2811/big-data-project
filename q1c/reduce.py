#!/usr/bin/python

import sys

current_ID = None
current_num_trips = 0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    id , count = line.strip().split("\t")

    try:
        count = int(count)
    except ValueError:
        continue

    if id == current_ID:
        current_num_trips += count
    else:
        if current_ID:
            # output goes to STDOUT (stream data that the program writes)
            print("%s\t%f" %( current_ID, current_num_trips ))
        current_ID = id
        current_num_trips = count

if current_ID == id:
    print('%s\t%f' % (current_ID, current_num_trips))