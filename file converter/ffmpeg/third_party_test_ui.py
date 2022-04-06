try:
	from PySide2.QtWidgets import *
	from PySide2 import QtGui, QtCore

except:
	from PySide.QtWidgets import *
	from PySide import QtGui, QtCore

from pprint import pprint
import os, re

class ThirdPartyTestUI(QWidget):

	export_button_signal = QtCore.Signal(dict)

	def __init__(self, main_window=None):
		super(ThirdPartyTestUI, self).__init__(parent=main_window)

		dir_name = os.path.dirname(__file__)
		my_name  = os.path.splitext(os.path.basename(__file__))[0]
		css_path = os.path.join(dir_name, my_name) + '.css'

		if os.path.isfile(css_path) == True:
			with open(css_path, 'r') as file:
				self.css_style = file.read()

		self.set_dict = {}
		self.set_dict['source_type'] = ['exr', 'mov']
		self.set_dict['source_file'] = 'Source File'
		self.set_dict['target_file'] = 'Target File'
		self.set_dict['format_type'] = 'jpg'
		self.set_dict['frame_range'] = 'Set Start Frame'
		self.set_dict['export']   	 = 'OK'

		self.setWindowTitle('File Converter Tool')
		# self.setMinimumHeight(360)
		self.setMinimumWidth(600)
		self.stand_icon = self.style().standardIcon(QStyle.SP_DialogOpenButton)
		layout = QVBoxLayout(self)

		convert_type = self.set_convert_type_widget()
		source_grp_setting = self.set_source_file_widget()
		export_jpg_setting = self.set_export_jpg_widget()
		target_grp_setting = self.set_target_file_widget()		

		layout.addWidget(convert_type)
		layout.addWidget(source_grp_setting)
		layout.addWidget(target_grp_setting)
		layout.addWidget(export_jpg_setting)
		layout.addStretch()

		self.update_stylesheet()
		
	def set_convert_type_widget(self):

		mini_widget = QWidget()
		mini_layout = QHBoxLayout(mini_widget)
		mini_layout.setContentsMargins(5, 10, 5, 0)
		mini_layout.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

		source_type = QLabel('Source Type')
		source_type.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
		source_type.setFixedWidth(95)
		mini_layout.addWidget(source_type)

		self.exr_src = QPushButton(self.set_dict['source_type'][0])
		self.mov_src = QPushButton(self.set_dict['source_type'][1])
		self.exr_src.setStyleSheet('background-color: black;')
		self.mov_src.setStyleSheet('background-color: black;')
		self.exr_hint = QLabel(u'請提供 EXR 資料夾路徑！')
		self.exr_hint.setVisible(False)
		reset_btn = QPushButton('Reset')

		self.exr_src.clicked.connect(lambda: self.change_browser_type(self.exr_src))
		self.mov_src.clicked.connect(lambda: self.change_browser_type(self.mov_src))
		reset_btn.clicked.connect(lambda: self.reset_src_type())

		for item in [self.exr_src, self.mov_src]:
			item.setFixedWidth(50)
			mini_layout.addWidget(item)
		mini_layout.addWidget(self.exr_hint)
		mini_layout.addStretch()
		mini_layout.addWidget(reset_btn)
		return mini_widget
	
	def reset_src_type(self):

		self.exr_src.setVisible(True)
		self.mov_src.setVisible(True)
		self.exr_hint.setVisible(False)
		self.source.clear()
		# self.target.clear()

	def change_browser_type(self, src_type):
		
		if src_type.text() == 'exr':
			self.exr_src.setVisible(True)
			self.mov_src.setVisible(False)
			self.exr_hint.setVisible(True)

		if src_type.text() == 'mov':
			self.mov_src.setVisible(True)
			self.exr_src.setVisible(False)
			self.exr_hint.setVisible(False)
	
	def get_source_file(self):

		if self.exr_src.isVisible() and self.mov_src.isHidden():
			title = 'Choose source folder'
			source_path = QFileDialog.getExistingDirectory(None, title, self.source.text())		
			self.source.setText(source_path)

		if self.mov_src.isVisible() and self.exr_src.isHidden():
			title = 'Choose source file'
			filters = 'video (*.mov)'
			get_path, filters = QFileDialog.getOpenFileName(None, title, self.source.text(), filters)
			self.source.setText(str(get_path))

		if self.exr_src.isVisible() and self.mov_src.isVisible():
			self.error_message([u'請先選擇source type！'])

	def save_export_file(self):

		title   = 'Save as ...'
		filters = 'image (*.jpg *.png) ;; video (*.mov)'
		get_path, filters = QFileDialog.getSaveFileName(None, title, self.target.text(), filters)
		self.target.setText(get_path)
	
	def controll_frame_range_enabled(self):

		if self.set_frame_range.isChecked():
			self.range.setEnabled(True)
		else:
			self.range.setEnabled(False)
	
	def set_browser_button(self):

		browse = QPushButton()
		browse.setFixedHeight(30)
		browse.setIcon(self.stand_icon)
		
		return browse

	def set_source_file_widget(self):
		
		source_widget = QWidget()
		source_layout = QHBoxLayout(source_widget)
		source_layout.setContentsMargins(5, 2, 5, 0)

		source_label = QLabel(self.set_dict['source_file'])
		source_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
		source_label.setFixedWidth(95)
		self.source = QLineEdit()
		self.source.setPlaceholderText("Z:/dev/sq1401_sh0110.mov")
		
		source_browse = self.set_browser_button()
		source_browse.clicked.connect(lambda: self.get_source_file())
		
		for item in [source_label, self.source, source_browse]:
			source_layout.addWidget(item)

		return source_widget

	def set_target_file_widget(self):

		target_widget = QWidget()
		target_layout = QHBoxLayout(target_widget)
		target_layout.setContentsMargins(5, 0, 5, 0)

		target_label = QLabel(self.set_dict['target_file'])
		target_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
		target_label.setFixedWidth(95)

		self.target = QLineEdit()
		self.target.setPlaceholderText("Z:/dev/test_%04d.jpg")

		target_browse = self.set_browser_button()
		target_browse.clicked.connect(lambda: self.save_export_file())
		
		for item in [target_label, self.target, target_browse]:
			target_layout.addWidget(item)
		return target_widget

	def set_export_jpg_widget(self):

		mini_widget = QWidget()
		mini_layout = QHBoxLayout(mini_widget)
		mini_layout.setContentsMargins(5, 0, 5, 10)

		empty_label = QLabel()
		empty_label.setFixedWidth(95)

		self.set_frame_range = QCheckBox(self.set_dict['frame_range'])
		self.set_frame_range.clicked.connect(self.controll_frame_range_enabled)
		
		self.range = QLineEdit()
		self.range.setEnabled(False)
		self.range.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.range.setFixedWidth(150)
		self.range.setPlaceholderText('1001')

		export_button = self.set_button_widget()
		export_button.setFixedWidth(150)

		for item in [empty_label, self.set_frame_range, self.range]:
			mini_layout.addWidget(item)		
		mini_layout.addStretch()
		mini_layout.addWidget(export_button)
		return mini_widget	

	def set_button_widget(self):

		button = QPushButton(self.set_dict['export'])
		button.setFixedHeight(35)
		button.clicked.connect(lambda: self.get_dict())

		return button

	def update_stylesheet(self):

		self.setStyleSheet(self.css_style)

	def error_message(self, msg_list=[]):

		msg = QMessageBox(self)
		msg.setWindowTitle(u'敲鑼打鼓！')
		text = '\n'.join(item for item in msg_list) + '     '
		msg.setText(text)
		msg.setStyleSheet(self.css_style)
		msg.exec_()

	def output_query_dict(self, query_dict, msg):
		
		self.export_button_signal.emit(query_dict)
		# pprint(query_dict)
		msg.close()

	def show_checking_msgbox(self, check_list, query_dict): 
		
		msg = QDialog()
		msg.setWindowTitle(u'敲鑼打鼓！')
		msg.setMinimumWidth(650)		
		
		mini_layout = QVBoxLayout(msg)
		mini_layout.setAlignment(QtCore.Qt.AlignVCenter)
		mini_layout.setContentsMargins(15, 15, 15, 15)
		
		welcome = QLabel()
		welcome.setText('\n'.join(check_list))
			
		btn_widget = QWidget()
		btn_layout = QHBoxLayout(btn_widget)
		btn_layout.setContentsMargins(0, 5, 0, 0)
		button = QPushButton('Export', msg)
		report = QPushButton(u'我想再安靜優雅地修改一下', msg)
		button.clicked.connect(lambda: self.output_query_dict(query_dict, msg))
		report.clicked.connect(lambda: msg.close())

		btn_layout.addWidget(button)
		btn_layout.addWidget(report)
		mini_layout.addWidget(welcome)
		mini_layout.addWidget(btn_widget)
		msg.setStyleSheet(self.css_style)
		msg.exec_()

	def get_dict(self):

		msg_list   = []
		check_list = [] 
		query_dict = {}
		query_dict['source_file'] = os.path.normpath(self.source.text()).replace('\\', '/')
		query_dict['target_file'] = os.path.normpath(self.target.text()).replace('\\', '/')
		query_dict['set_frame_range'] = self.range.isEnabled()
		query_dict['frame_range'] = self.range.text()
		
		##### exr source
		if os.path.isdir(query_dict['source_file']):
			if len(os.listdir(query_dict['source_file'])):
				file_name, ext = os.path.splitext(os.listdir(query_dict['source_file'])[0])
				first = os.path.splitext(os.listdir(query_dict['source_file'])[0])[0][-4:]
				last  = os.path.splitext(os.listdir(query_dict['source_file'])[-1])[0][-4:]
				if ext != '.exr':
					msg_list.append(u'請輸入來源檔案！')
				else:
					preview_name = query_dict['source_file'] + '/' + file_name[:-5] + '_++++' + ext
					four_ordinator = query_dict['source_file'] + '/' + file_name[:-5] + '_%04d' + ext
					check_list.append(u'請確認以下資訊：')
					check_list.append(u'來源檔名格式 | %s' % preview_name)
					check_list.append(u'來源圖檔序號 | %s-%s' % (first, last))
					query_dict['source_file'] = four_ordinator
			else:
				msg_list.append(u'這是一個空資料夾！')
		##### mov source
		elif os.path.isfile(query_dict['source_file']):					
			file_name, ext = os.path.splitext(query_dict['source_file'])
			if ext != '.mov':
				msg_list.append(u'請指定 mov 類型的檔案！')
			else:
				check_list.append(u'請確認以下資訊：')
				check_list.append(u'來源檔名 | %s' % query_dict['source_file'])
		else:
			msg_list.append(u'檔案路徑不存在！')

		##### check target file
		file = os.path.splitext(query_dict['target_file'])[0]
		ext  = os.path.splitext(query_dict['target_file'])[1]
		query_dict['target_ext'] = ext

		if os.path.isfile(query_dict['target_file']):
			if ext == '.mov':				
				check_list.append(u'輸出檔名格式 | %s' % query_dict['target_file'])
			elif ext == '.jpg' or ext == '.png':
				target_folder = os.path.dirname(query_dict['target_file'])
				os.listdir(target_folder)

				first = os.path.basename(os.listdir(target_folder)[0]).split('.')[0][-4:]
				last = os.path.basename(os.listdir(target_folder)[-1]).split('.')[0][-4:]

				query_dict['target_file'] = file[:-5] + '_%04d' + ext

				file_name = file[:-5] + '_++++' + ext
				check_list.append(u'輸出檔名格式 | %s' % file_name)
				check_list.append(u'輸出圖檔序號 | %s-%s' % (first, last))
				if query_dict['set_frame_range']:
					msg_list.append(u'請清除 target file 上的序號才能重新設定frame range！')

		else:
			if ext == '.mov':
				check_list.append(u'輸出檔名 | %s' % query_dict['target_file'])
			elif ext == '.jpg' or ext == '.png':
				if query_dict['set_frame_range']:
					if len(query_dict['frame_range']):
						file_name = file + '_++++' + ext
						check_list.append(u'輸出檔名 | %s' % file_name)
						re_list = re.findall('\d\d\d\d-\d\d\d\d', query_dict['frame_range'])
						if re_list == []:
							msg_list.append(u"請將四位起始格數以 '-' 號隔開！")
						check_list.append(u'輸出圖檔起始序號 | %s' % query_dict['frame_range'])
					else:
						msg_list.append(u'要輸入 frame range！')
				else:
					msg_list.append(u'請勾上 set frame range！')
			else:
				msg_list.append(u'target 檔名不完整！')

		if msg_list != []:
			self.error_message(msg_list)
		else:				
			self.show_checking_msgbox(check_list, query_dict)

def main():

	return ThirdPartyTestUI()