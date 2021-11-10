# [QPushButton Practice]

# print 'hello' button 
from PySide2.QtWidgets import* 

window = QWidget()
window.setWindowTitle('Testing')
layout = QHBoxLayout(window) 

def my_function():
	print('Hello') 

button = QPushButton('enter')
button.clicked.connect(my_function)
layout.addWidget(button)
window.setLayout(layout)
window.show() 


# print hello 'enter str'
from PySide2.QtWidgets import*

window = QWidget()
window.setWindowTitle('Testing')
layout = QHBoxLayout(window) 

def show_line_edit(input_widget):
	# QLineEdit用text()取的內容
	print('hello ' + input_widget.text()) 

button = QPushButton('enter')
name = QLineEdit()

# lambda執行最後結果
button.clicked.connect(lambda: show_line_edit(name))
layout.addWidget(name)
layout.addWidget(button)
window.setLayout(layout)
window.show() 


# Py2的lambda寫法
# 因為無法print出結果
def show_name(name):
	print('Hello ' + name) 

(lambda name: show_name(name))('Pan')
f = Lambda name: show_name(name)
f('Pan') 

# Py3的寫法
(Lambda name: print('Hello' + name))('Pan')
f = Lambda name: print('Hello' + name)
f('Pan') 


# make 10 buttons
from PySide2.QtWidgets import*
from functools import partial 

window = QWidget()
window.setWindowTitle('10 button test')
layout = QVBoxLayout(window) 

def show_line_edit(input_widget):
	print('Hello ' + input_widget) 

for i in range(1, 11):
	button = QPushButton('enter %s' % i)
	name = QLineEdit()
	# button.clicked.connect(lambda: show_line_edit(i)))
	layout.addWidget(button) 

window.setLayout(layout)
window.show()