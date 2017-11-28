#-------------------------#
#Program to display calendar
#-------------------------#

import calendar

while True:
	print("Enter 'x' for exit.")
	year = input("Enter Year: ")
	month = input("Enter month: ")
	if year == 'x':
		break
	else:
		Year = int(year)
		Month = int(month)
		print("\n",calendar.month(Year,Month))