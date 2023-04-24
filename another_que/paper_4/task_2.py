'''2. Define a function which returns a list contains only the palindrome strings from the list of provided string elements 
input: List of strings 
output: List of palindrome strings'''


list1 = ['cac','tac','malayalam']
for i,v in enumerate(list1):
    if v!=v[::-1]:
        list1.pop(i)
print(list1)