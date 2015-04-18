#!/usr/bin/env python
import sys,os
from datetime import datetime
current_driver = None
current_day=None
time_list=[0,1]
for line in sys.stdin:
	line=line.strip()
	driver,day,time=line.split(',')
	if current_driver==driver and current_day==day:
		time_list[1]=time
	else:
		if current_day and current_driver:
			try:
				minhour=datetime.strptime(time_list[0],'%H:%M:%S')
				maxhour=datetime.strptime(time_list[1],'%H:%M:%S')
				hours=maxhour-minhour
				hours=hours.total_seconds()
				hours=hours/3600
				print "%s,%s,%.2f"%(driver,day,hours)
			else:
				pass
		current_driver=driver
		current_day=day
		time_list[0]=time
try:
	minhour=datetime.strptime(time_list[0],'%H:%M:%S')
	maxhour=datetime.strptime(time_list[1],'%H:%M:%S')
	hours=maxhour-minhour
	hours=hours.total_seconds()
	hours=hours/3600
	print "%s,%s,%.2f"%(driver,day,hours)
else:
	pass
