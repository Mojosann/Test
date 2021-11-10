# [ini module intro]

# py2: ConfigParser
import configparser # py3

# read file
config = configparser.ConfigParser()
config.read('D:/Documents/work/TWR/TD class/file_format/my_test.ini')

# config.get(section, key)
print(config.get('P1', 'key1'))
print(config)


# write file
config = configparser.ConfigParser()
config.add_section('P1')
config.set('P1', 'key1', 'value1')
config.add_section('P2')
config.set('P2', 'key2', 'value2')

with open('D:/Documents/work/TWR/TD class/file_format/my_test.ini', 'w') as write_obj:
	config.write(write_obj)

'''
data_dict = {

	'Apocalypse_Now':{
		'width':1280,
		'height':920,
		'fps':25,
		'maya_version':2021,
		'renderer':'v-ray'
		},
	'Dune':{
		'width':1080,
		'height':720,
		'fps':50,
		'maya_version':2020,
		'renderer':'mantra'
		}
	}
config = configparser.ConfigParser()

for section in data_dict.keys():
	config.add_section(section)
	for key, value in data_dict[section].items():
		config.set(section, key, str(value))

with open('D:/Documents/work/TWR/TD class/file_format/my_test.ini', 'w') as write_obj:
	config.write(write_obj)
'''