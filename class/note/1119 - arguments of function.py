# [Arguments of function]
# 參數backup預設為true, 執行function時可不提供
# def td_copy_file(source_file, target_file, backup=True):

# [Default value]
# 不能放第一個! 會打架
# 只能放後面才會知道會分配給誰
def func(a=1, b, c):

def func(a, b, c=1):
	return None

func(1) # error
func(1, 2) # error
func(1, 2, 3)

# [Arbitrary Arguments: *args]

def test_func(*args):
	# 代表想放多少參數都可以
	# args為tuple
	print(args)

test_func(1, 2, 3, 4, 'a')

def test_func(a, b, *args):
	print(args)
	print(a, b)

test_func(1, 2) # 至少要給兩個 其他想給多少給多少
# args送進func時候可以用tuple index個別取出存成變數

def test_func(a, b, c):
	print(a, b, c)

# 下3個參數
test_tuple = (1, 2, 3)
test_func(*test_tuple) # *會炸開所有item

#下5個參數
test_tuple = (1, 2, 3, 4, 5) # 太多了!
test_func(*test_tuple)


# [Pass arguments by name]
def test_func(a, b, c):
	print(a, b, c)

# 依照參數名稱提供
test_func(c=3, b=2, a=1)

# 依照參數順序提供
test_func(3, 2, 1)

# [Arbitrary keyword arguments: **kwargs]
def test_func(**kwargs):
	print(kwargs)

# 幾個帶有變數名稱的參數
test_func(a=1, b=2)

def test_func(a, **kwargs):
	print(kwargs)
	print(a)

test_func(a=0, b=2, c=3) # 不能不給a

def test_func(a, b, c):
	print(a, b, c)

test_dict = {'a':1, 'b':2, 'c':3}
test_func(**test_dict)

# TypeError: test_func() takes exactly 3 arguments (2 given)
test_dict = {'a':1, 'b':2}
test_func(**test_dict)

# [example]
def test_func(a, b, c=3, *args, **kwargs):
	print(a)
	print(b)
	print(c)

	for arg in args:
		print(arg)

	for key, value in kwargs.items():
		print(key, value)

test_func(1, 2)
test_func(1, 2, 3)
test_func(1, 2, 3, 4)
test_func(1, 2, 3, 4, d=5, e=6)