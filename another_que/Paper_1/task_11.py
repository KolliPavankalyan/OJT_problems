'''11. Rewrite the program to get proper output
Match = 'version'
input=8
print(Match+input)'''

match = "version"
input = 8

print(match+" "+str(input))



#Approch 2:
match = "version"
input = 8
print("{} {}".format(match,input))

#Aproch 3;
match = "version"
input = 8
print(f"{match} {input}")