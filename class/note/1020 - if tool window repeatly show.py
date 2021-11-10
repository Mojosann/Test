# [Prevent tool window show again and again]

from PySide2 import QtWidgets
# 取得所有widget判斷特定屬性後 將其刪除

widget_list = QtWidgets.QApplication.allWidgets()

for widget in widget_list:
    print(widget)

    if widget.windowTitle() == 'Test tool':
        # delete widget.
        widget.deleteLater()

# 設定object name 為標記
# object name 自行命名
tool = QtWidgets.QWidget()
# tool.setObjectName('test_widget_name')
tool.setWindowTitle('Test tool')
tool.show()