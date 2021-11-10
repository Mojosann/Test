# [Checkbox intro]

# -*- coding: utf-8 -*-
from PySide2.QtWidgets import*
from functools import partial 

def button_command(check_widget_01, check_widget_02):
	# 是否選取
	if check_widget_01.isChecked():
		print(check_widget_01.text())
	if check_widget_02.isChecked():
		print(check_widget_02.text()) 

window = QWidget()
window.setWindowTitle('CheckBox test')
layout = QVBoxLayout(window) 

check_box_all = QCheckBox('All')
check_box_01 = QCheckBox('Apple')
check_box_02 = QCheckBox('Orange')
check_box_02.setChecked(True) # 預設選取
check_box_02.setChecked(False) # 預設不選取 

button = QPushButton('enter')
button.clicked.connect(partial(button_command, check_box_01, check_box_02))
layout.addWidget(check_box_all)
layout.addWidget(check_box_01)
layout.addWidget(check_box_02)
layout.addWidget(button) 

window.setLayout(layout)
window.show()