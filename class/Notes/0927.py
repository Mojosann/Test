#0927

import os
# 建立多層資料夾因為太深失敗 因為從上一層都沒有

temp_path = 'C:/Users/Academy/Documents'
folder_list = ['/temp', '/first', '/second', '/third']

for folder in folder_list:
    # 檢查第一層資料夾路徑是否存在
    if os.path.isdir(temp_path) == True:
        # 添加下一層資料夾名稱字串
        temp_path += folder
        #　創建該資料夾
        os.mkdir(temp_path)
        print(temp_path)

# 將路徑分割成清單後再接續串起來建立資料夾路徑
folder_list = ['D:', 'temp', 'twr', 'sq0010', 'sh0010', 'lighting']
new_path = ''
for folder in folder_list:
    new_path = new_path + '/' + folder
    print(new_path[1:])

# 

def make_dir(input_path):
    folder_path = ''
    folder_list = input_path.split('/')

    for folder in folder_list:
        folder_path = folder_path + '/' + folder
        if os.path.isdir(folder_path[1:]) != True:
            os.mkdir(folder_path[1:])
    print(folder_path[1:])

# 請使用func塞入任何很長的資料夾路徑 未存在ㄉ
make_dir('D:/temp/twr/sq0010/sh0010/lighting')

# 東西全部印出來再丟進func
# find exr file
def get_image_name_list(input_path):
    result_list = []
    path_data = os.listdir(input_path)
    for image_file in  path_data:
        if 'exr' in image_file:
            result_list.append(image_file)
    return result_list

image_list = get_image_name_list('Z:/images')
for exr in image_list:
    print(exr)

# find missing exr file
def find_missing_file(input_list):
    num_list = []
    for item in input_list:
        num_list.append(int(item.split('.')[-2][-3]))
        for num in range(num_list[0], num_list[1]):
            if num not in num_list:
                print(num, 'missing')
                
#使用func把image_list丟進去