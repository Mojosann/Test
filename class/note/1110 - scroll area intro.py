from main_window_maya import get_main_window
from PySide2.QtWidgets import *
from PySide2 import QtCore

def UI():

	main_window = get_main_window()

	window = QWidget()
	window.setParent(main_window)
	window.setWindowFlags(QtCore.Qt.Window)
	layout = QVBoxLayout(window)

	button_list_widget = QWidget()
	button_list_layout = QVBoxLayout(button_list_widget)

	for i in range(1, 51):
		button_name = 'BUTTON_%02d' % i
		button_widget = QPushButton(button_name)
		button_list_layout.addWidget(button_widget)

	scroll_widget = QScrollArea()

	# 將剛剛建立的button_list_widget指定給scroll_widget
	scroll_widget.setWidget(button_list_widget)
	# 設定scroll_widget裡的widget允許配合變換大小(resize)
	scroll_widget.setWidgetResizable(True)

	# 取得scroll_widget裡的widget
	scroll_widget.widget()
	# 移除scroll_widget裡的widget(少用)
	scroll_widget.takeWidget()

	layout.addWidget(scroll_widget)
	window.show()

UI()