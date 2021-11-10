# [if/else/range intro]

# range function
print(range(10))


test_list = [1, 2, 3, 4, 5, '6', '7', '8', '9', '10']

# index compare
for i in range(len(test_list)):
	print(test_list[i])

for i in range(0, 10, 2):
	print(i)

# make num list
for i in range(10, 151, 10):
	shot_num = '00' + str(i)
	shot_name = 'sh' + shot_num[-4:]
	print(shot_name)

# continue example
for item in test_list:
	if item <= 5:
		print('ok' + str(item))
		continue # nothing happend

# 1, 3, 5, 7, 9
for i in range(1, len(test_list)+1, 2):
	print(i)

# 2, 4, 6, 8, 10
for i in range(2, len(test_list)+1, 2):
	print(i)

# 3, 6, 9
for i in range(3, len(test_list)+1, 3):
	print(i)

# 10, 9, 8, 7...1
for i in range(int(test_list[-1]), -1, -1):
	print(i)

# break
i = 0
while i < len(test_list):
	print(test_list[i])
	i += 1

task_path = 'Z:/twr/sq0010/sh0010/lighting/twr_sq0010_sh0010_lighting_v001.ma'

# method(1)
for num in range(10, 151, 10):
	print('Z:/twr/sq0010/sh%04d/lighting/twr_sq0010_sh%04d_lighting_v001.ma' % (num, num))

# method(2)
for num in range(10, 151, 10):
	shot_num = '00' + str(num)
	shot_name = 'sh' + shot_num[-4:]
	print('Z:/twr/sq0010/' + shot_name + '/lighting/twr_sq0010_' + shot_name + '_lighting_v001.ma')