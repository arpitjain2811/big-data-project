#! /usr/bin/env python
import sys
import StringIO
import csv
lookuptable={}
with open('average-routes') as f:
	for line in f:
		values=line.strip().split(',')
		if ','.join(values[:2]) in lookuptable:
			print 'duplicates'
		else:
			lookuptable[','.join(values[:2])]=values[2]

for line in sys.stdin:
	csv_file = StringIO.StringIO(line.strip())
	csv_reader = csv.reader(csv_file)
	for values in csv_reader:
		pickup_neighbor=values[14]
		dropoff_neighbor=values[15]
		driver=values[1]
		trip_dur=values[9]
		if pickup_neighbor!='UNKNOWN' and dropoff_neighbor!='UNKNOWN':
			print '%s,%s,%s,%s'%(driver,pickup_neighbor,dropoff_neighbor,trip_dur)