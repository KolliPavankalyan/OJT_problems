'''16. Write a function split_in_half that splits a list in half and returns both halves.
>>> split_in_half([1, 2, 3, 4])
([1, 2], [3, 4])
'''

list_a = [1,2,3,4]
print((list_a[:len(list_a)//2], list_a[len(list_a)//2:]))