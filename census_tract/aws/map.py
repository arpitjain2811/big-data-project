#!/usr/bin/env python
import sys
sys.path.append('.')
import matplotlib
matplotlib.use('Agg')
from matplotlib.path import Path
from rtree import index as rtree
import numpy, shapefile, time

def findNeighborhood(location, index, neighborhoods):
    match = index.intersection((location[0], location[1], location[0], location[1]))
    for a in match:
        if any(map(lambda x: x.contains_point(location), neighborhoods[a][1])):
            return a
    return -1

def readNeighborhood(shapeFilename, index, neighborhoods):
    sf = shapefile.Reader(shapeFilename)
    for sr in sf.shapeRecords():
        if sr.record[1] not in ['005', '047', '061', '081','085']: continue
        paths = map(Path, numpy.split(sr.shape.points, sr.shape.parts[1:]))
        bbox = paths[0].get_extents()
        map(bbox.update_from_path, paths[1:])
        index.insert(len(neighborhoods), list(bbox.get_points()[0])+list(bbox.get_points()[1]))
        neighborhoods.append((sr.record[2], paths))
    neighborhoods.append(('UNKNOWN', None))

def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        values = line.split(',')
        if len(values)>1 and values[0]!='medallion': 
            yield values

def mapper():
    index = rtree.Index()
    neighborhoods = []
    readNeighborhood('cb_2013_36_tract_500k.shp', index, neighborhoods)
    agg = {}
    for values in parseInput():
        try:
            pickup_location = (float(values[10]), float(values[11]))
            dropoff_location = (float(values[12]), float(values[13]))
            dropoff_neighborhood = findNeighborhood(dropoff_location, index, neighborhoods)
            pickup_neighborhood = findNeighborhood(pickup_location, index, neighborhoods)
            if pickup_neighborhood!=-1:
                pickup_name = neighborhoods[pickup_neighborhood][0]
            else:
                pickup_name = "UNKNOWN"
            if dropoff_neighborhood!=-1:
                dropoff_name = neighborhoods[dropoff_neighborhood][0]
            else:
                dropoff_name = "UNKNOWN"    
            values.append(str(pickup_name))
            values.append(str(dropoff_name))
            print ','.join(values)
        except:
            values.append("UNKNOWN")
            values.append("UNKNOWN")
            print ','.join(values)
    
if __name__=='__main__':
    mapper()
