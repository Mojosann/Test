# reverse file_no
import os
folder = 'F:\\TEST_03\\twr_sq0010_sh0010\\'

# Default 
folder    = 'E:\\TEST_03\\twr_sq0010_sh0020\\'
title     = 'twr_sq0010_sh0020'
file_type = 'jpg'
first_no  = 0
last_no   = 100

for root, dirt, files in os.walk(folder):
	first_no  = int(files[0].split('.')[1])
	last_no   = int(files[-1].split('.')[1])
	#print(type(files)) #list
	#get new / old files continuous number
	old_sorted = list(range(first_no, last_no+1))
	new_sorted = old_sorted[::-1]	

	#put file_path into list
	new_file_list   = []
	final_file_list = []
	n = 1
	for i in new_sorted:
		args = {}
		args['folder']    = 'F:\\TEST_03\\twr_sq0010_sh0010\\'
		args['title']     = 'twr_sq0010_sh0010'
		args['file_no']   = '%04d'%(n)
		n +=1
		args['new_number'] = '%04d'%(i)
		args['file_type'] = 'jpg'

		data  = '{folder}{title}.{file_no}.{new_number}.{file_type}'.format(**args) #str
		data2 = '{folder}{title}.{new_number}.{file_type}'.format(**args)
		new_file_list.append(data)
		final_file_list.append(data2)
	#print(final_file_list) #list

#first stage rename
a = 0
for b in new_file_list:
	old_file = folder + files[a]
	new_file = b
	a += 1
	#print(old_file) #str
	os.rename(old_file, new_file)
	#print(old_file,'改名為：',new_file_list) > bad


#second stage rename
for root, dirt, files_2 in os.walk(folder):
	c = 0
	for d in final_file_list:
		new_file = folder + files_2[c]
		final_file = d
		c += 1
		print(new_file) #str
		os.rename(new_file, final_file)
