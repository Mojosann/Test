from main_window_houdini import get_main_window
from PySide2.QtWidgets import *
from PySide2 import QtCore

# [write a json file]
import json
import random

data_list = []
test_list = ['ani', 'fx']

for i in range(1, 51):
	data_dict = {}
	data_dict['name'] = 'mini_%02d' % i
	data_dict['type'] = test_list[random.randint(0, 1)]

	data_list.append(data_dict)

	#print(data_dict)

with open('D:/Documents/work/TWR/TD class/file_format/example.json', 'w') as write_obj:
	json_content = json.dumps(data_list, indent=2, sort_keys=True)
	write_obj.write(json_content)

# [set json file attr name's info as button name and group in scroll area]
# if change json file, button name will change

def scroll_UI():

	main_window = get_main_window()

	window = QWidget()
	window.setParent(main_window)
	window.setWindowFlags(QtCore.Qt.Window)
	layout = QVBoxLayout(window)

	button_list_widget = QWidget()
	button_list_layout = QVBoxLayout(button_list_widget)

	with open('D:/Documents/work/TWR/TD class/file_format/example.json', 'r') as read_obj:
		content = read_obj.read()
		data = json.loads(content)

		for item in data:
			name = item['name']
			button_name = name
			button_widget = QPushButton(button_name)
			button_list_layout.addWidget(button_widget)

	scroll_widget = QScrollArea()
	scroll_widget.setWidget(button_list_widget)
	scroll_widget.setWidgetResizable(True)

	layout.addWidget(scroll_widget)
	window.show()

def tab_UI():

	main_window = get_main_window()

	window = QWidget()
	window.setParent(main_window)
	window.setWindowFlags(QtCore.Qt.Window)
	layout = QVBoxLayout(window)

	tab_widget = QTabWidget()

	ani_button_list_widget = QWidget()
	ani_button_list_layout = QVBoxLayout(ani_button_list_widget)

	fx_button_list_widget = QWidget()
	fx_button_list_layout = QVBoxLayout(fx_button_list_widget)

	with open('D:/Documents/work/TWR/TD class/file_format/example.json', 'r') as read_obj:
		content = read_obj.read()
		data = json.loads(content)

		for item in data:
			name = item['name']
			button_name = name
			button_widget = QPushButton(button_name)

			if item['type'] == 'ani':
				ani_button_list_layout.addWidget(button_widget)

			if item['type'] == 'fx':
				fx_button_list_layout.addWidget(button_widget)

	ani_scroll_widget = QScrollArea()
	fx_scroll_widget = QScrollArea()

	ani_scroll_widget.setWidget(ani_button_list_widget)
	fx_scroll_widget.setWidget(fx_button_list_widget)

	ani_scroll_widget.setWidgetResizable(True)
	fx_scroll_widget.setWidgetResizable(True)

	tab_widget.addTab(ani_scroll_widget, 'ani')
	tab_widget.addTab(fx_scroll_widget, 'fx')

	layout.addWidget(tab_widget)
	window.show()