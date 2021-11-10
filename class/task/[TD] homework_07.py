with open('D:/Documents/work/TWR/TD class/homework/goal/log_data.csv', 'r') as read_obj:
	data_dict = {}
	for line in read_obj.readlines():
		name = line.split('\n')[0].split(',')[1]
		date = line.split('\n')[0].split(',')[0].split(' ')[0]
		time = line.split('\n')[0].split(',')[0].split(' ')[1]

		if data_dict.get(name) == None:
			data_dict[name] = {}

		if data_dict[name].get(date) == None:
			data_dict[name][date] = []
		data_dict[name][date].append(time) # mus not the same

info_dict = {}
for user in data_dict.keys():
	total_logs = 0
	for log in data_dict[user].values():
		total_logs += len(log)

	info_dict[user] = {}
	info_dict[user]['logs_of_day']       = sorted(data_dict[user])
	info_dict[user]['start_time_of_day'] = min(data_dict[user])
	info_dict[user]['end_time_of_day']   = max(data_dict[user])
	info_dict[user]['total_days']        = len(data_dict[user])
	info_dict[user]['total_logs']        = total_logs
	info_dict[user]['avg_log_of_day']    = total_logs/len(data_dict[user])

print(info_dict)