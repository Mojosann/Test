# -*- coding:utf-8 -*-
#version 10

user = {} ; data = []
#read file
with open('log_data.csv', 'r')as f:
	for line in f:
		data.append(line.strip('\n'))

#make user dict
for d in data:
	name = d.split(',')[1]
	day  = d.split(' ')[0]
	time = d.split(' ')[1].split(',')[0]

	if name not in user:
		user[name] = {} #set key and define type
	if day not in user[name]:
		user[name][day] = [] 
	user[name][day].append(time)

#print resault
for name, logs in user.items():
	total_logs = 0
	for log in [len(k) for k in user[name].values()]:
		log = int(log)
		total_logs += log

	print(name, 'logs of day', logs) #sorted(logs.items())
	print(name, 'start time of day', min(user[name].keys()))
	print(name, 'start time of day', max(user[name].keys()))
	print(name, 'total days', len(user[name]))
	print(name, 'total logs', total_logs)
	print(name, 'avg log of day', total_logs / len(user[name]))