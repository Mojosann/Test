#main_window_maya.py

import maya.OpenMayaUI
import shiboken2
from PySide2 import QtWidgets

# Get main window for maya.
def get_main_window():
    main_window_ptr = maya.OpenMayaUI.MQtUtil.mainWindow()
    parent = shiboken2.wrapInstance(long(main_window_ptr), QtWidgets.QWidget)
    return parent