'''17. Define the function which returns the counts of saturdays part of a year (year is an input [Ex: 2022]) '''

#import calendar
import datetime
def find_satdays(year):
    for day in range(1,8):
        date = datetime.date(year, 1, day)
        if date.weekday() == 5: 
            return day
year = int(input("Enter the year"))       
satday = find_satdays(year)


if year%100==0 and year%400==0:
    days = 366
elif year%100!=0 and  year%4==0:
    days = 366
else: 
    days = 365

remaing = ((days-satday)//7)+1
print(remaing)

