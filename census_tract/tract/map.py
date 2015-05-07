#!/usr/bin/python
import sys
import csv
from shapely.geometry import Point
import geopandas as gpd
myShapefile = gpd.read_file('tract.shp')
# print(myShapefile.head())
countylist=['005','047','061','081','085']
nyc_tract=myShapefile[myShapefile.COUNTYFP.isin(countylist)]
# %matplotlib inline

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    csv_reader = line.strip().split(',')
    for line in csv_reader:
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