# [QPixmap]

from PySide2 import QtWidgets, QtGui

# 經常用在UI上顯示圖片
label = QtWidgets.QLabel()
pixmap = QtGui.QPixmap("(image_file)")
pixmap = pixmap.scaled(80, 50, QtCore.Qt.IgnoreAspectRatio)
# 另外還有三種[IgnoreAspectRatio, KeepAspectRatio, KeepAspectRatioByExpanding]

label.setPixmap(pixmap)

# QtCore.Qt.SmoothTransformation # 因為圖片被拉扯後有鋸齒可以調edge


# [Practice]
from PySide2 import QtWidgets, QtGui, QtCore

window = QtWidgets.QWidget()
layout = QtWidgets.QHBoxLayout(window)

label = QLabel() # 加字是無意義的
label_ = QLabel('asas')
label_.setParenet(window) # 然後要強制設定位置 要算才有辦法放在正中間
pixmap = QPixmap("‪D:/Documents/work/TWR/TD class/homework/hw008_thumbnail/Blossom.png")
# 給路徑一定要用"" not ''
pixmap = pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio)
