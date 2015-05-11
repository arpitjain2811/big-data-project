#!/usr/bin/env python
import sys, os
from datetime import datetime

current_day=None
time_dur=0
for line in sys.stdin:
    line=line.strip()
    day,dur=line.split(',')
    # print driver,day,dur
#     # until different day and driver 
    if current_day==day:
        time_dur+=float(dur)
        # print time_dur
    else:
        # start new day and driver
        if current_day:
            hours=time_dur/3600.0
            print "%s,%.2f"%(current_day,hours)
            
            current_day=day
            time_dur=float(dur)
        # first row 
        else:
            
            current_day=day
            time_dur=float(dur)
if current_day:
    hours=time_dur/3600.0
    print "%s,%.2f"%(current_day,hours)


