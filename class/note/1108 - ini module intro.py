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
config.add_section('P1')
config.set('P1', 'key1', 'value1')
config.add_section('P2')
config.set('P2', 'key2', 'value2')

with open('D:/Documents/work/TWR/TD class/file_format/my_test.ini', 'w') as write_obj:
	config.write(write_obj)