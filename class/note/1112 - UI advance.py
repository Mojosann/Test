# 取得目前widget是否enable
widget.isEnabled()

# 設定目前widget的enable
# toolset維護時將一些工具enable關掉
# 閱讀條款後解鎖'下一步'的功能
widget.setEnabled(True) # (True/False)

# 取得目前widget是否可以被看見
widget.isHidden()

# 設定目前widget的visible
widget.setVisible(True) # (True/False)

# 視窗炸彈流程：
# 一直按後會出現新視窗 視窗內content會一直變換

# 設定widget部分的外觀資訊
# 直接使用css語法 但未完全支援
# widget.setStyleSheet(css_content)
# 可以先打好css_content = '(css語法)' 然後丟進setStyleSheet()

color: #FF0000
background-color:

font-size: 20-40px;
font-weight: bold;
font-family: calibri; # 是否要電腦有安裝才支援？

# description自動換行？ 建議使用textedit去做
# update斜體字？font-weight的部分
# 圖片是否支援gif?

# 元件內部間距(為了美觀):
margin: 10px;
padding: 10px;

border-radius:
border: 3px solid #0000FF

min-width: 100px;
max-width: 150px;

min-height: 30px;
max-height: 50px;

# 或是直接使用
widget.setFixedWidth(number) #寬
widget.setFixedHeight(number)　#高

# 有想要放圖的話
widget.setStyleSheet(css_content)
background-repeat: no-repeat;
background-position: center;
background-image: url({image_file});

# 設定widget內容的對齊方式
# 不適用於button
widget.setAlignment(align)

align = QtCore.Qt.AlignLeft
align = QtCore.Qt.AlignRight
align = QtCore.Qt.AlignHCenter
align = QtCore.Qt.AlignJustify

# QtCore.Qt.AlignTop
QtCore.Qt.AlignBottom
QtCore.Qt.AlignVCenter
QtCore.Qt.AlignBaseline

# 同時使用時 用|符號連接
QtCore.Qt.AlignHCneter|QtCore.Qt.AlignVCenter

# 將objectName當作ID
css_content = '''
QWidget # AAA
{
	font-size: 16px;
	font-weight: bold;
}'''

widget.setObjectName('AAA')
widget.setStyleSheet(css_content)

# 將Property當作attribute
css_content = '''
QWidget [x='OK']
{
	color: #FF0000;
	font-weight: bold;
}'''

weight.setProperty('X', 'OK')
weight.setStyleSheet(css_content)