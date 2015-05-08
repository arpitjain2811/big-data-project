#!/usr/bin/python
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
# pickup_

# Fare Table
# medallion             0
# hack_license          1
# vendor_id             2
# pickup_datetime       3
# payment_type          4
# fare_amount           5
# surcharge             6
# mta_tax               7
# tip_amount            8
# tolls_amount          9
# total_amount          10

# Assuming pickup and dropoff neighbourhood at 14 and 15 index of csv file

import sys
import StringIO
import csv
from collections import defaultdict

# input comes from STDIN (stream data that goes to the program)
H = defaultdict(int)
for line in sys.stdin:

    csv_file = StringIO.StringIO(line)
    csv_reader = csv.reader(csv_file)


    for l in csv_reader:

        #l = line.strip().split(',')
        # Data from vehicle table

        if len(l) == 16:
            #tag = "trip"
            if l[0] == "medallion":
                attributes_fare = l
                continue
            else:
                H[l[15]] += 1

for i in H.keys():
    print("%s\t%d"%(i,H[i]))