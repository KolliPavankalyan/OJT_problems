'''16. Write a function split_in_half that splits a list in half and returns both halves.

split_in_half([1, 2, 3, 4])

([1, 2], [3, 4])'''

def split_in_half(li):
    return li[:int(len(li)/2)],li[int(len(li)/2):]
print(split_in_half([1,2,3,4,5,6,7,8]))


