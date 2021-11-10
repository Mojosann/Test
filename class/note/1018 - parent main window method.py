# [Parent main window method]
# Maya / Nuke / Houdini friendly!

from PySide2 import QtWidgets, QtCore
from main_window_maya import get_main_window
# from main_window_houdini import get_main_window
# from main_window_nuke import get_main_window

# only run main() will close cus find no parent
# solution: give 3D software's main window
# term: garbage collection

def main():
    main_window = get_main_window()

    # method(1)
    tool = QtWidgets.QWidget(parent=main_window, f=QtCore.Qt.Window)
    tool = QtWidgets,QWidget(main_window, QtCore.Qt.Window)

    # method(2)
    tool = QtWidgets.QWidget(main_window)
    tool.setWindowFlags(QtCore.Qt.Window)

    # method(3)
    tool = QtWidgets.QWidget()
    tool.setParent(main_window) # give main window to be parent
    tool.setWindowFlags(QtCore.Qt.Window) # open tool as new window

    tool.show()