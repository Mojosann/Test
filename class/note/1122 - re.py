# [re (regular expression)]

import re
# 嘗試取得v02的資訊
# v:有v這個字; \d = 數字; +代表一個數字以上
# re.search(pattern, target_string)
re_resault = re.search('v\d+', 'td_sq0010_sh0010_lighting_v02.ma')

# 若re無法依照條件search到結果 則為None:
if re_resault != None:
	# 透過group()的function將search的資訊取回
	print(re_resault.group())

# 使用re.findall直接回傳list的結果 若無法取得則回傳空list
re_list = re.findall('v\d+.ma$', 'td_sq0010_sh0010_lighting_v02.ma')
print(re_list)

# [Metacharacters of re: ^$.+*?()[]{}\]
# 要判斷開頭結尾可以使用string.startswith('') or endswith('')
pattern = '^TD' # 字串開頭必須為TD
pattern = 'ma$' # 字串結尾必須為ma
pattern = '[0-9]' # []框住0-9任何數字 也可以a~z但只會找到一個
pattern = '[0-9]*' # ..0個或以上
pattern = '[0-9]+' # ..1個或以上
pattern = '[0-9]?' # ..0個或1個
pattern = '^[0-9]$' # 頭尾只允許一個數字

test = 'TD_test.ma'
test = 'TD_test1.ma'
test = 'TD_test23.ma'
test = '123456'

# 試試只允許數字的pattern
re_resault = re.search('^[0-9]+$', test)
if re_resault != None:
	print(re_resault.group())

pattern = '.' # 任何一個字元(除了\n)
pattern = '[A|B].+' # A或B的甚麼甚麼 有符合皆可 其他都不要
pattern = '[0-9]{3}' # 3個數字

# 將條件符合的另外一個做gruop
# ()代表group
pattern = 'v([0-9]{3})' # 可以只取數字不取v: group(1)
# 不包含0-9的...
pattern = '[^0-9]+'

test = 'A001_B102_21122'
test = 'A001B102_21122'
test = 'A001_B102_v21122'

re_resault = re.search('v([0-9]{6})', test)
if re_resault != None:
	print(re_resault.group())
	print(int(re_resault.group(1)))

# [Practice]
pattern = '^TD.+v([0-9]+).ma$'
test = 'TW_char_pan_mod_v001.mb'
test = 'TD_char_pan_mod_v002.ma'

re_resault = re.search(pattern, test)
if re_resault != None:
	print(re_resault.group())


# 練習取得version number: 數字only
# [Practice]
file_name = 'td_sq0010_sh0010_lighting_v02.ma'
file_name = 'cx9_sq0130_sh0090_lighting.v003.ma'
file_name = 'pro_sq0010_sh0010_lighting_pan.v07.ma'
file_name = 'RAN_AM0_010_LIGHT_V015.ma'

pattern = 'v([0-9]+)'

re_resault = re.search(pattern, file_name, re.IGNORECASE)
if re_resault != None:
	print(re_resault.group(1))

# [Practice 02]
pattern = '[V|v]([0-9]+)'
file_name = 'RAN_AM0_010_LIGHT_V015.ma'

re_resault = re.search(pattern, file_name)
if re_resault != None:
	print(re_resault.group(1))

# 忽略大小寫
re.search(pattern, file_name, re.IGNORECASE)

# [Practice 03]
file_name = 'RAN_AM0_010_LIGHT_V015.ma'
pattern = '_V([0-9]+)'

# method 1
re_resault = re.search(pattern, file_name)
if re_resault != None:
	print(re_resault.group(1))

# method 2
pattern = '_V([0-9]+)'
re_list = re.findall(pattern, file_name)
print(re_list[1])