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

				fps_not_25_list = []
				if title == 'fps':
					if title not in my_dict[seq][shot]:
						my_dict[seq][shot][title] = gay
						if my_dict[seq][shot][title] != 25:
							fps_not_25_list.append(my_dict[seq].get(shot))
				if title == 'start_frame':
					if title not in my_dict[seq][shot]:
						my_dict[seq][shot][title] = gay
				end_list = []
				if title == 'end_frame':
					if title not in my_dict[seq][shot]:
						my_dict[seq][shot][title] = gay
						if my_dict[seq][shot]['end_frame'] > my_dict[seq][shot]['start_frame']:
							end_list.append(my_dict[seq][shot])
				if title == 'width':
					if title not in my_dict[seq][shot]:
						my_dict[seq][shot][title] = gay
				if title == 'height':
					if title not in my_dict[seq][shot]:
						my_dict[seq][shot][title] = gay

				if title == 'task_list':
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
			for name, asset_type_info in asset_dict.items():
				#print(asset_type_info)
				
				if name == 'asset_dict':
					for asset_type, final in asset_type_info.items():
						if asset_type == 'CHAR':
							for item in final:
								if item not in char_list:
									char_list.append(item)

						if asset_type == 'SET':
							for item in final:
								if item not in set_list:
									set_list.append(item)

						if asset_type == 'PROP':
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

def sh_combo_command(sq_combo, sh_combo, char_list, prop_list, set_list, task, shot_grp):

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

		if my_dict[sequence][shot].get('task_list') != None:

			for check_box in task:
				check_box.setChecked(False)
				check = check_box.text()
				if check in sorted(my_dict[sequence][shot]['task_list']):
					check_box.setChecked(True)

		if my_dict[sequence][shot].get('fps') != None:
			shot_grp[0].setText(str(my_dict[sequence][shot]['fps']))

		if my_dict[sequence][shot].get('start_frame') != None:
			shot_grp[1].setText(str(my_dict[sequence][shot]['start_frame']))

		if my_dict[sequence][shot].get('end_frame') != None:
			shot_grp[2].setText(str(my_dict[sequence][shot]['end_frame']))

		if my_dict[sequence][shot].get('width') != None:
			shot_grp[3].setText(str(my_dict[sequence][shot]['width']))

		if my_dict[sequence][shot].get('height') != None:
			shot_grp[4].setText(str(my_dict[sequence][shot]['height']))

			
def UI():
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
	shot_combo_box.activated.connect(lambda: sh_combo_command(seq_combo_box, shot_combo_box, char_checkbox, prop_checkbox, set_checkbox, task_list, shot_list))

	select_layout.addWidget(seq_combo_box)
	select_layout.addWidget(shot_combo_box)

	# set line edit
	line_widget = QGroupBox('Shot Info')
	line_layout = QHBoxLayout(line_widget)

	shot_list = []
	for shot_info in ['fps', 'start_frame', 'end_frame', 'width', 'height']:
		shot_box = QLineEdit(shot_info)
		shot_box.setPlaceholderText(shot_info)
		line_layout.addWidget(shot_box)
		shot_list.append(shot_box)

	# set check box
	task_widget = QGroupBox('Task Info')
	task_layout = QHBoxLayout(task_widget)
	task_list = []
	for task_info in ['layout', 'animation', 'lighting', 'fx', 'comp']:
		task_box = QCheckBox(task_info)
		task_layout.addWidget(task_box)
		task_list.append(task_box)

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
	layout.addWidget(line_widget)
	layout.addWidget(task_widget)
	layout.addWidget(asset_widget)
	window.setLayout(layout)
	window.show()