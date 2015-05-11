#!/usr/bin/env python
import sys 
import StringIO
import csv     
pickup=None
dropoff=None
dis=.0
count=0
for line in sys.stdin:
	driver,pickup_neighbor,dropoff_neighbor,trip_dis=line.strip('\t').split(',')
	trip_dis=float(trip_dis)
	# print trip_dis,count
	if pickup==pickup_neighbor and dropoff==dropoff_neighbor:
		dis+=trip_dis
		count+=1
	else:
		if pickup and dropoff:
			if count==1:
				pass
			else:
				print pickup+','+dropoff+','+str(dis/count)+','+str(count)
				pickup=pickup_neighbor
				dropoff=dropoff_neighbor
				dis=trip_dis
				count=1
		else:
			pickup=pickup_neighbor
			dropoff=dropoff_neighbor
			dis+=trip_dis
			count+=1
if count==1:
	pass
else:
	print pickup+','+dropoff+','+str(dis/count)+','+str(count)
