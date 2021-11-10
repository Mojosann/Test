# [string function intro]

proj = task_path.split('/')[1]
sequ = task_path.split('/')[2]
shot = task_path.split('/')[3]
task = task_path.split('/')[4]

test_list = [1, 2, 3, 3, 3]

test_list.append(3)
test_list.insert(2, '5')


if 2 in test_list:
	test_list.remove(2)

for i in test_list:
	if i == 3:
		test_list.remove(i)


test_list.extend([proj, sequ, shot, task])
print(test_list)

test_item = 1
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if test_item in test_list:
	print('we got', test_item)

message = 'Hello, this is "TWR" TD school.'
data_list = message.split(' ')
data_list.remove('school.')
data_list.append('academy.')
new_message = ' ',join(data_list)

print(new_message)

if 'school' in message:
	print(message.replace('school', 'academy'))

# [Practice]
task_path = 'Z:/twr/sq0010/sh0010/lighting'

houdini_file = '_'.join(task_path.split('/')[1:])
print(houdini_file)

for i in test_list:
	if i % 2 == 0:
		print(i)