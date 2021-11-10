#main_window_nuke.py

import nuke
from PySide2 import QtWidgets

# Get main window for nuke
# For nuke version 11 and above.
def get_main_window():
	parent = None
	for widget in QtWidgets.QApplication.allWidgets():
		# For nuke11 and upper.
		if nuke.NUKE_VERSION_MAJOR >= 11:
			if type(widget) == type(QtWidgets.QMainWindow()):
				parent = widget
		return parent