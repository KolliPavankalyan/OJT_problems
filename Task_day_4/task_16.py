'''16. Write a function which will take a string argument and reverse the words in the string. For

example – Input string -- “Hello World”. Output should be “olleH dlroW”.'''


def reverse(string):
    string_list = string.split()
    new_list = [i[::-1] for i in string_list]
    final_out = " ".join(new_list)
    return final_out

print(reverse("Hello World pavan kalyan **+ "))