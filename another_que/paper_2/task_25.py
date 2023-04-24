'''25. Given an Integer n, count the total number of times 1 is appearing in all non-negative integers 
less than or equal to n.'''
num = int(input("enter a number :"))
count = 0

for i  in range(num+1):
    count += str(i).count("1")
print(count)