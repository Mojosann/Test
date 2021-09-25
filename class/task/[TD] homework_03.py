# animation / lighting / fx / comp
shot_dict = {
	'sh0010': 3,
	'sh0030': 2,
	'sh0020': 1,
	'sh0035': 1
}

task_dict = {}
task_dict[3] = ['animation', 'lighting', 'fx', 'comp']
task_dict[2] = ['animation', 'lighting', 'comp']
task_dict[1] = ['comp']

for shot_name, level in sorted(shot_dict.items()):
	for num in task_dict.keys():
		if num == shot_dict[shot_name]:
			for task in task_dict[num]:
				print('Z:/twr/sq0010/%s/%s' % (shot_name, task))
