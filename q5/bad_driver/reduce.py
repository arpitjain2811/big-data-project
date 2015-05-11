#!/usr/bin/python

import sys

current_diver = None
current_score = 0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    driver,score= line.strip().split(",")
    try:
        score= float(score)
    except ValueError:
        continue

    if driver == current_driver:
        current_score += score
    else:
        if current_driver:
            # output goes to STDOUT (stream data that the program writes)
            print("%s,%f" %( current_driver,current_score ))
        current_driver = driver
        current_score = score

if current_driver == driver:
    print("%s,%f" %( current_driver,current_score ))
