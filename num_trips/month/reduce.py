#!/usr/bin/python

import sys

current_date = None
current_num_trips = 0
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    date, num_trips = line.strip().split("\t")
    try:
        num_trips = int(num_trips)
    except ValueError:
        continue

    if date == current_date:
        current_num_trips += num_trips
    else:
        if current_date:
            # output goes to STDOUT (stream data that the program writes)
            print("%s\t%d" %( current_date,current_num_trips ))
        current_date = date
        current_num_trips = num_trips

if current_date == date:
    print("%s\t%d" %( current_date,current_num_trips ))
