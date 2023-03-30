'''20. You are given a string having alphabets,digits,special characters. Write three different functions

to extract the digits[should be in sorted order], special character & vowels[should be in reverse]

from the given string.

i/p string : "abcd123bye09@8"

o/p: digits - 012389

special character - @

vowels - ea'''


given_string = input("please enter string contains :")


def digit(given_string):
    digits = ""
    for i in given_string:
        if i.isdigit():
            digits += i
    return "".join((sorted(digits)))

def vowel(given_string):
    
    vowels = ""
    for i in given_string:
        if i in ["a","e","i","o","u"]:
            vowels+=i
    return vowels[::-1]

def special_characters(given_string):
    special_character = ""
    for i in given_string:
        if not i.isalnum():
            special_character+=i
    return special_character[::-1]

print("digits -", digit(given_string))
print("vowels -",vowel(given_string))
print("special character -",special_characters(given_string))


