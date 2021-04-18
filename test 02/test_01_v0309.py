# Way of finding missing file ver 2
#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
from os import walk
from os.path import exists

mainpath = 'D:\\document\\script\\TEST_01\\'

for root, dirs, files in walk(mainpath):
    first_no = int(files[0][8:12])
    last_no = int(files[-1][8:12])
    
for i in range(first_no, last_no+1):
    file_name = "td_test.%04d.jpg" % i
    path = mainpath + file_name

    if not os.path.exists(path):
        file_path = os.path.split(path)
        missing = file_path[-1]
        print(missing, 'missing')


#取得file_name的邏輯：
#可以先取得非數字部分 > 撈成字串
#再取得數字部分變成list
#最後取副檔名
#將三者結合丟到迭代器裡判斷路徑是否存在

