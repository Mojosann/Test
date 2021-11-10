# [change file path]
# maya / nuke friendly!
# houdini file usually save as binary

old_path = 'T:/academy/asset/char'
new_path = 'C:/Users/Academy/Documents/temp/asset/char'

# read file
read_obj = open('C:/Users/Academy/Documents/temp/old_file.ma', 'r')
content = read_obj.readlines()
read_obj.close()

# write file
write_obj = open('C:/Users/Academy/Documents/temp/new_file.ma', 'w')

for line in content:
	if old_path in line:
		print(line)
		new_data = line.replace(old_path, new_path)
		write_obj.write(new_data)
	else:
		write_obj.write(line)

write_obj.close()


# file IO with 'with'
old_path = 'T:/academy/asset/char'
new_path = 'C:/Users/Academy/Documents/temp/asset/char'

with open('C:/Users/Academy/Documents/temp/old_file.ma', 'r') as read_obj:
	content = read_obj.readlines()	
	with open('C:/Users/Academy/Documents/temp/new_file.ma', 'w') as write_obj:
		
		for line in content:
			if old_path in line:
				new_data = line.replace(old_path, new_path)
				write_obj.write(new_data)
			else:
				write_obj.write(line)


# [file format]
# ini(.ini, .cfg, .cof, .config..) key=value pair
	# wikipedia: usually save some data to a file to be default setting on UI, ex: username
	# 大前輩: 仍有其他可以儲存類似資訊的檔案格式
# JSON(.json): python dictionary
# XML(.xml)
# CSV(.csv)
# excel(.xls, .xlsx...): change ext as .xip and unxip
# SQL(.db)


# [ini file intro]
# read .ini file
with open('C:/Users/Academy/Desktop/coding/file_format/Engine.ini', 'r') as read_obj:
	content = read_obj.readlines()
	for item in content:
		if 'MulticastTimeToLive' in item:
			resault = item.split('=')[1]
			print(resault)


# translate ini file info to a dict
with open('C:/Users/Academy/Desktop/coding/file_format/Engine.ini', 'r') as read_obj:
	
	content = read_obj.readlines()
	section = None
	data_dict = {}

	for line in content:
		line = line.replace('\r', '') # rstrip() r = right(alse has lstrip())
		line = line.replace('\n', '')

		if line == '':
			continue

		if '[' and ']' in line:
			section = line
			section = section.replace('[', '')
			section = section.replace(']', '')

			data_dict[section] = {}

		if '=' in line:
			buffer_list = line.split('=')
			key = buffer_list[0]
			value = line.replace('%s=' % (key), '')
			# way 2
			value = line[len(key)+1]
			# way 3
			value = '='.join(buffer_list[1:])

			data_dict[section][key] = value

	print(data_dict)