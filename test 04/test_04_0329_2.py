# -*- coding:utf-8 -*-
#version 3

import os
import pandas as pd, csv, json
from collections import defaultdict #***

with open('log_data.csv', 'r') as csvfile:	

	#get start ~ end time of day
	Mary_logs = []
	John_logs = []

	#detach day and time
	Mary_day = defaultdict(list)
	John_day = defaultdict(list)

	for date_time, names in csv.reader(csvfile):
		all_logs = [names, date_time.split(' ')[0], date_time.split(' ')[1]]
		if 'Mary' in names:
			Mary_logs.append(all_logs[1])	
			Mary_each = [{all_logs[1]:all_logs[2]}]	#get logs records
			for m in Mary_each: 
				for key, value in m.items():
					Mary_day[key].append(value)
		elif 'John' in names:
			John_logs.append(all_logs[1])
			John_each = [{all_logs[1]:all_logs[2]}]
			for j in John_each: 
				for key, value in j.items():
					John_day[key].append(value)
	
	#remove repeat values and count total days 
	Mary_total_days = len(pd.unique(Mary_logs).tolist())
	John_total_days = len(pd.unique(John_logs).tolist())

#combine dictionary
main = {
'Mary':{'1.logs of day'		  : Mary_day,
		'2.start time of day' : Mary_logs[0], 
		'3.end time of day'	  : Mary_logs[-1],
		'4.total days'		  : Mary_total_days, 
		'5.total logs'		  : len(Mary_logs), 
		'6.avg log of day'	  : len(Mary_logs) / Mary_total_days,
		},

'John':{'1.logs of day'		  : John_day,
		'2.start time of day' : John_logs[0], 
		'3.end time of day'	  : John_logs[-1],
		'4.total days'		  : John_total_days, 
		'5.total logs'		  : len(John_logs), 
		'6.avg log of day'	  : len(John_logs) / John_total_days,
		}
		}
	
print(json.dumps(main, indent = 1))