# 1015 - get file (combo_box).py
# 已改寫成UI()版本: 1018 - combobox UI complete
# [Get image file tool (ComboBox)]

from main_window_houdini import get_main_window
from PySide2.QtWidgets import*
from PySide2.QtCore import*
import os 

def get_image_file(input_path, ext, result):

    path_data = os.listdir(input_path)

    for image_file in path_data:
        if ext in image_file:
            result.append(image_file) 

def button_command(file_path, combo_box, result):

    input_path = file_path.text()
    ext_name = combo_box.currentText()

    # use button to call function
    get_image_file(input_path, ext_name, result)

def UI():

    main_window = get_main_window()

    window = QWidget()
    window.setParent(main_window)
    window.setWindowFlags(QtCore.Qt.Window)
    window.setWindowTitle('Get image file tool')
    layout = QVBoxLayout(window)

    path = QGroupBox('Path info')   
    path_layout = QVBoxLayout(path)

    file_path = QLineEdit()
    #u'Chinese words…'(only maya)
    file_path.setPlaceholderText('path…')

    #set combobox
    combo_box = QComboBox()
    for ext_name in ['png', 'exr', 'jpg']:
        combo_box.addItem(ext_name)

    #default set
    combo_box.setCurrentIndex(1)

    result = QTextEdit()

    #set button
    button = QPushButton('Get')
    button.clicked.connect(lambda: button_command(file_path, combo_box, result))

    #set layout
    path_layout.addWidget(file_path)
    path_layout.addWidget(combo_box)
    path_layout.addWidget(button)
    layout.addWidget(path)
    layout.addWidget(result)
    window.show()