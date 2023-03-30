'''19. Write a function that takes two strings representing dates and returns the string

that represents the earliest point in time ? Ex. get_earliest("01/27/1832",

"01/27/1756") return '01/27/1756'.'''

def find_earliest_point(day1,day2):
    month1,date1,year1 = day1.split("/")
    month2,date2,year2 = day2.split("/")
    if (year1==year2) and (month1==month2) and (date1==date2):
        return "both times are equal"
    elif  int(year1) > int(year2):
        return day2
    elif int(month1) < int(month2):
        return day1
    else:
        if int(month1)>int(month2):
            return day2
        elif int(month1)<int(month2):
            return day1
        else:
            if int(date1)>int(date2):
                return day2
            elif int(date1)< int(date2):
                return day1
            

print(find_earliest_point("20/08/1999",'19/08/1999'))
