#!/usr/bin/env python
import sys, os
import datetime
for line in sys.stdin:
    line=line.strip()
    values=line.split(',')
    if values[0]!='medallion':
		starttime=datetime.datetime.strptime(values[5],'%Y-%m-%d %H:%M:%S')
		endtime=starttime+datetime.timedelta(seconds=float(values[8]))
		print "%s,%s,%s"%(values[1],datetime.datetime.strftime(starttime,'%Y-%m-%d'),datetime.datetime.strftime(starttime,'%H:%M:%S'))
		print "%s,%s,%s"%(values[1],datetime.datetime.strftime(endtime,'%Y-%m-%d'),datetime.datetime.strftime(endtime,'%H:%M:%S'))
