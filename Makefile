q3:
	hadoop jar /usr/hdp/2.2.0.0-2041/hadoop-mapreduce/hadoop-streaming-2.6.0.2.2.0.0-2041.jar -D mapred.reduce.tasks=10 -file q3/map.py -mapper q3/map.py -file q3/reduce.py -reducer q3/reduce.py -input /user/jx624/FOIL*/trip_fare_*.csv  -output AverageTip
q4:
	hadoop jar /usr/hdp/2.2.0.0-2041/hadoop-mapreduce/hadoop-streaming-2.6.0.2.2.0.0-2041.jar -D mapreduce.job.reduces=10 -D stream.num.map.output.key.fields=2 -file q4/map.py -mapper q4/map.py -file q4/reduce.py -reducer q4/reduce.py -input /user/jx624/FOIL2013/trip_data_*.csv  -output AverageTripbtwpoints
q6:
	hjs -D mapred.reduce.tasks=10 -file map.py -mapper map.py -file reduce.py -reducer reduce.py -input FOIL2010/trip_data*.csv -output q6_1_2010&
extra:
    hadoop jar /usr/hdp/2.2.0.0-2041/hadoop-mapreduce/hadoop-streaming-2.6.0.2.2.0.0-2041.jar -D mapreduce.job.reduces=10 -file extra/map.py -mapper extra/map.py -file extra/reduce.py -reducer extra/reduce.py -input /user/jx624/FOIL2013/trip_fare_*.csv  -output AverageTotal
