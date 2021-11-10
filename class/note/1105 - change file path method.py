# [change file path method]
# maya / nuke friendly!
# houdini file usually save as binary

old_path = 'T:/academy/asset/char'
new_path = 'C:/User/Academy/Documents/temp/asset/char'

# TD method(1)
read_obj = open('C:/User/Academy/Documents/temp/old_file.ma', 'r')
write_obj = open('C:/User/Academy/Documents/temp/new_file.ma', 'w')

for line in read_obj:
	if old_path in line:
		line.replace(old_path, new_path)
	write_obj.write(line)

read_obj.close()
write_obj.close()

# TD method(2)
with open('C:/User/Academy/Documents/temp/old_file.ma', 'r') as read_obj:
	with open('C:/User/Academy/Documents/temp/new_file.ma', 'w') as write_obj:
		for line in read_obj:
			if old_path in line:
				line.replace(old_path, new_path)
			write_obj.write(line)