import geopandas as gpd
import sys
myShapefile = gpd.read_file('tract.shp')
# print(myShapefile.head())
countylist=['005','047','061','081','085']
nyc_tract=myShapefile[myShapefile.COUNTYFP.isin(countylist)]
print 'tracts loaded'# %matplotlib inline
from shapely.geometry import Point
from pandas import DataFrame as df
test=df.from_csv(sys.argv[1],index_col=None)
print 'file loaded'
test.columns=[u'medallion', u'hack_license', u'vendor_id', u'rate_code', u'store_and_fwd_flag', u'pickup_datetime', u'dropoff_datetime', u'passenger_count', u'trip_time_in_secs', u'trip_distance', u'pickup_longitude', u'pickup_latitude', u'dropoff_longitude', u'dropoff_latitude']
test['pickup_tract']='<o>'
test['dropoff_tract']='<o>'
print 'value initiated'
for i in xrange(len(test.index)):
    print 'process'+str(i)+'lines'
    try:
        pickup_point=Point(test.pickup_longitude[i],test.pickup_latitude[i])
        test.loc[i,'pickup_tract']=nyc_tract.TRACTCE[nyc_tract.geometry.contains(pickup_point)].tolist()[0]
    except:
        pass
    try:
        dropoff_point=Point(test.dropoff_longitude[i],test.dropoff_latitude[i])
        test.loc[i,'dropoff_tract']=nyc_tract.TRACTCE[nyc_tract.geometry.contains(dropoff_point)].tolist()[0]
    except:
        pass
print 'saving to file'+sys.argv[1]+'.1'
test.to_csv(sys.argv[1]+'.1')

