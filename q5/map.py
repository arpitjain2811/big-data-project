#! /usr/bin/env python
import sys
import StringIO
import csv
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