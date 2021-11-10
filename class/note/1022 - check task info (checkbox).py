# [Check task info (checkbox)]

from main_window_houdini import get_main_window
from PySide2.QtWidgets import *
from PySide2 import QtCore
from functools import partial

def button_command(check_box_list, text):

    for item in check_box_list:
        
        if item.isChecked():
            text.append(item.text())

def all_button(all, check_box_list):

    for item in check_box_list:

        if all.isChecked():
            item.setChecked(True)
        else:
            item.setChecked(False)

def button_alone(all, check_box_list):
    
    if len(check_box_list) == 4:
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
    window.setWindowTitle('Check task')
    layout = QVBoxLayout(window)

    task_info = QGroupBox('Task info')
    task_layout = QVBoxLayout(task_info)

    check_box_list = []
    for item in ['animation', 'lighting', 'fx', 'comp']:
        check_box_item = QCheckBox(item)
        check_box_list.append(check_box_item)

    check_box_all = QCheckBox('All')
    check_box_all.clicked.connect(partial(all_button, check_box_all, check_box_list))

    for item in check_box_list:
        item.clicked.connect(partial(button_alone, check_box_all, check_box_list))

    edit_widget = QTextEdit()

    button = QPushButton('enter')
    button.clicked.connect(partial(button_command, check_box_list, edit_widget))

    task_layout.addWidget(check_box_all)
    for item in check_box_list:
        task_layout.addWidget(item)

    task_layout.addWidget(button)
    layout.addWidget(task_info)
    layout.addWidget(edit_widget)
    window.show()