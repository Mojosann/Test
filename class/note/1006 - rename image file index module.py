# [Rename image file index module]

import os 

def get_image_name_list(input_path, ext):
    
    result_list = []
    path_data = os.listdir(input_path)

    for image_file in path_data:
        if ext in image_file:
            #get full folder path
            new = input_path + '//' + image_file
            result_list.append(new)

    return result_list

#file number redefine number
def rename_image_to_2001(path_list):

    target_image_list = []
    #replace new num order
    for i in range(1, len(path_list)+1):
        for source_image in path_list:
            target_image = source_image.split('.')[0] + '.1%03d.' % i + source_image.split('.')[-1]
        target_image_list.append(target_image)

    for order in range(len(path_list)):
        print(path_list[order])
        print(target_image_list[order])
        print('')
        os.rename(path_list[order], target_image_list[order])

def main():
    file_list = get_image_name_list('C://User//Academy//Documents//temp//image', 'jpg')
    rename_image_to_1001(file_list)

main()