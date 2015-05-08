#!/usr/bin/env python
import sys, os
for line in sys.stdin:
    line=line.strip()
    values=line.split(',')
    # skip header
    if values[1]=='2013000944':
        date,time=values[5].split(' ')
        print "%s,%s,%s"%(values[1],date,values[8])


