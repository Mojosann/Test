from main_window_houdini import get_main_window
from PySide2.QtWidgets import *
from PySide2 import QtCore

# D:\temp\test.txt
def button_command(file_path, result):

	new_path = str(file_path.text())
	content = str(result.toPlainText())

	file_obj = open(new_path, 'w')
	file_obj.write(content)
	file_obj.close()

def UI():
	main_window = get_main_window()

	window = QWidget(parent=main_window, f=QtCore.Qt.Window)
	window.setWindowTitle('Write file tool')
	layout = QVBoxLayout(window)

	# set line edit
	path_widget = QLineEdit()
	path_widget.setPlaceholderText('path...')

	# set button
	button = QPushButton('write a file')
	button.clicked.connect(lambda: button_command(path_widget, result_widget))

	# set textedit
	result_widget = QTextEdit()
	result_widget.setPlaceholderText('write something...')

	# set layout
	layout.addWidget(path_widget)
	layout.addWidget(result_widget)
	layout.addWidget(button)
	window.show()