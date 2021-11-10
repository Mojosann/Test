with open('D:/Documents/work/TWR/TD class/homework/goal/log_data.csv', 'r') as read_obj:
	data_dict = {}
	for line in read_obj.readlines():
		name = line.split('\n')[0].split(',')[1]
		date = line.split('\n')[0].split(',')[0].split(' ')[0]
		time = line.split('\n')[0].split(',')[0].split(' ')[1]

		if data_dict.get(name) == None:
			data_dict[name] = {}
			data_dict[name]['log_set'] = {}
			data_dict[name]['result']  = {}

		if data_dict[name]['log_set'].get(date) == None:
			data_dict[name]['log_set'][date] = []
		data_dict[name]['log_set'][date].append(time) # mus not the same	

	for user in data_dict.keys():
		total_logs = 0
		for log in data_dict[user]['log_set'].values():
	 		total_logs += len(log)

		data_dict[user]['result']['logs_of_day']       = sorted(data_dict[user]['log_set'])
		data_dict[user]['result']['start_time_of_day'] = min(data_dict[user]['log_set'])
		data_dict[user]['result']['end_time_of_day']   = max(data_dict[user]['log_set'])
		data_dict[user]['result']['total_days']        = len(data_dict[user]['log_set'])
		data_dict[user]['result']['total_logs']        = total_logs
		data_dict[user]['result']['avg_log_of_day']    = total_logs/len(data_dict[user]['log_set'])
	
		print(user, data_dict[user]['result'])