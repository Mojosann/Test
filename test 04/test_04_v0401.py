# -*- coding:utf-8 -*-
#version 6

import csv, collections
 
day_list = collections.defaultdict(list)
Mary_day = collections.defaultdict(list)
John_day = collections.defaultdict(list)

with open('log_data.csv', 'r') as csvfile:	

	# 將file轉換成dict
	for date_time, name in csv.reader(csvfile):
		data = {name:{date_time.split(' ')[0]:date_time.split(' ')[1]}}

		# 設user為key的字典(去掉重複鍵)
		for key, value in data.items():
			day_list[key].append(value) 

	# 將user內的log分離日期與時間
	for m in day_list['Mary']: # {'2021-01-05': ['23:28:14'...],...
		for day, time in sorted(m.items()):
			Mary_day[day].append(time)
			
	for j in day_list['John']: 
		for day, time in j.items():
			John_day[day].append(time) 

# 將user與日期時間資料裝進字典
user = {}
user.update({'Mary_logs': sorted(Mary_day.items()), 'John_logs': sorted(John_day.items())})


# 求解組成清單印出結果
Mary = []
John = []

Mary.append(['logs of day',       user['Mary_logs']])
Mary.append(['start time of day', user['Mary_logs'][0][0]]) # 取第一鍵值對的鍵名
Mary.append(['end time of day',   user['Mary_logs'][-1][0]])
Mary.append(['total days',        len(user['Mary_logs'])])
Mary.append(['total logs',        len(day_list['Mary'])])
Mary.append(['avg log of day',    len(day_list['Mary']) / len(user['Mary_logs'])])

John.append(['logs of day',       user['John_logs']])
John.append(['start time of day', user['John_logs'][0][0]])
John.append(['end time of day',   user['John_logs'][-1][0]])
John.append(['total days',        len(user['John_logs'])])
John.append(['total logs',        len(day_list['John'])])
John.append(['avg log of day',    len(day_list['John']) / len(user['John_logs'])])

for m in Mary:
	print("Mary", m)
for j in John:
	print("John", j)

'''
# 將求解組合成字典
Mary = {'logs of day'	     : user['Mary_logs'],
		'start time of day'  : [day for day in Mary_day_list][0], 
		'end time of day'    : [day for day in Mary_day_list][-1],
		'total days'         : len(user['Mary_logs']), 
		'total logs'         : len(day_list['Mary']), 
		'avg log of day'	 : len(day_list['Mary']) / len(user['Mary_logs'])
		}

John = {'logs of day'	     : user['John_logs'],
		'start time of day'  : [day for day in John_day_list][0], 
		'end time of day'    : [day for day in John_day_list][-1],
		'total days'		 : len(user['John_logs']), 
		'total logs'		 : len(day_list['John']), 
		'avg log of day'	 : len(day_list['John']) / len(user['John_logs'])
		}
'''