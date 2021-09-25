# sh0010-sh0150
task_path = 'Z:/twr/sq0010/sh0010/lighting/twr_sq0010_sh0010_lighting_v001.ma'

# way 1
for num in range(10, 151, 10):
	task_path = 'Z:/twr/sq0010/sh%04d/lighting/twr_sq0010_sh%04d_lighting_v001.ma' % (num, num)
	print(task_path)

# way 2
for num in range(10, 151, 10):
	shot_num  = '00' + str(num)
	shot_name = 'sh' + shot_num[-4:]
	task_path = 'Z:/twr/sq0010/' + shot_name + '/lighting/twr_sq0010_' + shot_name + '_lighting_v001.ma'
	print(task_path)
