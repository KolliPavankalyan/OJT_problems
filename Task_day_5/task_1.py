'''1. Write a program in which two strings are given and determine if they share a common substring. A substring may be as small as one character. The function returns either “YES” or “NO”.'''



# Approach 1:
def check_substring(string1, string2):
    for i in string1:
        if i in string2:
            return "YES"
    return "NO"
string1 = input("Enter a string1  :")
string2 = input("Enter a string2  :")
print(check_substring(string1,string2))



#Approach 2:
# def check_Sub_String(string,substring):
#     if substring in string:
#         return "YES"
#     else:
#         return "NO"
# string = input("Enter a string  :")
# substring = input("Enter a substring  :")
# print(check_Sub_String(string,substring))

