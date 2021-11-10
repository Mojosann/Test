# module name: rename_obj_tool

# ver.Maya
from PySide2.QtWidgets import*
from PySide2.QtCore import*
import maya.cmds as cmds
import main_window_maya

def rename_selected_nodes(new_name):
    # update selection
    selected_list = cmds.ls(sl=True)
    
    # rename obj
    cont = 1
    for obj in sorted(selected_list):
        cmds.rename(obj, new_name + '_%03d' % cont)
        cont += 1

def button_command(name_widget):
    get_name = name_widget.text()
    rename_selected_nodes(get_name)

def UI():
    # main window
    main_window = main_window_maya.get_main_window()

    window = QWidget()
    window.setParent(main_window)
    window.setWindowFlags(Qt.Window)

    window.setWindowTitle('Rename object tool')
    main_layout = QVBoxLayout(window)

    # widget
    obj_name = QLineEdit()
    obj_name.setPlaceholderText('set new name...')
    button = QPushButton('Raname')
    button.clicked.connect(lambda: button_command(obj_name))

    main_layout.addWidget(obj_name)
    main_layout.addWidget(button)

    window.show()


# ver.Nuke
from PySide2.QtWidgets import*
from PySide2.QtCore import*
import nuke
import main_window_nuke

def rename_selected_nodes(new_name):
    # update selection
    selected_list = nuke.selectedNodes()
    get_name = lambda node: node.knob('name').getValue()
    sorted_list = sorted(selected_list, key=get_name)
    
    # rename obj
    cont = 1
    for obj in sorted_list:
        obj.knob('name').setValue(new_name + '_%03d' % cont)
        cont += 1

def button_command(name_widget):
    get_name = name_widget.text()
    rename_selected_nodes(get_name)

def UI():
    # main window
    main_window = main_window_nuke.get_main_window()

    window = QWidget(main_window)
    window.setWindowFlags(Qt.Window)

    window.setWindowTitle('Rename object tool')
    main_layout = QVBoxLayout(window)

    # widget
    obj_name = QLineEdit()
    obj_name.setPlaceholderText('set new name...')
    button = QPushButton('Raname')
    button.clicked.connect(lambda: button_command(obj_name))

    main_layout.addWidget(obj_name)
    main_layout.addWidget(button)

    window.show()


# ver.Houdini
from PySide2.QtWidgets import*
from PySide2.QtCore import*
import hou
import main_window_houdini

def rename_selected_nodes(new_name):
    # update selection
    selected_list = hou.selectedNodes()
    
    # rename obj
    cont = 1
    for obj in sorted(selected_list):
        obj.setName(new_name + '_%03d' % cont)
        cont += 1

def button_command(name_widget):
    get_name = name_widget.text()
    rename_selected_nodes(get_name)

def UI():
    # main window 
    main_window = main_window_houdini.get_main_window()
    window = QWidget(parent=main_window, f=Qt.Window)
    window.setWindowTitle('Rename object tool')
    main_layout = QVBoxLayout(window)

    # widget
    obj_name = QLineEdit()
    obj_name.setPlaceholderText('set new name...')
    button = QPushButton('Raname')
    button.clicked.connect(lambda: button_command(obj_name))

    main_layout.addWidget(obj_name)
    main_layout.addWidget(button)

    window.show()