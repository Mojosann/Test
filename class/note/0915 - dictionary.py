# [Dictionary intro]

test_dict = {'a': 'A', 'b': 'B'}

# key不一定要是字串
test_dict = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D'
}

data_dict = {
    'name': 'Anna',
    'age': 6,
    'last_name': 'Pan',
    'favorite': ['strawberry', 'apple'],
    'first_name': None
}

print(data_dict.get('name'))

data_dict['first_name'] = 'Lin'
print(data_dict.get('first_name'))

for key in data_dict.keys():
    print(key)
print(data_dict.items())

# twr task_path: 'Z:/twr/sq0010/sh0010/lighting'
# sp3 task_path: 'X:/sp3/sq0010/sh0010/lighting'
# bw task_path: 'Y:/bw/sq0010/sh0010/lighting'

driver_dict = {'bw': 'Y:/', 'spm3': 'X:/', 'twr': 'Z:/'}

for proj_code in ['twr', 'spm3', 'bw', 's7']:
    if driver_dict.get(proj_code) != None:
        task_path = driver_dict[proj_code] + proj_code + '/sq0010/sh0010/lighting'
        print(task_path)
    else:
        print(proj_code + ' missing!')

sq_dict = {
    'sq0010': ['sh0010', 'sh0020'],
    'sq0020': ['sh0010', 'sh0030', 'sh0050'],
    'sq0030': ['sh0020', 'sh0025', 'sh0030']
}

for sequence, shots in sq_dict.items():
    for shot in shots:
        print(sequence, shot)
        print('Z:/twr/%s/%s/lighting' % (sequence, shot))