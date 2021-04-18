# -*- coding:utf-8 -*-
#version 7

import csv
from collections import defaultdict

with open('log_data.csv', 'r')as f:
	user = defaultdict(lambda: defaultdict(list))
	for date_time, name in csv.reader(f):
		day  = date_time.split(' ')[0]
		time = date_time.split(' ')[1]
		user[name][day].append(time)
		

Mary_total_logs = 0
for log in [len(k) for k in user['Mary'].values()]:
	log = int(log)
	Mary_total_logs += log

John_total_logs = 0
for log in [len(k) for k in user['John'].values()]:
	log = int(log)
	John_total_logs += log


Mary_start_time_of_day = min(day for day in user['Mary'].keys())
Mary_end_time_of_day   = max(day for day in user['Mary'].keys())

John_start_time_of_day = min(day for day in user['John'].keys())
John_end_time_of_day   = max(day for day in user['Mary'].keys())


# 求解組成清單印出結果
Mary = []
John = []

Mary.append(['logs of day',       user['Mary']])
Mary.append(['start time of day', Mary_start_time_of_day])
Mary.append(['end time of day',   Mary_end_time_of_day])
Mary.append(['total days',        len(user['Mary'])])
Mary.append(['total logs',        Mary_total_logs])
Mary.append(['avg log of day',    Mary_total_logs / len(user['Mary'])])

John.append(['logs of day',       user['John']])
John.append(['start time of day', John_start_time_of_day])
John.append(['end time of day',   John_end_time_of_day])
John.append(['total days',        len(user['John'])])
John.append(['total logs',        John_total_logs])
John.append(['avg log of day',    John_total_logs / len(user['John'])])

for m in Mary:
	print("Mary", m)
for j in John:
	print("John", j)