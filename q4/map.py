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

        if len(l) == 14:
            #tag = "fare"
            if l[0] == "medallion":
                attributes_trip = l
                continue
            else:
                print("%f\t%f\t%d" % (float(l[10]),float(l[11]),1))