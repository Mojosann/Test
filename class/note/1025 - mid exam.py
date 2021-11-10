from PySide2.QtWidgets import *
from PySide2.QtCore import *
from functools import partial
import main_window_maya
import mid_exam_data

def get_seq_shot_data():
	my_dict = {}
	data_dict = mid_exam_data.get_mid_exam_data()
	for seq, shot_info in sorted(data_dict.items()):
		for shot, info in sorted(shot_info.items()):
			for title, gay in info.items():
				if seq not in my_dict:
					my_dict[seq] = {}
				if shot not in my_dict[seq]:
					my_dict[seq][shot] = {}
				if title == 'asset_dict':
					if title not in my_dict[seq][shot]:
						my_dict[seq][shot][title] = gay

	return my_dict

def get_asset_list(num):
	set_list = []
	char_list = []
	prop_list = []
	my_dict = get_seq_shot_data()
	for seq, shot_info in sorted(my_dict.items()):
		for shot, asset_dict in sorted(shot_info.items()):
			for name, asset_type in asset_dict.items():

				if asset_type != []:
					for type, final in asset_type.items():
						if type == 'CHAR':
							for item in final:
								if item not in char_list:
									char_list.append(item)

						if type == 'SET':
							for item in final:
								if item not in set_list:
									set_list.append(item)

						if type == 'PROP':
							for item in final:
								if item not in prop_list:
									prop_list.append(item)
				else:
					continue

	if num == 0:
		return char_list
	if num == 1:
		return prop_list
	if num == 2:
		return set_list

def sq_combo_command(sq_combo, sh_combo):

	sh_combo.clear()
	test_dict = get_seq_shot_data()
	sequence = sq_combo.currentText()
	for shot in sorted(test_dict[sequence]):
		sh_combo.addItem(shot)

def sh_combo_command(sq_combo, sh_combo, char_list, prop_list, set_list):

	my_dict = get_seq_shot_data()
	sequence = sq_combo.currentText()
	shot = sh_combo.currentText()

	if my_dict[sequence].get(shot) != None:
		if my_dict[sequence][shot].get('asset_dict') != None:
			
			for char_item in char_list:
				char_item.setChecked(False)
				
				asset_dict = my_dict[sequence][shot]['asset_dict']
				if asset_dict.get('CHAR') != None:
					if char_item.text() in asset_dict['CHAR']:
						char_item.setChecked(True)
				else:
					continue

			for prop_item in prop_list:
				prop_item.setChecked(False)
				
				asset_dict = my_dict[sequence][shot]['asset_dict']
				if asset_dict.get('PROP') != None:
					if prop_item.text() in asset_dict['PROP']:
						prop_item.setChecked(True)
				else:
					continue

			for set_item in set_list:
				set_item.setChecked(False)
				
				asset_dict = my_dict[sequence][shot]['asset_dict']
				if asset_dict.get('SET') != None:
					if set_item.text() in asset_dict['SET']:
						set_item.setChecked(True)
				else:
					continue

def main():
	main_window = main_window_maya.get_main_window()

	window = QWidget()
	window.setParent(main_window)
	window.setWindowFlags(Qt.Window)
	window.setWindowTitle('Get seq/shot info test')
	layout = QVBoxLayout(window)

	# set combobox
	select_widget = QGroupBox('Select')
	select_layout = QHBoxLayout(select_widget)

	test_dict = get_seq_shot_data()
	seq_combo_box = QComboBox()
	for seq in sorted(test_dict.keys()):
		seq_combo_box.addItem(seq)

	shot_combo_box = QComboBox()
	seq_combo_box.activated.connect(lambda: sq_combo_command(seq_combo_box, shot_combo_box))
	shot_combo_box.activated.connect(lambda: sh_combo_command(seq_combo_box, shot_combo_box, char_checkbox, prop_checkbox, set_checkbox))

	select_layout.addWidget(seq_combo_box)
	select_layout.addWidget(shot_combo_box)

	
	# set group checkbox
	asset_widget = QGroupBox('Asset')
	asset_layout = QHBoxLayout(asset_widget)

	char_widgets = QGroupBox('Char')
	char_layout = QVBoxLayout(char_widgets)
	char_list = get_asset_list(0)
	char_checkbox = []
	for item in sorted(char_list):
		char_item = QCheckBox(item)
		char_checkbox.append(char_item)
		char_layout.addWidget(char_item)

	prop_widgets = QGroupBox('Prop')
	prop_layout = QVBoxLayout(prop_widgets)
	prop_list = get_asset_list(1)
	prop_checkbox = []
	for item in sorted(prop_list):
		prop_item = QCheckBox(item)
		prop_checkbox.append(prop_item)
		prop_layout.addWidget(prop_item)

	set_widgets = QGroupBox('Prop')
	set_layout = QVBoxLayout(set_widgets)
	set_list = get_asset_list(2)
	set_checkbox = []
	for item in sorted(set_list):
		set_item = QCheckBox(item)
		set_checkbox.append(set_item)
		set_layout.addWidget(set_item)

	asset_layout.addWidget(char_widgets)
	asset_layout.addWidget(set_widgets)
	asset_layout.addWidget(prop_widgets)

	layout.addWidget(select_widget)
	layout.addWidget(asset_widget)
	window.setLayout(layout)
	window.show()