# [QFileDialog]
# Get a file with file dialog

window = QWidget()
layout = QVBoxLayout(window)

def get_a_file():
	title = 'open a file' # 視窗標題
	init_path = 'D:/Documents/work/TWR/TD class' # 起始的路徑
	filters = 'image files (*.jpg, *.png)' # all:*.* # 檔案的篩選條件
	get_file = QFileDialog.getOpenFileName(None, title, init_path, filters)
	print(get_file)

browse_button = QPushButton()
browse_button.clicked.connect(lambda:get_a_file())
layout.addWidget(browse_button)
window.show()


# 取一個已經存在的檔案
QtWidgets.QFileDialog.getOpenFileName()
# 取多個已經存在的檔案
QtWidgets.QFileDialog.getOpenFileNames()
# 指定一個要儲存的檔案
QtWidgets.QFileDialog.getSaveFileName()
# 取一個已經存在的路徑
QtWidgets.QFileDialog.getExistingDirectory()


# [Practice]
# 建立lineedit button(可嘗試standard icon), textedit
# 點擊button時 取得任何一個檔案
# 按下確認將檔案路徑印入line edit中
# QIcon: QtWidgets.QStyle.SP_DialogOpenButton
# 注意取消時不要出現error


# nuke / houdini unfriendly!

from PySide2 import QtWidgets, QtGui, QtCore

window = QtWidgets.QWidget()
layout = QtWidgets.QHBoxLayout(window)

def get_a_file(show):
	title = 'open a file' # 視窗標題
	init_path = 'D:/Documents/work/TWR/TD class' # 起始的路徑
	filters = 'python code (*.py)' # all:*.* # 檔案的篩選條件
	get_file = QtWidgets.QFileDialog.getOpenFileName(None, title, init_path, filters)
	#print(str(get_file[0]))
	show.setText(str(get_file[0]))

label = QtWidgets.QLabel('File Path:')
line = QtWidgets.QLineEdit()
line.setFixedWidth(350)

browse_button = QtWidgets.QPushButton()
stand_icon = browse_button.style().standardIcon(QtWidgets.QStyle.SP_DialogOpenButton)
browse_button.setIcon(stand_icon)
browse_button.clicked.connect(lambda:get_a_file(line))

layout.addWidget(label)
layout.addWidget(line)
layout.addWidget(browse_button)
window.show()