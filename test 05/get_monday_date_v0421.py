from datetime import datetime, timedelta

def get_monday_date(date=datetime.today().strftime('%Y-%m-%d')):
	
	# string translate to date
	date_date = datetime.strptime(date,'%Y-%m-%d')

	# search weekday, get delta (monday isoweekday() == 1)
	delta = date_date.isoweekday() - 1

	# get monday date
	resault = date_date - timedelta(days = delta)
	resault = resault.strftime('%Y-%m-%d')

	return resault

def main():

	query_date = '2021-01-01'
	monday = get_monday_date(query_date)
	print(query_date, 'monday is', monday)

	query_date = '2021-04-17'
	monday = get_monday_date(query_date)
	print(query_date, 'monday is', monday)

	query_date = '2021-07-18'
	monday = get_monday_date(query_date)
	print(query_date, 'monday is', monday)

	
if __name__ == '__main__':
	main()