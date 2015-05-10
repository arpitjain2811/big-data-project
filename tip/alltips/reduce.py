#!/usr/bin/python

import sys

current_date = None
current_tip = 0
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    date, tip = line.strip().split("\t")
    try:
        tip = float(tip)
    except ValueError:
        continue

    if date == current_date:
        current_tip += tip
    else:
        if current_date:
            # output goes to STDOUT (stream data that the program writes)
            print("%s\t%f" %( current_date,current_tip ))
        current_date = date
        current_tip = tip

if current_date == date:
    print("%s\t%f" %( current_date,current_tip ))
