#!/usr/bin/python

import sys

current_branch = None
current_num_trips = 0
current_trip_distance = 0.0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    branch, trip_distance, num_trips = line.strip().split("\t")
    try:
        num_trips = int(num_trips)
        trip_distance = float(trip_distance)
    except ValueError:
        continue

    if branch == current_branch:
        current_num_trips += num_trips
        current_trip_distance += trip_distance
    else:
        if current_branch:
            # output goes to STDOUT (stream data that the program writes)
            print("%s\t%f" %( current_branch,current_trip_distance/current_num_trips ))
        current_branch = branch
        current_num_trips = num_trips
        current_trip_distance = trip_distance

if current_branch == branch:
    print("%s\t%f" %( current_branch,current_trip_distance/current_num_trips ))
