# [Append content to a existed file]

from main_window_houdini import get_main_window
from PySide2.QtWidgets import *
from PySide2 import QtCore
from datetime import datetime


def button_command(file_path, result):

	new_path = str(file_path.text())
	plus = str(result.toPlainText())

	# add current time
	date = str(datetime.now())

	# add current user
	users = os.environ['USERNAME'] # by環境變數 cmd:SET (dos模式)

	file_obj = open(new_path, 'a')
	file_obj.write('\n' + plus + '\n')
	file_obj.write(date + '\n')
	file_obj.write(users + '\n')
	file_obj.close()

def UI():
	
	main_window = get_main_window()

	window = QWidget(parent=main_window, f=QtCore.Qt.Window)
	window.setWindowTitle('Append text to file tool')
	layout = QVBoxLayout(window)

	# set line edit
	path_widget = QLineEdit()
	path_widget.setPlaceholderText('path...')

	# set button
	button = QPushButton('Rewrite file')
	button.clicked.connect(lambda: button_command(path_widget, result_widget))

	# set textedit
	result_widget = QTextEdit()
	result_widget.setPlaceholderText('write something...')

	# set Label
	hint = QLabel('Info , user and time info will append to the file.')

	# set layout
	layout.addWidget(hint)
	layout.addWidget(path_widget)
	layout.addWidget(result_widget)
	layout.addWidget(button)
	window.show()