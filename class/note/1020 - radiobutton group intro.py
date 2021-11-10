# [Radio button group intro]

from main_window_houdini import get_main_window
from PySide2.QtWidgets import *
from PySide2 import QtCore

# QButtonGroup() seldom use!
def radio_ButtonGroup():

    main_window = get_main_window()

    window = QWidget()
    window.setParent(main_window)
    window.setWindowFlags(QtCore.Qt.Window)
    window.setWindowTitle('Radio button test')
    layout = QVBoxLayout(window)

    button_01 = QRadioButton('apple')
    button_02 = QRadioButton('orange')
    button_03 = QRadioButton('coffee')
    button_04 = QRadioButton('tea')

    fruit_grp = QButtonGroup()
    fruit_grp.addButton(button_02)
    fruit_grp.addButton(button_01)

    drink_grp = QButtonGroup()
    drink_grp.addButton(button_02)
    drink_grp.addButton(button_01)

    layout.addWidget(button_01)
    layout.addWidget(button_02)
    layout.addWidget(button_03)
    layout.addWidget(button_04)
    window.setLayout(layout)
    window.show()

def radio_GroupBox():

    main_window = get_main_window()

    window = QWidget()
    window.setParent(main_window)
    window.setWindowFlags(QtCore.Qt.Window)
    layout = QHBoxLayout(window)

    fruit_widgets = QGroupBox('Fruit')
    # fruit_widget = QtWidgets.QWidget()
    fruit_layout = QVBoxLayout(fruit_widgets)
    # fruit_label = QtWidgets.QLabel('Fruit')
    btn_01 = QRadioButton('apple')
    btn_02 = QRadioButton('orange')
    # fruit_layout.addWidget(fruit_label)
    fruit_layout.addWidget(btn_01)
    fruit_layout.addWidget(btn_02)

    drink_widgets = QGroupBox('Drink')
    # drink_widget = QtWidgets.QWidget()
    drink_layout = QVBoxLayout(drink_widgets)
    # drink_label = QtWidgets.QLabel('Drink')
    btn_03 = QRadioButton('tea')
    btn_04 = QRadioButton('coffee')
    # drink_layout.addWidget(drink_label)
    drink_layout.addWidget(btn_03)    
    drink_layout.addWidget(btn_04)

    layout.addWidget(fruit_widgets)
    layout.addWidget(drink_widgets)
    window.show()