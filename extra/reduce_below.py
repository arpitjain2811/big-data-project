#!/usr/bin/python

import sys

current_date = None
current_total_amount = 0.0
current_num_trips = 0.0
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    date, total_amount, num_trips = line.strip().split("\t")

    try:
        total_amount = float(total_amount)
        num_trips = float(num_trips)
    except ValueError:
        continue

    if date == current_date:
        current_total_amount += total_amount
        current_num_trips += num_trips
    else:
        if current_date:
            # output goes to STDOUT (stream data that the program writes)
            print("%s,%.2f,%.2f,%.2f,%.2f" %( current_date, current_total_amount,current_num_trips ))
        current_date = date
        current_total_amount = total_amount
        current_num_trips = num_trips

if current_date == date:
    print("%s,%.2f,%.2f,%.2f,%.2f" %( current_date, current_total_amount,current_num_trips ))
