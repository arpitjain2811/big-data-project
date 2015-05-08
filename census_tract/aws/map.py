#!/usr/bin/env python
import sys
import csv
import StringIO
from shapely.geometry import Point
import geopandas as gpd
myShapefile = gpd.read_file('tract.shp')
# print(myShapefile.head())
countylist=['005','047','061','081','085']
nyc_tract=myShapefile[myShapefile.COUNTYFP.isin(countylist)]
# %matplotlib inline

# input comes from STDIN (stream data that goes to the program)
<<<<<<< Updated upstream
for line in sys.stdin:

    csv_file = StringIO.StringIO(line)
    csv_reader = csv.reader(csv_file)
    for l in csv_reader:
        if l[0] != "medallion":
            try:
                pickup_point=Point(float(l[10]),float(l[11]))
                l.append(str(nyc_tract.TRACTCE[nyc_tract.geometry.contains(pickup_point)].tolist()[0]))
            except:
                l.append('<o>')
            try:
                dropoff_point=Point(float(l[12]),float(l[13]))
                l.append(str(nyc_tract.TRACTCE[nyc_tract.geometry.contains(dropoff_point)].tolist()[0]))
            except:
                l.append('<o>')
            print ','.join(l)
=======
for input_line in sys.stdin:
    line = input_line.strip().split(',')
    if line[0] != "medallion":
        try:
            pickup_point=Point(float(line[10]),float(line[11]))
            line.append(str(nyc_tract.TRACTCE[nyc_tract.geometry.contains(pickup_point)].tolist()[0]))
        except:
            line.append('<o>')
        try:
            dropoff_point=Point(float(line[12]),float(line[13]))
            line.append(str(nyc_tract.TRACTCE[nyc_tract.geometry.contains(dropoff_point)].tolist()[0]))
        except:
            line.append('<o>')
        print ','.join(line)
>>>>>>> Stashed changes
