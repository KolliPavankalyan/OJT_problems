'''23. Print the following pattern :
            *
           *-*
          *---*
         *-----*
        *-------*
'''


no_of_line = int(input("Enter a number : "))
spaces = " "
print(spaces*no_of_line+"*")
underscore_count = 1
for i in range(1,no_of_line+1):
    print((spaces*(no_of_line-i))+"*"+(underscore_count*"-")+"*")
    underscore_count+=2


