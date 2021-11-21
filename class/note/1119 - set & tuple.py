# [set & tuple]

# [set]
# set只用來除去list內重複項

a_list = [1, 2, 3, 1, 2, 4, 5]
b_list = [1, 2, 4, 2, 1, 1, 6]

num_set = {'a':[], 'b':[]}
for item in a_list:
	if item not in num_set['a']:
		num_set['a'].append(item)
for item in b_list:
	if item not in num_set['b']:
		num_set['b'].append(item)

# 1. a_list有哪些數字?
# 一定要轉成set才可以使用
# set(a_list)
# 要變成list再記得轉型回來list(set(b_list))

for item in num_set['a']:
	print(item)

# 2. b_list有哪些數字?
# set(b_list)

for item in num_set['b']:
	print(item)

# 3. a_list, b_list共有哪些數字?
# set(a_list)|set(b_list)

total_list = []
for item in a_list:
	if item not in total_list:
		total_list.append(item)
for item in b_list:
	if item not in total_list:
		total_list.append(item)
print(total_list)

# 4. a_list, b_list有哪些相同的數字?
# set(a_list)&set(b_list)

same_list = []
for a in a_list:
	for b in b_list:
		if a == b:
			if a not in same_list:
				same_list.append(a)
print(same_list)

# 5. a_list有哪些b_list沒有的數字?
# set(a_list)-set(b_list)

for item in a_list:
	if item not in b_list:
		print(item)

# 6. b_list有哪些a_list沒有的數字?
# set(b_list)-set(a_list)

for item in b_list:
	if item not in a_list:
		print(item)

# 7. b_list/a_list都沒有的數字?
# set(b_list)^set(a_list)

#宣告一個空的set
test_set = set()

#建立一個有值的set
test_set = {1, 2, 3, 4, 5}

# 將10加到set裡面
test_set.add(10)

# 將10從test_set移除
test_set.remove(10)

# set裡面的值是唯一的
# 無法直接變更或取得set裡面的值(但轉list就可以)
# 可以新增或移除set裡面的值


# [tuple]
# 宣告一個空的tuple
test_tuple = tuple()

# 建立一個有值的tuple
test_tuple = (1, 2, 3, 4, 5)

# 取的第0個值
test_tuple[0]

# 允許重複值
# 無法直接變更、"新增、移除(但轉list就可以)"tuple內的值
# 可以直接取得tuple內的值

# tuple可以做為dict的key可以暫時存取資料 但無法直接輸出json
# 原本要一層層去判斷才能取當前的key value pair
test_dict = {}
# test_dict = {'first':{'second':[1, 2, 2]}}
# 直接改用tuple
if test_dict.get(('first', 'second')) != None:
	#print(test_dictp[['first', 'second']]) # list as key: error
	test_dict[('first', 'second')]
	print(test_dict['first']['second']) # tupel as key: ok