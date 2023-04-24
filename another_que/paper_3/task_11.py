'''12. Write a function called parse_ranges, which accepts a string containing ranges of
numbers and returns an iterable of those numbers.
Ex: >>> parse_ranges('1-2,4-4,8-13')
[1, 2, 4, 8, 9, 10, 11, 12, 13]
'''
string = "1-2,4-4,8-13"
nums = [[int(j) for j in i.split("-")]for i in string.split(",")]
new_list = []
for i in nums:
    count = i[0]
    while count<=i[1]:
        new_list.append(count)
        count+=1
print(new_list)




