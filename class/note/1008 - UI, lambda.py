# [input name button window]

# from PySide2 import QtWidgets as..
from PySide2.QtWidgets import *

window = QWidget()
window.setWindowTitle('Testing')

# layout = QHBoxLayout(window) # parent=window
layout = QHBoxLayout()

# if int?
def show_line_edit(input_widget):

    # QLineEdit用text()取得內容
    print('hello ' + input_widget.text()) # return type == str


# button如果要用hotkey執行要判斷原3D內的hotkey有哪些避免衝突
# 可以set button執行完後就不可逆了
button = QPushButton('enter')
button.clicked.connect(lambda: show_line_edit(name))

# name = QLineEdit('Amy') 'Amy' as default value
name = QLineEdit()
name.setPlaceholderText("Don't mind me.") 

# name = QLineEdit().setPlaceholderText("Don't mind me.")會爆掉


# 注意add的順序
layout.addWidget(name)
layout.addWidget(button)

# window group layout進去
window.setLayout(layout)
window.show()

def my_function():
    print('Hello')

button = QtWidgets.QPushButton('Enter')
button.clicked.connect(my_function)
# 如果func裡面丟參數會執行錯誤


# 解釋lambda邏輯
# 也有別的寫法替代lambda 需要import其他module做setting
def my_function(name, age):
    print('hello ', name)
    print('you are %s old' % str(age))

def call_function():
    my_function('Pan', 35)

# 把call func變成lambda(匿名函式)
lambda: my_function('Pan', 35)

# 怎麼印出lambda的結果