# Way of finding missing file ver 3
#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
from os import walk
from os.path import exists

folder = 'Z:\\tmp\\manting\\python\\TEST_02\\'

for root, dirs, files in walk(folder):
    title = files[0][0:8]
    file_type = files[0][12:17]
    first_no = int(files[0][8:12])
    last_no = int(files[-1][8:12])

for i in range(first_no, last_no+1):
    file_no = '{:04d}'.format(i)
    path = "{}{}{}{}".format(folder, title, file_no, file_type)
        
    if not os.path.exists(path):
        file_name = os.path.split(path)[1]
        print(file_name, 'missing!')
