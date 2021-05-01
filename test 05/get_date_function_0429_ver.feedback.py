# -*- coding:utf-8 -*-
# ver.feedback

from datetime import datetime, timedelta

def get_week_date(date):
	# 如果是get_week_date()執行會出錯: 未給值
	# 如果是get_week_date(date)執行會出錯: date is not defined

	# def get_week_date(date=datetime.today().strftime('%Y-%m-%d')):
	# 特別在date後面加這一串是因為要set default value
	# 如果是get_week_date(date)執行會出錯: date is not defined
	# 如果是get_week_date()執行: 僅顯示完成，會使用今日日期做預設值
	# print(get_week_date()): 會印出今天的日期做成當週的字典
	# print(get_week_date): 印出<function get_week_date at 0x02CD98F0> >因此括號代表的意義是呼叫


	# string translate to date
	date_date = datetime.strptime(date,'%Y-%m-%d')

	# get week_delta list (ex: sunday isoweekday() == 0, ...)
	week_delta_list = []
	for delta in range(7):
		week_delta_list.append(date_date.isoweekday() - delta)
	
	# get week_date list (date - week's delta)
	week_date_list = []
	for date_delta in week_delta_list:
		new_date = (date_date - timedelta(days = date_delta)).strftime('%Y%m%d')
		week_date_list.append(new_date)
		#week_date_list.append((date_date - timedelta(days = date_delta)).strftime('%Y-%m-%d'))

	# set week_name order
	week_name_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']	
	
	# combine week_name / week_date into dict
	resault = {}
	for count in range(7):
		resault[week_name_list[count]] = week_date_list[count]

	return resault
	# 其實也可以同時return value 與 print value
	# 但通常只return value, print多發生在debug印出log紀錄(但最後要收合)
	# 通常更多時候是回傳type
	
	
def get_weekday_by_date(date, week_day_name):
	
	# get date's week date dict
	date_dict = get_week_date(date)
	
	# get week day name's date
	if week_day_name in date_dict:
		week_day_name = date_dict[week_day_name] #str
		return week_day_name


def get_monday_by_date(date):
	
	# translate 'YYYYMMDD' to 'YYYY-MM-DD' (str)
	#new_date = '%s-%s-%s' % (date[:4], date[4:6], date[6:]) > not necessary

	# get Monday's date
	monday_date = get_weekday_by_date(date, 'Monday')
	return monday_date.replace('-', '')


def main():
	
	# example 1
	query_date = '2021-03-08'
	query_week_day_name = 'Sunday'
	weekday = get_weekday_by_date(query_date, query_week_day_name)
	print("%s's %s is %s" % (query_date, query_week_day_name, weekday))
	
	monday = get_monday_by_date(query_date)
	print("%s's Monday is %s" % (query_date, monday))

	# example 2
	query_date = '2021-08-15'
	query_week_day_name = 'Thursday'
	weekday = get_weekday_by_date(query_date, query_week_day_name)
	print("%s's %s is %s" % (query_date, query_week_day_name, weekday))
	
	monday = get_monday_by_date(query_date)
	print("%s's Monday is %s" % (query_date, monday))

	# example 3
	query_date = '2021-04-07'
	query_week_day_name = 'Friday'
	weekday = get_weekday_by_date(query_date, query_week_day_name)
	print("%s's %s is %s" % (query_date, query_week_day_name, weekday))
	
	monday = get_monday_by_date(query_date)
	print("%s's Monday is %s" % (query_date, monday))


def test_func():
	print 'A'

# 比較輸出結果
if __name__ == '__main__':
	# main()

	test_func()
	# A (執行func所以印出A)

	test_func
	# 顯示完成，無回傳值
	
	print(test_func())
	# A, None(印出A與回傳空值)

	print(test_func)
	# 印出func obj名稱: <function test_func at 0x032B9BF0>
	
	a = test_func()
	# A (執行func所以印出a)
	
	print(a)
	# None (因為回傳值為空值)