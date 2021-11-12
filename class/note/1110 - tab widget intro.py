from main_window_maya import get_main_window
from PySide2.QtWidgets import *
from PySide2 import QtCore

def UI():

	main_window = get_main_window()

	window = QWidget()
	window.setParent(main_window)
	window.setWindowFlags(QtCore.Qt.Window)
	layout = QVBoxLayout(window)

	tab_widget = QTabWidget()

	widget_01 = QLabel('Hello')
	widget_02 = QPushButton('OK')
	button = QPushButton('enter')
	
	# tab的label自行命名
	tab_widget.addTab(widget_01, 'AAA')
	tab_widget.addTab(widget_02, 'BBB')

	layout.addWidget(tab_widget)
	layout.addWidget(button)
	window.show()

UI()