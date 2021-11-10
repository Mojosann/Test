# [Get exr file list]

import os

def get_image_name_list(input_path):

    result_list = []
    path_data = os.listdir(input_path)

    for image_file in  path_data:
        if 'exr' in image_file:
            result_list.append(image_file)

    return result_list