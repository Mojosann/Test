import json
import random

data_list = []
test_list = ['animation', 'fx']
enable_list = ['True', 'False']

for i in range(1, 51):

	data_dict = {}
	data_dict['name'] = 'mini_%02d' % i
	data_dict['type'] = test_list[random.randint(0, 1)]
	data_dict['enable'] = enable_list[random.randint(0, 1)]

	data_list.append(data_dict)

with open('D:/Documents/work/TWR/TD class/file_format/random.json', 'w') as file_obj:
	json_content = json.dumps(data_list, indent=2, sort_keys=True)
	file_obj.write(json_content)