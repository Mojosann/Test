# -*- coding:utf-8 -*-
# version 1

import os
import csv
from collections import defaultdict #***


with open('log_data.csv', 'r') as csvfile:	

	#get user's start / end time of day
	Mary_days = []
	John_days = []

	#get user's logs records
	Mary_each = []
	John_each = []

	#detach user's logs records day and time
	Mday = defaultdict(list)
	Jday = defaultdict(list)

	for date_time, names in csv.reader(csvfile):
		all_logs = [names, date_time.split(' ')[0], date_time.split(' ')[1]]
		for names in all_logs:
			if 'Mary' in names:
				Mary_days.append(all_logs[1])
				Mary_each = [{date_time.split(' ')[0]: date_time.split(' ')[1]}]
				for m in Mary_each: 
					for key, value in m.items():
						Mday[key].append(value)
			elif 'John' in names:
				John_days.append(all_logs[1])
				John_each = [{date_time.split(' ')[0]: date_time.split(' ')[1]}]
				for j in John_each: 
					for key, value in j.items():
						Jday[key].append(value)
	#get total days
	#Mary_total_days = len(pd.unique(Mary_days).tolist())
	#John_total_days = len(pd.unique(John_days).tolist())


with open('log_data.csv', 'r') as csvfile: #if missing will lose total_logs: finding solution...
	
	#get total logs
	mcout = 0
	jcout = 0
	for date_time, names in csv.reader(csvfile):
		if names == 'Mary':
			Mary_logs_of_day = [date_time]
			if date_time in Mary_logs_of_day: 
				mcout += 1
		elif names == 'John':
			John_logs_of_day = [date_time]
			if date_time in John_logs_of_day: 
				jcout += 1

#combine dictionary
main = {
'Mary':{'logs_of_day'		: Mday,
		'start_time_of_day'	: Mary_days[0], 
		'end_time_of_day'	: Mary_days[-1],
		'total_days'		: {}, 
		'total_logs'		: mcout, 
		'avg_log_of_day'	: [],
		},

'John':{'logs_of_day'		: Jday,
		'start_time_of_day'	: John_days[0], 
		'end_time_of_day'	: John_days[-1],
		'total_days'		: {}, 
		'total_logs'		: jcout, 
		'avg_log_of_day'	: [],
		}
		}

for key, value in main.items():
	print('{key} : {value}'.format(key = key, value = value))
