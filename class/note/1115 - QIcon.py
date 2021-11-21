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