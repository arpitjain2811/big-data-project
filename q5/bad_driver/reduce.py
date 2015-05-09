#!/usr/bin/env python
import sys 
import StringIO
import csv     
pickup=None
dropoff=None
dur=.0
count=0
for line in sys.stdin:
	driver,pickup_neighbor,dropoff_neighbor,trip_dur=line.strip('\t').split(',')
	trip_dur=float(trip_dur)
	# print trip_dur,count
	if pickup==pickup_neighbor and dropoff==dropoff_neighbor:
		dur+=trip_dur
		count+=1
	else:
		if pickup and dropoff:
			print pickup+','+dropoff+','+str(dur/count)+','+str(count)
			pickup=pickup_neighbor
			dropoff=dropoff_neighbor
			dur=trip_dur
			count=1
		else:
			pickup=pickup_neighbor
			dropoff=dropoff_neighbor
			dur+=trip_dur
			count+=1
print pickup+','+dropoff+','+str(dur/count)+','+str(count)
