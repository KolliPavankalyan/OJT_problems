'''22. Write a function where month and year are taken as arguments which returns the output
with all the dates of saturdays occuring the month'''

year = int(input("Please enter year  :"))
month = int(input("please enter month  :"))
def sat(year,month):
    for i in range(0,31):
        