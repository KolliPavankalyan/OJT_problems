'''3 Define logic for identifying the even numbers and odd numbers from the given list and generate a dictionary as follows 
numbers = [4,5,7,2,9,8] 
result == {"even":[4,2,8],"odd":[5,7,9]} '''


#Approach 1:
def identify_even_and_odd(given_list):
    given_list = [int(i) for i in given_list.split()]
    even = [i for i in given_list if i%2==0]
    odd = [i for i in given_list if i%2!=0]
    dict_a = {'even':even,'odd':odd}
    return dict_a
print(identify_even_and_odd(input("Please enter list of numbers :")))



#Approch 2:
# def identify_even_and_odd(given_list):
#     given_list = [int(i) for i in given_list.split()]
#     even =[]
#     odd = []
#     for i in given_list:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     dict_a = {}
#     dict_a['even']=even
#     dict_a['odd']=odd
#     print(dict_a)


# given_list = input("Enter list of numbers  :")
# identify_even_and_odd(given_list)

# #approch 3:
# given_list = input("Enter list of numbers")
# def identify_even_and_odd(given_list):
#     given_list = [int(i) for i in given_list.split()]
#     dict1 = {"even":[],"odd":[]}
#     for i in given_list:
#         if i%2==0:
#             dict1['even'].append(i)
#         else:
#             dict1['odd'].append(i)
#     return dict1
# print(identify_even_and_odd(given_list))