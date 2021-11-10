# [Get missing file and file list tool]
# different file name naming rules may cause get_missing_file_list() error.

from main_window_houdini import get_main_window
from PySide2.QtWidgets import*
from PySide2.QtCore import*
import os

def get_image_file(input_path, ext):

    image_list = []
    path_data = os.listdir(input_path)

    for image_file in path_data:
        if ext in image_file:
            image_list.append(image_file)

    return image_list

def get_missing_file_list(input_list):

    missing_list = []
    num_list = []

    for item in input_list:
        num_list.append(int(item.split('.')[1]))

    num_list.sort()

    for num in range(num_list[0], num_list[-1]+1):
        if num not in num_list:
            #print(num, 'missing!')
            missing_list.append(str(num))

    return missing_list 

def button_command(file_path, combo_box, text_edit):

    input_path = file_path.text()
    ext_name = combo_box.currentText()

    # use button to call function
    image_list = get_image_file(input_path, ext_name)
    missing_data = get_missing_file_list(image_list)

    for image in image_list:
        text_edit.append(str(image))
        #text_edit.setPlainText(image)

    #print(text_edit.toPlainText())
    for missing in missing_data:
        text_edit.append('%s missing!' % missing)

def UI():

    main_window = get_main_window()

    window = QWidget()
    window.setParent(main_window) # give main_window to be parent
    window.setWindowFlags(QtCore.Qt.Window) #open tool as new window
    window.setWindowTitle('Get missing file and file list tool')
    layout = QVBoxLayout(window)

    path = QGroupBox('Path info')   
    path_layout = QVBoxLayout(path)

    file_path = QLineEdit()
    file_path.setPlaceholderText('path…')

    #set combobox
    combo_box = QComboBox()
    for ext_name in ['png', 'exr', 'jpg']:
        combo_box.addItem(ext_name)

    #default combobox set
    combo_box.setCurrentIndex(1)

    #set button
    button = QPushButton('Get missing file / file list')
    button.clicked.connect(lambda: button_command(file_path, combo_box, text_edit))

    text_edit = QTextEdit()

    #set layout
    path_layout.addWidget(file_path)
    path_layout.addWidget(combo_box)
    path_layout.addWidget(button)
    layout.addWidget(path)
    layout.addWidget(text_edit)
    window.show()