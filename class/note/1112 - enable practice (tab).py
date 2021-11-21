# [widget.setEnabled practice (tab)]

from main_window_houdini import get_main_window
from PySide2.QtWidgets import *
from PySide2 import QtCore

def enable_UI():

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

	with open('D:/Documents/work/TWR/TD class/file_format/random.json', 'r') as read_obj:
		content = read_obj.read()
		data = json.loads(content)

		for item in data:
			name = item['name']
			button_name = name
			button_widget = QPushButton(button_name)

			if item['type'] == 'animation':
				ani_button_list_layout.addWidget(button_widget)

			if item['type'] == 'fx':
				fx_button_list_layout.addWidget(button_widget)

			if item['enable'] == 'True':
				button_widget.setEnabled(True)

			if item['enable'] == 'False':
				button_widget.setEnabled(False)

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