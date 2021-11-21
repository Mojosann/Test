# [Copy file function]
# function can back up file automatically
# when target file exists, will back up file to ./old/'file_name'
# when backup file exists, will rename 'file_name(1)'
# ex: aaa.txt, aaa(1).txt, aaa(2).txt...

import os, sys, shutil

def td_copy_file(source_file, target_file):

	if os.path.isfile(source_file) != True:
		print('file not exist!')
	
	if os.path.isfile(target_file) == True:
		old_path = os.path.dirname(target_file) + '/old'
		file_name = os.path.basename(target_file)
		backup_file = '%s/%s' % (old_path, file_name)

		if os.path.isdir(old_path) != True:
			os.mkdir(old_path)
			shutil.copyfile(source_file, backup_file)
			return 'back up %s complete!' % backup_file

		if os.path.isdir(old_path) == True:
			name, ext = os.path.splitext(file_name)
			backup_len = len(os.listdir(old_path))
			backup_file_index = '%s/%s(%s)%s' % (old_path, name, backup_len, ext)
			
			if os.path.isfile(backup_file) == True:
				if backup_len == 1:
					shutil.copyfile(source_file, backup_file_index)
					return 'back up %s complete!' % backup_file_index
				if backup_len > 1:
					shutil.copyfile(source_file, backup_file_index)
					return 'back up %s complete!' % backup_file_index

	else:
		shutil.copyfile(source_file, target_file)
		return 'back up complete!'

source = 'D:/Documents/work/TWR/TD class/homework/hw008_thumbnail/Bubbles.png'
target = 'D:/temp/file/Bubbles.png'
print(td_copy_file(source, target))