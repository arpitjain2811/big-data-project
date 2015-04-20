#!/usr/bin/env python
import sys, os
for line in sys.stdin:
    line=line.strip()
    values=line.split(',')
    # skip header
    if values[0]!='medallion':
        date,time=values[5].split(' ')
        print "%s,%s,%s"%(values[1],date,values[8])


