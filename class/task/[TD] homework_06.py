# rename obj tool

# ver.Maya
from PySide2.QtWidgets import*
import maya.cmds as cmds

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

# main window    
window = QWidget()
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
import nuke

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

# main window  
window = QWidget()
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
import hou

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

# main window        
window = QWidget()
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