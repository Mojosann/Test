# [User Interface intro]

# 為了兼顧不同軟體版本故不用cmds
# 不要存成py檔測試
from Pyside2 import QtWidgets

# 製作一個視窗
window = QtWidgets.QWidget()
window.show()

# 製作一個帶有十個按鈕的視窗
window = QtWidgets.QWidget()
layout = QtWidgets.QVBoxLayout()

for i in range(10):
    button = QtWidgets.QPushButton('Hello World')
    layout.addWidget(button)

window.setLayout(layout)
window.show()

window = QtWidgets.QWidget()

# V: vertical (also have 水平(H)
# 在QVBoxLayout放window就不用再setLayout
# layout = QVBoxLayout()
layout = QtWidgets.QVBoxLayout(window)

for i in range(10):
    button = QtWidgets.QPushButton('Hello World')
    layout.addWidget(button)

window.show()

# 直的(自己再做橫的
from PySide2.QtWidgets import *

main_widget = QWidget()
main_widget.setWindowTitle('Testing')

# widget塞入layout
# VBox
main_layout = QVBoxLayout(main_widget)

task_list = ['proj name', 'sequence', 'shot', 'task']

for item in task_list:
    widget_grp = QWidget()

    # Hbox
    task_layout = QHBoxLayout(widget_grp)
    
    label = QLabel(item)

    # 裡面不一定要放字
    edit = QLineEdit()
    task_layout.addWidget(label)
    task_layout.addWidget(edit)

    main_layout.addWidget(widget_grp)

main_widget.show()


# 把create widget變成function 參數丟task_list的東西
from PySide2.QtWidgets import *

def create_widget(task):
    widget_grp = QWidget()
    #Hbox
    task_layout = QVBoxLayout(widget_grp)
    
    label = QLabel(item)

    # 裡面不一定要放字
    edit = QLineEdit()
    task_layout.addWidget(label)
    task_layout.addWidget(edit)

    main_layout.addWidget(widget_grp)
    main_widget.show()

# 大的widget/layout放在func下面一次執行
main_widget = QWidget()
main_widget.setWindowTitle('Testing')

# widget塞入layout
# VBox
main_layout = QHBoxLayout(main_widget)

task_list = ['proj name', 'sequence', 'shot', 'task']
for item in task_list:
    create_widget(item)


# TD example: 看如何設定變數
from PySide2 import QtWidgets

# 製作視窗
window = QtWidgets.QWidget()
# 視窗塞入layout
main_layout = QtWidgets.QVBoxLayout(window)

# 先做widget再做layout, widget塞入layout
project_widget = QtWidgets.QWidget()
project_layout = QtWidgets.QHBoxLayout(project_widget)

label = QtWidgets.QLabel('project')
edit = QtWidgets.QLineEdit()
project_layout.addWidget(label)    
project_layout.addWidget(edit)

# widget塞入主layout
main_layout.addWidget(project_widget)
window.show()