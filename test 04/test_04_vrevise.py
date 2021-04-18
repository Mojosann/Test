# -*- coding:utf-8 -*-
#version revise

#read file
user_dict = {}
with open('log_data.csv', 'r')as f:
	for log_list in f:
		log_list.strip('\n')

		name       = log_list.strip('\n').split(',')[1]
		date_time  = log_list.strip('\n').split(',')[0]

		date = date_time.split(' ')[0]
		time = date_time.split(' ')[1]

		if user_dict.get(name) == None:
			user_dict[name] = {} #set key and define type
		if user_dict[name].get(date) == None:
			user_dict[name][date] = [] 
		user_dict[name][date].append(time)

#print resault
for name in user_dict:
	#sum([len(log) for log in user_dict[name].values()])
	total_logs_count = 0
	for log in user_dict[name].values(): #
		total_logs_count += len(log)

	logs_of_day       = user_dict[name]
	start_time_of_day = min(user_dict[name])
	end_time_of_day   = max(user_dict[name])
	total_days        = len(user_dict[name])
	avg_log_of_day    = total_logs_count / total_days

	print(name, 'logs of day',       logs_of_day) 
	print(name, 'start time of day', start_time_of_day)
	print(name, 'end time of day',   end_time_of_day)
	print(name, 'total days',        total_days)
	print(name, 'total logs',        total_logs_count)
	print(name, 'avg log of day',    avg_log_of_day)




'''
Mary, 2021-01-05, 23:28:18
Mary, 2021-01-05, 23:28:26


data_dict = {}

data_dict['Mary'] = {}
data_dict['Mary']['2021-01-05'] = []
data_dict['Mary']['2021-01-05'] 


print user.get('Mary') == None
print 'Mary' in user.keys()
user['Mary'] = {}
user['Mary'][date] = []
# print user.get('Mary')
'''