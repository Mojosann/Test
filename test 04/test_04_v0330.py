# -*- coding:utf-8 -*-
#version 5

import csv, json, collections
 
day_list	  = collections.defaultdict(list)
Mary_day_list = collections.defaultdict(list)
John_day_list = collections.defaultdict(list)

with open('log_data.csv', 'r') as csvfile:	

	# 將file轉換成dict
	for date_time, name in csv.reader(csvfile):
		data = {name:{date_time.split(' ')[0]:date_time.split(' ')[1]}}
		
		# 設user為key的字典
		for key, value in data.items():
			day_list[key].append(value) 

	# 將user內的log分離日期與時間
	for m in day_list['Mary']: # {'2021-01-05': ['23:28:14'...],...
		for day, time in m.items(): 
			Mary_day_list[day].append(time) 

	for j in day_list['John']: # {'2021-01-06': ['15:49:01', '15:49:01']}...
		for day, time in j.items():
			John_day_list[day].append(time) 

# 將user與日期時間資料裝進字典
user = {}
user.update({'Mary_logs': Mary_day_list, 'John_logs': John_day_list})

# 取出user的最早最晚log_day
Mary_start_day = [day for day in Mary_day_list][0]
for d in [day for day in Mary_day_list]:
	if Mary_start_day > d: 
		Mary_start_day = d
	else:
		Mary_end_day = d

John_start_day = [day for day in John_day_list][0]
for d in [day for day in John_day_list]:
	if John_start_day > d: 
		John_start_day = d
	else:
		John_end_day = d

# 求解組成清單印出結果
Mary = []
John = []

Mary.append(['logs of day',       user['Mary_logs']])
Mary.append(['start time of day', Mary_start_day])
Mary.append(['end time of day',   Mary_end_day])
Mary.append(['total days',        len(user['Mary_logs'])])
Mary.append(['total logs',        len(day_list['Mary'])])
Mary.append(['avg log of day',    len(day_list['Mary']) / len(user['Mary_logs'])])

John.append(['logs of day',       user['John_logs']])
John.append(['start time of day', John_start_day])
John.append(['end time of day',   John_end_day])
John.append(['total days',        len(user['John_logs'])])
John.append(['total logs',        len(day_list['John'])])
John.append(['avg log of day',    len(day_list['John']) / len(user['John_logs'])])

print("Mary", Mary)
print("John", John)

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