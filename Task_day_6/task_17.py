'''17. Write a function that takes a sequence (like a list, string, or tuple) and a number n

and returns the last n elements from the given sequence, as a list. For example:

>>> tail([1, 2, 3, 4, 5], 3)'''

# Approach 1:

def given_list(itarator,n):
    return (itarator[len(itarator)-n:])
# print(given_list([1,2,3,4,5],2))
print(given_list("pavankalyan",8))