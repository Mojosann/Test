# [Practice]
# 程式在console 將source path內的file複製過去target_path

import sys, os, shutil

source_path = 'Z:/practice/copy_test'

# target_path 'C:/Users/Academy/Desktop'
def copy_file(target_path):
	# check if folder exist
	if not os.path.isdir(target_path):
		os.mkdir(target_path)

	for item in os.listdir(source_path):

		if item in ['old', 'test']:
			continue
		if item == 'source':
			source_folder = '%s/%s' % (source_path, item)
			target_folder = '%s/%s' % (source_path, item)
			#print(source_folder)
			#print(target_folder)
			shutil.copytree(source_folder, target_folder)
		if '.' in item:
			source_file = '%s/%s' % (source_path, item)
			target_file = '%s/%s' % (target_path, item)
			#print(source_file)
			#print(target_file)
			#print('')
			shutil.copyfile(source_file, target_file)

if __name__ == '__main__':
	copy_file(sys.argv[1])
	sys.exit()