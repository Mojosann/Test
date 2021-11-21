# [Custom widget (folw layout)]

from main_window_maya import get_main_window
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui
import json

def create_custom_button(name, type, date, thumbnail, description):

        widget_unit = QPushButton()
        layout_unit = QVBoxLayout(widget_unit)

        widget_unit.setFixedWidth(255)
        widget_unit.setFixedHeight(350)
        widget_unit.setToolTip(description)
        
        widget_mini = QWidget()
        layout_mini = QVBoxLayout(widget_mini)

        pic_widget = QLabel()
        image = QtGui.QPixmap(thumbnail)
        pic_widget.setPixmap(image)
        
        type_label = QLabel(type)
        name_label = QLabel(name)
        date_label = QLabel(date)

        type_label.setStyleSheet('color: #CF9E9E; font-size: 18px; font-weight: bold; font-family: calibri;')
        name_label.setStyleSheet('color: tan; font-size: 25px; font-weight: bold; font-family: calibri;')
        date_label.setStyleSheet('color: #ADADAD; font-style:italic;')
        
        type_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        name_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        date_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)

        layout_mini.addWidget(type_label)
        layout_mini.addWidget(name_label)

        layout_mini.addWidget(date_label)
        layout_unit.addWidget(pic_widget)
        layout_unit.addWidget(widget_mini)

        return widget_unit

class FlowLayout(QtWidgets.QLayout):

    def __init__(self, parent=None, margin=0, spacing=2):
        """
        Create a new FlowLayout instance.
        This layout will reorder the items automatically.
        @param parent (QWidget)
        @param margin (int)
        @param spacing (int)
        """
        super(FlowLayout, self).__init__(parent)
        # Set margin and spacing
        if parent is not None: self.setMargin(margin)
        self.setSpacing(spacing)

        self.itemList = []

    def __del__(self):
        """Delete all the items in this layout"""
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        """Add an item at the end of the layout.
        This is automatically called when you do addWidget()
        item (QWidgetItem)"""
        self.itemList.append(item)

    def count(self):
        """Get the number of items in the this layout
        @return (int)"""
        return len(self.itemList)

    def itemAt(self, index):
        """Get the item at the given index
        @param index (int)
        @return (QWidgetItem)"""
        if index >= 0 and index < len(self.itemList):
            return self.itemList[index]
        return None

    def takeAt(self, index):
        """Remove an item at the given index
        @param index (int)
        @return (None)"""
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)
        return None

    def insertWidget(self, index, widget):
        """Insert a widget at a given index
        @param index (int)
        @param widget (QWidget)"""
        item = QtGui.QWidgetItem(widget)
        self.itemList.insert(index, item)

    def expandingDirections(self):
        """This layout grows only in the horizontal dimension"""
        return QtCore.Qt.Orientations(QtCore.Qt.Horizontal)

    def hasHeightForWidth(self):
        """If this layout's preferred height depends on its width
        @return (boolean) Always True"""
        return True

    def heightForWidth(self, width):
        """Get the preferred height a layout item with the given width
        @param width (int)"""
        height = self.doLayout(QtCore.QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        """Set the geometry of this layout
        @param rect (QRect)"""
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        """Get the preferred size of this layout
        @return (QSize) The minimum size"""
        return self.minimumSize()

    def minimumSize(self):
        """Get the minimum size of this layout
        @return (QSize)"""
        # Calculate the size
        size = QtCore.QSize()
        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())
        # Add the margins
        size += QtCore.QSize(2 * self.margin(), 2 * self.margin())
        return size

    def doLayout(self, rect, testOnly):
        """Layout all the items
        @param rect (QRect) Rect where in the items have to be laid out
        @param testOnly (boolean) Do the actual layout"""
        x = rect.x()
        y = rect.y()
        lineHeight = 0

        for item in self.itemList:
            wid = item.widget()
            spaceX = self.spacing()
            spaceY = self.spacing()
            nextX = x + item.sizeHint().width() + spaceX
            if nextX - spaceX > rect.right() and lineHeight > 0:
                x = rect.x()
                y = y + lineHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                lineHeight = 0

            if not testOnly:
                item.setGeometry(QtCore.QRect(QtCore.QPoint(x, y), item.sizeHint()))

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())

        return y + lineHeight - rect.y()

window = QWidget()
layout = QVBoxLayout(window)

button_list_widget = QWidget()
button_list_layout = FlowLayout(parent=button_list_widget)

button_list = []
with open("D:/Documents/work/TWR/TD class/file_format/The Powerpuff Girls.json", 'r') as read_obj:
    content = read_obj.read()
    data = json.loads(content)

for item in data:
    button_widget = create_custom_button(item['name'], item['type'], item['update_time'], item['thumbnail'], item['description'])
    button_list_layout.addWidget(button_widget)
    button_list.append(button_widget)

scroll_widget = QScrollArea()
scroll_widget.setWidget(button_list_widget)
scroll_widget.setWidgetResizable(True)
layout.addWidget(scroll_widget)
window.show()