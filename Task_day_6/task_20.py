'''20. Create a function that determines which day of the month the San Diego Python

meetup should be. It should accept year and month arguments and should return

a datetime.date object representing the day of the month for the meetup.

meetup_date(2012, 3)

datetime.date(2012, 3, 22)'''

import calendar
import datetime

def find_first_thursday(year, month):
    for day in range(1, 32):
            date = datetime.date(year, month, day)
            if date.weekday() == 3: 
                return day

year = 2012
month = 3
date = find_first_thursday(year, month)
print(datetime.date(year,month,(date+(3*7))))

