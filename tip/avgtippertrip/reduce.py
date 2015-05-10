#!/usr/bin/python

import sys

current_date = None
current_tip = 0.0
current_ntrip = 0
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    date, tip, ntrip = line.strip().split("\t")
    try:
        tip = float(tip)
        ntrip = int(ntrip)
    except ValueError:
        continue

    if date == current_date:
        current_tip += tip
        current_ntrip += ntrip
    else:
        if current_date:
            # output goes to STDOUT (stream data that the program writes)
            print("%s\t%f" %( current_date,current_tip/ntrip ))
        current_date = date
        current_tip = tip
        current_ntrip = ntrip

if current_date == date:
    print("%s\t%f" %( current_date,current_tip/ntrip ))
