#0922

# 製作有缺少的檔案清單
image_list = []
for i in range(1, 9):
    image_file = 'twr_sq0010_sh0010_beauty_v001.%04d.exr' % i
    # 不需要5
    if i == 5:
        continue
    image_list.append(image_file)

# 印出檔案清單
for image_file in image_list:
    print(image_file)

# func example
def hello_function(name):
    print('Hello, ' + name + ', this is a function.')

# call the function
hello_function('Eric')

def plus_function(a, b):
    result = a + b
    # 只要return就會離開function
    # 沒有這一行就會變成None
    return result

# 把回傳值定義成另一個新的變數
total = plus_function(1, 2)
print(total)

# 參數傳遞模式
def create_image_name_list(start_frame, end_frame, missing_frame):
    result_list = []
    for i in range(start_frame, end_frame):
        image_file = 'twr_sq0010_sh0010_beauty_v001.%04d.exr' % i
        if i == missing_frame:
            continue
        result_list.append(image_file)
    return result_list

image_list = create_image_name_list(100, 120, 106)

for image_file in image_list:
    print(image_file)


import os 
new_path = 'C:/Users/Academy/Documents/temp'
os.mkdir(new_path)

file_path = 'C:/Users/Academy/Documents/temp/0922.txt'
os.rmdir(new_path)

file_list = os.listdir('Z:/images')
for file_name in file_list:
    print(file_name)

new_path = 'C:/Users/Academy/Documents/temp'

# 判斷資料夾不存在就建立
# if os.path.isdir(new_path) != True
# if not os.path.isdir(new_path)
if os.path.isdir(new_path) == False:
    os.mkdir(new_path)

# 檔案存在才刪除
if os.path.isfile(file_path) == True:
    os.remove(file_path)

basename = os.path.basename('Z:/images/twr_sq0010_sh0010_beauty_v001.0025.jpg.txt')
name, ext = os.path.splitext(basename)
print(name, ext)
