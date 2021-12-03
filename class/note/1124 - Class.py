# [Class]
# 繼承object
# 還沒有做繼承前可以不打 但不打最後執行會掛掉

class Fruit(object):
	# init = initial(Constructor)
	# 一開始建立時會執行的部分
	# self也可以改成my, this
	def __init__(self):
		# 如果沒有self 變數只會活在當前func裡面
		self.color = 'red'
		self.weight = 0
	# create method
	def setColor(self, color):
		self.color = color

# create instance
apple為Fruit的一個instance
apple = Fruit()
print(apple.color)
print(apple.weight)
apple.setColor('purple')
print(apple.color)

# 也可以在__init__提供預設值
class Fruit(object):
	def __init__(self, color):
		self.color = color
		self.weight = 0

apple = Fruit('red')
print(apple.color)

# label = QLabel('test')
lemon = Fruit('green')
print(lemon.color)


class Fruit(object):
	# init = initial(Constructor)
	# 一開始建立時會執行的部分
	# self也可以改成my, this
	def __init__(self):
		# 如果沒有self 變數只會活在當前func裡面
		self.color = 'red'
		self.weight = 0
	# create method
	def setColor(self, color):
		self.color = color

# apple繼承於fruit
class Apple(Fruit):
	def __init__(self):
		# 先去執行apple的init
		super(Apple, self).__init__('red')
		# 或者
		super(Apple, self).__init__('')
		self.setColor('red')

class Apple(Fruit):
	def __init__(self, weight):
		super(Apple, self).__init__('red')
		self.weight = weight

apple01 = Apple(10)
print(apple01.weight)
apple01.setColor('green')
print(apple01.color)

class Apple(Fruit):
	def __init__(self, weight):
		super(Apple, self).__init__('red')
		self.weight = weight
	# override method(如果不滿意原本的)
	def setColor(self, color):
		# 裡面可以加判斷式 跑super去做可逆
		self.color = 'red with %s' % color

apple01 = Apple(10)
apple01.setColor('green')
print(apple01.color)


class Lemon(Fruit):
	def __init__(self, weight):
		super(Lemon, self).__init__('green')
		self.weight = weight

	def setColor(self, color):
		self.color = 'green with %s' % color

lemon01 = Lemon(10)
lemon01.setColor('yellow')
print(lemon01.color)

# 繼承(inheritance)提高程式碼的重用性(reusable)
# 多形(polymorphism)讓各class有一致性的介面 易於擴充維護