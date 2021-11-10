# [ComboBox intro]

from PySide2.QtWidgets import*

def button_command(combo_box):
    print(combo_box.currentIndex())
    print(combo_box.currentText())
    print(combo_box.count())

# main window
window = QWidget()
window.setWindowTitle('Combobox test')
layout = QVBoxLayout(window)

# set combobox
combo_box = QComboBox()
combo_box.addItem('Apple')
combo_box.addItem('Orange')
combo_box.addItem('Purple')

# default selection
combo_box.setCurrentIndex(1)
# if default selection not exists, set Index0
# combo_box.setCurrentText('Papaya')

# set button
button = QPushButton('Get')
button.clicked.connect(lambda: button_command(combo_box))

# set layout
layout.addWidget(combo_box)
layout.addWidget(button)
window.setLayout(layout)
window.show()