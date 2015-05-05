q3:
	hadoop jar /usr/hdp/2.2.0.0-2041/hadoop-mapreduce/hadoop-streaming-2.6.0.2.2.0.0-2041.jar -D mapred.reduce.tasks=10 -file q3/map.py -mapper q3/map.py -file q3/reduce.py -reducer q3/reduce.py -input /user/jx624/FOIL*/trip_fare_*.csv  -output AverageTip
q4:
	hadoop jar /usr/hdp/2.2.0.0-2041/hadoop-mapreduce/hadoop-streaming-2.6.0.2.2.0.0-2041.jar -D mapreduce.job.reduces=10 -D stream.num.map.output.key.fields=2 -file q4/map.py -mapper q4/map.py -file q4/reduce.py -reducer q4/reduce.py -input /user/jx624/FOIL2013/trip_data_*.csv  -output AverageTripbtwpoints
q6:
	hjs -D mapred.reduce.tasks=10 -file map.py -mapper map.py -file reduce.py -reducer reduce.py -input FOIL2010/trip_data*.csv -output q6_1_2010&
extra:
    hadoop jar /usr/hdp/2.2.0.0-2041/hadoop-mapreduce/hadoop-streaming-2.6.0.2.2.0.0-2041.jar -D mapreduce.job.reduces=10 -file extra/map.py -mapper extra/map.py -file extra/reduce_bins.py -reducer extra/reduce_bins.py -input /user/jx624/FOIL2013/trip_fare_*.csv  -output HacksBin
below:
	hadoop jar /usr/hdp/2.2.0.0-2041/hadoop-mapreduce/hadoop-streaming-2.6.0.2.2.0.0-2041.jar -file extra/map_below.py -mapper extra/map_below.py -file extra/reduce_below.py -reducer extra/reduce_below.py -input /user/jx624/FOIL2013/trip_fare_*.csv  -output Hackbelow
weather:
	hadoop jar /usr/hdp/2.2.0.0-2041/hadoop-mapreduce/hadoop-streaming-2.6.0.2.2.0.0-2041.jar -file Weather_data_corr/map_vendor.py -mapper Weather_data_corr/map_vendor.py -file Weather_data_corr/reduce.py -reducer Weather_data_corr/reduce.py -input /user/jx624/FOIL2013/trip_fare_*.csv  -output Vendor_total
