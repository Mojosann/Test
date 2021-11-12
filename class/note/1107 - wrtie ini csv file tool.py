# ver.ultimate

from main_window_houdini import get_main_window
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import os

shot_title_list = ['width', 'height', 'fps', 'maya version', 'renderer']
proj_title_list = ['Apocalypse Now', 'Dune', 'Joker', 'Free Guy']
dict_set = {}

def update_dict(new_dict):

	if new_dict != None:
		for key, value in new_dict.items():
			dict_set[key] = value

	return dict_set

def get_current_dict(proj_name, shot_info):

	data_dict = {}
	section = proj_name.currentText()

	if data_dict.get(section) == None:
		data_dict[section] = {}

	for item in shot_title_list:
		if data_dict[section].get(item) == None:
			data_dict[section][item] = None

	for value in range(len(shot_info)):
		data_dict[section][shot_title_list[value]] = str(shot_info[value].text())

	new = update_dict(data_dict)
	return new

def read_dict(proj_name, shot_info):

	for item in shot_info:
		item.clear()

	my_dict = update_dict(None)
	proj = proj_name.currentText()

	info_list = []
	for item in shot_title_list:
		info_list.append(my_dict[proj][item])

	for obj in range(len(info_list)):
		shot_info[obj].setText(info_list[obj])

def init_file(file_obj):

	with open(file_obj, 'w') as write_obj:
		
		write_obj.write(' ')

	return file_obj

def update_ini_file(file_obj, data_dict):
	
	with open(file_obj, 'w') as write_obj:
		for section in data_dict.keys():
			write_obj.write('[%s]\n' % section)
			for key, value in data_dict[section].items():
				write_obj.write('%s=%s\n' % (key, value))
			write_obj.write('\n')

	'''
	import configparser

	with open(file_obj, 'w') as write_obj:

		config = configparser.ConfigParser()

		for section in data_dict.keys():
			config.add_section(section)
			for key, value in data_dict[section].items():
				config.set(section, key, str(value))

		config.write(write_obj)
	'''

def update_csv_file(file_obj, data_dict):

	with open(file_obj, 'w') as write_obj:

		write_obj.write('name,')
		write_obj.write(','.join([info for info in shot_title_list]))

		for section in data_dict.keys():			
			write_obj.write('\n%s,' % (section))

			# sort
			value_list = []
			for item in range(len(shot_title_list)):
				value = data_dict[section][shot_title_list[item]]
				value_list.append(value)

			write_obj.write(','.join([value for value in value_list]))

def update_json_file(file_obj, data_dict):

	import json

	with open(file_obj, 'w') as write_obj:

		json_content = json.dumps(data_dict, indent=2, sort_keys=True)
		write_obj.write(json_content)

def update_xml_file(file_obj, data_dict):
	# cant newline ????
	import xml.etree.ElementTree as ET

	root = ET.Element('proj_info')
	
	for proj_name in data_dict.keys():

		proj = ET.Element(proj_name.replace(' ', '_'))
		info = ET.SubElement(proj, 'info')
			
		for key, value in data_dict[proj_name].items():
			info.set(key.replace(' ', '_'), str(value))

		root.append(proj)

	tree = ET.ElementTree(root)
	tree.write(file_obj)

def ini_button_command(proj_name, shot_info):

	my_dict = get_current_dict(proj_name, shot_info)
	file_path = 'D:/twr/project/log_file.ini'

	if os.path.isfile(file_path) == False:

		default = init_file(file_path)
		update_ini_file(file_path, my_dict)

	else:
		update_ini_file(file_path, my_dict)

def csv_button_command(proj_name, shot_info):

	my_dict = get_current_dict(proj_name, shot_info)
	file_path = 'D:/twr/project/log_file.csv'

	if os.path.isfile(file_path) == False:

		default = init_file(file_path)
		update_csv_file(file_path, my_dict)

	else:
		update_csv_file(file_path, my_dict)

def json_button_command(proj_name, shot_info):

	my_dict = get_current_dict(proj_name, shot_info)
	file_path = 'D:/twr/project/log_file.json'

	if os.path.isfile(file_path) == False:

		default = init_file(file_path)
		update_json_file(file_path, my_dict)

	else:
		update_json_file(file_path, my_dict)

def xml_button_command(proj_name, shot_info):

	my_dict = get_current_dict(proj_name, shot_info)
	file_path = 'D:/twr/project/log_file.xml'

	if os.path.isfile(file_path) == False:

		default = init_file(file_path)
		update_xml_file(file_path, my_dict)

	else:
		update_xml_file(file_path, my_dict)

def UI():

	main_window = get_main_window()

	window = QWidget()
	window.setParent(main_window)
	window.setWindowFlags(Qt.Window)
	window.setWindowTitle('Make shot info file tool')
	layout = QVBoxLayout(window)

	project_widget = QGroupBox('File info')
	project_layout = QHBoxLayout(project_widget)

	proj = QComboBox()
	for item in proj_title_list:
		proj.addItem(item)

	proj.activated.connect(lambda: read_dict(proj, shot_info_list))
	project_layout.addWidget(proj)
	
	shot_info_list = []
	for item in shot_title_list:
		shot_info = QLineEdit()
		shot_info.setPlaceholderText(item)
		shot_info_list.append(shot_info)
		project_layout.addWidget(shot_info)
	
	ini_button = QPushButton('Create INI file')
	csv_button = QPushButton('Create CSV file')
	json_button = QPushButton('Create JSON file')
	xml_button = QPushButton('Create XML file')

	ini_button.clicked.connect(lambda: ini_button_command(proj, shot_info_list))
	csv_button.clicked.connect(lambda: csv_button_command(proj, shot_info_list))
	json_button.clicked.connect(lambda: json_button_command(proj, shot_info_list))
	xml_button.clicked.connect(lambda: xml_button_command(proj, shot_info_list))

	layout.addWidget(project_widget)
	layout.addWidget(ini_button)
	layout.addWidget(csv_button)
	layout.addWidget(json_button)
	layout.addWidget(xml_button)
	
	window.show()