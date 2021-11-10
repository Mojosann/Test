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