'''11. Write a python function with name reverse_vowel that takes one string as an argument and 
reverse the order of vowels present in the string. The function should return the string having 
reversed order of vowels. For example – If the input string which is given as argument is ‘Hello’ 
then the output string should be ‘Holle’. You need to reverse the vowel irrespective of lowercase or 
uppercase.'''

string = "Hello"
vowels = ['A','E','I','O','U','a','e','i','o','u']
find_vowels = []
for i in string:
    if i in vowels:
        find_vowels.append(i)

find_vowels[::-1]
count =0
for i in string:
    if i in vowels:
        string.replace(i,find_vowels[count])
        print(string)
        count+=1
print(string)