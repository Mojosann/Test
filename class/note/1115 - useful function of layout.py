# [useful function of layout]

# left, top, right, bottom, default為11
layout.setCententsMargins(5, 5, 5, 5)
layout.getCententsMargins() # 取得margin
layout.contentsMargins() # 取得margin object

# 設定layout裡的元件與元件的間隔距離 default為-1(10)
layout.setSpacing(5)
layout.spacing() # 取得目前layout的spacing值

# make a custom widget
thumbnail, name, type, description, update_time
# def create_custom_button(name, type):

# 取得layout的總數
layout.count()

# [Practice]
# 取得指定index的item必須要使用.widget()才能取得內容
for i in range(layout.count()):
	item = layout.itemAt(index) # layout item
	widget = item.widget() # real widget, ex:QLabel, QPushButton

# 在layout的最後加上一個stretch(延伸物件)
# 讓widget固定在上方
layout.addStretch()

window = QWidget()
layout = QVBoxLayout(window)

btn_01 = QPushButton('btn_01')
btn_02 = QPushButton('btn_02')
layout.addWidget(btn_01)
layout.addStretch()
layout.addWidget(btn_02)
window.show()