#!/usr/bin/env python
import sys, os
import datetime
for line in sys.stdin:
    line=line.strip()
    values=line.split(',')
    if values[0]!='medallion':
        starttime=datetime.datetime.strptime(values[5],'%Y-%m-%d %H:%M:%S')
        dow=starttime.weekday()
        dur=float(values[8])
        print "%s,%s"%(dow,dur)
    
