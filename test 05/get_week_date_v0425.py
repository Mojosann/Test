from datetime import datetime, timedelta

# string translate to date
def get_date(date=datetime.today().strftime('%Y-%m-%d')):

	date_date = datetime.strptime(date,'%Y-%m-%d')
	return date_date


def get_week_delta(date): # monday(isoweekday() == 1)
	
	week_delta_list = []
	for delta in range(7):
		week_delta = date.isoweekday() - delta
		week_delta_list.append(week_delta)
	
	return week_delta_list


def get_week_date(date, week_delta_list):

	week_date_list = []
	for week_delta in week_delta_list:
		week_date = (date - timedelta(days = week_delta)).strftime('%Y-%m-%d')
		week_date_list.append(week_date)

	return week_date_list


def week_date_list(week_date_list):
	week_name_list = ['日', '一', '二', '三', '四', '五', '六']
	resault = list(zip(week_name_list, week_date_list))
	
	return resault


def main():
	date1 = get_date('2021-01-01')
	week_delta_list1 = get_week_delta(date1)
	weekday1 = get_week_date(date1, week_delta_list1)
	resault = week_date_list(weekday1)
	print(resault)

if __name__ == '__main__':
	main()