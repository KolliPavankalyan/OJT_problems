'''21. You are given a string and width. Your task is to wrap the string into paragraph of width in 
reverse order. Blank spaces should be ignored.
for eg: i/p - first line contains a string with blank spaces - Hello, welcome to this 
organisation.
 the second line conatins the width - 4
 o/p
lleH
ew,o
mocl
tote
osih
nagr
tasi
.noi'''
string = "Hello, welcome to this organisation."
string = string.replace(" ","")
k = int(input("Enter number of chars  :"))
for i in range(0,len(string)-1,k):
    print(string[i:i+k][::-1])