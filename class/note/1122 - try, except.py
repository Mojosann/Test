# [try...except...]
# 使用時兩者需同時存在
# 初學時候要避免使用不然會無法找到錯誤無法debug

test_file = 'D:/unknown_path/unknown_file.txt'

# original:
# error: permission denied 
with open(test_file, 'r') as read_obj:
	content = read_obj.read()

# change this:
try:
	with open(test_file, 'r') as read_obj:
	content = read_obj.read()
except:
	# 可以印出自己想要的東西
	print('something wrong %s' % test_file)
	# 也可以跳過
	#pass

# take error message
except BaseException as e:
	# [Error 2] No such file or directory: (file_path)
	print(e)

# [Throw a error with raise]
# use raise, 並用exception要把輸出的訊息包起來
def error_test():
	print('we are using raise')
	# 吐出message後中斷執行程式
	raise Exception('Hello error!')

# 執行error_test時將會出現error
error_test()