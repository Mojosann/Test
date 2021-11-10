# [Choose fruit & drink tool (radiobutton)]

from main_window_houdini import get_main_window
from PySide2.QtWidgets import *
from PySide2 import QtCore
from functools import partial

# result will get a choose dictionary
def button_command(fruit_grp, drink_grp, text):

	result = {}
	if result.get('Fruit') == None:
		result['Fruit'] = {}
	if result.get('Drink') == None:
		result['Drink'] = {}

	for item in fruit_grp:
		if item.isChecked():
			result['Fruit'][str(item.text())] = True
		else:
			result['Fruit'][str(item.text())] = False

	for item in drink_grp:
		if item.isChecked():
			result['Drink'][str(item.text())] = True
		else:
			result['Drink'][str(item.text())] = False

	text.append(str(result))

def UI():

	main_window = get_main_window()

	window = QWidget()
	window.setParent(main_window)
	window.setWindowFlags(QtCore.Qt.Window)
	window.setWindowTitle('Choose fruit & drink tool')

	layout = QVBoxLayout(window)
	mini_widget = QWidget()
	mini_layout = QHBoxLayout(mini_widget)

	fruit_widgets = QGroupBox('Fruit')
	fruit_layout = QVBoxLayout(fruit_widgets)
	btn_01 = QRadioButton('apple')
	btn_02 = QRadioButton('orange')
	fruit_layout.addWidget(btn_01)
	fruit_layout.addWidget(btn_02)

	drink_widgets = QGroupBox('Drink')
	drink_layout = QVBoxLayout(drink_widgets)
	btn_03 = QRadioButton('tea')
	btn_04 = QRadioButton('coffee')
	drink_layout.addWidget(btn_03)
	drink_layout.addWidget(btn_04)

	fruit_btn_list = [btn_01, btn_02]
	drink_btn_list = [btn_03, btn_04]

	edit_widget = QTextEdit()

	button = QPushButton('Get resault dictionary')
	button.clicked.connect(partial(button_command, fruit_btn_list, drink_btn_list, edit_widget))

	layout.addWidget(mini_widget)
	mini_layout.addWidget(fruit_widgets)
	mini_layout.addWidget(drink_widgets)
	layout.addWidget(button)
	layout.addWidget(edit_widget)

	window.show()