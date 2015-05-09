#!/usr/bin/python

import sys
k = 10
name = None
current_name = None
current_placeidset = []

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    try:
        name , placeid = line.strip().split("\t")
    except:
        continue 

    if name == current_name:
        current_placeidset.append(placeid)
    else:
        if current_name:
            pl = {}
            for p in current_placeidset:
                pl[p] = pl.get(p,0) + 1
            pref_places = sorted(pl, key = pl.get, reverse = True)    
            # output goes to STDOUT (stream data that the program writes)
            print("%s\t%s" %( current_name, ','.join(list(pref_places[:min(k,len(pref_places))])) ))
        current_name = name
        current_placeidset = []
        current_placeidset.append(placeid)

if current_name == name:
    pl = {}
    for p in current_placeidset:
        pl[p] = pl.get(p,0) + 1
    pref_places = sorted(pl, key = pl.get, reverse = True)    
    # output goes to STDOUT (stream data that the program writes)
    print("%s\t%s" %( current_name, ','.join(list(pref_places[:min(k,len(pref_places))])) ))