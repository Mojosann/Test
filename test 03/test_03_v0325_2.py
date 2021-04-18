# reverse file_no
#!/usr/bin/python
# -*- coding:utf-8 -*-

import os

# Default 
folder    = 'D:\\document\\script\TEST_03\\twr_sq0010_sh0010\\'
title     = 'twr_sq0010_sh0010'
file_type = 'jpg'
first_no  = 0
last_no   = 100

for root, dirt, files in os.walk(folder):
	first_no  = int(files[0].split('.')[1])
	last_no   = int(files[-1].split('.')[1])
	#type(files) 'list'
	#get new_files continuous number
	new_sorted = list(range(first_no, last_no+1))[::-1]
	
	#put file_path into list
	new_file_list   = []
	final_file_list = []
	n = 1
	for i in new_sorted:
		args = {}
		args['folder']     = 'D:\\document\\script\TEST_03\\twr_sq0010_sh0010\\'
		args['title']      = 'twr_sq0010_sh0010'
		args['file_no']    = '%04d'%(n)
		n +=1
		args['new_number'] = '%04d'%(i)
		args['file_type']  = 'jpg'

		data  = '{folder}{title}.{file_no}.{new_number}.{file_type}'.format(**args) #str
		data2 = '{folder}{title}.{new_number}.{file_type}'.format(**args)
		new_file_list.append(data)
		final_file_list.append(data2)
	
#first stage rename
c = 0
for new_file in new_file_list:
	old_file = folder + files[c] #str
	c += 1
	os.rename(old_file, new_file)

#second stage rename
c = 0
for final_file in final_file_list:
	new_file = new_file_list[c] #str
	os.rename(new_file, final_file)
	c += 1