'''10. Write a function combine_lists should take two lists and return a new list
containing all elements from both lists.
'''

def combination_list(list1,list2):
    list1.extend(list2)
    return list1
print(combination_list([1,2,3,4],[5,6,7,8]))