# [Get sequence & shot (nested combobox)]

from main_window_houdini import get_main_window
from PySide2.QtWidgets import *
from PySide2 import QtCore
import os

def combo_command(sq_combo, sh_combo):
	sh_combo.clear()
		
	for shot in os.listdir('D://twr//' + sq_combo.currentText()):
		sh_combo.addItem(shot)

def button_command(sq_combo, sh_combo):
	print(sq_combo.currentText())
	print(sh_combo.currentText())


def UI():

	main_window = get_main_window()

	window = QWidget()
	window.setParent(main_window)
	window.setWindowFlags(QtCore.Qt.Window)
	window.setWindowTitle('Get sequence/shot test')
	layout = QHBoxLayout(window)

	# set combobox
	seq_combo_box = QComboBox()
	seq_list = os.listdir('D://twr')
	for seq in seq_list:
		seq_combo_box.addItem(seq)
		#shot_list = os.listdir('Z://twr//' + str(seq))
		#print(shot_list)

	shot_combo_box = QComboBox()
		
	for shot in os.listdir('D://twr//' + seq_combo_box.currentText()):
		shot_combo_box.addItem(shot)
	seq_combo_box.activated.connect(lambda: combo_command(seq_combo_box, shot_combo_box))

	#set button
	button = QPushButton('Get')
	button.clicked.connect(lambda: button_command(seq_combo_box, shot_combo_box))

	#set layout
	layout.addWidget(seq_combo_box)
	layout.addWidget(shot_combo_box)
	layout.addWidget(button)

	window.setLayout(layout)
	window.show()