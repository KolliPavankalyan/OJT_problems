'''1. Write a program in which two strings are given and determine if they share a
common substring. A substring may be as small as one character. The function
returns either “YES” or “NO”.
'''

string = input("Enter a string :")
sub_string = input("enter a sub string :")

def check_string(string,sub_string):
    for i in sub_string:
        if i in string:
            return "Yes"
    return "No"
print(check_string(string,sub_string))
