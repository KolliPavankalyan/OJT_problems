'''2. Define a function which returns a list contains only the palindrome strings from the list of provided string elements 
input: List of strings 
output: List of palindrome strings '''

def palindrome(given_list):
    new_list = []
    for i in given_list:
        if i==i[::-1]:
            new_list.append(i)
    return new_list
print(palindrome(["cac","tac","liriL","ata","malayalam"]))
