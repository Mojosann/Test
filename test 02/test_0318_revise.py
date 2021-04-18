# Way of finding missing file ver 4
#!/usr/bin/python
# -*- coding:utf-8 -*-

import os

# Default 
folder    = 'Z:\\tmp\\manting\\python\\TEST_01\\'
title     = 'untitle'
file_type = 'jpg'
first_no  = 0
last_no   = 100

# Get title, file_type, first_no, last_no
# td_test.0001.jpg
for root, dirs, files in os.walk(folder):
	title     = files[0].split('.')[0]
	first_no  = int(files[0].split('.')[1])
	last_no   = int(files[-1].split('.')[1])
	file_type = files[0].split('.')[-1]
	
for i in range(first_no, last_no+1):
	args = {}
	args['folder']    = 'Z:\\tmp\\manting\\python\\TEST_01\\'
	args['title']     = 'td_test'
	args['file_no']   = '%04d'%(i)
	args['file_type'] = 'jpg'

	image_file = '{folder}\{title}.{file_no}.{file_type}'.format(**args)

	if not os.path.exists(image_file):
		file_name = os.path.split(image_file)[1]
		print(file_name, 'missing!')