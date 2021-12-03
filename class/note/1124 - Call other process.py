import os
# [Call other process]
# cmd可以直接輸入黃字部分

# 開啟檔案總管(explorer)
os.system('explorer')

# 開啟檔案總管 並找到指定路徑
os.system('explorer Z:/practice')

# 開啟小算盤(calc)
os.system('calc')

# 開啟記事本(開啟程式直到結束後才會出現finish)
print('before')
os.system('notepad')
print('after')

# recogsife
# rehersife

file_path = 'Z:/practice/all_file_test'
file_list = []
for item in os.listdir(file_path):
	file = '%s/%s' % (file_path, item)
	file_list.append(file)

C:\User\Academy>dir

C:\User\Academy>dir /?
顯示清單檔案以列出目錄中的檔案及子目錄。
/B 使用單純格式(沒有標頭資訊或摘要)。
/S 顯示指定目錄及所有子目錄中的檔案。

dir /B /S

# 使用dir /b /s取得資料夾底下的所有檔案
cmd = 'dir /b /s Z:\\practice\\all_file_test'
cmd = r'dir /b /s Z:\\practice\\all_file_test' # keep raw string(防止轉義)
# resault = os.system(cmd)
# print(resault)
# 透過type取得型態
# print(type(resault))
# os.syetem執行時只會回傳int(1:執行正常, 0:不正常)

# os.popen取得回傳內容
# popen = process open
# resault = os.popen(cmd).read() # this is simple way

p_obj = os.popen(cmd)
resault = p_obj.read()
# print(resault)
print(resault.split('\n')[:-1])

# [取得file path底下的所有檔案(僅限檔案)]
def get_file_list(input_path):

	resault = []
	if os.path.isdir(input_path):
		cmd = 'dir /b /s %s' % (input_path.replace('/', '\\'))
		buffer_resault = os.popen(cmd).read()

		for line in buffer_resault.split('\n'):
			line = line.strip()

			if line == '':
				continue
			if not os.path.isdir(line):
				resault.append(line)

		for item in resault:
			print(item)

get_file_list('Z:/practice/all_file_test')


# [Subprocess]
import subprocess
# 開啟檔案總管 並指到特定路徑
# cmd_list = ['explorer', 'Z:\\practice\\all_file_test']
# cmd = 'explorer Z:\\practice\\all_file_test'
# subprocess.Popen(cmd) # 給字串或清單都可以

# 使用dir /b /s取的資料夾底下的所有檔案
cmd_list = ['dir', '/b', '/s', 'Z:\\practice\\all_file_test']
# subprocedd.Popen(cmd_list, shell=True) # 使用shell方式執行令命

# std = standard 標準輸出
# shell=True 用當下作業系統的console去執行不然會做不成
# batch mode
p = subprocess.Popen(cmd_list, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 用communicate不然就是read()
print(p.communicate()[0]) # stdout
print('+-----------------')
print(p.communicate()[1]) # stderr
# 因為已經被communicate拿走了所以以下是空的
p.stdout.read()
p.stderr.read()


# png轉檔jpg
# 第三方exe做事 添加所需的參數即可
C:\User\Academy>"C:\Program Files\Autodesk\Maya2020\bin\imconvert.exe" D:\Benedetta\Bubbles.png D:\Benedetta\Bubbles.jpg
# 用maya batch跑render
"C:\Program Files\Autodesk\Maya2020\bin\mayabatch.exe"