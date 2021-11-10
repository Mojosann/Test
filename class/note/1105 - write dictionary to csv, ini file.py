# [write dict to csv/ini file]

data_dict = {

	'A':{
		'KEY_1':'VALUE_1',
		'KEY_2':'VALUE_2',
		},
	'M':{
		'KEY_3':'VALUE_3',
		'KEY_4':'VALUE_4',
		}
	}

# csv method
# when section not the same and has different key, value should:
# name,KEY_1  ,KEY_2  ,KEY_3,KEY_4
# A   ,VALUE_1,VALUE_2,     ,
# M   ,       ,       ,VALUE_3,VALUE_4

with open('D:/Documents/work/TWR/TD class/file_format/data_dict_info.csv', 'w') as write_obj:
	
	keys_list = []
	write_obj.write('name,')
	
	for section in data_dict.keys():
		for key in data_dict[section].keys():
			keys_list.append(key)
	write_obj.write(','.join(keys_list))

	for section in data_dict.keys():
		write_obj.write('\n%s,' % (section))
		set_list = []
		for item in keys_list:
			if data_dict[section].get(item) != None:
				value = data_dict[section][item]
				set_list.append(value)
			else:
				set_list.append('')
		print(set_list)
		write_obj.write(','.join(set_list))


# ini method

# data structure
# [A]
# KEY_1=VALUE_1
# KEY_2=VALUE_2

# [M]
# KEY_3=VALUE_3
# KEY_4=VALUE_4

with open('D:/Documents/work/TWR/TD class/file_format/data_dict_info.ini', 'w') as write_obj:
	for section in data_dict.keys():
		write_obj.write('[%s]\n' % section)
		for key, value in sorted(data_dict[section].items()):
			write_obj.write('%s=%s\n' % (key, value))
		write_obj.write('\n')