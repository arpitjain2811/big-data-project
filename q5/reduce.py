# Create external table trip2013
# (hack_license string, pickup_datetime string,total_dur string) 
# row format delimited 
# fields terminated by ',' 
# lines terminated by '\n' 
# location 'alldriver-2013';


# longger routes:
#! /usr/bin/env python
# Trip Table
# medallion             0
# hack_license          1
# vendor_id             2
# rate_code             3
# store_and_fwd_flag    4
# pickup_datetime       5
# dropoff_datetime      6
# passenger_count       7
# trip_time_in_secs     8
# trip_distance         9
# pickup_longitude      10
# pickup_latitude       11
# dropoff_longitude     12
# dropoff_latitude      13
import sys      
pickup=None
dropoff=None
dur=.0
count=0
for line in sys.stdin:
		# print line
	driver,pickup_neighbor,dropoff_neighbor,trip_dur=line.strip().split(',')
	trip_dur=float(trip_dur)
	# print trip_dur,count
	if pickup==pickup_neighbor and dropoff==dropoff_neighbor:
		dur+=trip_dur
		count+=1
	else:
		if pickup and dropoff:
			print pickup+','+dropoff+','+str(dur/count)
			pickup=pickup_neighbor
			dropoff=dropoff_neighbor
			dur=trip_dur
			count=1
		else:
			pickup=pickup_neighbor
			dropoff=dropoff_neighbor
			dur+=trip_dur
			count+=1
# print key+','+str(dur/count)