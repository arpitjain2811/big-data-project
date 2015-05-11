#! /usr/bin/env python

lookuptable={}
# i=0
import sys
import StringIO
import csv
import datetime

with open('lookuptable') as f:
    for line in f:
        values=line.strip().strip('\n').split('\t')
        lookuptable[values[0]]=float(values[1])
        # i+=1
# print i,len(lookuptable)
for line in sys.stdin:
    line=line.strip()
    l=line.split(',')
    # print l
    if l[0] != 'medallion':
        try:
            driver=l[1]
            pickup = l[14]
            dropoff = l[15]
            key = pickup + '|' + dropoff
            evil_score=(float(l[9])-lookuptable[key])/lookuptable[key]
            if evil_score>0:
                print driver+','+str(evil_score)
        except:
            pass 