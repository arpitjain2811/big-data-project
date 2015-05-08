#!/usr/bin/python

import sys

name = None
current_name = None
current_num_trips = 0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    name , count = line.strip().split("\t")

    try:
        count = int(count)
    except ValueError:
        continue

    if name == current_name:
        current_num_trips += count
    else:
        if current_name:
            # output goes to STDOUT (stream data that the program writes)
            print("%s\t%d" %( current_name, current_num_trips ))
        current_name = name
        current_num_trips = count

if current_name == name:
    print('%s\t%d' % (current_name, current_num_trips))