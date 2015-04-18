q3:
	hadoop jar /usr/hdp/2.2.0.0-2041/hadoop-mapreduce/hadoop-streaming-2.6.0.2.2.0.0-2041.jar -D mapred.reduce.tasks=10 -file q3/map.py -mapper q3/map.py -file q3/reduce.py -reducer q3/reduce.py -input /user/jx624/FOIL2011/trip_fare_*.csv  -output AverageTip
q6:
	hjs -D mapred.reduce.tasks=10 -file map.py -mapper map.py -file reduce.py -reducer reduce.py -input FOIL2010/trip_data*.csv -output q6_1_2010&
