from datetime import datetime, timedelta

class GetDate:
	def __init__(self, date):
		self.date = date
		self.date = datetime.today().strftime('%Y-%m-%d')
		self.date = datetime.strptime(date,'%Y-%m-%d')

	def get_week_date(self): # monday(isoweekday() == 1
		week_delta_list = []
		for delta in range(8):
			week_delta = self.date.isoweekday() - delta
			week_delta_list.append(week_delta)
	
		week_date_list = []
		for week_delta in week_delta_list:
			week_date = (self.date - timedelta(days = week_delta)).strftime('%Y-%m-%d')
			week_date_list.append(week_date)

		week_name_list = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
		resault = list(zip(week_name_list, week_date_list))
		
		print('query_date: %s, week_date_list: %s' % (self.date, resault))

	def get_monday_date(self):
	
		# search weekday, - monday(isoweekday() == 1)
		delta = self.date.isoweekday() -1 

		# get monday date
		monday_date = (self.date - timedelta(days = delta)).strftime('%Y-%m-%d')

		print('query_date: %s, monday_date: %s' % (self.date, monday_date))


GetDate('2021-01-01').get_week_date()
GetDate('2021-04-06').get_week_date()
GetDate('2021-05-19').get_week_date()

GetDate('2021-01-01').get_monday_date()
GetDate('2021-04-06').get_monday_date()
GetDate('2021-05-19').get_monday_date()