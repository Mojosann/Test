# Way of finding missing file ver 1
# -*- coding:utf-8 -*-

import os
#str.split(string)分割字串
#.join(list) 將列表組成字串

for i in range(1001, 1201):
    filename = "td_test.%4d.jpg" % i
    mainpath = 'Z:\\tmp\\manting\\python\\TEST_01'
    path = mainpath + filename
    print(path)
    
    if not os.path.exists(path):
        file_path = os.path.split(path) #分割出目錄與檔案
        missing = file_path[-1]
        print(missing, '不存在')'''
