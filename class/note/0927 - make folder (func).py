# [Make folder path]

import os

def make_dir(input_path):

    folder_path = ''
    folder_list = input_path.split('/')

    for folder in folder_list:
        folder_path = folder_path + '/' + folder
        
        if os.path.isdir(folder_path[1:]) != True:
            os.mkdir(folder_path[1:])

    print(folder_path[1:])