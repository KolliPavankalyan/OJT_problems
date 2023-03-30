'''17. Write a program to replace duplicate adjacent alphabets from given string with ‘_’.

For Example -- input given string : 'abcdaa hssbbye' and output : ‘abcda_ hs_b_ye’'''

input = "abcdaa *abbcccccddddddddddd hssbbye"
output = input[0]
for i in range(1,len(input)):
    if input[i-1]==input[i]:
        output+="_"
    else:
        output+=input[i]
print(output)


