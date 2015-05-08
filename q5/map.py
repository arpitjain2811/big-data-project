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
for line in sys.stdin:
	values=line.strip().split(',')
	pickup_neighbor=values[14]
	dropoff_neighbor=values[15]
	driver=values[1]
	trip_dur=values[9]
	if pickup_neighbor!='UNKNOWN' and dropoff_neighbor!='UNKNOWN':
		print '%s,%s,%s,%s'%(driver,pickup_neighbor,dropoff_neighbor,trip_dur)