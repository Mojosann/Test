# -*- coding:utf-8 -*-
#version 9

user = {}
data = []

#read file
with open('log_data.csv', 'r')as f:
	for line in f:
		data.append(line.strip('\n'))

#make user dict
for d in data:
	name = d.split(',')[1]
	day  = d.split(' ')[0]
	time = d.split(' ')[1].split(',')[0]

	if user.get(name) == None:
		user[name] = {}
	if user[name].get(day) == None:
		user[name][day] = [] #define type
	user[name][day].append(time)

#count total logs
Mary_total_logs = 0
for log in [len(k) for k in user['Mary'].values()]:
	log = int(log)
	Mary_total_logs += log

John_total_logs = 0
for log in [len(k) for k in user['John'].values()]:
	log = int(log)
	John_total_logs += log

#make resault list
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

#print resault
for m in Mary:
	print("Mary", m)
for j in John:
	print("John", j)
