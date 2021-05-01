# ver.correct the way of getting Monday's date

from datetime import datetime, timedelta


def get_week_date(date=datetime.today().strftime('%Y-%m-%d')):

	# string translate to date
	date_date = datetime.strptime(date,'%Y-%m-%d')

	# get week_delta list (ex: sunday isoweekday() == 0, ...)
	week_delta_list = []
	for delta in range(7):
		week_delta_list.append(date_date.isoweekday() - delta)
	
	# get week_date list (date - week's delta)
	week_date_list = []
	for date_delta in week_delta_list:
		week_date_list.append((date_date - timedelta(days = date_delta)).strftime('%Y-%m-%d'))

	# set week_name order
	week_name_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']	
	
	# combine week_name / week_date into dict
	resault = {}
	for count in range(7):
		resault[week_name_list[count]] = week_date_list[count]
	return resault


def get_weekday_by_date(date, week_day_name):
	
	# get date's week date dict
	date_dict = get_week_date(date)
	
	# get week day name's date
	if week_day_name in date_dict:
		return date_dict[week_day_name] #str


def get_monday_by_date(date):
	
	# get Monday's date
	monday_date = get_weekday_by_date(date, 'Monday')
	return monday_date


def main():
	
	# example 1
	query_date = '2021-03-08'
	query_week_day_name = 'Sunday'
	weekday = get_weekday_by_date(query_date, query_week_day_name)
	print("%s's %s is %s" % (query_date, query_week_day_name, weekday))
	
	monday = get_monday_by_date(weekday)
	print("%s's Monday is %s" % (weekday, monday))

	# example 2
	query_date = '2021-08-15'
	query_week_day_name = 'Thursday'
	weekday = get_weekday_by_date(query_date, query_week_day_name)
	print("%s's %s is %s" % (query_date, query_week_day_name, weekday))
	
	monday = get_monday_by_date(weekday)
	print("%s's Monday is %s" % (weekday, monday))

	# example 3
	query_date = '2021-04-07'
	query_week_day_name = 'Friday'
	weekday = get_weekday_by_date(query_date, query_week_day_name)
	print("%s's %s is %s" % (query_date, query_week_day_name, weekday))
	
	monday = get_monday_by_date(weekday)
	print("%s's Monday is %s" % (weekday, monday))

if __name__ == '__main__':
	main()