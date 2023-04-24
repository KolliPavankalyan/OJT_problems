'''9. Create a function is_leap_year that accepts a year and returns True if (and only
if) the given year is a leap year.
'''
def find_leap_year(year):
    if year%100==0 and year%400==0:
        return True
    elif year %100 !=0 and year%4==0:
        return True
    return False
print(find_leap_year(1900))