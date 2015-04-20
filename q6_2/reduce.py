#!/usr/bin/env python
import sys, os
from datetime import datetime
current_driver = None
current_day=None
time_dur=0
for line in sys.stdin:
    line=line.strip()
    driver,day,dur=line.split(',')
    # until different day and driver 
    if current_driver==driver and current_day==day:
        time_dur+=float(dur)
    else:
        # start new day and driver
        if current_day and current_driver:
            hours=time_dur/3600.0
            print "%s,%s,%.2f"%(driver,day,hours)
        # first row 
        current_driver=driver
        current_day=day
        time_dur=float(dur)
if current_day and current_driver:
    hours=time_dur/3600.0
    print "%s,%s,%.2f"%(driver,day,hours)


