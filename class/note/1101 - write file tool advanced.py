# [Write file tool (Advanced)]

from main_window_houdini import get_main_window
from PySide2.QtWidgets import *
from PySide2 import QtCore
import os

# D:\temp\test.txt
def button_command(new_path, input_text):

	text_edit = str(input_text.toPlainText())
	request_path = str(new_path.text())

	# get request file folder path
	folder = os.path.dirname(request_path)

	# check if path is exist
	if os.path.isdir(folder) == True:
		file_obj = open(request_path, 'w')
		content = file_obj.write(text_edit)
		file_obj.close()

	# if path not exist: make folder path then create file
	else:
		new_folder = os.mkdir(folder)
		file_obj = open(request_path, 'w')
		content = file_obj.write(text_edit)
		file_obj.close()

def UI():

	main_window = get_main_window()
	window = QWidget()

	window.setParent(main_window)
	window.setWindowFlags(QtCore.Qt.Window)
	window.setWindowTitle('Write file tool (advanced)')
	layout = QVBoxLayout(window)

	file_info_widget = QGroupBox('File info')
	file_info_layout = QVBoxLayout(file_info_widget)

	hint_label = QLabel('input path to check if exist then write content to a file.')

	path_widget = QLineEdit()
	path_widget.setPlaceholderText('path...')

	# set button
	button = QPushButton('write a file')
	button.clicked.connect(lambda: button_command(path_widget, result_widget))

	# set textedit
	result_widget = QTextEdit()
	result_widget.setPlaceholderText('write something...')

	# set layout
	file_info_layout.addWidget(hint_label)
	file_info_layout.addWidget(path_widget)
	file_info_layout.addWidget(result_widget)
	file_info_layout.addWidget(button)
	layout.addWidget(file_info_widget)
	window.show()