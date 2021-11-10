# [Analyze file]

# read, replace and write file
read_obj = open('C:/Users/Academy/Desktop/coding/test.txt', 'r')
content = read_obj.read()
read_obj.close()

content = content.replace('Happy', 'byebye')

write_obj = open('C:/Users/Academy/Desktop/coding/test_not_exists.txt', 'w')
write_obj.write(content)
write_obj.close()

# read multiple lines(1)
read_obj = open('Z:/practce/lots_of_data.txt', 'r')
content = read_obj.read()

for line in content.split('\n'):
	print(line)

read_obj.close()

# read multiple lines(2)
read_obj = open('Z:/practce/lots_of_data.txt', 'r')
content_line = read_obj.readlines() # read data by readlines

for line in content_line:
	print(line)

read_obj.close()

# read multiple lines(3)
# 將檔案一行行讀取比較不占記憶體空間但速度稍慢
read_obj = open('Z:/practce/lots_of_data.txt', 'r')
line = read_obj.readline() # read data by readline

while line:
	print(line)
	line = read_obj.readline()

read_obj.close()

# 簡潔寫法
read_obj = open('Z:/practce/lots_of_data.txt', 'r')

for line in read_obj:
	print(line)

read_obj.close()

# [Practice]
read_obj = open('Z:/practce/lots_of_data.txt', 'r')

user_dict = {
	'John':0, 
	'Mary':0, 
	'Peter':0, 
	'Kevin':0
}

for line in read_obj:
	if 'John' in line:
		user_dict['John'] += 1
	if 'Mary' in line:
		user_dict['Mary'] += 1
	if 'Peter' in line:
		user_dict['Peter'] += 1
	if 'Kevin' in line:
		user_dict['Kevin'] += 1

print(user_dict)
read_obj.close()

# TD method
read_obj = open('Z:/practce/lots_of_data.txt', 'r')
user_dict = {}

for line in read_obj:
	# Get username from line at 1.
	buffer_list = line.split('\t')
	username = buffer_list[1]

	# set count_dict for username
	if user_dict.get(username) == None:
		user_dict[username] = 0
	user_dict[username] += 1

print(user_dict)

for name in user_dict.keys():
	print('%10s:%s' % (name, user_dict[name]))

read_obj.close()