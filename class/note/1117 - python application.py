# [Python Application]

# [Build at console mode]
# 將python file拉進cmd就會自動執行
# 或者貼上file path

# 也可以直接在cmd這樣做：
# python C:\Users\Academy\Desktop\coding\file_format\1117.py

# 將python.exe丟進cmd: C:\Users\Academy>C:\Python27\python.exe
# 然後空一格 將file path丟進去執行(如果要特別指定python version)
# C:\Users\Academy>C:\Python27\python.exe C:\Users\Academy\Desktop\coding\file_format\1117.py
# 這樣就可以執行!

# 轉檔程式的邏輯:
# C:\Users\Academy>ffmpeg.exe '要轉檔的路徑'

# [Build at Sublime text]
# tool>build system> resault
# ctrl+b


# [__name__ == '__main__']
# module attribute
# python.org

# 此檔案的絕對路徑
print(__file__)

# 執行module的名稱
print(__name__)

# 執行目前的module時..
if __name__ == '__main__':
	main()

# 當file是一個讓人import module時
# name就不會=module而會=module name
# ex: import my_module
# __name__ is my_module

# 因為別人import module不一定要用到main的所有執行可能只是某幾個func
# 寫if __name__ == '__main__': 可以避免別人run到原本module的main()


# [sys (system) module]
# get current python version
print(sys.version)

# 取得目前python用來載入module的相關路徑 type=list
# 透過以下這個尋找module
sys.path

for item in sys.path:
	print(item)

# 離開python後就會自動消失不會永久保存
sys.path.append(a_new_module_path)
sys.path.insert(0, a_new_module_path)
# 這裡的index是有意義的 會依照這個index去尋找module
# 一旦找到了同名的module就不會讀找到後面的module

import sys
# 存了一個叫做may.py在這個path
def main():
	print('may I have a cup.')

# 如果module有重名 可能會出現import module取錯的情況
sys.path.append("C:/Users/Academy/Desktop/coding")
for item in sys.path:
	print(item)

import may
reload(may)
may.main()
# 這樣就不一定要把module放進DDC的module folder內

# 用來取得console模式執行的參數
sys.argv

# sys.argv是一個list(index=0為程式本身)
print(sys.argv[0])

# 參數的數量
len(sys.argv)

# 在console mode讓程式結束
sys.exit()


# [shutil (shell utility) module]
# 複製檔案

# copy file(特別注意路徑、檔案是否已經存在的情況)
shutil.copyfile(source_file, target_file)

# 複製檔案並且連permission mode也一併複製過去
# modify time會是現在的時間
shutil.copy(source_file, target_file)

# 複製檔案並且連metadata的資訊也一併複製過去
# modify time會是現在的時間
shutil.copy2(source_file, target_file)

# 複製資料夾(連底下的子資料夾內容都會一併複製過去)
# metadata的資訊也會一併複製過去
# 不常用: 不保留metadata的方法就要避開此方法
shutil.copytree(source_folder, target_folder)

# 檔案取得權限不足時會出現permission error

# [Practice]
import os, shutil

source_path = 'Z:/practice/copy_test'
target_path = 'C:/Users/Academy/Desktop'

for item in os.listdir(path):

	if item in ['old', 'test']:
		continue

	if item == 'source':
		source_folder = '%s/%s' % (source_path, item)
		target_folder = '%s/%s' % (target_path, item)
		print(source_folder)
		print(target_folder)
		shutil.copytree(source_folder, target_folder)

	if '.' in item:
		source_file = '%s/%s' % (source_path, item)
		target_file = '%s/%s' % (target_path, item)
		print(source_file)
		print(target_file)
		shutil.copytree(source_file, target_file)