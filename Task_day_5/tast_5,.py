'''5. Write a function that accepts an iterable and returns a new iterable with all items from the original iterable except for duplicates. Ex. uniques_only([1, 2, 2, 1, 1, 3, 2, 1]) [1, 2, 3]'''

#Approch 1
# def duplicates(iterable):
#     set_a = set(iterable)
#     list_a = list(set_a)
#     print(list_a)

# duplicates([1, 2, 2, 1, 1, 3, 4,5,9,11,1,2,4,1,55,5,5,55,5,2, 1])



#Approch 2:

def duplicates(given_list):
    new_list = [int(i) for i in given_list.split()]
    uniq_elements = []
    for i in new_list:
        if i not in uniq_elements:
            uniq_elements.append(i)
    return uniq_elements

given_list = input("Enter the list :")
print(duplicates(given_list))
