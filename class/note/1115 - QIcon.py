# [QIcon]

# 多用於button windowtitle也可以放icon
from PySide2 import QtWidgets, QtGui, QtCore

# 將圖片嵌在PushButton中使用
button = QPushButton()
stand_icon = button.style().standardIcon(QStyle.SP_TrashIcon)
button.setIcon(stand_icon)
button.setIconSize(QtCore.QSize(16, 16)) #16, 32, 48, 128, 256


# [Practice]
button = QPushButton('Test icon') # 不想要放字就把字拿掉會只剩下圖
icon = QIcon('‪D:/Documents/work/TWR/TD class/homework/hw008_thumbnail/Blossom.png')
button.setIcon(icon)

layout.setPixmap(pixmap)
layout.addWidget(label)
layout.addWidget(button)


# [解決houdini中無法show出icon的問題]
from PySide2 import QtWidgets, QtGui, QtCore
import hou

main_win = hou.ui.mainQtWindow()
# 因為button還沒被實體化所以setParent到main window
button = QtWidgets.QPushButton('click')
stand_icon = main_win.style().standardIcon(QtWidgets.QStyle.SP_DialogOpenButton)
button.setIcon(stand_icon)
button.setIconSize(QtCore.QSize(16, 16))
button.show()

# 0223 - 當script不限於在houdini內使用的時候
# icon可以直接parent window
# 然後window再去parent別的main window (由其他module去加入main_window的fiunction)