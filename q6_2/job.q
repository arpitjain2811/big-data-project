#!/bin/sh
cd ~
/usr/bin/hadoop jar /usr/hdp/2.2.0.0-2041/hadoop-mapreduce/hadoop-streaming-2.6.0.2.2.0.0-2041.jar -D mapred.reduce.tasks=40 -file bigdata_q6_2/map.py -mapper bigdata_q6_2/map.py -file bigdata_q6_2/reduce.py -reducer bigdata_q6_2/reduce.py -input FOIL201*/trip_data*.csv -output q6_2

/usr/bin/hadoop jar /usr/hdp/2.2.0.0-2041/hadoop-mapreduce/hadoop-streaming-2.6.0.2.2.0.0-2041.jar -D mapred.reduce.tasks=2 -file bigdata_q6_1/word-1.py -mapper bigdata_q6_1/word-1.py -file bigdata_q6_1/count.py -reducer bigdata_q6_1/count.py -input q6_2/part-* -output triphour_count_by_day

/usr/bin/hadoop fs -getmerge triphour_count_by_day triphour_count_by_day

