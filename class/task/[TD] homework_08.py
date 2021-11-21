# Maya cant show setToolTip!

from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui
import json

def create_custom_button(name, type, date, thumbnail, description):

	widget_unit = QPushButton()
	layout_unit = QVBoxLayout(widget_unit)

	widget_unit.setFixedWidth(255)
	widget_unit.setFixedHeight(350)
	widget_unit.setToolTip(description)
		
	widget_mini = QWidget()
	layout_mini = QVBoxLayout(widget_mini)

	pic_widget = QLabel()
	image = QtGui.QPixmap(thumbnail)
	pic_widget.setPixmap(image)
		
	type_label = QLabel(type)
	name_label = QLabel(name)
	date_label = QLabel(date)

	type_label.setStyleSheet('color: #CF9E9E; font-size: 18px; font-weight: bold; font-family: calibri;')
	name_label.setStyleSheet('color: tan; font-size: 25px; font-weight: bold; font-family: calibri;')
	date_label.setStyleSheet('color: #ADADAD; font-style:italic;')
		
	type_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
	name_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
	date_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)

	layout_mini.addWidget(type_label)
	layout_mini.addWidget(name_label)

	layout_mini.addWidget(date_label)
	layout_unit.addWidget(pic_widget)
	layout_unit.addWidget(widget_mini)

	return widget_unit
		

window = QWidget()
layout = QVBoxLayout(window)

button_list_widget = QWidget()
button_list_layout = QVBoxLayout(button_list_widget)

button_list = []
with open('‪D:/Documents/work/TWR/TD class/file_format/The Powerpuff Girls.json', 'r') as read_obj:
	content = read_obj.read()
	data = json.loads(content)

for item in data:
	button_widget = create_custom_button(item['name'], item['type'], item['update_time'], item['thumbnail'], item['description'])
	button_list_layout.addWidget(button_widget)
	button_list.append(button_widget)

scroll_widget = QScrollArea()
scroll_widget.setWidget(button_list_widget)
scroll_widget.setWidgetResizable(True)
layout.addWidget(scroll_widget)
window.show()