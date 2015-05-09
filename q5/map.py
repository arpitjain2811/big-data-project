#! /usr/bin/env python
import sys
import StringIO
import csv
for line in sys.stdin:
	values=line.strip('\t').strip('\n').split(',')
	pickup_neighbor=values[14].strip('\t').strip('\n')
	dropoff_neighbor=values[15].strip('\t').strip('\n')
	driver=values[1].strip('\t').strip('\n')
	trip_dur=values[9].strip('\t').strip('\n')
	if pickup_neighbor!='UNKNOWN' and dropoff_neighbor!='UNKNOWN':
		print '%s,%s,%s,%s'%(driver,pickup_neighbor,dropoff_neighbor,trip_dur)