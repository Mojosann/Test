# [Practice]

file_obj = 'C:/Users/Academy/Desktop/seq_shot_v001.csv'

# data structure
# sequence,shot
# sq0010,sh0010
# sq0010,sh0020

with open(file_obj, 'r') as file_obj:
	content = file_obj.readlines()[1:]
	data_dict = {}
	for line in content:
		line = line.replace('\n', '')
		seq = line.split(',')[0]
		shot = line.split(',')[1]

		if data_dict.get(seq) == None:
			data_dict[seq] = []

		if shot not in data_dict[seq]:
			data_dict[seq].append(shot)
	#print(data_dict)


file_obj = 'C:/Users/Academy/Desktop/seq_shot_v002.csv'

# data structure
# sequence,shot,task
# sq0010,sh0010,"anim,light,comp"
# sq0010,sh0020,"anim,light,comp"
# sq0010,sh0030,comp

with open(file_obj, 'r') as file_obj:
	content = file_obj.readlines()[1:]
	data_dict = {}
	for line in content:
		line = line.replace('\n', '')
		line = line.replace('"', '')

		seq = line.split(',')[0]
		shot = line.split(',')[1]
		task = line.split(',')[2:]

		if data_dict.get(seq) == None:
			data_dict[seq] = {}

		if data_dict[seq].get(shot) == None:
			data_dict[seq][shot] = []

		if  task not in data_dict[seq][shot]:
			data_dict[seq][shot] = task 
	#print(data_dict)



# [json module intro]
import json

# read file
with open('C:/Users/Academy/Desktop/test.json', 'r') as file_obj:
	content = file_obj.read()
	data = json.loads(content)
	#print(data)

# write file
with open('C:/Users/Academy/Desktop/test.json', 'w') as file_obj:
	# json_content = json.dumps(data_dict) # translate data to json format
	# add other args: indent, sort_keys
	# should put dict!
	json_content = json.dumps(data_dict, indent=2, sort_keys=True)

	file_obj.write(json_content)
	# try to put different content and print json_content
	#print(json_content)

# [csv module intro]
import csv

# read file
with open('D:/Documents/work/TWR/TD class/homework/goal/log_data.csv', 'r') as file_obj:
	data_list = csv.reader(file_obj)
	for item in data_list:
		print(item)

# write file
with open('D:/Documents/work/TWR/TD class/file_format/my_test.csv', 'w') as file_obj:
	# lineterminator的參數用來避免多餘的斷行
	csv_writer = csv.writer(file_obj, lineterminator='\n')
	csv_writer.writerow(['a', 'b', 'c']) # only put list
	csv_writer.writerow(['1', '2', '3'])