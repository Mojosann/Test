# main_window_houdini.py

import hou
#Get main window for houdini.
def get_main_window():
    return hou.ui.mainQtWindow()