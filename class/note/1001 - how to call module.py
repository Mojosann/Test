import create_file
reload(create_file)
file_list = create_file.create_image_name_list(100, 170, 105)
print(file_list)

import test_image_file
reload(test_image_file)
test_image_file.main()