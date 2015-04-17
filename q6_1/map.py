#!/usr/bin/env python
import sys, os
for line in sys.stdin:
    line=line.strip()
    values=line.split(',')
    if values[0]!='medallion':
		day1,time1=values[5].split(' ')
		day2,time2=values[6].split(' ')
		print "%s,%s,%s"%(values[1],day1,time1)
		print "%s,%s,%s"%(values[1],day2,time2)
