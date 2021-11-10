# [Dictionary intro]

# request task
sq_dict = {
    'sq0010' : ['sh0010', 'sh0020'],
    'sq0020' : ['sh0010', 'sh0030', 'sh0050'],
    'sq0030' : ['sh0020', 'sh0025', 'sh0030']
}

# 印出鏡頭路徑
for sequence, shots in sorted(sq_dict.items()):
    for shot in shots:
        #print(sequence, shot)
        print('Z:/twr/%s/%s/lighting' % (sequence, shot))

# 有順序清單
for sq_name in ['sq0010', 'sq0020', 'sq0030', 'sq0040']:
    if sq_dict.get(sq_name) != None:
        for sh_name in sq_dict[sq_name]:
            print(sq_name + ' - ' + sh_name)
    else:
        print(sq_name, ' missing!')

# 字典內沒有順序
for sq_name in sq_dict:
    if sq_dict.get(sq_name) != None:
        for sh_name in sq_dict[sq_name]:
            print(sq_name + ' - ' + sh_name)
    else:
        print(sq_name + ' missing!')

# 九九乘法表
for i in range(2, 10):
    for s in range(1, 10):
        print( str(i) + ' x ' + str(s) + ' = ' + str(i*s))

number_list = ['3', '1', '5', '4', '2', '10', '100']
print(number_list)

# sorted的方法將清單排序後存到新變數 原清單排序不變
new_list = sorted(number_list)
print(new_list)

# result = None 因為它只是做事沒有要回傳值
number_list.sort()
print(number_list)


sq_dict = {
    'sq0010' : ['sh0010', 'sh0020'],
    'sq0020' : ['sh0010', 'sh0030', 'sh0050'],
    'sq0030' : ['sh0020', 'sh0025', 'sh0030']
}    

# sorted
for sq_name in sorted(sq_dict.keys()):
    if sq_dict.get(sq_name) != None:
        for sh_name in sq_dict[sq_name]:
            print(sq_name + ' - ' + sh_name)
    else:
        print(sq_name, + ' missing!')

# .sort()
sort_sqlist = sq_dict.keys()
sorted(sort_sqlist)


for sq_name in sort_sqlist:
    if sq_dict.get(sq_name) != None:
        for sh_name in sq_dict[sq_name]:
            print(sq_name + ' - ' + sh_name)
    else:
        print(sq_name + ' missing!')

# replace items in list
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_list[0] = 'A'
test_list[-4:] = [',', 'D', 'J', 'S']
test_list[-1] = 'z'

print(test_list)

data_dict = {
    'name' : 'Anna',
    'age' : 6,
    'last name' : 'Pan',
    'favourite' : ['strawberry', 'apple'],
    'first_name' : None
}

# 更改字典的值
data_dict['name'] = 'Elsa'

# 因為功能是取值不是給值不能執行
#data_dict.get('name') = 'Elsa'

# 新增key / value
data_dict['first_name'] = 'Elsa'

print(data_dict)

# ani, lgt, fx, comp
shot_dict = {
     'sh0010' : 3,
     'sh0030' : 2,
     'sh0020' : 1,
     'sh0035' : 1
     }

task_cont= {}
task_cont[3] = ['animation', 'lighting', 'fx', 'comp']
task_cont[2] = ['animation', 'lighting', 'comp']
task_cont[1] = ['comp']

for shot_name, cont in sorted(shot_dict.items()):
    for item in task_cont.keys():
        if shot_dict[shot_name] == item:
            # print('%s: %s' % (shot_name, task_cont[item]))
            for i in task_cont[item]:
                print(shot_name, i)