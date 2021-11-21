# [widget.setEnabled practice (checkbox)]

# 暫時將tab移除 全部放在同一個scroll area
# UI上新增兩個checkbox 分別為animation, fx
# 切換checkbox時, 將內容與所有button的type進行判斷
# 將不符合的button隱藏起來

from main_window_houdini import get_main_window
from PySide2.QtWidgets import *
from PySide2 import QtCore

def checkbox_command(type, checkbox_set):

	with open('D:/Documents/work/TWR/TD class/file_format/random.json', 'r') as read_obj:
		content = read_obj.read()
		data = json.loads(content)

		for item in data:
			if item['type'] == type.text():
				if item['enable'] == 'False':
					for checkbox in checkbox_set:
						if item['name'] == checkbox.text():
							if type.isChecked() == True:
								checkbox.setEnabled(False)
							else:
								checkbox.setEnabled(True)

def checkbox_UI():

	main_window = get_main_window()

	window = QWidget()
	window.setParent(main_window)
	window.setWindowFlags(QtCore.Qt.Window)
	layout = QVBoxLayout(window)

	check_box_widget = QWidget()
	ani_check = QCheckBox('animation')
	fx_check = QCheckBox('fx')

	ani_check.clicked.connect(lambda: checkbox_command(ani_check, button_list))
	fx_check.clicked.connect(lambda: checkbox_command(fx_check, button_list))	

	check_box_layout = QHBoxLayout(check_box_widget)
	check_box_layout.addWidget(ani_check)
	check_box_layout.addWidget(fx_check)

	button_list_widget = QWidget()
	button_list_layout = QVBoxLayout(button_list_widget)

	button_list = []
	with open('D:/Documents/work/TWR/TD class/file_format/random.json', 'r') as read_obj:
		content = read_obj.read()
		data = json.loads(content)

		for item in data:
			name = item['name']
			button_name = name
			button_widget = QPushButton(button_name)
			button_list_layout.addWidget(button_widget)
			button_list.append(button_widget)

	scroll_widget = QScrollArea()
	scroll_widget.setWidget(button_list_widget)
	scroll_widget.setWidgetResizable(True)
	layout.addWidget(check_box_widget)
	layout.addWidget(scroll_widget)
	window.show()