# 3. Given a tuple (“Msys”, “Technologies”, “2007”), add “Python” at the end of this tuple and the

# output should also be in the form of tuple. Make a note that tuples are immutable in nature so you

# need to find some idea to make modification and print the updated tuple.



# Approch 1:

given_tuple = ("Msys", "Technologies","2007")
con_list = list(given_tuple)
con_list.append("Python")
given_tuple = tuple(con_list)
print(given_tuple)

# Approch 2:

given_tuple = ("Msys", "Technologies","2007")
new_tuple = given_tuple + ("Python",)
print(new_tuple)

