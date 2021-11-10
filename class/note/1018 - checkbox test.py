# [CheckBox test]

from main_window_houdini import get_main_window
from PySide2.QtWidgets import *
from PySide2 import QtCore
from functools import partial

def button_command(check_list, result_syn):
    # 是否選取
    for item in check_list:
        if item.isChecked():
            # print(item.text())
            result_syn.append(item.text())

def all_button(all, check_box_list):
    
    for item in check_box_list:
        if all.isChecked():
            item.setChecked(True) # 預設選取
        else:
            item.setChecked(False) # 預設不選取

def button_alone(all, check_box_list):
    
    if len(check_box_list) == 2:
        all.setChecked(True)

    for item in check_box_list:        
        # 如果有一個選項沒選到
        if not item.isChecked():
            # 取消勾選all
            all.setChecked(False)
        else:
            item.setChecked(True)

def UI():

    main_window = get_main_window()

    window = QWidget(parent=main_window, f=QtCore.Qt.Window)
    window.setWindowTitle('CheckBox test')
    layout = QVBoxLayout(window)

    check_box_all = QCheckBox('All')

    check_box_list = []
    for item in ['Apple', 'Orange']:
        check_box_item = QCheckBox(item)
        check_box_list.append(check_box_item)
        check_box_item.clicked.connect(partial(button_alone, check_box_all, check_box_list))
    
    check_box_all.clicked.connect(partial(all_button, check_box_all, check_box_list))
    
    result = QTextEdit()

    # set button
    button = QPushButton('enter')
    button.clicked.connect(partial(button_command, check_box_list, result))

    layout.addWidget(check_box_all)
    for item in check_box_list:
        layout.addWidget(item)

    layout.addWidget(button)
    layout.addWidget(result)
    window.setLayout(layout)

    window.show()