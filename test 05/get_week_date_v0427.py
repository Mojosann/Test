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
	
	# return resault
	resault = []
	for count in range(7):
		week_name_date = week_name_list[count], week_date_list[count]
		resault.append(week_name_date)

	return resault


def main():

	query_date = '2021-01-01'
	week_date = get_week_date(query_date)
	print('%s week date: %s' % (query_date, week_date))

	query_date = '2021-04-17'
	week_date = get_week_date(query_date)
	print('%s week date: %s' % (query_date, week_date))

	query_date = '2021-07-28'
	week_date = get_week_date(query_date)
	print('%s week date: %s' % (query_date, week_date))

		
if __name__ == '__main__':
	main()