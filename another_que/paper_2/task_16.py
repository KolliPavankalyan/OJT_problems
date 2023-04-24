'''16. Write a function which will take a string argument and reverse the words in the string. For 
example – Input string -- “Hello World”. Output should be “olleH dlroW”.'''
given_string = "Hello World"
e = given_string.split()
for i in e:
    out=[i[::-1] for i in e]
print(" ".join(out))