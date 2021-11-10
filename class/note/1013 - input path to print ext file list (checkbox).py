# [Show ext file (checkbox)] 

from main_window_houdini import get_main_window
from PySide2.QtWidgets import *
from PySide2 import QtCore
from functools import partial
import os 

def get_image_file(input_path, ext, result):

	path_data = os.listdir(input_path)

	for image_file in path_data:
		if ext in image_file:
			# print(image_file)
			result.append(image_file) 

def button_command(input_widget, check_list, result):

	input_path = input_widget.text()

	for checkbox in check_list:
		if checkbox.isChecked():
			ext_name = checkbox.text()
			# use button to call function

	get_image_file(input_path, ext_name, result) 

def UI():

	main_window = get_main_window()

	window = QWidget()
	window.setParent(main_window)
	window.setWindowFlags(QtCore.Qt.Window)
	window.setWindowTitle('Get ext file')
	layout = QVBoxLayout(window) 

	path = QGroupBox('Path info')	
	path_layout = QVBoxLayout(path)

	file_path = QLineEdit()
	# u'chinese words…'(only maya)
	file_path.setPlaceholderText('path…') 

	# set checkbox
	check_list =[]
	for ext_name in ['png', 'exr', 'jpg']:
		check_widget = QCheckBox(ext_name) # QRadioButton
		check_list.append(check_widget) 
	
	result = QTextEdit()

	# set button
	button = QPushButton('Show ext file')
	button.clicked.connect(partial(button_command, file_path, check_list, result)) 

	# set layout
	path_layout.addWidget(file_path)
	for check_widget in check_list:
		path_layout.addWidget(check_widget)

	path_layout.addWidget(button)
	layout.addWidget(path) 
	layout.addWidget(result)
	window.show()