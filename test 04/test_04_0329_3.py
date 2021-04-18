# -*- coding:utf-8 -*-
#version 4

import os
import csv, json
from collections import defaultdict #***

with open('log_data.csv', 'r') as csvfile:	

	#get start ~ end time of day
	Mary_logs = []
	John_logs = []

	#detach day and time
	Mary_day = defaultdict(list)
	John_day = defaultdict(list)

	for date_time, names in csv.reader(csvfile):

		# ....:... 可以分行寫註解告知我到底再取甚麼變數 才不會每次都要想以下再幹嘛
		print '[%s] %s'%(date_time, names)
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
	Mary_total_days = len(Mary_day)	#len(pd.unique(Mary_logs).tolist())
	John_total_days = len(John_day) #len(pd.unique(John_logs).tolist())


#combine dictionary
main = {
'Mary':{'logs of day'	     : Mary_day,
		'start time of day'  : Mary_logs[0], 
		'end time of day'    : Mary_logs[-1],
		'total days'		 : Mary_total_days, 
		'total logs'		 : len(Mary_logs), 
		'avg log of day'	 : len(Mary_logs) / Mary_total_days},
'John':{'logs of day'	     : John_day,
		'start time of day'  : John_logs[0], 
		'end time of day'    : John_logs[-1],
		'total days'		 : John_total_days, 
		'total logs'		 : len(John_logs), 
		'avg log of day'	 : len(John_logs) / John_total_days}
		}
		
key_list = []
key_list.append('logs of day')
key_list.append('start time of day')
key_list.append('end time of day')
key_list.append('total days')
key_list.append('total logs')
key_list.append('avg log of day')
# from pprint import pprint
# pprint(main)
# print(json.dumps(main, indent = 1))
# for key in main['Mary'].keys():
# for key in key_list:
	# print key
# 	print main['Mary'][key]