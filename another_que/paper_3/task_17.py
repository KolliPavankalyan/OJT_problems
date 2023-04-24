'''17. Write a function that takes a sequence (like a list, string, or tuple) and a number n
and returns the last n elements from the given sequence, as a list. For example:
>>> tail([1, 2, 3, 4, 5], 3)
[3, 4, 5]
'''

list_a = [1,2,3,4,5]
num = int(input("enter rotaion number  :"))
num = num%len(list_a)
print(list_a[len(list_a)-num:])