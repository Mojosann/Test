# [Find missind file module]

import os

def get_image_name_list(input_path, ext):
    
    result_list = []

    path_data = os.listdir(input_path)
    for image_file in path_data:
        if ext in image_file:
            result_list.append(image_file)

    return result_list

def find_missing_file(input_list):

    num_list = []
    missing_list = []

    for item in input_list:
        num_list.append(int(item.split('.')[1]))

    num_list.sort()
    
    for num in range(num_list[0], num_list[-1]+1):
        if num not in num_list:
            missing_list.append(num)
            #print(num,  'missing!')

    return missing_list

def main():

    path = 'Z:/images'
    ext = 'exr'

    file_list = get_image_name_list(path, ext)
    miss_list = find_missing_file(file_list)

    for file in miss_list:
        print('%s missing!' % file)

main()