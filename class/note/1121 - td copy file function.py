# [Copy file function]
# function can back up file automatically
# when target file exists, will back up file to ./old/'file_name'
# when backup file exists, will rename 'file_name(1)'
# ex: aaa.txt, aaa(1).txt, aaa(2).txt...

from PySide2 import QtWidgets, QtGui, QtCore
import os, sys, shutil

def td_copy_file(source_file, target_file, log_data):
		
	if os.path.isfile(source_file) != True:
		log_data.append('file not exist!')
	
	# check target path exist
	target_path = os.path.dirname(target_file)
	if os.path.isdir(target_path) != True:
		os.mkdir(target_path)

	if os.path.isfile(target_file) != True:
		shutil.copyfile(source_file, target_file)
		log_data.append('back up complete!')

	else:		
		old_path = os.path.dirname(target_file) + '/old'
		file_name = os.path.basename(target_file)
		backup_file = '%s/%s' % (old_path, file_name)

		if os.path.isdir(old_path) != True:
			os.mkdir(old_path)
			shutil.copyfile(source_file, backup_file)
			log_data.append('back up %s complete!' % backup_file)

		else:
			name, ext = os.path.splitext(file_name)
			# avoid count other file in folder
			name_list = []
			for item in os.listdir(old_path):
				if name in item:
					name_list.append(item)

			backup_len = len(name_list)
			backup_file_index = '%s/%s(%s)%s' % (old_path, name, backup_len, ext)
			
			if os.path.isfile(backup_file) == True:
					shutil.copyfile(source_file, backup_file_index)
					log_data.append('back up %s(%s)%s complete!' % (name, backup_len, ext))

def get_a_file(show):
	title = 'open a file' # 視窗標題
	init_path = 'D:/Documents/work/TWR/TD class' # 起始的路徑
	filters = 'image file (*.jpg, *.png)' # all:*.* # 檔案的篩選條件
	get_file = QtWidgets.QFileDialog.getOpenFileName(None, title, init_path, filters)
	show.setText(str(get_file[0]))

def get_a_path(show, source):
	source = source.split('/')[-1]
	title = 'assign path' # 視窗標題
	init_path = 'D:/Documents/work/TWR/TD class' # 起始的路徑
	get_file = QtWidgets.QFileDialog.getExistingDirectory(None, title, init_path)
	show.setText('%s/%s' % (get_file, source))

def UI():

	main_window = QtWidgets.QApplication(sys.argv)
	window = QtWidgets.QWidget()
	window.setWindowTitle('Copy file tool')
	icon = QtGui.QIcon("D:/Documents/work/TWR/TD class/module/icon/6716_1521128123_fest.jpg")
	window.setWindowIcon(icon)
	layout = QtWidgets.QVBoxLayout(window)

	source_widget = QtWidgets.QWidget()
	source_layout = QtWidgets.QHBoxLayout(source_widget)
	label = QtWidgets.QLabel('Source Path ')
	label.setStyleSheet('color: black; font-size: 15px; font-weight: bold; font-family: calibri;')
	line = QtWidgets.QLineEdit()
	line.setStyleSheet('color: black; font-size: 15px; font-weight: bold; font-family: calibri;')

	line.setFixedWidth(550)

	target_widget = QtWidgets.QWidget()
	target_layout = QtWidgets.QHBoxLayout(target_widget)
	tlabel = QtWidgets.QLabel('Target Path ')
	tlabel.setStyleSheet('color: black; font-size: 15px; font-weight: bold; font-family: calibri;')
	tline = QtWidgets.QLineEdit()
	tline.setStyleSheet('color: black; font-size: 15px; font-weight: bold; font-family: calibri;')
	tline.setFixedWidth(550)

	browse_button = QtWidgets.QPushButton('open')
	stand_icon = browse_button.style().standardIcon(QtWidgets.QStyle.SP_DialogOpenButton)
	browse_button.setIcon(stand_icon)
	browse_button.clicked.connect(lambda:get_a_file(line))
	browse_button.setStyleSheet('color: #996400; font-size: 15px; font-weight: bold; font-family: calibri;')

	dir_button = QtWidgets.QPushButton('assign')
	dir_icon = browse_button.style().standardIcon(QtWidgets.QStyle.SP_DirHomeIcon)
	dir_button.setIcon(dir_icon)
	dir_button.clicked.connect(lambda:get_a_path(tline, line.text()))
	dir_button.setStyleSheet('color: #008080; font-size: 15px; font-weight: bold; font-family: calibri;')

	copy_button = QtWidgets.QPushButton('copy source to target !')
	copy_icon = copy_button.style().standardIcon(QtWidgets.QStyle.SP_FileIcon)
	copy_button.setIcon(copy_icon)
	copy_button.clicked.connect(lambda:td_copy_file(line.text(), tline.text(), log_data))
	copy_button.setStyleSheet('color: black; font-size: 15px; font-weight: bold; font-family: calibri;')

	log_data = QtWidgets.QTextEdit()
	log_data.setStyleSheet('color: black; font-size: 15px; font-weight: bold; font-family: calibri;')

	source_layout.addWidget(label)
	source_layout.addWidget(line)
	source_layout.addWidget(browse_button)
	target_layout.addWidget(tlabel)
	target_layout.addWidget(tline)
	target_layout.addWidget(dir_button)

	layout.addWidget(source_widget)
	layout.addWidget(target_widget)
	layout.addWidget(copy_button)
	layout.addWidget(log_data)
	window.show()
	
	main_window.exec_()

if __name__ == '__main__':
	#print(td_copy_file(sys.argv[1], sys.argv[2]))
	UI()
	sys.exit()