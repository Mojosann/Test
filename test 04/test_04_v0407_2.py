# -*- coding:utf-8 -*-
#version 8

user = {}
data = []
with open('log_data.csv', 'r')as f:
	for line in f:
		data.append(line.strip('\n'))

for d in data:
	name = d.split(',')[1]
	day  = d.split(' ')[0]
	time = d.split(' ')[1].split(',')[0]
	
	if name == 'Mary':
		if user.get('Mary') == None:
			user['Mary'] = {}
		if user['Mary'].get(day) == None:
			user['Mary'][day] = []
		if time not in user['Mary'][day]:
			user['Mary'][day].append(time)

	if name == 'John':
		if user.get('John') == None:
			user['John'] = {}
		if user['John'].get(day) == None:
			user['John'][day] = []
		if time not in user['John'][day]:
			user['John'][day].append(time)

Mary_total_logs = 0
for log in [len(k) for k in user['Mary'].values()]:
	log = int(log)
	Mary_total_logs += log

John_total_logs = 0
for log in [len(k) for k in user['John'].values()]:
	log = int(log)
	John_total_logs += log

# 求解組成清單印出結果
Mary = []
John = []

Mary.append(['logs of day',       user['Mary']])
Mary.append(['start time of day', min(user['Mary'].keys())])
Mary.append(['end time of day',   max(user['Mary'].keys())])
Mary.append(['total days',        len(user['Mary'])])
Mary.append(['total logs',        Mary_total_logs])
Mary.append(['avg log of day',    Mary_total_logs / len(user['Mary'])])

John.append(['logs of day',       user['John']])
John.append(['start time of day', min(user['John'].keys())])
John.append(['end time of day',   max(user['Mary'].keys())])
John.append(['total days',        len(user['John'])])
John.append(['total logs',        John_total_logs])
John.append(['avg log of day',    John_total_logs / len(user['John'])])

for m in Mary:
	print("Mary", m)
for j in John:
	print("John", j)