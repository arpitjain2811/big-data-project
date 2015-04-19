#!/usr/bin/python
import sys
import StringIO
import csv

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    csv_file = StringIO.StringIO(line)
    csv_reader = csv.reader(csv_file)

    for l in csv_reader:

        #l = line.strip().split(',')
        # Data from vehicle table

        if len(l) == 11:
            #tag = "fare"
            if l[0] == "medallion":
                attributes_fare = l
                continue
            else:
                print("%s\t%f\t%d" % (l[1],float(l[8]),1))